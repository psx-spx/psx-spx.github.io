#   GPU Memory Transfer Commands

The next three commands being described are when the high 3 bits are set to the
values 4 (100), 5 (101), and 6 (110). For them, the remaining 29 bits are ignored,
and can be set to any arbitrary value.

#### VRAM to VRAM blitting - command 4 (100)
```
  1st  Command
  2nd  Source Coord      (YyyyXxxxh)  ;Xpos counted in halfwords
  3rd  Destination Coord (YyyyXxxxh)  ;Xpos counted in halfwords
  4th  Width+Height      (YsizXsizh)  ;Xsiz counted in halfwords
```
Copies data within framebuffer. The transfer is affected by Mask setting.<br/>

#### CPU to VRAM blitting - command 5 (101)
```
  1st  Command
  2nd  Destination Coord (YyyyXxxxh)  ;Xpos counted in halfwords
  3rd  Width+Height      (YsizXsizh)  ;Xsiz counted in halfwords
  ...  Data              (...)      <--- usually transferred via DMA
```
Transfers data from CPU to frame buffer. If the number of halfwords to be sent
is odd, an extra halfword should be sent, as packets consist of 32bits words. The
transfer is affected by Mask setting.<br/>

#### VRAM to CPU blitting - command 6 (110)
```
  1st  Command                       ;\
  2nd  Source Coord      (YyyyXxxxh) ; write to GP0 port (as usually)
  3rd  Width+Height      (YsizXsizh) ;/
  ...  Data              (...)       ;<--- read from GP0 port (or via DMA)
```
Transfers data from frame buffer to CPU. Wait for bit27 of the status register
to be set before reading the image data. When the number of halfwords is odd,
an extra halfword is added at the end, as packets consist of 32bits words.<br/>

#### Masking and Rounding for FILL Command parameters
```
  Xpos=(Xpos AND 3F0h)                       ;range 0..3F0h, in steps of 10h
  Ypos=(Ypos AND 1FFh)                       ;range 0..1FFh
  Xsiz=((Xsiz AND 3FFh)+0Fh) AND (NOT 0Fh)   ;range 0..400h, in steps of 10h
  Ysiz=((Ysiz AND 1FFh))                     ;range 0..1FFh
```
Fill does NOT occur when Xsiz=0 or Ysiz=0 (unlike as for Copy commands).
Xsiz=400h works only indirectly: Param=400h is handled as Xsiz=0, however,
Param=3F1h..3FFh is rounded-up and handled as Xsiz=400h.<br/>

Note that because of the height (Ysiz) masking, a maximum of 511 rows can be
filled in a single command. Calling a fill with a full VRAM height of 512 rows
will be ineffective as the height will be masked to 0.<br/>

The 9-bit Ysiz mask is intrinsic to GP0(02h) and applies regardless of the
GP1(09h) state on 2 MB systems. Even with the upper bank enabled, a single
fast-fill can only cover 511 rows at a time; covering the full 1024-row
2 MB VRAM requires two or more fills with appropriate Ypos values. The Ypos
field separately follows the GP1(09h) gating: with bit 0 = 0 it is masked to
9 bits (mirror), with bit 0 = 1 the full 10-bit range is honored. A fill
whose (Ypos + Ysiz) exceeds the addressable VRAM size wraps to the opposite
edge per the Wrapping note below.

#### Masking for COPY Commands parameters
```
  Xpos=(Xpos AND 3FFh)                       ;range 0..3FFh
  Ypos=(Ypos AND 1FFh)                       ;range 0..1FFh
  Xsiz=((Xsiz-1) AND 3FFh)+1                 ;range 1..400h
  Ysiz=((Ysiz-1) AND 1FFh)+1                 ;range 1..200h
```
Parameters are just clipped to 10bit/9bit range, the only special case is that
Size=0 is handled as Size=max. Ysiz is therefore in the range 1..512, and the
formula gives a non-monotone result for raw Ysiz values that have bit 9 set:
e.g. raw Ysiz=513 produces an effective transfer of 1 row, raw Ysiz=520
produces 8 rows, and raw Ysiz=1024 produces 512 rows. Software issuing a
transfer should match the data phase to the effective Ysiz, otherwise the
extra CPU writes will overflow into the GP0 command stream and corrupt the
GPU state.<br/>

On 2 MB systems, the Ypos 9-bit mask above is the masking that applies with
GP1(09h).0=0; with GP1(09h).0=1 the upper Y bit is also honored and Ypos
covers the full 0..1023 range. The Ysiz mask is unchanged. Source / destination
regions may therefore straddle the Y=512 bank boundary cleanly when GP1(09h)
is enabled, including the case where both the source and the destination of a
GP0(80h) blit are on opposite sides of the boundary.<br/>

#### Notes
The coordinates for the above VRAM transfer commands are absolute framebuffer
addresses (not relative to Draw Offset, and not clipped to Draw Area).<br/>
Non-DMA transfers seem to be working at any time, but GPU-DMA Transfers seem to
be working ONLY during V-Blank (outside of V-Blank, portions of the data appear
to be skipped, and the following words arrive at wrong addresses), unknown if
it's possible to change that by whatever configuration settings...? That
problem appears ONLY for continous DMA aka VRAM transfers (linked-list DMA aka
Ordering Table works even outside V-Blank).<br/>

#### Wrapping
If the Source/Dest starting points plus the width/height value exceed the
addressable VRAM size, then the Copy/Fill operations wrap to the opposite
memory edge (without any carry-out from X to Y, nor from Y to X). The
addressable VRAM size is 1024x512 with GP1(09h).0=0 (the default after a
GP1(00h) reset), and 1024x1024 on 2 MB systems with GP1(09h).0=1.<br/>
