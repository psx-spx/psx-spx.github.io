#   Pinouts - GPU Pinouts (for old 160-pin GPU)
Old 160-pin GPU is used on PU-7 boards and EARLY-PU-8 boards.<br/>

#### IC203 - Sony CXD8514Q - Old 160pin GPU for use with Dual-ported VRAM
Unlike the later 208pin GPU's, the old 160pin GPU has less supply pins, and, it
doesn't have a 24bit RGB output (nor any other video output at all), instead,
it's used with a RGB D/A converter that reads the video data directly from the
Dual-ported VRAM chips (ie. from special RAM chips with two data busses, one
bus for GPU read/write access, and one for the RGB video output).<br/>
```
  1-VCC     21-GND  41-D16  61-D2     81-D12'a  101-GND     121-D7'b 141-GND
  2-GND     22-D31  42-D15  62-D1     82-D11'a  102-DT/OE'b 122-D6'b 142-53MHz
  3-/GPUCS  23-D30  43-VCC  63-D0     83-D10'a  103-DT/OE'a 123-D5'b 143-VCC
  4-GPU.A2  24-D29  44-GND  64-GND    84-D9'a   104-/RAS    124-D4'b 144-GND
  5-/GPURD  25-D28  45-D14  65-VCC    85-D8'a   105-/WE'a   125-D3'b 145-FSC
  6-/GPUWR  26-D27  46-D13  66-A8'a   86-VCC    106-/WE'b   126-D2'b 146-VCC
  7-DACK2   27-D26  47-D12  67-A7'a   87-GND    107-/SE     127-D1'b 147-GND
  8-/RESET  28-VCC  48-D11  68-A6'a   88-D7'a   108-SC      128-D0'b 148-DOTCLK
  9-VCC     29-GND  49-D10  69-A5'a   89-D6'a   109-VCC     129-VCC  149-VCC
  10-GND    30-D25  50-GND  70-GND    90-D5'a   110-GND     130-GND  150-GND
  11-SYSCK0 31-D24  51-VCC  71-A4'a   91-D4'a   111-D15'b   131-A8'b 151-MEMCK1
  12-VCC    32-D23  52-D9   72-A3'a   92-D3'a   112-D14'b   132-A7'b 152-MEMCK2
  13-GND    33-D22  53-D8   73-A2'a   93-D2'a   113-D13'b   133-A6'b 153-BLANK
  14-DREQ2  34-D21  54-D7   74-A1'a   94-D1'a   114-D12'b   134-A5'b 154-/24BPP
  15-/IRQ1  35-D20  55-D6   75-A0'a   95-D0'a   115-D11'b   135-A4'b 155-/CSYNC
  16-HBLANK 36-VCC  56-D5   76-GND    96-VCC    116-D10'b   136-A3'b 156-/HSYNC
  17-VBLANK 37-GND  57-D4   77-VCC    97-DSF    117-D9'b    137-A2'b 157-/VSYNC
  18-high?  38-D19  58-D3   78-D15'a  98-/CAS'b 118-D8'b    138-A1'b 158-VCC
  19-high?  39-D18  59-GND  79-D14'a  99-/CAS'a 119-VCC     139-A0'b 159-GND
  20-VCC    40-D17  60-VCC  80-D13'a  100-VCC   120-GND     140-VCC  160-DSYSCK0
```
Pin 1-63,148,160 = CPU Bus, Pin 66-139 = VRAM Bus (two chips, A and B), Pin
142-155 = Misc (CXA and RGB chips), Pin 18-19,156-157 = Test points.<br/>
Pin 3,5,6,11,98,99,102,103,108,148,160 via 22 ohm. Pin 104,105,106 via 100 ohm.
Pin 107 via 220 ohm. Pin 155 via 2200 ohm. Pin 145 via 220+2200 ohm.<br/>
```
  151-?       ---   (mem clock?)
  152-?             (mem clock?)
  153-BLANK         (high in HBLANK & VBLANK)
  154-/24BPP        (high=15bpp, low=24bpp)
  156-/HSYNC        rate:65us=15KHz, low:3.5us
  157-/VSYNC        rate:20ms=50Hz, low:130us=TwoLines
```

