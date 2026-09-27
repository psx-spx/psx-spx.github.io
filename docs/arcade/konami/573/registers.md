## Register map

All standard PS1 registers, with the exception of the CD-ROM drive's, are
present and accessible. System 573-specific hardware is mapped into the DEV0
region at `0x1f000000`. IRQ10 and DMA5, normally reserved for the expansion bus
(and lightguns) on a regular PS1, are used to access the ATAPI drive, while IRQ2
and DMA3 go unused.

**NOTE**: DEV0 must be configured prior to accessing any of these registers. The
configuration value written by Konami's code to the DEV0 delay/size register at
`0x1f801008` is `0x24173f47`. Afterwards, *all* bus writes shall be 16 or 32
bits wide. The behavior of 8-bit writes is undefined, but 8-bit reads work as
intended.

| Address range           | Description                                            |
| :---------------------- | :----------------------------------------------------- |
| `0x1f000000-0x1f3fffff` | Bank switched, can be mapped to flash or PCMCIA slots  |
| `0x1f400000-0x1f40000f` | [Konami ASIC registers](builtin-io.md#konami-asic-registers)        |
| `0x1f480000-0x1f48000f` | [IDE register bank 0](#ide-registers)                  |
| `0x1f4c0000-0x1f4c000f` | [IDE register bank 1](#ide-registers)                  |
| `0x1f620000-0x1f623fff` | [RTC registers](#rtc-registers) and battery-backed RAM |
| `0x1f640000-0x1f6400ff` | [I/O board registers](expansion-io.md#io-boards)                      |
| `0x1f500000-0x1f6a0001` | [Other registers](#other-registers)                    |

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
|    6 | W  | `IO0` direction on security cartridge (0 = input/high-z) |
|    7 |    | Unknown (goes into CPLD)                                 |
| 8-15 |    | _Unused_                                                 |

Bit 6 controls whether `IO0` on the security cartridge is an input or an output.
If set, `IO0` will output the same logic level as `D0`, otherwise the pin will
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

#### `0x1f6a0000`: **Security cartridge outputs**

| Bits | RW | Description                      |
| ---: | :- | :------------------------------- |
|  0-7 | W  | To `D0-D7` on security cartridge |
| 8-15 |    | _Unused_                         |

The lower 8 bits written to this register are latched on pins `D0-D7` of the
cartridge slot. See the security cartridge section for an explanation of what
each pin is wired to. Bit 0 additionally controls the `IO0` pin when configured
as an output through the bank switch register. Writing to this register will set
the `DRDY` flag, which can then be cleared by the cartridge.
