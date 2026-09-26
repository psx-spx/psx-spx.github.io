#   GPU Timings
#### Nominal Video Clock

```
  NTSC video clock = 53.693175 MHz
  PAL video clock  = 53.203425 MHz
```
Consoles will always use the video clock for its region, regardless of the GPU
being configured in NTSC or PAL output mode, because an NTSC console lacks a PAL
reference clock and vice versa. Without modifications for an additional
oscillator for the other region, consoles may experience drift over time when
playing content from a different video region. See vertical refresh rates below.

#### Vertical Video Timings
```
  263 scanlines per field for NTSC non-interlaced
  262.5 scanlines per field for NTSC interlaced

  314 scanlines per field for PAL non-interlaced
  312.5 scanlines per field for PAL interlaced
```
Horizontal blanking and vertical blanking signals occur on the video output side
as expected for NTSC/PAL signals. These are not necessarily the same as the
timer/interrupt HBLANK and VBLANK.

#### Vertical Refresh Rates
```
  NTSC mode on NTSC video clock
  Interlaced:     59.940 Hz
  Non-interlaced: 59.826 Hz

  PAL mode on PAL video clock
  Interlaced:     50.000 Hz
  Non-interlaced: 49.761 Hz

  NTSC mode on PAL video clock
  Interlaced:     59.393 Hz
  Non-interlaced: 59.280 Hz

  PAL mode on NTSC video clock
  Interlaced:     50.460 Hz
  Non-interlaced: 50.219 Hz
```
For emulation purposes, it's recommended to use an NTSC video clock when running
NTSC content (or in NTSC mode) and a PAL clock when running PAL content (or in
PAL mode).

TODO: Derivations for vertical refresh rates; horizontal timing notes

**Nocash's original GPU Timings notes:**
#### Video Clock
The PSone/PAL video clock is the cpu clock multiplied by 11/7.<br/>
```
  CPU Clock   =  33.868800MHz (44100Hz*300h)
  Video Clock =  53.222400MHz (44100Hz*300h*11/7)
```
For other PSX/PSone PAL/NTSC variants, see:<br/>
[Pinouts - CLK Pinouts](../pinouts/clk-pinouts.md#pinouts-clk-pinouts)<br/>

#### Vertical Timings
```
  PAL:  314 scanlines per frame (13Ah)
  NTSC: 263 scanlines per frame (107h)
```
Timer1 can use the hblank signal as input, allowing to count scanlines (unless
the display is configured to 0 pixels width, which would cause an endless
hblank). The hblank signal is generated even during vertical blanking/retrace.<br/>

#### Horizontal Timings
```
  PAL:  3406 video cycles per scanline (or 3406.1 or so?)
  NTSC: 3413 video cycles per scanline (or 3413.6 or so?)
```
Dotclocks:<br/>
```
  PSX.256-pix Dotclock =  5.322240MHz (44100Hz*300h*11/7/10)
  PSX.320-pix Dotclock =  6.652800MHz (44100Hz*300h*11/7/8)
  PSX.368-pix Dotclock =  7.603200MHz (44100Hz*300h*11/7/7)
  PSX.512-pix Dotclock = 10.644480MHz (44100Hz*300h*11/7/5)
  PSX.640-pix Dotclock = 13.305600MHz (44100Hz*300h*11/7/4)
  Namco GunCon 385-pix =  8.000000MHz (from 8.00MHz on lightgun PCB)
```
Dots per scanline are, depending on horizontal resolution, and on PAL/NTSC:<br/>
```
  320pix/PAL: 3406/8  = 425.75 dots     320pix/NTSC: 3413/8  = 426.625 dots
  640pix/PAL: 3406/4  = 851.5 dots      640pix/NTSC: 3413/4  = 853.25 dots
  256pix/PAL: 3406/10 = 340.6 dots      256pix/NTSC: 3413/10 = 341.3 dots
  512pix/PAL: 3406/5  = 681.2 dots      512pix/NTSC: 3413/5  = 682.6 dots
  368pix/PAL: 3406/7  = 486.5714 dots   368pix/NTSC: 3413/7  = 487.5714 dots
```
Timer0 can use the dotclock as input, however, the Timer0 input "ignores" the
fractional portions (in most cases, the values are rounded down, ie. with 340.6
dots/line, the timer increments only 340 times/line; the only value that is
rounded up is 425.75 dots/line) (for example, due to the rounding, the timer
isn't running exactly twice as fast in 512pix/PAL mode than in 256pix/PAL
mode). The dotclock signal is generated even during horizontal/vertical
blanking/retrace.<br/>

#### Frame Rates
```
  PAL:  53.222400MHz/314/3406 = ca. 49.76 Hz (ie. almost 50Hz)
  NTSC: 53.222400MHz/263/3413 = ca. 59.29 Hz (ie. almost 60Hz)
```

#### Note
Above values include "hidden" dots and scanlines (during horizontal and
vertical blanking/retrace).<br/>
