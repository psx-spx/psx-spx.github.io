#   Render Line Commands
When the upper 3 bits of the first GP0 command are set to 2 (010), then the command can
be decoded using the following bitfield:
```
  0-7   R0     Line color          (or first vertex color if IIP=1)
  8-15  G0     Line color          (or first vertex color if IIP=1)
  16-23 B0     Line color          (or first vertex color if IIP=1)
  24           Unused
  25    ABE    Semi-transparency   (0=Off, 1=On)
  26           Unused
  27    PLL    Vertex Count        (0=Single, 1=Polyline)
  28    IIP    Shading             (0=Flat, 1=Gouraud)
  29-31 CODE   Command             (always 2 for lines)
```

So each vertex can be seen as the following list of words:
```
Color      xxBBGGRR    - optional, only present for gouraud shading
Vertex     YYYYXXXX    - required, two signed 16 bits values
```

When polyline mode is active, at least two vertices must be sent to the GPU.
The vertex list is terminated by the bits 12-15 and 28-31 equaling `0x5`, or
`(word & 0xF000F000) == 0x50005000`. The terminator value occurs on the first
word of the vertex (i.e. the color word if it's a gouraud shaded).<br/>

If the 2 vertices in a line overlap, then the GPU will draw a 1x1 rectangle in
the location of the 2 vertices using the colour of the first vertex.<br/>

#### Note
Lines are displayed up to \<including\> their lower-right coordinates (ie.
unlike as for polygons, the lower-right coordinate is not excluded).<br/>
If dithering is enabled (via texture page command), then both monochrome and
shaded lines are drawn with dithering (this differs from monochrome polygons and
monochrome rectangles).<br/>

#### Wire-Frame
Poly-Lines can be used (among others) to create Wire-Frame polygons (by setting
the last Vertex equal to Vertex 1).<br/>
