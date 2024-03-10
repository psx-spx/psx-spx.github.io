#   CDROM File Formats
#### Official PSX File Formats
[CDROM File Official Sony File Formats](cdromfileformats.md#cdrom-file-official-sony-file-formats)<br/>

#### Executables
[CDROM File Playstation EXE and SYSTEM.CNF](cdromfileformats.md#cdrom-file-playstation-exe-and-systemcnf)<br/>
[CDROM File PsyQ .CPE Files (Debug Executables)](cdromfileformats.md#cdrom-file-psyq-cpe-files-debug-executables)<br/>
[CDROM File PsyQ .SYM Files (Debug Information)](cdromfileformats.md#cdrom-file-psyq-sym-files-debug-information)<br/>

#### Video Files
[CDROM File Video Texture Image TIM/PXL/CLT (Sony)](cdromfileformats.md#cdrom-file-video-texture-image-timpxlclt-sony)<br/>
[CDROM File Video Texture/Bitmap (Other)](cdromfileformats.md#cdrom-file-video-texturebitmap-other)<br/>
[CDROM File Video 2D Graphics CEL/BGD/TSQ/ANM/SDF (Sony)](cdromfileformats.md#cdrom-file-video-2d-graphics-celbgdtsqanmsdf-sony)<br/>
[CDROM File Video 3D Graphics TMD/PMD/TOD/HMD/RSD (Sony)](cdromfileformats.md#cdrom-file-video-3d-graphics-tmdpmdtodhmdrsd-sony)<br/>
[CDROM File Video STR Streaming and BS Picture Compression (Sony)](cdromfileformats.md#cdrom-file-video-str-streaming-and-bs-picture-compression-sony)<br/>

#### Audio Files
[CDROM File Audio Single Samples VAG (Sony)](cdromfileformats.md#cdrom-file-audio-single-samples-vag-sony)<br/>
[CDROM File Audio Sample Sets VAB and VH/VB (Sony)](cdromfileformats.md#cdrom-file-audio-sample-sets-vab-and-vhvb-sony)<br/>
[CDROM File Audio Sequences SEQ/SEP (Sony)](cdromfileformats.md#cdrom-file-audio-sequences-seqsep-sony)<br/>
[CDROM File Audio Other Formats](cdromfileformats.md#cdrom-file-audio-other-formats)<br/>
[CDROM File Audio Streaming XA-ADPCM](cdromfileformats.md#cdrom-file-audio-streaming-xa-adpcm)<br/>
[CDROM File Audio CD-DA Tracks](cdromfileformats.md#cdrom-file-audio-cd-da-tracks)<br/>

#### Virtual Filesystem Archives
PSX titles are quite often using virtual filesystems, with numerous custom file
archive formats.<br/>
[CDROM File Archives with Filename](cdromfileformats.md#cdrom-file-archives-with-filename)<br/>
[CDROM File Archives with Offset and Size](cdromfileformats.md#cdrom-file-archives-with-offset-and-size)<br/>
[CDROM File Archives with Offset](cdromfileformats.md#cdrom-file-archives-with-offset)<br/>
[CDROM File Archives with Size](cdromfileformats.md#cdrom-file-archives-with-size)<br/>
[CDROM File Archives with Chunks](cdromfileformats.md#cdrom-file-archives-with-chunks)<br/>
[CDROM File Archives with Folders](cdromfileformats.md#cdrom-file-archives-with-folders)<br/>
[CDROM File Archives in Hidden Sectors](cdromfileformats.md#cdrom-file-archives-in-hidden-sectors)<br/>
More misc stuff...<br/>
[CDROM File Archive HED/DAT/BNS/STR (Ape Escape)](cdromfileformats.md#cdrom-file-archive-heddatbnsstr-ape-escape)<br/>
[CDROM File Archive WAD.WAD, BIG.BIN, JESTERS.PKG (Crash/Herc/Pandemonium)](cdromfileformats.md#cdrom-file-archive-wadwad-bigbin-jesterspkg-crashhercpandemonium)<br/>
[CDROM File Archive BIGFILE.BIG (Gex)](cdromfileformats.md#cdrom-file-archive-bigfilebig-gex)<br/>
[CDROM File Archive BIGFILE.DAT (Gex - Enter the Gecko)](cdromfileformats.md#cdrom-file-archive-bigfiledat-gex-enter-the-gecko)<br/>
[CDROM File Archive FF9 DB (Final Fantasy IX)](cdromfileformats.md#cdrom-file-archive-ff9-db-final-fantasy-ix)<br/>
[CDROM File Archive Ace Combat 2 and 3](cdromfileformats.md#cdrom-file-archive-ace-combat-2-and-3)<br/>
[CDROM File Archive NSD/NSF (Crash Bandicoot 1-3)](cdromfileformats.md#cdrom-file-archive-nsdnsf-crash-bandicoot-1-3)<br/>
[CDROM File Archive STAGE.DIR and *.DAT (Metal Gear Solid)](cdromfileformats.md#cdrom-file-archive-stagedir-and-dat-metal-gear-solid)<br/>
[CDROM File Archive DRACULA.DAT (Dracula)](cdromfileformats.md#cdrom-file-archive-draculadat-dracula)<br/>
[CDROM File Archive Croc 1 (DIR, WAD, etc.)](cdromfileformats.md#cdrom-file-archive-croc-1-dir-wad-etc)<br/>
[CDROM File Archive Croc 2 (DIR, WAD, etc.)](cdromfileformats.md#cdrom-file-archive-croc-2-dir-wad-etc)<br/>
[CDROM File Archive Headerless Archives](cdromfileformats.md#cdrom-file-archive-headerless-archives)<br/>
Using archives can avoid issues with the PSX's poorly implemented ISO
filesystem: The PSX kernel supports max 800h bytes per directory, and lacks
proper caching for most recently accessed directories (additionally, some
archives can load the whole file/directory tree from continous sectors, which
could be difficult in ISO filesystems).<br/>

#### Compression
[CDROM File Compression](cdromfileformats.md#cdrom-file-compression)<br/>

#### Misc
[CDROM File XYZ and Dummy/Null Files](cdromfileformats.md#cdrom-file-xyz-and-dummynull-files)<br/>

#### General CDROM Disk Images
[CDROM Disk Images CCD/IMG/SUB (CloneCD)](cdromfileformats.md#cdrom-disk-images-ccdimgsub-clonecd)<br/>
[CDROM Disk Images CDI (DiscJuggler)](cdromfileformats.md#cdrom-disk-images-cdi-discjuggler)<br/>
[CDROM Disk Images CUE/BIN/CDT (Cdrwin)](cdromfileformats.md#cdrom-disk-images-cuebincdt-cdrwin)<br/>
[CDROM Disk Images MDS/MDF (Alcohol 120%)](cdromfileformats.md#cdrom-disk-images-mdsmdf-alcohol-120)<br/>
[CDROM Disk Images NRG (Nero)](cdromfileformats.md#cdrom-disk-images-nrg-nero)<br/>
[CDROM Disk Image/Containers CDZ](cdromfileformats.md#cdrom-disk-imagecontainers-cdz)<br/>
[CDROM Disk Image/Containers ECM](cdromfileformats.md#cdrom-disk-imagecontainers-ecm)<br/>
[CDROM Subchannel Images](cdromfileformats.md#cdrom-subchannel-images)<br/>
[CDROM Disk Images Other Formats](cdromfileformats.md#cdrom-disk-images-other-formats)<br/>

#### FILENAME.EXT
The BIOS seems to support only (max) 8-letter filenames with 3-letter
extension, typically all uppercase, eg. "FILENAME.EXT". Eventually, once when
the executable has started, some programs might install drivers for long
filenames(?)<br/>

The PSX uses the standard CDROM ISO9660 filesystem without any encryption (ie.
you can put an original PSX CDROM into a DOS/Windows computer, and view the
content of the files in text or hex editors without problems).<br/>

#### Note
MagDemoNN is short for "Official U.S. Playstation Magazine Demo Disc NN"<br/>



##   CDROM File Official Sony File Formats
#### Official Sony File Formats
[https://psx.arthus.net/sdk/Psy-Q/DOCS/Devrefs/Filefrmt.pdf] - Sony 1998<br/>
```
  File Formats
    (c) 1998 Sony Computer Entertainment Inc.
    Publication date: November 1998
  Chapter 1: Streaming Audio and Video Data
    STR: Streaming (Movie) Data                               1-3
    BS: MDEC Bitstream Data                                   1-8
    XA: CD-ROM Voice Data                                     1-31
  Chapter 2: 3D Graphics
    RSD: 3D Model Data [RSD,PLY,MAT,GRP,MSH,PVT,COD,MOT,OGP]  2-3
    TMD: Modeling Data for OS Library                         2-24
    PMD: High-Speed Modeling Data                             2-35
    TOD: Animation Data                                       2-40
    HMD: Hierarchical 3D Model, Animation and Other Data      2-49
  Chapter 3: 2D Graphics
    TIM: Screen Image Data                                    3-3
    SDF: Sprite Editor Project File                           3-8
    PXL: Pixel Image Data                                     3-11
    CLT: Palette Data                                         3-14
    ANM: Animation Information                                3-16
    TSQ: Animation Time Sequence                              3-22
    CEL: Cell Data                                            3-23
    BGD: BG Map Data                                          3-27
  Chapter 4: Sound
    SEQ: PS Sequence Data                                     4-3
    SEP: PS Multi-Track Sequence Data                         4-3
    VAG: PS Single Waveform Data                              4-5
    VAB: PS Sound Source Data [VAB and VH/VB]                 4-5
    DA: CD-DA Data                                            4-7
  Chapter 5: PDA and Memory Card
    FAT: Memory Card File System Specification                5-3
```
Most games are using their own custom file formats. However, VAG, VAB/VH(VB,
STR/XA, and TIM are quite popular (because they are matched to the PSX
low-level data encoding). Obviously, EXE is also very common (although not
included in the above document).<br/>



##   CDROM File Playstation EXE and SYSTEM.CNF
#### SYSTEM.CNF
Contains boot info in ASCII/TXT format, similar to the CONFIG.SYS or
AUTOEXEC.BAT files for MSDOS. A typical SYSTEM.CNF would look like so:<br/>
```
  BOOT = cdrom:\abcd_123.45;1 arg ;boot exe (drive:\path\name.ext;version)
  TCB = 4                         ;HEX (=4 decimal)   ;max number of threads
  EVENT = 10                      ;HEX (=16 decimal)  ;max number of events
  STACK = 801FFF00                ;HEX (=memtop-256)
```
The first line specifies the executable to load, from the "cdrom:" drive, "\"
root directory, filename "abcd\_123.45" (case-insensitive, the real name in the
disk directory would be uppercase, ie. "ABCD\_123.45"), and, finally ";1" is the
file's version number (a rather strange ISO-filesystem specific feature) (the
version number should be usually/always 1). Additionally, "arg" may contain an
optional 128-byte command line argument string, which is copied to address
00000180h, where it may be interpreted by the executable (most or all games
don't use that feature).<br/>
Each line in the file should be terminated by 0Dh,0Ah characters... not sure if
it's also working with only 0Dh, or only 0Ah...?<br/>

#### ABCD\_123.45
This is a normal executable (exactly as for the .EXE files, described below),
however, the filename/extension is taken from the game code (the "ABCD-12345"
text that is printed on the CD cover), but, with the minus replaced by an
underscore, and due to the 8-letter filename limit, the last two characters are
stored in the extension region.<br/>
That "XXXX\_NNN.NN" naming convention seems to apply for all official licensed
PSX games. Wild Arms does unconventionally have the file in a separate folder,
"EXE\SCUS\_946.06".<br/>

#### PSX.EXE (Boot-Executable) (default filename when SYSTEM.CNF doesn't exist)
#### XXXX\_NNN.NN (Boot-Executable) (with filename as specified in SYSTEM.CNF)
#### FILENAME.EXE (General-Purpose Executable)
PSX executables are having an 800h-byte header, followed by the code/data.<br/>
```
  000h-007h ASCII ID "PS-X EXE"
  008h-00Fh Zerofilled
  010h      Initial PC                   (usually 80010000h, or higher)
  014h      Initial GP/R28               (usually 0)
  018h      Destination Address in RAM   (usually 80010000h, or higher)
  01Ch      Filesize (must be N*800h)    (excluding 800h-byte header)
  020h      Data section Start Address   (usually 0)
  024h      Data Section Size in bytes   (usually 0)
  028h      BSS section Start Address    (usually 0) (when below Size=None)
  02Ch      BSS section Size in bytes    (usually 0) (0=None)
  030h      Initial SP/R29 & FP/R30 Base (usually 801FFFF0h) (or 0=None)
  034h      Initial SP/R29 & FP/R30 Offs (usually 0, added to above Base)
  038h-04Bh Reserved for A(43h) Function (should be zerofilled in exefile)
  04Ch-xxxh ASCII marker
             "Sony Computer Entertainment Inc. for Japan area"
             "Sony Computer Entertainment Inc. for Europe area"
             "Sony Computer Entertainment Inc. for North America area"
             (or often zerofilled in some homebrew files)
             (the BIOS doesn't verify this string, and boots fine without it)
  xxxh-7FFh Zerofilled
  800h...   Code/Data                  (loaded to entry[018h] and up)
```
The code/data is simply loaded to the specified destination address, ie. unlike
as in MSDOS .EXE files, there is no relocation info in the header.<br/>
Note: In bootfiles, SP is usually 801FFFF0h (ie. not 801FFF00h as in
system.cnf). When SP is 0, the unmodified caller's stack is used. In most cases
(except when manually calling DoExecute), the stack values in the exeheader
seem to be ignored though (eg. replaced by the SYSTEM.CNF value).<br/>
The memfill region is zerofilled by a "relative" fast word-by-word fill (so
address and size must be multiples of 4) (despite of the word-by-word filling,
still it's SLOW because the memfill executes in uncached slow ROM).<br/>
The reserved region at [038h-04Bh] is internally used by the BIOS to memorize
the caller's RA,SP,R30,R28,R16 registers (for some bizarre reason, this
information is saved in the exe header, rather than on the caller's stack).<br/>
Additionally to the initial PC,R28,SP,R30 values that are contained in the
header, two parameter values are passed to the executable (in R4 and R5
registers) (however, usually that values are simply R4=1 and R5=0).<br/>
Like normal functions, the executable can return control to the caller by
jumping to the incoming RA address (provided that it hasn't destroyed the stack
or other important memory locations, and that it has pushed/popped all
registers) (returning works only for non-boot executables; if the boot
executable returns to the BIOS, then the BIOS will simply lockup itself by
calling the "SystemErrorBootOrDiskFailure" function.<br/>

#### Relocatable EXE
Fade to Black (CINE.EXR) contains ID "PS-X EXR" (instead "PS-X EXE") and string
"PSX Relocable File - Delphine Software Int.", this is supposedly some custom
relocatable exe file (unsupported by the PSX kernel).<br/>

#### MSDOS.EXE and WINDOWS.EXE Files
Some PSX discs contain DOS or Windows .EXE files (with "MZ" headers), eg.
devkit leftovers, or demos/gimmicks.<br/>



##   CDROM File PsyQ .CPE Files (Debug Executables)
#### Fileheader
```
  00h 4   File ID (01455043h aka "CPE",01h)
```

#### Chunk 00h: End of File
```
  00h 1   Chunk ID (00h)
```

#### Chunk 01h: Load Data
```
  00h 1   Chunk ID (01h)
  01h 4   Address (usually 80010000h and up)
  05h 4   Size (LEN)
  09h LEN Data (binary EXE code/data)
```
Theoretically, this could contain the whole EXE body in a single chunk.
However, the PsyQ files are usually containing hundreds of small chunks (with
each function and each data item in a separate chunk). For converting CPE to
EXE, use "ExeOffset = (CpeAddress AND 1FFFFFFFh)-10000h+800h".<br/>

#### Chunk 02h: Run Address (whatever, optional, usually not used in CPE files)
```
  00h 1   Chunk ID (02h)
  01h 4   Address
```
Unknown what this is. It's not the entrypoint (which is set via chunk 03h).
Maybe intended to change the default load address (usually 80010000h)?<br/>

#### Chunk 03h: Set Value 32bit (LEN=4) (used for entrypoint)
#### Chunk 04h: Set Value 16bit (LEN=2) (unused)
#### Chunk 05h: Set Value 8bit  (LEN=1) (unused)
#### Chunk 06h: Set Value 24bit (LEN=3) (unused)
```
  00h 1   Chunk ID (03h..06h)
  01h 2   Register (usually 0090h=Initial PC, aka Entrypoint)
  03h LEN Value (8bit..32bit)
```

#### Chunk 07h: Select Workspace (whatever, optional, usually not used in CPE)
```
  00h 1   Chunk ID (07h)
  01h 4   Workspace number (usually 00000000h)
```

#### Chunk 08h: Select Unit (whatever, usually first chunk in CPE file)
```
  00h 1   Chunk ID (08h)
  01h 1   Unit (usually 00h)
```

#### Example from LameGuy's sample.cpe:
```
  0000h 4    File ID ("CPE",01h)
  0004h 2    Select Unit 0            (08h,00h)
  0006h 7    Set Entrypoint 8001731Ch (03h,0090h,8001731Ch)
  000Dh 0Dh  Load   (01h,800195F8h,00000004h,0,0,0,0)
  001Ah ..   Load   (01h,80010000h,0000002Bh,...)
  004Eh ..   Load   (01h,8001065Ch,00000120h,...)
  0177h ...  Load   (01h,8001077Ch,0000012Ch,...)
  02ACh ...  Load   (01h,800108A8h,000000A4h,...)
  ...   ...  Load   (...)
  98F4h ...  Load   (01h,800195F0h,00000008h,...)
  9905h 1    End    (00h)
```



##   CDROM File PsyQ .SYM Files (Debug Information)
PsyQ .SYM Files contain debug info, usually bundled with PsyQ .MAP and Psy .CPE
files. Those files are generated by PsyQ tools, which appear to be still in use
for homebrew PSX titles.<br/>
The files are occassionally also found on PSX CDROMs:<br/>
```
  Legacy of Kain PAL version (\DEGUG\NTSC\KAIN2.SYM+MAP+CPE)
  RC Revenge (\RELEASE.SYM)
  Twisted Metal: Small Brawl (MagDemo54: TMSB\TM.SYM)
  Jackie Chan Stuntmaster (GAME_REL.SYM+CPE)
  SnoCross Championship Racing (MagDemo37: SNOCROSS\SNOW.TOC\SNOW.MAP)
  Sled Storm (MagDemo24: DEBUG\MAIN.MAP)
  E.T. Interplanetary Mission (MagDemo54: MEGA\MEGA.CSH\* has SYM+CPE+MAP)
```

#### Fileheader .SYM
```
  00h 4  File ID ("MND",01h)
  04h 4  Whatever (0,0,0,0)    ;TOMB5: 0,02h,0,0
  08h .. Chunks (see below)
```

```
 _______________________________ Symbol Chunks ________________________________
```

#### Chunk 01h: Symbol (Immediate, eg. memsize, or membase)
#### Chunk 02h: Symbol (Function Address for Internal & External Functions)
#### Chunk 05h: Symbol (?)
#### Chunk 06h: Symbol (?)
```
  00h 4   Address/Value
  04h 1   Chunk ID (01h/02h/05h/06h)
  05h 1   Symbol Length (LEN)
  06h LEN Symbol (eg. "VSync")
```

```
 __________________________ Source Code Line Chunks ___________________________
```

#### Chunk 80h: Source Code Line Numbers: Address for 1 Line
```
  00h 4   Address (for 1 line, starting at current line)
  04h 1   Chunk ID (80h)
```

#### Chunk 82h: Source Code Line Numbers: Address for N Lines (8bit)
```
  00h 4   Address (for N lines, starting at current line)
  04h 1   Chunk ID (82h)
  05h 1   Number of Lines (00h=None, or 02h and up?)
```

#### Chunk 84h: Source Code Line Numbers: Address for NN Lines (16bit)
```
  00h 4   Address (for N lines, starting at current line)
  04h 1   Chunk ID (84h)
  05h 2   Number of Lines (?)
```

#### Chunk 86h: Source Code Line Numbers: Address for Line NNN (32bit?)
```
  00h 4   Address (for 1 line, starting at newly assigned current line)
  04h 1   Chunk ID (84h)
  05h 4   Absolute Line Number (rather than number of lines) (?)
```

#### Chunk 88h: Source Code Line Numbers: Start with Filename
```
  00h 4   Address (start address)
  04h 1   Chunk ID (88h=Filename)
  05h 4   First Line Number (after comments/definitions) (32bit?)
  09h 1   Filename Length (LEN)
  0Ah LEN Filename (eg. "C:\path\main.c")
```

#### Chunk 8Ah: Source Code Line Numbers: End of Source Code
```
  00h 4   Address (end address)
  04h 1   Chunk ID (8Ah)
```

```
 __________________________ Internal Function Chunks __________________________
```

#### Chunk 8Ch: Internal Function: Start with Filename
```
  00h 4    Address
  04h 1    Chunk ID (8Ch)
  05h 4    Whatever (1Eh,00h,20h,00h)  ;or 1Eh,00h,18h,00h
  09h 4    Whatever (00h,00h,1Fh,00h)
  0Dh 4    Whatever (00h,00h,00h,C0h)
  11h 4    Whatever (FCh,FFh,FFh,FFh)  ;mask? neg.offset?
  15h 4    Whatever (10h,00h,00h,00h)  <-- line number (32bit?)
  19h 1    Filename Length (LEN1)
  1Ah LEN1 Filename (eg. "C:\path\main.c")
  xxh 1    Symbol Length (LEN2)
  xxh LEN2 Symbol (eg. "VSync")
```

#### Chunk 8Eh: Internal Function: End of Function (end of chunk 8Ch)
```
  00h 4   Address
  04h 1   Chunk ID (8Eh)
  05h 4   Line Number                 <-- line number (32bit?)
```

#### Chunk 90h: Internal Function:Whatever90h... first instruction in main func?
#### Chunk 92h: Internal Function:Whatever92h... last instruction in main func?
Maybe line numbers? Or end of definitions for incoming parameters?<br/>
```
  00h 4   Address
  04h 1   Chunk ID (90h/92h)
  05h 4   Whatever (1Fh,00h,00h,00h)  <-- line number relative to main.start?
```

```
 _____________________________ Class/Type Chunks ______________________________
```

#### Chunk 94h: Type/Symbol (Simple Types?)
```
  00h 4   Offset (when used within a structure, or stack-N, or otherwise zero)
  04h 1   Chunk ID (94h)
  05h 2   Class (000Dh=Type.alias, 000Ah=Address, 0001h=Stack, 0002h=Addr)
  07h 2   Type (XX = 8bit,16bit,signed,etc.?)
  09h 4   Zero, or Size in Bytes (for "memblocks")
  0xh 1   Symbol Name Length (LEN)
  0xh LEN Symbol Name (eg. "size_t")
```

#### Chunk 96h: Type/Symbol (Complex Structures/Arrays?)
```
  00h 4   Offset (when used within a structure, otherwise zero)
  04h 1   Chunk ID (96h)
  05h 2   Class (02h=Array,08h=RefToStruct,0Dh=DefineAlias,66h=StructEnd)
  07h 2   Type (0xh=Small, 3xh=WithArrayStuff?) (same/similar as in chunk 94h)
  09h 4     Struct Size in Bytes
  0Dh 2     Array Dimensions (DIM) (0=none) ;eg. [3][4] --> 0002h
  0Fh DIM*4 Array Entries per Dimension     ;eg. [3][4] --> 00000003h,00000004h
  xxh 1     Internal Fake Name Length (LEN1) (0=none)
  xxh LEN1  Internal Fake Name  (eg. ".1fake")
  xxh 1     Symbol Name Length (LEN2)
  xxh LEN2  Symbol Name (eg. "r")
```

```
 ______________________________ Class/Type Values _____________________________
```

#### Class definition (in chunk 94h) (and somewhat same/similar in chunk 96h)
(looks same/similar as C\_xxx class values in COFF files!)<br/>
```
  0001h = Local variable              (with Offset = negative stack offset)
  0002h = Global variable or Function (with Offset = address)
  0008h = Item in Structure           (with Offser = offset within struct)
  0009h = Incoming Function param     (with Offset = index; 0,4,8,etc.)
  000Ah = Type address / struc start? (with Offset = zero)
  000Dh = Type alias                  (with Offset = zero)
```

#### Type definition (in chunk 94h/96h)
(maybe lower 4bit=type, and next 4bit=usage/variant?)<br/>
(looks same/similar as T\_xxx type values in COFF files!)<br/>
```
  0000h =
  0001h =
  0002h =
  0003h =                (16bit signed?)
  0004h = int            (32bit signed?)
  0005h =
  0006h =
  0007h =
  0008h = (address)      (32bit unsigned?) (with Definition=000Ah)
  0009h =
  000Ah =
  000Bh =
  000Ch = u_char         (8bit unsigned?)
  000Dh = u_short,ushort (16bit unsigned?)
  000Eh = u_int          (32bit unsigned?)
  000Fh = u_long         (64bit unsigned?) (or rather SAME as above?)
  0021h = function with 0 params, and/or return="nothing"?
  0024h = main function with 2 params, and/or return="int"?
  0052h = argv           (string maybe?)
  0038h = GsOT           (huh?)
  00F8h = GsOT_TAG       (huh?)
  00FCh = PACKET         (huh?)
  ??    = float,bool,string,ptr,packet,(un-)signed8/16/32/64bit,etc
  ??    = custom type/struct (using value 000xh plus "fake" name, or so?)
```

```
 __________________________________ .MAP File _________________________________
```

#### PsyQ .MAP File
The .SYM file is usually bundled with a .MAP file, which is containing a
summary of the symbolic info as ASCII text (but without info on line numbers or
data types). For example:<br/>
```
    Start     Stop   Length      Obj Group            Section name
 80010000 80012D5B 00002D5C 80010000 text             .rdata
 80012D5C 800C8417 000B56BC 80012D5C text             .text
 800C8418 800CDAB7 000056A0 800C8418 text             .data
 800CDAB8 800CFB63 000020AC 800CDAB8 text             .sdata
 800CFB64 800D5C07 000060A4 800CFB64 bss              .sbss
 800D5C08 800DD33F 00007738 800D5C08 bss              .bss
```

```
  Address  Names alphabetically
 800CFE80 ACE_amount
 800CFB94 AIMenu
 800CDE5C AXIS_LENGTH
 8005E28C AddClippedTri
 8005DFEC AddVertex
 ...
```

```
  Address  Names in address order
 00000000 _cinemax_obj
 00000000 _cinemax_header_org
 00000000 _cinemax_org
 00000000 _mcardx_sbss_size
 00000000 _mcardx_org
 ...
```



##   CDROM File Video Texture Image TIM/PXL/CLT (Sony)
TIM/PXL/CLT are standard formats from Sony's devkit. TIM is used by many PSX
games.<br/>
```
  .TIM   contains Pixel data, and (optional) CLUT data  ;-all in one file
  .PXL   contains Pixel data only                       ;\in two separate files
  .CLT   contains CLUT data only (if any)               ;/
```

#### TIM Format
```
  000h 1  File ID  (always 10h=TIM)
  001h 1  Version  (always 00h)
  002h 2  Reserved (always 0000h) (or 1 or 2 for Compressed TIM, see below)
  004h 4  Flags (bit0-2=Type; see below, bit3=HasCLUT, bit4-31=Reserved/zero)
  ...  .. Data Section for CLUT (Palette), only exists if Flags.bit3=1, HasCLUT
  ...  .. Data Section for Pixels (Bitmap/Texture)
```
The Type in Flags.bit0-2 can be 0=4bpp, 1=8bpp, 2=16bpp, 3=24bpp, 4=Mixed.<br/>
NFL Blitz 2000 (MagDemo26: B2000\DATA\ARTD\_G.BIN) does additionally use Type
5=8bit.<br/>
The Type value value is only a hint on how to view the Pixel data (the data is
copied to VRAM regardless of the type; 4=Mixed is meant to indicate that the
data contains different types, eg. both 4bpp & 8bpp textures).<br/>
Type 3=24bpp is quite rare, but does exist (eg. Colony Wars (MagDemo02:
CWARS\GAME.RSC\DEMO.TIM).<br/>

#### The format of the CLUT and Pixel Data Section(s) is:
```
  000h 4  Size of Data Section (Xsiz*2*Ysiz+0Ch)  ;maybe rounded to 4-byte?
  004h 4  Destination Coord    (YyyyXxxxh)  ;Xpos counted in halfwords
  008h 4  Width+Height         (YsizXsizh)  ;Xsiz counted in halfwords
  00Ch .. VRAM Data (to be DMAed to frame buffer)
```
Note: Above is usually a multiple of 4 bytes, but not always:<br/>
Shadow Madness (MagDemo18: SHADOW\DATA\ANDY\LOADSAVE\\*.TIM) contains TIM
bitmaps with 27x27 or 39x51 halfwords; those files have odd section size &
odd total filesize. Gran Turismo 2 (GT2.VOL\arcade\arc\_other.tim\0000) also has
odd size. Unknown if the CLUT can also have odd size (which would misalign the
following Bitmap section).<br/>
Bust A Groove (MagDemo18: BUSTGR\_A\G\_COMMON.DFS\0005) has 0x0 pixel Bitmaps
(with CLUT data).<br/>

#### PXL/CLT Format
PXL/CLT is very rare. And oddly, with swapped ID values (official specs say
11h=PXL, 12h=CLT, but the existing games do use 11h=CLT, 12h=PXL).<br/>
Used by Granstream Saga (MagDemo10 GS\\*)<br/>
Used by Bloody Roar 1 (MagDemo06: BL\\*)<br/>
Used by Bloody Roar 2 (MagDemo22: ASC,CMN,EFT,LON,SND,ST5,STU\\*)<br/>

#### CLT Format
```
  000h 1  File ID  (always 11h=CLT) (although Sony's doc says 12h)
  001h 1  Version  (always 00h)
  002h 2  Reserved (always 0000h)
  004h 4  Flags (bit0-1=Type=2; bit2-31=Reserved/zero)
  ...  .. Data Section for CLUT (Palette)
```
The .CLT Type should be always 2 (meant to indicate 16bit CLUT entries).<br/>

#### PXL Format
```
  000h 1  File ID  (always 12h=PXL) (although Sony's doc says 11h)
  001h 1  Version  (always 00h)
  002h 2  Reserved (always 0000h)
  004h 4  Flags (bit0-?=Type; see below, bit?-31=Reserved/zero)
  ...  .. Data Section for Pixels (Bitmap/Texture)
```
This does probably support the same 5 types as in .TIMs (though official Sony
docs claim the .PXL type to be only 1bit wide, but netherless claim that PXL
can be 4bpp, 8bpp, or 16bpp).<br/>

```
 _______________________________ Compressed TIM _______________________________
```

#### Compressed TIMs
Ape Escape (Sony 1999) is using a customized TIM format with 4bpp compression:<br/>
[CDROM File Compression TIM-RLE4/RLE8](cdromfileformats.md#cdrom-file-compression-tim-rle4rle8)<br/>
Other than that, TIMs can be compressed via generic compression functions (like
LZSS, GZIP), or via bitmap dedicated compression formats (like BS, JPG, GIF).<br/>

```
 ______________________________ Malformed Files _______________________________
```

#### Malformed TIMs in BIGFILE.DAT
```
  Used by Legacy of Kain: Soul Reaver (eg. BIGFILE.DAT\folder04h\file13h)
  Used by Gex - Enter the Gecko (eg. BIGFILE.DAT\file0Fh\LZcompressed)
```
Malformed TIMs contain texture data preceeded by a dummy 14h-byte TIM header
with following constant values:<br/>
```
  10 00 00 00  02 00 00 00  04 00 08 00  00 02 00 00  00 02 00 02  ;<-- this
  10 00 00 00  02 00 00 00  04 00 08 00  00 00 00 00  00 02 00 02  ;<-- or this
```
The malformed entries include:<br/>
```
  [04h]=Type should indicated the color depth, but it's always 02h=16bpp.
  [08h]=Width*2*Height+0Ch should be 8000Ch, but malformed is 80004h.
  Total filesize should be 80014h, but Gecko files are often MUCH smaller.
```
Also, destination yloc should be 0..1FFh, but PSX "Lemmings & Oh No! More
Lemmings" (FILES\GFX\\*.TIM) has yloc=200h (that game also has vandalized .BMP
headers with 2-byte alignment padding after ID "BM", whilst pretending that
those extra bytes aren't there in data offset and total size entries).<br/>

#### Oversized TIMs
```
  Used by Pong (MagDemo24: LES02020\*\*.TIM)
```
Has 200x200h pix, but section size (and filesize) are +2 bigger than that:<br/>
```
  10 00 00 00 02 00 00 00 0E 00 08 00 C0 01 00 00 00 02 00 02  ;Pong *.TIM
  10 00 00 00 02 00 00 00 0E 00 07 00 00 02 00 00 C0 01 00 02  ;Pong WORLD.TIM
  10 00 00 00 02 00 00 00 0E 80 03 00 00 02 00 01 C0 01 00 01  ;Pong ZONE*.TIM
```

#### Miscomputed Section Size
NBA Basketball 2000 (MagDemo28: FOXBB\TIM\\*.TIM) has TIMs with section size
"0Ch+Xsiz\*Ysiz" instead of "0Ch+Xsiz\*2\*Ysiz".<br/>

#### NonTIMs in Bloody Roar 1 and 2
```
  Bloody Roar 1 (CMN\INIT.DAT\000Eh)
  Bloody Roar 2 (CMN\SE00.DAT, CMD\SEL00.DAT\0030h and CMN\VS\VS.DAT\0000h)
```
This looks somehow TIM-inspired, but has ID=13h.<br/>
```
  13 00 00 00 02 00 00 00 0C 20 00 00 00 00 F8 01 00 01 10 00  ;Bloody Roar 1
  13 00 00 00 02 00 00 00 0C 20 00 00 00 00 00 00 00 01 10 00  ;Bloody Roar 2
```

#### Other uncommon/malformed TIM variants
And, Heart of Darkness has a TIM with Size entry set to Xsiz\*2\*Ysiz+0Eh
(instead of +0Ch) (that malformed TIM is found inside of the RNC compressed
IMAGES\US.TIM file).<br/>
Also, NFL Gameday '99 (MagDemo17: GAMEDAY\PHOTOS.FIL) contains a TIM cropped to
800h-byte size (containing only the upper quarter of the photo).<br/>
Also, not directly malformed, but uncommon: Final Fantasy IX contains 14h-byte
0x0 pixel TIMs (eg. FF9.IMG\dir04\file0046\1B-0000\04-0001).<br/>
Klonoa (MagDemo08: KLONOA\FILE.IDX\3\2\0..1) has 0x0pix TIM (plus palette).<br/>

#### Malformed CLTs
```
  Used by Secret of Mana, WM\WEFF\*.CLT
```
ID is 10h=TIM, Flags=10101009h (should be ID=12h, Flags=02h).<br/>



##   CDROM File Video Texture/Bitmap (Other)
Apart from Sony's TIM (and PXL/CLT) format, there are a bunch of other
texture/bitmap formats:<br/>

#### Compressed Bitmaps
```
  .BS used by several games (and also in most .STR videos)
  .GIF used by Lightspan Online Connection CD
  .JPG used by Lightspan Online Connection CD
  .BMP with RLE4 used by Lightspan Online Connection CD (MONOFONT, PROPFONT)
  .BMP with RLE8+Delta also used by Online Connection CD (PROPFONT\ARIA6.BMP)
  .PCX with RLE used by Jampack Vol. 1 (MDK\CD.HED\*.pcx)
```

#### Uncompressed Bitmaps
```
  .BMP
  .BMP used by Mat Hoffman's Pro BMX (MagDemo39: BMX\BMXCD.HED\*)
  .BMP used by Mat Hoffman's Pro BMX (MagDemo48: MHPB\BMXCD.HED\*)
  .BMP used by Thrasher: Skate and Destroy (MagDemo27: SKATE\ASSETS\*.ZAL)
  .BMP used by Dave Mirra Freestyle BMX (MagDemo36,46: BMX\ASSETS\*.ZAL)
  .VRM .IMG .TEX .TIM .RAW .256 .COL .4B .15B .R16 .TPG - raw VRAM data
  "SC" memory card icons
```

#### Targa TGA and Paintbrush PCX
[CDROM File Video Texture/Bitmap (TGA)](cdromfileformats.md#cdrom-file-video-texturebitmap-tga)<br/>
[CDROM File Video Texture/Bitmap (PCX)](cdromfileformats.md#cdrom-file-video-texturebitmap-pcx)<br/>

#### PSI bitmap - Power Spike (MagDemo43: POWER\GAME.IDX\\*.BIZ\\*.PSI)
```
  000h 10h   Name 1 ("FILENAME.BMP", zeropadded)
  010h 10h   Name 2 ("FILENAME.PSI", zeropadded)
  020h 4     Bits per pixel (usually 4, 8, or 16)
  024h 2     Bitmap VRAM Dest.X ?
  026h 2     Bitmap VRAM Dest.Y ?
  028h 2     Bitmap Width in pixels
  02Ah 2     Bitmap Height in pixels
  02Ch 2     Palette VRAM Dest.X ?   ;\zero for 16bpp
  02Eh 2     Palette VRAM Dest.Y ?   ;/
  030h 2     Bitmap Width in Halfwords (PixelWidth*bpp/16)
  032h 2     Palette Size in Halfwords (0, 10h, 100h for 16bpp,4npp,8bpp)
  034h 4     Maybe Bitmap present flag (always 1)
  038h 4     Maybe Palette present flag (0=16bpp, 1=4bpp/8bpp)
  03Ch ..    Bitmap pixels
  ...  ..    Palette (if any, for 4bpp: 16x16bit, for 8bpp: 256x16bit)
```

#### JumpStart Wildlife Safari Field Trip (MagDemo52: DEMO\DATA.DAT\\*.DAT+\*.PSX)
This game does use two different (but nearly identical) bitmap formats (with
either palette or bitmap data stored first).<br/>
```
  000h 4     Total Filesize (Width*Height+20Ch)
  004h 2     Bitmap Width
  006h 2     Bitmap Height
  008h 4     Unknown, always 1 (maybe 1=8bpp?)
 In .DAT files (512x192 or 256x64 pix), palette first:
  00Ch 200h  Palette data
  20Ch ..    Bitmap data
 In .PSX files (64x64 pix), bitmap first:
  00Ch ..    Bitmap data
  ...  200h  Palette data
```
To detect the "palette first" format, check for these conditions(s):<br/>
```
  Filename extension is ".DAT"
  Bitmap Width<>Height (non-square)
  [00Ch..20Bh] has AllMSBs>=80h, and SomeLSBs<80h
```
Note: The bitmaps are vertically mirrored (starting with bottom-most scanline).<br/>

#### WxH Bitmap (Width\*Height)
Used by Alone in the Dark The New Nightmare (FAT.BIN\BOOK,DOC,INTRO,MENU\\*)<br/>
Used by Rayman (RAY\JUN,MON,MUS\\*) (but seems to contain map data, not pixels)<br/>
```
  000h 2   Width  (W)   ;\usually 320x240 (or 512x240 or 80x13)
  002h 2   Height (H)   ;/
  004h ..  Bitmap 16bpp (W*H*2 bytes)
```

#### RAWP Bitmap
Used by Championship Motocross (MagDemo25: SMX\RESHAD.BIN\\*) ("RAWP")<br/>
```
  000h 4     ID "RAWP" (this variant has BIG-ENDIAN width/height!)
  004h 2     Width  (usually 280h=640pix or 140h=320pix) (big-endian!!!)
  006h 2     Height (usually 1E0h=480pix or F0h=240pix)  (big-endian!!!)
  008h ..    Bitmap data, 16bpp (width*height*2 bytes)
```

#### XYWH Bitmap/Palette (X,Y,Width\*Height) (.BIT and .CLT)
Used by CART World Series (MagDemo04: CART\\*.BIT and \*.BIN\\*)<br/>
Used by NFL Gameday '98 (MagDemo04: GAMEDAY\BUILD\GRBA.FIL\\*)<br/>
Used by NFL Gameday '99 (MagDemo17: GAMEDAY\\*.BIT and \*.FIL\\*)<br/>
Used by NFL Gameday 2000 (MagDemo27: GAMEDAY\\*.BIT)<br/>
Used by NCAA Gamebreaker '98 (MagDemo05: GBREAKER\\*.BIT and UFLA.BIN\\*)<br/>
Used by NCAA Gamebreaker 2000 (MagDemo27: GBREAKER\\*.BIT and \*.FIL\\*)<br/>
Used by Twisted Metal 4 (MagDemo30: TM4DATA\\*.MR,\*.IMG\\*.bit,\*.clt)<br/>
```
  000h 2   VRAM.X             (X) (0..3FFh)
  002h 2   VRAM.X             (Y) (0..1FFh)
  004h 2   Width in halfwords (W) (1..400h)
  006h 2   Height             (H) (1..200h)
  008h ..  Bitmap or Palette data (W*H*2 bytes)
```

#### Doom (PSXDOOM\ABIN\PSXDOOM.WAD\\*\\*)
```
  000h 2     Hotspot X (signed) (usually 0)
  002h 2     Hotspot Y (signed) (usually 0)
  004h 2     Width in bytes
  006h 2     Height
  008h ..    Bitmap 8bpp (Width*Height bytes)
```
Most files have Hotspot X=0,Y=0, WAD\LOADING has X=FF80h,Y=FF8Ah, and WAD\S\\*
has X=0..Width, Y=0..Height+1Ah (eg. S\BKEY\*, S\BFG\*, S\PISFA0 have large Y).<br/>
The files do not contain any palette info... maybe 2800h-byte PLAYPAL does
contain the palette(s)?<br/>

#### Lemmings & Oh No! More Lemmings (FILES\GFX\\*.BOB, FILES\SMLMAPS\\*.BOB)
```
  000h 2       Width
  002h 2       Height
  004h 100h*3  Palette 24bit RGB888
  304h ..      Bitmap 8bpp (Width*Height bytes)
  ..   (1700h) Unknown (only in SMLMAPS\*.BOB, not in GFX\*.BOB)
```
Apart from .BOB, the FILES\GFX folder also has vandalized .BMP (with ID
"BM",00h,00h) and corrupted .TIM (with VRAM.Y=200h).<br/>

#### Perfect Assassin (DATA.JFS\DATA\\*.BM)
```
  000h 4      Format 1 (0=8bpp, 1=16bpp)
  004h 4      Format 2 (1=8bpp, 2=16bpp)
  008h 4      Width in pixels
  00Ch 4      Height in pixels
  010h ..     Bitmap Data
  ...  (300h) Palette 18bit RGB666 (R,G,B range 00h..3Fh) (only if format 8bpp)
```

#### One (DIRFILE.BIN\\*.VCF)
```
  000h 4     Unknown (always 1)
  004h 4     Unknown (always 8)
  008h 4     Unknown (always 2) (maybe 2=16bpp?)
  00Ch 4     Width in pixels (3Ah, 140h, or 280h)
  010h 4     Height          (3Ah, or F0h)
  014h ..    Bitmap 16bpp (Width*Height*2 bytes)
```

#### One (DIRFILE.BIN\\*.VCK and DIRFILE.BIN\w\*\sect\*.bin\TEXTURE  001)
```
  000h 2     Number if Files (N)
  002h 2     Number of VRAM.Slots (less or equal than Number of Files)
  004h 4     ID "BLK0"
  008h N*10h File List
  ...  ..    1st File Bitmap
  ...  ..    1st File Palette (20h/200h/0 bytes for 4bpp/8bpp/16bpp)
  ...  ..    2nd File Bitmap
  ...  ..    2nd File Palette (only if PaletteID=FileNo=1)
  ...  ..    3rd File Bitmap
  ...  ..    3rd File Palette (only if PaletteID=FileNo=2)
  ...  ..    etc.
```
File List entries:<br/>
```
  000h 2     VRAM.X in halfwords (0..1Fh, +bit15=Blank)  ;\within current
  002h 2     VRAM.Y              (0..3Fh)                ;/VRAM.Slot
  004h 2     Width in pixels (max 80h/40h/20h for 4bpp/8bpp/16bpp)
  006h 2     Height          (max 40h)
  008h 2     VRAM.Slot       (0,1,2,3,...,NumSlots-1)
  00Ah 2     Unknown         (0,1,2,4 in *.vck, 4 in sect*.bin)
  00Ch 2     Color Depth     (0=4bpp, 1=8bpp, 2=16bpp)
  00Eh 2     Palette ID      (0..FileNo-1=Old, FileNo=New, FFFFh=None/16bpp)
  NumFiles-1, or ID of already used palette)
```
Note: VRAM.Slots are 20h\*40h halfwords.<br/>
Bitmaps can either have newly defined palettes (when PaletteID=FileNo), or
re-use previously defined "old" palettes (when PaletteID\<FileNo).<br/>
The Blank flag allows to define a blank region (for whatever purpose), the file
doesn't contain any bitmap/palette data for such blank regions.<br/>

#### BMR Bitmaps
These are 16bpp bitmaps, stored either in uncompressed .BMR files, or in
compressed .RLE files:<br/>
[CDROM File Compression RLE_16](cdromfileformats.md#cdrom-file-compression-rle16)<br/>
```
  Apocalypse (MagDemo16: APOC\CD.HED\*.RLE and *.BMR)
  Spider-Man 1 older version (MagDemo31: SPIDEY\CD.HED\*.RLE)
  Spider-Man 1 newer version (MagDemo40: SPIDEY\CD.HED\*.RLE and .BMR)
  Spider-Man 2 (MagDemo50: HARNESS\CD.HED\*.RLE)
  Tony Hawk's Pro Skater (MagDemo22: PROSKATE\CD.HED\*.BMR)
```
The width/height for known filesizes are:<br/>
```
  33408h bytes --> 512x205pix, 16bpp (Apocalypse warning.rle)
  3C008h bytes --> 512x240pix, 16bpp (most common)
  96008h bytes --> 640x480pix, 16bpp (tony hawk's pro skater)
```
Most of the older BMR files (in Apocalypse) have valid 8-byte headers:<br/>
```
  000h 2     Unknown (FFA0h) (ID for files with valid headers?)
  002h 2     Dest.Y (usually 0) (11h=(240-205)/2 in Apocalypse warning.rle)
  004h 2     Width  (usually 200h=512pix)
  006h 2     Height (usually F0h=240pix) (CDh=205pix in Apocalypse warning.rle)
  008h ..    Bitmap data, 16bpp (width*height*2 bytes)
```
Most or all newer BMR files (in Apocalypse "loadlogo.rle", and in all files in
Spider-Man 1, Spider-Man-2, Tony Hawk's Pro Skater) have the 8-byte header
replaced by unused 8-byte at end of file:<br/>
```
  000h ..    Bitmap data, 16bpp (width*height*2 bytes)
  ..   8     Unused (garbage or extra pixels, not transferred to VRAM)
```
BUG: The bitmaps in all .BMR files (both with/without header) are distorted:
The last 4-byte (rightmost 2pix) of each scanline should be actually located at
the begin of the scanline, and the last scanline is shifted by an odd amount of
bytes (resulting in nonsense 16bpp pixel colors); Spider-Man is actually
displaying the bitmap in that distorted form (although it does mask off some
glitches: one of the two bad rightmost pixels is replaced by a bad black
leftmost pixel, and glitches in upper/lower lines aren't visible on 224-line
NTSC screens).<br/>

#### Croc 1 (retail: \*.IMG) (retail only, not in MagDemo02 demo version)
#### Croc 2 (MagDemo22: CROC2\CROCII.DIR\\*.IMG)
#### Disney's The Emperor's New Groove (MagDemo39: ENG\KINGDOM.DIR\\*.IMG)
#### Disney's Aladdin in Nasira's Rev. (MagDemo46: ALADDIN\ALADDIN.DIR\\*.IMG)
Contains raw 16bpp bitmaps, with following sizes:<br/>
```
  25800h bytes = 12C00h pixels (320x240)  ;Croc 1 (retail version)
  3C000h bytes = 1E000h pixels (512x240)
  96000h bytes = 4B000h pixels (640x480)
```
Note: The .IMG format is about same as .BMR files (but without the 8-byte
header, and without distorted scanlines).<br/>

#### Mat Hoffman's Pro BMX (MagDemo39: BMX\FE.WAD+STR\\*.BIN) (Activision)
#### Mat Hoffman's Pro BMX (MagDemo48: MHPB\FE.WAD+STR\\*.BIN) (Shaba/Activision)
```
  000h 2     Bits per pixel (4 or 8)
  002h 2     Bitmap Width in pixels
  004h 2     Bitmap Height in pixels
  006h 2     Zero
  008h N*2   Palette (with N=(1 SHL bpp))
  ...  ..    Bitmap (with Width*Height*bpp/8 bytes)
  ...  (..)  Zeropadding to 4-byte boundary (old version only)
```
The trailing alignment padding exists only in old demo version (eg. size of
78x49x8bpp "coreypp.bin" is old=10F8h, new=10F6h).<br/>

#### E.T. Interplanetary Mission (MagDemo54: MEGA\MEGA.CSH\\*)
```
  000h 2     Type (0=4bpp, 1=8bpp, 2=16bpp)
  002h 2     Unknown (usually 0000h, or sometimes CCCCh)
  004h 2     Bitmap Width in pixels
  006h 2     Bitmap Height in pixels
  008h 200h  Palette (always 200h-byte, even for 4bpp or 16bpp)
  208h ..    Bitmap (Width*Height*bpp/8 bytes)
```
Palette is 00h-or-CCh-padded when 4bpp, or CCh-filled when 16bpp.<br/>
Note: Some files contain two or more such bitmaps (of same or different sizes)
badged together.<br/>

#### EA Sports: Madden NFL '98 (MagDemo02: TIBURON\\*.DAT\\*)
#### EA Sports: Madden NFL 2000 (MagDemo27: MADN00\\*.DAT\\*)
#### EA Sports: Madden NFL 2001 (MagDemo39: MADN01\\*.DAT\\*)
This format is used in various EA Sports Madden .DAT archives, it contains
standard TIMs with extra Headers/Footers.<br/>
```
  000h 4     Offset to TIM (1Ch) (Hdr size)    (1Ch)               ;\
  004h 4     Offset to Footer    (Hdr+TIM size)(123Ch,1A3Ch,1830h) ;
  008h 2     Bitmap Width in pixels      (40h or 60h or 30h)       ;
  00Ah 2     Bitmap Height in pixels     (40h)                     ;
  00Ch 4     Unknown, always 01h         (01h)                     ; Header
  010h 4     Unknown, always 23h         (23h)                     ; 1Ch bytes
  014h 2     Unknown, always 0101h       (101h)                    ;
  016h 1     Bitmap Width in pixels      (40h or 60h or 30h)       ;
  017h 1     Bitmap Height in pixels     (40h)                     ;
  018h 4     Unknown, always 00h         (0)                       ;/
  01Ch ..    TIM (Texture, can be 4bpp, 8bpp, 16bpp)               ;-TIM
  ...  4     Unknown, always C0000222h   (C0000222h)               ;\
  ...  2     Unknown, always 0001h       (0001h)                   ;
  ...  1     Bitmap Width in pixels      (40h or 60h or 30h)       ; Footer
  ...  1     Bitmap Height in pixels     (40h)                     ; 12h bytes
  ...  4     Unknown, always 78000000h   (78000000h)               ;
  ...  6     Unknown                     (0,0,80h,0,0,0)           ;/
```
Purpose is unknown; the 8bit Width/Height entries might be TexCoords.<br/>
The PORTRAITS.DAT archives are a special case:<br/>
```
  Madden NFL '98 (MagDemo02: TIBURON\PORTRAIT.DAT) (48x64, 16bpp)
  Madden NFL 2000 (MagDemo27: MADN00\PORTRAIT.DAT) (96x64, 8bpp plus palette)
  Madden NFL 2001 (MagDemo39: MADN01\PORTRAIT.DAT) (64x64, 8bpp plus palette)
```
Those PORTRAITS.DAT don't have any archive header, instead they do contain
several images in the above format, each one zeropadded to 2000h-byte size.<br/>

#### 989 Sports: NHL Faceoff '99 (MagDemo17: FO99\\*.KGB\\*.TEX)
#### 989 Sports: NHL Faceoff 2000 (MagDemo28: FO2000\\*.TEX)
#### 989 Sports: NCAA Final Four 2000 (MagDemo30: FF00\\*.TEX)
```
  000h 0Ch  ID "TEX PSX ",01h,00h,00h,00h    ;used in 989 Sports games
  00Ch 4    Number of Textures
  010h 4    Total Filesize
  014h 4    Common Palette Size    (0=200h, 1=None, 2=20h)
  018h (..) Common Palette, if any (0,20h,200h bytes)
  ...  ..   Texture(s)
 Texture format:
  000h 10h  Filename (eg. "light1", max 16 chars, zeropadded if shorter)
  010h 4    Width in pixels  (eg. 40h)
  014h 4    Height           (eg. 20h or 40h)
  018h 4    Unknown          (always 0)
  01Ch 4    Number of Colors (eg. 10h, 20h or 100h)
  020h ..   Bitmap (4bpp when NumColors<=10h, 8bpp when NumColors>10h)
  ...  (..) Palette (NumColors*2 bytes, only present if Common Palette=None)
```
The .TEX files may be in ISO folders, KGB archives, DOTLESS archives. And, some
are stored in headerless .DAT/.CAT archives (which start with ID "TEX PSX ",
but seem to have further files appended thereafter).<br/>

#### Electronic Arts .PSH (SHPP)
FIFA - Road to World Cup 98 (with chunk C0h/C1h = RefPack compression)<br/>
NCAA March Madness 2000 (MagDemo32: MM2K\\*.PSH)<br/>
Need for Speed 3 Hot Pursuit (\*.PSH, ZLOAD\*.QPS\RefPack.PSH)<br/>
ReBoot (DATA\\*.PSH) (with chunk 6Bh)<br/>
Sled Storm (MagDemo24: DEBUG,ART,ART2,ART3,SOUND\\*.PSH) (with Comment, Mipmap)<br/>
WCW Mayhem (MagDemo28: WCWDEMO\\*.BIG\\*.PSH) (with chunk C0h/C1h = RefPack)<br/>
```
  000h 4    ID "SHPP"
  004h 4    Total Filesize (or Filesize-0Ch, eg. FIFA'98 ZLEG*.PSH)
  008h 4    Number of Textures (N)
  00Ch 4    ID "GIMX"
  010h N*8  File List
  ...  ..   Data (each File contains a Bitmap chunk, and Palette chunk, if any)
 File List entries:
  000h 4    Name (ascii) (Mipmaps use the same name for each mipmap level)
  004h 4    Offset from begin of archive to first Chunk of file
  Caution: Most PSH files do have the above offsets sorted in increasing order,
  but some have UNSORTED offsets, eg. Sled Storm (MagDemo24: ART3\LOAD1.PSH),
  so one cannot easily compute sizes as NextOffset-CurrOffset.
  Note: Mipmap textures consist of two files with same name and different
  resolution, eg. in Sled Storm (MagDemo24: ART\WORLD0x.PSH)
 Bitmap Chunk:
  000h 1    Chunk Type (40h=PSX/4bpp, 41h=PSX/8bpp, 42h=PSX/16bpp)
  001h 3    Offset from current chunk to next chunk (000000h=None)
  004h 2    Bitmap Width in pixels (can be odd, pad lines to 2-byte boundary)
  006h 2    Bitmap Height
  008h 2    Center X   (whatever that is)
  00Ah 2    Center Y   (whatever that is)
  00Ch 2    Position X (whatever that is, plus bit12-15=flags?)
  00Eh 2    Position Y (whatever that is, plus bit12-15=flags?)
  010h ..   Bitmap data (each scanline is padded to 2-byte boundary)
  ...  ..   Padding to 8-byte boundary
 Compressed Bitmap Chunk:
  000h 1    Chunk Type (C0h=PSX/4bpp, C1h=PSX/8bpp, and probably C2h=PSX/16bpp)
  001h 0Fh  Same as in Chunk 40h/41h/42h (see there)
  010h ..   Compressed Bitmap data (usually/always with Method=10FBh)
  ...  ..   Padding to 8-byte boundary
 Palette Chunk (if any) (only for 4bpp/8bpp bitmaps, not for 16bpp):
  000h 1    Chunk Type (23h=PSX/Palette)
  001h 3    Offset from current chunk to next chunk (000000h=None)
  004h 2    Palette Width in halfwords (10h or 100h)
  006h 2    Palette Height             (1)
  008h 2    Unknown (usually same as Width) (or 80D0h or 9240h)
  00Ah 2    Unknown (usually 0000h)         (or 0001h or 0002h)
  00Ch 2    Unknown (usually 0000h)
  00Eh 2    Unknown (usually 00F0h)
  010h ..   Palette data (16bit per color)
  Note: The odd 80D0h,0001h values occur in Sled Storm ART\WORKD00.PSH\TBR1)
 Unknown Chunk (eg. ReBoot (DATA\AREA15.PSH\sp*))
  000h 1    Chunk Type (6Bh)
  001h 3    Offset from current chunk to next chunk (000000h=None)
  004h 8    Unknown (2C,00,00,3C,03,00,00,00)
  00Ch -    For whatever reason, there is no 8-byte padding here
 Comment Chunk (eg. Sled Storm (MagDemo24: ART\WORLD0x.PSH))
  000h 1    Chunk Type (6Fh=PSX/Comment)
  001h 3    Offset from current chunk to next chunk (000000h=None)
  004h ..   Comment ("Saved in Photoshop Plugin made by PEE00751@...",00h)
  ...  ..   Zeropadding to 8-byte boundary
 Unknown Chunk (eg. Sled Storm (MagDemo24: ART\WORLD09.PSH\ADAA))
  000h 1    Chunk Type (7Ch)
  001h 3    Offset from current chunk to next chunk (000000h=None)
  004h 2Ch  Unknown (reportedly Hot spot / Pix region, but differs on PSX?)
```
The whole .PSH file or the bitmap chunks can be compressed:<br/>
[CDROM File Compression EA Methods](cdromfileformats.md#cdrom-file-compression-ea-methods)<br/>
Variants of the .PSH format are also used on PC, PS2, PSP, XBOX (with other
Chunk Types for other texture/palette formats, and for optional extra data).
For details, see: [http://wiki.xentax.com/index.php/EA\_SSH\_FSH\_Image]


#### Destruction Derby Raw (MagDemo35: DDRAW\\*.PCK,\*.FNT,\*.SPR)
This format can contain one single Bitmap, or a font with several small
character bitmaps.<br/>
```
  000h 2     ID "BC"                                        ;\
  002h 1     Color Depth (1=4bpp, 2=8bpp, 4=16bpp)          ; Header
  003h 1     Type        (40h=Bitmap, C0h=Font)             ;/
  ...  (2)   Palette Unknown (0 or 1)                       ;\only if Bitmap
  ...  (2)   Palette Unknown (1)                            ; 4bpp or 8bpp
  ...  (..)  Palette data (20h or 200h bytes for 4bpp/8bpp) ;/
  ...  2     Bitmap Number of Bitmaps-1 (N-1)               ;\
  ...  2     Bitmap Width in pixels                         ;
  ...  2     Bitmap Height in pixels                        ; Bitmap(s)
  ...  N*1   Bitmap Tilenumbers (eg. "ABCDEFG..." for Fonts);
  ...  N*1   Bitmap Proportional Font widths? (0xh or FFh)  ;
  ...  N*BMP Bitmap(s) for all characters                   ;/
  ...  (20h) Palette Data (20h bytes for 4bpp)              ;-only if Font/4bpp
```
All bitmap scanlines are padded to 2-byte boundary, eg. needed for:<br/>
```
  INGAME1\BOWL2.PTH\SPRITES.PTH\ST.SPR    30x10x4bpp: 15 --> 16 bytes/line
  INGAME1\BOWL2.PTH\SPRITES.PTH\STOPW.SPR 75x40x4bpp: 37.5 --> 38 bytes/line
```
The BC files are usually compressed (either in PCK file, or in the compressed
DAT portion of a PTH+DAT archive).<br/>

#### Cool Boarders 2 (MagDemo02: CB2\DATA\*\\*.FBD)
```
  000h 2    ID ("FB")                                ;\File Header
  002h 2    Always 1 (version? 4bpp? num entries?)   ;/
  004h 2    Palette VRAM Dest X (eg. 300h)           ;\
  006h 2    Palette VRAM Dest Y (eg. 1CCh,1EDh,1FFh) ; Palette Header
  008h 2    Palette Width in halfwords (eg. 100h)    ; (all zero when unused)
  00Ah 2    Palette Height (eg. 1 or 0Dh)            ;/
  00Ch 2    Bitmap VRAM Dest X (eg. 140h or 200h)    ;\
  00Eh 2    Bitmap VRAM Dest Y (eg. 0 or 100h)       ; Bitmap Header
  010h 2    Bitmap Width in halfwords                ;
  012h 2    Bitmap Height                            ;/
  ...  ..   Palette Data (if any)                    ;-Palette Data
  ...  ..   Bitmap Data                              ;-Bitmap Data
```
The bitmap data seems to be 4bpp and/or 8bpp, but it's hard to know the correct
palette (some files have more than 16 or 256 palette colors, or don't have any
palette at all).<br/>



##   CDROM File Video Texture/Bitmap (TGA)
#### Targa TGA
```
  000h 1   Image ID Size (00h..FFh, usually 0=None)      ;0
  001h 1   Palette Present Flag (0=None, 1=Present)      ;0            iv=1
  002h 1   Data Type code (0,1,2,3,9,10,11,32,33)        ;NEBULA=2     iv=1
  003h 2   Palette First Color (usually 0)               ;0            iv=0
  005h 2   Palette Number of Colors (usually 100h)       ;0            iv=100h
  007h 1   Palette Bits per Color (16,24,32, usually 24) ;0            iv=18h
  008h 2   Bitmap X origin (usually 0)                   ;0
  00Ah 2   Bitmap Y origin (usually 0)                   ;0
  00Ch 2   Bitmap Width                                  ;NEBULA=20h LOGO=142h
  00Eh 2   Bitmap Height                                 ;NEBULA=20h
  010h 1   Bitmap Bits per Pixel (8,16,24,32 exist?)     ;NEBULA=18h   iv=8
  011h 1   Image Descriptor (usually 0)                  ;0
  012h ..  Image ID Data (if any, len=[00h], usually 0=None)
  ...  ..  Palette
  ...  ..  Bitmap
  ...  1Ah Footer (8x00h, "TRUEVISION-XFILE.", 00h) (not present in iview)
```
Data Type [02h]:<br/>
```
  00h = No image data included  ;-Unknown purpose
  01h = Color-mapped image      ;\
  02h = RGB image               ; Uncompressed
  03h = Black and white image   ;/
  09h = Color-mapped image      ;\Runlength
  0Ah = RGB image               ;/
  0Bh = Black and white image   ;-Unknown compression method
  20h = Color-mapped image      ;-Huffman+Delta+Runlength
  21h = Color-mapped image      ;-Huffman+Delta+Runlength+FourPassQuadTree
```
The official specs do list the above 9 types, but do describe only 4 types in
detail (type 01h,02h,09h,0Ah).<br/>
```
  Type 01h and 09h lack details on supported bits per pixel (8bpp with 100h
    colors does exist; unknown if less (or more) than 8bpp are supported,
    and if so, in which bit order.
  Type 02h and 0Ah are more or less well documented.
  Type 03h has unknown bit-order, also unknown if/how it differs from type
    01h with 1bpp.
  Type 0Bh, 20h, 21h lack any details on the compression method.
```
TGA's are used by a couple of PSX games/demos (all uncompressed):<br/>
```
  16bpp: Tomb Raider 2 (MagDemo01: TOMBRAID\*.RAW)
  24bpp: Tomb Raider 2 (MagDemo05: TOMB2\*.TGA)
  24bpp: Colony Wars Venegance (MagDemo14: CWV\GAME.RSC\NEBULA*.TGA, *SKY.TGA)
  24bpp: Colony Wars Red Sun (MagDemo31: CWREDSUN\GAME.RSC\000A\*)
  16bpp: Colony Wars Venegance (MagDemo14: CWV\GAME.RSC\LOGO.DAT)
  16bpp: X-Men: Mutant Academy (MagDemo50: XMEN2\*)
  16bpp: Disney's Tarzan (MagDemo42: TARZAN\*)
  8bpp+Wrong8bitAttr: SnoCross Championship Racing (MagDemo37: SNOCROSS\*.TGA)
  16bpp+WrongYflip: SnoCross Championship Racing (MagDemo37: SNOCROSS\*.TGA)
```
For whatever reason, TGA is still in use on newer consoles:<br/>
```
  32bpp: 3DS AR Games (RomFS:\i_ar\tex\hm*.lz77
```



##   CDROM File Video Texture/Bitmap (PCX)
#### PC Paintbrush .PCX files (ZSoft)
Default extension is .PCX (some tools did use .PCX for the "main" image, and
.PCC for smaller snippets that were clipped/cropped/copied from from a large
image).<br/>
```
  000h 1    File ID (always 0Ah=PCX/ZSoft)
  001h 1    Version (0,2,3,4,5)
  002h 1    Compression (always 01h=RLE) (or inofficial: 00h=Uncompressed)
  003h 1    Bits per Pixel (per Plane) (1, 2, 4, or 8)
  004h 2    Window X1   ;\
  006h 2    Window Y1   ; Width  = X2+1-X1
  008h 2    Window X2   ; Height = Y2+1-Y1
  00Ah 2    Window Y2   ;/
  00Ch 2    Horizontal Resolution in DPI  ;\often square, but can be also zero,
  00Eh 2    Vertical Resolution in DPI    ;/or screen size, or other values
  010h 30h  EGA/VGA Palette (16 colors, 3-byte per color = R,G,B) (or garbage)
  010h 1    CGA: Bit7-4=Background Color (supposedly IRGB1111 ?)
  013h 1    CGA: Bit7:0=Color,1=Mono,Bit6:0=Yellow,1=White,Bit5:0=Dim,1=Bright
  014h 1    Paintbrush IV: New CGA Color1 Green  ;\weird new way to encode CGA
  015h 1    Paintbrush IV: New CGA Color1 Red    ;/palette in these two bytes
  040h 1    Reserved (00h) (but is 96h in animals.pcx)
  041h 1    Number of color planes (1=Palette, 3=RGB, or 4=RGBI)
  042h 2    Bytes per Line (per plane) (must be N*2) (=(Width*Bits+15)/16*2)
  044h 2    PaletteInfo? (0000h/xxxxh=Normal, 0001h=Color/BW, 0002h=Grayscale)
  046h 2    Horizontal screen size in pixels  ;\New fields, found only
  048h 2    Vertical screen size in pixels    ;/in Paintbrush IV/IV Plus
  04Ah 36h  Reserved (zerofilled) (or garbage in older files, custom in MGS)
  080h ..   Bitmap data (RLE compressed)
  ...  1    VGA Palette ID (0Ch=256 colors)                      ;\when 8bpp
  ..   300h VGA Palette (256 colors, 3-byte per color  = R,G,B)  ;/
```
Decoding PCX files is quite a hardcore exercise due to a vast amount of
versions, revisions, corner cases, incomplete & bugged specifications, and
inofficial third-party glitches.<br/>

#### PCX Versions
```
  00h = Version 2.5 whatever ancient stuff
  02h = Version 2.8 with custom 16-color palette
  03h = Version 2.8 without palette (uses fixed CGA/EGA palette)
  04h = Version ?.? without palette (uses fixed CGA/EGA palette)
  05h = Version 3.0 with custom 16-color or 256-color palette or truecolor
```
NOTE: Version[01h]=05h with PaletteInfo[44h]=0001h..0002h is Paintbrush IV?<br/>

#### Known PCX Color Depths
```
  planes=1, bits=1  P1        ;1bit, HGC 2 color (iview and paint shop pro 2)
  planes=1, bits=2  P2        ;2bit, CGA 4 color (with old/new palette info)
  planes=3, bits=1  RGB111    ;3bit, EGA 8 color (official samples)  ;\version
  planes=4, bits=1  IRGB1111  ;4bit, EGA 16 color (paint shop pro 2) ;/03h..04h
  planes=1, bits=4  P4        ;4bit, BMP 16 color (iview)
  planes=1, bits=8  P8        ;8bit, VGA 256 color palette
  planes=1, bits=8  I8        ;8bit, VGA 256 level grayscale (gmarbles.pcx)
  planes=3, bits=8  BGR888    ;24bit, truecolor (this is official 24bit format)
 ;planes=1, bits=24 BGR888 ?  ;24bit, reportedly exists? poor compression
 ;planes=4, bits=4  ABGR4444  ;16bit, wikipedia-myth? unlikely to exist
 ;planes=4, bits=8  ABGR8888  ;32bit, truecolor+alpha (used in abydos.dcx\*)
```

#### Width and Height
These are normally calculated as so:<br/>
```
  Width  = X2+1-X1      ;width for normal files
  Height = Y2+1-Y1      ;height for normal files
```
However, a few PCX files do accidentally want them to be calculated as so:<br/>
```
  Width  = X2-X1        ;width for bugged files
  Height = Y2-Y1        ;height for bugged files
```
Files with bugged width can be (sometimes) detected as so:<br/>
```
  (Width*Bits+15)/16*2) > BytesPerLine
```
Files with bugged height can be detected during decompression:<br/>
```
  BeginOfLastScanline >= Filesize (or Filesize-301h for files with palette)
```
Bugged sample files are SAMPLE.DCX, marbles.pcx and gmarbles.pcx. RLE
decompression may crash when not taking care of such files.<br/>

#### Color Planes and Palettes
The official ZSoft PCX specs are - wrongly - describing planes as:<br/>
```
  plane0 = red         ;\
  plane1 = green       ; this is WRONG, NONSENSE, does NOT exist
  plane2 = blue        ;
  plane3 = intensity   ;/
```
The 8-color and 16-color EGA images are actually using plane0,1,2,(3) as
bit0,1,2,(3) of the EGA color number; which implies plane0=blue (ie. red/blue
are opposite of the ZSoft document).<br/>
The truecolor and truecolor+alpha formats have plane0..2=red,green,blue (as
described by ZSoft), but they don't have any intensity plane (a few files are
using plane3=alpha).<br/>

#### Mono 2-Color Palette
This format was intended for 640x200pix 2-color CGA graphics, it's also common
for higher resolution FAX or print images. The general rule for these files is
to use this colors:<br/>
```
  color0=black
  color1=white
```
There are rumours that color1 could be changed to any of the 16 CGA colors
(supposedly via [10h].bit7-4, but most older & newer 2-color files have
that byte set to 00h, so one would end up with black-on-black).<br/>
Some newer 2-color files contain RGB palette entries [10h]=000000h,
[13h]=FFFFFFh (and [16h..3Fh]=00h-filled or FFh-filled).<br/>
Iview does often display 2-color images with color1=dark green (somewhat
mysteriously; it's doing that even for files that don't contain any CGA color
numbers or RGB palette values that could qualify as dark green).<br/>

#### 4-Color Palettes
This format was intended for 320x200pix 4-color CGA graphics, and the palette
is closely bound to colors available in CGA graphics modes. Color0 is defined
in [10h], and Color1-3 were originally defined in [13h], and later in
[14h,15h]:<br/>
```
  color0=[10h].bit7-4  ;(Color0 IRGB)  ;CGA Port 3D9h.bit3-0 (usually 0=black)
  bright=[13h].bit5                    ;CGA Port 3D9h.bit4    ;\
  palette=[13h].bit6                   ;CGA Port 3D9h.bit5    ; old method
  if [13h].bit7 then palette=2         ;CGA Port 3D8h.bit2    ;/
  if [01h]=05h and [44h]=0001h then                           ;\new "smart"
    if [14h]>200 or [15h]>200 then bright=1, else bright=0    ; method used in
    if [14h]>[15h] then palette=0 else palette=1              :/Paintbrush IV
  if palette=0 and bright=0 then color1..3=02h,04h,06h  ;\green-red-yellow
  if palette=0 and bright=1 then color1..3=0Ah,0Ch,0Eh  ;/
  if palette=1 and bright=0 then color1..3=03h,05h,07h  ;\cyan-magenta-white
  if palette=1 and bright=1 then color1..3=0Bh,0Dh,0Fh  ;/
  if palette=2 and bright=0 then color1..3=03h,04h,07h  ;\cyan-red-white
  if palette=2 and bright=1 then color1..3=0Bh,0Ch,0Fh  ;/
```
Palette=2 uses some undocumented CGA glitch, it was somewhat intended to output
grayscale by disabling color burst on CGA hardware with analog composite
output, but actually most or all CGA hardware is having digital 4bit IRGB
output, which outputs cyan-red-white.<br/>
The new "smart" method is apparently trying to detect if [13h-1Bh] contains RGB
values with Color1=Green or Cyan, and to select the corresponding CGA palette;
unfortunately such PCX files are merely setting [14h,15h] to match up with the
"smart" formula, without actually storing valid RGB values in [13h-1Bh].<br/>

#### 8-Color and 16-Color, with fixed EGA Palettes (version=03h or 04h)
These images have 3 or 4 planes. Plane0-3 correspond to bit0-3 of the EGA color
numbers (ie. blue=plane0, green=plane1, red=plane2, and either intensity=plane3
for 16-color, or intensity=0 for 8-color images).<br/>
Some 8-Color sample images (with version=03h and 04h) can be found bundled with
PC Paintbrush Plus 1.22 for Windows. A 16-color sample called WINSCR.PCX can be
found elsewhere in internet.<br/>
Caution 1: Official ZSoft specs are wrongly claiming plane0=red and
plane2=blue; this is wrong (although Paint Shop Pro 2 is actually implementing
it that way) (whilst MS Paint for Win95b can properly display them) (most other
tools are trying to read a palette from [10h..3Fh], which is usually garbage
filled in version=03h..04h).<br/>
Caution 2: The standard EGA palette is used for version=03h..04h (many docs
claim it to be used for version=03h only).<br/>

#### 16-Color, with custom EGA/VGA Palettes (version=02h or 05h)
These can have 1 plane with 4 bits, or 4 planes with 1 bit. Header[10h..3Fh]
contains a custom 16-color RGB palette with 3x8bit per R,G,B.<br/>
Classic VGA hardware did only use the upper 6bit of the 8bit values.<br/>
Classic EGA hardware did only use the upper 2bit of the 8bit values (that, only
when having a special EGA monitor with support for more than 16 colors).<br/>

#### 256-Color VGA Palettes (version=05h)
These have 1 plane with 8 bits. And a 256-color RGB palette with 3x8bit per
R,G,B appended at end of file.<br/>
The appended 256-color palette should normally exist only in 256-color images,
some PCX tools are reportedly always appending the extra palette to all
version=05h files (even for 2-color files).<br/>

#### 256-Level Grayscale Images (version=05h and [44h]=0002h)
The most obvious and reliable way is to use a palette with grayscale RGB
values. However, Paintbrush IV is explicetly implementing (or ignoring?) an
obscure grayscale format with following settings:<br/>
```
  [01h]=version=05h, and [44h]=0002h=grayscale
```
That settings are used in a file called gmarbles.pcx (which does contain a
256-color RGB palette with gray RGB values, ie. one can simply ignore the
special settings, and display it as normal 256-color image).<br/>

#### Default 16-color CGA/EGA Palettes
```
  Color  Name                     IRGB1111 RGB222 RGB888   Windows
  00h    dark black               0000     000    000000   000000
  01h    dark blue                0001     002    0000AA   000080
  02h    dark green               0010     020    00AA00   008000
  03h    dark cyan                0011     022    00AAAA   008080
  04h    dark red                 0100     200    AA0000   800000
  05h    dark magenta             0101     202    AA00AA   800080
  06h    dark yellow (brown)      0110     210!!  AA5500!! 808000
  07h    dark white (light gray)  0111     222    AAAAAA   C0C0C0!!
  08h    bright black (dark gray) 1000     111    555555   808080!!
  09h    bright blue              1001     113    5555FF   0000FF
  0Ah    bright green             1010     131    55FF55   00FF00
  0Bh    bright cyan              1011     133    55FFFF   00FFFF
  0Ch    bright red               1100     311    FF5555   FF0000
  0Dh    bright magenta           1101     313    FF55FF   FF00FF
  0Eh    bright yellow            1110     331    FFFF55   FFFF00
  0Fh    bright white             1111     333    FFFFFF   FFFFFF
```
Some notes on number of colors:<br/>
```
 CGA supports 16 colors in text mode (but only max 4 colors in graphics mode).
 EGA supports the same 16 colors as CGA in both text and graphics mode.
 EGA-with-special-EGA-monitor supports 64 colors (but only max 16 at once).
 VGA supports much colors (but can mimmick CGA/EGA colors, or similar colors)
```
CGA is using a 4pin IRGB1111 signal for up to 16 colors in text mode (max 4
colors in graphics mode), and CGA monitors contain some circuitry to convert
"dark yellow" to "brown" (though cheap CGA clones may display it as "dark
yellow").<br/>
EGA can display CGA colors (with all 16 colors in graphics mode).
EGA-with-special-EGA-monitor uses 6pin RGB222 signals for up to 64 colors (but
not more than 16 colors at once).<br/>
Windows is also using those 16 standard colors (when not having any VGA driver
installed, and also in 256-color VGA mode, in the latter case the 16 standard
colors are held to always available (even if different tasks are trying to
simultanously display different images with different palettes).<br/>
However, Windows has dropped brown, and uses non-pastelized bright colors.<br/>

#### PCX files in PSX games
```
  .PCX with RLE used by Jampack Vol. 1 (MDK\CD.HED\*.pcx)
  .PCX with RLE used by Hot Wheels Extreme Racing (MagDemo52: US_01293\MISC\*)
  .PCX with RLE used by Metal Gear Solid (slightly corrupted PCX files)
```

#### PCX files in PSX Metal Gear Solid (MGS)
MGS is storing some extra data at [4Ah..57h] (roughly resembling the info in
TIM files).<br/>
```
  04Ah 2    Custom MGS ID (always 3039h)
  04Ch 2    Display Mode? (08h/18h=4bit, 09h/19h=8bit)
  04Eh 2    Bitmap X-coordinate in VRAM (reportedly "divided by 2" ???)
  050h 2    Bitmap Y-coordinate in VRAM
  052h 2    Palette X-coordinate in VRAM
  054h 2    Palette Y-coordinate in VRAM
  056h 2    Palette number of actually used colors (can be less than 16/256)
  058h 28h  Reserved (zerofilled)
  080h ..   Bitmap data (RLE compressed)
  ...  1    VGA Palette ID (0Ch=256 colors)                      ;\when 8bpp
  ..   300h VGA Palette (256 colors, 3-byte per color  = R,G,B)  ;/
  ..   ..   Padding to 4-byte boundary, ie. palette isn't at filesize-301h !!!
```
MGS has filesize padded to 4-byte boundary. That is causing problems for files
with 256-color palette: The official way to find the palette is to stepback
301h bytes from end of file, which won't work with padding. To find the MGS
palette, one must decompress the whole bitmap, and then expect the 301h-byte
palette to be located after the compressed data.<br/>
As an extra oddity, MGS uses non-square ultra-high DPI values.<br/>

#### DCX Archives
DCX archives contain multiple PCX files (eg. multi-page FAX documents). The
standard format is as so:<br/>
```
  0000h 4     ID (3ADE68B1h) (987654321 decimal)
  0004h 4000h File List (32bit offsets) (max 1023 files, plus 0=End of List)
  1004h ..    File Data area (PCX files)
```
However, some files have the first PCX at offset 1000h (ie. the list is only
3FFCh bytes tall). Reportedly there are also files that start with yet smaller
offsets (for saving space when the file list contains fewer entries).<br/>
The PCX filesize is next-curr offset (or total-curr for last file).<br/>

#### References
[https://www.fileformat.info/format/pcx/egff.htm]




##   CDROM File Video 2D Graphics CEL/BGD/TSQ/ANM/SDF (Sony)
CEL/BGD/TSQ/ANM/SDF<br/>

#### CEL: Cell Data (official format with 8bit header entries)
This does merely translate Tile Numbers to VRAM Addresses and Attributes (with
the actual VRAM bitmap data usually being stored in .TIM files).<br/>
```
  000h 1   File ID (22h)
  001h 1   Version (3)
  002h 2   Flag (bit15=WithAttr, bit14=AttrDataSize:0=8bit,1=16bit, bit13-0=0)
  004h 2   Number of cell data items (in cell units) (N)
  006h 1   Sprite Editor Display Window Width  (in cell units)
  007h 1   Sprite Editor Display Window Height (in cell units)
  008h ..  Cell Data[N] (64bit entries)
  ...  ..  Cell Attr[N] (0bit/8bit/16bit user data? depending on Flag)
```
Cell Data:<br/>
```
  0-7   Tex Coord X (8bit)
  8-15  Tex Coord Y (8bit)
  16-21 Clut X      (6bit)
  22-30 Clut X      (9bit)
  31    Semi-transparency enable        ;-only in Version>=3
  32    Vertical Reversal   (Y-Flip)    ;\only in Version=0 and Version>=2
  33    Horizontal Reversal (X-Flip)    ;/
  34-47 Unused
  48-52 Texture Page (5bit)
  53-54 Semi Transparency     (0=B/2+F/2, 1=B+F, 2=B-F, 3=B+F/4)
  55-56 Texture page colors   (0=4bit, 1=8bit, 2=15bit, 3=Reserved)
  57-60 Sprite Editor Color Set Number  ;\
  61    Unused                          ; only in Version>=3
  62-63 Sprite Editor TIM Bank          ;/     XXX else hardcoded?
```
This is used in R-Types, CG.1\file3Dh\file00h, but [6,7] are 16bit wide! And
there are a LOT of ZEROes appended (plus FFh-padding due to CG.1 archive size
units).<br/>
Used by R-Types (CG.1\file07h\file01h, size 08h\*04h, with 8bit attr)<br/>
Used by R-Types (CG.1\file07h\file03h, size 10h\*08h, with 16bit attr)<br/>
Used by R-Types (CG.1\file07h\file05h, size 04h\*04h, with 16bit attr)<br/>
Used by Tiny Tank (MagDemo23: TINYTANK\TMD05.DSK\\*.CEL, size 08h\*05h)<br/>

#### CEL16: Inofficial CEL hack with 16bit entries and more extra data (R-Types)
This is an inofficial hack used by R-Types, the game does use both the official
CEL and inofficial CEL16 format.<br/>
```
  000h 1   File ID (22h)        ;\same as in official CEL version
  001h 1   Version (3)          ;/
  002h 2   Flag (...unknown meaning in this case...?)           ;<-- ?
  004h 2   Number of cell data items (in cell units) (N)
  006h 2   Sprite Editor Display Window Width  (in cell units)  ;<-- 16bit!
  008h 2   Sprite Editor Display Window Height (in cell units)  ;<-- 16bit!
  00Ah ..  Cell Data[N] (64bit entries)
  ...  ..  Cell Attr[N] (16bit/192bit user data, depending on Flag or so...?)
```
Used by R-Types (CG.1\file12h\file00h, size 0120h\*000Fh with 192bit attr)<br/>
Used by R-Types (CG.1\file15h\file00h, size 0168h\*000Fh with ? attr)<br/>
Used by R-Types (CG.1\file1Ch\file00h, size 00D8h\*000Fh with ? attr)<br/>

#### BGD: BG Map Data (official format with 8bit header entries)
```
  000h 1   File ID (23h)
  001h 1   Version (0)
  002h 2   Flag (bit15=WithAttr, bit14=AttrDataSize:0=8bit,1=16bit, bit13-0=0)
  004h 1   BG Map Width  (in cell units) (W)
  005h 1   BG Map Height (in cell units) (H)
  006h 1   Cell Width    (in pixels)
  007h 1   Cell Height   (in pixels)
  008h ..  BG Map Data[W*H] (16bit cell numbers)
  ...  ..  BG Map Attr[W*H] (0bit/8bit/16bit user data? depending on Flag)
```
Used by R-Types (CG.1\file07h\file00h, official BGD format)<br/>
Used by Cardinal Syn (MagDemo03,09: SYN\SONY\KROLOGO.WAD\\*.BGD)<br/>
Used by Tiny Tank (MagDemo23: TINYTANK\TMD05.DSK\\*.BGD, with 8bit entries).<br/>

#### BGD16: Inofficial BGD hack with 16bit entries (R-Types)
This is an inofficial hack used by R-Types, the game does use both the official
BGD and inofficial BGD16 format. Apparently invented to support bigger BG Map
Widths for huge sidescrolling game maps.<br/>
```
  000h 1   File ID (23h)        ;\same as in official BGD version
  001h 1   Version (0)          ;/
  002h 2   Flag (bit15=WithAttr, bit14=AttrDataSize:0=8bit,1=16bit, bit13-0=0)
  004h 2   BG Map Width  (in cell units) (W)                    ;<-- 16bit!
  006h 2   BG Map Height (in cell units) (H)                    ;<-- 16bit!
  008h 2   Cell Width    (in pixels)                            ;<-- 16bit!
  00Ah 2   Cell Height   (in pixels)                            ;<-- 16bit!
  00Ch ..  BG Map Data[W*H] (16bit cell numbers)
  ...  ..  BG Map Attr[W*H] (0bit/8bit/16bit user data? depending on Flag)
  ...  ..  FFh-padding (in case being stored in R-Types' DOT1 archives)
```
Used by R-Types (CG.1\file3Ch\file00h, inofficial BGD16 format)<br/>

#### TSQ: Animation Time Sequence
```
  000h 1   File ID (24h)
  001h 1   Version (1)
  002h 2   Number of Sequence data entries (N)
  004h N*8 Sequence Data (64bit entries)
```
Sequence Data:<br/>
```
  0-15  Sprite Group Number to be displayed
  16-23 Display Time
  24-27 Unused
  28-31 Attribute (user defined) (only in Version>=1)
  32-47 Hotspot X Coordinate
  48-63 Hotspot Y Coordinate
```
There aren't any known games using .TSQ files.<br/>

#### ANM: Animation Information
```
  000h 1    File ID (21h)
  001h 1    Version (3=normal) (but see below notes on older versions)
  002h 2    Flag (bit0-1=TPF, bit2-11=0, bit12-15=CLT)
             0-1   TPF PixFmt (0=4bpp, 1=8bpp, 2/3=Reserved)   ;version>=2 only
             2-11  -   Reserved (0)
             12-15 CLT Number of CLUT Groups, for color animation
  004h 2    Number of Sprites Groups
  006h 2    Number of Sequences (N) (can be 0=None)
  008h N*8  Sequence(s) (64bit per entry)  ;Num=[004h]
  ...  ..   Sprite Group(s)                ;Num=[006h]
  ...  ..   CLUT Group(s)                  ;Num=[002h].bit12-15
```
Sequence entries:<br/>
```
  000h 2  Sprite Group Number to be displayed (range 0..AnimHdr[004h]-1)
  002h 1  Display Time (can be 00h or 0Ah or whatever)
  003h 1  Attribute (bit0-3=Unused/Zero, bit4-7=User defined)  ;version>=3 only
  004h 2  Hotspot X Coordinate (usually 0, or maybe can be +/-NN ?)
  006h 2  Hotspot Y Coordinate (usually 0, or maybe can be +/-NN ?)
```
Sprite Group entries:<br/>
```
 Each "Group" seems to represent one animation frame.
 Each "Group" can contain one or more sprites (aka metatiles).
 Below stuff is "4+N*14h" bytes, that seems to repeat "AnmHeader[004h] times"
 XXX... actually below can be "4+N*10h" or "4+N*14h" bytes
 XXX... so, maybe maybe some entries like width/height are optional?
  000h 4     Number of Sprites in this Sprite Group ("sprites per metatile"?)
  004h 14h*N Sprite(s) (see below)
 Sprites:
  000h 1   Tex Coord X (8bit)
  001h 1   Tex Coord Y (8bit)
  002h 1   Offset X from Hotspot within frame (maybe vertex x ?)
  003h 1   Offset Y from Hotspot within frame (maybe vertex y ?)
  004h 2   CBA Clut Base (bit0-5=ClutX, Bit6-14=ClutY, bit15=SemiTransp)
  006h 2   FLAGs (bit0-4, bit5-6, bit7-8, bit9, bit10, bit11, bit12-15)
            0-4   TPN Texture Page Number
            5-6   ABR Semi-Transparency Rate
            7-8   TPF Pixel depth (0=4bpp, 1=8bpp, 2=16bpp)
            9     -   Reserved
            10    RSZ Scaling  (0=No, 1=Scaled)
            11    ROT Rotation (0=No, 1=Rotated)
            12-15 THW Texture Width/Height div8 (0=Other custom width/height)
  008h (2) Texture Width    "of optional size" (uh?)  ;\only present if
  00Ah (2) Texture Height   "of optional size" (uh?)  ;/FLAGs.bit12-15=0 ?)
  00Ch 2   Angle of Rotation (in what units?)
  00Eh 2   Sprite Editor info (bit0-7=Zero, bit8-13=ClutNo, bit14-15=TimBank)
  010h 2   Scaling X (for Vertex?) (as whatever fixed point number) (eg. 1000h)
  012h 2   Scaling Y (for Vertex?) (as whatever fixed point number) (eg. 1000h)
```
CLUT Group entries:<br/>
```
  000h 4  CLUT size in bytes (Width*Height*2+0Ch)
  004h 2  Clut X Coordinate
  006h 2  Clut Y Coordinate
  008h 2  Clut Width
  00Ah 2  Clut Height
  00Ch .. CLUT entries (16bit per entry, Width*Height*2 bytes)
```
Note: ALICE.PAC\MENU.PAC\CON00.ANM has NumSequences=0 and NumSpriteGroups=2Dh
(unknown if/how that is animated, maybe it has 2Dh static groups? or the groups
are played in order 0..2Ch with display time 1 frame each?).<br/>
Used by Alice in Cyberland (ALICE.PAC\\*.ANM) (ANM v3)<br/>
Unknown if there are any other games are using that format.<br/>

#### SDF: Sprite Editor Project File
This is an ASCII text file for "artist boards" with following entries:<br/>
```
  TIM0 file0.tim             ;\
  TIM1 file1.pxl file1.clt   ; four TIM banks (with TIM or PXL/CLT files)
  TIM2                       ; (or no filename for empty banks)
  TIM3                       ;/
  CEL0 file0.cel             ;-one CEL (with CEL, or no filename if none)
  MAP0 file0.bgd             ;\
  MAP1 file1.bgd             ; four BG MAP banks (with BGD filenames)
  MAP2                       ; (or no filename for empty banks)
  MAP3                       ;/
  ANM0 file0.anm             ;-one ANM (with ANM, or no filename if none)
  DISPLAY n       ;0-3=256/320/512/640x240, 4-7=256/320/512/640x480
  COLOR n         ;0=4bpp, 1=8bpp  ;docs are unclear, is it COLORn or COLOR n?
  ADDR0 texX texY clutX clutY numColorSets ;\
  ADDR1 texX texY clutX clutY numColorSets ; four texture/palette offsets
  ADDR2 texX texY clutX clutY numColorSets ; for the corresponding TIM banks
  ADDR3 texX texY clutX clutY numColorSets ;/ (or whatever for empty banks?)
```



##   CDROM File Video 3D Graphics TMD/PMD/TOD/HMD/RSD (Sony)
```
 ____________________________________ TMD _____________________________________
```

#### TMD - Modeling Data for OS Library
```
  000h 4     ID (00000041h)
  004h 4     Flags (bit0=FIXP, bit1-31=Reserved/zero)
  008h 4     Number of Objects (N)     ;"integral value" uh?
  00Ch N*1Ch Object List (1Ch-byte per entry)
  ...  ..    Data (Vertices, Normals, Primitives)
```
Object List entries:<br/>
```
  000h 4    Start address of a Vertex     ;\Address values depend on the
  004h 4    Number of Vertices            ; file header's FIXP flag:
  008h 4    Start address of a Normal     ;  FIXP=0 Addr from begin of Object
  00Ch 4    Number of Normals             ;  FIXP=0 Addr from begin of TMD File
  010h 4    Start address of a Primitive  ;
  014h 4    Number of Primitives          ;/
  018h 4    Scale (signed shift value, Pos=SHL, Neg=SHR) (not used by LIBGS)
```
Vertex entries (8-byte):<br/>
```
  000h 2    Vertex X (signed 16bit)
  002h 2    Vertex Y (signed 16bit)
  004h 2    Vertex Z (signed 16bit)
  006h 2    Unused
```
Normal entries (8-byte) (if any, needed only for computing light directions):<br/>
```
  000h 2    Normal X (fixed point 1.3.12)
  002h 2    Normal Y (fixed point 1.3.12)
  004h 2    Normal Z (fixed point 1.3.12)
  006h 2    Unused
```
Primitive entries (variable length):<br/>
```
  000h 1    Output Size/4 of the GPU command (after GTE conversion)
  001h 1    Input Size/4 of the Packet Data in the TMD file
  002h 1    Flag
              0   Light source calculation (0=On, 1=Off)
              1   Clip Back (0=Clip, 1=Don't clip) (for Polygons only)
              2   Shading (0=Flat, 1=Gouraud)
                   (Valid only for the polygon not textured,
                   subjected to light source calculation)
              3-7 Reserved (0)
  003h 1    Mode (20h..7Fh) (same as GP0(20h..7Fh) command value in packet)
  004h ..   Packet Data
```
Packet Data (for Polygons)<br/>
```
  000h 4   GPU Command+Color for that packet (CcBbGgRrh), see GP0(20h..3Fh)
  ... (4)  Texcoord1+Palette (ClutYyXxh)               ;\
  ... (4)  Texcoord2+Texpage (PageYyXxh)               ; only if Mode.bit2=1
  ... (4)  Texcoord3         (0000YyXxh)               ;
  ... (4)  Texcoord4         (0000YyXxh) ;-quad only   ;/
  ... (4)  Color2 (00BbGgRrh)                          ;\
  ... (4)  Color3 (00BbGgRrh)                          ; only if Flag.bit2=1
  ... (4)  Color4 (00BbGgRrh) ;-quad only              ;/
  ... (2)  Normal1 (index in Normal list?)  ;always, unless Flag.bit0=1
  ...  2   Vertex1 (index in Vertex list?)
  ... (2)  Normal2 (index in Normal list?)             ;-only if Mode.bit4=1
  ...  2   Vertex2 (index in Vertex list?)
  ... (2)  Normal3 (index in Normal list?)             ;-only if Mode.bit4=1
  ...  2   Vertex3 (index in Vertex list?)
  ... (2)  Normal4 (index in Normal list?) ;\quad only ;-only if Mode.bit4=1
  ...  2   Vertex4 (index in Vertex list?) ;/
  ... (2)  Unused zeropadding (to 4-byte boundary)
```
Packet Data (for Lines)<br/>
```
  000h 4   GPU Command+Color for that packet (CcBbGgRrh), see GP0(40h,50h)
  ... (4)  Color2 (00BbGgRrh)                          ;-only if Mode.bit4=1
  ...  2   Vertex1 (index in Vertex list?)
  ...  2   Vertex2 (index in Vertex list?)
```
Packet Data (for Rectangle/Sprites)<br/>
```
  000h 4   GPU Command+Color for that packet (CcBbGgRrh), see GP0(60h..7Fh)
  ...  ..  Unknown, reportedy "with 3-D coordinates and the drawing
           content is the same as a normal sprite."
```
Note: Objects should usually contain Primitives and Vertices (and optionally
Normals), however, N2O\SHIP.TMD does contain some dummy Objects with Number of
Vertices/Normals/Primitives all set to zero.<br/>
Used by Playstation Logo (in sector 5..11 on all PSX discs, 3278h bytes)<br/>
Used by ...???model???... (MagDemo54: MODEL\\*.BIN\\*.TMD)<br/>
Used by Alice in Cyberland (ALICE.PAC\xxx\_TM\*.FA\\*.TMD)<br/>
Used by Armored Core (MagDemo02: AC10DEMP\MS\MENU\_TMD.T\\*)<br/>
Used by Bloody Roar 1 (MagDemo06: CMN\EFFECT.DAT\0005h)<br/>
Used by Deception III Dark Delusion (MagDemo33: DECEPT3\K3\_DAT.BIN\056A,0725\\*)<br/>
Used by Gundam Battle Assault 2 (DATA\\*.PAC\\*)<br/>
Used by Hear It Now (Playstation Developer's Demo) (\*.TMD and FISH.DAT).<br/>
Used by Jersey Devil (MagDemo10: JD\\*.BZZ\\*)<br/>
Used by Klonoa (MagDemo08: KLONOA\FILE.IDX\\*)<br/>
Used by Legend of Dragoon (MagDemo34: LOD\DRAGN0.BIN\16xxh)<br/>
Used by Macross VF-X 2 (MagDemo23: VFX2\DATA01\\*.TMD)<br/>
Used by Madden NFL '98 (MagDemo02: TIBURON\MODEL01.DAT\\*)<br/>
Used by No One Can Stop Mr. Domino (MagDemo18: DATA\\*, .TMD and DOT1\TMD)<br/>
Used by O.D.T. (MagDemo17: ODT\\*.LNK\\*)<br/>
Used by Parappa (MagDemo01: PARAPPA\COMPO01.INT\3\\*.TMD)<br/>
Used by Resident Evil 1 (PSX\ITEM\_M1\\*.DOR\0001)<br/>
Used by Starblade Alpha (FLT\SB2.DAT\\* and TEX\SB2.DAT\\*)<br/>
Used by Tiny Tank (MagDemo23: TINYTANK\TMD\*.DSK\\*.TMD)<br/>
Used by WCW/nWo Thunder (MagDemo19: THUNDER\RING\\*.TMD)<br/>
Used by Witch of Salzburg (the MODELS\\*.MDL\\*.TMD)<br/>
Used by Scooby Doo and the Cyber Chase (MagDemo54: MODEL\\*\\*)<br/>

```
 ____________________________________ PMD _____________________________________
```

#### PMD - High-Speed Modeling Data
This is about same as TMD, with less features, intended to work fasrer.<br/>
```
  000h 4    ID (00000042h)
  004h 4    Offset to Primitives
  008h 4    Offset to Shared Vertices (or 0=None)
  00Ch 4    Number of Objects
  010h ..   Objects         (4+N*4 bytes each, with offsets to Primitives)
  ...  ..   Primitives
  ...  ..   Shared Vertices (8-bytes each, if any)
```
Vertex entries (8-byte):<br/>
```
  000h 2    Vertex X (signed 16bit)
  002h 2    Vertex Y (signed 16bit)
  004h 2    Vertex Z (signed 16bit)
  006h 2    Unused
```
Objects:<br/>
```
  000h 4    Number of Primitives
  004h N*4  Offsets to Primitives ... maybe relative to hdr[004h] ?
```
Primitives:<br/>
```
  000h 2    Number of Packets
  002h 2    Type flags
             0    Polygon   (0=Triangle, 1=Quadrilateral)
             1    Shading   (0=Flat, 1=Gouraud)           ;uh, with ONE color?
             2    Texture   (0=Texture-On, 1=Texture-Off) ;uh, withoutTexCoord?
             3    Shared    (0=Independent vertex, 1=Shared vertex)
             4    Light source calculation (0=Off, 1=On)  ;uh, withoutNormal?
             5    Clip      (0=Back clip, 1=No back clip)
             6-15 Reserved for system
  004h ...  Packet(s)
```
Packet entries, when Type.bit3=0 (independent vertex):<br/>
```
  000h 4   GPU Command+Color for that packet (CcBbGgRrh), see GP0(20h..7Fh)
  004h 8   Vertex1 (Xxxxh,Yyyyh,Zzzzh,0000h)
  00Ch 8   Vertex2 (Xxxxh,Yyyyh,Zzzzh,0000h)
  014h 8   Vertex3 (Xxxxh,Yyyyh,Zzzzh,0000h)
  01Ch (8) Vertex4 (Xxxxh,Yyyyh,Zzzzh,0000h) ;<-- only when Type.bit0=1 (quad)
```
Packet entries, when Type.bit3=1 (shared vertex):<br/>
```
  000h 4   GPU Command+Color for that packet (CcBbGgRrh), see GP0(20h..7Fh)
  004h 4   Offset to Shared Vertex1    ;offsets are
  008h 4   Offset to Shared Vertex2    ;"from the start of a row"
  00Ch 4   Offset to Shared Vertex3    ;aka from "Packet+04h" ?
  010h (4) Offset to Shared Vertex4          ;<-- only when Type.bit0=1(quad)
```
Unknown if/how Texture/Light is implemented... without TexCoords/Normals?<br/>
Unknown if/how Gouraud is implemented... with ONE color and without Normals?<br/>
Used only by a few games:<br/>
```
  Cool Boarders 2 (MagDemo02: CB2\DATA3\*.PMD)
  Cardinal Syn (MagDemo03,09: SYN\*\*.WAD\*.PMD)    (4-byte hdr plus PMD file)
  Sesame Streets Sports (MagDemo52: SSS\LV*\*MRG\*) (4-byte hdr plus PMD file)
```
Unknown if/which other games are using the PMD format.<br/>

```
 ____________________________________ TOD _____________________________________
```

#### TOD - Animation Data
```
  000h 1    ID (50h)
  001h 1    Version (0)
  002h 2    Resolution (time per frame in 60Hz units, can be 0) (60Hz on PAL?)
  004h 4    Number of Frames
  008h ..   Frame1
  ...  ..   Frame2
  ...  ..   Frame3
  ...  ..   etc.
```
Frames:<br/>
```
  000h 2    Frame Size in words (ie. size/4)
  002h 2    Number of Packets (can be 0=None, ie. do nothing this frame)
  004h 4    Frame Number (increasing 0,1,2,3,..)
  008h ...  Packet(s)
```
Packet:<br/>
```
  000h 2    Object ID
  002h 1    Type/Flag (bit0-3=Type, bit4-7=Flags)
  003h 1    Packet Size ("in words (4 bytes)")
  004h ...  Packet Data
```
XXX... in Sony's doc.<br/>
Used by Witch of Salzburg (ANIM\ANM0\ANM0.TOD) (oddly with [02h]=0000h)<br/>
Used by Parappa (MagDemo01: PARAPPA\COMPO01.INT\3\\*.TOD)<br/>
Used by Macross VF-X 2 (MagDemo23: VFX2\DATA01\\*.TOD and \*.TOX)<br/>
Used by Alice in Cyberland (ALICE.PAC\xxx\_T\*.FA\\*.TOD)<br/>
Unknown if/which other games are using the TOD format.<br/>

```
 ____________________________________ HMD _____________________________________
```

#### HMD - Hierarchical 3D Model, Animation and Other Data
```
  000h 4    ID (00000050h)   ;same as in TOD, which CAN ALSO have MSBs=zero(!)
  004h 4    MAP FLAG (0 or 1, set when mapped via GsMapUnit() function)
  008h 4    Primitive Header Section pointer (whut?)
  00Ch 4    Number of Blocks
  010h 4*N  Pointers to Blocks
  ...       Primitive Header section    (required)
  ...       Coordinate section          (optional)
  ...       Primitive section           (required)
```
This format is very complicated, see Sony's "File Formats" document for
details.<br/>
.HMD used by Brunswick Bowling (MagDemo13: THQBOWL\\*).<br/>
.HMD used by Soul of the Samurai (MagDemo22: RASETSU\0\OPT01T.BIN\0\0\\*)<br/>
.HMD used by Bloody Roar 2 (MagDemo22: LON\LON\*.DAT\\*, ST5\ST\*.DAT\02h..03h)<br/>
.HMD used by Ultimate Fighting Championship (MagDemo38: UFC\CU00.RBB\6Bh..EFh)<br/>
Unknown if/which games other are using the HMD format.<br/>

```
 ____________________________________ RSD _____________________________________
```

#### RSD Files (RSD,PLY,MAT,GRP,MSH,PVT,COD,MOT,OGP)
RSD files consist of a set of several files (RSD,PLY,MAT,etc). The files
contain the "polygon source code" in ASCII text format, generated from Sony's
"SCE 3D Graphics Tool". For use on actual hardware, the "RSDLINK" utility can
be used to convert them to binary (TMD, PMD, TOD?, HMB?) files.<br/>
```
  RSD Main project file
  PLY Polygon Vertices (Vertices, Normals, Polygons)
  MAT Polygon Material (Color, Blending, Texture)
  GRP Polygon Grouping
  MSH Polygon Linking                   ;\
  PVT Pivot Rotation center offsets     ; New Extended
  COD Vertex Coordinate Attributes      ; (since RSD version 3)
  MOT Animation Information             ;/
  OGP Vertex Object Grouping            ;-Sub-extended
```
All of the above files are in ASCII text format. Each file is starting with a
"@typYYMMDD" string in the first line of the file, eg. "@RSD970401" for RSD
version 3. Vertices are defined as floating point values (as ASCII strings).<br/>
There's more info in Sony's "File Formats" document, but the RSD stuff isn't
used on retail discs. Except:<br/>
```
  RSD/GRP/MAT/PLY (and DXF=whatever?) used on Yaroze disc (DTL-S3035)
```



##   CDROM File Video STR Streaming and BS Picture Compression (Sony)
#### STR Files (movie streams)
[CDROM File Video Streaming STR (Sony)](cdromfileformats.md#cdrom-file-video-streaming-str-sony)<br/>
[CDROM File Video Streaming STR Variants](cdromfileformats.md#cdrom-file-video-streaming-str-variants)<br/>
[CDROM File Video Streaming Framerate](cdromfileformats.md#cdrom-file-video-streaming-framerate)<br/>
[CDROM File Video Streaming Audio](cdromfileformats.md#cdrom-file-video-streaming-audio)<br/>
[CDROM File Video Streaming Chunk-based formats](cdromfileformats.md#cdrom-file-video-streaming-chunk-based-formats)<br/>
[CDROM File Video Streaming Mis-mastered files](cdromfileformats.md#cdrom-file-video-streaming-mis-mastered-files)<br/>
Apart from the 20h-byte STR headers, movies basically consist of a series of BS
files (see below).<br/>

#### BS Files (Huffman compressed MDEC codes)
BS stands for bitstream, which might refer to the use in STR files, or to the
Huffman bitstreams.<br/>
[CDROM File Video BS Compression Versions](cdromfileformats.md#cdrom-file-video-bs-compression-versions)<br/>
[CDROM File Video BS Compression Headers](cdromfileformats.md#cdrom-file-video-bs-compression-headers)<br/>
The header is followed by the bitstream...<br/>
```
  v1/v2/v3/ea/iki --> first bit in bit15 of first halfword (good for psx)
  v0              --> first bit in bit7 of first byte (not so good for psx)
  (to use the same decoder for all version: swap each 2 bytes in v0)
```
For each block, the bitstream contains one DC value, up to 63 AC values,
terminated by EOB (end of block).<br/>
[CDROM File Video BS Compression DC Values](cdromfileformats.md#cdrom-file-video-bs-compression-dc-values)<br/>
[CDROM File Video BS Compression AC Values](cdromfileformats.md#cdrom-file-video-bs-compression-ac-values)<br/>
Apart from being used in STR movies, BS can be also used to store single
pictures:<br/>
[CDROM File Video BS Picture Files](cdromfileformats.md#cdrom-file-video-bs-picture-files)<br/>

#### Wacwac (similar as BS, but with completely different Huffman codes)
[CDROM File Video Wacwac MDEC Streams](cdromfileformats.md#cdrom-file-video-wacwac-mdec-streams)<br/>

#### Credits
Thanks to Michael Sabin for info on various STR and BS variants:<br/>
[https://github.com/m35/jpsxdec/]




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
[CDROM File Video Polygon Streaming](cdromfileformats.md#cdrom-file-video-polygon-streaming)<br/>

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

```
 ______________________________________________________________________________
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

```
 ________________________ Customized STR Video Headers ________________________
```

#### Viewpoint (with slightly modified STR header)
```
  008h 4    Frame number (0=First)                      ;<-- instead of 1=First
  01Ch 2    Unknown (always D351h)                      ;<-- instead of zero
  01Eh 2    Number of Frames in this STR file           ;<-- instead of zero
```

#### Capcom games
Resident Evil 2 (ZMOVIE\\*.STR, PL0\ZMOVIE\\*.STR)<br/>
Super Puzzle Fighter II Turbo (STR/CAPCOM15.STR)<br/>
```
  01Ch 4    Sector number of 1st sector of current frame  ;<-- instead of zero
```

#### Chrono Cross Disc 2 Video
Chrono Cross Disc 1 does have normal STR headers, but Disc 2 has Type.bit8
toggled:<br/>
```
  002h 2    STR Type (8101h=Disc 2)                       ;<-- instead of 8001h
```
And, the Chrono Cross "final movie" does reportedly have "additional
properties". Unknown, what that means, it does probably refer to the last movie
on Chrono Cross Disc 2, which is quite huge (90Mbyte), and has lower resolution
(160x112), and might have whatever "additional properties"?<br/>

#### Need for Speed 3
Need for Speed 3 Hot Pursuit (MOVIES\\*.XA, contains videos, not raw XA-ADPCM)<br/>
Jackie Chan Stuntmaster (FE\MOVIES\\*.STR)<br/>
With slightly modified STR headers:<br/>
```
  014h 4    Number of Frames (..excluding last some frames?) ;-instead BS[0..3]
  018h 4    Unlike the above modified entry, this is normal  ;-copy of BS[4..7]
```

#### ReBoot (MOVIES\\*.WXA)
This has leading XA-ADPCM, and customized STR header:<br/>
```
  014h 2    Type (0000h=Normal, 01FFh=Empty frames at end of video)
  016h 2    Number of Frames (excluding empty ones at end of video)
  018h 8    Zerofilled
```

#### Gran Turismo 1 (230Mbyte STREAM.DAT) and Gran Turismo 2 (330Mbyte STREAM.DAT)
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

#### PGA Tour 96, 97, 98 (VIDEO\..\\*.XA and ZZBUFFER\\*.STR)
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

#### Alice in Cyber Land (\*.STR)
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

#### Encrypted iki (Panekit - Infinitive Crafting Toy Case)
```
  014h 8    Copy of decrypted BS header (instead of encrypted BS header)
```

#### Princess Maker: Yumemiru Yousei (PM3.STR)
#### Parappa (Japanese Demo version only) (S0/GUIDE.STR)
These files do have BS ID=3000h (except, the first and last some frames have
nromal ID=3800h). The STR header is quite normal (apart from reflecting the odd
BS ID):<br/>
```
  016h 2    Copy of BS ID, 3000h in most frames (instead of 3800h)
  020h 7E0h Data (in BS format, also with BS ID 3000h, instead of 3800h)
```

#### Starblade Alpha and Galaxian 3
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

#### Largo Winch: Commando SAR (FMV\NSPIN\_W.RNG)
This is a somewhat "normal" movie, without audio, and with the STR headers
moved to the begin of the file:<br/>
```
  000h Nx20h   STR Headers  ;size = filesize/800h*20h
  ...  Nx7E0h  Data         ;size = filesize/800h*7E0h
```
Note: The movie contains the rotating "W" logo, which is looped in Start
screen.<br/>

#### Player Manager (1996, Anco Software) (FILMS\1..3\\*.STR)
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

#### Chiisana Kyojin Microman (DAT\STAGE\*\\*.MV)
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

#### Black Silence padding
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

#### Ridge Racer Type 4 (only PAL version) (R4.STR)
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

#### Mat Hoffman's Pro BMX (MagDemo48: MHPB\SHORT.STR)
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

#### Final Fantasy VII (FF7) (MOVIE\\*.MOV and MOVIE\\*.STR)
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

#### Final Fantasy IX (FF9) (\*.STR and \*.MBG)
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

```
 _______________________ Non-standard STR Video Headers _______________________
```

#### Final Fantasy VIII (FF8)
Video frames are always 320x224. The video frames are preceeded by two
SPU-ADPCM audio sectors.<br/>
```
  000h 4    ID "SMJ",01h=Video
  004h 1    Sector number within current Frame (02h..num-1) (2..9 for video)
  005h 1    Total number of Audio+Video sectors in this frame, minus 1 (9)
  006h 2    Frame number (0=First)
  008h 7F8h Data (in BS v2 format)
```

#### Ace Combat 3 Electrosphere (in 520Mbyte ACE.SPH/SPB archive)
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

#### Judge Dredd (1998, Gremlin) (CUTS\\*.IXA and LEVELS\\*\\*.IXA)
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

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_<br/>

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
[CDROM File Audio Streaming XA-ADPCM](cdromfileformats.md#cdrom-file-audio-streaming-xa-adpcm)<br/>
However, there are also movies without audio. And a few movies with SPU-ADPCM
audio.<br/>

#### SPU-ADPCM in Chunk-based formats
[CDROM File Video Streaming Chunk-based formats](cdromfileformats.md#cdrom-file-video-streaming-chunk-based-formats)<br/>

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
[CDROM File XYZ and Dummy/Null Files](cdromfileformats.md#cdrom-file-xyz-and-dummynull-files)<br/>
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
[CDROM File Video Polygon Streaming](cdromfileformats.md#cdrom-file-video-polygon-streaming)<br/>

#### MPEG1 (on VCD Video CDs)
MPEG1 uses I/P/B-Frames, the I-Frames may reach similar compression as BS
files. However, P-Frames and B-Frames do compress much better than BS files.<br/>
[CDROM Video CDs (VCD)](cdromfileformats.md#cdrom-video-cds-vcd)<br/>
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
The first 20h byte of the iki header & data are encrypted. Among others,
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
[CDROM File Compression LZSS (Serial Experiments Lain)](cdromfileformats.md#cdrom-file-compression-lzss-serial-experiments-lain)<br/>
The Transparency Mask is stored as scanlines (not as macroblocks), the
upper/left pixel is in bit7-6 of first byte, the 2bit alpha values are ranging
from 0=Transparent to 3=Solid.<br/>

#### BS ea Headers (Electronic Arts)
EA videos are chunk based (instead of using 20h-byte .STR headers).<br/>
[CDROM File Video Streaming Chunk-based formats](cdromfileformats.md#cdrom-file-video-streaming-chunk-based-formats)<br/>
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
[Macroblock Decoder (MDEC)](macroblockdecodermdec.md)<br/>



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
[CDROM File Compression GT-ZIP (Gran Turismo 1 and 2)](cdromfileformats.md#cdrom-file-compression-gt-zip-gran-turismo-1-and-2)<br/>
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
[SPU ADPCM Samples](soundprocessingunitspu.md#spu-adpcm-samples)<br/>
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
[http://github.com/vgmstream/vgmstream/blob/master/src/meta/vag.c] ;very detailed<br/>
[http://wiki.xentax.com/index.php/VAG_Audio] ;rather incomplete and perhaps wrong<br/>



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
```
 __________________________ .SQ .HD .HD (SSsq/SShd) ___________________________
```

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

#### Sequence Data (\*.SQ)
```
  000h 2       Unknown (always 64h)
  002h 2       Unknown (always 1E0h)
  004h 1?      Unknown (varies)
  005h 7       Zerofilled
  00Ch 4       ID "SSsq"
  010h 10h*10h Unknown Table
  110h ..      Unknown Data
```

#### Voice Header (\*.HD)
```
  000h 4     Size of the .HD file itself
  004h 4     Size of the corresponding .BD file
  008h 4     Zero
  00Ch 4     ID "SShd"
  010h 1Ch*4 Offsets to data (or FFFFFFFFh=None)
  080h ..    Data
```

#### Voice Bonary (\*.BD) (same as .VB files)
```
  000h ..    SPU-ADPCM data (usually starting with zerofilled 10h-byte block)
```

```
 ____________________________ DNSa/PMSa/FNSa/FMSa _____________________________
```

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

#### "PMSa"  (aka SaMPles backwaords)
```
  000h 4     ID "PMSa"
  004h 4     Total Filesize
  008h 8     Zerofilled
  010h ..    SPU-ADPCM data (usually starting with zerofilled 10h-byte block)
```

#### "DNSa"  (aka SouND backwards)
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

#### "FNSa"  (aka SouNd-F... backwards)
These are whatever tiny files (with filesize 1Ch or 2Ch).<br/>
```
  000h 4     ID "FNSa"
  ...  ..    Unknown
```

#### "FMSa"  (aka SaMples-F... backwards)
```
  000h 4     ID "FMSa"
  008h ..    Unknown..
  ...  ..    SPU-ADPCM data (usually starting with zerofilled 10h-byte block)
```

```
 ____________________________________ AKAO ____________________________________
```

There a several games that have sound files with ID "AKAO".<br/>
```
  XXX does that include different AKAO formats... for Samples and Midi?
```
AKAO is also used in several streaming movies:<br/>
[CDROM File Video Streaming Audio](cdromfileformats.md#cdrom-file-video-streaming-audio)<br/>

```
 ___________________________________ Others ___________________________________
```

Alone in the Dark IV has MIDB and DSND chunks (which contain sound files).<br/>

#### See also
The page below does mention several PSX sound formats, plus some open source
& closed source tools for handling those files.<br/>
github.com/loveemu/vgmdocs/blob/master/Conversion\_Tools\_for\_Video\_Game\_Music.md<br/>



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



##   CDROM File Archives with Filename
```
 _______________________________ Entrysize=08h ________________________________
```

#### WWF Smackdown (MagDemo33: TAI\\*.PAC)
```
  000h 4     ID ("DPAC")                                        ;\
  004h 4     Unknown (100h)                                     ;
  008h 4     Number of files (N)                                ;
  00Ch 4     Directory Size (N*8)                               ; Header
  010h 4     File Data area size (SIZE = Totalsize-Headersize)  ;
  014h 4     Unknown (1)                                        ;
  018h 7E8h  Zerofilled (padding to 800h-byte boundary)         ;
  800h N*8   File List                                          ;
  ...  ..    Zerofilled (padding to 800h-byte boundary)         ;/
  ...  SIZE  File Data area                                     ;-Data area
 File List entries:
  000h 8     Filename ("NAME")
  004h 2     File Offset/800h (increasing)
  006h 2     File Size/800h
```
The DPAC archives can contain generic files (eg .TIM) and child archives (in a
separate archive format, with ID "PAC ").<br/>

```
 _______________________________ Entrysize=10h ________________________________
```

#### Championship Motocross (MagDemo25: SMX\RESHEAD.BIN and RESBODY.BIN)
RESHEAD.BIN:<br/>
```
  000h N*10h  File List (220h bytes)
 File List entries:
  000h 8      Filename ("FILENAME", if shorter: terminated by 00h plus garbage)
  008h 4      Filesize in bytes
  00Ch 4      Offset/800h in RESBODY.BIN (increasing) (or FFFFFFFFh if Size=0)
```
RESBODY.BIN:<br/>
```
  000h ..     File Data (referenced from RESHEAD.BIN)
```

#### One (DIRFILE.BIN\w\*\sect\*.bin)
```
  000h N*10h File List
  ...  ..    File Data area
 File List entries:
  000h 0Ch   Filename (eg. "FILENAME 001")     ;for last entry: "END      000"
  00Ch 4     Offset (increasing, N*10h and up) ;for last entry: zero
```

#### True Love Story 1 and 2 (TLS\*\MCD.DIR and MCD.IMG)
MCD.DIR:<br/>
```
  000h N*10h  File List
  ...  10h    End marker (FFh-filled)
 File List entries:
  000h 8      Filename (zeropadded if less than 8 chars)
  008h 2      Zero (0000h)
  00Ah 2      Size/800h
  00Ch 4      Offset/800h in MCD.IMG
 Note: Filenames are truncated to 8 chars (eg. "FOREST.T" instead "FOREST.TIM")
```
MCD.IMG:<br/>
```
  000h ..     File Data area (encrypted in True Love Story 2)
```
In True Love Story 2, the MCD.IMG data is encrypted as follows:<br/>
```
 init_key_by_filename(name):    ;for MCD.IMG (using filenames from MCD.DIR)
  i=0, key0=0001h, key1=0001h, key2=0001h
  while i<8 and name[i]<>00h
    key0=(key0 XOR name[i])
    key1=(key1 * name[i]) AND FFFFh
    key2=(key2 + name[i]) AND FFFFh
  ret
 init_key_by_numeric_32bit_seed(seed):  ;maybe for LINEAR.IMG and PICT.IMG ?
  key0=(seed) AND FFFFh
  key1=(seed - (seed*77975B9h/400000000h)*89h) AND FFFFh
  key2=(seed - (seed*9A1F7E9h/20000000000h)*3527h) AND FFFFh
  ret
 decrypt_data(addr,len):
  for i=1 to len/2
    key2=key2/2 + (key0 AND 1)*8000h
    key0=key0/2 + (key1 AND 1)*8000h
    key1=key1/2 + ((key1/2 OR key0) AND 1)*8000h
    key0=((((key1+47h) AND FFFFh)/4) XOR key0)+key2+(((key1+47h)/2) AND 1)
    halfword[addr]=halfword[addr] XOR key0, addr=addr+2
  ret
```
The MCD.\* files don't contain any encryption flag. Below are some values that
could be used to distinguish between encrypted and unencrypted MCD archives
(though that may fail in case of any other games/versions with other values):<br/>
```
  Item                    Unencrypted   Encrypted
  Parent Folder name      "TLS"         "TLS2"
  First name in MCD.DIR   "BACKTILE"    "TEST.RPS"
  First word in MCD.IMG   00000010h     074D4C8Ah
```

#### Star Wars Rebel Assault 2 (RESOURCE.\*, and nested therein)
#### BallBlazer Champions (\*.DAT, and nested therein)
The Rebel RESOURCE.\* files start with name "bigEx" or "fOFS", BallBlazer \*.DAT
start with "SFXbase" or "tpage", nested files start with whatever other names.<br/>
```
  000h N*10h File List
  ...  (4)   CRC32 on above header (Top-level only, not in Nested archives)
  ...  ..    File Data area
  ...  (..)  Huge optional padding to xx000h-byte boundary (in BallBlazer .DAT)
 File List entries in Top-level archives (with [0Ch].bit31=1):
  000h 8     Filename (zeropadded if less than 8 chars)
  008h 4     Decompressed Size (or 0=File isn't compressed)
  00Ch 4     Offset, self-relative from current List entry (plus bit31=1)
 File List entries in Nested archives (with [0Ch].bit31=0):
  000h 0Ch   Filename (zeropadded if less than 12 chars)
  00Ch 4     Offset, self-relative from current List entry (plus bit31=0)
 Last File List entry has [00h..0Bh]=zerofilled, and Offset to end of file.
```
Uncompressed Data Format (when List entry [08h]=0 or [0Ch].bit31=0):<br/>
```
  000h ..    Uncompressed Data
  ...  ..    CRC32 on above Data (Top-level only, not in Nested archives)
```
Compressed Data Format (when List entry [08h]\>0 and [0Ch].bit31=1)::<br/>
```
  000h 1     Compression Method (01h=LZ/16bit, 02h=LZ/24bit)
  001h 3     Decompressed Size (big-endian)
  004h ..    Compressed Data
  ...  ..    Zeropadding to 4-byte boundary
  ...  ..    CRC32 on above bytes (method, size, compressed data, padding)
```
[CDROM File Compression RESOURCE (Star Wars Rebel Assault 2)](cdromfileformats.md#cdrom-file-compression-resource-star-wars-rebel-assault-2)<br/>

```
 _______________________________ Entrysize=14h ________________________________
```

#### Fighting Force (MagDemo01: FGHTFRCE\\*.WAD)
```
  000h 4     Number of files                                  (big endian)
  004h N*14h File List
  ...  ..    File Data
```
File List entries:<br/>
```
  000h 0Ch   Filename ("FILENAME.EXT", zeropadded if shorter than 12 chars)
  00Ch 4     Filesize in bytes (can be odd)                   (big endian)
  010h 4     Fileoffset in bytes (increasing, 4-byte aligned) (big endian)
```

#### Parappa (MagDemo01: PARAPPA\\*.INT)
#### Um Jammer Lammy (MagDemo24: UJL\\*.INT)
```
  0000h 2000h Folder 1
  2000h ..    File Data for Folder 1
  ...   2000h Folder 2
  ...   ..    File Data for Folder 2
  ...   2000h Folder End marker (FFFFFFFFh, plus zeropadding)
```
Folder entries:<br/>
```
  0000h 4      Folder ID (increasing, 1,2,3, or FFFFFFFFh=End)
  0004h 4      Number of files (max 198h) (N)
  0008h 4      File Data Area size/800h   (S)
  000Ch 4      Zero (0)
  0010h N*14h  File List
  ...   ..     Zeropadding to 2000h
  2000h S*800h File Data Area for this folder
```
File List entries:<br/>
```
  000h 4     Filesize in bytes
  004h 10h   Filename (FILENAME.EXT, zeropadded)
```
File Offsets are always 4-byte aligned (required for Um Jammer Lammy, which
contains Filesizes that aren's multiples of 4).<br/>
Note: There can be more than one folder with same ID (ie. when having more than
198h TIM files, which won't fit into a single 2000h-byte folder).<br/>

#### Gran Turismo 1 (MagDemo10: GT\BG.DAT\\*, GT\COURSE.DAT\\*)
#### Gran Turismo 1 (MagDemo15: GT\BG.DAT\\*, GT\COURSE.DAT\\*)
#### JumpStart Wildlife Safari Field Trip (MagDemo52: DEMO\DATA.DAT\\*.DAT)
These are child archives found inside of the main GT-ARC and DATA.DAT archives.<br/>
```
  000h 4     Number of Files (eg. 26h) (usually at least 02h or higher)
  004h N*14h File List
  ...  ..    File Data area
 File List entries:
  000h 10h   Filename ("FILENAME.EXT", zeropadded if shorter)
  010h 4     Offset in bytes (increasing, 4-byte-aligned?)
```

#### Croc 2 (MagDemo22: CROC2\CROCII.DAT and CROCII.DIR)
#### Disney's The Emperor's New Groove (MagDemo39: ENG\KINGDOM.DIR+DAT)
#### Disney's Aladdin in Nasira's Revenge (MagDemo46: ALADDIN\ALADDIN.DIR+DAT)
```
 DIR:
  000h 4     Number of Entries (0Eh)
  004h N*14h File List
 DAT:
  000h ..    File Data (referenced from CROCII.DIR)
```
File List entries:<br/>
```
  000h 0Ch   Filename ("FILENAME.EXT", zeropadded if shorter)
  00Ch 4     File Size in bytes
  010h 4     File Offset in .DAT file (800h-byte aligned, increasing)
```

#### Alice in Cyberland (ALICE.PAC, and nested .PAC, .FA, .FA2 archives)
```
  000h N*14h File List
  ...  14h   Zerofilled (File List end marker)
  ...  ..    File Data area
 File List entries:
  000h 0Ch   Filename ("FILENAME.EXT", zeropadded if shorter)
  00Ch 4     Offset (increasing, 4-byte aligned)
  010h 4     Filesize in bytes (can be odd, eg. for .FA2 files)
```
PAC and FA are uncompressed, FA2 is compressed via some LZ5-variant:<br/>
[CDROM File Compression LZ5 and LZ5-variants](cdromfileformats.md#cdrom-file-compression-lz5-and-lz5-variants)<br/>

#### Interplay Sports Baseball 2000 (MagDemo22:BB2000\DATA\HOG.TOC\UNIFORMS\\*.UNI)
```
  000h N*14h  File List (3Ch*14b bytes, unused entries are zeropadded)
  4B0h ..     Data area (TIM files for player uniforms)
 File List entries:
  000h 10h    Filename ("FILENAME.EXT", zeropadded)
  010h 4      Offset (zerobased, from begin of Data area, increasing)
```

```
 _______________________________ Entrysize=18h ________________________________
```

#### Invasion from Beyond (MagDemo15: IFB\\*.CC)
```
  000h 0Ch   Fixed ID (always "KotJCo01Dir ") (always that same string)
  00Ch 4     Number of Files
  010h N*18h File List
  ...  ..    File Data area
```
File List entries:<br/>
```
  000h 10h   Filename ("FILENAME.EXT", zeropadded)
  010h 4     Offset in bytes (increasing, 1-byte or 4-byte aligned)
  014h 4     Filesize in bytes (can be odd)
```
Note: Alignment is optional: Files in IFB\HANGAR\\*.CC and IFB\MAPS\\*.CC use
4-byte aligned offsets (but may have odd filesizes). Files in IFB\INCBINS\\*.CC
don't use any alignment/padding.<br/>

#### Ghost in the Shell (MagDemo03: GITSDEMO\S01\\*.FAC)
```
  000h N*18h File List (18h-bytes each)
  ...  18h   File List end marker (zerofilled)
  ...  ..    File Data
```
File List entries:<br/>
```
  000h 1     Filename Checksum (sum of bytes at [001h..00Dh])
  001h 1     Filename Length (excluding ending zeroes) (eg. 8, 9, 10, 12)
  002h 0Ch   Filename ("FILENAME.EXT", zeropadded if less than 12 chars)
  00Eh 2     Unknown (2000h) (maybe attr and/or ending zero for filename)
  010h 4     Filesize in bytes (can be odd)
  014h 4     Offset (increasing, 4-byte aligned)
```

#### Oddworld: Abe's Exodus (MagDemo17: ABE2\\*.LVL)
#### Oddworld: Abe's Exodus (MagDemo21: ABE2\\*.LVL and nested .IDX files)
```
  000h 4     Header Size in bytes  (2800h) (can be MUCH bigger than needed)
  004h 4     Zero
  008h 4     ID "Indx"
  00Ch 4     Zero
  010h 4     Number of Files (N)   (CEh) (can be zero=empty in .IDX files)
  014h 4     Header Size/800h      (05h)
  018h 4     Zero
  01Ch 4     Zero
  020h N*18h File List
  ...  ..    Zeropadding to end of Headersize
  ...  ..    File Data area
```
File List entries (in .LVL files):<br/>
```
  000h 0Ch   Filename ("FILENAME.EXT", zeropadded if shorter)
  00Ch 4     Offset/800h
  010h 4     File Size/800h
  014h 4     File Size in bytes
```
File List entries (in .IDX files):<br/>
```
  IDX files use the same File List entry format as LVL, but the offsets
  seem to refer to an external file with corresponding name, for example:
    cdrom:\ABE2\CR.LVL\CR.IDX     ;directory info
    cdrom:\ABE2\CR.MOV            ;external data (the .MOV being a .STR video)
  XXX: That's not tested/verified, and not implemented in no$psx file viewer.
```

#### Monkey Hero (MagDemo17: MONKEY\BIGFILE.PSX and nested .PSX files)
```
  000h 4     Unknown              (6)
  004h 4     Total Filesize       (1403800h)
  008h 2     Unknown, Alignment?  (800h)
  00Ah 2     Number of Files, excluding zerofilled File List entries (ACh)
  00Ch 4     Header Size          (1800h)
  010h 4     Unknown, Entrysize?  (18h)
  014h 4     Unknown, Entrysize?  (18h)
  018h N*18h File List (can contain unused zerofilled entries here and there!)
  ...  ..    File Data area
```
File List entries:<br/>
```
  000h 10h   Filename ("FILENAME.EXT", zeropadded)
  010h 4     File Offset in bytes (800h-byte aligned, unusorted/not increasing)
  014h 4     File Size in bytes
```

#### NHL Faceoff '99 (MagDemo17: FO99\\*.KGB and nested \*.PRM \*.TMP \*.ZAM)
#### NHL Faceoff 2000 (MagDemo28: FO2000\\*.KGB, Z.CAT, and nested \*.PRM and \*.TMP)
```
  000h 4     ID "KGB",00h
  004h 4     Number of Files         (N)
  008h (4)   Number of Files negated (-N)   ;<-- optional, not in LITESHOW.KGB
  ...  N*18h File List
  ...  (..)  CBh-padding to alignment boundary (only if align=800h)
  ...  ..    File Data area
```
File List entries:<br/>
```
  000h 10h   Filename ("FILENAME.EXT", terminated by 00h, padded with CDh)
  010h 4     File Size in bytes
  014h 4     File Offset (800h-byte or 1/4-byte? aligned)
```

#### Syphon Filter 1 (MagDemo18: SYPHON\SUBWAY.FOG) (4Mbyte, namelen=10h)
```
  000h 4     Unknown (80000001h)
  004h 4     Offset/800h to Final Padding area
  008h 8     Zerofilled
  010h N*18h File List
  ...  (..)  CDh-padding to 800h-byte alignment boundary
  ...  ..    File Data area
  ...  800h  Some text string talking about "last-sector bug"
  ...  40BEh Final Padding area (CDh-filled)
```
File List entries:<br/>
```
  000h 10h   Filename ("FILENAME.EXT", terminated by 00h, padded with CDh)
  010h 4     File Offset/800h (increasing)
  014h 4     File Size/800h
```
This is almost same as the newer v2 format in Syphon Filter 2 (see there for
details).<br/>

#### Centipede (MagDemo23: ARTFILES\\*.ART)
```
  000h 0Fh   ID ("Art", zeropadded)             ;\
  00Fh 1     Type or so ("?")                   ; sorts of File List entry
  010h 4     Number of entries plus 1 (N+1)     ; for root folder
  014h 4     Total Size in bytes (can be odd)   ;/
  018h N*18h File List
  ...  ...   File Data area
 File List entries:
  000h 0Fh   Filename ("FILENAME", zeropadded)
  00Fh 1     Type/extension or so ("X" or "D")
  010h 4     File Offset (unaligned, increasing)
  014h 4     File Size in bytes (can be odd)
```
Note: C0L7.ART includes zerofilled 18h-bytes as last File List entry, BONU.ART
doesn't have any such zerofilled entry.<br/>
Unknown if this can have child folders (maybe in similar form as the root
folder entry).<br/>

#### Sheep Raider (MagDemo52: SDWDEMO\\*.SDW)
#### Sheep Raider (MagDemo54: SDWDEMO\\*.SDW)
```
  000h 4     Unknown (301h)
  004h 4     Zero (0)
  008h 4     Number of files (N)
  00Ch N*18h File List
  ...  ..    Zeropadding to 800h-byte boundary
  ...  ..    File Data area
 File List entries:
  000h 4     Offset (800h-byte aligned, increasing)
  004h 4     Filesize in bytes
  008h 1     Unknown (01h)
  009h 0Fh   Filename ("FILENAME.EXT",00h, plus garbage padding)
```
The SDW archive contains malformed 200h\*1A4h pixel TIMs.<br/>
```
  Texsize is 6900Eh, but should be 6900Ch = 200h*1A4h*2+0Ch
  Filesize is 6A000h, but should be 69014h = 200h*1A4h*2+14h
```

#### Wing Commander III (\*.LIB)
```
  000h 2     Number of Files (C9h)
  002h N*18h File List
  ...  (..)  Padding to 800h-byte boundary (if any, eg. in MOVIES.LIB)
  ...  ..    File data area (800h-byte aligned, or unaligned)
 File List entries:
  000h 4     Filesize in bytes
  004h 4     Offset (increasing, 800h-byte aligned, or unaligned)
  008h 10h   Filename ("filename.ext", zeropadded)
```

#### Largo Winch - Commando SAR (LEVELS\\*.DCF)
```
  000h 4     ID "DCAT"
  004h 4     Number of Entries
  008h N*18h File List
  ...  ..    Zerofilled (padding to 800h-byte boundary)
  ...  ..    File Data area
 File List entries:
  000h 10h   Filename ("FILENAME.EXT", terminated by 00h, plus garbage padding)
  010h 4     Filesize in bytes
  014h 4     Offset (increasing, 800h-byte aligned)
```

#### Policenauts (NAUTS\\*.DPK)
```
  000h 4     ID "FRID"
  004h 4     Always E0000000h
  008h 4     Always 800h (...maybe alignment)
  00Ch 4     Number of Entries (N)
  010h 4     Header Size (N*18h+20h, plus padding to 800h-byte boundary)
  014h 4     Always 18h (...maybe entry size)
  018h 8     Zerofilled
  020h N*18h File List
  ...  ..    Zerofilled (padding to 800h-byte boundary)
  ...  ..    File Data area
 File List entries:
  000h 0Ch   Filename ("FILENAME.EXT", zeropadded if shorter)
  00Ch 4     Offset (increasing, 800h-byte aligned)
  010h 4     Filesize in bytes
  014h 4     Unknown (checksum? random?)
```

#### Actua Ice Hockey 2 (Best Sports Games Ever (demo), AH2\GAMEDATA\\*.MAD)
```
  000h N*18h File List
  ...  ..    File Data area (directly after File List, without end-code)
 Note: There is no file-list end-marker (instead, the Offset in 1st File
       entry does imply the end of File List).
 File List entries:
  000h 10h  Filename ("FILENAME.EXT", zeropadded)
  010h 4    Offset (increasing, 4-byte aligned, or unaligned for TXT files)
  014h 4    Filesize in bytes (or weird nonsense in SFX.MAD)
```
There are several oddities in demo version (unknown if that's in retail, too):<br/>
```
 SFX.MAD has nonsense Filesize entries (eg. 164h for a 15150h-byte file).
 FACES.MAD contains only one TIM file... but as 3Mbyte junk appended?
 RINKS.MAD and TEAMS.MAD start with 0Dh,0Ah,1Ah followed by 4Mbyte junk.
 MISCFILE.MAD contains several nested .mad files.
 MISCFILE.MAD\panfont.mad\*.txt --> starts with FF,FE --> that's 16bit Unicode?
```

#### Muppet Monster Adventure (MagDemo37: MMA\GAMEDATA+WORLDS\*\\*.INF+WAD)
```
 INF:
  000h N*18h File List
 WAD:
  000h ..    File Data area
```
File List entries:<br/>
```
  000h 4     File Offset/800h in .WAD file
  004h 4     File Size in bytes
  008h 10h   Filename ("FILENAME.EXT", zeropadded)
```

#### Army Men Air Attack 2 (MagDemo40: AMAA2\\*.PCK)
```
  000h 4     Number of entries (N)
  004h N*18h File List
  ...  ..    Zeropadding to 800h-byte boundary
  ...  ..    File Data area
 File List entries:
  000h 10h   Filename ("FILENAME.EXT", zeropadded)
  010h 4     Fileoffset (800h-byte aligned, increasing)
  014h 4     Filesize in bytes
```

#### Mort the Chicken (MagDemo41: MORT\\*.PPF and .TPF)
```
  000h 2     Type (31h=TPF with TIMs, 32=PPF with PMDs)
  002h 2     Number of entries (N) (can be 0=None, eg. STAGE*\MORT.PPF)
  004h 4     File List Size (N*18h)
  008h 4     Header Size (always 14h)
  00Ch 4     Data area Size (Filesize-14h-N*18h)
  010h 4     Data area Offset (14h+N*18h)
  014h N*18h File List
  ...  ..    File Data area
 File List entries:
  000h 10h   Filename ("FILENAME.EXT", zeropadded)
  010h 4     Filesize in bytes
  014h 4     Fileoffset (from begin of Data area, increasing)
```

#### Hot Wheels Extreme Racing (MagDemo52: US\_01293\VEHICLES\\*.CAB)
```
  000h 4     ID "BACR" (aka RCAB backwards)
  004h 4     Number of entries (N)
  008h N*18h File List
  ...  ..    File Data area
 File List entries:
  000h 10h   Filename ("FILENAME.EXT", zeropadded)
  020h 4     Offset (from begin of Data area, increasing, 4-byte aligned)
  024h 4     Filesize in bytes (can be odd)
```

```
 _______________________________ Entrysize=19h ________________________________
```

#### WAD Format (Wipeout 2097)
PSX Wipeout 2097, cdrom:\WIPEOUT2\SOUND\SAMPLES.WAD:\\*.vag<br/>
PSX Wipeout 2097, cdrom:\WIPEOUT2\TRACK\*\TRACK.WAD:\\*.\*<br/>
PSX Wipeout 3 (MagDemo25: WIPEOUT3\\*)<br/>
```
  000h 2     Number of files
  002h N*19h Directory Entries for all files
  ...  ..    Data for all files (without any alignment, in same order as above)
```
Directory Entries<br/>
```
  000h 10h Filename (ASCII, can be lowercase), terminated by 00h, plus garbage
  010h 4   Filesize in bytes  ;\maybe compressed/uncompressed, or rounded,
  014h 4   Filesize in bytes  ;/always both same
  018h 1   Unknown (always 00h)
```
The filesize entry implies offset to next file.<br/>

```
 _______________________________ Entrysize=1Ch ________________________________
```

#### Command & Conquer, Red Alert (MagDemo05: RA\\*) FAT/MIX/XA
```
  000h 4     Number of entries with location 0=MIX (M=65h)
  000h 4     Number of entries with location 1=XA  (X=1)
  008h M*1Ch File List for location 0=MIX
  ...  X*1Ch File List for location 1=XA
```
File List entries:<br/>
```
  000h 10h   Filename (terminated by 00h, padded with garbage)
  010h 4     Offset/800h in DATA.MIX or Offset/930h DATA.XA file (increasing)
  014h 4     Filesize in bytes
  018h 4     File Location (0=DATA.MIX, 1=DATA.XA)
```

#### Syphon Filter 2 (MagDemo30: SYPHON\TRAIN.FOG) (2.8Mbyte, namelen=14h)
```
  000h 4     Unknown (80000001h)
  004h 4     Offset/800h to Final Padding area
  008h 8     Zerofilled
  010h N*1Ch File List
  ...  (..)  CDh-padding to 800h-byte alignment boundary
  ...  ..    File Data area
  ...  3394h Final Padding area (CDh-filled)
```
File List entries:<br/>
```
  000h 14h   Filename ("FILENAME.EXT", terminated by 00h, padded with CDh)
  014h 4     File Offset/800h (increasing)
  018h 4     File Size/800h
```
This is almost same as the older v1 format in Syphon Filter 1:<br/>
```
  v1 (Syphon Filter 1) has filename_len=10h (and filelist_entrysize=18h)
  v2 (Syphon Filter 2) has filename_len=14h (and filelist_entrysize=1Ch)
```
To detect the version: Count the length of the "ASCII chars + 00h byte + CDh
padding bytes" at offset 10h.<br/>
Note: The FOG archive in Syphon Filter 2 demo version does contain some empty
dummy files (with intact filename, but with offset=0 and size=0).<br/>

```
 _______________________________ Entrysize=20h ________________________________
```

#### Colony Wars (MagDemo02: CWARS\GAME.RSC)
#### Colony Wars Venegance (MagDemo14: CWV\GAME.RSC, 8Mbyte)
```
  000h 4     Number of Files
  004h N*20h File List
  ...  10h   File List End: Name    (zerofilled)
  ...  4     File List End: Offset  (total filesize, aka end of last file)
  ...  0Ch   File List End: Padding (zerofilled)
  ...  ..    File Data area
```
File List entries:<br/>
```
  000h 10h   Filename ("FILENAME.EXT", terminated by 00h, padded with garbage)
  010h 4     File Offset in bytes (increasing, 4-byte aligned)
  014h 0Ch   Padding (garbage) (usually 800F68A0h,800F68A0h,800F68A0h)
```
Note: Colony Wars Red Sun does also have a GAME.RSC file (but in different
format, with folder structure).<br/>

#### WarGames (MagDemo14: WARGAMES\\*.DAT)
```
  000h 4     Number of Files (1C3h)
  004h N*20h File List
  ...  ..    Zeropadding to 800h-byte boundary
  ...  ..    File Data area
```
File List entries:<br/>
```
  000h 10h   Filename ("FILENAME.EXT", zeropadded, sorted alphabetically)
  010h 4     File Offset/800h (unsorted, not increasing)
  014h 4     File Size in bytes
  018h 4     File Size/800h
  01Ch 4     Zero
```

#### Running Wild (MagDemo15: RUNWILD\\*.BIN)
```
  000h N*20h File List
  ...  4     File List End Offset/800h (end of last file)
  ...  4     File List End Size (zero)
  ...  18h   File List End Name (zerofilled)
  ...  ..    Padding to 800h-byte boundary (each 20h-byte: 01h, and 1Fh zeroes)
  ...  ..    File Data
```
File List entries:<br/>
```
  000h 4     Offset/800h (increasing)
  004h 4     Filesize in bytes
  008h 18h   Filename ("FILENAME.EXT" or ":NAME" or ":NAME:NAME", zeropadded)
```
Files with extension .z or .Z are compressed:<br/>
[CDROM File Compression Z (Running Wild)](cdromfileformats.md#cdrom-file-compression-z-running-wild)<br/>

#### Test Drive Off-Road 3 (MagDemo27: TDOR3\TDOR3.DAT)
About same as the other Test Drive games, but with shorter filenames.<br/>
```
  000h N*20h  File List (1920h bytes used; with padding: 5800h bytes in total)
  ...  ..     Zeropadding to Headersize (5800h)
  ...  ..     File Data area
 File List entries:
  000h 18h    Filename ("FILENAME.EXT" or "PATH\FILENAME.EXT", zeropadded)
  018h 4      Filesize in bytes
  01Ch 4      File (Offset-Headersize)/800h
```
TDOR3.DAT contains DOT1 child archives and many RNC compressed files: --\>
CDROM File Compression RNC (Rob Northen Compression)<br/>

#### Tiny Tank (MagDemo23: TINYTANK\\*.DSK)
```
  000h 4     ID ("TDSK")                                      ;\
  004h 4     Number of Files (1Bh)                            ; Directory
  008h N*20h File List                                        ;/
  ...  4     1st File Size (same as Size entry in File List)  ;\File Data area
  ...  ..    1st File Data                                    ; (each file os
  ...  4     2nd File Size (same as Size entry in File List)  ; preceeded by
  ...  ..    2nd File Data                                    ; a size entry)
  ...  ..    etc.                                             ;/
 File List entries:
  000h 10h   Filename ("FILENAME.EXT", zeropadded)
  010h 4     File Size in bytes
  014h 4     Unknown (35xxxxxxh..372xxxxxh)
  018h 4     Unknown (3724xxxxh) (Timestamp maybe?)
  01Ch 4     File Offset in bytes (increasing, 4-byte aligned)
```
Note: The File Offset points to a 32bit value containing a copy of the
Filesize, and the actual file starts at Offset+4.<br/>

#### MAG 3 (MagDemo26: MAG3\MAG3.DAT, 7Mbyte)
```
  000h N*20h  File List (B60h bytes)
  ...  ..     Zeropadding to 800h-byte boundary
  ...  ..     File Data area (files are AAh-padded to 800h-byte boundary)
 File List entries:
  000h 4      Filesize in bytes
  004h 2      File Offset/800h (16bit) (increasing)
  006h 1Ah    Filename ("FILENAME.EXT" or "PATH\FILENAME.EXT", zeropadded)
```

#### Play with the Teletubbies (MagDemo35: TTUBBIES\\*.RES)
```
  000h 2     Zero (0000h)
  002h 2     Number of Files (N)
  004h 4     Data Base (N*20h+10h)
  008h 4     Unknown (20h)  ;-maybe File List entry size?
  00Ch 2     Unknown (10h)  ;\maybe filename length and/or header size?
  00Eh 2     Unknown (10h)  ;/
  010h N*20h File List
  ...  ..    File Data area
```
File List entries:<br/>
```
  000h 4     Zero
  004h 4     File Offset (increasing, 4-byte aligned, relative to Data Base)
  008h 4     File Size in bytes (can be odd)
  00Ch 4     Zero
  010h 10h   Filename ("FILENAME.EXT", zeropadded)
```

#### Mat Hoffman's Pro BMX (old demo) (MagDemo39: BMX\FE.WAD+STR) (uncompressed)
#### Mat Hoffman's Pro BMX (new demo) (MagDemo48: MHPB\FE.WAD+STR) (compressed)
```
 WAD:
  000h N*20h File List
 STR:
  000h ..    File Data (MagDemo39: 4.5Mbyte, MagDemo48: compressed/2.8Mbyte)
 File List entries:
  000h 14h   Filename ("FILENAME.EXT", zeropadded)
  014h 4     Offset in bytes, 4-byte aligned, in STR file
  018h 4     Filesize, compressed (always rounded to multiple of 4 bytes)
  01Ch 4     Filesize, decompressed (zero when not compressed)
```
The decompressor is using an Inflate variant with slightly customized block
headers:<br/>
```
  - end flag is processed immediately (instead of after the block)
  - blocktype is only 1bit wide (instead of 2bit)
  - stored blocks have plain 16bit len (without additional 16bit inverse len)
```
Everything else is same as described here:<br/>
[CDROM File Compression ZIP/GZIP/ZLIB (Inflate/Deflate)](cdromfileformats.md#cdrom-file-compression-zipgzipzlib-inflatedeflate)<br/>
Instead of "tinf\_uncompress", use the function below:<br/>
```
 bmx_tinf_style_uncompress(dst,src)
  tinf_init()                   ;init constants (needed to be done only once)
 @@lop:
  if tinf_getbit()=0 then goto @@done   ;end flag, 1bit
  if tinf_getbit()=0 then               ;blocktype, 1bit
    tinf_align_src_to_byte_boundary()
    len=LittleEndian16bit[src], src=src+2   ;get len (without inverse len)
    for i=0 to len-1, [dst]=[src], dst=dst+1, src=src+1, next i   ;uncompressed
  else
    tinf_decode_dynamic_trees(), tinf_inflate_compressed_block()  ;compressed
  gpto @@lop
 @@done:
  ret
```
Note: Apart from the MHPB\FE.WAD archive, many MHPB\\*.BIN files seem to be also
compressed (unknown if that's the same compression method; and, if so, they
would lack decompressed size info).<br/>

```
 _______________________________ Entrysize=28h ________________________________
```

#### Demo Menu, PlayStation Magazine Demo Disc 03-54, MENU.FF
Used on most PlayStation Magazine Demo Discs (Disc 03-54, except Disc 01-02)<br/>
Used on PlayStation Underground 3.1 (and maybe other issues)<br/>
Used on Interactive CD Sampler Disc Volume 10 (maybe others, but not Vol 4,5)<br/>
```
  000h 4     Number of entries (eg. 20h or 28h)
  004h N*28h File List
  ...  ..    Garbage padding to 800h-byte boundary
  ...  ..    File Data
  ...  ..    Huge zeropadding to 200000h or 2EE000h (2048Kbyte or 3000Kbyte)
```
File List entries:<br/>
```
  000h 20h   Filename (terminated by 00h, padded with... looks like garbage)
  020h 4     Size/800h
  024h 4     Offset/800h (increasing)
```
Contains .BS, .TIM, .TXT, .VH, .VB files. The size seems to be always(?)
2048Kbytes, 2992Kbytes, 2000Kbytes, or 3000Kbytes (often using only the first
quarter, and having the remaining bytes zeropadded).<br/>

#### Test Drive 4 (MagDemo03: TD4.DAT) (headersize=2000h, used=0...h)
#### Test Drive 5 (MagDemo13: TD5.DAT) (headersize=3000h, used=1EF8h)
#### Demolition Racer (MagDemo27: DR\DD.DAT) (headersize=5000h, used=2328h)
This is used by several games, with different Headersizes (2000h or 3000h or
5000h), with Offsets relative to the Headersize. To detect the Headersize, skip
used entries, skip following zeropadding, then round-down to 800h-byte boundary
(in case the 1st file contains some leading zeroes).<br/>
```
  000h N*28h File List (less than 0C00h bytes used in TD4 demo)
  ...   ..   Zeropadding to Headersize (2000h or 3000h or 5000h)
  ...   ..   File Data
```
File List entries:<br/>
```
  000h 20h   Filename ("PATH\FILENAME.EXT", zeropadded)
  020h 4     Size in bytes
  024h 4     (Offset-Headersize)/800h (increasing)
```
TD5.DAT and DD.DAT contain DOT1 child archives and many RNC compressed files:<br/>
[CDROM File Compression RNC (Rob Northen Compression)](cdromfileformats.md#cdrom-file-compression-rnc-rob-northen-compression)<br/>

#### Gekido (MagDemo31: GEKIDO\GLOBAL.CD)
```
  0000h N*28h File List
  21C0h ...   Unknown random gibberish? (23h,E8h,0Ch,1Dh,79h,C5h,24h,...)
  4000h ...   File Data area
```
File List entries:<br/>
```
  000h 1Ch   Filename ("\PATH\FILENAME.EXT;0", zeropadded)
  01Ch 4     Filesize in bytes
  020h 4     Fileoffset in bytes (4000h and up, increasing)
  024h 4     Filechecksum (32bit sum of all bytes in the file)
```
There is no "number of files" entry, and no "file list end marker" (though the
"random gibberish" might serve as end marker, as long it doesn't start with "\"
backslash).<br/>

#### Team Buddies (MagDemo37: BUDDIES\BUDDIES.DAT\\* and nested \*.BND files)
```
  000h 4     ID "BIND"
  004h 4     Number of files (N)
  008h N*28h File List
  ...  ..    File Data area
```
File List entries:<br/>
```
  000h 20h   Filename ("\FILENAME.EXT", zeropadded)
  020h 4     File Offset (increasing, 4-byte aligned)     ;\see note
  024h 4     File Size in bytes (always a multiple of 4)  ;/
```
Note: There is a 4-byte gap between most files, that appears to be caused by
weird/bugged alignment handling done as so:<br/>
```
  size=((filesize+3) AND not 3)       ;size entry for curr file (plus 3)
  offs=((filesize+4) AND not 3)+offs  ;offs entry for next file (plus 4 !!!)
```
Namely, odd filesizes (eg. for TXT files in BUDDIES.DAT\00D2h..00D7h) are
forcefully rounded-up to 4 bytes boundary. If that rounding has occurred then
there is no additional 4-byte gap (but the 4-byte gap will appear if the
original filesize was already 4-byte aligned).<br/>

#### JumpStart Wildlife Safari Field Trip (MagDemo52: DEMO\DATA.DAT)
```
  000h 4     Number of entries (N)
  004h 4     Number of entries (same as above)
  008h 4     Number of entries (same as above)
  00Ch 4     Number of entries (same as above)
  010h N*28  File List
  ...  ..    Zeropadding to 800h-byte boundary
  ...  ..    File Data area
 File List entries:
  000h 20h   Filename ("\PATH\FILENAME.EXT", zeropadded)
  020h 4     Offset/800h, from begin of Data area (increasing)
  024h 4     Filesize in bytes
```

```
 _______________________________ Entrysize=34h ________________________________
```

#### Army Men: Air Attack (MagDemo28: AMAA\PAK\\*.PAK)
```
  000h 4      Number of Files
  004h N*34h  File List
  ...  ..     Zeropadding to 4000h
  4000h ..    File Data area
 File List entries:
  000h 10h    Filename ("FILENAME.EXT", zeropadded)
  010h 4      Filesize in bytes  ;\always both same, always
  014h 4      Filesize in bytes  ;/both multiple of 800h
  018h 4      Zero
  01Ch 4      Type    (07h..1Ah)
  020h 4      Subtype (00h..01h)
  024h 10h    Zero
```
The used Type.Subtype values are:<br/>
```
  07h.0   .TIM (*.TIM)
  07h.01h .TIM (HUD_*.TIM)
  08h.0   .TIM (PSTART.TIM)
  09h.0   .TIM (FONT.TIM)
  0Ah.0   .SFX
  0Eh.0   .MBL
  10h.0   .ATR
  11h.0   .RLC
  13h.0   .AST
  15h.0   .SCD
  16h.0   .TXT (PAUSED.TXT)
  17h.0   .TXT (OBJECT*.TXT)
  18h.0   .BIN
  1Ah.0   Misc (.3DO=TIM, .V=TXT, and TERRAIN.CLP .HI .LIT .MAP .PAT .POB .TER)
```

```
 _______________________________ Entrysize=40h ________________________________
```

#### Ninja (MagDemo13: NINJA\CUTSEQ\\*.WAD and NINJA\WADS\\*.WAD)
```
  000h 4     Number of Files (N)
  004h 4     Size of File Data area (SIZ) (total filesize-8-N*40h)
  008h N*40h File List
  ...  SIZ   File Data area
 File List entries:
  000h 4     Filesize in bytes
  004h 4     Fileoffset in bytes (zerobased, from begin of File Data area)
  008h 38h   Filename, zeropadded
```
#### You Don't Know Jack (MagDemo23: YDKJ\RES\\*.GLU)
#### You Don't Know Jack 2 (MagDemo41: YDKJV2\\*\\*.GLU)
```
  000h 4     ID ("GLUE")
  004h 4     Unknown (always 400h)
  008h 4     Number of Files (N)
  00Ch 4     Header Size (40h+N*40h)
  010h 30h   Zerofilled
  040h N*40h File List
  ...  ..    Garbage padding to alignment boundary
  ...  ..    File Data area
 File List entries:
  000h 20h   Filename ("FILENAME.EXT", zeropadded)
  020h 4     File Offset in bytes (increasing, 800h-byte aligned)
  024h 4     File Size in bytes
  028h 2     File ID Number 1 (eg. 1-71 for C01.GLU-C71.GLU)
  02Ah 2     Unknown (random, checksum, ?)
  02Ch 4     File ID Number 2 (eg. increasing: 1, 2, 3)
  030h 10h   Zerofilled
```
Most .GLU files are 800h-byte aligned (except SHORTY\\*.GLU and THREEWAY\\*GLU
which use 4-byte alignment).<br/>
The files do start on alignment boundaries, but there is no alignment padding
after end of last file.<br/>

```
 _______________________________ Entrysize=60h ________________________________
```

#### Army Men Air Attack 2 (MagDemo40: AMAA2\\*.PCK\\*.PAK)
```
  000h 4     Number of entries (N)
  010h N*60h File List
  ...  ..    Zeropadding to 2000h
  2000h ..   File Data area
 File List entries:
  000h 4     Timestamp? (BFxxxxh..C0xxxxh) (or zero, in first file)
  004h 4     Unknown (always 421C91h)
  008h 4     Unknown (200h or 60200h)
  00Ch 4     Filesize (uncompressed)
  010h 4     Filesize (compressed, or 0 when not compressed)
  014h 4     File Checksum (sum of all bytes in uncompressed file data)
  018h 4     Unknown (random 32bit value?)
  01Ch 10h   Filename ("FILENAME.EXT", zeropadded)
  02Ch 4     Zerofilled
  030h 4     Unknown (0 or 1 or 8)
  034h 4     File Type (see below)
  038h 8     Zerofilled
  040h 4     Offset MSBs (Fileoffset-2000h)/800h  ;\increasing, 4-byte aligned
  044h 4     Offset LSBs (Fileoffset AND 7FFh)    ;/(or zero when filesize=0)
  048h 18h   Zerofilled
```
File Type values are 07h=TIM, 0Ah=SFX, 0Eh=MBL, 10h=ATR, 13h=AST, 15h=SCD,
19h=VTB, 1Bh=DCS, 1Dh=DSS, 1Eh=STR, 1Fh=DSM, 20h=FNT, 21h=TER, 25h=PMH,
26h=Misc.<br/>
Most of the files are SCRATCH compressed:<br/>
[CDROM File Compression LZ5 and LZ5-variants](cdromfileformats.md#cdrom-file-compression-lz5-and-lz5-variants)<br/>
There are also several uncompressed files (eg. VERSION.V, \*.SFX, and many of
the TERRAIN.\* files).<br/>

```
 _______________________________ Entrysize=90h ________________________________
```

#### Grind Session (MagDemo33: GRIND\SLIP.GRV)
#### Grind Session (MagDemo36: GRIND\SLIP.GRV)
#### Grind Session (MagDemo42: GRIND\SLIP.GRV)
#### Grind Session (MagDemo45: GRIND\SLIP.GRV)
```
  000h 4     ID (A69AA69Ah)
  004h 4     Number of files (N)
  008h N*90h File List
  ...  ..    File Data area
 File List entries:
  000h 80h   Filename ("DATA\FILENAME.EXT",00h, plus CDh-padding)
  080h 4     File Offset in bytes (increasing, 4-byte aligned)
  084h 4     File Size in bytes
  088h 8     Unknown (random/checksum?)
```

```
 _____________________________ Variable Entrysize _____________________________
```

#### HED/WAD
```
  Used by Spider-Man (MagDemo31,40: SPIDEY\CD.HED and CD.WAD)
  Used by Spider-Man 2 (MagDemo52: SPIDEY\CD.HED and CD.WAD)
  Used by Tony Hawk's Pro Skater (MagDemo22: PROSKATE\CD.HED and CD.WAD)
  Used by Apocalypse (MagDemo16: APOC\CD.HED and CD.WAD)       ;with PADBUG
  Used by MDK (Jampack Vol. 1: MDK\CD.HED and CD.WAD)          ;without ENDCODE
  Used by Mat Hoffman's Pro BMX (old demo) (MagDemo39: BMX\BMXCD.HED+WAD)
```
Format of the CD.HED file:<br/>
```
  000h ..  File Entries (see below)
  ...  (1) End code (FFh) (if any, not present in MDK)
```
File Entry format:<br/>
```
  000h ..  Filename (ASCII, terminated by 00h, zeropadded to 4-byte boundary)
  ...  4   Offset in CD.WAD (in bytes, usually 800h-byte aligned)
  ...  4   Filesize (in bytes)
```
PADBUG: Apocalypse does append 1..800h bytes alignment padding (instead of
1..7FFh or 0 bytes).<br/>

#### Dance UK (DATA.PAK)
```
  000h 4      Number of Files (N) (1ADh)
  004h 4      Unknown (7) (maybe HeaderSize/800h, same as first Offset/800h ?)
  008h 4      Unknown (1430h = 14h+N*0Ch, same as first Name pointer)
  00Ch 4      Unknown (1430h = 14h+N*0Ch, same as first Name pointer)
  010h 4      Unknown (1430h = 14h+N*0Ch, same as first Name pointer)
  014h N*4    Name List (pointers to name strings, 1430h and up)  6B4h bytes
  ...  N*4    Size List (filesize in bytes)                       6B4h bytes
  ...  N*4    Offset List (Offset/800h)                           6B4h bytes
  ...  N*var  Name Strings (ASCII strings, "folder\filename.ext",00h)
  ...  ..     Zerofilled (padding to 800h-byte boundary)
  ...  ..     File Data area
```

#### Kula Quest / Kula World / Roll Away (\*.PAK)
```
  000h 4     Number of Files (N)
  004h N*8   File List (2x32bit entries: Offset, Size) (unaligned, can be odd)
  ...  N*4   File Name Offsets
  ...  N*var File Name Strings ("FILE NN",0Ah,00h)
  ...  ..    Garbage-padding to 4-byte boundary
  ...  (4)   Optional extra garbage? ("MON " in ATLANTFI.PAK, MARSFI.PAK, etc.)
  ...  ..    File Data area (ZLIB compressed, starting with big-endian 789Ch)
```
[CDROM File Compression ZIP/GZIP/ZLIB (Inflate/Deflate)](cdromfileformats.md#cdrom-file-compression-zipgzipzlib-inflatedeflate)<br/>

#### Largo Winch - Commando SAR (NTEXTURE\\*.GRP and LEVELS\\*.DCF\\*.CAT and \*.GRP)
```
  000h 4     ID (12h,34h,56h,78h) (aka 12345678h in big endian)
  004h 4     Header Size (offset to File Data area)
  008h 4     Number of Entries (can be 0=None, eg. LEVELS\LARGO07.DCF\Z16.CAT)
  00Ch N*var Name List (Filenames in form "FILENAME.EXT",00h)
  ...  ..    Zeropadding to 4-byte boundary
  ...  N*4   Size List (Filesizes in bytes)
  ...  ..    File Data area
```

#### Jackie Chan Stuntmaster (RTARGET\GAME.GCF and LEV\*.LCF)
```
  000h 4     Number of files (N) (3..EBh)                 (big-endian)
  004h N*Var File List (list size is implied in first file offset)
  ...  ..    Zeropadding to 800h-byte boundary
  ...  ..    File Data area
 File List entries:
  000h 4     File Type (ascii, .LLN .TXI .TPG .RCI .RCP .WDB .PCI .PCP .BLK)
  004h 4     File Size (can be odd)                       (big-endian)
  008h 4     File Offset (increasing, 800h-byte aligned)  (big-endian)
  00Ch 4     Extra Size (0 or 4 or 8)                     (big-endian)
  010h ..    Extra Data (if any) (32bit number, or "TEXTURES")
```

#### Syphon Filter 1 (MagDemo18: SYPHON\\*.HOG, SYPHON\SUBWAY.FOG\\*.HOG,SLF.RFF)
#### Syphon Filter 2 (MagDemo30: SYPHON\\*.HOG, SYPHON\TRAIN.FOG\\*.HOG,SLF.RFF)
```
  000h 4     Timestamp? (36xxxxxxh=v1?, 38xxxxxxh=v2?, other=SLF.RFF)
  004h 4     Number of Files          (N)
  008h 4     Base for Offset List  (always 14h)
  00Ch 4     Base for String Table (v1=N*4+14h, or v2=N*4+18h)
  010h 4     Base for File Data (end of String Table plus align 4/800h/920h)
  014h N*4   Offsets to File(s) (increasing, first=0, relative to above [010h])
  ... (4)    v2 only: End Offset for Last File (HOG filesize minus [010h])
  ...  ..    String Table (filename list in form of "FILENAME.EXT",00h)
  ...  ..    Zeropadding to 4-byte or 800h-byte boundary
  ...  ..    File Data area
```
There are two versions: Syphon Filter 1 (v1) and Syphon Filter 2 (v2):<br/>
```
  v1 has [0Ch]=N*4+14h (without end-of-last-file entry; use end=total_size)
  v2 has [0Ch]=N*4+18h (and does have end-of-last-file entry)
  v1 has STR files in ISO filesystem (not in HOG archives)
  v2 has STR files in MOVIES.HOG (with [10h]=920h and [14h and up]=sectors)
```
Normally, the following is common for v1/v2:<br/>
```
  v1/v2 has [10h]=data base, aligned to 4 or 800h
  v1/v2 has [14h and up] in BYTE-offsets, relative to base=[10h]
  v1/v2 uses HOG format in .HOG files also in SLF.RFF
  v1/v2 has further .RFF files (but that aren't in HOG format)
```
There are several inconsistent special cases for some v2 files:<br/>
```
  v2 MOVIE.HOG has [10h]=920h (which is meant to mean base="after 1st sector")
  v2 MOVIE.HOG has [14h and up] in SECTOR-units, with base="after 1st sector"
  v2 SLF.RFF does contain two HOG archives badged together (plus final padding)
  v2 has some empty 0-byte .HOG files (at least so in demo version)
```
Danger: The special value 920h means that headersize is one 800h-byte sector
(whereas 920h is dangerously close to REAL headersize, eg. v1 PCHAN.HOG has
headersize=908h which means one 800h-byte sector plus 108h bytes) (the 920h
thing should occur only in v2 though, since v1 has STR files stored in ISO
filesystem instead of in HOG archives).<br/>

#### Electronic Arts 32bit BIGF archives
```
  000h 4   ID "BIGF" (normal case, all big-endian, 4-byte aligned)     ;\
           ID "BIGH" (with [04h]=little-endian instead big-endian)     ;
           ID "BIG4" (with 40h-byte alignment padding instead 4-byte)  ;
  004h 4   Sum of Header+Filesizes (excluding Padding's!) (big-endian) ; Header
  008h 4   Number of entries (N)                  ;11h    (big-endian) ;
  00Ch 4   Size of Header (including File List)   ;11Fh   (big-endian) ;
  010h ..  File List                                                   ;/
  ...  ..  Padding to 1/4/8-byte boundary (optional, before each file) ;\Data   ...  ..  File Data                                                   ;/
```
File List entries (with variable length names, entries aren't 4-byte aligned):<br/>
```
  000h 4   Offset in bytes (increasing, often 4/8-byte aligned)    (big-endian)
  004h 4   Size in bytes (can be odd, but often rounded to 4-byte) (big-endian)
  008h ..  Filename (ASCII, terminated by 00h) ;variable length
  Note: Filenames can be empty ("",00h) (eg. in WCWDEMO\ZSOUND.BIG)
```
Used by PGA Tour 96, 97, 98 (\*.VIV)<br/>
Used by FIFA - Road to World Cup 98 (MOP\*.BK\*, Z4TBLS.BIG\\*.t, ZMO\*.BIG\\*.viv)<br/>
Used by Fifa 2000 (Best Sports demo: FIFADEMO\\*.BIG, \*.SBK, and nested .viv)<br/>
Used by Need for Speed 3 Hot Pursuit (\*.VIV)<br/>
Used by WCW Mayhem (MagDemo28: WCWDEMO\\*.BIG) (odd filesizes & nameless
files)<br/>
This is reportedly also used for various other Electronic Arts games for PC,
PSX, and PS2 (often with extension \*.BIG, \*.VIV).<br/>
Reportedly also "BIGH" and "BIG4" exist:<br/>
```
  http://wiki.xentax.com/index.php/EA_BIG_BIGF_Archive
```
Other Electronic Arts file formats (used inside or alongside big archives):<br/>
```
  https://wiki.multimedia.cx/index.php/Electronic_Arts_Formats_(2) - BNK etc
```

#### Electronic Arts 24bit C0FB archives
```
  000h 2   ID C0FBh                (C0h,FBh)  (big-endian)      ;\
  002h 2   Size of Header-4        (00h,15h)  (big-endian)      ; Header
  004h 2   Number of Files         (00h,01h)  (big-endian)      ;
  006h ..  File List                                            ;/
  019h ..  Padding to 4-byte boundary?                          ;-Padding
  01Ch ..  File Data                                            ;-Data
  ...  4   "CRCF"                                               ;\
  ...  4   Unknown (0C,00,00,00) (chunk-size little-endian?)    ; Footer
  ...  4   Unknown (3B,2E,00,00) (checksum maybe?)              ;/
```
File List entries (with variable length names, and unaligned 24bit values):<br/>
```
  000h 3   Offset in bytes (increasing)        ;(big-endian, 24bit)
  004h 3   Size in bytes                       ;(big-endian, 24bit)
  008h ..  Filename (ASCII, terminated by 00h) ;variable length
```
Used by FIFA - Road to World Cup 98 (\*.BIG)<br/>
Used by Sled Storm (MagDemo24: ART\ZZRIDER.UNI, with 8 files insides)<br/>

#### Destruction Derby Raw (MagDemo35: DDRAW\\*.PTH+.DAT, and nested therein)
```
 PTH File:
  000h N*var File List
 DAT File:
  000h ..    File Data area
```
File List entries:<br/>
```
  000h ..    Filename ("FILENAME.EXT",00h) (variable length)
  ...  4     File Size in bytes (can be odd)
  ...  4     File Offset in bytes in DAT file (increasing, unaligned)
```
Caution: Filenames in PTH archives aren't sorted alphabetically (so DAT isn't
always guaranteed to be the previous entry from PTH, namely, that issue occurs
in MagDemo35: DDRAW\INGAME\NCKCARS.PTH\\*.PTH+DAT).<br/>
Caution: The whole .DAT file can be compressed: If the sum of the filesizes in
PTH file does exceed the size of the DAT file then assume compression to be
used (normally, the top-level DATs are uncompressed, and nested DATs are
compressed).<br/>
[CDROM File Compression PCK (Destruction Derby Raw)](cdromfileformats.md#cdrom-file-compression-pck-destruction-derby-raw)<br/>

#### SnoCross Championship Racing (MagDemo37: SNOCROSS\SNOW.TOC+.IMG)
```
 TOC:
  000h N*var File List
 IMG:
  000h ..    File Data area
```
File List entries:<br/>
```
  000h ..    Filename ("DATA\FILENAME.EXT",00h) (variable length)
  ...  4     File Offset (increasing, 800h-byte aligned, in .IMG file)
  ...  4     File Size in bytes
```
Resembles DDRAW\\*.PTH+.DAT (but Offset/Size are swapped, and uses 800h-align).<br/>
Note: The archive contains somewhat corrupted TGA's:<br/>
```
  TGA[10h..11h] = 08h,08h  ;bpp=8 (okay) and attr=8 (nonsense)
  TGA[10h..11h] = 10h,01h  ;bpp=16 (okay) and attr=1 (okay) but it's yflipped
```



##   CDROM File Archives with Offset and Size
#### Crash Team Racing (retail: BIGFILE.BIG, and MagDemo30/42: KART\SAMPLER.BIG)
```
  000h 4     Zero
  004h 4     Number of Files (260h)
  010h N*8   File entries
  ...  ..    Zeropadding to 800h byte boundary
  ...  ..    File Data
```
File Entries:<br/>
```
  000h 4   Fileoffset/800h (increasing)
  004h 4   Filesize in bytes
```
Filetypes in the archive include...<br/>
```
  MDEC v2 STR's  (file 1E1h..1F8h,1FAh)
  TIM textures  (file 01FBh..0200h and others)
  empty files   (file 01F9h and others)
  small archives with named entries (file B5h,124h,125h,126h and others)
  stuff with date string and names (file 253h,256h)
  there seem to be no nested BIG files inside of the main BIG file
```

#### Black Matrix (\*.DAT)
```
  000h 4    Number of files (N) (eg. 196h)
  004h 4    Unknown (always 0Bh) (maybe sector size shift?)
  008h N*4  File List
  ...  ..   Zeropadding to 800h-byte boudary
  ...  ..   File Data
```
File List entries:<br/>
```
  000h 2    Offset/800h (increasing)
  002h 2    Size/800h (can be zero)
```
The "files" might actually contain small child folders? Or the whole stuff is
just some kind of data structure, not an actual file system archive.<br/>

#### Charumera (\*.CVF)
```
  000h N*4  File List
  ...  ..   Zeropadding to 800h-byte boundary
  ...  ..   File Data area
 File List entries:
  000h 1    Size/800h   (8bit)
  001h 3    Offset/800h (24bit, increasing)
```

#### Vs (MagDemo03: THQ\\*) has .CDB archives
```
  000h  N*8   File List
  ...   ..    Zeropadding to 800h-byte boundary
  ...   ..    File Data
  ...   ..    Garbage padding (can be several megabytes tall)
```
File List entries:<br/>
```
  000h 2     Offset/800h (increasing)
  002h 2     Size/800h (same as below, rounded up to sector units)
  004h 4     Size in bytes
```
Note: The files may consist of multiple smaller files badged together (eg.
DISPLAY.CDB contains several TIMs per file).<br/>
Some CDB archives have garbage padding at end of file: BIN.CDB (2Kbyte),
CSEL.CDB (80K), DISPLAY.CDB (70K), MOT.CDB (10648Kbyte). Maybe that's related
to deleted files in the Vs demo version and/or to updating the CDB archives
with newer/smaller content, but without truncating the CDB filesize
accordingly.<br/>

#### Monster Rancher (MagDemo06: MR\_DEMO\\*.OBJ)
#### Deception III Dark Delusion (MagDemo33: DECEPT3\K3\_DAT.BIN)
#### Star Trek Invasion (MagDemo34: STARTREK\STARTREK.RES)
Similar as .CDB archives (but with 32bit offset, and without duplicated size).<br/>
```
  000h  N*8   File List
  ...   4     File List end marker (00000000h)
  ...   ..    Garbage padding to 800h-byte boundary
  ...   ..    File Data
```
File List entries:<br/>
```
  000h 4     Offset/800h (increasing)
  004h 4     Size in bytes (often zero; for unused file numbers)
```
Note: Files are usually padded with 0..7FFh bytes to 800h-byte boundary, but
STARTREK.RES does append additional 800h-byte padding after each file (ie.
800h..FFFh padding bytes in total).<br/>

#### Einhander (MagDemo08: BININDEX.BIN/BINPACK0.BIN/BINPACK1.BIN)
```
  000h X*4  File List for BINPACK0.BIN                   ;\
  ...  ..   Zeropadding                                  ; BINPACK0
  410h ..   Unknown (some/all of it looks like garbage)  ;/
  800h Y*4  File List for BINPACK1.BIN                   ;\
  ...  ..   Zeropadding                                  ; BINPACK1
  C10h ..   Unknown (some/all of it looks like garbage)  ;/
```
File List entries:<br/>
```
  000h 2    Offset/800h in BINPACK0.BIN or BINPACK1.BIN
  002h 2    Size/800h
```

#### SO98 Archives (NBA Shootout '98, MagDemo10: SO98\..\*.MDL \*.TEX \*.ANI \*.DAT)
Resembles .BZE (in terms of duplicated size entry).<br/>
```
  000h 4     Number of Files
  004h 4     Size of File Data area (total filesize-N*0Ch-8)
  008h N*0Ch File List
  ...  ..    File Data area
```
File List entries:<br/>
```
  000h 4   Offset (zerobased, from begin of File Data area)
  004h 4   Size in bytes
  008h 4   Size rounded to mutiple of 4-bytes
```
.DAT contains .TIM .SEQ .VB .VH and nested SO98 archives<br/>
.MDL contains whatever (and empty 0-byte files)<br/>
.TEX contains .TIM<br/>
.ANI contains whatever<br/>

#### Gran Turismo 1 (MagDemo10: GT\\*.DAT) GT-ARC
#### Gran Turismo 1 (MagDemo15: GT\\*.DAT) GT-ARC
#### Gran Turismo 2 (GT2.VOL\arcade\arc\_fontinfo) GT-ARC
```
  000h 0Ch   ID "@(#)GT-ARC",00h,00h
  00Ch 2     Content Type (8001h=Compressed, 0001h=Uncompressed)
  00Eh 2     Number of Files (eg. 0Fh)
  010h N*0Ch File List
  ...  ..    File Data area
 File List entries:
  000h 4     Offset in bytes (increasing, unaligned)
  004h 4     Compressed File Size (can be odd)  ;\both same when uncompressed
  008h 4     Decompressed File Size             ;/(ie. when [00Ch]=0001h)
```
MESSAGES.DAT, SOUND.DAT, TITLE.DAT which are completely uncompressed GT-ARC's.
Most other GT-ARC's contain LZ compressed files. In case of CARINF.DAT it's
vice-versa, the files are uncompressed, but the GT-ARC itself is LZ compressed
(the fileheader contains 00h,"@(#)GT-A",00h,"RC",00h,00h; it can be detected
via those bytes, but lacks info about decompressed size).<br/>
[CDROM File Compression GT-ZIP (Gran Turismo 1 and 2)](cdromfileformats.md#cdrom-file-compression-gt-zip-gran-turismo-1-and-2)<br/>

#### O.D.T. (MagDemo17: ODT\\*.LNK and ODT\RSC\NTSC\ALLSOUND.SND and nested LNK's)
#### Barbie Explorer (MagDemo50: BARBIEX\\*.STR and nested therein)
```
  000h 4     Number of Files (N)
  004h N*8   File List
  ...  ..    File Data area
```
File List entries:<br/>
```
  000h 4     Offset in bytes (increasing, 1/4-byte? aligned)
  004h 4     File Size in bytes (usually N*4, TXT's in ODT are padded as so)
```
Quirk: Instead of rounding only Offsets to N\*4 byte boundary, all Sizes are
rounded to N\*4 bytes (eg. TXT files in ODT\RSC\NTSC\GFILES.LNK\01 with odd
number of characters are are zeropadded to N\*4 bytes).<br/>
Note: The PADBUG archives in Final Fantasy VIII (FF8) are very similar (but
have a different alignment quirk).<br/>

#### Bust A Groove (MagDemo18: BUSTGR\_A\\*.DFS and BUSTGR\_B\\*.DFS) (DFS)
#### Bust-A-Groove 2 (MagDemo37: BUSTAGR2\BUST2.BIN\\*) (main=DF2 and child=DFS)
Same as in O.D.T. with extra "DFS\_" ID at start of file.<br/>
```
  000h 4     ID "DFS_" (with align 4) or "DF2_" (with align 800h)
  004h 4     Number of Files (N)
  008h N*8   File List
  ...  ..    File Data area
 File List entries:
  000h 4     Fileoffset in bytes (4-byte or 800h-byte aligned, increasing)
  004h 4     Filesize in bytes (can be odd, eg. in BUSTGR_A\SELECT.BPE\*)
```
The game does use uncompressed DFS archives (in .DFS files) and compressed DFS
archives (in .BPE files):<br/>
[CDROM File Compression BPE (Byte Pair Encoding)](cdromfileformats.md#cdrom-file-compression-bpe-byte-pair-encoding)<br/>
The game does also use .DBI files (which contain filenames and other strings,
whatever what for).<br/>

#### Monaco Grand Prix Racing Simulation 2 (MagDemo24: EXE\\*\\*.SUN)
Same as DFS, but with Total Filesize instead of "DFS\_".<br/>
```
  000h 4     Total used filesize (excluding zeropadding to 2EE000h)
  004h 4     Number of Files (N)
  008h N*8   File List
  ...  ..    File Data area
  ...  (..)  In some files: Zeropadding to 2EE000h (3072Kbytes)
```
File Entries:<br/>
```
  000h 4     Offset (increasing, 4-byte aligned, see note)
  004h 4     Filesize in bytes (can be odd in Monaco)
```
Note: The alignment in Monaco is a bit glitchy:<br/>
```
  If (Size AND 3)=0 then NextOffset=Offset+Size             ;Align4
  If (Size AND 3)>0 then NextOffset=Offset+Size+Align800h   ;Align800h
  Namely, Monaco has files with Size=3BC5h.
```
The first file starts with unknown 32bit value, followed by "pBAV".<br/>

#### Rollcage (MagDemo19: ROLLCAGE\SPEED.IMG) (2Mbyte)
#### Rollcage Stage II (MagDemo31: ROLLCAGE\SPEED.IDX+SPEED.IMG) (3Kbyte+9Mbyte)
#### Sydney 2000 (MagDemo37: OLY2000\DEMO.IDX+DEMO.IMG) (1Kbyte+2Mbyte)
```
 Rollcage 1 uses a single IMG file that contains both directory and data:
  000h 4     Header offset (0)          ;\
  004h 4     Header size (10h+N*10h)    ; this seems to be a File List entry
  008h 4     Header size (10h+N*10h)    ; for the header itself
  00Ch 4     Zero                       ;/
  010h N*10h File List                  ;-File List for actual files
  ...  ..    Zeropadding to 800h-byte boundary
  ...  ..    File Data area
  Number of files is "IMG[04h]/10h" (minus 1 for excluding the header itself)
 The other titles have seaparate IDX and IMG files for directory and data:
  SPEED.IDX = Directory (N*10h bytes File List with offsets into SPEED.IMG)
  SPEED.IMG = File data
  Number of files is "Filesize(SPEED.IDX)/10h"
```
File List entries:<br/>
```
  000h 4     Fileoffset in bytes (800h-byte aligned, increasing)
  004h 4     Filesize in bytes
  008h 4     When compressed:   GT20 Header [004h] (decompressed size)
             When uncompressed: Same as filesize
  00Ch 4     When compressed:   GT20 Header [008h] (overlap, usuallly 3, or 7)
             When uncompressed: Zero
```
The compression related entries allow to pre-allocated the decompression buffer
(without needing to load the actual GT20 file header), and then load the
comprssed file to the top of the decompression buffer.<br/>
[CDROM File Compression GT20 and PreGT20](cdromfileformats.md#cdrom-file-compression-gt20-and-pregt20)<br/>

#### Ultimate 8 Ball (MagDemo23: POOL.DAT) (5.5Mbyte)
```
  000h 4      Number of Entries
  004h N*0Ch  File List
  ...  ..     Zeropadding to 800h-byte boundary
  ...  ..     File Data area
 File List entries:
  000h 4      Unknown (random/checksum?)
  004h 4      File Offset (800h-byte aligned, increasing)
  008h 4      File Size in bytes
```
Notes: The LAST file isn't zeropadded to 800h-byte boundary. The File List
includes some unused entries (all 0Ch-bytes zerofilled).<br/>

#### BIGFOOL - 3D Baseball (BIGFILE.FOO)
```
  000h N*0Ch  File List                                   (154h entries)
  ...  N*4    Filename Checksums (?)                      (154h entries)
  ...  ..     Zerofilled (padding to 800h-byte boundary)
  ...  ..     File Data area
```
The 1st list entry describes the current directory itself, as so:<br/>
```
  000h 4      Number of entries (including the 1st entry itself)
  004h 4      Offset/800h (always 0, relative from begin of directory)
  008h 4      Type        (always 3=Directory)
```
Further list entries are Files or Subdirectories, as so:<br/>
```
  000h 4      For Files: Size in bytes, for Directories: Number of entries
  004h 4      Offset/800h (from begin of current directory, increasing)
  008h 4      Type        (0=File, 3=Directory)
```

#### Spec Ops - Airborne Commando (BIGFILE.CAT and nested CAT files therein)
```
  000h 4     File ID                                 (always 01h,02h,04h,08h)
  004h 4     Maybe Version?                          (always 01h,00h,01h,00h)
  008h 4     Header Size (18h+N*8+ArchiveNameLength)    ;eg. 4ECh
  00Ch 4     Sector Alignment (can be 4 or 800h)
  010h 4     Number of Files (N)                        ;eg. 99h
  014h 4     Length of Archive Name (including ending 00h)
  018h N*8   File entries (see below)
  ...  ..    Archive Name, ASCII, terminated by 00h     ;eg. "bigfile.dir",00h
  ...  ..    Zeropadding to Sector Alignment boundary
  ...  ..    File Data
```
File Entries:<br/>
```
  000h 4   Fileoffset (with above Sector Alignment) (increasing)
  004h 4   Filesize in bytes
```
Filetypes in the archive include...<br/>
```
  nested CAT archives (file 07h,0Ch,11h,16h,1Bh,20h,25h,etc)
  empty files         (file 3Eh,5Ah-5Fh,62h-67h,etc)
  MDEC v2 STR's       (file 95h-96h)
  XA-ADPCM's          (inside of nested CAT, in file94h\file*)
```
There are "strings" in some files, are those filenames, eg. Icon\_xxx etc?<br/>

#### Hot Shots Golf 2 (retail: DATA\F0000.BIN, MagDemo31/42: HSG2\MINGOL2.BIN)
The DATA directory is 13800h bytes tall. But, the PSX kernel supports max 800h
bytes per ISO directory (so the kernel can only see the first 33 files in that
directory). The game isn't actually trying to parse the ISO directory entries,
instead, it's using the 2800h-byte offset/size list in F0000.BIN to access the
directory content:<br/>
```
  0000h+N*4 1     Sector MM in BCD      ;\based at 00:06:00 for file 0
  0001h+N*4 1     Sector SS in BCD      ; (unused files are set to 00:00:00)
  0002h+N*4 1     Sector FF in BCD      ;/
  0003h+N*4 1     Size MSB in hex (Size/800h/100h)
  2000h+N   1     Size LSB in hex (Size/800h AND FFh)
  2800h     (..)  Data area for file 001h..590h (demo version only)
```
Retail Version disc layout:<br/>
```
  Sector 000ADh  SCUS_944.76       ;exefile     ;\
  Sector 00130h  SYSTEM.CNF                     ; iso root folder
  Sector 00131h  DATA (sub-folder, 27h sectors) ;/
  Sector 00158h  (padding)                      ;-padding to 00:06:00
  Sector 001C2h  DATA\F0000.BIN    ;file 000h   ;\
  Sector 001C7h  DATA\F0001.BIN    ;file 001h   ;
  ...                                           ; iso data folder
  Sector 00B54h  DATA\F0032.BIN    ;file 020h   ;
  Sector 00B9Bh  DATA\F0033.BIN    ;file 021h   ;  ;\files exceeding the 800h
  ...            ...                            ;  ; directory size limit, not
  Sector 1A0C9h  DATA\F1907.BIN    ;file 773h   ;/ ;/accessible via PSX kernel
  Sector 1AAF1h  DUMMY.BIN                      ;-iso root folder (padding)
```
Demo version in Playstation Magazine is a bit different: It has only two large
.BIN files (instead of hundreds of smaller .BIN files). The directory is stored
in first 2800h bytes of MINGOL2.BIN. The MM:SS:FF offsets are numbered as if
they were located on sector 00:06:00 and up (to get the actual location:
subtract 00:06:00 and then add the starting sector number of MINGOL2.BIN).<br/>
```
  Sector 07148h  HSG2\MINGOL2.BIN  ;file 000h..590h  ;demo binary files
  Sector 0AC1Dh  HSG2\MINGOL2X.BIN ;file 76Ch        ;demo streaming file(s)
  Sector 0B032h  HSG2\SCUS_944.95  ;exefile          ;demo exe file
```
Note: File 000h is a dummy entry referring to the 2800h-byte list itself
(retail file 000h has offset=00:06:00 but size=0, demo file 000h has offset and
size set to zero). File 001h is the first actual file (at offset=00:06:05, ie.
after the 2800h-byte list)<br/>

#### Threads of Fate (MagDemo33: TOF\DEWPRISM.HED+.EXE+.IMG)
The demo version uses "Virtual Sectors" in HED+EXE+IMG files. Apart from that,
the format is same as for the "Hidden Sectors" in retail version:<br/>
[CDROM File Archives in Hidden Sectors](cdromfileformats.md#cdrom-file-archives-in-hidden-sectors)<br/>

#### WWF Smackdown (MagDemo33: TAI\\*.PAC\\*, and nested therein)
These "PAC " files are found in the main archives (which use a separate archive
format, with ID "DPAC").<br/>
```
  000h 4     ID ("PAC ")                                        ;\
  004h 4     Number of files (N)                                ; Header
  008h N*8   File List                                          ;/
  ...  ..    File Data area                                     ;-Data area
```
File List entries:<br/>
```
  000h 2     File ID (inreasing, but may skip numbers, ie. non-linear)
  002h 3     File Offset (increasing, relative to begin of Data area)
  005h 3     File Size
```
Bug: TAI\C.PAC\EFFC\0001h has TWO entries with File ID=0002h.<br/>

#### Tyco R/C Racing (MagDemo36: TYCO\MAINRSRC.BFF)
```
  000h 4     Unknown (1)
  004h 4     Filelist Offset          (800h)
  008h 4     Filelist Size (N*8+4)    (7ACh)
  ...  ..    Padding to 800h-byte boundary (see note)
  800h 4     Number of files (N)      (F5h)
  804h N*8   File List
  ...  ..    Padding to 800h-byte boundary (see note)
  ...  ..    File Data area
```
File List entries:<br/>
```
  000h 4     File Offset in bytes (increasing, 800h-byte aligned)
  004h 4     File Size in bytes
```
Padding Note: Padding after headers & files is weirdly done in two steps:<br/>
```
  Step 1: Zeropadding to 200h-byte boundary    (first 0..1FFh bytes)
  Step 2: Garbagepadding to 800h-byte boundary (last 0..600h bytes)
```

#### Team Buddies (MagDemo37: BUDDIES\BUDDIES.DAT)
```
  000h 2     ID ("BD")
  002h 2     Number of files (N)
  004h N*8   File List
  ...  ..    Zeropadding to 3000h
  3000h ..   File Data area
```
File List entries:<br/>
```
  000h 4     File Offset/800h (increasing)
  004h 4     File Size in bytes
```

#### Gundam Battle Assault 2 (DATA\\*.PAC, and nested therein)
```
  000h 4     ID ("add",00h)
  004h 4     Fixed (4)
  008h 4     Offset to File List (usually/always 20h)
  00Ch 4     Number of Files (N)
  010h 4     Fixed (10h)
  014h 0Ch   Zerofilled
  020h N*10h File List
  ...  ..    File Data area
```
File List entries:<br/>
```
  000h 4     Offset (increasing, 4-byte aligned)  ;\or both zero
  004h 4     Size (can be odd)                    ;/
  008h 4     Unknown (0) (or 00h,10h,11h,20h,30h,40h when Offset/Size=0)
  00Ch 4     Zero (0)
```

#### Incredible Crisis (MagDemo38: IC\\*.CDB)
```
  000h 4     Number of files (N)
  004h N*4   File List
  ...  ..    Zeropadding to 800h-byte boundary
```
File List entries:<br/>
```
  000h 2     File Offset/800h (increasing)
  002h 2     File Size/800h
```

#### Ape Escape Sound Archive (MagDemo22:KIDZ\KKIIDDZZ.HED\DAT\1Bh-1Dh,49h-53h,..)
#### Ape Escape Sound Archive (MagDemo44:KIDZ\KKIIDDZZ.HED\DAT\1Bh-1Dh,4Fh-59h,..)
```
  000h 5*4   File Sizes   (can be odd) (can be 0 for 2nd and 5th file)
  014h 5*4   File Offsets (28h and up, increasing by sizes rounded to N*10h)
  028h ..    File Data area (first file usually/always contains "SShd")
```

#### Ultimate Fighting Championship (MagDemo38: UFC\CU00.RBB)
```
  0000h 4    ID "siff"                                  ;\Header
  0004h 4    Total Filesize (DADB1Ch)                   ;/
  0008h 4    ID "RSRC"                                  ;\
  000Ch 4    String Size (70h)                          ; ASCII string
  0010h 70h  String "RC ver1.0 Copyright",...,00h       ;/
  0080h 4    ID "RIDX"                                  ;\
  0084h 4    File List Size     (1F78h) (3EFh*8)        ; Directory
  0088h N*8  File List (Offset, Size1)                  ;/
  2000h 4    ID "EXIX"                                  ;\
  2004h 4    Extended List Size (FBCh)  (3EFh*4)        ; Extended
  2008h N*4  Extended List (Size2)                      ;/
  2FC4h 4    ID "GAP0"                                  ;\Alignment Padding
  2FC8h 4    Padding Size (2Ch)                         ; (so that next chunk
  2FCCh 2Ch  Padding (1Ah-filled)                       ;/starts at boundary-8)
  2FF8h 4    ID "RBB0"                                  ;\
  2FFCh 4    File Data area Size (DAAB1Ch)              ; Data area
  3000h ..   File Data area                             ;/
```
File List entries (RIDX):<br/>
```
  000h 4     File Offset (increasing, 4-byte aligned, from ID "RBB0" plus 8)
  004h 4     File Size in bytes (can be odd)
```
Extended List entries (EXIX):<br/>
```
  000h 4     File Size in bytes (always the same size as in RIDX chunk)
```

#### Ultimate Fighting Championship (MagDemo38: UFC\CU00.RBB\183h,37Bh..3EBh)
```
  000h 4     ID "OIFF"                                  ;\Header
  004h 4     Total Filesize                             ;/
  008h 4     ID "TIMT" or "ANMT"                        ;\
  00Ch 4     Size (N*4)                                 ; Directory Table
  010h N*4   File List (offsets from begin of Data ID+8);/
  ...  4     ID "TIMD" or "ANMD"                        ;\
  ...  4     Data Area size (SIZ) (Filesize-18h-N*4)    ; Data area
  ...  SIZ   Data Area                                  ;/
```

#### E.T. Interplanetary Mission (MagDemo54: MEGA\MEGA.CSH+.BIN)
```
 MEGA.CSH:
  000h N*0Ch File List
 MEGA.BIN:
  000h ..    File Data area
```
File List entries:<br/>
```
  000h 4     Offset (in MEGA.BIN file, 800h-byte aligned, increasing)
  004h 4     Unknown (32bit id/random/checksum/whatever)
  008h 4     Filesize in bytes
```

#### Driver 2 The Wheelman is Back (MagDemo40: DRIVER2\SOUND\\*\\*)
```
  000h 4     Number of entries (1 or more)
  004h N*10h File List
  ...  ..    File Data area (.VB aka SPU-ADPCM)
 File List entries:
  000h 4     Offset from begin of Data area, increasing
  004h 4     Filesize in bytes
  008h 4     Unknown (0 or 1)
  00Ch 4     Unknown (AC44h, 0FA0h, 2EE0h, 2710h, 2B11h, 3E80h, 1F40h, etc.)
 Note: Above AC44h might 44100Hz, or just file number 44100 decimal?
```

#### Thrasher: Skate and Destroy (MagDemo27: SKATE\ASSETS\\*.ZAL) (Z-Axis)
#### Dave Mirra Freestyle BMX (MagDemo36: BMX\ASSETS\\*.ZAL) (Z-Axis)
#### Dave Mirra Freestyle BMX (MagDemo46: BMX\ASSETS\\*.ZAL) (Z-Axis)
```
  000h 4     ID (always 2A81511Ch)
  004h 0Ch   Zerofilled
  010h 1     Unknown (1)
  011h 1     Compression Flag for all files (00h=Uncompressed, 80h=Compressed)
  012h 2     Number of files (bit0-13?=N, bit14=Unknown, can be set)
  014h N*0Ch File List, 12 bytes/entry      ;<-- when [11h]=00h=uncompressed
  014h N*10h File List, 16 bytes/entry      ;<-- when [11h]=80h=compressed
  ...  ..    File Data area
```
File List entries (0Ch or 10h bytes per entry, depending on compression):<br/>
```
  000h 4     File ID (usually 0=first, increasing) (or 0001h,7531h,7532h,...)
  004h 4     Offset-10h in bytes (increasing, 4h-byte aligned)
  008h 4     Filesize, uncompressed (can be odd)
  00Ch (4)   Filesize, compressed (can be odd)   ;<-- exists only if compressed
```
For decompression, see:<br/>
[CDROM File Compression ZAL (Z-Axis)](cdromfileformats.md#cdrom-file-compression-zal-z-axis)<br/>

#### Speed Punks (MagDemo32: SPUNKS\\*.GDF)
```
  000h 4     ID "0FDG XSP" (aka PSX GDF0 backwards)
  008h 4     Header Size (N*10h+10h)
  00Ch 4     Number of files (N)
  010h N*10h File List
  ...  ..    Zeropadding to 800h-byte boundary
  ...  ..    File Data area
 File List entries:
  000h 4     ID/Type ("MARV", "MARS", "MARD", "PMET", "COLR", "MROF")
  004h 4     ID/Num  (usually 1 SHL N, or all zero)
  008h 4     Offset (800h-byte aligned, increasing)
  00Ch 4     Size in bytes
```

#### Legend of Dragoon (MagDemo34: LOD\SECT\\*.BIN, and nested therein)
```
  000h 4     ID "MRG",1Ah
  004h 4     Number of Files (eg. 0, 1, 2, 193h, 2E7h, or 1DBBh)
  008h N*8   File List
  ...  ..    Padding to 800h-byte boundary (8Ch-filled) (not in nested MRG's)
  ...  ..    File Data area
 File List entries:
  000h 4     Offset/800h, or 4-byte aligned Offset/1 (increasing)
  004h 4     Size (can be odd, and can be zero)
 Size oddities:
  Empty files in demo version have Size=0 and Offset=0.
  Empty files in retail version have Size=0 and Offset=OffsetOfNextFile.
  MRG archives can start or end with Empty files.
  All files can be empty (eg. retail DRAGN0.BIN\1190h).
  NumFiles can be zero (eg. retail DRAGN0.BIN\1111h, demo DRAGN0.BIN\10E2h).
 Offset oddities:
  SECT\*.BIN have Offset/800h
  Nested MRGs have 4-byte aligned Offset/1
  The two variants can be detected as:
   if FirstOffset=(NumFiles*8+8) then NestedVariant
   if FirstOffset=(NumFiles*8+8+7FFh) AND NOT 7FFh then RootVariant
  Whereas, FirstOffset is the first NONZERO offset in file list (important
  for demo version, which has archives that start with ZERO offsets).
```

#### RC Revenge (MagDemo37: RV2\BB\3.BBK and Retail: BB\\*\\*.BBK)
This does basically contain four large files (and four info blocks with info on
the content of those files).<br/>
```
  000h 4     Random/Checksum?
  004h 4     Faded ID (FADED007h)
  008h 4     Part 1 Offset (Sound)     (always E5Ch)
  00Ch 4     Part 2 Offset (Texture)   (when Type=01h: Offset-E5Ch)
  010h 4     Part 3 Offset (?)         (when Type=01h: Offset-E5Ch)
  014h 4     Part 4 Offset (?)         (when Type=01h: Offset-E5Ch)
  018h 4     Type (10h or 20h=Normal)  (or 01h=Special in BB\8\*.BBK)
  01Ch B0Ch  Part 1 Info (Sound)       (when Type=01h: garbage-filled)
  B28h 314h  Part 2 Info (Texture)
  E3Ch 14h   Part 3 Info (?)
  E50h 0Ch   Part 4 Info (?)
  E5Ch ..    Part 1 Data (Sound, SPU-ADPCM data, if any)
  ...  ..    Part 2 Data (Texture data) (starts with BDEF1222h or BDEF1111h)
  ...  ..    Part 3 Data (?)   ;\maybe map, models, and/or whatever
  ...  ..    Part 4 Data (?)   ;/
```
Part 1 Info (Sound info) (if any):<br/>
```
  01Ch 4     Random/Checksum?
  020h 4     Faded ID (FADED007h)
  024h 4     Part 1 Size              (eg.7C7F0h)
  028h 4     SPU Start Addr           (1010h) (for data from file offset E5Ch)
  02Ch 4     SPU Middle Addr          (eg. 58F70h)
  030h 4     SPU End Addr             (eg. 7D800h) (start+size)
  034h 2     Middle entry number      (often 3Ch)
  036h 2     Number of used entries-1 (eg. 50h means that 51h entries are used)
  038h AF0h  Sample List (100 entries, unused ones are zerofilled)
  914h 214h  Zerofilled (unused 1Ch-byte entries) (total is 1Ch*64h)
 Sample List entries:
  000h 4     SPU Offset (1010h and up) (SpuOffset=1010h is FileOffset=E5Ch)
  004h 4     Sample Size in bytes
  008h 4     Unknown (0)
  00Ch 4     Unknown (0)
  010h 4     Pitch   (400h=11025Hz, 800h=22050Hz, 2E7h=8000Hz, 8B5h=24000Hz)
  014h 4     Unknown (0 or 1)
  018h 4     File ID (00001F08h and up)
```
Part 2 Info (Texture info):<br/>
```
  B28h 4     Random/Checksum?
  B2Ch 4     Faded ID (FADED007h)
  B30h 4     Part 2 Size      (N*16000h)  ;Width=2C0h halfwords, Height=N*64
  B34h 4     Zero             (0h)
  B38h 4     Some RAM Address (8010xxxxh)
  B3Ch 4     Unknown          (eg. 195h or E3h) ;same as at [DA4h]
  B40h 4+4   VRAM Address X,Y (140h,0)          ;maybe load target
  B48h 4+4   VRAM Address X,Y (140h,0)          ;maybe palette base?
  B50h 4+4   VRAM Address X,Y (xx0h,Height-40h) ;often at/near end of used area
  B58h 4     Unknown          (eg. 1D0h or 1E0h)
  B5Ch 4     Unknown          (eg. 1Ah or 0Dh)
  B60h 200h  Some halfwords?  (most are FFFFh, some are 0000h)
  D60h 40h   Zerofilled       (0)
  DA0h 4     Unknown          (eg. 185h or E2h)
  DA4h 4     Unknown          (eg. 195h or E3h) ;same as at [B3Ch]
  DA8h 9x10h Special Texpages (VramX,Y, SizeX,Y, StepX,Y, Flag/Type/Num or so?)
  E38h 4     Some RAM Address (800Axxxxh)
```
Part 3 Info:<br/>
```
  E3Ch 4     Random/Checksum?
  E40h 4     Faded ID (FADED007h)
  E44h 4     Part 3 Size                  (eg. A9728h or 51264h)
  E48h 4     RAM End Address (start+size) (eg. 801Fxxxxh) (near memtop)
  E4Ch 4     RAM Start Address (end-size) (eg. 801xxxxxh)
```
Part 4 Info:<br/>
```
  E50h 4     Random/Checksum?
  E54h 4     Faded ID (FADED007h)
  E58h 4     Part 4 Size (usually 10CCCh) (or 105E0h in demo version)
```
Note: File CAT\RDS.CAT does also start with ID=FADED007h (but contains whatever
different stuff).<br/>



##   CDROM File Archives with Offset
Below are archives that start with a simple Offset list. The DOT1 and DOTLESS
types are "standard" archives used by many PSX games (although the "standard"
was probably independently created by different developers).<br/>

#### DOT1 Archives (named after the ".1" extension in R-Types)
Used by various titles:<br/>
```
  R-Types (CG.1, PR\PR.1, and nested inside CG.1)
  Final Fantasy IX (nested inside FF9.IMG, FF9.IMG\DB, FF9.IMG\DB\DOT1)
  Legend of Mana (*.EFF,*.SET,*.BTP(?) in folders SND*,SOUND,WM(?))
  Witch of Salzburg (*.ANM/BIN/BSS/DAT/MDL/SCE)
  Rayman (RAY\*.XXX, RAY\SND\*.ALL, and nested inside *.XXX)
  Pandemonium II (JESTERS.PKG\0101\0008 and JESTERS.PKG\0101\000D)
  Incredible Crisis (MagDemo38: IC\TAN_DAT.CDB\<DOTLESS>\<DOT1>\<SHIFTJIS>)
  Various games on PlayStation Magazine Demo Discs (Disc 03-54)
```
DOT1 (in lack of a better name) is a simple archive format that contains Number
of Entries and List with Increasing Offsets to File data.<br/>
```
  000h 4    Number of Files (N)                 (eg. 2..18)
  004h N*4  File List (offsets to each file, increasing, aligned)
  ...  (4)  Optional: Total filesize (aka end-offset for last list entry)
  ...  ..   Optional: Zeropadding to alignment boundary (when alignment>4)
  ...  ..   File Data
```
There are four variants with different alignment (and in some cases, with an
extra entry with end-offset for last file):<br/>
```
  Align800h, no extra entry    R-Types (CG.1 and PR\PR.1)
  Align4,    no extra entry    R-Types (nested in CG.1), FF9 (in IMG, IMG\DB)
  Align2,    no extra entry    Incredible Crisis (IC\TAN_DAT.CDB\*\*)
  Align800h, with extra entry  MLB 2000 (DATA.WAD)
  Align10h,  with extra entry  Witch of Salzburg (*.ANM/BIN/BSS/DAT/MDL/SCE)
  Align4,    with extra entry  Rayman (*.XXX, *.ALL)
```
The files can be detected by checking [004h]=4+(N\*4), 4+(N\*4)+Align800h,
4+(N\*4)+4, or 4+(N\*4)+4+Align10h, and checking that the offsets are increasing
with correct alignment (Rayman has some empty files with same offset), and
don't exceed the total filesize. And that the alignment space is zeropadded (in
case of R-Types, only the header is 00h-padded, but files are FFh-padded).<br/>
The detection could go wrong, especially if the archive contains very few
files, some of the nested DOT1's contain only one file (header "00000001h,
00000008h", without any further increasing offsets or padding). As workaround,
accept such files only if they have a ".1" filename extension, or if they were
found inside of a bigger DOT1, IMG, or DB archive.<br/>
Final Fantasy IX contains some DOT1's with fewer than few entries (the file
being only 4-bytes tall, containing value NumEntries=00000000h).<br/>

#### NFL Gameday '98 (MagDemo04: GAMEDAY\\*.FIL) (32bit) (with nested FIL's)
#### NFL Gameday '99 (MagDemo17: GAMEDAY\\*.FIL) (32bit)
#### NFL Gameday 2000 (MagDemo27: GAMEDAY\\*.FIL) (16bit and 32bit)
#### NCAA Gamebreaker '98 (MagDemo05: GBREAKER\\*.FIL,\*.BIN) (16bit and 32bit)
#### NCAA Gamebreaker 2000 (MagDemo27: GBREAKER\\*.FIL) (16bit and 32bit)
FIL/32bit (with [02h]=FFFFh):<br/>
```
  000h 2    Number of Files (N)
  002h 2    ID for 32bit version (FFFFh=32bit entries)
  004h N*4  File List (offsets to each file, increasing, 4-byte aligned)
  ...  ..   File Data
```
FIL/16bit (with [02h]\<\>FFFFh, eg. FLAG\*.FIL and VARS\STARTUP2.FIL\0\\*):<br/>
```
  000h 2    Number of Files (N)
  002h N*2  File List (offsets to each file, increasing, 4-byte aligned)
  ...  ..   Zeropadding to 4-byte boundary
  ...  ..   File Data
```

#### PreSizeDOT1 (Ace Combat 2) (retail and MagDemo01: ACE2.DAT\\*)
Like DOT1, but with Total Filesize being oddly stored at begin of file.<br/>
```
  000h 4    Total Filesize (aka end-offset for last list entry)
  004h 4    Number of Files (N)
  008h N*4  File List (offsets to each file, increasing, 4-byte aligned)
  ...  ..   File Data
```
Note: Ace Combat 2 contains PreSizeDOT1 (ACE2.DAT\02h..1Dh,36h..B2h) and normal
DOT1 archives (nested in PreSizeDOT1's and in ACE2.DAT\B3h..E1h).<br/>

#### DOT-T (somewhat same as DOT1, but with 16bit entries)
Armored Core (MagDemo02, AC10DEMP\\*.T)<br/>
```
  000h 2    Number of Files
  002h N*2  File List (Offset/800h to file data, increasing)
  ...  2    Total Size/800h (end-offset for last file)
  ...  ..   Zeropadding to 800h-byte boundary
  ...  ..   File Data
```
This can contain many empty 0-byte files (aka unused file numbers; though maybe
those files exist in the retail version, but not in the demo version).<br/>

#### DOTLESS Archive
Hot Shots Golf (MagDemo07: HSG\\*.DAT)<br/>
Hot Shots Golf 2 (retail: DATA\F0000.BIN\\*, MagDemo31/42: HSG2\MINGOL2.BIN\\*)<br/>
Starblade Alpha (FLT\\*.DAT, TEX\\*.DAT)<br/>
Incredible Crisis (MagDemo38: IC\TAN\_DAT.CDB\\<DOTLESS\>)<br/>
```
  000h N*4  Offsets to File data (increasing, usually 4-byte aligned)
  ...  (4)  Filesize (end-offset for last file) (only in Ape Escape)
  ...  ...  File Data
```
Like DOT1, but without Number of Files entry (instead, the first offset does
imply the end of file list). There's no extra entry for end of last file
(instead, that's implied in the total filesize). Most files have at least 5
entries, but HSG\TITLE0.DAT seems to contain only one entry (ie. the whole
header contains only one value, 00000004h, followed by something that looks
like raw bitmap data).<br/>
Also used by Ape Escape (MINIGAME\\* included nested ones), the Ape Escape files
do have an end-marker with last-offset (that will appear as an empty 0-byte
file at end of list when not specifically handling it).
MINIGAME\MINI2\BXTIM.BIN does also have several 0-byte files inside of the file
list.<br/>

#### Twisted Metal: Small Brawl (MagDemo54: TMSB\SHL\\*.TMS)
```
  000h 4     Size of Data Area (total filesize minus 0D0h)
  004h 4     Number of files
  008h N*4   File List (zerobased offsets from begin of Data Area)
  ...  ..    Zeropadding to 0D0h
  0D0h ..    File Data Area
```
This resembles DOT1, with an extra size entry and padding to 0D0h.<br/>

#### Ridge Racer Type 4 (MagDemo19: R4DEMO\R4.BIN, 39Mbyte)
#### Ridge Racer Type 4 (MagDemo21: R4DEMO\R4.BIN, 39Mbyte)
Basically, this is alike DOT1, but SECTOR numbers, and with extra entries...<br/>
```
  000h 4     Number of Files (N) (3C9h)
  004h N*4   File List (Offset/800h)
  ...  4     Total Size/800h                  ;<-- last offset
  ...  4     Unknown (00,E8,82,2E)            ;<-- ??? maybe chksum*800h or so?
  ...  ..    Zeropadding to 800h-byte boundary
  ...  ..    File Data area
```

#### Legend of Legaia (MagDemo20: LEGAIA\PROT.DAT)
```
  000h 4     Zero
  004h 4     Number of Entries (4D3h)
  008h N*4   File List (Offset/800h)
  ...  4     Total Size/800h (aka end Offset/800h of last file)
  ...  ..    Zeropadding to 800h-byte boundary
  ...  ..    File Data area
```
The PROT.DAT does not contain filenames, however, it's bundled with CDNAME.TXT,
which appears to contain symbolic names for (some) indices:<br/>
```
  #define init_data 0           ;for file 0000h
  #define gameover_data 1       ;for file 0001h
  #define town01 3              ;for file 0003h
  #define town0b 12             ;for file 000Ch
  ...                           ;...
  #define other6 1222           ;for file 04C6h
  #define other7 1228           ;for file 04CCh
```
The DAT file contains many zerofilled "dummy" files with 800h-byte size.<br/>

#### Bloody Roar 1 (MagDemo06: BL\\*.DAT)
#### Bloody Roar 2 (MagDemo22: ASC,CMN,EFT,LON,SND,ST5,STU\\*.DAT)
```
  000h 4     Number of Entries (N)
  004h N*4   File List (Offset-(4+N*4), increasing) (or FFFFFFFFh=Unused entry)
  ...  ..    File Data area
```
Most or all files in DAT archives are PreGT20 compressed.<br/>
[CDROM File Compression GT20 and PreGT20](cdromfileformats.md#cdrom-file-compression-gt20-and-pregt20)<br/>
Note: Unused entries can occur anywhere, eg. Bloody Roar 2 CMN\SEL01.DAT does
have both first and LAST entry marked as unused (FFFFFFFFh). Also, there may be
a lot of unused entries, eg. Bloady Roar 1 CMN\TITLE00.DAT uses only 5 of 41h
entries).<br/>

#### Klonoa (MagDemo08: KLONOA\FILE.IDX\\*)
```
  000h 4     ID "OA05"
  004h N*4   Offset List (usually/always 5 used entries, plus zeropadding)
  030h ..    File Data area (usually/always starting at offset 30h)
```

#### C - The Contra Adventure (DATA\SND\\*.SGG)
```
  000h 4    ID "SEGG"
  004h 4    Offset to .VH file
  008h 4    Offset to .VB file
  00Ch 4    Number of .SEQ files (N) (usually 6Eh, or 08h in MENU.SGG)
  010h N*4  Offsets to .SEQ files (increasing, unaligned)
  ...  ..   SEQ files
  ...  ..   Padding to 4-byte boundary
  ...  ..   VH file
  ...  ..   VB file
```

#### Ninja (MagDemo13: NINJA\VRW\\*.VRW)
```
  000h 8     ID "VRAM-WAD" (here as archive ID, although same as compress ID)
  004h N*4   File List (offsets to Data)  ;NumFiles=(FirstOffset-8)/4
  ...  ..    Data (compressed .PAK files, which do ALSO have ID="VRAM-WAD")
```
The compressed .PAK files are using a LZ5-variant:<br/>
[CDROM File Compression LZ5 and LZ5-variants](cdromfileformats.md#cdrom-file-compression-lz5-and-lz5-variants)<br/>

#### The Next Tetris (MagDemo22: TETRIS\\*) has PSX.BSE (and nested therein)
```
  000h 4     Unknown (3)
  004h 4     Total Size
  008h 4     Number of Files (N) (max 40h, for max 40h*4 bytes in file list)
  00Ch N*4   File List (increasing offsets, 800h-byte aligned)
  ...  ..    Unknown (looks like garbage padding for unused File List entries)
  10Ch 6F4h  42h-filled padding to 800h-byte boundary
  800h ..    File Data area
```

#### Tactics Ogre (UBF\*.BIN)
```
  000h 8     Fixed (88h,0,0,0,0,0,0,0)
  008h 4     Number of Files (eg. 1Dh or 585h, including last/end file)
  00Ch N*4   File List (increasing offsets, 800h-byte aligned)
  ...  ..    Zeropadding to 800h-byte boundary
  ...  ..    File Data area
```
Note: The last file is a TXT file containing "LINK-FILE END....",0Dh,0Ah,1Ah,
plus zeropadding to 800h-byte boundary.<br/>

#### Spyro the Dragon (MagDemo12: SPYRO\PETE.WAD)
```
  000h 4     Total Filesize (3E800h in Spyro)
  004h N*8   File List      (1B0h bytes in Spyro)
  ...  ..    Zeropadding to 800h-byte boundary
  ...  ..    File Data (4-byte aligned, despite of above 800h-byte hdr padding)
```
File List entries:<br/>
```
  000h 4     Fileoffset (increasing, 4-byte aligned)
  004h 4     File ID? (unsorted, not increasing, used range is 000h..1FAh)
```



##   CDROM File Archives with Size
#### Disney-Pixar's Monsters, Inc. (MagDemo54: MINC\\*.BZE)
```
  000h 4     Zero (0)
  004h 4     Type/ID (27100h=160000, 2BF20h=180000, 30D40h=200000 decimal)
  008h 4     Number of files
  00Ch N*0Ch File List
  ...  ..    Zeropadding to 7FCh
  7FCh 4     Checksum (32bit sum of SIGN-EXPANDED bytes at [000h..7FBh])
  ...  ..    File Data
```
File List entries:<br/>
```
  000h 4     File Type/ID or so (roughly increasing, eg. 1,3,6,5,7,8,9,A,B)
  004h 4     Filesize in bytes
  008h 4     Filesize rounded up to multiple of 800h bytes
```

#### Bugs Bunny: Lost in Time (MagDemo25: BBLIT\\*.BZZ) (without extra entry)
#### The Grinch (MagDemo40: GRINCH\\*.BZZ) (with extra entry)
Resembles .BZE, but without the Type entry in Header.<br/>
```
  000h 4     Fixed 1 (maybe version, or compression flag)
  004h (4)   Unknown (000xxxx0h)   ;<-- Extra in The Grinch only (not Bunny)
  ...  4     Number of files
  ...  N*0Ch File List
  ...  ..    Zeropadding to 7FCh
  7FCh 4     Checksum (32bit sum of SIGN-EXPANDED bytes at [000h..7FBh])
  ...  ..    File Data
```
File List entries:<br/>
```
  000h 4     File Type/ID or so (roughly increasing, eg. 1,2,3,6,5,7,8,9,A)
  004h 4     Filesize in bytes (rounded to N*4 even if compressed data is less)
  008h 4     Filesize rounded up to multiple of 800h bytes
```
Files are compressed, starting with 0Bh, same as in Jersey Devil...<br/>
[CDROM File Compression BZZ](cdromfileformats.md#cdrom-file-compression-bzz)<br/>
Note: The TIM files in Bugs Bunny and The Grinch BZZ archives consists of two
TIMs badged together: A 4x4 pix dummy TIM, followed by the actual 512x125 pix
TIM (in some cases followed some extra bytes at end of file?).<br/>

#### Jersey Devil .BZZ (MagDemo10: JD\\*.BZZ)
Resembles .BZE, but without the Type entries in Header and File List, and
without Header checksum.<br/>
```
  000h 4     Fixed 1 (maybe version, or compression flag)
  004h 4     Number of files (4)
  008h N*8   File List
  ...  ..    Zeropadding to 800h-byte boundary (without checksum, unlike .BZE)
  ...  ..    File Data
```
File List entries:<br/>
```
  000h 4     Size in bytes
  004h 4     Size rounded to multiple of 800h
```
Files are compressed, starting with 0Bh, same as in Bugs Bunny...<br/>
[CDROM File Compression BZZ](cdromfileformats.md#cdrom-file-compression-bzz)<br/>

#### Jackie Chan Stuntmaster (RCHARS\\*.RR)
#### NBA Basketball 2000 (MagDemo28: FOXBB\\*.RR)
```
  000h 2     ID ("PX")
  002h 2     Unknown (1 or 3)
  004h 4     Header Size (eg. 80h, 7C0h, or 1730h) (N*8+8)
  008h N*8   File List
  ...  ..    Zeropadding to 800h-byte boundary
  ...  ..    File Data area
 File List entries:
  000h 4     Offset (increasing, 800h-byte aligned)
  004h 1     Zero
  005h 3     Filesize in bytes (24bit) (can be odd)
```
Jackie Chan Stuntmaster does always have headersize=1730h (with many unused
entries with size=0, both in the middle & at the end of File List).<br/>

#### Bomberman World (MagDemo15: BOMBER\\*.RC)
```
                XXX detect this WITH extension=".RC" check before OBJ
                    (else type=1 could be mistaken as offs=1) (eg RC1\BP0*.RC)
```
Resembles .OBJ but contains Filetype? instead of Offset.<br/>
```
  000h N*8   File List
  ...  8     File List end (zerofilled)
  ...  ..    Garbage padding to 800h-byte boundary
```
File List entries:<br/>
```
  000h 4     Filetype (see below)
  004h 4     Filesize in bytes
```
There can be several files with same type in one .RC archive. Type values are:<br/>
```
  00h = End of File List (at least so when Type and Size are both zero)
  01h = .TIM
  02h = Unknown
  03h = Unknown
  05h = .VH
  06h = .VB
  09h = Unknown
  0Ah = .TIM (left half of a larger image) (right half has type 01h)
  0Bh = Unknown
  0Ch = Unknown
```

#### Mat Hoffman's Pro BMX (new demo) (MagDemo48: MHPB\BMXCD.HED+WAD)
This format is used by the NEW demo version on MagDemp48 (the OLD demo version
on MagDemo39 did use Spider-Man-style HED/WAD format with filenames).<br/>
```
 HED:
  000h 2     Number of entries (N)
  002h N*6   File List
 WAD:
  000h ...   File data (at 800h-byte aligned locations)
```
File List entries:<br/>
```
  000h 3     File ID (24bit)
  003h 3     File Size in bytes (21bit, max 2Mbyte) (upper 3bit=unused?)
```
Note: HED is processed at 80052AC0h in MagDemo48.<br/>

#### Madden NFL 2000 (MagDemo27: MADN00\\*.DAT and nested therein)
#### Madden NFL 2001 (MagDemo39: MADN01\\*.DAT and nested therein)
```
  000h 4     Header Size (N*SectorSize) (xxh, 800h, 1000h, 4800h, or 920h)
  004h 4     Sector Size (4=ChildArchive, 800h=MainArchive, 920h=FMV/MADN00)
  008h 4     File List entrysize (0=32bit, 1=16bit/MADN00, 4=16bit/MADN01)
  00Ch N*2/4 File List (16bit or 32bit filesizes in bytes)
  ...  ..    Zeropadding to SectorSize boundary
  ...  ..    Files (with above sizes, each zeropadded to SectorSize boundary)
```
Dummy files have filesize=1 (but they do nethertheless occupy a whole data
sector).<br/>
Unknown why the FMV file in MADN00 is using SectorSize=920h (it appears to be
FORM2 related, although the file seems to be stored in FORM1 sectors, but the
STR movie appears to work okay despite of the odd size).<br/>

#### Croc 2 (MagDemo22: CROC2\CROCII.DIR\FESOUND.WAD)
#### Disney's The Emperor's New Groove (MagDemo39:ENG\KINGDOM.DIR\FESOUND.WAD)
#### Disney's Aladdin in Nasira's Rev. (MagDemo46:ALADDIN\ALADDIN.DIR\FESOUND.WAD)
```
  000h 4     Total Filesize-4
  004h N*14h File List (2 entries in Croc2, 3 entries in Aladdin/Emperor)
  ...  ..    File Data area (SPU-ADPCM( (.VB files with leading zeroes)
 File List entries:               (Aladdin/Emperor) (Croc2)
  000h 4     Sample Rate in Hertz (AC44h=44100Hz)   (5622h=22050Hz)
  004h 2     Sample Rate Pitch    (1000h=44100Hz)   (0800h=22050Hz)
  006h 2     Unknown              (7Fh)             (32h)
  008h 4     Unknown              (1)               (8)
  00Ch 4     Unknown              (1FC0001Fh)       (40008Fh)
  010h 4     Filesize             (xxx0h)           (xxx0h)
```
The number of files is implied in sum of filesizes versus total size.<br/>

#### Dino Crisis 1 and 2 (PSX\DATA\\*.DAT and \*.DBS and \*.TEX) ("dummy header")
```
  000h 800h  File List (with 10h or 20h bytes per entry)
  800h ..    File Data (each file is zeropadded to 800h-byte boundary)
```
File List entrysize can be 10h or 20h bytes:<br/>
```
  Dino Crisis 1 --> always size 10h
  Dino Crisis 2 --> usually size 20h
  Dino Crisis 2 --> sometimes size 10h (eg. SC24.DAT, SC48.DAT, WEP_*.DAT)
```
File List entries:<br/>
```
 File List entries, type 0 and 7:
  000h 4     Type (0=Data (or .BS pictures), 7=CompressedData)
  004h 4     Size
  008h 4     RAM Addresss (80000000h..801FFFFFh)
  00Ch 4     Zero
  010h (10h) Zerofilled
 File List entries, type 1 and 2 and 8:
  000h 4     Type (1=Bitmap, 2=Palette, 8=CompressedBitmap)
  004h 4     Size (see below Size Notes)
  008h 2     VRAM Address X     (0..3FFh)
  00Ah 2     VRAM Address Y     (0..1FFh) (or 280h in Dino 2 ST703.DAT)
  00Ch 2     Width in halfwords (1..400h)
  00Eh 2     Height             (1..200h)
  010h (10h) Zerofilled
 File List entries, type 3 and 4:
  000h 4     Type (3=VoiceHeader("Gian"), 4=VoiceData(SPU-ADPCM))
  004h 4     Size
  008h 4     SPU Address (0..7FFF0h)
  00Ch 2     Unknown (0..7)  ;\usually both same (or val1=0, val2>0)
  00Eh 2     Unknown (0..7)  ;/
  010h (10h) Zerofilled
 File List entries, type 5 (eg. ME*.DAT):
  000h 4     Type (5=Unknown... maybe Midi-style or so)
  004h 4     Size
  008h 4     Load Address (0, or on next 4-byte boundary after previous file)
  00Ch 2     Unknown (0..2)  ;\always both same
  00Eh 2     Unknown (0..2)  ;/
  010h (10h) Zerofilled
 File List entries, type 6 and 9:
  The EXE code does also accept type 6 and 9 (type 6 is handled same as
  type 0, and type 9 is ignored), but the actual archives don't seem to
  contain any files with those types.
 File List entries, padding for unused entries:
  000h 10h   Type ("dummy header    ")
  010h (10h) Zerofilled
```
Size Notes:<br/>
```
 Bitmaps and Palettes can have following sizes:
  Width*Height*2                       ;normal case
  Width*Height*2 + Align(1000h)        ;eg. Dino Crisis 1 DOOR*.DAT
  Width*Height*2 + Align(800h)         ;eg. Dino Crisis 2 DOOR27.DAT
 CompressedBitmaps can have following sizes in compressed form:
  Less than Width*Height*2             ;normal case
  Less than Width*Height*2 + 1000h     ;eg. Dino Crisis 2 M_RESULT,ST002.DAT
 CompressedBitmaps can have following sizes after decompression:
  Width*Height*2 + 8                   ;normal case
  Width*Height*2 + Align(1000h?) + 8   ;eg. Dino Crisis 2 M_RESULT,ST002.DAT
```
Note: Dino Crisis DEMO version (MagDemo28: DINO\TRIAL.DAT) does also contain
"dummy header" DAT archives (but, unlike as in retail version, they are hidden
somewhere inside of the headerless 14Mbyte TRIAL.DAT archive).<br/>
Type 7 and 8 are using LZSS compression:<br/>
[CDROM File Compression LZSS (Dino Crisis 1 and 2)](cdromfileformats.md#cdrom-file-compression-lzss-dino-crisis-1-and-2)<br/>
Apart from LZSS, Type 4 is using SPU-ADPCM compression, and some Type 0 files
contain .BS compressed pictures (eg. Dino Crisis 2 PSX\DATA\ST\*.DBS\\*).<br/>



##   CDROM File Archives with Chunks
Chunk-based archives have chunk headers for each file, but don't have a central
directory. That's mainly useful when loading the whole archive to memory.<br/>

#### Interchange File Format (IFF)
IFF has been invented by Electronic Arts in 1985 on Amiga (hence using 2-byte
alignment and big-endian size values).<br/>
IFF does mainly define a standarized file structure for use with custom
group/chunk types (it does also define some Amiga-specific standard audio/video
types, but those are barely useful on PSX).<br/>
The files are starting with a Group Header, followed by Chunks:<br/>
```
 Group Header:
  000h 4     Group ID ("FORM") (or "LIST" or "CAT " or "PROP")
  004h 4     Group Size-08h (SIZ) (filesize-8) (big-endian)
  008h 4     Group Type (4-character ASCII) (should be an unique identifier)
  00Ch SIZ-4 Chunk(s), and/or nested Group(s)
 Chunk Format:
  000h 4     Chunk Type (4-character ASCII) (meaning depends on Group Type)
  004h 4     Chunk Size (SIZ) (big-endian)
  00Ch SIZ   Data (eg. .TIM, .VB, .VH or custom data)
  ...  ..    Zeropadding to 2-byte boundary
```
Used by Forsaken (MagDemo09: FORSAKEN\\*\\*.BND,MP,PCO)<br/>
Used by Perfect Assassin (DATA.JFS\DATA\SCREEN1.LBM)<br/>
Used by Star Wars Demolition (MagDemo39,41: STARWARS\\*.EXP)<br/>
Used by Turbo Prop Racing (MagDemo11: RRACER\\*.IFF, except COURSE.IFF)<br/>
Used by Viewpoint (VIEW.DIR\\*.VCF,\*.VCS,\*.ST\*) - some have wrong Size entry?<br/>
Used by Vigilante 8 (MagDemo09: EXAMPLE\\*.EXP)<br/>
Used by Wing Commander III (\*.LIB\\*.IFF)<br/>
Bugs in Viewpoint: fonts\\*.vcf have correct Groupsize=Filesize-8, but
screens\\*.vcf have incorrect Groupsize=Filesize-4, and streams\\*.vcf have
weirdest random Groupsize=Filesize+(-04h,+08h,+14h,+5A0h).<br/>

#### Z-Axis little-endian IFF variant
Unlike real IFF, these are using little-endian, and don't have a Group Type
entry. There seem to be no nested FORMs. Alignment is kept as 2-byte.<br/>
```
 Group Header:
  000h 4     Group ID ("FORM" or "BODY")
  004h 4     Group Size-08h (SIZ) (little-endian)
  008h SIZ   Chunk(s)
 Chunk Format:
  000h 4     Chunk Type (4-character ASCII)
  004h 4     Chunk Size (SIZ) (little-endian)
  00Ch SIZ   Data
  ...  ..    Zeropadding to 2-byte boundary
```
ID "FORM" used by Thrasher: Skate and Destroy (MagDemo27: SKATE\ASSETS\\*.ZAL\\*)<br/>
ID "FORM" used by Dave Mirra Freestyle BMX (MagDemo36,46: BMX\ASSETS\\*.ZAL\\*)<br/>
ID "BODY" used by Colony Wars (MagDemo02: CWARS\GAME.RSC\\*.BND)<br/>
ID "BODY" used by Colony Wars Venegance (MagDemo14: CWV\GAME.RSC\\*.BND)<br/>

#### Alice in Cyberland little-endian IFF variant (.TPK)
Same as Z-Axis IFF variant, except Group IDs are different, and the Header
sizes are included in the Group/Chunk sizes.<br/>
```
 Group Header:
  000h 4     Group ID ("hTIX","hFNT","hMBD","hHBS")
  004h 4     Group Size (total filesize) (little-endian)
  ...  (8)   Unknown extra (0,0,0,0,0Ch,0,0,0)   ;<-- only in "hHBS" files
  ...  ..    Chunk(s)
 Chunk Format:
  000h 4     Chunk Type ("cCLT","cBIT","cSTR","cMAP","cIDX","cVAB","cSEQ")
  004h 4     Chunk Size (SIZ) (little-endian)
  00Ch SIZ-8 Data
  ...  ..    Maybe Zeropadding to boundary? (Chunk Size is always N*4 anyways)
```
ID "hTIX" used by Alice in Cyberland (ALICE.PAC\alice.tpk, csel.tpk, etc.)<br/>
ID "hFNT" used by Alice in Cyberland (ALICE.PAC\alice.tpk, juri.tpk, etc.)<br/>
ID "hMBD" used by Alice in Cyberland (ALICE.PAC\\*.FA2\\*.MBD)<br/>
ID "hHBS" used by Alice in Cyberland (ALICE.PAC\0x\_xx.HBS)<br/>

#### Touring Car Championship (MagDemo09: TCAR\GAME\\*\\*.BFX)
#### Jarret & LaBonte Stock Car Racing (MagDemo38: WTC\\*\\*.BFX)
Contains several simple chunks:<br/>
```
  000h 4     Chunksize in bytes (SIZ) (usually a multiple of 4)
  004h SIZ   Chunkdata (eg. .TIM file or other stuff)
```
There is no end-marker in last chunk (it simply ends at total filesize).<br/>

#### Colony Wars Venegance (MagDemo14: CWV\GAME.RSC\VAG.WAD)
#### Colony Wars Red Sun (MagDemo31: CWREDSUN\GAME.RSC\0002\VAG\_WAD)
Contains several simple chunks with filenames:<br/>
```
  000h 0Ch   Chunk Filename ("filename.ext", zeropadded if shorter)
  00Ch 4     Chunk Data Size in bytes (SIZ)
  010h SIZ   Chunk Data (usually VAGp files, in VAG.WAD)
```
There is no end-marker in last chunk (it simply ends at total filesize).<br/>
Red Sun VAG\_WAD is a bit odd: The "extension" is \_WAD instead .WAD, the chunk
names include prefix "RedSun\", which leaves only 5 chars for the actual name,
causig duplicated names like "RedSun\laser" (which were supposedly meant to be
named laser1, laser2, laser3 or the like), and many of the Red Dun VAG files
contain damaged 30h-byte VAG header entries, eg. zero instead of ID "VAGp").<br/>

#### Mat Hoffman's Pro BMX (new demo) (MagDemo48: MHPB\STILLS.BIN)
Contains .BS files in several chunks:<br/>
```
  000h ..    Chunk(s) (.BS files with extra header info)
  ...  4     End Marker (00000000h)
 Chunk format:
  000h 4     Chunk size (including whole chunk header)
  004h 2     Bitmap Width  (eg. F0h)
  006h 2     Bitmap Height (eg. 80h)
  008h 2     Data Size/4 (same as (Chunksize-0Ch-filenamelen)/4)
  00Ah 2     MDEC Size/4 (same as at Data[0])
  00Ch ..    Filename (eg. "lsFact",00h or "bsRooftop1",00h)  ;\filename field
  ...  ..    Filename Zeropadding to 4-byte boundary          ;/
  ...  ..    Data (in BS v2 format) (MDEC Size/4, BS ID 3800h, etc.)
```
Note: STILLS.BIN exists in newer BMX demo in MagDemo48 only (not in MagDemo39).<br/>

#### Ridge Racer (TEX\*.TMS)
#### Ridge Racer Revolution (BIG\*.TMS)
#### Ridge Racer Type 4 (MagDemo19+21: R4DEMO\R4.BIN\\*\\*)
```
  000h 4     ID (100h)
  004h ..    Chunk(s)
  ...  4     Zero (Chunk Size=0=End)
  ...  ..    Optional zeropadding to 800h-byte boundary (in R4.BIN\*)
```
Chunk Format:<br/>
```
  000h 4     Chunk Size (SIZ)
  004h SIZ   Chunk Data (TIM file) (note: includes 0x0pix TIMs with palette)
```

#### Jet Moto 2 (MagDemo03: JETMOTO2\\*.TMS)
#### Twisted Metal 2 (MagDemo50: TM2\\*.TMS)
Contains a fileheader and .TIM files in several chunks:<br/>
```
  000h 8     ID "TXSPC",0,0,0 (aka CPSXT backwards)
  008h 4     Timestamp? (32A5C8xxh)
  00Ch 4     Number of Chunks (N) (can be 0=None, eg. TM2\SCREEN\ARROWS.TMS)
  010h N*4   Unknown
  ...  N*var Chunks
 Chunk format:
  000h 4     Chunk Size-4 (SIZ)
  004h SIZ   Chunk Data (TIM file)
```

#### Princess Maker - Yumemiru Yousei (BDY\\*.BD and PM.\*)
The BDY\\*.BD files do simply contain several chunks:<br/>
```
  000h ..   Chunk(s)
```
The PM.\* files do contain several "folders" with fixed size:<br/>
```
  000h ..   Chunk(s) for 1st folder              ;\Foldersizes are:
  ...  ..   Zeropadding to Foldersize-boundary   ;  20000h (PM.DT0 and PM.PCC)
  ...  ..   Chunk(s) for 2nd folder              ;  28000h (PM.MAP)
  ...  ..   Zeropadding to Foldersize-boundary   ;  42000h (PM.SD0)
  ...  ..   etc.                                 ;/
```
Chunk Format:<br/>
```
  000h 4    Chunk ID   (800000xxh)
  004h 4    Chunk Size (size of Data part, excluding ID+Size)
  008h ..   Data
```
The Data for different Chunk IDs does usually have a small header (often with
w,h,x,y entries, aka width/height, vram.x/y) followed by the actual data body:<br/>
```
  80000004h  x(2),y(2),width(2),height(2)    Bitmap 8bpp          ;PM.PCC,MAP
  80000005h  w(2),h(2),zero(4)               Array32bit(w,h)      ;PM.MAP
  80000006h  x(2),width(2)                   Bitmap Palette       ;PM.*
  80000007h  x(2),y(2),w(1),h(1),zero(2)     Array8bit(w,h)       ;PM.MAP
  80000010h  width(2),height(2),x(2),y(2)    Bitmap 16bpp         ;*.BD
  80000012h  zero(0)                         ?                    ;*.BD
  80000014h  x(2),y(2),width(2),height(2)    Bitmap 4bpp          ;PM.DT0
  80000016h  x(2),y(2),w(1),h(1),n(1),3Fh(1) BitmapArray4bpp(n*2) ;PM.DT0
  80000018h  ...                             ?                    ;PM.PCC
  8000001Ah  zero(8)                         ?                    ;PM.PCC
  8000001Ch  x(2),y(2),width(2),height(2)    Bitmap 1bpp flags?   ;*.BD
  80000020h  zero(8)                         Sound .SEQ file      ;PM.SD0
  80000021h  zero(8)                         Sound .VH file       ;PM.SD0
  80000022h  zero(8)                         Sound .VB file       ;PM.SD0
  80000024h  x(2),zero(6)                    ?                    ;PM.DT0\4\0
  00000000h  Zeropadding to next folder      Zeropadding          ;PM.*
```

#### Project Horned Owl (COMDATA.BIN, DEMODATA.BIN, ROLL.BIN, ST\*DATA.BIN)
```
  000h ..    Chunks
```
Chunk Format:<br/>
```
  000h 1     Chunk Type (see below)
  001h 3     Unknown (some flags or file ID, or zero in many files)
  004h 4     Chunk Size (SIZ)
  008h SIZ   Chunk Data (eg. SEQ file)
```
Chunk Type values:<br/>
```
  02h  unknown                      ST*.BIN
  05h  .TXT                         ROLL.BIN
  05h  LZ-compressed TIM            DEMODATA.BIN, ST*.BIN (except ST1*.BIN)
  06h  DOT1 with stuff and TSQ??    ST*.BIN
  07h  .TMD                         DEMODATA.BIN, ST*.BIN (except ST1*.BIN)
  08h  unknown                      ST*.BIN
  09h  "PRM:"                       ST*.BIN
  0Ah  unknown                      ST*.BIN
  0Bh  DOT1 with stuff              ST*.BIN (except ST1*.BIN) (odd: ST3*.BIN)
  0Ch  .SEQ                         ROLL.BIN, ST*.BIN
  0Dh  unknown                      COMDATA.BIN
  0Eh  unknown                      ST*.BIN
  0Fh  DOT1 with LZ-compressed TIMs ST*.BIN
  10h  DEFLATE-compressed TIM       COMDATA.BIN, ROLL.BIN, ST*.BIN
  11h  DOT1 with stuff              ST*.BIN
  Note: Type=05h can be uncompressed TXT or compressed TIM.
```
For detection, the existing .BIN files start with following values:<br/>
```
  07 00 00 00 xx xx 00 00 41 00 00 00 ..   TMD Model ("A")
  0C 00 00 00 xx xx 00 00 70 51 45 53 ..   SEQ Midi  ("pQES")
  0E xx 00 00 08 00 00 00 xx xx xx xx ..   Whatever in ST7DATA.BIN (see note)
  10 01 00 00 24 28 00 00 EC 9B 7F 70 ..   Deflated TIM in COMDATA.BIN
  10 08 1A 00 30 0C 00 00 ED 58 4F 88 ..   Deflated TIM in ROLL.BIN
  ST7DATA.BIN has 2 chunks with Type=0Eh, followed by SEQ chunk at offset=20h.
```
TIMs are compressed via HornedLZ (Type=05h,0Fh) or Deflate (Type=10h).<br/>
[CDROM File Compression HornedLZ](cdromfileformats.md#cdrom-file-compression-hornedlz)<br/>
[CDROM File Compression ZIP/GZIP/ZLIB (Inflate/Deflate)](cdromfileformats.md#cdrom-file-compression-zipgzipzlib-inflatedeflate)<br/>
The game's Inflate function does ignore the 2bit blocktype: All blocks must
have dynamic trees (fixed trees and uncompressed blocks aren't supported).<br/>

#### Blaster Master (DATA\\*.IDX, DATA\\*.DAT)
DATA\GRP.IDX, DATA\MAP.IDX, DATA\SEQ.IDX DATA\VAB.IDX:<br/>
```
  000h N*2  Chunk List (16bit Offset/800h to Part-1-Chunks in .DAT files)
  ...  ..   Zeropadding to 800h-byte boundary
  Notes:
  The Chunk List can contain zeroes (as first entry at offset 0, and as
  unused entries; in VAB.IDX those can be followed by further USED entries).
  For 2-part DAT files, the Chunk List contains offsets for Part 1 only.
```
DATA\SEQ.DAT:<br/>
```
  000h 4    Chunksize/800h                                           ;\
  004h 4    Datasize in bytes                                        ; Single
  008h 4    Always 015A5A01h or 015A5A00h                            ; Part
  00Ch 4    Always 2803h                                             ; with
  010h ..   Midi data .SEQ file                                      ; 1 file
  ...  ..   Zeropadding to 800h-byte boundary                        ;/
```
DATA\VAB.DAT:<br/>
```
  000h 4    Chunksize/800h                                           ;\
  004h 4    Size of .VH Voice Header in bytes                        ; Single
  008h 4    Size of .VB Voice Binary in bytes                        ; Part
  00Ch ..   Voice Header .VH file                                    ; with
  ...  ..   Zeropadding to 800h-byte boundary                        ; 2 files
  ...  ..   Voice Binary .VB file                                    ;
  ...  ..   Zeropadding to 800h-byte boundary                        ;/
```
DATA\GRP.DAT and DATA\MAP.DAT:<br/>
```
  000h 4    Part 1 Chunksize/800h                                    ;\
  004h 4    Size of all TIM files in bytes (can be 0=None)           ; Part 1
  008h ..   Texture data (several TIMs appended after each other)    ;
  ...  ..   Zeropadding to 800h-byte boundary                        ;/
  ...  4    Number of Files (N)                                      ;\
  ...  4    Part 2 Chunksize/800h                                    ;
  ...  N*8  File List                                                ; Part 2
  ...  ..   Garbage-padding to 800h-byte boundary?                   ;
  ...  ..   File Data area (each file Garbage-padded to 800h-byte)   ;
 File List entries:                                                  ;
  000h 4    File Type/ID                                             ;
  004h 4    Size in bytes                                            ;/
```
The DAT files are chunk-based (unfortunately, each DAT file is using its own
chunk format, some of them are using 2-part chunks).<br/>
The DAT chunks can be parsed without using the IDX file (the IDX can be helpful
for quick lookup, but even then, one will still need to parse the DAT chunk
headers to find the actual contents like TIM, SEQ, VB, VH files).<br/>

#### See also
[CDROM File Archive Darkworks Chunks (Alone in the Dark)](cdromfileformats.md#cdrom-file-archive-darkworks-chunks-alone-in-the-dark)<br/>
[CDROM File Archive Blue Chunks (Blue's Clues)](cdromfileformats.md#cdrom-file-archive-blue-chunks-blues-clues)<br/>
[CDROM File Archive HED/CDF (Parasite Eve 2)](cdromfileformats.md#cdrom-file-archive-hedcdf-parasite-eve-2)<br/>
[CDROM File Compression LZSS (Serial Experiments Lain)](cdromfileformats.md#cdrom-file-compression-lzss-serial-experiments-lain)<br/>
[CDROM File Compression SLZ/01Z (chunk-based compressed archive)](cdromfileformats.md#cdrom-file-compression-slz01z-chunk-based-compressed-archive)<br/>



##   CDROM File Archives with Folders
There are several ways to implement folder-like directory trees:<br/>
```
  - Using multiple archive files nested within each other
  - Using filenames with path string (eg. "path\filename.ext")
```
Other than that, below are special formats with dedicated folder structures.<br/>

#### Archives with Folders
[CDROM File Archive HUG/IDX/BIZ (Power Spike)](cdromfileformats.md#cdrom-file-archive-hugidxbiz-power-spike)<br/>
[CDROM File Archive TOC/DAT/LAY](cdromfileformats.md#cdrom-file-archive-tocdatlay)<br/>
[CDROM File Archive WAD (Doom)](cdromfileformats.md#cdrom-file-archive-wad-doom)<br/>
[CDROM File Archive WAD (Cardinal Syn/Fear Effect)](cdromfileformats.md#cdrom-file-archive-wad-cardinal-synfear-effect)<br/>
[CDROM File Archive DIR/DAT (One/Viewpoint)](cdromfileformats.md#cdrom-file-archive-dirdat-oneviewpoint)<br/>
[CDROM File Archive HED/CDF (Parasite Eve 2)](cdromfileformats.md#cdrom-file-archive-hedcdf-parasite-eve-2)<br/>
[CDROM File Archive IND/WAD (MTV Music Generator)](cdromfileformats.md#cdrom-file-archive-indwad-mtv-music-generator)<br/>
[CDROM File Archive GAME.RSC (Colonly Wars Red Sun)](cdromfileformats.md#cdrom-file-archive-gamersc-colonly-wars-red-sun)<br/>
[CDROM File Archive BIGFILE.DAT (Soul Reaver)](cdromfileformats.md#cdrom-file-archive-bigfiledat-soul-reaver)<br/>
[CDROM File Archive FF8 IMG (Final Fantasy VIII)](cdromfileformats.md#cdrom-file-archive-ff8-img-final-fantasy-viii)<br/>
[CDROM File Archive FF9 IMG (Final Fantasy IX)](cdromfileformats.md#cdrom-file-archive-ff9-img-final-fantasy-ix)<br/>
[CDROM File Archive GTFS (Gran Turismo 2)](cdromfileformats.md#cdrom-file-archive-gtfs-gran-turismo-2)<br/>
[CDROM File Archive Nightmare Project: Yakata](cdromfileformats.md#cdrom-file-archive-nightmare-project-yakata)<br/>
[CDROM File Archive FAdj0500 (Klonoa)](cdromfileformats.md#cdrom-file-archive-fadj0500-klonoa)<br/>
See also: PKG (a WAD.WAD variant with folders)<br/>

#### Perfect Assassin (\*.JFS)
```
 Overall File Structure
  JFS for root                                   ;\
  JFS for 1st folder   ;\these are dupicated,    ; header with complete list
  JFS for 2nd folder   ; also stored in below    ; of all file/folder names
  JFS for 3rd folder   ; data area               ;
  etc.                 ;/                        ;/
  JFS for 1st folder, plus data for files in that folder  ;\
  JFS for 2nd folder, plus data for files in that folder  ; data area
  JFS for 3rd folder, plus data for files in that folder  ;
  etc.                                                    ;/
```
JFS Headers (0Ch+N\*14h bytes)<br/>
```
  00h 4     ID "JFS",00h
  04h 4     Size in bytes (for root: including nearby child JFS's)
  08h 4     Number of file/folder entries in this folder (N)
  0Ch N*14h File/Folder entries
```
File Entries (with [10h].bit31=0):<br/>
```
  00h 12  "FILENAME.EXT" (or zeropadded if shorter)
  0Ch 4   Offset from begin of JFS in data area (without any alignment)
  10h 4   Size in bytes, plus 00000000h=File
```
Folder Entries (with [10h].bit31=1):<br/>
```
  00h 12  "DIRNAME.EXT" (or zeropadded if shorter)
  0Ch 4   Offset to child JFS in data area
  10h 4   Offset to child JFS in header area, plus 80000000h=ChildFolder
```
The JFS format is almost certainly unrelated to IBM's "Journaled File System".<br/>

#### Alone in the Dark The New Nightmare (FAT.BIN=Directory, and DATA.BIN=Data)
```
 FAT.BIN:
  00h 2     Number of folders (X) (43h)
  02h 2     Number of files   (Y) (8F0h)
  04h 4     Unknown               (1000h)
  08h X*10h Directory Entry 0000h..X-1 (entry 0000h is named "ROOT")
  ..  Y*10h File Entry 0000h..Y-1
 DATA.BIN:
  00h ..    File Data area
```
Directory Entries (10h bytes):<br/>
```
  00h 8    Name (terminated by 00h if less than 8 chars)
  08h 2    First Subdirectory number (0001h and up, 0000h would be root)
  0Ah 2    Number of Subdirectories  (0000h=None, if so above is usually 00FFh)
  0Ch 2    First File number         (0000h and up)
  0Eh 2    Number of files           (0000h=None, if so above is usually 00FFh)
```
File Entries (10h bytes):<br/>
```
  00h 8    Name (terminated by 00h if less than 8 chars)
  08h 4    Offset/800h to DATA.BIN
  0Ch 4    Size in bytes (when compressed: decompressed size+02000000h)
```
Compressed files (in LEVELS\\*\\* with Size.bit25=1) can be decompressed as so:<br/>
[CDROM File Compression Darkworks](cdromfileformats.md#cdrom-file-compression-darkworks)<br/>
The files include some TIM images, WxH images, binary files, and chunks:<br/>
[CDROM File Archive Darkworks Chunks (Alone in the Dark)](cdromfileformats.md#cdrom-file-archive-darkworks-chunks-alone-in-the-dark)<br/>

#### Interplay Sports Baseball 2000 (MagDemo22: BB2000\\* HOG.DAT and HOG.TOC)
```
 HOG.TOC:
  000h N*14h Folder/File List (starting with root folder)
 HOG.DAT:
  000h ..    File Data (referenced from HOG.TOC)
```
Folder entries:<br/>
```
  000h 1     Type      ("D"=Directory)
  001h 8     Name      ("FILENAME", zeropadded if shorter) (or "\" for root)
  009h 3     Extension (usually zero for directories)
  00Ch 4     Folder Offset/14h in .TOC file (aka 1st child file/folder index)
  010h 4     Folder Size/14h                (aka number of child files/folders)
```
File entries:<br/>
```
  000h 1     Type      ("F"=File)
  001h 8     Name      ("FILENAME", zeropadded if shorter)
  009h 3     Extension ("EXT", zeropadded if shorter)
  00Ch 4     File Offset/800h in .DAT file (increasing)
  010h 4     File Size in bytes
```

#### Tenchu 2 (MagDemo35: TENCHU2\VOLUME.DAT)
```
  000h 4     Unknown (demo=A0409901h, us/retail=A0617023h)
  004h 4     Unknown (0h)
  008h 4     Number of files   (F) (demo=B7h, us/retail=1294h)
  00Ch 4     Number of folders (D) (demo=0Fh, us/retail=3Eh)
  010h D*8   Folder List
  ...  ..    Zerofilled (padding to 800h-byte boundary)
  800h F*10h File List
  ...  ..    Zerofilled (padding to 800h-byte boundary)
  ...  ..    File Data area
```
Folder List entries:<br/>
```
  000h 4     Folder ID (Random, maybe folder name checksum?)
  004h 4     First file number in this folder (0=first, increasing)
```
File List entries:<br/>
```
  000h 4     File Offset/800h
  004h 4     File Size in bytes
  008h 4     Folder ID (same as Parent Folder ID in Folder List)
  00Ch 4     File ID (Random, maybe file name checksum?)
```

#### Blasto (MagDemo10: BLASTO\BLASTO.DAT and BLASTO\BLASTO.LFS)
```
 LFS:
  000h N*18h File/Folder List
 DAT:
  000h ..    File data
```
File entries (with [10h]=Positive):<br/>
```
  000h 10h   Filename ("FILENAME.EXT", zeropadded)
  010h 4     Offset in bytes, in BLASTO.DAT
  014h 4     Size in bytes
```
Folder entries (with [10h]=Negative):<br/>
```
  000h 10h   Foldername ("DIRNAME", zeropadded)
  010h 4     Index to first child (at Offset=(-Index)*18h in BLASTO.LFS)
  014h 4     Zero
```
Folder end marker (with [00h]=00h or 80h):<br/>
```
  000h 1     End marker, at end of root & child directories (00h or 80h)
  001h 17h   Unknown
```

#### Twisted Metal 4 (MagDemo30: TM4DATA\\*.MR and \*.IMG)
These are relative small archives with hundreds of tiny chunks (with registry
style Symbol=Value assignments), and a few bigger chunks (with .mod .vab .bit
.clt files).<br/>
```
  000h 4     Fixed ID (CCCC0067h)
  004h ..    Root Folder (with Name="Root",00h,FDh,FDh,FDh)
 Folder Chunk format:
  000h 1     Length of Name (including 4-byte padding)
  001h 1     Number of Child Folders
  002h 2     Number of Child Files
  004h ..    Name ("name",00h, CDh-padded to 4-byte boundary; Root=FDh-padded)
  ...  ..    Child File(s)
  ...  ..    Child Folder(s)
 File Chunk format:
  000h 1     Length of filename (including 4-byte padding)
  001h 1     Filetype           (see below)
  002h 2     Array Size         (or FFFFh for non-array filetypes)
  004h 4     Filesize (SIZ)     (including 4-byte padding)
  008h 4     Decompressed Size  (or 0=Uncompressed)
  00Ch ..    Filename/Symbol    ("name.ext",00h, CDh-padded to 4-byte boundary)
  ...  SIZ   Data/Value         (CDh-padded to 4-byte boundary)
```
Some filenames have trailing non-ascii characters, for example:<br/>
```
  "AXEL.MR\display\resolution\r3\Groups\Combined_Polyset",1Ah,01h,04h,00h
  "CALYPSO.MR\display\resolution\r3\Groups\Combined_Polyset",A8h,00h, CDh,CDh
```
Filetypes:<br/>
```
  Typ Size  Expl.
  02h var   Text String (terminated by 00h, garbage-or-00h-padded to 4-byte)
  03h 8     Misc (*.IMG\textures\*)                          ;\
  03h 20h   Misc (*.MR\display\resolution\r*\Groups\*)       ; these are all
  03h var   Misc (*.MR\display\resolution\*List)             ; filetype=03h
  03h file  Misc (*.MR\display\*.bit) (same as type=0Ch)     ;/
  04h 4     Numeric 32bit
  05h 8     Numeric 4x16bit point (X,Y,Z,CDCDh)
  06h file  Model (*.mod) (DOTLESS archive with model data)
  0Bh 4     Numeric 32bit repeat,light
  0Ch file  XYWH Bitmap/Palette (*.bit, *.clt) (in GAME.IMG, MENU\menu)
  0Dh 4     Numeric 32bit delay
  0Eh 4     Numeric 32bit color (maybe 24bit RGB plus 00h-padding?)
  0Fh 10h   Whatever 10h-byte "pos"
  10h file  Sony .VAB file (*.vab)
  12h N*1   Array? (with Arraysize=0014h)
  16h N*??  Array Text Strings (with Arraysize=0001h) (in MAIN.MR\worlds)
  1Ah N*10h Array Guns,startpoints (RCCAR.MR\*, NEON.MR\world)
  1Bh 4     Numeric 2x16bit (X,Y) (in MENU.MR)
  1Ch N*4   Array lloc (in MENU.MR\menu\screens) (with Arraysize=04h or 1Fh)
  25h 8     Whatever 8-byte (in GAME.MR\dualShock)
  26h N*8   Array CollideArray (in GAME.MR\dualShock) (with Arraysize=4 or 6)
```
Compressed Data (when [008h]\<\>0):<br/>
```
  000h ..    ZLIB compressed data (usually starting with big-endian 789Ch)
  (compression is used for almost all files, except VERY small ones)
```
[CDROM File Compression ZIP/GZIP/ZLIB (Inflate/Deflate)](cdromfileformats.md#cdrom-file-compression-zipgzipzlib-inflatedeflate)<br/>



##   CDROM File Archive HUG/IDX/BIZ (Power Spike)
#### Power Spike (MagDemo43: POWER\GAME.IDX and .HUG)
POWER\GAME.HUG<br/>
```
  000h ..    File Data
```
POWER\GAME.IDX<br/>
```
  000h 4     ID "HUGE"
  004h 4     Checksum (sum of all bytes at [010h and up])
  008h 4     Number of Folders (D) (87h)
  00Ch 4     Number of Files   (F) (F9h)
  010h D*1Ch Folder List (Folder 0..D-1)
  ...  F*18h File List   (File 0..F-1)
```
Folder List entries:<br/>
```
  000h 0Ch   Folder Name ("DIRNAME", zeropadded)
  00Ch 4     First Child File      (or FFFFFFFFh=None)
  010h 4     Number of Child Files (or 00000000h=None)
  014h 4     First Child Folder    (or FFFFFFFFh=None)
  018h 4     Next Sibling Folder   (or FFFFFFFFh=None)
```
File List entries:<br/>
```
  000h 0Ch   File Name ("FILENAME.EXT", zeropadded if shorter than 12)
  00Ch 4     File Checksum (sum of all bytes in file added together)
  010h 4     File Offset/800h in GAME.HUG
  014h 4     File Size in bytes
```
The root entries are Folder 0 (and its siblings). That is, the root can contain
only folders (not files).<br/>
The IDX/HUG archive contains many BIZ archives (and some TXT files).<br/>

#### Power Spike (MagDemo43: POWER\GAME.IDX\\*.BIZ) (BIZ nested in IDX/HUG)
```
  000h 4     ID "BIG!"
  004h 4     Number of entries (N)
  008h N*1Ch File List
  ...  ..    BIZ compressed File Data
```
File List entries<br/>
```
  000h 10h   Filename (zeropadded)
  010h 4     File Offset (increasing, unaligned, can be odd)
  014h 4     File Size decompressed
  018h 4     File Size compressed
```
All files in the BIZ archive are BIZ compressed (unknown if it does also
support uncompressed files).<br/>
[CDROM File Compression LZ5 and LZ5-variants](cdromfileformats.md#cdrom-file-compression-lz5-and-lz5-variants)<br/>
The BIZ archive seems to be solely containing PSI bitmaps (even files in
GAME.IDX\SOUND\MUSIC\\*.BIZ do merely contain PSI bitmaps, not audio files).<br/>



##   CDROM File Archive TOC/DAT/LAY
Used in PSX Lightspan Online Connection CD (CD.TOC, CD.DAT, CD.LAY).<br/>
```
  CD.TOC contains File/Folder entries
  CD.DAT contains the actual File bodies
  CD.LAY devkit leftover (list of filenames to be imported from PC to TOC/DAT)
```
The .TOC file doesn't have any file header, it does just start with the first
File/Folder folder entry in root directory. The directory chains with
file/folder entries are sorted alphabetically, each chain is terminated by a
final entry which does point to parent directory.<br/>

#### File Entries
```
  00h 4   Offset to next Sibling File/Folder/Final entry
  04h 4   Filesize in bytes
  08h 4   Filedata Offset/800h in CD.DAT
  0Ch ..  Filename (ASCII, terminated by 00h)
  ... ..  Padding to 4-byte boundary (garbage)
```

#### Folder Entries (with Filesize=FFFFFFFFh)
```
  00h 4   Offset to next Sibling File/Folder/Final entry
  04h 4   Filesize (always FFFFFFFFh in Folder entries)
  08h 4   Offset to first File/Folder in Child directory
  0Ch ..  Name of Child directory (ASCII, terminated by 00h)
  ... ..  Padding to 4-byte boundary (garbage)
```

#### Final Entries (with Name="",00h and Filesize=FFFFFFFxh)
```
  00h 4   Offset to next Sibling entry (00000000h=None)
  04h 4   Filesize (FFFFFFFFh in child folders, FFFFFFFEh in root folder)
  08h 4   Offset to first File/Folder in Parent directory (or to self for root)
  0Ch 1   Empty Name ("",00h)
  0Dh 3   Padding to 4-byte boundary (garbage)
```



##   CDROM File Archive WAD (Doom)
#### Doom, PSXDOOM\ABIN\\*.WAD and PSXDOOM\MAPDIR\*\\*.WAD)
The .WAD format is used by Doom (for DOS, Jaguar, PSX, etc), various homebrew
Doom hacks, and some other developers have adopted the format and used .WAD in
other game engines.<br/>
```
  000h 4     ID "IWAD" (or "PWAD" for homebrew patches, or "PACK" in A.D. Cop)
  004h 4     Number of File List entries (N) (including final ENDOFWAD entry)
  008h 4     Offset to Directory Area (filesize-N*10h)
  00Ch ..    File Data area
  ...  N*10h File List
```
File List entries:<br/>
```
  000h 4   Offset to file data (increasing by compressed size, 4-byte aligned)
  004h 4   Filesize in bytes   (uncompressed size) (zero in ENDOFWAD file)
  008h 8   Filename (uppercase ASCII, zeropadded if less than 8 chars)
```

#### Folders
The directory can contain names like F\_START, F\_END, P1\_START, P1\_END with
filesize=0 to mark begin/end of something; that stuff can be considered as
subdirectories with 1- or 2-character names.<br/>
Notes: There are also regular files with underscores which are unrelated to
folders (eg. F\_SKY01). There are also 0-byte dummy files (eg. MAP17 in first
entry MAP17.WAD). And there's a 0-byte dummy file with name ENDOFWAD in last
file list entry (at least, it's present versions with compression support).<br/>

#### LZSS Decompression
Compression is indicated by Filename[0].bit7=1. The compressed size is
NextFileOffset-FileOffset (that requires increasing offsets in File List,
including valid offsets for 0-byte files like F\_START, F\_END, ENDOFWAD).<br/>
```
  @@collect_more:
   flagbits=[src]+100h, src=src+1    ;8bit flags
  @@decompress_lop:
   flagbits=flagbits SHR 1
   if zero then goto @@collect_more
   if carry=0 then
     [dst]=[src], dst=dst+1, src=src+1
   else
     disp=([src]*10h)+([src+1]/10h)+1, len=([src+1] AND 0Fh)+1, src=src+2
     if len=1 then goto @@decompress_done
     for i=1 to len, [dst]=[dst-disp], dst=dst+1, next i
   endif
   goto @@decompress_lop
  @@decompress_done:
   ret
```
The game engine may insist on some files to be compressed or uncompressed (so
compression may be required even if the uncompressed data would be smaller).<br/>

More info: [http://doomwiki.org/wiki/WAD]




##   CDROM File Archive WAD (Cardinal Syn/Fear Effect)
#### .WAD files (Cardinal Syn/Fear Effect)
This format exists in two version:<br/>
```
  Old format: Without leading Header Size entry (Cardinal Syn MagDemo03: SYN\*)
  New format: With leading Header Size entry    (eg. Fear Effect)
```
Version detection could be done somewhat as so:<br/>
```
  if [04h]*1Ch+8 >= [00h] then OLD version
```
For loading the Old Header, one must guess the max header size (4000h should
work, in fact, most or all Old Headers seem to be max 800h), or load more data
on the fly as needed.<br/>
```
  000h (4) Header Size (including folder/type/file directories) (new version)
  ...  4   Number of Folders
  ...  ..  Folder List (root)
  ...  ..  Type Lists  (for each folder)
  ...  ..  File Lists  (for each folder\type)
  ...  ..  File Data   (for each folder\type\file)
 Folder List Entries:
  000h 14h Folder name (ASCII, zeropadded)
  014h 4   Offset to Type List
  018h 4   Number of different Types in this folder
 Type List Entries:
  000h 4   Offset to file entries (of same type, eg. .TIM files)
  004h 4   Number of file entries (of same type, eg. .TIM files)
  008h 4   Sum of all Filesizes with that type
  00Ch 4   Group Type (0000000xh)
 File List entries (Files within Type list):
  000h 14h Name (ASCII, terminated by 00h, plus garbage padding)
  014h 4   Offset to File Data  (seems 4-byte aligned... always?)
  018h 4   File Type (000x00xxh)
  01Ch 4   Filesize in bytes  ;\maybe compressed/uncompressed, or rounded,
  020h 4   Filesize in bytes  ;/always both same
```
Note: The Type List for one folder can contain several entries with same Group
Type, eg. Fear Effect GSHELLE.WAD\CREDIT has 5 type list entries (with
2xGroup0, 2xGroup1, 1xGroup2).<br/>

The Type List, Group Type and File Type stuff seems to have no function, apart
from faster look up (the types are also implied in the filename extension).
Except, Fear Effect .RMD .VB .VH have some unknown stuff encoded in File Type
bit16-19.<br/>
Group Type is usually 0 (except for .TIM .VB .VH .MSG .SPU .OFF).<br/>
The .TIM .VB .VH .SEQ files are using standard Sony file formats. The .PMD file
seems to be also Sony standard (except that it contains a 00000000h prefix,
then followed by the 00000042h PMD format ID).<br/>

#### Cardinal Syn Types
```
  .BGD FileType=00000001h
  .ANM FileType=00000003h
  .TIM FileType=00000004h (GroupType=1)
  .SP2 FileType=00000005h
  .PMD FileType=00000007h
  .MOV FileType=00000008h
  .SPR FileType=0000000Ch
  .PVT FileType=0000000Dh
  .DB  FileType=0000000Eh
  .VH  FileType=00000010h (GroupType=1) ;only in OLDER demo version MagDemo03
  .VB  FileType=00000011h (GroupType=1)
  .MSG FileType=00000012h (GroupType=1) (actually, this is .TIM, too)
  .KMD FileType=00000013h
  .OC  FileType=00000018h
  .EMD FileType=00000019h
  .COL FileType=0000001Bh
  .CF  FileType=0000001Ch
  .CFB FileType=0000001Dh
  .CL  FileType=0000001Eh
  .SPU FileType=0000001Fh (GroupType=1) ;added in newer demo version MagDemo09
  .OFF FileType=00000020h (GroupType=1) ;added in newer demo version MagDemo09
  .RCT FileType=00000021h               ;added in newer demo version MagDemo09
```

#### Fear Effect Types
```
  .TIM FileType=00000000h (GroupType=1)
  .RMD FileType=000x0001h
  .DB  FileType=00000002h
  .ANM FileType=00000003h
  .SYM FileType=00000004h
  .VB  FileType=000x0008h (GroupType=1)
  .SEQ FileType=00000010h
  .BIN FileType=00000012h
  .SFX FileType=00000013h
  .VH  FileType=000x0014h (GroupType=2)
  .TM  FileType=00000015h
  .NRM FileType=00000017h
  .WPD FileType=00000018h
```



##   CDROM File Archive DIR/DAT (One/Viewpoint)
#### DIR/DAT (One/Viewpoint)
```
  Used by One (DATAFILE.BIN and DIRFILE.BIN)
  Used by Viewpoint (VIEW.DAT and VIEW.DIR)
```
Format of the DIR file:<br/>
```
  000h 60h Extension List (20h x 3-char ASCII, zeropadded if shorter than 3)
  060h ..  Root Directory    (can contain folders and files)
  ...  ..  Child Directories (can contain files) (maybe also sub-folders?)
```
Extension List contains several uppercase 3-character ASCII extensions, in a
hex editor this will appear as a continous string of gibberish (dots=00h):<br/>
```
  In Viewpoint: "...VCSVCFBINTXTVH.VB.STRST1ST2ST3......//..."
  In One:       "...VCTVCKSNDBINCPEINI..................//..."
```
Directory Entries contain bitstreams with ASCII characters squeezed into 6bit
values:<br/>
```
  000h 1   Length of Filename and Extension index
             bit7-3  File Extension Index (0..1Fh = Offset I*3 in DIR file)
             bit2-0  Filename Length-1    (0..7 = 1..8 chars)
  001h ..  Filename in 6bit chars (N*6+7/8 bytes = 1..6 bytes for 1..8 chars)
             bit7-2  1st character, whole 6bit            ;\1st byte
             bit1-0  2nd character, upper 2bit (if any)   ;/
             bit7-4  2nd character, lower 4bit (if any)   ;\2nd byte (if any)
             bit3-0  3rd character, upper 4bit (if any)   ;/
             bit7-6  3rd character, lower 2bit (if any)   ;\3rd byte (if any)
             bit5-0  4th character, whole 6bit (if any)   ;/
             bit7-2  5th character, whole 6bit (if any)   ;\4th byte (if any)
             bit1-0  6th character, upper 2bit (if any)   ;/
             bit7-4  6th character, lower 4bit (if any)   ;\5th byte (if any)
             bit3-0  7th character, upper 4bit (if any)   ;/
             bit7-6  7th character, lower 2bit (if any)   ;\6th byte (if any)
             bit5-0  8th character, whole 6bit (if any)   ;/
             bitN-0  Zeropadding in LSBs of last byte     ;-zeropadding
           The 6bit characters codes are:
             00h..09h="0..9", 0Ah..23h="a..z", 24h="_", 25h..3Fh=Unused
  ...  4   Filesize and End Flag
             bit31   End of Directory Flag   (0=Not last entry, 1=Last entry)
             bit30-0 Filesize 31bit          (or 0=Child Folder)
  ...  4   Offset and fixed bit
             bit31   Unknown (always 1)
             bit30-0 File Offset in DAT file (or Folder offset in DIR file)
```



##   CDROM File Archive Darkworks Chunks (Alone in the Dark)
#### Alone in the Dark The New Nightmare (FAT.BIN\\*)
The files in FAT.BIN are using a messy chunk format: There's no clear ID+Size
structure. There are 7 different chunk types (DRAM, DSND, MIDB, G3DB, VRAM,
WEAP, HAND), each type requires different efforts to compute the chunk size.<br/>

#### VRAM Chunks (Texture/Palette) (in various files)
```
  000h 4     ID "VRAM"
  004h 4     With Tags (0=No, 1=Yes) (or "DRAM" when empty 4-byte chunk)
  008h (4)   Number of Tagged items (N) (0=None)  ;\only when [4]=1
  00Ch N*10h Tagged Item(s)                       ;/(not so in LEVELS\*\VIEW*)
  ...  ..    Scanline Rows(s)
  ...  4     End code (00000000h) (aka final Scanline Row with width=0)
 Tagged Item(s) (IMG, LINE, GLOW, FLARE, BALLE, BLINK, COURIER7, BMP_xxx):
  000h 8     Tag (ASCII, if less than 8 chars: terminate by 00h, pad by FDh)
  008h 8     Data
 Scanline Row(s) (bitmap scanlines and palette data):
  000h 4     Header (bit0-8=Width, bit10-18=Y, bit20-29=X, bit9,19,30,31=?)
  004h W*2   Data (Width*2 bytes, to be stored at VRAM(X,Y))
```
Empty VRAM chunks can be either 4 or 10h bytes tall. The 4-byte variant is
directly followed by another chunk name (eg. "VRAMDRAM"), the 10h-byte variant
contains four words ("VRAM",WithTags=1,NumTags=0,EndCode=0).<br/>
Note: Some files contain two VRAM chunks (eg. LEVELS\\*\VIEW\*).<br/>

#### G3DB Chunks (Models) (in various files)
```
  000h 4   ID "G3DB"
  004h 4   Unknown (0, 1, or 2)
  008h 4   Size of Data part (SIZ)
  00Ch 4   Number of List entries (eg. 6 or 0Ah or 117Ch) (N)
  010h SIZ Data (supposedly LibGDX models in G3DB format)
  ...  N*4 List
```

#### DRAM Chunks (Text and Binary data) (in various files)
```
  000h 4   ID "DRAM"
  004h 4   Size of Data part (SIZ) (can be odd)
  008h 4   Number of List entries (N)
  00Ch SIZ Data (raw data, and/or tags TEXT, SPC, COURIER7)
  ...  N*4 List
```

#### WEAP Chunks (Weapons) (in WEAPON\\*\\*)
```
  000h 4   ID "WEAP"
  004h 4   Size-10h?
  008h ..  Data
```
Followed by VRAM and DSND chunks.<br/>

#### HAND Chunks (Hands) (in LEFTHAND\\*\HAND\*)
```
  000h 4   ID "HAND"
  004h 4   Size-0Ch?  (18h)
  008h 8   Zerofilled
  010h 4x4 Unknown (FFh,FF00h,xF0000h,FF3232h,FF6464h,FFDCDCh,FFFFFFh,..)
  020h 4   Unknown (0, 1, 101h, or 201h)
```
Followed by VRAM and G3DB chunks.<br/>

#### MIDB Chunks (Music) (in MIDI\\*\\*)
```
  000h 4      ID "MIDB"
  004h 1      Unknown (0 or 1)
  005h 1      Number of SEQ blocks              (1..4) (S)
  006h 1      Number of Unknown 80h-byte blocks (1..2) (U)
  007h U*80h  Unknown Blocks (mostly FFh-filled)
  ...  S*Var  SEQ Block(s)
  ...  ..     VAB Block
 SEQ Blocks:
  Probably some MIDI sequence data, similar to Sony's .SEQ format.
  000h 4      Size-0Ch (can be odd)
  004h 8      Name (zeropadded if less than 8 chars)
  00Ch 4      ID "DSEQ"    ;\Size
  010h ..     Data         ;/
 VAB Blocks:
  Apparently inspired on Sony's .VAB format (but the ID is spelled other way
  around, Lists have variable size, and entries have different format).
  000h 4      ID "VABp"  (this is: not pBAV, unlike normal .VAB files)
  004h 4      Unknown (0)
  008h 4      Unknown (0)
  00Ch 4      Size of all SPU-ADPCM samples (SIZ)
  010h 2      Number of List 1 entries (N1)
  012h 2      Number of List 2 entries (N2)
  014h 2      Number of Samples        (N3)
  016h 6      Unused? (CCh-filled)
  01Ch N1*10h List 1
  ...  N2*10h List 2
  ...  N3*2   Sample Size List (size of each SPU-ADPCM sample)
  ...  SIZ    SPU-APDCM Sample(s)
```

#### DSND Chunks (Sounds) (in various files)
```
  000h 4   ID "DSND"
  004h 4   Unknown (0 or 2)
  008h ..  VAB Block (same as in MIDB chunks, see there)
```

#### Note
DRAM and MIDB chunks can have odd size; there isn't any alignment padding, so
all following chunks can start at unaligned locations.<br/>



##   CDROM File Archive Blue Chunks (Blue's Clues)
#### Blue's Clues: Blue's Big Musical (\*.TXD)
```
  000h 4    Size of AUDD+SEPD+VABB chunks ;\for quick look-up only
  004h 4    Size of all VRAM chunks       ; (can be ignored by chunk crawlers)
  008h 4    Size of STGE+ANIM+FRAM chunks ;/(note: sum is total filesize-0Ch)
  ...  ..   AUDD Chunk    (contains .VH)                  ;\
  ...  ..   SEPD Chunk(s) (contains .SEP)                 ; sound
  ...  ..   VABB Chunk    (contains .VB)                  ;/
  ...  (..) VRAM Chunk(s) (not in IN\FE2.TXD)             ;-textures/palettes
  ...  (..) STGE Chunk    (if any, not in IN\FE*.TXD)     ;-stage data?
  ...  (..) ANIM Chunk    (if any, not in IN\FE*.TXD)     ;\animation
  ...  (..) FRAM Chunk(s) (if any, not in IN\FE*.TXD)     ;/
  ...  (..) Further groups with ANIM+FRAM Chunks (if any) ;-more animation(s)
 AUDD Chunks:
  000h 4    Chunk ID ("AUDD")
  004h 4    Chunk Size (of whole chunk from Chunk ID and up)
  008h 4    Compression Flag (0=Uncompressed)
  00Ch 4    Zero
  010h ..   VH File (Sony Voice Header, starting with ID "pBAV")
 SEPD Chunks:
  000h 4    Chunk ID ("SEPD")
  004h 4    Chunk Size (of whole chunk from Chunk ID and up)
  008h 4    Compression Flag (0=Uncompressed)
  00Ch 2    Zero
  00Eh 2    Number of sequences (in the SEP sequence archive)
  010h 4    Zero
  014h ..   SEP File (Sony Sequence archive, starting with ID "pQES")
  ...  ..   Zeropadding to 4-byte boundary
 VABB Chunks:
  000h 4    Chunk ID ("VABB")
  004h 4    Chunk Size (of whole chunk from Chunk ID and up)
  008h 4    Compression Flag (0=Uncompressed)
  00Ch ..   VB File (Sony Voice Binary, with raw SPU-ADPCM samples)
 VRAM Chunks:
  000h 4    Chunk ID ("VRAM")
  004h 4    Chunk Size (of whole chunk from Chunk ID and up)
  008h 4    Compression Flag (1=Compressed)
  00Ch 2    VRAM.X
  00Eh 2    VRAM.Y
  010h 2    Width in halfwords
  012h 2    Height
  014h 4    Decompressed Size (Width*Height*2)  ;\Texture Bitmaps 8bpp
  018h ..   Compressed Data                     ; (or Palettes, in last VRAM
  ...  ..   Zeropadding to 4-byte boundary      ;/chunk)
 STGE Chunks:
  000h 4    Chunk ID ("STGE")
  004h 4    Chunk Size (of whole chunk from Chunk ID and up)
  008h 4    Compression Flag (0=Uncompressed)
  00Ch ..   Unknown (stage data?)
 ANIM Chunks:
  000h 4    Chunk ID ("ANIM")
  004h 4    Chunk Size (of whole chunk from Chunk ID and up)
  008h 4    Compression Flag (0=Uncompressed)
  00Ch ..   Unknown (animation sequence info?)
 FRAM Chunks:
  000h 4    Chunk ID ("FRAM")
  004h 4    Chunk Size (of whole chunk from Chunk ID and up)
  008h 4    Compression Flag (0=When Chunksize=14h, 1=When Chunksize>14h)
  00Ch 1    Width in bytes
  00Dh 1    Height
  00Eh 6    Unknown, looks like three signed 16bit values (maybe X,Y,Z)?
  014h (4)  Decompressed Size (Width*Height*1)  ;\Animation Frame Bitmap 8bpp
  018h (..) Compressed Data                     ; (only if Chunksize>14h)
  ...  (..) Zeropadding to 4-byte boundary      ;/
```
VRAM and FRAM chunks with [08h]=1 (and Chunksize\>14h) are compressed:<br/>
[CDROM File Compression Blues](cdromfileformats.md#cdrom-file-compression-blues)<br/>



##   CDROM File Archive HED/CDF (Parasite Eve 2)
Crazy Data Format (CDF) is used by Parasite Eve 2, on Disc 1 and 2:<br/>
1: PE\_Disk.01 Stage0.hed Stage0.cdf Stage1.cdf Stage2.cdf Stage3.cdf Inter0.str<br/>
2: PE\_Disk.02 Stage0.hed Stage0.cdf Stage3.cdf Stage4.cdf Stage5.cdf Inter1.str<br/>

#### STAGE0.HED and STAGE0.CDF
This uses separate header/data files. The directory is stored in STAGE0.HED:<br/>
```
  0000h 78h   Streaming List (03h entries, 28h-bytes each, all entries used)
  0078h 1B00h File List (360h entries, 8 bytes each, all entries used)
  1B78b 8     File List End Code (FFFFFFFFh,FFFFFFFFh)
```
The actual data for the files (and audio stream) is stored in STAGE0.CDF.<br/>

#### STAGE1.CDF .. STAGE5.CDF
```
  0000h 800h  Root: Folder List (100h entries, 8-byte each, unused=zeropadded)
  0800h ..    1st Folder (File/Streaming List and Data)
  ...   ..    2nd Folder (File/Streaming List and Data)
  ...   ..    etc.
```
Folder List entries:<br/>
```
  000h 4  Folder ID (usually N*100+1 decimal, increasing, eg. 101,201,301,etc.)
  004h 4  Folder Size/800h (of whole folder, with File/Stream List and Data)
  The Folder List ends with unused/zeropadded entries with ID/Size=00000000h.
```
Folder format:<br/>
```
  0000h 510h  File List      (A2h entries, 8-bytes each, unused=zeropadded)
  0510h 4     Zero           (padding to decimally-minded offset 1300 aka 514h)
  0514h 2D0h  Streaming List (12h entries, 28h-bytes each, unused=zeropadded)
  07E4h 1Ch   Zero           (padding to end of sector)
  0800h ...   Data (for Files, Audio streams, and sometimes also Movie streams)
```

#### File List entries (in STAGE0 and STAGE1-5)
```
  000h 4  File ID (increasing, eg. 0,1,2,3,4,etc.) (or 99) (or N*100+x)
  004h 4  File Offset/800h in in .CDF (from begin of current Folder)
```
For STAGE0, file list ends with ID/Offset=FFFFFFFFh at end of HED file. For
STAGE1-5, file list ends with unused/zeropadded entries with
ID/Offset=00000000h.<br/>
The filesize can be computed as "NextOffset-CurrOffset" (at 800h-byte
resolution). Whereas, "NextOffset" can be:<br/>
```
  The offset of next File in File List (same as CurrOffset for 0-byte files)
  The offset of next Audio stream in Streaming List
  The offset of next Movie stream in Streaming List (if it's in .CDF, not .STR)
  The size of the current Folder (for STAGE1-5)
  The size of the whole .CDF file (for STAGE0)
```
For STAGE1-5, audio streams are usually stored at the end of folder (after the
files). However, for STAGE0, audio streams are oddly inserted between file21000
and file30100.<br/>

#### File Chunks (for files within File List)
Most CDF files in STAGE0 and STAGE1-5 do contain one or more chunks with
10h-byte chunk headers (this can be considered as an additional filesystem
layer, with the chunk data being the actual files).<br/>
```
  000h 1  Chunk Type (see below)
  001h 1  End Flag (01h=More Chunks follow, FFh=Last Chunk)
  002h 2  Unknown (usually 800h, sometimes 500h or 600h)
            (eg. 500h in stage0\file30301\chunkX)
            (eg. 600h in stage1\folder1201\file0\chunkXYZ)
  004h 4  Chunk Size/800h
  008h 4  Unknown (usually zero) (or 80xxxx00h in Chunk Type 0 files?)
  00Ch 4  Zero (0)
  010h .. Data (Chunk Size-10h bytes)
```
Chunk Types:<br/>
```
  00h=Room package            .pe2pkg
  01h=Image                   .pe2img
  02h=CLUT                    .pe2clut
  04h=CAP2 Text               .pe2cap2
  05h=Room backgrounds        .bs
  06h=SPK/MPK music program   .spk  ;stereo/mono, sound/music, single/multiple?
  07h=ASCII text              .txt     (eg. stage0\20101..20132)
 ;Reportedy also (but wrong):
 ;60h=Sounds                  .pe2snd  (but nope, that's wrong, see below)
 ;60h is a MDEC movie from Streaming List (unrelated to File List chunks),
 ;60h is 20h-byte .STR header each 800h-bytes (occurs in "stage1\folder501")
```
There are some chunkless files:<br/>
```
  stage0\40105...40198 are raw hMPK files without chunks
  stage0\11000, 20213, 20214, 20300, .., 660800 and 900000 are empty 0-byte
```

#### Streaming List Movie entries (stream type 1)
```
  000h 2    Stream Type (0001h=Movie)
  002h 2    Unknown (8000h or 0000h)
  004h 4    Offset/800h in current Folder of .CDF file ;<-- used when [024h]=0
  008h 4    Offset/800h in INTERx.STR file             ;<-- used when [024h]>0
  00Ch 2    Unknown (0000h)
  00Eh 2    Stream ID (increasing, usually starting at 64h aka 100 decimal)
  010h 2    Stream sub.ID (usually 0, increases +1 upon multiple same IDs)
  012h 2    Picture Width  (0140h = 320 decimal)
  014h 2    Picture Height (00F0h = 224 decimal)
  016h 2    Unknown (0000h)
  018h 2    Unknown (0000h or 0018h)   maybe 24bpp or 24fps
  01Ah 2    Unknown (73Ah or 359h or 3DCh)  (Size? but it's slighty too large?)
  01Ch 6    Unknown (zero)
  022h 2    Unknown (0 or 1) (often 1 when [024h]>0, but not always)
  024h 2    Movie number in INTERx.STR, 1 and up? (or 0=Movie is in STAGEx.CDF)
  026h 2    Unknown (0 or 1)
```
The size of movie streams in .CDF can be computed in similar fashion as for
File List entries (see there for details).<br/>
The size of movie streams in .STR cannot be computed easily (the next stream
isn't neccassarily stored at the next higher offset; even if it's within same
folder). As workaround, one could create a huge list with all streams from all
Folders in all STAGEx.CDFs (or scan the MDEC .STR headers in .STR file; and
check when the increasing frame number wraps to next stream).<br/>
The dual offsets are oddly computed as: [004h]=[008h]+EndOfLastFileInFolder
(that gives the correct value in the used entry, and a nonsensical value in the
other entry).<br/>

#### Streaming List Audio entries (stream type 2)
```
  000h 2    Stream Type (0002h=Audio)
  002h 2    Unknown (806Ah or increasing 0133h,0134h,0135h)
  004h 4    Offset/800h in STAGEx.CDF file (increasing offsets)
  008h 4    Unknown (0 or 13000h or E000h)
  00Ch 2    Stage Number (0..5 = STAGE0-5)
  00Eh 2    Stream ID (1, or increasing 3Ah,3Bh,3Ch)
  010h 4    Stream sub.ID (usually 0Bh, increases +0Ah upon multiple same IDs)
  014h 2    Unknown (0 or 2B0h or 3ADh or 398h) (Size/800h minus something?)
  016h 2    Unknown (usually 20h, sometimes 0Fh)
  018h 4    Unknown (2 or 1)              ... maybe num channels ?
  01Ch 2+2  Unknown (0,0 or 800h,800h)
  020h 8    Unknown (0)
```
The size of audio streams can be computed in similar fashion as for File List
entries (see there for details).<br/>

#### Audio Stream Data (stored alongsides with file data in STAGEx.CDF file)
This contains a 800h-byte header a list of 32bit indices:<br/>
```
  000h 800h Whatever increasing 32bit index/timing values? FFFFFFFFh=special?
  ;That header exists in stage0\ and stage3\folder101\
  ;That header doesn't exist in all files (eg. not in stage1\folder301\)
```
then followed by several chunk-like STM blocks with 10h-byte headers:<br/>
```
  000h 4  Chunk Index (increases each second chunk, from 0 and up)
  004h 4  Number of Chunk Indices
  008h 4  Fixed (02h,"STM")                                  ;2-channel Stream?
  00Ch 1  Chunk Subindex (toggles 00h or 01h per each chunk) ;ch left/right?
  00Dh 1  Chunk Size/800h
  00Eh 4  Unknown (can be 00h, 01h, 11h, 20h, 21h)
  00Fh 4  Unknown (can be A0h or C0h)
  010h .. Data (Chunk Size-10h bytes) (looks like SPU-ADPCM audio)
```
After the last STM chunk, there is more unknown stuff:<br/>
```
  000h 0   Number of ADPCM blocks?            (eg. 28h    or 49h)
  004h 4   Size of extra data block in bytes  (eg. 13900h or 24200h)
  008h 38h Zerofilled
  040h 8   Zerofilled (maybe 1st sample of 1st SPU-ADPCM block)
  048h ..  Looks like more SPU-ADPCM block(s), terminated by ADPCM end flag(s)
  ...  ..  Zerofilled (padding to end of last 800h-byte sector)
```

#### Movie Stream Data (stored in .CDF, or in separate INTERx.STR file)
The movies are usually stored in INTERx.STR (except, some have them stored in
STAGEx.CDF, eg. stage1\folder501, stage1\folder801, stage2\folder2101,
stage2\folder3001).<br/>
The data consists of standard .STR files (with 20h-byte headers on each
800h-byte sector), with the MDEC data being in huffman .BS format (with .BS
header... per frame?).<br/>
And, supposedly interleaved with XA-ADPCM audio sectors...?<br/>

#### PE\_DISK.01 and PE\_DISK.02
The presence of these files is probably used to detect which disc is inserted.
The file content is unknown (looks like 800h-byte random values).<br/>

#### Note
Reportedly "Files inside archive may be compressed with custom LZSS
compression" (unknown if/when/where/really/which files).<br/>



##   CDROM File Archive IND/WAD (MTV Music Generator)
#### MTV Music Generator (IND/WAD) (MagDemo30: JESTER\WADS\ECTS.IND and .WAD)
ECTS.IND contains FOLDER info:<br/>
```
  0000h 20h   Name/ID ("Music 2", zeropadded)
  0020h 4     Unknown (110000h)
  0024h 4     Filesize-1000h (size excluding last 1000h-byte padding)
  0028h 4     Unknown (17E0h)
  002Ch 4     Unknown (5)
  0030h N*10h Folder List, starting with Root in first 10h-byte
  2CF0h 4     Small Padding (34h-filled)
  2CF4h 1000h Final Padding (34h-filled)
 Folder List entries that refer to Child Folders in ECTS.IND:
  000h 8     Folder Name ("EXTRA*~*", zeropadded if less than 8) ("" for root)
  008h 2     Self-relative Index to first Child folder (positive)
  00Ah 2     Number of Child Folders (0..7FFFh)
  00Ch 4     Always 0007FFFFh (19bit Offset=7FFFFh, plus 13bit Size=0000h)
 Folder List entries that refer to File Folders in ECTS.WAD:
  000h 8     Folder Name ("EXTRA*~*", zeropadded if less than 8)
  008h 2     Self-relative Index to Parent folder (negative)
  00Ah 2     Number of Child Folders (always 8000h=None)
  00Ch 4     Offset and Size in ECTS.WAD
 The 32bit "Offset and Size" entry consists of:
  0-18   19bit Offset/800h in ECTS.WAD
  19-31  13bit Size/800h-1 in ECTS.WAD
```
ECTS.WAD contains FILE info and actual FILE data:<br/>
```
 There are several File Folders (at the locations specified in ECTS.IND).
 The separate File Folders look as so:
  000h 4     Number of files (N)
  004h N*10h File List
  ...  ..    34h-Padding to 800h-byte boundary
  ...  ..    File Data area
 File List entries:
  000h 8     File Name ("NAMELIST", "ACIDWO~1", etc.) (00h-padded if shorter)
  008h 4     Offset/800h (always from begin of WAD, not from begin of Folder)
  00Ch 4     Filesize in bytes
 The first file in each folder is called "NAMELIST" and contains this:
  000h 20h   Long Name for Parent Folder (eg. "Backgrounds", zeropadded)
  020h 20h   Long Name for this Folder   (eg. "Extra 1", zeropadded)
  040h N*20h Long Names for all files in folder (except for NAMELIST itself)
 For example, Long name for "ACIDWO~1" would be "Acidworld". Short names are
 uppercase, max 8 chars, without spaces (with "~N" suffix if the long name
 contains spaces or more than 8 chars). Many folder names are truncated to
 one char (eg. "D" for Long name "DTex"), in such cases short names CAN be
 lowercase (eg. "z" for  Long name "zTrans").
 The Long Names are scattered around in the NAMELIST files in ECTS.WAD file,
 so they aren't suitable for lookup (unless when loading all NAMELIST's).
```



##   CDROM File Archive GAME.RSC (Colonly Wars Red Sun)
#### Colony Wars Red Sun (MagDemo31: CWREDSUN\GAME.RSC, 13Mbyte)
```
  0000h 4     Offset to Bonkers List (2794h)
  0004h F*8   Folder List                      (80h bytes, 10h entries)
  0084h N*14h File List(s) for each folder     (2710h bytes, 1F4h entries)
  2794h 4     Number of Bonkers     (FE3h)
  2798h B*8   Bonkers List                     (7F18h bytes, FE3h entries)
  A6B0h 8     Unknown (zerofilled)
  A6B8h ..    File Data area
```
Folder List entries:<br/>
```
  000h 4     Offset to File List for this folder   ;\both zero when empty
  004h 4     Number of Files in this folder        ;/
```
File List entries:<br/>
```
  000h 10h   Filename ("FILENAME_EXT", zeropadded)
  010h 3     Index (in Bonkers list) (000h..Fxxh)
  013h 1     Folder Number where the file is stored (00h..0Fh)
```
Bonkers List entries:<br/>
```
  000h 4     File Offset (to Data, inreasing, 4-byte aligned, A6B8h and up)
  004h 4     Folder Number where the file is stored (00h..0Fh)
```
Offsets/Indices in Folder/File list are unsorted (not increasing).<br/>
Offsets in Bonkers List are increasing (so filesizes can be computed as
size=next-curr, except, the LAST file must be computed as size=total-curr).<br/>
There is no "number of folders entry" nor "folder list end marker", as
workaround, while crawling the folder list, search the smallest file list
offset, and treat that as folder list end offset.<br/>
In the demo version, all File List entries for Folder 5 are pointing to files
with filesize=0, however, the Bonkers List has a lot more "hidden" entries that
are marked to belong to Folder 5 with nonzero filesize.<br/>
Note: Older Colony Wars titles did also have a GAME.RSC file (but in different
format, without folder structure).<br/>



##   CDROM File Archive BIGFILE.DAT (Soul Reaver)
#### Legacy of Kain: Soul Reaver - BIGFILE.DAT
#### Legacy of Kain: Soul Reaver (MagDemo26: KAIN2\BIGFILE.DAT)
```
  000h 2     Number of Folders (175h in retail, 0Ah in demo)
  002h 2     Zero
  004h N*8   Folder List (8-byte per Folder)
  ...  ..    Zeropadding (to 800h-byte boundary)
  ...  ..    1st Folder (with File List, and File Data for that folder)
  ...  ..    2nd Folder (with File List, and File Data for that folder)
  ...  ..    3rd Folder (with File List, and File Data for that folder)
  ...  ..    etc.
```
Folder List entries:<br/>
```
  000h 2     Unknown (somehow randomly increases from -8000h to +7E8Fh)
  002h 2     Number of Files in this Folder (eg. 97h)
  004h 4     Offset to Folder (usually 800h-aligned)
```
Folder format:<br/>
```
  000h 2     Number of Files (same value as FolderistEntry[002h]) ;\encrypted
  002h 2     Zero                                                 ; by 16bit
  004h N*10h File List (10h-byte per Folder)                      ; XOR value
  ...  ..    Zeropadding (to 800h-byte boundary)                  ;/
  ...  ..    File Data for this folder                            ;-unencrypted
```
File List entries:<br/>
```
  000h 4     Unknown (random? filename hash? encrypted name?)
  004h 4     File Size in bytes
  008h 4     File Offset (usually 800h-aligned)
  00Ch 4     Unknown (random? filename hash? encrypted name?)
```
Encryption:<br/>
The file header, the first some Folder headers (those in first quarter or so),
and (all?) File Data is unencrypted (aka XORed with 0000h).<br/>
The Folder headers at higher offsets are encrypted with a 16bit XOR value. That
XOR value is derived from Subchannel Q via LibCrypt:<br/>
[CDROM Protection - LibCrypt](cdromfileformats.md#cdrom-protection-libcrypt)<br/>
When not having the Subchannel data (or when not knowing which Folders are
encrypted or unencrypted), one can simply obtain the encryption key from one of
these entries (which will be key=0000h when unencrypted):<br/>
```
  key = FileListEntry[000h] XOR FolderListEntry[002h]  ;encrypted num entries
  key = FileListEntry[002h]                            ;encrypted Zero
  key = FileListEntry[zeropadding, if any]             ;encrypted Zeropadding
```
LibCrypt seems to be used only in PAL games, unknown if the Soul Reaver NTSC
version does also have some kind of encryption.<br/>



##   CDROM File Archive FF8 IMG (Final Fantasy VIII)
FF8 is quite a mess without clear directory structure. Apart from SYSTEM.CNF
and boot EXE, there is only one huge IMG file. There are at least two central
directories: The Root directory (usually at the start of the IMG file), and the
Fields directory (hidden in a compressed file that can be found in the Root
directory). Moreover, there are files that exist in neither of the directories
(most notably the Movies at the end of the IMG file).<br/>

#### IMG File
The IMG file doesn't have a unique file header, it can be best detected by
checking the filename: FF8DISCn.IMG with n=1-4 for Disc 1-4 (or only
FF8DISC1.IMG or FF8.EXE+FF8TRY.IMG for demo versions).<br/>
The directories contain ISO sector numbers (originated from begin of the ISO
area at sector 00:02:00). Accordingly, it's best to extract data from the whole
disc image (in CUE/BIN format or the like). When having only the raw IMG file,
one most know/guess the starting sector number (eg. assume that the first Root
File is located on the sector after the Root Directory, and convert sector
numbers ISO-to-IMG accordingly).<br/>
Another oddity is that many files contain RAM addresses (80000000h-801FFFFFh),
unknown how far that's relevant, and if there are cases where one would need to
convert RAM addresses to IMG offsets.<br/>

#### Root Directory
The Root Directory is found at:<br/>
```
  Offset 0000h in FF8DISCn.IMG in NTSC retail versions
  Offset 2800h in FF8DISCn.IMG in PAL retail versions
  Offset 0000h in FF8DISC1.IMG in french demo version
  Offset ?????h in FF8.EXE in MagDemo23 (...maybe offset 3357Ch ?)
  Offset 33510h in FF8.EXE in japanese demo version ?
  Offset 33584h in FF8.EXE in other demo versions   ?
```
For detection:<br/>
```
  if FF8DISCn.IMG starts with 000003xxh --> assume Root at IMG offset 0
  if FF8DISCn.IMG starts with xxxxxxxxh --> assume Root at IMG offset 2800h
  if FF8TRY.IMG starts with "SmCdReadCore" --> assume Root somewhere in EXE
```
File List:<br/>
```
  000h N*8  File List entries
  ...  ..   Zeropadding to end of 800h-byte sector
```
File List entries:<br/>
```
  000h 4    ISO Sector Number (origin at 00:02:00) (unsorted, not increasing)
  004h 4    Filesize in bytes
```
The file list does usually end with zeropadding (unknown if that applies to all
versions; namely the Demo version might end with gibberish instead of having
800h-byte sector padding).<br/>

#### Fields Directory
The Fields Directory is located in Root file 0002h. First of, decompress that
file, then search the following byte sequences to find the start/end of the
directory:<br/>
```
  retail.start  040005241800bf8f1400b18f1000b08f2000bd270800e00300000000
  retail.end    0000010002000300
  demo.start    76DF326F34A8D0B863C8C0EC4BE817F8
  demo.end      0000000000000000000000000000000000100010
```
The bytes between those start/end pattern contain the Directory, with entries
in same format as Root directory:<br/>
```
  000h 4    ISO Sector Number (origin at 00:02:00)
  004h 4    Filesize in bytes
```
Notes: Root file 0002h is about 190Kbyte (decompressed), of which, the Fields
Directory takes up about 8Kbytes, the remaining data contains other stuff.<br/>
The sector numbers in the Fields Directory refer to other locations in the IMG
file (not to data in Root File 0002h).<br/>

#### Movie List
There is no known central directory for the movies (unknown if such a thing
exists, or if the movie sector numbers are scattered around, stored in separate
files). However, a movie list can be generated by crawling the movie headers,
starting at end of IMG file:<br/>
```
  sector = NumSectors(IMG file)
 @@lop:
  seek(sector-1), read(buf,08h bytes)
  if first4byte[buf+0]=("SMJ",01h), or ("SMN",01h) then
    num_sectors=(byte[buf+5]+1)*(halfword[buf+6]+1)
    sector=sector-num_sectors
    AddToMovieFileList(sector, num_sectors)
    goto @@lop
  endif
```
That should cover all movies, which are all at the end of the IMG file (except,
there's one more movie-like file elsewhere in the middle of IMG file, that file
has only SMN/SMR audio sectors, without any SMJ video sectors).<br/>

#### PADBUG archives
PADBUG archives are used in Root files 001Eh..007Fh, most of them contain two
AKAO files (except file 004Bh contains one AKAO and one TXT file).<br/>
```
  000h 4     Number of Files (N) (usually 2)
  004h N*8   File List
  ...  ..    File Data area
```
File List entries:<br/>
```
  000h 4     Offset in bytes (increasing, 4-byte aligned, see Quirk)
  004h 4     File Size in bytes (can be odd)
```
Quirk: All files are zeropadded with 1-4 bytes to 4-byte boundary (ie. files
that do end on a 4-byte boundary will be nethertheless padded with 4 zeroes).<br/>
Note: The PADBUG archives resemble LNK archives in  O.D.T. (though those LNK
archives have a different unique 4-byte padding quirk).<br/>

#### Compression
[CDROM File Compression LZ5 and LZ5-variants](cdromfileformats.md#cdrom-file-compression-lz5-and-lz5-variants)<br/>
FF8 does reportedly also use GZIP (unknown in which files).<br/>

#### Known/unknown sectors for US version FF8DISC1.IMG
```
  root sectors:       27CBh ;\
  field sectors:      D466h ; total known sectors: 36D13h
  movie sectors:     270E2h ;/
  unknown sectors:   14F49h
  total IMG sectors: 4BC5Ch
```

#### See also
[https://github.com/myst6re/deling/blob/master/FF8DiscArchive.cpp]

[https://ff7-mods.github.io/ff7-flat-wiki/FF8/PlaystationMedia.html]




##   CDROM File Archive FF9 IMG (Final Fantasy IX)
#### Final Fantasy IX (FF9.IMG, 320Mbyte) Overall format
```
  000h Root Directory
  800h 1st Child Folder
  ...  2nd Child Folder
  ...  3rd Child Folder
  ...  ...
  8000h ?     Last folder, with Type3, contains 1FFh x increasing 16bit numbers
  ...  Data for files in 1st Child Folder
  ...  Data for files in 2nd Child Folder
  ...  Data for files in 3rd Child Folder
  ...
```

#### IMG Root Directory
```
  000h 4     ID "FF9 "
  004h 4     Unknown (06h on Disc 1 of 4) (maybe version, or disc id?)
  008h 4     Number of Folder List entries (0Fh)
  00Ch 4     Unknown (01h on Disc 1 of 4) (maybe version, or disc id?)
                 (or Offset/800h to first file list?)
  010h N*10h Folder List
  ...  ..    Padding to 800h-byte boundary ("FF9 FF9 FF9 FF9 ")
```
Folder List entries:<br/>
```
  000h 4     FolderType (2=Normal, 3=Special, 4=Last entry)
  004h 4     Number of entries in File List (0..1FFh ?)
  008h 4     Offset/800h to Child Folder with File List
  00Ch 4     Offset/800h to File Data (same as 1st offs in File List) (0=Last)
```

#### IMG Child Folders (FolderType=2)
```
  000h N*8   File List entries (N=Number of files, from Root directory)
  N*8  8     File List END entry (ID=FFFFh, Attr=FFFFh, Offs=EndOfLastFile)
  ...  ..    Zeropadding to 800h-byte boundary
```
File List entries:<br/>
```
  000h 2     File ID (increasing, often decimal 0,10,100, or FFFFh=Last)
  002h 2     Attr (unknown purpose, eg. 0,2,3,4,8,21h,28h,2Fh,44h,114h,FFFFh)
  004h 4     Offset/800h to File Data (increasing, implies end of prev entry)
```

#### IMG Child Folders (FolderType=3)
```
  000h N*2   File Offsets/800h, from File Data Offset in Root (or FFFFh=None)
  N*2  2     End Offset for last file
```
The filesize can be computed as (NextOffs-CurrOffs)\*800h, however, one must
skip unused entries (FFFFh) to find NextOffs.<br/>

#### Nested Child Archives
Most of the files in FF9.IMG are DB archives, there are also some DOT1
archives.<br/>
[CDROM File Archive FF9 DB (Final Fantasy IX)](cdromfileformats.md#cdrom-file-archive-ff9-db-final-fantasy-ix)<br/>
There are various combinations of IMG, DB, DOT1 archives nested up to 4 levels
deep:<br/>
```
  IMG\DOT1         (eg. dir01\file003C)
  IMG\DB           (eg. dir01\file2712)
  IMG\DB\DOT1      (eg. dir01\file2712\00-0411)
  IMG\DB\DOT1\DOT1 (eg. dir01\file2712\00-0443\*)
  IMG\DB\DB        (eg. dir03\file2328\1B-000*)
```

#### Folders in Root directory
```
  dir00 - Status/Menu/Battle/... -Text and random stuff.
  dir01 - Misc Images (Logos, Fonts, World 'mini' Map images, etc).
  dir02 - Dialog Text
  dir03 - Map models (Mini-zidane, airships, save point moogle, tent...)
  dir04 - Field models
  dir05 - Monster Data (Part I, stats, names, etc).
  dir06 - Location Data (Dungeon, Cities, etc).
  dir07 - Monster Data (Part II, 3d models)
  dir08 - Weapon Data (including models)
  dir09 - Samplebanks and Sequencer Data (ie music).
  dir0A - party members Data (including models)
  dir0B - Sound effects
  dir0C - World Map Data
  dir0D - Special effects (magic, summons...)
```

#### See also
[https://ninjatoes.blogspot.com/2020/07/]

[https://wiki.ffrtt.ru/index.php?title=Main_Page]




##   CDROM File Archive GTFS (Gran Turismo 2)
#### Gran Turismo 2 (MagDemo27: GT2\GT2.VOL, GT2.VOL\arcade\arc\_carlogo) - GTFS
```
  000h 4     ID "GTFS"                                             ;\
  004h 4     Zero                                                  ;
  008h 2     Number of 4-byte File Offset List entries (N)         ; File(0)
  00Ah 2     Number of 20h-byte File/Folder Name List entries (F)  ;
  00Ch 4     Zero                                                  ;
  010h N*4   File Offset List (see below)                          ;/
  ...  ..    Zeropadding to 800h-byte boundary
  ...  F*20h File/Folder Name List (see below)                     ;-File(1)
  ...  ..    Zeropadding to 800h-byte boundary
  ...  ..    File Data                                             ;-File(2)
  ...  ..    Zeropadding to 800h-byte boundary
  ...        File Data                                             ;-File(3)
  ...  ..    ...
  ...        File Data                                             ;-File(N-2)
  ...  ..    Zeropadding to 800h-byte boundary
  EOF  0     End of File                                           ;-File(N-1)
```
That is, for N files, numbered File(0)..File(N-1):<br/>
```
  File(0) and File(1) = Directory information
  File(2)..File(N-2)  = Regular data files
  File(N-1)           = Offset List entry points to the end of .VOL file
```
File Offset List entries, in File(0):<br/>
Contains information for all files, including File(0) and File(1), and
including an entry for File(N-1), which contains the end offset for the last
actual file, ie. for File(N-2).<br/>
```
  Bit0-10  = Number of padding bytes in last sector of this file (0..7FFh)
  Bit11-31 = Offset/800h to first sector of this file (increasing)
  To compute the filesize: Size=(Entry[N+1] AND FFFFF800h)-Entry[N]
```
File/Folder Name List entries, in File(1):<br/>
Contains information for all files, excpet File(0), File(1), File(N-1), plus
extra entries for Folders, plus ".." entries for links to Parent folders.<br/>
```
  000h 4     Unknown (379xxxxxh) (maybe timestamp?)
  004h 2     When Flags.bit0=0: Index of File in File Offset List (2 and up)
             When Flags.bit0=1: Index of first child in Name List, or...
             When Flags.bit0=1: Index of 1st? parent in Name List (Name="..")
  006h 1     Flags (bit0:0=File, 1=Directory; bit7:1=Last Child entry)
  007h 19h   Name (ASCII, zeropadded)
```
The game does use several archive formats: GTFS (including nested GTFS inside
of main GTFS) and WAD.WAD and DOT1.<br/>
The game does use some GT-ZIP compressed files, and many GZIP compressed files
(albeit with corrupted/zeropadded GZIP footers; due to DOT1 filesize 4-byte
padding and (unneccessarily) GTFS 800h-byte padding).<br/>
[CDROM File Compression GT-ZIP (Gran Turismo 1 and 2)](cdromfileformats.md#cdrom-file-compression-gt-zip-gran-turismo-1-and-2)<br/>
[CDROM File Compression ZIP/GZIP/ZLIB (Inflate/Deflate)](cdromfileformats.md#cdrom-file-compression-zipgzipzlib-inflatedeflate)<br/>
To extract the decompressed size from the corrupted GZIP footers, one could
compute the compressed "size" (excluding the GZIP header, footer, and padding),
and search for a footer entry that is bigger than "size".<br/>
```
  size=gz_filesize
  size=size-GzipHeader(including ExtraHeader, Filename, Comment, HeaderCrc)
  size=size-GzipFooter(8)   ;initially assuming 8-byte footer (without padding)
  i=gz_filesize-4
 @@search_footer:
  if buf[i]<size then i=i-1, size=size-1 goto @@search_footer
  decompressed_size = buf[i]
```
Note: Above doesn't recurse the worst-case compression ratio, where compressed
files could be slightly bigger than decompressed files.<br/>



##   CDROM File Archive Nightmare Project: Yakata
#### Nightmare Project: Yakata
ISO Files:<br/>
```
  CD.IMG      550Mbyte  Contains file 004h..FFFh
  CDRTBL.DAT  32Kbyte   Alias for file 000h (File List for file 000h..FFFh)
  FDTBL.DAT   2Kbyte    Alias for file 001h (Folder List and Disc ID)
  SLPS_010.4* 500Kbyte  Alias for file 003h (Boot EXE)
  SYSTEM.CNF  72bytes   Alias for file 002h (Boot Info)
  XXXXXXXX.   27Mbyte   Padding (zerofilled)
```
FDTBL.DAT (Folder List):<br/>
```
 FDLTBL.DAT seems to be used to divide the file list in CDRTBL.DAT into
 separate folders. The Folder List entries are containing the first file number
 for each folder. Empty folders have same file number as next entry.
 The last folder contains the specified file number plus all remaining files.
  000h 56h*2 Folder List (16bit File Numbers, increasing from 0004h to 0xxxh)
  0ACh 748h  Zerofilled
  7F4h 0Ah   Game ID (ASCII "SLPS1045",00h,00h; always so on Disc 1..3)
  7FEh 2     Disc ID (1..3 = Disc 1..3)
```
CDRTBL.DAT (File List):<br/>
```
  000h 8000h File List (1000h x 8-byte entries)
 File List entries:
  000h 4   Sector (MM:SS:FF:00 in BCD, increasing)  ;\all zero for
  004h 2   Size1  (NumFramesCh1 or NumSectors)      ; unused entries
  006h 2   Size0  (NumFramesCh0 or Zero)            ;/
 The meaning of the Size entries depends on the file type:
  Normal binaries:  [004h]=NumSectors     [006h]=0             (1 channel)
  XA-ADPCM streams: [004h]=NumSectors-50h [006h]=0             (16 channels)
  MDEC streams:     [004h]=NumFrames      [006h]=0             (audio+video)
  Special streams:  [004h]=NumFramesCh1   [006h]=NumFramesCh0  (2 channels)
 To determine the actual filesize, one must compute the difference between
  sectors for current and next used file entry (or end of CD.IMG for last file;
  or alternately assume last file to be a Normal Binary with Size=NumSectors).
 Normal Binaries:
  Contains single files (file=0/channel=0). Filetypes include TIM, VB, VH,
  other/custom file formats, and DOT1 archives.
  The DOT1 archives have 4-byte aligned offsets, but, unconventionally, with
  some offsets set to ZERO (usually the last entry, and sometimes also other
  entries):
  SEQ files (Disc1:Dir08h\File173h)       ;with ZERO entries    (=uncommon)
  SEQ files (Disc1:Dir09h\File176h..3D7h) ;with ZERO entries    (=uncommon)
  SEQ files (Disc1:Dir0Ah\File3DAh..3E6h) ;with ZERO entries    (=uncommon)
  TIM files (Disc1:Dir4Fh\File962h..983h) ;with ZERO entries    (=uncommon)
  TIM files (Disc1:Dir0Ch\File414h..426h) ;without ZERO entries (=normal DOT1)
 XA-ADPCM Streams (Disc1:Dir0Bh\File3E7h..413h):
  These contain 16 audio streams (file=1/channel=00h-0Fh). The Size entry is
  set to total size in sectors for all streams, minus 50h (ie. there appears
  to be 50h sectors appended as padding before next file).
 MDEC Streams (Disc1:Dir53h\FileBD1h..BEBh):
  These are standard STR files with MDEC video (file=0/channel=1) and
  XA-ADPCM (file=1/channel=1). There are 10 sectors per frame (8-9 video
  sectors plus 1-2 audio sectors). The total filesize is NumFrames*10+Align(8)
  sectors; the Align(8) might be there to include one final audio sector.
 Special Streams (Disc1:Dir07h\File0E9h-16Eh and Dir50h\File985h..B58h):
  These are custom STR files (non-MDEC format), perhaps containing Polygon
  streams or whatever.
  There are two channels (file=1/channel=00h-01h), each channel contains
  data that consists of 5 sectors per frame (1xHeader plus 4xData).
  The sectors have STR ID=0160h, and STR Type as follows:
    0000h=Whatever special, channel 0 header (sector 0)
    0400h=Whatever special, channel 1 header (sector 1)
    0001h=Whatever special, channel 0 data   (sector 2,4,6,8)
    0401h=Whatever special, channel 1 data   (sector 3,5,7,9)
  The File List size entries contain Number of Frames for each channel (either
  of these entries may be zero, or bigger/smaller/same than the other entry).
  The smaller channel is padded to same size as bigger channel (ie. total
  filesize is "max(NumFramesCh0,NumFramesCh1)*10 sectors"; though that formula
  doesn't always hold true, for example, Disc1:Dir50h\FileA2Dh and FileB1Bh
  are bigger or smaller than expected).
```



##   CDROM File Archive FAdj0500 (Klonoa)
#### Klonoa (MagDemo08: KLONOA\FILE.IDX+FILE.BIN)
```
 FILE.IDX
  000h 8     ID "FAdj0500"
  008h 38h   RAM addresses       (80xxxxxxh, 0Ch words)
  038h 4     Zero
  03Ch 4     RAM address         (80xxxxxxh)
  040h N*10h File List (including Folder start/end markers)
 FILE.BIN
  000h ..    File Data area (split into filesizes from FILE.IDX)
```
File List entries:<br/>
```
 Type 0 (Folder End):
  000h 4     Type (0=Folder End)
  000h 4     Zero
  008h 4     RAM address         (always 801EAF8Ch)
  00Ch 4     Zero
 Type 1.a (Folder Start):
  000h 4     Type (1=Folder Start)
  000h 4     Folder Offset/800h  (offset of FIRST file in this Folder)
  008h 4     RAM address         (always 801EAF8Ch)
  00Ch 4     Folder Size/800h    (size of ALL files in this Folder)
 Type 1.b (Force Offset, can occur between Files within a Folder):
  000h 4     Type (1=Same as Folder Start)
  000h 4     Folder Offset/800h  (offset of NEXT file in this Folder)
  008h 4     RAM address         (always 801EAF8Ch)
  00Ch 4     Folder Size/800h    (zero for Force Offset)
 Type 2 (File entries, within Folder Start/End):
  000h 4     Type (2=File)
  004h 4     Filesize in bytes   (4-byte aligned?)
  008h 4     RAM address 1       (80xxxxxxh, or zero)
  00Ch 4     RAM address 2       (80xxxxxxh)
```
File Offsets are usually 4-byte aligned (at offset+filesize from previous
entry). Except, the first file after Folder Start (and Force Offset) is
800h-byte aligned.<br/>
The archive contains DOT1 archives, OA05 archives, Ulz compression, and TIM,
TMD, VAB, SEQ, VB files.<br/>



##   CDROM File Archives in Hidden Sectors
#### Hidden Sector Overview
Xenogears, Chrono Cross, and Threads of Fate contain only two files in the ISO
filesystem (SYSTEM.CNF and the boot executable). The CDROMs contain standard
ISO data in Sector 10h-16h, followed by Hidden stuff in Sector 17h and up:<br/>
```
  Sector 10h (00:02:16)  Volume Descriptor (CD001)      ;\
  Sector 11h (00:02:17)  Volume Terminator (CD001)      ;
  Sector 12h (00:02:18)  Path Table 1                   ;
  Sector 13h (00:02:19)  Path Table 2                   ; standard ISO
  Sector 14h (00:02:20)  Path Table 3                   ;
  Sector 15h (00:02:21)  Path Table 4                   ;
  Sector 16h (00:02:22)  Root Directory                 ;/
  Sector 17h (00:02:23)  Hidden ID                      ;\
  Sector 18h (00:02:24)  Hidden Directory               ; hidden directory
  Sector ..  (00:02:xx)  Hidden Unknown                 ;/
  Sector ..  (00:02:xx)  Hidden Files... (referenced via Hidden Directory)
```
Note: Like normal files, all hidden entries have their last sector flagged as
SM=89h (that applies to all three Hidden ID, Directory, Unknown entries, and to
all Hidden Files). For details, see:<br/>
[CDROM XA Subheader, File, Channel, Interleave](cdromdrive.md#cdrom-xa-subheader-file-channel-interleave)<br/>

#### Xenogears (2 discs, 1998)
```
 Sector 17h (Hidden.ID)
  000h 0Eh  ID ("DS01_XENOGEARS"=Disc 1, or "DS02_XENOGEARS"=Disc 2)
  00Eh 7F2h Zerofilled
 Sector 18h..27h
  000h N*7  File List entries
 Sector 28h (Hidden.Unknown)
  Seems to contain a list of 16bit indices 0000h..1037h,FFFFh in File List
  (that, as raw list indices, regardless of the directory structure)
  000h      Unknown 0016 0018 FFFF FFFF 01A8 FFFF FFFF FFFF  ;\
  010h      Unknown FFFF FFFF FFFF FFFF 0A35 0A3A 0D35 0AD3  ; as so on Disc 2
  020h      Unknown 0A22 0A2E 0A2F FFFF FFFF FFFF FFFF FFFF  ; (values<>FFFFh
  030h      Unknown 0014 0001 0013 FFFF 0075 FFFF FFFF FFFF  ; on Disc 1
  040h      Unknown 0C10 0C14 0C15 0C19 0F52 FFFF FFFF FFFF  ; are 5 less, eg.
  050h      Unknown 0F4C 0B6E 0C4D 1037 0C09 0BAD FFFF FFFF  ; 0011,0013,FFFF..)
  060h      Unknown 002E 0034 FFFF FFFF FFFF FFFF FFFF FFFF  ;
  070h      Unknown FFFF FFFF FFFF FFFF                      ;/
  078h 2    Disc Number      (0001h=Disc 1, 0002h=Disc 2)
  07Ah 786h Zerofilled
 Sector 29h 1st file
```
File List entries:<br/>
```
  000h 3    24bit Offset (increasing sector number, or 0=special)
  003h 4    32bit Size   (filesize in bytes, or negative or 0=special)
```
The Offset/Size can have following meanings:<br/>
```
  offset=curr,    size=+N    file at sector=curr, size N bytes
  offset=curr,    size=-N    begin of sub-directory, with N files
  offset=curr,    size=0     empty file, size 0 bytes
  offset=0,       size=0     unused file entry
  offset=FFFFFFh, size=0     end of root-directory
```
Notes: The Hidden.Directory size seems to be hardcoded to 10h sectors
(alternately, one could treat the sector of the 1st file entry as end of
Hidden.Directory plus Hidden.Unknown).<br/>
Root entry 0004h and 0005h are aliases for ISO files SYSTEM.CNF and boot EXE.
There seem to be no nested sub-directories (but there are several DOT1 child
archives, in root- and sub-directories, eg. 00DCh\0000h\\*).<br/>

#### Chrono Cross (2 discs, 1999,2000)
#### Threads of Fate (aka Dewprism) (1 disc, 1999,2000)
```
 Sector 17h (Hidden.ID)
  000h 2    Disc Number      (0001h=Disc 1, 0002h=Disc 2)
  002h 2    Number of Discs? (0002h) (always 2, even if only 1 disc)
  004h 2+2  Sector and Size for Hidden.ID        (Sector=0017h, Size=002Ch)
  008h 2+2  Sector and Size for Hidden.Directory (Sector=0018h, Size=60E0h)
  00Ch 2+2  Sector and Size for Hidden.Unknown   (Sector=0025h, Size=0022h)
  010h 10h  Zerofilled
  020h 0Ch  Title ID ("CHRONOCROSS",00h)      ;Chrono Cross (retail)
       09h  Title ID ("DEWPRISM",00h)         ;Threads of Fate (retail)
       10h  Title ID ("DEWPRISM_TAIKEN",00h)  ;Threads of Fate (demo)
  0xxh 7xxh Zerofilled (unused, since Hidden.ID has only Size=2Ch/29h/30h)
 Sector 18h..24h (Hidden.Directory)
  000h N*4  File List entries
  ...  ..   Zeropadding (till Size=60E0h, aka 6200 entries)
  ...  720h Zeropadding (till end of 800h-byte sector)
 Sector 25h (Hidden.Unknown)
  Seems to contain a list of 16bit indices 0000h..1791h,FFFFh in File List
  (though many of the listed indices are unused file list entries)
  000h 2    Disc Number      (0001h=Disc 1, 0002h=Disc 2)
  002h 10h  Unknown 0000 1791 1777 1775 00ED 09DF FFFF 0002    ;\same on
  012h 10h  Unknown 0025 0943 10E3 FFFF FFFF 0C77 0FD9 0FA3    ;/Disc 1+2
  022h ..   Zerofilled (unused, since Hidden.ID has only Size=0022h)
 Sector 26h  1st file (same as boot EXE in ISO)
```
File List entries:<br/>
```
  0-22   Sector number
  23     Flag (0=Normal, 1=Unused entry)
  24-31  Number of unused bytes in last sector, div8 (0..FFh = 0..7F8h bytes)
```
The directory is just a huge list of root files (without any folder structure;
many of the root files do contain DOT1 child archives though).<br/>
Root entry 0000h and 0001h are aliases for ISO files boot EXE and SYSTEM.CNF.<br/>
Filesizes can be computed as follows (that works for all entries including last
used entry; which is followed by some unused entries with bit23=1):<br/>
```
  filesize = ([addr+4]-[addr] AND 7FFFFFh)*800h - ([addr+3] AND FFh)*8
```
Unused entries with bit23=1 have Sector pointing to end of previous file
(needed for filesize calculation). There are some zeropadded entries at end of
list (with whole 32bit zero). There are hundreds of dummy txt files (24-byte
"It's CDMAKE Dummy!",0Dh,0Ah,,0Dh,0Ah,20h and File08xxh: 8-byte "dummy",0,0,0)
although those are real used file entries, each occupying a whole separate
800h-byte sector.<br/>

#### Threads of Fate (demo version) (MagDemo33: TOF\DEWPRISM.HED+.EXE+.IMG)
The demo version is using the same directory format as retail version (but with
Virtual Sector numbers in HED+EXE+IMG files instead of Hidden Sectors).<br/>
```
  TOF\DEWPRISM.HED (6000h bytes)    VirtSector=1Ah,  PhysSector=A0A5h
  TOF\DEWPRISM.EXE (97800h bytes)   VirtSector=26h,  PhysSector=A0B1h
  TOF\DEWPRISM.IMG (19EA800h bytes) VirtSector=155h, PhysSector=A1E0h
```
The demo's Virtual Sectors start at 1Ah (instead of 17h), to convert them to
Physical Sectors: Subtract 1Ah, then add starting Sector Number of HED file.
The HED file contains Hidden.ID, Hidden.Directory, and Hidden.Unknown.<br/>



##   CDROM File Archive HED/DAT/BNS/STR (Ape Escape)
#### Ape Escape KKIIDDZZ.HED/.DAT/.BNS/.STR
```
  000h 52Ch List for .DAT file    ;value 0000h..6FFFh = sector 0..6FFFh in DAT
  52Ch D4h  Zerofilled
  600h C4h  List for .BNS file    ;value 7000h..71AFh = sector 0..1AFh in BNS
  6C4h 3Ch  Zerofilled
  700h 50h  List for .STR file(s) ;raw CDROM sector numbers from 00:02:00
  750h B0h  Zerofilled
```
List entries, for all three lists (32bit values):<br/>
```
  0-19   File Offset/800h (20bit)
  20-31  File Size/800h   (12bit)
```
The sector numbers in DAT and BNS are basically counted from begin of the .DAT
file (which has 7000h sectors in retail version, and the .BNS file does follow
right thereafter on the next sector) (the demo version (MagDemo22: KIDZ\\*) has
only 105Ah sectors in .DAT, and the BNS entries at offset 600h start with 105Ah
accordingly).<br/>
There are 29 STR files in DEMO\\*.STR and STR\\*.STR, and 20 of them (?) are
referenced in HED ? There are also several .ALL files in above folders.<br/>
Note: Most of the STR files in Ape Escape contain polygon animation streams
rather than BS compressed bitmaps. Ape Escape is (c)1999 by Sony.<br/>
```
  .HED is 2048 bytes
  .DAT is 58720256 bytes = 3800000h bytes  ;div800h would be 7000h
  .BNS is 884736 bytes = D8000h bytes      ;div800h would be 1B0h
  .STR's: 7D3Bh+150 = 7DD1h = sector for STR\LAB.STR
```
Some files contain RLE compressed TIMs:<br/>
[CDROM File Compression TIM-RLE4/RLE8](cdromfileformats.md#cdrom-file-compression-tim-rle4rle8)<br/>
Some files contain raw headerless SPU-ADPCM (eg. DAT file 00Ah).<br/>



##   CDROM File Archive WAD.WAD, BIG.BIN, JESTERS.PKG (Crash/Herc/Pandemonium)
Below are two slightly different formats. WAD.WAD has unused entries
00h-filled. The PKG format has them FFh-filled, and does additionally support
Folders, and does have a trailing ASCII string. There's also a difference on
whether or not to apply alignment to empty 0-byte files.<br/>
However, the formats can appear almost identical (unused entries, 0-byte files,
and folders are optional, without them, the only difference would be the
presence of the ASCII string; which does exist only in 800h-byte aligned PKG's
though).<br/>

#### WAD.WAD (Crash/Crash)
Used by Crash Bandicoot 3 (DRAGON\WAD.WAD, plus nested WADs inside of WAD.WAD)<br/>
Used by Crash Team Racing (SPYR02\WAD.WAD, plus nested WADs inside of WAD.WAD)<br/>
Used by Madden NFL'98 (MagDemo02: TIBURON\.DAT except PORTRAIT,SPRITES,XA.DAT)<br/>
Used by N2O (MagDemo09, N2O\PSXMAP.TRM and N2O\PSXSND.SND)<br/>
Used by Speed Racer (MagDemo10: SPDRACER\ALL1.BIN, with 0-byte, unpadded eof)<br/>
Used by Gran Turismo 2 (MagDemo27: GT2\GT2.OVL = 128Kbyte WAD.WAD with GZIP's)<br/>
Used by Jonah Lomu Rugby (LOMUDEMO\SFX\\*.VBS, ENGLISH\\*.VBS)<br/>
Used by Judge Dredd (\*.CAP and \*.MAD)<br/>
Used by Spyro 2 Ripto's Rage (SPYRO2\WAD.WAD, and nested WAD's therein)<br/>
Used by Spyro 3 Year of the Dragon (SPYRO3\WAD.WAD, and nested WAD's therein)<br/>
Used by Men: Mutant Academy (MagDemo33: PSXDATA\WAD.WAD\\*, childs in PWF)<br/>
```
  000h N*8  File List
  ...  ..   Zeropadding to 4-byte or 800h-byte boundary (or garbage padding)
  ...  ..   File Data...
```
The File List can contain Files, and Unused entries:<br/>
```
  000h 4    Offset in bytes (4- or 800h-byte aligned, increasing) ;\both zero
  004h 4    Size in bytes (always multiples of 800h bytes)        ;/when Unused
```
The Offset in first entry implies size of the File List (the list has no
end-marker other than the following zeropadding; which doesn't always exist,
ie. not in 4-byte aligned files, and not in case of garbage padding).<br/>
The last entry has Offset+Size+Align = Total WAD filesize (except, Speed Racer
doesn't have alignment padding after the last file).<br/>
The WAD.WAD format doesn't have folder entries, however, it is often used with
nested WADs inside of the main WAD, which is about same as folders.<br/>
The alignment can be 4-byte or 800h-byte: N2O uses 4-byte for the main WADs.
Madden NFL '98 uses 800h-byte for main WAD and 4-byte for child WADs (file
08h,0Ah,0Ch in TIBURON\MODEL01.DAT and file 76h in PIX01.DAT). Crash Bandicoor
3 and Crash Team Racing use 800h-byte for both main & child WADs (although
with garbage padding instead of zeropadding in child WAD headers).<br/>
Unused entries have Offset=0, Size=0.<br/>
Empty 0-byte files (should) have Size=0 and Offset=PrevOffs+PrevSize+Align
(except, Speed Racer has Offset=PrevOffs+PrevSize, ie. without Align for 0-byte
files).<br/>

#### X-Men: Mutant Academy (MagDemo33,50: PSXDATA\WAD.WAD)
This does resemble standard WAD.WAD, but with leading 800h-byte extra stuff.<br/>
```
  000h 4     ID ("PWF ")                                ;\
  004h 4     Total Filesize (707800h)                   ;
  008h 4     Unknown (1)                                ; extra stuff
  00Ch 4     Number of files (N)                        ;
  010h 7F0h  Zerofilled                                 ;/
  800h N*8   File List                                  ;\
  ...  ..    Zerofilled (padding to 800h-byte boundary) ; standard WAD.WAD
  ...  ..    File Data area                             ;/
 File List entries:
  000h 4     File Offset in bytes (increasing, 800h-byte aligned)
  004h 4     File Size in bytes
```
The archive contains child archives in DOT1 format, and in standard WAD.WAD
format (without PWF header).<br/>

#### PKG (Herc/Pandemonium/UnholyWar)
Used by Pandemonium II (JESTERS.PKG, with Files+Folders+Unused entries)<br/>
Used by Herc's Adventure (BIG.BIN, with Files+Unused entries, without Folders)<br/>
Used by Unholy War (MagDemo12:CERBSAMP.PKG, with 0-byte files and nested PKG's)<br/>
Used by 102 Dalmatians (MagDemo40: PTTR\PSXDEMO.PKG)<br/>
```
  000h N*8  File List
  ...  ..   ASCII string (junk, but somewhat needed as nonzero end marker)
  ...  ..   Zeropadding to 800h-byte boundary; not in 4-byte aligned nested PKG
  ...  ..   File Data...
```
The File List can contain Files, Folders, and Unused entries. The overall
format of the list entries is:<br/>
```
  000h 4    Offset in bytes (increasing, or 0=First child)  ;\both FFFFFFFFh
  004h 4    Size in bytes (always nonzero)                  ;/when Unused
```
Files and Folders do have exactly the same format, the only difference is that
Folders will have Offset=00000000h in the NEXT list entry (in other words, the
folder entry is followed by child entries, which start with Offset=0).<br/>
Offsets for Root entries are 800h-byte aligned, relative to begin of PKG file.<br/>
Offsets for Child entries are 4-byte aligned, relative to Parent Folder Offset.<br/>
The last Child entry has Offset+Size+Align(4) = Parent Folder Size.<br/>
The last Root entry has Offset+Size+Align(800h) = Total PKG filesize.<br/>
The last Root entry is usually followed by the ASCII string (which looks like
junk, but it is useful because it equals to NextOffset=Nonzero=NoChilds).<br/>
```
<B>  Example</B>
  00003800h,00000666h   ;root00h          (file 666h bytes, padded=800h)
  00004000h,00000300h   ;root01h\..       (folder 300h bytes, padded=800h)
  00000000h,000000FDh   ;root01h\child00h (file FDh bytes, padded=100h)  ;\300h
  FFFFFFFFh,FFFFFFFFh   ;root01h\child01h (unused)                       ; byte
  00000100h,000001FDh   ;root01h\child02h (file 1FDh bytes, padded=200h) ;/
  00004800h,00001234h   ;root02h          (file 1234h bytes, padded=1800h)
  00006000h,00001234h   ;root03h          (file 1234h bytes, padded=1800h)
  FFFFFFFFh,FFFFFFFFh   ;root04h          (unused)
  00007800h,00001234h   ;root05h          (file 1234h bytes, padded=1800h)
  etc.
```
Notes: Unused entries can occur in both root and child folders (except, of
course, not as first or last entry in child folders). Folders seem to occur
only in root folder (although the format would allow nested folders).<br/>
Alternately, instead of Folders, one can use nested PKG's (the nested ones are
using 4-byte align, without ASCII string and zeropadding in header).<br/>



##   CDROM File Archive BIGFILE.BIG (Gex)
#### Gex (GXDATA\BIGFILE.BIG and nested BIG files therein)
```
  000h 4     Number of Files (eg. F4h)
  004h 0Ch   Zero
  010h N*10h File entries
  ...  4     Archive ID (eg. 00000000h, FF53EC8Bh, or 83FFFFFFh)
  ...  ..    Zeropadding to 800h byte boundary
  ...  ..    File Data
```
File Entries:<br/>
```
  000h 4   Archive ID (same value as in above header)
  004h 4   Filename checksum or so (randomly ordered, not increasing)
  008h 4   Filesize in bytes
  00Ch 4   Fileoffset (800h-byte aligned) (increasing)
```
Filetypes in the archive include...<br/>
```
  looks like a lot of raw data without meaningful file headers...
  file C3h,ECh are raw SPU-ADPCM
  file 08h,09h are nested BIG archives, but with FileEntry[00h]=FF53EC8Bh
  file D9h,DAh are nested BIG archives, but with FileEntry[00h]=83FFFFFFh
```
FileEntry[04h] sometimes has similar continous values (maybe caused by similar
filenames, and using a simple checksum, not CRC32).<br/>



##   CDROM File Archive BIGFILE.DAT (Gex - Enter the Gecko)
#### Gex - Enter the Gecko - BIGFILE.DAT
Used by Gex 2: Enter the Gecko (BIGFILE.DAT)<br/>
Used by Gex 3: Deep Cover Gecko (MagDemo20: G3\BIGFILE.DAT) -- UNSORTED<br/>
Used by Akuji (MagDemo18: AKUJI\BIGFILE.DAT)<br/>
Used by Walt Disney World Racing Tour (MagDemo35: GK\BIGFILE.DAT) -- UNSORTED<br/>
```
  000h 4     Number of Files      (C0h)
  004h N*18h File entries
  ...  ..    Zeropadding to 800h byte boundary
  ...  ..    File Data
```
File Entries:<br/>
```
  000h 4     Random
  004h 4     Filesize in bytes (uncompressed size)
  008h 4     Filesize in bytes (compressed size, or 0=uncompressed)
  00Ch 4     Fileoffset (800h-byte aligned) (increasing, unless UNSORTED)
  010h 4     Random
  014h 4     Random (or ascii in 1st file)
```
LZ Decompression:<br/>
```
  @@collect_more:
   flagbits=[src]+[src+1]*100h+10000h, src=src+2    ;16bit flags, unaligned
  @@decompress_lop:
   if dst>=dst.end then goto @@decompress_done
   flagbits=flagbits SHR 1
   if zero then goto @@collect_more
   if carry=0 then
     [dst]=[src], dst=dst+1, src=src+1
   else
     len=([src] AND 0Fh)+1), disp=([src] AND 0F0h)*10h+[src+1], src=src+2
     if len=1 or disp=0 then goto invalid   ;weirdly, these are left unused
     for i=1 to len, [dst]=[dst-disp], dst=dst+1, next i
   endif
   goto @@decompress_lop
  @@decompress_done:
   ret
```
Filetypes in the archive include...<br/>
```
  standard TIM  (eg. file 01h,02h)
  malformed TIM (eg. file 0Fh,14h) (with [8]=2*cx*cy+4 instead 2*cx*cy+0Ch)
  crippled VAB  (eg. file 0Eh,13h) (with hdr=filesize-4 plus raw ADPCM samples)
  several DNSa  (eg. file 0Dh,12h,17h,BCh) SND sound? (also used by kain)
  PMSa          (eg. Gex 3, World Racing) (SMP spu-adpcm samples)
  there seem to be no nested DAT files inside of the main DAT file
```
Note: same malformed TIMs are also in Legacy of Kain (folder0004h\file0013h).<br/>



##   CDROM File Archive FF9 DB (Final Fantasy IX)
#### DB Archive
```
  000h 1   ID (DBh)
  001h 1   Number of Types
  002h 2   Zero (0)
  004h N*4 Type List
  ...  ..  File Lists & File Data for each Type
```
Type List entries:<br/>
```
  000h 3   Offset to File List (self-relative, from current entry in Type List)
  003h 1   Data Type (00h..1Fh)
```
File List:<br/>
```
  000h 1   Data type (00h..1Fh) (same as in Type List)
  001h 1   Number of Files
  002h 2   Zero (0)
  004h N*2 File ID List (unique ID per type) (different types may have same ID)
  ...  ..  Zeropadding to 4-byte boundary
  ...  N*4 Offset List (self-relative, from current entry in Offset List)
  ...  4   End Offset  (first-relative, from first entry in Offset List)
  ...  ..  File Data (referenced from above Offset List)
```

#### Data Types
```
  00h  Misc (DOT1 Archives, or other files)
  01h  Unused?
  02h  Reportedly 3D Model data (vertices,quads,triangles,texcoords)
  03h  Reportedly 3D Animation sequences
  04h  TIM Texture
  05h  Reportedly Scripts (hdr="EV")              (eg. dir04\file32\1B-0001)
  06h  ?                                          (eg. dir02\file*)
  07h  Sound "Sequencer Data" (hdr="AKAO")        (eg. dir09\file*)
  08h  Sound? tiny files (hdr="AKAO")             (eg. dir04\file32\1B-0001)
  09h  Sound Samples (hdr="AKAO")                 (eg. dir0B\file*)
  0Ah  Reportedly Field Tiles and Field Camera parameters
  0Bh  Reportedly Field Walkmesh                  (eg. dir04\file32\1B-0001)
  0Ch  Reportedly Battle Scene geometry           (eg. dir06\file*)
  0Dh  ?                                          (eg. dir01\file01)
  0Eh  Unused?
  0Fh  Unused?
  10h  ?                                          (eg. dir05\file*)
  11h  ?                                          (eg. dir05\file*)
  12h  Reportedly CLUT and TPage info for models  (eg. dir04\file32\1B-0001)
  13h  Unused?
  14h  ?                                          (eg. dir05\file*)
  15h  Unused?
  16h  ?  (eg. dir04\file32\1B-0001)
  17h  ?  (eg. dir04\file32\1B-0000)
  18h  Sound (hdr="AKAO")  (eg. dir04\file32\1B-0001)
  19h  ?  (eg. dir04\file32\1B-0001)
  1Ah  ?  (eg. dir06\file*)
  1Bh  DB Archives (ie. further DB's nested inside of the parent DB archive)
  1Ch  ?  (eg. dir04\file32\1B-0001)
  1Dh  ?  (eg. dir03\file2328\1B-0001)
  1Eh  ?  (eg. dir04\file32\1B-0001)
  1Fh  ?  (eg. dir04\file32\1B-0001)
  20h..FFh Unused?
```



##   CDROM File Archive Ace Combat 2 and 3
#### Ace Combat 2 (Namco 1997) (ACE2.DAT and ACE2.STH/STP)
There are two archives, stored in three files:<br/>
```
  ACE2.DAT Directory for Data in ACE2.DAT itself         ;normal binary data
  ACE2.STH Directory for Data in separate ACE2.STP file  ;streaming data
```
Directory Format:<br/>
```
  000h 4    Unknown (1)
  004h 4    Number of entries (N)
  008h N*8  File List
```
File List entries (64bit):<br/>
```
  0-27   28bit Size/N (DAT=Size/4, STP=Size/800h)
  28-31  4bit  Type or Channel Number (see below)
  32-63  32bit Offset/800h in ACE2.STP or ACE2.DAT file
```
The files are interleaved depending on the Type/Channel number:<br/>
```
  File    Bit28-31 Channel Sector types...             Interleave Notes
  DAT     0        ch=0    DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD 1:1   data (normal)
  DAT     2        ch=0    DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD 1:1   data (exe)
  STH     0-6      ch=0-6  S.......S.......S.......S....... 1:8   stereo
  STH     8        ch=1    vvvvvvvSvvvvvvvSvvvvvvvSvvvvvvvS 1:1   video+stereo
  Whereas D=data, S=Stereo/Audio, v=video, .=other channels
```
Note: The DAT file does additionally contain PreSizeDOT1 and DOT1 child
archives.<br/>
Demo: The archives in demo version (MagDemo01: ACE2.\*) contain only a handful
of files; the two EXE files in demo DAT archive are only 800h-byte dummy files,
and demo STP is corrupted: Recorded as CDROM image with 920h-byte sectors,
instead of as actual CD-XA sectors).<br/>

#### Ace Combat 3 Electrosphere (Namco 1999) (ACE.BPH/BPB and ACE.SPH/SPB)
There are two archives, stored in four files:<br/>
```
  ACE.BPH Directory for Data in separate ACE.BPB file  ;normal binary data
  ACE.SPH Directory for Data in separate ACE.SPB file  ;streaming data
```
Directory Format:<br/>
```
  000h 4    ID "AC3E" (=Ace Combat 3 Electrosphere)
  004h 4    Type (BPH=3=Data?, SPH=1=Streaming?)
  008h 2    BCD Month/Day?     (Japan=0427h, US=1130h)
  00Ah 2    BCD Year (or zero) (SPH=1999h, BPH=0)
  00Ch 4    Unknown (SPH=0, BPH/US=16CFh or BPH/JP=1484h)
  010h 4    Number of entries (N)
  014h N*8  File List
```
File List entries (64bit), when Bit31=1 (normal entries):<br/>
```
  0-18   19bit Size/N           (BPH=Size/4, SPB=Size/800h)
  19-23  5bit  Channel Number   (BPH=0, SPH=0..1Fh)
  24-26  3bit  Channel Interval (BPH=0, SPH=1 SHL N, eg. 3=Interval 1:8)
  27     1bit  Video Flag       (0=No, 1=Has Video sectors)
  28     1bit  Audio Flag       (0=No, 1=Has Audio sectors)
  29     1bit  Always 1 (except special entries with Bit31=0, see below)
  30     1bit  Unknown (US: Always 1, Japan: 0 or 1)
  31     1bit  Always 1 (except special entries with Bit31=0, see below)
  32-63  32bit Offset/800h in ACE.BPB or ACE.SPB file   (or 0 when bit31=0 ?)
```
File List entries (64bit), when Bit31=0:<br/>
```
  For unknown purpose, the normal entries with Bit31=1 are occassionally   followed by one or more entries with Bit31=0.
  Unknown if those entries do affect the actual storage (like switching to
  different channel numbers, or jumping to non-continous sector numbers).
  That unknown stuff exists in Japanese version only, not in US version.
  0-18   19bit Unknown (maybe some snippet size value in whatever units?)
  19-23  5bit  Always 0     (instead of Channel)
  24-27  4bit  Same as in most recent entry with Bit31=1
  28-31  4bit  Always 5     (instead of Flags)
  32-63  32bit Always 0     (instead of Offset)
```
The files are interleaved depending on the Channel Interval setting (and with
types data/audio/video depending on Flags).<br/>
```
  File    Bit24-31    Sector types...                  Interval  Content
  BPH.US  E0h         DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD 1:1       data
  SPH.US  F8h         SvvvvvvvSvvvvvvvSvvvvvvvSvvvvvvv 1:1       stereo+video
  SPH.US  FBh         S.......v.......S.......v....... 1:8       stereo+video
  SPH.US  F3h         S.......S.......S.......S....... 1:8       stereo
  SPH.US  F4h         S...............S............... 1:16      stereo
  SPH.US  F5h         M............................... 1:32      mono
  BPH.JAP E0h         DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD 1:1       data
  SPH.JAP B8h,F8h     SvvvvvvvSvvvvvvvSvvvvvvvSvvvvvvv 1:1       stereo+video
  SPH.JAP B9h         Svvv....vvvv....Svvv....vvvv.... 1:2 (4:8) stereo+video
  SPH.JAP BAh,FAh     Mv......vv......vv......vv...... 1:4 (2:8) mono+video
  SPH.JAP BBh,FBh     S.......v.......S.......v....... 1:8       stereo+video
  SPH.JAP B3h,F3h     S.......S.......S.......S....... 1:8       stereo
  SPH.JAP B5h,F5h     M............................... 1:32      mono
  Whereas D=data, S=Stereo/Audio, M=Mono/Audio, v=Video, .=Other channels
```
As shown above, interval 1:2 and 1:4 are grouped as 4:8 and 2:8 (ie. 4 or 2
continous sectors per 8 sectors).<br/>
The Subheader's Channel number is specified in the above directory entries,
Subheader's File number is fixed (0 for BPB, and 1 for SPB).<br/>
[CDROM XA Subheader, File, Channel, Interleave](cdromdrive.md#cdrom-xa-subheader-file-channel-interleave)<br/>
The SPB file is about 520Mbyte in both US and Japan, however, the Japanese
version does reportedly contain more movies and some storyline that is missing
in US/EU versions.<br/>
The BPB file contains DOT1 child archives, and Ulz compressed files.<br/>
[CDROM File Compression Ulz/ULZ (Namco)](cdromfileformats.md#cdrom-file-compression-ulzulz-namco)<br/>
The SPB file contains movies with non-standard STR headers (and also uncommon:
interleaved videos on different channels, at least so in the japanese version).<br/>
Demo: The archives do also exist on the demo version (MagDemo30: AC3\\*), but
the .SPB file is corrupted: Recorded as a RIFF/CDXAfmt file, instead of as
actual CD-XA sectors).<br/>



##   CDROM File Archive NSD/NSF (Crash Bandicoot 1-3)
#### NSD/NSF versions
```
  v0  Crash Bandicoot Prototype (oldest known prototype from 08 Apr 1996)
  v1  Crash Bandicoot 1         (retail: S*\*.NSD and .NSF)
  v2  Crash Bandicoot 2         (MagDemo02: CRASH\S0\*.NSD and .NSF)
  v3  Crash Bandicoot 3 Warped  (MagDemo26,50: (S0\*.NSD and .NSF)
```

```
 ____________________________________ NSD _____________________________________
```

#### Overall NSD Structure (v0 contains only the Lookup entries)
```
  0000h 100h*4  Lookup Table, using index=((Filename/8000h) AND FFh) ;\
  0400h 4       Number of Chunks in .NSF file                        ; Lookup
  0404h 4       Number of Files in Lookup File List (N)              ;/
  0408h 4       Level Data Filename (eg. 4F26E8DFh="DATh.L")         ;-LevelDat
  040Ch 4       Bitmap Number of Colors (100h) (P) (0=None)          ;\
  0410h 4       Bitmap Width    (200h or 1B0h) (X) (0=None)          ; Bitmap
  0414h 4       Bitmap Height   (0D8h or 090h) (Y) (0=None)          ;/
  0418h 4       Compression: Offset/800h of first uncompressed chunk ;\
  041Ch 4       Compression: Number of compressed chunks (0..40h)    ; Compress
  0420h 40h*4   Compression: Compressed Chunk List (0=unused entry)  ;/
  ...   N*8     Lookup File List                                     ;-Lookup
  ...   ..      Level Data (size/format varies, see below)           ;-LevelDat
  ...   P*2     Bitmap Palette (16bit values, 8000h..FFFFh)          ;\Bitmap
  ...   X*Y     Bitmap Pixels  (0D8h*200h)                           ;/
```
There are four .NSD versions, which can be distinguished via filesize:<br/>
```
  v0  NSD Filesize=408h + N*8                           ;-Lookup only
  v1  NSD Filesize=520h + N*8 + P*2+X*Y + 210h          ;\
  v2  NSD Filesize=520h + N*8 + P*2+X*Y + 1DCh+S*18h    ; with extra stuff
  v3  NSD Filesize=520h + N*8 + P*2+X*Y + 2DCh+S*18h    ;/
```
Note: v0 is mainly used by the Crash Bandicoot prototype, but the Crash
Bandicoot 1 retail version does also have a few v0 files.<br/>

#### NSD Lookup
The lookup table allows to find files (by filenames) in the NSF files. It does
merely contain the NSF chunk number, so one must load/decompress that chunk to
find the file's exact size/location in that chunk.<br/>
One can create a complete file list by scanning the whole NSF file without
using the NDS lookup table.<br/>
```
 Lookup File List entries (indexed via Lookup Table):
  00h 4   Chunk Number in .NSF file
  04h 4   Filename (five 6bit characters)
```
Filenames:<br/>
```
  0     Type (always 1=Filename) (as opposed to 0=Memory Pointer)
  1-6   5th character ;-Extension  ;\character set is:
  7-12  4th character ;\           ; 00h..09h="0..9"
  13-18 3rd character ; Name       ; 0Ah..23h="a..z"
  19-24 2nd character ;            ; 24h..3Dh="A..Z"
  25-30 1st character ;/           ;/3Eh..3Fh="_" and "!"
  31    Always zero?
```
Special name: 6396347Fh="NONE.!"<br/>

#### NSD Level Data
Level Data exists in NSD v1-v3 (v0 does also have Level Data, but it's stored
in NSF file "DAT\*.L" instead of in the NSD file). There are two major versions:<br/>
```
 Level Data in NSD v1 (or NSF v0 file DAT*.L):
  000h  4       01h                                                  ;\
  004h  4       Level Number (xxh) (same as xx in S00000xx.NSD/NSF)  ;
  008h  4       3807C8FBh = "s0_h.Z" ?                               ; LevelDat
  00Ch  4       Zero                                                 ; v1
  010h  4       Zero                                                 ;
  014h  L*4     Namelist (40h*4)                                     ;
  ...   4       5Ah                                                  ;
  ...   F8h     Zerofilled                                           ;/
 Level Data in NSD v2-v3:
  000h  4       Number of Spawn Points (S)                           ;\
  004h  4       Zero                                                 ;
  008h  4       Level Number (xxh) (same as xx in S00000xx.NSD/NSF)  ; LevelDat
  00Ch  4       Number of Objects? (can be bigger than below list)   ; v2/v3
                  (eg. 1BDh or A5h or E4h)                           ;
  010h  L*4     Namelist for Objects?  (v2=40h*4, or v3=80h*4)       ;
  ...   4       Unknown, always 5Ah (maybe just list end marker?)    ;
  ...   C8h     Zerofilled                                           ;
  ...   S*18h   Spawn Points                                         ;/
```

#### NSD Bitmap
This bitmap is displayed while loading the level.<br/>

#### NSD Compression Info
Compression is only used in v1 (v2-v3 do also have the compression entries at
[418h..51Fh], but they are always zerofilled).<br/>
```
 Compressed Chunk List entries at [420h..51Fh]:
  0-5   Compressed Chunk Size/800h (1..1Fh=800h..F800h bytes, 20h..3Fh=Bad?)
  6-31  Compressed Chunk Offset/800h
```
Note: Crash Bandicoot 1 retail does also have a few uncompressed files (either
v0 files without compression info, or v1 files with zerofilled compression
info).<br/>

```
 ____________________________________ NSF _____________________________________
```

NSF files consist of 64Kbyte chunks (compressed chunks are smaller, but will be
64Kbyte after decompression). Each chunk can contain one or more file(s). That
implies that all files must be smaller than 64Kbyte (larger textures or ADPCM
samples must be broken into multiple smaller files).<br/>
All files (except Textures) are NSF Child Archives which contain one or more
smaller files/items.<br/>

#### NSF Chunk Types
```
 N*8Kbyte-Compressed-chunks:
  000h 2    ID, always 1235h (instead of 1234h)
  002h 2    Zero
  004h 4    Decompressed Size (max 10000h) (usually 9xxxh..Fxxxh, often Fxxxh)
  008h 4    Skip Size (max 40h or so, when last LZSS_len was 40h)
  00Ch ..   Compressed data
  ...  SK   Unused (Skip size)
  ...  ..   Final uncompressed bytes (10000h-compressed_size-skip_size)
 64Kbyte-Texture-chunks:
  000h 2    ID, always 1234h
  002h 2    Chunk Family (1=Texture)
  004h 4    Filename (five 6bit characters)
  008h 4    File Type (5=Texture)
  00Ch 4    Checksum (sum of bytes ar [0..FFFFh], with initial [0Ch]=00000000h)
  010h ...  Zerofilled
  020h ...  Texture data (raw VRAM data, FFE0h bytes?)
 64Kbyte-NonTexture-chunks:
  000h 2    ID, always 1234h
  002h 2    Chunk Family (0=Misc or 2..5=Sound)
  004h 4    Chunk Number*2+1
  008h 4    Number of Files (N) (can be 0, eg. prototype S0000003 chunk21h)
  00Ch 4    Checksum (sum of bytes ar [0..FFFFh], with initial [0Ch]=00000000h)
  010h N*4  File List (Offsets from ID=1234h to entries) (4-byte aligned)
  ...  ..   Offset for end of last File
  ...  ..   File Data (NSF Child Archives) (includes Type/Filename)
  ...  ..   Padding to 10000h-byte boundary
```

#### NSF Child Archives
```
  000h 4    ID, always 0100FFFFh
  004h 4    Filename (five 6bit characters)
  008h 4    File Type (01h..04h, or 06h..15h)
  00Ch 4    Item Count (I)
  010h I*4  Item List (Offsets from ID=0100FFFFh to items) (...unaligned?)
  ...  ..   Offset for end last item
  ...  ..   Data (Items)
```

#### NSF Chunk Loading and Decompression
The compression is a mixup of LZSS and RLE. Compressed chunks are max F800h
bytes tall (10000h bytes after decompression).<br/>
```
  dst=chunk_buffer_64kbyte
  if chunksize is known (from NSD file)
    src=dest=dst+10000h-chunksize
    diskread(fpos,src,chunksize)
  else (when parsing raw NSF file without NSD file)
    src=temp_buffer_64kbyte
    diskread(fpos,src,10000h)
  dst_start=dst, src_start=src
  if halfword[src+00h]<>1234h then   ;check ID (1234h=raw, or 1235h=compressed)
    dst_end=dst+word[src+04h]
    skip_size=word[src+08h]
    src=src+0Ch
    while dst<dst_end
      x=[src], src=src+1
      if x<80h then
        for i=0 to x-1, [dst]=[src], dst=dst+1, src=src+1, next i ;uncompressed
      else
        x=(x AND 7Fh)*100h+[src], src=src+1
        disp=x/8, len=(x AND 7)+3, if len=0Ah then len=40h
        for i=0 to len-1, [dst]=[dst-disp], dst=dst+1, next i     ;compressed
    src=src+src_skip
  if src<>dst then
    while dst<dst_start+10000h, [dst]=[src], dst=dst+1, src=src+1 ;uncompressed
  chunksize=src-src_start  ;<-- compute (when chunksize was unknown)
  fpos=fpos+chunksize      ;<-- fileposition of next chunk
```
As shown above, the chunk is intended to be loaded to the end of the
decompression buffer, so trailing uncompressed bytes would be already in place
without needing further relocation (despite of that intention, the actual game
code is uselessly relocating src to dst, even when src=dst).<br/>
Note: All compressed files seem to have an uncompressed copy with same filename
in another chunk (the NSD Lookup table does probably(?) point to the compressed
variant, which should reduce CDROM loading time).<br/>

```
 _________________________________ Filetypes __________________________________
```

#### Filetype Summary
Below shows File Type, Chunk Family, Extension (5th character of filename), the
version where the type is used, 4-letter type names (as found in the EXE
files), and a more verbose description.<br/>
```
  Typ Family Ext Ver  Name Description
  00h -      !   -    NONE Nothing
  01h 0      V   all  SVTX Misc.Vertices
  02h 0      G   all  TGEO Misc.Model         ;\changed format in v2-v3 ?
  03h 0      W   all  WGEO Misc.WorldScenery  ;/
  04h 0      S   all  SLST Misc.UnknownSLST
  05h 01h    T   all  TPAG Texture.VRAM
  06h 0      L   v0   LDAT Misc.LevelData     ;-stored in NSD in v1-v3
  07h 0      Z   all  ZDAT Misc.Entity        ;-changed format in v2-v3 ?
  08h -      -   -    CPAT Internal?
  09h -      -   -    BINF Internal?
  0Ah -      -   -    OPAT Internal?
  0Bh 0      C   all  GOOL Misc.GoolBytecode
  0Ch 02h    A   v0   ADIO OldSound.Adpcm     ;\type 0Ch
  0Ch 03h    A   all  ADIO Sound.Adpcm        ;/
  0Dh 0      M   all  MIDI Misc.MidiMusic     ;-changed format in v1-v3 ?
  0Eh 04h    N   all  INST Sound.Instruments
  0Fh 0      D   v0-1 IMAG Misc.UnknownIMAG   ;\type 0Fh
  0Fh 0      X   v2-3 VCOL Misc.UnknownVCOL   ;/
  10h -      -   -    LINK Internal?
  11h 0      P   v0-1 MDAT Misc.UnknownMDAT   ;\type 11h
  11h 0      R   v3   RAWD Misc.UnknownRAWD   ;/
  12h 0      U   v0-1 IPAL Misc.Unknown      ;-Crash 1 only? (eg. S0000019.NSF)
  13h 0      B   v1-3 PBAK Misc.DemoPlayback ;-eg. in MagDemo02
  14h 0      V   v0-1 CVTX Misc.UnknownCVTX   ;\type 14h
  14h 05h    O   v2-3 SDIO Speech.Adpcm       ;/
  15h 0      D   v2-3 VIDO Misc.UnknownVIDO
```
As shown above, Type 0Ch is used with family 02h/03h, and Type 0Fh,11h,14h have
two variants each (with different extensions). The Extensions do usually
corresponding with the Types (although extension V,D are used for two different
types each).<br/>

#### See also:
[https://gist.github.com/ughman/3170834]

[https://dl.dropbox.com/s/fu29g6xn97sa4pl/crash2fileformat.html]


#### Weird Note
"Sound entries don't need to be aligned as strictly for most (all?) emulators."<br/>
What does that mean???<br/>
Is there a yet unknown 16-byte DMA alignment requirement on real hardware?<br/>



##   CDROM File Archive STAGE.DIR and \*.DAT (Metal Gear Solid)
Metal Gear Solid (MagDemo13: MGS\\*)<br/>
Metal Gear Solid (MagDemo25: MGS\\*)<br/>
Metal Gear Solid (MagDemo44: MGS\\*) (looks same as in MagDemo13)<br/>
Metal Gear Solid (Retail: MGS\\*)<br/>

#### Summary of ISO files in MGS folder (with filesizes for different releases)
```
  File        MagDemo13/44 MagDemo25  Retail/PAL
  .EXE        9C000h       9C800h     9D800h      ;-executable
  STAGE.DIR   590800h      11A7800h   42AE000h    ;-main archive
  FACE.DAT    2CA000h      3Dh (txt)  358800h     ;-face animation archive
  ZMOVIE.STR  -            -          2D4E800h    ;-movie archive
  DEMO.DAT    149B000h     3Dh (txt)  EC20000h    ;\DAT/SYM combos (the .SYM
  DEMO.SYM    88h          -          -           ; files were leaked in
  VOX.DAT     14F2000h     9F800h     B054800h    ; MagDemo13/MagDemo44 only)
  VOX.SYM     988h         -          -           ;/
  BRF.DAT     -            66800h     575800h     ;\whatever, unknown format(s)
  RADIO.DAT   16CB8h       3Dh (txt)  1AA956h     ;/
```

#### STAGE.DIR:
```
  000h 4     Size of File List (N*0Ch)
  004h N*0Ch Folder List
  ...  ..    Zeropadding to 800h-byte boundary
  ...  ..    Folder Data
 Folder List entries:
  000h 8     Foldername (zeropadded if less than 8 chars)  ;nickname=stg
  008h 4     Offset/800h to File List
 Folder Data (per folder):
  000h 2     Unknown (always 1) (maybe File List size/800h?)
  002h 2     Folder Size/800h (of whole folder, with file list plus file data)
  004h N*8   File List
  ...        Zeropadding to 800h-byte
  800h       Data (for files in current folder)
 File List entries:
  000h 2     File ID (checksum on name)
  002h 1     File Family (one of following chars: "cnrs")
  003h 1     File Type   (one of following chars: "abcdeghiklmoprswz",FFh)
  004h 4     File Size (or File Offset, when File Family="c")
```
Combinations of Family/Type characters are:<br/>
```
  .?a    ???? if any ???? (does NOT exist on PAL disc 1)    ;nickname=azm
  .sb    MIPS binary code  (leading)                        ;nickname=bin
  .cc    Whatever          (eg. vr10\*, s01a\*)             ;nickname=con
  .nd    Texture Archive   (leading) (contains PCX files)   ;nickname=dar
  .rd    Misc Archive      (leading) (eg. init\*)           ;nickname=dar
  .se    Sound Effects?    (trailing)                       ;nickname=efx
  .cg    Whatever, reportedly bytecode functions            ;nickname=gcx
  .ch    Whatever                                           ;nickname=hzm
  .ci    Whatever          (eg. ending\*, s01a\*)           ;nickname=img
  .ck    Whatever, model? aka "pat_xxx" files               ;nickname=kmd
  .cl    Lights, first word = size/10h                      ;nickname=lit
  .sm    Sound Music? Nested DOT1+DOTLESS Archives          ;nickname=mt3
  .co    Whatever "OARa"   (eg. d16e\*, s00a\*, s02c\*)     ;nickname=oar
  .cp    PCX bitmap        (eg. init\*)                     ;nickname=pcc
  .cr    Whatever "sNRJ1F" (eg. roll\*)                     ;nickname=rar
  .cs    Whatever          (eg. d16e\*, s01a\*)             ;nickname=sgt
  .sw    Wave Archive      (trailing)                       ;nickname=wvx
  .cz    Whatever "KMDa"   (eg. s11a, a11c, s14e, s15a)     ;nickname=zmd
  .c,FFh End of Family="c" area                             ;nickname=dar?
```
Files are starting on 800h-byte boundaries. Files with Family="c" are special,
they contain an Offset entries instead of a Size entries, that Offsets are
4-byte aligned (relative to the 800h-byte aligned offset of the first
Family="c" entry), the list of Family="c" entries is terminated by an entry
with Family="c" and Type=FFh (which contains the end-offset of the last
c-Family entry, aka the size of all c-Family entries).<br/>
Note: The above 3-letter nicknames are used on some webpages (unknown why,
maybe they are derived from MGS filename extensions in the PC version).<br/>

#### FACE.DAT (face animations for video calls):
This contains several large blocks (supposedly one per stage, each block having
its own file list). There is no directory to find the begin of the separate
blocks, but one can slowly crawl through the file:<br/>
```
  NextBlock = CurrBlock + 4 + Offset(lastfile)+Size(lastfile) + Align800h
```
The content of each block is:<br/>
```
  000h 4     Number of Files in this block (eg. 19h or 1Ch)
  004h N*0Ch File List for this block
  ...  ..    File Data for this block
  ...  ..    Zeropadding to 800h-byte boundary (followed by next block, if any)
 File List entries:
  000h 2     File Type (0=Main/Eye/Mouth frames, 1=All frames are full size)
  002h 2     File ID (name checksum?)
  004h 4     Filesize in bytes
  008h 4     Offset in bytes, minus 4
```
Type 0 Files in FACE.DAT:<br/>
```
 This type use a single palette for all frames, and only the first frame is
 full 52x89pix, the other frames contain only the update sections (eg. eyes).
  000h 4     Offset to 200h-byte palette       (usually 20h)    ;\Main
  004h 4     Offset to Main Bitmap (52x89pix) (usually 220h)    ;/
  008h 4     Offset to 4th Bitmap  (usually xxxxh or 0=None)    ;\Eyes
  00Ch 4     Offset to 5th Bitmap  (usually xxxxh or 0=None)    ;/
  010h 4     Zero
  014h 4     Offset to 2nd Bitmap  (usually 143Ch or 0=None)    ;\Mouth
  018h 4     Offset to 3rd Bitmap  (usually xxxxh or 0=None)    ;/
  01Ch 4     Zero
  020h 200h  Palette (256 colors) ;\Main
  220h 1218h Main Bitmap          ;/
  1438h 4    Zero
  143Ch ..   2nd Bitmap (if any)  ;\Mouth
  ...   ..   3rd Bitmap (if any)  ;/
  ...   ..   4th Bitmap (if any)  ;\Eyes
  ...   ..   5th Bitmap (if any)  ;/
```
Type 1 Files in FACE.DAT:<br/>
```
 This type use separate palettes for each frame, all frames are full 52x89pix.
  000h 4     Number of frames
  004h N*0Ch Frame List
  ...  200h  1st Frame Palette
  ...  1218h 1st Frame Bitmap (52x89pix)
  ...  4     ?
  ...  200h  2nd Frame Palette
  ...  1218h 2nd Frame Bitmap (52x89pix)
  ...  4     ?
  ...  ..    3rd Frame ...
 Frame List entries:
  000h 4     Offset to Palette
  004h 4     Offset to Bitmap (usually at Palette+200h)
  008h 4     Unknown (often 000x000xh)
```
Bitmap Format (for both Type 0 and Type 1):<br/>
```
  000h 1     Offset X (always 00h in Main Bitmap)
  001h 1     Offset Y (always 00h in Main Bitmap)
  002h 1     Width    (always 34h in Main Bitmap, or less in 2nd-5th bitmap)
  003h 1     Height   (always 59h in Main Bitmap, or less in 2nd-5th bitmap)
  004h ..    Bitmap Pixels at 8bpp (Width*Height bytes)
```

#### DEMO.DAT, DEMO.SYM
#### VOX.DAT, VOX.SYM
The .DAT files contain several huge blocks, found on 800h-boundaries starting
with:<br/>
```
  10 08 00 00 0x 00 00 00 ..
```
The .SYM files (if present) contain Names and .DAT Offsets/800h for those huge
blocks in text format:<br/>
```
  "0xNNNNNNNN name",0Ah
```
VOX.DAT does (among others) contain SPU-ADPCM chunks with 2004h bytes or less,
that is, a 1+3 byte chunk header (01h=SPU-ADPCM, 002004h=Size), plus 2000h byte
or less SPU-ADPCM data.<br/>

#### RADIO.DAT:
Whatever, contains chunks with text messages, chunks are about as so:<br/>
```
  000h 4   Unknown    (eg. 36h,BFh,5Eh,00h)
  004h 4   Unknown    (eg. 03h,13h,00h,00h)
  008h 1   Unknown    (eg. 80h)
  009h 2   Chunk Size (eg. 0xh,xxh)          ;big-endian
  ..   ..  Chunk Data (Chunk Size-2 bytes) (binary stuff, and text strings)
```

#### BRF.DAT:
Contains several "folders" in this format:<br/>
```
  000h 4   Number of files in this folder
  004h ..  File(s)
  ...  ..  01h-padding to 800h-byte boundary
 Files have this format:
  000h ..  Filename ("name.pll",00h)
  ...  ..  Zeropadding to 4-byte boundary (aligned to begin of BRF.DAT)
  ...  4   File data size (usually a multiple of 4)
  ...  ..  File data
  ...  1   Zero (00h)
```
The above "folders" are then followed by several PCX files:<br/>
```
  000h ..  PCX file (starting with 0A,05,01,01 or 0A,05,01,08)
  ...  ..  01h-padding to 800h-byte boundary
```
The first part with .pll files does contain some kind of chunk sizes that could
be used to find the next entry (but that would be very slow).<br/>
The second part with .PCX files doesn't have any chunk sizes at all (though one
could decompress the .PCX file to find the end of each file) (also one could
guess/find them by looking for 0A,05,01,01/08 on 800h-byte boundaries).<br/>

#### ZMOVIE.STR (movie archive with several STR files with subtitles)
[CDROM File Video Streaming STR Variants](cdromfileformats.md#cdrom-file-video-streaming-str-variants)<br/>

#### STAGE.DIR\\*\\*.sb - stage binary/header
This is the first file in most folders (except "init\*" folders).<br/>
The file contains MIPS binary program code. And, there are ascii strings near
end of .sb files, which include filenames, alike:<br/>
```
  "name.c",00h + garbage-padding to 4-byte boundary  ;<-- maybe source code?
  "pat_lamp",00h + zero- padding to 4-byte boundary  ;<-- name for File ID !
```
Those filenames do cover some (not all) of the name checksums in the STAGE.DIR
folder.<br/>

#### STAGE.DIR\\*\\*.cp, STAGE.DIR\\*\\*.nd\.p, BRF.DAT\\* - PCX bitmap files
MGS is using customized/corrupted PCX files as standard texture format (in
STAGE.DIR\\*\\*.cp, STAGE.DIR\\*\\*.nd\\*.p, and BRF.DAT\\*).<br/>
For details on PCX format (and MGS-specific customizations), see:<br/>
[CDROM File Video Texture/Bitmap (PCX)](cdromfileformats.md#cdrom-file-video-texturebitmap-pcx)<br/>
Apart from PCX, there's also custom texture format for animated bitmaps (in
FACE.DAT), and a few TIM images (in STAGE.DIR\init\*\\*.rd\\*.r)<br/>

#### STAGE.DIR\\*\\*.nd - texture archive (with .PCX files)
#### STAGE.DIR\init\*\\*.rd - misc archive (with misc files)
These archives contain several chunks in following format:<br/>
```
  000h 2     File ID (checksum on name?)
  002h 1     File Type (one of following chars: "p" for .nd, or "kors" for .rd)
  003h 1     Zero (00h)
  004h 4     Chunk Size (rounded to 4-byte boundary)
  008h ..    Chunk Data
```
The File Type can be:<br/>
```
  .p    PCX bitmap                      ;-in *\*.nd archives
  .k    Whatever                        ;\
  .o    Whatever "OARa"                 ; in init*\*.rd archives
  .a    Whatever                        ;
  .r    Misc (TIM and other stuff)      ;/
```
There can be 1-2 texture archives per STAGE.DIR folder (both having File
ID=0000h) (probably due to a memory size limit: the game does probably load one
archive with max 300Kbytes, relocate its contents to VRAM, then load the next
archive, if any).<br/>

#### STAGE.DIR\\*\\*.sw - wave archive
There can be one or more .sw files per stage folder (eg. two sw's in
"vr\*\\*.sw").<br/>
```
  000h 4     Unknown (800h or C00h)       ;big-endian
  004h 4     Size of File List (N*10h)    ;big-endian
  008h 8     Zerofilled
  010h N*10h File List (xx,xx,xx,00,00,00,00,7F,00,00,00,0F,00,19,0A,00)
  ...  4     Unknown (40000h or 60000h)   ;big-endian
  ...  4     Size of SPU-ADPCM Data area  ;big-endian
  ...  8     Zerofilled
  ...  ..    SPU-ADPCM Data area (indexed from File List)
 File List entries:
  000h 4     Offset+Flags                 ;little-endian!
               bit0-16  Offset (from begin of SPU-ADPCM Data area)
               bit17    Unknown (0 or 1)
               bit18    Unknown (1)
               bit19-31 Unknown (0)
  004h 12    Whatever (always 00,00,00,7F,00,00,00,0F,00,19,0A,00)
```
The unknown fields might contain volume, ADSR, pitch or the like?<br/>

#### STAGE.DIR\\*\\*.se - sound effects? maybe short midi-like sequences or so?
```
  000h 80h*10h List (unused entries are 1x00000000h,3xFFFFFFFFh)
  800h ..      Data (whatever, usually 14h or more bytes per list entry)
 List entries:
  000h 1       Unknown (eg. 01h,10h,20h,A0h,80h,FFh)    ;\
  001h 1       Number of Voices? (1..3)                 ; all zero for
  002h 1       Unknown (1 or 0)                         ; unused list entries
  003h 1       Unknown (2 or 0 or 1)                    ;/
  004h 4       Offset-800h for 1st Voice?               ;-FFFFFFFFh=Unused
  008h 4       Offset-800h for 2nd Voice? (if any)      ;-FFFFFFFFh=Unused
  00Ch 4       Offset-800h for 3rd Voice? (if any)      ;-FFFFFFFFh=Unused
 Data:
  Seems to contain 4-byte entries (last entry being 00,00,FE,FF).
```

#### STAGE.DIR\\*\\*.sm - whatever nested archives - sound music? mide-like?
This does resemble a DOT1 Parent archive with 1-4 DOTLESS Child archives.
Except, the offsets in Child archives are counted from begin of Parent archive.<br/>
```
 Data:
  Seems to contain 4-byte entries (last entry being 00,00,FE,FF).
```

#### File IDs
File IDs in STAGE.DIR (and maybe elsewhere, too) are computed as so:<br/>
```
  sum=0,
  for i=0 to len(filename)-1
    sum=sum*20h+filename[i]          ;\or so, 16bit overflows might be
    sum=(sum+sum/10000h) AND FFFFh   ;/cropped slightly differently
```
Examples: "abst"=1706h, "selectvr"=8167h.<br/>
Some filenames are empty (name="", ID=0000h).<br/>
Some filenames do match up with the STAGE.DIR foldername.<br/>
Some filenames do match up with strings in .sb file of current folder.<br/>
Other filenames are unknown.<br/>



##   CDROM File Archive DRACULA.DAT (Dracula)
#### Dracula - The Resurrection - DRACULA.DAT (180Mbyte)
```
  000h 4     Zero
  004h 4     Number of Entries (503h)
  008h 4     Zero
  00Ch 4     Random
  010h 10h   Zero
  020h N*10h File List
  ...  ..    Zeropadding to 800h-byte boundary
  ...  ..    Fild Data area
```
File List entries:<br/>
```
  000h 4     Offset/800h
  004h 4     Type (see below for info on different file types)
  008h 4     Filesize in bytes
  00Ch 4     Random (or 0 when Filesize=0)
```
Most of the .DAT file consists of groups of 3 files (with type 01h/40h, 20h and
400h; of which the files with type 20h and 400h may have Size=0=empty).<br/>
```
  Type=00000001h Cubemap           ;\either one of these
  Type=00000040h Cubemap.empty     ;/
  Type=00000020h Cubemap.overlay?  ;\these have size=0 when unused
  Type=00000400h Cubemap.sounds    ;/
```
There are some general purpose files with other types at end of .DAT file:<br/>
```
  Type=00000000h Archive with TIMs         (Size=AB74h)  (" RSC3.1V")
  Type=00000004h Unknown                   (Size=16164h) (00000064h)
  Type=00000008h Related to DRACULA1.STR   (Size=1000h)  (" RTS1.1V")
  Type=00001000h Unknown                   (Size=2000h)  ("BXFS1.1V")
  Type=00008000h Unknown                   (Size=71Dh)   ("  CM1.1V")
  Type=00020000h Unknown                   (Size=3B9h)   (" GSM0.1V")
  Type=02000000h Unknown                   (Size=0h)     (empty)
  Type=00000100h Related to DRACULA1.XA    (Size=1000h)  ("RAAX1.1V")
  Type=00000010h Unknown                   (Size=450h)   (" HYP0.1V")
  Type=00100000h Unknown                   (Size=4014h)  (" xFS1.1V") (x=A1h)
  Type=00000080h Unknown                   (Size=258F4h) (00000010h)
  Type=00000200h TIM (gui charset)         (Size=6E9Eh)  (TIM)
  Type=00010000h TIM (gui buttons)         (Size=10220h) (TIM)
  Type=00040000h Unknown                   (Size=2C4h)   (" TES0.1V")
  Type=00002000h TIM (gui book pages)      (Size=1040h)  (TIM)
  Type=00000800h Cubemap ;\as Type 01h,    (Size=4092Ch) (" RIV3.1V")
  Type=00004000h Cubemap ;/but [10h,14h]=0 (Size=4092Ch) (" RIV3.1V", too)
```
Type 01h - Cubemap:<br/>
```
  000h 8     Name, ASCII, padded with leading spaces (eg. " RIV3.1V")
  008h 4     Something (0, 1 or 2) (unknown, this isn't number of list entries)
  00Ch 4     Zero
  010h 4     Offset to Ext data (ACh)                       ;\ext data
  014h 4     Size of Ext data (eg. 0 or 84h)                ;/
  018h 6*4   Offsets to Side 0-5                            ;\cubemap sides
  030h 6*4   Sizes of Side 0-5 (0, 10220h, or 10820h)       ;/
  048h 44h   Zerofilled
  08Ch 20h   Name, ASCII (eg. "DEBUT0.VR", zeropadded)
  0ACh ..    Ext Data (if any)
  ...  ..    Cubemap TIM sides (if any)
 Note: The cubemap TIMs have 100h or 400h colors (in the latter case: 100h  colors for each quarter of the 8bpp bitmap).
 Note: The TIMs can be arranged as 3D-cubemap with six sides, or as hires
 2D-bitmap (composed of four TIMs, and 2 empty TIMs with size=0).
```
Type 40h - Empty Cubemap:<br/>
```
  Same as Type 01h, but size is always 0ACh (and all seven Size entries are 0)
```
Type 400h - Sound VAG's:<br/>
```
  000h 8     Name, ASCII, padded with leading spaces (eg. " XFS0.1V")
  008h 4     Zero
  00Ch 4     Number of Files (N) (max 10h)
  010h N*10h File List (100h bytes, zeropadded when less than 10h files)
  110h ..    File Data (VAG files)
 File List entries:
  000h 4     Unknown (55F0h, 255F0h or 20000h)
  004h 4     File ID (01010000h, increasing, or other when above=2xxxxh)
  008h 4     Offset in bytes                                ;\.VAG files
  00Ch 4     Filesize in bytes                              ;/
```
Type 20h - Cubemap overlays, polygons, effects or so?:<br/>
```
  000h 8      Name, ASCII, padded with leading dot (eg. ".MNA4.1V")
  008h 4      Zero
  00Ch 4      Random
  010h 4      Unknown 01h
  014h 4      Total Number of 40h-byte blocks (01h..[018h]) (H)
  018h 4      Total Number of 120h-byte blocks (eg. 1Fh,31h) (N)
  01Ch 4      Total Number of 1Ch-byte blocks (eg. 1Eh, 50h, F7h) (M)
  020h 4      Unknown 0 or 1 (in file 4EAh)
  024h 4      Unknown 01h
  028h 6*4    Offsets to Side 0-5 (at end of file and up) (or 0)  ;\cubemap
  040h 6*4    Sizes of Side 0-5   (10220h, or 10820h)     (or 0)  ;/sides
  058h H*40h  40h-byte blocks
  ...  N*120h 120h-byte blocks (related to offsets in 40h-byte blocks)
  ...  M*1Ch  1Ch-byte blocks  (related to offsets in 120h-byte blocks)
  ...  ..     Unknown data     (related to offsets in 1Ch-byte blocks)
  ...  ..     Ext data         (related to Ext offsets in 40h-byte blocks)
  FILE DOES END HERE!
  (below is allocated in above header, but not actually stored in the file)
  (maybe allocated as rendering buffer?)
  ...  -      Cubemap TIM sides
 The 40h-byte blocks are:
  000h 20h    Name (eg. "FLAMMES", zeropadded)
  020h 4      Unknown 01h or 00h
  024h 4      Offset to 120h-byte blocks (usually 98h, or higher)
  028h 4      Unknown 00h
  02Ch 4      Number of 120h-byte blocks (01h..[018h])
  030h 4      Unknown 01h
  034h 4      Ext Offset                ;\usually all zero
  038h 4      Ext Size (3C000h)         ; (except, nonzero in file 4EAh)
  03Ch 4      Ext Random (checksum?)    ;/
 The 120h-byte blocks are:
  000h 18h*4  List with Offsets to 1Ch-byte blocks (usually 4 entries nonzero)
  060h 18h*4  List with Zeroes
  0C0h 18h*4  List with Numbers of 1Ch-byte blocks (usually max 4 entries)
 The 1Ch-byte blocks are:
  000h 4      Unknown 04h
  004h 4      Width   20h or 10h
  008h 4      Height  20h or 10h or 30h
  00Ch 4      Unknown 60h or 10h
  010h 4      Unknown 00h or 30h
  014h 4      Offset to Unknown Data
  018h 4      Size of Unknown Data (Width*Height*1)
```
Type 00h - TIMs:<br/>
```
  000h 8      Name (" RSC3.1V")
  008h 8      Zerofilled
  010h 4      Number of used entries (1Fh) (max 80h)
  014h 80h*4  Offset List    (offsets to files) (A14h and up)
  214h 80h*4  Zero List      (zerofilled)
  414h 80h*4  Size List      (filesizes)
  614h 80h*4  Width List     (0Ch,18h,34h,2Ch) (in pixels)
  814h 80h*4  Height List    (0Ch,24h,34h,2Ch)
  A14h ..     Data (TIM files, with mouse pointers)
```



##   CDROM File Archive Croc 1 (DIR, WAD, etc.)
#### Croc 1 (MagDemo02: CROC\\*) (plus more files in retail version)
CROCFILE.DIR and CROCFILE.1:<br/>
```
 CROCFILE.DIR:
  000h 4     Number of Entries (N)
  004h N*18h File List
  ...  4     Checksum (sum of all of the above bytes)
 CROCFILE.1:
  000h ..    File Data (referenced from .DIR)
 File List entries:
  000h 0Ch   Filename ("FILENAME.EXT", zeropadded if shorter)
  00Ch 4     File Size in bytes (can be odd) (including 8 byte for size/chksum)
  010h 4     File Offset in .1 file (unaligned, can be odd, increasing)
  014h 4     Zero (0)
```
CROCFILE.DIR\MP\*.MAP (and MAP files inside of MAP\*.WAD and MP090-100\_\*.WAD):<br/>
```
  000h 4    Size-8 of whole file (or Size-0 for those in MP*.WAD)
  004h 4    Flags? (usually 0Ch or 14h)
  008h 1    Filename length                (including trailing 00h, if any)
  009h ..   Filename ("P:\CROC\EDITOR\MAPS\..\*.MAP") (+00h in MAP05*.WAD)
  ...  ..   Unknown
  ...  1    Description length
  ...  ..   Description (eg. "Default New Map")
  ...  ..   Unknown
  ...  (4)  Checksum of whole file (sum of all bytes) (not in MP*.WAD)
```
CROCFILE.DIR\\*.WAD:<br/>
```
 MAP*.WAD:
  000h 4    Size-8 of whole file
  004h ..   MAP file(s) (each with size/checksum, same format as MP*.MAP)
  ...  4    Checksum of whole file (sum of all of the above bytes)
 CROC.WAD, CROCSLID.WAD, EXCLUDE.WAD, MP*.WAD, OPTIONS.WAD, SWIMCROC.WAD:
  000h 4    Size-8 of whole file
  004h 4    Offset-8 to SPU-ADPCM data area
  008h ..   Data File area (model.MOD anim.ANI, bytecode.BIN, header.CVG, etc.)
  ...  ..   SPU-ADPCM data area (if any, note in CROCSLID.WAD and OPTIONS.WAD)
  The Data File area contains several "files" but doesn't have any directory
  with filename/offset/size. The only way to find the separate files seems to
  be to detect the type/filesize of each file, and then advance to next file
  (bytecode.BIN files start with a size entry, but files like .MOD or .ANI
  require parsing their fileheader for computing filesize).
  Note: The PC version reportedly has .WAD files bundled with .IDX file (that
  makes it easier to find files and filenames).
  Note: The STRAT.DIR file contains a list of filenames used in .WAD files
  (but lacks info on offset/size, so it isn't really useful).
```
CROCFILE.DIR\\*.BIN:<br/>
```
 Sound.BIN Files (CROCFILE.DIR\AMBI*.BIN, MAP*.BIN, JRHYTHM.BIN, REVERB.BIN):
  000h 4    Size of .SEQ file                   ;\if any (not in REVERB.BIN)
  004h ..   SEQ file (starting with ID "pQES")  ;/
  ...  4    Size of .VH file                    ;\always present
  ...  ..   VH file (starting with ID "pBAV")   ;/
  ...  ..   VB file (sample data, SPU-ADPCM data, up to end of file)
 Music.BIN files (MAGMUS.BIN, MUSIC.BIN):
  000h 4      Size-8 of whole file (118h)
  004h ..     Increasing 32bit values ;sector numbers in PACK*.STR files or so?
  ...  4      Unknown (2EEh or 258h) (aka 750 or 600 decimal)
  ...  ..     Zeropadding
  11Ch 4      Checksum (sum of all of the above bytes)
  Note: MUSIC.BIN has an extra copy (without chksum) in EXCLUDE.WAD\MUSIC.BIN
 Ascii.BIN files (CREDITS*.BIN, MNAME.BIN):
  000h 4      Size-8 of whole file
  004h (2)    Type or so? (02h,01h) (only in CREDITS*.BIN, not in MNAME.BIN)
  ...  ..     Ascii strings (each string is: len,"text string",unknown)
  ...  4      Checksum (sum of all of the above bytes)
 Texture.BIN files (type 4) (STILLGO.BIN, STILLST.BIN, STILLTL.BIN):
  000h 2      Type (4=Texture/uncompressed, with 0Eh-byte list entries)
  002h 1      Zero (maybe Extra6byte as in type 5,6 Texture.BIN files)
  003h 2      Number of List entries (N) (always 4B0h in all three files)
  005h 2      Number of Texture Pages (usually 2)
  007h 2      Zero (maybe Unknown/Animation as in type 5,6 Texture.BIN files)
  009h N*0Eh  Polygon List (?,?,?,?,?,?, x1,y1, x2,y1, x1,y2, x2,y2)
  ...  40000h Texture Page uncompressed data (two pages, 20000h bytes each)
  ...  4      Checksum (sum of all of the above bytes)
 Texture.BIN files (type 5,6) (ENDTEXT*.BIN, FONT.BIN, FRONTEND.BIN,
 OUTRO.BIN, PUBLISH.BIN, STILL*.BIN, TB*.BIN, TK*.BIN, TPAGE213.BIN):
  000h 4      Zero (0)               (in TPAGE213.BIN: Size-8 of whole file)
  004h 2      Type (6=Texture/RLE16) (in TPAGE213.BIN: 5=Texture/uncompressed)
  006h 1      Extra6byte flag/size (0=None, 3=Extra6byte: TB*.BIN, TPAGE*.BIN)
  ...  (6)    Extra6byte data (unknown purpose, only present when [006h]=3)
  ...  2      Number of Polygon List entries (N)
  ...  2      Number of Texture Pages (usually 1) (in TK*_ENM.BIN: usually 2)
  ...  2      Number of Unknown Blocks (0=None, or 1,2,4,8)
  ...  (..)   Unknown Block(s), if any
  ...  2      Number of Animation Blocks (0=None)
  ...  (..)   Animation Block(s), if any
  ...  N*0Ch  Polygon List (?,?,?,?, x1,y1, x2,y1, x1,y2, x2,y2)  ;x,y or y,x?
  ...  (4)    Texture Page compressed size (T1) ;\only when [004h]=Type=6
  ...  (T1)   Texture Page compressed data      ;/
  ...  (4)    Texture Page compressed size (T2) ;\only when [004h]=Type=6
  ...  (T2)   Texture Page compressed data      ;/     and NumPages=2
  ...  20000h Texture Page uncompressed data    ;-only when [004h]=Type=5
  ...  4      Checksum (sum of all of the above bytes)
  Unknown Block(s):
  (Unknown purpose, each Unknown Block has the format shown below)
  000h 2    Unknown (looks like some index value, different for each entry)
  002h 2    Number of Unknown Items (eg. 1 or 2 or 4)
  004h ..   Unknown Items (NumItems*6 bytes) (three halfwords each?)
  Animation Block(s):
  (This is supposedly used to update portions of the Texture Page for
  animated textures, each Animation Block has the format shown below)
  000h 2    Number of Bitmap Frames in this Animation (usually 8)
  002h 2    Bitmap Width (in halfword units)
  004h 2    Bitmap Height
  006h 2    Unknown (1 or 3)                    ;\
  008h 2    Unknown (C10h, CC8h, 1E8h, or xxxh) ; maybe vram X,Y address?
  00Ah 2    Unknown (0)                         ;/
  00Ch ..   Bitmap Frames (Width*2*Height*NumFrames bytes, uncompressed)
  Croc 1 RLE16 compression:
  This is using unsigned little-endian 16bit LEN/DATA pairs, LEN can be:
   0000h..7FFFh --> Load one halfword, fill 1..8000h halfwords
   8000h..FFFFh --> Copy 1..8000h uncompressed halfwords
  BUG: Texture pages should be 20000h bytes (256x256 halfwords), but for
  whatever reason, the size of decompressed data can be 1FFEAh, 1FFF0h,
  1FFFAh, 20000h, or 20002h.
 Bytecode.BIN (inside of .WAD files):
  000h 4    Size of whole file
  004h ..   Whatever bytecode (starting with initial 16bit program counter?)
 Unknown.BIN (last 1-2 file(s) in EXCLUDE.WAD file):
  000h 4     Number of entries (N)
  004h N*18h Whatever
  ...  4     Checksum (sum of above bytes)
  Unknown purpose, retail version has one such file (with 0Ah entries), demo
  version has two such files (with 0Ah and 4Eh entries. The files start with:
  0A,00,00,00,00,00,00,00,00,00,64,00,00,00,EB,FF,...  ;demo+retail
  4E,00,00,00,00,00,64,00,00,00,50,00,00,00,64,00,...  ;demo
```
CROCFILE.DIR\\*.MOD<br/>
```
 Demo version has one .MOD file in CROCFILE.DIR (retail has more such files):
  000h 2     Number of Models (N) (1 or more) (up to ECh exists)     ;\header
  002h 2     Flags (0 or 1)                                          ;/
  004h N*Var SubHeadersWithData  ;see below                          ;-data
  ...  4     Checksum (sum of all of the above bytes)                ;-checksum
  SubHeadersWithData(N*Var):
  004h 4     Radius                                                  ;\
  008h 48h   Bounding Box[9*8] (each 8byte are 4x16bit: X,Y,Z,0)     ; for each
  050h 4     Number of Vertices (V)                                  ; model
  054h V*8   Vectors (4x16bit: X,Y,Z,0)                              ;
  ...  V*8   Normals (4x16bit: X,Y,Z,0)                              ;
  ...  4     Number of Faces (F) (aka Polygons?)                     ;
  ...  F*14h Faces   (8x16bit+4x8bit: X,Y,Z,0,V1,V2,V3,V4, Tex/RGB)  ;
  ...  2     Number of collision info 1? (X)     ;\                  ;
  ...  2     Number of collision info 2? (Y)     ; only if           ;
  ...  X*2Ch Collision info 1?                   ; Flags.bit0=1      ;
  ...  Y*2Ch Collision info 2?                   ;/                  ;/
 There are further .MOD models inside of .WAD files, with slightly
 re-arranged entries (and additional reserved/garbage fields):
  000h 2     Number of Models (N) (1 or more) (up to ECh exists)     ;\
  002h 2     Flags (0 or 1)                                          ; header
  004h 4     Reserved/garbage (usually 224460h) (or 22C9F4h/22DF54h) ;/
  008h (4)   Number of Models WITH Data arrays (M)                   ;\
  00Ch (M*2) Model Numbers WITH Data arrays (increasing, 0..N-1)     ; ext.hdr
  ...  (..)  Padding to 4-byte boundary (garbage, usually=M)         ;/
  ...  N*68h Subheader(s)   ;see below                               ;-part 1
  ...  N*Var DataArray(s)   ;see below                               ;-part 2
  Subheaders(N*68h):
  000h 4     Radius                                                  ;\
  004h 48h   Bounding Box[9*8] (each 8byte are 4x16bit: X,Y,Z,0)     ; for each
  04Ch 4     Number of Vertices (V)                                  ; model
  050h 4     Reserved/garbage (usually 0022xxxxh)                    ;
  054h 4     Reserved/garbage (usually 0022xxxxh)                    ;
  058h 4     Number of Faces (F) (aka Polygons?)                     ;
  05Ch 4     Reserved/garbage (usually 0022xxxxh)                    ;
  060h 2     Number of collision info1? (X)                          ;
  062h 2     Number of collision info2? (Y)                          ;
  064h 4     Reserved/garbage (usually 0022xxxxh) or xxxxxxxxh)      ;/
  DataArrays(N*Var) with sizes V,F,X,Y from corresponding Subheader:
  (if ext.hdr is present, then below exists only for models listed in ext.hdr)
  000h V*8   Vectors (4x16bit: X,Y,Z,0)                              ;\
  ...  V*8   Normals (4x16bit: X,Y,Z,0)                              ; for each
  ...  F*14h Faces   (8x16bit+4x8bit: X,Y,Z,0,V1,V2,V3,V4, Tex/RGB)  ; model
  ...  X*2Ch Collision info 1?                                       ;
  ...  Y*2Ch Collision info 2?                                       ;/
 The ext.hdr mentioned above exists only in some .MOD files (usually in one of
 the last chunks of MP*.WAD). Files with ext.hdr have N>1, Flags=1 (but files
 without ext.hdr can also have those settings). Files with ext.hdr do usually
 have uncommon garbage values at hdr[4], which isn't too helpful for detection.
 The only way to detect models with ext.hdr seems to be to check if the ext.hdr
 contains valid increasing entries in range 0..N-1.
 WAD's that do contain a model with ext.hdr do usually also contain an extra
 100h-byte file, that file contains N bytes for model 0..N-1 (plus zeropadding
 to 100h-byte size), the bytes are supposedly redirecting models without Data
 Arrays to some other data source.
 The 100h-byte files don't have any header or checksum, they contain up to 9Ch
 entries (so there's always some zeropadding to 100h), the existing 100h-byte
 files contain following values in first 4 bytes (as 32bit value):
  04141401h, 0C040017h, 01010101h, 09030503h, 0A0B0A0Bh, 03020102h, 0C060900h,
  00060501h, 04040201h, 01010203h, 01030201h, 05000302h, 0C040317h, or Zero.
  To distinguish from other files: BIN/MAP files start with a 4-byte aligned
  Size value; if Size=0 or (Size AND 3)>0 or Size>RemainingSize then it's
  probably a 100h-byte file. Best also check if last some bytes are zeropadded.
 Exceptions:
  Retail MP090..MP100_*.WAD has model with ext.hdr, but no 100h-byte file
  Demo MP041_00.WAD has model with ext.hdr, with zerofilled 100h-byte file
 Note: Some models have ALL models listed in ext.hdr (which is about same as
 not having any ext.hdr at all; except, they ARE bundled with 100h-byte file).
```
CROCFILE.DIR\MP\*.DEM<br/>
```
 Some (not all) MP*.WAD files are bundled with MP*.DEM files, supposedly
 containing data for demonstration mode. There are two versions:
  demo version:   size 2584h (9604 decimal) (some files with partial checksum)
  retail version: size 0E10h (3600 decimal) (without checksum)
```
CROCFILE.DIR\CROCWALK.ANI:<br/>
```
 Animation data, there is only one such file in CROCFILE.DIR:
  000h 2       Value (100h)
  002h 2       Number of Triggers (T) (2)
  004h (T*2)   Trigger List (with 2x8bit entries: FrameNo, TriggerID)
  ...  ..      Probably, Padding to 4-byte boundary (when T=odd)
  ...  4       Number of entries 1 (X)
  ...  X*18h   Whatever Array 1
  ...  4       Number of entries 2 (Y) (usually/always 64h)
  ...  X*Y*4   Whatever Array 2
  ...  4       Number of entries 3 (Z) (usually/always 0Ah)
  ...  X*Z*18h Whatever Array 3
 There are further .ANI files inside of .WAD files:
  000h 2       Value (100h or 200h)                         ;Animation Speed?
  002h 2       Number of Triggers (T) (0, 1, 2, 3, 5, or 9)
  004h 4       Garbage/Pointer (usually 224460h) (or zero)
  008h 4       Number of entries 1 (X) (1 or more)          ;Num Frames
  00Ch 4       Garbage/Pointer (usually 22C9F4h) (or 224460h or 22DF54h)
  010h 4       Number of entries 2 (Y) (usually 64h) (or 0) ;Num Vertices (?)
  014h 4       Garbage/Pointer
  018h 4       Number of entries 3 (Z) (usually 0Ah) (or 6 or 9)
  01Ch 4       Garbage/Pointer
  020h (T*2)   Trigger List (with 2x8bit entries: FrameNo, TriggerID)
  ...  ..      Padding to 4-byte boundary (garbage, usually=X)
  ...  X*18h   Whatever Array 1
  ...  X*4     Garbage/Pointers (0021EE74h,0021EE74h,xxx,...)
  ...  X*Y*4   Whatever Array 2   ;Vertex 3x10bit?            ;only if Y>0
  ...  (X*4)   Garbage/Pointers (0021EE74h,0021EE74h,xxx,...) ;only if Y>0
  ...  X*Z*18h Whatever Array 3
```
CROCFILE.DIR\TCLD.CVG:<br/>
```
 There is only one such file in CROCFILE.DIR:
  000h 4      Size-8 of whole file
  004h 4      Unknown (0)
  008h 4      Unknown (1)
  00Ch ..     SPU-ADPCM data
  ...  4      Checksum (sum of all of the above bytes)
 There are further .CVG files inside of .WAD files, these consist of two
 parts; 0Ch-byte Headers (in the data file area), and raw SPU-ADPCM data
 (in the spu-adpcm data area at end of the .WAD file):
  Header(0Ch):
  000h 4      Size+8 of data part
  004h 4      Unknown (0)
  008h 4      Unknown (0 or 1)
  Data(xxxx0h):
  000h ..     SPU-ADPCM data (starting with sixteen 00h bytes)
```
STRAT.DIR (in retail version with extra copy in CROCFILE.DIR\STRAT.DIR):<br/>
```
 This file contains a list of filenames for files inside of .WAD files, but
 it does NOT tell where those files are (in which WAD at which offset).
  000h 4     Number of Entries (N)
  004h N*xxh File List (retail=14h bytes, or demo=18h bytes per entry)
  ...  4     Checksum (sum of all of the above bytes)
 List entries are:
  demo:   entrysize=18h  ;Filename(0Ch)+Size(4)+Zeroes(8)
  retail: entrysize=14h  ;Filename(0Ch)+        Zeroes(8)
 The list contains hundreds of filenames, with following extensions:
  *.BIN  byte-code strategies
  *.MOD  models
  *.ANI  animations
  *.CVG  spu-adpcm voice data
 These "filenames" seem to be actually solely used as "memory handle names":
  MemoryHandle(#1) = LoadFile("FILENAME.BIN")  ;<-- names NOT used like this
  MemoryHandle("FILENAME.BIN") = LoadFile(#1)  ;<-- names used like this
```
PACK\*.STR (retail version only):<br/>
```
  Huge files with XA-ADPCM audio data
```
MAGMUS.STR (demo version only):<br/>
```
  Huge mis-mastered 24Mbyte file (contains several smaller XA-ADPCM blocks,
  accidentally stored in 800h-byte FORM1 data sectors, instead of 914h-byte
  FORM2 audio sectors).
```
ARGOLOGO.STR, FOXLOGO.STR<br/>
```
  MDEC movies
```
COPYRIGHT.IMG, WARNING.IMG<br/>
```
  Raw bitmaps (25800h bytes, uncompressed, 320x240x16bpp)
```
CUTS\\*.AN2 (looks like cut-scenes with polygon-streaming):<br/>
[CDROM File Video Polygon Streaming](cdromfileformats.md#cdrom-file-video-polygon-streaming)<br/>
Note: MOD/ANI files contain many Reserved/Garbage/Pointer entries which are
replaced by pointers after loading (the initial values seem to have no purpose;
they are aften set to constants with value 002xxxxxh which could be useful for
file type detection, but they vary in different game versions).<br/>
See also:<br/>
[https://github.com/vs49688/CrocUtils/] (for PC version, PSX support in progress)<br/>



##   CDROM File Archive Croc 2 (DIR, WAD, etc.)
#### Croc 2 (MagDemo22: CROC2\CROCII.DIR\T\*.WAD+DEM)
#### Disney's The Emperor's New Groove (MagDemo39: ENG\KINGDOM.DIR\T\*.WAD+DEM)
#### Disney's Aladdin in Nasira's Rev. (MagDemo46: ALADDIN\ALADDIN.DIR\T\*.WAD+DEM)
#### Alien Resurrection, and Harry Potter 1 and 2 ... slightly different format?
Overall .WAD format:<br/>
```
  000h 4      Total Filesize+/-xx (-4 or +800h or +1800h)
  004h 4+4+.. XSPT Chunk        ;Textures
  ...  4+4+.. XSPS Chunk        ;SPU-ADPCM Sound (if any, not in all .WAD's)
  ...  4+4+.. XSPD Chunk        ;...whatever Data...?
  ...  4+4    DNE Chunk         ;End marker (in Harry Potter: with data!)
```
XSPT Chunk (Textures):<br/>
```
  000h 4        Chunk Name "XSPT" (aka TPSX backwards)
  004h 4        Chunk Size (excluding 8-byte Name+Size)
  008h 4        Chunk Flags (02h or 06h or 0Eh)  ;02h in Croc 2
  00Ch (20h)    Name (eg. "Default new map", zeropadded)  ;\if Flags bit2=1
  ...  (804h)   Unknown ... SAME as in XSPD chunk !!!     ;/
  ...  4        Number of List 1 entries (N1) (xxh..xxxh) ;\
  ...  4        Number of Texture Pages (1..4)            ; List 1 and NumPages
  ...  N1*0Ch   List 1 Whatever (6B 2F xx 00..)           ;/
  ...  4        Number of List 2 entries (N2) (0..xxh)    ;\
  ...  4        Unknown (2 or 7)                          ; List 2
  ...  N2*04h   List 2 Whatever (halfwords?) (if N2>0)    ;/
  ...  (5*C00h) Whatever, 5*C00h, Palette+Stuff?          ;-if Flags bit3=1
  ...  ..       RLE16 compressed Texture Pages            ;-Texture bitmap
 RLE16 Texture notes:
  Compressed data consists of signed little-endian 16bit LEN+DATA pairs:
   LEN=0000h        --> invalid/unused
   LEN=0001h..7FFFh --> copy LEN halfwords from src
   LEN=8000h..FFFFh --> load ONE halfword as fillvalue, fill -LEN halfwords
  Compressed size is everything up to end of XSPT chunk
  Decompressed size is 20000h*NumTexturePages (=20000h,40000h,60000h or 80000h)
  That is: Width=256 halfwords, height 256*NumTexturePages lines. There seems
  to be only one RLE16 compression block for all Texture Pages, rather than one
  RLE16 block for each Page.
 BUG #1: Decompressed data in Aladding/Emperor does often contain only
  1FFFEh,3FFFEh,5FFFEh,7FFFEh bytes (the decompressed data has correct size
  when appending ONE halfword with random/zero value).
 BUG #2: Compressed data in Croc 2 ends with a RLE16 length value (-LEN), but
  lacks the corresponding RLE16 filldata (the decompressed data is 7FFFEh when
  filling those LEN halfwords with random/zero values).
```
XSPS Chunk (SPU-ADPCM Sound) (if any, isn't present in all .WAD files):<br/>
```
  000h 4      Chunk Name "XSPS" (aka SPSX backwards)       ;\
  004h 4      Chunk Size (excluding 8-byte Name+Size)      ; header
  008h 4      Chunk Flags (0 or 3 or 7)                    ;/
  00Ch 4      Number of Sounds (N1) (1..xxh)               ;\always present
  010h N1*14h Sound List                                   ;/
  ...  (4)     VAB/VH Size                                 ;\if Flags=3 or 7
  ...  (..)    VAB/VH Header                               ;/   (bit0 or bit1?)
  ...  (4)     Unknown (2 or 4)                            ;-if Flags=3 or 7
  ...  (4)     Whut (N2)                                   ;\if Flags.bit2=1
  ...  (N2*10h) Whut List (4 words: xxh,10h,xxxx00h,xxxx0h);/
  ...  4       Size of all Part 1 Sound Data blocks               ;\always
  ...  ..      SPU-ADPCM Sound Data (referenced from Sound List)  ;/
  ...  (4)     Size of all Part 2 Sound Data blocks (+8)          ;\if Flags=
  ...  (..)    SPU-ADPCM Sound Data (referenced from Sound List?) ;    3 or 7
  ...  (8)     Zero                                               ;/
 Sound List entries (as in FESOUND.WAD):
  000h 4    Sample Rate in Hertz (AC44h=44100Hz, 5622h=22050Hz, 3E80h=16000Hz)
  004h 2    Sample Rate Pitch    (1000h=44100Hz, 0800h=22050Hz, 05CEh=16000Hz)
  006h 2    Unknown (7Fh)
  008h 4    Unknown (1)          (1)               (8)
  00Ch 4    Unknown (42008Fh)    (1FC0001Fh)       (40008Fh)
  010h 4    Filesize             (xxx0h)           (xxx0h)
```
XSPD Chunk:<br/>
```
  000h 4     Chunk Name "XSPD" (aka DPSX backwards)
  004h 4     Chunk Size (excluding 8-byte Name+Size)
  008h 4     Flags-and/or-other stuff ? (eg. 00000094h or 0A801094h)
  00Ch 804h  Unknown ... SAME as in XSPT chunk !!!
  810h ..    Unknown ...
```
DNE Chunk (End marker):<br/>
```
  000h 4     Chunk Name " DNE" (aka END backwards)
  004h 4     Chunk Size (0)           (except, in Harry Potter: nonzero)
  ...  ..    Data (usually none such) (except, in Harry Potter: with data!)
```
Additional DEM files (always 1774h bytes) (if any, not all .WAD's have .DEM's):<br/>
```
  000h 4     Number of entries (N) (always 2EEh, aka 750 decimal)
  004h N*8   Whatever entries... maybe data for demonstration mode?
```
See also:<br/>
[http://wiki.xentax.com/index.php/Argonaut\_WAD]




##   CDROM File Archive Headerless Archives
#### Headerless Archives
Some games use files that contain several files badged together. For example,<br/>
```
  PSX Resident Evil 2, COMMON\DATA\*.DIE contains TIM+VAB badged together
  PSX Resident Evil 2, COMMON\DATA\*.ITP contains 1000h-byte aligned TIMs
  Blaster Master, DATA\MENU\*\*.PRT contains three smaller TIMs badged together
  Blaster Master, DATA\MENU\*\*.BG contains three bigger TIMs badged together
  Misadventures of Tron Bonne, KATWA\*.BIN contains headerless archives (with TIMs and audio)
  Headerless BSS files contain several BS files with huge padding inbetween
```
To some level one could detect & resolve such cases, eg. TIM contains
information about the data block size(s), if the file is bigger, then there may
be further file(s) appended.<br/>
Some corner cases may be: Files with odd size may insert alignment padding
before next file. Archives with 800h-byte filesize resolution will have
zeropadding (or garbage) if the real size isn't a mutiple of 800h. Regardless
of that two cases, archives may use zeropadding to 800h-byte or even
10000h-byte boundaries (as workaround one could skip zeroes until reaching a
well-aligned nonzero word or double word (assuming that most files start with
nonzero values; though not always, eg. raw ADPCM or raw bitmaps).<br/>



##   CDROM File Compression
#### Compressed Bitmaps
```
  .BS used by several games (and also in most .STR videos)
  .GIF used by Lightspan Online Connection CD
  .JPG used by Lightspan Online Connection CD
  .BMP with RLE4 used by Lightspan Online Connection CD (MONOFONT, PROPFONT)
  .BMP with RLE8+Delta also used by Online Connection CD (PROPFONT\ARIA6.BMP)
  .PCX with RLE used by Jampack Vol. 1 (MDK\CD.HED\*.pcx)
  .PCX with RLE used by Hot Wheels Extreme Racing (MagDemo52: US_01293\MISC\*)
  .PCX with RLE used by Metal Gear Solid (slightly corrupted PCX files)
```

#### Compressed Audio
```
  .XA uses XA-ADPCM (and also used in .STR videos)
  .VAG .VB .VAB uses SPU-ADPCM
```

#### Compressed Files
[CDROM File Compression LZSS (Moto Racer 1 and 2)](cdromfileformats.md#cdrom-file-compression-lzss-moto-racer-1-and-2)<br/>
[CDROM File Compression LZSS (Dino Crisis 1 and 2)](cdromfileformats.md#cdrom-file-compression-lzss-dino-crisis-1-and-2)<br/>
[CDROM File Compression LZSS (Serial Experiments Lain)](cdromfileformats.md#cdrom-file-compression-lzss-serial-experiments-lain)<br/>
[CDROM File Compression ZOO/LZSS](cdromfileformats.md#cdrom-file-compression-zoolzss)<br/>
[CDROM File Compression Ulz/ULZ (Namco)](cdromfileformats.md#cdrom-file-compression-ulzulz-namco)<br/>
[CDROM File Compression SLZ/01Z (chunk-based compressed archive)](cdromfileformats.md#cdrom-file-compression-slz01z-chunk-based-compressed-archive)<br/>
[CDROM File Compression LZ5 and LZ5-variants](cdromfileformats.md#cdrom-file-compression-lz5-and-lz5-variants)<br/>
[CDROM File Compression PCK (Destruction Derby Raw)](cdromfileformats.md#cdrom-file-compression-pck-destruction-derby-raw)<br/>
[CDROM File Compression GT-ZIP (Gran Turismo 1 and 2)](cdromfileformats.md#cdrom-file-compression-gt-zip-gran-turismo-1-and-2)<br/>
[CDROM File Compression GT20 and PreGT20](cdromfileformats.md#cdrom-file-compression-gt20-and-pregt20)<br/>
[CDROM File Compression HornedLZ](cdromfileformats.md#cdrom-file-compression-hornedlz)<br/>
[CDROM File Compression LZS (Gundam Battle Assault 2)](cdromfileformats.md#cdrom-file-compression-lzs-gundam-battle-assault-2)<br/>
[CDROM File Compression BZZ](cdromfileformats.md#cdrom-file-compression-bzz)<br/>
[CDROM File Compression RESOURCE (Star Wars Rebel Assault 2)](cdromfileformats.md#cdrom-file-compression-resource-star-wars-rebel-assault-2)<br/>
[CDROM File Compression TIM-RLE4/RLE8](cdromfileformats.md#cdrom-file-compression-tim-rle4rle8)<br/>
[CDROM File Compression RLE_16](cdromfileformats.md#cdrom-file-compression-rle16)<br/>
[CDROM File Compression PIM/PRS (Legend of Mana)](cdromfileformats.md#cdrom-file-compression-pimprs-legend-of-mana)<br/>
[CDROM File Compression BPE (Byte Pair Encoding)](cdromfileformats.md#cdrom-file-compression-bpe-byte-pair-encoding)<br/>
[CDROM File Compression RNC (Rob Northen Compression)](cdromfileformats.md#cdrom-file-compression-rnc-rob-northen-compression)<br/>
[CDROM File Compression Darkworks](cdromfileformats.md#cdrom-file-compression-darkworks)<br/>
[CDROM File Compression Blues](cdromfileformats.md#cdrom-file-compression-blues)<br/>
[CDROM File Compression Z (Running Wild)](cdromfileformats.md#cdrom-file-compression-z-running-wild)<br/>
[CDROM File Compression ZAL (Z-Axis)](cdromfileformats.md#cdrom-file-compression-zal-z-axis)<br/>
[CDROM File Compression EA Methods](cdromfileformats.md#cdrom-file-compression-ea-methods)<br/>
[CDROM File Compression ZIP/GZIP/ZLIB (Inflate/Deflate)](cdromfileformats.md#cdrom-file-compression-zipgzipzlib-inflatedeflate)<br/>
[CDROM File Compression LArc/LHarc/LHA (LZS/LZH)](cdromfileformats.md#cdrom-file-compression-larclharclha-lzslzh)<br/>
[CDROM File Compression UPX](cdromfileformats.md#cdrom-file-compression-upx)<br/>
[CDROM File Compression LZMA](cdromfileformats.md#cdrom-file-compression-lzma)<br/>
[CDROM File Compression FLAC audio](cdromfileformats.md#cdrom-file-compression-flac-audio)<br/>
Some other archvies that aren't used by any PSX games, but, anyways...<br/>
[CDROM File Compression ARJ](cdromfileformats.md#cdrom-file-compression-arj)<br/>
[CDROM File Compression ARC](cdromfileformats.md#cdrom-file-compression-arc)<br/>
[CDROM File Compression RAR](cdromfileformats.md#cdrom-file-compression-rar)<br/>
[CDROM File Compression ZOO](cdromfileformats.md#cdrom-file-compression-zoo)<br/>
[CDROM File Compression nCompress.Z](cdromfileformats.md#cdrom-file-compression-ncompressz)<br/>
[CDROM File Compression Octal Oddities (TAR, CPIO, RPM)](cdromfileformats.md#cdrom-file-compression-octal-oddities-tar-cpio-rpm)<br/>
[CDROM File Compression MacBinary, BinHex, PackIt, StuffIt, Compact Pro](cdromfileformats.md#cdrom-file-compression-macbinary-binhex-packit-stuffit-compact-pro)<br/>

#### Compressed Archives
Some Archives have "built-in" compression.<br/>
[CDROM File Archive WAD (Doom)](cdromfileformats.md#cdrom-file-archive-wad-doom)<br/>
[CDROM File Archive BIGFILE.DAT (Gex - Enter the Gecko)](cdromfileformats.md#cdrom-file-archive-bigfiledat-gex-enter-the-gecko)<br/>



##   CDROM File Compression LZSS (Moto Racer 1 and 2)
#### Moto Racer 1 ("LZSS" with len+2) (MagDemo03: MRDEMO\IMG\\*.TIM)
#### Moto Racer 2 ("LZSS" with len+3) (MagDemo16: MR2DEMO\IMG\\*.TIM and .TPK)
```
  000h 4     ID "LZSS"
  004h 4     Decompressed Size
  008h ..    Compressed Data
```
This LZSS variant is unusually using 6bit len and 10bit disp. And, there are
two versions: Moto Racer 1 uses len+2, and Moto Racer 1 uses len+3. There is no
version information in the header, one workaround is to decompress the whole
file with len+2, and, if the resulting size is too small, retry with len+3.
Observe that the attempt with len+2 may cause page faults (eg. if the sum of
len values is smaller than disp; so allocate some extra space at begin of
compression buffer, or do error checks),<br/>
```
  @@collect_more:
   flagbits=[src]+100h, src=src+1    ;8bit flags
  @@decompress_lop:
   flagbits=flagbits SHR 1
   if zero then goto @@collect_more
   if carry=1 then
     [dst]=[src], dst=dst+1, src=src+1
   else
     disp=([src]+[src+1]*100h) AND 3FFh, len=([src+1]/4)+2_or_3, src=src+2
     if disp=0 then goto @@decompress_done
     for i=1 to len, [dst]=[dst-disp], dst=dst+1, next i
   endif
   goto @@decompress_lop
  @@decompress_done:
   ret
```



##   CDROM File Compression LZSS (Dino Crisis 1 and 2)
#### Dino Crisis 1 and 2 (PSX\DATA\\*.DAT and \*.DBS and \*.TEX, File type 7,8)
Dino Crisis LZSS Decompression for files with type 7 and 8:<br/>
```
  @@collect_more:
   flagbits=[src]+100h, src=src+1    ;8bit flags
  @@decompress_lop:
   flagbits=flagbits SHR 1
   if zero then goto @@collect_more
   if carry=1 then
     [dst]=[src], dst=dst+1, src=src+1
   else
     disp=[src]+[src+1]*100h AND FFFh, len=[src+1]/10h+2, src=src+2
     if disp=0 then error
     for i=1 to len, [dst]=[dst-disp], dst=dst+1, next i
   endif
   if src<src_end then goto @@decompress_lop
   ret
```
The compressed file & archive header don't contain any info on the
decompressed size (except, for compressed bitmaps, the archive header does
contain width/height entries, nethertheless the decompressed file is usually
BIGGER then width\*height\*2 (it can contain padding, plus 8 bytes).<br/>



##   CDROM File Compression LZSS (Serial Experiments Lain)
Serial Experiments Lain is using LZSS compression for TIMs (in SITEA.BIN,
SITEN.BIN), and for Transparency Masks (in LAPKS.BIN).<br/>

#### Serial Experiments Lain (7MB SITEA.BIN on Disc 1, 5MB SITEB.BIN on Disc 2)
These are huge 5-7 Mbyte files with hundreds of chunks. Each chunk contains one
compressed TIM.<br/>
```
 Each chunk is having this format:
  000h 4     Chunk ID "napk"
  004h 4     Decompressed size
  008h ..    LZSS compressed TIM data
  ...  ..    Zeropadding to 800h-byte boundary
```
Unknown how the game is accessing chunks (there is no chunk size info, so one
would need read the whole file (or at least first 4-byte of each 800h-byte
sector) for finding chunks with ID="napk").<br/>

#### Serial Experiments Lain (LAPKS.BIN on Disc 1 and 2)
This a huge 14Mbyte file with 59 chunks. Each chunk contains one or more 24bpp
.BS images with black background (the images in each chunk are forming a short
animation sequence; width/height may vary because all images are cropped to
rectangles containing non-black pixels).<br/>
```
 Each chunk is having this format:
  000h 4     Chunk ID "lapk"
  004h 4     Chunk size (excluding 8-byte chunk header, excluding zeropadding)
  008h 4     Number of Files in this Chunk (N)
  00Ch N*0Ch File List
  ...  ..    File Data (bitmaps in .BS v0 format with uncommon headers)
  ...  ..    Zeropadding to 800h-byte boundary
 File List entries:
  000h 4     Offset in bytes (zerobased, from begin of File Data area)
  004h 2     Bitmap Width/2 + some 3bit value in LSBs?
  006h 2     Bitmap Height
  00Ch 4     Zero
 File Data (bitmaps in .BS v0 format with uncommon headers):
  000h 2     Bitmap Width
  002h 2     Bitmap Height
  004h 2     Quant for Y1,Y2,Y3,Y4
  006h 2     Quant for Cr,Cb
  008h 4     Size of compressed BS Bitstream plus 4 ;Transparency at [008h]+0Ch
  00Ch 2     Size/2 of MDEC data (after huffman decompression, without padding)
  00Eh 2     BS Version (0) (actually MSBs of above Size, but it's always 0)
  010h ..    BS Bitstream with DC and AC values (Huffman compressed MDEC data)
  ...  4     Transparency Mask Decompressed Size (Width*Height*2/8) (=2bpp)
  ...  ..    Transparency Mask LZSS-compressed data
```
BUG: The chunksize at C3A800h is set to 4C614h but should be 4D164h (the next
chunk starts at C88000h).<br/>
Unknown how the game is accessing chunks (crawling all chunks would be
exceptionally slow due to CDROM seek times, and won't work with the BUGGED
chunksize).<br/>

#### Decompression function
This LZSS variant is unusually using 8bit len and 8bit disp.<br/>
```
   dst_end=dst+[src], src=src+4   ;decompressed size
  @@collect_more:
   flagbits=([src] SHL 24)+800000h, src=src+1    ;8bit flags
  @@decompress_lop:
   if dst=dst_end then goto @@decompress_done
   flagbits=flagbits SHL 1    ;32bit shift with carry-out/zeroflag
   if zero then goto @@collect_more
   if carry=0 then
     [dst]=[src], dst=dst+1, src=src+1
   else
     disp=[src]+1, len=[src+1]+3, src=src+2
     for i=1 to len, [dst]=[dst-disp], dst=dst+1, next i
   endif
   goto @@decompress_lop
  @@decompress_done:
   ret
```



##   CDROM File Compression ZOO/LZSS
#### Jarret & LaBonte Stock Car Racing (MagDemo38: WTC\\*.ZOO)
```
  0000h 4     Decompressed Size                          ;\1st sector
  0004h 7FCh  Garbage                                    ;/
  0800h 4     Decompressed Size (same as above)          ;\2nd sector
  0804h 7FCh  LZSS compressed data, part 1               ;/
  1000h 800h  LZSS compressed data, part 2               ;-3rd sector
  1800h 800h  LZSS compressed data, part 3               ;-4th sector
  ...   ..    etc.
```
Note: The file format & compression method is unrelated to ZOO archives (to
distinguish between the formats: ZOO archives have [0014h]=FDC4A7DCh, the
ZOO/LZSS files have [0014h]=Garbage).<br/>
The decompressed WTC\\*.ZOO files can contain large TIMs, or chunk-based
archives (where each chunk can contain one or more small TIMs), or other stuff.<br/>

#### Decompression function
```
  decompress_file:
   if LittleEndian32bit[src+14h]=FDC4A7DCh then goto error ;refuse ZOO archives
   if LittleEndian32bit[src]<>LittleEndian32bit[src+800h] then goto error
   curr=src+800h
   src=curr+4
  @@sector_lop:
   call decompress_sector
   curr=curr+800h
   src=curr
   if src<src_end then goto @@sector_lop
   ret
  ;---
  decompress_sector:
  @@collect_more:
   flagbits=([src] SHL 24)+800000h, src=src+1    ;8bit flags
  @@decompress_lop:
   flagbits=flagbits SHL 1    ;32bit shift with carry-out/zeroflag
   if zero then goto @@collect_more
   if carry=0 then
     [dst]=[src], dst=dst+1, src=src+1
   else
     disp=[src]*100h+[src+1], src=src+2
     if disp=FFFFh then goto @@decompress_done
     len=(disp/800h)+3, disp=(disp AND 7FFh)+1
     for i=1 to len, [dst]=[dst-disp], dst=dst+1, next i
   endif
   goto @@decompress_lop
  @@decompress_done:
   ret
```



##   CDROM File Compression Ulz/ULZ (Namco)
Ulz/ULZ uses fairly normal LZSS compression, unusually with variable Len/Disp
ratio, three separate data streams (flg/lz/dta), and rather weird end check in
version=0.<br/>

#### Ulz Format (Ace Combat 3 Electrosphere, Namco)
#### Ulz Format (Klonoa, MagDemo08: KLONOA\FILE.IDX\\*)
```
  000h 4    ID ("Ulz",1Ah) (parts lowercase)
  004h 3    Decompressed Size in bytes
  007h 1    Version (0 or 2)
  008h 3    Offset to Uncompressed data   <-- reportedly can be 0 in version=0?
  00Bh 1    Number of Disp bits (DispBits=N, LenBits=16-N) (usually 0Ah..0Dh)
  00Ch 4    Offset to Compressed data
  010h ..   Compression Flags   (32bit entries)
  ...  ..   Uncompressed data   (8bit entries)
  ...  ..   Zeropadding to 4-byte boundary
  ...  ..   Compressed data     (16bit entries)
```
Most files use version=2 (eg. US:ACE.BPH\0006h\000Fh contains DOT1 with TIMs).<br/>
Some files use version=0 (eg. US:ACE.BPH\0048h\\*\\* contains TIMs).<br/>

#### ULZ Format (Time Crisis, Namco)
```
  000h 4    ID ("ULZ",1Ah) (all uppercase)
  004h 2    Zero
  006h 1    Version (0 or 2)
  007h 1    Number of Disp bits (DispBits=N, LenBits=16-N) (usually 0Ah..0Dh)
  008h 4    Offset to Uncompressed data
  00Ch 4    Offset to Compressed data
  010h 4    Decompressed Size in bytes
  014h ..   Compression Flags   (32bit entries)
  ...  ..   Uncompressed data   (8bit entries)
  ...  ..   Zeropadding to 4-byte boundary
  ...  ..   Compressed data     (16bit entries)
```
Most files use version=2 (eg. EUR: AD\*\TIM\*.FHT\\*)<br/>
Some files use version=0 (eg. EUR: AD4\TIM0\_0.FHT\0018h, 0019h)<br/>

#### Ulz/ULZ Decompression Function
```
  if [src+00h]="Ulz",1Ah then
    version   = Byte[src+07h]
    disp_bits = Byte[src+0Bh]
    dst_end   = LittleEndian24bit[src+04h] + dst
    src_dta   = LittleEndian24bit[src+08h] + src
    src_lz    = LittleEndian32bit[src+0Ch] + src
    src_flg   = src + 10h
    add_len   = 3
    flg_1st   = 31  ;process flag bit31 first
  if [src+00h]="ULZ",1Ah then
    version   = Byte[src+06h]
    disp_bits = Byte[src+07h]
    src_dta   = LittleEndian32bit[src+08h] + src
    src_lz    = LittleEndian32bit[src+0Ch] + src
    dst_end   = LittleEndian32bit[src+10h] + dst
    src_flg   = src + 14h
    add_len   = 2
    flg_1st   = 0   ;process flag bit0 first
  collected = 80000000h   ;initially empty, plus stop bit
 @@decompress_lop:
  if version=2 AND dst=dst_end then goto @@decompress_done
  flag = collected AND 80000000h
  collected=collected*2
  if collected=0
    collected = LittleEndian32bit[src_flg], src_flg=src_flg+4
    if flg_1st=0 then ReverseBitOrder(collected)  ;or make custom/faster code
    flag = collected AND 80000000h
    if version=0 AND collected=0 then goto @@decompress_done
    if version=0 then collected=collected*2       ;<-- has implied stop bit
    if version=2 then collected=collected*2 + 1   ;<-- shift-in stop bit
  if flag=0     ;compressed
    disp = LittleEndian16bit[src_lz], src_lz=src_lz+2
    len  = (disp SHR disp_bits) + add_len
    disp = (disp AND ((1 shl disp_bits)-1)) + 1
    for i=1 to len, [dst]=[dst-disp], dst=dst+1, next i
  else          ;uncompressed
    [dst]=[src_dta], dst=dst+1, src_dta=src_dta+1
  goto @@decompress_lop
 @@decompress_done:
  ret
```
Note: Version=2 has 32 flags per 32bit. Version=0 has 31 flags and 1 stop bit
per 32bit, plus 32 null bits at end of data (which is all rather wasteful,
there's no good reason to use version=0).<br/>



##   CDROM File Compression SLZ/01Z (chunk-based compressed archive)
SLZ/01Z files are Chunk-based archives with one or more compressed chunk(s).<br/>
Used by Hot Shots Golf 2 (retail: DATA\F0000.BIN\\*, MagDemo31/42:
HSG2\MINGOL2.BIN\\*)<br/>

#### SLZ/01Z chunk headers
The archive consists of Chunk(s) in following format:<br/>
```
  000h 3     ID (either "01Z" or "SLZ", both are used)
  003h 1     Method (00h=Uncompressed, 01h=LZSS, 02h=LZSS+FILL)
  004h 4     Compressed size (SIZ) (same as decompressed when Method=0)
  008h 4     Decompressed size
  00Ch 4     Distance to next chunk, if any (SIZ+10h+Align4, or 0=None)
  010h SIZ   Compressed data
```

#### SLZ/01Z  decompression function:
```
   method=byre[src+3]
   len=word[src+8]
   src=src+10h
   if method=0 then
     for i=1 to len, [dst]=[src], dst=dst+1, src=src+1, next i
     goto @@decompress_done
   dst_end = dst+len
  @@collect_more:
   flagbits=[src]+100h, src=src+1    ;8bit flags
  @@decompress_lop:
   if method=2 AND dst=dst_end then goto @@decompress_done
   flagbits=flagbits SHR 1
   if zero then goto @@collect_more
   if carry=1 then
     [dst]=[src], dst=dst+1, src=src+1
   else
     disp=([src]+[src+1]*100h) AND 0FFFh, len=([src+1]/10h)+3, src=src+2
     if method=1 AND disp=0 then goto @@decompress_done
     if method=2 AND len=12h then     ;special fill mode...
       len=disp/100h+3, val=disp AND FFh               ;len=3..12h
       if len=3 then len=val+13h, val=[src], src=src+1 ;len=13h..112h
       for i=1 to len, [dst]=val, dst=dst+1, next i    ;len=4..112h
     else
       for i=1 to len, [dst]=[dst-disp], dst=dst+1, next i
   endif
   goto @@decompress_lop
  @@decompress_done:
   ret
```



##   CDROM File Compression LZ5 and LZ5-variants
#### Original LArc LZ5 (method "-lz5-")
LZ5 was used by LArc compression tool from 1988/1989, decompression is also
supported by LHarc/LHA. LZ5 is basically LZSS compression, but with some
oddities:<br/>
```
  LZ5 is often implemented with a ringbuf (instead of actual sliding window)
  LZ5 uses absolute ringbuf indices (instead of relative sliding dest indices)
  LZ5 requires the ringbuf to be initially prefilled with constants
  LZ5 ringbuf is 1000h bytes tall and starts with write index FEEh
```
LArc was discontinued in 1989, but LZ5-variants have been kept used on PSX and
Nintendo DSi; those variants are just using the raw compression, without LArc
archive headers.<br/>

#### DSi Dr. Mario (DSiware, Nintendo/Arika, 2008-2009)
```
 INFO.DAT
  encrypted directory with filename, offset and compressed/uncompressed size
 GAME.DAT
  000h 4   ID "ALZ1"
  004h ... ALZ1 Compressed data (with size as defined in INFO.DAT)
  ...  4   ID "ALZ1"
  ...  ... ALZ1 Compressed data (with size as defined in INFO.DAT)
  ...
```

#### PSX Final Fantasy VII (FF7)
ALZ1 compression is used in various folders (ENEMY\*, STAGE\*, STARTUP, MAGIC,
FIELD, MINI, MOVIE, WORLD) with various filename extensions (.LZS .BSX .DAT
.MIM .TIZ .PRE .BSZ .TXZ).<br/>
```
  000h 4   Compressed Size       ;=Filesize-4
  004h ..  ALZ1 Compressed data (Filesize-4 bytes)
```
Detection can be more or less reliably done by checking [000h]=Filesize-4, one
could also check the filename extensions, although .DAT doesn't qualify as
unique extension.<br/>
The file doesn't contain any info on the decompressed size, so one cannot know
the decompression buffer size without first decompressing the file.<br/>
Note: For whatever reason, the game does also have one GZIP compressed file
(BATTLE\TITLE.BIN).<br/>

#### PSX Final Fantasy VIII (FF8)
About same as FF7, but detection is less reliable because there are no
filenames or extensions, and the file header is somewhat randomly set to
[000h]=(Filesize-4)+0..7, unknown why, maybe it's allocating dummy bytes to
last some compression flags.<br/>
```
  000h 4   Compressed Size+0..7  ;=(Filesize-4)+0..7
  004h ..  ALZ1 Compressed data (Filesize-4 bytes)
```
ALZ1 is used in four Root files (0001h,0002h,0017h,001Ah), and in many Field
files, and maybe in further files elsewhere.<br/>

#### PSX Ultimate Fighting Championship (MagDemo38: UFC\CU00.RBB\383h\\*)
```
  000h 8     ID "00zLATAD" (aka DATALz00 backwards)               ;\PreHeader
  008h 4     Total Filesize excluding PreHeader+Padding (SIZ+0Ch) ;/
  00Ch 4     Unknown (always 1000h)                               ;\
  010h 4     Compressed data size                       (SIZ)     ; Header
  014h 4     Decompressed data size                               ;/
  018h SIZ   zLATAD Compressed data                               ;-Data
  ...  ..    Padding to 4-byte boundary                           ;-Padding
```

#### Ninja (MagDemo13: NINJA\LOADPICS\\*.PAK and NINJA\VRW\FOREST.VRW\\*)
```
  000h 8     ID "VRAM-WAD"
  008h 4     Compressed size (Filesize-Padding-10h)
  00Ch 4     Decompressed size       (18000h, 28000h, 40000h bytes)
  010h ..    VRAMWAD Compressed data (192x256, 320x256, 512x256 halfwords)
  ...  (..)  Padding to 4-byte boundary (if any, in files in .VRW archives)
```
Observe that Ninja is using the same ID="VRAM-WAD" for .PAK files and .VRW
archives (if [008h]=Filesize-Padding-10h then it's a compressed .PAK file,
otherwise it's a .VRW archive; whereas, those .VRW archives do themselves
contain several .PAK files).<br/>

#### PSX Power Spike (MagDemo43: POWER\GAME.IDX\\*.BIZ)
BIZ compression is used in BIZ archives (which are nested in IDX/HUG archive).
The compressed & decompressed size is stored in the BIZ archive.<br/>
Note: Power Spike 20h-filled initial BIZ ringbuf is required for sky pixels in:<br/>
```
  MagDemo43: POWER\GAME.IDX\PERSOS\PSX\CUSTOM\\TEXTURE\NFIELD.BIZ\LPORJ.PSI
```

#### PSX Army Men Air Attack 2 (MagDemo40: AMAA2\\*.PCK\\*.PAK)
SCRATCH compression is used in PAK archives (which are nested in PCK archive).
The compressed & decompressed size is stored in the PAK archive.<br/>
Note: The decompressor uses half of the 1Kbyte Scratchpad RAM at 1F800000h as
ringbuf (hence the name and unusual small 200h-byte ringbuf size).<br/>

#### Alice in Cyberland (ALICE.PAC\\*.FA2)
```
  000h ..   FA2 Compressed .FA archive
```
The decompressor is at 80093A3Ch (but the code isn't permanently in memory),
and it's by far one of the worst decompression functions in compilerland.<br/>

#### Decompression
```
   DEFAULT = ALZ1 or BIZ or LZ5
   if DEFAULT then wr=0FEEh, mask=FFFh    ;\
   if VRAMWAD then wr=0FEEh, mask=FFFh    ; initial ringbuf write index
   if zLATAD  then wr=0000h, mask=FFFh    ; and ringbuf mask (size-1)
   if SCRATCH then wr=01BEh, mask=1FFh    ;
   if FA2     then wr=00EFh, mask=0FFh    ;/
   if FA2     then len2=0
   initialize_ringbuf_content (see below)
   numbits=0
  @@decompress_lop:
   if dst>=dst.end then goto @@decompress_done
   if numbits=0
     flagbits=[src], numbits=8, src=src+1    ;8bit flags
   numbits=numbits-1
   if VRAMWAD or FA2 then flagbits SHL 1, else flagbits=flagbits SHR 1
   if carry=1 then
     dta=[src], [dst]=dta, ringbuf[wr AND mask]=dta
     dst=dst+1, wr=wr+1, src=src+1
   else
     if DEFAULT then rd=[src]+([src+1]/10h)*100h), len=([src+1] AND 0Fh)+3
     if zLATAD  then rd=[src]+([src+1] AND 0Fh)*100h), len=([src+1]/10h)+3
     if SCRATCH then rd=[src]+([src+1]/80h)*100h), len=([src+1] AND 7Fh)+3
     if VRAMWAD then rd=[src+1]+([src]/10h)*100h), len=([src] AND 0Fh)+3
     if FA2     then rd=[src], len=len2, len2=0, src=src+1
     if FA2 and len=0 then len=[src]/10h+2, len2=([src] AND 0Fh)+2, src=src+1
     if FA2=0   then src=src+2
     for i=1 to len   ;read ringbuf[rd] (instead of relative [dst-rd])
       dta=ringbuf[rd AND mask], [dst]=dta, ringbuf[wr AND mask]=dta
       dst=dst+1, wr=wr+1, rd=rd+1
     next i
   endif
   goto @@decompress_lop
  @@decompress_done:
   ret
```

#### Initial Ringbuf Content
```
  if ALZ1 or zLATAD then
    ringbuf[000h..FFFh]=(00h)              ;zeroes
  if VRAMWAD then
    ringbuf[000h..FEDh]=(00h)              ;zeroes
    ringbuf[FEEh..FFFh]=(uninitialized)    ;uninitialized, don't use
  if BIZ then
    ringbuf[000h..FEDh]=(20h)              ;ascii space
    ringbuf[FEEh..FFFh]=(uninitialized)    ;uninitialized, don't use
  if SCRATCH then
    ringbuf[000h..1BFh]=(00h)              ;zeroes
    ringbuf[1C0h..1FFh]=(uninitialized)    ;uninitialized, don't use
  if FA2 then
    ringbuf[000h..0FFh]=(00h)              ;zeroes
  if LZ5 then
    ringbuf[000h..CFFh]=(000h..CFFh)/0Dh   ;increasing, repeated 0Dh times each
    ringbuf[D00h..DFFh]=(00h..FFh)         ;increasing
    ringbuf[E00h..EFFh]=(FFh..00h)         ;decreasing
    ringbuf[F00h..F7Fh]=(00h)              ;zeroes
    ringbuf[F80h..FEDh]=(20h)              ;ascii space
    ringbuf[FEEh..FFFh]=(should be 00h)    ;see note, better don't use
```
Note: The last 12h bytes in LZ5 are 00h in LArc v3.33 (though unknown if that's
intended and stable), LHarc source code did accidentally set them to 20h (which
is reportedly fixed in later LHA versions).<br/>



##   CDROM File Compression PCK (Destruction Derby Raw)
#### Destruction Derby Raw (MagDemo35: DDRAW\\*.PCK,EXE,DAT)
```
  000h 3     Decompressed size (24bit, little-endian)
  003h 1     Unused (0)
  004h ...   LZSS compressed data, starting with 30bit+2bit flags
```
The compression is used in some ISO files, which can be detected as:<br/>
```
  [03h]=00h, [04h]=00h, [08h]="PS-X EXE"                ;DDRAW\*.EXE
  [03h]=00h, [04h] AND FCh=00h, [08h]="BC",04h,40h,0,0  ;DDRAW\LDPICS\*.PCK
```
The compression is also used in nested PTH+DAT archives (where the whole DAT is
compressed), which can be detected by checking if the sum of the PTH filesizes
exceeds the DAT filesize.<br/>

#### Self-decompressing GUI code in PSX BIOS for SCPH-7000 and up
The PSX BIOS seems to use the same LZSS format for the self-decompressing GUI
code (with GUI/decompression starting at 80030000h).<br/>

#### Decompression function
```
   dst_end=dst+LittleEndian24bit[src], src=src+4
  @@collect_more:
   flagbits=BigEndian32bit([src]), src=src+4
   dispbits=14-(flagbits AND 03h), flagbits=(flagbits OR 3)-1
   dispmask=(1 SHL dispbits)-1
  @@decompress_lop:
   flagbits=flagbits SHL 1    ;32bit shift with carry-out/zeroflag
   if zero then goto @@collect_more
   if carry=0 then
     [dst]=[src], dst=dst+1, src=src+1
   else
     disp=BigEndian16bit[src], src=src+2
     len=(disp SHR dispbits)+3
     disp=(disp AND dispmask)+1
     for i=1 to len, [dst]=[dst-disp], dst=dst+1, next i
   endif
   id dst<dst_end then goto @@decompress_lop
  @@decompress_done:
   ret
```



##   CDROM File Compression GT-ZIP (Gran Turismo 1 and 2)
#### BS iki Video
IKI is a rather uncommon variant of the .STR video format (used by Gran Turismo
1 and 2, Legend of Legaia, Legend of Dragoon, Omega Boost, Um Jammer Lammy).<br/>
IKI videos have a custom .BS header, including some GT-ZIP compressed data:<br/>
```
  000h 2   MDEC Size/4 (after huffman decompression) (rounded to 80h/4 bytes)
  002h 2   File ID (3800h)
  004h 2   Bitmap Width in pixels     ;instead quant
  006h 2   Bitmap Height in pixels    ;instead version
  008h 2   Size of GT-ZIP compressed data (plus 2-byte alignment padding)
  00Ah ..  GT-ZIP compressed DC/Quant values (plus 2-byte alignment padding)
  ...  ..  Huffman compressed AC data blocks (Cr,Cb,Y1,Y2,Y3,Y4, Cr,Cb,Y1,Y2..)
```
The number of blocks is NumBlocks=(Width+15)/16\*(height+15)/16\*6. The size of
the decompressed GT-ZIP data is NumBlocks\*2.<br/>

#### Gran Turismo 1 (MagDemo10: GT\\*.DAT) - headerless
#### Gran Turismo 1 (MagDemo15: GT\\*.DAT) - headerless
```
  000h ..    Compressed Data (without header)
```
This is used for compressing files inside of GT-ARC archives (or in one case,
for compressing the whole GT-ARC archive). The GT-ARC directory contains
additional compression info, see GT-ARC description for details.<br/>
The file GT\GAMEFONT.DAT is also GT-ZIP compressed, but lacks any ID or info on
decompressed size, and there are at least two GAMEFONT.DAT versions (in
MagDemo10 va MagDemo15), both versions are 8000h byte when decompressed, and
compressed data starts with 00,FF,FF,00,00,00,80,00,00,01,17,07.<br/>

#### Gran Turismo 2 (MagDemo27: GT2\GT2.VOL\arcade\arc\_other.tim\\*) - with header
```
  000h 0Ch   ID "@(#)GT-ZIP",0,0
  00Ch 4     Decompressed Size
  010h ..    Compressed Data (unknown compressed size due to below padding)
  ...  ..    Zeropadding to 4-byte boundary (when stored in DOT1 archives)
```
This is used for compressing some files in one DOT1 archive (most other files
in Gran Turismo 2 are using GZIP compression; with corrupted/zeropadded GZIP
footers).<br/>

#### Decompression function
```
   if [src]="@(#)GT-ZIP",0,0 then dst.end=dst+[src+0Ch], src=src+10h
  @@collect_more:
   flagbits=[src]+100h, src=src+1    ;8bit flags
  @@decompress_lop:
   if src>=src.end then goto @@decompress_done  ;(when src.end is known)
   if dst>=dst.end then goto @@decompress_done  ;(when dst.end is known)
   flagbits=flagbits SHR 1
   if zero then goto @@collect_more
   if carry=0 then
     [dst]=[src], dst=dst+1, src=src+1
   else
     len=[src], src=src+1, disp=[src], src=src+1                 ;len, disp
     if disp>=80h then disp=(disp-80h)*100h+[src], src=src+1     ;longer disp
     for i=1 to (len+3), [dst]=[dst-(disp+1)], dst=dst+1, next i
   endif
   goto @@decompress_lop
  @@decompress_done:
   ret
```

#### Notes
Depending on the source, only the compressed or decompressed size may be known:<br/>
```
  Source                    Compressed Size           Decompressed Size
  Compressed GAMEFONT.DAT   In ISO Filesystem         Unknown (n/a)
  Compressed GT-ARC         In ISO Filesystem         Unknown (n/a)
  Files in GT-ARC           In GT-ARC                 In GT-ARC
  Files with GT-ZIP header  Unknown (due to padding)  In GT-ZIP
  DC values in IKI videos   Unknown (due to padding)  From Width*Height
```
Gran Turismo 1 has ID "@(#)GT-ZIP" (and "@(#)G.T-ZIPB" whatever that is) stored
in Main RAM (though unknown if/which/any files do have those IDs).<br/>
Gran Turismo 2 has ID "@(#)GT-ZIP" in "GT2\GT2.VOL\arcade\arc\_other.tim\\*",
apart from that, it does mainly use GZIP compressed files.<br/>



##   CDROM File Compression GT20 and PreGT20
#### GT20 Compressed Files
Used by Rollcage (MagDemo19: ROLLCAGE\SPEED.IMG\\*)<br/>
Used by Rollcage Stage II (MagDemo31: ROLLCAGE\SPEED.IDX\\*)<br/>
Used by Sydney 2000 (MagDemo37: OLY2000\DEMO.IDX\\* and OLY2000\GTO\\*.GTO)<br/>
Reportedly also Chill (PS1) (\*.GTO)<br/>
Reportedly also Ducati World: Racing Challenge<br/>
Reportedly also Martian Gothic: Unification (PS1) (\*.GT20)<br/>
```
  000h 4     ID ("GT20"=Compressed) (or reportedly "NOGT"=Uncompressed)
  004h 4     Size of decompressed data in bytes
  008h 4     Overlap for in-situ decompression (usually 3, or sometimes 7)
  00Ch 4     Size of Leading Zeropadding in bytes (0..7FFh)
  010h ..    Leading Zeropadding (0..7FFh bytes)
  ...  ..    Compressed Data
```
The Leading Zeropadding can be used to arrange the data to end on a sector
boundary (useful when loading the file in units of whole sectors, and wanting
to load it to the end of the decompression buffer).<br/>
```
 DecompressGT20:
  src=src+word[src+0Ch]+10h      ;skip header and any leading zeropadding
  collected=00000001h  ;end-bit
 @@lop:
  if GetBit=0
    [dst]=[src], dst=dst+1, src=src+1               ;uncompressed byte
  else
    if GetBit=0
      disp=byte[src]-100h, src=src+1                ;disp=(-100h..-1)
      len=(GetBit*2)+(GetBit*1)+2                   ;len=(2..5)
    else
      tmp=halfword[src], src=src+2
      disp=(tmp/8)-2000h                            ;disp=(-2000h..-1)
      len=(tmp AND 7)+2                             ;len=(2..9)
      if len=2
        tmp=byte[src], src=src+1
        if (tmp AND 80h) then disp=disp-2000h       ;disp=(-4000h..-1)
        len=(len AND 7Fh)+2                         ;len=(2..81h)
        if len=3 then goto decompression_done
        if len=2 then len=halfword[src], src=src+2  ;len=(0..FFFFh)
    for i=1 to len, [dst]=[dst+disp], dst=dst+1, next i
  goto @@lop
 ;---
 GetBit:
  collected=collected SHR 1
  if zero then collected=(word[src] SHR 1)+80000000h, src=src+4
  return carry (from shift right)
```
Note: Uncompressed files can reportedly contain "NOGT" in the header, however,
Rollcage does have compressed files (with GT20 header), and raw uncompressed
files (without any NOGT header).<br/>
[https://zenhax.com/viewtopic.php?t=13175] (specs)<br/>
See also: [http://wiki.xentax.com/index.php/GT20\_Archive] (blurp)<br/>

#### Pre-GT20 Compressed Files
Used by Bloody Roar 1 (MagDemo06: BL\\*.DAT\\*)<br/>
Used by Bloody Roar 2 (MagDemo22: ASC,CMN,EFT,LON,SND,ST5,STU\\*.DAT\\*)<br/>
```
  000h 4    Compression Method (0=None, 2=Compressed, Other=Invalid)
  004h 4    Compressed Size (SIZ) (same as decompressed when method=0)
  008h 4    Decompressed Size
  00Ch SIZ  Compressed Data
  ...  ..   Garbagepadding to 4-byte boundary (in 4-byte aligned DAT files)
```
This is apparently on older version of what was later called GT20. The PreGT20
decompression works as so:<br/>
```
 DecompressPreGT20:
  src=src+0Ch                    ;skip header
  collected=80h  ;end-bit
 @@lop:
  if GetBit=1
    [dst]=[src], dst=dst+1, src=src+1               ;uncompressed byte
  else
    if GetBit=0
      len=(GetBit*2)+(GetBit*1)+2                   ;len=(2..5)
      disp=byte[src]-100h, src=src+1                ;disp=(-100h..-1)
    else
      tmp=bigendian_halfword[src], src=src+2
      disp=(tmp/8)-2000h                            ;disp=(-2000h..-1)
      len=(tmp AND 7)+2                             ;len=(2..9)
      if len=2
        len=byte[src]+1, src=src+1                  ;len=(1..100h)
        if len=1 then goto decompression_done
    for i=1 to len, [dst]=[dst+disp], dst=dst+1, next i
  goto @@lop
 ;---
 GetBit:
  collected=collected SHL 1    ;8bit shift
  if zero then collected=(byte[src] SHL 1)+01h, src=src+1
  return carry (from 8bit shift left)
```
Note: Uncompressed files with Method=0 exist in Bloody Roar 2 (CMN\SEL01.DAT).<br/>
Bloody Roar 1 (MagDemo06) has decompressor at 8016DD64h (method 0 and 2).<br/>
Bloody Roar 2 (MagDemo22) has decompressor at 8015C8C0h (method 0 and 2).<br/>



##   CDROM File Compression HornedLZ
Used by Project Horned Owl (\*.BIN\\*) (and within self-decompressing EXE)<br/>

#### HornedLZ Detection
The easiest way to detect HornedLZ files is to check first 4 bytes:<br/>
```
  B3 10 00 4F ..    Compressed TIM with TIM Type=00h (4bpp without CLUT)
  DB 10 00 3F ..    Compressed TIM with TIM Type=08h,09h,etc.
```
Alternately, one could check the Chunktype (in the parent archive):<br/>
```
  Type=05h can be uncompressed .TXT or HornedLZ-compressed .TIM
    (check if 2nd data byte is ASCII or 10h)
  Type=0Fh is a DOT1 archive with HornedLZ-compressed .TIMs
    (parse the DOT1 archive and treat its contents as compressed .TIMs)
  Type=10h contains Deflated TIMs
    (a completely different compression method)
```

#### DecompressHornedLZ:
```
  collected=01h  ;end-bit
 @@lop:
  if GetBit=1
    [dst]=[src], dst=dst+1, src=src+1               ;uncompressed byte
  else
    if GetBit=1
      tmp=[src], src=src+1
      len=tmp/40h+2, disp=tmp or (-40h)       ;len=(2..05h), disp=(-40h..-1)
    else
      tmp=[src]*100h+[src+1], src=src+2
      len=tmp/1000h+2, disp=tmp or (-1000h)   ;len=(2..11h), disp=(-1000h..-1)
      if len=2 then
        len=[src]+2, src=src+1                ;len=(2..101h)
        if len=2 then goto decompression_done
    for i=1 to len, [dst]=[dst+disp], dst=dst+1, next i
  goto @@lop
 ;---
 GetBit:
  collected=collected SHR 1
  if zero then collected=([src] SHR 1)+80h, src=src+1
  return carry (from shift right)
```
Note: The end code has all bits zero, except, disp is don't care (it's usually
FFFh).<br/>



##   CDROM File Compression LZS (Gundam Battle Assault 2)
#### Gundam Battle Assault 2 (DATA\\*.PAC\\*, with ID="lzs")
```
  000h 4     ID ("lzs",00h)
  004h 4     Zerofilled
  008h 4     Fixed (must be 1) (method/version?)
  00Ch 14h   Zerofilled
  020h 2     Fixed (must be 3) (method/version?)
  022h 2     Offset to Compressed Data minus 20h (usually 38h-20h)
  024h 4     Decompressed Size
  028h 2     Flagsize (must be 08h, 10h, or 20h) (usually 20h=32bit)
  02Ah 2     Lensize  (must be 02h..07h)         (usually 05h=5bit)
  02Ch 4     Compressed Size (total filesize, including "lzs" header)
  030h 8     Name? (always "000000",00h,00h)
  038h ..    Compressed data (usually at offset 38h)
```
decompress\_gundam\_lzs:<br/>
```
   dst_end = dst+littleendian32bit[src+24h]
   flg_bits = littleendian16bit[src+28h]   ;8,16,32
   len_bits = littleendian16bit[src+2Ah]   ;2..7
   len_mask = (1 shl len_bits)-1           ;03h..7Fh
   src=src+littleendian16bit[src+22h]+20h
   collected_bits=0
  @@collect_more:
   for i=0 to flg_bits/8-1    ;read 8bit/16bit/32bit little-endian
     collected_bits=collected_bits+([src] SHL (i*8)), src=src+1
   num_collected=flg_bits
  @@decompress_lop:
   if dst=dst_end then goto @@decompress_done
   if num_collected=0 then goto @@collect_more
   num_collected=num_collected-1
   flagbits=flagbits SHR 1
   if carry=1 then
     [dst]=[src], dst=dst+1, src=src+1
   else
     temp=bigendian16bit[src], src=src+2
     len=(temp AND len_mask)+3
     disp=(temp SHR len_bits), if disp=0 then goto @@decompress_error
     for i=1 to len, [dst]=[dst-disp], dst=dst+1, next i
   endif
   goto @@decompress_lop
  @@decompress_done:
   ret
```



##   CDROM File Compression BZZ
Used in .BZZ archives. Note that there are three slightly different .BZZ
archive formats (they are all using the same BZZ compression, only the BZZ
archive headers are  different).<br/>
```
  Jersey Devil .BZZ (MagDemo10: JD\*.BZZ)
  Bugs Bunny: Lost in Time (MagDemo25: BBLIT\*.BZZ)
  The Grinch (MagDemo40: GRINCH\*.BZZ)
```
Neither the file header nor the archive directory entries do contain any
information about the decompressed size. Best workaround might be to decompress
the file twice (without storing the output in 1st pass, to determine the size
of the decompression buffer for 2nd pass).<br/>

#### BZZ Decompression
The compression is fairly standard LZSS, except that it supports non-linear
length values, and it does support uncommon Len/Disp pairs like
7bitLen/9bitDisp (though usually, it does use standard 4bitLen/12bitDisp).<br/>
```
  decompress_bzz:
   method=byte[src], src=src+1       ;method (00h..1Fh) ;usually/always 0Bh)
   shifter  = ((method/8) and 3)     ;00h..03h                ;usually 1
   len_bits = ((method and 7) xor 7) ;07h..00h                ;usually 4
   len_mask = (1 shl len_bits)-1     ;7Fh..00h                ;usually 0Fh
   threshold=len_mask/2, if threshold>07h then threshold=13h  ;usually 07h
   for i=0 to len_mask
     if i>threshold then len_table[i] = ((i-threshold) shl shifter)+threshold+3
     else len_table[i] = i+3 ;method=18h max=(7Fh-13h)*8+13h+3=376h=886 decimal
   next i                    ;method=0Hh max=(0Fh-07h)*2+07h+3=1Ah=26 decimal
   num_flags=bigendian24bit[src]+1, src=src+3   ;NUM24+1
  @@collect_more:
   if src>=src_end then goto @@decompress_error
   flagbits=[src]+100h, src=src+1    ;8bit flags
  @@decompress_lop:
   flagbits=flagbits SHR 1
   if zero then goto @@collect_more
   if carry=1 then
     if src>=src_end then goto @@decompress_error
     [dst]=[src], dst=dst+1, src=src+1
   else
     if src+1>=src_end then goto @@decompress_error
     temp=bigendian16bit[src], src=src+2
     len=len_table[temp AND len_mask]
     disp=temp SHR len_bits, if disp=0 then goto @@decompress_error
     for i=1 to len, [dst]=[dst-disp], dst=dst+1, next i
   endif
   num_flags=num_flags-1, if num_flags>0 then goto @@decompress_lop
  @@decompress_error:
   ret
```
Bug: Files can randomly contain NUM24 or NUM24+1 codes (that seems to be due to
a compressor bug or different compressor versions; the two variants are
unfortunately randomly mixed even within the same game).<br/>
And, compressed files are padded to 4-byte boundary (making it impossible to
distinguish between "NUM24+1" and "NUM24+padding").<br/>
```
  Case 1) source has NUM24+1 codes
           --> decode all NUM24+1 codes (otherwise output will be too small)
  Case 2) source has NUM24 codes (and enough padding for another code)
           --> decode all NUM24+1 codes (for compatibility with case 1)
           --> output will have some constant garbage byte(s) appended
           --> exception: omit last code if it contains invalid disp=0
  Case 3) source has NUM24 codes (and not enough padding for another code)
           --> decode only NUM24 codes (abort if NUM24+1 exceeds src_end)
           --> output should (probably) have correct size
           --> never exceed src_end which would be highly unstable
```



##   CDROM File Compression RESOURCE (Star Wars Rebel Assault 2)
#### Star Wars Rebel Assault 2 (RESOURCE.\*\\*)
#### BallBlazer Champions (\*.DAT)
```
 decompression function:
  base=src, method=[src], dst_end=dst+BigEndian24bit[src+1], src=src+4
 @@decompress_lop:
  if dst>=dst_end then goto @@decompress_done
  if [src] AND 80h then
    if method=01h then
      len=([src]-80h)/8+3, disp=(BigEndian16bit[src] AND 7FFh)+1, src=src+2
    else  ;method=02h
      len=([src]-80h)+4, disp=(BigEndian16bit[src+1])+1, src=src+3
    for i=1 to len, [dst]=[dst-disp], dst=dst+1
  else    ;uncompressed
    len=[src]+1, src=src+1
    for i=1 to len, [dst]=[src], src=src+1, dst=dst+1
  goto @@decompress_lop
 @@decompress_done:
  src=(src+3) AND NOT 3
  if LittleEndian32bit[src]<>crc(base, src-base) then error
  ret
```
Note: Compression is (normally) used only in Top-level RESOURCE.\* and \*.DAT
archives (not in Nested archives). The Top-level archives do also contain some
uncompressed files (which contain data that is compressed on its own: SPU-ADPCM
audio, or encrypted BS bitmaps).<br/>

#### Special case for BallBlazer Champions
Normally only Top-level archives contain compression, however, there are also
some Nested archives with compression in BallBlazer Champions:<br/>
```
  STD_BBX.DAT\s*t\tp_a\*    ;\double compression, Top-level is ALSO compressed
  BBX_INTR.DAT\data1\pics\* ;/
  BBX_INTR.DAT\Stad\pics\*  ;\
  BBX_INTR.DAT\Stad\wire\*  ; Nested archives with compression
  BBX_INTR.DAT\Subtitl\*    ;
  BBX_INTR.DAT\Subtitl\sub\*;/
```
The Nested archives don't have any compression flag or decompressed size
entries (so there's no good way for detecting compression in nested files).<br/>



##   CDROM File Compression TIM-RLE4/RLE8
Ape Escape (Sony 1999) (MagDemo22: KIDZ\\*) has several compressed and
uncompressed TIMs in headerless archives, the archives can contain:<br/>
```
  Compressed 4bpp RLE4-TIM with uncompressed CLUT ;\only 4bpp can be compressed
  Compressed 4bpp RLE8-TIM with uncompressed CLUT ;/
  Uncompressed 4bpp TIM with uncompressed CLUT    ;\only this type/combinations
  Uncompressed 8bpp TIM with uncompressed CLUT    ; are allowed if uncompressed
  Uncompressed 16pp TIM without CLUT              ;/
  End code 00000000h (plus more zeropadding)      ;-end of headerless archive
```
The compression method is indicated by changing a reserved halfword in the TIM
header:<br/>
```
  hdr[02h]=Method (0000h=Uncompressed, 0001h=RLE4, 0002h=RLE8)
```
The rest of the bytes in TIM header and in CLUT section are same as for normal
TIMs. The Bitmap section is as follows:<br/>
Decompressed size must be computed as Width\*Height\*2. The Section Size entry
contains Section header size, plus compressed size, plus padding to 4-byte
boundary.<br/>
Method=0001h (RLE4):<br/>
```
 @@decompress_lop:
  color=[src]/10h, len=([src] AND 0Fh)+1, src=src+1
  for i=1 to len, putpixel(color), next i               ;len=1..10h
  if numpixels<Width*Height*4 then goto @@decompress_lop
```
Method=0002h (RLE8):<br/>
```
 @@decompress_lop:
  color1=[src]/10h, color2=[src] AND 0Fh, src=src+1
  if color1=color2
    len=[src]+2, src=src+1
    for i=1 to len, putpixel(color1), next i            ;len=2..101h
  else
    putpixel(color1), if numpixels<Width*Height*4 then putpixel(color2)
  for i=1 to len, putpixel(color)       ;len=1..10h
  if numpixels<Width*Height*4 then goto @@decompress_lop
```
The decompression functions in Ape Escape (MagDemo22: KIDZ\\*) are found at:<br/>
```
  80078760h ape_escape_load_tim_archive
  8007894Ch ape_escape_decompress_with_4bit_lengths
  800789FCh ape_escape_decompress_with_8bit_lengths
```
Examples for compressed TIMs are found at:<br/>
```
  RLE8: Ape Escape, MagDemo22: KIDZ\KKIIDDZZ.HED\DAT\file004h\1stTIM
  RLE4: Ape Escape, MagDemo22: KIDZ\KKIIDDZZ.HED\DAT\file135h\1stTIM
  RLE8: Ape Escape, MagDemo22: KIDZ\KKIIDDZZ.HED\DAT\file139h\1stTIM
```
Being made by Sony, this might be an official (but late) TIM format extension,
unknown if there are any other games using that compression.<br/>



##   CDROM File Compression RLE\_16
#### Apocalypse (MagDemo16: APOC\CD.HED\\*.RLE)
#### Spider-Man (MagDemo31,40: SPIDEY\CD.HED\\*.RLE)
#### Spider-Man 2 (MagDemo50: HARNESS\CD.HED\\*.RLE)
```
  000h 8     ID "_RLE_16_"
  008h 4     Decompressed Size (usually 3C008h) (33408h=Apocalypse warning.rle)
  00Ch ..    RLE Compressed Data (usually a .BMR bitmap)
```
This is using simple RLE compression with 16bit len/data units (suitable for
16bpp VRAM data). The compression ratio ranges from not so bad to very bad.<br/>

#### Decompression
```
  src=src+0Ch                                       ;skip ID and size
 @@decompress_lop:
  len=halfword[src], src=src+2
  if len=0000h then goto @@decompress_done          ;end-code
  if (len AND 8000h)=0 then
    for i=1 to len, halfword[dst]=halfword[src], dst=dst+2, src=src+2, next i
  else
    fillvalue=halfword[src], src=src+2
    for i=1 to len-8000h, halfword[dst]=fillvalue, dst=dst+2, next i
  goto @@decompress_lop
 @@decompress_done:
  ret
```

#### Other RLE16 variants
A similar RLE16 variant is used in Croc 1, and another variant in Croc 2.<br/>
[CDROM File Archive Croc 1 (DIR, WAD, etc.)](cdromfileformats.md#cdrom-file-archive-croc-1-dir-wad-etc)<br/>
[CDROM File Archive Croc 2 (DIR, WAD, etc.)](cdromfileformats.md#cdrom-file-archive-croc-2-dir-wad-etc)<br/>



##   CDROM File Compression PIM/PRS (Legend of Mana)
#### Legend of Mana (.PIM/.PRS)
```
  000h 1   Unknown (always 01h) (maybe File ID or Compression method)
  001h ..  Compressed data  ;for TIM: usually 00,10, F0,00, 00,0x, F0,00, ...
```
Compression codes are:<br/>
```
  nn,data[nn+1]  ;nn=00..EF len=nn+1   [dst]=data[1]             ;-uncompressed
  F0,xn                     len=n+3    [dst]=0x         ;1x4bit  ;\
  F1,nn,xx                  len=nn+4   [dst]=xx         ;1x8bit  ;
  F2,nn,yx                  len=nn+2   [dst]=0x,0y      ;2x4bit  ; RLE fill
  F3,nn,xx,yy               len=nn+2   [dst]=xx,yy      ;2x8bit  ;
  F4,nn,xx,yy,zz            len=nn+2   [dst]=xx,yy,zz   ;3x8bit  ;/
  F5,nn,xx,data[nn+4]       len=nn+4   [dst]=xx,data[1]          ;\interleaved
  F6,nn,xx,yy,data[nn+3]    len=nn+3   [dst]=xx,yy,data[1]       ; fill combo
  F7,nn,xx,yy,zz,data[nn+2] len=nn+2   [dst]=xx,yy,zz,data[1]    ;/
  F8,nn,xx                  len=nn+4   [dst]=xx    ;xx=xx+1      ;\
  F9,nn,xx                  len=nn+4   [dst]=xx    ;xx=xx-1      ; fill with
  FA,nn,xx,ss               len=nn+5   [dst]=xx    ;xx=xx+ss     ; signed step
  FB,nn,xx,yy,ss ;ss=signed len=nn+3   [dst]=xx,yy ;yyxx=yyxx+ss ;/
  FC,xx,ny                  len=n+4    [dst]=[dst-yxx-1]         ;\
  FD,xx,nn                  len=nn+14h [dst]=[dst-xx-1]          ; LZ compress
  FE,xn                     len=n+3    [dst]=[dst-x*8-8]         ;/
  FF                        len=0      end                       ;-end code
```
The compression is used for several files in Legend of Mana:<br/>
```
  BIN\*.BIN       ---> packed misc binary
  MAP\*\FDATA.PRS ---> packed resource, whatever
  MAP\*\MAP*.PRS  ---> packed MPD resource, "SKmapDat"
  WM\WMTIM\*.PIM  ---> packed TIM image, 384x384x4bpp, bad compression ratio
  WM\WMAP\*.PAT   ---> packed loaddata
  WM\WMAP\*.PIM   ---> packed TIM image, 320x256x16bit, with UNCOMPRESSED dupe
```



##   CDROM File Compression BPE (Byte Pair Encoding)
Byte Pair Encoding (BPE) does replace the most common byte-pairs with bytes
that don't occur in the data. That does work best if there are unused bytes
(eg. ASCII text, or 8bpp bitmaps with less than 256 colors).<br/>

#### Bust A Groove (MagDemo18: BUSTGR\_A\\*.BPE)
#### Bust-A-Groove 2 (MagDemo37: BUSTAGR2\BUST2.BIN\\*)
```
  000h 4     ID "BPE_"
  004h 4     Total Filesize of compressed file including header (big-endian)
  ...  ..    Compression block(s)
 Each compression block contains:
  000h ..    Dictionary info
  ...  2     Size of compressed data (big-endian)
  ...  ..    Compressed data
```
The decompression function in Bust A Groove (MagDemo18) is at 80023860h, the
heap is in 1Kbyte Scratchpad RAM at 1F800208h, so heap size should be max 1F8h
bytes (assuming that the remaining Scratchpad isn't used for something else).
The fileheader lacks info about the decompressed size.<br/>

#### Legend of Dragoon (MagDemo34: LOD\OVL\\*.OV\_ and LOD\SECT\\*.BIN\\*)
```
  000h 4     Decompressed size (little-endian)
  004h 4     ID "BPE",1Ah
  008h ..    Compression block(s)
  ...  ..    End code (00000000h) (aka last block with Blocksize=0)
 Each compression block contains:
  000h 4     Size of decompressed block (little-endian) (or 0=End code)
  004h ..    Dictionary info
  ...  ..    Compressed data
  ...  ..    Padding to 4-byte boundary
```
Max nesting appears to be 2Ch, the decompression function allocates a 30h-byte
heap on stack, and fetches source data in 32bit units (occupying 4 heap bytes),
the decompressor does then remove 1 byte from heap, and adds 2 bytes in case of
nested codes.<br/>

#### BPE Decompression for Bust-A-Groove and Legend of Dragoon
```
  if [src+0]="BPE_" then type=GROOVE                                    ;\
  if [src+4]="BPE",1Ah then type=DRAGOON                                ;
  if type=GROOVE then src_end = src+BigEndian32bit[src+4]               ; hdr
  if type=DRAGOON then dst_end = dst+LittleEndian32bit[src+0]           ;
  src=src+8                                                             ;/
 @@block_lop:
  if type=DRAGOON then                                                  ;\blk
    dst_blk_end = dst+LittleEndian32bit[src]+4, src=src+4               ; len
    if dst=dst_blk_end then goto @@decompress_done                      ;/
  for i=00h to FFh, dict1[i]=i, next i                                  ;\
  i=00h                                                                 ;
 @@dict_lop:                                                            ; dict
  num=[src], src=src+1                                                  ;
  if num>7Fh then i=i+(num-7Fh), num=0, if i=100h then goto @@dict_done ;
  for j=0 to num                                                        ;
    a=[src], src=src+1                                                  ;
    if a<>i then b=[src], src=src+1, dict1[i]=a, dict2[i]=a             ;
    i=i+1                                                               ;
  if i<100h then goto @@dict_lop                                        ;
 @@dict_done:                                                           ;/
  if type=GROOVE then                                                   ;\blk
    src_blk_end = src+BigEndian16bit[src]+2, src=src+2                  ;/len
  i=0                                                                   ;\
 @@data_lop:                                                            ;
  if i=0 then                                                ;\         ; data
    if type=GROOVE and src=src_blk_end then goto @@data_done ; get data ;
    if type=DRAGOON and dst=dst_blk_end then goto @@data_done; from src ;
    x=[src], src=src+1                                       ; or heap  ;
  else                                                       ;          ;
    i=i-1, x=heap[i]                                         ;/         ;
  a=dict1[x]                                    ;-xlat                  ;
  if a=x then                                   ;\                      ;
    [dst]=x, dst=dst+1                          ; output data to        ;
  else                                          ; dst or heap           ;
    b=dict2[x], heap[i]=b, heap[i+1]=a, i=i+2   ;/                      ;
  goto @@data_lop                                                       ;
 @@data_done:                                                           ;/
  if type=GROOVE and src<src_end then goto @@block_lop                  ;\next
  if type=DRAGOON then src=(src+3) AND not 3, goto @@block_lop          ;/blk
 @@decompress_done:
  if type=DRAGOON and dst<>dst_end then error
  ret
```

#### Electronic Arts
Electronic Arts games support several compression methods, including a BPE
variant. That BPE variant is a bit unusual: It does have only one compression
block (with a single dictionary for the whole file), and uses escape codes for
rarely used bytes.<br/>
[CDROM File Compression EA Methods](cdromfileformats.md#cdrom-file-compression-ea-methods)<br/>



##   CDROM File Compression RNC (Rob Northen Compression)
#### Rob Northen compression
Rob Northen compression (RNC) is a LZ/Huffman compression format used by
various games for PC, Amiga, PSX, Mega Drive, Game Boy, SNES and Atari Lynx.<br/>
Most RNC compressed files come in a standard 12h-byte header:<br/>
```
  000h 3   Signature ("RNC") (short for Rob Northen Computing compression)
  003h 1   Compression Method (01h or 02h)
  004h 4   Size of Uncompressed Data                             ;big-endian
  008h 4   Size of Compressed Data (SIZ)                         ;big-endian
  00Ch 2   CRC16 on Uncompressed Data (with initial value 0000h) ;big-endian
  00Eh 2   CRC16 on Compressed Data   (with initial value 0000h) ;big-endian
  010h 1   Leeway (difference between compressed and uncompressed data in
                   largest pack chunk, if larger than decompressed data)
  011h 1   Number of pack chunks
  012h SIZ Compressed Data
  ... (..) Zeropadding to 800h-byte boundary-4 ;\as so in PSX Heart of Darkness
  ... (4)  Unknown                             ;/
```
The compressed data consists of interleaved bit- and byte-streams, the first 2
bits of the bit stream are ignored.<br/>

#### RNC Method 1 - with custom Huffman trees
The bit-stream is read in 16bit units (the 1st bit being in bit0 of 1st byte).<br/>
```
  Each pack chunk contains the following:
  * 3 Huffman trees (one for literal data sizes, one for distance values,
    and one for length values) in the bit stream. These consist of:
      o A 5 bit value for the amount of leaf nodes in the tree
      o 4 bit values for each node representing their bit depth.
  * One 16 bit value in the bitstream for the amount of subchunks in the
    pack chunk.
  * The subchunk data, which contains for each subchunk:
      o A Huffman code value from the first tree in the bit stream for the
        amount of literals in the byte stream.
      o Literals from the byte stream.
      o A Huffman code from the bit stream that represents the distance - 1
        of a distance/length pair.
      o A Huffman code from the bit stream that represents the length - 2
        of a distance/length pair.
```
Unknown how that works exactly (see source code for details), unknown if method
1 was used on PSX.<br/>

#### RNC Method 2 - with hardcoded Huffman trees
The bit-stream is read in 8bit units (the 1st bit being in bit7).<br/>
```
  0     + Byte(DATA[1])              Copy 1 Byte from Source
  1000  + Dist + Byte(X)             Copy 4 Bytes from Dest-(Dist+X+1)
  10010 + Dist + Byte(X)             Copy 6 Bytes from Dest-(Dist+X+1)
  10011 + Dist + Byte(X)             Copy 7 Bytes from Dest-(Dist+X+1)
  1010  + Dist + Byte(X)             Copy 5 Bytes from Dest-(Dist+X+1)
  10110 + Dist + Byte(X)             Copy 8 Bytes from Dest-(Dist+X+1)
  10111 + nnnn + Byte(DATA[12..72])  Copy nnnn*4+12 Bytes from Source
  110   + Byte(X)                    Copy 2 Bytes from Dest-(X+1)
  1110  + Dist + Byte(X)             Copy 3 bytes from Dest-(Dist+X+1)
  1111  + Byte(0) + 0 + zeropadding  End of last pack chunk
  1111  + Byte(0) + 1                End of non-last pack chunk
  1111  + Byte(L) + Dist + Byte(X)   Copy L+8 Bytes from Dest-(Dist+X+1) ;L>00h
```
Dist values:<br/>
```
  0      = 0000h            1000   = 0200h
  110    = 0100h            1001   = 0300h
  111000 = 0C00h            101000 = 0800h
  111001 = 0D00h            101001 = 0900h
  11101  = 0600h            10101  = 0400h
  111100 = 0E00h            101100 = 0A00h
  111101 = 0F00h            101101 = 0B00h
  11111  = 0700h            10111  = 0500h
```
The purpose of the pack chunks isn't quite clear, it might be related to memory
restrictions on old CPUs. In PSX Heart of Darkness they are chosen so that the
decompressed data is max 3000h bytes per chunk. Unknown if the next chunk may
copy data from previous chunk.<br/>

#### Links
```
  http://aminet.net/package/util/pack/RNC_ProPack - official tool & source code
  https://segaretro.org/Rob_Northen_compression - description (contains bugs)
```

RNC is used in a number of games by UK developers (notably Bullfrog and
Traveller's Tales), including Sonic 3D: Flickies' Island, Blam! Machinehead,
Dungeon Keeper 2, Magic Carpet, Syndicate and Syndicate Wars.<br/>

#### RNC in PSX Games
```
  Method 2: Demolition Racer (MagDemo27: DR\DD.DAT\*.RNC)
  Method 2: Heart of Darkness (IMAGES\US.TIM)
  Method 2: Jonah Lomu Rugby (LOMUDEMO\GFX\*.PAK)
  Method 2: NBA Jam: Tournament Edition (*.RNC, headerless .BIN/.GFX archives)
  Method 2: Test Drive 5 (MagDemo13: TD5.DAT\*.RNC)
  Method 2: Test Drive Off-Road 3 (MagDemo27: TDOR3\TDOR3.DAT\*.rnc)
```

#### RNC in Mega Drive games
```
  3 Ninjas Kick Back
  Addams Family
  Addams Family Values
  The Adventures of Mighty Max
  Ast�rix and the Great Rescue
  Ast�rix and the Power of the Gods
  The Incredible Hulk
  The Itchy & Scratchy Game (unreleased)
  Marsupilami
  Mortal Kombat
  Mr. Nutz
  Outlander
  The Pagemaster
  RoboCop 3
  Spirou
  Spot Goes to Hollywood
  Stargate
  Street Racer
  Tinhead
  Tintin in Tibet
  World Championship Soccer II
```



##   CDROM File Compression Darkworks
Used by Alone in the Dark The New Nightmare (FAT.BIN\LEVELS\\*\chunks)<br/>

#### Decompression
The decompressor is designed to hook the sector loading function: It does
decompress incoming sectors during loading, and forwards the decompressed data
to the original sector loading function. The decompressed data is temporarily
stored in two small Dict buffers (which do also serve as compression
dictionary).<br/>
```
 decompress:
  dictsize=1000h, dict0=alloc(dictsize), dict1=alloc(dictsize)
  src=load_next_800h_byte_sector  ;load first sector
  dst=dict0                       ;temp dest in current dict
  dst_base=dst                    ;memorize start of newly decompressed data
 @@decompress_lop:
  if [src]=00h then                                             ;\
    esc=[src+1], src=src+1                                      ;
    forward_to_actual_dest(source=dst_base, len=dst-dst_base)   ; escape
    if esc=0 or esc>4 then esc=2 (or warn_invalid_escape_code)  ;
    if esc=1 then goto @@decompress_done                        ;
    if esc=2 or esc=4 then src=load_next_800h_byte_sector       ;
    if esc=3 or esc=4 then swap(dict0,dict1), dst=dict0         ;
    dst_base=dst                                                ;/
  elseif ([src] AND 03h)=0 then                                 ;\
    len=[src]/4+2, dat=[src+1], src=src+2                       ; fill 8bit
    for i=1 to len, [dst]=dat, dst=dst+1                        ;/
  elseif ([src] AND 03h)=1 then                                 ;\
    len=[src]/4+([src+2] AND 40h)+4                             ;
    ptr=[src+1]+([src+2] AND 3Fh)*100h                          ; LZ compressed
    if ptr+len>dictsize then error (exceeds allocated dictsize) ;
    if ([src+2] AND 80h) then ptr=ptr=dict1 else ptr=ptr=dict0  ;
    src=src+3                                                   ;
    for i=1 to len, [dst]=[ptr], ptr=ptr+1, dst=dst+1           ;/
  elseif ([src] AND 03h)=2 then                                 ;\
    len=[src]/4+3, dat0=[src+1], dat1=[src+2], src=src+3        ; fill 16bit
    for i=1 to len, [dst]=dat0, [dst+1]=dat1, dst=dst+2         ;/
  elseif ([src] AND 03h)=3 then                                 ;\
    len=[src]/4+1, src=src+1                                    ; uncompressed
    for i=1 to len, [dst]=[src], src=src+1, dst=dst+1           ;/
  goto @@decompress_lop
 @@decompress_done:
  dealloc(dict0), dealloc(dict1)
  ret
```
There are one or more escape codes per sector (one to indicate the of the
sector, plus further escape codes to swap the Dict buffers whenever the current
Dict is full).<br/>
The original decompressor is doing the forwarding in 800h-byte units, so Dict
swapping may be only done when dict0 contains a multiple of 800h bytes (aka
dictsize bytes).<br/>
For whatever reason, there are only 4Kbyte per Dict allocated (although the
14bit LZ indices could have addressed up to 16Kbyte per Dict).<br/>



##   CDROM File Compression Blues
#### Blue's Clues: Blue's Big Musical (VRAM and FRAM chunks in \*.TXD)
Decompression function:<br/>
```
  if LittleEndian32bit[src+08h]<>1 then error  ;compression flag
  dst_end=dst+LittleEndian32bit[src+14h], src=src+18h, num_collected=0
 @@decompress_lop:
  if GetBit=1 then
    [dst]=[src], src=src+1, dst=dst+1           ;code 1 uncompressed byte
  elseif GetBit=1 then
    len=[src], src=src+1                        ;code 01 fill or end code
    if len=00h then goto @@decompress_done
    len=len+1, fillvalue=[dst-1]
    for i=1 to len, [dst]=fillvalue, dst=dst+1
  else
    len=GetBit*2+GetBit
    if len=0 then                               ;code 0000 long LZ range
      len=[src] AND 0Fh, disp=[src]/10h+[src+1]*10h-1000h, src=src+2
    else                                        ;code 00xx short LZ range
      disp=[src]-100h, src=src+1
    len=len+1
    for i=1 to len, [dst]=[dst+disp], dst=dst+1
  goto @@decompress_lop
 @@decompress_done:
  if dst<>dst_end then error
  ret
 ;---
 GetBit:
  if num_collected=0 then collected=[src], src=src+1, num_collected=8
  collected=collected*2
  return (collected/100h) AND 1
```



##   CDROM File Compression Z (Running Wild)
#### Running Wild (MagDemo15: RUNWILD\\*.BIN\\*.Z and \*.z)
```
  decompress_z:
   src=src+4            ;skip 32bit decompressed size entry
  @@reload_lop:
   load_table1          ;table for first 9bits
   load_table2          ;table for codes longer than 9bits
  @@decompress_lop:
   sym=get_symbol()
   if sym<100h then [dst]=sym, dst=dst+1, goto @@decompress_lop
   if sym=100h then goto @@escape
   len=sym-0FCh                         ;change 101h..140h to 05h..44h
   disp=((get_symbol()-101h)*40h)       ;change 101h..140h to 00h..3Fh*40h
   disp=((get_symbol()-101h) or disp)+1 ;change 101h..140h to 00h..3Fh+above+1
   copy len bytes from dst-disp to dst
   goto @@decompress_lop
  @@escape:
   if GetBits(1)=0 then goto @@reload_lop
   ret
  ;-----
  load_table1:
   t=0
  @@load_lop:
   x=GetBits(10h)
   if x and 8000h then num=1 else num=(1 shl (9-(x/400h)))
   for i=1 to num, table1[t]=x, t=t+1, next i
   if t<200h then goto @@load_lop
   ret
  ;-----
  load_table2:
   num=GetBits(9)*2      ;can be 0=none, max=3FEh
   if num>0 then for i=0 to num-1, table2[i]=GetBits(9), next i
   ret
  ;-----
  get_symbol:
   ;returns a value in range 0..140h:
   ;  00h..FFh   = data 00h..FFh   (or unused for disp codes)
   ;  100h       = escape          (or unused for disp codes)
   ;  101h..140h = length 05h..44h (or 6bit fraction of 12bit disp)
   ;  141h..3FFh = would be possible for short codes, but shouldn't be used
   x=table1[PeekBits(9)]
   if (x and 8000h)=0 then SkipBits(x/400h), return (x and 3FFh)  ;-short code
   SkipBits(9)   ;skip first 9 bits, and process futher bit(s)..  ;\
   x=x-0C000h    ;change C000h..C1FFh and up to 000h..1FFh        ; long code
  @@lop:                                                          ; (with more
   x=table2[x*2+GetBits(1)]             ;branch node0/node1       ; than 9bit)
   if x>=141h then x=x-141h, goto @@lop                           ;
   return x                                                       ;/
```
The bitstream is fetched in little endian 16bit units (the first bit is in bit7
of second byte). PeekBits returns the next some bits without discarding them,
SkipBits does discard them, GetBits does combine PeekBits+SkipBits.<br/>
Note: The decompression function in Running Wild (MagDemo15) is at 80029D10h.<br/>



##   CDROM File Compression ZAL (Z-Axis)
#### Thrasher: Skate and Destroy (MagDemo27: SKATE\ASSETS\\*.ZAL) (Z-Axis)
#### Dave Mirra Freestyle BMX (MagDemo36: BMX\ASSETS\\*.ZAL) (Z-Axis)
#### Dave Mirra Freestyle BMX (MagDemo46: BMX\ASSETS\\*.ZAL) (Z-Axis)
ZAL compression is used in ZAL archives. The archive header contains compressed
and decompressed size for each file (and a compression flag indicating whether
the archive is compressed at all).<br/>

#### ZAL Decompression
```
  if src_len=0 then goto @@decompress_done      ;empty (without end code)
  lzlen=0, rawlen=0
  if [src]=10h..FFh then                                ;\special handling
    rawlen=[src]-11h, src=src+1                         ; for code=10h..FFh
    if rawlen<=0 then goto @@decompress_error           ;/at begin of source
 @@decompress_lop:
  memcopy(dst-disp,dst,lzlen)   ;copy compressed bytes
  memcopy(src,dst,rawlen)       ;copy uncompressed bytes
  code=[src], src=src+1
  if code=00h..0Fh then
    if rawlen=0   ;when OLD rawlen=0...
      lzlen=0, rawlen=code+3                            ;\
      if rawlen=3 then                                  ;
        while [src]=00h, rawlen=rawlen+FFh, src=src+1   ;
        rawlen=rawlen+[src]+0Fh, src=src+1              ;/
    else          ;when OLD rawlen>0, and depending on OLD lzlen...
      rawlen=code AND 03h
      disp=code/4+[src]*4, src=src+1
      if lzlen=0 then disp=disp+801h, lzlen=3, else then disp=disp+1h, lzlen=2
  if code=10h..1Fh then
    lzlen=(code AND 07h)+2
    if lzlen=2 then
      while [src]=00h, lzlen=lzlen+FFh, src=src+1
      lzlen=lzlen+[src]+07h, src=src+1
    rawlen=[src] AND 03h, disp=[src]/4+[src+1]*40h+(code/8 AND 1)*4000h+4000h
    src=src+2
    if disp=4000h AND code=11h then goto @@decompress_done    ;end code
    if disp=4000h AND code<>11h then goto @@decompress_error
  if code=20h..3Fh then
    lzlen=code-20h+2
    if lzlen=2 then
      while [src]=00h, lzlen=lzlen+FFh, src=src+1
      lzlen=lzlen+[src]+1Fh, src=src+1
    rawlen=[src] AND 03h, disp=[src]/4+[src+1]*40h+1, src=src+2
  if code=40h..FFh then
    rawlen=code AND 03h
    lzlen=(code/20h)+1
    disp=((code/4) AND 07h)+([src]*8)+1, src=src+1
  goto @@decompress_lop
 @@decompress_done:
  ret
```



##   CDROM File Compression EA Methods
#### Electronic Arts Compression Headers
The files start with a 16bit big-endian Method value, with following bits:<br/>
```
  0-7     ID (usually FBh) (or 31h for Method 4A31h with 16bit sizes)
  8       Extended Header (usually 0) (or 1 for headers with extra entries)
  9-14    Used to distinguish different methods
  15      Extended Size (usually 0 for 24bit sizes) (or 1 for 32bit sizes)
```
The most common Method values are:<br/>
```
  10FBh = LZSS Compression (RefPack)
  90FBh = LZSS Compression (RefPack, with 32bit size) (not on PSX)
  30FBh = Huffman Compression
  32FBh = Huffman Compression with filter
  34FBh = Huffman Compression with dual filter
  46FBh = BPE Byte-Pair Encoding
  4AFBh = RLE Run-Length Encoding
  4A31h = RLE Run-Length Encoding, with 16bit size
  C0FBh = File Archive (not a compression method)
```
Most or all PSX files have Bit8=0, but anyways, the decompressor does support
skipping extra header entries in files with Bit8=1 (with all methods except
RLE).<br/>
Most or all PSX files have Bit15=0, games for newer consoles can reportedly
have Method=90FBh (unknown if anything like B2FBh or CAFBh does also exist).<br/>
Most or all PSX files have Bit0-7=FBh (supposedly short for Frank Barchard),
the 16bit mode with Bit0-7=31h is supported for Method=4A31h only (the
decompressor would also accept invalid methods like 1031h or 3431h, but doesn't
actually support 16bit mode for those).<br/>

#### Compression Formats
[CDROM File Compression EA Methods (LZSS RefPack)](cdromfileformats.md#cdrom-file-compression-ea-methods-lzss-refpack)<br/>
[CDROM File Compression EA Methods (Huffman)](cdromfileformats.md#cdrom-file-compression-ea-methods-huffman)<br/>
[CDROM File Compression EA Methods (BPE)](cdromfileformats.md#cdrom-file-compression-ea-methods-bpe)<br/>
[CDROM File Compression EA Methods (RLE)](cdromfileformats.md#cdrom-file-compression-ea-methods-rle)<br/>

#### Usage in PSX games
The compression can be used to compress whole files:<br/>
```
  PGA Tour 96, 97, 98 (*.* and *.VIV\*) (with method 10FBh)
  Need for Speed 3 Hot Pursuit (*.Q* with method 10FBh, 30FBh, 32FBh)
```
Or to compress texture bitmaps inside of .PSH file chunks:<br/>
```
  FIFA - Road to World Cup 98 (*.PSH chunk C0h/C1h with method 10FBh)
  Sled Storm (MagDemo24: ART3\LOAD*.PSH chunk C0h/C1h with method 10FBh)
  WCW Mayhem (MagDemo28: WCWDEMO\*.BIG\*.PSH with chunk C0h/C1h with 10FBh)
```
The decompressor supports further methods (like 34FBh, 46FBh, 4AFBh), but there
aren't any files or chunks known to actually use those compression formats.<br/>

Note: Some compressed files are slightly larger than uncompressed files (eg.
filesizes for PGA Tour 96, 97, 98 COURSES\\*\\*.VIV\\*.mis are compressed=58h,
uncompressed=50h).<br/>

#### See also
[http://wiki.niotso.org/RefPack] - LZ method<br/>



##   CDROM File Compression EA Methods (LZSS RefPack)
#### RefPack
```
  000h 2     Method (10FBh, or 11FBh,90FBh,91FBh) (big-endian)
  ...  (3/4) Compressed size   (24bit or 32bit)   (optional)
  ...  3/4   Uncompressed size (24bit or 32bit)   (big-endoan)
  ...  ..    Compressed data
```
The compression is some kind of LZSS/LZH variant (similar to Z-Axis .ZAL
files). The compressed data consists of a big-endian bit-stream (or
byte-stream, as all codes are multiples of 8bits). The Compression codes are:<br/>
```
  0ddzzzrrdddddddd                  rawlen=r(2), lzlen=z(3)+3,  disp=d(10)+1
  10zzzzzzrrdddddddddddddd          rawlen=r(2), lzlen=z(6)+4,  disp=d(14+1
  110dzzrrddddddddddddddddzzzzzzzz  rawlen=r(2), lzlen=z(10)+5, disp=d(17)+1
  111rrrrr                          rawlen=r(5)*4+4, lzlen=0
  111111rr                          rawlen=r(2), lzlen=0, endflag=1
```
refpack\_decompress:<br/>
```
  method=BigEndian16bit[src], src=src+2
  if (method AND 100h)>0 then src=src+3+method/8000h ;compressed size, if any
  if (method AND 8000h]=0 then dst_size=BigEndian24bit[src], src=src+3
  if (method AND 8000h)>0 then dst_size=BigEndian32bit[src], src=src+4
  endflag=0
 @@decompress_lop:
  if ([src] AND 80h)=0 then
    rawlen=[src] AND 03h
    lzlen=([src] AND 1Fh)/4+3
    disp=([src] AND 60h)*8+[src+1]+1
    src=src+2
  elseif ([src] AND 40h)=0 then
    rawlen=[src+1]/40h
    lzlen=[src] AND 3Fh+4
    disp=([src+1] AND 3Fh)*100h+[src+2]+1
    src=src+3
  elseif ([src] AND 20h)=0 then
    rawlen=[src] AND 03h
    lzlen=([src] AND 0Ch)*40h+[src+3]+5
    disp=([src] AND 10h)*1000h+[src+1]*100h+[src+2]+1
    src=src+4
  elseif ([src] AND FCh)=FCh then
    rawlen=[src] AND 03h
    lzlen=0
    src=src+1, endflag=1
  else
    rawlen=([src] AND 1Fh)*4+4
    lzlen=0
    src=src+1
  for i=1 to rawlen, [dst]=[src], src=src+1, dst=dst+1, next i
  for i=1 to lzlen, [dst]=[dst-disp], dst=dst+1, next i
  if endflag=0 then goto @@decompress_lop
  if (dst-dst_base)<>dst_size then error
  ret
```



##   CDROM File Compression EA Methods (Huffman)
#### Huffman
```
  000h 2    Method (30FBh..35FBh) (big-endian)
  ...  (3)  Extra 3 bytes (only present if Method.bit8=1)
  ...  3    Decompressed Size     (big-endian)
  ...  1    Escape code
  ...  ..   Number of codes per width
  ...  ..   Data placement for each code
  ...  ..   Compressed Data
```

#### Huffman
```
  decompress_ea_huffman:
   method=GetBits(16)    ;3xFBh                     ;-get method (30FBh..35FBh)
   if method AND 100h then dummy=GetBits(24)        ;-skip extra (if any)
   dst_size=GetBits(24)                             ;-get uncompressed size
   ESC=GetBits(8)                                   ;-get escape code
   huffwidth=0, huffcode=0, totalnumcodes=0         ;\
   while (huffcode shl (10h-huffwidth))<10000h      ;
     num=GetVarLenCode                              ; get num codes per width
     huffwidth=huffwidth+1                          ;
     numcodes_per_width[width]=num                  ;
     totalnumcodes=totalnumcodes+num                ;
     huffcode=(huffcode*2)+num                      ;/
   for i=0 to FFh, data_defined_flags[i]=00h        ;\
   dat=FFh, index=0                                 ;
   while index<totalnumcodes                        ;
     n=GetVarLenCode+1               ;-             ; get/assign data values
     while n>0  ;search Nth notyet defined entry    ;
       dat=(dat+1) AND FFh  ;wrap in 8bit range!    ;
       if data_defined_flags[dat]=0 then n=n-1      ;
     data_defined_flags[dat]=1                      ;
     data_values[index]=dat, index=index+1          ;/
   huffcode=0000h, index=0                          ;\
   InitEmptyHuffTree(data_tree)                     ;
   for width=1 to huffwidth                         ;
     for i=1 to numcodes_per_width[width]           ; create huffman tree
       dat=data_values[index], index=index+1        ;
       CreateHuffCode(data_tree,dat,huffcode,width) ;
       huffcode=huffcode+(1 shl (10h-width)         ;/
  @@decompress_lop:                                 ;\
   dat=GetHuffCode(data_tree)                       ;
   if dat<>ESC                                      ;
     [dst]=dat, dst=dst+1                           ; decompress
   else                                             ;
     num=GetVarLenCode                              ;
     if num=0 then                                  ;
       if GetBits(1)=1 then goto @@decompress_done  ;
       [dst]=GetBits(8), dst=dst+1                  ;
     else                                           ;
       dat=[dst-1]                                  ;
       for i=0 to num-1, [dst]=dat, dst=dst+1       ;
   goto @@decompress_lop                            ;/
  @@decompress_done:
   if (dst-dst_base)<>dst_size then error                 ;-error check
   dst=dst_base, x=00h, y=00h                             ;\
   if (method AND FEFFh)=32FBh                            ; optional final
     for i=0 to dst_size-1, x=x+[dst+i], [dst+i]=x        ; unfiltering
   if (method AND FEFFh)=34FBh                            ;
     for i=0 to dst_size-1, x=x+[dst+i], y=y+x, [dst+i]=y ;/
   ret
  ;------------------
  GetVarLenCode:
   num=2
   while GetBits(1)=0, num=num+1
   return (GetBits(num)+(1 shl num)-4)
  GetBits(num):
   return "num" bits, fetched from big-endian bitstream
  GetHuffCode(data_tree):
   ...
  InitEmptyHuffTree(data_tree):
   ...
  CreateHuffCode(data_tree,dat,huffcode,width):
   ...
  numcodes_per_width[10h]   ;9bit numcodes per width 0..15 (entry[0]=unused)
  data_values[100h]         ;8bit data values for up to 100h huffman codes
  data_defined_flags[100h]  ;1bit flags for data(00h..FFh)
```




##   CDROM File Compression EA Methods (BPE)
#### Byte-Pair Encoding
```
  000h 2    Method (46FBh or 47FBh) (big-endian)
  ...  (5)  Extra 5 bytes (only present if Method=47FBh)
  ...  3    Decompressed Size       (big-endian)
  ...  1    Escape code
  ...  1    Number of Dict entries (N)
  ...  N*3  Dict (each 3 bytes: Index,Dat1,Dat2)
  ...  ..   Compressed Data
```
decompress\_bpe:<br/>
```
  method=BigEndian16bit[src], src=src+2
  if method=47FBh then src=src+5
  dst_size=BigEndian24bit[src], src=src+3
  esc=[src], src=src+1
  num=[src], src=src+1
  for i=0 to FFh, dict1[i]=i    ;initially default=self (uncompressed bytes)
  for i=1 to num, j=[src], dict1[j]=[src+1], dict2[j]=[src+2], src=src+3
 @@decompress_lop:
  x=[src], src=src+1
  if x=dict1[x] then
    if x=esc then x=[src], src=src+1, if x=00h then goto @@decompress_done
    [dst]=x, dst=dst+1
  else
    heap[0]=x, i=1
    while i>0
      i=i-1, x=heap[i], a=dict1[x]
      if a=x then [dst]=x, dst=dst+1                    ;\output data to
      else b=dict2[x], heap[i]=b, heap[i+1]=a, i=i+2    ;/dst or heap
  goto @@decompress_lop
 @@decompress_done:
  if (dst-dst_base)<>dst_size then error
  ret
```



##   CDROM File Compression EA Methods (RLE)
#### Run-Length Encoding
```
  000h 2    Method (4AFBh=24bit or 4A31h=16bit) (big-endian)
  ...  2/3  Decompressed Size (24bit or 16bit)  (big-endian)
  ...  ..   Compressed Data
```
Compression codes are:<br/>
```
  00h..3Fh  Copy 0..3Fh uncompressed bytes
  40h..7Fh  Load new fillbyte and fill 0..3Fh bytes
  80h..BFh  Use old fillbyte and fill 0..3Fh bytes (initial fillbyte=00h)
  C0h..FFh  Copy 0..3Fh bytes with constant value in upper 4bit
```
decompress\_bpe:<br/>
```
  method=BigEndian16bit[src], src=src+2
  if (method AND 00FFh)=31h then dst_size=BigEndian16bit[src], src=src+2
  if (method AND 00FFh)<>31h then dst_size=BigEndian24bit[src], src=src+3
  fillbyte=00h  ;initially zero
 @@decompress_lop:
  type=[src]/40h, len=[src] AND 3Fh, src=src+1, dst_size=dst_size-len
  if type=0 then                                          ;\uncompressed bytes
    for i=1 to len, [dst]=[src], src=src+1, dst=dst+1     ;/
  elseif type=1 then                                      ;\
    fillbyte=[src], src=src+1                             ; fill with new dat
    for i=1 to len, [dst]=fillbyte, dst=dst+1             ;/
  elseif type=2 then                                      ;\fill with old dat
    for i=1 to len, [dst]=fillbyte, dst=dst+1             ;/
  elseif type=3 then
    x=[src], [dst]=x, src=src+1, dst=dst+1, x=x AND F0h
    for i=2 to len      ;<-- or so?
      if (i AND 1)=0 then [dst]=x+([src]/10h) dst=dst+1
      if (i AND 1)=1 then [dst]=x+([src] AND 0Fh), dst=dst+1, src=src+1
  if dst_size<>0 then goto @@decompress_lop
  ret
```



##   CDROM File Compression ZIP/GZIP/ZLIB (Inflate/Deflate)
Inflate/Deflate is a common (de-)compression algorithm, used by ZIP, ZLIB, and
GZIP.<br/>

[Inflate - Core Functions](cdromfileformats.md#inflate-core-functions)<br/>
[Inflate - Initialization & Tree Creation](cdromfileformats.md#inflate-initialization-tree-creation)<br/>
[Inflate - Headers and Checksums](cdromfileformats.md#inflate-headers-and-checksums)<br/>

#### PSX Disk Images
In PSX cdrom-images, ZLIB is used by the .CDZ cdrom-image format:<br/>
[CDROM Disk Image/Containers CDZ](cdromfileformats.md#cdrom-disk-imagecontainers-cdz)<br/>
In PSX cdrom-images, Inflate is used by .PBP and .CHD cdrom-image formats:<br/>
[CDROM Disk Images PBP (Sony)](cdromfileformats.md#cdrom-disk-images-pbp-sony)<br/>
[CDROM Disk Images CHD (MAME)](cdromfileformats.md#cdrom-disk-images-chd-mame)<br/>

#### PSX Games
In PSX games, ZLIB is used by:<br/>
```
  Twisted Metal 4 (MagDemo30: TM4DATA\*.MR\* and *.IMG\*)
  Kula Quest / Kula World / Roll Away (*.PAK) (*.PAK\*)
  (and probably more games... particulary files starting with "x")
```
In PSX games, GZIP is used by:<br/>
```
  Final Fantasy VII (FF7) (BATTLE\TITLE.BIN)
  Gran Turismo 2 (MagDemo27: GT2\*) (with corrupted/zeropadded GZIP footers)
  Mat Hoffman's Pro BMX (old demo) (MagDemo39: BMX\BMXCD.HED\TITLE_H.ZLB)
```
In PSX games, Inflate (with slightly customized block headers) is used by:<br/>
```
  Mat Hoffman's Pro BMX (new demo) (MagDemo48: MHPB\FE.WAD+STR)
```
In PSX games, Inflate (with ignored block type, dynamic tree only) is used by:<br/>
```
  Project Horned Owl (COMDATA.BIN, DEMODATA.BIN, ROLL.BIN, ST*DATA.BIN)
```



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
#### tinf\_gzip\_uncompress(dst, destLen, src, sourceLen)
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
  k=max(length,5552)    ;max length for avoiding 32bit overflow before mod
  for i=0 to k-1, s1=s1+[src], s2=s2+s1, src=src+1, next i
  s1=s1 mod 65521, s2=s2 mod 65521, length=length-k
 return (s2*10000h+s1)
```




##   CDROM File Compression LArc/LHarc/LHA (LZS/LZH)
LHA (formerly LHarc) is an old DOS compression tool with backwards
compatibility for LArc. LHA appears to have been particulary popular in Japan,
and in the Amiga scene.<br/>
LHA archives are used by at least one PSX game:<br/>
```
  PSX Championship Surfer (MagDemo43: HWX\*.DAT)    ;method lh5
```
And, there are various PSX games with compression based on LArc's method lz5:<br/>
[CDROM File Compression LZ5 and LZ5-variants](cdromfileformats.md#cdrom-file-compression-lz5-and-lz5-variants)<br/>

#### Overall File Format
Default archive filename extension is .LZH for LHarc/LHA (lh\*-methods), or .LZS
for LArc (lz\*-methods).<br/>
Archives can contain multiple files, and are usually terminated by a 00h-byte:<br/>
```
  LHA Header+Data for 1st file
  LHA Header+Data for 2nd file
  End Marker (00h)
```
There is no central directory, one must crawl all headers to create a list of
files in the archive.<br/>
Caution: There is a hacky test file (larc333\initial.lzs) with missing end byte
(it does just end at filesize).<br/>
LHA Header v2 Headersize=xx00h would conflict with End Byte (as workaround,
insert a Nullbyte between Ext.Headers and Data to change Headersize to xx01h.<br/>

#### LHA Header v0 (with [14h]=00h)
```
  00h     1   Header Size (Method up to including Extended Area) (=16h+F+E)
  01h     1   Header Checksum, sum of bytes at [02h+(0..15h+F+E)]
  02h     5   Compression Method (eg. "-lh0-"=Uncompressed)
  07h     4   Compressed Size
  0Bh     4   Uncompressed Size
  0Fh     2   Last modified time (in MS-DOS format)
  11h     2   Last modified date (in MS-DOS format)
  13h     1   MS-DOS File attribute (usually 20h)
  14h     1   Header level (must be 00h for v0)
  15h     1   Path\Filename Length
  16h     (F) Path\Filename (eg. "PATH\FILENAME.EXT")
                     '\' may apper in the 2nd byte of Shift_JIS, processing
                     of Shift_JIS is indispensable when you need full
                     implementation of reading Pathname.
  16h+F   2   CRC16 (with initial value 0000h) on uncompressed file
  18h+F   (E) Extended area (used by UNIX in v0)
  18h+F+E ..  Compressed data
```
Note: Reportedly, old LArc files don't have CRC16 (unknown if that is true, the
ONLY known version is LArc v3.33, which DOES have CRC16, if older versions
didn't have that CRC then they did perhaps behave as if E=(-2)?).<br/>

#### LHA Header v1 (with [14h]=01h)
```
  00h     1   Header Size (Method up to including 1st Ext Size) (=19h+F+E)
  01h     1   Base Header Checksum, sum of bytes at [02h+(0..18h+F+E)]
  02h     5   Compression Method (eg. "-lh0-"=Uncompressed)
  07h     4   Skip size (size of all Extended Headers plus Uncompressed Size)
  0Bh     4   Uncompressed Size
  0Fh     2   Last modified time (in MS-DOS format)
  11h     2   Last modified date (in MS-DOS format)
  13h     1   Reserved     (must be 20h) (but is 02h on Amiga)
  14h     1   Header level (must be 01h for v1)
  15h     1   Length of Filename (or 00h when name is in Extended Header)
  16h     (F) Filename (eg. "FILENAME.EXT; path (if any) is in Extended Header)
  16h+F   2   CRC16 (with initial value 0000h) on uncompressed file
  18h+F   1   Compression Tool OS ID (eg. "M"=MSDOS)
  19h+F   (E) Extended area (unused in v1, use Ext Headers instead)
  19h+F+E 2   Size of 1st Extended Header (0000h=None)
  1Bh+F+E ..  Extended Header(s) (optional stuff)
  ...     ..  Compressed data
```

#### LHA Header v2 (with [14h]=02h)
```
  00h     2   Header Size (whole Header including all Extended Headers)
  02h     5   Compression Method (eg. "-lh0-"=Uncompressed)
  07h     4   Compressed Size
  0Bh     4   Uncompressed Size
  0Fh     4   Last modified date and time (seconds since 1st Jan 1970 UTC)
  13h     1   Reserved     (must be 20h) (but is 02h on Amiga)
  14h     1   Header level (must be 02h for v2)
  15h     2   CRC16 (with initial value 0000h) on uncompressed file
  17h     1   Compression Tool OS ID (eg. "M"=MSDOS)
  18h     2   Size of first Extended Header (0000h=None)
  1Ah     ..  Extended Header(s) (filename and optional stuff)
  ...     0/1 Nullbyte (End-Marker conflict: change Headersize xx00h to xx01h)
  ...     ..  Compressed data
```

#### LHA Header v3 (with [14h]=03h)
Kinda non-standard (supported only in late japanese LHA beta versions): Allows
Header and Ext.Headers to exceed 64Kbyte, which is rather useless.<br/>
```
  00h     2   Word size for 32bit Header entries (always 4=32bit)
  02h     5   Compression Method (eg. "-lh0-"=Uncompressed)
  07h     4   Compressed Size
  0Bh     4   Uncompressed Size
  0Fh     4   Last modified date and time (seconds since 1st Jan 1970 UTC)
  13h     1   Reserved     (must be 20h)
  14h     1   Header level (must be 03h for v3)
  15h     2   CRC16 (with initial value 0000h) on uncompressed file
  17h     1   Compression Tool OS ID (eg. "M"=MSDOS)
  18h     4   Header Size (whole Header including all Extended Headers)
  1Ch     4   Size of first Extended Header (00000000h=None)
  20h     ..  Extended Header(s) (filename and optional stuff)
  ...     ..  Compressed data
```

#### Compression Methods
```
  Method Len    Window
  -lz4-  -  -   -        LArc Uncompressed File
  -lh0-  -  -   -        LHA  Uncompressed File
  -lhd-  -  -   -        LHA  Uncompressed Directory name entry
  -lzs-  2..17  2Kbyte   LArc LZSS-Compressed  (rare, very-very old)    ;-15bit
  -lz5-  3..17  4Kbyte   LArc LZSS-Compressed  (LArc srandard)          ;-16bit
  -lh1-  3..60  4Kbyte   LHA  LZHUF-Compressed (old LHA standard)
  -lh2-  3..256 8Kbyte   LHA  Obscure test     (used in self-extractor)
  -lh3-  3..256 8Kbyte   LHA  Obscure test     (experimental)
  -lh4-  3..256 4Kbyte   LHA  AR002-Compressed (rare, for small RAM)    ;\4bit
  -lh5-  3..256 8Kbyte   LHA  AR002-Compressed (new LHA standard)       ;/
  -lh6-  3..256 32Kbyte  LHA  AR002-Compressed (rare)                   ;\
  -lh7-  3..256 64Kbyte  LHA  AR002-Compressed (rare)                   ; 5bit
  -lh8-  3..256 64Kbyte  LHA  AR002-Compressed (accidently same as lh7) ;
  -lh9-  3..256 128Kbyte LHA  AR002-Compressed (unimplemented proposal) ;
  -lha-  3..256 256Kbyte LHA  AR002-Compressed (unimplemented proposal) ;
  -lhb-  3..256 512Kbyte LHA  AR002-Compressed (unimplemented proposal) ;
  -lhc-  3..256 1Mbyte   LHA  AR002-Compressed (unimplemented proposal) ;
  -lhe-  3..256 2Mbyte   LHA  AR002-Compressed (unimplemented proposal) ;
  -lhx-  3..256 512Kbyte LHA  AR002-Compressed (rare)                   ;/
```
Apart from above methods, there are various other custom hacks/extensions.<br/>

#### Extended Headers
```
  00h     1   Extension Type (00h..FFh, eg. 01h=Filename)
  01h     ..  Extension Data
  ...     2/4 Size of next Extended Header (0=None) (v1/v2=16bit, v3=32bit)
```
Extension Type values:<br/>
```
  00h   CRC16 on whole Header with InitialValue=0000h and InitialCrcEntry=0000h
  01h   Filename
  02h   Directory name (with FFh instead of "\", and usually with trailing FFh)
  3Fh   Comment (unspecified format/purpose)
  40h   MS-DOS File attribute of MS-DOS format
  41h   Windows FILETIME for last access, creation, and modification
  42h   Filesize (uncompressed and compressed size, when exceeding 32bit)
  50h   Unix Permission
  51h   Unix User ID and Group ID
  52h   Unix Group name
  53h   Unix User name (owner)
  54h   Unix Last modified time in time_t format
  7Dh   Capsule offs/size (if the OS adds extra header/footer to the filebody)
  7Eh   OS/2 Extended attribute
  7Fh   Level 3 Attribute in Unix form and MS-DOS form
  FFh   Level 3 Attribute in Unix form
```
Note: There appears to be no MAC specific format (instead, the LHA MAC version
is including a MacBinary header in the compressed files).<br/>

#### See also
The site below has useful links with info about headers (see LHA Notes), source
code, and test archives:<br/>
```
  http://fileformats.archiveteam.org/wiki/LHA
```



##   CDROM File Compression UPX
#### UPX Compression (used in AmiDog's GTE test)
UPX is a tool for creating self-decompressing executables. It's most commonly
used for DOS/Windows EXE files, but it does also support consoles like PSX. The
PSX support was added in UPX version 1.90 beta (11 Nov 2002).<br/>
```
  000h 88h      Standard PS-X EXE header
  088h 20h      Unknown
  0A8h 4        ASCII ID "UPX!"
  0ACh 1Eh      Unknown
  0CAh 9Ah      ASCII "$info: This file is ..."
  164h 69Ch     Zerofilled
  800h ..       Leading zeropadding (to make below end on 800h-byte boundary)
  ...  ..       Decompression stub
  ...  ..       Compressed data (ending on 800h-byte boundary)
```



##   CDROM File Compression LZMA
LZMA is combining LZ+Huffman+Probabilities. The LZ+Huffman bitstream is rather
simple (using hardcoded huffman trees), the high compression ratio is reached
by predicting probabilities for the bitstream values (that is, the final
compressed data is smaller than the bitstream).<br/>

#### LZMA Bitstreams
```
  000h 1   Ignored byte (usually 00h, unknown purpose)
  001h ..  Bitstream with actual compression codes
  ...  ..  EOS end code (end of stream) (optional)
  ...  ..  Ignored byte (present in case of Normalization after last code)
  ...  ..  Padding to byte-boundary
```
Apart from the bitstream, one must know several parameters (which may be
hardcoded, or stored in custom file headers in front of the bitstream):<br/>
```
  Three decompression parameters: lc, lp, pb
  Decompressed size (required if the bitstream has no EOS end code)
  Dictionary size (don't care when decompressing the whole file to memory)
  Presence/Absence of EOS end code
```

#### .lzma files (LZMA\_Alone format from LZMA SDK)
```
  000h 1   Parameters (((pb*5)+lp)*9)+lc  (usually 5Dh)         ;\
  001h 4   Dictionary Size in bytes       (usually 10000h)      ; Header
  005h 8   Decompressed Size in bytes     (or -1=Unknown)       ;/
  00Dh 1   LZMA ignored 1st byte of bitstream (00h)             ;\LZMA
  00Eh ..  LZMA bitstream (with optional EOS end code)          ;/
```
The files are often starting with 5Dh,00h,00h. However, there's no real File
ID, and there's no CRC, the format is rather unsuitable for file sharing.<br/>
The end of the bitstream is indicated by EOS end code, or by Decompressed Size
entry (or both).<br/>

#### .lz files (LZIP)
LZIP files can contain one or more "LZIP Members" plus optional extra data:<br/>
```
  000h ..  LZIP Member(s)
  ...  ..  Optional extra data (if any) (eg. zeropadding or some SHA checksum)
```
Whereas, a normal .lz file contains only one "Member", without extra data.<br/>
Each of the "LZIP Member(s)" is having following format:<br/>
```
  000h 5   ID and version ("LZIP",01h)                          ;\LZIP Header
  005h 1   Dictionary size (5bit+3bit code, see below)          ;/
  006h ..  LZMA bitstream (with lc=3, lp=0, pb=2) (with EOS end code)
  ...  4   CRC32 on uncompressed data                           ;\
  ...  8   Size of uncompressed data                            ; LZIP Footer
  ...  8   Size of compressed data (including header+footer)    ;/
```
The dictionary size should be 1000h..20000000h bytes, computed as so:<br/>
```
  temp = 1 SHL (hdr[005h] AND 1Fh)
  dict_size = temp - (temp/10h)*(hdr[005h]/20h)
```
The LZIP format doesn't really allow to determine the uncompressed size before
decompression (one must either decompress the whole file to detect the size, or
one could try to find the Footer at end of file; which requires weird
heuristics because the LZIP manual is explicitely stating that it's valid to
append extra data after the Footer).<br/>
```
  http://www.nongnu.org/lzip/manual/lzip_manual.html#File-format
```

#### .chd (MAME compressed CDROM and HDD images)
The CHD format has its own headers and supports several compression methods
including LZMA. Leaving apart the CHD specific headers, the raw LZMA bitstreams
are stored as so:<br/>
```
  000h ..  LZMA bitstream (with lc=3, lp=0, pb=2) (without EOS end code)
```

#### .xz files (XZ Utils)
This is a slightly overcomplicated format with LZMA2 compression and optional
filters.<br/>
[CDROM File Compression XZ](cdromfileformats.md#cdrom-file-compression-xz)<br/>

#### .7z files (7-Zip archives)
```
  000h 6   ID ("7z",BCh,AFh,27h,1Ch)
  ...  ..  ..
```
The 7z format defines many compression methods. The ones normally used are
LZMA2 (default for 7-Zip 9.30 alpha +), LZMA (default for 7-Zip prior to 9.30
alpha), PPMd, and bzip2.<br/>
[http://fileformats.archiveteam.org/wiki/7z]


#### LZMA2 (used in .7z and .xz files)
LZMA2 is a container format with LZMA chunks. The LZMA function is slightly
customized: It can optionally skip some LZMA initialization steps (and thereby
re-use the dictionary/state from previous chunks). The chunks are:<br/>
```
 ChunkID=00h - Last chunk:
  000h 1   Chunk ID (00h=End)
 ChunkID=01h..02h - Uncompressed chunks:
  000h 1   Chunk ID (01h=Uncompressed+ResetDictionary, 02h=Uncompressed)
  001h 2   Uncompressed Data Size-1     (big-endian)
  003h ..  Uncompressed Data (to be copied to destination and dictionary)
  Note: The uncompressed data is stored in LZMA dictionary, and
  the last uncompressed byte is updating the LZMA prevbyte.
 ChunkID=03h..7Fh - Invalid chunks:
  000h 1   Chunk ID (03h..7Fh=Invalid)
 ChunkID=80h..FFh - LZMA-compressed chunks:
  000h 1   Chunk ID (80h/A0h/C0h/E0h + Upper5bit(UncompressedSize-1))
  001h 2   LSBs(UncompressedSize-1)       (big-endian)
  003h 2   CompressedSize-1               (big-endian)
  005h (1) Parameters (((pb*5)+lp)*9)+lc  (only present if ChunkID=C0h..FFh)
  ...  ..  LZMA bitstream (without EOS end code)
```
LZMA status gets reset depending on the Chunk ID:<br/>
```
  ChunkID  dict/prev  lc/lp/pb  state  dist[0-3]  probabilities  code/range
  01h      reset      -         -      -          -              -
  02h      -          -         -      -          -              -
  80h+n    -          -         -      -          -              reset
  A0h+n    -          -         reset  reset      reset          reset
  C0h+n    -          reset     reset  reset      reset          reset
  E0h+nn   reset      reset     reset  reset      reset          reset
  (Note: Those resets occur before processing the chunk data)
```
Note: dict/prev reset means that previous byte is assumed to be 00h (and old
dictionary content isn't used, somewhat allowing random access or multicore
decompression).<br/>
Apart from the chunks, LZMA2 does usually contain a Dictionary Size byte:<br/>
```
  Dictionary Size byte (00h..28h = 4K,6K,8K,12K,16K,24K,..,2G,3G,4G)
 Which can be decoded as so:
  if (param AND 1)=0 then dict_size=1000h shl (param/2)
  if (param AND 1)=1 then dict_size=1800h shl (param/2)
  if param=28h then dict_size=FFFFFFFFh   ;4GB-1
  if param>28h then error
 In .xz files, that byte is stored alongsides with the Filter ID.
```

#### LZMA Source code
Compact LZMA decompression ASM code can be found here:<br/>
```
  https://github.com/ilyakurdyukov/micro-lzmadec
```
Above code is for self-decompressing executables (for plain LZMA, ignore the
stuff about EXE/ELF headers). The two "static" versions are size-optimized
(they contain weird and poorly commented programming tricks, and do require
additional initialization code from "test\_static.c"). For normal purposes, it's
probably better to port the 64bit fast version to 32bit (instead of dealing
with the trickery in the 32bit static version).<br/>



##   CDROM File Compression XZ
#### Overall Structure of .xz File
```
  000h ..  Stream(s)
```
Note: To determine the total uncompressed size, one must process the file
backwards, starting at footer of last stream.<br/>

#### Stream
```
  000h 6   Header ID (FDh,"7zXZ",00h) (FDh,37h,7Ah,58h,5Ah,00h) ;\
  006h 2   Checksum Type (0000h, 0100h, 0400h or 0A00h)         ; Header
  008h 4   Header CRC32 on above 2 bytes                        ;/
  00Ch ..  Compressed Block(s)                                  ;-Block(s)
  ...  ..  Index List                                           ;-Index
  ...  4   Footer CRC32 on below 6 bytes                        ;\
  ...  4   Index List Size/4-1                                  ; Footer
  ...  2   Checksum Type (must be same as in Header)            ;
  ...  2   Footer ID ("YZ") (59h,5Ah)                           ;/
  ...  ..  Optional Zeropadding (multiple of 4 bytes)           ;-Padding
 Checksum Type (for Block checksums):
  0000h=None
  0100h=CRC32 (little-endian)
  0400h=CRC64 (little-endian)
  0A00h=SHA256 (big-endian)
  Other=Reserved
```

#### Index List
```
  000h 1    Index Indicator (00h) (as opposed to 01h..FFh in Block Headers)
  001h VL   Number of Records (must be same as number of Blocks in Stream)
  ...  ..   Index Record(s)
  ...  ..   Zeropadding to 4-byte boundary
  ...  4    CRC32 on above bytes
 Index Record:
  000h VL   Unpadded Block Size (BlockHeader + CompressedData + 0 + Checksum)
  ...  VL   Uncompressed Block Size
```

#### Compressed Block
```
  000h 1    Block Header Size/4-1 (01h..FFh = 8..400h bytes)           ;\
  001h 1    Block Flags                                                ;
  002h (VL) Compressed Size     ;present if Flags.bit6 = 1             ; Header
  ...  (VL) Uncompressed Size   ;present if Flags.bit7 = 1             ;
  ...  ..   Filter Info 0 (LAST filter when DECOMPRESSING)             ;
  ...  (..) Filter Info 1       ;present if Flags.bit0-1 = 1,2,3       ;
  ...  (..) Filter Info 2       ;present if Flags.bit0-1 = 2,3         ;
  ...  (..) Filter Info 3       ;present if Flags.bit0-1 = 3           ;
  ...  ..   Zeropadding to 4-byte boundary                             ;
  ...  (..) Optional Zeropadding (multiple of 4 bytes)                 ;
  ...  4    CRC32 on above bytes                                       ;/
  ...  ..   Compressed Data                                            ;-Data
  ...  ..   Zeropadding to 4-byte boundary                             ;-Pad
  ...  (..) Checksum on uncompressed Data (None/CRC32/CRC64/SHA256)    ;-Check
 Block Flags:
  0-1  Number of filters-1                (0..3 = 1..4 filters)
  2-5  Reserved (0)
  6    Compressed Size field is present   (0=No, 1=Present)
  7    Uncompressed Size field is present (0=No, 1=Present)
 Filter Info:
  000h VL   Filter ID
  ...  VL   Size of Filter Properties
  ...  ..   Filter Properties
 Filter IDs:
  03h                        Delta Filter       (with 1 byte param)
  04h..09h                   Executable Filters (with 0 or 4 byte param)
  21h                        LZMA2 Compression  (with 1 byte param)
  300h..4FFh                 Reserved to ease .7z compatibility
  20000h..7FFFFh             Reserved to ease .7z compatibility
  2000000h..7FFFFFFh         Reserved to ease .7z compatibility
  xxxxxxxxxxxxxxxxh          Custom Registered IDs (obtained from Lasse Collin)
  3Frrrrrrrrrriiiih          Custom Random IDs (40bit random+16bit filterno)
  4000000000000000h and up   Reserved for internal use (don't use in xz files)
```
Note: The first decompression filter must be LZMA2, which reads from compressed
data stream, and writes to decompressed data (and also implies the size of
compressed/decompressed data). The other filters (if any) are unfiltering the
decompressed data.<br/>

#### Filter 21h: LZMA2 Compression Method
This "filter" is the actual compression method (XZ supports only one method).<br/>
It can be combined with BCJ/Delta filters (whereas, LZMA2 must be always used
as LAST compression filter, aka FIRST decompression filter).<br/>
```
 The filter parameter is 1 byte tall:
  Dictionary Size byte (00h..28h = 4K,6K,8K,12K,16K,24K,..,2G,3G,4G)
 The compressed data contains:
  LZMA2 chunks (with LZMA-compressed data and/or uncompressed data)
```

#### Filter 03h: Delta Filter
The filter parameter is 1 byte tall:<br/>
```
  Distance-1 (00h..FFh = distance 1..100h)
<B> unfilter_delta(buf,len,param_byte):</B>
  dist=byte(param)+1, i=dist   ;init dist and skip first some unfiltered bytes
  while i<len, byte(buf[i]) = buf[i]+buf[i-dist], i=i+1
```

#### Filter 04h-09h: Executable Branch/Call/Jump (BCJ) Filters
These filters can replace relative jump addresses by absolute values.<br/>
```
  ID   Parameters    Alignment  Description
  04h  0 or 4 bytes  1 byte     80x86 filter (32bit or 64bit)
  05h  0 or 4 bytes  4 bytes    PowerPC filter (big endian)
  06h  0 or 4 bytes  16 bytes   IA64 filter
  07h  0 or 4 bytes  4 bytes    ARM filter (little endian)
  08h  0 or 4 bytes  2 bytes    ARM Thumb filter (little endian)
  09h  0 or 4 bytes  4 bytes    SPARC filter
  0Ah,0Bh                       Inofficial hacks/proposals for ARM64?
```
The filter parameter field can 0 or 4 bytes tall:<br/>
```
  if param_size=0 then offset=00000000h
  if param_size=4 then offset=LittleEndian32bit(param)
 Nonzero offsets are intended for executables with multiple sections and
 cross-section jumps. The offset shall/must match the filter's alignment.
<B> unfilter_bcj_x86(buf,len,offset):</B>
  i=0, len=len-4, offset=offset+4
  while i<len
    x=byte[buf+i], i=i+1
    if (x AND FEh)=E8h                     ;Opcode=E8h or E9h
      x=LittleEndian32bit[buf+i]
      if ((x+01000000h) AND FE000000h)=0   ;MSB=00h or FFh
        LittleEndian32bit[buf+i]=SignExpandLower25bit(x-i-offset)
      i=i+4
<B> unfilter_bcj_arm(buf,len,offset):</B>
  i=0, len=len/4, offset=(offset+8)/4
  while i<len
    x=LittleEndian32bit[buf+i*4]
    if (x AND FF000000h)=EB000000h
      LittleEndian32bit[buf+i*4]=((x-i-offset) and 00FFFFFFh)+EB000000h
    i=i+1
<B> unfilter_bcj_armthumb(buf,len,offset):</B>
  i=0, len=len/2-1, offset=(offset+4)/2
  while i<len
    x=LittleEndian32bit[buf+i*2]
    if (x AND F800F800h)=F800F000h
      msw=LittleEndian16bit[buf+i*2+0] AND 7FFh
      lsw=LittleEndian16bit[buf+i*2+2] AND 7FFh
      x=msw*800h+lsw-i-offset
      LittleEndian16bit[buf+i*2+0]=F000h+(7FFh and (x/800h))
      LittleEndian16bit[buf+i*2+2]=F800h+(7FFh and (x/1))
    i=i+1
<B> unfilter_bcj_sparc(buf,len,offset):</B>
  i=0, len=len/4, offset=offset/4
  while i<len
    x=BigEndian32bit[buf+i*4]
    if (x AND FFC00000h)=40000000h or (x AND FFC00000h)=7FC00000h
      x=SignExpandLower23bit(x-i-offset)
      BigEndian32bit[buf+i*4]=(x AND 3FFFFFFFh)+40000000h
    i=i+1
<B> unfilter_bcj_powerpc(buf,len,offset):</B>
  i=0, len=len/4, offset=offset/4
  while i<len
    x=BigEndian32bit[buf+i*4]
    if (x AND FC000003h)=48000001h
      BigEndian32bit[buf+i*4]=(((x/4-i-offset) AND 00FFFFFFh)*4)+48000001h
    i=i+1
<B> unfilter_bcj_ia64(buf,len,offset):</B>
  i=0, len=len/10h, offset=offset/10h
  xlat[0..1Fh]=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,6,6,0,0,7,7,4,4,0,0,4,4,0,0
  while i<len
    flags=xlat[byte[buf] and 1Fh]       ;shared 5bit for three 41bit opcodes
    for slot=0 to 2
      if flags and (1 shl slot)         ;process three 41bit opcodes
        bitbase=slot*41+5
        hi=byte[buf+(bitbase+37)/8] shr ((bitbase+37) and 7) and 0Fh
        lo=LittleEndian16bit[buf+(bitbase+9)/8] shr ((bitbase+9) and 7) and 07h
        if hi=5 and lo=0
          mid=LittleEndian32bit[buf+(bitbase+13)/8]
          x=mid shr ((bitbase+13) and 7)
          x=x and 8FFFFFh, if (x and 800000h) then x=x-700000h
          x=x-i-offset
          x=x and 1FFFFFh, if (x and 100000h) then x=x+700000h
          mid=mid AND NOT (8FFFFFh shl ((bitbase+13) and 7))  ;strip old
          mid=mid OR x shl ((bitbase+13) and 7))              ;place new
          LittleEndian32bit[buf+(bitbase+13)/8]=mid           ;apply
    i=i+1, buf=buf+10h
```

#### Cyclic Redundancy Checks (CRCs)
CRC32 uses 32bit (with polynomial=EDB88320h). CRC64 does basically use the same
function (with 64bit values and polynomial=C96C5795D7870F42h).<br/>

#### Endianness and Variable Length (VL) Integers
Little-endian is used for 16bit/32bit/64bit values (Flags, Sizes, CRCs).<br/>
Big-endian is used for 256bit SHA256 and for values within LZMA2 chunks.<br/>
Variable length integers (marked VL in above tables) are used for Sizes and
IDs, these values may contain max 63bit, stored in 1-9 bytes:<br/>
```
  decode_variable_len_integer:
   i=0, num=0
  @@lop:
   x=[src], src=src+1, num=num+((x and 7Fh) shl i), i=i+7
   if x AND 80h then goto @@lop
   return num
```

#### Notes and References
XZ Utils for Windows is claimed to work on Win98 (that is, it will throw an
error about missing MSVCRT.DLL:\_\_\_mb\_cur\_max\_func). XZ Utils for DOS does work
on Win98.<br/>
Official XZ file format specs for can be found at:<br/>
```
  https://tukaani.org/xz/format.html
```
The BCJ filters aren't documented in XZ specs, but are defined in XZ source
code, see src\liblzma\simple\\*.c). There's also this mail thread about
semi-official ARM64 filters:<br/>
```
  https://www.mail-archive.com/xz-devel@tukaani.org/msg00537.html
```



##   CDROM File Compression FLAC audio
FLAC is a lossless audio compression format.<br/>

#### FLAC file format
```
  000h 4   FLAC ID ("fLaC")
  004h ..  Metadata block with STREAMINFO
  ...  ..  Metadata block(s) with further info (optional)
  ...  ..  FLAC Frame(s)
```
The whole file can be read as big-endian bitstream (although bitstream reading
is mainly required for the Frame bodies) (the Frame header/footer and Metadata
blocks are byte-aligned and can be read as byte-stream).<br/>
Metadata Block format:<br/>
```
  1bit    Last Metadata block flag (1=Last, 0=More blocks follow)
  7bit    Block Type (see below)
  24bit   Size of following metadata in bytes (N)
  N*8bit  Metadata (depending on Type)
```
Metadata Block Types:<br/>
```
  00h = STREAMINFO
  01h = PADDING
  02h = APPLICATION
  03h = SEEKTABLE
  04h = VORBIS_COMMENT
  05h = CUESHEET
  06h = PICTURE
  ..  = Reserved
  7Fh = Invalid (to avoid confusion with a frame sync code)
```
#### FLAC METADATA\_BLOCK\_STREAMINFO
```
  16bit  Minimum Block size in samples (10h..FFFFh)  ;\min=max implies
  16bit  Maximum Block size in samples (10h..FFFFh)  ;/fixed blocksize
  24bit  Minimum Frame size in bytes (or 0=Unknown)
  24bit  Maximum Frame size in bytes (or 0=Unknown)
  20bit  Sample rate in Hertz (01h..9FFF6h = 1..655350 Hz)
  3bit   Number of channels-1 (00h..07h = 1..8 channels)
  5bit   Bits per sample-1    (03h..1Fh = 4..32 bits) (max 24bit implemented)
  36bit  Total number of samples per channel (or 0=Unknown)
  128bit MD5 on unencoded audio data (...in which format? endian/interleave?)
```

#### More info
The FLAC file format is documented here:<br/>
```
  https://xiph.org/flac/format.html
```
Source code for a compact FLAC decoder can be found here:<br/>
```
  https://www.nayuki.io/page/simple-flac-implementation
```



##   CDROM File Compression ARJ
#### ARJ archives contain several chunks
```
  Main header chunk
  Local file chunk(s)
  Chapter chunk(s), backup related, exist only in newer archives
  End Marker
```

#### ARJ main "comment" header, with [00Ah]=2
This is stored at the begin of the archive. The format is same as for local
file header (but with file-related entries set to zero, or to global security
settings).<br/>
```
  000h 2   ARJ ID (EA60h, aka 60000 decimal)
  002h 2   Header size (from 004h up to including Filename+Comment) (max 2600)
  004h 1   Header size (from 004h up to including Extra Data) (1Eh+extra)
  005h 1   Archiver version number (01h..0xh)
  006h 1   Minimum archiver version to extract (usually 01h)
  007h 1   Host OS
  008h 1   ARJ Flags (bit0-7, see below)
  009h 1   Security version (2 = current)
  00Ah 1   File Type        (must be 2=ARJ Comment in main header)
  00Bh 1   Reserved/Garbage (LSB of Archive creation Date/Time, same as [00Ch])
  00Ch 4   Date/Time when archive was created
  010h 4   Date/Time when archive was last modified
  014h 4   Zero  (or Secured Archive size, excluding Security and Protection)
  018h 4   Zero  (or Security envelope file position) (after End Marker)
  01Ch 2   Zero  (or Filespec position in filename) (0) (what is that??)
  01Eh 2   Zero  (or Security envelope size in bytes) (78h, if any)
  020h 1   Zero  (or >2.50?: Encryption version, 0-1=Old, 2=New, 4=40bit GOST)
  021h 1   Zero  (or >2.50?: Last chapter (eg. 4 when having chapter 1..4)
  022h (1) Extra data: ARJ Protection factor                         ;\extra,
  023h (1) Extra data: ARJ Flags (bit0=ALTVOLNAME, bit1=ReservedBit) ; if any
  024h (2) Extra data: Spare bytes                                   ;/
  ...  ..  Filename, max 500 bytes ("FILENAME.ARJ",00h)
  ...  ..  Comment, max 2048 bytes ("ASCII Comment",00h)
  ...  4   CRC32 on Header (from 004h up to including Comment)
  ...  2   Size of 1st extended header (usually 0=none)
  ...  (0) Extended Header(s?) (usually none such)
```

#### ARJ local file header, with [00Ah]=0,1,3,4
This occurs at the begin of each file in the archive.<br/>
```
  000h 2   ARJ ID (EA60h, aka 60000 decimal)
  002h 2   Header size (from 004h up to including Filename+Comment) (max 2600)
  004h 1   Header size (from 004h up to including Extra Data) (1Eh+extra)
  005h 1   Archiver version number
  006h 1   Minimum archiver version to extract (usually 01h)
  007h 1   Host OS
  008h 1   ARJ Flags (bit0,2-5)
  009h 1   Method
  00Ah 1   File Type (0=Binary, 1=Text, 3=Directory Name, 4=Volume Name)
  00Bh 1   Reserved/Garbage (LSB of Archive update Date/Time?)
  00Ch 4   Date/Time modified
  010h 4   Filesize, compressed (max 7FFFFFFFh)
  014h 4   Filesize, uncompressed
  018h 4   CRC32 on uncompressed file data
  01Ch 2   Zero  (or Filespec position in filename) (what is that??)
  01Eh 2   File access mode (aka MSDOS file attribute) (20h=Normal)
  020h 1   Zero  (or >2.50?: first chapter of file's lifespan)
  021h 1   Zero  (or >2.50?: last chapter of file's lifespan)
  022h (4) Extra data: Extended file position (maybe for split?)  ;\extra,
  026h (4) Extra data: Date/Time accessed                  ;\ARJ  ; 0,4 or 10h
  03Ah (4) Extra data: Date/Time created                   ; 2.62 ; bytes
  03Eh (4) Extra data: Original file size even for volumes ;/     ;/
  ...  ..  Filename, max 500 bytes ("PATH/FILENAME.EXT",00h)
  ...  ..  Comment, max 2048 bytes ("ASCII Comment",00h)
  ...  4   CRC32 on Header (from 004h up to including Comment)
  ...  2   Size of 1st extended header (usually 0=none)
  ...  (0) Extended Header(s?) (usually none such)
  ...  ..  Compressed file data
```
Entry 3Eh might be meant to contain Original Size of TEXT files (with CR,LFs),
however, the entry is just set to 00000000h in ARJ 2.75a. Or maybe it's meant
to mean size of whole file (in split-volumes)?<br/>

#### ARJ backup "chapter" header (ARJ \>2.50?) (exists in 2.75a), with [00Ah]=5
This is rarely used and supported only in newer ARJ versions. The format is
same as for local file header (but with file-related entries being nonsense in
TECHNOTE; in practice, those nonsense values seem to be zero).<br/>
```
  000h 2   ARJ ID (EA60h, aka 60000 decimal)
  002h 2   Header size (from 004h up to including Filename+Comment) (max 2600)
  004h 1   Header size (from 004h up to including Extra Data) (1Eh+extra)
  005h 1   Archiver version number (eg. 0Ah=2.75a)
  006h 1   Minimum archiver version to extract (usually 01h)
  007h 1   Host OS
  008h 1   ARJ Flags (usually 00h)
  009h 1   Method (usually 01h, although chapters have no data)  what file???
  00Ah 1   File Type (must be 5=ARJ Chapter)
  00Bh 1   Reserved/Garbage (LSB of Chapter Date/Time, same as [00Ch])
  00Ch 4   Date/Time stamp created
  010h 4   Zero  (or reportedly, ?)                              what question?
  014h 4   Zero  (or reportedly, ?)                              what question?
  018h 4   Zero  (or reportedly, original file's CRC32)          what file???
  01Ch 2   Zero  (or reportedly, entryname position in filename) what file???
  01Eh 2   Zero  (or reportedly, file access mode)               what file???
  020h 1   Chapter range start (01h=First chapter?)              what range???
  021h 1   Chapter range end   (contains same value as above)    what range???
  022h (4) Extra data: Extended file position (usually none such)what extra???
  ...  ..  Filename ("<<<001>>>",00h for First chapter)
  ...  ..  Comment  ("",00h)
  ...  4   CRC32 on Header (from 004h up to including Comment)
  ...  2   Size of 1st extended header (usually 0=none)
  ...  (0) Extended Header(s?) (usually none such)
```

#### ARJ End Marker (with [002h]=0000h)
This is stored at the end of the archive.<br/>
```
  000h 2   ARJ ID (EA60h, aka 60000 decimal)
  002h 2   Header size (0=End)
```
Note: The End Marker may be followed by PROTECT info and Security envelope.<br/>

#### ARJ Method [009h]
```
  0 = stored (uncompressed)
  1 = compressed most (default) (Window=6800h=26Kbyte, Chars=255, Tree=31744)
  2 = compressed medium         (Window=5000h=20Kbyte, Chars=72, Tree=30720)
  3 = compressed less           (Window=2000h=8Kbyte, Chars=32, Tree=30720)
  4 = compressed least/fastest  (Window=6800h? or 8000h?)
  8 = no data, no CRC  ;\unknown if/where that is used (maybe only used
  9 = no data          ;/internally, and never stored in actual files?)
```

#### ARJ File Type [00Ah]
```
  0 = binary file (default)
  1 = text file (with converted line breaks, via -t1 switch)
  2 = ARJ comment header (aka ARJ main file header)
  3 = directory name
  4 = volume label (aka disc name)
  5 = ARJ chapter label (aka begin of newer backup sections)
```

#### ARJ Flags (in Main [008h])
```
  0  GARBLED
  1  OLD_SECURED   has old signature (with signature in Main Header?)
  1  ANSIPAGE      ANSI codepage used by ARJ32 (for what? for "FILENAME.ARJ"?)
  2  VOLUME        presence of succeeding volume
  3  ARJPROT
  4  PATHSYM       archive name translated ("\" changed to "/")
  5  BACKUP        obsolete
  6  SECURED       has new signature (in security envelope?)
  7  ALTNAME       dual-name archive
```
#### ARJ Flags (in Local [008h])
```
  0  GARBLED       passworded file
  1  NOT USED
  2  VOLUME        continued file to next volume (file is split)
  3  EXTFILE       file starting position field (for split files)
  4  PATHSYM       filename translated ("\" changed to "/")
  5  BACKUP_FLAG   obsolete
```
#### ARJ Flags (in Chapter [008h])
```
  0  GARBLED                          ;\
  1  RESERVED                         ;
  2  VOLUME                           ; what does that mean in Chapters???
  3  EXTFILE                          ;
  4  PATHSYM                          ;/
  5  BACKUP        obsolete < 2.50a   ;-how can obsolete exist in Chapters???
  6  RESERVED
```

#### Host OS [007h]
```
  0=MSDOS, 1=PRIMOS, 2=UNIX, 3=AMIGA, 4=MACDOS (aka MAC-OS)
  5=OS/2, 6=APPLE GS, 7=ATARI ST, 8=NEXT
  9=VAX VMS, 10=WIN95, 11=WIN32 (aka WinNT or so?)
```

#### ARJ Method 1-3 (LHA/LZH compression)
These methods are same as LHA's "-lh6-" compression method (albeit the three
ARJ methods are allocating slighly less memory for the sliding window).<br/>

#### ARJ Method 4 (custom fastest compression)
```
 @@decompress_lop:
  if dst>=dst_end then goto @@decompress_done
  width=count_ones(max=7), len = get_bits(width) + (1 shl width)+1
  if len=2 then
    [dst]=get_bits(8), dst=dst+1
  else ;len>=3
    width=count_ones(max=4)+9, disp = get_bits(width) + (1 shl width)-1FFh
    for i=1 to len, [dst]=[dst-disp], dst=dst+1, next i
  goto @@decompress_lop
 @@decompress_done:
  ret
 ;---
 count_ones(max):
  num=0
 @@lop:
  if get_bits(1)=1 then
    num=num+1, if num<max then goto @@lop
  return num
```
get\_bits(N) is same as in method 1-3 (fetching N bits, MSB first, starting with
bit7 of first byte).<br/>

#### ARJ Glossary & Oddities
BACKUPs seem to keep old files (instead overwrting them by newer files)<br/>
CHAPTERs seems to be a new backup type (instead of [008h].Bit5=Backup flag).<br/>
COMMENTS can be text... with ANSI.SYS style ANSI escape codes?<br/>
DATE/TIME stamps seem to be MSDOS format (16bit date plus 16bit time)<br/>
EXTENDED headers seem to be unused, somewhat inspired on LHA format but with
CRC32 instead CRC16 (unknown if the "1st extended header" can be followed by
2nd, 3rd, and further extended headers in LHA fashion) (bug: older ARJ versions
are reportedly treating the extended CRC32 as 16bit value).<br/>
GARBLED seems to refer to encrypted password protected archives.<br/>
PROTECTED seems to mean Error Correction added in newer ARJ archives.<br/>
SECURED seems to mean archive with signature from registered manufacturers.<br/>
SPLIT aka VOLUMEs means large ARJ's stored in fragments on multiple disks.<br/>
TEXT (aka [00Ah]=1 aka -t1 switch aka "C Text" aka "7-bit text") converts
linebreaks from CR,LF to LF to save memory (the uncompressed size and
uncompressed CRC32 entries refer to that converted LF format, not to the
original CR,LF format; the official name "7-bit text" is nonsense: All
characters are stored as 8bit values, not 7bit values).<br/>
TIMEBOMB causes newer ARJ versions to refuse to work (and request the user to
check for non-existing newer updates) (eg. ARJ 2.86 is no longer working, ARJ
2.75a does still work without timebomb).<br/>

#### See also
The various ARJ versions include .TXT or .DOC files (notably, ARJ.TXT is user
manual, TECHNOTE.TXT contains hints on the ARJ file format). There's also an
open source version.<br/>



##   CDROM File Compression ARC
#### ARC Archives
ARC is an old DOS and CP/M compression tool from 1985-1990. ARC files contain
chunks in following format:<br/>
```
  000h 1     Fixed ID (1Ah)
  001h 1     Compression Method (00h..1Fh)
  002h 13    Filename ("FILENAME.EXT",00h) (garbage-padded if shorter)
  00Fh 4     Filesize, compressed
  013h 4     File Timestamp in MSDOS format
  017h 2     CRC16 with initial value 0000h on uncompressed/decrypted file
  019h (4)   Filesize, uncompressed  ;<-- not present for Method=1
  ...  ..    Compressed file data (size as stored in [00Fh])
```
The chunksize depends on the Method:<br/>
```
  Method 00h and 1Fh --> Chunksize=02h       (archive/subdir end markers)
  Method 01h         --> Chunksize=19h+[0Fh] (old uncompressed ARC archives)
  Others Methods     --> Chunksize=1Dh+[0Fh] (normal case)
```
Compression Methods (aka "header versions"):<br/>
```
  00h     End-of-archive marker (1Ah,00h)
  01h     ARC v?     Uncompressed (with short 19h-byte header)
  02h     ARC v?     Uncompressed (with normal 1Dh-byte header)
  03h     ARC v?     Packed    (RLE90)                   Used for small files
  04h     ARC v?     Squeezed  (RLE90+Huffman)           Based on CP/M Squeeze
  05h     ARC v4.00  Crunched  (OldRandomizedLZW)        Derived from LZWCOM
  06h     ARC v4.10  Crunched  (RLE90+OldRandomizedLZW)  Alike CP/M Crunch v1.x
  07h     ARC vBeta? Crunched  (RLE90+NewRandomizedLZW)  Leaked beta version?
  08h     ARC v5.00  Crunched  (RLE90+ClearGap12bitLZW)  Most common ARC method
  09h     Inofficial Squashed  (ClearGap13bitLZW)        Used by PKARC/PKPAK
  0Ah     ARC v7.xx  Trimmed   (RLE90+LZHUF)             Based on LHArc lh1
  0Ah     Inofficial Crushed   (RLE90+LZW/LZMW?)         PAK
  0Bh     Inofficial Distilled (LZ77+Huffman)            PAK v2.0
  14h-1Dh ARC v6.0 Used/reserved for Information items:
  14h     Archive info
  15h     Extended File info (maybe a prefix(?) for actual file entries?)
  16h     OS-specific info
  1Eh-27h ARC v6.0 Used/reserved for Control items:
  1Eh     ARC v6.00 Subdir (nested ARC-like format, created by the "z" option)
  1Fh     ARC v6.00 End-of-subdir marker (1Ah,1Fh)
  48h     Not used in ARC  ;\Hyper archives start with 1Ah,48h or 1Ah,53h
  53h     Not used in ARC  ;/(an unrelated format that also starts with 1Ah)
  80h-xxh Not used in ARC  ;-Spark archives (ARC-like, with extended headers)
```
Information items use standard 1Dh-byte headers (with [002h]="",00h,
[00Fh]=SizeOfAllItem(s), [019h]=Junk. The data part at offset 01Dh can contain
one or more item(s) in following format:<br/>
```
  000h 2     Item size (LEN)
  002h 1     Item Subtype
  003h ..    Item Data (LEN-3 bytes)
```
Information item types as used by ARC 6.0:<br/>
```
  Method=14h, Subtype=0  Archive description          (eg. "Comment blah",00h)
  Method=14h, Subtype=1  Archive creator program name (eg. "ARC 7.12 ...",00h)
  Method=14h, Subtype=2  Archive modifier program name
  Method=15h, Subtype=0  File description             (eg. "Comment blah",00h)
  Method=15h, Subtype=1  File long filename (if not MS-DOS "8.3" filename)
  Method=15h, Subtype=2  File extended date-time info (reserved)
  Method=15h, Subtype=3  File Icon                    (reserved)
  Method=15h, Subtype=4  File attributes (see below)  (eg. "RWHSN",00h)
  Method=16h, Subtype=.. Operating system info        (reserved)
```
File attributes can contain following uppercase chars:<br/>
```
  R=ReadAccess, W=WriteAccess, H=HiddenFile, 1=SystemFile, N=NetworkShareable
```

#### Sub-directories
Sub-directories are implemented as nested ARC files - about same as when
storing the sub-directory files in SUBDIR.ARC, and including that SUBDIR.ARC
file in the main archive with Method 02h. Except that:<br/>
It's using Method 1Eh (instead Method 02h), with filename SUBDIR (instead
SUBDIR.ARC), and with [019h]=Nonsense (instead uncompressed size), and the
nested file ends with Method 1Fh (instead Method 00h).<br/>

#### RLE90 (run-length compression with value 90h used as escape code)
ARC does use raw RLE90 for small files (eg. 4-byte "aaaa"). ARC does also use
RLE90 combined with other methods (perhaps because ARC wasn't very fast,
compressing 100Kbytes could reportedly take several minutes; and without RLE90
pre-compression it might have been yet slower).<br/>
```
  90h,00h       Output 90h, but DON'T change prevbyte    ;<-- ARC
  90h,00h       Output 90h, and DO set prevbyte=90h      ;<-- BinHex
  90h,00h       Output 90h, and UNKNOWN what to do       ;<-- StuffIt
  90h,01h..03h  Output prevbyte 00h..02h times (this is not useful)
  90h,04h..FFh  Output prevbyte 03h..FEh times (this does save memory)
  xxh           Output xxh, and memorize prevbyte=xxh
 arc_decompress_rle90:
  src_end = src+src_size
  prevbyte = <initially undefined in ARC source code>
 @@decompress_lop:
  if src>=src_end then goto @@decompress_done
  x=[src], src=src+1
  if x<>90h then
    [dst]=x, dst=dst+1, prevbyte=x    ;output x, and memorize prevbyte=x
  else  ;x=90h
    x=[src], src=src+1
    if x=00h then
      [dst]=90h, dst=dst+1            ;output 90h, but DO NOT change prevbyte
      if BinHex then prevbyte=90h     ;for BinHex, DO change prevbyte
    else
      for i=1 to x-1, [dst]=prevbyte, dst=dst+1, next i
  goto @@decompress_lop
```
RLE90 is used by ARC (and Spark and ArcFS), StuffIt, and BinHex (some of these
may handle "prevbyte" differently; the handling in ARC is somewhat stupid as it
cannot compress repeating 90h-bytes).<br/>

#### Squeeze
```
  000h 2    Number of Tree entries (0..100h) (when 0, assume tree=FEFFh,FEFFh)
  002h N*4  Tree entries (16bit node0, 16bit node1)
  ...  ..   Huffman bitstream (starting in bit0 of first byte)
  ...  ..   Maybe supposedly padding to byte boundary?
 The 16bit nodes are:
  0000h..00FFh  Next Tree index
  0100h..FEFEh  Invalid
  FEFFh         End of compressed data
  FF00h..FFFFh  Data values FFh..00h (these are somewhat inverted/reversed)
 arc_decumpress_squeeze:
  if [src]=0000h then tree=empty_tree, else tree=src+2  ;-start tree
  InitBitstreamLsbFirst(src+2+[src]*4)                  ;-start bitstream
 @@decompress_lop:
  index=0000h                                           ;\
  while index<FEFFh                                     ; huffman decode
    index=[tree+index*4+GetBits(1)*2]                   ;/
  if index>FEFFh then                                   ;-check end code
    [dst]=(index XOR FFh) AND FFh), dst=dst+1           ;-store data
    goto @@decompress_lop
  return
 empty_tree dw FEFFh,FEFFh   ;upen empty tree, ARC defines two 1bit END codes
```
[http://fileformats.archiveteam.org/wiki/Squeeze]


#### Randomized LZW
```
 arc_decompress_randomized_lzw:
  num_free=1000h, stack=empty, oldcode=-1
  for i=0 to FFFh, lzw_parent[i]=EEEEh    ;mark all codes as unused
  for i=0 to FFh, create_code(FFFFh,i)    ;codes for 00h..FFh with parent=none
 @@decompress_lop:
  if src>=src_end then goto @@decompress_done
  code=GetBitsMsbFirst(12), i=code
  if lzw_parent[i]=EEEEh then i=oldcode, push(oldbyte)  ;-for KwKwK strings
  while lzw_parent[i]<>FFFFh, push(lzw_data[i]), i=lzw_parent[i]
  oldbyte=lzw_data[i], [dst]=oldbyte, dst=dst+1
  if oldcode<>-1 then create_code(oldcode,oldbyte)
  oldcode=code
  while stack<>empty, [dst]=pop(), dst=dst+1
  goto @@decompress_lop
 @@decompress_done:
  ret
 ;---
 create_code(parent,data):
  if num_free=0 then goto @@no_further_codes, else num_free=num_free-1  ;-full
  i=(parent+data) AND 0000FFFFh                                         ;\
  if method=7 then i=(i*3AE1h) AND FFFh         ;new "fast" randomizer  ;
  else i=(sqr(i OR 800h)/40h) AND FFFh          ;old "slow" randomizer  ;
  if lzw_parent[i]=EEEEh then goto @@found_free                         ; alloc
  while lzw_sibling[i]>0000h, do i=lzw_sibling[i]    ;find chain end    ; code
  e=i, i=(i+65h) AND FFFh     ;memorize chain end & do some random skip ;
  while lzw_parent[i]<>EEEEh, do i=(i+1) AND FFFh    ;find a free code  ;
  lzw_sibling[e]=i    ;weirdly, i=0 will make it behave as sibling=none ;
 @@found_free:                                                          ;/
  lzw_data[i]=data, lzw_parent[i]=parent, lzw_sibling[i]=0000h          ;-apply
 @@no_further_codes:
  ret
```
Codes are always 12bit (unlike normal LZW that often starts with 9bit codes).<br/>
There won't be any new codes created if the table is full, the existing codes
can be kept used if they do match the remaining data (unfortunatly this LZW
variant has no Clear code for resetting the table when they don't match).<br/>
Instead of just using the first free entry, code allocation is using some weird
pseudo-random-sibling logic (which is totally useless and will slowdown
decompression, but compressed files do contain such randomized codes, so it
must be reproduced here).<br/>

#### ClearGap LZW
This is more straight non-randomized LZW with Clear codes (and weird gaps after
Clear codes). The compression (and gaps) are same as for nCompress (apart from
different headers):<br/>
[CDROM File Compression nCompress.Z](cdromfileformats.md#cdrom-file-compression-ncompressz)<br/>
```
  ARC Method 8 with 1-byte header (0Ch) --> nCompress 3-byte header 1Fh,9Dh,8Ch
  ARC Method 9 without header           --> nCompress 3-byte header 1Fh,9Dh,8Dh
```
Method 8 does have 0Ch as first byte (indicating max 12bit codesize, this must
be always 0Ch, the ARC decoder supports only that value). Method 9 uses max
13bit codesize (but doesn't have any leading codesize byte).<br/>

#### LZHUF
This is based on LHArc lh1. Like lh1, it does have 13Ah data/len codes, and
1000h distance codes. There are two differences:<br/>
```
  Differences          LHArc method lh1        ARC method 0Ah
  Data/len codes:      100h..139h=Len(3..3Ch)  100h=End, 101h..139h=Len(3..3Bh)
  Initial dictionary:  20h-filled              Uninitialized
```

#### Notes
ARC file/directory names are alphabetically sorted, that does apply even when
adding files to an existing archive (they are inserted at alphabetically sorted
locations rather than being appended at end of archive).<br/>
ARC files can be encrypted/garbled with password (via "g" option), the chunk
header doesn't contain any flags for indicating encrypted files (except, the
CRC16 will be wrong when not supplying the correct password).<br/>
ARC end-marker (1Ah,00h) may be followed by additional padding bytes, or by
additional information from third-party tools:<br/>
```
  PKARC/PKPAK adds comments (starting with "PK",AAh,55h)
  PAK adds extended records (described in PAK.DOC file in the v2.51)
```

#### See also
[http://fileformats.archiveteam.org/wiki/ARC_(compression_format)]

[https://www.fileformat.info/format/arc/corion.htm]

[http://cd.textfiles.com/pcmedic/utils/compress/arc520s.zip] - source code<br/>

[https://github.com/ani6al/arc] - source code, upgraded with method 9 and 4<br/>

[https://entropymine.wordpress.com/2021/05/11/arcs-trimmed-compression-scheme/]<br/>

[http://www.textfiles.com/programming/FORMATS/arc-lbr.pro] - benchmarks<br/>



##   CDROM File Compression RAR
RAR is a compression format for enthusiastic users (who love to download the
latest RAR version before being able to decompress those RAR files).<br/>

#### RAR v1.3 (March 1994, used only in RAR 1.402)
This format was only used by RAR 1.402, and discontinued after three months
when RAR 1.5 got released.<br/>
```
 File Header:
  000h 4     ID "RE~^" (aka 52h,45h,7Eh,5Eh)
  004h 2     Header Size  (usually 0007h, or bigger when Comment/Ext1 exist)
  006h 1     Archive Flags (80h or xxh)
  ...  (2)   Archive Comment Size   ;\Only present when ArchiveFlags.bit1=1
  ...  (..)  Archive Comment Data   ;/
  ...  (2)   Ext1 Size              ;\Only present when ArchiveFlags.bit5=1
  ...  (..)  Ext1 Data              ;/
  ...  ..    Unknown (TECHNOTE hints sth can be here, when bigger HeaderSize?)
 Archive Flags:
  0   Volume   (maybe related to split-volume on several floppies?)
  1   Comment
  2   Unknown? (non-english description is in 1.402's TECHNOTE.DOC)
  3   Unknown? (non-english description is in 1.402's TECHNOTE.DOC)
  4   Unknown? (non-english description is in 1.402's TECHNOTE.DOC)
  5   EXT1
  6   Unspecified (maybe unused)
  7   Unspecified (maybe unused, but... it's usually 1)
 File Data blocks:
  000h 4     Filesize, compressed
  004h 4     Filesize, uncompressed
  008h 2     Checksum on uncompressed? file (sum=LeftRotate16bit(sum+byte[i])
  00Ah 2     Header Size (usually 0015h+FilenameLength)
  00Ch 4     File Modification Timestamp in MSDOS format
  010h 1     File Attribute in MSDOS format (20h=Normal)
  011h 1     Flags
  012h 1     Version (0=0.99, 1=1.00, 2=1.30) (always 2 in public version)
  013h 1     Filename Length
  014h 1     Method (00h=m0a=Stored, 03h=m3a=Default) (1..5 = fastest..best)
  ...  (2)   File Comment Length        ;\Only present if FileFlags.bit3=1
  ...  (..)  File Comment Data          ;/
  ...  ..    Filename ("PATH\FILENAME.EXT", without any end marker)
  ...  ..    Unknown (TECHNOTE hints sth can be here, when bigger HeaderSize?)
  ...  ..    Compressed file data
 File Flags:
  0   Unknown? (non-english description is in 1.402's TECHNOTE.DOC)
  1   Unknown? (non-english description is in 1.402's TECHNOTE.DOC)
  2   Unknown? (non-english description is in 1.402's TECHNOTE.DOC)
  3   Comment  (non-english description is in 1.402's TECHNOTE.DOC)
  4-7 Unspecified (maybe unused)
```

#### RAR 1.5 (June 1994) and newer
Overall Chunk Format:<br/>
```
  000h 2    Chunk Header CRC; Lower 16bit of CRC32 on [002h..HdrSize-1 or less]
  002h 1    Chunk Type (72h..7Ah)
  003h 2    Chunk Flags
  005h 2    Chunk Header Size
  007h (4)  Data block size    ;<-- Only present if Flags.bit15=1
  ...  ..   Header values (depending on Chunk Type and Chunk Header Size)
  ...  ..   Data block         ;<-- Only present if Flags.bit15=1
 Chunk Types:
  72h="r"=Marker block (with "r" being 3rd byte in ID "Rar!",1Ah)
  73h="s"=Archive header
  74h="t"=File header
  75h="u"=Old style Comment header (nested within Type 73h/74h)
  76h="v"=Old style Authenticity information
  77h="w"=Old style Subblock
  78h="x"=Old style Recovery record
  79h="y"=Old style Authenticity information
  7AH="z"=Subblock
 Chunk Flags:
  0-13   Flags, meaning depends on Chunk Type
  14     If set, older RAR versions (before 1.52 or so?) will ignore the
               block and remove it when the archive is updated. If clear, the
               block is copied to the new archive file when the archive is
               updated;
               or does "older" mean older than the "archiver version"?
  15     Data Block present (0=No, 1=Yes, with size at [007h])
```

Type 72h, Marker Block (MARK\_HEAD)<br/>
This 7-byte ID occurs at the begin of RAR files (or after the executable in
case of self-extracting files).<br/>
```
  000h 7       ID ("Rar!",1Ah,07h,00h) (or "Rar!",1Ah,07h,01h for RAR 5.0)
 The above ID can be somewhat parsed as normal chunk header, as so:
  000h 2       Faux CRC          (6152h, no actual valid CRC)
  002h 1       Chunk Type        (72h)
  003h 2       Faux Flags        (1A21h, no actual meaning)
  005h 2       Chunk Header size (0007h)
```

Type 73h, Archive Header (MAIN\_HEAD)<br/>
```
  000h 2       CRC32 AND FFFFh of fields HEAD_TYPE to RESERVED2
  002h 1       Chunk Type: 73h
  003h 2       Archive HeaderFlags
  005h 2       Header size (usually 000Dh) (plus Comment Block, if any)
  007h 2       RESERVED1 (0000h)
  009h 4       RESERVED2 (0000011Dh)
  ...  (..)    Comment block ;<-- only present if Flags.bit1=1
  ...  (..)    Reserved for additional blocks
 Archive Header Chunk Flags:
  0     Volume attribute (archive volume) (split-volume? volume-label? what?)
  1     Archive comment present              ;<-- used only before RAR 3.x
          RAR 3.x uses "the separate comment block" and does not set this flag.
  2     Archive lock attribute
  3     Solid attribute (solid archive)
  4     New volume naming scheme (0=Old="name.???", 1=New="name.partN.rar")
  5     Authenticity information present     ;<-- used only before RAR 3.x
  6     Recovery record present
  7     Chunk headers are encrypted
  8     First volume                         ;<-- set only by RAR 3.0 and later
  9-13  Reserved for internal use
  14-15 See overall Chunk Format
```

Type 74h, File Header (File in Archive)<br/>
```
  000h 2     CRC32 AND FFFFh on HEAD_TYPE to FILEATTR and file name
  002h 1     Header Type: 74h
  003h 2     Bit Flags
  005h 2     File header full size including file name and comments
  007h 4     Compressed file size (can be bigger than uncompressed)
  00Bh 4     Uncompressed file size
  00Fh 1     Operating system used for archiving
  010h 4     CRC32 on uncompressed file
  014h 4     File Modification Timestamp in MSDOS format
  018h 1     RAR version needed to extract file (Major*10+Minor) (min=0Fh=1.5)
  019h 1     Compression Method (usually 35h in RAR 1.52)
  01Ah 2     Filename size
  01Ch 4     File Attribute in MSDOS format (20h=Normal, Upper24bit=whatever=0)
  ...  (..)  Comment block                      ;-Only present if Flags.bit3=1
  ...  (4)   MSBs of compressed file size       ;\Only present if Flags.Bit8=1
  ...  (4)   MSBs of uncompressed file size     ;/
  ...  ..    Filename ("PATH\FILENAME.EXT")
  ...  (..)  Filename extra fields (see Flags.bit9+bit11)
  ...  (8)   Encryption SALT                    ;-Only present if Flags.Bit10=1
  ...  (..)  Extended Time, variable size       ;-Only present if Flags.Bit12=1
  ...  (..)  * other new fields may appear here.
  ...  ..    Compressed file data
 File Chunk Flags:
  0     File continued from previous volume
  1     File continued in next volume
  2     File encrypted with password
  3     File comment present              ;<-- used only before RAR 3.x
          RAR 3.x uses the separate comment block and does not set this flag.
  4     Information from previous files is used (solid flag) ;RAR 2.0 and later
  5-7   Dictionary bits (for RAR 2.0 and later)
  8     64bit Filesizes (for files "larger than 2Gb")
  9     Unicode Filename, this can be in Dual or Single name form:
          Dual name:   "NormalName",00h,"UnicodeName"   ;<-- in UTF-8 or what?
          Single name: "UnicodeName"                    ;<-- in UTF-8
  10    Header contains 8-byte Encryption SALT entry
  11    Backup File (with version number ";n" appended to filename)
  12    Extended Time field present
  13-14 -
  15    Data Block present (always 1=With 32bit size at [007h], or 64bit size)
 Dictionary Bits (bit5-7)
  00h=Dictionary Size 64 Kbyte
  01h=Dictionary Size 128 Kbyte   ;\
  02h=Dictionary Size 256 Kbyte   ; RAR 2.0 and up
  03h=Dictionary Size 512 Kbyte   ;
  04h=Dictionary Size 1024 Kbyte  ;/
  05h=Dictionary Size 2048 Kbyte  ;\RAR ?? and up
  06h=Dictionary Size 4096 Kbyte  ;/
  07h=File is a directory         ;-RAR 2.0 and up
 Operating System Indicators:
  00h=MS DOS
  01h=OS/2
  02h=Windows
  03h=Unix
  04h=Mac OS
  05h=BeOS
  ??h=Android?
 Compression Method:
  35h=Default in RAR 1.52 (used even when file is too small to be compressed)
  xxh=Other methods (unknown values)
  30h=Stored (RAR 2.00 supports uncompressed small files and -m0 switch)
  N/A=Stored (RAR 1.52 simply ignores "-m0" switch, and enforces "-m1" or so)
```

Type 75h, Comment block:<br/>
```
  000h 2    Header CRC of fields from HEAD_TYPE to COMM_CRC
  002h 1    Chunk Type: 75h
  003h 2    Chunk Flags (unknown if/which flags are used)
  005h 2    Chunk Header size (0Eh+Compressed comment size)
  007h 2    Uncompressed comment size
  009h 1    RAR version needed to extract comment
  00Ah 1    Packing Method
  00Ch 2    Comment CRC
  00Eh ..   Compressed comment data
```

Sub-formats<br/>
The RAR format is comprised of many sub-formats that have changed over the
years. The different formats and their descriptions are as follows:<br/>
```
  * 1.3 (Does not have the RAR! signature)
        o There is difficulty finding information regarding this sub-format.
  * 1.5
        o Utilizes a proprietary compression method that is not public.
        o Considered the root model of subsequent formats.
        o A detailed list of information can be found here.
  * 2.0
        o Utilizes a proprietary compression method that is not public.
        o Based off of version 1.5 of the RAR file format.
  * 3.0
        o Utilizes the PPMII and Lempel-Ziv (LZSS)] algorithms.
        o Encryption now uses cipher block chaining (AES?-CBC) instead of AES
        o Based off of version 1.5 of the RAR file format.
```

#### See also
Older RAR versions did include a TECHNOTE file describing the file format of
those versions (TECHNOTE for 1.402 exist in unknown-language only, perhaps
russian, and TECHNOTE was discontinued somewhere between 2.5 and 2.9).<br/>
There is official decompression source code for newer RAR versions.<br/>



##   CDROM File Compression ZOO
#### ZOO Archives
```
 File Header:
  000h 20   Text Message (usually "ZOO #.## Archive.",1Ah,00h,00h)
  014h 4    ID (FDC4A7DCh) (use this ID for detection, and ignore above text)
  018h 4    Offset to first Chunk          (22h or 2Ah+commentsize?)
  01Ch 4    Offset to first Chunk, negated (-22h or -2Ah-commentsize?)
  020h 1+1  Version needed to extract (Major,Minor) (usually 1,01 or 2,00)
  022h (1)  Archive Header Type (01h)                           ;\
  023h (4)  Offset to Archive Comment (0=None)                  ; v2.00 and
  027h (2)  Length of Archive Comment (0=None)                  ; up only
  029h (1)  Version Data (01h or 03h)          "HVDATA"         ;/
 File Chunks:
  000h 4    ID (FDC4A7DCh)
  004h 1    Type of directory entry (1=Old, 2=New, with extra entries)
  005h 1    Compression method (0=Stored, 1=LZW/default, 2=LZH)
  006h 4    Offset to next Chunk
  00Ah 4    Offset to File Data
  00Eh 4    File Modification Date/time in MSDOS format
  012h 2    CRC16 on uncompressed file (with initial value 0000h)
  014h 4    Filesize, uncompressed
  018h 4    Filesize, compressed
  01Ch 1+1  Version needed to extract (Major,Minor) (usually 1,00 or 2,01)
  01Eh 1    Deleted flag (0=Normal, 1=Deleted)
  01Fh 1    File structure (unknown purpose)
  020h 4    Offset of comment field (0=None)
  024h 2    Length of comment field (0=None)
  026h 13   Short Filename ("FILENAME.EXT",00h, garbage padded if shorter)
  033h (1)  Unknown (4Fh) (or 00h when with comment?)              ;-Type=1
  033h (2)  Length of 038h and up (0Ah+longname+dirname)           ;\
  035h (1)  Timezone (signed) (7Fh=Unknown)                        ;
  036h (2)  CRC16 on Header (000h..037h+[033h], with [036h]=0000h) ;
  038h (1)  Length of Long Filename (0=None, use Short Filename)   ;
  039h (1)  Length of Directory name (0=None)                      ; Type=2
  03Ah (..) Long Filename  ("longfilename.ext",00h) (if any)       ;
  ...  (..) Directory name ("/path",00h)            (if any)       ;
  ...  (2)  System ID (0=Unix, 1=DOS, 2=Portable) (but for DOS=0)  ;
  ...  (3)  File Attributes (24bit)               (but for DOS=0)  ;
  ...  (1)  Backup Flags (bit7=On, bit6=Last, bit0-3=Generation)   ;
  ...  (2)  Backup File Version Number (for backup copies)         ;/
  ...  5    File Leader aka Fudge Factor ("@)#(",00h)              ;\
  ...  ..   File Data                                              ; All types
  ...  ..   File Comment (if any) (ASCII, "Text string",0Ah)       ;/
 Last Chunk:
  000h 4     ID (FDC4A7DCh)
  004h (30h) Zerofilled                                            ;-Type 1
  004h (1)   Fixed (02h)                                           ;\
  005h (31h) Zerofilled                                            ; Tyoe 2
  036h (2)   CRC16 on Header (with [036h]=0000h) (always 83FCh)    ;/
  ...  (..)  Comments may be stored here (if added after archive creation)
  ...  (..)  Padding, if any (1Ah-filled in some files)
```

Notes:<br/>
Method LZW is quite straight, the bitstream is fetched LSB first, codesize is
initially 9bit, max 13bit, with two special codes (100h=Clear, 101h=Stop),
there aren't any gaps after clear codes, the unusual part is that the bitstream
does start with a clear code.<br/>
Method LZH is slower, requires Zoo 2.10, and is used only when specifiying "h"
option in commandline. LZH has 8Kbyte window, same as LHA's "lh5", with an
extra end marker (blocksize=0000h=end).<br/>
Comments may be stored anywhere in the middle or at the end of the archive
(even after the zerofilled last chunk) (depending on whether the comment or
further files where last added to the archive).<br/>
Zoo is from 1986-1991, long filenames were supported only for OSes that did
support them at that time (ie. not for DOS/Windows).<br/>
When adding new files, Zoo defaults to maintain backups of old files in the
archive (older files are marked as "deleted" via [01Eh]=1, but are kept in the
archive; until the user issues command "P" for repacking/removing deleted
files) (Zoo 2.xx can additionally use a "generation" limit of 0..15, which
means to keep 0..15 older copies).<br/>
All offsets are originated from begin of archive.<br/>

#### Zoo Tiny format (single-file) (commandline "z" option)
This format is called Tiny in Zoo source code, but isn't documented in the Zoo
manual or Zoo help screen. Tiny can contain only a single file (alike gzip).
The purpose appears to be using Tiny as temporary files when moving files from
one archive to another (without needing to decompress & recompress the
file), for example:<br/>
```
  zoo xz source.too testfile.txt     ;extract to tiny/temp file testfile.tzt
  zoo az dest.zoo   testfile.txt     ;import from tiny/temp file testfile.tzt
```
The tiny/temp file extensions have the middle character changed to "z" (eg.
"tzt" instead of "txt").<br/>
Going by zoo source code, the format should look as so:<br/>
```
  000h 2   Zoo Tiny ID (07FEh)
  002h 1   Type (01h)
  003h 1   Compression Method
  004h 4   Date/time in MSDOS format
  008h 2   CRC16 on uncompressed file, or what (?)
  00Ah 4   Filesize, uncompressed
  00Eh 4   Filesize, compressed
  012h 1   Major_ver
  013h 1   Minor_ver
  014h 2   Comment size (0=None)
  016h 13  Short Filename
  023h ..  File data     ... plus comment, if any?
```
But, files from Zoo DOS version are reportedly starting with 07h,01h (instead
FEh,07h,01h).<br/>
And, using Zoo DOS version with "z" option in Win98 does merely display "Zoo:
FATAL: I/O error or disk full."<br/>

#### Zoo Filter format (for modem streaming) (commandline "f" command)
This command is documented in the Zoo manual, although it isn't actually
supported in Zoo DOS version. The intended purpose is to use Zoo as a filter to
speedup modem transfers.<br/>
Going by some information snippets, the transfer format appears to be somewhat
as so:<br/>
```
  000h 2   Zoo Filter ID (32h,5Ah)
  ...  ..  Compressed data
  ...  2   CRC16 on uncompressed file, or what (?)
```
The transfer uses stdin/stdout instead of source/dest filenames (although, the
OS commandline interface may allow to assign filenames via "\>" and "\<").<br/>
There is no compression method entry (so both sides must know whether they
shall use LZW or LZH).<br/>
Unknown if there are any transfer size entries, or LZW/LZH end codes, or maybe
the streaming is infinite (with CRCs inserted here ot there)?<br/>



##   CDROM File Compression nCompress.Z
nCompress is some kind of a Gzip predecessor. The program was originally called
"compress" and later renamed to "ncompress" (and sometimes called
"(n)compress"). Compressed files have uppercase ".Z" attached to their original
name.<br/>

#### nCompress.Z
The header is rather small and lacks info on decompressed size (ie. the one
must process the whole bitstream to determine the size, and accordingly, the
fileformat doesn't allow padding to be appended at end of file). To detect .Z
files, examine the first three bytes, and best also check that the leading 9bit
codes don't exceed num\_codes (with num\_codes increasing from 101h and up for
each new code).<br/>
```
  000h 2    ID (1Fh,9Dh)
  002h 1    Mode (MaxBits(9..16) + bit7=WithClearCode) (usually 90h)
  003h ..   ClearGap LZW compressed data (or raw LZW when mode.bit7=0)
```
Compression is relative straight LZW, resembling 8bit GIFs, with 9bit initial
codesize, with preset codes 000h..0FFh=Data and (optional) 100h=Clear code
(there is no End code). Codes are allocated from 101h and up (100h and up if
without Clear code).<br/>
The bitstream is fetched LSB first (starting in bit0 of first byte). The
decoder is prefetching groups of eight codes (N-bytes with eight N-bit codes),
the odd part is that Clear codes are discarding those prefetched bytes (so
Clear codes will be followed by Gaps with unused bytes).<br/>
ClearGap LZW is also used by ARC Method 8 and 9.<br/>



##   CDROM File Compression Octal Oddities (TAR, CPIO, RPM)
Below are file formats with unix/linux-style octal numbers (unknown if they are
serious about using that formats, or if they do consider them as decently
amusing, or whatever).<br/>

#### Compression
TAR and CPIO are uncompressed archives, however, they are usually enclosed in a
compressed Gzip file (or some other compression format like nCompress, Bzip2).<br/>

#### TAR format (1979)
```
  0000h ..        TAR Chunk(s)
  ...   400h      TAR End Marker (400h bytes zerofilled)
  ...   ..        Zerofilled (whatever further padding)
```
TAR Chunk format:<br/>
```
  000h 100 text   Filename ("path/filename.ext",00h)
  064h 8   octal  Mode Flags
  06Ch 8   octal  User ID
  074h 8   octal  Group ID
  07Ch 12  octal  Filesize
  088h 12  octal  File modification time (seconds since 01 Jan 1970)
  094h 8   octal  Header Checksum (sum of byte[0..1F3h], with [94h..9Bh]=20h)
  09Ch 1   text   Type (00h or "0" for normal files)
  09Dh 100 text   Whatever link name
  101h 8   text   Tar ID (6x00h or "ustar",00h,"00" or "ustar  ",00h)
  109h 32  text   User Name (owner)
  129h 32  text   Group Name
  149h 8   octal  Device major  ;\device number (when Type="4")
  151h 8   octal  Device minor  ;/
  159h 155 ?      Whatever prefix         ;-when ID="ustar",00h,"00" or 6x00h
  159h 131 ?      Whatever prefix         ;\
  1DCh 12  octal  File access time        ; when ID="ustar  ",00h
  1E8h 12  octal  File status-change time ;/
  1F4h 12  -      Zeropadding to 200h-byte boundary
  200h ..  -      File data (Filesize bytes)
  ...  ..  -      Zeropadding to 200h-byte boundary
```
TAR numeric values are weirdly stored as octal ASCII strings, often decorated
with leading or trailing spaces. For example, 8-byte octal value 123o (53h) can
look as so (with "." meaning 00h end-byte):<br/>
```
  "0000123."  <-- normal weirdness, with leading zeroes and end-byte ("."=00h)
  "  123 . "  <-- extra weird, leading/trailing spaces, mis-placed end-byte
  "   123  "  <-- extra weird, leading/trailing spaces, without end-byte
```
See also: [https://www.gnu.org/software/tar/manual/html_node/Standard.html]


#### CPIO Format (1977) (and MAC .PAX files)
```
  0000h ..        CPIO Chunk(s) (with actual files)
  ...   57h       CPIO Chunk    (with filename "TRAILER!!!",00h)
  ...   ..        Zeropadding to 200h-byte boundary (not always present)
```
The chunks are simple, but they do exist in five weirdly different variants:<br/>
```
  Align 2, Binary, little-endian (but partial "big-endian" for 2x16bit pairs)
  Align 2, Binary, big-endian
  Align 1, Ascii, octal strings
  Align 4, Ascii, hexadecimal lowercase strings, checksum=0)
  Align 4, Ascii, hexadecimal lowercase strings, checksum=sum of bytes in file)
```
Binary, little-or-big-endian:<br/>
```
  000h 2   binary 16bit ID (71C7h)                      ;-little-or big endian
  002h 2   binary 16bit  dev                                    ;\
  004h 2   binary 16bit  ino                                    ; same
  006h 2   binary 16bit  mode                                   ; endianness
  008h 2   binary 16bit  uid                                    ; as in ID
  00Ah 2   binary 16bit  gid                                    ;
  00Ch 2   binary 16bit  nlink                                  ; (but be aware
  00Eh 2   binary 16bit  rdev                                   ; of the fixed
  010h 2   binary 16bit File modification time, upper 16bit  ;\ ; upper/lower
  012h 2   binary 16bit File modification time, lower 16bit  ;/ ; 16bit order
  014h 2   binary 16bit Filename size (including ending 00h)    ; for time and
  016h 2   binary 16bit Filesize, upper 16bit                ;\ ; filesize)
  018h 2   binary 16bit Filesize, lower 16bit                ;/ ;/
  01Ah ..  text   Filename, terminated by 00h ("path/filename",00h)
  ...  ..  binary Zeropadding to 2-byte boundary
  ...  ..  binary File data (Filesize bytes)
  ...  ..  binary Zeropadding to 2-byte boundary
```
Ascii/octal CPIO Chunk format:<br/>
```
  000h 6   octal  18bit ID "070707" (=71C7h)
  006h 6   octal  18bit dev    ;\unique file id
  00Ch 6   octal  18bit ino    ;/within archive
  012h 6   octal  18bit Mode (file attributes)
  018h 6   octal  18bit User ID of owner
  01Eh 6   octal  18bit Group ID
  024h 6   octal  18bit nlink (related to duplicated dev/ino?)
  02Ah 6   octal  18bit rdev (system-defined info on char/blk devices)
  030h 11  octal  33bit File modification time
  03Bh 6   octal  18bit Filename size (including ending 00h)
  041h 11  octal  33bit Filesize
  04Ch ..  text   Filename, terminated by 00h ("path/filename",00h)
  ...  ..  binary File data (Filesize bytes)
```
Ascii/hex CPIO Chunk format:<br/>
```
  000h 6   hex    24bit ID "070701"=Without Checksum, or "070702"=With Checksum
  006h 8   hex    32bit  ino (does that 32bit value include 16bit "dev"?)
  00Eh 8   hex    32bit  mode
  016h 8   hex    32bit  uid
  01Eh 8   hex    32bit  gid
  026h 8   hex    32bit  nlink
  02Eh 8   hex    32bit  mtime
  036h 8   hex    32bit Filesize
  03Eh 8   hex    32bit  devmajor
  046h 8   hex    32bit  devminor
  04Eh 8   hex    32bit  rdevmajor
  056h 8   hex    32bit  rdevminor
  05Eh 8   hex    32bit Filename size (including ending 00h)
  066h 8   hex    32bit Checksum, sum of all bytes in file, zero when ID=070701
  06Eh ..  text   Filename, terminated by 00h ("path/filename",00h)
  ...  ..  binary Zeropadding to 4-byte boundary
  ...  ..  binary File data (Filesize bytes)
  ...  ..  binary Zeropadding to 4-byte boundary
```
CPIO numeric values are weird octal ASCII strings (eg. 6-byte "000123"), but,
unlike TAR, without extra oddities like spaces or end-bytes.<br/>
[https://www.systutorials.com/docs/linux/man/5-cpio/]


#### RPM Format (1997) (BIG-ENDIAN)
RPM files contain Linux installation packages. The RPM does basically contain a
CPIO archive bundled with additional header/records with installation
information.<br/>
```
  000h 60h File Header      (officially called "Lead" instead of "Header")
  060h ..  Signature Record (contains "Header Record" in "Signature format")
  ...  ..  Padding          (to 8-byte boundary)
  ...  ..  Info Record      (called "Header" and also uses "Signature format")
  ...  ..  Archive file     (usually a GZIP compressed CPIO) (called "Payload")
```
File Header (aka Lead) (60h bytes):<br/>
```
  000h 4    File ID (EDh,ABh,EEh,DBh)     (aka octal string "\355\253\356\333")
  004h 1    Major version (3)
  005h 1    Minor version (0)
  006h 2    Type (0=Binary Package, 1=Source Package)
  008h 2    Architecture ID (defined in ISO/IEC 23360)
  00Ah 66   Package name, terminated by 00h
  04Ch 2    Operating System ID (1)
  04Eh 2    Signature Type (5)
  050h 16   Reserved space (officially undefined, usually zerofilled)
```
Signature/Info Records (10h+N\*10h+SIZ bytes):<br/>
```
  000h 4     Record ID (8Eh,ADh,E8h,01h)  (aka octal string "\216\255\350\001")
  004h 4     Reserved (zerofilled)        (aka octal string "\000\000\000\000")
  008h 4     Number of Item List entries  (N)
  00Ch 4     Size of Item Data            (SIZ)
  010h N*10h Item List (4x32bit each: Tag, Type, Offset, Size)
  ...  SIZ   Item Data (referenced via Offset/Size entries in above list)
```
Item Type values:<br/>
```
  00h=NULL         Not Implemented
  01h=CHAR         Unknown, maybe unsigned 8bit         (unaligned)
  02h=INT8         Unknown, maybe signed 8bit           (unaligned)
  03h=INT16        Unknown, maybe signed 16bit          (align2)
  04h=INT32        Unknown, maybe signed 323bit         (align4)
  05h=INT64        Reserved, maybe signed 643bit        (maybe align8)
  06h=STRING       Variable, NUL terminated string      (unaligned)
  07h=BIN          Unknown, reportedly 1-byte size???   (unaligned)
  08h=STRING_ARRAY Variable, Sequence of NUL terminated strings (unaligned)
  09h=I18NSTRING   Variable, Sequence of NUL terminated strings (unaligned)
```
Item Tag values:<br/>
```
  There are dozens of required & optional tag values defined.
```
RPM source code packages are often bundled with a .spec file (inside of the
CPIO archive), that .spec file contains source code in text format for creating
the RPM header/records.<br/>

#### File Extensions
```
 Basic extensions:
  .cpio (CPIO)
  .pax  (CPIO for MAC)
  .rpm  (RPM installation package for RPM package manager)
  .spec (RPM source file for creating RPM header/records)
  .tar  (TAR, tape archive)
 Double extensions (and short forms like tgz):
  .tgz  short for .tar.gz  (gzip)
  .tbz  short for .tar.bz2 (bzip2)
  .txz  short for .tar.xz  (XZ)
  .tlz  short for .tar.lz  (Lzip) or .tar.lzma (LZMA_Alone)
  .tzst short for .tar.zst (zstandard)
  .tsz  short for .tar.sz  (Sunzip)
  .taz  short for .tar.Z   (nCompress or possibly some other compressed format)
  .tz   short for .tar.Z   (nCompress or possibly some other compressed format)
  .spm  short for .src.rpm (RPM source code package)
```



##   CDROM File Compression MacBinary, BinHex, PackIt, StuffIt, Compact Pro
Below are related to MAC filesystems (where the file body consists of separate
Data and Resource forks), and file type/creator values (resembling filename
extensions).<br/>

#### MacBinary I,II,III format (v1,v2,v3)
MacBinary contains a single uncompressed file, used for transferring MAC files
via network, or storing MAC files on non-MAC filesystems.<br/>
PackIt/StuffIt archives do often have leading MacBinary headers. MacBinary
doesn't have any unique filename extension (.bin may be used, more often it's
using the same extension as the enclosed file, eg. .sit if it contains a
StuffIt archive).<br/>
Also, archives without explicit MAC support may use MacBinary format within
compressed files (eg. LZH archives created with LHA MAC version).<br/>
```
  000h 1   Old version number, must be kept at zero for compatibility
  001h 1   Length of filename (1..63) (though v3 says 1..31)
  002h 63  Filename (only "length" bytes are significant)
  041h 4   File type    (normally expressed as four characters)
  045h 4   File creator (normally expressed as four characters)
  049h 1   Finder flags, bit8-15 (see [065h] for bit0-7)
  04Ah 1   Zero (must be 00h for compatibility)
  04Bh 2   File Vertical position within its window
  04Dh 2   File Horizontal position within its window
  04Fh 2   File Window or folder ID
  051h 1   Protected flag (bit0=Protected, whatever that is)
  052h 1   Zero (must be 00h for compatibility)
  053h 4   Filesize, Data Fork     (0=None)
  057h 4   Filesize, Resource Fork (0=None)
  05Bh 4   File Timestamp, creation
  05Fh 4   File Timestamp, last modification
  063h 27  v1:    Reserved (zerofilled)
  063h 2   v2/v3: Length of Get Info comment (if any, usually 0000h)
  065h 1   v2/v3: Finder Flags, bit0-7 (see [049h] for bit8-15)
  066h 6   v2:    Reserved (zerofilled)
  066h 4   v3:    ID ("mBIN"=MacBinary III)
  06Ah 1   v3:    Script of file name (from fdScript field of an fxInfo record)
  06Bh 1   v3:    Extended Finder flags (from fdXFlags field of fxInfo record)
  06Ch 8   v2/v3: Reserved (zerofilled)
  074h 4   v2/v3: Length of "total files" when "packed files are unpacked", uh?
  078h 2   v2/v3: Extended Header size (reserved for future, always 0000h)
  07Ah 1   v2/v3: MacBinary II uploader version           (81h=v2, 82h=v3)
  07Bh 1   v2/v3: MacBinary II downloader minimum version (81h=v2)
  07Ch 2   v2/v3: CRC16-XMODEM on [000h..07Bh]
  07Eh 2   Reserved for computer type and OS ID (0000h)
  ...  ..  Extended Header (if any, maybe stored here? when [078h]>0)
  ...  ..  Padding to 80h-byte boundary
  ...  ..  Data Fork (if any)
  ...  ..  Padding to 80h-byte boundary
  ...  ..  Resource Fork (if any)
  ...  ..  Padding to 80h-byte boundary
  ...  ..  Get Info comment (if any, usually none)
```
CRC16-XMODEM: [http://www.sunshine2k.de/coding/javascript/crc/crc_js.html]


#### BinHex 4.0 (.hqx) (ASCII, RLE90, big-endian)
Decoding binhex files is done via following steps (in that order):<br/>
```
  1) ASCII to BINARY conversion (similar to BASE64)
  2) RLE90 decompression of whole file (header+data+resource+crc's)
  3) Processing the header+data+resource from the decompressed binary
  4) For Multipart files, repeat above steps for each part
```
ASCII to BINARY:<br/>
```
  The file may start with some text message, comments, description. Skip any
  such text lines until reaching a line that contains this 45-byte ID string:
    (This file must be converted with BinHex 4.0)
  That line should be followed by following characters (each char representing
  6bit binary value, MSB first, first char is bit7-2 of first byte):
    !"#$%&'()*+,-    char(21h..2Dh) --> bin(00h..0Ch)
    0123456          char(30h..36h) --> bin(0Dh..13h)
    89               char(38h..39h) --> bin(14h..15h)
    @ABCDEFGHIJKLMN  char(40h..4Eh) --> bin(16h..24h)
    PQRSTUV          char(50h..56h) --> bin(25h..2Bh)
    XYZ[             char(58h..5Bh) --> bin(2Ch..2Fh)
    `abcdef          char(60h..66h) --> bin(30h..36h)
    hijklm           char(68h..6Dh) --> bin(37h..3Ch)
    pqr              char(70h..72h) --> bin(3Dh..3Fh)
    :                char(3Ah)      --> start/end marker
    CR/LF            char(0Dh/0Ah)  --> linebreaks per 64 chars (CR and/or LF)
    SPC/TAB          char(09h/20h)  --> blanks (reportedly in some files)
```
RLE90 Decompression:<br/>
```
  RLE90 decompression is same as in ARC files, except, code 90h,00h is handled
  differently: ARC keeps prevbyte=unchanged, BinHex sets prevbyte=90h.
  RLE90 compression is somewhat optional: 90h must be encoded as 90h,00h,
  but many encoders don't bother to compress repeating bytes (eg. many files
  contain "!!!!!!!!" chars aka uncompressed 00h-filled bytes).
  There is no way to know the decompressed size before decompression (either
  decompress the whole file and allocate more memory as needed, or decompress
  only the header (filename+16h bytes) and then compute decompressed size as
  filename+16h+data+2+resource+2 bytes).
```
Decompressed Binary (big-endian):<br/>
```
  The decompressed binary contains following data (similar as MacBinary):
    00h   1    Length of Filename (1..63)
    01h   ..   Filename ("FILENAME.EXT")
    01h+N 1    Version (00h)
    02h+N 4    File Type
    06h+N 4    File Creator
    0Ah+N 2    Finder Flags
    0Ch+N 4    Filesize, uncompressed, Data Fork
    10h+N 4    Filesize, uncompressed, Resource Fork
    14h+N 2    Header CRC16-XMODEM on uncompressed 14h+N bytes
    16h+N ..   Data Fork
    ...   2    Data Fork CRC16-XMODEM on uncompressed Data Fork
    ...   ..   Resource Fork
    ...   2    Resource Fork CRC16-XMODEM on uncompressed Resource Fork
    ...   ..   Padding (might reportedly occur in some files)
  Caution: There is a document that does claim that the CRC field should be be
  set to 0000h before CRC calculation, and that the CRC would be computed on
  Size+2 bytes (up to including he CRC field), that appears to be nonsense,
  the CRC is computed on Size+0 bytes, not Size+2.
```
Multipart files:<br/>
```
  Emails or other text documents may contain multiple binhex files, if so,
  each part should be reportedly followed by a line containing:
    --- end of part NN ---
  Unknown if there are any .hqx files with such multipart stuff.
  Unknown if the next part starts with "(This file must.." or just with ":".
```
Note: Many files with .hqx extension are actually raw .sit or .cpt files (maybe
because somebody had removed the binhex encoding without altering the filename
extension).<br/>

#### PackIt (.pit) (Macintosh) (1986) (big-endian)
MAC File Type,Creator IDs = "PIT ","PIT " \<-- normal (=uncompressed?)<br/>
MAC File Type,Creator IDs = "PIT ","UPIT" \<-- other (=compressed?)<br/>
```
 Bitstream for Uncompressed File Entries:
  32bits    Uncompressed Header[000h..003h] (Method/Crypto="PMag")
  ..bits    Uncompressed Header[004h..061h] (uncompressed size = 5Eh)
  ..bits    Uncompressed Data+Resource+CRC  (uncompressed size = Data+Rsrc+2)
 Bitstream for Compressed File Entries:
  32bits    Uncompressed Header[000h..003h] (Method/Crypto="PMa4")
  ..bits    Compressed Huffman Tree         (for decoding following bits)
  ..bits    Compressed Header[004h..061h]   (uncompressed size = 5Eh)
  ..bits    Compressed Data+Resource+CRC    (uncompressed size = Data+Rsrc+2)
  ..bits    Padding to 8bit-boundary        (byte align next File Entry)
 Bitstream for Archive End Marker (after last file):
  32bits    Uncompressed Header[000h..003h] (Method/Crypto="PEnd")
 File Entry Format:
  000h 4    Method/Crypto (usually "PMag"=Uncompressed, "PMa4"=Huffman)
  004h 1    Filename length
  005h 63   Filename ("FILENAME", garbage padded)
  044h 4    File Type
  048h 4    File Creator
  04Ch 2    Finder flags
  04Eh 2    Locked?
  050h 4    Filesize, uncompressed, Data fork
  054h 4    Filesize, uncompressed, Resource fork
  058h 4    Timestamp, creation
  05Ch 4    Timestamp, modification
  060h 2    CRC16-XMODEM on [004h..05Fh]
  ...  ..   Data Fork
  ...  ..   Resource Fork
  ...  2    CRC16-XMODEM on uncompressed Data+Resource forks
 Method/Crypto:
  "PEnd" = Archive End marker (4-byte end marker, without filename etc.)
  "PMag" = Uncompressed
  "PMa1" = Uncompressed, Encrypted Simple
  "PMa2" = Uncompressed, Encrypted DES
  "PMa3" = Uncompressed, Encrypted reserved
  "PMa4" = Huffman
  "PMa5" = Huffman, Encrypted Simple
  "PMa6" = Huffman, Encrypted DES
  "PMa7" = Huffman, Encrypted reserved
 Decompression:       ;for PackIt (and also for StuffIt method 03h)
  InitBitstreamMsbFirst(src)             ;-src is after "PMa4" PackIt ID
  tree=GetMem(200h*4)                    ;-alloc tree (probably less needed)
  num_entries=0                          ;\init tree
  root=GetTreeEntry                      ;/
  while dst<dst_end                      ;-decompress, till end...
    index=root                           ;\
    while index<FF00h                    ; huffman decode
      index=[tree+index*4+GetBits(1)*2]  ;/
    [dst]=index AND FFh, dst=dst+1       ;-store data
  return
 ;---
 GetTreeEntry:
  if GetBits(1)=1 then
    return GetBits(8)+FF00h            ;-final data entry
  else
    index=num_entries                  ;-current index
    num_entries=num_entries+1          ;-alloc next index
    [tree+index*4+0*2] = GetTreeEntry  ;-recursive call for node0
    [tree+index*4+1*2] = GetTreeEntry  ;-recursive call for node1
    return index
```
http://www.network172.com/early-mac-software/packit-source-code/] - official<br/>

#### StuffIt (.sit) (Macintosh) (old format) (1987) (big-endian)
MAC File Type,Creator IDs = "SIT!","SIT!" (version=01h).<br/>
MAC File Type,Creator IDs = "SITD","SIT!" (version=02h).<br/>
MAC File Type,Creator IDs = "APPL","STi0" (whatever, with ID="ST65")<br/>
```
 StuffIt Archive Header:
  000h 4    ID ("SIT!", short for StuffIt)
            Reportedly, there are several alternate IDs:
              "SIT!","ST46","ST50","ST60","ST65","STin","STi2","STi3","STi4"
            Unknown why, and if some do differ somehow (ST65 appears to be
            same as SIT!) (for STi, the "i" might be short for it? installer?)
  004h 2    Number of entries in root directory
  006h 4    Total size of archive
  00Ah 4    ID ("rLau", short for Raymond Lau)
  00Eh 1    Version number (01h=v1.x-v1.5.x, 02h=v1.6-v4.5)
  00Fh 7    Reserved (zerofilled)                          ;-when version=01h
  00Fh 1    Unknown (C6h or FFh)                           ;\
  010h 4    Offset to first root entry (16h or elsewhere!) ; when version=02h
  014h 2    Unknown (0001h or FFFFh)                       ;/
 File Entries:
  000h 1    Compression method, Resource fork
  001h 1    Compression method, Data fork
  002h 1    Filename length (1..63 for version=01h, 1..31 for version=02h)
  003h 1Fh  Filename ("FILENAME.EXT", garbage padding)
  022h 20h  Filename further chars                         ;-when version=01h
  022h 2    Filename+size CRC                              ;\
  024h 2    Unknown (always 0000h or 0986h?)               ; when version=02h
  026h 4    Unknown Resource fork related    ;maybe window ;
  02Ah 4    Unknown Data fork related        ;coords ?     ;
  02Eh 1    Unknown Data fork related                      ;
  02Fh 1    Unknown Resource fork related                  ;
  030h 2    Number of child entries (excluding End marker) ;
  032h 4    Offset to previous entry                       ;
  036h 4    Offset to next entry                           ;
  03Ah 4    Offset to parent entry                         ;
  03Eh 4    Offset to first child (or -1 for file entries) ;/
  042h 4    File type     (eg. "APPL")
  046h 4    File creator  (eg. "ACTA")
  04Ah 2    Finder flags  (2100h)
  04Ch 4    Creation date
  050h 4    Modification date
  054h 4    Filesize, uncompressed, Resource fork  (0=None)
  058h 4    Filesize, uncompressed, Data fork      (0=None)
  05Ch 4    Filesize, compressed, Resource fork    (0=None)
  060h 4    Filesize, compressed, Data fork        (0=None)
  064h 2    CRC16 on uncompressed(?) Resource fork (0=None)
  066h 2    CRC16 on uncompressed(?) Data fork     (0=None)
  068h 1    Pad bytes for encrypted Resource? (00h)
  069h 1    Pad bytes for encrypted Data?     (00h)
  06Ah 2    Unknown Data fork related     (0000h, or 0004h=Encrypted?)
  06Ch 2    Unknown Resource fork related (0000h, or 0004h=Encrypted?)
  06Eh 2    CRC16 on Header [000h..06Dh] with initial=0000h
  070h ..   Compressed Data, Resource fork (if any) (size=[05Ch])
  ...  ..   Compressed Data, Data fork     (if any) (size=[060h])
 StuffIt Methods:
  00h Uncompressed
  01h RLE90        (same as... unknown if this is like BinHex, or like ARC)
  02h ClearGap LZW (same as nCompress, 14bit, with Clear(+gap), no Stop code)
  03h Huffman      (same as PackIt "PMa4" method)
  05h LZHUF        (same as LHA "lh1" method)
  06h Fixed Huffman  Segmented. PackBits, then optional Huffman coding.
                       The set of Huffman codes is predefined, but the meaning
                       of a code can be different in each segment
  08h MW (Miller-Wegman, presumably LZMW)
  0Dh LZ+Huffman   (?)                             ;-StuffIt and StuffIt5
  0Eh Installer    (uh?)
  0Fh Arsenic      (BWT and arithmetic coding)     ;-StuffIt5 only?
  1xh Encrypted methods (same as above, plus encryption)
  20h Folder start                                 ;\StuffIt (not StuffIt5)
  21h Folder end                                   ;/
```
Common methods are 02h,03h,0Dh (rarely also 00h,01h,05h) (and 0Fh for
StuffIt5).<br/>
Folders have BOTH methods set to 20h. Uncompressed Data size is WHAT? (maybe
sum of all decompressed files in that folder?) Compressed Data size is size in
SIT file including 70h-byte folder end-marker. The Folder END marker has both
methods set to 21h. The Folder END marker has NONSENSE data size entries?<br/>
When version=01h (eg. blackfor.sit), folder/file entries start at offset 16h,
and are ordered as so:<br/>
```
  Folder start
    Child entries
    Folder end
  Folder start
    Child entries
    Folder end
```
When version=02h (eg. cabletron.sit), folder/file entries start at offset from
archive header [010h] (which can be anywhere at offset 16h, or near end of
archive), and are ordered as specified in file header entries [022h..041h].<br/>

#### StuffIt 5 (.sit) (Macintosh, Windows) (1997) (big-endian)
```
 StuffIt Archive Header:
  000h 82   ID "StuffIt (c)1997",...,"/StuffIt/",0Dh,0Ah,1Ah,00h)
  052h 1    Version (always 05h)
  053h 1    Flags (can be 00h, 10h, 80h) (bit4=what?, bit7=Encrypted)
  054h 4    Total size of archive
  058h 4    Offset to first entry in root directory (64h, plus Extra Data)
  05Ch 2    Number of entries in root directory
  05Eh 4    Same as [058h] (maybe one is 1st entry, and other is Header size)?
  062h 2    Header CRC16 on [000h..[05xh]-1] with [062h]=0000h and initial=0
  064h ..   Extra Data (see below)
  ...  ..   File/Folder entries
 Extra data can be:
  None (when [58h]=64h)                                  ;with Flags=00h
  05h,76h,35h,B9h,87h,11h             ;maybe 05h=Length? ;with Flags=80h=crypto
  0Dh,A5h,A5h,"Reserved",A5h,A5h,00h) ;maybe 0Dh=Length? ;with Flags=10h=what?
 File/Folder entries:
  000h ..   Base Header
  ...  ..   OS Header (depending on OS Type in Base Header)
  ...  ..   Resource fork (if any) (MAC only, not Windows)
  ...  ..   Data fork     (if any)
 Base Header:
  000h 4    ID (A5A5A5A5h) (or B4B4B4B4h=corrupted charset conversion maybe?)
  004h 1    OS Type (1=Mac, 3=Windows)
  005h 1    Unknown (0)
  006h 2    Base Header size (41h)  (30h+IV?+Filename+Comment)
  008h 1    Unknown (0) (maybe Flags MSB?)
  009h 1    Flags (bit3=Comment, bit6=Folder, bit5=Encrypted)
  00Ah 4    Timestamp, Creation     (Mac OS format, seconds since 1904)
  00Eh 4    Timestamp, Modification (Mac OS format, seconds since 1904)
  012h 4    Offset of previous entry          (0=None)
  016h 4    Offset of next entry              (0=None)
  01Ah 4    Offset of parent folder entry     (0=None)
  01Eh 2    Filename size (F)
  020h 2    Base Header CRC-16 on [000h..[006h]-1]
  022h (4)  Offset of first child entry in folder (FFFFFFFFh=End) ;\Folder
  026h (4)  Size of complete directory                            ; (if Flags
  02Ah (4)  Unknown                                               ; bit6=1)
  02Eh (2)  Number of child entries (excluding folder End marker) ;/
  022h (4)  Data fork uncompressed size                           ;\
  026h (4)  Data fork compressed size                             ;
  02Ah (2)  Data fork CRC-16 (0 for method 0Fh)                   ; File
  02Ch (2)  Data fork Unknown (0000h)                             ; (if Flags
  02Eh (1)  Data fork compression method (00h,0Dh,0Fh)            ; bit6=0)
  02Fh (1)  Data fork Encryption IV? size                         ;
  ...  (..) Data fork Encryption IV? data                         ;/
  ...  ..   File/Folder name ("FILENAME.EXT")
  ...  (2)  Comment size (K)                                      ;\Comment
  ...  (2)  Comment Unknown (0)                                   ; (if Flags
  ...  (..) Comment data                                          ;/bit3=1)
 OS Header for Mac (OS=1):
  000h 2       Flags2 (bit0=HasResource, bit4=same as archive header [053h] ?)
  002h 2       CRC16 on OS Header (with [002h]=0000h, initial=0)
  004h 4       Mac OS file type     ;\
  008h 4       Mac OS file creator  ; as so for Files
  00Ch 2       Mac OS Finder flags  ; (seems to contain
  00Eh 2       Mac OS Unknown       ; other stfuff/junk
  010h 4       Mac OS Unknown       ; for Folders)
  014h 4       Mac OS Unknown       ;
  018h 4       Mac OS Unknown       ;
  01Ch 4       Mac OS Unknown       ;
  020h 4       Mac OS Unknown       ;/
  024h (4)     Resource fork uncompressed size               ;\
  028h (4)     Resource fork compressed size                 ; only if
  02Ch (2)     Resource fork CRC-16 (0 for method 0Fh)       ; Flags2
  02Eh (2)     Resource fork Unknown                         ; bit0=1
  030h (1)     Resource fork compression method              ;
  031h (1)     Resource fork Encryption IV? size             ;
  ...  (..)    Resource fork Encryption IV? data             ;/
 OS Header for Windows (OS=3):
  000h 2       Flags 2 (bit4=same as archive header [053h] ?)
  002h 2       CRC16 on OS Header (with [002h]=0000h, initial=0)
  004h 4       Windows File Attribute (20h=Normal, 10h=Folder)
  008h 08h     Windows Zerofilled
  010h 4       Windows Timestamp last accessed?
  014h 4       Windows Unknown (0005xxxxh)
  018h 08h     Windows Zerofilled
```
StuffIt 5 seems to only use 00h, 0Dh and 0Fh. See "StuffItSpecs" for
descriptions of the algorithms.<br/>

#### StuffIt X (.sitx) (Macintosh, Windows) (20xx?)
```
 StuffIt Archive Header:
  000h 8    ID "StuffIt!" (reportedly "StuffIt?" also exists)
  008h ..   Unknown...
```
The StuffIt X headers are somehow compressed/compacted (there are very few 00h
bytes even when filesize entries should have zeroes in MSBs).<br/>
[https://github.com/incbee/Unarchiver/blob/master/XADMaster/XADStuffItXParser.m]


#### Compact Pro aka Compactor (.cpt) (Macintosh) (1990s) (big-endian)
MAC File Type,Creator IDs = "PACT","CPCT".<br/>
Compact Pro (originally called Compactor) was a MAC archiver competing with
StuffIt. There's also a DOS tool (ExtractorPC) for extracting .cpt files on PCs
(albeit released in .EXE.sit.hqx format, making it unlikely that PC users could
have used it).<br/>
```
 Archive header:
  000h   1   File ID           (always 01h)
  001h   1   Volume number     (01h for single-volume, Other=Unknown)
  002h   2   Random Volume ID? (...must be same in all split volume files?)
  004h   4   Offset to Footer  (from begin of file)
  008h   ..  Compressed files  (resource+data fork pairs)
  ...    ..  Footer            (directory information)
 Footer format:
  000h   4   CRC32 XOR FFFFFFFFh on following bytes
  004h   2   Number of entries in root folder (including all child entries)
  006h   1   Comment length (usually 00h=None)
  007h   N   Comment
  007h+N ..  File/Folder entries
 Folder entries, with [000h].bit=1:
  000h   1   Foldername length (N), plus bit7=Type (1=Folder)
  001h   N   Foldername ("FOLDERNAME")
  001h+N 2   Number of entries in this folder (including all child entries)
 File entries, with [000h].bit=0:
  000h   1   Filename length (N), plus bit7=Type (0=File)
  001h   N   Filename ("FILENAME.EXT")
  001h+N 1   Volume number (01h for single-volume, Other=Unknown)
  002h+N 4   Offset to compressed Resource (followed by compressed Data)
  006h+N 4   File type
  00Ah+N 4   File creator
  00Eh+N 4   Timestamp, creation     (seconds since 1904)
  012h+N 4   Timestamp, modification (seconds since 1904)
  016h+N 2   Finder flags
  018h+N 4   CRC32 XOR FFFFFFFFh on uncompressed Resource + Data forks
  01Ch+N 2   Method/Flags (see below)
  01Eh+N 4   Filesize, uncompressed, Resource fork
  022h+N 4   Filesize, uncompressed, Data fork
  026h+N 4   Filesize, compressed, Resource fork
  02Ah+N 4   Filesize, compressed, Data fork
 Method/Flags:
  0     Encryption               (0=None, 1=Encrypted, unknown how)
  1     Method for Resource fork (0=RLE8182, 1=RLE8182+LZSSHUF)
  2     Method for Data fork     (0=RLE8182, 1=RLE8182+LZSSHUF)
  3-15  Unknown/unused           (0)
 Note: RLE8182 and RLE8182+LZSSHUF are also used by Mac DiskDoubler.
```
RLE8182 Compression:<br/>
```
 This is same as RLE90, with two-byte escape code (81h,82h instead of 90h):
  81h,82h,00h       Output 81h,82h
  81h,82h,01h..03h  Output prevbyte 00h..02h times (this is not useful)
  81h,82h,04h       Output prevbyte 03h times (useful if prev=81h, next=82h)
  81h,82h,05h..FFh  Output prevbyte 04h..FEh times (this does save memory)
  81h,xxh           Output 81h, and then process xxh
  81h,padding       Output 81h, at end of file (with padding<>82h)
  xxh               Output xxh (unless it is 81h)
 Note: prevbyte is the previous output byte (ie. that stored at [dst-1]).
 If the uncompressed file ends with 81h, then the compressed file MUST contain
 a dummy padding byte (the RLE decoder in macutils sets a prefix flag upon 81h,
 but doesn't output it to dst until receiving the padding byte, which could be
 81h, or any value other than 82h).
```
LZSSHUF Compression:<br/>
```
 This uses LZSS-style flag bits (to distinguish between data and len/disp),
 combined with three Huffman trees (for data, len, disp values). The sliding
 window is 2000h bytes (8Kbytes). The format appears to be a simplified variant
 or LHA compression (but gets complicated by inventing weird corner cases).
```
DecompressLzsshuf:<br/>
```
  if uncompressed_size=0 then goto @@all_done   ;-empty (eg. for unused forks)
  [dst+0000h..1FFCh]=uninitialized              ;\
  [dst+1FFDh..1FFFh]=00h,00h,00h                ; prefill sliding window
  dst+dst+2000h                                 ;/
 @@block_lop:
  InitBitstreamMsbFirst(src)
  GetLzsshufTree(data_tree,100h)  ;tree for data=00h..FFh
  GetLzsshufTree(len_tree,40h)    ;tree for len=00h..3Fh (0,1 usually unused)
  GetLzsshufTree(disp_tree,80h)   ;tree for dispUpper7bit=00h..7Fh
  block_org=src, blocksize=0      ;block origin (after above trees)
 @@decompress_lop:
  if src>=src_end then goto @@all_done  ;<-- this may overshoot on padding bits
  if out>=out_end then goto @@all_done  ;<-- more precise; if RleOnTheFly
  if blocksize>=1FFF0h AND type=CompactPro then goto @@block_done
  if blocksize>=0FFF0h AND type=Disc Double then goto @@block_done
  if GetBits(1)=1 then
    [dst]=GetHuffCode(data_tree), dst=dst+1, blocksize=blocksize+2
  else
    len=GetHuffCode(len_tree)+0, blocksize=blocksize+3
    disp=GetHuffCode(disp_tree)*40h+GetBits(6), if disp=0000h then disp=2000h
    for i=1 to len, [dst]=[dst-disp], dst=dst+1, next i
  if RleOnTheFly then forward above byte(s) to RLE (which advances "out" ptr)
  goto @@decompress_lop
 @@block_done:
  ;the decoder does prefetch data in 16bit units, and it does always have
  ;16..31 bits prefetched, these bits are discarded at block end...
  src=src+2+((src-block_org) AND 1) ;discard 16..31 bits (till 16bit-boundary)
  goto @@block_lop                  ;start next block, with new trees
 @@all_done:
  ret
```
GetLzsshufTree(tree,max):<br/>
```
  num=GetBits(8)*2, if num>max then goto error ;number of symbols (00h and up)
  for i=0 to num-1, codesizes[i]=GetBits(4)    ;sizes (1..15 bits, or 0=unused)
  lzh_explode_tree(tree,codesizes,num)         ;alike LHA trees
  ret
```
Minor Corner cases:<br/>
```
  Disp=0 acts as Disp=2000h (don't care when using ringbuf[index AND 1FFFh])
  Len=0..1 could be definied in the len_tree (but are usually size=0bit=unused)
  Unknown if disp_tree & len_tree can be empty (when using data_tree only)?
  RLE ending with 81h,padding should only output 81h (see RLE8182 description)
```
Incomplete Trees<br/>
```
  A few .cpt files (eg. ABC's-1.09.cpt.hqx\..\Colin's ABC's\Message.h) have
  incomplete trees (like only one disp code, "0"=DispUpper7bit=00h, without
  defining any further huffman codes like "1" or "1xxx").
  This isn't much of a problem (except, one may need to remove incomplete tree
  error checking in the "lzh_explode_tree" function).
```
End of Last Block<br/>
```
  End of Last Block is usually determined by forwarding the LZSSHUF output
  directly to the RLE8182 decompressor (which does then check if uncompressed
  size is reached) (marked "RleOnTheFly" in above sample code).
  Alternately, one could decompress in separate steps (LZSSHUF to tempbuf, and
  then tempbuf to RLE8182), but that requires to deal with padding bits.
    - padding seems to be 16..31 bits (?) alike at end of blocksize
    - padding bits are (always?) zeroes, which act as flag=0=compressed
    - compressed data occupies at least flg(1),len(1),disp(1),displsbs(6)=9bits
  That can lead to decoding a few extra codes (with lengths up to 3Fh each),
  so the tempbuf must have trailing space for writing that garbage padding.
  And, those padding bits tend to translate to disp=0000h (aka disp=2000h),
  which can cause reads from the whole sliding window, so tempbuf requires
  2000h leading bytes to avoid page faults (not just the 3 initialized bytes).
```
See also:<br/>
[https://github.com/dgilman/macutils/blob/master/macunpack/cpt.c] - source code<br/>
[https://github.com/MacPaw/XADMaster/wiki/CompactProSpecs] - confused anti-specs<br/>

#### Self-Extracting Archives (SEA)
The abbreviation SEA (and extension .sea) is used for several self-extracting
MAC archives. The Resource fork contains an executable (as indicated by
Type="APPL") which contains the decompressor, and the Data fork contains the
archive.<br/>
```
  MAC File Type,Creator IDs = "APPL","aust" (StuffIt).
  MAC File Type,Creator IDs = "APPL","EXTR" (CompactPro).
  MAC File Type,Creator IDs = "APPL","DSEA" (DiskDoubler).
```
There are some oddities for .sea files found in internet:<br/>
```
  StuffIt .sea files: These are often raw StuffIt archives (apparently
    somebody had removed the MacBinary header and the resource fork with
    the decompressor).
  CompactPro .sea files: These are often stored as MacBinary without 80h-byte
    padding appended to the Data and Resource forks.
    That applies to "Santa.sea" but other such files have OTHER corruptions,
    which may include wrong Size and/or garbage in reserved MacBinary fields?
```
Note: Not to be confused with ARC archives from System Enhancement Associates
(SEA).<br/>

#### Mac OS Data forks
The Data fork contains the "normal data" part of the file (eg. anything like
.TXT .DOC .GIF .JPG .WAV .ZIP .LZH .SIT .PIT .CPT etc).<br/>

#### Mac OS Resource forks
The Resource fork can contain executable code resources (similar to .EXE files;
with File Type="APPL"), and various other resources (fonts, icons, text strings
for dialog boxes, etc). Those resources are stored in a filesystem-style
archive and can be accessed with IDs and/or name strings.<br/>
```
 Resource fork Header:
  000h 4    Offset to Resource Data section (from start of file) (100h)
  004h 4    Offset to Resource Map section  (from start of file) (100h+DataSiz)
  008h 4    Size of Resource Data section (can be 0=None)
  00Ch 4    Size of Resource Map section
  010h F0h  Unknown (can contain filename/type.. MAYBE just garbage padding?)
  100h ..   Resource Data section, contains Data Record(s)
  ...  ..   Resource Map section
 Data Record(s) in Resource Data section (usually at offset 100h and up):
  000h 4    Size of Data for this record
  004h ..   Data for this record
 Resource Map section:
  000h 4    Offset to Resource Data section (from start of file) ;\
  004h 4    Offset to Resource Map section  (from start of file) ; same as in
  008h 4    Size of Resource Data section                        ; header
  00Ch 4    Size of Resource Map section                         ;/
  010h 4    Zero (internally used by Resource Manager, nextResourceMap)
  014h 2    Zero (internally used by Resource Manager, fileRef)
  016h 2    Map Attributes
              0-4  Zero (reserved)
              5    Zero (internally used by Resource Manager, changed)
              6    Zero (internally used by Resource Manager, need compression)
              7    Resource map is read-only
              8-15 Zero (reserved)
  018h 2    Offset to Type List (from start of resource map) (usually 1Ch ?)
  01Ah 2    Offset to Name List (from start of resource map)
  ...  ..   Type List
  ...  ..   Resource List (with one or more entry for each entry in Type List)
  ...  ..   Name List (each name consists of 8bit NameLength, plus name string)
 Type List follows the header and contains an array of resource type records.
  000h 2    Number of Type Records, minus one (FFFFh=None, 0000h=One, etc.)
  002h N*8  Type Records
 Type Record format:
  000h 4    Resource Type (four-character constant)
  004h 2    Number of Resource List entries, minus one (0000h=One, etc.)
  006h 2    Offset to first Resource List entry (from start of Type List)
 Resource List entries:
  000h 2    Resource ID (C000h..FFFFh=Special/Owned)
  002h 2    Offset to Resource Name (from start of Name List) (FFFFh=None)
  004h 1    Attributes
              0    Resource data is compressed             (0=No, 1=Compressed)
              1    Zero (internally used by Resource Manager, changed)
              2    Load Resource as soon as file is opened (0=No, 1=Preload)
              3    Resource is read-only                   (0=No, 1=Protected)
              4    Resource may not be moved in memory     (0=No, 1=Locked)
              5    Resource may be paged out of memory     (0=No, 1=Purgeable)
              6    Load Resource to        (0=Application heap, 1=System Heap)
              7    Zero (reserved)
  005h 3    Offset to Resource Data (from start of Resource Data section)
  008h 4    Zero (internally used by Resource Manager, resourcePtr)
 Note: Some (or all?) 16bit offsets are reportedly signed (max 32Kbyte), the
 24bit offsets are reportedly unsigned (max 16Mbyte).
```
Compressed Resources (when Attributes.bit0=1)<br/>
```
 Compressed resource have a standarized header, the decompression function(s)
 are supposed to be stored in separate "dmcp" resource (unknown if the OS is
 also providing standard decompression functions).
  000h 4      ID (always A89F6572h for compressed resource)
  004h 2      Always 0012h (maybe compression header size)
  006h 1      Type (08h=Type8, 09h=Type9)
  007h 1      Always 01h
  008h 4      Uncompressed resource size
  00Ch 1      For Type8: workingBufferFractionalSize               ;\
  00Dh 1      For Type8: expansionBufferSize                       ; Type8
  00Eh 2      For Type8: dcmpID (ID in "dmcp" decompress resource) ;
  010h 2      For Type8: Zero (reserved?)                          ;/
  00Ch 2      For Type9: dcmpID (ID in "dmcp" decompress resource) ;\Type9
  00Eh 4      For Type9: decompressor_specific_parameters_with_io  ;/
  012h ..     Compressed Resource Data
 http://formats.kaitai.io/compressed_resource/
```
Owned Resources (with Resource ID=C000h..FFFFh):<br/>
```
 https://github.com/kreativekorp/ksfl/wiki/Macintosh-Resource-File-Format
```
The upper 5bit (mask F800h) indicate the resource type of the owner, the middle
6bit (mask 07E0h) indicate the resource id of the owner, and the lower 5bit
(mask 001Fh) indicate the "sub-id" of the owned resource.<br/>
```
  ID MSBs    Owner Type  Notes
  C000h      DRVR        driver or desk accessory
  C800h      WDEF        window definition: code to draw windows
  D000h      MDEF        menu definition: code to draw menus
  D800h      CDEF        control definition: code to draw UI widgets
  E000h      PDEF        printer driver
  E800h      PACK        utility code package/library used by the Mac OS
  F000h      cdev        control panel; owner id is set to 1
  F800h      reserved    reserved for future use
```
The Mac OS Resource Manager used this scheme to ensure that certain types of
programs, themselves stored in resources, could find the other resources they
needed even if the resources had to be renumbered to avoid conflicts. Utilities
such as Font/DA Mover that were used to install and remove these programs used
this scheme to ensure that all associated resources were installed or removed
as well, and renumber the resources if necessary to avoid conflicts.<br/>



##   CDROM File XYZ and Dummy/Null Files
#### Dummy/Null Files
Most PSX discs have huge zerofilled dummy files with about 32Mbytes, using
filenames like DUMMY, NUL, NULL, or ZNULL, this is probably done to tweak the
disc to have valid sector numbers at the end of disc (to help the drive head to
know which sector it is on).<br/>
Of course, Sony could as well pad the discs with longer Lead-Out areas, but the
dummy files may have been needed during development with CDRs (though burning
such large files doesn't exactly speed up development).<br/>
There are different ways to make sure that the file is at end of the disc:<br/>
- Some CDROM burning tools may allow to specify which file is where<br/>
- Some games have the file alphabetically sorted as last file in last folder<br/>
- Some games have the file declared as audio track<br/>
- Some games (additionally) have large zeropadding at end of their archive file<br/>

#### XYZ Files
To reduce seek times, it can make sense to have the boot files & small
files at the begin of the disc.<br/>
Some games seem to use alphabetically sorted file/folder names to tweak Movies
and XA-audio to be located at the end of disc (eg. using ZMOVIE as folder
name).<br/>



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

#### Missing Sectors & Sector Size
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

#### Entry & Points & Sessions
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
[CDROM File Compression ZIP/GZIP/ZLIB (Inflate/Deflate)](cdromfileformats.md#cdrom-file-compression-zipgzipzlib-inflatedeflate)<br/>

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
[CDROM File Compression ZIP/GZIP/ZLIB (Inflate/Deflate)](cdromfileformats.md#cdrom-file-compression-zipgzipzlib-inflatedeflate)<br/>
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
 ________________________________ CHD Metadata ________________________________
```

#### V3/V4/V5 Metadata
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

#### V3/V4/V5 Metadata in ASCII format
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

#### CHCD Metadata (94Ch bytes, plus 10h-byte metadata header)
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

```
 __________________________________ CHD Maps __________________________________
```

The Maps contain info (offset, size, compression method, etc.) for the separate
compression blocks.<br/>

#### V1/V2 map format (64bit entries with 44bit+20bit):
```
  44bit     Offset to compressed data
  20bit     Size of compressed data (or uncompressed data when size=hunksize)
```
Unknown if offset is in upper or lower 44bit.<br/>

#### V3/V4 map entries (per hunk):
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

#### V5 Map Formats
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

#### Uncompressed V5 Map loading (when [filehdr+10h]=00000000h)
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

#### Compressed V5 Map loading (when [filehdr+10h]\<\>00000000h)
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
codes with size 1, 2, 2. The traditional standard assignment would be 0, 10,
11. But CHD is instead assigning them as 00, 01, 1.<br/>

```
 ______________________________ CHD Compression _______________________________
```

#### Compression V1-V4 format 0 (uncompressed)
#### Compression V5 0,0,0,0 (uncompressed)
```
  000h ..   Uncompressed data
```
Uncompressed format can be selected in CHD Map entries (per hunk), and in CHD
file header (per whole file).<br/>

#### Compression V1-V4 format 1 (zlib) (Generic Deflate)
#### Compression V1-V4 format 2 (zlib+) (Generic Deflate)
#### Compression V5 "zlib" (Generic Deflate)
```
  000h ..   Deflate-compressed data
```

#### Compression V5 "lzma" (Generic LZMA)
```
  000h ..   LZMA-compressed data (with lc=3, lp=0, pb=2) (without EOS end code)
```

#### Compression V5 "flac" (Generic FLAC)
```
  000h 1    Output format for 16bit samples ("L"=Little-endian, "B"=Big-endian)
  001h ..   FLAC-compressed data frame(s)
```

#### Compression V5 "huff" (Generic Huffman)
```
  000h ..   Huffman-compressed data (small tree, large tree, plus data)
```

#### Compression V5 "cdzl" (CDROM Deflate+Delate)
```
  000h ..   ECC Flags, (SectorsPerHunk+7)/8 bytes ;little-endian, bit0=1st flag
  ...  2/3  Size of compressed Data part (SIZ)    ;big-endian, 16bit or 24bit
  ...  SIZ  Deflate compressed Data part          ;uncompressed=930h*N bytes
  ...  ..   Deflate compressed Subchannel part    ;uncompressed=60h*N bytes
```

#### Compression V5 "cdlz" (CDROM LZMA+Deflate)
```
  000h ..   ECC Flags, (SectorsPerHunk+7)/8 bytes ;little-endian, bit0=1st flag
  ...  2/3  Size of compressed Data part (SIZ)    ;big-endian, 16bit or 24bit
  ...  SIZ  LZMA compressed Data part             ;uncompressed=930h*N bytes
  ...  ..   Deflate compressed Subchannel part    ;uncompressed=60h*N bytes
```

#### Compression V5 "cdfl" (CDROM FLAC+Deflate)
```
  000h ..   FLAC-compressed Data Frame(s)         ;uncompressed=930h*N bytes
  ...  ..   Deflate compressed Subchannel part    ;uncompressed=60h*N bytes
```

#### Compression V5 "avhu" (A/V mixup with Huffman and FLAC or so)
This isn't used on CDROMs and details are unknown/untested. It does reportedly
exist in different versions, and does combine different compression methods for
audio and video data.<br/>

#### Compression V4 format 3 (AV)
Unknown, maybe same/similar as "avhu".<br/>

#### Compression V3-V4 secondary compression method (FLAC CDDA)
CHD source code claims that V3-V4 maps support "FLAC CDDA", but it doesn't
actually seem to support that (audio discs compressed with chdman v0.145 are
merely using Deflate).<br/>

```
 _________________________ CHD Compression for CDROMs _________________________
```

#### CDROM "cdzl" and "cdlz"
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

#### CDROM "cdfl"
There are no ECC flags (since Audio sectors don't have ECC).<br/>
There is no size entry (one must decompress the whole FLAC part to find the
begin of the Subchannel part).<br/>
The FLAC output is always stored in BIG-ENDIAN format (because CHD likes to use
big-endian for audio sectors, unlike formats like CUE/BIN).<br/>

#### CDROM Subchannel data
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

```
 ___________________________ CHD CDROM Sector Sizes ___________________________
```

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

```
 __________________________ CHD Compression Methods ___________________________
```

#### Deflate
This is raw Deflate (despite of being called "zlib" in chd headers and source
code; there aren't any ZLIB headers nor Adler checksums). V1-V4 does
distinguish between "zlib" and "zlib+" (both are using normal Deflate) (V3/V4
are always using "zlib+") (the "+" does probably just mean that file was
compressed with improved compression ratio).<br/>
[CDROM File Compression ZIP/GZIP/ZLIB (Inflate/Deflate)](cdromfileformats.md#cdrom-file-compression-zipgzipzlib-inflatedeflate)<br/>

#### LZMA
This contains a raw LZMA bitstream (without .lzma or .lz headers). The LZMA
bitstream starts with 8 ignored bits, if Normalization occurs after last
compression code, then it will also end with 8 ignored bits (those ignored bits
aren't CHD-specific, they do also occur in other LZMA-based formats).<br/>
[CDROM File Compression LZMA](cdromfileformats.md#cdrom-file-compression-lzma)<br/>

#### FLAC
The data consists of raw FLAC Frames (without FLAC file header or FLAC metadata
blocks), the format is always signed 16bit/stereo (NumChannels=2
SampleDepth=16), the sample rate is don't care for compression purposes (the
FLAC Frame headers have it set to 09h=44100Hz).<br/>
Each FLAC Frame starts with a 14bit Sync mark (3FFEh), and ends with 16bit CRC.
There are usually several FLAC frames per CHD hunk (one must decompress all
FLAC frames, until reaching the decompressed hunk size).<br/>
Each FLAC Frame contains Left samples, followed by Right samples. After
decompression, CHD does store them in interleaved form (L,R,L,R,etc.)<br/>
[CDROM File Compression FLAC audio](cdromfileformats.md#cdrom-file-compression-flac-audio)<br/>

#### Huffman
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

```
 _________________________________ CHD Notes __________________________________
```

#### Track/Hunk Padding and Missing Index0 sectors
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

#### Parent references
Parent files are only used for writeable media like harddisks. The idea is to
store the original installation and operating system in a readonly Parent file,
and to store changes that file in a writeable Child file.<br/>
Unknown what determines which parent belongs to which child, and if parents can
be nested with other grandparents. Anyways, Parents aren't needed for CDROMs
(except, one could theoretically store CDROM patches in child files).<br/>

#### Self references
This can be used to reference to another identical hunk in the same file (eg.
zerofilled sectors or other duplicated data). There are some restrictions for
CDROMs: Data sector headers contain increasing sector numbers, so there won't
be any identical sectors. However, Audio sectors can be identical (unless they
are stored with subchannel info, which does also contain increasing sector
numbers).<br/>

#### Mini
Mini is only used in V3/V4 maps. It does apparently store the "data" directly
in the 8-byte Map offset field.<br/>
```
  XXX Unknown what kind of "data" that is
  (probably "normal compressed data", that happens to be 8 bytes or smaller).
```
Mini isn't used in V5 because the compressed V5 map doesn't contain any offset
fields (and things like zerofilled sectors could be as well encoded as Self
instead of Mini).<br/>

#### CHDMAN versions
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

#### References
CHD source code (see files cdrom.\*, chd\*.\*, etc):<br/>
```
  https://github.com/mamedev/mame/tree/master/src/lib/util
```
CHDMAN commandline tool for generating chd files:<br/>
```
  https://github.com/mamedev/mame/blob/master/src/tools/chdman.cpp
```
CHD decompression clone with useful comments:<br/>
```
  https://github.com/SnowflakePowered/chd-rs/tree/master/chd-rs/src
```
CHD format reverse-engineering thread:<br/>
```
  http://www.psxdev.net/forum/viewtopic.php?f=70&t=3980
```



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
```
  http://www.ezbsystems.com/isz/iszspec.txt
```
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
