## Pinouts

- [Main board pinouts (`GX700-PWB(A)`)](#main-board-pinouts-gx700-pwba)
- [Analog I/O board pinouts (`GX700-PWB(F)`)](#analog-io-board-pinouts-gx700-pwbf)
- [Digital I/O board pinouts (`GX894-PWB(B)A`)](#digital-io-board-pinouts-gx894-pwbba)
- [Security cartridge pinouts](#security-cartridge-pinouts)

### Main board pinouts (`GX700-PWB(A)`)

#### RGB Output ('DB15')

Labelled RGB out, this is following the usual VGA pinout but it is not VGA compatible as
it uses 15 KHz C-Sync instead of 31 KHz H/V-Sync and a nominal resolution of 320x240p
compared to 640x480p.

| Pin | Name      | Dir |
| --: | :-------- | :-- |
|   1 | `R`       | O   |
|   2 | `G`       | O   |
|   3 | `B`       | O   |
|   4 | `NC`      |     |
|   5 | `GND`     |     |
|   6 | `GND`     |     |
|   7 | `GND`     |     |
|   8 | `GND`     |     |
|   9 | `NC`      |     |
|  10 | `GND`     |     |
|  11 | `NC`      |     |
|  12 | `NC`      |     |
|  13 | `C-Sync`  | O   |
|  14 | `V-Sync*` | O   |
|  15 | `NC`      |     |

Note *: Pin 14 signal is not normally present. There is an unmarked two-pin header near the 
RGB out port which when bridged will join this pin to V-Sync.

#### Analog input port (`ANALOG`, `CN3`)

The inputs are wired directly to the 573's built-in ADC with no protection, so
they can only accept voltages in 0-5V range. This connector is usually used for
potentiometers and similar resistive analog controls.

| Pin | Name  | Dir |
| --: | :---- | :-- |
|   1 | `5V`  |     |
|   2 | `5V`  |     |
|   3 | `NC`  |     |
|   4 | `NC`  |     |
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
|   6 | `RX`     | I   |                              |  28 | `IO0`    | IO  |                                    |
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
|  A5 | `GND`  |     |  B5 | `V-SYNC` | O   |
|  A6 | `GND`  |     |  B6 | `H-SYNC` | O   |
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

#### H8/3644 JVS MCU pin mapping

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

#### Digital I/O XC9536 CPLD pin mapping

| Pin | JTAG | CPLD alt. | Dir | Connected to | Usage                                |
| --: | ---: | :-------- | :-- | :----------- | :----------------------------------- |
|   1 |   51 |           | IO  | System bus   | Data bus bit 15                      |
|   2 |  105 |           | IO  | System bus   | Data bus bit 14                      |
|   3 |  102 |           | IO  | System bus   | Data bus bit 13                      |
|   4 |   96 |           | IO  | System bus   | Data bus bit 12                      |
|   5 |   99 | `GCK1`    |     | Unknown      | Unknown (system clock?)              |
|   6 |   93 | `GCK2`    |     |              | _Unused_                             |
|   7 |   87 | `GCK3`    | O   | Light bank B | Output B3                            |
|   8 |   90 |           | O   | Light bank B | Output B2                            |
|   9 |   84 |           | O   | Light bank B | Output B1                            |
|  11 |   81 |           | O   | Light bank B | Output B0                            |
|  12 |   78 |           | O   | Light bank C | Output C7                            |
|  13 |   75 |           | O   | Light bank C | Output C6                            |
|  14 |   72 |           | O   | Light bank C | Output C5                            |
|  18 |   69 |           | O   | Light bank C | Output C4                            |
|  19 |   66 |           | O   | Light bank C | Output C3                            |
|  20 |   63 |           | O   | Light bank C | Output C2                            |
|  22 |   60 |           | O   | Light bank C | Output C1                            |
|  24 |   57 |           | O   | Light bank C | Output C0                            |
|  25 |    3 |           | O   | Audio DAC    | Chip reset/mute                      |
|  26 |    6 |           | ?   | FPGA         | Configuration status/reset (`/INIT`) |
|  27 |    9 |           | ?   | FPGA         | Configuration status (`DONE`)        |
|  28 |   12 |           | O   | FPGA         | Configuration reset (`/PROGRAM`)     |
|  29 |   15 |           | O   | FPGA         | Configuration data (`DIN`)           |
|  33 |   18 |           | O   | FPGA         | Configuration bit clock (`CCLK`)     |
|  34 |   21 |           | I   | System bus   | I/O board chip select (`/CS?`)       |
|  35 |   24 |           | I   | System bus   | Read/write strobe?                   |
|  36 |   27 |           | I   | System bus   | Read/write strobe?                   |
|  37 |   30 |           | I   | System bus   | Address bus bit 7                    |
|  38 |   33 |           | I   | System bus   | Address bus bit 6                    |
|  39 |   36 | `GSR`     | I   | System bus   | Address bus bit 5                    |
|  40 |   39 | `GTS2`    | I   | System bus   | Address bus bit 4                    |
|  42 |   45 | `GTS1`    | I   | System bus   | Address bus bit 3                    |
|  43 |   42 |           | I   | System bus   | Address bus bit 2                    |
|  44 |   48 |           | I   | System bus   | Address bus bit 1                    |

#### Digital I/O XCS40XL FPGA pin mapping

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
|    77 |  423 | `/INIT`       | IO  | -     | -    | CPLD                 | Configuration status/reset       |
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
|    98 |  495 |               | O   |       | Slow | ARCnet transceiver   | Network TX enable (same as TX)   |
|    99 |  498 |               | O   |       | Slow | ARCnet transceiver   | Network TX                       |
|   100 |  501 |               | I   | Yes   |      | ARCnet transceiver   | Network RX                       |
|   101 |  504 |               |     |       |      |                      | _Unused_                         |
|   102 |  507 | `GCK4`        |     |       |      |                      | _Unused_                         |
|   104 |      | `DONE`        | IO  | -     | -    | CPLD                 | Configuration status             |
|   106 |      | `/PROGRAM`    | I   | -     | -    | CPLD                 | Configuration reset              |
|   107 |  510 | `D7`          | IO  | No    | Slow | DS2433 (unpopulated) | Unused 1-wire bus (open-drain)   |
|   108 |  513 | `GCK5`        |     |       |      |                      | _Unused_                         |
|   109 |  516 |               | IO  | No    | Slow | DS2401               | 1-wire bus (open-drain)          |
|   110 |  519 |               | I   | No    |      | System bus           | Address bus bit 7                |
|   111 |  525 |               |     |       |      |                      | _Unused_                         |
|   112 |  534 | `D6`          | I   | No    |      | System bus           | Address bus bit 6                |
|   113 |  537 |               | I   | No    |      | System bus           | Address bus bit 5                |
|   114 |  540 |               | I   | No    |      | System bus           | Address bus bit 4                |
|   115 |  543 |               | I   | No    |      | System bus           | Address bus bit 3                |
|   116 |  546 |               | I   | No    |      | System bus           | Address bus bit 2                |
|   117 |  549 |               | I   | No    |      | System bus           | Address bus bit 1                |
|   119 |  558 |               | O   |       | Slow | Unknown              | Unknown                          |
|   120 |  561 |               | IO  | Yes   | Slow | System bus           | Data bus bit 15                  |
|   122 |  564 | `D5`          | IO  | Yes   | Slow | System bus           | Data bus bit 14                  |
|   123 |  567 |               | IO  | Yes   | Slow | System bus           | Data bus bit 13                  |
|   124 |  576 |               | IO  | Yes   | Slow | System bus           | Data bus bit 12                  |
|   125 |  579 |               | IO  | Yes   | Slow | System bus           | Data bus bit 11                  |
|   126 |  582 |               | IO  | Yes   | Slow | System bus           | Data bus bit 10                  |
|   127 |  585 |               | IO  | Yes   | Slow | System bus           | Data bus bit 9                   |
|   128 |  588 | `D4`          | IO  | Yes   | Slow | System bus           | Data bus bit 8                   |
|   129 |  591 |               | IO  | Yes   | Slow | System bus           | Data bus bit 7                   |
|   132 |  594 | `D3`          | IO  | Yes   | Slow | System bus           | Data bus bit 6                   |
|   133 |  597 |               | IO  | Yes   | Slow | System bus           | Data bus bit 5                   |
|   134 |  600 |               | IO  | Yes   | Slow | System bus           | Data bus bit 4                   |
|   135 |  603 |               | IO  | Yes   | Slow | System bus           | Data bus bit 3                   |
|   136 |  606 |               | IO  | Yes   | Slow | System bus           | Data bus bit 2                   |
|   137 |  609 |               | IO  | Yes   | Slow | System bus           | Data bus bit 1                   |
|   138 |  618 | `D2`          | IO  | Yes   | Slow | System bus           | Data bus bit 0                   |
|   139 |  621 |               |     |       |      |                      | _Unused_                         |
|   141 |  624 |               |     |       |      |                      | _Unused_                         |
|   142 |  627 |               | I   | No    |      | System bus           | I/O board chip select (`/CS?`)   |
|   144 |  639 |               |     |       |      |                      | _Unused_                         |
|   145 |  642 |               | I   | No    |      | System bus           | Write strobe (`/WR0`)            |
|   146 |  645 |               | I   | No    |      | System bus           | Read strobe (`/RD`)              |
|   147 |  648 |               |     |       |      |                      | _Unused_                         |
|   148 |  651 |               | I   | No    |      | MAS3507D             | MP3 data request flag (`PI19`)   |
|   149 |  654 | `D1`          | O   |       | Slow | MAS3507D             | PIO chip select (`/PCS`)         |
|   150 |  657 |               | IO  | No    | Slow | MAS3507D             | I2C `SDA`                        |
|   151 |  666 |               | IO  | No    | Slow | MAS3507D             | I2C `SCL`                        |
|   152 |  669 |               | O   |       | Slow | MAS3507D             | Chip reset (`/POR`)              |
|   153 |  672 | `D0`/`DIN`    | I   | -     | -    | CPLD                 | Configuration data               |
|   154 |  675 | `GCK6`/`DOUT` |     |       |      |                      | _Unused_                         |
|   155 |      | `CCLK`        | I   | -     | -    | CPLD                 | Configuration bit clock          |
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
- Light outputs must be configured as open-drain in order to work properly. The
  optocouplers' anodes are fed 5V rather than 3.3V; setting the outputs high
  instead of putting them into high-z will result in a voltage difference of
  ~1.7V across the optocouplers' LEDs, which is enough to trigger them.
- The "5V tolerant I/O" option in Xilinx's bitstream generator **must** be
  enabled when building custom bitstreams. There are no level shifters between
  the FPGA and the 573's system bus.
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
