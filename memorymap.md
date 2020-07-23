#   Memory Map
#### Memory Map
```
  KUSEG     KSEG0     KSEG1
  00000000h 80000000h A0000000h  2048K  Main RAM (first 64K reserved for BIOS)
  1F000000h 9F000000h BF000000h  8192K  Expansion Region 1 (ROM/RAM)
  1F800000h 9F800000h    --      1K     Scratchpad (D-Cache used as Fast RAM)
  1F801000h 9F801000h BF801000h  8K     I/O Ports
  1F802000h 9F802000h BF802000h  8K     Expansion Region 2 (I/O Ports)
  1FA00000h 9FA00000h BFA00000h  2048K  Expansion Region 3 (whatever purpose)
  1FC00000h 9FC00000h BFC00000h  512K   BIOS ROM (Kernel) (4096K max)
        FFFE0000h (KSEG2)        0.5K   I/O Ports (Cache Control)
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
  Address   Name   Size   Privilege    Code-Cache  Data-Cache
  00000000h KUSEG  2048M  Kernel/User  Yes         (Scratchpad)
  80000000h KSEG0  512M   Kernel       Yes         (Scratchpad)
  A0000000h KSEG1  512M   Kernel       No          No
  C0000000h KSEG2  1024M  Kernel       (No code)   No
```
Kernel Memory: KSEG1 is the normal physical memory (uncached), KSEG0 is a
mirror thereof (but with cache enabled). KSEG2 is usually intended to contain
virtual kernel memory, in the PSX it's containing Cache Control I/O Ports.<br/>
User Memory: KUSEG is intended to contain 2GB virtual memory (on extended MIPS
processors), the PSX doesn't support virtual memory, and KUSEG simply contains
a mirror of KSEG0/KSEG1 (in the first 512MB) (trying to access memory in the
remaining 1.5GB causes an exception).<br/>

#### Code Cache
Works in the cached regions (KUSEG and KSEG0).<br/>
There are reportedly some restrictions... not sure there... eventually it is
using the LSBs of the address as cache-line number... so, for example, it
couldn't simultaneously memorize opcodes at BOTH address 80001234h, AND at
address 800F1234h (?)<br/>

#### Data Cache aka Scratchpad
The MIPS CPU usually have a Data Cache, but, in the PSX, Sony has misused it as
"Scratchpad", that is, the "Data Cache" is mapped to a fixed memory location at
1F800000h..1F8003FFh (ie. it's used as Fast RAM, rather than as cache).<br/>
There \<might\> be a way to disable that behaviour (via Port FFFE0130h or
so), but, the Kernel is accessing I/O ports via KUSEG, so activating Data Cache
would cause the Kernel to access cached I/O ports.<br/>
Not tested yet, but most probably the Scratchpad can be used only for Data (ie.
NOT for program Code?).<br/>

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

#### More Memory Info
For Info on Exception vectors, Unused/Garbage memory locations, I/O Ports,
Expansion ROM Headers, and Memory Waitstate Control, etc. see:<br/>
[I/O Map](iomap.md)<br/>
[Memory Control](memorycontrol.md)<br/>
[EXP1 Expansion ROM Header](expansionportpio.md#exp1-expansion-rom-header)<br/>
[BIOS Memory Map](kernelbios.md#bios-memory-map)<br/>
[BIOS Memory Allocation](kernelbios.md#bios-memory-allocation)<br/>
[COP0 - Exception Handling](cpuspecifications.md#cop0---exception-handling)<br/>
[Unpredictable Things](unpredictablethings.md)<br/>



