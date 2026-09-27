#   Compression

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
[CDROM File Compression LZSS (Moto Racer 1 and 2)](#cdrom-file-compression-lzss-moto-racer-1-and-2)<br/>
[CDROM File Compression LZSS (Dino Crisis 1 and 2)](#cdrom-file-compression-lzss-dino-crisis-1-and-2)<br/>
[CDROM File Compression LZSS (Serial Experiments Lain)](#cdrom-file-compression-lzss-serial-experiments-lain)<br/>
[CDROM File Compression ZOO/LZSS](#cdrom-file-compression-zoolzss)<br/>
[CDROM File Compression Ulz/ULZ (Namco)](#cdrom-file-compression-ulzulz-namco)<br/>
[CDROM File Compression SLZ/01Z (chunk-based compressed archive)](#cdrom-file-compression-slz01z-chunk-based-compressed-archive)<br/>
[CDROM File Compression LZ5 and LZ5-variants](#cdrom-file-compression-lz5-and-lz5-variants)<br/>
[CDROM File Compression PCK (Destruction Derby Raw)](#cdrom-file-compression-pck-destruction-derby-raw)<br/>
[CDROM File Compression GT-ZIP (Gran Turismo 1 and 2)](#cdrom-file-compression-gt-zip-gran-turismo-1-and-2)<br/>
[CDROM File Compression GT20 and PreGT20](#cdrom-file-compression-gt20-and-pregt20)<br/>
[CDROM File Compression HornedLZ](#cdrom-file-compression-hornedlz)<br/>
[CDROM File Compression LZS (Gundam Battle Assault 2)](#cdrom-file-compression-lzs-gundam-battle-assault-2)<br/>
[CDROM File Compression BZZ](#cdrom-file-compression-bzz)<br/>
[CDROM File Compression RESOURCE (Star Wars Rebel Assault 2)](#cdrom-file-compression-resource-star-wars-rebel-assault-2)<br/>
[CDROM File Compression TIM-RLE4/RLE8](#cdrom-file-compression-tim-rle4rle8)<br/>
[CDROM File Compression RLE_16](#cdrom-file-compression-rle_16)<br/>
[CDROM File Compression PIM/PRS (Legend of Mana)](#cdrom-file-compression-pimprs-legend-of-mana)<br/>
[CDROM File Compression BPE (Byte Pair Encoding)](#cdrom-file-compression-bpe-byte-pair-encoding)<br/>
[CDROM File Compression RNC (Rob Northen Compression)](#cdrom-file-compression-rnc-rob-northen-compression)<br/>
[CDROM File Compression Darkworks](#cdrom-file-compression-darkworks)<br/>
[CDROM File Compression Blues](#cdrom-file-compression-blues)<br/>
[CDROM File Compression Z (Running Wild)](#cdrom-file-compression-z-running-wild)<br/>
[CDROM File Compression ZAL (Z-Axis)](#cdrom-file-compression-zal-z-axis)<br/>
[CDROM File Compression EA Methods](#cdrom-file-compression-ea-methods)<br/>
[CDROM File Compression ZIP/GZIP/ZLIB (Inflate/Deflate)](#cdrom-file-compression-zipgzipzlib-inflatedeflate)<br/>
[CDROM File Compression LArc/LHarc/LHA (LZS/LZH)](#cdrom-file-compression-larclharclha-lzslzh)<br/>
[CDROM File Compression UPX](#cdrom-file-compression-upx)<br/>
[CDROM File Compression LZMA](#cdrom-file-compression-lzma)<br/>
[CDROM File Compression FLAC audio](#cdrom-file-compression-flac-audio)<br/>
Some other archvies that aren't used by any PSX games, but, anyways...<br/>
[CDROM File Compression ARJ](#cdrom-file-compression-arj)<br/>
[CDROM File Compression ARC](#cdrom-file-compression-arc)<br/>
[CDROM File Compression RAR](#cdrom-file-compression-rar)<br/>
[CDROM File Compression ZOO](#cdrom-file-compression-zoo)<br/>
[CDROM File Compression nCompress.Z](#cdrom-file-compression-ncompressz)<br/>
[CDROM File Compression Octal Oddities (TAR, CPIO, RPM)](#cdrom-file-compression-octal-oddities-tar-cpio-rpm)<br/>
[CDROM File Compression MacBinary, BinHex, PackIt, StuffIt, Compact Pro](#cdrom-file-compression-macbinary-binhex-packit-stuffit-compact-pro)<br/>

#### Compressed Archives
Some Archives have "built-in" compression.<br/>
[CDROM File Archive WAD (Doom)](archives.md#cdrom-file-archive-wad-doom)<br/>
[CDROM File Archive BIGFILE.DAT (Gex - Enter the Gecko)](archives.md#cdrom-file-archive-bigfiledat-gex-enter-the-gecko)<br/>



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
The compressed file &amp; archive header don't contain any info on the
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
#### Jarret &amp; LaBonte Stock Car Racing (MagDemo38: WTC\\*.ZOO)
```
  0000h 4     Decompressed Size                          ;\1st sector
  0004h 7FCh  Garbage                                    ;/
  0800h 4     Decompressed Size (same as above)          ;\2nd sector
  0804h 7FCh  LZSS compressed data, part 1               ;/
  1000h 800h  LZSS compressed data, part 2               ;-3rd sector
  1800h 800h  LZSS compressed data, part 3               ;-4th sector
  ...   ..    etc.
```
Note: The file format &amp; compression method is unrelated to ZOO archives (to
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
The compressed &amp; decompressed size is stored in the BIZ archive.<br/>
Note: Power Spike 20h-filled initial BIZ ringbuf is required for sky pixels in:<br/>
```
  MagDemo43: POWER\GAME.IDX\PERSOS\PSX\CUSTOM\\TEXTURE\NFIELD.BIZ\LPORJ.PSI
```

#### PSX Army Men Air Attack 2 (MagDemo40: AMAA2\\*.PCK\\*.PAK)
SCRATCH compression is used in PAK archives (which are nested in PCK archive).
The compressed &amp; decompressed size is stored in the PAK archive.<br/>
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
Used by Rollcage (MagDemo19: ROLLCAGE\SPEED.IMG\\\*)<br/>
Used by Rollcage Stage II (MagDemo31: ROLLCAGE\SPEED.IDX\\\*)<br/>
Used by Sydney 2000 (MagDemo37: OLY2000\DEMO.IDX\\\* and OLY2000\GTO\\\*.GTO)<br/>
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
<https://zenhax.com/viewtopic.php?t=13175> (specs)<br/>
See also: <http://wiki.xentax.com/index.php/GT20_Archive> (blurp)<br/>

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
[CDROM File Archive Croc 1 (DIR, WAD, etc.)](archives.md#cdrom-file-archive-croc-1-dir-wad-etc)<br/>
[CDROM File Archive Croc 2 (DIR, WAD, etc.)](archives.md#cdrom-file-archive-croc-2-dir-wad-etc)<br/>



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
[CDROM File Compression EA Methods](#cdrom-file-compression-ea-methods)<br/>



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
<http://aminet.net/package/util/pack/RNC_ProPack> - official tool &amp; source code<br/>
<https://segaretro.org/Rob_Northen_compression> - description (contains bugs)<br/>


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
  Asterix and the Great Rescue
  Asterix and the Power of the Gods
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
[CDROM File Compression EA Methods (LZSS RefPack)](#cdrom-file-compression-ea-methods-lzss-refpack)<br/>
[CDROM File Compression EA Methods (Huffman)](#cdrom-file-compression-ea-methods-huffman)<br/>
[CDROM File Compression EA Methods (BPE)](#cdrom-file-compression-ea-methods-bpe)<br/>
[CDROM File Compression EA Methods (RLE)](#cdrom-file-compression-ea-methods-rle)<br/>

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
<http://wiki.niotso.org/RefPack> - LZ method<br/>



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

[Inflate - Core Functions](#inflate-core-functions)<br/>
[Inflate - Initialization &amp; Tree Creation](#inflate-initialization-tree-creation)<br/>
[Inflate - Headers and Checksums](#inflate-headers-and-checksums)<br/>

#### PSX Disk Images
In PSX cdrom-images, ZLIB is used by the .CDZ cdrom-image format:<br/>
[CDROM Disk Image/Containers CDZ](diskimages.md#cdrom-disk-imagecontainers-cdz)<br/>
In PSX cdrom-images, Inflate is used by .PBP and .CHD cdrom-image formats:<br/>
[CDROM Disk Images PBP (Sony)](diskimages.md#cdrom-disk-images-pbp-sony)<br/>
[CDROM Disk Images CHD (MAME)](diskimages.md#cdrom-disk-images-chd-mame)<br/>

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



##   Inflate - Initialization &amp; Tree Creation
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
[CDROM File Compression LZ5 and LZ5-variants](#cdrom-file-compression-lz5-and-lz5-variants)<br/>

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
<http://fileformats.archiveteam.org/wiki/LHA>



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
<http://www.nongnu.org/lzip/manual/lzip_manual.html#File-format>

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
[CDROM File Compression XZ](#cdrom-file-compression-xz)<br/>

#### .7z files (7-Zip archives)
```
  000h 6   ID ("7z",BCh,AFh,27h,1Ch)
  ...  ..  ..
```
The 7z format defines many compression methods. The ones normally used are
LZMA2 (default for 7-Zip 9.30 alpha +), LZMA (default for 7-Zip prior to 9.30
alpha), PPMd, and bzip2.<br/>
<http://fileformats.archiveteam.org/wiki/7z>


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

<https://github.com/ilyakurdyukov/micro-lzmadec>

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

<https://tukaani.org/xz/format.html>

The BCJ filters aren't documented in XZ specs, but are defined in XZ source
code, see src\liblzma\simple\\*.c). There's also this mail thread about
semi-official ARM64 filters:<br/>

<https://www.mail-archive.com/xz-devel@tukaani.org/msg00537.html>



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

<https://xiph.org/flac/format.html>

Source code for a compact FLAC decoder can be found here:<br/>

<https://www.nayuki.io/page/simple-flac-implementation>



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

#### ARJ Glossary &amp; Oddities
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
<http://fileformats.archiveteam.org/wiki/Squeeze>


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
[CDROM File Compression nCompress.Z](#cdrom-file-compression-ncompressz)<br/>
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
<http://fileformats.archiveteam.org/wiki/ARC_(compression_format)>

<https://www.fileformat.info/format/arc/corion.htm>

<http://cd.textfiles.com/pcmedic/utils/compress/arc520s.zip> - source code<br/>

<https://github.com/ani6al/arc> - source code, upgraded with method 9 and 4<br/>

<https://entropymine.wordpress.com/2021/05/11/arcs-trimmed-compression-scheme/><br/>

<http://www.textfiles.com/programming/FORMATS/arc-lbr.pro> - benchmarks<br/>



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
one archive to another (without needing to decompress &amp; recompress the
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
See also: <https://www.gnu.org/software/tar/manual/html_node/Standard.html>


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
<https://www.systutorials.com/docs/linux/man/5-cpio/>


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
CRC16-XMODEM: <http://www.sunshine2k.de/coding/javascript/crc/crc_js.html>


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
<http://www.network172.com/early-mac-software/packit-source-code/> - official<br/>

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
<https://github.com/incbee/Unarchiver/blob/master/XADMaster/XADStuffItXParser.m>


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
<https://github.com/dgilman/macutils/blob/master/macunpack/cpt.c> - source code<br/>
<https://github.com/MacPaw/XADMaster/wiki/CompactProSpecs> - confused anti-specs<br/>

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
```
<http://formats.kaitai.io/compressed_resource/>

Owned Resources (with Resource ID=C000h..FFFFh):<br/>

<https://github.com/kreativekorp/ksfl/wiki/Macintosh-Resource-File-Format>

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
To reduce seek times, it can make sense to have the boot files &amp; small
files at the begin of the disc.<br/>
Some games seem to use alphabetically sorted file/folder names to tweak Movies
and XA-audio to be located at the end of disc (eg. using ZMOVIE as folder
name).<br/>
