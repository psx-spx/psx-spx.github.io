#   Control Blocks
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
