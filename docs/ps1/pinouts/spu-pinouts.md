#   Pinouts - SPU Pinouts
#### IC308 - SONY CXD2922Q (SPU) (on PU-7, EARLY-PU-8 boards)
#### IC308 - SONY CXD2925Q (SPU) (on LATE-PU-8, PU-16, PU-18, PU-20 boards)
```
  1-D0    14-D11  27-A8    40-GND    53-3.5V  66-A15  79-5V    92-LRIA
  2-D1    15-GND  28-3.5V  41-SYSCK  54-GND   67-A14  80-A3    93-DTIA
  3-3.5V  16-D12  29-GND   42-GND    55-D7    68-A13  81-A2    94-BCIB
  4-GND   17-D13  30-A9    43-TEST   56-D6    69-A12  82-A1    95-LRIB
  5-D2    18-D14  31-/SPU  44-TES2   57-D5    70-A11  83-A0    96-DTIB
  6-D3    19-D15  32-/RD   45-D15    58-D4    71-A10  84-/WE0  97-BCKO
  7-D4    20-A1   33-/WR   46-D14    59-D3    72-A9   85-/OE0  98-LRCO
  8-D5    21-A2   34-DACK  47-D13    60-D2    73-A8   86-/WE1  99-DATO
  9-D6    22-A3   35-/IRQ  48-D12    61-D1    74-A7   87-/OE1  100-WCKO
  10-D7   23-A4   36-DREQ  49-D11    62-D0    75-A6   88-GND
  11-D8   24-A5   37-MUTE  50-D10    63-/RAS  76-A5   89-XCK
  12-D9   25-A6   38-/RST  51-D9     64-/CAS  77-A4   90-GND
  13-D10  26-A7   39-NC    52-D8     65-GND   78-GND  91-BCIA
```
Pin 1..36 = MIPS-CPU bus. Pin 45..87 = SPU-RAM bus (A0,A10-A15,/WE1,OE1=NC).
Pin 91..99 = Digital serial audio in/out (A=CDROM, B=EXP, O=OUT).<br/>

#### IC732 - SONY CXD2941R (SPU+CDROM+SPU\_RAM) (on PM-41(2) boards)
```
  1-DA16   23-FILO  45-LOCK  67-FSTO  89-SCSY   111-XCS   133-HD9   155-VSS5
  2-DA15   24-FILI  46-SSTP  68-COUT  90-SCLK   112-XRD   134-HD8   156-HA1
  3-DA14   25-PCO   47-SFDR  69-XDRST 91-SQSO   113-XWR   135-HD7   157-HA0
  4-VDDM0  26-CLTV  48-SRDR  70-DA11  92-SENS   114-HINT  136-HD6   158-VDDM3
  5-DA13   27-AVSSO 49-TFDR  71-DA10  93-DATA   115-XIRQ  137-VDD4  159-XCK
  6-DA12   28-RFAC  50-TRDR  72-DA09  94-XLAT   116-VDDM2 138-HD5   160-DTIB
  7-LRCK   29-BIAS  51-VSSM1 73-DA08  95-CLOK   117-XSCS  139-HD4   161-BCKO
  8-WDCK   30-ASYI  52-FFDA  74-AVSMO 96-XINT   118-XHCS  140-HD3   162-LRCO
  9-VDD0   31-AVDDO 53-FRDA  75-AVDMO 97-A4     119-XHRD  141-HD2   163-DAVDD0
  10-VSS0  32-ASYO  54-MDP   76-DA07  98-A3     120-XHWR  142-VSS4  164-DAREFL
  11-PSSL  33-VC    55-MDS   77-DA06  99-A2     121-DACK  143-HD1   165-AOUTL
  12-ASYE  34-CE    56-VDD2  78-VDDM1 100-A1    122-DREQ  144-HD0   166-DAVSS0
  13-GND   35-CEO   57-VSS2  79-DA05  101-A0    123-XRST  145-VSSM3 167-DAVSS1
  14-C4M   36-CEI   58-MIRR  80-DA04  102-D7    124-VDD3  146-HA9   168-AOUTR
  15-C16M  37-RFDC  59-DFCT  81-DA03  103-D6    125-SYSCK 147-HA8   169-DAREFR
  16-FSOF  38-ADIO  60-AVSM1 82-DA02  104-D5    126-VSS3  148-HA7   170-DAVDD1
  17-XTSL  39-AVDD1 61-AVDM1 83-DA01  105-D4    127-HD15  149-HA6   171-MUTO
  18-VDD1  40-IGEN  62-FOK   84-WFCK  106-VSSM2 128-HD14  150-HA5   172-DATO
  19-GND   41-AVSS1 63-PWMI  85-SCOR  107-D3    129-HD13  151-HA4   173-MTS3
  20-VPCO1 42-TE    64-FSW   86-SBSO  108-D2    130-HD12  152-VDD5  174-MTS2
  21-VPCO2 43-SE    65-MON   87-EXCK  109-D1    131-HD11  153-HA3   175-MTS1
  22-VCTL  44-FE    66-ATSK  88-SQCK  110-D0    132-HD10  154-HA2   176-MTS0
```

