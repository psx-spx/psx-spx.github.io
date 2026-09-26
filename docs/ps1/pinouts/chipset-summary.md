#   Pinouts - Chipset Summary
#### PSX/PSone Mainboards
```
  Board    Expl.
  PU-7     PSX, with AV multiout+cinch+svideo, GPU in two chips (160+64pins)
  PU-8     PSX, with AV multiout+cinch, four 8bit Main RAM chips
            EARLY-PU-8: "PU-8 1-658-467-11, N4" --> old chipset, resembles PU-7
            LATE-PU-8:  "PU-8 1-658-467-22, N6" --> new chipset, other as PU-7
  PU-9     PSX, without SCPH-number (just sticker saying "NOT FOR SALE, SONY)
  PU-16    PSX, with extra Video CD daughterboard (for SCPH-5903)
  PU-18    PSX, with AV multiout only, single 32bit Main RAM (instead 4x8bit)
  PU-20    PSX, unknown if/how it differs from PU-18
  PU-22    PSX, unknown if/how it differs from PU-18
  PU-23    PSX, with serial port, but without expansion port
  PM-41    PSone, older PSone, for GPU/SPU with RAM on-board (see revisions)
  PM-41(2) PSone, newer PSone, for GPU/SPU with RAM on-chip
```
There are at least two revisions of the "PM-41" board:<br/>
```
  PM-41, 1-679-335-21  PSone with incomplete RGB signals on multiout port
  PM-41, 1-679-335-51  PSone with complete RGB signals on multiout port
```
The "incomplete" board reportedly requires to solder one wire to the multiout
port to make it fully functional... though no idea which wire... looks like the
+5V supply? Also, the capacitors near multiout are arranged slightly
differently.<br/>
The PM-41 board absorbed its external RAM across sub-revisions: -11..-51 use an
external VRAM chip + external SPU-RAM chip (CXD8561 GPU + CXD2938Q SPU/CDROM);
-61 switches to the CXD9500Q GPU with on-chip VRAM (but keeps the external
SPU-RAM + CXD2938Q); only -71 ("PM-41(2)") adds the CXD2941R with on-chip
SPU-RAM. So GPU-RAM was integrated one sub-revision before SPU-RAM.<br/>

#### CPU chips
```
  IC103 - 208pin - "SONY CXD8530BQ"  ;seen on PU-7 board
  IC103 - 208pin - "SONY CXD8530CQ"  ;seen on PU-7 and PU-8 boards
  IC103 - 208pin - "SONY CXD8606Q"   ;seen in PU-18 schematic
  IC103 - 208pin - "SONY CXD8606AQ"  ;seen on PU-xx? board
  IC103 - 208pin - "SONY CXD8606BQ"  ;seen on PM-41, PU-23, PU-20 boards
  IC103 - 208pin - "SONY CXD8606CQ"  ;seen on PM-41 board, too
```
These chips contain the MIPS CPU, COP0, and COP2 (aka GTE), MDEC and DMA.<br/>

#### GPU chips - Graphics Processing Unit
```
  IC203 - 160pin - "SONY CXD8514Q"   ;seen on PU-7 and EARLY-PU-8 boards
  IC203 - 208pin - "SONY CXD8561Q"   ;seen on LATE-PU-8 board
  IC203 - 208pin - "SONY CXD8561BQ"  ;seen on PU-18, PU-20 boards
  IC203 - 208pin - "SONY CXD8561CQ"  ;seen on PM-41 board
  IC203 - 208pin - "SONY CXD9500Q"   ;with on-chip RAM ;PM-41 -61 and PM-41(2) -71 boards
  IC21  - 208pin - "SONY CXD8538Q"   ;seen on GP-11 (namco System 11) boards
  IC103 - 208pin - "SONY CXD8654Q"   ;seen on GP-15 (namco System 12) boards
```

