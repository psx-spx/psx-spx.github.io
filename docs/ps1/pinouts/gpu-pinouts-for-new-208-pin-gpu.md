#   Pinouts - GPU Pinouts (for new 208-pin GPU)
New 206-pin GPU is used LATE-PU-8 boards and up.<br/>

#### GPU Pinouts (IC203)

| Pin | Name        | Pin | Name        | Pin | Name         | Pin | Name        |
| --: | :---------- | --: | :---------- | --: | :----------- | --: | :---------- |
|   1 | `HOST./CS`  |  53 | `HOST.D10`  | 105 | `GND`        | 157 | `NTSC/PAL`  |
|   2 | `HOST.A0`   |  54 | `HOST.D9`   | 106 | `VDD`        | 158 | `/VSYNC`    |
|   3 | `HOST./RD`  |  55 | `HOST.D8`   | 107 | `SGRAM.D9`   | 159 | `/HSYNC`    |
|   4 | `HOST./WR`  |  56 | `HOST.D7`   | 108 | `SGRAM.D8`   | 160 | `DAC.B0`    |
|   5 | `HOST.DACK` |  57 | `HOST.D6`   | 109 | `SGRAM.D7`   | 161 | `DAC.B1`    |
|   6 | `/RESET`    |  58 | `HOST.D5`   | 110 | `SGRAM.D6`   | 162 | `DAC.B2`    |
|   7 | `VDD`       |  59 | `HOST.D4`   | 111 | `SGRAM.D5`   | 163 | `DAC.B3`    |
|   8 | `GND`       |  60 | `GND`       | 112 | `SGRAM.D4`   | 164 | `GND`       |
|   9 | `/SYSCLK`   |  61 | `VDD`       | 113 | `GND`        | 165 | `VDD`       |
|  10 | `VDD`       |  62 | `HOST.D3`   | 114 | `VDD`        | 166 | `DAC.B4`    |
|  11 | `GND`       |  63 | `HOST.D2`   | 115 | `SGRAM.D3`   | 167 | `DAC.B5`    |
|  12 | `HOST.DREQ` |  64 | `HOST.D1`   | 116 | `SGRAM.D2`   | 168 | `DAC.B6`    |
|  13 | `HOST./IRQ` |  65 | `HOST.D0`   | 117 | `SGRAM.D1`   | 169 | `DAC.B7`    |
|  14 | `HBLANK`    |  66 | `GND`       | 118 | `SGRAM.D0`   | 170 | `DAC.G0`    |
|  15 | `GND`       |  67 | `VDD`       | 119 | `GND`        | 171 | `DAC.G1`    |
|  16 | `VDD`       |  68 | `PCKSL2`    | 120 | `VDD`        | 172 | `DAC.G2`    |
|  17 | `VBLANK`    |  69 | `PCKSL1`    | 121 | `SGRAM./CS1` | 173 | `DAC.G3`    |
|  18 | `HVHLD`     |  70 | `PCKSL0`    | 122 | `SGRAM./CS0` | 174 | `GND`       |
|  19 | `GND`       |  71 | `TEST3`     | 123 | `SGRAM.DSF`  | 175 | `VDD`       |
|  20 | `GND`       |  72 | `TEST2`     | 124 | `SGRAM./RAS` | 176 | `DAC.G4`    |
|  21 | `NC`        |  73 | `TEST1`     | 125 | `SGRAM./CAS` | 177 | `DAC.G5`    |
|  22 | `VDD`       |  74 | `TEST0`     | 126 | `SGRAM./WE`  | 178 | `DAC.G6`    |
|  23 | `VDD`       |  75 | `VDD`       | 127 | `SGRAM.DQMH` | 179 | `DAC.G7`    |
|  24 | `HOST.D31`  |  76 | `GND`       | 128 | `SGRAM.DQML` | 180 | `DAC.R0`    |
|  25 | `HOST.D30`  |  77 | `SGRAM.D31` | 129 | `GND`        | 181 | `DAC.R1`    |
|  26 | `HOST.D29`  |  78 | `SGRAM.D30` | 130 | `VDD`        | 182 | `DAC.R2`    |
|  27 | `HOST.D28`  |  79 | `SGRAM.D29` | 131 | `MCLKOUT`    | 183 | `DAC.R3`    |
|  28 | `HOST.D27`  |  80 | `VDD`       | 132 | `GND`        | 184 | `GND`       |
|  29 | `VDD`       |  81 | `GND`       | 133 | `VDD`        | 185 | `VDD`       |
|  30 | `GND`       |  82 | `SGRAM.D28` | 134 | `MCLKIN`     | 186 | `DAC.R4`    |
|  31 | `HOST.D26`  |  83 | `SGRAM.D27` | 135 | `GND`        | 187 | `DAC.R5`    |
|  32 | `HOST.D25`  |  84 | `SGRAM.D26` | 136 | `VDD`        | 188 | `DAC.R6`    |
|  33 | `HOST.D24`  |  85 | `SGRAM.D25` | 137 | `SGRAM.A9`   | 189 | `DAC.R7`    |
|  34 | `HOST.D23`  |  86 | `SGRAM.D24` | 138 | `SGRAM.A8`   | 190 | `GND`       |
|  35 | `HOST.D22`  |  87 | `VDD`       | 139 | `SGRAM.A7`   | 191 | `VDD`       |
|  36 | `HOST.D21`  |  88 | `GND`       | 140 | `SGRAM.A6`   | 192 | `VCLK_NTSC` |
|  37 | `VDD`       |  89 | `SGRAM.D23` | 141 | `VDD`        | 193 | `VDD`       |
|  38 | `GND`       |  90 | `SGRAM.D22` | 142 | `GND`        | 194 | `GND`       |
|  39 | `HOST.D20`  |  91 | `SGRAM.D21` | 143 | `SGRAM.A5`   | 195 | `VDD`       |
|  40 | `HOST.D19`  |  92 | `SGRAM.D20` | 144 | `SGRAM.A4`   | 196 | `VCLK_PAL`  |
|  41 | `HOST.D18`  |  93 | `SGRAM.D19` | 145 | `SGRAM.A3`   | 197 | `VDD`       |
|  42 | `HOST.D17`  |  94 | `SGRAM.D18` | 146 | `GND`        | 198 | `GND`       |
|  43 | `VDD`       |  95 | `SGRAM.D17` | 147 | `VDD`        | 199 | `PCK`       |
|  44 | `GND`       |  96 | `GND`       | 148 | `SGRAM.A2`   | 200 | `GND`       |
|  45 | `HOST.D16`  |  97 | `VDD`       | 149 | `SGRAM.A1`   | 201 | `VDD`       |
|  46 | `HOST.D15`  |  98 | `SGRAM.D16` | 150 | `SGRAM.A0`   | 202 | `DMASK`     |
|  47 | `HOST.D14`  |  99 | `SGRAM.D15` | 151 | `VDD`        | 203 | `ODE2`      |
|  48 | `HOST.D13`  | 100 | `SGRAM.D14` | 152 | `GND`        | 204 | `GND`       |
|  49 | `HOST.D12`  | 101 | `SGRAM.D13` | 153 | `FSC`        | 205 | `VDD`       |
|  50 | `HOST.D11`  | 102 | `SGRAM.D12` | 154 | `VDD`        | 206 | `/DSYSCK`   |
|  51 | `VDD`       | 103 | `SGRAM.D11` | 155 | `GND`        | 207 | `GND`       |
|  52 | `GND`       | 104 | `SGRAM.D10` | 156 | `CSYNC`      | 208 | `VDD`       |

