#   PSX Dev-Board Protocol
This page documents the DECI communication protocol and host-side interface used by the DTL-H2000, DTL-H2500, and DTL-H2700 PlayStation development boards. For board chipsets and physical component lists, see [PSX Dev-Board Chipsets](psxdevboardchipsets.md).

The DTL-H2000 is an ISA-bus development board. The DTL-H2500 is a PCI-bus variant with automatic configuration. The DTL-H2700 is an ISA-bus board identical to the H2000 but with an additional Performance Analyzer (bus logic analyzer) on two daughterboards.

All three boards use the same DECI (DEbugging Communication Interface) protocol for debugging, program upload, and PCDRV host file system access. The protocol is transport-agnostic - the DECI command format, opcodes, and PCDRV file operations are identical regardless of whether the underlying transport is ISA or PCI. The H2700 adds extra hardware for the Performance Analyzer.

#### ISA I/O Port Map (DTL-H2000, DTL-H2700)
The ISA-bus boards use a set of I/O ports at a configurable base address. The base is set via DIP switches on the board. Factory default is 0x1340 for the H2700 (the H2000 commonly uses 0x0320). The DIP switches set the upper 12 bits of the address.
```
  Port base+0   Status Register (16-bit read)
  Port base+1   Command/Result Byte (8-bit read/write)
  Port base+2   Data Port (16-bit read/write, bulk transfers)
  Port base+4   Control Register A (8-bit write)
  Port base+5   Mode Register (8-bit read/write)
  Port base+6   Reset Control (8-bit write)
  Port base+7   Reserved
  Port base+C   Performance Analyzer Status/Control (16-bit, H2700 only)
  Port base+E   Performance Analyzer Data (16-bit, H2700 only)
```

#### Status Register (base+0, read)
```
  Bit 0     Word ready (single word available in data port)
  Bit 1     Bulk read ready (large transfer available)
  Bit 2     Write ready (data port can accept writes)
  Bit 3     Command accept ready (port1 can accept a command byte)
  Bit 4     Command complete (result available in port1)
  Bits 5-15 Unknown/unused
```

#### Control Register A (base+4, write)
```
  0x01      Initialize / acknowledge
  0x10      Trigger pending command
  0x20      Acknowledge result
  0x71      Reset sequence
```

#### Mode Register (base+5, read/write)
```
  Bit 4     Pending command flag (set to signal command ready)
  Other     Write 0x01 during reset sequence
```

#### Reset Control (base+6, write)
```
  0x01      Assert reset (used during initialization and resetPS)
  Other     Target-specific reset modes (e.g. op22 writes AL directly)
```

#### IRQ Configuration
Valid IRQs: 10, 11, 12, 15. Configurable via jumper on the board, `/I` command line flag, or `IRQ` setting in `PSYQ.INI`. Standard 8259 PIC handling. IRQ is optional - the protocol works in pure polling mode.

#### DECI Protocol Overview
Communication between the host PC and the PlayStation target uses the DECI (DEbugging Communication Interface) protocol. All commands follow a master-slave model where the host initiates and the target responds.

#### Connection Sequence
```
  1. Write 0x04 to port base+1 (command byte)
  2. Set bit 4 of port base+5 (pending command flag)
  3. Write 0x01 to port base+4 (trigger command)
  4. Poll port base+0 bit 4 until set (command complete)
  5. Read port base+1 (result byte)
  6. If result == 2, target is connected
```

#### Reset Sequence
```
  1. Disable IRQ (if configured)
  2. Write 0x01 to port base+6
  3. Write 0x71 to port base+4
  4. Write 0x01 to port base+5
```

#### DECI Command Buffer Format
Each command sends a 6-byte or 10-byte buffer through the data port (base+2), written as 16-bit words:
```
  Byte 0    DECI command code
  Byte 1    Unit/target ID (variable for PS1 target ops, 0x80 for host-side ops)
  Byte 2-3  Parameter (big-endian, typically length)
  Byte 4-5  Parameter (big-endian)
  Byte 6-9  Address parameter (10-byte commands only, big-endian)
```

