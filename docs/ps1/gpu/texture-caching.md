#   Texture Caching
The GPU has 2 Kbyte Texture Cache<br/>
There is also a CLUT cache that is preserved between GPU drawing commands. The
CLUT cache is invalidated when different CLUT index values are used or when
GP0(01h) is issued.<br/>
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
