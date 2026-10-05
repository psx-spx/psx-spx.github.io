#   Vibration/Rumble Control
Rumble (aka "Vibration Function") is basically controlled by two previously
unused bytes of the standard controller Read command.<br/>
There are two methods to control the rumble motors, the old method is very
simple (but supports only one motor), the new method envolves a bunch of new
configuration commands (and supports two motors).<br/>
```
  SCPH-1150  DualAnalog Pad with 1 motor                  ;-old rumble method
  SCPH-1200  DualAnalog Pad with 2 motors, PSX-design     ;\new rumble method
  SCPH-110   DualAnalog Pad with 2 motors, PSone-design   ;/
  SCPH-10010 DualAnalog Pad with 2 motors, PS2/Dualshock2 ;-plus analog buttons
  Blaze Scorpion Lightgun with rumble      ;\unknow how to control rumble
  Fishing controllers with rumble          ;/
  SCPH-1180 Analog Pad without rumble      ;-no config commands (43h gets ID byte, then no /ACK)
  SCPH-1110 Analog Stick without rumble    ;-unknow if there're config commands
```

#### Old Method, one motor, no config commands (SCPH-1150, SCPH-1200, SCPH-110)
The SCPH-1150 doesn't support any special config commands, instead, rumble is
solely done via the normal joypad read command:<br/>
```
  Send  01h 42h 00h xx  yy  (00h 00h 00h 00h)
  Reply HiZ id  5Ah buttons ( analog-inputs )
```
The rumble motor is simply controlled by three bits in the xx/yy bytes:<br/>
```
  xx --> must be 40h..7Fh            (ie. bit7=0, bit6=1) ;\switches motor on
  yy --> must be 01h,03h,...,FDh,FFh (ie. bit0=1)         ;/
```
The motor control is digital on/off (no analog slow/fast), recommended values
would be yyxx=0140h=on, and yyxx=0000h=off.<br/>
LED state is don't care (rumble works with led OFF, RED, and GREEN). In absence
of config commands, the LED can be controlled only manually (via Analog
button), the current LED state is implied in the controller "id" byte.<br/>
For backwards compatibility, the above old method does also work on SCPH-1200
and SCPH-110 (for controlling the right/small motor), alternately those newer
pads can use the config commands (for gaining access to both motors).<br/>

#### New Method, two motors, with config commands (SCPH-1200, SCPH-110)
For using the new rumble method, one must unlock the new rumble mode, for that
purpose Sony has invented a "slightly" overcomplicated protocol with not less
than 16 new commands (the rumble relevant commands are 43h and 4Dh, also,
command 44h may be useful for activating analog inputs by software, and, once
when rumble is unlocked, command 42h is used to control the rumble motors).
Anyways, here's the full command set...<br/>
[Configuration Commands](controllers-configuration-commands.md#configuration-commands)<br/>
And, the rumble-specific config command is described below...<br/>

#### Config Mode - Command 4Dh - SetActAlign
```
  Send  01h 4Dh 00h aa  bb  cc  dd  ee  ff     ;<-- set NEW aa..ff values
  Reply Hiz F3h 5Ah aa  bb  cc  dd  ee  ff     ;<-- returns OLD aa..ff values
```
Bytes aa,bb,cc,dd,ee,ff control the meaning of the 4th,5th,6th,7th,8th,9th
command byte in the controller read command (Command 42h).<br/>
```
  00h      = Map actuator 0, Right/small Motor (Motor M2) to bit0 of this byte
  01h      = Map actuator 1, Left/Large Motor (Motor M1) to bit0-7 of this byte
  02h..FEh = Map actuator 2..FEh (none exist on SCPH-1200/Dualshock2 pads)
  FFh      = Map nothing to this byte
```
In practice, one would usually send either one of these command/values:<br/>
```
  Send  01h 4Dh 00h 00h 01h FFh FFh FFh FFh    ;enable new method (two motors)
  Send  01h 4Dh 00h FFh FFh FFh FFh FFh FFh    ;disable motor control
```
Alternately, one could swap the motors by swapping values in aa/bb. Or one
could map the motors anywhere to cc/dd/ee/ff (this will increase the command
length in digital mode, hence changing digital mode ID from 41h to 42h or 43h).
Or, one could map further rumble motors or other outputs to the six bytes (if
any such controller would exist).<br/>
In the initial state, aa..ff are all FFh, and the controller does then use the
old rumble control method (with only one motor). However, that old method gets
disabled once when having messed with config commands (unknown if/how one can
re-enable the old method by software).<br/>
The values are actuator numbers as listed by Command 46h, whose Size field
tells how many bits/bytes of the mapped byte the actuator uses. libpad's
PadSetActAlign(port, data) sends this command (wrapped in 43h 01h / 43h 00h)
with the game's six bytes.<br/>

#### Actuator current limit (libpad)
The console can supply up to 60 units of current to all controllers combined
(libpad.h: PadMaxCurr=60; one unit is 10mA). Each actuator's maximum drain is
returned by Command 46h:<br/>
```
  SCPH-1150   motor              10 units   (no config mode, fixed in libpad)
  SCPH-1200   actuator 0, small  10 units
  SCPH-1200   actuator 1, large  20 units
```
So one SCPH-1200 with both motors on draws 30 units, and two such pads on a
Multi Tap already reach the limit. Sony's libpad enforces this in software,
once per frame, while building the 42h command for each controller:<br/>
```
  - The running total is cleared at the start of each vsync.
  - Controllers are processed in order: port 1 (Multi Tap slots A..D), then
    port 2, and within each controller by actuator number.
  - An actuator counts as "on" if any 42h byte mapped to it (via 4Dh) is
    nonzero (only bit0 is tested for actuators with Size=00h).
  - An "on" actuator is allowed if total+Curr <= 60, and then adds its full
    Curr to the total, whatever its speed value.
  - Otherwise, all 42h bytes mapped to it are sent as 00h for that frame.
  - Later actuators are still checked, so a smaller one may fit after a
    larger one was refused.
```
PadSetAct() never refuses a value and returns no error; the refused motors
just stay off. For SCPH-1150 pads, libpad charges 10 units when the two
old-method bytes would switch the motor on (xx=40h..7Fh, yy bit0 set), and
sends both bytes as 00h if that does not fit. In Sony's words: "If actuator
parameters are set so that the 60-unit limit is exceeded, the actuators
connected to the larger port numbers are ignored (they are forcibly stopped).
This is particularly important for applications that use Multi Taps."<br/>
The PS2 IOP controller driver (padman) has a similar check with the same 60
unit limit, but applies it to each controller separately.<br/>

#### Unknown Dualshock2 Vibration
Dualshock2 does reportedly have "two more levels of vibration", unknown what
that means and if it's used by any PSX or PS2 games... it might refer to the
small motor which usually has only 2 levels (on/off) and might have 4 levels
(fast/med/slow/off) on dualshock2... but, if so, it's unknown how to
control/unlock that feature.<br/>
Also, the PSone controller (SCPH-110) appear to have been released shortly
after Dualshock2, unknown if that means that it might have that feature, too.<br/>

#### Note
Rumble is a potentially annoying feature, so games that do support rumble
should also include an option to disable it.<br/>
