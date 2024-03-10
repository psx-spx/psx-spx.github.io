#   DMA Channels
#### DMA Register Summary
```
  1F80108xh DMA0 channel 0  MDECin  (RAM to MDEC)
  1F80109xh DMA1 channel 1  MDECout (MDEC to RAM)
  1F8010Axh DMA2 channel 2  GPU (lists + image data)
  1F8010Bxh DMA3 channel 3  CDROM   (CDROM to RAM)
  1F8010Cxh DMA4 channel 4  SPU
  1F8010Dxh DMA5 channel 5  PIO (Expansion Port)
  1F8010Exh DMA6 channel 6  OTC (reverse clear OT) (GPU related)
  1F8010F0h DPCR - DMA Control register
  1F8010F4h DICR - DMA Interrupt register
```
These ports control DMA at the CPU-side. In most cases, you'll additionally
need to initialize an address (and transfer direction, transfer enabled, etc.)
at the remote-side (eg. at the GPU-side for DMA2).<br/>

#### 1F801080h+N\*10h - D#\_MADR - DMA base address (Channel 0..6) (R/W)
```
  0-23  Memory Address where the DMA will start reading from/writing to
  24-31 Not used (always zero)
```
In SyncMode=0, the hardware doesn't update the MADR registers (it will contain
the start address even during and after the transfer) (unless Chopping is
enabled, in that case it does update MADR, same does probably also happen when
getting interrupted by a higher priority DMA channel).<br/>
In SyncMode=1 and SyncMode=2, the hardware does update MADR (it will contain
the start address of the currently transferred block; at transfer end, it'll
hold the end-address in SyncMode=1, or the end marker in SyncMode=2)<br/>
Notes: Address bits 0-1 are writeable, but any updated current/end addresses are
word-aligned with bits 0-1 forced to zero.<br/>
The address counter wraps around when counting down from 000000h to FFFFFCh,
leading to words after wraparound not being written to RAM (as FFFFFCh is past
the default 8 MB main RAM region).<br/>

#### 1F801084h+N\*10h - D#\_BCR - DMA Block Control (Channel 0..6) (R/W)
For SyncMode=0 (ie. for OTC and CDROM):<br/>
```
  0-15  BC    Number of words (0001h..FFFFh) (or 0=10000h words)
  16-31 0     Not used (usually 0 for OTC, or 1 ("one block") for CDROM)
```
For SyncMode=1 (ie. for MDEC, SPU, and GPU-vram-data):<br/>
```
  0-15  BS    Blocksize (words) ;for GPU/SPU max 10h, for MDEC max 20h
  16-31 BA    Amount of blocks  ;ie. total length = BS*BA words
```
For SyncMode=2 (ie. for GPU-command-lists):<br/>
```
  0-31  0     Not used (should be zero) (transfer ends at END-CODE in list)
```
BC/BS/BA can be in range 0001h..FFFFh (or 0=10000h). For BS, take care not to
set the blocksize larger than the buffer of the corresponding unit can hold.
(GPU and SPU both have a 16-word buffer). A larger blocksize means faster
transfer.<br/>
SyncMode=1 decrements BA to zero, SyncMode=0 with chopping enabled decrements
BC to zero (aside from that two cases, D#\_BCR isn't changed during/after
transfer).<br/>

