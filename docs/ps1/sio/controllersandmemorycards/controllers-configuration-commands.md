#   Configuration Commands
Some controllers can be switched from Normal Mode to Config Mode. The Config
Mode was invented for activating the 2nd rumble motor in SCPH-1200 analog
joypads. Additionally, the Config commands can switch between analog/digital
inputs (without needing to manually press the Analog button), activate more
analog inputs (on Dualshock2), and let software query which modes and
actuators the controller supports. Sony calls these "extended protocol"
controllers. The PS2 kept the same protocol and only added the Dualshock2
analog button commands.<br/>

Sony's PS1 documentation does not name the raw command bytes, only the libpad
functions built on them. The command names below are the ones used by the PS2
IOP controller driver (padman), with the corresponding PS1 libpad function in
brackets where one exists.<br/>

#### Normal Mode
```
  42h  ReadData           Read Buttons (and analog inputs when in analog mode)
  43h  EnterConfigMode    Enter Configuration Mode (or stay in normal mode)
```
Transfer length in Normal Mode is 5 bytes (Digital mode), or 9 bytes (Analog
mode), or up to 21 bytes (Dualshock2).<br/>

#### Configuration Mode
```
  40h  VrefParam          Dualshock2 only: set analog button parameter
  41h  QueryButtonMask    Dualshock2 only: get selectable reply bytes
  42h  ReadData           Read Buttons AND analog inputs (even in digital mode)
  43h  ExitConfigMode     Exit Configuration Mode (or stay in config mode)
  44h  SetMainMode        Set analog/digital mode and lock    (PadSetMainMode)
  45h  QueryModel         Get model and number of modes/actuators
  46h  QueryAct           Get actuator info                   (PadInfoAct)
  47h  QueryComb          Get actuator combination list       (PadInfoComb)
  48h  -                  Not used by any library, see below
  49h  -                  Unused
  4Ah  -                  Unused
  4Bh  -                  Continuation of QueryComb (used by libpad)
  4Ch  QueryMode          Get mode ID table entry             (PadInfoMode)
  4Dh  SetActAlign        Map actuators to ReadData bytes     (PadSetActAlign)
  4Eh  -                  Unused
  4Fh  SetButtonInfo      Dualshock2 only: select ReadData reply bytes
```
Transfer length in Config Mode is always 9 bytes.<br/>

#### Normal Mode - Command 42h - ReadData
```
  Send  01h 42h 00h xx  yy  (00h 00h 00h 00h) (...)
  Reply HiZ id  5Ah buttons ( analog-inputs ) (dualshock2 buttons...)
```
The normal read command, see Standard Controller chapter for details on buttons
and analog inputs. The xx/yy bytes have effect only if rumble is unlocked; use
Command 43h to enter config mode, and Command 4Dh to map the actuators to these
bytes. With the usual mapping, xx/yy are assigned like so:<br/>
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
When using libpad, the motor values may additionally be forced to 00h by the
library's current limiter, see
[Vibration/Rumble Control](controllers-vibration-rumble-control.md#vibrationrumble-control).<br/>

#### Normal Mode - Command 43h - EnterConfigMode
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
Controllers without config mode don't enter it (eg. the SCPH-1180 stops
acknowledging after the ID byte), which is how software tells them apart from
extended protocol controllers.<br/>
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

#### Config Mode - Command 42h - ReadData
```
  Send  01h 42h 00h M2  M1  00h 00h 00h 00h
  Reply HiZ F3h 5Ah buttons  analog-inputs
```
Same as command 42h in normal mode, but with forced analog response (ie. analog
inputs and L3/R3 buttons are returned even in Digital Mode with LED=Off).<br/>

#### Config Mode - Command 43h - ExitConfigMode
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

