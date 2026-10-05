#   Interrupt/Exception Handling
The Playstation's Kernel uses an uncredible inefficient and unstable exception
handler; which may have been believed to be very powerful and flexible.<br/>

#### Inefficiency
For a maximum of slowness, it does always save and restore all CPU registers
(including such that aren't used in the exception handler). It does then go
through a list of installed interrupt handlers - and executes ALL of them. For
example, a Timer0 IRQ is first passed to the Cdrom and Vblank handlers (which
must reject it, no thanks), before it does eventually reach the Timer0 handler.<br/>

#### Unstable IRQ Handling
A fundamental mistake in the exception handler is that it doesn't memorize the
incoming IRQ flags. So the various interrupt handlers must check Port 1F801070h
one after each other. That means, if a high priority handler has rejected IRQ
processing (because the desired IRQ flag wasn't set at that time), then a lower
priority handler may process it (assuming that the IRQ flag got set in the
meantime), and, in worst case it may even acknowledge it (so the high priority
handler does never receive it).<br/>
To avoid such problems, there should be only ONE handler installed for each IRQ
source. However, that isn't always possible because the Kernel automatically
installs some predefined handlers. Most noteworthy, the totally bugged
DefaultInterruptHandlers is always installed (and cannot be removed), so it
does randomly trigger Events. Fortunately, it does not acknowledge the IRQs
(unless SetIrqAutoAck was used to enable that fatal behaviour).<br/>

#### B(18h) - ResetEntryInt()
Applies the default "Exit" structure (which consists of a pointer to
ReturnFromException, and the Kernel's exception stacktop (minus 4, for whatever
reason), and zeroes for the R16..R23,R28,R30 registers. Returns the address of
that structure.<br/>
See HookEntryInt for details.<br/>

#### B(19h) - HookEntryInt(addr)
addr points to a structure (with same format as for the setjmp function):<br/>
```
  00h 4    r31/ra,pc ;usually ptr to ReturnFromException function
  04h 4    r28/sp    ;usually exception stacktop, minus 4, for whatever reason
  08h 4    r30/fp    ;usually 0
  0Ch 4x8  r16..r23  ;usually 0
  2Ch 4    r28/gp    ;usually 0
```
The hook function is executed only if the ExceptionHandler has been fully
executed (after processing an IRQ, many interrupt handlers are calling
ReturnFromException to abort further exception handling, and thus do skip the
hook function). Once when the hook function has finished, it should execute
ReturnFromException. The hook function is called with r2=1 (that is important
if the hook address was recorded with setjmp, where it "returns" to the
setjmp caller, with r2 as "return value").<br/>

#### Priority Chains
The Kernel's exception handler has four priority chains, each may contain one
or more Interrupt or Exception handlers. The default handlers are:<br/>
```
  Prio Chain Content
  0    CdromDmaIrq, CdromIoIrq, SyscallException
  1    CardSpecificIrq, VblankIrq, Timer2Irq, Timer1Irq, Timer0Irq
  2    PadCardIrq
  3    DefInt
```
The exception handler calls all handlers, starting with the first element in
the priority 0 chain (ie. usually CdromDmaIrq). The separate handlers must
check if they want to process the IRQ (eg. CdromDmaIrq would process only CDROM
DMA IRQs, but not joypad IRQs or so). If it has processed and acknowledged the
IRQ, then the handler may execute ReturnFromException, which causes the
handlers of lower priority to be skipped (if there are still other
unacknowledge IRQs pending, then the hardware will re-enter the exception
handler as soon as the RFE opcode in ReturnFromException does re-enable
interrupts).<br/>

#### C(02h) - SysEnqIntRP(priority,struc)  ;bugged, use with care
Inserts a new element in the specified priority chain. The new element is
inserted at the begin of the chain, so (within that priority chain) the new
element has highest priority.<br/>
```
  00h 4  pointer to next element    (0=none)  ;this pointer is inserted by BIOS
  04h 4  pointer to SECOND function (0=none)  ;executed if func1 returns r2<>0
  08h 4  pointer to FIRST  function (0=none)  ;executed first
  0Ch 4  Not used (usually zero)
```
BUG: SysDeqIntRP can remove only the first element in the chain (see there for
details), so adding new chain elements may cause OTHER functions to be unable
to remove their chain elements. The BIOS seems to be occassionally
adding/removing the "CardSpecificIrq" and "PadCardIrq" (with priority 1 and 2),
so using that priorities may cause the BIOS to be unable to remove that IRQ
handlers. Using priority 0 and 3 should work (as long as the software takes
care to remove only the newest elements) (but there should be no conflicts with
the BIOS which does never remove priority 0 and 3 elements) (leaving apart that
DequeueCdIntr and _96_remove try to remove priority 0 elements, but that
functions won't work anyways; due to the same bug).<br/>

#### C(03h) - SysDeqIntRP(priority,struc)  ;bugged, use with care
Removes the specified element from the specified priority chain.<br/>
BUG: The function tries to search the whole chain (and to remove the element if
it finds it). However, it does only check the first element properly, and,
thereafter it reads a garbage value from an uninitialized stack location, and
acts more or less unpredictable. So, it can remove only the first element in
the chain, ie. it should be called only if you are SURE that there's no newer
element in the chain, and only if you are SURE that the element IS in the
chain.<br/>

#### SYS(01h) - EnterCriticalSection()  ;syscall with r4=01h
Disables interrupts by clearing SR (cop0r12) Bit 2 and 10 (of which, Bit2 gets
copied to Bit0 once when returning from the syscall exception). Returns 1 if
both bits were set, returns 0 if one or both of the bits were already zero.<br/>

#### SYS(02h) - ExitCriticalSection()   ;syscall with r4=02h
Enables interrupts by set SR (cop0r12) Bit 2 and 10 (of which, Bit2 gets copied
to Bit0 once when returning from the syscall exception). There's no return
value (all registers except SR and K0 are unchanged).<br/>

#### C(0Dh) - SetIrqAutoAck(irq,flag)
Specifies if the DefaultInterruptHandler shall automatically acknowledge IRQs.
The "irq" paramter is the number of the interrupt, ie. 00h..0Ah = IRQ0..IRQ10.
The "flag" value should be 0 to disable AutoAck, or non-zero to enable AutoAck.
By default, AutoAck is disabled for all IRQs.<br/>
Mind that the DefaultInterruptHandler is totally bugged. Especially the AutoAck
feature doesn't work very well: It may cause higher priority handlers to miss
their IRQ, and it may even cause the DefaultInterruptHandler to miss its own
IRQs.<br/>

#### C(06h) - ExceptionHandler()
The C(06h) vector points to the exception handler, ie. to the function that is
invoked from the 4 opcodes at address 80000080h, that opcodes jump directly to
the exception handler, so patching the C(06h) vector has no effect.<br/>
Reading the C(06h) entry can be used to let a custom 80000080h handler pass
control back to the default handler (that, by a "direct" jump, not by the usual
"MOV R9,06h / CALL 0C0h" method, which would destroy main programs R9
register).<br/>
Also, reading C(06h) may be useful for patching the exception handler (which
contains a bunch of NOP opcodes, which seem to be intended to insert additional
opcodes, such like debugger exception handling) (Note: some of that NOPs are
reserved for Memory Card IRQ handling).<br/>
BUG: Early BIOS versions did try to examine a copy of cop0r13 in r2 register,
but did forgot cop0r13 to r2 (so they examined garbage), this was fixed in
newer BIOS versions, additionally, most commercial games still include patches
for compatibility with the old BIOS.<br/>

#### B(17h) - ReturnFromException()
Restores the CPU registers (R1-R31,HI,LO,SR,PC) (except R26/K0) from the
current TCB. This function is usually executed automatically at the end of the
ExceptionHandler, however, functions in the exception chain may call
ReturnFromException to return immediately, without processing chain elements of
lower priority.<br/>

#### C(00h) - EnqueueTimerAndVblankIrqs(priority) ;used with prio=1
#### C(01h) - EnqueueSyscallHandler(priority) ;used with prio=0
#### C(0Ch) - InitDefInt(priority) ;used with prio=3
Internally used to add some default IRQ and Exception handlers.<br/>

#### No Nested Exceptions
The Kernel doesn't support nested exceptions, that would require a decreasing
exception stack, however, the kernel saves the incoming CPU registers in the
current TCB, and an exception stack with fixed start address for internal
push/pop during exception handling. So, nesting would overwrite these values.
Do not enable IRQs, and don't trap other exceptions (like break or syscall
opcodes, or memory or overlow errors) during exception handling.<br/>
Note: The execption stack has a fixed size of 1000h bytes (and is located
somewhere in the first 64Kbytes of memory).<br/>
