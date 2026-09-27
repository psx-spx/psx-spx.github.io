## Security cartridges

Most System 573 games use cartridges that plug into the slot on the right side
of the main board as an anti-piracy measure and/or to add game specific I/O
functionality (particularly for games that do not otherwise require any I/O
board). Cartridges typically contain a password protected EEPROM, used to store
game and installation information, and in some cases a DS2401 unique serial
number chip.

- [Electrical interface](#electrical-interface)
- [Cartridge EEPROM types](#cartridge-eeprom-types)
- [EEPROM-less cartridge variants](#eeprom-less-cartridge-variants)
- [X76F041 cartridge variants](#x76f041-cartridge-variants)
- [ZS01 cartridge variants](#zs01-cartridge-variants)
- [Cartridge identifiers](#cartridge-identifiers)

### Electrical interface

All communication with the cartridge is performed through the following means:

- an 8-bit parallel input port (`I0-I7`), readable via register `0x1f400004`;
- a latched 8-bit parallel output port (`D0-D7`), controlled by register
  `0x1f6a0000`;
- a single tristate I/O pin (`IO0`), which can be either configured as a
  floating input or set to output the same logic level as `D0` through register
  `0x1f500000`;
- the CPU's SIO1 interface (`TX`, `RX`, `/RTS`, `/CTS`, `/DTR`, `/DSR`);
- four bus handshaking lines (`IRDY`, `DRDY`, `/IREQ`, `/DACK`).

As all EEPROMs used in cartridges have an I2C interface rather than a parallel
one, `IO0` is used in combination with individual bits of the parallel I/O ports
to bitbang I2C. The SIO1 interface either goes unused or is translated to RS-232
voltage levels and broken out to a connector on the cartridge.

See the pinouts section for more information on the security cartridge slot.

#### Handshaking lines

The cartridge slot carries two status lines *unofficially* known as `IRDY` and
`DRDY` plus two inputs named `/IREQ` and `/DACK`, probably meant for
synchronization with cartridges that would actually use `D0-D7` and `I0-I7` as a
parallel data bus rather than to bitbang serial protocols. No currently known
cartridge uses these pins.

`DRDY` is set whenever the 573 writes to the output port, even if no bits have
actually changed. The cartridge can monitor this signal to know when to read a
byte from the port and then pull `/DACK` low to reset it. To send a byte to the
573 the cartridge can pulse `/IREQ`, which will cause `IRDY` to go high until
the 573 accesses the input port. The 573 can read the status of `IRDY` (as well
as `DRDY`) through the Konami ASIC and wait for it to be set before reading the
next byte.

The cartridge I/O ports can basically be thought of as a single-byte FIFO, with
`DRDY` being the "TX buffer full" flag and `IRDY` the "RX buffer not empty"
flag. The handshaking lines are implemented using a handful of 74LS74 flip
flops.

**NOTE**: the JVS MCU also has its own handshaking lines, `JVSIRDY` and
`JVSDRDY`, which are actually used and work in pretty much the same way. See the
JVS interface section for more information on communicating with the MCU.

#### Note about RTS/CTS

The PS1 CPU's SIO1 UART has hardware flow control and will not transmit data
until CTS is asserted. In order to get around this most cartridges tie CTS to
RTS, allowing it to be controlled in software. Cartridges that use the serial
port (i.e. ones with a network port) have the pins tied together on the PCB,
while other cartridge types usually break them out to a shorted 2-pin jumper.

Some earlier games that do not use SIO1 for networking purposes redirect their
debug logging output to it (by calling the `AddSIO()` function provided by the
Sony SDK) if CTS and RTS are shorted on startup. On later 573 motherboard
revisions, the SIO1 pins are additionally broken out to a separate connector
(`CN24`) and made accessible even when a cartridge without a network port is
inserted.

### Cartridge EEPROM types

Konami's security cartridge driver supports the following EEPROMs:

| Manufacturer     | Chip                                          | "Response to reset" ID    | Capacity  |
| :--------------- | :-------------------------------------------- | :------------------------ | --------: |
| Xicor            | [X76F041](#x76f041-cartridge-variants)        | `19 55 aa 55` (LSB first) | 512 bytes |
| Xicor            | X76F100                                       | `19 00 aa 55` (LSB first) | 112 bytes |
| Konami/Microchip | [ZS01 (PIC16CE625)](#zs01-cartridge-variants) | `5a 53 00 01` (MSB first) | 112 bytes |

**NOTE**: Konami seems to have never manufactured X76F100 cartridges, however
most games that expect an X76F041 can also use the X76F100 interchangeably. ZS01
support was only added in later versions of the driver.

#### ZS01 protocol

The "ZS01" EEPROM (also known as "NS2K001") is actually a PIC16 microcontroller
that mostly replicates the X76F100's functionality, allowing the 573 to store up
to 112 bytes of data protected by a 64-bit password. Unlike the X76F041 and
X76F100, which use plaintext commands, all communication with the ZS01 is
obfuscated using a rudimentary scrambling algorithm. A CRC16 is attached to each
packet and used to detect attempts to tamper with the obfuscation. Attempting to
send too many requests with an invalid CRC16 will cause the ZS01 to self-erase
and reset the password.

A ZS01 transaction can be broken down into the following steps:

1.  The 573 prepares a 12-byte packet to be sent to the ZS01, containing a
    command, address and payload:

    | Bytes | Description                                       |
    | ----: | :------------------------------------------------ |
    |     0 | Command flags                                     |
    |     1 | Address bits 0-7                                  |
    |   2-9 | Payload (data for writes, response key for reads) |
    | 10-11 | CRC16 of bytes 0-9, big endian                    |

    The first byte is a 3-bit bitfield encoding the command and access type:

    | Bits | Description                                    |
    | ---: | :--------------------------------------------- |
    |    0 | Command (0 = write/erase, 1 = read)            |
    |    1 | Address bit 8 (unused, should be 0)            |
    |    2 | Access type (0 = unprivileged, 1 = privileged) |
    |  3-7 | Unused? (should be 0)                          |

    The access type bit specifies whether the command is privileged. Privileged
    commands require the ZS01's current password, while unprivileged commands do
    not.

    The address must be one of the following values:

    | Address     | Length   | Privileged | Description                                |
    | :---------- | -------: | :--------- | :----------------------------------------- |
    | `0x00-0x03` | 32 bytes | No         | Unprivileged data area                     |
    | `0x04-0x0e` | 80 bytes | Yes        | Privileged data area                       |
    | `0xfc`      |  8 bytes | No         | Internal ZS01 serial number                |
    | `0xfd`      |  8 bytes | No         | External DS2401 serial number              |
    | `0xfd`      |  8 bytes | Yes        | Erases data area when written (write-only) |
    | `0xfe`      |  8 bytes | Yes        | Configuration registers                    |
    | `0xff`      |  8 bytes | Yes        | New password (write-only)                  |

    Data is always read or written in aligned 8 byte blocks. Unprivileged areas
    can be read using either a privileged or unprivileged read command, but
    writing to them still requires a privileged write command.

2.  If the command is a read command, a random 8-byte "response key" is
    generated (typically as an MD5 hash of the current time from the RTC) and
    written to the payload field; the ZS01 will later use it to encrypt the
    returned data as a replay attack prevention measure. For write commands, the
    payload field is populated with the 8 bytes to be written.

3.  A CRC16 is calculated over the first 10 bytes of the packet and stored in
    the last 2 bytes in big endian format. The CRC is computed as follows:

    ```c
    #define ZS01_CRC16_POLYNOMIAL 0x1021

    uint16_t zs01_crc16(const uint8_t *data, size_t length) {
        uint16_t crc = 0xffff;

        for (; length; length--) {
            crc ^= *(data++) << 8;

            for (int bit = 8; bit; bit--) {
                uint16_t temp = crc;

                crc <<= 1;
                if (temp & (1 << 15))
                    crc ^= ZS01_CRC16_POLYNOMIAL;
            }
        }

        return (~crc) & 0xffff;
    }
    ```

4.  If the command is privileged, the 573 scrambles the payload field with the
    chip's currently set password, using the following algorithm:

    ```c
    // Note that this state is preserved across calls to zs01_scramble_payload()
    // and must be updated when a response is received (see step 8).
    uint8_t zs01_scrambler_state = 0;

    void zs01_scramble_payload(
        uint8_t *output, const uint8_t *input, size_t length,
        const uint8_t *password
    ) {
        for (; length; length--) {
            int value = *(input++) ^ zs01_scrambler_state;
            value     = (value + password[0]) & 0xff;

            for (int i = 1; i < 8; i++) {
                int add   = password[i] & 0x1f;
                int shift = password[i] >> 5;

                int shifted = value << shift;
                shifted    |= value >> (8 - shift);
                shifted    &= 0xff;

                value = (shifted + add) & 0xff;
            }

            zs01_scrambler_state = value;
            *(output++)          = value;
        }
    }
    ```

    The CRC16 is *not* updated to reflect the new data. This step is skipped for
    unprivileged read commands.

5.  All 12 bytes of the packet are scrambled with a fixed "command key", using
    the following algorithm:

    ```c
    static const uint8_t ZS01_COMMAND_ADD[]   = { 237, 8, 16, 11, 6, 4, 8, 30 };
    static const uint8_t ZS01_COMMAND_SHIFT[] = {   0, 3,  2,  2, 6, 2, 2,  1 };

    void zs01_scramble_packet(
        uint8_t *output, const uint8_t *input, size_t length
    ) {
        // Unlike zs01_scramble_payload(), this state is *not* preserved across
        // calls.
        uint8_t state = 0xff;

        output += length;
        input  += length;

        for (; length; length--) {
            int value = *(--input) ^ state;
            value     = (value + ZS01_COMMAND_ADD[0]) & 0xff;

            for (int i = 1; i < 8; i++) {
                int shifted = value << ZS01_COMMAND_SHIFT[i];
                shifted    |= value >> (8 - ZS01_COMMAND_SHIFT[i]);
                shifted    &= 0xff;

                value = (shifted + ZS01_COMMAND_ADD[i]) & 0xff;
            }

            state       = value;
            *(--output) = value;
        }
    }
    ```

6.  The scrambled packet is sent to the ZS01, which will respond to the first 11
    bytes immediately with an I2C ACK and to the last byte with an ACK after a
    short delay. The 573 then proceeds to read 12 bytes from the ZS01, issuing
    an I2C ACK for each byte received up until the last one.

7.  The 573 uses the response key generated in step 2 to unscramble the packet
    returned by the ZS01. The unscrambling algorithm is the same one used in
    step 5, applied in reverse:

    ```c
    void zs01_unscramble_packet(
        uint8_t *output, const uint8_t *input, size_t length,
        const uint8_t *response_key
    ) {
        uint8_t state = 0xff;

        output += length;
        input  += length;

        for (; length; length--) {
            int value      = *(--input);
            int last_state = state;
            state          = value;

            for (int i = 1; i < 8; i++) {
                int add   = response_key[i] & 0x1f;
                int shift = response_key[i] >> 5;

                int subtracted = (value - add) & 0xff;

                value  = subtracted >> shift;
                value |= subtracted << (8 - shift);
                value &= 0xff;
            }

            value       = (value - response_key[0]) & 0xff;
            *(--output) = value ^ last_state;
        }
    }
    ```

    For write commands, the response key required to unscramble the packet is
    the one sent as part of the last read command issued. For read commands, the
    ZS01 may either use the key provided in the payload field or the one from
    the last read command issued; Konami's code tries unscrambling responses
    with both.

8.  The unscrambled packet will contain the following fields:

    | Bytes | Description                                |
    | ----: | :----------------------------------------- |
    |     0 | Status code (0 = success, 1-5 = error)     |
    |     1 | New payload scrambler state                |
    |   2-9 | Payload (empty for writes, data for reads) |
    | 10-11 | CRC16 of bytes 0-9, big endian             |

    The 573 proceeds to compute the CRC16 of the first 10 bytes. If it does not
    match the one in the packet, it will try unscrambling the packet with a
    different response key (see step 7) before giving up. Otherwise, the global
    `zs01_scrambler_state` variable from step 4 is set to the value of byte 1,
    regardless of whether the status code is zero or not.

    The exact meaning of non-zero status codes is currently unknown.

### EEPROM-less cartridge variants

#### Hyper Bishi Bashi Champ 3-player cartridge (`GX700-PWB(E)`)

This is the only known cartridge type that has no EEPROM (although the PCB does
have an unpopulated X76F041 footprint). It has no plastic case, as it's meant to
be enclosed in the same case as the 573 itself. It has open-drain outputs for
driving up to 12 lights, arranged as 3 banks of 4 outputs each (one bank for
each player's buttons), plus an RS-232 transceiver for SIO1. The following pins
are used:

| Name   | Dir | Usage                                            |
| :----- | :-- | :----------------------------------------------- |
| `TX`   | O   | `TX` to network port (via RS-232 transceiver)    |
| `RX`   | I   | `RX` from network port (via RS-232 transceiver)  |
| `/RTS` | O   | Shorted to `/CTS` to enable SIO1                 |
| `/CTS` | I   | Shorted to `/RTS` to enable SIO1                 |
| `/DSR` | I   | Cartridge insertion detection (grounded)         |
| `D0`   | O   | Updates/latches bank 3 when pulsed               |
| `D1`   | O   | Updates/latches bank 2 when pulsed               |
| `D3`   | O   | Updates/latches bank 1 when pulsed               |
| `D4`   | O   | Data for light output 0 (green button)           |
| `D5`   | O   | Data for light output 1 (blue button)            |
| `D6`   | O   | Data for light output 2 (red button)             |
| `D7`   | O   | Data for light output 3 (start button)           |
| `?`    | O   | `DTR` to network port (via RS-232 transceiver)   |
| `?`    | I   | `DSR` from network port (via RS-232 transceiver) |

This cartridge has three connectors:

- `CN2` (5-pin): RS-232 port. Note that this port is *not* electrically isolated
  and shares its ground with the 573, unlike all other cartridges with an RS-232
  connector.
- `CN3` (16-pin): breaks out the light outputs and the incoming 12V supply from
  `CN4`.
- `CN4` (4-pin): 12V power input, connected through a short cable to `CN17` on
  the 573 main board.

### X76F041 cartridge variants

All X76F041 cartridges use the following pins:

| Name   | Dir | Usage                                                |
| :----- | :-- | :--------------------------------------------------- |
| `/DSR` | I   | Cartridge insertion detection (grounded)             |
| `D0`   | O   | Drives X76F041 I2C `SDA` when `IO0` is set as output |
| `D1`   | O   | X76F041 I2C `SCL`                                    |
| `D2`   | O   | X76F041 chip select (`/CS`)                          |
| `D3`   | O   | X76F041 reset (`RST`)                                |
| `IO0`  | IO  | X76F041 I2C `SDA` readout                            |

X76F041 cartridges equipped with a DS2401 additionally use the following pins:

| Name   | Dir | Usage                                  |
| :----- | :-- | :------------------------------------- |
| `D4`   | O   | Drives 1-wire bus low when pulled high |
| `I6`   | I   | DS2401 1-wire bus readout              |

#### Generic cartridge (`GX700-PWB(D)`)

Rectangular cartridge used by the earliest 573 games and as a separate
installation key for some later games. Contains only the X76F041 EEPROM and no
DS2401, but the PCB has an unpopulated footprint for an unknown 64-pin TQFP
part.

#### Generic cartridge with DS2401 (`GX894-PWB(D)`)

Rectangular cartridge similar to `GX700-PWB(D)` but equipped with a DS2401. The
PCB has two unpopulated SOIC footprints, one of which may possibly be for an
X76F100 or another I2C EEPROM.

#### Early serial port cartridge (`GX896-PWB(A)A`)

Seems to be an older variant of the more common `GX883-PWB(D)` cartridge, with
the same ports but no DS2401. As with the 3-player Bishi Bashi cartridge, it has
no case and is instead meant to sit inside the 573's own case.

| Name   | Dir | Usage                                            |
| :----- | :-- | :----------------------------------------------- |
| `TX`   | O   | `TX` to network port (via RS-232 transceiver)    |
| `RX`   | I   | `RX` from network port (via RS-232 transceiver)  |
| `/RTS` | O   | Shorted to `/CTS` to enable SIO1                 |
| `/CTS` | I   | Shorted to `/RTS` to enable SIO1                 |
| `?`    | O   | `CTRL0` to control port                          |
| `?`    | O   | `CTRL1` to control port                          |
| `?`    | O   | `CTRL2` to control port                          |
| `?`    | O   | `DTR` to network port (via RS-232 transceiver)   |
| `?`    | I   | `DSR` from network port (via RS-232 transceiver) |

This cartridge has two connectors:

- `CN2` (5-pin): electrically isolated RS-232 port. The transceiver is powered
  by an isolated DC-DC module and all signals going from/to the 573 are
  optoisolated.
- `CN3` (6-pin): three 5V logic level signals, used in some cabinets to control
  lights or the speaker amplifier.

#### Serial port cartridge with DS2401 (`GX883-PWB(D)`)

T-shaped cartridge with a DS2401, a "network" (RS-232) port and a "control" or
"amp box" port, commonly used by pre-ZS01 Bemani games. Uses the following pins:

| Name   | Dir | Usage                                            |
| :----- | :-- | :----------------------------------------------- |
| `TX`   | O   | `TX` to network port (via RS-232 transceiver)    |
| `RX`   | I   | `RX` from network port (via RS-232 transceiver)  |
| `/RTS` | O   | Shorted to `/CTS` to enable SIO1                 |
| `/CTS` | I   | Shorted to `/RTS` to enable SIO1                 |
| `?`    | O   | `CTRL0` to control port                          |
| `?`    | O   | `CTRL1` to control port                          |
| `?`    | O   | `CTRL2` to control port                          |
| `?`    | O   | `DTR` to network port (via RS-232 transceiver)   |
| `?`    | I   | `DSR` from network port (via RS-232 transceiver) |

This cartridge has two connectors:

- Network (5-pin, unlabeled on PCB): electrically isolated RS-232 port. The
  transceiver is powered by an isolated DC-DC module and all signals going
  from/to the 573 are optoisolated.
- Control/amp box (6-pin, unlabeled on PCB): three 5V logic level signals, used
  in some cabinets to control lights or the speaker amplifier.

#### PunchMania cartridge (`GX700-PWB(J)`)

T-shaped cartridge used only by PunchMania/Fighting Mania series. Contains an
X76F041, a DS2401 and an ADC0838 used to measure up to 8 analog inputs. The ADC
uses the following pins:

| Name | Dir | Usage                                                 |
| :--- | :-- | :---------------------------------------------------- |
| `D0` | O   | Chip select to ADC (`/CS`), shared with X76F041 `SDA` |
| `D1` | O   | Data clock to ADC (`CLK`), shared with X76F041 `SCL`  |
| `D5` | O   | Data input to ADC (`DI`)                              |
| `I0` | I   | Data output from ADC (`DO`)                           |
| `I1` | I   | SAR status from ADC (`SARS`)                          |

This cartridge has two connectors:

- Unknown (12-pin): analog input connector. As with the ADC built into the 573
  motherboard there seems to be no protection on the inputs, so only voltages in
  0-5V range are accepted.
- `CN4` (10-pin): unknown purpose. Seems to be always unpopulated.

#### Hyper Bishi Bashi Champ 2-player cartridge (`PWB0000068819`)

T-shaped cartridge with open-drain outputs for driving up to 8 lights, arranged
as 2 banks of 4 outputs each. Unlike the `GX700-PWB(E)` 3-player variant, it has
an X76F041 (but no DS2401), lacks the RS-232 port and does not seem to be
designed to be mounted inside the 573. The latches driving the light outputs use
the following pins:

| Name | Dir | Usage                                  |
| :--- | :-- | :------------------------------------- |
| `?`  | O   | Updates/latches bank 1 when pulsed     |
| `?`  | O   | Updates/latches bank 2 when pulsed     |
| `?`  | O   | Data for light output 0 (green button) |
| `?`  | O   | Data for light output 1 (blue button)  |
| `?`  | O   | Data for light output 2 (red button)   |
| `?`  | O   | Data for light output 3 (start button) |

This cartridge has two connectors:

- `CN2` (16-pin): breaks out the light outputs and the incoming 12V supply from
  `CN3`.
- `CN3` (4-pin): 12V power input, presumably connected to the power supply
  externally (i.e. not through the main board).

#### Salary Man Champ cartridge (`PWB0000088954`)

T-shaped cartridge with open-drain outputs for driving up to 8 lights (although
only 6 outputs seem to be populated). Contains an X76F041, a DS2401 and two 4094
shift registers, presumably chained. The shift registers use the following pins:

| Name | Dir | Usage                |
| :--- | :-- | :------------------- |
| `D5` | O   | Shift register clock |
| `D6` | O   | Shift register reset |
| `D7` | O   | Shift register data  |

This cartridge has two connectors:

- Unlabeled (16-pin): breaks out the light outputs and the incoming 12V supply.
- Unlabeled (4-pin): 12V power input, presumably connected to the power supply
  externally (i.e. not through the main board).

### ZS01 cartridge variants

All ZS01 cartridges use the following pins:

| Name   | Dir | Usage                                             |
| :----- | :-- | :------------------------------------------------ |
| `/DSR` | I   | Cartridge insertion detection (grounded)          |
| `D0`   | O   | Drives ZS01 I2C `SDA` when `IO0` is set as output |
| `D1`   | O   | ZS01 I2C `SCL`                                    |
| `D3`   | O   | ZS01 reset                                        |
| `IO0`  | IO  | ZS01 I2C `SDA` readout                            |

All cartridges are fitted with a DS2401, however it is connected to a GPIO pin
on the ZS01 rather than being directly exposed to the 573. The ZS01 additionally
provides its own unique serial number, which seems to be unused by games.

#### Serial port cartridge (`GE949-PWB(D)A`)

ZS01 variant of the `GX883-PWB(D)` cartridge. Uses the following pins:

| Name   | Dir | Usage                                            |
| :----- | :-- | :----------------------------------------------- |
| `TX`   | O   | `TX` to network port (via RS-232 transceiver)    |
| `RX`   | I   | `RX` from network port (via RS-232 transceiver)  |
| `/RTS` | O   | Shorted to `/CTS` to enable SIO1                 |
| `/CTS` | I   | Shorted to `/RTS` to enable SIO1                 |
| `?`    | O   | `CTRL0` to control port                          |
| `?`    | O   | `CTRL1` to control port                          |
| `?`    | O   | `CTRL2` to control port                          |
| `?`    | O   | `DTR` to network port (via RS-232 transceiver)   |
| `?`    | I   | `DSR` from network port (via RS-232 transceiver) |

This cartridge has two connectors:

- Network (5-pin, unlabeled on PCB): electrically isolated RS-232 port. The
  transceiver is powered by an isolated DC-DC module and all signals going
  from/to the 573 are optoisolated.
- Control/amp box (6-pin, unlabeled on PCB): three 5V logic level signals, used
  in some cabinets to control lights or the speaker amplifier.

#### Stripped down serial port cartridge (`GE949-PWB(D)B`)

T-shaped cartridge that uses the same PCB as `GE949-PWB(D)A` but only has the
ZS01, DS2401 and supporting parts are populated. Used by games that do not need
the RS-232 interface.

### Cartridge identifiers

Most games use the security cartride's EEPROM to store, among other data such as
the game code and region, a set of up to four 8-byte identifiers.

#### SID (silicon/serial ID?)

The serial number of the cartridge's DS2401, always present in cartridges that
have one. As per the 1-wire specification it has the following format:

| Bytes | Description                                     |
| ----: | :---------------------------------------------- |
|     0 | 1-wire family code (`0x01` for DS2401)          |
|   1-6 | 48-bit progressive serial number, little endian |
|     7 | CRC8 of bytes 0-6                               |

The CRC is computed as follows:

```c
#define DS2401_CRC8_POLYNOMIAL 0x8c

uint8_t ds2401_crc8(const uint8_t *data, size_t length) {
    uint8_t crc = 0;

    for (; length; length--) {
        uint8_t value = *(data++);

        for (int bit = 8; bit; bit--) {
            uint8_t temp = crc ^ value;

            value >>= 1;
            crc   >>= 1;
            if (temp & 1)
                crc ^= DS2401_CRC8_POLYNOMIAL;
        }
    }

    return crc & 0xff;
}
```

Refer to the DS2401 datasheet and Maxim 1-wire documentation for more details.

#### TID (trace ID)

Seems to be a cartridge-type-agnostic serial number. On cartridges without a
DS2401 the trace ID is assigned by Konami at manufacture time (see the master
calendar section) and has the following format:

| Bytes | Description                                   |
| ----: | :-------------------------------------------- |
|     0 | Trace ID type (`0x81`)                        |
|   1-2 | 16-bit "main" serial number, big endian       |
|   3-6 | 32-bit "sub" serial number, big endian        |
|     7 | Checksum (sum of bytes 0-6 xor'd with `0xff`) |

On cartridges with a DS2401 the trace ID is instead derived from the SID:

| Bytes | Description                                                       |
| ----: | :---------------------------------------------------------------- |
|     0 | Trace ID type (`0x82`)                                            |
|   1-2 | DS2401 serial number hash, big or little endian depending on game |
|   3-6 | _Reserved_ (must be 0)                                            |
|     7 | Checksum (sum of bytes 0-6 xor'd with `0xff`)                     |

The hash is calculated over bytes 1-6 of the SID (excluding the family code and
CRC8) using the following algorithm:

```c
// Note that some games set this to 14 instead of 16.
#define TRACE_ID_HASH_BIT_WIDTH 16

uint16_t trace_id_hash(const uint8_t *data, size_t length) {
    uint16_t hash = 0;

    for (size_t i = 0; i < (length * 8); i += 8) {
        uint8_t value = *(data++);

        for (size_t j = i; j < (i + 8); j++, value >>= 1) {
            if (value & 1)
                hash ^= 1 << (j % TRACE_ID_HASH_BIT_WIDTH);
        }
    }

    return hash;
}
```

#### MID (medium ID?)

Seems to be some kind of cartridge type flag, possibly indicating whether the
cartridge shall be used during or after game installation, or if it was used
when performing a game upgrade and shall no longer be usable to run the game it
initially shipped with.

| Bytes | Description                                       |
| ----: | :------------------------------------------------ |
|     0 | Cartridge type? (always `0x00`, `0x01` or `0x02`) |
|   1-6 | _Reserved_ (must be 0)                            |
|     7 | Checksum (sum of bytes 0-6 xor'd with `0xff`)     |

**NOTE**: `00 00 00 00 00 00 00 00` seems to be a valid MID value, despite
having an otherwise invalid checksum, and to have a different meaning from
`00 00 00 00 00 00 00 ff`.

#### XID (external ID?)

The serial number of the digital I/O board's DS2401, written to the cartridge
during installation by most games that use it in order to prevent reinstallation
on a different system. Has the same format as the SID. On a cartridge that has
not yet been paired to a 573 the XID is set to `00 00 00 00 00 00 00 00`.

When finishing installation or attempting to use a cartridge with a mismatching
XID the game will display the digital I/O board's serial number as an 8-digit
value (`XXXX-YYYY`), generated as follows:

```c
// Some games seem to only use the lower 32 bits of the DS2401's serial number,
// while others use all 48 bits.
size_t xid_to_string_32(char *output, const uint8_t *xid) {
    uint32_t value = 0
        | (xid[1] <<  0)
        | (xid[2] <<  8)
        | (xid[3] << 16)
        | (xid[4] << 24);

    int high = (value / 10000) % 10000;
    int low  = value % 10000;

    return sprintf(output, "%04d-%04d", high, low);
}

size_t xid_to_string_48(char *output, const uint8_t *xid) {
    uint64_t value = 0
        | (xid[1] <<  0)
        | (xid[2] <<  8)
        | (xid[3] << 16)
        | (xid[4] << 24)
        | (xid[5] << 32)
        | (xid[6] << 40);

    int high = (int) ((value / 10000) % 10000);
    int low  = (int) (value % 10000);

    return sprintf(output, "%04d-%04d", high, low);
}
```

Cartridges for games that use the digital I/O board typically come with a blank
label onto which the 8-digit ID can be written by the operator, to help keep
track of which cartridge goes into which system after installation.

Note that games that use other I/O boards with a DS2401, such as Kick &amp; Kick
and DDR Karaoke Mix, do not seem to write those boards' serial numbers to the
cartridge; they are stored in the internal flash memory instead.