Pin 77..150 = Video RAM Bus. Pin 156..189 = Video Out Bus. Other = CPU Bus. Pin
153: Sub Carrier (NC on newer boards whick pick color clock from IC204).<br/>

#### GPU Pinout Notes
- `SGRAM./CS1` is only used on arcade boards with 2 MB VRAM (two 1 MB chips).
- `HVHLD` is a lightgun input (similar to `/IRQ10` but handled in hardware) used
  only by some arcade boards. On retail consoles it has a 4.7k pullup to 3.5V.
- `TEST0-TEST3` are tied to 3.5V. `PCKSL0-PCKSL2` (outputs possibly related to
  the current horizontal/vertical resolution and thus pixel clock?) are left
  unconnected.
- `MCLKIN` and `MCLKOUT` are tied together and wired to the DAC's clock input.
  `MCLKIN` could possibly be an external clock input for genlocking purposes.
- On earlier motherboards and on most arcade boards only `VCLK_PAL` or
  `VCLK_NTSC` is wired up, depending on the console's region. On later boards
  both are tied together and connected to a programmable clock generator, which
  is preprogrammed to generate the appropriate frequency.
- `/VSYNC` and `/HSYNC` are only connected to test points.
- `/CSYNC = (/VSYNC AND /HSYNC)`. `BLANK = (VBLANK OR HBLANK)`.
- `SGRAM.DQML` is wired to both `DQM0` and `DQM2` on the SGRAM, while
  `SGRAM.DQMH` is wired to both `DQM1` and `DQM3`.
