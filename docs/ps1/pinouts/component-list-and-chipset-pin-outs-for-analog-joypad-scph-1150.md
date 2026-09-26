#   Pinouts - Component List and Chipset Pin-Outs for Analog Joypad, SCPH-1150
This applies for two controller versions:<br/>
```
  SCPH-1150 Analog Pad with Single Rumble Motor (japan only)
  SCPH-1180 Analog Pad without Rumble Motor
```
Both are using the same PCB, and the same SD657 chip. The difference is that
the motor, transistors, and some resistors aren't installed in SCPH-1180.<br/>

#### Analog Joypad Component List (SCPH-1150, single motor)
```
  Case "SONY, ANALOG, CONTROLLER, SonyCompEntInc. A, SCPH-1150 MADE IN CHINA"
  PCB1 "DD1P09A" (mainboard with digital buttons)
  PCB2 "DD1Q14A" (daughterboard with analog joysticks)
  PCB3 "DD1Q15A-R" (daughterboard with R-1, R-2 buttons) (J3)
  PCB4 "DD1Q15A-L" (daughterboard with L-1, L-2 buttons) (J2)
  U1  42pin "SD657, 9702K3006"   (2x21pins, L=17.8mm, W=7mm, W+Pins=11mm)
  U2   3pin "DR, 4.Z"
  Q1   3pin "BQ03" or so (motor post-amp)
  Q2   3pin "S6","SG","9S" or so (motor pre-amp)
  Y1   3pin "400CMA"
  CN1  8pin cable to PSX controller port
  CN2  8pin ribbon cable to analog-joystick daughterboard (not so robust cable)
  J1   2pin wires to rumble motor (in left handle) (digital, on/off)
  J2   3pin ribbon cable to L-1, L-2 button daughterboard
  J3   3pin ribbon cable to R-1, R-2 button daughterboard
  LED1 4pin red/green LED (optics without mirror)
  D1,D2 diodes
  plus resistors/capacitors
```

#### Analog Joypad Connection Cables (SCPH-1150)
CN1 (cable to PSX controller port) (same for SCPH-1150 and SCPH-1200)<br/>
```
  PSX.1 -------brown---- PAD.2 JOYDAT
  PSX.2 -------orange--- PAD.6 JOYCMD
  PSX.3 -------magenta-- PAD.8 +7.5V
  PSX.4 -------black---- PAD.3 GND
  PSX.5 -------red------ PAD.4 +3.5V
  PSX.6 -------yellow--- PAD.5 /JOYn
  PSX.7 -------blue----- PAD.7 JOYCLK
  PSX.8 ---              NC    /IRQ10
  PSX.9 -------green---- PAD.1 /ACK
  PSX.Shield --shield--- NC    (cable is shielded but isn't connected in joypad)
```
CN2 (ribbon cable to analog-joystick daughterboard) (SCPH-1150)<br/>
```
  8 +3.5V to POT pins
  7 Button L3 pins A,C
  6 GND to POT pins and Button L3/R3 pins B,D
  5 Button R3 pins A,C
  4 Axis R_Y middle POT pin (SD657.18)
  3 Axis R_X middle POT pin (SD657.17)
  2 Axis L_Y middle POT pin (SD657.16)
  1 Axis L_X middle POT pin (SD657.15)
```
J3 (ribbon cable to R-1, R-2 button daughterboard) (SCPH-1150)<br/>
```
  1 (red)  R1
  2 (gray) GND
  3 (gray) R2
```
J2 (ribbon cable to L-1, L-2 button daughterboard) (SCPH-1150)<br/>
```
  1 (red)  L1
  2 (gray) GND
  3 (gray) L2
```
J1 wires to small rumble motor (SCPH-1150)<br/>
```
  1 (red)   +7.5V
  2 (black) Q1
```

#### Analog Joypad Chipset Pin-Outs (SCPH-1150)
U1 42pin "SD657, 9702K3006"<br/>
```
  1  NC?
  2  NC?
  3  /RESET? (U2.3)
  4  OSC
  5  OSC
  6  BUTTON Bit3 START SW1
  7  BUTTON Bit2 R3 (via CN2.5)
  8  BUTTON Bit1 L3 (via CN2.7)
  9  BUTTON Bit0 SELECT SW3
  10 GND
  11 BUTTON Bit7 LEFT  SW4
  12 BUTTON Bit6 DOWN  SW5
  13 BUTTON Bit5 RIGHT SW6
  14 BUTTON Bit4 UP    SW7
  15 Analog Axis L_X (via CN2.1)
  16 Analog Axis L_Y (via CN2.2)
  17 Analog Axis R_X (via CN2.3)
  18 Analog Axis R_Y (via CN2.4)
  19 NC?
  20 3.5V
  21 3.5V
  ---
  22 BUTTON Bit15 [] SW11
  23 BUTTON Bit14 >< SW10
  24 BUTTON Bit13 () SW9
  25 BUTTON Bit11 R1 (via J3.1)
  26 BUTTON Bit12 /\ SW8
  27 BUTTON Bit10 L1 (via J3.1)
  28 BUTTON Bit9  R2 (via J3.3)
  29 BUTTON Bit8  L2 (via J3.3)
  30 PSX.2/CN1.6 JOYCMD  orange (via 220 ohm R14)
  31 PSX.1/CN1.2.JOYDAT  brown  (via 22 ohm R13 and diode D2)
  32 PSX.7/CN1.7 JOYCLK  blue   (via 220 ohm R12)
  33 PSX.6/CN1.5./JOYn   yellow (via 220 ohm R11)
  34 LED.GREEN (LED.4)
  35 LED.RED   (LED.3)
  36 MOTOR (via 4.7Kohm R8 to Q2, then via Q1 to motor)
  37 NC?
  38 NC?
  39 PSX.9/CN1.1./ACK    green  (via 22 ohm R10)
  40 NC?
  41 MODE SW2 (analog button)
  42 GND
```
U2 (probably reset signal related)<br/>
```
  1  from 3.5V (via R1,D1,R2)
  2  to U1.3 (/RESET?) (U2.rear contact = same as U2.pin2)
  3  GND
```
Q1 "BQ03" or so (motor post-amp)<br/>
```
  1  Q2.2 (via 1Kohm R7)
  2  to Motor (-)
  3  GND
```
Q2 "S6","SG","9S" or so (motor pre-amp)<br/>
```
  1  SD657.36 (via 4.7Kohm R8)
  2  Q1.1 (via 1Kohm R7) (and via 100Kohm R13 to GND)
  3  3.5V
```

#### Motor
Left/Single Motor (SCPH-1150)<br/>
```
  27.5mm Total Length (18.5mm Motor, 2mm Axis, 7mm Weight/block)
  12.0mm Width/Diameter (of Weight, and of Motor at flat side)
```