#### SPU chips - Sound Processing Unit
```
  IC308 - 100pin - "SONY CXD2922Q" (SPU)               ;PU-7 and EARLY-PU-8
  IC308 - 100pin - "SONY CXD2922BQ"(SPU)               ;EARLY-PU-8
  IC308 - 100pin - "SONY CXD2925Q" (SPU)               ;LATE-PU-8, PU-18, PU-20
  IC732 - 208pin - "SONY CXD2938Q" (SPU+CDROM)         ;PU-23 (PSX), PSone/PM-41 -11..-61
  IC732 - 176pin - "SONY CXD2941R" (SPU+CDROM+SPU_RAM) ;PSone/PM-41(2) (-71) Board
  IC402 - 24pin  - "AKM AK4309VM"  (Serial 2x16bit DAC);older boards only
  IC405 - 8pin   - "NJM2100E (TE2)" Audio Amplifier    ;PU-8 and PU-22 boards
  IC405 - 14pin  - "NJM2174" Audio Amplifier with Mute ;later boards
  IC405 - 14pin  - "NJM2790V (TE2)" Audio Amplifier    ;PM-41(2) (-71) board only
```

#### IC106 CPU-RAM / Main RAM chips
```
  IC106/IC107/IC108/IC109 - NEC 424805AL-A60 (28pin, 512Kx8) (PU-8 board)
  IC106 - "Samsung K4Q153212M-JC60" (70pin, 512Kx32) (newer boards)
  IC106 - "Toshiba T7X16 (70pin, 512Kx32) (newer boards, too)  ;PU-23 (SCPH-9000)
  IC106 - "Toshiba TC51V18325BJ-60S" (2MB) (PM-41 / PSone)
```

#### GPU-RAM / Video RAM chips
```
  IC201 - 64pin NEC uPD482445LGW-A70-S ;VRAM  ;\on PU-7 and EARLY-PU-8 board
  IC202 - 64pin NEC uPD482445LGW-A70-S ;VRAM  ;/split into 2 chips !
  IC201 - 64pin SEC KM4216Y256G-60     ;VRAM  ;\on other PU-7 board
  IC202 - 64pin SEC KM4216Y256G-60     ;VRAM  ;/split into 2 chips !
  IC201 - 100pin - Samsung KM4132G271BQ-10 (128Kx32x2)  ;-on later boards
  IC201 - 100pin - Samsung K4G163222A-PC70 (256Kx32x2)  ;-on PM-41
```
Note: The older 64pin VRAM chips are special dual-ported DRAM, the newer 100pin
VRAM chips are just regular DRAM.<br/>
Note: The PM-41 board uses a 2MB VRAM chip (but allows to access only 1MB)<br/>
Note: The CXD9500Q GPU has on-chip RAM (no external VRAM); used from PM-41 -61 onwards (incl. PM-41(2) -71).<br/>

#### IC310 - SPU-RAM - Sound RAM chips
```
  IC310 - 40pin - "TOSHIBA TC51V4260DJ-70"  ;seen on PU-8 board
  IC310 - 40pin - EliteMT M11B416256A-35J (256K x 16bit)
  IC310 - "Fujitsu MB814260-70PJER" (256Kx16) ;PU-23, PM-41 (-11..-61)
  IC310 - "NN514267 ATT-50" (256Kx16)         ;PU-23 (PU23-11/-21/-31/-51)
```
Note: The PM-41(2) board has on-chip RAM in the SPU (no external memory chip)<br/>

#### BIOS ROM
```
  IC102 - 40pin - "SONY ..."          ;seen on PU-7 & early-PU-8 board (40pin!)
  IC102 - 44pin - "SONY M538032E-02"  ;seen on PU-16 (video CD, 1Mbyte BIOS)
  IC102 - 32pin - "SONY M534031C-25"  ;seen on later-PU-8 board
  IC102 - 32pin - "SONY 2022"         ;seen on PU-8 (1-658-467-23)
  IC102 - 32pin - "SONY 2030"         ;seen on PU-18 board
  IC102 - 32pin - "SONY M534031E-47"  ;seen on PM-41 board and PM-41(2)
  IC102 - 32pin - "SONY M27V401D-41"  ;seen on PM-41 board, too
  IC102 - 32pin - "OKI MSM534031E-07GS / -10GS" ;PU-23 (SCPH-9000)
  IC102 - 32pin - "Samsung KM23V4000DG-15"      ;PU-23 alternate source (SCPH-9000)
  IC102 - 32pin - "OKI MSM534031E-45/46/47GS"   ;PM-41 by model: 45=SCPH-100(JP), 46=101/103(US/Asia), 47=102(PAL)
```

