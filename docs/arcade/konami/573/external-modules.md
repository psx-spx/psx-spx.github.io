## External modules

Over the 573's lifetime Konami introduced several add-ons that extended its
functionality. Unlike the I/O boards, these were external to the 573 unit and
not always mandatory. Not much is currently known about any of these.

### Relay board (`GN845-PWB(A)`)

A relatively simple lamp driver board, controlled by the optoisolated outputs
from the analog or digital I/O board. Commonly mounted in a metal box alongside
audio amplifier boards in most cabinets.

### DDR stage I/O board (`GN845-PWB(B)`)

Sits between the 573 and the sensors in each stage's arrow panels in Dance
Dance Revolution cabinets. It is based on a Xilinx XC9536 CPLD and allows the
573 to check the status of a specific pressure sensor (each panel has 4
sensors, one along each edge), in addition to ensuring DDR games can only be
played with an actual stage rather than just a joystick or buttons wired up to
the 573's JAMMA connector. Konami kept using the same board long after the 573
was discontinued, with the last game to use it being DDR X/X2 (PC based).

Each stage's board communicates with the 573 over 6 wires, of which 4 are the
up/down/left/right signals going to the JAMMA connector and 2 are light outputs
from the I/O board being misused as data and clock lines (see above). The board
initially asserts the right and up signals and waits for the 573 to issue an
initialization command by bitbanging it over the light outputs. Received bits
are acknowledged by the board by echoing them on the right signal and toggling
the up signal.

Once initialization is done the board goes into passthrough mode, asserting the
up/down/left/right signals whenever any of the respective arrow panels' sensors
are pressed. The 573 can issue another command to retrieve the status of each
sensor separately, which is then sent by the board in serialized form over the
right and up signals. DDR games only use this command to display sensor status
in the operator menu, no commands are sent to the board during actual gameplay.

The initialization protocol is currently unknown. The protocol used after
initialization is partially known (see links) but needs to be verified and
documented properly.

### PS1 controller and memory card adapter (`GE885-PWB(A)`)

A ridiculously overengineered JVS board providing support for accessing PS1
controllers and memory cards plugged into ports on the front of the cabinet.
Contains a Toshiba TMPR3904 CPU, a Xilinx XCS10XL Spartan-XL FPGA, 512 KB of RAM
and a 512 KB boot ROM; the ROM is only a small bootloader and the actual
firmware is downloaded from the 573 into RAM. There are also two connectors for
security dongles. Returns the following JVS identifier string:

```
KONAMI CO.,LTD.;White I/O;Ver1.0;White I/O PCB
```

Memory card support became common in later Bemani games, allowing players to
save their scores and play custom charts. GuitarFreaks is the only game known
to support external controllers through this board.

### PunchMania 2 PCMCIA splitter (`PWB0000085445`)

Combines two 32 MB PCMCIA flash cards into the same address space, allowing them
to be accessed as if they were a single 64 MB card. Connects to the 573 through
a cable that plugs into a passive PCMCIA slot adapter. Only used by PunchMania
2.

### e-Amusement network unit (`PWB0000100991`)

Used by some Bemani games, in particular later GuitarFreaks and DrumMania
releases. Provides networking functionality (DHCP and TCP/UDP sockets) as well
as a 10 or 20 GB IDE hard drive for storage of downloaded content. The module
contains a Toshiba TMPR3927 CPU, a Xilinx XC2S100 Spartan-2 FPGA, 16 MB of RAM,
a 512 KB boot ROM and a DP83815 PCI Ethernet MAC. As with the controller and
memory card adapter, the bulk of the firmware seems to be loaded from the 573.
Connects through PCMCIA slot 2, using the same cable and adapter as the
PunchMania PCMCIA splitter.

### Multisession unit (`GXA25-PWB(A)`)

A fairly large box containing a Toshiba TMPR3927 CPU, a Xilinx XC2S200 Spartan-2
FPGA and four (!) hardware MP3 decoders. It comes with up to four daughterboards
installed, each of which hosts a stereo DAC and has RCA jacks for audio input
and output plus a mini-DIN connector for RS-232 communication with a cabinet.
The box also has its own ATAPI CD-ROM drive and power supply.

Its purpose is to enable "session mode" in later Bemani games, which allows for
the same song to be played on multiple games at the same time with the box
playing the backing tracks and routing audio between the machines. It connects
to each cabinet's 573 using RS-232, through the "network" port on the security
cartridge.

### Master calendar

A JVS device used internally by Konami to initialize motherboards and security
cartridges during manufacturing. The exact hardware Konami used is unknown, but
the protocol can be inferred from game code. All games search the JVS bus on
startup and enter a "factory test" mode if any device with the following
identifier string is present:

```
KONAMI CO.,LTD.;Master Calendar;<any value>;<any value>
```

The game will then proceed to request the current date, time, game and region
information from the master calendar, initialize the RTC and program the
security cartridge. The master calendar also returns a unique trace ID (see the
cartridge data formats section) for each 573, used for identification purposes
on cartridges that lack a DS2401.

#### `0x70`: **Get date and time**

#### `0x71`: **Get game region or initialization data**

#### `0x7c, 0x7f, 0x00`: **Get trace ID "main" serial number**

#### `0x7c, 0x80, 0x00`: **Get trace ID "sub" serial number**

#### `0x7d, 0x80, 0x10`: **Get next ID**

#### `0x7e`: **Set DS2401 identifiers**

#### `0x7f`: **Unknown**

#### `0xf0`: **Reset master calendar**
