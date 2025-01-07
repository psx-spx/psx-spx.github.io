#   CDROM Drive
#### Playstation CDROM I/O Ports
[CDROM Controller I/O Ports](cdromdrive.md#cdrom-controller-io-ports)<br/>

#### Playstation CDROM Commands
[CDROM Controller Command Summary](cdromdrive.md#cdrom-controller-command-summary)<br/>
[CDROM - Control Commands](cdromdrive.md#cdrom-control-commands)<br/>
[CDROM - Seek Commands](cdromdrive.md#cdrom-seek-commands)<br/>
[CDROM - Read Commands](cdromdrive.md#cdrom-read-commands)<br/>
[CDROM - Status Commands](cdromdrive.md#cdrom-status-commands)<br/>
[CDROM - CD Audio Commands](cdromdrive.md#cdrom-cd-audio-commands)<br/>
[CDROM - Test Commands](cdromdrive.md#cdrom-test-commands)<br/>
[CDROM - Secret Unlock Commands](cdromdrive.md#cdrom-secret-unlock-commands)<br/>
[CDROM - Video CD Commands](cdromdrive.md#cdrom-video-cd-commands)<br/>
[CDROM - Mainloop/Responses](cdromdrive.md#cdrom-mainloopresponses)<br/>
[CDROM - Response Timings](cdromdrive.md#cdrom-response-timings)<br/>
[CDROM - Response/Data Queueing](cdromdrive.md#cdrom-responsedata-queueing)<br/>

#### General CDROM Disk Format
[CDROM Format](cdromformat.md)<br/>
[CDROM File Formats](cdromfileformats.md)<br/>
[CDROM Video CDs (VCD)](cdromvideocdsvcd.md)<br/>

#### Playstation CDROM Coprocessor
[CDROM Internal Info on PSX CDROM Controller](cdrominternalinfoonpsxcdromcontroller.md)<br/>



##   CDROM Controller I/O Ports
The CD-ROM drive is made up of several chips. The CPU only has direct access to
the sector buffer/decoder chip's "host" interface, which provides mailboxes to
communicate with the drive's microcontroller, a data port for reading sectors
and audio configuration registers. The interface is bank switched and consists
of four banks of four 8-bit registers each.

The following registers are available when reading:

| Bank | `0x1f801800`                              | `0x1f801801`                                  | `0x1f801802`                                  | `0x1f801803`                                            |
| ---: | :---------------------------------------- | :-------------------------------------------- | :-------------------------------------------- | :------------------------------------------------------ |
| 0, 2 | [`HSTS`](#0x1f801800-read-all-banks-hsts) | [`RESULT`](#0x1f801801-read-all-banks-result) | [`RDDATA`](#0x1f801802-read-all-banks-rddata) | [`HINTMSK_R`](#0x1f801803-read-banks-0-and-2-hintmsk_r) |
| 1, 3 | [`HSTS`](#0x1f801800-read-all-banks-hsts) | [`RESULT`](#0x1f801801-read-all-banks-result) | [`RDDATA`](#0x1f801802-read-all-banks-rddata) | [`HINTSTS`](#0x1f801803-read-banks-1-and-3-hintsts)     |

The following registers are available when writing:

| Bank | `0x1f801800`                                     | `0x1f801801`                                  | `0x1f801802`                                       | `0x1f801803`                                  |
| ---: | :----------------------------------------------- | :-------------------------------------------- | :------------------------------------------------- | :-------------------------------------------- |
|    0 | [`ADDRESS`](#0x1f801800-write-all-banks-address) | [`COMMAND`](#0x1f801801-write-bank-0-command) | [`PARAMETER`](#0x1f801802-write-bank-0-parameter)  | [`HCHPCTL`](#0x1f801803-write-bank-0-hchpctl) |
|    1 | [`ADDRESS`](#0x1f801800-write-all-banks-address) | [`WRDATA`](#0x1f801801-write-bank-1-wrdata)   | [`HINTMSK_W`](#0x1f801802-write-bank-1-hintmsk_w)  | [`HCLRCTL`](#0x1f801803-write-bank-1-hclrctl) |
|    2 | [`ADDRESS`](#0x1f801800-write-all-banks-address) | [`CI`](#0x1f801801-write-bank-2-ci)           | [`ATV0`](#0x1f801802-write-bank-2-atv0)            | [`ATV1`](#0x1f801803-write-bank-2-atv1)       |
|    3 | [`ADDRESS`](#0x1f801800-write-all-banks-address) | [`ATV2`](#0x1f801801-write-bank-3-atv2)       | [`ATV3`](#0x1f801802-write-bank-3-atv3)            | [`ADPCTL`](#0x1f801803-write-bank-3-adpctl)   |

#### `0x1f801800` (read, all banks): `HSTS`
#### `0x1f801800` (write, all banks): `ADDRESS`
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

#### `0x1f801801` (write, bank 0): `COMMAND`
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

#### `0x1f801802` (write, bank 0): `PARAMETER`
```
  0-7  Parameter Byte(s) to be used for next Command
```
Before sending a command, write any parameter byte(s) to this address.<br/>

#### `0x1f801803` (write, bank 0): `HCHPCTL`
```
  0-4 0    Not used (should be zero)
  5   SMEN Want Command Start Interrupt on Next Command (0=No change, 1=Yes)
  6   BFWR ...
  7   BFRD Want Data         (0=No/Reset Data Fifo, 1=Yes/Load Data Fifo)
```

#### `0x1f801802` (read, all banks): `RDDATA`
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

#### `0x1f801801` (read, all banks): `RESULT`
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

#### `0x1f801803` (read, banks 0 and 2): `HINTMSK_R`
#### `0x1f801802` (write, bank 1): `HINTMSK_W`
```
  0-4  Interrupt Enable Bits (usually all set, ie. 1Fh=Enable All IRQs)
  5-7  Unknown/unused (write: should be zero) (read: usually all bits set)
```
XXX WRITE: bit5-7 unused should be 0 // READ: bit5-7 unused<br/>

#### `0x1f801803` (read, banks 1 and 3): `HINTSTS`
#### `0x1f801803` (write, bank 1): `HCLRCTL`
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

#### Caution - Unstable IRQ Flag polling
IRQ flag changes aren't synced with the MIPS CPU clock. If more than one bit
gets set (and the CPU is reading at the same time) then the CPU does
occassionally see only one of the newly bits:<br/>
```
  0 ----------> 3   ;99.9%  normal case INT3's
  0 ----------> 5   ;99%    normal case INT5's
  0 ---> 1 ---> 3   ;0.1%   glitch: occurs about once per thousands of INT3's
  0 ---> 4 ---> 5   ;1%     glitch: occurs about once per hundreds of INT5's
```
As workaround, do something like:<br/>
```
 @@polling_lop:
  irq_flags = [1F801803h] AND 07h       ;<-- 1st read (may be still unstable)
  if irq_flags = 00h then goto @@polling_lop
  irq_flags = [1F801803h] AND 07h       ;<-- 2nd read (should be stable now)
  handle irq_flags and acknowledge them
```
The problem applies only when manually polling the IRQ flags (an actual IRQ
handler will get triggered when the flags get nonzero, and the flags will have
stabilized once when the IRQ handler is reading them) (except, a combination of
IRQ10h followed by IRQ3 can also have unstable LSBs within the IRQ handler).<br/>
The problem occurs only on older consoles (like LATE-PU-8), not on newer
consoles (like PSone).<br/>

#### `0x1f801802` (write, bank 2): `ATV0`
#### `0x1f801803` (write, bank 2): `ATV1`
#### `0x1f801801` (write, bank 3): `ATV2`
#### `0x1f801802` (write, bank 3): `ATV3`
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

#### `0x1f801803` (write, bank 3): `ADPCTL`
```
  0    ADPMUTE Mute ADPCM                 (0=Normal, 1=Mute)
  1-4  -       Unused (should be zero)
  5    CHNGATV Apply Audio Volume changes (0=No change, 1=Apply)
  6-7  -       Unused (should be zero)
```

#### `0x1f801801` (write, bank 1): `WRDATA`
```
  0-7  Data
```
This register seems to be restricted to 8bit bus, unknown if/how the PSX DMA
controller can write to it (it might support only 16bit data for CDROM).<br/>

#### `0x1f801801` (write, bank 2): `CI`
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

```
Pause -> Wait for INT3 IRQ -> clear IRQ (write 0x1f to 1f801803h.0) -> SetMode/Pause/Stop/SetMode/SeekL/... <br/>
ReadN/ReadS -> Wait for INT3 IRQ -> clear IRQ (write 0x1f to 1f801803h.0) -> SetMode/SetLoc/... <br/>
```
Will not drop any of the two commands, thus execute sequentially.<br/>
<br/>

```
Stop -> Wait for INT3 IRQ -> clear IRQ (write 0x1f to 1f801803h.0) -> SetMode/Pause/...<br/>
```
Will drop the second response of Stop(), and then execute the next command.<br/>




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
  ... maybe SMADPCLR (1F801803h.Index1.bit5) does clear SoundMap ADPCM buf?
  transfer 900h bytes (same format as ADPCM sectors) (Port 1F801801h.Index1)
  Note: Before sending a byte, one should wait for DRQs (1F801801h.Bit6=1)
  Note: ADPCM output doesn't start until the last (900h'th) byte is transferred
```
Sound Map mode may be very useful for testing XA-ADPCM directly from within an
exe file (without needing a cdrom with ADPCM sectors). And, Sound Map supports
both 4bit and 8bit compression (the SPU supports only 4bit).<br/>
Caution: If ADPCM wasn't playing, and one sends one 900h-byte block, then it
will get stored in one of three 900h-byte slots in SRAM, and one would expect
that slot to be played when the ADPCM output starts - however, actually, the
hardware will more or less randomly play one of the three slots; not
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
  1Ch Reset        -               INT3(stat), Delay            ;-not DTL-H2000
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
Some commands (04h,05h,10h,11h,1Dh) do also trigger Error 80h when the disk is
stopped.<br/>

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
  80h..8Fh a,b       ?                ;seem to do something on PS2
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
Multiple effects at once. Sets mode=20h, activates drive motor, Standby, abort
all commands.<br/>

#### Reset - Command 1Ch,(...) --\> INT3(stat) --\> Delay(1/8 seconds)
```
  Caution: Not supported on DTL-H2000 (v01)
```
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
around N-5..N+2 in double speed mode). This command will stop any current or pending ReadN or ReadS.<br/>
Trying to use SeekL on Audio CDs passes okay on the first response, but (after
two seconds or so) the second response will return an error (stat+4,04h), and
stop the drive motor... that error doesn't appear ALWAYS though... works in
some situations... such like when previously reading data sectors or so...?<br/>

#### SeekP - Command 16h --\> INT3(stat) --\> INT2(stat)
Seek to Setloc's location in audio mode (using the Subchannel Q position data,
which works on both Audio on Data disks).<br/>
After the seek, the disk stays on the seeked location forever (namely: when
seeking sector N, it does stay at around N-9..N-1 in single speed mode, or at
around N-2..N in double speed mode). This command will stop any current or pending ReadN or ReadS. <br/>
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
The command does automatically read the TOC of the new session. BUG: Older CD
Firmwares (16 May 1995 and older) don't clear the old TOC when loading Session
1, in that case SetSession(1) may update some (not all) TOC entries; ending up
with a mixup of old and new TOC entries.<br/>
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

When the shell is opened, INT5 is triggered regardless of whether a command was
executing or not. When this happens, all bits except shell open and error are cleared
in the status register. The error byte in the INT5 is set to 08h.<br/>

Some games send a Stop command before changing discs, but others just wait for the
user to open the shell, causing the disc to stop. The game can then send GetStat commands,
looping until bit 4 is cleared to detect when the new disc has been inserted.<br/>

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
[CDROM Protection - LibCrypt](cdromformat.md#cdrom-protection-libcrypt)<br/>

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
[CDROM - Test Commands - Version, Switches, Region, Chipset, SCEx](cdromdrive.md#cdrom-test-commands-version-switches-region-chipset-scex)<br/>
[CDROM - Test Commands - Test Drive Mechanics](cdromdrive.md#cdrom-test-commands-test-drive-mechanics)<br/>
[CDROM - Test Commands - Prototype Debug Transmission](cdromdrive.md#cdrom-test-commands-prototype-debug-transmission)<br/>
[CDROM - Test Commands - Read/Write Decoder RAM and I/O Ports](cdromdrive.md#cdrom-test-commands-readwrite-decoder-ram-and-io-ports)<br/>
[CDROM - Test Commands - Read HC05 SUB-CPU RAM and I/O Ports](cdromdrive.md#cdrom-test-commands-read-hc05-sub-cpu-ram-and-io-ports)<br/>



##   CDROM - Test Commands - Version, Switches, Region, Chipset, SCEx
#### 19h,20h --\> INT3(yy,mm,dd,ver)
Indicates the date (Year-month-day, in BCD format) and version of the HC05
CDROM controller BIOS. Known/existing values are:<br/>
```
  (unknown)        ;DTL-H2000 (with SPC700 instead HC05)
  94h,09h,19h,C0h  ;PSX (PU-7)               19 Sep 1994, version vC0 (a)
  94h,11h,18h,C0h  ;PSX (PU-7)               18 Nov 1994, version vC0 (b)
  94h,11h,28h,01h  ;PSX (DTL-H2000)          28 Nov 1994, version v01 (debug)
  95h,05h,16h,C1h  ;PSX (LATE-PU-8)          16 May 1995, version vC1 (a)
  95h,07h,24h,C1h  ;PSX (LATE-PU-8)          24 Jul 1995, version vC1 (b)
  95h,07h,24h,D1h  ;PSX (LATE-PU-8,debug ver)24 Jul 1995, version vD1 (debug)
  96h,08h,15h,C2h  ;PSX (PU-16, Video CD)    15 Aug 1996, version vC2 (VCD)
  96h,08h,18h,C1h  ;PSX (LATE-PU-8,yaroze)   18 Aug 1996, version vC1 (yaroze)
  96h,09h,12h,C2h  ;PSX (PU-18) (japan)      12 Sep 1996, version vC2 (a.jap)
  97h,01h,10h,C2h  ;PSX (PU-18) (us/eur)     10 Jan 1997, version vC2 (a)
  97h,08h,14h,C2h  ;PSX (PU-20)              14 Aug 1997, version vC2 (b)
  98h,06h,10h,C3h  ;PSX (PU-22)              10 Jun 1998, version vC3 (a)
  99h,02h,01h,C3h  ;PSX/PSone (PU-23, PM-41) 01 Feb 1999, version vC3 (b)
  A1h,03h,06h,C3h  ;PSone/late (PM-41(2))    06 Jun 2001, version vC3 (c)
  (unknown)        ;PS2,   xx xxx xxxx, late PS2 models...?
```

#### 19h,21h --\> INT3(flags)
Returns the current status of the POS0 and DOOR switches.<br/>
```
  Bit0   = HeadIsAtPos0 (0=No, 1=Pos0)
  Bit1   = DoorIsOpen   (0=No, 1=Open)
  Bit2   = EjectButtonOrOutSwOrSo? (DTL-H2000 only) (always 0 on retail)
  Bit3-7 = AlwaysZero
```

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

#### DTL-H2000 Memory Map
This version allows to read the whole 64Kbyte memory space (withou mirroring
everything to first 300h bytes). I/O Ports and Variables are at different
locations:<br/>
```
  000h..0DFh   RAM Part 1 (C0h bytes)
  0E0h..0FFh   I/O Area
  100h..1DFh   RAM Part 2 (C0h bytes)
  1E0h..1FFh   I/O Area
  200h..2DFh   RAM Part 3 (100h bytes)
  2E0h..7FFFh  Unknown
  8000h-BFFFh  Unknown  (lower 16K of 32K EPROM) (or unused?)
  C000h-FFFFh  Firmware (upper 16K of 32K EPROM)
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

The order of steps that happen when sending a command to the CD controller look roughly like this:
```
e.g. SetMode:
1. Command busy flag set immediately.
2. Response FIFO is populated.
3. Command is being processed.
4. Command busy flag is unset and parameter fifo is cleared.
5. Shortly after (around 1000-6000 cycles later), CDROM IRQ is fired.
```


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
pending INT1, one for undelivered INT1, and one for currently/incompletely
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
