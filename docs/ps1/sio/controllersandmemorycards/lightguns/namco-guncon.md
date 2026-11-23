#   Namco GunCon
#### GunCon Cinch-based Lightguns (Namco)
```
  __Halfword 0 (Controller Info)___________________
  0-15  Controller Info  (5A63h=Namco Lightgun; GunCon/Cinch Type)
  __Halfword 1 (Buttons)___________________________
  0-2   Not used              (All bits always 1)
  3     Button A (Left Side)  (0=Pressed, 1=Released) ;aka Joypad Start
  4-12  Not used              (All bits always 1)
  13    Trigger Button        (0=Pressed, 1=Released) ;aka Joypad O-Button
  14    Button B (Right Side) (0=Pressed, 1=Released) ;aka Joypad X-Button
  15    Not used              (All bits always 1)
  __Halfword 2 (X)_________________________________
  0-15  8MHz clks since HSYNC (01h=Error, or 04Dh..1CDh)
  __Halfword 3 (Y)_________________________________
  0-15  Scanlines since VSYNC (05h/0Ah=Error, PAL=20h..127h, NTSC=19h..F8h)
```
Caution: The gun should be read only shortly after begin of VBLANK.<br/>

#### Error/Busy Codes
Coordinates X=0001h, Y=0005h indicates "unexpected light":<br/>
```
  ERROR: Sensed light during VSYNC (eg. from a Bulb or Sunlight).
```
Coordinates X=0001h, Y=000Ah indicates "no light", this can mean either:<br/>
```
  ERROR: no light sensed at all (not aimed at screen, or screen too dark).
  BUSY: no light sensed yet (when trying to read gun during rendering).
```
To avoid the BUSY error, one should read the gun shortly after begin of VBLANK
(ie. AFTER rendering, but still BEFORE vsync). Doing that isn't as simple as
one might think:<br/>
On a NTSC console, time between VBLANK and VSYNC is around 30000 cpu clks,
reading the lightgun (or analog joypads) takes around 15000 cpu clks. So,
reading two controllers within that timeframe may be problematic (and reading
up to eight controllers via multitaps would be absolutely impossible). As a
workaround, one may arrange the read-order to read lightguns at VBLANK (and
joypads at later time). If more than one lightgun is connected, then one may
need to restrict reading to only one (or maybe: max two) guns per frame.<br/>

#### Minimum Brightness
Below are some average minimum brightness values, the gun may be unable to
return position data near/below that limits (especially coordinates close to
left screen border are most fragile). The exact limits may vary from gun to
gun, and will also depend on the TV Set's brightness setting.<br/>
```
  666666h Minimum Gray
  770000h Minimum Blue
  007700h Minimum Green
  000099h Minimum Red
```
The gun does also work with mixed colors (eg. white bold text on black
background works without errors, but the returned coordinates are a bit "jumpy"
in that case; returning the position of the closest white pixels).<br/>
BUG: On a plain RED screen, aiming at Y\>=00F0h, the gun is randomly
returning either Y, or Y-80h (that error occurs in about every 2nd frame, ie.
at 50% chance). It's strange... no idea what is causing that effect.<br/>

#### Coordinates
The coordinates are updated in all frames (as opposed to some lightguns which
do update them only when pulling the trigger).<br/>
The absolute min/max coordinates may vary from TV set to TV set (some may show
a few more pixels than others). The relation of the gun's Screen Coodinates to
VRAM Coordinates does (obviously) depend on where the VRAM is located on the
screen; ie. on the game's GP1(06h) and GP1(07h) settings.<br/>
Vertical coordinates are counted in scanlines (ie. equal to pixels). Horizontal
coordinates are counted in 8MHz units (which would equal a resolution of 385
pixels; which can be, for example, converted to 320 pixel resolution as
X=X\*320/385).<br/>

#### Misinformation (from bugged homebrew source code)
```
  __Halfword 2 (X)_________________________________
  0-7   X-Coordinate  (actual: see X-Offset)             ;\with unspecified
  8-15  X-Offset      (00h: X=X-80, Nonzero: X=X-80+220) ;/dotclock?
  __Halfword 3 (Y)_________________________________
  0-7   Y-Coordinate  (actual: Y=Y-25) (but then, max is only 230, not 263 ?)
  8-15  Pad ID        (uh, what id?) (reportedly too dark/bright error flag?)
```

#### Namco Lightgun Drawing
```
           _-_______________________--_
  ----->  |    namco            \\\\   \    Namco G-Con 45 (light gray) (cinch)
  sensor   |............ .. .....\\\\...|_
          |_ :          :..   _____      _\
            |  O        :__../  )))|    (
             \__________/  |_\____/|     \
               :               :   |      |
               :               :   |      |  NPC-103
         A-Button (Left)   Trigger |      |  SLPH-00034/SLEH-0007/SLUH-00035
         B-Button (Right)          |______|
```

#### See also
[Component List and Chipset Pin-Outs for Namco Lightgun, NPC-103](../../../pinouts/component-list-and-chipset-pin-outs-for-namco-lightgun-npc-103.md#component-list-and-chipset-pin-outs-for-namco-lightgun-npc-103)<br/>
