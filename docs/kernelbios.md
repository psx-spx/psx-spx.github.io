#   Kernel (BIOS)
[BIOS Overview](kernelbios.md#bios-overview)<br/>
[BIOS Memory Map](kernelbios.md#bios-memory-map)<br/>
[BIOS Function Summary](kernelbios.md#bios-function-summary)<br/>
[BIOS File Functions](kernelbios.md#bios-file-functions)<br/>
[BIOS File Execute and Flush Cache](kernelbios.md#bios-file-execute-and-flush-cache)<br/>
[BIOS CDROM Functions](kernelbios.md#bios-cdrom-functions)<br/>
[BIOS Memory Card Functions](kernelbios.md#bios-memory-card-functions)<br/>
[BIOS Interrupt/Exception Handling](kernelbios.md#bios-interruptexception-handling)<br/>
[BIOS Event Functions](kernelbios.md#bios-event-functions)<br/>
[BIOS Event Summary](kernelbios.md#bios-event-summary)<br/>
[BIOS Thread Functions](kernelbios.md#bios-thread-functions)<br/>
[BIOS Timer Functions](kernelbios.md#bios-timer-functions)<br/>
[BIOS Joypad Functions](kernelbios.md#bios-joypad-functions)<br/>
[BIOS GPU Functions](kernelbios.md#bios-gpu-functions)<br/>
[BIOS Memory Allocation](kernelbios.md#bios-memory-allocation)<br/>
[BIOS Memory Fill/Copy/Compare (SLOW)](kernelbios.md#bios-memory-fillcopycompare-slow)<br/>
[BIOS String Functions](kernelbios.md#bios-string-functions)<br/>
[BIOS Number/String/Character Conversion](kernelbios.md#bios-numberstringcharacter-conversion)<br/>
[BIOS Misc Functions](kernelbios.md#bios-misc-functions)<br/>
[BIOS Internal Boot Functions](kernelbios.md#bios-internal-boot-functions)<br/>
[BIOS More Internal Functions](kernelbios.md#bios-more-internal-functions)<br/>
[BIOS PC File Server](kernelbios.md#bios-pc-file-server)<br/>
[BIOS TTY Console (std_io)](kernelbios.md#bios-tty-console-stdio)<br/>
[BIOS Character Sets](kernelbios.md#bios-character-sets)<br/>
[BIOS Control Blocks](kernelbios.md#bios-control-blocks)<br/>
[BIOS Versions](kernelbios.md#bios-versions)<br/>
[BIOS Patches](kernelbios.md#bios-patches)<br/>



##   BIOS Overview
#### BIOS CDROM Boot
The main purpose of the BIOS is to boot games from CDROM, unfortunately, before
doing that, it displays the Sony intro. It's also doing some copy protection
and region checks, and refuses to boot unlicensed games, or illegal copies, or
games for other regions.<br/>

#### BIOS Bootmenu
The bootmenu shows up when starting the Playstation without CDROM inserted. The
menu allows to play Audio CDs, and to erase or copy game positions on Memory
Cards.<br/>

#### BIOS Functions
The BIOS contains a number of more or less useful, and probably more or less
inefficient functions that can be used by software.<br/>
No idea if it's easy to take full control of the CPU, ie. to do all hardware
access and interrupt handling by software, without using the BIOS at all?<br/>
Eventually the BIOS functions for accessing the CDROM drive are important, not
sure how complicated/compatible it'd be to access the CDROM drive directly via
I/O ports... among others, there might be different drives used in different
versions of the Playstation, which aren't fully compatible with each other?<br/>

#### BIOS Memory
The BIOS occupies 512Kbyte ROM with 8bit address bus (so the BIOS ROM is rather
slow, for faster execution, portions of it are relocated to the first 64K of
RAM). For some very strange reason, the original PSX BIOS executes all ROM
functions in uncached ROM, which is incredible slow (nocash BIOS uses cached
ROM, which does work without problems).<br/>
The first 64Kbyte of the 2Mbyte Main RAM are reserved for the BIOS (containing
exception handlers, jump tables, other data, and relocated code). That reserved
region does unfortunately include the "valuable" first 32Kbytes (valuable
because that memory could be accessed directly via [R0+immediate], without
needing to use R1..R31 as base register).<br/>



##   BIOS Memory Map
#### BIOS ROM Map (512Kbytes)
```
  BFC00000h Kernel Part 1  (code/data executed in uncached ROM)
  BFC10000h Kernel Part 2  (code/data relocated to cached RAM)
  BFC18000h Intro/Bootmenu (code/data decompressed and relocated to RAM)
  BFC64000h Character Sets
```

#### BIOS ROM Header/Footer
```
  BFC00100h Kernel BCD date  (YYYYMMDDh)
  BFC00104h Console Type     (see Port 1F802030h, Secondary IRQ10 Controller)
  BFC00108h Kernel Maker/Version Strings (separated by one or more 00h bytes)
  BFC7FF32h GUI Version/Copyright Strings (if any) (separated by one 00h byte)
```

#### BIOS RAM Map (1st 64Kbytes of RAM) (fixed addresses mainly in 1st 500h bytes)
```
  00000000h 10h    Garbage Area (see notes below)
  00000010h 30h    Unused/reserved
  00000040h 20h    COP0 debug-break vector (not used by Kernel) (in KSEG0)
  00000060h 4      RAM Size (in megabytes) (2 or 8)
  00000064h 4      Unknown (set to 00000000h)
  00000068h 4      Unknown (set to 000000FFh)
  0000006Ch 14h    Unused/reserved
  00000080h 10h    Exception vector (actually in KSEG0, ie. at 80000080h)
  00000090h 10h    Unused/reserved
  000000A0h 10h    A(nnh) Function Vector
  000000B0h 10h    B(nnh) Function Vector
  000000C0h 10h    C(nnh) Function Vector
  000000D0h 30h    Unused/reserved
  00000100h 58h    Table of Tables (BIOS Control Blocks) (see below)
  00000158h 28h    Unused/reserved
  00000180h 80h    Command line argument from SYSTEM.CNF; BOOT = fname argument
  00000200h 300h   A(nnh) Jump Table
  00000500h ...    Kernel Code/Data (relocated from ROM)
  0000Cxxxh ...    Unused/reserved
  0000DF80h 80h    Used for BIOS Patches (ie. used by games, not used by BIOS)
  0000DFFCh 4      Response value from Intro/Bootmenu
  0000E000h 2000h  Kernel Memory; ExCBs, EvCBs, and TCBs allocated via B(00h)
```

#### User Memory (not used by Kernel)
```
  00010000h ...    Begin of User RAM (Exefile, Data, Heap, Stack, etc.)
  001FFF00h ...    Default Stacktop (usually in KSEG0)
  1F800000h 400h   Scratchpad (Data-Cache mis-used as Fast RAM)
```

#### Table of Tables (see BIOS Control Blocks for details)
Each table entry consists of two 32bit values; containing the base address, and
total size (in bytes) of the corresponding control blocks.<br/>
```
  00000100h  ExCB Exception Chain Entrypoints (addr=var, size=4*08h)
  00000108h  PCB  Process Control Block       (addr=var, size=1*04h)
  00000110h  TCB  Thread Control Blocks       (addr=var, size=N*C0h)
  00000118h  -    Unused/reserved
  00000120h  EvCB Event Control Blocks        (addr=var, size=N*1Ch)
  00000128h  -    Unused/reserved
  00000130h  -    Unused/reserved
  00000138h  -    Unused/reserved
  00000140h  FCB  File Control Blocks         (addr=fixed, size=10h*2Ch)
  00000148h  -    Unused/reserved
  00000150h  DCB  Device Control Blocks       (addr=fixed, size=0Ah*50h)
```
File handles (fd=00h..0Fh) can be simply converted as fcb=[140h]+fd\*2Ch.<br/>
Event handles (event=F10000xxh) as evcb=[120h]+(event AND FFFFh)\*1Ch.<br/>

#### Garbage Area at Address 00000000h
The first some bytes of memory address 00000000h aren't actually used by the
Kernel, except for storing some garbage at that locations. However, this
garbage is actually important for bugged games like R-Types and Fade to Black
(ie. games that do read from address 00000000h due to using uninitialized
pointers).<br/>
Initially, the garbage area is containing a copy of the 16-byte exception
handler at address 80h, but the first 4-bytes are typically smashed (set to
00000003h from some useless dummy writes in some useless CDROM delays). Ie. the
16-bytes should have these values:<br/>
```
  [00000000h]=3C1A0000h  ;<-- but overwritten by 00000003h after soon
  [00000004h]=275A0C80h  ;<-- or 275A0C50h (in older BIOS)
  [00000008h]=03400008h
  [0000000Ch]=00000000h
```
For R-Types, the halfword at [0] must non-zero (else the game will do a DMA to
address 0, and thereby destroy kernel memory). Fade to Black does several
garbage reads from [0..9], a wrong byte value at [5] can cause the game to
crash with an invalid memory access exception upon memory card access.<br/>



##   BIOS Function Summary
#### Parameters, Registers, Stack
Argument(s) are passed in R4,R5,R6,R7,[SP+10h],[SP+14h],etc.<br/>
Caution: When calling a sub-function with N parameters, the caller MUST always
allocate N words on the stack, and, although the first four parameters are
passed in registers rather than on stack, the sub-function is allowed to
use/destroy these words at [SP+0..N\*4-1].<br/>
BIOS Functions (and custom callback functions) are allowed to destroy registers
R1-R15, R24-R25, R31 (RA), and HI/LO. Registers R16-R23, R29 (SP), and R30 (FP)
must be left unchanged (if the function uses that registers, then it must
push/pop them). R26 (K0) is reserved for exception handler and should be
usually not used by other functions. R27 (K1) and R28 (GP) are left more or
less unused by the BIOS, so one can more or less freely use them for whatever
purpose.<br/>
The return value (if any) is stored in R2 register.<br/>

#### A-Functions (Call 00A0h with function number in R9 Register)
```
  A(00h) or B(32h) open(filename,accessmode)
  A(01h) or B(33h) lseek(fd,offset,seektype)
  A(02h) or B(34h) read(fd,dst,length)
  A(03h) or B(35h) write(fd,src,length)
  A(04h) or B(36h) close(fd)
  A(05h) or B(37h) ioctl(fd,cmd,arg)
  A(06h) or B(38h) exit(exitcode)
  A(07h) or B(39h) isatty(fd)
  A(08h) or B(3Ah) getc(fd)
  A(09h) or B(3Bh) putc(char,fd)
  A(0Ah) todigit(char)
  A(0Bh) atof(src)     ;Does NOT work - uses (ABSENT) cop1 !!!
  A(0Ch) strtoul(src,src_end,base)
  A(0Dh) strtol(src,src_end,base)
  A(0Eh) abs(val)
  A(0Fh) labs(val)
  A(10h) atoi(src)
  A(11h) atol(src)
  A(12h) atob(src,num_dst)
  A(13h) setjmp(buf)
  A(14h) longjmp(buf,param)
  A(15h) strcat(dst,src)
  A(16h) strncat(dst,src,maxlen)
  A(17h) strcmp(str1,str2)
  A(18h) strncmp(str1,str2,maxlen)
  A(19h) strcpy(dst,src)
  A(1Ah) strncpy(dst,src,maxlen)
  A(1Bh) strlen(src)
  A(1Ch) index(src,char)
  A(1Dh) rindex(src,char)
  A(1Eh) strchr(src,char)  ;exactly the same as "index"
  A(1Fh) strrchr(src,char) ;exactly the same as "rindex"
  A(20h) strpbrk(src,list)
  A(21h) strspn(src,list)
  A(22h) strcspn(src,list)
  A(23h) strtok(src,list)  ;use strtok(0,list) in further calls
  A(24h) strstr(str,substr)       ;Bugged
  A(25h) toupper(char)
  A(26h) tolower(char)
  A(27h) bcopy(src,dst,len)
  A(28h) bzero(dst,len)
  A(29h) bcmp(ptr1,ptr2,len)      ;Bugged
  A(2Ah) memcpy(dst,src,len)
  A(2Bh) memset(dst,fillbyte,len)
  A(2Ch) memmove(dst,src,len)     ;Bugged
  A(2Dh) memcmp(src1,src2,len)    ;Bugged
  A(2Eh) memchr(src,scanbyte,len)
  A(2Fh) rand()
  A(30h) srand(seed)
  A(31h) qsort(base,nel,width,callback)
  A(32h) strtod(src,src_end) ;Does NOT work - uses (ABSENT) cop1 !!!
  A(33h) malloc(size)
  A(34h) free(buf)
  A(35h) lsearch(key,base,nel,width,callback)
  A(36h) bsearch(key,base,nel,width,callback)
  A(37h) calloc(sizx,sizy)            ;SLOW!
  A(38h) realloc(old_buf,new_siz)     ;SLOW!
  A(39h) InitHeap(addr,size)
  A(3Ah) _exit(exitcode)
  A(3Bh) or B(3Ch) getchar()
  A(3Ch) or B(3Dh) putchar(char)
  A(3Dh) or B(3Eh) gets(dst)
  A(3Eh) or B(3Fh) puts(src)
  A(3Fh) printf(txt,param1,param2,etc.)
  A(40h) SystemErrorUnresolvedException()
  A(41h) LoadTest(filename,headerbuf)
  A(42h) Load(filename,headerbuf)
  A(43h) Exec(headerbuf,param1,param2)
  A(44h) FlushCache()
  A(45h) init_a0_b0_c0_vectors
  A(46h) GPU_dw(Xdst,Ydst,Xsiz,Ysiz,src)
  A(47h) gpu_send_dma(Xdst,Ydst,Xsiz,Ysiz,src)
  A(48h) SendGP1Command(gp1cmd)
  A(49h) GPU_cw(gp0cmd)   ;send GP0 command word
  A(4Ah) GPU_cwp(src,num) ;send GP0 command word and parameter words
  A(4Bh) send_gpu_linked_list(src)
  A(4Ch) gpu_abort_dma()
  A(4Dh) GetGPUStatus()
  A(4Eh) gpu_sync()
  A(4Fh) SystemError
  A(50h) SystemError
  A(51h) LoadExec(filename,stackbase,stackoffset)
  A(52h) GetSysSp
  A(53h) SystemError           ;PS2: set_ioabort_handler(src)
  A(54h) or A(71h) _96_init()
  A(55h) or A(70h) _bu_init()
  A(56h) or A(72h) _96_remove()  ;does NOT work due to SysDeqIntRP bug
  A(57h) return 0
  A(58h) return 0
  A(59h) return 0
  A(5Ah) return 0
  A(5Bh) dev_tty_init()                                      ;PS2: SystemError
  A(5Ch) dev_tty_open(fcb,and unused:"path\name",accessmode) ;PS2: SystemError
  A(5Dh) dev_tty_in_out(fcb,cmd)                             ;PS2: SystemError
  A(5Eh) dev_tty_ioctl(fcb,cmd,arg)                          ;PS2: SystemError
  A(5Fh) dev_cd_open(fcb,"path\name",accessmode)
  A(60h) dev_cd_read(fcb,dst,len)
  A(61h) dev_cd_close(fcb)
  A(62h) dev_cd_firstfile(fcb,"path\name",direntry)
  A(63h) dev_cd_nextfile(fcb,direntry)
  A(64h) dev_cd_chdir(fcb,"path")
  A(65h) dev_card_open(fcb,"path\name",accessmode)
  A(66h) dev_card_read(fcb,dst,len)
  A(67h) dev_card_write(fcb,src,len)
  A(68h) dev_card_close(fcb)
  A(69h) dev_card_firstfile(fcb,"path\name",direntry)
  A(6Ah) dev_card_nextfile(fcb,direntry)
  A(6Bh) dev_card_erase(fcb,"path\name")
  A(6Ch) dev_card_undelete(fcb,"path\name")
  A(6Dh) dev_card_format(fcb)
  A(6Eh) dev_card_rename(fcb1,"path\name1",fcb2,"path\name2")
  A(6Fh) ?   ;card ;[r4+18h]=00000000h  ;card_clear_error(fcb) or so
  A(70h) or A(55h) _bu_init()
  A(71h) or A(54h) _96_init()
  A(72h) or A(56h) _96_remove()   ;does NOT work due to SysDeqIntRP bug
  A(73h) return 0
  A(74h) return 0
  A(75h) return 0
  A(76h) return 0
  A(77h) return 0
  A(78h) CdAsyncSeekL(src)
  A(79h) return 0               ;DTL-H: Unknown?
  A(7Ah) return 0               ;DTL-H: Unknown?
  A(7Bh) return 0               ;DTL-H: Unknown?
  A(7Ch) CdAsyncGetStatus(dst)
  A(7Dh) return 0               ;DTL-H: Unknown?
  A(7Eh) CdAsyncReadSector(count,dst,mode)
  A(7Fh) return 0               ;DTL-H: Unknown?
  A(80h) return 0               ;DTL-H: Unknown?
  A(81h) CdAsyncSetMode(mode)
  A(82h) return 0               ;DTL-H: Unknown?
  A(83h) return 0               ;DTL-H: Unknown?
  A(84h) return 0               ;DTL-H: Unknown?
  A(85h) return 0               ;DTL-H: Unknown?, or reportedly, CdStop (?)
  A(86h) return 0               ;DTL-H: Unknown?
  A(87h) return 0               ;DTL-H: Unknown?
  A(88h) return 0               ;DTL-H: Unknown?
  A(89h) return 0               ;DTL-H: Unknown?
  A(8Ah) return 0               ;DTL-H: Unknown?
  A(8Bh) return 0               ;DTL-H: Unknown?
  A(8Ch) return 0               ;DTL-H: Unknown?
  A(8Dh) return 0               ;DTL-H: Unknown?
  A(8Eh) return 0               ;DTL-H: Unknown?
  A(8Fh) return 0               ;DTL-H: Unknown?
  A(90h) CdromIoIrqFunc1()
  A(91h) CdromDmaIrqFunc1()
  A(92h) CdromIoIrqFunc2()
  A(93h) CdromDmaIrqFunc2()
  A(94h) CdromGetInt5errCode(dst1,dst2)
  A(95h) CdInitSubFunc()
  A(96h) AddCDROMDevice()
  A(97h) AddMemCardDevice()     ;DTL-H: SystemError
  A(98h) AddDuartTtyDevice()    ;DTL-H: AddAdconsTtyDevice ;PS2: SystemError
  A(99h) add_nullcon_driver()
  A(9Ah) SystemError            ;DTL-H: AddMessageWindowDevice
  A(9Bh) SystemError            ;DTL-H: AddCdromSimDevice
  A(9Ch) SetConf(num_EvCB,num_TCB,stacktop)
  A(9Dh) GetConf(num_EvCB_dst,num_TCB_dst,stacktop_dst)
  A(9Eh) SetCdromIrqAutoAbort(type,flag)
  A(9Fh) SetMem(megabytes)
```
Below functions A(A0h..B4h) not supported on pre-retail DTL-H2000 devboard:<br/>
```
  A(A0h) _boot()
  A(A1h) SystemError(type,errorcode)
  A(A2h) EnqueueCdIntr()  ;with prio=0 (fixed)
  A(A3h) DequeueCdIntr()  ;does NOT work due to SysDeqIntRP bug
  A(A4h) CdGetLbn(filename) ;get 1st sector number (or garbage when not found)
  A(A5h) CdReadSector(count,sector,buffer)
  A(A6h) CdGetStatus()
  A(A7h) bufs_cb_0()
  A(A8h) bufs_cb_1()
  A(A9h) bufs_cb_2()
  A(AAh) bufs_cb_3()
  A(ABh) _card_info(port)
  A(ACh) _card_load(port)
  A(ADh) _card_auto(flag)
  A(AEh) bufs_cb_4()
  A(AFh) card_write_test(port)  ;CEX-1000: jump_to_00000000h
  A(B0h) return 0               ;CEX-1000: jump_to_00000000h
  A(B1h) return 0               ;CEX-1000: jump_to_00000000h
  A(B2h) ioabort_raw(param)     ;CEX-1000: jump_to_00000000h
  A(B3h) return 0               ;CEX-1000: jump_to_00000000h
  A(B4h) GetSystemInfo(index)   ;CEX-1000: jump_to_00000000h
  A(B5h..BFh) N/A ;jump_to_00000000h
```

#### B-Functions (Call 00B0h with function number in R9 Register)
```
  B(00h) alloc_kernel_memory(size)
  B(01h) free_kernel_memory(buf)
  B(02h) init_timer(t,reload,flags)
  B(03h) get_timer(t)
  B(04h) enable_timer_irq(t)
  B(05h) disable_timer_irq(t)
  B(06h) restart_timer(t)
  B(07h) DeliverEvent(class, spec)
  B(08h) OpenEvent(class,spec,mode,func)
  B(09h) CloseEvent(event)
  B(0Ah) WaitEvent(event)
  B(0Bh) TestEvent(event)
  B(0Ch) EnableEvent(event)
  B(0Dh) DisableEvent(event)
  B(0Eh) OpenTh(reg_PC,reg_SP_FP,reg_GP)
  B(0Fh) CloseTh(handle)
  B(10h) ChangeTh(handle)
  B(11h) jump_to_00000000h
  B(12h) InitPAD2(buf1,siz1,buf2,siz2)
  B(13h) StartPAD2()
  B(14h) StopPAD2()
  B(15h) PAD_init2(type,button_dest,unused,unused)
  B(16h) PAD_dr()
  B(17h) ReturnFromException()
  B(18h) ResetEntryInt()
  B(19h) HookEntryInt(addr)
  B(1Ah) SystemError  ;PS2: return 0
  B(1Bh) SystemError  ;PS2: return 0
  B(1Ch) SystemError  ;PS2: return 0
  B(1Dh) SystemError  ;PS2: return 0
  B(1Eh) SystemError  ;PS2: return 0
  B(1Fh) SystemError  ;PS2: return 0
  B(20h) UnDeliverEvent(class,spec)
  B(21h) SystemError  ;PS2: return 0
  B(22h) SystemError  ;PS2: return 0
  B(23h) SystemError  ;PS2: return 0
  B(24h) jump_to_00000000h
  B(25h) jump_to_00000000h
  B(26h) jump_to_00000000h
  B(27h) jump_to_00000000h
  B(28h) jump_to_00000000h
  B(29h) jump_to_00000000h
  B(2Ah) SystemError  ;PS2: return 0
  B(2Bh) SystemError  ;PS2: return 0
  B(2Ch) jump_to_00000000h
  B(2Dh) jump_to_00000000h
  B(2Eh) jump_to_00000000h
  B(2Fh) jump_to_00000000h
  B(30h) jump_to_00000000h
  B(31h) jump_to_00000000h
  B(32h) or A(00h) open(filename,accessmode)
  B(33h) or A(01h) lseek(fd,offset,seektype)
  B(34h) or A(02h) read(fd,dst,length)
  B(35h) or A(03h) write(fd,src,length)
  B(36h) or A(04h) close(fd)
  B(37h) or A(05h) ioctl(fd,cmd,arg)
  B(38h) or A(06h) exit(exitcode)
  B(39h) or A(07h) isatty(fd)
  B(3Ah) or A(08h) getc(fd)
  B(3Bh) or A(09h) putc(char,fd)
  B(3Ch) or A(3Bh) getchar()
  B(3Dh) or A(3Ch) putchar(char)
  B(3Eh) or A(3Dh) gets(dst)
  B(3Fh) or A(3Eh) puts(src)
  B(40h) cd(name)
  B(41h) format(devicename)
  B(42h) firstfile2(filename,direntry)
  B(43h) nextfile(direntry)
  B(44h) rename(old_filename,new_filename)
  B(45h) erase(filename)
  B(46h) undelete(filename)
  B(47h) AddDrv(device_info)  ;subfunction for AddXxxDevice functions
  B(48h) DelDrv(device_name_lowercase)
  B(49h) PrintInstalledDevices()
```
Below functions B(4Ah..5Dh) not supported on pre-retail DTL-H2000 devboard:<br/>
```
  B(4Ah) InitCARD2(pad_enable)  ;uses/destroys k0/k1 !!!
  B(4Bh) StartCARD2()
  B(4Ch) StopCARD2()
  B(4Dh) _card_info_subfunc(port)  ;subfunction for "_card_info"
  B(4Eh) _card_write(port,sector,src)
  B(4Fh) _card_read(port,sector,dst)
  B(50h) _new_card()
  B(51h) Krom2RawAdd(shiftjis_code)
  B(52h) SystemError  ;PS2: return 0
  B(53h) Krom2Offset(shiftjis_code)
  B(54h) _get_errno()
  B(55h) _get_error(fd)
  B(56h) GetC0Table
  B(57h) GetB0Table
  B(58h) _card_chan()
  B(59h) testdevice(devicename)
  B(5Ah) SystemError  ;PS2: return 0
  B(5Bh) ChangeClearPAD(int)
  B(5Ch) _card_status(slot)
  B(5Dh) _card_wait(slot)
  B(5Eh..FFh) N/A ;jump_to_00000000h    ;CEX-1000: B(5Eh..F6h) only
  B(100h....) N/A ;garbage              ;CEX-1000: B(F7h.....) and up
```

#### C-Functions (Call 00C0h with function number in R9 Register)
```
  C(00h) EnqueueTimerAndVblankIrqs(priority) ;used with prio=1
  C(01h) EnqueueSyscallHandler(priority)     ;used with prio=0
  C(02h) SysEnqIntRP(priority,struc)  ;bugged, use with care
  C(03h) SysDeqIntRP(priority,struc)  ;bugged, use with care
  C(04h) get_free_EvCB_slot()
  C(05h) get_free_TCB_slot()
  C(06h) ExceptionHandler()
  C(07h) InstallExceptionHandlers()  ;destroys/uses k0/k1
  C(08h) SysInitMemory(addr,size)
  C(09h) SysInitKernelVariables()
  C(0Ah) ChangeClearRCnt(t,flag)
  C(0Bh) SystemError  ;PS2: return 0
  C(0Ch) InitDefInt(priority) ;used with prio=3
  C(0Dh) SetIrqAutoAck(irq,flag)
  C(0Eh) return 0               ;DTL-H2000: dev_sio_init
  C(0Fh) return 0               ;DTL-H2000: dev_sio_open
  C(10h) return 0               ;DTL-H2000: dev_sio_in_out
  C(11h) return 0               ;DTL-H2000: dev_sio_ioctl
  C(12h) InstallDevices(ttyflag)
  C(13h) FlushStdInOutPut()
  C(14h) return 0               ;DTL-H2000: SystemError
  C(15h) _cdevinput(circ,char)
  C(16h) _cdevscan()
  C(17h) _circgetc(circ)    ;uses r5 as garbage txt for _ioabort
  C(18h) _circputc(char,circ)
  C(19h) _ioabort(txt1,txt2)
  C(1Ah) set_card_find_mode(mode)  ;0=normal, 1=find deleted files
  C(1Bh) KernelRedirect(ttyflag)   ;PS2: ttyflag=1 causes SystemError
  C(1Ch) AdjustA0Table()
  C(1Dh) get_card_find_mode()
  C(1Eh..7Fh) N/A ;jump_to_00000000h
  C(80h.....) N/A ;mirrors to B(00h.....)
```

#### SYS-Functions (Syscall opcode with function number in R4 aka A0 Register)
```
  SYS(00h) NoFunction()
  SYS(01h) EnterCriticalSection()
  SYS(02h) ExitCriticalSection()
  SYS(03h) ChangeThreadSubFunction(addr) ;syscall with r4=03h, r5=addr
  SYS(04h..FFFFFFFFh) calls DeliverEvent(F0000010h,4000h)
```
The 20bit immediate in the "syscall imm" opcode is unused (should be zero).<br/>

#### BREAK-Functions (Break opcode with function number in opcode's immediate)
BRK opcodes may be used within devkits, however, the standard BIOS simply calls
DeliverEvent(F0000010h,1000h) and SystemError\_A\_40h upon any BRK opcodes (as
well as on any other unresolved exceptions).<br/>
```
  BRK(1C00h) Division by zero (commonly checked/invoked by software)
  BRK(1800h) Division overflow (-80000000h/-1, sometimes checked by software)
```
Below breaks are used in DTL-H2000 BIOS:<br/>
```
  BRK(1h) Whatever lockup or so?
  BRK(101h) PCInit()   Inits the fileserver.
  BRK(102h) PCCreat(filename, fileattributes)
  BRK(103h) PCOpen(filename, accessmode)
  BRK(104h) PCClose(filehandle)
  BRK(105h) PCRead(filehandle, length, memory_destination_address)
  BRK(106h) PCWrite(filehandle, length, memory_source_address)
  BRK(107h) PClSeek(filehandle, file_offset, seekmode)
  BRK(3C400h) User has typed "break" command in debug console
```
The break functions have argument(s) in A1,A2,A3 (ie. unlike normal BIOS
functions not in A0,A1,A2), and TWO return values (in R2, and R3). These
functions require a commercial/homebrew devkit... consisting of a Data Cable
(for accessing the PC's harddisk)... and an Expansion ROM (for handling the
BREAK opcodes)... or so?<br/>



##   BIOS File Functions
#### A(00h) or B(32h) - open(filename, accessmode) - Opens a file for IO
```
  out: V0  File handle (00h..0Fh), or -1 if error.
```
Opens a file on the target device for io. Accessmode is set like this:<br/>
```
  bit0     1=Read  ;\These bits aren't actually used by the BIOS, however, at
  bit1     1=Write ;/least 1 should be set; won't work when all 32bits are zero
  bit2     1=Exit without waiting for incoming data (when TTY buffer empty)
  bit9     0=Open Existing File, 1=Create New file (memory card only)
  bit15    1=Asynchronous mode (memory card only; don't wait for completion)
  bit16-31 Number of memory card blocks for a new file on the memory card
```
The PSX can have a maximum of 16 files open at any time, of which, 2 handles
are always reserved for std\_io, so only 14 handles are available for actual
files. Some functions (cd, testdevice, erase, undelete,
format, firstfile2, rename) are temporarily allocating 1 filehandle
(rename tries to use 2 filehandles, but, it does accidently use only 1
handle, too). So, for example, erase would fail if more than 13 file
handles are opened by the game.<br/>

#### A(01h) or B(33h) - lseek(fd, offset, seektype) - Move the file pointer
```
   seektype 0 = from start of file        (with positive offset)
            1 = from current file pointer (with positive/negative offset)
            2 = Bugs. Should be from end of file.
```
Moves the file pointer the number of bytes in A1, relative to the location
specified by A2. Movement from the eof is incorrect. Also, movement beyond the
end of the file is not checked.<br/>

#### A(02h) or B(34h) - read(fd, dst, length) - Read data from an open file
```
  out: V0  Number of bytes actually read, -1 if failed.
```
Reads the number of bytes from the specified open file. If length is not
specified an error is returned. Read per $0080 bytes from memory card (bu:) and
per $0800 from cdrom (cdrom:).<br/>

#### A(03h) or B(35h) - write(fd, src, length) - Write data to an open file
```
  out: V0  Number of bytes written.
```
Writes the number of bytes to the specified open file. Write to the memory card
per $0080 bytes. Writing to the cdrom returns 0.<br/>

#### A(04h) or B(36h) - close(fd) - Close an open file
Returns r2=fd (or r2=-1 if failed).<br/>

#### A(08h) or B(3Ah) - getc(fd) - read one byte from file
```
  out: R2=character (sign-expanded) or FFFFFFFFh=error
```
Internally redirects to "read(fd,tempbuf,1)". For some strange reason, the
returned character is sign-expanded; so, a return value of FFFFFFFFh could mean
either character FFh, or error.<br/>

#### A(09h) or B(3Bh) - putc(char,fd) - write one byte to file
Observe that "fd" is the 2nd paramter (not the 1st paramter as usually).<br/>
```
  out:  R2=Number of bytes actually written, -1 if failed
```
Internally redirects to "write(fd,tempbuf,1)".<br/>

#### B(40h) - cd(name) - Change the current directory on target device
Changes the current directory on the specified device, which should be "cdrom:"
(memory cards don't support directories). The PSX supports only a current
directory, but NOT a current device (ie. after cd, the directory name may be
ommited from filenames, but the device name must be still included in all
filenames).<br/>
```
  in:  A0  Pointer to new directory path (eg. "cdrom:\path")
```
Returns 1=okay, or 0=failed.<br/>
The function doesn't verify if the directory exists. Caution: For cdrom, the
function does always load the path table from the disk (even if it was already
stored in RAM, so cd is causing useless SLOW read/seek delays).<br/>

#### B(42h) - firstfile2(filename,direntry) - Find first file to match the name
Returns r2=direntry (or r2=0 if no matching files).<br/>
Searches for the first file to match the specified filename; the filename may
contain "?" and "\*" wildcards. "\*" means to ignore ALL following characters;
accordingly one cannot specify any further characters after the "\*" (eg.
"DATA\*" would work, but "\*.DAT" won't work). "?" is meant to ignore a single
character cell. Note: The "?" wildcards (but not "\*") can be used also in all
other file functions; causing the function to use the first matching name (eg.
erase "????" would erase the first matching file, not all matching files).<br/>
Start the name with the device you want to address. (ie. pcdrv:) Different
drives can be accessed as normally by their drive names (a:, c:, huh?) if path
is omitted after the device, the current directory will be used.<br/>
A direntry structure looks like this:<br/>
```
  00h 14h Filename, terminated with 00h
  14h 4   File attribute (always 0 for cdrom) (50h=norm or A0h=del for card)
  18h 4   File size
  1Ch 4   Pointer to next direntry? (not used?)
  20h 4   First Sector Number
  24h 4   Reserved (not used)
```
BUG: If "?" matches the ending 00h byte of a name, then any further characters
in the search expression are ignored (eg. "FILE?.DAT" would match to
"FILE2.DAT", but accidently also to "FILE").<br/>
BUG: For CDROM, the BIOS includes some code that is intended to realize disk
changes during firstfile2/nextfile operations, however, that code is so bugged
that it does rather ensure that the BIOS does NOT realize new disks being
inserted during firstfile2/nextfile.<br/>
BUG: firstfile2/nextfile is internally using a FCB. On the first call to
firstfile2, the BIOS is searching a free FCB, and does apply that as "search
fcb", but it doesn't mark that FCB as allocated, so other file functions may
accidently use the same FCB. Moreover, the BIOS does memorize that "search
fcb", and, even when starting a new search via another call to firstfile2, it
keeps using that FCB for search (without checking if the FCB is still free). A
possible workaround is not to have any files opened during firstfile2/nextfile
operations.<br/>

#### B(43h) - nextfile(direntry) - Searches for the next file to match the name
Returns r2=direntry (or r2=0 if no more matching files).<br/>
Uses the settings of a previous firstfile2/nextfile command.<br/>

#### B(44h) - rename(old\_filename, new\_filename)
Returns 1=okay, or 0=failed.<br/>

#### B(45h) - erase(filename) - Delete a file on target device
Returns 1=okay, or 0=failed.<br/>

#### B(46h) - undelete(filename)
Returns 1=okay, or 0=failed.<br/>

#### B(41h) - format(devicename)
Erases all files on the device (ie. for formatting memory cards).<br/>
Returns 1=okay, or 0=failed.<br/>

#### B(54h) - \_get\_errno()
Indicates the reason of the most recent file function error (open,
lseek, read, write, close, _get_error, ioctl, cd,
testdevice, erase, undelete, format, rename). Use
_get_errno() ONLY if an error has occured (the error code isn't reset to zero
by functions that are passing okay). firstfile2/nextfile do NOT affect
_get_errno(). See below list of File Error Numbers for more info.<br/>

#### B(55h) - \_get\_error(fd)
Basically same as B(54h), but allowing to specify a file handle for which error
information is to be received; accordingly it doesn't work for functions that
do use 'hidden' internal file handles (eg. erase, or unsuccessful
open). Returns FCB[18h], or FFFFFFFFh if the handle is invalid/unused.<br/>

#### A(05h) or B(37h) - ioctl(fd,cmd,arg)
Used only for TTY.<br/>

#### A(07h) or B(39h) - isatty(fd)
Returns bit1 of the file's DCB flags. That bit is set only for Duart/TTY, and
is cleared for Dummy/TTY, Memory Card, and CDROM.<br/>

#### B(59h) - testdevice(devicename)
Whatever. Checks the devicename, and if it's accepted, calls a device specific
function. For the existing devices (cdrom,bu,tty) that specific function simply
returns without doing anything. Maybe other devices (like printers or modems)
would do something more interesting.<br/>

#### File Error Numbers for B(54h) and B(55h)
```
  00h okay (though many successful functions leave old error code unchanged)
  02h file not found
  06h bad device port number (tty2 and up)
  09h invalid or unused file handle
  10h general error (physical I/O error, unformatted, disk changed for old fcb)
  11h file already exists error (create/undelete/rename)
  12h tried to rename a file from one device to another device
  13h unknown device name
  16h sector alignment error, or fpos>=filesize, unknown seektype or ioctl cmd
  18h not enough free file handles
  1Ch not enough free memory card blocks
  FFFFFFFFh invalid or unused file handle passed to B(55h) function
```



##   BIOS File Execute and Flush Cache
#### A(41h) - LoadTest(filename, headerbuf)
Loads the 800h-byte exe file header to an internal sector buffer, and does then
copy bytes [10h..4Bh] of that header to headerbuf[00h..3Bh].<br/>

#### A(42h) - Load(filename, headerbuf)
Same as LoadTest (see there for details), but additionally loads the body
of the executable (using the size and destination address in the file header),
and does call FlushCache. The exe can be then started via Exec (this isn't
done automatically by LoadTest). Unlike "LoadExec", the
"LoadTest/Exec" combination allows to return the new exe file to return
to the old exe file (instead of restarting the boot executable).<br/>
BUG: Uses the unstable FlushCache function (see there for details).<br/>

#### A(43h) - Exec(headerbuf, param1, param2)
Can be used to start a previously loaded executable. The function saves
R16,R28,R30,SP,RA in the reserved region of headerbuf (rather than on stack),
more or less slowly zerofills the memfill region specified in headerbuf, reads
the stack base and offset values and sets SP and FP to base+offset (or leaves
them unchanged if base=0), reads the GP value from headerbuf and sets GP to
that value. Then calls the excecutables entrypoint, with param1 and param2
passed in r4,r5.<br/>
If the executable (should) return, then R16,R28,R30,SP,RA are restored from
headerbuf, and the function returns with r2=1.<br/>

#### A(51h) - LoadExec(filename, stackbase, stackoffset)
This is a rather bizarre function. In short, it does load and execute the
specified file, and thereafter, it (tries to) reload and restart to boot
executable.<br/>
Part1: Takes a copy of the filename, with some adjustments: Everything up to
the first ":" or 00h byte is copied as is (ie. the device name, if it does
exist, or otherwise the whole path\filename.ext;ver), the remaining characters
are copied and converted to uppercase (ie. the path\filename.ext;ver part, or
none if the device name didn't exist), finally, checks if a ";" exists (ie. the
version suffix), if there's none, then it appends ";1" as default version.
CAUTION: The BIOS allocates ONLY 28 bytes on stack for the copy of the
filename, that region is followed by 4 unused bytes, so the maximum length
would be 32 bytes (31 characters plus EOL) (eg.
"device:\pathname\filename.ext;1",00h).<br/>
Part2: Enables IRQs via ExitCriticalSection, memorizes the stack base/offset
values from the previously loaded executable (which should have been the boot
executable, unless LoadExec should have been used in nested fashion),
does then use LoadTest to load the desired file, replaces the stack
base/offset values in its headerbuf by the LoadExec parameter values, and
does then execute it via Exec(headerbuf,1,0).<br/>
Part3: If the exefile returns, or if it couldn't be loaded, then the boot file
is (unsuccessfully) attempted to be reloaded: Enables IRQs via
ExitCriticalSection, loads the boot file via LoadTest, replaces the stack
base/offset values in its headerbuf by the values memorized in Part2 (which
\<should\> be the boot executable's values from SYSTEM.CNF, unless the
nesting stuff occurred), and does then execute the boot file via
Exec(headerbuf,1,0).<br/>
Part4: If the boot file returns, or if it couldn't be loaded, then the function
looks up in a "JMP $" endless loop (normally, returning from the boot exe
causes SystemError("B",38Ch), however, after using
LoadExec, this functionality is replaced by the "JMP $" lockup.<br/>
BUG: Uses the unstable FlushCache function (see there for details).<br/>
BUG: Part3 accidently treats the first 4 characters of the exename as memory
address (causing an invalid memory address exception on address 6F726463h, for
"cdrom:filename.exe").<br/>

#### A(9Ch) - SetConf(num\_EvCB, num\_TCB, stacktop)
Changes the number of EvCBs and TCBs, and the stacktop. These values are usually
initialized from the settings in the SYSTEM.CNF file, so using this function
usually shouldn't ever be required.<br/>
The function deallocates all old ExCBs, EvCBs, TCBs (so all Exception handlers,
Events, and Threads (except the current one) are lost, and all other memory
that may have been allocated via alloc\_kernel\_memory(size) is deallocated, too.
It does then allocate the new control blocks, and enqueue the default handlers.
Despite of the changed stacktop, the current stack pointer is kept intact, and
the function returns to the caller.<br/>

#### A(9Dh) - GetConf(num\_EvCB\_dst, num\_TCB\_dst, stacktop\_dst)
Returns the number of EvCBs, TCBs, and the initial stacktop. There's no return
value in the R2 register, instead, the three 32bit return values are stored at
the specified "dst" addresses.<br/>

#### A(44h) - FlushCache()
Flushes the Code Cache, so opcodes are ensured to be loaded from RAM. This is
required when loading program code via DMA (ie. from CDROM) (the cache
controller apparently doesn't realize changes to RAM that are caused by DMA).
The LoadTest and LoadExec functions are automatically calling
FlushCache (so FlushCache is required only when loading program code via
"read" or via "CdReadSector").<br/>
FlushCache may be also required when relocating or modifying program code by
software (the cache controller doesn't seem to realize modifications to memory
mirrors, eg. patching the exception handler at 80000080h seems to be work
without FlushCache, but patching the same bytes at 00000080h doesn't).<br/>
Note: The PSX doesn't have a Data Cache (or actually, it has, but it's misused
as Fast RAM, mapped to a fixed memory region, and which isn't accessable by
DMA), so FlushCache isn't required for regions that contain data.<br/>
BUG: The FlushCache function contains a handful of opcodes that do use the k0
register without having IRQs disabled at that time, if an IRQ occurs during
those opcodes, then the k0 value gets destroyed by the exception handler,
causing FlushCache to get trapped in an endless loop.<br/>
One workaround would be to disable all IRQs before calling FlushCache, however,
the BIOS does internally call the function without IRQs disabled, that applies
to:<br/>
```
  load_file  A(42h)
  load_exec  A(51h)
  add_device B(47h) (and all "add_xxx_device" functions)
  init_card  B(4Ah)
  and by intro/boot code
```
for load\_file/load\_exec, IRQ2 (cdrom) and IRQ3 (dma) need to be enabled, so the
"disable all IRQs" workaround cannot be used for that functions, however, one
can/should disable as many IRQs as possible, ie. everything except IRQ2/IRQ3,
and all DMA interrupts except DMA3 (cdrom).<br/>

#### Executable Memory Allocation
LoadTest and LoadExec are simply loading the file to the address
specified in the exe file header. There's absolutely no verification whether
that memory is (or isn't) allocated via malloc, or if it is used by the boot
executable, or by the kernel, or if it does contain RAM at all.<br/>
When using the "malloc" function combined with loading exe files, it may be
recommended not to pass all memory to InitHeap (ie. to keep a memory region
being reserved for loading executables).<br/>

#### Note
For more info about EXE files and their headers, see<br/>
[CDROM File Formats](cdromdrive.md#cdrom-file-formats)<br/>



##   BIOS CDROM Functions
#### General File Functions
CDROMs are basically accessed via normal file functions, with device name
"cdrom:" (which is an abbreviation for "cdrom0:", anyways, the port number is
ignored).<br/>
[BIOS File Functions](kernelbios.md#bios-file-functions)<br/>
[BIOS File Execute and Flush Cache](kernelbios.md#bios-file-execute-and-flush-cache)<br/>
Before starting the boot executable, the BIOS automatically calls _96_init(), so
the game doesn't need to do any initializations before using CDROM file
functions.<br/>

#### Absent CD-Audio Support
The Kernel doesn't include any functions for playing Audio tracks. Also,
there's no BIOS function for setting the XA-ADPCM file/channel filter values.
So CD Audio can be used only by directly programming the CDROM I/O ports.<br/>

#### Asynchronous CDROM Access
The normal File functions are always using synchroneous access for CDROM (ie.
the functions do wait until all data is transferred) (unlike as for memory
cards, accessmode.bit15 cannot be used to activate asynchronous cdrom access).<br/>
However, one can read files in asynchrouneous fashion via CdGetLbn,
CdAsyncSeekL, and CdAsyncReadSector. CDROM files are non-fragmented, so they
can be read simply from incrementing sector numbers.<br/>

#### A(A4h) - CdGetLbn(filename)
Returns the first sector number used by the file, or -1 in case of error.<br/>
BUG: The function accidently returns -1 for the first file in the directory
(the first file should be a dummy entry for the current or parent directory or
so, so that bug isn't much of a problem), if the file is not found, then the
function accidently returns garbage (rather than -1).<br/>

#### A(A5h) - CdReadSector(count,sector,buffer)
Reads \<count\> sectors, starting at \<sector\>, and writes data to
\<buffer\>. The read is done in mode=80h (double speed, 800h-bytes per
sector). The function waits until all sectors are transferred, and does then
return the number of sectors (ie. count), or -1 in case of error.<br/>

#### A(A6h) - CdGetStatus()
Retrieves the cdrom status via CdAsyncGetStatus(dst) (see there for details;
especially for cautions on door-open flag). The function waits until the event
indicates completion, and does then return the status byte (or -1 in case of
error).<br/>

#### A(78h) - CdAsyncSeekL(src)
Issues Setloc and SeekL commands. The parameter (src) is a pointer to a 3-byte
sector number (MM,SS,FF) (in BCD format).<br/>
The function returns 0=failed, or 1=okay. Completion is indicated by events
(class=F0000003h, and spec=20h, or 8000h).<br/>

#### A(7Ch) - CdAsyncGetStatus(dst)
Issues a GetStat command. The parameter (dst) is a pointer to a 1-byte location
that receives the status response byte.<br/>
The function returns 0=failed, or 1=okay. Completion is indicated by events
(class=F0000003h, and spec=20h, or 8000h).<br/>
Caution: The command acknowledges the door-open flag, but doesn't automatically
reload the path table (which is required if a new disk is inserted); if the
door-open flag was set, one should call a function that does forcefully load
the path table (like cd).<br/>

#### A(7Eh) - CdAsyncReadSector(count,dst,mode)
Issues SetMode and ReadN (when mode.bit8=0), or ReadS (when mode.bit8=1)
commands. count is the number of sectors to be read, dst is the destination
address in RAM, mode.bit0-7 are passed as parameter to the SetMode command,
mode.bit8 is the ReadN/ReadS flag (as described above). The sector size (for
DMA) depends on the mode value: 918h-bytes (bit4=1, bit5=X), 924h-bytes
(bit4=0, bit5=1), or 800h-bytes (bit4,5=0).<br/>
Before CdAsyncReadSector, the sector number should be set via
CdAsyncSeekL(src).<br/>
The function returns 0=failed, or 1=okay. Completion is indicated by events
(class=F0000003h, and spec=20h, 80h, or 8000h).<br/>

#### A(81h) - CdAsyncSetMode(mode)
Similar to CdAsyncReadSector (see there for details), but issues only the
SetMode command, without any following ReadN/ReadS command.<br/>

#### A(94h) - CdromGetInt5errCode(dst1,dst2)
Returns the first two response bytes from the most recent INT5 error:
[dst1]=status, [dst2]=errorcode. The BIOS doesn't reset these values in case of
successful completion, so the values are quite useless.<br/>

#### A(54h) or A(71h) - \_96\_init()
#### A(56h) or A(72h) - \_96\_remove()  ;does NOT work due to SysDeqIntRP bug
#### A(90h) - CdromIoIrqFunc1()
#### A(91h) - CdromDmaIrqFunc1()
#### A(92h) - CdromIoIrqFunc2()
#### A(93h) - CdromDmaIrqFunc2()
#### A(95h) - CdInitSubFunc()  ;subfunction for _96_init()
#### A(9Eh) - SetCdromIrqAutoAbort(type,flag)
#### A(A2h) - EnqueueCdIntr()  ;with prio=0 (fixed)
#### A(A3h) - DequeueCdIntr()  ;does NOT work due to SysDeqIntRP bug
Internally used CDROM functions for initialization and IRQ handling.<br/>



##   BIOS Memory Card Functions
#### General File Functions
Memory Cards aka Backup Units (bu) are basically accessed via normal file
functions, with device names "bu00:" (Slot 1) and "bu10:" (Slot 2),<br/>
[BIOS File Functions](kernelbios.md#bios-file-functions)<br/>
Before using the file functions for memory cards, first call
InitCARD2(pad\_enable), then StartCARD2(), and then \_bu\_init().<br/>

#### File Header, Filesize, and Sector Alignment
The first 100h..200h bytes (2..4 sectors) of the file must contain the title
and icon bitmap(s). For details, see:<br/>
[Memory Card Data Format](controllersandmemorycards.md#memory-card-data-format)<br/>
The filesize must be a multiple of 2000h bytes (one block), the maximum size
would be 1E000h bytes (when using all 15 blocks on the memory card). The
filesize must be specified when creating the file (ie. accessmode bit9=1, and
bit16-31=number of blocks). Once when the file is created, the BIOS does NOT
allow to change the filesize (unless by deleting and re-creating the file).<br/>
When reading/writing files, the amount of data must be a multiple of 80h bytes
(one sector), and the file position must be aligned to a 80h-byte boundary,
too. There's no restriction on fragmented files (ie. one may cross 2000h-byte
block boundaries within the file).<br/>

#### Poor Memcard Performance
PSX memory card accesses are typically super-slow. That, not so much because
the hardware would be slow, but rather because of improper inefficent code at
the BIOS side. The original BIOS tries to synchronize memory card accesses with
joypad accesses simply by accessing only one sector per frame (although it
could access circa two sectors). To the worst, the BIOS accesses Slot 1 only on
each second frame, and Slot 2 only each other frame (although in 99% of all
cases only one slot is accessed at once, so the access time drops to 0.5
sectors per frame).<br/>
Moreover, the memory card id, directory, and broken sector list do occupy 26
sectors (although the whole information would fit into 4 or 5 sectors) (a
workaround would be to read only the first some bytes, and to skip the
additional unused bytes - though that'd also mean to skip the checksums which
are unfortunately stored at the end of the sector).<br/>
And, anytime when opening a file (in synchronous mode), the BIOS does
additionally read sector 0 (which is totally useless, and gets especially slow
when opening a bunch of files; eg. when extracting the title/icon from all
available files on the card).<br/>

#### Asynchronous Access
The BIOS supports synchronous and asynchronous memory card access. Synchronous
means that the BIOS function doesn't return until the access has completed
(which means, due to the poor performance, that the function spends about 75%
of the time on inactivity) (except in nocash PSX bios, which has better
performance), whilst asynchronous access means that the BIOS function returns
immediately after invoking the access (which does then continue on interrupt
level, and does return an event when finished).<br/>
The file "read" and "write" functions act asynchronous when accessmode
bit15 is set when opening the file. Additionally, the A(ACh)
\_card\_load(port) function can be used to tell the BIOS to load
the directory entries and broken sector list to its internal RAM buffers (eg.
during the games title screen, so the BIOS doesn't need to load that data once
when the game enters its memory card menu). All other functions like erase
or format always act synchronous. The open/findfirst/findnext
functions do normally complete immediately without accessing the card at all
(unless the directory wasn't yet read; in that case the directory is loading in
synchronous fashion).<br/>
Unfortunately, the asynchronous response doesn't rely on a single callback
event, but rather on a bunch of different events which must be all allocated
and tested by the game (and of which, one event is delivered on completion)
(which one depends on whether function completed okay, or if an error
occurred).<br/>

#### Multitap Support (and Multitap Problems)
The BIOS does have some partial support for accessing more than two memory
cards (via Multitap adaptors). Device/port names "bu01:", "bu02:", "bu03:"
allow to access extra memory carts in slot1 (and "bu11:", "bu12:", "bu13:" in
slot2). Namely, those names will send values 82h, 83h, 84h to the memory card
slot (instead of the normal 81h value).<br/>
However, the BIOS directory\_buffer and broken\_sector\_list do support only two
memory cards (one in slot1 and one in slot2). So, trying to access more memory
cards may cause great data corruption (though there might be a way to get the
BIOS to reload those buffers before accessing a different memory card).<br/>
Aside from that problem, the BIOS functions are very-very-very slow even when
accessing only two memory cards. Trying to use the BIOS to access up to eight
memory cards would be very-extremly-very slow, which would be more annoying
than useful.<br/>

#### B(4Ah) - InitCARD2(pad\_enable)  ;uses/destroys k0/k1 !!!
#### B(4Bh) - StartCARD2()
#### B(4Ch) - StopCARD2()
#### A(55h) or A(70h) - \_bu\_init()

```
  --- Below are some lower level memory card functions ---
```

#### A(ABh) - \_card\_info(port)
#### B(4Dh) - \_card\_info\_subfunc(port)  ;subfunction for "\_card\_info"
Can be used to check if the most recent call to \_card\_write has completed
okay. Issues an incomplete dummy read command (similar to B(4Fh) -
\_card\_read). The read command is aborted once when receiving the status
byte from the memory card (the actual data transfer is skipped).<br/>

#### A(AFh) - card\_write\_test(port)  ;not supported by old CEX-1000 version
Resets the card changed flag. For some strange reason, this flag isn't
automatically reset after reading the flag, instead, the flag is reset upon
sector writes. To do that, this function issues a dummy write to sector 3Fh.<br/>

#### B(50h) - \_new\_card()
Normally any memory card read/write functions fail if the BIOS senses the card
change flag to be set. Calling this function tells the BIOS to ignore the card
change flag on the next read/write operation (the function is internally used
when loading the "MC" ID from sector 0, and when calling the card\_write\_test
function to acknowledge the card change flag).<br/>

#### B(4Eh) - \_card\_write(port,sector,src)
#### B(4Fh) - \_card\_read(port,sector,dst)
Invokes asynchronous reading/writing of a single sector. The function returns
1=okay, or 0=failed (on invalid sector numbers). The actual I/O is done on IRQ
level, completion of the I/O command transmission can be checked, among others,
via get/wait\_card\_status(slot) functions (with slot=port/10h).<br/>
In case of the write function, completion of the \<transmission\> does NOT
mean that the actual \<writing\> has completed, instead, write errors are
indicated upon completion of the \<next sector\> read/write transmission
(or, if there are no further sectors to be accessed; one can use \_card\_info to
verify completion of the last written sector).<br/>
The sector number should be in range of 0..3FFh, for some strange reason,
probably a BUG, the function also accepts sector 400h. The specified sector
number is directly accessed (it is NOT parsed through the broken sector
replacement list).<br/>

#### B(5Ch) - \_card\_status(slot)
#### B(5Dh) - \_card\_wait(slot)
Returns the status of the most recent I/O command, possible values are:<br/>
```
  01h=ready
  02h=busy/read
  04h=busy/write
  08h=busy/info
  11h=failed/timeout (eg. when no cartridge inserted)
  21h=failed/general error
```
\_card\_status returns immediately, \_card\_wait waits until a non-busy
state occurs.<br/>

#### A(A7h) - bufs\_cb\_0()
#### A(A8h) - bufs\_cb\_1()
#### A(A9h) - bufs\_cb\_2()
#### A(AAh) - bufs\_cb\_3()
#### A(AEh) - bufs\_cb\_4()
These five callback functions are internally used by the BIOS, notifying other
BIOS functions about (un-)successful completion of memory card I/O commands.<br/>

#### B(58h) - \_card\_chan()
This is a subfunction for the five bufs\_cb_\_xxx functions (indicating
whether the callback occured for a slot1 or slot2 access).<br/>

#### A(ACh) - \_card\_load(port)
Invokes asynchronous reading of the memory card directory. The function isn't
too useful because the BIOS tends to read the directory automatically in
various places in synchronous mode, so there isn't too much chance to replace
the automatic synchronous reading by asynchronous reading.<br/>

#### A(ADh) - \_card\_auto(flag)
Can be used to enable/disable auto format (0=off, 1=on). The \_bu\_init function
initializes auto format as disabled. If auto format is enabled, then the BIOS
does automatically format memory cards if it has failed to read the "MC" ID
bytes on sector 0. Although potentially useful, activating this feature is
rather destructive (for example, read errors on sector 0 might occur accidently
due to improperly inserted cards with dirty contacts, so it'd be better to
prompt the user whether or not to format the card, rather than doing that
automatically).<br/>

#### C(1Ah) - set\_card\_find\_mode(mode)
#### C(1Dh) - get\_card\_find\_mode()
Allows to get/set the card find mode (0=normal, 1=find deleted files), the mode
setting affects only the firstfile2/nextfile functions. All other file functions
are used fixed mode settings (always mode=0 for open, rename,
erase, and mode=1 for undelete).<br/>



##   BIOS Interrupt/Exception Handling
The Playstation's Kernel uses an uncredible inefficient and unstable exception
handler; which may have been believed to be very powerful and flexible.<br/>

#### Inefficiency
For a maximum of slowness, it does always save and restore all CPU registers
(including such that aren't used in the exception handler). It does then go
through a list of installed interrupt handlers - and executes ALL of them. For
example, a Timer0 IRQ is first passed to the Cdrom and Vblank handlers (which
must reject it, no thanks), before it does eventually reach the Timer0 handler.<br/>

#### Unstable IRQ Handling
A fundamental mistake in the exception handler is that it doesn't memorize the
incoming IRQ flags. So the various interrupt handlers must check Port 1F801070h
one after each other. That means, if a high priority handler has rejected IRQ
processing (because the desired IRQ flag wasn't set at that time), then a lower
priority handler may process it (assuming that the IRQ flag got set in the
meantime), and, in worst case it may even acknowledge it (so the high priority
handler does never receive it).<br/>
To avoid such problems, there should be only ONE handler installed for each IRQ
source. However, that isn't always possible because the Kernel automatically
installs some predefined handlers. Most noteworthy, the totally bugged
DefaultInterruptHandlers is always installed (and cannot be removed), so it
does randomly trigger Events. Fortunately, it does not acknowledge the IRQs
(unless SetIrqAutoAck was used to enable that fatal behaviour).<br/>

#### B(18h) - ResetEntryInt()
Applies the default "Exit" structure (which consists of a pointer to
ReturnFromException, and the Kernel's exception stacktop (minus 4, for whatever
reason), and zeroes for the R16..R23,R28,R30 registers. Returns the address of
that structure.<br/>
See HookEntryInt for details.<br/>

#### B(19h) - HookEntryInt(addr)
addr points to a structure (with same format as for the setjmp function):<br/>
```
  00h 4    r31/ra,pc ;usually ptr to ReturnFromException function
  04h 4    r28/sp    ;usually exception stacktop, minus 4, for whatever reason
  08h 4    r30/fp    ;usually 0
  0Ch 4x8  r16..r23  ;usually 0
  2Ch 4    r28/gp    ;usually 0
```
The hook function is executed only if the ExceptionHandler has been fully
executed (after processing an IRQ, many interrupt handlers are calling
ReturnFromException to abort further exception handling, and thus do skip the
hook function). Once when the hook function has finished, it should execute
ReturnFromException. The hook function is called with r2=1 (that is important
if the hook address was recorded with setjmp, where it "returns" to the
setjmp caller, with r2 as "return value").<br/>

#### Priority Chains
The Kernel's exception handler has four priority chains, each may contain one
or more Interrupt or Exception handlers. The default handlers are:<br/>
```
  Prio Chain Content
  0    CdromDmaIrq, CdromIoIrq, SyscallException
  1    CardSpecificIrq, VblankIrq, Timer2Irq, Timer1Irq, Timer0Irq
  2    PadCardIrq
  3    DefInt
```
The exception handler calls all handlers, starting with the first element in
the priority 0 chain (ie. usually CdromDmaIrq). The separate handlers must
check if they want to process the IRQ (eg. CdromDmaIrq would process only CDROM
DMA IRQs, but not joypad IRQs or so). If it has processed and acknowledged the
IRQ, then the handler may execute ReturnFromException, which causes the
handlers of lower priority to be skipped (if there are still other
unacknowledge IRQs pending, then the hardware will re-enter the exception
handler as soon as the RFE opcode in ReturnFromException does re-enable
interrupts).<br/>

#### C(02h) - SysEnqIntRP(priority,struc)  ;bugged, use with care
Inserts a new element in the specified priority chain. The new element is
inserted at the begin of the chain, so (within that priority chain) the new
element has highest priority.<br/>
```
  00h 4  pointer to next element    (0=none)  ;this pointer is inserted by BIOS
  04h 4  pointer to SECOND function (0=none)  ;executed if func1 returns r2<>0
  08h 4  pointer to FIRST  function (0=none)  ;executed first
  0Ch 4  Not used (usually zero)
```
BUG: SysDeqIntRP can remove only the first element in the chain (see there for
details), so adding new chain elements may cause OTHER functions to be unable
to remove their chain elements. The BIOS seems to be occassionally
adding/removing the "CardSpecificIrq" and "PadCardIrq" (with priority 1 and 2),
so using that priorities may cause the BIOS to be unable to remove that IRQ
handlers. Using priority 0 and 3 should work (as long as the software takes
care to remove only the newest elements) (but there should be no conflicts with
the BIOS which does never remove priority 0 and 3 elements) (leaving apart that
DequeueCdIntr and _96_remove try to remove priority 0 elements, but that
functions won't work anyways; due to the same bug).<br/>

#### C(03h) - SysDeqIntRP(priority,struc)  ;bugged, use with care
Removes the specified element from the specified priority chain.<br/>
BUG: The function tries to search the whole chain (and to remove the element if
it finds it). However, it does only check the first element properly, and,
thereafter it reads a garbage value from an uninitialized stack location, and
acts more or less unpredictable. So, it can remove only the first element in
the chain, ie. it should be called only if you are SURE that there's no newer
element in the chain, and only if you are SURE that the element IS in the
chain.<br/>

#### SYS(01h) - EnterCriticalSection()  ;syscall with r4=01h
Disables interrupts by clearing SR (cop0r12) Bit 2 and 10 (of which, Bit2 gets
copied to Bit0 once when returning from the syscall exception). Returns 1 if
both bits were set, returns 0 if one or both of the bits were already zero.<br/>

#### SYS(02h) - ExitCriticalSection()   ;syscall with r4=02h
Enables interrupts by set SR (cop0r12) Bit 2 and 10 (of which, Bit2 gets copied
to Bit0 once when returning from the syscall exception). There's no return
value (all registers except SR and K0 are unchanged).<br/>

#### C(0Dh) - SetIrqAutoAck(irq,flag)
Specifies if the DefaultInterruptHandler shall automatically acknowledge IRQs.
The "irq" paramter is the number of the interrupt, ie. 00h..0Ah = IRQ0..IRQ10.
The "flag" value should be 0 to disable AutoAck, or non-zero to enable AutoAck.
By default, AutoAck is disabled for all IRQs.<br/>
Mind that the DefaultInterruptHandler is totally bugged. Especially the AutoAck
feature doesn't work very well: It may cause higher priority handlers to miss
their IRQ, and it may even cause the DefaultInterruptHandler to miss its own
IRQs.<br/>

#### C(06h) - ExceptionHandler()
The C(06h) vector points to the exception handler, ie. to the function that is
invoked from the 4 opcodes at address 80000080h, that opcodes jump directly to
the exception handler, so patching the C(06h) vector has no effect.<br/>
Reading the C(06h) entry can be used to let a custom 80000080h handler pass
control back to the default handler (that, by a "direct" jump, not by the usual
"MOV R9,06h / CALL 0C0h" method, which would destroy main programs R9
register).<br/>
Also, reading C(06h) may be useful for patching the exception handler (which
contains a bunch of NOP opcodes, which seem to be intended to insert additional
opcodes, such like debugger exception handling) (Note: some of that NOPs are
reserved for Memory Card IRQ handling).<br/>
BUG: Early BIOS versions did try to examine a copy of cop0r13 in r2 register,
but did forgot cop0r13 to r2 (so they examined garbage), this was fixed in
newer BIOS versions, additionally, most commercial games still include patches
for compatibility with the old BIOS.<br/>

#### B(17h) - ReturnFromException()
Restores the CPU registers (R1-R31,HI,LO,SR,PC) (except R26/K0) from the
current TCB. This function is usually executed automatically at the end of the
ExceptionHandler, however, functions in the exception chain may call
ReturnFromException to return immediately, without processing chain elements of
lower priority.<br/>

#### C(00h) - EnqueueTimerAndVblankIrqs(priority) ;used with prio=1
#### C(01h) - EnqueueSyscallHandler(priority) ;used with prio=0
#### C(0Ch) - InitDefInt(priority) ;used with prio=3
Internally used to add some default IRQ and Exception handlers.<br/>

#### No Nested Exceptions
The Kernel doesn't support nested exceptions, that would require a decreasing
exception stack, however, the kernel saves the incoming CPU registers in the
current TCB, and an exception stack with fixed start address for internal
push/pop during exception handling. So, nesting would overwrite these values.
Do not enable IRQs, and don't trap other exceptions (like break or syscall
opcodes, or memory or overlow errors) during exception handling.<br/>
Note: The execption stack has a fixed size of 1000h bytes (and is located
somewhere in the first 64Kbytes of memory).<br/>



##   BIOS Event Functions
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
  F0000008h IRQ7  Controller (joypad/memcard)
  F0000009h IRQ9  SPU
  F000000Ah IRQ10 PIO ;uh, does the PIO have an IRQ signal? (IRQ10 is joypad)
  F000000Bh IRQ8  SIO
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



##   BIOS Event Summary
Below is a list of all events (class,spec values) that are delivered and/or
undelivered by the BIOS in one way or another. The BIOS does internally open
five events for cdrom (class=F0000003h with spec=10h,20h,40h,80h,8000h). The
various other class/spec's are only delivered by the BIOS (but not received by
the BIOS) (ie. a game may open/enable memory card events to receive
notifications from the BIOS).<br/>

#### CDROM Events
```
  F0000003h,10h  cdrom DMA finished (all sectors finished)
  F0000003h,20h  cdrom ?
  F0000003h,40h  cdrom dead feature (delivered only by unused functions)
  F0000003h,80h  cdrom INT4 (reached end of disk)
  F0000003h,100h         n/a ?  ;undelivered, but not opened, nor delivered
  F0000003h,200h                ;undelivered, but not opened
  F0000003h,8000h
```

#### Memory Card - Higher Level File/Device Events
```
  0000000xh,4     card file handle (x=fd) done okay
  F4000001h,4     card done okay (len=0)
  F4000001h,100h  card err busy  ;A(A9h)
  F4000001h,2000h card err eject ;A(AAh) or unformatted (bad "MC" id)
  F4000001h,8000h card err write ;A(A8h) or A(AEh) or general error
```

#### Memory Card - Lower Level Hardware I/O Events
```
  F0000011h,4      finished okay
  F0000011h,100h   err busy
  F0000011h,200h     n/a ?
  F0000011h,2000h  err
  F0000011h,8000h  err
  F0000011h,8001h  err (this one is NOT undelivered!)
```

#### Timer/Vblank Events
```
  F2000000h,2   Timer0 (IRQ4)
  F2000001h,2   Timer1 (IRQ5)
  F2000002h,2   Timer2 (IRQ6)
  F2000003h,2   Vblank (IRQ0) (unstable since IRQ0 is also used for joypad)
```

#### Default IRQ Handler Events (very unstable, don't use)
```
  F0000001h,1000h ;IRQ0  (VBLANK)
  F0000002h,1000h ;IRQ1  (GPU)
  F0000003h,1000h ;IRQ2  (CDROM)
  F0000004h,1000h ;IRQ3  (DMA)
  F0000005h,1000h ;IRQ4  (TMR0)
  F0000006h,1000h ;IRQ5  (TMR1)
  F0000006h,1000h ;IRQ6  (TMR2) (accidently uses same event as TMR1)
  F0000008h,1000h ;IRQ7  (joypad/memcard)
  F0000009h,1000h ;IRQ9  (SPU)
  F000000Ah,1000h ;IRQ10 (Joypad and PIO)
  F000000Bh,1000h ;IRQ8  (SIO)
```

#### Unresolved Exception Events
```
  F0000010h,1000h unknown exception ;neither IRQ nor SYSCALL
  F0000010h,4000h unknown syscall   ;syscall(04h..FFFFFFFFh)
```



##   BIOS Thread Functions
#### B(0Eh) - OpenTh(reg\_PC,reg\_SP\_FP,reg\_GP)
Searches a free TCB, marks it as used, and stores the inital program counter
(PC), global pointer (GP aka R28), stack pointer (SP aka R29), and frame
pointer (FP aka R30) (using the same value for SP and FP). All other registers
are left uninitialized (eg. may contain values from an older closed thread,
that includes the SR register, see note).<br/>
The return value is the new thread handle (in range FF000000h..FF000003h,
assuming that 4 TCBs are allocated) or FFFFFFFFh if there's no free TCB. The
function returns to the old current thread, use "ChangeTh" to switch to the
new thread.<br/>
Note: The desired max number of TCBs can be specified in the SYSTEM.CNF boot
file (the default is "TCB = 4", one initially used for the boot executable,
plus 3 free threads).<br/>

#### BUG - Unitialized SR Register
OpenTh does NOT initialize the SR register (cop0r12) of the new thread.
Upon powerup, the bootcode zerofills the TCB memory (so, the SR of new threads
will be initially zero; ie. Kernel Mode, IRQ's disabled, and COP2 disabled).
However, when closing/reopening threads, the SR register will have the value of
the old closed thread (so it may get started with IRQs enabled, and, in worst
case, if the old thread should have switched to User Mode, even without access
to KSEG0, KSEG1 memory).<br/>
Or, ACTUALLY, the memory is NOT zerofilled on powerup... so SR is total random?<br/>

#### B(0Fh) - CloseTh(handle)
Marks the TCB for the specified thread as unused. The function can be used for
any threads, including for the current thread.<br/>
Closing the current thread doesn't terminate the current thread, so it may
cause problems once when opening a new thread, however, it should be stable to
execute the sequence "DisableInterrupts, CloseCurrentThread,
ChangeOtherThread".<br/>
The return value is always 1 (even if the handle was already closed).<br/>

#### B(10h) - ChangeTh(handle)
Pauses the current thread, and activates the selected new thread (or crashes if
the specified handle was unused or invalid).<br/>
The return value is always 1 (stored in the R2 entry of the TCB of the old
thread, so the return value will be received once when changing back to the old
thread).<br/>
Note: The BIOS doesn't automatically switch from one thread to another. So, all
other threads remain paused until the current thread uses ChangeTh to pass
control to another thread.<br/>
Each thread is having it's own CPU registers (R1..R31,HI,LO,SR,PC), the
registers are stored in the TCB of the old thread, and restored when switching
back to that thread. Mind that other registers (I/O Ports or GTE registers
aren't stored automatically, so, when needed, they need to be pushed/popped by
software before/after ChangeTh).<br/>

#### C(05h) - get\_free\_TCB\_slot()
Subfunction for OpenTh, returns the number of the first free TCB (usually
in range 0..3) or FFFFFFFFh if there's no free TCB.<br/>

#### SYS(03h) ChangeThreadSubFunction(addr) ;syscall with r4=03h, r5=addr
Subfunction for ChangeTh, R5 contains the address of the new TCB, just like
all exceptions, the syscall exception is saving the CPU registers in the
current TCB, but does then apply the new TCB as current TCB, and so, it does
then enter the new thread when returning from the exception.<br/>



##   BIOS Timer Functions
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



##   BIOS Joypad Functions
#### Pad Input
Joypads should be initialized via InitPAD2(buf1,22h,buf2,22h), and StartPAD2().
The main program can read the pad data from the buf1/buf2 addresses (including
Status, ID1, button states, and any kind of analogue inputs). For more info on
ID1, Buttons and analogue inputs, see<br/>
[Controllers and Memory Cards](controllersandmemorycards.md)<br/>
Note: The BIOS doesn't include any functions for sending custom data to the
pads (such like for controlling rumble motors).<br/>

#### B(12h) - InitPAD2(buf1, siz1, buf2, siz2)
Memorizes the desired buf1/buf2 addresses, zerofills the buffers by using the
siz1/siz2 buffer size values (which should be 22h bytes each). And does some
initialization on the PadCardIrq element (but doesn't enqueue it, that must be
done by a following call to StartPAD2), and does set the "pad\_enable\_flag", that
flag can be also set/cleared via InitCARD2(pad\_enable), where it selects if the
Pads are kept handled together with Memory Cards. buf1/buf2 are having the
following format:<br/>
```
  00h      Status (00h=okay, FFh=timeout/wrong ID2)
  01h      ID1    (eg. 41h=digital_pad, 73h=analogue_pad, 12h=mouse, etc.)
  02h..21h Data   (max 16 halfwords, depending on lower 4bit of ID1)
```
Note: InitPAD2 does initially zerofill the buffers, so, until the first IRQ is
processed, the initial status is 00h=okay, with buttons=0000h (all buttons
pressed), to fix that situation, change the two status bytes to FFh after
calling InitPAD2 (or alternately, reject ID1=00h).<br/>
Once when the PadCardIrq is enqueued via StartPAD2, and while "pad\_enable\_flag"
is set, the data for (both) Pad1 and Pad2 is read on Vblank interrupts, and
stored in the buffers, the IRQ handler stores up to 22h bytes in the buffer
(regardless of the siz1/siz2 values) (eg. a Multitap adaptor uses all 22h
bytes).<br/>

#### B(13h) - StartPAD2()
Should be used after InitPAD2. Enqueues the PadCardIrq handler, and does
additionally initialize some flags.<br/>

#### B(14h) - StopPAD2()
Dequeues the PadCardIrq handler. Note that this handler is also used for memory
cards, so it'll "stop" cards, too.<br/>

#### B(15h) - PAD\_init2(type, button\_dest, unused, unused)
This is an extremely bizarre and restrictive function - don't use! The function
fails unless type is 20000000h or 20000001h (the type value has no other
function). The function uses "buf1/buf2" addresses that are located somewhere
"hidden" within the BIOS variables region, the only way to read from that
internal buffers is to use the ugly "PAD_dr()" function. For
some strange reason it FFh-fills buf1/buf2, and does then call
InitPAD2(buf1,22h,buf2,22) (which does immediately 00h-fill the previously
FFh-filled buffers), and does then call StartPAD2().<br/>
Finally, it does memorize the "button\_dest" address (see
PAD_dr() for details on that value). The two unused parameters
have no function, however, they are internally written back to the stack
locations reserved for parameter 2 and 3, ie. at [SP+08h] and [SP+0Ch] on the
caller's stack, so the function MUST be called with all four parameters
allocated on stack. Return value is 2 (or 0 if type was disliked).<br/>

#### B(16h) - PAD\_dr()
This is a very ugly function, using the internal "buf1/buf2" values from
"PAD_init2" and the "button\_dest" value that was passed to that
function.<br/>
If "button\_dest" is non-zero, then this function is automatically called by the
PadCardIrq handler, and stores it's return value at [button\_dest] (where it may
be read by the main program). If "button\_dest" is zero, then it isn't called
automatically, and it \<can\> be called manually (with return value in R2),
however, it does additionally write the return value to [button\_dest], ie. to
[00000000h] in this case, destroying that memory location.<br/>
The return value itself is useless garbage: The lower 16bit contain the pad1
buttons, the upper 16bit the pad2 buttons, of which, both values have reversed
byte-order (ie. the first button byte in upper 8bit). The function works only
with controller IDs 41h (digital joypad) and 23h (nonstandard device). For
ID=23h, the halfword is ORed with 07C7h, and bit6,7 are then cleared if the
analogue inputs are greater than 10h. For ID=41h the data is left intact. Any
other ID values, or disconnected joypads, cause the halfword to be set to FFFFh
(same as when no buttons are pressed), that includes newer analogue pads
(unless they are switched to "digital" mode).<br/>



##   BIOS GPU Functions
#### A(48h) - SendGP1Command(gp1cmd)
Writes [1F801814h]=gp1cmd. There's no return value (r2 is left unchanged).<br/>

#### A(49h) - GPU\_cw(gp0cmd)      ;send GP0 command word
Calls gpu\_sync(), and does then write [1F801810h]=gp0cmd. Returns the return
value from the gpu\_sync() call.<br/>

#### A(4Ah) - GPU\_cwp(src,num) ;send GP0 command word and parameter words
Calls gpu\_sync(), and does then copy "num" words from [src and up] to
[1F801810h], src should usually point to a command word, followed by num-1
parameter words. Transfer is done by software (without DMA). Always returns 0.<br/>

#### A(4Bh) - send\_gpu\_linked\_list(src)
Transfer an OT via DMA. Calls gpu\_sync(), and does then write
[1F801814h]=4000002h, [1F8010F4h]=0, [1F8010F0h]=[1F8010F0h] OR 800h,
[1F8010A0h]=src, [1F8010A4h]=0, [1F8010A8h]=1000401h. The function does
additionally output a bunch of TTY status messages via printf. The function
doesn't wait until the DMA is completed. There's no return value.<br/>

#### A(4Ch) - gpu\_abort\_dma()
Writes [1F8010A8h]=401h, [1F801814h]=4000000h, [1F801814h]=2000000h,
[1F801814h]=1000000h. Ie. stops GPU DMA, and issues GP1(4), GP1(2), GP1(1).
Returns 1F801814h, ie. the I/O address.<br/>

#### A(4Dh) - GetGPUStatus()
Reads [1F801814h] and returns that value.<br/>

#### A(46h) - GPU\_dw(Xdst,Ydst,Xsiz,Ysiz,src)
Waits until GPUSTAT.Bit26 is set (unlike gpu\_sync, which waits for Bit28), and
does then [1F801810h]=A0000000h, [1F801810h]=YdstXdst, [1F801810h]=YsizXsiz,
and finally transfers "N" words from [src and up] to [1F801810h], where "N" is
"Xsiz\*Ysiz/2". The data is transferred by software (without DMA) (by code
executed in the uncached BIOS region with high waitstates, so the data transfer
is very SLOW).<br/>
Caution: If "Xsiz\*Ysiz" is odd, then the last halfword is NOT transferred, so
the GPU stays waiting for the last data value.<br/>
Returns [SP+04h]=Ydst, [SP+08h]=Xsiz, [SP+0Ch]=Ysiz, [SP+10h]=src+N\*4, and
R2=src=N\*4.<br/>

#### A(47h) - gpu\_send\_dma(Xdst,Ydst,Xsiz,Ysiz,src)
Calls gpu\_sync(), writes [1F801810h]=A0000000h, [1F801814h]=4000002h,
[1F8010F0h]=[1F8010F0h] OR 800h, [1F8010A0h]=src, [1F8010A4h]=N\*10000h+10h
(where N="Xsiz\*Ysiz/32"), [1F8010A8h]=1000201h.<br/>
Caution: If "Xsiz\*Ysiz" is not a multiple of 32, then the last halfword(s) are
NOT transferred, so the GPU stays waiting for that values.<br/>
Returns R2=1F801810h, and [SP+04h]=Ydst, [SP+08h]=Xsiz, [SP+0Ch]=Ysiz.<br/>

#### A(4Eh) - gpu\_sync()
If DMA is off (when GPUSTAT.Bit29-30 are zero): Waits until GPUSTAT.Bit28=1 (or
until timeout).<br/>
If DMA is on: Waits until D2\_CHCR.Bit24=0 (or until timeout), and does then
wait until GPUSTAT.Bit28=1 (without timeout, ie. may hang forever), and does
then turn off DMA via GP1(04h).<br/>
Returns 0 (or -1 in case of timeout, however, the timeout values are very big,
so it may take a LOT of seconds before it returns).<br/>



##   BIOS Memory Allocation
#### A(33h) - malloc(size)
Allocates size bytes on the heap, and returns the memory handle (aka the
address of the allocated memory block). The address of the block is guaranteed
to by aligned to 4-byte memory boundaries. Size is rounded up to a multiple of
4 bytes. The address may be in KUSEG, KSEG0, or KSEG1, depending on the address
passed to InitHeap.<br/>
Caution: The BIOS (tries to) initialize the heap size to 0 bytes (actually it
accidently overwrites that initial setting by garbage during relocation), so
any call to malloc will fail, unless InitHeap has been used to initialize the
address/size of the heap.<br/>

#### A(34h) - free(buf)
Deallocates the memory block. There's no return value, and no error checking.
The function simply sets [buf-4]=[buf-4] OR 00000001h, so if buf is an invalid
handle it may destroy memory at [buf-4], or trigger a memory exception (for
example, when buf=0).<br/>

#### A(37h) - calloc(sizx, sizy)     ;SLOW!
Allocates xsiz\*ysiz bytes by calling malloc(xsiz\*ysiz), and, unlike malloc, it
does additionally zerofill the memory via SLOW "bzero" function. Returns the
address of the memory block (or zero if failed).<br/>

#### A(38h) - realloc(old\_buf, new\_size)   ;SLOW!
If "old\_buf" is zero, executes malloc(new\_size), and returns r2=new\_buf (or
0=failed). Else, if "new\_size" is zero, executes free(old\_buf), and returns
r2=garbage. Else, executes malloc(new\_size), bcopy(old\_buf,new\_buf,new\_size),
and free(old\_buf), and returns r2=new\_buf (or 0=failed).<br/>
Caution: The bcopy function is SLOW, and realloc does accidently copy
"new\_size" bytes from old\_buf, so, if the old\_size was smaller than new\_size
then it'll copy whatever garbage data - in worst case, if it exceeds the top of
the 2MB RAM region, it may crash with a locked memory exception, although
that'd happen only if SetMem(2) was used to restrict RAM to 2MBs.<br/>

#### A(39h) - InitHeap(addr, size)
Initializes the address and size of the heap - the BIOS does not automatically
do this, so, before using the heap, InitHeap must be called by software.
Usually, the heap would be memory region between the end of the boot
executable, and the bottom of the executable's stack. InitHeap can be also used
to deallocate all memory handles (eg. when a new exe file has been loaded, it
may use it to deallocate all old memory).<br/>
The heap is used only by malloc/realloc/calloc/free, and by the "qsort"
function.<br/>

#### B(00h) - alloc\_kernel\_memory(size)
#### B(01h) - free\_kernel\_memory(buf)
Same as malloc/free, but, instead of the heap, manages the 8kbyte control block
memory at A000E000h..A000FFFFh. This region is used by the kernel to allocate
ExCBs (4x08h bytes), EvCBs (N\*1Ch bytes), TCBs (N\*0C0h bytes), and the process
control block (1x04h bytes). Unlike the heap, the BIOS does automatically
initialize this memory region via SysInitMemory(addr,size), and does
autimatically allocate the above data (where the number of EvCBs and TCBs is as
specified in the SYSTEM.CNF file). Note: FCBs and DCBs are located elsewhere,
at fixed locations in the kernel variables area.<br/>

#### Scratchpad Note
The kernel doesn't include any allocation functions for the scratchpad (nor do
any kernel functions use that memory area), so the executable can freely use
the "fast" memory at 1F800000h..1F8003FFh.<br/>

#### A(9Fh) - SetMem(megabytes)
Changes the effective RAM size (2 or 8 megabytes) by manipulating port
1F801060h, and additionally stores the size in megabytes in RAM at [00000060h].<br/>
Note: The BIOS bootcode accidently sets the RAM value to 2MB (which is the
correct physical memory size), but initializes the I/O port to 8MB (which
mirrors the physical 2MB within that 8MB region), so the initial values don't
match up with each other.<br/>
Caution: Applying the correct size of 2MB may cause the "realloc" function to
crash (that function may accidently access memory above 2MB).<br/>



##   BIOS Memory Fill/Copy/Compare (SLOW)
Like most A(NNh) functions, below functions are executed in uncached BIOS ROM,
the ROM has very high waitstates, and the 32bit opcodes are squeezed through an
8bit bus. Moreover, below functions are restricted to process the data
byte-by-byte. So, they are very-very-very slow, don't even think about using
them.<br/>
Of course, that applies also for most other BIOS functions. But it's becoming
most obvious for these small functions; memcpy takes circa 160 cycles per byte
(reasonable would be less than 4 cycles), and bzero takes circa 105 cycles per
byte (reasonable would be less than 1 cycles).<br/>

#### A(2Ah) - memcpy(dst, src, len)
Copies len bytes from [src..src+len-1] to [dst..dst+len-1]. Refuses to copy any
data when dst=00000000h or when len\>7FFFFFFFh. The return value is always
the incoming "dst" value.<br/>

#### A(2Bh) - memset(dst, fillbyte, len)
Fills len bytes at [dst..dst+len-1] with the fillbyte value. Refuses to fill
memory when dst=00000000h or when len\>7FFFFFFFh. The return value is the
incoming "dst" value (or zero, when len=0 or len\>7FFFFFFFh).<br/>

#### A(2Ch) - memmove(dst, src, len) - bugged
Same as memcpy, but (attempts) to support overlapping src/dst regions, by using
a backwards transfer when src\<dst (and, for some reason, only when
dst\>=src+len).<br/>
BUG: The backwards variant accidently transfers len+1 bytes from [src+len..src]
down to [dst+len..dst].<br/>

#### A(2Dh) - memcmp(src1, src2, len) - bugged
Compares len bytes at [src1..src1+len-1] with [src2..src2+len-1], and
(attempts) to return the difference between the first mismatching bytes, ie.
[src1+N]-[src2+N], or 0 if there are no mismatches. Refuses to compare data
when src1 or src2 is 00000000h, and returns 0 in that case.<br/>
BUG: Accidently returns the difference between the bytes AFTER the first
mismatching bytes, ie. [src1+N+1]-[src2+N+1].<br/>
That means that a return value of 0 can mean absolutely anything: That the
memory blocks are identical, or that a mismatch has been found (but that the
NEXT byte after the mismatch does match), or that the function has failed (due
to src1 or src2 being 00000000h).<br/>

#### A(2Eh) - memchr(src, scanbyte, len)
Scans [src..src+len-1] for the first occurence of scanbyte. Refuses to scan any
data when src=00000000h or when len\>7FFFFFFFh. Returns the address of that
first occurence, or 0 if the scanbyte wasn't found.<br/>

#### A(27h) - bcopy(src, dst, len)
Same as "memcpy", but with "src" and "dst" exchanged. That is, the first
parameter is "src", the refuse occurs when "src" is 00000000h, and, returns the
incoming "src" value (whilst "memcpy" uses "dst" in that places).<br/>

#### A(28h) - bzero(dst, len)
Same as memset, but uses 00h as fixed fillbyte value.<br/>

#### A(29h) - bcmp(ptr1, ptr2, len) - bugged
Same as "memcmp", with exactly the same bugs.<br/>



##   BIOS String Functions
#### A(15h) - strcat(dst, src)
Appends src to the end of dst. Searches the ending 00h byte in dst, and copies
src to that address, up to including the ending 00h byte in src. Returns the
incoming dst value. Refuses to do anything if src or dst is 00000000h (and
returns 0 in that case).<br/>

#### A(16h) - strncat(dst, src, maxlen)
Same as "strcat", but clipped to "MaxSrc=(min(0,maxlen)+1)" characters, ie. the
total length is max "length(dst)+min(0,maxlen)+1". If src is longer or equal to
"MaxSrc", then only the first "MaxSrc" chars are copied (with the last byte
being replaced by 00h). If src is shorter, then everything up to the ending 00h
byte gets copied, but without additional padding (unlike as in "strncpy").<br/>

#### A(17h) - strcmp(str1, str2)
Compares the strings up to including ending 00h byte. Returns 0 if they are
identical, or otherwise [str1+N]-[str2+N], where N is the location of the first
mismatch, the two bytes are sign-expanded to 32bits before doing the
subtraction. The function rejects str1/str2 values of 00000000h (and returns
0=both are zero, -1=only str1 is zero, and +1=only str2 is zero).<br/>

#### A(18h) - strncmp(str1, str2, maxlen)
Same as "strcmp" but stops after comparing "maxlen" characters (and returns 0
if they did match). If the strings are shorter, then comparision stops at the
ending 00h byte (exactly as for strcmp).<br/>

#### A(19h) - strcpy(dst, src)
Copies data from src to dst, up to including the ending 00h byte. Refuses to
copy anything if src or dst is 00000000h. Returns the incoming dst address (or
0 if copy was refused).<br/>

#### A(1Ah) - strncpy(dst, src, maxlen)
Same as "strcpy", but clipped to "maxlen" characters. If src is longer or equal
to maxlen, then only the first "maxlen" chars are copied (but without appending
an ending 00h byte to dst). If src is shorter, then the remaining bytes in dst
are padded with 00h bytes.<br/>

#### A(1Bh) - strlen(src)
Returns the length of the string up to excluding the ending 00h byte (or 0 when
src is 00000000h).<br/>

#### A(1Ch) - index(src, char)
#### A(1Dh) - rindex(src, char)
#### A(1Eh) - strchr(src, char)  ;exactly the same as "index"
#### A(1Fh) - strrchr(src, char) ;exactly the same as "rindex"
Scans for the first (index) or last (rindex) occurence of char in the string.
Returns the memory address of that occurence (or 0 if there's no occurence, or
if src is 00000000h). Char may be 00h (returns the end address of the string).
Note that, despite of the function names, the return value is always a memory
address, NOT an index value relative to src.<br/>

#### A(20h) - strpbrk(src, list)
Scans for the first occurence of a character that is contained in the list. The
list contains whatever desired characters, terminated by 00h.<br/>
Returns the address of that occurence, or 0 if there was none. BUG: If there
was no occurence, it returns 0 only if src[0]=00h, and otherwise returns the
incoming "src" value (which is the SAME return value as when a occurence did
occur on 1st character).<br/>

#### A(21h) - strspn(src, list)
#### A(22h) - strcspn(src, list)
Scans for the first occurence of a character that is (strspn), or that isn't
(strcspn) contained in the list. The list contains whatever desired characters,
terminated by 00h.<br/>
Returns the index (relative to src) of that occurence. If there was no
occurence, then it returns the length of src. That silly return values do not
actually indicate if an occurence has been found or not (unless one checks for
[src+index]=00h or so).<br/>
\*\*\*<br/>
"The strcspn() function shall compute the length (in bytes) of the maximum
initial segment of the string pointed to by s1 which consists entirely of bytes
not from the string pointed to by s2."<br/>
"The strspn() function shall compute the length (in bytes) of the maximum
initial segment of the string pointed to by s1 which consists entirely of bytes
from the string pointed to by s2."<br/>
\*\*\*<br/>
Hmmmm, that'd be vice-versa?<br/>

#### A(23h) - strtok(src, list) ;first call
#### A(23h) - strtok(0, list) ;further call(s)
Used to split a string into fragments, list contains a list of characters that
are to be treated as separators, terminated by 00h.<br/>
The first call copies the incoming string to a buffer in the BIOS variables
area (the buffer size is 100h bytes, so the string should be max 255 bytes
long, plus the ending 00h byte, otherwise the function destroys other BIOS
variables), it does then search the first fragment, starting at the begin of
the buffer. Further calls (with src=00000000h) are searching further fragments,
starting at the buffer address from the previous call. The internal buffer is
used only for strtok, so its contents (and the returned string fragments)
remain intact until a new first call to strtok takes place.<br/>
The separate fragments are processed by searching the first separator, starting
at the current buffer address, the separator is then replaced by a 00h byte,
and the old buffer address is returned to the caller. Moreover, the function
tries to skip all continously following separators, until reaching a
non-separator, and does memorize that address for the next call (due to that
skipping further calls won't return empty fragments, the first call may do so
though). That skipping seems to be bugged, if list contains two or more
different characters, then additional separators aren't skipped.<br/>
```
  ",,TEXT,,,END" with list=","  returns "", "TEXT", "END"
  ",,TEXT,,,END" with list=",." returns "", "", "TEXT", "", "", "END"
```
Once when there are no more fragments, then 00000000h is returned.<br/>

#### A(24h) - strstr(str, substr) - buggy
Scans for the first occurence of substr in the string. Returns the memory
address of that occurence (or 0 if it was unable to find an occurence).<br/>
BUG: After rejecting incomplete matches, the function doesn't fallback to the
old str address plus 1, but does rather continue at the current str address.
Eg. it doesn't find substr="aab" in str="aaab" (in that example, it does merely
realize that "aab"\<\>"aaa" and then that "aab"\<\>"b").<br/>



##   BIOS Number/String/Character Conversion
#### A(0Eh) - abs(val)
#### A(0Fh) - labs(val)  ;exactly same as "abs"
Returns the absolute value (if val\<0 then R2=-val, else R2=val).<br/>

#### A(0Ah) - todigit(char)
Takes the incoming character, ANDed with FFh, and returns 0..9 for characters
"0..9" and 10..35 for "A..Z" or "a..z", or 0098967Fh (9,999,999 decimal) for
any other 7bit characters, or garbage for characters 80h..FFh.<br/>

#### A(25h) - toupper(char)
#### A(26h) - tolower(char)
Returns the incoming character, ANDed with FFh, with letters "A..Z" converted
to uppercase/lowercase format accordingly. Works only for char 00h..7Fh (some
characters in range 80h..FFh are left unchanged, others are randomly "adjusted"
by adding/subtracting 20h, and by sign-expanding the result to 32bits).<br/>

#### A(0Dh) - strtol(src, src\_end, base)
Converts a string to a number. The function skips any leading "blank"
characters (that are, 09h..0Dh, and 20h) (ie. TAB, CR, LF, SPC, and some
others) (some characters in range 80h..FFh are accidently treated as "blank",
too).<br/>
The incoming base value should be in range 2..11, although the function does
also accept the buggy values in range of 12..36 (for values other than 2..36 it
defaults to decimal/base10). The used numeric digits are "0..9" and "A..Z" (or
less when base is smaller than 36).<br/>
The string may have a negative sign prefix "-" (negates the result) (a "+" is
NOT recognized; and will be treated as the end of the string). Additionally,
the string may contain prefixes "0b" (binary/base2), "0x" (hex/base16), or "o"
(octal/base8) (only "o", not "0o"), allowing to override the incoming "base"
value.<br/>
BUG: Incoming base values greater than 11 don't work due to the prefix feature
(eg. base=16 with string "0b11" will be treated as 11 binary, and base=36 with
string "o55" will be treated as 55 octal) (the only workaround would be to
add/remove leading "0" characters, ie. "b11" or "00b11" or "0o55" would work
okay).<br/>
Finally, the function initializes result=0, and does then process the digits as
"result=result\*base+digit" (without any overflow checks) unless/until it
reaches an unknown digit (or when digit\>=base) (ie. the string may end with
00h, or with any other unexpected characters).<br/>
The function accepts both uppercase and lowercase characters (both as prefixes,
and as numeric digits). The function returns R2=result, and
[src\_end]=end\_address (ie. usually the address of the ending 00h byte; or of
any other unexpected end-byte). If src points to 00000000h, then the function
returns r2=0, and leaves [src\_end] unchanged.<br/>

#### A(0Ch) - strtoul(src, src\_end, base)
Same as "strtol" except that it doesn't recognize the "-" sign prefix (ie.
works only for unsigned numbers).<br/>

#### A(10h) - atoi(src)
#### A(11h) - atol(src)  ;exactly same as "atoi" (but slightly slower)
Same as "strtol", except that it doesn't return the string end address in
[src\_end], and except that it defaults to base=10, but still supports prefixes,
allowing to use base2,8,16. CAUTION: For some super bizarre reason, this
function treats "0" (a leading ZERO digit) as OCTAL prefix (unlike strtol,
which uses the "o" letter as octal prefix) (the "0x" and "0b" prefixes are
working as usually).<br/>

#### A(12h) - atob(src, num\_dst)
Calls "strtol(str,src\_end,10)", and does then exchange the two return values
(ie. sets R2=[src\_end], and [num\_dst]=value\_32bit).<br/>

#### A(0Bh) - atof(src) ;USES (ABSENT) COP1 FPU !!!
#### A(32h) - strtod(src, src\_end) ;USES (ABSENT) COP1 FPU !!!
These functions are intended to convert strings to floating point numbers,
however, the functions are accidently compiled for MIPS processors with COP1
floating point unit (which is not installed in the PSX, nor does the BIOS
support a COP1 software emulation), so calling these functions will produce a
coprocessor exception, causing the PSX to lockup via A(40h)
SystemErrorUnresolvedException.<br/>

#### Note
On other systems (eg. 8bit computers), "abs/atoi" (integer) and "labs/atol"
(long) may act differently. However, on the Playstation, both use signed 32bit
values.<br/>



##   BIOS Misc Functions
#### A(2Fh) - rand()
Advances the random generator as "x=x\*41C64E6Dh+3039h" (aka plus 12345
decimal), and returns a 15bit random value "R2=(x/10000h) AND 7FFFh".<br/>

#### A(30h) - srand(seed)
Changes the current 32bit value of the random generator.<br/>

#### A(B4h) - GetSystemInfo(index)  ;not supported by old CEX-1000 version
Returns a word, halfword, or string, depending on the selected index value:<br/>
```
  00h      Get Kernel BCD Date       (eg. 19951204h) (YYYYMMDDh)
  01h      Get Kernel Flags or so    (usually/always 000000003h)
  02h      Get Kernel Version String (eg. "CEX-3000/1001/1002 by K.S.",0)
  03h      Get whatever halfword     (usually 0)    ;PS2: returns cop0r15
  04h      Get whatever halfword     (usually 0)
  05h      Get RAM Size in kilobytes (usually 2048) ;=[00000060h] SHL 10
  06h..0Eh Get whatever halfwords    (usually 0,400h,0,200h,0,0,1,1,1)
  0Fh      N/A (returns zero) ;PS2: returns 0000h (effectively = same as zero)
  10h..FFFFFFFFh Not used (returns zero)
```
Note: The Date/Version are referring to the Kernel (in the first half of the
BIOS). The Intro and Bootmenu (in the second half of the BIOS) may have a
different version, there's no function to retrieve info on that portion,
however, a version string for it can be usually found at BFC7FF32h (eg. "System
ROM Version 4.5 05/25/00 E",0) (in many bios versions, the last letter of that
string indicates the region, but not in all versions) (the old SCPH1000 does
not include that version string at all).<br/>

#### B(56h) - GetC0Table()
#### B(57h) - GetB0Table()
Retrieves the address of the jump lists for B(NNh) and C(NNh) functions,
allowing to patch entries in that lists (however, the BIOS does often jump
directly to the function addresses, rather than indirectly via the list, so
patching may have little effect in such cases). Note: There's no function to
retrieve the address of the A(NNh) jump list, however, that list is
usually/always at 00000200h.<br/>

#### A(31h) - qsort(base, nel, width, callback)
Sorts an array, using a super-slow implementation of the "quick sort"
algorithm. base is the address of the array, nel is the number of elements in
the array, width is the size in bytes of each element, callback is a function
that receives pointers to two elements which need to be compared; callback
should return return zero if the elements are identical, or a positive/negative
number to indicate which element is bigger.<br/>
The qsort function rearranges the contents of the array, ie. depending on the
callback result, it may swap the contents of the two elements, for some bizarre
reason it doesn't swap them directly, but rather stores one of the elements
temporarily on the heap (that means, qsort works only if the heap was
initialized with InitHeap, and only if "width" bytes are free). There's no
return value.<br/>

#### A(35h) - lsearch(key, base, nel, width, callback)
#### A(36h) - bsearch(key, base, nel, width, callback)
Searches an element in an array (key is the pointer to the searched element,
the other parameters are same as for "qsort"). "lsearch" performs a slow linear
search in an unsorted array, by simply comparing one array element after each
other. "bsearch" assumes that the array contains sorted elements (eg. via
qsort), which is allowing to skip some elements, and to jump back and forth in
the array, until it has found the desired element (or the location where it'd
be, if it'd be in the array). Both functions return the address of the element
(or 0 if it wasn't found).<br/>

#### C(19h) - \_ioabort(txt1,txt2)
Displays the two strings on the TTY (in some cases the BIOS does accidently
pass garbage instead of the 2nd string though). And does then execute
_ioabort\_raw(1), see there for more details.<br/>

#### A(B2h) - _ioabort\_raw(param)  ;not supported by old CEX-1000 version
Executes "longjmp(ioabortbuffer,param)". Internally used to recover from
failed I/O operations, param should be nonzero to notify the setjmp caller
that the abort has occurred.<br/>

#### A(13h) - setjmp(buf)
This is a somewhat incomplete implementation of posix's setjmp, by storing the ABI-saved CPU registers in the specified buffer (30h bytes):<br/>
```
  00h 4    r31 (ra) (aka caller's pc)
  04h 4    r29 (sp)
  08h 4    r30 (fp)
  0Ch 4x8  r16..r23
  2Ch 4    r28 (gp)
```
That type of buffer can be used with "_ioabort", "longjmp", and also
"HookEntryInt(addr)".<br/>
The "setjmp" function returns 0 when called directly. However, it may return again -
to the same return address, and the same stack pointer - with another return value (which should be usually
non-zero, to indicate that the state has been restored (eg. _ioabort passes 1 as
return value).<br/>
Also noteworthy from what a compliant setjmp implementation should be doing
is the absence of saving the state of cop0 and cop2, thus making this slightly
unsuitable for a typical coroutine system implementation.<br/>

#### A(14h) - longjmp(buf, param)
Restores the R16-R23,GP,SP,FP,RA registers from a previously recorded 
jmp_buf buffer, and "returns" to that new RA address (rather than to the caller of the
longjmp function). The "param" value is passed as "return value" to the
code at RA, ie. usually to the caller of the original setjmp call. Noteworthy difference
from a conformant longjmp implementation is that the "param" value won't be clamped to 1 if
you pass 0 to it. So since setjmp returns 0 on the first call, the caller of longjmp must take
care that "param" is non-zero, so the callsite of setjmp can make the difference between the first
call and a rollback. See setjmp for further details.<br/>

#### A(53h) - set\_ioabort\_handler(src)  ;PS2 only  ;PSX: SystemError
Normally the _ioabort handler is changed only internally during booting, with
this new function, games can install their own _ioabort handler. src is pointer
to a 30h-byte "savestate" structure, which will be copied to the actual _ioabort
structure.<br/>

#### A(06h) or B(38h) - exit(exitcode)
Terminates the program and returns control to the BIOS; which does then lockup
itself via A(3Ah) _exit.<br/>

#### A(A0h) - \_boot()
Performs a warmboot (resets the kernel and reboots from CDROM). Unlike the
normal coldboot procedure, it doesn't display the "\<S\>" and "PS" intro
screens (and doesn't verify the "PS" logo in the ISO System Area), and, doesn't
enter the bootmenu (even if the disk drive is empty, or if it contains an Audio
disk). And, it doesn't reload the SYSTEM.CNF file, so the function works only
if the same disk is still inserted (or another disk with identical SYSTEM.CNF,
such like Disk 2 of the same game).<br/>

#### A(B5h..BFh) B(11h,24h..29h,2Ch..31h,5Eh..FFh) C(1Eh..7Fh) - N/A - Jump 0
These functions jump to address 00000000h. For whatever reason, that address
does usually contain a copy of the exception handler (ie. same as at address
80000080h). However, since there's no return address stored in EPC register,
the functions will likely crash when returning from the exception handler.<br/>

#### A(57h..5Ah,73h..77h,79h..7Bh,7Dh,7Fh..80h,82h..8Fh,B0h..B1h,B3h), and
#### C(0Eh..11h,14h) - N/A - Returns 0
No function. Simply returns with r2=00000000h.<br/>
Reportedly, A(85h) is CdStop, but that seems to be nonsense?<br/>

#### SYS(00h) - NoFunction()
No function. Simply returns without changing any registers or memory locations
(except that, of course, the exception handler destroys k0).<br/>

#### SYS(04h..FFFFFFFFh) - calls DeliverEvent(F0000010h,4000h)
These are syscalls with invalid function number in R4. For whatever reason that
is handled by issuing DeliverEvent(F0000010h,4000h). Thereafter, the syscall
returns to the main program (ie. it doesn't cause a SystemError).<br/>

#### A(3Ah) - \_exit(exitcode)
#### A(40h) - SystemErrorUnresolvedException()
#### A(A1h) - SystemError(type,errorcode) ;type "B"=Boot,"D"=Disk
These are used "SystemError" functions. The functions are repeatedly jumping to
themselves, causing the system to hang. Possibly useful for debugging software
which may hook that functions.<br/>

#### A(4Fh,50h,52h,53h,9Ah,9Bh) B(1Ah..1Fh,21h..23h,2Ah,2Bh,52h,5Ah) C(0Bh) - N/A
These are additional "SystemError" functions, but they are never used. The
functions are repeatedly jumping to themselves, causing the system to hang.<br/>

#### BRK(1C00h) - Division by zero (commonly checked/invoked by software)
#### BRK(1800h) - Division overflow (-80000000h/-1, sometimes checked by software)
The CPU does not generate any exceptions upon divide overflows, because of
that, the Kernel code and many games are commonly checking if the divider is
zero (by software), and, if so, execute a BRK 1C00h opcode. The default BIOS
exception handler doesn't handle BRK exceptions, and does simply redirect them
to SystemErrorUnresolvedException().<br/>



##   BIOS Internal Boot Functions
#### A(45h) - init\_a0\_b0\_c0\_vectors
Copies the three default four-opcode handlers for the A(NNh),B(NNh),C(NNh)
functions to A00000A0h..A00000CFh.<br/>

#### C(07h) - InstallExceptionHandlers()  ;destroys/uses k0/k1
Copies the default four-opcode exception handler to the exception vector at
80000080h..8000008Fh, and, for whatever reason, also copies the same opcodes to
80000000h..8000000Fh.<br/>

#### C(08h) - SysInitMemory(addr,size)
Initializes the address (A000E000h) and size (2000h) of the allocate-able
Kernel Memory region, and, seems to deallocate any memory handles which may
have been allocated via B(00h).<br/>

#### C(09h) - SysInitKernelVariables()
Zerofills all Kernel variables; which are usually at [00007460h..0000891Fh].<br/>
Note: During the boot process, the BIOS accidently overwrites the first opcode
of this function (by the last word of the A0h table), so, thereafter, this
function won't work anymore (nor would it be of any use).<br/>

#### C(12h) - InstallDevices(ttyflag)
Initializes the size and address of the File and Device Control Blocks (FCBs
and DCBs). Adds the TTY device by calling "KernelRedirect(ttyflag)", and the
CDROM and Memory Card devices by calling "AddCDROMDevice()" and
"AddMemCardDevice()".<br/>

#### C(1Ch) - AdjustA0Table()
Copies the B(32h..3Bh) and B(3Ch..3Fh) function addresses to A(00h..09h) and
A(3Bh..3Eh). Apparently Sony's compiler/linker can't insert the addresses in
the A0h table directly at compilation time, so this function is used to insert
them during execution of the boot code.<br/>



##   BIOS More Internal Functions
Below are mainly internally used device related subfunctions.<br/>

#### Internal Device Stuff
```
  A(5Bh) dev_tty_init()                                      ;PS2: SystemError
  A(5Ch) dev_tty_open(fcb,and unused:"path\name",accessmode) ;PS2: SystemError
  A(5Dh) dev_tty_in_out(fcb,cmd)                             ;PS2: SystemError
  A(5Eh) dev_tty_ioctl(fcb,cmd,arg)                          ;PS2: SystemError
  A(5Fh) dev_cd_open(fcb,"path\name",accessmode)
  A(60h) dev_cd_read(fcb,dst,len)
  A(61h) dev_cd_close(fcb)
  A(62h) dev_cd_firstfile(fcb,"path\name",direntry)
  A(63h) dev_cd_nextfile(fcb,direntry)
  A(64h) dev_cd_chdir(fcb,"path")
  A(65h) dev_card_open(fcb,"path\name",accessmode)
  A(66h) dev_card_read(fcb,dst,len)
  A(67h) dev_card_write(fcb,src,len)
  A(68h) dev_card_close(fcb)
  A(69h) dev_card_firstfile(fcb,"path\name",direntry)
  A(6Ah) dev_card_nextfile(fcb,direntry)
  A(6Bh) dev_card_erase(fcb,"path\name")
  A(6Ch) dev_card_undelete(fcb,"path\name")
  A(6Dh) dev_card_format(fcb)
  A(6Eh) dev_card_rename(fcb1,"path\name1",fcb2,"path\name2")
  A(6Fh) ?   ;card ;[r4+18h]=00000000h  ;card_clear_error(fcb) or so
  A(96h) AddCDROMDevice()
  A(97h) AddMemCardDevice()
  A(98h) AddDuartTtyDevice()   ;PS2: SystemError
  A(99h) add_nullcon_driver()
  B(47h) AddDrv(device_info)  ;subfunction for AddXxxDevice functions
  B(48h) DelDrv(device_name_lowercase)
  B(5Bh) ChangeClearPAD(int)   ;pad AND card (ie. used also for Card)
  C(15h) _cdevinput(circ,char)
  C(16h) _cdevscan()
  C(17h) _circgetc(circ)    ;uses r5 as garbage txt for _ioabort
  C(18h) _circputc(char,circ)
```

#### Device Names
Device Names are case-sensitive (usually lowercase, eg. "bu" for memory cards).
In filenames, the device name may be followed by a hexadecimal 32bit
non-case-sensitive port number (eg. "bu00:" for selecting the first memory card
slot). Accordingly, the device name should not end with a hexdigit (eg. "usb:"
would be treated as device "us" with port number 0Bh).<br/>
Standard device names are "cdrom:", "bu00:", "bu10:", "tty00:". Other,
nonstandard devices are:<br/>
```
  Castlevania is trying to access an unknown device named "sim:".
  Caetla (a firmware replacement for Cheat Devices) supports "pcdrv:" device.
```



##   BIOS PC File Server
#### DTL-H2000
Below BRK's are internally used in DTL-H2000 BIOS for two devices: "mwin:"
(Message Window) and "sim:" (CDROM Sim).<br/>

#### Caetla Blurb
Caetla (a firmware replacement for Cheat Devices) supports "pcdrv:" device, the
SN systems (=what?) device extension to access files on the drive of the pc.
This fileserver can be accessed by using the kernel functions, with the
"pcdrv:" device name prefix to the filenames or using the SN system calls.<br/>
The following SN system calls for the fileserver are provided. Accessed by
setting the registers and using the break command with the specified field.<br/>
The break functions have argument(s) in A1,A2,A3 (ie. unlike normal BIOS
functions not in A0,A1,A2), and TWO return values (in V0, and V1).<br/>

#### BRK(101h) - PCInit() - Inits the fileserver
No parameters.<br/>

#### BRK(102h) - PCCreat(filename, fileattributes) - Creates a new file on PC
```
  out: V0  0 = success, -1 = failure
       V1  file handle or error code if V0 is negative
```
Attributes Bits (standard MSDOS-style):<br/>
```
  bit0     Read only file (R)
  bit1     Hidden file    (H)
  bit2     System file    (S)
  bit3     Not used       (zero)
  bit4     Directory      (D)
  bit5     Archive file   (A)
  bit6-31  Not used       (zero)
```

#### BRK(103h) - PCOpen(filename, accessmode) - Opens a file on the PC
```
  out: V0  0 = success, -1 = failure
       V1  file handle or error code if V0 is negative
```

#### BRK(104h) - PCClose(filehandle) - Closes a file on the PC
```
  out: V0  0 = success, -1 = failure
       V1  0 = success, error code if V0 is negative
```

#### BRK(105h) - PCRead(filehandle, length, memory\_destination\_address)
```
  out: V0  0 = success, -1 = failure
       V1  number of read bytes or error code if V0 is negative.
```
Note: PCRead does not stop at EOF, so if you set more bytes to read than the
filelength, the fileserver will pad with zero bytes. If you are not sure of the
filelength obtain the filelength by PClSeek (A2=0, A3=2, V1 will return the
length of the file, don't forget to reset the file pointer to the start before
calling PCread!)<br/>

#### BRK(106h) - PCWrite(filehandle, length, memory\_source\_address)
```
  out: V0  0 = success, -1 = failure
       V1  number of written bytes or error code if V0 is negative.
```

#### BRK(107h) - PClSeek(filehandle, file\_offset, seekmode) - Change Filepos
seekmode may be from 0=Begin of file, 1=Current fpos, or 2=End of file.<br/>
```
  out: V0  0 = success, -1 = failure
       V1  file pointer
```



##   BIOS TTY Console (std\_io)
#### A(3Fh) - Printf(txt,param1,param2,etc.) - Print string to console
```
  in:  A0                     Pointer to 0 terminated string
       A1,A2,A3,[SP+10h..]    Argument(s)
```
Prints the specified string to the TTY console. Printf does internally use
"putchar" to output the separate characters (and expands char 09h and
0Ah accordingly).<br/>
The string can contain C-style escape codes (prefixed by "%" each):<br/>
```
  c         display ASCII character
  s         display ASCII string
  i,d,D     display signed Decimal number (d/i=default32bit, D=force32bit)
  u,U       display unsigned Decimal number (u=default32bit, U=force32bit)
  o,O       display unsigned Octal number (o=default32bit, O=force32bit)
  p,x,X     display unsigned Hex number (p=lower/force32bit, x=lower, X=upper)
  n         write 32bit/16bit string length to [parameter] (default32bit)
```
Additionally, following prefixes (inserted between "%" and escape code):<br/>
```
  + or SPC  show leading plus or space character in positive signed numbers
  NNN       fixed width (for padding or so) (first digit must be 1..9) (not 0)
  .NNN      fixed width (for clipping or so)
  *         variable width (using one of the parameters) (negative=ending_spc)
  .*        variable width
  -         force ending space padding (in case of width being specified)
  #         show leading "0x" or "0X" (hex), or ensure 1 leading zero (octal)
  0         show leading zero's
  L         unknown/no effect?
  h,l       force 16bit (h=halfword), or 32bit (l=long/word)
```
The force32bit codes (D,U,O,p,l) are kinda useless since the PSX defaults to
32bit parameters anyways. The force16bit code (h) may be useful as "%hn"
(writeback 16bit value), otherwise it's rather useless, unless signed 16bit
parameters have garbage in upper 16bit, for unsigned 16bit parameters it
doesn't work at all (accidently sign-expands 16bit to 32bit, and then displays
that signed 32bit value as giant unsigned value). Printf supports only octal,
decimal, and hex (but not binary).<br/>

#### A(3Eh) or B(3Fh) - puts(src) - Write string to TTY
```
  in: R4=address of string (terminated by 00h)
```
Like "printf", but doesn't resolve any "%" operands. Empty strings are handled
in a special way: If R4 points to a 00h character then nothing is output (as
one would expect it), but, if R4 is 00000000h then "\<NULL\>" is output
(only that six letters; without appending any CR or LF).<br/>

#### A(3Dh) or B(3Eh) - gets(dst) - Read string from TTY (keyboard input)
```
  in: r4=dst (pointer to a 128-byte buffer) - out: r2=dst (same is incoming r4)
```
Internally uses "getchar" to receive the separate characters (which are
thus masked by 7Fh). The received characters are stored in the buffer, and are
additionally sent back as echo to the TTY via std\_out\_putc.<br/>
The following characters are handled in a special way: 09h (TAB) is replaced by
a single SPC. 08h or 7FH (BS or DEL) are removing the last character from the
buffer (unless it is empty) and send 08h,20h,08h (BS,SPC,BS) to the TTY. 0Dh or
0Ah (CR or LF) do terminate the input (append 00h to the buffer, send 0Ah to
the TTY, which is expanded to 0Dh,0Ah by the std\_out\_putc function, and do then
return from the gets function).<br/>
The sequence 16h,NNh forces NNh to be stored in the buffer (even if NNh is a
special character like 00h..1Fh or 7Fh). If the buffer is full (circa max 125
chars, plus one extra byte for the ending 00h), or if an unknown control code
in range of 00h..1Fh is received without the 16h prefix, then 07h (BELL) is
sent to the TTY.<br/>

#### A(3Bh) or B(3Ch) - getchar() - Read character from TTY
Reads one character from the TTY console, by internally redirecting to
"read(0,tempbuf,1)". The returned character is ANDed by 7Fh (so, to read a
fully intact 8bit character, "read(0,tempbuf,1)" must be used instead of
this function).<br/>

#### A(3Ch) or B(3Dh) - putchar(char) - Write character to TTY
Writes the character to the TTY console, by internally redirecting to
"write(1,tempbuf,1)". Char 09h (TAB) is expanded to one or more SPC
characters, until reaching the next tabulation boundary (every 8 characters).
Char 0Ah (LF) is expanded to 0Dh,0Ah (CR,LF). Other special characters (which
should be handled at the remote terminal side) are 08h (BS, backspace, move
cursor one position to the left), and 07h (BELL, produce a short beep sound).<br/>

#### C(13h) - FlushStdInOutPut()
Closes and re-opens the std\_in (fd=0) and std\_out (fd=1) file handles.<br/>

#### C(1Bh) - KernelRedirect(ttyflag)  ;PS2: ttyflag=1 causes SystemError
Removes, re-mounts, and flushes the TTY device, the parameter selects whether
to mount the real DUART-TTY device (r4=1), or a Dummy-TTY device (r4=0), the
latter one sends any std\_out to nowhere. Values other than r4=0 or r4=1 do
remove the device, but do not re-mount it (which might result in problems).<br/>
Caution: Trying to use r4=1 on a PSX that does not has the DUART hardware
installed causes the BIOS to hang (so one should first detect the DUART
hardware, eg. by writing two different bytes to Port 1F802020h.1st/2nd access,
and the read and verify that two bytes).<br/>

#### Activating std\_io
The std\_io functions can be enabled via C(1Bh) KernelRedirect(ttyflag), the
BIOS is unable to detect the presence of the TTY hardware, by default the BIOS
bootcode disables std\_io by setting the initial KernelRedirect value at
[A000B9B0h] to zero, this is hardcoded shortly after the POST(E) output:<br/>
```
  call    output_post_r4        ;\output POST(E)
  +mov    r4,0Eh                ;/
  mov     r1,0A0010000h         ;\set [0A000B9B0h]=0 ;TTY=dummy/off
  call    reset_cont_d_3        ; and call reset_cont_d_3
  +mov    [r1-4650h],0          ;/
```
assuming that R28=A0010FF0h, the last 3 opcodes of above code can be replaced
by:<br/>
```
  mov     r1,1h                 ;\set [0A000B9B0h]=1 ;TTY=duart/on
  call    reset_cont_d_3        ; and call reset_cont_d_3
  +mov    [r28-4650h-0ff0h],r1  ;/
```
with that patch, the BIOS bootcode (and many games) are sending debug messages
to the debug terminal, via expansion port, see:<br/>
[EXP2 Dual Serial Port (for TTY Debug Terminal)](expansionportpio.md#exp2-dual-serial-port-for-tty-debug-terminal)<br/>
Note: The nocash BIOS automatically detects the DUART hardware, and activates
TTY if it is present.<br/>

#### B(49h) - PrintInstalledDevices()
Uses printf to display the long and short names from the DCB of the currently
installed devices. Doesn't do anything else. There's no return value.<br/>

#### Note
Several BIOS functions are internally using printf to output status
information, timeout, and error messages, etc. So, trying to close the TTY file
handles (fd=0 and fd=1) would cause such functions to work unstable.<br/>



##   BIOS Character Sets
#### B(51h) - Krom2RawAdd(shiftjis\_code)
```
  In: r4  = 16bit Shift-JIS character code
  Out: r2 = address in BIOS ROM of the desired character (or -1 = error)
```
r4 should be 8140h..84BEh (charset 2), or 889Fh..9872h (charset 3).<br/>

#### B(53h) - Krom2Offset(shiftjis\_code)
```
  In: r4  = 16bit Shift-JIS character code
  Out: r2 = offset within charset (without charset base address)
```
This is a subfunction for B(51h) Krom2RawAdd(shiftjis\_code).<br/>

#### Character Sets in ROM (112Kbytes)
The character sets are located at BFC64000h and up, intermixed with some other
stuff:<br/>
```
  BFC64000h  Charset 1 (16x15 pix, letters with accent marks)    (NOT in JAPAN)
  BFC65CB6h  Garbage   (four-and-a-half reverb tables, ioports, printf strings)
  BFC66000h  Charset 2 (16x15 pix, various alphabets, english, greek, etc.)
  BFC69D68h  Charset 3 (16x15 pix, japanese or chinese symbols or so)
  BFC7F8DEh  Charset 4 (8x15 pix, mainly ASCII letters)
  BFC7FE6Fh  Charset 5 (8x15 pix, additional punctuation marks)    (NOT in PS2)
  BFC7FF32h  Version   (Version and Copyright strings)        (NOT in SCPH1000)
  BFC7FF8Ch  Charset 6 (8x15 pix, seven-and-a-half japanese chars) (NOT in PS2)
  BFC80000h  End       (End of 512kBYTE BIOS ROM)
```
Charset 1 (and Garbage) is NOT included in japanese BIOSes (in the SCPH1000
version that region contains uncompressed program code, in newer japanese
BIOSes that regions are zerofilled)<br/>
Charset 1 symbols are as defined in JIS-X-0212 char(2661h..2B77h), and EUC-JP
char(8FA6E1h..8FABF7h).<br/>
Version (and Copyright) string is NOT included in SCPH1000 version (that BIOS
includes further japanese 8x15 pix chars in that region).<br/>
For charset 2 and 3 it may be recommended to use the B(51h)
Krom2RawAdd(shiftjis\_code) to obtain the character addresses. Not sure if that
BIOS function (or another BIOS function) allows to retrieve charset 1, 4, 5,
and 6 addresses?<br/>



##   BIOS Control Blocks
#### Exception Control Blocks (ExCB) (4 blocks of 8 bytes each)
```
  00h 4   ptr to first element of exception chain
  04h 4   not used (zero)
```

#### Event Control Blocks (EvCB) (usually 16 blocks of 1Ch bytes each)
```
  00h 4   class  (events are triggered when class and spec match)
  04h 4   status (0=free,1000h=disabled,2000h=enabled/busy,4000h=enabled/ready)
  08h 4   spec   (events are triggered when class and spec match)
  0Ch 4   mode   (1000h=execute function/stay busy, 2000h=no func/mark ready)
  10h 4   ptr to function to be executed when ready (or 0=none)
  14h 8   not used (uninitialized)
```

#### Thread Control Blocks (TCB) (usually 4 blocks of 0C0h bytes each)
```
  00h 4   status        (1000h=Free TCB, 4000h=Used TCB)
  04h 4   not used      (set to 1000h by OpenTh) (not for boot executable?)
  08h 80h r0..r31       (entries for r0/zero and r26/k0 are unused)
  88h 4   cop0r14/epc   (aka r26/k0 and pc when returning from exception)
  8Ch 8   hi,lo         (the mul/div registers)
  94h 4   cop0r12/sr    (stored/restored by exception, NOT init by OpenTh)
  98h 4   cop0r13/cause (stored when entering exception, NOT restored on exit)
  9Ch 24h not used      (uninitialized)
```

#### Process Control Block (1 block of 4 bytes)
```
  00h 4   ptr to TCB of current thread
```
The PSX supports only one process, and thus only one Process Control Block.<br/>

#### File Control Blocks (FCB) (16 blocks of 2Ch bytes each)
```
  00h 4  status (0=Free FCB) (nonzero=accessmode)
  04h 4  cdrom: disk_id (checksum across path table of the corresponding disk),
         memory card: port number (00h=slot1, 10h=slot2)
  08h 4  transfer address (for dev_in_out function)
  0Ch 4  transfer length  (for dev_in_out function)
  10h 4  current file position
  14h 4  device flags (copy of DCB[04h])
  18h 4  error  ;used by B(55h) - _get_error(fd)
  1Ch 4  Pointer to DCB for the file
  20h 4  filesize
  24h 4  logical block number (start of file) (for cdrom: at least)
  28h 4  file control block number (simply 0..15 for FCB number 0..15)
```

#### Device Control Blocks (DCB) (10 blocks of 50h bytes each)
```
  00h 4   ptr to lower-case short name ("cdrom", "bu", "tty") (or 0=Free DCB)
  04h 4   device flags (cdrom=14h, bu=14h, tty/dummy=1, tty/duart=3)
  08h 4   sector size  (cdrom=800h, bu=80h, tty=1)
  0Ch 4   ptr to upper-case long name  ("CD-ROM", "MEMORY CARD", "CONSOLE")
  10h 4   ptr to init()                                         (TTY only)
  14h 4   ptr to open(fcb,"path\name",accessmode)
  18h 4   ptr to in_out(fcb,cmd)                                (TTY only)
  1Ch 4   ptr to close(fcb)
  20h 4   ptr to ioctl(fcb,cmd,arg)                             (TTY only)
  24h 4   ptr to read(fcb,dst,len)
  28h 4   ptr to write(fcb,src,len)
  2Ch 4   ptr to erase(fcb,"path\name")
  30h 4   ptr to undelete(fcb,"path\name")
  34h 4   ptr to firstfile2(fcb,"path\name",direntry)
  38h 4   ptr to nextfile(fcb,direntry)
  3Ch 4   ptr to format(fcb)
  40h 4   ptr to cd(fcb,"path")                            (CDROM only)
  44h 4   ptr to rename(fcb1,"path\name1",fcb2,"path\name2")
  48h 4   ptr to remove()
  4Ch 4   ptr to testdevice(fcb,"path\name")
```



##   BIOS Versions
#### Kernel Versions
For the actual kernel, there seem to be only a few different versions. Most
PSX/PSone's are containing the version from 1995 (which is kept 1:1 the same in
all consoles; without any PAL/NTSC related customizations).<br/>
```
  28-Jul-1994  "DTL-H2000"                   ;v0.x (pre-retail devboard)
  22-Sep-1994  "CEX-1000 KT-3  by S.O."      ;v1.0 through v2.0
  no-new-date  "CEX-3000 KT-3  by K.S."      ;v2.1 only (old Port 1F801060h)
  04-Dec-1995  "CEX-3000/1001/1002 by K.S."  ;v2.2 through v4.5 (except v4.0)
  29-May-1997  "CEX-7000/-7001 by K.S.    "  ;v4.0 only (new Port 1F801010h)
  17-Jan-2000  "PS compatible mode by M.T."  ;v5.0 (Playstation 2)
```
The date and version string can be retrieved via GetSystemInfo(index).<br/>
The "CEX-7000/-7001" version was only "temporarily" used (when the kernel/gui
grew too large they changed the ROM size from 512K to 1024K; but did then
figure out that they could use a self-decompressing GUI to squeeze everything
into 512K; but they did accidentally still use the 1024K setting) (newer
consoles fixed that and switched back to the old version from 1995) (aside from
the different date/version string, the only changed thing is the opcode at
BFC00000h, which initializes port 1F801010h to BIOS ROM size of 1MB, instead of
512KB; no idea if that BIOS does actually contain additional data?).<br/>
The "CEX-3000 KT-3" version is already almost same as "CEX-3000/1001/1002",
aside from version/date, the only differences are at offset BFC00014h..1Fh, and
BFC003E0h (both related to Port 1F801060h).<br/>

#### Bootmenu/Intro Versions
This portion was updated more often. It's customized for PAL/NTSC displays,
japanese/english language, and (maybe?) region/licence string checks. The
SCPH1000 uses uncompressed Bootmenu/Intro code with "\<S\>" intro, but
without "PS" intro (or, "PS" is shown only on region matches?), newer versions
are using selfdecompressing code, with both intro screens. The GUI in older PSX
models looks like a drawing program for children, the GUI in newer PSX models
and in PSone's looks more like a modernized bathroom furniture, unknown how the
PS2 GUI looks like?<br/>
Games are communicating only with the Kernel, so the differences in the
Bootmenu/Intro part should have little or effect on compatibility (although
some I/O ports might be initialized differently, and although some games might
(accidently) read different (garbage) values from the ROM).<br/>
```
  Ver  CRC32    Used in                      System ROM Version  Kernel
  0.xj 18D0F7D8 DTL-H2000                    (no version string) dtlh2000
  1.0j 3B601FC8 SCPH-1000 and DTL-H1000      (no version string) cex1000
  1.1j 3539DEF6 SCPH-3000 and DTL-H1000H     "1.1 01/22/95"      ""
  2.0a 55847D8C DTL-H1001                    "2.0 05/07/95 A"    ""
  2.0e 9BB87C4B SCPH-1002 and DTL-H1002      "2.0 05/10/95 E"    ""
  2.1j BC190209 SCPH-3500                    "2.1 07/17/95 J"    cex3000
  2.1a AFF00F2F SCPH-1001 and DTL-H1101      "2.1 07/17/95 A"    ""
  2.1e 86C30531 SCPH-1002 and DTL-H1102      "2.1 07/17/95 E"    ""
  2.2j 24FC7E17 SCPH-5000 and DTL-H1200      "2.2 12/04/95 J"    cex3000/100x
  2.2a 37157331 SCPH-1001 and DTL-H1201/3001 "2.2 12/04/95 A"    ""
  2.2e 1E26792F SCPH-1002 and DTL-H1202/3002 "2.2 12/04/95 E"    ""
  2.2v 446EC5B2 SCPH-5903 (VCD, 1Mbyte)      "2.2 12/04/95 J"    ""
  2.2d DECB22F5 DTL-H1100                    "2.2 03/06/96 D"    ""
  3.0j FF3EEB8C SCPH-5500                    "3.0 09/09/96 J"    ""
  3.0a 8D8CB7E4 SCPH-5501/7003               "3.0 11/18/96 A"    ""
  3.0e D786F0B9 SCPH-5502/5552               "3.0 01/06/97 E"    ""
  4.0j EC541CD0 SCPH-7000/9000               "4.0 08/18/97 J"    cex7000
  4.1w B7C43DAD SCPH-7000W                       ...XXX...
  4.1a 502224B6 SCPH-7001/7501/7503/9001     "4.1 12/16/97 A"    cex3000/100x
  4.1e 318178BF SCPH-7002/7502/9002          "4.1 12/16/97 E"    ""
  4.3j F2AF798B SCPH-100  (PSone)            "4.3 03/11/00 J"    ""
  4.4a 6A0E22A0 SCPH-101  (PSone)            "4.4 03/24/00 ..XXX..
  4.4e 0BAD7EA9 SCPH-102  (PSone)            "4.4 03/24/00 E"    ""
  4.5a 171BDCEC SCPH-101  (PSone)            "4.5 05/25/00 A"    ""
  4.5e 76B880E5 SCPH-102  (PSone)            "4.5 05/25/00 E"    ""
  5.0t B7EF81A9 SCPH10000 (Playstation 2)    "5.0 01/17/00 T"    PS compatible
```
The System ROM Version string can be found at BFC7FF32h (except in v1.0).<br/>

v2.2j/a/e use exactly the same GUI as v2.1 (only the kernel was changed). v2.2d
is almost same as v2.2j (but with some GUI patches or so).<br/>
v4.1 and v4.5 use exactly the same GUI code for "A" and "E" regions (the only
difference is the last byte of the version string; which does specify whether
the GUI shall use PAL or NTSC).<br/>
v5.0 is playstation 2 bios (4MB) with more or less backwards compatible kernel.<br/>

#### Character Set Versions
The 16x15 pixel charsets at BFC66000h and BFC69D68h are included in all BIOSes,
however, the 16x15 portion for letters with accent marks at BFC64000h is
included only in non-japanese BIOSes, and in some newer japanese BIOSes (not
included in v4.0j, but they are included in v4.3j).<br/>
The 8x15 pixel charset with characters 21h..7Fh is included in all BIOSes. In
the SCPH1000, this region is followed by additional 8x15 punctuation marks at
char 80h and up, however, this region is missing in PS2 BIOS. Moreover, some
BIOSes include an incomplete 8x15 japanese character set (which ends abruptly
at BF7FFFFFh), in newer BIOSes, some of theses chars are replaced by the
version string at BFC7FF32h, and, the remaining 8x15 japanese chars were
removed in the PS2 BIOS version.<br/>



##   BIOS Patches
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
  254Axxxx sub  r10,xxxxh ;/                  ;30420080 and  r2,80h ;JOY_STAT.7
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
  2529xxxx sub  r9,xxxxh  ;=@@new_data_end    ;30420080 and  r2,80h ;JOY_STAT.7
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
