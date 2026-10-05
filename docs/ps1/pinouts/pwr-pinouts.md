#   PWR Pinouts
#### Voltage Summary
```
  +7.5V  Used to generate other voltages and CDROM/Joypad/MemoryCard/Expansion
  +5.0V  Used for Multiout, IC405, and IC502, and IC602
  +3.5V  Used for most ICs, and for Joypad/MemoryCard/Expansion
  +3.48V Used for SPU and CDROM
  GND    Ground, shared for all voltages
```

#### Fuses
There are a lot of SMD elements marked FBnnn, these are NOT fuses (at least
they don't seem to blow-up whatever you do). The actual fuses are marked PSnnn,
found near the power switch and near the power socket.<br/>

#### IC601 3pin   +5.0V   "78M05, RZ125, (ON)"
```
  1 +7.5V
  2 GND
  3 +5.0V   (used for Multiout, IC405, and IC502)
```

#### IC602 - Audio/CDROM Supply
Called "LP29851MX-3.5" in service manual.<br/>
```
  1 VIN    5.0V (in)
  2 GND    GND
  3 ON/OFF 5.0V (in)
  4 NOISE  ?
  5 VOUT   3.48V (out)
```

#### IC002/IC003 - Reset Generator (PM-41 board)
```
  IC002  IC003  Expl.
  2      2      connected to Q002 (reset input?)
  5      5      connected via capacitor to GND
  6      1      reset-output (IC002=wired to /RES, IC003: via Q004 to /RES)
  7      -      7.5V
  4      3      GND
  1,3,8  4      NC
```
/RES is connected via 330 ohm to GPU/CPU, and via 5K6 SPU/IC722/IC304.<br/>
Note: Either IC002 or IC003/Q004 can be installed on PM-41 boards. Most or all
boards seem to contain IC003/Q004.<br/>
Note: PSX consoles have something similar on the Power Supply boards (IC101:
M51957B).<br/>

#### IC606/IC607 - TL594CD - Pulse-Width-Modulation Power-Control Chip
```
  1 1IN+
  2 1IN-
  3 FEEDBACK
  4 DTC
  5 CT
  6 RT
  7 GND
  8 C1
  9  E1
  10 E2
  11 C2
  12 VCC
  13 OUTPUT CTRL
  14 REF
  15 2IN-
  16 2IN+
```

#### Q602
```
  x +7.5V
  y +3.5V
  z REG
```

#### CN602 - PU-8, PU-9 board Power Socket (to internal power supply board)
```
  1 Brown   7.5V (actually 7.69V)
  2 Red     GND  Ground
  3 Orange  3.5V (actually 3.48V)
  4 Yellow  GND  Ground
  5 White   STAND-BY (3.54V, always ON, even if power switch is off)
  6 Blue    GND  Ground
  7 Magenta /RES Reset input (from power-on logic and reset button)
```
Purpose of the standy-by voltage is unknown... maybe to expansion port?<br/>

#### CN602 - PU-18, PU-23 board Power Socket (to internal power supply board)
```
  1 Brown   7.5V (actually 7.92V or so) (ie. higher than in PSone)
  2 Red     GND  Ground
  3 Orange  3.5V (actually 3.53V or so) (ie. quite same as PSone)
  4 Yellow  GND  Ground
  5 White   /RES Reset input (from power-on logic and reset button)
```

#### CN102 - Controller/memory card daughter-board connector (PU-23 board)
```
  1 /IRQ10 (/IRQ10)
  2 /ACK (/IRQ7)
  3 /JOY2
  4 7.5V (or actually 7.92V)
  5 /JOY1
  6 DAT
  7 GND
  8 CMD
  9 3.5V
  10 CLK
```
