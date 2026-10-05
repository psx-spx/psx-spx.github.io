#   PS2 DVD Remote
An accessory released by Sony for the PS2, consisting of an infrared remote
control and a receiver dongle that plugs into a controller port. The remote
features all standard controller buttons (including L3/R3) as well as additional
controls for the PS2's DVD player.<br/>
The receiver behaves very differently from any other known device: it does not
respond to any command until a button on the remote is pressed. When a valid IR
code is received it will start accepting commands for about 2000-2500 ms, then
become unresponsive again. It will initially behave as two different devices,
one with address 01h acting like a standard digital controller and the other
with address 61h exposing IR codes as received from the remote.<br/>

#### Command 04h - IR poll (and disable controller mode)
```
  Send Reply Comment
  61h  N/A   IR receiver address
  04h  12h   Receive ID bits 0-7, send command byte
  00h  5Ah   Receive ID bits 8-15
  00h  len   Receive code length (20 for DVD remote, 0 if no button is pressed)
  00h  code  Receive code bits 16-23
  00h  code  Receive code bits 8-15
  00h  code  Receive code bits 0-7
```
Returns the IR code of the currently pressed button and its length in bits, or
000000h if no button is pressed (and the receiver is still responding to
commands). Received codes seem to "stick around" for some time even after the
button has been released; when a button is held down the remote resends its code
every 45 ms, so the receiver presumably keeps returning the same code for about
50 ms as a debouncing measure.<br/>
The code is returned LSB first and MSB aligned, i.e. it should be right-shifted
by (24 - len) bits to obtain the "raw" code as sent by the remote. For
instance:<br/>
```
  Code sent by remote (first bit after preamble to last bit):
    0000 0000 1011 1001 0010
  Code sent by remote (MSB to LSB):
    0100 1001 1101 0000 0000
  Data returned by receiver:
    code[16:23] = 01001001
    code[8:15]  = 11010000
    code[0:7]   = 0000xxxx ; xxxx = (24 - len) bits of padding (all zeroes)
  Reassembled MSB-aligned code (MSB to LSB):
    0100 1001 1101 0000 0000 xxxx
```
The receiver will stop acting like a digital controller and replying to address
01h after this command is sent for the first time. Command 06h can be used to
restore controller functionality (see below), unknown if there is also a
watchdog to automatically restore controller mode if no IR poll commands are
issued.<br/>

#### Command 06h, 03h - Re-enable controller mode
```
  Send Reply Comment
  61h  N/A   IR receiver address
  06h  12h   Receive ID bits 0-7, send command byte 1
  03h  5Ah   Receive ID bits 8-15, send command byte 2
  00h  ?     Receive unknown data, send padding
  00h  ?
  00h  ?
  00h  ?
```

#### Command 0Fh - Unknown
This command exists (the receiver will keep pulling /ACK low) but its purpose is
currently unknown. It could possibly be an alternate poll command that does not
disable controller mode.<br/>

#### IR code format
The DVD remote always emits 20-bit IR codes. The receiver does return the length
of the code, but it's unclear if it can receive codes with lengths other than 20
bits.<br/>
All non-controller buttons on the remote are arranged in an 8x16 button matrix,
shown below (transposed for readability):<br/>

| Col | Row 0  | Row 1    | Row 2  | Row 3    | Row 4 | Row 5   | Row 6    | Row 7 |
| --: | :----- | :------- | :----- | :------- | :---- | :------ | :------- | :---- |
|   0 | 1      |          |        | Previous |       |         | Slow <<  |       |
|   1 | 2      |          |        | Next     |       |         | Slow >>  |       |
|   2 | 3      |          |        | Play     |       |         |          |       |
|   3 | 4      |          |        | Scan <<  |       |         | Subtitle |       |
|   4 | 5      |          |        | Scan >>  |       | Display | Audio    |       |
|   5 | 6      |          |        | Shuffle  |       |         | Angle    |       |
|   6 | 7      |          |        |          |       |         |          |       |
|   7 | 8      |          |        |          |       |         |          |       |
|   8 | 9      |          | Time   | Stop     |       |         |          |       |
|   9 | 0      |          |        | Pause    |       |         |          | Up    |
|  10 |        | Title    | A<->B  |          |       |         |          | Down  |
|  11 | Enter  | DVD Menu |        |          |       |         |          | Left  |
|  12 |        |          | Repeat |          |       |         |          | Right |
|  13 |        |          |        |          |       |         |          |       |
|  14 | Return |          |        |          |       |         |          |       |
|  15 | Clear  | Program  |        |          |       |         |          |       |

Each button in the matrix is assigned a code as follows:<br/>
```
  code = 49D00h OR (row << 4) OR (column) ; sent LSB first

  ; where row = 0..7, column = 0..15
```
Controller buttons are handled separately and assigned different codes:<br/>
```
  code = DAD50h OR (id) ; sent LSB first

  ; where id = 0..15, index of the bit that would normally represent the button
  ; in the bitfield returned by a controller poll command
  ; (i.e. 0=Select, 1=L3, 2=R3, 3=Start, 4=Up, 5=Right, etc.)
```
Arrow buttons are a special case, as they are controller buttons but also have
matrix codes assigned. For those the remote alternates between both codes (see
below).<br/>

#### Low-level IR protocol
The remote emits IR pulses modulated with a 38 kHz carrier, as most remotes do.
Codes are sent as a 2460 µs "preamble" pulse followed by 24 data pulses, each of
which can be either 1250 µs (if the respective bit is 1) or 650 µs (if the
respective bit is 0) long. After each pulse including the preamble, the remote
waits 530 µs before sending the next pulse.<br/>
Every code is always sent at least 3 times in a row (more if the button is held
down but not necessarily a multiple of 3), approximately every 45 ms. For arrow
buttons the matrix code is sent 3 times first, then the respective controller
button code is sent 3 times, then the sequence repeats until the button is
released (with the total number of codes sent always being a multiple of 6 in
this case).<br/>

#### Built-in IR receivers
In later PS2 models, Sony integrated the IR receiver into the console. Assuming
the built-in receivers used the same circuitry as the external dongle, this may
explain its weird behavior: the receiver was likely designed to be wired in
parallel with one of the controller ports, and to be unresponsive until the
remote is actually in use to avoid interfering with another controller plugged
into the same port. Whether or not the integrated receivers are connected this
way has not been confirmed.<br/>
There is a second revision of the DVD remote with power and eject buttons, meant
to be used with the PS2 models that have a built-in receiver. Weirdly enough,
however, it seems to be incompatible with the older receiver dongle.<br/>
