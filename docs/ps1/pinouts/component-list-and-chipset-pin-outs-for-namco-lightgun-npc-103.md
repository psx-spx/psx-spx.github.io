#   Pinouts - Component List and Chipset Pin-Outs for Namco Lightgun, NPC-103
#### Schematic
http://www.nicolaselectronics.be/reverse-engineering-the-playstation-g-con45/<br/>

#### Namco Lightgun "NPC-103, (C) 1996 NAMCO LTD." Component List
PCB "DNP-0500A, NPC10300, namco, CMK-P3X"<br/>
```
  U1  44pin "NAMCO103P, 1611U1263, JAPAN 9847EAI, D0489AAF"
  U2   8pin "7071, 8C19" (=BA7071F, Sync Separator IC with AFC)
  XTAL 2pin "CSA 8.00WT"
  PS1  3pin Light sensor with metal shielding
  J1   9pin Connector for 9pin cable to PSX controller and GunCon plugs
  plus resistors and capacitors, and A1,A2,B1,B2,T1,T2 wires to buttons
```
PCB "DN-P-0501"<br/>
```
  DIP Button (with black T1,T2 wires) (trigger)
```
PCB "DN-P-0502"<br/>
```
  Button A (with red A1,A2 wires) (left side)
  Button B (with white B1,B2 wires) (right side)
```
Other Components<br/>
```
  Lens (20mm)
```
Cable Pinouts<br/>
```
  J1.Pin1 green  PSX.Controller.Pin5 +3.5V
  J1.Pin2 brown  PSX.Controller.Pin4 GND
  J1.Pin3 black  PSX.Controller.Pin9 /ACK/IRQ7
  J1.Pin4 red    PSX.Controller.Pin6 /JOYn
  J1.Pin5 yellow PSX.Controller.Pin1 JOYDAT
  J1.Pin6 orange PSX.Controller.Pin2 JOYCMD
  J1.Pin7 blue   PSX.Controller.Pin7 JOYCLK
  J1.Pin8 gray   GunCon shield (GND)
  J1.Pin9 white  GunCon composite video
  N/A            PSX.Controller.Pin3 +7.5V
  N/A            PSX.Controller.Pin8 /IRQ10
  N/A            PSX.Controller Shield
```
U1 "NAMCO103P" Pinouts (44pin, arranged as 4x11pin)<br/>
```
  1 GND    12 SYNC (from U2)                     23 3.5V   34 SW1 (A)
  2 GND    13 3.5V                               24 3.5V   35 3.5V
  3 GND    14 3.5V                               25 3.5V   36 3.5V
  4 GND    15 SW3 (TRIGGER)                      26 GND    37 SW2 (B)
  5 GND    16 JOYCLK (J1.Pin7 via 220 ohm R7)    27 GND    38 3.5V
  6 GND    17 3.5V                               28 GND    39 3.5V
  7 GND    18 JOYCMD (J1.Pin6 via 220 ohm R8)    29 GND    40 LIGHT (from PS1)
  8 GND    19 JOYDAT (J1.Pin5 via 0 ohm R10)     30 -      41 GND
  9 -      20 /JOYn (J1.Pin4 via 220 ohm R9)     31 GND    42 GND
  10 GND   21 /ACK/IRQ7 (J1.Pin3 via 0 ohm R11)  32 GND    43 OSC 8MHz
  11 GND   22 GND                                33 GND    44 OSC 8MHz
```
U2 "7071" Pinouts (=BA7071F, Sync Separator IC with AFC) (2x4pin)<br/>
```
  1 VIN      = SYNC.IN from J1.Pin9 Composite Video (via C5/C6/C7/R6)
  2 HD_OUT   = NC
  3 GND      = GND
  4 PD_OUT   = NC
  5 HOSC_R   = via 100K to GND
  6 VCC      = 3.5V
  7 VD_OUT   = NC
  8 SYNC_OUT = SYNC.OUT to U1.pin12 (with R4 pull-up)
```
