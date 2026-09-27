#   Controllers - Keyboards
There isn't any official retail keyboard for PSX, however, there is a shitload
of obscure ways to connect keyboards...<br/>

#### Sony SCPH-2000 PS/2 Keyboard/Mouse Adaptor (prototype/with cable) (undated)
#### Sony SCPH-2000 PS/2 Keyboard/Mouse Adaptor (without cable) (undated)
A PS/2 to PSX controller port adaptor. Maybe for educational Lightspan titles?<br/>
There are two hardware variants of the adaptor:<br/>
```
  Adaptor with short cable to PSX-controller port (and prototype marking)
  Adaptor without cable, directly plugged into controller port (final version?)
```
Unknown ^how to access those adaptors, and unknown if the two versions differ
at software side. There seem to be not much more than a handful of people
owning that adaptors, and none of them seems to know how to use it, or even how
to test if it's working with existing software...<br/>
- Keyboard reading might work with the Online Connection CD.<br/>
- Mouse reading might work with normal mouse compatible PSX games.<br/>

#### Lightspan Online Connection CD Keyboard (1997)
The Online Connection CD is a web browser from the educational Lightspan
series, the CD is extremly rare (there's only one known copy of the disc).<br/>
The thing requires a dial-up modem connected to the serial port (maybe simply
using the same RS232 adaptor as used by Yaroze). User input can be done via
joypad, or optionally, via some external keyboard (or keyboard adaptor)
hardware:<br/>
```
  Send  01h 42h 00h 00h 00h 00h 00h 00h 00h 00h 00h 00h 00h 00h 06h
  Reply HiZ 96h 5Ah num dat dat dat dat dat dat dat dat dat dat dat
```
The num byte indicates number of following scancodes (can be num=FFh, maybe
when no keyboard connected?, or num=00h..0Bh for max 11 bytes, unless the last
some bytes should have other meaning, like status/mouse data or so).<br/>
The keyboard scancodes are in "PS/2 Keyboard Scan Code Set 2" format.<br/>
The binary contains some (unused) code for sending data to the keyboard by
changing the 4th-11th byte, and resuming normal operation by setting 4th and
11th byte back to zero:<br/>
```
  Send  ..  ..  ..  01h xxh FFh FFh FFh FFh FFh 00h ..  ..  ..  ..
  Send  ..  ..  ..  00h ..  ..  ..  ..  ..  ..  00h ..  ..  ..  ..
```
Maybe 4th and 11th byte are number of following bytes, with xxh being some
command, and FFh's just being bogus padding; the xxh looks more like an
incrementing value though.<br/>
Despite of the mouse-based GUI, the browser software doesn't seem to support
mouse hardware (neither via PS/2 mice, nor PSX mice). Instead, the mouse arrow
can be merely moved via joypad's DPAD, or (in a very clumsy fashion) via
keyboard cursor keys.<br/>
Note: The browser uses SysEnqIntRP to install some weird IRQ handler that
forcefully aborts all controller (or memory card) transfers upon Vblank.
Unknown if that's somehow required to bypass bugs in the keyboard hardware. The
feature is kinda dangerous for memory card access (especially with fast memcard
access in nocash kernel, which allows to transfer more than one sector per
frame).<br/>

#### Spectrum Emulator Keyboard Adaptor (v1/serial port) (undated)
Made by Anthony Ball. [http://www.sinistersoft.com/psxkeyboard]

```
  [1F801058h]=00CEh  ;SIO1_MR 8bit, no parity, 2 stop bits (8N2)
  [1F80105Ah]=771Ch  ;SIO1_CR rx enable (plus whatever nonsense bits)
  [1F80105Eh]=006Ch  ;SIO1_BR 19200 bps
  RX   Keyboard Scancode (same ASCII-style as in later versions?)
  CTS  Caps-Lock state
  DSR  Num-Lock state
```

#### Spectrum Emulator Keyboard & Sega Sticks Adaptor (v2/controller port) (2000)
Made by Anthony Ball. [http://www.sinistersoft.com/psxkeyboard]

This adaptor can send pad/stick data,<br/>
```
  Send  01h 42h 00h  0h 0h
  Reply HiZ 41h 5Ah  PadA
```
as well as pad/sticks+keyboard data,<br/>
```
  Send  01h 42h 00h  0h 0h 0h 0h 0h 0h 0h 0h  00h 00h   0h 0h 0h 0h 0h 0h
  Reply HiZ E8h 5Ah  PadA  PadB  PadC  PadD   Ver Lock  Buffer(0..5)
```
The above mode(s) can be switched via ACPI Power/Sleep/Wake keys (on keyboards
that do have such keys).<br/>
```
  Version=1     ; version number
  0  SCROLL          ; scroll lock on
  1  NUM             ; num lock on
  2  CAPS            ; caps lock on
  3  DONETEST        ; keyboard has just done a selftest
  4  EMUA            ; emulation mode a
  5  EMUB            ; emulation mode b
```
For whatever reason, the PS/2 scancodes are translated to ASCII-style scancode
values (with bit7=KeyUp flag):<br/>
```
  01   11 12 13 14  15 16 17 18  19 1A 1B 1C  1D 69 1F
  60 21 22 68 24 25 5E 26 2A 28 29 5F 3D  2D  0B 0E 0F  67 2F 1E 2D
  27  51 57 45 52 54 59 55 49 4F 50 5B 5D 0D  10 61 62  37 38 39
  3B   41 53 44 46 47 48 4A 4B 4C 3A 40 23              34 35 36 2B
  02 5C 5A 58 43 56 42 4E 4D 3C 3E 3F     03     63     31 32 33
  04 05 06           20          07 08 09 0A  65 64 66  30    2E 6A
```
BUG: The thing conflicts with memory cards: It responds to ANY byte with value
01h (it should do so only if the FIRST byte is 01h).<br/>

#### Homebrew PS/2 Keyboard/Mouse Adaptor (undated/from PSone era)
```
  Send  01h 42h 00h 00h 00h 00h 00h
  Reply HiZ 12h 5Ah key flg dx  dy
```
flg:<br/>
```
  bit0-1 = Always 11b (unlike Sony mouse)
  bit2 = Left Mouse Button  (0=Pressed, 1=Released)
  bit3 = Right Mouse Button (0=Pressed, 1=Released)
  bit4-5 = Always 11b (like Sony mouse)
  bit6 = Key Release  (aka F0h prefix) (0=Yes)
  bit7 = Key Extended (aka E0h prefix) (0=Yes)
```
Made by Simon Armstrong. This thing emulates a standard PSX Mouse (and should
thus work with most or all mouse compatible games). Additionally, it's sending
keyboard flags/scancodes via unused mouse button bits.<br/>

#### Runix hardware add-on USB Keyboard/Mouse Adaptor (2001) (PIO extension port)
Runix is a homebrew linux kernel for PSX, it can be considered being the holy
grail of the open source scene because nobody has successfully compiled it in
the past 16 years.<br/>
- USB host controller SL811H driver with keyboard and mouse support;<br/>
- RTC support.<br/>
file: drivers/usb/sl811h.c<br/>

#### TTY Console
The PSX kernel allows to output "printf" debug messages via stdout. In the
opposite direction, it's supporting to receive ASCII user input via
"std\_in\_gets" (there isn't any software actually using that feature though,
except maybe debug consoles like DTL-H2000).<br/>
