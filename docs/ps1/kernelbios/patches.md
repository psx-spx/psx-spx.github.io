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

#### patch\_missing\_cop0r13\_in\_exception\_handler:
In newer Kernel version, the exception handler reads cop0r13/cause to r2,
examines the Excode value in r2, and if the exception was caused by an
interrupt, and if the next opcode (at EPC) is a GTE/COP2 command, then it does
increment EPC by 4. The GTE commands are executed even if an interrupt occurs
simultaneously, so, without adjusting EPC, the command would be executed twice.
With some commands that'd just waste some clock cycles, with other commands it
may cause data to be written twice to the GTE FIFOs, or may re-use the result
from the 1st command execution as input to the 2nd execution.<br/>
The old "CEX-1000 KT-3" Kernel version did examine r2, but it "forgot" to
previously load cop0r13 to r2, so it did randomly examine a garbage value. The
patch inserts the missing opcode, used in elo2 at 80033740h, and in Pandemonium
II at 8007F3FCh:<br/>
```
  240A00B0 mov  r10,0B0h                      ;\   00000000 nop
  0140F809 call r10                           ;    00000000 nop
  24090056 +mov  r9,56h                       ;/   241A0100 mov k0,100h
  3C0Axxxx mov  r10,xxxx0000h                 ;\   8F5A0008 mov k0,[k0+8h]
  3C09xxxx mov  r9,xxxx0000h                  ;    00000000 nop
  8C420018 mov  r2,[r2+06h*4] ;=C(06h)        ;    8F5A0000 mov k0,[k0]
  254Axxxx add  r10,xxxxh ;=@@new_data        ;    00000000 nop
  2529xxxx add  r9,xxxxh  ;=@@new_data_end    ;/   235A0008 addt k0,8h
          @@copy_lop:                         ;\   AF410004 mov [k0+4h],r1
  8D430000 mov  r3,[r10]                      ;    AF420008 mov [k0+8h],r2
  254A0004 add  r10,4h                        ;    AF43000C mov [k0+0Ch],r3
  24420004 add  r2,4h                         ;    AF5F007C mov [k0+7Ch],ra
  1549FFFC jne  r10,r9,@@copy_lop             ;    40026800 mov r2,cop0r13
  AC43FFFC +mov [r2-4h],r3                    ;/   00000000 nop
```
Alternately, same as above, but using k0/k1 instead of r10/r9, used in Ridge
Racer at 80047B14h:<br/>
```
  240A00B0 mov  r10,0B0h                      ;\     00000000 nop
  0140F809 call r10                           ;      00000000 nop
  24090056 +mov r9,56h                        ;/     241A0100 mov  k0,100h
  3C1Axxxx mov  k0,xxxx0000h                  ;\     8F5A0008 mov  k0,[k0+8h]
  3C1Bxxxx mov  k1,xxxx0000h                  ;      00000000 nop
  8C420018 mov  r2,[r2+06h*4] ;=C(06h)        ;      8F5A0000 mov  k0,[k0]
  275Axxxx add  k0,xxxxh  ;=@@new_data        ;      00000000 nop
  277Bxxxx add  k1,xxxxh  ;=@@new_data_end    ;/     235A0008 addt k0,8h
          @@copy_lop:                         ;\     AF410004 mov  [k0+4h],r1
  8F430000 mov  r3,[k0]                       ;      AF420008 mov  [k0+8h],r2
  275A0004 add  k0,4h                         ;      AF43000C mov  [k0+0Ch],r3
  24420004 add  r2,4h                         ;      AF5F007C mov  [k0+7Ch],ra
  175BFFFC jne  k0,k1,@@copy_lop              ;      40026800 mov  r2,cop0r13
  AC43FFFC +mov [r2-4h],r3                    ;/     00000000 nop
```
Alternately, slightly different code used in metal\_gear\_solid at 80095CC0h, and
in alone1 at 800A3ECCh:<br/>
```
  24090056 mov  r9,56h                        ;\
  240A00B0 mov  r10,0B0h                      ; B(56h) GetC0Table
  0140F809 call r10                           ;
  00000000 +nop                               ;/
  8C420018 mov  r2,[r2+06h*4] ;=00000C80h = exception_handler = C(06h)
  00000000 nop
  24420028 add  r2,28h
  00407821 mov  r15,r2
  3C0Axxxx lui  r10,xxxxh ;\@@ori_data        ;\
  254Axxxx add  r10,xxxxh ;/                  ;
  3C09xxxx lui  r9,xxxxh  ;\@@ori_data_end    ; @@ori_data:
  2529xxxx add  r9,xxxxh  ;/                  ;  AF410004 mov [k0+4h],r1
          @@verify_lop:                       ;  AF420008 mov [k0+8h],r2
  8D430000 mov  r3,[r10]                      ;  AF43000C mov [k0+0Ch],r3
  8C4B0000 mov  r11,[r2]                      ;  AF5F007C mov [k0+7Ch],ra
  254A0004 add  r10,4h                        ;  40037000 mov r3,cop0r14
  146B000E jne  r3,r11,@@verify_mismatch      ;  00000000 nop
  24420004 +add r2,4h                         ;
  1549FFFA jne  r10,r9,@@verify_lop           ;
  00000000 +nop                               ;/
  01E01021 mov  r2,r15
  3C0Axxxx lui  r10,xxxxh ;\@@new_data        ;\
  254Axxxx add  r10,xxxxh ;/                  ;
  3C09xxxx lui  r9,xxxxh  ;\@@new_data_end    ; @@new_data:
  2529xxxx add  r9,xxxxh  ;/                  ;  AF410004 mov [k0+4h],r1
          @@copy_lop:                         ;  AF420008 mov [k0+8h],r2
  8D430000 mov  r3,[r10]                      ;  40026800 mov r2,cop0r13
  00000000 nop                                ;  AF43000C mov [k0+0Ch],r3
  AC430000 mov  [r2],r3                       ;  40037000 mov r3,cop0r14
  254A0004 add  r10,4h                        ;  AF5F007C mov [k0+7Ch],ra
  1549FFFB jne  r10,r9,@@copy_lop             ;
  24420004 +add r2,4h                         ;/
          @@verify_mismatch:
```
Alternately, a bugged/nonfunctional homebrew variant (used by Hitmen's
"minimum" demo):<br/>
```
  ;BUG1: 8bit "movb r6" should be 32bit "mov r6"
  ;BUG2: @@copy_lop should transfer 6 words (not 7 words)
  ;BUG3: and, asides, the minimum demo works only with PAL BIOS (not NTSC)
  0xxxxxxx call xxxxxxxxh               ;\B(56h) GetC0Table
  00000000 +nop                         ;/(mov r8,0B0h, jmp r8, +mov r9,56h)
  3C04xxxx mov  r4,xxxx0000h  ;\@@ori_data
  2484xxxx add  r4,xxxxh      ;/
  90460018 movb r6,[r2+06h*4] ;BUG1 ;exception_handler = C(06h)
  24870018 add  r7,r4,18h ;@@ori_end     ;\
  24C50028 add  r5,r6,28h ;C(06h)+28h    ;
  00A03021 mov  r6,r5                    ;                   @@ori_data:
          @@verify_lop:                  ;  80086520 AF410004 mov [k0+4h],r1
  8CA30000 mov  r3,[r5]                  ;  80086524 AF420008 mov [k0+8h],r2
  8C820000 mov  r2,[r4]                  ;  80086528 AF43000C mov [k0+0Ch],r3
  00000000 nop                           ;  8008652C AF5F007C mov [k0+7Ch],ra
  1462000C jne  r3,r2,@@verify_mismatch  ;  80086530 40037000 mov r3,cop0r14
  24840004 +add r4,4h                    ;  80086534 00000000 nop
  1487FFFA jne  r4,r7,@@verify_lop       ;                   @@ori_end:
  24A50004 +add r5,4h                    ;/
  00C02821 mov  r5,r6                    ;\                  @@new_data:
  3C04xxxx mov  r4,xxxx0000h ;\@@new_data;  80086538 AF410004 mov [k0+4h],r1
  2484xxxx add  r4,xxxxh     ;/          ;  8008653C AF420008 mov [k0+8h],r2
  2483001C add  r3,r4,1Ch ;@@bugged_end  ;  80086540 40026800 mov r2,cop0r13
          @@copy_lop:                    ;  80086544 AF43000C mov [k0+0Ch],r3
  8C820000 mov  r2,[r4]                  ;  80086548 40037000 mov r3,cop0r14
  24840004 add  r4,4h                    ;  8008654C AF5F007C mov [k0+7Ch],ra
  ACA20000 mov  [r5],r2                  ;                   @@new_end:
  1483FFFC jne  r4,r3,@@copy_lop         ;  80086550 00000000 nop  ;BUG2
  24A50004 +add r5,4h                    ;/                  @@bugged_end:
          @@verify_mismatch:
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
  24090056 mov  r9,56h    ;\                  ;        @@new_data:
  240A00B0 mov  r10,0B0h  ; B(56h) GetC0Table ;3C02A001 lui  r2,0A001h
  0140F809 call r10       ;                   ;2442DFAC sub  r2,2054h
  00000000 +nop           ;/                  ;00400008 jmp  r2 ;=@@new_cont_d
  8C420018 mov  r2,[r2+06h*4] ;\get C(06h)    ;00000000 +nop    ;=A000DFACh
  00000000 nop                ;/              ;00000000 nop
  8C430070 mov  r3,[r2+70h]   ;\              ;        @@new_data_end:
  00000000 nop                ; get           ;        @@new_cont_d:
  3069FFFF and  r9,r3,0FFFFh  ; early_card    ;8C621074 mov  r2,[r3+1074h]
  00094C00 shl  r9,10h        ; irq_handler   ;00000000 nop
  8C430074 mov  r3,[r2+74h]   ;               ;30420080 and  r2,80h ;I_STAT.7
  00000000 nop                ;               ;1040000B jz   r2,@@ret
  306AFFFF and  r10,r3,0FFFFh ;/              ;00000000 +nop
  012A1821 add  r3,r9,r10                     ;        @@wait_lop:
  24620028 add  r2,r3,28h ;=early+28h         ;8C621044 mov  r2,[r3+1044h]
  3C0Axxxx lui  r10,xxxxh ;\@@new_data        ;00000000 nop
  254Axxxx sub  r10,xxxxh ;/                  ;30420080 and  r2,80h ;SIO0_SR.7
  3C09xxxx lui  r9,xxxxh  ;\@@new_data_end    ;1440FFFC jnz  r2,@@wait_lop
  2529xxxx sub  r9,xxxxh  ;/                  ;00000000 +nop
          @@copy_lop:                         ;3C020001 lui  r2,0001h
  8D430000 mov  r3,[r10]                      ;8C42DFFC mov  r2,[r2-2004h]
  00000000 nop                                ;00000000 nop
  AC430000 mov  [r2],r3                       ;00400008 jmp  r2 ;=[0000DFFCh]
  254A0004 add  r10,4h                        ;00000000 +nop
  1549FFFB jne  r10,r9,@@copy_lop             ;        @@ret:
  24420004 +add r2,4h                         ;03E00008 ret
  3C010001 lui  r1,0001h      ;\[DFFCh]=r2    ;00000000 +nop
  0xxxxxxx call xxxxxxxxh     ; and call ...  ;
  AC22DFFC +mov [r1-2004h],r2 ;/              ;
```
Alternately, elo2 uses slightly different code at 8003961Ch:<br/>
```
  240A00B0 mov  r10,0B0h  ;\                  ;        @@new_data:
  0140F809 call r10       ; B(56h) GetC0Table ;3C02xxxx lui  r2,8xxxh
  24090056 +mov r9,56h    ;/                  ;2442xxxx sub  r2,xxxxh
  8C420018 mov  r2,[r2+06h*4] ;\get C(06h)    ;00400008 jmp  r2 ;=@@new_cont_d
  00000000 nop                ;/              ;00000000 +nop    ;=8xxxxxxxh
  8C430070 mov  r3,[r2+70h]   ;\              ;00000000 nop
  00000000 nop                ; get           ;        @@new_data_end:
  3069FFFF and  r9,r3,0FFFFh  ; early_card    ;        @@new_cont_d:
  8C430074 mov  r3,[r2+74h]   ; irq_handler   ;8C621074 mov  r2,[r3+1074h]
  00094C00 shl  r9,10h        ;               ;00000000 nop
  306AFFFF and  r10,r3,0FFFFh ;               ;30420080 and  r2,80h ;I_STAT.7
  012A1821 add  r3,r9,r10     ;/              ;1040000B jz   r2,@@ret
  3C0Axxxx mov  r10,xxxx0000h                 ;00000000 +nop
  3C09xxxx mov  r9,xxxx0000h                  ;        @@wait_lop:
  24620028 add  r2,r3,28h ;=early+28h         ;8C621044 mov  r2,[r3+1044h]
  254Axxxx sub  r10,xxxxh ;=@@new_data        ;00000000 nop
  2529xxxx sub  r9,xxxxh  ;=@@new_data_end    ;30420080 and  r2,80h ;SIO0_SR.7
          @@copy_lop:                         ;1440FFFC jnz  r2,@@wait_lop
  8D430000 mov  r3,[r10]                      ;00000000 +nop
  254A0004 add  r10,4h                        ;3C02xxxx lui  r2,8xxxh
  24420004 add  r2,4h                         ;8C42xxxx mov  r2,[r2-xxxxh]
  1549FFFC jne  r10,r9,@@copy_lop             ;00000000 nop
  AC43FFFC +mov [r2-4h],r3                    ;00400008 jmp  r2 ;=[8xxxxxxxh]
  3C018xxx mov  r1,8xxx0000h  ;\[...]=r2,     ;00000000 +nop
  0xxxxxxx call xxxxxxxxh     ; and call ...  ;        @@ret:
  AC22xxxx +mov [r1+xxxxh],r2 ;/              ;03E00008 ret
           ...                                ;00000000 +nop
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
  240A00B0 mov  r10,0B0h          ;\
  0140F809 call r10               ; B(56h) GetC0Table
  24090056 +mov r9,56h            ;/
  3C0Axxxx mov  r10,xxxx0000h
  3C09xxxx mov  r9,xxxx0000h
  8C420018 mov  r2,[r2+06h*4] ;=00000C80h = exception_handler = C(06h)
  254Axxxx add  r10,xxxxh ;@@new_data
  2529xxxx add  r9,xxxxh  ;@@new_data_end
          @@copy_lop:             ;\  @@new_data:
  8D430000 mov  r3,[r10]          ;    00000000 nop
  254A0004 add  r10,4h            ;    00000000 nop
  24420004 add  r2,4h             ;    00000000 nop
  1549FFFC jne  r10,r9,@@copy_lop ;   @@new_data_end:
  AC43006C +mov [r2+70h-4],r3     ;/
```
Alternately, more inefficient, used in Blaster Master-Blasting Again
(SLUS-01031) at 80063FF4h, and Raiden DX at 80029694h:<br/>
```
  24090056 mov  r9,56h            ;\
  240A00B0 mov  r10,0B0h          ; B(56h) GetC0Table
  0140F809 call r10               ;
  00000000 +nop                   ;/
  8C420018 mov  r2,[r2+06h*4] ;=00000C80h = exception_handler = C(06h)
  3C0Axxxx mov  r10,xxxx0000h ;\@@new_data
  254Axxxx add  r10,xxxxh     ;/
  3C09xxxx mov  r9,xxxx0000h  ;\@@new_data_end
  2529xxxx add  r9,xxxxh      ;/
          @@copy_lop:             ;\
  8D430000 mov  r3,[r10]          ;   @@new_data:
  00000000 nop                    ;    00000000 nop
  AC430070 mov  [r2+70h],r3       ;    00000000 nop
  254A0004 add  r10,4h  ;src      ;    00000000 nop
  1549FFFB jne  r10,r9,@@copy_lop ;   @@new_data_end:
  24420004 +add r2,4h   ;dst      ;/
```
Note: the above code is same as "patch\_install\_lightgun\_irq\_handler", except
that it writes to r2+70h, instead of r2+80h.<br/>

