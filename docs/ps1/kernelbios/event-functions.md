#   Event Functions
#### B(08h) - OpenEvent(class, spec, mode, func)
Adds an event structure to the event table.<br/>
```
     class,spec - triggers if BOTH values match
     mode - (1000h=execute function/stay busy, 2000h=no func/mark ready)
     func - Address of callback function (0=None) (used only when mode=1000h)
  out: R2 = Event descriptor (F1000000h and up), or FFFFFFFFh if failed
```
Opens an event, should be called within a critical section. The return value is
used to identify the event to the other event functions. A list of event
classes, specs and modes is at the end of this section. Initially, the event is
disabled.<br/>
Note: The desired max number of events can be specified in the SYSTEM.CNF boot
file (the default is "EVENT = 10" (which is a HEX number, ie. 16 decimal; of
which 5 events are internally used by the BIOS for CDROM functions, so, of the
16 events, only 11 events are available to the game). A bigger amount of events
will slowdown the DeliverEvent function (which always scans all EvCBs, even if
all events are disabled).<br/>

#### B(09h) - CloseEvent(event) - releases event from the event table
Always returns 1 (even if the event handle is unused or invalid).<br/>

#### B(0Ch) - EnableEvent(event) - Turns on event handling for specified event
Always returns 1 (even if the event handle is unused or invalid).<br/>

#### B(0Dh) - DisableEvent(event) - Turns off event handling for specified event
Always returns 1 (even if the event handle is unused or invalid).<br/>

#### B(0Ah) - WaitEvent(event)
Returns 0 if the event is disabled. Otherwise hangs in a loop until the event
becomes ready, and returns 1 once when it is ready (and automatically switches
the event back to busy status). Callback events (mode=1000h) do never set the
ready flag (and thus WaitEvent would hang forever).<br/>
The main program simply hangs during the wait, so when using multiple threads,
it may be more recommended to create an own waitloop that checks TestEvent, and
to call ChangeTh when the event is busy.<br/>
BUG: The return value is unstable (sometimes accidently returns 0=disabled if
the event status changes from not-ready to ready shortly after the function
call).<br/>

#### B(0Bh) - TestEvent(event)
Returns 0 if the event is busy or disabled. Otherwise, when it is ready,
returns 1 (and automatically switches the event back to busy status). Callback
events (mode=1000h) do never set the ready flag.<br/>

#### B(07h) - DeliverEvent(class, spec)
This function is usually called by the kernel, it triggers all events that are
enabled/busy, and that have the specified class and spec values. Depending on
the mode, either the callback function is called (mode=1000h), or the event is
marked as enabled/ready (mode=2000h).<br/>

#### B(20h) - UnDeliverEvent(class, spec)
This function is usually called by the kernel, undelivers all events that are
enabled/ready, and that have mode=2000h, and that have the specified class and
spec values. Undeliver means that the events are marked as enabled/busy.<br/>

#### C(04h) - get\_free\_EvCB\_slot()
A subfunction for OpenEvent.<br/>

#### Event Classes
File Events:<br/>
```
  0000000xh memory card (for file handle fd=x)
```
Hardware Events:<br/>
```
  F0000001h IRQ0  VBLANK
  F0000002h IRQ1  GPU
  F0000003h IRQ2  CDROM Decoder
  F0000004h IRQ3  DMA controller
  F0000005h IRQ4  RTC0 (timer0)
  F0000006h IRQ5/IRQ6 RTC1 (timer1 or timer2)
  F0000007h N/A   Not used (this should be timer2)
  F0000008h IRQ7  SIO0 (joypad/memcard)
  F0000009h IRQ9  SPU
  F000000Ah IRQ10 PIO ;uh, does the PIO have an IRQ signal? (IRQ10 is joypad)
  F000000Bh IRQ8  SIO1
  F0000010h Exception ;CPU crashed (BRK,BadSyscall,Overflow,MemoryError, etc.)
  F0000011h memory card (lower level BIOS functions)
  F0000012h memory card (not used by BIOS; maybe used by Sony's devkit?)
  F0000013h memory card (not used by BIOS; maybe used by Sony's devkit?)
```
Event Events:<br/>
```
  F1xxxxxxh event (not used by BIOS; maybe used by Sony's devkit?)
```
Root Counter Events (Timers and Vblank):<br/>
```
  F2000000h Root counter 0 (Dotclock)                    (hardware timer)
  F2000001h Root counter 1 (horizontal retrace?)         (hardware timer)
  F2000002h Root counter 2 (one-eighth of system clock)  (hardware timer)
  F2000003h Root counter 3 (vertical retrace?) (this is a software timer)
```
User Events:<br/>
```
  F3xxxxxxh user (not used by BIOS; maybe used by games and/or Sony's devkit?)
```
BIOS Events (including such that have nothing to do with BIOS):<br/>
```
  F4000001h memory card (higher level BIOS functions)
  F4000002h libmath (not used by BIOS; maybe used by Sony's devkit?)
```
Thread Events:<br/>
```
  FFxxxxxxh thread (not used by BIOS; maybe used by Sony's devkit?)
```

#### Event Specs
```
  0001h counter becomes zero
  0002h interrupted
  0004h end of i/o
  0008h file was closed
  0010h command acknowledged
  0020h command completed
  0040h data ready
  0080h data end
  0100h time out
  0200h unknown command
  0400h end of read buffer
  0800h end of write buffer
  1000h general interrupt
  2000h new device
  4000h system call instruction ;SYS(04h..FFFFFFFFh)
  8000h error happened
  8001h previous write error happened
  0301h domain error in libmath
  0302h range error in libmath
```

#### Event modes
```
  1000h Execute callback function, and stay busy (do NOT mark event as ready)
  2000h Do NOT execute callback function, and mark event as ready
```
