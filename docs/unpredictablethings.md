#   Unpredictable Things
Normally, I/O ports should be accessed only at their corresponding size (ie.
16bit read/write for 16bit ports), and of course, only existing memory and I/O
addresses should be used. When not recursing that rules, some more or less
(un-)predictable things may happen...<br/>

#### I/O Write Datasize
```
  Address               Content         W.8bit  W.16bit W.32bit
  00000000h-00xFFFFFh   Main RAM        OK      OK      OK
  1F800000h-1F8003FFh   Scratchpad      OK      OK      OK
  1F801000h-1F801023h   MEMCTRL         (w32)   (w32)   OK
  1F80104xh             JOY_xxx         (w16)   OK      CROP
  1F80105xh             SIO_xxx         (w16)   OK      CROP
  1F801060h-1F801063h   RAM_SIZE        (w32)   (w32)   OK        (with crash)
  1F801070h-1F801077h   IRQCTRL         (w32)   (w32)   OK
  1F8010x0h-1F8010x3h   DMAx.ADDR       (w32)   (w32)   OK
  1F8010x4h-1F8010x7h   DMAx.LEN        OK      OK      OK
  1F8010x8h-1F8010xFh   DMAx.CTRL/MIRR  (w32)   (w32)   OK
  1F8010F0h-1F8010F7h   DMA.DPCR/DICR   (w32)   (w32)   OK
  1F8010F8h-1F8010FFh   DMA.unknown     IGNORE  IGNORE  IGNORE
  1F801100h-1F80110Bh   Timer 0         (w32)   (w32)   OK
  1F801110h-1F80110Bh   Timer 1         (w32)   (w32)   OK
  1F801120h-1F80110Bh   Timer 2         (w32)   (w32)   OK
  1F801800h-1F801803h   CDROM           OK      ?       ?
  1F801810h-1F801813h   GPU.GP0         ?       ?       OK
  1F801814h-1F801817h   GPU.GP1         ?       ?       OK
  1F801820h-1F801823h   MDEC.CMD/DTA    ?       ?       OK
  1F801824h-1F801827h   MDEC.CTRL       ?       ?       OK
  1F801C00h-1F801E7Fh   SPU             (i16)   OK      OK
  1F801E80h-1F801FFFh   SPU.UNUSED      IGNORE  IGNORE  IGNORE
  1F802020h-1F80202Fh   DUART           OK      ?       ?
  1F802041h             POST            OK      ?       ?
  FFFE0130h-FFFE0133h   CACHE.CTRL      (i32)   (i32)   OK
```
Whereas,<br/>
```
  OK    works
  (w32) write full 32bits (left-shifted if address isn't word-aligned)
  (w16) write full 16bits (left-shifted if address isn't halfword-aligned)
  (i32) write full 32bits (ignored if address isn't word-aligned)
  (i16) write full 16bits (ignored if address isn't halfword-aligned)
  CROP  write only lower 16bit (and leave upper 16bit unchanged)
```
It's somewhat "legit" to use 16bit writes on 16bit registers like RAM\_SIZE,
I\_STAT, I\_MASK, and Timer 0-2.<br/>
Non-4-byte aligned 8bit/16bit writes to RAM\_SIZE do crash (probably because the
"(w32)" effect is left-shifting the value, so lower 8bit become zero).<br/>
Results on unaligned I/O port writes (via SWL/SWR opcodes) are unknown.<br/>

#### I/O Read Datasize
In most cases, I/O ports can be read in 8bit, 16bit, or 32bit units, regardless
of their size, among others allowing to read two 16bit ports at once with a
single 32bit read. If there's only one 16bit port within a 32bit region, then
32bit reads often return garbage in the unused 16bits. Also, 8bit or 16bit VRAM
data reads via GPUREAD probably won't work? Expansion 2 Region can be accessed
only via 8bit reads, and 16bit/32bit reads seem to cause exceptions (or rather:
no such exception!) (except, probably 16bit reads are allowed when the region
is configured to 16bit databus width).<br/>
There are at least some special cases:<br/>
```
  FFFE0130h-FFFE0133h  8bit (+16bit?) read works ONLY from word-aligned address
```

#### Cache Problems
The functionality of the Cache is still widely unknown. Not sure if DMA
transfers are updating or invalidating cache. Cached Data within KSEG0 should
be automatically also cached at the corresponding mirrored address in KUSEG and
vice versa. Mirrors within KSEG1 (or within KUSEG) may be a different thing,
eg. when using addresses spead across the first 8MB region to access the 2MB
RAM. Same problems may occor for Expansion and BIOS mirrors, although, not sure
if that regions are cached.<br/>

#### Writebuffer Problems
The writebuffer seems to be disabled for the normal I/O area at 1F801000h,
however, it appears to be enabled for the Expansion I/O region at 1F802000h
(after writing to 1F802041h, the BIOS issues 4 dummy writes to RAM, apparently
(?) in order to flush the writebuffer). The same might apply for Expansion
Memory region at 1F000000h, although usually that region would contain ROM, so
it'd be don't care whether it is write-buffered or not.<br/>

#### CPU Load/Store Problems
XXcpuREG ---\> applies ONLY to LOAD (not to store)<br/>
Memory read/write opcodes take a 1-cycle delay until the data arrives at the
destination, ie. the next opcode should not use the destination register (or
more unlikely, the destination memory location) as source operand. Usually,
when trying to do so, the second opcode would receive the OLD value - however,
if an exception occurs between the two opcodes, then the read/write operation
may finish, and the second opcode would probably receive the NEW value.<br/>

