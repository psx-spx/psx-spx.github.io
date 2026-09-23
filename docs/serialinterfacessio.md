#   Serial Interfaces (SIO)
The console has two serial interfaces:

- SIO0, mapped at `0x1f801040`, connected to the controller and memory card
  ports and hardwired to run in synchronous master mode (similar to SPI);
- SIO1, mapped at `0x1f801050`, connected to the serial port and hardwired to
  run in asynchronous (UART) mode.

The two units are very similar, although not identical, and seem to be vaguely
based on the Intel 8251A USART. Official register and bit names for SIO1 (but
not SIO0) can be found in Sony's `libsio.h` header.

####  `0x1f801040 + 0x10*N`: `DR` (data register)
When read:
```
  0-7   Received Data      (1st RX FIFO entry) (oldest entry)
  8-15  Preview            (2nd RX FIFO entry)
  16-23 Preview            (3rd RX FIFO entry)
  24-31 Preview            (4th RX FIFO entry) (5th..8th cannot be previewed)
```
A data byte can be read when SR.1=1. Some emulators behave incorrectly when this
register is read using a 16/32-bit memory access, so it should only be accessed
as an 8-bit register.

When written:
```
  0-7   Data to be sent
  8-31  Not used
```
Writing to this register starts a transfer (if, or as soon as, TXEN=1 and CTS=on
and SR.2=Ready). Writing to this register while SR.0=Busy causes the old value
to be overwritten.

The "TXEN=1" condition is a bit more complex: Writing to DR latches the current
TXEN value, and the transfer DOES start if the current TXEN value OR the latched
TXEN value is set (ie. if TXEN gets cleared after writing to DR, then the
transfer may STILL start if the old latched TXEN value was set; this appears for
SIO transfers in Wipeout 2097).

#### `0x1f801044 + 0x10*N`: `SR` (status register, read-only)
```
  0     TXRDY   TX FIFO Not Full         (1=Ready for new byte)  (depends on CTS) (TX requires CTS)
  1     RXRDY   RX FIFO Not Empty        (0=Empty, 1=Data available)
  2     TXU     TX Idle                  (1=Idle/Finished)       (depends on TXEN and on CTS)
  3     PERROR  RX Parity Error          (0=No, 1=Error; Wrong Parity, when enabled) (sticky)
  4     OE      (SIO1) RX FIFO Overrun   (0=No, 1=Error; received more than 8 bytes) (sticky)
  5     FE      (SIO1) RX Framing Error  (0=No, 1=Error; Bad Stop Bit) (when RXEN)   (sticky)
  6     BRK?    (SIO1) RX Input Level    (0=Normal, 1=Inverted) ;only AFTER receiving Stop Bit
  7     DSR     DSR Input Level          (0=Off, 1=On) (remote DTR) ;DSR not required to be on
  8     CTS     (SIO1) CTS Input Level   (0=Off, 1=On) (remote RTS) ;CTS required for TX
  9     IRQ     Interrupt Request        (0=None, 1=IRQ) (See CR.Bit4,10-12)   (sticky)
  10            Not used                 (always zero)
  11-31 ?       Baudrate Timer           (15-21 bit timer, decrementing at 33MHz)
```
Bit 0 gets set after sending the start bit, bit 2 is set after sending all bits
including the stop bit if any.

On SIO0, DSR is wired to the /ACK pin on the controller and memory card ports;
bit 7 is thus set when /ACK is low (asserted) and cleared when it is high. Bits
4-6 and 8 are always zero.

The number of bits actually used by the baud rate timer is probably affected by
the reload factor set in MR.

#### `0x1f801048 + 0x10*N`: `MR` (mode register)
```
  0-1  BR     Baudrate Reload Factor  (1=MUL1, 2=MUL16, 3=MUL64) (or 0=MUL1 on SIO0, STOP on SIO1)
  2-3  CHLEN  Character Length        (0=5 bits, 1=6 bits, 2=7 bits, 3=8 bits)
  4    PEN    Parity Enable           (0=No, 1=Enable)
  5    P      Parity Type             (0=Odd, 1=Even)
  6-7  SB     (SIO1) stop bit length  (0=Reserved/1bit, 1=1bit, 2=1.5bits, 3=2bits)
  8    CPOL?  (SIO0) clock polarity   (0=High when idle, 1=Low when idle)
  9-15        Not used                (always zero)
```
Bits 6-7 on SIO0 and bit 8 on SIO1 are always zero. On SIO0 the character length
shall be set to 8, the clock polarity should be set to high-when-idle and parity
should be disabled, as all controllers and memory cards expect these settings.

#### `0x1f80104a + 0x10*N`: `CR` (control register)
```
  0     TXEN    TX Enable                (0=Disable, 1=Enable)
  1     DTR     DTR Output Level         (0=Off, 1=On)
  2     RXEN    RX Enable                (SIO1: 0=Disable, 1=Enable)  ;Disable also clears RXFIFO
                                         (SIO0: 0=only receive when /CS low, 1=force receiving single byte)
  3     BRK     (SIO1) TX Output Level   (0=Normal, 1=Inverted, during Inactivity & Stop bits)
  4     ERRRST  Acknowledge              (0=No change, 1=Reset SR.Bits 3,4,5,9)      (W)
  5     RTS     (SIO1) RTS Output Level  (0=Off, 1=On)
  6     INTRST  Reset                    (0=No change, 1=Reset most registers to zero) (W)
  7     ?       (SIO1) unknown?          (read/write-able when FACTOR non-zero) (otherwise always zero)
  8-9   BUFSZ   RX Interrupt Mode        (0..3 = IRQ when RX FIFO contains 1,2,4,8 bytes)
  10    TXIEN   TX Interrupt Enable      (0=Disable, 1=Enable) ;when SR.0-or-2 ;Ready
  11    RXIEN   RX Interrupt Enable      (0=Disable, 1=Enable) ;when N bytes in RX FIFO
  12    DSRIEN  DSR Interrupt Enable     (0=Disable, 1=Enable) ;when SR.7  ;DSR high or /ACK low
  13    PORT?   (SIO0) Port Select       (0=port 1, 1=port 2) (/CS pulled low when bit 1 set)
  14-15         Not used                 (always zero)
```
On SIO0, DTR is wired to the /CS pin on the controller and memory card ports;
bit 1 will pull (assert) /CS low when set. Bit 13 is used to select which port's
/CS shall be asserted (all other signals are wired in parallel).

