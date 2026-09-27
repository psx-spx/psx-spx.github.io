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

| SHA-1 (41337 bytes, LSB first)             | First used by                          |
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
Beat bitstreams seem to behave in a completely different way.

Homebrew software may also load custom bitstreams developed using the Xilinx ISE
4.2 toolchain (the last version to support Spartan-XL parts). The following
custom bitstreams are known to exist so far:

| SHA-1 (41337 bytes, LSB first)             | First used by               |
| :----------------------------------------- | :-------------------------- |
| `9d5acaae61f03f4d71831ebdb013af6189802ed2` | 573in1 1.0.0                |
| `e9212e9ff24fa876158f510e3c17649a110f60a4` | 573in1 (development branch) |

#### `0x1f640080` (FPGA, all bitstreams): **Magic number**

| Bits | RW | Description                                                                   |
| ---: | :- | :---------------------------------------------------------------------------- |
| 0-15 | R  | Magic number (`0x1234` for Konami bitstreams, `0x573f` for 573in1 bitstreams) |

This register is checked by some versions of Konami's digital I/O board driver
to make sure the bitstream was properly loaded.

#### `0x1f640082` (FPGA, 573in1 bitstream): **Configuration**

| Bits | RW | Description                                                                                 |
| ---: | :- | :------------------------------------------------------------------------------------------ |
|  0-7 | R  | Bitstream version (currently `0x02`)                                                        |
|    8 | RW | MP3 looping enable (1 = continue playing from start address when end address is reached)    |
|    9 | RW | Automatically clear DAC sample counter registers when starting MP3 playback (1 = clear)     |
|   10 | RW | Automatically clear register `0x1f6400cc` when DAC sample counter delta is read (1 = clear) |
|   11 | RW | Automatically disable sample counter if cleared while MP3 playback is stopped (1 = disable) |
|   12 | RW | Primary MP3 descrambler key (0 = `key1`, 1 = scrambled XOR of `key1` and `key2`)            |
|   13 | RW | Secondary MP3 descrambler key (0 = none, 1 = scrambled counter initialized from `key3`)     |
|   14 | RW | MP3 data feeder endianness (0 = read bits 15-8 then 7-0, 1 = read bits 7-0 then 15-8)       |
|   15 | RW | Swap bits 14 and 15 of `key1` when mutating it (1 = swap)                                   |

Custom register only implemented by the 573in1 bitstream, in order to allow for
emulation of quirks present in different versions of Konami's bitstreams as well
as control some additional features.

Bits 9-11 tune the behavior of the DAC sample counter registers (`0x1f6400ca`,
`0x1f6400cc` and `0x1f6400cf`). Setting all of them will make the registers
replicate the behavior of those provided by the DDR 3rdMIX bitstream onwards,
while clearing them will bring them closer to the earlier DDR Solo Bass Mix
bitstream's behavior.

Bits 12, 13 and 15 control the MP3 decryption algorithm. All of them shall be
set to decrypt MP3 files from DDR 3rdMIX onwards (scrambled with `key1`, `key2`
and `key3`) or cleared to play DDR Solo Bass Mix files (scrambled with `key1`
only). Bit 14 controls which byte of each 16-bit word in DRAM is fed to the
MAS3507D first and should be cleared for encrypted MP3 playback.

The 573in1 bitstream's descrambler can be configured to play unencrypted data by
performing the following steps:

- clear bits 12, 13 and 15;
- set bit 14 (encrypted MP3s are byte swapped as part of the scrambling process
  but an unencrypted file will have to be swapped during playback);
- clear `key1` by writing zero to register `0x1f6400a8`, which will render the
  decryption step a no-op.

#### `0x1f640090` (FPGA, all bitstreams): **Network board address**

#### `0x1f640092` (FPGA, all bitstreams): **Unknown (network related)**

#### `0x1f6400a0` (FPGA, all bitstreams): **MP3 data start address high**

#### `0x1f6400a2` (FPGA, all bitstreams): **MP3 data start address low**