#### Command Send/Receive Flow
After writing the command buffer to the data port, the host polls the status register and reads the result byte from port base+1 to determine what the target needs:
```
  Result 0  Target requests data: write payload words to data port (poll bit 2)
  Result 1  Target has data: read payload words from data port (poll bit 1/0)
  Result 2  Command complete
  Result 3  Extended status: read status byte from data port
              0xFF = send PSY-Q copyright string
  Result 5  Target disconnected
  Result 7  Flow control: read byte from data port
              0x7E = override timeout
              0x00 = command acknowledged
```
Bulk data transfers are done word-at-a-time through the data port, with up to 0x800 words (4KB) per burst when status bit 1 is set.

#### DECI Command Table
These are the BIOS-level opcodes and their corresponding DECI command codes. The BIOS opcodes are what programs like RUN.exe and DEXBIOS.COM use, while the DECI command codes are the bytes that appear in the command buffer on the wire.
```
  BIOS Op  DECI Cmd  Description
  00       -         Disconnect (direct port I/O, no DECI buffer)
  01       -         Select SCSI ID (local only)
  02       -         Get active SCSI ID
  07       -         Get PSY-Q report string (error code to text)
  11       0x00      Get target info (reads 24 bytes)
  12       0x02      Kill interrupts on target
  14       0x04      Read 4-byte value from target
  15       0x05      Send/receive data (bidirectional, lengths in CX/DX)
  19       0x21      Read target memory (address in DX:BX, length in CX)
  1a       0x20      Write target memory (address in DX:BX, length in CX)
  1b       0x0C      Target command, no data
  1c       0x0D      Target command, no data
  22       -         Reset PlayStation (direct port I/O to base+6)
  30       0x22      Read memory, alternate format (flag=0x80)
  39       0xC6      mkdir (host-side, unit=0x80)
  3a       0xC7      rmdir (host-side, unit=0x80)
  3b       0xC8      chdir (host-side, unit=0x80)
  3c       0xC9      creat - create file (returns 2-byte handle)
  3d       0xCA      open - open file (returns 2-byte handle)
  3e       0xCB      close - close file (handle in buf[2:3])
  3f       0xCC      read - read file (handle in buf[2:3], length in buf[4:5])
  40       0xCD      write - write file (handle in buf[2:3], length in buf[4:5])
  41       0xD0      unlink - delete file
  43       0xD1/D2   get/set file attributes (D1=get, D2=set)
  47       0xD3      getcwd - get current directory (returns 256-byte path)
  4e       0xD4      findfirst - find first file (returns 128-byte DTA)
  4f       0xD5      findnext - find next file (sends/receives 128-byte DTA)
  56       0xD6      Send two null-terminated strings (rename)
  57       0xD7/D8   Read/write 4 bytes (D7=read, D8=write)
```

#### PCDRV (Host File System Access)
DECI commands 0xC6-0xD8 (BIOS opcodes 0x39-0x57) implement PCDRV - a file system proxy that lets PlayStation programs access files on the host PC. The host-side handler (DEXBIOS.COM on DOS, or a Linux equivalent) translates these into native file operations.

Files are served relative to the working directory where the host-side handler was started. There is no explicit root path configuration - the DOS current directory is the PCDRV root.

The host maintains a handle table of up to 64 entries, mapping PlayStation-side file handles to host file handles. Read and write operations are chunked through a configurable buffer size.

On the PlayStation side, PCDRV requires the DECI debug stub to be installed (see SNPATCH below). The libsn library provides thin wrappers that issue MIPS BREAK instructions, which the debug stub intercepts and translates into DECI commands sent to the host through the development hardware.

#### SNPATCH - Debug Stub Installation
Before PCDRV or debugging can work, the PlayStation must have a DECI-aware debug stub installed. This is done by uploading and executing SNPATCH.CPE, which is included in the PSY-Q SDK.

