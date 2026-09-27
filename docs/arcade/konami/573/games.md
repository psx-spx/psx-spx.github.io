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
  `GE765-PWB(B)A` fishing controller I/O board included on systems that
  that came with Fisherman's Bait.

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

### DDR Solo I/O connectors

Solo cabinets use a different front panel from the standard 2-player ones: there
is an extra connector on the left side, and the connectors on the right differ.
The wiring, as given by the DDR Solo Bass Mix service manual, is:

| Location     | Connector | Wired to                                          |
| :----------- | :-------- | :------------------------------------------------ |
| Top left     | `XMR-10V` | Lamp outputs `B0-B3` on the digital I/O board, driving the relays for the AC outlets that power external lamps. |
| Middle left  | `XMR-12V` | Lamp outputs `B4-B7` and `C4-C7`, driving the cabinet's own lights. |
| Bottom left  | `XMR-07V` | `EXT-IN` (non-JAMMA button inputs) on the motherboard, going to a harness marked reserved with nothing connected to it. |
| Top right    | `YLR-08V` | RS-232 port on the digital I/O board. |
| Bottom right | `YLR-06V` | Lamp outputs `C0-C3`, driving the speaker neons. |

The RS-232 port is not known to have been used by any game, but its presence on
the panel implies Solo's FPGA bitstream implements a UART for it. Later games'
bitstreams do not, presumably because Konami ran out of room in the FPGA.

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

- [Hard-to-install games](#hard-to-install-games)
- [Homebrew guidelines](#homebrew-guidelines)
- [Missing support for PAL mode](#missing-support-for-pal-mode)
- [Flash chips and PCMCIA cards](#flash-chips-and-pcmcia-cards)
- [Known working replacement PCMCIA cards](#known-working-replacement-pcmcia-cards)
- [Known working replacement drives](drives.md#known-working-replacement-drives)
- [Bemani launcher error and status codes](#bemani-launcher-error-and-status-codes)

### Hard-to-install games

While the vast majority of 573 games can be trivially installed by inserting the
respective game disc (or sometimes a separate install disc) and a new security
cartridge, there are a few ones that require more complex installation
procedures:

- **Games without a CD-ROM**: for what should be obvious reasons, such games
  cannot be installed without either using homebrew flashing tools or injecting
  a flash image into another game's CD-ROM installer. Konami's "official"
  installation method was to boot the flash image from a PCMCIA card, which the
  game will detect and copy over to the internal flash.
- **Hyper Bishi Bashi Champ**, **Handle/Steering Champ**: RTC RAM is employed as
  a "suicide battery" of sorts by pre-populating it with a header and other data
  at the factory. If any of the data is corrupted or missing, the game will
  display "HARDWARE UNMATCHED" and refuse to boot any further.
- **Dance Dance Revolution (`JAB` version)**: also checks RTC RAM and will not
  boot if its header is missing from the first 32 bytes (subsequent data can be
  uninitialized and will be rebuilt automatically if needed). Additionally, even
  though the game requires a CD-ROM, its disc only contains CD-DA tracks and
  lacks an installer or flash image, requiring the same workarounds as
  CD-ROM-less games in order to install it.
- **Dance Dance Revolution 4thMIX PLUS** and **PLUS Solo**: as this game is an
  upgrade to DDR 4thMIX, the installer will refuse to proceed unless 4thMIX's
  header is present in the first 32 bytes of RTC RAM. This check is only
  performed during installation; the game itself will rebuild the entire
  contents of the RTC if the header is invalid.
- **Dancing Stage feat. Dreams Come True** (both analog I/O and digital I/O
  versions): notorious for requiring a lot of juggling with security cartridges.
  The installer prompts for a cartridge from a previous game that is allowed to
  be upgraded, which will be invalidated and made unusable as part of the
  installation process.

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
| ~~Centennial~~ | ~~PM24265, FL32M-20-\*-67~~          | 16x 28F016S5   |    32 MB |    8-bit | `0x8989`  | `0xaaaa`  | Yes\*   | See note below on model numbers                                           |
| ~~Centennial~~ | ~~PM24265, FL32M-20-\*-67~~          | 16x AM29F016   |    32 MB |    8-bit | `0x0101`  | `0xadad`  | No      | Same command set as Fujitsu cards, may work with ID check patching        |
| ~~Centennial~~ | ~~PM24276, FL32M-20-\*-J5-03~~       | 4x 28F640J5    |    32 MB |   16-bit | `0x0089`  | `0x0015`  | No      |                                                                           |
| ~~Centennial~~ | ~~PM24282, FL32M-20-\*-S5-03~~       | 16x AM29F016   |    32 MB |    8-bit | `0x0101`  | `0xadad`  | No      | Same command set as Fujitsu cards, may work with ID check patching        |
| Fujitsu        | "32MB Flash Card" (no model number?) | 16x MBM29F016A |    32 MB |    8-bit | `0x0404`  | `0xadad`  | **Yes** | Stock card (Konami sticker covers Fujitsu logo)                           |
| Fujitsu        | "32MB Flash Card" (no model number?) | 16x MBM29F017A |    32 MB |    8-bit | `0x0404`  | `0x3d3d`  | **Yes** | Stock card (Konami sticker covers Fujitsu logo)                           |
| Sharp          | ID245G01                             | 4x LH28F016S   |     8 MB |    8-bit | `0x8989`  | `0xaaaa`  | **Yes** | Stock card (Konami sticker covers Sharp logo), used by GunMania Zone Plus |
| Sharp          | ID245P01                             | 16x LH28F016S  |    32 MB |    8-bit | `0x8989`  | `0xaaaa`  | **Yes** | Stock card (Konami sticker covers Sharp logo)                             |

Note that most of these cards have identical labels and can typically only be
told apart from the model number printed on the bottom side or one of the edges.

**IMPORTANT**: the model numbers on Centennial cards seem to be inconsistent and
not necessarily related to which flash chips the card is fitted with. As such
**buying these cards for use with 573 games is strongly discouraged**, even
though some of them are known to use parts compatible with Konami's driver.

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
