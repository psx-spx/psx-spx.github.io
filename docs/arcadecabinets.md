#   Arcade Cabinets
#### PSX-Based Arcade Boards
The following arcade boards are known to be based on PSX hardware:

- Namco: System 10, System 11, System 12
- Konami: GV, GQ, [System 573](konamisystem573.md), Twinkle System
- Sony: ZN-1, ZN-2
- Taito: FX-1A, FX-1B, G-NET (uses ZN-2 motherboard)
- Atlus PSX, PS Arcade 95, Tecmo TPS

Currently only documentation for the System 573 exists. Information about other
arcade boards could be obtained from MAME source code.<br/>

#### CPU
Same as in PSX. Some boards (e.g. ZN-2) have the CPU clocked at a higher clock
speed, usually 48MHz.<br/>

#### GPU
Same as in PSX. Except, most or all boards are said to have 2MB VRAM instead of
1MB. Unknown how the extra VRAM is accessed... maybe as Y=512..1023... (though
the PSX VRAM transfer commands are limited to 9bit Ysiz values, but maybe Y
coordinates can be 10bit wide).<br/>

#### ROM vs CDROM
No known arcade board uses the same CD drive used in the PSX. Most of them have
no drive at all and use mask ROM or flash memory for game storage, while others
(such as the 573 and Twinkle System) are equipped with standard ATAPI/SCSI CD
drives or even hard drives in some cases. The 573 in particular has both 16MB
of flash memory soldered to the motherboard and a CD drive, allowing games to
e.g. quickly load data while also playing CD audio.<br/>

#### SPU
Most PSX-based arcade boards are having the PSX-SPU replaced by a different
sound chip (with each arcade manufacturer using their own custom sound chip,
often controlled by a separate sound CPU). Some have both the standard SPU as
well as additional hardware for music or DSP effects, usually on a separate
board.<br/>

#### Controls
Arcade boards are typically having digital joysticks instead of joypads, with
differently named buttons as well as additional coin inputs, service/test
buttons and DIP switches. Controls are connected to the motherboard through a
standard JAMMA connector and accessed via custom memory-mapped I/O ports
usually.<br/>

Some boards also feature a JVS port (RS-485 serial over USB cables, commonly
used instead of JAMMA to connect peripherals to modern arcade systems),
allowing standard JVS I/O boards to be used if supported by games.<br/>