SNPATCH.CPE is a CPE-format executable (not a PS-EXE) that installs a patched kernel and debug stub into the development board's SRAM at address 0x1FA00000. This SRAM is mapped into the PlayStation's address space by the development hardware.
```
  Boot sequence:
  1. Reset PlayStation (RESETPS 1)
  2. Upload and execute SNPATCH.CPE (RUN /w4 SNPATCH)
  3. Wait 500ms for kernel stabilization (DELAY)
  4. Upload and execute target program (RUN /w4 MYPROG)
```
SNPATCH copies approximately 240KB of code into three regions:
```
  0x1FA00000  7,540 bytes   Exception vectors, kernel entry points
  0x1FA08000  134,004 bytes Shell replacement, debugger core
  0x1FA66000  104,676 bytes Additional debug/PCDRV handler code
```
After copying, it flushes the instruction cache and transfers control to the patched entry points.

SNPATCH replaces both PATCHX.CPE (which had cache coherency bugs) and NEWDEX (which installed the debug stub separately). Three variants exist: SNPATCH.CPE (standard), SNPATCHJ.CPE (Japanese fonts), SNPATCHW.CPE (Western fonts including Latin diacritics, Greek, Cyrillic).

#### Performance Analyzer (DTL-H2700 only)
The DTL-H2700 includes a bus logic analyzer on two daughterboards, accessible through two additional I/O ports at base+0xC and base+0xE. The analyzer can capture main RAM bus, sub bus, and video RAM bus activity.

#### PA Port Map
```
  Port base+C  Status/Control Register (16-bit read/write)
  Port base+E  Data Register (16-bit read/write, also bulk read)
```

#### PA Control Register
The control register uses a bank-switching scheme to access multiple internal registers through the single data port:
```
  Bits 3:0   Command/mode
               0x01 = Start capture
               0x02 = Cancel capture
  Bits 7:4   Bank select (0x0-0xC)
  Bit 15     Hardware presence test bit
```

#### PA Register Banks
```
  Bank 0     Status (read): bits 1:0 = capture state
  Banks 1-10 Trigger/capture configuration (written during capture setup)
  Bank 0xB   Trace read address, low 16 bits (write)
  Bank 0xC   Trace read address, high 10 bits (write)
  Bank 1     Capture pointer low 16 bits (read)
  Bank 2     End pointer low 16 bits (read)
  Bank 3     Pointer high bits: bits 5:0 = capture ptr high, bits 13:8 = end ptr high
```

#### PA Hardware Detection
```
  1. Write 0x8000 to control (set bit 15)
  2. Read status: bits 15:12 must be 0x1, bits 11:8 must be 0x0, bit 7 must be set
  3. Write 0x0000 to control (clear bit 15)
  4. Read status: bit 7 must be clear
  If both checks pass, PA hardware is present.
```

#### PA Capture Flow
```
  1. Verify hardware (detection sequence above)
  2. Write trigger configuration to banks 1-10
  3. Write 0x01 to control register (start capture)
  4. Poll bank 0 status, bits 1:0 for completion
  5. Read capture/end pointers from banks 1-3
  6. Read trace data:
     a. Set address: write low 16 bits to bank 0xB, high 10 bits to bank 0xC
     b. Bulk read from data port (base+0xE) in chunks
  Maximum capture: 4M frames, 16 bytes per frame (64MB trace buffer)
  Address space: 26-bit frame address, shifted left 4 for byte address
```

#### PA Capture Frame Format
Each captured frame is 16 bytes (128 bits), representing a single clock cycle snapshot of the PlayStation's bus state. The hardware passively captures raw electrical signal levels - all bus type classification (idle, refresh, DMA, etc.) is performed in software by LIBPA.DLL through state machines that track RAS/CAS sequences, chip selects, and write enables across consecutive frames.