#### patch\_card\_specific\_delay:
Same purpose as the "early\_card\_irq\_patch" (but for the command/status bytes
rather than for the data bytes). The patch looks buggy since it inserts the
delay AFTER the acknowledge, but it DOES work (the BIOS accidently acknowledges
the IRQ twice; and the delay occurs PRIOR to 2nd acknowledge).<br/>
Used in Metal Gear Solid at 8009AAF0h, and in Legacy of Kain at 801A56D8h, and
in alone1 at 800AE38Ch:<br/>
```
  24090057 mov  r9,57h   ;\                   ;         @@new_data:
  240A00B0 mov  r10,0B0h ; B(57h) GetB0Table  ; 3C08A001 lui  r8,0A001h
  0140F809 call r10      ;/                   ; 2508DF80 sub  r8,2080h
  00000000 +nop                               ; 0100F809 call r8 ;=A000DF80h
  8C42016C mov  r2,[r2+5Bh*4] ;B(5Bh)         ; 00000000 +nop
  00000000 nop                                ; 00000000 nop
  8C4309C8 mov  r3,[r2+9C8h]  ;blah           ;         @@new_data_end:
  3C0Axxxx lui  r10,xxxxh ;\@@new_data        ; 946F000A movh r15,[r3+0Ah]
  254Axxxx sub  r10,xxxxh ;/                  ; 3C080000 mov  r8,0h
  3C09xxxx lui  r9,xxxxh  ;\@@new_data_end    ; 01E2C025 or   r24,r15,r2
  2529xxxx sub  r9,xxxxh  ;/                  ; 37190012 or   r25,r24,12h
          @@copy_lop:                         ; A479000A movh [r3+0Ah],r25
  8D480000 mov  r8,[r10]                      ; 24080028 mov  r8,28h
  00000000 nop                                ;         @@wait_lop:
  AC4809C8 mov  [r2+9C8h],r8   ;B(5Bh)+9C8h.. ; 2508FFFF sub  r8,1h
  254A0004 add  r10,4h                        ; 1500FFFE jnz  r8,@@wait_lop
  1549FFFB jne  r10,r9,@@copy_lop             ; 00000000 +nop
  24420004 +add r2,4h                         ; 03E00008 ret  ;above delay is
           ...                                ; 00000000 +nop ;in UNCACHED RAM
```
Alternately, slightly different code used in elo2 at800396D4h, and in Resident
Evil 2 at 800910E4h:<br/>
```
  240A00B0 mov  r10,0B0h ;\                   ;         @@swap_begin:
  0140F809 call r10      ; B(57h) GetB0Table  ; 3C088xxx lui  r8,8xxxh
  24090057 +mov r9,57h   ;/                   ; 2508xxxx sub  r8,xxxxh
  8C42016C mov  r2,[r2+5Bh*4] ;B(5Bh)         ; 0100F809 call r8 ;=8xxxxxxxh
  3C0Axxxx mov  r10,xxxx0000h                 ; 00000000 +nop
  3C09xxxx mov  r9,xxxx0000h                  ; 00000000 nop
  8C4309C8 mov  r3,[r2+9C8h] ;blah            ;         @@swap_end:
  254Axxxx sub  r10,xxxxh  ;=@@swap_begin     ;         ;- -  -
  2529xxxx sub  r9,xxxxh   ;=@@swap_end       ; 00000000 nop
          @@swap_lop:                         ; 240800C8 mov  r8,0C8h
  8C4309C8 mov  r3,[r2+9C8h] ;B(5Bh)+9C8h..   ;         @@wait_lop:
  8D480000 mov  r8,[r10]                      ; 2508FFFF sub  r8,1h
  254A0004 add  r10,4h                        ; 1500FFFE jnz  r8,@@wait_lop
  AD43FFFC mov  [r10-4h],r3                   ; 00000000 +nop
  24420004 add  r2,4h                         ; 03E00008 ret  ;above delay is
  1549FFFA jne  r10,r9,@@swap_lop             ; 00000000 +nop ;in CACHED RAM
  AC4809C4 +mov [r2+9C4h],r8                  ;
```

