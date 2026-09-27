### Konami ASIC registers

Registers in the `0x1f400000-0x1f40000f` region are handled by the Konami 056879
I/O ASIC, consisting of a single 8-bit output port and at least six 16-bit input
ports. The same chip was used in other Konami arcade boards of the time.

#### `0x1f400000` (ASIC register 0): **ADC** / **Coin counters** / **Audio control**

| Bits | RW | Description                                   |
| ---: | :- | :-------------------------------------------- |
|    0 | W  | Data input to ADC (`DI`)                      |
|    1 | W  | Chip select to ADC (`/CS`)                    |
|    2 | W  | Data clock to ADC (`CLK`)                     |
|    3 | W  | Coin counter 1 (1 = energize counter coil)    |
|    4 | W  | Coin counter 2 (1 = energize counter coil)    |
|    5 | W  | Built-in audio amplifier enable (0 = muted)   |
|    6 | W  | External audio input enable (0 = muted)       |
|    7 | W  | SPU DAC output enable (0 = muted)             |
|    8 | W  | JVS MCU reset output (0 = pull reset low)     |
| 9-15 |    | _Unused_                                      |

The ADC chip is an ADC0834 from TI, which uses a proprietary SPI-like protocol.
Its four inputs are wired to the `ANALOG` connector on the 573 motherboard.
Refer to the ADC083x datasheet for details on how to bitbang the protocol.

Mechanical coin counters are incremented by games whenever a coin is inserted by
setting bit 3 or 4 for a fraction of a second and then clearing them. Bit 5
controls whether the onboard audio amp is enabled but does not affect the RCA
line level outputs, which are always enabled. Setting bit 5 has no effect
immediately as the amplifier takes about a second to turn on.

Bit 6 is used by games to mute audio from the CD-ROM drive or digital I/O board.
However, testing on real hardware seems to suggest it is actually some sort of
attenuation control, as the audio is still audible (albeit at a very low volume)
when the bit is cleared. Note that some games, such as GuitarFreaks, break the
CD/MP3 output to separate jacks on the front I/O panel rather than routing it
through the motherboard, making bit 6 meaningless.

Bit 8 resets the JVS MCU. Since the reset pin is active-low, resetting is done
by writing 0, waiting at least 10 H8 clock cycles (the BIOS waits 2 hblanks)
and writing 1 again. Resetting the MCU will clear `JVSDRDY` but not `JVSIRDY`.
As the 056879 ASIC's output register is only 8 bits wide, bit 8 is actually
handled by a discrete flip-flop on the motherboard.

Unknown what reading from this port does.

#### `0x1f400004` (ASIC register 2): **DIP switches** / **JVS status** / **Security cartridge**

| Bits  | RW | Description                             |
| ----: | :- | :-------------------------------------- |
|   0-3 | R  | DIP switch 1-4 status (0 = on, 1 = off) |
|   4-5 | R  | Current JVS MCU status code             |
|   6-7 | R  | Current JVS MCU error code              |
|  8-15 | R  | `I0-I7` from security cartridge         |

The MCU status code can be one of the following values:

| Code | Description                                                     |
| ---: | :-------------------------------------------------------------- |
|    0 | Waiting for the 573 to read or write the first word of a packet |
|    1 | Busy (sending a packet or waiting for a response)               |
|    2 | Waiting for the 573 to finish reading or writing a packet       |
|    3 | _Unused_                                                        |

The MCU error code can be one of the following values:

| Code | Description                                                      |
| ---: | :--------------------------------------------------------------- |
|    0 | _Unused_                                                         |
|    1 | Packet written by the 573 has an invalid checksum                |
|    2 | Packet written by the 573 does not start with a `0xe0` sync byte |
|    3 | No error                                                         |

Once an error is reported, the MCU will enter an endless loop and become
unresponsive. In order to clear the error the MCU must be reset using bit 8 in
register `0x1f400000`.

The highest 8 bits read from this register are the current state of the security
cartridge's `I0-I7` pins. See the security cartridge section for an explanation
of what each bit is wired to. Unknown whether reading from this register will
clear the `IRDY` flag, if previously set by the cartridge.

Bit 3 (DIP switch 4) is used by the BIOS to determine whether to boot from
flash. If set, the BIOS will attempt to search for a valid executable on the
internal flash and both PCMCIA cards prior to falling back to the CD-ROM.

#### `0x1f400006` (ASIC register 3): **Misc. inputs**

