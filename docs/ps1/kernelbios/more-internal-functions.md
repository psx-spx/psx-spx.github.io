#   More Internal Functions
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
