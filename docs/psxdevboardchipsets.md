#   PSX Dev-Board Chipsets
#### Sony DTL-H2000 CPU Board
```
  CL825  20pin pin test points (2x10 pins)
  CL827  20pin pin test points (2x10 pins)
  U83    64pin SEC KM4216V256G-60 (DRAM 256Kx16) ;dual-ported VRAM
  U84    64pin SEC KM4216V256G-60 (DRAM 256Kx16) ;dual-ported VRAM
  CL828  20pin pin test points (2x10 pins)
  CL826  20pin pin test points (2x10 pins)
  X10     4pin JC53.20     (PAL, 53.203425MHz)
  X2      4pin 53.69317MHz (NTSC, 53.693175MHz)
  U62    20pin LVT244 (dual 4-bit 3-state noninverting buffer/line driver)
  U27    64pin Sony CXD2923AR    ;GPU'b
  CL813  20pin pin test points (2x10 pins)
  CL814  20pin pin test points (2x10 pins) (with one resistor or so installed)
  U16   160pin Sony CXD8514Q     ;GPU'a
  X7      4pin 67.73760 MHz
  CL807  20pin pin test points (2x10 pins)
  CL809  20pin pin test points (2x10 pins)
  CL811  20pin pin test points (2x10 pins)
  U801  208pin Sony CXD8530BQ    ;CPU
  U11    28pin SEC KM48V2104AJ-6 (DRAM 2Mx8) ;Main RAM
  U10    28pin SEC KM48V2104AJ-6 (DRAM 2Mx8) ;Main RAM
  U9     28pin SEC KM48V2104AJ-6 (DRAM 2Mx8) ;Main RAM
  U8     28pin SEC KM48V2104AJ-6 (DRAM 2Mx8) ;Main RAM
  CN801 100pin Blue connector (to other ISA board)
  U66    48pin LVT16244? (quad 4-bit 3-state noninverting buffer/line driver)
  U65    48pin LVT16244? (quad 4-bit 3-state noninverting buffer/line driver)
  U64    48pin LVT16245? (dual 8-bit 3-state noninverting bus transceiver)
  U34   100pin Sony CXD2922Q     ;SPU
  U63    14pin 74F74N (dual flipflop)
  U32    44pin SEC KM416V256B1-8 (DRAM 256Kx16)  ;SoundRAM
  CL801  20pin pin test points (2x10 pins)
  CL802  20pin pin test points (2x10 pins)
  Q881    3pin voltage stuff?
  U31    20pin 74ACT244P (dual 4-bit 3-state noninverting buffer/line driver)
  U35    18pin Sony CXD2554P or OKI M6538-01 (aka MSM6538-01?) (audio related?)
  U36    20pin Sanyo LC78815  ;16bit D/A Converter
  U37     8pin NEC ...?    C4558C?   D426N0B or 9426HOB or so?
  J806    8pin solder pads...
  J805    9pin solder pads...
  J804   10pin solder pads... (11pins, with only 10 contacts?)
  -      48pin solder pads (12x4pin config jumpers or so)
  U26    20pin SN74ALSxxx logic?
  U71    24pin Sony CXA1xxxx?  ;RGB?
  JPxx    9pin PAL/NTSC Jumpers (three 3pin jumpers)
  J801   24pin solder pads...
  J803    9pin rear connector: Serial Port (3.3V) (aka "J308") (DB9) (5+4pin)
  J802   15pin rear connector: AV Multi-out   (5+5+5pin)
  CN881  98pin ISA Bus Cart-edge (2x31 basic pins, plus 2x18 extended pins)
```

