#   Internal Boot Functions
#### A(45h) - init\_a0\_b0\_c0\_vectors
Copies the three default four-opcode handlers for the A(NNh),B(NNh),C(NNh)
functions to A00000A0h..A00000CFh.<br/>

#### C(07h) - InstallExceptionHandlers()  ;destroys/uses k0/k1
Copies the default four-opcode exception handler to the exception vector at
80000080h..8000008Fh, and, for whatever reason, also copies the same opcodes to
80000000h..8000000Fh.<br/>

#### C(08h) - SysInitMemory(addr,size)
Initializes the address (A000E000h) and size (2000h) of the allocate-able
Kernel Memory region, and, seems to deallocate any memory handles which may
have been allocated via B(00h).<br/>

#### C(09h) - SysInitKernelVariables()
Zerofills all Kernel variables; which are usually at [00007460h..0000891Fh].<br/>
Note: During the boot process, the BIOS accidently overwrites the first opcode
of this function (by the last word of the A0h table), so, thereafter, this
function won't work anymore (nor would it be of any use).<br/>

#### C(12h) - InstallDevices(ttyflag)
Initializes the size and address of the File and Device Control Blocks (FCBs
and DCBs). Adds the TTY device by calling "KernelRedirect(ttyflag)", and the
CDROM and Memory Card devices by calling "AddCDROMDevice()" and
"AddMemCardDevice()".<br/>

#### C(1Ch) - AdjustA0Table()
Copies the B(32h..3Bh) and B(3Ch..3Fh) function addresses to A(00h..09h) and
A(3Bh..3Eh). Apparently Sony's compiler/linker can't insert the addresses in
the A0h table directly at compilation time, so this function is used to insert
them during execution of the boot code.<br/>
