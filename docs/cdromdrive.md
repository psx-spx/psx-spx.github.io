#   CDROM Drive
#### Playstation CDROM I/O Ports
[CDROM Controller I/O Ports](cdromdrive.md#cdrom-controller-io-ports)<br/>

#### Playstation CDROM Commands
[CDROM Controller Command Summary](cdromdrive.md#cdrom-controller-command-summary)<br/>
[CDROM - Control Commands](cdromdrive.md#cdrom---control-commands)<br/>
[CDROM - Seek Commands](cdromdrive.md#cdrom---seek-commands)<br/>
[CDROM - Read Commands](cdromdrive.md#cdrom---read-commands)<br/>
[CDROM - Status Commands](cdromdrive.md#cdrom---status-commands)<br/>
[CDROM - CD Audio Commands](cdromdrive.md#cdrom---cd-audio-commands)<br/>
[CDROM - Test Commands](cdromdrive.md#cdrom---test-commands)<br/>
[CDROM - Secret Unlock Commands](cdromdrive.md#cdrom---secret-unlock-commands)<br/>
[CDROM - Video CD Commands](cdromdrive.md#cdrom---video-cd-commands)<br/>
[CDROM - Mainloop/Responses](cdromdrive.md#cdrom---mainloopresponses)<br/>
[CDROM - Response Timings](cdromdrive.md#cdrom---response-timings)<br/>
[CDROM - Response/Data Queueing](cdromdrive.md#cdrom---responsedata-queueing)<br/>

#### General CDROM Disk Format
[CDROM Disk Format](cdromdrive.md#cdrom-disk-format)<br/>
[CDROM Subchannels](cdromdrive.md#cdrom-subchannels)<br/>
[CDROM Sector Encoding](cdromdrive.md#cdrom-sector-encoding)<br/>
[CDROM XA Subheader, File, Channel, Interleave](cdromdrive.md#cdrom-xa-subheader-file-channel-interleave)<br/>
[CDROM XA Audio ADPCM Compression](cdromdrive.md#cdrom-xa-audio-adpcm-compression)<br/>
[CDROM ISO Volume Descriptors](cdromdrive.md#cdrom-iso-volume-descriptors)<br/>
[CDROM ISO File and Directory Descriptors](cdromdrive.md#cdrom-iso-file-and-directory-descriptors)<br/>
[CDROM ISO Misc](cdromdrive.md#cdrom-iso-misc)<br/>
[CDROM File Formats](cdromdrive.md#cdrom-file-formats)<br/>
[CDROM Video CDs (VCD)](cdromvideocdsvcd.md)<br/>

#### Playstation CDROM Protection
[CDROM Protection - SCEx Strings](cdromdrive.md#cdrom-protection---scex-strings)<br/>
[CDROM Protection - Bypassing it](cdromdrive.md#cdrom-protection---bypassing-it)<br/>
[CDROM Protection - Modchips](cdromdrive.md#cdrom-protection---modchips)<br/>
[CDROM Protection - Chipless Modchips](cdromdrive.md#cdrom-protection---chipless-modchips)<br/>
[CDROM Protection - LibCrypt](cdromdrive.md#cdrom-protection---libcrypt)<br/>

#### General CDROM Disk Images
[CDROM Disk Images CCD/IMG/SUB (CloneCD)](cdromdrive.md#cdrom-disk-images-ccdimgsub-clonecd)<br/>
[CDROM Disk Images CDI (DiscJuggler)](cdromdrive.md#cdrom-disk-images-cdi-discjuggler)<br/>
[CDROM Disk Images CUE/BIN/CDT (Cdrwin)](cdromdrive.md#cdrom-disk-images-cuebincdt-cdrwin)<br/>
[CDROM Disk Images MDS/MDF (Alcohol 120%)](cdromdrive.md#cdrom-disk-images-mdsmdf-alcohol-120)<br/>
[CDROM Disk Images NRG (Nero)](cdromdrive.md#cdrom-disk-images-nrg-nero)<br/>
[CDROM Disk Image/Containers CDZ](cdromdrive.md#cdrom-disk-imagecontainers-cdz)<br/>
[CDROM Disk Image/Containers ECM](cdromdrive.md#cdrom-disk-imagecontainers-ecm)<br/>
[CDROM Subchannel Images](cdromdrive.md#cdrom-subchannel-images)<br/>
[CDROM Disk Images Other Formats](cdromdrive.md#cdrom-disk-images-other-formats)<br/>

#### Playstation CDROM Coprocessor
[CDROM Internal Info on PSX CDROM Controller](cdrominternalinfoonpsxcdromcontroller.md)<br/>



##   CDROM Controller I/O Ports
#### 1F801800h - Index/Status Register (Bit0-1 R/W) (Bit2-7 Read Only)
```
  0-1 Index   Port 1F801801h-1F801803h index (0..3 = Index0..Index3)   (R/W)
  2   ADPBUSY XA-ADPCM fifo empty  (0=Empty) ;set when playing XA-ADPCM sound
  3   PRMEMPT Parameter fifo empty (1=Empty) ;triggered before writing 1st byte
  4   PRMWRDY Parameter fifo full  (0=Full)  ;triggered after writing 16 bytes
  5   RSLRRDY Response fifo empty  (0=Empty) ;triggered after reading LAST byte
  6   DRQSTS  Data fifo empty      (0=Empty) ;triggered after reading LAST byte
  7   BUSYSTS Command/parameter transmission busy  (1=Busy)
```
Bit3,4,5 are bound to 5bit counters; ie. the bits become true at specified
amount of reads/writes, and thereafter once on every further 32 reads/writes.<br/>

#### 1F801801h.Index0 - Command Register (W)
```
  0-7  Command Byte
```
Writing to this address sends the command byte to the CDROM controller, which
will then read-out any Parameter byte(s) which have been previously stored in
the Parameter Fifo. It takes a while until the command/parameters are
transferred to the controller, and until the response bytes are received; once
when completed, interrupt INT3 is generated (or INT5 in case of invalid
command/parameter values), and the response (or error code) can be then read
from the Response Fifo. Some commands additionally have a second response,
which is sent with another interrupt.<br/>

#### 1F801802h.Index0 - Parameter Fifo (W)
```
  0-7  Parameter Byte(s) to be used for next Command
```
Before sending a command, write any parameter byte(s) to this address.<br/>

#### 1F801803h.Index0 - Request Register (W)
```
  0-4 0    Not used (should be zero)
  5   SMEN Want Command Start Interrupt on Next Command (0=No change, 1=Yes)
  6   BFWR ...
  7   BFRD Want Data         (0=No/Reset Data Fifo, 1=Yes/Load Data Fifo)
```

#### 1F801802h.Index0..3 - Data Fifo - 8bit/16bit (R)
After ReadS/ReadN commands have generated INT1, software must set the Want Data
bit (1F801803h.Index0.Bit7), then wait until Data Fifo becomes not empty
(1F801800h.Bit6), the datablock (disk sector) can be then read from this
register.<br/>
```
  0-7  Data 8bit  (one byte), or alternately,
  0-15 Data 16bit (LSB=First byte, MSB=Second byte)
```
The PSX hardware allows to read 800h-byte or 924h-byte sectors, indexed as
[000h..7FFh] or [000h..923h], when trying to read further bytes, then the PSX
will repeat the byte at index [800h-8] or [924h-4] as padding value.<br/>
Port 1F801802h can be accessed with 8bit or 16bit reads (ie. to read a
2048-byte sector, one can use 2048 load-byte opcodes, or 1024 load halfword
opcodes, or, more conventionally, a 512 word DMA transfer; the actual CDROM
databus is only 8bits wide, so CPU/DMA are apparently breaking 16bit/32bit
reads into multiple 8bit reads from 1F801802h).<br/>

#### 1F801801h.Index1 - Response Fifo (R)
#### 1F801801h.Index0,2,3 - Response Fifo (R) (Mirrors)
```
  0-7  Response Byte(s) received after sending a Command
```
The response Fifo is a 16-byte buffer, most or all responses are less than 16
bytes, after reading the last used byte (or before reading anything when the
response is 0-byte long), Bit5 of the Index/Status register becomes zero to
indicate that the last byte was received.<br/>
When reading further bytes: The buffer is padded with 00h's to the end of the
16-bytes, and does then restart at the first response byte (that, without
receiving a new response, so it'll always return the same 16 bytes, until a new
command/response has been sent/received).<br/>

#### 1F801802h.Index1 - Interrupt Enable Register (W)
#### 1F801803h.Index0 - Interrupt Enable Register (R)
#### 1F801803h.Index2 - Interrupt Enable Register (R) (Mirror)
```
  0-4  Interrupt Enable Bits (usually all set, ie. 1Fh=Enable All IRQs)
  5-7  Unknown/unused (write: should be zero) (read: usually all bits set)
```
XXX WRITE: bit5-7 unused should be 0 // READ: bit5-7 unused<br/>

#### 1F801803h.Index1 - Interrupt Flag Register (R/W)
#### 1F801803h.Index3 - Interrupt Flag Register (R) (Mirror)
```
  0-2   Read: Response Received   Write: 7=Acknowledge   ;INT1..INT7
  3     Read: Unknown (usually 0) Write: 1=Acknowledge   ;INT8  ;XXX CLRBFEMPT
  4     Read: Command Start       Write: 1=Acknowledge   ;INT10h;XXX CLRBFWRDY
  5     Read: Always 1 ;XXX "_"   Write: 1=Unknown              ;XXX SMADPCLR
  6     Read: Always 1 ;XXX "_"   Write: 1=Reset Parameter Fifo ;XXX CLRPRM
  7     Read: Always 1 ;XXX "_"   Write: 1=Unknown              ;XXX CHPRST
```
Writing "1" bits to bit0-4 resets the corresponding IRQ flags; normally one
should write 07h to reset the response bits, or 1Fh to reset all IRQ bits.
Writing values like 01h is possible (eg. that would change INT3 to INT2, but
doing that would be total nonsense). After acknowledge, the Response Fifo is
made empty, and if there's been a pending command, then that command gets send
to the controller.<br/>
The lower 3bit indicate the type of response received,<br/>
```
  INT0   No response received (no interrupt request)
  INT1   Received SECOND (or further) response to ReadS/ReadN (and Play+Report)
  INT2   Received SECOND response (to various commands)
  INT3   Received FIRST response (to any command)
  INT4   DataEnd (when Play/Forward reaches end of disk) (maybe also for Read?)
  INT5   Received error-code (in FIRST or SECOND response)
         INT5 also occurs on SECOND GetID response, on unlicensed disks
         INT5 also occurs when opening the drive door (even if no command
            was sent, ie. even if no read-command or other command is active)
  INT6   N/A
  INT7   N/A
```
The other 2bit indicate something else,<br/>
```
  INT8   Unknown (never seen that bit set yet)
  INT10h Command Start (when INT10h requested via 1F801803h.Index0.Bit5)
```
The response interrupts are queued, for example, if the 1st response is INT3,
and the second INT5, then INT3 is delivered first, and INT5 is not delivered
until INT3 is acknowledged (ie. the response interrupts are NOT ORed together
to produce INT7 or so). The upper bits however can be ORed with the lower bits
(ie. Command Start INT10h and 1st Response INT3 would give INT13h).<br/>

#### 1F801802h.Index2 - Audio Volume for Left-CD-Out to Left-SPU-Input (W)
#### 1F801803h.Index2 - Audio Volume for Left-CD-Out to Right-SPU-Input (W)
#### 1F801801h.Index3 - Audio Volume for Right-CD-Out to Right-SPU-Input (W)
#### 1F801802h.Index3 - Audio Volume for Right-CD-Out to Left-SPU-Input (W)
Allows to configure the CD for mono/stereo output (eg. values "80h,0,80h,0"
produce normal stereo volume, values "40h,40h,40h,40h" produce mono output of
equivalent volume).<br/>
When using bigger values, the hardware does have some incomplete saturation
support; the saturation works up to double volume (eg. overflows that occur on
"FFh,0,FFh,0" or "80h,80h,80h,80h" are clipped to min/max levels), however, the
saturation does NOT work properly when exceeding double volume (eg. mono with
quad-volume "FFh,FFh,FFh,FFh").<br/>
```
  0-7  Volume Level (00h..FFh) (00h=Off, FFh=Max/Double, 80h=Default/Normal)
```
After changing these registers, write 20h to 1F801803h.Index3.<br/>
Unknown if any existing games are actually supporting mono output. Resident
Evil 2 uses these ports to produce fade-in/fade-out effects (although, for that
purpose, it should be much easier to use Port 1F801DB0h).<br/>

#### 1F801803h.Index3 - Audio Volume Apply Changes (by writing bit5=1)
```
  0    ADPMUTE Mute ADPCM                 (0=Normal, 1=Mute)
  1-4  -       Unused (should be zero)
  5    CHNGATV Apply Audio Volume changes (0=No change, 1=Apply)
  6-7  -       Unused (should be zero)
```

#### 1F801801h.Index1 - Sound Map Data Out (W)
```
  0-7  Data
```
This register seems to be restricted to 8bit bus, unknown if/how the PSX DMA
controller can write to it (it might support only 16bit data for CDROM).<br/>

#### 1F801801h.Index2 - Sound Map Coding Info (W)
```
  0    Mono/Stereo     (0=Mono, 1=Stereo)
  1    Reserved        (0)
  2    Sample Rate     (0=37800Hz, 1=18900Hz)
  3    Reserved        (0)
  4    Bits per Sample (0=4bit, 1=8bit)
  5    Reserved        (0)
  6    Emphasis        (0=Off, 1=Emphasis)
  7    Reserved        (0)
```

```
 =============================================================================
```

#### Command Execution
Command/Parameter transmission is indicated by bit7 of 1F801800h.<br/>
When that bit gets zero, the response can be read immediately (immediately for
MOST commands, but not ALL commands; so better wait for the IRQ).<br/>
Alternately, you can wait for an IRQ (which seems to take place MUCH later),
and then read the response.<br/>
If there are any pending cdrom interrupts, these MUST be acknowledged before
sending the command (otherwise bit7 of 1F801800h will stay set forever).<br/>

#### Command Busy Flag - 1F801800h.Bit7
Indicates ready-to-send-new-command,<br/>
```
  0=Ready to send a new command
  1=Busy sending a command/parameters
```
Trying to send a new command in the Busy-phase causes malfunction (the older
command seems to get lost, the newer command executes and returns its results
and triggers an interrupt, but, thereafter, the controller seems to hang). So,
always wait until the Busy-bit goes off before sending a command.<br/>
When the Busy-flag goes off, a new command can be send immediately (even if the
response from the previous command wasn't received yet), however, the new
command stays in the Busy-phase until the IRQ from the previous command is
acknowledged, at that point the actual transmission of the new command starts,
and the Busy-flag goes off (once when the transmission completes).<br/>

#### Misc
Trying to do a 32bit read from 1F801800h returns the 8bit value at 1F801800h
multiplied by 01010101h.<br/>

#### To init the CD
```
  -Flush all IRQs
  -1F801803h.Index0=0
  -Com_Delay=4901 (=1325h) (Port 1F801020h) (means 16bit or 32bit write?)
     (the write seems to be 32bit, clearing the upper16bit of the register)
  -Send two Getstat commands
  -Send Command 0Ah (Init)
  -Demute
```

#### Seek-Busy Phase
Warning: most or all of the info in the sentence below appear to incorrect
(either that, or I didn't understand that rather confusing sentence).<br/>
REPORTEDLY:<br/>
"You should not send some commands while the CD is seeking (ie. Getstat returns
with bit6 set). Thing is that stat only gets updated after a new command. I
haven't tested this for other command, but for the play command (03h) you can
just keep repeating the [which?] command and checking stat returned by that,
for bit6 to go low (and bit7 to go high in this case). If you don't and try to
do a getloc [GetlocP and/or GetlocL?] directly after the play command reports
it's done [what done? meaning sending start-to-play was "done"? or meaning play
reached end-of-disc?], the CD will stop. (I guess the CD can't get it's current
location while it's seeking, so the logic stops the seek to get an exact fix,
but never restarts..)"<br/>

#### Sound Map Flowchart
Sound Map mode allows to output XA-ADPCM from Main RAM (rather than from
CDROM).<br/>
```
  SPU: Init Master Volume Left/Right (Port 1F801D80h/1F801D82h)
  SPU: Init CD Audio Volume Left/Right (Port 1F801DB0h/1F801DB2h)
  SPU: Enable CD Audio (Port 1F801DAAh.Bit0=1)
  CDROM/CMD: send Stop command (probably better to avoid conflicts)
  CDROM/CMD: send Demute command (if muted) (but works only if disc inserted)
  CDROM/HOST: init Codinginfo (Port 1F801801h.Index2)
  CDROM/HOST: enable ADPCM (Port 1F801803h.Index3.Bit0=0)  ;probably needed?
  ... set dummy addr/len with DISHXFRC=1 ?  <-- NOT required !
  ... set SMEN ... and dummy BFWR?    <-- BOTH bits required ?
  transfer 900h bytes (same format as ADPCM sectors) (Port 1F801801h.Index1)
  Note: Before sending a byte, one should wait for DRQs (1F801801h.Bit6=1)
  Note: ADPCM output doesn't start until the last (900h'th) byte is transferred
```
Sound Map mode may be very useful for testing XA-ADPCM directly from within an
exe file (without needing a cdrom with ADPCM sectors). And, Sound Map supports
both 4bit and 8bit compression (the SPU supports only 4bit).<br/>
Caution: If ADPCM wasn't playing, and one sends one 900h-byte block, then it
will get stored in one of three 900h-byte slots in SRAM, and one would expect
that that slot to be played when the ADPCM output starts - however, actually,
the hardware will more or less randomly play one of the three slots; not
necessarily the slot that was updated most recently.<br/>



##   CDROM Controller Command Summary
#### Command Summary
```
  Command          Parameters      Response(s)
  00h -            -               INT5(11h,40h)  ;reportedly "Sync" uh?
  01h Getstat      -               INT3(stat)
  02h Setloc     E amm,ass,asect   INT3(stat)
  03h Play       E (track)         INT3(stat), optional INT1(report bytes)
  04h Forward    E -               INT3(stat), optional INT1(report bytes)
  05h Backward   E -               INT3(stat), optional INT1(report bytes)
  06h ReadN      E -               INT3(stat), INT1(stat), datablock
  07h MotorOn    E -               INT3(stat), INT2(stat)
  08h Stop       E -               INT3(stat), INT2(stat)
  09h Pause      E -               INT3(stat), INT2(stat)
  0Ah Init         -               INT3(late-stat), INT2(stat)
  0Bh Mute       E -               INT3(stat)
  0Ch Demute     E -               INT3(stat)
  0Dh Setfilter  E file,channel    INT3(stat)
  0Eh Setmode      mode            INT3(stat)
  0Fh Getparam     -               INT3(stat,mode,null,file,channel)
  10h GetlocL    E -               INT3(amm,ass,asect,mode,file,channel,sm,ci)
  11h GetlocP    E -               INT3(track,index,mm,ss,sect,amm,ass,asect)
  12h SetSession E session         INT3(stat), INT2(stat)
  13h GetTN      E -               INT3(stat,first,last)  ;BCD
  14h GetTD      E track (BCD)     INT3(stat,mm,ss)       ;BCD
  15h SeekL      E -               INT3(stat), INT2(stat)  ;\use prior Setloc
  16h SeekP      E -               INT3(stat), INT2(stat)  ;/to set target
  17h -            -               INT5(11h,40h)  ;reportedly "SetClock" uh?
  18h -            -               INT5(11h,40h)  ;reportedly "GetClock" uh?
  19h Test         sub_function    depends on sub_function (see below)
  1Ah GetID      E -               INT3(stat), INT2/5(stat,flg,typ,atip,"SCEx")
  1Bh ReadS      E?-               INT3(stat), INT1(stat), datablock
  1Ch Reset        -               INT3(stat), Delay
  1Dh GetQ       E adr,point       INT3(stat), INT2(10bytesSubQ,peak_lo) ;\not
  1Eh ReadTOC      -               INT3(late-stat), INT2(stat)           ;/vC0
  1Fh VideoCD      sub,a,b,c,d,e   INT3(stat,a,b,c,d,e)   ;<-- SCPH-5903 only
  1Fh..4Fh -       -               INT5(11h,40h)  ;-Unused/invalid
  50h Secret 1     -               INT5(11h,40h)  ;\
  51h Secret 2     "Licensed by"   INT5(11h,40h)  ;
  52h Secret 3     "Sony"          INT5(11h,40h)  ; Secret Unlock Commands
  53h Secret 4     "Computer"      INT5(11h,40h)  ; (not in version vC0, and,
  54h Secret 5     "Entertainment" INT5(11h,40h)  ; nonfunctional in japan)
  55h Secret 6     "<region>"      INT5(11h,40h)  ;
  56h Secret 7     -               INT5(11h,40h)  ;/
  57h SecretLock   -               INT5(11h,40h)  ;-Secret Lock Command
  58h..5Fh Crash   -               Crashes the HC05 (jumps into a data area)
  6Fh..FFh -       -               INT5(11h,40h)  ;-Unused/invalid
```
E = Error 80h appears on some commands (02h..09h, 0Bh..0Dh, 10h..16h, 1Ah,
1Bh?, and 1Dh) when the disk is missing, or when the drive unit is disconnected
from the mainboard.<br/>

#### sub\_function numbers (for command 19h)
Test commands are invoked with command number 19h, followed by a sub\_function
number as first parameter byte. The Kernel seems to be using only sub\_function
20h (to detect the CDROM Controller version).<br/>
```
  sub  params  response           ;Effect
  00h      -   INT3(stat)         ;Force motor on, clockwise, even if door open
  01h      -   INT3(stat)         ;Force motor on, anti-clockwise, super-fast
  02h      -   INT3(stat)         ;Force motor on, anti-clockwise, super-fast
  03h      -   INT3(stat)         ;Force motor off (ignored during spin-up)
  04h      -   INT3(stat)         ;Start SCEx reading and reset counters
  05h      -   INT3(total,success);Stop SCEx reading and get counters
  06h *    n   INT3(old)  ;\early ;Adjust balance in RAM, send CX(30+n XOR 7)
  07h *    n   INT3(old)  ; PSX   ;Adjust gain in RAM, send CX(38+n XOR 7)
  08h *    n   INT3(old)  ;/only  ;Adjust balance in RAM only
  06h..0Fh -   INT5(11h,10h)      ;N/A (11h,20h when NONZERO number of params)
  10h      -   INT3(stat) ;CX(..) ;Force motor on, anti-clockwise, super-fast
  11h      -   INT3(stat) ;CX(03) ;Move Lens Up (leave parking position)
  12h      -   INT3(stat) ;CX(02) ;Move Lens Down (enter parking position)
  13h      -   INT3(stat) ;CX(28) ;Move Lens Outwards
  14h      -   INT3(stat) ;CX(2C) ;Move Lens Inwards
  15h      -   INT3(stat) ;CX(22) ;If motor on: Move outwards,inwards,motor off
  16h      -   INT3(stat) ;CX(23) ;No effect?
  17h      -   INT3(stat) ;CX(E8) ;Force motor on, clockwise, super-fast
  18h      -   INT3(stat) ;CX(EA) ;Force motor on, anti-clockwise, super-fast
  19h      -   INT3(stat) ;CX(25) ;No effect?
  1Ah      -   INT3(stat) ;CX(21) ;No effect?
  1Bh..1Fh -   INT5(11h,10h)      ;N/A (11h,20h when NONZERO number of params)
  20h      -   INT3(yy,mm,dd,ver) ;Get cdrom BIOS date/version (yy,mm,dd,ver)
  21h      -   INT3(n)            ;Get Drive Switches (bit0=POS0, bit1=DOOR)
  22h ***  -   INT3("for ...")    ;Get Region ID String
  23h ***  -   INT3("CXD...")     ;Get Chip ID String for Servo Amplifier
  24h ***  -   INT3("CXD...")     ;Get Chip ID String for Signal Processor
  25h ***  -   INT3("CXD...")     ;Get Chip ID String for Decoder/FIFO
  26h..2Fh -   INT5(11h,10h)      ;N/A (11h,20h when NONZERO number of params)
  30h *    i,x,y     INT3(stat)       ;Prototype/Debug stuff   ;\supported on
  31h *    x,y       INT3(stat)       ;Prototype/Debug stuff   ; early PSX only
  4xh *    i         INT3(x,y)        ;Prototype/Debug stuff   ;/
  30h..4Fh ..        INT5(11h,10h)    ;N/A always 11h,10h (no matter of params)
  50h      a[,b[,c]] INT3(stat)       ;Servo/Signal send CX(a:b:c)
  51h **   39h,xx    INT3(stat,hi,lo) ;Servo/Signal send CX(39xx) with response
  51h..5Fh -         INT5(11h,10h)    ;N/A
  60h      lo,hi     INT3(databyte)   ;HC05 SUB-CPU read RAM and I/O ports
  61h..70h -         INT5(11h,10h)    ;N/A
  71h ***  adr       INT3(databyte)   ;Decoder Read one register
  72h ***  adr,dat   INT3(stat)       ;Decoder Write one register
  73h ***  adr,len   INT3(databytes..);Decoder Read multiple registers, bugged
  74h ***  adr,len,..INT3(stat)       ;Decoder Write multiple registers, bugged
  75h ***  -         INT3(lo,hi,lo,hi);Decoder Get Host Xfer Info Remain/Addr
  76h ***  a,b,c,d   INT3(stat)       ;Decoder Prepare Transfer to/from SRAM
  77h..FFh -         INT5(11h,10h)    ;N/A
```
\* sub\_functions 06h..08h, 30h..31h, and 4xh are supported only in vC0 and vC1.<br/>
\*\* sub\_function 51h is supported only in BIOS version vC2 and up.<br/>
\*\*\* sub\_functions 22h..25h, 71h..76h supported only in BIOS version vC1 and up.<br/>

#### Unsupported GetQ,VCD,SecretUnlock (command 1Dh,1Fh,5xh)
INT5 will be returned if the command is unsupported. That, WITHOUT removing the
Parameters from the FIFO, so the parameters will be accidently passed to the
NEXT command. To avoid that: clear the parameter FIFO via
[1F801803h.Index1]=40h after receiving the INT5 error.<br/>



##   CDROM - Control Commands
#### Sync - Command 00h --\> INTx(stat+1,40h) (?)
Reportedly "command does not succeed until all other commands complete. This
can be used for synchronization - hence the name."<br/>
Uh, actually, returns error code 40h = Invalid Command...?<br/>

#### Setfilter - Command 0Dh,file,channel --\> INT3(stat)
Automatic ADPCM (CD-ROM XA) filter ignores sectors except those which have the
same channel and file numbers in their subheader. This is the mechanism used to
select which of multiple songs in a single .XA file to play.<br/>
Setfilter does not affect actual reading (sector reads still occur for all
sectors).<br/>
XXX err... that is... does not affect reading of non-ADPCM sectors (normal
"data" sectors are kept received regardless of Setfilter).<br/>

#### Setmode - Command 0Eh,mode --\> INT3(stat)
```
  7   Speed       (0=Normal speed, 1=Double speed)
  6   XA-ADPCM    (0=Off, 1=Send XA-ADPCM sectors to SPU Audio Input)
  5   Sector Size (0=800h=DataOnly, 1=924h=WholeSectorExceptSyncBytes)
  4   Ignore Bit  (0=Normal, 1=Ignore Sector Size and Setloc position)
  3   XA-Filter   (0=Off, 1=Process only XA-ADPCM sectors that match Setfilter)
  2   Report      (0=Off, 1=Enable Report-Interrupts for Audio Play)
  1   AutoPause   (0=Off, 1=Auto Pause upon End of Track) ;for Audio Play
  0   CDDA        (0=Off, 1=Allow to Read CD-DA Sectors; ignore missing EDC)
```
The "Ignore Bit" does reportedly force a sector size of 2328 bytes (918h),
however, that doesn't seem to be true. Instead, Bit4 seems to cause the
controller to ignore the sector size in Bit5 (instead, the size is kept from
the most recent Setmode command which didn't have Bit4 set). Also, Bit4 seems
to cause the controller to ignore the \<exact\> Setloc position (instead,
data is randomly returned from the "Setloc position minus 0..3 sectors"). And,
Bit4 causes INT1 to return status.Bit3=set (IdError). Purpose of Bit4 is
unknown?<br/>

#### Init - Command 0Ah --\> INT3(stat) --\> INT2(stat)
Multiple effects at once. Sets mode=00h (or not ALL bits cleared?), activates
drive motor, Standby, abort all commands.<br/>

#### Reset - Command 1Ch,(...) --\> INT3(stat) --\> Delay(1/8 seconds)
Resets the drive controller, reportedly, same as opening and closing the drive
door. The command executes no matter if/how many parameters are used (tested
with 0..7 params). INT3 indicates that the command was started, but there's no
INT that would indicate when the command is finished, so, before sending any
further commands, a delay of 1/8 seconds (or 400000h clock cycles) must be
issued by software.<br/>
Note: Executing the command produces a click sound in the drive mechanics,
maybe it's just a rapid motor on/off, but it might something more serious, like
ignoring the /POS0 signal...?<br/>

#### MotorOn - Command 07h --\> INT3(stat) --\> INT2(stat)
Activates the drive motor, works ONLY if the motor was off (otherwise fails
with INT5(stat,20h); that error code would normally indicate "wrong number of
parameters", but means "motor already on" in this case).<br/>
Commands like Read, Seek, and Play are automatically starting the Motor when
needed (which makes the MotorOn command rather useless, and it's rarely used by
any games).<br/>
Myth: Older homebrew docs are referring to MotorOn as "Standby", claiming that
it would work similar as "Pause", that is wrong: the command does NOT pause
anything (if the motor is on, then it does simply trigger INT5, but without
pausing reading or playing).<br/>
Note: The game "Nightmare Creatures 2" does actually attempt to use MotorOn to
"pause" after reading files, but the hardware does simply ignore that attempt
(aside from doing the INT5 thing).<br/>

#### Stop - Command 08h --\> INT3(stat) --\> INT2(stat)
Stops motor with magnetic brakes (stops within a second or so) (unlike
power-off where it'd keep spinning for about 10 seconds), and moves the drive
head to the begin of the first track. Official way to restart is command 0Ah,
but almost any command will restart it.<br/>
The first response returns the current status (this already with bit5 cleared),
the second response returns the new status (with bit1 cleared).<br/>

#### Pause - Command 09h --\> INT3(stat) --\> INT2(stat)
Aborts Reading and Playing, the motor is kept spinning, and the drive head
maintains the current location within reasonable error.<br/>
The first response returns the current status (still with bit5 set if a Read
command was active), the second response returns the new status (with bit5
cleared).<br/>

#### Data/ADPCM Sector Filtering/Delivery
The PSX CDROM BIOS is first trying to send sectors to the ADPCM decoder, and,
if that didn't work out, then it's trying to send them to the main CPU (and if
that didn't work out either, then it's silently ignoring the sector).<br/>
```
 try_deliver_as_adpcm_sector:
  reject if CD-DA AUDIO format
  reject if sector isn't MODE2 format
  reject if adpcm_disabled(setmode.6)
  reject if filter_enabled(setmode.3) AND selected file/channel doesn't match
  reject if submode isn't audio+realtime (bit2 and bit6 must be both set)
  deliver: send sector to xa-adpcm decoder when passing above cases
 try_deliver_as_data_sector:
  reject data-delivery if "try_deliver_as_adpcm_sector" did do adpcm-delivery
  reject if filter_enabled(setmode.3) AND submode is audio+realtime (bit2+bit6)
  1st delivery attempt: send INT1+data, unless there's another INT pending
  delay, and retry at later time... but this time with file/channel checking!
  reject if filter_enabled(setmode.3) AND selected file/channel doesn't match
  2nd delivery attempt: send INT1+data, unless there's another INT pending
```
BUG: Note that the data delivery is done in two different attempts: The first
one regardless of file/channel, and the second one only on matching
file/channel (if filtering is enabled).<br/>



##   CDROM - Seek Commands
#### Setloc - Command 02h,amm,ass,asect --\> INT3(stat)
Sets the seek target - but without yet starting the seek operation. The actual
seek is invoked by certain commands: SeekL (Data) and SeekP (Audio) are doing
plain seeks (and do Pause after completion). ReadN/ReadS are similar to SeekL
(and do start reading data after the seek operation). Play is similar to SeekP
(and does start playing audio after the seek operation).<br/>
The amm,ass,asect parameters refer to the entire disk (not to the current
track). To seek to a specific location within a specific track, use GetTD to
get the start address of the track, and add the desired time offset to it.<br/>

#### SeekL - Command 15h --\> INT3(stat) --\> INT2(stat)
Seek to Setloc's location in data mode (using data sector header position data,
which works/exists only on Data tracks, not on CD-DA Audio tracks).<br/>
After the seek, the disk stays on the seeked location forever (namely: when
seeking sector N, it does stay at around N-8..N-0 in single speed mode, or at
around N-5..N+2 in double speed mode).<br/>
Trying to use SeekL on Audio CDs passes okay on the first response, but (after
two seconds or so) the second response will return an error (stat+4,04h), and
stop the drive motor... that error doesn't appear ALWAYS though... works in
some situations... such like when previously reading data sectors or so...?<br/>

#### SeekP - Command 16h --\> INT3(stat) --\> INT2(stat)
Seek to Setloc's location in audio mode (using the Subchannel Q position data,
which works on both Audio on Data disks).<br/>
After the seek, the disk stays on the seeked location forever (namely: when
seeking sector N, it does stay at around N-9..N-1 in single speed mode, or at
around N-2..N in double speed mode).<br/>
Note: Some older docs claim that SeekP would recurse only "MM:SS" of the
"MM:SS:FF" position from Setloc - that is wrong, it does seek to MM:SS:FF
(verified on a PSone).<br/>
After the seek, status is stat.bit7=0 (ie. audio playback off), until sending a
new Play command (without parameters) to start playback at the seeked location.<br/>

#### SetSession - Command 12h,session --\> INT3(stat) --\> INT2(stat)
Seeks to session (ie. moves the drive head to the session, with stat bit6 set
during the seek phase).<br/>
When issued during active-play, the command returns error code 80h.<br/>
When issued during play-spin-up, play is aborted.<br/>
```
  ___Errors___
  session = 00h causes error code 10h.     ;INT5(03h,10h), no 2nd/3rd response
  ___On a non-multisession-disk___
  session = 01h passes okay.               ;INT3(stat), and once INT2(stat)
  session = 02h or higher cause seek error ;INT3(stat), and twice INT5(06h,40h)
  ___On a multisession-disk with N sessions___
  session = 01h..N+1 passes okay   ;where N+1 moves to the END of LAST session
  session = N+2 or higher cause seek error  ;2nd response = INT5(06h,20h)
```
after seek error --\> disk stops spinning at 2nd response, then restarts
spinning for 1 second or so, then stops spinning forever... and following
gettn/gettd/getid/getlocl/getlocp fail with error 80h...<br/>
The command does automatically read the TOC of the new session.<br/>
There seems to be no way to determine the current sessions number (via Getparam
or so), and more important, no way to determine if the disk is a multi-session
disk or not... except by trial... which would stop the drive motor on seek
errors on single-session disks...?<br/>
For setloc, one must probably specifiy minutes within the 1st track of the new
session (the 1st track of 1st session usually/always starts at 00:02:00, but
for other sessions one would need to use GetTD)...?<br/>



##   CDROM - Read Commands
#### ReadN - Command 06h --\> INT3(stat) --\> INT1(stat) --\> datablock
Read with retry. The command responds once with "stat,INT3", and then it's
repeatedly sending "stat,INT1 --\> datablock", that is continued even after a
successful read has occured; use the Pause command to terminate the repeated
INT1 responses.<br/>
Unknown which responses are sent in case of read errors?<br/>
====<br/>
ReadN and ReadS cause errors if you're trying to read an unlicensed CD or CD-R
without a mod chip. Sectors on Audio CDs can be read only when CDDA is enabled
via Setmode (otherwise error code 40h is returned).<br/>
====<br/>
Actually, Read seems to work on unlicensed CD-R's, but the returned data is the
whole sector or so (the 2048 data bytes preceeded by a 12byte header, and
probably/maybe followed by error-correction info; in fact the total received
data in the Data Fifo is 4096 bytes; the last some bytes probably being
garbage) (however error correction is NOT performed by hardware, so the 2048
data bytes may be trashy) (however, if the error correction info IS received,
then error correction could be performed by software) (also Setloc doesn't seem
to work accurately on unlicensed CD-R's).<br/>
====<br/>
```
     ;Read occasionally returns 11h,40h ..? when TOC isn't loaded?
```
After receiving INT1, the Kernel does,<br/>
```
  [1F801800h]=00h
  00h=[1F801800h]
  [1F801803h]=00h
  00h=[1F801803h]
  [1F801800h]=00h
  [1F801803h]=80h
```
and then,<br/>
```
  [1F801018h]=00020943h  ;cdrom_delay
  [1F801020h]=0000132Ch  ;com_delay
```
then,<br/>
```
  x=[1F8010F4h] AND 00FFFFFFh   ;result is 00840000h
  [1F8010F4h] = x OR 00880000h
  [1F8010F0h] = [1F8010F0h] OR 00008000h
  [1F8010B0h] = A0010000h ;addr
  [1F8010B4h] = 00010200h ;LSBs=num words, MSBs=ignored/bullshit
  [1F8010B4h] = 11000000h ;DMA control
```
thereafter,<br/>
```
  [1F801800h]=01h
  [1F801803h]=40h    ;reset parameter fifo
  [0]=00000000h
  [0]=00000001h
  [0]=00000002h
  [0]=00000003h
  [1F801800h]=00h
  [1F801801h]=09h    ;command9 (pause)
```

#### ReadS - Command 1Bh --\> INT3(stat) --\> INT1(stat) --\> datablock
Read without automatic retry. Not sure what that means... does WHAT on errors?
Maybe intended for continous streaming video output (to skip bad frames, rather
than to interrupt the stream by performing read-retrys).<br/>

#### ReadN/ReadS
Both ReadN/ReadS are reading data sequentially, starting at the sector
specified with Setloc, and then automatically reading the following sectors.<br/>

#### CDROM Incoming Data / Buffer Overrun Timings
The Read commands are continously receiving 75 sectors per second (or 150
sectors at double speed), and, basically, the software must be fast enough to
process that amount of incoming data. However, the PSX hardware includes a
buffer that can hold up to a handful (exact number is unknown?) of sectors, so,
occasional delays of more than 1/75 seconds between processing two sectors
aren't causing lost sectors, unless the delay(s) are summing up too much. The
relevant steps for receiving data are:<br/>
```
  Wait for Interrupt Request (INT1)          ;indicates that data is available
  Send Data Request (1F801803h.Index0.Bit7=1);accept data
  Acknowledge INT1                           ;
  Copy Data to Main RAM (via I/O or DMA)     ;read data
```
The Data Request accepts the data for the currently pending interrupt, it
should be usually issued between receiving/acknowledging INT1 (however, it can
be also issued shortly after the acknowledge; even if there are further sectors
in the buffer, there seems to be a small delay between the acknowledge and the
next interrupt, and Data Requests during that period are still treated to
belong to the old interrupt).<br/>
If a buffer overrun has occured \<before\> issuing the Data Request, then
wrong data will be received, ie. some sectors will be skipped (the hardware
doesn't seem to support a buffer-overrun error flag? Anyways, see GetlocL
description for a possible way to detect buffer-overruns).<br/>
If a buffer overrun occurs \<after\> issuing the Data Request, then the
requested data can be still read via I/O or DMA intactly, ie. the requested
data is "locked", and the overrun will affect only the following sectors.<br/>

#### ReadTOC - Command 1Eh --\> INT3(stat) --\> INT2(stat)
```
  Caution: Supported only in BIOS version vC1 and up. Not supported in vC0.
```
Reread the Table of Contents of current session without reset. The command is
rather slow, the second response appears after about 1 second delay. The
command itself returns only status information (to get the actual TOC info, use
GetTD and GetTN commands).<br/>
Note: The TOC contains information about the tracks on the disk (not file names
or so, that kind of information is obtained via Read commands). The TOC is read
automatically on power-up, when opening/closing the drive door, and when
changing sessions (so, normally, it isn't required to use this command).<br/>

#### Setloc, Read, Pause
A normal CDROM access (such like reading a file) consists of three commands:<br/>
```
  Setloc, Read, Pause
```
Normally one shouldn't mess up the ordering of those commands, but if one does,
following rules do apply:<br/>
Setloc is memorizing the wanted target, and marks it as unprocessed, and has no
other effect (it doesn't start reading or seeking, and doesn't interrupt or
redirect any active reads).<br/>
If Read is issued with an unprocessed Setloc, then the drive is automatically
seeking the Setloc location (and marks Setloc as processed).<br/>
If Read is issued without an unprocessed Setloc, the following happens: If
reading is already in progress then it just continues reading. If Reading was
Paused, then reading resumes at the most recently received sector (ie.
returning that sector once another time).<br/>



##   CDROM - Status Commands
#### Status code (stat)
The 8bit status code is returned by Getstat command (and many other commands),
the meaning of the separate stat bits is:<br/>
```
  7  Play          Playing CD-DA         ;\only ONE of these bits can be set
  6  Seek          Seeking               ; at a time (ie. Read/Play won't get
  5  Read          Reading data sectors  ;/set until after Seek completion)
  4  ShellOpen     Once shell open (0=Closed, 1=Is/was Open)
  3  IdError       (0=Okay, 1=GetID denied) (also set when Setmode.Bit4=1)
  2  SeekError     (0=Okay, 1=Seek error)     (followed by Error Byte)
  1  Spindle Motor (0=Motor off, or in spin-up phase, 1=Motor on)
  0  Error         Invalid Command/parameters (followed by Error Byte)
```
If the shell is closed, then bit4 is automatically reset to zero after reading
stat with the Getstat command (most or all other commands do not reset that bit
after reading). If stat bit0 or bit2 is set, then the normal respons(es) and
interrupt(s) are not send, and, instead, INT5 occurs, and an error-byte is send
as second response byte, with the following values:<br/>
```
  ___These values appear in the FIRST response; with stat.bit0 set___
  10h - Invalid Sub_function (for command 19h), or invalid parameter value
  20h - Wrong number of parameters
  40h - Invalid command
  80h - Cannot respond yet (eg. required info was not yet read from disk yet)
           (namely, TOC not-yet-read or so)
           (also appears if no disk inserted at all)
  ___These values appear in the SECOND response; with stat.bit2 set___
  04h - Seek failed (when trying to use SeekL on Audio CDs)
  ___These values appear even if no command was sent; with stat.bit2 set___
  08h - Drive door became opened
```
80h appears on some commands (02h..09h, 0Bh..0Dh, 10h..16h, 1Ah, 1Bh?, and 1Dh)
when the disk is missing, or when the drive unit is disconnected from the
mainboard.<br/>

#### Stat Seek/Play/Read bits
There's is only max ONE of the three Seek/Play/Read bits set at a time, ie.
during Seek, ONLY the seek bit is set (and Read or Play doesn't get until seek
completion), that is important for Gran Turismo 1, which checks for seek
completion by waiting for READ getting set (rather than waiting for SEEK
getting cleared).<br/>

#### Getstat - Command 01h --\> INT3(stat)
Returns stat (like many other commands), and additionally does reset the shell
open flag (for the following commands; unless the shell is still opened). This
is different as for most or all other commands (which may return stat, but
which do not reset the shell open flag).<br/>
In other docs, the command is eventually referred to as "Nop", believing that
it does nothing than returning stat (ignoring the fact that it's having the
special shell open reset feature).<br/>

#### Getparam - Command 0Fh --\> INT3(stat,mode,null,file,channel)
Returns stat (see Getstat above), mode (see Setmode), a null byte (always 00h),
and file/channel filter values (see Setfilter).<br/>

#### GetlocL - Command 10h --\> INT3(amm,ass,asect,mode,file,channel,sm,ci)
Retrieves 4-byte sector header, plus 4-byte subheader of the current sector.
GetlocL can be send during active Read commands (but, mind that the
GetlocL-INT3-response can't be received until any pending Read-INT1's are
acknowledged).<br/>
The PSX hardware can buffer a handful of sectors, the INT1 handler receives the
\<oldest\> buffered sector, the GetlocL command returns the header and
subheader of the \<newest\> buffered sector. Note: If the returned
\<newest\> sector number is much bigger than the expected \<oldest\>
sector number, then it's likely that a buffer overrun has occured.<br/>
GetlocL fails (with error code 80h) when playing Audio CDs (or Audio Tracks on
Data CDs). These errors occur because Audio sectors don't have any
header/subheader (instead, equivalent data is stored in Subchannel Q, which can
be read with GetlocP).<br/>
GetlocL also fails (with error code 80h) when the drive is in Seek phase (such
like shortly after a new ReadN/ReadS command). In that case one can retry
issuing GetlocL (until it passes okay, ie. until the seek has completed).
During Seek, the drive seems to decode only Subchannel position data (but no
header/subheader data), accordingly GetlocL won't work during seek (however,
GetlocP does work during Seek).<br/>

#### GetlocP - Command 11h - INT3(track,index,mm,ss,sect,amm,ass,asect)
Retrieves 8 bytes of position information from Subchannel Q with ADR=1. Mainly
intended for displaying the current audio position during Play. All results are
in BCD.<br/>
```
  track:  track number (AAh=Lead-out area) (FFh=unknown, toc, none?)
  index:  index number (Usually 01h)
  mm:     minute number within track (00h and up)
  ss:     second number within track (00h to 59h)
  sect:   sector number within track (00h to 74h)
  amm:    minute number on entire disk (00h and up)
  ass:    second number on entire disk (00h to 59h)
  asect:  sector number on entire disk (00h to 74h)
```
Note: GetlocP is also used for reading the LibCrypt protection data:<br/>
[CDROM Protection - LibCrypt](cdromdrive.md#cdrom-protection---libcrypt)<br/>

#### GetTN - Command 13h --\> INT3(stat,first,last) ;BCD
Get first track number, and last track number in the TOC of the current
Session. The number of tracks in the current session can be calculated as
(last-first+1). The first track number is usually 01h in the first (or only)
session, and "last track of previous session plus 1" in further sessions.<br/>

#### GetTD - Command 14h,track --\> INT3(stat,mm,ss) ;BCD
For a disk with NN tracks, parameter values 01h..NNh return the start of the
specified track, parameter value 00h returns the end of the last track, and
parameter values bigger than NNh return error code 10h.<br/>
The GetTD values are relative to Index=1 and are rounded down to second
boundaries (eg. if track=N Index=0 starts at 12:34:56, and Track=N Index=1
starts at 12:36:56, then GetTD(N) will return 12:36, ie. the sector number is
truncated, and the Index=0 region is skipped).<br/>

#### GetQ - Command 1Dh,adr,point --\> INT3(stat) --\> INT2(10bytesSubQ,peak\_lo)
```
  Caution: Supported only in BIOS version vC1 and up. Not supported in vC0.
  Caution: When unsupported, Parameter Fifo isn't cleared after the command.
```
Allows to read 10 bytes from Subchannel Q in Lead-In (see CDROM Subchannels
chapter for details). Unlike GetTD, this command allows to receive the exact
MM:SS:FF address of the point'ed Track (GetTD reads a memorized MM:SS value
from RAM, whilst GetQ reads the full MM:SS:FF from the disk, which is slower
than GetTD, due to the disk-access).<br/>
With ADR=1, point can be a any point number for ADR=1 in Lead-in (eg.
01h..99h=Track N, A2h=Lead-Out). The returned 10 bytes are raw SubQ data
(starting with the ADR/Control value; of which the lower 4bits are always
ADR=1).<br/>
The 11th returned byte is the Peak LSB (similar as in Play+Report, but in this
case only the LSB is transferred, which is apparently a bug in CDROM BIOS, the
programmer probably wanted to send 10 bytes without peak, or 12 bytes with full
peak; although peak wouldn't be too useful, as it should always zero during
Lead-In... but some discs do seem return non-zero values for whatever reason).<br/>
Aside from ADR=1, a value of ADR=5 can be used on multisession disks (eg. with
point B0h, C0h). Not sure if any other ADR values can be used (ADR=3, ISRC is
usually not in the Lead-In, ADR=2, EAN may be in the lead-in, but one may need
to specify point equal to the first EAN byte).<br/>
If the ADR/Point combination isn't found, then a timeout occurs after circa 6
seconds (to avoid this, use GetTN to see which tracks/points exist). After the
timeout, the command starts playing track 1. If the controller wasn't already
in audio mode before sending the command, then it does switch off the drive
motor for a moment (that, after the timeout, and before starting playback).<br/>
In case of timeout, the normal INT3/INT2 responses are replaced by
INT3/INT5/INT5 (INT3 at command start, 1st INT5 at timeout/stop, and 2nd INT5
at restart/play).<br/>
Note: GetQ sends scratch noise to the SPU while seeking to the Lead-In area.<br/>

#### GetID - Command 1Ah --\> INT3(stat) --\> INT2/5 (stat,flags,type,atip,"SCEx")
```
  Drive Status           1st Response   2nd Response
  Door Open              INT5(11h,80h)  N/A
  Spin-up                INT5(01h,80h)  N/A
  Detect busy            INT5(03h,80h)  N/A
  No Disk                INT3(stat)     INT5(08h,40h, 00h,00h, 00h,00h,00h,00h)
  Audio Disk             INT3(stat)     INT5(0Ah,90h, 00h,00h, 00h,00h,00h,00h)
  Unlicensed:Mode1       INT3(stat)     INT5(0Ah,80h, 00h,00h, 00h,00h,00h,00h)
  Unlicensed:Mode2       INT3(stat)     INT5(0Ah,80h, 20h,00h, 00h,00h,00h,00h)
  Unlicensed:Mode2+Audio INT3(stat)     INT5(0Ah,90h, 20h,00h, 00h,00h,00h,00h)
  Debug/Yaroze:Mode2     INT3(stat)     INT2(02h,00h, 20h,00h, 20h,20h,20h,20h)
  Licensed:Mode2         INT3(stat)     INT2(02h,00h, 20h,00h, 53h,43h,45h,4xh)
  Modchip:Audio/Mode1    INT3(stat)     INT2(02h,00h, 00h,00h, 53h,43h,45h,4xh)
```
The status byte (ie. the first byte in the responses), may differ in some
cases; values shown above are typically received when issuing GetID shortly
after power-up; however, shortly after the detect-busy phase, seek-busy flag
(bit6) bit may be set, and, after issuing commands like Play/Read/Stop,
bit7,6,5,1 may differ. The meaning of the separate 2nd response bytes is:<br/>
```
  1st byte: stat  (as usually, but with bit3 same as bit7 in 2nd byte)
  2nd byte: flags (bit7=denied, bit4=audio... or reportedly import, uh?)
    bit7: Licensed (0=Licensed Data CD, 1=Denied Data CD or Audio CD)
    bit6: Missing  (0=Disk Present, 1=Disk Missing)
    bit4: Audio CD (0=Data CD, 1=Audio CD) (always 0 when Modchip installed)
  3rd byte: Disk type (from TOC Point=A0h) (eg. 00h=Audio or Mode1, 20h=Mode2)
  4th byte: Usually 00h (or 8bit ATIP from Point=C0h, if session info exists)
    that 8bit ATIP value is taken form the middle 8bit of the 24bit ATIP value
  5th-8th byte: SCEx region (eg. ASCII "SCEE" = Europe) (0,0,0,0 = Unlicensed)
```
The fourth letter of the "SCEx" string contains region information: "SCEI"
(Japan/NTSC), "SCEA" (America/NTSC), "SCEE" (Europe/PAL). The "SCEx" string is
displayed in the intro, and the PSX refuses to boot if it doesn't match up for
the local region.<br/>
With a modchip installed, the same response is sent for Mode1 and Audio disks
(except for Audio disks with very short TOCs (eg. singles) because SCEX reading
is aborted immediately after reading all TOC entries on Audio disks); whether
it is Audio or Mode1 can be checked by examining Subchannel Q ADR/Control.Bit6
(eg. via command 19h,60h,50h,00h).<br/>
Yaroze does return "SCEA" for SCEA discs, but, for SCEI,SCEE,SCEW discs it does
return four ASCII spaces (20h).<br/>



##   CDROM - CD Audio Commands
To play CD-DA Audio CDs, init the following SPU Registers: CD Audio Volume,
Main Volume, and SPU Control Bit0. Then send Demute command, and Play command.<br/>

#### Mute - Command 0Bh --\> INT3(stat)
Turn off audio streaming to SPU (affects both CD-DA and XA-ADPCM).<br/>
Even when muted, the CDROM controller is internally processing audio sectors
(as seen in 1F801800h.Bit2, which works as usually for XA-ADPCM), muting is
just forcing the CD output volume to zero.<br/>
Mute is used by Dino Crisis 1 to mute noise during modchip detection.<br/>

#### Demute - Command 0Ch --\> INT3(stat)
Turn on audio streaming to SPU (affects both CD-DA and XA-ADPCM). The Demute
command is needed only if one has formerly used the Mute command (by default,
the PSX is demuted after power-up (...and/or after Init command?), and is
demuted after cdrom-booting).<br/>

#### Play - Command 03h (,track) --\> INT3(stat) --\> optional INT1(report bytes)
Starts CD Audio Playback. The parameter is optional, if there's no parameter
given (or if it is 00h), then play either starts at Setloc position (if there
was a pending unprocessed Setloc), or otherwise starts at the current location
(eg. the last point seeked, or the current location of the current song; if it
was already playing). For a disk with N songs, Parameters 1..N are starting the
selected track. Parameters N+1..99h are restarting the begin of current track.
The motor is switched off automatically when Play reaches the end of the disk,
and INT4(stat) is generated (with stat.bit7 cleared).<br/>
The track parameter seems to be ignored when sending Play shortly after
power-up (ie. when the drive hasn't yet read the TOC).<br/>
===<br/>
"Play is almost identical to CdlReadS, believe it or not. The main difference
is that this does not trigger a completed read IRQ. CdlPlay may be used on data
sectors. However, all sectors from data tracks are treated as 00, so no sound
is played. As CdlPlay is reading, the audio data appears in the sector buffer,
but is not reliable. Game Shark "enhancement CDs" for the 2.x and 3.x versions
used this to get around the PSX copy protection."<br/>
Hmmm, what/where is the sector buffer... in the SPU?<br/>
And, what/who are the 2.x and 3.x versions?<br/>

#### Forward - Command 04h --\> INT3(stat) --\> optional INT1(report bytes)
#### Backward - Command 05h --\> INT3(stat) --\> optional INT1(report bytes)
After sending the command, the drive is in fast forward/backward mode, skipping
every some sectors. The skipping rate is fixed (it doesn't increase after some
seconds) (however, it increases when (as long as) sending the command again and
again). The sound becomes (obviously) non-continous, and also rather very
silent, muffled, and almost inaudible (that's making it rather useless; unless
it's combined with a track/minute/second display). To terminate
forward/backward, send a new Play command (with no parameters, so play starts
at the "searched" location). Backward automatically switches to Play when
reaching the begin of Track 1. Forward automatically Stops the drive motor with
INT4(stat) when reaching the end of the last track.<br/>
Forward/Backwards work only if the drive was in Play state, and only if Play
had already started (ie. not shortly/immediately after a Play command); if the
drive was not in Play state, then INT5(stat+1,80h) occurs.<br/>

#### Setmode bits used for Play command
During Play, only bit 7,2,1 of Setmode are used, all other Setmode bits are
ignored (that, including bit0, ie. during Play the drive is always in CD-DA
mode, regardless of that bit).<br/>
Bit7 (double speed) should be usually off, although it can be used for a fast
forward effect (with audible output). Bit2 (report) activates an optional
interrupt for Play, Forward, and Backward commands (see below). Bit1
(autopause) pauses play at the end of the track.<br/>

#### Report --\> INT1(stat,track,index,mm/amm,ss+80h/ass,sect/asect,peaklo,peakhi)
With report enabled via Setmode, the Play, Forward, and Backward commands do
repeatedly generate INT1 interrupts, with eight bytes response length. The
interrupt isn't generated on ALL sectors, and the response changes between
absolute time, and time within current track (the latter one indicated by bit7
of ss):<br/>
```
  amm/ass/asect are returned on asect=00h,20h,40h,60h   ;-absolute time
  mm/ss+80h/sect are returned on asect=10h,30h,50h,70h  ;-within current track
  (or, in case of read errors, report may be returned on other asect's)
```
The last two response bytes (peaklo,peakhi) contain the Peak value, as received
from the CXD2510Q Signal Processor. That is: An unsigned absolute peak level in
lower 15bit, and an L/R flag in upper bit. The L/R bit is toggled after each
SUBQ read, however the PSX Report mode does usually forward SUBQ only every 10
frames (but does read SUBQ in \<every\> frame), so L/R will stay stuck in
one setting (but may toggle after one second; ie. after 75 frames). And, peak
is reset after each read, so 9 of the 10 frames are lost.<br/>
Note: Report mode affects only CD Audio (not Data, nor XA-ADPCM sectors).<br/>

#### AutoPause --\> INT4(stat)
Autopause can be enabled/disabled via Setmode.bit1:<br/>
```
  Setmode.bit1=1: AutoPause=On  --> Issue INT4(stat) and PAUSE at end of TRACK
  Setmode.bit1=0: AutoPause=Off --> Issue INT4(stat) and STOP at end of DISC
```
End of Track is determined by sensing a track number transition in SubQ
position info. After autopause, the disc stays at the \<end\> of the old
track, NOT at the \<begin\> of the next track (so trying to resume playing
by sending a new Play command without new Seek/Setloc command will instantly
pause again).<br/>
Caution: SubQ track transitions may pause instantly when accidently starting to
play at the end of the previous track rather than at begin of desired track
(this \<might\> happen due to seek inaccuracies, for example, GetTD does
round down TOC entries from MM:SS:FF to MM:SS:00, which may be off by 0.99
seconds, although this error should be usually compensated by the leading
2-second pregap/index0 region at the begin of each track, unfortunately there
are a few .CUE sheet files that do lack both PREGAP and INDEX 00 entries on
audio tracks, which might cause problems with autopause).<br/>
AutoPause is used by Rayman and Tactics Ogre.<br/>

#### Playing XA-ADPCM Sectors (compressed audio data)
Aside from normal uncompressed CD Audio disks, the PSX can also play XA-ADPCM
compressed sectors. XA-ADPCM sectors are organized in Files (not in tracks),
and are "played" with Read command (not Play command).<br/>
To play XA-ADPCM, initialize the SPU for CD Audio input (as described above),
enable ADPCM via Setmode, then select the sector via Setloc, and issue a Read
command (typically ReadS).<br/>
XA-ADPCM sectors are interleaved, ie. only each Nth sector should be played
(where "N" depends on the Motor Speed, mono/stereo format, and sample rate). If
the "other" sectors do contain XA-ADPCM data too, then the Setfilter command
(and XA-Filter enable flag in Setmode) must be used to select the desired
sectors. If the "other" sectors do contain code or data (eg. MDEC video data)
which is wanted to be send to the CPU, then SetFilter isn't required to be
enabled (although it shouldn't disturb reading even if it is enabled).<br/>
If XA-ADPCM (and/or XA-Filter) is enabled via Setmode, then INT1 is generated
only for non-ADPCM sectors.<br/>
The Setmode sector-size selection is don't care for forwarding XA-ADPCM sectors
to the SPU (the hardware does always decompress all 900h bytes).<br/>



##   CDROM - Test Commands
[CDROM - Test Commands - Version, Switches, Region, Chipset, SCEx](cdromdrive.md#cdrom---test-commands---version-switches-region-chipset-scex)<br/>
[CDROM - Test Commands - Test Drive Mechanics](cdromdrive.md#cdrom---test-commands---test-drive-mechanics)<br/>
[CDROM - Test Commands - Prototype Debug Transmission](cdromdrive.md#cdrom---test-commands---prototype-debug-transmission)<br/>
[CDROM - Test Commands - Read/Write Decoder RAM and I/O Ports](cdromdrive.md#cdrom---test-commands---readwrite-decoder-ram-and-io-ports)<br/>
[CDROM - Test Commands - Read HC05 SUB-CPU RAM and I/O Ports](cdromdrive.md#cdrom---test-commands---read-hc05-sub-cpu-ram-and-io-ports)<br/>



##   CDROM - Test Commands - Version, Switches, Region, Chipset, SCEx
#### 19h,20h --\> INT3(yy,mm,dd,ver)
Indicates the date (Year-month-day, in BCD format) and version of the HC05
CDROM controller BIOS. Known/existing values are:<br/>
```
  (unknown)        ;DTL-H2000 (with SPC700 instead HC05)
  94h,09h,19h,C0h  ;PSX (PU-7)               19 Sep 1994, version vC0 (a)
  94h,11h,18h,C0h  ;PSX (PU-7)               18 Nov 1994, version vC0 (b)
  95h,05h,16h,C1h  ;PSX (LATE-PU-8)          16 May 1995, version vC1 (a)
  95h,07h,24h,C1h  ;PSX (LATE-PU-8)          24 Jul 1995, version vC1 (b)
  95h,07h,24h,D1h  ;PSX (LATE-PU-8,debug ver)24 Jul 1995, version vD1 (debug)
  96h,08h,15h,C2h  ;PSX (PU-16, Video CD)    15 Aug 1996, version vC2 (VCD)
  96h,08h,18h,C1h  ;PSX (LATE-PU-8,yaroze)   18 Aug 1996, version vC1 (yaroze)
  96h,09h,12h,C2h  ;PSX (PU-18) (japan)      12 Sep 1996, version vC2 (a.jap)
  97h,01h,10h,C2h  ;PSX (PU-18) (us/eur)     10 Jan 1997, version vC2 (a)
  97h,08h,14h,C2h  ;PSX (PU-20)              14 Aug 1997, version vC2 (b)
  98h,06h,10h,C3h  ;PSX (PU-22)              10 Jul 1998, version vC3 (a)
  99h,02h,01h,C3h  ;PSX/PSone (PU-23, PM-41) 01 Feb 1999, version vC3 (b)
  A1h,03h,06h,C3h  ;PSone/late (PM-41(2))    06 Jun 2001, version vC3 (c)
  (unknown)        ;PS2,   xx xxx xxxx, late PS2 models...?
```

#### 19h,21h --\> INT3(flags)
Returns the current status of the POS0 and DOOR switches. Bit0=HeadIsAtPos0,
Bit1=DoorIsOpen, Bit2-7=AlwaysZero.<br/>

#### 19h,22h --\> INT3("for Europe")
```
  Caution: Supported only in BIOS version vC1 and up. Not supported in vC0.
```
Indicates the region that console is to be used in:<br/>
```
  INT5(11h,10h)      --> NTSC, Japan (vC0)         --> requires "SCEI" discs
  INT3("for Europe") --> PAL, Europe               --> requires "SCEE" discs
  INT3("for U/C")    --> NTSC, North America       --> requires "SCEA" discs
  INT3("for Japan")  --> NTSC, Japan / NTSC, Asia  --> requires "SCEI" discs
  INT3("for NETNA")  --> Region-free yaroze version--> requires "SCEx" discs
  INT3("for US/AEP") --> Region-free debug version --> accepts unlicensed CDRs
```
The CDROMs must contain a matching SCEx string accordingly.<br/>
The string "for Europe" does also suggest 50Hz PAL/SECAM video hardware.<br/>
The Yaroze accepts any normal SCEE,SCEA,SCEI discs, plus special SCEW discs.<br/>

#### 19h,23h --\> INT3("CXD2940Q/CXD1817Q/CXD2545Q/CXD1782BR") ;Servo Amplifier
#### 19h,24h --\> INT3("CXD2940Q/CXD1817Q/CXD2545Q/CXD2510Q")  ;Signal Processor
#### 19h,25h --\> INT3("CXD2940Q/CXD1817Q/CXD1815Q/CXD1199BQ") ;Decoder/FIFO
```
  Caution: Supported only in BIOS version vC1 and up. Not supported in vC0.
```
Indicates the chipset that the CDROM controller is intended to be used with.
The strings aren't always precisely correct (CXD1782BR is actually CXA1782BR,
ie. CXA, not CXD) (and CXD1199BQ chips exist on PU-7 boards, but later PU-8
boards do actually use CXD1815Q) (and CXD1817Q is actually CXD1817R) (and newer
PSones are using CXD2938Q or possibly CXD2941R chips, but nothing called
CXD2940Q).<br/>
Note: Yaroze responds by CXD1815BQ instead of CXD1199BQ (but not by CXD1815Q).<br/>

#### 19h,04h --\> INT3(stat) ;Read SCEx string (and force motor on)
Resets the total/success counters to zero, and does then try to read the SCEx
string from the current location (the SCEx is stored only in the Lead-In area,
so, if the drive head is elsewhere, it will usually not find any strings,
unless a modchip is permanently simulating SCEx strings).<br/>
This is a raw test command (the successful or unsuccessful results do not
lock/unlock the disk). The results can be read with command 19h,05h (which will
terminate the SCEx reading), or they can be read from RAM with command
19h,60h,lo,hi (which doesn't stop reading). Wait 1-2 seconds before expecting
any results.<br/>
Note: Like 19h,00h, this command forces the drive motor to spin at standard
speed (synchronized with the data on the disk), works even if the shell is open
(but stops spinning after a while if the drive is empty).<br/>

#### 19h,05h --\> INT3(total,success)  ;Get SCEx Counters
Returns the total number of "Sxxx" strings received (where at least the first
byte did match), and the number of full "SCEx" strings (where all bytes did
match). Typically, the values are "01h,01h" for Licensed PSX Data CDs, or
"00h,00h" for disk missing, unlicensed data CDs, Audio CDs.<br/>
The counters are reset to zero, and SCEx receive mode is active for a few
seconds after booting a new disk (on power up, on closing the drive door, on
sending a Reset command, and on sub\_function 04h). The disk is unlocked if the
"success" counter is nonzero, the only exception is sub\_function 04h which does
update the counters, but does not lock/unlock the disk.<br/>



##   CDROM - Test Commands - Test Drive Mechanics
Signal Processor and Servo Amplifier<br/>

#### 19h,50h,msb[,mid,[lsb[,xlo]]] --\> INT3(stat)
Sends an 8bit/16bit/24bit command to the hardware, depending on number of
parameters:<br/>
```
  1 byte  --> send CX(Xx)       ;short 8bit command
  2 bytes --> send CX(Xxxx)     ;longer 16bit command
  3 bytes --> send CX(Xxxxxx)   ;full 24bit command
  4 bytes --> send CX(Xxxxxxxx) ;extended 32bit command (BIOS vC3 only)
  4..15 bytes: acts same as max (3 or 4 bytes) (extra bytes are ignored)
  0 bytes or more than 15 bytes: generates an error
```

#### 19h,51h,msb[,mid,[lsb]] --\> INT3(stat,hi,lo)  ;BIOS vC2/vC3 only
Supported by newer CDROM BIOSes only (such that use CXD2545Q or newer chips).<br/>
Works same as 19h,50h, but does additionally receive a response.<br/>
The command is always sending a 24bit CX(Xxxxxx) command, but it doesn't verify
the number of parameter bytes (when using more than 3 bytes: extra bytes are
ignored, when using less than 3 bytes: garbage is appended, which is somewhat
valid because 8bit/16bit commands can be padded to 24bit size by appending
"don't care" bits).<br/>
The command can be used to send any CX(..) command, but actually it does make
sense only for the get-status commands, see below "19h,51h,39h,xxh"
description.<br/>

#### 19h,51h,39h,xxh --\> INT3(stat,hi,lo)  ;BIOS vC2/vC3 only
Supported by newer CDROM BIOSes only (such that use CXD2545Q or newer chips).<br/>
Sends CX(39xx) to the hardware, and receives a response (the response.hi byte
is usually 00h for 8bit responses, or 00h..01h for 9bit responses). For
example, this can be used to dump the Coefficient RAM.<br/>

#### 19h,03h --\> INT3(stat) ;force motor off
Forces the motor to stop spinning (ignored during spin-up phase).<br/>

#### 19h,17h --\> INT3(stat) ;force motor on, clockwise, super-fast
#### 19h,01h --\> INT3(stat) ;force motor on, anti-clockwise, super-fast
#### 19h,02h --\> INT3(stat) ;force motor on, anti-clockwise, super-fast
#### 19h,10h --\> INT3(stat) ;force motor on, anti-clockwise, super-fast
#### 19h,18h --\> INT3(stat) ;force motor on, anti-clockwise, super-fast
Forces the drive motor to spin at maximum speed (which is much faster than
normal or double speed), in normal (clockwise), or reversed (anti-clockwise)
direction. The commands work even if the shell is open. The commands do not try
to synchronize the motor with the data on the disk (and do thus work even if no
disk is inserted).<br/>

#### 19h,00h --\> INT3(stat) ;force motor on, clockwise (even if shell open)
This command seems to have effect only if the drive motor was off. If it was
off, it does FFh-fills the TOC entries in RAM, and seek to the begin of the TOC
at 98:30:00 or so (where minute=98 means minus two). From that location, it
follows the spiral on the disk, although it does occassionally jump back some
seconds. After clearing the TOC, the command does not write new data to the TOC
buffer in RAM.<br/>
Note: Like 19h,04h, this command forces the drive motor to spin at standard
speed (synchronized with the data on the disk), works even if the shell is open
(but stops spinning after a while if the drive is empty).<br/>

#### 19h,11h --\> INT3(stat) ;Move Lens Up (leave parking position)
#### 19h,12h --\> INT3(stat) ;Move Lens Down (enter parking position)
#### 19h,13h --\> INT3(stat) ;Move Lens Outwards (away from center of disk)
#### 19h,14h --\> INT3(stat) ;Move Lens Inwards (towards center of disk)
Moves the laser lens. The inwards/outwards commands do move ONLY the lens (ie.
unlike as for Seek commands, the overall-laser-unit remains in place, only the
lens is moved).<br/>

#### 19h,15h - if motor on: move head outwards + inwards + motor off
Moves the drive head to outer-most and inner-most position. Note that the drive
doesn't have a switch that'd tell the controller when it has reached the
outer-most position (so it'll forcefully hit against the outer edge) (ie. using
this command too often may destroy the drive mechanics).<br/>
Note: The same destructive hit-outer-edge effect happens when using Setloc/Seek
with too large values (like minute=99h).<br/>

#### 19h,16h --\> INT3(stat) ;Unknown / makes some noise if motor is on
#### 19h,19h --\> INT3(stat) ;Unknown / no effect
#### 19h,1Ah --\> INT3(stat) ;Unknown / makes some noise if motor is on
Seem to have no effect?<br/>
19h,16h seems to Move Lens Inwards, too.<br/>

#### 19h,06h,new --\> INT3(old) ;Adjust balance in RAM, and apply it via CX(30+n)
#### 19h,07h,new --\> INT3(old) ;Adjust gain in RAM, and apply it via CX(38+n)
#### 19h,08h,new --\> INT3(old) ;Adjust balance in RAM only
These commands are supported only by older CDROM BIOS versions (those with
CXA1782BR Servo Amplifier).<br/>
Later BIOSes will respond with INT5(11h,20h) when trying to use these commands
(because CXD2545Q and later Servo Amplifiers don't support the CX(30/38+n)
commands).<br/>



##   CDROM - Test Commands - Prototype Debug Transmission
#### Serial Debug Messages
Older CDROM BIOSes are supporting debug message transmission via serial bus,
using lower 3bit of the HC05 "databus" combined with the so-called "ROMSEL" pin
(which apparently doesn't refer to Read-Only-Memory, but rather something like
Runtime-Output-Message, or whatever).<br/>
Data is transferred in 24bit units (8bit command/index from HC05, followed by
16bit data to/from HC05), bigger messages are divided into multiple such 24bit
snippets.<br/>
There are no connectors for external debug hardware on any PSX mainboards, so
the whole stuff seems to be dating back to prototypes. And it seems to be
removed from later BIOSes (which appear to use "ROMSEL" as "SCLK"; for
receiving status info from the new CXD2545Q chips).<br/>

#### 19h,30h,index,dat1,dat2 --\> INT3(stat) ;Prototype/Debug stuff
#### 19h,31h,dat1,dat2 --\> INT3(stat) ;Prototype/Debug stuff
#### 19h,4xh,index --\> INT3(dat1,dat2) ;Prototype/Debug stuff
These functions are supported on older CDROM BIOS only; later BIOSes respond by
INT5(11h,10h).<br/>
The functions do not affect the CDROM operation (they do simple allow to
transfer data between Main CPU and external debug hardware).<br/>
Sub functions 30h and 31h may fail with INT5(11h,80h) when receiving wrong
signals on the serial input line.<br/>
Sub function "4xh" value can be 40h..4Fh (don't care).<br/>

#### INT5 Debug Messages
Alongsides to INT5 errors, the BIOS is usually also sending information via the
above serial bus (the error info is divided into multiple 8bit+16bit snippets,
and contains stat, error code, mode, current SubQ position, and most recently
issued command).<br/>



##   CDROM - Test Commands - Read/Write Decoder RAM and I/O Ports
Caution: Below commands 19h,71h..76h are supported only in BIOS version vC1 and
up. Not supported in vC0.<br/>

#### 19h,71h,index --\> INT3(databyte) ;Read single register
index can be 00h..1Fh, bigger values seem to be mirrored to "index AND 1Fh",
with one exception: index 13h in NOT mirrored, instead, index 33h, 53h, 93h,
B3h, D3h, F3h return INT5(stat+1,10h), and index 73h returns INT5(stat+1,20h).<br/>
Aside from returning a value, the commands seem to DO something (like moving
the drive head when a disk is inserted). Return values are usually:<br/>
```
  index     value
  00h       04h      ;04h=empty, 8Eh=licensed, 24h=audio
  01h       [0B1h]   ;DCh=empty/licensed, DDh=audio
  02h       00h
  03h       00h          ;or variable when disk inserted
  04h       00h
  05h       80h          ;or 86h or 89h when disk inserted
  06h       C0h
  07h       02h
  08h       8Ah
  09h       C0h
  0Ah       00h
  0Bh       C0h
  0Ch       [1F2h]
  0Dh       [1F3h]
  0Eh       00h          ;or 8Eh or E6h when disk inserted    ;D4h/audio
  0Fh       00h          ;or sometimes 01h when disk inserted ;50h/audio
  10h       C0h
  11h       E0h
  12h       71h
  13h       stat
  14h       FFh
  15h..1Fh  C0h-filled        ;or 17h --> DEh
```

#### 19h,72h,index,databyte --\> INT3(stat) ;Write single register
```
  ;other response on param xx16h,xx18h with xx>00h
```

#### 19h,73h,index,len --\> INT3(databytes...) ;Read multiple registers (bugged)
#### 19h,74h,index,len,databytes --\> INT3(stat) ;Write multiple registers (bugged)
Same as read/write single register, but trying to transfer multiple registers
at once. BUG: The transfer should range from 00h to len-1, but the loop counter
is left uninitialized (set to X=48h aka "command number 19h-minus-1-mul-2"
instead of X=00h). Causing to the function to read/write garbage at index
48h..FFh, it does then wrap to 00h and do the correct intended transfer, but
the preceeding bugged part may have smashed RAM or I/O ports.<br/>

#### 19h,75h --\> INT3(remain.lo,remain.hi,addr.lo,addr.hi) ;Get Host Xfer Info
Returns a 4-byte value. In my early tests, on the first day it returned
B1h,CEh,4Ch,01h, on the next day 2Ch,E4h,95h,D5h, and on all following days
00h,C0h,00h,00h (no idea why/where the earlier values came from).<br/>
The first byte seems to be always 00h; no matter of [1F0h].<br/>
The second byte seems to be always C0h; no matter of [1F1h].<br/>
The third,fourth bytes are [1F2h,1F3h].<br/>
That two bytes are 0Ch,08h after Read commands.<br/>
```
  The first bytes are NOT affected by:
  destroying [1F0h] via too-many-parameters in command-buffer,
  changes to [1F1h] which may occur after read command (eg. may be 20h)
```

#### 19h,76h,len\_lo,len\_hi,addr\_lo,addr\_hi --\> INT3(stat) ;Prepare SRAM Transfer
Prepare Transfer to/from 32K SRAM.<br/>
After INT3, data can be read (same way as sector data after INT1).<br/>



##   CDROM - Test Commands - Read HC05 SUB-CPU RAM and I/O Ports
#### 19h,60h,addr\_lo,addr\_hi --\> INT3(data) ;Read one byte from Drive RAM or I/O
Reads one byte from the controller's RAM or I/O area, see the memory map below
for more info. Among others, the command allows to read Subchannel Q data, eg.
at [200h..209h], including ADR=2/UPC/EAN and ADR=3/ISRC values (which are
suppressed by GetlocP). Eg. wait for ADR\<\>2, then for ADR=2, then read
the remaining 9 bytes (because of the delayed IRQs, this works only at single
speed) (at double speed one can read only 5 bytes before the values get
overwritten by new data). Unknown if older boards (with 4.00MHz oscillators)
are fast enough to read all 10 SubQ bytes.<br/>

#### CDROM Controller I/O Area and RAM Memory Map
First 40h bytes are I/O ports (as in MC68HC05 datasheet):<br/>
```
  000h 4        FF 7B 00 FF  (other when disk inserted)
  004h 5        11 00 20 20 0C
  009h 1        00 (when disk inserted: changes between 00 or 80)
  00Ah 2        71 00
  00Ch 1        00 (when disk inserted: changes between 00 or 80)
  00Dh 3        20 20 20
  010h 8        02 80 00 60 00 00 99(orBB) 98
  018h 4     changes randomly (even when no disk inserted)
  01Ch 3        40 00 41
  01Fh 1     changes randomly (even when no disk inserted)
  020h 30    20h-filled
  03Eh 2        82h 20h
```
Next 200h bytes are RAM:<br/>
```
  040h 4        08 00 00 00  ;or 98 07 xx 0B when disk inserted ;[40].Bit1=MUTE
  044h 4     00h-filled
  048h 3        40 20 00     ;or 58 71 0F when disk inserted
  04Bh 1     changes randomly (nodisk: 00 or 80 / disk: BFh)
  04Ch 1     Zero (or C0h)
  04Dh 3     MM:SS:FF (begin of current track MM:SS:00h) (or increasing addr)
  050h 10    Subchannel Q (adjusted position values)
  05Ah 2        ...
  05Ch 1     00h (or 64h)
  05Dh 3     MM:SS:FF (current read address) (sticky address during pause)
  060h 1     increments at circa 16Hz or so (or other rate when spinning)
  061h 12    00h-filled ;or else when disk inserted
  06Dh 1        01      ;or 0C when disk inserted
  06Eh 2     SetFilter setting (file,channel)
  070h 16    00h-filled ;or else when disk inserted
  080h 8     00h-filled
  088h 3        03:SS:FF (three, second, fraction)
  08Bh 3        03:SS:FF (three, second, fraction)
  08Eh 2        01 FF (or other values)
  090h 1        00h (or 91h when disk inserted + spinning)
  091h 13    Zero
  09Eh 1        00h (or 01h when disk inserted + spinning)
  09Fh 1     Zero
  0A0h 1     Always 23h
  0A1h 1        09h (5Dh when disk inserted)
  0A2h 7     00h-filled
  0A9h 1        40
  0AAh 4     00h-filled
  0AEh 1        00 (no disk) or 01 (disk) or so
  0AFh 1        00            ;or 06 when disk inserted
  0B0h 7        00 DC 00 02 00 E0 08             ;\or else when disk inserted
  0B7h 1        20         ;Bit6+7=MUTE          ;
  0B8h 3        DE 00 00                         ;/
  0BBh 1     SetMode setting (mode)
  0BCh 1     GetStat setting (stat)
  0BDh 3     00h-filled
  0C0h 6     FFh-filled            ;stack...                    ;\
  0C6h 1     Usually DFh           ;sometimes [0EBh and up] are non-FFh, too
  0C7h 15    FFh-filled            ;(depending on disk or commands or so)
  0D6h 1     Usually FDh (or FFh)  ;                            ;
  0D7h 24    FFh-filled                                         ; stack
  0EFh 4     on power-up FFh-filled, other once when disk read  ;
  0F3h 7     changes randomly (even when no disk inserted)      ;
  0FAh 6       2E 3C 2A D6 10 95                                ;/
  100h 2x99  TOC Entries for Start of Track 1..99 (MM:SS)
  1C6h 1     TOC First Track number (usually 01h)
  1C7h 1     TOC Last Track number (usually 01h or higher)
  1C8h 3     TOC Entry for Start of Lead-Out (MM:SS:FF)
  1CBh 2     Zero
  1CDh 1     Depends on disk (01 or 02 or 06) (or 00 when no disk)
  1CEh 1     Zero
  1CFh 1     Depends on disk (NULL minus N*6) (or 00 when no disk)
               (maybe reflection level / laser intensity or so)
                [1CDh..1CFh]
                01 00 E8 --> licensed/metalgear/kain
                01 00 EE --> licensed/alone2
                06 00 E2 or 00 00 02 00 E8 --> licensed/wipeout
                02 00 DC --> unlicensed/elo
                02 00 D6 --> unlicensed/driver
                00 00 EE --> audio/lola
                00 00 FA --> audio/marilyn
                00 00 F4 --> audio/westen
                00 00 00 --> disk missing
               last byte is always in steps of 6
  1D0h 4     SCEx String
  1D4h 4     Zero
  1D8h 2     SCEx Counters (total,success)  ;for command 19h,05h
  1DAh 6       00h-filled     (or ... SS:FF)
  1E0h 6     Command Buffer (usually 19h,60h,E2h,01h = Read RAM Command)
  1E6h 7       00h-filled (unless destroyed by more-than-6-byte-commands)
  1EDh 3     Setloc setting (MM:SS:FF)
  1F0h 1       00h          (unless destroyed by more-than-6-byte-commands)
  1F1h 3       C0h 00h 00h ;or 20h,0Ch,50h or C0h,0Ch,08h ;for command(19h,75h)
                           ;or 00h,00h,00h for audio
                           ;or 80h,00h,00h for disk missing
  1F4h 4       00h-filled ... or SCEx string
  1F8h 1       00h
  1F9h 1     Selected Target (parameter from Play and SetSession commands)
  1FAh 5       00h-filled       ;01 01 00 8B 00 00   ;or 01 02 8B 00 00
                       01 00 8B 00 00 -- audio/unlicensed
                       01 01 00 00 00 -- licensed
  1FFh 1       00h-on power up, changes when disk inserted  ;or 01 = Playing
    1FDh 3       MM:SS:FF (only during command 19h,00h) (MM=98..99=TOC)
  200h 10    Subchannel Q (real values)
  20Ah 2       whatever
  20Ch 1     Zero
  20Dh 1     Desired Session (from SetSession command)
  20Eh 1     Current Session (actual location of drive head)
  20Fh 1     Zero
  210h 10    Subchannel Q (adjusted position values)
  21Ah 6     00h-filled
  220h 4     Data Sector Header (MM:SS:FF:Mode)
  224h 4     Data Sector CD-XA Subheader (file,channel,sm,ci)
  228h 1         00h
  229h 1     Usually 00h (shortly other value on power-up, and maybe on seek)
  22Ah 1         10h (or 00h when no disk)
  22Bh 3     00h-filled
  22Eh 2         01,03 or 0A,00 or 03,01 (or else for other disk)
  230h 3     00h-filled (or other during spin-up / read-toc or so)
  233h 0Dh   00h-filled (unused RAM)
```
Other/invalid addresses are:<br/>
```
  240h..2FFh  - Invalid (00h-filled) (no ROM, RAM, or I/O mapped here)
  300h..3FFh  - Mirror of 200h..2FFh    ;\the BIOS is doing that
  400h..FFFFh - Mirrors of 000h..3FFh   ;/mirroring by software
```

#### Writing to RAM
There is no command for writing to RAM. Except that, one can write to the
command/parameter buffer at 1E0h and up. Normally, the longest known command
should have 6 bytes (19h,76h,a,b,c,d), and longer commands results in "bad
number of parameters" response - however, despite of that error message, the
controller does still store ALL parameter bytes in RAM (at address 1E1h..2E0h,
then wrapping back to 1E1h). Whereas, writing more than 16 bytes (FIFO storage
size) will mirror the FIFO content twice, and more than 32 bytes (FIFO counter
size) will work only when feeding extra data into the FIFO during transmission.
Anyways, writing to 1E1h and up doesn't allow to do interesting things (such
like manipulating the stack and executing custom code on the CPU).<br/>

#### Subchannel Q Notes
The "adjusted position values" at 050h, 210h, 310h contain only position
information (with ADR=1) (the PSX seems to check only the lower 2bit of the
4bit ADR value, so it also treats ADR=5 as ADR=1, too). Additionally, during
Lead-In, bytes 7..9 are overwritten by the position value from bytes 3..5. The
"real values" contain unadjusted data, including ADR=2 and ADR=3 etc.<br/>



##   CDROM - Secret Unlock Commands
#### SecretUnlockPart1 - Command 50h --\> INT5(11h,40h)
#### SecretUnlockPart2 - Command 51h,"Licensed by" --\> INT5(11h,40h)
#### SecretUnlockPart3 - Command 52h,"Sony" --\> INT5(11h,40h)
#### SecretUnlockPart4 - Command 53h,"Computer" --\> INT5(11h,40h)
#### SecretUnlockPart5 - Command 54h,"Entertainment" --\> INT5(11h,40h)
#### SecretUnlockPart6 - Command 55h,\<region\> --\> INT5(11h,40h)
#### SecretUnlockPart7 - Command 56h --\> INT5(11h,40h)
```
  Caution: Supported only in BIOS version vC1 and up. Not supported in vC0.
  Caution: Supported only in Europe/USA. Nonfunctional in Japan/Asia.
  Caution: When unsupported, Parameter Fifo isn't cleared after the command.
```
Sending these commands with the correct strings (in order 50h through 56h) does
disable the "SCEx" protection. The region can be detected via test command
19h,22h, and must be translated to the following \<region\> string:<br/>
```
  "of America"    ;for NTSC/US          ;\
  "(Europe)"      ;for PAL/Europe       ; handled, and actually working
  "World wide"    ;for Yaroze           ;/
  "Inc."          ;for NTSC/JP          ;-non-functional
```
In the unlocked state, ReadN/ReadS are working for unlicensed CD-Rs, and for
imported CDROMs from other regions (both without needing modchips). However
there are some cases which may still cause problems: The GetID command (1Ah)
does still identify the disc as being unlicensed, same for the Get SCEx
Counters test command (19h,05h). And, if a game should happen to send the Reset
command (1Ch) for some weird reason, then the BIOS would forget the unlocking,
same for games that set the "HCRISD" I/O port bit. On the contrary,
opening/closing the drive door does not affect the unlocking state.<br/>
The commands have been discovered in September 2013, and appear to be supported
by all CDROM BIOS versions (from old PSXes up to later PSones).<br/>
Note that the commands do always respond with INT5 errors (even on successful
unlocking).<br/>
Japanese consoles are internally containing code for processing the Secret
Unlock commands, but they are not actually executing that code, and even if
they would do so: they are ignoring the resulting unlocking flag, making the
commands nonfunctional in Japan/Asia regions.<br/>

#### SecretLock - Command 57h --\> INT5(11h,40h)
Undoes the unlocking and restores the normal locked state (same happens when
sending the Unlocking commands in wrong order or with wrong parameters).<br/>

#### SecretCrash - Command 58h..5Fh --\> Crash
Jumps to a data area and executes random code. Results are more or less
unpredictable (as they involve executing undefined opcodes). Eventually the CPU
might hit a RET opcode and recover from the crash.<br/>



##   CDROM - Video CD Commands
```
  Caution: Supported only on SCPH-5903, not supported on any other consoles.
  Caution: When unsupported, Parameter Fifo isn't cleared after the command.
```

```
  1Fh VideoCD      sub,a,b,c,d,e   INT3(stat,a,b,c,d,e)   ;<-- SCPH-5903 only
  1Fh..4Fh -       -               INT5(11h,40h)  ;-Unused/invalid
```

#### VideoCdSio - Cmd 1Fh,01h,JoyL,JoyH,State,Task,0 --\> INT3(stat,req,mm,ss,ff,x)
The JoyL/JoyH bytes contain 16bit button (and drive door) bits:<br/>
```
  0  Drive Door  (0=Open)    (from CDROM stat bit4) ;Open
  1  Button /\   (0=Pressed) (from PSX pad bit12) ;N/A       ;PBC: Back/LevelUp
  2  Button []   (0=Pressed) (from PSX pad bit15) ;Enter Menu
  3  Button ()   (0=Pressed) (from PSX pad bit13) ;Leave Menu     ;PBC: Confirm
  4  Button ><   (0=Pressed) (from PSX pad bit14) ;N/A
  5  Start       (0=Pressed) (from PSX pad bit3)  ;Play/Pause
  6  Select      (0=Pressed) (from PSX pad bit0)  ;Stop (prompt restart/resume)
  7  Always 0    (0)         (fixed)              ;N/A
  8  DPAD Up     (0=Pressed) (from PSX pad bit4)  ;Menu Up           ;PBC: +1
  9  DPAD Right  (0=Pressed) (from PSX pad bit5)  ;Menu Right/change ;PBC: +10
  10 DPAD Down   (0=Pressed) (from PSX pad bit6)  ;Menu Down         ;PBC: -1
  11 DPAD Left   (0=Pressed) (from PSX pad bit7)  ;Menu Left/change  ;PBC: -10
  12 Button R1   (0=Pressed) (from PSX pad bit11) ;Prev Track/Restart Track
  13 Button R2   (0=Pressed) (from PSX pad bit9)  ;Fast Forward (slowly)
  14 Button L1   (0=Pressed) (from PSX pad bit10) ;Next Track (if any)
  15 Button L2   (0=Pressed) (from PSX pad bit8)  ;Fast Backward (slowly)
```
The State byte can be:<br/>
```
  00h  Motor Off (or spin-up)   (when stat.bit1=0)
  01h  Playing                  (when stat.bit7=1)
  02h  Paused (and not seeking) (when stat.bit6=0)
  (note: State remains unchanged when seeking)
```
The Task byte can be:<br/>
```
  00h = Confirms that "Tocread" (aka setsession 1) request was processed
  01h = Detect VCD Disc (used on power-up, and after door open) (after spin-up)
  02h = Handshake (request ack response)
  0Ah = Door opened during play (int5/door error)
  80h = No disc
  FFh = No change (nop)
```
The req byte in the INT3 response can be:<br/>
```
  00h  Normal (no special event occured and no action requested)
  01h  Request CD to Seek_and_play (using mm:ss:ff response parameter bytes)
  02h  Request CD to Pause                ;cmd(09h)    -->int3(stat),int2(stat)
  03h  Request CD to Stop                 ;cmd(08h)    -->int3(stat),int2(stat)
  04h  Request CD to Tocread (setsession1);cmd(12h,01h)-->int3(stat),int2(stat)
  05h  Handshake Command was processed, and this is the "ack" response
  06h  Request CD to Fast Forward         ;cmd(04h)    -->int3(stat)
  07h  Request CD to Fast Backward        ;cmd(05h)    -->int3(stat)
  80h  Detect Command was processed, and disc was detected as VCD
  81h  Detect Command was processed, and disc was detected as Non-VCD
```

#### VideoCdSwitch - Cmd 1Fh,02h,flag,x,x,x,x --\> INT3(stat,0,0,x,x,x)
```
  00h      = Normal PSX Mode  (PortF.3=LOW)  (Audio/Video from GPU/SPU chips)
  01h..FFh = Special VCD Mode (PortF.3=HIGH) (Audio/Video from MDEC/OSD chips)
```

#### Some findings on the SC430924 firmware...
The version/date is "15 Aug 1996, version C2h", although the "C2h" is
misleading: The firmware is nearly identical to version "C1h" from PU-8 boards
(the stuff added in normal "C2h" versions would be for PU-18 boards with
different cdrom chipset).<br/>

Compared to the original C1h version, there are only a few changes: A
initialization function for initializing port F on power-up. And new command
(command 1Fh, inserted in the various command tables), with two subfunctions
(01h and 02h):<br/>
- Command 1Fh,01h,a,b,c,d,e --\> INT3(stat,a,b,c,d,e) Serial 5-byte
read-write<br/>
- Command 1Fh,02h,v,x,x,x,x --\> INT3(stat,0,0,x,x,x) Toggle 1bit (port
F.bit3)<br/>
Whereas,<br/>
```
  x = don't care/garbage
  v = toggle state (00h=normal=PortF.3=LOW, 01h..FFh=special=PortF.3=HIGH)
      (toggle gpu vs mpeg maybe?)
  a,b,c,d,e = five bytes sent serially, and five bytes response received
      serially (send/receive done simultaneously)
```

The Port F bits are:<br/>
```
  Port F.Bit0 = Serial Data In
  Port F.Bit1 = Serial Data Out
  Port F.Bit2 = Serial Clock Out
  Port F.Bit3 = Toggle (0=Normal, 1=Special)
```

And that's about all. Ie. essentially, the only change is that the new command
controls Port F. There is no interaction with the remaining firmware (ie.
reading, seeking, and everything is working as usually, without any video-cd
related changes).<br/>
The SCEx stuff is also not affected (ie. Video CDs would be seen as unlicensed
discs, so the PSX couldn't read anything from those discs, aside from Sub-Q
position data, of course). The SCEx region is SCEI aka "Japan" (or actually for
Asia in this case).<br/>

#### Note
The SPU MUTE Flag (SPUCNT.14) does also affect VCD Audio (mute is applied to
the final analog audio amplifier). All other SPUCNT bits can be zero for VCD.<br/>



##   CDROM - Mainloop/Responses
#### SUB-CPU Mainloop
The SUB-CPU is running a mainloop that is handling hardware events (by simple
polling, not by IRQs):<br/>
```
  check for incoming sectors (from CDROM decoder)
  check for incoming commands (from Main CPU)
  do maintenance stuff on the drive mechanics
```
There is no fixed priority: if both incoming sector and incoming command are
present, then the SUB-CPU may handle either one, depending on which portion of
the mainloop it is currently executing.<br/>
There is no fixed timing: if the mainloop is just checking for a specific
event, then a new event may be processed immediately, otherwise it may take
whole mainloop cycle until the SUB-CPU sees the event.<br/>
Whereas, the mainloop cycle execution time isn't constant: It may vary
depending on various details. Especially, some maintenance stuff is only
handled approximately around 15 times per second (so there are 15 slow mainloop
cycles per second).<br/>

#### Responses
The PSX can deliver one INT after another. Instead of using a real queue, it's
merely using some flags that do indicate which INT(s) need to be delivered.
Basically, there seem to be two flags: One for Second Response (INT2), and one
for Data/Report Response (INT1). There is no flag for First Response (INT3);
because that INT is generated immediately after executing a command.<br/>
The flag mechanism means that the SUB-CPU cannot hold more than one undelivered
INT1. That, although the CDROM Decoder does notify the SUB-CPU about all newly
received sectors, and it can hold up to eight sectors in the 32K SRAM. However,
the SUB-CPU BIOS merely sets a sector-delivery-needed flag (instead of
memorizing which/how many sectors need to be delivered, and, accordingly, the
PSX can use only three of the available eight SRAM slots: One for currently
pending INT1, one for undelivered INT1, and one for currently/incompletly
received sector).<br/>

#### First Response (INT3) (or INT5 if failed)
The first response is sent immediately after processing a command. In detail:<br/>
The mainloop checks for incoming commands once every some clock cycles, and
executes commands under following condition:<br/>
```
  Main CPU has sent a command, AND, there is no INT pending
  (if an INT is pending, then the command won't be executed yet, but will be
  executed in following mainloop cycles; once when INT got acknowledged)
  (even if no INT is pending, the mainloop may generate INT1/INT2 before
  executing the command, if so, as said above, the command won't execute yet)
```
Once when the command gets executed it will sent the first response immediately
after the command execution (which may only take a few clock cycles, or some
more cycles, for example Init/ReadTOC do include some time consuming
initializations). Anyways, there will be no other INTs generated during command
execution, so once when the command execution has started, it's guaranteed that
the next INT will contain the first response.<br/>

#### Second Responses (INT2) (or INT5 if failed)
Some commands do send a second response after actual command execution:<br/>
```
  07h MotorOn    E -               INT3(stat), INT2(stat)
  08h Stop       E -               INT3(stat), INT2(stat)
  09h Pause      E -               INT3(stat), INT2(stat)
  0Ah Init         -               INT3(late-stat), INT2(stat)
  12h SetSession E session         INT3(stat), INT2(stat)
  15h SeekL      E -               INT3(stat), INT2(stat)  ;\use prior Setloc
  16h SeekP      E -               INT3(stat), INT2(stat)  ;/to set target
  1Ah GetID      E -               INT3(stat), INT2/5(stat,flg,typ,atip,"SCEx")
  1Dh GetQ       E adr,point       INT3(stat), INT2(10bytesSubQ,peak_lo)
  1Eh ReadTOC      -               INT3(late-stat), INT2(stat)
```
In some cases (like seek or spin-up), it may take more than a second until the
2nd response is sent.<br/>
It should be highly recommended to WAIT until the second response is generated
BEFORE sending a new command (it wouldn't make too much sense to send a new
command between first and second response, and results would be unknown, and
probably totally unpredictable).<br/>
Error Notes: If the command has been rejected (INT5 sent as 1st response) then
the 2nd response isn't sent (eg. on wrong number of parameters, or if disc
missing). If the command fails at a later stage (INT5 as 2nd response), then
there are cases where another INT5 occurs as 3rd response (eg. on
SetSession=02h on non-multisession-disk).<br/>

#### Data/Report Responses (INT1)
```
  03h Play       E (track)         INT3(stat), optional INT1(report bytes)
  04h Forward    E -               INT3(stat), optional INT1(report bytes)
  05h Backward   E -               INT3(stat), optional INT1(report bytes)
  06h ReadN      E -               INT3(stat), INT1(stat), datablock
  1Bh ReadS      E?-               INT3(stat), INT1(stat), datablock
```



##   CDROM - Response Timings
Here are some response timings, measured in 33MHz units on a PAL PSone. The
CDROM BIOSes mainloop is doing some maintenance stuff once and when, meaning
that the response time will be higher in such mainloop cycles (max values), and
less in normal cycles (min values). The maintenance timings do also depend on
whether the motor is on or off (and probably on various other factors like
seeking).<br/>

#### First Response
The First Response interrupt is sent almost immediately after processing the
command (that is, when the mainloop sees a new command without any old
interrupt pending). For GetStat, timings are as so:<br/>
```
  Command                Average   Min       Max
  GetStat (normal)       000c4e1h  0004a73h..003115bh
  GetStat (when stopped) 0005cf4h  000483bh..00093f2h
```
Timings for most other commands should be similar as above. One exception is
the Init command, which is doing some initialization before sending the 1st
response:<br/>
```
  Init                   0013cceh  000f820h..00xxxxxh
```
The ReadTOC command is doing similar initialization, and should have similar
timing as Init command. Some (rarely used) Test commands include things like
serial data transfers, which may be also quite slow.<br/>

#### Second Response
```
  Command                Average   Min       Max
  GetID                  0004a00h  0004922h..0004c2bh
  Pause (single speed)   021181ch  020eaefh..0216e3ch ;\time equal to
  Pause (double speed)   010bd93h  010477Ah..011B302h ;/about 5 sectors
  Pause (when paused)    0001df2h  0001d25h..0001f22h
  Stop (single speed)    0d38acah  0c3bc41h..0da554dh
  Stop (double speed)    18a6076h  184476bh..192b306h
  Stop (when stopped)    0001d7bh  0001ce8h..0001eefh
```
Moreover, Seek/Play/Read/SetSession/MotorOn/Init/ReadTOC are sending second
responses which depend on seek time (and spin-up time if the motor was off).
The seek timings are still unknown, and they are probably quite complicated:<br/>
The CDROM BIOS seems to split seek distance somehow into coarse steps (eg.
minutes) and fine steps (eg. seconds/sectors), so 1-minute seek distance may
have completely different timings than 59-seconds distance.<br/>
The amount of data per spiral winding increases towards ends of the disc (so
the drive head will need to be moved by shorter distance when moving from
minute 59 to 60 as than moving from 00 to 01).<br/>
The CDROM BIOS contains some seek distance table, which is probably optimized
for 72-minute discs (or whatever capacity is used on original PSX discs).
80-minute CDRs may have tighter spiral windings (the above seek table is
probably causing the drive head to be moved too far on such discs, which will
raise the seek time as the head needs to be moved backwards to compensate that
error).<br/>

#### INT1 Rate
```
  Command                Average   Min       Max
  Read (single speed)    006e1cdh  00686dah..0072732h
  Read (double speed)    0036cd2h  00322dfh..003ab2bh
```
The INT1 rate needs to be precise for CD-DA and CD-XA Audio streaming, exact
clock cycle values should be: SystemClock\*930h/4/44100Hz for Single Speed (and
half as much for Double Speed) (the "Average" values are AVERAGE values, not
exact values).<br/>



##   CDROM - Response/Data Queueing
[Below are some older/outdated test cases]<br/>

#### Sector Buffer
The CDROM sector buffer is 32Kx8 SRAM (IC303). The buffer is apparently divided
into 8 slots, theoretically allowing to buffer up to 8 sectors.<br/>
BUG: The drive controller seems to allow only 2 of those 8 sectors (the oldest
sector, and the current/newest sector).<br/>
Ie. after processing the INT1 for the oldest sector, one would expect the
controller to generate another INT1 for next newer sector - but instead it
appears to jump directly to INT1 for the newest sector (skipping all other
unprocessed sectors). There is no known way to get around that effect.<br/>
So far, the big 32Kbyte buffer is entirely useless (the two accessible sectors
could have been as well stored in a 8Kbyte chip) (unless, maybe the 32Kbytes
have been intended for some error-correction "read-ahead" purposes, rather than
as "look-back" buffer for old sectors; one of the unused slots might be also
used for XA-ADPCM sectors).<br/>
The bottom line is that one should process INT1's as soon as possible (ie.
before the cdrom controller receives and skips further sectors). Otherwise
sectors would be lost without notice (there appear to be absolutely no overrun
status flags, nor overrun error interrupts).<br/>

#### Update:
This is confirmed, as found in the SCEA_BBS.pdf bulletin board archive:
```
12/29/95 10:24 AM
Re(4): CD buffer
Thomas Boyd
CD
Dan Burnash
OK. This is the story of the CD ROM subsystem sector buffer:
The CD-ROM subsystem sector buffer is currently 32K. It is located in the CD-ROM subsystem.
It uses a sort-of tripple buffering system to read sectors in and make one (and ONLY one) sector
available to the user.
Common questions that spring to mind and their answers:
Q: 32K - (2352 bytes/sector)*(3 buffered sectors) = lots of leftover RAM! Can I use it? A: No. It is
not accessible by anything but the CD-ROM subsystem.
Q: How dissappointing. As consolation, can I be told what the extra memory is used for? A: The
memory was going to be used for sound mapping, but (1) the system would be too slow, and
(2) sound mapping is already done by the SPU. The current implementation of this memory is ...
nothing. It is vestigal and will be cut out in future manufacturing cost reduction designs.
Tom
```

#### Sector Buffer Test Cases
```
  Setloc(0:2:0)+Read
  Process INT1 --> receives sector header for 0:2:0
  Process INT1 --> receives sector header for 0:2:1
  Process INT1 --> receives sector header for 0:2:2
  Process INT1 --> receives sector header for 0:2:3
```
Above shows the normal flow when processing INT1's as they arise. Now,
inserting delays (and not processing INT1's during that delays):<br/>
```
  Setloc(0:2:0)+Read
  Process INT1 --> receives sector header for 0:2:0
  delay(1)
  Process INT1 --> receives sector header for 0:2:1 (oldest sector)
  Process INT1 --> receives sector header for 0:2:6 (newest sector)
  Process INT1 --> receives sector header for 0:2:7 (next sector)
```
Above suggests that the CDROM buffer can hold max 2 sectors (the oldest and
current one). However, using a longer delay:<br/>
```
  Setloc(0:2:0)+Read
  Process INT1 --> receives sector header for 0:2:0
  delay(2)
  Process INT1 --> receives sector header for 0:2:9  (oldest/overwritten)
  Process INT1 --> receives sector header for 0:2:11 (newest sector)
  Process INT1 --> receives sector header for 0:2:12 (next sector)
```
Above indicates that sector buffer can hold 8 sectors (as the sector 1 slot is
overwritten by sector 9). And, another test with even longer delay:<br/>
```
  Setloc(0:2:0)+Read
  Process INT1 --> receives sector header for 0:2:0
  delay(3)
  Process INT1 --> receives sector header for 0:2:17 (currently received)
  Process INT1 --> receives sector header for 0:2:16 (newest full sector)
  Process INT1 --> receives sector header for 0:2:17 (next sector)
  Process INT1 --> receives sector header for 0:2:18 (next sector)
```
Above is a special case where sector 17 appears twice; the first one is the
sector 1 slot (which was overwritten by sector 9, and apparently then half
overwritten by sector 17).<br/>

#### Sector Buffer VS GetlocL Response Tests
```
  Setloc(0:2:0)+Read
  Process INT1 --> receives sector header for 0:2:0
  GetlocL
  Process INT3 --> receives getloc info for 0:2:0
  Process INT1 --> receives sector header for 0:2:1
  Process INT1 --> receives sector header for 0:2:2
  Process INT1 --> receives sector header for 0:2:3
```
Another test, with Delay BEFORE Getloc:<br/>
```
  Setloc(0:2:0)+Read
  Process INT1 --> receives sector header for 0:2:0
  Delay(1)
  GetlocL
  Process INT1 --> receives sector header for 0:2:1
  Process INT3 --> receives getloc info for 0:2:6
  Process INT1 --> receives sector header for 0:2:6
  Process INT1 --> receives sector header for 0:2:7
```
Another test, with Delay AFTER Getloc:<br/>
```
  Setloc(0:2:0)+Read
  Process INT1 --> receives sector header for 0:2:0
  GetlocL
  Delay(1)
  Process INT3 --> receives getloc info for 0:2:0
  Process INT1 --> receives sector header for 0:2:5
  Process INT1 --> receives sector header for 0:2:6
  Process INT1 --> receives sector header for 0:2:7
```
Another test, with Delay BEFORE and AFTER Getloc:<br/>
```
  Setloc(0:2:0)+Read
  Process INT1 --> receives sector header for 0:2:0
  Delay(1)
  GetlocL
  Delay(1)
  Process INT1 --> receives sector header for 0:2:9
  Process INT1 --> receives sector header for 0:2:11
  Process INT3 --> receives getloc info for 0:2:12
  Process INT1 --> receives sector header for 0:2:12
  Process INT1 --> receives sector header for 0:2:13
```

#### Sector Buffer VS Pause Response Tests
```
  Setloc(0:2:0)+Read
  Process INT1 --> receives sector header for 0:2:0
  Pause
  Process INT3 --> receives stat=22h (first pause response)
  Process INT2 --> receives stat=02h (second pause response)
```
Another test, with Delay BEFORE Pause:<br/>
```
  Setloc(0:2:0)+Read
  Process INT1 --> receives sector header for 0:2:0
  Delay(1)
  Pause
  Process INT1 --> receives sector header for 0:2:1 (oldest)
  Process INT3 --> receives stat=22h (first pause response)
  Process INT2 --> receives stat=02h (second pause response)
```
Another test, with Delay AFTER Pause:<br/>
```
  Setloc(0:2:0)+Read
  Process INT1 --> receives sector header for 0:2:0
  Pause
  Delay(1)
  Process INT3 --> receives stat=22h (first pause response)
  Process INT2 --> receives stat=02h (second pause response)
```
Another test, with Delay BEFORE and AFTER Pause:<br/>
```
  Setloc(0:2:0)+Read
  Process INT1 --> receives sector header for 0:2:0
  Delay(1)
  Pause
  Delay(1)
  Process INT1 --> receives sector header for 0:2:9 (oldest/overwritten)
  Process INT3 --> receives stat=22h (first pause response)
  Process INT2 --> receives stat=02h (second pause response)
```
For above: Note that, despite of Pause, the CDROM is still writing to the
internal buffer (and overwrites slot 1 by sector 9) (this might be because the
Pause command isn't processed at all until INT1 is processed).<br/>

#### Double Commands (Getloc then Pause)
```
  Setloc(0:2:0)+Read
  Process INT1 --> receives sector header for 0:2:0
  GetlocL
  Pause
  Process INT3 --> receives stat=22h (first pause response)
  Process INT2 --> receives stat=02h (second pause response)
```
Another test,<br/>
```
  Setloc(0:2:0)+Read
  Process INT1 --> receives sector header for 0:2:0
  Delay(1)
  GetlocL
  Pause
  Process INT1 --> receives sector header for 0:2:1
  Process INT1 --> receives sector header for 0:2:6
  Process INT3 --> receives stat=22h (first pause response)
  Process INT2 --> receives stat=02h (second pause response)
```
Another test,<br/>
```
  Setloc(0:2:0)+Read
  Process INT1 --> receives sector header for 0:2:0
  GetlocL
  Delay(1)
  Pause
  Process INT3 --> receives getloc info for 0:2:0 (first getloc response)
  Process INT3 --> receives stat=22h (first pause response)
  Process INT2 --> receives stat=02h (second pause response)
```
Another test,<br/>
```
  Setloc(0:2:0)+Read
  Process INT1 --> receives sector header for 0:2:0
  Delay(1)
  GetlocL
  Delay(1)
  Pause
  Process INT1 --> receives sector header for 0:2:9 (oldest/overwritten)
  Process INT3 --> receives stat=22h (first pause response)
  Process INT2 --> receives stat=02h (second pause response)
```

#### Double Commands (Pause then Getloc)
```
  Setloc(0:2:0)+Read
  Process INT1 --> receives sector header for 0:2:0
  Pause
  GetlocL
  Process INT3 --> receives getloc info for 0:2:0 (first getloc response)
  Process INT1 --> receives sector header for 0:2:1
  Process INT1 --> receives sector header for 0:2:2
  Process INT1 --> receives sector header for 0:2:3
```
Another test,<br/>
```
  Setloc(0:2:0)+Read
  Process INT1 --> receives sector header for 0:2:0
  Delay(1)
  Pause
  GetlocL
  Process INT1 --> receives sector header for 0:2:1
  Process INT3 --> receives getloc info for 0:2:6 (first getloc response)
  Process INT1 --> receives sector header for 0:2:6
  Process INT1 --> receives sector header for 0:2:7
```
Another test,<br/>
```
  Setloc(0:2:0)+Read
  Process INT1 --> receives sector header for 0:2:0
  Pause
  Delay(1)
  GetlocL
  Process INT3 --> receives stat=22h (first pause response)
  Process INT3 --> receives getloc info for 0:2:6 (first getloc response)
  (No further INT's, ie. read is paused, but second-pause-response is lost).
```
Another test,<br/>
```
  Setloc(0:2:0)+Read
  Process INT1 --> receives sector header for 0:2:0
  Pause
  Delay(1)
  GetlocL
  Delay(1)
  Process INT3 --> receives stat=22h (first pause response)
  Process INT3 --> receives getloc info for 0:2:6 (first getloc response)
  Process INT2 --> receives stat=02h (second pause response)
```
Another test,<br/>
```
  Setloc(0:2:0)+Read
  Process INT1 --> receives sector header for 0:2:0
  Delay(1)
  Pause
  Delay(1)
  GetlocL
  Process INT1 --> receives sector header for 0:2:9
  Process INT1 --> receives sector header for 0:2:11
  Process INT3 --> receives getloc info for 0:2:12 (first getloc response)
  Process INT1 --> receives sector header for 0:2:12
  Process INT1 --> receives sector header for 0:2:13
```



##   CDROM Disk Format
#### Overview
The PSX uses a ISO 9660 filesystem, with data stored on CD-XA (Mode2) Sectors.
ISO 9660 is standard for CDROM disks, although newer CDROMs may use extended
filesystems, allowing to use long filenames and lowercase filenames, the PSX
Kernel doesn't support such stuff, and, in fact, it's putting some restrictions
on the ISO standard: it's limiting file names to MSDOS-style 8.3 format, and
it's allowing only a limited number of files and directories per disk.<br/>

#### CDROM Filesystem (ISO 9660 aka ECMA-119)
```
  Originally intended for Mode1 Sectors (but is also used for CD-XA Mode2)
  Supports "FILENAME.EXT;VERSION" filenames (version is usually "1")
  Supports all-uppercase filenames and directory names (0-9, A-Z, underscore)
  For PSX: Max 8-character filenames with max 3-character extensions
  For PSX: Max 8-character directory names, without extension
  For PSX: Max one sector per directory (?)
  For PSX: Max one sector (or less?) per path table (?)
```

#### CDROM Extended Architecture (CD-ROM XA aka CD-XA)
```
  Uses Mode2 Sectors (see Sector Encoding chapter)
  Allows 800h or 914h byte data per sector (with/without error correction)
  Allows to break interleaved data into separate files/channels
  Supports XA-ADPCM compressed audio data
  Stores "CD-XA001" at 400h Primary Volume Descriptor (?)
  Stores 14 extra bytes in System Use area (LEN_SU) of Directory Entries
```

#### Physical Audio/CDROM Disk Format (ISO/IEC 10149 aka ECMA-130)
```
  Defines physical metrics of the CDROM and Audio disks
  Defines Sub-channels and Track.Index and Minute.Second.Fraction numbering
  Defines 14bit-per-byte encoding, and splits sectors into frames
  Defines ECC and EDC (error correction and error detection codes)
```

#### Available Documentation
ISO documents are commercial standards (not available for download), however,
they are based on ECMA standards (which are free for download, however, the
ECMA stuff is in PDF format, so one may treat it as commercial bullshit, too).
CD-ROM XA is commercial only (not available for download), and, CD-XA doesn't
seem to have become very popular outside of the PSX-world, so there's very
little information available, portions of CD-XA are also used in the CD-i
standard (which may be a little better or worse documented).<br/>

#### Stuff
```
  sessions  one or more sessions per disk
  tracks    99 tracks per disk     (01h..99h) (usually only 01h on Data Disks)
  index     99 indices per track   (01h..99h) (rarely used, usually always 01h)
  minutes   74 minutes per disk    (00h..73h) (or more, with some restrictions)
  seconds   60 seconds per minute  (00h..59h)
  sectors   75 sectors per second  (00h..74h)
  frames    98 frames per sector
  bytes     33 bytes per frame (24+1+8 = data + subchannel + error correction)
  bits      14 bits per byte   (256 valid combinations, and many invalid ones)
```

#### Track.Index (stored in subchannel, in BCD format)
Multiple Tracks are usually used only on Audio Disks (one track for each song,
numbered 01h and up), a few Audio Disks may also split Tracks into separate
fragments with different Index values (numbered 01h and up, but most tracks
have only Index 01h). A simple Data Disk would usually contain only one Track
(all sectors marked Track=01h and Index=01h), although some more complex Data
Disks may have multiple Data tracks and/or Audio tracks.<br/>

#### Minute.Second.Sector (stored in subchannel, and in Data sectors, BCD format)
The sectors on CDROMs and CD Audio disks are numbered in Minutes, Seconds, and
1/75 fragments of a second (where a "second" is referring to single-speed
drives, ie. the normal CD Audio playback speed).<br/>
Minute.Second.Sector is stored twice in the subchannel (once the "absolute"
time, and once the "local" time).<br/>
The "absolute" sector number (counted from the begin of the disk) is mainly
relevant for Seek purposes (telling the controller if the drive head is on the
desired location, or if it needs to move the head backwards or forwards).<br/>
The "local" sector number (counted from the begin of the track) is mainly
relevant for Audio Players, allowing to pass the data directly to the
Minute:Second display, without needing to subtract the start address of the
track.<br/>
Data disks are additionally storing the "absolute" values in their Data Areas,
basically that's just the subchannel data duplicated, but more precisely
assigned - the problem with the subchannel data is that the CD Audio standard
seems to lack a clear definition that would assign the begin of the sub-channel
block to the exact begin of a sector; so, when using only the subchannel data,
some Drive Controllers may assign the begin of a new sector to another location
as than other Controllers do, for Audio Disks that isn't too much of a problem,
but for Data Disks it'd be fatal.<br/>

#### Subchannels
Each frame contains 8 subchannel bits (named P,Q,R,S,T,U,V,W). So, a sector
(with 98 frames) contains 98 bits (12.25 bytes) for each subchannel.<br/>
[CDROM Subchannels](cdromdrive.md#cdrom-subchannels)<br/>

#### Error Correction
Each Frame contains 8 bytes Error Correction information, which is mainly used
for Audio Disks, but it isn't 100% fail-proof, for that reason, Data Disks are
containing additional Error Correction in the 930h-byte data area (the audio
correction is probably focusing on repairing the MSBs of the 16bit samples, and
gives less priority on the LSBs). Error Correction is some kind of a huge
complex checksum, which allows to detect the location of faulty bytes, and to
fix them.<br/>

#### 930h-Byte Sectors
The "user" area for each sector is 930h bytes (2352 bytes). That region is
combined of the 24-byte data per frame (and excludes the 8-byte audio error
correction info, and the 1-byte subchannel data).<br/>
Most CDROM Controllers are only giving access to this 930h-byte region (ie.
there's no way to read the audio error correction info by software, and only
limited access to the subchannel data, such like allowing to read only the
Q-channel for showing track/minute/second in audio playback mode).<br/>
On Audio disks, the 930h bytes are plain data, on Data disks that bytes are
containing headers, error correction, and usually only 800h bytes user data
(for more info see Sector Encoding chapter).<br/>

#### Sessions
Multi-Sessions are mainly used on CDR's, allowing to append newer data at the
end of the disk at a later time. First of, the old session must contain a flag
indicating that there may be a newer session, telling the CDROM Controller to
search if one such exists (and if that is equally flagged, to search for an
even newer session, and so on until reaching the last and newest session).<br/>
Each session contains a complete new ISO Volume Descriptor, and may
additionally contain new Path Tables, new Directories, and new Files. The
Driver Controller is usually recursing only the Volume Descriptor of the newest
session. However, the various Directory Records of the new session may refer to
old files or old directories from previous sessions, allowing to "import" the
older files, or to "rename" or "delete" them by assigning new names to that
files, or by removing them from the directory.<br/>
The PSX is reportedly not supporting multi-session disks, but that doesn't seem
to be correct, namely, the Setsession command is apparently intended for that
purpose... though not sure if the PSX Kernel is automatically searching the
newest session... otherwise the boot executable in the first session would need
to do that manually by software, and redirect control to the boot executable in
the last session.<br/>



##   CDROM Subchannels
#### Subchannel P
Subchannel P contains some kind of a Pause flag (to indicate muted areas
between Audio Tracks). This subchannel doesn't have any checksum, so the data
cannot be trusted to be intact (unless when sensing a longer stream of
all-one's, or all zero's). Theoretically, the 98 pause bits are somehow
associated to the 98 audio frames (with 24 audio bytes each) of the sector.
However, reportedly, Subchannel P does contain two sync bits, if that is true,
then there'd be only 96 pause flags for 98 audio frames. Strange.<br/>
Note: Another way to indicate "paused" regions is to set Subchannel Q to ADR=1
and Index=00h.<br/>

#### Subchannel Q
contains the following information:<br/>
```
  Bits Expl.
  2    Sub-channel synchronization field
  8    ADR/Control (see below)
  72   Data (content depends on ADR)
  16   CRC-16-CCITT error detection code (big-endian: bytes ordered MSB, LSB)
```
Possible values for the ADR/Control field are:<br/>
```
  Bit0-3 ADR (0=No data, 1..3=see below, 4..0Fh=Reserved)
  Bit4   Audio Preemphasis  (0=No, 1=Yes)      (Audio only, must be 0 for Data)
  Bit5   Digital Copy       (0=Prohibited, 1=Allowed)
  Bit6   Data               (0=Audio, 1=Data)
  Bit7   Four-Channel Audio (0=Stereo, 1=Quad) (Audio only, must be 0 for Data)
```
The 72bit data regions are, depending on the ADR value...<br/>

#### Subchannel Q with ADR=1 during Lead-In -- Table of Contents (TOC)
```
  8    Track number (fixed, must be 00h=Lead-in)
  8    Point (01h..99h or A0h..A2h, see last three bytes for more info)
  24   MSF address (incrementing address within the Lead-in area)
         Note: On some disks, these values are choosen so that the lead-in
         <starts> at 00:00:00, on other disks so that it <ends> at 99:59:74.
  8    Reserved (00h)
```
When Point=01h..99h (Track 1..99) or Point=A2h (Lead-Out):<br/>
```
  24   MSF address (absolute address, start address of the "Point" track)
```
When Point=A0h (First Track Number):<br/>
```
  8    First Track number (BCD)
  8    Disk Type Byte (00h=CD-DA or CD-ROM, 10h=CD-I, 20h=CD-ROM-XA)
  8    Reserved (00h)
```
When Point=A1h (Last Track Number):<br/>
```
  8    Last Track number (BCD)
  16   Reserved (0000h)
```
ADR=1 should exist in 3 consecutive lead-in sectors.<br/>

#### Subchannel Q with ADR=1 in Data region -- Position
```
  8    Track number (01h..99h=Track 1..99)
  8    Index number (00h=Pause, 01h..99h=Index within Track)
  24   Track relative MSF address (decreasing during Pause)
  8    Reserved (00h)
  24   Absolute MSF address
```
ADR=1 is required to exist in at least 9 out of 10 consecutive data sectors.<br/>

#### Subchannel Q with ADR=1 during Lead-Out -- Position
```
  8    Track number (fixed, must be AAh=Lead-Out)
  8    Index number (fixed, must be 01h) (there's no Index=00h in Lead-Out)
  24   Track relative MSF address (increasing, 00:00:00 and up)
  8    Reserved (00h)
  24   Absolute MSF address
```
ADR=1 should exist in 3 consecutive lead-out sectors (and may be then followed
by ADR=5 on multisession disks).<br/>

#### Subchannel Q with ADR=2 -- Catalogue number of the disc (UPC/EAN barcode)
```
  52   EAN-13 barcode number (13-digit BCD)
  12   Reserved (000h)
  8    Absolute Sector number (BCD, 00h..74h) (always 00h during Lead-in)
```
If the first digit of the EAN-13 number is "0", then the remaining digits are a
UPC-A barcode number. Either the 13-digit EAN-13 number, or the 12-digit UPC-A
number should be printed as barcode on the rear-side of the CD package.<br/>
The first some digits contain a country code (EAN only, not UPC), followed by a
manufacturer code, followed by a serial number. The last digit contains a
checksum, which can be calculated as 250 minus the sum of the first 12 digits,
minus twice the sum of each second digit, modulated by 10.<br/>
ADR=2 isn't included on all CDs, and, many CDs do have ADR=2, but the 13 digits
are all zero. Most CDROM drives do not allow to read EAN/UPC numbers.<br/>
If present, ADR=2 should exist in at least 1 out of 100 consecutive sectors.
ADR=2 may occur also in Lead-in.<br/>

#### Subchannel Q with ADR=3 -- ISRC number of the current track
(ISO 3901 and DIN-31-621):<br/>
```
  12   Country Code      (two 6bit characters)   (ASCII minus 30h) ;eg. "US"
  18   Owner Code        (three 6bit characters) (ASCII minus 30h)
  2    Reserved          (zero)
  8    Year of recording (2-digit BCD) ;eg. 82h for 1982
  20   Serial number     (5-digit BCD) ;usually increments by 1 or 10 per track
  4    Reserved          (zero)
  8    Absolute Sector number (BCD, 00h..74h) (always 00h during Lead-in)
```
Most CDROM drives for PC's do not allow to read ISRC numbers (or even worse,
they may accidently return the same ISRC number on every two tracks).<br/>
If present, ADR=3 should exist in at least 1 out of 100 consecutive sectors.
However, reportedly, ADR=3 should not occur in Lead-in.<br/>

#### Subchannel Q with ADR=5 in Lead-in -- Multisession Lead-In Info
When Point=B0h:<br/>
```
  8    Track number (fixed, must be 00h=Lead-in)
  8    POINT = B0h (multi-session disc)
  24   MM:SS:FF = the start time for the next possible session's program area,
       a final session is indicated by FFh:FFh:FFh,
       or when the ADR=5 / Point=B0h is absent.
  8    Number of different Mode-5 pointers present.
  24   MM:SS:FF = the maximum possible start time of the outermost Lead-out
```
When Point=C0h:<br/>
```
  8    Track number (fixed, must be 00h=Lead-in)
  8    POINT = C0h (Identifies a Multisession disc, together with POINT=B0h)
  24   ATIP values from Special Information 1, ID=101
  8    Reserved (must be 00h)
  24   MM:SS:FF = Start time of the first Lead-in area of the disc
```
And, optionally, when Point=C1h:<br/>
```
  8    Track number (fixed, must be 00h=Lead-in)
  8    POINT=C1h
  8x7  Copy of information from A1 point in ATIP
```

#### Subchannel Q with ADR=5 in Lead-Out -- Multisession Lead-Out Info
```
  8    Track number (fixed, must be AAh=Lead-out)
  8    POINT = D1h (Identifies a Multisession lead-out)
  24   Usually zero (or maybe ATIP as in Lead-In with Point=C0h...?)
  8    Seems to be the session number?
  24   MM:SS:FF = Absolute address of the First data sector of the session
```
Present in 3 consequtive sectors (3x ADR=1, 3x ADR=5, 3x ADR=1, 3x ADR=5, etc).<br/>

#### Subchannel Q with ADR=5 in Lead-in -- CDR/CDRW Skip Info (Audio Only)
When Point=01h..40h:<br/>
```
  8    Track number (fixed, must be 00h=Lead-in)
  8    POINT=01h..40h (This identifies a specific playback skip interval)
  24   MM:SS:FF Skip interval stop time in 6 BCD digits
  8    Reserved (must be 00h)
  24   MM:SS:FF Skip interval start time in 6 BCD digits
```
When Point=B1h:<br/>
```
  8    Track number (fixed, must be 00h=Lead-in)
  8    POINT=B1h (Audio only: This identifies the presence of skip intervals)
  8x4  Reserved (must be 00h,00h,00h,00h)
  8    the number of skip interval pointers in POINT=01h..40h
  8    the number of skip track assignments in POINT=B2h..B4h
  8    Reserved (must be 00h)
```
When Point=B2h,B3h,B4h:<br/>
```
  8    Track number (fixed, must be 00h=Lead-in)
  8    POINT=B2h,B3h,B4h (This identifies tracks that should be skipped)
  8    1st Track number to skip upon playback (01h..99h, must be nonzero)
  8    2nd Track number to skip upon playback (01h..99h, or 00h=None)
  8    3rd Track number to skip upon playback (01h..99h, or 00h=None)
  8    Reserved (must be 00h)... unclear... OR... 4th (of 7) skip info's...?
  8    4th Track number to skip upon playback (01h..99h, or 00h=None)
  8    5th Track number to skip upon playback (01h..99h, or 00h=None)
  8    6th Track number to skip upon playback (01h..99h, or 00h=None)
```
Note: Skip intervals are seldom written by recorders and typically ignored by
readers.<br/>

#### Subchannel R..W
Subchannels R..W are usually unused, except for some extended formats:<br/>
```
  CD-TEXT in the Lead-In area (see below)
  CD-TEXT in the Data area    (rarely used)
  CD plus Graphics (CD+G)     (rarely used)
```
Most CDROM drives do not allow to read these subchannels. CD-TEXT was designed
by Sony and Philips in 1997, so it should be found only on (some) newer discs.
Most CD/DVD players don't support it (the only exception is that CD-TEXT seems
to be popular for car hifi equipment). Most record labels don't support
CD-TEXT, even Sony seems to have discontinued it on their own records after
some years (so CD-TEXT is very rare on original disks, however, CDR software
does often allow to write CD-TEXT on CDRs).<br/>

#### Subchannel R..W, when used for CD-TEXT in the Lead-In area
CD-TEXT is stored in the six Subchannels R..W. Of the 12.25 bytes (98 bits) per
subchannel, only 12 bytes are used. Together, all 6 subchannels have a capacity
of 72 bytes (6x12 bytes) per sector. These 72 bytes are divided into four
CD-TEXT fragments (of 18 bytes each). The format of these 18 bytes is:<br/>
```
  00h 1  Header Field ID1: Pack Type Indicator
  01h 1  Header Field ID2: Track Number
  02h 1  Header Field ID3: Sequence Number
  03h 1  Header Field ID4: Block Number and Character Position Indicator
  04h 12 Text/Data Field
  10h 2  CRC-16-CCITT (big-endian) (across bytes 00h..0Fh)
```
ID1 - Pack Type Indicator:<br/>
```
  80h   Titel      (TEXT)
  81h   Performer  (TEXT)
  82h   Songwriter (TEXT)
  83h   Composer   (TEXT)
  84h   Arranger   (TEXT)
  85h   Message    (TEXT)
  86h   Disc ID    (TEXT?)  (content/format/purpose unknown?)
  87h   Genre      (BINARY) (ID codes unknown?)
  88h   TOC        (BINARY) (content/format/purpose unknown?)
  89h   TOC2       (BINARY) (content/format/purpose unknown?)
  8Ah   Reserved for future
  8Bh   Reserved for future
  8Ch   Reserved for future
  8Dh   Reserved for "content provider" aka "closed information"
  8Eh   UPC/EAN and ISRC Codes (TEXT) (content/format/purpose unknown?)
  8Fh   Blocksize (BINARY) (see below)
```
ID2 - Track Number:<br/>
```
  00h       Title/Performer/etc. for the Disc
  01h..63h  Title/Performer/etc. for Track 1..99 (Non-BCD) (Bit7=Extension)
```
ID3 - Sequence Number:<br/>
```
  00h..FFh  Incrementing Number (00h=First 18-byte fragment, 01h=Second, etc.)
```
ID4 - Block Number and Character Position Indicator:<br/>
```
  Bit7      Character Set      (0=8bit, 1=16bit)
  Bit6-4    Block Number       (0..7 = Language number, as set by "Blocksize")
  Bit3-0    Character Position (0..0Eh=Position, 0Fh=Append to prev fragment)
```
Example Data (generated with CDRWIN):<br/>
```
  ID TR SQ CH <------------Text/Data------------> -CRC-  <---Text--->
  80 00 00 00 54 65 73 74 44 69 73 6B 54 69 74 6C E2 22  TestDiskTitl
  80 00 01 0C 65 00 54 65 73 74 54 72 61 63 6B 54 C9 1B  e.TestTrackT
  80 01 02 0A 69 74 6C 65 31 00 54 65 73 74 54 72 40 3A  itle1.TestTr
  80 02 03 06 61 63 6B 54 69 74 6C 65 32 00 00 00 80 E3  ackTitle2...
  81 00 04 00 54 65 73 74 44 69 73 6B 50 65 72 66 03 DF  TestDiskPerf
  81 00 05 0C 6F 72 6D 65 72 00 54 65 73 74 54 72 12 A5  ormer.TestTr
  81 01 06 06 61 63 6B 50 65 72 66 6F 72 6D 65 72 BC 5B  ackPerformer
  81 01 07 0F 31 00 54 65 73 74 54 72 61 63 6B 50 AC 41  1.TestTrackP
  81 02 08 0A 65 72 66 6F 72 6D 65 72 32 00 00 00 64 1A  erformer2...
  8F 00 09 00 01 01 02 00 04 05 00 00 00 00 00 00 6D E2  ............
  8F 01 0A 00 00 00 00 00 00 00 00 03 0B 00 00 00 CD 0C  ............
  8F 02 0B 00 00 00 00 00 09 00 00 00 00 00 00 00 FC 8C  ............
  00   ;<--- for some reason, CDRWIN stores an ending 00h byte in .CDT files
```
Each Text string is terminated by a 00h byte (or 0000h for 16bit character
set). If there's still room in the 12-byte data region, then first characters
for the next Text string (for the next track) are appended after the 00h byte
(if there's no further track, then the remaining bytes should be padded with
00h).<br/>
The "Blocksize" (ID1=8Fh) consists three packs with 24h bytes of data (first
0Ch bytes stored with ID2=00h, next 0Ch bytes with ID2=01h, and last 0Ch bytes
with ID2=02h):<br/>
```
  00h  1   Character set (00h,01h,80h,81h,82h = see below)
  01h  1   First track number (usually/always 01h)
  02h  1   Last track number (01h..63h)
  03h  1   1bit-cd-text-in-data-area-flag, 7bit-copy-protection-flags
  04h  16  Number of 18-byte packs for ID1=80h..8Fh
  14h  8   Last sequence number of block 0..7 (or 00h=none)
  1Ch  8   Language codes for block 0..7 (definitions are unknown)
```
Character Set values (for ID1=8Fh, ID2=00h, DATA[0]=charset):<br/>
```
  00h ISO 8859-1
  01h ISO 646, ASCII
  80h MS-JIS
  81h Korean character code
  82h Mandarin (standard) Chinese character code
  Other = reserved
```
"In case the same character stings is used for consecutive tracks, character
09h (or 0909h for 16bit charset) may be used to indicate the same as previous
track. It shall not used for the first track."<br/>

#### adjust\_crc\_16\_ccitt(addr\_len)  ;for CD-TEXT and Subchannel Q
```
  lsb=00h, msb=00h      ;-initial value (zero for both CD-TEXT and Sub-Q)
  for i=0 to len-1      ;-len (10h for CD-TEXT, 0Ah for Sub-Q)
    x = [addr+i] xor msb
    x = x xor (x shr 4)
    msb = lsb xor (x shr 3) xor (x shl 4)
    lsb = x xor (x shl 5)
  next i
  [addr+len+0]=msb xor FFh, [addr+len+1]=lsb xor FFh   ;inverted / big-endian
```



##   CDROM Sector Encoding
#### Audio
```
  000h 930h Audio Data (2352 bytes) (LeftLsb,LeftMsb,RightLsb,RightMsb)
```
#### Mode0 (Empty)
```
  000h 0Ch  Sync
  00Ch 4    Header (Minute,Second,Sector,Mode=00h)
  010h 920h Zerofilled
```
#### Mode1 (Original CDROM)
```
  000h 0Ch  Sync
  00Ch 4    Header (Minute,Second,Sector,Mode=01h)
  010h 800h Data (2048 bytes)
  810h 4    EDC (checksum accross [000h..80Fh])
  814h 8    Zerofilled
  81Ch 114h ECC (error correction codes)
```
#### Mode2/Form1 (CD-XA)
```
  000h 0Ch  Sync
  00Ch 4    Header (Minute,Second,Sector,Mode=02h)
  010h 4    Sub-Header (File, Channel, Submode AND DFh, Codinginfo)
  014h 4    Copy of Sub-Header
  018h 800h Data (2048 bytes)
  818h 4    EDC (checksum accross [010h..817h])
  81Ch 114h ECC (error correction codes)
```
#### Mode2/Form2 (CD-XA)
```
  000h 0Ch  Sync
  00Ch 4    Header (Minute,Second,Sector,Mode=02h)
  010h 4    Sub-Header (File, Channel, Submode OR 20h, Codinginfo)
  014h 4    Copy of Sub-Header
  018h 914h Data (2324 bytes)
  92Ch 4    EDC (checksum accross [010h..92Bh]) (or 00000000h if no EDC)
```

#### encode\_sector
```
  sector[000h]=00h,FFh,FFh,FFh,FFh,FFh,FFh,FFh,FFh,FFh,FFh,00h
  sector[00ch]=bcd(adr/75/60)      ;0..7x
  sector[00dh]=bcd(adr/75 MOD 60)  ;0..59
  sector[00eh]=bcd(adr MOD 75)     ;0..74
  sector[00fh]=mode
  if mode=00h then
    sector[010h..92Fh]=zerofilled
  if mode=01h then
    adjust_edc(sector+0, 800h+10h)
    sector[814h..817h]=00h,00h,00h,00h,00h,00h,00h,00h
    calc_p_parity(sector)
    calc_q_parity(sector)
  if mode=02h and form=1
    sector[012h]=sector[012h] AND (NOT 20h)  ;indicate not form2
    sector[014h..017h]=sector[010h..013h]    ;copy of sub-header
    adjust_edc(sector+10h,800h+8)
    push sector[00ch]           ;\temporarily clear header
    sector[00ch]=00000000h      ;/
    calc_p_parity(sector)
    calc_q_parity(sector)
    pop sector[00ch]            ;-restore header
  if mode=02h and form=2
    sector[012h]=sector[012h] OR 20h         ;indicate form2
    sector[014h..017h]=sector[010h..013h]    ;copy of sub-header
    adjust_edc(sector+10h,914h+8)            ;edc is optional for form2
```

#### calc\_parity(sector,offs,len,j0,step1,step2)
```
  src=00ch, dst=81ch+offs, srcmax=dst
  for i=0 to len-1
    base=src, x=0000h, y=0000h
    for j=j0 to 42
      x=x xor GF8_PRODUCT[j,sector[src+0]]
      y=y xor GF8_PRODUCT[j,sector[src+1]]
      src=src+step1, if (step1=2*44) and (src>=srcmax) then src=src-2*1118
    sector[dst+2*len+0]=x AND 0FFh, [dst+0]=x SHR 8
    sector[dst+2*len+1]=y AND 0FFh, [dst+1]=y SHR 8
    dst=dst+2, src=base+step2
```
calc\_p\_parity(sector) = calc\_parity(sector,0,43,19,2\*43,2)<br/>
calc\_q\_parity(sector) = calc\_parity(sector,43\*4,26,0,2\*44,2\*43)<br/>

#### adjust\_edc(addr,len)
```
  x=00000000h
  for i=0 to len-1
    x=x xor byte[addr+i], x=(x shr 8) xor edc_table[x and FFh]
  word[addr+len]=x  ;append EDC value (little endian)
```

#### init\_tables
```
  for i=0 to FFh
    x=i, for j=0 to 7, x=x shr 1, if carry then x=x xor D8018001h
    edc_table[i]=x
  GF8_LOG[00h]=00h, GF8_ILOG[FFh]=00h, x=01h
  for i=00h to FEh
    GF8_LOG[x]=i, GF8_ILOG[i]=x
    x=x SHL 1, if carry8bit then x=x xor 1dh
  for j=0 to 42
    xx=GF8_ILOG[44-j],  yy=subfunc(xx xor 1,19h)
    xx=subfunc(xx,01h), xx=subfunc(xx xor 1,18h)
    xx=GF8_LOG[xx], yy = GF8_LOG[yy]
    GF8_PRODUCT[j,0]=0000h
    for i=01h to FFh
      x=xx+GF8_LOG[i], if x>=255 then x=x-255
      y=yy+GF8_LOG[i], if y>=255 then y=y-255
      GF8_PRODUCT[j,i]=GF8_ILOG[x]+(GF8_ILOG[y] shl 8)
```

#### subfunc(a,b)
```
  if a>0 then
    a=GF8_LOG[a]-b, if a<0 then a=a+255
    a=GF8_ILOG[a]
  return(a)
```



##   CDROM XA Subheader, File, Channel, Interleave
The Sub-Header for normal data sectors is usually 00h,00h,08h,00h (some PSX
sectors have 09h instead 08h, indicating the end of "something" or so?<br/>

#### 1st Subheader byte - File Number (FN)
```
  0-7 File Number    (00h..FFh) (for Audio/Video Interleave, see below)
```

#### 2nd Subheader byte - Channel Number (CN)
```
  0-4 Channel Number (00h..1Fh) (for Audio/Video Interleave, see below)
  5-7 Should be always zero
```

#### 3rd Subheader byte - Submode (SM)
```
  0   End of Record (EOR) (all Volume Descriptors, and all sectors with EOF)
  1   Video     ;\Sector Type (usually ONE of these bits should be set)
  2   Audio     ; Note: PSX .STR files are declared as Data (not as Video)
  3   Data      ;/
  4   Trigger           (for application use)
  5   Form2             (0=Form1/800h-byte data, 1=Form2, 914h-byte data)
  6   Real Time (RT)
  7   End of File (EOF) (or end of Directory/PathTable/VolumeTerminator)
```
The EOR bit is set in all Volume Descriptor sectors, the last sector (ie. the
Volume Descriptor Terminator) additionally has the EOF bit set. Moreover, EOR
and EOF are set in the last sector of each Path Table, and last sector of each
Directory, and last sector of each File.<br/>

#### 4th Subheader byte - Codinginfo (CI)
When used for Data sectors:<br/>
```
  0-7 Reserved (00h)
```
When used for XA-ADPCM audio sectors:<br/>
```
  0-1 Mono/Stereo     (0=Mono, 1=Stereo, 2-3=Reserved)
  2-2 Sample Rate     (0=37800Hz, 1=18900Hz, 2-3=Reserved)
  4-5 Bits per Sample (0=Normal/4bit, 1=8bit, 2-3=Reserved)
  6   Emphasis        (0=Normal/Off, 1=Emphasis)
  7   Reserved        (0)
```

#### Audio/Video Interleave (Multiple Files/Channels)
The CDROM drive mechanics are working best when continously following the data
spiral on the disk, that works fine for uncompressed Audio Data at normal
speed, but compressed Audio Data the disk is spinning much too fast. To avoid
the drive to need to pause reading or to do permanent backwards seeking, CD-XA
allows to store data interleaved in separate files/channels. With common
interleave values like so:<br/>
```
  Interleave   Data Format
  1/1 (none)   44100Hz Stereo CD Audio at normal speed
  1/8          37800Hz Stereo ADPCM compressed Audio at double speed
  1/16         18900Hz Stereo ADPCM compressed Audio at double speed
  1/16         37800Hz Mono   ADPCM compressed Audio at double speed
  1/32         18900Hz Mono   ADPCM compressed Audio at double speed
  7/8          15fps 320x224 pixel MDEC compressed Videos at double speed
  Unknown if 1/16 and 1/32 interleaves are actually possible (the PSX cdrom
  controller seems to overwrite the IC303 sector buffer entries once every
  eight sectors, so ADPCM data may get destroyed on interleaves above 1/8).
  (Crash Team Racing uses 37800Hz Mono at Double speed, so 1/16 must work).
```
For example, 1/8 means that the controller processes only each 8th sector (each
having the same File Number and Channel Number), and ignores the next 7 sectors
(which must have other File Number and/or other Channel Number). There are
various ways to arrange multiple files or channels, for example,<br/>
```
  one file with eight 1/8 audio channels
  one file with one 1/8 audio channels, plus one 7/8 video channel (*)
  one file with one 1/8 audio channels, plus 7 unused channels
  eight different files with one 1/8 audio channel each
  etc.
```
(\*) If the Audio and Video data belongs together then both should use the SAME
channel.<br/>
Note: Above interleave values are assuming that PSX Game Disks are always
running at double speed (that's fastest for normal data files, and ADPCM files
are usually using the same speed; otherwise it'd be neccessary to change the
drive speed everytime when switching between Data to ADPCM modes).<br/>
Note: The file/channel numbers can be somehow selected with the Setfilter
command. No idea if the controller is automatically switching to the next
channel or so when reaching the end of the file?<br/>

#### Real Time Streaming
With the above Interleave, files can be played continously at real time - that,
unless read-errors do occur. In that case the drive controller would usually
perform time-consuming error-correction and/or read-retries. For video/audio
streaming the resulting delay would be tendencially more annoying as than
processing or skipping the incorrect data.<br/>
In such cases the drive controller is allowed to ignore read errors; that
probably on sectors that have the Real Time (RT) flag set in their subheaders.
The controller is probably doing some read-ahead buffering (so, if it has
buffered enough data, then it may still perform read retries and/or error
correction, as long as it doesn't affect real time playback).<br/>



##   CDROM XA Audio ADPCM Compression
CD-ROM XA ADPCM is used for Audio data compression. Each 16bit sample is
encoded in 4bit nibbles; so the compression rate is almost 1:4 (only almost 1:4
because there are 16 header bytes within each 128-byte portion). The data is
usually/always stored on 914h-byte sectors (without error correction).<br/>

#### Subheader
The Subheader (see previous chapter) contains important info for ADPCM: The
file/channel numbers for Interleaved data, and the codinginfo flags:
mono/stereo flag, 37800Hz/18900Hz sampling rate, 4bit/8bit format, and
emphasis.<br/>

#### ADPCM Sectors
Each sector consists of 12h 128-byte portions (=900h bytes) (the remaining 14h
bytes of the sectors 914h-byte data region are 00h filled).<br/>
The separate 128-byte portions consist of a 16-byte header,<br/>
```
  00h..03h  Copy of below 4 bytes (at 04h..07h)
  04h       Header for 1st Block/Mono, or 1st Block/Left
  05h       Header for 2nd Block/Mono, or 1st Block/Right
  06h       Header for 3rd Block/Mono, or 2nd Block/Left
  07h       Header for 4th Block/Mono, or 2nd Block/Right
  08h       Header for 5th Block/Mono, or 3rd Block/Left  ;\unknown/unused
  09h       Header for 6th Block/Mono, or 3rd Block/Right ; for 8bit ADPCM
  0Ah       Header for 7th Block/Mono, or 4th Block/Left  ; (maybe 0, or maybe
  0Bh       Header for 8th Block/Mono, or 4th Block/Right ;/copy of above)
  0Ch..0Fh  Copy of above 4 bytes (at 08h..0Bh)
```
followed by twentyeight data words (4x28-bytes),<br/>
```
  10h..13h  1st Data Word (packed 1st samples for 2-8 blocks)
  14h..17h  2nd Data Word (packed 2nd samples for 2-8 blocks)
  18h..1Bh  3rd Data Word (packed 3rd samples for 2-8 blocks)
  ...       Nth Data Word (packed Nth samples for 2-8 blocks)
  7Ch..7Fh  28th Data Word (packed 28th samples for 2-8 blocks)
```
and then followed by the next 128-byte portion.<br/>
The "Copy" bytes are allowing to repair faulty headers (ie. if the CDROM
controller has sensed a read-error in the header then it can eventually replace
it by the copy of the header).<br/>

#### XA-ADPCM Header Bytes
```
  0-3   Shift  (0..12) (0=Loudest) (13..15=Reserved/Same as 9)
  4-5   Filter (0..3) (only four filters, unlike SPU-ADPCM which has five)
  6-7   Unused (should be 0)
```
Note: The 4bit (or 8bit) samples are expanded to 16bit by left-shifting them by
12 (or 8), that 16bit value is then right-shifted by the selected 'shift'
amount. For 8bit ADPCM shift should be 0..8 (values 9..12 will cut-off the
LSB(s) of the 8bit value, this works, but isn't useful). For both 4bit and 8bit
ADPCM, reserved shift values 13..15 will act same as shift=9).<br/>

#### XA-ADPCM Data Words (32bit, little endian)
```
  0-3   Nibble for 1st Block/Mono, or 1st Block/Left  (-8h..+7h)
  4-7   Nibble for 2nd Block/Mono, or 1st Block/Right (-8h..+7h)
  8-11  Nibble for 3rd Block/Mono, or 2nd Block/Left  (-8h..+7h)
  12-15 Nibble for 4th Block/Mono, or 2nd Block/Right (-8h..+7h)
  16-19 Nibble for 5th Block/Mono, or 3rd Block/Left  (-8h..+7h)
  20-23 Nibble for 6th Block/Mono, or 3rd Block/Right (-8h..+7h)
  24-27 Nibble for 7th Block/Mono, or 4th Block/Left  (-8h..+7h)
  28-31 Nibble for 8th Block/Mono, or 4th Block/Right (-8h..+7h)
```
or, for 8bit ADPCM format:<br/>
```
  0-7   Byte for 1st Block/Mono, or 1st Block/Left    (-80h..+7Fh)
  8-15  Byte for 2nd Block/Mono, or 1st Block/Right   (-80h..+7Fh)
  16-23 Byte for 3rd Block/Mono, or 2nd Block/Left    (-80h..+7Fh)
  24-31 Byte for 4th Block/Mono, or 2nd Block/Right   (-80h..+7Fh)
```

#### decode\_sector(src)
```
  src=src+12+4+8   ;skip sync,header,subheader
  for i=0 to 11h
   for blk=0 to 3
    IF stereo ;left-samples (LO-nibbles), plus right-samples (HI-nibbles)
      decode_28_nibbles(src,blk,0,dst_left,old_left,older_left)
      decode_28_nibbles(src,blk,1,dst_right,old_right,older_right)
    ELSE      ;first 28 samples (LO-nibbles), plus next 28 samples (HI-nibbles)
      decode_28_nibbles(src,blk,0,dst_mono,old_mono,older_mono)
      decode_28_nibbles(src,blk,1,dst_mono,old_mono,older_mono)
    ENDIF
   next blk
   src=src+128
  next i
  src=src+14h+4    ;skip padding,edc
```

#### decode\_28\_nibbles(src,blk,nibble,dst,old,older)
```
  shift  = 12 - (src[4+blk*2+nibble] AND 0Fh)
  filter =      (src[4+blk*2+nibble] AND 30h) SHR 4
  f0 = pos_xa_adpcm_table[filter]
  f1 = neg_xa_adpcm_table[filter]
  for j=0 to 27
    t = signed4bit((src[16+blk+j*4] SHR (nibble*4)) AND 0Fh)
    s = (t SHL shift) + ((old*f0 + older*f1+32)/64);
    s = MinMax(s,-8000h,+7FFFh)
    halfword[dst]=s, dst=dst+2, older=old, old=s
  next j
```

#### Pos/neg Tables
```
  pos_xa_adpcm_table[0..4] = (0, +60, +115, +98, +122)
  neg_xa_adpcm_table[0..4] = (0,   0,  -52, -55,  -60)
```
Note: XA-ADPCM supports only four filters (0..3), unlike SPU-ADPCM which
supports five filters (0..4).<br/>

#### Old/Older Values
The incoming old/older values are usually that from the previous part, or
garbage (in case of decoding errors in the previous part), or whatever (in case
there was no previous part) (ie. maybe zero on power-up?) (and maybe there's
also a way to reset the values to zero at the begin of a new file, or \*maybe\*
it's silently done automatically when issuing seek commands?).<br/>

#### 25-point Zigzag Interpolation
The CDROM decoder is applying some weird 25-point zigzag interpolation when
resampling the 37800Hz XA-ADPCM output to 44100Hz. This part is different from
SPU-ADPCM (which uses 4-point gaussian pitch interpolations). For example,
XA-ADPCM interpolation applied to a square wave looks like this:<br/>
```
                                                 .            .
           .--------------.                      | |        | |
           |              |                     .'.'.'----'.'.'.
           |              |                     | |          | |
           |              |                     |              |
           | Decompressed |                     |    Final     |
           |   XA-ADPCM   |                     |   XA-ADPCM   |
           |   Waveform   |                     |    Output    |
           |              |                   | |              | |
           |              |             ---.'.'.'              '.'.'.---
   --------'              '--------          | |                | |
                                               '                '
```
The zigzagging does produce some (inaudible) 22050Hz noise, and does produce
some low-pass (?) filtering ("sinc filter"). The effect can be reproduced
somewhat like so:<br/>
```
<B>  Output37800Hz(sample):</B>
    ringbuf[p AND 1Fh]=sample, p=p+1, sixstep=sixstep-1
    if sixstep=0
      sixstep=6
      Ouput44100Hz(ZigZagInterpolate(p,Table1))
      Ouput44100Hz(ZigZagInterpolate(p,Table2))
      Ouput44100Hz(ZigZagInterpolate(p,Table3))
      Ouput44100Hz(ZigZagInterpolate(p,Table4))
      Ouput44100Hz(ZigZagInterpolate(p,Table5))
      Ouput44100Hz(ZigZagInterpolate(p,Table6))
      Ouput44100Hz(ZigZagInterpolate(p,Table7))
    endif
<B>  ZigZagInterpolate(p,TableX):</B>
    sum=0
    for i=1 to 29, sum=sum+(ringbuf[(p-i) AND 1Fh]*TableX[i])/8000h, next i
    return MinMax(sum,-8000h,+7FFFh)
<B>  Table1, Table2, Table3, Table4, Table5, Table6, Table7  ;Index</B>
    0     , 0     , 0     , 0     , -0001h, +0002h, -0005h  ;1
    0     , 0     , 0     , -0001h, +0003h, -0008h, +0011h  ;2
    0     , 0     , -0001h, +0003h, -0008h, +0010h, -0023h  ;3
    0     , -0002h, +0003h, -0008h, +0011h, -0023h, +0046h  ;4
    0     , 0     , -0002h, +0006h, -0010h, +002Bh, -0017h  ;5
    -0002h, +0003h, -0005h, +0005h, +000Ah, +001Ah, -0044h  ;6
    +000Ah, -0013h, +001Fh, -001Bh, +006Bh, -00EBh, +015Bh  ;7
    -0022h, +003Ch, -004Ah, +00A6h, -016Dh, +027Bh, -0347h  ;8
    +0041h, -004Bh, +00B3h, -01A8h, +0350h, -0548h, +080Eh  ;9
    -0054h, +00A2h, -0192h, +0372h, -0623h, +0AFAh, -1249h  ;10
    +0034h, -00E3h, +02B1h, -05BFh, +0BCDh, -16FAh, +3C07h  ;11
    +0009h, +0132h, -039Eh, +09B8h, -1780h, +53E0h, +53E0h  ;12
    -010Ah, -0043h, +04F8h, -11B4h, +6794h, +3C07h, -16FAh  ;13
    +0400h, -0267h, -05A6h, +74BBh, +234Ch, -1249h, +0AFAh  ;14
    -0A78h, +0C9Dh, +7939h, +0C9Dh, -0A78h, +080Eh, -0548h  ;15
    +234Ch, +74BBh, -05A6h, -0267h, +0400h, -0347h, +027Bh  ;16
    +6794h, -11B4h, +04F8h, -0043h, -010Ah, +015Bh, -00EBh  ;17
    -1780h, +09B8h, -039Eh, +0132h, +0009h, -0044h, +001Ah  ;18
    +0BCDh, -05BFh, +02B1h, -00E3h, +0034h, -0017h, +002Bh  ;19
    -0623h, +0372h, -0192h, +00A2h, -0054h, +0046h, -0023h  ;20
    +0350h, -01A8h, +00B3h, -004Bh, +0041h, -0023h, +0010h  ;21
    -016Dh, +00A6h, -004Ah, +003Ch, -0022h, +0011h, -0008h  ;22
    +006Bh, -001Bh, +001Fh, -0013h, +000Ah, -0005h, +0002h  ;23
    +000Ah, +0005h, -0005h, +0003h, -0001h, 0     , 0       ;24
    -0010h, +0006h, -0002h, 0     , 0     , 0     , 0       ;25
    +0011h, -0008h, +0003h, -0002h, +0001h, 0     , 0       ;26
    -0008h, +0003h, -0001h, 0     , 0     , 0     , 0       ;27
    +0003h, -0001h, 0     , 0     , 0     , 0     , 0       ;28
    -0001h, 0     , 0     , 0     , 0     , 0     , 0       ;29
```
The above formula/table gives nearly correct results, but with small rounding
errors in some cases - possibly due to actual rounding issues, or due to
factors with bigger fractional portions, or due to a completely different
formula...<br/>
Probably, the hardware does actually do the above stuff in two steps: first,
applying a zig-zag filter (with only around 21-points) to the 37800Hz output,
and then doing 44100Hz interpolation (2-point linear or 4-point gaussian or
whatever) in a second step.<br/>
That two-step theory would also match well for 18900Hz resampling (which has
lower-pitch zigzag, and gets spread accross about fifty 44100Hz samples).<br/>

#### XA-ADPCM Emphasis
With XA-Emphasis enabled in Sub-header, output will appear as so:<br/>
```
           .------------.                           ....-----.
           |            |                        .''         |
           |    Raw     |                       .'    XA     |
           |   ADPCM    |                       |  Emphasis  '.
           |  Waveform  |                       |   Output    '..
   --------'            '----------     --------'                ''''---
```
The exact XA-Emphasis formula is unknown (maybe it's just same as for CD-DA's
SUBQ emphasis). Additionally, zig-zag interpolation is applied (somewhere
before or after applying the emphasis stuff).<br/>
Note: The Emphasis feature isn't used by any known PSX games.<br/>

#### Uninitialized Six-step Counter
The hardware does contain some six-step counter (for interpolating 37800Hz to
44100Hz, ie. to insert one extra sample after each six samples). The 900h-byte
sectors contain a multiple of six samples, so the counter will be always same
before & after playing a sector. However, the initial counter value on
power-up is uninitialized random (and the counter will fallback to that initial
random setting after each 900h-byte sector).<br/>

#### RIFF Headers (on PCs)
When reading files that consist of 914h-byte sectors on a PC, the PC seems to
automatically insert a 2Ch-byte RIFF fileheader. Like so, for ADPCM audio
files:<br/>
```
  00h 4   "RIFF"
  04h 4   Total Filesize (minus 8)
  08h 8   "CDXAfmt "
  10h 4   Size of below stuff (10h)
  14h 14  Stuff (looks like the "LEN_SU" region from XA-Directory Record)
  22h 2   Zero  (probably just dummy padding for 32bit alignment)
  24h 4   "data"
  28h 4   Size of following data (usually N*930h)
```
That RIFF stuff isn't stored on the CDROM (at least not in the file area)
(however, some of that info, like the "=UXA" stuff, is stored in the directory
area of the CDROM).<br/>
After the RIFF header, the normal sector data is appended, that, with the full
930h bytes per sector (ie. the 914h data bytes preceeded by sync bytes, header,
subheader, and followed by the EDC value).<br/>
The Channel Interleave doesn't seem to be resolved, ie. the Channels are kept
arranged as how they are stored on the CDROM. However, File Interleave
\<should\> be resolved, ie. other Files that "overlap" the file shouldn't
be included in the file.<br/>



##   CDROM ISO Volume Descriptors
#### System Area (prior to Volume Descriptors)
The first 16 sectors on the first track are the system area, for a Playstation
disk, it contains the following:<br/>
```
  Sector 0..3   - Zerofilled (Mode2/Form1, 4x800h bytes, plus ECC/EDC)
  Sector 4      - Licence String
  Sector 5..11  - Playstation Logo (3278h bytes) (remaining bytes FFh-filled)
  Sector 12..15 - Zerofilled (Mode2/Form2, 4x914h bytes, plus EDC)
```
Of which, the Licence String in sector 4 is,<br/>
```
  000h 32    Line 1      ("          Licensed  by          ")
  020h 32+6  Line 2 (EU) ("Sony Computer Entertainment Euro"," pe   ") ;\either
  020h 32+1  Line 2 (JP) ("Sony Computer Entertainment Inc.",0Ah)      ; one of
  020h 32+6  Line 2 (US) ("Sony Computer Entertainment Amer","  ica ") ;/these
  041h 1983  Empty (JP)    (filled by repeating pattern 62x30h,1x0Ah, 1x30h)
  046h 1978  Empty (EU/US) (filled by 00h-bytes)
```
The Playstation Logo in sectors 5..11 contains data like so,<br/>
```
  0000h ..   41h,00h,00h,00h,00h,00h,00h,00h,01h,00h,00h,00h,1Ch,23h,00h,00h
  0010h ..   51h,01h,00h,00h,A4h,2Dh,00h,00h,99h,00h,00h,00h,1Ch,00h,00h,00h
  0020h ..   ...
  3278h 588h FF-filled (remaining bytes on sector 11)
```
the Logo contains a header, polygons, vertices and normals for the "PS" logo
(which is displayed when booting from CDROM). Some BIOS versions are comparing
these 3278h bytes against an identical copy in ROM, and refuse to boot if the
data isn't 1:1 the same:<br/>
- US/ASIA BIOS always accepts changed logos.<br/>
- PAL BIOS accepts changed logos up to v3.0E (and refuses in v4.0E and up).<br/>
- JP BIOS never accepts changed logos (and/or changed license strings?).<br/>
Note: PAL BIOS with "region-patch-modchip" does behave same as US/ASIA BIOS.<br/>

#### Volume Descriptors (Sector 16 and up)
Playstation disks usually have only two Volume Descriptors,<br/>
```
  Sector 16    - Primary Volume Descriptor
  Sector 17    - Volume Descriptor Set Terminator
```

#### Primary Volume Descriptor (sector 16 on PSX disks)
```
  000h 1    Volume Descriptor Type        (01h=Primary Volume Descriptor)
  001h 5    Standard Identifier           ("CD001")
  006h 1    Volume Descriptor Version     (01h=Standard)
  007h 1    Reserved                      (00h)
  008h 32   System Identifier             (a-characters) ("PLAYSTATION")
  028h 32   Volume Identifier             (d-characters) (max 8 chars for PSX?)
  048h 8    Reserved                      (00h)
  050h 8    Volume Space Size             (2x32bit, number of logical blocks)
  058h 32   Reserved                      (00h)
  078h 4    Volume Set Size               (2x16bit) (usually 0001h)
  07Ch 4    Volume Sequence Number        (2x16bit) (usually 0001h)
  080h 4    Logical Block Size in Bytes   (2x16bit) (usually 0800h) (1 sector)
  084h 8    Path Table Size in Bytes      (2x32bit) (max 800h for PSX)
  08Ch 4    Path Table 1 Block Number     (32bit little-endian)
  090h 4    Path Table 2 Block Number     (32bit little-endian) (or 0=None)
  094h 4    Path Table 3 Block Number     (32bit big-endian)
  098h 4    Path Table 4 Block Number     (32bit big-endian) (or 0=None)
  09Ch 34   Root Directory Record         (see next chapter)
  0BEh 128  Volume Set Identifier         (d-characters) (usually empty)
  13Eh 128  Publisher Identifier          (a-characters) (company name)
  1BEh 128  Data Preparer Identifier      (a-characters) (empty or other)
  23Eh 128  Application Identifier        (a-characters) ("PLAYSTATION")
  2BEh 37   Copyright Filename            ("FILENAME.EXT;VER") (empty or text)
  2E3h 37   Abstract Filename             ("FILENAME.EXT;VER") (empty)
  308h 37   Bibliographic Filename        ("FILENAME.EXT;VER") (empty)
  32Dh 17   Volume Creation Timestamp     ("YYYYMMDDHHMMSSFF",timezone)
  33Eh 17   Volume Modification Timestamp ("0000000000000000",00h)
  34Fh 17   Volume Expiration Timestamp   ("0000000000000000",00h)
  360h 17   Volume Effective Timestamp    ("0000000000000000",00h)
  371h 1    File Structure Version        (01h=Standard)
  372h 1    Reserved for future           (00h-filled)
  373h 141  Application Use Area          (00h-filled for PSX and VCD)
  400h 8    CD-XA Identifying Signature   ("CD-XA001" for PSX and VCD)
  408h 2    CD-XA Flags (unknown purpose) (00h-filled for PSX and VCD)
  40Ah 8    CD-XA Startup Directory       (00h-filled for PSX and VCD)
  412h 8    CD-XA Reserved                (00h-filled for PSX and VCD)
  41Ah 345  Application Use Area          (00h-filled for PSX and VCD)
  573h 653  Reserved for future           (00h-filled)
```

#### Volume Descriptor Set Terminator (sector 17 on PSX disks)
```
  000h 1    Volume Descriptor Type    (FFh=Terminator)
  001h 5    Standard Identifier       ("CD001")
  006h 1    Terminator Version        (01h=Standard)
  007h 2041 Reserved                  (00h-filled)
```

#### Boot Record (none such on PSX disks)
```
  000h 1    Volume Descriptor Type    (00h=Boot Record)
  001h 5    Standard Identifier       ("CD001")
  006h 1    Boot Record Version       (01h=Standard)
  007h 32   Boot System Identifier    (a-characters)
  027h 32   Boot Identifier           (a-characters)
  047h 1977 Boot System Use           (not specified content)
```

#### Supplementary Volume Descriptor (none such on PSX disks)
```
  000h 1    Volume Descriptor Type (02h=Supplementary Volume Descriptor)
  001h ..   Same as for Primary Volume Descriptor (see there)
  007h 1    Volume Flags           (8bit)
  008h ..   Same as for Primary Volume Descriptor (see there)
  058h 32   Escape Sequences       (32 bytes)
  078h ..   Same as for Primary Volume Descriptor (see there)
```

#### Volume Partition Descriptor (none such on PSX disks)
```
  000h 1    Volume Descriptor Type      (03h=Volume Partition Descriptor)
  001h 5    Standard Identifier         ("CD001")
  006h 1    Volume Partition Version    (01h=Standard)
  007h 1    Reserved                    (00h)
  008h 32   System Identifier           (a-characters) (32 bytes)
  028h 32   Volume Partition Identifier (d-characters) (32 bytes)
  048h 8    Volume Partition Location   (2x32bit) Logical Block Number
  050h 8    Volume Partition Size       (2x32bit) Number of Logical Blocks
  058h 1960 System Use                  (not specified content)
```

#### Reserved Volume Descriptors (none such on PSX disks)
```
  000h 1    Volume Descriptor Type    (04h..FEh=Reserved, don't use)
  001h 2047 Reserved                  (don't use)
```



##   CDROM ISO File and Directory Descriptors
The location of the Root Directory is described by a 34-byte Directory Record
being located in Primary Volume Descriptor entries 09Ch..0BDh. The data therein
is: Block Number (usually 22 on PSX disks), LEN\_FI=01h, Name=00h, and,
LEN\_SU=00h (due to the 34-byte limit).<br/>

#### Format of a Directory Record
```
  00h 1      Length of Directory Record (LEN_DR) (33+LEN_FI+pad+LEN_SU)
  01h 1      Extended Attribute Record Length (usually 00h)
  02h 8      Data Logical Block Number (2x32bit)
  0Ah 8      Data Size in Bytes        (2x32bit)
  12h 7      Recording Timestamp       (yy-1900,mm,dd,hh,mm,ss,timezone)
  19h 1      File Flags 8 bits         (usually 00h=File, or 02h=Directory)
  1Ah 1      File Unit Size            (usually 00h)
  1Bh 1      Interleave Gap Size       (usually 00h)
  1Ch 4      Volume Sequence Number    (2x16bit, usually 0001h)
  20h 1      Length of Name            (LEN_FI)
  21h LEN_FI File/Directory Name ("FILENAME.EXT;1" or "DIR_NAME" or 00h or 01h)
  xxh 0..1   Padding Field (00h) (only if LEN_FI is even)
  xxh LEN_SU System Use (LEN_SU bytes) (see below for CD-XA disks)
```
LEN\_SU can be calculated as "LEN\_DR-(33+LEN\_FI+Padding)". For CD-XA disks (as
used in the PSX), LEN\_SU is 14 bytes:<br/>
```
  00h 2      Owner ID Group  (whatever, usually 0000h, big endian)
  02h 2      Owner ID User   (whatever, usually 0000h, big endian)
  04h 2      File Attributes (big endian):
               0   Owner Read    (usually 1)
               1   Reserved      (0)
               2   Owner Execute (usually 1)
               3   Reserved      (0)
               4   Group Read    (usually 1)
               5   Reserved      (0)
               6   Group Execute (usually 1)
               7   Reserved      (0)
               8   World Read    (usually 1)
               9   Reserved      (0)
               10  World Execute (usually 1)
               11  IS_MODE2        (0=MODE1 or CD-DA, 1=MODE2)
               12  IS_MODE2_FORM2  (0=FORM1, 1=FORM2)
               13  IS_INTERLEAVED  (0=No, 1=Yes...?) (by file and/or channel?)
               14  IS_CDDA         (0=Data or ADPCM, 1=CD-DA Audio Track)
               15  IS_DIRECTORY    (0=File or CD-DA, 1=Directory Record)
             Commonly used Attributes are:
               0D55h=Normal Binary File (with 800h-byte sectors)
               2555h=Unknown            (wipeout .AV files) (MODE1 ??)
               4555h=CD-DA Audio Track  (wipeout .SWP files, alone .WAV file)
               3D55h=Streaming File     (ADPCM and/or MDEC or so)
               8D55h=Directory Record   (parent-, current-, or sub-directory)
  06h 2      Signature     ("XA")
  08h 1      File Number   (Must match Subheader's File Number)
  09h 5      Reserved      (00h-filled)
```
The names are alphabetically sorted, no matter if the names refer to files or
directories (ie. SUBDIR would be inserted between STRFILE.EXT and SYSFILE.EXT).
The first two entries (with non-ascii names 00h and 01h) are referring to
current and parent directory.<br/>

#### Path Tables
The Path Table contain a summary of the directory names (the same information
is also stored in the directory records, so programs may either use path tables
or directory records; the path tables are allowing to read the whole directory
tree quickly at once, without neeeding to seek from directory to directory).<br/>
Path Table 1 is in Little-Endian format, Path Table 3 contains the same data in
Big-Endian format. Path Table 2 and 4 are optional copies of Table 1 and 3. The
size and location of the tables is stored in Volume Descriptor entries
084h..09Bh. The format of the separate entries within a Path Table is,<br/>
```
  00h 1       Length of Directory Name (LEN_DI) (01h..08h for PSX)
  01h 1       Extended Attribute Record Length  (usually 00h)
  02h 4       Directory Logical Block Number
  06h 2       Parent Directory Number           (0001h and up)
  08h LEN_DI  Directory Name (d-characters, d1-characters) (or 00h for Root)
  xxh 0..1    Padding Field (00h) (only if LEN_FI is odd)
```
The first entry (directory number 0001h) is the root directory, the root
doesn't have a name, nor a parent (the name field contains a 00h byte, rather
than ASCII text, LEN\_DI is 01h, and parent is 0001h, making the root it's own
parent; ignoring the fact that incest is forbidden in many countries).<br/>
The next entries (directory number 0002h and up) (if any) are sub-directories
within the root (sorted in alphabetical order, and all having parent=0001h).
The next entries are sub-directories (if any) of the first sub-directory (also
sorted in alphabetical order, and all having parent=0002h). And so on.<br/>
PSX disks usually contain all four tables (usually on sectors 18,19,20,21).<br/>

#### Format of an Extended Attribute Record (none such on PSX disks)
If present, an Extended Attribute Record shall be recorded over at least one
Logical Block. It shall have the following contents.<br/>
```
  00h 4       Owner Identification (numerical value)  ;\used only if
  04h 4       Group Identification (numerical value)  ; File Flags Bit4=1
  08h 2       Permission Flags (16bit, little-endian) ;/
  0Ah 17      File Creation Timestamp      ("YYYYMMDDHHMMSSFF",timezone)
  1Bh 17      File Modification Timestamp  ("0000000000000000",00h)
  2Ch 17      File Expiration Timestamp    ("0000000000000000",00h)
  3Dh 17      File Effective Timestamp     ("0000000000000000",00h)
  4Eh 1       Record Format                (numerical value)
  4Fh 1       Record Attributes            (numerical value)
  50h 4       Record Length                (numerical value)
  54h 32      System Identifier            (a-characters, a1-characters)
  74h 64      System Use                   (not specified content)
  B4h 1       Extended Attribute Record Version (numerical value)
  B5h 1       Length of Escape Sequences   (LEN_ESC)
  B6h 64      Reserved for future standardization (00h-filled)
  F6h 4       Length of Application Use    (LEN_AU)
  FAh LEN_AU  Application Use
  xxh LEN_ESC Escape Sequences
```
Unknown WHERE that data is located... the Directory Records can specify the
Extended Attribute Length, but not the location... maybe it's meant to be
located in the first some bytes or blocks of the File or Directory...?<br/>



##   CDROM ISO Misc
#### Both Byte Order
All 16bit and 32bit numbers in the ISO region are stored twice, once in
Little-Endian order, and then in Big-Endian Order. For example,<br/>
```
  2x16bit value 1234h     ---> stored as 34h,12h,12h,34h
  2x32bit value 12345678h ---> stored as 78h,56h,34h,12h,12h,34h,56h,78h
```
Exceptions are the 16bit Permission Flags which are stored only in
Little-Endian format (although the flags are four 4bit groups, so that isn't a
real 16bit number), and, the Path Tables are stored in both formats, but
separately, ie. one table contains only Little-Endian numbers, and the other
only Big-Endian numbers.<br/>

#### d-characters (Filenames)
```
  "0..9", "A..Z", and "_"
```

#### a-characters
```
  "0..9", "A..Z", SPACE, "!"%&'()*+,-./:;<=>?_"
```
Ie. all ASCII characters from 20h..5Fh except "#$@[\]^"<br/>

SEPARATOR 1 = 2Eh (aka ".") (extension; eg. "EXT")<br/>
SEPARATOR 2 = 3Bh (aka ";") (file version; "1".."32767")<br/>

#### Fixed Length Strings/Filenames
The Volume Descriptors contain a number fixed-length string/filename fields
(unlike the Directory Records and Path Tables which have variable lengths).
These fields should be padded with SPACE characters if they are empty, or if
the string is shorter than the maximum length.<br/>
Filename fields in Volume Descriptors are referring to files in the Root
Directory. On PSX disks, the filename fields are usually empty, but some disks
are mis-using the Copyright Filename to store the Company Name (although no
such file exists on the disk).<br/>

#### Volume Descriptor Timestamps
The various timestamps occupy 17 bytes each, in form of<br/>
```
  "YYYYMMDDHHMMSSFF",timezone
  "0000000000000000",00h         ;empty timestamp
```
The first 16 bytes are ASCII Date and Time digits (Year, Month, Day, Hour,
Minute, Second, and 1/100 Seconds. The last byte is Offset from Greenwich Mean
Time in number of 15-minute steps from -48 (West) to +52 (East); or actually:
to +56 when recursing Kiribati's new timezone.<br/>
Note: PSX games manufactured in year 2000 were accidently marked to be created
in year 0000.<br/>

#### Recording Timestamps
Occupy only 7 bytes, in non-ascii format<br/>
```
  year-1900,month,day,hour,minute,second,timezone
  00h,00h,00h,00h,00h,00h,00h    ;empty timestamp
```
The year ranges from 1900+0 to 1900+255.<br/>

#### File Flags
If this Directory Record identifies a directory then bit 2,3,7 shall be set to
ZERO.<br/>
If no Extended Attribute Record is associated with the File Section identified
by this Directory Record then bit positions 3 and 4 shall be set to ZERO.<br/>
```
  0  Existence       (0=Normal, 1=Hidden)
  1  Directory       (0=File, 1=Directory)
  2  Associated File (0=Not an Associated File, 1=Associated File)
  3  Record
        If set to ZERO, shall mean that the structure of the information in
        the file is not specified by the Record Format field of any associated
        Extended Attribute Record (see 9.5.8).
        If set to ONE, shall mean that the structure of the information in
        the file has a record format specified by a number other than zero in
        the Record Format Field of the Extended Attribute Record (see 9.5.8).
  4  Restrictions    (0=None, 1=Restricted via Permission Flags)
  5  Reserved        (0)
  6  Reserved        (0)
  7  Multi-Extent    (0=Final Directory Record for the file, 1=Not final)
```

#### Permission Flags (in Extended Attribute Records)
```
  0-3   Permissions for upper-class owners
  4-7   Permissions for normal owners
  8-11  Permissions for upper-class users
  12-15 Permissions for normal users
```
This is a bit bizarre, an upper-class owner is "an owner who is a member of a
group of the System class of user". An upper-class user is "any user who is a
member of the group specified by the Group Identification field". The separate
4bit permission codes are:<br/>
```
  Bit0  Permission to read the file    (0=Yes, 1=No)
  Bit1  Must be set (1)
  Bit2  Permission to execute the file (0=Yes, 1=No)
  Bit3  Must be set (1)
```



##   CDROM File Formats
#### FILENAME.EXT
The BIOS seems to support only (max) 8-letter filenames with 3-letter
extension, typically all uppercase, eg. "FILENAME.EXT". Eventually, once when
the executable has started, some programs might install drivers for long
filenames(?)<br/>

#### SYSTEM.CNF
Contains boot info in ASCII/TXT format, similar to the CONFIG.SYS or
AUTOEXEC.BAT files for MSDOS. A typical SYSTEM.CNF would look like so:<br/>
```
  BOOT = cdrom:\abcd_123.45;1 arg ;boot exe (drive:\path\name.ext;version)
  TCB = 4                         ;HEX (=4 decimal)   ;max number of threads
  EVENT = 10                      ;HEX (=16 decimal)  ;max number of events
  STACK = 801FFF00                ;HEX (=memtop-256)
```
The first line specifies the executable to load, from the "cdrom:" drive, "\"
root directory, filename "abcd\_123.45" (case-insensitive, the real name in the
disk directory would be uppercase, ie. "ABCD\_123.45"), and, finally ";1" is the
file's version number (a rather strange ISO-filesystem specific feature) (the
version number should be usually/always 1). Additionally, "arg" may contain an
optional 128-byte command line argument string, which is copied to address
00000180h, where it may be interpreted by the executable (most or all games
don't use that feature).<br/>
Each line in the file should be terminated by 0Dh,0Ah characters... not sure if
it's also working with only 0Dh, or only 0Ah...?<br/>

A note on the "ABCD\_123.45" file:<br/>
This is a normal executable (exactly as for the .EXE files, described below),
however, the filename/extension is taken from the game code (the "ABCD-12345"
text that is printed on the CD cover), but, with the minus replaced by an
underscore, and due to the 8-letter filename limit, the last two characters are
stored in the extension region.<br/>
That "XXXX\_NNN.NN" naming convention seems to apply for all official licensed
PSX games, not sure if it's possible to specify something like "FILENAME.EXE"
as boot-file.<br/>

#### XXXX\_NNN.NN (Boot-Executable) (filename specified in SYSTEM.CNF)
#### FILENAME.EXE (General-Purpose Executable)
PSX executables are having an 800h-byte header, followed by the code/data.<br/>
```
  000h-007h ASCII ID "PS-X EXE"
  008h-00Fh Zerofilled
  010h      Initial PC                   (usually 80010000h, or higher)
  014h      Initial GP/R28               (usually 0)
  018h      Destination Address in RAM   (usually 80010000h, or higher)
  01Ch      Filesize (must be N*800h)    (excluding 800h-byte header)
  020h      Unknown/Unused               (usually 0)
  024h      Unknown/Unused               (usually 0)
  028h      Memfill Start Address        (usually 0) (when below Size=None)
  02Ch      Memfill Size in bytes        (usually 0) (0=None)
  030h      Initial SP/R29 & FP/R30 Base (usually 801FFFF0h) (or 0=None)
  034h      Initial SP/R29 & FP/R30 Offs (usually 0, added to above Base)
  038h-04Bh Reserved for A(43h) Function (should be zerofilled in exefile)
  04Ch-xxxh ASCII marker
             "Sony Computer Entertainment Inc. for Japan area"
             "Sony Computer Entertainment Inc. for Europe area"
             "Sony Computer Entertainment Inc. for North America area"
             (or often zerofilled in some homebrew files)
             (the BIOS doesn't verify this string, and boots fine without it)
  xxxh-7FFh Zerofilled
  800h...   Code/Data                  (loaded to entry[018h] and up)
```
The code/data is simply loaded to the specified destination address, ie. unlike
as in MSDOS .EXE files, there is no relocation info in the header.<br/>
Note: In bootfiles, SP is usually 801FFFF0h (ie. not 801FFF00h as in
system.cnf). When SP is 0, the unmodified caller's stack is used. In most cases
(except when manually calling DoExecute), the stack values in the exeheader
seem to be ignored though (eg. replaced by the SYSTEM.CNF value).<br/>
The memfill region is zerofilled by a "relative" fast word-by-word fill (so
address and size must be multiples of 4) (despite of the word-by-word filling,
still it's SLOW because the memfill executes in uncached slow ROM).<br/>
The reserved region at [038h-04Bh] is internally used by the BIOS to memorize
the caller's RA,SP,R30,R28,R16 registers (for some bizarre reason, this
information is saved in the exe header, rather than on the caller's stack).<br/>
Additionally to the initial PC,R28,SP,R30 values that are contained in the
header, two parameter values are passed to the executable (in R4 and R5
registers) (however, usually that values are simply R4=1 and R5=0).<br/>
Like normal functions, the executable can return control to the caller by
jumping to the incoming RA address (provided that it hasn't destroyed the stack
or other important memory locations, and that it has pushed/popped all
registers) (returning works only for non-boot executables; if the boot
executable returns to the BIOS, then the BIOS will simply lockup itself by
calling the "SystemErrorBootOrDiskFailure" function.<br/>

The PSX uses the standard CDROM ISO9660 filesystem without any encryption (ie.
you can put an original PSX CDROM into a DOS/Windows computer, and view the
content of the files in text or hex editors without problems).<br/>

#### PSX.EXE
Aside from SYSTEM.CNF, the Kernel seems to be also checking for a file named
PSX.EXE, purpose is unknown, maybe this is the default executable name when
SYSTEM.CNF is not found?<br/>



##   CDROM Protection - SCEx Strings
#### SCEx String
The heart of the PSX copy-protection is the four-letter "SCEx" string, encoded
in the wobble signal of original PSX disks, which cannot reproduced by normal
CD writers. The last letter varies depending on the region, "SCEI" for Japan,
"SCEA" for America (and all other NTSC countries except Japan), "SCEE" for
Europe (and all other PAL countries like Australia). If the string is missing
(or if it doesn't match up for the local region) then the PSX refuses to boot.
The verification is done by the Firmware inside of the CDROM Controller (not by
the PSX BIOS, so there's no way to bypass it by patching the BIOS ROM chip).<br/>

#### Wobble Groove and Absolute Time in Pregroove (ATIP) on CD-R's
A "blank" CDR contains a pre-formatted spiral on it. The number of windings in
the spiral varies depending on the number of minutes that can be recorded on
the disk. The spiral isn't made of a straight line (------), but rather a
wobbled line (/\/\/\), which is used to adjust the rotation speed during
recording; at normal drive speed, wobble should produce a 22050Hz sine wave.<br/>
Additionally, the CDR wobble is modulated to provide ATIP information, ATIP is
used for locating and positioning during recording, and contains information
about the approximate laser power necessary for recording, the last possible
time location that lead out can start, and the disc application code.<br/>
Wobble is commonly used only on (recordable) CDRs, ie. usually NOT on
(readonly) CDROMs and Audio Disks. The copyprotected PSX CDROMs are having a
short CDR-style wobble period in the first some seconds, which seems to contain
the "SCEx" string instead of ATIP information.<br/>

#### Other Protections
Aside from the SCEx string, PSX disks are required to contain region and
licence strings (in the ISO System Area, and in the .EXE file headers), and the
"PS" logo (in the System Area, too). This data can be reproduced with normal CD
writers, although it may be illegal to distribute unlicensed disks with licence
strings.<br/>



##   CDROM Protection - Bypassing it
#### Modchips
A modchip is a small microcontroller which injects the "SCEx" signal to the
mainboard, so the PSX can be booted even from CDRs which don't contain the
"SCEx" string. Some modchips are additionally patching region checks contained
in the BIOS ROM.<br/>
Note: Although regular PSX disks are black, the hardware doesn't verify the
color of the disks, and works also with normal silver disks.<br/>

#### Disk-Swap-Trick
Once when the PSX has recognized a disk with the "SCEx" signal, it'll be
satisfied until a new disk is inserted, which is sensed by the SHELL\_OPEN
switch. When having that switch blocked, it is possible to insert a CDR without
the PSX noticing that the disk was changed.<br/>
Additionally, the trick requires some boot software that stops the drive motor
(so the new disk can be inserted, despite of the PSX thinking that the drive
door is still closed), and that does then start the boot executable on the new
disk.<br/>
The boot software can be stored on a special boot-disk (that do have the "SCEx"
string on it). Alternately, a regular PSX game disk could be used, with the
boot software stored somewhere else (eg. on Expansion ROM, or BIOS ROM
replacement, or Memory Card).<br/>

#### Booting via BIOS ROM or Expansion ROM
The PSX can be quite easily booted via Expansion ROM, or BIOS ROM replacements,
allowing to execute code that is stored in the ROM, or that is received via
whatever serial or parallel cable connection from a PC.<br/>
However, even with a BIOS replacement, the protection in the CDROM controller
is still active, so the ROM can't read "clean" data from the CDROM Drive
(unless the Disk-Swap trick is used).<br/>
Whereas, no "clean" data doens't mean no data at all. The CDROM controller does
still seem to output "raw" data (without removing the sector header, and
without handling error correction, and with only limited accuracy on the sector
position). So, eventually, a customized BIOS could convert the "raw" data to
"clean" data.<br/>

#### Secret Unlock Commands
There is an "official" backdoor that allows to disable the SCEx protection by
software via secret commands (for example, sending those commands can be done
via BIOS patches, nocash BIOS clone, or Expansion ROMs).<br/>
[CDROM - Secret Unlock Commands](cdromdrive.md#cdrom---secret-unlock-commands)<br/>

#### Booting via Memory Card
Some games that load data from memory cards may get confused if the save data
isn't formatted as how they expect it - with some fine tuning you can get them
to "crash" in a manner that they do accidently execute bootcode stored on the
memory card.<br/>
Requires a tools to write to the memory card (eg. parallel port cable), and the
memory card data customized for a specific game, and an original CDROM with
that specific game. Once when the memory card code is booted, the Disk-Swap
trick can be used.<br/>



##   CDROM Protection - Modchips
#### Modchip Source Code
The Old Crow mod chip source code works like so:<br/>
```
  entrypoint:                   ;at power_up
    gate=input/highz
    data=input/highz
    wait 50 ms
    data=output/low
    wait 850 ms
    gate=output/low
    wait 314 ms
  loop:
    wait 72 ms                  ;pause (eighteen "1=low" bits)
    sendbyte("S")               ;1st letter
    sendbyte("C")               ;2nd letter
    sendbyte("E")               ;3rd letter
    sendbyte(...)               ;4th letter (A, E, or I, depending on region)
    goto loop
  sendbyte(char):
    sendbit(0)                  ;one start bit (0=highz)
    for i=0 to 7
      sendbit(char AND 1)       ;output data (LSB first)
      char=char/2
    next i
    sendbit(1)                  ;1st stop bit (1=low)
    sendbit(1)                  ;2nd stop bit (1=low)
    return
  sendbit(bit):
    if bit=1 then data=output/low elseif bit=0 then data=input/highz
    wait 4 ms           ;4ms per bit = 250 bits per second
    return
```

#### Connection for the data/gate/sync signals:
For older PSX boards (data/gate):<br/>
```
  Board        data             gate
  PU-xx        unknown?         unknown?        ;older PSX boards
```
For newer PSX and PSone boards (data/sync):<br/>
```
  Board        data             sync
  PU-23, PM-41 CXD2938Q.Pin42   CXD2938Q.Pin5   ;newer PSX and older PSone
  PM-41(2)     CXD2941R.Pin36   CXD2941R.Pin76  ;newer PSone boards
```
On the mainboard should be a big SMD capacitor (connected to the "data" pin),
and a big testpoint (connected to the "sync" pin); it's easier to connect the
signals to that locations than to the tiny CXD-chip pins.<br/>
gate and data must be tristate outputs, or open-collector outputs (or normal
high/low outputs passed through a diode).<br/>

#### Note on "data" pin (all boards)
Transfers the "SCEx" data. Note that the signal produced by the modchip is
looking entirly different than the signal produced by original disks, the real
signal would be modulated 22050Hz wobble, while the modchip is simply dragging
the signal permanently LOW throughout "1" bits, and leaves it floating for "0"
bits. Anyways the "faked" signal seems to be accurate enough to work.<br/>

#### Note on "gate" pin (older PSX boards only)
The "gate" pin needs to be LOW only for use with original licensed disks
(reportedly otherwise the SCEx string on that disks would conflict with the
SCEx string from the modchip).<br/>
At the mainboard side, the "gate" signal is an input, and "data" is an inverted
output of the gate signal (so dragging gate to low, would cause data to go
high).<br/>

#### Note on "sync" pin (newer PSX and PSone boards only)
The "sync" pin is a testpoint on the mainboard, which does (at single speed)
output a frequency of circa 44.1kHz/6 (of which some clock pulses seem to be
longer or shorter, probably to indicate adjustments to the rotation speed).<br/>
Some modchips are connected directly to "sync" (so they are apparently
synchronizing the data output with that signal; which is not implemented in the
above source code).<br/>
Anyways, other modchips are using a more simplified connection: The modchip
itself connects only to the "data" pin, and "sync" is required to be wired to
IC723.Pin17.<br/>

#### Note on Multi-Region chips
Modchips that are designed to work in different regions are sending a different
string (SCEA, SCEE, SCEI) in each loop cycle. Due to the slow 250bps transfer
rate, it may take a while until the PSX has received the correct string, so
this multi-region technique may cause a noticeable boot-delay.<br/>

#### Stealth (hidden modchip)
The Stealth connection is required for some newer games with anti-modchip
protection, ie. games that refuse to run if they detect a modchip. The
detection relies on the fact that the SCEx signal is normally received only
when booting the disk, whilst older modchips were sending that signal
permanently. Stealth modchips are sending the signal only on power-up (and when
inserting a new disk, which can be sensed via SHELL\_OPEN signal).<br/>
Modchip detection reportedly works like so (not too sure if all commands are
required, some seem to be rather offtopic):<br/>
```
  1.  Com 19h,20h   ;Retrieve CDROM Controller timestamp
  2.  Com 01h       ;CdlNop: Get CD status
  3.  Com 07h       ;CdlMotorOn: Make CD-ROM drive ready (blah?)
  4.  Com 02h,1,1,1 ;CdlSetloc(01:01:01) (sector that does NOT have SCEx data)
  5.  Com 0Eh,1     ;CdlSetmode: Turn on CD-DA read mode
  6.  Short Delay
  7.  Com 16h       ;CdlSeekP: Seek to Setloc's parameters (4426)
  8.  Com 0Bh       ;CdlMute: Turn off sound so CdlPlay is inaudible
  9.  Com 03h       ;CdlPlay: Start playing CD-DA.
  10. Com 19h,04h   ;ResetSCExInfo (reset GetSCExInfo response to 0,0)
  11. Long Delay    ;wait until the modchip (if any) has output SCEx data
  12. Com 19h,05h   ;GetSCExInfo (returns total,success counters)
  13. Com 09h       ;CdlPause: Stop command 19h.
```
If GetSCExInfo returns nonzero values, then the console is equipped with a
modchip, and if so, anti-modchip games would refuse to work (no matter if the
disk is an illegal copy, or not).<br/>

#### NTSC-Boot BIOS Patch
Typically connects to two or three BIOS address/data lines, apparently watching
that signals, and dragging a data line LOW at certain time, to skip software
based region checks (eg. allowing to play NTSC games on PAL consoles).<br/>
Aside from the modchip connection, that additionally requires to adjust the
video signal (in 60Hz NTSC mode, the PSX defaults to generate a NTSC video
signal) (whilst most PAL screens can handle 60Hz refresh, they can't handle
NTSC colors) (on PSone boards, this can be fixed simply by grounding the /PAL
pin; IC502.Pin13) (on older PSX boards it seems to be required to install an
external color clock generator).<br/>

#### MODCHIP Connection Example
Connection for 8pin "12C508" mod chip from fatcat.co.nz for a PAL PSone with
PM-41 board (ie. with 208pin SPU CXD2938Q, and 52pin IC304 "C 3060,
SC430943PB"):<br/>
```
  1 3.5V        (supply)
  2 IC304.Pin44 (unknown?) (XLAT)
  3 BIOS.Pin15  (D2)
  4 BIOS.Pin31  (A18)
  5 SPU.Pin5    ("sync")
  6 SPU.Pin42   ("data")
  7 IC304.Pin19 (SHELL_OPEN)
  8 GND         (supply)
```
The chip can be used in a Basic connection (with only pin1,5,6,8 connected), or
Stealth and NTSC-Boot connection (additionally pin2,3,4,7 connected). Some
other modchips (such without internal oscillator) are additionally connected to
a 4MHz or 4.3MHz signal on the mainboard. Some early modchips also connected to
a bunch of additional pins that were reportedly for power-on timings (whilst
newer chips use hardcoded power-on delays).<br/>

#### Nocash BIOS "Modchip" Feature
The nocash PSX bios outputs the "data" signal on the A20 address line, so
(aside from the BIOS chip) one only needs to install a 1N4148 diode and two
wires to unlock the CDROM:<br/>
```
  SPU.Pin42 "data" -------|>|------ CPU.Pin149 (A20)
  SPU.Pin5  "sync" ---------------- IC723.Pin17
```
With the "sync" connection, the SCEx signal from the disk is disabled (ie. even
original licensed disks are no longer recognized, unless SCEx is output via A20
by software). For more variants, see:<br/>
[CDROM Protection - Chipless Modchips](cdromdrive.md#cdrom-protection---chipless-modchips)<br/>



##   CDROM Protection - Chipless Modchips
The nocash kernel clone outputs a SCEX signal via A20 and A21 address lines,
(so one won't need a separate modchip/microprocessor):<br/>
```
  A20 = the normal SCEX signal (inverted ASCII, eg. "A" = BEh)   ;all boards
  A21 = uninverted SCEX signal (uninverted ASCII, eg. "A" = 41h) ;PU-7..PU-20
  A21 = always 1 during SCEX output                              ;PU-22 and up
```
When using the clone bios as internal ROM replacement, A20 can be used with
simple wires/diodes. Doing that with external expansion ROMs would cause the
console to stop working when unplugging the ROM, hence needing a slightly more
complex circuit with transistors/logic chips.<br/>

#### External Expansion ROM version, for older boards (PU-7 through PU-20):
```
              .--------.-.                 .--------.-.
  GATE--------|C  NPN  |  .    DATA--------|C  NPN  |  .
  A20--[10K]--|B  BC   |  |    A21--[10K]--|B  BC   |  |
  GND---------|E  547  |  '    GND---------|E  547  |  '
              '--------'-'                 '--------'-'
```

#### External Expansion ROM version, for newer boards (PU-22):
```
         .-------------------.
  A21----|OE1,OE2            |
  A20----|IN1   74HC126  OUT1|--- DATA
  WFCK---|IN2            OUT2|--- SYNC
         '-------------------'
```

#### Internal Kernel ROM version, for older boards (PU-7 through PU-20):
```
  GATE---------GND
  DATA---------A20
```

#### Internal Kernel ROM version, for newer boards (PU-22 through PM-41(2)):
```
  SYNC--------WFCK
  DATA---|>|---A20
```

#### What pin is where...
```
  GATE is IC703.Pin2  (?) (8pin chip with marking "082B")   ;PU-7? .. PU-16
  GATE is IC706.Pin7/10   (16pin "118" (uPC5023GR-118)      ;PU-18 .. PU-20
  SYNC is IC723.Pin17(TEO)(20pin "SONY CXA2575N")           ;PU-22 .. PM-41(2)
  DATA is IC???.Pin7 (CG) (8pin chip with marking "2903")   ;PU-7? .. PU-16
  DATA is IC706.Pin1 (CG) (16pin "118" (uPC5023GR-118)      ;PU-18 .. PU-20
  DATA is HC05.Pin17 (CG) (52pin "SONY SC4309xxPB")         ;PU-7 .. EARLY-PU-8
  DATA is HC05.Pin32 (CG) (80pin "SONY E35D, 4246xx 185")   ;LATE-PU-8 .. PU-20
  DATA is SPU.Pin42 (CEI) (208pin "SONY CXD2938Q")          ;PU-22 .. PM-41
  DATA is SPU.Pin36?(CEI) (176pin "SONY CXD2941R")          ;PM-41(2)
  WFCK is SPU.Pin5 (WFCK) (208pin "SONY CXD2938Q")          ;PU-22 .. PM-41
  WFCK is SPU.Pin84(WFCK) (176pin "SONY CXD2941R")          ;PM-41(2)
  A20  is CPU.Pin149(A20) (208-pin CPU CXD8530 or CXD8606)  ;PU-7 .. PM-41(2)
  A20  is EXP.Pin28 (A20) (68-pin Expansion Port)           ;PU-7 .. PU-22
  A21  is CPU.Pin150(A21) (208-pin CPU CXD8530 or CXD8606)  ;PU-7 .. PM-41(2)
  A21  is EXP.Pin62 (A21) (68-pin Expansion Port)           ;PU-7 .. PU-22
```
GATE on PU-18 is usually IC706.Pin7 (but IC706.Pin10 reportedly works, too).<br/>
GATE on PU-20 is usually IC706.Pin10 (but IC706.Pin7 might work, too).<br/>



##   CDROM Protection - LibCrypt
LibCrypt is an additional copy-protection, used by about 100 PSX games. The
protection uses a 16bit decryption key, which is stored as bad position data in
Subchannel Q. The 16bit key is then used for a simple XOR-decryption on certain
800h-byte sectors.<br/>

#### Protected sectors generation schemas
There are some variants on how the Subchannel Q data is modified:<br/>
```
  1. 2 bits from both MSFs are modified,
     CRC-16 is recalculated and XORed with 0x0080.
     Games: MediEvil (E).
  2. 2 bits from both MSFs are modified,
     original CRC-16 is XORed with 0x8001.
     Games: CTR: Crash Team Racing (E) (No EDC), CTR: Crash Team Racing (E)
     (EDC), Dino Crisis (E), Eagle One: Harrier Attack (E) et al.
  3. Either 2 bits or none from both MSFs are modified,
     CRC-16 is recalculated and XORed with 0x0080.
     Games: Ape Escape (S) et al.
```
Anyways, the relevant part is that the modified sectors have wrong CRCs (which
means that the PSX cdrom controller will ignore them, and the GetlocP command
will keep returning position data from the previous sector).<br/>

#### LibCrypt sectors
The modified sectors could be theoretically located anywhere on the disc,
however, all known protected games are having them located on the same sectors:<br/>
```
  No.    <------- Minute=03/Normal ------->  <------- Minute=09/Backup ------->
  Bit15  14105 (03:08:05)  14110 (03:08:10)  42045 (09:20:45)  42050 (09:20:50)
  Bit14  14231 (03:09:56)  14236 (03:09:61)  42166 (09:22:16)  42171 (09:22:21)
  Bit13  14485 (03:13:10)  14490 (03:13:15)  42432 (09:25:57)  42437 (09:25:62)
  Bit12  14579 (03:14:29)  14584 (03:14:34)  42580 (09:27:55)  42585 (09:27:60)
  Bit11  14649 (03:15:24)  14654 (03:15:29)  42671 (09:28:71)  42676 (09:29:01)
  Bit10  14899 (03:18:49)  14904 (03:18:54)  42813 (09:30:63)  42818 (09:30:68)
  Bit9   15056 (03:20:56)  15061 (03:20:61)  43012 (09:33:37)  43017 (09:33:42)
  Bit8   15130 (03:21:55)  15135 (03:21:60)  43177 (09:35:52)  43182 (09:35:57)
  Bit7   15242 (03:23:17)  15247 (03:23:22)  43289 (09:37:14)  43294 (09:37:19)
  Bit6   15312 (03:24:12)  15317 (03:24:17)  43354 (09:38:04)  43359 (09:38:09)
  Bit5   15378 (03:25:03)  15383 (03:25:08)  43408 (09:38:58)  43413 (09:38:63)
  Bit4   15628 (03:28:28)  15633 (03:28:33)  43634 (09:41:59)  43639 (09:41:64)
  Bit3   15919 (03:32:19)  15924 (03:32:24)  43963 (09:46:13)  43968 (09:46:18)
  Bit2   16031 (03:33:56)  16036 (03:33:61)  44054 (09:47:29)  44059 (09:47:34)
  Bit1   16101 (03:34:51)  16106 (03:34:56)  44159 (09:48:59)  44164 (09:48:64)
  Bit0   16167 (03:35:42)  16172 (03:35:47)  44312 (09:50:62)  44317 (09:50:67)
```
Each bit is stored twice on Minute=03 (five sectors apart). For some reason,
there is also a "backup copy" on Minute=09 (however, the libcrypt software
doesn't actually support using that backup stuff, and, some discs don't have
the backup at all (namely, discs with less than 10 minutes on track 1?)).<br/>
A modified sector means a "1" bit, an unmodified means a "0" bit. The 16bit
keys of the existing games are always having eight "0" bits, and eight "1" bits
(meaning that there are 16 modified sectors on Minute=03, and, if present,
another 16 ones one Minute=09).<br/>

#### Example (Legacy of Kain)
Legacy of Kain (PAL) is reading the LibCrypt data during the title screen, and
does then display GOT KEY!!! on TTY terminal (this, no matter if the correct
16bit key was received).<br/>
The actual protection jumps in a bit later (shortly after learning to glide,
the game will hang when the first enemies appear if the key isn't okay).
Thereafter, the 16bit key is kept used once and when to decrypt 800h-byte
sector data via simple XORing.<br/>
The 16bit key (and some other related counters/variables) aren't stored in RAM,
but rather in COP0 debug registers (which are mis-used as general-purpose
storage in this case), for example, the 16bit key is stored in LSBs of the
"cop0r3" register.<br/>



##   CDROM Disk Images CCD/IMG/SUB (CloneCD)
#### File.IMG - 2352 (930h) bytes per sector
Contains the sector data, recorded at 930h bytes per sector. Unknown if other
sizes are also used/supported (like 800h bytes/sector, or even images with
mixed sizes of 800h and 930h for different tracks).<br/>

#### File.SUB - 96 (60h) bytes per sector (subchannel P..W with 96 bits each)
Contains subchannel data, recorded at 60h bytes per sector.<br/>
```
  00h..0Bh 12 Subchannel P (Pause-bits, usually all set, or all cleared)
  0Ch..17h 12 Subchannel Q (ADR/Control, custom info, CRC-16-CCITT)
  18h..5Fh .. Subchannel R..W (usually zero) (can be used for CD-TEXT)
```
Optionally, the .SUB file can be omitted (it's needed only for discs with
non-standard subchannel data, such like copy-protected games).<br/>

#### File.CCD - Lead-in info in text format
Contains Lead-in info in ASCII text format. Lines should be terminated by
0Dh,0Ah. The overall CCD filestructure is:<br/>
```
  [CloneCD]     ;File ID and version
  [Disc]        ;Overall Disc info
  [CDText]      ;CD-TEXT (included only if present)
  [Session N]   ;Session(s) (numbered 1 and up)
  [Entry N]     ;Lead-in entries (numbered 0..."TocEntries-1")
  [TRACK N]     ;Track info (numbered 1 and up)
```
Read on below for details on the separate sections.<br/>

#### [CloneCD]
```
  Version=3             ;-version (usually 3) (rarely 2)
```

#### [Disc]
```
  TocEntries=4          ;-number of [Entry N] fields (lead-in info blocks)
  Sessions=1            ;-number of sessions (usually 1)
  DataTracksScrambled=0 ;-unknown purpose (usually 0)
  CDTextLength=0        ;-total size of 18-byte CD-TEXT chunks (usually 0)
  CATALOG=NNNNNNNNNNNNN ;-13-digit EAN-13 barcode (included only if present)
```

#### [CDText]
```
  Entries=N       ;number of following entries (CDTextLength/18) (not /16)
  Entry 0=80 00 NN NN NN NN NN NN NN NN NN NN NN NN NN NN   ;entry 0
  Entry 1=80 NN NN NN NN NN NN NN NN NN NN NN NN NN NN NN   ;entry 1
  ...
  Entry XX=8f NN NN NN NN NN NN NN NN NN NN NN NN NN NN NN  ;entry N-1
  Note: Each entry contains 16 bytes (ie. "18-byte CD-TEXT" with CRC excluded)
  "NN NN NN.." consists of 2-digit lowercase HEX numbers (without leading "0x")
```

#### [Session 1]
```
  PreGapMode=2          ;-unknown purpose (usually 1 or 2)
  PreGapSubC=1          ;-unknown purpose (usually 0 or 1)
```

#### [Entry 0]
[Entry 0..2] are usually containing Point A0h..A2h info. [Entry 3..N] are
usually TOC info for Track 1 and up.<br/>
```
  Session=1             ;-session number that this entry belongs to (usually 1)
  Point=0xa0            ;-point (0..63h=Track, non-BCD!) (A0h..XXh=specials) Q2
  ADR=0x01              ;-lower 4bit of ADR/Control (usually 1)           Q0.lo
  Control=0x04          ;-upper 4bit of ADR/Control (eg. 0=audio, 4=data) Q0.hi
  TrackNo=0             ;-usually/always 0 (as [Entry N]'s are in Lead-in)   Q1
  AMin=0                ;\current MSF address                                Q3
  ASec=0                ; (dummy zero values) (actual content                Q4
  AFrame=0              ; would be current lead-in position)                 Q5
  ALBA=-150             ;/ALBA=((AMin*60+ASec)*75+AFrame)-PreGapSize
  Zero=0                ;-probably reserved byte from Q channel              Q6
  PMin=1                ;\referenced MSF address (non-BCD!), for certain     Q7
  PSec=32               ; Point's, PMin may contain a Track number, and PSec Q8
  PFrame=0              ; the disc type value (that without non-BCD-glitch)  Q9
  PLBA=6750             ;/PLBA=((PMin*60+PSec)*75+PFrame)-PreGapSize
```

#### [TRACK 1]             ;-track number (non-BCD) (1..99)
```
  MODE=2                ;-mode (0=Audio, 1=Mode1, 2=Mode2)
  ISRC=XXXXXNNNNNNN     ;-12-letter/digit ISRC code (included only if present)
  INDEX 0=N             ;-1st sector with index 0, missing EVEN if any?
  INDEX 1=N             ;-1st sector with index 1, usually same as track's PLBA
  INDEX 2=N             ;-1st sector with index 2, if any
  etc.
```

#### Missing Sectors & Sector Size
The .CCD file doesn't define the "PreGapSize" (the number of missing sectors at
begin of first track). It seems to be simply constant " PreGapSize=150". Unless
one is supposed to calculate it as
"PreGapSize=((PMin\*60+PSec)\*75+PFrame)-PLBA".<br/>
The SectorSize seems to be also constant, "SectorSize=930h".<br/>

#### Non-BCD Caution
All Min/Sec/Frame/Track/Index values are expressed in non-BCD, ie. they must be
converted to BCD to get the correct values (as how they are stored on real
CDs). Exceptions are cases where those bytes have other meanings: For example,
"PSec=32" does normally mean BcdSecond=32h, but for Point A0h it would mean
DiscType=20h=CD-ROM-XA).<br/>
The Point value is also special, it is expressed in hex (0xNN), but nonetheless
it is non-BCD, ie. Point 1..99 are specified as 0x01..0x63, whilst, Point
A0h..FFh are specified as such (ie. as 0xA0..0xFF).<br/>

#### Versions
Version=1 doesn't seem to exist (or it is very rare). Version=2 is quite rare,
and it seems to lack the [TRACK N] entries (meaning that there is no MODE and
INDEX information, except that the INDEX 1 location can be assumed to be same
as PLBA). Version=3 is most common, this version includes [TRACK N] entries,
but often only with INDEX=1 (and up, if more indices), but without INDEX 0 (on
Track 1 it's probably missing due to pregap, on further Tracks it's missing
without reason) (so, only ways to reproduce INDEX=0 would be to guess it being
located 2 seconds before INDEX=1, or, to use the information from the separate
.SUB file, if that file is present; note: presence of index 0 is absolutely
required for some games like PSX Tomb Raider 2).<br/>

#### Entry & Points & Sessions
The [Entry N] fields are usually containing Point A0h,A1h,A2h, followed by
Point 1..N (for N tracks). For multiple sessions: The session is terminated by
Point B0h,C0h. The next session does then contain Point A0h,A1h,A2h, and Point
N+1..X (for further tracks). The INDEX values in the [TRACK N] entries are
originated at the begin of the corresponding session, whilst PLBA values in
[Entry N] entries are always originated at the begin of the disk.<br/>



##   CDROM Disk Images CDI (DiscJuggler)
#### Overall Format
```
  Sector Data (sector 00:00:00 and up)          ;-body
  Number of Sessions (1 byte)     <--- located at "Filesize-Footersize"
  Session Block for 1st session (15 bytes)      ;\
  nnn-byte info for 1st track                   ; 1st session
  nnn-byte info for 2nd track (if any)          ;
  etc.                                          ;/
  Session Block for 2nd session (15 bytes)      ;\
  nnn-byte info for 1st track                   ; 2nd session (if any)
  nnn-byte info for 2nd track (if any)          ;
  etc.                                          ;/
  etc.                                          ;-further sessions (if any)
  Session Block for no-more-sessions (15 bytes) ;-end marker
  nnn-byte Disc Info Block                      ;-general disc info
  Entrypoint (4 bytes)            <--- located at "Filesize-4"
```

#### Sector Data
Contains Sector Data for sector 00:00:00 and up (ie. all sectors are stored in
the file, there are no missing "pregap" sectors).<br/>
Sector Size can be 800h..990h bytes/sector (sector size may vary per track).<br/>

#### Number of Sessions (1 byte)
```
  00h   1   Number of Sessions (usually 1)
```

#### Session Block (15-bytes)
```
  00h   1   Unknown (00h)
  01h   1   Number of Tracks in session (01h..63h) (or 00h=No More Sessions)
  02h   7   Unknown (00h-filled)
  09h   1   Unknown (01h)
  0Ah   3   Unknown (00h-filled)
  0Dh   2   Unknown (FFh,FFh)
```

#### Track/Disc Header (30h+F bytes) (used in Track Blocks and Disc Info Block)
```
  00h   12  Unknown (FFh,FFh,00h,00h,01h,00h,00h,00h,FFh,FFh,FFh,FFh)
  0Ch   3   Unknown (DAh,0Ah,D5h or 64h,05h,2Ah) (random/id/chksum?)
  0Fh   1   Total Number of Tracks on Disc (00h..63h) (non-BCD)
  10h   1   Length of below Path/Filename (F)
  11h   (F) Full Path/Filename (eg. "C:\folder\file.cdi")
  11h+F 11  Unknown (00h-filled)
  1Ch+F 1   Unknown (02h)
  1Dh+F 10  Unknown (00h-filled)
  27h+F 1   Unknown (80h)
  28h+F 4   Unknown (00057E40h) (=360000 decimal) (disc capacity 80 minutes?)
  2Ch+F 2   Unknown (00h,00h)
  2Eh+F 2   Medium Type (0098h=CD-ROM, 0038h=DVD-ROM)
```

#### Track Block (E4h+F+I+T bytes)
```
  00h     30h+F Track/Disc Header (see above)
  30h+F   02h   Number of Indices (usually 0002h) (I=Num*4)
  32h+F   (I)   32bit Lengths (per index) (eg. 00000096h,00007044h)
  32h+FI  04h   Number of CD-Text blocks (usually 0) (T=Num*18+VariableLen's)
  36h+FI  (T)   CD-Text (if any) (see "mirage_parser_cdi_parse_cdtext")
  36h+FIT 02h   Unknown (00h,00h)
  38h+FIT 01h   Track Mode (0=Audio, 1=Mode1, 2=Mode2/Mixed)
  39h+FIT 07h   Unknown (00h,00h,00h,00h,00h,00h,00h)
  40h+FIT 04h   Session Number (starting at 0) (usually 00h)
  44h+FIT 04h   Track Number   (non-BCD, starting at 0) (00h..62h)
  48h+FIT 04h   Track Start Address (eg. 00000000h)
  4Ch+FIT 04h   Track Length        (eg. 000070DAh)
  50h+FIT 0Ch   Unknown (00h-filled)
  5Ch+FIT 04h   Unknown (00000000h or 00000001h)
  60h+FIT 04h   read_mode (0..4)
                  0: Mode1,        800h, 2048
                  1: Mode2,        920h, 2336
                  2: Audio,        930h, 2352
                  3: Raw+PQ,       940h, 2352+16 non-interleaved (P=only 1bit)
                  4: Raw+PQRSTUVW, 990h, 2352+96 interleaved
  64h+FIT 4     Control (Upper 4bit of ADR/Control, eg. 00000004h=Data)
  68h+FIT 1     Unknown (00h)
  69h+FIT 4     Track Length        (eg. 000070DAh) (same as above)
  6Dh+FIT 4     Unknown (00h,00h,00h,00h)
  71h+FIT 12    ISRC Code 12-letter/digit (ASCII?) string (00h-filled if none)
  7Dh+FIT 4     ISRC Valid Flag (0=None, Other?=Yes?)
  81h+FIT 1     Unknown (00h)
  82h+FIT 8     Unknown (FFh,FFh,FFh,FFh,FFh,FFh,FFh,FFh)
  8Ah+FIT 4     Unknown (00000001h)
  8Eh+FIT 4     Unknown (00000080h)
  92h+FIT 4     Unknown (00000002h)     (guess: maybe audio num channels??)
  96h+FIT 4     Unknown (00000010h)      (guess: maybe audio bits/sample??)
  9Ah+FIT 4     Unknown (0000AC44h) (44100 decimal, ie. audio sample rate?)
  9Eh+FIT 2Ah   Unknown (00h-filled)
  C8h+FIT 4     Unknown (FFh,FFh,FFh,FFh)
  CCh+FIT 12    Unknown (00h-filled)
  D8h+FIT 1       session_type  ONLY if last track of a session (else 0)
                   (0=Audio/CD-DA, 1=Mode1/CD-ROM, 2=Mode2/CD-XA)
  D9h+FIT 5     Unknown (00h-filled)
  DEh+FIT 1     Not Last Track of Session Flag (0=Last Track, 1=Not Last)
  DFh+FIT 1     Unknown (00h)
  E0h+FIT 4        address for last track of a session? (otherwise 00,00,FF,FF)
```

#### Disc Info Block (5Fh+F+V+T bytes)
```
  00h     30h+F Track/Disc Header (see above)
  30h+F   4     Disc Size (total number of sectors)
  34h+F   1     Volume ID Length (V) ;\from Primary Volume Descriptor[28h..47h]
  35h+F   (V)   Volume ID String     ;/(ISO Data discs) (unknown for Audio)
  35h+FV  1     Unknown (00h)
  36h+FV  4     Unknown (01h,00h,00h,00h)
  3Ah+FV  4     Unknown (01h,00h,00h,00h)
  3Eh+FV  13    EAN-13 Code 13-digit (ASCII?) string (00h-filled if none)
  4Bh+FV  4     EAN-13 Valid Flag (0=None, Other?=Yes?)
  4Fh+FV  4     CD-Text Length in bytes (T=Num*1)
  53h+FV  (T)   CD-Text (for Lead-in) (probably 18-byte units?)
  53h+FVT 8     Unknown (00h-filled)
  5Bh+FVT 4     Unknown (06h,00h,00h,80h)
```

#### Entrypoint (4 bytes) (located at "Filesize-4")
```
  00h     4     Footer Size in bytes
```



##   CDROM Disk Images CUE/BIN/CDT (Cdrwin)
#### .CUE/.BIN (CDRWIN)
CDRWIN stores disk images in two separate files. The .BIN file contains the raw
disk image, starting at sector 00:02:00, with 930h bytes per sector, but
without any TOC or subchannel information. The .CUE file contains additional
information about the separate track(s) on the disk, in ASCII format, for
example:<br/>
```
 FILE "PATH\FILENAME.BIN" BINARY
   TRACK 01 MODE2/2352
     INDEX 01 00:00:00           ;real address = 00:02:00  (+2 seconds)
   TRACK 02 AUDIO
     PREGAP 00:02:00             ;two missing seconds      (NOT stored in .BIN)
     INDEX 01 08:09:29           ;real address = 08:13:29  (+2 seconds +pregap)
   TRACK 03 AUDIO
     INDEX 00 14:00:29           ;real address = 14:04:29  (+2 seconds +pregap)
     INDEX 01 14:02:29           ;real address = 14:06:29  (+2 seconds +pregap)
   TRACK 04 AUDIO
     INDEX 00 18:30:20           ;real address = 18:34:20  (+2 seconds +pregap)
     INDEX 01 18:32:20           ;real address = 18:36:20  (+2 seconds +pregap)
```
The .BIN file does not contain ALL sectors, as said above, the first 2 seconds
are not stored in the .BIN file. Moreover, there may be missing sectors
somewhere in the middle of the file (indicated as PREGAP in the .CUE file;
PREGAPs are usually found between Data and Audio Tracks).<br/>
The MM:SS:FF values in the .CUE file are logical addresses in the .BIN file,
rather than physical addresses on real CDROMs. To convert the .CUE values back
to real addresses, add 2 seconds to all MM:SS:FF addresses (to compensate the
missing first 2 seconds), and, if the .CUE contains a PREGAP, then the pregap
value must be additionally added to all following MM:SS:FF addresses.<br/>
The end address of the last track is not stored in the .CUE, instead, it can be
only calculated by converting the .BIN filesize to MM:SS:FF format and adding 2
seconds (plus any PREGAP values) to it.<br/>

#### FILE \<filename\> BINARY|MOTOTOLA..or..MOTOROLA?|AIFF|WAVE|MP3
```
  (must appear before any other commands, except CATALOG)
  (uh, may also appear before further tracks)
```

#### FLAGS DCP 4CH PRE SCMS

#### INDEX NN MM:SS:FF

#### TRACK NN datatype
```
  AUDIO          ;930h  ;bytes 000h..92Fh
  CDG            ;?     ;?
  MODE1/2048     ;800h  ;bytes 010h..80Fh
  MODE1/2352     ;930h  ;bytes 000h..92Fh
  MODE2/2336     ;920h  ;bytes 010h..92Fh
  MODE2/2352     ;930h  ;bytes 000h..92Fh
  CDI/2336       ;920h  ;?
  CDI/2352       ;930h  ;bytes 000h..92Fh
```

#### PREGAP MM:SS:FF
#### POSTGAP MM:SS:FF
Duration of silence at the begin (PREGAP) or end (POSTGAP) of a track. Even if
it isn't specified, the first track will always have a 2-second pregap.<br/>
The gaps are NOT stored in the BIN file.<br/>

#### REM comment
Allows to insert comments/remarks (which are usually ignored). Some third-party
tools are mis-using REM to define additional information.<br/>

#### CATALOG 1234567890123
#### ISRC ABCDE1234567
```
  (ISRC must be after TRACK, and before INDEX)
```

#### PERFORMER "The Band"
#### SONGWRITER "The Writer"
#### TITLE "The Title"
These entries allow to define basic CD-Text info directly in the .CUE file.<br/>
Some third-party utilites allow to define additional CD-Text info via REM
lines, eg. "REM GENRE Rock".<br/>
Alternately, more complex CD-Text data can be stored in a separate .CDT file.<br/>

#### CDTEXTFILE "C:\LONG FILENAME.CDT"
Specifies an optional file which may contain CD-TEXT. The .CDT file consists of
raw 18-byte CD-TEXT fragments (which may include any type of information,
including exotic one's like a "Message" from the producer). For whatever
reason, there's a 00h-byte appended at the end of the file. Alternately to the
.CDT file, the less exotic types of CD-TEXT can be defined by PERFORMER, TITLE,
and SONGWRITER commands in the .CUE file.<br/>

#### Missing
Unknown if newer CUE/BIN versions do also support subchannel data.<br/>



##   CDROM Disk Images MDS/MDF (Alcohol 120%)
#### File.MDF - Contains sector data (optionally with sub-channel data)
Contains the sector data, recorded at 800h..930h bytes per sector, optionally
followed by 60h bytes subchannel data (appended at the end of each sector). The
stuff seems to be start on 00:02:00 (ie. the first 150 sectors are missing; at
least it is like so when "Session Start Sector" is -150).<br/>
The subchannel data (if present) consists of 8 subchannels, stored in 96 bytes
(each byte containing one bit per subchannel).<br/>
```
  Bit7..0 = Subchannel P..W (in that order, eg. Bit6=Subchannel Q)
```
The 96 bits (per subchannel) can be translated to bytes, as so:<br/>
```
  1st..8th bit  = Bit7..Bit0 of 1st byte (in that order, ie. MSB/Bit7 first)
  9st..16th bit = Bit7..Bit0 of 2nd byte ("")
  17th..        = etc.
```

#### File.MDS - Contains disc/lead-in info (in binary format)
An MDS file's structure consists of the following stuff ...<br/>
```
  Header              (58h bytes)
  Session block(s)    (usually one 18h byte entry)
  Data blocks         (N*50h bytes)
  Index blocks        (usually N*8 bytes)
  Filename blocks(s)  (usually one 10h byte entry)
  Filename string(s)  (usually one 6 byte string)
```

#### Header (58h bytes)
```
  00h 16  File ID ("MEDIA DESCRIPTOR")
  10h 2   Unknown (01h,03h or 01h,04h or 01h,05h) (Fileformat version?)
  12h 2   Media Type (0=CD-ROM, 1=CD-R, 2=CD-RW, 10h=DVD-ROM, 12h=DCD-R)
  14h 2   Number of sessions (usually 1)
  16h 4   Unknown (02h,00h,00h,00h)
  1Ah 2   Zero (for DVD: Length of BCA data)
  1Ch 8   Zero
  24h 4   Zero (for DVD: Offset to BCA data)
  28h 18h Zero
  40h 4   Zero (for DVD: Offset to Disc Structures)   (from begin of .MDS file)
  44h 0Ch Zero
  50h 4   Offset to First Session-Block (usually 58h) (from begin of .MDS file)
  54h 4   Zero (for DVD?: Offset to DPM data blocks)  (from begin of .MDS file)
```

#### Session-Blocks (18h bytes)
```
  00h 4   Session Start Sector (starting at FFFFFF6Ah=-150 in first session)
  04h 4   Session End Sector     (XXX plus 150 ?)
  08h 2   Session number (starting at 1) (non-BCD)
  0Ah 1   Number of Data Blocks with any Point value (Total Data Blocks)
  0Bh 1   Number of Data Blocks with Point>=A0h      (Special Lead-In info)
  0Ch 2   First Track Number in Session (01h..63h, non-BCD!)
  0Eh 2   Last Track Number in Session  (01h..63h, non-BCD!)
  10h 4   Zero
  14h 4   Offset to First Data-Block (usually 70h) (from begin of .MDS file)
```

#### Data-Blocks (50h bytes)
Block 0..2 are usually containing Point A0h..A2h info. Block 3..N are usually
TOC info for Track 1 and up.<br/>
```
  00h 1   Track mode (see below for details)
  01h 1   Number of subchannels in .MDF file (0=None, 8=Sector has +60h bytes)
  02h 1   ADR/Control (but with upper/lower 4bit swapped, ie. MSBs=ADR!)    Q0
  03h 1   TrackNo (usually/always 00h; as this info is in Lead-in area)     Q1
  04h 1   Point (Track 01h..63h, non-BCD!) (or A0h and up=Lead-in info)     Q2
  05h 4   Zero (probably dummy MSF and reserved byte from Q channel)   Q3..Q6?
  09h 1   Minute (Non-BCD!) (if track >= 0xA0 -> info about track ###)      Q7
                            (if track = 0xA2 -> min. @ lead-out)
  0Ah 1   Second (Non-BCD!) (if track = 0xA2 -> sec. @ lead-out)            Q8
  0Bh 1   Frame  (Non-BCD!) (if track = 0xA2 -> frame @ lead-out)           Q9
```
For Point\>=A0h, below 44h bytes at [0Ch..4Fh] are zero-filled<br/>
```
  0Ch 4   Offset to Index-block for this track    (from begin of .MDS file)
  10h 2   Sector size (800h..930h) (or 860h..990h if with subchannels)
  12h 1   Unknown (02h) (maybe number of indices?)
  13h 11h Zero
  24h 4   Track start sector, PLBA (00000000h=00:02:00)
  28h 8   Track start offset                      (from begin of .MDF file)
  30h 4   Number of Filenames for this track (usually 1)
  34h 4   Offset to Filename Block for this track (from begin of .MDS file)
  38h 18h Zero
```
Trackmode:<br/>
```
  (upper 4bit seem to be meaningless?)
  00h=None (used for entries with Point=A0h..FF)
  A9h=AUDIO       ;sector size = 2352    930h  ;bytes 000h..92Fh
  AAh=MODE1       ;sector size = 2048    800h  ;bytes 010h..80Fh
  ABh=MODE2       ;sector size = 2336    920h  ;bytes 010h..92Fh
  ACh=MODE2_FORM1 ;sector size = 2048    800h  ;bytes 018h..817h (incomplete!)
  ADh=MODE2_FORM2 ;sector size = 2324+0? 914h  ;bytes 018h..91Bh (incomplete!)
  ADh=MODE2_FORM2 ;sector size = 2324+4? 918h  ;bytes ??..?? (contains what?)
  ECh=MODE2       ;sector size = 2448    990h  ;(930h+60h) (with subchannels)
```

#### Index Blocks (usually 8 bytes per track)
```
  00h 4  Number of sectors with Index 0 (usually 96h or zero)
  04h 4  Number of sectors with Index 1 (usually size of main-track area)
```
Index blocks are usually 8 bytes in size (two indices per track). Maybe this
block is/was intended to allow to contain more indices (although the Alcohol
120% does always store only 2 indices, even when recording a CD with more than
2 indices per track).<br/>
The MDS file does usually contain Index blocks for \<all\> Data Blocks (ie.
including unused dummy Index Blocks for Data Blocks with Point\>=A0h).<br/>

#### Filename Blocks (10h bytes)
```
  00h 4  Offset to Filename (from begin of .MDS file)
  04h 1  Filename format (0=8bit, 1=16bit characters)
  05h 11 Zero
```
Normally all tracks are sharing the same filename block (although theoretically
the tracks could use separate filename blocks; with different filenames).<br/>

#### Filename Strings (usually 6 bytes)
```
  00h 6  Filename, terminated by zero (usually "*.mdf",00h)
```
Contains the filename of the of the sector data (usually "\*.mdf", indicating to
use the same name as for the .mds file, but with .mdf extension).<br/>

#### Missing
Unknown if/how this format supports EAN-13, ISRC, CD-TEXT.<br/>
Unknown if Track/Point/Index are BCD or non-BCD.<br/>



##   CDROM Disk Images NRG (Nero)
#### .NRG (NERO)
Nero is probably the most bloated and most popular CD recording software. The
first part of the file contains the disk image, starting at sector 00:00:00,
with 800h..930h bytes per sector. Additional chunk-based information is
appended at the end of the file, usually consisting of only four chunks:
CUES,DAOI,END!,NERO (in that order).<br/>

#### Chunk Entrypoint (in last 8/12 bytes of file)
```
  4   File ID "NERO"/"NER5"
  4/8 Fileoffset of first chunk
```

#### Cue Sheet (summary of the Table of Contents, TOC)
```
  4   Chunk ID "CUES"/"CUEX"
  4   Chunk size (bytes)
```
below EIGHT bytes repeated for each track/index,<br/>
of which, first FOUR bytes are same for both CUES and CUEX,<br/>
```
  1   ADR/Control from TOC (usually LSBs=ADR=1=fixed, MSBs=Control=Variable)
  1   Track  (BCD) (00h=Lead-in, 01h..99h=Track N, AAh=Lead-out)
  1   Index  (BCD) (usually 00h=pregap, 01h=actual track)
  1   Zero
```
next FOUR bytes for CUES,<br/>
```
  1   Zero
  1   Minute (BCD) ;starting at 00:00:00 = 2 seconds before ISO vol. descr.
  1   Second (BCD)
  1   Sector (BCD)
```
or, next FOUR four bytes for CUEX,<br/>
```
  4   Logical Sector Number (HEX) ;starting at FFFFFF6Ah (=00:00:00)
```
Caution: Above may contain two position 00:00:00 entries: one nonsense entry
for Track 00 (lead-in), followed by a reasonable entry for Track 01, Index 00.<br/>

#### Disc at Once Information
```
  4   Chunk ID "DAOI"/"DAOX"
  4   Chunk size (bytes)
  4   Garbage (usually same as above Chunk size)
  13  EAN-13 Catalog Number (13-digit ASCII) (or 00h-filled if none/unknown)
  1   Zero
  1   Disk type (00h=Mode1 or Audio, 20h=XA/Mode2) (and probably 10h=CD-I?)
  1   Unknown (01h)
  1   First track (Non-BCD) (01h..63h)
  1   Last track  (Non-BCD) (01h..63h)
```
below repeated for each track,<br/>
```
  12  ISRC in ASCII (eg. "USXYZ9912345") (or 00h-filled if none/unknown)
  2   Sector size (usually 800h, 920h, or 930h) (see Mode entry for more info)
  1   Mode:
        0=Mode1/800h ;raw mode1 data (excluding sync+header+edc+errorinfo)
        3=Mode2/920h ;almost full sector (exluding first 16 bytes; sync+header)
        6=Mode2/930h ;full sector (including first 16 bytes; sync+header)
        7=Audio/930h ;full sector (plain audio data)
      Mode values from wikipedia:
        00h for data                                     Mode1/800h
        02h
        03h for Mode 2 Form 1 data   eh? FORM1???        Mode2/920h
        05h for raw data                                 Mode1?/930h
        06h for raw Mode 2/form 1 data                   Mode2/930h
        07h for audio                                    Audio/930h
        0Fh for raw data with sub-channel                Mode1?/930h+WHAT?
        10h for audio with sub-channel                   Audio/930h+WHAT?
        11h for raw Mode 2/form 1 data with sub-channel  Mode2/WHAT?+WHAT?
       Note: Some newer files do actually use different sector sizes for each
       track (eg. 920h for the data track, and 930h for any following audio
       tracks), older files were using the same sector size for all tracks
       (eg. if the disk contained 930-byte Audio tracks, then Data tracks
       were stored at the same size, rather than at 800h or 920h bytes).
  3   Unknown (always 00h,00h,01h)
  4/8 Fileoffset 1 (Start of Track's Pregap) (with Index=00h)
  4/8 Fileoffset 2 (Start of actual Track) (with Index=01h and up)
  4/8 Fileoffset 3 (End of Track+1) (aka begin of next track's pregap)
```

#### End of chain
```
  4   Chunk ID "END!"
  4   Chunk size (always zero)
```

#### Track Information (contained only in Track at Once images)
```
  4     Chunk ID "TINF"/"ETNF"/"ETN2"
  4     Chunk size (bytes)
```
below repeated for each track,<br/>
```
  4/4/8 Track fileoffset        ;\32bit in TINF/ETNF chunks,
  4/4/8 Track length (bytes)    ;/64bit in ETN2 chunks
  4     Mode (should be same as in DAO chunks, see there) (implies sector size)
  0/4/4 Start lba on disc       ;\only in ETNF/ETN2 chunks,
  0/4/4 Unknown?                ;/not in TINF chunks
```

#### Unknown 1 (contained only in Track at Once images)
```
  4   Chunk ID "RELO"
  4   Chunk size (bytes)
  4   Zero
```

#### Unknown 2 (contained only in Track at Once images)
```
  4   Chunk ID "TOCT"
  4   Chunk size (bytes)
  1   Disk type (00h=Mode1 or Audio, 20h=XA/Mode2) (and probably 10h=CD-I?)
  1   Zero (00h)
```

#### Session Info (begin of a session) (contained only in multi-session images)
```
  4   Chunk ID "SINF"
  4   Chunk size (bytes)
  4   Number of tracks in session
```

#### CD-Text (contained only in whatever images)
```
  4   Chunk ID None/"CDTX"
  4   Chunk size (bytes) (must be a multiple of 18 bytes)
```
below repeated for each fragment,<br/>
```
  18  Raw 18-byte CD-text data fragments
```

#### Media Type? (contained only in whatever images)
```
  4   Chunk ID "MTYP"
  4   Chunk size (bytes)
  4   Unknown? (00000001h for CDROM) (maybe other value for DVD)
```

#### Notes
Newer/older .NRG files may contain 32bit/64bit values (and use "OLD"/"NEW"
chunk names) (as indicated by the "/" slashes).<br/>
CAUTION: All 16bit/32bit/64bit values are in big endian byte-order.<br/>

#### Missing
Unknown if newer NRG versions do also support subchannel data.<br/>



##   CDROM Disk Image/Containers CDZ
.CDZ is a compressed disk image container format (developed by pSX Author, and
used only by the pSX emulator). The disk is split into 64kbyte blocks, which
allows fast random access (without needing to decompress all preceeding
sectors).<br/>
However, the compression ratio is surprisingly bad (despite of being
specifically designed for cdrom compression, the format doesn't remove
redundant sector headers, error correction information, and EDC checksums).<br/>

#### .CDZ File Structure
```
  FileID ("CDZ",00h for cdztool v0/v1, or "CDZ",01h for cdztool v2 and up)
  One or two Chunk(s)
```

#### .CDZ Chunk Format
Chunk Header in v0 (unreleased prototype):<br/>
```
  4    32bit Decompressed Size (of all blocks) (must be other than "ZLIB")
```
Chunk Header in v1 (first released version):<br/>
```
  4    ZLIB ID ("ZLIB")
  8    64bit Decompressed Size (of all blocks)
```
Chunk Header in v2 and up (later versions):<br/>
```
  4    Chunk ID (eg. "CUE",00h)
  8    Chunk Size in bytes (starting at "ZLIB" up to including Footer, if any)
  4    ZLIB ID ("ZLIB")
  8    64bit Decompressed Size (of all blocks)
```
Chunk Body (same in all versions):<br/>
```
  4    Number of Blocks (N)
  4    Block 1 Compressed Size (CS.1)
  4    Block 1 Decompressed Size (always 00010000h, except last block)
  CS.1 Block 1 Compressed ZLIB Data (starting with 78h,9Ch)
  ...  ...                                     ;\
  4    Block N Compressed Size (CS.N)          ; further block(s)
  4    Block N Decompressed Size               ; (if any)
  CS.N Block N Compressed ZLIB Data            ;/
```
Chunk Footer in v0 (when above header didn't have the "ZLIB" ID):<br/>
```
  4*N       Directory Entries for N blocks     ;-this ONLY for BIN chunk
```
Chunk Footer in v1 and up:<br/>
```
  BPD*(N-1) Directory Entries for N-1 blocks   ;\this ONLY for BIN chunk
  1         Bytes per Directory Entry (BPD)    ;/(not for CUE/CCD/MDS)
```
The "Compressed ZLIB Data" parts contain Deflate'd data (starting with 2-byte
ZLIB header, and ending with 4-byte ZLIB/ADLER checksum), for details see:<br/>
[Inflate - Core Functions](cdromvideocdsvcd.md#inflate---core-functions)<br/>
[Inflate - Initialization & Tree Creation](cdromvideocdsvcd.md#inflate---initialization--tree-creation)<br/>
[Inflate - Headers and Checksums](cdromvideocdsvcd.md#inflate---headers-and-checksums)<br/>

#### .CDZ Chunks / Content
The chunk(s) have following content:<br/>
```
  noname+noname       --> .CUE+.BIN (cdztool v1 and below)
  "BIN",0             --> .ISO      (cdztool v2? and up)
  "CUE",0+"BIN",0     --> .CUE+.BIN (cdztool v2 and up)
  "CCD",0+"BIN",0     --> .CCD+.IMG (cdztool v2 and up)
  "CCD",0+"BIN",01h   --> .CCD+.IMG+.SUB (930h sectors, plus 60h subchannels)
  "MDS",0+"BIN",0     --> .MDS+.MDF (cdztool v5 only)
```
Note: cdztool doesn't actually recognize files with .ISO extension (however,
one can rename them to .BIN, and then compress them as CUE-less .BIN file).<br/>

#### Cdztool.exe Versions
```
  cdztool.exe v0, unrelased prototype
  cdztool.exe v1, 22 May 2005, CRC32=620dbb08, 102400 bytes, pSX v1.0-5
  cdztool.exe v2, 02 Jul 2006, CRC32=bcb29c1e, 110592 bytes, pSX v1.6
  cdztool.exe v3, 22 Jul 2006, CRC32=4062ba82, 110592 bytes, pSX v1.7
  cdztool.exe v4, 13 Aug 2006, CRC32=7388dd3d, 118784 bytes, pSX v1.8-11
  cdztool.exe v5, 22 Jul 2007, CRC32=f25c1659, 155648 bytes, pSX v1.12-13
```
Note: v0 wasn't ever released (it's only noteworthy because later versions do
have backwards compatibility for decompressing old v0 files). v1 didn't work
with all operating systems (on Win98 it just says "Error: Couldn't create
\<output\>" no matter what one is doing, however, v1 does work on later
windows versions like WinXP or so?).<br/>



##   CDROM Disk Image/Containers ECM
ECM (Error Code Modeler by Neill Corlett) is a utility that removes
unneccessary ECC error correction and EDC error detection values from
CDROM-images. This is making the images a bit smaller, but the real size
reduction isn't gained until subsequently compressing the images via tools like
ZIP. Accordingly, these files are extremly uncomfortable to use: One most first
UNZIP them, and then UNECM them.<br/>

#### .EXT.ECM - Double extension
ECM can be applied to various CDROM-image formats (like .BIN, .CDI, .IMG, .ISO,
.MDF, .NRG), as indicated by the double-extension. Most commonly it's applied
to .BIN files (hence using extension .BIN.ECM).<br/>

#### Example / File Structure
```
  45 43 4D 00                                      ;FileID "ECM",00h
  3C                                               ;Type 0, Len=10h (aka 0Fh+1)
  00 FF FF FF FF FF FF FF FF FF FF 00 00 02 00 02  ;16 data bytes
  02                                               ;Type 2, Len=1 (aka 00h+1)
  00 00 08 00 00 00 00 00 00 00 00 ..... 00 00 00  ;804h data bytes
  3C                                               ;Type 0, Len=10h (aka 0Fh+1)
  00 FF FF FF FF FF FF FF FF FF FF 00 00 02 01 02  ;16 data bytes
  02                                               ;Type 2, Len=1 (aka 00h+1)
  00 00 08 00 00 00 00 00 00 00 00 ..... 00 00 00  ;804h data bytes
  ...
  FC FF FF FF 3F                                   ;End Code (Len=FFFFFFFFh+1)
  NN NN NN NN                                      ;EDC (on decompressed data)
```

#### Type/Length Byte(s)
Type/Length is encoded in 1..5 byte(s), with "More=1" indicating that further
length byte(s) follow:<br/>
```
  1st Byte: Bit7=More, Bit6-2=LengthBit4-0, Bit1-0=Type(0..3)
  2nd Byte: Bit7=More, Bit6-0=LengthBit5-11
  3rd Byte: Bit7=More, Bit6-0=LengthBit12-18
  4th Byte: Bit7=More, Bit6-0=LengthBit19-25
  5th Byte: Bit7-6=Reserved/Zero, Bit5-0=LengthBit26-31
```
Length=FFFFFFFFh=End Indicator<br/>
The actual decompression LEN is: "LEN=Length+1"<br/>

#### ECM Decompression
Below is repeated LEN times (with LEN being the Length value plus 1):<br/>
```
  Type 0: load 1 byte, save 1 byte
  Type 1: load 803h bytes [0Ch..0Eh,10h..80Fh], save 930h bytes [0..92Fh]
  Type 2: load 804h bytes [14h..817h], save 920h bytes [10h..92Fh]
  Type 3: load 918h bytes [14h..91Bh], save 920h bytes [10h..92Fh]
```
Type 1-3 are reconstructing the missing bytes before saving. Type 2-3 are
saving only 920h bytes, so (if the original image contained full 930h byte
sectors) the missing 10h bytes must be inserted via Type 0. Type 0 can be also
used for copying whole sectors as-is (eg. Audio sectors, or Data sectors with
invalid Sync/Header/ECC/EDC values). And, Type 0 can be used to store
non-sector data (such like the chunks at the end of .NRG or .CDI files).<br/>

#### Central Mistakes
There's a lot of wrong with the ECM format. The two central problems are that
it doesn't support data-compression (and needs external compression tools like
zip/rar), and, that it doesn't contain a sector look-up table (meaning that
random access isn't possible unless when scanning the whole file until reaching
the desired sector).<br/>

#### Worst-case Scenario
As if ECM as such wouldn't be uncomfortable enough, you may expect typical ECM
users to get more things messed up. For example:<br/>
```
  A RAR file containing a 7Z file containing a ECM file containing a BIN file.
  The BIN containing only Track 1, other tracks stored in APE files.
  And, of course, the whole mess without including the required CUE file.
```



##   CDROM Subchannel Images
#### SBI (redump.org)
SBI Files start with a 4-byte FileID:<br/>
```
  4 bytes FileID ("SBI",00h)
```
The followed by entries as so:<br/>
```
  3 bytes real absolute MM:SS:FF address where the sub q data was bad
  1 byte Format: the format can be 1, 2 or 3:
  Format 1: complete 10 bytes sub q data            (Q0..Q9)
  Format 2: 3 bytes wrong relative MM:SS:FF address (Q3..Q5)
  Format 3: 3 bytes wrong absolute MM:SS:FF address (Q7..Q9)
```
Note: The PSX libcrypt protection relies on bad checksums (Q10..Q11), which
will cause the PSX cdrom controller to ignore Q0..Q9 (and to keep returning
position data from most recent sector with intact checksum).<br/>
Ironically, the SBI format cannot store the required Q10..Q11 checksum. The
trick for using SBI files with libcrypted PSX discs is to ignore the useless
Q0..Q9 data, and to assume that all sectors in the SBI file have wrong Q10..Q11
checksums.<br/>

#### M3S (Subchannel Q Data for Minute 3) (ePSXe)
M3S files are containing Subchannel Q data for all sectors on Minute=03 (the
region where PSX libcrypt data is located) (there is no support for storing the
(unused) libcrypt backup copy on Minute=09). The .M3S filesize is 72000 bytes
(60 seconds \* 75 sectors \* 16 bytes). The 16 bytes per sector are:<br/>
```
  Q0..Q9   Subchannel Q data (normally position data)
  Q10..Q11 Subchannel Q checksum
  Q12..Q15 Dummy/garbage/padding (usually 00000000h or FFFFFFFFh)
```
Unfortunately, there are at least 3 variants of the format:<br/>
```
  1. With CRC (Q0..Q11 intact) (and Q12..Q15 randomly 00000000h or FFFFFFFFh)
  2. Without CRC (only Q0..Q9 intact, but Q10..Q15 zerofilled)
  3. Without anything (only Q0 intact, but Q1..Q15 zerofilled)
```
The third variant is definetly corrupt (and one should ignore such zerofilled
entries). The second variant is corrupt, too (but one might attempt to repair
them by guessing the missing checksum: if it contains normal position values
assume correct crc, if it contains uncommon values assume a libcrypted sector
with bad crc).<br/>
The M3S format is intended for libcrypted PSX games, but, people seem to have
also recorded (corrupted) M3S files for unprotected PSX games (in so far, more
than often, the M3S files might cause problems, instead of solving them).<br/>
Note: The odd 16-byte format with 4-byte padding does somehow resemble the "P
and Q Sub-Channel" format 'defined' in MMC-drafts; if the .M3S format was based
on the MMC stuff: then the 16th byte might contain a Subchannel P "pause" flag
in bit7.<br/>

#### CDROM Images with Subchannel Data
Most CDROM-Image formats can (optionally) contain subchannel recordings. The
downsides are: Storing all 8 subchannels for a full CDROM takes up about
20MBytes. And, some entries may contain 'wrong' data (read errors caused by
scratches cannot be automatically repaired since subchannels do not contain
error correction info).<br/>
If present, the subchannel data is usually appended at the end of each sector
in the main binary file (one exception is CloneCD, which stores it in a
separate .SUB file instead of in the .IMG file).<br/>
```
  CCD/IMG/SUB (CloneCD)  P-W  60h-bytes Non-interleaved (in separate .SUB file)
  CDI (DiscJuggler)      P-Q  10h-bytes Non-interleaved (in .CDI file)
  ""                     P-W  60h-bytes Interleaved (in .CDI file)
  CUE/BIN/CDT (Cdrwin)        N/A
  ISO (single-track)          N/A
  MDS/MDF (Alcohol 120%) P-W  60h-bytes Interleaved (in .MDF file)
  NRG (Nero)             P-W  60h-bytes Interleaved (in .NRG file)
```
Interleaved Subchannel format (eg. Alcohol .MDF files):<br/>
```
  00h-07h   80 C0 80 80 80 80 80 C0   ;P=FFh, Q=41h=ADR/Control, R..W=00h
  08h-0Fh   80 80 80 80 80 80 80 C0   ;P=FFh, Q=01h=Track,       R..W=00h
  10h-17h   80 80 80 80 80 80 80 C0   ;P=FFh, Q=01h=Index,       R..W=00h
  18h-1Fh   80 80 80 80 80 80 80 80   ;P=FFh, Q=00h=RelMinute,   R..W=00h
  20h-27h   80 80 80 80 80 80 80 80   ;P=FFh, Q=00h=RelSecond,   R..W=00h
  28h-2Fh   80 80 80 80 80 80 80 80   ;P=FFh, Q=00h=RelSector,   R..W=00h
  30h-37h   80 80 80 80 80 80 80 80   ;P=FFh, Q=00h=Reserved,    R..W=00h
  38h-3Fh   80 80 80 80 80 80 80 80   ;P=FFh, Q=00h=AbsMinute,   R..W=00h
  40h-47h   80 80 80 80 80 80 C0 80   ;P=FFh, Q=02h=AbsSecond,   R..W=00h
  48h-4Fh   80 80 80 80 80 80 80 80   ;P=FFh, Q=00h=AbsSector,   R..W=00h
  50h-57h   80 80 C0 80 C0 80 80 80   ;P=FFh, Q=28h=ChecksumMsb, R..W=00h
  58h-5Fh   80 80 C0 C0 80 80 C0 80   ;P=FFh, Q=32h=ChecksumLsb, R..W=00h
```
Non-Interleaved Subchannel format (eg. CloneCD .SUB files):<br/>
```
  00h-0Bh   FF FF FF FF FF FF FF FF FF FF FF FF  ;Subchannel P (Pause)
  0Ch-17h   41 01 01 00 00 00 00 00 02 00 28 32  ;Subchannel Q (Position)
  18h-23h   00 00 00 00 00 00 00 00 00 00 00 00  ;Subchannel R
  24h-2Fh   00 00 00 00 00 00 00 00 00 00 00 00  ;Subchannel S
  30h-3Bh   00 00 00 00 00 00 00 00 00 00 00 00  ;Subchannel T
  3Ch-47h   00 00 00 00 00 00 00 00 00 00 00 00  ;Subchannel U
  48h-53h   00 00 00 00 00 00 00 00 00 00 00 00  ;Subchannel V
  54h-5Fh   00 00 00 00 00 00 00 00 00 00 00 00  ;Subchannel W
```
Non-Interleaved P-Q 10h-byte Subchannel format:<br/>
```
  This is probably based on MMC protocol, which would be as crude as this:
  The 96 pause bits are summarized in 1 bit. Pause/Checksum are optional.
  00h-09h   41 01 01 00 00 00 00 00 02 00        ;Subchannel Q (Position)
  0Ah-0Bh   28 32    ;<-- OPTIONAL, can be zero! ;Subchannel Q (Checksum)
  0Ch-0Eh   00 00 00                             ;Unused padding (zero)
  0F        80       ;<-- OPTIONAL, can be zero! ;Subchannel P (Bit7=Pause)
```



##   CDROM Disk Images Other Formats
#### .ISO - A raw ISO9660 image (can contain a single data track only)
Contains raw sectors without any sub-channel information (and thus it's
restricted to the ISO filesystem region only, and cannot contain extras like
additional audio tracks or additional sessions). The image should start at
00:02:00 (although I wouldn't be surprised if some \<might\> start at
00:00:00 or so). Obviously, all sectors must have the same size, either 800h or
930h bytes (if the image contains only Mode1 or Mode2/Form1 sectors then 800h
bytes would usually enough; if it contains one or more Mode2/Form2 sectors then
all sectors should be 930h bytes).<br/>
Handling .ISO files does thus require to detect the image's sector size, and to
search the sector that contains the first ISO Volume Descriptor. In case of
800h byte sectors it may be additionally required to detect if it is a Mode1 or
Mode2/Form1 image; for PSX images (and any CD-XA images) it'd be Mode2.<br/>

#### .CHD
Something used by MAME/MESS. Originally intended for compressed ROM-images, but
does also support compressed CDROM-images. Fileformat and compression ratio are
unknown. Also unknown if it allows random-access.<br/>
Some info can be found in MAME source code (looking at the source code for the
CHDMAN tool might be a good starting point... although the actual file
structure might be hidden in other source files).<br/>

#### .C2D
Something. Can contain compressed or uncompressed CDROM-images. Fileformat and
compression ratio are unknown. Also unknown if it allows random-access.<br/>
Some info on (uncompressed) .C2D files can be found in libmirage source code.<br/>

#### .ISZ
This is reportedly a "zipped" .ISO file, using some unknown compression format
(unrelated to pkzip .zip file format).<br/>

#### .MDX
Reportedly a compressed MDS/MDF file, supported by Daemon Tools. Fileformat and
compression ratio are unknown. Also unknown if it allows random-access.<br/>

#### .CU2/.BIN
Custom format used by PSIO (an SD-card based CDROM-drive emulator connected to
PSX expansion port). The .CU2 file is somewhat intended to be smaller and
easier to parse than normal .CUE files, the drawback is that it's kinda
non-standard, and doesn't support INDEX and ADSR information. A sample .CUE
file looks as so:<br/>
```
  ntracks 3
  size      39:33:17
  data1     00:02:00
  track02   31:36:46
  track03   36:03:17
  ;(insert 2 blanks lines here, and insert 1 leading space in next line)
  trk end 39:37:17
```
All track numbers and MM:SS:FF values are decimal. The ASCII strings should be
as shown above, but they are simple ignored by the PSIO firmware (eg. using
"popcorn666" instead of "size" or "track02" should also work). The first track
should be marked "data1", but PSIO ignores that string, too (it does always
treat track 1 as data, and track 2-99 as audio; thus not supporting PSX games
with multiple data tracks). The "trk end" value should be equal to the "size"
value plus 4 seconds (purpose is unknown, PSIO does just ignore the "trk end"
value).<br/>
CU2 creation seems to require CDROM images in "CUE/BIN redump.org format" (with
separate BIN files for each track), the CUE is then converted to a CU3 file
(which is used only temporarily), until the whole stuff is finally converted to
a CU2 file (and with all tracks in a single BIN file). Tools like RD2PSIO (aka
redump2psio) or PSIO's own SYSCON.ZIP might help on doing some of those steps
automatically.<br/>
Alongsides, PSIO uses a "multidisc.lst" file... for games that require more
than one CDROM disc?<br/>

#### CD Image File Format (Xe - Multi System Emulator)
This is a rather crude file format, used only by the Xe Emulator. The files are
meant to be generated by a utility called CDR (CD Image Ripper), which, in
practice merely displays an "Unable to read TOC." error message.<br/>
The overall file structure is, according to "Xe User's Manual":<br/>
```
  header: 200h bytes header (see below)
  data:   990h bytes per sector (2352 Main, 96 Sub), 00:00:00->Lead Out
```
The header "definition" from the "Xe User's Manual" is as unclear as this:<br/>
```
  000h   00
  001h   00
  002h   First Track
  003h   Last Track
  004h   Track 1 (ADR << 4) | CTRL              ;\
  005h   Track 1 Start Minutes                  ; Track 1
  006h   Track 1 Start Seconds                  ;
  007h   Track 1 Start Frames                   ;/
  ...     ...                                   ;-Probably Further Tracks (?)
  n+0    Last Track Start Minutes               ;\
  n+1    Last Track Start Seconds               ; Last Track
  n+2    Last Track Start Frames                ;
  n+3    Last Track (ADR << 4) | CTRL           ;/
  n+4    Lead-Out Track Start Minutes           ;\
  n+5    Lead-Out Track Start Seconds           ; Lead-Out
  n+6    Lead-Out Track Start Frames            ;
  n+7    Lead-Out Track (ADR << 4) | CTRL       ;/
  ...    00
  1FFh   00
```
Unknown if MM:SS:FF values and/or First+Last Track numbers are BCD or non-BCD.<br/>
Unknown if Last track is separately defined even if there is only ONE track.<br/>
Unknown if Track 2 and up include ADR/Control (and if yes: where?).<br/>
Unknown if ADR/Control is really meant to be \<before\> MM:SS:FF on Track
1.<br/>
Unknown if ADR/Control is really meant to be \<after\> MM:SS:FF on
Last+Lead-Out.<br/>
Unknown if this format does have a file extension (if yes: which?).<br/>
Unknown if subchannel data is meant to be interleaved or not.<br/>
The format supports only around max 62 tracks (in case each track is 4 bytes).<br/>
There is no support for "special" features like multi-sessions, cd-text.<br/>



