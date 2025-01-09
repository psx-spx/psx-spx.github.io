
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
- [BIOS](#bios)
- [Game-specific information](#game-specific-information)
- [Notes](#notes)
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
  is only partially known currently.
- Some revisions of the main board have two resistor footprints next to the
  Konami ASIC, one labeled `FJ` and the other `SH`. Only one of them is
  populated; it presumably sets or clears a bit in one of the ASIC input ports.
  Given the labels it may be related to the manufacturer of the onboard flash
  memory (Fujitsu or Sharp), however even boards fitted with Sharp chips come
  with the `FJ` resistor populated. Moreover, all known games identify the chips
  by probing their JEDEC ID.

## Differences vs. PS1

### Main changes

- **Main RAM is 4 MB** instead of 2 MB and **VRAM is 2 MB** instead of 1 MB. SPU
  RAM is still 512 KB.
- **The CD-ROM drive is completely different**. While the PS1's drive is fully
  integrated into the motherboard and uses a custom protocol, the 573 employs a
  standard ATAPI drive. It can thus boot from burned CD-Rs or even CD-RWs just
  fine (as long as the drive itself is capable of reading them in the first
  place), with no modifications needed to the stock hardware. There is no
  provision for playing XA-ADPCM, however CD-DA playback through the drive's own
  audio output (fed into the 573 motherboard via a 4-pin audio cable) is
  supported and used by some games.
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

- **Audio and video outputs**: unlike the PS1, which outputs composite, S-video
  and RGB, the 573 only outputs RGB with C-sync through the JAMMA connector and
  a DB15 port compliant with the JVS specification (same pinout as VGA but not
  directly compatible, as VGA normally runs at higher resolutions and uses
  separate H/V sync pins). A built-in 15 watt stereo speaker amplifier is also
  provided for cabinets that lack their own sound system.
- **JAMMA interface and built-in I/O ports**: the 573 provides multiple digital
  and analog ports for interfacing with arcade cabinet controls. Depending on
  the I/O board the system came with, these signals might be broken out through
  connectors on the system's case.
- **Internal 16 MB flash memory**: the 573's BIOS is capable of booting either
  from the CD drive or from an array of flash memory chips soldered to the
  motherboard, which are also memory mapped. Most Konami games are designed to
  run from flash: when attempting to run them from CD without also having them
  installed, the executable on the disc will erase the flash and install the
  game before starting. Most games still require the CD, in some cases a
  different one, to be kept in the drive after installation as they use it for
  music playback or to stream additional data.
- **PCMCIA memory card**: some games shipped with additional flash memory in the
  form of one or more 16 or 32 MB PCMCIA cards. Note that these are "linear"
  memory mapped flash cards without any built-in controller, not CF or
  ATA-compatible cards. See the BIOS section for more details on why CF cards
  are not supported.
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
| `0x1f500000-0x1f6a0001` | [Other registers](#other-registers)                    |

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

| Bits | RW | Description (ATA)                 | RW | Description (ATAPI)           |
| ---: | :- | :-------------------------------- | :- | :---------------------------- |
|    0 |    | _Reserved_                        | R  | Illegal length flag (`ILI`)   |
|    1 | R  | No media flag (`NM`)              | R  | End of media flag (`EOM`)     |
|    2 | R  | Command aborted flag (`ABRT`)     | R  | Command aborted flag (`ABRT`) |
|    3 | R  | Media change request flag (`MCR`) |    | _Reserved_                    |
|    4 | R  | Address not found flag (`IDNF`)   | R  | SCSI sense key bit 0          |
|    5 | R  | Media changed flag (`MC`)         | R  | SCSI sense key bit 1          |
|    6 | R  | Uncorrectable error flag (`UNC`)  | R  | SCSI sense key bit 2          |
|    7 | R  | DMA CRC error flag (`ICRC`)       | R  | SCSI sense key bit 3          |
| 8-15 |    | _Unused_                          |    | _Unused_                      |

When written:

| Bits | RW | Description (ATA)                       | RW | Description (ATAPI)                              |
| ---: | :- | :-------------------------------------- | :- | :----------------------------------------------- |
|    0 | W  | Command-specific feature index or flags | W  | Use overlapped mode for next command (`OVL`)     |
|    1 | W  | Command-specific feature index or flags | W  | Transfer data for next command using DMA (`DMA`) |
|  2-7 | W  | Command-specific feature index or flags | W  | _Reserved_ (should be 0)                         |
| 8-15 |    | _Unused_                                |    | _Unused_                                         |

#### `0x1f480004` (IDE bank 0, address 2): **Sector count**

| Bits | RW | Description (ATA)              | RW | Description (ATAPI)                                            |
| ---: | :- | :----------------------------- | :- | :------------------------------------------------------------- |
|    0 | W  | Transfer sector count bit 0    | R  | Pending transfer type (`C/D`, 0 = data, 1 = command)           |
|    1 | W  | Transfer sector count bit 1    | R  | Pending transfer direction (`I/O`, 0 = to device, 1 = to host) |
|    2 | W  | Transfer sector count bit 2    | R  | Pending transfer bus release flag (`REL`)                      |
|  3-7 | W  | Transfer sector count bits 3-7 | RW | Current command tag                                            |
| 8-15 |    | _Unused_                       |    | _Unused_                                                       |

In ATA 48-bit LBA mode, bits 8-15 of the number of sectors to transfer must be
written to this register first, followed by bits 0-7.

In ATA CHS or 28-bit LBA mode, setting this register to 0 will cause 256 sectors
to be transferred.

#### `0x1f480006` (IDE bank 0, address 3): **Sector number**

| Bits | RW | Description (ATA)                | RW | Description (ATAPI) |
| ---: | :- | :------------------------------- | :- | :------------------ |
|  0-7 | W  | CHS sector index or LBA bits 0-7 |    | _Unused_            |
| 8-15 |    | _Unused_                         |    | _Unused_            |

In ATA 48-bit LBA mode, bits 24-31 of the target LBA must be written to this
register first, followed by bits 0-7.

#### `0x1f480008` (IDE bank 0, address 4): **Cylinder number low**

| Bits | RW | Description (ATA)                            | RW | Description (ATAPI)          |
| ---: | :- | :------------------------------------------- | :- | :--------------------------- |
|  0-7 | RW | CHS cylinder index bits 0-7 or LBA bits 8-15 | RW | Transfer chunk size bits 0-7 |
| 8-15 |    | _Unused_                                     |    | _Unused_                     |

In ATA 48-bit LBA mode, bits 32-39 of the target LBA must be written to this
register first, followed by bits 8-15.

When reset, ATAPI drives will set this register to `0x14`.

#### `0x1f48000a` (IDE bank 0, address 5): **Cylinder number high**

| Bits | RW | Description (ATA)                              | RW | Description (ATAPI)           |
| ---: | :- | :--------------------------------------------- | :- | :---------------------------- |
|  0-7 | RW | CHS cylinder index bits 8-15 or LBA bits 16-23 | RW | Transfer chunk size bits 8-15 |
| 8-15 |    | _Unused_                                       |    | _Unused_                      |

In ATA 48-bit LBA mode, bits 40-47 of the target LBA must be written to this
register first, followed by bits 16-23.

When reset, ATAPI drives will set this register to `0xeb`.

#### `0x1f48000c` (IDE bank 0, address 6): **Head number** / **Drive select**

| Bits | RW | Description (ATA)                         | RW | Description (ATAPI)                       |
| ---: | :- | :---------------------------------------- | :- | :---------------------------------------- |
|  0-3 | W  | CHS head index or 28-bit LBA bits 24-27   |    | _Reserved_ (should be 0)                  |
|    4 | RW | Drive select (0 = primary, 1 = secondary) | RW | Drive select (0 = primary, 1 = secondary) |
|    5 |    | _Reserved_ (should be 1?)                 |    | _Reserved_ (should be 1?)                 |
|    6 | W  | Sector addressing mode (0 = CHS, 1 = LBA) |    | _Reserved_ (should be 0)                  |
|    7 |    | _Reserved_ (should be 1?)                 |    | _Reserved_ (should be 1?)                 |
| 8-15 |    | _Unused_                                  |    | _Unused_                                  |

Bits 0-3 are not used in ATA 48-bit LBA mode.

#### `0x1f48000e` (IDE bank 0, address 7): **Status** / **Command**

When read:

| Bits | RW | Description (ATA)              | RW | Description (ATAPI)              |
| ---: | :- | :----------------------------- | :- | :------------------------------- |
|    0 | R  | Error flag (`ERR`)             | R  | Check condition flag (`CHK`)     |
|    1 |    | _Reserved_                     |    | _Reserved_                       |
|    2 |    | _Reserved_                     |    | _Reserved_                       |
|    3 | R  | Data request flag (`DRQ`)      | R  | Data request flag (`DRQ`)        |
|    4 | R  | Drive write error flag (`DWE`) | R  | Overlapped service flag (`SERV`) |
|    5 | R  | Drive fault flag (`DF`)        | R  | Drive fault flag (`DF`)          |
|    6 | R  | Drive ready flag (`DRDY`)      | R  | Drive ready flag (`DRDY`)        |
|    7 | R  | Drive busy flag (`BSY`)        | R  | Drive busy flag (`BSY`)          |
| 8-15 |    | _Unused_                       |    | _Unused_                         |

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

Read-only mirror of the status register at `0x1f48000e` that returns the same
flags, but does not acknowledge any pending IRQ when read.

#### IDE DMA and quirks

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

| Bits | RW | Buffered | Description            |
| ---: | :- | :------- | :--------------------- |
|  0-3 | RW | Yes      | Minute units (0-9)     |
|  4-6 | RW | Yes      | Minute tens (0-5)      |
|    7 |    |          | _Reserved_ (must be 0) |
| 8-15 |    |          | _Unused_               |

#### `0x1f623ff6` (M48T58 register `0x1ffb`): **Hour**

| Bits | RW | Buffered | Description                          |
| ---: | :- | :------- | :----------------------------------- |
|  0-3 | RW | Yes      | Hour units (0-9, or 0-3 if tens = 2) |
|  4-5 | RW | Yes      | Hour tens (0-2)                      |
|  6-7 |    |          | _Reserved_ (must be 0)               |
| 8-15 |    |          | _Unused_                             |

Hours are always returned in 24-hour format, as there is no way to switch to
12-hour format.

#### `0x1f623ff8` (M48T58 register `0x1ffc`): **Day of week** / **Century**

| Bits | RW | Buffered | Description                                |
| ---: | :- | :------- | :----------------------------------------- |
|  0-2 | RW | Yes      | Day of week (1-7)                          |
|    3 |    |          | _Reserved_ (must be 0)                     |
|    4 | RW | Yes      | Century flag                               |
|    5 | RW | Unknown  | Century flag toggling enable (1 = enabled) |
|    6 | RW | Unknown  | Enable 512 Hz clock signal output on pin 1 |
|    7 |    |          | _Reserved_ (must be 0)                     |
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
|  5-7 |    |          | _Reserved_ (must be 0)                |
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
    MCU will wait for a response indefinitely even if no device is present.
5.  Read the packet, again two bytes at a time, from `0x1f40000a`, waiting for
    `JVSIRDY` to go high before each read and clearing it by writing to
    `0x1f520000` after each read. The status code will be set to 2 after the
    first word is read and back to 0 once no more data is available to read.

The MCU does not allow for non-JVS packets to be sent as it validates the sync
byte, checksum and uses the length field to determine packet length. Responses
cannot be received without sending a packet first either. The MCU will also
insert a 200 us minimum delay between the last byte of a received packet and the
first byte of the next packet.

## I/O boards

The System 573 was designed to be expanded with game-specific hardware using I/O
expansion boards mounted on top of the main board, and/or custom security
cartridges. I/O boards have access to the 16-bit system bus and are accessible
through the `0x1f640000-0x1f6400ff` region.

- [Analog I/O board (`GX700-PWB(F)`)](#analog-io-board-gx700-pwbf)
- [Digital I/O board (`GX894-PWB(B)A`)](#digital-io-board-gx894-pwbba)
- [Alternate analog I/O board (`GX700-PWB(K)`)](#alternate-analog-io-board-gx700-pwbk)
- [Fishing controller I/O board (`GE765-PWB(B)A`)](#fishing-controller-io-board-ge765-pwbba)
- [DDR Karaoke Mix I/O board (`GX921-PWB(B)`)](#ddr-karaoke-mix-io-board-gx921-pwbb)
- [GunMania I/O board (`PWB0000073070`)](#gunmania-io-board-pwb0000073070)
- [Hypothetical debugging board](#hypothetical-debugging-board)

### Analog I/O board (`GX700-PWB(F)`)

Used in early Bemani games such as DDR 1stMIX and 2ndMIX, as well as some
non-Bemani games. The name is misleading as the board does not deal with any
analog signals whatsoever; the name was given retroactively to distinguish it
from the digital I/O board. It provides up to 28 optoisolated open-drain outputs
typically used to control cabinet lights, split across 4 banks:

- **Bank A** (`CN33`): 8 outputs (A0-A7)
- **Bank B** (`CN34`): 8 outputs (B0-B7)
- **Bank C** (`CN35`): 8 outputs (C0-C7)
- **Bank D** (`CN36`): 4 outputs (D0-D3)

Some games shipped with partially populated analog I/O boards, thus not all
banks may be available. See the game-specific information section for details on
how lights are wired up on each cabinet type.

#### `0x1f640080`: **Bank A**

| Bits | RW | Description                          |
| ---: | :- | :----------------------------------- |
|    0 | W  | Output A1 (0 = grounded, 1 = high-z) |
|    1 | W  | Output A3 (0 = grounded, 1 = high-z) |
|    2 | W  | Output A5 (0 = grounded, 1 = high-z) |
|    3 | W  | Output A7 (0 = grounded, 1 = high-z) |
|    4 | W  | Output A6 (0 = grounded, 1 = high-z) |
|    5 | W  | Output A4 (0 = grounded, 1 = high-z) |
|    6 | W  | Output A2 (0 = grounded, 1 = high-z) |
|    7 | W  | Output A0 (0 = grounded, 1 = high-z) |
| 8-15 |    | _Unused_                             |

#### `0x1f640088`: **Bank B**

| Bits | RW | Description                          |
| ---: | :- | :----------------------------------- |
|    0 | W  | Output B1 (0 = grounded, 1 = high-z) |
|    1 | W  | Output B3 (0 = grounded, 1 = high-z) |
|    2 | W  | Output B5 (0 = grounded, 1 = high-z) |
|    3 | W  | Output B7 (0 = grounded, 1 = high-z) |
|    4 | W  | Output B6 (0 = grounded, 1 = high-z) |
|    5 | W  | Output B4 (0 = grounded, 1 = high-z) |
|    6 | W  | Output B2 (0 = grounded, 1 = high-z) |
|    7 | W  | Output B0 (0 = grounded, 1 = high-z) |
| 8-15 |    | _Unused_                             |

#### `0x1f640090`: **Bank C**

| Bits | RW | Description                          |
| ---: | :- | :----------------------------------- |
|    0 | W  | Output C1 (0 = grounded, 1 = high-z) |
|    1 | W  | Output C3 (0 = grounded, 1 = high-z) |
|    2 | W  | Output C5 (0 = grounded, 1 = high-z) |
|    3 | W  | Output C7 (0 = grounded, 1 = high-z) |
|    4 | W  | Output C6 (0 = grounded, 1 = high-z) |
|    5 | W  | Output C4 (0 = grounded, 1 = high-z) |
|    6 | W  | Output C2 (0 = grounded, 1 = high-z) |
|    7 | W  | Output C0 (0 = grounded, 1 = high-z) |
| 8-15 |    | _Unused_                             |

#### `0x1f640098`: **Bank D**

| Bits | RW | Description                          |
| ---: | :- | :----------------------------------- |
|    0 | W  | Output D3 (0 = grounded, 1 = high-z) |
|    1 | W  | Output D2 (0 = grounded, 1 = high-z) |
|    2 | W  | Output D1 (0 = grounded, 1 = high-z) |
|    3 | W  | Output D0 (0 = grounded, 1 = high-z) |
| 4-15 |    | _Unused_                             |

### Digital I/O board (`GX894-PWB(B)A`)

Used by later Bemani games, such as DDR from Solo onwards. This board features
the same 28 isolated open-drain outputs as the analog I/O board, plus a Xilinx
XCS40XL Spartan-XL FPGA and a Micronas MAS3507D audio decoder ASIC used to play
encrypted MP3 files. The FPGA has 24 MB of dedicated DRAM into which the files
are preloaded on startup, then decrypted on the fly and fed to the decoder. The
board also features 128 KB of SRAM used as a cache, RS-232 and ARCnet
transceivers for communication with other hardware and a DS2401 serial number
chip, used to prevent usage of the same security cartridge on more than one 573.

The vast majority of the registers provided by this board (including some but
not all light outputs) are handled by its FPGA, which requires a configuration
bitstream to be uploaded to it in order to work. Registers in the
`0x1f6400f0-0x1f6400ff` region are handled by a CPLD and are functional even if
no bitstream is loaded. There are several known versions of Konami's bitstream:

| SHA-1 (LSB first)                          | First used by                          |
| :----------------------------------------- | :------------------------------------- |
| `32d455a25eb26fe4e4b577cb0f0e3bebd0f82959` | Dance Dance Revolution Solo Bass Mix   |
| `a53b8906de95c34b6e3f053bd7488c888bc904b6` | Dance Dance Revolution 3rdMIX          |
| `5d27c84e812f71401f940621f79c5c6114192895` | GuitarFreaks 2ndMIX                    |
| `450b12627b7eacd3ea3f8b0b7a16589a13010c41` | Mambo a Go-Go                          |
| `53d0c1e3f6ae042d7d45ce889b79a12f1be5eabd` | Martial Beat e-Amusement               |
| `d1d0f123bbb9d5abfefbd556c366f9ded0779e41` | Martial Beat (leftover file 1, unused) |
| `f354619fe1a80cabe0b774784181b3bfeff0a3e9` | Martial Beat (leftover file 2, unused) |

The DDR and Mambo bitstreams all implement the same registers (listed below) and
seem to only differ in the MP3 decryption algorithm, while the unused Martial
Beat bitstreams seem to behave in a completely different way. Homebrew tools may
also load custom bitstreams, which can be developed using the Xilinx ISE
toolchain. See the pinouts section for a list of all devices connected to the
FPGA.

#### `0x1f640080` (FPGA, DDR/Mambo bitstream): **Magic number**

| Bits | RW | Description             |
| ---: | :- | :---------------------- |
| 0-15 | R  | Magic number (`0x1234`) |

This register is checked by some versions of Konami's digital I/O board driver
to make sure the bitstream was properly loaded.

#### `0x1f640090` (FPGA, DDR/Mambo bitstream): **Network board address**

#### `0x1f640092` (FPGA, DDR/Mambo bitstream): **Unknown (network related)**

#### `0x1f6400a0` (FPGA, DDR/Mambo bitstream): **MP3 data start address high**

#### `0x1f6400a2` (FPGA, DDR/Mambo bitstream): **MP3 data start address low**

#### `0x1f6400a4` (FPGA, DDR/Mambo bitstream): **MP3 data end address high**

#### `0x1f6400a6` (FPGA, DDR/Mambo bitstream): **MP3 data end address low**

#### `0x1f6400a8` (FPGA, DDR/Mambo bitstream): **MP3 frame counter** / **Descrambler key 1**

#### `0x1f6400aa` (FPGA, DDR/Mambo bitstream): **MP3 playback status**

When read:

| Bits | RW | Description                               |
| ---: | :- | :---------------------------------------- |
| 0-11 |    | _Unused_                                  |
|   12 | R  | MAS3507D MP3 data request flag (`PI19`)   |
|   13 | R  | MAS3507D MP3 error flag (`PI8`)           |
|   14 | R  | MAS3507D MP3 frame sync flag (`PI4`)      |
|   15 | R  | MAS3507D master clock ready flag (`WRDY`) |

When written:

| Bits  | RW | Description                                     |
| ----: | :- | :---------------------------------------------- |
|  0-11 |    | _Unused_                                        |
|    12 | W  | MAS3507D chip reset (`/POR`, 0 = pull low)      |
|    13 | W  | MAS3507D PIO chip select (`/PCS`, 0 = pull low) |
| 14-15 |    | _Unused_                                        |

During normal operation the reset input should be high and the PIO chip select
low. Setting the chip select high will result in the MAS3507D tristating `PI19`,
`PI8` and `PI4`.

#### `0x1f6400ac` (FPGA, DDR/Mambo bitstream): **MAS3507D I2C**

#### `0x1f6400ae` (FPGA, DDR/Mambo bitstream): **MP3 data feeder control**

| Bits  | RW | Description                                                |
| ----: | :- | :--------------------------------------------------------- |
|  0-11 |    | _Unused_                                                   |
|    12 | R  | Current playback status (0 = paused, 1 = playing)          |
|    13 | W  | Playback enable (0 = disabled/ignore bit 14, 1 = enabled)  |
|    14 | W  | Playback control (0 = pause, 1 = play)                     |
|    15 | W  | MP3 frame counter enable (0 = disabled/reset, 1 = enabled) |

Data is only fed to the MAS3507D when both bits 13 and 14 are set. Bit 12 is a
read-only copy of bit 14 and remains set if playback is stopped by clearing bit
13 only.

Bit 15 controls whether to increment register `0x1f6400a8` each time a rising
edge is detected on the MAS3507D's `PI4` (frame sync) pin. The counter is
automatically reset to zero when this bit is cleared.

#### `0x1f6400b0` (FPGA, DDR/Mambo bitstream): **DRAM write address high**

#### `0x1f6400b2` (FPGA, DDR/Mambo bitstream): **DRAM write address low**

#### `0x1f6400b6` (FPGA, DDR/Mambo bitstream): **DRAM read address high**

#### `0x1f6400b8` (FPGA, DDR/Mambo bitstream): **DRAM read address low**

#### `0x1f6400ba` (FPGA, DDR/Mambo bitstream): **Unknown**

#### `0x1f6400c0` (FPGA, DDR/Mambo bitstream): **Network data**

#### `0x1f6400c2` (FPGA, DDR/Mambo bitstream): **Network TX FIFO length**

#### `0x1f6400c4` (FPGA, DDR/Mambo bitstream): **Network RX FIFO length**

#### `0x1f6400c6` (FPGA, DDR/Mambo bitstream): **Unknown**

Seems to return `0x7654` on startup.

#### `0x1f6400c8` (FPGA, DDR/Mambo bitstream): **Unknown (network related)**

Seems to also return `0x7654` on startup.

#### `0x1f6400ca` (FPGA, DDR/Mambo bitstream): **DAC sample counter high**

#### `0x1f6400cc` (FPGA, DDR/Mambo bitstream): **DAC sample counter low**

#### `0x1f6400ce` (FPGA, DDR/Mambo bitstream): **DAC sample counter delta**

#### `0x1f6400e0` (FPGA, DDR/Mambo bitstream): **Bank A**

| Bits | RW | Description                          |
| ---: | :- | :----------------------------------- |
| 0-11 |    | _Unused_                             |
|   12 | W  | Output A4 (0 = grounded, 1 = high-z) |
|   13 | W  | Output A5 (0 = grounded, 1 = high-z) |
|   14 | W  | Output A6 (0 = grounded, 1 = high-z) |
|   15 | W  | Output A7 (0 = grounded, 1 = high-z) |

#### `0x1f6400e2` (FPGA, DDR/Mambo bitstream): **Bank A**

| Bits | RW | Description                          |
| ---: | :- | :----------------------------------- |
| 0-11 |    | _Unused_                             |
|   12 | W  | Output A0 (0 = grounded, 1 = high-z) |
|   13 | W  | Output A1 (0 = grounded, 1 = high-z) |
|   14 | W  | Output A2 (0 = grounded, 1 = high-z) |
|   15 | W  | Output A3 (0 = grounded, 1 = high-z) |

#### `0x1f6400e4` (FPGA, DDR/Mambo bitstream): **Bank B**

| Bits | RW | Description                          |
| ---: | :- | :----------------------------------- |
| 0-11 |    | _Unused_                             |
|   12 | W  | Output B4 (0 = grounded, 1 = high-z) |
|   13 | W  | Output B5 (0 = grounded, 1 = high-z) |
|   14 | W  | Output B6 (0 = grounded, 1 = high-z) |
|   15 | W  | Output B7 (0 = grounded, 1 = high-z) |

#### `0x1f6400e6` (FPGA, DDR/Mambo bitstream): **Bank D**

| Bits | RW | Description                          |
| ---: | :- | :----------------------------------- |
| 0-11 |    | _Unused_                             |
|   12 | W  | Output D0 (0 = grounded, 1 = high-z) |
|   13 | W  | Output D1 (0 = grounded, 1 = high-z) |
|   14 | W  | Output D2 (0 = grounded, 1 = high-z) |
|   15 | W  | Output D3 (0 = grounded, 1 = high-z) |

#### `0x1f6400e8` (FPGA, DDR/Mambo bitstream): **Internal logic reset**

Konami's code writes `0xf000`, followed by `0x0000`, a delay and `0xf000` again,
to this register after uploading the bitstream.

#### `0x1f6400ea` (FPGA, DDR/Mambo bitstream): **Descrambler key 2**

#### `0x1f6400ec` (FPGA, DDR/Mambo bitstream): **Descrambler key 3**

#### `0x1f6400ee` (FPGA, DDR/Mambo bitstream): **1-wire bus**

When read:

| Bits  | RW | Description               |
| ----: | :- | :------------------------ |
|   0-7 |    | _Unused_                  |
|     8 | R  | DS2433 1-wire bus readout |
|  9-11 |    | _Unused_                  |
|    12 | R  | DS2401 1-wire bus readout |
| 13-15 |    | _Unused_                  |

When written:

| Bits  | RW | Description                                                  |
| ----: | :- | :----------------------------------------------------------- |
|   0-7 |    | _Unused_                                                     |
|     8 | W  | Drive DS2433 1-wire bus low (1 = pull to ground, 0 = high-z) |
|  9-11 |    | _Unused_                                                     |
|    12 | W  | Drive DS2401 1-wire bus low (1 = pull to ground, 0 = high-z) |
| 13-15 |    | _Unused_                                                     |

In addition to the DS2401 the board has an unpopulated footprint for a DS2433
1-wire EEPROM, connected to a separate FPGA pin.

#### `0x1f6400f0` (CPLD): **Unknown (unused?)**

Konami's code does not write to this CPLD register.

#### `0x1f6400f2` (CPLD): **Unknown (unused?)**

Konami's code does not write to this CPLD register.

#### `0x1f6400f4` (CPLD): **DAC reset**

| Bits | RW | Description                                  |
| ---: | :- | :------------------------------------------- |
| 0-14 |    | _Unused_                                     |
|   15 | W  | Audio DAC reset/disable (0 = pull reset low) |

Konami's code uses this register to mute the DAC during FPGA and MAS3507D
initialization.

#### `0x1f6400f6` (CPLD): **FPGA status and control**

When read:

| Bits | RW | Description                      |
| ---: | :- | :------------------------------- |
| 0-11 |    | _Unused_                         |
|   12 | R  | Possibly `/INIT` from FPGA       |
|   13 | R  | Possibly `DONE` from FPGA        |
|   14 | R  | Board identification? (always 1) |
|   15 | R  | Board identification? (always 0) |

**NOTE**: all registers in the `0x1f6400f0-0x1f6400ff` region seem to return the
same value as this register when read, possibly due to incomplete address
decoding in the CPLD. Konami's driver only ever reads from this register and
treats all other CPLD registers as write-only.

When written:

| Bits | RW | Description                 |
| ---: | :- | :-------------------------- |
| 0-11 |    | _Unused_                    |
|   12 | W  | Possibly `/INIT` to FPGA    |
|   13 | W  | Possibly `DONE` to FPGA     |
|   14 | W  | Possibly `/PROGRAM` to FPGA |
|   15 | W  | Unused? (always 1)          |

This register is only written to 3 times when resetting the FPGA prior to
loading the bitstream. The values written are `0x8000` first, then `0xc000` and
finally `0xf000`.

#### `0x1f6400f8` (CPLD): **FPGA bitstream upload**

| Bits | RW | Description             |
| ---: | :- | :---------------------- |
| 0-14 |    | _Unused_                |
|   15 | W  | Bit to send to the FPGA |

Bits written to this register are sent to the FPGA's configuration interface
(`DIN` and `CCLK` pins, see the XCS40XL datasheet). There is no separate bit to
control the `CCLK` pin as clocking is handled automatically. The FPGA is wired
to boot in "slave serial" mode and wait for a bitstream to be loaded by the 573
through this port.

All known games load the bitstream from an array embedded in the executable or a
file on the internal flash (usually named `data/fpga/fpga_mp3.bin`), then write
its contents to this port LSB first and monitor the FPGA status register. The
bitstream is always 330696 bits (41337 bytes) long as per the XCS40XL datasheet.

#### `0x1f6400fa` (CPLD): **Bank C**

| Bits | RW | Description                          |
| ---: | :- | :----------------------------------- |
| 0-11 |    | _Unused_                             |
|   12 | W  | Output C0 (0 = grounded, 1 = high-z) |
|   13 | W  | Output C1 (0 = grounded, 1 = high-z) |
|   14 | W  | Output C2 (0 = grounded, 1 = high-z) |
|   15 | W  | Output C3 (0 = grounded, 1 = high-z) |

#### `0x1f6400fc` (CPLD): **Bank C**

| Bits | RW | Description                          |
| ---: | :- | :----------------------------------- |
| 0-11 |    | _Unused_                             |
|   12 | W  | Output C4 (0 = grounded, 1 = high-z) |
|   13 | W  | Output C5 (0 = grounded, 1 = high-z) |
|   14 | W  | Output C6 (0 = grounded, 1 = high-z) |
|   15 | W  | Output C7 (0 = grounded, 1 = high-z) |

#### `0x1f6400fe` (CPLD): **Bank B**

| Bits | RW | Description                          |
| ---: | :- | :----------------------------------- |
| 0-11 |    | _Unused_                             |
|   12 | W  | Output B0 (0 = grounded, 1 = high-z) |
|   13 | W  | Output B1 (0 = grounded, 1 = high-z) |
|   14 | W  | Output B2 (0 = grounded, 1 = high-z) |
|   15 | W  | Output B3 (0 = grounded, 1 = high-z) |

### Alternate analog I/O board (`GX700-PWB(K)`)

Used by Kick &amp; Kick. Has several optocouplers, plus a DS2401 serial number
chip and several unpopulated footprints.

This board is currently undocumented.

### Fishing controller I/O board (`GE765-PWB(B)A`)

Used by the Fisherman's Bait series. Uses an NEC uPD4701 mouse/trackball chip to
track motion of the fishing reel's rotary encoders and contains PWM drivers for
the feedback motors. Along with the analog I/O board, it is the only known board
that does *not* have a DS2401.

This board is currently undocumented.

### DDR Karaoke Mix I/O board (`GX921-PWB(B)`)

Used by DDR Karaoke Mix 1 and 2. Similarly to the digital I/O board, this board
features several optoisolated light outputs, an ARCnet PHY and a DS2401 serial
number chip. It also has composite video inputs and outputs, a video encoder to
convert the 573's native RGB output to composite and additional circuitry to
superimpose it onto the video feed from an external karaoke machine. An onboard
PC16552 UART is provided to communicate with the machine (the security cartridge
also exposes SIO1).

This board is currently undocumented.

### GunMania I/O board (`PWB0000073070`)

Used by GunMania and GunMania Zone Plus. Contains an RGB to S-video converter
which drives the cabinet's projector, several motor drivers, optoisolators, a
PC16552 UART and a DS2401 serial number chip. A DB25 connector on the side of
the board is used to interface to the resistive matrix used to detect bullet
shots.

This board is currently undocumented.

### Hypothetical debugging board

There is no proof whatsoever of this board having ever existed, but the BIOS and
some games attempt to access the hardware on it. It seems to contain at least a
Fujitsu MB89371 UART and a 7-segment display, although these may have actually
been on two separate boards (or built into a prototype board used by Konami
during development).

The MB89371 does not have a publicly available datasheet.

#### `0x1f640000`: **UART data**

#### `0x1f640002`: **UART control**

#### `0x1f640004`: **UART baud rate select**

#### `0x1f640006`: **UART mode**

#### `0x1f640010`: **7-segment display**

| Bits | RW | Description                    |
| ---: | :- | :----------------------------- |
|    0 | W  | Right digit segment G (0 = on) |
|    1 | W  | Right digit segment F (0 = on) |
|    2 | W  | Right digit segment E (0 = on) |
|    3 | W  | Right digit segment D (0 = on) |
|    4 | W  | Right digit segment C (0 = on) |
|    5 | W  | Right digit segment B (0 = on) |
|    6 | W  | Right digit segment A (0 = on) |
|    7 |    | _Unused_                       |
|    8 | W  | Left digit segment G (0 = on)  |
|    9 | W  | Left digit segment F (0 = on)  |
|   10 | W  | Left digit segment E (0 = on)  |
|   11 | W  | Left digit segment D (0 = on)  |
|   12 | W  | Left digit segment C (0 = on)  |
|   13 | W  | Left digit segment B (0 = on)  |
|   14 | W  | Left digit segment A (0 = on)  |
|   15 |    | _Unused_                       |

Used by the BIOS kernel while booting (in a similar way to the standard PS1
kernel, which uses register `0x1f802041` instead) as well as the shell and some
games. This may have been meant to be a POST display integrated into the 573
main board at some point.

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
- a single tristate I/O pin (`SDA`), which can be either configured as a
  floating input or set to output the same logic level as `D0` through register
  `0x1f500000`;
- the CPU's SIO1 interface (`TX`, `RX`, `/RTS`, `/CTS`, `/DTR`, `/DSR`);
- four bus handshaking lines (`IRDY`, `DRDY`, `/IREQ`, `/DACK`).

As all EEPROMs used in cartridges have an I2C interface rather than a parallel
one, `SDA` is used in combination with individual bits of the parallel I/O ports
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

| Name   | Dir | Usage                                              |
| :----- | :-- | :------------------------------------------------- |
| `/DSR` | I   | Cartridge insertion detection (grounded)           |
| `D0`   | O   | Drives X76F041 I2C SDA when `SDA` is set as output |
| `D1`   | O   | X76F041 I2C SCL                                    |
| `D2`   | O   | X76F041 chip select (`/CS`)                        |
| `D3`   | O   | X76F041 reset (`RST`)                              |
| `SDA`  | IO  | X76F041 I2C SDA readout                            |

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

| Name | Dir | Usage                                               |
| :--- | :-- | :-------------------------------------------------- |
| `D0` | O   | Chip select to ADC (`/CS`), shared with X76F041 SDA |
| `D1` | O   | Data clock to ADC (`CLK`), shared with X76F041 SCL  |
| `D5` | O   | Data input to ADC (`DI`)                            |
| `I0` | I   | Data output from ADC (`DO`)                         |
| `I1` | I   | SAR status from ADC (`SARS`)                        |

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

| Name   | Dir | Usage                                           |
| :----- | :-- | :---------------------------------------------- |
| `/DSR` | I   | Cartridge insertion detection (grounded)        |
| `D0`   | O   | Drives ZS01 I2C SDA when `SDA` is set as output |
| `D1`   | O   | ZS01 I2C SCL                                    |
| `D3`   | O   | ZS01 reset                                      |
| `SDA`  | IO  | ZS01 I2C SDA readout                            |

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

### PS1 controller and memory card adapter (`GE885-PWB(A)`)

A ridiculously overengineered JVS board providing support for accessing PS1
controllers and memory cards plugged into ports on the front of the cabinet.
Contains a Toshiba TMPR3904 CPU, a Xilinx XCS10XL Spartan-XL FPGA, 512 KB of RAM
and a 512 KB boot ROM; the ROM is only a small bootloader and the actual
firmware is downloaded from the 573 into RAM. There are also two connectors for
security dongles. Returns the following JVS identifier string:

```
KONAMI CO.,LTD.;White I/O;Ver1.0;White I/O PCB
```

Memory card support became common in later Bemani games, allowing players to
save their scores and play custom charts. GuitarFreaks is the only game known
to support external controllers through this board.

### PunchMania 2 PCMCIA splitter (`PWB0000085445`)

Combines two 32 MB PCMCIA flash cards into the same address space, allowing them
to be accessed as if they were a single 64 MB card. Connects to the 573 through
a cable that plugs into a passive PCMCIA slot adapter. Only used by PunchMania
2.

### e-Amusement network unit (`PWB0000100991`)

Used by some Bemani games, in particular later GuitarFreaks and DrumMania
releases. Provides networking functionality (DHCP and TCP/UDP sockets) as well
as a 10 or 20 GB IDE hard drive for storage of downloaded content. The module
contains a Toshiba TMPR3927 CPU, a Xilinx XC2S100 Spartan-2 FPGA, 16 MB of RAM,
a 512 KB boot ROM and a DP83815 PCI Ethernet MAC. As with the controller and
memory card adapter, the bulk of the firmware seems to be loaded from the 573.
Connects through PCMCIA slot 2, using the same cable and adapter as the
PunchMania PCMCIA splitter.

### Multisession unit (`GXA25-PWB(A)`)

A fairly large box containing a Toshiba TMPR3927 CPU, a Xilinx XC2S200 Spartan-2
FPGA and four (!) hardware MP3 decoders. It comes with up to four daughterboards
installed, each of which hosts a stereo DAC and has RCA jacks for audio input
and output plus a mini-DIN connector for RS-232 communication with a cabinet.
The box also has its own ATAPI CD-ROM drive and power supply.

Its purpose is to enable "session mode" in later Bemani games, which allows for
the same song to be played on multiple games at the same time with the box
playing the backing tracks and routing audio between the machines. It connects
to each cabinet's 573 using RS-232, through the "network" port on the security
cartridge.

### Master calendar

A JVS device used internally by Konami to initialize motherboards and security
cartridges during manufacturing. The exact hardware Konami used is unknown, but
the protocol can be inferred from game code. All games search the JVS bus on
startup and enter a "factory test" mode if any device with the following
identifier string is present:

```
KONAMI CO.,LTD.;Master Calendar;<any value>;<any value>
```

The game will then proceed to request the current date, time, game and region
information from the master calendar, initialize the RTC and program the
security cartridge. The master calendar also returns a unique trace ID (see the
cartridge data formats section) for each 573, used for identification purposes
on cartridges that lack a DS2401.

#### `0x70`: **Get date and time**

#### `0x71`: **Get game region or initialization data**

#### `0x7c, 0x7f, 0x00`: **Get trace ID "main" serial number**

#### `0x7c, 0x80, 0x00`: **Get trace ID "sub" serial number**

#### `0x7d, 0x80, 0x10`: **Get next ID**

#### `0x7e`: **Set DS2401 identifiers**

#### `0x7f`: **Unknown**

#### `0xf0`: **Reset master calendar**

## BIOS

The System 573 BIOS is based on a slightly modified version of Sony's standard
PS1 kernel, plus a custom shell executable.

- [Shell revisions](#shell-revisions)
- [Kernel differences](#kernel-differences)
- [Boot sequence](#boot-sequence)
- [Command-line arguments](#command-line-arguments)
- [JVS MCU test sequence](#jvs-mcu-test-sequence)
- [DVD-ROM support](#dvd-rom-support)
- [Scrapped CF card support](#scrapped-cf-card-support)
- [BIOS mod boards](#bios-mod-boards)

### Shell revisions

There seem to be either three or four different versions of the BIOS, all of
which share the same kernel but feature different shells:

| ROM marking | MAME ROM name         | SHA-1                                      | Used by                       |
| :---------- | :-------------------- | :----------------------------------------- | :---------------------------- |
| `700A01`    | `700a01.22g`          | `e1284add4aaddd5337bd7f4e27614460d52b5b48` | Most games                    |
| `700A01`    | `700a01,gchgchmp.22g` | `9aab8c637dd2be84d79007e52f108abe92bf29dd` | Gachagachamp                  |
| `700A01`    |                       |                                            | Unknown (undumped, see below) |
| `700B01`    | `700b01.22g`          | `a2421d0a494892c0e71003c96995ce8f945064dd` | Dancing Stage EuroMIX 2       |

`700A01` is the earliest and most common version. The only difference between
the two known variants of it is that they were linked to slightly different Sony
SDK releases; Konami's own code is identical across the two. There reportedly is
a third variant that shipped on systems that came with the JVS MCU unpopulated
(presumably it would skip the check for it), however no evidence of its
existence has ever been found. The shell is stored in ROM in both variants at
`0xbfc40000`, in the form of a standard PS1 executable (including the header)
that gets loaded at `0x803c0000` by the kernel.

`700B01` has a more complicated structure: it is split up into two separate
executables, one (at `0xbfc28000`, loaded at `0x80010000`) in charge of running
the self-test sequence and the other (at `0xbfc60000`, loaded at `0x80380000`)
handling CD-ROM or flash booting. The overall coding style suggests that it was
developed alongside the installers/launchers used by later Bemani games, but
dropped as the main feature it would have introduced over the `700A01` shell -
CF card support - was broken due to a PCB wiring mistake.

### Kernel differences

The kernel in both the `700A01` and `700B01` shells identifies itself as
`Konami OS by T.H.` with a 1995-09-01 build date. All other Konami PS1-based
arcade boards, with the exception of the Twinkle System, use a kernel with the
same identifier and date (but potentially different code). The kernels used by
other manufacturers' arcade boards also contain the same `T.H.` initials,
possibly hinting at the fact there was a single Sony employee in charge of
providing customized kernels to all arcade system manufacturers.

While the 573's kernel is functionally identical to its retail counterpart
(aside from its lack of support for the PS1's CD-ROM drive), several parts of it
have been slightly tweaked to account for the hardware:

- Most CD-ROM APIs and the ISO9660 filesystem driver seem to have been purged.
- The code to parse `SYSTEM.CNF` and launch the boot executable from the CD-ROM
  has been made inaccessible. The shell handles executable loading and booting
  executables on its own, without ever returning to the kernel.
- The kernel initializes the EXP1 region and clears the watchdog periodically
  while booting. It does *not* keep clearing it in the background (e.g. from the
  exception handler) once the shell is loaded.
- `700B01` performs a "memory initialization" sequence that fills various RAM
  areas with pseudorandom values (possibly for heap debugging purposes), showing
  `c1` through `c7` on the debugging board's 7-segment display in the process.
- `700B01` reads register `0x1f40000e` to determine which RAM footprints on the
  board are populated, then configures the main RAM controller accordingly.
- The GPU is reset and a series of color bars is displayed while the shell is
  being relocated to RAM. This feature is also present in other non-retail
  kernels such as the DTL-H2000's.
- The shell executable is launched through a stub that contains a
  `Lisenced by Sony Computer Entertainment Inc.(SCEI)` (sic) string, validated
  by the kernel in a similar (but not identical) way to PS1 expansion port ROMs.

### Boot sequence

All variants of the shell are far simpler than their PS1 counterparts, as they
lack any kind of UI (aside from a non-interactive status screen) and have *no*
*copy protection or anti-piracy checks* of any kind. Once loaded by the kernel,
they start by initializing the system bus and proceed to run a hardware
self-test. The outcome of all checks is displayed on screen, with the following
ones being performed:

- `22G`: BIOS ROM integrity check. A checksum is calculated and compared to the
  one stored at the end of the ROM;
- `16H`, `16G`, `14H`, `14G`: main RAM read/write test (first row of chips on
  the board, closest to the CPU);
- `12H`, `12G`, `9H`, `9G`: main RAM read/write test (second row of chips on the
  board, closest to the JAMMA connector);
- `4L`, `4P`: VRAM read/write test. This causes the 573 to briefly display
  random pixels as framebuffers are overwritten during the check;
- `10Q`: SPU RAM read/write test;
- `18E`: JVS MCU reset and status check;
- `CDR`: ATAPI CD-ROM drive initialization and executable loading.

**NOTE**: `700A01` shells do not actually test `4P`! The GPU starts up in 1 MB
VRAM mode by default and the shell does not enable the chip select for the
second bank, so the first VRAM chip is tested twice instead. This bug was fixed
in the `700B01` shell, which initializes the GPU correctly.

If any check fails the shell locks up, shows a blinking "HARDWARE ERROR...
RESET" prompt and stops clearing the watchdog after a few seconds, causing the
573 to reboot. Otherwise, the state of DIP switch 4 is checked and the shell
attempts to load an executable from four different sources in the following
order:

- PCMCIA flash card in slot 2 (if inserted and DIP switch 4 is on);
- PCMCIA flash card in slot 1 (if inserted and DIP switch 4 is on);
- Internal flash memory (if DIP switch 4 is on);
- `PSX.EXE` in the root directory of the disc inserted in the CD-ROM drive. The
  drive is only initialized after booting from flash or PCMCIA fails or if DIP
  switch 4 is off, thus the shell will not error out if a drive is not connected
  but a boot executable is present on the flash. Note that the drive must be set
  up as an IDE primary/master device using the appropriate jumpers.

As with Sony's PS1 shell, the 573 shell's ISO9660 filesystem driver only
implements a minimal subset of the specification and may not properly support
non-8.3 file names. It also **only allocates 2 KB for the disc's path table**,
so the total number of directories on the disc must be kept to a minimum in
order to prevent the shell from crashing. Unlike the PS1, however, the 573
ignores `SYSTEM.CNF` completely regardless of whether or not it is present on
the disc; the shell is hardcoded to always load `PSX.EXE`. Homebrew discs can
take advantage of this behavior to provide separate PS1 and 573 executables
instead of detecting the system type at runtime.

If DIP switch 4 is on, the shell expects to find a standard PS1 executable
(including the full 2048-byte header) at offset `0x24` on either the built-in
flash memory or one of the two PCMCIA flash cards, preceded by a CRC32 checksum
of it at offset `0x20`. The CRC is stored in little endian format and is *not*
calculated on the whole executable, but rather only on bytes whose offsets are a
power of two (i.e. on bytes at `0x24 + 0`, `0x24 + 1`, `0x24 + 2`, `0x24 + 4`
and so on). The check is implemented as follows:

```c
#define EXE_CRC32_POLYNOMIAL 0xedb88320 // 0x04c11db7 bit-reversed

uint32_t exe_crc32(const uint8_t *data, size_t length) {
    size_t   offset = 0;
    uint32_t crc    = 0xffffffff;

    while (offset < length) {
        crc ^= data[offset];

        for (int bit = 8; bit; bit--) {
            uint16_t temp = crc;

            crc >>= 1;
            if (temp & 1)
                crc ^= EXE_CRC32_POLYNOMIAL;

            if (offset)
                offset <<= 1;
            else
                offset = 1;
        }
    }

    return ~crc;
}

#define DIP_SWITCH_PTR    ((const uint32_t *) 0x1f400004)
#define EXE_CRC32_PTR     ((const uint32_t *) 0x1f000020)
#define EXE_HEADER_PTR    ((const uint8_t  *) 0x1f000024)
// Offset of the "text section size" field within the executable header
#define EXE_TEXT_SIZE_PTR ((const uint32_t *) 0x1f000040)

bool is_exe_valid(void) {
    if (*DIP_SWITCH_PTR & (1 << 3)) // 1 = DIP switch off
        return false;
    if (memcmp(EXE_HEADER_PTR, "PS-X EXE", 8))
        return false;

    size_t   length = 2048 + *EXE_TEXT_SIZE_PTR;
    uint32_t crc    = exe_crc32(EXE_HEADER_PTR, length);

    return (crc == *EXE_DATA_PTR);
}
```

Installing a new game usually involves inserting the installation disc and
turning off DIP switch 4 in order to prevent the shell from booting the game
currently installed on the internal flash.

### Command-line arguments

PS1 executables are generally launched with CPU registers `$a0` and `$a1` set to
zero, in order to make sure programs that interpret them as `argc` and `argv`
respectively will not crash by trying to parse invalid data. The `700A01` shell
follows this convention.

The `700B01` shell, however, does pass two arguments to the executable it loads.
`$a0` is thus set to 2, while `$a1` is set to point to an array containing
pointers to the following strings:

- `boot.rom=700B01`
- `boot.from=<device>`, where `<device>` is one of the following:
  - `flash.0` (internal flash memory)
  - `flash.1` (PCMCIA flash card in slot 1)
  - `flash.2` (PCMCIA flash card in slot 2)
  - `ata.2` (CF card in slot 2)
  - `cdrom`

The launchers used by later Bemani games use these arguments if present to
determine where to load the main game executable from, and fall back to
autodetecting the game's installation location otherwise.

### JVS MCU test sequence

The JVS MCU check is implemented in a different way between the two shell
revisions. While the `700A01` shell simply resets the MCU and validates the
status and error codes, the `700B01` self-test sequence performs 35 (!)
different checks, each validating the codes returned under different conditions.
The following tests are done:

1.  Reset MCU, clear `JVSIRDY`, ensure that:
    - status code = 0
    - error code = 3
    - `JVSIRDY` = 0
    - `JVSDRDY` = 0
    - incoming JVS data = `0x0000`
2.  Reset MCU, write valid dummy packet header (`0x00e0`), ensure that:
    - status code = 2
    - error code = 3
3.  Reset MCU, write invalid dummy packet header (`0x001f`), ensure that:
    - status code = 2
    - error code = 2
4.  Reset MCU, write 16 dummy packets (`0x1fe0`, `0x0004`, `1 << i`, checksum),
    for each packet ensure that:
    - status code = 1
    - error code = 3
5.  Reset MCU, write 16 dummy packets (same as above) with an invalid checksum,
    for each packet ensure that:
    - status code = 1
    - error code = 1

It is currently unclear if any data is actually sent to the JVS bus during step
4, as the shell may reset the MCU it before it starts sending the packet.

### DVD-ROM support

Even though neither of the shell versions was explicitly designed with DVD-ROM
support in mind, it *is* possible to run games from a DVD-ROM thanks to the fact
that the ATAPI commands used by the shell and games to read sectors from the
disc are medium-agnostic. Games that rely on CD-DA playback obviously cannot be
put on a DVD, however all other games (including ones that rely on the digital
I/O board for MP3 playback) will work as long as the disc is formatted as if it
were a typical 573 CD-ROM (ISO9660 with no extensions, no UDF, 8.3 file names
and a path table smaller than 2 KB).

**NOTE**: due to ATAPI incompatibility issues only a very limited number of
DVD-ROM drives will actually be recognized and work properly with the shells and
games. This is unrelated to the DVD format itself and is purely due to the fact
that, unlike CD-ROM drives, most DVD drives were manufactured after the ATAPI
specification got updated in a way that broke the 573's compatibility.

This accidental capability was greatly abused by bootleg Bemani "superdiscs"
that bundled multiple games on a single DVD-ROM and shipped with a modified
installation menu, allowing the user to pick which game to install. Each game on
a superdisc is patched to load its files from a subdirectory rather than from
the DVD's root.

Homebrew 573 software can be distributed as an ISO9660 image larger than 650 MB
meant to be burned to a DVD-R, if sacrificing PS1 compatibility and CD-DA
support is an option. In such case the image shall be distributed as an `.iso`
file with 2048-byte sectors, rather than the typical `.bin` and `.cue` file pair
used for PS1 games with 2352-byte Mode 2 sectors.

### Scrapped CF card support

In addition to booting from "linear" memory mapped PCMCIA flash cards, the
`700B01` shell features a driver for CF cards and a FAT filesystem parser that
allows it to mount a CF card inserted in PCMCIA slot 2 (via a passive
CF-to-PCMCIA adapter), search for a flash card image file and interpret its
contents as if it were an actual flash card, loading the executable directly
from it. Or at least, that *would* allow it to do so, had Konami not screwed up
the wiring of the PCMCIA slots.

CF cards can operate in three different interfacing modes: memory mapped, I/O
mapped and IDE compatibility mode. On the 573 only memory mapped mode is
accessible as the other modes require usage of I/O chip select pins that are not
connected. This mode, however, requires the host to issue 8-bit writes to the
card's 16-bit bus through the use of individual chip select lines for each byte
(`/CE1` and `/CE2`). While the PS1's CPU *does* have separate lower (`/WR0`) and
upper (`/WR1`) byte write strobes that could have been easily adapted to the
appropriate signals, Konami decided to cut this specific corner and shorted
`/CE1` and `/CE2` on each PCMCIA slot together, making it impossible to issue a
single-byte write.

**NOTE**: later revisions of the 573 main board seem to have unpopulated jumpers
next to the PCMCIA slots that can be used to rewire the chip select signals. It
is currently unclear if these jumpers are actually sufficient to enable CF card
booting without any additional hardware or BIOS modifications.

### BIOS mod boards

It is not uncommon to find 573s fitted with a bootleg BIOS "mod board" in place
of the stock `700A01` or `700B01` mask ROM. These boards used to be bundled
alongside bootleg game CD-ROMs and were apparently required in order to bypass
the "anti-piracy checks" in Konami's BIOS.

Of course, since neither version of the shell has any such checks, the claims
were completely misleading. The actual purpose of these boards was not to tamper
with the BIOS, but rather to piggyback on the system bus and provide a crude
authentication mechanism to the bootleg game, allowing it to verify that it was
indeed running on a 573 equipped with an appropriate mod board. In other words,
**mod boards were actually the bootleggers' implementation of Konami's**
**security cartridge system**, meant to prevent people from simply burning
copies of a bootleg CD-ROM and forcing them to buy bootleg kits from whoever
produced them instead. *Oh the irony.*

The added authentication circuitry will not create any issues with official nor
homebrew software, however most of these boards feature an additional party
trick: *the shell executable is altered to load a differently named executable*,
making bootleg discs unable to boot on a stock 573 and vice versa. The following
names have been found so far in modified BIOS ROMs:

- `QSY.DXD`
- `SSW.BXF`
- `TSV.AXG`
- `GSE.NXX`
- `NSE.GXX`

The following names have been found on unofficial game discs, but are not
confirmed to have ever been used in modified BIOS ROMs:

- `OSE.FXX`
- `QSU.DXH`
- `QSX.DXE`
- `QSZ.DXC`
- `RSU.CXH`
- `RSV.CXG`
- `RSW.CXF`
- `RSZ.CXC`
- `SSX.BXE`
- `SSY.BXD`
- `TSW.AXF`
- `TSX.AXE`
- `TSY.AXD`
- `TSZ.AXC`

Homebrew software should thus place multiple copies of the boot executable on
the CD-ROM to ensure any BIOS, modded or not, can successfully load it. An
interesting side note is that, for any of these names, summing the ASCII codes
of each character will always yield the same result. Presumably bootleggers were
unable to find the code in charge of BIOS ROM checksum validation and found it
easier to just turn the string into random nonsense whose checksum collided with
the original one.

## Game-specific information

### Black case I/O connectors

Fisherman's Bait and a few other non-Bemani games use a 573 housed in a black
case with blue front and back panels. Unlike the gray metal cases used by other
games, this case model has no cutouts for removable front and back panels that
hold game-specific connectors and instead has a fixed set of ports exposed:

- **Power**: 2x4 Molex connector that can be used as a power input or output,
  wired to `CN17`.
- **Option 1**: DE9 connector providing four analog inputs, wired to `CN3` on
  the main board.
- **Option 2**: DE9 connector providing six button (digital) inputs, of which
  four are also exposed on the JAMMA connector. Wired to `CN5` on the
  motherboard.
- **Reel connector** (back side): 3x3 Molex connector wired to the
  `GE765-PWB(B)A` fishing controller I/O board. Probably missing on systems that
  that did not come with Fisherman's Bait.

### DDR I/O connectors

Dance Dance Revolution uses a 573 enclosed in a gray metal case, with either an
analog or digital I/O board installed. The front panel has a cutout covered by a
metal plate, which in turn holds the following connectors:

- **1P** (10-pin white, only 7 pins used): connects to the left stage and
  controls arrow lights, in addition to being used for bitbanged communication
  with the stage PCB. Wired to light bank A on the I/O board.
- **2P** (10-pin orange, only 7 pins used): same as above for the right stage.
  Wired to light bank B on the I/O board.
- Unlabeled (10-pin red, only 7 pins used): connects to cabinet button and
  marquee lights. Wired to light bank C.
- Unlabeled (6-pin white, only 2 pins used): controls the inverter that drives
  the neon rings around the speakers. Wired to light bank D.

The back panel has a similar cutout, covered by a plate with holes for the
digital I/O board's RCA networking jacks.

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

First-generation DrumMania cabinets have lights wired up to the I/O board as
follows:

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

The wiring was changed in later cabinets, which use the following mapping
instead:

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

## Notes

- [Homebrew guidelines](#homebrew-guidelines)
- [Missing support for PAL mode](#missing-support-for-pal-mode)
- [Flash chips and PCMCIA cards](#flash-chips-and-pcmcia-cards)
- [Known working replacement PCMCIA cards](#known-working-replacement-pcmcia-cards)
- [Known working replacement drives](#known-working-replacement-drives)
- [Bemani launcher error and status codes](#bemani-launcher-error-and-status-codes)

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
  system type at runtime. Additional copies of `PSX.EXE` with the file names
  commonly used by BIOS mod boards (`QSY.DXD`, `TSV.AXG` and so on) shall also
  be present.
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

### Flash chips and PCMCIA cards

The PCMCIA flash cards required by most 573 games are "linear" (memory mapped)
cards consisting of one or more parallel flash memory chips wired directly to
the bus, rather than CF or ATA-compatible cards. As neither linear cards nor
parallel flash command sets are fully standardized, working with these cards may
be difficult without some prior knowledge.

There are two main variants of such cards:

- **8-bit**: these contain one or more pairs of flash chips with an 8-bit data
  bus each. Each pair has one chip wired to the lower byte of the data bus and
  the other wired to the upper byte. Commands must thus be issued to both chips
  at once by repeating the command byte (e.g. writing `0x9090` to issue the
  `0x90` JEDEC ID command). Issuing 8-bit writes to a single chip is *not*
  supported on the 573 due to the way chip select lines are wired up; see the
  BIOS CF card support section for more details.
- **16-bit**: these contain flash chips with a native 16-bit bus. The chips are
  simply mapped next to each other within the card's address space.

Konami's flash driver only supports 8-bit cards that use one of the following
chips:

| Manufacturer | Chip       | Capacity | Manuf. ID | Device ID |
| :----------- | :--------- | -------: | :-------- | :-------- |
| Fujitsu      | MBM29F016A |     2 MB | `0x04`    | `0xad`    |
| Fujitsu      | MBM29F017A |     2 MB | `0x04`    | `0x3d`    |
| Fujitsu      | MBM29F040A |   512 KB | `0x04`    | `0xa4`    |
| Intel        | 28F016S5   |     2 MB | `0x89`    | `0xaa`    |
| Sharp        | LH28F016S  |     2 MB | `0x89`    | `0xaa`    |

Most games, including the launchers used by later Bemani games, will check the
JEDEC IDs of the cards' chips on startup and **reject any unsupported chip,**
**even if valid game data is otherwise present on the card**. This makes it
impossible to manually install a game onto an unsupported card (e.g. through
homebrew tools) without also patching the launcher in order to skip the check.

The 573 main board seems to always be fitted with either MBM29F016A or LH28F016S
chips. The internal flash memory is accessed using the same driver as the flash
cards and has the same caveats (having to issue commands to two chips at once
and so on).

### Known working replacement PCMCIA cards

This is an incomplete list of PCMCIA flash cards that are known to work, or not
to work, with Konami's flash driver. Due to the JEDEC ID checks, only cards that
contain flash chips listed in the previous section will work.

| Manufacturer   | Model                                | Flash chips    | Capacity | Bus type | Manuf. ID | Device ID | Working | Notes                                                                     |
| :------------- | :----------------------------------- | :------------- | -------: | -------: | :-------- | :-------- | :------ | :------------------------------------------------------------------------ |
| Centennial     | PM24265, FL32M-20-\*-67              | 16x 28F016S5   |    32 MB |    8-bit | `0x8989`  | `0xaaaa`  | **Yes** |                                                                           |
| ~~Centennial~~ | ~~PM24276, FL32M-20-\*-J5-03~~       | 4x 28F640J5    |    32 MB |   16-bit | `0x0089`  | `0x0015`  | No      |                                                                           |
| ~~Centennial~~ | ~~PM24282, FL32M-20-\*-S5-03~~       | 16x AM29F016   |    32 MB |    8-bit | `0x0101`  | `0xadad`  | No      | Same command set as Fujitsu cards, may work with minimal game patching    |
| Fujitsu        | "32MB Flash Card" (no model number?) | 16x MBM29F016A |    32 MB |    8-bit | `0x0404`  | `0xadad`  | **Yes** | Stock card (Konami sticker covers Fujitsu logo)                           |
| Fujitsu        | "32MB Flash Card" (no model number?) | 16x MBM29F017A |    32 MB |    8-bit | `0x0404`  | `0x3d3d`  | **Yes** | Stock card (Konami sticker covers Fujitsu logo)                           |
| Sharp          | ID245G01                             | 4x LH28F016S   |     8 MB |    8-bit | `0x8989`  | `0xaaaa`  | **Yes** | Stock card (Konami sticker covers Sharp logo), used by GunMania Zone Plus |
| Sharp          | ID245P01                             | 16x LH28F016S  |    32 MB |    8-bit | `0x8989`  | `0xaaaa`  | **Yes** | Stock card (Konami sticker covers Sharp logo)                             |

Note that most of these cards have identical labels and can typically only be
told apart from the model number printed on the bottom side or one of the edges.

### Known working replacement drives

This is an incomplete list of drives that are known to work, or to be
incompatible, with the ATAPI driver Konami used in the BIOS shell and games. The
driver was likely written using an old version of the ATAPI specification as a
reference; CD-ROM drives manufactured in the late 1990s and very early 2000s
have a higher chance of being compatible than drives manufactured later,
possibly due to changes introduced in later revisions of the ATAPI specification
that broke the assumptions Konami's driver makes.

CD-DA playback is particularly problematic as Konami's code seems to be unable
to handle the subtle implementation differences across different drives. To add
insult to injury, some of the few drives that *do* work have bugs in their
subchannel handling that result in incorrect playback status data being reported
to the 573, completely breaking pre-digital-I/O Bemani titles that rely heavily
on audio timing.

| Manufacturer         | Known rebrands | Model          | Type | BIOS    | CD-DA   | Notes                               |
| :------------------- | :------------- | :------------- | :--- | :------ | :------ | :---------------------------------- |
| ASUSTeK              |                | DVD-E616P3     | DVD  | **Yes** | Unknown |                                     |
| Compaq               |                | CRN-8241B      | CD   | **Yes** | **Yes** | Laptop drive, has CD-DA sync issues |
| Creative             |                | CD4832E        | CD   | **Yes** | No      |                                     |
| Hitachi              |                | CDR-7930       | CD   | **Yes** | No      |                                     |
| LG                   | Compaq         | CRD-8400B      |      | **Yes** | Unknown |                                     |
| LG                   |                | GCE-8160B      | CD   | **Yes** | No      |                                     |
| LG                   |                | GCR-8523B      | CD   | **Yes** | Unknown |                                     |
| LG                   |                | GCR-8525B      | CD   | **Yes** | **Yes** | Has CD-DA sync issues               |
| LG                   |                | GDR-8163B      | DVD  | **Yes** | **Yes** |                                     |
| LG                   | HP             | GDR-8164B      | DVD  | **Yes** | **Yes** |                                     |
| LG                   |                | GH22LP20       | DVD  | **Yes** | Unknown |                                     |
| LG                   |                | GH22NP20       | DVD  | **Yes** | Unknown |                                     |
| ~~LG~~               |                | ~~GSA-4165B~~  | DVD  | No      |         |                                     |
| LG                   |                | GWA-4166B      | DVD  | **Yes** | Unknown |                                     |
| Lite-On              |                | DH-20A4P       |      | **Yes** | Unknown |                                     |
| Lite-On              |                | LH-18A1H       | DVD  | **Yes** | **Yes** |                                     |
| Lite-On              |                | LTD-163        | DVD  | **Yes** | Unknown |                                     |
| Lite-On              |                | LTD-165H       | DVD  | **Yes** | Unknown |                                     |
| Lite-On              |                | LTR-40125S     | CD   | **Yes** | Unknown |                                     |
| Lite-On              |                | SHW-160P6S     | DVD  | **Yes** | Unknown |                                     |
| Lite-On              |                | SOHR-48327S    |      | **Yes** | Unknown |                                     |
| Lite-On              | HP             | SOHR-4839S     | CD   | **Yes** | Unknown | Jitters on CD-RW                    |
| Lite-On              |                | XJ-HD166S      | DVD  | **Yes** | Unknown |                                     |
| Matsushita/Panasonic |                | CR-583         | CD   | **Yes** | **Yes** | Stock drive                         |
| Matsushita/Panasonic |                | CR-587         | CD   | **Yes** | **Yes** | Stock drive, can't read CD-R        |
| Matsushita/Panasonic |                | CR-589B        | CD   | **Yes** | **Yes** | Stock drive                         |
| Matsushita/Panasonic |                | CR-594C        | CD   | **Yes** | Unknown |                                     |
| Matsushita/Panasonic | HP             | SR-8585B       | DVD  | **Yes** | Unknown |                                     |
| Matsushita/Panasonic |                | SR-8589B       | DVD  | **Yes** | Unknown |                                     |
| Matsushita/Panasonic |                | UJDA770        |      | **Yes** | Unknown | Laptop drive                        |
| Mitsumi              |                | CRMC-FX4830T   | CD   | **Yes** | Unknown |                                     |
| NEC                  |                | CDR-1900A      | CD   | **Yes** | Unknown |                                     |
| ~~NEC~~              |                | ~~ND-2510A~~   | DVD  | No      |         |                                     |
| Sony                 | Compaq         | CDU701-Q1      | CD   | **Yes** | Unknown |                                     |
| Sony                 |                | CRX217E        | CD   | **Yes** | Unknown |                                     |
| Sony                 |                | DRU-510A       | DVD  | **Yes** | Unknown |                                     |
| Sony                 |                | DRU-810A       | DVD  | **Yes** | Unknown |                                     |
| TDK                  |                | AI-CDRW241040B | CD   | **Yes** | Unknown |                                     |
| TDK                  |                | AI-481648B     | CD   | **Yes** | Unknown |                                     |
| TEAC                 |                | CD-W552E       | CD   | **Yes** | Unknown |                                     |
| Toshiba              |                | SW-252         |      | **Yes** | Unknown |                                     |
| Toshiba              |                | TS-H292C       | CD   | **Yes** | Unknown |                                     |
| Toshiba              |                | XM-5702B       | CD   | **Yes** | Unknown |                                     |
| Toshiba              |                | XM-6102B       | CD   | **Yes** | **Yes** | Stock drive                         |
| Toshiba              |                | XM-7002B       | CD   | **Yes** | Unknown | Stock drive, laptop drive           |

**NOTE**: Konami shipped some units with a Toshiba XM-7002B laptop drive and a
passive adapter board (`GX874-PWB(B)`) to break out the drive's signals to a
regular 40-pin IDE connector. Laptop drives were also used by Konami in the
`GXA25-PWB(A)` multisession unit.

### Bemani launcher error and status codes

The installers and launchers used by Bemani titles that require the digital I/O
board have an extensive error and status reporting system. Launcher messages are
easily recognizable as they are always displayed in a blue window and have a
3-digit status code, however Japanese versions of the games will show them in
Japanese with no way to switch language (short of patching the launcher; all
launcher variants contain both English and Japanese strings).

Below is a list of all messages from launcher version 1.95 in both English and
Japanese, along with the respective status codes and indices in the launcher's
internal message array.

| Index | Type  | Status codes  | Description (English)                                                                                                                                                                                                                                                | Description (Japanese) |
| ----: | :---- | :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
|     0 | Error | 100           | <pre>Boot is not available from this device.<br />DEVICE=%s1</pre>                                                                                                                                                                                                   | <pre lang="ja">このデバイスからのブートはできません.<br />DEVICE=%s1</pre> |
|     1 | Error | 101           | <pre>Digital Sound PCB intialization failed.</pre>                                                                                                                                                                                                                   | <pre lang="ja">デジタルサウンド基板の初期化に失敗しました.</pre> |
|     2 | Error | 102           | <pre>Digital Sound PCB ROM error.</pre>                                                                                                                                                                                                                              | <pre lang="ja">デジタルサウンド基板ROMエラー.</pre> |
|     4 | Error | 104           | <pre>CD-ROM initialization failed.</pre>                                                                                                                                                                                                                             | <pre lang="ja">CD-ROMドライブの初期化に失敗しました.</pre> |
|     7 | Error | 107           | <pre>File system mounting failed.<br />Please check that correct CD-ROM is in use.</pre>                                                                                                                                                                             | <pre lang="ja">ファイルシステムのマウントに失敗しました.<br />CD-ROMが間違っていないか確認してください.</pre> |
|     9 | Error | 109           | <pre>File system mounting failed.<br />Please check that correct CD-ROM is in use.</pre>                                                                                                                                                                             | <pre lang="ja">ファイルシステムのマウントに失敗しました.<br />CD-ROMが間違っていないか確認してください.</pre> |
|    10 | Error | 110           | <pre>File system mounting failed.<br />Please check that correct CD-ROM is in use.</pre>                                                                                                                                                                             | <pre lang="ja">ファイルシステムのマウントに失敗しました.<br />CD-ROMが間違っていないか確認してください.</pre> |
|    11 | Error | 111           | <pre>File system mounting failed.<br />Please check that correct CD-ROM is in use.</pre>                                                                                                                                                                             | <pre lang="ja">ファイルシステムのマウントに失敗しました.<br />CD-ROMが間違っていないか確認してください.</pre> |
|    12 | Error | 112           | <pre>File system mounting failed.<br />Please check that correct CD-ROM is in use.</pre>                                                                                                                                                                             | <pre lang="ja">ファイルシステムのマウントに失敗しました.<br />CD-ROMが間違っていないか確認してください.</pre> |
|    13 | Error | 113           | <pre>Disc device initialization failed.</pre>                                                                                                                                                                                                                        | <pre lang="ja">ディスクデバイスの初期化に失敗しました.</pre> |
|    14 | Error | 114           | <pre>You are using an incorrect CD-ROM.<br />Replace CD-ROM to %s1 and<br />turn on the main power.</pre>                                                                                                                                                            | <pre lang="ja">CD-ROMが違います.<br />CD-ROMを%s1に交換し,電源を<br />入れ直してください.</pre> |
|    15 | Error | 115           | <pre>Disc device initialization failed.</pre>                                                                                                                                                                                                                        | <pre lang="ja">ディスクデバイスの初期化に失敗しました.</pre> |
|    16 | Error | 116           | <pre>Disc device initialization failed.</pre>                                                                                                                                                                                                                        | <pre lang="ja">ディスクデバイスの初期化に失敗しました.</pre> |
|    17 | Error | 117           | <pre>Config file error.<br />FILE=%s1<br />ERROR=%d2, LINE=%d3, COLUMN=%d4</pre>                                                                                                                                                                                     | <pre lang="ja">コンフィグファイルエラー.<br />FILE=%s1<br />ERROR=%d2, LINE=%d3, COLUMN=%d4</pre> |
|    19 | Error | 119           | <pre>You are using an incorrect CD-ROM.<br />Replace CD-ROM to %s1 and<br />turn on the main power.</pre>                                                                                                                                                            | <pre lang="ja">CD-ROMが違います.<br />CD-ROMを%s1に交換し,電源を<br />入れ直してください.</pre> |
|    20 | Error | 120           | <pre>Cassette is not installed.<br />Turn off the main power and install the<br />correct cassette then turn the power on.</pre>                                                                                                                                     | <pre lang="ja">カセットがセットされていません.<br />電源を切り,正しいカセットをセットして<br />再度電源を入れてください.</pre> |
|    21 | Error | 121           | <pre>Cassette error. (%d1)<br />Cassette does not match this game.<br />Check if the cassette is for this<br />game (%s2)<br />Refer to manual for more information.</pre>                                                                                           | <pre lang="ja">カセットエラー (%d1)<br />ゲームとカセットが対応していません.<br />カセットがこのゲーム(%s2)用のものか<br />確認してください.<br />詳しくは取り扱い説明書を参照してください.</pre> |
|    25 | Error | 125           | <pre>Boot is not available from this device.<br />DEVICE=%s1</pre>                                                                                                                                                                                                   | <pre lang="ja">このデバイスからゲームのブートはできません.<br />DEVICE=%s1</pre> |
|    26 | Error | 126           | <pre>Cassette error (%d1)</pre>                                                                                                                                                                                                                                      | <pre lang="ja">カセットエラー (%d1)</pre> |
|    27 | Error | 127           | <pre>Master Calendar network error.</pre>                                                                                                                                                                                                                            | <pre lang="ja">マスターカレンダー通信エラー.</pre> |
|    28 | Error | 128           | <pre>Master Calendar network error.</pre>                                                                                                                                                                                                                            | <pre lang="ja">マスターカレンダー通信エラー.</pre> |
|    29 | Error | 129           | <pre>Master Calendar network error.</pre>                                                                                                                                                                                                                            | <pre lang="ja">マスターカレンダー通信エラー.</pre> |
|    30 | Error | 130           | <pre>Installation boot device error.<br />Installation cassette is inserted.<br />Turn off the power.  Before turning the<br />power on:  1. Change the cassette to the<br />Operating Cassette to enter the game or<br />2. Set DIP-SW4 to "OFF" to install.</pre>  | <pre lang="ja">インストールブートデバイスエラー.<br />インストールカセットがセットされています.<br />電源を切り,ゲームを行うには運用カセットに<br />交換, インストールするにはDIP-SW4をOFFに<br />し,再度電源を入れてください.</pre> |
|    31 | Error | 131           | <pre>Installation Cassette does not correspond<br />to the machine.<br />Please use Installation Cassette marked<br />%s1 for installation.</pre>                                                                                                                    | <pre lang="ja">インストールカセットと本体との対応がとれて<br />いません. 認証番号%s1が記入された<br />インストールカセットを用いてインストール<br />してください.</pre> |
|    32 | Error | 132           | <pre>Cassette error (%d1)</pre>                                                                                                                                                                                                                                      | <pre lang="ja">カセットエラー (%d1)</pre> |
|    35 | Error | 135           | <pre>This cassette is used to convert another<br />game. This can not be used as an operating<br />cassette.</pre>                                                                                                                                                   | <pre lang="ja">このカセットはいちど次機種への<br />コンバージョンに使用されたものです.<br />運用カセットとして使用することはできません.</pre> |
|    36 | Error | 136           | <pre>Cassette error (%d1)</pre>                                                                                                                                                                                                                                      | <pre lang="ja">カセットエラー (%d1)</pre> |
|    38 | Error | 138           | <pre>File not found.<br />FILE=%s1</pre>                                                                                                                                                                                                                             | <pre lang="ja">ファイルが見つかりません.<br />FILE=%s1</pre> |
|    39 | Error | 139           | <pre>File reading error.<br />FILE=%s1</pre>                                                                                                                                                                                                                         | <pre lang="ja">ファイルリードエラー.<br />FILE=%s1</pre> |
|    40 | Error | 140           | <pre>File not found.<br />FILE=%s1</pre>                                                                                                                                                                                                                             | <pre lang="ja">ファイルが見つかりません.<br />FILE=%s1</pre> |
|    41 | Error | 141           | <pre>File reading error.<br />FILE=%s1</pre>                                                                                                                                                                                                                         | <pre lang="ja">ファイルリードエラー.<br />FILE=%s1</pre> |
|    42 | Error | 142           | <pre>File reading error.<br />FILE=%s1</pre>                                                                                                                                                                                                                         | <pre lang="ja">ファイルリードエラー.<br />FILE=%s1</pre> |
|    43 | Error | 143           | <pre>File reading error.<br />FILE=%s1</pre>                                                                                                                                                                                                                         | <pre lang="ja">ファイルリードエラー.<br />FILE=%s1</pre> |
|    44 | Error | 144           | <pre>File data error.<br />FILE=%s1</pre>                                                                                                                                                                                                                            | <pre lang="ja">ファイルデータエラー.<br />FILE=%s1</pre> |
|    45 | Error | 145           | <pre>File data error.<br />FILE=%s1</pre>                                                                                                                                                                                                                            | <pre lang="ja">ファイルデータエラー.<br />FILE=%s1</pre> |
|    46 | Error | 146           | <pre>Turn off the power and check if the Flash<br />Card is inserted properly.<br />Please turn the power on after checking.<br />DEVICE=%s1</pre>                                                                                                                   | <pre lang="ja">電源を切り, フラッシュカードが正しくセット<br />されているか確認してください. 準備が整って<br />から再び電源を入れてください.<br />DEVICE=%s1</pre> |
|    47 | Error | 147           | <pre>Checksum error.  If you have the latest<br />CD-ROM, please replace.  Turn off the<br />power and insert installation cassette.<br />Set DIP-SW4 to "OFF", then turn on the<br />power and reinstall CD-ROM.</pre>                                              | <pre lang="ja">チェックサムエラー. 最新のCD-ROMがあれば,<br />それに交換してください. 電源を切り,インス<br />トールカセットに交換,DIP-SW4をOFFにして<br />電源を入れ,再インストールしてください.</pre> |
|    48 | Error | 148           | <pre>Area specification error.<br />Only area specification below is available.<br /> %s1<br />Check the DIP-SW of Master Calendar.</pre>                                                                                                                            | <pre lang="ja">仕向地指定エラー.<br />本タイトルは次の仕向地のみ指定できます.<br /> %s1<br />マスターカレンダーのDIP-SWを確認して<br />ください.</pre> |
|    49 | Error | 149           | <pre>Cassette initialization error.<br />The cassette is already initialized as<br />Operating Cassette (%s1)<br />Reinitialization can not be completed.</pre>                                                                                                      | <pre lang="ja">カセット初期化エラー.<br />カセットはすでに運用カセット(%s1)<br />として初期化されています.<br />再初期化はできません.</pre> |
|    50 | Error | 150           | <pre>Cassette initialization error.<br />The cassette is already initialized as<br />Installation Cassette (%s1)<br />Reinitialization can not be completed.</pre>                                                                                                   | <pre lang="ja">カセット初期化エラー.<br />カセットはすでにインストールカセット<br />(%s1)として初期化されています.<br />再初期化はできません.</pre> |
|    51 | Error | 151           | <pre>File not found.<br />FILE=%s1</pre>                                                                                                                                                                                                                             | <pre lang="ja">ファイルが見つかりません.<br />FILE=%s1</pre> |
|    52 | Error | 152           | <pre>Turn off the power and check if the Flash<br />Card is inserted properly.<br />Please turn the power on after checking.<br />DEVICE=%s1</pre>                                                                                                                   | <pre lang="ja">電源を切り, フラッシュカードが正しくセット<br />されているか確認してください. 準備が整って<br />から再び電源を入れてください.<br />DEVICE=%s1</pre> |
|    53 | Error | 153           | <pre>Installation failed. (%d1)</pre>                                                                                                                                                                                                                                | <pre lang="ja">インストールに失敗しました (%d1)</pre> |
|    54 | Error | 154           | <pre>Assertion failed.<br />FILE=%s1<br />LINE=%d2</pre>                                                                                                                                                                                                             | <pre lang="ja">アサーションフェイル.<br />FILE=%s1<br />LINE=%d2</pre> |
|    55 | Error | 155           | <pre>Argument buffer overflow.</pre>                                                                                                                                                                                                                                 | <pre lang="ja">引数バッファオーバーフロー.</pre> |
|    56 | Error | 156           | <pre>File not found.<br />FILE=%s1</pre>                                                                                                                                                                                                                             | <pre lang="ja">ファイルが見つかりません.<br />FILE=%s1</pre> |
|    57 | Error | 157           | <pre>File data error.<br />FILE=%s1</pre>                                                                                                                                                                                                                            | <pre lang="ja">ファイルデータエラー.<br />FILE=%s1</pre> |
|    58 | Error | 158           | <pre>File reading error.<br />FILE=%s1</pre>                                                                                                                                                                                                                         | <pre lang="ja">ファイルリードエラー.<br />FILE=%s1</pre> |
|    59 | Error | 159           | <pre>Security Chip error. (%d1)<br />This Security Chip was initialized for<br />another title.</pre>                                                                                                                                                                | <pre lang="ja">セキュリティチップエラー.(%d1)<br />このセキュリティチップは他のタイトル用に<br />初期化されています.</pre> |
|    60 | Error | 160           | <pre>CD-ROM drive error</pre>                                                                                                                                                                                                                                        | <pre lang="ja">CD-ROMドライブエラー.</pre> |
|    61 | Error | 161           | <pre>RTC error</pre>                                                                                                                                                                                                                                                 | <pre lang="ja">RTCエラー.</pre> |
|    62 | Error | 162           | <pre>Specification selection error<br />Only specification below can be<br />selected for this title.<br /> %s1<br />Check the DIP-SW of machine.</pre>                                                                                                              | <pre lang="ja">商品仕様指定エラー.<br />本タイトルは次の商品仕様のみ指定できます.<br /> %s1<br />本体のDIP-SWを確認してください.</pre> |
|    64 | Error | 164           | <pre>Operating Cassette is not corresponding<br />with the machine.  Turn off the power and<br />replace it with Operating Cassette<br />No.%s1 then reboot.</pre>                                                                                                   | <pre lang="ja">運用カセットと本体との対応がとれていません.<br />電源を切り,認証番号%s1が記入された<br />運用カセットに交換して再起動してください.</pre> |
|    66 | Error | 166           | <pre>Incorrect cassette installed.</pre>                                                                                                                                                                                                                             | <pre lang="ja">不当なカセットです.</pre> |
|    67 | Error | 167           | <pre>Security Chip initialization failed. (%d1)</pre>                                                                                                                                                                                                                | <pre lang="ja">セキュリティチップ初期化エラー. (%d1)</pre> |
|    69 | Error | 169           | <pre>Cannot use this security cassette<br />as Installation Cassette.</pre>                                                                                                                                                                                          | <pre lang="ja">このセキュリティカセットはインストール<br />カセットとして使用することはできません.</pre> |
|    70 | Error | 170           | <pre>Cannot use this security cassette<br />as Installation Cassette.</pre>                                                                                                                                                                                          | <pre lang="ja">このセキュリティカセットはインストール<br />カセットとして使用することはできません.</pre> |
|    71 | Error | 171           | <pre>This version cannot initialize a cassette.<br />Please replace CD-ROM to %s1<br />for initialize, and turn off the power.<br />Set DIP-SW4 to "OFF", then turn on<br />the power.</pre>                                                                         | <pre lang="ja">このバージョンはカセットを初期化できません.<br />初期化するにはCD-ROMを%s1に<br />交換して電源を切り,DIP-SW4をOFFにして<br />再起動してください.</pre> |
|    72 | Error | 172           | <pre>You are using an incorrect CD-ROM.<br />Replace CD-ROM to %s1 and<br />turn on the main power.</pre>                                                                                                                                                            | <pre lang="ja">CD-ROMが違います.<br />CD-ROMを%s1に交換し,電源を<br />入れ直してください.</pre> |
|    73 | Error | 173           | <pre>Cannot use this security cassette.</pre>                                                                                                                                                                                                                        | <pre lang="ja">このセキュリティカセットは使用できません.</pre> |
|    74 | Error | 174           | <pre>Cannot use this security cassette.</pre>                                                                                                                                                                                                                        | <pre lang="ja">このセキュリティカセットは使用できません.</pre> |
|    75 | Error | 175           | <pre>Cassette is not corresponding with the<br />machine.  Turn off the power and<br />replace it with Cassette No.%s1<br />then reboot.</pre>                                                                                                                       | <pre lang="ja">カセットと本体との対応がとれていません.<br />電源を切り,認証番号%s1が記入された<br />カセットに交換して再起動してください.</pre> |
|    76 | Error | 176           | <pre>Cassette is not corresponding with the<br />machine.  Turn off the power and<br />replace it with Cassette No.%s1<br />then reboot.</pre>                                                                                                                       | <pre lang="ja">カセットと本体との対応がとれていません.<br />電源を切り,認証番号%s1が記入された<br />カセットに交換して再起動してください.</pre> |
|    77 | Error | 177           | <pre>Checksum error.<br />If you have the latest CD-ROM, please<br />replace.  Turn off the power and set<br />DIP-SW4 to "OFF", then turn on<br />the power and reinstall CD-ROM.</pre>                                                                             | <pre lang="ja">チェックサムエラー.<br />最新のCD-ROMがあればそれに交換してください.<br />電源を切ってDIP-SW4をOFFにしたあと,<br />電源を入れて再インストールしてください.</pre> |
|    78 | Error | 178           | <pre>This cassette is used to convert another<br />game. This can not be used to this game.</pre>                                                                                                                                                                    | <pre lang="ja">このカセットは次機種へのコンバージョンに<br />使用されたものです.<br />この機種で再び使用することはできません.</pre> |
|    79 | Error | 179           | <pre>Boot is not available from this device.<br />DEVICE=%s1</pre>                                                                                                                                                                                                   | <pre lang="ja">このデバイスからゲームのブートはできません.<br />DEVICE=%s1</pre> |
|    80 | Error | 180           | <pre>You are using an incorrect CD-ROM.<br />Replace CD-ROM to %s1 and<br />turn on the main power.</pre>                                                                                                                                                            | <pre lang="ja">CD-ROMが違います.<br />CD-ROMを%s1に交換し,電源を<br />入れ直してください.</pre> |
|    81 | Error | 181           | <pre>File system mounting failed.<br />Please check that correct CD-ROM is in use.</pre>                                                                                                                                                                             | <pre lang="ja">ファイルシステムのマウントに失敗しました.<br />CD-ROMが間違っていないか確認してください.</pre> |
|    82 | Error | 182           | <pre>File system mounting failed.<br />Please check that correct CD-ROM is in use.</pre>                                                                                                                                                                             | <pre lang="ja">ファイルシステムのマウントに失敗しました.<br />CD-ROMが間違っていないか確認してください.</pre> |
|    83 | Error | 183           | <pre>Installation boot device error.<br />Please turn off the power for installation,<br />and set DIP-SW4 to "OFF", then turn on<br />the power.</pre>                                                                                                              | <pre lang="ja">インストールブートデバイスエラー.<br />インストールするには電源を切り,DIP-SW4を<br />OFFにして再起動してください.</pre> |
|    84 | Error | 184           | <pre>CD-ROM drive error</pre>                                                                                                                                                                                                                                        | <pre lang="ja">CD-ROMドライブエラー.</pre> |
|    85 | Error | 185           | <pre>CD-ROM drive version update failed. (%d1)<br />Please call a dealer near you.</pre>                                                                                                                                                                             | <pre lang="ja">CD-ROMドライブのバージョンアップに失敗<br />しました. (%d1)<br />最寄りのサービスセンターにお問い合わせ<br />下さい.</pre> |
|    86 | Error | 186           | <pre>Cassette error (%d1)</pre>                                                                                                                                                                                                                                      | <pre lang="ja">カセットエラー (%d1)</pre> |
|    87 | Error | 187           | <pre>You are using the cassette of another<br />cabinet. Please use the correct cassette.<br />Please see details in operator's manual.</pre>                                                                                                                        | <pre lang="ja">異なる本体向けのカセットを使用しています.<br />正しい本体との組み合わせで使用してください.<br />詳しくは取り扱い説明書を参照してください.</pre> |
|    88 | Error | 188           | <pre>You are using the cassette of another<br />cabinet. Please use the correct cassette.<br />Please see details in operator's manual.</pre>                                                                                                                        | <pre lang="ja">異なる本体向けのカセットを使用しています.<br />正しい本体との組み合わせで使用してください.<br />詳しくは取り扱い説明書を参照してください.</pre> |
|    89 | Error | 189           | <pre>You are using unknown cabinet.<br />Check all connectors.<br />Please see details in operator's manual.</pre>                                                                                                                                                   | <pre lang="ja">不明な本体を使用しています.<br />各コネクタが外れていないか確認してください.<br />詳しくは取り扱い説明書を参照してください.</pre> |
|    90 | Error | 190           | <pre>You are using unknown cabinet.<br />Check all connectors.<br />Please see details in operator's manual.</pre>                                                                                                                                                   | <pre lang="ja">不明な本体を使用しています.<br />各コネクタが外れていないか確認してください.<br />詳しくは取り扱い説明書を参照してください.</pre> |
|    91 | Error | 191           | <pre>Non-applicable game installed.<br />To install this game,<br /> %s1<br />shall be installed first.</pre>                                                                                                                                                        | <pre lang="ja">異なるゲームがインストールされています.<br />このゲームをインストールするにはあらかじめ<br /> %s1<br />がインストールされている必要があります.</pre> |
|    92 | Error | 192           | <pre>This software is for the e-Amusement<br />system.<br />The game will only work on the e-Amusement<br />cabinet.</pre>                                                                                                                                           | <pre lang="ja">このゲームソフトはe-Amusement(レンタル)用<br />ソフトです.<br />e-Amusement用筐体でのみ動作します.</pre> |
|    93 | Error | 193           | <pre>This software is not for the e-Amusement<br />system.<br />The game doesn't work on the e-Amusement<br />cabinet.</pre>                                                                                                                                         | <pre lang="ja">このゲームソフトはe-Amusement(レンタル)用<br />ソフトではありません.<br />e-Amusement用筐体では動作しません.</pre> |
|    94 | Error | 194           | <pre>Non-applicable game installed.<br />To install this game,<br /> %s1<br />shall be installed first.</pre>                                                                                                                                                        | <pre lang="ja">異なるゲームがインストールされています.<br />このゲームをインストールするにはあらかじめ<br /> %s1<br />がインストールされている必要があります.</pre> |
|    95 | Error | 195           | <pre>Cassette initialization error.<br />The cassette is already initialized as<br />%s1<br />Reinitialization can not be completed.</pre>                                                                                                                           | <pre lang="ja">カセット初期化エラー.<br />カセットはすでに%s1として初期化<br />されています. 再初期化はできません.</pre> |
|    96 | Error | 196           | <pre>Cassette initialization error.<br />The cassette is already initialized as<br />%s1<br />Reinitialization can not be completed.</pre>                                                                                                                           | <pre lang="ja">カセット初期化エラー.<br />カセットはすでに%s1として初期化<br />されています. 再初期化はできません.</pre> |
|    97 | Error | 197           | <pre>Cassette initialization error.<br />The cassette is already initialized as<br />%s1<br />Reinitialization can not be completed.</pre>                                                                                                                           | <pre lang="ja">カセット初期化エラー.<br />カセットはすでに%s1として初期化<br />されています. 再初期化はできません.</pre> |
|    98 | Info  | 198, 500      | <pre>Installation completed.<br />Please write down the No.%s2<br />on cassette and machine.  Turn off the<br />power and replace cassette to<br />%s1 then turn on the power.</pre>                                                                                 | <pre lang="ja">インストール完了.<br />カセットと本体に認証番号%s2を記入<br />してください.電源を切ってカセットを<br />%s1に交換し,再度電源を入れて<br />ください.</pre> |
|    99 | Info  | 199, 501      | <pre>Installation complete.  Please write down<br />the No.%s3 on cassette and machine.<br />Replace CD-ROM to %s1 and turn off<br />the power then replace cassette to<br />%s2.  Set DIP-SW4 to "ON",<br />then turn on the power.</pre>                           | <pre lang="ja">インストール完了. カセットと本体に認証番号<br />%s3を記入してください.<br />CD-ROMを%s1に交換して電源を切り,<br />カセットを%s2に交換し,<br />DIP-SW4をONにして再度電源を入れてください.</pre> |
|   100 | Info  | 200, 502      | <pre>Operating cassette initialized.<br />The cassette was initialized as Operating<br />Cassette (%s1)</pre>                                                                                                                                                        | <pre lang="ja">運用カセット初期化完了.<br />カセットを運用カセット(%s1)として<br />初期化しました.</pre> |
|   101 | Info  | 201, 503      | <pre>Installation cassette initialized.<br />The cassette was initialized as<br />Installation Cassette (%s1)</pre>                                                                                                                                                  | <pre lang="ja">インストールカセット初期化完了.<br />カセットをインストールカセット(%s1)<br />として初期化しました.</pre> |
|   102 | Info  | 202, 504      | <pre>Initialized Operating Cassette<br />The cassette is already initialized as<br />Operating Cassette (%s1)<br />Reinitialization is not necessary.</pre>                                                                                                          | <pre lang="ja">初期化済み運用カセット.<br />カセットはすでに運用カセット(%s1)<br />として初期化されています. <br />再初期化の必要はありません.</pre> |
|   103 | Info  | 203, 505      | <pre>Initialized Installation Cassette<br />The cassette is already initialized as<br />Installation Cassette (%s1)<br />Reinitialization is not necessary.</pre>                                                                                                    | <pre lang="ja">初期化済みインストールカセット.<br />カセットはすでにインストールカセット<br />(%s1)として初期化されています.<br />再初期化の必要はありません.</pre> |
|   104 | Info  | 204, 506      | <pre>Installation completed.<br />Please write down the No.%s2<br />on cassette and machine.  Turn off the<br />power and replace cassette to<br />%s1 then turn on the power.</pre>                                                                                 | <pre lang="ja">インストール完了.<br />カセットと本体に認証番号%s2を記入<br />してください.電源を切ってカセットを<br />%s1に交換し,再度電源を入れて<br />ください.</pre> |
|   105 | Info  | 205, 507      | <pre>Installation complete.  Please write down<br />the No.%s3 on cassette and machine.<br />Replace CD-ROM to %s1 and turn off<br />the power then replace cassette to<br />%s2.  Set DIP-SW4 to "ON",<br />then turn on the power.</pre>                           | <pre lang="ja">インストール完了. カセットと本体に認証番号<br />%s3を記入してください.<br />CD-ROMを%s1に交換して電源を切り,<br />カセットを%s2に交換し,<br />DIP-SW4をONにして再度電源を入れてください.</pre> |
|   106 | Info  | 206, 508      | <pre>Installation completed.<br />Please write down the No.%s1<br />on cassette and machine.<br />Turn off the power, then reboot.</pre>                                                                                                                             | <pre lang="ja">インストール完了.<br />カセットと本体に認証番号%s1を記入<br />してください.<br />電源を切って再起動してください.</pre> |
|   107 | Info  | 207, 509      | <pre>Installation complete.<br />Please write down the No.%s2<br />on cassette and machine.<br />Replace CD-ROM to %s1 and turn off<br />the power.<br />Set DIP-SW4 to "ON", then reboot.</pre>                                                                     | <pre lang="ja">インストール完了.<br />カセットと本体に認証番号%s2を<br />記入してください.<br />CD-ROMを%s1に交換して電源を切り,<br />DIP-SW4をONにして再起動してください.</pre> |
|   108 | Info  | 208, 510      | <pre>Security cassette initialized.<br />The cassette was initialized for<br />%s1.</pre>                                                                                                                                                                            | <pre lang="ja">セキュリティカセット初期化完了.<br />カセットを%s1に初期化しました.</pre> |
|   109 | Info  | 209, 511      | <pre>Initialized Security Cassette<br />The cassette is already initialized for<br />%s1.<br />Reinitialization is not necessary.</pre>                                                                                                                              | <pre lang="ja">初期化済みセキュリティカセット.<br />カセットはすでに%s1に初期化<br />されています. 再初期化の必要はありません.</pre> |
|   110 | Info  | 210, 512      | <pre>SERVICE button is pressed.<br />To force installation, turn off the power,<br />change the cassette to the Installation<br />Cassette, and turn on the power with<br />pressing SERVICE switch.</pre>                                                           | <pre lang="ja">サービスボタンが押されています.<br />強制インストールを行うには電源を切り,<br />インストールカセットに交換して, サービス<br />ボタンを押しながら電源を入れてください.</pre> |
|   111 | Note  | 211, 513, 602 | <pre>CD-ROM drive version update in progress.<br />Please do not shut off power.<br />This will take a few moments.</pre>                                                                                                                                            | <pre lang="ja">現在CD-ROMドライブのバージョンアップを<br />実行しています.<br />電源を切らずにそのままお待ち下さい.</pre> |
|   112 | Note  | 212, 514, 603 | <pre>CD-ROM drive version update completed.</pre>                                                                                                                                                                                                                    | <pre lang="ja">CD-ROMドライブのバージョンアップが完了<br />しました.</pre> |
|   113 | Note  | 213, 515, 604 | <pre>Starting CD-ROM drive version update.<br />Please do not turn off the power while<br />updating.<br />Press TEST button to begin updating.</pre>                                                                                                                | <pre lang="ja">CD-ROMドライブのバージョンアップを行います.<br />バージョンアップ中は絶対に電源を切らないで<br />下さい.<br />テストボタンを押すとバージョンアップを開始<br />します.</pre> |
|   114 | Note  | 214, 516, 605 | <pre>Cleared RTC-RAM.<br />At Game Demo screen, press the test button<br />for the Test Mode and re-do the settings.<br /><br />Press the Test Button for the next screen.</pre>                                                                                     | <pre lang="ja">RTC-RAMをクリアしました.<br />ゲームデモが始まったらテストボタンを押して<br />テストモードに入り設定をやり直してください.<br /><br />テストボタンを押すと次に進みます.</pre> |

## Pinouts

- [Main board pinouts (`GX700-PWB(A)`)](#main-board-pinouts-gx700-pwba)
- [Analog I/O board pinouts (`GX700-PWB(F)`)](#analog-io-board-pinouts-gx700-pwbf)
- [Digital I/O board pinouts (`GX894-PWB(B)A`)](#digital-io-board-pinouts-gx894-pwbba)
- [Security cartridge pinouts](#security-cartridge-pinouts)

### Main board pinouts (`GX700-PWB(A)`)

#### Analog input port (`ANALOG`, `CN3`)

The inputs are wired directly to the 573's built-in ADC with no protection, so
they can only accept voltages in 0-5V range. This connector is usually used for
potentiometers and similar resistive analog controls.

| Pin | Name  | Dir |
| --: | :---- | :-- |
|   1 | `5V`  |     |
|   2 | `5V`  |     |
|   3 | `5V`  |     |
|   4 | `5V`  |     |
|   5 | `CH0` | I   |
|   6 | `GND` |     |
|   7 | `CH1` | I   |
|   8 | `CH2` | I   |
|   9 | `CH3` | I   |
|  10 | `GND` |     |

#### Digital output port (`EXT-OUT`, `CN4`)

Unlike the light output ports on most I/O boards, these are unisolated 5V logic
level outputs.

| Pin | Name   | Dir |
| --: | :----- | :-- |
|   1 | `5V`   |     |
|   2 | `5V`   |     |
|   3 | `OUT7` | O   |
|   4 | `OUT6` | O   |
|   5 | `OUT5` | O   |
|   6 | `OUT4` | O   |
|   7 | `OUT3` | O   |
|   8 | `OUT2` | O   |
|   9 | `OUT1` | O   |
|  10 | `OUT0` | O   |
|  11 | `GND`  |     |
|  12 | `GND`  |     |

#### Digital input port (`EXT-IN`, `CN5`)

Unlike `EXT-OUT`, this port is not a separate input port. It piggybacks on the
JAMMA button inputs instead, exposing the button 4 and 5 pins for both players
as well as a sixth button input which is not available on the JAMMA connector.
All inputs have a pullup resistor to 5V.

| Pin | Name    | Dir | JAMMA pin |
| --: | :------ | :-- | --------: |
|   1 | `5V`    |     |           |
|   2 | `5V`    |     |           |
|   3 | `P1_B4` | I   |        25 |
|   4 | `P1_B5` | I   |        26 |
|   5 | `P1_B6` | I   |           |
|   6 | `GND`   |     |           |
|   7 | `P2_B4` | I   |         c |
|   8 | `P2_B5` | I   |         d |
|   9 | `P2_B6` | I   |           |
|  10 | `GND`   |     |           |

#### Amplified speaker output (`SOUND-OUT`, `CN9`)

The pinout of this connector is currently unknown.

#### Main I/O board connector (`CN10`)

Used by I/O boards to connect to the motherboard. Note that the address and data
bus are 3.3V, while all other signals are 5V as they go through the CPLD.

| Pin | Name     | Dir | Pin | Name     | Dir |
| --: | :------- | :-- | --: | :------- | :-- |
|  A1 | `5V`     |     |  B1 | `5V`     |     |
|  A2 | `5V`     |     |  B2 | `5V`     |     |
|  A3 | `5V`     |     |  B3 | `5V`     |     |
|  A4 | `5V`     |     |  B4 | `5V`     |     |
|  A5 | `5V`     |     |  B5 | `5V`     |     |
|  A6 | `/RD`    | O   |  B6 | `/WR0`   | O   |
|  A7 | `/WR1`   | O   |  B7 | `GND`    |     |
|  A8 | `GND`    |     |  B8 | `SYSCLK` | O   |
|  A9 | `GND`    |     |  B9 | `GND`    |     |
| A10 | `/RESET` | O   | B10 | `/RESET` | O   |
| A11 | `GND`    |     | B11 | `GND`    |     |
| A12 | `/CS1`   | O   | B12 | `DMARQ5` | I   |
| A13 | `GND`    |     | B13 | `GND`    |     |
| A14 | `DMARQ5` | I   | B14 | `/CS1`   | O   |
| A15 | `/CS2`   | O   | B15 | `NC`     |     |
| A16 | `/IRQ10` | I   | B16 | `/IRQ10` | I   |
| A17 | `A22`    | O   | B17 | `A23`    | O   |
| A18 | `A20`    | O   | B18 | `A21`    | O   |
| A19 | `A14`    | O   | B19 | `A15`    | O   |
| A20 | `A12`    | O   | B20 | `A13`    | O   |
| A21 | `A6`     | O   | B21 | `A7`     | O   |
| A22 | `A4`     | O   | B22 | `A5`     | O   |
| A23 | `A2`     | O   | B23 | `A3`     | O   |
| A24 | `A0`     | O   | B24 | `A1`     | O   |
| A25 | `D14`    | IO  | B25 | `D15`    | IO  |
| A26 | `D12`    | IO  | B26 | `D13`    | IO  |
| A27 | `D10`    | IO  | B27 | `D11`    | IO  |
| A28 | `D8`     | IO  | B28 | `D9`     | IO  |
| A29 | `D6`     | IO  | B29 | `D7`     | IO  |
| A30 | `D4`     | IO  | B30 | `D5`     | IO  |
| A31 | `D2`     | IO  | B31 | `D3`     | IO  |
| A32 | `D0`     | IO  | B32 | `D1`     | IO  |
| A33 | `GND`    |     | B33 | `GND`    |     |
| A34 | `GND`    |     | B34 | `GND`    |     |
| A35 | `GND`    |     | B35 | `GND`    |     |
| A36 | `3.3V`   |     | B36 | `3.3V`   |     |
| A37 | `3.3V`   |     | B37 | `3.3V`   |     |
| A38 | `3.3V`   |     | B38 | `3.3V`   |     |
| A39 | `3.3V`   |     | B39 | `3.3V`   |     |
| A40 | `3.3V`   |     | B40 | `3.3V`   |     |

#### Analog CD-DA/MP3 audio input (`CD-DA IN`, `CN12`)

Connected to either the CD-ROM drive's audio output or to `CN16` on the digital
I/O board on systems equipped with a drive.

| Pin | Name   | Dir |
| --: | :----- | :-- |
|   1 | `LIN`  | I   |
|   2 | `AGND` |     |
|   3 | `AGND` |     |
|   4 | `RIN`  | I   |

#### Security cartridge slot (`CN14`)

All signals are 5V as they go through level shifters.

| Pin | Name     | Dir | Notes                        | Pin | Name     | Dir | Notes                              |
| --: | :------- | :-- | :--------------------------- | --: | :------- | :-- | :--------------------------------- |
|   1 | `GND`    |     |                              |  23 | `GND`    |     |                                    |
|   2 | `GND`    |     |                              |  24 | `GND`    |     |                                    |
|   3 | `/DSR`   | I   | Usually shorted to ground    |  25 | `MCUCLK` | O   | 7.3728 MHz JVS MCU clock           |
|   4 | `NC`     |     | May actually be `/DTR`?      |  26 | `GND`    |     |                                    |
|   5 | `TX`     | O   |                              |  27 | `DRDY`   | O   | Goes high when 573 updates `D0-D7` |
|   6 | `RX`     | I   |                              |  28 | `SDA`    | IO  |                                    |
|   7 | `/RESET` | IO  | System reset (from watchdog) |  29 | `/IREQ`  | I   | Sets `IRDY` when pulsed low        |
|   8 | `GND`    |     |                              |  30 | `/DACK`  | I   | Clears `DRDY` when pulsed low      |
|   9 | `GND`    |     |                              |  31 | `IRDY`   | O   | Goes low when 573 reads `I0-I7`    |
|  10 |          |     | Key (missing pin)            |  32 |          |     | Key (missing pin)                  |
|  11 | `?`      |     | Not connected?               |  33 | `I7`     | I   |                                    |
|  12 | `?`      |     | Not connected?               |  34 | `I6`     | I   |                                    |
|  13 | `D7`     | O   |                              |  35 | `I5`     | I   |                                    |
|  14 | `D6`     | O   |                              |  36 | `I4`     | I   |                                    |
|  15 | `D5`     | O   |                              |  37 | `I3`     | I   |                                    |
|  16 | `D4`     | O   |                              |  38 | `I2`     | I   |                                    |
|  17 | `D3`     | O   |                              |  39 | `I1`     | I   |                                    |
|  18 | `D2`     | O   |                              |  40 | `I0`     | I   |                                    |
|  19 | `D1`     | O   |                              |  41 | `5V`     |     |                                    |
|  20 | `D0`     | O   |                              |  42 | `5V`     |     |                                    |
|  21 | `5V`     |     |                              |  43 | `/RTS`   | O   | Usually shorted to `/CTS`          |
|  22 | `5V`     |     |                              |  44 | `/CTS`   | I   | Usually shorted to `/RTS`          |

#### Power input or output (`CN17`)

Commonly used to distribute the 12V rail to security cartridges with built-in
light drivers or external modules, but it can also used instead of the JAMMA
connector to supply power to the 573. The pinout is silkscreened on the board.

| Pin | Name  |
| --: | :---- |
|   1 | `12V` |
|   2 | `12V` |
|   3 | `GND` |
|   4 | `GND` |
|   5 | `5V`  |
|   6 | `5V`  |

#### I2S digital SPU audio output (`DIGITAL-AUDIO`, `CN19`)

Always unpopulated. Pin 4 outputs a 16.9344 MHz master clock (system clock
divided by 2, or 44100 Hz sampling rate multiplied by 384). This port does *not*
output audio from the CD-DA/MP3 input, which is not routed through the SPU.

| Pin | Name    | Dir |
| --: | :------ | :-- |
|   1 | `BCLK`  | O   |
|   2 | `SDOUT` | O   |
|   3 | `GND`   |     |
|   4 | `MCLK`  | O   |
|   5 | `LRCK`  | O   |

#### Secondary I/O board connector (`CN21`)

The address lines not wired to `CN10`, as well as the otherwise unused SIO0
controller and memory card bus, are broken out to this connector. No currently
known I/O board uses it. All signals are 3.3V.

| Pin | Name   | Dir | Pin | Name     | Dir |
| --: | :----- | :-- | --: | :------- | :-- |
|  A1 | `A8`   | O   |  B1 | `A9`     | O   |
|  A2 | `A10`  | O   |  B2 | `A11`    | O   |
|  A3 | `A16`  | O   |  B3 | `A17`    | O   |
|  A4 | `A18`  | O   |  B4 | `A19`    | O   |
|  A5 | `GND`  |     |  B5 | `?`      |     |
|  A6 | `GND`  |     |  B6 | `?`      |     |
|  A7 | `GND`  |     |  B7 | `GND`    |     |
|  A8 | `GND`  |     |  B8 | `DOTCLK` | O   |
|  A9 | `GND`  |     |  B9 | `GND`    |     |
| A10 | `GND`  |     | B10 | `/DSR`   | I   |
| A11 | `GND`  |     | B11 | `/DTR2`  | O   |
| A12 | `GND`  |     | B12 | `/DTR1`  | O   |
| A13 | `GND`  |     | B13 | `RX`     | I   |
| A14 | `GND`  |     | B14 | `TX`     | O   |
| A15 | `GND`  |     | B15 | `SCK`    | O   |

#### Watchdog test header (`WD-CHECK`, `CN22`)

Always unpopulated. Exposes the watchdog's clear input (pulsed whenever the CPU
writes to the watchdog clear register) as well as the reset output. Injecting
pulses to forcefully clear the watchdog should work, although it's much easier
to simply disable it by placing a jumper on `S86`.

| Pin | Name     | Dir |
| --: | :------- | :-- |
|   1 | `WDCLR`  | IO  |
|   2 | `/RESET` | O   |
|   3 | `5V`     |     |
|   4 | `GND`    |     |

#### GPU clock and compositing output (`CN23`)

Only present on later revisions of the main board and only populated on DDR
Karaoke Mix, which uses the semitransparency plane of the currently displayed
framebuffer as an alpha mask in order to composite the 573's output on top of
the incoming karaoke video feed.

| Pin | Name    | Dir | GPU pin |
| --: | :------ | :-- | ------: |
|   1 | `FSC`   | O   |     153 |
|   2 | `DMASK` | O   |     202 |
|   3 | `GND`   |     |         |

#### Security cartridge serial port (`CN24`)

Only present on later revisions of the main board and always unpopulated.
Exposes the same 5V SIO1 signals as the security cartridge slot.

| Pin | Name   | Dir | Cart pin |
| --: | :----- | :-- | -------: |
|   1 | `TX`   | O   |        5 |
|   2 | `RX`   | I   |        6 |
|   3 | `GND`  |     |          |
|   4 | `GND`  |     |          |
|   5 | `/RTS` | O   |       43 |
|   6 | `/CTS` | I   |       44 |

#### RGB video output (`CN25`)

Only present on later revisions of the main board and only populated on GunMania
and DDR Karaoke Mix, whose I/O boards feature RGB to S-video and composite
converters respectively. Exposes the same RGB signals as the JAMMA and DB15
connectors.

| Pin | Name    | Dir | JAMMA pin |
| --: | :------ | :-- | --------: |
|   1 | `GND`   | O   |           |
|   2 | `CSYNC` | O   |         P |
|   3 | `BOUT`  | O   |        13 |
|   4 | `GOUT`  | O   |         N |
|   5 | `ROUT`  | O   |        12 |

#### Watchdog configuration jumper (`S86`)

Always unpopulated. Shorting pins 2 and 3 will disable the watchdog while
keeping power-on reset functional. Pin 1 seems to be an active-high reset
output, unused by the 573.

| Pin | Name    | Dir |
| --: | :------ | :-- |
|   1 | `RESET` | O   |
|   2 | `GND`   |     |
|   3 | `WDEN`  | I   |

#### JVS MCU pin mapping

| Pin   | H8 GPIO   | Dir | Connected to       | Usage                                         |
| ----: | :-------- | :-- | :----------------- | :-------------------------------------------- |
|    11 | `P9_0`    | I   |                    | _Unused_                                      |
|    12 | `P9_1-2`  | O   | Konami ASIC        | Status code (readable from `0x1f400004`)      |
|    12 | `P9_3-4`  | O   | Konami ASIC        | Error code (readable from `0x1f400004`)       |
|    16 | `IRQ0`    | I   |                    | _Unused_                                      |
| 17-24 | `P6_0-7`  | O   | Konami ASIC        | Low byte of value readable from `0x1f40000a`  |
| 25-32 | `P5_0-7`  | O   | Konami ASIC        | High byte of value readable from `0x1f40000a` |
|    34 | `P7_3`    | I   | Handshaking logic  | Current `JVSDRDY` status                      |
|    35 | `P7_4`    | I   | Handshaking logic  | Current `JVSIRDY` status                      |
|    36 | `P7_5`    | I   |                    | _Unused_                                      |
|    37 | `P7_6`    | I   |                    | _Unused_                                      |
|    38 | `P7_7`    | I   |                    | _Unused_                                      |
| 39-46 | `P8_0-7`  | I   | Bus (via latch)    | High byte of value written to `0x1f680000`    |
|    47 | `P2_0`    | O   | RS-485 transceiver | JVS driver output enable                      |
|    48 | `P2_1`    | I   | RS-485 transceiver | JVS serial port RX                            |
|    49 | `P2_2`    | O   | RS-485 transceiver | JVS serial port TX                            |
|    50 | `P3_2`    | I   |                    | _Unused_                                      |
|    51 | `P3_1`    | I   |                    | _Unused_                                      |
|    52 | `P3_0`    | I   |                    | _Unused_                                      |
|    53 | `P1_0`    | O   | Handshaking logic  | `/JVSDACK` (clears `JVSDRDY` when pulsed low) |
|    54 | `P1_4`    | O   | Handshaking logic  | `JVSIREQ` (sets `JVSIRDY` when pulsed high)   |
|    55 | `P1_5`    | I   |                    | _Unused_                                      |
|    56 | `P1_6`    | I   |                    | _Unused_                                      |
|    57 | `P1_7`    | I   |                    | _Unused_                                      |
|  59-2 | `PB_7-0`  | I   | Bus (via latch)    | Low byte of value written to `0x1f680000`     |

### Analog I/O board pinouts (`GX700-PWB(F)`)

#### Output banks A, B (`CN33`, `CN34` respectively)

All outputs are open-drain. Pins 1 and 10 are tied together and connected to the
optocouplers' emitters.

| Pin | Name          | Dir |
| --: | :------------ | :-- |
|   1 | `ACOM`/`BCOM` |     |
|   2 | `A0`/`B0`     | O   |
|   3 | `A1`/`B1`     | O   |
|   4 | `A2`/`B2`     | O   |
|   5 | `A3`/`B3`     | O   |
|   6 | `A4`/`B4`     | O   |
|   7 | `A5`/`B5`     | O   |
|   8 | `A6`/`B6`     | O   |
|   9 | `A7`/`B7`     | O   |
|  10 | `ACOM`/`BCOM` |     |

#### Output bank C (`CN35`)

All outputs are open-drain. Unlike banks A and B, pin 10 is not tied to pin 1
but is instead connected to the EMI filters' ground (`FGND`), isolated from the
system ground but shared across all output banks.

| Pin | Name   | Dir |
| --: | :----- | :-- |
|   1 | `CCOM` |     |
|   2 | `C0`   | O   |
|   3 | `C1`   | O   |
|   4 | `C2`   | O   |
|   5 | `C3`   | O   |
|   6 | `C4`   | O   |
|   7 | `C5`   | O   |
|   8 | `C6`   | O   |
|   9 | `C7`   | O   |
|  10 | `FGND` |     |

#### Output bank D (`CN36`)

All outputs are open-drain.

| Pin | Name   | Dir |
| --: | :----- | :-- |
|   1 | `DCOM` |     |
|   2 | `D0`   | O   |
|   3 | `D1`   | O   |
|   4 | `D2`   | O   |
|   5 | `D3`   | O   |
|   6 | `FGND` |     |

### Digital I/O board pinouts (`GX894-PWB(B)A`)

#### Output bank C (`CN10`)

All outputs are open-drain. The optocouplers driving `C0-C3` have their emitters
wired to `CCOM0`, while those driving `C4-C7` have their emitters wired to
`CCOM1`.

| Pin | Name    | Dir |
| --: | :------ | :-- |
|   1 | `CCOM0` |     |
|   2 | `C0`    | O   |
|   3 | `C1`    | O   |
|   4 | `C2`    | O   |
|   5 | `C3`    | O   |
|   6 | `CCOM1` |     |
|   7 | `C4`    | O   |
|   8 | `C5`    | O   |
|   9 | `C6`    | O   |
|  10 | `C7`    | O   |

#### Output bank B (`CN11`)

All outputs are open-drain. The optocouplers driving `B0-B3` have their emitters
wired to `BCOM0`, while those driving `B4-B7` have their emitters wired to
`BCOM1`.

| Pin | Name    | Dir |
| --: | :------ | :-- |
|   1 | `BCOM0` |     |
|   2 | `B0`    | O   |
|   3 | `B1`    | O   |
|   4 | `B2`    | O   |
|   5 | `B3`    | O   |
|   6 | `BCOM1` |     |
|   7 | `B4`    | O   |
|   8 | `B5`    | O   |
|   9 | `B6`    | O   |
|  10 | `B7`    | O   |
|  11 | `NC`    |     |
|  12 | `NC`    |     |

#### Output bank A (`CN12`)

All outputs are open-drain. The optocouplers driving `A0-A3` have their emitters
wired to `ACOM0`, while those driving `A4-A7` have their emitters wired to
`ACOM1`.

| Pin | Name    | Dir |
| --: | :------ | :-- |
|   1 | `ACOM0` |     |
|   2 | `A0`    | O   |
|   3 | `A1`    | O   |
|   4 | `A2`    | O   |
|   5 | `A3`    | O   |
|   6 | `ACOM1` |     |
|   7 | `A4`    | O   |
|   8 | `A5`    | O   |
|   9 | `A6`    | O   |
|  10 | `A7`    | O   |
|  11 | `NC`    |     |
|  12 | `NC`    |     |
|  13 | `NC`    |     |

#### Output bank D (`CN13`)

All outputs are open-drain.

| Pin | Name   | Dir |
| --: | :----- | :-- |
|   1 | `DCOM` |     |
|   2 | `D0`   | O   |
|   3 | `D1`   | O   |
|   4 | `D2`   | O   |
|   5 | `D3`   | O   |

#### Input bank (`CN14`)

The pinout of this connector is currently unknown.

#### RS-232 serial port (`CN15`)

| Pin | Name   | Dir |
| --: | :----- | :-- |
|   1 | `TX`   | O   |
|   2 | `RX`   | O   |
|   3 | `GND`  |     |
|   4 | `GND`  |     |
|   5 | `RTS`  | O   |
|   6 | `CTS`  | O   |
|   7 | `DTR`  | O   |
|   8 | `DSR`  | O   |

#### Analog MP3 audio output (`CN16`)

Usually connected to `CN12` on the main board. GuitarFreaks routes this output
to a separate set of RCA jacks on the front I/O panel instead.

| Pin | Name   | Dir |
| --: | :----- | :-- |
|   1 | `LOUT` | O   |
|   2 | `AGND` |     |
|   3 | `AGND` |     |
|   4 | `ROUT` | O   |

#### Unknown (`CN17`)

The pinout of this connector is currently unknown.

#### I2S digital MP3 audio output (`CN18`)

| Pin | Name    | Dir | FPGA pin |
| --: | :------ | :-- | -------: |
|   1 | `MCLK`  | O   |       97 |
|   2 | `BCLK`  | O   |       94 |
|   3 | `SDOUT` | O   |       96 |
|   4 | `LRCK`  | O   |       95 |
|   5 | `?`     |     |          |
|   6 | `?`     |     |          |

#### XCS40XL FPGA pin mapping

| Pin   | JTAG | FPGA alt.     | Dir | Delay | Slew | Connected to         | Usage                            |
| ----: | ---: | :------------ | :-- | :---- | :--- | :------------------- | :------------------------------- |
|     2 |  170 | `GCK1`        | IO  | No    | Slow | DRAM                 | Data bus bit 4                   |
|     3 |  173 |               | IO  | No    | Slow | DRAM                 | Data bus bit 8                   |
|     4 |  176 |               | IO  | No    | Slow | DRAM                 | Data bus bit 9                   |
|     5 |  179 |               | IO  | No    | Slow | DRAM                 | Data bus bit 10                  |
|     6 |  182 | `TDI`         |     |       |      |                      | _Unused_                         |
|     7 |  185 | `TCK`         |     |       |      |                      | _Unused_                         |
|     8 |  194 |               | IO  | No    | Slow | DRAM                 | Data bus bit 3                   |
|     9 |  197 |               | IO  | No    | Slow | DRAM                 | Data bus bit 11                  |
|    10 |  200 |               | IO  | No    | Slow | DRAM                 | Data bus bit 2                   |
|    11 |  203 |               | IO  | No    | Slow | DRAM                 | Data bus bit 12                  |
|    12 |  206 |               |     |       |      |                      | _Unused_                         |
|    14 |  212 |               | IO  | No    | Slow | DRAM                 | Data bus bit 1                   |
|    15 |  215 |               | IO  | No    | Slow | DRAM                 | Data bus bit 0                   |
|    16 |  218 | `TMS`         |     |       |      |                      | _Unused_                         |
|    17 |  221 |               | IO  | No    | Slow | DRAM                 | Data bus bit 13                  |
|    19 |  236 |               | IO  | No    | Slow | DRAM                 | Data bus bit 14                  |
|    20 |  239 |               | IO  | No    | Slow | DRAM                 | Data bus bit 15                  |
|    21 |  242 |               | IO  | Yes   | Slow | SRAM                 | Data bus bit 3                   |
|    22 |  245 |               | IO  | Yes   | Slow | SRAM                 | Data bus bit 2                   |
|    23 |  248 |               | IO  | Yes   | Slow | SRAM                 | Data bus bit 4                   |
|    24 |  251 |               | IO  | Yes   | Slow | SRAM                 | Data bus bit 1                   |
|    27 |  254 |               | IO  | Yes   | Slow | SRAM                 | Data bus bit 5                   |
|    28 |  257 |               | IO  | Yes   | Slow | SRAM                 | Data bus bit 0                   |
|    29 |  260 |               | IO  | Yes   | Slow | SRAM                 | Data bus bit 6                   |
|    30 |  263 |               | O   |       | Slow | SRAM                 | Address bus bit 0                |
|    31 |  266 |               | IO  | Yes   | Slow | SRAM                 | Data bus bit 7                   |
|    32 |  269 |               | O   |       | Slow | SRAM                 | Address bus bit 1                |
|    34 |  284 |               | O   |       | Fast | SRAM                 | Chip select                      |
|    35 |  287 |               | O   |       | Slow | SRAM                 | Address bus bit 2                |
|    36 |  290 |               | O   |       | Slow | SRAM                 | Address bus bit 10               |
|    37 |  293 |               | O   |       | Slow | SRAM                 | Address bus bit 3                |
|    39 |  299 |               |     |       |      |                      | _Unused_                         |
|    40 |  302 |               | O   |       | Fast | SRAM                 | Output enable                    |
|    41 |  305 |               | O   |       | Slow | SRAM                 | Address bus bit 4                |
|    42 |  308 |               | O   |       | Slow | SRAM                 | Address bus bit 11               |
|    43 |  311 |               | O   |       | Slow | SRAM                 | Address bus bit 5                |
|    44 |  320 |               | O   |       | Slow | SRAM                 | Address bus bit 9                |
|    45 |  323 |               | O   |       | Slow | SRAM                 | Address bus bit 6                |
|    46 |  326 |               | O   |       | Slow | SRAM                 | Address bus bit 8                |
|    47 |  329 |               | O   |       | Slow | SRAM                 | Address bus bit 7                |
|    48 |  332 |               | O   |       | Slow | SRAM                 | Address bus bit 13               |
|    49 |  335 | `GCK2`        | O   |       | Slow | SRAM                 | Address bus bit 12               |
|    55 |  342 | `GCK3`        | O   |       | Fast | SRAM                 | Write enable                     |
|    56 |  345 | `/HDC`        | O   |       | Slow | SRAM                 | Address bus bit 14               |
|    57 |  348 |               | O   |       | Slow | SRAM                 | Address bus bit 16               |
|    58 |  351 |               | O   |       | Slow | SRAM                 | Address bus bit 15               |
|    59 |  354 |               | O   |       | Slow | Light bank D         | Output D3                        |
|    60 |  357 | `LDC`         | O   |       | Slow | Light bank D         | Output D2                        |
|    61 |  366 |               | I   | No    |      | Input bank           | Input 0                          |
|    62 |  369 |               | I   | No    |      | Input bank           | Input 1                          |
|    63 |  372 |               | I   | No    |      | Input bank           | Input 2                          |
|    64 |  375 |               | I   | No    |      | Input bank           | Input 3                          |
|    65 |  378 |               |     |       |      |                      | _Unused_                         |
|    67 |  384 |               | O   |       | Slow | Light bank D         | Output D1                        |
|    68 |  387 |               | O   |       | Slow | Light bank D         | Output D0                        |
|    69 |  390 |               | O   |       | Slow | Light bank B         | Output B7                        |
|    70 |  393 |               | O   |       | Slow | Light bank B         | Output B6                        |
|    72 |  396 |               | O   |       | Slow | Light bank B         | Output B5                        |
|    73 |  399 |               | O   |       | Slow | Light bank B         | Output B4                        |
|    74 |  414 |               | O   |       | Slow | Light bank A         | Output A3                        |
|    75 |  417 |               | O   |       | Slow | Light bank A         | Output A2                        |
|    76 |  420 |               | O   |       | Slow | Light bank A         | Output A1                        |
|    77 |  423 | `/INIT`       | IO  | -     | -    | CPLD                 | FPGA configuration status        |
|    80 |  426 |               | O   |       | Slow | Light bank A         | Output A0                        |
|    81 |  429 |               | O   |       | Slow | Light bank A         | Output A7                        |
|    82 |  432 |               | O   |       | Slow | Light bank A         | Output A6                        |
|    83 |  435 |               | O   |       | Slow | Light bank A         | Output A5                        |
|    84 |  438 |               | O   |       | Slow | Light bank A         | Output A4                        |
|    85 |  441 |               | I   | No    |      | RS-232 transceiver   | Serial port DSR                  |
|    87 |  456 |               | O   |       | Slow | RS-232 transceiver   | Serial port DTR                  |
|    88 |  459 |               | I   | No    |      | RS-232 transceiver   | Serial port RX                   |
|    89 |  462 |               | O   |       | Slow | RS-232 transceiver   | Serial port TX                   |
|    90 |  465 |               | I   | Yes   |      | RS-232 transceiver   | Serial port CTS                  |
|    92 |  471 |               |     |       |      |                      | _Unused_                         |
|    93 |  474 |               | O   |       | Slow | RS-232 transceiver   | Serial port RTS                  |
|    94 |  477 |               | O   |       | Slow | Audio DAC            | I2S bit clock (`BCLK`)           |
|    95 |  480 |               | O   |       | Slow | Audio DAC            | I2S frame clock (`LRCK`)         |
|    96 |  483 |               | O   |       | Slow | Audio DAC            | I2S data input (`SDIN`)          |
|    97 |  492 |               | O   |       | Slow | Audio DAC            | I2S master clock (`MCLK`)        |
|    98 |  495 |               | O   |       | Slow | ARCnet transceiver   | Network TX enable?               |
|    99 |  498 |               | O   |       | Slow | ARCnet transceiver   | Network TX?                      |
|   100 |  501 |               | I   | Yes   |      | ARCnet transceiver   | Network RX                       |
|   101 |  504 |               |     |       |      |                      | _Unused_                         |
|   102 |  507 | `GCK4`        |     |       |      |                      | _Unused_                         |
|   104 |      | `DONE`        | IO  | -     | -    | CPLD                 | FPGA configuration status        |
|   106 |      | `/PROGRAM`    | I   | -     | -    | CPLD                 | FPGA configuration reset         |
|   107 |  510 | `D7`          | IO  | No    | Slow | DS2433 (unpopulated) | Unused 1-wire bus (open drain)   |
|   108 |  513 | `GCK5`        |     |       |      |                      | _Unused_                         |
|   109 |  516 |               | IO  | No    | Slow | DS2401               | 1-wire bus (open drain)          |
|   110 |  519 |               | I   | No    |      | 573 bus              | Address bus bit 7                |
|   111 |  525 |               |     |       |      |                      | _Unused_                         |
|   112 |  534 | `D6`          | I   | No    |      | 573 bus              | Address bus bit 6                |
|   113 |  537 |               | I   | No    |      | 573 bus              | Address bus bit 5                |
|   114 |  540 |               | I   | No    |      | 573 bus              | Address bus bit 4                |
|   115 |  543 |               | I   | No    |      | 573 bus              | Address bus bit 3                |
|   116 |  546 |               | I   | No    |      | 573 bus              | Address bus bit 2                |
|   117 |  549 |               | I   | No    |      | 573 bus              | Address bus bit 1                |
|   119 |  558 |               | O   |       | Slow | Unknown              | Set up as AND of inputs 0-3 (?)  |
|   120 |  561 |               | IO  | Yes   | Slow | 573 bus              | Data bus bit 15                  |
|   122 |  564 | `D5`          | IO  | Yes   | Slow | 573 bus              | Data bus bit 14                  |
|   123 |  567 |               | IO  | Yes   | Slow | 573 bus              | Data bus bit 13                  |
|   124 |  576 |               | IO  | Yes   | Slow | 573 bus              | Data bus bit 12                  |
|   125 |  579 |               | IO  | Yes   | Slow | 573 bus              | Data bus bit 11                  |
|   126 |  582 |               | IO  | Yes   | Slow | 573 bus              | Data bus bit 10                  |
|   127 |  585 |               | IO  | Yes   | Slow | 573 bus              | Data bus bit 9                   |
|   128 |  588 | `D4`          | IO  | Yes   | Slow | 573 bus              | Data bus bit 8                   |
|   129 |  591 |               | IO  | Yes   | Slow | 573 bus              | Data bus bit 7                   |
|   132 |  594 | `D3`          | IO  | Yes   | Slow | 573 bus              | Data bus bit 6                   |
|   133 |  597 |               | IO  | Yes   | Slow | 573 bus              | Data bus bit 5                   |
|   134 |  600 |               | IO  | Yes   | Slow | 573 bus              | Data bus bit 4                   |
|   135 |  603 |               | IO  | Yes   | Slow | 573 bus              | Data bus bit 3                   |
|   136 |  606 |               | IO  | Yes   | Slow | 573 bus              | Data bus bit 2                   |
|   137 |  609 |               | IO  | Yes   | Slow | 573 bus              | Data bus bit 1                   |
|   138 |  618 | `D2`          | IO  | Yes   | Slow | 573 bus              | Data bus bit 0                   |
|   139 |  621 |               |     |       |      |                      | _Unused_                         |
|   141 |  624 |               |     |       |      |                      | _Unused_                         |
|   142 |  627 |               | I   | No    |      | 573 bus              | I/O board chip select            |
|   144 |  639 |               |     |       |      |                      | _Unused_                         |
|   145 |  642 |               | I   | No    |      | 573 bus              | Write strobe (`/WR0`)            |
|   146 |  645 |               | I   | No    |      | 573 bus              | Read strobe (`/RD`)              |
|   147 |  648 |               |     |       |      |                      | _Unused_                         |
|   148 |  651 |               | I   | No    |      | MAS3507D             | MP3 data request flag (`PI19`)   |
|   149 |  654 | `D1`          | O   |       | Slow | MAS3507D             | PIO chip select (`/PCS`)         |
|   150 |  657 |               | IO  | No    | Slow | MAS3507D             | I2C SDA                          |
|   151 |  666 |               | IO  | No    | Slow | MAS3507D             | I2C SCL                          |
|   152 |  669 |               | O   |       | Slow | MAS3507D             | Chip reset (`/POR`)              |
|   153 |  672 | `D0`/`DIN`    | I   | -     | -    | CPLD                 | FPGA configuration data          |
|   154 |  675 | `GCK6`/`DOUT` |     |       |      |                      | _Unused_                         |
|   155 |      | `CCLK`        | I   | -     | -    | CPLD                 | FPGA configuration clock         |
|   157 |    0 | `TDO`         |     |       |      |                      | _Unused_                         |
|   159 |    2 |               | I   | No    |      | MAS3507D             | Master clock ready flag (`WRDY`) |
|   160 |    5 | `GCK7`        | I   | No    |      | Crystal oscillator   | 29.45 MHz main clock             |
|   161 |    8 |               | I   | No    |      | MAS3507D             | MP3 frame sync flag (`PI4`)      |
|   162 |   11 |               | I   | No    |      | MAS3507D             | I2S master clock (`CLKO`/`MCLK`) |
|   163 |   14 | `CS1`         | O   |       | Slow | MAS3507D             | 14.725 MHz clock input (`CLKI`)  |
|   164 |   17 |               | O   |       | Slow | MAS3507D             | MP3 stream bit clock (`SIC`)     |
|   165 |   26 |               |     |       |      |                      | _Unused_                         |
|   166 |   32 |               | O   |       | Slow | MAS3507D             | MP3 stream frame clock (`SII`)   |
|   167 |   35 |               | O   |       | Slow | MAS3507D             | MP3 stream data input (`SID`)    |
|   168 |   38 |               | I   | No    |      | MAS3507D             | MP3 error flag (`PI8`)           |
|   169 |   41 |               | I   | No    |      | MAS3507D             | I2S bit clock (`SOC`/`BCLK`)     |
|   171 |   44 |               | I   | No    |      | MAS3507D             | I2S frame clock (`SOI`/`LRCK`)   |
|   172 |   47 |               | I   | No    |      | MAS3507D             | I2S data output (`SOD`/`SDOUT`)  |
|   174 |   62 |               | O   |       | Slow | DRAM                 | Address bus bit 5                |
|   175 |   65 |               | O   |       | Slow | DRAM                 | Address bus bit 6                |
|   176 |   68 |               | O   |       | Slow | DRAM                 | Address bus bit 4                |
|   177 |   71 |               | O   |       | Slow | DRAM                 | Address bus bit 7                |
|   178 |   74 |               | O   |       | Slow | DRAM                 | Address bus bit 3                |
|   179 |   77 |               | O   |       | Slow | DRAM                 | Address bus bit 8                |
|   180 |   80 |               | O   |       | Slow | DRAM                 | Address bus bit 2                |
|   181 |   83 |               | O   |       | Slow | DRAM                 | Address bus bit 9                |
|   184 |   86 |               | O   |       | Slow | DRAM                 | Address bus bit 1                |
|   185 |   89 |               | O   |       | Slow | DRAM                 | Address bus bit 10               |
|   186 |   92 |               | O   |       | Slow | DRAM                 | Address bus bit 0                |
|   187 |   95 |               | O   |       | Slow | DRAM                 | Address bus bit 11               |
|   188 |   98 |               | O   |       | Slow | DRAM                 | Address bus bit 12               |
|   189 |  101 |               | O   |       | Fast | DRAM                 | 22J row address strobe           |
|   190 |  104 |               | O   |       | Fast | DRAM                 | Output enable                    |
|   191 |  107 |               | O   |       | Fast | DRAM                 | 22H row address strobe           |
|   193 |  122 |               | O   |       | Fast | DRAM                 | 22G row address strobe           |
|   194 |  125 |               | O   |       | Fast | DRAM                 | 22G upper column address strobe  |
|   196 |  128 |               | O   |       | Fast | DRAM                 | Write enable                     |
|   197 |  131 |               | O   |       | Fast | DRAM                 | 22G lower column address strobe  |
|   198 |  134 |               | O   |       | Fast | DRAM                 | 22H upper column address strobe  |
|   199 |  137 |               | O   |       | Fast | DRAM                 | 22H lower column address strobe  |
|   200 |  140 |               | O   |       | Fast | DRAM                 | 22J upper column address strobe  |
|   201 |  143 |               | O   |       | Fast | DRAM                 | 22J lower column address strobe  |
|   202 |  152 |               |     |       |      |                      | _Unused_                         |
|   203 |  155 |               |     |       |      |                      | _Unused_                         |
|   204 |  158 |               | IO  | No    | Slow | DRAM                 | Data bus bit 7                   |
|   205 |  161 |               | IO  | No    | Slow | DRAM                 | Data bus bit 6                   |
|   206 |  164 |               | IO  | No    | Slow | DRAM                 | Data bus bit 5                   |
|   207 |  167 | `GCK8`        | I   | No    |      | Crystal oscillator   | 19.6608 MHz (UART?) clock        |

Notes:

- The FPGA has no access to the 33.8688 MHz system clock, despite it being
  broken out to the I/O board connector. Konami's bitstreams use the 29.45 MHz
  oscillator as the main clock, additionally dividing it down to 14.725 MHz and
  feeding it to the MAS3507D's clock input.
- The 19.6608 MHz clock is left unused by most (all?) bitstream variants, but
  was likely meant to be used for RS-232. Dividing it by 512, 1024, 2048 or 4096
  will give the standard baud rates of 38400, 19200, 9600 and 4800 respectively.
  The UART driving the RS-232 port may have been removed from the bitstream at
  some point to make room for the other circuitry.
- Most input pins have external pullup resistors, so enabling the FPGA's
  internal pullups is not necessary.
- Light outputs must be configured as open drain in order to work properly. The
  optocouplers' anodes are fed 5V rather than 3.3V; setting the outputs high
  instead of putting them into high-z will result in a voltage difference of
  ~1.7V across the optocouplers' LEDs, which is enough to trigger them.
- The "5V tolerant I/O" option in Xilinx's bitstream generator **must** be
  enabled when building custom bitstreams. There are no level shifters between
  the FPGA and the 573 bus.
- The FPGA's `M0`, `M1` and `/PWRDWN` pins seem to be hardwired to 3.3V.
- The DAC's `CKS` pin is hardwired to ground, so the I2S master clock must
  always be 256 \* the sampling rate.
- Pin 119 is set up by the DDR bitstream as a logical AND of pins 61-64. It is
  currently unclear if it goes to any other part on the board.
- Konami's bitstreams map the DRAM chips into a single address space as follows:
  - `0x0000000-0x07fffff`: 22H
  - `0x0800000-0x0ffffff`: 22J
  - `0x1000000-0x17fffff`: 22G

### Security cartridge pinouts

#### RS-232 "network" connector

Present on `GX700-PWB(E)`, `GX896-PWB(A)A`, `GX883-PWB(D)` and `GE949-PWB(D)A`
cartridges. All signals use RS-232 voltage levels. Note that DTR and DSR are
*not* wired to the respective SIO1 pins but to the security cartridge I/O pins.

On the `GX700-PWB(E)` cartridge the signals are referenced to the 573's ground
and not isolated. On all other cartridge types, the RS-232 transceiver is
powered through an isolated DC-DC module and fully eletrically isolated from the
573; the `GND` pin is the transceiver's isolated ground.

| Pin | Name  | Dir |
| --: | :---- | :-- |
|   1 | `TX`  | O   |
|   2 | `RX`  | I   |
|   3 | `DTR` | O   |
|   4 | `DSR` | I   |
|   5 | `GND` |     |

#### "Control" or "amp box" connector

Present on `GX896-PWB(A)A`, `GX883-PWB(D)` and `GE949-PWB(D)A` cartridges.
Unlike the RS-232 connector these are unisolated 5V logic level signals driven
through open-drain buffers, with pullup resistors to 5V.

| Pin | Name    | Dir |
| --: | :------ | :-- |
|   1 | `GND`   |     |
|   2 | `CTRL0` | O   |
|   3 | `GND`   |     |
|   4 | `CTRL1` | O   |
|   5 | `CTRL2` | O   |
|   6 | `5V`    |     |

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
