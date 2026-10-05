#   Racing Controllers
#### neGcon Racing Controller (Twist) (NPC-101/SLPH-00001/SLEH-0003)
```
  __Halfword 0 (Controller Info)_______________________________________________
  0-15  Controller Info  (5A23h=neGcon)
  __Halfword 1 (Digital Switches)______________________________________________
  0-2   Not used       (always 1)       (would be Select, L3, R3 on other pads)
  3     Start Button   (0=Pressed, 1=Released)
  4     Joypad Up      (0=Pressed, 1=Released)
  5     Joypad Right   (0=Pressed, 1=Released)
  6     Joypad Down    (0=Pressed, 1=Released)
  7     Joypad Left    (0=Pressed, 1=Released)
  8-10  Not used       (always 1)       (would be L2, R2, L1 on other pads)
  11    R Button       (0=Pressed, 1=Released) (would be R1 on other pads)
  12    B Button       (0=Pressed, 1=Released) (would be /\ on other pads)
  13    A Button       (0=Pressed, 1=Released) (would be () on other pads)
  14-15 Not used       (always 1)              (would be ><, [] on other pads)
  __Halfword 2 (Right joystick) (analog pad/stick in analog mode only)_________
  0-7   Steering Axis    (00h=Left, 80h=Center, FFh=Right) (or vice-versa?)
  8-15  Analog I button  (00h=Out ... FFh=In)  (Out=released, in=pressed?)
  __Halfword 3 (Left joystick) (analog pad/stick in analog mode only)__________
  0-7   Analog II button (00h=Out ... FFh=In)  (Out=released, in=pressed?)
  8-15  Analog L button  (00h=Out ... FFh=In)  (Out=released, in=pressed?)
```
The Twist controller works like a paddle or steering wheel, but doesn't have a
wheel or knob, instead, it can be twisted: To move into one direction (=maybe
right?), turn its right end away from you (or its left end towards you). For
the opposite direction (=maybe left?), do it vice-versa.<br/>
```
     _____         _  _         _____                              ____
    |__L__\_______/ || \_______/__R__|                            /    \
   /    _   namco   ||   neGcon       \                          /      \
  |   _| |_         ||            B    |                        |       |
  |  |_ X _|    ....||....     II   A  | .... Rotation Axis ... | ...  \|/
  |    |_|          ||            I    |                        |
  |        START    ||                 |                         \
  |       ________  ||  ________       |                          \__\
  |      /        \_||_/        \      |                             /
   \____/                        \____/
```

#### Namco Volume Controller (a paddle with two buttons) (SLPH-00015)
This is a cut-down variant of the neGcon, just a featureless small box. It does
have the same ID value as neGcon (ID=5A23h), but, it excludes most digital, and
all analog buttons.<br/>
```
   _______
  | namco |      Halfword 1 (digital buttons):
  |       |      Bit3  Button A (0=Pressed) (aka neGcon Start button)
  | A   B |      Bit13 Button B (0=Pressed) (aka neGcon A button aka () button)
  |       |      Other bits     (not used, always 1)
  |   _   |      Halfword 2 and 3 (analog inputs):
  |  (_)  |      Steering Axis  (00h..FFh)  (as for neGcon)
  |_______|      Analog I,II,L button values (not used, always 00h)
```

#### SANKYO N.ASUKA aka Nasca Pachinco Handle (SLPH-00007)
Another cut-down variant of the neGcon (with ID=5A23h, too). But, this one
seems to have only one button. Unlike Namco's volume controller it doesn't look
featureless. It looks pretty much as shown in the ascii-arts image below. Seems
to be supported by several irem titles. No idea what exactly it is used for,
it's probably not a sewing machine controller, nor an electronic amboss.<br/>
```
   ____ ____     Halfword 1 (digital buttons):
  |   /   _ \    Bit12 Button   (0=Pressed) (aka neGcon B button aka /\ button)
  |_ /   (_) )   Other bits     (not used, always 1)
  |_|___    /\   Halfword 2 and 3 (analog inputs):
   ____|   |_    Steering Axis  (00h..FFh)  (as for neGcon)
  |__________|   Analog I,II,L button values (not used, always 00h)
```

