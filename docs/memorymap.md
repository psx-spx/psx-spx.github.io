#   Memory Map
#### Memory Map
```
  KUSEG     KSEG0     KSEG1
  00000000h 80000000h A0000000h  2048K  Main RAM (first 64K reserved for BIOS)
  1F000000h 9F000000h BF000000h  8192K  Expansion Region 1 (ROM/RAM)
  1F800000h 9F800000h    --      1K     Scratchpad (D-Cache used as Fast RAM)
  1F801000h 9F801000h BF801000h  4K     I/O Ports
  1F802000h 9F802000h BF802000h  8K     Expansion Region 2 (I/O Ports)
  1FA00000h 9FA00000h BFA00000h  2048K  Expansion Region 3 (SRAM BIOS region for DTL cards)
  1FC00000h 9FC00000h BFC00000h  512K   BIOS ROM (Kernel) (4096K max)
        FFFE0000h (in KSEG2)     0.5K   Internal CPU control registers (Cache Control)
```
Additionally, there are a number of memory mirrors.<br/>

#### Additional Memory (not mapped to the CPU bus)
```
  1024K   VRAM (Framebuffers, Textures, Palettes) (with 2KB Texture Cache)
  512K    Sound RAM (Capture Buffers, ADPCM Data, Reverb Workspace)
  0.5K    CDROM controller RAM (see CDROM Test commands)
  16.5K   CDROM controller ROM (Firmware and Bootstrap for MC68HC05 cpu)
  32K     CDROM Buffer (IC303) (32Kx8) (BUG: only two sectors accessible?)
  128K    External Memory Card(s) (EEPROMs)
```

#### KUSEG,KSEG0,KSEG1,KSEG2 Memory Regions
```
  Address   Name   i-Cache     Write-Queue
  00000000h KUSEG  Yes         Yes
  80000000h KSEG0  Yes         Yes
  A0000000h KSEG1  No          No
  C0000000h KSEG2  (No code)   No
```
Kernel Memory: KSEG1 is the normal physical memory (uncached), KSEG0 is a
mirror thereof (but with cache enabled). KSEG2 is usually intended to contain
virtual kernel memory, but in the PSX it's containing Cache Control hardware registers.<br/>
User Memory: KUSEG is intended to contain 2GB virtual memory (on extended MIPS
processors), the PSX doesn't support virtual memory, and KUSEG simply contains
a mirror of KSEG0/KSEG1 (in the first 512MB) (trying to access memory in the
remaining 1.5GB causes an exception).<br/>

#### i-Cache
The i-Cache can hold 4096 bytes, or 1024 instructions.<br/>
It is only active in the cached regions (KUSEG and KSEG0).<br/>
There are reportedly some restrictions... not sure there... eventually it is
using the LSBs of the address as cache-line number... so, for example, it
couldn't simultaneously memorize opcodes at BOTH address 80001234h, AND at
address 800F1234h (?)<br/>

#### Scratchpad
MIPS CPUs usually have a d-Cache, but, in the PSX, Sony has assigned it as
what's referenced as the "Scratchpad",  mapped to a fixed memory location at
1F800000h..1F8003FFh, ie. it's used as Fast RAM, rather than as cache.<br/>
There \<might\> be a way to disable that behavior (via Port FFFE0130h or
so), but, the Kernel is accessing I/O ports via KUSEG, so activating Data Cache
would cause the Kernel to access cached I/O ports.<br/>
The purpose of the scratchpad is to have a more flexible cache system available
to the programmer. Neither the kernel nor the Sony libraries will try to make use
of it, so it is therefore completely up for grabs to the programmer. A good example
would be if you were to write a piece of code that's doing a lot of CRC computation,
to use the 1KB scratchpad to initially load the CRC lookup tables, which incidentally,
is exactly 1KB large. Doing this will speed up reads from the lookup table,
while also keeping the whole CRC code in the i-Cache, hence being more optimal than 
what you'd get with an automatic d-Cache system where parts of the table would be evicted
while reading the data to compute the CRC of. Unlike an automatic d-Cache system however, 
there is no row burst reads, so memory throughput is still much lower than if a d-Cache was present.<br/>
Note that the scratchpad is NOT executable. Attempts to jump to this region will cause
a bus error on the first instruction fetch. Attemping to force the scratchpad to be 
executable using the bit 17 "Swap cache mode" in cop0 r12/SR do not work, and 
a bus error will still occur.<br/>