#### IC207 - SONY CXD2923AR - Digital VRAM to Analog RGB Converter (for old GPU)
This chip is used with the old 160pin GPU and two Dual-ported VRAM chips. The
2x16bit databus is capable of reading up to 32bits of VRAM data, and the chip
does then extract the 15bit or 24bit RGB values from that data (depending on
the GPU's current color depth).<br/>
The RGB outputs (pin 5,7,9) seem to be passed through transistors and
capacitors... not sure how the capacitors could output constant voltage
levels... unless the RGB signals are actually some kind of edge-triggering PWM
pulses rather than real analog levels(?)<br/>
```
  1-test?  9-BLUE    17-GND     25-D0'a  33-D8'a   41-D15'a  49-D7'b   57-D13'b
  2-test?  10-Vxx    18-MEMCK1  26-D1'a  34-D9'a   42-D0'b   50-D8'b   58-D14'b
  3-Vxx    11-test?  19-/24BPP  27-D2'a  35-D10'a  43-D1'b   51-D9'b   59-D15'b
  4-Vxx    12-test?  20-MEMCK2  28-D3'a  36-D11'a  44-D2'b   52-D10'b  60-GND
  5-RED    13-test?  21-BLANK   29-D4'a  37-D12'a  45-D3'b   53-D11'b  61-GND
  6-Vxx    14-aGND?  22-DOTCLK  30-D5'a  38-D13'a  46-D4'b   54-D12'b  62-GND
  7-GREEN  15-aGND?  23-GND     31-D6'a  39-D14'a  47-D5'b   55-GND    63-test?
  8-GND    16-aGND?  24-Vxx     32-D7'a  40-GND    48-D6'b   56-Vxx    64-GND
```
Pin 5,7,9 = RGB outputs (via transistors and capacitors?), Pin 18-22 = GPU, Pin
25-59 = VRAM (chip A and B), Pin 1-2,11-13,63 = Test points.<br/>

#### IC201 - 64pin NEC uPD482445LGW-A70-S or SEC KM4216Y256G-60 (VRAM 256Kx16)
#### IC202 - 64pin NEC uPD482445LGW-A70-S or SEC KM4216Y256G-60 (VRAM 256Kx16)
These are special Dual-ported VRAM chips (with two data busses), the D0-D15
pins are wired to the GPU (for read/write access), the Q0-Q15 pins are wired to
the RGB D/A converter (for sequential video output).<br/>
```
  1-VCC     9-Q2    17-D5    25-/UWE  33-GND   41-DSF  49-Q10   57-VCC
  2-/DT/OE  10-D2   18-VCC   26-/RAS  34-A3    42-GND  50-D11   58-D14
  3-GND     11-Q3   19-Q6    27-A8    35-A2    43-D8   51-Q11   59-Q14
  4-Q0      12-D3   20-D6    28-A7    36-A1    44-Q8   52-GND   60-D15
  5-D0      13-GND  21-Q7    29-A6    37-A0    45-D9   53-D12   61-Q15
  6-Q1      14-Q4   22-D7    30-A5    38-QSF   46-Q9   54-Q12   62-GND
  7-D1      15-D4   23-GND   31-A4    39-/CAS  47-VCC  55-D13   63-/SE
  8-VCC     16-Q5   24-/LWE  32-VCC   40-NC    48-D10  56-Q13   64-SC
```
The 8bit /LWE and /UWE write signals are shortcut with each other and wired to
the GPU's 16bit /WE write signal.<br/>

#### IC501 24pin "SONY CXA1645M" Analog RGB to Composite (older boards only)
```
  1-GND1  4-BIN   7-NPIN   10-SYNCIN  13-IREF  16-YOUT   19-VCC2   22-GOUT
  2-RIN   5-NC    8-BFOUT  11-BC      14-VREF  17-YTRAP  20-CVOUT  23-ROUT
  3-GIN   6-SCIN  9-YCLPC  12-VCC1    15-COUT  18-FO     21-BOUT   24-GND2
```
Used only on older boards (eg. PU-7, PU-8, PU-16), newer boards generate
composite signal via 48pin IC502.<br/>
Pin7 (NPIN): NTSC=VCC, PAL=GND. Pin6 (SCIN aka FSC): Sub Carrier aka PAL/NTSC
color clock, which can be derived from three different sources:<br/>
```
  GPU pin 145 (old 160-pin GPU)
  GPU pin 154 (new 208-pin GPU)
  IC204 (on later boards, eg. PSone)
```
for the color clocks from GPU pins, the GPU does try to automatically generate
PAL or NTSC clock depending on current frame rate, which is resulting in
"wrong" color clock when chaning between 50Hz/60Hz mode).<br/>