#### Sony DTL-H2000 PIO Board
```
  JP72x 68pin Black connector (maybe equivalent to 68pin PSX expansion port?)
  SWI    5pin solder pads...
  U371  40pin HN27C4000G-12 (512Kx8 / 256Kx16 EPROM) (sticker: "94/7/27")
  U370  84pin Altera EPM7160ELC84-12 (sticker: "U730, cntl 1")
  U3    14pin SN74ALS1004N (hex inverters)
  U43   44pin Altera EPM7032LC44-10 (sticker: "U43, add 1")
  U716  28pin Sharp LH5498D-35 (FIFO 2Kx9)
  U717  28pin Sharp LH5498D-35 (FIFO 2Kx9)
  U719  28pin Sharp LH5498D-35 (FIFO 2Kx9)
  U720  28pin Sharp LH5498D-35 (FIFO 2Kx9)
  U724  20pin SN74ALS688N  (8bit inverting identity comparator with enable)
  U722  20pin SN74ALS245AN (8bit tristate noninverting bus transceiver)
  U47   20pin 74FCT244ATP  (dual 4-bit 3-state noninverting buffer/line driver)
  U732  48pin LVT16245? (dual 8-bit 3-state noninverting bus transceiver)
  U711  20pin SN74ALS244BN (dual 4-bit 3-state noninverting buffer/line driver)
  U712  20pin SN74ALS244BN (dual 4-bit 3-state noninverting buffer/line driver)
  U713  20pin 74HC244AP    (dual 4-bit 3-state noninverting buffer/line driver)
  U714  20pin 74HC244AP    (dual 4-bit 3-state noninverting buffer/line driver)
  U721  20pin SN74ALS244BN (dual 4-bit 3-state noninverting buffer/line driver)
  U55   14pin SN74ALS08N   (quad 2-input AND gates)
  U726  20pin SN74ALS245AN (8bit tristate noninverting bus transceiver)
  U715  20pin 74HC244AP    (dual 4-bit 3-state noninverting buffer/line driver)
  JPxx 100pin Blue connector (to other ISA board)
  U738  20pin LVT244 (SMD) (dual 4-bit 3-state noninverting buffer/line driver)
  U734  32pin KM684000G-7 (SRAM 512Kx8)         ;\maybe 1Mbyte EXP3 RAM ?
  U733  32pin KM684000G-7 (SRAM 512Kx8)         ;/
  U725  20pin SN74ALS688N  (8bit inverting identity comparator with enable)
  S700  24pin 12bit DIP switch  (select I/O Address bits A15..A4)
  JP700  8pin Jumper (4x2 pins) (select IRQ15/IRQ12/IRQ11/IRQ10)
  JP7xx 12pin Jumper (3x4 pins) (select DMA7/DMA6/DMA5)
  U64   48pin LVT16245? (dual 8-bit 3-state noninverting bus transceiver)
  U65   48pin LVT16244? (quad 4-bit 3-state noninverting buffer/line driver)
  U66   48pin LVT16244? (quad 4-bit 3-state noninverting buffer/line driver)
  U737  48pin LVT16244? (quad 4-bit 3-state noninverting buffer/line driver)
  U710  20pin SN74ALS244BN (dual 4-bit 3-state noninverting buffer/line driver)
  U709  20pin HD74HC245P   (8bit tristate noninverting bus transceiver)
  U723  14pin SN74ALS38AN (quad open-collector NAND gates with buffered output)
  U2    14pin SN74LS19AN  (hex inverters with schmitt-trigger)
  U1     8pin Dallas DS1232 (MicroMonitor Chip) ;power-good-detect ?
  U708  20pin HD74HC245P   (8bit tristate noninverting bus transceiver)
  X3     2pin 4.1900 (4.19MHz for SPC700 CPU)
  U42   80pin P823, U01Q (Sony CXP82300 SPC700 CPU with piggyback EPROM socket)
  U42'  32pin 27C256A-15 (EPROM 32Kx8) (sticker: "94/11/28")
  U706  10pin some slim chip with 1x10 pins
  BT700  2pin battery (or super-cap?) for DS1302S (?) (not installed)
  U729?  5pin voltage stuff?
  U40    8pin Dallas DS1302S (real time clock)
  X4     2pin small crystal (32.768kHz for DS1302S)
  JP702 34pin Black connector (maybe for internal CDROM Emulator ISA cart?)
  U736  28pin Sony CXK58257ASP-70L (SRAM 32Kx8)         ;CDROM Sector Buffer?
  U735 100pin Sony CXD1199BQ    ;CDROM Decoder/FIFO
  JP715 40pin Blue connector... to external DTL-H2010 CDROM drive?
  JP721  9pin rear connector: Joypad/Memcard 2 (DB9)
  JP719  9pin rear connector: Joypad/Memcard 1 (DB9)
  ?      -    rear hole for cdrom-cable to Blue 40pin connector?
  J70x  98pin ISA Bus Cart-edge (2x31 basic pins, plus 2x18 extended pins)
```
JP715 must be either connected to an external CDROM drive, or to some of
"terminator" plug (which shortcuts Pin23 and Pin26 with each other; software
may hang upon certain I/O operations without that terminator).<br/>

