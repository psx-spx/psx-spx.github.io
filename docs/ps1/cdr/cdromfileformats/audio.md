#   Audio

##   CDROM File Audio Single Samples VAG (Sony)
#### VAG audio samples
PSX Lightspan Online Connection CD, cdrom:\CD.TOC:\UI\*\\*.VAG<br/>
PSX Wipeout 2097, cdrom:\WIPEOUT2\SOUND\SAMPLES.WAD:\\*.vag (version=02h)<br/>
PSX Perfect Assassin, DATA.JFS:\AUDIO\\*.VAG and DATA.JFS:\SND\\*.VAG<br/>
```
  000h 4    File ID (usually "VAGp")
  004h 4    Version (usually 02h, or 20h)                       (big-endian)
  008h 4    Reserved (0) (except when ID="VAGi")                (big-endian)
  00Ch 4    Channel Size (data size... per channel?)            (big-endian)
  010h 4    Sample Rate (in Hertz) (eg. 5622h=22050Hz)          (big-endian)
  014h 0Ch  Reserved (0) (except when version=2)
  020h 10h  Name (ASCII, zeropadded)
  ... (..)  Optional ID string (eg. "STEREO" in upper/lowercase)
  ... (..)  Optional Padding to Data start
  ...  ..   ADPCM Data for channel(s) (usually at offset 030h)
```
VAG files are used on PSX, PSP, PS2, PS3, PS4. The overall 1-channel mono
format is same for consoles. But there are numerous different variants for
interleaved 2-channel stereo data.<br/>

#### VAG Filename Extensions
```
  .vag      default (eg. many PSX games)
  .vig      2-channel with interleave=10h (eg. PS2 MX vs ATV Untamed)
  .vas      2-channel with interleave=10h (eg. PS2 Kingdom Hearts II)
  .swag     2-channel with interleave=filesize/2 (eg. PSP Frantix)
  .l and .r 2-channel in l/r files (eg. PS2 Gradius V, PS2 Crash Nitro Kart)
  .str      whatever (eg. P?? Ben10 Galactic Racing)
  .abc      whatever (eg. PSP F1 2009 (v6), according to wiki.xentax.com)
```

#### VAG File IDs (header[000h])
```
  "VAGp"  default (eg. many PSX games)
  "VAG1"  1-channel (eg. PS2 Metal Gear Solid 3)
  "VAG2"  2-channel (eg. PS2 Metal Gear Solid 3)
  "VAGi"  2-channel interleaved (eg. ?)
  "pGAV"  little endian with extended header (eg. PS2 Jak 3, PS2 Jak X)
  "AAAp"  extra header, followed by "VAGp" header (eg. PS2 The Red Star)
```

#### VAG Versions (header[004h])
```
  00000000h   v1.8 PC
  00000002h   v1.3 Mac (eg. PSX Wipeout 2097, in SAMPLES.WAD)
  00000003h   v1.6+ Mac
  00000020h   v2.0 PC (most common, eg. PSX Perfect Assassin)
  00000004h   ? (later games, uh when/which?)
  00000006h   ? (vagconf, uh when/which?)
  00020001h   v2.1 (vagconf2)   ;\with HEVAG coding instead SPU-ADPCM
  00030000h   v3.0 (vagconf2)   ;/(eg. PS4/Vita)
  40000000h   ? (eg. PS2 Killzone) (1-channel, little endian header)
```

#### Reserved Header entries for ID="VAGi"
```
  008h 4  Interleave (little endian) (the other header entries are big endian)
```

#### Reserved Header entries for Version=00000002h (eg. PSX Wipeout 2097)
This does reportedly contain some default "base" settings for the PSX SPU:<br/>
```
  014h 2  Volume left                    4Eh,82h  ;-Port 1F801C00h
  016h 2  Volume right                   4Eh,82h  ;-Port 1F801C02h
  018h 2  Pitch (includes fs modulation) A8h,88h  ;-Port 1F801C04h +extra bit?
  01Ah 2  ADSR1                          00h,00h  ;-Port 1F801C08h
  01Ch 2  ADSR2                          00h,E1h  ;-Port 1F801C0Ah
  01Eh 2  ?                              A0h,23h  ;-Port 1F801C0xh maybe?
```

