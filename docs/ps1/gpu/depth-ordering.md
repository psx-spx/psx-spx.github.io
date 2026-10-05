#   Depth Ordering
#### Absent Depth Buffer
The PlayStation's GPU stores only RGB colors in the framebuffer (ie. unlike
modern 3D processors, it's NOT buffering Depth values; leaving apart the Mask
bit, which could be considered as a tiny 1bit "Depth" or "Priority" value). In
fact, the GPU supports only X,Y coordinates, and it's totally unaware of Z
coordinates. So, when rendering a polygon, the hardware CANNOT determine which
of the new pixels are in front/behind of the old pixels in the buffer.<br/>

#### Simple Ordering
The rendering simply takes place in the ordering as the data is sent to the GPU
(ie. the most distant objects should be sent first). For 2D graphics, it's
fairly easy follow that order (eg. even multi-layer 2D graphics can be using
DMA2-continous mode).<br/>

#### Depth Ordering Table (OT)
For 3D graphics, the ordering of the polygons may change more or less randomly
(eg. when rotating/moving the camera). To solve that problem, the whole
rendering data is usually first stored in a Depth Ordering Table (OT) in Main
RAM, and, once when all polygons have been stored in the OT, the OT is sent to
the GPU via "DMA2-linked-list" mode.<br/>

#### Initializing an empty OT (via DMA6)
DMA channel 6 can be used to set up an empty linked list, in which each entry
points to the previous:<br/>
```
  DPCR    - enable bits                                 ;Example=x8xxxxxxh
  D6_MADR - pointer to the LAST table entry             ;Example=8012300Ch
  D6_BCR  - number of list entries                      ;Example=00000004h
  D6_CHCR - control bits (should be 11000002h)          ;Example=11000002h
```
Each entry has a size of 00h words (upper 8bit), and a pointer to the previous
entry (lower 24bit). With the above Example values, the generated table would
look like so:<br/>
```
  [80123000h]=00FFFFFFh  ;1st entry, points to end code (xxFFFFFFh)
  [80123004h]=00123000h  ;2nd entry, points to 1st entry
  [80123008h]=00123004h  ;3rd entry, points to 2nd entry
  [8012300Ch]=00123008h  ;last entry, points to 3rd entry (table entrypoint)
```

#### Inserting Entries (Passing GTE data to the OT) (by software)
The GTE commands AVSZ3 and AVSZ4 can be used to calculate the Average Z
coordinates of a polygon (based on its three or four Z coordinates). The result
is returned as a 16bit Z value in GTE register OTZ, the commands do also allow
to divide the result, to make it less than 16bit (the full 16bit would require
an OT of 256KBytes - for the EMPTY table, which would be a waste of memory, and
which would slowdown the DMA2/DMA6 operations) (on the other hand, a smaller
table means less depth resolution).<br/>
```
  [PacketAddr+0]      = [80123000h+OTZ*4] + (N SHL 24)   <--internal link chain
  [PacketAddr+4..N*4] = GP0 Command(s) and Parameters    <--data (send to GP0)
  [80123000h+OTZ*4]   = PacketAddr AND FFFFFFh           <--internal link chain
```
If there's been already an entry (at the same OTZ index), then the new polygon
will be processed first (ie. it will appear "behind" of the old entry).<br/>
Not sure if the packet size must be limited to max N=16 words (ie. as for the
DMA2-continous block size) (due to GP0 FIFO size limits)?<br/>

#### Sending the OT to the GPU (via DMA2-linked-list mode)
```
  1 - Wait until GPU is ready to receive commands ;GP1.R.28
  2 - Enable DMA channel 2                  ;DPCR
  3 - Set GPU to DMA cpu->gpu mode          ;[GP1]=04000002h aka GP1(04h)
  3 - Set D2_MADR to the start of the list  ;(LAST Entry) ;Example=80123010h
  4 - Set D2_BCR to zero                    ;(length unused, end at END-CODE)
  5 - Set D2_CHCR to link mode, mem->GPU and dma enable   ;=01000401h
```