#### Mad Catz Steering Wheel (SLEH-0006)
A neGcon compatible controller. The Twist-feature has been replaced by a
steering wheel (can be turned by 270 degrees), and the analog I and II buttons
by foot pedals. The analog L button has been replaced by a digital button (ie.
in neGcon mode, the last byte of the controller data can be only either 00h or
FFh). When not using the pedals, the I/II buttons on the wheel can be used
(like L button, they aren't analog though).<br/>
```
        __________________________
       /   ____________________   \    Stick
      /   /                    \   \    ___        Brakes  Gas
     /   (                      )   \  (   )         II     I
    /  I  \                    /  A  \  \ /          ___   ___
   / /\ II \____________MODE__/  B /\ \  |          |   | |   |
  | |  \ L  _                   R /  | | |          |!!!|_|!!!|___
  | |   ) _| |_   MadCatz        (   | |_|_        /|!!!| |!!!|  /
  | |  | |_ X _|                  |  | | | |      / |___| |___| /
  | |  |   |_|                    |  | |  /      / =========== /
  | |   \         SEL STA        /   | | /      / =========== /
   \ \__/ ______________________ \__/ / /      /_____________/
    \____/                      \____/_/
       |___________________________|
```

Unlike the neGon, the controller has Select, \>\< and [] buttons, and a
second set of L/R buttons (at the rear-side of the wheel) (no idea if L1/R1 or
L2/R2 are at front?). Aside from the neGcon mode, the controller can be also
switched to Digital mode (see below for button chart).<br/>

#### MadCatz Dual Force Racing Wheel
Same as above, but with a new Analog mode (additionally to Digital and neGcon
modes). The new mode is for racing games that support only Analog Joypads
(instead of neGcon). Additionally it supports vibration feedback.<br/>

#### MadCatz MC2 Vibration compatible Racing Wheel and Pedals
Same as above, but with a redesigned wheel with rearranged buttons, the digital
pad moved to the center of the wheel, the L/R buttons at the rear-side of the
wheel have been replaced by 2-way butterfly buttons ("pull towards user" acts
as normal, the new "push away from user" function acts as L3/R3).<br/>
```
            ____________________
           /  ________________  \   ___ Stick      Brakes  Gas
          /  /       MC2      \  \ (   )             ___   ___
         /  /__________________\  \ \ /             |   | |   |
        |    A ()    _|_    I ><   | |              |!!!|_|!!!|___
        |   B /\ _    |    _ II [] | |             /|!!!| |!!!|  /
     ___|  L2   / \  STA  / \ R2   |_|_           / |___| |___| /
    /    \     /   | SEL |   \    /    \         / =========== /
   /  ____\    |___|     |___|   /____  \       / =========== /
  /__/     \____________________/     \__\     /_____________/
```

#### MadCatz Button Chart
```
  Mode     Buttons...................... Gas Brake Stick Wheel
  Digital  >< [] () /\ L1 R1 L2 R2 L1 R1 ><  ()    L1/R1 lt/rt
  Analog   >< [] () /\ L1 R1 L2 R2 L3 R3 UP  DN    L1/R1 LT/RT
  Negcon   I  II A  B  L  R  L  R  L  R  I   II    up/dn Twist
```
Whereas, lt/rt/up/dn=Digital Pad, UP/DN=Left Analog Pad Up/Down, LT/RT=Right
Analog Pad Left/Right. Analog mode is supported only by the Dual Force and MC2
versions, L3/R3 only by the MC2 version.<br/>

#### Namco Jogcon (NPC-105/SLEH-0020/SLPH-00126/SLUH-00059)
```
  __Halfword 0 (Controller Info)___________________
  0-15  Controller Info  (5AE3h=Jogcon in Jogcon mode) (ie. not Digital mode)
 halfword1: buttons: same as digital pad
 halfword2:
   0    unknown (uh, this isn't LSB of rotation?)
   1-15 dial rotation (signed offset since last read?) (or absolute position?)
 halfword3:
   0    flag: dial was turned left  (0=no, 1=yes)
   1    flag: dial was turned right (0=no, 1=yes)
   2-15 unknown
```
Rotations of the dial are recognized by an optical sensor (so, unlike
potentiometers, the dial can be freely rotated; by more than 360 degrees). The
dial is also connected to a small motor, giving it a real force-feedback effect
(unlike all other PSX controllers which merely have vibration feedback).
Although that's great, the mechanics are reportedly rather cheap and using the
controller doesn't feel too comfortable. The Jogcon is used only by Ridge Racer
4 for PS1 (and Ridge Racer 5 for PS2), and Breakout - Off the Wall Fun.<br/>
The Mode button probably allows to switch between Jogcon mode and Digital Pad
mode (similar to the Analog button on other pads), not sure if the mode can be
also changed by software via configuration commands...? Unknown how the motor
is controlled; probably somewhat similar to vibration motors, ie. by the M1
and/or M2 bytes, but there must be also a way to select clockwise and
anticlockwise direction)...? The controller does reportedly support config
command 4Dh (same as analog rumble).<br/>
```
       ___       ________       ___
    __/_L_\__   /        \   __/_R_\__
   /    _    \ / LED MODE \-/         \
  |   _| |_   | SEL    STA |     /\    |
  |  |_ X _|  |  ________  |  []    () |
  |    |_|    | /        \ |     ><    |
  |\_________/\/          \/\__ ______/|
  |       |   |   JOGCON   |   |       |
  |       |   |    DIAL    |   |       |
  |       |    \          /    |       |
  |       |     \________/     |       |
  |       |                    |       |
  |       |                    |       |
   \_____/                      \_____/
```
