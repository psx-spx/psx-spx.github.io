#   Memory Control
The Memory Control registers are initialized by the BIOS, and, normally
software doesn't need to change that settings. Some registers are useful for
expansion hardware (allowing to increase the memory size and bus width).<br/>

#### 1F801000h - DEV0 Base Address (usually 1F000000h)
```
  0-23   Base address       (R/W)
  24-31  Fixed, always 1Fh  (R)
```
The behavior of this register is somewhat inconsistent. Normally, the base
address is forcefully aligned to the DEV0 region's size by masking off the
bottommost N bits (where N = number of address lines, as set in register
1F801008h). For instance, if the number of DEV0 address lines is set to 8,
setting this register to 1F000000h or 1F0000FFh has the same effect.<br/>
When performing a PIO DMA transfer, however, all bits of this register are
output on the bus regardless of the currently set region size. The System 573
relies on this behavior as it changes the base address to 1F480000h prior to
reading data from the IDE CD-ROM using DMA (and does not reset it to 1F000000h
afterwards).<br/>
Note: presumably the masking lets the bus interface compute addresses quickly by
replacing masked off bits with the LSBs of the incoming address value from the
CPU, thus only requiring a few multiplexers instead of a full adder.<br/>

#### 1F801004h - DEV8 Base Address (usually 1F802000h)
Same as 1F801000h, however trying to use ANY other value than 1F802000h seems to
disable the DEV8 region, rather than mapping it to the specified address
(ie. Port 1F801004h doesn't seem to work).<br/>
For DEV1, the address seems to be fixed (1FA00000h).<br/>

#### 1F801008h - DEV0 Delay/Size (usually 0013243Fh) (512Kbytes, 8bit bus) (573: 24173F47h)
#### 1F80100Ch - DEV1 Delay/Size (usually 00003022h) (1 byte)
#### 1F801010h - DEV2 (BIOS ROM) Delay/Size (usually 0013243Fh) (512Kbytes, 8bit bus)
#### 1F801014h - DEV4 (SPU) Delay/Size (200931E1h) (use 220931E1h for SPU-RAM reads)
#### 1F801018h - DEV5 (CD-ROM) Delay/Size (00020843h or 00020943h)
#### 1F80101Ch - DEV8 Delay/Size (usually 00070777h) (128 bytes, 8bit bus)
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
their own values. By default, DEV0 will be set to 16 cycles when writing, which
is the slowest possible. If the programmer wants to write to a flash chip on
DEV0, or communicate with a computer, speeding up write access is recommended.

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
Maximum size would be DEV0 = 17h (8MB), DEV2 = 16h (4MB), DEV8 = 0Dh (8KB),
DEV1 = 15h (2MB). Trying to select larger sizes would overlap the internal I/O
ports, and crash the PSX. The Size bits seem to be ignored for SPU/CDROM. The
SPU timings seem to be applied for both the 200h-byte SPU region at 1F801C00h
and for the 200h-byte unknown region at 1F801E00h.<br/>

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

#### 1F801060h - DRAM\_CTRL? (R/W) (usually 00000B88h) (or 00000888h)
```
  0-2   Refresh hold-off during DMA  (0=none, 1..6=(4 << (N-1)) cycles, 7=unlimited)
  3     /CAS and /WE wiring          (0=common /CAS with per-byte /WE, 1=per-byte /CAS with common /WE)
  4-5   Refresh period               (0..3=(256 + 64*N) cycles)
  6     Unknown
  7     Consecutive access waitstate (0=none, 1=1 cycle)
  8     /RAS1 bank size bit 1        (see below)
  9     /RAS0 bank size bit 1        (see below)
  10    Enable /RAS1 bank            (0=disable/bus fault on access, 1=enable)
  11    Bank size bit 0              (see below, common to both banks)
  12-15 Unknown
  16-31 Unused (Garbage)
```

The two main RAM banks are mapped in memory sequentially, /RAS1 after /RAS0.
Each of them can be 1, 2, 4 or 8MB in size, determined as follows:
```
  /RAS0 size = 1MB << ((DRAM_CTRL.9 << 1) | DRAM_CTRL.11)
  /RAS1 size = 1MB << ((DRAM_CTRL.8 << 1) | DRAM_CTRL.11)
```

Assuming two banks of the same size, possible values for bits 8-11 are thus:
```
  0000 = 1MB bank on /RAS0 + 15MB unmapped
  0011 = 4MB bank on /RAS0 + 12MB unmapped
  0100 = 1MB bank on /RAS0 +  1MB bank on /RAS1 + 14MB unmapped
  0111 = 4MB bank on /RAS0 +  4MB bank on /RAS1 +  8MB unmapped
  1000 = 2MB bank on /RAS0 + 14MB unmapped
  1011 = 8MB bank on /RAS0 +  8MB unmapped
  1100 = 2MB bank on /RAS0 +  2MB bank on /RAS1 + 12MB unmapped
  1111 = 8MB bank on /RAS0 +  8MB bank on /RAS1
```

Notes:
- "Unmapped" means that the CPU generates an exception when accessing that area.
- The DRAM controller determines which bank to access from the CPU address bit
  immediately above the /RAS0 bank size: A20 for 1MB, A21 for 2MB, A22 for 4MB
  or A23 for 8MB.
- Bits 0-2 set how many cycles a refresh can be postponed by while the DRAM
  controller is busy handling a DMA transfer. The default value of 0 forces DMA
  transfers to yield to a refresh immediately. Instruction fetches and data
  reads/writes seem to be unaffected.
- Bit 7 inserts an idle cycle between any two consecutive RAM accesses
  (including refreshes), but not between each word in a DMA or instruction fetch
  burst. Clearing it causes many games to hang during CD-ROM loading on
  EARLY-PU-8 and LATE-PU-8 boards (but works on PU-18 onwards).
- Bit 3 is only implemented in later CPU revisions (verified to be nonfunctional
  on the DTL-H2700) and swaps /CAS and /WE when set. See the CPU pinouts section
  for more details.

The BIOS writes different values depending on the console revision:
```
PU-7, EARLY-PU-8:
  0B80h    Single 2MB bank (four 512Kx8 chips), byte masking via /WE
           (incorrectly set as an 8MB bank, correct setting would be 0880h)
Later consoles:
  0B88h    Single 2MB bank (one 512Kx32 chip), byte masking via /CAS
           (incorrectly set as an 8MB bank, correct setting would be 0888h)
DTL-H2000, DTL-H2700:
  0B80h    Single 8MB bank (four 2Mx8 chips), byte masking via /WE
           (correctly set as 8MB)
DTL-H2500:
  0B88h    Single 8MB bank (four 2Mx8 chips), byte masking via /CAS
           (correctly set as 8MB)
System 573 (700A01, 700B01 if ASIC revision bit = 1):
  0C80h    Two 2MB banks (four 512Kx8 chips each), byte masking via /WE
           (correctly set as 4MB)
System 573 (700B01 if ASIC revision bit = 0):
  4788h    Two 4MB banks, byte masking via /CAS
           (probably an incorrect setting for the two alternate 1Mx16 RAM
           footprints on revision D of the PCB, labeled "DR16M16")
```

Several retail games (Puzzle Bobble, Gundam Battle Assault 2, likely more) and
homebrew (the FreePSXBoot BIOS shell exploit) are known to rely on the three
accidental "mirrors" created by the BIOS incorrectly configuring the DRAM
controller for an 8MB bank instead of 2MB; this sometimes happens due to
developers forgetting to move the stack down from 807FFFxxh to 801FFFxxh.
Wipeout uses the SetMem() BIOS function to shrink the bank size to 2MB.

#### Main RAM array organization
The 2MB main RAM is organized as 2048 rows of 256 columns, 4 bytes per column,
ie. 1024 bytes per row.<br/>
The CPU address maps onto the array linearly:<br/>
```
  row    = addr[20:10]
  column = addr[9:2]
```
So a 1KB-aligned block is exactly one DRAM row, and crossing a 1KB boundary
crosses a row.<br/>
The controller uses a closed-page policy between transactions: a fresh row
address is emitted on every transaction, even when the previous transaction
touched the same row. Fast-page mode applies only within a single burst, so
there is no page-hit bonus for two separate accesses to the same row.<br/>
Refresh is distributed, one row every 256 CPU cycles, sweeping all 2048 rows in
roughly 15.5ms.<br/>

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
IBLKSZ (bits 8-9) controls the i-cache refill burst length. With the default
value of 1 (4-word), a cache miss at word 0 fills the entire 4-word line. With
IBLKSZ=0 (2-word), a miss at word 0 fills only words 0 and 1. Misses at words
1, 2, or 3 always fill from the accessed word to end-of-line regardless of
IBLKSZ. See the [i-Cache](memorymap.md#i-cache) section for details on fill
behavior and per-word valid bits.<br/>
When TAG is set and IsC is set in COP0 SR, stores to the cache address space
write to the i-cache tag memory. The stored value is:
```
  tag = (data AND 0Fh) OR (offset AND FFFFF000h)
```
The low 4 bits of the write data become the per-word valid bits. The upper
address bits come from the **write offset**, not the data. Writing 0 at each
line's base address (offset = line * 16) clears the valid bits while setting
the address portion to 0, effectively invalidating the line. Code words are not
affected by tag writes.<br/>
TAG mode reads (loads with TAG set in BCC and IsC set) return the valid bits in
bits [3:0] and a tag match result in bit [4]. Bit 4 is set if the stored tag's
address field matches the read address. The upper bits [31:5] contain code word
data that leaks through and should be ignored. TAG mode reads are primarily
useful for diagnostics, not for normal cache management.<br/>
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
##### "D-cache" mode (RAM=0, DS=1)
Bit 3 may be cleared to unmap the scratchpad from memory and use it as a data
cache instead, however doing so produces an unusual fill behavior due to the
scratchpad SRAM not being equipped with tag memory; each cache line's "tag" is
hardcoded to its respective scratchpad address. The address tag of any
non-scratchpad load will therefore never match, and every load is a cache miss
that fills scratchpad as a side effect.<br/>
The miss-fill writes the loaded word into scratchpad at slot
`(load_byte_addr >> 2) AND 0FFh`. The fill is **word-granular** regardless of
load width: `lb`, `lh`, and `lw` all populate the full word containing the
accessed byte/half. Each load produces exactly one word fill - there is no
burst behavior. The most useful pattern in this mode is loading a 1KB block
from main RAM into scratchpad with a sequence of `lw` instructions, saving
the explicit `sw` to scratchpad that a manual copy would require.<br/>
The mechanism has several specific characteristics, all hardware-verified on
SCPH-5501:<br/>
- The cache **never produces a true hit**. Every load is a miss-fill, even
immediately after a previous load filled the same slot. If main RAM is
modified between two loads of the same address (e.g. via the uncached KSEG1
mirror), the second load sees the new RAM value.
- **KSEG1 (uncached) loads bypass the d-cache entirely.** They do not fill
scratchpad.
- **Stores do not spill into scratchpad.** Only loads do. Stores in this mode
go to main RAM (or the targeted I/O) without touching scratchpad.
- Reads or writes targeting the scratchpad address range
(1F800000h..1F8003FFh) **deadlock the bus** in this mode. With scratchpad
disabled by RAM=0, those addresses no longer have a normal responder.
Recovery requires a power cycle.
- Bits 4-5 (DBLKSZ) have no effect on fill behavior in this mode, and seem
to have no effect in normal scratchpad mode either. The CPU will always
fetch one word at a time from RAM, rather than attempting to prefetch an
entire line using a burst read (as it does with the i-cache).
- Bits 0-2 (LOCK / INV / TAG) are inert when COP0 SR.IsC is clear.
- COP0 SR.SwC has no observable effect on this behavior.<br/>
