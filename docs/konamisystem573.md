
# Konami System 573

The System 573 is a PlayStation-based system used in a number of Konami arcade
games from the late 90s and early 2000s, most notably Dance Dance Revolution
and other early Bemani (Konami's rhythm game division) games.

- [Differences vs. PS1](#differences-vs-ps1)
- [Register map](#register-map)
- [I/O boards](#io-boards)
- [Security cartridges](#security-cartridges)
- [External modules](#external-modules)
- [Connectors](#connectors)
- [Game-specific information](#game-specific-information)
- [Misc. notes](#misc-notes)
- [Credits, sources and links](#credits-sources-and-links)

This document is currently work-in-progress. Here is a list of things that are
still missing:

- JVS communications and the microcontroller that handles them have to be
  documented. The microcontroller's firmware has already been dumped.
- The registers controlling the `EXT-IN` and `EXT-OUT` connectors haven't yet
  been found.
- PAL mode hasn't been tested on the 573. Konami games only ever used NTSC, so
  the 573 might in fact be unable to output PAL.
- I/O boards, *especially* the digital I/O board, need to be properly reverse
  engineered and documented. Some games are reportedly capable of telling if
  the analog I/O board is missing, so it must have at least one readable
  register.
- The DDR stage I/O board's communication protocol is largely unknown. More
  tests need to be done on real hardware and its CPLD shall be dumped if
  possible.
- The 700B01 BIOS contains references to the ability to boot from a FAT
  filesystem on a CF card inserted into a PCMCIA slot, which would actually be
  impossible due to the way the slots are wired up. That definitely needs more
  research.

## Differences vs. PS1

### Main changes

- **Main RAM is 4 MB** instead of 2 MB and **VRAM is 2 MB** instead of 1 MB.
  SPU RAM is still 512 KB.
- **The CD drive is completely different**. While the PS1's drive is fully
  integrated into the motherboard and uses a custom protocol, the 573 employs a
  standard ATAPI drive. This means there is no provision for playing XA-ADPCM,
  even though CD audio can still be played (as long as the 4-pin audio cable
  between the drive and the 573 motherboard is present). There is no wobble
  groove to worry about, but some drives the system shipped with are reportedly
  unable to read CD-Rs. Most 573 units have had their drive replaced (usually
  with a DVD drive) at least once, so this should not be an issue.
- **The SPI bus for controllers and memory cards is unused**. It is broken out
  to a connector, however no known I/O board uses it. Some games supported PS1
  memory cards through an adapter connected over JVS, with its own CPU and
  local SPI bus (more details about this later).
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
- **PCMCIA memory card**: some games shipped with additional flash memory in
  the form of a PCMCIA card, with sizes ranging from 16 to 64 MB. Note that
  these are "linear" memory-mapped cards without any built-in controller, not
  CF or ATA-compatible cards (which would be incompatible with the 573's PCMCIA
  wiring).
- **RTC and battery-backed 8 KB RAM**: used by games to store settings, save
  data and installation info (possibly including serial numbers). Unfortunately
  the RTC chip is one of those all-in-one things with a battery sealed inside,
  soldered directly to the motherboard. It goes without saying that 573 boards
  with a working RTC are rare.
- **JVS bus**: allows connection of multiple daisy chained peripherals using a
  standardized protocol based on a serial (RS-485) bus. The JVS specification
  requires devices to use *USB connectors* (USB-A at the host side, full size
  USB-B on peripherals) to carry RS-485 signals. The JVS port on the 573 was
  only ever "officially" used for the PS1 memory card reader module, however
  some games seem to support JVS I/O boards and input devices in addition to
  the built-in JAMMA connector.
- **Security cartridge**: optionally installed on the 573's side, contains a
  password protected EEPROM that holds factory pre-programmed data as well as
  keys generated during game installation, plus in some case a 64-bit serial
  number ROM. Security cartridges were bundled with most game discs as a way to
  prevent copying, as the discs themselves had no other protection of any kind.
  The CPU's serial port (SIO1) is also wired to the security cartridge slot.

## Register map

All standard PS1 registers, with the exception of the CD drive's, are present.
System 573-specific hardware is mapped into the EXP1 region at `0x1f000000`.
IRQ10 and DMA5, normally reserved for the expansion bus (and lightguns) on a
regular PS1, are used to access the ATAPI CD drive, while IRQ2 and DMA3 go
unused.

**NOTE**: EXP1 must be configured prior to accessing any of these registers.
The proper configuration value to write to the EXP1 delay/size register at
`0x1f801008` is `0x24173f47`. Afterwards, *all* bus writes shall be 16 or 32
bits wide. The behavior of 8-bit writes is undefined (8-bit reads work as
intended).

| Address range           | Description                                            |
| :---------------------- | :----------------------------------------------------- |
| `0x1f000000-0x1f3fffff` | Bank switched, can be mapped to flash or PCMCIA slots  |
| `0x1f400000-0x1f40000f` | [Konami ASIC registers](#konami-asic-registers)        |
| `0x1f480000-0x1f48000f` | [IDE register bank 0](#ide-registers)                  |
| `0x1f4c0000-0x1f4c000f` | [IDE register bank 1](#ide-registers)                  |
| `0x1f620000-0x1f623fff` | [RTC registers](#rtc-registers) and battery-backed RAM |
| `0x1f640000-0x1f6400ff` | [I/O board registers](#io-boards)                      |

### Konami ASIC registers

The Konami 056879 ASIC, used in most of their late 90s arcade boards, is
nothing more than a single 16-bit output port and 6 (possibly more?) 16-bit
input ports in a single package.

- `0x1f400000` (ASIC register 0): **ADC SPI, coin counters, audio**

  | Bits | RW | Description                                 |
  | ---: | :- | :------------------------------------------ |
  |    0 | W  | SPI MOSI to ADC                             |
  |    1 | W  | SPI CS to ADC                               |
  |    2 | W  | SPI SCK to ADC                              |
  |    3 | W  | Coin counter 1 (1 = energize counter coil)  |
  |    4 | W  | Coin counter 2 (1 = energize counter coil)  |
  |    5 | W  | Built-in audio amplifier enable (0 = muted) |
  |    6 | W  | External audio input enable? (0 = muted)    |
  |    7 | W  | SPU DAC output enable (0 = muted)           |
  |    8 | W  | Status bus clock to microcontroller         |
  | 9-15 |    | Unused?                                     |

  The ADC chip is an ADC0834 from TI, which uses a proprietary SPI(-like)
  protocol. Its four inputs are wired to the `ANALOG` connector on the 573
  motherboard. Refer to the ADC083x datasheet for details on how to bitbang the
  protocol.

  Mechanical coin counters are incremented by games whenever a coin is inserted
  by setting bit 3 or 4 for a fraction of a second and then clearing them. Bit
  5 controls whether the onboard audio amp is enabled, but does not affect the
  RCA line level outputs (which are always enabled). Setting bit 5 has no
  effect immediately as the amp takes about a second to turn on.

  The exact purpose of bit 6 is unclear. Games use it to mute audio from the CD
  drive or digital I/O board; in particular, this bit is cleared during attract
  mode if attract mode sounds are disabled. However, testing on real hardware
  seems to suggest it is some sort of downmixing or attenuation control rather
  than a proper mute.

  Unknown what reading from this port does.

- `0x1f400004` (ASIC register 2): **Misc. inputs**

  | Bits  | RW | Description                        |
  | ----: | :- | :--------------------------------- |
  |   0-3 | R  | DIP switch status                  |
  |   4-7 | R  | Status bus from microcontroller    |
  |  8-15 | RW | From `I0-I7` on security cartridge |

  The highest 8 bits read from this register are the state of the security
  cartridge's pins `I0-I7`. See the security cartridge section for an
  explanation of what each bit is wired to.

  Bit 3 (DIP switch 4) is used by the BIOS to determine whether to boot from
  the internal flash or CD drive. If set, the BIOS will attempt to search for
  a valid executable on the flash before initializing the drive.

- `0x1f400006` (ASIC register 3): **Misc. inputs**

  | Bits  | RW | Description                               |
  | ----: | :- | :---------------------------------------- |
  |     0 | R  | SPI MISO from ADC                         |
  |     1 | R  | SAR status from ADC                       |
  |     2 | R  | From `SDA` on security cartridge          |
  |     3 | R  | JVS sense input                           |
  |     4 | R  | JVS receive buffer status (1 = not empty) |
  |     5 | R  | Unknown (JVS-related)                     |
  |     6 | R  | `ISIG` status on security cartridge       |
  |     7 | R  | `DSIG` status on security cartridge       |
  |     8 | R  | Coin switch input 1 (inverted)            |
  |     9 | R  | Coin switch input 2 (inverted)            |
  |    10 | R  | PCMCIA card 1 insertion (0 = present)     |
  |    11 | R  | PCMCIA card 2 insertion (0 = present)     |
  |    12 | R  | Test button (built-in and JAMMA pin 15)   |
  | 13-15 |    | Unused?                                   |

  See the security cartridge section for more details about `ISIG` and  `DSIG`.
  For bit 2 to be valid, `SDA` should be set as an input by clearing the
  respective bit in the bank switch register.

- `0x1f400008` (ASIC register 6): **JAMMA controls**

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

  **NOTE**: since buttons are active low (wired between JAMMA pins and ground),
  all bits are 0 when a button is pressed and 1 when it isn't.

  The BIOS and games often read from this register and discard the result as a
  way of (inefficiently) keeping the CPU's write queue flushed.

- `0x1f40000a` (ASIC register 5): **JVS receive buffer**

  | Bits | RW | Description                          |
  | ---: | :- | :----------------------------------- |
  | 0-15 | R  | JVS data output from microcontroller |

- `0x1f40000c` (ASIC register 6): **JAMMA controls**

  | Bits  | RW | Description                      |
  | ----: | :- | :------------------------------- |
  |   0-7 |    | Unused?                          |
  |     8 | R  | Player 1 button 4 (JAMMA pin 25) |
  |     9 | R  | Player 1 button 5 (JAMMA pin 26) |
  |    10 | R  | Service button (JAMMA pin R)     |
  |    11 | R  | Player 1 button 6 (JAMMA pin 27) |
  | 12-15 |    | Unused?                          |

  **NOTE**: since buttons are active low (wired between JAMMA pins and ground),
  all bits are 0 when a button is pressed and 1 when it isn't.

- `0x1f40000e` (ASIC register 7): **JAMMA controls**

  | Bits  | RW | Description                      |
  | ----: | :- | :------------------------------- |
  |   0-7 |    | Unused?                          |
  |     8 | R  | Player 2 button 4 (JAMMA pin c)  |
  |     9 | R  | Player 2 button 5 (JAMMA pin d)  |
  |    10 |    | Unused?                          |
  |    11 | R  | Player 2 button 6 (JAMMA pin e)  |
  | 12-15 |    | Unused?                          |

  **NOTE**: since buttons are active low (wired between JAMMA pins and ground),
  all bits are 0 when a button is pressed and 1 when it isn't.

### IDE registers

The IDE interface is already well documented in many places. It consists of a
16-bit parallel data bus with a 3-bit address bus and 2 bank select pins
(`/CS0` and `/CS1`), giving a total of 16x 16-bit registers of which only 9 are
typically used. The 40-pin IDE cable carries a few other signals, such as an
interrupt pin and DMA control pins (unused on the 573). On the 573 the two IDE
banks are mapped to two separate memory regions at `0x1f480000` (CS0) and
`0x1f4c0000` (CS1). The interrupt pin is routed into IRQ10 through the CPLD,
while DMA and status pins are not connected.

On the 573 most (but not all) games expect an ATAPI CD drive to be always
connected and set as master. Connecting an additional ATA hard drive, CF card
or IDE-to-SATA bridge configured as slave does not seem to interfere with the
BIOS. Homebrew games and apps can leverage such a drive to e.g. dump the flash
or save arbitrary data, or to load assets for debugging without having to burn
discs.

Note that ATAPI gives slightly different meanings to most IDE registers, so
homebrew apps that support an additional ATA drive will have to interpret
registers differently depending on whether they are accessing the master ATAPI
drive or the slave ATA drive. Refer to the ATA and ATAPI specifications for
more details.

- `0x1f480000` (IDE address 0, CS0): **Data transfer**

  Data transfers can also be performed through DMA5, see below for details.

- `0x1f480002` (IDE address 1, CS0): **Error** / **Features**

- `0x1f480004` (IDE address 2, CS0): **Sector count**

- `0x1f480006` (IDE address 3, CS0): **Sector number**

- `0x1f480008` (IDE address 4, CS0): **Cylinder number low**

- `0x1f48000a` (IDE address 5, CS0): **Cylinder number high**

- `0x1f48000c` (IDE address 6, CS0): **Head number** / **Drive select**

- `0x1f48000e` (IDE address 7, CS0): **Status** / **Command**

- `0x1f4c000c` (IDE address 6, CS1): **Alternate status**

### IDE DMA and quirks

DMA channel 5, normally unused/reserved for the expansion port on a PS1, can be
used to transfer data to/from the IDE bus... with some caveats. The "correct"
way to connect an IDE drive to the PS1's DMA controller would to be to wire up
`DMARQ` and `DMACK` from the drive directly to the respective pins on the CPU,
allowing the DMA controller to synchronize transfers to the drive's internal
buffer seamlessly.

However, Konami being Konami, they didn't do this on the 573. Instead the drive
will "see" a DMA read or write as a burst of regular (PIO) CPU-issued reads or
writes. As such, the drive shall be configured (using the IDE "set features"
command) for PIO data transfer rather than DMA transfer, and bits 9-10 in the
`DMA5_CHCR` register shall be cleared to put the channel in manual sync mode.
The `DRQ` bit in the status register must also be polled manually prior to
starting a transfer to make sure the drive is ready for it.

### RTC registers

The RTC chip is an ST M48T58. This chip behaves like a normal 8192-byte 8-bit
static RAM; in the System 573 it's connected to the lower 8 bits of the
16-bit data bus and should be accessed by performing 16-bit bus accesses and
ignoring/masking out the upper 8 bits (like when accessing IDE/ATAPI control
registers).

As explained in the M48T58 datasheet, the first 8184 bytes are just regular
SRAM while the last 8 bytes are mapped to the RTC. Note that all clock values
are buffered, i.e. they are stored in intermediate registers rather than being
directly read from/written to the clock counters. Bit 6 in the control register
must be set before reading the time to fetch the current time from the clock,
and bit 7 must be set after writing new values to copy them over.

**NOTE**: in the "RWC" column, "C" means the value is updated by the clock
logic when bit 6 in the control register is set.

- `0x1f623ff0` (M48T58 address `0x1ff8`): **Calibration** / **Control**

  | Bits | RWC | Description                                             |
  | ---: | :-- | :------------------------------------------------------ |
  |  0-4 | RW  | Calibration offset (0-31), adjusts oscillator frequency |
  |    5 | RW  | Sign bit for calibration offset                         |
  |    6 | W   | Read trigger, write 1 to update registers from clock    |
  |    7 | W   | Write trigger, write 1 to set clock to match registers  |
  | 8-15 |     | _Unused_                                                |

- `0x1f623ff2` (M48T58 address `0x1ff9`): **Seconds** / **Stop**

  | Bits | RWC | Description                                      |
  | ---: | :-- | :----------------------------------------------- |
  |  0-3 | RWC | Seconds (0-9)                                    |
  |  4-6 | RWC | Tens of seconds (0-5)                            |
  |    7 | RW  | Stop flag, write 1 to pause clock or 0 to resume |
  | 8-15 |     | _Unused_                                         |

- `0x1f623ff4` (M48T58 address `0x1ffa`): **Minutes**

  | Bits | RWC | Description           |
  | ---: | :-- | :-------------------- |
  |  0-3 | RWC | Minutes (0-9)         |
  |  4-6 | RWC | Tens of minutes (0-5) |
  | 7-15 |     | _Unused_              |

- `0x1f623ff6` (M48T58 address `0x1ffb`): **Hours**

  | Bits | RWC | Description                     |
  | ---: | :-- | :------------------------------ |
  |  0-3 | RWC | Hours (0-9, or 0-3 if tens = 2) |
  |  4-5 | RWC | Tens of hours (0-2)             |
  | 6-15 |     | _Unused_                        |

  Hours are always returned in 24-hour format. Unlike other RTC chips there is
  no way to switch to 12-hour format.

- `0x1f623ff8` (M48T58 address `0x1ffc`): **Day of week** / **Century**

  | Bits | RWC | Description                                      |
  | ---: | :-- | :----------------------------------------------- |
  |  0-2 | RWC | Day of week (1-7)                                |
  |    3 |     | _Unused_                                         |
  |    4 | RWC | Century flag                                     |
  |    5 | RW  | Century flag toggling enable, write 0 to disable |
  |    6 | RW  | Enable 512 Hz clock signal output on pin 1       |
  | 7-15 |     | _Unused_                                         |

  The day of week register is an independent counter that is incremented at
  midnight. There is no logic for calculating the day of week, it is the user's
  responsibility to calculate it when changing the time. It's unclear whether
  Konami games interpret 1 as Monday or Sunday.

  Bit 4 is a single-bit "counter" that gets toggled on each turn of the century
  (not something that happens that often). It can be frozen by clearing bit 5.
  Setting bit 6 will route the internal oscillator's output to M48T58 pin 1,
  which does not seem to be connected to anything on the 573.

- `0x1f623ffa` (M48T58 address `0x1ffd`): **Day of month** / **Battery state**

  | Bits | RWC | Description                                          |
  | ---: | :-- | :--------------------------------------------------- |
  |  0-3 | RWC | Day of month (range depends on tens and month)       |
  |  4-5 | RWC | Tens of day of month (range depends on month)        |
  |    6 | R   | Low battery flag (1 = battery voltage is below 2.5V) |
  |    7 | RW  | Battery monitoring enable (1 = enabled)              |
  | 8-15 |     | _Unused_                                             |

- `0x1f623ffc` (M48T58 address `0x1ffe`): **Month**

  | Bits | RWC | Description                     |
  | ---: | :-- | :------------------------------ |
  |  0-3 | RWC | Month (1-9, or 0-2 if tens = 1) |
  |    4 | RWC | Tens of month (0-1)             |
  | 5-15 |     | _Unused_                        |

- `0x1f623ffe` (M48T58 address `0x1fff`): **Year**

  | Bits | RWC | Description        |
  | ---: | :-- | :----------------- |
  |  0-3 | RWC | Year (0-9)         |
  |  4-7 | RWC | Tens of year (0-9) |
  | 8-15 |     | _Unused_           |

  The year counter covers a full century, going from 00 to 99. On each overflow
  the century flag in the day of week register is toggled.

### Other registers

These registers are implemented almost entirely using 74-series logic and the
XC9536 CPLD on the main board.

- `0x1f500000`: **Bank switch** / **Security cartridge**

  | Bits | RW | Description                                              |
  | ---: | :- | :------------------------------------------------------- |
  |  0-5 | W  | Bank number (0-47, see below)                            |
  |    6 | W  | `SDA` direction on security cartridge (0 = input/high-z) |
  |    7 |    | Unknown (goes into CPLD)                                 |
  | 8-15 |    | _Unused_                                                 |

  Bit 6 controls whether `SDA` on the security cartridge is an input or an
  output. If set, `SDA` will output the same logic level as `D0`, otherwise the
  pin will be floating. Bits 0-5 are used to select what shall be mapped to the
  first 4 MB of the expansion region at `0x1f000000`, according to the
  following table:

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

- `0x1f520000`: **JVS reset control?**

  | Bits | RW | Description                           |
  | ---: | :- | :------------------------------------ |
  |  0-6 |    | _Unused_                              |
  |    8 | W  | Reset pin output (0 = pull reset low) |
  | 9-15 |    | _Unused_                              |

  This register hasn't been tested nor confirmed to exist, but it is supposed
  to reset the JVS microcontroller.

- `0x1f560000`: **IDE reset control**

  | Bits | RW | Description                           |
  | ---: | :- | :------------------------------------ |
  |    0 | W  | Reset pin output (0 = pull reset low) |
  | 1-15 |    | _Unused_                              |

  Since the IDE reset pin is active-low, resetting the CD drive is done by
  writing 0 to this register, then waiting a few milliseconds and finally
  writing 1 again. Note that the IDE protocol also specifies a way to
  "soft-reset" devices using the `SRST` bit in the device control register.

- `0x1f5c0000`: **Watchdog clear**

  | Bits | RW | Description |
  | ---: | :- | :---------- |
  | 0-15 |    | _Unused_    |

  This register is a dummy write-only port that clears the watchdog timer
  embedded in the Konami 058232 ASIC when any value is written to it. The
  minimum rate the watchdog must be cleared at is currently unknown, but the
  BIOS and most games seem to write to this port at least once per frame.

  If the watchdog is not constantly cleared, it will generate a reset pulse and
  reboot the 573. There is no way to disable the watchdog other than physically
  modifying the 573 and desoldering the 058232 ASIC (which also drives coin
  counters), or cutting its reset output pin.

- `0x1f600000`: **External outputs?**

  | Bits | RW | Description                        |
  | ---: | :- | :--------------------------------- |
  |  0-7 | RW | To `D0-D7` on `EXT-OUT` connector? |
  | 8-15 |    | _Unused_                           |

  This register hasn't been tested nor confirmed to exist. It is probably
  related to the `EXT-OUT` connector, which seems to just be an 8-bit output
  port.

- `0x1f680000`: **JVS transmit buffer**

  | Bits | RW | Description                       |
  | ---: | :- | :-------------------------------- |
  | 0-15 | W  | JVS data input to microcontroller |

- `0x1f6a0000`: **Security cartridge outputs**

  | Bits | RW | Description                      |
  | ---: | :- | :------------------------------- |
  |  0-7 | RW | To `D0-D7` on security cartridge |
  | 8-15 |    | _Unused_                         |

  The lower 8 bits written to this register go to the cartridge's pins `D0-D7`.
  See the security cartridge section for an explanation of what each pin is
  wired to. Bit 0 additionally controls the `SDA` pin when set to output (see
  the bank switch register). According to MAME, reading from this register will
  yield the last value written to it.

## I/O boards

Having been used in all sorts of games, from DDR to fishing simulators, the
System 573 was designed to be expanded with game-specific hardware using I/O
boards mounted on top of the main board, custom security cartridges or both.
I/O boards have full access to the 16-bit system bus and are mapped to the
`0x1f640000-0x1f6400ff` region.

Several boards are known to exist although so far most of them haven't yet
been documented nor fully emulated in MAME.

### Analog I/O board (`GX700-PWB(F)`)

The name is misleading as the board does not deal with any analog signals
whatsoever, all it does is providing a few registers for controlling lights on
the cabinet through high-current optocouplers. The name was given retroactively
to differentiate it from the digital I/O board.

This board provides up to 32 light outputs through 4 connectors. See the
game-specific information section for details on how lights are wired up on
each cabinet type.

- `0x1f640040`: **Light control 0**

  | Bits | RW | Description       |
  | ---: | :- | :---------------- |
  |    0 | W  | To light output 3 |
  |    1 | W  | To light output 2 |
  |    2 | W  | To light output 7 |
  |    3 | W  | To light output 6 |
  |    4 | W  | To light output 5 |
  |    5 | W  | To light output 4 |
  |    6 | W  | To light output 1 |
  |    7 | W  | To light output 0 |
  | 8-15 |    | Unused            |

- `0x1f640044`: **Light control 1**

  | Bits | RW | Description        |
  | ---: | :- | :----------------- |
  |    0 | W  | To light output 11 |
  |    1 | W  | To light output 10 |
  |    2 | W  | To light output 15 |
  |    3 | W  | To light output 14 |
  |    4 | W  | To light output 13 |
  |    5 | W  | To light output 12 |
  |    6 | W  | To light output 9  |
  |    7 | W  | To light output 8  |
  | 8-15 |    | Unused             |

- `0x1f640048`: **Light control 2**

  | Bits | RW | Description        |
  | ---: | :- | :----------------- |
  |    0 | W  | To light output 19 |
  |    1 | W  | To light output 18 |
  |    2 | W  | To light output 23 |
  |    3 | W  | To light output 22 |
  |    4 | W  | To light output 21 |
  |    5 | W  | To light output 20 |
  |    6 | W  | To light output 17 |
  |    7 | W  | To light output 16 |
  | 8-15 |    | Unused             |

- `0x1f64004c`: **Light control 3**

  | Bits | RW | Description        |
  | ---: | :- | :----------------- |
  |    0 | W  | To light output 27 |
  |    1 | W  | To light output 26 |
  |    2 | W  | To light output 31 |
  |    3 | W  | To light output 30 |
  |    4 | W  | To light output 29 |
  |    5 | W  | To light output 28 |
  |    6 | W  | To light output 25 |
  |    7 | W  | To light output 24 |
  | 8-15 |    | Unused             |

### Digital I/O board (`GX894-PWB(B)A`)

This board was used for pretty much all Bemani games besides earlier ones which
used CD audio and the analog I/O board. In addition to the usual light control
circuitry, this board features an FPGA and an MPEG decoder ASIC to play
encrypted MP3 files. The FPGA has 24 MB of dedicated RAM onto which the files
are preloaded on startup, then decrypted on the fly and fed to the decoder. The
board also features two RCA jacks for communication with other cabinets and a
64-bit unique serial number, copied to the security cartridge during
installation in order to prevent operators from installing the same game on
multiple systems.

**NOTE**: the vast majority of the registers provided by this board (including
light control) are handled by its FPGA, which requires a configuration
bitstream to be uploaded to it through the appropriate register in order to
work. There are two known versions of Konami's bitstream, with the only
difference being the decryption algorithm. All games that use the digital I/O
board upload the bitstream to the FPGA on startup before accessing any other
register.

A homebrew game would have to do the same, however distributing Konami's
bitstream would be problematic from a copyright standpoint. **The digital I/O**
**board is thus currently unusable by homebrew**. This might change in the
future if a custom FPGA bitstream is ever going to be developed; the custom
bitstream would not only skip decryption but also implement a custom set of
registers (rather than the ones described below), sidestepping the lack of
documentation entirely.

- `0x1f6400e0`: **Light control 1** (implemented by bitstream)

  | Bits | RW | Description       |
  | ---: | :- | :---------------- |
  | 0-11 |    | Unused?           |
  |   12 | W  | To light output 4 |
  |   13 | W  | To light output 7 |
  |   14 | W  | To light output 5 |
  |   15 | W  | To light output 6 |

- `0x1f6400e2`: **Light control 0** (implemented by bitstream)

  | Bits | RW | Description       |
  | ---: | :- | :---------------- |
  | 0-11 |    | Unused?           |
  |   12 | W  | To light output 0 |
  |   13 | W  | To light output 3 |
  |   14 | W  | To light output 1 |
  |   15 | W  | To light output 2 |

- `0x1f6400e4`: **Light control 3** (implemented by bitstream)

  | Bits | RW | Description        |
  | ---: | :- | :----------------- |
  | 0-11 |    | Unused?            |
  |   12 | W  | To light output 12 |
  |   13 | W  | To light output 15 |
  |   14 | W  | To light output 13 |
  |   15 | W  | To light output 14 |

- `0x1f6400e6`: **Light control 7** (implemented by bitstream)

  | Bits | RW | Description        |
  | ---: | :- | :----------------- |
  | 0-11 |    | Unused?            |
  |   12 | W  | To light output 28 |
  |   13 | W  | To light output 31 |
  |   14 | W  | To light output 29 |
  |   15 | W  | To light output 30 |

- `0x1f6400f6`: **FPGA status**

- `0x1f6400f8`: **FPGA bitstream upload**

- `0x1f6400fa`: **Light control 4** (implemented by bitstream)

  | Bits | RW | Description        |
  | ---: | :- | :----------------- |
  | 0-11 |    | Unused?            |
  |   12 | W  | To light output 16 |
  |   13 | W  | To light output 19 |
  |   14 | W  | To light output 17 |
  |   15 | W  | To light output 18 |

- `0x1f6400fc`: **Light control 5** (implemented by bitstream)

  | Bits | RW | Description        |
  | ---: | :- | :----------------- |
  | 0-11 |    | Unused?            |
  |   12 | W  | To light output 20 |
  |   13 | W  | To light output 23 |
  |   14 | W  | To light output 21 |
  |   15 | W  | To light output 22 |

- `0x1f6400fe`: **Light control 2** (implemented by bitstream)

  | Bits | RW | Description        |
  | ---: | :- | :----------------- |
  | 0-11 |    | Unused?            |
  |   12 | W  | To light output 8  |
  |   13 | W  | To light output 11 |
  |   14 | W  | To light output 9  |
  |   15 | W  | To light output 10 |

- `0x1f6400ee`: **DS2401 ID chip** (implemented by bitstream)

### Alternate analog I/O board (`GX700-PWB(K)`)

This board is currently undocumented.

### Fishing controls board (`GE765-PWB(B)A`)

This board is currently undocumented.

### DDR Karaoke Mix I/O board (`GX921-PWB(B)`)

This board is currently undocumented.

### Gun Mania I/O board (`GX700-PWB(K)A`)

This board is currently undocumented.

### Hypothetical debugging board

There is no proof whatsoever of this board having ever existed, but the BIOS
and some games attempt to access the hardware on it. In particular it seems to
contain at least a Fujitsu MB89371 UART and a 7-segment display, although these
might have actually been on two separate boards. The only game known to access
the serial ports is Great Bishi Bashi Champ.

The MB89371 does not have a publicly available datasheet.

- `0x1f640000`: **UART data**

- `0x1f640002`: **UART control**

- `0x1f640004`: **UART baud rate select**

- `0x1f640006`: **UART mode**

- `0x1f640010`: **7-segment display**

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

  The BIOS shell shows "00" on this display (but contains a function to show
  any hexadecimal value). Kick &amp; Kick shows an animated spinner, some other
  games show error or status codes on it. This might have been meant to be a
  POST display to be integrated into the 573 main board at some point.

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

| Name (on PCB)   | Type | Used by           | Additional I/O connectors            | Additional hardware                                   |
| :-------------- | :--- | :---------------- | :----------------------------------- | :---------------------------------------------------- |
| `GX700-PWB(D)`  | X    | Analog I/O games  |                                      | _Unpopulated (T)QFP footprint_                        |
| `GX894-PWB(D)`  | XI?  | Unknown           |                                      | _Unpopulated SOIC footprints_                         |
| `GX700-PWB(J)`  | XI   | PunchMania        | Analog in (12-pin), unknown (10-pin) | SPI ADC chip for analog inputs                        |
| `GX883-PWB(D)`  | XI   | Digital I/O games | Network (5-pin), amp box (6-pin)     | RS-232 transceiver powered by isolated DC-DC module   |
| `GE949-PWB(D)A` | ZI   | Digital I/O games | Network (5-pin), amp box (6-pin)     | RS-232 transceiver powered by isolated DC-DC module   |
| `GE949-PWB(D)B` | ZI   | Digital I/O games | Unpopulated 5-pin, 6-pin             | _Same as above but only security chips are populated_ |
| `PWB0000068819` | X    | Hyper BB Champ    | 12V input (4-pin), lights (16-pin)   | Latch controlled light outputs                        |
| `PWB0000088954` | XI   | Salary Man Champ  | 12V input (4-pin), lights (16-pin)   | Shift register controlled light outputs               |

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

#### Different game/install cartridges

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

## External modules

Over the 573's lifetime Konami introduced several add-ons that extended its
functionality. Unlike the I/O boards, these were external to the 573 unit and
usually optional, although some later games started to require them in order to
boot. Not much is currently known about any of these.

- **PS1 controller/memory card adapter**: sits between the 573 and any panel
  mounted memory card (and sometimes controller) ports. It has an internal
  Toshiba TMPR3904 CPU that handles communication with the cards and connects
  to the 573 via the JVS bus.
- **e-Amusement network unit** (used by later GFDM games): connects to the 573
  through PCMCIA, using a cable that ends in a dummy card. Once again it has
  its own processor - a Toshiba TMPR3927 running at 133 MHz with 8 MB of RAM,
  far more powerful than the 573 itself - as well as an internal 2.5-inch IDE
  drive and a PCI Ethernet chip. It seems to run a proprietary kernel provided
  by Toshiba known as UDEOS.
- **Multi-session unit** (used by some Bemani games): it has yet another
  TMPR3927, an FPGA and 4 (!) MPEG decoder chips. It comes with 3 or 4
  daughterboards installed, each of which hosts a stereo I2S DAC and has RCA
  jacks for audio input and output. The box also has its own CD drive and power
  supply. Its purpose is to enable "session mode", which allows for the same
  song to be played on multiple games at the same time, with the box playing
  the backing track and routing audio between the cabinets. It connects to each
  cabinet's 573 using RS-232, through the "network" port on the security
  cartridge.
- **Master calendar**: this was a JVS device used by Konami to program security
  cartridges at the factory. All games that use a security cartridge search the
  JVS bus on startup and enter a "factory test" mode if a device identifying as
  a master calendar is connected. The game will then proceed to initialize the
  cartridge after an authentication handshake with the master calendar. Even
  though nothing is known about the actual hardware Konami used, this device
  has been successfully replicated using an Arduino (see the links section).

## Connectors

This is (a good approximation of) what the front panel of a 573 looks like:

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
   front panel that blocks access to the eject button for whatever reason.
2. **Sub-panels**: the gray variant of the case has a cutout for a plate to
   hold additional I/O connectors here. Different games have different plates,
   see the game-specific information section for details on which connectors
   are broken out for each game. There is another sub-panel cutout on the back
   of the 573 as well, used by some I/O boards to expose additional ports.
3. **Security cartridge**: cartridges are inserted into a slot on the 573's
   right side and locked in place by plastic tabs. Hotplugging cartridges while
   the system is powered on will result in *permanent* damage to the cartridge,
   the 573 or both due to ESD (this has been proven to happen).
4. **JAMMA**: this is a standard PCB edge connector used in arcade systems,
   carrying 5V and 12V power rails, analog RGB video, a mono speaker output
   (wired to the left channel of the built-in amp, see below) and button and
   coin inputs. The 573 doesn't use the negative 5V rail.
5. **DIP switches**: a set of four DIP switches for quick game configuration.
   The first three are used by some games (and can be freely used by homebrew)
   while the last one is reserved by the BIOS and used to select whether to
   boot from the CD or from the internal flash.
6. **JVS "USB" port**: as already mentioned this is not an actual USB port but
   rather a serial bus which can be used to connect peripherals and external
   I/O boards. As the underlying protocol is RS-485, multiple devices can be
   daisy chained.
7. **"VGA" and RCA outputs**: these are also mandated by the JVS specification
   and are useful for hooking the system up for testing without needing a JAMMA
   "supergun" or similar adapter. Note that the VGA connector does not output
   standard VGA with separate h-sync and v-sync but 240p/480i RGB with c-sync
   only, i.e. it's closer to SCART than it is to VGA. An upscaler such as the
   GBS8200 (which has a VGA input that supports c-sync) is required to connect
   the 573 to anything other than a CRT TV.
8. **Speaker outputs**: the 573 has a built-in 15W amplifier, which can be used
   for either mono output (via the speaker pins on the JAMMA connector) or for
   stereo through this 4-pin connector. Bemani cabs do not use this output,
   relying on a more powerful external amp plugged into the RCA jacks instead.

## Game-specific information

### Sub-panels

Black/blue case models, most commonly used in Fisherman's Bait and in a few
non-Bemani games that do not require I/O boards, have no sub-panel cutouts and
instead expose some of the built-in ports through a handful of connectors:

- **Power**: a hefty 2x4 Molex connector for powering the board, wired to the
  motherboard's power connector. 
- **Option 1**: DE9 connector providing 8 analog inputs, wired to the
  `ANALOG` connector on the motherboard. These inputs seem to go directly
  into the 573's ADC chip *with no protection whatsoever*.
- **Option 2**: DE9 connector providing 8 digital (3.3V?) inputs, wired to the
  `EXT-IN` connector on the motherboard.
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
|      0 | Player 1 up arrow           |
|      1 | Player 1 left arrow         |
|      2 | Player 1 right arrow        |
|      3 | Player 1 down arrow         |
|      4 | Data to player 1 stage I/O  |
|    5-6 | _Unused_                    |
|      7 | Clock to player 1 stage I/O |
|      8 | Player 2 up arrow           |
|      9 | Player 2 left arrow         |
|     10 | Player 2 right arrow        |
|     11 | Player 2 down arrow         |
|     12 | Data to player 2 stage I/O  |
|  13-14 | _Unused_                    |
|     15 | Clock to player 2 stage I/O |
|     16 | _Unused_                    |
|     17 | Player 1 buttons            |
|     18 | Player 2 buttons            |
|     19 | _Unused_                    |
|     20 | Bottom right marquee light  |
|     21 | Bottom left marquee light   |
|     22 | Top left marquee light      |
|     23 | Top right marquee light     |
|  24-27 | _Unused_                    |
|     28 | Speaker neon (digital I/O)  |
|     29 | _Unused_                    |
|     30 | Speaker neon (analog I/O)   |
|     31 | _Unused_                    |

Light outputs 4, 7, 12 and 15 do not actually control any lamps, but are used
to communicate with each stage's I/O board. See below for details.

### DDR stage I/O board

In Dance Dance Revolution cabinets, the sensors in each stage's arrow panels
are not connected directly to the 573 but go through a board commonly known as
the "stage I/O". This board, based on a Xilinx XC9536 CPLD, has two purposes:
allowing the 573 to check the status of a specific pressure sensor (each panel
has 4 sensors, one along each edge) and ensuring DDR games can only be played
with an actual stage, rather than just a joystick or buttons wired up to the
573's JAMMA connector. Konami kept using the same board long after the 573 was
discontinued, with the last game to use it being DDR X/X2.

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

### DrumMania light mapping

First-generation DrumMania cabinets (*unofficially* called "1st Mix") have
lights wired up to the I/O board as follows:

| Output | Connected to  |
| -----: | :------------ |
|   0-15 | _Unused_      |
|     16 | Hi-hat        |
|     17 | High tom      |
|     18 | Low tom       |
|     19 | Snare         |
|     20 | Cymbal        |
|     21 | Start button  |
|     22 | Select button |
|  23-26 | _Unused_      |
|     27 | Bottom neon   |
|  28-29 | _Unused_      |
|     30 | Spotlight     |
|     31 | Top neon      |

The wiring was changed in 2nd Mix and later cabinets, which use the following
mapping instead:

| Output | Connected to  |
| -----: | :------------ |
|      0 | Hi-hat        |
|      1 | High tom      |
|      2 | Low tom       |
|      3 | Snare         |
|    4-7 | _Unused_      |
|      8 | Spotlight     |
|      9 | Top neon      |
|     10 | _Unused_      |
|     11 | Bottom neon   |
|     12 | Cymbal        |
|     13 | Start button  |
|     14 | Select button |
|  15-31 | _Unused_      |

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
  lights and eject the CD (as some cases block access to the drive's eject
  button for whatever reason).

### Known working replacement drives

This is an incomplete list of drives that are known to work (or to be
incompatible) with Konami's ATAPI driver, used by both the BIOS and games. Note
that CD-DA support is problematic due to the way Konami's code reads the disc's
table of contents. Thus, very few drives are confirmed to work with games that
use CD-DA (i.e. pretty much all games that don't use the digital I/O board).

| Manufacturer | Model        | BIOS    | CD-DA   | Notes                        |
| :----------- | :----------- | :------ | :------ | :--------------------------- |
| ASUSTeK      | DVD-E616P3   | **Yes** | Unknown |                              |
| Compaq       | 179137-701   | **Yes** | **Yes** |                              |
| Creative     | CD4832E      | **Yes** | No      |                              |
| Hitachi      | CDR-7930     | **Yes** | No      |                              |
| LG           | GCR-8523B    | **Yes** | Unknown |                              |
| LG           | GDR-8163B    | **Yes** | **Yes** |                              |
| LG           | GDR-8164B    | **Yes** | **Yes** |                              |
| LG           | GH22NP20     | **Yes** | Unknown |                              |
| Lite-On      | LH-18A1H     | **Yes** | **Yes** |                              |
| Lite-On      | LTD-163      | **Yes** | Unknown |                              |
| Lite-On      | LTD-165H     | **Yes** | Unknown |                              |
| Lite-On      | LTR-40125S   | **Yes** | Unknown |                              |
| Lite-On      | XJ-HD166S    | **Yes** | Unknown |                              |
| Matsushita   | CR-583       | **Yes** | **Yes** | Stock drive                  |
| Matsushita   | CR-587       | **Yes** | **Yes** | Stock drive, can't read CD-R |
| Matsushita   | CR-589B      | **Yes** | **Yes** | Stock drive                  |
| Matsushita   | SR8589B      | **Yes** | Unknown |                              |
| Mitsumi      | CRMC-FX4830T | **Yes** | Unknown |                              |
| NEC          | CDR-1900A    | **Yes** | Unknown |                              |
| NEC          | ND-2510A     | No      |         |                              |
| Panasonic    | CR-594C      | **Yes** | Unknown |                              |
| Sony         | DRU-510A     | **Yes** | Unknown |                              |
| Sony         | DRU-810A     | **Yes** | Unknown |                              |
| TDK          | AI-481648B   | **Yes** | Unknown |                              |
| TEAC         | CD-W552E     | **Yes** | Unknown |                              |
| Toshiba      | XM-5702B     | **Yes** | Unknown |                              |
| Toshiba      | XM-6102B     | **Yes** | No      | Has issues with homebrew     |

## Credits, sources and links

This document is the result of a joint effort consisting of months if not years
of original research, brought to you by:

- **spicyjpeg** (documentation writing, hardware test coding)
- **Naoki Saito** (hardware reverse engineering, schematic tracing, tests)
- **smf** (initial reverse engineering and implementation of the 573 MAME
  driver)
- **Grandstand** (tests with security cartridges and ATAPI drives)
- **Shiz** (security cartridge details)

Traced schematics, datasheets and additional resources are available in
[Naoki's 573 repo](https://github.com/NaokiS28/KSystem-573). Shiz also
maintains a [documentation repo](https://github.com/Shizmob/arcade-docs) for
several arcade systems including the 573.

In addition to original research, some information has been aggregated from the
following sources:

- [System 573 MAME driver](https://github.com/mamedev/mame/blob/master/src/mame/konami/ksys573.cpp)
- [windyfairy/987123879113's MAME fork](https://github.com/987123879113/mame)
  and [gobbletools](https://github.com/987123879113/gobbletools)
- ATAPI specification (revision 2.6, January 1996)
- M48T58, ADC0834, X76F041 and X76F100 datasheets
- [DDR stage I/O protocol notes](https://github.com/nchowning/open-io/blob/master/NOTES.txt)
- [List of working ATAPI drives](https://gamerepair.info/hardware/1_system_573)
- ["The Almost Definitive Guide to Session Mode Linking"](https://www2.gvsu.edu/brittedg/SessionGuide.pdf)
- [Japanese page about drummania](https://callusnext.com/pcbs/system573_dm.html)
  (has network adapter and multisession unit pictures)
- [Light output for Salary Man Champ](http://solid-orange.com/1569) and
  [Hyper Bishi Bashi Champ](http://solid-orange.com/1581)
- [system573\_tool](https://github.com/onikutaro/system573_tool) (possibly the
  first ever homebrew app for the 573)
- [Arduino-based master calendar clone](https://www.arcade-projects.com/threads/konami-system-573-master-calendar.2646/#post-34907)
- [Z-I-v forum post with security cartridge info](https://zenius-i-vanisher.com/v5.2/viewthread.php?threadid=2825)

Huge thanks to the Rhythm Game Cabs Discord server and everyone who provided
valuable information about the 573!
