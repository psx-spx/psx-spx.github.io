#   Pinouts - VCD Pinouts
SCPH-5903 Video CD PlayStation<br/>

#### VCD Mainboard "PU-16, 1-655-191-11" Component List
The overall design is very close to LATE-PU-8 boards (1-658-467-2x). Changed
components are IC102/IC304 (different kernel and cdrom firmware),
C318/C325/C327 (height reduced capacitors for mounting the daughterboard above
of them). Plus some extra components: Three triple multiplexors (for switching
between PSX and VCD audio/video), and the daughterboard connector.<br/>
```
  IC102 44pin SONY, M538032E-02, JAPAN 6465401 (uncommonly big BIOS, 1Mx8)
  IC304 52pin C 4021 SC430924PB (HC05 sub-cpu, with extra Video CD command 1Fh)
  C318   2pin S5        ;\tantalum capacitors with lower height (instead
  C325   2pin CA7       ; of the electrolytic capacitors on PU-8 boards)
  C327   2pin CA7       ;/
  ICnnn 16pin 4053C (Triple multiplexor, for Audio LRCK,BCLK,DATA) (PCB top)
  ICnnn 16pin 4053C (Triple multiplexor, for Video FSC,CSYNC)      (PCB bottom)
  ICnnn 16pin 2283  (Triple multiplexor, for Video R,G,B)          (PCB bottom)
  CNnnn 30pin Connector to daughterboard                           (PCB top)
```

#### VCD Daughterboard "MP-45, 1-665-192-11" Component List
```
  IC102   3pin  TA78M05F voltage regulator (7.5V to 5V) (Toshiba)
  IC104 120pin  CXD1852AQ Video CD decoder (Sony)
  IC106  40pin  MB814260-70 (256Kx16 DRAM) (Fujitsu) ;see also: IC114
  IC107  20pin  6230FV 649 115 (OSD, similar to BU6257AFV-E2) (PCB back)
  IC109  14pin  Y2932 (TLC2932 PLL) (TI) (for RGB.DAC.CLK)
  IC110  44pin  TDA8771AH Triple Video DAC for RGB (Philips) (PCB back)
  IC111  64pin  CXP10224-603R 732A02E (MCU) (Sony)
  IC112  14pin  HCT32A (74HCT32 Quad OR gate) (TI) (PCB back) (for RGB.DAC.CLK)
  IC113   8pin  H74 7H (single D-type flip-flop; OSD clock divider) (PCB back)
  IC114  40pin  MB814260-70 (256Kx16 DRAM) (Fujitsu) ;see also: IC106
  CN101  30pin  Male Connector (to female 30pin socket on PU-16 mainboard)
  X103    2pin  45.00MHz (for VCD decoder chip)
  X104    4pin  12.000MHz (for MCU chip)
  X105    2pin  28.636MHz (for VCD decoder chip) (8*3.579545 NTSC clock)
```

#### VCD Daughterboard Connector
```
                               .--.---.
                         GND  / 1   2 | GND
    (CXD1815Q.86)    CD.BCLK |  3   4 | CD.LRCK    (CXD1815Q.84)
    (CXD1815Q.87)    CD.C2PO |  5   6 | CD.DATA    (CXD1815Q.85)
                         GND |  7   8 | CD.SQCK    (CXD2510Q.67) CXP.31
         (TDA.44) VIDEO.OUTR |  9  10 | CD.SQSO    (CXD2510Q.66) CXP.29
                         GND | 11  12 | SIO.OUT    (HC05.51.PORTF1 to CXP.47)
         (TDA.40) VIDEO.OUTG | 13  14 | SIO.IN     (HC05.50.PORTF0 from CXP.48)
                         GND | 15  16 | SIO.CLK    (HC05.52.PORTF2 to CXP.49)
         (TDA.36) VIDEO.OUTB | 17  18 | VIDEO.FSC  (CXD1852AQ.95)
                         GND | 19  20 | VIDEO.CSYNC(CXD1852AQ.96)
          (PSU.3)       3.5V | 21  22 | 3.5V       (PSU.3)
          (PSU.1)       7.5V | 23  24 | AUDIO.FSXI (CXD1852AQ.103 to VCD)
          (PSU.7)       /RES | 25  26 | AUDIO.DATA (CXD1852AQ.100)
  (CXD1852AQ.102) AUDIO.BCLK | 27  28 | AUDIO.LRCK (CXD1852AQ.101)
                         GND | 29  30 | GND
                             '--------'
```