| Bits  | RW | Description                                   |
| ----: | :- | :-------------------------------------------- |
|     0 | R  | Data output from ADC (`DO`)                   |
|     1 | R  | SAR status from ADC (`SARS`)                  |
|     2 | R  | From `IO0` on security cartridge              |
|     3 | R  | Sense input from JVS port                     |
|     4 | R  | `JVSIRDY` status from JVS MCU                 |
|     5 | R  | `JVSDRDY` status from JVS MCU                 |
|     6 | R  | `IRDY` status from security cartridge         |
|     7 | R  | `DRDY` status from security cartridge         |
|     8 | R  | Coin switch input 1 (0 = coin being inserted) |
|     9 | R  | Coin switch input 2 (0 = coin being inserted) |
|    10 | R  | PCMCIA card 1 insertion (0 = card present)    |
|    11 | R  | PCMCIA card 2 insertion (0 = card present)    |
|    12 | R  | Service button (JAMMA pin R, 0 = pressed)     |
| 13-15 |    | Unused?                                       |

See the security cartridge section for more details about `IRDY` and  `DRDY`. In
order for bit 2 to be valid, `IO0` should be set as an input by clearing the
respective bit in register `0x1f500000`.

#### `0x1f400008` (ASIC register 4): **JAMMA controls**

| Bits | RW | Description                            |
| ---: | :- | :------------------------------------- |
|    0 | R  | Player 2 joystick left (JAMMA pin X)   |
|    1 | R  | Player 2 joystick right (JAMMA pin Y)  |
|    2 | R  | Player 2 joystick up (JAMMA pin V)     |
|    3 | R  | Player 2 joystick down (JAMMA pin W)   |
|    4 | R  | Player 2 button 1 (JAMMA pin Z)        |
|    5 | R  | Player 2 button 2 (JAMMA pin a)        |
|    6 | R  | Player 2 button 3 (JAMMA pin b)        |
|    7 | R  | Player 2 start button (JAMMA pin U)    |
|    8 | R  | Player 1 joystick left (JAMMA pin 20)  |
|    9 | R  | Player 1 joystick right (JAMMA pin 21) |
|   10 | R  | Player 1 joystick up (JAMMA pin 18)    |
|   11 | R  | Player 1 joystick down (JAMMA pin 19)  |
|   12 | R  | Player 1 button 1 (JAMMA pin 22)       |
|   13 | R  | Player 1 button 2 (JAMMA pin 23)       |
|   14 | R  | Player 1 button 3 (JAMMA pin 24)       |
|   15 | R  | Player 1 start button (JAMMA pin 17)   |

As buttons are active-low (wired between JAMMA pins and ground), all bits are 0
when a button is pressed and 1 otherwise. The BIOS and games often read from
this register and discard the result as a way of (inefficiently) flush the CPU's
write queue.

#### `0x1f40000a` (ASIC register 5): **Data from JVS MCU**

| Bits | RW | Description                |
| ---: | :- | :------------------------- |
| 0-15 | R  | Current data word from MCU |

This register is only valid when the `JVSIRDY` flag is set. After reading, a
dummy write to `0x1f520000` shall be issued to clear `JVSIRDY`. If the MCU has
more data available, it will update the register and set the flag again.

#### `0x1f40000c` (ASIC register 6): **JAMMA controls** / **External inputs**

| Bits  | RW | Description                             |
| ----: | :- | :-------------------------------------- |
|   0-7 |    | Unused?                                 |
|     8 | R  | Player 1 button 4 (JAMMA pin 25)        |
|     9 | R  | Player 1 button 5 (JAMMA pin 26)        |
|    10 | R  | Test button (built-in and JAMMA pin 15) |
|    11 | R  | Player 1 button 6                       |
| 12-15 |    | Unused?                                 |

As buttons are active-low (wired between JAMMA pins and ground), all bits are 0
when a button is pressed and 1 otherwise.

The signals for buttons 4 and 5 are wired in parallel to both JAMMA and the
`EXT-IN` connector, while button 6 can only be connected through `EXT-IN` and is
usually unused.

#### `0x1f40000e` (ASIC register 7): **JAMMA controls** / **External inputs**

| Bits  | RW | Description                             |
| ----: | :- | :-------------------------------------- |
|   0-7 |    | Unused?                                 |
|     8 | R  | Player 2 button 4 (JAMMA pin c)         |
|     9 | R  | Player 2 button 5 (JAMMA pin d)         |
|    10 |    | Main RAM layout type (0 = new, 1 = old) |
|    11 | R  | Player 2 button 6                       |
| 12-15 |    | Unused?                                 |

As buttons are active-low (wired between JAMMA pins and ground), all bits are 0
when a button is pressed and 1 otherwise.

The signals for buttons 4 and 5 are wired in parallel to both JAMMA and the
`EXT-IN` connector, while button 6 can only be connected through `EXT-IN` and is
usually unused.

Bit 10 is probed by the 700B01 BIOS kernel to determine how to configure the
main RAM controller. If cleared, the configuration register at `0x1f801060` is
set to `0x4788`, otherwise it is set to `0x0c80`. This check was introduced
alongside revision D of the main board, which features alternate footprints for
two 2 MB chips in place of eight 512 KB ones.

#### `0x1f520000`: **`JVSIRDY` clear**

| Bits | RW | Description |
| ---: | :- | :---------- |
| 0-15 |    | _Unused_    |

