#   Memory Card Images
There are a lot of different ways to get a save from a memory card onto your
PC's hard disk, and these ways sometimes involve sticking some additional
information into a header at the beginning of the file.<br/>

#### Raw Memory Card Images (without header) (ie. usually 128K in size)
```
  SmartLink .PSM,
  WinPSM .PS,
  DataDeck .DDF,
  FPSX .MCR,
  ePSXe .MCD...
```
don't stick any header on the data at all, so you can just read it in and treat
it like a raw memory card.<br/>

All of these headers contain a signature at the top of the file. The three most
common formats and their signatures are:<br/>

```
     Connectix Virtual Game Station format (.MEM): "VgsM", 64 bytes
     PlayStation Magazine format (.PSX): "PSV", 256 bytes
```

some programs will OMIT any blank or unallocated blocks from the end of the
memory card -- if only three save blocks on the card are in use, for example,
saving the other twelve is pointless.<br/>

#### Xploder and Action Replay Files (54 byte header)
```
  00h..14h Filename in ASCII, terminated by 00h (max 20 chars, plus ending 00h)
  15h..35h Title in ASCII, terminated by 00h (max 32 chars, plus ending 00h)
  36h..    File Block(s) (starting with the Title sector)
```
This format contains only a single file (not a whole memory card). The filename
should be the same as used in the Memory Card Directory. The title is more or
less don't care; it may be the SHIFT-JIS title from the Title Sector converted
to ASCII.<br/>

#### .MCS Files (Single Save Format)
MCS files consist of the 128 byte directory frame for the savefile's first block followed by all of that savefile's blocks in linked list order. When importing this format, the directory frame should be parsed for the save filename and the filesize while other fields should be ignored. The rest of the directory frame fields and any extra directory frames, in the case of multi-block saves, should be reconstructed based on the destination memory card.

#### .GME Files (usually 20F40h bytes)
InterAct GME format, produced by the DexDrive.<br/>
```
  000h 12   ASCII String "123-456-STD",00h
  00Ch 4    Usually zerofilled (or meaningless garbage in some files)
  010h 5    Always 00h,00h,01h,00h,01h
  015h 16   Copy of Sector 0..15 byte[00h] ;"M", followed by allocation states
  025h 16   Copy of Sector 0..15 byte[08h] ;00h, followed by next block values
  035h 11   Usually zerofilled (or meaningless garbage in some files)
  040h F00h Fifteen Description Strings (each one 100h bytes, padded with 00h)
  F40h 128K Memory Card Image (128K) (unused sectors 00h or FFh filled)
```
This is a very strange file format, no idea where it comes from. It contains a
F40h bytes header (mainly zerofilled), followed by the whole 128K of FLASH
memory (mainly zerofilled, too, since it usually contains only a small single
executable file).<br/>
