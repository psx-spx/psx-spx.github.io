#   BIOS Versions
#### Kernel Versions
For the actual kernel, there seem to be only a few different versions. Most
PSX/PSone's are containing the version from 1995 (which is kept 1:1 the same in
all consoles; without any PAL/NTSC related customizations).<br/>
```
  28-Jul-1994  "DTL-H2000"                   ;v0.x (pre-retail devboard)
  22-Sep-1994  "CEX-1000 KT-3  by S.O."      ;v1.0 through v2.0
  no-new-date  "CEX-3000 KT-3  by K.S."      ;v2.1 only (old Port 1F801060h)
  27-Jul-1995  "Konami OS by T.H."           ;Twinkle System
  01-Sep-1995  "Konami OS by T.H."           ;Konami GV, GQ, System 573
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
