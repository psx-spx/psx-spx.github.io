#   Serial Port (SIO)
#### 1F801050h SIO\_TX\_DATA (W)
```
  0-7   Data to be sent
  8-31  Not used
```
Writing to this register starts transmit (if, or as soon as, TXEN=1 and CTS=on
and SIO\_STAT.2=Ready). Writing to this register while SIO\_STAT.0=Busy causes
the old value to be overwritten.<br/>
The "TXEN=1" condition is a bit more complex: Writing to SIO\_TX\_DATA latches
the current TXEN value, and the transfer DOES start if the current TXEN value
OR the latched TXEN value is set (ie. if TXEN gets cleared after writing to
SIO\_TX\_DATA, then the transfer may STILL start if the old latched TXEN value
was set; this appears for SIO transfers in Wipeout 2097).<br/>

#### 1F801050h SIO\_RX\_DATA (R)
```
  0-7   Received Data      (1st RX FIFO entry) (oldest entry)
  8-15  Preview            (2nd RX FIFO entry)
  16-23 Preview            (3rd RX FIFO entry)
  24-31 Preview            (4th RX FIFO entry) (5th..8th cannot be previewed)
```
A data byte can be read when SIO\_STAT.1=1. Data should be read only via 8bit
memory access (the 16bit/32bit "preview" feature is rather unusable).<br/>

#### 1F801054h SIO\_STAT (R)
```
  0     TX Ready Flag 1   (1=Ready/Started)  (depends on CTS) (TX requires CTS)
  1     RX FIFO Not Empty (0=Empty, 1=Not Empty)
  2     TX Ready Flag 2   (1=Ready/Finished) (depends on TXEN and on CTS)
  3     RX Parity Error   (0=No, 1=Error; Wrong Parity, when enabled) (sticky)
  4     RX FIFO Overrun   (0=No, 1=Error; Received more than 8 bytes) (sticky)
  5     RX Bad Stop Bit   (0=No, 1=Error; Bad Stop Bit) (when RXEN)   (sticky)
  6     RX Input Level    (0=Normal, 1=Inverted) ;only AFTER receiving Stop Bit
  7     DSR Input Level   (0=Off, 1=On) (remote DTR) ;DSR not required to be on
  8     CTS Input Level   (0=Off, 1=On) (remote RTS) ;CTS required for TX
  9     Interrupt Request (0=None, 1=IRQ)                             (sticky)
  10    Unknown           (always zero)
  11-25 Baudrate Timer    (15bit timer, decrementing at 33MHz)
  26-31 Unknown (usually zero, sometimes all bits set)
```
Note: Bit0 gets cleared after sending the Startbit, Bit2 gets cleared after
sending all bits up to including the Stopbit.<br/>

#### 1F801058h SIO\_MODE (R/W) (eg. 004Eh --\> 8N1 with Factor=MUL16)
```
  0-1   Baudrate Reload Factor (1=MUL1, 2=MUL16, 3=MUL64) (or 0=STOP)
  2-3   Character Length       (0=5bits, 1=6bits, 2=7bits, 3=8bits)
  4     Parity Enable          (0=No, 1=Enable)
  5     Parity Type            (0=Even, 1=Odd) (seems to be vice-versa...?)
  6-7   Stop bit length        (0=Reserved/1bit, 1=1bit, 2=1.5bits, 3=2bits)
  8-15  Not used (always zero)
```

#### 1F80105Ah SIO\_CTRL (R/W)
```
  0     TX Enable (TXEN)  (0=Disable, 1=Enable, when CTS=On)
  1     DTR Output Level  (0=Off, 1=On)
  2     RX Enable (RXEN)  (0=Disable, 1=Enable)  ;Disable also clears RXFIFO
  3     TX Output Level   (0=Normal, 1=Inverted, during Inactivity & Stop bits)
  4     Acknowledge       (0=No change, 1=Reset SIO_STAT.Bits 3,4,5,9)      (W)
  5     RTS Output Level  (0=Off, 1=On)
  6     Reset             (0=No change, 1=Reset most SIO_registers to zero) (W)
  7     Unknown? (read/write-able when FACTOR non-zero) (otherwise always zero)
  8-9   RX Interrupt Mode    (0..3 = IRQ when RX FIFO contains 1,2,4,8 bytes)
  10    TX Interrupt Enable  (0=Disable, 1=Enable) ;when SIO_STAT.0-or-2 ;Ready
  11    RX Interrupt Enable  (0=Disable, 1=Enable) ;when N bytes in RX FIFO
  12    DSR Interrupt Enable (0=Disable, 1=Enable) ;when SIO_STAT.7  ;DSR=On
  13-15 Not used (always zero)
```

