#   Pinouts - HC05 Pinouts
#### Motorola HC05 chip versions for PSX cdrom control
```
  80pin "4246xx" - MC68HC05L16, on-chip ROM (DTL-H120x & old retail consoles)
  80pin "MC68HC705L16CFU" - MC68HC705L16, on-chip ROM (DTL-H100x, and PU-9)
  52pin "SC4309xx" - MC68HC05G6, on-chip ROM (newer retail consoles)
```
The early DTL-H2000 devboard is also using a 80pin CPU (with piggyback EPROM
socket), but that CPU is a Sony CXP82300 SPC700 CPU, not a Motorola HC05 CPU.<br/>

#### IC304 - "C 3060, SC430943PB, G63C 185" (PAL/PSone) - CDROM Controller
Called "MC68HC05G6PB" in service manual (=8bit CPU).<br/>
```
  1  NC     NC (TEST:DTR/out) (VCD:AVSEL/out)   ;-Port F           ;PortF.Bit3
  2  VDD    3.5V
  3  NC     NC          ;\                                   ;maybe PortE.Bit7?
  4  NC     NC          ; maybe MSBs of Port E               ;maybe PortE.Bit6?
  5  NC     NC          ;/                                   ;maybe PortE.Bit5?
  6  DECA4  SPU102      ;\                                         ;PortE.Bit4
  7  DECA3  SPU101      ; Port E [04h], aka Address/Index          ;PortE.Bit3
  8  DECA2  SPU99       ;                                          ;PortE.Bit2
  9  DECA1  SPU98       ;                                          ;PortE.Bit1
  10 DECA0  SPU97       ;/                                         ;PortE.Bit0
  11 VSS    GND
  12 NDLY   GND     reserved for factory test, should be wired to VDD, not GND?
  13 /RES   /RES (via 5K6)
  14 OSC1   4.3MHz (SPU11)(used as external clock for some modchips)(low volts)
  15 OSC2   NC
  16 F-BIAS         aka FOK=NC (in SCPH-5500)                      ;PortB.Bit0
  17 CG     NC      aka CG=CG (in SCPH-5500)     ;this IS portb.1! ;PortB.Bit1
  18 LMTSW  /POS0 (switch, GNDed when head at inner-most position) ;PortB.Bit2
  19 DOOR   SHELL_OPEN                                             ;PortB.Bit3
  20 TEST2  NC                                                     ;PortB.Bit4
  21 TEST1  to CL316                                               ;PortB.Bit5
  22 COUT               NC                                         ;PortB.Bit6
  23 SENSE  SPU82  ;CXD2510Q.69                                    ;PortB.Bit7
  24 SUBQ   SPU81  ;CXD2510Q.66                                    ;PortC.Bit0
  25 NC     NC     ;NC                                             ;PortC.Bit1
  26 SQCK   SPU80  ;CXD2510Q.67                                    ;PortC.Bit2
  27 SPEED  IC722.Pin3 (SW)                                        ;PortC.Bit3
  28 AL/TE         ;transisor aka MIRROR=..   (in SCPH-5500);ISN'T PortB.Bit1 !
  29 ROMSEL        ;NC        aka ROMSEL=SCLK (in SCPH-5500)       ;PortC.Bit5
  30 /XINT  SPU79  ;CXD1815Q.14                                    ;PortC.Bit6
  31 SCOR   SPU77  ;CXD2510Q.63                                    ;PortC.Bit7
  32 VDD    3.5V
  33 DECD0  CD.D0       ;\                                         ;PortA.Bit0
  34 DECD1  CD.D1       ;                                          ;PortA.Bit1
  35 DECD2  CD.D2       ;                                          ;PortA.Bit2
  36 DECD3  CD.D3       ; Port A [00h], aka Data                   ;PortA.Bit3
  37 DECD4  CD.D4       ;                                          ;PortA.Bit4
  38 DECD5  CD.D5       ;                                          ;PortA.Bit5
  39 VSS    GND         ;
  40 DECD6  CD.D6       ;                                          ;PortA.Bit6
  41 DECD7  CD.D7       ;/                                         ;PortA.Bit7
  42 NC     NC                                               ;maybe PortD.Bit0?
  43 DATA   SPU74 (via 22 ohm)                                     ;PortD.Bit1
  44 XLAT   SPU75 (via 22 ohm)                                     ;PortD.Bit2
  45 CLOK   SPU76 (via 22 ohm)                                     ;PortD.Bit3
  46 DECCS  SPU94                                                  ;PortD.Bit4
  47 DECWR  SPU95                                                  ;PortD.Bit5
  48 DECRD  SPU96                                                  ;PortD.Bit6
  49 LDON   IC723.Pin11                                            ;PortD.Bit7
  50 NC     NC (TEST:TX/out)  (VCD:SIO.IN/in)   ;\PortF (used by   ;PortF.Bit0
  51 NC     NC (TEST:RX/in)   (VCD:SIO.OUT/out) ; Motorola Testmode;PortF.Bit1
  52 NC     NC (TEST:RTS/out) (VCD:SIO.CLK/out) ;/and VCD version) ;PortF.Bit2
```
This chip isn't connected directly to the CPU, but rather to a Fifo Interface,
which is then forwarding data to/from the CPU. On older PSX boards, that Fifo
Interface has been located in a separate chip, on newer PSX boards and PSone
boards, the Fifo stuff is contained in the SPU chip. The CDROM has a 32K
buffer, which is also implemeted at the Fifo Interface side.<br/>
OSC input (internally HC05 is running at OSC/2, ie. around 2MHz):<br/>
```
  PU-8      4.0000MHz from separate 4.000MHz oscillator (X302)
  PU-16     4.0000MHz from separate 4.000MHz oscillator (X302)
  DTL-H2000 4.1900MHz from separate 4.1900MHz oscillator (SPC700, not HC05)
  PU-18     4.2336MHz from CXD2545Q.pin68 (Servo+Signal) (FSOF=16.9344MHz/4)
  PU-20     4.2xxxMHz from CXD1817R.pin?  (Servo+Signal+Decoder)
  PM-41     4.2xxxMHz from CXD2938Q.pin11 (Servo+Signal+Decoder+SPU)
```

