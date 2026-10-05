#   Memory Cards
#### Sony Playstation Memory Card (SCPH-1020)
The "SONY CXD8732AQ" chip is installed on memory cards with "SPC02K1020B"
boards, however, the text layer on the board says that it's an "LC86F8604A"
chip. So, the CXD8732AQ is most probably a standard LC86F8604A chip (more on
that below) with a Sony Memory Card BIOS ROM on it.<br/>
The "SONY CXD8732AQ" comes in a huge 64pin package, but it connects only to:<br/>
```
  5 = /IRQ7   (via 22 ohm)         2 = /RESET (from U2)
  6 = JOYCLK  (via 220 ohm)        30,31 = CF1,CF2 (12 clock pulses per 2us)
  7 = /JOYn   (via 220 ohm)        14,16,25,32,38,39,61 = 3.5V (via 3.3 ohm)
  12 = JOYCMD (via 220 ohm)        8,15,28,29 = GND
  13 = JOYDAT (via 22 ohm)         All other pins = Not connected
```
Aside from that chip, the board additionally contains some resistors,
capacitors, z-diodes (for protection against too high voltages), a 6MHz
oscillator (for the CPU), and a 5pin reset generator (on the cart edge
connector, the supply pins are slightly longer than the data signal pins, so
when inserting the cartridge, power/reset gets triggered first; the 7.5V supply
pin is left unconnected, only 3.5V are used).<br/>
Caution: The "diagonal edge" at the upper-left of the CXD8732AQ chip is Pin 49
(not pin 1), following the pin numbers on the board (and the Sanyo datasheet
pinouts), pin 1 is at the lower-left.<br/>

#### Sanyo LC86F8604A
8bit CPU with 132Kbyte EEPROM, 4Kbyte ROM, 256 bytes RAM, 2 timers, serial
port, and general purpose parallel ports. The 132K EEPROM is broken into 128K
plus 4K, the 4K might be internally used by the CPU, presumably containing the
BIOS (not too sure if it's really containing 4K EEPROM plus 4K ROM, or if it's
meant to be only either one).<br/>
```
  1=P40/A0  9=P13   17=TP0  25=VDD  33=A11  41=NC   49=A7    57=NC
  2=/RES    10=P14  18=TP1  26=NC   34=A9   42=NC   50=A6    58=NC
  3=TEST2   11=P15  19=TP2  27=NC   35=A8   43=NC   51=A5    59=NC
  4=TEST1   12=P16  20=TP3  28=NC   36=A13  44=NC   52=A4    60=NC
  5=P10     13=P17  21=TP4  29=VSS  37=A14  45=A17  53=NC    61=NC61
  6=P11     14=/CE  22=TP5  30=CF1  38=/WE  46=A16  54=NC    62=P43/A3
  7=P12     15=A10  23=TP6  31=CF2  39=VDD  47=A15  55=NC    63=P42/A2
  8=VSS     16=/OE  24=TP7  32=VDD  40=EP   48=A12  56=NC    64=P41/A1
```
Ports P10..P17 have multiple functions (I/O port, data bus, serial, etc):<br/>
```
  P10/DQ0/SEPMOD       P12/DQ2/FSI0  P14/DQ4    P16/DQ6/SI0/FSTART
  P11/DQ1/SCLK0/FSCLK  P13/DQ3       P15/DQ5    P17/DQ7/SO0/FRW
```
In March 1998, Sanyo has originally announced the LC86F8604A as an 8bit CPU
with "2.8V FLASH, achieved for the first time in the industry", however,
according to their datasheet, what they have finally produced is an 8bit CPU
with "3.5V EEPROM". Although, maybe the 3.5V EEPROM version came first, and the
2.8V FLASH was announced to be a later low-power version of the old chip;
namely, otherwise, it'd be everyones guess what kind of memory Sony used in
memory cards before 1998?<br/>

#### Note
For the actual pin-outs of the cart-edge connector, see<br/>
[Controller Ports and Memory-Card Ports](controller-ports-and-memory-card-ports.md#controller-ports-and-memory-card-ports)<br/>
