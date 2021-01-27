#   CPU Specifications
#### CPU
[CPU Registers](cpuspecifications.md#cpu-registers)<br/>
[CPU Opcode Encoding](cpuspecifications.md#cpu-opcode-encoding)<br/>
[CPU Load/Store Opcodes](cpuspecifications.md#cpu-loadstore-opcodes)<br/>
[CPU ALU Opcodes](cpuspecifications.md#cpu-alu-opcodes)<br/>
[CPU Jump Opcodes](cpuspecifications.md#cpu-jump-opcodes)<br/>
[CPU Coprocessor Opcodes](cpuspecifications.md#cpu-coprocessor-opcodes)<br/>
[CPU Pseudo Opcodes](cpuspecifications.md#cpu-pseudo-opcodes)<br/>

#### System Control Coprocessor (COP0)
[COP0 - Register Summary](cpuspecifications.md#cop0-register-summary)<br/>
[COP0 - Exception Handling](cpuspecifications.md#cop0-exception-handling)<br/>
[COP0 - Misc](cpuspecifications.md#cop0-misc)<br/>
[COP0 - Debug Registers](cpuspecifications.md#cop0-debug-registers)<br/>



##   CPU Registers
All registers are 32bit wide.<br/>
```
  Name       Alias    Common Usage
  (R0)       zero     Constant (always 0) (this one isn't a real register)
  R1         at       Assembler temporary (destroyed by some pseudo opcodes!)
  R2-R3      v0-v1    Subroutine return values, may be changed by subroutines
  R4-R7      a0-a3    Subroutine arguments, may be changed by subroutines
  R8-R15     t0-t7    Temporaries, may be changed by subroutines
  R16-R23    s0-s7    Static variables, must be saved by subs
  R24-R25    t8-t9    Temporaries, may be changed by subroutines
  R26-R27    k0-k1    Reserved for kernel (destroyed by some IRQ handlers!)
  R28        gp       Global pointer (rarely used)
  R29        sp       Stack pointer
  R30        fp(s8)   Frame Pointer, or 9th Static variable, must be saved
  R31        ra       Return address (used so by JAL,BLTZAL,BGEZAL opcodes)
  -          pc       Program counter
  -          hi,lo    Multiply/divide results, may be changed by subroutines
```
R0 is always zero.<br/>
R31 can be used as general purpose register, however, some opcodes are using it
to store the return address: JAL, BLTZAL, BGEZAL. (Note: JALR can optionally
store the return address in R31, or in R1..R30. Exceptions store the return
address in cop0r14 - EPC).<br/>

#### R29 (SP) - Full Decrementing Wasted Stack Pointer
The CPU doesn't explicitly have stack-related registers or opcodes, however,
conventionally, R29 is used as stack pointer (SP). The stack can be accessed
with normal load/store opcodes, which do not automatically increase/decrease
SP, so the SP register must be manually modified to (de-)allocate data.<br/>
The PSX BIOS is using "Full Decrementing Wasted Stack".<br/>
Decrementing means that SP gets decremented when allocating data (that's common
for most CPUs) - Full means that SP points to the first ALLOCATED word on the
stack, so the allocated memory is at SP+0 and above, free memory at SP-1 and
below, Wasted means that when calling a sub-function with N parameters, then
the caller must pre-allocate N works on stack, and the sub-function may freely
use and destroy these words; at [SP+0..N\*4-1].<br/>

For example, "push ra,r16,r17" would be implemented as:<br/>
```
  sub  sp,20h
  mov  [sp+14h],ra
  mov  [sp+18h],r16
  mov  [sp+1Ch],r17
```
where the allocated 20h bytes have the following purpose:<br/>
```
  [sp+00h..0Fh]  wasted stack (may, or may not, be used by sub-functions)
  [sp+10h..13h]  8-byte alignment padding (not used)
  [sp+14h..1Fh]  pushed registers
```




##   CPU Opcode Encoding
#### Primary opcode field (Bit 26..31)
```
  00h=SPECIAL 08h=ADDI  10h=COP0 18h=N/A   20h=LB   28h=SB   30h=LWC0 38h=SWC0
  01h=BcondZ  09h=ADDIU 11h=COP1 19h=N/A   21h=LH   29h=SH   31h=LWC1 39h=SWC1
  02h=J       0Ah=SLTI  12h=COP2 1Ah=N/A   22h=LWL  2Ah=SWL  32h=LWC2 3Ah=SWC2
  03h=JAL     0Bh=SLTIU 13h=COP3 1Bh=N/A   23h=LW   2Bh=SW   33h=LWC3 3Bh=SWC3
  04h=BEQ     0Ch=ANDI  14h=N/A  1Ch=N/A   24h=LBU  2Ch=N/A  34h=N/A  3Ch=N/A
  05h=BNE     0Dh=ORI   15h=N/A  1Dh=N/A   25h=LHU  2Dh=N/A  35h=N/A  3Dh=N/A
  06h=BLEZ    0Eh=XORI  16h=N/A  1Eh=N/A   26h=LWR  2Eh=SWR  36h=N/A  3Eh=N/A
  07h=BGTZ    0Fh=LUI   17h=N/A  1Fh=N/A   27h=N/A  2Fh=N/A  37h=N/A  3Fh=N/A
```

#### Secondary opcode field (Bit 0..5) (when Primary opcode = 00h)
```
  00h=SLL   08h=JR      10h=MFHI 18h=MULT  20h=ADD  28h=N/A  30h=N/A  38h=N/A
  01h=N/A   09h=JALR    11h=MTHI 19h=MULTU 21h=ADDU 29h=N/A  31h=N/A  39h=N/A
  02h=SRL   0Ah=N/A     12h=MFLO 1Ah=DIV   22h=SUB  2Ah=SLT  32h=N/A  3Ah=N/A
  03h=SRA   0Bh=N/A     13h=MTLO 1Bh=DIVU  23h=SUBU 2Bh=SLTU 33h=N/A  3Bh=N/A
  04h=SLLV  0Ch=SYSCALL 14h=N/A  1Ch=N/A   24h=AND  2Ch=N/A  34h=N/A  3Ch=N/A
  05h=N/A   0Dh=BREAK   15h=N/A  1Dh=N/A   25h=OR   2Dh=N/A  35h=N/A  3Dh=N/A
  06h=SRLV  0Eh=N/A     16h=N/A  1Eh=N/A   26h=XOR  2Eh=N/A  36h=N/A  3Eh=N/A
  07h=SRAV  0Fh=N/A     17h=N/A  1Fh=N/A   27h=NOR  2Fh=N/A  37h=N/A  3Fh=N/A
```

#### Opcode/Parameter Encoding
```
  31..26 |25..21|20..16|15..11|10..6 |  5..0  |
   6bit  | 5bit | 5bit | 5bit | 5bit |  6bit  |
  -------+------+------+------+------+--------+------------
  000000 | N/A  | rt   | rd   | imm5 | 0000xx | shift-imm
  000000 | rs   | rt   | rd   | N/A  | 0001xx | shift-reg
  000000 | rs   | N/A  | N/A  | N/A  | 001000 | jr
  000000 | rs   | N/A  | rd   | N/A  | 001001 | jalr
  000000 | <-----comment20bit------> | 00110x | sys/brk
  000000 | N/A  | N/A  | rd   | N/A  | 0100x0 | mfhi/mflo
  000000 | rs   | N/A  | N/A  | N/A  | 0100x1 | mthi/mtlo
  000000 | rs   | rt   | N/A  | N/A  | 0110xx | mul/div
  000000 | rs   | rt   | rd   | N/A  | 10xxxx | alu-reg
  000001 | rs   | 00000| <--immediate16bit--> | bltz
  000001 | rs   | 00001| <--immediate16bit--> | bgez
  000001 | rs   | 10000| <--immediate16bit--> | bltzal
  000001 | rs   | 10001| <--immediate16bit--> | bgezal
  00001x | <---------immediate26bit---------> | j/jal
  00010x | rs   | rt   | <--immediate16bit--> | beq/bne
  00011x | rs   | N/A  | <--immediate16bit--> | blez/bgtz
  001xxx | rs   | rt   | <--immediate16bit--> | alu-imm
  001111 | N/A  | rt   | <--immediate16bit--> | lui-imm
  100xxx | rs   | rt   | <--immediate16bit--> | load rt,[rs+imm]
  101xxx | rs   | rt   | <--immediate16bit--> | store rt,[rs+imm]
  x1xxxx | <------coprocessor specific------> | coprocessor (see below)
```

#### Coprocessor Opcode/Parameter Encoding
```
  31..26 |25..21|20..16|15..11|10..6 |  5..0  |
   6bit  | 5bit | 5bit | 5bit | 5bit |  6bit  |
  -------+------+------+------+------+--------+------------
  0100nn |0|0000| rt   | rd   | N/A  | 000000 | MFCn rt,rd_dat  ;rt = dat
  0100nn |0|0010| rt   | rd   | N/A  | 000000 | CFCn rt,rd_cnt  ;rt = cnt
  0100nn |0|0100| rt   | rd   | N/A  | 000000 | MTCn rt,rd_dat  ;dat = rt
  0100nn |0|0110| rt   | rd   | N/A  | 000000 | CTCn rt,rd_cnt  ;cnt = rt
  0100nn |0|1000|00000 | <--immediate16bit--> | BCnF target ;jump if false
  0100nn |0|1000|00001 | <--immediate16bit--> | BCnT target ;jump if true
  0100nn |1| <--------immediate25bit--------> | COPn imm25
  010000 |1|0000| N/A  | N/A  | N/A  | 000001 | COP0 01h  ;=TLBR
  010000 |1|0000| N/A  | N/A  | N/A  | 000010 | COP0 02h  ;=TLBWI
  010000 |1|0000| N/A  | N/A  | N/A  | 000110 | COP0 06h  ;=TLBWR
  010000 |1|0000| N/A  | N/A  | N/A  | 001000 | COP0 08h  ;=TLBP
  010000 |1|0000| N/A  | N/A  | N/A  | 010000 | COP0 10h  ;=RFE
  1100nn | rs   | rt   | <--immediate16bit--> | LWCn rt_dat,[rs+imm]
  1110nn | rs   | rt   | <--immediate16bit--> | SWCn rt_dat,[rs+imm]
```

#### Illegal Opcodes
All opcodes that are marked as "N/A" in the Primary and Secondary opcode tables
are causing a Reserved Instruction Exception (excode=0Ah).<br/>
The unused operand bits (eg. Bit21-25 for LUI opcode) should be usually zero,
but do not necessarily trigger exceptions if set to nonzero values.<br/>



##   CPU Load/Store Opcodes
#### Load instructions
```
  movbs rt,[imm+rs]  lb  rt,imm(rs)    rt=[imm+rs]  ;byte sign-extended
  movb  rt,[imm+rs]  lbu rt,imm(rs)    rt=[imm+rs]  ;byte zero-extended
  movhs rt,[imm+rs]  lh  rt,imm(rs)    rt=[imm+rs]  ;halfword sign-extended
  movh  rt,[imm+rs]  lhu rt,imm(rs)    rt=[imm+rs]  ;halfword zero-extended
  mov   rt,[imm+rs]  lw  rt,imm(rs)    rt=[imm+rs]  ;word
```
Load instructions can read from the data cache (if the data is not in the
cache, or if the memory region is uncached, then the CPU gets halted until it
has read the data) (however, the PSX doesn't have a data cache).<br/>

#### Caution - Load Delay
The loaded data is NOT available to the next opcode, ie. the target register
isn't updated until the next opcode has completed. So, if the next opcode tries
to read from the load destination register, then it would (usually) receive the
OLD value of that register (unless an IRQ occurs between the load and next
opcode, in that case the load would complete during IRQ handling, and so, the
next opcode would receive the NEW value).<br/>

#### Store instructions
```
  movb  [imm+rs],rt  sb  rt,imm(rs)    [imm+rs]=(rt AND FFh)   ;store 8bit
  movh  [imm+rs],rt  sh  rt,imm(rs)    [imm+rs]=(rt AND FFFFh) ;store 16bit
  mov   [imm+rs],rt  sw  rt,imm(rs)    [imm+rs]=rt             ;store 32bit
```
Store operations are passed to the write-buffer, so they can execute within a
single clock cycle (unless the write-buffer was full, in that case the CPU gets
halted until there's room in the buffer). But, the PSX doesn't have a
writebuffer...?<br/>

#### Load/Store Alignment
Halfword addresses must be aligned by 2, word addresses must be aligned by 4,
trying to access mis-aligned addresses will cause an exception. There's no
alignment restriction for bytes.<br/>

#### Unaligned Load/Store
```
  lwr   rt,imm(rs)     load right bits of rt from memory (usually imm+0)
  lwl   rt,imm(rs)     load left  bits of rt from memory (usually imm+3)
  swr   rt,imm(rs)     store right bits of rt to memory (usually imm+0)
  swl   rt,imm(rs)     store left  bits of rt to memory (usually imm+3)
```
There's no delay required between lwl and lwr, so you can use them directly
following eachother, eg. to load a word anywhere in memory without regard to
alignment:<br/>
```
  lwl   r2,$0003(t0)   ;\no delay required between these
  lwr   r2,$0000(t0)   ;/(although both access r2)
  nop                  ;-requires load delay HERE (before reading from r2)
  and   r2,r2,0ffffh   ;-access r2 (eg. reducing it to unaligned 16bit data)
```

#### Unaligned Load/Store (Details)
LWR/SWR transfers the right (=lower) bits of Rt, up-to 32bit memory boundary:<br/>
```
  lwr/swr [N*4+0]     transfer whole 32bit of Rt to/from [N*4+0..3]
  lwr/swr [N*4+1]     transfer lower 24bit of Rt to/from [N*4+1..3]
  lwr/swr [N*4+2]     transfer lower 16bit of Rt to/from [N*4+2..3]
  lwr/swr [N*4+3]     transfer lower  8bit of Rt to/from [N*4+3]
```
LWL/SWL transfers the left (=upper) bits of Rt, down-to 32bit memory boundary:<br/>
```
  lwl/swl [N*4+0]     transfer upper  8bit of Rt to/from [N*4+0]
  lwl/swl [N*4+1]     transfer upper 16bit of Rt to/from [N*4+0..1]
  lwl/swl [N*4+2]     transfer upper 24bit of Rt to/from [N*4+0..2]
  lwl/swl [N*4+3]     transfer whole 32bit of Rt to/from [N*4+0..3]
```
The CPU has four separate byte-access signals, so, within a 32bit location, it
can transfer all fragments of Rt at once (including for odd 24bit amounts). The
transferred data is not zero- or sign-expanded, eg. when transferring 8bit
data, the other 24bit of Rt and [mem] will remain intact.<br/>

Note: The aligned variant can also misused for blocking memory access on
aligned addresses (in that case, if the address is known to be aligned, only
one of the opcodes are needed, either LWL or LWR).... Uhhhhhhhm, OR is that NOT
allowed... more PROBABLY that doesn't work?<br/>



##   CPU ALU Opcodes
#### arithmetic instructions
```
  addt rd,rs,rt    add   rd,rs,rt         rd=rs+rt (with overflow trap)
  add  rd,rs,rt    addu  rd,rs,rt         rd=rs+rt
  subt rd,rs,rt    sub   rd,rs,rt         rd=rs-rt (with overflow trap)
  sub  rd,rs,rt    subu  rd,rs,rt         rd=rs-rt
  addt rt,rs,imm   addi  rt,rs,imm        rt=rs+(-8000h..+7FFFh) (with ov.trap)
  add  rt,rs,imm   addiu rt,rs,imm        rt=rs+(-8000h..+7FFFh)
```
The opcodes "with overflow trap" do trigger an exception (and leave rd
unchanged) in case of overflows.<br/>

#### comparison instructions
```
  setlt slt   rd,rs,rt  if rs<rt then rd=1 else rd=0 (signed)
  setb  sltu  rd,rs,rt  if rs<rt then rd=1 else rd=0 (unsigned)
  setlt slti  rt,rs,imm if rs<(-8000h..+7FFFh)  then rt=1 else rt=0 (signed)
  setb  sltiu rt,rs,imm if rs<(FFFF8000h..7FFFh) then rt=1 else rt=0(unsigned)
```

#### logical instructions
```
  and  rd,rs,rt    and  rd,rs,rt         rd = rs AND rt
  or   rd,rs,rt    or   rd,rs,rt         rd = rs OR  rt
  xor  rd,rs,rt    xor  rd,rs,rt         rd = rs XOR rt
  nor  rd,rs,rt    nor  rd,rs,rt         rd = FFFFFFFFh XOR (rs OR rt)
  and  rt,rs,imm   andi rt,rs,imm        rt = rs AND (0000h..FFFFh)
  or   rt,rs,imm   ori  rt,rs,imm        rt = rs OR  (0000h..FFFFh)
  xor  rt,rs,imm   xori rt,rs,imm        rt = rs XOR (0000h..FFFFh)
```

#### shifting instructions
```
  shl  rd,rt,rs    sllv rd,rt,rs          rd = rt SHL (rs AND 1Fh)
  shr  rd,rt,rs    srlv rd,rt,rs          rd = rt SHR (rs AND 1Fh)
  sar  rd,rt,rs    srav rd,rt,rs          rd = rt SAR (rs AND 1Fh)
  shl  rd,rt,imm   sll  rd,rt,imm         rd = rt SHL (00h..1Fh)
  shr  rd,rt,imm   srl  rd,rt,imm         rd = rt SHR (00h..1Fh)
  sar  rd,rt,imm   sra  rd,rt,imm         rd = rt SAR (00h..1Fh)
  mov  rt,i*10000h lui  rt,imm            rt = (0000h..FFFFh) SHL 16
```
Unlike many other opcodes, shifts use 'rt' as second (not third) operand.<br/>
The hardware does NOT generate exceptions on SHL overflows.<br/>

#### Multiply/divide
```
  smul rs,rt       mult   rs,rt           hi:lo = rs*rt (signed)
  umul rs,rt       multu  rs,rt           hi:lo = rs*rt (unsigned)
  sdiv rs,rt       div    rs,rt           lo = rs/rt, hi=rs mod rt (signed)
  udiv rs,rt       divu   rs,rt           lo = rs/rt, hi=rs mod rt (unsigned)
  mov  rd,hi       mfhi   rd              rd=hi  ;move from hi
  mov  rd,lo       mflo   rd              rd=lo  ;move from lo
  mov  hi,rs       mthi   rs              hi=rs  ;move to hi
  mov  lo,rs       mtlo   rs              lo=rs  ;move to lo
```
The mul/div opcodes are starting the multiply/divide operation, starting takes
only a single clock cycle, however, trying to read the result from the hi/lo
registers while the mul/div operation is busy will halt the CPU until the
mul/div has completed. For multiply, the execution time depends on rs (ie.
"small\*large" can be much faster than "large\*small").<br/>
```
  __umul_execution_time_____________________________________________________
  Fast  (6 cycles)   rs = 00000000h..000007FFh
  Med   (9 cycles)   rs = 00000800h..000FFFFFh
  Slow  (13 cycles)  rs = 00100000h..FFFFFFFFh
  __smul_execution_time_____________________________________________________
  Fast  (6 cycles)   rs = 00000000h..000007FFh, or rs = FFFFF800h..FFFFFFFFh
  Med   (9 cycles)   rs = 00000800h..000FFFFFh, or rs = FFF00000h..FFFFF801h
  Slow  (13 cycles)  rs = 00100000h..7FFFFFFFh, or rs = 80000000h..FFF00001h
  __udiv/sdiv_execution_time________________________________________________
  Fixed (36 cycles)  no matter of rs and rt values
```
For example, when executing "umul 123h,12345678h" and "mov r1,lo", one can
insert up to six (cached) ALU opcodes, or read one value from PSX Main RAM
(which has 6 cycle access time) between the "umul" and "mov" opcodes without
additional slowdown.<br/>
The hardware does NOT generate exceptions on divide overflows, instead, divide
errors are returning the following values:<br/>
```
  Opcode  Rs              Rd       Hi/Remainder  Lo/Result
  udiv    0..FFFFFFFFh    0   -->  Rs            FFFFFFFFh
  sdiv    0..+7FFFFFFFh   0   -->  Rs            -1
  sdiv    -80000000h..-1  0   -->  Rs            +1
  sdiv    -80000000h      -1  -->  0             -80000000h
```
For udiv, the result is more or less correct (as close to infinite as
possible). For sdiv, the results are total garbage (about farthest away from
the desired result as possible).<br/>
Note: After accessing the lo/hi registers, there seems to be a strange rule
that one should not touch the lo/hi registers in the next 2 cycles or so... not
yet understood if/when/how that rule applies...?<br/>



##   CPU Jump Opcodes
#### jumps and branches
Note that the instruction following the branch will always be executed.<br/>
```
  jmp  dest        j      dest        pc=(pc and F0000000h)+(imm26bit*4)
  call dest        jal    dest        pc=(pc and F0000000h)+(imm26bit*4),ra=$+8
  jmp  rs          jr     rs          pc=rs
  call rs,ret=rd   jalr (rd,)rs(,rd)  pc=rs, rd=$+8 ;see caution
  je   rs,rt,dest  beq    rs,rt,dest  if rs=rt  then pc=$+4+(-8000h..+7FFFh)*4
  jne  rs,rt,dest  bne    rs,rt,dest  if rs<>rt then pc=$+4+(-8000h..+7FFFh)*4
  js   rs,dest     bltz   rs,dest     if rs<0   then pc=$+4+(-8000h..+7FFFh)*4
  jns  rs,dest     bgez   rs,dest     if rs>=0  then pc=$+4+(-8000h..+7FFFh)*4
  jgtz rs,dest     bgtz   rs,dest     if rs>0   then pc=$+4+(-8000h..+7FFFh)*4
  jlez rs,dest     blez   rs,dest     if rs<=0  then pc=$+4+(-8000h..+7FFFh)*4
  calls  rs,dest   bltzal rs,dest     if rs<0   then pc=$+4+(..)*4, ra=$+8
  callns rs,dest   bgezal rs,dest     if rs>=0  then pc=$+4+(..)*4, ra=$+8
```

#### JALR cautions
Caution: The JALR source code syntax varies (IDT79R3041 specs say "jalr rs,rd",
but MIPS32 specs say "jalr rd,rs"). Moreover, JALR may not use the same
register for both operands (eg. "jalr r31,r31") (doing so would destroy the
target address; which is normally no problem, but it can be a problem if an IRQ
occurs between the JALR opcode and the following branch delay opcode; in that
case BD gets set, and EPC points "back" to the JALR opcode, so JALR is executed
twice, with destroyed target address in second execution).<br/>

#### exception opcodes
Unlike for jump/branch opcodes, exception opcodes are immediately executed (ie.
without executing the following opcode).<br/>
```
  syscall  imm20        generates a system call exception
  break    imm20        generates a breakpoint exception
```
The 20bit immediate doesn't affect the CPU (however, the exception handler may
interprete it by software; by examing the opcode bits at [epc-4]).<br/>



##   CPU Coprocessor Opcodes
#### Coprocessor Instructions (COP0..COP3)
```
  mov  rt,cop#Rd(0-31)       mfc# rt,rd       ;rt = cop#datRd ;data regs
  mov  rt,cop#Rd(32-63)      cfc# rt,rd       ;rt = cop#cntRd ;control regs
  mov  cop#Rd(0-31),rt       mtc# rt,rd       ;cop#datRd = rt ;data regs
  mov  cop#Rd(32-63),rt      ctc# rt,rd       ;cop#cntRd = rt ;control regs
  mov  cop#cmd,imm25         cop# imm25       ;exec cop# command 0..1FFFFFFh
  mov  cop#Rt(0-31),[rs+imm] lwc# rt,imm(rs)  ;cop#dat_rt = [rs+imm]  ;word
  mov  [rs+imm],cop#Rt(0-31) swc# rt,imm(rs)  ;[rs+imm] = cop#dat_rt  ;word
  jf   cop#flg,dest          bc#f dest        ;if cop#flg=false then pc=$+disp
  jt   cop#flg,dest          bc#t dest        ;if cop#flg=true  then pc=$+disp
  rfe                        rfe              ;return from exception (COP0)
  tlb<xx>                    tlb<xx>          ;virtual memory related (COP0)
```
Unknown if any tlb-opcodes (tlbr,tlbwi,tlbwr,tlbp) are implemented in the psx?<br/>

#### Caution - Load Delay
When reading from a coprocessor register, the next opcode cannot use the
destination register as operand (much the same as the Load Delays that occur
when reading from memory; see there for details).<br/>
Reportedly, the Load Delay applies for the next TWO opcodes after coprocessor
reads, but, that seems to be nonsense (the PSX does finish both COP0 and COP2
reads after ONE opcode).<br/>

#### Caution - Store Delay
In some cases, a similar delay occurs when writing to a coprocessor register.
COP0 is more or less free of store delays (eg. one can read from a cop0
register immediately after writing to it), the only known exception is the cop2
enable bit in cop0r12.bit30 (setting that cop0 bit acts delayed, and cop2 isn't
actually enabled until after 2 clock cycles or so).<br/>
Writing to cop2 registers has a delay of 2..3 clock cycles. In most cases, that
is probably (?) only 2 cycles, but special cases like writing to IRGB (which
does additionally affect IR1,IR2,IR3) take 3 cycles until the result arrives in
all registers).<br/>
Note that Store Delays are counted in numbers of clock cycles (not in numbers
of opcodes). For 3 cycle delay, one must usually insert 3 cached opcodes (or
one uncached opcode).<br/>



##   CPU Pseudo Opcodes
#### Pseudo instructions (native/spasm)
```
  nop                  ;alias for sll r0,r0,0
  move rd,rs           ;alias for addu rd,rs,r0
  la   rx,imm32        ;load address   (alias for lui rx / addiu rx)
  li   rx,imm32        ;load immediate (alias for lui rx / ori   rx)
  li   rx,imm16        ;load immediate (alias for ori, range 0..FFFFh)
  li   rx,-imm15       ;load immediate (alias for addiu, range -1..-8000h)
  li   rx,imm16*10000h ;load immediate (alias for lui)
  lw   rx,imm32        ;load from address (lui rx / lw rx,rx)
  sw   rx,imm32        ;store to address  (lui r1 / sw rx,r1) (destroys r1!)
  lb,lh,lwl,lwr,lbu,lhu;as above pseudo lw
  sb,sh,swl,swr        ;as above pseudo sw (ie. also destroys r1!)
  alu  rx,op           ;alias for alu  rx,rx,op
  alu(u) rx,rx,imm     ;alias for alui(u) rx,rx,imm
  jalr  rx             ;alias for jalr (RA,)rx(,RA)
  subi(u) rt,rs,imm    ;alias for addi(u) rt,rs,-imm
  beqz rx,dest         ;alias for beq rx,r0,dest
  bnez rx,dest         ;alias for bne rx,r0,dest
  b   dest             ;alias for beq r0,r0,dest (jump relative/spasm)
  bra dest             ;alias for ...? (jump relative/gnu)
  bal dest             ;alias for ...? (call relative/spasm)
```

#### Pseudo instructions (nocash/a22i)
```
  mov  rx,NNNN0000h    ;alias for lui  rx,NNNNh
  mov  rx,0000NNNNh    ;alias for or   rx,r0,NNNNh  ;max +FFFFh
  mov  rx,-imm15       ;alias for add  rx,r0,-NNNNh ;min -8000h
  mov  rx,ry           ;alias for or   rx,ry,0  (or "addiu")
  nop                  ;alias for shl  r0,r0,0
  jrel dest            ;alias for blez R0,dest   ;relative jump
  crel dest            ;alias for callns R0,dest ;relative call
  jz   rx,dest         ;alias for je   rx,R0,dest
  jnz  rx,dest         ;alias for jne  rx,R0,dest
  call rx              ;alias for call rx,ret=RA
  ret                  ;alias for jmp  ra
  subt rt,rs,imm       ;alias for addt rt,rs,-imm
  sub  rt,rs,imm       ;alias for add  rt,rs,-imm
  alu  rx,op           ;alias for alu  rx,rx,op
  neg(t) rx,ry         ;alias for sub(t) rx,R0,ry
  not    rx,ry         ;alias for nor    rx,R0,ry
  neg(t)/not rx        ;alias for neg(t)/not rx,rx
  setz rx,ry           ;alias for setb rx,ry,1   (set if zero)
  setnz rx,ry          ;alias for setb rx,R0,ry  (set if nonzero)
  syscall/break        ;alias for syscall/break 000000h
```
Below are pseudo instructions combined of two 32bit opcodes...<br/>
```
  movp rx,imm32        ;alias for lui  rx,imm16 -plus- or rx,rx,imm16)
  mov(bhs)p rx,[imm32] ;load from address (lui rx,imm16 / mov rx,[rx+imm16])
  movu [rs+imm]        ;alias for lwr/swr [rs+imm] plus lwl/swl [rs+imm+3]
  reti                 ;alias for jmp k0 plus rfe
```
Below are pseudo instructions combined of two or more 32bit opcodes...<br/>
```
  push rlist           ;alias for sub sp,n*4 -- mov [sp+(1..n)*4],r1..rn
  pop  rlist           ;alias for mov r1..rn,[sp+(1..n)*4] -- add sp,n*4
  pop  pc,rlist        ;alias for pop ra,rlist -- jmp ra
```

#### Possible more Pseudos...
```
  call x0000000h ;call y0000000h (could be half-working for mem mirrors?)
  setae,setge    ;--> setb,setlt with swapped operands
```

#### Directives (nocash)
```
  .mips          ;select MIPS instruction set (alternately .hc05 for MC68HC05)
  .bios          ;create a .ROM file (instead of .EXE)
  .auto_nop      ;append NOPs to jumps ;unless next opcode starts with a +
  org imm        ;assume following code to be originated at address "imm"
  db n(,n(..)))  ;define 8bit data values(s) or quoted ASCII strings
  dw n(,n(..)))  ;define 16bit data values(s) (not 32bit data!)
  dd n(,n(..)))  ;define 32bit data values(s)
  .align imm
  0              ;alias for immediate 0 and register R0 (whichever fits)
```

#### Directives (native)
```
  org imm        ;self-explaining (but, default=$80010000 for spasm!)
  align imm      ;self-explaining (probably zeropadded?)
  db n(,n(..)))  ;define 8bit data values(s) or quoted ASCII strings
  dh n(,n(..)))  ;define 16bit data values(s)
  dw n(,n(..)))  ;define 32bit data values(s) (not 16bit data!)
  dcb len,value  ;fill <len> bytes by <value> (different as DCB on ARM CPUs)
  xyz            ;define label "xyz" at current address (without colon)
  xyz equ n      ;assign value n to xyz
  xyz = n        ;probably same/sililar as "equ"
  ;xyz           ;comments invoked with semicolon (spasm)
  incbin file.bin       ;import binary file
  include file.asm      ;import asm file
  zero           ;alias for r0
  >imm32         ;alias for (i-(i AND 8000h))/10000h,  and/or i/10000h ?
  <imm32         ;alias for (i AND 0FFFFh), used for SW(+/-) and ORI(+)?
  end       ;N/A ;no "end" or ".end" directive needed/used by spasm
  r1 aka at ;N/A ;some assemblers may (optionally) reject to use r1/at
```

#### Syntax for unknown assembler (for pad.s)
It uses "0x" for HEX values (but doesn't use "$" for registers).<br/>
It uses "#" instead of ";" for comments.<br/>
It uses ":" for labels (fortunately).<br/>
The assembler has at least one directive: ".byte" (equivalent to "db" on other
assemblers).<br/>
I've no clue which assembler is used for that syntax... could that be the Psy-Q
assembler?<br/>



##   COP0 - Register Summary
#### COP0 Register Summary
```
  cop0r0-r2   - N/A
  cop0r3      - BPC - Breakpoint on execute (R/W)
  cop0r4      - N/A
  cop0r5      - BDA - Breakpoint on data access (R/W)
  cop0r6      - JUMPDEST - Randomly memorized jump address (R)
  cop0r7      - DCIC - Breakpoint control (R/W)
  cop0r8      - BadVaddr - Bad Virtual Address (R)
  cop0r9      - BDAM - Data Access breakpoint mask (R/W)
  cop0r10     - N/A
  cop0r11     - BPCM - Execute breakpoint mask (R/W)
  cop0r12     - SR - System status register (R/W)
  cop0r13     - CAUSE - (R)  Describes the most recently recognised exception
  cop0r14     - EPC - Return Address from Trap (R)
  cop0r15     - PRID - Processor ID (R)
  cop0r16-r31 - Garbage
  cop0r32-r63 - N/A - None such (Control regs)
```



##   COP0 - Exception Handling
#### cop0r13 - CAUSE - (Read-only, except, Bit8-9 are R/W)
Describes the most recently recognised exception<br/>
```
  0-1   -      Not used (zero)
  2-6   Excode Describes what kind of exception occured:
                 00h INT     Interrupt
                 01h MOD     Tlb modification (none such in PSX)
                 02h TLBL    Tlb load         (none such in PSX)
                 03h TLBS    Tlb store        (none such in PSX)
                 04h AdEL    Address error, Data load or Instruction fetch
                 05h AdES    Address error, Data store
                             The address errors occur when attempting to read
                             outside of KUseg in user mode and when the address
                             is misaligned. (See also: BadVaddr register)
                 06h IBE     Bus error on Instruction fetch
                 07h DBE     Bus error on Data load/store
                 08h Syscall Generated unconditionally by syscall instruction
                 09h BP      Breakpoint - break instruction
                 0Ah RI      Reserved instruction
                 0Bh CpU     Coprocessor unusable
                 0Ch Ov      Arithmetic overflow
                 0Dh-1Fh     Not used
  7     -      Not used (zero)
  8-15  Ip     Interrupt pending field. Bit 8 and 9 are R/W, and
               contain the last value written to them. As long
               as any of the bits are set they will cause an
               interrupt if the corresponding bit is set in IM.
  16-27 -      Not used (zero)
  28-29 CE     Contains the coprocessor number if the exception
               occurred because of a coprocessor instuction for
               a coprocessor which wasn't enabled in SR.
  30    -      Not used (zero)
  31    BD     Is set when last exception points to the
               branch instuction instead of the instruction
               in the branch delay slot, where the exception
               occurred.
```

#### cop0r12 - SR - System status register (R/W)
```
  0     IEc Current Interrupt Enable  (0=Disable, 1=Enable) ;rfe pops IUp here
  1     KUc Current Kernal/User Mode  (0=Kernel, 1=User)    ;rfe pops KUp here
  2     IEp Previous Interrupt Disable                      ;rfe pops IUo here
  3     KUp Previous Kernal/User Mode                       ;rfe pops KUo here
  4     IEo Old Interrupt Disable                       ;left unchanged by rfe
  5     KUo Old Kernal/User Mode                        ;left unchanged by rfe
  6-7   -   Not used (zero)
  8-15  Im  8 bit interrupt mask fields. When set the corresponding
            interrupts are allowed to cause an exception.
  16    Isc Isolate Cache (0=No, 1=Isolate)
              When isolated, all load and store operations are targetted
              to the Data cache, and never the main memory.
              (Used by PSX Kernel, in combination with Port FFFE0130h)
  17    Swc Swapped cache mode (0=Normal, 1=Swapped)
              Instruction cache will act as Data cache and vice versa.
              Use only with Isc to access & invalidate Instr. cache entries.
              (Not used by PSX Kernel)
  18    PZ  When set cache parity bits are written as 0.
  19    CM  Shows the result of the last load operation with the D-cache
            isolated. It gets set if the cache really contained data
            for the addressed memory location.
  20    PE  Cache parity error (Does not cause exception)
  21    TS  TLB shutdown. Gets set if a programm address simultaneously
            matches 2 TLB entries.
            (initial value on reset allows to detect extended CPU version?)
  22    BEV Boot exception vectors in RAM/ROM (0=RAM/KSEG0, 1=ROM/KSEG1)
  23-24 -   Not used (zero)
  25    RE  Reverse endianness   (0=Normal endianness, 1=Reverse endianness)
              Reverses the byte order in which data is stored in
              memory. (lo-hi -> hi-lo)
              (Has affect only to User mode, not to Kernel mode) (?)
              (The bit doesn't exist in PSX ?)
  26-27 -   Not used (zero)
  28    CU0 COP0 Enable (0=Enable only in Kernal Mode, 1=Kernal and User Mode)
  29    CU1 COP1 Enable (0=Disable, 1=Enable) (none such in PSX)
  30    CU2 COP2 Enable (0=Disable, 1=Enable) (GTE in PSX)
  31    CU3 COP3 Enable (0=Disable, 1=Enable) (none such in PSX)
```

#### cop0r14 - EPC - Return Address from Trap (R)
```
  0-31  Return Address from Exception
```
This address is the instruction at which the exception took place, unless BD is
set in CAUSE, then the instruction was at EPC+4.<br/>
Interrupts should always return to EPC+0, no matter of the BD flag. That way,
if BD=1, the branch gets executed again, that's required because EPC stores
only the current program counter, but not additionally the branch destination
address.<br/>
Other exceptions may require to handle BD. In simple cases, when BD=0, the
exception handler may return to EPC+0 (retry execution of the opcode), or to
EPC+4 (skip the opcode that caused the exception). Note that jumps to faulty
memory locations are executed without exception, but will trigger address
errors and bus errors at the target location, ie. EPC (and BadVAddr, in case of
address errors) point to the faulty address, not to the opcode that has jumped
to that address).<br/>

#### Interrupts vs GTE Commands
If an interrupt occurs "on" a GTE command (cop2cmd), then the GTE command is
executed, but nethertheless, the return address in EPC points to the GTE
command. So, if the exeception handler would return to EPC as usually, then the
GTE command would be executed twice. In best case, this would be a waste of
clock cycles, in worst case it may lead to faulty result (if the results from
the 1st execution are re-used as incoming parameters in the 2nd execution). To
fix the problem, the exception handler must do:<br/>
```
  if (cause AND 7Ch)=00h                ;if excode=interrupt
   if ([epc] AND FE000000h)=4A000000h   ;and opcode=cop2cmd
    epc=epc+4                           ;then skip that opcode
```
Note: The above exception handling is working only in newer PSX BIOSes, but in
very old PSX BIOSes, it is only incompletely implemented (see "BIOS Patches"
chapter for common workarounds; or write your own exception handler without
using the BIOS).<br/>
Of course, the above exeption handling won't work in branch delays (where BD
gets set to indicate that EPC was modified) (best workaround is not to use GTE
commands in branch delays).<br/>

#### cop0cmd=10h - RFE opcode - Prepare Return from Exception
The RFE opcode moves some bits in cop0r12 (SR): bit2-3 are copied to bit0-1,
and bit4-5 are copied to bit2-3, all other bits (including bit4-5) are left
unchanged.<br/>
The RFE opcode does NOT automatically jump to EPC. Instead, the exception
handler must copy EPC into a register (usually R26 aka K0), and then jump to
that address. Because of branch delays, that would look like so:<br/>
```
  mov  k0,epc  ;get return address
  push k0      ;save epc in memory (if you expect nested exceptions)
  ...          ;whatever (ie. process CAUSE)
  pop  k0      ;restore from memory (if you expect nested exceptions)
  jmp  k0      ;jump to K0 (after executing the next opcode)
  +rfe         ;move SR bit4/5 --> bit2/3 --> bit0/1
```
If you expect exceptions to be nested deeply, also push/pop SR. Note that
there's no way to leave all registers intact (ie. above code destroys K0).<br/>

#### cop0r8 - BadVaddr - Bad Virtual Address (R)
Contains the address whose reference caused an exception. Set on any MMU type
of exceptions, on references outside of kuseg (in User mode) and on any
misaligned reference. BadVaddr is updated ONLY by Address errors (Excode 04h
and 05h), all other exceptions (including bus errors) leave BadVaddr unchanged.<br/>

#### Exception Vectors (depending on BEV bit in SR register)
```
  Exception     BEV=0         BEV=1
  Reset         BFC00000h     BFC00000h   (Reset)
  UTLB Miss     80000000h     BFC00100h   (Virtual memory, none such in PSX)
  COP0 Break    80000040h     BFC00140h   (Debug Break)
  General       80000080h     BFC00180h   (General Interrupts & Exceptions)
```
Note: Changing vectors at 800000xxh (kseg0) seems to be automatically reflected
to the instruction cache without needing to flush cache (at least it worked
SOMETIMES in my test proggy... but NOT always? ...anyways, it'd be highly
recommended to flush cache when changing any opcodes), whilst changing mirrors
at 000000xxh (kuseg) seems to require to flush cache.<br/>
The PSX uses only the BEV=0 vectors (aside from the reset vector, the PSX BIOS
ROM doesn't contain any of the BEV=1 vectors).<br/>

#### Exception Priority
```
  Reset At any time (highest)            ;-reset
  AdEL Memory (Load instruction)         ;\
  AdES Memory (Store instruction)        ; memory (data load/store)
  DBE  Memory (Load or store)            ;/
  MOD  ALU (Data TLB)                    ;\
  TLBL ALU (DTLB Miss)                   ; none such
  TLBS ALU (DTLB Miss)                   ;/
  Ovf  ALU                               ;-overflow
  Int  ALU                               ;-interrupt
  Sys  RD (Instruction Decode)           ;\
  Bp   RD (Instruction Decode)           ;
  RI   RD (Instruction Decode)           ;
  CpU  RD (Instruction Decode)           ;/
  TLBL I-Fetch (ITLB Miss)               ;-none such
  AdEL IVA (Instruction Virtual Address) ;\memory (opcode fetch)
  IBE  RD (end of I-Fetch, lowest)       ;/
```



##   COP0 - Misc
#### cop0r15 - PRID - Processor ID (R)
```
  0-7   Revision
  8-15  Implementation
  16-31 Not used
```
For a Playstation with CXD8606CQ CPU, the PRID value is 00000002h.<br/>
Unknown if/which other Playstation CPU versions have other values...?<br/>

#### cop0r6 - JUMPDEST - Randomly memorized jump address (R)
The is a rather strange totally useless register. After certain exceptions, the
CPU does memorize a jump destination address in the register. Once when it has
memorized an address, the register becomes locked, and the memorized value
won't change until it becomes unlocked by a new exception. Exceptions that do
unlock the register are Reset and Interrupts (cause.bit10). Exceptions that do
NOT unlock the register are syscall/break opcodes, and software generated
interrupts (eg. cause.bit8).<br/>
In the unlocked state, the CPU does more or less randomly memorize one of the
next some jump destinations - eg. the destination from the second jump after
reset, or from a jump that occured immediately before executing the IRQ
handler, or from a jump inside of the IRQ handler, or even from a later jump
that occurs shortly after returning from the IRQ handler.<br/>
The register seems to be read-only (although the Kernel initialization code
writes 0 to it for whatever reason).<br/>

#### cop0r0..r2, cop0r4, cop0r10, cop0r32..r63 - N/A
Registers 0,1,2,4,10 control virtual memory on some MIPS processors (but
there's none such in the PSX), and Registers 32..63 (aka "control registers")
aren't used in any MIPS processors. Trying to read any of these registers
causes a Reserved Instruction Exception (excode=0Ah).<br/>

#### cop0cmd=01h,02h,06h,08h - TLBR,TLBWI,TLBWR,TLBP
The PSX supports only one cop0cmd (cop0cmd=10h aka RFE). Trying to execute the
TLBxx opcodes causes a Reserved Instruction Exception (excode=0Ah).<br/>

#### jf/jt cop0flg,dest - conditional cop0 jumps
#### mov [mem],cop0reg / mov cop0reg,[mem] - coprocessor cop0 load/store
Not supported by the CPU. Trying to execute these opcodes causes a Coprocessor
Unusable Exception (excode=0Bh, ie. unlike above, not 0Ah).<br/>

#### cop0r16-r31 - Garbage
Trying to read these registers returns garbage (but does not trigger an
exception). When reading one of the garbage registers shortly after reading a
valid cop0 register, the garbage value is usually the same as that of the valid
register. When doing the read later on, the return value is usually 00000020h,
or when reading much later it returns 00000040h, or even 00000100h. No idea
what is causing that effect...?<br/>
Note: The garbage registers can be accessed (without causing an exception) even
in "User mode with cop0 disabled" (SR.Bit1=1 and SR.Bit28=0); accessing any
other existing cop0 registers (or executing the rfe opcode) in that state is
causing Coprocessor Unusable Exceptions (excode=0Bh).<br/>



##   COP0 - Debug Registers
The COP0 debug registers seem to be PSX specific, normal R30xx CPUs like IDT's
R3041 and R3051 don't have anything similar.<br/>

#### cop0r7 - DCIC - Breakpoint control (R/W)
```
  0      Automatically set by hardware upon Any break            (R/W)
  1      Automatically set by hardware upon BPC Code break       (R/W)
  2      Automatically set by hardware upon BDA Data break       (R/W)
  3      Automatically set by hardware upon BDA Data-Read break  (R/W)
  4      Automatically set by hardware upon BDA Data-Write break (R/W)
  5      Automatically set by hardware upon any-jump break       (R/W)
  6-11   Not used (always zero)
  12-13  Jump Redirection (0=Disable, 1..3=Enable) (see note)    (R/W)
  14-15  Unknown? (R/W)
  16-22  Not used (always zero)
  23     Super-Master Enable 1 for bit24-29
  24     Execution breakpoint     (0=Disabled, 1=Enabled) (see BPC, BPCM)
  25     Data access breakpoint   (0=Disabled, 1=Enabled) (see BDA, BDAM)
  26     Break on Data-Read       (0=No, 1=Break/when Bit25=1)
  27     Break on Data-Write      (0=No, 1=Break/when Bit25=1)
  28     Break on any-jump        (0=No, 1=Break on branch/jump/call/etc.)
  29     Master Enable for bit28 (..and/or exec-break at address>=80000000h?)
  30     Master Enable for bit24-27
  31     Super-Master Enable 2 for bit24-29
```
When a breakpoint address match occurs the PSX jumps to 80000040h (ie. unlike
normal exceptions, not to 80000080h). The Excode value in the CAUSE register is
set to 09h (same as BREAK opcode), and EPC contains the return address, as
usually. One of the first things to be done in the exception handler is to
disable breakpoints (eg. if the any-jump break is enabled, then it must be
disabled BEFORE jumping from 80000040h to the actual exception handler).<br/>

#### cop0r7.bit12-13 - Jump Redirection Note
If one or both of these bits are nonzero, then the PSX seems to check for the
following opcode sequence,<br/>
```
  mov rx,[mem]   ;load rx from memory
  ...            ;one or more opcodes that do not change rx
  jmp/call rx    ;jump or call to rx
```
if it does sense that sequence, then it sets PC=[00000000h], but does not store
any useful information in any cop0 registers, namely it does not store the
return address in EPC, so it's impossible to determine which opcode has caused
the exception. For the jump target address, there are 31 registers, so one
could only guess which of them contains the target value; for "POP PC" code
it'd be usually R31, but for "JMP [vector]" code it may be any register. So far
the feature seems to be more or less unusable...?<br/>

#### cop0r5 - BDA - Breakpoint on Data Access Address (R/W)
#### cop0r9 - BDAM - Breakpoint on Data Access Mask (R/W)
Break condition is "((addr XOR BDA) AND BDAM)=0".<br/>

#### cop0r3 - BPC - Breakpoint on Execute Address (R/W)
#### cop0r11 - BPCM - Breakpoint on Execute Mask (R/W)
Break condition is "((PC XOR BPC) AND BPCM)=0".<br/>

#### Note (BREAK Opcode)
Additionally, the BREAK opcode can be used to create further breakpoints by
patching the executable code. The BREAK opcode uses the same Excode value (09h)
in CAUSE register. However, the BREAK opcode jumps to the normal exception
handler at 80000080h (not 80000040h).<br/>

#### Note (LibCrypt)
The debug registers are mis-used by "Legacy of Kain: Soul Reaver" (and maybe
also other games) for storing libcrypt copy-protection related values (ie. just
as a "hidden" location for storing data, not for actual debugging purposes).<br/>
[CDROM Protection - LibCrypt](cdromdrive.md#cdrom-protection-libcrypt)<br/>

#### Note (Cheat Devices/Expansion ROMs)
The Expansion ROM header supports only Pre-Boot and Post-Boot vectors, but no
Mid-Boot vector. Cheat Devices are often using COP0 breaks for Mid-Boot Hooks,
either with BPC=BFC06xxxh (break address in ROM, used in older cheat
firmwares), or with BPC=80030000h (break address in RAM aka relocated GUI
entrypoint, used in later cheat firmwares). Moreover, aside from the Mid-Boot
Hook, the Xplorer cheat device is also supporting a special cheat code that
uses the COP0 break feature.<br/>

#### Note (Datasheet)
Note: COP0 debug registers are described in LSI's "L64360" datasheet, chapter
14. And in their LR33300/LR33310 datasheet, chapter 4.<br/>
