
# Arcade Cabinets

The following arcade PCBs are known to be based on PlayStation hardware:

| Manufacturer | Board                            | CPU clock | GPU       | RAM     | VRAM   | Additional CPUs                            | Audio                                                         | Storage                                                    |
| :----------- | :------------------------------- | --------: | :-------- | ------: | -----: | :----------------------------------------- | :------------------------------------------------------------ | :--------------------------------------------------------- |
| Konami       | GV                               |    33 MHz | v0        |    2 MB |   1 MB |                                            | SPU, CD-DA                                                    | SCSI CD-ROM, optional flash module (`PWB402610`)           |
| Konami       | GQ                               |    33 MHz | v1        |    4 MB |   2 MB | 68000, TMS57002                            | 2x Konami 054539 PCM (no SPU)                                 | SCSI hard drive                                            |
| Konami       | [System 573](konamisystem573.md) |    33 MHz | v2        |    4 MB |   2 MB | H8/3644                                    | SPU, CD-DA, optional Micronas MAS3507D MP3 (`GX894-PWB(B)A`)  | Internal flash, optional ATAPI CD-ROM, PCMCIA flash cards  |
| Konami       | Twinkle System                   |    33 MHz | v2        |    4 MB |   2 MB | Optional 68000 (`TWINKLE/SPU`), DVD player | SPU, optional Ricoh RF5C400 PCM (`TWINKLE/SPU`)               | SCSI CD-ROM, IDE hard drive (`TWINKLE/SPU`), unused floppy |
| Namco        | System 10                        |    50 MHz | v2        |   16 MB |   2 MB |                                            | SPU, optional Sanyo LC82310 MP3 (`MEM(P3) PCB`)               | Game-specific mask ROM/flash module, optional ATAPI CD-ROM |
| Sony         | COH-100                          |    33 MHz | v1        |    4 MB |   2 MB | Provided by manufacturer PCB (see below)   | Provided by manufacturer PCB (see below, has unpopulated SPU) | Provided by manufacturer PCB (see below)                   |
| Sony         | COH-110                          |    33 MHz | v2        |    4 MB |   2 MB | Provided by manufacturer PCB (see below)   | Provided by manufacturer PCB (see below, no SPU)              | Provided by manufacturer PCB (see below)                   |
| Sony         | COH-700                          |    50 MHz | v2b       |    4 MB |   2 MB | Provided by manufacturer PCB (see below)   | Provided by manufacturer PCB (see below, no SPU)              | Provided by manufacturer PCB (see below)                   |
| Sony         | COH-716                          |    50 MHz | v2        |   16 MB |   2 MB | Provided by manufacturer PCB (see below)   | Provided by manufacturer PCB (see below, no SPU)              | Provided by manufacturer PCB (see below)                   |
| Sony         | ZN-1                             |    33 MHz | v2        |  4-8 MB | 1-2 MB | Provided by manufacturer PCB (see below)   | SPU, extra hardware provided by manufacturer PCB (see below)  | Provided by manufacturer PCB (see below)                   |
| Sony         | ZN-2                             |    50 MHz | v2 or v2b | 4-16 MB |   2 MB | Provided by manufacturer PCB (see below)   | SPU, extra hardware provided by manufacturer PCB (see below)  | Provided by manufacturer PCB (see below)                   |

The following systems are based on a Sony CPU daughterboard mounted on top of a
custom manufacturer-specific main board:

| Manufacturer | Main board | CPU board          | Additional CPUs                     | Audio                                                 | Storage                                                    |
| :----------- | :--------- | :----------------- | :---------------------------------- | :---------------------------------------------------- | :--------------------------------------------------------- |
| Namco        | System 11  | COH-100 or COH-110 | Namco C76 (custom H8)               | Namco C352 PCM                                        | Game-specific mask ROM module                              |
| Namco        | System 12  | COH-700 or COH-716 | H8/3002, optional SH-2 (`CDXA PCB`) | Namco C352 PCM, XA-ADPCM decoded by SH-2 (`CDXA PCB`) | Game-specific mask ROM/flash module, optional ATAPI CD-ROM |

The following systems are based on a Sony ZN-1 or ZN-2 motherboard with a
manufacturer-specific daughterboard mounted on top:

