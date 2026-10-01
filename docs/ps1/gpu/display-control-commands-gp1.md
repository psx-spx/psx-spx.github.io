#   GPU Display Control Commands (GP1)
GP1 Display Control Commands are sent by writing the 8bit Command number
(MSBs), and 24bit parameter (LSBs) to Port 1F801814h. Unlike GP0 commands, GP1
commands are passed directly to the GPU (ie. they can be sent even when the
FIFO is full).<br/>

#### GP1(00h) - Reset GPU
```
  0-23  Not used (zero)
```
Resets the GPU to the following values:<br/>
```
  GP1(01h)      ;clear fifo
  GP1(02h)      ;ack irq (0)
  GP1(03h)      ;display off (1)
  GP1(04h)      ;dma off (0)
  GP1(05h)      ;display address (0)
  GP1(06h)      ;display x1,x2 (x1=200h, x2=200h+256*10)
  GP1(07h)      ;display y1,y2 (y1=010h, y2=010h+240)
  GP1(08h)      ;display mode 320x200 NTSC (0)
  GP0(E1h..E6h) ;rendering attributes (0)
```
Accordingly, GP1.read becomes 14802000h. The x1,y1 values are too small, ie. the
upper-left edge isn't visible. Note that GP1(09h) is NOT affected by the reset
command.<br/>

#### GP1(01h) - Reset Command Buffer
```
  0-23  Not used (zero)
```
Resets the command buffer and CLUT cache.<br/>

#### GP1(02h) - Acknowledge GPU Interrupt (IRQ1)
```
  0-23  Not used (zero)                                        ;GP1.R.24
```
Resets the IRQ flag in GP1.R.24. The flag can be set via GP0(1Fh).<br/>

#### GP1(03h) - Display Enable
```
  0    DMSK  Display On/Off   (0=On, 1=Off)                         ;GP1.R.23
  1-23       Not used (zero)
```
Turns display on/off. "Note that a turned off screen still gives the flicker of
NTSC on a PAL screen if NTSC mode is selected."<br/>
The "Off" settings displays a black picture (and still sends /SYNC signals to
the television set). (Unknown if it still generates vblank IRQs though?)<br/>

#### GP1(04h) - DMA Direction / Data Request
```
  0-1  DMD  DMA Direction (0=Off, 1=WFNF, 2=WFEP, 3=RFFL) ;GP1.R.29-30
              0 ---> DMA requests off
              1 ---> DMA request on GP0 write FIFO not full
              2 ---> DMA request on GP0 write FIFO empty
              3 ---> DMA request while GPUREAD data is ready
  2-23      Not used (zero)
```
Notes: Manually sending/reading data by software (non-DMA) is ALWAYS possible,
regardless of the GP1(04h) setting. The GP1(04h) setting does affect the
meaning of GP1.R.25.<br/>

#### Display start/end
Specifies where the display area is positioned on the screen, and how much data
gets sent to the screen. The screen sizes of the display area are valid only if
the horizontal/vertical start/end values are default. By changing these you can
get bigger/smaller display screens. On most TV's there is some black around the
edge, which can be utilised by setting the start of the screen earlier and the
end later. The size of the pixels is NOT changed with these settings, the GPU
simply sends more data to the screen. Some monitors/TVs have a smaller display
area and the extended size might not be visible on those sets. "(Mine is
capable of about 330 pixels horizontal, and 272 vertical in 320\*240 mode)"<br/>

#### GP1(05h) - Start of Display area (in VRAM)
```
  0-9   X (0-1023)    (halfword address in VRAM)  (relative to begin of VRAM)
  10-18 Y (0-511)     ;\on v0 GPU, or with GP1(09h).0=0
  19-23 Not used (zero)         ;/
  10-19 Y (0-1023)    ;\on v2 GPU with 2 MB VRAM and GP1(09h).0=1
  20-23 Not used (zero)         ;/
```
Upper/left Display source address in VRAM. The size and target position on
screen is set via Display Range registers; target=X1,Y1;
size=((X2-X1)/cycles\_per\_pix), (Y2-Y1).<br/>
On v2 GPUs with 2 MB VRAM enabled via GP1(09h).0=1, the Y field is 10-bit
and the full 0..1023 range is honored. If the displayed area would extend
past Y=1023 the read address wraps modulo 1024, so a display starting at
Y=1023 shows row 1023 followed by row 0 onwards rather than a black
scanline.<br/>

