#   File Execute and Flush Cache
#### A(41h) - LoadTest(filename, headerbuf)
Loads the 800h-byte exe file header to an internal sector buffer, and does then
copy bytes [10h..4Bh] of that header to headerbuf[00h..3Bh].<br/>

#### A(42h) - Load(filename, headerbuf)
Same as LoadTest (see there for details), but additionally loads the body
of the executable (using the size and destination address in the file header),
and does call FlushCache. The exe can be then started via Exec (this isn't
done automatically by LoadTest). Unlike "LoadExec", the
"LoadTest/Exec" combination allows to return the new exe file to return
to the old exe file (instead of restarting the boot executable).<br/>
BUG: Uses the unstable FlushCache function (see there for details).<br/>

#### A(43h) - Exec(headerbuf, param1, param2)
Can be used to start a previously loaded executable. The function saves
R16,R28,R30,SP,RA in the reserved region of headerbuf (rather than on stack),
more or less slowly zerofills the memfill region specified in headerbuf, reads
the stack base and offset values and sets SP and FP to base+offset (or leaves
them unchanged if base=0), reads the GP value from headerbuf and sets GP to
that value. Then calls the excecutables entrypoint, with param1 and param2
passed in r4,r5.<br/>
If the executable (should) return, then R16,R28,R30,SP,RA are restored from
headerbuf, and the function returns with r2=1.<br/>

#### A(51h) - LoadExec(filename, stackbase, stackoffset)
This is a rather bizarre function. In short, it does load and execute the
specified file, and thereafter, it (tries to) reload and restart to boot
executable.<br/>
Part1: Takes a copy of the filename, with some adjustments: Everything up to
the first ":" or 00h byte is copied as is (ie. the device name, if it does
exist, or otherwise the whole path\filename.ext;ver), the remaining characters
are copied and converted to uppercase (ie. the path\filename.ext;ver part, or
none if the device name didn't exist), finally, checks if a ";" exists (ie. the
version suffix), if there's none, then it appends ";1" as default version.
CAUTION: The BIOS allocates ONLY 28 bytes on stack for the copy of the
filename, that region is followed by 4 unused bytes, so the maximum length
would be 32 bytes (31 characters plus EOL) (eg.
"device:\pathname\filename.ext;1",00h).<br/>
Part2: Enables IRQs via ExitCriticalSection, memorizes the stack base/offset
values from the previously loaded executable (which should have been the boot
executable, unless LoadExec should have been used in nested fashion),
does then use LoadTest to load the desired file, replaces the stack
base/offset values in its headerbuf by the LoadExec parameter values, and
does then execute it via Exec(headerbuf,1,0).<br/>
Part3: If the exefile returns, or if it couldn't be loaded, then the boot file
is (unsuccessfully) attempted to be reloaded: Enables IRQs via
ExitCriticalSection, loads the boot file via LoadTest, replaces the stack
base/offset values in its headerbuf by the values memorized in Part2 (which
\<should\> be the boot executable's values from SYSTEM.CNF, unless the
nesting stuff occurred), and does then execute the boot file via
Exec(headerbuf,1,0).<br/>
Part4: If the boot file returns, or if it couldn't be loaded, then the function
looks up in a "JMP $" endless loop (normally, returning from the boot exe
causes SystemError("B",38Ch), however, after using
LoadExec, this functionality is replaced by the "JMP $" lockup.<br/>
BUG: Uses the unstable FlushCache function (see there for details).<br/>
BUG: Part3 accidently treats the first 4 characters of the exename as memory
address (causing an invalid memory address exception on address 6F726463h, for
"cdrom:filename.exe").<br/>

#### A(9Ch) - SetConf(num\_EvCB, num\_TCB, stacktop)
Changes the number of EvCBs and TCBs, and the stacktop. These values are usually
initialized from the settings in the SYSTEM.CNF file, so using this function
usually shouldn't ever be required.<br/>
The function deallocates all old ExCBs, EvCBs, TCBs (so all Exception handlers,
Events, and Threads (except the current one) are lost, and all other memory
that may have been allocated via alloc\_kernel\_memory(size) is deallocated, too.
It does then allocate the new control blocks, and enqueue the default handlers.
Despite of the changed stacktop, the current stack pointer is kept intact, and
the function returns to the caller.<br/>

#### A(9Dh) - GetConf(num\_EvCB\_dst, num\_TCB\_dst, stacktop\_dst)
Returns the number of EvCBs, TCBs, and the initial stacktop. There's no return
value in the R2 register, instead, the three 32bit return values are stored at
the specified "dst" addresses.<br/>

#### A(44h) - FlushCache()
Flushes the Code Cache, so opcodes are ensured to be loaded from RAM. This is
required when loading program code via DMA (ie. from CDROM) (the cache
controller apparently doesn't realize changes to RAM that are caused by DMA).
The LoadTest and LoadExec functions are automatically calling
FlushCache (so FlushCache is required only when loading program code via
"read" or via "CdReadSector").<br/>
FlushCache may be also required when relocating or modifying program code by
software (the cache controller doesn't seem to realize modifications to memory
mirrors, eg. patching the exception handler at 80000080h seems to be work
without FlushCache, but patching the same bytes at 00000080h doesn't).<br/>
Note: The PSX doesn't have a Data Cache (or actually, it has, but it's misused
as Fast RAM, mapped to a fixed memory region, and which isn't accessable by
DMA), so FlushCache isn't required for regions that contain data.<br/>
BUG: The FlushCache function contains a handful of opcodes that do use the k0
register without having IRQs disabled at that time, if an IRQ occurs during
those opcodes, then the k0 value gets destroyed by the exception handler,
causing FlushCache to get trapped in an endless loop.<br/>
One workaround would be to disable all IRQs before calling FlushCache, however,
the BIOS does internally call the function without IRQs disabled, that applies
to:<br/>
```
  load_file  A(42h)
  load_exec  A(51h)
  add_device B(47h) (and all "add_xxx_device" functions)
  init_card  B(4Ah)
  and by intro/boot code
```
for load\_file/load\_exec, IRQ2 (cdrom) and IRQ3 (dma) need to be enabled, so the
"disable all IRQs" workaround cannot be used for that functions, however, one
can/should disable as many IRQs as possible, ie. everything except IRQ2/IRQ3,
and all DMA interrupts except DMA3 (cdrom).<br/>

#### Executable Memory Allocation
LoadTest and LoadExec are simply loading the file to the address
specified in the exe file header. There's absolutely no verification whether
that memory is (or isn't) allocated via malloc, or if it is used by the boot
executable, or by the kernel, or if it does contain RAM at all.<br/>
When using the "malloc" function combined with loading exe files, it may be
recommended not to pass all memory to InitHeap (ie. to keep a memory region
being reserved for loading executables).<br/>

#### Note
For more info about EXE files and their headers, see<br/>
[CDROM File Formats](../cdr/cdromfileformats/index.md)<br/>
