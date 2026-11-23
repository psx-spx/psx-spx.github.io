#   Patches
The original PSX Kernel mainly consists of messy and unstable compiler
generated code, and, to the worst, the \<same\> author seems to have
attempted to use assembler code in some places. In result, most commercial
games are causing a greater mess by inserting patches in the kernel code...<br/>
Which has been a nasty surprise when making the nocash PSX bios; which
obviously wasn't compatible with these patches. The only solutions would have
been to insert hundreds of NOPs to make my bios \<exactly\> as bloated as
the original bios (which I really didn't want to do), or to create
anti-patch-patches.<br/>

#### Patches and Anti-Patch-Patches
As shown below, all known patches are invoked by a B(56h) or B(57h) function
call. In the nocash PSX bios, these two functions are examining the following
opcodes, if the opcodes are a known patch, then the BIOS reproduces the desired
behaviour, and does then continue normal execution after those opcodes. If the
opcodes are unknown, then the BIOS simply locks up; and shows an error message
with the address of that opcodes in the TTY window; info about any such unknown
opcodes would be welcome!<br/>

#### Compatibility
If you want to (or need to) use patches, please use byte-identical opcodes as
commercial games do (as shown below; only the "xxxx" address digits are don't
care), so the nocash PSX bios (or other homebrewn BIOSes) can detect and
reproduce them. Or alternately, don't use the BIOS, and access I/O ports
directly, which is much better and faster anyways.<br/>
The listings below are in GNU as syntax, with each opcode word on the left. An
instruction in a branch delay slot is indented by one extra space.<br/>

#### patch\_missing\_cop0r13\_in\_exception\_handler:
In newer Kernel version, the exception handler reads cop0r13/cause to $v0,
examines the Excode value in $v0, and if the exception was caused by an
interrupt, and if the next opcode (at EPC) is a GTE/COP2 command, then it does
increment EPC by 4. The GTE commands are executed even if an interrupt occurs
simultaneously, so, without adjusting EPC, the command would be executed twice.
With some commands that'd just waste some clock cycles, with other commands it
may cause data to be written twice to the GTE FIFOs, or may re-use the result
from the 1st command execution as input to the 2nd execution.<br/>
The old "CEX-1000 KT-3" Kernel version did examine $v0, but it "forgot" to
previously load cop0r13 to $v0, so it did randomly examine a garbage value. The
patch inserts the missing opcode, used in elo2 at 80033740h, and in Pandemonium
II at 8007F3FCh:<br/>
```
  240A00B0 li $t2, 0xb0                                       ;\   00000000 nop
  0140F809 jalr $t2                                           ;    00000000 nop
  24090056  li $t1, 0x56                                      ;/   241A0100 li $k0, 0x100
  3C0Axxxx lui $t2, %hi(new_data)                             ;\   8F5A0008 lw $k0, 0x8($k0)
  3C09xxxx lui $t1, %hi(new_data_end)                         ;    00000000 nop
  8C420018 lw $v0, 0x18($v0) ;=C(06h)                         ;    8F5A0000 lw $k0, 0x0($k0)
  254Axxxx addiu $t2, $t2, %lo(new_data) ;=new_data           ;    00000000 nop
  2529xxxx addiu $t1, $t1, %lo(new_data_end)  ;=new_data_end  ;/   235A0008 addi $k0, $k0, 0x8
          copy_lop:                                           ;\   AF410004 sw $at, 0x4($k0)
  8D430000 lw $v1, 0x0($t2)                                   ;    AF420008 sw $v0, 0x8($k0)
  254A0004 addiu $t2, $t2, 0x4                                ;    AF43000C sw $v1, 0xc($k0)
  24420004 addiu $v0, $v0, 0x4                                ;    AF5F007C sw $ra, 0x7c($k0)
  1549FFFC bne $t2, $t1, copy_lop                             ;    40026800 mfc0 $v0, $13
  AC43FFFC  sw $v1, -0x4($v0)                                 ;/   00000000 nop
```
Alternately, same as above, but using $k0/$k1 instead of $t2/$t1, used in Ridge
Racer at 80047B14h:<br/>
```
  240A00B0 li $t2, 0xb0                                           ;\     00000000 nop
  0140F809 jalr $t2                                               ;      00000000 nop
  24090056  li $t1, 0x56                                          ;/     241A0100 li $k0, 0x100
  3C1Axxxx lui $k0, %hi(new_data)                                 ;\     8F5A0008 lw $k0, 0x8($k0)
  3C1Bxxxx lui $k1, %hi(new_data_end)                             ;      00000000 nop
  8C420018 lw $v0, 0x18($v0) ;=C(06h)                             ;      8F5A0000 lw $k0, 0x0($k0)
  275Axxxx addiu $k0, $k0, %lo(new_data)      ;=new_data          ;      00000000 nop
  277Bxxxx addiu $k1, $k1, %lo(new_data_end)  ;=new_data_end      ;/     235A0008 addi $k0, $k0, 0x8
          copy_lop:                                               ;\     AF410004 sw $at, 0x4($k0)
  8F430000 lw $v1, 0x0($k0)                                       ;      AF420008 sw $v0, 0x8($k0)
  275A0004 addiu $k0, $k0, 0x4                                    ;      AF43000C sw $v1, 0xc($k0)
  24420004 addiu $v0, $v0, 0x4                                    ;      AF5F007C sw $ra, 0x7c($k0)
  175BFFFC bne $k0, $k1, copy_lop                                 ;      40026800 mfc0 $v0, $13
  AC43FFFC  sw $v1, -0x4($v0)                                     ;/     00000000 nop
```
Alternately, slightly different code used in metal\_gear\_solid at 80095CC0h, and
in alone1 at 800A3ECCh:<br/>
```
  24090056 li $t1, 0x56                                           ;\
  240A00B0 li $t2, 0xb0                                           ; B(56h) GetC0Table
  0140F809 jalr $t2                                               ;
  00000000  nop                                                   ;/
  8C420018 lw $v0, 0x18($v0) ;=00000C80h = exception_handler = C(06h)
  00000000 nop
  24420028 addiu $v0, $v0, 0x28
  00407821 addu $t7, $v0, $zero
  3C0Axxxx lui $t2, %hi(ori_data)             ;\ori_data          ;\
  254Axxxx addiu $t2, $t2, %lo(ori_data)      ;/                  ;
  3C09xxxx lui $t1, %hi(ori_data_end)         ;\ori_data_end      ; ori_data:
  2529xxxx addiu $t1, $t1, %lo(ori_data_end)  ;/                  ;  AF410004 sw $at, 0x4($k0)
          verify_lop:                                             ;  AF420008 sw $v0, 0x8($k0)
  8D430000 lw $v1, 0x0($t2)                                       ;  AF43000C sw $v1, 0xc($k0)
  8C4B0000 lw $t3, 0x0($v0)                                       ;  AF5F007C sw $ra, 0x7c($k0)
  254A0004 addiu $t2, $t2, 0x4                                    ;  40037000 mfc0 $v1, $14
  146B000E bne $v1, $t3, verify_mismatch                          ;  00000000 nop
  24420004  addiu $v0, $v0, 0x4                                   ;
  1549FFFA bne $t2, $t1, verify_lop                               ;
  00000000  nop                                                   ;/
  01E01021 addu $v0, $t7, $zero
  3C0Axxxx lui $t2, %hi(new_data)             ;\new_data          ;\
  254Axxxx addiu $t2, $t2, %lo(new_data)      ;/                  ;
  3C09xxxx lui $t1, %hi(new_data_end)         ;\new_data_end      ; new_data:
  2529xxxx addiu $t1, $t1, %lo(new_data_end)  ;/                  ;  AF410004 sw $at, 0x4($k0)
          copy_lop:                                               ;  AF420008 sw $v0, 0x8($k0)
  8D430000 lw $v1, 0x0($t2)                                       ;  40026800 mfc0 $v0, $13
  00000000 nop                                                    ;  AF43000C sw $v1, 0xc($k0)
  AC430000 sw $v1, 0x0($v0)                                       ;  40037000 mfc0 $v1, $14
  254A0004 addiu $t2, $t2, 0x4                                    ;  AF5F007C sw $ra, 0x7c($k0)
  1549FFFB bne $t2, $t1, copy_lop                                 ;
  24420004  addiu $v0, $v0, 0x4                                   ;/
          verify_mismatch:
```
Alternately, a bugged/nonfunctional homebrew variant (used by Hitmen's
"minimum" demo):<br/>
```
  ;BUG1: 8bit "lbu $a2" should be 32bit "lw $a2"
  ;BUG2: copy_lop should transfer 6 words (not 7 words)
  ;BUG3: and, asides, the minimum demo works only with PAL BIOS (not NTSC)
  0xxxxxxx jal 0xXXXXXXXX                           ;\B(56h) GetC0Table
  00000000  nop                                     ;/(li $t0,0xb0; jr $t0; li $t1,0x56)
  3C04xxxx lui $a0, %hi(ori_data)         ;\ori_data
  2484xxxx addiu $a0, $a0, %lo(ori_data)  ;/
  90460018 lbu $a2, 0x18($v0)             ;BUG1 ;exception_handler = C(06h)
  24870018 addiu $a3, $a0, 0x18 ;ori_end             ;\
  24C50028 addiu $a1, $a2, 0x28 ;C(06h)+28h          ;
  00A03021 addu $a2, $a1, $zero                      ;                   ori_data:
          verify_lop:                                ;  80086520 AF410004 sw $at, 0x4($k0)
  8CA30000 lw $v1, 0x0($a1)                          ;  80086524 AF420008 sw $v0, 0x8($k0)
  8C820000 lw $v0, 0x0($a0)                          ;  80086528 AF43000C sw $v1, 0xc($k0)
  00000000 nop                                       ;  8008652C AF5F007C sw $ra, 0x7c($k0)
  1462000C bne $v1, $v0, verify_mismatch             ;  80086530 40037000 mfc0 $v1, $14
  24840004  addiu $a0, $a0, 0x4                      ;  80086534 00000000 nop
  1487FFFA bne $a0, $a3, verify_lop                  ;                   ori_end:
  24A50004  addiu $a1, $a1, 0x4                      ;/
  00C02821 addu $a1, $a2, $zero                      ;\                  new_data:
  3C04xxxx lui $a0, %hi(new_data) ;\new_data         ;  80086538 AF410004 sw $at, 0x4($k0)
  2484xxxx addiu $a0, $a0, %lo(new_data)     ;/      ;  8008653C AF420008 sw $v0, 0x8($k0)
  2483001C addiu $v1, $a0, 0x1c ;bugged_end          ;  80086540 40026800 mfc0 $v0, $13
          copy_lop:                                  ;  80086544 AF43000C sw $v1, 0xc($k0)
  8C820000 lw $v0, 0x0($a0)                          ;  80086548 40037000 mfc0 $v1, $14
  24840004 addiu $a0, $a0, 0x4                       ;  8008654C AF5F007C sw $ra, 0x7c($k0)
  ACA20000 sw $v0, 0x0($a1)                          ;                   new_end:
  1483FFFC bne $a0, $v1, copy_lop                    ;  80086550 00000000 nop  ;BUG2
  24A50004  addiu $a1, $a1, 0x4                      ;/                  bugged_end:
          verify_mismatch:
```

#### early\_card\_irq\_patch:
Because of a hardware glitch the card IRQ cannot be acknowledged while the
external IRQ signal is still LOW, making it neccessary to insert a delay that
waits until the signal gets HIGH before acknowledging the IRQ.<br/>
The original BIOS is so inefficient that it takes hundreds of clock cycles
between the interrupt request and the IRQ acknowledge, so, normally, it doesn't
require an additional delay.<br/>
However, the central mistake in the IRQ handler is that it doesn't memorize
which IRQ has originally triggered the interrupt. For example, it may get
triggered by a timer IRQ, but a newer card IRQ may occur during IRQ handling,
in that case, the card IRQ may get processed and acknowledged without the
required delay.<br/>
Used in Metal Gear Solid at 8009AA5Ch, and in alone1 at 800AE2F8h:<br/>
```
  24090056 li $t1, 0x56                       ;\                   ;        new_data:
  240A00B0 li $t2, 0xb0                       ; B(56h) GetC0Table  ;3C02A001 lui $v0, 0xa001
  0140F809 jalr $t2                           ;                    ;2442DFAC addiu $v0, $v0, -0x2054
  00000000  nop                               ;/                   ;00400008 jr $v0 ;=new_cont_d
  8C420018 lw $v0, 0x18($v0)                      ;\get C(06h)     ;00000000  nop    ;=A000DFACh
  00000000 nop                                    ;/               ;00000000 nop
  8C430070 lw $v1, 0x70($v0)                      ;\               ;        new_data_end:
  00000000 nop                                    ; get            ;        new_cont_d:
  3069FFFF andi $t1, $v1, 0xffff                  ; early_card     ;8C621074 lw $v0, 0x1074($v1)
  00094C00 sll $t1, $t1, 0x10                     ; irq_handler    ;00000000 nop
  8C430074 lw $v1, 0x74($v0)                      ;                ;30420080 andi $v0, $v0, 0x80 ;I_STAT.7
  00000000 nop                                    ;                ;1040000B beqz $v0, ret
  306AFFFF andi $t2, $v1, 0xffff                  ;/               ;00000000  nop
  012A1821 addu $v1, $t1, $t2                                      ;        wait_lop:
  24620028 addiu $v0, $v1, 0x28               ;=early+28h          ;8C621044 lw $v0, 0x1044($v1)
  3C0Axxxx lui $t2, %hi(new_data)             ;\new_data           ;00000000 nop
  254Axxxx addiu $t2, $t2, %lo(new_data)      ;/                   ;30420080 andi $v0, $v0, 0x80 ;SIO0_SR.7
  3C09xxxx lui $t1, %hi(new_data_end)         ;\new_data_end       ;1440FFFC bnez $v0, wait_lop
  2529xxxx addiu $t1, $t1, %lo(new_data_end)  ;/                   ;00000000  nop
          copy_lop:                                                ;3C020001 lui $v0, 0x1
  8D430000 lw $v1, 0x0($t2)                                        ;8C42DFFC lw $v0, -0x2004($v0)
  00000000 nop                                                     ;00000000 nop
  AC430000 sw $v1, 0x0($v0)                                        ;00400008 jr $v0 ;=[0000DFFCh]
  254A0004 addiu $t2, $t2, 0x4                                     ;00000000  nop
  1549FFFB bne $t2, $t1, copy_lop                                  ;        ret:
  24420004  addiu $v0, $v0, 0x4                                    ;03E00008 jr $ra
  3C010001 lui $at, 0x1                           ;\[DFFCh]=$v0    ;00000000  nop
  0xxxxxxx jal 0xXXXXXXXX                         ; and call ...   ;
  AC22DFFC  sw $v0, -0x2004($at)                  ;/               ;
```
Alternately, elo2 uses slightly different code at 8003961Ch:<br/>
```
  240A00B0 li $t2, 0xb0                       ;\                   ;        new_data:
  0140F809 jalr $t2                           ; B(56h) GetC0Table  ;3C02xxxx lui $v0, 0xXXXX
  24090056  li $t1, 0x56                      ;/                   ;2442xxxx addiu $v0, $v0, 0xXXXX
  8C420018 lw $v0, 0x18($v0)                      ;\get C(06h)     ;00400008 jr $v0 ;=new_cont_d
  00000000 nop                                    ;/               ;00000000  nop    ;=8xxxxxxxh
  8C430070 lw $v1, 0x70($v0)                      ;\               ;00000000 nop
  00000000 nop                                    ; get            ;        new_data_end:
  3069FFFF andi $t1, $v1, 0xffff                  ; early_card     ;        new_cont_d:
  8C430074 lw $v1, 0x74($v0)                      ; irq_handler    ;8C621074 lw $v0, 0x1074($v1)
  00094C00 sll $t1, $t1, 0x10                     ;                ;00000000 nop
  306AFFFF andi $t2, $v1, 0xffff                  ;                ;30420080 andi $v0, $v0, 0x80 ;I_STAT.7
  012A1821 addu $v1, $t1, $t2                     ;/               ;1040000B beqz $v0, ret
  3C0Axxxx lui $t2, %hi(new_data)                                  ;00000000  nop
  3C09xxxx lui $t1, %hi(new_data_end)                              ;        wait_lop:
  24620028 addiu $v0, $v1, 0x28               ;=early+28h          ;8C621044 lw $v0, 0x1044($v1)
  254Axxxx addiu $t2, $t2, %lo(new_data)      ;=new_data           ;00000000 nop
  2529xxxx addiu $t1, $t1, %lo(new_data_end)  ;=new_data_end       ;30420080 andi $v0, $v0, 0x80 ;SIO0_SR.7
          copy_lop:                                                ;1440FFFC bnez $v0, wait_lop
  8D430000 lw $v1, 0x0($t2)                                        ;00000000  nop
  254A0004 addiu $t2, $t2, 0x4                                     ;3C02xxxx lui $v0, 0xXXXX
  24420004 addiu $v0, $v0, 0x4                                     ;8C42xxxx lw $v0, 0x0($v0)
  1549FFFC bne $t2, $t1, copy_lop                                  ;00000000 nop
  AC43FFFC  sw $v1, -0x4($v0)                                      ;00400008 jr $v0 ;=[8xxxxxxxh]
  3C018xxx lui $at, 0x8XXX                        ;\[...]=$v0,      ;00000000  nop
  0xxxxxxx jal 0xXXXXXXXX                         ; and call ...   ;        ret:
  AC22xxxx  sw $v0, 0x0($at)                      ;/               ;03E00008 jr $ra
           ...                                                     ;00000000  nop
```
Note: The above @@wait\_lop's should be more preferably done with timeouts (else
they may hang endless if a Sony Mouse is newly connected; the mouse does have
/ACK stuck LOW on power-up).<br/>

