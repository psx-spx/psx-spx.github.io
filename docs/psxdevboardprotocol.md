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
