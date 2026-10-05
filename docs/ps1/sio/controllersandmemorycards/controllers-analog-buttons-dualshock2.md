#   Analog Buttons (Dualshock2)
Dualshock2 has three new commands (40h,41h,4Fh) for configuring analog buttons.
Additionally, Command 45h does return a different type byte for Dualshock2.<br/>
Dualshock2 is a PS2 controller. However, it can be also used with PSX games
(either by connecting the controller to a PSX console, or by playing a PSX game
on a PS2 console).<br/>
The analog button feature is reportedly rarely used by PS2 games (and there
aren't any PSX games known to use it).<br/>

#### Config Mode - Command 40h - VrefParam
```
  Send  01h 40h 00h Idx Val 00h 00h 00h 00h  ;<-- Set NEW Val, array[Idx]=Val
  Reply HiZ F3h 5Ah 00h 00h Val 00h 00h 00h  ;<-- Old Val (or FFh when Idx>0Bh)
```
Allows to change twelve values (with Idx=00h..0Bh, and Val=00h..03h), one
for each of the twelve analog buttons. Default is Val=02h. The PS2 IOP
controller driver (padman) sends this command for all twelve indices whenever
it enables the analog buttons, with values set by the game (padSetVrefParam).
The name suggests a reference level for each pressure sensor, but there is no
noticable difference between Val=0,1,2,3. It might have subtle effects on
things like...<br/>
```
  Digital button sensitivity, or Analog button sensitivity, or
  Analog button bit-depth/conversion speed, or something else?
```

#### Config Mode - Command 41h - QueryButtonMask
```
  Send  01h 41h 00h 00h 00h 00h 00h 00h 00h
  Reply HiZ F3h 5Ah FFh FFh 03h 00h 00h 00h
```
Returns a constant bitmask indicating which reply bytes can be enabled/disabled
via Command 4Fh (ie. 3FFFFh = 18 bits). The PS2 libpad uses it to detect
analog button support: padInfoPressMode() returns true only when the mask is
3FFFFh.<br/>

#### Config Mode - Command 4Fh - SetButtonInfo
```
  Send  01h 4Fh 00h aa  bb  cc  dd  ee  ff
  Reply HiZ F3h 5Ah 00h 00h 00h 00h 00h 00h
```
This can output some 48bit value (bit0=aa.bit0, bit47=ff.bit7), used to
enable/disable Reply bytes in the controller read command (Command 42h).<br/>
```
  -      HighZ                   (always transferred)      1st byte
  -      ID/Mode/Len             (always transferred)      2nd byte
  -      5Ah                     (always transferred)      3rd byte
  0      LSB of digital buttons  (0=No, 1=Yes)             4th byte
  1      MSB of digital buttons  (0=No, 1=Yes)             5th byte
  2      RightJoyX               (0=No, 1=Yes)             6th byte
  3      RightJoyY               (0=No, 1=Yes)             7th byte
  4      LeftJoyX                (0=No, 1=Yes)             8th byte
  5      LeftJoyY                (0=No, 1=Yes)             9th byte
  6      DPAD Right              (0=No, 1=Yes) button 00h  10th byte
  7      DPAD Left               (0=No, 1=Yes) button 01h  11th byte
  8      DPAD Up                 (0=No, 1=Yes) button 02h  12th byte
  9      DPAD Down               (0=No, 1=Yes) button 03h  13th byte
  10     Button /\               (0=No, 1=Yes) button 04h  14th byte
  11     Button ()               (0=No, 1=Yes) button 05h  15th byte
  12     Button ><               (0=No, 1=Yes) button 06h  16th byte
  13     Button []               (0=No, 1=Yes) button 07h  17th byte
  14     Button L1               (0=No, 1=Yes) button 08h  18th byte
  15     Button R1               (0=No, 1=Yes) button 09h  19th byte
  16     Button L2               (0=No, 1=Yes) button 0Ah  20th byte
  17     Button R2               (0=No, 1=Yes) button 0Bh  21st byte
  18-39  Must be 0 (otherwise command is ignored)
  40-47  Unknown (no effect?)
```
Usually, one would use one of the following command/values:<br/>
```
  Send  01h 4Fh 00h 03h 00h 00h 00h 00h 00h  Digital buttons
  Send  01h 4Fh 00h 3Fh 00h 00h 00h 00h 00h  Digital buttons + analog sticks
  Send  01h 4Fh 00h FFh FFh 03h 00h 00h 00h  Enable all 18 input bytes
```
The transfer order is 1st..21st byte as shown above (unless some bits are
cleared, eg. if bit0-5=0 and bit6=1 then DPAD Right would appear as 4th byte
instead of 10th byte). The command length increases/decreases depening on the
number of enabled bits. The transfer length is always 3+N bytes (including a
00h padding byte when the number of enabled bits is odd). The analog mode ID
byte changes depending on number of halfwords.<br/>
CAUTION: Sending Command 44h does RESET the Command 4Fh setting (either to
DigitalMode=000003h or AnalogMode=00003Fh; same happens when toggling mode via
Analog button).<br/>

Note: Some Dualshock2 Config Mode commands do occassionally send 00h, 5Ah, or
FFh as last (9th) reply byte (unknown if that is some error/status thing, or
garbage).<br/>

#### Analog Button Sensitivity
The pressure sensors are rather imprecise and results may vary on various
factors, including the pressure angle.<br/>
```
  00h       Button released
  01h..2Fh  Normal (soft) pressure
  30h..FEh  Medium pressure
  FFh       Hard pressure
```
Software can safely distinguish between soft and hard pressure.<br/>
Medium pressure is less predictably: The values do not increase linearily, it's
difficult to apply a specific amount of medium pressure (such like 80h..9Fh),
increasing pressure may sometimes jump from 24h to FFh, completely skipping the
medium range.<br/>
Relying on the medium range might work for accelleration buttons (where the
user could still adjust the pressure when the accelleration is too high or too
low); but it would be very bad practice to assign irreversible actions to
medium pressure (such like Soft=Load, Medium=Save, Hard=Quit).<br/>

#### Digital Button Sensitivity
Digital inputs are converting the analog inputs as so:<br/>
```
  Analog=00h      --> not pressed
  Analog=01h..FFh --> pressed (no matter if soft, medium, or hard pressure)
```
Digital inputs are working even when also having analog input enabled for the
same button.<br/>

#### See also
[https://gist.github.com/scanlime/5042071] - tech (=mentions unknown details)
[https://store.curiousinventor.com/guides/PS2/] - guide (=omits unknown stuff)
