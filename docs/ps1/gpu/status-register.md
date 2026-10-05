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
  13    ODE2  Interlace Field       (or, always 1 when GP1(08h).5=0)
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
In 480-lines mode, bit31 changes per frame. And in 240-lines mode, the bit
changes per scanline. The bit is always zero during Vblank (vertical retrace
and upper/lower screen border).<br/>
The bit names listed here are from version 2.8 of the PS2 SDK, which includes
unstripped debug symbols that reference the PGIF's `PG_STAT` register used for
PS1 GPU emulation; some of them appear in PS1 libraries as well.<br/>

#### Note
Further GPU status information can be retrieved via GP1(10h) and GP0(C0h).<br/>

#### Ready Bits
Bit28: Normally, this bit gets cleared when the command execution is busy (ie.
once when the command and all of its parameters are received), however, for
Polygon and Line Rendering commands, the bit gets cleared immediately after
receiving the command word (ie. before receiving the vertex parameters). The
bit is used as DMA request in DMA Mode 2, accordingly, the DMA would probably
hang if the Polygon/Line parameters are transferred in a separate DMA block
(ie. the DMA probably starts ONLY on command words).<br/>
Bit27: Gets set after sending GP0(C0h) and its parameters, and stays set until
all data words are received; used as DMA request in DMA Mode 3.<br/>
Bit26: Gets set when the GPU wants to receive a command. If the bit is cleared,
then the GPU wants to either receive additional parameters/data or it is busy with command
execution (and doesn't want to receive anything). Note that this bit can NOT be used
to determine when the GPU is finished drawing a DMA chain of primitives, as it will briefly
go high after processing each primitive.<br/>
Bit25: This is the DMA Request bit, however, the bit is also useful for non-DMA
transfers, especially in the FIFO State mode.<br/>
