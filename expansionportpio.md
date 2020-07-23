#   Expansion Port (PIO)
Expansion Port can contain ROM, RAM, I/O Ports, etc. For ROM, the first 256
bytes would contain the expansion ROM header.<br/>

For region 1, the CPU outputs a chip select signal (CPU Pin 98, /EXP).<br/>
For region 2, the CPU doesn't produce a chip select signal (the region is
intended to contain multiple I/O ports, which do require an address decoder
anyways, that address decoder could treat any /RD or /WR with A13=Hi and A23=Hi
and A22=Lo as access to expansion region 2 (for /WR, A22 may be ignored;
assuming that the BIOS is read-only).<br/>

#### Size/Bus-Width
The BIOS initalizes Expansion Region 1 to 512Kbyte with 8bit bus, and Region 2
to 128 bytes with 8bit bus. However, the size and data bus-width of these
regions can be changed, see:<br/>
[Memory Control](memorycontrol.md)<br/>
For Region 1, 32bit reads are supported even in 8bit mode (eg. 32bit opcode
fetches are automatically processed as four 8bit reads).<br/>
For Region 2, only 8bit access seems to be supported (except that probably
16bit mode allows 16bit access), anyways, larger accesses seem to cause
exceptions... not sure if that can be disabled...?<br/>

