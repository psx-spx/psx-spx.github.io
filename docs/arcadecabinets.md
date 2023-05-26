
# Arcade Cabinets

The following arcade PCBs are known to be based on PlayStation hardware:

| Manufacturer | Board                             | CPU clock | GPU       | RAM     | VRAM   | Additional CPUs        | Audio                                | Storage                                               |
| :----------- | :-------------------------------- | --------: | :-------- | ------: | -----: | :--------------------- | :----------------------------------- | :---------------------------------------------------- |
| Konami       | GV                                |    33 MHz | v0        |    2 MB |   1 MB |                        | SPU, CD-DA                           | SCSI CD-ROM, optional flash daughterboard             |
| Konami       | GQ                                |    33 MHz | v1        |    4 MB |   2 MB | 68000, TMS57002        | 2x custom PCM chip                   | SCSI hard drive                                       |
| Konami       | [System 573](konamisystem573.md)  |    33 MHz | v2        |    4 MB |   2 MB | H8/3644                | SPU, CD-DA, optional MP3 decoder     | 16 MB flash, optional ATAPI CD-ROM, PCMCIA cards      |
| Konami       | Twinkle System                    |    33 MHz | v2        |    4 MB |   2 MB | 68000, DVD player      | SPU, Ricoh RF5C400                   | SCSI CD-ROM, IDE hard drive, VCD/DVD, optional floppy |
| Namco        | System 11 (COH-100 CPU board)     |    33 MHz | v1        |    4 MB |   2 MB | Namco C76              | SPU (unpopulated), custom PCM chip   | Mask ROM daughterboard                                |
| Namco        | System 11 (COH-110 CPU board)     |    33 MHz | v2        |    4 MB |   2 MB | Namco C76              | Custom PCM chip                      | Mask ROM daughterboard                                |
| Namco        | System 12 (COH-700 CPU board)     |    50 MHz | v2b       |    4 MB |   2 MB | H8/3002, optional SH-2 | Custom PCM chip, optional XA-ADPCM   | Mask ROM/flash daughterboard, optional ATAPI CD-ROM   |
| Namco        | System 12 (COH-716 CPU board)     |    50 MHz | v2        |   16 MB |   2 MB | H8/3002, optional SH-2 | Custom PCM chip, optional XA-ADPCM   | Mask ROM/flash daughterboard, optional ATAPI CD-ROM   |
| Namco        | System 10                         |    50 MHz | v2        |   16 MB |   2 MB |                        | SPU, optional MP3 decoder            | Mask ROM/flash daughterboard, optional ATAPI CD-ROM   |
| Sony         | ZN-1                              |    33 MHz | v2        |  4-8 MB | 1-2 MB | Optional game-specific | SPU, optional game-specific hardware | Mask ROM/flash daughterboard                          |
| Sony         | ZN-2                              |    50 MHz | v2 or v2b | 4-16 MB |   2 MB | Optional game-specific | SPU, optional game-specific hardware | Mask ROM/flash daughterboard                          |
| Taito        | FX-1A (ZN-1 + custom addon board) |    33 MHz | v2        |    4 MB |   1 MB | Z80                    | SPU, Yamaha YM2610B                  | Mask ROM daughterboard                                |
| Taito        | FX-1B (ZN-1 + custom addon board) |    33 MHz | v2        |    4 MB |   1 MB |                        | SPU, custom Zoom DSP                 | Mask ROM daughterboard                                |
| Taito        | G-NET (ZN-2 + custom addon board) |    50 MHz | v2b       |    4 MB |   2 MB | MN1020012A, TMS57002   | SPU, custom Zoom DSP                 | 8 MB flash, custom encrypted PCMCIA/CF card           |

The following boards were mentioned in the original nocash page, but almost
nothing is known about them:

- Atlus PSX
- PS Arcade 95
- Tecmo TPS

Currently only documentation for the System 573 exists. More information about
other arcade boards could be obtained from MAME source code.

## CPU

Most boards use the same CPUs as retail consoles and development units. The
System 10, System 12 and ZN-2 feature a later CPU revision that allows for up
to 16 MB main RAM (as opposed to 8 MB on the standard CPUs) and clock speeds of
up to 50 MHz. The bus interface and memory control registers on these chips may
behave differently from the ones found on standard CPUs due to the extended
address space.

## GPU

Most systems have a regular v2 GPU but expand VRAM to 2 MB, arranged as a
1024x1024 buffer rather than 1024x512. The Konami GQ and COH-100 (CPU + GPU
daughterboard used in early System 11 units) have the v1 "prototype" GPU, which
uses completely different commands from v0/v2 and is generally not compatible
with any known version of Sony's development tools. Most System 11 games seem to
support both GPU types.

Some System 12 and ZN-2 variants use a later revision of the v2 GPU (v2b). The
differences between v2 and v2b GPUs are currently unknown.

## Audio

Almost all boards extend the SPU's functionality with additional hardware,
usually a custom fixed-function DSP and in some cases a separate sound CPU. The
custom audio hardware is typically on a separate board, with some systems
allowing it to be unplugged if the game does not require it. The Konami GQ,
System 11 (both COH-100 and COH-110 variants) and System 12 omit the SPU
entirely.

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

With the exception of Konami, all manufacturers used mask ROMs or flash memory
for game storage. The wiring and layout of the ROMs varies for each board; on
some systems the BIOS and game are part of the same ROM, while others have
separate BIOS and game ROMs. Graphical and audio assets may also be stored
separately or within the main game ROM.

Konami systems store game executables and assets on standard SCSI/IDE hard
drives or CD-ROMs. The System 573 can also boot from its built-in flash or a
PCMCIA flash card, using the CD-ROM drive only to install new games, however
the vast majority of 573 games are too large to fit entirely in the flash and
still rely on reading files from the disc after installation. The Twinkle
System is particularly unusual as it has a CD-ROM drive accessed by the main
CPU, a separate hard drive used by the audio board and an external DVD player
unit for background videos.

The System 10 and System 12 are the only known non-Konami boards with CD-ROM
support. The former can be connected directly to an ATAPI drive, while the
latter requires an expansion module that provides an IDE interface and XA-ADPCM
decoding through an integrated SH-2 CPU. Whether these boards support CD-ROM
booting without any game ROMs installed is currently unknown.

## Security

The implementation of anti-piracy measures varies for each manufacturer.

- Namco boards have their ROMs encrypted, with a CPLD ("KEYCUS" chip) wired
  between the CPU and ROM performing on-the-fly decryption. Some KEYCUS chips
  require the CPU to issue commands in order to unlock different sections of the
  ROM.
- Sony's ZN-1 and ZN-2 are fitted by each manufacturer with a custom BIOS ROM
  and security microcontroller, which are then verified by the games. This makes
  it harder to convert a ZN-1 or ZN-2 game to a different one by simply swapping
  out the game-specific daughterboard.
- CD-ROMs for Konami boards were typically shipped alongside a security dongle
  or cartridge that must be plugged in to boot the game. Some games write the
  system's serial number to the dongle during installation, preventing
  installation of the same game on more than one cabinet. The System 573's
  optional MP3 decoder board additionally features an FPGA used to decrypt MP3
  files on the disc during playback.
- Taito G-NET games are stored on a custom manufactured PCMCIA card which is not
  readable by any normal means. The contents of the card are presumably
  encrypted as well.
