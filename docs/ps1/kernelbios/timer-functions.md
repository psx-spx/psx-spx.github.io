#   Timer Functions
#### Timers (aka Root Counters)
The three hardware timers aren't internally used by any BIOS functions, so they
can be freely used by the game, either via below functions, or via direct I/O
access.<br/>

#### Vblank
Some of the below functions are allowing to use Vblank IRQs as a fourth
"timer". However, Vblank IRQs are internally used by the BIOS for handling
joypad and memory card accesses. One could theoretically use two separate
Vblank IRQ handlers, one for joypad, and one as "timer", but the BIOS is much
too unstable for such "shared" IRQ handling (it may occassionally miss one of
the two handlers).<br/>
So, although Vblank IRQs are most important for games, the PSX BIOS doesn't
actually allow to use them for purposes other than joypad access. A possible
workaround is to examine the status byte in one of the joypad buffers (ie. the
InitPAD2(buf1,22h,buf2,22h) buffers). Eg. a wait\_for\_vblank function could look
like so: set buf1[0]=55h, then wait until buf1[0]=00h or buf1[0]=FFh.<br/>

#### B(02h) - init\_timer(t,reload,flags)
When t=0..2, resets the old timer mode by setting [1F801104h+t\*16]=0000h,
applies the reload value by [1F801108h+t\*16]=reload, computes the new mode:<br/>
```
  if flags.bit4=0 then mode=0048h else mode=0049h
  if flags.bit0=0 then mode=mode OR 100h
  if flags.bit12=1 then mode=mode OR 10h
```
and applies it by setting [1F801104h+t\*16]=mode, and returns 1. Does nothing
and returns zero for t\>2.<br/>

#### B(03h) - get\_timer(t)
Reads the current timer value: Returns halfword[1F801100h+t\*16] for t=0..2.
Does nothing and returns zero for t\>2.<br/>

#### B(04h) - enable\_timer\_irq(t)
#### B(05h) - disable\_timer\_irq(t)
Enables/disables timer or vblank interrupt enable bits in [1F801074h], bit4,5,6
for t=0,1,2, or bit0 for t=3, or random/garbage bits for t\>3. The enable
function returns 1 for t=0..2, and 0 for t=3. The disable function returns
always 1.<br/>

#### B(06h) - restart\_timer(t)
Sets the current timer value to zero: Sets [1F801100h+t\*16]=0000h and returns 1
for t=0..2. Does nothing and returns zero for t\>2.<br/>

#### C(0Ah) - ChangeClearRCnt(t,flag) ;root counter (aka timer)
Selects what the kernel's timer/vblank IRQ handlers shall do after they have
processed an IRQ (t=0..2: timer 0..2, or t=3: vblank) (flag=0: do nothing; or
flag=1: automatically acknowledge the IRQ and immediately return from
exception). The function returns the old (previous) flag value.<br/>
