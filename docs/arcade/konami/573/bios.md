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
  on its own, without ever returning to the kernel.
- The kernel initializes the DEV0 region and clears the watchdog periodically
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
- The shell is launched through a stub that contains a
  `Lisenced by Sony Computer Entertainment Inc.(SCEI)` \[sic\] string, validated
  by the kernel in a similar (but not identical) way to PS1 expansion port ROMs.

### Boot sequence

All variants of the shell are far simpler than their PS1 counterparts, as they
lack any kind of UI (aside from a non-interactive status screen) and have *no*
*copy protection or anti-piracy checks* of any kind. Once loaded by the kernel,
they start by initializing the system bus and proceed to run a hardware
self-test. The outcome of all checks is displayed on screen, with the following
ones being performed:

- `22G`: BIOS ROM integrity check. A checksum is computed and verified against
  the one present in the ROM at `0xbfc7fffc-0xbfc7ffff`;
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
        }

        if (offset)
            offset <<= 1;
        else
            offset = 1;
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

    // BUG: the actual size of the executable including the header is
    // (2048 + *EXE_TEXT_SIZE_PTR), however neither the 700A01 nor 700B01 shells
    // take this into account and instead end up ignoring the executable's last
    // 2048 bytes.
    uint32_t crc = exe_crc32(EXE_HEADER_PTR, *EXE_TEXT_SIZE_PTR);

    return (crc == *EXE_CRC32_PTR);
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

## Bootleg mod boards

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

### `DDRTURBO` mod board

Board required by and specific to the DDR Extreme PLUS hack. Unlike all other
currently known boards, this one actually adds new functionality to the system:
the ability to speed up MP3 playback... *by taking the place of the 29.45 MHz*
*main oscillator* on the digital I/O board, which is desoldered and replaced
with a bodge wire. It features three crystal oscillators supplying the following
clocks:

- **29.5 MHz** (0.16% faster than stock, referred to as "Normal Speed" in
  Extreme PLUS)
- **33 MHz** (12.05% faster than stock, referred to as "Speed up 10%" in Extreme
  PLUS)
- **36 MHz** (22.24% faster than stock, referred to as "Speed up 20%" in Extreme
  PLUS)

The board listens for reads from the upper half of BIOS ROM
(`0xbfc40000-0xbfc7ffff`) and latches bits 5-6 of the byte read to determine
which clock to output to the digital I/O board:

| Byte read    | Clock           |
| -----------: | --------------: |
| `0b*00*****` |          33 MHz |
| `0b*01*****` |          36 MHz |
| `0b*10*****` |        29.5 MHz |
| `0b*11*****` | Unknown (none?) |

**NOTE**: kernel code execution while the game is running will *not* affect the
clock as the kernel is contained entirely within the ROM's first half. The
second half is in fact only accessed on startup when relocating the shell
executable to RAM and computing the ROM checksum.

In order to switch clocks, Extreme PLUS always reads from one of the following
addresses:

| Address read | Byte read | Clock    |
| -----------: | --------: | -------: |
| `0xbfc40ebf` |    `0x55` | 29.5 MHz |
| `0xbfc40810` |    `0x00` |   33 MHz |
| `0xbfc41341` |    `0xaa` |   36 MHz |

The board's EPROM holds a copy of the 700A01 BIOS with the last byte of the
checksum at `0xbfc7ffff` modified from `0xf9` to `0x39`. Extreme PLUS uses this
change to detect the mod board and will refuse to run if it is not present. The
padding byte at `0xbfc7fffb` is also changed from `0xff` to `0x3f` in order for
the contents of the ROM to match the new checksum.
