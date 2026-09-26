#   Controllers - Configuration Commands
Some controllers can be switched from Normal Mode to Config Mode. The Config
Mode was invented for activating the 2nd rumble motor in SCPH-1200 analog
joypads. Additionally, the Config commands can switch between analog/digital
inputs (without needing to manually press the Analog button), activate more
analog inputs (on Dualshock2), and read some type/status bytes.<br/>

#### Normal Mode
```
  42h "B" Read Buttons (and analog inputs when in analog mode)
  43h "C" Enter/Exit Configuration Mode (stay normal, or enter)
```
Transfer length in Normal Mode is 5 bytes (Digital mode), or 9 bytes (Analog
mode), or up to 21 bytes (Dualshock2).<br/>

#### Configuration Mode
```
  40h "@" Unused, or Dualshock2: Get/Set ButtonAttr?
  41h "A" Unused, or Dualshock2: Get Reply Capabilities
  42h "B" Read Buttons AND analog inputs (even when in digital mode)
  43h "C" Enter/Exit Configuration Mode (stay config, or exit)
  44h "D" Set LED State (analog mode on/off)
  45h "E" Get LED State (and Type/constants)
  46h "F" Get Variable Response A (depending on incoming bit)
  47h "G" Get whatever values (response HiZ F3h 5Ah 00h 00h 02h 00h 01h 00h)
  48h "H" Unknown (response HiZ F3h 5Ah 00h 00h 00h 00h 01h 00h)
  49h "I" Unused
  4Ah "J" Unused
  4Bh "K" Unused
  4Ch "L" Get Variable Response B (depending on incoming bit)
  4Dh "M" Get/Set RumbleProtocol
  4Eh "N" Unused
  4Fh "O" Unused, or Dualshock2: Set ReplyProtocol
```
Transfer length in Config Mode is always 9 bytes.<br/>

#### Normal Mode - Command 42h "B" - Read Buttons (and analog inputs when enabled)
```
  Send  01h 42h 00h xx  yy  (00h 00h 00h 00h) (...)
  Reply HiZ id  5Ah buttons ( analog-inputs ) (dualshock2 buttons...)
```
The normal read command, see Standard Controller chapter for details on buttons
and analog inputs. The xx/yy bytes have effect only if rumble is unlocked; use
Command 43h to enter config mode, and Command 4Dh to unlock rumble. Command 4Dh
has billions of combinations, among others allowing to unlock only one of the
two motors, and to exchange the xx/yy bytes, however, with the default values,
xx/yy are assigned like so:<br/>
```
  yy.bit0-7 ---> Left/Large Motor M1 (analog slow/fast) (00h=stop, FFh=fastest)
  xx.bit0   ---> Right/small Motor M2 (digital on/off)  (0=off, 1=on)
```
The Left/Large motor starts spinning at circa min=50h..60h, and, once when
started keeps spinning downto circa min=38h. The exact motor start boundary
depends on the current position of the weight (if it's at the "falling" side,
then gravity helps starting), and also depends on external movements (eg. it
helps if the user or the other rumble motor is shaking the controller), and may
also vary from controller to controller, and may also depend on the room
temperature, dirty or worn-out mechanics, etc.<br/>

