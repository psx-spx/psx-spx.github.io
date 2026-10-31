#   I/O Ports, DMA Channels, Commands, VRAM
#### GPU I/O Ports (`0x1f801810`, `0x1f801814`)
```
  Port        Name  Dir    Expl.
  0x1f801810  GP0   Write  Send GP0 Commands/Packets (Rendering and VRAM Access)
                    Read   Receive responses to GP0(C0h) and GP1(10h) commands
  0x1f801814  GP1   Write  Send GP1 Commands (Display Control) (and DMA Control)
                    Read   Receive GPU Status Register
```
GP0 has a 64-byte (16-word) command FIFO buffer, in addition to the command the
GPU is currently executing. Writing to a full FIFO does not stall the CPU and
does not drop the new word: the newest words overwrite the oldest queued ones.
Software must check GPUSTAT (or use DMA) before writing.<br/>
See [GP0 write FIFO](#gp0-write-fifo) below for the flags that report it.<br/>
Optionally, Port 1F801810h (Read/Write) can be also accessed via DMA2.<br/>
The communication between the CPU and the GPU is a 32-bits data-only bus called
the VBUS. Aside from address line 2 being connected, in order to make the difference
between port 0 and 1, there are no other address line between the two chips.<br/>
Thus the GPU can be seen as a blackbox that executes 32 bits commands.<br/>

#### GPU Timers / Synchronization
Most of the Timers are bound to GPU timings, see<br/>
[Timers](../system/timers.md)<br/>
[Interrupts](../system/interrupts.md)<br/>

#### GPU-related DMA Channels (DMA2 and DMA6)
```
  Channel                   Recommended for
  DMA2 in Linked Mode     - Sending rendering commands  ;GP0(20h..7Fh,E1h..E6h)
  DMA2 in Continuous Mode - VRAM transfers to/from GPU  ;GP0(A0h,C0h)
  DMA6                    - Initializing the Link List  ;Main RAM
```
Note: Before using DMA2, set up the DMA Direction in GP1(04h).<br/>
DMA2 is equivalent to accessing Port 1F801810h (GP0) by software.<br/>
DMA6 just initializes data in Main RAM (not physically connected to the GPU).<br/>

#### GP0 write FIFO
Words written to GP0, by the CPU or by DMA2, wait in the FIFO until the GPU
takes them. Which GPUSTAT bit reports its state depends on the DMA Direction
set with GP1(04h).<br/>
With GP1(04h)=1, bit 25 reads 0 once about 11 words are queued behind a busy
GPU, before the 16 words are used up, and goes back to 1 as the GPU takes
words. Waiting for bit 25 before each write is enough to stream any amount of
data. That includes a poly-line much longer than the FIFO: the GPU consumes it
one segment at a time, and a 60-vertex poly-line written this way draws
completely. Without the wait the CPU is not slowed down, and words are lost as
described above.<br/>
Bit 26 is not a FIFO flag: it reads 0 while a command is still waiting for its
parameters, and it is 0 after each word of a poly-line, so it cannot pace
a stream. Bit 28 also reads 0 throughout such a stream.<br/>
DMA2 transfers:
```
  DMA2 mode  GP1(04h)  Result
  1 (block)  1         completes, but 16-word blocks lose words (lines,
                       polygons and rectangles); 1-word blocks are exact
  1 (block)  2         hangs if a block ends inside a polygon or line command
                       (poly-lines included); blocks of whole commands are fine,
                       rectangles do not hang
  2 (list)   2         a 12-word node is transferred intact, a 240-word node
                       loses words; behind a busy GPU a node over 17 words
                       loses words (see below)
```
The hang comes from bit 28 being the DMA request in that mode. For polygon and
line commands it drops right after the command word and stays 0 until the
command is done, so the block after the one with the command word does not
start. The transfer stops for good: CHCR stays busy, BCR shows exactly one block
gone, and GPUSTAT bits 25, 26 and 28 all read 0.<br/>
In linked-list mode the DMA request is only checked between nodes. The words
of one node are sent back to back: a long node is transferred at once even
while the GPU is still drawing, and is then corrupted. With a node made of
GP0(E6h), a 256x200 semi-transparent quad (GP0(2Ah)), GP0(68h) dots and
GP0(E6h):
```
  Node words  Result
  up to 17    correct
  19          the quad stops halfway (25376 of 51200 pixels drawn)
  21          the quad is not drawn, the dots are
  23 and up   the quad is cut short, the dots are lost or have wrong values
```
A small primitive does not make a long node safe: 16 dots after a 4x4
semi-transparent quad, in one 39-word node, are all lost. The same 39 words
behind a 256x200 quad, split into nodes of up to 8 words, are drawn correctly,
because the DMA waits for the GPU between nodes. Linking each primitive as its
own node avoids the problem; packing several primitives into one node does
not, as soon as the GPU can be busy when the node starts.<br/>
Not every GP0 command waits in the FIFO. GP0(00h), GP0(04h..1Eh), GP0(E0h),
GP0(E3h..E5h) and GP0(E7h..EFh) do not take up space in it, even while the GPU
is busy. GP0(01h), GP0(1Fh), GP0(E1h), GP0(E2h), GP0(E6h) and all drawing and
transfer commands are queued. GP0(03h) is queued on v2 GPUs only. See
[Other Commands](other-commands.md).<br/>

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
Where each group is documented:

- Misc commands: [Clear Cache](#clear-cache) and [Quick Rectangle Fill](#quick-rectangle-fill) below, the rest (NOP, mirrors, IRQ) in [Other Commands](other-commands.md)
- [Polygon](render-polygon-commands.md), [Line](render-line-commands.md) and [Rectangle](render-rectangle-commands.md) primitives
- VRAM-to-VRAM, CPU-to-VRAM and VRAM-to-CPU blits: [Memory Transfer Commands](memory-transfer-commands.md)
- Environment commands, GP0(E1h) to GP0(E6h): [Rendering Attributes](rendering-attributes.md#gp0e1h-draw-mode-setting-aka-tpage)

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
16bit: The hardware linearly converts the 24bit RGB value to 15bit RGB by
dropping the lower 3 bits of each color value and additionally sets the mask bit
(bit15) to 0.<br/>
Rectangle filling is not affected by the GP0(E6h) mask setting, acting as if
GP0(E6h).0 and GP0(E6h).1 are both zero.<br/>
This command is typically used to do a quick clear, as it'll be faster to run
than an equivalent Render Rectangle command.<br/>

#### VRAM Overview / VRAM Addressing
VRAM can be 1 MB or 2 MB (not mapped to the CPU bus) (it can be read/written
only via I/O or DMA). The memory is used for:<br/>
```
  Framebuffer(s)      ;Usually 2 buffers (Drawing Area, and Display Area)
  Texture Page(s)     ;Required when using Textures
  Texture Palette(s)  ;Required when using 4bit/8bit Textures
```
1 MB VRAM is laid out as 512 lines of 2048 bytes each. 2 MB VRAM (only present
on some arcade boads, not on consoles) is laid out as 1024 lines instead. It is
accessed via coordinates, ranging from (0,0)=Upper-Left to (N,1023)=Lower-Right.<br/>
```
  Unit  = 4bit  8bit  16bit  24bit   Halfwords   | Unit   = Lines
  Width = 4096  2048  1024   682.66  1024        | Height = 512/1024
```
The horizontal coordinates are addressing memory in
4bit/8bit/16bit/24bit/halfword units (depending on what data formats you are
using) (or a mixup thereof, eg. a halfword-base address, plus a 4bit texture
coordinate).<br/>
