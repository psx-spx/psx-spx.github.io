#   Video Streaming and BS Compression

##   CDROM File Video STR Streaming and BS Picture Compression (Sony)
#### STR Files (movie streams)
[CDROM File Video Streaming STR (Sony)](#cdrom-file-video-streaming-str-sony)<br/>
[CDROM File Video Streaming STR Variants](#cdrom-file-video-streaming-str-variants)<br/>
[CDROM File Video Streaming Framerate](#cdrom-file-video-streaming-framerate)<br/>
[CDROM File Video Streaming Audio](#cdrom-file-video-streaming-audio)<br/>
[CDROM File Video Streaming Chunk-based formats](#cdrom-file-video-streaming-chunk-based-formats)<br/>
[CDROM File Video Streaming Mis-mastered files](#cdrom-file-video-streaming-mis-mastered-files)<br/>
Apart from the 20h-byte STR headers, movies basically consist of a series of BS
files (see below).<br/>

#### BS Files (Huffman compressed MDEC codes)
BS stands for bitstream, which might refer to the use in STR files, or to the
Huffman bitstreams.<br/>
[CDROM File Video BS Compression Versions](#cdrom-file-video-bs-compression-versions)<br/>
[CDROM File Video BS Compression Headers](#cdrom-file-video-bs-compression-headers)<br/>
The header is followed by the bitstream...<br/>
```
  v1/v2/v3/ea/iki --> first bit in bit15 of first halfword (good for psx)
  v0              --> first bit in bit7 of first byte (not so good for psx)
  (to use the same decoder for all version: swap each 2 bytes in v0)
```
For each block, the bitstream contains one DC value, up to 63 AC values,
terminated by EOB (end of block).<br/>
[CDROM File Video BS Compression DC Values](#cdrom-file-video-bs-compression-dc-values)<br/>
[CDROM File Video BS Compression AC Values](#cdrom-file-video-bs-compression-ac-values)<br/>
Apart from being used in STR movies, BS can be also used to store single
pictures:<br/>
[CDROM File Video BS Picture Files](#cdrom-file-video-bs-picture-files)<br/>

#### Wacwac (similar as BS, but with completely different Huffman codes)
[CDROM File Video Wacwac MDEC Streams](#cdrom-file-video-wacwac-mdec-streams)<br/>

#### Credits
Thanks to Michael Sabin for info on various STR and BS variants:<br/>
<https://github.com/m35/jpsxdec/>




##   CDROM File Video Streaming STR (Sony)
#### .STR Sectors (with 20h-byte headers) (for MDEC Movies, or User data)
```
  000h 2    StStatus (0160h) (RV6Rh; R=Reserved=0, V=Version=1, 6=Fixed ID)
  002h 2    StType (0000h..7FFFh=User Defined, 8000h..FFFFh=System; 8001h=MDEC)
  004h 2    StSectorOffset (Sector number in the frame, 0=First)
  006h 2    StSectorSize   (Number of sectors in the frame) (eg. 4 or 5)
  008h 4    StFrameNo      (Frame number, 1=First) (except Viewpoint=0)
  00Ch 4    StFrameSize    (in bytes, in this frame, excluding headers/padding)
 When StType=0000h..7FFFh:
  010h 10h  StUser         (user defined data)
  020h 7E0h User data      (more user defined data)
 When StType=8001h=MDEC (the only system defined type) (with StStatus=0160h):
  010h 2    StMovieWidth                  (eg. 0140h)
  012h 2    StMovieHeight                 (eg. 00F0h)
  014h 4    StHeadM (reserved for system) (eg. 38000720h) ;\same as [020h-027h]
  018h 4    StHeadV (reserved for system) (eg. 00020001h) ;/from 1st STR sector
  01Ch 4    Unspecified                   (eg. 00000000h) (except Viewpoint<>0)
  020h 7E0h Data (in BS format) (or padding, when image is smaller than frame)
```
The default file extension .STR is used by various games (though some games use
other extensions, the .FMV files in Tomb Raider do also contain standard
20h-byte .STR sector headers).<br/>

#### Video Frames
The video frames consist of BS compressed images (that is, all sectors have STR
headers at 000h..01Fh, and the first sector of each frame does additionally
contain a standard BS fileheader at offset 020h..027h).<br/>
```
  See "CDROM File Video BS Compression" chapters
```
Less common, there is also a format for streaming polygon animations instead of
BS compressed bitmaps:<br/>
[CDROM File Video Polygon Streaming](#cdrom-file-video-polygon-streaming)<br/>

#### STR Resolution
The Width/Height entries are almost always multiples of 16 pixels. But there
are a few exceptions:<br/>
```
  Height=260 (104h) in Star Wars Rebel Assault II, NTSC (S1\L01_PLAY.STR)
  Height=200 (0C8h) in Perfect Assassin (DATA.JFS\CDV\*.STR)
  Height=40  (028h) in Gran Turismo 1 (TITLE.DAT\*, MagDemo10 and MagDemo15)
  Width=232  (0E8h) in Gran Turismo 1 (TITLE.DAT\*, MagDemo10 only)
```
For such videos, the width/height of MDEC decompression buffer in RAM must be
rounded up to multiples of 16 pixels (and the decompressed picture should be
cropped to the STR header width/height before forwarding it to VRAM).<br/>
Note: The extra scanlines are usually padded with the bottom-most scanline
(except, Gran Turismo 1 has gray-padding in lower/right pixels). Ideally, one
would repeat the bottom-most pixels in zigzag order.<br/>

#### Subtitles
Metal Gear Solid MGS\ZMOVIE.STR contains subtitles as text strings: The first
sector of the .STR file is something custom (without STR header), the remaining
movie consists of STR sectors with StType=0001h for subtitles and StType=8001h
for picture frames.<br/>
Unknown if other games are using the same method, or other methods.<br/>
Obviously, subtitles could be also displayed as part of the compressed image,
but text strings are much smaller, have better quality, and would also allow to
support multiple languages.<br/>



##   CDROM File Video Streaming STR Variants
#### STR ID Values
```
  2-byte  0160h         ;Standard STR header
  1-byte  01h           ;Ace Combat 3 Electrosphere
  4-byte  "SMJ",01h     ;Final Fantasy 8, Video
  4-byte  "SMN",01h     ;Final Fantasy 8, Audio/left
  4-byte  "SMR",01h     ;Final Fantasy 8, Audio/righ
  4-byte  0000000xh     ;Judge Dredd
  4-byte  DDCCBBAAh     ;Crusader: No Remorse, older Electronic Arts
  4-byte  08895574h     ;Chunk header in 1st sector only, Best Sports (demo)
  4-byte  "VLC0"        ;Chunk header in 1st sector only, newer Electronic Arts
  4-byte  "VMNK"        ;Chunk header in 1st sector only, Policenauts
  4-byte  01h,"XSP"     ;Sentient header in 1st sector only
  N-byre  zero(es)      ;Polygons? (in last 150Mbyte of PANEKIT.STR)
```

#### STR Type values (for videos that do have STR ID=0160h):
The official definition from Sony's File Formats document is as so;<br/>
```
  0000h..7FFFh=User Defined
  8000h..FFFFh=System (with 8001h=MDEC being the only officially defined type)
```
In practice, the following values are used (of which, 8001h is most common).<br/>
```
  0000h=Polygon Video, Wacwac as Polygon Stream
  0000h=Polygon Video?, Army Men Air Attack 2 (MagDemo40: AMAA2\*.PMB)
  0000h=MDEC Video, Alice in Cyberland
  0001h=MDEC Video, Ridge Racer Type 4 (PAL version, 320x176 pix)
  0001h=Whatever extra data for XA-ADPCM streams (Bits Laboratory games)
  0001h=Whatever non-audio waverform? (3D Baseball)
  0001h=Subtitles, Metal Gear Solid MGS\ZMOVIE.STR
  0002h=Software-rendered video (without using MDEC/GTE) (Cyberia)
  0002h=MDEC Video, Wacwac with IntroTableSet
  0003h=MDEC Video, Wacwac with EndingTableSet
  0004h=MDEC Video, Final Fantasy 9 (MODE2/FORM2)
  0008h=SPU-ADPCM, AKAO audio (Final Fantasy 9)
  0000h=SPU-ADPCM, AKAO audio (Chrono Cross Disc 1, Legend of Mana)
  0001h=SPU-ADPCM, AKAO audio (Chrono Cross Disc 1, Legend of Mana)
  0100h=SPU-ADPCM, AKAO audio (Chrono Cross Disc 2)
  0101h=SPU-ADPCM, AKAO audio (Chrono Cross Disc 2)
  0000h=Whatever special, channel 0 header (Nightmare Project: Yakata)
  0400h=Whatever special, channel 1 header (Nightmare Project: Yakata)
  0001h=Whatever special, channel 0 data   (Nightmare Project: Yakata)
  0401h=Whatever special, channel 1 data   (Nightmare Project: Yakata)
  5349h=MDEC Video, Gran Turismo 1 and 2 (with BS iki)
  0078h=MDEC Ending Dummy  (Mat Hoffman's Pro BMX (MagDemo48: MHPB\SHORT.STR)
  5673h=MDEC Leading Dummy (Mat Hoffman's Pro BMX (MagDemo48: MHPB\SHORT.STR)
  8001h=MDEC Video, Standard MDEC (most common type value)
  8001h=Polygon Video (Ape Escape) (same ID as standard MDEC)
  8001h=Eagle One: Harrier Attack various types (MDEC and other data)
  8001h=Dance series SPU-ADPCM streaming (with STR[1Ch]=DDCCBBAAh)
  8101h=MDEC Video, Standard MDEC plus bit8=FlagDisc2 (Chrono Cross Disc 2)
```

#### Leading XA-ADPCM
Most movies start with STR video sectors. But a few games start with XA-ADPCM:<br/>
```
  Ace Combat 3 Electrosphere (*.SPB)
  Alice in Cyber Land (*.STR)
  Judge Dredd (*.IXA) ;and very small 4-byte STR header
  ReBoot (MOVIES\*.WXA)
```
Also, Aconcagua (Wacwac) has XA-ADPCM before Video (but, yet before that, it
has 150 leading zerofilled sectors).<br/>
Also, Porsche Challenge (SRC\MENU\STREAM\\*.STR) starts with corrupted
Subheaders, which may appear as leading XA-ADPCM (depending on how to
interprete the corrupted header bits).<br/>

#### Leading SPU-ADPCM
```
  EA videos     ;\
  Crusader      ; chunks
  Policenauts   ;/
  AKAO videos
```

#### Metal Gear Solid (MGS\ZMOVIE.STR, 47Mbyte)
This is an archive dedicated to STR movies (with number of frames instead of
filesize entries). Metal Gear Solid does also have cut-scenes with polygon
animations (but those are supposedly stored elsewhere?).<br/>
```
  000h 4    Number of entries (4)
  004h N*8  File List
  ...  ..   Zerofilled
```
File List entries:<br/>
```
  000h 2    Unknown... decreasing values?
  002h 2    Number of Frames (same as last frame number in STR header)
  004h 4    Offset/800h (to begin of STR movie, with subtiltes in 1st sector)
```
Disc 1 has four movies: The first one has a bit more than 12.5 sectors/frame,
the other three have a bit more than 10 sectors/frame (eg. detecting the
archive format could be done checking for entries wirh 8..16 sectors/frame).<br/>
Example, from Disc 1:<br/>
```
  04 00 00 00
  ED 97 9E 01  01 00 00 00 ;num sectors=1439h ;div19Eh=C.81h ;97EDh-6137h=36B6h
  37 61 86 01  3A 14 00 00 ;num sectors=0F41h ;div186h=A.03h ;6137h-38D0h=2867h
  D0 38 10 03  7B 23 00 00 ;num sectors=1EA1h ;div310h=A.00h ;38D0h-2302h=15CEh
  02 23 73 02  1C 42 00 00 ;num sectors=1881h ;div273h=A.01h ;2302h-0000h=2302h
```
The files in the ZMOVIE.STR archive start with subtitles in 1st sector (this is
usually/always only one single sector for the whole movie):<br/>
```
  000h 2    STR ID   (0160h)                                       ;\
  002h 2    STR Type (0001h=Subtitles)                             ;
  004h 2    Sector number within Subtitles (0)                     ; STR
  006h 2    Number of Sectors with Subtitles (1)                   ; header
  008h 4    Frame number (1)                                       ;
  00Ch 4    Data size counted in 4-byte units (same as [02Ch]/4)   ;
  010h 10h  Zerofilled                                             ;/
  020h 4    Unknown (2)                                            ;\
  024h 4    Unknown (1AAh, 141h, or 204h)                          ; Data
  028h 4    Unknown (00100000h)                                    ; part
  02Ch 4    Size of all Subtitle entries in bytes plus 10h         ;
  030h ..   Subtitle entries                                       ;/
  ...  ..   Zeropadding to 800h-byte boundary                      ;-padding
```
Subtitle entries:<br/>
```
  000h 4    Offset from current subtitle to next subtitle (or 0=Last subtitle)
  004h 4    First Frame number when to display the subtitle?
  008h 4    Number of frames when to display the subtitle?
  00Ch 4    Zero
  010h ..   Text string, terminated by 00h
  ...  ..   Zeropadding to 4-byte boundary
```
The text strings are ASCII, with special 2-byte codes (80h,7Bh=Linebreak,
1Fh,20h=u-Umlaut, etc).<br/>

#### Customized STR Video Headers

##### Viewpoint (with slightly modified STR header)
```
  008h 4    Frame number (0=First)                      ;<-- instead of 1=First
  01Ch 2    Unknown (always D351h)                      ;<-- instead of zero
  01Eh 2    Number of Frames in this STR file           ;<-- instead of zero
```

##### Capcom games
Resident Evil 2 (ZMOVIE\\*.STR, PL0\ZMOVIE\\*.STR)<br/>
Super Puzzle Fighter II Turbo (STR/CAPCOM15.STR)<br/>
```
  01Ch 4    Sector number of 1st sector of current frame  ;<-- instead of zero
```

##### Chrono Cross Disc 2 Video
Chrono Cross Disc 1 does have normal STR headers, but Disc 2 has Type.bit8
toggled:<br/>
```
  002h 2    STR Type (8101h=Disc 2)                       ;<-- instead of 8001h
```
And, the Chrono Cross "final movie" does reportedly have "additional
properties". Unknown, what that means, it does probably refer to the last movie
on Chrono Cross Disc 2, which is quite huge (90Mbyte), and has lower resolution
(160x112), and might have whatever "additional properties"?<br/>

##### Need for Speed 3
Need for Speed 3 Hot Pursuit (MOVIES\\*.XA, contains videos, not raw XA-ADPCM)<br/>
Jackie Chan Stuntmaster (FE\MOVIES\\*.STR)<br/>
With slightly modified STR headers:<br/>
```
  014h 4    Number of Frames (..excluding last some frames?) ;-instead BS[0..3]
  018h 4    Unlike the above modified entry, this is normal  ;-copy of BS[4..7]
```

##### ReBoot (MOVIES\\*.WXA)
This has leading XA-ADPCM, and customized STR header:<br/>
```
  014h 2    Type (0000h=Normal, 01FFh=Empty frames at end of video)
  016h 2    Number of Frames (excluding empty ones at end of video)
  018h 8    Zerofilled
```

##### Gran Turismo 1 (230Mbyte STREAM.DAT) and Gran Turismo 2 (330Mbyte STREAM.DAT)
These two games use BS iki format, and (unlike other iki videos) also special
STR headers:<br/>
```
  002h 2    STR Type (5349h) ("IS")         ;-special (instead 8001h)
  010h 2    Total number of frames in video ;-special (instead width)
  012h 2    Flags (bit15=1st, bit14=last)   ;-special (instead height)
  014h 8    Zero                            ;-special (instead BS header copy)
  020h 7E0h Data (in BS iki format)         ;-BS iki header (with width/height)
```
Caution: The STR header values aren't constant throughout the frame:<br/>
```
  Namely, flags in [012h] are toggled on first/last sector of each frame,
  and of course [04h] does also increase per sector.
```

##### PGA Tour 96, 97, 98 (VIDEO\..\\*.XA and ZZBUFFER\\*.STR)
Used by all movies in PGA Tour 96, 97 (and for the ZZBUFFER\BIGSPY.STR dummy
padding movie in PGA Tour 98).<br/>
The videos have normal BS v2 data, but the Frame Size entry is 8 smaller than
usually. As workaround, always load [0Ch]+8 for all movies with standard STR
headers (unless that would exceed [06h]\*7E0h).<br/>
```
  00Ch 4    Frame Size-8 (ie. excluding 8-byte BS header)  ;instead of Size-0
```
The padding videos in ZZBUFFER folder have additional oddities in STR header:<br/>
```
  ZZBUFFER\SPY256.STR    [14h..1Fh]=normal copy of 8-byte BS v2 header and zero
  ZZBUFFER\SPYGLASS.STR  [14h..1Fh]=zerofilled                          ;\BS v1
  ZZBUFFER\SPYTEST.STR   [14h..1Fh]=00 00 10 00 00 00 00 09 00 00 07 EE ;/
  ZZBUFFER\BIGSPY.STR    Used in PGA Tour 98 (instead of above three files)
```
SPYTEST.STR has nonsense quant values exceeding the 0000h..003Fh range (first
frame has quant=00B1h, and later frames go as high as quant=FFxxh, that kind of
junk is probably unrelated to BS fraquant). The oddities for SPYTEST.STR do
also occur in some frames in PGA Tour 98 BIGSPY.STR. Anyways, those ZZBUFFER
files seem to be only unused padding files.<br/>

##### Alice in Cyber Land (\*.STR)
Note: First sector contains XA-ADPCM audio (video starts in 2nd sector).<br/>
```
 STR Sector Header:
  002h 2    STR Type (0000h=Alice in Cyber Land video)            ;-special
  008h 4    Frame number (1=First) (bit15 set in last frame, or FFFFh)
  010h 10h  Zerofilled (instead width/height and BS header copy)  ;-special
  020h 7E0h Data (in BS v2 format)
```
Frames are always 320x240.<br/>
The frame number of the last used frame of a movie has the bit15 set. After
that last frame, there are some empty frame(s) with frame number FFFFh.<br/>
For some reason there are "extra audio sectors in between movies" (uh?).<br/>
Many of the movies have a variable frame rate. All movies contain frames
sequences that match one of the following frame rates: 7.5 fps, 10 fps, 15 fps,
30 fps.<br/>

##### Encrypted iki (Panekit - Infinitive Crafting Toy Case)
```
  014h 8    Copy of decrypted BS header (instead of encrypted BS header)
```

##### Princess Maker: Yumemiru Yousei (PM3.STR)
##### Parappa (Japanese Demo version only) (S0/GUIDE.STR)
These files do have BS ID=3000h (except, the first and last some frames have
nromal ID=3800h). The STR header is quite normal (apart from reflecting the odd
BS ID):<br/>
```
  016h 2    Copy of BS ID, 3000h in most frames (instead of 3800h)
  020h 7E0h Data (in BS format, also with BS ID 3000h, instead of 3800h)
```

##### Starblade Alpha and Galaxian 3
These movies have Extra stuff in the data section. The STR header is quite
normal (apart from reflecting the Extra stuff):<br/>
```
  00Ch 4    Frame Size in bytes (=size of ExtraHeader + BsData + ExtraData)
  014h 4    Copy of Extra Header        ;instead of BS[0..3]
  018h 4    Copy of BS[0..3]            ;instead of BS[4..7]
  020h 7E0h Data (ExtraHeader + BsData + ExtraData)
```
The data part looks as so:<br/>
```
  000h 2    Size of BS Data area    (S1)        ;\Extra Header
  002h 2    Size of Extra Data area (S2)        ;/
  004h S1   BS Data (in BS v3 format)           ;-BS Data
  ..   S2   Extra Data (unknown purpose)        ;-Extra Data
```
Note: Starblade Alpha does use that format for GAMEn.STR and NAME.STR in FLT
and TEX folders (the other movies in that game are in normal STR format).<br/>

##### Largo Winch: Commando SAR (FMV\NSPIN\_W.RNG)
This is a somewhat "normal" movie, without audio, and with the STR headers
moved to the begin of the file:<br/>
```
  000h Nx20h   STR Headers  ;size = filesize/800h*20h
  ...  Nx7E0h  Data         ;size = filesize/800h*7E0h
```
Note: The movie contains the rotating "W" logo, which is looped in Start
screen.<br/>

##### Player Manager (1996, Anco Software) (FILMS\1..3\\*.STR)
```
  006h 2    Number of Sectors in this Frame-1 (8..9 = 9..10 sectors)
  00Ch 4    Frame Size in bytes               (8..9*7E0h = 3F00h or 46E0h)
  010h 2    Bitmap Width                      (always F0h)
  012h 2    Bitmap Width                      (always 50h)
  014h 0Ch  Zerofilled (instead copy of BS header or copy of Extra header)
  020h 7E0h Data (Extra Stuff, BS v2 data, plus Unused stuff)
```
The data part occupies 9-10 sectors, consisting of:<br/>
```
  0000h Extra Stuff   (7E0h bytes, whatever, often starts with 00,FF,00,FF,..)
  07E0h BS v2 data    (3720h or 3F00h bytes, including FFh-padding)
  ...   Unused Sector (7E0h bytes, same as in previous frame or zerofilled)
```
The compressor tries to match the picture quality to the number of sectors per
frame, but it's accidentally leaving the last sector unused:<br/>
```
  For 9 sectors:  Only 1..7 are used, sector 8 is same as in previous frame
  For 10 sectors: Only 1..8 are used, sector 9 is zerofilled
```
Apart from the odd format in FILMS\1..3\\*.STR, the game does also have normal
videos in FILMS\\*.STR.<br/>

##### Chiisana Kyojin Microman (DAT\STAGE\*\\*.MV)
The .MV files have 5 sectors/frame: Either 5 video sectors without audio, or
4-5 video sectors plus XA-ADPCM audio (in the latter case, audio is in each 8th
sector (07h,0Fh,17h,1Fh,etc), hence having filesize rounded up to N\*8 sectors):<br/>
```
  Filesize = 800h*((NumberOfFrames*5))             ;5 sectors, no xa-adpcm
  Filesize = 800h*((NumberOfFrames*5+7) AND not 7) ;4-5 sectors, plus xa-adpcm
```
Caution: The STR header values aren't constant throughout the frame:<br/>
```
  Sector 0: [10h] = Number of Frames,   [12h]=Junk
  Sector 1: [10h] = Junk,               [12h]=0
  Sector 2: [10h] = Junk,               [12h]=Junk
  Sector 3: [10h] = Junk,               [12h]=Same as below (Bitmap Height)
 Below ONLY when having 5 sectors per frame:
  Sector 4: [10h] = Bitmap Width (140h) [12h]=Bitmap Height (D0h)
 That is, frames with 4 sectors do NOT have any Bitmap Width entry
 (the duplicated Height entry in sector 3 exists, so one could compute
 Width=NumMacroBlocks*100h/Height, or assume fixed Width=320, Height=208).
```
The Junk values can be zero, or increase/decrease during the movie, some or all
of them seem to be sign-expanded from 12bit (eg. increasing values can wrap
from 07xxh to F8xxh).<br/>
Apart from the odd DAT\STAGE\*\\*.MV files, the game does also have .STR files
with normal STR headers and more sectors per frame (DAT\STAGE16,21,27\\*.STR,
DAT\OTHER\\*.STR, DAT\OTHER\CM\\*.STR, and MAT\DAT\\*.STR).<br/>

##### Black Silence padding
Used by Bugriders: The Race of Kings (MOVIE\\*XB.STR)<br/>
Used by Rugrats Studio Tour (MagDemo32: RUGRATS\DATA\OPEN\\*B.STR)<br/>
```
  Each movie file is followed by dummy padding file. For example, in Bugriders:
  MOVIE\*XA.STR  Movie clip             (with correct size, 320x192)
  MOVIE\*XB.STR  Black Silence padding  (wrong size 640x192, should be 320x192)
```
The names are sorted alphabetically and exist in pairs (eg. CHARMXA.STR and
CHARMXB.STR), and the disc sectors are following the same sort order.<br/>
The padding files contain only black pixels and silent XA-ADPCM sectors, with
following unique STR header entries, notably with wrong Width entry (the MDEC
data contains only 320x192 pixels).<br/>
```
  00Ch 4    Frame Size    (087Ch)
  010h 2    Bitmap Width  (wrongly set to 640, should be 320)
  012h 2    Bitmap Height (192)
  014h 2    MDEC Size     (05A0h)
  016h 2    BS ID         (3800h)
  018h 2    BS Quant      (0001h)
  01Ah 2    BS Version    (0002h)
  Filesize is always 44Fh sectors (about 2.2Mbyte per *XB.STR file)
```
The huge 7 second padding is a very crude way to avoid the next movie to be
played when not immediately pausing the CDROM at end of current movie.<br/>

##### Ridge Racer Type 4 (only PAL version) (R4.STR)
The 570Mbyte R4.STR file contains XA-ADPCM in first three quarters, and two STR
movies in last quarter:<br/>
```
  1st NTSC/US movie: 320x160 pix, 0F61h frames, 4-5 sectors/frame, normal STR
  1st PAL/EUR movie: 320x176 pix, 0CD0h frames, 5-6 sectors/frame, special STR
  2nd NTSC/US movie: 320x160 pix, 1D6Ah frames, 4-5 sectors/frame, normal STR
  2nd PAL/EUR movie: 320x160 pix, 18B5h frames, 5-6 sectors/frame, normal STR
```
As seen above, the PAL movies have lower framerate. And, the 1st PAL movie has
higher resolution, plus some other customized STR header entries:<br/>
```
  002h 2    STR Type (0001h=Custom, 176pix PAL video)         ;instead of 8001h
  006h 2    Number of Sectors in this Frame (always 5..6)
  00Ch 4    Frame Size (always 2760h or 2F40h, aka 7E0h*5..6)
  012h 2    Bitmap Height (00B0h, aka 176 pixels)             ;instead of 00A0h
  014h 8    Zerofilled                                        ;instead BS[0..7]
  020h 7E0h Data (in BS v3 format, plus FFh-padding)
```
That is, the special video is standard MDEC, the only problem is detecting it
as such (despite of the custom STR Type entry).<br/>

##### Mat Hoffman's Pro BMX (MagDemo48: MHPB\SHORT.STR)
This contains a normal MDEC movie, but with distorted "garbage" in first and
last some sectors.<br/>
```
  1st sector          STR Type 5673h (Leading Dummy)                ;\
  2nd sector          STR Type 8001h (distorted/empty MDEC)         ; junk
  3rd..6th sector     STR Type 8001h (distorted/garbage MDEC)       ;/
  7th sector and up   STR Type 8001h (normal MDEC, with odd [01Ch]) ;-movie
  Last 96h sectors    STR Type 0078h (Ending Dummy)                 ;-junk
```
1st Sector:<br/>
```
  002h 2    STR Type (5673h=Leading Dummy)
  004h 4    Whatever (0004000Ch)
  008h 4    Whatever (0098967Fh)
  00Ch 4    Frame Size (always 100h)
  010h 7F0h EAh-filled
```
2nd Sector:<br/>
```
  002h 2    STR Type (8001h=Normal MDEC ID, but content is empty)
  004h 4    Whatever (0004000Ch)        ;\
  008h 4    Whatever (0098967Fh)        ; same as in 1st sector
  00Ch 4    Frame Size (always 100h)    ; (but ID at [002h] differes)
  010h 7F0h EAh-filled                  ;/
```
3rd-6th Sector:<br/>
```
  002h 2    STR Type (8001h=Normal MDEC ID, but content is distorted)
  004h 2    Sector number within current Frame (always 0)
  006h 2    Number of Sectors in this Frame (always 1)
  008h 4    Frame number (increasing, 1..4 for 3rd..6th sector)
  00Ch 4    Frame Size (always 7D0h)
  010h 10h  EAh-filled
  020h 7D0h Unknown (random/garbage?)
  7F0h 10h  EAh-filled
```
7th Sector and up (almost standard MDEC):<br/>
```
 Caution: The STR header values aren't constant throughout the frame:
 Entry entry [01Ch] is incremented per sector (or wraps to 0 in new section).
  01Ch 4    Increasing sector number (within current movie section or so)
```
Last 96h Sectors:<br/>
```
  002h 2    STR Type (0078h=Ending Dummy)
  004h 2    Sector number within current Frame (always 0)
  006h 2    Number of Sectors in this Frame (always 1)
  008h 4    Frame number (increasing, in last 96h sectors)
  00Ch 4    Frame Size (always 20h)
  010h 2    Bitmap Width  (always 40h)
  012h 2    Bitmap Height (always 40h)
  014h 7ECh Zerofilled
```

##### Final Fantasy VII (FF7) (MOVIE\\*.MOV and MOVIE\\*.STR)
These movies have Extra stuff in the data section. The STR header is quite
normal (apart from reflecting the Extra stuff):<br/>
```
  00Ch 4    Frame Size in bytes (including 28h-byte extra stuff)
  014h 8    Copy of Extra data [0..7]           :-instead of BS header[0..7]
  020h 7E0h Data (ExtraData + BsData)
```
The data part looks as so:<br/>
```
  000h 28h  Extra data (unknown purpose, reportedly "Camera data" ... whut?)
  028h ..   BS Data (in BS v1 format)
```

##### Final Fantasy IX (FF9) (\*.STR and \*.MBG)
There are several customized STR header entries:<br/>
```
  002h 2    STR Type (0004h=FF9/Video)                      ;instead of 8001h
  004h 2    Sector number within current Frame (02h..num-1) (2..9 for video)
  006h 2    Total number of Audio+Video sectors in this frame (always 0Ah)
  00Ch 4    Frame Size/4 (of BS data, excluding MBG extra)  ;instead of Size/1
  014h 8    Copy of BS[0..7] from 8th video sector          ;instead 1st sector
  01Ch 2    Usually 0000h (or 0004h in some MBG sectors)    ;inszead of 0000h
  01Eh 2    Usually 0000h (or 3xxxh in some MBG sectors)    ;inszead of 0000h
  020h 8F4h Data (in BS v2 format, plus MBG extra data, if any)
```
Caution: The STR header values aren't constant throughout the frame:<br/>
```
  Namely, entry [1Ch..1Fh]=nonzero occurs only on the sector that does contain
  the end of BS data (=and begin of MBG extra data), and of course [04h] does
  also increase per sector.
```
Sector ordering has BS data snippets arranged backwards, for example, if BS
data does occupy 2.5 sectors:<br/>
```
  [04h]=00h-01h 1st-2nd audio sector, SPU-ADPCM (see Audio streaming chapter)
  [04h]=02h-06h 1st-5th video sector, unused, [020h..913h] is FFh-filled
  [04h]=07h     6th video sector, contains end of BS data and MBG extra, if any
  [04h]=08h     7th video sector, contains middle of BS data
  [04h]=09h     8th video sector, contains begin of BS data
```
Sector type/size, very unusually with FORM2 sectors:<br/>
```
  Audio sectors are MODE2/FORM1 (800h bytes, with error correction)
  Video sectors are MODE2/FORM2 (914h bytes, without error correction)
```
Huffman codes are standard BS v2, with one odd exception: MDEC 001Eh/03E1h
(run=0, level=+/-1Eh) should be usually encoded as 15bit Huffman codes, FF9 is
doing that for 001Eh, but 03E1h is instead encoded as 22bit Escape code:<br/>
```
  000000000100010         MDEC=001Eh (run=0, level=+1Eh) ;-normal (used)
  000000000100011         MDEC=03E1h (run=0, level=-1Eh) ;-normal (not used)
  0000010000001111100001  MDEC=03E1h (run=0, level=-1Eh) ;-escape (used)
```
There are two movie variants: \*.STR and \*.MBG. Most MBG files (except
SEQ02\MBG102.MBG) contain extra MBG info in [01Ch..01Fh] and extra MBG data
appended after the BS data. If present, the appended MBG data is
often/always(?) just these 28h-bytes:<br/>
```
  FF FF FF FF FE FF FE 41 AD AD AD AD AD AD AD AD
  AD AD AD AD AD AD AD AD AD AD AD AD AD AD AD AD
  AD AD AD AD AD AD AD AD
  (followed by FF's, which might be padding, or part of the extra data)
```
Unknown if some sectors contain more/other MBG data, perhaps compressed BG
pixel-depth values for drawing OBJs in front/behind BG pixels?<br/>

#### Non-standard STR Video Headers

##### Final Fantasy VIII (FF8)
Video frames are always 320x224. The video frames are preceeded by two
SPU-ADPCM audio sectors.<br/>
```
  000h 4    ID "SMJ",01h=Video
  004h 1    Sector number within current Frame (02h..num-1) (2..9 for video)
  005h 1    Total number of Audio+Video sectors in this frame, minus 1 (9)
  006h 2    Frame number (0=First)
  008h 7F8h Data (in BS v2 format)
```

##### Ace Combat 3 Electrosphere (in 520Mbyte ACE.SPH/SPB archive)
The videos start with one XA-ADPCM sector, followed by the first Video sector.<br/>
```
 STR Sector Header:
  000h 1    Always 01h
  001h 1    Sector number within current Frame (00h..num-1) (8bit)
  002h 2    Number of Sectors in this Frame
  004h 2    Unknown (1 or 3)
  006h 2    Frame number (decreasing, 0=Last)
  008h 2    Bitmap Width in pixels    ;\130hxE0h or 140hxB0h or 80hx60h
  00Ah 2    Bitmap Height in pixels   ;/
  00Ch 4    Zero
  010h 2    Zero, or decreasing timer (decreases approx every 2 sectors)
  012h 2    Zero, or decreasing timer (decreases approx every 1 sector)
  014h 3    Zero
  017h 1    Zero, or increases with step 2 every some hundred sectors
  018h 2    Zero, or Timer (increments when [1Ah] wraps from 04h to 01h)
  01Ah 1    Zero, or Timer (increments when [1Bh] wraps from 5Fh to 00h]
  01Bh 1    Zero, or Timer (increments approx every 1 sector)
  01Ch 2    Zero, or Whatever (changes to whatever every many hundred sectors)
  01Eh 2    Zero, or 0204h
  020h 7E0h Data (in BS v3 format)
```
Caution: The STR header values aren't constant throughout the frame:<br/>
```
  Namely, entry [10h..1Fh] can change within the frame (happens in japanese
  version), and of course [01h] does also increase per sector.
```
The Japanese version may be the only game that has two streaming videos running
in parallel on different channels.<br/>
That means, non-japanese version is different...?<br/>

##### Judge Dredd (1998, Gremlin) (CUTS\\*.IXA and LEVELS\\*\\*.IXA)
This is a lightgun-game with "interactive movies". The gameplay consists of
running on a fixed path through a scene with pre-recorded background graphics,
the only player interaction is aiming the gun at other people that show up in
that movie scene. There are two movie types:<br/>
```
  LEVELS\*\*.IXA  - Interactive gameplay movies
  CUTS\*.IXA      - Non-interactive cut-scene movies
```
Both CUTS and LEVELS have unusually small 4-byte STR headers:<br/>
```
  000h 4    Sector number within current Frame (LEVELS=0..8, or CUTS=0..9)
  004h 7FCh Data (see below)
```
Data for CUTS is 320x240pix (10 sectors per frame):<br/>
```
  Note: CUTS videos have 2 leading XA-ADPCM sectors
  000h ..   BS Data (in BS v2/v3 format)                        ;-BS picture
```
Data for LEVELS is 320x352pix plus extra stuff (9 sectors per frame):<br/>
```
  Note: LEVELS videos have 1 leading XA-ADPCM sector
  000h 4    Offset to BS Data (always 28h)                      ;\
  004h 4*6  Offsets to Extra Stuff 1..6                         ; extra header
  01Ch 0Ch  Zerofilled                                          ;/
  028h ..   BS Data (in BS v2/v3 format)                        ;-BS picture
  ...  ..   Extra Stuff 1..6                                    ;-extra data
```
The unusual 320x352pix resoltution contains a 320x240pix BG image, with
additional 320x112pix texture data appended at the bottom.<br/>
Extra Stuff 1..6 does supposedly contain info for animating enemies and/or
backgrounds.<br/>

#### iki
The .iki video format (found in files with .IKI or .IK2 extension) is used in
several games made by Sony. iki movie sectors have some different properties:<br/>
```
  * There are only as many iki video sectors as needed to hold all the
    frame's data. Remaining sectors are null.
  * The first sector's Submode.Channel starts at zero, then increments for
    each sector after that, and resets to zero after an audio sector.
  * IK2 videos can also have variable frame rates that are very inconsistent.
```



##   CDROM File Video Streaming Framerate
According to Sony, BS encoded 320x240pix videos can be played at 30fps (with
cdrom running at double speed).<br/>

#### STR Frame Rate
As a general rule, the frame rate is implied in CDROM rotation speed (150 or 75
sectors per second, minus the audio sectors, divided by the number of sectors
per video frame).<br/>

#### Fixed/Variable Framerates
The frame can drop on video frames that contain more sectors than usually.
Video frames that require fewer sectors than often padded with zerofilled
sectors. However, some games don't have that padding, so they could end up
reeceiving up to 150 single-sector frames per second; the actual framerate is
supposedly slowed down to 60Hz or less via Vblank timer (and with the CDROM
reading getting paused when the read-ahead buffer gets full).<br/>

#### Audio Samplerate
XA-ADPCM audio contains samplerate info (in the FORM2 subheader), the
samplerate versus amount of audio sectors can be used to compute the CDROM
rotation speed.<br/>
There are two exceptions: Some movies don't have any audio at all, and some
movies use SPU-ADPCM instead of XA-ADPCM. In the latter case, the SPU Pitch
(samplerate) may (or may not) be found somewhere in the audio sector headers.<br/>

#### CDROM Rotation speed
As said above, the speed can be often detected via audio sample rate.
Otherwise, the general rule is that most PSX games are used 2x speed (150
sectors/second). But, there are a few games with 1x speed (see below).<br/>

#### CDROM Single speed (75 sectors/frame)
Here are probably most of the USA games with videos at 1x speed.<br/>
```
  007 - The World Is Not Enough
  1Xtreme
  Arcade Party Pak
  Atari Anniversary Edition Redux
  Blast Radius
  Blue's Clues - Blue's Big Musical
  Chessmaster II
  Chronicles of the Sword
  Civilization II
  Colin McRae Rally
  Creatures - Raised in Space
  Cyberia
  Demolition Racer
  Dune 2000
  ESPN Extreme Games
  FIFA Soccer 97
  Fade to Black
  Family Connection - A Guide to Lightspan
  Fear Effect
  Fox Hunt
  Interactive CD Sampler Volume 1
  Jade Cocoon - Story of the Tamamayu
  Jeopardy! 2nd Edition
  Juggernaut
  Krazy Ivan
  MTV Sports - Skateboarding featuring Andy Macdonald
  MTV Sports - T.J. Lavin's Ultimate BMX
  Medal of Honor
  Medal of Honor - Underground
  Official U.S. PlayStation Magazine Demo Disc 23
  Planet of the Apes
  PlayStation Underground Number 2
  Shockwave Assault
  Starblade Alpha
  Starwinder - The Ultimate Space Race
  Str.at.e.s. 1 - Match-A-Batch
  Str.at.e.s. 5 - Parallel Lives!
  Str.at.e.s. 7 - Riddle Roundup!
  The X-Files
  Top Gun - Fire at Will!
  Um Jammer Lammy
  Uprising X
  Wheel of Fortune - 2nd Edition
  Williams Arcade's Greatest Hits
```



##   CDROM File Video Streaming Audio
#### Audio Stream
STR movies are usually interleaved with XA-ADPCM sectors (the audio sectors are
automatically decoded by the CDROM hardware and consist of raw ADPCM data
without STR headers).<br/>
[CDROM File Audio Streaming XA-ADPCM](audio.md#cdrom-file-audio-streaming-xa-adpcm)<br/>
However, there are also movies without audio. And a few movies with SPU-ADPCM
audio.<br/>

#### SPU-ADPCM in Chunk-based formats
[CDROM File Video Streaming Chunk-based formats](#cdrom-file-video-streaming-chunk-based-formats)<br/>

#### SPU-ADPCM in Chrono Cross/Legend of Mana Audio Sector
Chrono Cross Disc 1 (HiddenDirectory\1793h..17A6h)<br/>
Chrono Cross Disc 2 (HiddenDirectory\1793h..179Dh)<br/>
Legend of Mana (MOVIE\\*.STR, except some movies without audio)<br/>
```
  000h 2    STR ID   (0160h)
  002h 2    STR Type (0000h, 0001h, 0100h, or 0101h)
              0000h=Legend of Mana, Audio normal sectors
              0001h=Legend of Mana, Audio sectors near end of movie
              0000h=Chrono Cross Disc 1, Audio.left?
              0001h=Chrono Cross Disc 1, Audio.right?
              0100h=Chrono Cross Disc 2, Audio.left?
              0101h=Chrono Cross Disc 2, Audio.right?
  004h 2    Sector number in Frame (0=Audio.left?, 1=Audio.right?)
  006h 2    Number of Audio sectors in this frame (always 2)
  008h 4    Frame number (1=First)
  00Ch 4    Unused (Chrono: FFh-filled or Mana: 00000FC0h=2x7E0h=Framesize?)
  010h 10h  Unused (Chrono: FFh-filled or Mana: 00h-filled)
  020h 60h  Unused (FFh-filled)
  080h 4    ID "AKAO"
  084h 4    Frame number (0=First)
  088h 8    Unused (zerofilled)
  090h 4    Remaining Time (step 690h) (can get stuck at 0340h or 0B20h at end)
  094h 4    Zero
  098h 4    Unknown (11h)
  09Ch 4    Pitch (1000h=44100Hz)
  0A0h 4    Number of bytes of audio data (always 690h)
  0A4h 2Ch  Unused (zerofilled)
  0D0h 690h Audio  (10h-byte SPU-ADPCM blocks) (1680 bytes)
  760h A0h  Unused (10h-byte SPU-ADPCM blocks with flag=03h and other bytes=0)
```
Note: The Chrono/Mana STR files start with Audio frames in first sector
(except, some Legend of Mana movies don't have any Audio, and do start with
Video frames).<br/>

#### SPU-ADPCM in Final Fantasy VIII (FF8)
```
  000h 4    ID "SMN",01h=Audio/left, "SMR",01h=Audio/right
  004h 1    Sector number in Frame (0=Audio.left, 1=Audio.right)
  005h 1    Total number of Audio+Video sectors in this frame, minus 1 (1 or 9)
  006h 2    Frame number (0=First)
  008h E8h  Unknown (camera data?) (232 bytes)
  0F0h 6    Audio ID (usually "MORIYA", sometimes "SHUN.M")
  0F6h 0Ah  Unknown (10 bytes) (reportedly 10 bytes at offset 250 = FAh ?????)
  100h 4    ID "AKAO"
  104h 4    Frame number (0=First)
  108h 14h  Unknown (20 bytes)
  11Ch 4    Pitch (1000h=44100Hz)
  120h 4    Number of bytes of audio data (always 690h)
  124h 2Ch  Unknown (44 bytes)
  150h 20h  Unknown (32 bytes)
  170h 690h SPU-ADPCM Audio data (690h bytes)
```
There is one special case on disc 1: a movie with no video. Each 'frame'
consists of two sectors: the first is the left audio channel, the second is the
right audio channel.<br/>

#### SPU-ADPCM in Final Fantasy IX (FF9) (\*.STR and \*.MBG)
The FF9 audio sectors are normal MODE2/FORM1 sectors (unlike the FF9 video
sectors, which are MODE2/FORM2).<br/>
```
  000h 2    STR ID   (0160h)
  002h 2    STR Type (0008h=FF9/Audio)
  004h 2    Sector number in Frame (0=Audio.left, 1=Audio.right)
  006h 2    Total number of Audio+Video sectors in this frame (always 0Ah)
  008h 4    Frame number (1=First)
  00Ch 4    Zero
  010h 1    Audio flag? (00h=No Audio, 01h=Audio)
  011h 4Fh  Zerofilled --- XXX or whatever (when above is 00h)
  060h 4    Number of Frames in this STR file
  064h 1Ch  EEh-filled
 Below 780h bytes are all zerofilled when [10h]=00h (no audio)
 Below 780h bytes are reportedly all ABh-filled "in the last frame of a movie
 on Disc 4" (unknown which movie, and if that occurs in other movies, too)
  080h 4    ID "AKAO"
  084h 4    Frame number (0=First)
  088h 14h  Unknown (20 bytes)
  09Ch 4    Pitch (116Ah=48000Hz) (or 1000h=44100Hz in final movie)
  0A0h 4    Number of bytes of audio data (0, 720h, 730h, or 690h=final movie)
  0A4h 2Ch  Unknown (44 bytes)
  0D0h 730h SPU-ADPCM audio (plus leftover/padding when less than 730h bytes)
```

#### Dance series SPU-ADPCM streaming (bigben interactive, DATA.PAK\stream\\*.str)
This format is used for raw SPU-ADPCM streaming (without video).<br/>
SLES-04121 Dance: UK<br/>
SLES-04161 Dance: UK eXtra TraX<br/>
SLES-04129 Dance Europe<br/>
SLES-04162 All Music Dance! (Italy)<br/>
```
  000h 2    STR ID   (0160h)
  002h 2    STR Type (8001h, same as MDEC)
  004h 2    Sector number within current Frame (0000h..num-1)
  006h 2    Number of Sectors in this Frame (always 9)
  008h 4    Frame number (0=First)
  00Ch 4    Frame Size in bytes (always 4000h)
  010h 4    Whatever (always 00A000A0h, would be width/height if it were video)
  014h 8    Zerofilled
  01Ch 4    Special ID (always DDCCBBAAh for Dance audio)
  020h 7E0h Data (in SPU-ADPCM format, mono, 22200Hz aka Pitch=07F5h)
```
Note: Sector 0..8 contain 9\*7E0h=46E0h bytes data per frame, but only 4000h
bytes are used (the last 6E0h bytes in sector 8 are same as in sector 7).<br/>

#### Raw SPU-ADPCM Streaming
Some games are using raw SPU-ADPCM for streaming. That is, the file is
basically a normal .VB file, but it can be dozens of megabytes tall (ie. too
large to be loaded into RAM all at once).<br/>
```
  Disney's The Emperor's New Groove (MagDemo39: ENG\STREAM\*.CVS)
  Disney's Aladdin in Nasira's Revenge (MagDemo46: ALADDIN\STREAM\*.CVS)
```



##   CDROM File Video Streaming Chunk-based formats
#### Newer Electronic Arts videos (EA)
EA videos are chunk based (instead of using 20h-byte .STR headers). The next
chunk starts right at the end of the previous chunk (without padding to sector
boundaries).<br/>
```
 STR Sector Header:
  No STR Sector header (first sector starts directly with "VLC0" chunk)
 VLC0 Chunk (at begin of movie file):
  000h 4     Chunk ID "VLC0"
  004h 4     Chunk Size (always 1C8h)     (big-endian)
  008h 1C0h  16bit MDEC values for E0h huffman AC codes (little-endian)
 MDEC Chunks (video frames):
  000h 4     Chunk ID "MDEC"                           ;\
  004h 4     Chunk Size (...)             (big-endian) ; custom chunk header,
  008h 2     Bitmap Width in pixels       (big-endian) ; instead of STR header
  00Ah 2     Bitmap Height in pixels      (big-endian) ;
  00Ch 4     Frame Number (starting at 0) (big-endian) ;/
  010h ..    Data (in BS v2 format, but using custom Huffman codes from VLC0)
  ...  ..    Zeropadding to 4-byte boundary
 Audio Chunks (au00/au01):
  000h 4     Chunk ID ("au00"=normal, "au01"=last audio chunk)
  004h 4     Chunk Size (...)                                   (big-endian)
  008h 4     Total number of 2x4bit samples in previous chunks  (big-endian)
  00Ch 2     Unknown (always 800h) (maybe Pitch: 800h=22050Hz)  (big-endian)
  00Eh 2     Unknown (always 200h)                              (big-endian)
  ...  ..    SPU-ADPCM audio data, left  (0Fh bytes per sample block)
  ...  ..    SPU-ADPCM audio data, right (0Fh bytes per sample block)
  ...  ..    Garbagepadding to 4-byte boundary
  Note: SPU-ADPCM does normally have 10h-byte blocks, but in this case,
  the 2nd byte (with loop flags) is omitted, hence only 0Fh-byte blocks.
 Zero Chunk (zeropadding at end of file, exists only in some EA videos):
  000h ..    Zeropadding
```

#### Older Electronic Arts videos
Crusader: No Remorse (1996 Origin Systems) (MOVIES\\*.STR)<br/>
Soviet Strike (1996 Electronic Arts)<br/>
Battle Stations (1997 Electronic Arts)<br/>
Andretti Racing (1996 Electronic Arts)<br/>
```
 STR Sector Header:
  000h 4    ID (DDCCBBAAh) (aka AABBCCDDh big-endian)
  004h 4    Sector number within STR file (0=First, up to Filesize/800h-1)
  008h 7F8h Data (video and audio chunks, see below) (first chunk is "ad20")
 Video Chunks (MDEC):
  000h 4    Chunk ID "MDEC"                           ;\
  004h 4    Chunk Size (...)             (big-endian) ;
  008h 2    Bitmap Width in pixels       (big-endian) ; custom chunk header
  00Ah 2    Bitmap Height in pixels      (big-endian) ;
  00Ch 4    Frame Number (starting at 0) (big-endian) ;/
  010h ..   Data (in BS v2 format)                    ;-standard BS v2 data
 Audio Chunks (ad20/ad21) (22050Hz stereo):
  000h 4    Chunk ID ("ad20"=normal, "ad21"=last audio chunk)
  004h 4    Chunk Size (1A50h or 1A70h)                        (big-endian)
  008h 4    Total number of 2x4bit samples in previous chunks  (big-endian)
  00Ch 2    Unknown (always 800h) (maybe Pitch: 800h=22050Hz)  (big-endian)
  00Eh 2    Unknown (always 200h)                              (big-endian)
  010h ..   SPU-ADPCM audio data, left  (10h bytes per sample block)
  ...  ..   SPU-ADPCM audio data, right (10h bytes per sample block)
 Last STR Sector:
  000h 18h  FFh-filled (aka 8-byte STR header and 10h-byte Chunk header)
  018h -    Nothing (total STR filesize is N*800h+18h bytes)
```

#### Oldest Electronic Arts videos
Wing Commander III: Heart of the Tiger (MOVIES1.LIB\\*.wve) (1995, EA/Origin)<br/>
```
 STR Sector Header:
  No STR Sector header (first sector starts directly with "Ad10" chunk)
 Video Chunks (MDEC):
  000h 4    Chunk ID "MDEC"                           ;\
  004h 4    Chunk Size (2xx0h)           (big-endian) ;
  008h 2    Bitmap Width in pixels       (big-endian) ; custom chunk header
  00Ah 2    Bitmap Height in pixels      (big-endian) ;
  00Ch 2    Unknown (7FFFh)              (big-endian) ;
  00Eh 2    Unknown (AD14h or AD24h)     (big-endian) ;/
  010h ..   Data (in BS v2 format)                    ;-standard BS v2 data
  ...  ..   Padding, up to circa 20h bytes, FFh-filled
 Audio Chunks (Ad10/Ad11) (22050Hz stereo):
  000h 4    Chunk ID ("ad20"=normal, "ad21"=last audio chunk)
  004h 4    Chunk Size (D38h or D28h) (or less in last chunk)  (big-endian)
  010h ..   SPU-ADPCM audio data, left  ? (10h bytes per sample block)
  ...  ..   SPU-ADPCM audio data, right ? (10h bytes per sample block)
```
Audio seems to be 22050Hz stereo, however, chunks with size=D38h have odd
amounts of sampleblocks, so it isn't as simple as having left/right in
first/second half.<br/>

#### Policenauts (Japan, 1996 Konami) (NAUTS\MOVIE\\*.MOV)
```
 STR Sector Header:
  No STR Sector header (first sector starts directly with "VMNK" chunk)
 First chunk (800h bytes):
  000h 4     ID "VMNK" (aka KNMV backwards, maybe for Konami Video/Movie)
  004h 4     Unknown (01h)
  008h 4     Unknown (01h)
  00Ch 4     Unknown (F0h)
  010h 4     Size of KLBS chunks?          (40000h)
  014h 4     Bitmap X1 (aka left border)?  (16pix, 10h)
  018h 4     Bitmap Y1 (aka upper border)? (16pix, 10h)
  01Ch 4     Bitmap Width                  (288pix, 120h)
  020h 4     Bitmap Height                 (144pix, 90h)
  024h 7E4h  Zerofilled
 Further chunks (40000h bytes, each):
  000h 8     Zerofilled
  008h 4     Chunk ID "KLBS" (aka SBLK backwards, maybe for Stream Block)
  00Ch 4     Chunk Size (usually 40000h)
  010h 4     Number of Name List entries
  014h 4     Number of Name List entries (same as above)
  018h 8     Zerofilled
  020h N*30h Name List
  ...  ..    Data (referenced from Name List)
  ...  ..    Zeropadding (to end of 40000h-byte chunk)
```
The Name List does resemble a file archive, however, the "filenames" are just
Type IDs (eg. all picture frames do have the same name).<br/>
```
 Name List entries:
  000h 8     Zerofilled
  008h 8     Data Type Name (eg. "SCIPPDTS")
  010h 4     Time when to play/display the frame (0 and up)
  014h 4     Time duration for that frame (usually 14h for Picture frames)
  018h 4     Data Offset in bytes (from begin of chunk)
  01Ch 4     Data Size in bytes
  020h 10h   Zerofilled
```
Data Formats for the different Data Types...<br/>
```
 Type "SDNSHDTS" aka SNDS,STDH - SoundStdHeader (Size=800h, Duration=0)
  000h 4     Maybe Pitch? (800h)                            (big-endian)
  004h 4     Maybe Pitch? (800h)                            (big-endian)
  008h 4     Total SPU-ADPCM size in bytes (for whole .MOV) (big-endian)
  00Ch 4     Unknown (FFFFFFFFh)                            (whatever)
  010h 4     Unknown (00007FFFh)                            (big-endian)
  014h 7ECh  Zerofilled
 Type "SDNSSDTS" aka SNDS,STDS - SoundStdStream (Size=10h..4000h, Duration=9Ch)
  000h 4000h SPU-ADPCM data in 10h-byte blocks (last chunk is less than 4000h)
 Type "SCIPPDTS" aka PICS,STDP - PictureStdPicture (Size=3xxxh, Duration=14h)
  000h 3xxxh Picture Frame (in BS v1 format)
 Type "SCTELLEC" aka ETCS,CELL - ExtraCells? (Size=0Ch, Duration=1)
  000h ..    Maybe subtitle related...?
 Type "SCTEGOLD" aka ETCS,DLOG - ExtraD-log? (Size=19h..31h, Duration=27h..44h)
  000h ..    Maybe subtitle related...?
```
Note: Total number of 10h-byte SPU-ADPCM blocks can be odd (so the audio seems
to be mono).<br/>
Apart from the .MOV files, there's also one standard .STR file for the Knnami
Intro (with normal STR headers and BS v2 data).<br/>

#### Best Sports Games Ever (DD\\*.VLC and MOVIES\\*.VLC) (Powerline Demo Disc menu)
This format is used for still images with only frame, and for looping short
animation sequences in the Demo Disc Menu. There's no audio.<br/>
```
 Header Chunk:
  000h 4    Fixed ID (74h,55h,89h,08h aka 08895574h)
  004h 2    Bitmap Width           (140h)
  006h 2    Bitmap Height          (100h)
  008h 2    Video Frame Size/4     (17A0h or 13B0h)
  00Ah 2    Number of Video Frames (01h or 32h)
  00Ch 4    Frame End ID (eg. 62DCCACEh) (random?, but stays same within movie)
 Video Frame Chunk(s):
  ...  ..   Data (in BS v1/v2/v3 format)         ;\size = hdr[008h]*4
  ...  ..   FFh-filled (padding to Frame Size)   ;/
  ...  4    Frame End ID (eg. 62DCCACEh)         ;-same value as in hdr[00Ch]
```
For random access, best is seeking "fpos=N\*(Framesize+4)+10h", alternately one
could search "fpos=LocationAfterFrameEndID".<br/>

#### Sentient (FILMS\\*.FXA)
This is having neither per-sector STR headers nor Chunk headers, instead it's
having raw data with fixed size of 10 sectors per frame.<br/>
File Header (sector 0, 800h bytes):<br/>
```
  000h 4    File ID (01h,"XSP") (aka PSX backwards)
  004h 2    Unknown (0001h)
  006h 2    Unknown (0040h) (this is used for something...)
  008h 2    Bitmap Width  (0140h)
  00Ah 2    Bitmap Height (00F0h)
  00Ch 4    Total number of video frames
  010h 4    Number of video sectors per frame (always 8)
  014h 4    Total number of video sectors, excluding audio/dummy (=NumFrames*8)
  018h 1    Zero
  019h 1    Sector List size (28h) (ie. each 4 frames)  ;\or zerofilled when
  01Ah 28h  Sector Types (2=Video, 1=Audio, 0=Dummy)    ;/not present
  042h ..   Zerofilled
  7xxh ..   Unknown, maybe just garbage ...?
  ...  ..   Zerofilled
```
The frame rate is 15fps with 10 sectors per frame (8xVideo and either 2xAudio
or 1xAudio+1xDummy). The Video/Audio/Dummy sector arrangement does repeat each
40 sectors (aka each 4 frames):<br/>
```
  vVvvvvv--vvVvvv--vvvvVv--vvvvvv-Vvvvvvv-  Video
  -------A-------A-------A-------A-------A  Audio
  --------D-------D-------D---------------  Dummy
  V = 1st sector of video frame
  v = 2nd..8th sector of video frame (or fileheader in case of sector 0)
  A = Audio (each 8th sector, ie. sector 07h,0Fh,17h,1Fh,etc.)
  D = Dummy (occurs after some (not all) audio sectors)
 Some files have that sector arrangement stored in header[019h..041h], but
 other files have that header entries zerofilled (despite of using the same
 arrangement).
```
Video frames are 8 sectors (4000h-byte), first and last 8 bytes are swapped:<br/>
```
  0000h 8     Last 8 bytes of BS v1 bitstream   ;\or garbage padding
  0008h 3FF0h First 3FF0h of BS v1 bitstream    ;/
  3FF8h 8     Footer (64bit, with squeezed BS header and other info)
 The footer bits are:
  0-4    5bit   Quant (00h..1Fh) (only 5bit, not 6bit)
  5-15   11bit  MDEC Size in 20h-word units (80h-byte units)
  16-23  8bit   Unknown (lowbits are often same as bit48 and up?)
  24-31  8bit   BS ID/100h (3800h/100h)
  32-47  16bit  Frame Number (0=First)
  48-63  16bit  Next Sector Number (start of next video frame)
 To decrypt/convert the frame to standard BS v1 format:
  x=[3FF8h]                      ;get footer
  [3FF8h..3FFFh]=[0000h..0007h]  ;last 8 bytes of bitstream
  [0000h]=(x AND FF00FFE0h)      ;size and ID=3800h
  [0004h]=(x AND 1Fh)+10000h     ;quant and version=v1
 The next_sector number is usually current_sector+1 (or +2 if that would be
 audio), in last frame it does point to end of file.
 Bitstreams smaller than 3FF8h are garbage padded (initially some 32bit garbage
 values, and in later frames leftovers from previous bitstream sectors).
```
Dummy sectors contain 800h bytes:<br/>
```
  000h 4     Always FFFFFFFFh (unfortunately, this isn't a unique ID)
  004h 7FCh  Garbage (zeroes, random, or even leaked ASM source code)
 Dummy sectors have the same Subheader as video sectors, the leading FFFFFFFFh
 could also occur in BS bitstreams or frames with garbage padding, so one must
 use the sector arrangement pattern to identify dummy sectors.
```
Audio sectors are XA-ADPCM and can be filtered via Subheader, or via sector
arrangement pattern.<br/>



##   CDROM File Video Streaming Mis-mastered files
#### Mis-mastered streaming files
There are several discs that have streaming data stored as partial CDROM images
(instead of as real CDROM sectors).<br/>
```
  Format        Content    Where
  raw 920h-byte STR        K9.5 1 - Live in Airedale (ZZBUFFER.STR)  ;\
  raw 920h-byte STR        Need for Speed 3 (MOVIES\ZZZZZZZ*.PAD)    ;
  raw 920h-byte STR        3D Baseball (ZZZZZZZZ.ZZZ)                ; intended
  raw 920h-byte STR        Wing Commander III (DUMMY.DAT)            ; padding
  raw 920h-byte STR        R-Types (DMY\DUMMY.BIN)                   ;
  raw 920h+junk STR+junk   Grand Slam (DUMMY.BIN)                    ;
  raw 920h-byte XA-ADPCM   Spec Ops Airborne Commando (PADDING.NUL)  ;
  raw 920h-byte SW-STR     Cyberia (ENDFILL\*.STR) (software render) ;
  RIFFs/CDXAfmt STRs       Sonic Wings Special (SW00.DMY = two RIFFs);/
  raw 920h-byte XA-ADPCM   Rugrats (MagDemo19: STREAMS\DB02.ISF)     ;\nonsense
  raw 920h-byte Data BABEh Rugrats (MagDemo19: STREAMS\OPEN.BIN)     ; dupes
  raw ???-byte  CDDA       Championship Surfer (MagDemo43: HWX\MUSIC);/
  raw ???-byte  CDDA       Twisted Metal 2 (MagDemo50: TM2\FRWYSUB.DA) ;-?
  raw 920h-byte STR        Sonic Wings Special (MOV\MQ*.STR)         ;-unused?
  raw 920h-byte STR        Apocalypse (MagDemo16: APOC\*.STR)
  raw 920h-byte XA-ADPCM   Apocalypse (MagDemo16: APOC\*.XA)
  raw 920h-byte XA-ADPCM   NFL Xtreme (MagDemo13: NFLX\GAME\SOUND\2PLAYRNO.XA)
  raw 920h-byte XA-ADPCM   Ace Combat 2 (MagDemo01: ACE2.STP)
  raw 920h-byte XA-ADPCM   Colony Wars (MagDemo02: CWARS\DEMO.PAK)
  raw 920h-byte XA-ADPCM   Best Sports demo (AH2\GAMEDATA\COM\MUSIC\MUSIC.IXA)
  raw 920h-byte XA-ADPCM   Tomb Raider: Last Revelation (MagDemo29: TR4\XA1.XA)
  raw 800h-byte XA-ADPCM   Croc 1 demo (MagDemo02: CROC\MAGMUS.STR) (FORM1)
  RIFF/CDXAfmt  XA-ADPCM   Best Sports demo (LOMUDEMO\SFX\COMMENT.STR)
  RIFF/CDXAfmt  ?+XA-ADPCM Ace Combat 3 Electrosphere (MagDemo30: AC3\*.SPB)
  RIFF/CDXAfmt  XA-ADPCM   Colony Wars Venegance (MagDemo14: CWV\SONYDEMO.PAK)
  RIFF/WAVEfmt  CDDA       T'ai Fu (MagDemo16: TAIFU\3_10.WAV, 2x16bit 44100Hz)
  RIFF/WAVEfmt  CDDA       Psalm69 (beta) FRONT\FIRE.TRK
```
The 920h-byte sectors exclude the leading Sync mark and MM:SS:FF:Mode2 value.<br/>
```
 Data/movie sectors look as so:
  000h 4    Sub-Header (File, Channel, Submode OR 20h, Codinginfo)
  004h 4    Copy of Sub-Header
  008h 800h Data (2048 bytes)           ;<-- contains STR movie sectors
  808h 4    EDC (zerofilled)
  80Ch 114h ECC (zerofilled)
 And XA-ADPCM sectors look as so:
  000h 4    Sub-Header (File, Channel, Submode OR 64h, Codinginfo)
  004h 4    Copy of Sub-Header
  008h 900h Data (18*128 bytes)         ;\contains XA-ADPCM audio sectors
  908h 14h  Data (zerofilled)           ;/
  91Ch 4    EDC (zerofilled)
```
The RIFF/CDXAfmt has a standard RIFF header, followed by 930h-byte sectors
(same format as when opening CDROM streaming files in Windows). The
RIFF/WAVEfmt is just a standard .WAV file.<br/>
In case of the ZZ\*.\* files on retail discs, the developers did intentionally
append some non-functional dummy STR files (instead of appending zerofilled
30Mbyte at end of disc).<br/>
[CDROM File XYZ and Dummy/Null Files](compression.md#cdrom-file-xyz-and-dummynull-files)<br/>
In case of the Demo Discs, the developers did probably have high hopes to
release a demo version with working streaming data, just to find out that Sony
had screwed up the data format (or maybe they had only accidentally included
streaming data, without actually using it in demo version). Confusingly, the
corrupted files were released on several discs (magazine demos, and other demo
releases).<br/>
The Rugrats demo has intact files in RUGRATS\CINEMAT and RUGRATS\XA folders,
plus nonsense copies of that files in 920h-byte format in STREAMS folder.<br/>

#### Partially mis-mastered files
Legend of Dragoon (MagDemo34: LOD\XA\LODXA00.XA has FIRST SECTOR mis-mastered
(it has TWO sub-headers (01,00,48,00,01,00,48,00,01,01,64,04,01,01,64,04), the
remaining sectors are looking okay).<br/>

#### Porsche Challenge (USA) (SRC\MENU\STREAM\\*.STR)
The subheader and data of the 1st sector are accidently overwritten by some
ASCII string:<br/>
```
  000h 4    Subheader       01 44 2D 52            ".D-R"    ;\distorted
  004h 4    Subheader copy  01 4D 20 47            ".M G"    ;/"CD-ROM G"
  008h 299h Data ASCII      65 6E 65 72 61 ...     "enerator for Windows"...
  2A1h 567h Data BS bitstream (but lacks BS header and start of bitstream)
```
The 2nd sector and up are containing intact STR headers (for the 2nd-Nth sector
of 1st frame, but the whole 1st frame is unusable due to missing 1st sector;
however, the following frames are intact).<br/>



##   CDROM File Video BS Compression Versions
#### STR/BS Version Summary, with popularity in percents (roughly)
```
  Version         .STR movies   .BS pictures
  BS v2            60%           6%            Most games
  BS v3            20%           4%            Some newer games
  BS v1            15%           0.1%          Old games
  BS ea            2%            - (?)         Electronic Arts titles
  BS iki           0.5%          0.1%          Several games
  BS fraquant      0.2%          0.1%          Rare (X-Files, Eagle One)
  BS v0            0.1%          -             Rare (Serial Experiments Lain)
  BS v2/v3.crypt   0.2%          -             Rare (Star Wars games)
  BS iki.encrypted 0.1%          -             Rare (Panekit)
  Wacwac MDEC      0.1%          -             Rare (Aconcagua)
  Polygon Streams  0.x% (?)      -             Some titles
  Raw MDEC         -             -             Was never used in files?
  MPEG1            -             -             VCD Video CDs
  None             ?%   (?)      90%           No videos or BS pictures
```
Most games can decrypt v1/v2/v3 videos (no matter which of the three versions
they are actually using), newer games do occassionally use v3 for picture
compression, but often stick with v2 for video streaming (perhaps because v3
does require slightly more CPU load; unknown if the higher CPU load has been an
actual issue, and if it has been solved in the later (more optimized)
decompressor versions) (unknown if there are other benefits like v2 having
better DC quality or better compression in some cases?).<br/>

#### BS v0 (used by only one known game)
```
  v0 used by Serial Experiments Lain
```
This game is apparently using a very old and very unoptimized decoder (although
it was released in 1997, when most or all other games did already have decoders
with v1/v2/v3 support).<br/>
The v0 decoder has different header, lacks End of Frame codes, and uses Huffman
codes with different AC values than v1/v2/v3/iki.<br/>

#### BS v1 (used by older games, some of them also having v2 videos)
```
  v1 used by Wipeout 2097 (MAKE.AV, XTRO*.AV)
  v1 used by Viewpoint (MOVIES\*.STR) (oddly with [08h]=FirstFrame=0 and
        [1Ch]=Unspecified=Nonzero) (the game also has ".str" files in
        VIEW.DIR\streams, but that isn't MDEC/STR stuff)
  v1 used by Ridge Racer Revolution (MOVIE\*.STR)
  v1 used by Policenauts
  v1 used by Final Fantasy VII (FF7)
  v1? used by Tekken 2
  v1/v2 used by Final Fantasy Tactics (OPEN*.STR)
  v1/v2 used by Project Horned Owl (*.STR)
  v1/v2 used by Gex (*.FMV)
  (and probably more)
```
v1 and v2 can be decoded with the same decompressor. The only difference is
that v1 was generated with an older compressor (which did accidently store
nonsense 22bit escape codes with run=N, level=0 in the bitstream; whereas one
could as well use run+N+1 in the next code, or omit it completely if next code
is EOB).<br/>

#### BS v2 (most games)
```
  v2 used by Gex - Enter the Gecko (*.STR)
  v2 used by Tomb Raider (FMV\*.FMV)
  v2 used by Alone (STR*\*.STR)
  v2 used by Kain (*.STR)
  v2 used by Fear Effect (BOOT.SID, LOGO.SID, ABGA\ABGA.FLX)
  v2 used by Parasite Eve 2 (INTERx.STR, and in .CDF's eg. stage1\folder501)
  v2 used by Witch of Salzburg (MOVIE\*.STR)
  v2 used by Breath of Fire III (LOGO\*.STR)
  v2 used by Hear it Now (MOVIE\*.STR)
  v2 used by Legend of Mana (MOVIE\*.STR)
  v2 used by Misadventures of Tron Bonne (STR\*.STR)
  v2 used by Rayman (VIDEO\*.STR)
  v2 used by Resident Evil 1 (PSX\MOVIE\*.STR)                ;\although v3 is
  v2 used by Resident Evil 2 (PL0\ZMOVIE\*.STR, ZMOVIE\*.STR) ;/used in *.BSS
  v2 used by Tokimeki Memorial 2 (VX*.STR)
  v2 used by Spider-Man (CINEMAS\*.STR)
  v2 used by Perfect Assassin (CDV\*.STR)
  v2 used by Pandemonium 2 (*.STR)
  v2 used by Die Hard Trilogy 2 (MOVIE\*.STR)
  v2 used by Need for Speed 3 (MOVIES\*.STR) (oddly with [14h,18h]<>[20h,24h])
  v2 used by Wild Arms (STR\*.STR)
  v2 used by Wild Arms 2 (STR\*.STR)
  v2 used by Frogger (*.STR)
  v2 used by Gundam Battle Assault (XA\*.STR)
  v2 used by Alundra (MOVIE\*.MOV)
  v2 used by Spec Ops (file 95h,96h within BIGFILE.CAT)
  v2 used by Crash Team Racing (file 1E1h..1F8h,1FAh within BIGFILE.BIG)
  (and many more)
```
Same as v1, but without the compressor bug.<br/>

#### BS v3 (used by some newer games, some of them also having v2 videos)
```
  v2/v3 used by Lemmings Oh No More Lemmings (ANIMS\*.STR)
  v2/v3 used by Castlevania (*.STR)
  v3 used by Heart of Darkness (CINE\*.STR, SETUP\*.STR)
  v3 used by R-Types (MV\*.STR)
  v3 used by Black Matrix (MOVIE\*.STR)
  v3 used by Nightmare Creatures II (INTRO\*.STR, LEVEL*\*.STR)
  (and many more)
```
Same as v2, but using Huffman compressed DC values.<br/>

#### BS ea (Electronic Arts)
Used by many EA Sports titles and several other titles from Electronic Arts:<br/>
```
  Castrol Honda Superbike Racing
  EA Sports Supercross 2000, 2001
  Future Cop - L.A.P.D. (retail and MagDemo14: FCOPLAPD\*.WVE and *.FSV)
  Hot Wheels - Turbo Racing
  Jampack Vol. 2
  Knockout Kings 99, 2000, 2001
  Madden NFL 99, 2000, 2001, 2002, 2003, 2004, 2005 (eg. MADN00\FMVIDEO.DAT\*)
  NASCAR 98, 99, 2000, 2001 (and 98 Collector's Edition, and 99 Legacy)
  NASCAR Thunder 2002, 2003, 2004 and NASCAR Rumble
  Nuclear Strike
  Official U.S. PlayStation Magazine Demo Disc 39 (...XXX which game?)
  PlayStation Underground Jampack - Winter 2000
  Road Rash Jailbreak, and Road Rash 3D
  Tiger Woods PGA Tour Golf, and Tiger Woods USA Tour 2001
```
Uses VLC0 and MDEC chunks (instead of STR headers), the MDEC chunks contain
standard BS v2 data, but using custom MDEC values from VLC0 chunk.<br/>

#### BS fraquant
```
  X-Files (Fox Interactive/Hyperbole Studios, 1999)
  Eagle One: Harrier Attack (Infogrames/Glass Ghost, 2000)
  Blue's Clues: Blue's Big Musical (Mattel/Viacom/TerraGlyph, 2000)
```
This replaces the 6bit quant value by a 16bit fixed-point quant value (done by
manipulating the Quant Table instead of using QuantDC, apart from that extra
feature it's internally using normal BS v1/v2/v3 decoding).<br/>

#### BS iki
```
  iki: Gran Turismo 1 (STREAM.DAT)   ;\with uncommon STR header
  iki: Gran Turismo 2 (STREAM.DAT)   ;/
  iki: Hot Shots Golf 2 / Everybody's Golf 2 (MagDemo31: HSG2\MINGOL2X.BIN)
  iki: Legend of Legaia (MagDemo20: LEGAIA\MOV\MV2.STR)
  iki: Legend of Dragoon (STR\*.IKI)
  iki: Omega Boost (MOVIE\*.IKI)
  iki: Um Jammer Lammy (MagDemo24: UJL\*.IKI) (retail: *\*.IKI and CM\*.IK2)
  iki: plus a dozen of japanese-only titles
```
This might have been used between v2 and v3, iki is using uncommon BS headers
and LZ compressed Quant/DC values (whilst v3 is using Huffman compressed DC
values).<br/>

#### Encrypted iki
```
  Panekit - Infinitive Crafting Toy Case (first 13Mbyte in PANEKIT.STR)
```
Same as normal iki, with some SWAP/ADD/XOR-encrytion in first 20h-bytes.<br/>

#### Encrypted v2/v3
```
  v3.xor used by Star Wars Masters of Teras Kasi (MagDemo03: MASTERS\*.STR)
  v2.xor supported (but not actually used) by Star Wars Masters (MagDemo03)
  v3.swap used by Star Wars Rebel Assault II (*.STR, *.SED, Stills)
  v2.swap used by Star Wars Rebel Assault II (*.STR)
  v3.swap used by BallBlazer Champions (*.STR)
```
Same as normal v2/v3 with simple XOR-encryption or SWAP-encryption.<br/>

#### Wacwac MDEC
```
  Aconcagua (JP) (2000 Sony/WACWAC!) (STR_01_00.STR and STR_09_01.STR)
```
Similar to v3, but uses completely different Huffman codes than BS video.<br/>

#### Polygon Streaming (instead of MDEC picture streaming)
```
  Ape Escape (DEMO\*.STR, STR\*.STR, and KKIIDDZZ.HED\STR\0006h and up)
  Aconcagua (most STRs are Polygon Streams, except two are Wacwac MDEC streams)
  Panekit - Infinitive Crafting Toy Case (last 150Mbyte in PANEKIT.STR)
```
Polygon streams contain vertices (for textures that are stored elsewhere).
Usually needing only one sector per frame. This can be useful for animations
that were recorded from real actors. Drawbacks are more edgy graphics and lower
color depth (although that may fit in with the game engine).<br/>
[CDROM File Video Polygon Streaming](#cdrom-file-video-polygon-streaming)<br/>

#### MPEG1 (on VCD Video CDs)
MPEG1 uses I/P/B-Frames, the I-Frames may reach similar compression as BS
files. However, P-Frames and B-Frames do compress much better than BS files.<br/>
[CDROM Video CDs (VCD)](../cdromvideocdsvcd.md)<br/>
MPEG1 isn't used in any PSX games, but VCDs can be viewed on SCPH-5903 consoles
(or via software decoder in nocash PSX kernel clone).<br/>

#### Titles without movies
Most PSX titles do include movies, exceptions are some early launch titles and
educational titles:<br/>
```
  Ridge Racer 1 (1994)
  Lightspan Online Connection CD
```



##   CDROM File Video BS Compression Headers
There are several different BS headers. The File ID/Version entries can be used
to detect the correct type. The MDEC Size entry contains the size after Huffman
decompression (ie. the half-decompressed size before passing the data to the
MDEC decompression hardware) (usually divided by 4 and rounded up to 80h/4
bytes).<br/>

#### BS v1/v2/v3 header
```
  000h 2    MDEC Size/4 (after huffman decompression) (rounded to 80h/4 bytes)
  002h 2    File ID (3800h)
  004h 2    Quantization step/factor (0000h..003Fh, for MDEC "DCT.bit10-15")
  006h 2    Version (1, 2, or 3) (2 is most common)
  008h ...  Huffman compressed data blocks (Cr,Cb,Y1,Y2,Y3,Y4, Cr,Cb,Y1,Y2..)
```

#### Encrypted v2/v3
Encryption is used in Star Wars games, there are two encryption schemes (XOR
and SWAP).<br/>
XOR-encrypt: Star Wars Masters of Teras Kasi (MagDemo03: MASTERS\\*.STR):<br/>
```
  000h 2   MDEC Size/4 (rounded to 80h/4 bytes) (unencrypted) ;\same as normal
  002h 2   File ID (3800h)                      (unencrypted) ; BS v1/v2/v3
  004h 2   Quant (0..3Fh)                       (unencrypted) ;/
  006h 2   Version (in bit15, plus random in LSBs):
             00xxh..7FFFh for v2 (unknown if this could include values 0..3)
             8000h..FFFFh for v3 (bit14-0=random, varies in each frame)
  008h ..  Encrypted bitstream
             (each halfword XORed by BE67h for v2, or XORed by E67Bh for v3)
  ...  (2) Zeropadding to 4-byte boundary (unencrypted)
  ...  ..  Zeropadding to end of sector   (unencrypted)
 The XOR values BE67h/E67Bh are hardcoded in the Star Wars Masters of Teras
 Kasi .EXE (same XOR values for both retail and demo version), unknown if any
 other games are also using that kind of encryption (and if yes, if they are
 using the same XOR values).
```
SWAP-encrypt: BallBlazer Champions, Star Wars Rebel Assault II (\*.STR, \*.SED):<br/>
```
  000h 2   MDEC Size/4 (rounded to 80h/4 bytes) ;\same as normal
  002h 2   File ID (3800h)                      ; BS v1/v2/v3
  004h 2   Quant (0..3Fh)                       ;/
  006h 2   Version (random 16bit, 00xxh..FFFFh) ;-no meaningful version info
  008h 2   Bitstream 2nd halfword               ;\to "decrypt" the file,
  00Ah 2   Bitstream 1st halfword               ;/these must be swapped
  00Ch ..  Bitstream 3rd halfword and up        ;-in normal order
```
Whilst XORing or SWAPping the halfwords is simple, the more difficult part is
distinguishing between SWAP-v2/v3 and XOR-v2/v3 encryption. This can be done as
so:<br/>
```
  if header[06h]<=0003h then assume unencrypted v0/v1/v2/v3
  if header[06h]>=0004h then strip any trailing 0 bits, and check EndOfFrame..
  if last 10bit = 0111111111 then assume SWAP.v2
  if last 10bit = 1111111111 then assume SWAP.v3
  otherwise assume XOR.v2/v3 (and use header[06h].bit15 to distinguish v2/v3)
```

#### BS iki Header
IKI videos have a custom .BS header, including some GT-ZIP compressed data:<br/>
```
  000h 2   MDEC Size/4 (rounded to 80h/4 bytes)         ;\same as normal
  002h 2   File ID (3800h)                              ;/BS v1/v2/v3
  004h 2   Bitmap Width in pixels     ;instead of Quant
  006h 2   Bitmap Height in pixels    ;instead of Version
  008h 2   Size of GT-ZIP compressed data (plus 2-byte alignment padding)
  00Ah ..  GT-ZIP compressed DC/Quant values (plus 2-byte alignment padding)
  ...  ..  Huffman compressed AC data blocks (Cr,Cb,Y1,Y2,Y3,Y4, Cr,Cb,Y1,Y2..)
```
The number of blocks is NumBlocks=(Width+15)/16\*(height+15)/16\*6. The size of
the decompressed GT-ZIP data is NumBlocks\*2.<br/>

#### Encrypted iki
The first 20h byte of the iki header &amp; data are encrypted. Among others,
the ID 3800h is inverted (=C7FFh). To decrypt them:<br/>
```
  [buf+00h]=[buf+00h] XOR FFFFFFFFh
  [buf+04h] <--> [buf+08h]          ;exchange 2x32bit
  [buf+0Ch] <--> [buf+0Eh]          ;exchange 2x16bit
  [buf+10h]=[buf+10h]+FFFF6F7Bh
  [buf+14h]=[buf+14h]+69140000h
  [buf+18h]=[buf+18h]+FFFF7761h
  [buf+1Ch]=[buf+1Ch]+6B040000h
```
Note: The .STR header's StHeadM/StHeadV fields contain a copy of the decrypted
values. The PANEKIT.STR file is 170Mbyte tall, but only the first 13Mbyte
contain movie data... the rest is unknown stuff... often with zeroes followed
by 7B,44,F0,29,E0,28 unknown what for...?<br/>

#### BS fraquant
```
  X-Files, GRAPHICS\*.STR,*.BIN, LOGOS\*.STR,*.BS
  Eagle One: Harrier Attack (\*.STR, DATA*\*.STR) (leading zerofilled sectors)
  Blue's Clues: Blue's Big Musical (*.STR) (has one leading zerofilled sector)
```
This has a normal BS v1/v2/v3 header, with special quant entry:<br/>
```
  004h 2    Quant (0001h..0003h, or fixed-point 8000h..9xxxh)
```
The decoder is using the default\_quant\_table (02h,10h,10h,13h,..,53h)
multiplied with a fixed point number:<br/>
```
  quant=BsHeader[04h]   ;get fractional quant value
  BsHeader[04h]=0001h   ;force quant=1 (for use in BS v1/v2/v3 decoder)
  if quant<8000h then quant=quant*200h else quant=quant AND 7FFFh
  quant[0]=default_quant_table[0]
  for i=1 to 3Fh,
    x=(default_quant_table[i]*quant)/200h
    if x=00000000h then quant[i]=01h else quant[i]=(x AND FFh)
  next i
  use MDEC(2) command to apply quant[0..3Fh] to both Luma and Chroma tables
  use normal BS v1/v2/v3 decoder to decompress the bitmap
```
BsHeader[04h] should be 0001h..0003h, or 8000h..862Bh (values outside that
range would overflow the 8bit quant table entries). Values 0001h..0003h should
should give same results as for normal BS decoding, so only values 8000h and up
do need special decoding.<br/>
Caution: Despite of the overflows, quant\>862Bh is used (eg. X-Files
GRAPHICS\GRAPHICS.BIN has quant=88C4h, Blue's Big Musical has quant=93E9h;
those images do look okay, so the compressor seems to have recursed the
overflows; or the overflow affects only a few pixels), however, very large with
LSBs all zero (eg. 9000h) can cause 8bit table entries to become 00h (due to
ANDing the result with FFh).<br/>
Note: X-Files LOGOS\POP\*.STR have quant=8001h (=near zero), that files are only
60Kbyte and seem to be all black.<br/>
Note: The movie engine uses COP2 GPF opcodes to calculate quant values.<br/>

#### v0 Header (in STR files)
```
  000h 1   Quant for Y1,Y2,Y3,Y4  (00h..3Fh)
  001h 1   Quant for Cr,Cb        (00h..3Fh)
  002h 2   File ID (3800h) (or Frame Number in ENDROLL1.STR on Disc 2)
  004h 2   MDEC Size/2 (!), and without padding (!) (unlike v1/v2/v3/iki)
  006h 2   BS Version (0) (actually MSBs of above Size, but it's always 0)
  008h ..  Huffman Bitstream, first bit in bit7 of first byte
```

#### v0 Header (in LAPKS.BIN chunks)
LAPKS.BIN contains several chunks, each chunk contains an animation sequence
with picture frame(s), each frame starts with following header:<br/>
```
  000h 2   Bitmap Width in pixels     ;\cropped to non-black screen area,
  002h 2   Bitmap Height in pixels    ;/size can vary within the sequence
  004h 2   Quant for Y1,Y2,Y3,Y4  (0000h..003Fh)
  006h 2   Quant for Cr,Cb        (0000h..003Fh)
  008h 4   Size of compressed BS Bitstream plus 4 ;Transparency at [008h]+0Ch
  00Ch 2   Size/2 of MDEC data (after huffman decompression, without padding)
  00Eh 2   BS Version (0) (actually MSBs of above Size, but it's always 0)
  010h ..  BS Bitstream with DC and AC values (Huffman compressed MDEC data)
  ...  4   Transparency Mask Decompressed Size (Width*Height*2/8) (=2bpp)
  ...  ..  Transparency Mask LZSS-compressed data
```
For decompressing the transparency mask:<br/>
[CDROM File Compression LZSS (Serial Experiments Lain)](compression.md#cdrom-file-compression-lzss-serial-experiments-lain)<br/>
The Transparency Mask is stored as scanlines (not as macroblocks), the
upper/left pixel is in bit7-6 of first byte, the 2bit alpha values are ranging
from 0=Transparent to 3=Solid.<br/>

#### BS ea Headers (Electronic Arts)
EA videos are chunk based (instead of using 20h-byte .STR headers).<br/>
[CDROM File Video Streaming Chunk-based formats](#cdrom-file-video-streaming-chunk-based-formats)<br/>
VLC0 Chunk: Custom MDEC values (to be assigned to normal BS v2 Huffman codes).<br/>
MDEC Chunks: Width/Height and BS v2 data (using MDEC values from VLC0 chunk).<br/>

#### Raw MDEC
There aren't any known pictures or movies in raw MDEC format. However, the
Huffman decompression functions do usually output raw data in this format:<br/>
```
  000h 2   MDEC Size/4 (after huffman decompression) (rounded to 80h/4 bytes)
  002h 2   File ID (3800h)
  004h ..  MDEC data (16bit DC/AC/EOB codes)
  ...  ..  Padding (FE00h-filled to 80h-byte DMA transfer block size boundary)
```
The first 4 bytes are the MDEC(1) command, the "ID" is always 3800h (equivalent
to selecting 16bpp output; for 24bpp this must be changed to 3000h before
passing the command to the MDEC hardware). The remaining bytes are MDEC data
(padded to 80h-byte boundary).<br/>
[Macroblock Decoder (MDEC)](../../cpu/mdec/macroblockdecodermdec.md)<br/>



##   CDROM File Video BS Compression DC Values
#### DC v0
```
  nnnnnnnnnn        DC Value (signed 10bit, -200h..+1FFh)
```
This is similar as v1/v2, except there is no End code for End of Frame, and the
.BS header contains two separate quant values (for Cr/Cb and Y1-Y4).<br/>
```
  If output_size=NumberOfMdecCodes*2 then EndOfFrame
  If BlockIsCrCb then QuantDC=DC+QuantC*400h else QuantDC=DC+QuantY*400h
```

#### DC v1/v2/ea
```
  nnnnnnnnnn        DC Value (signed 10bit, -200h..+1FEh)
  0111111111        End of Frame (+1FFh, that, in place of Cr)
```
This is similar as v0, except there is only one Quant value for all blocks, and
the header lacks info about the exact decompressed size, instead, compression
end is indicated by a newly added end code:<br/>
```
  If DC=+1FFh then EndOfFrame
  QuantDC=DC+Quant*400h
```

#### DC v3
Similar as v1/v2, but DC values (and End code) are now Huffman compressed
offsets relative to old DC, with different Huffman codes for Cr/Cb and Y1-Y4:<br/>
```
  For Cr/Cb         For Y1..Y4      Offset (added to old DC of Y/Cr/Cb block)
  00                100             +(00h)                      ;\
  01s               00s             -(01h)*4     ,+(01h)*4      ;
  10sn              01sn            -(03h..02h)*4,+(02h..03h)*4 ; required
  110snn            101snn          -(07h..04h)*4,+(04h..07h)*4 ; codes
  1110snnn          110snnn         -(0Fh..08h)*4,+(08h..0Fh)*4 ; for 10bit
  11110snnnn        1110snnnn       -(1Fh..10h)*4,+(10h..1Fh)*4 ; range
  111110snnnnn      11110snnnnn     -(3Fh..20h)*4,+(20h..3Fh)*4 ;
  1111110snnnnnn    111110snnnnnn   -(7Fh..40h)*4,+(40h..7Fh)*4 ;/
  11111110snnnnnnn  1111110snnnnnnn -(FFh..80h)*4,+(80h..FFh)*4 ;-11bit (!)
  -                 11111110        Unused                      ;\
  111111110         111111110       Unused                      ; unused
  1111111110        1111111110      Unused                      ;/
  1111111111        1111111111      End of Frame                ;-end code
  Note: the "snnn" bits are indexing the values in right column,
  with s=0 for negative values, and s=1 for positive values.
```
The decoding works as so (with oldDcXxx=0 for first macroblock):<br/>
```
  If bits=1111111111 then EndOfFrame
  If BlockIsCr then DC=DecodeHuffman(HuffmanCodesCbCr)+oldDcCr, oldDcCr=DC
  If BlockIsCb then DC=DecodeHuffman(HuffmanCodesCbCr)+oldDcCb, oldDcCb=DC
  If BlockIsY1234 then DC=DecodeHuffman(HuffmanCodesY1234)+oldDcY, oldDcY=DC
  If older_version AND DC>=0 then QuantDC=Quant*400h or (DC)       ;\requires
  If older_version AND DC<0  then QuantDC=Quant*400h or (DC+400h)  ;/11bit
  If newer_version           then QuantDC=Quant*400h+(DC AND 3FFh) ;-wrap 10bit
```
Note: The offsets do cover signed 11bit range -3FCh..+3FCh. Older v3 decoders
did require 11bit offsets (eg. add +3FCh to change DC from -200h to +1FCh).
Newer v3 decoders can wrap within 10bit (eg. add -4 to wrap DC from -200h to
+1FCh).<br/>

#### DC iki
The DC values (including Quant values for each block) are separately stored as
GT-ZIP compressed data in the IKI .BS header.<br/>
[CDROM File Compression GT-ZIP (Gran Turismo 1 and 2)](compression.md#cdrom-file-compression-gt-zip-gran-turismo-1-and-2)<br/>
Calculate NumBlocks=(Width+15)/16\*(height+15)/16\*6, decompress the DC values
(until DecompressedSize=NumBlocks\*2). During Huffman decompression, read the DC
values from the decompressed DC buffer (instead of from the Huffman bitstream):<br/>
```
  If BlockNo>=NumBlocks then EndOfFrame
  QuantDC = DCbuf[BlockNo]*100h + DCbuf[BlockNo+NumBlocks]
```
As shown above, the Hi- and Lo-bytes are stored in separate halves of the DC
buffer (which may gain better compression).<br/>



##   CDROM File Video BS Compression AC Values
Below shows the huffman codes and corresponding 16bit MDEC values; the "xx"
bits contain an index in the list of 16bit MDEC values, the "s" bit means to
negate the AC level (in lower 10bit of the 16bit MDEC value) when s=1.<br/>

#### Huffman codes for AC values BS v1/v2/v3/iki
```
  10                     FE00h          ;End of Block, EOB
  11s                    0001h
  011s                   0401h
  010xs                  0002h,0801h
  0011xs                 1001h,0C01h
  00101s                 0003h
  00100xxxs              3401h,0006h,3001h,2C01h,0C02h,0403h,0005h,2801h
  0001xxs                1C01h,1801h,0402h,1401h
  00001xxs               0802h,2401h,0004h,2001h
  000001xxxxxxxxxxxxxxxx 0000h..FFFFh   ;Escape code for raw 16bit values
  000001xxxxxx0000000000 0000h..FC00h   ;Escape nonsense level=0 (used in v1)
  0000001xxxs            4001h,1402h,0007h,0803h,0404h,3C01h,3801h,1002h
  00000001xxxxs          000Bh,2002h,1003h,000Ah,0804h,1C02h,5401h,5001h,
                         0009h,4C01h,4801h,0405h,0C03h,0008h,1802h,4401h
  000000001xxxxs         2802h,2402h,1403h,0C04h,0805h,0407h,0406h,000Fh,
                         000Eh,000Dh,000Ch,6801h,6401h,6001h,5C01h,5801h
  0000000001xxxxs        001Fh,001Eh,001Dh,001Ch,001Bh,001Ah,0019h,0018h,
                         0017h,0016h,0015h,0014h,0013h,0012h,0011h,0010h
  00000000001xxxxs       0028h,0027h,0026h,0025h,0024h,0023h,0022h,0021h,
                         0020h,040Eh,040Dh,040Ch,040Bh,040Ah,0409h,0408h
  000000000001xxxxs      0412h,0411h,0410h,040Fh,1803h,4002h,3C02h,3802h,
                         3402h,3002h,2C02h,7C01h,7801h,7401h,7001h,6C01h
  000000000000           Unused
```

#### Huffman codes for AC values BS v0 (Serial Experiments Lain)
```
  10                           FE00h          ;End of Block, EOB
  11s                          0001h
  011s                         0002h
  010xs                        0401h,0003h
  0011xs                       0801h,0005h
  00101s                       0004h
  00100xxxs                    000Ah,000Bh,0403h,1801h,000Ch,000Dh,1C01h,000Eh
  0001xxs                      0006h,0C01h,0402h,0007h
  00001xxs                     0008h,1001h,0009h,1401h
  000001xxxxxx0xxxxxxx         0000h..FC00h+(+001h..+07Fh AND 3FFh) ;\
  000001xxxxxx000000001xxxxxxx 0000h..FC00h+(+080h..+0FFh AND 3FFh) ; Escape
  000001xxxxxx000000000xxxxxxx Unused                               ; codes
  000001xxxxxx1xxxxxxx         0000h..FC00h+(-080h..-001h AND 3FFh) ;
  000001xxxxxx100000000xxxxxxx 0000h..FC00h+(-100h..-081h AND 3FFh) ;
  000001xxxxxx100000001xxxxxxx Unused                               ;/
  0000001xxxs                  000Fh,0802h,2001h,0404h,0010h,0011h,2401h,0012h
  00000001xxxxs                0013h,0405h,0014h,2801h,0015h,0C02h,3001h,0017h,
                               0016h,2C01h,0018h,001Ch,0019h,0406h,0803h,001Bh
  000000001xxxxs               001Ah,3401h,001Dh,0407h,1002h,001Fh,001Eh,3801h,
                               0020h,0021h,0408h,0023h,0022h,1402h,0024h,0025h
  0000000001xxxxs              0804h,0409h,0418h,0026h,3C01h,0027h,0C03h,1C03h,
                               0028h,0029h,002Ah,002Bh,040Ah,002Ch,1802h,002Dh
  00000000001xxxxs             002Fh,002Eh,4001h,0805h,0030h,040Bh,0031h,0033h,
                               0032h,1C02h,0034h,1003h,0035h,4401h,040Ch,0037h
  000000000001xxxxs            0036h,0038h,0039h,5401h,003Ah,0C04h,040Dh,5C01h,
                               2002h,003Bh,0806h,4C01h,003Ch,2402h,6001h,4801h
  000000000000                 Unused
```
Uses different 16bit MDEC values, and the Escape code is different: 8bit levels
are 2bit shorter than v1/v2/v3, but 9bit levels are much longer, and 10bit
levels are not supported at all (those v0 Escape codes are described in Sony's
File Format documented; albeit accidentally because the doc was actually trying
to describe v2/v3).<br/>

#### Huffman codes for AC values BS ea (Electronic Arts)
This is using custom MDEC values from VLC0 chunk, and assigns them to the
standard Huffman codes. There are two special MDEC values:<br/>
```
  FE00h End of Block (EOB)
  7C1Fh Escape code (huffman code will be followed by v2-style 16bit value)
```
VLC0 chunk entries 00h..DFh are mapped to the following Huffman codes:<br/>
```
  10                   00
  11x                  01,02
  011x                 03,04
  010xx                05,06,07,08
  0011xx               0D,0E,0B,0C
  00101x               09,0A
  00100xxxx            2E,2F,22,23,2C,2D,2A,2B,26,27,24,25,20,21,28,29
  0001xxx              15,16,13,14,0F,10,11,12
  00001xxx             1A,1B,1E,1F,18,19,1C,1D
  000001               17h
  0000001xxxx          3E,3F,38,39,30,31,34,35,32,33,3C,3D,3A,3B,36,37
  00000001xxxxx        46,47,54,55,4E,4F,44,45,4A,4B,52,53,5E,5F,5C,5D,
                       42,43,5A,5B,58,59,48,49,4C,4D,40,41,50,51,56,57
  000000001xxxxx       74,75,72,73,70,71,6E,6F,6C,6D,6A,6B,68,69,66,67,
                       64,65,62,63,60,61,7E,7F,7C,7D,7A,7B,78,79,76,77
  0000000001xxxxx      9E,9F,9C,9D,9A,9B,98,99,96,97,94,95,92,93,90,91,
                       8E,8F,8C,8D,8A,8B,88,89,86,87,84,85,82,83,80,81
  00000000001xxxxx     B0,B1,AE,AF,AC,AD,AA,AB,A8,A9,A6,A7,A4,A5,A2,A3,
                       A0,A1,BE,BF,BC,BD,BA,BB,B8,B9,B6,B7,B4,B5,B2,B3
  000000000001xxxxx    C6,C7,C4,C5,C2,C3,C0,C1,C8,C9,D4,D5,D2,D3,D0,D1,
                       CE,CF,CC,CD,CA,CB,DE,DF,DC,DD,DA,DB,D8,D9,D6,D7
  000000000000         Unused
```
All codes can be freely assigned (Escape and EOB don't need to be at 10 and
000001, and the last huffman bit doesn't have to serve as sign bit).<br/>

#### Notes
All BS versions are using the same Huffman codes (the different BS versions do
just assign different 16bit MDEC codes to them).<br/>
The huffman codes can be neatly decoded by "counting leading zeroes" (without
needing bitwise node-by-node processing; this is done in IKI video decoders via
GTE registers LZCS and LZCR). Sony's normal v2/v3 decoders are using a yet
faster method: A large table to interprete the next 13bit of the bitstream, the
table lookup can decode up to 3 huffman codes at once (if the 13bit contain
several small huffman codes).<br/>



##   CDROM File Video BS Picture Files
#### BS Picture Files
A couple of games are storing single pictures in .BS files:<br/>
```
  Alice in Cyberland (ALICE.PAC\*.BS)
  BallBlazer Champions (BBX_EXTR.DAT\Pics\*) (SWAP-encrypted)
  Bugriders: The Race of Kings (*\*.BS and STILLS\MENUS.BS\*)
  Die Hard Trilogy 2 (DATA\*.DHB, DATA\DH*\L*\*.DHB, MOVIE\*.DHB)
  Dino Crisis 2 (PSX\DATA\ST*.DBS\*)
  Duke Nukem (MagDemo12: DN_TTK\*)
  Final Fantasy VII (FF7) (MOVIE\FSHIP2*.BIN\*) (BS v1)
  Gran Turismo 1 (retail TITLE.DAT\* and MagDemo10/15) (in BS iki format)
  Jet Moto 2 (MagDemo03: JETMOTO2\*)
  Mary-Kate and Ashley Crush Course (MagDemo52: CRUSH\SCRN\*.BS)
  Mat Hoffman's Pro BMX (MagDemo48: MHPB\STILLS.BIN\*) (with width/height info)
  NFL Gameday '99 (MagDemo17: GAMEDAY\FE\GD98DATA.DAT)
  Official U.S. PlayStation Magazine Demo Disc 01-02 (MENU\DATA\*.BSS)
  Official U.S. PlayStation Magazine Demo Disc 03-54 (MENU.FF\*)
  Parasite Eve 2 (INIT.BS, and within .HED/.CDF archives)
  Resident Evil 1 (PSX\STAGE*\*.BSS, headerless archive, 8000h-byte align)
  Resident Evil 2 (COMMON\BSS\*.BSS, headerless archive, 10000h-byte align)
  Rugrats (MagDemo19: RUGRATS\*)
  Rugrats Studio Tour (MagDemo32: RUGRATS\DATA\RAW\*.BS)
  Starwars Demolition (MagDemo39+MagDemo41: STARWARS\SHELL\.BS+.TBL\*)
  Star Wars Rebel Assault 2 (RESOURCE.000\Stills\*) (SWAP-encrypted)
  Ultimate Fighting Championship (MagDemo38: UFC\CU00.RBB\390h..3E2h)
  Vigilante 8 (MagDemo09: EXAMPLE\*)
  Witch of Salzburg (PICT\PIC*\*.BS and DOT1 archives *.BSS, *.DAT, *.BIN)
  X-Files (LOGOS\*.BS and GRAPHICS\GRAPHICS.BIN and GRAPHICS\PACKEDBS.BIN\*)
  You Don't Know Jack 2 (MagDemo41: YDKJV2\RES\UI\*.BS)
```
Note: Those .BS files are usually hidden in custom file archives.<br/>

#### BS Picture Resolution
Movies have Width/Height entries (in the .STR header). Raw .BS picture files
don't have any such information. However, there are ways to guess the correct
resolution:<br/>
```
  For BS iki format, use resolution from iki header (eg. Gran Turismo 1)
  For MHPB\STILLS.BIN, there's width/height in chunk headers
  Count the number of blocks (EOB codes) during Huffman decompression
  Divide that number by 6 to get the number of Macroblocks
  Search matches for Height=NumBlocks/Width with Width>=Height and Remainder=0
  If Height=300..400, assume double H-resolution, repeat with Width/2>=Height
  And/or use a list of known common resoltions (see below examples)
  Search arrangements with many similar colors on adjacent macroblocks
```
Common resolutions are:<br/>
```
  Blocks Pixels   Example
  F0h    256x240  any?
  12Ch   320x240  Resident Evil 2 (COMMON\BSS\*.BSS)
  1E0h   512x240  Demo Disc 03-54 (MENU.FF\*), Duke Nukem (MagDemo12)
  1E0h   640x192  Less common than above (but used by Witch of Salzburg)
  4B0h   640x480  Vigilante 8 (MagDemo09), Jet Moto 2 (MagDemo03)
  var    random   Witch of Salzburg has various random resolutions
  iki    ikihdr   Gran Turismo 1 has A0hxA0h and odd size (!) E8hx28h
  ?      ?        Final Fantasy VII (FF7)
  ?      ?        Ultimate Fighting Championship (UFC\CU00.RBB\3B7h..3E2h)
  118h   320x224  Alice in Cyberland (most files; or two such as panorama)
  230h   ?        Alice in Cyberland (AD_115.BS and AD_123A.BS)
```
Some other possible, but rather unlikely results would be:<br/>
```
  C8h    320x160  Unlikely for pictures (but used for STR videos, eg. Alone)
  F0h    320x192  Unlikely for pictures (but used for STR videos, eg. Wipeout)
  1E0h   384x320  Very unlikely to see that vertical resolution on PSX
```
Witch of Salzburg has many small .BS files with various uncommon resolutions
(most of them are bundled with 16-byte .TXT files with resolution info).<br/>

#### Extended BS with Width/Height
Starwars Demolition (MagDemo39: STARWARS\SHELL\DEMOLOGO.BS+RESOURCE.TBL\\*)<br/>
Starwars Demolition (MagDemo41: STARWARS\SHELL\DEMOLOGO.BS+RESOURCE.TBL\\*)<br/>
```
  000h 2    Width  (280h)       ;\extra header
  002h 2    Height (1E0h)       ;/
  004h 2    MDEC Size/4 (after huffman decompression) (rounded to 80h/4 bytes)
  006h 2    File ID (3800h)
  008h 2    Quantization step/factor (0000h..003Fh, for MDEC "DCT.bit10-15")
  00Ah 2    Version (1, 2, or 3) (2 is most common)
  00Ch ...  Huffman compressed data blocks (Cr,Cb,Y1,Y2,Y3,Y4, Cr,Cb,Y1,Y2..)
```



##   CDROM File Video Wacwac MDEC Streams
Wacwac uses different Huffman codes than BS videos, the decoder has some
promising ideas that might yield slightly better compression than BS v3.
However, it is used by only one known game:<br/>
```
  Aconcagua (JP) (2000 Sony/WACWAC!)
```
And even that game is only using it in two movies, and the movies are barely
making any use of it: The 20Mbyte intro scene is a picture slide show (where
the camera is zooming across twelve black and white images), the 50Mbyte ending
scene is providing a more cinematic experience (the camera is scrolling through
a text file with developer staff names).<br/>

#### Wacwac MDEC Stream Sectors
```
  000h 2    STR ID   (0160h)
  002h 2    STR Type WACWAC Tables (0002h=IntroTableSet, 0003h=EndingTableSet)
  004h 2    Sector number within current Frame (0000h..num-1)
  006h 2    Number of Sectors in this Frame
  008h 4    Frame number (6 or 11 and up, because 1st some frames are Polygons)
  00Ch 4    Frame Size in bytes
  010h 2    Bitmap Width  (always 140h)  ;\always 320x208 (in fact, the
  012h 2    Bitmap Height (always 0D0h)  ;/decoder is hardcoded as so)
  014h 4    Quant (0..3Fh) (same for all sectors within the frame)
  018h 8    Zerofilled
  020h 7E0h Raw Bitstream data (without Quant or BS header) (garbage padded)
```
Aconcagua has dozens of STR files with Polygon Streams. MDEC Streams are found
only in two STR files for Intro and Ending scenes:<br/>
```
  Intro=Disc1:\ST01_01\STR_01_00.STR     Ending=Disc2:\ST09_01\STR_09_01.STR
  Leading zeroes (150 sectors)           Leading zeroes (150 sectors)
  Frame 0001h..0005h Polygon Frames      Frame 0001h..000Ah Polygon Frames
  Frame 0006h..0545h MDEC Frames 20MB    Frame 000Bh..0D79h MDEC Frames 50MB
  Frame 0546h..1874h Polygon Frames 48MB
```
Audio is normal XA-ADPCM, with the first audio sector occuring before 1st frame
(after the leading zeropadded 150 sectors).<br/>

#### Wacwac Huffman Bitstreams
Wacwac uses little-endian bitstreams (starting with low bit in bit0 of first
byte). To decode the separate blocks in the bitstream:<br/>
```
  Read Huffman code for DC, and output Quant*400h+(DC AND 3FFh)
  Read Huffman code for Size, aka num1,num2,num3 values for below reads
  Repeat num1 times: Read Huffman code for AC1, and output AC
  Repeat num2 times: Read Huffman code for AC2, and output AC
  Repeat num3 times: Read Huffman code for AC3, and output AC
  Output EOB (end of block)
```
The header/data lacks info about MDEC size after Huffman decompression, the
worst case size for 320x208pix would be:<br/>
```
  14h*0Dh*6*41h*2+Align(80h)+Header(4) = 31880h+4 bytes
```
Note: The bitstream consists of separate 16x208pix slices (set DC for Cr,Cb,Y
to zero at begin of each slice, and skip padding to 32bit-boundary at end of
each slice).<br/>

#### Wacwac Huffman Table Sets
Aconcagua has two table sets, stored in PROGRAM.BIN (in compressed form,
appearing as so: FF,90,16,2E,06,20,03,D6,etc). While watching the intro movie,
the uncompressed sets can be found at these RAM locations:<br/>
```
  80112AF8h (1690h bytes)  ;Table Set for Intro Scene
  80114188h (1B68h bytes)  ;Table Set for Ending Scene
```
Each Table Set has a 38h-byte header, followed by five tables:<br/>
```
  000h 4    Table Set size (1690h or 1B68h)
  004h 4    Table Set exploded size (when allocating 16bit/DC, 32bit/Size/AC)
  008h 2    Size Table max Huffman size in bits  (0Ah or 09h)           ;\Size
  00Ah 2    Size Table number of entries         (40h)                  ;/
  00Ch 2    DC Table max Huffman size in bits    (0Bh)                  ;\
  00Eh 2    DC Table number of entries           (100h)                 ; DC
  010h 2    DC Huffman code Escape 10bit (non-relative 10bit DC value)  ;
  012h 2    DC Huffman size Escape 10bit (3 or 6, escape prefix size)   ;/
  014h 2    AC1 Table max Huffman size in bits   (0Eh or 0Bh)           ;\
  016h 2    AC1 Table number of entries          (0DAh or 100h)         ;
  018h 2    AC1 Huffman code Escape 7bit  (run=0bit, level=signed7bit)  ; AC1
  01Ah 2    AC1 Huffman code Escape 16bit (run=6bit, level=10bit)       ;
  01Ch 2    AC1 Huffman size Escape 7bit  (9 or 7, escape prefix size)  ;
  01Eh 2    AC1 Huffman size Escape 16bit (9 or 7, escape prefix size)  ;/
  020h 2    AC2 Table max Huffman size in bits   (0Eh)                  ;\
  022h 2    AC2 Table number of entries          (AAh or F4h)           ;
  024h 2    AC2 Huffman code Escape 8bit  (run=3bit, level=signed5bit)  ; AC2
  026h 2    AC2 Huffman code Escape 16bit (run=6bit, level=10bit)       ;
  028h 2    AC2 Huffman size Escape 8bit  (10 or 9, escape prefix size) ;
  02Ah 2    AC2 Huffman size Escape 16bit (10 or 9, escape prefix size) ;/
  02Ch 2    AC3 Table max Huffman size in bits   (0Eh)                  ;\
  02Eh 2    AC3 Table number of entries          (87h or B2h)           ;
  030h 2    AC3 Huffman code Escape 8bit  (run=4bit, level=signed4bit)  ; AC3
  032h 2    AC3 Huffman code Escape 16bit (run=6bit, level=10bit)       ;
  034h 2    AC3 Huffman size Escape 8bit  (10 or 9, escape prefix size) ;
  036h 2    AC3 Huffman size Escape 16bit (10 or 9, escape prefix size) ;/
  038h ..   Size Table (64bit per entry)    ;\
  ...  ..   DC Table   (32bit per entry)    ;
  ...  ..   AC1 Table  (64bit per entry)    ; Tables
  ...  ..   AC2 Table  (64bit per entry)    ;
  ...  ..   AC3 Table  (64bit per entry)    ;/
```
Size Table entries (64bit):<br/>
```
  0-1    Zero
  2-31   Huffman code (10bit max)
  32-39  Number of AC1 codes in this block  ;\implies End of Block (EOB)
  40-47  Number of AC2 codes in this block  ; after those AC codes
  48-55  Number of AC3 codes in this block  ;/
  56-63  Huffman size (1..10 bits)
```
DC Table entries (32bit):<br/>
```
  0-9    Relative DC Value (relative to old DC from memorized Cr,Cb,Y)
  10-15  Huffman size (1..11 bits)
  16-31  Huffman code (11bit max)
 Notes: For the relative DC's, the decoder does memorize DC for Cr,Cb,Y upon
  decoding Cr,Cb,Y1,Y3 (but does NOT memorize DC when decoding Y2,Y4).
  Initial DC for Cr,Cb,Y is zero at begin of each 16x208pix slice.
 Obscurities: The decoder does accidentally use bit10 to sign-expand the
  DC value in bit0-9 (but does mask-off those bugged sign bits thereafter),
  and the decoder does uselessly memorize Y1 and Y3 separately (but uses only
  the most recently memorized value).
```
AC1/AC2/AC3 Table entries (64bit):<br/>
```
  0-1    Zero
  2-31   Huffman code (14bit max)
  32-47  MDEC code (6bit run, and 10bit AC level)
  48-63  Huffman size (1..14 bits)
```
The Escape codes are stored in the 38h-byte Table Set header (instead of in the
tables), the init function uses that info for patching escape-related opcodes
in the decoder function (that would allow to omit table lookups upon escape
codes; the decoder doesn't actually omit such lookups though).<br/>
To simplify things, one could store the escape codes in the tables (eg. using
special MDEC values like FC00h+35h for run=3bit, level=signed5bit).<br/>



##   CDROM File Video Polygon Streaming
#### Ape Escape - Polygon Streaming
Used by Ape Escape (Sony 1999) (DEMO\\*.STR and some STR\\*.STR files and
KKIIDDZZ.HED\STR\0006h and up).<br/>
The files start with zerofilled sectors (without STR headers), followed by
sectors with STR headers with [00h]=0160h, [02h]=8001h (same values as for
MDEC), but with [10h..1Fh]=zero (without resolution/header info). And the data
at [20h] starts with something like 14h,00h,03h,FFh,2Ah,02h,00h,00h.<br/>
That data seems to consist of polygon coordinates/attributes that are rendered
as movie frames. The texture seems to be stored elsewhere (maybe in the .ALL
files that are bundled with some .STR files).<br/>

#### Panekit - Polygon Streaming
Panekit STR seems to use Polygon Streaming (except 1st some Megabytes are
MDEC).<br/>

#### Aconcagua - Polygon Streaming
Aconcagua STR does use Polygon Streaming (except first+last movie are MDEC).<br/>

#### Cyberia (1996) (TF\STR\\*.STR)
Cyberia is using Software-rendering for both movies and in-game graphics. That
is, PSX hardware features like MDEC, GTE, and GPU-Polygons are left all unused,
and the GPU is barely used for transferring data from CPU to VRAM.<br/>
The STR header for software-rendered movie frames looks as so:<br/>
```
  000h 2    STR ID   (0160h)
  002h 2    STR Type (0002h=Custom, Software rendering)
  004h 2    Sector number within current Frame (0..num-1)
  006h 2    Number of Sectors in this Frame    (varies)
  008h 4    Frame Number (1=First)
  00Ch 4    Frame Size in Bytes/4 (note: first frame in MAP*.STR is quite big)
  010h 2    Rendering Width  (0140h)
  012h 2    Rendering Height (00C0h)
  014h 0Ch  Unknown (zerofilled or random garbage)
  020h 7E0h Custom data for software rendering
```
Note: First sector of First frame does usually have byte[22h]=88h (except
FINMUS.STR). The Custom data part is often have garbage padding (such like
ASCII strings with "c2str" command line tool usage instructions).<br/>

#### Croc 1 (CUTS\\*.AN2)
Probably cut-scenes with polygon animations. The files seem to contain
2300h-byte data frames (plus XA-ADPCM sectors inserted here and there).<br/>
```
  000h 4     Number of remaining frames
  ...  22FCh Unknown data (zeropadded if smaller)
```

```
 _______________ Unknown Streaming Data (Polygons or whatever) ________________
```

#### Custom STR - 3D Baseball (BIGFILE.FOO)
This is used for several files in 3D Baseball (BIGFILE.FOO):<br/>
```
  BIGFILE.FOO\0151h\0005h,0009h,000Fh,0017h,001Bh, 02E5h,02E9h,..,0344h,0348h
  BIGFILE.FOO\0152h\0186h,018Ch,0192h,0198h)
  BIGFILE.FOO\0153h\029Ah,02A0h,02A6h,02ACh)
```
The files contain some kind of custom streaming data, with custom STR header,
and data containing increasing/decreasing bytes... maybe non-audio waveforms?<br/>
```
  000h 2    STR ID   (0160h)
  002h 2    STR Type (0001h=Custom)
  004h 2    Sector number within current Frame (always 0)
  006h 2    Number of Sectors in this Frame    (always 1)
  008h 4    Frame Number (1=First)
  00Ch 4    Frame Size (6FAh or 77Ah, sometimes 17Ah or 1FAh or 20Ah)
  010h 2    Unknown (280h, or sometimes 300h or 340h)
  012h 2    Frame Time (0=First, increases with step [19h], usually +5 or +7)
  014h 2    Unknown (280h, or sometimes 300h or 3C0h, or 0)
  016h 1    Frame Time (same as [012h] AND FFh)
  017h 1    Unknown (0 or 1)
  018h 1    Unknown (40h, or 80h, or C0h)
  019h 1    Duration? (5 or 7, or sometimes less, step for Frame Time)
  01Ah 1    Unknown (3, or less in last some frames)
  01Bh 5    Zerofilled
  020h 7E0h Data (increasing/decreasing bytes... maybe non-audio waveforms?)
```

#### Army Men Air Attack 2 (MagDemo40: AMAA2\\*.PMB)
```
  000h 2     STR ID   (0160h)
  002h 2     STR Type (0000h=Custom)
  004h 2     Sector number within current Frame (0..2)
  006h 2     Number of Sectors in this Frame    (always 4) (3xSTR + 1xADPCM)
  008h 4     Frame Number (1=First)
  00Ch 4     Frame Size? (800h, despite of having 3 sectors with 7E0h each?)
  010h 2     Unknown (00h or 01h)
  012h 2     Unknown (A3h or ABh ... 6Ch or 7Bh ... or 43h or 49h)
  014h 2     Sector number within current Frame (0..2) (same as [004h])
  016h 0Ah   Zerofilled
  020h 7E0h  Data (polygon streaming or so?)
```
Note: The .PMB file is bundled with a .PMH file, which might contain header
info?<br/>

#### Bits Laboratory games (Charumera, and True Love Story series)
```
  Charumera                  ENDING.XA     (with dummy/zero data)
  True Love Story            TLS\MULTI.XA  (with nonzero data)
  True Love Story 2          TLS2\ENDING.STR and TLS2\MULTI.XA
  True Love Story Fan Disc            ;\probably use that format, too
  True Love Story: Remember My Heart  ;/(not verified)
```
The STR headers have STR ID=0160h and STR Type=0001h, STR header[10h..1Fh]
contains nonsense BS video info (with BS ID=3800h, although there isn't any BS
data in the actual data part at offset 20h and up).<br/>
The files do mainly contain XA-ADPCM sectors, plus some STR sectors in non-MDEC
format. Unknown if that STR sectors are separate channels, or if they are used
in parallel with the XA-ADPCM channel(s).<br/>
Unknown what the STR sectors are used for (perhaps Polygon Streaming, audio
subtitles, or simple garbage padding for unused audio sectors). In some files,
the STR sectors appear to be just dummy padding (STR header plus zerofilled
data area).<br/>

#### Nightmare Project: Yakata
This game has normal MDEC Streams, and Special Streams in non-MDEC format (eg.
Disc1, File 0E9h-16Eh and 985h-B58h), perhaps containing Polygon Streams or
whatever.<br/>
There are two channels (file=1/channel=00h-01h), each channel contains data
that consists of 5 sectors per frame (1xHeader plus 4xData). The sectors have
STR ID=0160h, and STR Type as follows:<br/>
```
  0000h=Whatever special, channel 0 header (sector 0)
  0400h=Whatever special, channel 1 header (sector 1)
  0001h=Whatever special, channel 0 data   (sector 2,4,6,8)
  0401h=Whatever special, channel 1 data   (sector 3,5,7,9)
```

#### Eagle One: Harrier Attack STR files
```
  \*.STR            MDEC movies  ;\BS fraquant (except, demo version
  \DATA*\*.STR      MDEC movies  ;/            on MagDemo31 uses mormal BS v2)
  \DATA*\M*\L*.STR  Multi-language TXT files with STR header on each sector
  \DATA*\M*\I*.STR  unknown binary data (whatever and SPU-ADPCM)
  \LANGN.STR        unknown binary data (whatever)
```
All of the above have STR Type=8001h (but only the MDEC movies have BS ID
3800h; the MDEC movies start with 13 zerofilled sectors that are all zeroes
without any STR/BS headers).<br/>
