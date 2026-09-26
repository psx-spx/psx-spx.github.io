#   Controllers - Lightguns - Konami Justifier/Hyperblaster (IRQ10)
#### Overall IRQ10-Based Lightgun Access
```
  Send  01h 42h 00h x0h 00h
  Reply HiZ 31h 5Ah buttons
```
The purpose of the "x0h" byte is probably to enable IRQ10 (00h=off, 10h=on),
this would allow to access more than one lightgun (with only one per frame
having the IRQ enabled).<br/>

#### Standard IRQ10-based Lightguns (Konami)
The Controller Data simply consists of the ID and buttons states:<br/>
```
  __Halfword 0 (Controller Info)___________________
  0-15  Controller Info  (5A31h=Konami Lightgun; Timer/IRQ10 type)
  __Halfword 1 (Buttons)
  0-2   Not used                 (All bits always 1)
  3     Start Button (Left Side) (0=Pressed, 1=Released)  ;aka Joypad Start
  4-13  Not used                 (All bits always 1)
  14    Back Button  (Rear End)  (0=Pressed, 1=Released)  ;aka Joypad X-Button
  15    Trigger Button           (0=Pressed, 1=Released)  ;aka Joypad []-Button
```
The coordinates aren't part of the controller data, instead they must be read
from Timer 0 and 1 upon receiving IRQ10 (see IRQ10 Notes below).<br/>

#### Konami Lightgun Drawing
```
     __                 ______ _
   _|__\_______________/  ___ \ \   Konami Justifier/Hyperblaster (light green)
  |   _______________ __ /   \ \ \
  |__|   _ _ _ _     |==|    O| \O\ .... Back Button (Rear End)
     |__:_:_:_:_:__  |___\__ /  ( (
                   |_|  ) \  :   \ \
      Trigger ......  \___/| :...|.|.... Start Button (Left Side)
                           |     | |
                           |     | | SLPH-00013/SLPH-00014/SLEH-0005/SLUH-00017
                          /     _|_|
                          \___--
```

#### Konami IRQ10 Notes
The PSX does have a lightgun input (Pin 8 of the controller), but, Sony did
apparently "forget" to latch the current cathode ray beam coordinates by
hardware when sensing the lightgun signal (quite strange, since that'd be a
simple, inexpensive, and very obvious feature for a gaming console).<br/>
Instead, the lightgun signal triggers IRQ10, and the interrupt handler is
intended to "latch" the coordinates by software (by reading Timer 0 and 1
values, which must configured to be synchronized with the GPU).<br/>
That method requires IRQ handling to be properly implemented in software
(basically, IRQs should not be disabled for longer periods, and DMA transfers
should not block the bus for longer periods). In practice, most programmers
probably don't realize how to do that, to the worst, Sony seems to have
delivered a slightly bugged library (libgun) to developers.<br/>
For details on Timers, see:<br/>
[Timers](../../system/timers.md)<br/>
In some consoles, IRQ10 seems to be routed through a Secondary IRQ Controller,
see:<br/>
[DEV8 DTL-H2000 I/O Ports](../../pio/expansionportpio.md#dev8-dtl-h2000-io-ports)<br/>

#### IRQ10 Priority
For processing IRQ10 as soon as possible, it should be assigned higher priority
than all other IRQs (ie. when using the SysEnqIntRP BIOS function, it should be
the first/newest element in priority chain 0). The libgun stuff assigns an even
higher priority by patching the BIOS exception handler, causing IRQ10 to be
processed shortly before processing the priority chains (the resulting IRQ
priority isn't actually higher as when using 1st element of chain 0; the main
difference is that it skips some time consuming code which pushes registers
R4..R30). For details on that patch, see:<br/>
[BIOS Patches](../../kernelbios/patches.md#bios-patches)<br/>
Even if IRQ10 has highest priority, execution of (older) other IRQs may cause a
new IRQ10 to be executed delayed (because IRQs are disabled during IRQ
handling), to avoid that problem: Best don't enable any other IRQs except IRQ0
and IRQ10, or, if you need other IRQs, best have them enabled only during
Vblank (there are no scanlines drawn during vblank, so IRQ10 should never
trigger during that period). DMAs might also slow down IRQ execution, so best
use them only during Vblank, too.<br/>

#### IRQ10 Timer Reading
To read the current timer values the IRQ10 handler would be required to be
called \<immediately\> after receiving the IRQ10 signal, which is more or
less impossible; if the main program is trying to read a mul/div/gte result
while the mul/div/gte operation is still busy may stop the CPU for some dozens
of clock cycles, and active DMA transfers or cache hits and misses in the IRQ
handler may cause different timings, moreover, timings may become completely
different if IRQs are disabled (eg. while another IRQ is processed).<br/>
However, IRQ10 does also get triggered in the next some scanlines, so the first
IRQ10 is used only as a notification that the CPU should watch out for further
IRQ10's. Ie. the IRQ10 handler should disable all DMAs, acknowledge IRQ10, and
then enter a waitloop that waits for the IRQ10 bit in I\_STAT to become set
again (or abort if a timeout occurs) and then read the timers, reportedly like
so:<br/>
```
  IF NTSC then X=(Timer0-140)*0.198166, Y=Timer1
  IF PAL  then X=(Timer0-140)*0.196358, Y=Timer1
```
No idea why PAL/NTSC should use different factors, that factors are looking
quite silly/bugged, theoretically, the pixel-to-clock ratio should be the
exactly same for PAL and NTSC...?<br/>
Mind that reading Timer values in Dotclock/Hblank mode is unstable, for Timer1
this can be fixed by the read-retry method, for Timer0 this could be done too,
but one would need to subtract the retry-time to get a correct coordinate;
alternately Timer0 can run at system clock (which doesn't require read-retry),
but it must be then converted to video clock (mul 11, div 7), and then from
video clock to dot clock (eg. div 8 for 320-pixel mode).<br/>
Above can be repeated for the next some scanlines (allowing to take the medium
values as result, and/or to eliminate faulty values which are much bigger or
smaller than the other values). Once when you have collected enough values,
disable IRQ10, so it won't trigger on further scanlines within the current
frame.<br/>

#### IRQ10 Bugs
BUG: The "libgun" library doesn't acknowledge the old IRQ10 \<immediately\>
before waiting for a new IRQ10, so the timer values after sensing the new IRQ10
are somewhat random (especially for the first processed scanline) (the library
allows to read further IRQ10's in further scanlines, which return more stable
results).<br/>
No idea how many times IRQ10 gets typically repeated? Sporting Clays allocates
a buffer for up to 20 scanlines (which would cause pretty much of a slowdown
since the CPU is just waiting during that period) (nethertheless, the game uses
only the first timer values, ie. the bugged libgun-random values).<br/>

Unknown if/how two-player games (with 2 lightguns) are working with the IRQ10
method... if IRQ10 is generated ONLY after pressing the trigger button, then it
may work, unless both players have Trigger pressed at the same time... and,
maybe one can enable/disable the lightguns by whatever commmand being sent to
the controller (presumably that "x0h" byte, see above), so that gun 1 generates
IRQ10 only in each second frame, and gun 2 only in each other frame...?<br/>