This register is a dummy write-only port that clears the `JVSIRDY` flag when any
value is written to it. The flag is set by the JVS MCU whenever a new data word
is available for reading from `0x1f40000a`.

#### `0x1f600000`: **External outputs**

| Bits | RW | Description                           |
| ---: | :- | :------------------------------------ |
|  0-7 | W  | To `OUT0-OUT7` on `EXT-OUT` connector |
| 8-15 |    | _Unused_                              |

The lower 8 bits written to this register are latched on pins `OUT0-OUT7` of the
external output connector (see the pinouts section). This connector is used by
some games to control cabinet lights without using an I/O board.

#### `0x1f680000`: **Data to JVS MCU**

| Bits | RW | Description      |
| ---: | :- | :--------------- |
| 0-15 | W  | Data word to MCU |

In order to prevent overruns, this register shall only be accessed when
`JVSDRDY` is cleared. Writing to it will set `JVSDRDY`.

## JVS interface

The System 573 is equipped with a JVS host interface, allowing for connection of
I/O modules, controllers and other devices that implement the JVS protocol
commonly used in arcade cabinets.

JVS uses a single RS-485 bus running at 115200 bits per second, shared by all
devices. The standard JVS connector is a single USB-A port, with the data lines
used as the RS-485 differential pair and the `VBUS` pin as a sensing line (see
the JVS specification for details). JVS devices typically have a full size USB-B
port for connection to the host, plus optionally another USB-A port for daisy
chaining additional devices. The RS-485 bus needs to be terminated; some boards
will automatically insert a termination resistor when connected as the last node
in a daisy chain.

The 573's [video output](pinouts.md#rgb-output-db15) is 15 KHz only, so make
sure the cabinet or monitor supports 15 KHz video when using it with a JVS
cabinet.

### Packet format

A JVS packet can be up to 258 bytes long and is made up of the following fields:

| Byte | Description                                                    |
| ---: | :------------------------------------------------------------- |
|    0 | Synchronization byte, must be `0xe0`                           |
|    1 | Destination address                                            |
|    2 | Length (number of payload bytes including checksum)            |
|   3- | Payload                                                        |
|      | Checksum (sum of address, length and payload bytes modulo 256) |

**NOTE**: when a JVS packet is sent over the RS-485 bus, any `0xd0` or `0xe0`
byte other than the synchronization byte must be escaped as `0xd0 0xcf` or
`0xd0 0xdf` respectively, in order to allow downstream devices to reliably
determine the end of a packet. On the 573, the JVS MCU handles escaping outbound
packets and unescaping inbound packets automatically. The escaping process does
*not* update the length field to reflect the escaped length of the packet.

Refer to the JVS specification for details on the contents of standard and
vendor-specific payloads.

### MCU communication protocol

The system's JVS interface is managed by a dedicated H8/3644 microcontroller,
interfaced through two 16-bit latches and handshaking lines (in a similar way to
the 8-bit ports on the security cartridge slot). The MCU's firmware is stored in
OTP ROM and consists of a simple loop that buffers the data written by the 573,
sends it, waits for a response to be received and lets the 573 read it.

In order to perform a JVS transaction the 573 must:

1.  Reset the MCU through register `0x1f400000`, clear `JVSIRDY` by writing to
    `0x1f520000` then wait for the status and error codes in register
    `0x1f400004` to be set to 0 and 3 respectively.
2.  Write the packet two bytes at a time to `0x1f680000`, waiting for `JVSDRDY`
    to go low before each write. Words are little endian, so for instance the
    first word of a packet with destination address `0x01` would be `0x01e0`. If
    the total length of the packet is odd, the last byte shall still be written
    as a word (with the upper byte zeroed out).
3.  Wait for the status code to become 1. At this point the MCU will send the
    packet and wait for a response from a device on the bus.
4.  Wait for the status code to become 0, signalling a valid response has been
    received and can be read out. A timeout should be implemented here, as the
    MCU will wait for a response indefinitely even if no device is present. The
    MCU has no concept of a broadcast, so this also applies to the JVS reset
    command: nothing on the bus answers a reset, so the MCU blocks on it forever
    and `JVSDRDY` never drops again. The status and error codes read 1 and 3
    throughout - busy, no error - and no further packet will be written out. The
    only way out is resetting the MCU through bit 8 of `0x1f400000`.
5.  Read the packet, again two bytes at a time, from `0x1f40000a`, waiting for
    `JVSIRDY` to go high before each read and clearing it by writing to
    `0x1f520000` after each read. The status code will be set to 2 after the
    first word is read and back to 0 once no more data is available to read.

The MCU does not allow for non-JVS packets to be sent as it validates the sync
byte, checksum and uses the length field to determine packet length. Responses
cannot be received without sending a packet first either. The MCU will also
insert a 200 µs minimum delay between the last byte of a received packet and the
first byte of the next packet.
