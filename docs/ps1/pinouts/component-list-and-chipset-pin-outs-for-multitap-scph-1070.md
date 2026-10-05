#   Component List and Chipset Pin-Outs for Multitap, SCPH-1070
#### Multitap Component List
```
  Case "SONY, MULTITAP, SonyComputerEntertainmentInc, SCPH-1070 MADE IN CHINA"
  PCB1 "SONY 1-659-343-11" (mainboard with Slot A,B, ICs, X1, PSX-cable)
  PCB2 "SONY 1-711-414-11" (daughterboard with Slot C,D)
  IC? 64pin "SONY JAPAN, CXD103, -166Q, 550D66E"            (smd/back side)
  IC02 8pin "7W14, 5K" some tiny SMD chip (for JOYCLK)      (smd/back side)
  X1   2pin "4.00G CMj" oscillator                          (front side)
  J34  2pin fuse or 1 ohm resistor or so (for +3.5V input)  (front side)
  Jxx  2pin normal wire bridges (except: J34 is NOT a wire) (front side)
```
Cables from Multitap PCB1 to PCB2:<br/>
```
  1pin black wire Shield/GND (lower edge)
  1pin black wire Shield/GND (upper edge)
  2x8pin red/gray ribbon cable (side edge)
  2x2pin red/gray ribbon cable (lower edge)
  2pin red/gray ribbon cable (upper middle) (gray=+3.3V, red=+7.5V)
```
plus a bunch of SMD capacitors and around 70 SMD resistors.<br/>

#### Multitap PSX Controller Port Cable
```
  PSX.1 -------brown------ TAP.1 JOYDAT ;via  47 ohm (R57) to CXD.35
  PSX.2 -------orange----- TAP.2 JOYCMD ;via 220 ohm (R58) to CXD.37
  PSX.3 -------magenta---- TAP.3 +7.5V  ;directly to +7.5V on JOY/CARD's
  PSX.4 -------black------ TAP.4 GND    ;directly to GND
  PSX.5 -------red-------- TAP.5 +3.5V  ;via 1 ohm or so (J34) to +3.3V
  PSX.6 -------yellow----- TAP.6 /JOYn  ;via 220 ohm (R59) to CXD.46
  PSX.7 -------blue------- TAP.7 JOYCLK ;via 220 ohm (R60) to IC02.pin6
  PSX.8 -------gray------- TAP.8 /IRQ10 ;via 47 ohm (R02/R16/R30/R44) to JOY's
  PSX.9 -------green------ TAP.9 /ACK   ;via 47 ohm (R61) to CXD.51
  PSX.Shield --shield----- TAP.shielding.plate (GND)
```

#### Multitap CARD A/B/C/D Slots
```
  1 JOYDAT Via  47 ohm (R11/R25/R38/R5x) to CXD.18/29/60/5 (and to JOY slot)
  2 JOYCMD Via 220 ohm (R10/R24/R39/R52) to CXD.19/30/62/6
  3 +7.5V  Directly to PSX.3
  4 GND    Directly to PSX.4
  5 +3.3V  Via J34 to PSX.5 (+3.5V)
  6 /JOYn  Via 220 ohm (R09/R2x/Rxx/R51) to CXD.11/22/52/61
  7 JOYCLK Via 220 ohm (R08/R2x/Rxx/R50) to CXD.33/33/47/47
  9 /ACK   Via  47 ohm (R07/R2x/Rxx/R49) to CXD.12/21/45/64
```

#### Multitap JOY A/B/C/D Slots
```
  1 JOYDAT Via  47 ohm (R06/Rxx/R34/R5x) to CXD.18/29/60/5 (and to CARD slot)
  2 JOYCMD Via 220 ohm (R05/R19/R35/R5x) to CXD.17/28/59/4
  3 +7.5V  Directly to PSX.3
  4 GND    Directly to PSX.4
  5 +3.3V  Via 1 ohm or so (J34) to PSX.5 (+3.5V)
  6 /JOYn  Via 220 ohm (R04/R18/R32/R4x) to CXD.16/20/55/63
  7 JOYCLK Via 220 ohm (R03/R17/R31/R45) to CXD.15/23/56/2
  8 /IRQ10 Via  47 ohm (R02/R16/R30/R44) to PSX.8
  9 /ACK   Via  47 ohm (R01/R15/R29/R43) to CXD.13/27/54/7
  Shield   Directly to Shield/GND
```

#### Multitap IC02 8pin "7W14, 5K" some tiny SMD chip
```
  1
  2
  3
  4 GND
  5
  6 via 220 ohm (R60) to PSX.7 (JOYCLK)
  7 to CXD.Pin48
  8 +3.3V, aka via 1 ohm (J34) to PSX.5 (+3.5V)
```

#### Multitap "SONY CXD103-166Q" Chip Pin-Outs (Multitap CPU)
```
  1 via to 10K (R63) to +3.3V, and via C13 to GND (probably power-on reset)
  2 JOY.D.7.JOYCLK
  3
  4 JOY.D.2.JOYCMD
  5 JOY/CARD.D.1.JOYDAT
  6 CARD.D.2.JOYCMD
  7 JOY.D.9./ACK
  8 4MHz X1/C12
  9 4MHz X1/C11
  10 GND
  11 CARD.A.6./JOYn
  12 CARD.A.9./ACK
  13 JOY.A.9./ACK
  14
  15 JOY.A.7.JOYCLK
  16 JOY.A.6./JOYn
  17 JOY.A.2.JOYCMD
  18 JOY/CARD.A.1.JOYDAT
  19 CARD.A.2.JOYCMD
  ---
  20 JOY.B.6./JOYn
  21 CARD.B.9./ACK
  22 CARD.B.6./JOYn
  23 JOY.B.7.JOYCLK
  24
  25 GND
  26 +3.3V
  27 JOY.B.9./ACK
  28 JOY.B.2.JOYCMD
  29 JOY/CARD.B.1.JOYDAT
  30 CARD.B.2.JOYCMD
  31 GND
  32
  ---
  33 CARD.A/B.7.JOYCLK
  34
  35 PSX.1.JOYDAT
  36
  37 PSX.2.JOYCMD
  38
  39
  40
  41
  42 GND
  43
  44 GND
  45 CARD.C.9./ACK
  46 PSX.6./JOYn
  47 CARD.C/D.7.JOYCLK
  48 IC02.Pin7.PSX.JOYCLK
  49
  50
  51 PSX.9./ACK
  ---
  52 CARD.C.6./JOYn
  53
  54 JOY.C.9./ACK
  55 JOY.C.6./JOYn
  56 JOY.C.7.JOYCLK
  57 GND
  58 +3.3V
  59 JOY.C.2.JOYCMD
  60 JOY/CARD.C.1.JOYDAT
  61 CARD.D.6./JOYn
  62 CARD.C.2.JOYCMD
  63 JOY.D.6./JOYn
  64 CARD.D.9./ACK
```
