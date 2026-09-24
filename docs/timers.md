#   Timers
The CPU is equipped with three 16-bit timers or "root counters":

- timer 0, mapped at `0x1f801100` and clocked by either the system clock or the
  GPU's pixel clock;
- timer 1, mapped at `0x1f801110` and clocked by either the system clock or the
  GPU's horizontal blank signal;
- timer 2, mapped at `0x1f801120` and always running from the system clock, but
  with an optional prescaler to divide it by 8.

Official register and bit names can be found in `timerman.h` in Sony's PS2 IOP
SDK.

#### `0x1f801100 + 0x10*N`: `COUNT`
```
  0-15  Current Counter value (incrementing)
  16-31 Garbage
```
This register is automatically incrementing. It is write-able (allowing to set
it to any value). It gets forcefully reset to 0000h on any write to the Counter
Mode register and when reaching counter overflow condition (either when reaching
FFFFh, or when reaching the selected target value).

Writing a Current value larger than the Target value will not trigger the
condition of Mode CMP, but make the counter run until FFFFh and wrap around to
0000h once, before using the target value.

#### `0x1f801104 + 0x10*N`: `MODE`
```
  0     GATF  Synchronization Enable (0=Free Run, 1=Synchronize via GATM)
  1-2   GATM  Synchronization Mode   (0-3, see lists below)
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
  3     ZRET  Reset counter to 0000h    (0=After Counter=FFFFh, 1=After Counter=COMP)
  4     CMP   IRQ when Counter=COMP     (0=Disable, 1=Enable)
  5     OVFL  IRQ when Counter=FFFFh    (0=Disable, 1=Enable)
  6     REPT  IRQ Once/Repeat Mode      (0=One-shot, 1=Repeatedly)
  7     LEVL  IRQ Pulse/Toggle Mode     (0=Short INTF=0 Pulse, 1=Toggle INTF on/off)
  8     EXTC  (Timers 0/1) Clock Source (0=System Clock, 1=Dotclock/Hblank)
  9     PSCL  (Timer 2) Prescaler       (0=Divide by 1, 1=Divide by 8)
  10    INTF  Interrupt Request         (0=Yes, 1=No) (Set after Writing)    (W=1) (R)
  11    EQUF  Reached COMP Value        (0=No, 1=Yes) (Reset after Reading)        (R)
  12    OVFF  Reached FFFFh Value       (0=No, 1=Yes) (Reset after Reading)        (R)
  13-15       Unused/zero               ("NTPS" on PS2 IOP)
  16-31       Garbage (next opcode)
```
In one-shot mode, the IRQ is pulsed/toggled only once (one-shot mode doesn't
stop the counter, it just suppresses any further IRQs until a new write to the
Mode register occurs; if both IRQ conditions are enabled in Bit4-5, then
one-shot mode triggers only one of those conditions; whichever occurs first).

Normally, Pulse mode should be used (INTF is permanently set, except for a few
clock cycles when an IRQ occurs). In Toggle mode, INTF is set after writing to
the Mode register, and becomes inverted on each IRQ (in one-shot mode, it
remains zero after the IRQ) (in repeat mode it inverts INTF on each IRQ, so
IRQ4/5/6 are triggered only each 2nd time, ie. when INTF changes from 1 to 0).

The "free run" mode is simply saying that the counter will not reset at a given
threshold value.

#### `0x1f801108 + 0x10*N`: `COMP` / `TARGET`
```
  0-15  Counter Target value
  16-31 Garbage
```
When the ZRET flag is set, the counter increments up to (including) the selected
target value, and does then restart at 0000h. PS2 IOP documentation calls this
register `COMP` but symbol names in PS1 libraries refer to it as `TARGET`.

#### Dotclock/Hblank
For more info on dotclock and hblank timings, see:

[GPU Timings](graphicsprocessingunitgpu.md#gpu-timings)

Caution: Reading the Current Counter Value can be a little unstable (when using
dotclk or hblank as clock source); the GPU clock isn't in sync with the CPU
clock, so the timer may get changed during the CPU read cycle. As a workaround:
repeat reading the timer until the received value is the same (or slightly
bigger) than the previous value.

#### Reset and Wrap
When resetting the Counter by writing the Mode register, it will stay at 0000h
for 2 clock cycles before counting up.

When writing the Current value, it will stay at the written value for 2 clock
cycles before counting up or checking against Target overflows.

When wrapping around at FFFFh (ZRET not set), it will stay at 0000h for only
1 clock cycle.

When being reset to 0000h by reaching the Target value (ZRET set), it will
stay at 0000h for 2 clock cycles.

Example behavior with COMP Value of 0001h and ZRET set:
```
clock cycle 0 - Counter Value = 0000h
clock cycle 1 - Counter Value = 0000h
clock cycle 2 - Counter Value = 0001h
clock cycle 3 - Counter Value = 0000h
clock cycle 4 - Counter Value = 0000h
clock cycle 5 - Counter Value = 0001h
```