| Manufacturer            | Main board   | Daughterboard                   | Additional CPUs                   | Audio                             | Storage                                          |
| :---------------------- | :----------- | :------------------------------ | :-------------------------------- | :-------------------------------- | :----------------------------------------------- |
| Acclaim                 | ZN-1         | `PCB-100102`                    | Optional ADSP-2181 (`PCB-100095`) | PCM from ADSP-2181 (`PCB-100095`) | Mask ROMs, EPROMs                                |
| Atari                   | ZN-1         | Primal Rage 2 (`PSXTRA`)        |                                   |                                   | EPROMs, IDE hard drive                           |
| Atlus                   | ZN-1         | Heaven's Gate (`ATHG-01`)       | 68000                             | Yamaha YMZ280B PCM/ADPCM          | Mask ROMs, EPROMs                                |
| Capcom                  | ZN-1 or ZN-2 | `95681-2`                       | Z80                               | Capcom Q-Sound PCM/ADPCM          | Mask ROMs, EPROMs                                |
| Capcom                  | ZN-2         | `97695-1`                       | Z80                               | Capcom Q-Sound PCM/ADPCM          | Mask ROMs, EPROMs                                |
| Eighting/Raizing        | ZN-1         | `RA9701 SUB`                    | 68000                             | Yamaha YMF271-F FM/PCM            | Mask ROMs, EPROMs                                |
| Eighting/Raizing, Tecmo | ZN-1         | `PS9805`                        | 68000                             | Yamaha YMF271-F FM/PCM            | Mask ROMs, EPROMs, flash                         |
| Eighting/Raizing        | ZN-1         | Bust-A-Move 2 (`MTR990601-(A)`) | H8/3644                           | PCM streamed by H8/3644           | Mask ROMs, flash, IDE hard drive or ATAPI CD-ROM |
| Taito                   | ZN-1         | FX-1 (`SROM PCB-A`)             | Z80                               | Yamaha YM2610 FM/ADPCM            | Mask ROMs, EPROMs                                |
| Taito                   | ZN-1         | FX-1 (`ZROM PCB`)               | MN1020012A, TMS57002              | Zoom ZSG-2 PCM                    | Mask ROMs, EPROMs                                |
| Taito                   | ZN-1 or ZN-2 | G-NET (`FC PCB`)                | MN1020012A, TMS57002              | Optional Zoom ZSG-2 PCM           | Secure PCMCIA or CF-like flash card              |
| Tecmo                   | ZN-1         | TPS System (`TPS1-7`)           | Optional Z80                      | Optional Yamaha YMZ280B PCM/ADPCM | Mask ROMs, EPROMs                                |
| Video System            | ZN-1         | `VS34`                          |                                   |                                   | Mask ROMs                                        |

Currently only documentation for the System 573 exists. More information about
other arcade boards could be obtained from MAME source code.

## CPU

Most boards use the same CPUs as retail consoles and development units but
extend main RAM to up to 16 MB, with 4 MB being the most common configuration.
The System 10, COH-716 and ZN-2 run the CPU at 50 MHz instead of 33 and feature
a different chip revision from any known stock console, presumably rated for the
higher clock speed but otherwise functionally identical.

## GPU

Most systems have a regular 208-pin v2 GPU but expand VRAM from 1 to 2 MB,
arranged as a 1024x1024 buffer rather than 1024x512. The Konami GQ and COH-100
instead use the v1 "prototype" GPU, which employs a different command format. As
the System 11 could come fitted with either a COH-100 or COH-110, some System 11
games support both formats.

As with CPUs, some ZN-2 variants and the COH-700 use a later arcade-only
revision ("v2b") of the v2 GPU. This change may also be related to the clock
speed increase, however not all systems running at 50 MHz seem to use the newer
GPU.

## Audio

Almost all boards extend the SPU's functionality with additional hardware,
usually consisting of a custom PCM mixer and in some cases a separate CPU
driving it. The extra circuitry is typically in charge of playing music
(fulfilling the same role as CD-DA and XA-ADPCM on retail consoles), with the
SPU still handling playback of all other audio.

