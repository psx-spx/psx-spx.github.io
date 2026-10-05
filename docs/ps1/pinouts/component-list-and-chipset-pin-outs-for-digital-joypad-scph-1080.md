#   Component List and Chipset Pin-Outs for Digital Joypad, SCPH-1080
#### Digital Joypad Component List (SCPH-1080)
```
  Case: "SONY, CONTROLLER, Sony Computer Entertainment Inc. H"
  Case: "SCPH-1080 Made in China"
  PCB: "CMK-PIHB /\, CFS8121-200010-01"
  U?: 32pin "(M), SC401800, FB C37B, JSJD520C" (Motorola) (TQFP-32 package)
  U?: 14pin "BA10339F, 528 293" (Quad Comparator) (/ACK,JOYDAT,and reset or so)
  X?:  3pin "4.00G1f" (on PCB bottom side)
  Z1:  2pin z-diode or so (on PCB bottom side) (+1.7V VREF for BA10339F)
  CN?: 7pin cable to controller port (plus shield; but not connected to PCB)
  C1   2pin   to GND and R5
  C2   2pin capacitor for power supply input (between +3.5V and GND)
  C3   2pin   between BA.pin8 and (via R6) BA.pin15
  R1   2pin 1M ohm (for X1)
  R2   2pin 2.7K
  R3   2pin 8xK ohm?
  R4   2pin 100K
  R5   2pin 22K ohm
  R6   2pin 56K ohm
  RN1  8pin 4x200 ohm (/JOYn,JOYCMD,JOYCLK)
  RN2  8pin 4x22K ohm (pull-ups for button bit0..3)
  RN3  8pin 4x22K ohm (pull-ups for button bit12..15)
  RN4  8pin 4x22K ohm (pull-ups for button bit8..11)
  RN5  8pin 4x22K ohm (pull-ups for button bit4..7)
```

#### Digital Joypad Connection Cable:
```
  PSX.1 -------brown---- PAD.2 JOYDAT
  PSX.2 -------orange--- PAD.6 JOYCMD
  PSX.3 ---              NC    +7.5V
  PSX.4 -------black---- PAD.3 GND
  PSX.5 -------red------ PAD.4 +3.5V
  PSX.6 -------yellow--- PAD.5 /JOYn
  PSX.7 -------blue----- PAD.7 JOYCLK
  PSX.8 ---              NC    /IRQ10
  PSX.9 -------green---- PAD.1 /ACK
  PSX.Shield --shield--- NC    (cable is shielded but isn't connected in joypad)
```

#### Digital Joypad 32pin SC401800 Chip Pin-Outs
```
  1 Bit14 SW-X
  2 Bit13 SW-O
  3 Bit12 SW-/\
  4 Bit11 SW-R1 (via cable pin1, white wire)
  5 Bit10 SW-L1 (via cable pin1, white wire)
  6 Bit9  SW-R2 (via cable pin3, black wire)
  7 Bit8  SW-L2 (via cable pin3, black wire)
  8 via BA10339F.pin7 to cn.2 JOYDAT (PSX.1)
  ---
  9  via RN1 (200 ohm) to cn.5 /JOYn  (PSX.6)
  10 via RN1 (200 ohm) to cn.6 JOYCMD (PSX.2)
  11 via RN1 (200 ohm) to cn.7 JOYCLK (PSX.7)
  12 GND to cn.3 (PSX.4)
  13 Bit7 SW-LEFT
  14 Bit6 SW-DOWN
  15 Bit5 SW-RIGHT
  16 via BA10339F.pin5 to cn.1 /ACK (PSX.9)
  ---
  17 Bit4 SW-UP
  18 Bit3 SW-START
  19 Bit2 (HI) (would be R3 on Analog Pads) ;\unused, but working button inputs
  20 Bit1 (HI) (would be L3 on Analog Pads) ;/(each fitted with a RN2 pullup)
  21 Bit0 SW-SELECT
  22
  23
  24 wired to SC401800.pin25
  ---
  25 wired to SC401800.pin24
  26 4.00MHz'a
  27 4.00MHz'b
  28 +3.5V to cn.4 (PSX.5)
  29 wired to SC401800.pin32, and via 22K ohm to +3.5V, and to BA.14
  30
  31 Bit15 SW-[]
  32 wired to SC401800.pin29
```

#### Digital Joypad 14pin BA10339F Chip Pin-Outs
```
  1 OUT2  CN.2 JOYDAT (PSX.1)
  2 OUT1  CN.1 /ACK (PSX.9)
  3 VCC   +3.5V
  4 -IN1  +1.7V VREF via Z1 to GND
  5 +IN1  CXD.16 /ACK
  6 -IN2  +1.7V VREF via Z1 to GND
  7 +IN2  CXD.8  JOYDAT
  ---
  8 -IN3  +1.7V VREF via Z1 to GND
  9 +IN3      C3,R3,R4
  10 -IN4     C1 to +3.5V
  11 +IN4 GND
  12 GND  GND
  13 OUT4     NC ??
  14 OUT3 CXD.29/32
```
