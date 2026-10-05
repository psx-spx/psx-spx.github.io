#   Mouse
#### Sony Mouse Controller
```
  __Halfword 0 (Controller Info)________________
  0-15  Controller Info  (5A12h=Mouse)
  __Halfword 1 (Mouse Buttons)__________________
  0-7   Not used         (All bits always 1)
  8-9   Unknown          (Seems to be always 0) (maybe SNES-style sensitivity?)
  10    Right Button     (0=Pressed, 1=Released)
  11    Left Button      (0=Pressed, 1=Released)
  12-15 Not used         (All bits always 1)
  __Halfword 2 (Mouse Motion Sensors)___________
  0-7   Horizontal Motion (-80h..+7Fh = Left..Right) (00h=No motion)
  8-15  Vertical Motion   (-80h..+7Fh = Up..Down)    (00h=No motion)
```

#### Sony Mouse Hardware Bug on Power-On
On Power-on (or when newly connecting it), the Sony mouse does draw /ACK to LOW
on power-on, and does then hold /ACK stuck in the LOW position.<br/>
For reference: Normal controllers and memory cards set /ACK=LOW only for around
100 clk cycles, and only after having received a byte from the console.<br/>
The /ACK pin is shared for both controllers and both memory cards, so the stuck
/ACK is also "blocking" all other connected controllers/cards. To release the
stuck /ACK signal: Send a command (at least one 01h byte) to both controller
slots.<br/>

#### Sony Mouse Compatible Games
```
  3D Lemmings
  Alien Resurrection
  Area 51
  Ark of Time
  Atari Anniversary Edition
  Atlantis: The Lost Tales
  Breakout: Off the Wall Fun
  Broken Sword: The Shadow of the Templars
  Broken Sword II: The Smoking Mirror
  Clock Tower: The First Fear
  Clock Tower II: The Struggle Within
  Command & Conquer: Red Alert
  Command & Conquer: Red Alert - Retaliation
  Constructor (Europe)
  Die Hard Trilogy
  Die Hard Trilogy 2: Viva Las Vegas
  Discworld
  Discworld II: Missing Presumed...!?
  Discworld Noir
  Dune 2000
  Final Doom
  Galaxian 3
  Ghoul Panic
  Klaymen Klaymen: Neverhood no Nazon (Japan)
  Lemmings and Oh No! More Lemmings
  Monopoly
  Music 2000
  Myst
  Neorude (Japan)
  Perfect Assassin
  Policenauts (Japan)
  Puchi Carat
  Quake II
  Railroad Tycoon II
  Rescue Shot
  Risk
  Riven: The Sequel to Myst
  RPG Maker
  Sentinel Returns
  SimCity 2000
  Syndicate Wars
  Tempest 2000 (Tempest X3)
  Theme Aquarium (Japan)
  Transport Tycoon
  Warhammer: Dark Omen
  Warzone 2100
  X-COM: Enemy Unknown
  X-COM: Terror from the Deep
  Z
```
Note: There are probably many more mouse compatible games.<br/>
Certain games, mostly FPS games such as Quake II and Doom, have players plug a standard digital/analog pad in port 1
and a mouse in port 2. This way, players can use the mouse for aiming and shooting, while the pad can be used for moving, reloading, and so on.<br/>

#### Sony Mouse Component List
PCB "TD-T41V/\, MITSUMI"<br/>
Component Side:<br/>
```
  1x 3pin   4.00MHz "[M]4000A, 85 2"
  2x 2pin   button (left/right)
  1x 8pin   connector (to cable with shield and 7 wires)
  1x 3pin   "811, T994I"
  2x 3pin   photo transistor (black)  ;\or so, no idea which one is
  2x 2pin   photo diode (transparent) ;/sender and which is sensor
  1x 2pin   electrolyt capacitor 16V, 10uF
```
Solder/SMD Side:<br/>
```
  1x 32pin  "(M), SC442116, FB G22K, JSAA815B"
  1x 14pin  "BA10339F, 817 L67" (Quad Comparator)
  2x 3pin   "LC" (amplifier for photo diodes)
  1x 3pin   "24-" (looks like a dual-diode or so)
  plus many SMD resistors/capacitors
```
Cable:<br/>
```
  PSX.Controller.Pin1 DAT   ---- brown  -- Mouse.Pin4
  PSX.Controller.Pin2 CMD   ---- red    -- Mouse.Pin3
  PSX.Controller.Pin3 +7.5V ---- N/A
  PSX.Controller.Pin4 GND   ---- orange -- Mouse.Pin7 GND (G)
  PSX.Controller.Pin5 +3.5V ---- yellow -- Mouse.Pin1
  PSX.Controller.Pin6 /CSn  ---- green  -- Mouse.Pin5
  PSX.Controller.Pin7 SCK   ---- blue   -- Mouse.Pin2
  PSX.Controller.Pin8 /IRQ  ---- N/A
  PSX.Controller.Pin9 /ACK  ---- purple -- Mouse.Pin6
  PSX.Controller.Shield -------- shield -- Mouse.Pin8 GND (SHIELD)
```

