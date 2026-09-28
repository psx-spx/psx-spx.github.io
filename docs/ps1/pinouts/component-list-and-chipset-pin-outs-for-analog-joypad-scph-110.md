#   Pinouts - Component List and Chipset Pin-Outs for Analog Joypad, SCPH-110
#### Analog Joypad Component List (SCPH-110, two motors, PSone-design)
```
  Case "SONY, ANALOG CONTROLLER, SonyCompEntInc. A, SCPH-110 MADE IN CHINA"
  PCB1 "SA1Q22A, <PF-LP>, KPC, 7694V-0" (mainboard with joysticks onboard)
  PCB2 "..." (membrane/foil with digital buttons)
  U1  44pin "SD707, 039 107"" (4x11pin)
  Q1   3pin "KA" (big transistor for left/big M1 rumble motor)
  Q2   3pin "LG" (small transistor for right/small M2 rumble motor)
  D1   2pin diode (for large motor, reference Z-diode with pull-up?)
  D2   3pin dual-diode (R5/IRQ7 to GND and R3/DAT to GND)
       (not fitted on the "S003" PCB1 revision, which works without it)
  CN1  9pin cable to PSX controller port
  J1  16pin ribbon cable from membrane/foil
  M1   2pin wires to left/big rumble motor (analog, slow/fast)
  M2   2pin wires to right/small rumble motor (digital, on/off)
  LED1 2pin red analog mode LED (with long legs, without mirror/optics)
  plus resistors/capacitors
```

#### Analog Joypad Connection Cables (SCPH-110)
CN1 (cable to PSX controller port)<br/>
```
  1 +3.5V (logic supply)
  2 GND3  (logic supply)
  3 /IRQ7
  4 /SEL
  5 CMD
  6 DAT
  7 CLK
  8 GND7  (motor supply)
  9 +7.5V (motor supply)
```
J1 (ribbon cable with membrane/foil with digital buttons)<br/>
```
  1 BUTTON Bit8 L2
  2 BUTTON Bit10 L1
  3 BUTTON Bit4 UP
  4 BUTTON Bit5 RIGHT
  5 BUTTON Bit6 DOWN
  6 BUTTON Bit7 LEFT
  7 GND3
  8 ANALOG BUTTON
  9 BUTTON Bit0 SELECT
  10 BUTTON Bit3 START
  11 BUTTON Bit15 SQUARE   []
  12 BUTTON Bit14 CROSS    ><
  13 BUTTON Bit13 CIRCLE   ()
  14 BUTTON Bit12 TRIANGLE /\
  15 BUTTON Bit11 R1
  16 BUTTON Bit9 R2
```
M1 wires to left/big rumble motor (SCPH-110)<br/>
```
  1 (red)   Q1
  2 (black) GND (via some ohm)
```
M2 wires to right/small rumble motor (SCPH-110)<br/>
```
  1 (red)   +7.5V
  2 (black) Q2
```

#### U1 ("SD707, 039 107")
```
  1 via R9/Q2 to M2 (right/small)     (digital 0V=off, 3V=on)
  2 via "JP1" to LED (330 ohm)
  3 +3.5V
  4 BUTTON Bit2 R3
  5 vr2 RX (lt/rt)
  6 vr1 RY (up/dn)
  7 vr4 LX (lt/rt)
  8 vr3 LY (up/dn)
  9 BUTTON Bit1 L3
  10 GND3
  11 GND7
  ---
  12 via Q1 to M1 (left/large)       (1V=off, 6V=fast)
  13 via D1/R7 to M1 (left/large)    (6.7V)
  14 +7.5V
  15 +7.5V
  16 BUTTON Bit8 L2
  17 BUTTON Bit10 L1
  18 BUTTON Bit4 UP
  19 BUTTON Bit5 RIGHT
  20 BUTTON Bit6 DOWN
  21 BUTTON Bit7 LEFT
  22 GND3
  ---
  23 BUTTON Bit9 R2
  24 BUTTON Bit11 R1
  25 BUTTON Bit12 TRIANGLE /\
  26 BUTTON Bit13 CIRCLE   ()
  27 BUTTON Bit14 CROSS    ><
  28 BUTTON Bit15 SQUARE   []
  29 BUTTON Bit3 START
  30 BUTTON Bit0 SELECT
  31 ANALOG BUTTON
  32 NC
  33 +3.5V
  ---
  34 GND3
  35 NC
  36 via R5 to /IRQ7
  37 via R1 to /SEL
  38 via R4 to CMD
  39 via R3 to DAT
  40 via R2 to CLK
  41 +7.5V
  42 +7.5V
  43 GND7
  44 GND7
```

#### Misc
VR1..VR4 -- analog inputs<br/>
R1..R5 -- signals to/from psx<br/>
R6              ?<br/>
R7              M1<br/>
R8<br/>
R9<br/>
R10<br/>
JP1<br/>
C1 3.5V to GND3 (22uF)<br/>
C2 3.5V to GND3 (U1)<br/>
C3 VR1 to GND3<br/>
C4 VR2 to GND3<br/>
C5 VR3 to GND3<br/>
C6 VR4 to GND3<br/>
C7 M2+ to M2-<br/>
C8 M1+ to M1-<br/>
C9 M1 related<br/>
S5<br/>
S6<br/>

#### Motors
```
 Left/Large Motor (SCPH-110)
  23.0mm Total Length (12.0mm Motor, 3mm Axis, 8.0mm Weight/plates)
  24.0mm Diameter (Motor), 20.0mm Diameter (Weight/plates)
 Right/Small Motor (SCPH-110)
  25.4mm Total Length (18.7mm Motor, 2mm Axis, 4.7mm Weight/plates)
  12.0mm Width/Diameter (of Weight, and of Motor at flat side)
```

```
  M1+ --o---Q1---o--------- U1.12
        |   |    |          analog
  Left  |   |    C9
  Large |   |    |
        |   o----o--------- 7.5V
        |        |
       C8       R7
        |   D1   |          6.7V
        o---|>|--o--------- U1.13
        |
  M1- --o------------------ GND7
```

D1 is probably a Z-diode with R7 as pull-up, creating a reference/source
voltage at U1.13 for the analog output at U1.12.<br/>

```
  M2+ --o------------------ 7.5V
        |
  Right |   o-------o--R9-- U1.1
  Small |   |       |       on/off
       C7   |       R10
        |   |       |
  M2- --o---Q2------o------ GND7
                                   ___                          ___ ____
       axis                       |   |                        /   \    \
     __/___                 ______| m |        __.____________|__.  |    |
   /__/__/ |               | w |  |   |       |     | | axis  |     |    |
  |      |/  weight        |___|  |___|        \___/_/         \___/____/
   \____/                                      weight             motor
```