#### Sony DTL-H2500 Dev board (PCI bus)
Newer revision of the DTL-H2000 board. Consists of a single PCI card (plus tiny
daughterboard with Controller ports).<br/>
```
  Mainboard     "PI-27 1-589-867-11, DTL-H2500, MAIN BOARD 1575E01A0, SONY"
  Daughterboard "SONY,CN-102 1-589-865-11,CONNECTOR BOARD,DTL-H2500,1575E02A0"
  CJ1      9pin rear connector: DB9
  CJ2?    15pin rear connector: AV Multi-out   (5+5+5pin)
  CJ3     10pin gray connector (to controller daughterboard with two DB9's)
  CJ4     34pin black connector (maybe for internal CDROM Emulator ISA cart?)
  CJ5     50pin black connector (to DTL-H2510, Gray Internal CDROM Drive?)
  CJ6     68pin black connector (maybe equivalent to 68pin PSX expansion port?)
  -      124pin PCI bus cart edge connector
  CJ1'     9pin rear connector: DB9 (CTR1, joypad 1)     ;\
  CJ2'     9pin rear connector: DB9 (CTR2, joypad 2)     ; on daughterboard
  CJ3'    10pin gray ribbon cable (to CJ3 on main board) ;/
  IC103  208pin Sony CXD8530CQ (CPU)
  IC106   28pin SEC KM48V2104AT-6 (DRAM 2Mx8)
  IC107   28pin SEC KM48V2104AT-6 (DRAM 2Mx8)
  IC108   28pin SEC KM48V2104AT-6 (DRAM 2Mx8)
  IC109   28pin SEC KM48V2104AT-6 (DRAM 2Mx8)
  IC201   64pin SEC KM4216V256G-60 (DRAM 256Kx16) ;dual-ported VRAM
  IC202   64pin SEC KM4216V256G-60 (DRAM 256Kx16) ;dual-ported VRAM
  IC203  160pin Sony CXD8514Q     ;GPU'a
  IC207   64pin Sony CXD2923AR    ;GPU'b
  IC303   28pin HM62W256LFP-7T (CDROM SRAM 32Kx8)               ;on back side
  IC304   52pin "D 2021, SC430920PB, G64C 185, JSAA9618A" (Sub-CPU)  ;on back
  IC305  100pin Sony CXD1199BQ (CDROM Decoder/FIFO)             ;on back side
  IC308  100pin Sony CXD2922BQ (SPU)                            ;on back side
  IC310   44pin SEC KM416V256BLT-7 (DRAM 256Kx16)  ;SoundRAM    ;on back side
  IC402   24pin something bigger
  IC404    8pin something small
  IC405    8pin something small
  IC501   24pin Sony CXA1645M (Analog RGB to Composite)         ;on back side
  IC701    4pin "RD, 5B" or so                                  ;on back side
  IC801  +++pin "ALTERA, FLEX, EPF8820ARC208-3, A9607"
  IC802   20pin LVT245A <--                                     ;on back side
  IC803   52pin "IDT71321, LA35J, S9704P" (2Kx8 dual port SRAM)
  IC804   20pin LVT244A
  IC805    8pin something with socket (sticker: "PD3")
  IC807-2 32pin MX 27C1000MC-90 (PROM)   ;\on back side
  IC808   32pin F 29F040A-90    (FLASH)  ;/BIOS on these chip(s) or so?
  IC901    4pin 37, 69      ;\on back side
  IC902    4pin 37, 69      ;/
  ICxxx?  28pin "DALLAS, DS1230Y-100, NONVOLATILE SRAM"
  U28     20pin LVT244A
  Z1      20pin LVT244A     ;\on back side
  Z2      20pin LVT245A <-- ;/
  Z3      20pin LVT244A
  Z4      20pin LVT244A     ;\
  Z5      20pin LVT245A <-- ; on back side
  Z6      20pin LVT244A     ;/
  Z7      20pin LVT244A
  Z8      20pin LVT244A
  Z9      20pin LVT244A
  X101     4pin RC67.73, JVC 5L (67.7376MHz oscillator for main cpu)
  X201     4pin JC53.20, JVC 6A (for GPU, PAL)
  X202     4pin JC53.69, JVC 6A (for GPU, NTSC)
  X302     3pin 4.000MHz (for sub-cpu)
```

