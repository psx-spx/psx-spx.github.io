#   CDROM Video CDs (VCD)
VCDs are Video CDs with MPEG compression, yielding a playtime of 72 minutes per
disc (whole movies usually being stored on two CDs). VCDs are popular in asia
(as opposed to VHS tapes used in western world).<br/>

#### VCDs on Playstation
For the Playstation, the asian SCPH-5903 model includes a special daughterboard
with MPEG decoding hardware for playing VCDs.<br/>
[CDROM - Video CD Commands](cdromdrive.md#cdrom---video-cd-commands)<br/>
[Pinouts - VCD Pinouts](pinouts.md#pinouts---vcd-pinouts)<br/>
Without that hardware it has been widely believed to be impossible to play VCDs
on Playstations, although, as of 2017, it turned out that the Playstation's CPU
and MDEC decoder are fast enough for that purpose (when skipping B-frames,
rendering the movie in monochrome without colors, and reducing audio output to
11kHz/mono).<br/>

#### ISO Filesystem (Track 1)
[VCD ISO Basic Files (INFO, ENTRIES, AVSEQnn, ISO Filesystem)](cdromvideocdsvcd.md#vcd-iso-basic-files-info-entries-avseqnn-iso-filesystem)<br/>
[VCD ISO Playback Control PBC Files (PSD, LOT, ITEMnnnn)](cdromvideocdsvcd.md#vcd-iso-playback-control-pbc-files-psd-lot-itemnnnn)<br/>
[VCD ISO Search Files (SCANDATA, SEARCH, TRACKS, SPICONTX)](cdromvideocdsvcd.md#vcd-iso-search-files-scandata-search-tracks-spicontx)<br/>
[VCD ISO Misc files (CAPTnn, AUDIOnn, KARINFO, PICTURES, CDI)](cdromvideocdsvcd.md#vcd-iso-misc-files-captnn-audionn-karinfo-pictures-cdi)<br/>

#### MPEG Streams (Track 2 and up)
[VCD MPEG-1 Multiplex Stream](cdromvideocdsvcd.md#vcd-mpeg-1-multiplex-stream)<br/>
[VCD MPEG-1 Video Stream](cdromvideocdsvcd.md#vcd-mpeg-1-video-stream)<br/>
XXX MPEG-1 Macroblocks<br/>
[VCD MP2 Audio Stream](cdromvideocdsvcd.md#vcd-mp2-audio-stream)<br/>

#### VCD Versions & Variants
XXX<br/>



##   VCD ISO Basic Files (INFO, ENTRIES, AVSEQnn, ISO Filesystem)
#### Primary Volume Descriptor (00:02:16)
VCDs are having a standard ISO Primary Volume Descriptor, with some VCD
specific entries:<br/>
```
  008h 32  System Identifier (always "CD-RTOS CD-BRIDGE" for VCDs)
  028h 32  Volume Identifier (often nonsense, eg. "" or "__" or "VolumeLabel")
  23Eh 128 Application Identifier ("CDI/CDI_APPL.VCD;1" or "CDI/CDI_VCD.APP;1")
  400h 8   CD-XA Identifying Signature ("CD-XA001" for PSX and VCD)
```
There are some more differences to normal CDROMs:<br/>
```
  VCDs are using MODE2 (with 800h-byte and 914h-byte sectors)
  MPEG videos are on extra data tracks (outside of the ISO area on Track 1)
  Files in VCD or SVCD folders use fixed sectors numbers (00:04:00 and up)
  All 16bit/32bit values in files in VCD,SVCD,EXT,etc are BIG-ENDIAN
```
Due to the fixed sector numbers, VCDs players can completely ignore the ISO
filesystem with filenames and folders, and just address everything via sector
numbers (though accessing files in EXT and CDI folders seem to require using
the filesystem).<br/>

#### VCD\INFO.VCD or SVCD\INFO.SVD (00:04:00) (800h bytes, one sector)
```
  000h 8    ID "VIDEO_CD" for VCD (or "SUPERVCD"/"HQ-VCD  " for SVCD)
  008h 1    Version             ;Version Major (01h) (or 02h for VCD 2.0)
  009h 1    System Profile Tag  ;Version Minor (00h) (or 01h for VCD 1.1 or HQ)
  00Ah 16   Album ID/Desc (name in ASCII, padded with SPC) (usually empty)
  01Ah 2    Total Number of CDs in Album (1..N) ;\usually always 1,1 (even
  01Ch 2    Number of this CD in Album   (1..N) ;/for movies with 2 discs)
  01Eh 13   PAL Flags, 98x1bit, for each Track? (0=NTSC, 1=PAL)
  02Bh 1    InfoStatusFlags (see below)
 Below is usually zero-filled when not using PBC
  02Ch 4    Size of PSD.VCD file (or PSD.SVD?) (0=None)
  030h 3    First segment addr MM:SS:00 in BCD    (00:02:00 ???)
  033h 1    Offset Multiplier for "PsdOffset" values in PSD.VCD (must be 8)
  034h 2    Number of ListIDs in LOT.VCD file (1..7FFFh, plus 1 in some discs)
  036h 2    Number of ITEMnnnn.DAT files (plus nonsense in some discs?)
 Below is usually zero-filled (maybe exists on SVCD only?)
  038h 1980 SegmentContent[1..1980] (b0-1=Audio, b2-4=Video, b5=Cont, b6-7=OGT)
  7F4h 5*2  volume start time[0]: 5x16bit  ;aka playing_time[5] in seconds (?)
  7FEh 2    Reserved (0)
```
InfoStatusFlags at [02Bh] describes certain characteristics of the disc:<br/>
```
  bit0   Reserved, must be zero
  bit1-2 Restriction (0=No, 1..3=Restricted category 1..3) (eg. "not for kids")
  bit3   Special Information is encoded in the pictures, uh?
  bit4   MPEG User Data is used for Closed Caption (user_data_cc) (0=No, 1=Yes)
  bit5   Next Disc with PBC     (0=Start at ListID#1, 1=Start at ListID#2)
  bit6   Next Disc without PBC  (0=Start at Track #2, 1=Start at Track #3)
  bit7   Extended PBC available (0=No, 1=Yes... aka EXT\PSD_X exists?)
```
Note: Bit5/6 are used only if the next disc has the same Album ID (eg. the
feature allows to skip copyright messages if the same message was already shown
on another disc).<br/>
First\_segment\_addr: The location of the first sector of the Segment Play Item
Area [that is... the first ITEMnnnn.DAT file?], in the form mm:ss:00. Must be
00:00:00 if PSD size is zero. If PSD size is nonzero, but no segments used:
Usually set to 00:02:00.<br/>

#### VCD\ENTRIES.VCD or SVCD\ENTRIES.SVD (00:04:01) (800h bytes, one sector)
```
  000h 8     ID "ENTRYVCD" for VCD and SVCD (or "ENTRYSVD" for VCD30)
  008h 1     Version               ;\same as in INFO.VCD/SVD
  009h 1     System Profile Tag    ;/
  00Ah 2     Number of Entries/Chapters (1..500)
  00Ch 4*500 Entry[N] (Track 02h..99h, and MM:SS:FF) (all 4 bytes in BCD)
  7DCh 36    Reserved (0)
```
Version;<br/>
```
  0x02 --- VCD2.0
  0x01 --- SVCD, should be same as version in INFO.SVD
```
Sys\_prof\_tag;<br/>
```
  0x01 if VCD1.1
  0x00 else
```

#### MPEGAV\AVSEQnn.DAT (pointers to max 98 MPEG-1 Tracks, nn=01..98) (for VCDs)
#### MPEG2\AVSEQnn.MPG (pointers to max 98 MPEG-2 Tracks, nn=01..98) (for SVCDs)
#### MPEGAV\AVSEQnn.MPG (pointers to WHATEVER) (as so on some SVCDs or VCD30?)
These filesystem entries contain pointers to the video tracks (that is, outside
of the ISO area on Track 1).<br/>
Commercially made SVCDs can reportedly contain 7 folders: Autorun, Data, Ext,
Mpegav, Segment, Svcd and Vmp (ie. there's no MPEG2 folder on all SVCDs? though
that MPEGAV folder is said to contain a .MPG file instead of .DAT file).<br/>



##   VCD ISO Playback Control PBC Files (PSD, LOT, ITEMnnnn)
Playback Control (PBC) is an optional feature that allows to define menues,
pictures or text pages (whereas all those is internally just consisting of MPEG
compressed bitmaps; rather than of text characters).<br/>
Presence of the PBC feature is indicated by PSD.VCD filesize entry (in
INFO.VCD) being nonzero. PBC seems to be supported by most VCDs (except older
discs from around 1997), however, many VCDs are merely including a single
PlayList entry for the movie track, without any further menues/extras.<br/>

#### VCD\PSD.VCD or SVCD\PSD.SVD (00:04:34 and up) (max 256 sectors)
The Descriptors in this file can be considered as being "program code". The
program is usually stuck on "executing" the current descriptor (eg. playing a
movie, or showing a selection menu) without automatically increasing the
program counter. Actual program flow occurs only if the user presses a button
(or upon selection timeouts), causing the program to "goto" to a new PsdOffset.
And, something does probably happen upon end-of-track/item... maybe that does
automatically trigger the Next button handler?<br/>
```
<B> PsdPlayListDescriptor (14+2*N bytes):</B>
  00h 1   Type (10h=PlayList)
  01h 1   Number of Items (noi)     ;for Start-of-Movie and Numeric-Input?
  02h 2   ListID for this Descriptor (1..7FFFh)
  04h 2   PsdOffset for Prev button                 (FFFFh=Disable)
  06h 2   PsdOffset for Next button                 (FFFFh=Disable)
  08h 2   PsdOffset for Return/back button          (FFFFh=Disable)
  0Ah 2   Play time in 1/15s (=max 72.8 minutes) (or 0000h=full item)
  0Ch 1   Delay time in "1s/10s" units after ;<-- uh, after? after what?
  0Dh 1   Auto pause time in "1s/10s" units (used for each item in list if
          the auto pause flag in a sector is true) [WHAT is that? Trigger bit?]
  0Eh 2*N ItemID[N]  ;item number (0..599 or 1000..2979)
          Entry 0 is for "start of movie" (usually 0002h=Track 2)
          Entry 1..N-1 is for numeric input ?
<B> PsdSelectionListDescriptor (20+2*N bytes, or 36+6*N bytes):</B>
  00h      1   Type (18h=SELECTION_LIST, or 1Ah=EXT_SELECTION_LIST)
  01h      1   Flags (bit0=SelectionArea, bit1=CommandList, bit2-7=Reserved)
  02h      1   nos     <-- aka Number of Numeric-input selections ?
  03h      1   bsn     <-- ?
  04h      2   ListID for this Descriptor (1..7FFFh)
  06h      2   PsdOffset for Prev button
  08h      2   PsdOffset for Next button
  0Ah      2   PsdOffset for Return/back button
  0Ch      2   PsdOffset for Default button (uh, what is that?)
  0Eh      2   PsdOffset for Timeout
  10h      1   totime  <-- aka Timeout Time maybe? in WHAT units?
  11h      1   loop    <-- aka ?
  12h      2   itemid  <-- aka Item to be displayed during the selection?
  14h      2*N PsdOffset[N] for Numeric-input ?
 Below only for SVCDs (with Type=18h), or for Extended VCDs (with Type=1Ah):
 (14h+2*N) 4   Area for Prev    (x1,y1,x2,y2)  ;\these extra entries exist for
 (18h+2*N) 4   Area for Next    (x1,y1,x2,y2)  ; SVCDs with Type=18h, and
 (1Ch+2*N) 4   Area for Return  (x1,y1,x2,y2)  ; Extended VCDs with Type=1Ah
 (20h+2*N) 4   Area for Default (x1,y1,x2,y2)  ; (but do NOT exist for
 (24h+2*N) 4*N Area[N]          (x1,y1,x2,y2)  ;/older VCDs with Type=18h)
<B> PsdEndListDescriptor (8 bytes)</B>
  00h 1     Type (1Fh=EndList)
  01h 1     Next_disc   ;00h to stop PBC or NNh to switch to disc no NN (BCD!?)
  02h 2     Item (0 or 1000..2979, should be still image, eg. Change Disc pic)
  04h 4     Reserved (0)
  N/A -     This descriptor doesn't have a ListID (unlike as other descriptors)
<B> PsdCommandListDescriptor (5+2*N bytes)</B>
  00h 1     Type (20h=CommandList)
  01h 2     Command_count
  03h 2     ListID for this Descriptor (1..7FFFh)
  05h 2*N   command[EMPTY_ARRAY_SIZE]  ;uh, WHAT is a command?
<B> PsdAlignmentPadding (after each list entry)</B>
  00h 0..7  Padding to next 8-byte PsdOffset boundary (00h-filled)
```
Delay values in "1s/10s" units (for PlayList[0Ch,0Dh]):<br/>
```
  1..60   --> wait "N" seconds
  61..254 --> wait "(N-60)*10+60" seconds
  255     --> wait infinite
```
Item numbers (0..599 or 1000..2979) can be:<br/>
```
  0..1        - Play nothing
  2..99       - Play Track 2..99 (TOC tracks, for AVSEQnn.DAT and AUDIOnn.DAT?)
  100..599    - Play Entry 1..500 from table in ENTRIES file up to end of track
  600..999    - Reserved
  1000..2979  - Play SPI Segment Play Item 1..1980 (ITEMnnnn.DAT file)
  2980..65535 - Reserved
```
PsdOffset values can be:<br/>
```
  0..N   Offset within PSD.VCD file, in 8-byte units
  FFFDh  PSD_OFS_MULTI_DEF_NO_NUM ;\uh, what is that?
  FFFEh  PSD_OFS_MULTI_DEF        ;/
  FFFFh  PSD_OFS_DISABLED         ;-no function assigned to the button
```
For whatever reason, some PsdOffsets are specified as ListID (lid), these
ListID values must be translated to actual PsdOffset via the ListID Offset
Table (aka LOT.VCD/LOT.SVD file).<br/>

#### VCD\LOT.VCD or SVCD\LOT.SVD (00:04:02..33) (64Kbyte, 32 sectors)
The ListID Offset Table (LOT) allows to translate ListIDs to PsdOffsets. The
file is always 64Kbyte in size (unused entries should be set to FFFFh).<br/>
The PSD.VCD file does also assign ListIDs to each descriptor (ie. instead of
using the LOT.VCD file, one could also scan all descriptors in PSD.VCD when
searching a specific ListID).<br/>
```
  0000h 2       Reserved (0)
  0002h 2*7FFFh PsdOffset[1..7FFFh]  ;for ListID 1..7FFFh
```
Note: ListID#1 is used as entrypoint to PSD.VCD when inserting a new disc (or
when inserting another disc of the SAME movie, the entrypoint can be ListID#2,
depending on the Next Disc flag in INFO.VCD).<br/>

#### SEGMENT\ITEMnnnn.DAT (Pictures, Menu screens) (nnnn=0001..1980)
These files contain Pictures/Menu screens referenced from PSD.VCD. The files
seem to be stored in FORM2 sectors (not FORM1). Unknown if the files are
located on Track 1.<br/>
The content of the files seems to resemble short MPEG video clips (with only
one picture frame, or eventually with a few frames for short animations,
including audio in some cases). Still images are said to be allowed to use
twice the resolution of MPEG videos.<br/>

#### EXT\PSD\_X.VCD or EXT\PSD\_X.SVD (extended version of PSD.VCD)
#### EXT\LOT\_X.VCD or EXT\LOT\_X.SVD (extended version of LOT.VCD)
The "extended" files are often identical to the normal PSD/LOT files. The
difference is that, if disc uses SelectionLists, then PSD should use the normal
descriptor (18h), and PSD\_X should use the extended descriptor (1Ah), the
latter one seems to be intended to allow to highlight the current menu
selection (particulary useful when using +/- buttons instead of Numeric Keypad
input). Note: Nethertheless, Muppets from Space uses descriptor 18h in PSD\_X.<br/>
Unknown if SVCDs do really have "extended" files, too (theoretically the VCD
extension should be a default feature for SVCDs).<br/>

#### Playback Control Issues
Although PBC was intended as "nice extra feature", many VCDs are containing
faulty PSD files. In general, VCD players should either leave PBC unsupported
(or provide an option for disabling it).<br/>
Red Dragon from 2003 uses extended selection lists, but crops PSD\_X.VCD to the
same filesize as PSD.VCD.<br/>
Muppets from Space from 1999 assigns weird functions to Prev/Next buttons (Next
wraps from Last Track to First Track, but Prev doesn't wrap from First to Last;
default Non-PBC Prev/Next functions are more user friendly).<br/>
Sony's SCPH-5903 console refuses to display the HH:MM:SS playback time when
using PBC (instead it does only display a "PBC" logo).<br/>



##   VCD ISO Search Files (SCANDATA, SEARCH, TRACKS, SPICONTX)
Below files can help searching I-frames, and provide some info about the
content of Tracks and Segments.<br/>
Essentially, searching I-frames is possible without these files - however, if
present, then the files may be useful in two cases: For discs with variable
bitrates (which isn't allowed on VCDs though), and, for CDROM firmwares that
don't support "inaccurate" seeking (like telling it to start reading anywhere
NEAR some MM:SS:FF value, so one could skip sectors till reaching an I-frame)
(ie. if the firmware insists on a "accurate" seek position, then it's best to
give it a known I-frame address).<br/>

#### Caution: Overlapping Sectors (!?!)
Reportedly the new SVCD files TRACKS.SVD and SEARCH.DAT are on these sectors:<br/>
```
  TRACKS_SVD_SECTOR = (PSD_VCD_SECTOR+1)    ;aka 2nd sector in PSD.SVD?
  SEARCH_DAT_SECTOR = (TRACKS_SVD_SECTOR+1) ;aka 3rd..Nth sector in PSD.SVD?
```
If that's correct, then the files would overlap with PSD.SVD (when PSD.SVD is
bigger than one sector), that would be weird, but possible (ie. the "PsdOffset"
in PSD.SVD would need to "skip" the region used by those two files).<br/>

#### EXT\SCANDATA.DAT (12+3\*N bytes for VCD 2.0) (or 16+3\*N+2\*X+3\*Y+3\*Z for SVCD)
This file fulfills much the same purpose of the SEARCH.DAT file except that
this file is mandatory only if the System Profile Tag of the INFO.SVD file is
0x01 (HQ-VCD) and also that it contains sector addresses also for each video
Segment Play Items in addition to the regular MPEG tracks.<br/>
```
 SCANDATA.DAT Format for VCD 2.0 (12+3*N bytes):
  000h 8    ID "SCAN_VCD"
  008h 1    Version (02h for VCD 2.0)
  009h 1    Reserved (0)
  00Ah 2    Number of scan points (in 0.5s units) (max FFFFh = ca. 9.1 hours)
  00Ch 3*N  Scan Point[0..N-1]  ;MM:SS:FF of closest I-frame
 SCANDATA.DAT Format for SVCD (16+3*N+2*X+3*Y+3*Z bytes):
  000h 8    ID "SCAN_VCD"
  008h 1    Version (01h for SVCD)
  009h 1    Reserved (0)
  00Ah 2    scandata_count ;number of 3-byte entries in the table
  00Ch 2    track_count    ;number of MPEG tracks on disc
  00Eh 2    spi_count      ;number of consecutively recorded play item segments
                           ; (as opposed to the number of segment play items).
  010h 3*N  msf_t cum_playtimes[N]  ;cumulative playing time up to track N.
                                    ; (track time just wraps at 99:59:74)
  xxxh 2*X  spi_indexes[X]          ;Indexes into the following scandata table
  xxxh 2    mpegtrack_start_index   ;Index into the following scandata table
                                    ; (where the MPEG track scan points start)
  xxxh 3*Y  The scandata table... [Y]  ;8bit Track Number and 16bit Index
                uint8_t  track_num;      /* Track number as in TOC
                uint16_t table_offset;   /* Index into scandata table
  xxxh 3*Z  msf_t scandata_table[Z]  ;MM:SS:FF
```

#### SVCD\SEARCH.DAT (13+3\*N bytes)
This file defines where the scan points are. It covers all mpeg tracks
together. A scan point at time T is the nearest I-picture in the MPEG stream to
the given time T. Scan points are given at every half-second for the entire
duration of the disc.<br/>
```
  000h 8    ID "SEARCHSV"
  008h 1    Version (01h)
  009h 1    Reserved (0)
  00Ah 2    Number of scan points
  00Ch 1    Time_interval (in units of 0.5 seconds) (must be 01h)
  00Dh 3*N  Scan Point[0..N-1]  ;MM:SS:FF of closest I-frame
```
Note: This SVCD file is about same as the old EXT\SCANDATA.DAT file on VCDs
(with one extra entry for Time Interval). Whilst, SVCDs are storing some
different stuff in EXT\SCANDATA.DAT (despite of the identical filename).<br/>

#### SVCD\TRACKS.SVD (11+4\*N bytes) (or rarely:11+5\*N bytes)
The TRACKS.SVD file contains a series of structures, one for each track, which
indicates the track's playing time (in sectors, not actually real time) and
contents.<br/>
SVCD\TRACKS.SVD is a mandatory file which describes the numbers and types of
MPEG tracks on the disc.<br/>
```
 SVCD\TRACKS.SVD Format for SVCD (11+4*N bytes):
  000h 8   ID "TRACKSVD"
  008h 1   Version (01h)
  009h 1   Reserved (0)
  00Ah 1   Number of MPEG tracks (N)
  00Bh 3*N Track playing_time[N]  (MM:SS:FF, in BCD)(in sectors, not real time)
  0xxh 1*N TrackContent[N]  ;bit0-1=Audio,bit2-4=Video,bit5=Reserved,bit6-7=OGT
 SVCD\TRACKS.SVD Format for VCD30 (11+5*N bytes) (some sort of SVCD-prototype):
  000h 8   ID "TRACKSVD"
  008h 1   Version (01h)
  009h 1   Reserved (0)
  00Ah 1   Number of MPEG tracks (N)
  00Bh 5*N Cum_Playing_time and Content (MM:SS:FF in BCD, and OGT, Audio)
```

#### SVCD\SPICONTX.SVD (1000h bytes, two sectors)
Unknown if/when/where/why this file exists, possibly only on VCD30?<br/>
Note: The same info can be stored in INFO.SVD at offsets [038h..7F3h].<br/>
```
  0000h 8       ID "SPICONSV"
  0008h 1       Version (01h)
  0009h 1       Reserved (0)
  000Ah 2*1980  Segment Content[1..1980] (1st byte=OGT, 2nd byte=Audio)
  0F82h 126     Reserved (0)
```

#### Content Flags for Segments and Tracks
For SVCD\INFO.SVD and SVCD\TRACKS.SVD (on SVCD) these are encoded in 1 byte:<br/>
```
  bit0-1  Audio characteristics:
            0 = No MPEG audio stream
            1 = One MPEG1 or MPEG2 audio stream without extension
            2 = Two MPEG1 or MPEG2 audio streams without extension
            3 = One MPEG2 multi-channel audio stream with extension
  bit2-4  Video characteristics:
            In TRACKS.SVD this must be 0,3,7 (no still pictures)
            0 = No MPEG video data
            1 = NTSC still picture
            2 = NTSC Reserved (NTSC still pic hires?)
            3 = NTSC motion picture
            4 = Reserved
            5 = PAL still picture
            6 = PAL Reserved (PAL still pic hires?)
            7 = PAL motion picture
  bit5    Indicates segment is continuation of an item
            In TRACKS.SVD this must be 0 (reserved)
            0 = First or only segment of item
            1 = Second or later segment of item
  bit6-7  Overlay Graphics/Text (OGT):
            0 = No OGT substream
            1 = Sub-stream 0 available
            2 = Sub-stream 0 & 1 available
            3 = All OGT sub-substreams available
```
For SPICONTX.SVD and SVCD\TRACKS.SVD (on VCD30) these are encoded in 2 bytes:<br/>
```
  1st byte = Audio characteristics        ;\probably same values as
  2nd byte = Overlay Graphics/Text (OGT)  ;/in above bitfields?
```



##   VCD ISO Misc files (CAPTnn, AUDIOnn, KARINFO, PICTURES, CDI)
#### EXT\CAPTnn.DAT (Closed Caption data, aka subtitles) (SVCD only?)
VCDs with subtitles are usually/always having the subtitles encoded directly in
the picture frames (ie. in the MPEG macroblocks, rather than using the Closed
Caption feature).<br/>
These CAPTnn.DAT files are intended for Closed Captions (eg. subtitles in
different languages and/or for deaf people).<br/>
Alternately, the "user\_data\_cc" flag in INFO.VCD?/INFO.SVD can indicate to
store Closed Captions in MPEG User Data (with START\_CODE=000001B2h=User Data)
instead of in EXT\CAPTnn.DAT. Either way, the format of those Closed Captions
is unknown.<br/>
Moreover, Content can be flagged to have Overlay Graphics/Text (OGT), whatever
that is: it might be related to Closed Captions.<br/>
Note: Reportedly CAPTnn.DAT can exist on VCDs and SVCDs (although the same
person reported that VCDs do not support subtitles, so that info sounds wrong).<br/>

#### CDDA\AUDIOnn.DAT (pointers to uncompressed CD Audio Tracks)
These filesystem entries contain pointers to uncompressed audio tracks tracks
(that is, outside of the ISO area on Track 1).<br/>
Most VCDs don't have audio tracks (though some VCDs do contain empty CDDA
folders).<br/>
Maybe the feature is occassionally used the other way around: Music discs
containing VCD clips as bonus feature?<br/>

#### KARAOKE\KARINFO.xxx (whatever)
The KARAOKE folder exists on many VCDs (about 50%), but it's usually/always
empty on all discs.<br/>
Reportedly the folder can contain "KARINFO.xxx" files, but the purpose/format
of that files is unknown.<br/>
Reportedly there are Midi VCDs (MVCDs) for karaoke, maybe those discs have
"KARINFO.xxx" files(?)<br/>

#### PICTURES\\*.\* (whatever)
Unknown purpose. The PICTURES folder has been spotted on one VCD (Wallace and
Gromit), but the folder was just empty.<br/>

#### CDI\\*.\* (some kind of GUI/driver for Philips CDI Players)
The CDI folder is some relict for Philips CDI Players, it isn't used by normal
VCD players, however, the CDI folder & files are included on most or all
VCDs.<br/>
The path/name for the CDI executable is stored at offset 23Eh in the ISO
Primary Volume Descriptor (usually "CDI/CDI\_APPL.VCD;1" or "CDI/CDI\_VCD.APP;1")
(or accidentally "CDI\_CDI\_VCD.APP;1" on homebrew Nero discs).<br/>
The files in the CDI folder are usually just some standard files (without any
customizations), however, there are some different revisions of these files:<br/>
```
<B> Revision A (spotted on two discs from 1997 and 1999):</B>
  CDI_APPL.VCD   80702 bytes, 04-Mar-1996, CRC32=AE8FC5D0h  ;executable
  VCD_BACK.DYV   92572 bytes, 18-Jul-1995, CRC32=00693E5Eh  ;whatever?
  VCD_BTN.C8     93719 bytes, 18-Jul-1995, CRC32=FF0A636Ah  ;whatever?
<B> Revision B (spotted on a disc from 2003):</B>
  CDI_VCD.APP    20648 bytes, 00-Nul-0000  CRC32=DC885F70h  ;executable
  CDI_FONT.FNT  145388 bytes, 00-Nul-0000  CRC32=FB4D63F4h  ;font?
  CDI_ALL.RTF        ? bytes,              CRC32=?          ;realtimefile?
  CDI_BUM.RTF        ? bytes,              CRC32=?          ;realtimefile?
<B> Revision C (spotted on a disc from 2006, and homebrews from 2001 and 2017):</B>
  CDI_VCD.APP   102400 bytes, 00-Nul-0000  CRC32=E91E128Dh  ;executable
  CDI_VCD.CFG      193 bytes, 00-Nul-0000  CRC32=D1C6F7ADh  ;config/ascii
  CDI_TEXT.FNT   13616 bytes, 00-Nul-0000  CRC32=BDC55E86h  ;font?
  CDI_IMAG.RTF 1510028 bytes, 00-Nul-0000  CRC32=(RIFF)     ;realtimefile?
```
CDI\_VCD.CFG is some ASCII text file (with uncommon 0Dh,0Dh,0Ah line breaks),
the file could be customized to change things like GUI colors, but most or all
discs seem to contain the same file with CRC32=D1C6F7ADh. Note: The CFG file is
missing on the homebrew DemoVCD.<br/>
CDI\_IMAG.RTF is seen as 1510028 byte file under windows (that is, with a
windows RIFF header, and with data area containing the whole 930h bytes from
each sector; this includes the MM:SS:FF values from the sector header, so the
RTF file may look slightly different depending on which sectors it has been
stored on, although the files are usually exactly same apart from those
MM:SS:FF values). Note: The RTF file is cropped to 1324220 bytes (instead of
1510028) on the homebrew DemoVCD (apart from that, the file is same as normal).<br/>
CDI\_ALL.RTF and CDI\_BUM.RTF cannot be read/copied under Windows 7 (which is
weirdly reporting them to use an "invalid MS-DOS function"; some people also
reported having CDI\_IMAG.RTF files with similar problems). The reason is
unknown, maybe windows doesn't fully support the CD filesystem, or some VCDs
are violating the filesystem specs, or whatever... maybe windows is
mis-identifying certain RTF files as Rich Text Format files and tries to
prevent virus-infections by throwing a faked "MS-DOS" error message.<br/>



##   VCD MPEG-1 Multiplex Stream
#### Multiplex Stream & Sector Boundaries
The Multiplex stream is some higher level stream, intended to help to
distinguish between Audio- and Video-streams (which are enclosed in the
Multiplex stream). MPEG's are somewhat organized in "sectors", with sector size
varying for normal .mpg files and VCDs:<br/>
```
  VCD discs   --> Sector Size = 914h bytes (the discs MODE2/FORM2 sector size)
  .mpg files  --> Sector Size = 800h bytes (regardless of physical sector size)
```
Sectors are always beginning with a Multiplex Packet (and Multiplex Packets are
never crossing sector boundaries). If the amount of video data exceeds the
sector size, then it's split into several Multiplex packets, whereas, that may
happen anywhere in the video stream (ie. there can be Multiplex Headers
occurring even in the middle of Video packet).<br/>

#### MPEG-1 Multiplex Pack (sector header) (12 bytes)
The Pack Header is found at the begin of the stream (on VCDs, it's also found
at the begin of each sector). The SCR values might help on identifying the
current playback position, and, with the bitrate value, this could be also used
to compute the distance to another position (though there are other ways to
determine the position/bitrate, so the Pack is kinda useless).<br/>
```
 32bit PACK_START_CODE (000001BAh)                                      ;-4byte
  2bit Fixed (00b for MPEG-1) (would be 01b for MPEG-2)                 ;\
  2bit Fixed (10b)                                                      ;
  3bit System Clock Reference, bit32-30  ;\                             ;
  1bit Marker (1)                        ; System Clock Reference (SCR) ;
 15bit System Clock Reference, bit29-15  ; (intended Time,              ; 5byte
  1bit Marker (1)                        ; in 90kHz clock cycles)       ;
 15bit System Clock Reference, bit14-0   ;/                             ;
  1bit Marker (1)                                                       ;/
  1bit Marker (1)                                                       ;\
 22bit Multiplex Rate (total bitrate of the stream, in 400bit/s units)  ; 3byte
  1bit Marker (1)                                                       ;/
```

#### MPEG-1 Multiplex System Header (12+N\*3 bytes)(optionally)(at start of stream)
The System Header is usally found after the first Pack at the begin of the
stream.<br/>
```
 32bit SYSTEM_HEADER_START_CODE (000001BBh)                             ;\6byte
 16bit Header Length minus 6 (in bytes) (0006h+N*3)                     ;/
  1bit Marker (1)                                                       ;\
 22bit Rate bound (max multiplex rate of all packs in the stream,       ; 3byte
  1bit Marker (1)                              in 400bit/s units)       ;/
  6bit Audio Bound (max number of audio streams in this ISO stream)     ;\
  1bit Fixed Flag (1=Fixed bitrate)                                     ; 1byte
  1bit CSPS Flag  (1=Constrained)                                       ;/
  1bit System Audio Lock Flag  XXX                                      ;\
  1bit System Video Lock Flag  XXX                                      ; 1byte
  1bit Marker (1)                                                       ;
  5bit Video Bound (max number of video streams in this ISO stream)     ;/
  8bit Reserved (FFh)                                                   ;-1byte
```
Followed by N\*3 bytes for the streams (each with first bit=set):<br/>
```
  8bit Stream ID (C0h..DFh=Audio, E0h..EFh=Video)                       ;\
  2bit Fixed (11b)                                                      ; 3byte
  1bit STD buffer scale (0=Mul128/audio, 1=Mul1024/video)               ;
 13bit STD buffer size  (largest required buffer over all packets)      ;/
```
Terminated by a value with first bit=cleared (eg. next 000001xxh value).<br/>

#### MPEG-1 Multiplex Video/Audio/Special Packets (7..24 bytes, plus data)
These packets are encapsulating the lower-level Video/Audio streams.<br/>
```
  32bit  START (000001xxh BDh-BFh=Special, C0h-DFh=Audio, E0h-EFh=Video);\6byte
  16bit  Packet Length minus 6 (in bytes) (1..18, plus data)            ;/
```
If (and while) next two bits are 11b (0..16 padding bytes):<br/>
```
  (2bit) Fixed (11b, indicates presence of stuffing)       ;\optional 0..16byte
  (6bit) Fixed (111111b)                                   ;/
```
If next two bits are 01b (buffer size info):<br/>
```
  (2bit) Fixed (01b, indicates presence of buffer size)        ;\
  (1bit) STD Buffer Scale (0=Mul128/audio, 1=Mul1024/video)    ; optional 2byte
 (13bit) STD Buffer Size (for decoding, in above scale units)  ;/
```
Always:<br/>
```
   2bit  Fixed (00b, indicates no further stuffing/buffer info);\
   1bit  PTS Flag (Presentation Time Stamp)                    ; 0.5 bytes
   1bit  DTS Flag (Decoding Time Stamp)                        ;/
```
If PTS Flag set:<br/>
```
  (3bit) Presentation Time Stamp, bit32-30       ;\
  (1bit) Marker (1)                              ; optional 4.5 bytes
 (15bit) Presentation Time Stamp, bit29-15       ; (time when to output the
  (1bit) Marker (1)                              ; the packet to audio/video
 (15bit) Presentation Time Stamp, bit14-0        ; hardware, in 90kHz cycles)
  (1bit) Marker (1)                              ;/
```
If DTS Flag set (in this case PTS Flag must be also set):<br/>
```
  (4bit) Fixed (0001b)                           ;\
  (3bit) Decoding Time Stamp, bit32-30           ; optional 5 bytes
  (1bit) Marker (1)                              ; (recommended time when
 (15bit) Decoding Time Stamp, bit29-15           ; to decode the block,
  (1bit) Marker (1)                              ; in 90kHz cycles)
 (15bit) Decoding Time Stamp, bit14-0            ;
  (1bit) Marker (1)                              ;/
```
If PTS and DTS Flags are both zero:<br/>
```
  (4bit) Fixed (1111b)                           ;-optional 0.5 bytes
```
Always:<br/>
```
  ...  packet data bytes                         ;-data...(not crossing sector)
```
Note: The first Multiplex Video Packet would usually start with a Sequence
Header Code (000001B3h), and the first Multiplex Audio Packet should always
start with an Audio Sync Word (FFFh).<br/>
However, the size of the Multiplex packets does usually differ from the size of
the packets in the audio/video stream, so new Multiplex Packets may occur
anywhere in the middle of those streams (eg. in the middle of a video slice,
the next Multiplex Video packet would then begin with the remaining slice
bytes, rather than with a 000001xxh code; it's also possible that a Multiplex
Audio packet gets inserted in the middle of the video slice).<br/>
The best (or easiest) way to get continous data for the lower level streams
might be to memcopy the data from Multiplex packets to separate Audio &
Video buffers.<br/>

#### MPEG-1 Multiplex End Code (4 bytes)
```
 32bit END_CODE (000001B9h)                                             ;-4byte
```
This should occur at the end of the video. On a VCD it does also occur at the
end of each video track.<br/>



##   VCD MPEG-1 Video Stream
The Video stream is part of the Multiplex stream, meaning that the Video
packets preceeded (and interrupted) by Multiplex headers. Ie. before processing
the Video packets, one must first extract the video snippets from the Multiplex
stream (see previous chapter).<br/>

#### MPEG-1 Video Sequence Header (12, 76, or 140 bytes, ie. 12+N\*64)
```
  32bit SEQUENCE_HEADER_CODE (000001B3h)                        ;-4byte
  12bit Width in pixels  (1..4095)                              ;\3byte
  12bit Height in pixels (1..2800, for max AFh slices)          ;/
   4bit Aspect Ratio (01h..0Eh, see below)                      ;\1byte
   4bit Framerate    (01h..08h, see below)                      ;/
  18bit Bitrate (in 400bit/s units, 3FFFFh=variable rate)       ;\
   1bit Marker (1)                                              ; 3byte
  10bit VBV (required decoding memory size, in "16 kB" units)   ; +6bit
   1bit Constrained Parameter Flag                              ;/
   1bit Load Intra Q Matrix      (0=No, use Standard Matrix, 1=Yes, Custom)
```
Next 64byte only when above bit was set:<br/>
```
 (64byte) Intra Quantizer Matrix (64 x 8bit, unsigned) (in zigzag order)
   1bit Load Non-Intra Q Matrix  (0=No, use Standard Matrix, 1=Yes, Custom)
```
Next 64byte only when above bit was set:<br/>
```
 (64byte) Non-Intra Quantizer Matrix (64 x 8bit, unsigned) (in zigzag order)
```
Aspect Ratio values:<br/>
```
  0     -       ;forbidden
  1     1.0     ;square pixels
  2     0.6735  ;0.6735
  3     0.7031  ;16:9, 625 line, PAL
  4     0.7615  ;0.7615
  5     0.8055  ;0.8055
  6     0.8437  ;16:9, 525 line, NTSC
  7     0.8935  ;0.8935
  8     0.9157  ;4:3, 625 line, PAL, CCIR601
  9     0.9815  ;0.9815
  10    1.0255  ;1.0255
  11    1.0695  ;1.0695
  12    1.0950  ;4:3, 525 line, NTSC, CCIR601
  13    1.1575  ;1.1575
  14    1.2015  ;1.2015
  15    -       ;reserved
```
Frame Rate values:<br/>
```
  0     -                     ;forbidden
  1     23.976 (24000/1001)   ;NTSC encapsulated film rate
  2     24.0                  ;Standard international cinema film rate
  3     25.0                  ;PAL  video frame rate (625/50)
  4     29.97  (30000/1001)   ;NTSC video frame rate
  5     30.0                  ;NTSC video frame rate drop-frame (525/60)
  6     50.0                  ;PAL  double frame rate/progressive
  7     59.94  (60000/1001)   ;NTSC double frame rate
  8     60.0                  ;NTSC double frame rate drop-frame
  9-15  -                     ;reserved
```

#### MPEG-1 Video Group of Pictures (GOP) (8 bytes) XXX...
```
 32bit GROUP_START_CODE (000001B8h)
  1bit Drop Frame (1=drop this frame; for reducing 30 fps to 29.97 fps)
  5bit Time Code Hours   (0..23)
  6bit Time Code Minutes (0..59)
  1bit Marker (1)
  6bit Time Code Seconds (0..59)
  6bit Time Code Picture (0..59)
  1bit Closed GOP
  1bit Broken Link
```

#### MPEG-1 Video Picture Header XXX...
```
  32bit  PICTURE_START_CODE (00000100h)                           ;\
  10bit  Temporal Reference (display order, 0..3FFh)              ; 61bit
   3bit  Coding Type (0=Invalid, 1=I, 2=P, 3=B, 4=D, 5-7=Reserved);
  16bit  VBV Delay (in 90kHz cycles, FFFFh=variable bitrate)      ;/
```
If Coding Type is 2 or 3 (P-Frame or B-Frame):<br/>
```
  (1bit) full fel forward vector   (0=half pix, 1=full pix)     ;\optional 4bit
  (3bit) forward f code            (0=invalid, 1..7=0..6bits)   ;/
```
If Coding Type is 3 (B-Frame):<br/>
```
  (1bit) full backward vector                                   ;\optional 4bit
  (3bit) backward f code                                        ;/
```
If (and while) next bit is set:<br/>
```
  (1bit) Fixed (1, indicates presence of Extra Info)            ;\opt. N*9bit
  (8bit) Extra Information                                      ;/
```
End of Extra:<br/>
```
   1bit  Fixed (0, indicates no further Extra Info)             ;-1bit
 0-7bit  Padding to byte boundary (0)                           ;-0..7bit
```
Coding Type values:<br/>
```
  0  Forbidden
  1  I - Intra Coded                      (full image)
  2  P - Predictive Coded                 (based on prev I or P frame)
  3  B - Bidirectionally Predictive Coded (based on prev+next I or P frame)
  4  D - DC Intra Coded                   (don't care, lowres thumbnail)
  5  Reserved
  6  Reserved
  7  Reserved
```

#### Frame Order
```
  DISPLAY ORDER:
  I B B B P B B B P B B B P B B B I B B B P B B B P B B B P B B B ...
  |       |_______|_______|       |       |_______|_______|
  |               |               |               |
  I-Frame         P-frames        I-Frame         P-frames
```
The B-fames require to know the next P- (or I-) frame in advance, for that
reason, the frames are stored as "PBBB" (although being played as "BBBP"):<br/>
```
  STORAGE ORDER:
  I P B B B P B B B P B B B I B B B P B B B P B B B P B B B ...
  | |_______|_______|       |       |_______|_______|
  |         |               |               |
  I-Frame   P-frames        I-Frame         P-frames
```

#### MPEG-1 Video Slice
Slices are containing the actual 16x16 pixel Macro Blocks. Usually a Slice
contains one horizontal line - although, theoretically, it could be longer or
shorter, ie. a slice could wrap to next line, or a line could be split into
several slices (with the leading "MBA Increment" value greater than 1 to define
the horizontal start offset).<br/>
```
  32bit  PACK_START_CODE (000001xxh; xx=01h..AFh; vertical index) ;-4byte
   5bit  Quantizer Scale (1..31) (may be later changed by blocks) ;-5bit
```
If (and while) next bit is set:<br/>
```
  (1bit) Fixed (1, indicates presence of Extra Info)              ;\opt. N*9bit
  (8bit) Extra Information                                        ;/
```
End of Extra:<br/>
```
   1bit  Fixed (0, indicates no further Extra Info)               ;-1bit
```
If (and while) next 23bit are nonzero (ie. until next 000001xxh):<br/>
```
   ...   Macroblock (within horizontal line)                      ;...
```
Final padding:<br/>
```
 0-7bit  Padding to byte boundary (0)                             ;-0..7bit
```

#### MPEG-1 Video Group/Sequence Extension Data (reserved)
#### MPEG-1 Video User Data (optional)
```
 32bit START_CODE (000001B2h=User Data, 000001B5h=Extension Data)       ;-4byte
   ... data (end is signaled by presence of next 000001xxh code)        ;-data
```
User Data can contain Closed Captions (see flag in VCD\INFO.VCD or
SVCD\INFO.SVD).<br/>
User Data contains 11h-byte "Created with Nero" in some homebrew discs.<br/>

#### MPEG-1 Video Sequence End Code (4 bytes)
```
  32bit SEQUENCE_END_CODE (000001B7h)                                   ;-4byte
```




#### MPEG-1 Video 4:2:0 Macroblock
```
         N*11bit  Macroblock_address_increase escape/stuffing codes (if any)
         1..11bit Macroblock_address_increase
         1-6bit   Macroblock_type
         5bit     Quantizer_scale
         ...      Motion_vector
         3-9bit   Coded_block_pattern
         ...      Block(i)
```
Aka...<br/>
```
  Addr Incr
  Type
  Motion Vector
  QScale
  CBP
  Block b0 (Y1)
  Block b1 (Y2)
  Block b2 (Y3)
  Block b3 (Y4)
  Block b4 (Cb)
  Block b5 (Cr)
```




##   VCD MP2 Audio Stream
VCD video discs and .mpg movie files are having the MP2 Audio Stream enclosed
in the Multiplex stream (whilst .mp2 audio files may contain raw MP2 data
without Multiplex stream).<br/>

Each MP2 frame is starting with a FFFh syncword (which is always located on a
byte boundary). Unfortunately, the value FFFh can also occur anywhere in the
audio data (eg. a 16bit sample with value 3FFCh).<br/>
So, when starting mid-stream, one will need some guessing when searching a
valid syncword. The best method is to compute the frame size (based on the
supposed frame header), and then to check if supposed frame begins AND ends
with a sync word. Moreover, one could check for invalid sample rate values in
the frame header, or invalid "groupings" in the frame's data part.<br/>
VCDs are conventionally having three audio frames encoded in one CDROM sector,
so the first syncword can be simply found right after the multiplex packet
header (though that might differ in some cases: VCD2.0 allows different audio
bitrates, and a CDROM sector could be theoretically shared for Audio and Video
data).<br/>

#### Overall MP2 Frame Format
```
  Header (32bit)
  Optional CRC (16bit) (or 0bit if none)
  Allocation Information
  Scale Factor Selector Information
  Scale Factors
  Data
```

#### MP2 Header
```
  12bit Syncword (FFFh)                                         ;\
  1bit  Revision (0=MPEG-2, 1=MPEG-1)                           ; 2 bytes
  2bit  Layer (2=Audio LayerII)                                 ;
              (3=LayerI, 1=LayerIII, r3=reserved)               ;
  1bit  Protection_bit (1=no crc)                               ;/
  4bit  Bitrate_index (1..14)                                   ;\
          (0=free format, 15=reserved)                          ;
  2bit  Sampling_frequency                                      ; 1 byte
  1bit  Padding_bit                                             ;
  1bit  Private_bit                                             ;/
  2bit  Mode                                                    ;\
  2bit  Mode_extension (aka bound)                              ;
  1bit  Copyright                                               ; 1 byte
  1bit  Original/home                                           ;
  2bit  Emphasis                                                ;/
```

#### MP2 Checksum (optional)
```
 16bit CRC
```

#### Allocation Information
#### Scale Factor Selector Information
#### Scale Factors
#### Data
```
  XXX...
```



##   Inflate
Inflate/Deflate is a common (de-)compression algorithm. In the PSX world, it's
used by the .CDZ cdrom-image format.<br/>

[Inflate - Core Functions](cdromvideocdsvcd.md#inflate---core-functions)<br/>
[Inflate - Initialization & Tree Creation](cdromvideocdsvcd.md#inflate---initialization--tree-creation)<br/>
[Inflate - Headers and Checksums](cdromvideocdsvcd.md#inflate---headers-and-checksums)<br/>



##   Inflate - Core Functions
#### tinf\_uncompress(dst,src)
```
 tinf_init()                    ;init constants (needed to be done only once)
 tinf_align_src_to_byte_boundary()
 repeat
  bfinal=tinf_getbit()          ;read final block flag (1 bit)
  btype=tinf_read_bits(2)       ;read block type (2 bits)
  if btype=0 then tinf_inflate_uncompressed_block()
  if btype=1 then tinf_build_fixed_trees(), tinf_inflate_compressed_block()
  if btype=2 then tinf_decode_dynamic_trees(), tinf_inflate_compressed_block()
  if btype=3 then ERROR         ;reserved
 until bfinal=1
 tinf_align_src_to_byte_boundary()
 ret
```

#### tinf\_inflate\_uncompressed\_block()
```
 tinf_align_src_to_byte_boundary()
 len=LittleEndian16bit[src+0]                             ;get len
 if LittleEndian16bit[src+2]<>(len XOR FFFFh) then ERROR  ;verify inverse len
 src=src+4                                                ;skip len values
 for i=0 to len-1, [dst]=[src], dst=dst+1, src=src+1, next i    ;copy block
 ret
```

#### tinf\_inflate\_compressed\_block()
```
 repeat
  sym1=tinf_decode_symbol(tinf_len_tree)
  if sym1<256
   [dst]=sym1, dst=dst+1
  if sym1>256
   len  = tinf_read_bits(length_bits[sym1-257])+length_base[sym1-257]
   sym2 = tinf_decode_symbol(tinf_dist_tree)
   dist = tinf_read_bits(dist_bits[sym2])+dist_base[sym2]
   for i=0 to len-1, [dst]=[dst-dist], dst=dst+1, next i
 until sym1=256
 ret
```

#### tinf\_decode\_symbol(tree)
```
 sum=0, cur=0, len=0
 repeat                         ;get more bits while code value is above sum
  cur=cur*2 + tinf_getbit()
  len=len+1
  sum=sum+tree.table[len]
  cur=cur-tree.table[len]
 until cur<0
 return tree.trans[sum+cur]
```

#### tinf\_read\_bits(num)     ;get N bits from source stream
```
 val=0
 for i=0 to num-1, val=val+(tinf_getbit() shl i), next i
 return val
```

#### tinf\_getbit()           ;get one bit from source stream
```
 bit=tag AND 01h, tag=tag/2
 if tag=00h then tag=[src], src=src+1, bit=tag AND 01h, tag=tag/2+80h
 return bit
```

#### tinf\_align\_src\_to\_byte\_boundary()
```
 tag=01h   ;empty/end-bit (discard any bits, align src to byte-boundary)
 ret
```



##   Inflate - Initialization & Tree Creation
#### tinf\_init()
```
 tinf_build_bits_base(length_bits, length_base, 4, 3)
 length_bits[28]=0, length_base[28]=258
 tinf_build_bits_base(dist_bits, dist_base, 2, 1)
 ret
```

#### tinf\_build\_bits\_base(bits,base,delta,base\_val)
```
 for i=0 to 29
  bits[i]=min(0,i-delta)/delta
  base[i]=base_val
  base_val=base_val+(1 shl bits[i])
 ret
```

#### tinf\_build\_fixed\_trees()
```
 for i=0 to 6, tinf_len_tree.table[i]=0, next i       ;[0..6]=0   ;len tree...
 tinf_len_tree.table[7,8,9]=24,152,112                ;[7..9]=24,152,112
 for i=0 to 23,  tinf_len_tree.trans[i+0]  =i+256, next i  ;[0..23]   =256..279
 for i=0 to 143, tinf_len_tree.trans[i+24] =i+0,   next i  ;[24..167] =0..143
 for i=0 to 7,   tinf_len_tree.trans[i+168]=i+280, next i  ;[168..175]=280..287
 for i=0 to 111, tinf_len_tree.trans[i+176]=i+144, next i  ;[176..287]=144..255
 for i=0 to 4, tinf_dist_tree.table[i]=0, next i   ;[0..4]=0,0,0,0,0 ;\dist
 tinf_dist_tree.table[5]=32                        ;[5]=32           ; tree
 for i=0 to 31, tinf_dist_tree.trans[i]=i, next i  ;[0..31]=0..31    ;/
 ret
```

#### tinf\_decode\_dynamic\_trees()
```
 hlit  = tinf_read_bits(5)+257           ;get 5 bits HLIT (257-286)
 hdist = tinf_read_bits(5)+1             ;get 5 bits HDIST (1-32)
 hclen = tinf_read_bits(4)+4             ;get 4 bits HCLEN (4-19)
 for i=0 to 18, lengths[i]=0, next i
 for i=0 to hclen-1                      ;read lengths for code length alphabet
  lengths[clcidx[i]]=tinf_read_bits(3)   ;get 3 bits code length (0-7)
 tinf_build_tree(code_tree, lengths, 19) ;build code length tree
 for num=0 to hlit+hdist-1               ;decode code lengths for dynamic trees
  sym = tinf_decode_symbol(code_tree)
  len=1, val=sym                         ;default (for sym=0..15)
  if sym=16 then len=tinf_read_bits(2)+3, val=lengths[num-1] ;3..6 previous
  if sym=17 then len=tinf_read_bits(3)+3, val=0              ;3..10 zeroes
  if sym=18 then len=tinf_read_bits(7)+11, val=0             ;11..138 zeroes
  for i=1 to len, lengths[num]=val, num=num+1, next i
 tinf_build_tree(tinf_len_tree,  0,      hlit)    ;\build trees
 tinf_build_tree(tinf_dist_tree, 0+hlit, hdist)   ;/
 ret
```

#### tinf\_build\_tree(tree, first, num)
```
 for i=0 to 15, tree.table[i]=0, next i     ;clear code length count table
 ;scan symbol lengths, and sum code length counts...
 for i=0 to num-1, x=lengths[i+first], tree.table[x]=tree.table[x]+1, next i
 tree.table[0]=0
 sum=0          ;compute offset table for distribution sort
 for i=0 to 15, offs[i]=sum, sum=sum+tree.table[i], next i
 for i=0 to num-1  ;create code to symbol xlat table (symbols sorted by code)
  x=lengths[i+first], if x<>0 then tree.trans[offs[x]]=i, offs[x]=offs[x]+1
 next i
 ret
```

#### tinf\_data
```
 clcidx[0..18] = 16,17,18,0,8,7,9,6,10,5,11,4,12,3,13,2,14,1,15   ;constants
```

```
 typedef struct TINF_TREE:
   unsigned short table[16]     ;table of code length counts
   unsigned short trans[288]    ;code to symbol translation table
```

```
 TINF_TREE tinf_len_tree   ;length/symbol tree
 TINF_TREE tinf_dist_tree  ;distance tree
 TINF_TREE code_tree       ;temporary tree (for generating the dynamic trees)
 unsigned char lengths[288+32]   ;temporary 288+32 x 8bit ;\for dynamic tree
 unsigned short offs[16]         ;temporary 16 x 16bit    ;/creation
```

```
 unsigned char  length_bits[30]
 unsigned short length_base[30]
 unsigned char  dist_bits[30]
 unsigned short dist_base[30]
```



##   Inflate - Headers and Checksums
#### tinf\_gzip\_uncompress(void \*dest, \*destLen, \*source, sourceLen)
```
 src_start=src, dst_start=dst                 ;memorize start addresses
 if (src[0]<>1fh or src[1]<>8Bh) then ERROR   ;check id bytes
 if (src[2]<>08h) then ERROR                  ;check method is deflate
 flg=src[3]                                   ;get flag byte
 if (flg AND 0E0h) then ERROR                 ;verify reserved bits
 src=src+10                                                 ;skip base header
 if (flg AND 04h) then src=src+2+LittleEndian16bit[src]     ;skip extra data
 if (flg AND 08h) then repeat, src=src+1, until [src-1]=00h ;skip file name
 if (flg AND 10h) then repeat, src=src+1, until [src-1]=00h ;skip file comment
 hcrc=(tinf_crc32(src_start, src-src_start) & 0000ffffh))   ;calc header crc
 if (flg AND 02h) then x=LittleEndian16bit[src], src=src+2  ;get header crc
 if (flg AND 02h) then if x<>hcrc then ERROR                ;verify header
 tinf_uncompress(dst, destLen, src, src_start+sourceLen-src-8)  ;----> inflate
 crc32=LittleEndian32bit[src], src=src+4   ;get crc32 of decompressed data
 dlen=LittleEndian32bit[src], src=src+4    ;get decompressed length
 if (dlen<>destLen) then ERROR                              ;verify dest len
 if (crc32<>tinf_crc32(dst_start,dlen)) then ERROR          ;verify crc32
 ret
```

#### tinf\_zlib\_uncompress(dst, destLen, src, sourceLen)
```
 src_start=src, dst_start=dst         ;memorize start addresses
 hdr=BigEndian16bit[src], src=src+2   ;get header
 if (hdr MOD 31)<>0 then ERROR        ;check header checksum (modulo)
 if (hdr AND 20h)>0 then ERROR        ;check there is no preset dictionary
 if (hdr AND 0F00h)<>0800h then ERROR ;check method is deflate
 if (had AND 0F000h)>7000h then ERROR ;check window size is valid
 tinf_uncompress(dst, destLen, src, sourceLen-6)      ;------> inflate
 chk=BigEndian32bit[src], src=src+4                   ;get data checksum
 if src-src_start<>sourceLen then ERROR               ;verify src len
 if dst-dst_start<>destLen then ERROR                 ;verify dst len
 if a32<>tinf_adler32(dst_start,destLen)) then ERROR  ;verify data checksum
 ret
```

#### tinf\_adler32(src, length)
```
 s1=1, s2=0
 while (length>0)
  k=max(length,5552)
  for i=0 to k-1, s1=s1+[src], s2=s2+s1, src=src+1, next i
  s1=s1 mod 65521, s2=s2 mod 65521, length=length-k
 return (s2*10000h+s1)
```



