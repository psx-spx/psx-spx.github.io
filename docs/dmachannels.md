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
Note: Address bit0-1 are writeable, but any updated current/end addresses are
word-aligned with bit0-1 forced to zero.<br/>

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
  0       Transfer Direction    (0=To Main RAM, 1=From Main RAM)
  1       Memory Address Step   (0=Forward;+4, 1=Backward;-4)
  2-7     Not used              (always zero)
  8       Chopping Enable       (0=Normal, 1=Chopping; run CPU during DMA gaps)
  9-10    SyncMode, Transfer Synchronisation/Mode (0-3):
            0  Start immediately and transfer all at once (used for CDROM, OTC)
            1  Sync blocks to DMA requests   (used for MDEC, SPU, and GPU-data)
            2  Linked-List mode              (used for GPU-command-lists)
            3  Reserved                      (not used)
  11-15   Not used              (always zero)
  16-18   Chopping DMA Window Size (1 SHL N words)
  19      Not used              (always zero)
  20-22   Chopping CPU Window Size (1 SHL N clks)
  23      Not used              (always zero)
  24      Start/Busy            (0=Stopped/Completed, 1=Start/Enable/Busy)
  25-27   Not used              (always zero)
  28      Start/Trigger         (0=Normal, 1=Manual Start; use for SyncMode=0)
  29      Unknown (R/W) Pause?  (0=No, 1=Pause?)     (For SyncMode=0 only?)
  30      Unknown (R/W)
  31      Not used              (always zero)
```
The Start/Trigger bit is automatically cleared upon BEGIN of the transfer, this
bit needs to be set only in SyncMode=0 (setting it in other SyncModes would
force the first block to be transferred instantly without DRQ, which isn't
desired).<br/>
The Start/Busy bit is automatically cleared upon COMPLETION of the transfer,
this bit must be always set for all SyncModes when starting a transfer.<br/>
For DMA6/OTC there are some restrictions, D6\_CHCR has only three
read/write-able bits: Bit24,28,30. All other bits are read-only: Bit1 is always
1 (step=backward), and the other bits are always 0.<br/>

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
  28-30 Unknown, Priority Offset or so? (R/W)
  31    Unknown, no effect? (R/W)
```
Initial value on reset is 07654321h. If two or more channels have the same
priority setting, then the priority is determined by the channel number
(DMA0=Lowest, DMA6=Highest).<br/>

#### 1F8010F4h - DICR - DMA Interrupt Register (R/W)
```
  0-5   Unknown  (read/write-able)
  6-14  Not used (always zero)
  15    Force IRQ (sets bit31)            (0=None, 1=Force Bit31=1)
  16-22 IRQ Enable for DMA0..DMA6         (0=None, 1=Enable)
  23    IRQ Master Enable for DMA0..DMA6  (0=None, 1=Enable)
  24-30 IRQ Flags for DMA0..DMA6          (0=None, 1=IRQ)    (Write 1 to reset)
  31    IRQ Master Flag                   (0=None, 1=IRQ)    (Read only)
```
IRQ flags in Bit(24+n) are set upon DMAn completion - but caution - they are
set ONLY if enabled in Bit(16+n).<br/>
Bit31 is a simple readonly flag that follows the following rules:<br/>
```
  IF b15=1 OR (b23=1 AND (b16-22 AND b24-30)>0) THEN b31=1 ELSE b31=0
```
Upon 0-to-1 transition of Bit31, the IRQ3 flag (in Port 1F801070h) gets set.<br/>
Bit24-30 are acknowledged (reset to zero) when writing a "1" to that bits (and,
additionally, IRQ3 must be acknowledged via Port 1F801070h).<br/>

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
  DMA5 PIO      N/A       (not used by any known games)
  DMA6 OTC      11000002h (always)
```
XXX: DMA2 values 01000201h (VramWrite), 01000401h (List) aren't 100% confirmed
to be used by ALL existing games. All other values are always used as listed
above.<br/>

#### Linked List DMA
GPU data is often transferred from RAM to GP0 using DMA2 in linked list mode. In this mode,
the DMA controller transfers words in "nodes", with the first node starting in the address indicated by D2_MADR.<br/>
Each node is composed of a header word (the very first word in the node) and some extra words to be DMA'd before moving on to the next node. The node header is formatted like this:<br/>

```
  0-23  Address of the next node (or end marker)
  24-31 Number of extra words to transfer for this node
```

If the address of the next node has bit 23 set, ie if `(address & 0x800000) != 0` then the DMA controller will not move on to the next node and the DMA transfer ends. In this case that address is commonly referred to as the "end marker" for the DMA.<br/>
Commercial and homebrew games typically use 0xffffff as the end marker, however other values such as 0x800002, 0x934567, and so on will also do the trick assuming bit 23 is set.

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
PIO isn't used by any games (and if used: could be configured to other rates)<br/>
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