The bit assignments below were reverse-engineered from LIBPA.DLL and PA32.EXE (PSY-Q SDK 4.4). Waveform signal assignments were confirmed empirically using crafted PAD files loaded in PA32.EXE. Bits not listed are not accessed by the software and may be unused capture lines, reserved, or internal PA hardware state.
```
  Word 0 (bytes 0-3) - SDRAM Bus and Control Signals
  ---------------------------------------------------
  Bytes 0-1 (16-bit LE):
    SDRAM multiplexed address lines (active during RAS and CAS phases).
    The software reconstructs full SDRAM addresses by capturing the row
    address during RAS then the column address during CAS. The exact
    mapping from raw bits to logical address bits involves non-trivial
    rearrangement in the DLL and has not been fully decoded.

  Byte 1:
    Bit 4 (0x10)   Main bus access strobe (active during bus transactions)
    Bit 7 (0x80)   SBus direction (1=read, 0=write)
    Bits 0-3,5,6   Part of SDRAM muxed address (exact mapping not decoded)

  Byte 2:
    Bit 0 (0x01)   SBus device select
    Bit 1 (0x02)   SIO1 RXD (receive data)
    Bit 2 (0x04)   SIO1 DSR (data set ready)
    Bit 3 (0x08)   VRAM port 0 access strobe
    Bit 4 (0x10)   VRAM port 1 access strobe
    Bit 5           Not accessed by software
    Bit 6 (0x40)   VRAM clock edge A (toggles on VRAM bus activity)
    Bit 7 (0x80)   VRAM clock edge B (toggles on VRAM bus activity)

  Byte 3:
    Bit 0 (0x01)   RAM chip select
    Bits 2-1       Transaction boundary (both set = end of bus cycle)
    Bits 6-3       nMWEN[3:0] - SDRAM byte write enables (active-low,
                   one per byte lane, active count = bytes written)
    Bit 7           Not accessed by software


  Word 1 (bytes 4-7) - Address Bus and SBus Selects
  --------------------------------------------------
  Bytes 4-7 (32-bit LE):
    Bits 28-5      24-bit bus address (valid during addressed transactions)

  Byte 4:
    Bit 0 (0x01)   SBus control flag
    Bit 2 (0x04)   PIO device select
    Bit 4 (0x10)   VBLNK (vertical blank signal)

  Byte 7:
    Bit 5 (0x20)   SPU chip select
    Bit 6 (0x40)   GPU / DMA bus arbitration


  Word 2 (bytes 8-11) - VRAM Bus and Peripheral Signals
  ------------------------------------------------------
  Bytes 8-10 (from 32-bit LE):
    Bits 16-8      9-bit VRAM X coordinate, port 0 (half-pixel units)
    Bits 25-17     9-bit VRAM X coordinate, port 1 (half-pixel units)
    VRAM Y coordinates are accumulated by software across frames,
    not directly present in the raw capture.

  Byte 8:
    Bit 1 (0x02)   GUNINT (lightgun interrupt signal)
    Bit 2 (0x04)   PIO flag (sub-bus)
    Bit 6 (0x40)   CD device select
    Bits 0,3,4,5,7 Not accessed by software

  Byte 11:
    Bit 2 (0x04)   VRAM transfer active A
    Bit 3 (0x08)   VRAM transfer active B
    Bit 4 (0x10)   VRAM vertical sync (used by VRAM decoder for frame sync)
    Bit 6 (0x40)   VRAM read/write direction
    Bit 7 (0x80)   SIO1 CTS (clear to send)
    Bits 0,1,5     Not accessed by software


  Word 3 (bytes 12-15) - GPU Data Bus
  ------------------------------------
  Full 32-bit capture of the GPU data bus. Interpretation depends on
  what the GPU is doing at the time of capture:
    During OT traversal:  Bits 31-24 = GP0 command byte
                          Bits 23-0  = next OT pointer (0xFFFFFF = end)
    During vertex data:   Bits 15-0  = X coordinate
                          Bits 31-16 = Y coordinate
    During color data:    Bits 7-0   = Red
                          Bits 15-8  = Green
                          Bits 23-16 = Blue
  The GP0 command byte identifies the GPU primitive type:
    0x20 POLY_F3     0x24 POLY_FT3    0x28 POLY_F4     0x2C POLY_FT4
    0x30 POLY_G3     0x34 POLY_GT3    0x38 POLY_G4     0x3C POLY_GT4
    0x40 LINE_F2     0x48 LINE_F3     0x4C LINE_F4
    0x50 LINE_G2     0x58 LINE_G3     0x5C LINE_G4
    0x60 TILE_any    0x64 SPRT_any    0x70 TILE_1      0x74 TILE_8
    0x78 TILE_16     0x7C SPRT_8/16
    0x02 BlockFill
    0xE0+ GP1 commands (display control)
```

