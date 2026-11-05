#   Status Register
####  `0x1f801814`: `GP1` (GPU status register, when read)
nocash's original version of the documentation refers to this register as
`GPUSTAT`; this is not official Sony naming, see
[Legacy names from outdated documentation](../system/iomap.md#legacy-names-from-outdated-documentation)
for other renamed registers.<br/>
```
  0-3   TBX   Texture page X Base   (N*64)                              ;GP0(E1h).0-3
  4     TBY   Texture page Y Base 1 (N*256) (ie. 0, 256, 512 or 768)    ;GP0(E1h).4
  5-6   ABR   Semi-transparency     (0=B/2+F/2, 1=B+F, 2=B-F, 3=B+F/4)  ;GP0(E1h).5-6
  7-8   TPF   Texture page colors   (0=4bit, 1=8bit, 2=15bit, 3=Reserved)GP0(E1h).7-8
  9     DTD   Dither 24bit to 15bit (0=Off/strip LSBs, 1=Dither Enabled);GP0(E1h).9
  10    DFE   Drawing to display area (0=Prohibited, 1=Allowed)         ;GP0(E1h).10
  11    PBW   Set Mask-bit when drawing pixels (0=No, 1=Yes/Mask)       ;GP0(E6h).0
  12    PBC   Draw Pixels           (0=Always, 1=Not to Masked areas)   ;GP0(E6h).1
  13    ODE2  Interlace Field       (v2 GPU only, see below)
  14    REV?  Flip screen horizontally (0=Off, 1=On, v1 only)           ;GP1(08h).7
  15    TBY2  Texture page Y Base 2 (N*512) (only for 2 MB VRAM)        ;GP0(E1h).11
  16    HDS2  Horizontal Resolution 2     (0=256/320/512/640, 1=368)    ;GP1(08h).6
  17-18 HDS   Horizontal Resolution 1     (0=256, 1=320, 2=512, 3=640)  ;GP1(08h).0-1
  19    VDS   Vertical Resolution         (0=240, 1=480, when Bit22=1)  ;GP1(08h).2
  20    NPB   Video Mode                  (0=NTSC/60Hz, 1=PAL/50Hz)     ;GP1(08h).3
  21    LBS   Display Area Color Depth    (0=15bit, 1=24bit)            ;GP1(08h).4
  22    IRS   Vertical Interlace          (0=Off, 1=On)                 ;GP1(08h).5
  23    DMSK  Display Enable              (0=Enabled, 1=Disabled)       ;GP1(03h).0
  24    IRQ   Interrupt Request (IRQ1)    (0=Off, 1=IRQ)       ;GP0(1Fh)/GP1(02h)
  25    DREQ  DMA / Data Request, meaning depends on GP1(04h) DMA Direction:
                When GP1(04h)=0 ---> Always zero (0)
                When GP1(04h)=1 ---> GP0 write FIFO not full (0=Full, 1=Not Full)
                When GP1(04h)=2 ---> Same as WFEP
                When GP1(04h)=3 ---> Same as RFFL
  26    IDLE  Ready to receive Cmd Word   (0=No, 1=Ready)  ;GP0(...) ;via GP0 write
  27    RFFL  GP0 read data ready         (0=No, 1=Ready)  ;GP0(C0h) ;via GPUREAD
  28    WFEP  GP0 write FIFO empty        (0=No, 1=Empty)  ;GP0(...) ;via GP0 write
  29-30 DMD   DMA Direction               (0=Off, 1=WFNF, 2=WFEP, 3=RFFL)    ;GP1(04h).0-1
  31    ODE   Drawing even/odd lines in interlace mode (0=Even or Vblank, 1=Odd)
```
In 480-lines mode, bit31 changes per field (see below). And in 240-lines mode,
the bit changes per scanline. The bit is always zero during Vblank (vertical
retrace and upper/lower screen border).<br/>
The bit names listed here are from version 2.8 of the PS2 SDK, which includes
unstripped debug symbols that reference the PGIF's `PG_STAT` register used for
PS1 GPU emulation; some of them appear in PS1 libraries as well.<br/>

#### Bits 13 and 31 in 480-line interlaced mode
In 480i the fields alternate between a long and a short one: 263 and 262 lines
in NTSC, 313 and 312 in PAL. Counting lines as hblanks since the vblank that
opens each field, with the display range used here (Y1=10h, Y2=100h in NTSC,
Y1=27h, Y2=125h in PAL):
```
  Bit  GPU    NTSC 263-line field      NTSC 262-line field
  31   v0/v2  0 for lines 0-22,        always 0
              1 from 23 until vblank
  13   v2     1 for lines 0-5, 0 from 6   0 for lines 0-4, 1 from 5
  13   v0     always 0                 always 0

  Bit  GPU    PAL 313-line field       PAL 312-line field
  31   v0/v2  0 for lines 0-58,        always 0
              1 from 59 until vblank
  13   v2     1 for lines 0-18,        0 for lines 0-17, 1 from 18
              0 from 19
  13   v0     always 0                 always 0
```
Neither change is tied to the vblank. Bit 31 goes to 1 on scanline Y1, the top
of the display area, and back to 0 at the vblank. Bit 13 changes on the last
scanline of each frame, the one before scanline 0: it falls at the end of the
long frame and rises at the end of the short one. Moving Y2 moves bit 13's
change relative to the vblank (1 and 2 lines after it with Y2=104h, 21 and 22
with Y2=F0h, in NTSC), and moving Y1 moves bit 31's (39 lines after the vblank
with Y1=20h). A Y2 past the last scanline of the field (108h in NTSC) gives no
vblank IRQ at all.<br/>
So on a v2 GPU bit 13 tells the fields apart all the way through the vblank.
On a v0 GPU bit 13 never sets in this mode, which leaves bit 31, which behaves
the same on both and only reads 1 during the displayed lines of the long field.
The timeline is the same at 256, 320 and 640 pixels wide and does not depend on
GP0(E1h).10 or on the display being enabled. PAL was measured at 256 pixels
wide only. The 368 and 512 pixel widths are not covered here.<br/>
With GP0(E1h).10=0, the rows of the parity bit 31 indicates (odd rows while it
reads 1, even rows while it reads 0) are the ones the GPU does not draw; see
[Draw to display enable](misc.md#draw-to-display-enable).<br/>

#### Switching interlace on and off
After GP1(08h) turns interlace on (240p to 480i), the field the write falls in
runs to the next vblank with bit 31 at 0, and the field after it is a long one
(263 or 313 lines) with bit 31 rising at Y1, then the alternation continues. Bit
13 follows the same fields from the switch on. A write in the first few lines
of the vblank can instead fall in a long field, and then a short field comes
first.<br/>
After interlace is turned off (480i to 240p), every field is 263 lines (314 in
PAL) and bit 31 toggles per scanline from the write on. Bit 13 then
keeps the value it had at the write: it reads 0 or 1 in 240p depending on which
field interlace was turned off in. It reads 1 after GP1(00h), which selects
240p, so "always 1 when interlace is off" only holds when the GPU was reset
since the last 480i field, or never left 240p.<br/>
With GP1(08h).5 set but the vertical resolution bit (GP1(08h).2) clear, the
fields keep alternating in length and bit 13 keeps changing per field, but bit
31 toggles per scanline as in 240p.<br/>
The vertical counter appears to be 10 bits wide. In PAL, interlace turned off at
scanline 309 and back on at 312 makes the next vblank IRQ come 1008 lines after
the first write, which is (1024-309)+293 with Y2=125h (293), and bit 31 rises
754 lines after it, which is scanline 39 (Y1) after a wrap at 1024. That is what a counter
that missed the end of a 312-line frame and ran on to 1023 would do.<br/>
Bit 31 behaves the same on v0 and v2 in all of these cases, display on and off.
Measured in NTSC on a SCPH-1000 (v0), a SCPH-1001 and a SCPH-5501 (v2), PAL on a
SCPH-1000, a SCPH-5501 and a SCPH-7001; the Y1/Y2 variations on a SCPH-5501, a
SCPH-7001, a SCPH-9002 in NTSC mode and a SCPH-1000.<br/>

#### Note
Further GPU status information can be retrieved via GP1(10h) and GP0(C0h).<br/>

#### Ready Bits
WFEP (bit 28): For Polygon and Line Rendering commands, the bit gets cleared
immediately after receiving the command word (ie. before receiving the vertex
parameters). It does not stay cleared while the command draws: bit 28 reads 1
while a triangle, rectangle, fill or copy is still being drawn, and only bit 26
shows the drawing. A triangle sets it again after its setup (a few hundred
cycles at most), a quad once its first triangle is drawn, and a poly-line when
its last segment starts; see the table in
[GP0 write FIFO](i-o-ports-dma-channels-commands-vram.md#gp0-write-fifo). The
bit is used as DMA request in DMA Mode 2, accordingly, the DMA hangs if the
Polygon/Line parameters are transferred in a separate DMA block (ie. the DMA
probably starts ONLY on command words).<br/>
RFFL (bit 27): Gets set after sending GP0(C0h) and its parameters, and stays set until
all data words are received; used as DMA request in DMA Mode 3.<br/>
IDLE (bit 26): Gets set when the GPU wants to receive a command. If the bit is cleared,
then the GPU wants to either receive additional parameters/data or it is busy with command
execution (and doesn't want to receive anything). Note that this bit can NOT be used
to determine when the GPU is finished drawing a DMA chain of primitives, as it will briefly
go high after processing each primitive.<br/>
Bit25: This is the DMA Request bit, however, the bit is also useful for non-DMA
transfers, especially in the FIFO State mode. With GP1(04h)=2 it rises together
with bit 28 after a command in nearly every case; once, after a flat triangle,
bit 28 read 1 at once and bit 25 only ~200 cycles later (?).<br/>
