#   Memory Card Data Format
#### Data Size
```
  Total Memory 128KB = 131072 bytes = 20000h bytes
  1 Block 8KB = 8192 bytes = 2000h bytes
  1 Frame 128 bytes = 80h bytes
```
The memory is split into 16 blocks (of 8 Kbytes each), and each block is split
into 64 sectors (of 128 bytes each). The first block is used as Directory, the
remaining 15 blocks are containing Files, each file can occupy one or more
blocks.<br/>

#### Header Frame (Block 0, Frame 0)
```
  00h-01h Memory Card ID (ASCII "MC")
  02h-7Eh Unused (zero)
  7Fh     Checksum (all above bytes XORed with each other) (usually 0Eh)
```

#### Directory Frames (Block 0, Frame 1..15)
```
  00h-03h Block Allocation State
            00000051h - In use ;first-or-only block of a file
            00000052h - In use ;middle block of a file (if 3 or more blocks)
            00000053h - In use ;last block of a file   (if 2 or more blocks)
            000000A0h - Free   ;freshly formatted
            000000A1h - Free   ;deleted (first-or-only block of file)
            000000A2h - Free   ;deleted (middle block of file)
            000000A3h - Free   ;deleted (last block of file)
  04h-07h Filesize in bytes (2000h..1E000h; in multiples of 8Kbytes)
  08h-09h Pointer to the NEXT block number (minus 1) used by the file
            (ie. 0..14 for Block Number 1..15) (or FFFFh if last-or-only block)
  0Ah-1Eh Filename in ASCII, terminated by 00h (max 20 chars, plus ending 00h)
  1Fh     Zero (unused)
  20h-7Eh Garbage (usually 00h-filled)
  7Fh     Checksum (all above bytes XORed with each other)
```
Filesize [04h..07h] and Filename [0Ah..1Eh] are stored only in the first
directory entry of a file (ie. with State=51h or A1h), other directory entries
have that bytes zero-filled.<br/>

#### Filename Notes
The first some letters of the filename should indicate the game to which the
file belongs, in case of commercial games this is conventionally done like so:
Two character region code:<br/>
```
  "BI"=Japan, "BE"=Europe, "BA"=America
```
followed by 10 character game code,<br/>
```
  in "AAAA-NNNNN" form     ;for Pocketstation executables replace "-" by "P"
```
where the "AAAA" part does imply the region too; (SLPS/SCPS=Japan,
SLUS/SCUS=America, SLES/SCES=Europe) (SCxS=Made by Sony, SLxS=Licensed by
Sony), followed by up to 8 characters,<br/>
```
  "abcdefgh"
```
(which may identify the file if the game uses multiple files; this part often
contains a random string which seems to be allowed to contain any chars in
range of 20h..7Fh, of course it shouldn't contain "?" and "\*" wildcards).<br/>

#### Broken Sector List (Block 0, Frame 16..35)
```
  00h-03h Broken Sector Number (Block*64+Frame) (FFFFFFFFh=None)
  04h-7Eh Garbage (usually 00h-filled) (some cards have [08h..09h]=FFFFh)
  7Fh     Checksum (all above bytes XORed with each other)
```
If Block0/Frame(16+N) indicates that a given sector is broken, then the data
for that sector is stored in Block0/Frame(36+N).<br/>

#### Broken Sector Replacement Data (Block 0, Frame 36..55)
```
  00h-7Fh Data (usually FFh-filled, if there's no broken sector)
```

#### Unused Frames (Block 0, Frame 56..62)
```
  00h-7Fh Unused (usually FFh-filled)
```

#### Write Test Frame (Block 0, Frame 63)
Reportedly "write test". Usually same as Block 0 ("MC", 253 zero-bytes, plus
checksum 0Eh).<br/>

#### Title Frame (Block 1..15, Frame 0) (in first block of file only)
```
  00h-01h  ID (ASCII "SC")
  02h      Icon Display Flag
             11h...Icon has 1 frame  (static) (same image shown forever)
             12h...Icon has 2 frames (animated) (changes every 16 PAL frames)
             13h...Icon has 3 frames (animated) (changes every 11 PAL frames)
            Values other than 11h..13h seem to be treated as corrupted file
            (causing the file not to be listed in the bootmenu)
  03h      Block Number (1-15)  "icon block count"  Uh?
                   (usually 01h or 02h... might be block number within
                   files that occupy 2 or more blocks)
                   (actually, that kind of files seem to HAVE title frames
                   in ALL of their blocks; not only in their FIRST block)
                   (at least SOME seem to have such duplicated title frame,
                   but not all?)
  04h-43h  Title in Shift-JIS format (64 bytes = max 32 characters)
  44h-4Fh  Reserved (00h)
  50h-5Fh  Reserved (00h)  ;<-- this region is used for the Pocketstation
  60h-7Fh  Icon 16 Color Palette Data (each entry is 16bit CLUT)
```
For more info on entries [50h..5Fh], see<br/>
[Pocketstation File Header/Icons](../pocketstation.md#pocketstation-file-headericons)<br/>

#### Icon Frame(s) (Block 1..15, Frame 1..3) (in first block of file only)
```
  00h-7Fh  Icon Bitmap (16x16 pixels, 4bit color depth)
```
Note: The icons are shown in the BIOS bootmenu (which appears when starting the
PlayStation without a CDROM inserted). The icons are drawn via GP0(2Ch)
command, ie. as Textured four-point polygon, opaque, with texture-blending,
whereas the 24bit blending color is 808080h (so it's quite the same as raw
texture without blending). As semi-transparency is disabled, Palette/CLUT
values can be 0000h=FullyTransparent, or 8000h=SolidBlack (the icons are
usually shown on a black background, so it doesn't make much of a difference).<br/>

#### Data Frame(s) (Block 1..15, Frame N..63; N=excluding any Title/Icon Frames)
```
  00h-7Fh  Data
```
Note: Files that occupy more than one block are having only ONE Title area, and
only one Icon area (in the first sector(s) of their first block), the
additional blocks are using sectors 0..63 for plain data.<br/>

#### Shift-JIS Character Set (16bit) (used in Title Frames)
Can contain japanese or english text, english characters are encoded like so:<br/>
```
  81h,40h      --> SPC
  81h,43h..97h --> punctuation marks
  82h,4Fh..58h --> "0..9"
  82h,60h..79h --> "A..Z"
  82h,81h..9Ah --> "a..z"
```
Titles shorter than 32 characters are padded with 00h-bytes.<br/>
Note: The titles are \<usually\> in 16bit format (even if they consist of
raw english text), however, the BIOS memory card manager does also accept 8bit
characters 20h..7Fh (so, in the 8bit form, the title could be theoretically up
to 64 characters long, but, nethertheless, the BIOS displays only max 32
chars).<br/>
For displaying Titles, the BIOS includes a complete Shift-JIS character set,<br/>
[BIOS Character Sets](../../kernelbios/character-sets.md#bios-character-sets)<br/>
Shift-JIS is focused on asian languages, and does NOT include european letters
(eg. such with accent marks). Although the non-japanese PSX BIOSes DO include a
european character set, the BIOS memory card manager DOESN'T seem to translate
any title character codes to that character set region.<br/>