#### IC104 "Sony CXD1852AQ" (MPEG-1 Decoder for Video CD) (120 pin)
```
   1-GND   16-HD7   31-GND   46-MD4   61-GND   76-G/Y3  91-GND       106-XTL2O
   2-XTL0O 17-MA3   32-MA7   47-MD11  62-/VOE  77-G/Y4  92-HSYNC     107-XTL2I
   3-XTL0I 18-MA4   33-MA8   48-MD3   63-R/Cr0 78-G/Y5  93-VSYNC     108-VDD
   4-VDD   19-MA2   34-/RAS  49-MD12  64-R/Cr1 79-G/Y6  94-FID/FHREF 109-C2PO
   5-HA2   20-MA5   35-/MWE  50-MD2   65-R/Cr2 80-G/Y7  95-CBLNK/FSC 110-LRCI
   6-HA3   21-MA1   36-/CAS2 51-MD13  66-R/Cr3 81-B/Cb0 96-CSYNC     111-DATI
   7-HD0   22-GND   37-/CAS0 52-MD1   67-R/Cr4 82-B/Cb1 97-/SGRST    112-BCKI
   8-HD1   23-MA6   38-MD7   53-MD14  68-R/Cr5 83-B/Cb2 98-CLK0O     113-DOIN
   9-HD2   24-MA0   39-MD8   54-MD0   69-R/Cr6 84-B/Cb3 99-DOUT      114-/HCS
  10-HD3   25-BC    40-MD6   55-MD15  70-R/Cr7 85-B/Cb4 100-DATO     115-/HDT
  11-HD4   26-TCKI  41-MD9   56-OSDEN 71-G/Y0  86-B/Cb5 101-LRCO     116-HRW
  12-HD5   27-TDI   42-MD5   57-OSDB  72-G/Y1  87-B/Cb6 102-BCKO     117-/HIRQ
  13-HD6   28-TENA1 43-MD10  58-OSDG  73-G/Y2  88-B/Cb7 103-FSXI     118-/RST
  14-VDD   29-TDO   44-VDD   59-OSDR  74-VDD   89-DCLK  104-VDD      119-HA0
  15-GND   30-VST   45-GND   60-VDD   75-GND   90-VDD   105-GND      120-HA1
```
The Hxxx pins are for the Host (the 8bit CXP CPU), the Mxxx for the RAM chips,
the R/G/B pins are 24bit RGB video. Pin36 can be /CAS2 or MA9 (and, the VCD
daughterboard has alternate solderpads for one large RAM instead of two small
RAMs).<br/>

#### IC107 "6230FV" (OSD chip, similar to BU6257AFV-E2) (20 pin)
```
   1-SIO.CLK   5-VDD      9-TEST  13-BLK2   17-OSDG
   2-SIO./CS   6-/CKOUT  10-GND   14-VC2    18-OSDB
   3-SIO.DTA   7-OSCOUT  11-BLK1  15-OSDEN  19-/VSYNC
   4-/RESET    8-OSCIN   12-VC1   16-OSDR   20-/HSYNC
```
SIO pin1/2/3 are wired to CXP pin38/37/36. OSCIN is the RGB DAC CLK divided by
two (from H74 chip pin5). OSD/SYNC on pin15-20 connect to the MPEG1 decoder
chip.<br/>
No datasheet (but pinouts are same/similar as for BU6257AFV, documented in
several service manuals for tape decks with vcd player: HCD-V5500,
HCD-V8900/V8900AV, HCD-V909AV).<br/>

#### IC111 "Sony CXP10224-603R" (8bit SPC700 CPU) (64pin LQFP)
```
   1-PB5=TP    17-PD5=/HCS       33-AVREF=VDD             49-PG5/SCK1=HC05.PF2
   2-PB4=TP    18-PD4=TP         34-AVDD=VDD              50-PG4=/RST.OUT
   3-PB3=HA3   19-PD3=TP         35-PF7/AN7=TP            51-PG3/TO=TP
   4-PB2=HA2   20-PD2=TP         36-PF6/AN6=OSD.DTA       52-PA7=TP
   5-PB1=HA1   21-PD1=TP         37-PF5/AN5=OSD./CS       53-PA6=TP
   6-PB0=HA0   22-PD0=TP         38-PF4/AN4=OSD.CLK       54-PA5=TP
   7-PC7=HD7   23-MP/TEST=GND    39-PF3/AN3=GND           55-PA4=TP
   8-PC6=HD6   24-XTAL=12MHZ     40-PF2/AN2=GND           56-VPP=VDD
   9-PC5=HD5   25-EXTAL=12MHZ    41-PF1/AN1=GND           57-VDD=VDD
  10-PC4=HD4   26-VSS=GND        42-PF0/AN0=10KtoGND      58-VSS=GND
  11-PC3=HD3   27-/RST=/RES      43-PE3/PWM1=TP           59-PA3=TP
  12-PC2=HD2   28-/CS0=VDD       44-PE2/PWM0=TP           60-PA2=TP
  13-PC1=HD1   29-SI0=CD.SQSO    45-PE1/INT2/EC=/VSYNC    61-PA1=TP
  14-PC0=HD0   30-SO0=TP         46-PE0/INT0=/HIRQ        62-PA0=TP
  15-PD7=HRW   31-/SCK0=CD.SQCK  47-PG7/SI1/INT1=HC05.PF1 63-PB7=TP
  16-PD6=/HDT  32-AVSS=GND       48-PG6/SO1=HC05.PF0      64-PB6=TP
```
Pin 3-15,45,46,50 connect to MPEG1 decoder. Pin 36-38 to OSD. Pin 47-49 to
HC05.PortF. Pin 27 is /RESET from PSU. Pin 29,31 are SUBQ from CXD2510Q. The
"TP" pins connect to test points (but seem to be NC otherwise).<br/>
Pinouts are same as in CXP811P24 datasheet (which uses SPC700 instruction set;
that instruction set is also used by SNES sound CPU).<br/>

