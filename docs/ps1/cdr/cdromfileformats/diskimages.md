#   Disk Images

##   CDROM Disk Images CCD/IMG/SUB (CloneCD)
#### File.IMG - 2352 (930h) bytes per sector
Contains the sector data, recorded at 930h bytes per sector. Unknown if other
sizes are also used/supported (like 800h bytes/sector, or even images with
mixed sizes of 800h and 930h for different tracks).<br/>

#### File.SUB - 96 (60h) bytes per sector (subchannel P..W with 96 bits each)
Contains subchannel data, recorded at 60h bytes per sector.<br/>
```
  00h..0Bh 12 Subchannel P (Pause-bits, usually all set, or all cleared)
  0Ch..17h 12 Subchannel Q (ADR/Control, custom info, CRC-16-CCITT)
  18h..5Fh .. Subchannel R..W (usually zero) (can be used for CD-TEXT)
```
Optionally, the .SUB file can be omitted (it's needed only for discs with
non-standard subchannel data, such like copy-protected games). And, some
CloneCD disc images are bundled with an empty 0-byte .SUB file (which is about
same as completely omitting the .SUB file).<br/>

#### File.CCD - Lead-in info in text format
Contains Lead-in info in ASCII text format. Lines should be terminated by
0Dh,0Ah. The overall CCD filestructure is:<br/>
```
  [CloneCD]     ;File ID and version
  [Disc]        ;Overall Disc info
  [CDText]      ;CD-TEXT (included only if present)
  [Session N]   ;Session(s) (numbered 1 and up)
  [Entry N]     ;Lead-in entries (numbered 0..."TocEntries-1")
  [TRACK N]     ;Track info (numbered 1 and up)
```
Read on below for details on the separate sections.<br/>

#### [CloneCD]
```
  Version=3             ;-version (usually 3) (rarely 2)
```

#### [Disc]
```
  TocEntries=4          ;-number of [Entry N] fields (lead-in info blocks)
  Sessions=1            ;-number of sessions (usually 1)
  DataTracksScrambled=0 ;-unknown purpose (usually 0)
  CDTextLength=0        ;-total size of 18-byte CD-TEXT chunks (usually 0)
  CATALOG=NNNNNNNNNNNNN ;-13-digit EAN-13 barcode (included only if present)
```

#### [CDText]
```
  Entries=N       ;number of following entries (CDTextLength/18) (not /16)
  Entry 0=80 00 NN NN NN NN NN NN NN NN NN NN NN NN NN NN   ;entry 0
  Entry 1=80 NN NN NN NN NN NN NN NN NN NN NN NN NN NN NN   ;entry 1
  ...
  Entry XX=8f NN NN NN NN NN NN NN NN NN NN NN NN NN NN NN  ;entry N-1
  Note: Each entry contains 16 bytes (ie. "18-byte CD-TEXT" with CRC excluded)
  "NN NN NN.." consists of 2-digit lowercase HEX numbers (without leading "0x")
```

#### [Session 1]
```
  PreGapMode=2          ;-unknown purpose (usually 1 or 2) (or 0)
  PreGapSubC=1          ;-unknown purpose (usually 0 or 1)
```
Above are unknown, PreGapMode might be 0=Audio, 1=Mode1, 2=Mode2 for pregap,
though unknown for which pregap(s) of which track(s), presumably for first
track?<br/>

#### [Entry 0]
[Entry 0..2] are usually containing Point A0h..A2h info. [Entry 3..N] are
usually TOC info for Track 1 and up.<br/>
```
  Session=1             ;-session number that this entry belongs to (usually 1)
  Point=0xa0            ;-point (0..63h=Track, non-BCD!) (A0h..XXh=specials) Q2
  ADR=0x01              ;-lower 4bit of ADR/Control (usually 1)           Q0.lo
  Control=0x04          ;-upper 4bit of ADR/Control (eg. 0=audio, 4=data) Q0.hi
  TrackNo=0             ;-usually/always 0 (as [Entry N]'s are in Lead-in)   Q1
  AMin=0                ;\current MSF address                                Q3
  ASec=0                ; (dummy zero values) (actual content                Q4
  AFrame=0              ; would be current lead-in position)                 Q5
  ALBA=-150             ;/ALBA=((AMin*60+ASec)*75+AFrame)-PreGapSize
  Zero=0                ;-probably reserved byte from Q channel              Q6
  PMin=1                ;\referenced MSF address (non-BCD!), for certain     Q7
  PSec=32               ; Point's, PMin may contain a Track number, and PSec Q8
  PFrame=0              ; the disc type value (that without non-BCD-glitch)  Q9
  PLBA=6750             ;/PLBA=((PMin*60+PSec)*75+PFrame)-PreGapSize
```

#### [TRACK 1]             ;-track number (non-BCD) (1..99)
```
  MODE=2                ;-mode (0=Audio, 1=Mode1, 2=Mode2)
  ISRC=XXXXXNNNNNNN     ;-12-letter/digit ISRC code (included only if present)
  INDEX 0=N             ;-1st sector with index 0, missing EVEN if any?
  INDEX 1=N             ;-1st sector with index 1, usually same as track's PLBA
  INDEX 2=N             ;-1st sector with index 2, if any
  etc.
```

#### Missing Sectors &amp; Sector Size
The .CCD file doesn't define the "PreGapSize" (the number of missing sectors at
begin of first track). It seems to be simply constant "PreGapSize=150". Unless
one is supposed to calculate it as
"PreGapSize=((PMin\*60+PSec)\*75+PFrame)-PLBA".<br/>
The SectorSize seems to be also constant, "SectorSize=930h".<br/>

#### Non-BCD Caution
All Min/Sec/Frame/Track/Index values are expressed in non-BCD, ie. they must be
converted to BCD to get the correct values (as how they are stored on real
CDs). Exceptions are cases where those bytes have other meanings: For example,
"PSec=32" does normally mean BcdSecond=32h, but for Point A0h it would mean
DiscType=20h=CD-ROM-XA).<br/>
The Point value is also special, it is expressed in hex (0xNN), but nonetheless
it is non-BCD, ie. Point 1..99 are specified as 0x01..0x63, whilst, Point
A0h..FFh are specified as such (ie. as 0xA0..0xFF).<br/>

#### Versions
Version=1 doesn't seem to exist (or it is very rare). Version=2 is quite rare,
and it seems to lack the [TRACK N] entries (meaning that there is no MODE and
INDEX information, except that the INDEX 1 location can be assumed to be same
as PLBA). Version=3 is most common, this version includes [TRACK N] entries,
but often only with INDEX=1 (and up, if more indices), but without INDEX 0 (on
Track 1 it's probably missing due to pregap, on further Tracks it's missing
without reason) (so, only ways to reproduce INDEX=0 would be to guess it being
located 2 seconds before INDEX=1, or, to use the information from the separate
.SUB file, if that file is present; note: presence of index 0 is absolutely
required for some games like PSX Tomb Raider 2).<br/>

#### Entry &amp; Points &amp; Sessions
The [Entry N] fields are usually containing Point A0h,A1h,A2h, followed by
Point 1..N (for N tracks). For multiple sessions: The session is terminated by
Point B0h,C0h. The next session does then contain Point A0h,A1h,A2h, and Point
N+1..X (for further tracks). The INDEX values in the [TRACK N] entries are
originated at the begin of the corresponding session, whilst PLBA values in
[Entry N] entries are always originated at the begin of the disk.<br/>



##   CDROM Disk Images CDI (DiscJuggler)
#### Overall Format
```
  Sector Data (sector 00:00:00 and up)          ;-body
  Number of Sessions (1 byte)     <--- located at "Filesize-Footersize"
  Session Block for 1st session (15 bytes)      ;\
  nnn-byte info for 1st track                   ; 1st session
  nnn-byte info for 2nd track (if any)          ;
  etc.                                          ;/
  Session Block for 2nd session (15 bytes)      ;\
  nnn-byte info for 1st track                   ; 2nd session (if any)
  nnn-byte info for 2nd track (if any)          ;
  etc.                                          ;/
  etc.                                          ;-further sessions (if any)
  Session Block for no-more-sessions (15 bytes) ;-end marker
  nnn-byte Disc Info Block                      ;-general disc info
  Entrypoint (4 bytes)            <--- located at "Filesize-4"
```

#### Sector Data
Contains Sector Data for sector 00:00:00 and up (ie. all sectors are stored in
the file, there are no missing "pregap" sectors).<br/>
Sector Size can be 800h..990h bytes/sector (sector size may vary per track).<br/>

#### Number of Sessions (1 byte)
```
  00h   1   Number of Sessions (usually 1)
```

#### Session Block (15-bytes)
```
  00h   1   Unknown (00h)
  01h   1   Number of Tracks in session (01h..63h) (or 00h=No More Sessions)
  02h   7   Unknown (00h-filled)
  09h   1   Unknown (01h)
  0Ah   3   Unknown (00h-filled)
  0Dh   2   Unknown (FFh,FFh)
```

#### Track/Disc Header (30h+F bytes) (used in Track Blocks and Disc Info Block)
```
  00h   12  Unknown (FFh,FFh,00h,00h,01h,00h,00h,00h,FFh,FFh,FFh,FFh)
  0Ch   3   Unknown (DAh,0Ah,D5h or 64h,05h,2Ah) (random/id/chksum?)
  0Fh   1   Total Number of Tracks on Disc (00h..63h) (non-BCD)
  10h   1   Length of below Path/Filename (F)
  11h   (F) Full Path/Filename (eg. "C:\folder\file.cdi")
  11h+F 11  Unknown (00h-filled)
  1Ch+F 1   Unknown (02h)
  1Dh+F 10  Unknown (00h-filled)
  27h+F 1   Unknown (80h)
  28h+F 4   Unknown (00057E40h) (=360000 decimal) (disc capacity 80 minutes?)
  2Ch+F 2   Unknown (00h,00h)
  2Eh+F 2   Medium Type (0098h=CD-ROM, 0038h=DVD-ROM)
```

#### Track Block (E4h+F+I+T bytes)
```
  00h     30h+F Track/Disc Header (see above)
  30h+F   02h   Number of Indices (usually 0002h) (I=Num*4)
  32h+F   (I)   32bit Lengths (per index) (eg. 00000096h,00007044h)
  32h+FI  04h   Number of CD-Text blocks (usually 0) (T=Num*18+VariableLen's)
  36h+FI  (T)   CD-Text (if any) (see "mirage_parser_cdi_parse_cdtext")
  36h+FIT 02h   Unknown (00h,00h)
  38h+FIT 01h   Track Mode (0=Audio, 1=Mode1, 2=Mode2/Mixed)
  39h+FIT 07h   Unknown (00h,00h,00h,00h,00h,00h,00h)
  40h+FIT 04h   Session Number (starting at 0) (usually 00h)
  44h+FIT 04h   Track Number   (non-BCD, starting at 0) (00h..62h)
  48h+FIT 04h   Track Start Address (eg. 00000000h)
  4Ch+FIT 04h   Track Length        (eg. 000070DAh)
  50h+FIT 0Ch   Unknown (00h-filled)
  5Ch+FIT 04h   Unknown (00000000h or 00000001h)
  60h+FIT 04h   read_mode (0..4)
                  0: Mode1,        800h, 2048
                  1: Mode2,        920h, 2336
                  2: Audio,        930h, 2352
                  3: Raw+PQ,       940h, 2352+16 non-interleaved (P=only 1bit)
                  4: Raw+PQRSTUVW, 990h, 2352+96 interleaved
  64h+FIT 4     Control (Upper 4bit of ADR/Control, eg. 00000004h=Data)
  68h+FIT 1     Unknown (00h)
  69h+FIT 4     Track Length        (eg. 000070DAh) (same as above)
  6Dh+FIT 4     Unknown (00h,00h,00h,00h)
  71h+FIT 12    ISRC Code 12-letter/digit (ASCII?) string (00h-filled if none)
  7Dh+FIT 4     ISRC Valid Flag (0=None, Other?=Yes?)
  81h+FIT 1     Unknown (00h)
  82h+FIT 8     Unknown (FFh,FFh,FFh,FFh,FFh,FFh,FFh,FFh)
  8Ah+FIT 4     Unknown (00000001h)
  8Eh+FIT 4     Unknown (00000080h)
  92h+FIT 4     Unknown (00000002h)     (guess: maybe audio num channels??)
  96h+FIT 4     Unknown (00000010h)      (guess: maybe audio bits/sample??)
  9Ah+FIT 4     Unknown (0000AC44h) (44100 decimal, ie. audio sample rate?)
  9Eh+FIT 2Ah   Unknown (00h-filled)
  C8h+FIT 4     Unknown (FFh,FFh,FFh,FFh)
  CCh+FIT 12    Unknown (00h-filled)
  D8h+FIT 1       session_type  ONLY if last track of a session (else 0)
                   (0=Audio/CD-DA, 1=Mode1/CD-ROM, 2=Mode2/CD-XA)
  D9h+FIT 5     Unknown (00h-filled)
  DEh+FIT 1     Not Last Track of Session Flag (0=Last Track, 1=Not Last)
  DFh+FIT 1     Unknown (00h)
  E0h+FIT 4        address for last track of a session? (otherwise 00,00,FF,FF)
```