#### Expansion 1 - EXP1 - Intended to contain ROM
[EXP1 Expansion ROM Header](expansionportpio.md#exp1-expansion-rom-header)<br/>

#### Expansion 2 - EXP2 - Intended to contain I/O Ports
[EXP2 Dual Serial Port (for TTY Debug Terminal)](expansionportpio.md#exp2-dual-serial-port-for-tty-debug-terminal)<br/>
[EXP2 DTL-H2000 I/O Ports](expansionportpio.md#exp2-dtl-h2000-io-ports)<br/>
[EXP2 Post Registers](expansionportpio.md#exp2-post-registers)<br/>
[EXP2 Nocash Emulation Expansion](expansionportpio.md#exp2-nocash-emulation-expansion)<br/>

#### Expansion 3 - EXP3 - Intended to contain RAM
Not used by BIOS nor by any games. Seems to contain 1Mbyte RAM with 16bit
databus (ie. 512Kx16) in DTL-H2000.<br/>

#### Other Expansions
Aside from the above, the Expansion regions can be used for whatever purpose,
however, mind that the BIOS is reading from the ROM header region, and is
writing to the POST register (so 1F000000h-1F0000FFh and 1F802041h should be
used only if the hardware isn't disturbed by those accesses).<br/>

#### Missing Expansion Port
The expansion port is installed only on older PSX boards, newer PSX boards and
all PSone boards don't have that port. However, the CPU should still output all
expansion signals, and there should be big soldering points on the board, so
it'd be easy to upgrade the console.<br/>

#### Latched Address Bus
Note that A0..A23 are latched outputs, so they can be used as general purpuse
24bit outputs, provided that the system bus isn't used for other purposes (such
like /BIOS, /SPU, /CD accesses) (A0..A23 are not affected by Main RAM and GPU
addressing, nor by internal I/O ports like Timer and IRQ registers).<br/>



##   EXP1 Expansion ROM Header
#### Expansion 1 - ROM Header (accessed with 8bit databus setting)
```
  Address  Size Content
  1F000000h 4   Post-Boot Entrypoint (eg. 1F000100h and up)
  1F000004h 2Ch Post-Boot ID ("Licensed by Sony Computer Entertainment Inc.")
  1F000030h 50h Post-Boot TTY Message (must contain at least one 00h byte)
  1F000080h 4   Pre-Boot Entrypoint  (eg. 1F000100h and up)
  1F000084h 2Ch Pre-Boot ID  ("Licensed by Sony Computer Entertainment Inc.")
  1F0000B0h 50h Not used     (should be zero, but may contain code/data/io)
  1F000100h ..  Code, Data, I/O Ports, etc.
```
The entrypoints are called if their corresonding ID strings are present, return
address to BIOS is passed in R31, so the expansion ROM may return control to
BIOS, if that should be desired.<br/>
Aside from verifying the IDs, the BIOS will also display the Post-Boot ID
string (and the following message string) via TTY (done right before calling
the Post-Boot Entrypoint).<br/>

#### Pre-Boot Function
The Pre-Boot function is called almost immediately after Reset, with only some
Memory Control registers initialized, the BIOS function vectors at A0h, B0h,
and C0h are NOT yet initialized, so the Pre-Boot function can't use them.<br/>

#### Post-Boot Function
The Post-Boot function gets called while showing the "PS" logo, but before
loading the .EXE file. The BIOS function vectors at A0h, B0h, and C0h are
already installed and can be used by the Post-Boot Function.<br/>
Note that the Post-Boot Function is called ONLY when the "PS" logo is shown
(ie. not if the CDROM drive is empty, or if it contains an Audio CD).<br/>

#### Mid-Boot Hook
One common trick to hook the Kernel after BIOS initialization, but before CDROM
loading is to use the Pre-Boot handler to set a COP0 opcode fetch hardware
breakpoint at 80030000h (after returning from the Pre-Boot handler, the Kernel
will initialize important things like A0h/B0h/C0h tables, and will then break
again when starting the GUI code at 80030000h) (this trick is used by Action
Replay v2.0 and up).<br/>

#### Note
Expansion ROMs are most commonly used in cheat devices,<br/>
[Cheat Devices](cheatdevices.md)<br/>



##   EXP2 Dual Serial Port (for TTY Debug Terminal)
#### SCN2681 Dual Asynchronous Receiver/Transmitter (DUART)
The PSX/PSone retail BIOS contains some TTY Debug Terminal code; using an
external SCN2681 chip which can be connected to the expansion port.<br/>
Whilst supported by all PSX/PSone retail BIOSes on software side, there aren't
any known PSX consoles/devboards/expansions actually containing DUARTs on
hardware side.<br/>

#### 1F802023h/Read - RHRA - DUART Rx Holding Register A (FIFO) (R)
#### 1F80202Bh/Read - RHRB - DUART Rx Holding Register B (FIFO) (R)
#### 1F802023h/Write - THRA - DUART Tx Holding Register A (W)
#### 1F80202Bh/Write - THRB - DUART Tx Holding Register B (W)
```
  7-0  Data (aka Character)
```
The hardware can hold max 2 Tx characters per channel (1 in the THR register,
and one currently processed in the Tx Shift Register), and max 4 Rx characters
(3 in the RHR FIFO, plus one in the Rx Shift Register) (when receiving a 5th
character, the "old newest" value in the Rx Shift Register is lost, and the
overrun flag is set).<br/>

#### 1F802020h/FirstAccess - MR1A - DUART Mode Register 1.A (R/W)
#### 1F802028h/FirstAccess - MR1B - DUART Mode Register 1.B (R/W)
```
  7    RxRTS Control       (0=No, 1=Yes)
  6    RxINT Select        (0=RxRDY, 1=FFULL)
  5    Error Mode          (0=Char, 1=Block)
  4-3  Parity Mode   (0=With Parity, 1=Force Parity, 2=No Parity, 3=Multidrop)
  2    Parity Type         (0=Even, 1=Odd)
  1-0  Bits per Character  (0=5bit, 1=6bit, 2=7bit, 3=8bit)
```
Note: In block error mode, block error conditions must be cleared by using the
error reset command (command 4) or a receiver reset (command 2).<br/>

#### 1F802020h/SecondAccess - MR2A - DUART Mode Register 2.A (R/W)
#### 1F802028h/SecondAccess - MR2B - DUART Mode Register 2.B (R/W)
```
  7-6  Channel Mode       (0=Normal, 1=Auto-Echo, 2=Local loop, 3=Remote loop)
  5    TxRTS Control      (0=No, 1=Yes) (when 1 --> OP0=RTSA / OP1=RTSB)
  4    CTS Enable         (0=No, 1=Yes) (when 1 --> IP0=CTSA / IP1=CTSB)
  3-0  Tx Stop Bit Length (00h..0Fh = see below)
```
Stop Bit Lengths:<br/>
```
  0=0.563  1=0.625  2=0.688  3=0.750  4=0.813  5=0.875  6=0.938  7=1.000
  8=1.563  9=1.625  A=1.688  B=1.750  C=1.813  D=1.875  E=1.938  F=2.000
```
Add 0.5 to values shown for 0..7 if channel is programmed for 5 bits/char.<br/>

#### 1F802021h/Write - CSRA - DUART Clock Select Register A (W)
#### 1F802029h/Write - CSRB - DUART Clock Select Register B (W)
```
  7-4  Rx Clock Select  (0..0Ch=See Table, 0Dh=Timer, 0Eh=16xIP, 0Fh=1xIP)
  3-0  Tx Clock Select  (0..0Ch=See Table, 0Dh=Timer, 0Eh=16xIP, 0Fh=1xIP)
```
The 2681 has some sets of predefined baud rates (set1/set2 selected via ACR.7),
additionally, in BRG Test Mode, set3/set4 are used instead of set1/set2), the
baud rates for selections 00h..0Dh are:<br/>
```
  Rate 00h  01h 02h   03h   04h   05h   06h    07h  08h   09h  0Ah   0Bh  0Ch
  Set1 50   110 134.5 200   300   600   1200   1050 2400  4800 7200  9600 38400
  Set2 75   110 134.5 150   300   600   1200   2000 2400  4800 1800  9600 19200
  Set3 4800 880 1076  19200 28800 57600 115200 1050 57600 4800 57600 9600 38400
  Set4 7200 880 1076  14400 28800 57600 115200 2000 57600 4800 14400 9600 19200
```
Selection 0Eh/0Fh are using an external clock source (derived from
IP3,IP4,IP5,IP6 pins; for TxA,RxA,TxB,RxB respectively).<br/>

#### 1F802022h/Write - CRA - DUART Command Register A (W)
#### 1F80202Ah/Write - CRB - DUART Command Register B (W)
```
  7    Not used    (should be 0)
  6-4  Miscellaneous Commands (0..7 = see below)
  3    Disable Tx  (0=No change, 1=Disable)
  2    Enable Tx   (0=No change, 1=Enable) ;Don't use with Command 3 (Reset Rx)
  1    Disable Rx  (0=No change, 1=Disable)
  0    Enable Rx   (0=No change, 1=Enable) ;Don't use with Command 2 (Reset Tx)
```
The command values for CRA (or CRB) are:<br/>
```
  0 No command          ;no effect
  1 Reset MR pointer    ;force "FirstAccess" state for MR1A (or MR1B) access
  2 Reset receiver      ;reset RxA (or RxB) registers, disable Rx, flush Fifo
  3 Reset transmitter   ;reset TxA (or TxB) registers
  4 Reset Error Flags           ;reset SRA.7-4 (or SRB.7-4) to zero
  5 Reset Break-Change IRQ Flag ;reset ISR.2 (or ISR.6) to zero
  6 Start break  ;after current char, pause Tx with TxDA=Low (or TxDB=Low)
  7 Stop break   ;output one High bit, then continue Tx (ie. undo pause)
```
Access to the upper four bits of the command register should be separated by 3
edges of the X1 clock. A disabled transmitter cannot be loaded.<br/>

#### 1F802025h/Read - ISR - DUART Interrupt Status Register (R)
#### 1F802025h/Write - IMR - DUART Interrupt Mask Register (W)
```
  7    Input Port Change   (0=No, 1=Yes) (Ack via reading IPCR) ;see ACR.3-0
  6    Break Change B      (0=No, 1=Yes) (Ack via CRB/Command5)
  5    RxRDYB/FFULLB       (0=No, 1=Yes) (Ack via reading data) ;see MR1B.6
  4    THRB Empty (TxRDYB) (0=No, 1=Yes) (Ack via writing data) ;same as SRB.2
  3    Counter Ready       (0=No, 1=Yes) (Ack via CT_STOP)
  2    Break Change A      (0=No, 1=Yes) (Ack via CRA/Command5)
  1    RxRDYA/FFULLA       (0=No, 1=Yes) (Ack via reading data) ;see MR1A.6
  0    THRA Empty (TxRDYA) (0=No, 1=Yes) (Ack via writing data) ;same as SRA.2
```

#### 1F802021h/Read - SRA - DUART Status Register A (R)
#### 1F802029h/Read - SRB - DUART Status Register B (R)
```
  7    Rx Received Break*        (0=No, 1=Yes) ;received 00h without stop bit
  6    Rx Framing Error*         (0=No, 1=Yes) ;received data without stop bit
  5    Rx Parity Error*          (0=No, 1=Yes) ;received data with bad parity
  4    Rx Overrun Error          (0=No, 1=Yes) ;Rx FIFO full + RxShiftReg full
  3    Tx Underrun  (TxEMT)      (0=No, 1=Yes) ;both TxShiftReg and THR empty
  2    Tx THR Empty (TxRDY)      (0=No, 1=Yes) ;same as ISR.0 / ISR.4
  1    Rx FIFO Full (FFULL)      (0=No, 1=Yes) ;set upon 3 or more characters
  0    Rx FIFO Not Empty (RxRDY) (0=No, 1=Yes) ;set upon 1 or more characters
```
Bit7-5 are appended to the corresponding data character in the receive FIFO. A
read of the status provides these bits (7:5) from the top of the FIFO together
with bits (4:0). These bits are cleared by a "reset error status" command. In
character mode they are discarded when the corresponding data character is read
from the FIFO. In block error mode, block error conditions must be cleared by
using the error reset command (command 4x) or a receiver reset.<br/>

#### 1F802024h/Write - ACR - DUART Aux. Control Register (W)
```
  7    Select Baud Rate Generator (BRG) Set   (0=Set1/Set3, 1=Set2/Set4)
  6-4  Counter/Timer Mode and Source          (see below)
  3-0  IP3..IP0 Change Interrupt Enable Flags (0=Off, 1=On)
```
Counter/Timer Mode and Clock Source Settings:<br/>
```
  Num  Mode      Clock Source
  0h   Counter   External (IP2)
  1h   Counter   TxCA - 1x clock of Channel A transmitter
  2h   Counter   TxCB - 1x clock of Channel B transmitter
  3h   Counter   Crystal or external clock (x1/CLK) divided by 16
  4h   Timer     External (IP2)
  5h   Timer     External (IP2) divided by 16
  6h   Timer     Crystal or external clock (x1/CLK)
  7h   Timer     Crystal or external clock (x1/CLK) divided by 16
```
In Counter Mode, the Counter Ready flag is set on any underflow, and the
counter wraps to FFFFh and keeps running (but may get stopped by software).<br/>
In Timer Mode, automatic reload occurs on any underflow, the counter flag
(which can be output to OP3) is toggled on any underflow, but the Counter Ready
flag is set only on each 2nd underflow (unlike as in Counter mode).<br/>

#### 1F802024h/Read - IPCR - DUART Input Port Change Register (R)
```
  7-4  IP3..IP0 Change Occured Flags (0=No, 1=Yes)    ;auto reset after read
  3-0  Current IP3-IP0 Input states  (0=Low, 1=High)  ;Same as IP.3-0
```
Reading from this register automatically resets IPCR.7-4 and ISR.7.<br/>

#### 1F80202Dh/Read - IP - DUART Input Port (R)
```
  7    Not used (always 1)
  6-0  Current IP6-IP0 Input states (0=Low, 1=High)  ;LSBs = Same as IPCR.3-0
```
IP0-6 can be used as general purpose inputs, or for following special purposes:<br/>
```
  IP6 External RxB Clock     ;see CSRB.7-4
  IP5 External TxB Clock     ;see CSRB.3-0
  IP4 External RxA Clock     ;see CSRA.7-4
  IP3 External TxA Clock     ;see CSRA.3-0
  IP2 External Timer Input   ;see AUX.6-4
  IP1 Clear to Send B (CTSB) ;see MR2B.5
  IP0 Clear to Send A (CTSA) ;see MR2A.5
```
Note: The 24pin chip doesn't have any inputs, the 28pin chip has only one input
(IP2), the 40pin/44pin chips have seven inputs (IP0-IP6).<br/>

#### 1F80202Eh/Write - DUART Set Output Port Bits Command (Set means Out=LOW)
#### 1F80202Fh/Write - DUART Reset Output Port Bits Command (Reset means Out=HIGH)
```
  7-0  Change "OPR" OP7-OP0 Output states (0=No change, 1=Set/Reset)
```
Note: The 24pin chip doesn't have any outputs, the 28pin chip has only two
outputs (OP0,OP1), the 40pin/44pin chips have eight outputs (OP0-OP7).<br/>

#### 1F80202Dh/Write - OPCR - DUART Output Port Configuration Register (W)
```
  7    OP7      (0=OPR.7, 1=TxRDYB)
  6    OP6      (0=OPR.6, 1=TxRDYA)
  5    OP5      (0=OPR.5, 1=RxRDY/FFULLB)
  4    OP4      (0=OPR.4, 1=RxRDY/FFULLA)
  3-2  OP3      (0=OPR.3, 1=Clock/Timer Output, 2=TxCB(1x), 3=RxCB(1x))
  1-0  OP2      (0=OPR.2, 1=TxCA(16x), 2=TxCA(1x), 3=RxCA(1x))
```
Additionally, the OP0 and OP1 outputs are controlled via MR2A.5 and MR2B.5.<br/>

#### 1F802022h/Read - - DUART Toggle Baud Rate Generator Test Mode (Read=Strobe)
#### 1F80202Ah/Read - - DUART Toggle 1X/16X Test Mode (Read=Strobe)
```
  7-0  Not used (just issue a dummy-read to toggle the test mode on/off)
```
BGR Test switches between Baud Rate Set1/Set2 and Set3/Set4.<br/>
1X/16X Test switches between whatever...?<br/>

#### 1F80202Eh/Read - CT\_START - DUART Start Counter Command (Read=Strobe)
#### 1F80202Fh/Read - CT\_STOP - DUART Stop Counter Command (Read=Strobe)
```
  7-0  Not used (just issue a dummy-read to strobe start/stop command)
```
Start: Forces reload (copies CTLR/CTUR to CTL/CTU), and starts the timer.<br/>
Stop-in-Counter-Mode: Resets ISR.3, and stops the timer.<br/>
Stop-in-Timer-Mode: Resets ISR.3, but doesn't stop the timer.<br/>

#### 1F802026h/Read - CTU - DUART Counter/Timer Current Value, Upper/Bit15-8 (R)
#### 1F802027h/Read - CTL - DUART Counter/Timer Current Value, Lower/Bit7-0 (R)
#### 1F802026h/Write - CTUR - DUART Counter/Timer Reload Value, Upper/Bit15-8 (W)
#### 1F802027h/Write - CTLR - DUART Counter/Timer Reload Value, Lower/Bit7-0 (W)
The CTLR/CTUR reload value is copied to CTL/CTU upon Start Counter Command. In
Timer mode (not in Counter mode), it is additionally copied automatically when
the timer undeflows.<br/>

#### 1F80202Ch - N/A - DUART Reserved Register (neither R nor W)
Reserved.<br/>

#### Chip versions
The SCN2681 is manufactured with 24..44 pins, the differences are:<br/>
```
  24pin basic cut-down version          ;without IP0-1/OP0-1 = without CTS/RTS
  28pin additional IP2,OP0,OP1,X2       ;without IP0-1 = without CTS
  40pin additional IP0-IP6,OP0-OP7,X2   ;full version
  44pin same as 40pin with four NC pins ;full version (SMD)
```
Unknown which of them is supposed to be used with the PSX?<br/>
Note: The Motorola 68681 should be the same as the Philips/Signetics 2681.<br/>

#### Notes
Unknown if the Interrupt signal is connected to the PSX... there seems to be no
spare IRQ for it, though it \<might\> share an IRQ with whatever other
hardware...?<br/>
The BIOS seems to use only one of the two channels; for the std\_io functions:<br/>
[BIOS TTY Console (std_io)](kernelbios.md#bios-tty-console-stdio)<br/>
Aside from the external DUART, the PSX additionally contains an internal UART,<br/>
[Serial Port (SIO)](serialportsio.md)<br/>
The DTL-H2000 devboard uses a non-serial "ATCONS" channel for TTY stuff,<br/>
[EXP2 DTL-H2000 I/O Ports](expansionportpio.md#exp2-dtl-h2000-io-ports)<br/>



##   EXP2 DTL-H2000 I/O Ports
The DTL-H2000 contains extended 8Mbyte Main RAM (instead of normal 2Mbyte),
plus additional 1MByte RAM in Expansion Area at 1FA00000h, plus some I/O ports
at 1F8020xxh:<br/>

#### 1F802000h - DTL-H2000: EXP2:  - ATCONS STAT (R)
```
  0    Unknown, used for something
  1    Unknown/unused
  2    Unknown, used for something
  3    TTY/Atcons TX Ready     (0=Busy, 1=Ready)
  4    TTY/Atcons RX Available (0=None, 1=Yes)
  5-7  Unknown/unused
```

#### 1F802002h - DTL-H2000: EXP2:  - ATCONS DATA (R and W)
```
  0-7  TTY/Atcons RX/TX Data
```
TTY channel for message output (TX) and debug console keyboard input (RX). The
DTL-H2000 is using this "ATCONS" stuff instead of the DUART stuff used in
retail console BIOSes ("CONS" seems to refer to "Console", and "AT" might refer
to PC/AT or whatever).<br/>

#### 1F802004h - DTL-H2000: EXP2:  - 16bit - ?
```
  0-15 Data...?
```

#### 1F802030h - DTL-H2000: Secondary IRQ10 Controller (IRQ Flags)
This register does expand IRQ10 (Lightgun) to more than one IRQ source. The
register contains only Secondary IRQ Flags (there seem to be no Secondary IRQ
Enable bits; at least not for Lightguns).<br/>
```
  0     ... used for something
  1    Lightgun IRQ (write: 0=No change, 1=Acknowledge) (read: 0=None, 1=IRQ)
  2-3  Unknown/unused (write: 0=Normal)
  4     ... acknowledged at 1FA00B04h, otherwise unused
  5     ... TTY RX ?
  6-7  Unknown/unused (write: 0=Normal)
  8-31 Not used by DTL-H2000 BIOS (but Lightgun games write 0 to these bits)
```
Retail games that support IRQ10-based "Konami" Lightguns are containing code
for detecting and accessing port 1F802030h. The detection works by examining a
value in the BIOS ROM like so:<br/>
```
  IF [BFC00104h]=00002000h then Port 1F802030h does exist     (DTL-H2000)
  IF [BFC00104h]=00002500h then Port 1F802030h does NOT exist
  IF [BFC00104h]=00000003h then Port 1F802030h does NOT exist (default)
  IF [BFC00104h]= <other>  then Port 1F802030h does NOT exist
```
Normal consoles don't include Port 1F802030h, and IRQ10 is wired directly to
the controller port, and the value at [BFC00104h] is always 00000003h.
Accordingly, one cannot upgrade the console just by plugging a Secondary IRQ10
controller to the expansion port (instead, one would need to insert the
controller between the CPU and controller plug, and to install a BIOS with
[BFC00104h]=00002000h).<br/>
The DTL-H2000 BIOS accesses 1F802030h with 8bit load/store opcodes, however,
the Lightgun games use 32bit load/store - which is theoretically overlapping
port 1F802032h, though maybe the memory system does ignore the upper bits.<br/>

#### 1F802032h - DTL-H2000: EXP2:  - maybe IRQ enable?
```
  0    Used for something (CLEARED on some occassions)
  1-3  Unknown/unused
  4    Used for something (SET on some occassions)
  5-7  Unknown/unused
```

#### 1F802040h - DTL-H2000: EXP2: 1-byte - DIP Switch?
```
  0-7  DIP Value (00h..FFh, but should be usually 00h..02h)
```
This register selects the DTL-H2000 boot mode, for whatever reason it's called
"DIP Switch" register, although the DTL-H2000 boards don't seem to contain any
such DIP Switches (instead, it's probably configured via some I/O ports on PC
side). Possible values are:<br/>
```
  DIP=0 --> .. long delay before TTY?   with "PSX>" prompt, throws CDROM cmds
  DIP=1 --> .. long delay before TTY?   no "PSX>" prompt           PSY-Q?
  DIP=2 --> .. instant TTY?             with "PSX>" prompt
  DIP=3 --> Lockup
  DIP=04h..FFh --> Lockup with POST=04h..FFh
```

#### 1F802042h - DTL-H2000: EXP2: POST/LED (R/W)
[EXP2 Post Registers](expansionportpio.md#exp2-post-registers)<br/>



##   EXP2 Post Registers
#### 1F802041h - POST - External 7-segment Display (W)
```
  0-3  Current Boot Status (00h..0Fh)
  4-7  Not used by BIOS    (always set to 0)
```
During boot, the BIOS writes incrementing values to this register, allowing to
display the current boot status on an external 7 segment display (much the same
as Port 80h used in PC BIOSes).<br/>

#### 1F802042h - DTL-H2000: EXP2: POST/LED (R/W)
```
  0-7 Post/LED value
```
8bit wide, otherwise same as POST 1F802041h on retail consoles.<br/>

#### 1F802070h - POST2 - Unknown? (W) - PS2
Might be a configuration port, or it's another POST register (which is used
prior to writing the normal POST bytes to 1FA00000h).<br/>
The first write to 1F802070h is 32bit, all further writes seem to be 8bit.<br/>

#### 1FA00000h - POST3 - External 7-segment Display (W) - PS2
Similar to POST, but PS2 BIOS uses this address.<br/>



##   EXP2 Nocash Emulation Expansion
#### 1F802060h Emu-Expansion ID1 "E" (R)
#### 1F802061h Emu-Expansion ID2 "X" (R)
#### 1F802062h Emu-Expansion ID3 "P" (R)
#### 1F802063h Emu-Expansion Version (01h) (R)
Contains ID and Version.<br/>

#### 1F802064h Emu-Expansion Enable1 "O" (R/W)
#### 1F802065h Emu-Expansion Enable2 "N" (R/W)
Activates the Halt and Turbo Registers (when set to "ON").<br/>

#### 1F802066h Emu-Expansion Halt (R)
When enabled (see above), doing an 8bit read from this address stops the CPU
emulation unless/until an Interrupt occurs (when "CAUSE AND SR AND FF00h"
becomes nonzero). Can be used to reduce power consumption, and to make the
emulation faster.<br/>

#### 1F802067h Emu-Expansion Turbo Mode Flags (R/W)
When enabled (see above), writing to this register activates/deactivates
"turbo" mode, which is causing new data to arrive immediately after
acknowledging the previous interrupt.<br/>
```
  0   CDROM Turbo       (0=Normal, 1=Turbo)
  1   Memory Card Turbo (0=Normal, 1=Turbo)
  2   Controller Turbo  (0=Normal, 1=Turbo)
  3-7 Reserved (must be zero)
```