#### IC109 "TLC2932" (PLL) (14pin)
```
  1-LOGIC_VDD=5V            5-FIN-B=HSYNC.PLL 9-PFD_INHIBIT=GND  13-BIAS
  2-SELECT=5V               6-PFD_OUT         10-VCO_INHIBIT=GND 14-VCO_VDD=5V
  3-VCO_OUT=RGB.DAC.CLK.PLL 7-LOGIC_GND=GND   11-VCO_GND=GND
  4-FIN-A=FID/FHREF.PLL     8-NC              12-VCO_IN
```
Used to generate the CLK for the TDA chip (that is, the dotclk, paused during
VSYNC, or so?). The same CLK, divided by two, is also used as OSD.OSCIN.<br/>

#### IC112 "74HCT32" (Quad OR gate) (14pin)
```
   1-FID/FHREF.MPEG  4-HSYNC.MPEG   8-(low)  11-RGB.DAC.CLK.TDA  7-GND
   2-FID/FHREF.MPEG  5-HSYNC.MPEG   9-GNDed  12-RGB.DAC.CLK.PLL  14-VCC/5V
   3-FID/FHREF.PLL   6-HSYNC.PLL   10-GNDed  13-RGB.DAC.CLK.PLL
```
Used to sharpen the output from the PLL chip, and to level-shift signals for
the two PLL inputs from 3.5V to 5V. The input-pairs for the OR gates are
shortcut with each other, so the chip isn't actually ORing anything.<br/>

#### IC113 "H74 7H" (single D-type flip-flop; OSD clock divider) (8 pin)
```
  1-CLK   2-D   3-/Q   4-GND   5-Q   6-/RES   7-/SET   8-VCC
```
Used to divide the RGB DAC CLK by two. CLK comes from TDA.pin31, D and /Q are
shortcut with each other, /RES and /SET are wired to VDD, and Q goes to
OSD.OSCIN.<br/>

#### ICnnn "4053C" (Triple multiplexor, for Audio LRCK,BCLK,DATA) (16pin)
```
  1-IN2B=DATA.VCD   5-IN3A=LRCK.SPU    9-SEL3=LRCK.SEL   13-IN1B=BCLK.VCD
  2-IN2A=DATA.SPU   6-/OE=GNDed       10-SEL2=DATA.SEL   14-OUT1=BCLK.OUT
  3-IN3B=LRCK.VCD   7-VEE=GNDed       11-SEL1=BCLK.SEL   15-OUT2=DATA.OUT
  4-OUT3=LRCK.OUT   8-GND=GND         12-IN1A=BCLK.SPU   16-VDD=VDD/3.5V
```
The three SEL pins are wired to HC05.PortF3, the three SPU pins are wired via
10Kohm.<br/>

#### ICnnn "4053C" (Triple multiplexor, for Video FSC,CSYNC) (16pin)
```
  1-IN2B=FSC.VCD    5-IN3A=CSYNC.PSX   9-SEL3=CSYNC.SEL  13-IN1B=GNDed
  2-IN2A=FSC.PSX    6-/OE=GNDed       10-SEL2=FSC.SEL    14-OUT1=NCed
  3-IN3B=CSYNC.VCD  7-VEE=GNDed       11-SEL1=DUMMY.SEL  15-OUT2=FSC.OUT
  4-OUT3=CSYNC.OUT  8-GND=GND         12-IN1A=GNDed      16-VDD=VCC/5V
```
The three SEL pins are wired to HC05.PortF3, the two OUTx pins are wired via
2.2Kohm.<br/>

#### ICnnn "NJM2283" (Triple multiplexor, for Video R,G,B) (16pin)
```
  1-IN1B=R.VCD      5-OUT2=G.OUT       9-IN3B=B.VCD      13-V=VCC/5V
  2-SEL1=R.SEL      6-OUT3=B.OUT      10-GND3=81ohm/GND  14-IN2B=G.VCD
  3-OUT1=R.OUT      7-SEL3=B.SEL      11-IN2A=G.PSX      15-GND1=GND
  4-GND2=GND        8-IN3A=B.PSX      12-SEL2=G.SEL      16-IN1A=R.PSX
```
The three SEL pins are wired to HC05.PortF3, the six INxx pins wired through
resistors and capacitors, the three OUTx pins are wired through capacitors.<br/>