#### Disc Info Block (5Fh+F+V+T bytes)
```
  00h     30h+F Track/Disc Header (see above)
  30h+F   4     Disc Size (total number of sectors)
  34h+F   1     Volume ID Length (V) ;\from Primary Volume Descriptor[28h..47h]
  35h+F   (V)   Volume ID String     ;/(ISO Data discs) (unknown for Audio)
  35h+FV  1     Unknown (00h)
  36h+FV  4     Unknown (01h,00h,00h,00h)
  3Ah+FV  4     Unknown (01h,00h,00h,00h)
  3Eh+FV  13    EAN-13 Code 13-digit (ASCII?) string (00h-filled if none)
  4Bh+FV  4     EAN-13 Valid Flag (0=None, Other?=Yes?)
  4Fh+FV  4     CD-Text Length in bytes (T=Num*1)
  53h+FV  (T)   CD-Text (for Lead-in) (probably 18-byte units?)
  53h+FVT 8     Unknown (00h-filled)
  5Bh+FVT 4     Unknown (06h,00h,00h,80h)
```

#### Entrypoint (4 bytes) (located at "Filesize-4")
```
  00h     4     Footer Size in bytes
```



##   CDROM Disk Images CUE/BIN/CDT (Cdrwin)
#### .CUE/.BIN (CDRWIN)
CDRWIN stores disk images in two separate files. The .BIN file contains the raw
disk image, starting at sector 00:02:00, with 930h bytes per sector, but
without any TOC or subchannel information. The .CUE file contains additional
information about the separate track(s) on the disk, in ASCII format, for
example:<br/>
```
 FILE "PATH\FILENAME.BIN" BINARY
   TRACK 01 MODE2/2352
     INDEX 01 00:00:00           ;real address = 00:02:00  (+2 seconds)
   TRACK 02 AUDIO
     PREGAP 00:02:00             ;two missing seconds      (NOT stored in .BIN)
     INDEX 01 08:09:29           ;real address = 08:13:29  (+2 seconds +pregap)
   TRACK 03 AUDIO
     INDEX 00 14:00:29           ;real address = 14:04:29  (+2 seconds +pregap)
     INDEX 01 14:02:29           ;real address = 14:06:29  (+2 seconds +pregap)
   TRACK 04 AUDIO
     INDEX 00 18:30:20           ;real address = 18:34:20  (+2 seconds +pregap)
     INDEX 01 18:32:20           ;real address = 18:36:20  (+2 seconds +pregap)
```
The .BIN file does not contain ALL sectors, as said above, the first 2 seconds
are not stored in the .BIN file. Moreover, there may be missing sectors
somewhere in the middle of the file (indicated as PREGAP in the .CUE file;
PREGAPs are usually found between Data and Audio Tracks).<br/>
The MM:SS:FF values in the .CUE file are logical addresses in the .BIN file,
rather than physical addresses on real CDROMs. To convert the .CUE values back
to real addresses, add 2 seconds to all MM:SS:FF addresses (to compensate the
missing first 2 seconds), and, if the .CUE contains a PREGAP, then the pregap
value must be additionally added to all following MM:SS:FF addresses.<br/>
The end address of the last track is not stored in the .CUE, instead, it can be
only calculated by converting the .BIN filesize to MM:SS:FF format and adding 2
seconds (plus any PREGAP values) to it.<br/>

#### FILE \<filename\> BINARY|MOTOTOLA..or..MOTOROLA?|AIFF|WAVE|MP3
```
  (must appear before any other commands, except CATALOG)
  (uh, may also appear before further tracks)
```

#### FLAGS DCP 4CH PRE SCMS

#### INDEX NN MM:SS:FF

#### TRACK NN datatype
```
  AUDIO          ;930h  ;bytes 000h..92Fh
  CDG            ;?     ;?
  MODE1/2048     ;800h  ;bytes 010h..80Fh
  MODE1/2352     ;930h  ;bytes 000h..92Fh
  MODE2/2336     ;920h  ;bytes 010h..92Fh
  MODE2/2352     ;930h  ;bytes 000h..92Fh
  CDI/2336       ;920h  ;?
  CDI/2352       ;930h  ;bytes 000h..92Fh
```

#### PREGAP MM:SS:FF
#### POSTGAP MM:SS:FF
Duration of silence at the begin (PREGAP) or end (POSTGAP) of a track. Even if
it isn't specified, the first track will always have a 2-second pregap.<br/>
The gaps are NOT stored in the BIN file.<br/>

#### REM comment
Allows to insert comments/remarks (which are usually ignored). Some third-party
tools are mis-using REM to define additional information.<br/>

#### CATALOG 1234567890123
#### ISRC ABCDE1234567
```
  (ISRC must be after TRACK, and before INDEX)
```

#### PERFORMER "The Band"
#### SONGWRITER "The Writer"
#### TITLE "The Title"
These entries allow to define basic CD-Text info directly in the .CUE file.<br/>
Some third-party utilites allow to define additional CD-Text info via REM
lines, eg. "REM GENRE Rock".<br/>
Alternately, more complex CD-Text data can be stored in a separate .CDT file.<br/>

