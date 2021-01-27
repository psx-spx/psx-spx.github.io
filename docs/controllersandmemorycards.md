#   Controllers and Memory Cards
#### Controllers/Memory Cards
[Controller and Memory Card I/O Ports](controllersandmemorycards.md#controller-and-memory-card-io-ports)<br/>
[Controller and Memory Card Misc](controllersandmemorycards.md#controller-and-memory-card-misc)<br/>
[Controller and Memory Card Signals](controllersandmemorycards.md#controller-and-memory-card-signals)<br/>
[Controller and Memory Card Multitap Adaptor](controllersandmemorycards.md#controller-and-memory-card-multitap-adaptor)<br/>

#### Controllers
[Controllers - Communication Sequence](controllersandmemorycards.md#controllers-communication-sequence)<br/>
[Controllers - Standard Digital/Analog Controllers](controllersandmemorycards.md#controllers-standard-digitalanalog-controllers)<br/>
[Controllers - Mouse](controllersandmemorycards.md#controllers-mouse)<br/>
[Controllers - Racing Controllers](controllersandmemorycards.md#controllers-racing-controllers)<br/>
[Controllers - Lightguns](controllersandmemorycards.md#controllers-lightguns)<br/>
[Controllers - Rumble Configuration](controllersandmemorycards.md#controllers-rumble-configuration)<br/>
[Controllers - Dance Mats](controllersandmemorycards.md#controllers-dance-mats)<br/>
[Controllers - Fishing Controllers](controllersandmemorycards.md#controllers-fishing-controllers)<br/>
[Controllers - I-Mode Adaptor (Mobile Internet)](controllersandmemorycards.md#controllers-i-mode-adaptor-mobile-internet)<br/>
[Controllers - Additional Inputs](controllersandmemorycards.md#controllers-additional-inputs)<br/>
[Controllers - Misc](controllersandmemorycards.md#controllers-misc)<br/>

#### Memory Cards
[Memory Card Read/Write Commands](controllersandmemorycards.md#memory-card-readwrite-commands)<br/>
[Memory Card Data Format](controllersandmemorycards.md#memory-card-data-format)<br/>
[Memory Card Images](controllersandmemorycards.md#memory-card-images)<br/>
[Memory Card Notes](controllersandmemorycards.md#memory-card-notes)<br/>

#### Pocketstation (Memory Card with built-in LCD screen and buttons)
[Pocketstation](pocketstation.md)<br/>

#### Pinouts
[Pinouts - Controller Ports and Memory-Card Ports](pinouts.md#pinouts-controller-ports-and-memory-card-ports)<br/>



##   Controller and Memory Card I/O Ports
#### 1F801040h JOY\_TX\_DATA (W)
```
  0-7   Data to be sent
  8-31  Not used
```
Writing to this register starts the transfer (if, or as soon as TXEN=1 and
JOY\_STAT.2=Ready), the written value is sent to the controller or memory card,
and, simultaneously, a byte is received (and stored in RX FIFO if JOY\_CTRL.1 or
JOY\_CTRL.2 is set).<br/>
The "TXEN=1" condition is a bit more complex: Writing to SIO\_TX\_DATA latches
the current TXEN value, and the transfer DOES start if the current TXEN value
OR the latched TXEN value is set (ie. if TXEN gets cleared after writing to
SIO\_TX\_DATA, then the transfer may STILL start if the old latched TXEN value
was set).<br/>

#### 1F801040h JOY\_RX\_DATA (R)
```
  0-7   Received Data      (1st RX FIFO entry) (oldest entry)
  8-15  Preview            (2nd RX FIFO entry)
  16-23 Preview            (3rd RX FIFO entry)
  24-31 Preview            (4th RX FIFO entry) (5th..8th cannot be previewed)
```
A data byte can be read when JOY\_STAT.1=1. Data should be read only via 8bit
memory access (the 16bit/32bit "preview" feature is rather unusable, and
usually there shouldn't be more than 1 byte in the FIFO anyways).<br/>

#### 1F801044h JOY\_STAT (R)
```
  0     TX Ready Flag 1   (1=Ready/Started)
  1     RX FIFO Not Empty (0=Empty, 1=Not Empty)
  2     TX Ready Flag 2   (1=Ready/Finished)
  3     RX Parity Error   (0=No, 1=Error; Wrong Parity, when enabled)  (sticky)
  4     Unknown (zero)    (unlike SIO, this isn't RX FIFO Overrun flag)
  5     Unknown (zero)    (for SIO this would be RX Bad Stop Bit)
  6     Unknown (zero)    (for SIO this would be RX Input Level AFTER Stop bit)
  7     /ACK Input Level  (0=High, 1=Low)
  8     Unknown (zero)    (for SIO this would be CTS Input Level)
  9     Interrupt Request (0=None, 1=IRQ7) (See JOY_CTRL.Bit4,10-12)   (sticky)
  10    Unknown (always zero)
  11-31 Baudrate Timer    (21bit timer, decrementing at 33MHz)
```

#### 1F801048h JOY\_MODE (R/W) (usually 000Dh, ie. 8bit, no parity, MUL1)
```
  0-1   Baudrate Reload Factor (1=MUL1, 2=MUL16, 3=MUL64) (or 0=MUL1, too)
  2-3   Character Length       (0=5bits, 1=6bits, 2=7bits, 3=8bits)
  4     Parity Enable          (0=No, 1=Enable)
  5     Parity Type            (0=Even, 1=Odd) (seems to be vice-versa...?)
  6-7   Unknown (always zero)
  8     CLK Output Polarity    (0=Normal:High=Idle, 1=Inverse:Low=Idle)
  9-15  Unknown (always zero)
```

#### 1F80104Ah JOY\_CTRL (R/W) (usually 1003h,3003h,0000h)
```
  0     TX Enable (TXEN)  (0=Disable, 1=Enable)
  1     /JOYn Output      (0=High, 1=Low/Select) (/JOYn as defined in Bit13)
  2     RX Enable (RXEN)  (0=Normal, when /JOYn=Low, 1=Force Enable Once)
  3     Unknown? (read/write-able) (for SIO, this would be TX Output Level)
  4     Acknowledge       (0=No change, 1=Reset JOY_STAT.Bits 3,9)          (W)
  5     Unknown? (read/write-able) (for SIO, this would be RTS Output Level)
  6     Reset             (0=No change, 1=Reset most JOY_registers to zero) (W)
  7     Not used             (always zero) (unlike SIO, no matter of FACTOR)
  8-9   RX Interrupt Mode    (0..3 = IRQ when RX FIFO contains 1,2,4,8 bytes)
  10    TX Interrupt Enable  (0=Disable, 1=Enable) ;when JOY_STAT.0-or-2 ;Ready
  11    RX Interrupt Enable  (0=Disable, 1=Enable) ;when N bytes in RX FIFO
  12    ACK Interrupt Enable (0=Disable, 1=Enable) ;when JOY_STAT.7  ;/ACK=LOW
  13    Desired Slot Number  (0=/JOY1, 1=/JOY2) (set to LOW when Bit1=1)
  14-15 Not used             (always zero)
```
Caution: After slot selection (via Bits 1,13), one should issue a delay before
sending the the first data byte: Digital Joypads may work without delay,
Dualshock and Mouse require at least some small delay, and older Analog Joypads
require a huge delay (around 500 clock cycles for SCPH-1150), official kernel
waits more than 2000 cycles (which is much more than needed).<br/>

#### 1F80104Eh JOY\_BAUD (R/W) (usually 0088h, ie. circa 250kHz, when Factor=MUL1)
```
  0-15  Baudrate Reload value for decrementing Baudrate Timer
```
Timer reload occurs when writing to this register, and, automatically when the
Baudrate Timer reaches zero. Upon reload, the 16bit Reload value is multiplied
by the Baudrate Factor (see 1F801048h.Bit0-1), divided by 2, and then copied to
the 21bit Baudrate Timer (1F801044h.Bit11-31). The 21bit timer decreases at
33MHz, and, it ellapses twice per bit (once for CLK=LOW and once for CLK=HIGH).<br/>
```
  BitsPerSecond = (44100Hz*300h) / MIN(((Reload*Factor) AND NOT 1),1)
```
The default BAUD value is 0088h (equivalent to 44h cpu cycles), and default
factor is MUL1, so CLK pulses are 44h cpu cycles LOW, and 44h cpu cycles HIGH,
giving it a transfer rate of circa 250kHz per bit (33MHz divided by 88h
cycles).<br/>
Note: The Baudrate Timer is always running; even if there's no transfer in
progress.<br/>

#### /IRQ7 (/ACK) Controller and Memory Card - Byte Received Interrupt
Gets set after receiving a data byte - that only if an /ACK has been received
from the peripheral (ie. there will be no IRQ if the peripheral fails to send
an /ACK, or if there's no peripheral connected at all).<br/>
```
  Actually, /IRQ7 means "more-data-request",
  accordingly, it does NOT get triggered after receiving the LAST byte.
```
I\_STAT.7 is edge triggered (that means it can be acknowledge before or after
acknowledging JOY\_STAT.9). However, JOY\_STAT.9 is NOT edge triggered (that
means it CANNOT be acknowledged while the external /IRQ input is still low; ie.
one must first wait until JOY\_STAT.7=0, and then set JOY\_CTRL.4=1) (this is
apparently a hardware glitch; note: the LOW duration is circa 100 clock
cycles).<br/>

#### /IRQ10 (/IRQ) Controller - Lightpen Interrupt
Pin8 on Controller Port. Routed directly to the Interrupt Controller (at
1F80107xh). There are no status/enable bits in the JOY\_registers (at
1F80104xh).<br/>

#### RX FIFO / TX FIFO Notes
The JOY registers can hold up to 8 bytes in RX direction, and almost 2 bytes in
TX direction (just like the SIO registers, see there for details), however,
normally only 1 byte should be in the RX/TX registers (one shouldn't send a 2nd
byte until /ACK is sensed, and, since the transfer CLK is dictated by the CPU,
the amount of incoming data cannot exceed 1 byte; provided that one reads
received response byte after each transfer).<br/>
Unlike SIO, the JOY status register doesn't have a RX FIFO Overrun flag.<br/>

#### General Notes
RXEN should be usually zero (the hardware automatically enables receive when
/JOYn is low). When RXEN is set, the next transfer causes data to be stored in
RX FIFO even when /JOYn is high; the hardware automatically clears RXEN after
the transfer.<br/>
For existing joypads and memory cards, data should be always transferred as
8bit no parity (although the JOY registers do support parity just like SIO
registers).<br/>

#### Plugging and Unplugging Cautions
During plugging and unplugging, the Serial Data line may be dragged LOW for a
moment; this may also affect other connected devices because the same Data line
is shared for all controllers and memory cards (for example, connecting a
joypad in slot 1 may corrupt memory card accesses in slot 2).<br/>
Moreover, the Sony Mouse does power-up with /ACK=LOW, and stays stuck in that
state until it is accessed at least once (by at least sending one 01h byte to
its controller port); this will also affect other devices (as a workaround one
should always access BOTH controller ports; even if a game uses only one
controller, and, code that waits for /ACK=HIGH should use timeouts).<br/>

#### Emulation Note
After sending a byte, the Kernel waits 100 cycles or so, and does THEN
acknowledge any old IRQ7, and does then wait for the new IRQ7. Due to that
bizarre coding, emulators can't trigger IRQ7 immediately within 0 cycles after
sending the byte.<br/>



##   Controller and Memory Card Misc
#### BIOS Functions
Controllers can be probably accessed via InitPad and StartPad functions,<br/>
[BIOS Joypad Functions](kernelbios.md#bios-joypad-functions)<br/>
Memory cards can be accessed by the filesystem (with device names "bu00:"
(slot1) and "bu10:" (slot2) or so). Before using that device names, it seems to
be required to call InitCard, StartCard, and \_bu\_init (?).<br/>

#### Connectors
The PlayStation has four connectors (two controllers, two memory cards),<br/>
```
  Memory Card 1         Memory Card 2
  Controller 1          Controller 2
```
The controller ports have 9 pins, the memory cards only 8 pins. However, there
are only 10 different pins in total.<br/>
```
  JOYDAT,JOYCMD,JOYCLK  Data in/out/clock
  +7.5V,+3.5V,GND       Supply
  /JOY1,/JOY2  Selects controller/memorycard 1, or controller/memorycard 2
  /ACK         Indicates that the device is ready to send more data (IRQ7)
  /IRQ10       Lightgun (controllers only, not memory card) (IRQ10)
```
Most of these pins are shared for all 4 connectors (eg. a CLK signal meant to
be sent to one device will also arrive at the other 3 devices).<br/>
The /JOYn signals are selecting BOTH the corresponding controller, and the
corresponding memory card (whether it is a controller access or memory card
access depends on the first byte transferred via the CMD line; this byte should
be 01h=Controller, or 81h=Memory Card; or, a special case would be 21h=Yaroze
Access Card).<br/>

#### Data In/Out
The data is transferred in units of bytes, via separate input and output lines.
So, when sending byte, the hardware does simultaneously receive a response
byte.<br/>
One exception is the first command byte (which selects either the controller,
or the memory card) until that byte has been sent, neither the controller nor
memory card are selected (and so the first "response" byte should be ignored;
probably containing more or less stable high-z levels).<br/>
The other exception is, when you have send all command bytes, and still want to
receive further data, then you'll need to send dummy command bytes (should be
usually 00h) to receive the response bytes.<br/>



##   Controller and Memory Card Signals
#### Overview
```
       ____                                                              _____
  /SEL     |____________________________________________________________|
       ______        ____        ____        ____        ____        _________
  CLK        ||||||||    ||||||||    ||||||||    ||||||||    ||||||||
       _______________________________________________________________________
  CMD       X  01h   XXXX  42h   XXXX  00h   XXXX  00h   XXXX  00h   XXXX
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            _____________________________________________________________
  DAT  -----XXXXXXXXXXXXX   ID   XXXX  5Ah   XXXX  key1  XXXX  key2  XXXX-----
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  /ACK ---------------|_|---------|_|---------|_|---------|_|-----------------
```

#### Top command. First comminucation(device check)
```
       ____
  /SEL     |__________________________________________________________________
       ______   _   _   _   _   _   _   _   __________________   _   _   _   _
  CLK        |_| |_| |_| |_| |_| |_| |_| |_|                  |_| |_| |_| |_|
       __________                                                  ___
  CMD            |________________________________________________|   |_______
                                                              ____
  DAT  -----XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    |___________
  /ACK ----------------------------------------------|___|--------------------
```

X = none, - = Hi-Z<br/>

\* 0x81 is memory-card, 0x01 is standard-pad at top command.<br/>
\* serial data transfer is LSB-First format.<br/>
\* data is down edged output, PSX is read at up edge in shift clock.<br/>
\* PSX expects No-connection if not returned Acknowledge less than 100 usec.<br/>
\* clock pulse is 250KHz.<br/>
\* no need Acknowledge at last data.<br/>
\* Acknowledge signal width is more than 2 usec.<br/>
\* time is 16msec between SEL from previous SEL.<br/>
\* SEL- for memory card in PAD access.<br/>



##   Controller and Memory Card Multitap Adaptor
#### SCPH-1070 (Multitap)
The Multitap is an external adaptor that allows to connect 4 controllers, and 4
memory cards to one controller port. When using two adaptors (one on each
slot), up to 8 controllers and 8 memory cards can be used.<br/>

#### Multitap Controller Access
Normally joypad reading is done by sending this bytes to the pad:<br/>
```
  01 42 00 00 ..   ;normal read
```
And with the multitap, there are even two different ways how to access extra
pads:<br/>
```
  01 42 01 00 ..   ;method 1: receive special ID and data from ALL four pads
  0n 42 00 00 ..   ;method 2: receive data from pad number "n" (1..4)
```
The first method seems to be the more commonly used one (and its special ID is
also good for detecting the multitap); see below for details.<br/>
The second method works more like "normal" reads, among other it's allowing to
transfer more than 4 halfwords per slot (unknown if any existing games are
using that feature).<br/>
The IRQ10 signal (for Konami Lightguns) is simply wired to all four slots via
small resistors (without special logic for activating/deactivating the IRQ on
certain slots).<br/>

#### Multitap Controller Access, Method 1 Details
Below LONG response is activated by sending "01h" as third command byte;
observe that sending that byte does NOT affect the current response. Instead,
it does request that the NEXT command shall return special data, as so:<br/>
```
  Halfword 0      --> Controller ID for MultiTap (5A80h=Multitap)
  Halfword 1..4   --> Player A (Controller ID, Buttons, Analog Inputs, if any)
  Halfword 5..8   --> Player B (Controller ID, Buttons, Analog Inputs, if any)
  Halfword 9..12  --> Player C (Controller ID, Buttons, Analog Inputs, if any)
  Halfword 13..16 --> Player D (Controller ID, Buttons, Analog Inputs, if any)
```
With this method, the Multitap is always sending 4 halfwords per slot (padded
with FFFFh values for devices like Digital Joypads and Mice; which do use less
than 4 halfwords); for empty slots it's padding all 4 halfwords with FFFFh.<br/>
Sending the request is possible ONLY if there is a controller in Slot A (if
controller Slot A is empty then the Slot A access aborts after the FIRST byte,
and it's thus impossible to send the request in the THIRD byte).<br/>
Sending the request works on access to Slot A, trying to send another request
during the LONG response is glitchy (for whatever strange reason); one must
thus REPEATEDLY do TWO accesses: one dummy Slot A access (with the request),
followed by the long Slot A+B+C+D access.<br/>
```
  Previous access had REQ=0 and returned Slot A data ---> returns Slot A data
  Previous access had REQ=0 and returned Slot A-D data -> returns Slot A data
  Previous access had REQ=1 and returned Slot A data ---> returns Slot A-D data
  Previous access had REQ=1 and returned Slot A-D data -> returns garbage
  Previous access had REQ=1 and returned garbage -------> returns Slot A-D data
```
In practice:<br/>
Toggling REQ on/off after each command: Returns responses toggling between
normal Slot A data and long Slot A+B+C+D data.<br/>
Sending REQ=1 in ALL commands: Returns responses toggling between Garbage and
long Slot A+B+C+D data.<br/>
Both of the above is working (one needs only the Slot A+B+C+D part, and it
doesn't matter if the other part is Slot A, or Garbage; as long as the software
is able/aware of ignoring the Garbage). Garbage response means that the
multitap returns ONLY four bytes, like so: Hiz,80h,5Ah,LSB (ie. the leading
HighZ byte, the 5A80h Multitap ID, and the LSB of the Slot A controller ID),
and aborts transfer after that four bytes.<br/>

#### Multitap Memory Card Access
Normally memory card access is done by sending this bytes to the card:<br/>
```
  80 xx .. ..      ;normal access
```
And with the multitap, memory cards can be accessed as so:<br/>
```
  8n xx .. ..      ;access memory card in slot "n" (1..4)
```
That's the way how its done in Silent Hill. Although for the best of confusion,
it doesn't actually work in that game (probably the developer has just linked
in the multitap library, without actually supporting the multitap at higher
program levels).<br/>

#### Multitap Games
```
  Bomberman World
  Breakout: Off the Wall Fun
  Circuit Breakers
  Crash Team Racing
  FIFA series soccer games
  Frogger
  Gauntlet: Dark Legacy
  Hot Shots Golf 2 & 3
  NBA Live (any year) (up to 8 players with two multitaps)
  Need For Speed 3
  Need For Speed 5
  Poy Poy (4 players hitting each other with rocks and trees)
  Running Wild
```

#### Multitap Versions
```
                   .------.
   SCPH-1070       |      |        SCPH-111
   (gray case)     |      |        (white case)
   (for PSX)       |    D |        (for PSone)
                   |      |                   .----------------.
        cable      |      |        cable     .'   D        C   '.
            ''--.. |    C |         '''--..__|                  |
                  \|      |                  |                  |
  .----------------'      |                  '.   A        B   .'
  |                       |                   '----------------'
  |                       |
  |    A        B        /
  '---------------------'
```
The cable connects to one of the PSX controller ports (which also carries the
memory card signals). The PSX memory card port is left unused (and is blocked
by a small edge on the Multitap's plug).<br/>

#### MultiTap Parsed Controller IDs
Halfword 0 is parsed (by the BIOS) as usually, ie. the LSB is moved to MSB, and
LSB is replaced by status byte (so ID 5A80h becomes 8000h=Multitap/okay, or
xxFFh=bad). Halfwords 1,5,9,13 are NOT parsed (neither by the BIOS nor by the
Multitap hardware), however, some info in the internet is hinting that Sony's
libraries might be parsing these IDs too (so for example 5A41h would become
4100h=DigitalPad/okay, or xxFFh=bad).<br/>

#### Power Supply
The Multitap is powered by the PSX controller port. Unknown if there are any
power supply restrictions (up to eight controllers and eight cards may scratch
some limits, especially when doing things like activating rumble on all
joypads). However, the Multitap hardware itself doesn't do much on supply
restrictions (+3.5V is passed through something; maybe some fuse, loop, or 1
ohm resistor or so) (and +7.5V is passed without any restrictions).<br/>

#### See also
[Pinouts - Component List and Chipset Pin-Outs for Multitap, SCPH-1070](pinouts.md#pinouts-component-list-and-chipset-pin-outs-for-multitap-scph-1070)<br/>



##   Controllers - Communication Sequence
#### Controller Communication Sequence
```
  Send Reply Comment
  01h  Hi-Z  Controller Access (unlike 81h=Memory Card access), dummy response
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
[Controller and Memory Card Multitap Adaptor](controllersandmemorycards.md#controller-and-memory-card-multitap-adaptor)<br/>
The two MOT bytes are meant to control the rumble motors (for normal non-rumble
controllers, that bytes should be 00h), however, the MOT bytes have no effect
unless rumble is enabled via config commands, for details, see<br/>
[Controllers - Rumble Configuration](controllersandmemorycards.md#controllers-rumble-configuration)<br/>

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
  5A80h=Multitap            (multiplayer adaptor) (when activated)
  5AE3h=Jogcon              (steering dial)
  5AF3h=Config Mode         (when in config mode; see rumble command 43h)
  FFFFh=High-Z              (no controller connected, pins floating High-Z)
```



##   Controllers - Standard Digital/Analog Controllers
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
```

#### Analog Mode Note
On power-up, the controllers are in digital mode (with analog inputs disabled).
Analog mode can be (de-)activated manually by pushing the Analog button.
Alternately, analog mode can be (de-)activated by software via rumble
configuration commands (though that's supported only on newer pads; those with
two rumble motors).<br/>
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
[Pinouts - Component List and Chipset Pin-Outs for Digital Joypad, SCPH-1080](pinouts.md#pinouts-component-list-and-chipset-pin-outs-for-digital-joypad-scph-1080)<br/>
[Pinouts - Component List and Chipset Pin-Outs for Analog Joypad, SCPH-1150](pinouts.md#pinouts-component-list-and-chipset-pin-outs-for-analog-joypad-scph-1150)<br/>
[Pinouts - Component List and Chipset Pin-Outs for Analog Joypad, SCPH-1200](pinouts.md#pinouts-component-list-and-chipset-pin-outs-for-analog-joypad-scph-1200)<br/>
[Pinouts - Component List and Chipset Pin-Outs for Analog Joypad, SCPH-110](pinouts.md#pinouts-component-list-and-chipset-pin-outs-for-analog-joypad-scph-110)<br/>



##   Controllers - Mouse
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
Plus: Dracula - The Resurrection<br/>

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
  PSX.Controller.Pin1 JOYDAT ---- brown  -- Mouse.Pin4
  PSX.Controller.Pin2 JOYCMD ---- red    -- Mouse.Pin3
  PSX.Controller.Pin3 +7.5V  ---- N/A
  PSX.Controller.Pin4 GND    ---- orange -- Mouse.Pin7 GND (G)
  PSX.Controller.Pin5 +3.5V  ---- yellow -- Mouse.Pin1
  PSX.Controller.Pin6 /JOYn  ---- green  -- Mouse.Pin5
  PSX.Controller.Pin7 JOYCLK ---- blue   -- Mouse.Pin2
  PSX.Controller.Pin8 /IRQ10 ---- N/A
  PSX.Controller.Pin9 /ACK   ---- purple -- Mouse.Pin6
  PSX.Controller.Shield --------- shield -- Mouse.Pin8 GND (SHIELD)
```

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



##   Controllers - Racing Controllers
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



##   Controllers - Lightguns
There are two different types of PSX lightguns (which are incompatible with
each other).<br/>

#### Namco Lightgun (GunCon)
Namco's Cinch-based lightguns are extracting Vsync/Hsync timings from the video
signal (via a cinch adaptor) (so they are working completely independed of
software timings).<br/>
[Controllers - Lightguns - Namco (GunCon)](controllersandmemorycards.md#controllers-lightguns-namco-guncon)<br/>

#### Konami Lightgun (IRQ10)
Konami's IRQ10-based lightguns are using the lightgun input on the controller
slot (which requires IRQ10/timings being properly handled at software side).<br/>
[Controllers - Lightguns - Konami Justifier/Hyperblaster (IRQ10)](controllersandmemorycards.md#controllers-lightguns-konami-justifierhyperblaster-irq10)<br/>
The IRQ10-method is reportedly less accurate (although that may be just due to
bugs at software side).<br/>

#### Third-Party Lightguns
There are also a lot of unlicensed lightguns which are either IRQ10-based, or
Cinch-based, or do support both.<br/>
For example, the Blaze Scorpion supports both IRQ10 and Cinch, and it does
additionally have a rumble/vibration function; though unknown how that rumble
feature is accessed, and which games are supporting it).<br/>

#### Lightgun Games
[Controllers - Lightguns - PSX Lightgun Games](controllersandmemorycards.md#controllers-lightguns-psx-lightgun-games)<br/>

#### Compatibilty Notes (IRQ10 vs Cinch, PAL vs NTSC, Calibration)
Some lightguns are reportedly working only with PAL or only with NTSC games
(unknown which guns, and unknown what is causing problems; the IRQ10 method
should be quite hardware independed, the GunCon variant, too, although
theoretically, some GunCon guns might have problems to extract Vsync/Hsync from
either PAL or NTSC composite signals).<br/>
Lightguns from different manufacturers are reportedly returning slightly
different values, so it would be recommended to include a calibration function
in the game, using at least one calibration point (that would also resolve
different X/Y offsets caused by modifying GP1 display control registers).<br/>
Lightguns are needing to sense light from the cathode ray beam; as such they
won't work on regions of the screen that contain too dark/black graphics.<br/>



##   Controllers - Lightguns - Namco (GunCon)
#### GunCon Cinch-based Lightguns (Namco)
```
  __Halfword 0 (Controller Info)___________________
  0-15  Controller Info  (5A63h=Namco Lightgun; GunCon/Cinch Type)
  __Halfword 1 (Buttons)___________________________
  0-2   Not used              (All bits always 1)
  3     Button A (Left Side)  (0=Pressed, 1=Released) ;aka Joypad Start
  4-12  Not used              (All bits always 1)
  13    Trigger Button        (0=Pressed, 1=Released) ;aka Joypad O-Button
  14    Button B (Right Side) (0=Pressed, 1=Released) ;aka Joypad X-Button
  15    Not used              (All bits always 1)
  __Halfword 2 (X)_________________________________
  0-15  8MHz clks since HSYNC (01h=Error, or 04Dh..1CDh)
  __Halfword 3 (Y)_________________________________
  0-15  Scanlines since VSYNC (05h/0Ah=Error, PAL=20h..127h, NTSC=19h..F8h)
```
Caution: The gun should be read only shortly after begin of VBLANK.<br/>

#### Error/Busy Codes
Coordinates X=0001h, Y=0005h indicates "unexpected light":<br/>
```
  ERROR: Sensed light during VSYNC (eg. from a Bulb or Sunlight).
```
Coordinates X=0001h, Y=000Ah indicates "no light", this can mean either:<br/>
```
  ERROR: no light sensed at all (not aimed at screen, or screen too dark).
  BUSY: no light sensed yet (when trying to read gun during rendering).
```
To avoid the BUSY error, one should read the gun shortly after begin of VBLANK
(ie. AFTER rendering, but still BEFORE vsync). Doing that isn't as simple as
one might think:<br/>
On a NTSC console, time between VBLANK and VSYNC is around 30000 cpu clks,
reading the lightgun (or analog joypads) takes around 15000 cpu clks. So,
reading two controllers within that timeframe may be problematic (and reading
up to eight controllers via multitaps would be absolutely impossible). As a
workaround, one may arrange the read-order to read lightguns at VBLANK (and
joypads at later time). If more than one lightgun is connected, then one may
need to restrict reading to only one (or maybe: max two) guns per frame.<br/>

#### Minimum Brightness
Below are some average minimum brightness values, the gun may be unable to
return position data near/below that limits (especially coordinates close to
left screen border are most fragile). The exact limits may vary from gun to
gun, and will also depend on the TV Set's brightness setting.<br/>
```
  666666h Minimum Gray
  770000h Minimum Blue
  007700h Minimum Green
  000099h Minimum Red
```
The gun does also work with mixed colors (eg. white bold text on black
background works without errors, but the returned coordinates are a bit "jumpy"
in that case; returning the position of the closest white pixels).<br/>
BUG: On a plain RED screen, aiming at Y\>=00F0h, the gun is randomly
returning either Y, or Y-80h (that error occurs in about every 2nd frame, ie.
at 50% chance). It's strange... no idea what is causing that effect.<br/>

#### Coordinates
The coordinates are updated in all frames (as opposed to some lightguns which
do update them only when pulling the trigger).<br/>
The absolute min/max coordinates may vary from TV set to TV set (some may show
a few more pixels than others). The relation of the gun's Screen Coodinates to
VRAM Coordinates does (obviously) depend on where the VRAM is located on the
screen; ie. on the game's GP1(06h) and GP1(07h) settings.<br/>
Vertical coordinates are counted in scanlines (ie. equal to pixels). Horizontal
coordinates are counted in 8MHz units (which would equal a resolution of 385
pixels; which can be, for example, converted to 320 pixel resolution as
X=X\*320/385).<br/>

#### Misinformation (from bugged homebrew source code)
```
  __Halfword 2 (X)_________________________________
  0-7   X-Coordinate  (actual: see X-Offset)             ;\with unspecified
  8-15  X-Offset      (00h: X=X-80, Nonzero: X=X-80+220) ;/dotclock?
  __Halfword 3 (Y)_________________________________
  0-7   Y-Coordinate  (actual: Y=Y-25) (but then, max is only 230, not 263 ?)
  8-15  Pad ID        (uh, what id?) (reportedly too dark/bright error flag?)
```

#### Namco Lightgun Drawing
```
           _-_______________________--_
  ----->  |    namco            \\\\   \    Namco G-Con 45 (light gray) (cinch)
  sensor   |............ .. .....\\\\...|_
          |_ :          :..   _____      _\
            |  O        :__../  )))|    (
             \__________/  |_\____/|     \
               :               :   |      |
               :               :   |      |  NPC-103
         A-Button (Left)   Trigger |      |  SLPH-00034/SLEH-0007/SLUH-00035
         B-Button (Right)          |______|
```

#### See also
[Pinouts - Component List and Chipset Pin-Outs for Namco Lightgun, NPC-103](pinouts.md#pinouts-component-list-and-chipset-pin-outs-for-namco-lightgun-npc-103)<br/>



##   Controllers - Lightguns - Konami Justifier/Hyperblaster (IRQ10)
#### Overall IRQ10-Based Lightgun Access
```
  Send  01h 42h 00h x0h 00h
  Reply HiZ 31h 5Ah buttons
```
The purpose of the "x0h" byte is probably to enable IRQ10 (00h=off, 10h=on),
this would allow to access more than one lightgun (with only one per frame
having the IRQ enabled).<br/>

#### Standard IRQ10-based Lightguns (Konami)
The Controller Data simply consists of the ID and buttons states:<br/>
```
  __Halfword 0 (Controller Info)___________________
  0-15  Controller Info  (5A31h=Konami Lightgun; Timer/IRQ10 type)
  __Halfword 1 (Buttons)
  0-2   Not used                 (All bits always 1)
  3     Start Button (Left Side) (0=Pressed, 1=Released)  ;aka Joypad Start
  4-13  Not used                 (All bits always 1)
  14    Back Button  (Rear End)  (0=Pressed, 1=Released)  ;aka Joypad X-Button
  15    Trigger Button           (0=Pressed, 1=Released)  ;aka Joypad []-Button
```
The coordinates aren't part of the controller data, instead they must be read
from Timer 0 and 1 upon receiving IRQ10 (see IRQ10 Notes below).<br/>

#### Konami Lightgun Drawing
```
     __                 ______ _
   _|__\_______________/  ___ \ \   Konami Justifier/Hyperblaster (light green)
  |   _______________ __ /   \ \ \
  |__|   _ _ _ _     |==|    O| \O\ .... Back Button (Rear End)
     |__:_:_:_:_:__  |___\__ /  ( (
                   |_|  ) \  :   \ \
      Trigger ......  \___/| :...|.|.... Start Button (Left Side)
                           |     | |
                           |     | | SLPH-00013/SLPH-00014/SLEH-0005/SLUH-00017
                          /     _|_|
                          \___--
```

#### Konami IRQ10 Notes
The PSX does have a lightgun input (Pin 8 of the controller), but, Sony did
apparently "forget" to latch the current cathode ray beam coordinates by
hardware when sensing the lightgun signal (quite strange, since that'd be a
simple, inexpensive, and very obvious feature for a gaming console).<br/>
Instead, the lightgun signal triggers IRQ10, and the interrupt handler is
intended to "latch" the coordinates by software (by reading Timer 0 and 1
values, which must configured to be synchronized with the GPU).<br/>
That method requires IRQ handling to be properly implemented in software
(basically, IRQs should not be disabled for longer periods, and DMA transfers
should not block the bus for longer periods). In practice, most programmers
probably don't realize how to do that, to the worst, Sony seems to have
delivered a slightly bugged library (libgun) to developers.<br/>
For details on Timers, see:<br/>
[Timers](timers.md)<br/>
In some consoles, IRQ10 seems to be routed through a Secondary IRQ Controller,
see:<br/>
[EXP2 DTL-H2000 I/O Ports](expansionportpio.md#exp2-dtl-h2000-io-ports)<br/>

#### IRQ10 Priority
For processing IRQ10 as soon as possible, it should be assigned higher priority
than all other IRQs (ie. when using the SysEnqIntRP BIOS function, it should be
the first/newest element in priority chain 0). The libgun stuff assigns an even
higher priority by patching the BIOS exception handler, causing IRQ10 to be
processed shortly before processing the priority chains (the resulting IRQ
priority isn't actually higher as when using 1st element of chain 0; the main
difference is that it skips some time consuming code which pushes registers
R4..R30). For details on that patch, see:<br/>
[BIOS Patches](kernelbios.md#bios-patches)<br/>
Even if IRQ10 has highest priority, execution of (older) other IRQs may cause a
new IRQ10 to be executed delayed (because IRQs are disabled during IRQ
handling), to avoid that problem: Best don't enable any other IRQs except IRQ0
and IRQ10, or, if you need other IRQs, best have them enabled only during
Vblank (there are no scanlines drawn during vblank, so IRQ10 should never
trigger during that period). DMAs might also slow down IRQ execution, so best
use them only during Vblank, too.<br/>

#### IRQ10 Timer Reading
To read the current timer values the IRQ10 handler would be required to be
called \<immediately\> after receiving the IRQ10 signal, which is more or
less impossible; if the main program is trying to read a mul/div/gte result
while the mul/div/gte operation is still busy may stop the CPU for some dozens
of clock cycles, and active DMA transfers or cache hits and misses in the IRQ
handler may cause different timings, moreover, timings may become completely
different if IRQs are disabled (eg. while another IRQ is processed).<br/>
However, IRQ10 does also get triggered in the next some scanlines, so the first
IRQ10 is used only as a notification that the CPU should watch out for further
IRQ10's. Ie. the IRQ10 handler should disable all DMAs, acknowledge IRQ10, and
then enter a waitloop that waits for the IRQ10 bit in I\_STAT to become set
again (or abort if a timeout occurs) and then read the timers, reportedly like
so:<br/>
```
  IF NTSC then X=(Timer0-140)*0.198166, Y=Timer1
  IF PAL  then X=(Timer0-140)*0.196358, Y=Timer1
```
No idea why PAL/NTSC should use different factors, that factors are looking
quite silly/bugged, theoretically, the pixel-to-clock ratio should be the
exactly same for PAL and NTSC...?<br/>
Mind that reading Timer values in Dotclock/Hblank mode is unstable, for Timer1
this can be fixed by the read-retry method, for Timer0 this could be done too,
but one would need to subtract the retry-time to get a correct coordinate;
alternately Timer0 can run at system clock (which doesn't require read-retry),
but it must be then converted to video clock (mul 11, div 7), and then from
video clock to dot clock (eg. div 8 for 320-pixel mode).<br/>
Above can be repeated for the next some scanlines (allowing to take the medium
values as result, and/or to eliminate faulty values which are much bigger or
smaller than the other values). Once when you have collected enough values,
disable IRQ10, so it won't trigger on further scanlines within the current
frame.<br/>

#### IRQ10 Bugs
BUG: The "libgun" library doesn't acknowledge the old IRQ10 \<immediately\>
before waiting for a new IRQ10, so the timer values after sensing the new IRQ10
are somewhat random (especially for the first processed scanline) (the library
allows to read further IRQ10's in further scanlines, which return more stable
results).<br/>
No idea how many times IRQ10 gets typically repeated? Sporting Clays allocates
a buffer for up to 20 scanlines (which would cause pretty much of a slowdown
since the CPU is just waiting during that period) (nethertheless, the game uses
only the first timer values, ie. the bugged libgun-random values).<br/>

Unknown if/how two-player games (with 2 lightguns) are working with the IRQ10
method... if IRQ10 is generated ONLY after pressing the trigger button, then it
may work, unless both players have Trigger pressed at the same time... and,
maybe one can enable/disable the lightguns by whatever commmand being sent to
the controller (presumably that "x0h" byte, see above), so that gun 1 generates
IRQ10 only in each second frame, and gun 2 only in each other frame...?<br/>



##   Controllers - Lightguns - PSX Lightgun Games
#### PSX Lightgun Games
Some games are working only with IRQ10 or only with Cinch, some games support
both methods:<br/>
```
  Area 51 (Mesa Logic/Midway) (IRQ10)
  Crypt Killer (Konami) (IRQ10)
  Die Hard Trilogy 1: (Probe Entertainment) (IRQ10)
  Die Hard Trilogy 2: Viva Las Vegas (n-Space) (IRQ10/Cinch)
  Elemental Gearbolt (Working Designs) (IRQ10/Cinch)
  Extreme Ghostbusters: Ultimate Invasion (LSP) (Cinch)
  Galaxian 3 (Cinch)
  Ghoul Panic (Namco) (Cinch)
  Gunfighter: The Legend of Jesse James (Rebellion) (Cinch)
  Judge Dredd (Gremlin) (Cinch)
  Lethal Enforcers 1-2 (Konami) (IRQ10)
  Maximum Force (Midway) (IRQ10/Cinch)
  Mighty Hits Special (Altron) (EU/JPN) (Cinch)
  Moorhuhn series (Phenomedia) (Cinch)
  Point Blank 1-3 (Namco) (Cinch)
  Project Horned Owl (Sony) (IRQ10)
  Rescue Shot (Namco) (Cinch)
  Resident Evil: Gun Survivor (Capcom) (JPN/PAL versions) (Cinch)
  Silent Hill (IRQ10) ("used for an easter egg")
  Simple 1500 Series Vol.024 - The Gun Shooting (unknown type)
  Simple 1500 Series Vol.063 - The Gun Shooting 2 (unknown type)
  Snatcher (IRQ10)
  Sporting Clays (Charles Doty) (homebrew with buggy source code) (IRQ10/Cinch)
  Star Wars: Rebel Assault II (IRQ10)
  Time Crisis, and Time Crisis 2: Project Titan (Namco) (Cinch)
```
Note: The RPG game Dragon Quest Monsters does also contain IRQ10 lightgun code
(though unknown if/when/where the game does use that code).<br/>



##   Controllers - Rumble Configuration
Rumble (aka "Vibration Function") is basically controlled by two previously
unused bytes of the standard controller Read command.<br/>
There are two methods to control the rumble motors, the old method is very
simple (but supports only one motor), the new method envolves a bunch of new
configuration commands (and supports two motors).<br/>
```
  SCPH-1150 DualAnalog Pad with 1 motor                 ;-old rumble method
  SCPH-1200 DualAnalog Pad with 2 motors, PSX-design    ;\new rumble method
  SCPH-110  DualAnalog Pad with 2 motors, PSone-design  ;/
  Blaze Scorpion Lightgun with rumble      ;\unknow how to control rumble
  Fishing controllers with rumble          ;/
  SCPH-1180 Analog Pad without rumble      ;\unknow if there're config commands
  SCPH-1110 Analog Stick without rumble    ;/for analog mode (probably not)
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

#### Normal Mode
```
  42h "B" Read Buttons (and analog inputs when in analog mode)
  43h "C" Enter/Exit Configuration Mode (stay normal, or enter)
```

#### Configuration Mode
```
  40h "@" Unknown (response HiZ F3h 5Ah 6x00h)
  41h "A" Unknown (response HiZ F3h 5Ah 6x00h)
  42h "B" Read Buttons AND analog inputs (even when in digital mode)
  43h "C" Enter/Exit Configuration Mode (stay config, or exit)
  44h "D" Set LED State (analog mode on/off)
  45h "E" Get LED State (and whatever other status/version values)
  46h "F" Get Variable Response A (depending on incoming bit)
  47h "G" Get whatever values (response HiZ F3h 5Ah 00h 00h 02h 00h 01h 00h)
  48h "H" Unknown (response HiZ F3h 5Ah 00h 00h 00h 00h 01h 00h)
  49h "I" Unknown (response HiZ F3h 5Ah 6x00h)
  4Ah "J" Unknown (response HiZ F3h 5Ah 6x00h)
  4Bh "K" Unknown (response HiZ F3h 5Ah 6x00h)
  4Ch "L" Get Variable Response B (depending on incoming bit)
  4Dh "M" Unlock Rumble (and select response length)
  4Eh "N" Unknown (response HiZ F3h 5Ah 6x00h)
  4Fh "O" Unknown (response HiZ F3h 5Ah 6x00h)
```

#### Normal Mode - Command 42h "B" - Read Buttons (and analog inputs when enabled)
```
  Send  01h 42h 00h xx  yy  (00h 00h 00h 00h)
  Reply HiZ id  5Ah buttons ( analog-inputs )
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
  Send  01h 43h 00h xx  00h (zero padded...)
  Reply HiZ id  5Ah buttons (analog inputs...)
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
with normal command 42h. Some controller revisions will only change config mode
state upon receiving the entire command sequence while others will set it
immediately on receiving the xx byte. So while aborting the command sequence
early (i.e. setting JOY_CTRL to 0 after sending xx, which some homebrew software
does) may work for setting config mode state on some controllers, in practice
this technique is undefined behavior and use should be avoided.<br/>

#### Config Mode - Command 44h "D" - Set LED State (analog mode on/off)
```
  Send  01h 44h 00h val sel 00h 00h 00h 00h
  Reply HiZ F3h 5Ah 00h 00h 00h 00h 00h 00h
```
If "sel=02h", then "val" is applied as new LED state (val=00h for LED off aka
Digital mode, and val=01h for LED on/red aka analog mode).<br/>

#### Config Mode - Command 45h "E" - Get LED State (and whatever values)
```
  Send  01h 45h 00h 00h 00h 00h 00h 00h 00h
  Reply HiZ F3h 5Ah 01h 02h val 02h 01h 00h
```
Returns val=00h for LED off, and val=01h for LED on/red. The other values might
indicate the number of rumble motors, analog inputs, or version information, or
so.<br/>

#### Config Mode - Command 46h "F" - Get Variable Response A
```
  Send  01h 46h 00h xx  00h 00h 00h 00h 00h
  Reply Hiz F3h 5Ah 00h 00h yy  yy  yy  yy
```
Purpose unknown. Response varies: If xx=00h then yy=01h,02h,00h,0ah, else if
xx=01h then yy=01h,01h,01h,14h.<br/>

#### Config Mode - Command 47h "G" - Get whatever values
```
  Send  01h 47h 00h 00h 00h 00h 00h 00h 00h
  Reply HiZ F3h 5Ah 00h 00h 02h 00h 01h 00h
```
Purpose unknown.<br/>

#### Config Mode - Command 4Ch "L" - Get Variable Response B
```
  Send  01h 4Ch 00h xx  00h 00h 00h 00h 00h
  Reply Hiz F3h 5Ah 00h 00h 00h yy  00h 00h
```
Purpose unknown. Response varies: If xx=00h then yy=04h, else if xx=01h then
yy=07h.<br/>

#### Config Mode - Command 4Dh "M" - Unlock Rumble (and select response length)
```
  Send  01h 4Dh 00h aa  bb  cc  dd  ee  ff
  Reply Hiz F3h 5Ah <-----old values----->
```
This command does basically unlock the rumble motors (so they can be controlled
with command 42h), this is usually done by setting aa..ff to 00h, 01h, FFh,
FFh, FFh, FFh. There are billons of other combinations for aa..ff, some rules
are:<br/>
```
  when cc.bit1-7 are all zero --> transfer one extra halfword
  when ee.bit1-7 are all zero --> transfer another extra halfword
  when cc,dd,ee,ff are ALL nonzero --> unlock small motor
  when aa=01h --> unlock large motor (and swap VAL1 and VAL2)
  when bb=01h --> unlock large motor (default)
  when cc.bit0=1 --> disable large motor (unless cc.bit7=1)
  when ff.bit0=1 --> disable large motor (unless something)
```
The extra halfword(s) increase the transfer length by 1 or 2 halfwords (and
accordingly, the digital mode ID changes from 41h to 42h or 43h), the
controller returns 00h bytes for the extra halfwords, in analog mode, the ID
and transfer length remains unchanged (since it always has extra halfwords for
analog responses). So, the extra halfwords seem to be output to the controller
(rather than response data), possibly intended to control additional rumble
motors or to output data to other hardware features.<br/>

#### Config Mode - Command 48h "H" - Unknown (response HiZ F3h 5Ah 4x00h 01h 00h)
```
  Send  01h 48h 00h 00h 00h 00h 00h 00h 00h
  Reply HiZ F3h 5Ah 00h 00h 00h 00h 01h 00h
```
This command does return a bunch of 00h bytes, and one 01h byte. Purpose
unknown. The command does not seem to be used by any games.<br/>

#### Config Mode - Command 40h "@" - Unknown (response HiZ F3h 5Ah 6x00h)
#### Config Mode - Command 41h "A" - Unknown (response HiZ F3h 5Ah 6x00h)
#### Config Mode - Command 49h "I" - Unknown (response HiZ F3h 5Ah 6x00h)
#### Config Mode - Command 4Ah "J" - Unknown (response HiZ F3h 5Ah 6x00h)
#### Config Mode - Command 4Bh "K" - Unknown (response HiZ F3h 5Ah 6x00h)
#### Config Mode - Command 4Eh "N" - Unknown (response HiZ F3h 5Ah 6x00h)
#### Config Mode - Command 4Fh "O" - Unknown (response HiZ F3h 5Ah 6x00h)
```
  Send  01h 4xh 00h 00h 00h 00h 00h 00h 00h
  Reply HiZ F3h 5Ah 00h 00h 00h 00h 00h 00h
```
These commands do return a bunch of 00h bytes. Purpose unknown. These commands
do not seem to be used by any games.<br/>

#### Note
Rumble is a potentially annoying feature, so games that do support rumble
should also include an option to disable it.<br/>



##   Controllers - Dance Mats
PSX Dance Mats are essentially normal joypads with uncommonly arranged buttons,
the huge mats are meant to be put on the floor, so the user could step on them.<br/>

#### Dance Mat vs Joypad Compatibility
There are some differences to normal joypads: First of, the L1/L2/R1/R2
shoulder buttons are missing in most variants. And, the mats are allowing to
push Left+Right and Up+Down at once, combinations that aren't mechanically
possible on normal joypads (some dancing games do actually require those
combinations, whilst some joypad games may get confused on them).<br/>

#### Dance Mat Unknown Things
Unknown if the mat was sold in japan, and if so, with which SLPH/SCPH number.<br/>
Unknown if the mat's middle field is also having a button assigned.<br/>
Unknown if the mat is having a special controller ID, or if there are other
ways to detect mats (the mats are said to be compatible with skateboard games,
so the mats are probably identifying themselves as normal digital joypad;
assuming that those skateboard games haven't been specifically designed for
mats).<br/>

#### Dance Mat Games
```
  D.D.R. Dance Dance Revolution 2nd Remix
  (and maybe whatever further games)
```
The mats can be reportedly also used with whatever skateboard games.<br/>

#### Dance Mat Variants
There is the US version (DDR Dance Pad, SLUH-00071), and a slightly different
European version (Official Dance Mat, SLEH-00023: shiny latex style with
perverted colors, and Start/Select arranged differently). The japanese version
(RU017) resembles the US version, but without Triangle/Square symbols drawn in
lower left/right edges.<br/>
And there is a handheld version (with additional L1/L2/R2/R1 buttons; maybe
unlicensed; produced as MINI DDR, and also as Venom Mini Dance Pad).<br/>

```
   US Version (white/black/red/blue)         Handheld Version (blue/gray)
    __________.---------.___________          _____/ MINI  \_____
   |          \         /           |        |      D.D.R.       |
   |  SELECT   '-------'    START   |        |L1 L2 SEL STA R2 R1|
   |------------.------.------------|        | ___    ___    ___ |
   |  .''''.   /        \   .''''.  |        || X |  | ^ |  | O ||
   | |  \/  | |    /\    | | .''. | |        ||___|  |___|  |___||
   | |  /\  | |   /..\   | | '..' | |        | ___   .---.   ___ |
   |  '....'  '.   ||   .'  '....'  |        || < | |Stay | | > ||
   | .-------. .''''''''. .-------. |        ||___| |Cool!| |___||
   |/   /|   .'          '.   |\   \|        | ___   '___'   ___ |
   |   / |-- |            | --| \   |        || []|  | v |  | /\||
   |   \ |-- | Stay Cool! | --| /   |        ||___|  |___|  |___||
   |\   \|   '.          .'   |/   /|        |___________________|
   | '-------' '........' '-------' |
   |  .''''.  .'   ||   '.  .''''.  |        Gothic Dance Mat (black/silver)
   | |  /\  | |   \''/   | | |''| | |         _.----------._
   | | /__\ | |    \/    | | |..| | |        | \ SEL  STA / | This one
   |  '....'   \        /   '....'  |        |  '--------'  | wasn't ever
   '------------'------'------------'        | .----------. | produced,
                                             | |  .''''.  | | as cool as
   European Version (pink/blue/yellow)       | | |  /\  | | | it could have
    __________.---------.___________         | | | /..\ | | | been, the lame
   |          \ SEL STA /           |        | |  '.||.'  | | marketing
   |           '-------'            |        | +----------+ | people didn't
   |----------.----------.----------|        | |  .''''.  | | even think
   |  .''''.  |  .''''.  |  .''''.  |        | | |  /\  | | | about it.
   | |  \/  | | |  /\  | | | .''. | |        | | | /..\ | | |
   | |  /\  | | | /..\ | | | '..' | |        | |  '.||.'  | |
   |  '....'  |  '.||.'  |  '....'  |        | +----------+ |
   |----------+-..    ..-+----------|        | |  .'||'.  | |
   |  .'/|'.  /   ''''   \  .'|\'.  |        | | | \''/ | | |
   | | / |--|/            \|--| \ | |        | | |  \/  | | |
   | | \ |--|\            /|--| / | |        | |  '....'  | |
   |  '.\|.'  \   ....   /  '.|/.'  |        | +----------+ |
   |----------+-''    ''-+----------|        | |  .'||'.  | |
   |  .''''.  |  .'||'.  |  .''''.  |        | | | \''/ | | |
   | |  /\  | | | \''/ | | | |''| | |        | | |  \/  | | |
   | | /__\ | | |  \/  | | | |..| | |        | |  '....'  | |
   |  '....'  |  '....'  |  '....'  |        | '----------' '
   '----------|----------|----------'        '--------------'
```

#### Stay Cool?
Despite of the "Stay Cool!" slogan, the mat wasn't very cool - not at all! It
offered only two steps back-and-forth, and also allowed to do extremly uncool
side-steps. Not to mention that it would melt when dropping a burning cigarette
on it. Stay Away!<br/>



##   Controllers - Fishing Controllers
The fishing rods are (next to lightguns) some of the more openly martial
playstation controllers - using the credo that "as long as you aren't using
dynamite: it's okay to kill them cause they don't have any feelings."<br/>

#### PSX Fishing Controller Games
```
  Action Bass (Syscom Entertainment) (1999) (SLPH-00100)
  Bass Landing (ASCII/agetec) (1999) (SLPH-00100, SLUH-00063)
  Bass Rise, Fishing Freaks (Bandai) (1999) (BANC-0001)
  Bass Rise Plus, Fishing Freaks (Bandai) (2000) (BANC-0001, SLPH-00100)
  Breath of Fire IV (Capcom) (SLUH-00063)
  Championship Bass (EA Sports) (2000) (SLUH-00063)
  Fish On! Bass (Pony Canyon) (1999) (BANC-0001, SLPH-00100)
  Fisherman's Bait 2/Exiting Bass2 - Big Ol'Bass(Konami)(SLPH-00100,SLUH-00063)
  Fishing Club: (series with 3 titles) (have "headset-logo" on back?)
  Lake Masters II (1999) (Dazz/Nexus) (SLPH-00100)
  Lake Masters Pro (1999) (Dazz/Nexus) (BANC-0001, SLPH-00100)
  Let's Go Bassfishing!: Bass Tsuri ni Ikou! (Banpresto) (1999) (SLPH-00100)
  Matsukata Hiroki no World Fishing (BPS The Choice) (1999) (SLPH-00100)
  Murakoshi Seikai-Bakuchou Nihon Rettou (Victor) (SLPH-00100)
  Murakoshi Masami-Bakuchou Nippon Rettou:TsuriConEdition (1999) (SLPH-00100)
  Pakuchikou Seabass Fishing (JP, 03/25/99) (Victor) (SLPH-00100)
  Perfect Fishing: Bass Fishing (2000) (Seta) (yellow/green logo)
  Perfect Fishing: Rock Fishing (2000) (Seta) (yellow/green logo)
  Oyaji no Jikan: Nechan, Tsuri Iku De! (2000) (Visit) (BANC-0001, SLPH-00100)
  Reel Fishing II / Fish Eyes II (2000)(Natsume/Victor)(SLPH-00100, SLUH-00063)
  Simple 1500 Series Vol. 29: The Tsuri (2000) (yellow/green logo)
  Suizokukan Project: Fish Hunter e no Michi (1999)(Teichiku)(SLPH-00100)
  Super Bass Fishing (1999) (King) (BANC-0001, SLPH-00100, yellow/green logo)
  Super Black Bass X2 (2000) (Starfish) (SLPH-00100)
  Tsuwadou Keiryuu Mizuumihen (Best Edition)(2000) (ASCII PS1+PS2 controllers?)
  Tsuwadou Seabass Fishing (PlayStation the Best) (1999) (Oz Club) (SLPH-00100)
  Uki Uki Tsuri Tengoku Nagami/Uokami Densetsu Oe (2000) (Teichiku)(SLPH-00100)
  Umi no Nushi Tsuri-Takarajima ni Mukatte (1999)(Victor)(BANC-0001,SLPH-00100)
  Winning Lure (Hori) (2000) (for Hori HPS-97 controller)  AKA HPS-98 ?
```
For more see: http://www.gamefaqs.com/ps/list-109
(sports-\>nature-\>fishing)<br/>

#### Logos on CD Covers
US Fishing games should have a "SLUH-00063" logo. European Fishing games don't
have any fishing logos; apparently fishing controllers haven't been officially
released/supported in Europe.<br/>
Japanese Fishing games can have a bunch of logos: Usually BANC-0001 or
SLPH-00100 (or both).<br/>
Moreover, some japanese games have a yellow/green fishing logo with japanese
text (found on Perfect Fishing: Bass Fishing, Perfect Fishing: Rock Fishing,
Simple 1500 Series Vol. 29: The Tsuri, Super Bass Fishing) (unknown if that
logo refer to other special hardware, or if it means the "normal" BANC-0001 or
SLPH-00100 controllers.<br/>
And Moreover, some japanese games have some sort of "headset" logos with
japanese text, these seem to have same meaning as SLPH-00100; as indicated by
photos on CD cover of Tsuwadou Keiryuu Mizuumihen (Best Edition) (2000); that
CD cover also has a "headset 2" logo, which seems to mean a newer PS2 variant
of the SLPH-00100.<br/>

#### PSX Fishing Controllers
```
  ASCII SLPH-00100 (silver)
  ASCII PS2-version? (silver) (similar to SLPH-00100, with new mode switch?)
  agetec SLUS-00063 (silver) (US version of ASCII's SLPH-00100 controller)
  Bandai BANC-0001 (dark gray/blue) (has less buttons than ASCII/agetec)
  Interact Fission (light gray/blue)(similar to ASCII/agetec, 2 extra buttons?)
  Naki (transparent blue) (looks like a clone of the ASCII/agetec controllers)
  Hori HPS-97/HPS-98 (black/gray) (a fishing rod attached to a plastic fish)
```
Of these, the ASCII/agetec controllers seem to be most popular (and most
commonly supported). The Bandai contoller is also supported by a couple of
games (though the Bandai controller itself seems to be quite rare). The
Interact/Naki controllers are probably just clones of the ASCII/agetec ones.
The Hori controller is quite rare (and with its string and plastic fish, it's
apparently working completely different than the other fishing controllers).<br/>

#### Tech Info (all unknown)
Unknown how to detect fishing controllers.<br/>
Unknown how to read buttons, joystick, crank, motion sensors.<br/>
Unknown how to control rumble/vibration.<br/>
Unknown if/how Bandai differs from ASCII/agetec (aside from less buttons).<br/>
Unknown how the Hori thing works.<br/>

#### ASCII SLPH-00100 / agetec SLUH-00063 (silver)
```
          ___
       __|___|__
     _|         |_     _   __
    | |         | |   | |=|__| <--- crank handle
    | | SEL STA | |   | |
    | |         | |---|  \                         ASCII SLPH-00100
    |  \       /  |---|  /                         agetec SLUH-00063
   /  L1       R1  \  | |  __
  |  L2  .---.  R2  | |_|=|__|
  |     | joy |     |
  |     |stick|     |  <------- analog thumb controlled joystick
  | /\   '---'   >< |
  |   []       ()   |
   \     ASCII     /
    '.___________.'   \___ 10 buttons (SEL,STA,L1,L2,R1,R2,/\,[],(),><)
       \ _____ /
        |     |           Note: many (not all) agetec controllers
        |     |           have the >< and () buttons exchanged
        |     |
        |     |              Aside from the crank/buttons/joystick,
        |     |              the controller reportedly contains:
        |     |              some sort of motion sensors?
        |     |              some kind of rumble/vibration?
        |     |
        '.___.'
           '--...___ cable
```

#### Bandai BANC-0001 (dark gray/blue)
```
          ___
       __|___|__
     _|         |      _   __
    | .---.     |\    | |=|__| <--- crank handle
    || joy |    | |   | |
    ||stick|    | |-#-|  \
    | '---'     | |-#-|  /
   / \          |  \  | |  __
  |   |   ...   |   | |_|=|__|
  |   |  :   :  | ()|
  |   |O :___: O|   |   <--- two buttons: () and ><
  |   |- |___| -| ><|        and some slide switch with I and 0 positions?
  |   |         |   |
   \  |  BANDAI |  /      unknown if the joystick is digital or analog
    '._\_______/_.'
       |       |          unknown if there are motion sensors and/or rumble
       '.     .'
        |     |
        |     |
        |     |
        |     |
        |     |
        |     |
        |     |
        '.___.'
           '--...___ cable
```

#### Hori HPS-97 / HPS-98 (black/gray)
```
              ....----------------O
           .''                     \  HPS-97 (controller bundled with game)
          _:_        \              \ HPS-98 (controller only, for HPS-96 game)
       __|___|__      \ short        \
     _|         |_      elastic       \
    |             |     pole           \
    |             |                     \    <--- string (from pole to
    |     SW?     |     _   __           \        reel inside of fish)
   /               \   | |=|__|           \
  |      .---.      |  | |                 \
  | ( ) | joy |     |--|  \                 \               ___
  |     |stick|     |--|  /                  \             /   /
  | ( )  '---'      |  | |  __                \     ...---''''''--.  /|
  |                 |  |_|=|__| <--- crank     \   '               '/ |
   \    ( ) ( )    /                 handle     '..|                  |.
    '.___________.'                                |__________________| :
       \       /     \                                plastic fish      :
        |     |       joystick,                  (presumable some heavy :
        |     |       four buttons,              stationary thing that  :
        |     |       and a switch?              rests on floor)        :
        |     |                                  (presumably with       :
        |     |                                  motor-driven reel?)    :
        |     |                                                         :
        |     |     the two cables do probably connect                  :
        |     |     to both of the PSX controller slots                 :
        '.___.'                                            cable 2  ---'
           '--...___ cable 1
```



##   Controllers - I-Mode Adaptor (Mobile Internet)
The I-Mode Adaptor cable (SCPH-10180) allows to connect an I-mode compatible
mobile phone to the playstation's controller port; granting a mobile internet
connection to japanese games.<br/>

#### PSX Games for I-Mode Adaptor (Japan only)
```
  Doko Demo Issyo (PlayStation the Best release only) (Sony) 2000
  Doko Demo Issyo Deluxe Pack (Bomber eXpress/Sony) 2001
  Hamster Club-I (SLPS-03266) (Jorudan) 2002
  iMode mo Issyo: Dokodemo Issho Tsuika Disc (Bomber/Sony) 2001
  Keitai Eddy (iPC) 2000 (but, phone connects to SIO port on REAR side of PSX?)
  Komocchi (Victor) 2001
  Mobile Tomodachi (Hamster) 2002
  Motto Trump Shiyouyo! i-Mode de Grand Prix (Pure Sound) 2002
  One Piece Mansion (Capcom) 2001 (japanese version only)
```
The supported games should have a I-Mode adaptor logo on the CD cover (the logo
depicts two plugs: the PSX controller plug, and the smaller I-Mode plug).<br/>
Note: "Dragon Quest Monsters 1 & 2" was announced/rumoured to support
I-mode (however, its CD cover doesn't show any I-Mode adapter logo).<br/>

#### Tech Details (all unknown)
Unknown how to detect the thing, and how to do the actual data transfers.<br/>
The cable does contain a 64pin chip, an oscillator, and some smaller components
(inside of the PSX controller port connector).<br/>

#### Hardware Variant
Keitai Eddy seems to have the phone connect to the SIO port (on rear side of
the PSX, at least it's depicted like so on the CD cover). This is apparently
something different than the SCPH-10180 controller-port cable. Unknown what it
is exactly - probably some mobile internet connection too, maybe also using
I-mode, or maybe some other protocol.<br/>



##   Controllers - Additional Inputs
#### Reset Button
PSX only (not PSone). Reboots the PSX via /RESET signal. Probably including for
forcefully getting through the WHOLE BIOS Intro, making it rather
useless/annoying? No idea if it clears ALL memory during reboot?<br/>

#### CDROM Shell Open
Status bit of the CDROM controller. Can be used to sense if the shell is opened
(and also memorizes if the shell was opened since last check; allowing to sense
possible disk changes).<br/>

#### PocketStation
Memory Card with built-in LCD screen and Buttons (which can be used as
miniature handheld console). However, when it is connected to the PSX, the
buttons are vanishing in the cartridge slot, so the buttons cannot be used as
additional inputs for PSX games.<br/>

#### Serial Port PSX only (not PSone)
With an external adaptor (voltage conversion), the serial port can be used
(among others) to connect a RS232 Serial Mouse. Although, most or all
commercial games with mouse input are probably (?) supporting only Sony's Mouse
(on the controller port) (rather than standard RS232 devices on the serial
port).<br/>

#### TTY Debug Terminal
If present, the external DUART can be used for external keyboard input, at the
BIOS side, this is supported as "std\_in".<br/>



##   Controllers - Misc
#### Standard Controllers
```
  SCPH-1010  digital joypad (with short cable)
  SCPH-1080  digital joypad (with longer cable)
  SCPH-1030  mouse (with short cable)
  SCPH-1090  mouse (with longer cable)
  SCPH-1092  mouse (european?)
  SCPH-1110  analog joystick
  SCPH-1150  analog joypad (with one vibration motor, with red/green led)
  SCPH-1180  analog joypad (without vibration motors, with red/green led)
  SCPH-1200  analog joypad (with two vibration motors) (dualshock)
  SCPH-110   analog joypad (with two vibration motors) (dualshock for psone)
  SCPH-10010 dualshock2 (analog buttons, except L3/R3/Start/Select) (for ps2)
  SCPH-1070  multitap
```

#### Special Controllers
```
  SCPH-4010 VPick (guitar-pick controller) (for Quest for Fame, Stolen Song)
```
SLPH-0001 (nejicon)<br/>
BANDAI "BANC-0002" - 4 Buttons (Triangle, Circle, Cross, Square) (nothing more)<br/>

#### SCPH-2000 Keyboard/Mouse adapter
A PS/2 to PSX controller port adaptor, for educational Lightspan titles.<br/>
There are two variants of the adaptor:<br/>
```
  Adaptor with short cable to PSX-controller port (and prototype marking)
  Adaptor without cable, directly plugged into controller port (final version?)
```

#### Joystick
```
     __________                     __________
    |          |                   |    ^     |     ^
    | L1    R1 |                   | X <+> O  |    <+> = Digital Stick
     \      ___| <--- L2   [] ---> |___ v    /      v
      |    |     <--- R2   /\ --->     |    |
   ___|    |___________________________|    |___   Not sure if all buttons
  |   |    | SEL STA              =?=  |    |   |  are shown at their
  |   |    |                           |    |   |  correct locations?
  |   |    |_         []   /\         _|    |   |
  |  _|     /    L1             R1    \     |_  |
  |  \_____/          X     O          \_____/  |
  |   /___\      L2             R2      /___\   |
  |                                             |
  |                                             |
   \___________________________________________/
```

```
 The thumb buttons on the left act as L1 and R1,
    the trigger is L2, the pinky button is R2
 The thumb buttons on the right act as X and O,
    the trigger is Square and the pinky button is Triangle.
 I find this odd as the triggers should've been L1 and R1,
    the pinkies L2 and R2.
 The buttons are redundantly placed on the base as large buttons like what
    you'd see on a fight/arcade stick. Also with Start and Select.
 There is also a physical analog mode switch,
    not a button like on dual shock.
```



##   Memory Card Read/Write Commands
#### Reading Data from Memory Card
```
  Send Reply Comment
  81h  N/A   Memory Card Access (unlike 01h=Controller access), dummy response
  52h  FLAG  Send Read Command (ASCII "R"), Receive FLAG Byte
  00h  5Ah   Receive Memory Card ID1
  00h  5Dh   Receive Memory Card ID2
  MSB  (00h) Send Address MSB  ;\sector number (0..3FFh)
  LSB  (pre) Send Address LSB  ;/
  00h  5Ch   Receive Command Acknowledge 1  ;<-- late /ACK after this byte-pair
  00h  5Dh   Receive Command Acknowledge 2
  00h  MSB   Receive Confirmed Address MSB
  00h  LSB   Receive Confirmed Address LSB
  00h  ...   Receive Data Sector (128 bytes)
  00h  CHK   Receive Checksum (MSB xor LSB xor Data bytes)
  00h  47h   Receive Memory End Byte (should be always 47h="G"=Good for Read)
```
Non-sony cards additionally send eight 5Ch bytes after the end flag.<br/>
When sending an invalid sector number, original Sony memory cards respond with
FFFFh as Confirmed Address (and do then abort the transfer without sending any
data, checksum, or end flag), third-party memory cards typically respond with
the sector number ANDed with 3FFh (and transfer the data for that adjusted
sector number).<br/>

#### Writing Data to Memory Card
```
  Send Reply Comment
  81h  N/A   Memory Card Access (unlike 01h=Controller access), dummy response
  57h  FLAG  Send Write Command (ASCII "W"), Receive FLAG Byte
  00h  5Ah   Receive Memory Card ID1
  00h  5Dh   Receive Memory Card ID2
  MSB  (00h) Send Address MSB  ;\sector number (0..3FFh)
  LSB  (pre) Send Address LSB  ;/
  ...  (pre) Send Data Sector (128 bytes)
  CHK  (pre) Send Checksum (MSB xor LSB xor Data bytes)
  00h  5Ch   Receive Command Acknowledge 1
  00h  5Dh   Receive Command Acknowledge 2
  00h  4xh   Receive Memory End Byte (47h=Good, 4Eh=BadChecksum, FFh=BadSector)
```

#### Get Memory Card ID Command
```
  Send Reply Comment
  81h  N/A   Memory Card Access (unlike 01h=Controller access), dummy response
  53h  FLAG  Send Get ID Command (ASCII "S"), Receive FLAG Byte
  00h  5Ah   Receive Memory Card ID1
  00h  5Dh   Receive Memory Card ID2
  00h  5Ch   Receive Command Acknowledge 1
  00h  5Dh   Receive Command Acknowledge 2
  00h  04h   Receive 04h
  00h  00h   Receive 00h
  00h  00h   Receive 00h
  00h  80h   Receive 80h
```
This command is supported only by original Sony memory cards. Not sure if all
sony cards are responding with the same values, and what meaning they have,
might be number of sectors (0400h) and sector size (0080h) or whatever.<br/>

#### Invalid Commands
```
  Send Reply Comment
  81h  N/A   Memory Card Access (unlike 01h=Controller access), dummy response
  xxh  FLAG  Send Invalid Command (anything else than "R", "W", or "S")
```
Transfer aborts immediately after the faulty command byte, or, occasionally
after one more byte (with response FFh to that extra byte).<br/>

#### FLAG Byte
The initial value of the FLAG byte on power-up (and when re-inserting the
memory card) is 08h.<br/>
Bit3=1 is indicating that the directory wasn't read yet (allowing to sense
memory card changes). For some strange reason, bit3 is NOT reset when reading
from the card, but rather when writing to it. To reset the flag, games are
usually issuing a dummy write to sector number 003Fh, more or less
unneccessarily stressing the lifetime of that sector.<br/>
Bit2=1 seems to be intended to indicate write errors, however, the write
command seems to be always finishing without setting that bit, instead, the
error flag may get set on the NEXT command.<br/>
Note: Some (not all) non-sony cards also have Bit5 of the FLAG byte set.<br/>

#### Timings
IRQ7 is usually triggered circa 1500 cycles after sending a byte (counted from
the begin of the first bit), except, the last byte doesn't trigger IRQ7, and,
after the 7th byte of the Read command, an additional delay of circa 31000
cycles occurs before IRQ7 gets triggered (that strange extra delay occurs only
on original Sony cards, not on cards from other manufacturers).<br/>
There seems to be no extra delays in the Write command, as it seems, the data
is written on the fly, and one doesn't need to do any write-busy handling...
although, theoretically, the write shouldn't start until verifying the
checksum... so it can't be done on the fly at all...?<br/>

#### Notes
Responses in brackets are don't care, (00h) means usually zero, (pre) means
usually equal to the previous command byte (eg. the response to LSB is MSB).<br/>

Memory cards are reportedly "Flash RAM" which sounds like bullshit, might be
battery backed SRAM, or FRAM, or slower EEPROM or FLASH ROM, or vary from card
to card...?<br/>



##   Memory Card Data Format
#### Data Size
```
  Total Memory 128KB = 131072 bytes = 20000h bytes
  1 Block 8KB = 8192 bytes = 2000h bytes
  1 Frame 128 bytes = 80h bytes
```
The memory is split into 16 blocks (of 8 Kbytes each), and each block is split
into 64 sectors (of 128 bytes each). The first block is used as Directory, the
remaining 15 blocks are containing Files, each file can occupy one or more
blocks.<br/>

#### Header Frame (Block 0, Frame 0)
```
  00h-01h Memory Card ID (ASCII "MC")
  02h-7Eh Unused (zero)
  7Fh     Checksum (all above bytes XORed with each other) (usually 0Eh)
```

#### Directory Frames (Block 0, Frame 1..15)
```
  00h-03h Block Allocation State
            00000051h - In use ;first-or-only block of a file
            00000052h - In use ;middle block of a file (if 3 or more blocks)
            00000053h - In use ;last block of a file   (if 2 or more blocks)
            000000A0h - Free   ;freshly formatted
            000000A1h - Free   ;deleted (first-or-only block of file)
            000000A2h - Free   ;deleted (middle block of file)
            000000A3h - Free   ;deleted (last block of file)
  04h-07h Filesize in bytes (2000h..1E000h; in multiples of 8Kbytes)
  08h-09h Pointer to the NEXT block number (minus 1) used by the file
            (ie. 0..14 for Block Number 1..15) (or FFFFh if last-or-only block)
  0Ah-1Eh Filename in ASCII, terminated by 00h (max 20 chars, plus ending 00h)
  1Fh     Zero (unused)
  20h-7Eh Garbage (usually 00h-filled)
  7Fh     Checksum (all above bytes XORed with each other)
```
Filesize [04h..07h] and Filename [0Ah..1Eh] are stored only in the first
directory entry of a file (ie. with State=51h or A1h), other directory entries
have that bytes zero-filled.<br/>

#### Filename Notes
The first some letters of the filename should indicate the game to which the
file belongs, in case of commercial games this is conventionally done like so:
Two character region code:<br/>
```
  "BI"=Japan, "BE"=Europe, "BA"=America
```
followed by 10 character game code,<br/>
```
  in "AAAA-NNNNN" form     ;for Pocketstation executables replace "-" by "P"
```
where the "AAAA" part does imply the region too; (SLPS/SCPS=Japan,
SLUS/SCUS=America, SLES/SCES=Europe) (SCxS=Made by Sony, SLxS=Licensed by
Sony), followed by up to 8 characters,<br/>
```
  "abcdefgh"
```
(which may identify the file if the game uses multiple files; this part often
contains a random string which seems to be allowed to contain any chars in
range of 20h..7Fh, of course it shouldn't contain "?" and "\*" wildcards).<br/>

#### Broken Sector List (Block 0, Frame 16..35)
```
  00h-03h Broken Sector Number (Block*64+Frame) (FFFFFFFFh=None)
  04h-7Eh Garbage (usually 00h-filled) (some cards have [08h..09h]=FFFFh)
  7Fh     Checksum (all above bytes XORed with each other)
```
If Block0/Frame(16+N) indicates that a given sector is broken, then the data
for that sector is stored in Block0/Frame(36+N).<br/>

#### Broken Sector Replacement Data (Block 0, Frame 36..55)
```
  00h-7Fh Data (usually FFh-filled, if there's no broken sector)
```

#### Unused Frames (Block 0, Frame 56..62)
```
  00h-7Fh Unused (usually FFh-filled)
```

#### Write Test Frame (Block 0, Frame 63)
Reportedly "write test". Usually same as Block 0 ("MC", 253 zero-bytes, plus
checksum 0Eh).<br/>

#### Title Frame (Block 1..15, Frame 0) (in first block of file only)
```
  00h-01h  ID (ASCII "SC")
  02h      Icon Display Flag
             11h...Icon has 1 frame  (static) (same image shown forever)
             12h...Icon has 2 frames (animated) (changes every 16 PAL frames)
             13h...Icon has 3 frames (animated) (changes every 11 PAL frames)
            Values other than 11h..13h seem to be treated as corrupted file
            (causing the file not to be listed in the bootmenu)
  03h      Block Number (1-15)  "icon block count"  Uh?
                   (usually 01h or 02h... might be block number within
                   files that occupy 2 or more blocks)
                   (actually, that kind of files seem to HAVE title frames
                   in ALL of their blocks; not only in their FIRST block)
                   (at least SOME seem to have such duplicated title frame,
                   but not all?)
  04h-43h  Title in Shift-JIS format (64 bytes = max 32 characters)
  44h-4Fh  Reserved (00h)
  50h-5Fh  Reserved (00h)  ;<-- this region is used for the Pocketstation
  60h-7Fh  Icon 16 Color Palette Data (each entry is 16bit CLUT)
```
For more info on entries [50h..5Fh], see<br/>
[Pocketstation File Header/Icons](pocketstation.md#pocketstation-file-headericons)<br/>

#### Icon Frame(s) (Block 1..15, Frame 1..3) (in first block of file only)
```
  00h-7Fh  Icon Bitmap (16x16 pixels, 4bit color depth)
```
Note: The icons are shown in the BIOS bootmenu (which appears when starting the
PlayStation without a CDROM inserted). The icons are drawn via GP0(2Ch)
command, ie. as Textured four-point polygon, opaque, with texture-blending,
whereas the 24bit blending color is 808080h (so it's quite the same as raw
texture without blending). As semi-transparency is disabled, Palette/CLUT
values can be 0000h=FullyTransparent, or 8000h=SolidBlack (the icons are
usually shown on a black background, so it doesn't make much of a difference).<br/>

#### Data Frame(s) (Block 1..15, Frame N..63; N=excluding any Title/Icon Frames)
```
  00h-7Fh  Data
```
Note: Files that occupy more than one block are having only ONE Title area, and
only one Icon area (in the first sector(s) of their first block), the
additional blocks are using sectors 0..63 for plain data.<br/>

#### Shift-JIS Character Set (16bit) (used in Title Frames)
Can contain japanese or english text, english characters are encoded like so:<br/>
```
  81h,40h      --> SPC
  81h,43h..97h --> punctuation marks
  82h,4Fh..58h --> "0..9"
  82h,60h..79h --> "A..Z"
  82h,81h..9Ah --> "a..z"
```
Titles shorter than 32 characters are padded with 00h-bytes.<br/>
Note: The titles are \<usually\> in 16bit format (even if they consist of
raw english text), however, the BIOS memory card manager does also accept 8bit
characters 20h..7Fh (so, in the 8bit form, the title could be theoretically up
to 64 characters long, but, nethertheless, the BIOS displays only max 32
chars).<br/>
For displaying Titles, the BIOS includes a complete Shift-JIS character set,<br/>
[BIOS Character Sets](kernelbios.md#bios-character-sets)<br/>
Shift-JIS is focused on asian languages, and does NOT include european letters
(eg. such with accent marks). Although the non-japanese PSX BIOSes DO include a
european character set, the BIOS memory card manager DOESN'T seem to translate
any title character codes to that character set region.<br/>



##   Memory Card Images
There are a lot of different ways to get a save from a memory card onto your
PC's hard disk, and these ways sometimes involve sticking some additional
information into a header at the beginning of the file.<br/>

#### Raw Memory Card Images (without header) (ie. usually 128K in size)
```
  SmartLink .PSM,
  WinPSM .PS,
  DataDeck .DDF,
  FPSX .MCR,
  ePSXe .MCD...
```
don't stick any header on the data at all, so you can just read it in and treat
it like a raw memory card.<br/>

All of these headers contain a signature at the top of the file. The three most
common formats and their signatures are:<br/>

```
     Connectix Virtual Game Station format (.MEM): "VgsM", 64 bytes
     PlayStation Magazine format (.PSX): "PSV", 256 bytes
```

some programs will OMIT any blank or unallocated blocks from the end of the
memory card -- if only three save blocks on the card are in use, for example,
saving the other twelve is pointless.<br/>

#### Xploder and Action Replay Files (54 byte header)
```
  00h..14h Filename in ASCII, terminated by 00h (max 20 chars, plus ending 00h)
  15h..35h Title in ASCII, terminated by 00h (max 32 chars, plus ending 00h)
  36h..    File Block(s) (starting with the Title sector)
```
This format contains only a single file (not a whole memory card). The filename
should be the same as used in the Memory Card Directory. The title is more or
less don't care; it may be the SHIFT-JIS title from the Title Sector converted
to ASCII.<br/>

#### Other
"There exists another single-save format with a 128 byte header containing a
raw index frame for the initial block, which must be updated to match the
destination card, and the raw save data. I have seen this format once, but I
don't remember what it was called or where it came from. You may want to
account for this possibility in your format detection logic."<br/>

#### .GME Files (usually 20F40h bytes)
InterAct GME format, produced by the DexDrive.<br/>
```
  000h 12   ASCII String "123-456-STD",00h
  00Ch 4    Usually zerofilled (or meaningless garbage in some files)
  010h 5    Always 00h,00h,01h,00h,01h
  015h 16   Copy of Sector 0..15 byte[00h] ;"M", followed by allocation states
  025h 16   Copy of Sector 0..15 byte[08h] ;00h, followed by next block values
  035h 11   Usually zerofilled (or meaningless garbage in some files)
  040h F00h Fifteen Description Strings (each one 100h bytes, padded with 00h)
  F40h 128K Memory Card Image (128K) (unused sectors 00h or FFh filled)
```
This is a very strange file format, no idea where it comes from. It contains a
F40h bytes header (mainly zerofilled), followed by the whole 128K of FLASH
memory (mainly zerofilled, too, since it usually contains only a small single
executable file).<br/>



##   Memory Card Notes
#### Sony PSX Memory Cards
Sony has manufactured only 128KByte memory cards for PSX, no bigger/smaller
ones.<br/>

#### Sony PS2 Memory Cards
A special case would be PS2 cards, these are bigger, but PS2 cards won't fit
into PSX cards slots (unless when cutting an extra notch in the card edge
connector), a PSX game played on a PS2 console could theoretically access PS2
cards (if it supports the different directory structure on that cards).<br/>

#### Third Party Cards with bigger capacity
Some third party cards contain larger memory chips, however, the PSX
games/kernel are supporting only regular 128Kbyte cards, so the extra memory
can be used only by dividing it into several 128Kbyte memory card images.<br/>
Selecting a different memory card image can be done by a switch or button on
the card, or via joypad key combinations (joypad/card are sharing the same
signals, so the card could watch the traffic on joypad bus, provided that the
MIPS CPU is actually reading the joypad).<br/>

#### Third Party Cards with bigger capacity and Data Compression
Some cards are additionally using data compression to increase the card
capacity, but that techinque is having rather bad reputation and could result
in data loss. For example, if a game has allocated four blocks on the memory
card, then it'll expect to be able to overwrite that four blocks at any time
(without needing to handle "memory card full" errors), however, if the card is
full, and if the newly written data has worse compression ratio, then the card
will be unable to store the new game position (and may have already overwritten
parts of the old game position). As a workaround, such cards may use a LED to
warn users when running low on memory (ideally, there should be always at least
128Kbytes of free memory).<br/>

#### Joytech Smart Card Adaptor
The smart card adaptor plugs into memory card slot, and allows to use special
credit card-shaped memory cards. There don't seem to be any special features,
ie. the hardware setup does just behave like normal PSX memory cards.<br/>

#### Datel VMEM (virtual memory card storage on expansion port)
The Datel/Interact VMEM exists as standalone VMEM cartridge, and some Datel
Cheat Devices do also include the VMEM feature. Either way, the VMEM connects
to expansion port, and contain some large FLASH memory, for storing multiple
memory cards on it. Unknown, how that memory is accessed (maybe it must be
copied to a regular memory card, or maybe they've somehow hooked the Kernel (or
even the hardware signals?) so that games could directly access the VMEM?<br/>

#### Passwords (instead of Memory Cards)
Some older games are using passwords instead of memory cards to allow the user
to continue at certain game positions. That's nice for people without memory
card, but unfortunately many of that games are restricted to it - it'd be more
user friendly to support both passwords, and, optionally, memory cards.<br/>

#### Yaroze Access Cards (DTL-H3020)
The Yaroze Access Card connects to memory card slot, the card resembles regular
memory cards, but it doesn't contain any storage memory. Instead, it does
merely support a very basic Access Card detection command:<br/>
```
  Send Reply Comment
  21h  N/A?  Probably replies HighZ (ie. probably reads FFh)?
  53h  0xh?  Replies unknown 8bit value (upper 4bit are known to be zero)?
```
Ie. when receiving 21h as first byte, it replies by an ACK, and does then
output 0xh as response to the next byte.<br/>
Without the Access Card, the Yaroze Bootdisc will refuse to work (the disc
contains software for transferring data to/from PC, for developing homebrew
games).<br/>

#### Pocketstation (Memory Card with built-in LCD screen and buttons)
[Pocketstation](pocketstation.md)<br/>
