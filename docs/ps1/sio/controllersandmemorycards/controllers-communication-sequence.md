#   Controllers - Communication Sequence
#### Controller Communication Sequence
```
  Send Reply Comment
  01h  Hi-Z  Controller address
  42h  idlo  Receive ID bit0..7 (variable) and Send Read Command (ASCII "B")
  TAP  idhi  Receive ID bit8..15 (usually/always 5Ah)
  MOT  swlo  Receive Digital Switches bit0..7
  MOT  swhi  Receive Digital Switches bit8..15
  --- transfer stops here for digital pad (or analog pad in digital mode) ---
  00h  adc0  Receive Analog Input 0 (if any) (eg. analog joypad or mouse)
  00h  adc1  Receive Analog Input 1 (if any) (eg. analog joypad or mouse)
  --- transfer stops here for analog mouse ----------------------------------
  00h  adc2  Receive Analog Input 2 (if any) (eg. analog joypad)
  00h  adc3  Receive Analog Input 3 (if any) (eg. analog joypad)
  --- transfer stops here for analog pad (in analog mode) -------------------
  --- transfer stops here for nonstandard devices (steering/twist/paddle) ---
```
The TAP byte should be usually zero, unless one wants to activate Multitap
(multi-player mode), for details, see<br/>
[Controller and Memory Card Multitap Adaptor](controller-and-memory-card-multitap-adaptor.md#controller-and-memory-card-multitap-adaptor)<br/>
The two MOT bytes are meant to control the rumble motors (for normal non-rumble
controllers, that bytes should be 00h), however, the MOT bytes have no effect
unless rumble is enabled via config commands, for details, see<br/>
[Controllers - Configuration Commands](controllers-configuration-commands.md#controllers-configuration-commands)<br/>
[Controllers - Vibration/Rumble Control](controllers-vibration-rumble-control.md#controllers-vibrationrumble-control)<br/>

#### Controller ID (Halfword Number 0)
```
  0-3  Number of following halfwords (01h..0Fh=1..15, or 00h=16 halfwords)
  4-7  Controller Type (or currently selected Controller Mode)
  8-15 Fixed (5Ah)
```
Known 16bit ID values are:<br/>
```
  xx00h=N/A                 (initial buffer value from InitPad BIOS function)
  5A12h=Mouse               (two button mouse)
  5A23h=NegCon              (steering twist/wheel/paddle)
  5A31h=Konami Lightgun     (IRQ10-type)
  5A41h=Digital Pad         (or analog pad/stick in digital mode; LED=Off)
  5A53h=Analog Stick        (or analog pad in "flight mode"; LED=Green)
  5A63h=Namco Lightgun      (Cinch-type)
  5A73h=Analog Pad          (in normal analog mode; LED=Red)
  5A7xh=Dualshock2          (with variable number of inputs enabled)
  5A79h=Dualshock2          (with all analog/digital inputs enabled)
  5A80h=Multitap            (multiplayer adaptor) (when activated)
  5A96h=Keyboard            (rare lightspan keyboard)
  5AE3h=Jogcon              (steering dial)
  5AE8h=Keyboard/Sticks     (rare homebrew keyboard/segasticks adaptor)
  5AF3h=Config Mode         (when in config mode; see rumble command 43h)
  FFFFh=High-Z              (no controller connected, pins floating High-Z)
```
The PS2 DVD remote receiver identifies as either 5A41h (i.e. a digital
controller) when polled using standard controller commands, or 5A12h when using
address 61h to access the IR functionality.<br/>
