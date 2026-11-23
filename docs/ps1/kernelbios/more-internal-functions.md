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

C prototypes for the entries above that have a known signature:<br/>
```
  void dev_tty_init(void);                                                   ;A(5Bh)
  int dev_tty_open(struct File *fcb, const char *path, int accessmode);      ;A(5Ch)
  int dev_tty_in_out(struct File *fcb, int cmd);                             ;A(5Dh)
  int dev_tty_ioctl(struct File *fcb, int cmd, int arg);                     ;A(5Eh)
  int dev_cd_open(struct File *fcb, const char *path, int accessmode);       ;A(5Fh)
  int dev_cd_read(struct File *fcb, void *dst, int len);                     ;A(60h)
  struct DirEntry *dev_cd_firstfile(struct File *fcb, const char *path, struct DirEntry *direntry);  ;A(62h)
  struct DirEntry *dev_cd_nextfile(struct File *fcb, struct DirEntry *direntry);  ;A(63h)
  int dev_cd_chdir(struct File *fcb, char *path);                            ;A(64h)
  int dev_cd_close(struct File *fcb);                                        ;A(61h)
  int dev_card_open(struct File *fcb, const char *path, int accessmode);     ;A(65h)
  int dev_card_read(struct File *fcb, void *dst, int len);                   ;A(66h)
  int dev_card_write(struct File *fcb, void *src, int len);                  ;A(67h)
  int dev_card_close(struct File *fcb);                                      ;A(68h)
  struct DirEntry *dev_card_firstfile(struct File *fcb, const char *path, struct DirEntry *direntry);  ;A(69h)
  struct DirEntry *dev_card_nextfile(struct File *fcb, struct DirEntry *direntry);  ;A(6Ah)
  int dev_card_erase(struct File *fcb, const char *path);                    ;A(6Bh)
  int dev_card_undelete(struct File *fcb, const char *path);                 ;A(6Ch)
  int dev_card_format(struct File *fcb);                                     ;A(6Dh)
  int dev_card_rename(struct File *fcb1, const char *path1, struct File *fcb2, const char *path2);  ;A(6Eh)
  int AddCDROMDevice(void);                                                  ;A(96h)
  int AddMemCardDevice(void);                                                ;A(97h)
  int AddDuartTtyDevice(void);                                               ;A(98h)
  int add_nullcon_driver(void);                                              ;A(99h)
  int AddDrv(const struct Device *device_info);                              ;B(47h)
  int DelDrv(const char *device_name_lowercase);                             ;B(48h)
  int ChangeClearPAD(int value);                                             ;B(5Bh)
  void _cdevinput(struct CircularBuffer *circ, int c);                       ;C(15h)
  void _cdevscan(void);                                                      ;C(16h)
  int _circgetc(struct CircularBuffer *circ);                                ;C(17h)
```
A(61h), A(6Ch), C(15h) and C(17h) were read from the retail BIOS (SCPH-7001 v4.1): argument count from the registers read, return from whether v0 is set before the return. A(61h) ignores its argument and returns 0, C(15h) returns nothing. The rest come from nugget and OpenBIOS.<br/>

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
