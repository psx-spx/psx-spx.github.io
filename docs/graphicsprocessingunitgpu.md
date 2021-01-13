#   Graphics Processing Unit (GPU)
The GPU can render Polygons, Lines, or Rectangles to the Drawing Buffer, and
sends the Display Buffer to the Television Set. Polygons are useful for 3D
graphics (or rotated/scaled 2D graphics), Rectangles are useful for 2D graphics
and Text output.<br/>

[GPU I/O Ports, DMA Channels, Commands, VRAM](graphicsprocessingunitgpu.md#gpu-io-ports-dma-channels-commands-vram)<br/>
[GPU Render Polygon Commands](graphicsprocessingunitgpu.md#gpu-render-polygon-commands)<br/>
[GPU Render Line Commands](graphicsprocessingunitgpu.md#gpu-render-line-commands)<br/>
[GPU Render Rectangle Commands](graphicsprocessingunitgpu.md#gpu-render-rectangle-commands)<br/>
[GPU Rendering Attributes](graphicsprocessingunitgpu.md#gpu-rendering-attributes)<br/>
[GPU Memory Transfer Commands](graphicsprocessingunitgpu.md#gpu-memory-transfer-commands)<br/>
[GPU Other Commands](graphicsprocessingunitgpu.md#gpu-other-commands)<br/>
[GPU Display Control Commands (GP1)](graphicsprocessingunitgpu.md#gpu-display-control-commands-gp1)<br/>
[GPU Status Register](graphicsprocessingunitgpu.md#gpu-status-register)<br/>
[GPU Versions](graphicsprocessingunitgpu.md#gpu-versions)<br/>
[GPU Depth Ordering](graphicsprocessingunitgpu.md#gpu-depth-ordering)<br/>
[GPU Video Memory (VRAM)](graphicsprocessingunitgpu.md#gpu-video-memory-vram)<br/>
[GPU Texture Caching](graphicsprocessingunitgpu.md#gpu-texture-caching)<br/>
[GPU Timings](graphicsprocessingunitgpu.md#gpu-timings)<br/>
[GPU (MISC)](graphicsprocessingunitgpu.md#gpu-misc)<br/>



##   GPU I/O Ports, DMA Channels, Commands, VRAM
#### GPU I/O Ports (1F801810h and 1F801814h in Read/Write Directions)
```
  Port            Name    Expl.
  1F801810h-Write GP0     Send GP0 Commands/Packets (Rendering and VRAM Access)
  1F801814h-Write GP1     Send GP1 Commands (Display Control) (and DMA Control)
  1F801810h-Read  GPUREAD Receive responses to GP0(C0h) and GP1(10h) commands
  1F801814h-Read  GPUSTAT Receive GPU Status Register
```
It (=GP0 only?) has a 64-byte (16-word) command FIFO buffer.<br/>
Optionally, Port 1F801810h (Read/Write) can be also accessed via DMA2.<br/>
The communication between the CPU and the GPU is a 32-bits data-only bus called
the VBUS. Aside from address line 2 being connected, in order to make the difference
between port 0 and 1, there are no other address line between the two chips.<br/>
Thus the GPU can be seen as a blackbox that executes 32 bits commands.<br/>

#### GPU Timers / Synchronization
Most of the Timers are bound to GPU timings, see<br/>
[Timers](timers.md)<br/>
[Interrupts](interrupts.md)<br/>

#### GPU-related DMA Channels (DMA2 and DMA6)
```
  Channel                   Recommended for
  DMA2 in Linked Mode     - Sending rendering commands  ;GP0(20h..7Fh,E1h..E6h)
  DMA2 in Continuous Mode - VRAM transfers to/from GPU  ;GP0(A0h,C0h)
  DMA6                    - Initializing the Link List  ;Main RAM
```
Note: Before using DMA2, set up the DMA Direction in GP1(04h).<br/>
DMA2 is equivalent to accessing Port 1F801810h (GP0/GPUREAD) by software.<br/>
DMA6 just initializes data in Main RAM (not physically connected to the GPU).<br/>

#### GPU Command Summary
While it is probably more simple for the MIPS software to see GPU commands
as a collection of bytes, the GPU will only see 32 bits words being sent to it.
Therefore, while the Sony libraries will fill up structures to send to the GPU
using byte-level granularity, it is much more simple to see these as bitmasks
from the GPU's point of view.<br/>
So when processing commands on GP0, the GPU will first inspect the top 3 bits
of the 32 bits command being sent. Depending on the value of these 3 bits,
further decoding of the other bits can be done.<br/>
Commands sent to GP1 are more simple in nature to decode.<br/>
<br/>
Top 3 bits of a GP0 command:
```
  0 (000)      Misc commands
  1 (001)      Polygon primitive
  2 (010)      Line primitive
  3 (011)      Rectangle primitive
  4 (100)      VRAM-to-VRAM blit
  5 (101)      CPU-to-VRAM blit
  6 (110)      VRAM-to-CPU blit
  7 (111)      Environment commands
```
Some GP0 commands require additional parameters, which are written (following
the initial command) as further 32bit values to GP0. The execution of the command
starts when all parameters have been received (or, in case of Polygon/Line
commands, when the first 3/2 vertices have been received).

The astute reader will realize that there are shared bits between primitives, such
as the gouraud shading flag.

Unlike all the others, the environment commands are more clear to be seen as a single
8 bits command, therefore the rest of the document will refer to them by their
full 8 bits value.

#### Clear Cache
```
  1st  Command           (01000000h)
```
The GPU has a small texture cache, in order to reduce VRAM access. This command
flushes it, when mutating the VRAM, similar to how the CPU i-cache must be
flushed after writing new code and before executing it.<br/>
Note that it is possible to abuse the texture cache by changing pixels in VRAM that
the GPU loaded in its cache, therefore creating weird drawing effects, but this is
only seen in some demos, and never in actual games.<br/>

#### Quick Rectangle Fill
```
  1st  Color+Command     (02BbGgRrh)  ;24bit RGB value (see note)
  2nd  Top Left Corner   (YyyyXxxxh)  ;Xpos counted in halfwords, steps of 10h
  3rd  Width+Height      (YsizXsizh)  ;Xsiz counted in halfwords, steps of 10h
```
Fills the area in the frame buffer with the value in RGB. Horizontally the
filling is done in 16-pixel (32-bytes) units (see below masking/rounding).<br/>
The "Color" parameter is a 24bit RGB value, however, the actual fill data is
16bit: The hardware automatically converts the 24bit RGB value to 15bit RGB
(with bit15=0).<br/>
Fill is NOT affected by the Mask settings (acts as if Mask.Bit0,1 are both
zero).<br/>
This command is typically used to do a quick clear, as it'll be faster to run
than an equivalent Rectangle command.

#### VRAM Overview / VRAM Addressing
VRAM is 1MByte (not mapped to the CPU bus) (it can be read/written only via I/O
or DMA). The memory is used for:<br/>
```
  Framebuffer(s)      ;Usually 2 buffers (Drawing Area, and Display Area)
  Texture Page(s)     ;Required when using Textures
  Texture Palette(s)  ;Required when using 4bit/8bit Textures
```
The 1MByte VRAM is organized as 512 lines of 2048 bytes. It is accessed via
coordinates, ranging from (0,0)=Upper-Left to (N,511)=Lower-Right.<br/>
```
  Unit  = 4bit  8bit  16bit  24bit   Halfwords   | Unit   = Lines
  Width = 4096  2048  1024   682.66  1024        | Height = 512
```
The horizontal coordinates are addressing memory in
4bit/8bit/16bit/24bit/halfword units (depending on what data formats you are
using) (or a mixup thereof, eg. a halfword-base address, plus a 4bit texture
coordinate).<br/>

##   GPU Render Polygon Commands
When the upper 3 bits of the first GP0 command are set to 1 (001), then the command can
be decoded using the following bitfield:
```
 bit number   value   meaning
  31-29        001    polygon render
    28         1/0    gouraud / flat shading
    27         1/0    4 / 3 vertices
    26          1     textured / untextured
    25         1/0    semi transparent / solid
    24          0     texture blending
   23-0        rgb    first color value.
```

Subsequent data sent to GP0 to complete this command will be the vertex data for the
command. The meaning and count of these words will be altered by the initial flags
sent in the first command.

If doing flat rendering, no further color will be sent. If doing gouraud shading,
there will be one more color per vertex sent, and the initial color will be the
one for vertex 0.

If doing 3 or 4 vertices rendering, this will affect the total number of vertex sent.

If doing textured rendering, each vertex sent will also have a U/V texture coordinate
attached to it, as well as a CLUT index.

So each vertex data can be seen as the following set of words:
```
Color      xxBBGGRR    - optional, only present for gouraud shading
Vertex     YYYYXXXX    - required, two signed 16 bits values
UV         ClutUUVV    - optional, only present for textured polygons
```

The Clut index is only relevant for the first vertex seen in the stream of data. Any
further Clut index ought to be set to 0.

So for example, a solid flat blue triangle of coordinate (10, 20), (30, 40), (50, 60)
will be drawn using the following draw call data:
```
200000FF
00100020
00300040
00500060
```

And a quad with gouraud shading texture-blend will have the following structure:
```
2CR1G1B1
Yyy1Xxx1
ClutU1V1
00R2G2B2
Yyy2Xxx2
0000U2V2
00R3G3B3
Yyy3Xxx3
0000U3V3
00R4G4B4
Yyy4Xxx4
0000U4V4
```

Some combination of these flags can be seen as nonsense however, but it's important
to realize that the GPU will still process them properly. For instance, specifying
gouraud shading without texture blending will force the user to send the colors for
each vertex to satisfy the GPU's state machine, without them being actually used for
the rendering.

#### Notes
Polygons are displayed up to \<excluding\> their lower-right coordinates.<br/>
Four-point polygons are internally processed as two Three-point polygons, the
first consisting of Vertices 1,2,3, and the second of  Vertices 2,3,4.<br/>
Within the Three-point polygons, the ordering of the vertices is don't care at
the GPU side (a front-back check, based on clockwise or anti-clockwise
ordering, can be implemented at the GTE side).<br/>
Dither enable (in Texpage command) affects ONLY polygons that do use Gouraud
Shading or Texture Blending.<br/>

##   GPU Render Line Commands
When the upper 3 bits of the first GP0 command are set to 2 (010), then the command can
be decoded using the following bitfield:
```
 bit number   value   meaning
  31-29        010    line render
    28         1/0    gouraud / flat shading
    27         1/0    polyline / single line
    25         1/0    semi transparent / solid
   23-0        rgb    first color value.
```

So each vertex can be seen as the following list of words:
```
Color      xxBBGGRR    - optional, only present for gouraud shading
Vertex     YYYYXXXX    - required, two signed 16 bits values
```

When the polyline mode is active, then there is no fixed amount of words
to be sent. The last word will have a magic value, which will usually be
55555555, but also sometimes 50005000. Note that the magic value can then
either be for the color word, or the vertex word.


#### Note
Lines are displayed up to \<including\> their lower-right coordinates (ie.
unlike as for polygons, the lower-right coordinate is not excluded).<br/>
If dithering is enabled (via Texpage command), then both monochrome and shaded
lines are drawn with dithering (this differs from monochrome polygons and
monochrome rectangles).<br/>

#### Wire-Frame
Poly-Lines can be used (among others) to create Wire-Frame polygons (by setting
the last Vertex equal to Vertex 1).<br/>



##   GPU Render Rectangle Commands
Rectangles are drawn much faster than polygons. Unlike polygons, gouraud
shading is not possible, dithering isn't applied, the rectangle must forcefully
have horizontal and vertical edges, textures cannot be rotated or scaled, and,
of course, the GPU does render Rectangles as a single entity, without splitting
them into two triangles.<br/>

The Rectangle command can be decoded using the following bitfield:
```
 bit number   value   meaning
  31-29        011    rectangle render
  28-27        sss    rectangle size
    26         1/0    textured / untextured
    25         1/0    semi transparent / solid
   23-0        rgb    first color value.
```

The `size` parameter can be seen as the following enum:

```
  0 (00)      variable size
  1 (01)      single pixel (1x1)
  2 (10)      8x8 sprite
  3 (11)      16x16 sprite
```

Therefore, the whole draw call can be seen as the following sequence of words:
```
Color      ccBBGGRR    - command + color; color is ignored when textured
Vertex1    YYYYXXXX    - required, indicates the upper left corner to render
UV         ClutUUVV    - optional, only present for textured rectangles
Vertex2    YYYYXXXX    - optional, bottom right corner for variable sized rectangles
```

Unlike for Textured-Polygons, the "Texpage" must be set up separately for
Rectangles, via GP0(E1h). Width and Height can be up to 1023x511, however, the
maximum size of the texture window is 256x256 (so the source data will be
repeated when trying to use sizes larger than 256x256).<br/>

#### Texture Origin and X/Y-Flip
Vertex & Texcoord specify the upper-left edge of the rectangle. And,
normally, screen coords and texture coords are both incremented during
rendering the rectangle pixels.<br/>
Optionally, X/Y-Flip bits can be set in Texpage.Bit12/13, these bits cause the
texture coordinates to be decremented (instead of incremented). The X/Y-Flip
bits do affect only Rectangles (not Polygons, nor VRAM Transfers).<br/>
Caution: Reportedly, the X/Y-Flip feature isn't supported on old PSX consoles
(unknown which ones exactly, maybe such with PU-7 mainboards, and unknown how
to detect flipping support; except of course by reading VRAM).<br/>

#### Note
There are also two VRAM Transfer commands which work similar to GP0(60h) and
GP0(65h). Eventually, that commands might be even faster... although not sure
if they do use the Texture Cache?<br/>
The difference is that VRAM Transfers do not clip to the Drawig Area boundary,
do not support fully-transparent nor semi-transparent texture pixels, and do
not convert color depths (eg. without 4bit texture to 16bit framebuffer
conversion).<br/>



##   GPU Rendering Attributes
#### Vertex (Parameter for Polygon, Line, Rectangle commands)
```
  0-10   X-coordinate (signed, -1024..+1023)
  11-15  Not used (usually sign-extension, but ignored by hardware)
  16-26  Y-coordinate (signed, -1024..+1023)
  26-31  Not used (usually sign-extension, but ignored by hardware)
```
Size Restriction: The maximum distance between two vertices is 1023
horizontally, and 511 vertically. Polygons and lines that are exceeding that
dimensions are NOT rendered. For example, a line from Y1=-300 to Y2=+300 is NOT
rendered, a line from Y1=-100 to Y2=+400 is rendered (as far as it is within
the drawing area).<br/>
If portions of the polygon/line/rectangle are located outside of the drawing
area, then the hardware renders only the portion that is inside of the drawing
area. Not sure if the hardware is skipping all clipped pixels at once (within a
single clock cycle), or if it's (slowly) processing them pixel by pixel?<br/>

#### Color Attribute (Parameter for all Rendering commands, except Raw Texture)
```
  0-7    Red   (0..FFh)
  8-15   Green (0..FFh)
  16-23  Blue  (0..FFh)
  24-31  Command (in first paramter) (don't care in further parameters)
```
Caution: For untextured graphics, 8bit RGB values of FFh are brightest.
However, for texture blending, 8bit values of 80h are brightest (values
81h..FFh are "brighter than bright" allowing to make textures about twice as
bright as than they were originially stored in memory; of course the results
can't exceed the maximum brightness, ie. the 5bit values written to the
framebuffer are saturated to max 1Fh).<br/>

#### Texpage Attribute (Parameter for Textured-Polygons commands)
```
  0-8    Same as GP0(E1h).Bit0-8 (see there)
  9-10   Unused (does NOT change GP0(E1h).Bit9-10)
  11     Same as GP0(E1h).Bit11  (see there)
  12-13  Unused (does NOT change GP0(E1h).Bit12-13)
  14-15  Unused (should be 0)
```
This attribute is used in all Textured-Polygons commands.<br/>

#### Clut Attribute (Color Lookup Table, aka Palette)
This attribute is used in all Textured Polygon/Rectangle commands. Of course,
it's relevant only for 4bit/8bit textures (don't care for 15bit textures).<br/>
```
  0-5      X coordinate X/16  (ie. in 16-halfword steps)
  6-14     Y coordinate 0-511 (ie. in 1-line steps)
  15       Unknown/unused (should be 0)
```
Specifies the location of the CLUT data within VRAM.<br/>

#### GP0(E1h) - Draw Mode setting (aka "Texpage")
```
  0-3   Texture page X Base   (N*64) (ie. in 64-halfword steps)    ;GPUSTAT.0-3
  4     Texture page Y Base   (N*256) (ie. 0 or 256)               ;GPUSTAT.4
  5-6   Semi Transparency     (0=B/2+F/2, 1=B+F, 2=B-F, 3=B+F/4)   ;GPUSTAT.5-6
  7-8   Texture page colors   (0=4bit, 1=8bit, 2=15bit, 3=Reserved);GPUSTAT.7-8
  9     Dither 24bit to 15bit (0=Off/strip LSBs, 1=Dither Enabled) ;GPUSTAT.9
  10    Drawing to display area (0=Prohibited, 1=Allowed)          ;GPUSTAT.10
  11    Texture Disable (0=Normal, 1=Disable if GP1(09h).Bit0=1)   ;GPUSTAT.15
          (Above might be chipselect for (absent) second VRAM chip?)
  12    Textured Rectangle X-Flip   (BIOS does set this bit on power-up...?)
  13    Textured Rectangle Y-Flip   (BIOS does set it equal to GPUSTAT.13...?)
  14-23 Not used (should be 0)
  24-31 Command  (E1h)
```
The GP0(E1h) command is required only for Lines, Rectangle, and
Untextured-Polygons (for Textured-Polygons, the data is specified in form of
the Texpage attribute; except that, Bit9-10 can be changed only via GP0(E1h),
not via the Texpage attribute).<br/>
Texture page colors setting 3 (reserved) is same as setting 2 (15bit).<br/>
Note: GP0(00h) seems to be often inserted between Texpage and Rectangle
commands, maybe it acts as a NOP, which may be required between that commands,
for timing reasons...?<br/>

#### GP0(E2h) - Texture Window setting
```
  0-4    Texture window Mask X   (in 8 pixel steps)
  5-9    Texture window Mask Y   (in 8 pixel steps)
  10-14  Texture window Offset X (in 8 pixel steps)
  15-19  Texture window Offset Y (in 8 pixel steps)
  20-23  Not used (zero)
  24-31  Command  (E2h)
```
Mask specifies the bits that are to be manipulated, and Offset contains the new
values for these bits, ie. texture X/Y coordinates are adjusted as so:<br/>
```
  Texcoord = (Texcoord AND (NOT (Mask*8))) OR ((Offset AND Mask)*8)
```
The area within a texture window is repeated throughout the texture page. The
data is not actually stored all over the texture page but the GPU reads the
repeated patterns as if they were there.<br/>

#### GP0(E3h) - Set Drawing Area top left (X1,Y1)
#### GP0(E4h) - Set Drawing Area bottom right (X2,Y2)
```
  0-9    X-coordinate (0..1023)
  10-18  Y-coordinate (0..511)   ;\on Old 160pin GPU (max 1MB VRAM)
  19-23  Not used (zero)         ;/
  10-19  Y-coordinate (0..1023)  ;\on New 208pin GPU (max 2MB VRAM)
  20-23  Not used (zero)         ;/(retail consoles have only 1MB though)
  24-31  Command  (Exh)
```
Sets the drawing area corners. The Render commands GP0(20h..7Fh) are
automatically clipping any pixels that are outside of this region.<br/>

#### GP0(E5h) - Set Drawing Offset (X,Y)
```
  0-10   X-offset (-1024..+1023) (usually within X1,X2 of Drawing Area)
  11-21  Y-offset (-1024..+1023) (usually within Y1,Y2 of Drawing Area)
  22-23  Not used (zero)
  24-31  Command  (E5h)
```
If you have configured the GTE to produce vertices with coordinate "0,0" being
located in the center of the drawing area, then the Drawing Offset must be
"X1+(X2-X1)/2, Y1+(Y2-Y1)/2". Or, if coordinate "0,0" shall be the upper-left
of the Drawing Area, then Drawing Offset should be "X1,Y1". Where X1,Y1,X2,Y2
are the values defined with GP0(E3h-E4h).<br/>

#### GP0(E6h) - Mask Bit Setting
```
  0     Set mask while drawing (0=TextureBit15, 1=ForceBit15=1)   ;GPUSTAT.11
  1     Check mask before draw (0=Draw Always, 1=Draw if Bit15=0) ;GPUSTAT.12
  2-23  Not used (zero)
  24-31 Command  (E6h)
```
When bit0 is off, the upper bit of the data written to the framebuffer is equal
to bit15 of the texture color (ie. it is set for colors that are marked as
"semi-transparent") (for untextured polygons, bit15 is set to zero).<br/>
When bit1 is on, any (old) pixels in the framebuffer with bit15=1 are
write-protected, and cannot be overwritten by (new) rendering commands.<br/>
The mask setting affects all rendering commands, as well as CPU-to-VRAM and
VRAM-to-VRAM transfer commands (where it acts on the separate halfwords, ie. as
for 15bit textures). However, Mask does NOT affect the Fill-VRAM command.<br/>
This setting is used in games such as Metal Gear Solid and Silent Hill.

#### Note
GP0(E3h..E5h) do not take up space in the FIFO, so they are probably executed
immediately (even if there're still other commands in the FIFO). Best use them
only if you are sure that the FIFO is empty (otherwise the new Drawing Area
settings might accidentally affect older Rendering Commands in the FIFO).<br/>



##   GPU Memory Transfer Commands

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
  ...  Data              (...)       ;<--- read from GPUREAD port (or via DMA)
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

Note that because of the height (Ysiz) masking, a maximum of 511 rows can be filled in a single command. Calling a fill with a full VRAM height of 512 rows will be ineffective as the height will be masked to 0.

#### Masking for COPY Commands parameters
```
  Xpos=(Xpos AND 3FFh)                       ;range 0..3FFh
  Ypos=(Ypos AND 1FFh)                       ;range 0..1FFh
  Xsiz=((Xsiz-1) AND 3FFh)+1                 ;range 1..400h
  Ysiz=((Ysiz-1) AND 1FFh)+1                 ;range 1..200h
```
Parameters are just clipped to 10bit/9bit range, the only special case is that
Size=0 is handled as Size=max.<br/>

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
1024x512 pixel VRAM size, then the Copy/Fill operations wrap to the opposite
memory edge (without any carry-out from X to Y, nor from Y to X).<br/>



##   GPU Other Commands
#### GP0(1Fh) - Interrupt Request (IRQ1)
```
  1st  Command           (Cc000000h)                    ;GPUSTAT.24
```
Requests IRQ1. Can be acknowledged via GP1(02h). This feature is rarely used.<br/>
Note: The command is used by Blaze'n'Blade, but the game doesn't have IRQ1
enabled, and the written value (1F801810h) looks more like an I/O address,
rather than like a command, so not sure if it's done intentionally, or if it is
just a bug.<br/>

#### GP0(03h) - Unknown?
Unknown. Doesn't seem to be used by any games. Unlike the "NOP" commands,
GP0(03h) does take up space in FIFO, so it is apparently not a NOP.<br/>

#### GP0(00h) - NOP (?)
This command doesn't take up space in the FIFO (eg. even if a VRAM-to-VRAM
transfer is still busy, one can send dozens of GP0(00h) commands, without the
command FIFO becoming full. So, either the command is ignored (or, if it has a
function, it is executed immediately, even while the transfer is busy).<br/>
...<br/>
GP0(00h) unknown, used with parameter = 08A16Ch... or rather 08FDBCh ... the
written value seems to be a bios/ram memory address, anded with 00FFFFFFh...
maybe a bios bug?<br/>
GP0(00h) seems to be often inserted between Texpage and Rectangle commands,
maybe it acts as a NOP, which may be required between that commands, for timing
reasons...?<br/>

#### GP0(04h..1Eh,E0h,E7h..EFh) - Mirrors of GP0(00h) - NOP (?)
Like GP0(00h), these commands don't take up space in the FIFO. So, maybe, they
are same as GP0(00h), however, the Drawing Area/Offset commands GP0(E3h..E5h)
don't take up FIFO space either, so not taking up FIFO space doesn't
neccessarily mean that the command has no function.<br/>


##   GPU Display Control Commands (GP1)
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
Accordingly, GPUSTAT becomes 14802000h. The x1,y1 values are too small, ie. the
upper-left edge isn't visible. Note that GP1(09h) is NOT affected by the reset
command.<br/>

#### GP1(01h) - Reset Command Buffer
```
  0-23  Not used (zero)
```
Resets the command buffer and CLUT cache.<br/>

#### GP1(02h) - Acknowledge GPU Interrupt (IRQ1)
```
  0-23  Not used (zero)                                        ;GPUSTAT.24
```
Resets the IRQ flag in GPUSTAT.24. The flag can be set via GP0(1Fh).<br/>

#### GP1(03h) - Display Enable
```
  0     Display On/Off   (0=On, 1=Off)                         ;GPUSTAT.23
  1-23  Not used (zero)
```
Turns display on/off. "Note that a turned off screen still gives the flicker of
NTSC on a PAL screen if NTSC mode is selected."<br/>
The "Off" settings displays a black picture (and still sends /SYNC signals to
the television set). (Unknown if it still generates vblank IRQs though?)<br/>

#### GP1(04h) - DMA Direction / Data Request
```
  0-1  DMA Direction (0=Off, 1=FIFO, 2=CPUtoGP0, 3=GPUREADtoCPU) ;GPUSTAT.29-30
  2-23 Not used (zero)
```
Notes: Manually sending/reading data by software (non-DMA) is ALWAYS possible,
regardless of the GP1(04h) setting. The GP1(04h) setting does affect the
meaning of GPUSTAT.25.<br/>

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
  10-18 Y (0-511)     (scanline number in VRAM)   (relative to begin of VRAM)
  19-23 Not used (zero)
```
Upper/left Display source address in VRAM. The size and target position on
screen is set via Display Range registers; target=X1,Y2;
size=(X2-X1/cycles\_per\_pix), (Y2-Y1).<br/>

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
Video clock unit used depends on console region, regardless of NTSC/PAL video mode set by GP1(08h).3; see section on [nominal video clocks](#nominal-video-clock) for values.<br/>

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
lines, but on most analog television sets, only 224 lines are visible (8 lines of overscan on top and 8 lines of overscan on bottom). Many PAL games display only 256 lines (underscan with black borders).<br/>
Some games such as Chrono Cross will occasionally adjust these values to create a screen shake effect, so proper emulation of this command is necessary for those particular cases.<br/>

#### GP1(08h) - Display mode
```
  0-1   Horizontal Resolution 1     (0=256, 1=320, 2=512, 3=640) ;GPUSTAT.17-18
  2     Vertical Resolution         (0=240, 1=480, when Bit5=1)  ;GPUSTAT.19
  3     Video Mode                  (0=NTSC/60Hz, 1=PAL/50Hz)    ;GPUSTAT.20
  4     Display Area Color Depth    (0=15bit, 1=24bit)           ;GPUSTAT.21
  5     Vertical Interlace          (0=Off, 1=On)                ;GPUSTAT.22
  6     Horizontal Resolution 2     (0=256/320/512/640, 1=368)   ;GPUSTAT.16
  7     "Reverseflag"               (0=Normal, 1=Distorted)      ;GPUSTAT.14
  8-23  Not used (zero)
```
Note: Interlace must be enabled to see all lines in 480-lines mode (interlace
is causing ugly flickering, so a non-interlaced low resolution image is
typically having better quality than a high resolution interlaced image, a
pretty bad example are the intro screens shown by the BIOS). The Display Area
Color Depth does NOT affect the Drawing Area (the Drawing Area is
\<always\> 15bit).<br/>
When the "Reverseflag" is set, the display scrolls down 2 lines or so, and
colored regions are getting somehow hatched/distorted, but black and white
regions are still looking okay. Don't know what that's good for? Probably
relates to PAL/NTSC-Color Clock vs PSX-Dot Clock mismatches: Bit7=0 causes
Flimmering errors (errors at different locations in each frame), and Bit7=1
causes Static errors (errors at same locations in all frames)?<br/>

#### GP1(10h) - Get GPU Info
#### GP1(11h..1Fh) - Mirrors of GP1(10h), Get GPU Info
After sending the command, the result can be read (immediately) from GPUREAD
register (there's no NOP or other delay required) (namely GPUSTAT.Bit27 is used
only for VRAM-Reads, but NOT for GPU-Info-Reads, so do not try to wait for that
flag).<br/>
```
  0-23  Select Information which is to be retrieved (via following GPUREAD)
```
On Old 180pin GPUs, following values can be selected:<br/>
```
  00h-01h = Returns Nothing (old value in GPUREAD remains unchanged)
  02h     = Read Texture Window setting  ;GP0(E2h) ;20bit/MSBs=Nothing
  03h     = Read Draw area top left      ;GP0(E3h) ;19bit/MSBs=Nothing
  04h     = Read Draw area bottom right  ;GP0(E4h) ;19bit/MSBs=Nothing
  05h     = Read Draw offset             ;GP0(E5h) ;22bit
  06h-07h = Returns Nothing (old value in GPUREAD remains unchanged)
  08h-FFFFFFh = Mirrors of 00h..07h
```
On New 208pin GPUs, following values can be selected:<br/>
```
  00h-01h = Returns Nothing (old value in GPUREAD remains unchanged)
  02h     = Read Texture Window setting  ;GP0(E2h) ;20bit/MSBs=Nothing
  03h     = Read Draw area top left      ;GP0(E3h) ;20bit/MSBs=Nothing
  04h     = Read Draw area bottom right  ;GP0(E4h) ;20bit/MSBs=Nothing
  05h     = Read Draw offset             ;GP0(E5h) ;22bit
  06h     = Returns Nothing (old value in GPUREAD remains unchanged)
  07h     = Read GPU Type (usually 2)    ;see "GPU Versions" chapter
  08h     = Unknown (Returns 00000000h) (lightgun on some GPUs?)
  09h-0Fh = Returns Nothing (old value in GPUREAD remains unchanged)
  10h-FFFFFFh = Mirrors of 00h..0Fh
```
The selected data is latched in GPUREAD, the same/latched value can be read
multiple times, but, the latch isn't automatically updated when changing GP0
registers.<br/>

#### GP1(09h) - New Texture Disable
```
  0     Texture Disable (0=Normal, 1=Allow Disable via GP0(E1h).11) ;GPUSTAT.15
  1-23  Unknown (seems to have no effect)
```
This feature seems to be intended for debugging purposes (most released games
do contain program code for disabling textures, but do never execute it).<br/>
GP1(09h) seems to be supported only on New GPUs. Old GPUs don't support it all,
and there seem to be some Special/Prototype GPUs that use GP1(20h) instead of
GP1(09h).<br/>

#### GP1(20h) - Special/Prototype Texture Disable
```
  0-23  Unknown (501h=Texture Enable, 504h=Texture Disable, or so?)
```
Seems to be a used only on whatever arcade/prototype GPUs. New GPUs are using
GP1(09h) instead of GP1(20h).<br/>

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



##   GPU Status Register
#### 1F801814h - GPUSTAT - GPU Status Register (R)
```
  0-3   Texture page X Base   (N*64)                              ;GP0(E1h).0-3
  4     Texture page Y Base   (N*256) (ie. 0 or 256)              ;GP0(E1h).4
  5-6   Semi Transparency     (0=B/2+F/2, 1=B+F, 2=B-F, 3=B+F/4)  ;GP0(E1h).5-6
  7-8   Texture page colors   (0=4bit, 1=8bit, 2=15bit, 3=Reserved)GP0(E1h).7-8
  9     Dither 24bit to 15bit (0=Off/strip LSBs, 1=Dither Enabled);GP0(E1h).9
  10    Drawing to display area (0=Prohibited, 1=Allowed)         ;GP0(E1h).10
  11    Set Mask-bit when drawing pixels (0=No, 1=Yes/Mask)       ;GP0(E6h).0
  12    Draw Pixels           (0=Always, 1=Not to Masked areas)   ;GP0(E6h).1
  13    Interlace Field       (or, always 1 when GP1(08h).5=0)
  14    "Reverseflag"         (0=Normal, 1=Distorted)             ;GP1(08h).7
  15    Texture Disable       (0=Normal, 1=Disable Textures)      ;GP0(E1h).11
  16    Horizontal Resolution 2     (0=256/320/512/640, 1=368)    ;GP1(08h).6
  17-18 Horizontal Resolution 1     (0=256, 1=320, 2=512, 3=640)  ;GP1(08h).0-1
  19    Vertical Resolution         (0=240, 1=480, when Bit22=1)  ;GP1(08h).2
  20    Video Mode                  (0=NTSC/60Hz, 1=PAL/50Hz)     ;GP1(08h).3
  21    Display Area Color Depth    (0=15bit, 1=24bit)            ;GP1(08h).4
  22    Vertical Interlace          (0=Off, 1=On)                 ;GP1(08h).5
  23    Display Enable              (0=Enabled, 1=Disabled)       ;GP1(03h).0
  24    Interrupt Request (IRQ1)    (0=Off, 1=IRQ)       ;GP0(1Fh)/GP1(02h)
  25    DMA / Data Request, meaning depends on GP1(04h) DMA Direction:
          When GP1(04h)=0 ---> Always zero (0)
          When GP1(04h)=1 ---> FIFO State  (0=Full, 1=Not Full)
          When GP1(04h)=2 ---> Same as GPUSTAT.28
          When GP1(04h)=3 ---> Same as GPUSTAT.27
  26    Ready to receive Cmd Word   (0=No, 1=Ready)  ;GP0(...) ;via GP0
  27    Ready to send VRAM to CPU   (0=No, 1=Ready)  ;GP0(C0h) ;via GPUREAD
  28    Ready to receive DMA Block  (0=No, 1=Ready)  ;GP0(...) ;via GP0
  29-30 DMA Direction (0=Off, 1=?, 2=CPUtoGP0, 3=GPUREADtoCPU)    ;GP1(04h).0-1
  31    Drawing even/odd lines in interlace mode (0=Even or Vblank, 1=Odd)
```
In 480-lines mode, bit31 changes per frame. And in 240-lines mode, the bit
changes per scanline. The bit is always zero during Vblank (vertical retrace
and upper/lower screen border).<br/>

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
then the GPU does either want to receive data, or it is busy with a command
execution (and doesn't want to receive anything).<br/>
Bit25: This is the DMA Request bit, however, the bit is also useful for non-DMA
transfers, especially in the FIFO State mode.<br/>



##   GPU Versions
#### Summary of GPU Differences
```
  Differences...                Old 160pin GPU          New 208pin GPU
  GPU Chip                      CXD8514Q                CXD8561Q/BQ/CQ/CXD9500Q
  Mainboard                     EARLY-PU-8 and below    LATE-PU-8 and up
  Memory Type                   Dual-ported VRAM        Normal DRAM
  GPUSTAT.13 when interlace=off always 0                always 1
  GPUSTAT.14                    always 0                reverseflag
  GPUSTAT.15                    always 0                texture_disable
  GP1(10h:index3..4)            19bit (1MB VRAM)        20bit (2MB VRAM)
  GP1(10h:index7)               N/A                     00000002h version
  GP1(10h:index8)               mirror of index0        00000000h zero
  GP1(10h:index9..F)            mirror of index1..7     N/A
  GP1(20h)                      whatever? used for detecting old gpu
  GP0(E1h).bit12/13             without x/y-flip        with x/y-flip
  GP0(03h)                      N/A (no stored in fifo) unknown/unused command
  Shaded Textures               ((color/8)*texel)/2     (color*texel)/16
  GP0(02h) FillVram             xpos.bit0-3=0Fh=bugged  xpos.bit0-3=ignored
  dma-to-vram: doesn't work with blksiz>10h (new gpu works with blksiz=8C0h!)
  dma-to-vram: MAYBE also needs extra software-handshake to confirm DMA done?
   320*224 pix = 11800h pix = 8C00h words
  GP0(80h) VramToVram           works                   Freeze on large moves?
```

#### Shaded Textures
The Old GPU crops 8:8:8 bit gouraud shading color to 5:5:5 bit before
multiplying it with the texture color, resulting in rather poor graphics. For
example, the snow scence in the first level of Tomb Raider I looks a lot
smoother on New GPUs.<br/>
The cropped colors are looking a bit as if dithering would be disabled
(although, technically dithering works fine, but due to the crippled color
input, it's always using the same dither pattern per 8 intensities, instead of
using 8 different dither patterns).<br/>

#### Memory/Rendering Timings
The Old GPU uses two Dual-ported VRAM chips (each with two 16bit databusses,
one for CPU/DMA/rendering access, and one for output to the video DAC). The New
GPU uses s normal DRAM chip (with single 32bit databus).<br/>
The exact timing differences are unknown, but the different memory types should
result in quite different timings:<br/>
The Old GPU might perform better on non-32bit aligned accesses, and on memory
accesses performed simultaneously with DAC output.<br/>
On the other hand, the New GPU's DRAM seems to be faster in some cases (for
example, during Vblank, it's fast enough to perform DMA's with blksiz\>10h,
which exceeds the GPU's FIFO size, and causes lost data on Old GPUs).<br/>

#### X/Y-Flip and 2MB Video RAM
The X/Y-flipping feature may be used by arcade games (provided that the arcade
board is fitted with New GPUs). The flipping feature does also work on retail
consoles with New GPUs, but PSX games should never use that feature (for
maintaining compatiblity with older PSX consoles).<br/>
2Mbyte Video RAM is used on some arcade boards. Whilst PSX retail consoles are
always containing only 1MByte RAM, so the feature cannot be used even if the
console contains a New GPU. There's one special case: Some PSone consoles are
actually fitted with 2MB chips (maybe because smaller chips haven't been in
production anymore), but the chips are wired so that only half of the memory is
accessible (the extra memory could be theoretically unlocked with some minimal
hardware modification).<br/>

#### GPU Detection (and optional texture disable)
Below is slightly customized GPU Detection function taken from Perfect Assassin
(the index7 latching works ONLY on New GPUs, whilst old GPUs would leave the
latched value unchanged; as a workaround, the index4 latching is used to ensure
that the latch won't contain 000002h on old GPUs, assuming that index4 is never
set to 000002h).<br/>
```
  [1F801814h]=10000004h       ;GP1(10h).index4 (latch draw area bottom right)
  [1F801814h]=10000007h       ;GP1(10h).index7 (latch GPU version, if any)
  if ([1F801810h] AND 00FFFFFFh)=00000002h then goto @@gpu_v2
  [1F801810h]=([1F801814h] AND 3FFFh) OR E1001000h ;change GPUSTAT via GP0(E1h)
  dummy=[1F801810h]           ;dummy read (unknown purpose)
  if ([1F801814h] AND 00001000h) then goto @@gpu_v1 else goto @@gpu_v0
 ;---
 @@gpu_v0:  ;Old 160pin GPU (EARLY-PU-8)
  return 0
 ;---
 @@gpu_v1:  ;unknown GPU type, maybe some custom arcade/prototype version ?
  if want_tex_dis then [1F801814h]=20000504h  ;GP1(20h)
  return 1
 ;---
 @@gpu_v2:  ;New 208pin GPU (LATE-PU-8 and up)
  if want_tex_dis then [1F801814h]=09000001h  ;GP1(09h)
  return 2
```

#### GP0(02h) FillVram
The FillVram command does normally ignore the lower 4bit of the x-coordinate
(and software should always set those bits to zero). However, if the 4bits are
all set, then the Old GPU does write each 2nd pixel to wrong memory address.
For example, a 32x4 pixel fill produces following results for x=0..1Fh:<br/>
```
  0h              10h             20h             30h             40h
  |               |               |               |               |
  ################################                                 ;\x=00h..0Eh
  ################################                                 ; and, x=0Fh
  ################################                                 ; on NEW GPU
  ################################                                 ;/
   # # # # # # # ################## # # # # # # #                  ;\
   # # # # # # # ################## # # # # # # #                  ; x=0Fh
   # # # # # # # ################## # # # # # # #                  ; on OLD GPU
   # # # # # # # ################## # # # # # # #                  ;/
                  ################################                 ;\x=10h..1Eh
                  ################################                 ; and, x=1Fh
                  ################################                 ; on NEW GPU
                  ################################                 ;/
                   # # # # # # # ################## # # # # # # #  ;\
                   # # # # # # # ################## # # # # # # #  ; x=1Fh
                   # # # # # # # ################## # # # # # # #  ; on OLD GPU
                   # # # # # # # ################## # # # # # # #  ;/
```

#### Arcade GPUs
Some arcade boards are using normal retail GPUs, however, there are also two
special non-retail 208pin GPUs which seem to be solely used on arcade boards:<br/>
```
  IC21  - 208pin - "SONY CXD8538Q"   ;seen on GP-11 (namco System 11) boards
  IC103 - 208pin - "SONY CXD8654Q"   ;seen on GP-15 (namco System 12) boards
```
The exact differences to retail GPUs are unknown. One of the special GPUs is
said to use entierly different command numbers for rendering commands (maybe
some old prototype variant, or maybe some protection against cloning arcade
boards with retail chips).<br/>



##   GPU Depth Ordering
#### Absent Depth Buffer
The PlayStation's GPU stores only RGB colors in the framebuffer (ie. unlike
modern 3D processors, it's NOT buffering Depth values; leaving apart the Mask
bit, which could be considered as a tiny 1bit "Depth" or "Priority" value). In
fact, the GPU supports only X,Y coordinates, and it's totally unaware of Z
coordinates. So, when rendering a polygon, the hardware CANNOT determine which
of the new pixels are in front/behind of the old pixels in the buffer.<br/>

#### Simple Ordering
The rendering simply takes place in the ordering as the data is sent to the GPU
(ie. the most distant objects should be sent first). For 2D graphics, it's
fairly easy follow that order (eg. even multi-layer 2D graphics can be using
DMA2-continous mode).<br/>

#### Depth Ordering Table (OT)
For 3D graphics, the ordering of the polygons may change more or less randomly
(eg. when rotating/moving the camera). To solve that problem, the whole
rendering data is usually first stored in a Depth Ordering Table (OT) in Main
RAM, and, once when all polygons have been stored in the OT, the OT is sent to
the GPU via "DMA2-linked-list" mode.<br/>

#### Initializing an empty OT (via DMA6)
DMA channel 6 can be used to set up an empty linked list, in which each entry
points to the previous:<br/>
```
  DPCR    - enable bits                                 ;Example=x8xxxxxxh
  D6_MADR - pointer to the LAST table entry             ;Example=8012300Ch
  D6_BCR  - number of list entries                      ;Example=00000004h
  D6_CHCR - control bits (should be 11000002h)          ;Example=11000002h
```
Each entry has a size of 00h words (upper 8bit), and a pointer to the previous
entry (lower 24bit). With the above Example values, the generated table would
look like so:<br/>
```
  [80123000h]=00FFFFFFh  ;1st entry, points to end code (xxFFFFFFh)
  [80123004h]=00123000h  ;2nd entry, points to 1st entry
  [80123008h]=00123004h  ;3rd entry, points to 2nd entry
  [8012300Ch]=00123008h  ;last entry, points to 3rd entry (table entrypoint)
```

#### Inserting Entries (Passing GTE data to the OT) (by software)
The GTE commands AVSZ3 and AVSZ4 can be used to calculate the Average Z
coordinates of a polygon (based on its three or four Z coordinates). The result
is returned as a 16bit Z value in GTE register OTZ, the commands do also allow
to divide the result, to make it less than 16bit (the full 16bit would require
an OT of 256KBytes - for the EMPTY table, which would be a waste of memory, and
which would slowdown the DMA2/DMA6 operations) (on the other hand, a smaller
table means less depth resolution).<br/>
```
  [PacketAddr+0]      = [80123000h+OTZ*4] + (N SHL 24)   <--internal link chain
  [PacketAddr+4..N*4] = GP0 Command(s) and Parameters    <--data (send to GP0)
  [80123000h+OTZ*4]   = PacketAddr AND FFFFFFh           <--internal link chain
```
If there's been already an entry (at the same OTZ index), then the new polygon
will be processed first (ie. it will appear "behind" of the old entry).<br/>
Not sure if the packet size must be limited to max N=16 words (ie. as for the
DMA2-continous block size) (due to GP0 FIFO size limits)?<br/>

#### Sending the OT to the CPU (via DMA2-linked-list mode)
```
  1 - Wait until GPU is ready to receive commands ;GPUSTAT.28
  2 - Enable DMA channel 2                  ;DPCR
  3 - Set GPU to DMA cpu->gpu mode          ;[GP1]=04000002h aka GP1(04h)
  3 - Set D2_MADR to the start of the list  ;(LAST Entry) ;Example=80123010h
  4 - Set D2_BCR to zero                    ;(length unused, end at END-CODE)
  5 - Set D2_CHCR to link mode, mem->GPU and dma enable   ;=01000401h
```



##   GPU Video Memory (VRAM)
#### Framebuffer
The framebuffer contains the image that is to be output to the Television Set.
The GPU supports 10 resolutions, with 16bit or 24bit per pixel.<br/>
```
  Resolution  16bit      24bit      |  Resolution  16bit      24bit
  256x240     120Kbytes  180Kbytes  |  256x480     240Kbytes  360Kbytes
  320x240     150Kbytes  225Kbytes  |  320x480     300Kbytes  450Kbytes
  368x240     xx0Kbytes  xx0Kbytes  |  368x480     xx0Kbytes  xx0Kbytes
  512x240     240Kbytes  360Kbytes  |  512x480     480Kbytes  720Kbytes
  640x240     300Kbytes  450Kbytes  |  640x480     600Kbytes  900Kbytes
```
Note: In most cases, you'll need TWO framebuffers (one being displayed, and
used as rendering target) (unless you are able to draw the whole new image
during vblank, or unless when using single-layer 2D graphics). So, resolutions
that occupy more than 512K would exceed the available 1MB VRAM when using 2
buffers. Also, high resolutions mean higher rendering load, and less texture
memory.<br/>
```
<B>  15bit Direct Display (default) (works with polygons, lines, rectangles)</B>
  0-4   Red       (0..31)
  5-9   Green     (0..31)
  10-14 Blue      (0..31)
  15    Mask flag (0=Normal, 1=Do not allow to overwrite this pixel)
<B>  24bit Direct Display (works ONLY with direct vram transfers)</B>
  0-7    Red      (0..255)
  8-15   Green    (0..255)
  16-23  Blue     (0..255)
```
Note: The 24bit pixels occupy 3 bytes (not 4 bytes with unused MSBs), so each 6
bytes contain two 24bit pixels. The 24bit display mode works only with VRAM
transfer commands like GP0(A0h); the rendering commands GP0(20h..7Fh) cannot
output 24bit data. Ie. 24bit mode is used mostly for MDEC videos (and some 2D
games like Heart of Darkness).<br/>

#### Texture Bitmaps
A texture is an image put on a polygon or sprite. The data of a texture can be
stored in 3 different modes:<br/>
```
<B>  16bit Texture (Direct Color)             ;(One 256x256 page = 128Kbytes)</B>
  0-4   Red       (0..31)         ;\Color 0000h        = Fully-Transparent
  5-9   Green     (0..31)         ; Color 0001h..7FFFh = Non-Transparent
  10-14 Blue      (0..31)         ; Color 8000h..FFFFh = Semi-Transparent (*)
  15    Semi Transparency Flag    ;/(*) or Non-Transparent for opaque commands
<B>  8bit Texture (256 Color Palette)         ;(One 256x256 page = 64Kbytes)</B>
  0-7   Palette index for 1st pixel (left)
  8-15  Palette index for 2nd pixel (right)
<B>  4bit Texture (16 Color Palette)          ;(One 256x256 page = 32Kbytes)</B>
  0-3   Palette index for 1st pixel (left)
  4-7   Palette index for 2nd pixel (middle/left)
  8-11  Palette index for 3rd pixel (middle/right)
  12-15 Palette index for 4th pixel (right)
```
A Texture Page is a 256x256 texel region in VRAM (the Polygon rendering
commands are using Texcoords with 8bit X,Y coordinates, so polygons cannot use
textures bigger than 256x256) (the Rectangle rendering commands with
width/height parameters could theoretically use larger textures, but the
hardware clips their texture coordinates to 8bit, too).<br/>
The GP0(E2h) Texture Window (aka Texture Repeat) command can be used to reduce
the texture size to less than 256x256 texels.<br/>
The Texture Pages can be located in the frame buffer on X multiples of 64
halfwords and Y multiples of 256 lines.<br/>

#### Texture Palettes - CLUT (Color Lookup Table)
The clut is a the table where the colors are stored for the image data in the
CLUT modes. The pixels of those images are used as indexes to this table. The
clut is arranged in the frame buffer as a 256x1 image for the 8bit clut mode,
and a 16x1 image for the 4bit clut mode.<br/>
```
  0-4   Red       (0..31)         ;\Color 0000h        = Fully-Transparent
  5-9   Green     (0..31)         ; Color 0001h..7FFFh = Non-Transparent
  10-14 Blue      (0..31)         ; Color 8000h..FFFFh = Semi-Transparent (*)
  15    Semi Transparency Flag    ;/(*) or Non-Transparent for opaque commands
```
The clut data can be arranged in the frame buffer at X multiples of 16
(X=0,16,32,48,etc) and anywhere in the Y range of 0-511.<br/>

#### Texture Color Black Limitations
On the PSX, texture color 0000h is fully-transparent, that means textures
cannot contain Black pixels. However, in some cases, Color 8000h (Black with
semi-transparent flag) can be used, depending on the rendering command:<br/>
```
  opaque command, eg. GP0(24h)      --> 8000h = Non-Transparent Black
  semi-transp command, eg. GP0(26h) --> 8000h = Semi-Transparent Black
```
So, with semi-transparent rendering commands, it isn't possible to use
Non-Transparent Black pixels in textures, the only workaround is to use colors
like 0001h (dark red) or 0400h (dark blue). However, due to the PSX's rather
steeply increasing intensity ramp, these colors are clearly visible to be
brighter than black.<br/>

#### RGB Intensity Notes
The Playstations RGB values aren't linear to normal RGB values (as used on
PCs). The min/max values are of course the same, but the medium values differ:<br/>
```
  Intensity        PC      PSX
  Minimum          0       0
  Medium (circa)   16      8
  Maximum          31      31
```
Ie. on the PSX, the intensity increases steeply from 0 to 15, and less steeply
from 16 to 31.<br/>



##   GPU Texture Caching
The GPU has 2 Kbyte Texture Cache<br/>
There is also a CLUT cache that is preserved between GPU drawing commands. The CLUT cache is invalidated when different CLUT index values are used or when GP0(01h) is issued. It is unknown if the CLUT cache overlaps or is shared with the Texture Cache.

If polygons with texture are displayed, the GPU needs to read these from the
frame buffer. This slows down the drawing process, and as a result the number
of polygons that can be drawn in a given timespan. To speed up this process the
GPU is equipped with a texture cache, so a given piece of texture needs not to
be read multiple times in succession.<br/>
The texture cache size depends on the color mode used for the textures.<br/>
In 4 bit CLUT mode it has a size of 64x64, in 8 bit CLUT it's 32x64 and in
15bitDirect is 32x32. A general speed up can be achieved by setting up textures
according to these sizes. For further speed gain a more precise knowledge of
how the cache works is necessary.<br/>

#### Cache blocks
The texture page is divided into non-overlapping cache blocks, each of a unit
size according to color mode. These cache blocks are tiled within the texture
page.<br/>
```
  +-----+-----+-----+--
  |cache|     |     |
  |block|     |
  |    0|   1 |    2   ..
  +-----+-----+--
  |..   |     |
```

#### Cache entries
Each cache block is divided into 256 cache entries, which are numbered
sequentially, and are 8 bytes wide. So a cache entry holds 16 4bit clut pixels
8 8bit clut pixels, or 4 15bitdirect pixels.<br/>
```
  4bit and 8bit clut:        15bitdirect:
  +----+----+----+----+     +----+----+----+----+----+----+----+----+
  |   0|   1|   2|   3|     |   0|   1|   2|   3|   4|   5|   6|   7|
  +----+----+----+----+     +----+----+----+----+----+----+----+----+
  |   4|   5|   6|   7|     |   8|   9|   a|   b|   c|   d|   e|   f|
  +----+----+----+----+     +----+----+----+----+----+----+----+----+
  |   8|   9|  ..           |  10|  11|  ..
  +----+----+--             +----+----+--
  |   c|  ..|               |  18|  ..|
  +----+--                  +----+--
  |  ..                     |  ..
```
The cache can hold only one cache entry by the same number, so if f.e. a piece
of texture spans multiple cache blocks and it has data on entry 9 of block 1,
but also on entry 9 of block 2, these cannot be in the cache at once.<br/>



##   GPU Timings
#### Nominal Video Clock

```
  NTSC video clock = 53.693175 MHz
  PAL video clock  = 53.203425 MHz
```
Consoles will always use the video clock for its region, regardless of the GPU being configured in NTSC or PAL output mode, because an NTSC console lacks a PAL reference clock and vice versa. Without modifications for an additional oscillator for the other region, consoles may experience drift over time when playing content from a different video region. See vertical refresh rates below.

#### Vertical Video Timings
```
  263 scanlines per field for NTSC non-interlaced
  262.5 scanlines per field for NTSC interlaced

  314 scanlines per field for PAL non-interlaced
  312.5 scanlines per field for PAL interlaced
```
Horizontal blanking and vertical blanking signals occur on the video output side as expected for NTSC/PAL signals. These are not necessarily the same as the timmer/interrupt HBLANK and VBLANK.

#### Vertical Refresh Rates
```
  NTSC mode on NTSC video clock
  Interlaced:     59.940 Hz
  Non-interlaced: 59.826 Hz

  PAL mode on PAL video clock
  Interlaced:     50.000 Hz
  Non-interlaced: 49.761 Hz

  NTSC mode on PAL video clock
  Interlaced:     59.393 Hz
  Non-interlaced: 59.280 Hz

  PAL mode on NTSC video clock
  Interlaced:     50.460 Hz
  Non-interlaced: 50.219 Hz
```
For emulation purposes, it's recommended to use an NTSC video clock when running NTSC content (or in NTSC mode) and a PAL clock when running PAL content (or in PAL mode).

TODO: Derivations for vertical refresh rates; horizontal timing notes

**Nocash's original GPU Timings notes:**
#### Video Clock
The PSone/PAL video clock is the cpu clock multiplied by 11/7.<br/>
```
  CPU Clock   =  33.868800MHz (44100Hz*300h)
  Video Clock =  53.222400MHz (44100Hz*300h*11/7)
```
For other PSX/PSone PAL/NTSC variants, see:<br/>
[Pinouts - CLK Pinouts](pinouts.md#pinouts---clk-pinouts)<br/>

#### Vertical Timings
```
  PAL:  314 scanlines per frame (13Ah)
  NTSC: 263 scanlines per frame (107h)
```
Timer1 can use the hblank signal as input, allowing to count scanlines (unless
the display is configured to 0 pixels width, which would cause an endless
hblank). The hblank signal is generated even during vertical blanking/retrace.<br/>

#### Horizontal Timings
```
  PAL:  3406 video cycles per scanline (or 3406.1 or so?)
  NTSC: 3413 video cycles per scanline (or 3413.6 or so?)
```
Dotclocks:<br/>
```
  PSX.256-pix Dotclock =  5.322240MHz (44100Hz*300h*11/7/10)
  PSX.320-pix Dotclock =  6.652800MHz (44100Hz*300h*11/7/8)
  PSX.368-pix Dotclock =  7.603200MHz (44100Hz*300h*11/7/7)
  PSX.512-pix Dotclock = 10.644480MHz (44100Hz*300h*11/7/5)
  PSX.640-pix Dotclock = 13.305600MHz (44100Hz*300h*11/7/4)
  Namco GunCon 385-pix =  8.000000MHz (from 8.00MHz on lightgun PCB)
```
Dots per scanline are, depending on horizontal resolution, and on PAL/NTSC:<br/>
```
  320pix/PAL: 3406/8  = 425.75 dots     320pix/NTSC: 3413/8  = 426.625 dots
  640pix/PAL: 3406/4  = 851.5 dots      640pix/NTSC: 3413/4  = 853.25 dots
  256pix/PAL: 3406/10 = 340.6 dots      256pix/NTSC: 3413/10 = 341.3 dots
  512pix/PAL: 3406/5  = 681.2 dots      512pix/NTSC: 3413/5  = 682.6 dots
  368pix/PAL: 3406/7  = 486.5714 dots   368pix/NTSC: 3413/7  = 487.5714 dots
```
Timer0 can use the dotclock as input, however, the Timer0 input "ignores" the
fractional portions (in most cases, the values are rounded down, ie. with 340.6
dots/line, the timer increments only 340 times/line; the only value that is
rounded up is 425.75 dots/line) (for example, due to the rounding, the timer
isn't running exactly twice as fast in 512pix/PAL mode than in 256pix/PAL
mode). The dotclock signal is generated even during horizontal/vertical
blanking/retrace.<br/>

#### Frame Rates
```
  PAL:  53.222400MHz/314/3406 = ca. 49.76 Hz (ie. almost 50Hz)
  NTSC: 53.222400MHz/263/3413 = ca. 59.29 Hz (ie. almost 60Hz)
```

#### Note
Above values include "hidden" dots and scanlines (during horizontal and
vertical blanking/retrace).<br/>



##   GPU (MISC)
#### GP0(20h..7Fh) - Render Command Bits
```
  0-23  Color for (first) Vertex                   (Not for Raw-Texture)
  24    Texture Mode      (0=Blended, 1=Raw)       (Textured-Polygon/Rect only)
  25    Semi Transparency (0=Off, 1=On)            (All Render Types)
  26    Texture Mapping   (0=Off, 1=On)            (Polygon/Rectangle only)
  27-28 Rect Size   (0=Var, 1=1x1, 2=8x8, 3=16x16) (Rectangle only)
  27    Num Vertices      (0=Triple, 1=Quad)       (Polygon only)
  27    Num Lines         (0=Single, 1=Poly)       (Line only)
  28    Shading           (0=Flat, 1=Gouroud)      (Polygon/Line only)
  29-31 Primitive Type    (1=Polygon, 2=Line, 3=Rectangle)
```

#### Perspective (in-)correct Rendering
The PSX doesn't support perspective correct rendering: Assume a polygon to be
rotated so that it's right half becomes more distant to the camera, and it's
left half becomes closer. Due to the GTE's perspective division, the right half
should appear smaller than the left half.<br/>
The GPU supports only linear interpolations for rendering - that is correct
concerning the X and Y screen coordinates (which are still linear to each
other, even after perspective division, since both are divided by the same
value).<br/>
However, texture coordinates (and Gouraud shaded colors) are NOT linear to the
screen coordinates, and so, the linear interpolated PSX graphics are often
looking rather distorted, that especially for textures that contain straight
lines. For color shading the problem is less obvious (since shading is kinda
blurry anyways).<br/>

#### Perspective correct Rendering
For perspective correct rendering, the polygon's Z-coordinates would be needed
to be passed from the GTE to the GPU, and, the GPU would then need to use that
Z-coordinates to "undo" the perspective division for each pixel (that'd require
some additional memory, and especially a powerful division unit, which isn't
implemented in the hardware).<br/>
As a workaround, you can try to reduce the size of your polygons (the
interpolation errors increase in the center region of larger polygons).
Reducing the size would be only required for polygons that occupy a larger
screen region (which may vary depending on the distance to the camera).<br/>
Ie. you may check the size AFTER perspective division, if it's too large, then
break it into smaller parts (using the original coordinates, NOT the screen
coordinates), and then pass the fragments to the GTE another time.<br/>
Again, perspective correction would be relevant only for certain textures (not
for randomly dithered textures like sand, water, fire, grass, and not for
untextured polygons, and of course not for 2D graphics, so you may exclude
those from size reduction).<br/>

#### 24bit RGB to 15bit RGB Dithering (enabled in Texpage attribute)
For dithering, VRAM is broken to 4x4 pixel blocks, depending on the location in
that 4x4 pixel region, the corresponding dither offset is added to the 8bit
R/G/B values, the result is saturated to +00h..+FFh, and then divided by 8,
resulting in the final 5bit R/G/B values.<br/>
```
  -4  +0  -3  +1   ;\dither offsets for first two scanlines
  +2  -2  +3  -1   ;/
  -3  +1  -4  +0   ;\dither offsets for next two scanlines
  +3  -1  +2  -2   ;/(same as above, but shifted two pixels horizontally)
```
POLYGONs (triangles/quads) are dithered ONLY if they do use gouraud shading or
texture blending.<br/>
LINEs are dithered (no matter if they are mono or do use gouraud shading).<br/>
RECTs are NOT dithered (no matter if they do use texture blending).<br/>

#### Shading information
"Texture RGB values control the brightness of the individual colors ($00-$7f).
A value of $80 in a color will take the former value as data." (What...?
probably means the "double brightness" effect... or does it want to tell that
ALL colors of 80h..FFh have only single brightness.. rather than reaching
double brightness at FFh...?)<br/>

#### Shading
The GPU has a shading function, which will scale the color of a primitive to a
specified brightness. There are 2 shading modes: Flat shading, and gouraud
shading. Flat shading is the mode in which one brightness value is specified
for the entire primitive. In Gouraud shading mode, a different brightness value
can be given for each vertex of a primitive, and the brightness between these
points is automatically interpolated.<br/>

#### Semi Transparency
When semi transparency is set for a pixel, the GPU first reads the pixel it
wants to write to, and then calculates the color it will write from the 2
pixels according to the semitransparency mode selected. Processing speed is
lower in this mode because additional reading and calculating are necessary.
There are 4 semitransparency modes in the GPU.<br/>
```
  B=Back  (the old pixel read from the image in the frame buffer)
  F=Front (the new halftransparent pixel)
  * 0.5 x B + 0.5 x F    ;aka B/2+F/2
  * 1.0 x B + 1.0 x F    ;aka B+F
  * 1.0 x B - 1.0 x F    ;aka B-F
  * 1.0 x B +0.25 x F    ;aka B+F/4
```

#### Draw to display enable
This will enable/disable any drawing to the area that is currently displayed.
Not sure yet WHY one should want to disable that?<br/>
Also not sure HOW and IF it works... the SIZE of the display area is implied by
the screen size - which is horizontally counted in CLOCK CYCLES, so, to obtain
the size in PIXELS, the hardware would require to divide that value by the
number of cycles per pixel, depending on the current resolution...?<br/>



