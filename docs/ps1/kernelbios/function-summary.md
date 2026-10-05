#   Function Summary
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
