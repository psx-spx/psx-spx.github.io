#   Textures, 2D and 3D Graphics

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
data contains different types, eg. both 4bpp &amp; 8bpp textures).<br/>
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
  000h 1  File ID  ( 11h=CLT) (although Sony's doc says 12h)
  001h 1  Version  ( 00h)
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

#### Compressed TIMs
Ape Escape (Sony 1999) is using a customized TIM format with 4bpp compression:<br/>
[CDROM File Compression TIM-RLE4/RLE8](compression.md#cdrom-file-compression-tim-rle4rle8)<br/>
Other than that, TIMs can be compressed via generic compression functions (like
LZSS, GZIP), or via bitmap dedicated compression formats (like BS, JPG, GIF).<br/>

#### Malformed Files

##### Malformed TIMs in BIGFILE.DAT
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
Also, destination yloc should be 0..1FFh, but PSX "Lemmings &amp; Oh No! More
Lemmings" (FILES\GFX\\*.TIM) has yloc=200h (that game also has vandalized .BMP
headers with 2-byte alignment padding after ID "BM", whilst pretending that
those extra bytes aren't there in data offset and total size entries).<br/>

##### Oversized TIMs
```
  Used by Pong (MagDemo24: LES02020\*\*.TIM)
```
Has 200x200h pix, but section size (and filesize) are +2 bigger than that:<br/>
```
  10 00 00 00 02 00 00 00 0E 00 08 00 C0 01 00 00 00 02 00 02  ;Pong *.TIM
  10 00 00 00 02 00 00 00 0E 00 07 00 00 02 00 00 C0 01 00 02  ;Pong WORLD.TIM
  10 00 00 00 02 00 00 00 0E 80 03 00 00 02 00 01 C0 01 00 01  ;Pong ZONE*.TIM
```

##### Miscomputed Section Size
NBA Basketball 2000 (MagDemo28: FOXBB\TIM\\*.TIM) has TIMs with section size
"0Ch+Xsiz\*Ysiz" instead of "0Ch+Xsiz\*2\*Ysiz".<br/>

##### NonTIMs in Bloody Roar 1 and 2
```
  Bloody Roar 1 (CMN\INIT.DAT\000Eh)
  Bloody Roar 2 (CMN\SE00.DAT, CMD\SEL00.DAT\0030h and CMN\VS\VS.DAT\0000h)
```
This looks somehow TIM-inspired, but has ID=13h.<br/>
```
  13 00 00 00 02 00 00 00 0C 20 00 00 00 00 F8 01 00 01 10 00  ;Bloody Roar 1
  13 00 00 00 02 00 00 00 0C 20 00 00 00 00 00 00 00 01 10 00  ;Bloody Roar 2
```

##### Other uncommon/malformed TIM variants
And, Heart of Darkness has a TIM with Size entry set to Xsiz\*2\*Ysiz+0Eh
(instead of +0Ch) (that malformed TIM is found inside of the RNC compressed
IMAGES\US.TIM file).<br/>
Also, NFL Gameday '99 (MagDemo17: GAMEDAY\PHOTOS.FIL) contains a TIM cropped to
800h-byte size (containing only the upper quarter of the photo).<br/>
Also, not directly malformed, but uncommon: Final Fantasy IX contains 14h-byte
0x0 pixel TIMs (eg. FF9.IMG\dir04\file0046\1B-0000\04-0001).<br/>
Klonoa (MagDemo08: KLONOA\FILE.IDX\3\2\0..1) has 0x0pix TIM (plus palette).<br/>

##### Malformed CLTs
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
[CDROM File Video Texture/Bitmap (TGA)](#cdrom-file-video-texturebitmap-tga)<br/>
[CDROM File Video Texture/Bitmap (PCX)](#cdrom-file-video-texturebitmap-pcx)<br/>

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

#### Lemmings &amp; Oh No! More Lemmings (FILES\GFX\\*.BOB, FILES\SMLMAPS\\*.BOB)
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
[CDROM File Compression RLE_16](compression.md#cdrom-file-compression-rle_16)<br/>
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
[CDROM File Compression EA Methods](compression.md#cdrom-file-compression-ea-methods)<br/>
Variants of the .PSH format are also used on PC, PS2, PSP, XBOX (with other
Chunk Types for other texture/palette formats, and for optional extra data).
For details, see: <http://wiki.xentax.com/index.php/EA_SSH_FSH_Image>


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
versions, revisions, corner cases, incomplete &amp; bugged specifications, and
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
(supposedly via [10h].bit7-4, but most older &amp; newer 2-color files have
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
<https://www.fileformat.info/format/pcx/egff.htm>




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

#### PMD - High-Speed Modeling Data
This is about same as TMD, with less features, intended to work faster.<br/>
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
