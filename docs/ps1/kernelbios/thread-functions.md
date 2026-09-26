#   BIOS Thread Functions
#### B(0Eh) - OpenTh(reg\_PC,reg\_SP\_FP,reg\_GP)
Searches a free TCB, marks it as used, and stores the inital program counter
(PC), global pointer (GP aka R28), stack pointer (SP aka R29), and frame
pointer (FP aka R30) (using the same value for SP and FP). All other registers
are left uninitialized (eg. may contain values from an older closed thread,
that includes the SR register, see note).<br/>
The return value is the new thread handle (in range FF000000h..FF000003h,
assuming that 4 TCBs are allocated) or FFFFFFFFh if there's no free TCB. The
function returns to the old current thread, use "ChangeTh" to switch to the
new thread.<br/>
Note: The desired max number of TCBs can be specified in the SYSTEM.CNF boot
file (the default is "TCB = 4", one initially used for the boot executable,
plus 3 free threads).<br/>

#### BUG - Unitialized SR Register
OpenTh does NOT initialize the SR register (cop0r12) of the new thread.
Upon powerup, the bootcode zerofills the TCB memory (so, the SR of new threads
will be initially zero; ie. Kernel Mode, IRQ's disabled, and COP2 disabled).
However, when closing/reopening threads, the SR register will have the value of
the old closed thread (so it may get started with IRQs enabled, and, in worst
case, if the old thread should have switched to User Mode, even without access
to KSEG0, KSEG1 memory).<br/>
Or, ACTUALLY, the memory is NOT zerofilled on powerup... so SR is total random?<br/>

#### B(0Fh) - CloseTh(handle)
Marks the TCB for the specified thread as unused. The function can be used for
any threads, including for the current thread.<br/>
Closing the current thread doesn't terminate the current thread, so it may
cause problems once when opening a new thread, however, it should be stable to
execute the sequence "DisableInterrupts, CloseCurrentThread,
ChangeOtherThread".<br/>
The return value is always 1 (even if the handle was already closed).<br/>

#### B(10h) - ChangeTh(handle)
Pauses the current thread, and activates the selected new thread (or crashes if
the specified handle was unused or invalid).<br/>
The return value is always 1 (stored in the R2 entry of the TCB of the old
thread, so the return value will be received once when changing back to the old
thread).<br/>
Note: The BIOS doesn't automatically switch from one thread to another. So, all
other threads remain paused until the current thread uses ChangeTh to pass
control to another thread.<br/>
Each thread is having it's own CPU registers (R1..R31,HI,LO,SR,PC), the
registers are stored in the TCB of the old thread, and restored when switching
back to that thread. Mind that other registers (I/O Ports or GTE registers
aren't stored automatically, so, when needed, they need to be pushed/popped by
software before/after ChangeTh).<br/>

#### C(05h) - get\_free\_TCB\_slot()
Subfunction for OpenTh, returns the number of the first free TCB (usually
in range 0..3) or FFFFFFFFh if there's no free TCB.<br/>

#### SYS(03h) ChangeThreadSubFunction(addr) ;syscall with r4=03h, r5=addr
Subfunction for ChangeTh, R5 contains the address of the new TCB, just like
all exceptions, the syscall exception is saving the CPU registers in the
current TCB, but does then apply the new TCB as current TCB, and so, it does
then enter the new thread when returning from the exception.<br/>