#### IC732 - SONY CXD2938Q (SPU+CDROM) (on newer boards) (PM-41 boards)
```
  1-SCLK    27-RFAC  53-TrckR 79-/XINT 105-A0    131-3.5V   157-(tst) 183-A8
  2-GNDed   28-GNDed 54-TrckF 80-SQCK  106-3.5V  132-D9     158-(tst) 184-A7
  3-GNDed   29-CLTV  55-FocuR 81-SQSO  107-A1    133-D8     159-GND   185-A6
  4-SBSO    30-PCO   56-3.5V  82-SENSE 108-A2    134-D7     160-D15   186-A5
  5-WFCK    31-FILI  57-FocuF 83-GND   109-A3    135-D6     161-D0    187-GND
  6-GNDed   32-FILO  58-SledR 84-GND   110-A4    136-D5     162-D14   188-A4
  7-C16M    33-VCTL  59-SledF 85-CD.D7 111-A5    137-3.5V   163-D1    189-A3
  8-3.5V    34-VPC02 60-NC    86-CD.D6 112-3.5V  138-D4     164-D13   190-A2
  9-C4M     35-VPC01 61-GND   87-CD.D5 113-A6    139-D3     165-3.5V  191-A1
  10-GNDed  36-VC    62-NC    88-CD.D4 114-A7    140-D2     166-D2    192-A0
  11-4.3MHz 37-FE    63-GND   89-CD.D3 115-A8    141-D1     167-D12   193-3.5V
  12-12MHz  38-SE    64-(tst) 90-CD.D2 116-A9    142-D0     168-D3    194-NC
  13-V16M   39-TE    65-(tst) 91-CD.D1 117-/IRQ2 143-GND    169-D11   195-(tst)
  14-DOUT   40-CE    66-note  92-CD.D0 118-/IRQ9 144-33MHzS 170-D10   196-GND
  15-LACK   41-CEO   67-note  93-3.5V  119-/RD   145-       171-D4    197-(tst)
  16-WDCK   42-CEI   68-(tst) 94-CD/CS 120-/WR   146-3.48V  172-D9    198-NC
  17-3.5Ved 43-RFDC  69-3.5V  95-CD/WR 121-DMA4  147-ZZ11   173-GND   199-NC
  18-LOCK   44-ADIO  70-(tst) 96-CD/RD 122-GND   148-GND    174-D5    200-NC
  19-GND    45-GND   71-(tst) 97-CD.A0 123-GND   149-GND    175-D8    201-3.5V
  20-MDS    46-IGEN  72-(tst) 98-CD.A1 124-/SPUW 150-ZZ7    176-D6    202-NC
  21-MDP    47-AVD1  73-(tst) 99-CD.A2 125-D15   151-3.48V  177-D7    203-NC
  22-3.5Ved 48-GNDed 74-DATA  100-GND  126-D14   152-/RES   178-/CAS  204-NC
  23-AVDO   49-GNDed 75-XLAT  101-CDA3 127-D13   153-3.5V   179-/WE   205-GND
  24-ASYO   50-GND   76-CLOK  102-CDA4 128-D12   154-ZZ5    180-3.5V  206-(tst)
  25-ASYI   51-GNDed 77-SCOR  103-/CD  129-D11   155-(tst)  181-/OE   207-(tst)
  26-BIAS   52-GNDed 78-GND   104-/SPU 130-D10   156-(tst)  182-/RAS  208-GND
```
Pin 74..102 = SubCPU. Pin 103..144 = MainCPU. Pin 160..192 = Sound RAM Bus.<br/>
Pin 21 and 53..59 = Drive Motor Control (IC722).<br/>
Pin 1..47 are probably mainly CDROM related.<br/>
Pin 39 "TE9" = IC723.Pin16 - CL709, and via 15K to SPU.39<br/>
Pin 66 connects via 4K7 to IC723.Pin19.<br/>
Pin 67 not connected (but there's room for an optional capacitor or resistor)<br/>
The (tst) pins are wired to test points (but not connected to any components)<br/>

#### CXD2938Q SPU Pinout Notes
Pin 74,75,76,119,120 are connected via 22 ohm.<br/>
Pin 103,104 are connected via 100 ohm.<br/>
ZZnn = IC405 Pin nn (analog audio related, L/R/MUTE).<br/>
Pin 103..142 = System Bus (BIOS,CPU). Pin 160..192 = Sound RAM Bus.<br/>
Pin 178 used for both /CASL and /CASH (which are shortcut with each other).<br/>
Pin 146 and 151 are 3.48V (another supply, not 3.5V).<br/>
Pin 147 and 150 are connected via capacitors.<br/>
Pin 195 and 197 testpoints are found below of the pin 206/207 testpoints.<br/>
```
 SPU155 (tst) always low         ;=maybe external audio (serial) this?
 SPU156 (tst) 45kHz  (22us)      ;=probably 44.1kHz (ext audio sample-rate)
 SPU157 (tst) 2777kHz  (0.36us)  ;=probably 64*44.1kHz (ext audio bit-rate)
 SPU158 (tst) always high        ;=maybe external audio (serial) or this?
```
SPU.Pin5 connects to MANY modchips<br/>
SPU.Pin42 connects to ALL modchips<br/>
SPU.Pin42 via capacitor to SPU.Pin41, and via resistor?/diode? to IC723.10<br/>

#### CXD2938Q CDROM clocks
```
  SPU197  (*) 7.35kHz (44.1kHz/6) (stable clock, maybe DESIRED drive speed)
  SPU5    (*) 7.35kHz (44.1kHz/6) (unstable clock, maybe ACTUAL drive speed)
  SPU15   (*) 44.1kHz (44.1kHz*1)
  SPU16   (*) 88.2kHz (44.1kHz*2)
  SPU206  (*) circa 2.27MHz
  SPU70   (*) whatever clock (with SHORT low pulses)
```
(\*) these frequencies are twice as fast in double speed mode.<br/>

#### CXD2938Q CDROM signals
```
  SPU207  fastsignal?
  SPU195  slowsignal?
  SPU18   usually high, low during seek or spinup or so
  SPU44   superslow hi/lo with superfast noise on it
  SPU73   mainly LOW with occasional HIGH levels...
  SPU71   LOW=SPIN_OK, PULSE=SPIN_UP/DOWN_OR_STOPPED
  SPU72   similar as SPU71
  SPU64   LOW=STOP, HI=SPIN
  SPU68   always low...?
  SPU65   whatever?
  SPU75   mainly HIGH, short LOW pulses when changing speed up/down/break
```

#### CXD2938Q CDROM/SPU Testpoints (on PM-41 board)
```
                |                                       | SPU73
                |          CXD2938Q (SPU)               |       SPU72
                |          (on PM-41 board)             | SPU70 SPU71
                |                                       | SPU64 SPU65 SPU68
  SPU206 SPU207 |_______________________________________|
   SPU197
    SPU195                   SPU16                   SPU44
                  SPU18 SPU5 SPU15
                          SPU12
```

#### IC402 - 24pin AKM AK4309VM (or AK4309AVM/AK4310VM) - Serial 2x16bit DAC
```
  1-TST?  4-/PD   7-CKS    10-LRCK  13-NC?    16-AOUTL  19-GNDa  22-VREFH
  2-VCCd  5-/RST  8-BICK   11-NC?   14-NC?    17-VCOM   20-NC?   23-VREFL
  3-GNDd  6-MCLK  9-SDATA  12-NC?   15-AOUTR  18-VCCa   21-NC?   24-DZF?
```
Used only on older boards (eg. PU-8), newer boards seem to have the DAC in the
208pin SPU.<br/>
No 24pin AK4309VM datasheet exists (however it seems to be same as 20pin
AK4309B's, with four extra NC pins at pin10-14).<br/>

#### IC405 - "2174, 1047C, JRC" or "3527, 0A68" (on newer boards)
Called "NJM2174" in service manual. Audio Amplifier with Mute.<br/>
```
  1  GND
  2  NC     ? via 100ohm to multiout pin 9    ;Audio Left (white cinch)
  3  OUT-R  ?
  4  MUTE1      ;specified as LOW = Mute
  5  MUTE2      ;specified as HIGH = Mute
  6  MUTEC      ;unspecified, maybe capacitor, or output based on MUTE1+MUTE2?
  7  IN-R     via capacitor to SPU.150
  8  BIAS
  9  NC
  10 NC
  11 IN-L     via capacitor to SPU.147
  12 OUT-L  ?
  13 NC     ? via 100ohm to multiout pin 11   ;Audio Right (red cinch)
  14 VCC      +5.0V (via L401)
```
Audio amplifier, for raising the signals to 5V levels.<br/>

#### IC405 - "NJM2100E (TE2)" Audio Amplifier (on older PU-8 and PU-22 boards)
```
  1-ROUT
  2-RIN- IC732.SPU.150
  3-RIN+
  4-GND
  5-LIN+
  6-LIN- IC732.SPU.147
  7-LOUT
  8-VCC 4.9V (+5.0V via L401)
```
