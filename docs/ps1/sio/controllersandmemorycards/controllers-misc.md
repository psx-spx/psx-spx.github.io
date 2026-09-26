#   Controllers - Misc
#### Standard Controllers
```
  SCPH-1010  digital joypad (with short cable)
  SCPH-1080  digital joypad (with longer cable)
  SCPH-1030  mouse (with short cable)
  SCPH-1090  mouse (with longer cable)
  SCPH-1092  mouse (european?)
  SCPH-1110  analog joystick
  SCPH-1150  analog joypad (with one vibration motor, with red/green led)
  SCPH-1180  analog joypad (without vibration motors, with red/green led)
  SCPH-1200  analog joypad (with two vibration motors) (dualshock)
  SCPH-110   analog joypad (with two vibration motors) (dualshock for psone)
  SCPH-10010 dualshock2 (analog buttons, except L3/R3/Start/Select) (for ps2)
  SCPH-1070  multitap
```

#### Special Controllers
```
  SCPH-4010 VPick (guitar-pick controller) (for Quest for Fame, Stolen Song)
```
SLPH-0001 (nejicon)<br/>
BANDAI "BANC-0002" - 4 Buttons (Triangle, Circle, Cross, Square) (nothing more)<br/>

#### Joystick
```
     __________                     __________
    |          |                   |    ^     |     ^
    | L1    R1 |                   | X <+> O  |    <+> = Digital Stick
     \      ___| <--- L2   [] ---> |___ v    /      v
      |    |     <--- R2   /\ --->     |    |
   ___|    |___________________________|    |___   Not sure if all buttons
  |   |    | SEL STA              =?=  |    |   |  are shown at their
  |   |    |                           |    |   |  correct locations?
  |   |    |_         []   /\         _|    |   |    (drawing is based on
  |  _|     /    L1             R1    \     |_  |    below riddle/lyrics)
  |  \_____/          X     O          \_____/  |
  |   /___\      L2             R2      /___\   |
  |                                             |
  |                                             |
   \___________________________________________/
```

```
 The thumb buttons on the left act as L1 and R1,
    the trigger is L2, the pinky button is R2
 The thumb buttons on the right act as X and O,
    the trigger is Square and the pinky button is Triangle.
 I find this odd as the triggers should've been L1 and R1,
    the pinkies L2 and R2.
 The buttons are redundantly placed on the base as large buttons like what
    you'd see on a fight/arcade stick. Also with Start and Select.
 There is also a physical analog mode switch,
    not a button like on dual shock.
```

#### MX4SIO
The MX4SIO is a homebrew microSD card adapter for the PS2 that plugs into a
memory card slot, taking advantage of the fact that SD cards support an SPI mode
which is more or less compatible with SIO0. The adapter is completely passive
and has the card wired up as follows:<br/>

| uSD pin | Name         | Wired to MC pin |
| ------: | :----------- | :-------------- |
|       1 | `D2`/`NC`    | -               |
|       2 | `D3`/`/CS`   | `/CS`           |
|       3 | `CMD`/`MOSI` | `CMD`/`MOSI`    |
|       4 | `VCC`        | `+3.5V`         |
|       5 | `SCK`        | `SCK`           |
|       6 | `GND`        | `GND`, `/ACK`   |
|       7 | `D0`/`MISO`  | `DAT`/`MISO`    |
|       8 | `D1`/`NC`    | -               |

Unfortunately, this design has a fatal flaw that makes it unusable as-is on the
PS1: /ACK is permanently shorted to ground, taking down the entire controller
bus. However, it should be possible to use the MX4SIO on a PS1 with custom
driver code once the MX4SIO's /ACK pin is masked out with some tape, or if no
other controllers or memory cards are plugged in.<br/>
Note that, as SD cards do not employ the addressing scheme used by standard
controllers and memory cards, the MX4SIO should get its own dedicated /CSn pin
and not share the port with a controller (i.e. if the MX4SIO is plugged in slot
2, then controller port 2 shall be left unused).<br/>
