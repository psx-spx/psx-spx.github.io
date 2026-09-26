#   Mods - PAL/NTSC Color Mods
The PSX hardware is more or less capable of generating both PAL and NTSC
signals. However, it's having the bad habbit to do this automatically depending
on the game's frame rate. And worse, it's doing it regardless of whether the
board is having matching oscillators installed (eg. a PAL board in 60Hz mode
will produce NTSC encoding with faulty NTSC color clock).<br/>
```
  color encoding    PAL             NTSC
  color clock       4.43361875MHz   3.579545MHz
  frame rate        50Hz            60Hz
```

#### RGB Cables
RGB cables don't rely on composite PAL/NTSC color encoding, and thus don't need
any color mods (except, see the caution on GNDed pins for missing
53.20MHz/53.69MHz oscillators below).<br/>

#### Newer Consoles (PU-22, PU-23, PM-41, PM-41(2))
These consoles have 17.734MHz (PAL) or 14.318MHz (NTSC) oscillators with
constant dividers, so the color clock will be always constant, and one does
only need to change the color encoding:<br/>
```
  /PAL (IC502.pin13) ---/cut/--- /PAL (GPU.pin157)
  /PAL (IC502.pin13) ----------- GND (PAL) or VCC (NTSC)
```
This forces the console to be always producing the desired composite color
format (regardless of whether the GPU is in 50Hz or 60Hz mode).<br/>
That works for NTSC games on PAL consoles (and vice-versa). However, it won't
work for NTSC consoles with PAL TV Sets (for that case it'd be easiest to
install an extra oscillator, as done on older consoles).<br/>

#### Older Consoles (PU-7, PU-8, PU-16, PU-18, PU-20)
These consoles have 53.20MHz (PAL) or 53.69MHz (NTSC) oscillators and the GPU
does try to change the clock divider depending on the frame rate (thereby
producing a nonsense clock signal that's neither PAL nor NTSC). Best workaround
is to install an extra 4.43361875MHz (PAL) or 3.579545MHz (NTSC) oscillator
(with internal amplifier, ie. in 4pin package, which resembles DIP14, hence the
pin 1,7,8,14 numbering):<br/>
```
  GPU ------------------/cut/--- CXA1645M.pin6  SCIN
  GPU ------------------/cut/--- CXA1645M.pin7  /PAL
  Osc.pin14 VCC ---------------- CXA1645M.pin12 VCC (5V)
  Osc.pin7  GND ---------------- CXA1645M.pin1  GND
  Osc.pin8  OUT ---------------- CXA1645M.pin6  SCIN
  Osc.pin1  NC  --
  GND (PAL) or VCC (NTSC) ------ CXA1645M.pin7  /PAL
```
Caution: Many mainboards have solder pads for both 53.20MHz and 53.69MHz
oscillators, the missing oscillator is either GNDed or shortcut with the
installed oscillator (varies from board to board, usually via 0 ohm resistors
on PCB bottom side). If it's GNDed, remove that connection, and instead have it
shortcut with the installed oscillator.<br/>
Alternately, instead of the above mods, one could also install the missing
oscillator (and remove its 0 ohm resistor), so the board will have both
53.20MHz and 53.69MHz installed; that will produce perfect PAL and NTSC signals
in 50Hz and 60Hz mode accordingly, but works only if the TV Set recognizes both
PAL and NTSC signals.<br/>

#### Notes
External 4.433MHz/3.579MHz osciallors won't be synchronized with the GPU frame
rate (normally you don't want them to be synchronized, but there's some small
risk that they might get close to running in sync, which could result in static
or crawling color artifacts).<br/>
For the CXA1645 chip modded to a different console region, one should also
change one of the resistors (see datasheet), there's no noticable difference on
the TV picture though.<br/>

#### Region Checks
Some kernel versions contain regions checks (additionally to the SCEx check),
particulary for preventing NTSC games to run on PAL consoles, or non-japanese
games on japanese consoles. Some PAL modchips can bypass that check (by
patching the region byte in BIOS). Expansions ROMs or nocash kernel clone could
be also used to avoid such checks.<br/>
