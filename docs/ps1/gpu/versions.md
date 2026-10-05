#   Versions
#### Summary of GPU Differences
```
  Differences...                v0 (160-pin)            v1 (208-pin prototype)  v2 (208-pin)
  GPU Chip                      CXD8514Q                CXD8538Q                CXD8561Q/BQ/CQ/CXD9500Q
  Mainboard                     EARLY-PU-8 and below    Arcade boards only      LATE-PU-8 and up
  Memory Type                   Dual-ported VRAM        Dual-ported VRAM        Normal DRAM
  GP1.R.13 when interlace=off   always 0                unknown                 always 1
  GP1.R.14                      always 0                screen flip             nonfunctional screen flip
  GP1.R.15                      always 0                always 0?               bit1 of tpage Y base
  GP1(10h:index3..4)            19-bit (1 MB VRAM)      22-bit (2 MB VRAM)      20-bit (2 MB VRAM)
  GP1(10h:index7)               N/A                     00000001h version       00000002h version
  GP1(10h:index8)               mirror of index0        00000000h zero          00000000h zero
  GP1(10h:index9..F)            mirror of index1..7     unknown                 N/A
  GP1(09h)                      N/A                     N/A                     VRAM size
  GP1(20h)                      N/A                     VRAM size/settings      N/A
  GP0(E1h).bit11                N/A                     N/A                     bit1 of tpage Y base
  GP0(E1h).bit12/13             without x/y-flip        without x/y-flip        with x/y-flip
  GP0(03h)                      N/A (no stored in fifo) unknown                 unknown/unused command
  Shaded Textures               ((color/8)*texel)/2     unknown                 (color*texel)/16
  GP0(02h) FillVram             xpos.bit0-3=0Fh=bugged  unknown                 xpos.bit0-3=ignored

  dma-to-vram: doesn't work with blksiz>10h (v2 gpu works with blksiz=8C0h!)
  dma-to-vram: MAYBE also needs extra software-handshake to confirm DMA done?
   320*224 pix = 11800h pix = 8C00h words
```
The CXD8538Q (v1) GPU was only ever used in some arcade boards. Among other
things, this GPU seems to use completely different drawing commands and has some
additional functionality not available on v0/v2 GPUs (reportedly GP1(08h).bit7
can be used to flip the screen horizontally?). It may however have a smaller
texture cache or no cache at all, which would explain why the screen flipping
feature had to be removed from v2 to make room on the die for the cache.<br/>
There is another arcade-only GPU revision, the CXD8654Q (v2b). It seems to use
the same commands as regular v2 GPUs, but the differences between v2b and v2 are
currently unknown.<br/>

#### Shaded Textures
The v0 GPU crops 8:8:8 bit gouraud shading color to 5:5:5 bit before multiplying
it with the texture color, resulting in rather poor graphics. For example, the
snow scence in the first level of Tomb Raider I looks a lot smoother on v2 GPUs.
This bug was presumably already fixed on the v1 prototype GPU (unconfirmed).<br/>
The cropped colors are looking a bit as if dithering would be disabled
(although, technically dithering works fine, but due to the crippled color
input, it's always using the same dither pattern per 8 intensities, instead of
using 8 different dither patterns).<br/>

#### Memory/Rendering Timings
The v0 GPU uses two Dual-ported VRAM chips (each with two 16bit databusses,
one for CPU/DMA/rendering access, and one for output to the video DAC). The New
GPU uses s normal DRAM chip (with single 32bit databus).<br/>
The exact timing differences are unknown, but the different memory types should
result in quite different timings:<br/>
The v0 GPU might perform better on non-32bit aligned accesses, and on memory
accesses performed simultaneously with DAC output.<br/>
On the other hand, the v2 GPU's DRAM seems to be faster in some cases (for
example, during Vblank, it's fast enough to perform DMA's with blksiz\>10h,
which exceeds the GPU's FIFO size, and causes lost data on v0 GPUs).<br/>

#### X/Y-Flip and PSone 2 MB VRAM
The X/Y-flipping feature may be used by arcade games (provided that the arcade
board is fitted with v2 GPUs). The flipping feature does also work on retail
consoles with v2 GPUs, but PSX games should never use that feature (for
maintaining compatiblity with older PSX consoles).<br/>
Some PSone consoles seem to be fitted with 2 MB VRAM chips (maybe because
smaller chips had not been in production anymore), but only the first 1 MB
region is accessible. However, as all PSone models use a v2 GPU which supports
2 MB VRAM, it should be possible to rewire the chip selects to make the upper
half accessible.<br/>

#### GPU Detection (and optional VRAM size switching)
Below is slightly customized GPU Detection function taken from Perfect Assassin
(the index7 latching works ONLY on v1/v2 GPUs, whilst v0 GPUs would leave the
latched value unchanged; as a workaround, the index4 latching is used to ensure
that the latch won't contain 000002h on v0 GPUs, assuming that index4 is never
set to 000002h).<br/>
```
  [1F801814h]=10000004h       ;GP1(10h).index4 (latch draw area bottom right)
  [1F801814h]=10000007h       ;GP1(10h).index7 (latch GPU version, if any)
  if ([1F801810h] AND 00FFFFFFh)=00000002h then goto @@gpu_v2
  [1F801810h]=([1F801814h] AND 3FFFh) OR E1001000h ;change GP1.read via GP0(E1h)
  dummy=[1F801810h]           ;dummy read (unknown purpose)
  if ([1F801814h] AND 00001000h) then goto @@gpu_v1 else goto @@gpu_v0
 ;---
 @@gpu_v0:
  return 0
 ;---
 @@gpu_v1:
  if want_2mb_vram then [1F801814h]=20000504h  ;GP1(20h)
  return 1
 ;---
 @@gpu_v2:
  if want_2mb_vram then [1F801814h]=09000001h  ;GP1(09h)
  return 2
```

#### GP0(02h) FillVram
The FillVram command does normally ignore the lower 4bit of the x-coordinate
(and software should always set those bits to zero). However, if the 4bits are
all set, then the old v0 GPU does write each 2nd pixel to wrong memory address.
For example, a 32x4 pixel fill produces following results for x=0..1Fh:<br/>
```
  0h              10h             20h             30h             40h
  |               |               |               |               |
  ################################                                 ;\x=00h..0Eh
  ################################                                 ; and, x=0Fh
  ################################                                 ; on v2 GPU
  ################################                                 ;/
   # # # # # # # ################## # # # # # # #                  ;\
   # # # # # # # ################## # # # # # # #                  ; x=0Fh
   # # # # # # # ################## # # # # # # #                  ; on v0 GPU
   # # # # # # # ################## # # # # # # #                  ;/
                  ################################                 ;\x=10h..1Eh
                  ################################                 ; and, x=1Fh
                  ################################                 ; on v2 GPU
                  ################################                 ;/
                   # # # # # # # ################## # # # # # # #  ;\
                   # # # # # # # ################## # # # # # # #  ; x=1Fh
                   # # # # # # # ################## # # # # # # #  ; on v0 GPU
                   # # # # # # # ################## # # # # # # #  ;/
```