The Konami GQ and all systems based on Sony's CPU daughterboards omit the SPU
altogether and rely entirely on custom sound hardware. The Twinkle System has
the SPU populated but all games that require its dedicated audio board will
leave it unused.

## Controls

Most systems are designed to be connected to a cabinet through a JAMMA board
edge connector, which carries power, a video output, player controls and
coin/service button inputs. These inputs are typically accessed via custom
memory-mapped I/O ports. As control schemes may vary greatly from game to game,
many systems also provide means to connect additional inputs or expansion
boards.

Some boards feature a JVS port (a standardized serial bus protocol used to
connect controls and peripherals to modern arcade systems), allowing standard
JVS I/O boards to be used if supported by games.

## Storage

With the exception of Konami, all manufacturers adopted solid state game storage
(mask ROMs, EPROMs and/or flash memory). The wiring and layout of the ROMs
varies across boards; on some systems the BIOS, game binary and its assets are
part of the same ROM region, while others split them into separate areas. Boards
with custom sound hardware usually store samples and other audio data in
dedicated ROMs accessed directly by the hardware in question.

Konami systems store game executables and assets on standard SCSI/IDE hard
drives or CD-ROMs. The System 573 can also boot from its built-in flash or a
PCMCIA flash card, using the CD-ROM drive only to install new games, however
the vast majority of 573 games are too large to fit entirely in the flash and
still rely on reading files from the disc after installation. The Twinkle
System is particularly unusual as it has a CD-ROM drive accessed by the main
CPU, a separate hard drive used by the audio board and an external DVD player
unit for background videos.

The System 12, System 10 and the ZN-1 with the Bust-A-Move 2 ROM board are the
only currently known non-Konami PCBs with CD-ROM support. The former requires an
expansion module that provides an IDE interface and XA-ADPCM decoding through an
integrated SH-2 CPU, while the latter two can be connected directly to a drive.
In all cases the CD-ROM is only used for audio streaming and the boards are not
otherwise capable of booting directly from it without a ROM board installed.

## Security

The implementation of anti-piracy measures varies for each manufacturer.

- Namco's System 11 and 12 employ a CPLD or ASIC ("KEYCUS" chip) on each ROM
  module as a game-specific security coprocessor the CPU communicates with. In
  the case of the System 12, the KEYCUS chip seems to double as a lockout device
  and restrict access to the ROMs until the game issues an unlocking sequence.
- Namco System 10 games also use a KEYCUS CPLD but wire it between the CPU and
  ROMs, allowing it to perform on-the-fly unscrambling of their encrypted
  contents in addition to the lockout functionality.
- Similarly, most Taito G-NET games are stored on non-standard PCMCIA flash
  cards that require unlock sequences specific to each game prior to being
  accessed.
- Sony's ZN-1 and ZN-2 are fitted by each manufacturer with a custom BIOS ROM
  and security/decryption ASIC, which the game-specific ROM daughterboard then
  relies on. This makes it harder to convert ZN-1 or ZN-2 games by simply
  swapping out the daughterboard.
- CD-ROMs for Konami boards were typically shipped alongside a security dongle
  or cartridge that must be plugged in to boot the game. Some games write the
  system's serial number to the dongle during installation, preventing
  installation of the same game on more than one cabinet. The System 573's
  optional MP3 decoder board additionally features an FPGA used to decrypt MP3
  files on the disc during playback.

## Games

Some of the most notable arcade titles to use the boards listed here include:

- **Beatmania IIDX** up to 8th Style (Twinkle System)
- **Dance Dance Revolution** up to EXTREME (System 573)
- **DrumMania** up to 10thMIX (System 573)
- **GuitarFreaks** up to 11thMIX (System 573)
- **Point Blank 2** (System 11 or System 12)
- **Point Blank 3** (System 10)
- **Soul Calibur** (System 12)
- **Soul Edge** (System 11)
- **Street Fighter EX** (Capcom ZN-1)
- **Street Fighter EX2** (Capcom ZN-2)
- **Taiko no Tatsujin** up to 6 (System 10)
- **Tekken** and **Tekken 2** (System 11)
- **Tekken 3** (System 12)
- **Tetris: The Grand Master** (Capcom ZN-2)
