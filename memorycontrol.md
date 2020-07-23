#   Memory Control
The Memory Control registers are initialized by the BIOS, and, normally
software doesn't need to change that settings. Some registers are useful for
expansion hardware (allowing to increase the memory size and bus width).<br/>

#### 1F801000h - Expansion 1 Base Address (usually 1F000000h)
#### 1F801004h - Expansion 2 Base Address (usually 1F802000h)
```
  0-23   Base Address   (Read/Write)
  24-31  Fixed          (Read only, always 1Fh)
```
For Exansion 1, the address is forcefully aligned to the selected expansion
size (see below), ie. if the size is bigger than 1 byte, then the lower bit(s)
of the base address are ignored.<br/>
For Expansion 2, trying to use ANY other value than 1F802000h seems to disable
the Expansion 2 region, rather than mapping it to the specified address (ie.
Port 1F801004h doesn't seem to work).<br/>
For Expansion 3, the address seems to be fixed (1FA00000h).<br/>

#### 1F801008h - Expansion 1 Delay/Size (usually 0013243Fh) (512Kbytes, 8bit bus)
#### 1F80100Ch - Expansion 3 Delay/Size (usually 00003022h) (1 byte)
#### 1F801010h - BIOS ROM Delay/Size (usually 0013243Fh) (512Kbytes, 8bit bus)
#### 1F801014h - SPU Delay/Size (200931E1h) (use 220931E1h for SPU-RAM reads)
#### 1F801018h - CDROM Delay/Size (00020843h or 00020943h)
#### 1F80101Ch - Expansion 2 Delay/Size (usually 00070777h) (128 bytes, 8bit bus)
```
  0-3   Unknown (R/W)
  4-7   Access Time        (00h..0Fh=00h..0Fh Cycles)
  8     Use COM0 Time      (0=No, 1=Yes, add to Access Time)
  9     Use COM1 Time      (0=No, 1=Probably Yes, but has no effect?)
  10    Use COM2 Time      (0=No, 1=Yes, add to Access Time)
  11    Use COM3 Time      (0=No, 1=Yes, clip to MIN=(COM3+6) or so?)
  12    Data Bus-width     (0=8bit, 1=16bit)
  13-15 Unknown (R/W)
  16-20 Memory Window Size (1 SHL N bytes) (0..1Fh = 1 byte ... 2 gigabytes)
  21-23 Unknown (always zero)
  24-27 Unknown (R/W) ;must be non-zero for SPU-RAM reads
  28    Unknown (always zero)
  29    Unknown (R/W)
  30    Unknown (always zero)
  31    Unknown (R/W) (Port 1F801008h only; always zero for other ports)
```
Trying to access addresses that exceed the selected size causes an exception.
Maximum size would be Expansion 1 = 17h (8MB), BIOS = 16h (4MB), Expansion 2 =
0Dh (8KB), Expansion 3 = 15h (2MB). Trying to select larger sizes would overlap
the internal I/O ports, and crash the PSX. The Size bits seem to be ignored for
SPU/CDROM. The SPU timings seem to be applied for both the 200h-byte SPU region
at 1F801C00h and for the 200h-byte unknown region at 1F801E00h.<br/>

#### 1F801020h - COM\_DELAY / COMMON\_DELAY (00031125h or 0000132Ch or 00001325h)
```
  0-3   COM0 - Offset A   ;used for SPU/EXP2 (and for adjusted CDROM timings)
  4-7   COM1 - No effect? ;used for EXP2
  8-11  COM2 - Offset B   ;used for BIOS/EXP1/EXP2
  12-15 COM3 - Min Value  ;used for CDROM
  16-17 COM? - Unknown    ;used for whatever
  18-31 Unknown/unused (read: always 0000h)
```
This register contains clock cycle offsets that can be added to the Access Time
values in Port 1F801008h..1Ch. Works (somehow) like so:<br/>
```
  1ST=0, SEQ=0, MIN=0
  IF Use_COM0 THEN 1ST=1ST+COM0-1, SEQ=SEQ+COM0-1
  IF Use_COM2 THEN 1ST=1ST+COM2,   SEQ=SEQ+COM2
  IF Use_COM3 THEN MIN=COM3
  IF 1ST<6 THEN 1ST=1ST+1   ;(somewhat like so)
  1ST=1ST+AccessTime+2, SEQ=SEQ+AccessTime+2
  IF 1ST<(MIN+6) THEN 1ST=(MIN+6)
  IF SEQ<(MIN+2) THEN SEQ=(MIN+2)
```
The total access time is the sum of First Access, plus any Sequential
Access(es), eg. for a 32bit access with 8bit bus: Total=1ST+SEQ+SEQ+SEQ.<br/>
If the access is done from code in (uncached) RAM, then 0..4 cycles are added
to the Total value (the exact number seems to vary depending on the used COMx
values or so).<br/>
And the purpose... probably allows to define the length of the chipselect
signals, and of gaps between that signals...?<br/>

#### 1F801060h - RAM\_SIZE (R/W) (usually 00000B88h) (or 00000888h)
```
  0-2   Unknown (no effect)
  3     Crashes when zero (except PU-7 and EARLY-PU-8, which <do> set bit3=0)
  4-6   Unknown (no effect)
  7     Delay on simultaneous CODE+DATA fetch from RAM (0=None, 1=One Cycle)
  8     Unknown (no effect) (should be set for 8MB, cleared for 2MB)
  9-11  Define 8MB Memory Window (first 8MB of KUSEG,KSEG0,KSEG1)
  12-15 Unknown (no effect)
  16-31 Unknown (Garbage)
```
Possible values for Bit9-11 are:<br/>
```
  0 = 1MB Memory + 7MB Locked
  1 = 4MB Memory + 4MB Locked
  2 = 1MB Memory + 1MB HighZ + 6MB Locked
  3 = 4MB Memory + 4MB HighZ
  4 = 2MB Memory + 6MB Locked              ;<--- would be correct for PSX
  5 = 8MB Memory                           ;<--- default by BIOS init
  6 = 2MB Memory + 2MB HighZ + 4MB Locked     ;<-- HighZ = Second /RAS
  7 = 8MB Memory
```
The BIOS initializes this to setting 5 (8MB) (ie. the 2MB RAM repated 4 times),
although the "correct" would be setting 4 (2MB, plus other 6MB Locked). The
remaining memory, after the first 8MB, and up to the Expansion/IO/BIOS region
seems to be always Locked.<br/>
The HighZ regions are FFh-filled, that even when grounding data lines on the
system bus (ie. it is NOT a mirror of the PIO expansion region).<br/>
Locked means that the CPU generates an exception when accessing that area.<br/>
Note: Wipeout uses a BIOS function that changes RAM\_SIZE to 00000888h (ie. with
corrected size of 2MB, and with the unknown Bit8 cleared). Gundam Battle
Assault 2 does actually use the "8MB" space (with stacktop in mirrored RAM at
807FFFxxh).<br/>
Clearing bit7 causes many games to hang during CDROM loading on both EARLY-PU-8
and LATE-PU-8 (but works on PU-18 through PM-41).<br/>

#### FFFE0130h Cache Control (R/W)
```
  0-2   Unknown (Read/Write)                                            (R/W)
  3     Scratchpad Enable 1 (0=Disable, 1=Enable when Bit7 is set, too) (R/W)
  4-5   Unknown (Read/Write)                                            (R/W)
  6     Unknown (read=always zero)                  (R) or (W) or unused..?
  7     Scratchpad Enable 2 (0=Disable, 1=Enable when Bit3 is set, too) (R/W)
  8     Unknown                                                         (R/W)
  9     Crash (0=Normal, 1=Crash if code-cache enabled)                 (R/W)
  10    Unknown (read=always zero)                  (R) or (W) or unused..?
  11    Code-Cache Enable (0=Disable, 1=Enable)                         (R/W)
  12-31 Unknown                                                         (R/W)
```
Used by BIOS to initialize cache (in combination with COP0), like so:<br/>
```
 Init Cache Step 1:
  [FFFE0130h]=00000804h, then set cop0_sr=00010000h, then
  zerofill each FOURTH word at [0000..0FFFh], then set cop0_sr=zero.
 Init Cache Step 2:
  [FFFE0130h]=00000800h, then set cop0_sr=00010000h, then
  zerofill ALL words at [0000h..0FFFh], then set cop0_sr=zero.
 Finish Initialization:
  read 8 times 32bit from [A0000000h], then set [FFFE0130h]=0001E988h
```
Note: FFFE0130h is described in LSI's "L64360" datasheet, chapter 14 (and
probably also in their LR33300/LR33310 datasheet, if it were available in
internet).<br/>