#### PA Waveform Signals
The PA captures five individual digital signal lines, displayed as waveforms in the PA32 GUI alongside a synthetic SYSCLK reference clock. The signal-to-bit assignments have been confirmed empirically by crafting test PAD files and observing the PA32 waveform display:
```
  Byte 4 bit 4 (0x10)   VBLNK   Vertical blank
  Byte 8 bit 1 (0x02)   GUNINT  Lightgun interrupt
  Byte 2 bit 1 (0x02)   RXD1    SIO1 receive data (active-low on hardware)
  Byte 2 bit 2 (0x04)   DSR1    SIO1 data set ready (active-low on hardware)
  Byte 11 bit 7 (0x80)  CTS1    SIO1 clear to send (active-low on hardware)
```
The GUI displays these with asterisks (GUNINT*, RXD1*, DSR1*, CTS1*) to indicate active-low signals. SYSCLK is not captured from hardware - it is a synthetic reference waveform generated by PA32.EXE.

#### PA Decoded Analysis Views
The PA software (PA32.EXE + LIBPA.DLL) decodes the raw frames into several analysis views:
```
  Main RAM Bus (Time)   - Transaction type per cycle: Idle, Refresh, RAS Precharge,
                          PIO DMA Write/Read, CD Write/Read, SPU DMA Write/Read,
                          Internal DMA Write/Read, GPU DMA Write/Read,
                          Data Write/Read, Inst Burst Read
  Sub Bus (Time)        - Peripheral bus activity: Idle, Read/Write PIO,
                          Read/Write CD, Read/Write SPU, Read/Write RAM,
                          Read/Write Others
  Video RAM Bus         - VRAM transfer type: Idle, Read, Write, Block Write,
                          Read Modify Write, Texture Read, CLUT Read A/B
  GPU Packets           - Decoded GPU primitives: polygon types, lines, sprites,
                          tiles, block fills, null packets, commands
  Waveform Signals      - Five digital signal traces (see above)
```
The bus type classification is not stored in the capture data. It is derived at display time by multi-frame state machines in LIBPA.DLL that track SDRAM RAS/CAS sequences, chip select transitions, and write enable patterns across consecutive frames.

#### PA Not Yet Documented
The following aspects of the PA hardware and software have not been reverse-engineered:
```
  - SDRAM address bit scrambling (the exact rearrangement of raw bits in bytes 0-1
    to reconstruct logical addresses through RAS/CAS phases)
  - Trigger configuration (the meaning of the registers in banks 1-10 that
    control what conditions start and stop a capture)
  - The VRAM bus decoder's full state machine (multi-cycle classification of
    Read vs Write vs Block Write vs Read-Modify-Write vs Texture Read vs CLUT Read)
  - 15 bits in the capture frame not accessed by the software
    (byte 2 bit 5, byte 3 bit 7, byte 8 bits 0/3/4/5/7, byte 11 bits 0/1/5)
  - Physical signal line mapping to PA daughterboard pins
```