#### CDTEXTFILE "C:\LONG FILENAME.CDT"
Specifies an optional file which may contain CD-TEXT. The .CDT file consists of
raw 18-byte CD-TEXT fragments (which may include any type of information,
including exotic one's like a "Message" from the producer). For whatever
reason, there's a 00h-byte appended at the end of the file. Alternately to the
.CDT file, the less exotic types of CD-TEXT can be defined by PERFORMER, TITLE,
and SONGWRITER commands in the .CUE file.<br/>

#### Missing
Unknown if newer CUE/BIN versions do also support subchannel data.<br/>

#### Malformed .CUE files
Some .CCD files are bundled with uncommon/corrupted .CUE files, with entries as
so:<br/>
```
   TRACK 1 MODE2/2352   ;three spaces indent, and 1-digit track
   INDEX 1 00:00:00     ;three spaces indent, and 1-digit index
```
Normally, that should look as so:<br/>
```
  TRACK 01 MODE2/2352   ;two spaces indent, and 2-digit track
    INDEX 01 00:00:00   ;four spaces indent, and 2-digit index
```
The purpose of the malformed .CUE might be unsuccessful compatibility, or
tricking people into thinking that .CCD works better than .CUE.<br/>



##   CDROM Disk Images MDS/MDF (Alcohol 120%)
#### File.MDF - Contains sector data (optionally with sub-channel data)
Contains the sector data, recorded at 800h..930h bytes per sector, optionally
followed by 60h bytes subchannel data (appended at the end of each sector). The
stuff seems to be start on 00:02:00 (ie. the first 150 sectors are missing; at
least it is like so when "Session Start Sector" is -150).<br/>
The subchannel data (if present) consists of 8 subchannels, stored in 96 bytes
(each byte containing one bit per subchannel).<br/>
```
  Bit7..0 = Subchannel P..W (in that order, eg. Bit6=Subchannel Q)
```
The 96 bits (per subchannel) can be translated to bytes, as so:<br/>
```
  1st..8th bit  = Bit7..Bit0 of 1st byte (in that order, ie. MSB/Bit7 first)
  9st..16th bit = Bit7..Bit0 of 2nd byte ("")
  17th..        = etc.
```

#### File.MDS - Contains disc/lead-in info (in binary format)
An MDS file's structure consists of the following stuff ...<br/>
```
  Header              (58h bytes)
  Session block(s)    (usually one 18h byte entry)
  Data blocks         (N*50h bytes)
  Index blocks        (usually N*8 bytes)
  Filename blocks(s)  (usually one 10h byte entry)
  Filename string(s)  (usually one 6 byte string)
  Read error(s)       (usually none such)
```

#### Header (58h bytes)
```
  00h 16  File ID ("MEDIA DESCRIPTOR")
  10h 2   Unknown (01h,03h or 01h,04h or 01h,05h) (Fileformat version?)
  12h 2   Media Type (0=CD-ROM, 1=CD-R, 2=CD-RW, 10h=DVD-ROM, 12h=DCD-R)
  14h 2   Number of sessions (usually 1)
  16h 4   Unknown (02h,00h,00h,00h)
  1Ah 2   Zero (for DVD: Length of BCA data)
  1Ch 8   Zero
  24h 4   Zero (for DVD: Offset to BCA data)
  28h 18h Zero
  40h 4   Zero (for DVD: Offset to Disc Structures)   (from begin of .MDS file)
  44h 0Ch Zero
  50h 4   Offset to First Session-Block (usually 58h) (from begin of .MDS file)
  54h 4   Offset to Read errors (usually 0=None)      (from begin of .MDS file)
```

#### Session-Blocks (18h bytes)
```
  00h 4   Session Start Sector (starting at FFFFFF6Ah=-150 in first session)
  04h 4   Session End Sector     (XXX plus 150 ?)
  08h 2   Session number (starting at 1) (non-BCD)
  0Ah 1   Number of Data Blocks with any Point value (Total Data Blocks)
  0Bh 1   Number of Data Blocks with Point>=A0h      (Special Lead-In info)
  0Ch 2   First Track Number in Session (01h..63h, non-BCD!)
  0Eh 2   Last Track Number in Session  (01h..63h, non-BCD!)
  10h 4   Zero
  14h 4   Offset to First Data-Block (usually 70h) (from begin of .MDS file)
```

#### Data-Blocks (50h bytes)
Block 0..2 are usually containing Point A0h..A2h info. Block 3..N are usually
TOC info for Track 1 and up.<br/>
```
  00h 1   Track mode (see below for details)
  01h 1   Number of subchannels in .MDF file (0=None, 8=Sector has +60h bytes)
  02h 1   ADR/Control (but with upper/lower 4bit swapped, ie. MSBs=ADR!)    Q0
  03h 1   TrackNo (usually/always 00h; as this info is in Lead-in area)     Q1
  04h 1   Point  (Non-BCD!) (Track 01h..63h) (or A0h and up=Lead-in info)   Q2
  05h 4   Zero (probably dummy MSF and reserved byte from Q channel)   Q3..Q6?
  09h 1   Minute (Non-BCD!)  ;\MM:SS:FF of Point'ed track                   Q7
  0Ah 1   Second (Non-BCD!)  ; (or disc/lead-out info when Point>=A0h)      Q8
  0Bh 1   Frame  (Non-BCD!)  ;/                                             Q9
```
For Point\>=A0h, below 44h bytes at [0Ch..4Fh] are zero-filled<br/>
```
  0Ch 4   Offset to Index-block for this track    (from begin of .MDS file)
  10h 2   Sector size (800h..930h) (or 860h..990h if with subchannels)
  12h 1   Unknown (02h) (maybe number of indices?)
  13h 11h Zero
  24h 4   Track start sector, PLBA (00000000h=00:02:00)(or 00000096h=00:02:00?)
  28h 8   Track start offset                      (from begin of .MDF file)
  30h 4   Number of Filenames for this track (usually 1)
  34h 4   Offset to Filename Block for this track (from begin of .MDS file)
  38h 18h Zero
```
Trackmode:<br/>
```
  (upper 4bit seem to be meaningless?)
  00h=None (used for entries with Point=A0h..FF)
  A9h=AUDIO       ;sector size = 2352    930h  ;bytes 000h..92Fh
  AAh=MODE1       ;sector size = 2048    800h  ;bytes 010h..80Fh
  ABh=MODE2       ;sector size = 2336    920h  ;bytes 010h..92Fh
  ACh=MODE2_FORM1 ;sector size = 2048    800h  ;bytes 018h..817h (incomplete!)
  ADh=MODE2_FORM2 ;sector size = 2324+0? 914h  ;bytes 018h..91Bh (incomplete!)
  ADh=MODE2_FORM2 ;sector size = 2324+4? 918h  ;bytes ??..?? (contains what?)
  ECh=MODE2       ;sector size = 2448    990h  ;(930h+60h) (with subchannels)
```

#### Index Blocks (usually 8 bytes per track)
```
  00h 4  Number of sectors with Index 0 (usually 96h or zero)
  04h 4  Number of sectors with Index 1 (usually size of main-track area)
```
Index blocks are usually/always 8 bytes in size (two indices per track, even
when recording a CD with more than 2 indices per track).<br/>
The MDS file does usually contain Index blocks for \<all\> Data Blocks (ie.
including unused dummy Index Blocks for Data Blocks with Point\>=A0h).<br/>

#### Filename Blocks (10h bytes)
```
  00h 4  Offset to Filename (from begin of .MDS file)
  04h 1  Filename format (0=8bit, 1=16bit characters)
  05h 11 Zero
```
Normally all tracks are sharing the same filename block (although theoretically
the tracks could use separate filename blocks; with different filenames).<br/>

#### Filename Strings (usually 6 bytes)
```
  00h 6  Filename, terminated by zero (usually "*.mdf",00h)
```
Contains the filename of the of the sector data (usually "\*.mdf", indicating to
use the same name as for the .mds file, but with .mdf extension).<br/>

#### Read errors aka DPM data blocks (present if errors occured during recording)
```
  00h 4   Unknown (1)
  04h 4   Offset to following stuff
  08h 4   Unknown (2)
  0Ch 4   Unknown (7)
  10h 4   Unknown (1)
  14h 4   Number of read errors (E)
  18h E*4 LBA's for sectors with read errors (0 and up)
```
Instead of (or additionally to) read errors, there may be also hundreds of
Kbytes of unknown stuff appended (text strings in 8bit or 16bit format, binary
numbers, and huge zerofilled blocks).<br/>

#### Missing
Unknown if/how this format supports EAN-13, ISRC, CD-TEXT.<br/>



##   CDROM Disk Images NRG (Nero)
#### .NRG (NERO)
Nero is probably the most bloated and most popular CD recording software. The
first part of the file contains the disk image, starting at sector 00:00:00,
with 800h..930h bytes per sector. Additional chunk-based information is
appended at the end of the file, usually consisting of only four chunks:
CUES,DAOI,END!,NERO (in that order).<br/>

#### Chunk Entrypoint (in last 8/12 bytes of file)
```
  4   File ID "NERO"/"NER5"
  4/8 Fileoffset of first chunk
```

#### Cue Sheet (summary of the Table of Contents, TOC)
```
  4   Chunk ID "CUES"/"CUEX"
  4   Chunk size (bytes)
```
below EIGHT bytes repeated for each track/index,<br/>
of which, first FOUR bytes are same for both CUES and CUEX,<br/>
```
  1   ADR/Control from TOC (usually LSBs=ADR=1=fixed, MSBs=Control=Variable)
  1   Track  (BCD) (00h=Lead-in, 01h..99h=Track N, AAh=Lead-out)
  1   Index  (BCD) (usually 00h=pregap, 01h=actual track)
  1   Zero
```
next FOUR bytes for CUES,<br/>
```
  1   Zero
  1   Minute (BCD) ;starting at 00:00:00 = 2 seconds before ISO vol. descr.
  1   Second (BCD)
  1   Sector (BCD)
```
or, next FOUR four bytes for CUEX,<br/>
```
  4   Logical Sector Number (HEX) ;starting at FFFFFF6Ah (=00:00:00)
```
Caution: Above may contain two position 00:00:00 entries: one nonsense entry
for Track 00 (lead-in), followed by a reasonable entry for Track 01, Index 00.<br/>

#### Disc at Once Information
```
  4   Chunk ID "DAOI"/"DAOX"
  4   Chunk size (bytes)
  4   Garbage (usually same as above Chunk size)
  13  EAN-13 Catalog Number (13-digit ASCII) (or 00h-filled if none/unknown)
  1   Zero
  1   Disk type (00h=Mode1 or Audio, 20h=XA/Mode2) (and probably 10h=CD-I?)
  1   Unknown (01h)
  1   First track (Non-BCD) (01h..63h)
  1   Last track  (Non-BCD) (01h..63h)
```
below repeated for each track,<br/>
```
  12  ISRC in ASCII (eg. "USXYZ9912345") (or 00h-filled if none/unknown)
  2   Sector size (usually 800h, 920h, or 930h) (see Mode entry for more info)
  1   Mode:
        0=Mode1/800h ;raw mode1 data (excluding sync+header+edc+errorinfo)
        3=Mode2/920h ;almost full sector (exluding first 16 bytes; sync+header)
        6=Mode2/930h ;full sector (including first 16 bytes; sync+header)
        7=Audio/930h ;full sector (plain audio data)
      Mode values from wikipedia:
        00h for data                                     Mode1/800h
        02h
        03h for Mode 2 Form 1 data   eh? FORM1???        Mode2/920h
        05h for raw data                                 Mode1?/930h
        06h for raw Mode 2/form 1 data                   Mode2/930h
        07h for audio                                    Audio/930h
        0Fh for raw data with sub-channel                Mode1?/930h+WHAT?
        10h for audio with sub-channel                   Audio/930h+WHAT?
        11h for raw Mode 2/form 1 data with sub-channel  Mode2/WHAT?+WHAT?
       Note: Some newer files do actually use different sector sizes for each
       track (eg. 920h for the data track, and 930h for any following audio
       tracks), older files were using the same sector size for all tracks
       (eg. if the disk contained 930-byte Audio tracks, then Data tracks
       were stored at the same size, rather than at 800h or 920h bytes).
  3   Unknown (always 00h,00h,01h)
  4/8 Fileoffset 1 (Start of Track's Pregap) (with Index=00h)
  4/8 Fileoffset 2 (Start of actual Track) (with Index=01h and up)
  4/8 Fileoffset 3 (End of Track) (aka begin of next track's pregap)
```

#### End of chain
```
  4   Chunk ID "END!"
  4   Chunk size (always zero)
```

#### Track Information (contained only in Track at Once images)
```
  4     Chunk ID "TINF"/"ETNF"/"ETN2"
  4     Chunk size (bytes)
```
below repeated for each track,<br/>
```
  4/4/8 Track fileoffset        ;\32bit in TINF/ETNF chunks,
  4/4/8 Track length (bytes)    ;/64bit in ETN2 chunks
  4     Mode (should be same as in DAO chunks, see there) (implies sector size)
  0/4/4 Start lba on disc       ;\only in ETNF/ETN2 chunks,
  0/4/4 Unknown?                ;/not in TINF chunks
```

#### Unknown 1 (contained only in Track at Once images)
```
  4   Chunk ID "RELO"
  4   Chunk size (bytes)
  4   Zero
```

#### Unknown 2 (contained only in Track at Once images)
```
  4   Chunk ID "TOCT"
  4   Chunk size (bytes)
  1   Disk type (00h=Mode1 or Audio, 20h=XA/Mode2) (and probably 10h=CD-I?)
  1   Zero (00h)
```

#### Session Info (begin of a session) (contained only in multi-session images)
```
  4   Chunk ID "SINF"
  4   Chunk size (bytes)
  4   Number of tracks in session
```

#### CD-Text (contained only in whatever images)
```
  4   Chunk ID None/"CDTX"
  4   Chunk size (bytes) (must be a multiple of 18 bytes)
```
below repeated for each fragment,<br/>
```
  18  Raw 18-byte CD-text data fragments
```

#### Media Type? (contained only in whatever images)
```
  4   Chunk ID "MTYP"
  4   Chunk size (bytes)
  4   Unknown? (00000001h for CDROM) (maybe other value for DVD)
```

#### Optional Filenames (names where the image was generated from?)
```
  4   Chunk ID "AFNM"
  4   Chunk size (bytes)
  ..  Track Filenames (eg. "Track1.wav",0,"Track2.wav",0)
```

#### Optional Volume name
```
  4   Chunk ID "VOLM"
  4   Chunk size (bytes)
  ..  Name (eg. "Audio CD",00h)
```

#### Notes
Newer/older .NRG files may contain 32bit/64bit values (and use "OLD"/"NEW"
chunk names) (as indicated by the "/" slashes).<br/>
CAUTION: All 16bit/32bit/64bit values are in big endian byte-order.<br/>

#### Missing
Unknown if newer NRG versions do also support subchannel data.<br/>



##   CDROM Disk Image/Containers CDZ
.CDZ is a compressed disk image container format (developed by pSX Author, and
used only by the pSX emulator). The disk is split into 64kbyte blocks, which
allows fast random access (without needing to decompress all preceeding
sectors).<br/>
However, the compression ratio is surprisingly bad (despite of being
specifically designed for cdrom compression, the format doesn't remove
redundant sector headers, error correction information, and EDC checksums).<br/>

#### .CDZ File Structure
```
  FileID ("CDZ",00h for cdztool v0/v1, or "CDZ",01h for cdztool v2 and up)
  One or two Chunk(s)
```

#### .CDZ Chunk Format
Chunk Header in v0 (unreleased prototype):<br/>
```
  4    32bit Decompressed Size (of all blocks) (must be other than "ZLIB")
```
Chunk Header in v1 (first released version):<br/>
```
  4    ZLIB ID ("ZLIB")
  8    64bit Decompressed Size (of all blocks)
```
Chunk Header in v2 and up (later versions):<br/>
```
  4    Chunk ID (eg. "CUE",00h)
  8    Chunk Size in bytes (starting at "ZLIB" up to including Footer, if any)
  4    ZLIB ID ("ZLIB")
  8    64bit Decompressed Size (of all blocks)
```
Chunk Body (same in all versions):<br/>
```
  4    Number of Blocks (N)
  4    Block 1 Compressed Size (CS.1)
  4    Block 1 Decompressed Size (always 00010000h, except last block)
  CS.1 Block 1 Compressed ZLIB Data (starting with 78h,9Ch)
  ...  ...                                     ;\
  4    Block N Compressed Size (CS.N)          ; further block(s)
  4    Block N Decompressed Size               ; (if any)
  CS.N Block N Compressed ZLIB Data            ;/
```
Chunk Footer in v0 (when above header didn't have the "ZLIB" ID):<br/>
```
  4*N       Directory Entries for N blocks     ;-this ONLY for BIN chunk
```
Chunk Footer in v1 and up:<br/>
```
  BPD*(N-1) Directory Entries for N-1 blocks   ;\this ONLY for BIN chunk
  1         Bytes per Directory Entry (BPD)    ;/(not for CUE/CCD/MDS)
```
The "Compressed ZLIB Data" parts contain Deflate'd data (starting with 2-byte
ZLIB header, and ending with 4-byte ZLIB/ADLER checksum), for details see:<br/>
[CDROM File Compression ZIP/GZIP/ZLIB (Inflate/Deflate)](compression.md#cdrom-file-compression-zipgzipzlib-inflatedeflate)<br/>

#### .CDZ Chunks / Content
The chunk(s) have following content:<br/>
```
  noname+noname       --> .CUE+.BIN (cdztool v1 and below)
  "BIN",0             --> .ISO      (cdztool v2? and up)
  "CUE",0+"BIN",0     --> .CUE+.BIN (cdztool v2 and up)
  "CCD",0+"BIN",0     --> .CCD+.IMG (cdztool v2 and up)
  "CCD",0+"BIN",01h   --> .CCD+.IMG+.SUB (930h sectors, plus 60h subchannels)
  "MDS",0+"BIN",0     --> .MDS+.MDF (cdztool v5 only)
```
Note: cdztool doesn't actually recognize files with .ISO extension (however,
one can rename them to .BIN, and then compress them as CUE-less .BIN file).<br/>

#### Cdztool.exe Versions
```
  cdztool.exe v0, unrelased prototype
  cdztool.exe v1, 22 May 2005, CRC32=620dbb08, 102400 bytes, pSX v1.0-5
  cdztool.exe v2, 02 Jul 2006, CRC32=bcb29c1e, 110592 bytes, pSX v1.6
  cdztool.exe v3, 22 Jul 2006, CRC32=4062ba82, 110592 bytes, pSX v1.7
  cdztool.exe v4, 13 Aug 2006, CRC32=7388dd3d, 118784 bytes, pSX v1.8-11
  cdztool.exe v5, 22 Jul 2007, CRC32=f25c1659, 155648 bytes, pSX v1.12-13
```
Note: v0 wasn't ever released (it's only noteworthy because later versions do
have backwards compatibility for decompressing old v0 files). v1 didn't work
with all operating systems (on Win98 it just says "Error: Couldn't create
\<output\>" no matter what one is doing, however, v1 does work on later
windows versions like WinXP or so?).<br/>



