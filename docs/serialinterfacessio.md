#   Serial Interfaces (SIO)
The console has two serial interfaces, SIO0 (connected to the controller and
memory card ports) and SIO1 (connected to the serial port). SIO0 is hardwired to
run in synchronous mode, while SIO1 can only operate in asynchronous mode. Both
units are fairly similar, although not identical, and seem to be vaguely based
on the Intel 8251A USART chip.<br/>

#### 1F801040h+N\*10h - SIO#\_TX\_DATA (W)
```
  0-7   Data to be sent
  8-31  Not used
```
Writing to this register starts a transfer (if, or as soon as, TXEN=1 and CTS=on
and SIO\_STAT.2=Ready). Writing to this register while SIO\_STAT.0=Busy causes
the old value to be overwritten.<br/>
The "TXEN=1" condition is a bit more complex: Writing to SIO\_TX\_DATA latches
the current TXEN value, and the transfer DOES start if the current TXEN value
OR the latched TXEN value is set (ie. if TXEN gets cleared after writing to
SIO\_TX\_DATA, then the transfer may STILL start if the old latched TXEN value
was set; this appears for SIO transfers in Wipeout 2097).<br/>

#### 1F801040h+N\*10h - SIO#\_RX\_DATA (R)
```
  0-7   Received Data      (1st RX FIFO entry) (oldest entry)
  8-15  Preview            (2nd RX FIFO entry)
  16-23 Preview            (3rd RX FIFO entry)
  24-31 Preview            (4th RX FIFO entry) (5th..8th cannot be previewed)
```
A data byte can be read when SIO\_STAT.1=1. Some emulators behave incorrectly
when this register is read using a 16/32-bit memory access, so it should only
be accessed as an 8-bit register.<br/>

#### 1F801044h+N\*10h - SIO#\_STAT (R)
```
  0     TX FIFO Not Full       (1=Ready for new byte)  (depends on CTS) (TX requires CTS)
  1     RX FIFO Not Empty      (0=Empty, 1=Data available)
  2     TX Idle                (1=Idle/Finished)       (depends on TXEN and on CTS)
  3     RX Parity Error        (0=No, 1=Error; Wrong Parity, when enabled) (sticky)
  4     SIO1 RX FIFO Overrun   (0=No, 1=Error; received more than 8 bytes) (sticky)
  5     SIO1 RX Bad Stop Bit   (0=No, 1=Error; Bad Stop Bit) (when RXEN)   (sticky)
  6     SIO1 RX Input Level    (0=Normal, 1=Inverted) ;only AFTER receiving Stop Bit
  7     DSR Input Level        (0=Off, 1=On) (remote DTR) ;DSR not required to be on
  8     SIO1 CTS Input Level   (0=Off, 1=On) (remote RTS) ;CTS required for TX
  9     Interrupt Request      (0=None, 1=IRQ) (See SIO_CTRL.Bit4,10-12)   (sticky)
  10    Unknown                (always zero)
  11-31 Baudrate Timer         (15-21 bit timer, decrementing at 33MHz)
```
Bit 0 gets set after sending the start bit, bit 2 is set after sending all bits
including the stop bit if any.<br/>
On SIO0, DSR is wired to the /ACK pin on the controller and memory card ports;
bit 7 is thus set when /ACK is low (asserted) and cleared when it is high. Bits
4-6 and 8 are always zero.<br/>
The number of bits actually used by the baud rate timer is probably affected by
the reload factor set in SIO\_MODE.<br/>

#### 1F801048h+N\*10h - SIO#\_MODE (R/W) (eg. 004Eh --\> 8N1 with Factor=MUL16)
```
  0-1   Baudrate Reload Factor     (1=MUL1, 2=MUL16, 3=MUL64) (or 0=MUL1 on SIO0, STOP on SIO1)
  2-3   Character Length           (0=5 bits, 1=6 bits, 2=7 bits, 3=8 bits)
  4     Parity Enable              (0=No, 1=Enable)
  5     Parity Type                (0=Even, 1=Odd) (seems to be vice-versa...?)
  6-7   SIO1 stop bit length       (0=Reserved/1bit, 1=1bit, 2=1.5bits, 3=2bits)
  8     SIO0 clock polarity (CPOL) (0=High when idle, 1=Low when idle)
  9-15  Not used (always zero)
```
Bits 6-7 on SIO0 and bit 8 on SIO1 are always zero. On SIO0 the character length
shall be set to 8, the clock polarity should be set to high-when-idle and parity
should be disabled, as all controllers and memory cards expect these settings.</br>

