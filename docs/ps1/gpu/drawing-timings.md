#   Drawing Timings
The time the GPU takes to draw a primitive or run a transfer, for the v0 GPU
(160-pin CXD8514Q, dual-ported VRAM) and the v2 GPU (208-pin CXD8561Q and
later, DRAM). See [GPU Versions](versions.md) for which consoles carry which.<br/>

All figures are in CPU cycles (33.8688 MHz), counted from the last word of the
command until GPUSTAT bits 26 and 28 both read 1. The cost of the CPU writing
the command words is not included. A primitive costs:<br/>
```
  time = setup + rows * per_row + pixels * per_pixel
```
where rows and pixels are the rows and pixels actually drawn.<br/>

#### v0 GPU (SCPH-1000)
```
  Primitive                             Setup  Per row  Per pixel
  Triangle, flat                           50        6       0.51
  Triangle, flat, semi                     50        6       1.53
  Triangle, gouraud                       200        6       1.02
  Triangle, gouraud, semi                 200        6       3.06
  Triangle, textured, cached              130        6       1.02
  Triangle, textured, cached, semi        130        6       3.06
  Triangle, textured gouraud, cached      295        6       1.02
  Triangle, textured 4bpp, uncached       170        7       1.85
  Triangle, textured 8bpp, uncached       380        7       2.67
  Triangle, textured 15bpp, uncached      130        6       4.33
  Triangle, tex 15bpp, uncached, semi     130        6       6.36
  Quad, flat                               50       12       0.51
  Quad, flat, semi                         50       13       1.53
  Quad, gouraud                           335       11       1.03
  Quad, gouraud, semi                     335       11       3.06
  Quad, textured, cached                  215       11       1.02
  Quad, textured, cached, semi            215       11       3.06
  Quad, textured gouraud, cached          465       10       1.03
  Quad, textured 4bpp, uncached           220        7       1.87
  Quad, textured 8bpp, uncached           460       11       2.69
  Quad, textured 15bpp, uncached          215       10       4.34
  Quad, tex 15bpp, uncached, semi         215       10       6.37
  Rectangle, flat                          50        6       0.51
  Rectangle, flat, semi                    50        6       1.53
  Rectangle, textured, cached              50        6       0.51
  Rectangle, textured 4bpp, uncached       50      100       1.06
  Rectangle, textured 8bpp, uncached       50        0       2.17
  Rectangle, textured 15bpp, uncached      50        2       3.81
  Rectangle, tex 15bpp, uncached, semi     50        3       4.83
```
```
  Transfer                              Setup  Per row  Per pixel
  GP0(02h) fill                            30        7       0.06
  GP0(80h) VRAM to VRAM                    50        -       1.63
  GP0(A0h) by DMA, 16-word blocks          30        2       0.88
  GP0(C0h) by DMA, 16-word blocks         170        3       1.50
```

#### v2 GPU (SCPH-1001, SCPH-7001)
```
  Primitive                             Setup  Per row  Per pixel
  Triangle, flat                           50        2       0.53
  Triangle, flat, semi                     50        8       0.74
  Triangle, gouraud                       200        2       1.01
  Triangle, gouraud, semi                 200        2       1.06
  Triangle, textured, cached              130        2       1.01
  Triangle, textured, cached, semi        130        2       1.06
  Triangle, textured gouraud, cached      295        2       1.01
  Triangle, textured 4bpp, uncached       170        6       1.61
  Triangle, textured 8bpp, uncached       420        4       2.27
  Triangle, textured 15bpp, uncached      130        5       3.48
  Triangle, tex 15bpp, uncached, semi     165        6       3.88
  Quad, flat                               50        6       0.52
  Quad, flat, semi                         50       12       0.78
  Quad, gouraud                           335        4       1.01
  Quad, gouraud, semi                     335        4       1.06
  Quad, textured, cached                  215        4       1.01
  Quad, textured, cached, semi            215        5       1.06
  Quad, textured gouraud, cached          495        2       1.02
  Quad, textured 4bpp, uncached           220        2       1.70
  Quad, textured 8bpp, uncached           470        9       2.31
  Quad, textured 15bpp, uncached          215        5       3.50
  Quad, tex 15bpp, uncached, semi         215       16       3.87
  Rectangle, flat                          50        4       0.51
  Rectangle, flat, semi                    50        0       0.83
  Rectangle, textured, cached              50        2       0.53
  Rectangle, textured 4bpp, uncached       50       90       0.95
  Rectangle, textured 8bpp, uncached       50        0       1.89
  Rectangle, textured 15bpp, uncached      50        6       3.01
  Rectangle, tex 15bpp, uncached, semi     50        7       3.50
```
```
  Transfer                              Setup  Per row  Per pixel
  GP0(02h) fill                            10        8       0.05
  GP0(80h) VRAM to VRAM                    50        -       1.38
  GP0(A0h) by DMA, 16-word blocks          80        1       0.87
  GP0(C0h) by DMA, 16-word blocks          40        2       1.09
```

#### Notes
- Semi is semi-transparency. All four blend modes of GP0(E1h) cost the same.
- Dithering does not change any of the figures.
- Cached means the texels are already in the [texture cache](texture-caching.md),
  for example a primitive smaller than the cache block or a small texture window.
  The texture depth does not matter then. Uncached means the cache (and CLUT
  cache) was invalidated with GP0(01h) before the draw and the texture is mapped
  1:1, so no texel is fetched twice. Most textured primitives fall in between.
- The setup of 4bpp and 8bpp uncached primitives includes loading the CLUT.
- A quad is drawn as two triangles, so its per-row cost is about twice a
  triangle's and its setup is higher.
- The setup of untextured and cached primitives is the same on both GPUs. Setup
  figures are accurate to about 30 cycles and per-row figures to about 5.
- A primitive entirely outside the drawing area still costs its setup plus
  0.7 to 1.3 cycles for each row it would have covered. A rectangle of width 0 costs
  the same; one of height 0 costs only its setup.
- A degenerate polygon (all vertices on one point or one row) draws nothing and
  is not skipped: flat untextured ones cost their setup, gouraud and textured ones
  cost more than a 1-pixel primitive of the same kind (for example about 460
  cycles for a gouraud quad).
- Large untextured primitives on the v2 GPU vary by up to about 5% between
  identical draws, the v0 GPU by well under 1% (?).
- DMA transfers in 16-word blocks take about the same time on both GPUs. Larger
  blocks are faster, so the block size sets the rate.
- The figures were taken with the display enabled (320x240, 15bpp, NTSC)
  showing the drawn area, drawing at the top left of VRAM.

The figures are produced by the gpu-timing test in
[pcsx-redux/nugget](https://github.com/pcsx-redux/nugget/tree/main/tests/gpu-timing).<br/>
