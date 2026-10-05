#   Controller and Memory Card Multitap Adaptor
#### SCPH-1070 (Multitap)
The Multitap is an external adaptor that allows to connect 4 controllers, and 4
memory cards to one controller port. When using two adaptors (one on each
slot), up to 8 controllers and 8 memory cards can be used.<br/>

#### Multitap Controller Access
Normally joypad reading is done by sending this bytes to the pad:<br/>
```
  01 42 00 00 ..   ;normal read
```
And with the multitap, there are even two different ways how to access extra
pads:<br/>
```
  01 42 01 00 ..   ;method 1: receive special ID and data from ALL four pads
  0n 42 00 00 ..   ;method 2: receive data from pad number "n" (1..4)
```
The first method seems to be the more commonly used one (and its special ID is
also good for detecting the multitap); see below for details.<br/>
The second method works more like "normal" reads, among other it's allowing to
transfer more than 4 halfwords per slot (unknown if any existing games are
using that feature).<br/>
The IRQ10 signal (for Konami Lightguns) is simply wired to all four slots via
small resistors (without special logic for activating/deactivating the IRQ on
certain slots).<br/>

#### Multitap Controller Access, Method 1 Details
Below LONG response is activated by sending "01h" as third command byte;
observe that sending that byte does NOT affect the current response. Instead,
it does request that the NEXT command shall return special data, as so:<br/>
```
  Halfword 0      --> Controller ID for MultiTap (5A80h=Multitap)
  Halfword 1..4   --> Player A (Controller ID, Buttons, Analog Inputs, if any)
  Halfword 5..8   --> Player B (Controller ID, Buttons, Analog Inputs, if any)
  Halfword 9..12  --> Player C (Controller ID, Buttons, Analog Inputs, if any)
  Halfword 13..16 --> Player D (Controller ID, Buttons, Analog Inputs, if any)
```
With this method, the Multitap is always sending 4 halfwords per slot (padded
with FFFFh values for devices like Digital Joypads and Mice; which do use less
than 4 halfwords); for empty slots it's padding all 4 halfwords with FFFFh.<br/>
Sending the request is possible ONLY if there is a controller in Slot A (if
controller Slot A is empty then the Slot A access aborts after the FIRST byte,
and it's thus impossible to send the request in the THIRD byte).<br/>
Sending the request works on access to Slot A, trying to send another request
during the LONG response is glitchy (for whatever strange reason); one must
thus REPEATEDLY do TWO accesses: one dummy Slot A access (with the request),
followed by the long Slot A+B+C+D access.<br/>
```
  Previous access had REQ=0 and returned Slot A data ---> returns Slot A data
  Previous access had REQ=0 and returned Slot A-D data -> returns Slot A data
  Previous access had REQ=1 and returned Slot A data ---> returns Slot A-D data
  Previous access had REQ=1 and returned Slot A-D data -> returns garbage
  Previous access had REQ=1 and returned garbage -------> returns Slot A-D data
```
In practice:<br/>
Toggling REQ on/off after each command: Returns responses toggling between
normal Slot A data and long Slot A+B+C+D data.<br/>
Sending REQ=1 in ALL commands: Returns responses toggling between Garbage and
long Slot A+B+C+D data.<br/>
Both of the above is working (one needs only the Slot A+B+C+D part, and it
doesn't matter if the other part is Slot A, or Garbage; as long as the software
is able/aware of ignoring the Garbage). Garbage response means that the
multitap returns ONLY four bytes, like so: Hiz,80h,5Ah,LSB (ie. the leading
HighZ byte, the 5A80h Multitap ID, and the LSB of the Slot A controller ID),
and aborts transfer after that four bytes.<br/>

#### Multitap Memory Card Access
Normally memory card access is done by sending this bytes to the card:<br/>
```
  80 xx .. ..      ;normal access
```
And with the multitap, memory cards can be accessed as so:<br/>
```
  8n xx .. ..      ;access memory card in slot "n" (1..4)
```
That's the way how its done in Silent Hill. Although for the best of confusion,
it doesn't actually work in that game (probably the developer has just linked
in the multitap library, without actually supporting the multitap at higher
program levels).<br/>

#### Multitap Games
```
  Bomberman / Bomberman Party Edition (requires Multitap on Port 2 instead of 1)
  Bomberman World
  Breakout: Off the Wall Fun
  Circuit Breakers
  Crash Team Racing
  FIFA series soccer games
  Frogger
  Hot Shots Golf 2 & 3
  Jigsaw Island: Japan Graffiti / Jigsaw Madness (requires Multitap on Port 2 instead of 1)
  NBA Live (any year) (up to 8 players with two multitaps)
  Need For Speed 3
  Need For Speed 5
  Poy Poy (4 players hitting each other with rocks and trees)
  Running Wild
  S.C.A.R.S. (requires Multitap on Port 2 instead of 1)
  Zen Nippon Pro Wrestling: Ouja no Tamashii (requires Multitap on Port 2 instead of 1)
```
Most Multitap games supporting up to 4 or 5 controllers require the device to be plugged into Port 1, but a small number of games strangely require the device to be plugged into Port 2 instead.<br/>

#### Multitap Versions
```
                   .------.
   SCPH-1070       |      |        SCPH-111
   (gray case)     |      |        (white case)
   (for PSX)       |    D |        (for PSone)
                   |      |                   .----------------.
        cable      |      |        cable     .'   D        C   '.
            ''--.. |    C |         '''--..__|                  |
                  \|      |                  |                  |
  .----------------'      |                  '.   A        B   .'
  |                       |                   '----------------'
  |                       |
  |    A        B        /
  '---------------------'
```
The cable connects to one of the PSX controller ports (which also carries the
memory card signals). The PSX memory card port is left unused (and is blocked
by a small edge on the Multitap's plug).<br/>

#### MultiTap Parsed Controller IDs
Halfword 0 is parsed (by the BIOS) as usually, ie. the LSB is moved to MSB, and
LSB is replaced by status byte (so ID 5A80h becomes 8000h=Multitap/okay, or
xxFFh=bad). Halfwords 1,5,9,13 are NOT parsed (neither by the BIOS nor by the
Multitap hardware), however, some info in the internet is hinting that Sony's
libraries might be parsing these IDs too (so for example 5A41h would become
4100h=DigitalPad/okay, or xxFFh=bad).<br/>

#### Power Supply
The Multitap is powered by the PSX controller port. Unknown if there are any
power supply restrictions (up to eight controllers and eight cards may scratch
some limits, especially when doing things like activating rumble on all
joypads). However, the Multitap hardware itself doesn't do much on supply
restrictions (+3.5V is passed through something; maybe some fuse, loop, or 1
ohm resistor or so) (and +7.5V is passed without any restrictions).<br/>

#### PS2 multitap
Sony made a multitap adapter for the PS2, however it is not compatible with the
PS1 as it plugs into both the controller and memory card ports (which are not
wired in parallel on the PS2). The protocol is also different: rather than
modifying packets it seems to act as a mostly-passive port multiplexer,
accepting switching commands with address 61h. Unknown if the PS2 multitap is
backwards compatible with the SCPH-1070 protocol.<br/>

#### See also
[Component List and Chipset Pin-Outs for Multitap, SCPH-1070](../../pinouts/component-list-and-chipset-pin-outs-for-multitap-scph-1070.md#component-list-and-chipset-pin-outs-for-multitap-scph-1070)<br/>