#### PS/2 and USB Mouse Adaptors
Some keyboard adaptors are also including a mouse adaptor feature (either by
simulating normal Sony Mouse controller data, or via more uncommon ways like
using the PSX expansion port).<br/>
[Keyboards](controllers-keyboards.md#keyboards)<br/>

#### RS232 Mice
Below is some info on RS232 serial mice. That info isn't directly PSX related
as the PSX normally doesn't support those mice.<br/>
With some efforts, one can upgrade the PSX SIO port to support RS232 voltages,
and with such a modded console one could use RS232 mice (in case one wants to
do that).<br/>
The nocash PSX bios can map a RS232 mouse to a spare controller slot (thereby
simulating a Sony mouse), that trick may work with various PSX games.<br/>

#### Standard Serial Mouse
A serial mouse should be read at 1200 bauds, 7 data bits, no parity, 1 stop bit
(7N1) with DTR and RTS on. For best compatibility, the mouse should output 2
stop bits (so it could be alternately also read as 7N2 or 8N1). When the mouse
gets moved, or when a button gets pressed/released, the mouse sends 3 or 4
characters:<br/>
```
  __First Character____________________
  6    First Character Flag (1)
  5    Left Button  (1=Pressed)
  4    Right Button (1=Pressed)
  2-3  Upper 2bit of Vertical Motion
  0-1  Upper 2bit of Horizontal Motion
  __Second Character___________________
  6    Non-first Character Flag (0)
  5-0  Lower 6bit of Horizontal Motion
  __Third Character____________________
  6    Non-first Character Flag (0)
  5-0  Lower 6bit of Vertical Motion
  __Fourth Character (if any)__________
  6    Non-first Character Flag (0)
  5    Middle Button (1=Pressed)
  4    Unused ???
  3-0  Wheel  ???
```
Additionally, the mouse outputs a detection character (when switching RTS (or
DTR?) off and on:<br/>
```
  "M" = Two-Button Mouse (aka "Microsoft" mouse)
  "3" = Three-Button Mouse (aka "Logitech" mouse)
  "Z" = Mouse-Wheel
```
Normally, the detection response consist of a single character (usually "M"),
though some mice have the "M" followed by 11 additional characters of garbage
or version information (these extra characters have bit6=0, so after detection,
one should ignore all characters until receiving the first data character with
bit6=1).<br/>

#### Mouse Systems Serial Mouse (rarely used)
Accessed at 1200 bauds, just like standard serial mouse, but with 8N1 instead
7N1, and with different data bytes.<br/>
```
  __First Byte_________________________
  7-3  First Byte Code (10000b)
  2    Left? Button   (0=Pressed)
  1    Middle? Button (0=Pressed)
  0    Right? Button  (0=Pressed)
  __Second Byte________________________
  7-0  Horizontal Motion (X1)
  __Third Byte_________________________
  7-0  Vertical Motion   (Y1)
  __Fourth Byte________________________
  7-0  Horizontal Motion (X2)
  __Fifth Byte_________________________
  7-0  Vertical Motion   (Y2)
```
The strange duplicated 8bit motion values are usually simply added together,
ie. X=X1+X2 and Y=Y1+Y2, producing 9bit motion values.<br/>

#### Notes
The Sony Mouse connects directly to the PSX controller port. Alternately serial
RS232 mice can be connected to the SIO port (with voltage conversion adaptor)
(most or all commercial games don't support SIO mice, nor does the original
BIOS do so, however, the nocash BIOS maps SIO mice to unused controller slots,
so they can be used even with commercial games; if the game uses BIOS functions
to read controller data).<br/>
Serial Mice (and maybe also the Sony mouse) do return raw mickeys, so effects
like double speed threshold must (should) be implemented by software. Mice are
rather rarely used by PSX games. The game "Perfect Assassin" includes
ultra-crude mouse support, apparently without threshold, and without properly
matching the cursor range to the screen resolution.<br/>