#### 1F801088h+N\*10h - D#\_CHCR - DMA Channel Control (Channel 0..6) (R/W)
```
  0     Transfer direction (0=device to RAM, 1=RAM to device)
  1     MADR increment per step (0=+4, 1=-4)
  2-7   Unused
  8     When 1:
        -Burst mode: enable "chopping" (cycle stealing by CPU)
        -Slice mode: Causes DMA to hang
        -Linked-list mode: Transfer header before data?
  9-10  Transfer mode (SyncMode)
        0=Burst (transfer data all at once after DREQ is first asserted)
        1=Slice (split data into blocks, transfer next block whenever DREQ is asserted)
        2=Linked-list mode
        3=Reserved
  11-15 Unused
  16-18 Chopping DMA window size (1 << N words)
  19    Unused
  20-22 Chopping CPU window size (1 << N cycles)
  23    Unused
  24    Start transfer (0=stopped/completed, 1=start/busy)
  25-27 Unused
  28    Force transfer start without waiting for DREQ
  29    In forced-burst mode, pauses transfer while set.
        In other modes, stops bit 28 from being cleared after a slice is transferred.
        No effect when transfer was caused by a DREQ.
  30    Perform bus snooping (allows DMA to read from -nonexistent- cache?)
  31    Unused
```
Bit 28 is automatically cleared upon BEGIN of the transfer, this bit needs to be
set only in SyncMode=0 (setting it in other SyncModes would force the first
block to be transferred instantly without DREQ, which isn't desired).<br/>
Bit 24 is automatically cleared upon COMPLETION of the transfer, this bit must
be always set for all SyncModes when starting a transfer.<br/>
For DMA6/OTC there are some restrictions, D6\_CHCR has only three
read/write-able bits: 24,28,30. All other bits are read-only: bit 1 is always
1 (increment=-4), and the other bits are always 0.<br/>

#### 1F8010F0h - DPCR - DMA Control Register (R/W)
```
  0-2   DMA0, MDECin  Priority      (0..7; 0=Highest, 7=Lowest)
  3     DMA0, MDECin  Master Enable (0=Disable, 1=Enable)
  4-6   DMA1, MDECout Priority      (0..7; 0=Highest, 7=Lowest)
  7     DMA1, MDECout Master Enable (0=Disable, 1=Enable)
  8-10  DMA2, GPU     Priority      (0..7; 0=Highest, 7=Lowest)
  11    DMA2, GPU     Master Enable (0=Disable, 1=Enable)
  12-14 DMA3, CDROM   Priority      (0..7; 0=Highest, 7=Lowest)
  15    DMA3, CDROM   Master Enable (0=Disable, 1=Enable)
  16-18 DMA4, SPU     Priority      (0..7; 0=Highest, 7=Lowest)
  19    DMA4, SPU     Master Enable (0=Disable, 1=Enable)
  20-22 DMA5, PIO     Priority      (0..7; 0=Highest, 7=Lowest)
  23    DMA5, PIO     Master Enable (0=Disable, 1=Enable)
  24-26 DMA6, OTC     Priority      (0..7; 0=Highest, 7=Lowest)
  27    DMA6, OTC     Master Enable (0=Disable, 1=Enable)
  28-30 CPU memory access priority  (0..7; 0=Highest, 7=Lowest)
  31    No effect, should be CPU memory access enable (R/W)
```
Initial value on reset is 07654321h. If two or more channels have the same
priority setting, then the priority is determined by the channel number
(DMA0=Lowest, DMA6=Highest, CPU=higher than DMA6?).<br/>

#### 1F8010F4h - DICR - DMA Interrupt Register (R/W)
```
  0-6   Controls channel 0-6 completion interrupts in bits 24-30.
        When 0, an interrupt only occurs when the entire transfer completes.
        When 1, interrupts can occur for every slice and linked-list transfer.
        No effect if the interrupt is masked by bits 16-22.
  7-14  Unused
  15    Bus error flag. Raised when transferring to/from an address outside of RAM. Forces bit 31. (R/W)
  16-22 Channel 0-6 interrupt mask. If enabled, channels cause interrupts as per bits 0-6.
  23    Master channel interrupt enable.
  24-30 Channel 0-6 interrupt flags. (R, write 1 to reset)
  31    Master interrupt flag (R)
```
IRQ flags in bit (24+n) are set upon DMAn completion - but caution - they are
set ONLY if enabled in bit (16+n) (unlike interrupt flags in I_STAT, which are
always set regardless of whether the respective IRQ is masked).<br/>
Bit 31 is a simple readonly flag that follows the following rules:<br/>
```
  IF b15=1 OR (b23=1 AND (b16-22 AND b24-30)>0) THEN b31=1 ELSE b31=0
```
Upon 0-to-1 transition of Bit 31, the IRQ3 flag in I\_STAT gets set.<br/>
Bits 24-30 are acknowledged (reset to zero) when writing a "1" to that bits (and
additionally, IRQ3 must be acknowledged via I\_STAT).<br/>

#### 1F8010F8h (usually 7FFAC68Bh? or 0BFAC688h)
```
    (changes to 7FE358D1h after DMA transfer)
```
#### 1F8010FCh (usually 00FFFFF7h) (...maybe OTC fill-value)
```
    (stays so even after DMA transfer)
```
Contains strange read-only values (but not the usual "Garbage").<br/>
Not yet tested during transfer, might be remaining length and address?<br/>

#### Commonly used DMA Control Register values for starting DMA transfers
```
  DMA0 MDEC.IN  01000201h (always)
  DMA1 MDEC.OUT 01000200h (always)
  DMA2 GPU      01000200h (VramRead), 01000201h (VramWrite), 01000401h (List)
  DMA3 CDROM    11000000h (normal), 11400100h (chopped, rarely used)
  DMA4 SPU      01000201h (write), 01000200h (read, rarely used)
  DMA5 PIO      11150100h (System 573 ATAPI read), ? (System 573 ATAPI write)
  DMA6 OTC      11000002h (always)
```
XXX: DMA2 values 01000201h (VramWrite), 01000401h (List) aren't 100% confirmed
to be used by ALL existing games. All other values are always used as listed
above.<br/>

#### Linked List DMA
GPU commands are usually sent from RAM to GP0 using DMA2 in linked list mode. In
this mode, the DMA controller transfers words in "nodes", with the first node
starting in the address indicated by D2_MADR.<br/>
Each node is composed of a header word (the very first word in the node) and
some extra words to be DMA'd before moving on to the next node. The node header
is formatted like this:<br/>

```
  0-23  Address of the next node (or end marker)
  24-31 Number of extra words to transfer for this node
```

The transfer is stopped once an end marker is reached. On some (earlier?) CPU
revisions any address with bit 23 set will be interpreted as an end marker,
while on other revisions all bits must be set (i.e. the address must be FFFFFF).
This change was probably necessary as later CPU versions added support for up to
16 MB RAM addressing, which made addresses in the 800000-FFFFFC range valid.<br/>

#### DMA Transfer Rates
```
  DMA0 MDEC.IN     1 clk/word   ;0110h clks per 100h words ;\plus whatever
  DMA1 MDEC.OUT    1 clk/word   ;0110h clks per 100h words ;/decompression time
  DMA2 GPU         1 clk/word   ;0110h clks per 100h words ;-plus ...
  DMA3 CDROM/BIOS  24 clks/word ;1800h clks per 100h words ;\plus single/double
  DMA3 CDROM/GAMES 40 clks/word ;2800h clks per 100h words ;/speed sector rate
  DMA4 SPU         4 clks/word  ;0420h clks per 100h words ;-plus ...
  DMA5 PIO         20 clks/word ;1400h clks per 100h words ;-not actually used
  DMA6 OTC         1 clk/word   ;0110h clks per 100h words ;-plus nothing
```
MDEC decompression time is still unknown (may vary on RLE and color/mono).<br/>
GPU polygon rendering time is unknown (may be quite slow for large polys).<br/>
GPU vram read/write time is unknown (may vary on horizontal screen resolution).<br/>
CDROM BIOS default is 24 clks, for some reason most games change it to 40 clks.<br/>
SPU transfer is unknown (may have some extra delays).<br/>
XXX is SPU really only 4 clks (theoretically SPU access should be slower)?<br/>
PIO is only used on some arcade systems (and configured with different timings).<br/>
OTC is just writing to RAM without extra overload.<br/>
CDROM/SPU/PIO timings can be configured via Memory Control registers.<br/>

#### DRAM Hyper Page mode
DMA is using DRAM Hyper Page mode, allowing it to access DRAM rows at 1 clock
cycle per word (effectively around 17 clks per 16 words, due to required row
address loading, probably plus some further minimal overload due to refresh
cycles). This is making DMA much faster than CPU memory accesses (CPU DRAM
access takes 1 opcode cycle plus 6 waitstates, ie. 7 cycles in total)<br/>

#### CPU Operation during DMA
CPU is running during DMA within very strict rules. It can be kept running when accessing only cache, scratchpad, COP0 and GTE.<br/>
It can also make use of the 4 entry Write queue for both RAM and I/O registers, see:<br/>
[Write queue](memorymap.md#Write-queue)<br/>
Any read access from RAM or I/O registers or filling more than 4 entries into the write queue will stall the CPU until the DMA is finished.<br/>
Additionally, the CPU operation resumes during periods when DMA gets interrupted
(ie. after SyncMode 1 blocks, after SyncMode 2 list entries) (or in SyncMode 0
with Chopping enabled).<br/>

#### PS2 IOP DMA
The PS2's IOP has an extended DMA unit with more channels, new control registers
and an additional chain mode (SyncMode=3). For more details, see:<br/>
[ps2tek - IOP DMA](https://psi-rockin.github.io/ps2tek/#iopdma)<br/>
