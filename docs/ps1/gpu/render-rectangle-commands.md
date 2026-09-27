#   GPU Render Rectangle Commands
Rectangles are drawn much faster than polygons. Unlike polygons, gouraud
shading is not possible, dithering isn't applied, the rectangle must forcefully
have horizontal and vertical edges, textures cannot be rotated or scaled, and,
of course, the GPU does render Rectangles as a single entity, without splitting
them into two triangles. Note that this is sometimes refered to as a "sprite".<br/>

The Rectangle command can be decoded using the following bitfield:
```
  0-7   R0    Rectangle color     (ignored if TGE=1)
  8-15  G0    Rectangle color     (ignored if TGE=1)
  16-23 B0    Rectangle color     (ignored if TGE=1)
  24    TGE   Texture Color Mode  (0=Shaded/Modulated, 1=Raw)
  25    ABE   Semi-transparency   (0=Off, 1=On) (if textured: texture bit15 must also be set)
  26    TME   Texture Mapping     (0=Off, 1=On)
  27-28 SIZ   Rectangle Size      (0=Variable, 1=1x1, 2=8x8, 3=16x16)
  29-31 CODE  Command             (always 3 for rectangles)
```

Therefore, the whole draw call can be seen as the following sequence of words:
```
Color         ccBBGGRR    - command + color; color is ignored when textured
Vertex1       YYYYXXXX    - required, indicates the upper left corner to render
UV            ClutVVUU    - optional, only present for textured rectangles
Width+Height  YsizXsiz    - optional, dimensions for variable sized rectangles (max 1023x511)
```

Unlike for textured polygons, the texture page must be set up separately for
Rectangles, via GP0(E1h). Width and Height can be up to 1023x511, however, the
maximum size of the texture window is 256x256 (so the source data will be
repeated when trying to use sizes larger than 256x256).<br/>

Width and Height are masked to their field widths, Xsiz AND 3FFh and
Ysiz AND 1FFh, and unlike the Copy commands there is no case where a size of
zero means maximum. Nothing is drawn at all when either masked dimension comes
out as zero, which happens for raw widths of 0, 400h and 800h, and for raw
heights of 0 and 200h. A raw size above the mask wraps rather than clamping, so
Xsiz=401h draws a single column rather than 1024 of them, and Xsiz=7FFh draws
1023. Computing a width of exactly 400h and getting an empty rectangle is an
easy one to hit from software that clamps its own sizes to 1024.<br/>

If using a texture with a rectangle primitive, please that the texture UV, 
as well as the texture width must be even. If not, there will be one pixel
sampling errors in the drawn rectangle every 16 pixels.

#### Texture Origin and X/Y-Flip
Vertex & Texcoord specify the upper-left edge of the rectangle. And,
normally, screen coords and texture coords are both incremented during
rendering the rectangle pixels.<br/>
Optionally, X/Y-Flip bits can be set in TPage.Bit12/13, these bits cause the
texture coordinates to be decremented (instead of incremented). The X/Y-Flip
bits do affect only Rectangles (not Polygons, nor VRAM Transfers).<br/>
Caution: X/Y-Flip is a v2 GPU feature, and is absent on the v0 GPU used by
early consoles such as the SCPH-1000.<br/>

#### Note
There are also two VRAM Transfer commands which work similar to GP0(60h) and
GP0(65h). Eventually, that commands might be even faster... although not sure
if they do use the Texture Cache?<br/>
The difference is that VRAM Transfers do not clip to the Drawig Area boundary,
do not support fully-transparent nor semi-transparent texture pixels, and do
not convert color depths (eg. without 4bit texture to 16bit framebuffer
conversion).<br/>