Bit 2 behaves differently on SIO0: when not set, incoming data will be ignored
unless bit 1 is also set. When set, data will be received regardless of whether
/CS is asserted, however bit 2 will be automatically cleared after a byte is
received.

Note that some emulators do not implement all SIO0 interrupts, as the kernel's
controller driver only ever uses the DSR (/ACK) interrupt.

#### `0x1f80105c`: SIO1 unknown
This is an internal register, which usually shouldn't be accessed by software.
Messing with it has rather strange effects: After writing a value "X" to this
register, reading returns "X ROR 8" eventually "ANDed with 1F1Fh and ORed with
C0C0h or 8080h" (depending on the character length in MR). SIO0 does not have
this register.

#### `0x1f80104e + 0x10*N`: `BR` (baud rate register)
```
  0-15  Baudrate Reload value for decrementing Baudrate Timer
```
The timer is decremented on every clock cycle and reloaded when writing to this
register and when it reaches zero. Upon reload, the 16-bit Reload value is
multiplied by the Baudrate Factor (see MR.Bit0-1), divided by 2, and then copied
to the 21-bit Baudrate Timer (MR.Bit11-31). The resulting transfer rate can be
calculated as follows:
```
  SIO0: BitsPerSecond = 33868800 / MAX(((Reload*Factor) AND NOT 1),1)
  SIO1: BitsPerSecond = 33868800 / MAX(((Reload*Factor) AND NOT 1),Factor)
```
According to the original nocash page, the way this register works is actually
slightly different for SIO0 vs. SIO1:
```
  SIO0_BAUD is multiplied by Factor, and does then elapse "2" times per bit.
  SIO1_BAUD is NOT multiplied, and, instead, elapses "2*Factor" times per bit.
```
The standard baud rate for SIO0 devices, including both controllers and memory
cards, is ~250 kHz, with BR being set to 0088h (serial clock high for 44h cycles
then low for 44h cycles).

#### DR Write Notes
The hardware can hold (almost) 2 bytes in the TX direction (one being currently
transferred, and, once when the start bit was sent, another byte can be stored
in DR). When writing to DR, both SR.0 and SR.2 become zero. As soon as the
transfer starts, SR.0 becomes set (indicating that one can write a new byte to
DR; although the transmission is still busy). As soon as the transfer of the
most recently written byte ends, SR.2 becomes set.

#### DR Read Notes
The hardware can hold 8 bytes in the RX direction (when receiving further
byte(s) while the RX FIFO is full, then the last FIFO entry will by overwritten
by the new byte, and SR.4 gets set; the hardware does NOT automatically disable
RTS when the FIFO becomes full). The RX FIFO overrun flag is not accessible on
SIO0.

Data can be read from DR when SR.1 is set, that flag gets automatically cleared
after reading from DR (unless there are still further bytes in the RX FIFO).
Note: The hardware does always store incoming data in RX FIFO (even when Parity
or Stop bits are invalid).

Note: A 16bit read allows to read two FIFO entries at once; nethertheless, it
removes only ONE entry from the FIFO. On the contrary, a 32bit read DOES remove
FOUR entries (although, there's nothing that'd indicate if the FIFO did
actually contain four entries).

Reading from Empty RX FIFO returns either the most recently received byte or
zero (the hardware stores incoming data in ALL unused FIFO entries; eg. if five
entries are used, then the data gets stored thrice, after reading 6 bytes, the
FIFO empty flag gets set, but nethertheless, the last byte can be read two more
times, but doing further reads returns 00h).

#### Interrupt Acknowledge Notes
First reset I\_STAT.8, then set CR.4 (when doing it vice-versa, the hardware may
miss a new IRQ which may occur immediately after setting CR.4) (and I\_STAT.8 is
edge triggered, so that bit can be reset even while SR.9 is still set).

When acknowledging via CR.4 with the enabled condition(s) in CR.10-12 still
being true (eg. the RX FIFO is still not empty): the IRQ does trigger again
(almost) immediately (it goes off only for a very short moment; barely enough to
allow I\_STAT.8 to sense a edge).

#### Note
For more details on how SIO0 is used to communicate with controllers and memory
cards, see:

[Controller and Memory Card Overview](controllersandmemorycards.md#controller-and-memory-card-overview)<br/>

For serial port pinouts, PSone SIO1 upgrading, and for building RS232 adaptors,
see:

[Pinouts - SIO Pinouts](pinouts.md#pinouts-sio-pinouts)

Aside from the internal SIO port, the PSX BIOS supports two additional external
serial ports, connected to the expansion port.

[DEV8 Dual Serial Port (for TTY Debug Terminal)](expansionportpio.md#dev8-dual-serial-port-for-tty-debug-terminal)

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
Hz).

Ridge Racer Revolution is also said to support 2P link.

Keitai Eddy seems to allow to connect a mobile phone to the SIO port (the games
CD cover suggests so; this seems to be something different than the "normal"
I-Mode adaptor, which would connect to controller port, not to SIO port).