#### GP1(06h) - Horizontal Display range (on Screen)
```
  0-11   X1 (260h+0)       ;12bit       ;\counted in video clock units,
  12-23  X2 (260h+320*8)   ;12bit       ;/relative to HSYNC
```
Specifies the horizontal range within which the display area is displayed. For
resolutions other than 320 pixels it may be necessary to fine adjust the value
to obtain an exact match (eg. X2=X1+pixels\*cycles\_per\_pix).<br/>
The number of displayed pixels per line is "(((X2-X1)/cycles\_per\_pix)+2) AND
NOT 3" (ie. the hardware is rounding the width up/down to a multiple of 4
pixels).<br/>
Most games are using a width equal to the horizontal resolution (ie. 256, 320,
368, 512, 640 pixels). A few games are using slightly smaller widths (probably
due to programming bugs). Pandemonium 2 is using a bigger "overscan" width
(ensuring an intact picture without borders even on mis-calibrated TV sets).<br/>
The 260h value is the first visible pixel on normal TV Sets, this value is used
by MOST NTSC games, and SOME PAL games (see below notes on Mis-Centered PAL
games).<br/>
Video clock unit used depends on console region, regardless of NTSC/PAL video
mode set by GP1(08h).3; see section on [nominal video clocks](timings.md#nominal-video-clock)
for values.<br/>

For official games, X1 and X2 seem to vary based on resolution.<br/>
The following values are used for the fullscreen range:

| Width    | X1  | X2   | Range |
| -------: | :-- | :--- | :---- |
| NTSC 256 | 590 | 3150 | 2560  |
| NTSC 320 | 600 | 3160 | 2560  |
| NTSC 368 | 539 | 3227 | 2688  |
| NTSC 512 | 615 | 3175 | 2560  |
| NTSC 640 | 620 | 3180 | 2560  |
| PAL 256  | 610 | 3170 | 2560  |
| PAL 320  | 624 | 3184 | 2560  |
| PAL 368  | 560 | 3248 | 2688  |
| PAL 512  | 635 | 3195 | 2560  |
| PAL 640  | 640 | 3200 | 2560  |

#### GP1(07h) - Vertical Display range (on Screen)
```
  0-9   Y1 (NTSC=88h-(240/2), (PAL=A3h-(288/2))  ;\scanline numbers on screen,
  10-19 Y2 (NTSC=88h+(240/2), (PAL=A3h+(288/2))  ;/relative to VSYNC
  20-23 Not used (zero)
```
Specifies the vertical range within which the display area is displayed. The
number of lines is Y2-Y1 (unlike as for the width, there's no rounding applied
to the height). If Y2 is set to a much too large value, then the hardware stops
to generate vblank interrupts (IRQ0).<br/>
The 88h/A3h values are the middle-scanlines on normal TV Sets, these values are
used by MOST NTSC games, and SOME PAL games (see below notes on Mis-Centered
PAL games).<br/>
The 240/288 values are for fullscreen pictures. Many NTSC games display 240
lines, but on most analog television sets, only 224 lines are visible (8 lines
of overscan on top and 8 lines of overscan on bottom). Many PAL games display
only 256 lines (underscan with black borders).<br/>
Some games such as Chrono Cross will occasionally adjust these values to create
a screen shake effect, so proper emulation of this command is necessary for
those particular cases.<br/>

#### GP1(08h) - Display mode
```
  0-1  HDS   Horizontal Resolution 1     (0=256, 1=320, 2=512, 3=640) ;GP1.R.17-18
  2    VDS   Vertical Resolution         (0=240, 1=480, when Bit5=1)  ;GP1.R.19
  3    NPB   Video Mode                  (0=NTSC/60Hz, 1=PAL/50Hz)    ;GP1.R.20
  4    LBS   Display Area Color Depth    (0=15bit, 1=24bit)           ;GP1.R.21
  5    IRS   Vertical Interlace          (0=Off, 1=On)                ;GP1.R.22
  6    HDS2  Horizontal Resolution 2     (0=256/320/512/640, 1=368)   ;GP1.R.16
  7    REV?  Flip screen horizontally    (0=Off, 1=On, v1 only)       ;GP1.R.14
  8-23       Not used (zero)
```
Note: Interlace must be enabled to see all lines in 480-lines mode (interlace
causes ugly flickering, so a non-interlaced low resolution image typically has
better quality than a high resolution interlaced image, a pretty bad example
is the intro screens shown by the BIOS). The Display Area Color Depth bit does
NOT affect GP0 draw commands, which always draw in 15 bit. However, the
Vertical Interlace flag DOES affect GP0 draw commands.<br/>
Bit 7 is referred to as "reverse" by older versions of Sony's GPU library and is
only supported on v1 arcade/prototype GPUs; the only game currently known to use
it is Crypt Killer (Konami GQ). On a v2 GPU setting this bit seems to do
nothing, though nocash's original notes report that it corrupts the display
output instead (possibly on a different sub-revision of the v2 GPU).<br/>

#### GP1(10h) - Read GPU internal register
#### GP1(11h..1Fh) - Mirrors of GP1(10h), Read GPU internal register
After sending the command, the result can be read (immediately) from GP0
register (there's no NOP or other delay required) (namely GP1.R.Bit27 is used
only for VRAM reads, but NOT for register reads, so do not try to wait for that
flag).<br/>
```
  0-23  Register index (via following GP0 read)
```
On v0 GPUs, the following indices are supported:<br/>
```
  00h-01h = Returns Nothing (old value in GP0.read remains unchanged)
  02h     = Read Texture Window setting  ;GP0(E2h) ;20bit/MSBs=Nothing
  03h     = Read Draw area top left      ;GP0(E3h) ;19bit/MSBs=Nothing
  04h     = Read Draw area bottom right  ;GP0(E4h) ;19bit/MSBs=Nothing
  05h     = Read Draw offset             ;GP0(E5h) ;22bit
  06h-07h = Returns Nothing (old value in GP0.read remains unchanged)
  08h-FFFFFFh = Mirrors of 00h..07h
```
On v2 (and v1?) GPUs, the following indices are supported:<br/>
```
  00h-01h = Returns Nothing (old value in GP0.read remains unchanged)
  02h     = Read Texture Window setting  ;GP0(E2h) ;20bit/MSBs=Nothing
  03h     = Read Draw area top left      ;GP0(E3h) ;20bit/MSBs=Nothing
  04h     = Read Draw area bottom right  ;GP0(E4h) ;20bit/MSBs=Nothing
  05h     = Read Draw offset             ;GP0(E5h) ;22bit
  06h     = Returns Nothing (old value in GP0.read remains unchanged)
  07h     = Read GPU version (1 or 2)
  08h     = Unknown (Returns 00000000h) (lightgun? VRAM size set via GP1(09h)?)
  09h-0Fh = Returns Nothing (old value in GP0.read remains unchanged)
  10h-FFFFFFh = Mirrors of 00h..0Fh
```
The selected data is latched in GP0, the same/latched value can be read multiple
times, but, the latch isn't automatically updated when changing GP0 registers.<br/>

#### GP1(09h) - Set VRAM size (v2)
```
  0     Allow Y coordinates in 512-1023 range (0=No/wrap to 0-511, 1=Yes)
  1-23  Unknown (seems to have no effect)
```
Gates whether the upper Y address bit reaches the VRAM address decoder. With
bit 0 = 0 (the default after a GP1(00h) reset) all Y addressing is masked to
9 bits and the upper half of VRAM appears as a mirror of the lower half on
2 MB systems, or as open bus on retail systems where the second half is not
populated. With bit 0 = 1 the full 10-bit Y range is honored: GP0(E1h).bit11
can reference textures in the second half of VRAM, drawing area / drawing
offset / display area registers all accept Y values in 0..1023, and the
Copy / Fill commands address Y across the full bank. The GPU has two
separate chip select outputs for the first and second half; on a retail
console only the first output is used, so enabling this feature on a 1 MB
system will result in textures disappearing if GP0(E1h).bit11 is also set.<br/>
GP1(09h) is supported only on v2 GPUs; v0 GPUs don't support 2 MB VRAM at all
and v1 seems to use command GP1(20h) instead.<br/>

#### GP1(20h) - Set VRAM size (v1)
```
  0-23  Unknown (501h=1 MB, 504h=2 MB, or so?)
```
Seems to be used only on v1 arcade/prototype GPUs. Regular v2 GPUs use GP1(09h)
instead of GP1(20h).<br/>

#### GP1(0Bh) - Unknown/Internal?
```
  0-10  Unknown (GPU crashes after a while when set to 274h..7FFh)
  11-23 Unknown (seems to have no effect)
```
The register doesn't seem to be used by any games.<br/>

#### GP1(0Ah,0Ch..0Fh,21h..3Fh) - N/A
Not used?<br/>

#### GP1(40h..FFh) - N/A (Mirrors)
Mirrors of GP1(00h..3Fh).<br/>

#### Mis-Centered PAL Games (wrong GP1(06h)/GP1(07h) settings)
NTSC games are typically well centered (using X1=260h, and Y1/Y2=88h+/-N).<br/>
PAL games should be centered as X1=260h, and Y1/Y2=A3h+/-N) - these values
would be looking well on a Philips Philetta TV Set, and do also match up with
other common picture positions (eg. as used by Nintendo's SNES console).<br/>
However, most PAL games are using completely different "random" centering
values (maybe caused by different developers trying to match the centering to
the different TV Sets) (although it looks more as if the PAL developers just
went amok: Many PAL games are even using different centerings for their Intro,
Movie, and actual Game sequences).<br/>
In result, most PAL games are looking like crap when playing them on a real
PSX. For PSX emulators it may be recommended to ignore the GP1(06h)/GP1(07h)
centering, and instead, apply auto-centering to PAL games.<br/>
For PAL game developers, it may be recommended to add a screen centering option
(as found in Tomb Raider 3, for example). Unknown if this is really required...
or if X1=260h, and Y1/Y2=A3h+/-N would work fine on most or all PAL TV Sets?<br/>
