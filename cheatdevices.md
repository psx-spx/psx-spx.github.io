#   Cheat Devices
#### Action Replay, GameShark, Gamebuster, GoldFinger, Equalizer (Datel/clones)
The Datel devices exist in various official/cloned hardware revisions, the DB25
connector requires a special Comms Link ISA card (or a "FiveWire" mod for
making it compatible with normal PC parallel ports). Later "PAR3" models are
said to not require Comms Link, and do thus probably work directly with normal
parallel ports).<br/>
[Cheat Devices - Datel I/O](cheatdevices.md#cheat-devices---datel-io)<br/>
[Cheat Devices - Datel DB25 Comms Link Protocol](cheatdevices.md#cheat-devices---datel-db25-comms-link-protocol)<br/>
[Cheat Devices - Datel Chipset Pinouts](cheatdevices.md#cheat-devices---datel-chipset-pinouts)<br/>
[Cheat Devices - Datel Cheat Code Format](cheatdevices.md#cheat-devices---datel-cheat-code-format)<br/>

#### Xplorer/Xploder/X-Terminator (FCD/Blaze)
The FCD/Blaze devices are all same hardware-wise (with some cosmetic PCB
revisions, and with extra SRAM and bigger FLASH installed in some carts). The
DB25 connector can be directly connected to a PC parallel port.<br/>
[Cheat Devices - Xplorer Memory and I/O Map](cheatdevices.md#cheat-devices---xplorer-memory-and-io-map)<br/>
[Cheat Devices - Xplorer DB25 Parallel Port Function Summary](cheatdevices.md#cheat-devices---xplorer-db25-parallel-port-function-summary)<br/>
[Cheat Devices - Xplorer DB25 Parallel Port Command Handler](cheatdevices.md#cheat-devices---xplorer-db25-parallel-port-command-handler)<br/>
[Cheat Devices - Xplorer DB25 Parallel Port Low Level Transfer Protocol](cheatdevices.md#cheat-devices---xplorer-db25-parallel-port-low-level-transfer-protocol)<br/>
[Cheat Devices - Xplorer Versions](cheatdevices.md#cheat-devices---xplorer-versions)<br/>
[Cheat Devices - Xplorer Chipset Pinouts](cheatdevices.md#cheat-devices---xplorer-chipset-pinouts)<br/>
[Cheat Devices - Xplorer Cheat Code Format](cheatdevices.md#cheat-devices---xplorer-cheat-code-format)<br/>
[Cheat Devices - Xplorer Cheat Code and ROM-Image Decryption](cheatdevices.md#cheat-devices---xplorer-cheat-code-and-rom-image-decryption)<br/>

#### FLASH Chips (for both Xplorer and Datel)
[Cheat Devices - FLASH/EEPROMs](cheatdevices.md#cheat-devices---flasheeproms)<br/>

http://gamehacking.org/faqs/hackv500c.html - cheat code formats<br/>
http://doc.kodewerx.org/hacking\_psx.html - cheat code formats<br/>
http://xianaix.net/museum.htm - around 64 bios versions<br/>
http://www.murraymoffatt.com/playstation-xplorer.html - xplorer bioses<br/>

#### Separating between Gameshark and Xplorer Codes
```
  First Digit  Usage
  3,8          Same for Gameshark & Xplorer (for Xplorer: can be encrypted)
  1,2,C,D,E    Gameshark
  4,6,7,9,B,F  Xplorer
  0,5          Meaning differs for Gameshark & Xplorer
  A            Unused
```

Codebreaker<br/>
Megacom Power Replay III Game Enhancer<br/>



##   Cheat Devices - Datel I/O
#### Datel Memory and I/O Map (for PAR2 or so)
```
  1F000000h-1F01FFFFh R/W Flash (first 128K)
  1F020010h           R   Comms Link STB pin state (bit0)
  1F020018h           R   Switch Setting (bit0: 0=Off, 1=On)
  1F040000h-1F05FFFFh R/W Flash (second 128K) + feedback area (see below)
  1F060000h           R   Comms Link data in (byte)
  1F060008h           W   Comms Link data out (byte, pulses ACK to Comms Link)
```

#### Datel PAR1
Original PAR1 might have supported only 128K FLASH (?) if so, the I/O ports are
probably same as above, but without the "second 128K" FLASH area.<br/>

#### Datel PAR3
The PAR3 version is said to work with parallel ports (not needing the Comms
Link IDA card), and said to support more FLASH with bankswitching, so the I/O
ports must work somehow entirely different as described above.<br/>
Some notes from a (poorly translated) japanese document:<br/>
PAR3 Memory:<br/>
```
  1f000000-1f01ffff ROM. Change in bank switching.
  1f020000-1f03ffff ROM. Change in bank switching.
  1f040000-1f05ffff whopping RAM. It is able to use.
  1f060000-1f06003f I/O. Intently mirror to the subsequent 1f07ffff.
```
PAR3 I/O:<br/>
```
  1f060000 for reception. (1f060000 use only.) All bytes same treatment like.
             It is 01h in the state that does not connected anything.
  1f060008 for transmission. (1f060008 use only.) This is ffh in the state
             that does not connected anything.
  1f060010 during data reception it will stand the least significant bit.
             Usually is fe.
  1f060018 state of the push button. In not pressed and fefefefefefefefe,
             it will Ost ffffffffffffffff.
  1f060020 I think 1f060020 unused. It is ffffffffffffffff.
  1f060028 I think 1f060028 unused. It is ffffffffffffffff.
  1f060030 bank switching. 1 put and run-time of the ROM, and changes to the
             3's and the start-up of the ROM.
  1f060038 would be what? It is lbu. Like there is a meaning bits 0 and 1.
             It was fcfcfcfcfcfcfcfc. I think that it is bank cult.
```



##   Cheat Devices - Datel DB25 Comms Link Protocol
#### Boot Command Handler
The Boot Command Handler is executed once at Pre-Boot, and also (at least in
some firmware versions) once before displaying the GUI. Following command(s)
can be sent from PC side:<br/>
```
  Repeatedly send 8bit "W", until receiving "R"
  Repeatedly send 8bit "B", until receiving "W"
  Send 8bit command "X" (upload/exec) or "U" (upload/flash), and receive ECHO
  Send 32bit ADDRESS,  and receive ECHO or "BX" (bad command)
  Send 32bit LENGTH,   and receive ECHO
  Send DATA[LENGTH],   and receive ECHO
  Send 16bit CHECKSUM, and receive ECHO
  (for upload/flash and if checksum was good, PSX will now BURN ADDR,LENGTH)
  Send 16bit DUMMY, and receive "OK"/"BC"/"BF" (okay, bad chksum, bad flash)
  (for upload/exec and if checksum was good, PSX will now CALL ADDR)
  (thereafter, PAR2.0 and up will reboot via jmp BFC00000h)
```
Data is always transferred as byte-pair (send one byte, receive one byte),
16bit/32bit values are transferred MSB first (with ECHO after each byte).<br/>
The upload/exec command is supported by both Datel and Caetla, the upload/flash
command is supported by Datel only (but it's totally bugged in PAR1.99, and
might also have upwards compatiblity issues in later versions, so it's better
to upload a custom flash function via upload/exec instead of using
upload/flash).<br/>
The 16bit checksum is all DATA[len] bytes added together, and then ANDed with
0FFFh (ie. actually only 12bit wide).<br/>

#### Menu/Game Command Handler
There must be some further command handler(s) after the Boot Command Handler,
with support for additional cheat related commands, and (at least in Caetla)
with support for uploading EXE files with Kernel functions installed (the Boot
Command Handler at Pre-Boot time can also upload EXE code, but doesn't have
Kernel installed).<br/>
Original Datel commands for Menu/Game mode are unknown. The Caetla commands are
documented in japanese, and there are also two english translations:<br/>
http://www.psxdev.net/forum/viewtopic.php?f=49&t=370 - good (though
incomplete)<br/>
http://www.psxdev.net/forum/viewtopic.php?f=53&t=462#p6849 - very bad
(beware)<br/>



##   Cheat Devices - Datel Chipset Pinouts
There appear to be numerous Datel hardware revisions (and possibly numerous
Datel clones). So this chapter is unlikely to cover all hardware revisions.<br/>
```
 PSX Expansion cards:
  PCB              Controller         FLASH      DB25  spotted by
  DATEL REF 1215   GAL + 74HC245      128K+128K  yes   Type79
  DATEL REF 1288   DATEL ASIC1        256K       yes   nocash
  DATEL xxx?       GAL + PIC + HC245  128K       yes   CharlesMacD
  noname?          GAL + 74HC245      256K+0K    yes   Type79
  DATEL REF 1324   lots of chips?     lots?      no    CyrusDevX
  DATEL REF 1326   lots of chips?     lots?      yes   Type79
  PS-121 ZISAN     GAL + PIC? + HC245 128K       yes   Kryptonick
 Comms Link ISA cards:
  PCB                              Chipset                     spotted by
  DATEL COMMS LINK, XXX?           blurry SMD chipset?         lowres photo
  DATEL REF 1113, IBM SATURN LINK  1x74HC74, 2x74HC373, 1xXXX? Type79
  EMS, PCCOM                       1x74HC74, 2x74HC373, 1xXXX? jokergameth
 DIY Alternatives to Comms Link
  FiveWire    ;simple hardware mod for use with parallel ports, for SPP/EPP
  FreeWing    ;parallel port adaptor, lots of 74xxx TTL chips, for SPP/EPP
  ExStand     ;parallel port adaptor, lots of 74xxx TTL chips, for EPP
  CommLinkUSB ;USB adaptor, Buy-and-Diy technology (adafruit/teensy based)
```

#### DATEL REF1288 board (with DATEL ASIC1 chip)
The ASIC1 chip is found in this hardware:<br/>
```
  Label: "EQUALIZER, EVEN THE ODDS" (sticker on outside of case)
  Case:  "DATEL ENGLAND" (printed inside of case)
  PCB:   "DATEL REF1288 SONY SONYPSX2meg"
  U:  44pin "DATEL, ASIC1, A8B1944A, 9832"       ;custom logic chip
  U:  32pin "SST, 29EE020, 150-4C-NH, 981918-D"  ;256Kx8 EEPROM
  U:  8pin  "83BA, LM78L, 05ACM"                 ;5V voltage regulator
  CN: 25pin DB25 connector (for Comms Link ISA card)
  CN: 68pin PSX expansion port connector
  SW: 3pin  Switch
```
The ASIC1 is basically same as the PAL/GAL on other boards, with the 74HC245
transceiver intergrated; the ASIC1 is using a 44pin PLCC package, with pin1
being upper-middle, and pin7 being upper-left. Pinouts are:<br/>
```
  7  D0           18 DB25.2.DATA0    29 D0 (same as pin7)    40 A3
  8  D1           19 DB25.3.DATA1    30 EERPROM./WE          41 A4
  9  D2           20 DB25.4.DATA2    31 /WR                  42 /EXP
  10 GND          21 GND             32 GND                  43 GND
  11 D3           22 DB25.5.DATA3    33 /RD                  44 A17
  12 D4           23 DB25.6.DATA4    34 /MODE ("jumper")     1  A18
  13 D5           24 DB25.7.DATA5    35 VCC                  2  GND
  14 VCC          25 VCC             36 DB25.11.ACK          3  VCC
  15 D6           26 DB25.8.DATA6    37 ?                    4  EEPROM./OE
  16 VCC          27 DB25.9.DATA7    38 VCC                  5  DB25.10.STB
  17 D7           28 EEPROM./CS      39 ?                    6  SWITCH
```
D0 is wired to both pin7 and pin29. The /MODE pin is NC (but could be GNDed via
the two solder points in middle of the PCB). The SWITCH has 10K pullup (can can
get GNDed depending on switch setting).<br/>

#### PALCE20V8 Cuthbert Action Replay schematic (from hitmen webpage)
```
  1-NC         8-NC         15-NC                    22-NC
  2-FBIN       9-CPU.A4     16-GNDed                 23-FLASH./WE
  3-CPU.A17    10-CPU./EXP  17-DB25.pin10 (PAR.STB)  24-FBOUT
  4-CPU./WR    11-CPU.A3    18-FLASH./CS             25-FLASH./OE (and BUF.DIR)
  5-CPU./RD    12-CPU.A5    19-DB25.pin11 (PAR.ACK)  26-BUF./EN
  6-CPU.A18    13-SWITCH    20-CPU.D0                27-unused
  7-CPU.A20    14-GND       21-FLASH.A17             28-VCC
```

#### Charles MacDonald Game Shark schematic
```
  1-FBIN       7-CPU.A4.NC?    13-GNDed       19-FLASH./WE
  2-PIC.RC1    8-CPU./EXP.NC?  14-PAR.STB     20-FBOUT
  3-CPU./WR    9-CPU.A3        15-PIC.RA0     21-BUF.DIR
  4-CPU./RD    10-CPU.A2       16-PAR.ACK     22-BUF./OE
  5-CPU.A18    11-SWITCH       17-CPU.D0      23-PIC.RC0
  6-CPU.A17    12-GND          18-FLASH./OE   24-VCC
```
Uhm, schematic shows "PAR.ACK" instead of "BUF.DIR" as transceiver direction?<br/>
The 24pin PAL in Charles schematic does actually seem to be a 28pin PLCC GAL in
actual hardware (which has four NC pins, hence the 24pin notation in the
schematic).<br/>
The three PIC pins connect to a 28pin PIC16C55 microprocessor (unknown
purpose). Most of the PIC pins are NC (apart from the above three signals, plus
supply, plus OSC ... derived from some oscillator located "behind" the DB25
connector?).<br/>

#### Charles MacDonald Gold Finger schematic
```
  1-FBIN       6-CPU.A17       11-CPU.A2     16-FBOUT
  2-SWITCH     7-CPU.A4.NC?    12-PAR.ACK    17-CPU.A20
  3-CPU./WR    8-CPU./EXP.NC?  13-CPU.D0     18-PAR.STB
  4-CPU./RD    9-CPU.A3        14-FLASH./OE  19-BUF./OE
  5-CPU.A18    10-GND          15-FLASH./WE  20-VCC
```
Note: This is a datel clone, without "BUF.DIR" signal (instead, the transceiver
DIR pin is wired to "PAR.ACK"; it's probably functionally same as real datel
hardware, assuming that "PAR.ACK" is only a short pulse during writing; then
reading should be possible anytime else).<br/>

#### Charles MacDonald Comms Link schematic
PAL<br/>
```
  1-/STATUS    7-ISA.A6        13-JP2        19-NC
  2-ISA.A1     8-ISA.A7        14-ISA.A9     20-PCWR
  3-ISA.A2     9-ISA.A8        15-NC         21-/PCRD
  4-ISA.A3     10-ISA.AEN      16-ISA./IOW   22-NC
  5-ISA.A4     11-JP1          17-/IRQ       23-ISA./IOR
  6-ISA.A5     12-GND          18-ISA.D0     24-VCC
```
The JP1/JP2 pins allow to select Port 300h,310h,320h,330h via two jumpers. The
/IRQ pin could be forward to ISA./IRQ2..7 via six jumpers (but the feature is
ununsed and the six jumpers aren't installed at all).<br/>

#### DB25 Connector
```
  Pin  Parallel Port   CommsLink (PC)        cable         PAR (PSX)
  1    /STB    ---->   "strobe" ----.---o-------------o--    -- NC
  2-9  DATA <-/---->   DATA     <-- | --o-------------o-------> DATA
  10   /ACK    <----   "strobe" ----'---o-------------o-------> "strobe"
  11   BUSY    <----   "ack"    <-------o-------------o-------- "ack"
  12   PE      <----   NC       --    --o-------------o--    -- NC
  13   SLCT    <----   NC       --    --o-------------o--    -- NC
  14   /AUTOLF ---->   NC       --    --o-------------o--.  .-- GNDed
  15   /ERROR  <----   NC       --    --o-------------o--.  .-- GNDed
  16   /INIT   ---->   NC       --    --o-------------o--.  .-- GNDed
  17   /SELECT ---->   GNDed    --.  .--o-------------o--.  .-- GNDed
  18-25 GND    -----   GND      --'--'--o-------------o--'--'-- GND
```

#### nocash FiveWire mod (for connecting datel expansion cart to parallel port)
```
  disconnect DB25.pin14,15,16,17 from GND (may require to desolder the DB25)
  repair any GND connections that were "routed through" above pins
  wire DB25.pin1./STB    to DB25.pin10./ACK
  wire DB25.pin16./INIT  to PSX.EXPANSION.pin2./RESET
  wire DB25.pin15./ERROR to PSX.EXPANSION.pin28.A20
  wire DB25.pin13.SLCT   to PSX.EXPANSION.pin62.A21
  wire DB25.pin12.PE     to PSX.EXPANSION.pin29.A22
```



##   Cheat Devices - Datel Cheat Code Format
#### PSX Gameshark Code Format
```
  30aaaaaa 00dd   ;-8bit Write  [aaaaaa]=dd
  80aaaaaa dddd   ;-16bit Write [aaaaaa]=dddd
```
#### Below for v2.2 and up only
```
  D0aaaaaa dddd   ;-16bit/Equal     If dddd=[aaaaaa] then (exec next code)
  D1aaaaaa dddd   ;-16bit/NotEqual  If dddd<>[aaaaaa] then (exec next code)
  D2aaaaaa dddd   ;-16bit/Less      If dddd<[aaaaaa] then (exec next code)
  D3aaaaaa dddd   ;-16bit/Greater   If dddd>[aaaaaa] then (exec next code)
  E0aaaaaa 00dd   ;-8bit/Equal      If dd=[aaaaaa] then (exec next code)
  E1aaaaaa 00dd   ;-8bit/NotEqual   If dd<>[aaaaaa] then (exec next code)
  E2aaaaaa 00dd   ;-8bit/Less       If dd<[aaaaaa] then (exec next code)
  E3aaaaaa 00dd   ;-8bit/Greater    If dd>[aaaaaa] then (exec next code)
  10aaaaaa dddd   ;-16bit Increment [aaaaaa]=[aaaaaa]+dddd
  11aaaaaa dddd   ;-16bit Decrement [aaaaaa]=[aaaaaa]-dddd
  20aaaaaa 00dd   ;-8bit Increment  [aaaaaa]=[aaaaaa]+dd
  21aaaaaa 00dd   ;-8bit Decrement  [aaaaaa]=[aaaaaa]-dd
```
#### Below for v2.41 and up only
```
  D4000000 dddd   ;-Buttons/If  If dddd=JoypadButtons then (exec next code)
  D5000000 dddd   ;-Buttons/On  If dddd=JoypadButtons then (turn on all codes)
  D6000000 dddd   ;-Buttons/Off If dddd=JoypadButtons then (turn off all codes)
  C0aaaaaa dddd   ;-If/On       If dddd=[aaaaaa] (turn on all codes)
```
#### Below probably v2.41, too (though other doc claims for v2.2)
```
  5000nnbb dddd   ;\Slide Code aka Patch Code aka Serial Repeater
  aaaaaaaa ??ee   ;/for i=0 to nn-1, [aaaaaaaa+(i*bb)]=dddd+(i*??ee), next i
  00000000 0000   ;-Dummy (do nothing?) needed between slides (CD version only)
```
#### Below probably v2.41, too (though other doc claims for ALL versions)
```
  C1000000 nnnn   ;-Delays activation of codes by nnnn (4000-5000 = 20-30 sec)
  C2ssssss nnnn   ;\Copy ssss bytes from 80ssssss to 80tttttt
  80tttttt 0000   ;/
```
#### Below from Caetla .341 release notes
These are probably caetla-specific, not official Datel-codes. In fact, Caetla
.341 itself might be an inofficial hacked version of Caetla .34 (?) so below
might be totally inofficial stuff:<br/>
```
  C3aaaaaa 0000     ;\Indirect 8bit Write  [[aaaaaa]+bbbb]=dd
  9100bbbb 000000dd ;/
  C3aaaaaa 0001     ;\Indirect 16bit Write [[aaaaaa]+bbbb]=dddd (Tomb Raider 2)
  9100bbbb 0000dddd ;/
  C3aaaaaa 0002     ;\Indirect 32bit Write [[aaaaaa]+bbbb]=dddddddd
  9100bbbb dddddddd ;/
  FFFFFFFF 0001     ;-Optional prefix for GameShark 2.2 codes(force non-caetla)
  12aaaaaa dddddddd ;-32bit Increment [aaaaaa]=[aaaaaa]+dddddddd
  22aaaaaa dddddddd ;-32bit Decrement [aaaaaa]=[aaaaaa]-dddddddd
```

#### Notes
A maximum of 30 increment/decrement codes can be used at a time.<br/>
A maximum of 60 conditionals can be used at a time (this includes Cx codes).<br/>
Increment/decrement codes should (must?) be used with conditionals.<br/>
Unknown if greater/less conditionals are signed or unsigned.<br/>
Unclear if greater/less compare dddd by [aaaaaa], or vice-versa.<br/>
Unknown if 16bit codes do require memory alignment.<br/>



##   Cheat Devices - Xplorer Memory and I/O Map
#### Xplorer Memory Map
```
  1F000000h-1F03FFFFh.RW  First 256K of FLASH (fixed mapping)
  1F040000h-1F05FFFFh.RW  Map-able: 2x128K FLASH or 4x128K SRAM (if any)
  1F060000h-1F060007h.xx  I/O Ports
  1F060008h-1F06FFFFh     Mirrors of I/O at 1F060000h..1F060007h
  1F070000h-1F07FFFFh     Unused (open bus)
```
FLASH can be 256Kbyte (normal), or 512Kbyte (in FX versions). When programming
FLASH chips: Observe that the carts can be fitted with chips from different
manufacturers, and, Xplorer carts can have either one or two 256K chips, or one
512K chip.<br/>
SRAM can be 0Kbyte (normal/none), or 128Kbyte (in FX versions). The PCB
supports max 512K SRAM (but there aren't any carts having that much memory
installed).<br/>

#### Xplorer I/O Map
```
  1F005555h.W  FLASH Cmd 1st/3rd byte ;\for first FLASH chip
  1F002AAAh.W  FLASH Cmd 2nd byte     ;/
  1F045555h.W  FLASH Cmd 1st/3rd byte ;\for 2nd FLASH chip (if any)
  1F042AAAh.W  FLASH Cmd 2nd byte     ;/
  1F060000h.R  I/O - Switch Setting (bit0: 0=Off, 1=On)
  1F060001h.R  I/O - 8bit Data from PC (bit0-7)
  1F060001h.W  I/O - 8bit Latch (Data to PC, and Memory Mapping)
                 0  DB25.pin13.SLCT   ;\
                 1  DB25.pin12.PE     ; used for data to PC
                 2  DB25.pin11.BUSY   ;/
                 3  DB25.pin10./ACK   ;-used for handshake to PC
                 4  Memory Mapping (0=EEPROM, 1=SRAM)
                 5  Memory Mapping (EEPROM A17 when A18=1)
                 6  Memory Mapping (SRAM A17 or SRAM CE2)
                 7  Memory Mapping (SRAM A18 or NC)
  1F060002h.R  I/O - Handshake from PC (bit0)   (DB25.pin17./SEL)
  1F060005h.W  I/O - Unknown (used by Xplorer v4.52, set to 03h)
  1F060006h.R  I/O - Unknown (used by Xplorer v4.52, bit0 used)
  1F060007h.R  I/O - Unknown (used by Xplorer v4.52, bit0 used)
```



##   Cheat Devices - Xplorer DB25 Parallel Port Function Summary
#### Xplorer Parallel Port Commands (from PC side)
```
  GetByteByAddr32       Tx(5702h,Addr32), Rx(Data8)
  OldMenuBuReadFile     Tx(5703h), TxFilename, RxDataFFEEh
  OldMenuBuDeleteFile   Tx(5704h), TxFilename
  OldMenuBuWriteFile    Tx(5705h), TxFilename, TxFiledata
  OldMenuBuGetFileHdr   Tx(5706h), TxFilename, Rx(00h,00h), RxTurbo, Rx(02h)
  OldMenuBuOpenEvents   Tx(5707h)
  SetCop0Breakpoint     Tx(5708h,Addr32,Mask32,Ctrl32)   ;Menu: Dummy?
  OldMenuBuCopyFile     Tx(5709h), TxFilename  ;to other memcard
  OldMenuBuFormat       Tx(570Ah,Port8)
  OldMenuBuGetStatus2x  Tx(570Bh), Rx(Stat8,Stat8)  ;\different in old/new
  NewMenuBuGetStatus1x  Tx(570Bh,Port8), Rx(Stat8)  ;/
  MenuGetSetFlag        Tx(570Ch), Rx(Flag8)   ;get old flg, then set flg=01h
  NewMenuBuReadSector   Tx(570Dh,Port8,Sector16), Rx(Data[80h])
  NewMenuBuWriteSector  Tx(570Eh,Port8,Sector16,Data[80h])
  NewRawExecute         Tx(570Fh,Addr32)                 ;call Addr
  MidMenuBuggedExecJump Tx(5710h,ORra32,ORgp32,ORsp32,pc32) ;aka r31,r28,r29,pc
  MidMenuSendComment    Tx(5711h,Len8,AsciiMessage[Len])
  NewMenuFillVram       Tx(5712h,Xloc32,Yloc32,Xsiz32,Ysiz32,FillValue32)
  NewGetVram            Tx(5713h,Xloc32,Yloc32), Rx(Data[800h]) ;32x32pix
  NewGetSetIrqMask      Tx(5714h), Rx(OldMask16), Tx(NewMask16) ;Menu: Dummy
  NewSetVram            Tx(5715h,Xloc8,Yloc8,Data[800h]) ;X/Y=div32 ;32x32pix
  NewMenuGetFlgAndOrVal Tx(5716h), Rx(00h, or 01h,Val32)             ;\
  NewMenuGetTwoValues   Tx(5717h), Rx(Val32,Val32)                   ;
  NewMenu...            Tx(5718h), ...                               ;
  NewMenuGet2kGarbage   Tx(5719h,Dummy32), Rx(Garbage[800h])         ; whatever
  NewMenuGetSomeValue   Tx(571Ah), Rx(Val32)                         ;
  NewMenu...            Tx(571Bh,Data[4])  ;similar to 5763h         ;
  NewMenuNoLongerSupp.  Tx(571Ch)    ;probably WAS supported someday ;/
  GameAddCheatCode      Tx(5741h,Addr32,Data16), Rx(Index8)
  MenuReBootKernel      Tx(5742h)              ;jumps to BFC00000h
  GameDelCheatCode      Tx(5744h,Index8)
  GetMem                Tx(5747h,Addr32,Len32), Rx(Data[Len]), TxRxChksum
  Lock/Freeze           Tx(574Ch)
  OldMenuBuGetDirectory Tx(574Dh), RxTurbo
  MenuTestDB25Handshake Tx(574Eh), ...
  MenuOptimalGetMem     Tx(574Fh,Addr32,Len32), RxFaster(Data[Len]), TxRxChksum
  OldMenuGetWhatever    Tx(5750h), RxDataFFEEh                       ;-whatever
  Release/Unfreeze      Tx(5752h)
  SetMem                Tx(5753h,Addr32,Len32,Data[Len]), TxRxChksum
  TurboGetMem           Tx(5754h,Addr32,Len32), RxFast(Data[Len]), TxRxChksum
  MenuSetMemAndBurnFirm Tx(5755h,Addr32,Len32,Data[Len]), TxRxChksum ;burnFlash
  GetStateGameOrMenu    Tx(5757h), Rx(47h=Game, or 58h=Menu)
  SetMemAndExecute      Tx(5758h,Addr32,Len32,Data[Len]), TxRxChksum ;call Addr
  NewMenu...            Tx(5763h,Val32)    ;similar to 571Bh         ;-whatever
  GetByteByAddr24       Tx(5767h,Addr24), Rx(Data8)
  NewMenuBuggedExecJump Tx(577Ah,ORra32,ORgp32,ORsp32,pc32)  ;formerly 5710h
  NewMenuFlashAndReboot Tx(57C7h,Dest32,Len32,DataXorD3h[Len])
```
Function names starting with "Game/Menu" and/or "New/Mid/Old" are working only
in Game/Menu mode, or only in New/Old xplorer firmware versions (new commands
exist in v4.52, old commands exist in v1.091, mid commands exist in v2.005, but
neither in v1.091 nor v4.52, unknown when those new/mid/old commands have been
added/removed exactly, in which specific versions).<br/>

The only useful command is SetMemAndExecute, which works in ALL versions, and
which can be used to do whatever one wants to do (unfortunately, most of the
official & inoffical tools are relying on other weird commands, which are
working only with specific xplorer firmware versions).<br/>



##   Cheat Devices - Xplorer DB25 Parallel Port Command Handler
The command handler is called once and then during booting, during xplorer GUI,
and during Game execution.<br/>
Each call to the command handler does allow to execute ONLY ONE command,
however, the "Freeze" command can be used to force the xplorer to stay in the
command handler, so one can send MORE commands, until leaving the command
handler by sending the "Unfreeze" command.<br/>
The command handling can vary depending on current boot phase (see below
cautions on Pre-Boot, Mid-Boot, and In-Game phases).<br/>

#### Pre-Boot Handler
This is called shortly after the kernel has done some basic initialization, and
after the xplorer has relocated its EEPROM content to RAM (which means it may
called about a second after reset when using official PSX kernel and Xplorer
Firmware).<br/>
```
  OLD Explorer Firmware: Call command handler ONCE (in MENU mode)
  NEW Explorer Firmware: Call command handler TWICE (in MENU mode)
  if SWITCH=ON or [80000030h]="WHB." then
    NEW Explorer Firmware: Call command handler ONCE AGAIN (in MENU mode)
    Install Mid-Boot hook
  endif
```
Observe that the Kernel function vectors at A0h, B0h, and C0h aren't installed
at this point. If you want to upload an EXE with Kernel vectors installed: send
THREE dummy commands (eg. Unfreeze) to skip the above early command handling.
On the other hand, the ReBootKernel command can be used if you WANT to upload
something during Pre-Boot (the ReBootKernel command works only in MENU mode
though, ie. during Xplorer GUI, but not during Game).<br/>

#### Mid-Boot Handler (Xplorer GUI)
The Xplorer GUI is called only if the Pre-Boot handler has installed it (eg. if
the SWITCH was ON). The handler is called alongsides with joypad reading (which
does NOT take place during the Xplorer intro, so there will be a long dead spot
between Pre-Boot and Mid-Boot command handling).<br/>
```
  Call command handler ONCE (in MENU mode) alongsides with each joypad read
```
Observe that the GUI may have smashed various parts of the Kernel
initialization, so you can upload EXE files, and can use Kernel functions, but
the EXE won't get booted in same state as when booting from CDROM. The boot
state can also vary dramatically depending on the Xplorer Firmware version.<br/>

#### Post-Boot Handler (at start of CDROM booting)
This is called when starting CDROM booting.<br/>
```
  Install GAME mode hook for the B(17h) ReturnFromException() handler
  OLD Explorer Firmware: Call command handler ONCE (still in MENU mode)
  NEW Explorer Firmware: Call command handler ONCE (already in GAME mode)
```

#### In-Game Handler (after CDROM booting) (...probably also DURING booting?)
This is called via the hooked B(17h) ReturnFromException() handler.<br/>
```
  if SWITCH=ON
    Call command handler ONCE (in GAME mode) upon each B(17h)
    And, process game cheat codes (if any) upon each B(17h)
  endif
```
Observe that GAME mode doesn't support all commands. And, above will work only
if the game does use B(17h), eg. when using non-kernel exception handling, or
if it has crashed, or disabled exceptions. Some internal kernel functions are
using ReturnFromException() directly (without going through the indirect B(17h)
function table entry; so the hook cannot trap such direct returns).<br/>



##   Cheat Devices - Xplorer DB25 Parallel Port Low Level Transfer Protocol
All 16bit/24bit/32bit parameters are transferred MSB first.<br/>

#### Tx(Data) - transmit data byte(s)
```
  Output 8bit data to DATA0-7     (DB25.pin2-9)        ;-Send Data (D0-D7)
  Output /SEL=HIGH                (DB25.pin17)         ;\Handshake High
  Wait until /ACK=HIGH            (DB25.pin10)         ;/
  Output /SEL=LOW                 (DB25.pin17)         ;\Handshake Low
  Wait until /ACK=LOW             (DB25.pin10)         ;/
```

#### Rx(Data) - receive data byte(s)
```
  Wait until /ACK=HIGH            (DB25.pin10)         ;\
  Get 3bit from SLCT,PE,BUSY      (DB25.pin13,12,11)   ; 1st Part (D6,D7,HIGH)
  Output /SEL=HIGH                (DB25.pin17)         ;/
  Wait until /ACK=LOW             (DB25.pin10)         ;\
  Get 3bit from SLCT,PE,BUSY      (DB25.pin13,12,11)   ; 2nd Part (D3,D4,D5)
  Output /SEL=LOW                 (DB25.pin17)         ;/
  Wait until /ACK=HIGH            (DB25.pin10)         ;\
  Get 3bit from SLCT,PE,BUSY      (DB25.pin13,12,11)   ; 3rd Part (D0,D1,D2)
  Output /SEL=HIGH                (DB25.pin17)         ;/
  Wait until /ACK=LOW             (DB25.pin10)         ;\4th Part (ver,LOW,LOW)
  Get 3bit from SLCT,PE,BUSY      (DB25.pin13,12,11)   ;  (ver=LOW  for v1.091)
  Output /SEL=LOW                 (DB25.pin17)         ;/ (ver=HIGH for v4.52)
  Wait until all 4bits LOW        (DB25.pin13,12,11,10);-xlink95 fails if not
```

#### RxFast(Data) for TurboGetMem - slightly faster than normal Rx(Data)
First, for invoking the Turbo transfer:<br/>
```
  Wait for BUSY=LOW               (DB25.pin11)
  Output DATA = 00h               (DB25.pin2-9)
  Wait for BUSY=HIGH              (DB25.pin11)
  Output DATA = ECh               (DB25.pin2-9)
```
Thereafter, receive the actual Data byte(s) as so:<br/>
```
  Wait for /ACK transition        (DB25.pin10)         ;\
  Get 3bit from SLCT,PE,BUSY      (DB25.pin13,12,11)   ; 1st Part (D6,D7,LOW)
  Output DATA = 02h               (DB25.pin2-9)        ;/
  Wait for /ACK transition        (DB25.pin10)         ;\
  Get 3bit from SLCT,PE,BUSY      (DB25.pin13,12,11)   ; 2nd Part (D3,D4,D5)
  Output DATA = 04h               (DB25.pin2-9)        ;/
  Wait for /ACK transition        (DB25.pin10)         ;\
  Get 3bit from SLCT,PE,BUSY      (DB25.pin13,12,11)   ; 3rd Part (D0,D1,D2)
  Output DATA = 01h               (DB25.pin2-9)        ;/
```
The /ACK transitions can be sensed by polling the parallel port IRQ flag on PC
side.<br/>

#### RxFaster(Data) for OptimalGetMem - much faster than normal Rx(Data)
First, for invoking the Turbo transfer:<br/>
```
  Output DATA = 00h  ;<-- crap    (DB25.pin2-9)        ;-BUGGY, but REQUIRED
```
Thereafter, receive the actual Data byte(s) as so:<br/>
```
  Get 4bit from SLCT,PE,BUSY,/ACK (DB25.pin13,12,11,10);\1st Part (D4,D5,D6,D7)
  Output DATA = 00h               (DB25.pin2-9)        ;/
  Get 4bit from SLCT,PE,BUSY,/ACK (DB25.pin13,12,11,10);\2nd Part (D0,D1,D2,D3)
  Output DATA = 01h               (DB25.pin2-9)        ;/
```
BUG: The first received byte will be garbage with upper and lower 4bit both
containing the lower 4bits (the bugged firmware does explicitely want DATA=00h
before transfer, although DATA=00h is also 'confirming' that the upper 4bit can
be 'safely' replaced by lower 4bit).<br/>

#### TxRxChksum for SetMem/GetMem functions
```
  Tx(chkMsb), Rx(chkMsb), Tx(chkLsb), Rx(chkLsb), Rx("OK" or "CF" or "BG")
```
The 16bit checksum is all bytes in Data[Len] added together. The two final
response bytes should be "OK"=Okay, or, if the transmitted chksum didn't match,
either "CF"=ChecksumFail (for SetMem functions) or "BG"=BadGetChecksum (for
GetMem functions). MenuSetMemAndBurnFirm is a special case with three response
codes: "OF"=FlashOkay, "CF"=ChecksumFail, "FF"=FlashWriteFail.<br/>

#### TxFilename for Memcard (bu) functions
```
  Rx(Addr32), Tx(Addr32,Len32,Data[Len]), TxRxChksum
```
This is internally using the standard "SetMem" function; preceeded by
Rx(Addr32). Whereas Addr is the target address for the filename (just pass the
Rx'ed address to the Tx part), Len should be max 38h, Data should be the
filename with ending zero (eg. "bu10:name",00h).<br/>

#### TxFiledata for Memcard (bu) WriteFile
```
  Rx(Filename[26h])                       ;-name from TxFilename, echo'ed back
  Rx(Addr32)                              ;-buffer address for fragments
  Tx(NumFragments8)                       ;-number of fragments
  Tx(Addr32,Len32,Data[Len]), TxRxChksum  ;<-- repeat this for each fragment
  Rx(FileHandle8)                         ;-ending dummy byte (filehandle)
```
This is also using the standard "SetMem" function, plus some obscure extra's.
The filedata is split into fragments, Len should be max 2000h per fragment.<br/>

#### RxDataFFEEh for Memcard (bu) ReadFile and GetWhatever
```
  Rx(FFEEh,"W",Len32,Data[Len]  ;<-- can be repeated for several fragments
  Rx(FFEEh,"CA")                ;<-- End Code (after last fragment)
```
Memcard ReadFile does transfer N fragments of Len=2000h (depending on
filesize). The GetWhatever function transfers one fragment with Len=80h,
followed by N\*6 fragments with Len=40Ah.<br/>

#### RxTurbo for Memcard (bu) GetDirectory/GetFileHeader functions
```
  Rx(Addr32), Tx(Addr32,Len32), RxFast(Data[Len]), TxRxChksum
```
This is internally using the standard "TurboGetMem" function; preceeded by
Rx(Addr32). Whereas Addr is the source address of the actual data (just pass
the Rx'ed address to the Tx part).<br/>
For GetDirectoy, Len should be max 800h (actual/data data is only 4B0h bytes,
ie. 258h bytes per memcard, aka 28h bytes per directory entry). For
GetFileHeader, Len should be max 80h.<br/>



##   Cheat Devices - Xplorer Versions
#### Xplorer names
```
  Xploder (Germany/USA)
  Xplorer (England/Spain/Netherlands)
  X-Terminator (Japan)
```

#### Xplorer suffices
```
  V1/V2/V3  normal boards   (256K EEPROM, no SRAM, no DB25 resistor)
  FX/DX     extended boards (512K EEPROM, 128K SRAM, with DB25 resistor)
  PRO       meaningless suffix
```
The V1/V2/V3 suffix does just indicate the pre-installed firmware version (so
that suffices become meaningless after software upgrades).<br/>
The FX suffix (or DX in japan) indicates that the PCB contains more memory and
an extra resistor (the memory/resistor are intended for use with the "X-Assist"
add-on device).<br/>

#### Xplorer PCB types
```
  1) PXT6     ;original board
  2) Nameless ;with alternate solder pads for smaller SRAM/GAL
  3) PXT6-3   ;with alternate solder pads for smaller SRAM/GAL and 2nd EEPROM
```

#### Xplorer Compatibility Issues
The three PCB versions are functionally identical, and do differ only by
cosmetic changes for alternate/smaller chip packages.<br/>
However, some things that can make difference in functionality are the
installed components and installed firmware version:<br/>
```
 - FX carts have some extra components & more memory installed.
   (needed for "bigger" firmwares, mainly needed for the X-Assist add-on)
 - FLASH chips from different manufacturers can occassionally cause problems
   (eg. older software not knowing how to program newer FLASH chips).
 - DB25 transfer protocol has some changed commands in each firmware version
   (and most transfer tools tend to rely on such commands, so most tools will
   fail unless the cart is flashed with a certain firmware version).
```

#### X-Assist add-on for Xplorer carts
The X-Assist is a quity huge clumsy controller with DPAD, plus 4 buttons, plus
small LCD screen. The thing connects to the Xplorer's DB25 connector, allowing
to enter/search cheat codes without using a PC.<br/>
The device works only with "FX" Xplorer boards (which contain an extra resistor
for outputting supply power on the DB25 connector, plus more memory which is
somewhat intended for use by the X-Assist thing).<br/>



##   Cheat Devices - Xplorer Chipset Pinouts
#### Xplorer Pinout GAL20V8 (generic array logic)
```
  1  IN0  (DB25.pin17./SEL)
  2  IN1  (PSX.pin14.A0)
  3  IN2  (PSX.pin48.A1)
  4  IN3  (PSX.pin15.A2)
  5  IN4  (74373.pin15.Q5)
  6  IN5  (PSX.pin4./EXP)
  7  IN6  (74373.pin12.Q4)
  8  IN7  (PSX.pin26.A16) (EEPROM.pin2.A16) (SRAM.pin2.A16) (10000h)
  9  IN8  (PSX.pin60.A17)                                   (20000h)
  10 IN9  (PSX.pin27.A18) (EEPROM.pin1.A18 or NC)           (40000h)
  11 IN10 (PSX.pin30./RD)
  12 GND
  ---
  13 IN11 (GND)
  14 IN12 (/SWITCH_ON)
  15 IO   (74373.pin11.LE)
  16 IO   (PSX.pin6.D0)
  17 IO   (SRAM./CE.pin22)
  18 IO   (EEPROM2./CE.pin22) (for 2nd EEPROM chip, if any)
  19 IO   (EEPROM1./CE.pin22) (for 1st EEPROM chip)
  20 IO   (NC)                       (reportedly has wire?)
  21 IO   (EEPROM.pin30.A17)         (reportedly A14 ?)
  22 IO   (74245.pin19./E)
  23 IN13 (PSX.pin64./WR) (SRAM.29, EEPROM.31)
  24 VCC
```
The GALs are programmed nearly identical for all Xplorer versions, some small
differences are: One or two EEPROM chip selects (depending on EEPROM chipset),
and extra ports at 1F060005h, 1F060006h, 1F060007h (used in v4.52).<br/>
Note: The 28pin PLCC GAL has same pinout as the 24pin chip, but with four NC
pins inserted (at pin 1,8,15,22, whereof, there is a wire routed "through" pin
8, so that pin isn't literally NC).<br/>

#### Xplorer Pinout 74373 (8bit tristate latch)
```
  1  /OE (GND)
  2  Q0  (DB25.pin13.SLCT)
  3  D0  (PSX)
  4  D1  (PSX)
  5  Q1  (DB25.pin12.PE)
  6  Q2  (DB25.pin11.BUSY)
  7  D2  (PSX)
  8  D3  (PSX)
  9  Q3  (DB25.pin10./ACK)
  10 GND
  11 LE  (GAL.pin15.LatchEnable)
  12 Q4  (GAL.pin7)             (0=EEPROM, 1=SRAM)
  13 D4  (PSX)
  14 D5  (PSX)
  15 Q5  (GAL.pin5)             (EEPROM bank 2/3)
  16 Q6  (SRAM.pin30.A17 or CE2)
  17 D6  (PSX)
  18 D7  (PSX)
  19 Q7  (SRAM.pin1.A18 or NC)
  20 VCC
```

#### Xplorer Pinout 74245 (8bit bus transceiver)
```
  1  DIR (GNDed)
  2  D7  (PSX)
  3  D6  (PSX)
  4  D5  (PSX)
  5  D4  (PSX)
  6  D3  (PSX)
  7  D2  (PSX)
  8  D1  (PSX)
  9  D0  (PSX)
  10 GND
  11 D0  (DB25.pin2)
  12 D1  (DB25.pin3)
  13 D2  (DB25.pin4)
  14 D3  (DB25.pin5)
  15 D4  (DB25.pin6)
  16 D5  (DB25.pin7)
  17 D6  (DB25.pin8)
  18 D7  (DB25.pin9)
  19 /E  (GAL.pin22)
  20 VCC
```

#### Xplorer Pinout 7805 (voltage regulator)
```
  1 5V   (VCC)
  2 GND  (GND)
  3 7.5V (PSX.pin18,52)
```

#### Xplorer Pinout SWITCH (on/off)
```
  OFF  NC
  COM  PAL.pin14 (with 10K pull-up to VCC)
  ON   GND
```

#### Xplorer Pinout DB25 (parallel/printer port)
```
  1  In  /STB  (NC)
  2  In  DATA0 (74245.pin11)
  3  In  DATA1 (74245.pin12)
  4  In  DATA2 (74245.pin13)
  5  In  DATA3 (74245.pin14)
  6  In  DATA4 (74245.pin15)
  7  In  DATA5 (74245.pin16)
  8  In  DATA6 (74245.pin17)
  9  In  DATA7 (74245.pin18)
  10 Out /ACK  (74373.Q3)
  11 Out BUSY  (74373.Q2)
  12 Out PE    (74373.Q1)
  13 Out SLCT  (74373.Q0)
  ---
  14 In  /LF   (NC)
  15 Out /ERR  (VCC via 0.47ohm) (installed only on carts with SRAM)
  16 In  /INIT (NC)
  17 In  /SEL  (GAL.IN0.pin1)
  18..25 GND   (Ground)
```

EEPROM.pin1 is NC on 256Kx8 chip (however it is wired to A18 for use with
512Kx8 chips).<br/>
EEPROM.pin30 is A17 from GAL.pin21 (not from PSX.A17), accordingly GAL.pin21 is
EEPROM.A17 (not A14).<br/>
Boards with solder pads for TWO EEPROMs are leaving A18 not connected on the
2nd EEPROM (but do connect A18 to the first EEPROM, so one could either use one
512K chip or two 256K chips).<br/>
DB25.pin15./ERR is VCC via 0.47ohm (installed only on carts with SRAM, intended
as supply for the X-ASSIST thing).<br/>
SRAM (if any) is wired to GAL.pin17 (/CE), 74373.Q6 (A17 or CE2), 74373.Q7 (A18
or NC), other SRAM pins are wired straight to D0-D7, A0-A16, /RD, /WR.<br/>
VCC is 5V, derived from a 7805 voltage converter (with 7.5V used as input).<br/>
Existing boards seem to have 128K SRAM (if any), so SRAM A17/A18 aren't
actually used (unless a board would have 512K SRAM), however, for 128K SRAMs
one should switch SRAM CE2 (aka A17) high.<br/>



##   Cheat Devices - Xplorer Cheat Code Format
#### PSX Xplorer/Xploder Code Format
```
  3taaaaaa 00dd  ;-8bit write  [aaaaaa]=dd
  8taaaaaa dddd  ;-16bit write [aaaaaa]=dddd
  00aaaaaa dddd  ;-32bit write [aaaaaa]=0000dddd  <-- not "0taaaaaa dddd" ?
  4t000000 000x  ;-Slow Motion (delay "x" whatever/ns,us,ms,frames?)
  7taaaaaa dddd  ;-IF [aaaaaa]=dddd then <execute following code>
  9taaaaaa dddd  ;-IF [aaaaaa]<>dddd then <execute following code>
  Ftaaaaaa dddd  ;-IF [aaaaaa]=dddd then activate "other selected" codes (uh?)
  5taaaaaa ?nnn  ;\
  d0d1d2d3 d4d5  ; write "?nnn" bytes to [aaaaaa]  ;ordered d0,d1,d2... ?
  d6d7d8.. ....  ;/
  6t000000 nnnn  ;\COP0 hardware breakpoint
  aaaaaaaa cccc  ; aaaaaaaa=break_address, mmmmmmmm=break_mask
  mmmmmmmm d0d1  ; nnnn=num_bytes (d0,d1,d2,etc.), cccc=break_type (see below)
  d2d3d4.. ....  ;/
  B?nnbbbb eeee  ;\Slide/Patch Code, with unclear end: "end=?nn+/-1" ?
  10aaaaaa dddd  ;/for i=0 to end, [aaaaaa+(i*bbbb)]=dddd+(i*eeee), next i
  C0aaaaaa dddd  ;-garbage/mirror of 70aaaaaa dddd ?  ;\or maybe meant to be
  D0aaaaaa dddd  ;-garbage/mirror of 70aaaaaa dddd ?  ;/same as on GameShark?
```
The second code digit (t) contains encryption type (bit0-2), and a "default
on/off" flag (bit3: 0=on, 1=off; whatever that means, it does probably require
WHATEVER actions to enable codes that are "off"; maybe via the Ftaaaaaa dddd
code).<br/>

#### break\_type (cccc) (aka MSBs of cop0r7 DCIC register)
```
  E180 (instruction gotton by CPU but not yet implemented) (uh, gotton what?)
  EE80 (data to be read or written)  ;<--looks okay
  E680 (data to be read)             ;<--looks okay
  EA80 (data to be wrtten)           ;<--looks okay
  EF80 (instruction)   ;<-- looks crap, should be probably E180
```
The CPU supports one data breakpoint and one instruction breakpoint (though
unknown if the Xplorer does support to use both simultaneously, or if it does
allow only one of them to be used).<br/>
If the break\_type/address/mask to match up with CPU's memory access actions...
then "something" does probably happen (maybe executing a sub-function that
consists of the d0,d1,d2,etc-bytes, if so, maybe at a fixed/unknown memory
address, or maybe at some random address; which would require relocatable
code).<br/>

#### Notes
The "Slide" code shall be used only with even addresses, unknown if other
16bit/32bit codes do also require aligned addresses.<br/>



##   Cheat Devices - Xplorer Cheat Code and ROM-Image Decryption
#### decrypt\_xplorer\_cheat\_code:
```
  key  = x[0] and 07h              ;'''''''' AABBCCDD EEFF '''''''';
  x[0] = x[0] xor key              ;         / / /  \  \ \         ;
  if key=0                         ; x[0] --' / /    \  \ '-- x[5] ;
    ;unencrypted (keep as is)      ; x[1] ---' /      \  '--- x[4] ;
  elseif key=4                     ; x[2] ----'        '----- x[3] ;
    x[1] = x[1] xor (025h)         ;,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,;
    x[2] = x[2] xor (0FAh + (x[1] and 11h))
    x[3] = x[3] xor (0C0h + (x[2] and 11h) + (x[1] xor 12h))
    x[4] = x[4] xor (07Eh + (x[3] and 11h) + (x[2] xor 12h) + x[1])
    x[5] = x[5] xor (026h + (x[4] and 11h) + (x[3] xor 12h) + x[2] + x[1])
  elseif key=5
    x[1] = (x[1] + 057h)  ;"W"ayne
    x[2] = (x[2] + 042h)  ;"B"eckett
    x[3] = (x[3] + 031h)  ;"1"
    x[4] = (x[4] + 032h)  ;"2"
    x[5] = (x[5] + 033h)  ;"3"
  elseif key=6
    x[1] = (x[1] + 0ABh) xor 01h
    x[2] = (x[2] + 0ABh) xor 02h
    x[3] = (x[3] + 0ABh) xor 03h
    x[4] = (x[4] + 0ABh) xor 04h
    x[5] = (x[5] + 0ABh) xor 05h
  elseif key=7
    x[5] = x[5] + 0CBh
    x[4] = x[4] + 0CBh + (x[5] and 73h)
    x[3] = x[3] + 05Ah + (x[4] and 73h) - (x[5] xor 90h)
    x[2] = x[2] + 016h + (x[3] and 73h) - (x[4] xor 90h) + x[5]
    x[1] = x[1] + 0F5h + (x[2] and 73h) - (x[3] xor 90h) + x[4] + x[5]
  else
    error ;(key=1,2,3)
  endif
```

#### decrypt\_xplorer\_fcd\_rom\_image:
```
  for i=0 to romsize-1
    x=45h
    y=(i and 37h) xor 2Ch
    if (i and 001h)=001h then x=x xor 01h
    if (i and 002h)=002h then x=x xor 01h
    if (i and 004h)=004h then x=x xor 06h
    if (i and 008h)=008h then x=x xor 04h
    if (i and 010h)=010h then x=x xor 18h
    if (i and 020h)=020h then x=x xor 30h
    if (i and 040h)=040h then x=x xor 60h
    if (i and 080h)=080h then x=x xor 40h
    if (i and 100h)=100h then x=x xor 80h
    if (i and 006h)=006h then x=x xor 0ch
    if (i and 00Eh)=00Eh then x=x xor 08h
    if (i and 01Fh)>=016h then x=x-10h
    rom[i]=(rom[i] XOR x)+y
  next i
```



##   Cheat Devices - FLASH/EEPROMs
#### FLASH/EEPROM Commands
Below commands should work on all chips (for write: page size may vary, eg. 1
byte, 128 bytes, or 256 bytes). Some chips do have some extra commands (eg. an
alternate older get id command, or sector erase commands, or config commands),
but those extras aren't needed for basic erase/write operations.<br/>
```
  [5555h]=AAh, [2AAAh]=55h, [5555h]=A0h, [addr..]=byte(s)  ;write page
  [5555h]=AAh, [2AAAh]=55h, [5555h]=90h, id=[0000h..0001h] ;enter id mode
  [5555h]=AAh, [2AAAh]=55h, [5555h]=F0h                    ;exit id mode
  [5555h]=AAh, [2AAAh]=55h, [5555h]=80h                    ;erase chip, step 1
  [5555h]=AAh, [2AAAh]=55h, [5555h]=10h                    ;erase chip, step 2
```
Above addresses are meant to be relative to the chip's base address (ie.
"5555h" would be 1F005555h in PSX expansion ROM area, or, if there are two
flash chips, then it would be 1F045555h for the 2nd chip in xplorer and datel
carts; whereas, that region is using bank switching in xplorer carts, so one
must output some FLASH address bits I/O ports, and the others via normal CPU
address bus; whilst datel carts have noncontinous FLASH areas at 1F000000h and
1F040000h, with a gap at 1F020000h).<br/>
Observe that the chips will output status info (instead of FLASH data) during
write/erase/id mode (so program code using those commands must execute in RAM,
not in FLASH memory).<br/>

#### FLASH/EEPROM Wait Busy
Waiting is required after chip erase and page write (after writing the last
byte at page end), and on some chips it's also required after enter/exit id
mode. Some chips indicate busy state via a toggle bit (bit6 getting inverted on
each 2nd read), and/or by outputting a value different than the written data,
and/or do require hardcoded delays (eg. AM29F040). Using the following 3-step
wait mechanism should work with all chips:<br/>
```
  Wait 10us (around 340 cpu cycles on PSX)   ;-step 1, hardcoded delay
  Wait until [addr]=[addr]                   ;-step 2, check toggle bit
  Wait until [addr]=data                     ;-step 3, check data
```
Whereas, "addr" should be the last written address (or 0000h for erase and
enter/exit id mode). And "data" should be the last written data (or FFh for
erase, or "don't care" for enter/exit id mode).<br/>

#### Board and Chip Detection
First of, one should detect the expansion board type, this can be done as so:<br/>
```
  Enter Chip ID mode (at 1F000000h)
  Compare 400h bytes at 1F000000h vs 1F020000h
  If different --> assume Datel PAR1/PAR2 hardware
  If same --> assume Xplorer hardware (or Datel PAR3, whatever that is)
  Exit Chip ID mode (at 1F000000h)
```
Next, detect the Chip ID for the (first) FLASH chip:<br/>
```
  Enter Chip ID mode (at 1F000000h)
  Read the two ID bytes (at 1F00000xh)
  Exit Chip ID mode (at 1F000000h)
```
Finally, one needs to check if there's a second FLASH chip, there are two such
cases:<br/>
```
  If cart=xplorer AND 1st_chip=256K --> might have a 2nd 256K chip
  If cart=datel   AND 1st_chip=128K --> might have a 2nd 128K chip
```
In both cases, the 2nd chip would be mapped at 1F400000h, and one can test the
following four combinations:<br/>
```
  Enter Chip ID (at 1F000000h) and Enter Chip ID (at 1F400000h) ;id1+id2
  Exit  Chip ID (at 1F000000h) and Enter Chip ID (at 1F400000h) ;id2
  Exit  Chip ID (at 1F400000h) and Enter Chip ID (at 1F000000h) ;id1
  Exit  Chip ID (at 1F400000h) and Exit  Chip ID (at 1F000000h) ;none
```
For each combination compare 400h bytes at 1F000000h vs 1F400000h.<br/>
```
  If they are all same --> there is only one chip (mirrored to both areas)
  If different --> 1F400000h is either garbage, or a 2nd chip
```
In the latter case, do Chip ID detection at 1F400000h to see if there's really
another chip there, and which type it is (if present, then it should be usually
the same type as the 1st chip; and if it's not present, then there might be
just open bus garbage instead of valid ID values).<br/>

#### FLASH/EEPROM Chip IDs
```
  ChipID  Kbyte Page Maker/Name         ;notes
  1Fh,D5h 128K  128  ATMEL AT29C010A    ;xplorer/prototypes?
  1Fh,35h 128K  128  ATMEL AT29LV010A   ;-
  1Fh,DAh 256K  256  ATMEL AT29C020     ;xplorer
  1Fh,BAh 256K  256  ATMEL AT29BV020    ;xplorer
  1Fh,A4h 512K  256  ATMEL AT29C040A    ;xplorer
  1Fh,C4h 512K  256  ATMEL AT29xV040A   ;-
  BFh,07h 128K  128  SST SST29EE010     ;-
  BFh,08h 128K  128  SST SST29xE010     ;-
  BFh,22h 128K  128  SST SST29EE010A    ;-
  BFh,23h 128K  128  SST SST29xE010A    ;-
  BFh,10h 256K  128  SST SST29EE020     ;xplorer
  BFh,12h 256K  128  SST SST29xE020     ;xplorer
  BFh,24h 256K  128  SST SST29EE020A    ;-
  BFh,25h 256K  128  SST SST2xEE020A    ;-
  BFh,04h 512K  256  SST SST28SF040     ;said to be used in "AR/GS Pro"
  DAh,C1h 128K  128  WINBOND W29EE01x   ;-
  DAh,45h 256K  128  WINBOND W29C020    ;-
  DAh,46h 512K  256  WINBOND W29C040    ;xplorer
  01h,A4h 512K    1  AMD AM29F040       ;nocash psone bios (intact console)
  20h,20h 128K    1  ST M29F010B        ;nocash psone bios (broken console)
  31h,B4h 128K   ??  CATALYST CAT28F010 ;NEEDS VPP=12V !!! ("PS-121 ZISAN")
```
The above Atmel/SST/Winbond chips are commonly used in Datel or Xplorer carts
(or both). The CATALYST chip is used in some Datel clones (but seems to require
12 volts, meaning that it can't be properly programmed on PSX, nethertheless,
it's reportedly working "well enough" to encounter flash corruption upon
programming attempts). The two ST/AMD chips aren't really common in PSX world
(except that I've personally used them in my PSones).<br/>



