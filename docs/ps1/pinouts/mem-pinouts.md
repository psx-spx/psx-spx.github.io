#   Pinouts - MEM Pinouts
#### IC102 - BIOS ROM (32pin, 512Kx8, used on LATE-PU-8 boards, and newer boards)
```
  1-A19  5-A7  9-A3   13-D0   17-D3  21-D7   25-A11  29-A14
  2-A16  6-A6  10-A2  14-D1   18-D4  22-/CE  26-A9   30-A17     ;/CE=/BIOS
  3-A15  7-A5  11-A1  15-D2   19-D5  23-A10  27-A8   31-A18
  4-A12  8-A4  12-A0  16-GND  20-D6  24-/OE  28-A13  32-3.5V    ;/OE=/RD
```
Uses standard EPROM pinouts, VCC is 3.5V though, when replacing the ROM by an
EPROM, it may be required to replace the supply by 5V. Note that, on PM-41
boards at least, Pin 1 is connected to A19 (allowing to install a 1MB BIOS chip
on that board, however, normally, a 512KB BIOS chip is installed, and, the CPU
is generating an exception when trying to access more than 512KB, but that 512K
limit can be disabled via memory control registers).<br/>
Datasheet for (MS-)M534031E does exist.<br/>

#### IC102 - BIOS ROM (40pin, 512Kx8, used on PU-7 boards, and EARLY-PU-8 boards)
```
  1-A18  6-A4   11-GND   16-D9   21-VCC  26-D6      31-GND(/BYTE) 36-A13
  2-A8   7-A3   12-/OE   17-D2   22-D4   27-D14     32-A17        37-A12
  3-A7   8-A2   13-D0    18-D10  23-D12  28-D7      33-A16        38-A11
  4-A6   9-A1   14-D8    19-D3   24-D5   29-A0(D15) 34-A15        39-A10
  5-A5   10-/CS 15-D1    20-D11  25-D13  30-GND     35-A14        40-A9
```
The chip supports 8bit/16bit mode, on the PSX D0-D14 are actually wired, but
A0/D15 is wired to A0, and /BYTE is wired to GND, so 16bit mode doesn't work.<br/>
Datasheet for MX23L4100 does exist.<br/>

#### IC102 - BIOS ROM (44pin, 1Mx8, used on P16-boards, ie. VCD console)
```
  1-NC  5-A7 9-A3   13-GND 17-D1  21-D3  25-D12 29-D14    33-/BYT 37-A14 41-A10
  2-A19 6-A6 10-A2  14-/OE 18-D9  22-D11 26-D5  30-D7     34-A17  38-A13 42-A9
  3-A18 7-A5 11-A1  15-D0  19-D2  23-VCC 27-D13 31-D15/A0 35-A16  39-A12 43-NC
  4-A8  8-A4 12-/CE 16-D8  20-D10 24-D4  28-D6  32-GND    36-A15  40-A11 44-NC
```
Pinouts are from OKI MSM538032E datasheet.<br/>

#### CPU-RAM (four 28pin chips) (older boards)
Unknown.<br/>
Note: The newer 70pin RAM comes up without external /REFRESH signal, but maybe
the 28pin RAMs required refresh (the CPU has some odd delays once and when).<br/>

#### IC106 - CPU-RAM (single 70pin chip, on newer boards)
"Samsung K4Q153212M-JC60" (70pin, 512Kx32) (newer boards)<br/>
"Toshiba T7X16" (70pin, 512Kx32) (newer boards, too)<br/>
```
  1-VCC   11-N.C   21-DQ15  31-A3   41-N.C   51-DQ17  61-DQ24
  2-DQ0   12-VCC   22-N.C   32-A4   42-N.C   52-DQ18  62-DQ25
  3-DQ1   13-DQ8   23-N.C!  33-A5   43-/OE   53-DQ19  63-DQ26
  4-DQ2   14-DQ9   24-N.C   34-A6   44-/W    54-VSS   64-DQ27
  5-DQ3   15-DQ10  25-N.C   35-VCC  45-/CAS3 55-DQ20  65-VSS
  6-VCC   16-DQ11  26-N.C   36-VSS  46-/CAS2 56-DQ21  66-DQ28
  7-DQ4   17-VCC   27-/RAS  37-A7   47-/CAS1 57-DQ22  67-DQ29
  8-DQ5   18-DQ12  28-A0    38-A8   48-/CAS0 58-DQ23  68-DQ30
  9-DQ6   19-DQ13  29-A1    39-A9   49-N.C   59-VSS   69-DQ31
  10-DQ7  20-DQ14  30-A2    40-N.C  50-DQ16  60-N.C   70-VSS
```
Notes: Pin23 must NC or VSS. In the PSone, /OE is wired to GND.<br/>
Datasheet for K4Q153212M-JC60 does exist (the chip supports 27ns Hyper Page
mode access, which seems to be used for DMA).<br/>

#### IC106/IC107/IC108/IC109 - CPU-RAM (four 28pin chips, on PU-8, PU-18 boards)
SEC KM48V514BJ-6 (DRAM 512Kx8) (four pieces = 512Kx32 = 2Mbyte)<br/>
```
  1-VCC  5-DQ3   9-A9     13-A3     17-A5  21-NC    25-DQ5
  2-DQ0  6-NC    10-A0    14-VCC    18-A6  22-/OE   26-DQ6
  3-DQ1  7-/W    11-A1    15-GND    19-A7  23-/CAS  27-DQ7
  4-DQ2  8-/RAS  12-A2    16-A4     20-A8  24-DQ4   28-GND
```
Datasheet for KM48V514B-6 and BL-6 exist (though none for BJ-6). The chips
support 25ns Hyper Page mode access.<br/>