#### 1F80105Ch SIO\_MISC (R/W)
This is an internal register, which usually shouldn't be accessed by software.
Messing with it has rather strange effects: After writing a value "X" to this
register, reading returns "X ROR 8" eventually "ANDed with 1F1Fh and ORed with
C0C0h or 8080h" (depending on the character length in SIO\_MODE).<br/>

#### 1F80105Eh SIO\_BAUD (R/W) (eg. 00DCh --\> 9600 bauds; when Factor=MUL16)
```
  0-15  Baudrate Reload value for decrementing Baudrate Timer
```
The Baudrate is calculated (based on SIO\_BAUD, and on Factor in SIO\_MODE):<br/>
```
  BitsPerSecond = (44100Hz*300h) / MIN(((Reload*Factor) AND NOT 1),Factor)
```

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
disable RTS when the FIFO becomes full).<br/>
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

#### SIO\_BAUD Notes
Timer reload occurs when writing to SIO\_BAUD, and, automatically when the
Baudrate Timer reaches zero. There should be two 16bit SIO timers (for TX and
RX), the upper 15bit of one of that timers can be read from SIO\_STAT (not sure
which one, and no idea if there's a way to read the other timer, too).<br/>
Or... maybe there is only ONE timer, and RX/TX are separated only by separate
"timer ellapsed" counters, in that case the MUL1 factor won't work properly,
but, with the MUL16 or MUL64 factors, RX could start anytime (eg. when TX has
already ellapsed a bunch of times)...?<br/>
The maximum baud rate may vary depending on the length and quality of the
cable, whether and how many inverters and anti-inverters are used (on the
mainboard and in external adaptor, and on whether signals are externally
converted to +/-12V levels)... anyways, rates up to 9600 baud should be working
in all cases.<br/>
However, running in no$psx, Wipeout 2097 seems to use about 2 million bauds...
although, in older no$psx versions, I believe I did see it using some kind of
baudrate detection, where it did try different rates in steps of 200 bauds or
so...?<br/>

#### SIO Ports vs JOY Ports
SIO uses I/O Addresses 1F801050h..1F80105Fh, which seem to be organized similar
to the Controller/Memory Card registers at 1F801040h..1F80104Fh, though not
identical, and with an additional register at 1F80105Ch, which has no
corresponding port at 1F80104Ch.<br/>
SIO\_BAUD is \<effectively\> same as for JOY\_BAUD, but, \<internally\>
they are a bit different:<br/>
```
  JOY_BAUD is multiplied by Factor, and does then ellapse "2" times per bit.
  SIO_BAUD is NOT multiplied, and, instead, ellapses "2*Factor" times per bit.
```
Unlike for the Controller/Memory Card ports, the data is transferred without
CLK signal, instead, it's using RS232 format, ie. the transfer starts with a
start bit, and is then transferred at a specific baudrate (which must be
configured identically at the receiver side). For RS232, data is usually 8bit,
and may optionally end with a parity bit, and one or two stop bits.<br/>

#### Note
For SIO Pinouts, PSone SIO upgrading, and for building RS232 adaptors, see:<br/>
[Pinouts - SIO Pinouts](pinouts.md#pinouts-sio-pinouts)<br/>
Aside from the internal SIO port, the PSX BIOS supports two additional external
serial ports, connected to the expansion port,<br/>
[EXP2 Dual Serial Port (for TTY Debug Terminal)](expansionportpio.md#exp2-dual-serial-port-for-tty-debug-terminal)<br/>

#### SIO Games
The serial port is used (for 2-player link) by Wipeout 2097 (that game
accidently assumes BAUDs based on 64\*1024\*1025 Hz rather than on 600h\*44100
Hz).<br/>
Ridge Racer Revolution is also said to support 2P link.<br/>
Keitai Eddy seems to allow to connect a mobile phone to the SIO port (the games
CD cover suggests so; this seems to be something different than the "normal"
I-Mode adaptor, which would connect to controller port, not to SIO port).<br/>

#### 8251A Note
The Playstation Serial Port is apparently based/inspired on the Intel 8251A
USART chip; which has very similar 8bit Mode/Command/Status registers.<br/>
