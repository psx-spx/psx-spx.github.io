#   Component List and Chipset Pin-Outs for Analog Joypad, SCPH-1200
#### Analog Joypad Component List (SCPH-1200, two motors)
```
  Case "SONY, ANALOG, CONTROLLER, SonyCompEntInc. H, SCPH-1200 MADE IN CHINA"
  PCB1 "01, /\YG-H2, (r)RU" (mainboard with digital buttons)
  PCB2 "M-29-01, YG-H3, (r)RU" (daughterboard with analog joysticks)
  PCB3 "E, /\YG-H2, (r)RU, 01" (daughterboard with R-1, R-2 buttons) (J1)
  PCB4 "01, W, /\YG-H2, (r)RU" (daughterboard with L-1, L-2 buttons) (J2)
  U1 44pin "SONY, CXD8771Q 4A03, JAPAN 9840 HAL, 148896"
  U2  4pin ",\\ 29" (PST9329) (System Reset with 2.9V detection voltage)
  U3  8pin "2904, 8346G, JRC" (NJM2904) (Dual Operational Amplifier)
  Q1  3pin ".Y S'" (big transistor for big M1 rumble motor)
  Q2  3pin "Z" (small transistor for small M2 rumble motor)
  Y1  3pin "800CMLX" or so (hides underneath of the CN2 ribbon cable)
  CN1 8pin cable to PSX controller port
  CN2 8pin ribbon cable to analog-joystick daughterboard
  J1  3pin ribbon cable to R-1, R-2 button daughterboard
  J2  3pin ribbon cable to L-1, L-2 button daughterboard
  M1  2pin wires to left/big rumble motor (analog, slow/fast)
  M2  2pin wires to right/small rumble motor (digital, on/off)
  ZD1,ZD2 some Z-diodes
  D1,D2 diodes near M1,M2 motors (these diodes aren't installed)
  LED1  red analog mode LED (with transparent optics/light direction mirror)
  plus resistors/capacitors
```

Note: There's also a different SCPH-1200 revision, which having a smaller
mainboard with analog joysticksonboard, plus a single sided PCB for the digital
buttons (that is, similar to SCPH-110, but with the single sided PCB instead of
membrane foil).<br/>

#### Analog Joypad Connection Cables (SCPH-1200)
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
CN2 (ribbon cable to analog-joystick daughterboard) (SCPH-1200)<br/>
```
  1 +3.5V to POT pins
  2 Button L3 pins C,D
  3 GND to POT pins and Button L3/R3 pins A,B
  4 Button R3 pins C,D
  5 Axis R_Y middle POT pin (CXD.20)
  6 Axis R_X middle POT pin (CXD.19)
  7 Axis L_X middle POT pin (CXD.21)
  8 Axis L_Y middle POT pin (CXD.22)
```
J1 (ribbon cable to R-1, R-2 button daughterboard) (SCPH-1200)<br/>
```
  1 (red)  R1
  2 (gray) GND
  3 (gray) R2
```
J2 (ribbon cable to L-1, L-2 button daughterboard) (SCPH-1200)<br/>
```
  1 (red)  L1
  2 (gray) GND
  3 (gray) L2
```
M1 wires to big rumble motor (SCPH-1200)<br/>
```
  + (red)   Q1.E
  - (black) GND
```
M2 wires to small rumble motor (SCPH-1200)<br/>
```
  + (red)   +7.5V
  - (black) Q2.C
```

#### Analog Joypad Chipset Pin-Outs (SCPH-1200)
U1 SONY CXD8771Q<br/>
```
  1 PSX.7/CN1.7 JOYCLK (via 220 ohm R2)
  2 via R10 to U3.3 (for big M1 motor)
  3 via R15 to Q2.B (for small M2 motor)
  4 GND
  5 BUTTON Bit15 []
  6 BUTTON Bit14 ><
  7 BUTTON Bit13 ()
  8 BUTTON Bit12 /\
  9 BUTTON Bit11 R1 (via J1.1)
  10 BUTTON Bit10 L1 (via J2.1)
  11 BUTTON Bit9 R2 (via J1.3)
  ---
  12 BUTTON Bit8 L2 (via J2.3)
  13 GND
  14 U2.Pin3 (reset)
  15 Y1'a
  16 Y1'b
  17 GND
  18 +3.5V
  19 Analog Axis R_X via CN2.6
  20 Analog Axis R_Y via CN2.5
  21 Analog Axis L_X via CN2.7
  22 Analog Axis L_Y via CN2.8
  ---
  23 GND
  24 GND
  25 GND
  26 GND
  27 GND
  28 +3.5V
  29 BUTTON Bit0 SELECT
  30 BUTTON Bit1 L3 (via CN2.2)
  31 BUTTON Bit2 R3 (via CN2.4)
  32 BUTTON Bit3 START
  33 BUTTON Bit4 UP
  ---
  34 BUTTON Bit5 RIGHT (aka spelled RIHGT on the PCB)
  35 BUTTON Bit6 DOWN
  36 BUTTON Bit7 LEFT
  37 PSX.6/CN1.5./JOYn  (via 220 ohm R1)
  38 ANALOG BUTTON
  39 GND
  40 +3.5V
  41 /LED (to LED1, and from there via 300 ohm R6 to +3.5V)
  42 PSX.9/CN1.1./ACK   (via 22 ohm R5)
  43 PSX.1/CN1.2.JOYDAT (via 22 ohm R3)
  44 PSX.2/CN1.6 JOYCMD (via 220 ohm R4)
```
U2 PST9329 (System Reset with 2.9V detection voltage)<br/>
```
  1 NC   GND
  2 GND  GND
  3 Vout U1.14
  4 VCC  +3.5V
```
U3 NJM2904 (Dual Operational Amplifier)<br/>
```
  1 A.OUTPUT  Q1.B (big motor M1 transistor)
  2 A.INPUT-  to R11/R12
  3 A.INPUT+  to R10/R17
  4 GND       PSX.4/CN1.3 GND
  5 B.INPUT+  GND
  6 B.INPUT-  NC?
  7 B.OUTPUT  NC?
  8 VCC       PSX.3/CN1.8 +7.5V
```
Q1 (transistor for big M1 motor)<br/>
```
  E M1+
  B U3.1 (NJM2904)
  C +7.5V
```
Q2 (transistor for small M2 motor)<br/>
```
  E GND
  B via 1K ohm R15 to U1.3 (CXD), and via 100K ohm R16 to GND
  C M2-
```

#### Motors
```
 Left/Large Motor (SCPH-1200)
  24.0mm Total Length (12.0mm Motor, 2.5mm Axis, 9.5mm Weight/plates)
  24.0mm Diameter (Motor), 20.0mm Diameter (Weight/plates)
 Right/Small Motor (SCPH-1200)
  25.4mm Total Length (18.7mm Motor, 2mm Axis, 4.7mm Weight/plates)
  12.0mm Width/Diameter (of Weight, and of Motor at flat side)
```
