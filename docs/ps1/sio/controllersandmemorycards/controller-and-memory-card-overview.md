#   Controller and Memory Card Overview
Controllers and memory cards connect to the console using a serial protocol and
are accessed through SIO0 registers:<br/>
[Serial Interfaces (SIO)](../serialinterfacessio.md)<br/>
The protocol used is similar to standard SPI, with no start/stop bytes and no
parity (even though SIO0 has support for it). Unlike typical SPI, only one byte
is transferred at a time and a separate wire (/ACK) is used by the device to
signal the PS1 that it is ready to exchange the next byte. For more details see:<br/>
[Controller and Memory Card Signals](controller-and-memory-card-signals.md#controller-and-memory-card-signals)<br/>

#### Device addressing
Each controller port and its respective memory card slot are wired in parallel,
and the /CSn signals select both the controller and the memory card when
asserted. This selection is narrowed down through a simple addressing scheme,
where the first byte sent by the console after asserting /CSn is the address of
the device that shall reply. All devices must keep the DAT line idle before
receiving this byte. Once the address is sent, the device that was addressed
shall pull /ACK low to signal its presence and start exchanging bytes.<br/>
The following addresses are known to be used:<br/>

| Device                               | Address |
| :----------------------------------- | ------: |
| Standard controller                  |   `01h` |
| Yaroze Access Card                   |   `21h` |
| PS2 multitap (incompatible with PS1) |   `21h` |
| PS2 DVD remote receiver              |   `61h` |
| Memory card                          |   `81h` |

#### DSR (/ACK) Controller and Memory Card - Byte Received Interrupt
Gets set after receiving a data byte - that only if an /ACK has been received
from the peripheral (ie. there will be no IRQ if the peripheral fails to send
an /ACK, or if there's no peripheral connected at all).<br/>
```
  Actually, DSR means "more-data-request",
  accordingly, it does NOT get triggered after receiving the LAST byte.
```
I\_STAT.7 is edge triggered (that means it can be acknowledge before or after
acknowledging SIO0\_STAT.9). However, SIO0\_STAT.9 is NOT edge triggered (that
means it CANNOT be acknowledged while the external /IRQ input is still low; ie.
one must first wait until SIO0\_STAT.7=0, and then set SIO0\_CTRL.4=1) (this is
apparently a hardware glitch; note: the LOW duration is circa 100 clock
cycles).<br/>

#### /IRQ10 (/IRQ) Controller - Lightpen Interrupt
Pin 8 on Controller Port. Routed directly to the Interrupt Controller (at
1F80107xh). There are no status/enable bits in the SIO0\_registers (at
1F80104xh).<br/>

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

#### BIOS Functions
Controllers can be probably accessed via InitPad and StartPad functions,<br/>
[BIOS Joypad Functions](../../kernelbios/joypad-functions.md#bios-joypad-functions)<br/>
Memory cards can be accessed by the filesystem (with device names "bu00:"
(slot1) and "bu10:" (slot2) or so). Before using that device names, it seems to
be required to call InitCard, StartCard, and \_bu\_init (?).<br/>

#### Synchronous I/O
The data is transferred in units of bytes, via separate input and output lines.
So, when sending byte, the hardware does simultaneously receive a response
byte.<br/>
One exception is the address byte (which selects either the controller,
or the memory card) until that byte has been sent, neither the controller nor
memory card are selected (and so the first "response" byte should be ignored;
probably containing more or less stable high-z levels).<br/>
The other exception is, when you have send all command bytes, and still want to
receive further data, then you'll need to send dummy command bytes (should be
usually 00h) to receive the response bytes.<br/>