#### `0x1f6400a4` (FPGA, all bitstreams): **MP3 data end address high**

#### `0x1f6400a6` (FPGA, all bitstreams): **MP3 data end address low**

#### `0x1f6400a8` (FPGA, all bitstreams): **MP3 frame counter** / **Descrambler key 1**

When read:

| Bits | RW | Description                                                     |
| ---: | :- | :-------------------------------------------------------------- |
| 0-15 | R  | Current MP3 frame count (number of MAS3507D `PI4` rising edges) |

When written:

| Bits | RW | Description          |
| ---: | :- | :------------------- |
| 0-15 | W  | Initial `key1` value |

The frame counter is only active when bit 15 in register `0x1f6400ae` is set.
Note that the MAS3507D also has an internal frame counter readable through I2C,
independent of this register.

#### `0x1f6400aa` (FPGA, all bitstreams): **MP3 playback status**

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

#### `0x1f6400ac` (FPGA, all bitstreams): **MAS3507D I2C**

| Bits  | RW | Description                         |
| ----: | :- | :---------------------------------- |
|  0-11 |    | _Unused_                            |
|    12 | RW | MAS3507D `SDA` (write 0 = pull low) |
|    13 | RW | MAS3507D `SCL` (write 0 = pull low) |
| 14-15 | RW | _Unused_                            |

Due to the MAS3507D relying heavily on I2C clock stretching (pulling `SCL` low
to request the host to wait), both `SDA` and `SCL` are bidirectional open-drain
signals.

#### `0x1f6400ae` (FPGA, all bitstreams): **MP3 data feeder control**

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

#### `0x1f6400b0` (FPGA, all bitstreams): **DRAM write address high**

#### `0x1f6400b2` (FPGA, all bitstreams): **DRAM write address low**

#### `0x1f6400b4` (FPGA, all bitstreams): **DRAM data**

| Bits | RW | Description       |
| ---: | :- | :---------------- |
| 0-15 | RW | Current data word |

**NOTE**: on some bitstream versions, all registers in the
`0x1f6400b0-0x1f6400bf` region seem to mirror this register when read (possibly
due to incomplete address decoding), however only a read from `0x1f6400b4` will
increment the current read pointer and kick off prefetching of the next word.

#### `0x1f6400b6` (FPGA, all bitstreams): **DRAM read address high**

#### `0x1f6400b8` (FPGA, all bitstreams): **DRAM read address low**

#### `0x1f6400ba` (FPGA, all bitstreams): **Unknown**

#### `0x1f6400c0` (FPGA, all bitstreams): **Network data**

#### `0x1f6400c2` (FPGA, all bitstreams): **Network TX FIFO length**

#### `0x1f6400c4` (FPGA, all bitstreams): **Network RX FIFO length**

#### `0x1f6400c6` (FPGA, all bitstreams): **Unknown**

Seems to return `0x7654` on startup.

#### `0x1f6400c8` (FPGA, all bitstreams): **Unknown (network related)**

Seems to also return `0x7654` on startup.

#### `0x1f6400ca` (FPGA, all bitstreams except Solo): **DAC sample counter high**

#### `0x1f6400cc` (FPGA, all bitstreams): **DAC sample counter low**

#### `0x1f6400ce` (FPGA, all bitstreams): **DAC sample counter delta**

#### `0x1f6400e0` (FPGA, all bitstreams): **Bank A**

| Bits | RW | Description                          |
| ---: | :- | :----------------------------------- |
| 0-11 |    | _Unused_                             |
|   12 | W  | Output A4 (0 = grounded, 1 = high-z) |
|   13 | W  | Output A5 (0 = grounded, 1 = high-z) |
|   14 | W  | Output A6 (0 = grounded, 1 = high-z) |
|   15 | W  | Output A7 (0 = grounded, 1 = high-z) |

#### `0x1f6400e2` (FPGA, all bitstreams): **Bank A**