#### Normal Mode - Command 43h "C" - Enter/Exit Configuration Mode
```
  Send  01h 43h 00h xx  00h (zero padded...)   (...)
  Reply HiZ id  5Ah buttons (analog inputs...) (dualshock2 buttons...)
```
When issuing command 43h from inside normal mode, the response is same as for
command 42h (button data) (and analog inputs when in analog mode) (but without
M1 and M2 parameters). While in config mode, the ID bytes are always "F3h 5Ah"
(instead of the normal analog/digital ID bytes).<br/>
```
  xx=00h Stay in Normal mode
  xx=01h Enter Configuration mode
```
Caution: Additionally to activating configuration commands, entering config
mode does also activate a Watchdog Timer which does reset the controller if
there's been no communication for about 1 second or so. The watchdog timer
remains active even when returning to normal mode via Exit Config command. The
reset does disable and lock rumble motors, and switches the controller to
Digital Mode (with LED=off, and analog inputs disabled). To prevent this, be
sure to keep issuing joypad reads even when not needing user input (eg. while
loading data from CDROM).<br/>
Caution 2: A similar reset occurs when the user pushes the Analog button; this
is causing rumble motors to be stopped and locked, and of course, the
analog/digital state gets changed.<br/>
Caution 3: If config commands were used, and the user does then push the analog
button, then the 5Ah-byte gets replaced by 00h (ie. responses change from "HiZ
id 5Ah ..." to "HiZ id 00h ...").<br/>

#### Config Mode - Command 42h "B" - Read Buttons AND analog inputs
```
  Send  01h 42h 00h M2  M1  00h 00h 00h 00h
  Reply HiZ F3h 5Ah buttons  analog-inputs
```
Same as command 42h in normal mode, but with forced analog response (ie. analog
inputs and L3/R3 buttons are returned even in Digital Mode with LED=Off).<br/>

#### Config Mode - Command 43h "C" - Enter/Exit Configuration Mode
```
  Send  01h 43h 00h xx  00h 00h 00h 00h 00h
  Reply HiZ F3h 5Ah 00h 00h 00h 00h 00h 00h
```
Equivalent to command 43h in normal mode, but returning 00h bytes rather than
button data, can be used to return to normal mode.<br/>
```
  xx=00h Enter Normal mode (Exit Configuration mode)
  xx=01h Stay in Configuration mode
```
Back in normal mode, the rumble motors (if they were enabled) can be controlled
with normal command 42h.<br/>

#### Config Mode - Command 44h "D" - Set LED State (analog mode on/off)
```
  Send  01h 44h 00h Led Key 00h 00h 00h 00h
  Reply HiZ F3h 5Ah 00h 00h Err 00h 00h 00h
```
The Led byte can be:<br/>
```
  When Led=00h      --> Digital mode, with LED=Off
  When Led=01h      --> Analog mode, with LED=On/red
  When Led=02h..FFh --> Ignored (and, in case of dualshock2: set Err=FFh)
```
The Key byte can be:<br/>
```
  When Key=00h..02h --> Unlock (allow user to push Analog button)
  When Key=03h      --> Lock (stay in current mode, ignore Analog button)
  When Key=04h..FFh --> Acts same as (Key AND 03h)
```
The Err byte is usually 00h (except, Dualshock2 sets Err=FFh upon Led=02h..FFh;
older PSX/PSone controllers don't do that).<br/>

#### Config Mode - Command 45h "E" - Get LED State (and Type/constants)
```
  Send  01h 45h 00h 00h 00h 00h 00h 00h 00h
  Reply HiZ F3h 5Ah Typ 02h Led 02h 01h 00h
```
Returns two interesting bytes:<br/>
```
  Led: Current LED State (00h=Off, 01h=On/red)
  Typ: Controller Type (01h=PSX/Analog Pad, 03h=PS2/Dualshock2)
```
The other bytes might indicate the number of rumble motors, analog sticks, or
version information, or so.<br/>

#### Config Mode - Command 46h "F" - Get Variable Response A
```
  Send  01h 46h 00h ii  00h 00h 00h 00h 00h
  Reply Hiz F3h 5Ah 00h 00h cc  dd  ee  ff
```
When ii=00h --\> returns cc,dd,ee,ff = 01h,02h,00h,0ah<br/>
When ii=01h --\> returns cc,dd,ee,ff = 01h,01h,01h,14h<br/>
Otherwise --\> returns cc,dd,ee,ff = all zeroes<br/>
Note: This is called PadInfoAct in official docs, ii is the actuator (aka
motor) and the last response byte contains its current drain (10 or 20 units).
Whereas, Sony inisits that controllers should never exceed 60 units (eg. when
having more than 2 joypads connected to multitaps).<br/>

#### Config Mode - Command 47h "G" - Get whatever values
```
  Send  01h 47h 00h 00h 00h 00h 00h 00h 00h
  Reply HiZ F3h 5Ah 00h 00h 02h 00h 01h 00h
```
Purpose unknown.<br/>

#### Config Mode - Command 4Ch "L" - Get Variable Response B
```
  Send  01h 4Ch 00h ii  00h 00h 00h 00h 00h
  Reply Hiz F3h 5Ah 00h 00h 00h dd  00h 00h
```
When ii=00h --\> returns dd=04h.<br/>
When ii=01h --\> returns dd=07h.<br/>
Otherwise --\> returns dd=00h.<br/>

#### Config Mode - Command 48h "H" - Unknown (response HiZ F3h 5Ah 4x00h 01h 00h)
```
  Send  01h 48h 00h ii  00h 00h 00h 00h 00h
  Reply HiZ F3h 5Ah 00h 00h 00h 00h ee  00h
```
When ii=00h..01h --\> returns ee=01h.<br/>
Otherwise --\> returns ee=00h.<br/>
Purpose unknown. The command does not seem to be used by any games.<br/>

#### Config Mode - Command 4Dh "M" - Get/Set RumbleProtocol
[Controllers - Vibration/Rumble Control](controllers-vibration-rumble-control.md#controllers-vibrationrumble-control)<br/>

#### Config Mode - Command 40h "@" Dualshock2: Get/Set ButtonAttr?
#### Config Mode - Command 41h "A" Dualshock2: Get Reply Capabilities
#### Config Mode - Command 4Fh "O" Dualshock2: Set ReplyProtocol
[Controllers - Analog Buttons (Dualshock2)](controllers-analog-buttons-dualshock2.md#controllers-analog-buttons-dualshock2)<br/>

#### Config Mode - Command 49h "I" - Unused
#### Config Mode - Command 4Ah "J" - Unused
#### Config Mode - Command 4Bh "K" - Unused
#### Config Mode - Command 4Eh "N" - Unused
#### Config Mode - Command 40h "@" - Unused (except, used by Dualshock2)
#### Config Mode - Command 41h "A" - Unused (except, used by Dualshock2)
#### Config Mode - Command 4Fh "O" - Unused (except, used by Dualshock2)
```
  Send  01h 4xh 00h 00h 00h 00h 00h 00h 00h
  Reply HiZ F3h 5Ah 00h 00h 00h 00h 00h 00h
```
These commands do return a bunch of 00h bytes. These commands do not seem to be
used by any games (apart from the Dualshock2 commands being used by Dualshock2
games).<br/>

#### Note
Something called "Guitar Hero controller" does reportedly also support Config
commands. Unknown if that thing does have the same inputs & rumble motors
as normal analog PSX joypads, and if it does return special type values.<br/>
