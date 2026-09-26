#   BIOS Character Sets
#### B(51h) - Krom2RawAdd(shiftjis\_code)
```
  In: r4  = 16bit Shift-JIS character code
  Out: r2 = address in BIOS ROM of the desired character (or -1 = error)
```
r4 should be 8140h..84BEh (charset 2), or 889Fh..9872h (charset 3).<br/>

#### B(53h) - Krom2Offset(shiftjis\_code)
```
  In: r4  = 16bit Shift-JIS character code
  Out: r2 = offset within charset (without charset base address)
```
This is a subfunction for B(51h) Krom2RawAdd(shiftjis\_code).<br/>

#### Character Sets in ROM (112Kbytes)
The character sets are located at BFC64000h and up, intermixed with some other
stuff:<br/>
```
  BFC64000h  Charset 1 (16x15 pix, letters with accent marks)    (NOT in JAPAN)
  BFC65CB6h  Garbage   (four-and-a-half reverb tables, ioports, printf strings)
  BFC66000h  Charset 2 (16x15 pix, various alphabets, english, greek, etc.)
  BFC69D68h  Charset 3 (16x15 pix, japanese or chinese symbols or so)
  BFC7F8DEh  Charset 4 (8x15 pix, mainly ASCII letters)
  BFC7FE6Fh  Charset 5 (8x15 pix, additional punctuation marks)    (NOT in PS2)
  BFC7FF32h  Version   (Version and Copyright strings)        (NOT in SCPH1000)
  BFC7FF8Ch  Charset 6 (8x15 pix, seven-and-a-half japanese chars) (NOT in PS2)
  BFC80000h  End       (End of 512kBYTE BIOS ROM)
```
Charset 1 (and Garbage) is NOT included in japanese BIOSes (in the SCPH1000
version that region contains uncompressed program code, in newer japanese
BIOSes that regions are zerofilled)<br/>
Charset 1 symbols are as defined in JIS-X-0212 char(2661h..2B77h), and EUC-JP
char(8FA6E1h..8FABF7h).<br/>
Version (and Copyright) string is NOT included in SCPH1000 version (that BIOS
includes further japanese 8x15 pix chars in that region).<br/>
For charset 2 and 3 it may be recommended to use the B(51h)
Krom2RawAdd(shiftjis\_code) to obtain the character addresses. Not sure if that
BIOS function (or another BIOS function) allows to retrieve charset 1, 4, 5,
and 6 addresses?<br/>
Charset 4 is halfwidth, single-byte Shift JIS codes 21h through 7Eh. This
matches ASCII except code 5Ch which is the halfwidth yen sign (¥) and 7Eh which
is overline (‾).<br/>
Charset 5 contains overhead/combining tilde, backslash (\\), broken bar (¦),
Shift JIS codes A1h through A5h and B0h, DEh, and DFh, left double quotation
mark (“), left single quotation mark (‘), and tilde (~).<br/>
Charset 6 is Shift JIS codes 82A5h through 82ACh, but in halfwidth, and the
last one is cut off.