#### Config Mode - Command 44h - SetMainMode
```
  Send  01h 44h 00h Mode Lock 00h 00h 00h 00h
  Reply HiZ F3h 5Ah 00h  00h  Err 00h 00h 00h
```
Mode is an index into the controller's mode ID table (see Command 4Ch). On
analog pads that table is {Digital, Analog}, so:<br/>
```
  When Mode=00h      --> Digital mode, with LED=Off
  When Mode=01h      --> Analog mode, with LED=On/red
  When Mode=02h..FFh --> Ignored (and, in case of dualshock2: set Err=FFh)
```
The Lock byte can be:<br/>
```
  When Lock=00h..02h --> Unlock (allow user to push Analog button)
  When Lock=03h      --> Lock (stay in current mode, ignore Analog button)
  When Lock=04h..FFh --> Acts same as (Lock AND 03h)
```
The Err byte is usually 00h (except, Dualshock2 sets Err=FFh upon
Mode=02h..FFh; older PSX/PSone controllers don't do that).<br/>
libpad's PadSetMainMode(port, offs, lock) sends this command with offs and
lock as given, followed by Command 4Dh re-sending the previously set actuator
alignment.<br/>

#### Config Mode - Command 45h - QueryModel
```
  Send  01h 45h 00h 00h 00h  00h  00h  00h  00h
  Reply HiZ F3h 5Ah Typ Modes Cur Acts Comb 00h
```
```
  Typ   Controller Type (01h=PSX/Analog Pad, 03h=PS2/Dualshock2)
  Modes Number of entries in the mode ID table (02h)        (see Command 4Ch)
  Cur   Index of the current mode in that table (00h=Digital, 01h=Analog)
  Acts  Number of actuators (02h)                           (see Command 46h)
  Comb  Number of actuator combination lists (01h)          (see Command 47h)
```
The values in brackets are those returned by SCPH-1200, SCPH-110 and Dualshock2 pads.
Because the analog pad's mode table is {Digital, Analog}, the Cur byte doubles
as the LED state. libpad uses Modes, Acts and Comb to size its tables, and
PadSetMainMode only accepts mode indices below Modes.<br/>

#### Config Mode - Command 46h - QueryAct
```
  Send  01h 46h 00h ii  00h 00h 00h 00h 00h
  Reply Hiz F3h 5Ah 00h 00h Func Sub Size Curr
```
Returns information about actuator number ii (00h..Acts-1). libpad's
PadInfoAct(port, actuator, term) returns these fields:<br/>
```
  Func      bit0-7   InfoActFunc  Actuator function (01h on both motors)
  Sub       bit0-6   InfoActSub   Function sub-type (02h=small, 01h=large motor)
  Sub       bit7     InfoActSign  Stop value flag (0 on both motors, 00h=stop)
  Size      bit0-7   InfoActSize  Parameter size (00h=1 bit on/off, 01h..=bytes)
  Curr      bit0-7   InfoActCurr  Maximum current drain (1 unit = 10mA)
```
SCPH-1200, SCPH-110 and Dualshock2 pads return:<br/>
```
  ii=00h  Func=01h Sub=02h Size=00h Curr=0Ah  Right/small motor, on/off, 10 units
  ii=01h  Func=01h Sub=01h Size=01h Curr=14h  Left/large motor, 1 byte, 20 units
  ii=02h..FFh  all zeroes
```
The actuator numbers are the values used in the Command 4Dh mapping (00h=small
motor, 01h=large motor). The Curr values are what libpad's current limiter adds
up, see
[Vibration/Rumble Control](controllers-vibration-rumble-control.md#vibrationrumble-control).
libpad.h defines the console's limit as PadMaxCurr=60 units, and the SCPH-1150
motor (which can't be queried) as PadCurrCTP1=10 units.<br/>

#### Config Mode - Command 47h - QueryComb
```
  Send  01h 47h 00h ii  00h 00h 00h 00h 00h
  Reply HiZ F3h 5Ah 00h 00h Num A0  A1  00h
```
Returns actuator combination list number ii (00h..Comb-1): Num is the number
of actuators in the list, followed by the actuator numbers. SCPH-1200, SCPH-110
and Dualshock2 pads have one list, Num=02h with actuators 00h and 01h; for ii=01h
and up they return all zeroes. libpad's PadInfoComb(port, list, offs) returns
Num for offs=-1 and the actuator numbers for offs=0 and up. When a list has
more entries than fit in the reply, libpad reads the remainder with Command
4Bh.<br/>

#### Config Mode - Command 4Bh - QueryComb continuation
```
  Send  01h 4Bh 00h 00h 00h 00h 00h 00h 00h
  Reply HiZ F3h 5Ah 00h 00h 00h 00h 00h 00h
```
Sent by libpad without parameters after Command 47h, when the combination
list has more than three entries. No known controller has such a list, and
SCPH-1200, SCPH-110 and Dualshock2 pads return 00h bytes.<br/>

#### Config Mode - Command 4Ch - QueryMode
```
  Send  01h 4Ch 00h ii  00h 00h  00h  00h 00h
  Reply Hiz F3h 5Ah 00h 00h IdHi IdLo 00h 00h
```
Returns entry ii (00h..Modes-1) of the controller's mode ID table, as a 16bit
value. The IDs are the controller type nibble of the normal mode ID byte
(bit4-7 of the 41h or 73h byte returned in normal mode):<br/>
```
  ii=00h  ID=0004h  Digital mode (ID byte 41h)
  ii=01h  ID=0007h  Analog mode  (ID byte 73h)
  ii=02h..FFh  ID=0000h
```
libpad's PadInfoMode(port, term, offs) returns this table with
term=InfoModeIdTable (offs=-1 returns the number of entries), and the entry
for the current mode with term=InfoModeCurExID.<br/>

#### Config Mode - Command 48h
```
  Send  01h 48h 00h ii  00h 00h 00h 00h 00h
  Reply HiZ F3h 5Ah 00h 00h 00h 00h ee  00h
```
When ii=00h..01h --\> returns ee=01h.<br/>
Otherwise --\> returns ee=00h.<br/>
Neither the PS1 libpad nor the PS2 padman driver sends this command, and no game is known to use
it.<br/>

#### Config Mode - Command 4Dh - SetActAlign
[Vibration/Rumble Control](controllers-vibration-rumble-control.md#vibrationrumble-control)<br/>

#### Config Mode - Command 40h - VrefParam (Dualshock2)
#### Config Mode - Command 41h - QueryButtonMask (Dualshock2)
#### Config Mode - Command 4Fh - SetButtonInfo (Dualshock2)
[Analog Buttons (Dualshock2)](controllers-analog-buttons-dualshock2.md#analog-buttons-dualshock2)<br/>

#### Config Mode - Commands 49h, 4Ah, 4Eh - Unused
#### Config Mode - Commands 40h, 41h, 4Fh - on PSX/PSone pads
```
  Send  01h 4xh 00h 00h 00h 00h 00h 00h 00h
  Reply HiZ F3h 5Ah 00h 00h 00h 00h 00h 00h
```
These commands do return a bunch of 00h bytes. They are not used by any games
(apart from the Dualshock2 commands being used by Dualshock2 games).<br/>

#### libpad initialization sequence
When libpad finds a controller that acknowledges command 43h, it reads the
controller's capabilities before reporting it as ready. PadGetState() returns
PadStateReqInfo (4) while the queries below are in progress, and
PadStateStable (6) once they are done.<br/>
```
  43h 01h       EnterConfigMode
  45h           QueryModel (number of modes, current mode, actuators, lists)
  4Ch Cur       QueryMode for the current mode
  47h ii        QueryComb for each list, to size the tables
  4Ch ii        QueryMode for each mode
  46h ii        QueryAct for each actuator
  47h ii        QueryComb for each list (plus 4Bh for long lists)
  43h 00h       ExitConfigMode
```
Each query in the last three steps is repeated until two consecutive replies
are identical. libpad never sends 44h or 4Dh on its own; those are only sent
when the game calls PadSetMainMode or PadSetActAlign.<br/>

#### Note
Something called "Guitar Hero controller" does reportedly also support Config
commands. Unknown if that thing does have the same inputs & rumble motors
as normal analog PSX joypads, and if it does return special type values.<br/>