#### IC310 - SPU-RAM (512Kbyte)
EliteMT M11B416256A-35J (256K x 16bit) (40pin SOJ, PM-41 boards)<br/>
Nippon Steel NN514256ALTT-50 (256K x 16bit) (40pin TSOP-II, PU-23 boards)<br/>
Toshiba TC51V4260DJ-70 (40pin, PU-8 board) (PseudoSRAM)<br/>
```
  1-5.0V  6-5.0V   11-NC   16-A0    21-VSS  26-A8    31-I/O8   36-I/O12
  2-I/O0  7-I/O4   12-NC   17-A1    22-A4   27-/OE   32-I/O9   37-I/O13
  3-I/O1  8-I/O5   13-/WE  18-A2    23-A5   28-/CASH 33-I/O10  38-I/O14
  4-I/O2  9-I/O6   14-/RAS 19-A3    24-A6   29-/CASL 34-I/O11  39-I/O15
  5-I/O3  10-I/O7  15-NC   20-5.0V  25-A7   30-NC    35-VSS    40-VSS
```
Note: SPU-RAM supply can be 3.5V (PU-8), or 5.0V (PU-22 and PM-41).<br/>
Note: The /CASL and /CASH pins are shortcut with each other on the mainboard,
both wired to the /CAS pin of the SPU (ie. always accessing 16bit data at
once).<br/>
Note: The TSOP-II package (18mm length, super-flat and with spacing between pin
10/11 and 30/31) is used on PU-23 boards. The pinouts and connections are
identical for SOJ and TSOP-II.<br/>
Note: Nippon Steels NN514256-series is normally 256Kx4bit, nethertheless, for
some bizarre reason, their 256Kx16bit chip is marked "NN514256ALTT"... maybe
that happened accidently in the manufacturing process.<br/>
Note: The PM-41(2) board has on-chip RAM in the SPU (no external memory chip).<br/>

#### IC303 - CDROM Buffer (32Kbyte)
"HM62W256LFP-7T" (SRAM 32Kx8) (PCB bottom side) (PU-8)<br/>
"SONY CXK5V8257BTM" 32Kx8 SRAM (PU-18)<br/>
```
  1-A14  4-A6  7-A3  10-A0  13-D2   16-D4  19-D7   22-/OE  25-A8   28-VCC
  2-A12  5-A5  8-A2  11-D0  14-GND  17-D5  20-/CS  23-A11  26-A13
  3-A7   6-A4  9-A1  12-D1  15-D3   18-D6  21-A10  24-A9   27-/WE
```
Used only on older boards (eg. PU-8, PU-18), newer boards seem to have that RAM
included in the 208pin SPU chip.<br/>

#### IC201 - GPU-RAM (1MByte) (or 2MByte, of which, only 1MByte is used though)
Samsung KM4132G271BQ-10 (128K x 32bit x 2 Banks, Synchronous Graphic RAM) 1MB<br/>
Samsung K4G163222A-PC70 (256K x 32bit x 2 Banks, Synchronous Graphic RAM) 2MB<br/>
```
  1-DQ3   13-DQ19  25-/WE     37-N.C 49-A6    61-DQ9   73-VDDQ  85-VSS  97-DQ0
  2-VDDQ  14-VDDQ  26-/CAS    38-N.C 50-A7    62-VSSQ  74-DQ24  86-N.C  98-DQ1
  3-DQ4   15-VDD   27-/RAS    39-N.C 51-A8    63-DQ10  75-DQ25  87-N.C  99-VSSQ
  4-DQ5   16-VSS   28-/CS     40-N.C 52-N.C   64-DQ11  76-VSSQ  88-N.C  100-DQ2
  5-VSSQ  17-DQ20  29-A9(BA)  41-N.C 53-DSF   65-VDD   77-DQ26  89-N.C
  6-DQ6   18-DQ21  30-NC(GND) 42-N.C 54-CKE   66-VSS   78-DQ27  90-N.C
  7-DQ7   19-VSSQ  31-A0      43-N.C 55-CLK   67-VDDQ  79-VDDQ  91-N.C
  8-VDDQ  20-DQ22  32-A1      44-N.C 56-DQM1  68-DQ12  80-DQ28  92-N.C
  9-DQ16  21-DQ23  33-A2      45-N.C 57-DQM3  69-DQ13  81-DQ29  93-N.C
  10-DQ17 22-VDDQ  34-A3      46-VSS 58-NC    70-VSSQ  82-VSSQ  94-N.C
  11-VSSQ 23-DQM0  35-VDD     47-A4  59-VDDQ  71-DQ14  83-DQ30  95-N.C
  12-DQ18 24-DQM2  36-N.C     48-A5  60-DQ8   72-DQ15  84-DQ31  96-VDD
```
Newer boards often have 2MB VRAM installed (of which only 1MB is used,
apparently the 2MB chips became cheaper than the 1MB chips). At the chip side,
the only difference is that Pin30 became an additional address line (that,
called A8, and, accordingly, the old A8,A9 pins were renamed to A9,A10). At the
mainboard side, the connection is exactly the same for both 1MB and 2MB chips;
Pin30 is grounded on both PU-23 boards (which typically have 1MB) and PM-41
boards (which typically have 2MB).<br/>
Note: The PM-41(2) board has on-chip RAM in the GPU (no external memory chip).<br/>
