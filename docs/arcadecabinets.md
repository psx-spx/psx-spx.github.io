#   Arcade Cabinets
#### PSX-Based Arcade Boards
```
  Namco System 11, System 12 (and System 10?)
  Capcom/Sony ZN-1, ZN-2
  Konami GV, Konami GQ
  Taito FX-1A, Taito FX-1B
  Atlus PSX, PS Arcade 95, Tecmo TPS
```

#### CPU
Same as in PSX. Except, one board is said to be having the CPU clocked at
48MHz, instead of 33MHz???<br/>

#### GPU
Same as in PSX. Except, most or all boards are said to have 2MB VRAM instead of
1MB. Unknown how the extra VRAM is accessed... maybe as Y=512..1023... (though
the PSX VRAM transfer commands are limited to 9bit Ysiz values, but maybe Y
coordinates can be 10bit wide).<br/>

#### ROM vs CDROM
Arcade games are stored on ROM (or FLASH) instead of using CDROM drives.<br/>

#### SPU
Most PSX-based arcade boards are having the PSX-SPU replaced by a different
sound chip (with each arcade manufacturer using their own custom sound chip,
often controlled by a separate sound CPU).<br/>

#### Controls
Arcade boards are typically having digital joysticks instead of joypads, with
differently named buttons (instead of /\,[],(),\>\<), probably accessed via
custom I/O ports (instead of serial transmission)? Plus additional coin inputs
and DIP switches.<br/>

Note: There's no documentation for those arcade boards yet, however, it might
be possible to extract that info from MAME source code.<br/>
