
# Konami System 573

The System 573 is a PlayStation-based system used in a number of Konami arcade
games from the late 90s and early 2000s, most notably Dance Dance Revolution and
other titles from the Bemani series of rhythm games.

- [Differences vs. PS1](#differences-vs-ps1)
- [Register map](#register-map)
- [JVS interface](#jvs-interface)
- [I/O boards](#io-boards)
- [Security cartridges](#security-cartridges)
- [External modules](#external-modules)
- [Connectors](#connectors)
- [BIOS](#bios)
- [Game-specific information](#game-specific-information)
- [Misc. notes](#misc-notes)
- [Pinouts](#pinouts)
- [Credits, sources and links](#credits-sources-and-links)

This document is currently work-in-progress. Here is an incomplete list of
things that need more research:

- The BIOS and games are notoriously picky about ATAPI drives. Konami's code
  shall be disassembled and tested in order to find out where and why drive
  initialization fails with most drives.
- The fishing controls I/O board has been fully reverse engineered, but
  documentation for it is missing.
- The DDR stage I/O board's communication protocol is largely unknown. More
  tests need to be done on real hardware and its CPLD shall be dumped if
  possible.
- The protocol used by the 573 to communicate with the e-Amusement network PCB
  is currently not known.

## Differences vs. PS1

### Main changes

- **Main RAM is 4 MB** instead of 2 MB and **VRAM is 2 MB** instead of 1 MB. SPU
  RAM is still 512 KB.
- **The CD-ROM drive is completely different**. While the PS1's drive is fully
  integrated into the motherboard and uses a custom protocol, the 573 employs a
  standard ATAPI drive. This means there is no provision for playing XA-ADPCM,
  even though CD audio can still be played (as long as the 4-pin audio cable
  between the drive and the 573 motherboard is present). There is no wobble
  groove to worry about, but some drives the system shipped with are reportedly
  unable to read CD-Rs. Most 573 units have had their drive replaced (usually
  with a DVD drive) at least once, so this should not be an issue.
- **The SIO0 bus for controllers and memory cards is unused**. It is broken out
  to a connector, however no known I/O board uses it. Some games supported PS1
  controllers and memory cards through an adapter connected over JVS (see the
  external modules section).
- **The "parallel I/O" expansion port is replaced by 2 PCMCIA slots**. These
  slots are wired in parallel and mapped at the same address as the internal
  flash through bank switching. They are fairly limited though as they only
  support 16-bit bus accesses (i.e. `/CE1` and `/CE2` are tied together, even
  though the CPU actually exposes them as separate signals!), have no DMA and
  don't expose the PCMCIA I/O and configuration space (`/IORD` and `/IOWR` are
  not connected at all). This makes them incompatible with CF cards and most
  PCMCIA devices.

### Additional hardware

- **JAMMA interface and built-in I/O ports**: the 573 provides multiple digital
  and analog ports for interfacing with arcade cabinet controls. Depending on
  the I/O board the system came with, these signals might be broken out through
  connectors on the system's case.
- **Internal 16 MB flash memory**: the 573's BIOS is capable of booting either
  from the CD drive or from an array of flash memory chips soldered to the
  motherboard, which are also memory-mapped. Most Konami games are designed to
  run from flash: when attempting to run them from CD without also having them
  installed, the executable on the disc will erase the flash and install the
  game before starting. Most games still require the CD, in some cases a
  different one, to be kept in the drive after installation as they use it for
  music playback or to stream additional data.
- **PCMCIA memory card**: some games shipped with additional flash memory in the
  form of one or more 16 or 32 MB PCMCIA cards. Note that these are "linear"
  memory mapped flash cards without any built-in controller, not CF or
  ATA-compatible cards (which would be incompatible with the 573's PCMCIA
  wiring).
- **RTC and battery-backed 8 KB RAM**: used by games to store settings, save
  data and installation info (possibly including serial numbers). Unfortunately
  the RTC chip is one of those all-in-one things with a battery sealed inside,
  soldered directly to the motherboard.
- **JVS host**: allows connection of multiple daisy chained peripherals using
  the standardized JVS protocol, based on a serial (RS-485) bus. The JVS port on
  the 573 was only ever "officially" used for the PS1 memory card reader module,
  however some games seem to support JVS I/O boards and input devices in
  addition to the built-in JAMMA connector.
- **Security cartridge**: optionally installed on the 573's side, contains a
  password protected EEPROM that holds factory pre-programmed data as well as
  keys generated during game installation, plus in some case a 64-bit serial
  number ROM. Security cartridges were bundled with most game discs as a way to
  prevent copying, as the discs themselves had no other protection of any kind.
  The CPU's serial port (SIO1) is also wired to the security cartridge slot.

## Register map

All standard PS1 registers, with the exception of the CD-ROM drive's, are
present and accessible. System 573-specific hardware is mapped into the EXP1
region at `0x1f000000`. IRQ10 and DMA5, normally reserved for the expansion bus
(and lightguns) on a regular PS1, are used to access the ATAPI drive, while IRQ2
and DMA3 go unused.

**NOTE**: EXP1 must be configured prior to accessing any of these registers. The
configuration value written by Konami's code to the EXP1 delay/size register at
`0x1f801008` is `0x24173f47`. Afterwards, *all* bus writes shall be 16 or 32
bits wide. The behavior of 8-bit writes is undefined, but 8-bit reads work as
intended.

| Address range           | Description                                            |
| :---------------------- | :----------------------------------------------------- |
| `0x1f000000-0x1f3fffff` | Bank switched, can be mapped to flash or PCMCIA slots  |
| `0x1f400000-0x1f40000f` | [Konami ASIC registers](#konami-asic-registers)        |
| `0x1f480000-0x1f48000f` | [IDE register bank 0](#ide-registers)                  |
| `0x1f4c0000-0x1f4c000f` | [IDE register bank 1](#ide-registers)                  |
| `0x1f620000-0x1f623fff` | [RTC registers](#rtc-registers) and battery-backed RAM |
| `0x1f640000-0x1f6400ff` | [I/O board registers](#io-boards)                      |

### Konami ASIC registers

Registers in the `0x1f400000-0x1f40000f` region are handled by the Konami 056879
I/O ASIC, consisting of a single 8-bit output port and at least six 16-bit input
ports. The same chip was used in other Konami arcade boards of the time.

#### `0x1f400000` (ASIC register 0): **ADC SPI, coin counters, audio**

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
CD/MP3 output to separate jacks on the sub-panel rather than routing it through
the motherboard, making bit 6 meaningless.

Bit 8 resets the JVS MCU. Since the reset pin is active-low, resetting is done
by writing 0, waiting at least 10 H8 clock cycles (the BIOS waits 2 hblanks)
and writing 1 again. Resetting the MCU will clear `JVSDRDY` but not `JVSIRDY`.
As the 056879 ASIC's output register is only 8 bits wide, bit 8 is actually
handled by a discrete flip-flop on the motherboard.

Unknown what reading from this port does.

#### `0x1f400004` (ASIC register 2): **Misc. inputs**

| Bits  | RW | Description                     |
| ----: | :- | :------------------------------ |
|   0-3 | R  | DIP switch status               |
|   4-5 | R  | Current JVS MCU status code     |
|   6-7 | R  | Current JVS MCU error code      |
|  8-15 | R  | `I0-I7` from security cartridge |

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
|     2 | R  | From `SDA` on security cartridge              |
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
order for bit 2 to be valid, `SDA` should be set as an input by clearing the
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

| Bits  | RW | Description                      |
| ----: | :- | :------------------------------- |
|   0-7 |    | Unused?                          |
|     8 | R  | Player 2 button 4 (JAMMA pin c)  |
|     9 | R  | Player 2 button 5 (JAMMA pin d)  |
|    10 |    | Unused?                          |
|    11 | R  | Player 2 button 6                |
| 12-15 |    | Unused?                          |

As buttons are active-low (wired between JAMMA pins and ground), all bits are 0
when a button is pressed and 1 otherwise.

The signals for buttons 4 and 5 are wired in parallel to both JAMMA and the
`EXT-IN` connector, while button 6 can only be connected through `EXT-IN` and is
usually unused.

### IDE registers

The IDE interface consists of a 16-bit parallel data bus with a 3-bit address
bus and two bank select pins (`/CS0` and `/CS1`), giving a total of sixteen
16-bit registers of which only nine are typically used. On the 573 the two IDE
banks are mapped to two separate memory regions at `0x1f480000` and `0x1f4c0000`
respectively. The IDE interrupt pin is routed into IRQ10 through the CPLD, while
all other signals on the 40-pin connector (DMA handshaking lines, status pins,
etc.) go unused.

Most 573 games, with the exception of those that run entirely from the internal
flash or PCMCIA cards, expect an ATAPI CD-ROM drive to be always connected and
configured as the primary (master) drive. Connecting an additional ATA hard
drive, CF card, IDE-to-SATA bridge or other device configured as secondary will
not interfere with the BIOS or games, thus homebrew games and apps can leverage
such a drive to store data separately from the currently installed game.

Note that IDE and ATAPI give slightly different meanings to each register. Refer
to the ATA and ATAPI specifications for more details.

#### `0x1f480000` (IDE bank 0, address 0): **Data**

| Bits | RW | Description                 |
| ---: | :- | :-------------------------- |
| 0-15 | RW | Current packet or data word |

Data transfers can also be performed through DMA. See below for details.

#### `0x1f480002` (IDE bank 0, address 1): **Error** / **Features**

When read:

| Bits | RW | Description (ATA)                 | Description (ATAPI)           |
| ---: | :- | :-------------------------------- | :---------------------------- |
|    0 | R  | _Unused_                          | Illegal length flag (`ILI`)   |
|    1 | R  | No media flag (`NM`)              | End of media flag (`EOM`)     |
|    2 | R  | Command aborted flag (`ABRT`)     | Command aborted flag (`ABRT`) |
|    3 | R  | Media change request flag (`MCR`) | _Unused_                      |
|    4 | R  | Address not found flag (`IDNF`)   | SCSI sense key bit 0          |
|    5 | R  | Media changed flag (`MC`)         | SCSI sense key bit 1          |
|    6 | R  | Uncorrectable error flag (`UNC`)  | SCSI sense key bit 2          |
|    7 | R  | DMA CRC error flag (`ICRC`)       | SCSI sense key bit 3          |
| 8-15 |    | _Unused_                          | _Unused_                      |

When written:

| Bits | RW | Description                             |
| ---: | :- | :-------------------------------------- |
|  0-7 | W  | Command-specific feature index or flags |
| 8-15 |    | _Unused_                                |

#### `0x1f480004` (IDE bank 0, address 2): **Sector count**

| Bits | RW | Description (ATA)     | Description (ATAPI) |
| ---: | :- | :-------------------- | :------------------ |
|  0-7 | W  | Transfer sector count | _Unused_            |
| 8-15 |    | _Unused_              | _Unused_            |

In ATA 48-bit LBA mode, bits 8-15 of the number of sectors to transfer must be
written to this register first, followed by bits 0-7.

In ATA CHS or 28-bit LBA mode, setting this register to 0 will cause 256 sectors
to be transferred.

#### `0x1f480006` (IDE bank 0, address 3): **Sector number**

| Bits | RW | Description (ATA)                | Description (ATAPI) |
| ---: | :- | :------------------------------- | :------------------ |
|  0-7 | W  | CHS sector index or LBA bits 0-7 | _Unused_            |
| 8-15 |    | _Unused_                         | _Unused_            |

In ATA 48-bit LBA mode, bits 24-31 of the target LBA must be written to this
register first, followed by bits 0-7.

#### `0x1f480008` (IDE bank 0, address 4): **Cylinder number low**

| Bits | RW | Description (ATA)                            | Description (ATAPI)          |
| ---: | :- | :------------------------------------------- | :--------------------------- |
|  0-7 | RW | CHS cylinder index bits 0-7 or LBA bits 8-15 | Transfer chunk size bits 0-7 |
| 8-15 |    | _Unused_                                     | _Unused_                     |

In ATA 48-bit LBA mode, bits 32-39 of the target LBA must be written to this
register first, followed by bits 8-15.

#### `0x1f48000a` (IDE bank 0, address 5): **Cylinder number high**

| Bits | RW | Description (ATA)                              | Description (ATAPI)           |
| ---: | :- | :--------------------------------------------- | :---------------------------- |
|  0-7 | RW | CHS cylinder index bits 8-15 or LBA bits 16-23 | Transfer chunk size bits 8-15 |
| 8-15 |    | _Unused_                                       | _Unused_                      |

In ATA 48-bit LBA mode, bits 40-47 of the target LBA must be written to this
register first, followed by bits 16-23.

#### `0x1f48000c` (IDE bank 0, address 6): **Head number** / **Drive select**

| Bits | RW | Description (ATA)                         | Description (ATAPI)                       |
| ---: | :- | :---------------------------------------- | :---------------------------------------- |
|  0-3 | W  | CHS head index or 28-bit LBA bits 24-27   | Reserved (should be 0)                    |
|    4 | RW | Drive select (0 = primary, 1 = secondary) | Drive select (0 = primary, 1 = secondary) |
|    5 |    | Reserved (should be 1?)                   | Reserved (should be 1?)                   |
|    6 | W  | Sector addressing mode (0 = CHS, 1 = LBA) | Reserved (should be 0)                    |
|    7 |    | Reserved (should be 1?)                   | Reserved (should be 1?)                   |
| 8-15 |    | _Unused_                                  | _Unused_                                  |

Bits 0-3 are not used in ATA 48-bit LBA mode.

#### `0x1f48000e` (IDE bank 0, address 7): **Status** / **Command**

When read:

| Bits | RW | Description (ATA)              | Description (ATAPI)              |
| ---: | :- | :----------------------------- | :------------------------------- |
|    0 | R  | Error flag (`ERR`)             | Error flag (`CHK`)               |
|    1 | R  | _Unused_                       | _Unused_                         |
|    2 | R  | _Unused_                       | _Unused_                         |
|    3 | R  | Data request flag (`DRQ`)      | Data request flag (`DRQ`)        |
|    4 | R  | Drive write error flag (`DWE`) | Overlapped service flag (`SERV`) |
|    5 | R  | Drive fault flag (`DF`)        | Drive fault flag (`DF`)          |
|    6 | R  | Drive ready flag (`DRDY`)      | Drive ready flag (`DRDY`)        |
|    7 | R  | Drive busy flag (`BSY`)        | Drive busy flag (`BSY`)          |
| 8-15 |    | _Unused_                       | _Unused_                         |

When written:

| Bits | RW | Description   |
| ---: | :- | :------------ |
|  0-7 | W  | Command index |
| 8-15 |    | _Unused_      |

In order to issue a command, the features, sector, cylinder and head registers
must be set up appropriately before writing the command ID to this register.
Refer to the ATA specification for a list of available commands and their
parameters.

`DRDY` is set by the drive when it is ready to execute an ATA command. Note that
ATAPI drives will *not* set `DRDY` initially, while still accepting ATAPI
commands, in order to prevent misdetection as a hard drive. Before sending any
command, a polling loop shall be used to wait until `BSY` is cleared.

`DRQ` is set when the drive is waiting for data to be read or written. Depending
on the drive and command, an interrupt may also be fired when `DRQ` goes high
after a command is issued. `ERR`/`CHK` is set if the last command executed
resulted in an error; in that case the error register will contain more
information about the cause of the error.

Reading from this register will acknowledge any pending drive interrupt and
deassert IRQ10. Note that, as with all PS1 interrupts, IRQ10 must additionally
be acknowledged at the interrupt controller side in order for it to fire again.

#### `0x1f4c000c` (IDE bank 1, address 6): **Alternate status**

| Bits | RW | Description (ATA)              | Description (ATAPI)              |
| ---: | :- | :----------------------------- | :------------------------------- |
|    0 | R  | Error flag (`ERR`)             | Error flag (`CHK`)               |
|    1 | R  | _Unused_                       | _Unused_                         |
|    2 | R  | _Unused_                       | _Unused_                         |
|    3 | R  | Data request flag (`DRQ`)      | Data request flag (`DRQ`)        |
|    4 | R  | Drive write error flag (`DWE`) | Overlapped service flag (`SERV`) |
|    5 | R  | Drive fault flag (`DF`)        | Drive fault flag (`DF`)          |
|    6 | R  | Drive ready flag (`DRDY`)      | Drive ready flag (`DRDY`)        |
|    7 | R  | Drive busy flag (`BSY`)        | Drive busy flag (`BSY`)          |
| 8-15 |    | _Unused_                       | _Unused_                         |

Read-only mirror of the status register at `0x1f48000e` that returns the same
flags, but does not acknowledge any pending IRQ when read.

### IDE DMA and quirks

DMA channel 5, normally reserved for the expansion port on a PS1, can be used to
transfer data to/from the IDE bus... with some caveats. The "correct" way to
connect an IDE drive to the PS1's DMA controller would to be to wire up `DMARQ`
and `/DMACK` from the drive directly to the respective pins on the CPU, allowing
the DMA controller to synchronize transfers to the drive's internal buffer in
chunked mode.

However, Konami being Konami, they did not do this on the 573. IDE drives will
instead interpret DMA reads or writes as a burst of regular ("PIO", as defined
in the ATA specification) CPU-issued reads or writes. As such, the drive shall
be configured for PIO data transfers rather than DMA using the "set features"
ATA command, and bits 9-10 in the `DMA5_CHCR` register shall be cleared to put
the channel in manual synchronization mode. The `DRQ` bit in the status register
must also be polled manually prior to starting a transfer, to ensure the drive
is ready for it.

### RTC registers

The RTC is an ST M48T58. This chip behaves like an 8 KB 8-bit static RAM, wired
to the lower 8 bits of the 16-bit data bus. It must thus be accessed by
performing 16-bit bus accesses and ignoring/masking out the upper 8 bits (as
with IDE control registers).

The first 8184 bytes are mapped to the `0x1f620000-0x1f623fef` region and are
simply battery-backed SRAM, which will retain its contents across power cycles
as long as the RTC's battery is not dead. The last 8 bytes are used as clock and
control registers.

The values of the clock registers are buffered: they are stored in intermediate
registers rather than being read from or written to the clock counters directly.
Bits 6 and 7 in the control register at `0x1f623ff0` are used to control
transfers between the registers and clock counters. All clock values are
returned in BCD format.

#### `0x1f623ff0` (M48T58 register `0x1ff8`): **Calibration** / **Control**

| Bits | RW | Buffered | Description                                             |
| ---: | :- | :------- | :------------------------------------------------------ |
|  0-4 | RW | Unknown  | Calibration offset (0-31), adjusts oscillator frequency |
|    5 | RW | Unknown  | Sign bit for calibration offset (1 = positive)          |
|    6 | W  | No       | Read mutex (1 = prevent buffered register updates)      |
|    7 | W  | No       | Write mutex and trigger                                 |
| 8-15 |    |          | _Unused_                                                |

The values of all buffered clock registers are updated automatically. Setting
bit 6 will disable this behavior while keeping the counters running, allowing
for the registers to be read reliably without the RTC updating them at the same
time. The bit shall be cleared after reading the registers.

Setting bit 7 will also halt buffered register updates, so that they can be
overwritten manually with new values. Clearing it afterwards will result in the
registers' values being copied back to the clock counters.

#### `0x1f623ff2` (M48T58 register `0x1ff9`): **Seconds** / **Stop**

| Bits | RW | Buffered | Description                                     |
| ---: | :- | :------- | :---------------------------------------------- |
|  0-3 | RW | Yes      | Second units (0-9)                              |
|  4-6 | RW | Yes      | Second tens (0-5)                               |
|    7 | RW | Unknown  | Stop flag (0 = clock paused, 1 = clock running) |
| 8-15 |    |          | _Unused_                                        |

#### `0x1f623ff4` (M48T58 register `0x1ffa`): **Minute**

| Bits | RW | Buffered | Description          |
| ---: | :- | :------- | :------------------- |
|  0-3 | RW | Yes      | Minute units (0-9)   |
|  4-6 | RW | Yes      | Minute tens (0-5)    |
|    7 |    |          | Reserved (must be 0) |
| 8-15 |    |          | _Unused_             |

#### `0x1f623ff6` (M48T58 register `0x1ffb`): **Hour**

| Bits | RW | Buffered | Description                          |
| ---: | :- | :------- | :----------------------------------- |
|  0-3 | RW | Yes      | Hour units (0-9, or 0-3 if tens = 2) |
|  4-5 | RW | Yes      | Hour tens (0-2)                      |
|  6-7 |    |          | Reserved (must be 0)                 |
| 8-15 |    |          | _Unused_                             |

Hours are always returned in 24-hour format, as there is no way to switch to
12-hour format.

#### `0x1f623ff8` (M48T58 register `0x1ffc`): **Day of week** / **Century**

| Bits | RW | Buffered | Description                                |
| ---: | :- | :------- | :----------------------------------------- |
|  0-2 | RW | Yes      | Day of week (1-7)                          |
|    3 |    |          | Reserved (must be 0)                       |
|    4 | RW | Yes      | Century flag                               |
|    5 | RW | Unknown  | Century flag toggling enable (1 = enabled) |
|    6 | RW | Unknown  | Enable 512 Hz clock signal output on pin 1 |
|    7 |    |          | Reserved (must be 0)                       |
| 8-15 |    |          | _Unused_                                   |

The day of week register is a free-running counter incremented alongside the day
counter. There is no logic for calculating the day of the week, so it must be
updated manually when setting the time. Konami games use 1 as Sunday, 2 as
Monday and so on.

Bit 4 is a single-bit "counter" that gets toggled each time the year counter
overflows. It can be frozen by clearing bit 5. Konami games do not use the
century flag, as they interpret any year counter value in 70-99 range as
1970-1999 and all other values as a year after 2000.

#### `0x1f623ffa` (M48T58 register `0x1ffd`): **Day of month** / **Battery state**

| Bits | RW | Buffered | Description                                          |
| ---: | :- | :------- | :--------------------------------------------------- |
|  0-3 | RW | Yes      | Day of month units (range depends on tens and month) |
|  4-5 | RW | Yes      | Day of month tens (range depends on month)           |
|    6 | R  | No       | Low battery flag (1 = battery voltage is below 2.5V) |
|    7 | RW | Unknown  | Battery monitoring enable (1 = enabled)              |
| 8-15 |    |          | _Unused_                                             |

Bit 6 is updated when the system is power cycled, if bit 7 has previously been
set.

#### `0x1f623ffc` (M48T58 register `0x1ffe`): **Month**

| Bits | RW | Buffered | Description                           |
| ---: | :- | :------- | :------------------------------------ |
|  0-3 | RW | Yes      | Month units (1-9, or 0-2 if tens = 1) |
|    4 | RW | Yes      | Month tens (0-1)                      |
|  5-7 |    |          | Reserved (must be 0)                  |
| 8-15 |    |          | _Unused_                              |

#### `0x1f623ffe` (M48T58 register `0x1fff`): **Year**

| Bits | RW | Buffered | Description      |
| ---: | :- | :------- | :--------------- |
|  0-3 | RW | Yes      | Year units (0-9) |
|  4-7 | RW | Yes      | Year tens (0-9)  |
| 8-15 |    |          | _Unused_         |

The year counter covers a full century, going from 00 to 99. On each overflow
the century flag in the day of week register is toggled.

### Other registers

These registers are implemented almost entirely using 74-series logic and the
XC9536 CPLD on the main board.

#### `0x1f500000`: **Bank switch** / **Security cartridge**

| Bits | RW | Description                                              |
| ---: | :- | :------------------------------------------------------- |
|  0-5 | W  | Bank number (0-47, see below)                            |
|    6 | W  | `SDA` direction on security cartridge (0 = input/high-z) |
|    7 |    | Unknown (goes into CPLD)                                 |
| 8-15 |    | _Unused_                                                 |

Bit 6 controls whether `SDA` on the security cartridge is an input or an output.
If set, `SDA` will output the same logic level as `D0`, otherwise the pin will
be floating. Bits 0-5 are used to switch the device mapped to the 4 MB
`0x1f000000-0x1f3fffff` region:

| Bank  | Mapped to                             |
| ----: | :------------------------------------ |
|     0 | Internal flash 1 (chips `31M`, `27M`) |
|     1 | Internal flash 2 (chips `31L`, `27L`) |
|     2 | Internal flash 3 (chips `31J`, `27J`) |
|     3 | Internal flash 4 (chips `31H`, `27H`) |
|  4-15 | _Unused_                              |
| 16-31 | PCMCIA card slot 1                    |
| 32-47 | PCMCIA card slot 2                    |
| 48-63 | _Unused_                              |

#### `0x1f520000`: **`JVSIRDY` clear**

| Bits | RW | Description |
| ---: | :- | :---------- |
| 0-15 |    | _Unused_    |

This register is a dummy write-only port that clears the `JVSIRDY` flag when any
value is written to it. The flag is set by the JVS MCU whenever a new data word
is available for reading from `0x1f40000a`.

#### `0x1f560000`: **IDE reset control**

| Bits | RW | Description                           |
| ---: | :- | :------------------------------------ |
|    0 | W  | Reset pin output (0 = pull reset low) |
| 1-15 |    | _Unused_                              |

Since the IDE reset pin is active-low, a reset is performed by writing 0 to this
register, then waiting a few milliseconds and writing 1 again. Note that the IDE
specification also defines a way to "soft-reset" devices (e.g. to abort
execution of a command) using the `SRST` bit in the device control register.

#### `0x1f5c0000`: **Watchdog clear**

| Bits | RW | Description |
| ---: | :- | :---------- |
| 0-15 |    | _Unused_    |

This register is a dummy write-only port that clears the watchdog timer embedded
in the Konami 058232 power-on reset and coin counter driver chip when any value
is written to it. The BIOS and games write to this port roughly once per frame.

If the watchdog is not cleared at least every 350-400 ms, it will pull the
system's reset line low for about 50 ms in order to force a reboot. The watchdog
can be disabled without affecting power-on reset by placing a jumper on `S86`
(see the pinouts section).

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

#### `0x1f6a0000`: **Security cartridge outputs**

| Bits | RW | Description                      |
| ---: | :- | :------------------------------- |
|  0-7 | W  | To `D0-D7` on security cartridge |
| 8-15 |    | _Unused_                         |

The lower 8 bits written to this register are latched on pins `D0-D7` of the
cartridge slot. See the security cartridge section for an explanation of what
each pin is wired to. Bit 0 additionally controls the `SDA` pin when configured
as an output through the bank switch register. Writing to this register will set
the `DRDY` flag, which can then be cleared by the cartridge.

Some games may rely on reads from this register returning the last value written
to it. This behavior is unconfirmed.

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

1. Reset the MCU through register `0x1f400000`, clear `JVSIRDY` by writing to
   `0x1f520000` then wait for the status and error codes in register
   `0x1f400004` to be set to 0 and 3 respectively.
2. Write the packet two bytes at a time to `0x1f680000`, waiting for `JVSDRDY`
   to go low before each write. Words are little endian, so for instance the
   first word of a packet with destination address `0x01` would be `0x01e0`. If
   the total length of the packet is odd, the last byte shall still be written
   as a word (with the upper byte zeroed out).
3. Wait for the status code to become 1. At this point the MCU will send the
   packet and wait for a response from a device on the bus.
4. Wait for the status code to become 0, signalling a valid response has been
   received and can be read out. A timeout should be implemented here, as the
   MCU will wait for a response indefinitely even if no device is present.
5. Read the packet, again two bytes at a time, from `0x1f40000a`, waiting for
   `JVSIRDY` to go high before each read and clearing it by writing to
   `0x1f520000` after each read. The status code will be set to 2 after the
   first word is read and back to 0 once no more data is available to read.

The MCU does not allow for non-JVS packets to be sent as it validates the sync
byte, checksum and uses the length field to determine packet length. Responses
cannot be received without sending a packet first either. The MCU will also
insert a 200 us minimum delay between the last byte of a received packet and the
first byte of the next packet.

## I/O boards

Having been used in all sorts of games, from DDR to fishing simulators, the
System 573 was designed to be expanded with game-specific hardware using I/O
boards mounted on top of the main board, custom security cartridges or both.
I/O boards have full access to the 16-bit system bus and are mapped to the
`0x1f640000-0x1f6400ff` region.

Several boards are known to exist although so far most of them haven't yet
been documented nor fully emulated in MAME.

- [Analog I/O board (`GX700-PWB(F)`)](#analog-io-board-gx700-pwbf)
- [Digital I/O board (`GX894-PWB(B)A`)](#digital-io-board-gx894-pwbba)
- [Alternate analog I/O board (`GX700-PWB(K)`)](#alternate-analog-io-board-gx700-pwbk)
- [Fishing controls board (`GE765-PWB(B)A`)](#fishing-controls-board-ge765-pwbba)
- [DDR Karaoke Mix I/O board (`GX921-PWB(B)`)](#ddr-karaoke-mix-io-board-gx921-pwbb)
- [Gun Mania I/O board (`PWB0000073070`, unconfirmed)](#gun-mania-io-board-pwb0000073070-unconfirmed)
- [Hypothetical debugging board](#hypothetical-debugging-board)

### Analog I/O board (`GX700-PWB(F)`)

The name is misleading as the board does not deal with any analog signals
whatsoever; the name was given retroactively to differentiate it from the
digital I/O board. It provides up to 28 optoisolated open-collector outputs
usually used to control cabinet lights, split across 4 banks:

- **Bank A** (wired to `CN33`): 8 outputs (A0-A7)
- **Bank B** (wired to `CN34`): 8 outputs (B0-B7)
- **Bank C** (wired to `CN35`): 8 outputs (C0-C7)
- **Bank D** (wired to `CN36`): 4 outputs (D0-D3)

See the game-specific information section for details on how lights are wired
up on each cabinet type.

#### `0x1f640080`: **Bank A**

| Bits | RW | Description              |
| ---: | :- | :----------------------- |
|    0 | W  | Output A1 (0 = grounded) |
|    1 | W  | Output A3 (0 = grounded) |
|    2 | W  | Output A5 (0 = grounded) |
|    3 | W  | Output A7 (0 = grounded) |
|    4 | W  | Output A6 (0 = grounded) |
|    5 | W  | Output A4 (0 = grounded) |
|    6 | W  | Output A2 (0 = grounded) |
|    7 | W  | Output A0 (0 = grounded) |
| 8-15 |    | _Unused_                 |

#### `0x1f640088`: **Bank B**

| Bits | RW | Description              |
| ---: | :- | :----------------------- |
|    0 | W  | Output B1 (0 = grounded) |
|    1 | W  | Output B3 (0 = grounded) |
|    2 | W  | Output B5 (0 = grounded) |
|    3 | W  | Output B7 (0 = grounded) |
|    4 | W  | Output B6 (0 = grounded) |
|    5 | W  | Output B4 (0 = grounded) |
|    6 | W  | Output B2 (0 = grounded) |
|    7 | W  | Output B0 (0 = grounded) |
| 8-15 |    | _Unused_                 |

#### `0x1f640090`: **Bank C**

| Bits | RW | Description              |
| ---: | :- | :----------------------- |
|    0 | W  | Output C1 (0 = grounded) |
|    1 | W  | Output C3 (0 = grounded) |
|    2 | W  | Output C5 (0 = grounded) |
|    3 | W  | Output C7 (0 = grounded) |
|    4 | W  | Output C6 (0 = grounded) |
|    5 | W  | Output C4 (0 = grounded) |
|    6 | W  | Output C2 (0 = grounded) |
|    7 | W  | Output C0 (0 = grounded) |
| 8-15 |    | _Unused_                 |

#### `0x1f640098`: **Bank D**

| Bits | RW | Description              |
| ---: | :- | :----------------------- |
|    0 | W  | Output D3 (0 = grounded) |
|    1 | W  | Output D2 (0 = grounded) |
|    2 | W  | Output D1 (0 = grounded) |
|    3 | W  | Output D0 (0 = grounded) |
| 4-15 |    | _Unused_                 |

### Digital I/O board (`GX894-PWB(B)A`)

This board was used by pretty much all Bemani games, besides earlier ones which
used CD audio and the analog I/O board. In addition to light control outputs,
this board features an FPGA and an MPEG decoder ASIC to play encrypted MP3
files. The FPGA has 24 MB of dedicated RAM into which the files are preloaded
on startup, then decrypted on the fly and fed to the decoder. The board also
features an ARCnet PHY and two RCA jacks for communication with other cabinets
and a 64-bit unique serial number, copied to the security cartridge during
installation in order to prevent operators from installing the same game on
multiple systems.

The vast majority of the registers provided by this board (including some but
not all light outputs) are handled by its FPGA, which requires a configuration
bitstream to be uploaded to it in order to work. Registers in the
`0x1f6400f0-0x1f6400ff` region are handled by a CPLD and are functional even if
no bitstream is loaded. There are three known versions of Konami's bitstream:

| SHA-1                                      | First used by                        |
| :----------------------------------------- | :----------------------------------- |
| `32d455a25eb26fe4e4b577cb0f0e3bebd0f82959` | Dance Dance Revolution Solo Bass Mix |
| `a53b8906de95c34b6e3f053bd7488c888bc904b6` | Dance Dance Revolution 3rdMIX        |
| `450b12627b7eacd3ea3f8b0b7a16589a13010c41` | Mambo a Go-Go                        |

Distributing these bitstreams would be problematic from a copyright standpoint,
thus **most of the digital I/O board's functionality is currently unusable by**
**homebrew software**. This might change in the future if a custom FPGA
bitstream is ever going to be developed; the custom bitstream would not only
skip decryption but also implement a custom set of registers (rather than the
ones described below), sidestepping the lack of documentation entirely.

#### `0x1f640080`: **Magic number** (impl. by bitstream)

| Bits | RW | Description             |
| ---: | :- | :---------------------- |
| 0-15 | R  | Magic number (`0x1234`) |

This register is read by Konami's digital I/O driver to make sure the bitstream
was properly loaded into the FPGA.

#### `0x1f6400e0`: **Bank A** (impl. by bitstream)

| Bits | RW | Description              |
| ---: | :- | :----------------------- |
| 0-11 |    | _Unused_                 |
|   12 | W  | Output A4 (0 = grounded) |
|   13 | W  | Output A5 (0 = grounded) |
|   14 | W  | Output A6 (0 = grounded) |
|   15 | W  | Output A7 (0 = grounded) |

#### `0x1f6400e2`: **Bank A** (impl. by bitstream)

| Bits | RW | Description              |
| ---: | :- | :----------------------- |
| 0-11 |    | _Unused_                 |
|   12 | W  | Output A0 (0 = grounded) |
|   13 | W  | Output A1 (0 = grounded) |
|   14 | W  | Output A2 (0 = grounded) |
|   15 | W  | Output A3 (0 = grounded) |

#### `0x1f6400e4`: **Bank B** (impl. by bitstream)

| Bits | RW | Description              |
| ---: | :- | :----------------------- |
| 0-11 |    | _Unused_                 |
|   12 | W  | Output B4 (0 = grounded) |
|   13 | W  | Output B5 (0 = grounded) |
|   14 | W  | Output B6 (0 = grounded) |
|   15 | W  | Output B7 (0 = grounded) |

#### `0x1f6400e6`: **Bank D** (impl. by bitstream)

| Bits | RW | Description              |
| ---: | :- | :----------------------- |
| 0-11 |    | _Unused_                 |
|   12 | W  | Output D0 (0 = grounded) |
|   13 | W  | Output D1 (0 = grounded) |
|   14 | W  | Output D2 (0 = grounded) |
|   15 | W  | Output D3 (0 = grounded) |

#### `0x1f6400ee`: **DS2401 ID chip** (impl. by bitstream)

#### `0x1f6400f0`: **Unknown**

Konami's code does not use this CPLD register.

#### `0x1f6400f2`: **Unknown**

Konami's code does not use this CPLD register.

#### `0x1f6400f4`: **Unknown (reset?)**

| Bits | RW | Description        |
| ---: | :- | :----------------- |
| 0-14 |    | _Unused_           |
|   15 | W  | Unknown (0 = low?) |

Probably controls the MAS3507D's reset pin. Bit 15 is cleared before uploading
the bitstream (and set again once the FPGA is initialized...?).

#### `0x1f6400f6`: **FPGA status and control**

When read:

| Bits | RW | Description       |
| ---: | :- | :---------------- |
| 0-11 |    | _Unused_          |
|   12 | R  | `/INIT` from FPGA |
|   13 | R  | `DONE` from FPGA  |
|   14 | R  | `/HDC` from FPGA  |
|   15 | R  | `LDC` from FPGA   |

**NOTE**: all registers in the `0x1f6400f0-0x1f6400ff` region seem to return
the same bits as this register when read, possibly due to incomplete address
decoding in the CPLD. Konami's code only ever reads from this register and
treats all other CPLD registers as write-only.

When written:

| Bits | RW | Description        |
| ---: | :- | :----------------- |
| 0-11 |    | _Unused_           |
|   12 | W  | Unknown 1          |
|   13 | W  | Unknown 2          |
|   14 | W  | Unknown 3          |
|   15 | W  | Unused? (always 1) |

This register is only written to 3 times when resetting the FPGA prior to
loading the bitstream. The values written are `0x8000` first, then `0xc000` and
finally `0xf000`. One of these bits probably controls the FPGA's `/PROGRAM`
input.

#### `0x1f6400f8`: **FPGA bitstream upload**

| Bits | RW | Description             |
| ---: | :- | :---------------------- |
| 0-14 |    | _Unused_                |
|   15 | W  | Bit to send to the FPGA |

Bits written to this register are sent to the FPGA's configuration interface
(`DIN` and `CCLK` pins, see the XCS40XL datasheet). There is no separate bit to
control the `CCLK` pin as clocking is handled automatically. The FPGA is wired
to boot in "slave serial" mode and wait for a bitstream to be loaded by the 573
through this port.

All known games load the bitstream from a file on the internal flash (usually
named `data/fpga/fpga_mp3.bin`), then bitbang its contents to this port LSB
first and monitor the FPGA status register. The bitstream is always 330696 bits
(41337 bytes) long as per the XCS40XL datasheet.

#### `0x1f6400fa`: **Bank C**

| Bits | RW | Description              |
| ---: | :- | :----------------------- |
| 0-11 |    | _Unused_                 |
|   12 | W  | Output C0 (0 = grounded) |
|   13 | W  | Output C1 (0 = grounded) |
|   14 | W  | Output C2 (0 = grounded) |
|   15 | W  | Output C3 (0 = grounded) |

#### `0x1f6400fc`: **Bank C**

| Bits | RW | Description              |
| ---: | :- | :----------------------- |
| 0-11 |    | _Unused_                 |
|   12 | W  | Output C4 (0 = grounded) |
|   13 | W  | Output C5 (0 = grounded) |
|   14 | W  | Output C6 (0 = grounded) |
|   15 | W  | Output C7 (0 = grounded) |

#### `0x1f6400fe`: **Bank B**

| Bits | RW | Description              |
| ---: | :- | :----------------------- |
| 0-11 |    | _Unused_                 |
|   12 | W  | Output B0 (0 = grounded) |
|   13 | W  | Output B1 (0 = grounded) |
|   14 | W  | Output B2 (0 = grounded) |
|   15 | W  | Output B3 (0 = grounded) |

### Alternate analog I/O board (`GX700-PWB(K)`)

This board is currently undocumented.

### Fishing controls board (`GE765-PWB(B)A`)

This board is currently undocumented.

### DDR Karaoke Mix I/O board (`GX921-PWB(B)`)

This board is currently undocumented.

### Gun Mania I/O board (`PWB0000073070`, unconfirmed)

This board is currently undocumented.

### Hypothetical debugging board

There is no proof whatsoever of this board having ever existed, but the BIOS
and some games attempt to access the hardware on it. In particular it seems to
contain at least a Fujitsu MB89371 UART and a 7-segment display, although these
might have actually been on two separate boards. The only game known to access
the serial ports is Great Bishi Bashi Champ.

The MB89371 does not have a publicly available datasheet.

#### `0x1f640000`: **UART data**

#### `0x1f640002`: **UART control**

#### `0x1f640004`: **UART baud rate select**

#### `0x1f640006`: **UART mode**

#### `0x1f640010`: **7-segment display**

| Bits | RW | Description                     |
| ---: | :- | :------------------------------ |
|    0 | W  | Second digit segment G (0 = on) |
|    1 | W  | Second digit segment F (0 = on) |
|    2 | W  | Second digit segment E (0 = on) |
|    3 | W  | Second digit segment D (0 = on) |
|    4 | W  | Second digit segment C (0 = on) |
|    5 | W  | Second digit segment B (0 = on) |
|    6 | W  | Second digit segment A (0 = on) |
|    7 |    | _Unused_                        |
|    8 | W  | First digit segment G (0 = on)  |
|    9 | W  | First digit segment F (0 = on)  |
|   10 | W  | First digit segment E (0 = on)  |
|   11 | W  | First digit segment D (0 = on)  |
|   12 | W  | First digit segment C (0 = on)  |
|   13 | W  | First digit segment B (0 = on)  |
|   14 | W  | First digit segment A (0 = on)  |
|   15 |    | _Unused_                        |

The BIOS shell shows "00" on this display (but contains a function to show any
hexadecimal value). Kick &amp; Kick shows an animated spinner, some other games
show error or status codes on it. This might have been meant to be a POST
display to be integrated into the 573 main board at some point.

## Security cartridges

There are several different security cartridges, most of which feature game
specific hardware and connectors to e.g. drive lights or interface to external
boxes. All of them fall into five categories, based on the actual security
chips they contain:

| Type   | Security EEPROM chip | ID chip  |
| :----- | :------------------- | :------- |
| **X**  | `X76F041`            |          |
| **XI** | `X76F041`            | `DS2401` |
| **Y**  | `X76F100`            |          |
| **YI** | `X76F100`            | `DS2401` |
| **ZI** | `PIC16C625` (`ZS01`) | `DS2401` |

**NOTE**: the existence of Y/YI cartridges has never been confirmed. All known
games that support Y/YI cartridges can also use X/XI cartridges interchangeably
and no actual X76F100-based cartridge was ever found in the wild.

The following cartridges are currently known to exist:

| Name (on PCB)   | Type | Used by                     | Additional I/O connectors                     | Additional hardware                                   |
| :-------------- | :--- | :-------------------------- | :-------------------------------------------- | :---------------------------------------------------- |
| `GX700-PWB(D)`  | X    | Most early games/installers |                                               | _Unpopulated (T)QFP footprint_                        |
| `GX896-PWB(A)A` | X    | Early DrumMania             | Network (5-pin), amp box (6-pin)              | RS-232 transceiver powered by isolated DC-DC module   |
| `GX894-PWB(D)`  | XI?  | Unknown                     |                                               | _Unpopulated SOIC footprints_                         |
| `GX700-PWB(J)`  | XI   | PunchMania                  | Analog inputs (12-pin), unknown (10-pin)      | SPI ADC chip for analog inputs                        |
| `GX883-PWB(D)`  | XI   | Early digital I/O games     | Network (5-pin), amp box (6-pin)              | RS-232 transceiver powered by isolated DC-DC module   |
| `GE949-PWB(D)A` | ZI   | Late digital I/O games      | Network (5-pin), amp box (6-pin)              | RS-232 transceiver powered by isolated DC-DC module   |
| `GE949-PWB(D)B` | ZI   | Late digital I/O games      | _Same as above but unpopulated_               | _Same as above but only security chips are populated_ |
| `PWB0000068819` | X    | Hyper BB Champ (2-player)   | 12V (4-pin), lights (16-pin)                  | Latch controlled light outputs                        |
| Unknown         | X    | Hyper BB Champ (3-player)   | 12V (4-pin), lights (16-pin), unknown (5-pin) | Latch controlled light outputs                        |
| `PWB0000088954` | XI   | Salary Man Champ            | 12V (4-pin), lights (16-pin)                  | Shift register controlled light outputs               |

The main security chip in all types other than ZI is actually just a simple
password-protected I2C EEPROM whose datasheet is readily available. ZI
cartridges use a microcontroller running custom firmware (which hasn't yet been
dumped) instead. XI, YI and ZI cartridges also feature a Dallas/Maxim DS2401
chip that communicates using the 1-wire protocol and, like all 1-wire devices,
provides a supposedly unique 64-bit serial number to identify the cartridge.
The DS2401 on ZI cartridges isn't directly accessible, it's instead read by the
ZS01.

PunchMania cartridges additionally contain an ADC0838 chip, which is identical
to the ADC0834 on the main board except with 8 channels instead of 4. The ADC's
inputs are broken out to a connector on the cartridge. Hyper Bishi Bashi Champ
and Salary Man Champ cartridges contain some 74 logic to control cabinet lights
and are fed 12V through a separate cable on the JAMMA harness.

Some games used an XI cartridge for running the installer and a ZI cartridge
for the actual game; MAME calls these games "XZI". MAME also declares some
games as "YYI" (YI cartridge for the installer and another YI cartridge to run
the game), however no YI cartridges are known to exist.

### Interface

The 573 motherboard has no dedicated SPI, I2C or 1-wire peripherals (other than
the unused PS1 controller SPI bus), so all communication with these chips is
bitbanged in software through a set of 6 UART pins, two 8-bit fixed direction
I/O ports plus a bidirectional pin:

| Name   | Dir | Common to all cartridge types            | XI/YI/ZI cartridges                     | Salary Man Champ cart  | Hyper BB Champ cart  | PunchMania cart     |
| :----- | :-- | :--------------------------------------- | :-------------------------------------- | :--------------------- | :------------------- | :------------------ |
| `TX`   | W   |                                          | Network connector TX1 (via RS-232 PHY)  |                        |                      |                     |
| `RX`   | R   |                                          | Network connector RX1 (via RS-232 PHY)  |                        |                      |                     |
| `/RTS` | W   | Serial port enable (shorted to CTS)      |                                         |                        |                      |                     |
| `/CTS` | R   | Serial port enable (shorted to RTS)      |                                         |                        |                      |                     |
| `/DTR` | W   | Not wired to the cartridge slot?         |                                         |                        |                      |                     |
| `/DSR` | R   | Cartridge presence detection (grounded)  |                                         |                        |                      |                     |
| `D0`   | W   | I2C SDA to security chip (through `SDA`) |                                         |                        | Player 3 light latch | SPI CS to ADC       |
| `D1`   | W   | I2C SCL to security chip                 |                                         |                        | Player 2 light latch | SPI SCK to ADC      |
| `D2`   | W   | I2C CS to security chip                  |                                         |                        |                      |                     |
| `D3`   | W   | Security chip reset                      |                                         |                        | Player 1 light latch |                     |
| `D4`   | W   |                                          | Drives 1-wire bus low when pulled high  |                        | Green button lights  |                     |
| `D5`   | W   |                                          |                                         | SCK to shift register  | Blue button lights   | SPI MOSI to ADC     |
| `D6`   | W   |                                          |                                         | Shift register reset   | Red button lights    |                     |
| `D7`   | W   |                                          | Network connector TX2? (via RS-232 PHY) | MOSI to shift register | Start button light   |                     |
| `I0`   | R   |                                          |                                         |                        |                      | SPI MISO from ADC   |
| `I1`   | R   |                                          |                                         |                        |                      | SAR status from ADC |
| `I2`   | R   |                                          |                                         |                        |                      |                     |
| `I3`   | R   |                                          |                                         |                        |                      |                     |
| `I4`   | R   |                                          | Network detect (unclear how this works) |                        |                      |                     |
| `I5`   | R   |                                          |                                         |                        |                      |                     |
| `I6`   | R   |                                          | 1-wire bus from/to DS2401 readout       |                        |                      |                     |
| `I7`   | R   |                                          | Network connector RX2? (via RS-232 PHY) |                        |                      |                     |
| `SDA`  | RW  | I2C SDA from/to security chip (see note) |                                         |                        |                      |                     |

`SDA` is a bidirectional pin that can be set by the 573 as an input (presumably
with a pullup resistor, as mandated by the I2C specification) or it can be set
to output the same logic level as `D0`.

#### Bus signalling

In addition to the signals above the cartridge slots carries two status lines
*unofficially* known as `ISIG` and `DSIG` and two inputs named `/IREQ` and
`/DACK`, probably meant for synchronization with cartridges that would actually
use the I/O ports as a parallel data bus rather than for bitbanging. No known
cartridge ever used these pins.

`DSIG` is set whenever the 573 writes to the output port, even if no bits have
actually changed. The cartridge can monitor this signal to know when to read a
byte from the port and then pull `/DACK` low to reset it. To send a byte to the
573 the cartridge can pulse `/IREQ`, which will cause `ISIG` to go high until
the 573 accesses the input port. The 573 can read the status of `ISIG` (as well
as `DSIG`) through the Konami ASIC and wait for it to be set before reading the
next byte.

Basically the cartridge I/O ports can be thought of as a single-byte FIFO, with
`DSIG` being the "TX buffer full" flag and `ISIG` the "RX buffer not empty"
flag.

#### Note about RTS/CTS

The CPU's SIO1 has hardware flow control and will not transmit anything if CTS
isn't asserted. To get around this all known cartridges wire CTS to RTS,
allowing it to be controlled in software. Cartridges that use the serial port
(i.e. the ones with the network port) simply have the pins shorted together,
while all other types break them out to a 2-pin jumper that is either
unpopulated or shorted out with a piece of wire.

It turns out that many games that don't use SIO1 for networking redirect their
debug log output to it (by calling the `AddSIO()` function provided by the Sony
SDK) if they detect that CTS and RTS are shorted on startup. Additionally on
later 573 revisions the SIO1 pins are broken out to a separate pin header
(`CN24`) and made accessible without needing any kind of adapter or probe
between the cartridge and the 573. Thus, was the normally unpopulated jumper
actually meant as a "debug switch" of sorts?

**NOTE**: I2C SDA from/to the security chip and the DS2401 1-wire bus are
*open-collector bidirectional lines*, which means they can be controlled by
both the 573 and the cassette. This is accomplished by having them pulled high
by a resistor, and using a transistor on each side to force them low. On the
573's side, the bits that control the transistors (`D0` and `D4`) are outputs
separate from the inputs used to read the lines (`SDA_I` and `1WIRE`), with
`D4` being inverted (i.e. set `D4` high to pull the 1-wire bus low).

Details on how to bitbang SPI, I2C and 1-wire are out of the scope of this
document, but plenty of documentation can be found online.

### ZS01 protocol

Konami's "ZS01" security chip, used in ZI cartridges, is a pre-programmed PIC16
microcontroller that mostly replicates the X76F100's functionality, allowing
the 573 to store up to 112 bytes of data protected by a 64-bit key. Unlike the
X76F100, however, the ZS01 communicates with the 573 using encrypted packets
and self-erases if too many attempts are made to tamper with the encryption.

A ZS01 transaction can be broken down into the following steps:

1. The 573 prepares a 12-byte buffer to be sent to the ZS01. The first 2 bytes
   represent the command (read or write) and the address to read from or write
   to, respectively. Data is always read or written in 8 byte blocks, with some
   blocks being reserved for "special" purposes such as changing keys or
   reading out the DS2401.
2. If the command is a write command the next 8 bytes are populated with the
   payload, in some cases encrypted with the ZS01's "data key" (different for
   each game). For read commands the 573 populates them with a random 64-bit
   nonce derived from RTC time, which will then be used by the ZS01 as a key to
   encrypt the response. This was probably meant as a way to prevent the replay
   attacks the X76F041 and X76F100 were vulnerable to.
3. A (non-standard) CRC16 of the 10 bytes generated so far is calculated and
   stored in the last 2 bytes of the buffer. All 12 bytes are then encrypted
   using a 64-bit "command key", which seems to be identical across all ZS01
   games.
4. The encrypted packet is sent to the ZS01. If the CRC16 is correct after
   decryption the ZS01 will reply with an I2C ACK, otherwise it will ignore the
   packet and decrement its remaining attempts counter.
5. The 573 proceeds to read 12 bytes from the ZS01 and decrypt them using the
   nonce it generated earlier. For write commands, the nonce provided in the
   last read command issued is reused by the ZS01.
6. The CRC16 of the response's first 10 bytes is calculated and compared
   against the one received in the last 2 bytes; if it matches, the response is
   considered valid. The first byte will be zero if the command was executed
   successfully by the ZS01. The second byte seems to be a "seed" of sorts used
   in the encryption algorithm. The remaining 8 bytes contain the requested
   payload for read commands.

## External modules

Over the 573's lifetime Konami introduced several add-ons that extended its
functionality. Unlike the I/O boards, these were external to the 573 unit and
not always mandatory. Not much is currently known about any of these.

### Relay board (`GN845-PWB(A)`)

A relatively simple lamp driver board, controlled by the optoisolated outputs
from the analog or digital I/O board. Commonly mounted in a metal box alongside
audio amplifier boards in most cabinets.

### DDR stage I/O board (`GN845-PWB(B)`)

Sits between the 573 and the sensors in each stage's arrow panels in Dance
Dance Revolution cabinets. It is based on a Xilinx XC9536 CPLD and allows the
573 to check the status of a specific pressure sensor (each panel has 4
sensors, one along each edge), in addition to ensuring DDR games can only be
played with an actual stage rather than just a joystick or buttons wired up to
the 573's JAMMA connector. Konami kept using the same board long after the 573
was discontinued, with the last game to use it being DDR X/X2 (PC based).

Each stage's board communicates with the 573 over 6 wires, of which 4 are the
up/down/left/right signals going to the JAMMA connector and 2 are light outputs
from the I/O board being misused as data and clock lines (see above). The board
initially asserts the right and up signals and waits for the 573 to issue an
initialization command by bitbanging it over the light outputs. Received bits
are acknowledged by the board by echoing them on the right signal and toggling
the up signal.

Once initialization is done the board goes into passthrough mode, asserting the
up/down/left/right signals whenever any of the respective arrow panels' sensors
are pressed. The 573 can issue another command to retrieve the status of each
sensor separately, which is then sent by the board in serialized form over the
right and up signals. DDR games only use this command to display sensor status
in the operator menu, no commands are sent to the board during actual gameplay.

The initialization protocol is currently unknown. The protocol used after
initialization is partially known (see links) but needs to be verified and
documented properly.

### PS1 controller and memory card adapter ("White I/O", `GE885-PWB(A)`)

A ridiculously overengineered JVS board providing support for accessing PS1
controllers and memory cards plugged into ports on the front of the cabinet.
This device is more or less self-contained as it contains a Toshiba TMPR3904
CPU, 512 KB of RAM and a boot ROM; however, the ROM is only a small bootloader
and the actual firmware is downloaded from the 573 into RAM. There are also
connectors for security dongles.

Memory card support became common in later Bemani games, allowing players to
save their scores and play custom charts. GuitarFreaks is the only game known
to support external controllers through this board.

### e-Amusement network unit (`PWB0000100991`)

Provides online connectivity to some Bemani games. It connects to the 573 via
PCMCIA, using a cable that ends in a dummy card. The board has a Toshiba
TMPR3927 CPU running at 133 MHz with 8 MB of RAM (far more powerful than the
573 itself!) as well as an internal 2.5-inch IDE drive and a PCI Ethernet chip.
Appears to run a proprietary kernel provided by Toshiba known as UDEOS.

### Multisession unit (`GXA25-PWB(A)`)

Probably the most overengineered piece of hardware Konami ever made: a fairly
large box containing yet another TMPR3927 CPU, an FPGA and 4 MPEG decoders. It
comes with 3 or 4 daughterboards installed, each of which hosts a stereo DAC
and has RCA jacks for audio input and output. The box also has its own CD drive
and power supply.

Its purpose is to enable "session mode" in later Bemani games, which allows for
the same song to be played on multiple games at the same time, with the box
playing the backing track and routing audio between the cabinets. It connects
to each cabinet's 573 using RS-232, through the "network" port on the security
cartridge.

### Master calendar

A JVS device used by Konami to program security cartridges at the factory. All
games that use a security cartridge search the JVS bus on startup and enter a
"factory test" mode if a device identifying as a master calendar is connected.
The game will then proceed to initialize the cartridge (and in some cases RTC
RAM) after an authentication handshake with the master calendar.

Even though nothing is known about the actual hardware Konami used, this device
has been successfully replicated using an Arduino (see the links section).

## Connectors

The front panel of a 573 looks approximately like this:

```
_________________________________________________ [3]
|   .-----------------------.      o------------o \
|   |     CD drive [1]      |      | Sub-panel  | |
|   |_______________________|      |    [2]     | |
|                                  o------------o |
| [_________JAMMA_________] * DIP JVS VGA RCA ... |
+------------[4]--------------[5]-[6]---[7]---[8]-+
```

1. **ATAPI CD drive**: a standard 5.25-inch unit held in place by a bracket
   mounted to the upper half of the case. Gray case variants usually came with
   a removable plate covering the drive cutout, while black/blue models have a
   front panel that hides the eject button behind a small hole.
2. **Sub-panels**: the gray variant of the case has a cutout for a plate to
   hold additional I/O connectors here. Different games have different plates,
   see the game-specific information section for details on which connectors
   are broken out for each game. There is another sub-panel cutout on the back
   of the 573 as well, used by some I/O boards to expose additional ports.
3. **Security cartridge**: cartridges are inserted into a slot on the 573's
   right side and locked in place by plastic tabs. Hotplugging cartridges while
   the system is powered on will result in *permanent* damage to the cartridge,
   the 573 or both due to ESD (this has been proven to happen).
4. **JAMMA**: a standard PCB edge connector used in arcade systems, carrying 5V
   and 12V power rails, analog RGB video, a mono speaker output (wired to the
   left channel of the built-in amp, see below) and button and coin inputs. The
   573 doesn't use the negative 5V rail provided by some JAMMA power supplies.
5. **DIP switches**: a set of four DIP switches for quick game configuration.
   The first three are used by some games (and can be freely used by homebrew)
   while the last one is reserved by the BIOS and used to select whether to
   boot from the CD or from the internal flash.
6. **JVS "USB" port**: this is not an actual USB port, but rather a serial bus
   which can be used to connect peripherals and external I/O boards. As the
   underlying protocol is RS-485, multiple devices can be daisy chained.
7. **"VGA" and RCA outputs**: these are also mandated by the JVS specification
   and are useful for hooking the system up for testing without needing a JAMMA
   "supergun" or similar adapter. Note that the VGA connector does not output
   standard VGA with separate h-sync and v-sync but 15 kHz (240p/480i) RGB with
   c-sync only. The signal levels are also higher than allowed by the VGA
   specification, since they are still meant to drive a JAMMA CRT monitor. An
   upscaler such as the GBS8200 (which has a VGA input that supports 15 kHz and
   c-sync) might be required to connect the 573 to an LCD monitor, although
   some monitors with VGA input are known to accept 15 kHz and may work with a
   direct connection.
8. **Speaker outputs**: the 573 has a built-in 15W amplifier, which can be used
   for either mono output (via the speaker pins on the JAMMA connector) or for
   stereo through this 4-pin connector. Bemani cabs do not use this output,
   relying on a more powerful external amp plugged into the RCA jacks instead.

## BIOS

The 573's BIOS is based on a slightly modified version of Sony's standard PS1
kernel, plus a custom shell executable that replaces the Sony one. The kernel
identifies itself as "Konami OS by T.H." and seems to have been used across all
Konami PS1-based arcade boards. The main difference from the PS1 kernel is that
most CD drive APIs and the ISO9660 filesystem driver have been removed. Other
than that there are no significant changes (e.g. controller and memory card
drivers are still present and functional, even though the controller port was
never used).

Contrary to popular belief, **the BIOS is NOT involved in copy protection**.
All security cartridge checks are implemented by the games themselves rather
than by the shell.

### Revisions

There seem to be at least three different versions of the BIOS:

| Chip marking | MAME ROM              | SHA-1                                      | Used by                       |
| :----------- | :-------------------- | :----------------------------------------- | :---------------------------- |
| `700A01`     | `700a01.22g`          | `e1284add4aaddd5337bd7f4e27614460d52b5b48` | Most games                    |
| `700A01`     | `700a01,gchgchmp.22g` | `9aab8c637dd2be84d79007e52f108abe92bf29dd` | Gachagachamp                  |
| `700A01`     |                       |                                            | Unknown (undumped, see below) |
| `700B01`     | `700b01.22g`          | `a2421d0a494892c0e71003c96995ce8f945064dd` | Dancing Stage EuroMIX 2       |

700A01 is the most common version. The only differences between the two known
variants of it are minor code improvements in the shell, with the kernel being
identical. There reportedly is a third variant that shipped on systems that
came with the H8/3644 microcontroller unpopulated (presumably it would not
check for it on startup), however no evidence of its existence has ever been
found. Old versions of MAME also used to reference a ROM named `700_a01.22g`,
but it seems to be the same as `700a01,gchgchmp.22g`.

700B01 shares the same kernel, but its shell is an entirely different beast. It
is split up into two separate executables, one in charge of running self-tests
and the other actually handling the boot sequence. The exact practical
differences other than the UI/font and some bugfixes in the tests are currently
unknown, but the 700B01 shell seems to be more advanced than the 700A01 one
from a cursory glance at the code.

### Boot sequence

Both the 700A01 and 700B01 shells are far simpler than their PS1 counterparts.
Once launched by the kernel, they start by configuring the bus (by writing
`0x24173f47` to the EXP1 configuration register) and proceed to run a hardware
self-test. The outcome of all tests is displayed on screen, with the following
chips being listed:

- `22G`: BIOS ROM (the shell and kernel are verified against a hardcoded
  checksum)
- `16H`, `16G`, `14H`, `14G`: main RAM (first row of chips)
- `12H`, `12G`, `9H`, `9G`: main RAM (second row of chips)
- `4L`, `4P`: VRAM (framebuffers are temporarily overwritten with pseudorandom
  noise, the self-test screen is redrawn afterwards)
- `10Q`: SPU RAM
- `18E`: H8/3644 microcontroller
- `CDR`: ATAPI CD drive

**NOTE**: the 700A01 shell does not actually test `4P`! It only tests the first
megabyte of VRAM and always reports `4P` as working due to a bug, which was
fixed in 700B01. A side effect of this is that the 700A01 BIOS will run and
pass all RAM and ROM checks in a regular PS1 emulator (as long as the emulator
is set up for 4 or 8 MB main RAM). The ROM checksum test fails on emulators
that patch the kernel on-the-fly to enable TTY output, such as DuckStation.

If any of these checks fails the shell locks up, shows a blinking "HARDWARE
ERROR... RESET" prompt and stops resetting the watchdog after a few seconds,
causing the 573 to reboot. Otherwise the shell attempts to load an executable
from four different sources, in the following order:

- PCMCIA flash card in slot 2 (if inserted and DIP switch 4 is on)
- PCMCIA flash card in slot 1 (if inserted and DIP switch 4 is on)
- Internal flash (if DIP switch 4 is on)
- `PSX.EXE` in the root directory of the CD

Like Sony's shell, the 573 shell's ISO9660 filesystem driver does not support
any extension, nor does it support non-8.3 file names. It also **only**
**allocates 2 KB for the path table**, so the number of directories on the disc
must be kept to a minimum to prevent the shell from crashing.

Unlike a regular PS1, the 573 ignores `SYSTEM.CNF` completely even if present
on the disc. Homebrew discs can take advantage of this behavior to provide
separate PS1 and 573 executables on the same disc. All official discs use Mode
1 sectors, unlike PS1 discs, but the 573 can also read Mode 2 Form 1 sectors
without issues since the BIOS only requests the 2048-byte data area from the
ATAPI drive.

If DIP switch 4 is on, the shell expects to find an executable at offset `0x24`
on either the built-in flash or one of the two flash cards, preceded by a CRC32
of it at offset `0x20`. The CRC32 is *not* calculated on the whole executable,
instead it is only calculated on bytes from the executable whose offsets are a
power of 2 (i.e. on bytes 0, 1, 2, 4, 8 and so on). The CRC variant used is the
Ethernet/"zlib" one, with polynomial `0x04c11db7`. The check is implemented in
the shell as follows:

```c
#define EXE_CRC32 ((const uint32_t *) 0x1f000020)
#define EXE_DATA  ((const uint8_t *)  0x1f000024)

const uint32_t crc32_table[256] = { /* ... */ };
uint32_t crc = 0xffffffff;

crc = (crc >> 8) ^ crc32_table[(crc & 0xff) ^ EXE_DATA[0]];
for (size_t i = 1; i < exe_size; i <<= 1)
    crc = (crc >> 8) ^ crc32_table[(crc & 0xff) ^ EXE_DATA[i]];

if ((~crc) == *EXE_CRC32)
    load_exe((void *) EXE_DATA);
```

DIP switch 4 can be turned off to force the shell to ignore any executables on
the flash. This is used when upgrading cabinets to a new game to run the
installer from the new CD, rather than the currently installed game from flash.

### Accidental DVD support

Even though neither the 573 nor its BIOS were designed with support for DVDs in
mind, it is possible to boot from a DVD (assuming the installed drive is a DVD
drive in the first place) thanks to the fact that the ATAPI command used by the
BIOS to read data sectors also works on DVDs. In order for this to work, the
DVD must be formatted as ISO9660 (not UDF) with no extensions, as if it were a
CD, and must of course contain a `PSX.EXE` file in the root directory.

This accidental capability was greatly abused by bootleg "superdiscs" (nothing
to do with the SNES CD attachment!) that bundled multiple games on a single
DVD and allowed the user to pick a game to install. Each game on these discs
was patched to load its files from a subdirectory rather than the root of the
disc, basically "namespacing" the assets. Obviously games that make use of CD
audio can't be put on a DVD, so superdiscs were limited to games that used the
digital I/O board for MP3 playback.

Homebrew games willing to sacrifice PS1 compatibility and CD-DA support can be
distributed on a DVD. In that case the game's disc image shall be an .iso file
with 2048-byte sectors, rather than the typical .bin and .cue pair for PS1 or
PS1/573 hybrid games with Mode 2 sectors.

### BIOS "modchips"

It is not uncommon to find "modchipped" 573 units out in the wild. These
"modchips" (sometimes more properly called "mod boards") were bundled back in
the day alongside bootleg game discs and are nothing more than a simple PCB
that plugs in place of the BIOS ROM (which happens to be the only chip that
comes socketed from the factory) on the motherboard. They were apparently
required to "skip the anti-piracy checks in the BIOS" and allow the 573 to read
burned discs.

Of course, since the 573 BIOS does no copy protection checks whatsoever, these
claims were misleading. The actual purpose of these boards was not to tamper
with the BIOS, but rather to piggyback on the system bus and provide a few
rudimentary challenge-response authentication registers as a way for bootleg
executables to verify that they were running on a modded 573. In other words
*the "modchips" were actually the bootleggers' implementation of a security*
*cartridge*, meant to stop people from simply burning copies of bootleg discs
and force them to buy the discs with their respective "modchips" from whoever
produced them instead. Oh the irony.

Although the added circuitry will not create any issues with official or
homebrew games, most of these boards also ship with a modified version of the
700A01 BIOS altered to load a differently named executable from the disc rather
than `PSX.EXE`. The following names have been found so far (more might exist):

- `QSY.DXD`
- `SSW.BXF`
- `TSV.AXG`
- `GSE.NXX`
- `NSE.GXX`

Homebrew games should thus place multiple copies of the boot executable on the
disc to improve compatibility with "modchipped" systems. An interesting side
note is that, for any of these names, summing the ASCII codes of each character
will always yield the same result. Presumably bootleggers were unable to find
the code in charge of BIOS ROM checksum validation and found it easier to just
turn the string into random nonsense whose checksum collided with the original
one...

## Game-specific information

### Sub-panels

Black/blue case models, most commonly used in Fisherman's Bait and in a few
non-Bemani games that do not require I/O boards, have no sub-panel cutouts and
instead expose some of the built-in ports through a handful of connectors:

- **Power**: a hefty 2x4 Molex connector for powering the board, wired to the
  motherboard's power connector.
- **Option 1**: DE9 connector providing 4 analog inputs, wired to the
  `ANALOG` connector on the motherboard. These inputs seem to go directly
  into the 573's ADC chip *with no protection whatsoever*.
- **Option 2**: DE9 connector providing 6 button (digital) inputs, wired to the
  `EXT-IN` connector on the motherboard. 4 of these inputs are also broken out
  to the JAMMA connector (see the pinouts section for details).
- **Reel connector** (back side): 3x3 Molex connector wired to the fishing
  controls I/O board. The cutout seems to actually be only present on systems
  that came with Fisherman's Bait.

Gray case models that came with Dance Dance Revolution, regardless of whether
they contain an analog or digital I/O board, have 4 connectors mounted to the
front sub-panel which break out the board's light outputs:

- **1P** (10-pin white, only 7 pins used): connects to the left stage and
  controls arrow lights. Two of the signals are additionally misused as a
  bitbanged SPI-like bus for communication with the pad.
- **2P** (10-pin orange, only 7 pins used): same as above for the right stage.
- Unlabeled (10-pin red, only 7 pins used): connects to cabinet button and
  marquee lights.
- Unlabeled (6-pin white, only 2 pins used): goes to the inverter that drives
  the neon rings around the speakers.

There are several other sub-panel variants which are currently undocumented.

### DDR light mapping

Dance Dance Revolution cabinets (standard 2-player ones, not Solo) have lights
wired up to the analog or digital I/O board as follows:

| Output | Connected to                |
| -----: | :-------------------------- |
|     A0 | Player 1 up arrow           |
|     A1 | Player 1 down arrow         |
|     A2 | Player 1 left arrow         |
|     A3 | Player 1 right arrow        |
|     A4 | Data to player 1 stage I/O  |
|     A5 | Clock to player 1 stage I/O |
|  A6-A7 | _Unused_                    |
|     B0 | Player 2 up arrow           |
|     B1 | Player 2 down arrow         |
|     B2 | Player 2 left arrow         |
|     B3 | Player 2 right arrow        |
|     B4 | Data to player 2 stage I/O  |
|     B5 | Clock to player 2 stage I/O |
|  B6-B7 | _Unused_                    |
|  C0-C1 | _Unused_                    |
|     C2 | Player 1 buttons            |
|     C3 | Player 2 buttons            |
|     C4 | Bottom right marquee light  |
|     C5 | Top right marquee light     |
|     C6 | Bottom left marquee light   |
|     C7 | Top left marquee light      |
|     D0 | Speaker neon                |
|  D1-D3 | _Unused_                    |

Light outputs A4, A5, B4 and B5 do not actually control any lamps, but are used
to communicate with each stage's I/O board. See the external modules section
for more details.

### DDR Solo input and light mapping

Dance Dance Revolution Solo cabinets, unlike 2-player cabinets, do not use a
stage I/O board to multiplex the sensors as each arrow panel only has 2 sensors
(rather than 4). Each sensor is instead wired directly to the JAMMA connector,
making use of most of the available inputs.

| JAMMA input       | Connected to        |
| :---------------- | :------------------ |
| Player 1 left     | Left sensor A       |
| Player 1 right    | Right sensor A      |
| Player 1 up       | Up sensor A         |
| Player 1 down     | Down sensor A       |
| Player 1 button 1 | Up-left sensor B    |
| Player 1 button 2 | Left sensor B       |
| Player 1 button 3 | Down sensor B       |
| Player 1 button 4 | _Unused_            |
| Player 1 button 5 | Left button         |
| Player 1 start    | Start button        |
| Player 2 left     | Up-left sensor A    |
| Player 2 right    | Up-right sensor A   |
| Player 2 up       | _Unused_            |
| Player 2 down     | _Unused_            |
| Player 2 button 1 | Up sensor B         |
| Player 2 button 2 | Right sensor B      |
| Player 2 button 3 | Up-right sensor B   |
| Player 2 button 4 | _Unused_            |
| Player 2 button 5 | Right button        |
| Player 2 start    | _Unused_ (shorted?) |

The light mapping is currently unknown. Solo cabinets have less lights compared
to their 2-player counterparts (e.g. arrow panel lamps are missing).

### DrumMania light mapping

First-generation DrumMania cabinets (*unofficially* called "1st Mix") have
lights wired up to the I/O board as follows:

| Output | Connected to  |
| -----: | :------------ |
|  A0-A7 | _Unused_      |
|  B0-B7 | _Unused_      |
|     C0 | Hi-hat        |
|     C1 | Snare         |
|     C2 | High tom      |
|     C3 | Low tom       |
|     C4 | Cymbal        |
|     C5 | _Unused_      |
|     C6 | Start button  |
|     C7 | Select button |
|     D0 | Spotlight     |
|     D1 | Top neon      |
|     D2 | _Unused_      |
|     D3 | Bottom neon   |

The wiring was changed in 2nd Mix and later cabinets, which use the following
mapping instead:

| Output | Connected to  |
| -----: | :------------ |
|     A0 | Hi-hat        |
|     A1 | Snare         |
|     A2 | High tom      |
|     A3 | Low tom       |
|  A4-A7 | _Unused_      |
|     B0 | Spotlight     |
|     B1 | Bottom neon   |
|     B2 | Top neon      |
|     B3 | _Unused_      |
|     B4 | Cymbal        |
|     B5 | _Unused_      |
|     B6 | Start button  |
|     B7 | Select button |
|  C0-C7 | _Unused_      |
|  D0-D3 | _Unused_      |

## Misc. notes

### Homebrew guidelines

It is relatively easy to develop homebrew games that can run on both a System
573 and a regular PlayStation 1, or to port existing PS1 homebrew to the 573.
Nevertheless, there are some significant differences between the two systems
and a game meant to run on both shall avoid using any feature that is only
available on one. "Hybrid" PS1/573 games shall adhere to the following
guidelines:

- **Do not use the extra RAM.** With the exception of development kits and
  modified units, consoles always have 2 MB of main RAM and 1 MB of VRAM. The
  additional RAM on the 573 might still be useful for 573-specific purposes
  such as FAT filesystem handling if an IDE hard drive is used.
- **Do not use XA-ADPCM.** XA is not supported by any ATAPI drive. CD-DA is
  supported by both the PS1 CD drive and ATAPI drives, however it will not work
  out-of-the-box on a 573 fitted with a digital I/O board as the 4-pin CD audio
  cable will not be plugged into the drive. Homebrew games that use CD-DA
  should display a splash screen showing how to unplug the cable from the I/O
  board and plug it into the drive (which is a quick reversible modification).
  SPU audio streaming can replace XA and will work on both platforms.
- **Have separate executables for PS1 and 573.** Since the PS1 BIOS parses
  `SYSTEM.CNF` while the 573 BIOS ignores it, a disc can have two different
  executables, one named `PSX.EXE` (which will be launched on a 573) and the
  other (which will run on a PS1) referenced by `SYSTEM.CNF`. This makes it
  easier to have two separate builds of the game rather than having to detect
  system type at runtime.
- **Do not rely on the RTC.** Most 573 boards have a dead RTC battery by now.
  As the battery is sealed inside the RTC it is basically impossible to replace
  without replacing the entire chip, which is something not all 573 owners can
  do. RTC RAM is additionally used by some games to store security-related data
  and shall not be used for saving.
- **Implement an operator/settings menu.** Among other things, the menu should
  allow the user to adjust the SPU's master volume, enable or disable the 573's
  built-in amplifier (which has no physical volume controls), test cabinet
  lights and eject the CD (as some cases hide the drive's eject button behind a
  small hole or make it difficult to access otherwise).

### Missing support for PAL mode

The 573 only supports 60 Hz mode (i.e. "NTSC", even though the video DAC has no
composite or S-video output so no color modulation is involved). Attempting to
switch the GPU into 50 Hz PAL mode using the `GP1(0x08)` command will result in
a crash, as only the NTSC clock input pin is wired up.

Support for 50 Hz can be added back by shorting pins 192 and 196 on the GPU
(which will give "PAL-on-NTSC" timings) or by connecting pin 192 to an external
oscillator tuned to generate a PAL clock. See the timings section of the GPU
page for more details.

### Known working replacement drives

This is an incomplete list of drives that are known to work (or to be
incompatible) with Konami's ATAPI driver, used by both the BIOS and games. Note
that CD-DA support is problematic due to the way Konami's code reads the disc's
table of contents. Thus, very few drives are confirmed to work with games that
use CD-DA (i.e. pretty much all games that don't use the digital I/O board).

| Manufacturer | Model          | Type | BIOS    | CD-DA   | Notes                        |
| :----------- | :------------- | :--- | :------ | :------ | :--------------------------- |
| ASUSTeK      | DVD-E616P3     | DVD  | **Yes** | Unknown |                              |
| Compaq       | CRN-8241B      | CD   | **Yes** | **Yes** | Laptop drive                 |
| Creative     | CD4832E        | CD   | **Yes** | No      |                              |
| Hitachi      | CDR-7930       | CD   | **Yes** | No      |                              |
| LG           | GCE-8160B      | CD   | **Yes** | No      |                              |
| LG           | GCR-8523B      | CD   | **Yes** | Unknown |                              |
| LG           | GDR-8163B      | DVD  | **Yes** | **Yes** |                              |
| LG           | GDR-8164B      | DVD  | **Yes** | **Yes** |                              |
| LG           | GH22LP20       | DVD  | **Yes** | Unknown |                              |
| LG           | GH22NP20       | DVD  | **Yes** | Unknown |                              |
| LG           | GSA-4165B      | DVD  | No      |         |                              |
| Lite-On      | LH-18A1H       | DVD  | **Yes** | **Yes** |                              |
| Lite-On      | LTD-163        | DVD  | **Yes** | Unknown |                              |
| Lite-On      | LTD-165H       | DVD  | **Yes** | Unknown |                              |
| Lite-On      | LTR-40125S     | CD   | **Yes** | Unknown |                              |
| Lite-On      | XJ-HD166S      | DVD  | **Yes** | Unknown |                              |
| Matsushita   | CR-583         | CD   | **Yes** | **Yes** | Stock drive                  |
| Matsushita   | CR-587         | CD   | **Yes** | **Yes** | Stock drive, can't read CD-R |
| Matsushita   | CR-589B        | CD   | **Yes** | **Yes** | Stock drive                  |
| Matsushita   | SR8589B        | DVD  | **Yes** | Unknown |                              |
| Mitsumi      | CRMC-FX4830T   | CD   | **Yes** | Unknown |                              |
| NEC          | CDR-1900A      | CD   | **Yes** | Unknown |                              |
| NEC          | ND-2510A       | DVD  | No      |         |                              |
| Panasonic    | CR-594C        | CD   | **Yes** | Unknown |                              |
| Panasonic    | UJDA770        | CD?  | **Yes** | Unknown | Laptop drive                 |
| Sony         | DRU-510A       | DVD  | **Yes** | Unknown |                              |
| Sony         | DRU-810A       | DVD  | **Yes** | Unknown |                              |
| TDK          | AI-CDRW241040B | CD   | **Yes** | Unknown |                              |
| TDK          | AI-481648B     | CD   | **Yes** | Unknown |                              |
| TEAC         | CD-W552E       | CD   | **Yes** | Unknown |                              |
| Toshiba      | XM-5702B       | CD   | **Yes** | Unknown |                              |
| Toshiba      | XM-6102B       | CD   | **Yes** | No      | Has issues with homebrew     |
| Toshiba      | XM-7002B       | CD   | **Yes** | Unknown | Stock drive, laptop drive    |

**NOTE**: Konami shipped some units with a Toshiba XM-7002B laptop drive and a
passive adapter board (`GX874-PWB(B)`) to break out the drive's signals to a
regular 40-pin IDE connector, possibly due to newer full size drives at the
time being incompatible with the ATAPI driver. Laptop drives seem to have been
first used by Konami in the multisession unit.

## Pinouts

### Analog input port (`ANALOG`, `CN3`)

The inputs are wired directly to the 573's built-in ADC, so they can only
accept voltages in 0-5V range. This connector is mostly useful for wiring up
potentiometers and similar resistive analog controls.

| Pin | Name  | Dir |
| --: | :---- | :-- |
|   1 | `5V`  |     |
|   2 | `5V`  |     |
|   3 | `5V`  |     |
|   4 | `5V`  |     |
|   5 | `CH0` | R   |
|   6 | `GND` |     |
|   7 | `CH1` | R   |
|   8 | `CH2` | R   |
|   9 | `CH3` | R   |
|  10 | `GND` |     |

### Digital output port (`EXT-OUT`, `CN4`)

| Pin | Name   | Dir |
| --: | :----- | :-- |
|   1 | `5V`   |     |
|   2 | `5V`   |     |
|   3 | `OUT7` | W   |
|   4 | `OUT6` | W   |
|   5 | `OUT5` | W   |
|   6 | `OUT4` | W   |
|   7 | `OUT3` | W   |
|   8 | `OUT2` | W   |
|   9 | `OUT1` | W   |
|  10 | `OUT0` | W   |
|  11 | `GND`  |     |
|  12 | `GND`  |     |

### Digital input port (`EXT-IN`, `CN5`)

Unlike `EXT-OUT`, this port is not a separate input port. It piggybacks on the
JAMMA button inputs instead, exposing the button 4 and 5 pins for both players
as well as a sixth button input which is not available on the JAMMA connector.

| Pin | Name    | Dir | JAMMA |
| --: | :------ | :-- | ----: |
|   1 | `5V`    |     |       |
|   2 | `5V`    |     |       |
|   3 | `P1_B4` | R   |    25 |
|   4 | `P1_B5` | R   |    26 |
|   5 | `P1_B6` | R   |     - |
|   6 | `GND`   |     |       |
|   7 | `P2_B4` | R   |     c |
|   8 | `P2_B5` | R   |     d |
|   9 | `P2_B6` | R   |     - |
|  10 | `GND`   |     |       |

### Main I/O board connector (`CN10`)

Used by all known I/O boards. Some signals seem to be duplicated across more
than one pin for whatever reason. Note that the address and data bus are 3.3V,
while all other signals are 5V as they go through the CPLD.

| Pin | Name     | Dir | Pin | Name     | Dir |
| --: | :------- | :-- | --: | :------- | :-- |
|  A1 | `5V`     |     |  B1 | `5V`     |     |
|  A2 | `5V`     |     |  B2 | `5V`     |     |
|  A3 | `5V`     |     |  B3 | `5V`     |     |
|  A4 | `5V`     |     |  B4 | `5V`     |     |
|  A5 | `5V`     |     |  B5 | `5V`     |     |
|  A6 | `/RD`    | W   |  B6 | `/WR0`   | W   |
|  A7 | `/WR1`   | W   |  B7 | `GND`    |     |
|  A8 | `GND`    |     |  B8 | `SYSCLK` | W   |
|  A9 | `GND`    |     |  B9 | `GND`    |     |
| A10 | `/RESET` | W   | B10 | `/RESET` | W   |
| A11 | `GND`    |     | B11 | `GND`    |     |
| A12 | `/EXP1`  | W   | B12 | `DMARQ5` | R   |
| A13 | `GND`    |     | B13 | `GND`    |     |
| A14 | `DMARQ5` | R   | B14 | `/EXP1`  | W   |
| A15 | `/EXP2`  | W   | B15 | `NC`     |     |
| A16 | `/IRQ10` | R   | B16 | `/IRQ10` | R   |
| A17 | `A22`    | W   | B17 | `A23`    | W   |
| A18 | `A20`    | W   | B18 | `A21`    | W   |
| A19 | `A14`    | W   | B19 | `A15`    | W   |
| A20 | `A12`    | W   | B20 | `A13`    | W   |
| A21 | `A6`     | W   | B21 | `A7`     | W   |
| A22 | `A4`     | W   | B22 | `A5`     | W   |
| A23 | `A2`     | W   | B23 | `A3`     | W   |
| A24 | `A0`     | W   | B24 | `A1`     | W   |
| A25 | `D14`    | RW  | B25 | `D15`    | RW  |
| A26 | `D12`    | RW  | B26 | `D13`    | RW  |
| A27 | `D10`    | RW  | B27 | `D11`    | RW  |
| A28 | `D8`     | RW  | B28 | `D9`     | RW  |
| A29 | `D6`     | RW  | B29 | `D7`     | RW  |
| A30 | `D4`     | RW  | B30 | `D5`     | RW  |
| A31 | `D2`     | RW  | B31 | `D3`     | RW  |
| A32 | `D0`     | RW  | B32 | `D1`     | RW  |
| A33 | `GND`    |     | B33 | `GND`    |     |
| A34 | `GND`    |     | B34 | `GND`    |     |
| A35 | `GND`    |     | B35 | `GND`    |     |
| A36 | `3.3V`   |     | B36 | `3.3V`   |     |
| A37 | `3.3V`   |     | B37 | `3.3V`   |     |
| A38 | `3.3V`   |     | B38 | `3.3V`   |     |
| A39 | `3.3V`   |     | B39 | `3.3V`   |     |
| A40 | `3.3V`   |     | B40 | `3.3V`   |     |

### Secondary I/O board connector (`CN21`)

This connector exposes the address lines not wired to `CN10` as well as the SPI
bus pins normally used for controllers and memory cards, which go unused on the
573 as no known I/O board ever used this connector. All signals are 3.3V.

| Pin | Name   | Dir | Pin | Name    | Dir |
| --: | :----- | :-- | --: | :------ | :-- |
|  A1 | `A8`   | W   |  B1 | `A9`    | W   |
|  A2 | `A10`  | W   |  B2 | `A11`   | W   |
|  A3 | `A16`  | W   |  B3 | `A17`   | W   |
|  A4 | `A18`  | W   |  B4 | `A19`   | W   |
|  A5 | `GND`  |     |  B5 | `?`     |     |
|  A6 | `GND`  |     |  B6 | `?`     |     |
|  A7 | `GND`  |     |  B7 | `GND`   |     |
|  A8 | `GND`  |     |  B8 | `DOTCK` | W   |
|  A9 | `GND`  |     |  B9 | `GND`   |     |
| A10 | `GND`  |     | B10 | `/ACK`  | R   |
| A11 | `GND`  |     | B11 | `/JOY2` | W   |
| A12 | `GND`  |     | B12 | `/JOY1` | W   |
| A13 | `GND`  |     | B13 | `MISO`  | R   |
| A14 | `GND`  |     | B14 | `MOSI`  | W   |
| A15 | `GND`  |     | B15 | `SCK`   | W   |

### Security cartridge slot (`CN14`)

All signals are 5V as they go through level shifters.

| Pin | Name     | Dir | Notes                           | Pin | Name    | Dir | Notes                                 |
| --: | :------- | :-- | :------------------------------ | --: | :------ | :-- | :------------------------------------ |
|   1 | `GND`    |     |                                 |  23 | `GND`   |     |                                       |
|   2 | `GND`    |     |                                 |  24 | `GND`   |     |                                       |
|   3 | `/DSR`   | R   | Usually shorted to ground       |  25 | `EXCLK` | W   | 7.3728 MHz clock (also goes into H8)  |
|   4 | `NC`     |     | May have been DTR at some point |  26 | `GND`   |     |                                       |
|   5 | `TX`     | W   |                                 |  27 | `DSIG`  | W   | Goes high when 573 updates `D0-D7`    |
|   6 | `RX`     | R   |                                 |  28 | `SDA`   | RW  | Can be tristated and read as an input |
|   7 | `/RESET` | RW  | System reset (from watchdog)    |  29 | `/IREQ` | R   | Sets `ISIG` when pulsed low           |
|   8 | `GND`    |     |                                 |  30 | `/DACK` | R   | Clears `DSIG` when pulsed low         |
|   9 | `GND`    |     |                                 |  31 | `ISIG`  | W   | Goes low when 573 reads `I0-I7`       |
|  10 | -        |     | Key (missing pin)               |  32 | -       |     | Key (missing pin)                     |
|  11 | `?`      |     | Not connected?                  |  33 | `I7`    | R   |                                       |
|  12 | `?`      |     | Not connected?                  |  34 | `I6`    | R   |                                       |
|  13 | `D7`     | W   |                                 |  35 | `I5`    | R   |                                       |
|  14 | `D6`     | W   |                                 |  36 | `I4`    | R   |                                       |
|  15 | `D5`     | W   |                                 |  37 | `I3`    | R   |                                       |
|  16 | `D4`     | W   |                                 |  38 | `I2`    | R   |                                       |
|  17 | `D3`     | W   |                                 |  39 | `I1`    | R   |                                       |
|  18 | `D2`     | W   |                                 |  40 | `I0`    | R   |                                       |
|  19 | `D1`     | W   |                                 |  41 | `5V`    |     |                                       |
|  20 | `D0`     | W   |                                 |  42 | `5V`    |     |                                       |
|  21 | `5V`     |     |                                 |  43 | `/RTS`  | W   | Shorted to `/CTS` on some cartridges  |
|  22 | `5V`     |     |                                 |  44 | `/CTS`  | R   | Shorted to `/RTS` on some cartridges  |

### Serial port (`CN24`, unpopulated)

Only present on later revisions of the main board. It exposes the exact same
serial port signals as the security cartridge slot.

| Pin | Name   | Dir | Cart |
| --: | :----- | :-- | ---: |
|   1 | `TX`   | W   |    5 |
|   2 | `RX`   | R   |    6 |
|   3 | `GND`  |     |      |
|   4 | `GND`  |     |      |
|   5 | `/RTS` | W   |   43 |
|   6 | `/CTS` | R   |   44 |

### I2S digital audio output (`CN19`, unpopulated)

Pin 4 outputs a 16.9344 MHz master clock (system clock divided by 2, or
sampling rate multiplied by 384).

| Pin | Name    | Dir |
| --: | :------ | :-- |
|   1 | `BCLK`  | W   |
|   2 | `SDOUT` | W   |
|   3 | `GND`   |     |
|   4 | `MCLK`  | W   |
|   5 | `LRCK`  | W   |

### Watchdog check header (`CN22`, unpopulated)

This header exposes the watchdog's clear input (pulsed whenever the CPU writes
to the watchdog clear register) as well as the reset output. Injecting pulses
to forcefully clear the watchdog should work, although it's much easier to
simply disable the watchdog by placing a jumper on `S86`.

| Pin | Name     | Dir |
| --: | :------- | :-- |
|   1 | `WDCLR`  | RW  |
|   2 | `/RESET` | RW  |
|   3 | `5V`     |     |
|   4 | `GND`    |     |

### Watchdog configuration jumper (`S86`, unpopulated)

Shorting pin 1 and 2 will disable the watchdog while keeping power-on reset
functional. Pin 3 is an active-high reset output, unused on the 573.

| Pin | Name    | Dir |
| --: | :------ | :-- |
|   1 | `WDEN`  | R   |
|   2 | `GND`   |     |
|   3 | `RESET` | W   |

### H8/3644 microcontroller pin mapping

| Pin   | H8 GPIO   | Dir | Connected to           | Usage                              |
| ----: | :-------- | :-- | :--------------------- | :--------------------------------- |
|    11 | `P9_0`    | R   |                        | _Unused_                           |
|    12 | `P9_1-4`  | W   | I/O ASIC               | Status output bus                  |
|    16 | `IRQ0`    | R   |                        | _Unused_                           |
| 17-24 | `P6_0-7`  | W   | I/O ASIC               | 16-bit JVS output bus (low byte?)  |
| 25-32 | `P5_0-7`  | W   | I/O ASIC               | 16-bit JVS output bus (high byte?) |
|    34 | `P7_3`    | R   | Unknown                |                                    |
|    35 | `P7_4`    | R   | Unknown                |                                    |
|    36 | `P7_5`    | R   |                        | _Unused_                           |
|    37 | `P7_6`    | R   |                        | _Unused_                           |
|    38 | `P7_7`    | R   |                        | _Unused_                           |
| 39-46 | `P8_0-7`  | R   | System bus (via latch) | 16-bit JVS write bus (low byte)    |
|    47 | `P2_0`    | W   | Unknown                |                                    |
|    48 | `P2_1/RX` | R   | RS485 transceiver      | JVS serial port receive            |
|    49 | `P2_2/TX` | W   | RS485 transceiver      | JVS serial port transmit           |
|    50 | `P3_2`    | R   |                        | _Unused_                           |
|    51 | `P3_1`    | R   |                        | _Unused_                           |
|    52 | `P3_0`    | R   |                        | _Unused_                           |
|    53 | `P1_0`    | W   | Unknown                |                                    |
|    54 | `P1_4`    | W   | Unknown                |                                    |
|    55 | `P1_5`    | R   |                        | _Unused_                           |
|    56 | `P1_6`    | R   |                        | _Unused_                           |
|    57 | `P1_7`    | R   |                        | _Unused_                           |
|  59-2 | `PB_7-0`  | R   | System bus (via latch) | 16-bit JVS write bus (high byte)   |

## Credits, sources and links

This document is the result of a joint effort consisting of years' worth of
research, brought to you by:

- **spicyjpeg** (documentation writing, software reverse engineering, testing)
- **Naoki Saito** (hardware reverse engineering, schematic tracing, testing)
- **987123879113** (digital I/O board reverse engineering, testing)
- **smf** (initial reverse engineering and implementation of the 573 MAME
  driver)
- **tensionvex** (testing)
- **Shiz** (security cartridge details)

Traced schematics, images, datasheets and additional resources are available in
[Naoki's 573 repo](https://github.com/NaokiS28/KSystem-573). Shiz also maintains
a [general documentation repo](https://github.com/Shizmob/arcade-docs) for
several arcade systems including the 573.

Some information has been aggregated from the following sources:

- [System 573 MAME driver](https://github.com/mamedev/mame/blob/master/src/mame/konami/ksys573.cpp)
- [987123879113's MAME fork](https://github.com/987123879113/mame) and
  [gobbletools](https://github.com/987123879113/gobbletools)
- ATAPI specification (revision 2.6, January 1996)
- ATA/ATAPI-6 specification (revision 1e, June 2001)
- JVS specification (third edition, command reference revision 1.3)
- HD6473644, M48T58, ADC0834, XCS40XL, MAS3507D, X76F041 and X76F100 datasheets
- [DDR stage I/O protocol notes](https://github.com/nchowning/open-io/blob/master/NOTES.txt)
- [JVS protocol notes](https://github.com/TheOnlyJoey/openjvs/wiki/Protocol)
- [Original (incomplete) list of working ATAPI drives](https://gamerepair.info/hardware/1_system_573)
- ["The Almost Definitive Guide to Session Mode Linking"](https://www2.gvsu.edu/brittedg/SessionGuide.pdf)
- [Callus Next PCB information](https://callusnext.com/pcbs)
- [Light output for Salary Man Champ](http://solid-orange.com/1569) and
  [Hyper Bishi Bashi Champ](http://solid-orange.com/1581)
- [system573\_tool](https://github.com/mrdion/system573_tool)
- [Arduino-based master calendar implementation](https://www.arcade-projects.com/threads/konami-system-573-master-calendar.2646/#post-34907)
- [Z-I-v forum post with security cartridge info](https://zenius-i-vanisher.com/v5.2/viewthread.php?threadid=2825)

Huge thanks to the Rhythm Game Cabs Discord server and everyone who provided
valuable information about the 573!