#### Reserved Header entries for Version=00000003h (according to wiki.xentax.com)
```
  01Eh 1  Number of channels (0 or 1=Mono, 2=Stereo)
```

#### Reserved Header entries for Version=00020001h and Version=00030000h
```
  01Ch 2  Zero                                      ;if non-zero: force Mono
  01Eh 1  Number of channels (0 or 1=Mono, 2=Stereo ;if 10h..FFh: force Mono
  01Fh 1  Zero                                      ;if non-zero: force Mono
```
Unknown if the above "force Mono" stuff is really needed (maybe it was intended
to avoid problems with Version=00000002h, and maybe never happens in
Version=00000003h and up)?<br/>

#### VAG ADPCM Data
The ADPCM data uses PSX SPU-ADPCM encoding (even on PS2 and up, except PS4 with
Version=0002001h or Version=00030000h, which do use HEVAG encoding).<br/>
[SPU ADPCM Samples](../../spu/soundprocessingunitspu.md#spu-adpcm-samples)<br/>
The data does usually start at offset 0030h (except, some files have extra
header data or padding at that location).<br/>
The first 10h-byte ADPCM block is usually all zero (used to initialize the
SPU).<br/>
2-channel (stereo) files are usually interleaved in some way.<br/>

#### VAG Endiannes
The file header entries are almost always big-endian (even so when used on
little endian consoles). There are a few exceptions:<br/>
ID="VAG1" has little endian [008h]=Interleave (remaining header is big-endian).<br/>
ID="pVAG" has (some?) header entries in little endian.<br/>
Version=40000000h has most or all header entries in little endian (perhaps
including the version being meant to be 00000040h).<br/>

#### VAG Channels
VAGs can be 1-channel (mono) or 2-channel (stereo). There is no standarized way
to detect the number of channels (it can be implied in the Filename Extension,
Header ID, in Reserved Header entries, in the Name string at [020h..02Fh], in
optional stuff at [030h], or in a separate VAG Header in the middle of the
file).<br/>

#### VAG Interleave
```
  None       default (for 1-channel mono) (and separate .l .r stereo files)
  800h       when ID="VAG2"
  [008h]     when ID="VAGi" (little-endian 32bit header[008h])
  1000h      when ID="pGAV" and [020h]="Ster" and this or that
  2000h      when ID="pGAV" and [020h]="Ster" and that or this
  10h        when filename extension=".vig"
  10h        when Version=0002001h or Version=00030000h (and channels=2)
  filesize/2 when filename extension=".swag"
  6000h      when [6000h]="VAGp" (eg. PSX The Simpsons Wrestling)
  1000h      when [1000h]="VAGp" (eg. PS2 Sikigami no Shiro)
  ...
```

#### AAAp Header
```
  000h 4     ID "AAAp"
  004h 2     Interleave
  006h 2     Number of Channels (can be 1 or 2?)
  008h 30h*N VAGp header(s) for each channel, with Version=00000020h
  ...  ..    ADPCM Data (interleaved when multiple channels)
```

#### See also
<http://github.com/vgmstream/vgmstream/blob/master/src/meta/vag.c> ;very detailed<br/>
<http://wiki.xentax.com/index.php/VAG_Audio> ;rather incomplete and perhaps wrong<br/>



##   CDROM File Audio Sample Sets VAB and VH/VB (Sony)
#### VAB vs VH/VB
```
  .VAB  contains VAB header, and ADPCM binaries   ;-all in one file
  .VH   contains only the VAB header              ;\in two separate files
  .VB   contains only the ADPCM binaries          ;/
```
PSX Perfect Assassin has some v7 .VH/.VB's (in \DATA.JFS:\SND\\*.\*)<br/>
PSX Resident Evil 2, COMMON\DATA\\*.DIE (contains .TIM+.VAB badged together)<br/>
PSX Spider-Man, CD.HED\l2a1.vab is VAB v5 (other VABs in that game are v7)<br/>
PSX Tenchu 2 (MagDemo35: TENCHU2\VOLUME.DAT\5\\* has VAB v20h, maybe a typo)<br/>

#### VAB Header (VH)
```
  0000h 4       File ID ("pBAV")
  0004h 4       Version (usually 7) (reportedly 6 exists, too) (5, 20h exists)
  0008h 4       VAB ID (usually 0)
  000Ch 4       Total .VAB filesize in bytes (or sum of .VH and .VB filesizes)
  0010h 2       Reserved (EEEEh)
  0012h 2       Number of Programs, minus 1 (0000h..007Fh = 1..128 programs)
  0014h 2       Number of Tones, minus? (max 0800h?) (aka max 10h per program)
  0016h 2       Number of VAGs, minus? (max 00FEh)
  0018h 1       Master Volume (usually 7Fh)
  0019h 1       Master Pan    (usually 40h)
  001Ah 1       Bank Attribute 1 (user defined) (usually 00h)
  001Bh 1       Bank Attribute 2 (user defined) (usually 00h)
  001Ch 4       Reserved (FFFFFFFFh)
  0020h 800h    Program Attributes 10h-byte per Program 00h..7Fh   (fixed size)
  0820h P*200h  Tone Attributes 200h-byte per Program 00h..P-1  (variable size)
  xx20h 200h    16bit VAG Sizes (div8) for VAG 00h..FFh            (fixed size)
  xx20h (...)   ADPCM data (only in .VAB files, otherwise in separate .VB file)
```
Program Attributes (10h-byte per Program, max 80h programs)<br/>
```
  000h 1      tones        Number of Tones in the Program (Yaroze: 4) (uh?)
  001h 1      mvol         Master Volume   (Yaroze: 0..127)
  002h 1      prior                        (Yaroze: N/A)
  003h 1      mode                         (Yaroze: N/A)
  004h 1      mpan         Master Panning  (Yaroze: 0..127)
  005h 1      reserved0
  006h 2      attr                         (Yaroze: N/A)
  008h 4      reserved1
  00Ch 4      reserved2
```
Tone Attributes (20h-byte per Tone, max 10h tones per Program)<br/>
```
  000h 1      prior        Tone Priority   (Yaroze: 0..127, 127=highest)
  001h 1      mode         Mode            (Yaroze: 0=Normal, 4=Reverberation)
  002h 1      vol          Tone Volume     (Yaroze: 0..127)
  003h 1      pan          Tone Panning    (Yaroze: 0..127)
  004h 1      center       Centre note (in semitone units) (Yaroze: 0..127)
  005h 1      shift        Centre note fine tuning         (Yaroze: 0..127)
  006h 1      min          Note limit minimum value     (Yaroze: 0..127)
  007h 1      max          Note limit maximum value     (Yaroze: 0..127)
  008h 1      vibW                                      (Yaroze: N/A)
  009h 1      vibT                                      (Yaroze: N/A)
  00Ah 1      porW                                      (Yaroze: N/A)
  00Bh 1      porT                                      (Yaroze: N/A)
  00Ch 1      pbmin        Max? value for downwards pitchbend  (Yaroze: 0..127)
  00Dh 1      pbmax        Max value for upwards pitchbend     (Yaroze: 0..127)
  00Eh 1      reserved1
  00Fh 1      reserved2
  010h 2      ADSR1        Attack,Decay    (Yaroze: 0..127,0..15)
  012h 2      ADSR2        Release,Sustain (Yaroze: 0..127,0..31)
  014h 2      prog         Program number that tone belongs to (Yaroze: 0..127)
  016h 2      vag          VAG number                          (Yaroze: 0..254)
  018h 8      reserved
```

#### VAB Binary (VB) (ADPCM data) (to be loaded to SPU RAM)
This can contain max 254 "VAG files" (maybe because having two (?) reserved
8bit numbers?).<br/>
Sony wants the total size of the ADPCM data to be max 7E000h bytes (which would
occupy most of the 512Kbyte SPU RAM, leaving little space for the echo buffer
or additional effects).<br/>
Note: The "VAG files" inside of VAB/VB are actually raw SPU-ADPCM data, without
any VAG file header. The first 10h-byte ADPCM block is usually zerofilled.<br/>



##   CDROM File Audio Sequences SEQ/SEP (Sony)
#### SEQ - Single Sequence
.SEQ contains MIDI-style sequences, the samples for the instruments can be
stored in a separate .VAB file (or .VH and .VB files).<br/>
Used by Perfect Assassin, DATA.JFS:\SND\\*.SEQ (bundled with \*.VH and \*.VB)<br/>
Used by Croc (MagDemo02: CROC\CROCFILE.DIR\AMBI\*.BIN, MAP\*.BIN, JRHYTHM.BIN)<br/>
Used by many other games.<br/>
```
  000h 4   File ID "pQES"
  004h 4   Version (1)                    (big endian?)
  008h 2   Resolution per quarter note      (01h,80h)
  00Ah 3   Tempo 24bit (8bit:16bit maybe?)  (07h,27h,0Eh)
  00Dh 2   Rhythm (NN/NN)                   (04h,02h)
  00Fh ... Score data, uh?    (with many MIDI KeyOn's: xx,9x,xx,xx)
  ...  3   End of SEQ (2Fh=End of Track)    (FFh,2Fh,00h)
```
The "Score data" seems to be more or less same as in Standard Midi Format (.smf
files), ie. containing timing values and MIDI commands/parameters.<br/>

#### SEP - Multi-Track Sequences
This is a simple "archive" with several SEQ-like sequences.<br/>
```
  000h 4   File ID "pQES"  ;same ID as in .SEQ files (!)
  004h 2   Version (0)     ;value 0, and only 16bit, unlike .SEQ files
  006h ..  1st Sequence
  ...  ..  2nd Sequence
  ...  ..  etc.
```
Sequences:<br/>
```
  000h 2   Sequence ID (0000h and up)     (big endian)        ;-ID number
  002h 2   Resolution per quarter note      (01h,80h)         ;\
  004h 3   Tempo 24bit                      (07h,27h,0Eh)     ; as in SEQ files
  007h 2   Rhythm (NN/NN)                   (04h,02h)         ;/
  009h 4   Data size (big endian, from 00Dh up to including End of SEQ(
  00Dh ... Score data, uh?                  (...)             ;\as in SEQ files
  ...  3   End of SEQ (2Fh=End of Track)    (FFh,2Fh,00h)     ;/
```
Used by Hear It Now (Playstation Developer's Demo) (RCUBE\RCUBE.SEP)<br/>
Used by Rayman (SND\BIGFIX.ALL\0002)<br/>
Used by Monster Rancher (MagDemo06, MR\_DEMO\DATA\MF\_DATA.OBJ\025B)<br/>
Used by Rugrats (MagDemo19: RUGRATS\DB02\\*.SEP and MENU\SOUND\SEPS\\*.SEP)<br/>
Used by Rugrats Studio Tour (MagDemo32: RUGRATS\DATA\SEPS\\*.SEP)<br/>
Used by Monkey Hero (MagDemo17: MONKEY\BIGFILE.PSX}\*.SEP)<br/>
Used by Pitfall 3D<br/>
Used by Blue's Clues: Blue's Big Musical (SEPD chunks in \*.TXD)<br/>



##   CDROM File Audio Other Formats

#### .SQ .HD .HD (SSsq/SShd)
This is a newer Sony format from 1999 (resembling the older .SEQ .VH .VB
format).<br/>
Used by Alundra 2, Ape Escape, Arc the Lad 3, Koukidou Gensou - Gunparade
March, Omega Boost, PoPoLoCrois Monogatari II, The Legend of Dragoon, Wild Arms
2.<br/>
```
  .SQ Sequence Data (with ID "SSsq")
  .HD Voice Header  (with ID "SShd")
  .BD Voice Binary  (raw SPU-ADPCM, same as .VB)
```

##### Sequence Data (\*.SQ)
```
  000h 2       Sequence Volume (0 .. 127, Always 64??)
  002h 2       Ticks per Quarter Note (always 1E0h)
  004h 2       Tempo
  005h 6       Zerofilled
  00Ch 4       ID "SSsq"
  010h 10h*10h Channels
  110h ..      Sequence
```

###### Channel
```
  000h 1       UNKNOWN
  001h 1       Channel Index
  002h 1       Program Index
  003h 1       Volume
  004h 1       Pan (0 .. 127, 64 is center)
  005h 4       UNKNOWN
  009h 1       Modulation (Multiplier for "breath" control)
  00Ah 1       Pitch Bend (0 .. 127, 64 is center)
  00Bh 1       Priority
  00Ch 1       Breath (0 .. 127 how quickly to loop over the breath wave)
  00Dh 1       UNKNOWN
  00Eh 1       Adjusted volume (combination of sequence volume and channel volume)
  00Fh 1       UNKNOWN
```

##### Voice Header (\*.HD)
```
  000h 4     Size of the .HD file itself
  004h 4     Size of the corresponding .BD file
  008h 4     Zero
  00Ch 4     ID "SShd"
  010h 1Ch*4 Offsets to data (or FFFFFFFFh=None)
  080h ..    Data
```

###### Data 0 - Programs
```
Header
  000h 2     Program Upper bound (count - 1)
  002h 2*n   Program offsets (FFFFh=None, yes the count can be higher than actual program count)
  ...  ...   Program data
```
```
 Program
  000h 1     Type + Tone Upper bound (FF = SFX, if not, 1st bit allows the program to play multiple tones per one KeyOn, rest is upper bound)
  001h 1     Volume (0 .. 127)
  002h 1     Pan (0 .. 127, 64 is center)
  003h 1     UNUSED
  004h 1     Pitch Bend multiplier
  005h 1     Breath wave index (7Fh=None)
  006h 1     SFX - Starting note
  007h 1     SFX - Tone count
```
```
Tone
  000h 1     Minimum note
  001h 1     Maximum note
  002h 1     Root key
  003h 1     Fine pitch adjustment (in 1/16 of a semitone)
  004h 2     ADPCM offset (*8)
  006h 4     ADSR
  00Ah 1     Volume override
  00Bh 1     Volume (0 .. 127)
  00Ch 1     Pan (0 .. 127, 64 is center)
  00Dh 1     Pitch Bend multiplier
  00Eh 1     Breath wave index (7Fh=None)
  00Fh 1     Flags (High priority, Noise, UNKNOWN, UNKNOWN, Pitch Bend from Program, Modulation, Breath wave from Program, Reverb)
```

###### Data 1 - Velocity volumes
```
  000h 2     UNUSED
  002h 1*80h Velocity volumes
```

###### Data 2 - Breath waves
```
  000h 2     Beath wave upper bound
  002h 2*n   Breath wave offsets
  ...  40h*n Breath waves (Only 60 out of the 64 values are used. And each represents 1 step in a 1 sec cycle at the lowest breath speed)
```


###### Data 3 - Sequence set (Used for SFX, uses a slightly altered subset of commands)
```
  000h 2     Sets upper bound
  002h 2*n   Set Offsets
  ...  2     Sequence upper bound (Set 0)
  ...  2*m   Sequence offset (Set 0)
  ... ...
  ... ...    Sequences (Terminated with FF 2F 00 - End of Track command)
```

###### Data 4 - Embedded SSsq (Used for SFX)
```
  000h 10h     SSsq header with just the volume
  010h 18h*10h Channels
  190h ...     Programs 
```

##### Voice Binary (\*.BD) (same as .VB files)
```
  000h ..    SPU-ADPCM data (usually starting with zerofilled 10h-byte block)
```

#### DNSa/PMSa/FNSa/FMSa
There are four four file types:<br/>
```
  "DNSa"  (aka SouND backwards)         ;sequence data
  "PMSa"  (aka SaMPles backwards)       ;samples with small header
  "FMSa"  (aka SaMples-F... backwards)  ;samples with bigger header   ;\Legacy
  "FNSa"  (aka SouNd-F... backwards)    ;whatever tiny file           ;/of Kain
```
Used by several games (usually inside of BIGFILE.DAT):<br/>
```
  Akuji (MagDemo18: AKUJI\BIGFILE.DAT\*) (DNSa,PMSa)
  Gex 2 (MagDemo08: GEX3D\BIGFILE.DAT\*) (DNSa)
  Gex 3: Deep Cover Gecko (MagDemo20: G3\BIGFILE.DAT\*) (DNSa,PMSa)
  Legacy of Kain 2 (MagDemo13: KAIN2\BIGFILE.DAT\*) (DNSa)
  Legacy of Kain 2 (MagDemo26: KAIN2\BIGFILE.DAT\*) (DNSa,PMSa,FNSa,FMSa)
  Walt Disney World Racing Tour (MagDemo35: GK\BIGFILE.DAT\*) (DNSa,PMSa)
```
Note: The exact file format does reportedly differ in each game.<br/>

##### "PMSa"  (aka SaMPles backwaords)
```
  000h 4     ID "PMSa"
  004h 4     Total Filesize
  008h 8     Zerofilled
  010h ..    SPU-ADPCM data (usually starting with zerofilled 10h-byte block)
```

##### "DNSa"  (aka SouND backwards)
```
  000h 4      ID "DNSa"   ;aka SND backwards
  004h 2      Offset from DNSa+4 to 8-byte entries (can be odd)
  006h 1      Unknown (3)
  007h 1      Number of 8-byte entries   (N1)
  008h 1?     Number of 10h-byte entries (N2)
  ...  ..     Unknown (..)
  ...  N1*8   Whatever 8-byte entries
  ...  N2*10h Whatever 10h-byte entries
  ...  ..     ... circa 40h 4-byte entries...?
  ...  ..     Unknown (..)
  ...  ..     Several blocks with ID "QESa" or "QSMa"  ;supposedly MIDI-style?
```

##### "FNSa"  (aka SouNd-F... backwards)
These are whatever tiny files (with filesize 1Ch or 2Ch).<br/>
```
  000h 4     ID "FNSa"
  ...  ..    Unknown
```

##### "FMSa"  (aka SaMples-F... backwards)
```
  000h 4     ID "FMSa"
  008h ..    Unknown..
  ...  ..    SPU-ADPCM data (usually starting with zerofilled 10h-byte block)
```

#### AKAO
There a several games that have sound files with ID "AKAO".<br/>
```
  XXX does that include different AKAO formats... for Samples and Midi?
```
AKAO is also used in several streaming movies:<br/>
[CDROM File Video Streaming Audio](streaming.md#cdrom-file-video-streaming-audio)<br/>

#### Others
Alone in the Dark IV has MIDB and DSND chunks (which contain sound files).<br/>

#### See also
The page below does mention several PSX sound formats, plus some open source
&amp; closed source tools for handling those files.<br/>
<https://github.com/loveemu/vgmdocs/blob/master/Conversion_Tools_for_Video_Game_Music.md><br/>



##   CDROM File Audio Streaming XA-ADPCM
#### Audio Streaming (XA-ADPCM)
Audio streaming is usually done by interleaving the .STR or .BS file's Data
sectors with XA-ADPCM audio sectors (the .STR/.BS headers don't contain any
audio info; because XA-ADPCM sectors are automatically decoded by the CDROM
controller).<br/>
Raw XA-ADPCM files (without video) are usually have .XA file extension.<br/>



##   CDROM File Audio CD-DA Tracks
The eleven .SWP files in Wipeout 2097 seem to be CD-DA audio tracks.<br/>
The one TRACK01.WAV in Alone in the Dark, too?<br/>
Other than that, tracks can be accessed via TOC instead of filenames.<br/>
