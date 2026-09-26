#   BIOS String Functions
#### A(15h) - strcat(dst, src)
Appends src to the end of dst. Searches the ending 00h byte in dst, and copies
src to that address, up to including the ending 00h byte in src. Returns the
incoming dst value. Refuses to do anything if src or dst is 00000000h (and
returns 0 in that case).<br/>

#### A(16h) - strncat(dst, src, maxlen)
Same as "strcat", but clipped to "MaxSrc=(min(0,maxlen)+1)" characters, ie. the
total length is max "length(dst)+min(0,maxlen)+1". If src is longer or equal to
"MaxSrc", then only the first "MaxSrc" chars are copied (with the last byte
being replaced by 00h). If src is shorter, then everything up to the ending 00h
byte gets copied, but without additional padding (unlike as in "strncpy").<br/>

#### A(17h) - strcmp(str1, str2)
Compares the strings up to including ending 00h byte. Returns 0 if they are
identical, or otherwise [str1+N]-[str2+N], where N is the location of the first
mismatch, the two bytes are sign-expanded to 32bits before doing the
subtraction. The function rejects str1/str2 values of 00000000h (and returns
0=both are zero, -1=only str1 is zero, and +1=only str2 is zero).<br/>

#### A(18h) - strncmp(str1, str2, maxlen)
Same as "strcmp" but stops after comparing "maxlen" characters (and returns 0
if they did match). If the strings are shorter, then comparision stops at the
ending 00h byte (exactly as for strcmp).<br/>

#### A(19h) - strcpy(dst, src)
Copies data from src to dst, up to including the ending 00h byte. Refuses to
copy anything if src or dst is 00000000h. Returns the incoming dst address (or
0 if copy was refused).<br/>

#### A(1Ah) - strncpy(dst, src, maxlen)
Same as "strcpy", but clipped to "maxlen" characters. If src is longer or equal
to maxlen, then only the first "maxlen" chars are copied (but without appending
an ending 00h byte to dst). If src is shorter, then the remaining bytes in dst
are padded with 00h bytes.<br/>

#### A(1Bh) - strlen(src)
Returns the length of the string up to excluding the ending 00h byte (or 0 when
src is 00000000h).<br/>

#### A(1Ch) - index(src, char)
#### A(1Dh) - rindex(src, char)
#### A(1Eh) - strchr(src, char)  ;exactly the same as "index"
#### A(1Fh) - strrchr(src, char) ;exactly the same as "rindex"
Scans for the first (index) or last (rindex) occurence of char in the string.
Returns the memory address of that occurence (or 0 if there's no occurence, or
if src is 00000000h). Char may be 00h (returns the end address of the string).
Note that, despite of the function names, the return value is always a memory
address, NOT an index value relative to src.<br/>

#### A(20h) - strpbrk(src, list)
Scans for the first occurence of a character that is contained in the list. The
list contains whatever desired characters, terminated by 00h.<br/>
Returns the address of that occurence, or 0 if there was none. BUG: If there
was no occurence, it returns 0 only if src[0]=00h, and otherwise returns the
incoming "src" value (which is the SAME return value as when a occurence did
occur on 1st character).<br/>

#### A(21h) - strspn(src, list)
#### A(22h) - strcspn(src, list)
Scans for the first occurence of a character that is (strspn), or that isn't
(strcspn) contained in the list. The list contains whatever desired characters,
terminated by 00h.<br/>
Returns the index (relative to src) of that occurence. If there was no
occurence, then it returns the length of src. That silly return values do not
actually indicate if an occurence has been found or not (unless one checks for
[src+index]=00h or so).<br/>
\*\*\*<br/>
"The strcspn() function shall compute the length (in bytes) of the maximum
initial segment of the string pointed to by s1 which consists entirely of bytes
not from the string pointed to by s2."<br/>
"The strspn() function shall compute the length (in bytes) of the maximum
initial segment of the string pointed to by s1 which consists entirely of bytes
from the string pointed to by s2."<br/>
\*\*\*<br/>
Hmmmm, that'd be vice-versa?<br/>

#### A(23h) - strtok(src, list) ;first call
#### A(23h) - strtok(0, list) ;further call(s)
Used to split a string into fragments, list contains a list of characters that
are to be treated as separators, terminated by 00h.<br/>
The first call copies the incoming string to a buffer in the BIOS variables
area (the buffer size is 100h bytes, so the string should be max 255 bytes
long, plus the ending 00h byte, otherwise the function destroys other BIOS
variables), it does then search the first fragment, starting at the begin of
the buffer. Further calls (with src=00000000h) are searching further fragments,
starting at the buffer address from the previous call. The internal buffer is
used only for strtok, so its contents (and the returned string fragments)
remain intact until a new first call to strtok takes place.<br/>
The separate fragments are processed by searching the first separator, starting
at the current buffer address, the separator is then replaced by a 00h byte,
and the old buffer address is returned to the caller. Moreover, the function
tries to skip all continously following separators, until reaching a
non-separator, and does memorize that address for the next call (due to that
skipping further calls won't return empty fragments, the first call may do so
though). That skipping seems to be bugged, if list contains two or more
different characters, then additional separators aren't skipped.<br/>
```
  ",,TEXT,,,END" with list=","  returns "", "TEXT", "END"
  ",,TEXT,,,END" with list=",." returns "", "", "TEXT", "", "", "END"
```
Once when there are no more fragments, then 00000000h is returned.<br/>

#### A(24h) - strstr(str, substr) - buggy
Scans for the first occurence of substr in the string. Returns the memory
address of that occurence (or 0 if it was unable to find an occurence).<br/>
BUG: After rejecting incomplete matches, the function doesn't fallback to the
old str address plus 1, but does rather continue at the current str address.
Eg. it doesn't find substr="aab" in str="aaab" (in that example, it does merely
realize that "aab"\<\>"aaa" and then that "aab"\<\>"b").<br/>
