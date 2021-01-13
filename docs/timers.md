#   Timers
#### 1F801100h+N\*10h - Timer 0..2 Current Counter Value (R/W)
```
  0-15  Current Counter value (incrementing)
  16-31 Garbage
```
This register is automatically incrementing. It is write-able (allowing to set
it to any value). It gets forcefully reset to 0000h on any write to the Counter
Mode register, and on counter overflow (either when exceeding FFFFh, or when
exceeding the selected target value).<br/>

#### 1F801104h+N\*10h - Timer 0..2 Counter Mode (R/W)
```
  0     Synchronization Enable (0=Free Run, 1=Synchronize via Bit1-2)
  1-2   Synchronization Mode   (0-3, see lists below)
         Synchronization Modes for Counter 0:
           0 = Pause counter during Hblank(s)
           1 = Reset counter to 0000h at Hblank(s)
           2 = Reset counter to 0000h at Hblank(s) and pause outside of Hblank
           3 = Pause until Hblank occurs once, then switch to Free Run
         Synchronization Modes for Counter 1:
           Same as above, but using Vblank instead of Hblank
         Synchronization Modes for Counter 2:
           0 or 3 = Stop counter at current value (forever, no h/v-blank start)
           1 or 2 = Free Run (same as when Synchronization Disabled)
  3     Reset counter to 0000h  (0=After Counter=FFFFh, 1=After Counter=Target)
  4     IRQ when Counter=Target (0=Disable, 1=Enable)
  5     IRQ when Counter=FFFFh  (0=Disable, 1=Enable)
  6     IRQ Once/Repeat Mode    (0=One-shot, 1=Repeatedly)
  7     IRQ Pulse/Toggle Mode   (0=Short Bit10=0 Pulse, 1=Toggle Bit10 on/off)
  8-9   Clock Source (0-3, see list below)
         Counter 0:  0 or 2 = System Clock,  1 or 3 = Dotclock
         Counter 1:  0 or 2 = System Clock,  1 or 3 = Hblank
         Counter 2:  0 or 1 = System Clock,  2 or 3 = System Clock/8
  10    Interrupt Request       (0=Yes, 1=No) (Set after Writing)    (W=1) (R)
  11    Reached Target Value    (0=No, 1=Yes) (Reset after Reading)        (R)
  12    Reached FFFFh Value     (0=No, 1=Yes) (Reset after Reading)        (R)
  13-15 Unknown (seems to be always zero)
  16-31 Garbage (next opcode)
```
In one-shot mode, the IRQ is pulsed/toggled only once (one-shot mode doesn't
stop the counter, it just suppresses any further IRQs until a new write to the
Mode register occurs; if both IRQ conditions are enabled in Bit4-5, then
one-shot mode triggers only one of those conditions; whichever occurs first).<br/>
Normally, Pulse mode should be used (Bit10 is permanently set, except for a few
clock cycles when an IRQ occurs). In Toggle mode, Bit10 is set after writing to
the Mode register, and becomes inverted on each IRQ (in one-shot mode, it
remains zero after the IRQ) (in repeat mode it inverts Bit10 on each IRQ, so
IRQ4/5/6 are triggered only each 2nd time, ie. when Bit10 changes from 1 to 0).<br/>
The "free run" mode is simply saying that the counter will not reset at a given threshold value.

#### 1F801108h+N\*10h - Timer 0..2 Counter Target Value (R/W)
```
  0-15  Counter Target value
  16-31 Garbage
```
When the Target flag is set (Bit3 of the Control register), the counter
increments up to (including) the selected target value, and does then restart
at 0000h.<br/>

#### Dotclock/Hblank
For more info on dotclock and hblank timings, see:<br/>
[GPU Timings](graphicsprocessingunitgpu.md#gpu-timings)<br/>
Caution: Reading the Current Counter Value can be a little unstable (when using
dotclk or hblank as clock source); the GPU clock isn't in sync with the CPU
clock, so the timer may get changed during the CPU read cycle. As a workaround:
repeat reading the timer until the received value is the same (or slightly
bigger) than the previous value.<br/>