#### Sony DTL-H2700 Dev board (ISA bus) (CPU, ANALYZER ...?)
Another revision of the DTL-H2000/DTL-H2500 boards. Consists of a single ISA
card stacked together with two huge daughterboards, and probably additionally
having a small connector daughterboard. Exact chipset is unknown (there might
be components on both sides of the PCBs, most of them not visible due to the
PCB stacking, so taking photos/scans of the PCBs would require advanced
techniques with screwdrivers).<br/>
Currently the only known chip name is an EPROM (MX 27C1000DC-90, with sticker
"Title=DTL-H2700, Ver=1.00, Date=96.12.4, Sum=046B No."). The ISA card is
having markings: "SONY HCD MWB-7? MADE IN JAPAN, PA47 1-589-003-01 1642E03A0".<br/>
One uncommon feature is an extra connector for a "trigger switch" (foot pedal),
which is reportedly used for activating performance analyzer logging.<br/>

#### Sony DTL-H201A / DT-HV - Graphic Artist Board (IBM PC/ATs to NTSC video)
```
  X2     xpin TXC-2 OSC 66.000MHz
  X1     xpin TXC-2AOSC 53.693MHz
  U16   14pin 74F74 (dual flipflop)
  U29   14pin 74AS04 (hex inverters)
  U14   20pin LVT244 (dual 4-bit 3-state noninverting buffer/line driver)
  U18   20pin LVT244 (dual 4-bit 3-state noninverting buffer/line driver)
  U15   20pin ACT244 (dual 4-bit 3-state noninverting buffer/line driver)
  U11   84pin Altera EPM7096LC84-12 (sticker: "artpc13" or "ARTPC13")
  U13  160pin Sony CXD8514Q     ;GPU'a
  U5    14pin ALS38A   ? (quad open-collector NAND gates with buffered output)
  U27   20pin ALS244AJ ? (dual 4bit tristate noninverting buffer/line driver)
  Q1     3pin T B596
  U23   64pin KM4216V256G-60 (DRAM 256Kx16) ;dual-ported VRAM
  U22   64pin KM4216V256G-60 (DRAM 256Kx16) ;dual-ported VRAM
  U28   64pin Sony CXD2923AR    ;GPU'b
  S1    16pin 8bit DIP switch (select I/O address A15..A8)
  S2     8pin 4bit DIP switch (select I/O address A7..A4)
  U1    20pin SN74ALS688N (8bit inverting identity comparator with enable)
  U2    20pin SN74ALS688N (8bit inverting identity comparator with enable)
  U3    20pin ALS245A (8bit tristate noninverting bus transceiver)
  JP9   12pin Jumper (6x2 pins) (select IRQ15/IRQ11/IRQ10/IRQ9/IRQ5/IRQ3)
  U26   24pin Sony CXA1145M ?  ;RGB?
  JP10   3pin Jumper   ;\
  JP12   3pin Jumper   ; select "S" or "O" (?)
  JP11   3pin Jumper   ;/
  J3    2pin? Yellow connector (composite video out?)
  J2?    pin? Mini DIN? connector (maybe S-video out?)
  J1    15pin High Density SubD (maybe video multi out?)
  CJx   98pin ISA Bus Cart-edge (2x31 basic pins, plus 2x18 extended pins)
```

