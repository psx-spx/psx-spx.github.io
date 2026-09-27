#   GPU Rendering Attributes
#### Vertex (Parameter for Polygon, Line, Rectangle commands)
```
  0-10   X-coordinate (signed, -1024..+1023)
  11-15  Not used (usually sign-extension, but ignored by hardware)
  16-26  Y-coordinate (signed, -1024..+1023)
  27-31  Not used (usually sign-extension, but ignored by hardware)
```
Size Restriction: The maximum distance between two vertices is 1023
horizontally, and 511 vertically. Polygons and lines that are exceeding that
dimensions are NOT rendered. For example, a line from Y1=-300 to Y2=+300 is NOT
rendered, a line from Y1=-100 to Y2=+400 is rendered (as far as it is within
the drawing area).<br/>

The distance is taken per edge, on the 11-bit field values as they arrive, and
the fields have already wrapped by then. A coordinate outside the -1024..+1023
range is therefore not a reason to drop the primitive: X=+1025 is simply
X=-1023, and the polygon is rendered at that wrapped position, usually on the
far side of the drawing area from where the software intended it. Only a
distance that is still above the limit after wrapping drops the primitive,
which for a single coordinate leaving the range means exactly the values that
land on -1024. Software that computes screen coordinates without clamping them
to the field range gets a misplaced polygon rather than a missing one.<br/>

For quads the checked edges are the four perimeter edges plus the edge between
Vertex2 and Vertex3, which is the diagonal the two rendered triangles share.
Vertex1 and Vertex4 are not an edge of either triangle and are not compared, so
a quad may legally span more than 1023 horizontally between those two.<br/>
If portions of the polygon/line/rectangle are located outside of the drawing
area, then the hardware renders only the portion that is inside of the drawing
area. Not sure if the hardware is skipping all clipped pixels at once (within a
single clock cycle), or if it's (slowly) processing them pixel by pixel?<br/>

#### Color Attribute (Parameter for all Rendering commands, except Raw Texture)
```
  0-7   Rn   Red   (0..FFh)
  8-15  Gn   Green (0..FFh)
  16-23 Bn   Blue  (0..FFh)
  24-31 ...  Command (in first paramter) (don't care in further parameters)
```
Caution: For untextured graphics, 8bit RGB values of FFh are brightest.
However, for modulation, 8bit values of 80h are brightest (values
81h..FFh are "brighter than bright" allowing to make textures about twice as
bright as than they were originially stored in memory; of course the results
can't exceed the maximum brightness, ie. the 5bit values written to the
framebuffer are saturated to max 1Fh).<br/>

#### TPage Attribute (Parameter for textured polygon commands)
```
  0-8   ...  Same as GP0(E1h).Bit0-8 (see there)
  9-10       Unused (does NOT change GP0(E1h).Bit9-10)
  11    ...  Same as GP0(E1h).Bit11  (see there)
  12-13      Unused (does NOT change GP0(E1h).Bit12-13)
  14-15      Unused (should be 0)
```
This attribute is used in all textured polygon commands.<br/>

#### Clut Attribute (Color Lookup Table, aka Palette)
This attribute is used in all Textured Polygon/Rectangle commands. Of course,
it's relevant only for 4bit/8bit textures (don't care for 15bit textures).<br/>
```
  0-5  CLX  X coordinate X/16  (ie. in 16-halfword steps)
  6-14 CLY  Y coordinate 0-511 (ie. in 1-line steps)  ;\on v0 GPU (max 1 MB VRAM)
  15        Unused (should be 0)                      ;/
  6-15 CLY  Y coordinate 0-1023 (ie. in 1-line steps) ;on v2 GPU (max 2 MB VRAM)
```
Specifies the location of the CLUT data within VRAM.<br/>