#### Oscillators and Clock Multiplier/Divider
```
  X101 - 4pin - "67.737" (NTSC, presumably)         ;PU-7 .. PU-20
  X201 - 2pin - "17.734" (PAL) or "14.318" (NTSC)   ;PU-22 .. PM-41(2)
  IC204 - 8pin - "CY2081SL-500T" (NTSC) or "CY2081SL-509T" (PAL, marked "2294A") ;PU-22 .. PM-41(2)
```

#### Voltage Converter (for +7.5V to +5.0V conversion)
```
  IC601 - 3pin - "78M05" or "78005"  ;used in PSone
  IC601 - "Toshiba TA78M05F (TE16L)" (PU-23) or "MC78M05CDTRK" (PM-41) ;+5V regulator
```

#### Pulse-Width-Modulation Power-Control Chip
```
  IC606 16pin/10mm "TL594CD" (alternately to IC607) ;seen on PM-41 board
  IC607 16pin/5mm  "T594"    (alternately to IC606) ;seen on PM-41 board, too
  IC606/607/608 - PM-41 rev-dependent: "BA00AS" (-11), "TL594CD-R2" (-21), "TL594CPWR" (-31..-71), "MM1562FFBE" (-61/-71)
```
The PM-41 board has locations for both IC606 and IC607, some boards have the
bigger IC606 (10mm) installed, others the smaller IC607 (5mm), both chips have
exactly the same pinouts, the only difference is the size.<br/>

#### Reset Generator
```
  IC002 - 8pin - <not installed> (would be alternately to IC003) ;\on PSone
  IC003 - 5pin - <usually installed>                             ;/
  IC101 - 5pin - M51957B (Reset Generator) (on PSX-power supply boards)
  IC002/IC003 - "M51957BFP-600D" (reset/voltage detector) ;PM-41 (-11/-21)
  IC002/IC003 - "RN5VD13AA-TL"   (voltage detector)       ;PM-41 (-31..-71), replaces M51957B
```

