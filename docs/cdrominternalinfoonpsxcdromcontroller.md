#   CDROM Internal Info on PSX CDROM Controller
PSX software can access the CDROM via Port 1F801800h..1F801803h (as described
in the previous chapters). The following chapters describe the inner workings
of the PSX CDROM controller - this information is here for curiosity only -
normally PSX software cannot gain control of those lower-level stuff (although
some low level registers can be manipulated via Test commands, but that will
usually conflict with normal operation).<br/>

#### Motorola MC68HC05 (8bit single-chip CPU)
The Playstation CDROM drive is controlled by a MC68HC05 8bit CPU with on-chip
I/O ports and on-chip BIOS ROM. There is no way to reprogram that BIOS, nor to
tweak it to execute custom code in RAM.<br/>
[CDROM Internal HC05 Instruction Set](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-hc05-instruction-set)<br/>
[CDROM Internal HC05 On-Chip I/O Ports](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-hc05-on-chip-io-ports)<br/>
[CDROM Internal HC05 I/O Port Usage in PSX](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-hc05-io-port-usage-in-psx)<br/>
[CDROM Internal HC05 Motorola Selftest Mode](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-hc05-motorola-selftest-mode)<br/>
The PSX can read HC05 I/O Ports and RAM via Test Commands:<br/>
[CDROM - Test Commands - Read HC05 SUB-CPU RAM and I/O Ports](cdromdrive.md#cdrom-test-commands-read-hc05-sub-cpu-ram-and-io-ports)<br/>

#### Decoder/FIFO (CXD1199BQ or CXD1815Q)
This chip handles error correction and ADPCM decoding, and acts as some sort of
FIFO interface between main/sub CPUs and incoming cdrom sector data. On the
MIPS Main CPU it is controlled via Port 1F801800h..1F801803h.<br/>
[CDROM Controller I/O Ports](cdromdrive.md#cdrom-controller-io-ports)<br/>
On the HC05 Sub CPU it is controlled via Port A (data in/out), Port E
(address/index), and Port D (read/write/select signals); the HC05 doesn't have
external address/data bus, so one must manually access the CXD1815Q via those
ports.<br/>
[CDROM Internal CXD1815Q Sub-CPU Configuration Registers](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-cxd1815q-sub-cpu-configuration-registers)<br/>
[CDROM Internal CXD1815Q Sub-CPU Sector Status Registers](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-cxd1815q-sub-cpu-sector-status-registers)<br/>
[CDROM Internal CXD1815Q Sub-CPU Address Registers](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-cxd1815q-sub-cpu-address-registers)<br/>
[CDROM Internal CXD1815Q Sub-CPU Misc Registers](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-cxd1815q-sub-cpu-misc-registers)<br/>
The PSX can read/write the Decoder I/O Ports and SRAM via Test commands:<br/>
[CDROM - Test Commands - Read/Write Decoder RAM and I/O Ports](cdromdrive.md#cdrom-test-commands-readwrite-decoder-ram-and-io-ports)<br/>
The sector buffer used in the PSX is 32Kx8 SRAM. Old PU-7 boards are using
CXD1199BQ chips, later boards are using CXD1815Q, and even later boards have
the stuff intergrated in the SPU. Note: The CXD1199BQ/CXD1815Q are about 99%
same as described in CXD1199AQ datasheet.<br/>

#### Signal Processor and Servo Amplifier
Older PSX mainboards are using two separate chips:<br/>
[CDROM Internal Commands CX(0x..3x) - CXA1782BR Servo Amplifier](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-commands-cx0x3x-cxa1782br-servo-amplifier)<br/>
[CDROM Internal Commands CX(4x..Ex) - CXD2510Q Signal Processor](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-commands-cx4xex-cxd2510q-signal-processor)<br/>
Later PSX mainboards have the above intergrated in a single chip, with some
extended features:<br/>
[CDROM Internal Commands CX(0x..Ex) - CXD2545Q Servo/Signal Combo](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-commands-cx0xex-cxd2545q-servosignal-combo)<br/>
Later version is CXD1817R (Servo/Signal/Decoder Combo).<br/>
Even later PSX mainboards have it integrated in the Sound Chip: CXD2938Q
(SPU+CDROM) with some changed bits and New SCEx transfer:<br/>
[CDROM Internal Commands CX(0x..Ex) - CXD2938Q Servo/Signal/SPU Combo](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-commands-cx0xex-cxd2938q-servosignalspu-combo)<br/>
Finally, PM-41(2) boards are using a CXD2941R chip (SPU+CDROM+SPU\_RAM), unknown
if/how far the CDROM part of that chip differs from CXD2938Q.<br/>
Some general notes:<br/>
[CDROM Internal Commands CX(xx) - Notes](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-commands-cxxx-notes)<br/>
[CDROM Internal Commands CX(xx) - Summary of Used CX(xx) Commands](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-commands-cxxx-summary-of-used-cxxx-commands)<br/>
The PSX can manipulate the CX(..) registers via some test commands:<br/>
[CDROM - Test Commands - Test Drive Mechanics](cdromdrive.md#cdrom-test-commands-test-drive-mechanics)<br/>
Note: Datasheets for CXD2510Q/CXA1782BR/CXD2545Q do exist.<br/>

#### CDROM Pinouts
[Pinouts - DRV Pinouts](pinouts.md#pinouts-drv-pinouts)<br/>
[Pinouts - HC05 Pinouts](pinouts.md#pinouts-hc05-pinouts)<br/>



##   CDROM Internal HC05 Instruction Set
#### ALU, Load/Store, Jump/Call
```
  Opcode      Clk HINZC Name Syntax
  x6 ...      2-5 --NZ- LDA  MOV  A,<op>      ;A=op
  xE ...      2-5 --NZ- LDX  MOV  X,<op>      ;X=op
  x7 ...      4-6 --NZ- STA  MOV  <op>,A      ;op=A
  xF ...      4-6 --NZ- STX  MOV  <op>,X      ;op=X
  xC ...      2-4 ----- JMP  JMP  <op>        ;PC=op
  xD ...      5-7 ----- JSR  CALL <op>        ;[SP]=PC, PC=op
  xB ...      2-5 H-NZC ADD  ADD  A,<op>      ;A=A+op
  x9 ...      2-5 H-NZC ADC  ADC  A,<op>      ;A=A+op+C
  x0 ...      2-5 --NZC SUB  SUB  A,<op>      ;A=A-op
  x2 ...      2-5 --NZC SBC  SBC  A,<op>      ;A=A-op-C
  x4 ...      2-5 --NZ- AND  AND  A,<op>      ;A=A AND op
  xA ...      2-5 --NZ- ORA  OR   A,<op>      ;A=A OR op
  x8 ...      2-5 --NZ- EOR  XOR  A,<op>      ;A=A XOR op
  x1 ...      2-5 --NZC CMP  CMP  A,<op>      ;A-op
  x3 ...      2-5 --NZC CPX  CMP  X,<op>      ;X-op
  x5 ...      2-5 --NZ- BIT  TEST A,<op>      ;A AND op
  A7,AF,AC = Reserved (no STA/STX/JMP with immediate operand)
```
Operands can be...<br/>
```
  Opcode      Clk ALU/LDA/LDX      Clk STA/STX          Clk JMP/CALL
  Ax nn         2 cmd r,nn           - N/A              -/6 call relative (BSR)
  Bx nn         3 cmd r,[nn]         4 mov [nn],r       2/5 cmd nn
  Cx nn mm      4 cmd r,[nnmm]       5 mov [nnmm],r     3/6 cmd nnmm
  Dx nn mm      5 cmd r,[X+nnmm]     6 mov [X+nnmm],r   4/7 cmd X+nnmm
  Ex nn         4 cmd r,[X+nn]       5 mov [X+nn],r     3/6 cmd X+nn
  Fx            3 cmd r,[X]          4 mov [X],r        2/5 cmd X
```

#### Read-Modify-Write
```
  Opcode      Clk HINZC Name Syntax
  xC ...      3-6 --NZ- INC  INC op      ;increment   ;op=op+1
  xA ...      3-6 --NZ- DEC  DEC op      ;decrement   ;op=op-1
  xF ...      3-6 --01- CLR  ??  op,00h  ;clear       ;op=op AND 00h
  x3 ...      3-6 --NZ1 COM  NOT op      ;complement  ;op=op XOR FFh
  x0 ...      3-6 --NZC NEG  NEG op      ;negate      ;op=00h-op
  x9 ...      3-6 --NZC ROL  RCL op      ;rotate left through carry
  x6 ...      3-6 --NZC ROR  RCR op      ;rotate right through carry
  x8 ...      3-6 --NZC LSL  SHL op      ;shift left logical
  x4 ...      3-6 --0ZC LSR  SHR op      ;shift right logical
  x7 ...      3-6 --NZC ASR  SAR op      ;shift right arithmetic
  xD ...      3-5 --NZ- TST  TEST op,FFh ;test for negative or zero (AND FFh?)
  x1,x2,x5,xB,xE = Reserved (except for: 42 = MUL)
```
Operands can be...<br/>
```
  Opcode      Clk RMW          Clk CLR                Clk TST
  3x nn         5 cmd [nn]       5 MOV [nn],00h         4 TEST [nn],0FFh
  4x            3 cmd A          3 MOV A,00h,slow       3 TEST A,0FFh,slow
  5x            3 cmd X          3 MOV X,00h,slow       3 TEST X,0FFh
  6x nn         6 cmd [X+nn]     6 MOV [X+nn],00h       5 TEST [X+nn],0FFh
  7x            5 cmd [X]        5 MOV [X],00h          4 TEST [X],0FFh
```
CLR includes a dummy-read-cycle, whilst TST does omit the dummy-write cycle.<br/>
The ",slow" RMW opcodes are smaller, but slower than equivalent ALU opcodes.<br/>

#### Bit Manipulation and Bit Test with Relative Jump (to $+3+/-dd)
```
  Opcode      Clk HINZC Name  Syntax
  00h+i*2 nn dd 5 ----C BRSET JNZ [nn].i,dest  ;C=[nn].i, branch if set
  01h+i*2 nn dd 5 ----C BRCLR JZ  [nn].i,dest  ;C=[nn].i, branch if clear
  10h+i*2 nn    5 ----- BSET  SET [nn].i       ;set [nn].i
  11h+i*2 nn    5 ----- BCLR  RES [nn].i       ;clear [nn].i
```

#### Branch (Relative jump to $+2+/-nn)
```
  Opcode      Clk HINZC Name    Syntax
  20 nn         3 ----- BRA     JR  nn      ;branch always
  21 nn         3 ----- BRN     NUL nn      ;branch never
  22 nn         3 ----- BHI     JA  nn      ;if C=0 and Z=0, higher        ?
  23 nn         3 ----- BLS     JBE nn      ;if C=1 or Z=1, lower or same  ?
  24 nn         3 ----- BCC/BHS JNC/JAE nn  ;if C=0, carry clear, higher.same
  25 nn         3 ----- BCS/BLO JC/JB nn    ;if C=1, carry set, lower
  26 nn         3 ----- BNE     JNZ/JNE nn  ;if Z=0, not equal / not zero
  27 nn         3 ----- BEQ     JZ/JE nn    ;if Z=1, equal / zero
  28 nn         3 ----- BHCC    JNH nn      ;if H=0, half-carry clear
  29 nn         3 ----- BHCS    JH  nn      ;if H=1, half-carry set
  2A nn         3 ----- BPL     JNS nn      ;if S=0, plus / not signed
  2B nn         3 ----- BMI     JS  nn      ;if S=1, minus / signed
  2C nn         3 ----- BMC     JEI nn      ;if I=0, interrupt mask clear
  2D nn         3 ----- BMS     JDI nn      ;if I=1, interrupt mask set
  2E nn         3 ----- BIL     JIL nn      ;if XX=LO, interrupt line low
  2F nn         3 ----- BIH     JIH nn      ;if XX=HI, interrupt line high
  AD nn         6 ----- BSR     CALL relative nn  ;branch to subroutine always
```

#### Control/Misc
```
  Opcode      Clk HINZC Name Syntax
  9D            2 ----- NOP  NOP            ;no operation
  97            2 ----- TAX  MOV X,A        ;transfer A to X
  9F            2 ----- TXA  MOV A,X        ;transfer X to A
  9C            2 ----- RSP  MOV SP,00FFh   ;reset stack pointer (SP=00FFh)
  42           11 0---0 MUL  MUL X,A        ;X:A=X*A (unsigned multiply)
  81            6 ----- RTS  RET            ;return from subroutine
  80            9 xxxxx RTI  RETI           ;return from interrupt
  99            2 ----1 SEC  STC            ;set carry flag
  98            2 ----0 CLC  CLC            ;clear carry flag
  9B            2 -1--- SEI  DI             ;set interrupt mask (disable ints)
  9A            2 -0--- CLI  EI             ;clear interrupt mask (enable ints)
  8E          ..2 -0--- STOP STOP           ;?
  8F          ..2 -0--- WAIT WAIT           ;?
  83           10 -1--- SWI  SWI            ;software interrupt ...? PC=[FFFCh]
  <IRQ>         ? ????? Interrupt           ;?                       PC=[FFFxh]
  <RESET>       ? ????? Reset               ;?                       PC=[FFFEh]
  82,84..8D,90..96,9E = Reserved
```
MUL isn't supported in original "M146805 CMOS" family (MUL is used/supported in
PSX cdrom controller).<br/>

#### Registers
```
  A   8bit  accumulator
  X   8bit  index register
  SP  6bit  stack pointer (range 00C0h..00FFh)
  PC  16bit program pointer (range 0000h..FFFFh)
  CCR 5bit  condition code register (flags) (111HINZC)
```

#### Pushed on IRQ are:
```
  SP.highest PC.lo
             PC.hi
             X
             A
  SP.lowest  Flags (CCR, 5bit condition code register) (111HINZC)
```

#### Addressing Modes
```
  nn       immediate             ;00h..FFh
  [nn]     direct address        ;[0000h..00FFh]
  [nnmm]   extended address      ;[0000h..FFFFh]
  [X]      indexed, no offset    ;[0000h..00FFh]
  [X+nn]   indexed, 8bit offset  ;[0000h..01FEh]
  [X+nnmm] indexed, 16bit offset ;[0000h..FFFFh]
  [nn].i   bit                   ;[0000h..00FFh].bit0..7
  dd       relative              ;$+2..3+(-80h..+7Fh)
```
Notes:<br/>
```
  operand "X+nn" performs an unsigned addition, and can address 0000h..01FEh.
  16bit operands (nnmm) are encoded in BIG-ENDIAN format (same for pushed PC).
```

#### Exception Vectors
Exception vectors are 16bit BIG-ENDIAN values at FFF0h-FFFFh (or at FFE0h-FFEFh
when running in Motorola Bootstrap mode).<br/>
```
  Vector Prio Usage
  FFF0h  7=lo TBI Vector (Timebase)
  FFF2h  6    SSPI Vector (SPI bus)     (SPI1 and SPI2)
  FFF4h  5    Timer 2 Interrupt Vector  (Timer 2 Input/Compare)
  FFF6h  4    Timer 1 Interrupt Vector  (Timer 1 Input/Compare/Overflow)
  FFF8h  3    KWI Vector (Key Wakeup)   (KWI0..7 pins)
  FFFAh  2    External Interrupt Vector (/IRQ1 and /IRQ2 pins)
  FFFCh  none Software Interrupt Vector (SWI opcode)            ;\regardless of
  FFFEh  1=hi Reset Vector              (/RESET signal and COP) ;/CPU's "I"
```

#### Directives/Pseudos (used by a22i assembler; in no$psx utility menu)
```
  .hc05         select HC05 instruction set (default would be .mips)
  .nocash       select nocash syntax (default would be .native opcode names)
  db ...        define 8bit byte(s), or quoted ascii strings
  dw ...        define 16bit word(s) in BIG ENDIAN (for HC05 exception vectors)
  org nnnn      change origin for following opcodes
  end           end of file
  mov c,[nn].i  alias for "jnz [nn].i,$+3" (dummy jump & set carry=[nn].i)
```



##   CDROM Internal HC05 On-Chip I/O Ports
#### HC05 Port 3Eh - MISC - Miscellaneous Register (R/W)
```
  0    OPTM  Option Map Select (bank-switching for Port 00h..0Fh)
  1    FOSCE Fast (Main) Oscillator Enable (0=Disable OSC, 1=Normal)
  2-3  SYS   System Clock Select (0=OSC/2, 1=OSC/4, 2=OSC/64, 3=XOSC/2)
  4-5  -     Not used (0)
  6    STUP  XOSC Time Up Flag   (R)
  7    FTUP  OSC Time Up Flag    (R)   (0=Busy, 1=Ready/Good/Stable)
```
Note: For PSX, OSC is 4.0000MHz (PU-7/PU-8), 4.2336MHz (PU-18 and up). SysClk
is usually set to OSC/2, ie. around 2MHz.<br/>

#### HC05 Port OPTM=0:00h - PORTA - Port A Data Register (R/W)
#### HC05 Port OPTM=0:01h - PORTB - Port B Data Register (R)
#### HC05 Port OPTM=0:02h - PORTC - Port C Data Register (R/W)
#### HC05 Port OPTM=0:03h - PORTD - Port D Data Register (R/W)
#### HC05 Port OPTM=0:04h - PORTE - Port E Data Register (R/W)
#### HC05 Port OPTM=0:05h - PORTF - Port F Data Register (R) (undoc: R/W)
These are general purpose I/O ports (controlling external pins). Some ports are
Input-only, and some can be optionally used for special things (like IRQs,
SPI-bus, or as Timer input/output).<br/>
```
  PA.0-7  PAn   Port A Bit0..7 Input/Output            (0=Low, 1=High) (R/W)
  PB.0-7  PBn   Port B Bit0..7 Input        /KWI0..7   (0=Low, 1=High) (R)
  PC.0    PC0   Port C Bit0    Input/Output /SDI1 (SPI)(0=Low, 1=High) (R/W)
  PC.1    PC1   Port C Bit1    Input/Output /SDO1 (SPI)(0=Low, 1=High) (R/W)
  PC.2    PC2   Port C Bit2    Input/Output /SCK1 (SPI)(0=Low, 1=High) (R/W)
  PC.3    PC3   Port C Bit3    Input/Output /TCAP (T1) (0=Low, 1=High) (R/W)
  PC.4    PC4   Port C Bit4    Input/Output /EVI  (T2) (0=Low, 1=High) (R/W)
  PC.5    PC5   Port C Bit5    Input/Output /EVO  (T2) (0=Low, 1=High) (R/W)
  PC.6    PC6   Port C Bit6    Input/Output /IRQ2      (0=Low, 1=High) (R/W)
  PC.7    PC7   Port C Bit7    Input/Output /IRQ1      (0=Low, 1=High) (R/W)
  PD.0-7  PDn   Port D Bit0..7 Input/Output            (0=Low, 1=High) (R/W)
  PE.0-7  PEn   Port E Bit0..7 Input/Output            (0=Low, 1=High) (R/W)
  PF.0-7  PFn   Port F Bit0..7 Input/Undoc  A/D-input  (0=Low, 1=High) (R)(R/W)
```

#### HC05 Port OPTM=1:00h - DDRA - Port A Data Direction Register (R/W)
#### HC05 Port OPTM=1:02h - DDRC - Port C Data Direction Register (R/W)
#### HC05 Port OPTM=1:03h - DDRD - Port D Data Direction Register (R/W)
#### HC05 Port OPTM=1:04h - DDRE - Port E Data Direction Register (R/W)
#### HC05 Port OPTM=1:05h - DDRF - Port F Data Direction Register (undoc)
```
  DDRX.0-7  DDRXn Port X Data Direction Bit0..7 (0=Input, 1=Output) (R/W)
```
Officially, there are no DDRB and DDRF registers (Port B and F are always
Inputs). Although, actually, Motorola's Bootstrap RAM \<does\> manipulate
DDRF.<br/>

#### HC05 Port OPTM=1:08h - RCR1 - Resistor Control Register 1 (R/W)
#### HC05 Port OPTM=1:09h - RCR2 - Resistor Control Register 2 (R/W)
```
  RCR1.0    RAL   Port A.Bit0-3 Pullup Resistors (0=Off, 1=On)
  RCR1.1    RAH   Port A.Bit4-7 Pullup Resistors (0=Off, 1=On)
  RCR1.2    RBL   Port B.Bit0-3 Pullup Resistors (0=Off, 1=On)
  RCR1.3    RBH   Port B.Bit4-7 Pullup Resistors (0=Off, 1=On)
  RCR1.4    RGL   Port G.Bit0-3 Pullup Resistors (0=Off, 1=On) ;\
  RCR1.5    RGH   Port G.Bit4-7 Pullup Resistors (0=Off, 1=On) ; on chips
  RCR1.6    RHL   Port H.Bit0-3 Pullup Resistors (0=Off, 1=On) ; with Port G,H
  RCR1.7    RHH   Port H.Bit4-7 Pullup Resistors (0=Off, 1=On) ;/
  RCR2.0-7  RCn   Port C.Bit0-7 Pullup Resistors (0=Off, 1=On)
```

#### HC05 Port OPTM=1:0Ah - WOM1 - Open Drain Output Control Register 1 (R/W)
#### HC05 Port OPTM=1:0Bh - WOM2 - Open Drain Output Control Register 2 (R/W)
```
  WOM1.0   AWOML Port A.Bit0-3 Open Drain Mode when DDR=1 (0=No, 1=Open Drain)
  WOM1.1   AWOMH Port A.Bit4-5 Open Drain Mode when DDR=1 (0=No, 1=Open Drain)
  WOM1.2   GWOML Port G.Bit0-3 Open Drain Mode when DDR=1 (0=No, 1=Open Drain)
  WOM1.3   GWOMH Port G.Bit4-5 Open Drain Mode when DDR=1 (0=No, 1=Open Drain)
  WOM1.4   HWOML Port H.Bit0-3 Open Drain Mode when DDR=1 (0=No, 1=Open Drain)
  WOM1.5   HWOMH Port H.Bit4-5 Open Drain Mode when DDR=1 (0=No, 1=Open Drain)
  WOM1.6-7 -     Not used (0)
  WOM2.0-5 CWOMn Port C.Bit0..5 Open Drain Mode when DDR=1 (0=No, 1=Open Drain)
  WOM2.6-7 -     Not used (always both bits set)
```

==== Interrupts =====<br/>

#### HC05 Port OPTM=0:08h - INTCR - Interrupt Control Register (R/W)
```
  0-1  -     Not used (0)
  2    IRQ2S IRQ2 Select Edge-Sensitive Only (0=LowLevelAndNegEdge, 1=NegEdge)
  3    IRQ1S IRQ1 Select Edge-Sensitive Only (0=LowLevelAndNegEdge, 1=NegEdge)
  4    KWIE  Key Wakeup Interrupt Enable (0=Disable, 1=Enable)
  5    -     Not used (0)
  6    IRQ2E IRQ2 Interrupt Enable (0=Disable, 1=Enable)
  7    IRQ1E IRQ1 Interrupt Enable (0=Disable, 1=Enable)
```

#### HC05 Port OPTM=0:09h - INTSR - Interrupt Status Register (R and W)
```
  0    RKWIF Reset Key Wakeup Interrupt Flag (0=No Change, 1=Reset) (W)
  1    -     Not used (0)
  2    RIRQ2 Reset IRQ2 Interrupt Flag       (0=No Change, 1=Reset) (W)
  3    RIRQ1 Reset IRQ1 Interrupt Flag       (0=No Change, 1=Reset) (W)
  4    KWIF  Key Wakeup Interrupt Flag (PB/KWI)       (0=No, 1=IRQ) (R)
  5    -     Not used (0)
  6    IRQ2F IRQ2 Interrupt Flag (PC6)                (0=No, 1=IRQ) (R)
  7    IRQ1F IRQ1 Interrupt Flag (PC7)                (0=No, 1=IRQ) (R)
```

#### HC05 Port OPTM=1:0Eh - KWIE - Key Wakeup Interrupt Enable Register (R/W)
```
  0-7  KWIEn Port B.Bit0..7 Key Wakeup Interrupt Enable (0=Disable, 1=Enable)
```

==== SPI Bus ====<br/>

#### HC05 Port OPTM=0:0Ah - SPCR1 - Serial Peripheral Control Register 1 (R/W)
```
  0    SPRn  SPI Clock Rate (0=ProcessorClock/2, 1=ProcessorClock/16)
  1-3  -     Not used (0)
  4    MSTRn SPI Master Mode Select      (0=Slave/SCK.In, 1=Master/SCK.Out)
  5    DORDn SPI Data Transmission Order         (0=MSB First, 1=LSB First)
  6    SPEn  SPI Enable (SPI1:PortC, SPI2:PortG) (0=Disable, 1=Enable)
  7    SPIEn SPI Interrupt Enable (... ack HOW?) (0=Disable, 1=Enable)
```

#### HC05 Port OPTM=0:0Bh - SPSR1 - Serial Peripheral Status Register 1 (R)
```
  0-5  -     Not used (0)
  6    DCOLn SPI Data Collision Occurred         (0=No, 1=Collision)
  7    SPIFn SPI Transfer Complete Flag          (0=Busy, 1=Complete) (R)
```
Note: SPSR1.7 appears to be reset after reading SPSR1 (probably same for
SPSR1.6, and maybe also same for whatever SPI IRQ signal).<br/>

#### HC05 Port OPTM=0:0Ch - SPDR1 - Serial Peripheral Data Register 1 (R/W)
```
  0-7  BITn  Data to be sent / being received
```

==== Time Base / Config ====<br/>

#### HC05 Port 10h - TBCR1 - Time Base Control Register 1 (R/W)
```
  0-1  T2R   Timer2 Prescaler (0=SysClk, 1=SysClk/4, 2=SysClk/32, 3=SysClk/256)
  2-3  T3R   PWM Prescaler    (0=CLK3, 1=CLK3/2, 2=CLK3/8, 3=Timer2compare)
  4-6  -     Not used (0)
  7    TBCLK Time Base Clock (0=XOSC, 1=OSC/128) ;<-- write-able only ONCE
```

#### HC05 Port 11h - TBCR2 - Time Base Control Register 2 (R/W, some bits R or W)
```
  0    COPC  COP Clear 2bit COP timeout divider (0=No Change, 1=Clear) (W)
  1    COPE  COP Enable                          ;<-- write-able only ONCE
  2    -     Not used (0)
  3    RTBIF Reset Time Base Interrupt Flag (0=No Change, 1=Clear TBIF) (W)
  4-5  TBR   Time Base Interrupt Rate (0=TBCLK/128, 1=/4096, 2=/8192, 3=/16384)
  6    TBIE  Time Base Interrupt Enable (0=Disable, 1=Enable)
  7    TBIF  Time Base Interrupt Flag   (0=No, 1=IRQ)        (R)
```

#### HC05 Port OPTM=1:0Fh - MOSR - Mask Option Status Register (R)
```
  0-4  -     Not used (0)
  5    XOSCR XOSC Feedback Resistor (0=None, 1=Implemented)
  6    OSCR  OSC Feedback Resistor  (0=None, 1=Implemented)
  7    RSTR  /RESET Pullup Resistor (0=None, 1=Implemented)
```
Reading this register returns A0h (on PSX/PSone with 52pin chips).<br/>

==== Timer 1 ====<br/>

#### HC05 Port 12h - TCR - Timer 1 Control Register (R/W)
```
  0    OLVL  Output Level on TCMP pin on Compare Match? (0=Low, 1=High)
  1    IEDG  Input Edge on TCAP pin (0=NegativeEdge, 1=PositiveEdge)
  2-4  -     Not used (0)
  5    TOIE  Timer Overflow Interrupt Enable (0=Disable, 1=Enable)
  6    OC1IE Output Compare Interrupt Enable (0=Disable, 1=Enable)
  7    ICIE  Input Capture Interrupt Enable  (0=Disable, 1=Enable)
```

#### HC05 Port 13h - TSR - Timer 1 Status Register (R)
```
  0-4  -     Not used (0)
  5    TOF   Timer Overflow Flag (0=No, 1=Yes) (R) ;clear by Port 19h access
  6    OC1F  Output Compare Flag (0=No, 1=Yes) (R) ;clear by Port 17h access
  7    ICF   Input Capture Flag  (0=No, 1=Yes) (R) ;clear by Port 15h access
```

#### HC05 Port 14h - ICH - Timer 1 Input Capture High (undoc)
#### HC05 Port 15h - ICL - Timer 1 Input Capture Low (undoc)
```
  0-15 Capture Value
```

#### HC05 Port 16h - OC1H - Timer 1 Output Compare 1 High (undoc)
#### HC05 Port 17h - OC1H - Timer 1 Output Compare 1 Low (undoc)
```
  0-15 Compare Value
```

#### HC05 Port 18h - TCNTH - Timer 1 Counter 1 High (undoc)
#### HC05 Port 19h - TCNTL - Timer 1 Counter 1 Low (undoc)
```
  0-15 Counter
```

#### HC05 Port 1Ah - ACNTH - Alternate Counter High (undoc)
#### HC05 Port 1Bh - ACNTL - Alternate Counter Low (undoc)
```
  0-15 Alternate Counter (uh, what?)
```

==== Timer 2 ====<br/>

#### HC05 Port 1Ch - TCR2 - Timer 2 Control Register (R/W)
```
  0    OL2   Timer Output 2 Edge (0=Falling, 1=Rising)
  1    OE2   Timer Output 2 Enable (EVO) (0=Disable, 1=Enable)
  2    IL2   Timer Input 2 Edge/Level (0=Low/Falling, 1=High/Rising)
  3    IM2   Timer Input 2 Mode Select for EVI (0=EventMode, 1=GatedByCLK2)
  4    T2CLK Timer 2 Clock Select (0=CLK2 from Prescaler, 1=EXCLK from EVI)
  5    -     Not used (0)
  6    OC2IE Output Compare 2 Interrupt Enable    (0=Disable, 1=Enable)
  7    TI2IE Timer Input 2 Interrupt Enable (EVI) (0=Disable, 1=Enable)
```

#### HC05 Port 1Dh - TSR2 - Timer 2 Status Register (R/W)
```
  0-1  -     Not used (0)
  2    ROC2F Reset Output Compare 2 Interrupt Flag (0=No Change, 1=Clear) (W)
  3    RTI2F Reset Timer Input 2 Interrupt Flag    (0=No Change, 1=Clear) (W)
  4-5  -     Not used (0)
  6    OC2F  Output Compare 2 Interrupt Flag    (0=No, 1=Yes) (R)
  7    TI2F  Timer Input 2 Interrupt Flag (EVI) (0=No, 1=Yes) (R)
```

#### HC05 Port 1Eh - OC2 - Timer 2 Output Compare Register (R/W)
```
  0-7  Compare Value ("Transferred to buffer on certain events?")
```

#### HC05 Port 1Fh - TCNT2 - Timer 2 Counter Register (R) (W=Set Counter to 01h)
```
  0-7  Counter Value, incremented at T2R (set to 01h on Compare Matches)
```

==== Reserved ====<br/>

#### HC05 Port 3Fh - Unknown/Unused
Reading this port via Sony's test command returns 20h (same as openbus), but
reading it via Motorola's selftest function returns 00h (unlike openbus), so it
seems to have some unknown/undocumented function; bit5 might indicate selftest
mode, or it might reflect initialization of whatever other ports.<br/>

#### HC05 Port OPTM=0:06h..07h,0Dh..0Fh - Reserved
#### HC05 Port OPTM=1:01h,06h..07h,0Ch..0Dh - Reserved
#### HC05 Port 20h..3Dh - Reserved
These ports are unused/reserved. Trying to read them on a PSone does return 20h
(possibly the prefetched next opcode value from the RAM test command). Other
HC05 variants contain some extra features in these ports:<br/>
[CDROM Internal HC05 On-Chip I/O Ports - Extras](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-hc05-on-chip-io-ports-extras)<br/>
The PSX CDROM BIOS doesn't use any of these ports - execpt, it is writing
[20h]=2Eh (possibly to disable unused LCD hardware; which might be actually
present in the huge 80pin HC05 chips on old PU-7 mainboards).<br/>

#### HC05 Openbus
Openbus values can be read from invalid memory locations, on PSX with 52pin
chips:<br/>
```
  I/O bank 0:    0:06h..07h, 0:0Dh..0Fh
  I/O bank 1:    1:01h, 1:06h..07h, 1:0Ch..0Dh, and upper 4bit of 1:05h
  Unbanked I/O:  20h..3Dh
  Unused Memory: 0240h..0FFFh, 5000h..FDFFh
```
The returned openbus value depends on the opcode's memory operand:<br/>
```
  [nn],[mmnn],[nn+x],[mmnn+x] --> returns LAST byte of current opcode (=nn)
  [x]                         --> returns FIRST byte of following opcode
```



##   CDROM Internal HC05 On-Chip I/O Ports - Extras
#### HC05 Port OPTM=0:0Dh - SPCR2 - Serial Peripheral Control Register 2 (R/W)
#### HC05 Port OPTM=0:0Eh - SPSR2 - Serial Peripheral Status Register 2 (R)
#### HC05 Port OPTM=0:0Fh - SPDR2 - Serial Peripheral Data Register 2 (R/W)
This is a second SPI channel, works same as first SPI channel, but using the
lower 3bits of Port G (instead of Port C) for the SPI signals.<br/>

#### HC05 Port OPTM=0:06h - PORTG - Port G Data Register (R/W)
#### HC05 Port OPTM=0:07h - PORTH - Port H Data Register (R/W)
#### HC05 Port 3Ch - PORTJ - Port J Data Register (R/W)
```
  PG.0    PG0   Port G Bit0    Input/Output /SDI2      (0=Low, 1=High) (R/W)
  PG.1    PG1   Port G Bit1    Input/Output /SDO2      (0=Low, 1=High) (R/W)
  PG.2    PG2   Port G Bit2    Input/Output /SCK2      (0=Low, 1=High) (R/W)
  PG.3    PG3   Port G Bit3    Input/Output /TCMP      (0=Low, 1=High) (R/W)
  PG.4    PG4   Port G Bit4    Input/Output /PWM0      (0=Low, 1=High) (R/W)
  PG.5    PG5   Port G Bit5    Input/Output /PWM1      (0=Low, 1=High) (R/W)
  PG.6    PG6   Port G Bit6    Input/Output /PWM2      (0=Low, 1=High) (R/W)
  PG.7    PG7   Port G Bit7    Input/Output /PWM3      (0=Low, 1=High) (R/W)
  PH.0-7  PHn   Port H Bit0..7 Input/Output            (0=Low, 1=High) (R/W)
  PJ.0-3  PJn   Port J Bit0..3 Output                  (0=Low, 1=High) (R/W)
  PJ.4-7  -     Not used (0)
```

#### HC05 Port OPTM=1:06h - DDRG - Port G Data Direction Register (R/W)
#### HC05 Port OPTM=1:07h - DDRH - Port H Data Direction Register (R/W)
```
  0-7  DDRXn Port X Data Direction Bit0..7 (0=Input, 1=Output) (R/W)
```

#### HC05 Port 20h - LCDCR - LCD Control Register (R/W)
```
  0    -     Not used (0)
  1    PDH   Select Port D (H) (0=FP35-FP38 pins, 1=PD7-PD4 pins)
  2    PEL   Select Port E (L) (0=FP31-FP34 pins, 1=PE3-PE0 pins)
  3    PEH   Select Port E (H) (0=FP27-FP30 pins, 1=PE7-PE4 pins)
  4    -     Not used (0)
  5-6  DUTY  LCD Duty Select (...)
  7    LCDE  LCD Output Enable BP and FP pins (0=Disable, 1=Enable)
```

#### HC05 Port 21h..34h - LCDDR1..20 - LCD Data Register 1..20 (R/W)
```
  0-3  First Data Unit  ;\Fourty 4bit LCD values (in the twenty registers)
  4-7  Second Data Unit ;/(some duties use only the LSBs of that 4bit values)
```

#### HC05 Port 34h - PWMCR - PWM Pulse Width Modulation Control Register (R/W)
```
  0-3  CH0-3 PWM Channel 0..3 on Port G.Bit4-7 Enable (0=Disable, 1=Enable)
  4-7  -     Not used (0)
```

#### HC05 Port 35h - PWMCNT - PWM Counter Register (R) (W=Set Counter to FFh)
```
  0-7  PWM Counter, incremented at PHI2 (range 01h..FFh)
```

#### HC05 Port 36h - PWMDR0 - PWM Duty Register 0 (R/W)
#### HC05 Port 37h - PWMDR1 - PWM Duty Register 1 (R/W)
#### HC05 Port 38h - PWMDR2 - PWM Duty Register 2 (R/W)
#### HC05 Port 39h - PWMDR3 - PWM Duty Register 3 (R/W)
```
  0-7  Duty (N cycles High, 255-N cycles Low)
```

#### HC05 Port 3Ah - ADR - A/D Data Register (R)
```
  0-3  A/D Conversion result (probably unsigned, 00h=Lowest, FFh=Max voltage?)
```

#### HC05 Port 3Bh - ADSCR - A/D Status and Control Register (R/W)
```
  0-3  CH0-3 A/D Channel (0..7=PortF.Bit0-7, 8..0Fh=Reserved/Vref/FactorTest)
  4    -     Not used (0)
  5    ADON  A/D Charge Pump enable (0=Disable, 1=Enable)
  6    ADRC  A/D RC Oscillator On (0=Normal/Use CPU Clock, 1=Use RC Clock)
  7    COCO  A/D Conversion Complete (0=Busy, 1=Complete) (R)
```

#### HC05 Port 3Dh - PCR - Program Control Register (R/W) (for EPROM version)
```
  0    PGM   EPROM Program Command (0=Normal, 1=Apply Programming Power)
  1    ELAT  EPROM Latch Control (0=Normal/Read, 1=Latch/Write)
  2-7  RES   Reserved for Factory Testing (always 0 in user mode)
```



##   CDROM Internal HC05 I/O Port Usage in PSX
#### Port A - Data (indexed via Port E)
```
  porta.0-7 i/o  CXD1815Q.Data (indexed via Port E)
  porta.0   in   debug.dta.serial.in  ;\normally unused (exists in early bios)
  porta.1   out  debug.dta.serial.out ; (prototype/debug_status stuff)
  porta.2   out  debug.clk.serial.out ;/(with portc.5 = debug.select)
```

#### Port B - Inputs
```
  portb.0   in   F-BIAS  ;unused
  portb.1   in   SCEx input (serial 250 baud, received via 1000Hz timer2 irq)
  portb.2   in   LMTSW  aka /POS0        ;\pos0 and door switches
  portb.3   in   DOOR   aka SHELL_OPEN   ;/
  portb.4   in   TEST2
  portb.5   in   TEST1 (CL316) enter test mode (instead of mainloop)
  portb.6   in   COUT   ;<-- unused, extra pin, not "SENSE=COUT"
  portb.7   in   CXD2510Q.SENSE ;-from CXD2510Q (and forwarded from CXA1782BR)
```

#### Port C - Inputs/Outputs
```
  portc.0   in   CXD2510Q.SUBQ  ;\
  portc.1   in?  NC (SPI.OUT)   ; used via SPDR1 to receive SPI bus SUBQ data
  portc.2   out  CXD2510Q.SQCK  ;/
  portc.3   out  SPEED
  portc.4   out    ="SPEED XOR 1"  ... AL/TE ... or CG ... or MIRR ?
  portc.5   out  ROMSEL: debug.select   (or "SCLK" on later boards???)
  portc.6   in   CXD1815Q.XINT/IRQ2 ;unused (instead INTSTS bits are polled)
  portc.7   in   CXD2510Q.SCOR/IRQ1 ;used via polling INTSR.7 (not as irq)
```

#### Port D - Outputs
```
  portd.0   out  NC             ;-unused (always 1)
  portd.1   out  CXD2510Q.DATA  ;\serial bus for CXD2510Q
  portd.2   out  CXD2510Q.XLAT  ; (and also forwarded to CXA1782BR)
  portd.3   out  CXD2510Q.CLOK  ;/
  portd.4   out  CXD1815Q.DECCS ;\
  portd.5   out  CXD1815Q.DECWR ; control for data/index on Port A/E
  portd.6   out  CXD1815Q.DECRD ;/
  portd.7   out  LDON  ... IC723.Pin11 ... maybe "laser on" ?
```

#### Port E - Index (for data on Port A)
```
  porte.0-4 out  CXD1815Q.Index (for data on Port A)
  porte.5   out  NC, not used
  porte.6   out  NC, see "idx_4xh" maybe test signal ???
  porte.7   out? NC, TEST? configured as OUTPUT... but used as INPUT?
```

#### Port F - Motorola Bootstrap Serial I/O (not used in cdrom bios)
```
  portf.0   out  NC, TX         ;\
  portf.1   in   NC, RX         ; not used by sony's cdrom bios
  portf.2   out  NC, RTS        ; (but used by motorola's bootstrap rom)
  portf.3   out  NC, DTR        ;/
  portf.0   in   Serial Data In  (from daughterboard)  ;\
  portf.1   out  Serial Data Out   (to daughterboard)  ; usage in SCPH-5903
  portf.2   out  Serial Clock Out  (to daughterboard)  ; (PSX with Video CD)
  portf.3   out  Audio/Video Select (0=Normal, 1=VCD)  ;/
  portf.4-7 -    NC, not used (probably pins don't even exist)
```

#### Other HC05 I/O Ports
```
  SPI 1   - used for receiving SUBQ (via Port C)
  IRQ 1   - used for latching/polling SUBQ's "SCOR" (not used as interrupt)
  IRQ 2   - connects to CXD1815Q.XINT, but isn't actually used at all
  Timer 1 - unused
  Timer 2 - generates 1000Hz interrupts (for 250 baud "SCEx" string transfers)
  DDRx    - data directions for Port A-F (as listed above)
```
Note: The PSX has the HC05 clocked via 4.00MHz oscillator (older boards), or
via 4.3MHz signal from SPU (newer boards); internally, the HC05 is clocked at
half of those frequencies (ie. around 2 MHz).<br/>



##   CDROM Internal HC05 Motorola Selftest Mode
#### 52-pin HC05 chips (newer psx cdrom controllers)
52-pin chips are used on LATE-PU-8 boards, and on later boards ranging from
PU-18 up to PM-41(2).<br/>
[CDROM Internal HC05 Motorola Selftest Mode (52pin chips)](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-hc05-motorola-selftest-mode-52pin-chips)<br/>

#### 80-pin HC05 chips (older psx cdrom controllers)
80-pin chips are used PU-7, EARLY-PU-8, and PU-9 boards.<br/>
[CDROM Internal HC05 Motorola Selftest Mode (80pin chips)](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-hc05-motorola-selftest-mode-80pin-chips)<br/>

#### 32-pin HC05 chips (joypad/mouse)
Sony's Digital Joypad and Mouse are using 32pin chips (with TQFP-32 package),
which are probably containing Motorola HC05 CPUs, too. Unknown if/how those
chips can be switched into bootstrap/dumping modes.<br/>

#### Pinouts
[Pinouts - HC05 Pinouts](pinouts.md#pinouts-hc05-pinouts)<br/>



##   CDROM Internal HC05 Motorola Selftest Mode (52pin chips)
#### Motorola Bootstrap ROM
The Motorola MC68HC05 chips are including a small bootstrap ROM which gets
activated upon /RESET when having two pins strapped to following levels:<br/>
```
  Pin30 PortC.6 (/IRQ2) (/XINT) ----> wire to 3.5V (VCC)
  Pin31 PortC.7 (/IRQ1) (SCOR)  ----> wire to 7V (2xVCC)
```
Moreover, two pins are needed on /RESET for selecting a specific test mode:<br/>
```
  Pin16 PortB.0 ----> ModeSelectBit0 (0=GND, 1=3.5V)
  Pin17 PortB.1 ----> ModeSelectBit1 (0=GND, 1=3.5V)
```
The selectable four modes are:<br/>
```
  Mode0: Jump to RAM Address 0040h (useless when RAM is empty)
  Mode1: Semifunctional Selftest (useless)
  Mode2: Upload 200h bytes to RAM & jump to 0040h (allows fast/custom dumping)
  Mode3: Download ROM as ASCII hexdump (nice, but very slow)
```
The upload/download functions are using following additional pins:<br/>
```
  Pin50 PortF.0 ----> TX output (11bytes: 0Dh,0Ah," AAAA DD ")
  Pin51 PortF.1 <---- RX input  (1byte: "!" to request next 11 bytes)
  Pin52 PortF.2 ----> RTS output or so (not needed)
  Pin1  PortF.3 ----> DTR output or so (not needed)
  Ground ------------ GND for RX/TX
```
RX/TX are RS232-like serial signals (but using other voltages, 0=0V and
1=3.5V). Transfer format is 8-N-1, ie. one startbit(0), 8 databits LSB first,
no parity, one stopbit(1). Baudrate is OSC/2/208 (ie. 9616 bps for 4.000MHz, or
10176 bps for 4.2336MHz clock derived from CXD2545Q/CXD2938Q).<br/>
Note: Above pins may vary on some chips (namely on chips that don't have
PortF). The pins for entering bootstrap mode (PortC in this case) should be
described in datasheets; but transfer protocol and mode selection (PortB) and
transmission (PortF) aren't officially documented.<br/>

#### Mode2: Upload 200h bytes to RAM & jump to 0040h
This mode is very simple and powerful: After /RESET, you send 200h bytes to the
RX input (without any response on TX output), the bytes are stored at
0040h..023Fh in RAM, and the chip jumps to 0040h after transferring the last
byte. The uploaded program can contain a custum highspeed dumping function, or
perform hardware tests, etc. A custom dumping function for PSX/PSone can be
found at:<br/>
```
  http://www.psxdev.net/forum/viewtopic.php?f=70&t=557
```
After uploading the 200h-byte dumping function it will respond by send 4540h
bytes (containing some ASCII string, the 16.5Kbyte ROM image, plus dumps for
RAM and (banked) I/O port region, plus openbus tests for unused memory and I/O
regions.<br/>

#### Wiring for Mode2 on PSX/PSone consoles with 52-pin HC05 chips
```
                            .------------ pin31, PC7, SCOR, cut the connection
                   39       |   27               to Signal Processor,
                 .-----------------.             then wire Pin31 to 7.5V
              40 |                 | 26
                 |  C nnnn         |
                 |  SC4309nnPB     |
                 |  G63C 185       |
  pin50, TX <--- |                 | ---- pin17, PB1, SCEX, wire to 3.5V,
  pin51, RX ---> |                 |                  for Mode2 Selection
              52 | O               | 14
                 '-----------------'
                   1            13
```
Good places to pick 3.5V and 7.5V from nice solder pads are:<br/>
```
  CN602.Pin1  = 7.5V     ;\on PSX boards (with either 5pin or
  CN602.Pin3  = 3.5V     ;/               7pin CN602 connectors)
  IC601.Pin1  = 7.5V     ;-on PSone boards (3pin 78M05 voltage regulator)
  IC102.Pin32 = 3.5V     ;-on PSone boards (32pin Main BIOS ROM chip)
```
The SCOR trace on Pin31, connects to Signal Processor...<br/>
```
  CXD2510Q.Pin63  (eg. on PU-8 boards)   ;\
  CXD2545Q.Pin74  (eg. on PU-18 boards)  ; either one of these, depending
  CXD1817R.Pin49  (eg. on PU-20 boards)  ; on which chipset you have
  CXD2938Q.Pin77  (eg. on PM-41 boards)  ;
  CXD2941R.Pin85  (eg. PM-41(2) boards)  ;/
```
cut that trace (preferably on the PCB between two vias or test points, so you
can later repair it easily) (better don't try to lift Pin31, it breaks off
easily)<br/>
Note: Mode2 also requires Pin16=Low, and Pin30=High (but PSX/PSone boards
should have those pins at that voltages anyways).<br/>

#### Mode3: Download ROM as ASCII hexdump
This mode is very slow and not too powerful. But it may useful if you can't get
Mode2 working for whatever reason. Wiring for Mode3 is same as above, plus
PortB.0=3.5V. In this mode, the chip will send one 0Dh,0Ah," AAAA DD " string
immediately after /RESET (with 16bit address "AAAA" (initially 1000h), and 8bit
data "DD"). Thereafter the chip will wait for incoming commands:<br/>
```
  4-digit ASCII HEX address --> change address, and return 0Dh,0Ah," AAAA DD "
  chr(00h) --> increment address, and return 0Dh,0Ah," AAAA DD "
  chr(07h) --> jump to current address (not so useful)
  other characters --> same as chr(00h)
  All digits/characters sent to RX input will produce an echo on TX output.
```
Basic setup would be wiring RX to GND (the chip will treat that as infinite
stream of start bits with chr(00h), so it will respond by sending data from
increasing addresses automatically; the increment wraps from 4FFFh to FE00h
(skipping the gap between Main ROM and Bootstrap ROM), and also wraps from
FFFFh to 0000h; transfer is ultraslow: 13 characters needed per dumped byte:
chr(00h) to chip, chr(00h) echo from chip, and 0Dh,0Ah," AAAA DD " from chip.<br/>



##   CDROM Internal HC05 Motorola Selftest Mode (80pin chips)
#### 80pin Sony 4246xx chips
And for anyone else planning to try this, these are the connections:<br/>
```
  Pin PortC
  46  PC7/IRQ1 (SCOR) disconnect from PCB, then wire the pin to Vtst (7.6V)
  45  PC6/IRQ2 (/XINT) wire to Vdd (3.5V) (you have to solder to the pin)
```
In bootstrap mode, Port A is used as follows:<br/>
```
  Pin PortA DDRA Usage
  23  PA0   in   RXD
  24  PA1   out  TXD
  25  PA2   in   -
  26  PA3   in   Testmode.bit0 (GND=0, 3.5V=1)
  27  PA4   in   Testmode.bit1 (GND=0, 3.5V=1)
  28  PA5   in   Testmode.bit2 (GND=0, 3.5V=1)
  29  PA6   out  RTS (don't care)
  30  PA7   out  -
```
The selectable testmodes are:<br/>
```
  PA5 PA4 PA3  Effect
  0   x   x    Jump to 0040h      ;\
  1   0   0    Test (complex)     ; not so useful
  1   0   1    Test (simple loop) ;/
  1   1   0    ROM Dump 4200h bytes (plain binary, non-ASCII)
  1   1   1    RAM Upload 100h bytes to 0040h..013Fh, then jump to 0040h
```
RX/TX are plain binary (non-ASCII), baudrate is 9600 (when using 4.000MHz
oscillator), transfer format is 8,N,2 (aka 8,N,1 with an extra pause bit).<br/>

#### Wiring for Upload/Download on PSX consoles with 80-pin HC05 chips
```
                  .------------ pin46, PC7/IRQ1, SCOR, cut & wire to 7.5V
                  |.----------- pin45, PC6/IRQ2, wire to 3.5V
         60       ||  41
       .-----------------.
    61 |               o | 40
       |  Sony Computer  |           ,----- pin28, PA5, wire to 3.5V
       |  Entertainment  | _________/  ,--- pin27, PA4, wire to 3.5V
       |  Inc. (C) E35D  | ==========='---- pin26, PA3, mode select
       |     4246xx 185  | ----> pin24, PA1, TXD (for ROM dump)
       |                 | <---- pin23, PA0, RXD (for RAM upload)
    80 | O               | 21
       '-----------------'
         1            20
```
Good places to pick 3.5V and 7.5V from nice solder pads are:<br/>
```
  CN602.Pin1  = 7.5V     ;\on PSX boards (with 7pin CN602 connectors)
  CN602.Pin3  = 3.5V     ;/
```
Credits to TriMesh for finding the 80pin chip's bootstrap signals.<br/>

#### Other 80pin chips
DTL-H100x uses 80pin chip with onchip PROM (chip text "(M) MC68HC705L15",
instead of "Sony [...] 4246xx"), wiring for serial dumping on that is unknown
(the bootstrap ROM may be a little different because it should contain PROM
burning functions). PU-9 boards boards seem to use a similar PROM (with some
sticker on it).<br/>
DTL-H2000 uses 80pin CXP82300 chip with socketed piggyback 32pin EPROM - that
chip is a Sony SPC700 CPU, not a Motorola HC05 CPU. Accordingly there's no
Motorola Bootstrap mode in it, but of course one could simply dump the EPROM
with standard eprom utilities, but nobody did do so yet).<br/>



##   CDROM Internal CXD1815Q Sub-CPU Configuration Registers
#### 00h - DRVIF - Drive Interface (W)
```
  0-1 "L"     Reserved (should be 0)
  2   LSB 1st CD DSP DATA order               (0=MSB first, 1=LSB first)
  3-4 BCK MD  CD DSP Number of BCLKs per WCLK (0=16, 1=24, 2=32, 3=Reserved)
  5   BCK RED Strobe DATA on BLCK Edge        (0=Falling Edge, 1=Rising Edge)
  6   LCH LOW Channel on LRCK=Low             (0=Right, 1=Left)
  7   C2PL1st      ... C2PO lower byte 1st
```

#### 01h - CONFIG 1 - Configuration 1 (W)
```
  0   HCLKDIS  HCLK Pin Output (0=8.4672MHz, 1=Disable; Fixed Low)
  1   CLKDIS   CLK Pin Output (0=16.9344MHz, 1=Disable; Fixed Low)
  2   9BITRAM  SRAM Databus width (0=8bit/normal, 1=9bit)
  3-4 RAM SZ   SRMA Address bus (0=32K, 1=64K, 2=128K, 3=Reserved)
  5   PRTYCTL      ... Priority Control
  6   XSLOW    Number of clock cycles per DMA cycle (0=12, 1=4) (for SRAM)
  7   "L"      Reserved (should be 0)
```

#### 02h - CONFIG 2 - Configuration 2 (W)
```
  0   "L"      Reserved (should be 0)
  1   DACODIS        .... DAC Out Disable
  2   DAMIXEN  Digital Audio Mixer Enable (0=Attentuator/Mixer for CD-DA, 1=No)
  3   SMBF2    Number of Sound Map Buffer Surfaces (0=Three, 1=Two)
  4   SPMCTL   Sound Parameter Majority Control (0=?)  ;\for ADPCM params
  5   SPECTL   Sound Parameter Error Control    (0=?)  ;/
  6-7 "L"      Reserved (should be 0)
```

#### 03h - DECCTL - Decoder Control (W)
```
  0-2 DECMD    Decoder Mode (0-7)
                 0 or 1  Decoder Disable            ;-disable sector reading
                 2 or 3  Monitor-only Mode          ;\no error correction
                 4       Write-only Mode            ;/
                 5       Real-time Correction Mode  ;\with error correction
                 6       Repeat Correction Mode     ;/
                 7       CD-DA Mode                 ;-audio
  3   AUTODIST Auto Distinction (0=Use MODESEL/FORMSEL bits, 1=Use Sector Hdr)
               (Error Correction is done according to above MODE/FORM values)
  4   FORMSEL  Form Select (0=FORM1, 1=FORM2) (must be 0 for MODE1)
  5   MODESEL  Mode Select (0=MODE1, 1=MODE2)
  6   ECCSTR   ECC Strategy (0=Normal, 1=Use Error Flags; requires 9bit SRAM)
  7   ENDLADR  Enable Drive Last Address    ...
```

#### 07h - CHPCTL - Chip Control (W)
```
  0   "L"      Reserved (should be 0)
  1   DBLSPD   Double Speed Mode (0=Normal, 1=Double) (init CD DSP first)
  2   RPSTART  Repeat Correction Start (0=No, 1=Start) (automatically cleared)
  3   SWOPEN   Sync Window Open (0=SyncControlledByIC, 1=OpenDetectionWindow)
  4   CD-DA    CD-DA Play     (0=No, 1=Playback CD-DA as audio)
  5   CDDAMUTE CD-DA Mute     (0=Normal, 1=Mute CD-DA Audio)
  6   RTMUTE   Real-time Mute (0=Normal, 1=Mute CDROM ADPCM)
  7   SMMUTE   Sound Map Mute (0=Normal, 1=Mute Sound Map ADPCM)
```



##   CDROM Internal CXD1815Q Sub-CPU Sector Status Registers
#### 00h - ECCSTS - ECC Status (R)
```
  0 CFORM   FORM assumed by Error Correction (0=FORM1, 1=FORM2)
  1 CMODE   MODE assumed by Error Correction (0=MODE1, 1=MODE2)
  2 ECCOK   ECC Okay (0=Bad, 1=Okay)
  3 EDCOK   EDC Okay (0=Bad, 1=Okay)
  4 CORDONE Correction Done (0=None, 1=Error occurred and was corrected)
  5 CORINH  Correction Inhibit (0=Okay,1=AUTODIST couldn't determine MODE/FORM)
  6 ERINBLK Erasure in Block (0=Okay, 1=At least 1 byte is wrong & uncorrected)
  7 EDCALL0 EDC all-zero  (0=No/EDC Exists, 1=Yes/All four EDC bytes are 00h)
```

#### 01h - DECSTS - Decoder Status (R)
```
  0   NOSYNC   No Sync       (0=Okay, 1=Sector Sync Mark Missing)
  1   SHRTSCT  Short Sector  (0=Okay, 1=Sector Sync Mark within Sector Data)
  2-4 -        Reserved (undefined)
  5   RTADPBSY Real-time ADPCM Busy (0=No, 1=Busy/playback)
  6-7 -        Reserved (undefined)
```

#### 02h - HDRFLG - Header/Subheader Error Flags for HDR/SHDR registers (R)
```
  0 CI      Error in 4th Subheader byte (Coding Info) (0=Okay, 1=Error)
  1 SUBMODE Error in 3rd Subheader byte (Submode)     (0=Okay, 1=Error)
  2 CHANNEL Error in 2nd Subheader byte (Channel)     (0=Okay, 1=Error)
  3 FILE    Error in 1st Subheader byte (File)        (0=Okay, 1=Error)
  4 MODE    Error in 4th Header byte (MODE)           (0=Okay, 1=Error)
  5 BLOCK   Error in 3rd Header byte (FF)             (0=Okay, 1=Error)
  6 SEC     Error in 2nd Header byte (SS)             (0=Okay, 1=Error)
  7 MIN     Error in 1st Header byte (MM)             (0=Okay, 1=Error)
```
Error flags for current sector are probably stored straight in this register
(ie. these flags are probably available even without using 9bit SRAM).<br/>
Or maybe not... if the chip supports receiving newer sectors during
time-consuming error corrections... then those newer would need to be stored in
SRAM, and would thus require 9bit SRAM for the error flags?<br/>

#### 03h - HDR - Header Bytes (R)
```
  1st read: 1st Header byte (MM)
  2nd read: 2nd Header byte (SS)
  3rd read: 3rd Header byte (FF)
  4th read: 4th Header byte (MODE)
```

#### 04h - SHDR - Subheader Bytes (R)
```
  1st read: 1st Subheader byte (File)
  2nd read: 2nd Subheader byte (Channel)
  3rd read: 3rd Subheader byte (Submode) (SM)
  4th read: 4th Subheader byte (Coding Info) (CI)
```
The contents of the HDRFLG, HDR, SHDR registers indicate:<br/>
```
      (1) The corrected value in the real-time correction or
          repeat correction mode
      (2) Value of the raw data from the drive in the monitor-only
          or write-only mode
    The CMOME? and CMODE bits (bits 1, 0) of ECCSTS indicate the FORM and MODE
    of the sector the decoder has discriminated by the raw data from the drive.
    Due to erroneous correction, the values of these bits may be at variance
    with those of the HDR register MODE byte and SHDR register submode byte
    bit5.
```

Unknown when 1st..4th read indices are reset for HDR and SHDR (maybe on access
to certain I/O ports, or maybe anytime when receiving a new sector), also
unknown what happens on 5th read and up.<br/>



##   CDROM Internal CXD1815Q Sub-CPU Address Registers
Drive Address -- used for storing incoming CDROM sectors in Buffer RAM<br/>
Host Address -- used for transferring Buffer RAM to (or from) Main CPU<br/>
ADPCM Address -- used for Real-time ADPCM audio output from Buffer RAM<br/>

#### 05h - CMADR - Drive Current Minute Address (R)
```
  0-6   CMADR    Address bit10-16 (in 1Kbyte steps)
  7     -        Reserved (undefined)
```
Indicates the start address of the most recently decoded sector (called "Minute
Address" because it points to the MM byte of the MM:SS:FF:MODE sector header).
Normally, CMADR should be forwarded to Host:<br/>
```
  HADR = (CMADR AND 7Fh)*400h+offset
  HXFR = length OR 4000h
```
Whereas, offset would be usually 00h, 04h, or 0Ch (to start reading from the
begin of the sector, or to skip 4-byte MODE1 header, or 12-byte MODE2 header).
And length would be usually 800h (normal data sector), or 924h (entire sector,
excluding the leading 12 sync-bytes). Length bit14 is undocumented/reserved,
but the PSX CDROM BIOS does set that bit for whatever reason.<br/>
Alternately, the sector can be forwarded to the Real-time ADPCM decoder:<br/>
```
  ADPMNT = (CMADR AND 7Fh) OR 80h
```

#### 19h - ADPMNT - ADPCM "MNT" Address (W)
```
  0-6   ADPxxx  ADPCM source Address bit10-16 (in 1Kbyte-steps)
  7     RTADPEN Real-time ADPCM Enable (0=Disable, 1=Enable Real-time ADPCM)
```

#### 04h - DLADR-L, Drive Last Address, bit0-7 (W)
#### 05h - DLADR-M, Drive Last Address, bit8-15 (W)
#### 06h - DLADR-H, Drive Last Address, bit16 (W)
```
  0-16  DLADR  Addr. bit0-16     ...
  17-23 "L"    Reserved (should be 0)
```

#### 10h - DADRC-L - Drive Address Counter, bit0-7 (W)
#### 11h - DADRC-M - Drive Address Counter, bit8-15 (W)
#### 12h - DADRC-H - Drive Address Counter, bit16 (W)
```
  0-16  DADRC    Incrementing Drive-to-Buffer Write Address, bit0-16
  17-23 "L"      Reserved (should be 0)
```

#### 0Eh - DADRC-L - Drive Address Counter, Bit0-7 (R)
#### 0Fh - DADRC-M - Drive Address Counter, Bit8-15 (R)
```
  0-15  DADRC Address bit0-15  ;bit16 is in Port 0Bh            ...
```

#### 0Ch - HXFR-L - Host Transfer Length, bit0-7 (W)
#### 0Dh - HXFR-H - Host Transfer Length, bit8-11 and stuff (W)
```
  0-11  HXFR     number of data bytes, bit0-11 (0..FFFh)       ...
  12    HADR.16  HADR  bit16
  13    "L"      Reserved (should be 0)
  14    "L" ??   Reserved (should be 0)   ;<-- XXX but on PSX: Always 1 !?!
                                          ;    seems to Disable INT8 ?!!!
  15    DISHXFRC Disable HXFRC (0=Use HXFRC, 1=Disable, Infinite-or-Zero Len?)
```

#### 0Eh - HADR-L - Host Transfer Address, bit0-7 (W)
#### 0Fh - HADR-M - Host Transfer Address, bit8-15 (W)
```
  0-15  HADR     Addr. bit0-15  ;bit16 in Port 0Dh    ...
```

#### 0Ah - HXFRC-L - Host Transfer Remain Counter, bit0-7 (R)
#### 0Bh - HXFRC-H - Host Transfer Remain Counter, bit8-11, and other bits (R)
```
  0-11  HXFRC Host Transfer Counter bit0-11 (number of remaining bytes)
  12    HADRC bit16  ;MSB of Port 0Ch/0Dh
  13    DADRC bit16  ;MSB of Port 0Eh/0Fh
  14-15 -     Reserved (undefined) (usually both bits set)
```

#### 0Ch - HADRC-L - Host Transfer Address Counter, bit0-7 (R)
#### 0Dh - HADRC-M - Host Transfer Address Counter, bit8-15 (R)
```
  0-15  HADRC Address bit0-15  ;bit16 is in Port 0Bh
```
"This counter keeps the addresses which write or read the data with host
into/from the buffer.<br/>
When data from the host is written into the buffer or data to the host is read
from the buffer, the HADRC value is output from MA0 to 16. HADRC is incremented
each time one byte of data from the drive is read from the buffer (BFRD is
high) or written into the buffer (BFWR is high)."<br/>

#### Note
When reading from SRAM, data seems to go through a 8-byte data fifo, the HXFRC
(remain) and HADRC (addr) values aren't aware of that FIFO (ie. if there's data
in the fifo, then addr will be 8 bigger and remain 8 smaller than what has
arrived at the host).<br/>

#### Unclear Notes
"If sound map data is to be transferred before the data is transferred
(immediately after the host has set the BFRD and BFWR bits (bits 7 and 6) of
the HCHPCTL register high)":<br/>
```
  900h is loaded into HXFRC
  and 600Ch, 6A0Ch, or 740Ch is loaded into HADRC
  (at least, supposedly, above addresses , for cases when using 32K SRAM)
```
"At any other time":<br/>
```
  HADR and HXFR are loaded into HADRC and HXFRC
```
Unknown what the above crap is trying to say exactly.<br/>
"At any other time" does apparently refer to cases when transfers get started
(whilst during transfer, the address/remain values are obviously
increasing/decreasing).<br/>
For sound map, theoretically, the SMEN bit should be set, but above does
somewhat suggest that BFRD or BFWR (or actually: both BFRD and BFWR) need to be
set...?<br/>

#### Sector Buffer Memory Map (32Kx8 SRAM)
```
  0000h 1st Sector (at 0000h..0923h) (unused gap at 0924h..0BFFh)
  0C00h 2nd Sector (at 0C00h..1523h) (unused gap at 1524h..17FFh)
  1800h 3rd Sector (at 1800h..2123h) (unused gap at 2124h..23FFh)
  2400h 4th Sector (at 2400h..2D23h) (unused gap at 2D24h..2FFFh)
  3000h 5th Sector (at 3000h..3923h) (unused gap at 3924h..3BFFh)
  3C00h 6th Sector (at 3C00h..4523h) (unused gap at 4524h..47FFh)
  4800h 7th Sector (at 4800h..5123h) (unused gap at 5124h..53FFh)
  5400h 8th Sector (at 5400h..5D23h) (unused gap at 5D24h..5FFFh)
  6000h Soundmap ADPCM Buffer (at 600Ch..690Bh) (gaps at 6000h and 690Ch)
  6A00h Soundmap ADPCM Buffer (at 6A0Ch..730Bh) (gaps at 6A00h and 730Ch)
  7400h Soundmap ADPCM Buffer (at 740Ch..7D0Bh) (gaps at 7400h and 7D0Ch)
  7E00h Unknown/Unused
```



##   CDROM Internal CXD1815Q Sub-CPU Misc Registers
#### 16h - HIFCTL - Host Interface Control (W)
```
  0-2  HINT    Request Host Interrupt (INT1..INT7, or 0=None/No change)
  3-7  "L"     Reserved (should be 0)
```

#### 11h - HIFSTS - Host Interface Status (R)
```
  0-2 HINTSTS  Pending Host Interrupt (INT1..INT7, or 0=None/All acknowledged)
  3   DMABUSY  DMA Busy (0=Data FIFO Empty and HXFRC=0, 1=Data Transfer Busy)
  4   PRMRRDY  Paramter Read Ready (0=Parameter FIFO Empty, 1=Ready/Not Empty)
  5   RSLEMPT  Result Empty        (0=Response FIFO Not Empty, 1=Empty)
  6   RSLWRDY  Result Write Ready  (0=Response FIFO Full, 1=Ready/Not Full)
  7   BUSYSTS  Command Busy Status (0=Command Not Empty, 1=Ack'ed by CLRBUSY)
```

#### 0Ah - CLRCTL - Clear Control (W)
```
  0   RESYNC   Sync with CD DSP (0=No change, 1=Resync, eg. after speed change)
  1-3 "L"      Reserved (should be 0)
  4   RTADPCLR Abort Real-time ADPCM (0=No Change, 1=Abort; when ADPMNT.7=0)
  5   CLRRSLT  Clear Reply FIFO    (0=No change, 1=Acknowledge; clear FIFO)
  6   CLRBUSY  Acknowledge Command (0=No change, 1=Acknowledge; clear BUSYSTS)
  7   CHPRST   Chip Reset          (0=No change, 1=Do Chip Initialization)
```

#### 07h - INTSTS - Interrupt Status (R) - (0=No, 1=IRQ)
#### 09h - INTMSK - Interrupt Mask (W) - (0=Disable, 1=Enable)
#### 0Bh - CLRINT - Clear Interrupt Status (W) - (0=No change, 1=Clear/Ack)
```
  0   HCRISD   Host Chip Reset Issued
  1   HSTCMND  Host Command                ...
  2   DECINT   Decoder Interrupt           ..
  3   HDMACMP  Host DMA Complete           .   <-- PSX: used for retry ?!?!!!
  4   RTADPEND Real-time ADPCM end
  5   RSLTEMPT Result Empty
  6   DECTOUT  Decoder Time Out
  7   DRVOVRN  Drive Overrun
```

#### 12h - HSTPRM - Host Parameter (R)
```
  0-7  Param FIFO (check HIFSTS.4 to see if the FIFO is empty)
```
HIFSTS.4 goes off when all bytes read.<br/>
Said to have 8-byte FIFO in CXD1199AQ datasheet.<br/>
But, PSX has 16-byte Parameter FIFO...!?!<br/>

#### 13h - HSTCMD - Host Command (R)
```
  0-7  Command (check INTSTS.1 or HIFSTS.7 to see if a command was sent)
```
Command should be ack'ed via CLRINT.1 and CLRCTL.6.<br/>

#### 17h - RESULT - Response FIFO (W)
```
  0-7  Data (has 8-byte FIFO)
```
Said to have 8-byte FIFO in CXD1199AQ datasheet.<br/>
But, PSX has 16-byte Response FIFO...!?!<br/>

#### 08h - ADPCI - ADPCM Coding Information (R)
```
  0   S/M      ADPCM Stereo/Mono        (0=Mono, 1=Stereo)
  1   -        Reserved (undefined)
  2   FS       ADPCM Sampling Frequency (0=37.8kHz, 1=18.9kHz)
  3   -        Reserved (undefined)
  4   BITLNGTH ADPCM Sample Bit Length  (0=Normal/4bit, 1=8bit)
  5   ADPBUSY  ADPCM Decoding           (0=No, 1=Yes/Busy)
  6   EMPHASIS ADPCM Emphasis           (0=Normal/Off, 1=On)
  7   MUTE     DA Data is Muted (uh?)   (0=No, 1=Yes/Muted)
```
Unknown if ADPCI is affected by configurations by Main-CPU's Sound Map ADPCM or
by Sub-CPU's Real-time ADPCM (or by both)?<br/>
Note: Bit5,7 are semi-undocumented in the datasheet (mentioned in the ADPCI
description, but missing in overall register summary).<br/>

#### 1Bh - RTCI - Real-time ADPCM Coding Information (W)
```
  0    S/M      ADPCM Stereo/Mono        (0=Mono, 1=Stereo)
  1    "L"      Reserved (should be 0)
  2    FS       ADPCM Sampling Frequency (0=37.8kHz, 1=18.9kHz)
  3    "L"      Reserved (should be 0)
  4    BITLNGTH ADPCM Sample Bit Length  (0=Normal/4bit, 1=8bit)
  5    "L"      Reserved (should be 0)
  6    EMPHASIS ADPCM Emphasis           (0=Normal/Off, 1=On)
  7    "L"      Reserved (should be 0)
```

#### 06h,09h,10h,14h..1Fh - Reserved (R)
```
  0-7  Reserved (undefined)
```
Of these, 09h and 10h are officially unused/reserved. And addresses 06h and
14h..1Fh aren't officially mentioned to exist at all.<br/>
Trying to read these registers on a PSone returns Data=C0h for 06h, 09h, 10h,
15h-16h, 18h-1Fh, and Data=FFh for 14h, and Data=DEh for 17h.<br/>

#### 08h,13h-15h,18h,1Ah,1Ch-1Fh - Reserved (W)
```
  0-7  Reserved (should be 00h) (or don't write at all)
```
Of these, 09h,13h-15h,18h,1Ah are officially unused/reserved. And addresses
1Ch-1Fh aren't officially mentioned to exist at all.<br/>



##   CDROM Internal Commands CX(0x..3x) - CXA1782BR Servo Amplifier
#### CXA1782BR - CX(0x) - Focus Servo Control - "FZC" FocusZeroCross at SENS pin
```
  23-20 4bit  Command (00h)
  19    1bit  FS4 Focus Servo (0=Off, 1=On)
  18    1bit  FS3 DEFECT
  17    1bit  FS2 Enable Focus Search Voltage (0=Off, 1=On)
  16    1bit  FS1 Select Focus Search Voltage (0=Falling, 1=Rising)
  15-0  16bit Unused (don't care)
```
For Focus Search: Keep FS1=on, and toggle FS2 on and off (this will generate a
waveform, and SENS will indicate when reaching a good focus voltage).<br/>

#### CXA1782BR - CX(1x) - Tracking/Brake/Sled - "DEFECT" at SENS pin
```
  23-20 4bit  Command (01h)
  19    1bit  TG1,TG2 ON/OFF Tracking Servo Gain Up/Normal (hmmm?)
  18    1bit  Brake Circuit ON/OFF
  17-16 2bit  PS Sled Kick Height (0=+/-1, 1=+/-2, 2=Undoc, 3="Don't use"?)
  15-0  16bit Unused (don't care)
```
Note: The PSX CDROM BIOS does use the "Undoc" setting (ie. bit17=1), but the
effect is undoc/unknown?<br/>
Note: CX(1x) works different on CXD2545Q (some bits are moved around, and the
"SledKickHeight" bits are renamed to "SledKickLevel" and moved to different/new
CX(3X) commands.<br/>

#### CXA1782BR - CX(2x) - Tracking and Sled Servo Control - "TZC" at SENS pin
```
  23-20 4bit  Command (02h)
  19-18 2bit  Tracking Control (0=Off, 1=Servo On, 2=F-Jump, 3=R-Jump) ;TM1,3,4
  17-16 2bit  Sled Control     (0=Off, 1=Servo On, 2=F-Fast, 3=R-Fast) ;TM2,5,6
  15-0  16bit Unused (don't care)
```

#### CXA1782BR - CX(3x) - "Automatic Adjustment Comparator Output" at SENS pin
```
  23-20 4bit  Command (03h)
  19    1bit  Value to be adjusted (0=Balance, 1=Gain)
  18-16 3bit  New Balance or Gain value (depending on above bit)
  15-0  16bit Unused (don't care)
```
Note: CX(3x) is extended and works very different on CXD2545Q.<br/>

#### CXA1782BR Command 4x..7x - "HIGH-Z" at SENS pin
```
  N-N   4bit  Command (04h..07h)
```

#### CXA1782BR Command 8x..Fx - "UNSPECIFIED???" at SENS pin
```
  N-N   4bit  Command (08h..0Fh)
```

#### Note
The Servo Amplifier isn't directly connected to the CPU. Instead, it's
connected as a slave device to the Signal Processor. There are two ways to
access the Servo Amplifier:<br/>
1) The CPU can send CX(0X..3X) commands to the Signal Processor (which will
then forward them to the Servo Amplifier).<br/>
2) The Signal Processor can send CX(0X..3X) commands to the Servo Amplifier
(this happens during CX(4xxx) Auto Sequence command).<br/>



##   CDROM Internal Commands CX(4x..Ex) - CXD2510Q Signal Processor
#### CXD2510Q - CX(4xxx) - Auto Sequence
```
  23-20 4bit  Command (4)
  19-16 4bit  AS3-0 Auto Sequence Command (see below)
  15-12 4bit  MT3-0 Max Timer Value (N timer units, or 0=Invalidate Timer)
  11    1bit  LSSL  Timer Units     (0=2.9ms, 1=186ms) (for above MT value)
  10-8  3bit  Unused (zero)
  7-0   8bit  Unused (don't care)
```
Values for AS (Auto Sequence Command):<br/>
```
  00h     Cancel
  04h/05h Forward/Reverse Fine Search   ;<--sends CX(25h) ;\these do internally
  07h     Focus-On                      ;<--sends CX(02h) ; send commands to
  08h/09h Forward/Reverse 1 Track Jump  ;\                ; CXA1782BR
  0Ah/0Bh Forward/Reverse 10 Track Jump ;   sends CX(25h) ; and, auto sequence
  0Ch/0Dh Forward/Reverse 2N Track Jump ;/                ;/is interrupted?
  0Eh/0Fh Forward/Reverse 1N Track Move ;<--CXD2545Q only(Reserved on CXD2510Q)
  01h..03h,06h = Reserved
```

#### CXD2510Q - CX(5x) - Blind,Brake,Overflow Timer
```
  23-20 4bit  Command (5)
  19-16 4bit  TR3-0 Timer (N*0.022ms for Blind/Overflow, N*0.045ms for Brake)
  15-8  8bit  Unused (don't care on CXD2510Q, zero on CXD2545Q)
  7-0   8bit  Unused (don't care)
```

#### CXD2510Q - CX(6xx) - SledKick,Brake,Kick Timer
```
  23-20 4bit  Command (6)
  19-16 4bit  SD3-0 Timer KICK.D (N*2.9ms for Fine Search? else N*1.45ms?)
  15-12 4bit  KF3-0 Timer KICK.F (N*0.09ms)
  11-8  4bit  Unused (don't care on CXD2510Q, zero on CXD2545Q)
  7-0   8bit  Unused (don't care)
```

#### CXD2510Q - CX(7xxxx) - Track jump count setting (for Auto Sequence Command)
```
  23-20 4bit  Command (7)
  19-4  16bit Track Jump Count Setting (0..65535) for Command 4x
  3-0   4bit  Unused (don't care)
```

#### CXD2510Q - CX(8xx) - MODE Specification
```
  23-20 4bit  Command (8)
  19    1bit  CDROM        (0=Audio, 1=CDROM; no average and pre-value stuff)
  18    1bit  DOUT Mute    (0=Not muted, 1=Mute DOUT)
  17    1bit  D.out Mute-F (0=Not muted, 1=Mute DA)
  16    1bit  WSEL         (0=Enhanced Sync Window, 1=Enhanced Anti-Rolling)
  15    1bit  VCO SEL      (0=Double Correction, 1=Quadruple Correction)
  14    1bit  ASHS         (0=Double Correction, 1=Quadruple Correction)
  13    1bit  SOCT         (0=Output SubQ to SQSO, 1=Output Each? to SQSO)
  12    1bit  Unused (zero)
  11-8  4bit  Unused (don't care on CXD2510Q, zero on CXD2545Q)
  7-0   8bit  Unused (don't care)
```

#### CXD2510Q - CX(9xx) - Function Specification
```
  23-20 4bit  Command (9)
  19    1bit  DCLV ON-OFF (complex stuff, related to gain and frequencies)
  18    1bit  DSPB ON-OFF (0=Normal Speed, 1=Double Speed; fixed pitch)
  17    1bit  ASEQ ON-OFF (select output on SENS pin)
  16    1bit  DPLL ON-OFF (0=Analog RFPLL, 1=Digital RFPLL)
  15-14 1bit  Bilingual Audio (0=Stereo, 1=RightOnly, 2=LeftOnly, 3=Mute)
  13    1bit  FLFC (normally 0)
  12    1bit  Unused (zero)
  11-8  4bit  Unused (don't care on CXD2510Q, zero on CXD2545Q)
  7-0   8bit  Unused (don't care)
```

#### CXD2510Q - CX(Axx) - Audio Control
```
  23-20 4bit  Command (0Ah)
  19    1bit  Vari Up   (write 1-then-0 to increase pitch by +0.1%)
  18    1bit  Vari Down (write 1-then-0 to decrease pitch by -0.1%)
  17    1bit  Mute (0=Not muted; unless muted elsewhere, 1=Mute & Peak=0)
  16    1bit  ATT  (0=Attentuation off, 1=Minus 12 dB)
  15-14 2bit  PCT  (0=Normal, 1=LevelMeter, 2=PeakMeter, 3=Normal) (0-1=QuadC2)
  13-12 2bit  Unused (zero)
  11-8  4bit  Unused (don't care on CXD2510Q, zero on CXD2545Q)
  7-0   8bit  Unused (don't care)
```
Normal: SQSO outputs... WHAT?<br/>
PeakMeter: SQSO outputs highest peak ever on any channel (bit15: usually 0)<br/>
LevelMeter: SQSO outputs recent peak (with bit15 toggled: 0=Right, 1=Left)<br/>

#### CXD2510Q - CX(Bxxxx) - Traverse Monitor Counter Setting
```
  23-20 4bit  Command (0Bh)
  19-4  16bit Traverse Monitor Count (used when monitored by COMP and COUT) (?)
  3-0   4bit  Unused (don't care)
```

#### CXD2510Q - CX(Cxx) - Spindle Servo Coefficient Setting
```
  23-20 4bit  Command (0Ch)
  19-18 2bit  Gain MDP for CLVP mode (0=-6db, 1=0dB, 1=+6dB, 3=Reserved)
  17-16 2bit  Gain MDS for CLVS/CLVP (0=-12dB, 1=-6dB, 2=0dB, 3=Reserved)
  15    1bit  Zero (zero)
  14    1bit  Gain DCLV0 overall gain (0=0dB, 1=+6dB
  13-12 2bit  Unused (zero)
  11-8  4bit  Unused (don't care on CXD2510Q, zero on CXD2545Q)
  7-0   8bit  Unused (don't care)
```

#### CXD2510Q - CX(Dx) - CLV Control
```
  23-20 4bit  Command (0Dh)
  19    1bit  DCLV PWM MD Digital CLV PWM mode  (0=Use MDS+MDP, 1=Ternary MDP)
  18    1bit  TB Bottom Hold in CLVS/CLVH modes (0=At cycle RFCK/32, 1=RFCK/16)
  17    1bit  TP Peak Hold in CLVS mode         (0=At cycle RFCK/4, 1=RFCK/2)
  16    1bit  Gain CLVS for CLVS mode (0=0dB, 1=+6dB)(always +6dB in CLVP mode)
  15-8  8bit  Unused (don't care on CXD2510Q, zero on CXD2545Q)
  7-0   8bit  Unused (don't care)
```

#### CXD2510Q - CX(Ex) - CLV Mode
```
  23-20 4bit  Command (0Eh)
  19-16 4bit  CM3-0
  15-8  8bit  Unused (don't care on CXD2510Q, zero on CXD2545Q)
  7-0   8bit  Unused (don't care)
```
Values for CM (CLV Mode):<br/>
```
  00h Stop  Spindle Motor Stop mode
  06h CLVA  Automatic CLVS/CLVP switching mode, normally used for playback
  08h Kick  Spindle Motor Forward rotation mode
  0Ah Brake Spindle Motor Reverse rotation mode
  0Ch CLVH  Peak hold at 34kHz
  0Eh CLVS  Rough Servo Mode, RF-PLL related
  0Fh CLVP  PLL Servo mode
```

#### N/A - CX(F) - Reserved
```
  23-0  N/A  Don't use
```

#### SUBQ Output
```
 80bit subq
 15bit peak level (lsb first) (absolute/unsigned value)
 1bit  peak l/r flag (aka appears as "MSB" of peak level)
```
L/R is toggled after each SUBQ reading, however the PSX Report mode does
usually forward SUBQ only every 10 frames, so it stays stuck in one setting
(but may toggle after one second; ie. every 75 frames). And, peak is reset
after each read, so 9 of the 10 frames are lost.<br/>

#### CXD2510Q - SENS output
```
  Index         ASEQ=0  ASEQ=1   ;<-- ASEQ can be set via CX(9xx)
  0X            HighZ   SEIN (FZC)                     ;\aka SENS output
  1X            HighZ   SEIN (A.S)    ... aka DEFECT   ; from CXA1782BR
  2X            HighZ   SEIN (T.Z.C)  ... aka TZC      ; forwarded through
  3X            HighZ   SEIN (SSTOP)  ... aka Gain/Bal ;/CXD2510Q
  4X            HighZ   XBUSY
  5X            HighZ   FOK
  6X            HighZ   SEIN (HighZ)
  AX            GFS     GFS
  BX            COMP    COMP
  CX            COUT    COUT
  EX            /OV64   /OV64
  7X-9X,DX,FX   HighZ   0
```
Whereas,<br/>
```
 FZC    Focus Zero Cross
 DEFECT Defect?
 TZC    Tracking Zero Cross
 SSTOP  Gain or Balance adjust reached wanted level
 XBUSY  Low while the auto sequencer operation is busy
 FOK    High for "focus OK" (same as FOK pin)
 GFS    High when the played back frame sync is obtained with correct timing
 COMP   Measures the number of tracks set with Reg B. High when Reg B is
          latched, low when the initial Reg B number is input by CNIN
 COUT   Measures the number of tracks set with Reg B. High when Reg B is
          latched, toggles each time the Reg B number is input by CNIN. While
          $44 and $45 are being executed, toggles with each CNIN 8-count
          instead of the Reg B number
 OV64   Low when filtered EFM signal is lengthened by 64 channel clock
          pulses or more
```



##   CDROM Internal Commands CX(0x..Ex) - CXD2545Q Servo/Signal Combo
#### CXD2545Q - CX(0x) and CX(2x) - same as CXA1782BR Servo Amplifier
[CDROM Internal Commands CX(0x..3x) - CXA1782BR Servo Amplifier](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-commands-cx0x3x-cxa1782br-servo-amplifier)<br/>

#### CXD2545Q - CX(4x..Ex) - same as CXD2510Q Signal Processor
[CDROM Internal Commands CX(4x..Ex) - CXD2510Q Signal Processor](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-commands-cx4xex-cxd2510q-signal-processor)<br/>
One small difference is that the CXD2545Q supports a new "M Track Move"
function as part of the CX(4xxx) command. And, some "don't care" bits are now
reserved (ie. some commands need to be padded with additional leading "0"
bits).<br/>

#### CXD2545Q - CX(1x) - Anti Shock/Brake/Tracking Gain/Filter
```
  23-20 4bit  Command (01h)
  19    1bit  Anti Shock (0=Off, 1=On)
  18    1bit  Brake      (0=Off, 1=On)
  17    1bit  Tracking Gain (0=Normal, 1=Up)
  16    1bit  Tracking Gain Filter (0=Select 1, 1=Select 2)
  15-0  16bit Unused (don't care)
```

#### CXD2545Q - CX(30..33) - Sled Kick Level
```
  23-20 4bit  Command (03h)
  19-18 2bit  Subcommand (0)
  17-16 2bit  Sled Kick Level (0=+/-1, 1=+/-2, 2=+/-3, 3=+/-4)
  15-0  16bit Unused (don't care)
```

#### CXD2545Q - CX(34xxxx) - Write to Coefficient RAM
```
  23-16 8bit  Command (34h)
  15    1bit  Zero (0)
  14-8  7bit  Address (00h..4Fh = Select Coefficient K00..K4F)
  7-0   8bit  Data    (00h..FFh = New value)
  PLUS  8bit  Eight more bits on PSone (!)
```
Allows to change the default preset coefficient values,<br/>
[CDROM Internal Coefficients (for CXD2545Q)](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-coefficients-for-cxd2545q)<br/>

#### CXD2545Q - CX(34Fxxx) - Write to Special Register
```
  23-12 12bit Command (34Fh)
  11-10 2bit  Index (0=TRVSC, 1=FBIAS, 2=?, 3=?)
  9-0   10bit Data (for FBIAS: bit0=don't care)
```

#### CXD2545Q - CX(35xxxx) - FOCUS SEARCH SPEED/VOLTAGE/AUTO GAIN
```
  23-16 8bit  Command (35h)
  15-14 2bit  FT  Focus Search-up speed 1
  13-8  6bit  FS  Focus Search limit voltage (default 011000b) (+/-1.875V)
  7     1bit  FTZ Focus Search-up speed 2
  6-0   7bit  FG  AGF Convergence Gain Setting (default 0101101b)
```

#### CXD2545Q - CX(36xxxx) - DTZC/TRACK JUMP VOLTAGE/AUTO GAIN
```
  23-16 8bit  Command (36h)
  15    1bit  Zero (0)
  14    1bit  DTZC DTZC Delay (0=4.25us/Default, 1=8.5us)
  13-8  6bit  TJ   Track Jump voltage (default 001110b) (+/-1.09V)
  7     1bit  Zero (0)
  6-0   7bit  TG   AGT Convergence Gain Setting (default 0101110b)
```

#### CXD2545Q - CX(37xxxx) - FZSL/SLED MOVE/Voltage/AUTO GAIN
```
  23-16 8bit  Command (37h)
  15-14 2bit  FZS              XXX pg. 84
  13-8  6bit  SM    Sled Move Voltage
  7     1bit  AGS
  6     1bit  AGJ
  5     1bit  AGGF
  4     1bit  AGGT
  3     1bit  AGV1
  2     1bit  AGV2
  1     1bit  AGHS
  0     1bit  AGHT
```

#### CXD2545Q - CX(38xxxx) - Level/Auto Gain/DFSW (Initialize)
```
  23-16 8bit  Command (38h)
  15    1bit  VCLM VC level measurement on/off
  14    1bit  VCLC VC level compensation for FCS_In Register on/off
  13    1bit  FLM  Focus zero level measurement on/off
  12    1bit  FLC0 Focus zero level compensation for FZC Register on/off
  11    1bit  RFLM RF zero level measurement on/off
  10    1bit  RFLC RF zero level compensation on/off
  9     1bit  AGF  Focus automatic gain adjustment on/off
  8     1bit  AGT  Tracking automatic gain adjustment on/off
  7     1bit  DFSW Defect switch disable (1=disable defect measurement)
  6     1bit  LKSW Lock switch (1=disable sled free-running prevention)
  5     1bit  TBLM Traverse center measurement on/off
  4     1bit  TCLM Tracking zero level measurement on/off
  3     1bit  FLC1 Focus zero level compensation for FCS_In Register on/off
  2     1bit  TLC2 Traverse center compensation on/off
  1     1bit  TLC1 Tracking zero level compensation on/off
  0     1bit  TLC0 VC level compensation for TRK/SLD_In register on/off
```
VCLM,FLM,RFLM,TCLM are accepted every 2.9ms.<br/>

#### CXD2545Q - CX(39xx) - Select internal RAM/Registers for serial readout
```
  23-16 8bit  Command (39h)
  15    1bit  DAC Serial data readout DAC mode on/off
  14-8  7bit  SD  Serial readout data select (see below)
  7-0   8bit  Unused (don't care)
```
Serial Readout Addresses:<br/>
```
  Addr    Data  Content
  00h     8bit  VC input signal
  01h     8bit  SE input signal
  02h     8bit  TE input signal
  03h     8bit  FE input signal
  04h-07h 9bit  TE AVRG register (mirrored to 04h-07h)
  08h-0Bh 9bit  FE AVRG register (mirrored to 08h-0Bh)
  0Ch-0Fh 9bit  VC AVRG register (mirrored to 0Ch-0Fh)
  12h     8bit  RFDC envelope (peak)
  13h     8bit  RFDC envelope (bottom)
  1Ch     9bit  TRVSC register
  1Dh     9bit  FBIAS register
  1Eh     8bit  RFDC input signal
  1Fh     8bit  RF AVRG register
  20h-3Fh 16bit Data RAM        (M00-M1F)
  40h-7Fh 8bit  Coefficient RAM (K00-K3F) (note: K40-K4F cannot be read out)
```

#### CXD2545Q - CX(3Ax000) - Focus BIAS addition enable
```
  23-16 8bit  Command (3Ah)
  15    1bit  Zero (0)
  14    1bit  FBON: FBIAS register addition (0=off, 1=Add FBIAS to FCS)
  13-0  14bit Zero (0)
```

#### CXD2545Q - CX(3Bxxxx) - Operation for MIRR/DFCT/FOK
```
  23-16 8bit  Command (3Bh)
  15-14 2bit  SFO  FOK Slice Level (...depends on SFOX)
  13-12 2bit  SDF  DFCT Slice Level (0=89mV, 1=134mV, 2=179mV, 3=224mV)
  11-10 2bit  MAX  DFCT Maximum Time (0=No Limit, 1=2ms, 2=2.36ms, 3=2.72ms)
  9     1bit  SFOX FOK Slice Level (...depends on SFO)
  8     1bit  BTF  Bottom Hold Double-Speed Count-Up mode for MIRR (0=off)
  7-6   2bit  D2V  Peak Hold 2 for DFCT (0=22.05kHz, 1=44.1, 2=88.2, 3=176.4)
  5-4   2bit  D1V  Peak Hold 1 for DFCT (0=176.4kHz, 1=352.8, 2=705.6, 3=1411)
  3-0   4bit  Zero (0)
```

#### CXD2545Q - CX(3Cxxxx) - TZC for COUT SLCT HPTZC (Default)
```
  23-16 8bit  Command (3Ch)
  15-0  16bit Unused (don't care)
```

#### CXD2545Q - CX(3Dxxxx) - TZC for COUT SLCT DTZC
```
  23-16 8bit  Command (3Dh)
  15-0  16bit Unused (don't care)
```

#### CXD2545Q - CX(3Exxxx) - Filter
```
  23-16 8bit  Command (3Eh)
  15-14 2bit  F1NDM FCS servo filter 1st stage (1=normal, 2=down)
  13-12 2bit  F3NUM FCS servo filter 3rd stage (1=normal, 2=up)
  11-10 2bit  T1NDM TRK servo filter 1st stage (1=normal, 2=down)
  9-8   2bit  T3NUM TRK servo filter 3rd stage (1=normal, 2=up)
  7     1bit  DFIS  FCS hold filter input extraction node (0=M05, 1=M04)
  6     1bit  TLCD  Mask TLC2 set by D2 of CX(38) only when FOK low
  5     1bit  RFLP  Pass signal from RFDC pin through low-pass-filter
  4-0   5bit  Zero (0)
```

#### CXD2545Q - CX(3Fxxxx) - Others
```
  23-16 8bit  Command (3Fh)          ... XXX pg. 89
  15-14 2bit  Unused (0)
  13-12 2bit  XTD
  11    1bit  Unused (0)
  10-8  3bit  DRR
  7     1bit  Unused (0)
  6     1bit  ASFG
  5     1bit  Unused (0)
  4     1bit  LPAS
  3-2   2bit  SRO
  1-0   2bit  Unused (0)
```

#### CXD2545Q feedback on 39xx: see pg. 77 (eg. 390C = VC AVRG)
XXX<br/>

#### CXD2545Q - SENS output
```
  Index          ASEQ=0  ASEQ=1           Length
  $0X            Z       FZC              -
  $1X            Z       AS               -
  $2X            Z       TZC              -
  $38            Z       AGOK*1           -
  $38            Z       XAVEBSY*1        -
  $30-37,$3A-3F  Z       SSTP             -
  $3904          Z       TE Avrg Reg.     9 bit
  $3908          Z       FE Avrg Reg.     9 bit
  $390C          Z       VC Avrg Reg.     9 bit
  $391C          Z       TRVSC Reg.       9 bit
  $391D          Z       FB Reg.          9 bit
  $391F          Z       RFDC Avrg Reg.   8 bit
  $4X            Z       XBUSY            -
  $5X            Z       FOK              -
  $6X            Z       0                -
  $AX            GFS     GFS              -
  $BX            COMP    COMP             -
  $CX            COUT    COUT             -
  $EX            OV64    OV64             -
  $7X-9X,DX,FX   Z       0                -
```
\*1 $38 outputs AGOK during AGT and AGF command settings, and XAVEBSY during
AVRG measurement.<br/>
SSTP is output in all other cases.<br/>



##   CDROM Internal Commands CX(0x..Ex) - CXD2938Q Servo/Signal/SPU Combo
Most commands are same as on CXD2545Q. New/changed commands are:<br/>

#### CXD2938Q - CX(349xxxxx) - New SCEx
Older PSX consoles have received the "SCEx" string at 250 baud via HC05
PortB.bit1, which allowed modchips to injected faked "SCEx" signals to that
pin. To prevent that, the CXD2938Q contains some new 32bit commands that allow
to receive somewhat encrypted "SCEx" strings via SPI bus. The used commands
are:<br/>
```
  CX(34910000) NewScexStopReading
  CX(3491xy80) NewScexRandomKey(xy)
  CX(34920000) NewScexFlushResyncOrSo
  CX(34944A00) NewScexInitValue1
  CX(3498C000) NewScexInitValue2
  CX(349C1000) NewScexThis   ;\inverse  ;\use CX(3C2080) for COUT selection
  CX(349D1000) NewScexThat   ;/of COUT  ;/
```
The relevant command is NewScexRandomKey(xy) which does send a random value
(x=01h..0Fh, and y=01h), and does then receive a 12-byte response via SPI bus
(which is normally used to receive SUB-Q data).<br/>
```
  1st byte: Unknown/unused (normally ADR/Control) ;\these should be probably
  2nd byte: Unknown/unused (normally Track)       ; set to some invalid values
  3rd byte: Unknown/unused (normally Index/Point) ;/to avoid SUB-Q confusion
  4th..10th byte: SCEx data or Dummy bytes (depending on xy.bit7..1)
  11th..12th byte: Unknown/unused (normally Audio Peak level)
```
The 12-byte packet does contain one SCEx character encoded in 4th..10th byte
corresponding to Flags in "xy" bit 7..1 (in that order):<br/>
All bytes with Flag=1 are ORed together to compute a Character byte (those
bytes could be all set to 53h for "S", or if more than one flag is set, it
could be theoretically split to something like 41h and 12h).<br/>
All bytes with Flag=0 are ORed together to compute a Dummy byte. If the
Character byte is same as the Dummy byte, then it gets destroyed by setting
Character=00h (to avoid that, one could set all dummies to 00h, or set one or
more dummies to FFh, for example).<br/>
Finally, "xy" bit0=0 indicates that the resulting character byte is inverted
(XORed by FFh), however, the CDROM BIOS does always use bit0=1, so the
inversion feature is never used.<br/>
For the whole SCEx string, there must be at least one 00h byte inserted between
each character (or some Char=Dummy mismatch, which results in Char=00h either),
and there should be a few more 00h bytes preceeding the first character ("S").<br/>
Note: Modchips didn't bother to reproduce that new SCEx transfers, instead they
have simply bypassed it by injecting the 250 baud SCEx string to some analog
lower level signal.<br/>

#### CXD2938Q - CX(3Bxxxx) - Some Changed Bits
Same as in older version, but initialized slightly differently: CXD2545Q used
CX(3B2250) whilst CXD2938Q is using CX(3B7250).<br/>

#### CXD2938Q - CX(3Cxxxx) - TzcCoutSelect with New/Changed Extra Bits
The CXD2545Q used two 8bit commands, CX(3C) and CX(3D), for TzcOut selection,
which are now replaced by a single 24bit command, CX(3Cxxxx), and which do
include a new mode related to New SCEx.<br/>
```
  CXD2545Q   CXD2938Q
  CX(3C)     CX(3C0080) TzcCoutSelectHPTZC;\ <--formerly CX(3C)
  -          CX(3C2080) TzcCoutSelectSCEX ;  <--special NewScex mode
  CX(3D)     CX(3C4080) TzcCoutSelectDTZC ;/ <--formerly CX(3D)
```

#### CXD2938Q - CX(8xxxxx) - Disc Mode with New/Changed Extra Bits
Command CX(8xx) has been 12bit wide on CXD2545Q, and is now expanded 24bit
width (with some changed/unknown bits).<br/>
```
  CXD2545Q   CXD2938Q
  CX(8180)   CX(810408) MODE = Audio (CD-DA)
  CX(8120)   CX(812400) MODE = Audio (CD-DA) (manual SPI bus access)
  CX(8980)   CX(890408) MODE = CDROM (Data)
  -          CX(898000) MODE = CDROM (Data) (used on RESET)
```

#### CXD2938Q - CX(9xx000) - Normal/Double Speed with New Extra Bits
Command CX(9xx) has been 12bit wide on CXD2545Q (with bit12=reserved/zero), and
is now expanded 24bit width (with bit12=unknown/one and bit11-0=unknown/zero).<br/>

#### CXD2938Q - CX(Dx0000) and CX(Ex0000) - New Zero Padding
Commands CX(Dx) and CX(Ex) have been 8bit wide on CXD2545Q, and are now
zeropadded to 24bit width, ie. CX(Dx0000) and CX(Ex0000). Unknown if the extra
bits are hiding any extra features. In practice, the CDROM BIOS is always
setting them zero (except in some test commands which are accidently still
using the old 8bit form, resulting in garbage in lower 16bits).<br/>



##   CDROM Internal Commands CX(xx) - Notes
#### Serial Command Transmission (for Signal Processor and Servo Amplifier)
Commands are sent serially LSB first via DATA,CLOK,XLAT pins: DATA+CLOK are
used to send commands to the chip, command execution is then applied by
dragging XLAT low for a moment.<br/>
Commands can be up to 24bits in length, but unused LSBs (the "don't care" bits)
can be omitted; the PSX BIOS clips the length to 8bit/16bit where possible (due
to the LSB-first transfer order, the chip does treat the most recently
transferred bit as MSB=bit23, and there's no need to transfer the LSBs if they
aren't used).<br/>
Aside from being used as command number, the four most recently transferred
bits are also used to select SENS status feedback (for the SENS selection it
doesn't matter if the four bits were terminated by XLAT or not).<br/>

#### Sled Motor / Track Jumps / Tracking
The Sled motor moves the drive head to the current read position. On a Compact
Disc, the term "Track" does normally refer to Audio tracks (songs). But the
drive hardware uses the terms "Track" and "Tracking" for different purposes:<br/>
Tracking appears to refer to moving the Optics via magnets (ie. moving only the
laser/lens, without actually moving the whole sled) (this is done for fine
adjustments, and it seems to happen more or less automatically; emulators can
just return increasing sectors without needing to handle special tracking
commands).<br/>
Track jumps refer to moving the entire Sled, one "track" is equal to one spiral
winding (1.6 micrometers). One winding contains between 9 sectors on innermost
windings, and 22.5 sectors on outermost windings (the PSX cdrom bios is
translating the sector-distance to non-linear track-distance, and emulators
must undo that translation; otherwise the sled doesn't arrive at the intended
location; the cdrom bios will retry seeking a couple of times and eventually
settle down at the desired location - but it will timeout if the sled emulation
is too inaccurate).<br/>
The PSX hardware uses two mechanisms for moving the Sled:<br/>
Command CX(4xxx) Forward/Reverse Track Jump: allows to move the sled by
1..131070 tracks (ie. max 210 millimeters), and the hardware does stop
automatically after reaching the desired distance.<br/>
Command CX(2x) Forward/Reverse Fast Sled: moves the sled continously until it
gets stopped by another command (in this mode, software can watch the COUT
signal, which gets toggled each "N" tracks; whereas "N" can be selected via
Command CX(Bxxxx), which is configured to N=100h in PSX).<br/>
The PSX cdrom bios is issuing another Fast Sled command (in opposite direction)
after Fast Sled commands, emulators must somehow interprete this as "sled
slowdown" (rather than as actually moving the sled in opposite direction, which
could move the sled miles away from the target). For some reason vC1 BIOS is
using a relative short slowdown period, whilst vC2/vC3 are using much longer
slowdown periods (probably related to different SledKickHeight aka
SledKickLevel settings and/or to different Sled Move Voltage settings).<br/>

#### Focus / Gain / Balance
The hardware includes commands for adjusting & measuring
focus/gain/balance. Emulators can just omit that stuff, and can always
signalize good operation (except that one should emulate failures for Disc
Missing; and eventually also for cases like Laser=Off, or Spindle=Stopped).<br/>
Focus does obviously refer to moving the lens up/down. Gain does probably refer
to reflection level/laser intensity. Balance might refer to tracking
adjustments or so.<br/>



##   CDROM Internal Commands CX(xx) - Summary of Used CX(xx) Commands
The PSX CDROM BIOS versions vC1, vC2, and vC3 are using following CX()
commands:<br/>
```
<B>  <--vC1-->  <--vC2-->  <--vC3--></B>
<B>  CXD2510Q   CXD2545Q   CXD2938Q</B>
  CX(00)     CX(00)     CX(00)     AllFocusSwitchesOff
  CX(02)     CX(02)     CX(02)     FocusSearchVoltageFalling
  CX(03)     CX(03)     CX(03)     FocusSearchVoltageRising ;ForTestOnly
  CX(08)     CX(08)     CX(08)     FocusServoOn
  CX(0C)     CX(0C)     CX(0C)     FocusServoOnAndDefectOn ;diff.usage vC# ?
  -----
  CX(11)     -          -          SledKickHeight2
  CX(12)     -          -          SledKickHeightInvalid
  CX(19)     -          -          TrackingGainAndSledKickHeight2
  CX(1D)     -          -          TrackingGainBrakeAndSledKickHeight2
  CX(1E)     -          -          TrackingGainBrakeAndSledKickHeightInvalid
  -----
  -          CX(11)     CX(11)     AntiShockOff            ;\
  -          CX(13)     CX(13)     AntiShockOffGainUp      ;
  -          CX(17)     CX(17)     AntiShockOffGainUpBrake ;/
  -----
  CX(20)     CX(20)     CX(20)     SledAndTrackingOff
  CX(21)     CX(21)     CX(21)     SledServoOn          ;ForTestOnly
  CX(22)     CX(22)     CX(22)     SledFastForward
  CX(23)     CX(23)     CX(23)     SledFastReverse
  CX(24)     -          -          TrackingServoOn
  CX(25)     CX(25)     CX(25)     SledAndTrackingServoOn
  -          CX(26)     CX(26)     SledFastForwardAndTrackingServoOn
  CX(28)     CX(28)     CX(28)     TrackingForwardJump  ;ForTestOnly
  CX(2C)     CX(2C)     CX(2C)     TrackingReverseJump  ;ForTestOnly
  -----
  CX(30+n)   -          -          BalanceAdjust(0..7)
  CX(38+n)   -          -          GainAdjust(0..7)
  -----
  -          CX(30)     CX(30)     SetSledKickLevel1       ;\
  -          CX(31)     CX(31)     SetSledKickLevel2       ;
  -          CX(32)     CX(32)     SetSledKickLevel3       ;/
  -----
  -          CX(3400E6) CX(3400E6) SetK00toE6hSledInputGain            ;def=E0h
  -          CX(340730) CX(340730) SetK07to30hSledAutoGain       ;blah ;def=30h
  -          CX(34114A) CX(34114A) SetK11to4AhFocusOutputGain          ;def=32h
  -          CX(341330) CX(341330) SetK13to30hFocusAutoGain      ;blah ;def=30h
  -          CX(341D6F) CX(341D6F) SetK1Dto6FhTrackingLowBoostFilterAL ;def=44h
  -          CX(341F64) CX(341F64) SetK1Fto64hTrackingLowBoostFilterBL ;def=5Eh
  -          CX(342220) CX(342220) SetK22to20hTrackingOutputGain       ;def=18h
  -          CX(342330) CX(342330) SetK23to30hTrackingAutoGain   ;blah ;def=30h
  -          CX(342D28) CX(342D28) SetK2Dto28hFocusGainDownOutputGain  ;def=1Bh
  -          CX(343E70) CX(343E70) SetK3Eto70hTrackingGainUpOutputGain ;def=57h
  -          -          CX(34910000) NewScexStopReading      ;\
  -          -          CX(3491x180) NewScexRandomKey(x)     ;
  -          -          CX(34920000) NewScexFlushResyncOrSo  ; SCEX SPECIAL
  -          -          CX(34944A00) NewScexInitValue1       ; see also:
  -          -          CX(3498C000) NewScexInitValue2       ; CX(3C2080)
  -          -          CX(349C1000) NewScexThis   ;\inverse ;
  -          -          CX(349D1000) NewScexThat   ;/of COUT ;/
  -          CX(34F000) CX(34F000) SetTRVSCto000h
  -          CX(34Fxxx) CX(34Fxxx) SetFBIAStoNNNh
  -----
  -          CX(3740AA) CX(3740AA) SetSMto00h      ;\set SM to 0,6,7,9
  -          CX(3746AA) CX(3746AA) SetSMto06h      ; (sled move voltage)
  -          CX(3747AA) CX(3747AA) SetSMto07h      ; (and init several
  -          CX(3749AA) CX(3749AA) SetSMto09h      ;/fixed settings)
  -----
  -          CX(380010) CX(380010) ModeMeasureTrackingZeroLevel ;\Measure modes
  -          CX(380800) CX(380800) ModeMeasureRfZeroLevel       ; (accepted
  -          CX(382000) CX(382000) ModeMeasureFocusZeroLevel    ; every 2.9ms)
  -          CX(388000) CX(388000) ModeMeasureVcLevel           ;/
  -          CX(38140A) CX(38140A) ModeCompensate
  -          CX(38140E) CX(38140E) ModeCompensateAndTraverseCenter
  -          CX(38148A) CX(38148A) ModeCompensateAndDefectOff
  -          CX(38148E) CX(38148E) ModeCompensateAndDefectOffTraverseCenter
  -          CX(3814AA) CX(3814AA) ModeCompensateAndStuffAndMeasureTraverse ;!
  -          CX(38150A) CX(38150A) ModeCompensateAndTrackingAutoGain
  -          CX(38150E) CX(38150E) ModeCompensateAndTrackingAutoGain
  -          CX(38160A) CX(38160A) ModeCompensateAndFocusAutoGain
  -----
  -          CX(391E)   -          SenseRFDCinputSignalWithoutDAC  ;\rather
  -          CX(3983)   -          SenseFEinputSignalWithDAC       ;/unused
  -          CX(399C)   -          SenseTRVSCregisterWithDAC       ;\only if
  -          CX(399D)   -          SenseFBIASregisterWithDAC       ;/TEST1=LOW
  -----
  -          CX(3A0000) CX(3A0000) FocusBiasAdditionOff            ;\
  -          CX(3A4000) CX(3A4000) FocusBiasAdditionOn             ;/
  -          CX(3B2250)!CX(3B7250)!InitOperationForMirrDfctFok <-- vC2/vC3 DIFF
  -          CX(3C)  !!!CX(3C0080) TzcCoutSelectHPTZC;\ <--formerly CX(3C)
  -          -       !!!CX(3C2080) TzcCoutSelectSCEX ;  <--special NewScex mode
  -          CX(3D)  !!!CX(3C4080) TzcCoutSelectDTZC ;/ <--formerly CX(3D)
  -          CX(3E0000) CX(3E0000) InitFilterBits                  ;\
  -          CX(3E0008) CX(3E0008) InitFilterBitsInvalid           ;/
  -          CX(3F0008) CX(3F0008) InitOtherStuff                  ;-
  -----
  CX(4000)   CX(4000)   CX(4000)   AutoSeqCancel
  CX(4700)   CX(4700)   CX(4700)   AutoSeqFocusOn
  CX(4800)   CX(4800)   CX(4800)   Forward1track
  CX(4900)   CX(4900)   CX(4900)   Reverse1track
  CX(4C00)   CX(4C00)   CX(4C00)   Forward2Ntrack
  CX(4D00)   CX(4D00)   CX(4D00)   Reverse2Ntrack
  -----
  CX(54)     CX(54)     CX(54)     BlindBrakeOverflowTimer=4
  CX(5A)     CX(5A)     CX(5A)     BlindBrakeOverflowTimer=A
  CX(6100)   CX(6100)   CX(6100)   SledKickBrakeKickTimer
  CX(70xxx0) CX(70xxx0) CX(70xxx0) TrackJumpCountSetting
  CX(8180)   CX(8180)!!!CX(810408) MODE = Audio (CD-DA)
  -          CX(8120)!!!CX(812400) MODE = Audio (CD-DA) (manual SPI bus access)
  -          -          CX(810000/UNUSED)
  -          -          CX(812000/UNUSED)
  CX(8980)   CX(8980)   CX(890408) MODE = CDROM (Data)
  -          -          CX(898000) MODE = CDROM (Data) (used on RESET)
  CX(9B00)   CX(9B00)!!!CX(9B1000) NormalSpeed
  CX(9F00)   CX(9F00)!!!CX(9F1000) DoubleSpeed
  CX(A040)   CX(A040)   CX(A040)   Attentuation Off
  CX(A140)   CX(A140)   CX(A140)   Attentuation -12 dB
  CX(B01000) CX(B01000) CX(B01000) TraverseMonitorCounterSetting
  CX(C600)   CX(C600)   CX(C600)   SpindleServoCoefficientSetting
  CX(D7)     CX(D7)     CX(D70000) ClvControl (fixed)
  CX(E0)     CX(E0)     CX(E00000) SpindleMotorStop
  -          -          CX(E02000) <-- aka bugged CX(E0) with CRAP=2000h
  CX(E6)     CX(E6)     CX(E60000) AutomaticNormal
  CX(E8)     CX(E8)     CX(E80000) SpindleMotorForward
  -          -          CX(E8crap) <-- aka bugged CX(E8) with CRAP=xxxxh
  CX(EA)     CX(EA)     CX(EA0000) SpindleMotorReverse
  -          -          CX(EAcrap) <-- aka bugged CX(EA) with CRAP=xxxxh
  CX(EE)     CX(EE)     CX(EE0000) RoughServo
  -----
  CX(F)      CX(F)      CX(F)      Unused (N/A)
  -----
  CX(Xx)     CX(Xx)     CX(Xx)       ;\
  CX(Xxxx)   CX(Xxxx)   CX(Xxxx)     ; TestCommand (cmd_19h_50h)
  CX(Xxxxxx) CX(Xxxxxx) CX(Xxxxxx)   ;
  -          -          CX(Xxxxxxxx) ;/
  -          CX(Xxxxxx) CX(Xxxxxx) SerialSense, CX(Xxxx) with extra 8bit junk
```
Note: for vC2, some CX(38xxxx) values may differ depending on
"set\_mid\_lsb\_to\_140Eh".<br/>
For vC2, CX(Dx) and CX(Ex) should be officially zero-padded to CX(Dx00) and
CX(Ex00), but the vC2 BIOS doesn't do that, it still uses short 8bit form.<br/>
For vC2, CX(Dx) and CX(Ex) should be apparently zero-padded to CX(Dx0000) and
CX(Ex0000), at least, the vC3 BIOS is doing so (except on some test comannds
that do still use the CX(Ex) short form).<br/>

#### Used Sense Values
```
  sense(30)  SEIN.BAL       ;vC2: SSTP
  sense(38)  SEIN.GAIN      ;vC2: AGOK(AGT/AGF) or XAVEBSY(AVRG) or SSTP(else?)
  sense(40)  XBUSY (low=AutoSeqBusy)
  sense(50)  FOK   (high=FokusOkay)
  sense(A0)  GFS   (high=GoodFrameSync, ie. CorrectPlaybackSpeed)
  sense(C5)  COUT  (toggles each 100h 'tracks') (100h=selected via CX(B01000))
  sense(EA)  /OV64 (low=EFM too long?)
```



##   CDROM Internal Coefficients (for CXD2545Q)
The CXD2545Q contains Preset Coefficients in internal ROM, which are copied to
internal Coefficient RAM shortly after Reset. CX(34xxxx) allows to change those
RAM settings, and CX(39xxxx) allows to readout some of those values serially.<br/>

#### CXD2545Q - Coefficient Preset Values
```
  Addr Val Expl.
  K00  E0  Sled input gain
  K01  81  Sled low boost filter A-H
  K02  23  Sled low boost filter A-L
  K03  7F  Sled low boost filter B-H
  K04  6A  Sled low boost filter B-L
  K05  10  Sled output gain
  K06  14  Focus input gain
  K07  30  Sled auto gain
  K08  7F  Focus high cut filter A
  K09  46  Focus high cut filter B
  K0A  81  Focus low boost filter A-H
  K0B  1C  Focus low boost filter A-L
  K0C  7F  Focus low boost filter B-H
  K0D  58  Focus low boost filter B-L
  K0E  82  Focus phase compensate filter A
  K0F  7F  Focus defect hold gain
  K10  4E  Focus phase compensate filter B
  K11  32  Focus output gain
  K12  20  Anti shock input gain
  K13  30  Focus auto gain
  K14  80  HPTZC / Auto Gain High pass filter A
  K15  77  HPTZC / Auto Gain High pass filter B
  K16  80  Anti shock high pass filter A
  K17  77  HPTZC / Auto Gain low pass filter B
  K18  00  Fix (should not change this preset value)
  K19  F1  Tracking input gain
  K1A  7F  Tracking high cut filter A
  K1B  3B  Tracking high cut filter B
  K1C  81  Tracking low boost filter A-H
  K1D  44  Tracking low boost filter A-L
  K1E  7F  Tracking low boost filter B-H
  K1F  5E  Tracking low boost filter B-L
  K20  82  Tracking phase compensate filter A
  K21  44  Tracking phase compensate filter B
  K22  18  Tracking output gain
  K23  30  Tracking auto gain
  K24  7F  Focus gain down high cut filter A
  K25  46  Focus gain down high cut filter B
  K26  81  Focus gain down low boost filter A-H
  K27  3A  Focus gain down low boost filter A-L
  K28  7F  Focus gain down low boost filter B-H
  K29  66  Focus gain down low boost filter B-L
  K2A  82  Focus gain down phase compensate filter A
  K2B  44  Focus gain down defect hold gain
  K2C  4E  Focus gain down phase compensate filter B
  K2D  1B  Focus gain down output gain
  K2E  00  Not used
  K2F  00  Not used
  K30  80  Fix (should not change this preset value)
  K31  66  Anti shock low pass filter B
  K32  00  Not used
  K33  7F  Anti shock high pass filter B-H
  K34  6E  Anti shock high pass filter B-L
  K35  20  Anti shock filter comparate gain
  K36  7F  Tracking gain up2 high cut filter A
  K37  3B  Tracking gain up2 high cut filter B
  K38  80  Tracking gain up2 low boost filter A-H
  K39  44  Tracking gain up2 low boost filter A-L
  K3A  7F  Tracking gain up2 low boost filter B-H
  K3B  77  Tracking gain up2 low boost filter B-L
  K3C  86  Tracking gain up phase compensate filter A
  K3D  0D  Tracking gain up phase compensate filter B
  K3E  57  Tracking gain up output gain
  K3F  00  Not used
  K40  04  Tracking hold filter input gain
  K41  7F  Tracking hold filter A-H
  K42  7F  Tracking hold filter A-L
  K43  79  Tracking hold filter B-H
  K44  17  Tracking hold filter B-L
  K45  6D  Tracking hold filter output gain
  K46  00  Not used
  K47  00  Not used
  K48  02  Focus hold filter input gain
  K49  7F  Focus hold filter A-H
  K4A  7F  Focus hold filter A-L
  K4B  79  Focus hold filter B-H
  K4C  17  Focus hold filter B-L
  K4D  54  Focus hold filter output gain
  K4E  00  Not used
  K4F  00  Not used
```
