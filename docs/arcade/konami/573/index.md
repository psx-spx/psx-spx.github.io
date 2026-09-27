
# Konami System 573

The System 573 is a PlayStation-based system used in a number of Konami arcade
games from the late 90s and early 2000s, most notably Dance Dance Revolution and
other titles from the Bemani series of rhythm games.

- [Differences vs. PS1](#differences-vs-ps1)
- [Register map](registers.md#register-map)
- [JVS interface](builtin-io.md#jvs-interface)
- [I/O boards](expansion-io.md#io-boards)
- [Security cartridges](security-cartridges.md#security-cartridges)
- [External modules](external-modules.md#external-modules)
- [BIOS](bios.md#bios)
- [Bootleg mod boards](bios.md#bootleg-mod-boards)
- [Game-specific information](games.md#game-specific-information)
- [Notes](games.md#notes)
- [Pinouts](pinouts.md#pinouts)
- [Credits, sources and links](#credits-sources-and-links)

This document is currently work-in-progress. Here is an incomplete list of
things the authors believe need more research:

- The BIOS and games are notoriously picky about ATAPI drives due to Konami's
  libraries not always respecting timings and polling registers in the way
  suggested by the specifications. Such issues shall be documented more in
  detail.
- The `GE765-PWB(B)A` and `PWB0000073070` I/O boards have been fully and
  partially reverse engineered respectively, but documentation for them is
  missing.
- The `GN845-PWB(B)` DDR stage PCB's communication protocol is largely unknown.
  More tests need to be done on real hardware and its CPLD shall be dumped if
  possible.
- The protocol used by the 573 to communicate with the `PWB0000100991` network
  PCB has been reversed, however very little about the PCB's own hardware and
  software stack is otherwise known.
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