#### patch\_card\_info\_step4:
The "card\_info" function sends an incomplete read command to the card; in order
to receive status information. After receiving the last byte, the function does
accidently send a further byte to the card, so the card responds by another
byte (and another IRQ7), which is not processed nor acknowledged by the BIOS.
This patch kills the opcode that sends the extra byte.<br/>
Used in alone1 at 800AE214h:<br/>
```
  24090057 mov  r9,57h                        ;\
  240A00B0 mov  r10,0B0h                      ; B(57h) GetB0Table
  0140F809 call r10                           ;
  00000000 +nop                               ;/
  240A0009 mov  r10,9h        ;=blah
  8C42016C mov  r2,[r2+5Bh*4] ;=B(5Bh)
  00000000 nop
  20431988 addt r3,r2,1988h   ;=B(5Bh)+1988h  ;\store a NOP,
  0xxxxxxx call xxxxxxxxh                     ; and call ...
  AC600000 +mov [r3],0        ;=nop           ;/
```

#### patch\_pad\_error\_handling\_and\_get\_pad\_enable\_functions:
If a transmission error occurs (or if there's no controller connected), then
the Pad handler handler does usually issue a strange chip select signal to the
OTHER controller slot, and does then execute the bizarre\_pad\_delay function.
The patch below overwrites that behaviour by NOPs. Purpose of the original (and
patched) behaviour is unknown.<br/>
Used by Perfect Assassin at 800519D4h:<br/>
```
  240A00B0 mov  r10,0B0h                      ;\
  0140F809 call r10                           ; B(57h) GetB0Table
  24090057 +mov r9,57h                        ;/
  8C42016C mov  r2,[r2+5Bh*4] ;=B(5Bh)
  3C01xxxx mov  r1,xxxx0000h
  20430884 addt r3,r2,884h    ;B(5Bh)+884h
  AC23xxxx mov  [r1+xxxxh],r3 ;<--- SetPadEnableFlag()
  3C01xxxx mov  r1,xxxx0000h
  20430894 addt r3,r2,894h    ;B(5Bh)+894h
  2409000B mov  r9,0Bh        ;len
  AC23xxxx mov  [r1+xxxxh],r3 ;<--- ClearPadEnableFlag()
          @@fill_lop:                         ;\
  2529FFFF sub  r9,1h                         ;
  AC400594 mov  [r2+594h],0   ;B(5Bh)+594h..  ; erase error handling
  1520FFFD jnz  r9,@@fill_lop                 ;
  24420004 +add r2,4h                         ;/
```
Alternately, same as above, but with inefficient nops, used by Sporting Clays
at 8001B4B4h:<br/>
```
  24090057 mov  r9,57h       ;\
  240A00B0 mov  r10,0B0h     ; B(57h) GetB0Table
  0140F809 call r10          ;
  00000000 +nop              ;/
  8C42016C mov  r2,[r2+5Bh*4]
  2409000B mov  r9,0Bh ;len
  20430884 addt r3,r2,884h
  3C01xxxx mov  r1,xxxx0000h
  AC23xxxx mov  [r1+xxxxh],r3 ;<--- SetPadEnableFlag()
  20430894 addt r3,r2,894h
  3C01xxxx mov  r1,xxxx0000h
  AC23xxxx mov  [r1+xxxxh],r3 ;<--- ClearPadEnableFlag()
          @@fill_lop:         ;\
  AC400594 mov  [r2+594h],0   ;
  24420004 add  r2,4h         ; erase error handling
  2529FFFF sub  r9,1h         ;
  1520FFFC jnz  r9,@@fill_lop ;
  00000000 +nop               ;/
```
Alternately, same as above, but without getting PadEnable functions, used in
Pandemonium II (at 80083C94h and at 8010B77Ch):<br/>
```
  240A00B0 mov  r10,0B0h              ;\
  0140F809 call r10                   ; B(57h) GetB0Table
  24090057 +mov r9,57h                ;/
  8C42016C mov  r2,[r2+5Bh*4] ;=B(5Bh)
  2409000B mov  r9,0Bh        ;len            ;\
          @@fill_lop:                         ;
  2529FFFF sub  r9,1h                         ; erase error handling
  AC400594 mov  [r2+594h],0   ;B(5Bh)+594h..  ;
  1520FFFD jnz  r9,@@fill_lop                 ;
  24420004 +add r2,4h                         ;/
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
  240A00B0 mov  r10,0B0h                      ;\
  0140F809 call r10                           ; B(57h) GetB0Table
  24090057 +mov r9,57h                        ;/
  8C42016C mov  r2,[r2+5Bh*4] ;B(5Bh)
  3C0Axxxx mov  r10,xxxx0000h
  3C09xxxx mov  r9,xxxx0000h
  3C01xxxx mov  r1,xxxx0000h
  204307A0 addt r3,r2,7A0h    ;B(5Bh)+7A0h
  254Axxxx add  r10,xxxxh  ;=@@new_data
  2529xxxx add  r9,xxxxh   ;=@@new_data_end
  AC23xxxx mov  [r1-xxxxh],r3 ;<--- SetPadOutput(src1,blah1,src2,blah2)
          @@double_copy_lop:                  ;\
  8D430000 mov  r3,[r10]                      ;           @@new_data:
  254A0004 add  r10,4h                        ;   00551024 and     r2,r21
  AC4303D8 mov  [r2+3D8h],r3  ;<--- here      ;   00000000 nop
  24420004 add  r2,4h                         ;   00000000 nop
  1549FFFB jne  r10,r9,@@double_copy_lop      ;   00000000 nop
  AC4304DC +mov [r2+4DCh],r3  ;<--- here      ;/          @@new_data_end:
```
Alternately, more inefficient (with NOPs), used in Lemmings at 80036618h:<br/>
```
  24090057 mov  r9,57h                        ;\
  240A00B0 mov  r10,0B0h                      ; B(57h) GetB0Table
  0140F809 call r10                           ;
  00000000 +nop                               ;/
  3C0Axxxx mov  r10,xxxx0000h
  254Axxxx add  r10,xxxxh    ;=@@new_data
  3C09xxxx movp r9,xxxx0000h
  2529xxxx add  r9,xxxxh     ;=@@new_data_end
  8C42016C mov  r2,[r2+5Bh*4] ;B(5Bh)
  00000000 nop
  204307A0 addt r3,r2,7A0h    ;B(5Bh)+7A0h
  3C01xxxx mov  r1,xxxx0000h
  AC23xxxx mov  [r1+xxxxh],r3 ;<--- SetPadOutput(src1,blah1,src2,blah2)
          @@double_copy_lop:                  ;\
  8D430000 mov  r3,[r10]                      ;           @@new_data:
  00000000 nop                                ;   00551024 and     r2,r21
  AC4303D8 mov  [r2+3D8h],r3                  ;   00000000 nop
  AC4304E0 mov  [r2+4E0h],r3                  ;   00000000 nop
  24420004 add  r2,4h                         ;   00000000 nop
  254A0004 add  r10,4h                        ;           @@new_data_end:
  1549FFF9 jne  r10,r9,@@double_copy_lop      ;
  00000000 +nop                               ;/
```

#### patch\_no\_pad\_card\_auto\_ack:
This patch suppresses automatic IRQ0 (vblank) acknowleding in the Pad/Card IRQ
handler, that, even if auto-ack is enabled. Obviously, one could as well
disable auto-ack via B(5Bh) ChangeClearPAD(int), so this patch is total
nonsense. Used in Resident Evil 2 at 800919ACh:<br/>
```
  240A00B0 mov   r10,0B0h                      ;\
  0140F809 call  r10                           ; B(57h) GetB0Table
  24090057 +mov  r9,57h                        ;/
  8C42016C mov   r2,[r2+5Bh*4] ;=B(5Bh)
  240A0009 mov   r10,9h        ;len            ;\
  2043062C addt  r3,r2,62Ch    ;=B(5Bh)+62Ch   ;
          @@fill_lop:                          ;
  254AFFFF sub   r10,1h                        ;
  AC600000 mov   [r3],0                        ;
  1540FFFD jnz   r10,@@fill_lop                ;
  24630004 +add  r3,4h                         ;/
```
Alternately, same as above, but more inefficient, used in Sporting Clays at
8001B53Ch:<br/>
```
  24090057 mov   r9,57h                        ;\
  240A00B0 mov   r10,0B0h                      ; B(57h) GetB0Table
  0140F809 call  r10                           ;
  00000000 +nop                                ;/
  240A0009 mov   r10,9h    ;len
  8C42016C mov   r2,[r2+5Bh*4]
  00000000 nop
  2043062C addt  r3,r2,62Ch
          @@fill_lop:                          ;\
  AC600000 mov   [r3],0                        ;
  24630004 add   r3,4h                         ;
  254AFFFF sub   r10,1h                        ;
  1540FFFC jnz   r10,@@fill_lop                ;
  00000000 +nop                                ;/
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
  240A00B0 mov  r10,0B0h     ;\
  0140F809 call r10          ; B(56h) GetC0Table
  24090056 +mov r9,56h       ;/
  3C0Axxxx mov  r10,xxxx0000h ;src
  3C09xxxx mov  r9,xxxx0000h  ;src.end
  8C420018 mov  r2,[r2+06h*4] ;C(06h)
  254Axxxx add  r10,xxxxh     ;src
  2529xxxx add  r9,xxxxh      ;src.end (=src+10h)
          @@copy_lop:              ;\    ;        @@src:
  8D430000 mov  r3,[r10]           ;     ;3C02xxxx mov  r2,xxxx0000h
  254A0004 add  r10,4h             ;     ;2442xxxx add  r2,xxxxh
  24420004 add  r2,4h              ;     ;0040F809 call r2  ;lightgun_proc
  1549FFFC jne  r10,r9,@@copy_lop  ;     ;00000000 +nop
  AC43007C +mov [r2+80h-4],r3      ;/             @@src_end:
```
Alternately, same as above, but more inefficient, used in DQM (Dragon Quest
Monsters 1&2) at 80089390h (install) and 800893F8h (uninstall):<br/>
```
  24090056 mov  r9,56h        ;\
  240A00B0 mov  r10,0B0h      ; B(56h) GetC0Table
  0140F809 call r10           ;
  00000000 +nop               ;/
  8C420018 mov  r2,[r2+06h*4] ;=00000C80h = exception_handler = C(06h)
  3C0Axxxx mov  r10,xxxx0000h ;\@@new_data (3xNOP)
  254Axxxx add  r10,-xxxxh    ;/
  3C09xxxx mov  r9,xxxx0000h  ;\@@new_data_end
  2529xxxx add  r9,-xxxxh     ;/
          @@copy_lop:             ;\
  8D430000 mov  r3,[r10]          ; @@new_data: ;for (un-)install...
  00000000 nop                    ; 00000000 nop / 3C02xxxx mov r2,xxxx0000h
  AC430080 mov  [r2+80h],r3       ; 00000000 nop / 2442xxxx add r2,-xxxxh
  254A0004 add  r10,4h            ; 00000000 nop / 0040F809 call r2  ;proc
  1549FFFB jne  r10,r9,@@copy_lop ; @@new_data_end:
  24420004 +add r2,4h             ;/
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
  8C030474 mov   r3,[200h+(9Dh*4)]      ;\get ptr to A(9Dh) GetConf (done so,
  00000000 nop                          ;/as there's no "GetA0Table" funtion)
  94620000 movh  r2,[r3+0h] ;lui msw    ;\
  84630004 movhs r3,[r3+4h] ;lw lsw+8   ; extract ptr to "boot_cnf_values"
  00021400 shl   r2,10h     ;msw*10000h ; (from first 2 opcodes of GetConf)
  2442FFF8 sub   r2,8h      ;undo +8    ;
  00431021 add   r2,r3      ;lsw        ;/
  AC450000 mov   [r2+0h],r5 ;num_TCB    ;\set num_EvCB,num_TCB,stacktop
  AC440004 mov   [r2+4h],r4 ;num_EvCB   ; (unlike A(9Ch) SetConf, without
  03E00008 ret                          ; actually reallocting anything)
  AC460008 +mov  [r2+8h],r6 ;stacktop   ;/
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