#### DTL-S2020 aka Psy-Q CD Emu
```
  Yellow PCB "CD Emulator System, (C) Cirtech & SN Systems Ldt, 1994 v1.2"
  IC    24pin GAL20V8B
  IC    68pin Analog Devices ADSP-2101 (16bit DSP Microprocessor)
  IC    20pin HD74HC244P
  IC15  20pin HD74HC244P
  IC14  20pin CD74HCT245E
  IC7   28pin 27C512-10     (EPROM 64Kx8) (yellow sticker, without text)
  IC    28pin HY62256ALP-70 (SRAM 32Kx8)
  IC12  28pin HY62256ALP-70 (SRAM 32Kx8)
  IC    28pin HY62256ALP-70 (SRAM 32Kx8)
  IC13  84pin Emulex/QLogic FAS216 (Fast Architecture SCSI Processor)
  IC5   84pin Emulex/QLogic FAS216 (Fast Architecture SCSI Processor)
  IC4   24pin GAL20V8B (near IO Addr jumpers)
  IC    20pin 74LS244B1   (near lower 8bit of ISA databus)
  IC    20pin SN74LS245N? (near lower 8bit of ISA databus)
  IC    20pin SN74LS245N  (near upper 8bit of ISA databus)
  DMA   12pin Jumpers (select DMA7/6/5)
  IRQ   12pin Jumpers (select IRQ15/12/11/10/7/5)
  IO    16pin Jumpers (select IO Addr 300/308/310/318/380/388/390/398)
  SCSI   6pin Jumpers (select SCSI ID 4/2/1) (aka 3bit 0..7 ?)
  PL3   34pin Connector to DTL-H2000 ?
  PL1   50pin Connector to INTERNAL SCSI hardware ?
  PL2  50pin? Connector to EXTERNAL SCSI hardware ? (25pin plug/50pin cable?)
  Jx    98pin ISA Bus Cart-edge (2x31 basic pins, plus 2x18 extended pins)
```
Note: There's also a similar ISA cart (DTL-S510B) with less chips and less
connectors.<br/>
Note: The SN Systems carts seem to have been distributed by Sony (with
"DTL-Sxxxx" numbers), and also distributed by Psygnosis. The external SCSI
connectors can be possibly also used with Psy-Q Development Systems for SNES
and Sega Saturn?<br/>

#### PSY-Q Development System (Psygnosis 1994)
```
  32pin GM76C8128ALLFW85 (SRAM 128Kx8)
  44pin ALTERA EPM7032LC44-15T
  34pin EMULEX FAS101 (SCSI Interface Processor)
  28pin 27C64 (EPROM 8Kx8) (green sticker, without text)
  20pin LCX245 (=74245?)
   8pin 2112, CPA, H9527 (?)
   3pin transistor? voltage regulator?
  20pin DIP socket (containing two 10pin resistor networks)
  20pin DIP socket (containing two 10pin resistor networks)
   2pin CR2032 Battery 3V
  68pin Connector to PSX "Parallel I/O" expansion port
  25pin Connector to SCSI hardware (to DTL-S510B or DTL-S2020 ISA cart or so?)
```

#### Sony DTL-H800 Sound Artist Board (with optical fibre audio out)
```
  U15  24pin ?
  U5   28pin 27C256 (EPROM 32Kx8) (not installed)
  U7    4pin 67.7376MHz oscillator
  U8   14pin ?
  U11  44pin SEC KM416V256B1-8 (DRAM 256Kx16)  ;SoundRAM
                (44pin package with middle 4pin missing, 40pins used)
  U10 100pin Sony CXD2925Q  ;SPU
  U4  160pin Lattice IspLSI 3256 (sticker: "VER3")
  U6  128pin Lattice IspLSI xxxx ?
  U12  48pin ?
  U13  48pin ?
  U3   20pin 74ACT244
  U14   5pin "LM25755, -3.3 P+" ?
  U2   54pin ?
  U1   54pin ?
  U9    ?pin GP1F31T (light transmitting unit for optical fibre cable)
  ?   124pin PCI bus cart edge connector
  ?     8pin internal jumper/connector? (7pin installed, 1pin empty)
```
Note: There's also a similar board (DTL-H700) for MAC/NuBus instead of PCI bus.<br/>

