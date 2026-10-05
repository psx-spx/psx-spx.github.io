#   Standard Digital/Analog Controllers
```
       ___                      ___           ___                      ___
    __/_L_\__   Analog Pad   __/_R_\__     __/_L_\__  Digital Pad   __/_R_\__
   /    _    \--------------/         \   /    _    \--------------/         \
  |   _| |_   |            |     /\    | |   _| |_   |            |     /\    |
  |  |_ X _|  |SEL      STA|  []    () | |  |_ X _|  |            |  []    () |
  |    |_|  ___   ANALOG   ___   ><    | |    |_|    |  SEL  STA  |     ><    |
  |\______ / L \   LED    / R \ ______/| |\_________/--------------\_________/|
  |       | Joy |--------| Joy |       | |       |                    |       |
  |      / \___/          \___/ \      | |      /                      \      |
   \____/                        \____/   \____/                        \____/
```

#### Standard Controllers
```
  __Halfword 0 (Controller Info)_______________________________________________
  0-15  Controller Info  (5A41h=digital, 5A73h=analog/pad, 5A53h=analog/stick)
  __Halfword 1 (Digital Switches)______________________________________________
  0   Select Button    (0=Pressed, 1=Released)
  1   L3/Joy-button    (0=Pressed, 1=Released/None/Disabled) ;analog mode only
  2   R3/Joy-button    (0=Pressed, 1=Released/None/Disabled) ;analog mode only
  3   Start Button     (0=Pressed, 1=Released)
  4   Joypad Up        (0=Pressed, 1=Released)
  5   Joypad Right     (0=Pressed, 1=Released)
  6   Joypad Down      (0=Pressed, 1=Released)
  7   Joypad Left      (0=Pressed, 1=Released)
  8   L2 Button        (0=Pressed, 1=Released) (Lower-left shoulder)
  9   R2 Button        (0=Pressed, 1=Released) (Lower-right shoulder)
  10  L1 Button        (0=Pressed, 1=Released) (Upper-left shoulder)
  11  R1 Button        (0=Pressed, 1=Released) (Upper-right shoulder)
  12  /\ Button        (0=Pressed, 1=Released) (Triangle, upper button)
  13  () Button        (0=Pressed, 1=Released) (Circle, right button)
  14  >< Button        (0=Pressed, 1=Released) (Cross, lower button)
  15  [] Button        (0=Pressed, 1=Released) (Square, left button)
  __Halfword 2 (Right joystick) (analog pad/stick in analog mode only)_________
  0-7   adc0 RightJoyX (00h=Left, 80h=Center, FFh=Right)
  8-15  adc1 RightJoyY (00h=Up,   80h=Center, FFh=Down)
  __Halfword 3 (Left joystick) (analog pad/stick in analog mode only)__________
  0-7   adc2 LeftJoyX  (00h=Left, 80h=Center, FFh=Right)
  8-15  adc3 LeftJoyY  (00h=Up,   80h=Center, FFh=Down)
  __Further Halfword(s) (Dualshock2 only, and only if enabled)_________________
  0-7   ..   Analog Button (if enabled) (00h=Released, FFh=Max Pressure)
  8-15  ..   Analog Button (if enabled) (00h=Released, FFh=Max Pressure)
  ..    ..   ..
```

#### Analog Mode Note
On power-up, the controllers are in digital mode (with analog inputs disabled).
Analog mode can be (de-)activated manually by pushing the Analog button.
Alternately, analog mode can be (de-)activated by software via rumble
configuration commands (though that's supported only on newer pads; those with
two rumble motors). It is essential that emulators and any third-party hardware have a way of manually toggling analog mode, similar to original analog controllers, as certain games like Gran Turismo 1 will not attempt to enter analog mode on their own, even if they support analog controls and detect an analog controller.<br/>
Since analog pads boot in digital mode and will return the same ID byte as digital controllers, the most common way of distinguishing between the 2 is to send a Dualshock-only command (Typically command 43h - enter/exit config mode) and seeing how the controller responds to it.<br/>
The analog sticks are mechanically restricted to a "circular field of motion"
(most joypads can reach "min/max" values only in "straight" horizontal or
vertical directions, but not in "diagonal" directions).<br/>

#### Analog Joypad Range
```
               ...''''''''''...
       ____ .''________________''._____       ___ 00h
      |  .''                      ''.  |
      |.'                            '.|      ___ 10h
      .'                              '.
     :|                                |:
    : |                                | :    ___ 60h
   .' |            .''''''.            | '.
   :  |          .'        '.          |  :
   :  |          :          :          |  :   ___ 80h
   :  |          :          :          |  :
   :  |          '.        .'          |  :
   '. |            '......'            | .'   ___ A0h
    : |                                | :
     :|                                |:
      '.                              .'      ___ F0h
      |'.                            .'|
      |__'..______________________..'__|      ___ FFh
      .     '..                ..'     .
     00h       '''..........'''       FFh
```

```
   Big Circle   --> Mechanically possible field of motion
   Square Area  --> Digitally visible 8bit field of motion
   Small Circle --> Resting position when releasing the joystick
```
Example min/center/max values for three different pads:<br/>
```
  SCPH-1150          Min=(00,00), Mid: (72..90,79..AC), Max=(FF,FF) at 25'C
  SCPH-1200          Min=(0E,0E), Mid: (6C..8A,75..79), Max=(ED,ED) at 16'C
  SCPH-110           Min=(11,11), Mid: (8A..9F,70..96), Max=(FD,FD) at 16'C
```
Values may vary for other pads and/or different temperatures.<br/>

#### Dual Analog Pad in LED=Green Mode
Basically same as normal analog LED=Red mode, with following differences:<br/>
```
  ID is 5A53h (identifying itself as analog stick) (rather than analog pad)
  Left/right joy-buttons disabled (as for real analog stick, bits are always 1)
  Some buttons are re-arranged: bit9=L1 bit10=[] bit11=/\ bit12=R1 bit15=R2
```
Concerning the button names, the real analog-stick does NOT have re-arranged
buttons (eg. it's L1 button is in bit10), however, concerning the button
locations, the analog stick's buttons are arranged completely differently as on
analog pads (so it might be rather uncomfortable to play analog stick games on
analog pads in LED=Red mode; the LED=Green mode is intended to solve that
problem).<br/>
Might be useful for a few analog-stick games like MechWarrior 2, Ace Combat 2,
Descent Maximum, and Colony Wars. In most other cases the feature is rather
confusing (that's probably why the LED=Green mode wasn't implemented on the
Dual Shock).<br/>

#### See also
[Component List and Chipset Pin-Outs for Digital Joypad, SCPH-1080](../../pinouts/component-list-and-chipset-pin-outs-for-digital-joypad-scph-1080.md#component-list-and-chipset-pin-outs-for-digital-joypad-scph-1080)<br/>
[Component List and Chipset Pin-Outs for Analog Joypad, SCPH-1150](../../pinouts/component-list-and-chipset-pin-outs-for-analog-joypad-scph-1150.md#component-list-and-chipset-pin-outs-for-analog-joypad-scph-1150)<br/>
[Component List and Chipset Pin-Outs for Analog Joypad, SCPH-1200](../../pinouts/component-list-and-chipset-pin-outs-for-analog-joypad-scph-1200.md#component-list-and-chipset-pin-outs-for-analog-joypad-scph-1200)<br/>
[Component List and Chipset Pin-Outs for Analog Joypad, SCPH-110](../../pinouts/component-list-and-chipset-pin-outs-for-analog-joypad-scph-110.md#component-list-and-chipset-pin-outs-for-analog-joypad-scph-110)<br/>
