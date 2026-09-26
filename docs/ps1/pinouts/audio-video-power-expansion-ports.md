#   Pinouts - Audio, Video, Power, Expansion Ports
#### AV Multi Out (Audio/Video Port)
```
  1      RGB-Video Green
  2      RGB-Video Red
  3      Supply +5.0V (eg. supply for external RF adaptor)
  4      RGB-Video Blue
  5      Supply Ground
  6      S-Video C (chrominance)
  7      Composite Video (yellow cinch)
  8      S-Video Y (luminance)                    ____________________________
  9      Audio Left      (white cinch)           |                            |
  10     Audio Left Ground                       | 12 11 10 9 8 7 6 5 4 3 2 1 |
  11     Audio Right     (red cinch)             |____________________________|
  12     Audio Right Ground
  Shield Video Ground
```
The standard AV-cable connects only to Pins 7,9,10,11,12,Shield (with pin 1 and
3 and Shield shortcut with each other, used for both audio and video ground).<br/>
The plug on that cable does have additional sparings for pin 1,3,5 (though
without any metal-contacts installed in there) (pin 3,5 would be used as supply
for external RF modulators) (no idea what pin 1 could be used for though?).<br/>
RGB displays may (or may not) be able to extract /SYNC from the Composite
signal, if that doesn't work, note that /SYNC (and separate /VSYNC, /HSYNC
signals) are found on the GPU pinouts, moreover, the GPU outputs 24bit digital
RGB.<br/>
Not sure if a VGA monitor can be connected? The SYNC signals are there (see GPU
pinputs), but the vertical resolution is only 200/240 lines... standard VGA
displays probably support only 400/480 lines (or higher resolutions for newer
multisync SVGA displays) (as far as I know, the classic 200 lines VGA mode is
actually outputting 400 lines, with each line repeated twice).<br/>

#### Parallel Port (PIO) (Expansion Port) (CN103)
This port exists only on older PSX boards (not on newer PSX boards, and not on
PSone boards).<br/>
The parallel port is used by various third-party unlicensed cheat cartridges and
VCD player addons, as well as by the PSIO optical drive emulator (see below).<br/>
```
             ________
            |        |                            Console Rear View
      GND ==| 1   35 |== GND                 .-------------------------.
   /RESET  =| 2   36 |=  DACK5               |1  2  3  ... ... 32 33 34|
    DREQ5  =| 3   37 |=  /IRQ10              |35 36 37 ... ... 66 67 68|
     /CS0  =| 4   38 |=  /WR1                |__.-------------------.__|
(SBEN)GND  =| 5   39 |=  GND(CS2)
       D0  =| 6   40 |=  D1
       D2  =| 7   41 |=  D3
       D4  =| 8   42 |=  D5
       D6  =| 9   43 |=  D7
       D8  =|10   44 |=  D9
      D10  =|11   45 |=  D11
      D12  =|12   46 |=  D13
      D14  =|13   47 |=  D15
       A0  =|14   48 |=  A1
       A2  =|15   49 |=  A3
      GND  =|16   50 |=  GND
    +3.5V ==|17   51 |== +3.5V
    +7.5V ==|18   52 |== +7.5V
      GND  =|19   53 |=  GND
       A4  =|20   54 |=  A5
       A6  =|21   55 |=  A7
       A8  =|22   56 |=  A9
      A10  =|23   57 |=  A11
      A12  =|24   58 |=  A13
      A14  =|25   59 |=  A15
      A16  =|26   60 |=  A17
      A18  =|27   61 |=  A19
      A20  =|28   62 |=  A21
      A22  =|29   63 |=  A23
      /RD  =|30   64 |=  /WR0
(/IRQ2)NC  =|31   65 |=  NC(/CS5)
    SYSCK  =|32   66 |=  LRCK
     BCLK  =|33   67 |=  SDIN
      GND ==|34   68 |== GND
            |________|
```
On a stock console, pin 5 is ground and pins 31 and 65 are not connected. These
pins are repurposed by the PSIO's switch board to allow the PSIO to emulate the
CD-ROM drive; when pin 5 (SBEN) is high, the switch board disconnects the CPU's
/CS5 and /IRQ2 pins from the CD drive and routes them to pins 65 and 31
respectively, allowing the PSIO to take over. Pin 39 can also be repurposed in a
similar way to allow /CS2 and thus the internal BIOS ROM to be overridden.<br/>
For more details see:<br/>
[pcsx-redux - PIO port](https://github.com/grumpycoders/pcsx-redux/wiki/PIO-port)<br/>
[pcsx-redux - Switch Board](https://github.com/grumpycoders/pcsx-redux/wiki/Switch-Board)<br/>

#### Internal Power Supply (PSX)
The PSX contains an internal power supply, however, like the PSone, it's only
having a "Standby" button, which merely disconnects 3.5V and 7.9V from the
mainboard. The actual power supply remains powered, and wastes energy day and
night, thanks Sony!<br/>

#### External Power Supply (PSone)
```
  Inner +7.5V DC 2.0A   (inside diameter 0.8mm)
  Outer GND             (outside diameter 5.0mm)
```
