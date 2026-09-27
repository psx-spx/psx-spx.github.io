#   Pinouts - CLK Pinouts
The "should-be" CPU clock is 33.868800 Hz (ie. the 44100Hz CDROM/Audio clock,
multiplied by 300h). However, the different PSX/PSone boards are using
different oscillators, multipliers and dividers, which aren't exactly reaching
that "should-be" value. The PSone are using a single oscillator for producing
CPU/GPU clocks, and for producing the TV/color signal:<br/>
```
  For PAL,  Fsc=4.43361875MHz (5^6*283.75Hz+25Hz) --> 4*Fsc=17.734MHz
  For NTSC, Fsc=3.579545MHz   (4.5*455/572 MHz)   --> 4*Fsc=14.318MHz
```

#### PSone/PAL - IC204 8pin - "CY2081, SL-509" or "2294A, 1913"
Clock Multiplier/Divider<br/>
```
  1 53MHz          ;17.734MHz*3 = 53.202 MHz (?)
  2 GND
  3 X1 17.734MHz
  4 X2 17.734MHz
  5 67MHz          ;17.734MHz*3*2*7/11 = 67.711636 MHz (?)
  6 4.4Mhz         ;17.734MHz/4 = 4.4335MHz  (?)  ;via 2K2 to IC502.pin15
  7 3.5V
  8 3.5V
```

#### PSone/NTSC - IC204 8pin "CY2081 SL-500" (PSone, and PSX/PU-20 and up)
Unknown. Uses a 14.318MHz oscillator, so multiply/divide factors must be
somehow different.<br/>
```
   3*3*7*5/2/11 = 14.3181818
   3*3*7*7*100  = 44100
```
The "optimal" conversion would be (hardware is barely able to do that):<br/>
```
   14.3181818 * 3*7*11*64 / (5*5*5*5*5) = 67.737600
```
So, maybe it's doing<br/>
```
   14.3181818 * 2*2*13/11   ... or so?
```

#### PSX/PAL
PU-7 and PU-8 boards are using three separate oscillators:<br/>
```
  X101: 67.737MHz (div2 = CPU Clock = 33.8685MHz) (div600h = 44.1kHz audio)
  X201: 53.20MHz (GPU Clock) (div12 = PAL color clock)
  X302: 4.000MHz (for CDROM SUB CPU)
```
PU-18 does have same X101/X201 as above, but doesn't seem to have X302.<br/>

#### PSX/NTSC
PU-7 and PU-8 boards are using three separate oscillators:<br/>
```
  X101: 67.737MHz (div2 = CPU Clock = 33.8685MHz) (div600h = 44.1kHz audio)
  X201: 53.69MHz (GPU Clock) (div15 = NTSC color clock)
  X302: 4.000MHz (for CDROM SUB CPU)
```
PU-20 works more like PSone (a single oscillator, and CY2081 SL-500 divider)<br/>
