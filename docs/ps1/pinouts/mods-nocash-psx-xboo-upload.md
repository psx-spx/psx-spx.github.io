#   Mods - Nocash PSX-XBOO Upload
#### Nocash PSX-XBOO Connection (required)
```
  GND (BOARD)       --------- GND    (SUBD.18-25, CNTR.19-30)
  A16 (ROM.2)       --------- SLCT   (SUBD.13, CNTR.13)     ;\
  A17 (ROM.30)      --------- PE     (SUBD.12, CNTR.12)     ; 4bit.dta.out
  A18 (ROM.31)      --------- /ACK   (SUBD.10, CNTR.10)     ;
  A19 (ROM.1)       --------- BUSY   (SUBD.11, CNTR.11)     ;/
  /RESET            ---|>|--- /INIT  (SUBD.16, CNTR.31)     ;-reset.in
  D0..D7 (74HC541)  --------- DATA   (SUBD.2-9, CNTR.2-9)   ;\
  Y0..Y7 (74HC541)  --------- D0..D7 (ROM.13-15,17-21)      ; 7bit.dta.in, and
  /OE1 (74HC541.1)  --------- /EXP   (CPU.98)               ; 1bit.dta.clk.in
  /OE2 (74HC541.19) --------- /OE    (ROM.24)               ;
  GND  (74HC541.10) --------- GND    (BOARD)                ;
  VCC  (74HC541.20) --------- +5V    (BOARD)                ;/
```

#### Nocash PSX-BIOS Connection (required)
```
  A0..A19 (ROM) --------- A0..A19 (EPROM)
  D0..D7  (ROM) --------- D0..D7  (EPROM)
  /BIOS (CPU.97)--------- /CS  (EPROM.22)
  /OE (ROM.24)  --------- /OE  (EPROM.24)
  +5V (BOARD)   --------- VCC  (EPROM.32)
  GND (BOARD)   --------- GND  (EPROM.16)
  /CS (ROM.22)  --/cut/-- /BIOS (CPU.97)
  /CS (ROM.22)  --------- +5V  (BOARD) (direct, or via 100k ohm)
```

#### Nocash BIOS "Modchip" Feature (optional)
```
  SPU.Pin42 "data" -------|>|------ CPU.Pin149 (A20)
  SPU.Pin5  "sync" ---------------- IC723.Pin17
```
The nocash PSX bios outputs the "data" signal on the A20 address line, so
(aside from the BIOS chip) one only needs to install a 1N4148 diode and two
wires to unlock the CDROM. For more variants, see:<br/>
[CDROM Protection - Chipless Modchips](../cdr/cdromformat.md#cdrom-protection-chipless-modchips)<br/>

#### Composite NTSC/PAL Mod (optional)
[Mods - PAL/NTSC Color Mods](mods-pal-ntsc-color-mods.md#mods-palntsc-color-mods)<br/>

#### Component List
```
  32pin socket for EPROM
  EPROM (or FLASH)
  74HC541 (8-bit 3-state noninverting buffer/line driver)
  1N4148 diode (for reset signal)
  1N4148 diode (for optional "modchip" feature)
  36pin Centronics socket for printer cable (or 25pin dsub)
```

#### PSX-XBOO Upload BIOS
The required BIOS is contained in no$psx (built-in in the no$psx.exe file), the
Utility menu contains a function for creating a standalone ROM-image (file
PSX-XBOO.ROM in no$psx folder; which can be then burned to FLASH or EPROM).<br/>

#### Pinouts
```
              ______  ______                      ____  ____
             |      \/      |                    |    \/    |
  A19,VPP12  | 1         32 |  VCC6         /OE1 |1       20| VCC
        A16  | 2         31 |  A18,/PGM       D0 |2       19| /OE2
        A15  | 3         30 |  A17            D1 |3       18| Y0
        A12  | 4         29 |  A14            D2 |4       17| Y1
         A7  | 5         28 |  A13            D3 |5 74541 16| Y2
         A6  | 6         27 |  A8             D4 |6       15| Y3
         A5  | 7         26 |  A9,IDENT12     D5 |7       14| Y4
         A4  | 8         25 |  A11            D6 |8       13| Y5
         A3  | 9         24 |  /OE,VPP12      D7 |9       12| Y6
         A2  | 10        23 |  A10           GND |10      11| Y7
         A1  | 11        22 |  /CE,(/PGM)        |__________|
         A0  | 12        21 |  D7
         D0  | 13        20 |  D6
         D1  | 14        19 |  D5
         D2  | 15        18 |  D4
        GND  | 16        17 |  D3
             |______________|
```

#### Note
Instead of the above internal mod, the nocash kernel clone can be also
installed on cheat devices, which do also include DB25 connectors for parallel
port uploads, too.<br/>
For DB25 parallel port uploads, do the following mods to the cheat device:<br/>
```
 - Datel: use the FiveWire mod to get it parallel port compatible
 - Xplorer: simply wire DB25./INIT to EXP./RESET (with diode, if needed)
```
