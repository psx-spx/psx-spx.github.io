#   CDROM Format
#### General CDROM Disk Format
[CDROM Disk Format](cdromformat.md#cdrom-disk-format)<br/>
[CDROM Subchannels](cdromformat.md#cdrom-subchannels)<br/>
[CDROM Sector Encoding](cdromformat.md#cdrom-sector-encoding)<br/>
[CDROM Scrambling](cdromformat.md#cdrom-scrambling)<br/>
[CDROM XA Subheader, File, Channel, Interleave](cdromformat.md#cdrom-xa-subheader-file-channel-interleave)<br/>
[CDROM XA Audio ADPCM Compression](cdromformat.md#cdrom-xa-audio-adpcm-compression)<br/>
[CDROM ISO Volume Descriptors](cdromformat.md#cdrom-iso-volume-descriptors)<br/>
[CDROM ISO File and Directory Descriptors](cdromformat.md#cdrom-iso-file-and-directory-descriptors)<br/>
[CDROM ISO Misc](cdromformat.md#cdrom-iso-misc)<br/>
[CDROM File Formats](cdromfileformats.md)<br/>
[CDROM Video CDs (VCD)](cdromvideocdsvcd.md)<br/>

#### Playstation CDROM Protection
[CDROM Protection - SCEx Strings](cdromformat.md#cdrom-protection-scex-strings)<br/>
[CDROM Protection - Bypassing it](cdromformat.md#cdrom-protection-bypassing-it)<br/>
[CDROM Protection - Modchips](cdromformat.md#cdrom-protection-modchips)<br/>
[CDROM Protection - Chipless Modchips](cdromformat.md#cdrom-protection-chipless-modchips)<br/>
[CDROM Protection - LibCrypt](cdromformat.md#cdrom-protection-libcrypt)<br/>



##   CDROM Disk Format
#### Overview
The PSX uses a ISO 9660 filesystem, with data stored on CD-XA (Mode2) Sectors.
ISO 9660 is standard for CDROM disks, although newer CDROMs may use extended
filesystems, allowing to use long filenames and lowercase filenames, the PSX
Kernel doesn't support such stuff, and, in fact, it's putting some restrictions
on the ISO standard: it's limiting file names to MSDOS-style 8.3 format, and
it's allowing only a limited number of files and directories per disk.<br/>

#### CDROM Filesystem (ISO 9660 aka ECMA-119)
```
  Originally intended for Mode1 Sectors (but is also used for CD-XA Mode2)
  Supports "FILENAME.EXT;VERSION" filenames (version is usually "1")
  Supports all-uppercase filenames and directory names (0-9, A-Z, underscore)
  For PSX: Max 8-character filenames with max 3-character extensions
  For PSX: Max 8-character directory names, without extension
  For PSX: Max one sector per directory (?)
  For PSX: Max one sector (or less?) per path table (?)
```

#### CDROM Extended Architecture (CD-ROM XA aka CD-XA)
```
  Uses Mode2 Sectors (see Sector Encoding chapter)
  Allows 800h or 914h byte data per sector (with/without error correction)
  Allows to break interleaved data into separate files/channels
  Supports XA-ADPCM compressed audio data
  Stores "CD-XA001" at 400h Primary Volume Descriptor (?)
  Stores 14 extra bytes in System Use area (LEN_SU) of Directory Entries
```

#### Physical Audio/CDROM Disk Format (ISO/IEC 10149 aka ECMA-130)
```
  Defines physical metrics of the CDROM and Audio disks
  Defines Sub-channels and Track.Index and Minute.Second.Fraction numbering
  Defines 14bit-per-byte encoding, and splits sectors into frames
  Defines ECC and EDC (error correction and error detection codes)
```

#### Available Documentation
ISO documents are commercial standards (not available for download), however,
they are based on ECMA standards (which are free for download, however, the
ECMA stuff is in PDF format, so one may treat it as commercial bullshit, too).
CD-ROM XA is commercial only (not available for download), and, CD-XA doesn't
seem to have become very popular outside of the PSX-world, so there's very
little information available, portions of CD-XA are also used in the CD-i
standard (which may be a little better or worse documented).<br/>

#### Stuff
```
  sessions  one or more sessions per disk
  tracks    99 tracks per disk     (01h..99h) (usually only 01h on Data Disks)
  index     99 indices per track   (01h..99h) (rarely used, usually always 01h)
  minutes   74 minutes per disk    (00h..73h) (or more, with some restrictions)
  seconds   60 seconds per minute  (00h..59h)
  sectors   75 sectors per second  (00h..74h)
  frames    98 frames per sector
  bytes     33 bytes per frame (24+1+8 = data + subchannel + error correction)
  bits      14 bits per byte   (256 valid combinations, and many invalid ones)
```

#### Track.Index (stored in subchannel, in BCD format)
Multiple Tracks are usually used only on Audio Disks (one track for each song,
numbered 01h and up), a few Audio Disks may also split Tracks into separate
fragments with different Index values (numbered 01h and up, but most tracks
have only Index 01h). A simple Data Disk would usually contain only one Track
(all sectors marked Track=01h and Index=01h), although some more complex Data
Disks may have multiple Data tracks and/or Audio tracks.<br/>

#### Minute.Second.Sector (stored in subchannel, and in Data sectors, BCD format)
The sectors on CDROMs and CD Audio disks are numbered in Minutes, Seconds, and
1/75 fragments of a second (where a "second" is referring to single-speed
drives, ie. the normal CD Audio playback speed).<br/>
Minute.Second.Sector is stored twice in the subchannel (once the "absolute"
time, and once the "local" time).<br/>
The "absolute" sector number (counted from the begin of the disk) is mainly
relevant for Seek purposes (telling the controller if the drive head is on the
desired location, or if it needs to move the head backwards or forwards).<br/>
The "local" sector number (counted from the begin of the track) is mainly
relevant for Audio Players, allowing to pass the data directly to the
Minute:Second display, without needing to subtract the start address of the
track.<br/>
Data disks are additionally storing the "absolute" values in their Data Areas,
basically that's just the subchannel data duplicated, but more precisely
assigned - the problem with the subchannel data is that the CD Audio standard
seems to lack a clear definition that would assign the begin of the sub-channel
block to the exact begin of a sector; so, when using only the subchannel data,
some Drive Controllers may assign the begin of a new sector to another location
as than other Controllers do, for Audio Disks that isn't too much of a problem,
but for Data Disks it'd be fatal.<br/>

#### Subchannels
Each frame contains 8 subchannel bits (named P,Q,R,S,T,U,V,W). So, a sector
(with 98 frames) contains 98 bits (12.25 bytes) for each subchannel.<br/>
[CDROM Subchannels](cdromformat.md#cdrom-subchannels)<br/>

#### Error Correction
Each Frame contains 8 bytes Error Correction information, which is mainly used
for Audio Disks, but it isn't 100% fail-proof, for that reason, Data Disks are
containing additional Error Correction in the 930h-byte data area (the audio
correction is probably focusing on repairing the MSBs of the 16bit samples, and
gives less priority on the LSBs). Error Correction is some kind of a huge
complex checksum, which allows to detect the location of faulty bytes, and to
fix them.<br/>

#### 930h-Byte Sectors
The "user" area for each sector is 930h bytes (2352 bytes). That region is
combined of the 24-byte data per frame (and excludes the 8-byte audio error
correction info, and the 1-byte subchannel data).<br/>
Most CDROM Controllers are only giving access to this 930h-byte region (ie.
there's no way to read the audio error correction info by software, and only
limited access to the subchannel data, such like allowing to read only the
Q-channel for showing track/minute/second in audio playback mode).<br/>
On Audio disks, the 930h bytes are plain data, on Data disks that bytes are
containing headers, error correction, and usually only 800h bytes user data
(for more info see Sector Encoding chapter).<br/>

#### Sessions
Multi-Sessions are mainly used on CDR's, allowing to append newer data at the
end of the disk at a later time. First of, the old session must contain a flag
indicating that there may be a newer session, telling the CDROM Controller to
search if one such exists (and if that is equally flagged, to search for an
even newer session, and so on until reaching the last and newest session).<br/>
Each session contains a complete new ISO Volume Descriptor, and may
additionally contain new Path Tables, new Directories, and new Files. The
Driver Controller is usually recursing only the Volume Descriptor of the newest
session. However, the various Directory Records of the new session may refer to
old files or old directories from previous sessions, allowing to "import" the
older files, or to "rename" or "delete" them by assigning new names to that
files, or by removing them from the directory.<br/>
The PSX is reportedly not supporting multi-session disks, but that doesn't seem
to be correct, namely, the Setsession command is apparently intended for that
purpose... though not sure if the PSX Kernel is automatically searching the
newest session... otherwise the boot executable in the first session would need
to do that manually by software, and redirect control to the boot executable in
the last session.<br/>



##   CDROM Subchannels
#### Subchannel P
Subchannel P contains some kind of a Pause flag (to indicate muted areas
between Audio Tracks). This subchannel doesn't have any checksum, so the data
cannot be trusted to be intact (unless when sensing a longer stream of
all-one's, or all zero's). Theoretically, the 98 pause bits are somehow
associated to the 98 audio frames (with 24 audio bytes each) of the sector.
However, reportedly, Subchannel P does contain two sync bits, if that is true,
then there'd be only 96 pause flags for 98 audio frames. Strange.<br/>
Note: Another way to indicate "paused" regions is to set Subchannel Q to ADR=1
and Index=00h.<br/>

#### Subchannel Q
contains the following information:<br/>
```
  Bits Expl.
  2    Sub-channel synchronization field
  8    ADR/Control (see below)
  72   Data (content depends on ADR)
  16   CRC-16-CCITT error detection code (big-endian: bytes ordered MSB, LSB)
```
Possible values for the ADR/Control field are:<br/>
```
  Bit0-3 ADR (0=No data, 1..3=see below, 4..0Fh=Reserved)
  Bit4   Audio Preemphasis  (0=No, 1=Yes)      (Audio only, must be 0 for Data)
  Bit5   Digital Copy       (0=Prohibited, 1=Allowed)
  Bit6   Data               (0=Audio, 1=Data)
  Bit7   Four-Channel Audio (0=Stereo, 1=Quad) (Audio only, must be 0 for Data)
```
The 72bit data regions are, depending on the ADR value...<br/>

#### Subchannel Q with ADR=1 during Lead-In -- Table of Contents (TOC)
```
  8    Track number (fixed, must be 00h=Lead-in)
  8    Point (01h..99h or A0h..A2h, see last three bytes for more info)
  24   MSF address (incrementing address within the Lead-in area)
         Note: On some disks, these values are choosen so that the lead-in
         <starts> at 00:00:00, on other disks so that it <ends> at 99:59:74.
  8    Reserved (00h)
```
When Point=01h..99h (Track 1..99) or Point=A2h (Lead-Out):<br/>
```
  24   MSF address (absolute address, start address of the "Point" track)
```
When Point=A0h (First Track Number):<br/>
```
  8    First Track number (BCD)
  8    Disk Type Byte (00h=CD-DA or CD-ROM, 10h=CD-I, 20h=CD-ROM-XA)
  8    Reserved (00h)
```
When Point=A1h (Last Track Number):<br/>
```
  8    Last Track number (BCD)
  16   Reserved (0000h)
```
ADR=1 should exist in 3 consecutive lead-in sectors.<br/>

#### Subchannel Q with ADR=1 in Data region -- Position
```
  8    Track number (01h..99h=Track 1..99)
  8    Index number (00h=Pause, 01h..99h=Index within Track)
  24   Track relative MSF address (decreasing during Pause)
  8    Reserved (00h)
  24   Absolute MSF address
```
ADR=1 is required to exist in at least 9 out of 10 consecutive data sectors.<br/>

#### Subchannel Q with ADR=1 during Lead-Out -- Position
```
  8    Track number (fixed, must be AAh=Lead-Out)
  8    Index number (fixed, must be 01h) (there's no Index=00h in Lead-Out)
  24   Track relative MSF address (increasing, 00:00:00 and up)
  8    Reserved (00h)
  24   Absolute MSF address
```
ADR=1 should exist in 3 consecutive lead-out sectors (and may then be followed
by ADR=5 on multisession disks).<br/>

#### Subchannel Q with ADR=2 -- Catalogue number of the disc (UPC/EAN barcode)
```
  52   EAN-13 barcode number (13-digit BCD)
  12   Reserved (000h)
  8    Absolute Sector number (BCD, 00h..74h) (always 00h during Lead-in)
```
If the first digit of the EAN-13 number is "0", then the remaining digits are a
UPC-A barcode number. Either the 13-digit EAN-13 number, or the 12-digit UPC-A
number should be printed as barcode on the rear-side of the CD package.<br/>
The first some digits contain a country code (EAN only, not UPC), followed by a
manufacturer code, followed by a serial number. The last digit contains a
checksum, which can be calculated as 250 minus the sum of the first 12 digits,
minus twice the sum of each second digit, modulated by 10.<br/>
ADR=2 isn't included on all CDs, and, many CDs do have ADR=2, but the 13 digits
are all zero. Most CDROM drives do not allow to read EAN/UPC numbers.<br/>
If present, ADR=2 should exist in at least 1 out of 100 consecutive sectors.
ADR=2 may occur also in Lead-in.<br/>

#### Subchannel Q with ADR=3 -- ISRC number of the current track
(ISO 3901 and DIN-31-621):<br/>
```
  12   Country Code      (two 6bit characters)   (ASCII minus 30h) ;eg. "US"
  18   Owner Code        (three 6bit characters) (ASCII minus 30h)
  2    Reserved          (zero)
  8    Year of recording (2-digit BCD) ;eg. 82h for 1982
  20   Serial number     (5-digit BCD) ;usually increments by 1 or 10 per track
  4    Reserved          (zero)
  8    Absolute Sector number (BCD, 00h..74h) (always 00h during Lead-in)
```
Most CDROM drives for PC's do not allow to read ISRC numbers (or even worse,
they may accidently return the same ISRC number on every two tracks).<br/>
If present, ADR=3 should exist in at least 1 out of 100 consecutive sectors.
However, reportedly, ADR=3 should not occur in Lead-in.<br/>

#### Subchannel Q with ADR=5 in Lead-in -- Multisession Lead-In Info
When Point=B0h:<br/>
```
  8    Track number (fixed, must be 00h=Lead-in)
  8    POINT = B0h (multi-session disc)
  24   MM:SS:FF = the start time for the next possible session's program area,
       a final session is indicated by FFh:FFh:FFh,
       or when the ADR=5 / Point=B0h is absent.
  8    Number of different Mode-5 pointers present.
  24   MM:SS:FF = the maximum possible start time of the outermost Lead-out
```
When Point=C0h:<br/>
```
  8    Track number (fixed, must be 00h=Lead-in)
  8    POINT = C0h (Identifies a Multisession disc, together with POINT=B0h)
  24   ATIP values from Special Information 1, ID=101
  8    Reserved (must be 00h)
  24   MM:SS:FF = Start time of the first Lead-in area of the disc
```
And, optionally, when Point=C1h:<br/>
```
  8    Track number (fixed, must be 00h=Lead-in)
  8    POINT=C1h
  8x7  Copy of information from A1 point in ATIP
```

#### Subchannel Q with ADR=5 in Lead-Out -- Multisession Lead-Out Info
```
  8    Track number (fixed, must be AAh=Lead-out)
  8    POINT = D1h (Identifies a Multisession lead-out)
  24   Usually zero (or maybe ATIP as in Lead-In with Point=C0h...?)
  8    Seems to be the session number?
  24   MM:SS:FF = Absolute address of the First data sector of the session
```
Present in 3 consequtive sectors (3x ADR=1, 3x ADR=5, 3x ADR=1, 3x ADR=5, etc).<br/>

#### Subchannel Q with ADR=5 in Lead-in -- CDR/CDRW Skip Info (Audio Only)
When Point=01h..40h:<br/>
```
  8    Track number (fixed, must be 00h=Lead-in)
  8    POINT=01h..40h (This identifies a specific playback skip interval)
  24   MM:SS:FF Skip interval stop time in 6 BCD digits
  8    Reserved (must be 00h)
  24   MM:SS:FF Skip interval start time in 6 BCD digits
```
When Point=B1h:<br/>
```
  8    Track number (fixed, must be 00h=Lead-in)
  8    POINT=B1h (Audio only: This identifies the presence of skip intervals)
  8x4  Reserved (must be 00h,00h,00h,00h)
  8    the number of skip interval pointers in POINT=01h..40h
  8    the number of skip track assignments in POINT=B2h..B4h
  8    Reserved (must be 00h)
```
When Point=B2h,B3h,B4h:<br/>
```
  8    Track number (fixed, must be 00h=Lead-in)
  8    POINT=B2h,B3h,B4h (This identifies tracks that should be skipped)
  8    1st Track number to skip upon playback (01h..99h, must be nonzero)
  8    2nd Track number to skip upon playback (01h..99h, or 00h=None)
  8    3rd Track number to skip upon playback (01h..99h, or 00h=None)
  8    Reserved (must be 00h)... unclear... OR... 4th (of 7) skip info's...?
  8    4th Track number to skip upon playback (01h..99h, or 00h=None)
  8    5th Track number to skip upon playback (01h..99h, or 00h=None)
  8    6th Track number to skip upon playback (01h..99h, or 00h=None)
```
Note: Skip intervals are seldom written by recorders and typically ignored by
readers.<br/>

#### Subchannel R..W
Subchannels R..W are usually unused, except for some extended formats:<br/>
```
  CD-TEXT in the Lead-In area (see below)
  CD-TEXT in the Data area    (rarely used)
  CD plus Graphics (CD+G)     (rarely used)
```
Most CDROM drives do not allow to read these subchannels. CD-TEXT was designed
by Sony and Philips in 1997, so it should be found only on (some) newer discs.
Most CD/DVD players don't support it (the only exception is that CD-TEXT seems
to be popular for car hifi equipment). Most record labels don't support
CD-TEXT, even Sony seems to have discontinued it on their own records after
some years (so CD-TEXT is very rare on original disks, however, CDR software
does often allow to write CD-TEXT on CDRs).<br/>

#### Subchannel R..W, when used for CD-TEXT in the Lead-In area
CD-TEXT is stored in the six Subchannels R..W. Of the 12.25 bytes (98 bits) per
subchannel, only 12 bytes are used. Together, all 6 subchannels have a capacity
of 72 bytes (6x12 bytes) per sector. These 72 bytes are divided into four
CD-TEXT fragments (of 18 bytes each). The format of these 18 bytes is:<br/>
```
  00h 1  Header Field ID1: Pack Type Indicator
  01h 1  Header Field ID2: Track Number
  02h 1  Header Field ID3: Sequence Number
  03h 1  Header Field ID4: Block Number and Character Position Indicator
  04h 12 Text/Data Field
  10h 2  CRC-16-CCITT (big-endian) (across bytes 00h..0Fh)
```
ID1 - Pack Type Indicator:<br/>
```
  80h   Titel      (TEXT)
  81h   Performer  (TEXT)
  82h   Songwriter (TEXT)
  83h   Composer   (TEXT)
  84h   Arranger   (TEXT)
  85h   Message    (TEXT)
  86h   Disc ID    (TEXT?)  (content/format/purpose unknown?)
  87h   Genre      (BINARY) (ID codes unknown?)
  88h   TOC        (BINARY) (content/format/purpose unknown?)
  89h   TOC2       (BINARY) (content/format/purpose unknown?)
  8Ah   Reserved for future
  8Bh   Reserved for future
  8Ch   Reserved for future
  8Dh   Reserved for "content provider" aka "closed information"
  8Eh   UPC/EAN and ISRC Codes (TEXT) (content/format/purpose unknown?)
  8Fh   Blocksize (BINARY) (see below)
```
ID2 - Track Number:<br/>
```
  00h       Title/Performer/etc. for the Disc
  01h..63h  Title/Performer/etc. for Track 1..99 (Non-BCD) (Bit7=Extension)
```
ID3 - Sequence Number:<br/>
```
  00h..FFh  Incrementing Number (00h=First 18-byte fragment, 01h=Second, etc.)
```
ID4 - Block Number and Character Position Indicator:<br/>
```
  Bit7      Character Set      (0=8bit, 1=16bit)
  Bit6-4    Block Number       (0..7 = Language number, as set by "Blocksize")
  Bit3-0    Character Position (0..0Eh=Position, 0Fh=Append to prev fragment)
```
Example Data (generated with CDRWIN):<br/>
```
  ID TR SQ CH <------------Text/Data------------> -CRC-  <---Text--->
  80 00 00 00 54 65 73 74 44 69 73 6B 54 69 74 6C E2 22  TestDiskTitl
  80 00 01 0C 65 00 54 65 73 74 54 72 61 63 6B 54 C9 1B  e.TestTrackT
  80 01 02 0A 69 74 6C 65 31 00 54 65 73 74 54 72 40 3A  itle1.TestTr
  80 02 03 06 61 63 6B 54 69 74 6C 65 32 00 00 00 80 E3  ackTitle2...
  81 00 04 00 54 65 73 74 44 69 73 6B 50 65 72 66 03 DF  TestDiskPerf
  81 00 05 0C 6F 72 6D 65 72 00 54 65 73 74 54 72 12 A5  ormer.TestTr
  81 01 06 06 61 63 6B 50 65 72 66 6F 72 6D 65 72 BC 5B  ackPerformer
  81 01 07 0F 31 00 54 65 73 74 54 72 61 63 6B 50 AC 41  1.TestTrackP
  81 02 08 0A 65 72 66 6F 72 6D 65 72 32 00 00 00 64 1A  erformer2...
  8F 00 09 00 01 01 02 00 04 05 00 00 00 00 00 00 6D E2  ............
  8F 01 0A 00 00 00 00 00 00 00 00 03 0B 00 00 00 CD 0C  ............
  8F 02 0B 00 00 00 00 00 09 00 00 00 00 00 00 00 FC 8C  ............
  00   ;<--- for some reason, CDRWIN stores an ending 00h byte in .CDT files
```
Each Text string is terminated by a 00h byte (or 0000h for 16bit character
set). If there's still room in the 12-byte data region, then first characters
for the next Text string (for the next track) are appended after the 00h byte
(if there's no further track, then the remaining bytes should be padded with
00h).<br/>
The "Blocksize" (ID1=8Fh) consists of three packs with 24h bytes of data (first
0Ch bytes stored with ID2=00h, next 0Ch bytes with ID2=01h, and last 0Ch bytes
with ID2=02h):<br/>
```
  00h  1   Character set (00h,01h,80h,81h,82h = see below)
  01h  1   First track number (usually/always 01h)
  02h  1   Last track number (01h..63h)
  03h  1   1bit-cd-text-in-data-area-flag, 7bit-copy-protection-flags
  04h  16  Number of 18-byte packs for ID1=80h..8Fh
  14h  8   Last sequence number of block 0..7 (or 00h=none)
  1Ch  8   Language codes for block 0..7 (definitions are unknown)
```
Character Set values (for ID1=8Fh, ID2=00h, DATA[0]=charset):<br/>
```
  00h ISO 8859-1
  01h ISO 646, ASCII
  80h MS-JIS
  81h Korean character code
  82h Mandarin (standard) Chinese character code
  Other = reserved
```
"In case the same character stings is used for consecutive tracks, character
09h (or 0909h for 16bit charset) may be used to indicate the same as previous
track. It shall not used for the first track."<br/>

#### adjust\_crc\_16\_ccitt(addr\_len)  ;for CD-TEXT and Subchannel Q
```
  lsb=00h, msb=00h      ;-initial value (zero for both CD-TEXT and Sub-Q)
  for i=0 to len-1      ;-len (10h for CD-TEXT, 0Ah for Sub-Q)
    x = [addr+i] xor msb
    x = x xor (x shr 4)
    msb = lsb xor (x shr 3) xor (x shl 4)
    lsb = x xor (x shl 5)
  next i
  [addr+len+0]=msb xor FFh, [addr+len+1]=lsb xor FFh   ;inverted / big-endian
```



##   CDROM Sector Encoding
#### Audio
```
  000h 930h Audio Data (2352 bytes) (LeftLsb,LeftMsb,RightLsb,RightMsb)
```
#### Mode0 (Empty)
```
  000h 0Ch  Sync   (00h,FFh,FFh,FFh,FFh,FFh,FFh,FFh,FFh,FFh,FFh,00h)
  00Ch 4    Header (Minute,Second,Sector,Mode=00h)
  010h 920h Zerofilled
```
#### Mode1 (Original CDROM)
```
  000h 0Ch  Sync   (00h,FFh,FFh,FFh,FFh,FFh,FFh,FFh,FFh,FFh,FFh,00h)
  00Ch 4    Header (Minute,Second,Sector,Mode=01h)
  010h 800h Data (2048 bytes)
  810h 4    EDC (checksum across [000h..80Fh])
  814h 8    Zerofilled
  81Ch 114h ECC (error correction codes)
```
#### Mode2/Form1 (CD-XA)
```
  000h 0Ch  Sync   (00h,FFh,FFh,FFh,FFh,FFh,FFh,FFh,FFh,FFh,FFh,00h)
  00Ch 4    Header (Minute,Second,Sector,Mode=02h)
  010h 4    Sub-Header (File, Channel, Submode AND DFh, Codinginfo)
  014h 4    Copy of Sub-Header
  018h 800h Data (2048 bytes)
  818h 4    EDC (checksum across [010h..817h])
  81Ch 114h ECC (error correction codes)
```
#### Mode2/Form2 (CD-XA)
```
  000h 0Ch  Sync   (00h,FFh,FFh,FFh,FFh,FFh,FFh,FFh,FFh,FFh,FFh,00h)
  00Ch 4    Header (Minute,Second,Sector,Mode=02h)
  010h 4    Sub-Header (File, Channel, Submode OR 20h, Codinginfo)
  014h 4    Copy of Sub-Header
  018h 914h Data (2324 bytes)
  92Ch 4    EDC (checksum across [010h..92Bh]) (or 00000000h if no EDC)
```

#### encode\_sector
```
  sector[000h]=00h,FFh,FFh,FFh,FFh,FFh,FFh,FFh,FFh,FFh,FFh,00h
  sector[00ch]=bcd(adr/75/60)      ;0..7x
  sector[00dh]=bcd(adr/75 MOD 60)  ;0..59
  sector[00eh]=bcd(adr MOD 75)     ;0..74
  sector[00fh]=mode
  if mode=00h then
    sector[010h..92Fh]=zerofilled
  if mode=01h then
    adjust_edc(sector+0, 800h+10h)
    sector[814h..817h]=00h,00h,00h,00h,00h,00h,00h,00h
    calc_p_parity(sector)
    calc_q_parity(sector)
  if mode=02h and form=1
    sector[012h]=sector[012h] AND (NOT 20h)  ;indicate not form2
    sector[014h..017h]=sector[010h..013h]    ;copy of sub-header
    adjust_edc(sector+10h,800h+8)
    push sector[00ch]           ;\temporarily clear header
    sector[00ch]=00000000h      ;/
    calc_p_parity(sector)
    calc_q_parity(sector)
    pop sector[00ch]            ;-restore header
  if mode=02h and form=2
    sector[012h]=sector[012h] OR 20h         ;indicate form2
    sector[014h..017h]=sector[010h..013h]    ;copy of sub-header
    adjust_edc(sector+10h,914h+8)            ;edc is optional for form2
```

#### calc\_parity(sector,offs,len,j0,step1,step2)
```
  src=00ch, dst=81ch+offs, srcmax=dst
  for i=0 to len-1
    base=src, x=0000h, y=0000h
    for j=j0 to 42
      x=x xor GF8_PRODUCT[j,sector[src+0]]
      y=y xor GF8_PRODUCT[j,sector[src+1]]
      src=src+step1, if (step1=2*44) and (src>=srcmax) then src=src-2*1118
    sector[dst+2*len+0]=x AND 0FFh, [dst+0]=x SHR 8
    sector[dst+2*len+1]=y AND 0FFh, [dst+1]=y SHR 8
    dst=dst+2, src=base+step2
```
calc\_p\_parity(sector) = calc\_parity(sector,0,43,19,2\*43,2)<br/>
calc\_q\_parity(sector) = calc\_parity(sector,43\*4,26,0,2\*44,2\*43)<br/>

#### adjust\_edc(addr,len)
```
  x=00000000h
  for i=0 to len-1
    x=x xor byte[addr+i], x=(x shr 8) xor edc_table[x and FFh]
  word[addr+len]=x  ;append EDC value (little endian)
```

#### init\_tables
```
  for i=0 to FFh
    x=i, for j=0 to 7, x=x shr 1, if carry then x=x xor D8018001h
    edc_table[i]=x
  GF8_LOG[00h]=00h, GF8_ILOG[FFh]=00h, x=01h
  for i=00h to FEh
    GF8_LOG[x]=i, GF8_ILOG[i]=x
    x=x SHL 1, if carry8bit then x=x xor 1dh
  for j=0 to 42
    xx=GF8_ILOG[44-j],  yy=subfunc(xx xor 1,19h)
    xx=subfunc(xx,01h), xx=subfunc(xx xor 1,18h)
    xx=GF8_LOG[xx], yy = GF8_LOG[yy]
    GF8_PRODUCT[j,0]=0000h
    for i=01h to FFh
      x=xx+GF8_LOG[i], if x>=255 then x=x-255
      y=yy+GF8_LOG[i], if y>=255 then y=y-255
      GF8_PRODUCT[j,i]=GF8_ILOG[x]+(GF8_ILOG[y] shl 8)
```

#### subfunc(a,b)
```
  if a>0 then
    a=GF8_LOG[a]-b, if a<0 then a=a+255
    a=GF8_ILOG[a]
  return(a)
```



##   CDROM Scrambling
#### Scrambling
Scambling does XOR the data sectors with random values (done to avoid regular
patterns). The scrambling is applied to Data sector bytes[00Ch..92Fh] (not to
CD-DA audio sectors, and not to the leading 12-byte Sync mark in Data sectors).<br/>
The (de-)scrambling is done automatically by the CDROM controller, so disc
images should usually contain unscrambled data (there are some exceptions such
like CD-i discs that have audio and data sectors mixed inside of the same
track; which may confuse the CDROM controller about whether or not to apply
scrambling to which sectors; so one may need to manually XOR the faulty sectors
in the disc image).<br/>
The scrambling pattern is derived from a 15bit polynomial counter (much like a
noise generator in sound chips). The data bits are XORed with the counters low
bit, and the counters lower 2bit are XORed with each other, and shifted in to
the counters upper bit. To compute 8 bits and once, and store them in a
924h-byte table:<br/>
```
  poly=0001h  ;init 15bit polynomial counter
  for i=0 to 924h-1
    scramble_table[i]=poly AND FFh
    poly=(((poly XOR poly/2) AND 0FFh)*80h) XOR (poly/100h)
  next i
```
The resulting table content should be:<br/>
```
  01h,80h,00h,60h,00h,28h,00h,1Eh,80h,08h,60h,06h,A8h,02h,FEh,81h,
  80h,60h,60h,28h,28h,1Eh,9Eh,88h,68h,66h,AEh,AAh,FCh,7Fh,01h,E0h,
  etc.
```
After scrambling, the data is reportedly "shuffled and byte-swapped". Unknown
what shuffling means. And unknown what/where/why byte-swapping is done (it does
reportedly swap each two bytes in the whole(?) 930h-byte (data-?) sector; which
might date back to different conventions for disc images to contain "16bit
audio samples" in big- or little-endian format).<br/>



##   CDROM XA Subheader, File, Channel, Interleave
The Sub-Header for normal data sectors is usually 00h,00h,08h,00h (some PSX
sectors have 09h instead 08h, indicating the end of "something" or so?<br/>

#### 1st Subheader byte - File Number (FN)
```
  0-7 File Number    (00h..FFh) (for Audio/Video Interleave, see below)
```

#### 2nd Subheader byte - Channel Number (CN)
```
  0-4 Channel Number (00h..1Fh) (for Audio/Video Interleave, see below)
  5-7 Should be always zero
```
Whilst not officially allowed, PSX Ace Combat 3 Electrosphere does use
Channel=FFh for unused gaps in interleaved streaming sectors.<br/>

#### 3rd Subheader byte - Submode (SM)
```
  0   End of Record (EOR) (all Volume Descriptors, and all sectors with EOF)
  1   Video     ;\Sector Type (usually ONE of these bits should be set)
  2   Audio     ; Note: PSX .STR files are declared as Data (not as Video)
  3   Data      ;/
  4   Trigger           (for application use)
  5   Form2             (0=Form1/800h-byte data, 1=Form2, 914h-byte data)
  6   Real Time (RT)
  7   End of File (EOF) (or end of Directory/PathTable/VolumeTerminator)
```
The EOR bit is set in all Volume Descriptor sectors, the last sector (ie. the
Volume Descriptor Terminator) additionally has the EOF bit set. Moreover, EOR
and EOF are set in the last sector of each Path Table, and last sector of each
Directory, and last sector of each File.<br/>

#### 4th Subheader byte - Codinginfo (CI)
When used for Data sectors:<br/>
```
  0-7 Reserved (00h)
```
When used for XA-ADPCM audio sectors:<br/>
```
  0-1 Mono/Stereo     (0=Mono, 1=Stereo, 2-3=Reserved)
  2-2 Sample Rate     (0=37800Hz, 1=18900Hz, 2-3=Reserved)
  4-5 Bits per Sample (0=Normal/4bit, 1=8bit, 2-3=Reserved)
  6   Emphasis        (0=Normal/Off, 1=Emphasis)
  7   Reserved        (0)
```

#### Audio/Video Interleave (Multiple Files/Channels)
The CDROM drive mechanics are working best when continously following the data
spiral on the disk, that works fine for uncompressed Audio Data at normal
speed, but compressed Audio Data the disk is spinning much too fast. To avoid
the drive to need to pause reading or to do permanent backwards seeking, CD-XA
allows to store data interleaved in separate files/channels. With common
interleave values like so:<br/>
```
  Interleave   Data Format
  1/1 (none)   44100Hz Stereo CD Audio at normal speed
  1/8          37800Hz Stereo ADPCM compressed Audio at double speed
  1/16         18900Hz Stereo ADPCM compressed Audio at double speed
  1/16         37800Hz Mono   ADPCM compressed Audio at double speed
  1/32         18900Hz Mono   ADPCM compressed Audio at double speed
  7/8          15fps 320x224 pixel MDEC compressed Videos at double speed
  Unknown if 1/16 and 1/32 interleaves are actually possible (the PSX cdrom
  controller seems to overwrite the IC303 sector buffer entries once every
  eight sectors, so ADPCM data may get destroyed on interleaves above 1/8).
  (Crash Team Racing uses 37800Hz Mono at Double speed, so 1/16 must work).
```
For example, 1/8 means that the controller processes only each 8th sector (each
having the same File Number and Channel Number), and ignores the next 7 sectors
(which must have other File Number and/or other Channel Number). There are
various ways to arrange multiple files or channels, for example,<br/>
```
  one file with eight 1/8 audio channels
  one file with one 1/8 audio channels, plus one 7/8 video channel (*)
  one file with one 1/8 audio channels, plus 7 unused channels
  eight different files with one 1/8 audio channel each
  etc.
```
(\*) If the Audio and Video data belongs together then both should use the SAME
channel.<br/>
Note: Above interleave values are assuming that PSX Game Disks are always
running at double speed (that's fastest for normal data files, and ADPCM files
are usually using the same speed; otherwise it'd be neccessary to change the
drive speed everytime when switching between Data to ADPCM modes).<br/>
Note: The file/channel numbers can be somehow selected with the Setfilter
command. No idea if the controller is automatically switching to the next
channel or so when reaching the end of the file?<br/>

#### Unused sectors in Interleave
There are different ways to mark unused sectors in interleaved streams. Ace
Combat 3 uses Channel=FFh=Invalid. Tron Bonne uses Submode=00h=Nothing
(notably, that game has a 74Mbyte XA file that leaves about 75% unused).<br/>
```
  Subheader bytes: 01h,FFh,64h,01h   ;Ace Combat 3 Electrosphere
  Subheader bytes: 01h,00h,00h,00h   ;Misadventures of Tron Bonne (XA\*.XA)
```

#### Real Time Streaming
With the above Interleave, files can be played continously at real time - that,
unless read-errors do occur. In that case the drive controller would usually
perform time-consuming error-correction and/or read-retries. For video/audio
streaming the resulting delay would be tendencially more annoying as than
processing or skipping the incorrect data.<br/>
In such cases the drive controller is allowed to ignore read errors; that
probably on sectors that have the Real Time (RT) flag set in their subheaders.
The controller is probably doing some read-ahead buffering (so, if it has
buffered enough data, then it may still perform read retries and/or error
correction, as long as it doesn't affect real time playback).<br/>



##   CDROM XA Audio ADPCM Compression
CD-ROM XA ADPCM is used for Audio data compression. Each 16bit sample is
encoded in 4bit nibbles; so the compression rate is almost 1:4 (only almost 1:4
because there are 16 header bytes within each 128-byte portion). The data is
usually/always stored on 914h-byte sectors (without error correction).<br/>

#### Subheader
The Subheader (see previous chapter) contains important info for ADPCM: The
file/channel numbers for Interleaved data, and the codinginfo flags:
mono/stereo flag, 37800Hz/18900Hz sampling rate, 4bit/8bit format, and
emphasis.<br/>

#### ADPCM Sectors
Each sector consists of 12h 128-byte portions (=900h bytes) (the remaining 14h
bytes of the sectors 914h-byte data region are 00h filled).<br/>
The separate 128-byte portions consist of a 16-byte header,<br/>
```
  00h..03h  Copy of below 4 bytes (at 04h..07h)
  04h       Header for 1st Block/Mono, or 1st Block/Left
  05h       Header for 2nd Block/Mono, or 1st Block/Right
  06h       Header for 3rd Block/Mono, or 2nd Block/Left
  07h       Header for 4th Block/Mono, or 2nd Block/Right
  08h       Header for 5th Block/Mono, or 3rd Block/Left  ;\unknown/unused
  09h       Header for 6th Block/Mono, or 3rd Block/Right ; for 8bit ADPCM
  0Ah       Header for 7th Block/Mono, or 4th Block/Left  ; (maybe 0, or maybe
  0Bh       Header for 8th Block/Mono, or 4th Block/Right ;/copy of above)
  0Ch..0Fh  Copy of above 4 bytes (at 08h..0Bh)
```
followed by twentyeight data words (4x28-bytes),<br/>
```
  10h..13h  1st Data Word (packed 1st samples for 2-8 blocks)
  14h..17h  2nd Data Word (packed 2nd samples for 2-8 blocks)
  18h..1Bh  3rd Data Word (packed 3rd samples for 2-8 blocks)
  ...       Nth Data Word (packed Nth samples for 2-8 blocks)
  7Ch..7Fh  28th Data Word (packed 28th samples for 2-8 blocks)
```
and then followed by the next 128-byte portion.<br/>
The "Copy" bytes are allowing to repair faulty headers (ie. if the CDROM
controller has sensed a read-error in the header then it can eventually replace
it by the copy of the header).<br/>

#### XA-ADPCM Header Bytes
```
  0-3   Shift  (0..12) (0=Loudest) (13..15=Reserved/Same as 9)
  4-5   Filter (0..3) (only four filters, unlike SPU-ADPCM which has five)
  6-7   Unused (should be 0)
```
Note: The 4bit (or 8bit) samples are expanded to 16bit by left-shifting them by
12 (or 8), that 16bit value is then right-shifted by the selected 'shift'
amount. For 8bit ADPCM shift should be 0..8 (values 9..12 will cut-off the
LSB(s) of the 8bit value, this works, but isn't useful). For both 4bit and 8bit
ADPCM, reserved shift values 13..15 will act same as shift=9).<br/>

#### XA-ADPCM Data Words (32bit, little endian)
```
  0-3   Nibble for 1st Block/Mono, or 1st Block/Left  (-8h..+7h)
  4-7   Nibble for 2nd Block/Mono, or 1st Block/Right (-8h..+7h)
  8-11  Nibble for 3rd Block/Mono, or 2nd Block/Left  (-8h..+7h)
  12-15 Nibble for 4th Block/Mono, or 2nd Block/Right (-8h..+7h)
  16-19 Nibble for 5th Block/Mono, or 3rd Block/Left  (-8h..+7h)
  20-23 Nibble for 6th Block/Mono, or 3rd Block/Right (-8h..+7h)
  24-27 Nibble for 7th Block/Mono, or 4th Block/Left  (-8h..+7h)
  28-31 Nibble for 8th Block/Mono, or 4th Block/Right (-8h..+7h)
```
or, for 8bit ADPCM format:<br/>
```
  0-7   Byte for 1st Block/Mono, or 1st Block/Left    (-80h..+7Fh)
  8-15  Byte for 2nd Block/Mono, or 1st Block/Right   (-80h..+7Fh)
  16-23 Byte for 3rd Block/Mono, or 2nd Block/Left    (-80h..+7Fh)
  24-31 Byte for 4th Block/Mono, or 2nd Block/Right   (-80h..+7Fh)
```

#### decode\_sector(src)
```
  src=src+12+4+8   ;skip sync,header,subheader
  for i=0 to 11h
   for blk=0 to 3
    IF stereo ;left-samples (LO-nibbles), plus right-samples (HI-nibbles)
      decode_28_nibbles(src,blk,0,dst_left,old_left,older_left)
      decode_28_nibbles(src,blk,1,dst_right,old_right,older_right)
    ELSE      ;first 28 samples (LO-nibbles), plus next 28 samples (HI-nibbles)
      decode_28_nibbles(src,blk,0,dst_mono,old_mono,older_mono)
      decode_28_nibbles(src,blk,1,dst_mono,old_mono,older_mono)
    ENDIF
   next blk
   src=src+128
  next i
  src=src+14h+4    ;skip padding,edc
```

#### decode\_28\_nibbles(src,blk,nibble,dst,old,older)
```
  shift  = 12 - (src[4+blk*2+nibble] AND 0Fh)
  filter =      (src[4+blk*2+nibble] AND 30h) SHR 4
  f0 = pos_xa_adpcm_table[filter]
  f1 = neg_xa_adpcm_table[filter]
  for j=0 to 27
    t = signed4bit((src[16+blk+j*4] SHR (nibble*4)) AND 0Fh)
    s = (t SHL shift) + ((old*f0 + older*f1+32)/64);
    s = MinMax(s,-8000h,+7FFFh)
    halfword[dst]=s, dst=dst+2, older=old, old=s
  next j
```

#### Pos/neg Tables
```
  pos_xa_adpcm_table[0..4] = (0, +60, +115, +98, +122)
  neg_xa_adpcm_table[0..4] = (0,   0,  -52, -55,  -60)
```
Note: XA-ADPCM supports only four filters (0..3), unlike SPU-ADPCM which
supports five filters (0..4).<br/>

#### Old/Older Values
The incoming old/older values are usually that from the previous part, or
garbage (in case of decoding errors in the previous part), or whatever (in case
there was no previous part) (ie. maybe zero on power-up?) (and maybe there's
also a way to reset the values to zero at the begin of a new file, or \*maybe\*
it's silently done automatically when issuing seek commands?).<br/>

#### 25-point Zigzag Interpolation
The CDROM decoder is applying some weird 25-point zigzag interpolation when
resampling the 37800Hz XA-ADPCM output to 44100Hz. This part is different from
SPU-ADPCM (which uses 4-point gaussian pitch interpolations). For example,
XA-ADPCM interpolation applied to a square wave looks like this:<br/>
```
                                                 .            .
           .--------------.                      | |        | |
           |              |                     .'.'.'----'.'.'.
           |              |                     | |          | |
           |              |                     |              |
           | Decompressed |                     |    Final     |
           |   XA-ADPCM   |                     |   XA-ADPCM   |
           |   Waveform   |                     |    Output    |
           |              |                   | |              | |
           |              |             ---.'.'.'              '.'.'.---
   --------'              '--------          | |                | |
                                               '                '
```
The zigzagging does produce some (inaudible) 22050Hz noise, and does produce
some low-pass (?) filtering ("sinc filter"). The effect can be reproduced
somewhat like so:<br/>
```
<B>  Output37800Hz(sample):</B>
    ringbuf[p AND 1Fh]=sample, p=p+1, sixstep=sixstep-1
    if sixstep=0
      sixstep=6
      Ouput44100Hz(ZigZagInterpolate(p,Table1))
      Ouput44100Hz(ZigZagInterpolate(p,Table2))
      Ouput44100Hz(ZigZagInterpolate(p,Table3))
      Ouput44100Hz(ZigZagInterpolate(p,Table4))
      Ouput44100Hz(ZigZagInterpolate(p,Table5))
      Ouput44100Hz(ZigZagInterpolate(p,Table6))
      Ouput44100Hz(ZigZagInterpolate(p,Table7))
    endif
<B>  ZigZagInterpolate(p,TableX):</B>
    sum=0
    for i=1 to 29, sum=sum+(ringbuf[(p-i) AND 1Fh]*TableX[i])/8000h, next i
    return MinMax(sum,-8000h,+7FFFh)
<B>  Table1, Table2, Table3, Table4, Table5, Table6, Table7  ;Index</B>
    0     , 0     , 0     , 0     , -0001h, +0002h, -0005h  ;1
    0     , 0     , 0     , -0001h, +0003h, -0008h, +0011h  ;2
    0     , 0     , -0001h, +0003h, -0008h, +0010h, -0023h  ;3
    0     , -0002h, +0003h, -0008h, +0011h, -0023h, +0046h  ;4
    0     , 0     , -0002h, +0006h, -0010h, +002Bh, -0017h  ;5
    -0002h, +0003h, -0005h, +0005h, +000Ah, +001Ah, -0044h  ;6
    +000Ah, -0013h, +001Fh, -001Bh, +006Bh, -00EBh, +015Bh  ;7
    -0022h, +003Ch, -004Ah, +00A6h, -016Dh, +027Bh, -0347h  ;8
    +0041h, -004Bh, +00B3h, -01A8h, +0350h, -0548h, +080Eh  ;9
    -0054h, +00A2h, -0192h, +0372h, -0623h, +0AFAh, -1249h  ;10
    +0034h, -00E3h, +02B1h, -05BFh, +0BCDh, -16FAh, +3C07h  ;11
    +0009h, +0132h, -039Eh, +09B8h, -1780h, +53E0h, +53E0h  ;12
    -010Ah, -0043h, +04F8h, -11B4h, +6794h, +3C07h, -16FAh  ;13
    +0400h, -0267h, -05A6h, +74BBh, +234Ch, -1249h, +0AFAh  ;14
    -0A78h, +0C9Dh, +7939h, +0C9Dh, -0A78h, +080Eh, -0548h  ;15
    +234Ch, +74BBh, -05A6h, -0267h, +0400h, -0347h, +027Bh  ;16
    +6794h, -11B4h, +04F8h, -0043h, -010Ah, +015Bh, -00EBh  ;17
    -1780h, +09B8h, -039Eh, +0132h, +0009h, -0044h, +001Ah  ;18
    +0BCDh, -05BFh, +02B1h, -00E3h, +0034h, -0017h, +002Bh  ;19
    -0623h, +0372h, -0192h, +00A2h, -0054h, +0046h, -0023h  ;20
    +0350h, -01A8h, +00B3h, -004Bh, +0041h, -0023h, +0010h  ;21
    -016Dh, +00A6h, -004Ah, +003Ch, -0022h, +0011h, -0008h  ;22
    +006Bh, -001Bh, +001Fh, -0013h, +000Ah, -0005h, +0002h  ;23
    +000Ah, +0005h, -0005h, +0003h, -0001h, 0     , 0       ;24
    -0010h, +0006h, -0002h, 0     , 0     , 0     , 0       ;25
    +0011h, -0008h, +0003h, -0002h, +0001h, 0     , 0       ;26
    -0008h, +0003h, -0001h, 0     , 0     , 0     , 0       ;27
    +0003h, -0001h, 0     , 0     , 0     , 0     , 0       ;28
    -0001h, 0     , 0     , 0     , 0     , 0     , 0       ;29
```
The above formula/table gives nearly correct results, but with small rounding
errors in some cases - possibly due to actual rounding issues, or due to
factors with bigger fractional portions, or due to a completely different
formula...<br/>
Probably, the hardware does actually do the above stuff in two steps: first,
applying a zig-zag filter (with only around 21-points) to the 37800Hz output,
and then doing 44100Hz interpolation (2-point linear or 4-point gaussian or
whatever) in a second step.<br/>
That two-step theory would also match well for 18900Hz resampling (which has
lower-pitch zigzag, and gets spread across about fifty 44100Hz samples).<br/>

#### XA-ADPCM Emphasis
With XA-Emphasis enabled in Sub-header, output will appear as so:<br/>
```
           .------------.                           ....-----.
           |            |                        .''         |
           |    Raw     |                       .'    XA     |
           |   ADPCM    |                       |  Emphasis  '.
           |  Waveform  |                       |   Output    '..
   --------'            '----------     --------'                ''''---
```
The exact XA-Emphasis formula is unknown (maybe it's just same as for CD-DA's
SUBQ emphasis). Additionally, zig-zag interpolation is applied (somewhere
before or after applying the emphasis stuff).<br/>
Note: The Emphasis feature isn't used by any known PSX games.<br/>

#### Uninitialized Six-step Counter
The hardware does contain some six-step counter (for interpolating 37800Hz to
44100Hz, ie. to insert one extra sample after each six samples). The 900h-byte
sectors contain a multiple of six samples, so the counter will be always same
before & after playing a sector. However, the initial counter value on
power-up is uninitialized random (and the counter will fallback to that initial
random setting after each 900h-byte sector).<br/>

#### RIFF Headers (on PCs)
When reading files that consist of 914h-byte sectors on a PC, the PC seems to
automatically insert a 2Ch-byte RIFF fileheader. Like so, for ADPCM audio
files:<br/>
```
  00h 4   "RIFF"
  04h 4   Total Filesize (minus 8)
  08h 8   "CDXAfmt "
  10h 4   Size of below stuff (10h)
  14h 14  Stuff (looks like the "LEN_SU" region from XA-Directory Record)
  22h 2   Zero  (probably just dummy padding for 32bit alignment)
  24h 4   "data"
  28h 4   Size of following data (usually N*930h)
```
That RIFF stuff isn't stored on the CDROM (at least not in the file area)
(however, some of that info, like the "=UXA" stuff, is stored in the directory
area of the CDROM).<br/>
After the RIFF header, the normal sector data is appended, that, with the full
930h bytes per sector (ie. the 914h data bytes preceeded by sync bytes, header,
subheader, and followed by the EDC value).<br/>
The Channel Interleave doesn't seem to be resolved, ie. the Channels are kept
arranged as how they are stored on the CDROM. However, File Interleave
\<should\> be resolved, ie. other Files that "overlap" the file shouldn't
be included in the file.<br/>



##   CDROM ISO Volume Descriptors
#### System Area (prior to Volume Descriptors)
The first 16 sectors on the first track are the system area, for a Playstation
disk, it contains the following:<br/>
```
  Sector 0..3   - Zerofilled (Mode2/Form1, 4x800h bytes, plus ECC/EDC)
  Sector 4      - Licence String
  Sector 5..11  - Playstation Logo (3278h bytes) (remaining bytes FFh-filled)
  Sector 12..15 - Zerofilled (Mode2/Form2, 4x914h bytes, plus EDC)
```
Of which, the Licence String in sector 4 is,<br/>
```
  000h 32    Line 1      ("          Licensed  by          ")
  020h 32+6  Line 2 (EU) ("Sony Computer Entertainment Euro"," pe   ") ;\either
  020h 32+1  Line 2 (JP) ("Sony Computer Entertainment Inc.",0Ah)      ; one of
  020h 32+6  Line 2 (US) ("Sony Computer Entertainment Amer","  ica ") ;/these
  041h 1983  Empty (JP)    (filled by repeating pattern 62x30h,1x0Ah, 1x30h)
  046h 1978  Empty (EU/US) (filled by 00h-bytes)
```
The Playstation Logo in sectors 5..11 contains data like so,<br/>
```
  0000h ..   41h,00h,00h,00h,00h,00h,00h,00h,01h,00h,00h,00h,1Ch,23h,00h,00h
  0010h ..   51h,01h,00h,00h,A4h,2Dh,00h,00h,99h,00h,00h,00h,1Ch,00h,00h,00h
  0020h ..   ...
  3278h 588h FF-filled (remaining bytes on sector 11)
```
the Logo contains a .TMD header, polygons, vertices and normals for the "PS"
logo (which is displayed when booting from CDROM). Some BIOS versions are
comparing these 3278h bytes against an identical copy in ROM, and refuse to
boot if the data isn't 1:1 the same:<br/>
- NTSC US/ASIA BIOS always accepts changed logos.<br/>
- PAL  EU BIOS accepts changed logos up to v3.0E (and refuses in v4.0E and up).<br/>
- NTSC JP BIOS never accepts changed logos (and/or changed license strings?).<br/>
Note: A region-patch-modchip causes PAL BIOS to behave same as US/ASIA BIOS.<br/>

#### Volume Descriptors (Sector 16 and up)
Playstation disks usually have only two Volume Descriptors,<br/>
```
  Sector 16    - Primary Volume Descriptor
  Sector 17    - Volume Descriptor Set Terminator
```

#### Primary Volume Descriptor (sector 16 on PSX disks)
```
  000h 1    Volume Descriptor Type        (01h=Primary Volume Descriptor)
  001h 5    Standard Identifier           ("CD001")
  006h 1    Volume Descriptor Version     (01h=Standard)
  007h 1    Reserved                      (00h)
  008h 32   System Identifier             (a-characters) ("PLAYSTATION")
  028h 32   Volume Identifier             (d-characters) (max 8 chars for PSX?)
  048h 8    Reserved                      (00h)
  050h 8    Volume Space Size             (2x32bit, number of logical blocks)
  058h 32   Reserved                      (00h)
  078h 4    Volume Set Size               (2x16bit) (usually 0001h)
  07Ch 4    Volume Sequence Number        (2x16bit) (usually 0001h)
  080h 4    Logical Block Size in Bytes   (2x16bit) (usually 0800h) (1 sector)
  084h 8    Path Table Size in Bytes      (2x32bit) (max 800h for PSX)
  08Ch 4    Path Table 1 Block Number     (32bit little-endian)
  090h 4    Path Table 2 Block Number     (32bit little-endian) (or 0=None)
  094h 4    Path Table 3 Block Number     (32bit big-endian)
  098h 4    Path Table 4 Block Number     (32bit big-endian) (or 0=None)
  09Ch 34   Root Directory Record         (see next chapter)
  0BEh 128  Volume Set Identifier         (d-characters) (usually empty)
  13Eh 128  Publisher Identifier          (a-characters) (company name)
  1BEh 128  Data Preparer Identifier      (a-characters) (empty or other)
  23Eh 128  Application Identifier        (a-characters) ("PLAYSTATION")
  2BEh 37   Copyright Filename            ("FILENAME.EXT;VER") (empty or text)
  2E3h 37   Abstract Filename             ("FILENAME.EXT;VER") (empty)
  308h 37   Bibliographic Filename        ("FILENAME.EXT;VER") (empty)
  32Dh 17   Volume Creation Timestamp     ("YYYYMMDDHHMMSSFF",timezone)
  33Eh 17   Volume Modification Timestamp ("0000000000000000",00h)
  34Fh 17   Volume Expiration Timestamp   ("0000000000000000",00h)
  360h 17   Volume Effective Timestamp    ("0000000000000000",00h)
  371h 1    File Structure Version        (01h=Standard)
  372h 1    Reserved for future           (00h-filled)
  373h 141  Application Use Area          (00h-filled for PSX and VCD)
  400h 8    CD-XA Identifying Signature   ("CD-XA001" for PSX and VCD)
  408h 2    CD-XA Flags (unknown purpose) (00h-filled for PSX and VCD)
  40Ah 8    CD-XA Startup Directory       (00h-filled for PSX and VCD)
  412h 8    CD-XA Reserved                (00h-filled for PSX and VCD)
  41Ah 345  Application Use Area          (00h-filled for PSX and VCD)
  573h 653  Reserved for future           (00h-filled)
```

#### Volume Descriptor Set Terminator (sector 17 on PSX disks)
```
  000h 1    Volume Descriptor Type    (FFh=Terminator)
  001h 5    Standard Identifier       ("CD001")
  006h 1    Terminator Version        (01h=Standard)
  007h 2041 Reserved                  (00h-filled)
```

#### Boot Record (none such on PSX disks)
```
  000h 1    Volume Descriptor Type    (00h=Boot Record)
  001h 5    Standard Identifier       ("CD001")
  006h 1    Boot Record Version       (01h=Standard)
  007h 32   Boot System Identifier    (a-characters)
  027h 32   Boot Identifier           (a-characters)
  047h 1977 Boot System Use           (not specified content)
```

#### Supplementary Volume Descriptor (none such on PSX disks)
```
  000h 1    Volume Descriptor Type (02h=Supplementary Volume Descriptor)
  001h ..   Same as for Primary Volume Descriptor (see there)
  007h 1    Volume Flags           (8bit)
  008h ..   Same as for Primary Volume Descriptor (see there)
  058h 32   Escape Sequences       (32 bytes)
  078h ..   Same as for Primary Volume Descriptor (see there)
```
In practice, this is used for Joliet:<br/>
[CDROM Extension Joliet](cdromformat.md#cdrom-extension-joliet)<br/>

#### Volume Partition Descriptor (none such on PSX disks)
```
  000h 1    Volume Descriptor Type      (03h=Volume Partition Descriptor)
  001h 5    Standard Identifier         ("CD001")
  006h 1    Volume Partition Version    (01h=Standard)
  007h 1    Reserved                    (00h)
  008h 32   System Identifier           (a-characters) (32 bytes)
  028h 32   Volume Partition Identifier (d-characters) (32 bytes)
  048h 8    Volume Partition Location   (2x32bit) Logical Block Number
  050h 8    Volume Partition Size       (2x32bit) Number of Logical Blocks
  058h 1960 System Use                  (not specified content)
```

#### Reserved Volume Descriptors (none such on PSX disks)
```
  000h 1    Volume Descriptor Type    (04h..FEh=Reserved, don't use)
  001h 2047 Reserved                  (don't use)
```



##   CDROM ISO File and Directory Descriptors
The location of the Root Directory is described by a 34-byte Directory Record
being located in Primary Volume Descriptor entries 09Ch..0BDh. The data therein
is: Block Number (usually 22 on PSX disks), LEN\_FI=01h, Name=00h, and,
LEN\_SU=00h (due to the 34-byte limit).<br/>

#### Format of a Directory Record
```
  00h 1      Length of Directory Record (LEN_DR) (33+LEN_FI+pad+LEN_SU) (0=Pad)
  01h 1      Extended Attribute Record Length (usually 00h)
  02h 8      Data Logical Block Number (2x32bit)
  0Ah 8      Data Size in Bytes        (2x32bit)
  12h 7      Recording Timestamp       (yy-1900,mm,dd,hh,mm,ss,timezone)
  19h 1      File Flags 8 bits         (usually 00h=File, or 02h=Directory)
  1Ah 1      File Unit Size            (usually 00h)
  1Bh 1      Interleave Gap Size       (usually 00h)
  1Ch 4      Volume Sequence Number    (2x16bit, usually 0001h)
  20h 1      Length of Name            (LEN_FI)
  21h LEN_FI File/Directory Name ("FILENAME.EXT;1" or "DIR_NAME" or 00h or 01h)
  xxh 0..1   Padding Field (00h) (only if LEN_FI is even)
  xxh LEN_SU System Use (LEN_SU bytes) (see below for CD-XA disks)
```
LEN\_SU can be calculated as "LEN\_DR-(33+LEN\_FI+Padding)". For CD-XA disks (as
used in the PSX), LEN\_SU is 14 bytes:<br/>
```
  00h 2      Owner ID Group  (whatever, usually 0000h, big endian)
  02h 2      Owner ID User   (whatever, usually 0000h, big endian)
  04h 2      File Attributes (big endian):
               0   Owner Read    (usually 1)
               1   Reserved      (0)
               2   Owner Execute (usually 1)
               3   Reserved      (0)
               4   Group Read    (usually 1)
               5   Reserved      (0)
               6   Group Execute (usually 1)
               7   Reserved      (0)
               8   World Read    (usually 1)
               9   Reserved      (0)
               10  World Execute (usually 1)
               11  IS_MODE2        (0=MODE1 or CD-DA, 1=MODE2)
               12  IS_MODE2_FORM2  (0=FORM1, 1=FORM2)
               13  IS_INTERLEAVED  (0=No, 1=Yes...?) (by file and/or channel?)
               14  IS_CDDA         (0=Data or ADPCM, 1=CD-DA Audio Track)
               15  IS_DIRECTORY    (0=File or CD-DA, 1=Directory Record)
             Commonly used Attributes are:
               0D55h=Normal Binary File (with 800h-byte sectors)
               1555h=Uncommon           (fade to black .DPS and .XA files)
               2555h=Uncommon           (wipeout .AV files) (MODE1 ??)
               4555h=CD-DA Audio Track  (wipeout .SWP files, alone .WAV file)
               3D55h=Streaming File     (ADPCM and/or MDEC or so)
               8D55h=Directory Record   (parent-, current-, or sub-directory)
  06h 2      Signature     ("XA")
  08h 1      File Number   (Must match Subheader's File Number)
  09h 5      Reserved      (00h-filled)
```
Directory sectors do usually have zeropadding at the end of each sector:<br/>
```
  - Directory sizes are always rounded up to N*800h-bytes.
  - Directory entries should not cross 800h-byte sector boundaries.
  There may be further directory entries on the next sector after the padding.
  To deal with that, skip 00h-bytes until finding a nonzero LEN_DR value (or
  slightly faster, upon a 00h-byte, directly jump to next sector instead of
  doing a slow byte-by-byte skip).
  Note: Padding between sectors does rarely happen on PSX discs because the
  PSX kernel supports max 800h bytes per directory (one exception is PSX Hot
  Shots Golf 2, which has an ISO directory with more than 800h bytes; it does
  use a lookup file instead of actually parsing the while ISO directory).
```
Names are alphabetically sorted, no matter if the names refer to files or
directories (ie. SUBDIR would be inserted between STRFILE.EXT and SYSFILE.EXT).
The first two entries (with non-ascii names 00h and 01h) are referring to
current and parent directory.<br/>

#### Path Tables
The Path Table contain a summary of the directory names (the same information
is also stored in the directory records, so programs may either use path tables
or directory records; the path tables are allowing to read the whole directory
tree quickly at once, without neeeding to seek from directory to directory).<br/>
Path Table 1 is in Little-Endian format, Path Table 3 contains the same data in
Big-Endian format. Path Table 2 and 4 are optional copies of Table 1 and 3. The
size and location of the tables is stored in Volume Descriptor entries
084h..09Bh. The format of the separate entries within a Path Table is,<br/>
```
  00h 1       Length of Directory Name (LEN_DI) (01h..08h for PSX)
  01h 1       Extended Attribute Record Length  (usually 00h)
  02h 4       Directory Logical Block Number
  06h 2       Parent Directory Number           (0001h and up)
  08h LEN_DI  Directory Name (d-characters, d1-characters) (or 00h for Root)
  xxh 0..1    Padding Field (00h) (only if LEN_FI is odd)
```
The first entry (directory number 0001h) is the root directory, the root
doesn't have a name, nor a parent (the name field contains a 00h byte, rather
than ASCII text, LEN\_DI is 01h, and parent is 0001h, making the root it's own
parent; ignoring the fact that incest is forbidden in many countries).<br/>
The next entries (directory number 0002h and up) (if any) are sub-directories
within the root (sorted in alphabetical order, and all having parent=0001h).
The next entries are sub-directories (if any) of the first sub-directory (also
sorted in alphabetical order, and all having parent=0002h). And so on.<br/>
PSX disks usually contain all four tables (usually on sectors 18,19,20,21).<br/>

#### Format of an Extended Attribute Record (none such on PSX disks)
If present, an Extended Attribute Record shall be recorded over at least one
Logical Block. It shall have the following contents.<br/>
```
  00h 4       Owner Identification (numerical value)  ;\used only if
  04h 4       Group Identification (numerical value)  ; File Flags Bit4=1
  08h 2       Permission Flags (16bit, little-endian) ;/
  0Ah 17      File Creation Timestamp      ("YYYYMMDDHHMMSSFF",timezone)
  1Bh 17      File Modification Timestamp  ("0000000000000000",00h)
  2Ch 17      File Expiration Timestamp    ("0000000000000000",00h)
  3Dh 17      File Effective Timestamp     ("0000000000000000",00h)
  4Eh 1       Record Format                (numerical value)
  4Fh 1       Record Attributes            (numerical value)
  50h 4       Record Length                (numerical value)
  54h 32      System Identifier            (a-characters, a1-characters)
  74h 64      System Use                   (not specified content)
  B4h 1       Extended Attribute Record Version (numerical value)
  B5h 1       Length of Escape Sequences   (LEN_ESC)
  B6h 64      Reserved for future standardization (00h-filled)
  F6h 4       Length of Application Use    (LEN_AU)
  FAh LEN_AU  Application Use
  xxh LEN_ESC Escape Sequences
```
Unknown WHERE that data is located... the Directory Records can specify the
Extended Attribute Length, but not the location... maybe it's meant to be
located in the first some bytes or blocks of the File or Directory...?<br/>



##   CDROM ISO Misc
#### Both Byte Order
All 16bit and 32bit numbers in the ISO region are stored twice, once in
Little-Endian order, and then in Big-Endian Order. For example,<br/>
```
  2x16bit value 1234h     ---> stored as 34h,12h,12h,34h
  2x32bit value 12345678h ---> stored as 78h,56h,34h,12h,12h,34h,56h,78h
```
Exceptions are the 16bit Permission Flags which are stored only in
Little-Endian format (although the flags are four 4bit groups, so that isn't a
real 16bit number), and, the Path Tables are stored in both formats, but
separately, ie. one table contains only Little-Endian numbers, and the other
only Big-Endian numbers.<br/>

#### d-characters (Filenames)
```
  "0..9", "A..Z", and "_"
```

#### a-characters
```
  "0..9", "A..Z", SPACE, "!"%&'()*+,-./:;<=>?_"
```
Ie. all ASCII characters from 20h..5Fh except "#$@[\]^"<br/>

SEPARATOR 1 = 2Eh (aka ".") (extension; eg. "EXT")<br/>
SEPARATOR 2 = 3Bh (aka ";") (file version; "1".."32767")<br/>

#### Fixed Length Strings/Filenames
The Volume Descriptors contain a number fixed-length string/filename fields
(unlike the Directory Records and Path Tables which have variable lengths).
These fields should be padded with SPACE characters if they are empty, or if
the string is shorter than the maximum length.<br/>
Filename fields in Volume Descriptors are referring to files in the Root
Directory. On PSX disks, the filename fields are usually empty, but some disks
are mis-using the Copyright Filename to store the Company Name (although no
such file exists on the disk).<br/>

#### Volume Descriptor Timestamps
The various timestamps occupy 17 bytes each, in form of<br/>
```
  "YYYYMMDDHHMMSSFF",timezone
  "0000000000000000",00h         ;empty timestamp
```
The first 16 bytes are ASCII Date and Time digits (Year, Month, Day, Hour,
Minute, Second, and 1/100 Seconds. The last byte is Offset from Greenwich Mean
Time in number of 15-minute steps from -48 (West) to +52 (East); or actually:
to +56 when recursing Kiribati's new timezone.<br/>
Note: PSX games manufactured in year 2000 were accidently marked to be created
in year 0000.<br/>

#### Recording Timestamps
Occupy only 7 bytes, in non-ascii format<br/>
```
  year-1900,month,day,hour,minute,second,timezone
  00h,00h,00h,00h,00h,00h,00h    ;empty timestamp
```
The year ranges from 1900+0 to 1900+255.<br/>

#### File Flags
If this Directory Record identifies a directory then bit 2,3,7 shall be set to
ZERO.<br/>
If no Extended Attribute Record is associated with the File Section identified
by this Directory Record then bit positions 3 and 4 shall be set to ZERO.<br/>
```
  0  Existence       (0=Normal, 1=Hidden)
  1  Directory       (0=File, 1=Directory)
  2  Associated File (0=Not an Associated File, 1=Associated File)
  3  Record
        If set to ZERO, shall mean that the structure of the information in
        the file is not specified by the Record Format field of any associated
        Extended Attribute Record (see 9.5.8).
        If set to ONE, shall mean that the structure of the information in
        the file has a record format specified by a number other than zero in
        the Record Format Field of the Extended Attribute Record (see 9.5.8).
  4  Restrictions    (0=None, 1=Restricted via Permission Flags)
  5  Reserved        (0)
  6  Reserved        (0)
  7  Multi-Extent    (0=Final Directory Record for the file, 1=Not final)
```

#### Permission Flags (in Extended Attribute Records)
```
  0-3   Permissions for upper-class owners
  4-7   Permissions for normal owners
  8-11  Permissions for upper-class users
  12-15 Permissions for normal users
```
This is a bit bizarre, an upper-class owner is "an owner who is a member of a
group of the System class of user". An upper-class user is "any user who is a
member of the group specified by the Group Identification field". The separate
4bit permission codes are:<br/>
```
  Bit0  Permission to read the file    (0=Yes, 1=No)
  Bit1  Must be set (1)
  Bit2  Permission to execute the file (0=Yes, 1=No)
  Bit3  Must be set (1)
```



##   CDROM Extension Joliet
#### Typical Joliet Disc Header
The discs contains two separate filesystems, the ISO one for backwards
compatibilty, and the Joliet one with longer filenames and Unicode characters.<br/>
```
  Sector 16 - Primary Volume Descriptor (with 8bit uppercase ASCII ISO names)
  Sector 17 - Secondary Volume Descriptor (with 16bit Unicode Joliet names)
  Sector 18 - Volume Descriptor Set Terminator
  Sector .. - Path Tables and Directory Records (for ISO)
  Sector .. - Path Tables and Directory Records (for Joliet)
  Sector .. - File Data Sectors (shared for ISO and Joliet)
```
There is no way to determine which ISO name belongs to which Joliet name
(except, filenames do usually point to the same file data sectors, but that
doesn't work for empty files, and doesn't work for folder names).<br/>
The ISO names can be max 31 chars (or shorter for compatibility with DOS short
names: Nero does truncate them to max 14 chars "FILENAME.EXT;1", all uppercase,
with underscores instead of spaces, and somehow assigning names like
"FILENAMx.EXT;1" in case of duplicated short names).<br/>

#### Secondary Volume Descriptor (aka Supplementary Volume Descriptor)
This is using the same format as ISO Primary Volume Descriptor (but with some
changed entries).<br/>
[CDROM ISO Volume Descriptors](cdromformat.md#cdrom-iso-volume-descriptors)<br/>
Changed entries are:<br/>
```
  000h 1     Volume Descriptor Type (02h=Supplementary instead of 01h=Primary)
  007h 1     Volume Flags           (whatever, instead of Reserved)
  008h 2x32  Identifier Strings     (16-char Unicode instead 32-char ASCII)
  058h 32    Escape Sequences       (see below, instead of Reserved)
  08Ch 4x4   Path Tables            (point to new tables with Unicode chars)
  09Ch 34    Root Directory Record  (point to root with Unicode chars)
  0BEh 4x128 Identifier Strings     (64-char Unicode instead 128-char ASCII)
  2BEh 3x37  Filename Strings       (18-char Unicode instead 37-char ASCII)
```
The Escape Sequences entry contains three ASCII chars (plus 29-byte
zeropadding), indicating the ISO 2022 Unicode charset:<br/>
```
  %/@   UCS-2 Level 1
  %/C   UCS-2 Level 2
  %/E   UCS-2 Level 3
```

#### Directory Records and Path Tables
This is using the standard ISO format (but with 16bit Unicode characters
instead of 8bit ASCII chars).<br/>
[CDROM ISO File and Directory Descriptors](cdromformat.md#cdrom-iso-file-and-directory-descriptors)<br/>

#### File and Directory Name Characters
All characters are stored in 16bit Big Endian format. The LEN\_FI filename entry
contains the length in bytes (ie. numchars\*2). Charaters 0000h/0001h are
current/parent directory. Characters 0020h and up can be used for
file/directory names, except six reserved characters: \*/:;?\<br/>
All names must be sorted by their character numbers, padded with zero (without
attempting to merge uppercase, lowercase, or umlauts to nearby locations).<br/>

#### File and Directory Name Length
```
  max 64 chars according to original Joliet specs from 1995
  max 110 chars (on standard CDROMs, with LEN_SU=0)
  max 103 chars (on CD-XA discs, with LEN_SU=14)
```
Joliet Filenames include ISO-style version suffices (usually ";1", so the
actual filename lengths are two chars less than shown above).<br/>
The original 64-char limit was perhaps intended to leave space for future
extensions in the LEN\_SU region. The 64-char limit can cause problems with
verbose names (eg. "Interprete - Title (version).mp3"). Microsoft later changed
the limit to up to 110 chars.<br/>
The 110/103-char limit is caused by the 8bit "LEN\_DR=(33+LEN\_FI+pad+LEN\_SU)"
entry in the Directory Records.<br/>
Joliet allows to exceed the 8-level ISO directory nesting limit, however, it
doesn't allow to exceed the 240-byte (120-Unicode-char) limit in ISO 9660
section 6.8.2.1 for the total "path\filename" lengths.<br/>

#### Official Specs
Joliet Specification, CD-ROM Recording Spec ISO 9660:1988, Extensions for
Unicode Version 1; May 22, 1995, Copyright 1995, Microsoft Corporation<br/>
```
  http://littlesvr.ca/isomaster/resources/JolietSpecification.html
```



##   CDROM Protection - SCEx Strings
#### SCEx String
The heart of the PSX copy-protection is the four-letter "SCEx" string, encoded
in the wobble signal of original PSX disks, which cannot be reproduced by
normal CD writers. The last letter varies depending on the region:<br/>
```
  "SCEI" for Japan
  "SCEA" for America (and all other NTSC countries except Japan)
  "SCEE" for Europe (and all other PAL countries like Australia)
```
If the string is missing (or if it doesn't match up for the local region) then
the PSX refuses to boot. The verification is done by the Firmware inside of the
CDROM Controller (not by the PSX BIOS, so there's no way to bypass it by
patching the BIOS ROM chip).<br/>

#### Wobble Groove and Absolute Time in Pregroove (ATIP) on CD-R's
A "blank" CDR contains a pre-formatted spiral on it. The number of windings in
the spiral varies depending on the number of minutes that can be recorded on
the disk. The spiral isn't made of a straight line (------), but rather a
wobbled line (/\/\/\), which is used to adjust the rotation speed during
recording; at normal drive speed, wobble should produce a 22050Hz sine wave.<br/>
Additionally, the CDR wobble is modulated to provide ATIP information, ATIP is
used for locating and positioning during recording, and contains information
about the approximate laser power necessary for recording, the last possible
time location that lead out can start, and the disc application code.<br/>
Wobble is commonly used only on (recordable) CDRs, ie. usually NOT on
(readonly) CDROMs and Audio Disks. The copyprotected PSX CDROMs are having a
short CDR-style wobble period in the first some seconds, which seems to contain
the "SCEx" string instead of ATIP information.<br/>

#### Other Protections
Aside from the SCEx string, PSX disks are required to contain region and
licence strings (in the ISO System Area, and in the .EXE file headers), and the
"PS" logo (in the System Area, too). This data can be reproduced with normal CD
writers, although it may be illegal to distribute unlicensed disks with licence
strings.<br/>



##   CDROM Protection - Bypassing it
#### Modchips
A modchip is a small microcontroller which injects the "SCEx" signal to the
mainboard, so the PSX can be booted even from CDRs which don't contain the
"SCEx" string. Some modchips are additionally patching region checks contained
in the BIOS ROM.<br/>
Note: Although regular PSX disks are black, the hardware doesn't verify the
color of the disks, and works also with normal silver disks.<br/>

#### Disk-Swap-Trick
Once when the PSX has recognized a disk with the "SCEx" signal, it'll be
satisfied until a new disk is inserted, which is sensed by the SHELL\_OPEN
switch. When having that switch blocked, it is possible to insert a CDR without
the PSX noticing that the disk was changed.<br/>
Additionally, the trick requires some boot software that stops the drive motor
(so the new disk can be inserted, despite of the PSX thinking that the drive
door is still closed), and that does then start the boot executable on the new
disk.<br/>
The boot software can be stored on a special boot-disk (that do have the "SCEx"
string on it). Alternately, a regular PSX game disk could be used, with the
boot software stored somewhere else (eg. on Expansion ROM, or BIOS ROM
replacement, or Memory Card).<br/>

#### Booting via BIOS ROM or Expansion ROM
The PSX can be quite easily booted via Expansion ROM, or BIOS ROM replacements,
allowing to execute code that is stored in the ROM, or that is received via
whatever serial or parallel cable connection from a PC.<br/>
However, even with a BIOS replacement, the protection in the CDROM controller
is still active, so the ROM can't read "clean" data from the CDROM Drive
(unless the Disk-Swap trick is used).<br/>
Whereas, no "clean" data doens't mean no data at all. The CDROM controller does
still seem to output "raw" data (without removing the sector header, and
without handling error correction, and with only limited accuracy on the sector
position). So, eventually, a customized BIOS could convert the "raw" data to
"clean" data.<br/>

#### Secret Unlock Commands
There is an "official" backdoor that allows to disable the SCEx protection by
software via secret commands (for example, sending those commands can be done
via BIOS patches, nocash BIOS clone, or Expansion ROMs).<br/>
[CDROM - Secret Unlock Commands](cdromdrive.md#cdrom-secret-unlock-commands)<br/>

#### Booting via Memory Card
Some games that load data from memory cards may get confused if the save data
isn't formatted as how they expect it - with some fine tuning you can get them
to "crash" in a manner that they do accidently execute bootcode stored on the
memory card. This is how tonyhax's game exploits and FreePSXBoot's BIOS shell
exploit work.<br/>
Requires a tools to write to the memory card (eg. parallel port cable), and the
memory card data customized for a specific game, and an original CDROM with
that specific game. Once when the memory card code is booted, the Disk-Swap
trick can be used.<br/>



##   CDROM Protection - Modchips
#### Modchip Source Code
The Old Crow mod chip source code works like so:<br/>
```
  entrypoint:                   ;at power_up
    gate=input/highz
    data=input/highz
    wait 50 ms
    data=output/low
    wait 850 ms
    gate=output/low
    wait 314 ms
  loop:
    wait 72 ms                  ;pause (eighteen "1=low" bits)
    sendbyte("S")               ;1st letter
    sendbyte("C")               ;2nd letter
    sendbyte("E")               ;3rd letter
    sendbyte(...)               ;4th letter (A, E, or I, depending on region)
    goto loop
  sendbyte(char):
    sendbit(0)                  ;one start bit (0=highz)
    for i=0 to 7
      sendbit(char AND 1)       ;output data (LSB first)
      char=char/2
    next i
    sendbit(1)                  ;1st stop bit (1=low)
    sendbit(1)                  ;2nd stop bit (1=low)
    return
  sendbit(bit):
    if bit=1 then data=output/low elseif bit=0 then data=input/highz
    wait 4 ms           ;4ms per bit = 250 bits per second
    return
```
That is, 62 bits per transfer at 250bps = circa 4 transfers per second.<br/>

#### Connection for the data/gate/sync signals:
For older PSX boards (data/gate):<br/>
```
  Board        data             gate
  PU-xx        unknown?         unknown?        ;older PSX boards
```
For newer PSX and PSone boards (data/sync):<br/>
```
  Board        data             sync
  PU-23, PM-41 CXD2938Q.Pin42   CXD2938Q.Pin5   ;newer PSX and older PSone
  PM-41(2)     CXD2941R.Pin36   CXD2941R.Pin76  ;newer PSone boards
```
On the mainboard should be a big SMD capacitor (connected to the "data" pin),
and a big testpoint (connected to the "sync" pin); it's easier to connect the
signals to that locations than to the tiny CXD-chip pins.<br/>
gate and data must be tristate outputs, or open-collector outputs (or normal
high/low outputs passed through a diode).<br/>

#### Note on "data" pin (all boards)
Transfers the "SCEx" data. Note that the signal produced by the modchip is
looking entirly different than the signal produced by original disks, the real
signal would be modulated 22050Hz wobble, while the modchip is simply dragging
the signal permanently LOW throughout "1" bits, and leaves it floating for "0"
bits. Anyways the "faked" signal seems to be accurate enough to work.<br/>

#### Note on "gate" pin (older PSX boards only)
The "gate" pin needs to be LOW only for use with original licensed disks
(reportedly otherwise the SCEx string on that disks would conflict with the
SCEx string from the modchip).<br/>
At the mainboard side, the "gate" signal is an input, and "data" is an inverted
output of the gate signal (so dragging gate to low, would cause data to go
high).<br/>

#### Note on "sync" pin (newer PSX and PSone boards only)
The "sync" pin is a testpoint on the mainboard, which does (at single speed)
output a frequency of circa 44.1kHz/6 (of which some clock pulses seem to be
longer or shorter, probably to indicate adjustments to the rotation speed).<br/>
Some modchips are connected directly to "sync" (so they are apparently
synchronizing the data output with that signal; which is not implemented in the
above source code).<br/>
Anyways, other modchips are using a more simplified connection: The modchip
itself connects only to the "data" pin, and "sync" is required to be wired to
IC723.Pin17.<br/>

#### Note on Multi-Region chips
Modchips that are designed to work in different regions are sending a different
string (SCEA, SCEE, SCEI) in each loop cycle. Due to the slow 250bps transfer
rate, it may take a while until the PSX has received the correct string, so
this multi-region technique may cause a noticeable boot-delay.<br/>

#### Stealth (hidden modchip)
The Stealth connection is required for some newer games with anti-modchip
protection, ie. games that refuse to run if they detect a modchip. The
detection relies on the fact that the SCEx signal is normally received only
when booting the disk, whilst older modchips were sending that signal
permanently. Stealth modchips are sending the signal only on power-up (and when
inserting a new disk, which can be sensed via SHELL\_OPEN signal).<br/>
Modchip detection reportedly works like so (not too sure if all commands are
required, some seem to be rather offtopic):<br/>
```
  1.  Com 19h,20h   ;Retrieve CDROM Controller timestamp
  2.  Com 01h       ;CdlNop: Get CD status
  3.  Com 07h       ;CdlMotorOn: Make CD-ROM drive ready (blah?)
  4.  Com 02h,1,1,1 ;CdlSetloc(01:01:01) (sector that does NOT have SCEx data)
  5.  Com 0Eh,1     ;CdlSetmode: Turn on CD-DA read mode
  6.  Short Delay
  7.  Com 16h       ;CdlSeekP: Seek to Setloc's parameters (4426)
  8.  Com 0Bh       ;CdlMute: Turn off sound so CdlPlay is inaudible
  9.  Com 03h       ;CdlPlay: Start playing CD-DA.
  10. Com 19h,04h   ;ResetSCExInfo (reset GetSCExInfo response to 0,0)
  11. Long Delay    ;wait until the modchip (if any) has output SCEx data
  12. Com 19h,05h   ;GetSCExInfo (returns total,success counters)
  13. Com 09h       ;CdlPause: Stop command 19h.
```
If GetSCExInfo returns nonzero values, then the console is equipped with a
modchip, and if so, anti-modchip games would refuse to work (no matter if the
disk is an illegal copy, or not).<br/>

#### NTSC-Boot BIOS Patch
Typically connects to two or three BIOS address/data lines, apparently watching
that signals, and dragging a data line LOW at certain time, to skip software
based region checks (eg. allowing to play NTSC games on PAL consoles).<br/>
Aside from the modchip connection, that additionally requires to adjust the
video signal (in 60Hz NTSC mode, the PSX defaults to generate a NTSC video
signal) (whilst most PAL screens can handle 60Hz refresh, they can't handle
NTSC colors) (on PSone boards, this can be fixed simply by grounding the /PAL
pin; IC502.Pin13) (on older PSX boards it seems to be required to install an
external color clock generator).<br/>

#### MODCHIP Connection Example
Connection for 8pin "12C508" mod chip from fatcat.co.nz for a PAL PSone with
PM-41 board (ie. with 208pin SPU CXD2938Q, and 52pin IC304 "C 3060,
SC430943PB"):<br/>
```
  1 3.5V        (supply)
  2 IC304.Pin44 (unknown?) (XLAT)
  3 BIOS.Pin15  (D2)
  4 BIOS.Pin31  (A18)
  5 SPU.Pin5    ("sync")
  6 SPU.Pin42   ("data")
  7 IC304.Pin19 (SHELL_OPEN)
  8 GND         (supply)
```
The chip can be used in a Basic connection (with only pin1,5,6,8 connected), or
Stealth and NTSC-Boot connection (additionally pin2,3,4,7 connected). Some
other modchips (such without internal oscillator) are additionally connected to
a 4MHz or 4.3MHz signal on the mainboard. Some early modchips also connected to
a bunch of additional pins that were reportedly for power-on timings (whilst
newer chips use hardcoded power-on delays).<br/>

#### Nocash BIOS "Modchip" Feature
The nocash PSX bios outputs the "data" signal on the A20 address line, so
(aside from the BIOS chip) one only needs to install a 1N4148 diode and two
wires to unlock the CDROM:<br/>
```
  SPU.Pin42 "data" -------|>|------ CPU.Pin149 (A20)
  SPU.Pin5  "sync" ---------------- IC723.Pin17
```
With the "sync" connection, the SCEx signal from the disk is disabled (ie. even
original licensed disks are no longer recognized, unless SCEx is output via A20
by software). For more variants, see:<br/>
[CDROM Protection - Chipless Modchips](cdromformat.md#cdrom-protection-chipless-modchips)<br/>



##   CDROM Protection - Chipless Modchips
The nocash kernel clone outputs a SCEX signal via A20 and A21 address lines,
(so one won't need a separate modchip/microprocessor):<br/>
```
  A20 = the normal SCEX signal (inverted ASCII, eg. "A" = BEh)   ;all boards
  A21 = uninverted SCEX signal (uninverted ASCII, eg. "A" = 41h) ;PU-7..PU-20
  A21 = always 1 during SCEX output                              ;PU-22 and up
```
When using the clone bios as internal ROM replacement, A20 can be used with
simple wires/diodes. Doing that with external expansion ROMs would cause the
console to stop working when unplugging the ROM, hence needing a slightly more
complex circuit with transistors/logic chips.<br/>

#### External Expansion ROM version, for older boards (PU-7 through PU-20):
```
              .--------.-.                 .--------.-.
  GATE--------|C  NPN  |  .    DATA--------|C  NPN  |  .
  A20--[10K]--|B  BC   |  |    A21--[10K]--|B  BC   |  |
  GND---------|E  547  |  '    GND---------|E  547  |  '
              '--------'-'                 '--------'-'
```

#### External Expansion ROM version, for newer boards (PU-22):
```
         .-------------------.
  A21----|OE1,OE2            |
  A20----|IN1   74HC126  OUT1|--- DATA
  WFCK---|IN2            OUT2|--- SYNC
         '-------------------'
```

#### Internal Kernel ROM version, for older boards (PU-7 through PU-20):
```
  GATE---------GND
  DATA---------A20
```

#### Internal Kernel ROM version, for newer boards (PU-22 through PM-41(2)):
```
  SYNC--------WFCK
  DATA---|>|---A20
```

#### What pin is where...
```
  GATE is IC703.Pin2  (?) (8pin chip with marking "082B")   ;PU-7? .. PU-16
  GATE is IC706.Pin7/10   (16pin "118" (uPC5023GR-118)      ;PU-18 .. PU-20
  SYNC is IC723.Pin17(TEO)(20pin "SONY CXA2575N")           ;PU-22 .. PM-41(2)
  DATA is IC???.Pin7 (CG) (8pin chip with marking "2903")   ;PU-7? .. PU-16
  DATA is IC706.Pin1 (CG) (16pin "118" (uPC5023GR-118)      ;PU-18 .. PU-20
  DATA is HC05.Pin17 (CG) (52pin "SONY SC4309xxPB")         ;PU-7 .. EARLY-PU-8
  DATA is HC05.Pin32 (CG) (80pin "SONY E35D, 4246xx 185")   ;LATE-PU-8 .. PU-20
  DATA is SPU.Pin42 (CEI) (208pin "SONY CXD2938Q")          ;PU-22 .. PM-41
  DATA is SPU.Pin36?(CEI) (176pin "SONY CXD2941R")          ;PM-41(2)
  WFCK is SPU.Pin5 (WFCK) (208pin "SONY CXD2938Q")          ;PU-22 .. PM-41
  WFCK is SPU.Pin84(WFCK) (176pin "SONY CXD2941R")          ;PM-41(2)
  A20  is CPU.Pin149(A20) (208-pin CPU CXD8530 or CXD8606)  ;PU-7 .. PM-41(2)
  A20  is EXP.Pin28 (A20) (68-pin Expansion Port)           ;PU-7 .. PU-22
  A21  is CPU.Pin150(A21) (208-pin CPU CXD8530 or CXD8606)  ;PU-7 .. PM-41(2)
  A21  is EXP.Pin62 (A21) (68-pin Expansion Port)           ;PU-7 .. PU-22
```
GATE on PU-18 is usually IC706.Pin7 (but IC706.Pin10 reportedly works, too).<br/>
GATE on PU-20 is usually IC706.Pin10 (but IC706.Pin7 might work, too).<br/>



##   CDROM Protection - LibCrypt
LibCrypt is an additional copy-protection, used by about 100 PSX games. The
protection uses a 16bit decryption key, which is stored as bad position data in
Subchannel Q. The 16bit key is then used for a simple XOR-decryption on certain
800h-byte sectors.<br/>

#### Protected sectors generation schemas
There are some variants on how the Subchannel Q data is modified:<br/>
```
  1. 2 bits from both MSFs are modified,
     CRC-16 is recalculated and XORed with 0x0080.
     Games: MediEvil (E).
  2. 2 bits from both MSFs are modified,
     original CRC-16 is XORed with 0x8001.
     Games: CTR: Crash Team Racing (E) (No EDC), CTR: Crash Team Racing (E)
     (EDC), Dino Crisis (E), Eagle One: Harrier Attack (E) et al.
  3. Either 2 bits or none from both MSFs are modified,
     CRC-16 is recalculated and XORed with 0x0080.
     Games: Ape Escape (S) et al.
```
Anyways, the relevant part is that the modified sectors have wrong CRCs (which
means that the PSX cdrom controller will ignore them, and the GetlocP command
will keep returning position data from the previous sector).<br/>

#### LibCrypt sectors
The modified sectors could be theoretically located anywhere on the disc,
however, all known protected games are having them located on the same sectors:<br/>
```
  No.    <------- Minute=03/Normal ------->  <------- Minute=09/Backup ------->
  Bit15  14105 (03:08:05)  14110 (03:08:10)  42045 (09:20:45)  42050 (09:20:50)
  Bit14  14231 (03:09:56)  14236 (03:09:61)  42166 (09:22:16)  42171 (09:22:21)
  Bit13  14485 (03:13:10)  14490 (03:13:15)  42432 (09:25:57)  42437 (09:25:62)
  Bit12  14579 (03:14:29)  14584 (03:14:34)  42580 (09:27:55)  42585 (09:27:60)
  Bit11  14649 (03:15:24)  14654 (03:15:29)  42671 (09:28:71)  42676 (09:29:01)
  Bit10  14899 (03:18:49)  14904 (03:18:54)  42813 (09:30:63)  42818 (09:30:68)
  Bit9   15056 (03:20:56)  15061 (03:20:61)  43012 (09:33:37)  43017 (09:33:42)
  Bit8   15130 (03:21:55)  15135 (03:21:60)  43177 (09:35:52)  43182 (09:35:57)
  Bit7   15242 (03:23:17)  15247 (03:23:22)  43289 (09:37:14)  43294 (09:37:19)
  Bit6   15312 (03:24:12)  15317 (03:24:17)  43354 (09:38:04)  43359 (09:38:09)
  Bit5   15378 (03:25:03)  15383 (03:25:08)  43408 (09:38:58)  43413 (09:38:63)
  Bit4   15628 (03:28:28)  15633 (03:28:33)  43634 (09:41:59)  43639 (09:41:64)
  Bit3   15919 (03:32:19)  15924 (03:32:24)  43963 (09:46:13)  43968 (09:46:18)
  Bit2   16031 (03:33:56)  16036 (03:33:61)  44054 (09:47:29)  44059 (09:47:34)
  Bit1   16101 (03:34:51)  16106 (03:34:56)  44159 (09:48:59)  44164 (09:48:64)
  Bit0   16167 (03:35:42)  16172 (03:35:47)  44312 (09:50:62)  44317 (09:50:67)
```
Each bit is stored twice on Minute=03 (five sectors apart). For some reason,
there is also a "backup copy" on Minute=09 (however, the libcrypt software
doesn't actually support using that backup stuff, and, some discs don't have
the backup at all (namely, discs with less than 10 minutes on track 1?)).<br/>
A modified sector means a "1" bit, an unmodified means a "0" bit. The 16bit
keys of the existing games are always having eight "0" bits, and eight "1" bits
(meaning that there are 16 modified sectors on Minute=03, and, if present,
another 16 ones one Minute=09).<br/>

#### Example (Legacy of Kain)
Legacy of Kain (PAL) is reading the LibCrypt data during the title screen, and
does then display GOT KEY!!! on TTY terminal (this, no matter if the correct
16bit key was received).<br/>
The actual protection jumps in a bit later (shortly after learning to glide,
the game will hang when the first enemies appear if the key isn't okay).
Thereafter, the 16bit key is kept used once and when to decrypt 800h-byte
sector data via simple XORing.<br/>
The 16bit key (and some other related counters/variables) aren't stored in RAM,
but rather in COP0 debug registers (which are mis-used as general-purpose
storage in this case), for example, the 16bit key is stored in LSBs of the
"cop0r3" register.<br/>
In particular, the encryption is used for some of the BIGFILE.DAT folder
headers:<br/>
[CDROM File Archive BIGFILE.DAT (Soul Reaver)](cdromfileformats.md#cdrom-file-archive-bigfiledat-soul-reaver)<br/>
