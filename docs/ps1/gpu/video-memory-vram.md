#   Video Memory (VRAM)
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
  0-4   Red       (0..31)         ;\Color 0000h        = Fully-transparent
  5-9   Green     (0..31)         ; Color 0001h..7FFFh = Non-transparent
  10-14 Blue      (0..31)         ; Color 8000h..FFFFh = Semi-transparent (*)
  15    Semi-transparency Flag    ;/(*) or Non-transparent for opaque commands
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
  0-4   Red       (0..31)         ;\Color 0000h        = Fully-transparent
  5-9   Green     (0..31)         ; Color 0001h..7FFFh = Non-transparent
  10-14 Blue      (0..31)         ; Color 8000h..FFFFh = Semi-transparent (*)
  15    Semi-transparency Flag    ;/(*) or Non-transparent for opaque commands
```
The clut data can be arranged in the frame buffer at X multiples of 16
(X=0,16,32,48,etc) and anywhere in the Y range of 0-511 (0-1023 if 2 MB VRAM is
present).<br/>

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
like 0001h (dark red) or 0400h (dark blue). However, on some monitors with
particularly high gamma, these colors might be clearly visible to be brighter
than black.<br/>