##   CDROM Disk Image/Containers ECM
ECM (Error Code Modeler by Neill Corlett) is a utility that removes
unneccessary ECC error correction and EDC error detection values from
CDROM-images. This is making the images a bit smaller, but the real size
reduction isn't gained until subsequently compressing the images via tools like
ZIP. Accordingly, these files are extremly uncomfortable to use: One most first
UNZIP them, and then UNECM them.<br/>

#### .EXT.ECM - Double extension
ECM can be applied to various CDROM-image formats (like .BIN, .CDI, .IMG, .ISO,
.MDF, .NRG), as indicated by the double-extension. Most commonly it's applied
to .BIN files (hence using extension .BIN.ECM).<br/>

#### Example / File Structure
```
  45 43 4D 00                                      ;FileID "ECM",00h
  3C                                               ;Type 0, Len=10h (aka 0Fh+1)
  00 FF FF FF FF FF FF FF FF FF FF 00 00 02 00 02  ;16 data bytes
  02                                               ;Type 2, Len=1 (aka 00h+1)
  00 00 08 00 00 00 00 00 00 00 00 ..... 00 00 00  ;804h data bytes
  3C                                               ;Type 0, Len=10h (aka 0Fh+1)
  00 FF FF FF FF FF FF FF FF FF FF 00 00 02 01 02  ;16 data bytes
  02                                               ;Type 2, Len=1 (aka 00h+1)
  00 00 08 00 00 00 00 00 00 00 00 ..... 00 00 00  ;804h data bytes
  ...
  FC FF FF FF 3F                                   ;End Code (Len=FFFFFFFFh+1)
  NN NN NN NN                                      ;EDC (on decompressed data)
```

#### Type/Length Byte(s)
Type/Length is encoded in 1..5 byte(s), with "More=1" indicating that further
length byte(s) follow:<br/>
```
  1st Byte: Bit7=More, Bit6-2=LengthBit4-0, Bit1-0=Type(0..3)
  2nd Byte: Bit7=More, Bit6-0=LengthBit5-11
  3rd Byte: Bit7=More, Bit6-0=LengthBit12-18
  4th Byte: Bit7=More, Bit6-0=LengthBit19-25
  5th Byte: Bit7-6=Reserved/Zero, Bit5-0=LengthBit26-31
```
Length=FFFFFFFFh=End Indicator<br/>
The actual decompression LEN is: "LEN=Length+1"<br/>

#### ECM Decompression
Below is repeated LEN times (with LEN being the Length value plus 1):<br/>
```
  Type 0: load 1 byte, save 1 byte
  Type 1: load 803h bytes [0Ch..0Eh,10h..80Fh], save 930h bytes [0..92Fh]
  Type 2: load 804h bytes [14h..817h], save 920h bytes [10h..92Fh]
  Type 3: load 918h bytes [14h..91Bh], save 920h bytes [10h..92Fh]
```
Type 1-3 are reconstructing the missing bytes before saving. Type 2-3 are
saving only 920h bytes, so (if the original image contained full 930h byte
sectors) the missing 10h bytes must be inserted via Type 0. Type 0 can be also
used for copying whole sectors as-is (eg. Audio sectors, or Data sectors with
invalid Sync/Header/ECC/EDC values). And, Type 0 can be used to store
non-sector data (such like the chunks at the end of .NRG or .CDI files).<br/>

#### Central Mistakes
There's a lot of wrong with the ECM format. The two central problems are that
it doesn't support data-compression (and needs external compression tools like
zip/rar), and, that it doesn't contain a sector look-up table (meaning that
random access isn't possible unless when scanning the whole file until reaching
the desired sector).<br/>

#### Worst-case Scenario
As if ECM as such wouldn't be uncomfortable enough, you may expect typical ECM
users to get more things messed up. For example:<br/>
```
  A RAR file containing a 7Z file containing a ECM file containing a BIN file.
  The BIN containing only Track 1, other tracks stored in APE files.
  And, of course, the whole mess without including the required CUE file.
```



##   CDROM Subchannel Images
#### SBI (redump.org)
SBI Files start with a 4-byte FileID:<br/>
```
  4 bytes FileID ("SBI",00h)
```
Then followed by entries as so:<br/>
```
  3 bytes real absolute MM:SS:FF address where the sub q data was bad
  1 byte Format: the format can be 1, 2 or 3:
  Format 1: complete 10 bytes sub q data            (Q0..Q9)
  Format 2: 3 bytes wrong relative MM:SS:FF address (Q3..Q5)
  Format 3: 3 bytes wrong absolute MM:SS:FF address (Q7..Q9)
```
Note: The PSX libcrypt protection relies on bad checksums (Q10..Q11), which
will cause the PSX cdrom controller to ignore Q0..Q9 (and to keep returning
position data from most recent sector with intact checksum).<br/>
Ironically, the SBI format cannot store the required Q10..Q11 checksum. The
trick for using SBI files with libcrypted PSX discs is to ignore the useless
Q0..Q9 data, and to assume that all sectors in the SBI file have wrong Q10..Q11
checksums.<br/>

#### M3S (Subchannel Q Data for Minute 3) (ePSXe)
M3S files are containing Subchannel Q data for all sectors on Minute=03 (the
region where PSX libcrypt data is located) (there is no support for storing the
(unused) libcrypt backup copy on Minute=09). The .M3S filesize is 72000 bytes
(60 seconds \* 75 sectors \* 16 bytes). The 16 bytes per sector are:<br/>
```
  Q0..Q9   Subchannel Q data (normally position data)
  Q10..Q11 Subchannel Q checksum
  Q12..Q15 Dummy/garbage/padding (usually 00000000h or FFFFFFFFh)
```
Unfortunately, there are at least 3 variants of the format:<br/>
```
  1. With CRC (Q0..Q11 intact) (and Q12..Q15 randomly 00000000h or FFFFFFFFh)
  2. Without CRC (only Q0..Q9 intact, but Q10..Q15 zerofilled)
  3. Without anything (only Q0 intact, but Q1..Q15 zerofilled)
```
The third variant is definetly corrupt (and one should ignore such zerofilled
entries). The second variant is corrupt, too (but one might attempt to repair
them by guessing the missing checksum: if it contains normal position values
assume correct crc, if it contains uncommon values assume a libcrypted sector
with bad crc).<br/>
The M3S format is intended for libcrypted PSX games, but, people seem to have
also recorded (corrupted) M3S files for unprotected PSX games (in so far, more
than often, the M3S files might cause problems, instead of solving them).<br/>
Note: The odd 16-byte format with 4-byte padding does somehow resemble the "P
and Q Sub-Channel" format 'defined' in MMC-drafts; if the .M3S format was based
on the MMC stuff: then the 16th byte might contain a Subchannel P "pause" flag
in bit7.<br/>

#### CDROM Images with Subchannel Data
Most CDROM-Image formats can (optionally) contain subchannel recordings. The
downsides are: Storing all 8 subchannels for a full CDROM takes up about
20MBytes. And, some entries may contain 'wrong' data (read errors caused by
scratches cannot be automatically repaired since subchannels do not contain
error correction info).<br/>
If present, the subchannel data is usually appended at the end of each sector
in the main binary file (one exception is CloneCD, which stores it in a
separate .SUB file instead of in the .IMG file).<br/>
```
  CCD/IMG/SUB (CloneCD)  P-W  60h-bytes Non-interleaved (in separate .SUB file)
  CDI (DiscJuggler)      P-Q  10h-bytes Non-interleaved (in .CDI file)
  ""                     P-W  60h-bytes Interleaved (in .CDI file)
  CUE/BIN/CDT (Cdrwin)        N/A
  ISO (single-track)          N/A
  MDS/MDF (Alcohol 120%) P-W  60h-bytes Interleaved (in .MDF file)
  NRG (Nero)             P-W  60h-bytes Interleaved (in .NRG file)
```
Interleaved Subchannel format (eg. Alcohol .MDF files):<br/>
```
  00h-07h   80 C0 80 80 80 80 80 C0   ;P=FFh, Q=41h=ADR/Control, R..W=00h
  08h-0Fh   80 80 80 80 80 80 80 C0   ;P=FFh, Q=01h=Track,       R..W=00h
  10h-17h   80 80 80 80 80 80 80 C0   ;P=FFh, Q=01h=Index,       R..W=00h
  18h-1Fh   80 80 80 80 80 80 80 80   ;P=FFh, Q=00h=RelMinute,   R..W=00h
  20h-27h   80 80 80 80 80 80 80 80   ;P=FFh, Q=00h=RelSecond,   R..W=00h
  28h-2Fh   80 80 80 80 80 80 80 80   ;P=FFh, Q=00h=RelSector,   R..W=00h
  30h-37h   80 80 80 80 80 80 80 80   ;P=FFh, Q=00h=Reserved,    R..W=00h
  38h-3Fh   80 80 80 80 80 80 80 80   ;P=FFh, Q=00h=AbsMinute,   R..W=00h
  40h-47h   80 80 80 80 80 80 C0 80   ;P=FFh, Q=02h=AbsSecond,   R..W=00h
  48h-4Fh   80 80 80 80 80 80 80 80   ;P=FFh, Q=00h=AbsSector,   R..W=00h
  50h-57h   80 80 C0 80 C0 80 80 80   ;P=FFh, Q=28h=ChecksumMsb, R..W=00h
  58h-5Fh   80 80 C0 C0 80 80 C0 80   ;P=FFh, Q=32h=ChecksumLsb, R..W=00h
```
Non-Interleaved Subchannel format (eg. CloneCD .SUB files):<br/>
```
  00h-0Bh   FF FF FF FF FF FF FF FF FF FF FF FF  ;Subchannel P (Pause)
  0Ch-17h   41 01 01 00 00 00 00 00 02 00 28 32  ;Subchannel Q (Position)
  18h-23h   00 00 00 00 00 00 00 00 00 00 00 00  ;Subchannel R
  24h-2Fh   00 00 00 00 00 00 00 00 00 00 00 00  ;Subchannel S
  30h-3Bh   00 00 00 00 00 00 00 00 00 00 00 00  ;Subchannel T
  3Ch-47h   00 00 00 00 00 00 00 00 00 00 00 00  ;Subchannel U
  48h-53h   00 00 00 00 00 00 00 00 00 00 00 00  ;Subchannel V
  54h-5Fh   00 00 00 00 00 00 00 00 00 00 00 00  ;Subchannel W
```
Non-Interleaved P-Q 10h-byte Subchannel format:<br/>
```
  This is probably based on MMC protocol, which would be as crude as this:
  The 96 pause bits are summarized in 1 bit. Pause/Checksum are optional.
  00h-09h   41 01 01 00 00 00 00 00 02 00        ;Subchannel Q (Position)
  0Ah-0Bh   28 32    ;<-- OPTIONAL, can be zero! ;Subchannel Q (Checksum)
  0Ch-0Eh   00 00 00                             ;Unused padding (zero)
  0F        80       ;<-- OPTIONAL, can be zero! ;Subchannel P (Bit7=Pause)
```