#### GP0(E1h) - Draw Mode setting (aka "TPage")
```
  0-3   TBX   Texture page X Base   (N*64) (ie. in 64-halfword steps)    ;GP1.R.0-3
  4     TBY   Texture page Y Base 1 (N*256) (ie. 0, 256, 512 or 768)     ;GP1.R.4
  5-6   ABR   Semi-transparency     (0=B/2+F/2, 1=B+F, 2=B-F, 3=B+F/4)   ;GP1.R.5-6
  7-8   TPF   Texture page colors   (0=4bit, 1=8bit, 2=15bit, 3=Reserved);GP1.R.7-8
  9     DTD   Dither 24bit to 15bit (0=Off/strip LSBs, 1=Dither Enabled) ;GP1.R.9
  10    DFE   Drawing to display area (0=Prohibited, 1=Allowed)          ;GP1.R.10
  11    TBY2  Texture page Y Base 2 (N*512) (v1/v2 GPU only, w/ 2MB VRAM);GP1.R.15
  12    IX?   Textured Rectangle X-Flip     (v2 GPU only) (BIOS does set this bit on power-up...?)
  13    IY?   Textured Rectangle Y-Flip     (v2 GPU only) (BIOS does set it equal to GP1.R.13...?)
  14-23       Not used (should be 0)
  24-31 CODE  Command  (E1h)
```
The GP0(E1h) command is required only for Lines, Rectangle, and
untextured polygons (for textured polygons, the data is specified through the
texture page attribute; except that, Bits 9-10 can be changed only via GP0(E1h),
not via the page attribute).<br/>
Texture page colors setting 3 (reserved) is same as setting 2 (15bit).<br/>
Bits 4 and 11 are the LSB and MSB of the 2-bit texture page Y coordinate.
Normally only bit 4 is used as retail consoles only have 1 MB VRAM. Setting bit
11 (Y>=512) on a retail console with a v2 GPU will result in textures
disappearing if 2 MB VRAM support was previously enabled using GP1(09h), as the
VRAM chip select will no longer be active. Bit 11 is always ignored by v0 GPUs
that do not support 2 MB VRAM.<br/>
Note: GP0(00h) seems to be often inserted between texture page and rectangle
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
  Texcoord = (Texcoord AND (NOT (Mask * 8))) OR ((Offset AND Mask) * 8)
```
The area within a texture window is repeated throughout the texture page. The
data is not actually stored all over the texture page but the GPU reads the
repeated patterns as if they were there. Considering all possible regular
tilings of UV coordinates for powers of two, the texture window primitive can
be constructed as follows using a desired set of parameters of `tiling_x`,
`tiling_y`, `window_pos_x`, `window_pos_y`, `u`, `v` and `color_mode`:<br/>
```
x_tiling_factor = {8: 0b11111, 16: 0b11110, 32: 0b11100, 64: 0b11000, 128: 0b10000, 256: 0b00000}[tiling_x]
y_tiling_factor = {8: 0b11111, 16: 0b11110, 32: 0b11100, 64: 0b11000, 128: 0b10000, 256: 0b00000}[tiling_y]
x_offset = u & 0b11111
x_offset <<= {15: 0, 8: 1, 4: 2}[color_mode]
x_offset >>= 3;
y_offset = v & 0b11111
y_offset >>= 3
texture_window_prim = (0xE20 << 20) | (y_offset << 15) | (x_offset << 10) | (y_tiling_factor << 5) | x_tiling_factor
```

#### GP0(E3h) - Set Drawing Area top left (X1,Y1)
#### GP0(E4h) - Set Drawing Area bottom right (X2,Y2)
```
  0-9    X-coordinate (0..1023)
  10-18  Y-coordinate (0..511)   ;\on v0 GPU (max 1 MB VRAM)
  19-23  Not used (zero)         ;/
  10-19  Y-coordinate (0..1023)  ;\on v2 GPU (max 2 MB VRAM)
  20-23  Not used (zero)         ;/
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
  0     PBW  Set mask while drawing (0=TextureBit15, 1=ForceBit15=1)   ;GP1.R.11
  1     PBC  Check mask before draw (0=Draw Always, 1=Draw if Bit15=0) ;GP1.R.12
  2-23       Not used (zero)
  24-31      Command  (E6h)
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