#### CDROM Chips
```
  U42   80pin    SUB-CPU (CXP82300) with piggyback EPROM ;DTL-H2000
  IC304 80pin    SUB-CPU (MC68HC05L16) 80pin package     ;PU-7 and EARLY-PU-8
  IC304 52pin    SUB-CPU (MC68HC05G6) 52pin package      ;LATE-PU-8 and up
  IC305 - 100pin SONY CXD1199BQ (Decoder/FIFO)           ;PU-7
  IC305 - 100pin SONY CXD1815Q  (Decoder/FIFO)           ;PU-8, PU-18
  IC309 - 100pin SONY CXD2516Q  (Signal Processor)       ;PU-7 (100pin!)
  IC309 - 80pin  SONY CXD2510Q  (Signal Processor)       ;PU-8 and DTL-H2510
  IC702 - 48pin  SONY CXA1782BR (Servo Amplifier)        ;PU-7, PU-8
  IC101 - 100pin SONY CXD2515Q  (=CXD2510Q+CXA1782BR)    ;DTL-H2010
  IC701 - 100pin SONY CXD2545Q  (=CXD2510Q+CXA1782BR)    ;PU-18
  IC720 - 144pin SONY CXD1817R  (=CXD2545Q+CXD1815Q)     ;PU-20
  IC102 - 28pin - "BA6297AFP"           ;seen on DTL-H2010 drives
  IC704 - 28pin - "BA6398FP"            ;seen on PU-7
  IC722 - 28pin - "BA6397FP"            ;seen on late PU-8
  IC722 - 28pin - "BA5947FP"            ;seen on PM-41 and various boards
  IC722 - 28pin - "Panasonic AN8732SB"  ;seen on PM-41 board
  IC722 - 28pin - "Rohm BA5977FP-E2"    ;seen on PU-23 (SCPH-9000)
  IC722 - 28pin - "Rohm BA5947FP-E2"    ;seen on PM-41 (SCPH-100, confirms BA5947FP above)
  ICxxx - 20pin  SONY CXA1571N    (RF Amplifier) (on DTL-H2010 drives)
  IC703 - 20pin  SONY CXA1791N    (RF Amplifier) (on PU-18 boards)
  IC723 - 20pin  SONY CXA2575N-T4 (RF Matrix Amplifier) (on PU-22 .. PM-41(2))
```
Note: The SUB-CPU contains an on-chip BIOS (which does exist in at least seven
versions, plus US/JP/PAL-region variants, plus region-free debug variants).<br/>
Known IC304 (MC68HC05G6) mask-ROM part numbers by region (...2=JP/Asia, ...3=PAL, ...4=US):<br/>
```
  SC430942PB ;SCPH-9000/9003 (PU-23), SCPH-100/103 (PM-41 -11..-61)
  SC430943PB ;SCPH-9002 (PU-23, PAL), SCPH-102 (PM-41, PAL)
  SC430944PB ;SCPH-9001 (PU-23, US),  SCPH-101 (PM-41, US)
  SC430947PB ;SCPH-100/103 (PM-41(2) -71) ;new rev for CXD2941R
  SC430948PB ;SCPH-102     (PM-41(2) -71, PAL)
  SC430949PB ;SCPH-101     (PM-41(2) -71, US)
```

#### RGB Chips
```
  IC207 64pin "SONY CXD2923AR" VRAM Data to Analog RGB         ;\oldest
  IC501 24pin "SONY CXA1645M" Analog RGB to Composite          ;/
  IC202 44pin "Philips TDA8771H" Digital RGB to Analog RGB     ;\old boards
  IC202 44pin "Motorola MC141685FT" Digital RGB to Analog RGB  ;/
  IC?   48pin "H7240AKV" 24bit RGB to Analog+Composite         ;-SCPH-7001?
  IC502 48pin "SONY CXA2106R-T4" 24bit RGB to Analog+Composite ;-newer boards
```

#### MISC
```
  CDROM Drive: "KSM-440BAM" ;seen used with PM-41 board
  IC602 5pin "National LP2985IM5X-3.5" (3.5V LDO; top-marked "L/\1B" or "3DR") ;PU-23, PM-41 (-11..-61)
```

#### Controller/Memory Card Chips
```
  U?  24pin "9625H, CFS8121"     ;SCPH-1080, digital pad (alternate?)
  U?   ?pin "SC438001"           ;SCPH-1080, digital pad (alternate?)
  U?  32pin "(M), SC401800"      ;SCPH-1080, digital pad
  U?  32pin "(M), SC442116"      ;SCPH-xxxx, mouse
  IC? 64pin "SONY CXD103, -166Q" ;SCPH-1070, multitap
  U1  42pin "SD657, 9702K3006"   ;SCPH-1150, analog pad, single motor
  U1  42pin "SD657, 9726K3002"   ;SCPH-1180, analog pad, without motor
  U1  44pin "SONY CXD8771Q"      ;SCPH-1200, analog pad, two motors (PSX)
  U1  44pin "SD707, 039 107"     ;SCPH-110,  analog pad, two motors (PSone)
  U1  44pin "SD787A"             ;SCPH-xxx,  analog pad, two motors (PS2?)
  U?  64pin "SONY CXD8732AQ"     ;SCPH-1020, memory card, on-chip FLASH
  U?  XXpin other chips          ;SCPH-xxxx, memory card, external FLASH
  U1  44pin "NAMCO103P"          ;NPC-103, namco lightgun
```