#### 1F80104Ah+N\*10h - SIO#\_CTRL (R/W)
```
  0     TX Enable (TXEN)      (0=Disable, 1=Enable)
  1     DTR Output Level      (0=Off, 1=On)
  2     RX Enable (RXEN)      (SIO1: 0=Disable, 1=Enable)  ;Disable also clears RXFIFO
                              (SIO0: 0=only receive when /CS low, 1=force receiving single byte)
  3     SIO1 TX Output Level  (0=Normal, 1=Inverted, during Inactivity & Stop bits)
  4     Acknowledge           (0=No change, 1=Reset SIO_STAT.Bits 3,4,5,9)      (W)
  5     SIO1 RTS Output Level (0=Off, 1=On)
  6     Reset                 (0=No change, 1=Reset most registers to zero) (W)
  7     SIO1 unknown?         (read/write-able when FACTOR non-zero) (otherwise always zero)
  8-9   RX Interrupt Mode     (0..3 = IRQ when RX FIFO contains 1,2,4,8 bytes)
  10    TX Interrupt Enable   (0=Disable, 1=Enable) ;when SIO_STAT.0-or-2 ;Ready
  11    RX Interrupt Enable   (0=Disable, 1=Enable) ;when N bytes in RX FIFO
  12    DSR Interrupt Enable  (0=Disable, 1=Enable) ;when SIO_STAT.7  ;DSR high or /ACK low
  13    SIO0 port select      (0=port 1, 1=port 2) (/CS pulled low when bit 1 set)
  14-15 Not used              (always zero)
```
On SIO0, DTR is wired to the /CS pin on the controller and memory card ports;
bit 1 will pull (assert) /CS low when set. Bit 13 is used to select which port's
/CS shall be asserted (all other signals are wired in parallel).<br/>
Bit 2 behaves differently on SIO0: when not set, incoming data will be ignored
unless bit 1 is also set. When set, data will be received regardless of whether
/CS is asserted, however bit 2 will be automatically cleared after a byte is
received.<br/>
Note that some emulators do not implement all SIO0 interrupts, as the kernel's
controller driver only ever uses the DSR (/ACK) interrupt.<br/>

#### 1F80105Ch - SIO1\_MISC (R/W)
This is an internal register, which usually shouldn't be accessed by software.
Messing with it has rather strange effects: After writing a value "X" to this
register, reading returns "X ROR 8" eventually "ANDed with 1F1Fh and ORed with
C0C0h or 8080h" (depending on the character length in SIO\_MODE). SIO0 does not
have this register.<br/>

#### 1F80104Eh+N\*10h - SIO#\_BAUD (R/W) (eg. 00DCh --\> 9600 bps; when Factor=MUL16)
```
  0-15  Baudrate Reload value for decrementing Baudrate Timer
```
The timer is decremented on every clock cycle and reloaded when writing to this
register and when it reaches zero. Upon reload, the 16-bit Reload value is
multiplied by the Baudrate Factor (see SIO\_MODE.Bit0-1), divided by 2, and then
copied to the 21-bit Baudrate Timer (SIO\_MODE.Bit11-31). The resulting transfer
rate can be calculated as follows:<br/>
```
  SIO0: BitsPerSecond = 33868800 / MIN(((Reload*Factor) AND NOT 1),1)
  SIO1: BitsPerSecond = 33868800 / MIN(((Reload*Factor) AND NOT 1),Factor)
```
According to the original nocash page, the way this register works is actually
slightly different for SIO0 vs. SIO1:<br/>
```
  SIO0_BAUD is multiplied by Factor, and does then elapse "2" times per bit.
  SIO1_BAUD is NOT multiplied, and, instead, elapses "2*Factor" times per bit.
```
The standard baud rate for SIO0 devices, including both controllers and memory
cards, is ~250 kHz, with SIO0\_BAUD being set to 0088h (serial clock high for
44h cycles then low for 44h cycles).<br/>

#### SIO\_TX\_DATA Notes
The hardware can hold (almost) 2 bytes in the TX direction (one being currently
transferred, and, once when the start bit was sent, another byte can be stored
in SIO\_TX\_DATA). When writing to SIO\_TX\_DATA, both SIO\_STAT.0 and SIO\_STAT.2
become zero. As soon as the transfer starts, SIO\_STAT.0 becomes set (indicating
that one can write a new byte to SIO\_TX\_DATA; although the transmission is
still busy). As soon as the transfer of the most recently written byte ends,
SIO\_STAT.2 becomes set.<br/>

#### SIO\_RX\_DATA Notes
The hardware can hold 8 bytes in the RX direction (when receiving further
byte(s) while the RX FIFO is full, then the last FIFO entry will by overwritten
by the new byte, and SIO\_STAT.4 gets set; the hardware does NOT automatically
disable RTS when the FIFO becomes full). The RX FIFO overrun flag is not
accessible on SIO0.<br/>
Data can be read from SIO\_RX\_DATA when SIO\_STAT.1 is set, that flag gets
automatically cleared after reading from SIO\_RX\_DATA (unless there are still
further bytes in the RX FIFO). Note: The hardware does always store incoming
data in RX FIFO (even when Parity or Stop bits are invalid).<br/>
Note: A 16bit read allows to read two FIFO entries at once; nethertheless, it
removes only ONE entry from the FIFO. On the contrary, a 32bit read DOES remove
FOUR entries (although, there's nothing that'd indicate if the FIFO did
actually contain four entries).<br/>
Reading from Empty RX FIFO returns either the most recently received byte or
zero (the hardware stores incoming data in ALL unused FIFO entries; eg. if five
entries are used, then the data gets stored thrice, after reading 6 bytes, the
FIFO empty flag gets set, but nethertheless, the last byte can be read two more
times, but doing further reads returns 00h).<br/>

