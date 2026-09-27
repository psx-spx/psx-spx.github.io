#   GPU (MISC)
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

#### 24bit RGB to 15bit RGB Dithering (enabled in texture page attribute)
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
modulation.<br/>
LINEs are dithered (no matter if they are mono or do use gouraud shading).<br/>
RECTs are NOT dithered (no matter if they do use modulation or not).<br/>

#### Shading
The GPU has a shading function, which will scale the color of a primitive to a
specified brightness. There are 2 shading modes: Flat shading, and gouraud
shading. Flat shading is the mode in which one brightness value is specified
for the entire primitive. In Gouraud shading mode, a different brightness value
can be given for each vertex of a primitive, and the brightness between these
points is automatically interpolated.<br/>

#### Semi-transparency
When semi-transparency is set for a pixel, the GPU first reads the pixel it
wants to write to, and then calculates the color it will write from the 2
pixels according to the semi-transparency mode selected. Processing speed is
lower in this mode because additional reading and calculating are necessary.
There are 4 semi-transparency modes in the GPU.<br/>
```
  B=Back  (the old pixel read from the frame buffer)
  F=Front (the new semi-transparent pixel)
  * 0.5 x B + 0.5 x F    ;aka B/2+F/2
  * 1.0 x B + 1.0 x F    ;aka B+F
  * 1.0 x B - 1.0 x F    ;aka B-F
  * 1.0 x B +0.25 x F    ;aka B+F/4
```
For textured primitives using 4-bit or 8-bit textures, bit 15 of each CLUT entry
acts as a semi-transparency flag and determines whether to apply semi-transparency
to the pixel or not. If the semi-transparency flag is off, the new pixel is
written to VRAM as-is.<br/>
When using additive blending, if a channel's intensity is greater than 255, it
gets clamped to 255 rather than being masked. Similarly, if using subtractive
blending and a channel's intensity ends up being < 0, it's clamped to 0.<br/>

#### Modulation (also known as Texture Blending)
Modulation is a colour effect that can be applied to textured primitives.
For each pixel of the primitive it combines every colour channel of the fetched
texel with the corresponding channel of the interpolated vertex colour according
to this formula (Assuming all channels are 8-bit).<br/>
```glsl
  finalChannel.rgb = (texel.rgb * vertexColour.rgb) / vec3(128.0)
```
Using modulation, one can either decrease (if the vertex colour channel value is
< 128) or increase (if it's > 128) the intensity of each colour channel of the
texel, which is helpful for implementing things such as brightness effects.<br/>
Using a vertex colour of 0x808080 (ie all channels set to 128) is equivalent to
not applying modulation to the primitive, as shown by the above formula.<br/>
"Texture blending" is not meant to be confused with normal blending, ie an
operation that merges the backbuffer colour with the incoming pixel and draws
the resulting colour to the backbuffer. The PS1 has this capability to an extent,
using semi-transparency.<br/>

#### Draw to display enable
This will enable/disable any drawing to the area that is currently displayed.
Not sure yet WHY one should want to disable that?<br/>
Also not sure HOW and IF it works... the SIZE of the display area is implied by
the screen size - which is horizontally counted in CLOCK CYCLES, so, to obtain
the size in PIXELS, the hardware would require to divide that value by the
number of cycles per pixel, depending on the current resolution...?<br/>
