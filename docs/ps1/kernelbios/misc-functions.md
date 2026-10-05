#   Misc Functions
#### A(2Fh) - rand()
Advances the random generator as "x=x\*41C64E6Dh+3039h" (aka plus 12345
decimal), and returns a 15bit random value "R2=(x/10000h) AND 7FFFh".<br/>

#### A(30h) - srand(seed)
Changes the current 32bit value of the random generator.<br/>

#### A(B4h) - GetSystemInfo(index)  ;not supported by old CEX-1000 version
Returns a word, halfword, or string, depending on the selected index value:<br/>
```
  00h      Get Kernel BCD Date       (eg. 19951204h) (YYYYMMDDh)
  01h      Get Kernel Flags or so    (usually/always 000000003h)
  02h      Get Kernel Version String (eg. "CEX-3000/1001/1002 by K.S.",0)
  03h      Get whatever halfword     (usually 0)    ;PS2: returns cop0r15
  04h      Get whatever halfword     (usually 0)
  05h      Get RAM Size in kilobytes (usually 2048) ;=[00000060h] SHL 10
  06h      Get arcade board flag     (usually 0)
  07h      Get VRAM Size in kilobytes (usually 400h)
  08h      Get whatever halfword     (usually 0)
  09h      Get SPU RAM Size in kilobytes (usually 200h)
  0Ah..0Bh Get whatever halfwords    (usually 0,0)
  0Ch..0Dh Get whatever halfwords    (usually 1,1)
  0Eh      Get non-arcade flag       (usually 1)
  0Fh      N/A (returns zero) ;PS2: returns 0000h (effectively = same as zero)
  10h..FFFFFFFFh Not used (returns zero)
```
Note: The Date/Version are referring to the Kernel (in the first half of the
BIOS). The Intro and Bootmenu (in the second half of the BIOS) may have a
different version, there's no function to retrieve info on that portion,
however, a version string for it can be usually found at BFC7FF32h (eg. "System
ROM Version 4.5 05/25/00 E",0) (in many bios versions, the last letter of that
string indicates the region, but not in all versions) (the old SCPH1000 does
not include that version string at all).<br/>
The old CEX-1000 kernel lacks this function. LIBETC's GetSystemInfo works
around that: if the word at 000004D0h is nonzero it is called instead;
otherwise the words at BFC00000h..BFC0457Fh are summed, and if the sum is
4A20382Ch the library answers by itself: index 0/1 from [BFC00100h/104h],
index 2 as the pointer BFC00129h, index 3 as cop0r15 AND FFh, index 5 as
[00000060h] SHL 10, and index 4 and 06h..0Eh from a hardcoded table of the
usual values above. Any other sum returns -1.<br/>

#### B(56h) - GetC0Table()
#### B(57h) - GetB0Table()
Retrieves the address of the jump lists for B(NNh) and C(NNh) functions,
allowing to patch entries in that lists (however, the BIOS does often jump
directly to the function addresses, rather than indirectly via the list, so
patching may have little effect in such cases). Note: There's no function to
retrieve the address of the A(NNh) jump list, however, that list is
usually/always at 00000200h.<br/>

#### A(31h) - qsort(base, nel, width, callback)
Sorts an array, using a super-slow implementation of the "quick sort"
algorithm. base is the address of the array, nel is the number of elements in
the array, width is the size in bytes of each element, callback is a function
that receives pointers to two elements which need to be compared; callback
should return return zero if the elements are identical, or a positive/negative
number to indicate which element is bigger.<br/>
The qsort function rearranges the contents of the array, ie. depending on the
callback result, it may swap the contents of the two elements, for some bizarre
reason it doesn't swap them directly, but rather stores one of the elements
temporarily on the heap (that means, qsort works only if the heap was
initialized with InitHeap, and only if "width" bytes are free). There's no
return value.<br/>