#### CPU Register Problems - R1 (AT), R26 (K0), R29 (SP)
Exception handlers cannot preserve all registers, before returning, they must
load the return address into a general purpose register (conventionally R26 aka
K0), so be careful not to use that register, unless you are 100% sure that no
interrupts and no other exceptions can occur. Some exception handlers might
also destroy R27 aka K1 (though execption handler in the PSX Kernel leaves that
register unchanged).<br/>
Some assemblers (not a22i in nocash syntax mode) are internally using R1 aka AT
as scratch register for some pseudo opcodes, including for a "sw rx,imm32"
pseudo opcode (which is nearly impossible to separate from the normal "sw
rx,imm16" opcode), be careful not to use R1, unless you can trust your
assembler not to destroy that register behind your back.<br/>
The PSX Kernel uses "Full-Decrementing-Wasted-Stack", where "Wasted" means that
when calling a sub-function with N parameters, then the caller must
pre-allocate N works on stack, and the sub-function may freely use and destroy
these words; at [SP+0..N\*4-1].<br/>

#### Locked Locations in Memory and I/O Area
```
  00800000h           ;-when Main RAM configured to end at 7FFFFFh
  1F080000h 780000h   ;-when Expansion 1 configured to end at 7FFFFh
  1F800400h C00h      ;-region after Scratchpad
  1F801024h 1Ch       ;\
  1F801064h 0Ch       ;
  1F801078h 08h       ;
  1F801140h 6C0h      ; gaps in I/O region
  1F801804h 0Ch       ;
  1F801818h 08h       ;
  1F801828h 3D8h      ;/
  1F802080h 3FDF80h   ;-when Expansion 2 configured to end at 7Fh
  1FC80000h 60380000h ;-when BIOS ROM configured to end at 7FFFFh
  C0000000h 1FFE0000h ;\
  FFFE0020h E0h       ; gaps in KSEG2 (cache control region)
  FFFE0140h 1FEC0h    ;/
```
Trying to access these locations generates an exception. For KSEG0 and KSEG1,
locked regions are same as for first 512MB of KUSEG.<br/>

#### Mirrors in I/O Area
```
  1F80108Ch+N*10h - D#_CHCR Mirrors - (N=0..6, for DMA channel 0..6)
```
Read/writeable mirrors of DMA Control registers at 1F801088h+N\*10h.<br/>

#### Garbage Locations in I/O Area
```
  1F801062h (2 bytes)  ;\
  1F801072h (2 bytes)  ; unused addresses in Memory and Interrupt Control area
  1F801076h (2 bytes)  ;/
  1F801102h (2 bytes)  ;\
  1F801106h (2 bytes)  ; unused addresses in Timer 0 area
  1F80110Ah (6 bytes)  ;/
  1F801112h (2 bytes)  ;\
  1F801116h (2 bytes)  ; unused addresses in Timer 1 area
  1F80111Ah (6 bytes)  ;/
  1F801122h (2 bytes)  ;\
  1F801126h (2 bytes)  ; unused addresses in Timer 2 area and next some bytes
  1F80112Ah (22 bytes) ;/
  1F801820h (4 bytes)  ;-read MDEC Data-Out port (if there is no data)
  FFFE0000h (32 bytes) ;\
  FFFE0100h (48 bytes) ; unused addresses in Cache control area
  FFFE0132h (2 bytes)  ; (including write-only upper 16bit of Port FFFE0130h)
  FFFE0134h (12 bytes) ;/
```
Unlike all other unused I/O addresses, these addresses are unlocked (ie. they
do not trigger exceptions on access), however they do not seem to contain
anything useful. The BIOS never seems to use them. Writing any values to them
seems to have no effect. And reading acts somewhat unstable:<br/>
Usually returns zeros in most cases. Except that, the first byte on a 10h-byte
boundary often returns the lower 8bit of the memory address (eg.
[FFFE0010h]=10h). And, when [FFFE0130h].Bit11=0, then reading from these
registers does return the 32bit opcode that is to be executed next (or at some
locations, the opcode thereafter).<br/>

#### PSX as Abbreviation for Playstation 1
In gaming and programming scene, "PSX" is most commonly used as abbreviation
for the original Playstation series (occasionally including PSone). Sony has
never officially used that abbreviation, however, the Playstation BIOS contains
the ASCII strings "PSX" and "PS-X" here and there. The letters "PS" are widely
believed to stand for PlayStation, and the meaning of the "X" is totally
unknown (although, actually it may stand for POSIX.1, see below).<br/>

#### PSX as Abbreviation for POSIX.1
According to JMI Software Systems, "PSX" is a trademark of themselves, and
stands for "single-user, single-group, subset of POSIX.1" (POSIX stands for
something commonly used by HLL programmers under UNIX or so). That "PSX" kernel
from JMI is available for various processors, including MIPS processors, and
like the playstation, it does include functions like "atoi", and does support
TTY access via Signetics 2681 DUART chips. The DTL-H2000 does also have
POSIX-style "PSX\>" prompt. So, altogether, it's quite possible that Sony has
licensed the kernel from JMI.<br/>

#### PSX as Abbreviation for an Extended Playstation 2
As everybody agrees, PSX should be used only as abbreviation for Playstation 1,
and nobody should never ever use it for the Playstation 2. Well, nobody, except
Sony... despite of the common use as abbreviation for Playstation 1 (and
despite of the JMI trademark)... in 2003, Sony has have released a "Playstation
2 with built-in HDD/DVD Videorecorder" and called that thing "PSX" for the best
of confusion.<br/>
