#   Number/String/Character Conversion
#### A(0Eh) - abs(val)
#### A(0Fh) - labs(val)  ;exactly same as "abs"
Returns the absolute value (if val\<0 then R2=-val, else R2=val).<br/>

#### A(0Ah) - todigit(char)
Takes the incoming character, ANDed with FFh, and returns 0..9 for characters
"0..9" and 10..35 for "A..Z" or "a..z", or 0098967Fh (9,999,999 decimal) for
any other 7bit characters, or garbage for characters 80h..FFh.<br/>

#### A(25h) - toupper(char)
#### A(26h) - tolower(char)
Returns the incoming character, ANDed with FFh, with letters "A..Z" converted
to uppercase/lowercase format accordingly. Works only for char 00h..7Fh (some
characters in range 80h..FFh are left unchanged, others are randomly "adjusted"
by adding/subtracting 20h, and by sign-expanding the result to 32bits).<br/>

#### A(0Dh) - strtol(src, src\_end, base)
Converts a string to a number. The function skips any leading "blank"
characters (that are, 09h..0Dh, and 20h) (ie. TAB, CR, LF, SPC, and some
others) (some characters in range 80h..FFh are accidently treated as "blank",
too).<br/>
The incoming base value should be in range 2..11, although the function does
also accept the buggy values in range of 12..36 (for values other than 2..36 it
defaults to decimal/base10). The used numeric digits are "0..9" and "A..Z" (or
less when base is smaller than 36).<br/>
The string may have a negative sign prefix "-" (negates the result) (a "+" is
NOT recognized; and will be treated as the end of the string). Additionally,
the string may contain prefixes "0b" (binary/base2), "0x" (hex/base16), or "o"
(octal/base8) (only "o", not "0o"), allowing to override the incoming "base"
value.<br/>
BUG: Incoming base values greater than 11 don't work due to the prefix feature
(eg. base=16 with string "0b11" will be treated as 11 binary, and base=36 with
string "o55" will be treated as 55 octal) (the only workaround would be to
add/remove leading "0" characters, ie. "b11" or "00b11" or "0o55" would work
okay).<br/>
Finally, the function initializes result=0, and does then process the digits as
"result=result\*base+digit" (without any overflow checks) unless/until it
reaches an unknown digit (or when digit\>=base) (ie. the string may end with
00h, or with any other unexpected characters).<br/>
The function accepts both uppercase and lowercase characters (both as prefixes,
and as numeric digits). The function returns R2=result, and
[src\_end]=end\_address (ie. usually the address of the ending 00h byte; or of
any other unexpected end-byte). If src points to 00000000h, then the function
returns r2=0, and leaves [src\_end] unchanged.<br/>

#### A(0Ch) - strtoul(src, src\_end, base)
Same as "strtol" except that it doesn't recognize the "-" sign prefix (ie.
works only for unsigned numbers).<br/>

#### A(10h) - atoi(src)
#### A(11h) - atol(src)  ;exactly same as "atoi" (but slightly slower)
Same as "strtol", except that it doesn't return the string end address in
[src\_end], and except that it defaults to base=10, but still supports prefixes,
allowing to use base2,8,16. CAUTION: For some super bizarre reason, this
function treats "0" (a leading ZERO digit) as OCTAL prefix (unlike strtol,
which uses the "o" letter as octal prefix) (the "0x" and "0b" prefixes are
working as usually).<br/>

#### A(12h) - atob(src, num\_dst)
Calls "strtol(str,src\_end,10)", and does then exchange the two return values
(ie. sets R2=[src\_end], and [num\_dst]=value\_32bit).<br/>

#### A(0Bh) - atof(src) ;USES (ABSENT) COP1 FPU !!!
#### A(32h) - strtod(src, src\_end) ;USES (ABSENT) COP1 FPU !!!
These functions are intended to convert strings to floating point numbers,
however, the functions are accidently compiled for MIPS processors with COP1
floating point unit (which is not installed in the PSX, nor does the BIOS
support a COP1 software emulation), so calling these functions will produce a
coprocessor exception, causing the PSX to lockup via A(40h)
SystemErrorUnresolvedException.<br/>

#### Note
On other systems (eg. 8bit computers), "abs/atoi" (integer) and "labs/atol"
(long) may act differently. However, on the Playstation, both use signed 32bit
values.<br/>