#### HC05 - 80pin version (pinout from MC68HC05L16 datasheet)
```
  1 VDD
  2 FP28/PE6    ;\
  3 FP29/PE5    ;
  4 FP30/PE4    ;
  5 FP31/PE3    ; Port E LSBs
  6 FP32/PE2    ;
  7 FP33/PE1    ;
  8 FP34/PE0    ;/
  9 FP35/PD7    ;\
  10 FP36/PD6   ; Port D MSBs
  11 FP37/PD5   ;
  12 FP38/PD4   ;/
  13 VLCD3
  14 VLCD2
  15 VLCD1
  16 VSS
  17 NDLY
  18 XOSC1
  19 XOSC2
  20 /RESET
  ---
  21 OSC1
  22 OSC2
  23 PA0        ;\
  24 PA1        ;
  25 PA2        ;
  26 PA3        ; Port A
  27 PA4        ;
  28 PA5        ;
  29 PA6        ;
  30 PA7        ;/
  31 PB0/KWI0   ;\
  32 PB1/KWI1   ;
  33 PB2/KWI2   ;
  34 PB3/KWI3   ; Port B
  35 PB4/KWI4   ;
  36 PB5/KWI5   ;
  37 PB6/KWI6   ;
  38 PB7/KWI7   ;/
  39 PC0/SDI    ;\
  40 PC1/SDO    ;
  ---           ;
  41 PC2/SCK    ; Port C
  42 PC3/TCAP   ;
  43 PC4/EVI    ;
  44 PC5/EVO    ;
  45 PC6/IRQ2   ;
  46 PC7/IRQ1   ;/
  47 VDD
  48 BP3/PD3            ;\
  49 BP2/PD2            ; Port D LSBs
  50 BP1/PD1            ;
  51 BP0 (no "PD0")     ;/
  52 FP0
  53 FP1
  54 FP2
  55 FP3
  56 FP4
  57 FP5
  58 FP6
  59 FP7
  60 VSS
  ---
  61 FP8
  62 FP9
  63 FP10
  64 FP11
  65 FP12
  66 FP13
  67 FP14
  68 FP15
  69 FP16
  70 FP17
  71 FP18
  72 FP19
  73 FP20
  74 FP21
  75 FP22
  76 FP23
  77 FP24
  78 FP25
  79 FP26
  80 FP27/PE7   ;- Port E MSB
```

#### HC05 - 32pin/64pin Versions
Sony's Digital Joypad and Mouse contain 32pin CPUs, which are probably also
HC05's:<br/>
[Pinouts - Component List and Chipset Pin-Outs for Digital Joypad, SCPH-1080](component-list-and-chipset-pin-outs-for-digital-joypad-scph-1080.md#pinouts-component-list-and-chipset-pin-outs-for-digital-joypad-scph-1080)<br/>
Moreover, some old memory cards contain a 64pin Motorola SC419510FU (probably
also a HC05) with separate Atmel AT29LV010A (128Kx8 FLASH).<br/>