#### Interrupt Acknowledge Notes
First reset I\_STAT.8, then set SIO.CTRL.4 (when doing it vice-versa, the
hardware may miss a new IRQ which may occur immediately after setting
SIO.CTRL.4) (and I\_STAT.8 is edge triggered, so that bit can be reset even
while SIO\_STAT.9 is still set).<br/>
When acknowledging via SIO\_CTRL.4 with the enabled condition(s) in
SIO\_CTRL.10-12 still being true (eg. the RX FIFO is still not empty): the IRQ
does trigger again (almost) immediately (it goes off only for a very short
moment; barely enough to allow I\_STAT.8 to sense a edge).<br/>

#### Note
For more details on how SIO0 is used to communicate with controllers and memory
cards, see:<br/>
[Controller and Memory Card Misc](controllersandmemorycards.md#controller-and-memory-card-misc)<br/>
For serial port pinouts, PSone SIO1 upgrading, and for building RS232 adaptors,
see:<br/>
[Pinouts - SIO Pinouts](pinouts.md#pinouts-sio-pinouts)<br/>
Aside from the internal SIO port, the PSX BIOS supports two additional external
serial ports, connected to the expansion port.<br/>
[EXP2 Dual Serial Port (for TTY Debug Terminal)](expansionportpio.md#exp2-dual-serial-port-for-tty-debug-terminal)<br/>

#### SIO1 link cable games
The serial ports on two consoles can be connected with an SCPH-1040 Link Cable
(known as Taisen Cable, or "Fight Cable" in Japan) for multiplayer functionality
on games that support this method. This was used by a small number of games in
the console's lifecycle, but inconveniently required a second console and copy
of the game.

Two-Console Link Cable Games (Incomplete List):
```
Andretti Racing
Armored Core (and Armored Core "Link Versus Demo" disc)
Armored Core Project Phantasma
Armored Core Master of Arena
Assault Rigs
Ayrton Senna Kart Duel
Blast Radius
Bogey Dead 6
Burning Road
Bushido Blade
Bushido Blade 2
C1 -Circuit-
CART World Series
Command & Conquer Red Alert
Command & Conquer Red Alert Retaliation
Cool Boarders 2
Dead in the Water
Descent
Descent Maximum
Destruction Derby
Duke Nukem Total Meltdown
Dodgem Arena
Doom
Dune 2000
Explosive Racing (X Racing in NTSC-J)
Final Doom
Formula 1
Formula 1 98
Grand Tour Racing '98 (Gekisou!! Grand Racing -Total Driving'- in NTSC-J, Total Drivin in PAL)
Independence Day
Krazy Ivan
Leading Jockey Highbred
Metal Jacket
Mobile Suit Z-Gundam
Monaco Grand Prix Racing Simulation 2 (Monaco Grand Prix in NTSC-U/C)
Motor Toon Grand Prix (reportedly NTSC-U/C version only)
Motor Toon Grand Prix 2
Motor Toon Grand Prix USA Edition
The Need for Speed (Over Drivin' DX in NTSC-J)
PrePre Vol. 2
Pro Pinball Big Race USA
RacinGroovy
Real Robots Final Attack
Red Asphalt (Rock & Roll Racing 2 Red Asphalt in PAL)
Ridge Racer Revolution
R4 Ridge Racer Type 4
Robo Pit
Rogue Trip Vacation 2012
San Francisco Rush Extreme Racing (reportedly PAL version only)
Shutokou Battle R
Sidewinder
Sidewinder USA
Soukou Kihei Votoms Gaiden: Ao no Kishi Berserga Monogatari
Streak Hoverboard Racing
Test Drive 4
Test Drive Off-Road (reportedly NTSC-U/C only)
TOCA 2 Touring Car Challenge (TOCA 2 Touring Cars in PAL)
Trick'N Snowboarder (Tricky Sliders Freestyle Snowboard in NTSC-J)
Twisted Metal III
Wing Over
Wipeout
Wipeout 3 Special Edition
Wipeout XL (Wipeout 2097 in PAL)
Zero Pilot Ginyoku no Senshi
```

The serial port is used (for 2-player link) by Wipeout 2097 (that game
accidently assumes BAUDs based on 64\*1024\*1025 Hz rather than on 600h\*44100
Hz).<br/>
Ridge Racer Revolution is also said to support 2P link.<br/>
Keitai Eddy seems to allow to connect a mobile phone to the SIO port (the games
CD cover suggests so; this seems to be something different than the "normal"
I-Mode adaptor, which would connect to controller port, not to SIO port).<br/>
