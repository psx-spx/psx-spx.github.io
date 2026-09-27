#   Executables and Debug Files

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

#### Symbol Chunks

##### Chunk 01h: Symbol (Immediate, eg. memsize, or membase)
##### Chunk 02h: Symbol (Function Address for Internal &amp; External Functions)
##### Chunk 05h: Symbol (?)
##### Chunk 06h: Symbol (?)
```
  00h 4   Address/Value
  04h 1   Chunk ID (01h/02h/05h/06h)
  05h 1   Symbol Length (LEN)
  06h LEN Symbol (eg. "VSync")
```

#### Source Code Line Chunks

##### Chunk 80h: Source Code Line Numbers: Address for 1 Line
```
  00h 4   Address (for 1 line, starting at current line)
  04h 1   Chunk ID (80h)
```

##### Chunk 82h: Source Code Line Numbers: Address for N Lines (8bit)
```
  00h 4   Address (for N lines, starting at current line)
  04h 1   Chunk ID (82h)
  05h 1   Number of Lines (00h=None, or 02h and up?)
```

##### Chunk 84h: Source Code Line Numbers: Address for NN Lines (16bit)
```
  00h 4   Address (for N lines, starting at current line)
  04h 1   Chunk ID (84h)
  05h 2   Number of Lines (?)
```

##### Chunk 86h: Source Code Line Numbers: Address for Line NNN (32bit?)
```
  00h 4   Address (for 1 line, starting at newly assigned current line)
  04h 1   Chunk ID (84h)
  05h 4   Absolute Line Number (rather than number of lines) (?)
```

##### Chunk 88h: Source Code Line Numbers: Start with Filename
```
  00h 4   Address (start address)
  04h 1   Chunk ID (88h=Filename)
  05h 4   First Line Number (after comments/definitions) (32bit?)
  09h 1   Filename Length (LEN)
  0Ah LEN Filename (eg. "C:\path\main.c")
```

##### Chunk 8Ah: Source Code Line Numbers: End of Source Code
```
  00h 4   Address (end address)
  04h 1   Chunk ID (8Ah)
```

#### Internal Function Chunks

##### Chunk 8Ch: Internal Function: Start with Filename
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

##### Chunk 8Eh: Internal Function: End of Function (end of chunk 8Ch)
```
  00h 4   Address
  04h 1   Chunk ID (8Eh)
  05h 4   Line Number                 <-- line number (32bit?)
```

##### Chunk 90h: Internal Function:Whatever90h... first instruction in main func?
##### Chunk 92h: Internal Function:Whatever92h... last instruction in main func?
Maybe line numbers? Or end of definitions for incoming parameters?<br/>
```
  00h 4   Address
  04h 1   Chunk ID (90h/92h)
  05h 4   Whatever (1Fh,00h,00h,00h)  <-- line number relative to main.start?
```

#### Class/Type Chunks

##### Chunk 94h: Type/Symbol (Simple Types?)
```
  00h 4   Offset (when used within a structure, or stack-N, or otherwise zero)
  04h 1   Chunk ID (94h)
  05h 2   Class (000Dh=Type.alias, 000Ah=Address, 0001h=Stack, 0002h=Addr)
  07h 2   Type (XX = 8bit,16bit,signed,etc.?)
  09h 4   Zero, or Size in Bytes (for "memblocks")
  0xh 1   Symbol Name Length (LEN)
  0xh LEN Symbol Name (eg. "size_t")
```

##### Chunk 96h: Type/Symbol (Complex Structures/Arrays?)
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

#### Class/Type Values

##### Class definition (in chunk 94h) (and somewhat same/similar in chunk 96h)
(looks same/similar as C\_xxx class values in COFF files!)<br/>
```
  0001h = Local variable              (with Offset = negative stack offset)
  0002h = Global variable or Function (with Offset = address)
  0008h = Item in Structure           (with Offser = offset within struct)
  0009h = Incoming Function param     (with Offset = index; 0,4,8,etc.)
  000Ah = Type address / struc start? (with Offset = zero)
  000Dh = Type alias                  (with Offset = zero)
```

##### Type definition (in chunk 94h/96h)
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

#### .MAP File

##### PsyQ .MAP File
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