#### patch\_uninstall\_early\_card\_irq\_handler:
Used to uninstall the "early\_card\_irq\_vector" (the BIOS installs that vector
from inside of B(4Ah) InitCARD2(pad\_enable), and, without patches, the BIOS
doesn't allow to uninstall it thereafter).<br/>
Used in Breath of Fire III (SLES-01304) at 8017E790, and also in Ace Combat 2
(SLUS-00404) at 801D23F4:<br/>
```
  240A00B0 li $t2, 0xb0            ;\
  0140F809 jalr $t2                ; B(56h) GetC0Table
  24090056  li $t1, 0x56           ;/
  3C0Axxxx lui $t2, %hi(new_data)
  3C09xxxx lui $t1, %hi(new_data_end)
  8C420018 lw $v0, 0x18($v0) ;=00000C80h = exception_handler = C(06h)
  254Axxxx addiu $t2, $t2, %lo(new_data) ;new_data
  2529xxxx addiu $t1, $t1, %lo(new_data_end)  ;new_data_end
          copy_lop:                ;\  new_data:
  8D430000 lw $v1, 0x0($t2)        ;    00000000 nop
  254A0004 addiu $t2, $t2, 0x4     ;    00000000 nop
  24420004 addiu $v0, $v0, 0x4     ;    00000000 nop
  1549FFFC bne $t2, $t1, copy_lop  ;   new_data_end:
  AC43006C  sw $v1, 0x6c($v0)      ;/
```
Alternately, more inefficient, used in Blaster Master-Blasting Again
(SLUS-01031) at 80063FF4h, and Raiden DX at 80029694h:<br/>
```
  24090056 li $t1, 0x56                           ;\
  240A00B0 li $t2, 0xb0                           ; B(56h) GetC0Table
  0140F809 jalr $t2                               ;
  00000000  nop                                   ;/
  8C420018 lw $v0, 0x18($v0)                  ;=00000C80h = exception_handler = C(06h)
  3C0Axxxx lui $t2, %hi(new_data)             ;\new_data
  254Axxxx addiu $t2, $t2, %lo(new_data)      ;/
  3C09xxxx lui $t1, %hi(new_data_end)         ;\new_data_end
  2529xxxx addiu $t1, $t1, %lo(new_data_end)  ;/
          copy_lop:                               ;\
  8D430000 lw $v1, 0x0($t2)                       ;   new_data:
  00000000 nop                                    ;    00000000 nop
  AC430070 sw $v1, 0x70($v0)                      ;    00000000 nop
  254A0004 addiu $t2, $t2, 0x4   ;src             ;    00000000 nop
  1549FFFB bne $t2, $t1, copy_lop                 ;   new_data_end:
  24420004  addiu $v0, $v0, 0x4  ;dst             ;/
```
Note: the above code is same as "patch\_install\_lightgun\_irq\_handler", except
that it writes to $v0+70h, instead of $v0+80h.<br/>

#### patch\_card\_specific\_delay:
Same purpose as the "early\_card\_irq\_patch" (but for the command/status bytes
rather than for the data bytes). The patch looks buggy since it inserts the
delay AFTER the acknowledge, but it DOES work (the BIOS accidently acknowledges
the IRQ twice; and the delay occurs PRIOR to 2nd acknowledge).<br/>
Used in Metal Gear Solid at 8009AAF0h, and in Legacy of Kain at 801A56D8h, and
in alone1 at 800AE38Ch:<br/>
```
  24090057 li $t1, 0x57  ;\                                       ;         new_data:
  240A00B0 li $t2, 0xb0  ; B(57h) GetB0Table                      ; 3C08A001 lui $t0, 0xa001
  0140F809 jalr $t2      ;/                                       ; 2508DF80 addiu $t0, $t0, -0x2080
  00000000  nop                                                   ; 0100F809 jalr $t0 ;=A000DF80h
  8C42016C lw $v0, 0x16c($v0) ;B(5Bh)                             ; 00000000  nop
  00000000 nop                                                    ; 00000000 nop
  8C4309C8 lw $v1, 0x9c8($v0)  ;blah                              ;         new_data_end:
  3C0Axxxx lui $t2, %hi(new_data)             ;\new_data          ; 946F000A lhu $t7, 0xa($v1)
  254Axxxx addiu $t2, $t2, %lo(new_data)      ;/                  ; 3C080000 lui $t0, 0x0
  3C09xxxx lui $t1, %hi(new_data_end)         ;\new_data_end      ; 01E2C025 or $t8, $t7, $v0
  2529xxxx addiu $t1, $t1, %lo(new_data_end)  ;/                  ; 37190012 ori $t9, $t8, 0x12
          copy_lop:                                               ; A479000A sh $t9, 0xa($v1)
  8D480000 lw $t0, 0x0($t2)                                       ; 24080028 li $t0, 0x28
  00000000 nop                                                    ;         wait_lop:
  AC4809C8 sw $t0, 0x9c8($v0)   ;B(5Bh)+9C8h..                    ; 2508FFFF addiu $t0, $t0, -0x1
  254A0004 addiu $t2, $t2, 0x4                                    ; 1500FFFE bnez $t0, wait_lop
  1549FFFB bne $t2, $t1, copy_lop                                 ; 00000000  nop
  24420004  addiu $v0, $v0, 0x4                                   ; 03E00008 jr $ra  ;above delay is
           ...                                                    ; 00000000  nop ;in UNCACHED RAM
```
Alternately, slightly different code used in elo2 at800396D4h, and in Resident
Evil 2 at 800910E4h:<br/>
```
  240A00B0 li $t2, 0xb0   ;\                                   ;         swap_begin:
  0140F809 jalr $t2       ; B(57h) GetB0Table                  ; 3C088xxx lui $t0, 0x8XXX
  24090057  li $t1, 0x57  ;/                                   ; 2508xxxx addiu $t0, $t0, 0xXXXX
  8C42016C lw $v0, 0x16c($v0) ;B(5Bh)                          ; 0100F809 jalr $t0 ;=8xxxxxxxh
  3C0Axxxx lui $t2, %hi(swap_begin)                            ; 00000000  nop
  3C09xxxx lui $t1, %hi(swap_end)                              ; 00000000 nop
  8C4309C8 lw $v1, 0x9c8($v0) ;blah                            ;         swap_end:
  254Axxxx addiu $t2, $t2, %lo(swap_begin)  ;=swap_begin       ;         ;- -  -
  2529xxxx addiu $t1, $t1, %lo(swap_end)    ;=swap_end         ; 00000000 nop
          swap_lop:                                            ; 240800C8 li $t0, 0xc8
  8C4309C8 lw $v1, 0x9c8($v0) ;B(5Bh)+9C8h..                   ;         wait_lop:
  8D480000 lw $t0, 0x0($t2)                                    ; 2508FFFF addiu $t0, $t0, -0x1
  254A0004 addiu $t2, $t2, 0x4                                 ; 1500FFFE bnez $t0, wait_lop
  AD43FFFC sw $v1, -0x4($t2)                                   ; 00000000  nop
  24420004 addiu $v0, $v0, 0x4                                 ; 03E00008 jr $ra  ;above delay is
  1549FFFA bne $t2, $t1, swap_lop                              ; 00000000  nop ;in CACHED RAM
  AC4809C4  sw $t0, 0x9c4($v0)                                 ;
```

#### patch\_card\_info\_step4:
The "card\_info" function sends an incomplete read command to the card; in order
to receive status information. After receiving the last byte, the function does
accidently send a further byte to the card, so the card responds by another
byte (and another IRQ7), which is not processed nor acknowledged by the BIOS.
This patch kills the opcode that sends the extra byte.<br/>
Used in alone1 at 800AE214h:<br/>
```
  24090057 li $t1, 0x57                           ;\
  240A00B0 li $t2, 0xb0                           ; B(57h) GetB0Table
  0140F809 jalr $t2                               ;
  00000000  nop                                   ;/
  240A0009 li $t2, 0x9            ;=blah
  8C42016C lw $v0, 0x16c($v0)     ;=B(5Bh)
  00000000 nop
  20431988 addi $v1, $v0, 0x1988  ;=B(5Bh)+1988h  ;\store a NOP,
  0xxxxxxx jal 0xXXXXXXXX                         ; and call ...
  AC600000  sw $zero, 0x0($v1)    ;=nop           ;/
```

#### patch\_pad\_error\_handling\_and\_get\_pad\_enable\_functions:
If a transmission error occurs (or if there's no controller connected), then
the Pad handler handler does usually issue a strange chip select signal to the
OTHER controller slot, and does then execute the bizarre\_pad\_delay function.
The patch below overwrites that behaviour by NOPs. Purpose of the original (and
patched) behaviour is unknown.<br/>
Used by Perfect Assassin at 800519D4h:<br/>
```
  240A00B0 li $t2, 0xb0                          ;\
  0140F809 jalr $t2                              ; B(57h) GetB0Table
  24090057  li $t1, 0x57                         ;/
  8C42016C lw $v0, 0x16c($v0)    ;=B(5Bh)
  3C01xxxx lui $at, 0xXXXX
  20430884 addi $v1, $v0, 0x884  ;B(5Bh)+884h
  AC23xxxx sw $v1, 0x0($at)      ;<--- SetPadEnableFlag()
  3C01xxxx lui $at, 0xXXXX
  20430894 addi $v1, $v0, 0x894  ;B(5Bh)+894h
  2409000B li $t1, 0xb           ;len
  AC23xxxx sw $v1, 0x0($at)      ;<--- ClearPadEnableFlag()
          fill_lop:                              ;\
  2529FFFF addiu $t1, $t1, -0x1                  ;
  AC400594 sw $zero, 0x594($v0)  ;B(5Bh)+594h..  ; erase error handling
  1520FFFD bnez $t1, fill_lop                    ;
  24420004  addiu $v0, $v0, 0x4                  ;/
```
Alternately, same as above, but with inefficient nops, used by Sporting Clays
at 8001B4B4h:<br/>
```
  24090057 li $t1, 0x57      ;\
  240A00B0 li $t2, 0xb0      ; B(57h) GetB0Table
  0140F809 jalr $t2          ;
  00000000  nop              ;/
  8C42016C lw $v0, 0x16c($v0)
  2409000B li $t1, 0xb ;len
  20430884 addi $v1, $v0, 0x884
  3C01xxxx lui $at, 0xXXXX
  AC23xxxx sw $v1, 0x0($at)      ;<--- SetPadEnableFlag()
  20430894 addi $v1, $v0, 0x894
  3C01xxxx lui $at, 0xXXXX
  AC23xxxx sw $v1, 0x0($at)      ;<--- ClearPadEnableFlag()
          fill_lop:              ;\
  AC400594 sw $zero, 0x594($v0)  ;
  24420004 addiu $v0, $v0, 0x4   ; erase error handling
  2529FFFF addiu $t1, $t1, -0x1  ;
  1520FFFC bnez $t1, fill_lop    ;
  00000000  nop                  ;/
```
Alternately, same as above, but without getting PadEnable functions, used in
Pandemonium II (at 80083C94h and at 8010B77Ch):<br/>
```
  240A00B0 li $t2, 0xb0                  ;\
  0140F809 jalr $t2                      ; B(57h) GetB0Table
  24090057  li $t1, 0x57                 ;/
  8C42016C lw $v0, 0x16c($v0)    ;=B(5Bh)
  2409000B li $t1, 0xb           ;len            ;\
          fill_lop:                              ;
  2529FFFF addiu $t1, $t1, -0x1                  ; erase error handling
  AC400594 sw $zero, 0x594($v0)  ;B(5Bh)+594h..  ;
  1520FFFD bnez $t1, fill_lop                    ;
  24420004  addiu $v0, $v0, 0x4                  ;/
```

#### patch\_optional\_pad\_output:
The normal BIOS functions are only allowing to READ from the controllers, but
not to SEND data to them (which would be required to control Rumble motors, and
to auto-activate Analog mode without needing the user to press the Analog
button). Internally, the BIOS does include some code for sending data to the
controller, but it doesn't offer a function vector for setting up the data
source address, and, even if that would be supported, it clips the data bytes
to 00h or 01h. The patch below retrieves the required SetPadOutput function
address (in which only the src1/src2 addresses are relevant, the blah1/blah2
values aren't used), and suppresses clipping (ie. allows to send any bytes in
range 00h..FFh).<br/>
Used in Resident Evil 2 at 80091914h:<br/>
```
  240A00B0 li $t2, 0xb0                                          ;\
  0140F809 jalr $t2                                              ; B(57h) GetB0Table
  24090057  li $t1, 0x57                                         ;/
  8C42016C lw $v0, 0x16c($v0)                    ;B(5Bh)
  3C0Axxxx lui $t2, %hi(new_data)
  3C09xxxx lui $t1, %hi(new_data_end)
  3C01xxxx lui $at, 0xXXXX
  204307A0 addi $v1, $v0, 0x7a0                  ;B(5Bh)+7A0h
  254Axxxx addiu $t2, $t2, %lo(new_data)      ;=new_data
  2529xxxx addiu $t1, $t1, %lo(new_data_end)  ;=new_data_end
  AC23xxxx sw $v1, 0x0($at)                      ;<--- SetPadOutput(src1,blah1,src2,blah2)
          double_copy_lop:                                       ;\
  8D430000 lw $v1, 0x0($t2)                                      ;           new_data:
  254A0004 addiu $t2, $t2, 0x4                                   ;   00551024 and $v0, $v0, $s5
  AC4303D8 sw $v1, 0x3d8($v0)                    ;<--- here      ;   00000000 nop
  24420004 addiu $v0, $v0, 0x4                                   ;   00000000 nop
  1549FFFB bne $t2, $t1, double_copy_lop                         ;   00000000 nop
  AC4304DC  sw $v1, 0x4dc($v0)                   ;<--- here      ;/          new_data_end:
```
Alternately, more inefficient (with NOPs), used in Lemmings at 80036618h:<br/>
```
  24090057 li $t1, 0x57                                        ;\
  240A00B0 li $t2, 0xb0                                        ; B(57h) GetB0Table
  0140F809 jalr $t2                                            ;
  00000000  nop                                                ;/
  3C0Axxxx lui $t2, %hi(new_data)
  254Axxxx addiu $t2, $t2, %lo(new_data)      ;=new_data
  3C09xxxx lui $t1, %hi(new_data_end)
  2529xxxx addiu $t1, $t1, %lo(new_data_end)  ;=new_data_end
  8C42016C lw $v0, 0x16c($v0) ;B(5Bh)
  00000000 nop
  204307A0 addi $v1, $v0, 0x7a0    ;B(5Bh)+7A0h
  3C01xxxx lui $at, 0xXXXX
  AC23xxxx sw $v1, 0x0($at) ;<--- SetPadOutput(src1,blah1,src2,blah2)
          double_copy_lop:                                     ;\
  8D430000 lw $v1, 0x0($t2)                                    ;           new_data:
  00000000 nop                                                 ;   00551024 and $v0, $v0, $s5
  AC4303D8 sw $v1, 0x3d8($v0)                                  ;   00000000 nop
  AC4304E0 sw $v1, 0x4e0($v0)                                  ;   00000000 nop
  24420004 addiu $v0, $v0, 0x4                                 ;   00000000 nop
  254A0004 addiu $t2, $t2, 0x4                                 ;           new_data_end:
  1549FFF9 bne $t2, $t1, double_copy_lop                       ;
  00000000  nop                                                ;/
```

#### patch\_no\_pad\_card\_auto\_ack:
This patch suppresses automatic IRQ0 (vblank) acknowleding in the Pad/Card IRQ
handler, that, even if auto-ack is enabled. Obviously, one could as well
disable auto-ack via B(5Bh) ChangeClearPAD(int), so this patch is total
nonsense. Used in Resident Evil 2 at 800919ACh:<br/>
```
  240A00B0 li $t2, 0xb0                          ;\
  0140F809 jalr $t2                              ; B(57h) GetB0Table
  24090057  li $t1, 0x57                         ;/
  8C42016C lw $v0, 0x16c($v0)    ;=B(5Bh)
  240A0009 li $t2, 0x9           ;len            ;\
  2043062C addi $v1, $v0, 0x62c  ;=B(5Bh)+62Ch   ;
          fill_lop:                              ;
  254AFFFF addiu $t2, $t2, -0x1                  ;
  AC600000 sw $zero, 0x0($v1)                    ;
  1540FFFD bnez $t2, fill_lop                    ;
  24630004  addiu $v1, $v1, 0x4                  ;/
```
Alternately, same as above, but more inefficient, used in Sporting Clays at
8001B53Ch:<br/>
```
  24090057 li $t1, 0x57                        ;\
  240A00B0 li $t2, 0xb0                        ; B(57h) GetB0Table
  0140F809 jalr $t2                            ;
  00000000  nop                                ;/
  240A0009 li $t2, 0x9    ;len
  8C42016C lw $v0, 0x16c($v0)
  00000000 nop
  2043062C addi $v1, $v0, 0x62c
          fill_lop:                            ;\
  AC600000 sw $zero, 0x0($v1)                  ;
  24630004 addiu $v1, $v1, 0x4                 ;
  254AFFFF addiu $t2, $t2, -0x1                ;
  1540FFFC bnez $t2, fill_lop                  ;
  00000000  nop                                ;/
```
Either way, no matter if using the patch or if using ChangeClearPAD(int),
having auto-ack disabled allows to install a custom vblank IRQ0 handler, which
is probably desired for most games, however, mind that the PSX BIOS doesn't
actually support the same IRQ to be processed by two different IRQ handlers,
eg. the custom handler may acknowledge the IRQ even when the Pad/Card handler
didn't process it, so pad input may become bumpy.<br/>

#### patch\_install\_lightgun\_irq\_handler:
Used in Sporting Clays at 80027D68h (when Konami Lightgun connected):<br/>
```
  240A00B0 li $t2, 0xb0      ;\
  0140F809 jalr $t2          ; B(56h) GetC0Table
  24090056  li $t1, 0x56     ;/
  3C0Axxxx lui $t2, 0xXXXX         ;src
  3C09xxxx lui $t1, 0xXXXX         ;src.end
  8C420018 lw $v0, 0x18($v0)       ;C(06h)
  254Axxxx addiu $t2, $t2, 0xXXXX  ;src
  2529xxxx addiu $t1, $t1, 0xXXXX  ;src.end (=src+10h)
          copy_lop:                     ;\    ;        src:
  8D430000 lw $v1, 0x0($t2)             ;     ;3C02xxxx lui $v0, 0xXXXX
  254A0004 addiu $t2, $t2, 0x4          ;     ;2442xxxx addiu $v0, $v0, 0xXXXX
  24420004 addiu $v0, $v0, 0x4          ;     ;0040F809 jalr $v0  ;lightgun_proc
  1549FFFC bne $t2, $t1, copy_lop       ;     ;00000000  nop
  AC43007C  sw $v1, 0x7c($v0)           ;/             src_end:
```
Alternately, same as above, but more inefficient, used in DQM (Dragon Quest
Monsters 1&2) at 80089390h (install) and 800893F8h (uninstall):<br/>
```
  24090056 li $t1, 0x56                       ;\
  240A00B0 li $t2, 0xb0                       ; B(56h) GetC0Table
  0140F809 jalr $t2                           ;
  00000000  nop                               ;/
  8C420018 lw $v0, 0x18($v0)                  ;=00000C80h = exception_handler = C(06h)
  3C0Axxxx lui $t2, %hi(new_data)             ;\new_data (3xNOP)
  254Axxxx addiu $t2, $t2, %lo(new_data)      ;/
  3C09xxxx lui $t1, %hi(new_data_end)         ;\new_data_end
  2529xxxx addiu $t1, $t1, %lo(new_data_end)  ;/
          copy_lop:                               ;\
  8D430000 lw $v1, 0x0($t2)                       ; new_data: ;for (un-)install...
  00000000 nop                                    ; 00000000 nop 3C02xxxx lui $v0, 0xXXXX
  AC430080 sw $v1, 0x80($v0)                      ; 00000000 nop 2442xxxx addiu $v0, $v0, 0xXXXX
  254A0004 addiu $t2, $t2, 0x4                    ; 00000000 nop 0040F809 jalr $v0  ;proc
  1549FFFB bne $t2, $t1, copy_lop                 ; new_data_end:
  24420004  addiu $v0, $v0, 0x4                   ;/
```
Some lightgun games (eg. Project Horned Owl) do (additionally to above stuff)
hook the exception vector at 00000080h, the hook copies the horizontal
coordinate (timer0) to a variable in RAM, thus getting the timer0 value
"closest" to the actual IRQ execution. Doing that may eliminate some
unpredictable timing offsets that could be caused by cache hits/misses during
later IRQ handling (and may also eliminate a rather irrelevant 1-cycle
inaccuracy depending on whether EPC was pointing to a GTE opcode, and also
eliminates constant cycle offsets depending on whether early\_card\_irq\_handler
was installed and enabled, and might eliminate timing differences for different
BIOS versions).<br/>

#### set\_conf\_without\_realloc:
Used in Spec Ops Airborne Commando at 80070AE8h, and also in the homebrew game
Roll Boss Rush at 80010B68h and 8001B85Ch. Purpose is unknown (maybe to
override improperly defined .EXE headers).<br/>
```
  8C030474 lw $v1, 0x474($zero)               ;\get ptr to A(9Dh) GetConf (done so,
  00000000 nop                                ;/as there's no "GetA0Table" funtion)
  94620000 lhu $v0, 0x0($v1)     ;lui msw     ;\
  84630004 lh $v1, 0x4($v1)      ;lw lsw+8    ; extract ptr to "boot_cnf_values"
  00021400 sll $v0, $v0, 0x10    ;msw*10000h  ; (from first 2 opcodes of GetConf)
  2442FFF8 addiu $v0, $v0, -0x8  ;undo +8     ;
  00431021 addu $v0, $v0, $v1    ;lsw         ;/
  AC450000 sw $a1, 0x0($v0)      ;num_TCB     ;\set num_EvCB,num_TCB,stacktop
  AC440004 sw $a0, 0x4($v0)      ;num_EvCB    ; (unlike A(9Ch) SetConf, without
  03E00008 jr $ra                             ; actually reallocting anything)
  AC460008  sw $a2, 0x8($v0)     ;stacktop    ;/
```

#### Cheat Devices
CAETLA detects the PSX BIOS version by checksumming BFC06000h..BFC07FFFh and
does then use some hardcoded BIOS addresses based on that checksum. The reason
for doing that is probably that the Pre-Boot Expansion ROM vector is called
with the normal A0h/B0h/C0h vectors being still uninitialized.<br/>
Problems are that the hardcoded addresses won't work with all BIOSes (eg. not
with the no$psx bios clone, probably also not with the newer PS2 BIOS),
moreover, the checksumming can fail with patched original BIOSes (eg. no$psx
allows to enable TTY debug messages and to skip the BIOS intro).<br/>
The Cheat Firmwares are probably also hooking the Vblank handler, and maybe
also some other functions.<br/>
ACTION REPLAY (at least later versions like 2.81) uses the Pre-Boot handler to
set a COP0 hardware breakpoint at 80030000h and does then resume normal BIOS
booting (which will then initialize important things like A0h/B0h/C0h tables,
and will then break when starting the GUI code at 80030000h).<br/>
XPLORER searches opcode 24040385h at BFC06000h and up, and does then place a
COP0 opcode fetch breakpoint at the opcode address+10h (note: this is within a
branch delay slot, which makes COP0 emulation twice as complicated). XPLORER
does also require space in unused BIOS RAM addresses (eg. Xplorer v3.20: addr
7880h at 1F002280h, addr 017Fh at 1F006A58h).<br/>

#### Note
Most games include two or three patches. The only game that I've seen so far
that does NOT use any patches is Wipeout 2097.<br/>
