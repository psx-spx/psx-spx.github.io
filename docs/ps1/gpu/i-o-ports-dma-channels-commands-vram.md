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
