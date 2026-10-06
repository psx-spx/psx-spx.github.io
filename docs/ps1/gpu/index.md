#   Graphics Processing Unit (GPU)
The GPU can render Polygons, Lines, or Rectangles to the Drawing Buffer, and
sends the Display Buffer to the Television Set. Polygons are useful for 3D
graphics (or rotated/scaled 2D graphics), Rectangles are useful for 2D graphics
and Text output.<br/>

![v2 GPU block diagram](diagrams/gpu-v2.svg)

The v0 GPU has the same pipeline, but drives dual-ported VRAM and an external
RAMDAC instead of SGRAM:<br/>

![v0 GPU block diagram](diagrams/gpu-v0.svg)

[I/O Ports, DMA Channels, Commands, VRAM](i-o-ports-dma-channels-commands-vram.md#io-ports-dma-channels-commands-vram)<br/>
[Render Polygon Commands](render-polygon-commands.md#render-polygon-commands)<br/>
[Render Line Commands](render-line-commands.md#render-line-commands)<br/>
[Render Rectangle Commands](render-rectangle-commands.md#render-rectangle-commands)<br/>
[Rendering Attributes](rendering-attributes.md#rendering-attributes)<br/>
[Memory Transfer Commands](memory-transfer-commands.md#memory-transfer-commands)<br/>
[Other Commands](other-commands.md#other-commands)<br/>
[Display Control Commands (GP1)](display-control-commands-gp1.md#display-control-commands-gp1)<br/>
[Status Register](status-register.md#status-register)<br/>
[Versions](versions.md#versions)<br/>
[Depth Ordering](depth-ordering.md#depth-ordering)<br/>
[Video Memory (VRAM)](video-memory-vram.md#video-memory-vram)<br/>
[Texture Caching](texture-caching.md#texture-caching)<br/>
[Timings](timings.md#timings)<br/>
[GPU (MISC)](misc.md#gpu-misc)<br/>
