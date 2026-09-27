#   BIOS Memory Fill/Copy/Compare (SLOW)
Like most A(NNh) functions, below functions are executed in uncached BIOS ROM,
the ROM has very high waitstates, and the 32bit opcodes are squeezed through an
8bit bus. Moreover, below functions are restricted to process the data
byte-by-byte. So, they are very-very-very slow, don't even think about using
them.<br/>
Of course, that applies also for most other BIOS functions. But it's becoming
most obvious for these small functions; memcpy takes circa 160 cycles per byte
(reasonable would be less than 4 cycles), and bzero takes circa 105 cycles per
byte (reasonable would be less than 1 cycles).<br/>

#### A(2Ah) - memcpy(dst, src, len)
Copies len bytes from [src..src+len-1] to [dst..dst+len-1]. Refuses to copy any
data when dst=00000000h or when len\>7FFFFFFFh. The return value is always
the incoming "dst" value.<br/>

#### A(2Bh) - memset(dst, fillbyte, len)
Fills len bytes at [dst..dst+len-1] with the fillbyte value. Refuses to fill
memory when dst=00000000h or when len\>7FFFFFFFh. The return value is the
incoming "dst" value (or zero, when len=0 or len\>7FFFFFFFh).<br/>

#### A(2Ch) - memmove(dst, src, len) - bugged
Same as memcpy, but (attempts) to support overlapping src/dst regions, by using
a backwards transfer when src\<dst (and, for some reason, only when
dst\>=src+len).<br/>
BUG: The backwards variant accidently transfers len+1 bytes from [src+len..src]
down to [dst+len..dst].<br/>

#### A(2Dh) - memcmp(src1, src2, len) - bugged
Compares len bytes at [src1..src1+len-1] with [src2..src2+len-1], and
(attempts) to return the difference between the first mismatching bytes, ie.
[src1+N]-[src2+N], or 0 if there are no mismatches. Refuses to compare data
when src1 or src2 is 00000000h, and returns 0 in that case.<br/>
BUG: Accidently returns the difference between the bytes AFTER the first
mismatching bytes, ie. [src1+N+1]-[src2+N+1].<br/>
That means that a return value of 0 can mean absolutely anything: That the
memory blocks are identical, or that a mismatch has been found (but that the
NEXT byte after the mismatch does match), or that the function has failed (due
to src1 or src2 being 00000000h).<br/>

#### A(2Eh) - memchr(src, scanbyte, len)
Scans [src..src+len-1] for the first occurence of scanbyte. Refuses to scan any
data when src=00000000h or when len\>7FFFFFFFh. Returns the address of that
first occurence, or 0 if the scanbyte wasn't found.<br/>

#### A(27h) - bcopy(src, dst, len)
Same as "memcpy", but with "src" and "dst" exchanged. That is, the first
parameter is "src", the refuse occurs when "src" is 00000000h, and, returns the
incoming "src" value (whilst "memcpy" uses "dst" in that places).<br/>

#### A(28h) - bzero(dst, len)
Same as memset, but uses 00h as fixed fillbyte value.<br/>

#### A(29h) - bcmp(ptr1, ptr2, len) - bugged
Same as "memcmp", with exactly the same bugs.<br/>