#### A(35h) - lsearch(key, base, nel, width, callback)
#### A(36h) - bsearch(key, base, nel, width, callback)
Searches an element in an array (key is the pointer to the searched element,
the other parameters are same as for "qsort"). "lsearch" performs a slow linear
search in an unsorted array, by simply comparing one array element after each
other. "bsearch" assumes that the array contains sorted elements (eg. via
qsort), which is allowing to skip some elements, and to jump back and forth in
the array, until it has found the desired element (or the location where it'd
be, if it'd be in the array). Both functions return the address of the element
(or 0 if it wasn't found).<br/>

#### C(19h) - \_ioabort(txt1,txt2)
Displays the two strings on the TTY (in some cases the BIOS does accidently
pass garbage instead of the 2nd string though). And does then execute
_ioabort\_raw(1), see there for more details.<br/>

#### A(B2h) - _ioabort\_raw(param)  ;not supported by old CEX-1000 version
Executes "longjmp(ioabortbuffer,param)". Internally used to recover from
failed I/O operations, param should be nonzero to notify the setjmp caller
that the abort has occurred.<br/>

#### A(13h) - setjmp(buf)
This is a somewhat incomplete implementation of posix's setjmp, by storing the ABI-saved CPU registers in the specified buffer (30h bytes):<br/>
```
  00h 4    r31 (ra) (aka caller's pc)
  04h 4    r29 (sp)
  08h 4    r30 (fp)
  0Ch 4x8  r16..r23
  2Ch 4    r28 (gp)
```
That type of buffer can be used with "_ioabort", "longjmp", and also
"HookEntryInt(addr)".<br/>
The "setjmp" function returns 0 when called directly. However, it may return again -
to the same return address, and the same stack pointer - with another return value (which should be usually
non-zero, to indicate that the state has been restored (eg. \_ioabort passes 1 as
return value).<br/>
Also noteworthy from what a compliant setjmp implementation should be doing
is the absence of saving the state of cop0 and cop2, thus making this slightly
unsuitable for a typical coroutine system implementation.<br/>

#### A(14h) - longjmp(buf, param)
Restores the R16-R23,GP,SP,FP,RA registers from a previously recorded
jmp_buf buffer, and "returns" to that new RA address (rather than to the caller of the
longjmp function). The "param" value is passed as "return value" to the
code at RA, ie. usually to the caller of the original setjmp call. Noteworthy difference
from a conformant longjmp implementation is that the "param" value won't be clamped to 1 if
you pass 0 to it. So since setjmp returns 0 on the first call, the caller of longjmp must take
care that "param" is non-zero, so the callsite of setjmp can make the difference between the first
call and a rollback. See setjmp for further details.<br/>

#### A(53h) - set\_ioabort\_handler(src)  ;PS2 only  ;PSX: SystemError
Normally the _ioabort handler is changed only internally during booting, with
this new function, games can install their own \_ioabort handler. src is pointer
to a 30h-byte "savestate" structure, which will be copied to the actual \_ioabort
structure.<br/>

#### A(06h) or B(38h) - exit(exitcode)
Terminates the program and returns control to the BIOS; which does then lockup
itself via A(3Ah) _exit.<br/>

#### A(A0h) - \_boot()
Performs a warmboot (resets the kernel and reboots from CDROM). Unlike the
normal coldboot procedure, it doesn't display the "\<S\>" and "PS" intro
screens (and doesn't verify the "PS" logo in the ISO System Area), and, doesn't
enter the bootmenu (even if the disk drive is empty, or if it contains an Audio
disk). And, it doesn't reload the SYSTEM.CNF file, so the function works only
if the same disk is still inserted (or another disk with identical SYSTEM.CNF,
such like Disk 2 of the same game).<br/>

#### A(B5h..BFh) B(11h,24h..29h,2Ch..31h,5Eh..FFh) C(1Eh..7Fh) - N/A - Jump 0
These functions jump to address 00000000h. For whatever reason, that address
does usually contain a copy of the exception handler (ie. same as at address
80000080h). However, since there's no return address stored in EPC register,
the functions will likely crash when returning from the exception handler.<br/>

#### A(57h..5Ah,73h..77h,79h..7Bh,7Dh,7Fh..80h,82h..8Fh,B0h..B1h,B3h), and
#### C(0Eh..11h,14h) - N/A - Returns 0
No function. Simply returns with r2=00000000h.<br/>
Reportedly, A(85h) is CdStop, but that seems to be nonsense?<br/>

#### SYS(00h) - NoFunction()
No function. Simply returns without changing any registers or memory locations
(except that, of course, the exception handler destroys k0).<br/>

#### SYS(04h..FFFFFFFFh) - calls DeliverEvent(F0000010h,4000h)
These are syscalls with invalid function number in R4. For whatever reason that
is handled by issuing DeliverEvent(F0000010h,4000h). Thereafter, the syscall
returns to the main program (ie. it doesn't cause a SystemError).<br/>

#### A(3Ah) - \_exit(exitcode)
#### A(40h) - SystemErrorUnresolvedException()
#### A(A1h) - SystemError(type,errorcode) ;type "B"=Boot,"D"=Disk
These are used "SystemError" functions. The functions are repeatedly jumping to
themselves, causing the system to hang. Possibly useful for debugging software
which may hook that functions.<br/>

#### A(4Fh,50h,52h,53h,9Ah,9Bh) B(1Ah..1Fh,21h..23h,2Ah,2Bh,52h,5Ah) C(0Bh) - N/A
These are additional "SystemError" functions, but they are never used. The
functions are repeatedly jumping to themselves, causing the system to hang.<br/>

#### BRK(1C00h) - Division by zero (commonly checked/invoked by software)
#### BRK(1800h) - Division overflow (-80000000h/-1, sometimes checked by software)
The CPU does not generate any exceptions upon divide overflows, because of
that, the Kernel code and many games are commonly checking if the divider is
zero (by software), and, if so, execute a BRK 1C00h opcode. The default BIOS
exception handler doesn't handle BRK exceptions, and does simply redirect them
to SystemErrorUnresolvedException().<br/>
