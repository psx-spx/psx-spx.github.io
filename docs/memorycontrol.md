#   Memory Control
The Memory Control registers are initialized by the BIOS, and, normally
software doesn't need to change that settings. Some registers are useful for
expansion hardware (allowing to increase the memory size and bus width).<br/>

#### 1F801000h - Expansion 1 Base Address (usually 1F000000h)
```
  0-23   Base address       (R/W)
  24-31  Fixed, always 1Fh  (R)
```
The behavior of this register is somewhat inconsistent. Normally, the base
address is forcefully aligned to the EXP1 region's size by masking off the
bottommost N bits (where N = number of address lines, as set in register
1F801008h). For instance, if the number of EXP1 address lines is set to 8,
setting this register to 1F000000h or 1F0000FFh has the same effect.<br/>
When performing a PIO DMA transfer, however, all bits of this register are
output on the bus regardless of the currently set region size. The System 573
relies on this behavior as it changes the base address to 1F480000h prior to
reading data from the IDE CD-ROM using DMA (and does not reset it to 1F000000h
afterwards).<br/>
Note: presumably the masking lets the bus interface compute addresses quickly by
replacing masked off bits with the LSBs of the incoming address value from the
CPU, thus only requiring a few multiplexers instead of a full adder.<br/>

#### 1F801004h - Expansion 2 Base Address (usually 1F802000h)
Same as 1F801000h, however trying to use ANY other value than 1F802000h seems to
disable the Expansion 2 region, rather than mapping it to the specified address
(ie. Port 1F801004h doesn't seem to work).<br/>
For Expansion 3, the address seems to be fixed (1FA00000h).<br/>

#### 1F801008h - Expansion 1 Delay/Size (usually 0013243Fh) (512Kbytes, 8bit bus) (573: 24173F47h)
#### 1F80100Ch - Expansion 3 Delay/Size (usually 00003022h) (1 byte)
#### 1F801010h - BIOS ROM Delay/Size (usually 0013243Fh) (512Kbytes, 8bit bus)
#### 1F801014h - SPU Delay/Size (200931E1h) (use 220931E1h for SPU-RAM reads)
#### 1F801018h - CDROM Delay/Size (00020843h or 00020943h)
#### 1F80101Ch - Expansion 2 Delay/Size (usually 00070777h) (128 bytes, 8bit bus)
```
  0-3   Write Delay        (00h..0Fh=01h..10h Cycles)
  4-7   Read Delay         (00h..0Fh=01h..10h Cycles)
  8     Recovery Period    (0=No, 1=Yes, uses COM0 timings)
  9     Hold Period        (0=No, 1=Yes, uses COM1 timings)
  10    Floating Period    (0=No, 1=Yes, uses COM2 timings)
  11    Pre-strobe Period  (0=No, 1=Yes, uses COM3 timings)
  12    Data Bus-width     (0=8bits, 1=16bits)
  13    Auto Increment     (0=No, 1=Yes)
  14-15 Unknown (R/W)
  16-20 Number of address bits (memory window size = 1 << N bytes)
  21-23 Unknown (always zero)
  24-27 DMA timing override
  28    Address error flag. Write 1 to it to clear it.
  29    DMA timing select  (0=use normal timings, 1=use bits 24-27)
  30    Wide DMA           (0=use bit 12, 1=override to full 32 bits)
  31    Wait               (1=wait on external device before being ready)
```
When booting, all these registers are using the maximum cycle delays for both
reads and writes. Then, the BIOS will immediately select a faster read
access delay, resulting in a visible speed up after the first few instructions.
The effects aren't immediate however. The BIOS boots using the following instructions:

```mips
bfc00000    lui        $t0, 0x0013
bfc00004    ori        $t0, 0x243f
bfc00008    lui        $at, 0x1f80
bfc0000c    sw         $t0, 0x1010($at)
bfc00010    nop
bfc00014    li         $t0, 0x0b88
bfc00018    lui        $at, 0x1f80
bfc0001c    sw         $t0, 0x1060($at)
bfc00020    nop
```

When using a logic analyzer to monitor the boot sequence, the instruction at
bfc00014 is still read using the old timings since reset, and then the instruction
at bfc00018 is finally read using the sped up timings.

Reads and writes access times aren't symmetrical, and are each controlled with
their own values. By default, EXP1 will be set to 16 cycles when writing, which
is the slowest possible. If the programmer wants to write to a flash chip on
EXP1, or communicate with a computer, speeding up write access is recommended.

The fastest a port could go would be by setting the lowest 16 bits to zero, which
will result in 3 CPU cycles for a single byte access.

!CS always goes active at least one cycle before !WR or !RD go active. The various
timing changes are between all the events inside the data read/write waveform. The
whole formula for computing the total access time is fairly complex overall, and
difficult to properly describe.

- The pre-strobe period will add delays between the moment the data bus is set,
  and the moment !CS goes active.
- The hold period will keep the data in the data bus for some more cycles after
  !WR goes inactive, and before !CS goes inactive. The accessed device is supposed
  to sample the data bus during this interval.
- The floating period will keep the data bus floating for some more cycles after
  !RD goes inactive, and before !CS goes inactive. The accessed device is supposed
  to stop driving the data bus during this interval. The CPU will sample the data
  bus somewhere before or exactly when !CS goes inactive.
- The recovery period will add delays between two operations.

The data bus width will influence if the CPU does full 16 bits reads, or only
8 bits. When doing 32 bits operations, the CPU will issue 2 16-bits operations,
or 4 8-bits operations, keeping !CS active the whole time, and strobing !WR or
!RD accordingly. When doing these sequences, the address bus will also increment
automatically between each operation, if the auto-increment bit is active.

This means it is possible to slightly shorten the read time of 4 bytes off the
same address by disabling auto-increment, and reading a full word. The CPU will
then read 4 bytes off the same address, and place them all into each byte of
the loaded register.

The DMA timing override portion will replace the access timing when doing DMA,
only if the DMA override flag is set.

The Wide DMA flag will enable full 32 bits DMA operations on the bus, by reusing
the low 16-bits address signals as the high 16-bits data. This means that if
the CPU is doing Wide DMA reads, the low 16-bits of the address bus will become
inputs.

Trying to access addresses that exceed the selected size causes a bus exception.
Maximum size would be Expansion 1 = 17h (8MB), BIOS = 16h (4MB), Expansion 2 =
0Dh (8KB), Expansion 3 = 15h (2MB). Trying to select larger sizes would overlap
the internal I/O ports, and crash the PSX. The Size bits seem to be ignored for
SPU/CDROM. The SPU timings seem to be applied for both the 200h-byte SPU region
at 1F801C00h and for the 200h-byte unknown region at 1F801E00h.<br/>

#### 1F801020h - COM\_DELAY / COMMON\_DELAY (00031125h or 0000132Ch or 00001325h)
```
  0-3   COM0 - Recovery period cycles
  4-7   COM1 - Hold period cycles
  8-11  COM2 - Floating release cycles
  12-15 COM3 - Strobe active-going edge delay
  16-31 Unknown/unused (read: always 0000h)
```
This register contains clock cycle offsets that can be added to the Access Time
values in Port 1F801008h..1Ch. Works (somehow) like so:<br/>
```
  1ST=0, SEQ=0, MIN=0
  IF Use_COM0 THEN 1ST=1ST+COM0-1, SEQ=SEQ+COM0-1
  IF Use_COM2 THEN 1ST=1ST+COM2,   SEQ=SEQ+COM2
  IF Use_COM3 THEN MIN=COM3
  IF 1ST<6 THEN 1ST=1ST+1   ;(somewhat like so)
  1ST=1ST+AccessTime+2, SEQ=SEQ+AccessTime+2
  IF 1ST<(MIN+6) THEN 1ST=(MIN+6)
  IF SEQ<(MIN+2) THEN SEQ=(MIN+2)
```
The total access time is the sum of First Access, plus any Sequential
Access(es), eg. for a 32bit access with 8bit bus: Total=1ST+SEQ+SEQ+SEQ.<br/>
If the access is done from code in (uncached) RAM, then 0..4 cycles are added
to the Total value (the exact number seems to vary depending on the used COMx
values or so).<br/>

#### 1F801060h - RAM\_SIZE (R/W) (usually 00000B88h) (or 00000888h)
```
  0-2   Unknown (no effect)
  3     Crashes when zero (except PU-7 and EARLY-PU-8, which <do> set bit3=0)
  4-6   Unknown (no effect)
  7     Delay on simultaneous CODE+DATA fetch from RAM (0=None, 1=One Cycle)
  8     Unknown (no effect) (should be set for 8MB, cleared for 2MB)
  9     RAM chip size 1 (0=1MB or 2MB, 1=4MB or 8MB)
  10    Enable /RAS1 bank (0=disable/bus fault on access, 1=enable)
  11    RAM chip size 2 (0=1MB or 4MB, 1=2MB or 8MB)
  12-15 Unknown (no effect)
  16-31 Unknown (Garbage)
```
Possible values for bits 9-11 are:<br/>
```
  000 = 1MB bank on /RAS0 + 15MB unmapped
  001 = 4MB bank on /RAS0 + 12MB unmapped
  010 = 1MB bank on /RAS0 + 1MB bank on /RAS1 (?) + 14MB unmapped
  011 = 4MB bank on /RAS0 + 4MB bank on /RAS1 (?) + 8MB unmapped
  100 = 2MB bank on /RAS0 + 14MB unmapped
  101 = 8MB bank on /RAS0 + 8MB unmapped
  110 = 2MB bank on /RAS0 + 2MB bank on /RAS1 (?) + 12MB unmapped
  111 = 8MB bank on /RAS0 + 8MB bank on /RAS1 (?)
```
The BIOS writes different values depending on the console revision:<br/>
```
PU-7, EARLY-PU-8:
  0B80h    Single 2MB bank (four 512Kx8 chips) on /RAS0
           (incorrectly set as an 8MB bank, correct setting would be 0880h)
Later consoles:
  0B88h    Single 2MB bank (one 512Kx32 chip) on /RAS0
           (incorrectly set as an 8MB bank, correct setting would be 0888h)
DTL-H2000, DTL-H2700, DTL-H2500:
  0B88h    Single 8MB bank (four 2Mx8 chips) on /RAS0
           (correctly set as 8MB)
System 573 (700A01, 700B01 if ASIC revision bit = 1):
  0C80h    Two 2MB banks (four 512Kx8 chips each) on /RAS0 and /RAS1 respectively
           (correctly set as 4MB)
System 573 (700B01 if ASIC revision bit = 0):
  4788h    Two 4MB banks on /RAS0 and /RAS1 respectively
           (probably an incorrect setting for the two alternate 1Mx16 RAM
           footprints on revision D of the PCB, labeled "DR16M16")
```
"Unmapped" means that the CPU generates an exception when accessing that area.<br/>
Note: Wipeout uses a BIOS function that changes RAM\_SIZE to 00000888h (ie. with
corrected size of 2MB, and with the unknown Bit8 cleared). Gundam Battle
Assault 2 does actually use the "8MB" space (with stacktop in mirrored RAM at
807FFFxxh).<br/>
Clearing bit7 causes many games to hang during CDROM loading on both EARLY-PU-8
and LATE-PU-8 (but works on PU-18 through PM-41).<br/>

#### FFFE0130h - BCC, BIU/Cache Configuration Register (R/W)
```
  0     LOCK   Enable cache lock mode              (when COP0_SR.IsC=1)
  1     INV    Enable cache invalidation mode      (when COP0_SR.IsC=1)
  2     TAG    Enable cache tag test mode          (when COP0_SR.IsC=1, used to flush i-cache)
  3     RAM    Enable cache scratchpad mode        (usually 1, broken - see note)
  4-5   DBLKSZ Data cache refill size              (usually 0, broken - see note)
  6     -      Always 0 (R)
  7     DS     Enable data cache                   (usually 1, disables scratchpad when 0)
  8-9   IBLKSZ Instruction cache refill size       (0=2 words, 1=4 words/default, 2-3=invalid/crash)
  10    IS0    Always 0 (R)                        (supposedly "Enable instruction cache set 0")
  11    IS1    Enable instruction cache
  12    INTP   Supposedly "Interrupt polarity"     (usually 0)
  13    RDPRI  Supposedly "Enable read priority"   (usually 1)
  14    NOPAD  Supposedly "No wait state"          (usually 1)
  15    BGNT   Supposedly "Enable bus grant"       (usually 1)
  16    LDSCH  Supposedly "Enable load scheduling" (usually 1)
  17    NOSTR  Supposedly "No streaming"           (usually 0)
  18-31 -      Reserved (R/W)
```
Documented in chapter 14 of the datasheet for LSI's L64360, which specifically
states it "includes the LR33300 Family Control Registers described in the
CW33300 manual".<br/>
Used primarily by the BIOS to flush the i-cache in combination with the COP0
status register, like so:<br/>
```c
uint32_t sr = COP0_SR;

BCC     = TAG | IS1;
COP0_SR = IsC;

for (int i = 0; i < 0x1000; i += 16) // Clear tags (one for each 4-word line)
    *((volatile uint32_t *) i) = 0;

COP0_SR = 0;
BCC     = IS1;
COP0_SR = IsC;

for (int i = 0; i < 0x1000; i += 4) // Clear cache lines
    *((volatile uint32_t *) i) = 0;
for (int i = 0; i < 8; i++)         // Wait by reading dummy words from uncached RAM?
    *((volatile uint32_t *) 0xa0000000);

COP0_SR = 0;
BCC     = RAM | DS | IBLKSZ_4 | IS1 | RDPRI | NOPAD | BGNT | LDSCH;
COP0_SR = sr;
```
At least one game (TOCA World Touring Cars, SLES-02572) flushes the cache using
custom code running from uncached RAM (KSEG1) instead of calling the BIOS
function described above. It follows a slightly different sequence:
```c
uint32_t bcc = BCC, sr = COP0_SR;

COP0_SR = 0;
BCC     = (BCC & ~(LOCK | INV | DS | IS0)) | TAG | IS1;
COP0_SR = IsC;

for (int i = 0; i < 0x1000; i += 16) // Clear tags (one for each 4-word line)
    *((volatile uint32_t *) i) = 0;

COP0_SR = 0;
BCC     = bcc;
COP0_SR = sr;
```
A usable version of this code
[is available](https://github.com/pcsx-redux/nugget/blob/main/common/hardware/flushcache.s).<br/>
Bit 3 may be cleared to unmap the scratchpad from memory and use it as a data
cache instead, however doing so will result in erratic behavior due to it not
being equipped with tag memory; each cache line's "tag" seems to be hardcoded to
its respective scratchpad address instead. With bit 3 cleared, data in the
scratchpad will be updated during CPU loads but no cache hits will ever occur.<br/>
Bits 4-5 seem to have no effect whatsoever. The CPU will always fetch one word
at a time from RAM, rather than attempting to prefetch an entire line using a
burst read (as it does with the i-cache).<br/>