| Bits | RW | Description                          |
| ---: | :- | :----------------------------------- |
| 0-11 |    | _Unused_                             |
|   12 | W  | Output A0 (0 = grounded, 1 = high-z) |
|   13 | W  | Output A1 (0 = grounded, 1 = high-z) |
|   14 | W  | Output A2 (0 = grounded, 1 = high-z) |
|   15 | W  | Output A3 (0 = grounded, 1 = high-z) |

#### `0x1f6400e4` (FPGA, all bitstreams): **Bank B**

| Bits | RW | Description                          |
| ---: | :- | :----------------------------------- |
| 0-11 |    | _Unused_                             |
|   12 | W  | Output B4 (0 = grounded, 1 = high-z) |
|   13 | W  | Output B5 (0 = grounded, 1 = high-z) |
|   14 | W  | Output B6 (0 = grounded, 1 = high-z) |
|   15 | W  | Output B7 (0 = grounded, 1 = high-z) |

#### `0x1f6400e6` (FPGA, all bitstreams): **Bank D**

| Bits | RW | Description                          |
| ---: | :- | :----------------------------------- |
| 0-11 |    | _Unused_                             |
|   12 | W  | Output D0 (0 = grounded, 1 = high-z) |
|   13 | W  | Output D1 (0 = grounded, 1 = high-z) |
|   14 | W  | Output D2 (0 = grounded, 1 = high-z) |
|   15 | W  | Output D3 (0 = grounded, 1 = high-z) |

#### `0x1f6400e8` (FPGA, all bitstreams): **Internal logic reset**

| Bits | RW | Description                                                  |
| ---: | :- | :----------------------------------------------------------- |
| 0-11 |    | _Unused_                                                     |
|   12 | W  | Unknown reset (0 = reset)                                    |
|   13 | W  | Reset MP3 feeder and master clock divider to DAC (0 = reset) |
|   14 | W  | Unknown reset (0 = reset)                                    |
|   15 | W  | Unknown reset (0 = reset)                                    |

Konami's code writes `0xf000`, followed by `0x0000`, a delay and `0xf000` again,
to this register after uploading the bitstream.

#### `0x1f6400ea` (FPGA, all bitstreams): **Descrambler key 2**

| Bits | RW | Description          |
| ---: | :- | :------------------- |
| 0-15 | W  | Initial `key2` value |

#### `0x1f6400ec` (FPGA, all bitstreams): **Descrambler key 3**

| Bits | RW | Description          |
| ---: | :- | :------------------- |
|  0-7 | W  | Initial `key3` value |
| 8-15 |    | _Unused_             |

#### `0x1f6400ee` (FPGA, all bitstreams): **1-wire bus**

When read:

| Bits  | RW | Description               |
| ----: | :- | :------------------------ |
|   0-7 |    | _Unused_                  |
|     8 | R  | DS2433 1-wire bus readout |
|  9-11 |    | _Unused_                  |
|    12 | R  | DS2401 1-wire bus readout |
| 13-15 |    | _Unused_                  |

When written:

| Bits  | RW | Description                                            |
| ----: | :- | :----------------------------------------------------- |
|   0-7 |    | _Unused_                                               |
|     8 | W  | Drive DS2433 1-wire bus low (1 = pull low, 0 = high-z) |
|  9-11 |    | _Unused_                                               |
|    12 | W  | Drive DS2401 1-wire bus low (1 = pull low, 0 = high-z) |
| 13-15 |    | _Unused_                                               |

In addition to the DS2401 the board has an unpopulated footprint for a DS2433
1-wire EEPROM, connected to a separate FPGA pin.

#### `0x1f6400f0` (CPLD): **Unknown (unused?)**

Konami's code does not write to this CPLD register.

#### `0x1f6400f2` (CPLD): **Unknown (unused?)**

Konami's code does not write to this CPLD register.

#### `0x1f6400f4` (CPLD): **DAC reset**

| Bits | RW | Description                         |
| ---: | :- | :---------------------------------- |
| 0-14 |    | _Unused_                            |
|   15 | W  | Audio DAC reset/disable (0 = reset) |

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
