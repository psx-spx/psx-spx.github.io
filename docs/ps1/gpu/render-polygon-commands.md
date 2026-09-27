#   GPU Render Polygon Commands
When the upper 3 bits of the first GP0 command are set to 1 (001), then the command can
be decoded using the following bitfield:
```
  0-7   R0     Polygon color       (or first vertex color if IIP=1, ignored if TGE=1)
  8-15  G0     Polygon color       (or first vertex color if IIP=1, ignored if TGE=1)
  16-23 B0     Polygon color       (or first vertex color if IIP=1, ignored if TGE=1)
  24    TGE    Texture Color Mode  (0=Shaded/Modulated, 1=Raw)
  25    ABE    Semi-transparency   (0=Off, 1=On) (if textured: texture bit15 must also be set)
  26    TME    Texture Mapping     (0=Off, 1=On)
  27    VTX    Vertex Count        (0=Triangle, 1=Quad)
  28    IIP    Shading             (0=Flat, 1=Gouraud)
  29-31 CODE   Command             (always 1 for polygons)
```
(Bit names are known from the documentation Sony released for the .TMD and .PMD
file formats, and seem to match their PS2 GS counterparts as well.)

Subsequent data sent to GP0 to complete this command will be the vertex data for the
command. The meaning and count of these words will be altered by the initial flags
sent in the first command.

If doing flat rendering, no further color will be sent. If doing gouraud shading,
there will be one more color per vertex sent, and the initial color will be the
one for vertex 0.

If doing textured rendering, each vertex sent will also have a U/V texture coordinate
attached to it, as well as a CLUT index.

So each vertex data can be seen as the following set of words:
```
Color      xxBBGGRR               - optional, only present for gouraud shading
Vertex     YYYYXXXX               - required, two signed 16 bits values
UV         ClutVVUU or PageVVUU   - optional, only present for textured polygons
```

The upper 16 bits of the first two UV words contain extra information. The first
word holds the [Clut index](rendering-attributes.md#clut-attribute-color-lookup-table-aka-palette). The
second word contains [texture page information](rendering-attributes.md#tpage-attribute-parameter-for-textured-polygon-commands).
Any further clut/page bits should be set to 0.


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
ClutV1U1
00R2G2B2
Yyy2Xxx2
PageV2U2
00R3G3B3
Yyy3Xxx3
0000V3U3
00R4G4B4
Yyy4Xxx4
0000V4U4
```

Some combination of these flags can be seen as nonsense however, but it's important
to realize that the GPU will still process them properly. For instance, specifying
gouraud shading without modulation will force the user to send the colors for
each vertex to satisfy the GPU's state machine, without them being actually used for
the rendering.

#### Notes
Polygons are displayed up to \<excluding\> their lower-right coordinates.<br/>
Quads are internally processed as two triangles, the
first consisting of vertices 1,2,3, and the second of vertices 2,3,4. This is an
important detail, as splitting the quad into triangles affects the way colours
are interpolated.<br/>
Within the triangle, the ordering of the vertices doesn't matter on
the GPU side (a front-back check, based on clockwise or anti-clockwise
ordering, can be implemented at the GTE side).<br/>
Dither enable (in texture page command) affects ONLY polygons that do use
gouraud shading or modulation.<br/>
