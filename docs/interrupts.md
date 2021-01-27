#   Interrupts
#### 1F801070h I\_STAT - Interrupt status register (R=Status, W=Acknowledge)
#### 1F801074h I\_MASK - Interrupt mask register (R/W)
Status: Read I\_STAT (0=No IRQ, 1=IRQ)<br/>
Acknowledge: Write I\_STAT (0=Clear Bit, 1=No change)<br/>
Mask: Read/Write I\_MASK (0=Disabled, 1=Enabled)<br/>
```
  0     IRQ0 VBLANK (PAL=50Hz, NTSC=60Hz)
  1     IRQ1 GPU   Can be requested via GP0(1Fh) command (rarely used)
  2     IRQ2 CDROM
  3     IRQ3 DMA
  4     IRQ4 TMR0  Timer 0 aka Root Counter 0 (Sysclk or Dotclk)
  5     IRQ5 TMR1  Timer 1 aka Root Counter 1 (Sysclk or H-blank)
  6     IRQ6 TMR2  Timer 2 aka Root Counter 2 (Sysclk or Sysclk/8)
  7     IRQ7 Controller and Memory Card - Byte Received Interrupt
  8     IRQ8 SIO
  9     IRQ9 SPU
  10    IRQ10 Controller - Lightpen Interrupt. Also shared by PIO and DTL cards.
  11-15 Not used (always zero)
  16-31 Garbage
```

#### Secondary IRQ10 Controller (Port 1F802030h)
[EXP2 DTL-H2000 I/O Ports](expansionportpio.md#exp2-dtl-h2000-io-ports)<br/>

#### Interrupt Request / Execution
The interrupt request bits in I\_STAT are edge-triggered, ie. the get set ONLY
if the corresponding interrupt source changes from "false to true".<br/>
If one or more interrupts are requested and enabled, ie. if "(I\_STAT AND
I\_MASK)=nonzero", then cop0r13.bit10 gets set, and when cop0r12.bit10 and
cop0r12.bit0 are set, too, then the interrupt gets executed.<br/>

#### Interrupt Acknowledge
To acknowledge an interrupt, write a "0" to the corresponding bit in I\_STAT.
Most interrupts (except IRQ0,4,5,6) must be additionally acknowledged at the
I/O port that has caused them (eg. JOY\_CTRL.bit4).<br/>
Observe that the I\_STAT bits are edge-triggered (they get set only on
High-to-Low, or False-to-True edges). The correct acknowledge order is:<br/>
```
  First, acknowledge I_STAT                (eg. I_STAT.bit7=0)
  Then, acknowledge corresponding I/O port (eg. JOY_CTRL.bit4=1)
```
When doing it vice-versa, the hardware may miss further IRQs (eg. when first
setting JOY\_CTRL.4=1, then a new IRQ may occur in JOY\_STAT.4 within a single
clock cycle, thereafter, setting I\_STAT.7=0 would successfully reset I\_STAT.7,
but, since JOY\_STAT.4 is already set, there'll be no further edge, so I\_STAT.7
won't be ever set in future).<br/>

#### COP0 Interrupt Handling
Relevant COP0 registers are cop0r13 (CAUSE, reason flags), and cop0r12 (SR,
control flags), and cop0r14 (EPC, return address), and, cop0cmd=10h (aka RFE
opcode) is used to prepare the return from interrupts. For more info, see<br/>
[COP0 - Exception Handling](cpuspecifications.md#cop0-exception-handling)<br/>

#### PSX specific COP0 Notes
COP0 has six hardware interrupt bits, of which, the PSX uses only cop0r13.bit10
(the other ones, cop0r13.bit11-15 are always zero). cop0r13.bit10 is NOT a
latch, ie. it gets automatically cleared as soon as "(I\_STAT AND I\_MASK)=zero",
so there's no need to do an acknowledge at the cop0 side. COP0 additionally has
two software interrupt bits, cop0r13.bit8-9, which do exist in the PSX, too,
these bits are read/write-able latches which can be set/cleared manually to
request/acknowledge exceptions by software.<br/>

#### Halt Function (Wait for Interrupt)
The PSX doesn't have a HALT opcode, so, even if the program is merely waiting
for an interrupt to occur, the CPU is always running at full speed, which is
resulting in high power consumption, and, in case of emulators, high CPU
emulation load. To save energy, and to make emulation smoother on slower
computers, I've added a Halt function for use in emulators:<br/>
[EXP2 Nocash Emulation Expansion](expansionportpio.md#exp2-nocash-emulation-expansion)<br/>
