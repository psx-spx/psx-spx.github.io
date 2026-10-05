#   DRV Pinouts
#### IC304 - 52pin/80pin - Motorola HC05 8bit CPU
[HC05 Pinouts](hc05-pinouts.md#hc05-pinouts)<br/>

#### IC305 - SONY CXD1815Q - CDROM Decoder/FIFO (used on PU-8, PU-16, PU-18)
```
  1-D0    14-/XINT 27-/HRD  40-GND   53-VDD   66-/MWR  79-GND   92-LRCO
  2-D1    15-GND   28-VDD   41-HDRQ  54-GND   67-MDB0  80-CLK   93-WCKO
  3-VDD   16-A0    29-GND   42-/HAC  55-MA8   68-MDB1  81-HCLK  94-BCKO
  4-GND   17-A1    30-/HWR  43-MA0   56-MA9   69-MDB2  82-CKSL  95-MUTE
  5-D2    18-A2    31-HD0   44-MA1   57-MA10  70-MDB3  83-RMCK  96-TD7
  6-D3    19-A3    32-HD1   45-MA2   58-MA11  71-MDB4  84-LRCK  97-TD6
  7-D4    20-A4    33-HD2   46-T01   59-MA12  72-MDB5  85-DATA  98-TD5
  8-D5    21-TD0   34-HD3   47-T02   60-MA13  73-MDB6  86-BCLK  99-TD4
  9-D6    22-/HRS  35-HD4   48-MA3   61-MA14  74-MDB7  87-C2PO  100-TD3
  10-D7   23-/HCS  36-HD5   49-MA4   62-MA15  75-MDBP  88-EMP
  11-/CS  24-HA0   37-HD6   50-MA5   63-MA16  76-XTL2  89-/RST
  12-/RD  25-HA1   38-HD7   51-MA6   64-/MOE  77-XTL1  90-GND
  13-/WR  26-HINT  39-HDP   52-MA7   65-GND   78-VDD   91-DATO
```
Pin 1..20 to HC05 CPU, pin 22..42 to MIPS cpu, pin 43..75 to SRAM cd-buffer.<br/>
The pinouts/registers in CXD1199AQ datasheet are about 99% same as CXD1815Q.<br/>
Note: Parity on the 8bit data busses is NC. SRAM is 32Kx8 (A15+A16 are NC).
Later boards have this integrated in the SPU.<br/>

#### ICsss - SONY CXA1782BR - CDROM Servo Amplifier (used on PU-8 boards)
```
  1-FEO    7-FE_M   13-RA_O  19-CLK    25-FOK   31-RF_O  37-FE_BIAS 43-LPFI
  2-FEI    8-SRCH   14-SL_P  20-XLT    26-CC2   32-RF_M  38-F       44-TEI
  3-FDFCT  9-TGU    15-SL_M  21-DATA   27-CC1   33-LD    39-E       45-ATSC
  4-FGD    10-TG2   16-SL_O  22-XRST   28-CB    34-PD    40-EI      46-TZC
  5-FLB    11-FSET  17-ISET  23-C.OUT  29-CP    35-PD1   41-GND     47-TDFCT
  6-FE_O   12-TA_M  18-VCC   24-SENS   30-RF_I  36-PD2   42-TEO     48-VC
```
Datasheet exists. Later boards have CXA1782BR+CXD2510Q integrated in CXD2545Q,
and even later boards have it integrated in the SPU.<br/>

#### IC309 - SONY CXD2510Q - CDROM Signal Processor (used on PU-8, PU-16 boards)
```
  1-FOK   11-PDO   21-GNDa 31-WDCK        41-DA09-XPLCK 51-APTL 61-EMPH 71-DATA
  2-FSW   12-GND   22-VLTV 32-LRCK        42-DA08-GFS   52-GND  62-WFCK 72-XLAT
  3-MON   13-TEST0 23-VDDa 33-VDD 5V      43-DA07-RFCK  53-XTAI 63-SCOR 73-VDD
  4-MDP   14-NC    24-RF   34-DA16-SDTA48 44-DA06-C2PO  54-XTAO 64-SBSO 74-CLOK
  5-MDS   15-NC    25-BIAS 35-DA15-SCLK48 45-DA05-XRAOF 55-XTSL 65-EXCK 75-SEIN
  6-LOCK  16-VPCO  26-ASYI 36-DA14-SDTA64 46-DA04-MNT3  56-FSTT 66-SQSO 76-CNIN
  7-NC    17-VCKI  27-ASYO 37-DA13-SCLK64 47-DA03-MNT2  57-FSOF 67-SQCK 77-DATO
  8-VCOO  18-FILO  28-ASYE 38-DA12-LRCK64 48-DA02-MNT1  58-C16M 68-MUTE 78-XLTO
  9-VCOI  19-FILI  29-NC   39-DA11-GTOP   49-DA01-MNT0  59-MD2  69-SENS 79-CLKO
  10-TEST 20-PCO   30-PSSL 40-DA10-XUGF   50-APTR       60-DOUT 70-XRST 80-MIRR
```
Datasheet exists. Later boards have CXA1782BR+CXD2510Q integrated in CXD2545Q,
and even later boards have it integrated in the SPU.<br/>

#### IC701 - SONY CXD2545Q - Signal Processor + Servo Amp (used on PU-18 boards)
```
  1-SRON  14-TEST 27-TE   40-VDDa        53-DA09-XPLCK 66-FSTI 79-MUTE 92-DFCT
  2-SRDR  15-GND  28-SE   41-VDD         54-DA08-GFS   67-FSTO 80-SENS 93-FOK
  3-SFON  16-TES2 29-FE   42-ASYE        55-DA07-RFCK  68-FSOF 81-XRST 94-FSW
  4-TFDR  17-TES3 30-VC   43-PSSL        56-DA06-C2PO  69-C16M 82-DIRC 95-MON
  5-TRON  18-PDO  31-FILO 44-WDCK        57-DA05-XRAOF 70-MD2  83-SCLK 96-MDP
  6-TRDR  19-VPCO 32-FILI 45-LRCK        58-DA04-MNT3  71-DOUT 84-DFSW 97-MDS
  7-TFON  20-VCKI 33-PCO  46-DA16-SDTA48 59-DA03-MNT2  72-EMPH 85-ATSK 98-LOCK
  8-FFDR  21-VDDa 34-CLTV 47-DA15-SCLK48 60-DA02-MNT1  73-WFCK 86-DATA 99-SSTP
  9-FRON  22-IGEN 35-GNDa 48-DA14-SDTA64 61-DA01-MNT0  74-SCOR 87-XLAT 100-SFDR
  10-FRDR 23-GNDa 36-RFAC 49-DA13-SCLK64 62-XTAI       75-SBSO 88-CLOK
  11-FFON 24-ADIO 37-BIAS 50-DA12-LRCK64 63-XTAO       76-EXCK 89-COUT
  12-VCOO 25-RFC  38-ASYI 51-DA11-GTOP   64-XTSL/GNDed 77-SQSO 90-VDD
  13-VCOI 26-RFDC 39-ASYO 52-DA10-XUGF   65-GND        78-SQCK 91-MIRR
```
Datasheet exists. The CXD2545Q combines the functionality of CXA1782BR+CXD2510Q
from older boards (later boards have it integrated in the SPU). XTAI/XTAO input
is 16.9344MHz (44.1kHz\*180h), with XTSL=GND. Clock outputs are
FSTO=16.9344MHz/3, FSOF=16.9344MHz/4, C16M=16.9344MHz/1.<br/>

#### IC101 - SONY CXD2515Q - Signal Processor + Servo Amp (used on DTL-H2010)
Pinouts are same as CXD2545Q, except, three pins are different: Pin24=ADII
(instead of ADIO), Pin25=ADIO (instead of RFC), Pin68=C4M (instead of FSOF).<br/>

#### IC720 - 144pin SONY CXD1817R  (=CXD2545Q+CXD1815Q)  ;PU-20
```
  1..48 - unknown
  49 - SCOR
  50..144 - unknown
```

#### IC701 - 8pin chip (on bottom side, but NOT installed) (PU-7 and EARLY-PU-8)
```
  1-8 Unknown (maybe CDROM related, at least it's near other CDROM chips)
```

#### IC722 "BA5947FP" or "Panasonic AN8732SB" - IC for Compact Disc Players
Drive Motor related.<br/>
```
  1 to pin24,27
  2 SPINDLE            - via 15K to SPU21
  3 SW (ON/OFF)        - IC304.27
  4 TRACKING FORWARD
  5 TRACKING REVERSE
  6 FOCUS FORWARD
  7 FOCUS REVERSE
  8 GND                - CN702 pin 11
  9 NC (INTERNAL)      - via C731 (10uF) to GND
  10 +7.5V (Pow VCC ch1,2)
  11 FOCUS COIL (1)    - CN702 pin 15
  12 FOCUS COIL (2)    - CN702 pin 14
  13 TRACKING COIL (1) - CN702 pin 16
  14 TRACKING COIL (2) - CN702 pin 13
  15 SPINDLE MOTOR (1) - CN701 pin 4
  16 SPINDLE MOTOR (2) - CN701 pin 3
  17 SLED MOTOR (1)    - CN701 pin 1
  18 SLED MOTOR (2)    - CN701 pin 2
  19 +7.5V (Pow VCC ch3,4)
  20 MUTE              - /RES (via 5K6)
  21 GND
  22 SLED REVERSE
  23 SLED FORWARD
  24 to pin1
  25 via capacitors to pin1
  26 BIAS 1.75V
  27 to pin1
  28 +7.5V (Pre VCC)
```
Additionally to the above 28pins, the chip has two large grounded pins (between
pin 7/8 and 21/22) for shielding or cooling purposes.<br/>

#### IC703 - 20pin - "SONY CXA1791N" (RF Amplifier) (on PU-18 boards)
```
  1 LD       O APC amplifier output
  2 PD       I APC amplifier input
  3 PD1      I Input 1 for RF I-V amplifiers
  4 PD2      I Input 2 for RF I-V amplifiers
  5 GND/VEE  - Supply Ground
  6 F        I Input F for I-V amplifier
  7 E        I Input E for I-V amplifier
  8 VR       O DC Voltage Output (VCC+VEE)/2
  9 VC       I Center Voltage Input
  10 NC      - NC
  11 NC      - NC
  12 EO      O Monitoring Output for I-V amplifier E
  13 EI      - Gain Adjust for I-V amplifier E
  14 TE      O Tracking Error Amplifier Output
  15 FE_BIAS I BIAS Adjustment for Focus Error
  16 FE      O Focus Error Amplifier Output
  17 RFO     O RF Amplifier Output
  18 RFI     I RF Amplifier Input
  19 /LD_ON  I APC amplifier ON=GND, OFF=VCC
  20 VCC     - Supply
```
Datasheet for CXA1791N does exist. Later boards have IC703 replaced by IC723.
Older PU-7/PU-8 boards appear to have used a bunch of smaller components (8pin
chips and/or transistors) instead of 20pin RF amplifiers.<br/>

#### IC723 - 20pin - "SONY CXA2575N-T4" (RF (Matrix?) Amplifier) (PU-22..PM-41(2))
```
  1-TEIM
  2-TEIG
  3-VEE     GND
  4-E       via 33K to CN702 pin 4
  5-F       via 33K to CN702 pin 8
  6-PD2     via 36K to CN702 pin 6
  7-PD1     via 36K to CN702 pin 7
  8-PD      to CN702 pin 9
  9-LD
  10-VC     CL710, and CN702.Pin3, and via resistor?/diode? to SPU42
  11-LD_ON    IC304.Pin49 "LDON"  ..... XXX or is that Pin 20 "LD_ON" ?
  12-G_CONT                                                        ;or AL/TE?
  13-RF0    CL704, and...
  14-RFM
  15-FE     CL708, and...                 (maybe focus error?)
  16-TE     CL709, and via 15K to SPU.39  (maybe tracking error?)
  17-TE0
  18-COMP+
  19-MIRR   via 4K7 to SPU66
  20-VCC    3.48V (not 3.5V)
```
Used only on PU-22 .. PM-41(2) boards (PU-18 boards used IC703 "CXA1791N", and
even older boards... maybe had this in CXA1782BR... or maybe had it in a bunch
of 8pin NJMxxxx chips?).<br/>
There is no CXA2575N datasheet (but maybe some signals do resemble
CXA2570N/CXA2571N/CXA1791N datasheets).<br/>

#### CN702 CDROM Data Signal socket (PU-23 and PM-41 board)
```
  1-LD     to Q701
  2-VCC    to Q701
  3-VC     to IC723.Pin10 (and CL710)
  4-F-     to IC723.Pin4 (via 33K ohm)
  5-NC     to CL776
  6-PD2    to IC723.Pin6 (via 33K ohm)
  7-PD1    to IC723.Pin7 (via 33K ohm)
  8-E-     to IC723.Pin5 (via 33K ohm)
  9-M1     to IC723.Pin8
  10-VR    via 91 ohm to GND
  11-GND   GND
  12-LS    /POS0 (switch, GNDed when at head is at inner-most position)
  13-FCS+  TRACKING COIL (2)   ;\
  14-TRK+  FOCUS COIL (2)      ; or swapped?
  15-TRK   FOCUS COIL (1)      ;
  16-FCS   TRACKING COIL (1)   ;/
```
PU-23 and PM-41 board seem to be using exactly the same Drive, the only
difference is the length (and folding) of the attached cable.<br/>

#### CN701 CDROM Motor socket (PU-8, PU-18, PU-23, PM-41 boards)
```
  1-SL-   SLED MOTOR (1)
  2-SL+   SLED MOTOR (2)
  3-SP+   SPINDLE MOTOR (2)
  4-SP-   SPINDLE MOTOR (1)
```

#### CLnnn - Calibration Points (PU-23 and PM-41 boards)
```
  CL616 +7.5V (PM-41 only, not PM-23) (before power switch)
  CL617 GND   (PM-41 only, not PM-23)
  CL316 to IC304 pin 21
  CL704 to IC723.Pin13
  CL706 GND
  CL708 to IC723.Pin15
  CL709 to IC723.Pin16
  CL710 to IC723.Pin10, and CN702.Pin3
  CL711 via 1K to IC723.Pin15
  CL776 to CN702.Pin5
```
Probably test points for drive calibration or so.<br/>