- `DMASK` outputs the mask/"alpha" bit of the current pixel and is used by some
  arcade boards to composite the GPU's output on top of an external video
  source. `ODE2` indicates which field is currently being output in interlaced
  mode.

#### IC202 44pin "Philips TDA8771H" Digital to Analog RGB (older boards only)
Region Japan+Europe: TDA8771AN<br/>
Region America+Asia: MC151854FLTEG or so?<br/>
```
  1-IREF  6-GNDd1  11-R1   16-G4   21-B7  26-B2     31-CLK    36-OUTB  41-NC
  2-GNDa1 7-VDDd1  12-R0   17-G3   22-B6  27-VDDd2  32-VDDa1  37-NC    42-GNDa2
  3-R7    8-R4     13-G7   18-G2   23-B5  28-GNDd2  33-VREF   38-NC    43-VDDa4
  4-R6    9-R3     14-G6   19-G1   24-B4  29-B1     34-NC     39-VDDa3 44-OUTR
  5-R5    10-R2    15-G5   20-G0   25-B3  30-B0     35-VDDa2  40-OUTG
```
Used only LATE-PU-8 boards (and PU-16, which does even have two TDA8771AH
chips: one on the mainboard, and one on the VCD daughterboard).<br/>
Earlier boards are generating analog RGB via 64pin IC207, and later boards RGB
via 48pin IC502.<br/>

#### IC502 48pin "SONY CXA2106R-T4" - 24bit RGB video D/A converter

| Pin | Name         | Pin | Name       | Pin | Name | Pin | Name      |
| --: | :----------- | --: | :--------- | --: | :--- | --: | :-------- |
|   1 | `BCLAMP`     |  13 | `NTSC/PAL` |  25 | `G7` |  37 | `B3`      |
|   2 | `AGND2`      |  14 | `SYNCIN`   |  26 | `G6` |  38 | `B2`      |
|   3 | `ROUT`       |  15 | `SCIN`     |  27 | `G5` |  39 | `B1`      |
|   4 | `GOUT`       |  16 | `R7`       |  28 | `G4` |  40 | `B0`      |
|   5 | `BOUT`       |  17 | `R6`       |  29 | `G3` |  41 | `VCLK`    |
|   6 | `YOUT`       |  18 | `R5`       |  30 | `G2` |  42 | `DGND`    |
|   7 | `COUT`       |  19 | `R4`       |  31 | `G1` |  43 | `VREFIN`  |
|   8 | `VOUT`       |  20 | `DVDD`     |  32 | `G0` |  44 | `VREFOUT` |
|   9 | `AVCC2`      |  21 | `R3`       |  33 | `B7` |  45 | `AGND1`   |
|  10 | `YTRAP`      |  22 | `R2`       |  34 | `B6` |  46 | `RCRAMP`  |
|  11 | `NC`         |  23 | `R1`       |  35 | `B5` |  47 | `AVCC1`   |
|  12 | `POWER_SAVE` |  24 | `R0`       |  36 | `B4` |  48 | `GCLAMP`  |

Pin 3..8 (analogue outputs) are passed via external 75 ohm resistors.<br/>
Pin 6,7 additionally via 220uF. Pin 8 additionally via smaller capacitor.<br/>
Pin 10 (YTRAP) wired via 2K7 to 5.0V.<br/>
Pin 1,44,46,48 (can) connect via capacitors to ground (only installed for 44).<br/>
The 4.4MHz clock is obtained via 2K2 from IC204.Pin6.<br/>
The /PAL pin can be reportedly GROUNDED to force PAL colors in NTSC mode, when
doing that, you may first want to disconnect the pin from the GPU.<br/>
Note: Rohm BH7240AKV has same pinout (XXX but with pin7/pin8 swapped?)<br/>

#### Beware
Measuring in the region near GPU Pin10 is the nocash number one source for
blowing up components on the mainboard. If you want to measure that signals
while power is on, better measure them at the CPU side.<br/>