#### Sony COH-2000 (unknown purpose)
```
  U1   14pin SN74ALS388N  ?
  U2   20pin SN74ALS688N (8bit inverting identity comparator with enable)
  U3   20pin SN74ALS688N (8bit inverting identity comparator with enable)
  U4   24pin PALxxx ?
  U5   20pin SN74ALS245AN
  U6   20pin SN74ALS245AN
  U7   20pin SN74ALS244N
  U8   20pin SN74ALS244N
  U9   20pin SN74ALS245AN
  U10  20pin SN74ALS245AN
  U11  20pin SN74ALS244N
  S2   16pin 8bit DIP switch (ISA 15/14/13/12/11/10/9/8) ;I/O address bit15-8
  S1    8pin 4bit DIP switch (ISA 7/6/5/4)               ;I/O address bit7-4
  S3    8pin 4bit DIP switch (BISO? 3/2/1/0)         ;BISO? or BISD? or 8150?
  JPxx  .... several jumpers (unknown purpose)
  Jx    98pin ISA Bus Cart-edge (2x31 basic pins, plus 2x18 extended pins)
  J5    68pin Connector on rear side (unknown purpose)
```
Unknown what COH-2000 was used for. One theory was that it's related to
PSX-based arcade cabinets. The 68pin connector might be also related to the
68pin PSX "Parallel I/O" expansion port.<br/>

#### Sony DTL-H2010 (Black External CDROM Drive for DTL-H2000, CD-R compatible)
External front loading CDROM drive with Eject button. Connects to the blue
40pin connector on DTL-H2000 boards.<br/>
```
  IC101 100pin SONY CXD2515Q (Signal Processor + Servo Amp)   ;\
  IC102 28pin  BA6297AFP                                      ; on mainboard
  ICxx  20pin  SONY CXA1571N (RF Amp) (on tiny daughtboard)   ; (HCMK-81X)
  CN101 21pin connector to DEX2010.SCH board                  ;
  CN10x 12pin connector to KSS-240A (laser pickup)            ;
  S101   2pin pos0 switch or so?                              ;
  M101   2pin spindle motor                                   ;/
  U1    20pin 74ALS244BN                        ;\
  U2    20pin 74ALS244BN                        ;
  U3    20pin 74ALS244BN                        ; on DEX2010.SCH board
  J1     2pin connector to EJECT BUTTON         ;
  J2     5pin connector to LOADING MOTOR        ;
  J3    21pin connector to mainboard            ;
  JP1   40pin external connector to DTL-H2000   ;/
  CN151  5pin connector to DEX2010.SCH board    ;\
  M151   2pin loading motor (eject motor)       ; on CDM 14, CMK PSX board
  S151   2pin OUT SW ;\switches, probably to    ;
  S152   2pin IN SW  ;/sense load/eject status  ;/
  CN1    2pin connector to DEX2010.SCH board    ;\on DTL-H2010(1) board
  SW1    2pin eject button                      ;/
```
The required cable consists of a Yamaichi NFS-40a female connector (blue
connector on DTL-H2000 side), 0.635mm pitch ribbon cable, and 3M Sub-D MDR40
connector (silver connector on DTL-H2010 side). But caution: the odd/even pins
on the cable are somewhat swapped, on DTL-H2000 side the wires should be
ordered 1,2,3,4,..,39,40, but on DTL-H2010 side they should be ordered
2,1,4,3,..,40,39.<br/>

#### Sony DTL-H2510 (Gray Internal CDROM Drive)
This is some sort of a mimmicked front loading PC CDROM drive (consisting of a
tray that contains a normal (top-loading) PSX cdrom drive unit).<br/>
```
  IC309 80pin Sony CXD2510Q (CDROM Signal Processor)
  ICxx   ?pin Unknown if there are further ICs (eg. CXA1782BR should exist?)
  CN1   10pin Connector to daughterboard (with drive unit)
  CN2    4pin Connector to PC power supply (12V/5V and 2xGND)
  CN3   50pin Connector to DTL-H2500 or so? (need "PCS-E50FC" plug?)
```
There is no eject button, unknown if there's some eject motor, or if one
needs to push/pull the drive tray manually.<br/>

#### Sony SCPH-9903 (Gray SCEx-free Playstation)
A rare SCEx-free Playstation that can boot from CDR's without SCEx strings;
maybe intended for beta-testers. Marked "Property of Sony Computer
Entertainment", "U/C".<br/>
