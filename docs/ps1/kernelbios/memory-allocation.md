#   Memory Allocation
#### A(33h) - malloc(size)
Allocates size bytes on the heap, and returns the memory handle (aka the
address of the allocated memory block). The address of the block is guaranteed
to by aligned to 4-byte memory boundaries. Size is rounded up to a multiple of
4 bytes. The address may be in KUSEG, KSEG0, or KSEG1, depending on the address
passed to InitHeap.<br/>
Caution: The BIOS (tries to) initialize the heap size to 0 bytes (actually it
accidently overwrites that initial setting by garbage during relocation), so
any call to malloc will fail, unless InitHeap has been used to initialize the
address/size of the heap.<br/>

#### A(34h) - free(buf)
Deallocates the memory block. There's no return value, and no error checking.
The function simply sets [buf-4]=[buf-4] OR 00000001h, so if buf is an invalid
handle it may destroy memory at [buf-4], or trigger a memory exception (for
example, when buf=0).<br/>

#### A(37h) - calloc(sizx, sizy)     ;SLOW!
Allocates xsiz\*ysiz bytes by calling malloc(xsiz\*ysiz), and, unlike malloc, it
does additionally zerofill the memory via SLOW "bzero" function. Returns the
address of the memory block (or zero if failed).<br/>

#### A(38h) - realloc(old\_buf, new\_size)   ;SLOW!
If "old\_buf" is zero, executes malloc(new\_size), and returns r2=new\_buf (or
0=failed). Else, if "new\_size" is zero, executes free(old\_buf), and returns
r2=garbage. Else, executes malloc(new\_size), bcopy(old\_buf,new\_buf,new\_size),
and free(old\_buf), and returns r2=new\_buf (or 0=failed).<br/>
Caution: The bcopy function is SLOW, and realloc does accidently copy
"new\_size" bytes from old\_buf, so, if the old\_size was smaller than new\_size
then it'll copy whatever garbage data - in worst case, if it exceeds the top of
the 2MB RAM region, it may crash with a locked memory exception, although
that'd happen only if SetMem(2) was used to restrict RAM to 2MBs.<br/>

#### A(39h) - InitHeap(addr, size)
Initializes the address and size of the heap - the BIOS does not automatically
do this, so, before using the heap, InitHeap must be called by software.
Usually, the heap would be memory region between the end of the boot
executable, and the bottom of the executable's stack. InitHeap can be also used
to deallocate all memory handles (eg. when a new exe file has been loaded, it
may use it to deallocate all old memory).<br/>
The heap is used only by malloc/realloc/calloc/free, and by the "qsort"
function.<br/>

#### B(00h) - alloc\_kernel\_memory(size)
#### B(01h) - free\_kernel\_memory(buf)
Same as malloc/free, but, instead of the heap, manages the 8kbyte control block
memory at A000E000h..A000FFFFh. This region is used by the kernel to allocate
ExCBs (4x08h bytes), EvCBs (N\*1Ch bytes), TCBs (N\*0C0h bytes), and the process
control block (1x04h bytes). Unlike the heap, the BIOS does automatically
initialize this memory region via SysInitMemory(addr,size), and does
autimatically allocate the above data (where the number of EvCBs and TCBs is as
specified in the SYSTEM.CNF file). Note: FCBs and DCBs are located elsewhere,
at fixed locations in the kernel variables area.<br/>

#### Scratchpad Note
The kernel doesn't include any allocation functions for the scratchpad (nor do
any kernel functions use that memory area), so the executable can freely use
the "fast" memory at 1F800000h..1F8003FFh.<br/>

#### A(9Fh) - SetMem(megabytes)
Changes the effective RAM size by manipulating bits 8-10 of DRAM\_CTRL
(1F801060h), and additionally stores the size in megabytes in RAM at 00000060h.
There are two known variants of this function:<br/>
- the one found in retail and devkit kernels, which only supports setting the
  size to 2 or 8MB (single bank);
- the one used in arcade kernels, which additionally supports 4 and 16MB (as
  2x2MB and 2x8MB respectively).

The values written to DRAM\_CTRL assume bit 11 is already set and will be
incorrect otherwise.<br/>
Note: The retail BIOS bootcode accidently sets the RAM value to 2MB (which is
the correct physical memory size), but initializes the I/O port to 8MB (which
mirrors the physical 2MB within that 8MB region), so the initial values don't
match up with each other.<br/>
Caution: Applying the correct size of 2MB may cause the "realloc" function to
crash (that function may accidently access memory above 2MB).<br/>