##   CDROM Disk Images PBP (Sony)
#### .PBP
Sony's disc image format used on PSP. Can store multi-disc images in a single
file. Supports deflate data compression and some yet unknown audio compression.
A homebrew compressor can compress whole discs with deflate (which works, but
it isn't very good to compress audio sectors that way).<br/>

#### PBP Format (rev-engineered from homebrew DBALL.PBP)
```
  000000h 4    ID (00h,"PBP")
  000004h 4    Version? (10000h) (but, reportedly "always 100h or 1000100h")
  000008h 4    Offset of the file PARAM.SFO (28h)
  00000Ch 4    Offset of the file ICON0.PNG (3D8h)
  000010h 4    Offset of the file ICON1.PMF (3D8h) or ICON1.PNG
  000014h 4    Offset of the file PIC0.PNG  (3D8h) or UNKNOWN.PNG
  000018h 4    Offset of the file PIC1.PNG  (3D8h) or PICT1.PNG
  00001Ch 4    Offset of the file SND0.AT3  (3D8h)
  000020h 4    Offset of the file DATA.PSP  (3D8h)
  000024h 4    Offset of the file DATA.PSAR (10000h)
  000028h ..   PARAM.SFO file (zerofilled in homebrew PBP)
  0003D8h ..   PNG files etc  (zerofilled in homebrew PBP)
  010000h 0Ch  ID "PSISOIMG0000"
  01000Ch 4    PBP Size-10000h              (144740h)
  010010h 4    PBP Size-6420h (???)         (14E320h)
  010014h ..   Zerofilled
  010400h 0Bh  Game ID ("_SCUS_94476" for Hot Shots Golf 2)
  01040Bh ..   Zerofilled
  010800h A00h TOC List    (0Ah-byte per entry) (unused entries are zerofilled)
  011200h 20h  Zerofilled
  011220h 4    PBP Size-D2CFh (???)         (147471h)
  011224h 4    Zero
  011228h 4    Unknown     (7FFh)
  01122Ch 11h  Game Name   ("Hot Shots Golf",C2h,AEh,"2")
  01123Dh ..   Zerofilled
  014000h ..   Sector List (20h-byte per entry) (unused entries are zerofilled)
  ...     ..   Zerofilled
  110000h ..   Deflated sectors (9300h bytes after decompression)
  15467Dh B8h  One extra compression block that is NOT in Sector List ???
  154735h 0Bh  Weird padding with ASCII "00000000000"
  154740h -    End of file
 TOC List (Subchannel Q with ADR=1 during Lead-In):
  000h 1   ADR/Control (eg. 41h=Data Track)
  001h 1   Track       (always 00h=Lead-in for all TOC List entries)
  002h 1   Point       (A0h, A1h, A2h, or Track 01h and up)      (BCD?)
  003h 3   Dummy MSF   (usually 00:00:00 or weirdly 00:02:01)    (BCD?)
  006h 1   Reserved    (00h)
  007h 3   Actual MSF  (or TOC info for Point=A0h,A1h)           (BCD?)
 Example TOC (DBALL.PBP):
  41 00 A0 00 00 00 00 01 20 00   ;First Track (1) and Type (20h=CDROM-XA)
  41 00 A1 00 00 00 00 01 00 00   ;Last Track Number (1)
  41 00 A2 00 00 00 00 27 19 22   ;Lead-Out, uh at 27:19:22 in DBALL.PBP ???
  41 00 01 00 02 01 00 00 02 00   ;Track 1 at 00:02:00
  (remaining entries are zerofilled)
 Example TOC (PSALM69.PBP):
  01 00 01 00 02 00 00 00 00 00   ;Track 1 as audio <-- why that ???
  01 00 02 02 37 44 00 00 00 00   ;Track 2 as audio
  01 00 03 03 25 45 00 00 00 00   ;Track 3 as audio
  41 00 01 00 02 01 00 00 02 00   ;Track 1 as data <-- listed last?
  (remaining entries are zerofilled)
  (weirdly, most MM:SS:FF values are stored in byte[3..5] instead [7..9])
  (there are no point=A0h,A1h,A2h entries)
 Example TOC (GOOGLE_AI_TTS.PBP):
  01 00 01 00 02 00 00 00 00 00   ;Track 1 as audio
  01 00 02 00 02 30 00 00 00 00   ;Track 2 as audio, but without pregap?
  01 00 03 00 02 60 00 00 00 00   ;Track 3 as audio, but without pregap?
  01 00 04 00 03 15 00 00 00 00   ;Track 4 as audio, but without pregap?
  (remaining entries are zerofilled)
 Sector List:
  000h 4   Offset-110000h to Sector(N*10h)
  004h 2   Compressed size of Sector(N*10h+(0..0Fh))   ;9300h=uncompressed?
  006h 2   Zero (but, reportedly "usually 1... and 0 for the last entry")
  008h 10h Zero (but, reportedly "first 10h bytes of SHA1 sum of 10h sectors")
  018h 8   Zero (padding)
```
Data Compression is using raw Deflate (without any zlib headers or the like),
and it's unfortunately just compressing the sectors as-is (without filtering
out sector headers and ECC/EDC values).<br/>
[CDROM File Compression ZIP/GZIP/ZLIB (Inflate/Deflate)](compression.md#cdrom-file-compression-zipgzipzlib-inflatedeflate)<br/>
Audio Compression format is unknown:<br/>
```
  ?
```
Multi-disc format is unknown:<br/>
```
  ?
```
Retail files have "PGD" encryption:<br/>
```
  ?
```



##   CDROM Disk Images CHD (MAME)
All numbers are stored in Motorola (big-endian) byte ordering.<br/>

#### V1/V2 header (hdcomp):
V1/V2 contains harddisk related header entries (and apparently does't support
cdroms).<br/>
```
  000h 08h  ID "MComprHD" (MAME Compressed Hunks of Data)
  008h 4    Header size    (4Ch=V1, 50h=V2)
  00Ch 4    Header version (probably 01h=V1, 02h=V2)
  010h 4    Flags (bit0=DriveHasParent, bit1=AllowWrites)
  014h 4    Compression type (0=None, 1=ZLIB)
  018h 4    Number of sectors per hunk
  01Ch 4    Total number of hunks represented
  020h 4    Number of cylinders on hard disk
  024h 4    Number of heads on hard disk
  028h 4    Number of sectors on hard disk
  02Ch 10h  MD5 checksum on raw data
  03Ch 10h  MD5 checksum on parent file
  N/A  -    V1: Uses fixed 200h-byte Sector size
  04Ch (4)  V2: Number of bytes per sector
  ...  ?    Supposedly followed by map and/or data at whatever locations
```

#### V3/V4 header (chdman):
V3/V4 are inventing new "metadata" for info about harddisks or cdroms.<br/>
```
  000h 08h  ID "MComprHD" (MAME Compressed Hunks of Data)
  008h 4    Header size    (78h=V3, 6Ch=V4)
  00Ch 4    Header version (03h=V3, 04h=V4)
  010h 4    Flags (bit0=DriveHasParent, bit1=AllowWrites)
  014h 4    Compression type (0=None, 1=ZLIB, 2=ZLIB_PLUS) (V4: 3=AV)
  018h 4    Total number of hunks represented    (N)       (92h)
  01Ch 08h  Total size of all uncompressed hunks (N*2640h) (15D080h)
  024h 08h  Offset to the first blob of metadata
  02Ch 10h  V3: MD5 checksum on raw data                ;\
  03Ch 10h  V3: MD5 checksum on parent file             ;
  04Ch 4    V3: Number of bytes per hunk (2640h=990h*4) ; V3
  050h 14h  V3: SHA1 checksum on raw data               ;
  064h 14h  V3: SHA1 checksum on parent file            ;/
  02Ch 4    V4: Number of bytes per hunk (2640h=990h*4) ;\
  030h 14h  V4: SHA1 checksum on raw+meta               ; V4
  044h 14h  V4: SHA1 checksum on raw+meta of parent     ;
  058h 14h  V4: SHA1 checksum on raw data               ;/
  ...  N*10h Map entries (for each hunk)
  ...  10h   Map end marker ("EndOfListCookie",00h)
  ...  ..    Metadata Chunk(s)
  ...  ..    Compressed Sectors (aka hunks)
```

#### V5 header (chdman):
```
  000h 8    ID "MComprHD" (MAME Compressed Hunks of Data)
  008h 4    Header size    (7Ch=V5)
  00Ch 4    Header version (05h=V5)
  010h 4    Compressor 0 (usually "cdlz"=cdrom/lzma)
  014h 4    Compressor 1 (usually "cdzl"=cdrom/zlib)
  018h 4    Compressor 2 (usually "cdfl"=cdrom/flac)
  01Ch 4    Compressor 3 (usually 0=none)
  020h 8    Total size of all uncompressed hunks    (N*4C80h-HunkPadding)
  028h 8    Offset to Map                           (3D797h)
  030h 8    Offset to first Metadata chunk          (7Ch)
  038h 4    Number of bytes per hunk (512k maximum) (990h*8) (4C80h)
  03Ch 4    Number of bytes per sector              (990h)   (30h+60h)
  040h 14h  SHA1 on raw data
  054h 14h  SHA1 on raw+meta
  068h 14h  SHA1 on raw+meta of parent (0=No parent)
  ...  ..   Metadata Chunk(s)
  ...  ..   Padding to BytesPerHunk-boundary    ;\when uncompressed
  ...  ..   Uncompressed Sectors (aka hunks)    ;/
  ...  ..   Compressed Sectors (aka hunks)      ;-when compressed
  ...  ..   Map
```

#### CHD Metadata

##### V3/V4/V5 Metadata
Overall Metadata chunk format:<br/>
```
  000h 4   Chunk ID (aka Blob Tag) (eg. "CHT2" for each CDROM track)
  004h 1   Flags (00h=V3, 01h=V4/V5)  ;maybe some kind of flag/type/version?
  005h 3   Chunk Data Size (24bit)
  008h 8   Offset to next Chunk (or 0=Last chunk)
  010h ..  Chunk Data (eg. "TRACK:1 TYPE:MODE2_RAW ... POSTGAP:0",00h for CHT2)
```
There can be one or more chunks (eg. CHT2 chunk(s), one for each CDROM track).<br/>
```
  Summary of Chunk IDs and corresponding Data entries:
  ID_______Data_______________________________________________________
  "GDDD"   "CYLS,HEADS,SECS,BPS"         ;-hard disk standard info     ;\
  "IDNT"   ?                             ;-hard disk identify info     ; HDD
  "KEY "   ?                             ;-hard disk key info          ;/
  "CIS "   ?                             ;-pcmcia CIS info             ;-PCMCIA
  "CHCD"   94Ch-byte binary (4+99*24 bytes)                            ;\
  "CHTR"   "TRACK TYPE SUBTYPE FRAMES"                                 ; CD-ROM
  "CHT2"   "TRACK TYPE SUBTYPE FRAMES PREGAP PGTYPE PGSUB POSTGAP"     ;/
  "CHGT"   ?                                                           ;\Sega
  "CHGD"   "TRACK TYPE SUBTYPE FRAMES PAD PREGAP PGTYPE PGSUB POSTGAP" ;/GD-ROM
  "AVAV"   "FPS WIDTH HEIGHT INTERLACED CHANNELS SAMPLERATE"           ;\AV
  "AVLD"   ?   (A/V Laserdisc frame)                                   ;/
```

##### V3/V4/V5 Metadata in ASCII format
The ASCII items are separated by spaces as shown above (or commas for GDDD).<br/>
The last item in each chunk is terminated by 00h (at least so for CHTR/CHT2).<br/>
Most items are followed by a colon and decimal string (eg. TRACK:1), except,
TYPE,PGTYPE,SUBTYPE,PGSUB are followed by text strings (eg. TYPE:MODE2\_RAW).<br/>
```
  CYLS:#          Hard disc number of cylinders
  HEADS:#         Hard disc number of heads
  SECS:#          Hard disc number of sectors
  BPS:#           Hard disc bytes per sector
  TRACK:#         CDROM current track number (1..99)
  TYPE:string     CDROM sector type/size
  SUBTYPE:string  CDROM subchannel info (usually "NONE")
  FRAMES:#        CDROM number of sectors per track (with/without pregap?)
  PAD:#           Sega GDROM only: whatever pad value?
  PREGAP:#        CDROM ... maybe number of pregap sectors? (can be HUGE !!??)
  PGTYPE:string   CDROM ... whatever type?                  (usually "MODE1"??)
  PGSUB:string    CDROM ... whatever subchannel             (usually "RW"??)
  POSTGAP:#       CDROM ... maybe number of pstgap sectors? (usually 0)
  FPS:#.######    AV Video(?)-frames per second? with 6-digit fraction? (.avi?)
  WIDTH:#         AV Width      (maybe in pixels?)
  HEIGHT:#        AV Height     (maybe in pixels?) (with/without interlace?)
  INTERLACED:#    AV Interlace  (maybe a flag that might be maybe 0 or 1?)
  CHANNELS:#      AV Channels   (maybe audio mono/stereo or so?)
  SAMPLERATE:#    AV Samplerate (maybe audio samplerate, maybe in Hertz?)
 For SUBTYPE and PGSUB:
  "RW"      60h-byte interleaved   ;normal "cooked" 96 bytes per sector
  "RW_RAW"  60h-byte uninterleaved ;raw uninterleaved 96 bytes per sector
  "NONE"    0-byte                 ;no subcode data stored (default)
  (unknown how RAW and RW_RAW differ, one format does probably store 8 bits
  for 8 subchannels per byte... but unknown which format is doing so?)
 For TYPE and PGTYPE (and CHCD numeric type 0..7):
  "MODE1/2048" or "MODE1"                   CHCD=0  800h-byte ;\Data Mode1
  "MODE1/2352" or "MODE1_RAW"               CHCD=1  930h-byte ;/
  "MODE2/2336" or "MODE2"          ;\dupe?  CHCD=2  920h-byte ;\
  "MODE2/2336" or "MODE2_FORM_MIX" ;/       CHCD=5  920h-byte ;
  "MODE2/2048" or "MODE2_FORM1"             CHCD=3  800h-byte ; Data Mode2
  "MODE2/2324" or "MODE2_FORM2"             CHCD=4  914h-byte ;
  "MODE2/2352" or "MODE2_RAW" or "CDI/2352" CHCD=6  930h-byte ;/
  "AUDIO" (stored as big-endian samples!!!) CHCD=7  930h-byte ;-Audio CD-DA
```
Caution:<br/>
AUDIO sectors are conventionally stored as 16bit little-endian samples, but CHD
is storing them in big-endian (unlike formats like CUE/BIN).<br/>
Caution:<br/>
Older CHDMAN versions (eg. v0.146) did use nonsense "PGTYPE:MODE1" for all
tracks (including audio tracks), later versions (eg. v0.246) did fix that
issue; those newer files include a "V" prefix to indicate that the entry
contains "valid" info (eg. "PGTYPE:VAUDIO") (except, Track 1 keeps using
"PGTYPE:MODE1" without "V" and it's "MODE1" even on MODE2 discs).<br/>

##### CHCD Metadata (94Ch bytes, plus 10h-byte metadata header)
```
  000h 4     Number of tracks (N) (1..99)
  004h N*18h Track entries
  ...  ..    Zeropadding to 94Ch-byte size (when less than 99 tracks)
 Track entries:
  000h 4     Track Type       (0..7, CHCD=# in above table) (eg. 6=MODE2_RAW)
  004h 4     Subchannel Type  (0=RW, 1=RW_RAW, 2=None)
  008h 4     Sector Size      (800h, 914h, 920h or 930h)
  00Ch 4     Subchannel Size  (0 or 60h)
  010h 4     Number of Frames (aka number of sectors)
  014h 4     Padding Frames   (0..3) (to make Total Frames a multiple of 4)
```

#### CHD Maps

The Maps contain info (offset, size, compression method, etc.) for the separate
compression blocks.<br/>

##### V1/V2 map format (64bit entries with 44bit+20bit):
```
  44bit     Offset to compressed data
  20bit     Size of compressed data (or uncompressed data when size=hunksize)
```
Unknown if offset is in upper or lower 44bit.<br/>

##### V3/V4 map entries (per hunk):
```
  000h 8    Offset to compressed data  (64bit big-endian)
  008h 4    CRC32 on uncompressed data (32bit big-endian)
  00Ch 3    Size of compressed data    (24bit mixed-endian: Mid, Low, High)
  00Fh 1    Flags, indicating compression info (=whut? maybe below V34 stuff?)
```
V34\_MAP\_ENTRY\_FLAG\_TYPE\_MASK = 0x0f;     // what type of hunk<br/>
V34\_MAP\_ENTRY\_FLAG\_NO\_CRC    = 0x10;     // no CRC is present (which CRC?)<br/>
V3-V4 entry types<br/>
```
  V34_MAP_ENTRY_TYPE_INVALID        = 0  invalid type
  V34_MAP_ENTRY_TYPE_COMPRESSED     = 1  standard compression
  V34_MAP_ENTRY_TYPE_UNCOMPRESSED   = 2  uncompressed data
  V34_MAP_ENTRY_TYPE_MINI           = 3  mini: use offset as raw data
  V34_MAP_ENTRY_TYPE_SELF_HUNK      = 4  same as another hunk in this file
  V34_MAP_ENTRY_TYPE_PARENT_HUNK    = 5  same as a hunk in the parent file
  V34_MAP_ENTRY_TYPE_2ND_COMPRESSED = 6  compressed with secondary algorithm
```
Note: Secondary algorithm is NEVER used (it seems to have been intended for
FLAC CDDA, but that was apparently never actually implemented in V3/V4).<br/>
Blurp: Secondary algorithm is "usually FLAC CDDA" (unknown where that is
defined, and if one could also select other algorithms) ("usually FLAC" might
mean "always FLAC" for cdroms, and "not used" elsewhere).<br/>

##### V5 Map Formats
```
 V5 uncompressed map format (when [filehdr+10h]=00000000h):
  000h N*4  Hunk List (32bit offsets: Offset/BytesPerHunk) (usually 1,2,3..)
 V5 compressed map format (when [filehdr+10h]<>00000000h):
  000h 4    Length of compressed map
  004h 6    Offset of first block (48bit)     (E4h, after meta)
  00Ah 2    CRC16 on decompressed map entries
  00Ch 1    bits used to encode complength
  00Dh 1    bits used to encode self-refs
  00Eh 1    bits used to encode parent unit refs
  00Fh 1    Reserved for future use (probably zero)
  010h ..   Compressed Map entries (bitstream with Huffman/RLE encoding)
 The decompressed map entries should look as shown below (one could store them
 differently, eg. as 32bit little endian values; however, they must be stored
 exactly as shown below when computing the CRC16 on decompressed map entries):
  000h 1    Compression type (0..3=Codec0..3, 4=Uncompressed, 5=Self, 6=Parent)
  001h 3    Compressed length (24bit big-endian)
  004h 6    Offset to compressed data (48bit big-endian)
  00Ah 2    CRC16 on decompressed data (big-endian)
 V5 compression codecs:
  0,0,0,0 = CHD_CODEC_NONE        ;-unused (when using less than 4 codecs)
  "zlib" = CHD_CODEC_ZLIB         ;\
  "lzma" = CHD_CODEC_LZMA         ; general codecs
  "huff" = CHD_CODEC_HUFFMAN      ;
  "flac" = CHD_CODEC_FLAC         ;/
  "cdzl" = CHD_CODEC_CD_ZLIB      ;\
  "cdlz" = CHD_CODEC_CD_LZMA      ; general codecs with CD frontend
  "cdfl" = CHD_CODEC_CD_FLAC      ;/
  "avhu" = CHD_CODEC_AVHUFF       ;-A/V codecs
```

##### Uncompressed V5 Map loading (when [filehdr+10h]=00000000h)
```
  readfile(src,NumberOfHunks*4)                            ;\
  i=0                                                      ; load uncomoressed
  while i<NumberOfHunks                                    ; map (needed only
    ofs=bigendian32bit[src+i*4]*BytesPerHunk               ; for uncompressed
    byte[map+i*0Ch+00h]=04h             ;typ=Uncompressed  ; files, which can
    bigendian24bit[map+i*0Ch+01h]=BytesPerHunk             ; be created via
    bigendian48bit[map+i*0Ch+04h]=ofs                      ; chdman commandline
    bigendian16bit[map+i*0Ch+0Ah]=none  ;no crc            ; options)
    ofs=ofs+len, i=i+1                                     ;/
```

##### Compressed V5 Map loading (when [filehdr+10h]\<\>00000000h)
```
  readfile(hdr,10h)                                        ;\read map hdr and
  readfile(src,bigendian32bit[hdr+0])                      ; compressed map
  InitBitstream(src,BigEndianMsbFirst)                     ;/
  i=0                                                      ;\
  while i<10h                                              ;
    val=GetBits(4), num=1                                  ;
    if val=01h then                                        ; read huffman tree
      val=GetBits(4)                                       ;
      if val<>01h then num=GetBits(4)+3                    ;
    for j=1 to num, codesizes[i]=val, i=i+1                ;
  nonlzh_explode_tree(codetree,codesizes,10h)              ;/
  i=0, typ=0, num=0                                        ;\
  while i<NumberOfHunks                                    ;
    if num=0                                               ; load huffman coded
      x=GetHuffCode(codetree)                              ; map type values
      if x=07h then      ;COMPRESSION_RLE_SMALL            ;
        num=GetHuffCode(codetree)+03h                      ;
      elseif x=08h then  ;COMPRESSION_RLE_LARGE            ;
        num=GetHuffCode(codetree)*10h                      ;
        num=GetHuffCode(codetree)+num+13h                  ;
      else typ=x, num=1                                    ;
    byte[map+i*0Ch+0]=typ, i=i+1, num=num-1                ;/
  i=0, s=0, p=0             ;index,self,parent             ;\
  o=bigendian48bit[hdr+4]   ;offset                        ; load other
  while i<NumberOfHunks                                    ; map items
    typ=byte[map+i*0Ch+00h], ofs=o, len=0, crc=0           ;
    if typ<04h then len=GetBits([hdr+0Ch]), crc=GetBits(16);  ;Method 0..3
    elseif typ=04h then len=BytesPerHunk, crc=GetBits(16)  ;  ;Uncompressed
    elseif typ=05h then s=GetBits([hdr+0Dh]), ofs=s        ;  ;New Self
    elseif typ=06h then p=GetBits([hdr+0Eh]), ofs=p        ;  ;New Parent
    elseif typ=09h then typ=05h, ofs=s                     ;  ;Old Self
    elseif typ=0Ah then typ=05h, s=s+1, ofs=s              ;  ;Old Self+1
    elseif typ=0Bh then typ=06h, p=i*SectorsPerHunk, ofs=p ;  ;Direct Parent
    elseif typ=0Ch then typ=06h, ofs=p                     ;  ;Old Parent
    elseif typ=0Dh then typ=06h, p=p+SectorsPerHunk, ofs=p ;  ;Old Parent+1
    else goto error                                        ;
    byte[map+i*0Ch+00h]=typ                                ;
    bigendian24bit[map+i*0Ch+01h]=len                      ;
    bigendian48bit[map+i*0Ch+04h]=ofs                      ;
    bigendian16bit[map+i*0Ch+0Ah]=crc                      ;
    o=o+len, i=i+1                                         ;/
  if bigendian16bit[hdr+0Ah]<>noncrc16(map,i*0Ch) then error ;-final crc check
```
noncrc16: Uses the same polynomial as for CDROM subchannels, but with initial
value FFFFh (instead 0) and with final value left un-inverted (instead of
inverting it).<br/>
nonlzh\_explode\_tree: Uses the same concept as for LZH/ARJ huffman trees (it's
storing only the number of bits per each codes, and the codes are then
automatically assigned). But CHD is doing that backwards: It's starting with
the biggest codes (instead of smallest codes). For example, if you have three
codes with size 1, 2, 2. The traditional standard assignment would be 0, 10, 11.
But CHD is instead assigning them as 00, 01, 1.<br/>

#### CHD Compression

##### Compression V1-V4 format 0 (uncompressed)
##### Compression V5 0,0,0,0 (uncompressed)
```
  000h ..   Uncompressed data
```
Uncompressed format can be selected in CHD Map entries (per hunk), and in CHD
file header (per whole file).<br/>

##### Compression V1-V4 format 1 (zlib) (Generic Deflate)
##### Compression V1-V4 format 2 (zlib+) (Generic Deflate)
##### Compression V5 "zlib" (Generic Deflate)
```
  000h ..   Deflate-compressed data
```

##### Compression V5 "lzma" (Generic LZMA)
```
  000h ..   LZMA-compressed data (with lc=3, lp=0, pb=2) (without EOS end code)
```

##### Compression V5 "flac" (Generic FLAC)
```
  000h 1    Output format for 16bit samples ("L"=Little-endian, "B"=Big-endian)
  001h ..   FLAC-compressed data frame(s)
```

##### Compression V5 "huff" (Generic Huffman)
```
  000h ..   Huffman-compressed data (small tree, large tree, plus data)
```

##### Compression V5 "cdzl" (CDROM Deflate+Delate)
```
  000h ..   ECC Flags, (SectorsPerHunk+7)/8 bytes ;little-endian, bit0=1st flag
  ...  2/3  Size of compressed Data part (SIZ)    ;big-endian, 16bit or 24bit
  ...  SIZ  Deflate compressed Data part          ;uncompressed=930h*N bytes
  ...  ..   Deflate compressed Subchannel part    ;uncompressed=60h*N bytes
```

##### Compression V5 "cdlz" (CDROM LZMA+Deflate)
```
  000h ..   ECC Flags, (SectorsPerHunk+7)/8 bytes ;little-endian, bit0=1st flag
  ...  2/3  Size of compressed Data part (SIZ)    ;big-endian, 16bit or 24bit
  ...  SIZ  LZMA compressed Data part             ;uncompressed=930h*N bytes
  ...  ..   Deflate compressed Subchannel part    ;uncompressed=60h*N bytes
```

##### Compression V5 "cdfl" (CDROM FLAC+Deflate)
```
  000h ..   FLAC-compressed Data Frame(s)         ;uncompressed=930h*N bytes
  ...  ..   Deflate compressed Subchannel part    ;uncompressed=60h*N bytes
```

##### Compression V5 "avhu" (A/V mixup with Huffman and FLAC or so)
This isn't used on CDROMs and details are unknown/untested. It does reportedly
exist in different versions, and does combine different compression methods for
audio and video data.<br/>

##### Compression V4 format 3 (AV)
Unknown, maybe same/similar as "avhu".<br/>

##### Compression V3-V4 secondary compression method (FLAC CDDA)
CHD source code claims that V3-V4 maps support "FLAC CDDA", but it doesn't
actually seem to support that (audio discs compressed with chdman v0.145 are
merely using Deflate).<br/>

#### CHD Compression for CDROMs

##### CDROM "cdzl" and "cdlz"
If the sector's ECC flag is set:<br/>
```
  Fix the 0Ch-byte Sync mark at [000h..00Bh]
  Fix the 114h-byte ECC data at [81Ch..92Fh] in relation to Mode at [00Fh]
  Fixing just means to overwrite those values (there's no XOR-filter or so).
  CHD doesn't filter EDC values, MM:SS:FF:Mode Sector headers, nor  Subheaders.
```
The Size entry is 16bit (when N\*990h\<10000h) or 24bit (when
N\*990h\>=10000h), the size entry has no real purpose, however, it may be
useful for:<br/>
```
  decompressing the subchannel part without decompressing the whole data part,
  and for using libraries that don't return the end of the compressed data part
```

##### CDROM "cdfl"
There are no ECC flags (since Audio sectors don't have ECC).<br/>
There is no size entry (one must decompress the whole FLAC part to find the
begin of the Subchannel part).<br/>
The FLAC output is always stored in BIG-ENDIAN format (because CHD likes to use
big-endian for audio sectors, unlike formats like CUE/BIN).<br/>

##### CDROM Subchannel data
The Data part and Subchannel part must be interleaved after decompression (to
form 990h-byte sectors with 930h+60h bytes). The CHD map's CRC is then computed
on that interleaved data.<br/>
Most CHD files use metadata SUBTYPE:NONE which means that the 60h-byte
subchannel data is simply zerofilled and one must replace it by default
Index/Position values (AFTER the above CRC check). The CHD metadata lacks
accurate info about Index values; the PREGAP part is supposedly meant to have
Index=0 and the remaining sectors Index=1).<br/>
Although CHD files can contain subchannel data, CHDMAN has very limited support
for creating such files (the most practical way seems to be to convert
CCD/IMG/SUB to TOC/BIN and then convert that to CHD format).<br/>

#### CHD CDROM Sector Sizes

Decompressed CHD CDROM Sectors are always 990h bytes tall (930h+60h). However,
the Metadata TYPE/SUBTYPE entries may specify smaller sizes (corresponding to
the format of the original TOC/BIN or CUE/BIN image). CHD does arrange that
data as so:<br/>
```
  000h  Sector Data                    (800h, 914h, 920h or 930h bytes)
  ...   Subchannel Data                (0 or 60h bytes)
  ...   Zeropadding to 990h-byte size  (0..190h bytes)
```
That is somewhat okay for V3/V4 files, but involves two design mistakes that
conflict with the V5 format:<br/>
```
  - The ECC-Filter works only for 930h-byte sectors (920h does also contain
    ECC, but CHD can't filter that, resulting in very bad compression ratio)
  - The last 60h-byte are supposed to be Deflate-compressed Subchannel Data
    (but 800h..920h+60h sectors actually contain Zeropadding in that location)
```
Note: The CHD Map CRC checks are done on the above arrangement (including
zeropadding, and any prior ECC-unfiltering).<br/>
After the CRC check, one most relocate the Sector/Subchannel parts to their
actual locations (and replace zeropadding by actual Sync marks, header,
sub-header, ECC/EDC, and Subchannel data as needed).<br/>

#### CHD Compression Methods

##### Deflate
This is raw Deflate (despite of being called "zlib" in chd headers and source
code; there aren't any ZLIB headers nor Adler checksums). V1-V4 does
distinguish between "zlib" and "zlib+" (both are using normal Deflate) (V3/V4
are always using "zlib+") (the "+" does probably just mean that file was
compressed with improved compression ratio).<br/>
[CDROM File Compression ZIP/GZIP/ZLIB (Inflate/Deflate)](compression.md#cdrom-file-compression-zipgzipzlib-inflatedeflate)<br/>

##### LZMA
This contains a raw LZMA bitstream (without .lzma or .lz headers). The LZMA
bitstream starts with 8 ignored bits, if Normalization occurs after last
compression code, then it will also end with 8 ignored bits (those ignored bits
aren't CHD-specific, they do also occur in other LZMA-based formats).<br/>
[CDROM File Compression LZMA](compression.md#cdrom-file-compression-lzma)<br/>

##### FLAC
The data consists of raw FLAC Frames (without FLAC file header or FLAC metadata
blocks), the format is always signed 16bit/stereo (NumChannels=2
SampleDepth=16), the sample rate is don't care for compression purposes (the
FLAC Frame headers have it set to 09h=44100Hz).<br/>
Each FLAC Frame starts with a 14bit Sync mark (3FFEh), and ends with 16bit CRC.
There are usually several FLAC frames per CHD hunk (one must decompress all
FLAC frames, until reaching the decompressed hunk size).<br/>
Each FLAC Frame contains Left samples, followed by Right samples. After
decompression, CHD does store them in interleaved form (L,R,L,R,etc.)<br/>
[CDROM File Compression FLAC audio](compression.md#cdrom-file-compression-flac-audio)<br/>

##### Huffman
This is using some custom CHD-specific Huffman compression.<br/>
```
 decompress_chd_huffman_hunk:
  InitBitstream(src,BigEndianMsbFirst)                               ;-init
  codesizes[0..17h]=00h                     ;initially all unused    ;\
  codesizes[0]=GetBits(3)                   ;get first entry         ;
  i=GetBits(3)+1                            ;leading unused entries  ; small
 @@small_tree_lop:                                                   ; tree
  val=GetBits(3)                                                     ;
  if val=07h then goto @@small_tree_done    ;trailing unused entries ;
  codesizes[i]=val, i=i+1                   ;apply entry             ;
  if i<18h then goto @@small_tree_lop                                ;
 @@small_tree_done:                                                  ;
  nonlzh_explode_tree(codetree,codesizes,18h)                        ;/
  data=00h                                                           ;\
 @@large_tree_lop:                                                   ;
  val=GetHuffCode(codetree)-1               ;using small tree codes  ; large
  if val>=00h then                                                   ; tree
    data=val, codesizes[i]=data, i=i+1                               ;
  else                                                               ;
    len=GetBits(3)+2                                                 ;
    if len=7+2 then len=GetBits(8)+7+2                               ;
    for n=1 to len, codesizes[i]=datal, i=i+1                        ;
  if i<100h then goto @@large_tree_lop                               ;
  nonlzh_explode_tree(codetree,codesizes,100h)                       ;/
  for n=1 to decompressed_size                                       ;\data
    [dst]=GetHuffCode(codetree), dst=dst+1  ;using large tree codes  ;/
```

#### CHD Notes

##### Track/Hunk Padding and Missing Index0 sectors
A normal CDROM contains a series of sectors. The CHD format is violating that
in several ways: It's removing Index0/Pregap sectors, and it's instead
inserting dummy/padding sectors between tracks.<br/>
```
  Track        <---- Track1---------> <---- Track2---------> <--End-->
  Section      Index0 IndexN TrackPad Index0 IndexN TrackPad HunkPad
  Real Disc    Yes    Yes    -        Yes    Yes    -        -
  CHD Header   -      Yes    Yes      -      Yes    Yes      -
  CHD Data     -      Yes    Yes      -      Yes    Yes      Yes
```
That is, the critical parts are:<br/>
```
  Index0/pregap:  Metadata PREGAP:sectors isn't stored in compressed data
  Track padding:  Metadata FRAMES:sectors is rounded up to N*4 sectors
  Hunk padding:   The last hunk is additionally rounded up to hunksize
```
Missing Index0 might be a problem if a disc contains nonzero data between
tracks (like audio discs with applause in Index0 periods).<br/>
Track padding is total nonsense. The final hunk padding makes sense (but
confusingly that extra padding isn't included in the uncompressed size entry in
CHD header).<br/>

##### Parent references
Parent files are only used for writeable media like harddisks. The idea is to
store the original installation and operating system in a readonly Parent file,
and to store changes that file in a writeable Child file.<br/>
Unknown what determines which parent belongs to which child, and if parents can
be nested with other grandparents. Anyways, Parents aren't needed for CDROMs
(except, one could theoretically store CDROM patches in child files).<br/>

##### Self references
This can be used to reference to another identical hunk in the same file (eg.
zerofilled sectors or other duplicated data). There are some restrictions for
CDROMs: Data sector headers contain increasing sector numbers, so there won't
be any identical sectors. However, Audio sectors can be identical (unless they
are stored with subchannel info, which does also contain increasing sector
numbers).<br/>

##### Mini
Mini is only used in V3/V4 maps. It does apparently store the "data" directly
in the 8-byte Map offset field.<br/>
```
  XXX Unknown what kind of "data" that is
  (probably "normal compressed data", that happens to be 8 bytes or smaller).
```
Mini isn't used in V5 because the compressed V5 map doesn't contain any offset
fields (and things like zerofilled sectors could be as well encoded as Self
instead of Mini).<br/>

##### CHDMAN versions
CHD files can (cannot) be generated with the CHDMAN.EXE tool:<br/>
```
  chdman hdr meta  features/requirements/bugs/quirks/failures...
  v0.58  -   -     -   ;-CHD didn't exist in older MAME versions
  v0.59  V1  -     -   ;\
  v0.71  V2  -     -   ; supports harddisk CHD files only, not cdrom
  v0.78  V3  xxxx  -   ;/
  v0.81  V3  CHCD  bad ;-crashes after creating the CHD file header
  v0.90  V3  CHCD  ok  ;\
  v0.110 V3  CHCD  ok  ; requires cdrdao TOC/BIN as input (CUE/BIN does crash)
  v0.111 V3  CHTR  ok  ; (warning: BIN filenames may not contain space chars!)
  v0.112 V3  CHTR  bug ;    ;\works, but compression is somewhat bugged (files
  v0.118 V3  CHTR  bug ;    ;/are BIGGER instead of SMALLER after compression)
  v0.120 V3  CHTR  ok  ;
  v0.130 V3  CHTR  ok  ;
  v0.131 V4  CHTR  ok  ;/
  v0.140 V4  CHT2  ok  ;\requires "unicows.dll" (=Quintessential Media Player)
  v0.145 V4  CHT2  ok  ;/
  v0.146 V5  CHT2  bad ;\says output file already exists (crashes on -f force)
  v0.154 V5  CHT2  bad ;/
  v0.155 V5  CHT2  bad ;\crashes instantly (shortly before CreateEventW)
  v0.160 V5  CHT2  bad ;/
  v0.161 V5  CHT2  bad ;\says output file already exists (crashes on -f force)
  v0.169 V5  CHT2  bad ;/
  v0.170 V5  CHT2  bad ;\missing KERNEL32.DLL:AddVectoredExceptionHandler
  v0.217 V5  CHT2  bad ;/
  v0.218 V5  CHT2  bad ;\requires "newer version of windows" (64bit)
  v0.247 V5  CHT2  bad ;/
```
Note: The compression tool was originally called HDCOMP (V1/V2), and later
renamed to CHDMAN (V3/V4/V5).<br/>

##### References
CHD source code (see files cdrom.\*, chd\*.\*, etc):<br/>

<https://github.com/mamedev/mame/tree/master/src/lib/util>

CHDMAN commandline tool for generating chd files:<br/>

<https://github.com/mamedev/mame/blob/master/src/tools/chdman.cpp>

CHD decompression clone with useful comments:<br/>

<https://github.com/SnowflakePowered/chd-rs/tree/master/chd-rs/src>

CHD format reverse-engineering thread:<br/>

<http://www.psxdev.net/forum/viewtopic.php?f=70&t=3980>



##   CDROM Disk Images Other Formats
#### .ISO - A raw ISO9660 image (can contain a single data track only)
Contains raw sectors without any sub-channel information (and thus it's
restricted to the ISO filesystem region only, and cannot contain extras like
additional audio tracks or additional sessions). The image should start at
00:02:00 (although I wouldn't be surprised if some \<might\> start at
00:00:00 or so). Obviously, all sectors must have the same size, either 800h or
930h bytes (if the image contains only Mode1 or Mode2/Form1 sectors then 800h
bytes would usually enough; if it contains one or more Mode2/Form2 sectors then
all sectors should be 930h bytes).<br/>
Handling .ISO files does thus require to detect the image's sector size, and to
search the sector that contains the first ISO Volume Descriptor. In case of
800h byte sectors it may be additionally required to detect if it is a Mode1 or
Mode2/Form1 image; for PSX images (and any CD-XA images) it'd be Mode2.<br/>

#### .C2D
Something. Can contain compressed or uncompressed CDROM-images. Fileformat and
compression ratio are unknown. Also unknown if it allows random-access.<br/>
Some info on (uncompressed) .C2D files can be found in libmirage source code.<br/>

#### .ISZ - compressed ISO file with 800h-byte sectors (UltraISO)
This contains a compressed ISO filesystem, without supporting any CD-specific
features like Tracks, FORM2 sectors, or CD-DA Audio.<br/>

<http://www.ezbsystems.com/isz/iszspec.txt>

The format might be suitable for PC CDROMs, but it's useless for PSX CDROMs.<br/>


#### .MDX
Reportedly a "compressed" MDS/MDF file, supported by Daemon Tools.<br/>
Other info says that MDX is just MDS/MDF merged into a single file, without
mentioning any kind of "compression" support.<br/>
Basically... Daemon Tools is Adware that can merge MDS+MDF into one MDX file...
with additional Advertising?<br/>
However, the MDS+MDF format is completely different than MDX format:<br/>
```
  000h 10h  ID ("MEDIA DESCRIPTOR") (weirdly, same as in Alcohol .MDS)
  010h 2    Unknown (02h,01h) (maybe version or so)
  012h 1Ah  Copyright string (A9h," 2000-2015 Disc Soft Ltd.")
  02Ch 4    Unknown (FFFFFFFFh)
  030h 4    Offset to Unknown Footer (322040h) (N*800h+40h)
  034h 4    Unknown (0)
  038h 4    Unknown (B0h)
  03Ch 4    Unknown (0)
  040h N*800h  Sector Data
  322040h 270h Unknown (Advertising IDs? CRCs? Encrypted CUE sheet? Garbage?)
```


#### .CU2/.BIN
Custom format used by PSIO (an SD-card based CDROM-drive emulator connected to
PSX expansion port). The .CU2 file is somewhat intended to be smaller and
easier to parse than normal .CUE files, the drawback is that it's kinda
non-standard, and doesn't support INDEX and ADSR information. A sample .CUE
file looks as so:<br/>
```
  ntracks 3
  size      39:33:17
  data1     00:02:00
  track02   31:36:46
  track03   36:03:17
  ;(insert 2 blanks lines here, and insert 1 leading space in next line)
  trk end 39:37:17
```
All track numbers and MM:SS:FF values are decimal. The ASCII strings should be
as shown above, but they are simple ignored by the PSIO firmware (eg. using
"popcorn666" instead of "size" or "track02" should also work). The first track
should be marked "data1", but PSIO ignores that string, too (it does always
treat track 1 as data, and track 2-99 as audio; thus not supporting PSX games
with multiple data tracks). The "trk end" value should be equal to the "size"
value plus 4 seconds (purpose is unknown, PSIO does just ignore the "trk end"
value).<br/>
CU2 creation seems to require CDROM images in "CUE/BIN redump.org format" (with
separate BIN files for each track), the CUE is then converted to a CU3 file
(which is used only temporarily), until the whole stuff is finally converted to
a CU2 file (and with all tracks in a single BIN file). Tools like RD2PSIO (aka
redump2psio) or PSIO's own SYSCON.ZIP might help on doing some of those steps
automatically.<br/>
Alongsides, PSIO uses a "multidisc.lst" file... for games that require more
than one CDROM disc?<br/>

#### CD Image File Format (Xe - Multi System Emulator)
This is a rather crude file format, used only by the Xe Emulator. The files are
meant to be generated by a utility called CDR (CD Image Ripper), which, in
practice merely displays an "Unable to read TOC." error message.<br/>
The overall file structure is, according to "Xe User's Manual":<br/>
```
  header: 200h bytes header (see below)
  data:   990h bytes per sector (2352 Main, 96 Sub), 00:00:00->Lead Out
```
The header "definition" from the "Xe User's Manual" is as unclear as this:<br/>
```
  000h   00
  001h   00
  002h   First Track
  003h   Last Track
  004h   Track 1 (ADR << 4) | CTRL              ;\
  005h   Track 1 Start Minutes                  ; Track 1
  006h   Track 1 Start Seconds                  ;
  007h   Track 1 Start Frames                   ;/
  ...     ...                                   ;-Probably Further Tracks (?)
  n+0    Last Track Start Minutes               ;\
  n+1    Last Track Start Seconds               ; Last Track
  n+2    Last Track Start Frames                ;
  n+3    Last Track (ADR << 4) | CTRL           ;/
  n+4    Lead-Out Track Start Minutes           ;\
  n+5    Lead-Out Track Start Seconds           ; Lead-Out
  n+6    Lead-Out Track Start Frames            ;
  n+7    Lead-Out Track (ADR << 4) | CTRL       ;/
  ...    00
  1FFh   00
```
Unknown if MM:SS:FF values and/or First+Last Track numbers are BCD or non-BCD.<br/>
Unknown if Last track is separately defined even if there is only ONE track.<br/>
Unknown if Track 2 and up include ADR/Control (and if yes: where?).<br/>
Unknown if ADR/Control is really meant to be \<before\> MM:SS:FF on Track
1.<br/>
Unknown if ADR/Control is really meant to be \<after\> MM:SS:FF on
Last+Lead-Out.<br/>
Unknown if this format does have a file extension (if yes: which?).<br/>
Unknown if subchannel data is meant to be interleaved or not.<br/>
The format supports only around max 62 tracks (in case each track is 4 bytes).<br/>
There is no support for "special" features like multi-sessions, cd-text.<br/>