#### PA Capture File Format (.PAD)
PA32.EXE saves and loads capture data in `.PAD` files. The format uses MFC CArchive serialization with 32-bit tagged fields, followed by a bulk dump of raw capture frames. Two format versions exist: "PAD2.02" and "PAD2.03" - differences between them are unknown.
```
  File Structure:
    Header (variable length, typically ~13KB for the included tutorial)
    Raw frame data (16 bytes per frame, up to 64MB)
    End marker (4 bytes: 0x0001FFFF) (?)

  Header Tags (32-bit little-endian, format: category<<16 | field):
    Category 1 - File metadata:
      0x10001   String: format identifier ("PAD2.02" or "PAD2.03")
      0x10002   String: version string
      0x10003   uint16: unknown
      0x10004   uint32: unknown
      0x10005   uint32: unknown (stored at internal offset 0x1004C4)
      0x10006   uint32: unknown (stored at internal offset 0x1004C8)
      0x10007   uint32: unknown (stored at internal offset 0x1004CC)
      0x10008   uint16: unknown
      0x10009   uint16: unknown
      0x1000A   uint16: unknown
      0x1000B   String: label (e.g. "[Sampled on ]")
      0x1000C   Serialized object: additional metadata
      0x1000D   uint32: unknown
      0x1000E   uint16: unknown

    Category 2 - Trigger configuration:
      Internal structure not decoded.

    Category 3:
      0x30001   uint16: unknown

    Category 4 - Symbol map:
      Contains segment and function names with address ranges from the
      .MAP file. Used for address-to-symbol resolution during analysis.
      Per-entry serialization format not decoded.

    Category 5 - Capture data:
      0x50001   uint32: unknown (stored at internal offset 0x1004C4)
      0x50002   uint32: unknown (stored at internal offset 0x1004C8)
      0x50003   uint32: total frame count (stored at 0x1004CC, confirmed)
      0x50004   uint16: unknown (stored at 0x1004D0)
      0x50005   uint16: has raw data flag (stored at 0x1004D4, confirmed:
                if nonzero, tag 0x50014 contains frame data)
      0x50006-  uint16 values: configuration (stored at 0x1004D8-0x100500)
      0x50013
      0x50014   Bulk raw frame data (confirmed):
                No explicit length - reader uses frame count from 0x50003.
                Data is written/read in chunks of 0x400 (1024) frames.
                Each chunk is 0x4000 (16384) bytes of raw 16-byte frames.
                No per-chunk headers - pure concatenated raw frames.
      0x50015   uint16: unknown (stored at 0x100510)
      0x50016   uint16: unknown (stored at 0x100514)
      0x50017   uint16: unknown (stored at 0x100518)

    0x1FFFF   End marker (terminates the tag loop)

  Serialization notes:
    Strings: length-prefixed (1 byte for short strings; MFC CArchive may
    use 2-byte or 4-byte lengths for longer strings - not fully traced).
    Integer values are little-endian. Tag parsing reads 4 bytes at a time
    from the MFC CArchive stream.
```
The included tutorial capture (`PA/DATA/TUTO3.PAD`, 18MB) has a 13,156-byte header followed by 1,132,544 raw 16-byte frames (18,120,704 bytes) and 4 trailing bytes.

#### PA Software
```
  PA32.EXE    Windows GUI for capture visualization and analysis
  LIBPA.DLL   Win32 library implementing the PA protocol (CPalib C++ class)
  PSX95PA.VXD Win95 kernel driver (thin I/O port wrapper)
  PSXNTPA.SYS WinNT kernel driver (thin I/O port wrapper)
```
The PA software is included in the PSY-Q SDK under the PA directory. The kernel drivers only provide port I/O access - all protocol logic is in LIBPA.DLL.

#### Configuration Files
DEXBIOS.COM reads configuration from `PSYQ.INI`, located via the `PSYQ_PATH` environment variable:
```
  [DEXBIOS]
  ADDRESS=0320     ;I/O base address (hex, upper 12 bits)
  IRQ=11           ;IRQ number (0=disabled, 10/11/12/15 valid)
```
Command line flags `/A` (address) and `/I` (IRQ) override INI settings. The `/B` flag sets the PCDRV transfer buffer size in KB (range 2-32).