#### Memory Mirrors
As described above, the 512Mbyte KUSEG, KSEG0, and KSEG1 regions are mirrors of
each other. Additional mirrors within these 512MB regions are:<br/>
```
  2MB RAM can be mirrored to the first 8MB (strangely, enabled by default)
  512K BIOS ROM can be mirrored to the last 4MB (disabled by default)
  Expansion hardware (if any) may be mirrored within expansion region
  The seven DMA Control Registers at 1F8010x8h are mirrored to 1F8010xCh
```
The size of the RAM, BIOS, Expansion regions can be configured by software, for
Expansion Region it's also possible to change base address, see:<br/>
[Memory Control](memorycontrol.md)<br/>
The Scratchpad is mirrored only in KUSEG and KSEG0, but not in KSEG1.<br/>

#### Memory Exceptions
```
  Memory Error ------> Misalignments
               (and probably also KSEG access in User mode)
  Bus Error    ------> Unused Memory Regions (including Gaps in I/O Region)
               (unless RAM/BIOS/Expansion mirrors are mapped to "unused" area)
```

#### Write queue
The MIPS CPU has a 4-words deep pass-through write queue, in order to relieve
some bus contention when writing to memory. If reading the same memory location
that just got written into the write queue, it will first be flushed before
being read back from memory.<br/>
It is important to realize that the write queue's mechanism is only viable for
normal memory attached to the main CPU, and that any hardware register state machine
will get messed up by it.<br/>
The typical example is the typical JEDEC standard to access flash, which usually does
the following sequence to read the ID of a flash chip:
```C
    base[0xAAA] = 0xAA;
    base[0x555] = 0x55;
    base[0xAAA] = 0x90;
    uint8_t mnfctrID = base[0x000];
    uint8_t deviceId = base[0x002];
```

In this example above, if `base` is located in a memory segment that has the write queue
enabled, even if the low level assembly code will do the first 3 stores before doing 2 loads,
the physical signals sent to that device through the CPU bus will be seen in the sequence:
```
store(0xaaa, 0xaa)
load(0x000)
store(0x555, 0x55)
load(0x002)
store(0xaaa, 0x90)
```

Therefore, using KSEG1 that disables the write queue is the only way to ensure that the
operations are done in the proper way.

The above is valid for most of the hardware connected to the main CPU, such as the CDROM
controller, exp1, exp2, the SPU, or the GPU. Therefore, using BF80180xh to access the
CDROM registers is more correct than using 1F80180xh.

It is noteworthy that the Sony code will still incorrectly use KUSEG as the memory map
for all hardware registers, and they then spend a lot of time writing 4 dummy values
somewhere, in order to ensure the write queue has been flushed.

The SN debugger in contrast is properly using the KSEG1 memory map for all the hardware
registers, nullifying the need to flush the write queue when accessing it.

It's also noteworthy that doing ANY KSEG1 access (read OR write) will automatically stall
the CPU in order to flush the whole write queue before proceeding with the operation.
Therefore, all BIOS ROM operations will naturally and effectively have the write queue
disabled, as this code requires the CPU to read from KSEG1 constantly.

This also means that if using KUSEG for the hardware registers, another method to flush
the write queue, albeit potentially slightly less efficient, would be to simply read
the first byte located at BFC00000h. The latter is what is effectively described as the
official method to flush the write queue in the MIPS handbook. This could be potentially
useful to flush the write queue all at once, instead of flushing it word by word.

#### More Memory Info
For Info on Exception vectors, Unused/Garbage memory locations, I/O Ports,
Expansion ROM Headers, and Memory Waitstate Control, etc. see:<br/>
[I/O Map](iomap.md)<br/>
[Memory Control](memorycontrol.md)<br/>
[EXP1 Expansion ROM Header](expansionportpio.md#exp1-expansion-rom-header)<br/>
[BIOS Memory Map](kernelbios.md#bios-memory-map)<br/>
[BIOS Memory Allocation](kernelbios.md#bios-memory-allocation)<br/>
[COP0 - Exception Handling](cpuspecifications.md#cop0-exception-handling)<br/>
[Unpredictable Things](unpredictablethings.md)<br/>
