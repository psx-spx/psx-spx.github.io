#   Event Summary
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
