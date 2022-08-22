#   Pocketstation
#### Pocketstation
[Pocketstation Overview](pocketstation.md#pocketstation-overview)<br/>
[Pocketstation I/O Map](pocketstation.md#pocketstation-io-map)<br/>
[Pocketstation Memory Map](pocketstation.md#pocketstation-memory-map)<br/>
[Pocketstation IO Video and Audio](pocketstation.md#pocketstation-io-video-and-audio)<br/>
[Pocketstation IO Interrupts and Buttons](pocketstation.md#pocketstation-io-interrupts-and-buttons)<br/>
[Pocketstation IO Timers and Real-Time Clock](pocketstation.md#pocketstation-io-timers-and-real-time-clock)<br/>
[Pocketstation IO Infrared](pocketstation.md#pocketstation-io-infrared)<br/>
[Pocketstation IO Memory-Control](pocketstation.md#pocketstation-io-memory-control)<br/>
[Pocketstation IO Communication Ports](pocketstation.md#pocketstation-io-communication-ports)<br/>
[Pocketstation IO Power Control](pocketstation.md#pocketstation-io-power-control)<br/>
[Pocketstation SWI Function Summary](pocketstation.md#pocketstation-swi-function-summary)<br/>
[Pocketstation SWI Misc Functions](pocketstation.md#pocketstation-swi-misc-functions)<br/>
[Pocketstation SWI Communication Functions](pocketstation.md#pocketstation-swi-communication-functions)<br/>
[Pocketstation SWI Execute Functions](pocketstation.md#pocketstation-swi-execute-functions)<br/>
[Pocketstation SWI Date/Time/Alarm Functions](pocketstation.md#pocketstation-swi-datetimealarm-functions)<br/>
[Pocketstation SWI Flash Functions](pocketstation.md#pocketstation-swi-flash-functions)<br/>
[Pocketstation SWI Useless Functions](pocketstation.md#pocketstation-swi-useless-functions)<br/>
[Pocketstation BU Command Summary](pocketstation.md#pocketstation-bu-command-summary)<br/>
[Pocketstation BU Standard Memory Card Commands](pocketstation.md#pocketstation-bu-standard-memory-card-commands)<br/>
[Pocketstation BU Basic Pocketstation Commands](pocketstation.md#pocketstation-bu-basic-pocketstation-commands)<br/>
[Pocketstation BU Custom Pocketstation Commands](pocketstation.md#pocketstation-bu-custom-pocketstation-commands)<br/>
[Pocketstation File Header/Icons](pocketstation.md#pocketstation-file-headericons)<br/>
[Pocketstation File Images](pocketstation.md#pocketstation-file-images)<br/>
[Pocketstation XBOO Cable](pocketstation.md#pocketstation-xboo-cable)<br/>



##   Pocketstation Overview
#### Sony's Pocketstation (SCPH-4000) (1998)
The Pocketstation is a memory card with built-in LCD screen and buttons; aside
from using it as memory storage device, it can be also used as miniature
handheld console.<br/>

```
  CPU        ARM7TDMI (32bit RISC Processor) (variable clock, max 7.995MHz)
  Memory     2Kbytes SRAM (battery backed), 16Kbytes BIOS ROM, 128Kbytes FLASH
  Display    32x32 pixel LCD (black and white) (without any grayscales)
  Sound      Mini Speaker "(12bit PCM) x 1 unit" / "8bit PCM with 12bit range"
  Controls   5 input buttons, plus 1 reset button
  Infrared   Bi-directional (IrDA based)
  Connector  Playstation memory card interface
  RTC        Battery backed Real-Time Clock with time/date function
  Supply     CR2032 Battery (3VDC) (used in handheld mode, and for SRAM/RTC)
    _________
   / _______ \
  | |       | |
  | |  LCD  | |                                __
  | |_______| |                Side Views     | _|
  |\_________/|                               || <-------- Button Cover
  |   O       |          (Closed)      (Open) ||
  | O   O   O |    ____________          _____||  .------- Reset Button
  |   O       |   | LCD  \____ |        | LCD \|__|_
  |___________|   |___________||        |___________| <--- Memory card plug
```

#### The RTC Problem
The main problem of the Pocketstation seems to be that it tends to reset the
RTC to 1st January 1999 with time 00:00:00 whenever possible.<br/>
The BIOS contains so many RTC-reset functions, RTC-reset buttons, RTC-reset
flags, RTC-reset communication commands, RTC-reset parameters, RTC-reset
exceptions, RTC-reset sounds, and RTC-reset animations that it seems as if Sony
actually WANTED the Time/Date to be destroyed as often as possible.<br/>
The only possible reason for doing this is that the clock hardware is so
inaccurate that Sony must have decided to "solve" the problem at software
engineering side, by erasing the RTC values before the user could even notice
time inaccuracies.<br/>

#### CPU Specs
For details on the ARM7TDMI CPUs opcodes and exceptions, check GBATEK at,<br/>
http://problemkaputt.de/gbatek.htm (or .txt)<br/>
The GBA uses an ARM7TDMI CPU, too.<br/>

Thanks to Exophase, Orion, Fezzik, Dr.Hell for Pocketstation info.<br/>



##   Pocketstation I/O Map
#### Memory and Memory-Control Registers
```
  00000000h RAM        (2KB RAM) (first 512 bytes bytes reserved for kernel)
  02000000h FLASH1     Flash ROM (virtual file-mapped addresses in this region)
  04000000h BIOS_ROM      Kernel and GUI (16KB)
  06000000h F_CTRL        Control of Flash ROM
  06000004h F_STAT        Unknown?
  06000008h F_BANK_FLG    FLASH virtual bank mapping enable flags(16 bits)(R/W)
  0600000Ch F_WAIT1       waitstates...?
  06000010h F_WAIT2       waitstates, and FLASH-Write-Control-and-Status...?
  06000100h F_BANK_VAL    FLASH virtual bank mapping addresses (16 words) (R/W)
  06000300h F_EXTRA       Extra FLASH (256 bytes, including below F_SN, F_CAL)
  06000300h F_SN_LO       Extra FLASH Serial Number LSBs (nocash: 6BE7h)
  06000302h F_SN_HI       Extra FLASH Serial Number MSBs (nocash: 426Ch)
  06000304h F_?           Extra FLASH Unknown ?          (nocash: 05CAh)
  06000306h F_UNUSED1     Extra FLASH Unused halfword    (nocash: FFFFh)
  06000308h F_CAL         Extra FLASH LCD Calibration    (nocash: 001Ah)
  0600030Ah F_UNUSED2     Extra FLASH Unused halfword    (nocash: FFFFh)
  0600030Ch F_?           Extra FLASH Unknown ?          (nocash: 0010h)
  0600030Eh F_UNUSED3     Extra FLASH Unused halfword    (nocash: FFFFh)
  06000310h F_UNUSED4     Extra FLASH Unused (310..3FFh) (nocash: FFFFh-filled)
  08000000h FLASH2        Flash ROM (128KB) (physical addresses in this region)
  08002A54h F_KEY1        Flash Unlock Address 1 (W)
  080055AAh F_KEY2        Flash Unlock Address 2 (W)
```
#### Interrupts and Timers
```
  0A000000h INT_LATCH     Interrupt hold (R)
  0A000004h INT_INPUT     Interrupt Status (R)
  0A000008h INT_MASK_READ Read Interrupt Mask (R)
  0A000008h INT_MASK_SET  Set Interrupt Mask (W)
  0A00000Ch INT_MASK_CLR  Clear Interrupt Mask (W)
  0A000010h INT_ACK       Clear Interrupt hold (W)
  0A800000h T0_RELOAD     Timer 0 Maximum value
  0A800004h T0_COUNT      Timer 0 Current value
  0A800008h T0_MODE       Timer 0 Mode
  0A800010h T1_RELOAD     Timer 1 Maximum value
  0A800014h T1_COUNT      Timer 1 Current value
  0A800018h T1_MODE       Timer 1 Mode
  0A800020h T2_RELOAD     Timer 2 Maximum value
  0A800024h T2_COUNT      Timer 2 Current value
  0A800028h T2_MODE       Timer 2 Mode
  0B000000h CLK_MODE      Clock control (CPU and Timer Speed) (R/W)
  0B000004h CLK_STOP      Clock stop (Sleep Mode)
  0B800000h RTC_MODE      RTC Mode
  0B800004h RTC_ADJUST    RTC Adjust
  0B800008h RTC_TIME      RTC Time (R)
  0B80000Ch RTC_DATE      RTC Date (R)
```
#### Communication Ports, Audio/Video
```
  0C000000h COM_MODE      Com Mode
  0C000004h COM_STAT1     Com Status Register 1 (Bit1=Error)
  0C000008h COM_DATA      Com RX Data (R) and TX Data (W)
  0C000010h COM_CTRL1     Com Control Register 1
  0C000014h COM_STAT2     Com Status Register 2 (Bit0=Ready)
  0C000018h COM_CTRL2     Com Control Register 2
  0C800000h IRDA_MODE     Infrared Control (R/W)
  0C800004h IRDA_DATA     Infrared TX Data
  0C80000Ch IRDA_MISC     Infrared Unknown/Reserved
  0D000000h LCD_MODE      Video Control (R/W)
  0D000004h LCD_CAL       Video Calibration (?)
  0D000100h LCD_VRAM      Video RAM (80h bytes; 32x32bit) (R/W)
  0D800000h IOP_CTRL      IOP control
  0D800004h IOP_STAT      Read Current Start/Stop bits? (R)
  0D800004h IOP_STOP      Stop bits? (W)
  0D800008h IOP_START     Start bits? (W)
  0D80000Ch IOP_DATA      IOP data?   (not used by bios)
  0D800010h DAC_CTRL      DAC Control (R/W)
  0D800014h DAC_DATA      DAC data
  0D800020h BATT_CTRL     Battery Monitor Control
```
BIOS and FLASH can be read only in 16bit and 32bit units (not 8bit).<br/>
Upon reset, BIOS ROM is mirrored to address 00000000h (instead of RAM).<br/>
For most I/O ports, it is unknown if they are (R), (W), or (R/W)...?<br/>
I/O ports are usually accessed at 32bit width, occassionally some ports are
(alternately) accessed at 16bit width. A special case are the F\_SN registers
which seem to be required to be accessed at 16bit (not 32bit).<br/>

#### Memory Access Time
Memory Access Time for Opcode Fetch:<br/>
```
  WRAM        1 cycle (for ARM and THUMB)
  FLASH       2 cycles (for ARM), or 1 cycle (for THUMB)
  BIOS        ?
```
Memory Access Time for Data Read/Write:<br/>
```
  WRAM (and some F_xxx ports)                    1 cycle
  VIRT/PHYS/XTRA_FLASH, BIOS, VRAM, I/O          2 cycles
```
For data access, it doesn't matter if the access is 8bit/16bit/32bit (unlike as
for opcode fetch, where 16bit/thumb can be faster than 32bit/arm). There seems
to be no timing differences for sequential/non-sequential access.<br/>
Additional memory waitstates can be added via F\_WAIT2 (and F\_WAIT1 maybe).<br/>

#### Invalid/Unused Memory Locations
```
  00000800h-00FFFFFFh  Mirrors of 00000000h-000007FFh (2K RAM)
  01000000h-01FFFFFFh  Invalid (read causes data abort) (unused 16MB area)
  020xxxxxh-0201FFFFh  Invalid (read causes data abort) (disabled FLASH banks)
  02020000h-02FFFFFFh  Invalid (read causes data abort) (no Virt FLASH mirrors)
  03000000h-03FFFFFFh  Invalid (read causes data abort) (unused 16MB area)
  04004000h-04FFFFFFh  Mirrors of 04000000h-04003FFFh (16K BIOS)
  05000000h-05FFFFFFh  Invalid (read causes data abort)
  06000014h-060000FFh   Zerofilled (or maybe mirror of a ZERO port?) (F_xxx)
  06000140h-060002FFh   Zerofilled (or maybe mirror of a ZERO port?) (F_xxx)
  06000400h-06FFFFFFh   Zerofilled (or maybe mirror of a ZERO port?) (F_xxx)
  07000000h-07FFFFFFh  Invalid (read causes data abort) (unused 16MB area)
  08020000h-08FFFFFFh  Mirrors of 08000000h-0801FFFFh (128K Physical FLASH)
  09000000h-09FFFFFFh  Invalid (read causes data abort) (unused 16MB area)
  0A000014h-0A7FFFFFh  Mirrors of 0A000008h-0A00000Bh (INT_MASK_READ) (I_xxx)
  0A80000Ch            Mirror of 0A800000h-0A800003h (T0_RELOAD) (T0_xxx)
  0A80001Ch            Mirror of 0A800000h-0A800003h (T0_RELOAD) (T1_xxx)
  0A80002Ch            Mirror of 0A800000h-0A800003h (T0_RELOAD) (T2_xxx)
  0A800030h-0AFFFFFFh  Mirrors of 0A800000h-0A800003h (T0_RELOAD) (T_xxx)
  0B000008h-0B7FFFFFh  Mirrors of .... ? (CLK_xxx)
  0B800010h-0BFFFFFFh  Mirrors of 0B800008h-0B80000Bh (RTC_TIME)
  0C00000Ch-0C00000Fh  Zero (COM_xxx)
  0C00001Ch-0C7FFFFFh   Zerofilled (or maybe mirror of a ZERO port?) (COM_xxx)
  0C800008h-0CFFFFFFh   ? (IRDA_xxx)
  0D000008h-0D0000FFh   Zerofilled (or maybe mirror of a ZERO port?) (LCD_xxx)
  0D000180h-0D7FFFFFh   Zerofilled (or maybe mirror of a ZERO port?) (LCD_xxx)
  0D800018h             ? (DAC_xxx)
  0D80001Ch             ? (DAC_xxx)
  0D800024h-0DFFFFFFh   Zerofilled (or maybe mirror of a ZERO port?) (BATT_xxx)
  0E000000h-FFFFFFFFh  Invalid (read causes data abort) (unused 3872MB area)
```

#### Unsupported 8bit Reads
```
  02000000h-0201FFFFh VIRT_FLASH   ;\
  04000000h-04FFFFFFh BIOS_ROM     ; "garbage_byte" (see below)
  06000300h-060003FFh EXTRA_FLASH  ;
  08000000h-08FFFFFFh PHYS_FLASH   ;/
  0A800001h-0AFFFFFFh Timer area, odd addresses (with A0=1) mirror to 0A800001h
  0B800001h-0BFFFFFFh RTC area, odd addresses (with A0=1) mirror to ...?
```

#### Unsupported 16bit Reads
```
  0B800002h-0BFFFFFEh RTC area, odd addresses (with A1=1) mirror to 0B80000Ah
```

#### garbage\_byte (for unsupported 8bit reads)
The "garbage\_byte" depends on the LSBs of the read address, prefetched opcodes,
and recent data fetches:<br/>
```
  garbage_word = (prefetch OR (ramdata AND FFFFFFD0h))
  garbage_byte = (garbage_word shr (8*(addr and 3))) AND FFh
```
For ARM code, the "prefetch" is the 2nd next opcode after the LDRB:<br/>
```
  prefetch.bit0-31  = [curr_arm_opcode_addr+8]    ;-eg. from arm LDRB
```
For THUMB code, the "prefetch" is the 2nd next opcode after the LDRB (no matter
if that opcode is word-aligned or not), combined with the most recent ARM
opcode prefetch (eg. from the BX opcode switched from ARM to THUMB mode; that
value may get changed on interrupts):<br/>
```
  prefetch.bit0-15  = [recent_arm_opcode_addr+8]  ;-eg. from arm BX to thumb
  prefetch.bit16-31 = [curr_thumb_opcode_addr+4]  ;-eg. from thumb LDRB
```
The "ramdata" is related to most recent RAM read (eg. from POP or LDR opcodes
that have read data from RAM; however, writes to RAM, or literal pool reads
from FLASH don't affect it):<br/>
```
  ramdata.bit0-31   = [recent_ram_read_addr]      ;-eg. from LDR/POP from RAM
```
There might be some more/unknown things that affect the garbage (eg. opcode
fetches from RAM instead of FLASH, partial 8bit/16bit data reads from RAM, or
reads from I/O areas, current CPU clock speed, or unpredictable things like
temperature).<br/>
Note: The garbage\_byte is "used" by the pocketstation "Rockman" series games.<br/>



##   Pocketstation Memory Map
#### Overall Memory Map
```
  00000000h RAM      RAM (2K)   (or mirror of BIOS ROM upon reset)
  02000000h FLASH1   Flash ROM  (virtual file-mapped addresses in this region)
  04000000h BIOS_ROM BIOS (16K) (Kernel and GUI)
  06000300h F_SN...  Seems to contain a bunch of additional FLASH bytes?
  08000000h FLASH2   Flash ROM  (128K) (physical addresses in this region)
  0D000100h LCD_VRAM Video RAM  (128 bytes) (32x32 pixels, 1bit per pixel)
```

#### 00000000h..000001FFh - Kernel RAM
The first 200h bytes of RAM are reserved for the kernel.<br/>
```
  0000000h 20h  Exception handler opcodes (filled with LDR R15,[$+20h] opcodes)
  0000020h 20h  Exception handler addresses (in ARM state, no THUMB bit here)
  0000040h 80h  Sector buffer (and BU command parameter work space)
  00000C0h 8    ComFlags (see GetPtrToComFlags(), SWI 06h for details)
  00000C8h 2    BU Command FUNC3 Address (see GetPtrToFunc3addr() aka SWI 17h)
  00000CAh 1    Value from BU Command_50h, reset by SWI 05h (sense_auto_com)
  00000CBh 2    Not used
  00000CDh 1    Old Year (BCD, 00h..99h) (for sensing wrapping to new century)
  00000CEh 1    Alternate dir_index (when [0D0h]=0) (see SWI 15h and SWI 16h)
  00000CFh 1    Current Century (BCD, 00h..99h) (see GetBcdDate() aka SWI 0Dh)
  00000D0h 2    Current dir_index (for currently executed file, or 0=GUI)
  00000D2h 2    New dir_index (PrepareExecute(flag,dir_index,param), SWI 08h)
  00000D4h 4    New param     (PrepareExecute(flag,dir_index,param), SWI 08h)
  00000D8h 8    Alarm Setting        (see GetPtrToAlarmSetting() aka SWI 13h)
  00000E0h 4    Pointer to SWI table (see GetPtrToPtrToSwiTable() aka SWI 14h)
  00000E4h 3x4  Memory Card BU Command variables
  00000F0h 1    Memory Card FLAG byte (bit3=new_card, bit2=write_error)
  00000F1h 1    Memory Card Error offhold (0=none, 1=once)
  00000F2h 6    Not used
  00000F8h 4x4  Callback Addresses (set via SetCallbacks(index,proc), SWI 01h)
  0000108h 4    Snapshot ID (0xh,00h,"SE")
  000010Ch 74h  IRQ and SWI stack (stacktop at 180h)
  0000180h 80h  FIQ stack (stacktop at 200h)
```
Although one can modify that memory, one usually shouldn't do that, or at least
one must backup and restore the old values before returning control to the GUI
or to other executables. Otherwise, the only way to restore the original values
would be to press the Reset button (which would erase the RTC time/date).<br/>

#### 00000200h..000007FFh - User RAM and User stack (stacktop at 800h)
This region can be freely used by the game. The memory is zerofilled when the
game starts.<br/>

#### 02000000h - FLASH1 - Flash ROM (virtual file-mapped addresses in this region)
This region usually contains the currently selected file (including its title
and icon sectors), used to execute the file in this region, mapped to continous
addresses at 2000000h and up.<br/>

#### 08000000h - FLASH2 - Flash ROM (128K) (physical addresses in this region)
This region is used by the BIOS when reading the memory card directory (and
when writing data to the FLASH memory). The banking granularity is 2000h bytes
(one memory card block), that means that the hardware cannot map Replacement
Sectors which may be specified in the for Broken Sector List.<br/>

#### 04000000h - BIOS ROM (16K) - Kernel and GUI
```
  4000000h 1E00h Begin of Kernel (usually 1E00h bytes)
  4000014h 4     BCD Date in YYYYMMDDh format (19981023h for ALL versions)
  4001DFCh 4     Core Kernel Version  (usually "C061" or "C110")
  4001E00h 2200h Begin of GUI (usually 2200h bytes)
  4003FFCh 4     Japanese GUI Version (usually "J061" or "J110")
```
The "110" version does contain some patches, but does preserve same function
addresses as the "061" version, still it'd be no good to expect the BIOS to
contain any code/data at fixed locations (except maybe the GUI version string).
Kernel functions can be accessed via SWI Opcodes, and, from the PSX-side, via
BU Commands.<br/>

#### Bus-Width Restrictions
FLASH and BIOS ROM seem to be allowed to be read only in 16bit and 32bit units,
not in 8bit units? Similar restrictions might apply for some I/O ports...? RAM
can be freely read/written in 8bit, 16bit, and 32bit units.<br/>

#### Waitstates
Unknown if and how many waitstates are applied to the different memory regions.
The F\_WAIT1 and F\_WAIT2 registers seem to be somehow waitstate related. FLASH
memory does probably have a 16bit bus, so 32bit data/opcode fetches might be
slower then 16bit reads...? Similar delays might happen for other memory and
I/O regions...?<br/>



##   Pocketstation IO Video and Audio
#### 0D000000h - LCD\_MODE - LCD control word (R/W)
```
  0-2  Draw mode; seems to turn off bits of the screen;
         0: All 32 rows on      ;\
         1: First 8 rows on     ;
         2: Second 8 rows on    ;
         3: Third 8 rows on     ; (these are not necessarily all correct?)
         4: Fourth 8 rows on    ;
         5: First 16 rows on    ;
         6: Middle 16 rows on   ;
         7: Bottom 16 rows on   ;/
  3    CPEN      (0=Does some weird fade out of the screen, 1=Normal)
  4-5  Refresh rate
         0: Makes a single blue (yes, blue, yes, on a black/white display)
            line appear at the top or middle of the screen - don't use!
         1: 64Hz? (might be 32Hz too, like 2)
         2: 32Hz
         3: 16Hz (results in less intensity on black pixels)
  6    Display active                (0=Off, 1=On)
  7    Rotate display by 180 degrees (0=For Handheld Mode, 1=For Docked Mode)
  8-31 Unknown (should be zero)
```
Software should usually set LCD\_MODE.7 equal to INT\_INPUT.Bit11 (docking flag).
In handheld mode, the button-side is facing towards the player, whilst in
Docked mode (when the Pocketstation is inserted into the PSX controller port),
the button-side is facing towards the PSX, so the screen coordinates become
vice-versa, which can be "undone" by the Rotation flag.<br/>

#### 0D000004h - LCD\_CAL - LCD Calibration (maybe contrast or so?)
Upon the reset, the kernel sets LCD\_CAL = F\_CAL AND 0000003Fh. Aside from that,
it doesn't use LCD\_CAL.<br/>

#### 0D000100h..D00017Fh - LCD\_VRAM - 32x32 pixels, 1bit color depth (R/W)
This region consists of 32 words (32bit values),<br/>
```
  [D000100h]=Top, through [D00017Ch]=Bottom-most scanline
```
The separate scanlines consist of 32bit each,<br/>
```
  Bit0=Left, through Bit31=Right-most Pixel (0=White, 1=Black)
```
That [D000100h].Bit0=Upper-left arrangement applies if the Rotate bit in
LCD\_MODE.7 is set up in the conventional way, if it is set the opposite way,
then it becomes [D00017Ch].Bit31=Upper-left.<br/>
The LCD\_VRAM area is reportedly mirrored to whatever locations?<br/>

#### 0D800010h - DAC\_CTRL - Audio Control (R/W)
```
  0     Audio Enable enable    (0=Off, 1=On)
  1-31  Unknown, usually zero
```
Note: Aside from the bit in DAC\_CTRL, audio must be also enabled/disabled via
IOP\_STOP/IOP\_START bit5. Unknown if/which different purposes that bits have.<br/>

#### 0D800014h - DAC\_DATA - Audio D/A Converter
Unknown how many bits are passed to the D/A converter, probably bit8-15, ie. 8
bits...?<br/>
```
  0-7   Probably unused, usually zero (or fractional part when lowered volume)
  8-15  Signed Audio Outut Level (usually -7Fh..+7Fh) (probably -80h works too)
  16-31 Probably unused, usually sign-expanded from bit15
```
The Pocketstation doesn't have any square wave or noise generator (nor a sound
DMA channel). So the output levels must be written to DAC\_DATA by software,
this is usually done via Timer1/IRQ-8 (to reduce CPU load caused by high audio
frequencies, it may be much more recommended to use Timer2/FIQ-13, because the
FIQ handler doesn't need to push r8-r12).<br/>
For example, to produce a 1kHz square wave, the register must be toggled
high/low at 2kHz rate. If desired, multiple channels can be mixed by software.
High frequencies and multiple voices may require high CPU speed settings, and
thus increase battery consumption (aside from that, battery consumption is
probably increased anyways when the speaker is enabled).<br/>



##   Pocketstation IO Interrupts and Buttons
#### 0A000004h - INT\_INPUT - Raw Interrupt Signal Levels (R)
```
  Bit   Type    Meaning
  0     IRQ     Button Fire     (0=Released, 1=Pressed)
  1     IRQ     Button Right    (0=Released, 1=Pressed)
  2     IRQ     Button Left     (0=Released, 1=Pressed)
  3     IRQ     Button Down     (0=Released, 1=Pressed)
  4     IRQ     Button Up       (0=Released, 1=Pressed)
  5     ?       Unknown?        (?)
  6     FIQ (!) COM              ;for the COM_registers?      (via /SEL Pin?)
  7     IRQ     Timer 0
  8     IRQ     Timer 1
  9     IRQ     RTC (square wave) (usually 1Hz) (when RTC paused: 4096Hz)
  10    IRQ     Battery Low     (0=Normal, 1=Battery Low)
  11    IRQ     Docked ("IOP")  (0=Undocked, 1=Docked to PSX) (via VCC Pin?)
  12    IRQ     Infrared Rx
  13    FIQ (!) Timer 2
  14-15 N/A     Not used
```
The buttons are usually read directly from this register (rather than being
configured to trigger IRQs) (except in Sleep mode, where the Fire Button IRQ is
usually used to wakeup). Also, bit9-11 are often read from this register.<br/>
The direction keys seem to be separate buttons, ie. unlike as on a joystick or
DPAD, Left/Right (and Up/Down) can be simultaneously pressed...?<br/>

#### 0A000008h - INT\_MASK\_SET - Set Interrupt Mask (W)
#### 0A00000Ch - INT\_MASK\_CLR - Clear Interrupt Mask (W)
#### 0A000008h - INT\_MASK\_READ - Read Interrupt Mask (R)
```
  INT_MASK_SET  Enable Interrupt Flags         (0=No change, 1=Enable)   (W)
  INT_MASK_CLR  Disable Interrupt Flags        (0=No change, 1=Disable)  (W)
  INT_MASK_READ Current Interrupt Enable Flags (0=Disabled, 1=Enabled)   (R)
```
The locations of the separate bits are same as in INT\_INPUT (see there).<br/>

#### 0A000000h - INT\_LATCH - Interrupt Request Flags (R)
#### 0A000010h - INT\_ACK - Acknowledge Interrupts (W)
```
  INT_LATCH Latched Interrupt Requests   (0=None, 1=Interrupt Request)   (R)
  INT_ACK   Clear Interrupt Requests     (0=No change, 1=Acknowledge)    (W)
```
The locations of the separate bits are same as in INT\_INPUT (see there).<br/>
The interrupts seem to be edge-triggered (?), ie. when the corresponding bits
in INT\_INPUT change from 0-to-1. Unknown if the request bits get set when the
corresponding interrupt is disabled in INT\_MASK...?<br/>

ATTENTION: The GUI doesn't acknowledge Fire Button interrupts on wakeup... so,
it seems as if button interrupts are NOT latched... ie. the button "INT\_LATCH"
bits seem to be just an unlatched mirror of the "INT\_INPUT" bits... that might
also apply for some other interrupt...?<br/>
However, after wakeup, the gui does DISABLE the Fire Button interrupt, MAYBE
that does automatically acknowledge it... in that case it might be latched...?<br/>

Reading outside the readable region (that is where exactly?) seems to mirror to
0A000008h. Enabling IRQs for the buttons seems to make it impossible to poll
them... is that really true?<br/>



##   Pocketstation IO Timers and Real-Time Clock
#### Timer and RTC interrupts
```
  INT_INPUT.7     Timer 0 IRQ    ;used as 30Hz frame rate IRQ by GUI
  INT_INPUT.8     Timer 1 IRQ    ;used as Audio square wave IRQ by GUI
  INT_INPUT.13    Timer 2 FIQ (this one via FIQ vector, not IRQ vector)
  INT_INPUT.9     RTC IRQ (usually 1Hz) (or 4096Hz when RTC paused)
```

#### 0A800000h - T0\_RELOAD - Timer 0 Reload Value
#### 0A800010h - T1\_RELOAD - Timer 1 Reload Value
#### 0A800020h - T2\_RELOAD - Timer 2 Reload Value
```
  0-15  Reload Value (when timer becomes less than zero)
```
Writes to this register are ignored if the timer isn't stopped?<br/>

#### 0A800004h - T0\_COUNT - Timer 0 Current value
#### 0A800014h - T1\_COUNT - Timer 1 Current value
#### 0A800024h - T2\_COUNT - Timer 2 Current value
```
  0-15  Current value (decrementing)
```
Timer interrupts: The timers will automatically raise interrupts if they're
enabled, there's no need to set a bit anywhere for IRQs (but you need to enable
the respect interrupts in INT\_MASK).<br/>

#### 0A800008h - T0\_MODE - Timer 0 Control
#### 0A800018h - T1\_MODE - Timer 1 Control
#### 0A800028h - T2\_MODE - Timer 2 Control
```
  0-1  Timer Divider (0=Div2, 1=Div32, 2=Div512, 3=Div2 too)
  2    Timer Enable  (0=Stop, 1=Decrement)
  3-15 Unknown (should be zero)
```
Timers are clocked by the System Clock (usually 4MHz, when CLK\_MODE=7), divided
by the above divider setting. Note that the System Clock changes when changing
the CPU speed via CLK\_MODE, so Timer Divider and/or Timer Reload must be
adjusted accordingly.<br/>

#### 0B800000h - RTC\_MODE - RTC control word
```
  0    Pause RTC (0=Run/1Hz, 1=Pause/4096Hz)
  1-3  Select value to be modified via RTC_ADJUST
  4-31 Not used?
```
The selection bits can be:<br/>
```
  00h = Second        ;\
  01h = Minute        ;
  02h = Hour          ; used in combination with RTC_ADJUST
  03h = Day of Week   ; while RTC is paused
  04h = Day           ;
  05h = Month         ;
  06h = Year          ;/
  07h = Unknown       ;-usually used when RTC isn't paused
```
When paused, the RTC IRQ bit in INT\_INPUT.9 runs at 4096Hz (instead 1Hz).<br/>

#### 0B800004h - RTC\_ADJUST - Modify value (write only)
Writing a value here seems to increment the current selected parameter (by the
RTC control). What is perhaps (?) clear is that you have to wait for the RTC
interrupt signal to go low before writing to this.<br/>

#### 0B800008h - RTC\_TIME - Real-Time Clock Time (read only) (R)
```
  0-7   Seconds     (00h..59h, BCD)
  8-15  Minutes     (00h..59h, BCD)
  16-23 Hours       (00h..23h, BCD)
  24-31 Day of week (1=Sunday, ..., 7=Saturday)
```
Reading RTC\_TIME seems to be somewhat unstable: the BIOS uses a read/retry
loop, until it has read twice the same value (although it does read the whole
32bit at once by a LDR opcode, the data is maybe passed through a 8bit or 16bit
bus; so the LSBs might be a few clock cycles older than the MSBs...?).<br/>

#### 0B80000Ch - RTC\_DATE - Real-Time Clock Date (read only) (R)
```
  0-7   Day     (01h..31h, BCD)
  8-11  Month   (01h..12h, BCD)
  16-23 Year    (00h..99h, BCD)
  24-31 Unknown? (this is NOT used as century)
```
Reading RTC\_DATE seems to require the same read/retry method as RTC\_TIME (see
there). Note: The century is stored in battery-backed RAM (in the reserved
kernel RAM region) rather than in the RTC\_DATE register. The whole date,
including century, can be read via SWI 0Dh, GetBcdDate().<br/>



##   Pocketstation IO Infrared
The BIOS doesn't contain any IR functions (aside from doing some basic
initialization and power-down stuff).<br/>
IR is used in Final Fantasy 8's Chocobo World (press Left/Right in the Map
screen to go to the IR menu), and in Metal Gear Solid Integral (Press Up in the
main screen), and in PDA Remote 1 & 2 (one-directional TV remote control).<br/>

#### 0C800000h - IRDA\_MODE - Controlling the protocol - send/recv, etc. (R/W)
```
  0    Transfer Direction  (0=Receive, 1=Transmit)
  1    Disable IRDA        (0=Enable, 1=Disable)
  2    Unknown (reportedly IR_SEND_READY, uh?)
  3    Unknown (reportedly IR_RECV_READY, uh?)
  4-31 Unknown (should be zero)
```

#### 0C800004h - IRDA\_DATA - Infrared TX Data
```
  0    Transmit Data in Send Direction (0=LED Off, 1=LED On)
  1-31 Unknown (should be zero)
```
Bits are usually encoded as long or short ON pulses, separated by short OFF
pulses. Where long is usually twice as long as short.<br/>

#### 0C80000Ch - IRDA\_MISC
Unknown? Reportedly reserved.<br/>

#### INT\_INPUT.12 - IRQ - Infrared RX Interrupt
Seems to get triggered on raising or falling (?) edges of incoming data. The
interrupt handler seems to read the current counter value from one of the
timers (usually Timer 2, with reload=FFFFh) to determine the length of the
incoming IR pulse.<br/>

#### IR Notes
Mind that IR hardware usually adopts itself to the normal light conditions, so
if it receives an IR signal for a longer period, then it may treat that as the
normal light conditions (ie. as "OFF" state). To avoid that, one would usually
send a group of ON-OFF-ON-OFF pulses, instead of sending a single long ON
pulse:<br/>
```
   ___------------------___  One HIGH bit send as SINGLE-LONG-ON pulse   (BAD)
   ___-_-_-_-_-_-_-_-_-____  One HIGH bit send as MULTIPLE-ON-OFF pulses (OK)
```
that might be maybe done automatically by the hardware...?<br/>

Reportedly, Bit4 of Port 0D80000Ch (IOP\_DATA) is also somewhat IR related...?<br/>



##   Pocketstation IO Memory-Control
#### 06000000h - F\_CTRL
```
  0-31  Unknown
```
Written values are:<br/>
```
  00000000h  Used when disabling all virtual flash banks
  00000001h  Used before setting new virtual bank values
  00000002h  Used after setting virtual bank enable bits
  03h        Replace ROM at 00000000h by RAM (used after reset)
```
The GUI does additionally read from this register (and gets itself trapped in a
bizarre endless loop if bit0 was zero). Unknown if it's possible to re-enable
ROM at location 00000000h by writing any other values to this register?<br/>

#### 06000004h F\_STAT
```
  0-31  Unknown
```
The kernel issues a dummy read from this address (before setting F\_CTRL to
00000001h).<br/>

#### 06000008h F\_BANK\_FLG  ;FLASH virtual bank mapping enable flags (16 bits)(R/W)
```
  0-15   Enable physical banks 0..15 in virtual region (0=Disable, 1=Enable)
  16-31  Unknown (should be zero)
```

#### 06000100h F\_BANK\_VAL  ;FLASH virtual bank mapping addresses (16 words)(R/W)
This region contains 16 words, the first word at 06000100h for physical bank 0,
the last word at 0600013Ch for physical bank 15. Each word is:<br/>
```
  0-3    Virtual bank number
  4-31   Should be 0
```
Unused physical banks are usually mapped to 0Fh (and are additionally disabled
in the F\_BANK\_FLG register).<br/>

#### 0600000Ch F\_WAIT1     ;waitstates...?
```
  0..3   Unknown/not tested
  4      hangs hardware? but that bit is used in some cases!
  5..31  Unknown/not tested
```
Unknown, seems to control some kind of memory waitstates for FLASH (or maybe
RAM or BIOS ROM). Normally it is set to the following values:<br/>
```
  F_WAIT1=00000000h when CPU Speed = 00h..07h
  F_WAIT1=00000010h when CPU Speed = 08h..0Fh
```
Note: The kernels Docking/Undocking IRQ-11 handler does additionally do this:
"F\_WAIT1=max(08h,(CLK\_MODE AND 0Fh))" (that is a bug, what it actually wants to
do is to READ the current F\_WAIT.Bit4 setting).<br/>

#### 06000010h F\_WAIT2     ;waitstates, and FLASH-Write-Control-and-Status...?
```
  0      no effect? but that bit is used in some cases! maybe write-enable?
  1      hangs hardware?
  2      no effect?           READ: indicates 0=write-busy, 1=ready?  (R)
  3      hangs hardware?
  4      makes FLASH slower?
  5      makes WRAM and F_xxx as slow as other memory (0=1 cycle, 1=2 cycles)
  6      hangs hardware? but that bit is used in some cases!
  7      no effect?
  8..31  Unknown/not tested
```
Unknown, seems to control some kind of memory waitstates, maybe for another
memory region than F\_WAIT1, or maybe F\_WAIT2 is for writing, and F\_WAIT1 for
reading or so. Normally it is set to the following values:<br/>
```
  F_WAIT2=00000000h when CPU Speed = 00h..07h  ;\same as F_WAIT1
  F_WAIT2=00000010h when CPU Speed = 08h..0Fh  ;/
```
In SWI 0Fh and SWI 10h it is also set to:<br/>
```
  F_WAIT2=00000021h  ;SWI 10h, FlashWritePhysical(sector,src)
  F_WAIT2=00000041h  ;SWI 0Fh, FlashWriteSerial(serial_number)
```
Before completion, those SWIs do additionally,<br/>
```
  wait until reading returns F_WAIT2.Bit2 = 1
  and then set F_WAIT2=00000000h
```

#### 08002A54h - F\_KEY1 - Flash Unlock Address 1 (W)
#### 080055AAh - F\_KEY2 - Flash Unlock Address 2 (W)
Unlocks FLASH memory for writing. The complete flowchart for writing sector
data (or header values) is:<br/>
```
  if write_sector                               ;\
    F_WAIT2=00000021h                           ; write enable or so
  if write_header                               ;
    F_WAIT2=00000041h                           ;/
  [80055AAh]=FFAAh                              ;\
  [8002A54h]=FF55h                              ; unlock flash
  [80055AAh]=FFA0h                              ;/
  if write_sector                               ;\
    for i=0 to 3Fh                              ;
      [8000000h+sector*80h+i*2]=src[i*2]        ; write data
  if write_header                               ;
    [8000000h]=new F_SN_LO value                ;
    [8000002h]=new F_SN_HI value                ;
    [8000008h]=new F_CAL value                  ;/
  first, wait 4000 clock cycles                 ;\wait
  then, wait until F_WAIT2.Bit2=1               ;/
  F_WAIT2=00000000h                             ;-write disable or so
```
During the write operation one can (probably?) not read data (nor opcodes) from
FLASH memory, so the above code must be executed either in RAM, or in BIOS ROM
(see SWI 03h, SWI 0Fh, SWI 10h).<br/>

#### 06000300h - F\_SN\_LO - Serial Number LSBs
#### 06000302h - F\_SN\_HI - Serial Number MSBs
#### 06000308h - F\_CAL - Calibration value for LCD
```
  0-15  Data
```
This seems to be an additional "header" region of the FLASH memory
(additionally to the 128K of data). The F\_SN registers contain a serial number
or so (purpose unknown, maybe intended as some kind of an "IP" address for more
complex infrared network applications), the two LO/HI registers must be read by
separate 16bit LDRH opcodes (not by a single 32bit LDR opcode). The F\_CAL
register contains a 6bit calibration value for LCD\_CAL (contrast or so?).<br/>
Although only the above 3 halfwords are used by the BIOS, the "header" is
unlike to be 6 bytes in size, probably there are whatever number of additional
"header" locations at 06000300h and up...?<br/>
Note: Metal Gear Solid Integral uses F\_SN as some kind of copy protection (the
game refuses to run and displays "No copy" if F\_SN is different as when the
pocketstation file was initially created).<br/>

#### F\_BANK\_VAL and F\_BANK\_FLG Notes
Observe that the physical\_bank number (p) is used as array index, and that the
virtual bank number (v) is stored in that location, ie. table[p]=v, which is
unlike as one may have expected it (eg. on a 80386 CPU it'd be vice-versa:
table[v]=p).<br/>
Due to the table[p]=v assignment, a physical block cannot be mirrored to
multiple virtual blocks, instead, multiple physical blocks can be mapped to the
same virtual block (unknown what happens in that case, maybe the data becomes
ANDed together).<br/>



##   Pocketstation IO Communication Ports
#### 0C000000h - COM\_MODE - Com Mode
```
  0     Data Output Enable  (0=None/HighZ, 1=Output Data Bits)
  1     /ACK Output Level   (0=None/HighZ, 1=Output LOW)
  2     Unknown (should be set when expecting a NEW command...?)
  3-31  Unknown (should be zero)
```

#### 0C000008h - COM\_DATA - Com RX/TX Data
```
  0-7   Data (Write: to be transmitted to PSX, Read: been received from PSX)
  8-31  Unknown
```

#### 0C000004h - COM\_STAT1 - Com Status Register 1 (Bit1=Error)
```
  0     Unknown
  1     Error flag or so (0=Okay, 1=Error)
  2-31  Unknown
```
Seems to indicate whatever error (maybe /SEL disabled during transfer, or
timeout, or parity error or something else?) in bit1. Meaning of the other bits
is unknown. Aside from checking the error flag, the kernel does issue a dummy
read at the end of each transfer, maybe to acknowledge something, maybe the
hardware simply resets the error bit after reading (although the kernel doesn't
handle the bit like so when receiving the 1st command byte).<br/>
Aside from the above error flag, one should check if INT\_INPUT.11 becomes zero
during transfer (which indicates undocking).<br/>

#### 0C000014h - COM\_STAT2 - Com Status Register 2 (Bit0=Ready)
```
  0     Ready flag (0=Busy, 1=Ready) (when 8bits have been transferred)
  1-31  Unknown
```

#### 0C000010h - COM\_CTRL1 - Com Control Register 1
```
  0     Unknown (should be set AT BEGIN OF A NEW command...?)
  1     Unknown (0=Disable something, 1=Enable something)
  2-31  Unknown (should be zero)
```
Used values are:<br/>
```
  00000000h = unknown?  disable
  00000002h = unknown?  enable
  00000003h = unknown?  at BEGIN of a new command
```
When doing the enable thing, Bit1 should be set to 0-then-1...? Bit0 might
enable the data shift register... and bit1 might be a master enable and master
acknowledge for the COM interrupt... or something else?<br/>

#### 0C000018h - COM\_CTRL2 - Com Control Register 2
```
  0     Unknown (should be set, probably starts or acknowledges something)
  1     Unknown (should be set when expecting a NEW command...?)
  2-31  Unknown (should be zero)
```
Used values are:<br/>
```
  00000001h = unknown?  used before AND after each byte-transfer
  00000003h = unknown?  used after LAST byte of command (and when init/reset)
```
Maybe that two bits acknowledge the ready/error bits?<br/>

#### INT\_INPUT.6  FIQ (!) COM    for the COM\_registers?      (via /SEL Pin?)
```
  (via FIQ vector, not IRQ vector)
```

#### INT\_INPUT.11 IRQ Docked ("IOP")  (0=Undocked, 1=Docked to PSX)
Probably senses the voltage on the cartridge slots VCC Pin. Becomes zero when
Undocked (and probably also when the PSX is switched off).<br/>
The Kernel uses IRQ-11 for BOTH sensing docking and undocking, ie. as if the
IRQ would be triggered on both 0-to-1 and 1-to-0 transistions... though maybe
that feature just relies on switch-bounce. For the same reason (switch bounce),
the IRQ-11 handler performs a delay before it checks the new INT\_INPUT.11
setting (ie. the delay skips the unstable switch bound period, and allows the
signal to stabilize).<br/>

#### IOP\_START/IOP\_STOP.Bit1
The BIOS adjusts this bit somehow in relation to communication. Unknown
when/why/how it must be used. For details on IOP\_START/IOP\_STOP see Power
Control chapter.<br/>

#### Opcode E6000010h (The Undefined Instruction) - Write chr(r0) to TTY
This opcode is used by the SN Systems emulator to write chr(r0) to a TTY style
text window. r0 can be ASCII characters 20h and up, or 0Ah for CRLF. Using that
opcode is a not too good idea because the default BIOS undef instruction
handler simply runs into an endless loop, so games that are using it (eg.
Break-Thru by Jason) won't work on real hardware. That, unless the game would
change the undef instruction vector at [04h] in Kernel RAM, either replacing it
by a MOVS R15,R14 opcode (ignore exception and return to next opcode), or by
adding exception handling that outputs the character via IR or via whatever
cable connection. Observe that an uninitialized FUNC3 accidently destroys
[04h], so first init FUNC3 handler via SWI 17h, before trying to change [04h],
moreover, mind that SWI 05h may reset FUNC3, causing the problem to reappear.<br/>
Altogether, it'd be MUCH more stable to write TTY characters to an unused I/O
port... only problem is that it's still unknown which I/O ports are unused...
ie. which do neither trap data aborts, nor do mirror to existing ports...?<br/>



##   Pocketstation IO Power Control
#### 0B000000h - CLK\_MODE - Clock control (CPU and Timer Speed) (R/W)
```
  0-3  Clock Ratio (01h..08h, see below) (usually 7 = 3.99MHz)    (R/W)
  4    Clock Change State (0=Busy, 1=Ready)                       (Read-only)
  5-15 ?
```
Allows to change the CPU clock (and Timer clock, which is usually one half of
the CPU clock, or less, depending on the Timer Divider). Possible values are:<br/>
```
  00h = hangs hardware    ;-don't use
  01h = 0.063488 MHz      ;\
  02h = 0.126976 MHz      ;
  03h = 0.253952 MHz      ; 31*8000h / 1,2,4,8,16
  04h = 0.507904 MHz      ;
  05h = 1.015808 MHz      ;/
  06h = 1.998848 MHz      ;\
  07h = 3.997696 MHz      ; 61*8000h * 1,2,4
  08h = 7.995392 MHz      ;/
  09h..0Fh = same as 08h  ;-aliases
```
Before changing CLK\_MODE, F\_WAIT1 and F\_WAIT2 should be adjusted accordingly
(see there for details). Note that many memory regions have waitstates, the
full CPU speed can be reached mainly with code/data in WRAM.<br/>
For emulator authors: Note that some Pocketstation software will expect bit 4 of CLK\_MODE to go from 0 to 1 rather than just polling it until it's 1. For this reason, emulating bit 4 as always being 1 can very likely break.<br/>

#### 0B000004h - CLK\_STOP - Clock stop (Sleep Mode)
Stops the CPU until an interrupt occurs. The pocketstation doesn't have a
power-switch nor standby button, the closest thing to switch "power off" is to
enter sleep mode. Software should do that when the user hasn't pressed buttons
for 1-2 seconds (that, only in handheld mode, not when docked to the PSX; where
it's using the PSX power supply instead of the battery).<br/>
```
  0    Stop Clock (1=Stop)
  1-15 ?
```
Wakeup is usually done by IRQ-0 (Fire Button) and IRQ-11 (Docking). If alarm is
enabled, then the GUI also enables IRQ-9 (RTC), and compares RTC\_TIME against
the alarm setting each time when it wakes up.<br/>
Before writing to CLK\_STOP, one should do:<br/>
```
  DAC_CTRL=0                         ;\disable sound
  IOP_STOP=20h                       ;/
  LCD_MODE=0                         ;-disable video
  IRDA=whatever                      ;-disable infrared (if it was used)
  BATT_CTRL=BATT_CTRL AND FFFFFFFCh  ;-do whatever
  INT_MASK_SET=801h                  ;-enable Docking/Fire wakeup interrupts
```
The GUI uses CLK\_STOP only for Standby purposes (not for waiting for its 30Hz
"frame rate" timer 0 interrupt; maybe that isn't possible, ie. probably
CLK\_STOP does completely disable the system clock, and thus does stop
Timer0-2...?)<br/>

#### 0D800000h - IOP\_CTRL - Configures whatever...? (R/W)
```
  0-3  Probably Direction for IOP_DATA bit0..3 (0=Input, 1=Output)
  4-31 Unknown/Unused (seems to be always zero)
```
Unknown. Set to 0000000Fh by BIOS upon reset. Aside from that, the BIOS does
never use that register.<br/>

#### 0D800004h - IOP\_STAT (R) - Read Current bits? -- No, seems to be always 0
#### 0D800004h - IOP\_STOP (W) - Set IOP\_DATA Bits
#### 0D800008h - IOP\_START (W) - Clear IOP\_DATA Bits
These two ports are probably accessing a single register, writing "1" bits to
IOP\_STOP sets bits in that register, and writing "1" bits to IOP\_START clears
bits... or vice-versa...? Writing "0" bits to either port seems to leave that
bits unchanged. The meaning of most bits is still unknown:<br/>
```
  0    Unknown, STARTED by Kernel upon reset
  1    Red LED, Communication related (START=Whatever, STOP=Whatelse) (?)
  2    Unknown, STARTED by Kernel upon reset
  3    Unknown, STARTED by Kernel upon reset
  4    Never STARTED nor STOPPED by BIOS (maybe an INPUT, read via IOP_DATA)
  5    Sound Enable (START=On, STOP=Off)
  6    Unknown, STOPPED by Kernel upon reset
  7-31 Unknown, never STARTED nor STOPPED by BIOS
```
Aside from Bit1, it's probably not neccessary to change the unknown bits...?<br/>
Sound is usually disabled by setting IOP\_STOP=00000020h. IOP\_STAT is rarely
used. Although, one piece of code in the BIOS disables sound by setting
IOP\_STOP=IOP\_STAT OR 00000020h, that is probably nonsense, probably intended to
keep bits stopped if they are already stopped (which would happen anyways),
however, the strange code implies that reading from 0D800004h returns the
current status of the register, and that the bits in that register seem to be
0=Started, and 1=Stopped...?<br/>

#### 0D80000Ch - IOP\_DATA (R)
```
  0    ?
  1    Red LED (0=On, 1=Off)
  2    ?
  3    ?
  4    Seems to be always 1 (maybe Infrared input?)
  5-31 Unknown/Unused (seems to be always zero)
```
Unknown. Not used by the BIOS. Reportedly this register is 0010h if IR
Connection...? This register is read by Rewrite ID, and by Harvest Moon. Maybe
bit4 doesn't mean \<if\> IR connection exist, but rather \<contains\>
the received IR data level...?<br/>

#### 0D800020h - BATT\_CTRL - Battery Monitor Control?
Unknown. Somehow battery saving related. Upon reset, and upon leaving sleep
mode, the BIOS does set BATT\_CTRL=00000000h. Before entering sleep mode, it
does set BATT\_CTRL=BATT\_CTRL AND FFFFFFFCh, whereas, assuming that BATT\_CTRL
was 00000000h, ANDing it with FFFFFFFCh would simply leave it unchanged...
unless the hardware (or maybe a game) sets some bits in BATT\_CTRL to nonzero
values...?<br/>

#### Battery Low Interrupt
```
  INT_INPUT.10    IRQ     Battery Low     (0=Normal, 1=Battery Low)
```
Can be used to sense if the battery is low, if so, one may disable sound output
and/or reduce the CPU speed to increase the remaining battery lifetime. Unknown
how long the battery lasts, and how much the lifetime is affected by audio,
video, infrared, cpu speed, and sleep mode...?<br/>
The pocketstation can be also powered through the VCC pin (ie. when docked to
the PSX, then it's working even if the battery is empty; or even without
battery).<br/>



##   Pocketstation SWI Function Summary
#### SWI Function Summary
BIOS functions can be called via SWI opcodes (from both ARM and THUMB mode) (in
ARM mode, the SWI function number is in the lower 8bit of the 24bit field;
unlike as for example on the GBA, where it'd be in the upper 8bit). Parameters
(if any) are passed in r0,r1,r2. Return value is stored in r0 (all other
registers are left unchanged).<br/>
```
  SWI 00h - Reset()   ;don't use            out: everything destroyed
  SWI 01h - SetCallbacks(index,proc)        out: old proc
  SWI 02h - CustomSwi2(r0..r6,r8..r10)      out: r0
  SWI 03h - FlashWriteVirtual(sector,src)   out: 0=okay, 1=failed
  SWI 04h - SetCpuSpeed(speed)              out: old_speed
  SWI 05h - SenseAutoCom()                  out: garbage
  SWI 06h - GetPtrToComFlags()              out: ptr (usually 0C0h)
  SWI 07h - ChangeAutoDocking(flags.16-18)  out: incoming flags AND 70000h
  SWI 08h - PrepareExecute(flag,dir_index,param)  out: dir_index (new or old)
  SWI 09h - DoExecute(snapshot_saving_flag) out: r0=r0 (failed) or r0=param
  SWI 0Ah - FlashReadSerial()               out: F_SN
  SWI 0Bh - ClearComFlagsBit10()            out: new [ComFlags] (with bit10=0)
  SWI 0Ch - SetBcdDateTime(date,time)       out: garbage (RTC_DATE/10000h)
  SWI 0Dh - GetBcdDate()                    out: date (with century in MSBs)
  SWI 0Eh - GetBcdTime()                    out: time and day-of-week
  SWI 0Fh - FlashWriteSerial(serial_number) out: garbage (r0=0) ;old BIOS only!
  SWI 10h - FlashWritePhysical(sector,src)  out: 0=okay, 1=failed
  SWI 11h - SetComOnOff(flag)               out: garbage retadr to swi handler
  SWI 12h - TestSnapshot(dir_index)         out: 0=normal, 1=MCX1 with 1,0,"SE"
  SWI 13h - GetPtrToAlarmSetting()          out: ptr to alarm_setting
  SWI 14h - GetPtrToPtrToSwiTable()         out: ptr-to-ptr to swi_table
  SWI 15h - MakeAlternateDirIndex(flag,dir_index)  out: alt_dir_index (new/old)
  SWI 16h - GetDirIndex()                   out: dir_index (or alternate)
  SWI 17h - GetPtrToFunc3addr()             out: ptr to func3 address
  SWI 18h - FlashReadWhateverByte(sector)   out: [8000000h+sector*80h+7Eh]
  SWI 19h..FFh - garbage
  SWI 100h..FFFFFFh - mirrors of SWI 00h..FFh
```
The BIOS uses the same memory region for SWI and IRQ stacks, so both may not
occur simultaneously, otherwise one stack would be destroyed by the other
(normally that is no problem; IRQs are automatically disabled by the CPU during
SWI execution, SWIs aren't used from inside of default IRQ handlers, and SWIs
shouldn't be used from inside of hooked IRQ handlers).<br/>



##   Pocketstation SWI Misc Functions
#### SWI 01h - SetCallbacks(index,proc)
```
  r0=0  Set SWI 02h callback               (r1=proc, or r1=0=reset/default)
  r0=1  Set IRQ callback                   (r1=proc, or r1=0=none/default)
  r0=2  Set FIQ callback                   (r1=proc, or r1=0=none/default)
  r0=3  Set Download Notification callback (r1=proc, or r1=0=bugged/default)
```
All callbacks are called via BX opcodes (ie. proc.bit0 can be set for THUMB
code). SetCallbacks returns the old proc value (usually zero). The callbacks
are automatically reset to zero when (re-)starting an executable, or when
returning control to the GUI, so there's no need to restore the values by
software.<br/>

#### IRQ and FIQ Callbacks
Registers r0,r1,r12 are pushed by the kernels FIQ/IRQ handlers (so the
callbacks can use that registers without needing to push them). The FIQ handler
can additionally use r8..r11 without pushing them (the CPU uses a separate set
of r8..r12 registers in FIQ mode, nethertheless, the kernel DOES push r12 in
FIQ mode, without reason). Available stack is 70h bytes for the FIQ callback,
and 64h bytes for the IRQ callback.<br/>
The callbacks don't receive any incoming parameters, and don't need to respond
with a return value. The callback should return to the FIQ/IRQ handler (via
normal BX r14) (ie. it should not try to return to User mode).<br/>
The kernel IRQ handler does (after the IRQ callback) process IRQ-11 (IOP)
(which does mainly handle docking/undocking), and IRQ-9 (RTC) (which increments
the century if the year wrapped from 99h to 00h).<br/>
And the kernel FIQ handler does (before the FIQ callback) process IRQ-6 (COM)
(which does, if ComFlags.Bit9 is set, handle bu\_cmd's) (both IRQs and FIQs are
disabled, and the main program is stopped until the bu\_cmd finishes, or until a
joypad command is identified irrelevant, among others that means that
sound/timer IRQs aren't processed during that time, so audio output may become
distorted when docked).<br/>
When docked, the FIQ callback should consist of only a handful of opcodes, eg.
it may contain a simple noise, square wave generator, or software based sound
"DMA" function, but it should not contain more time-consuming code like sound
envelope processing; otherwise IRQ-6 (COM) cannot be executed fast enough to
handle incoming commands.<br/>

#### SWI 02h - CustomSwi2(r0..r6,r8..r10)      out: r0
Calls the SWI2 callback function (which can be set via SWI 01h). The default
callback address is 00000000h (so, by default, it behaves identically as SWI
00h). Any parameters can be passed in r0..r6 and r8..r10 (the other registers
aren't passed to the callback function). Return value can be stored in r0 (all
other registers are pushed/popped by the swi handler, as usually). Available
space on the swi stack is 38h bytes.<br/>
SWI2 can be useful to execute code in privileged mode (eg. to initialize FIQ
registers r8..r12 for a FIQ based sound engine) (which usually isn't possible
because the main program runs in non-privileged user mode).<br/>

#### SWI 04h - SetCpuSpeed(speed)              out: old\_speed
Changes the CPU speed. The BIOS uses it with values in range 01h..07h. Unknown
if value 00h can be also used? The function also handles values bigger than
07h, of which, some pieces of BIOS code look as if 08h would be the maximum
value...?<br/>
Before setting the new speed, the function sets F\_WAIT1 and F\_WAIT2 to
00000000h (or to 00000010h if speed.bit3=1). After changing the speed (by
writing the parameter to CLK\_MODE) it does wait until the new speed is applied
(by waiting for CLK\_MODE.bit4 to become zero). The function returns the old
value of CLK\_MODE, anded with 0Fh.<br/>



##   Pocketstation SWI Communication Functions
Communication (aka BU Commands, received from the PSX via the memory card slot)
can be handled by the pocketstations kernel even while a game is running.
However, communications are initially disabled when starting a game, so the
game should enable them via SWI 11h, and/or via calling SWI 05h once per frame.<br/>

#### SWI 11h - SetComOnOff(flag)
Can be used to enable/disable communication. When starting an executable,
communication is initially disabled, so it'd be a good idea to enable them
(otherwise the PSX cannot communicate with the Pocketstation while the game is
running).<br/>
When flag=0, disables communication: Intializes the COM\_registers, disables
IRQ-6 (COM), and clears ComFlags.9. When flag=1, enables communication:
Intializes the COM\_registers, enables IRQ-6 (COM), sets ComFlags.9 (when
docked), or clears Sys.Flags.9 (when undocked), and sets FAST cpu\_speed=7 (only
when docked). The function returns garbage (r0=retadr to swi\_handler).<br/>

#### SWI 06h - GetPtrToComFlags()
Returns a pointer to the ComFlags word in RAM, which contains several
communication related flags (which are either modified upon docking/undocking,
or upon receiving certain bu\_cmd's). The ComFlags word consists of the
following bits:<br/>
```
  0-3   Whatever (set/cleared when docked/undocked, and modified by bu_cmd's)
  4-7   Not used (should be zero)
  8     IRQ-11 (IOP) occurred  (set by irq handler, checked/cleared by SWI 05h)
  9     Communication Enabled And Docked (0=No, 1=Yes; prevents DoExecute)
  10    Reject writes to Broken Sector Region (sector 16..55)     (0=No, 1=Yes)
  11    Start file request (set by bu_cmd_59h, processed by GUI, not by Kernel)
  12-15 Not used (should be zero)
  16    Automatically power-down DAC audio on insert/removal      (0=No, 1=Yes)
  17    Automatically power-down IRDA infrared on insert/removal  (0=No, 1=Yes)
  18    Automatically adjust LCD screen rotate on insert/removal  (0=No, 1=Yes)
  19-27 Not used (should be zero)
  28    Indicates if a standard bu_cmd (52h/53h/57h) was received (0=No, 1=Yes)
  29    Set date/time request  (set by bu_cmd FUNC0, processed by BIOS)
  30    Destroy RTC and Start GUI request  (set by bu_cmd_59h, dir_index=FFFEh)
  31    Not used (should be zero)
```
Bit16-18 can be changed via SWI 07h, ChangeAutoDocking(flags). Bit10 can be
cleared by SWI 0Bh, ClearComFlagsBit10().<br/>

#### SWI 07h - ChangeAutoDocking(flags.16-18)
```
  0-15  Not used (should be zero)
  16    Automatically power-down DAC audio on insert/removal     (0=No, 1=Yes)
  17    Automatically power-down IRDA infrared on insert/removal (0=No, 1=Yes)
  18    Automatically adjust LCD screen rotate on insert/removal (0=No, 1=Yes)
  19-31 Not used (should be zero)
```
Copies bit16-18 of the incoming parameter to ComFlags.16-18, specifying how the
kernel IRQ-11 (IOP) handler shall process docking/undocking from the PSX
cartridge slot. The function returns the incoming flags value ANDed with
70000h.<br/>

#### SWI 0Bh - ClearComFlagsBit10()
Resets ComFlags.Bit10, ie. enables bu\_cmd\_57h (write\_sector) to write to the
Broken Sector region in FLASH memory (sector 16..55). SWI 0Bh returns the
current ComFlags value (the new value, with bit10=0).<br/>
Aside from calling SWI 0Bh, ComFlags.10 is also automatically cleared upon
IRQ-10 (IOP) (docking/undocking). ComFlags.10 can get set/cleared by the
Download Notification callback.<br/>

#### SWI 05h - SenseAutoCom()
Checks if docking/undocking has occurred (by examining ComFlags.8, which gets
set by the kernel IRQ-11 (IOP) handler). If that flag was set, then the
function does reset it, and does then reset FUNC3=0000h and [0CAh]=00h (both
only if docked, not when undocked), and, no matter if docked or undocked, it
enables communication; equivalent to SetComOnOff(1); which sets/clears
ComFlags.9. The function returns garbage (r0=whatever).<br/>
The GUI is calling SWI 05h once per frame. The overall purpose is unknown. It's
a good idea to reset FUNC3 and to Enable Communication (although that'd be
required only when docked, not when undocked), but SWI 05h is doing that only
on (un-)docking transitions (not when it was already docked). In general, it'd
make more sense to do proper initializations via SWI 11h and SWI 17h as than
trusting SWI 05h to do the job. The only possibly useful effect is that SWI 05h
does set/clear ComFlags.9 when docked/undocked.<br/>

#### SWI 17h - GetPtrToFunc3addr()
Returns a pointer to a halfword in RAM which contains the FUNC3 address (for
bu\_cmd\_5bh and bu\_cmd\_5ch). The address is only 16bit, originated at 02000000h
in FLASH (ie. it can be only in the first 64K of the file), bit0 can be set for
THUMB code. The default address is zero, which behaves bugged: It accidently
sets [00000004h]=00000000h, ie. replaces the Undefined Instruction exception
vector by a "andeq r0,r0,r0" opcode, due to that NOP-like opcode, any Undefined
Instruction exceptions will run into the SWI vector at [00000008h], and
randomly execute an SWI function; with some bad luck that may execute one of
the FlashWrite functions and destroy the saved files.<br/>
Although setting 0000h acts bugged, one should restore that setting before
returning control to GUI or other executables; otherwise the address would
still point to the FUNC3 address of the old unloaded executable, which is worse
than the bugged effect.<br/>
The FUNC3 address is automatically reset to 0000h when (if) SWI 05h
(SenseAutoCom) senses new docking.<br/>

#### Download Notification callback
Can be used to mute sound during communication, see SWI 01h,
SetCallbacks(index,proc), and BU Command 5Dh for details.<br/>



##   Pocketstation SWI Execute Functions
#### SWI 08h - PrepareExecute(flag,dir\_index,param)
dir\_index should be 0=GUI, or 1..15=First block of game. When calling
DoExecute, param is passed to the entrypoint of the game or GUI in r0 register
(see notes on GUI \<param\> values belows). For games, param may be
interpreted in whatever way.<br/>
When flag=0, the function simply returns the old dir\_index value. When flag=1,
the new dir\_index and param values are stored in Kernel RAM (for being used by
DoExecute); the values are stored only if dir\_index=0 (GUI), or if dir\_index
belongs to a file with "SC" and "MCX0" or "MCX1" IDs in it's title sector. If
dir\_index was accepted, then the new dir\_index value is returned, otherwise the
old dir\_index is returned.<br/>

#### GUI \<param\> values - for PrepareExecute(1,0,param)
PrepareExecute(1,0,param) prepares to execute the GUI (rather than a file).
When executing the GUI, \<param\> consists of the following destructive
bits:<br/>
```
  0-7  Command number (see below, MSBs=Primary command, LSBs=another dir_index)
  8    Do not store Alarm setting in Kernel RAM (0=Normal, 1=Don't store)
  9-31 Not used (should be zero)
```
The command numbers can be:<br/>
```
  Command 0xh --> Erase RTC time/date
  Command 1xh --> Enter GUI Time Screen with speaker symbol
  Command 20h --> Enter GUI Time Screen with alarm symbol
  Command 2xh --> Prompt for new Date/Time, then start dir_index (x)
  Command 3xh --> Enter GUI File Selection Screen, with dir_index (x) selected
  Command xxh --> Erase RTC time/date (same as Command 0xh)
```
For Command 2xh and 3xh, the lower 4bit of the command (x) must be a valid
dir\_index of the 1st block of a pocketstation executable, otherwise the BIOS
erases the RTC time/date. Bit8 is just a "funny" nag feature, allowing the user
to change the alarm setting, but with the changes being ignored (bit8 can be
actually useful in BU Command 59h, after FUNC2 was used for changing alarm).<br/>

#### SWI 09h - DoExecute(), or DoExecute(snapshot\_saving\_flag) for MCX1
Allows to return control to the GUI (when dir\_index=0), or to start an
executable (when dir\_index=1..15). Prior to calling DoExecute, parameters
should be set via PrepareExecute(1,dir\_index,param), when not doing that,
DoExecute would simply restart the current executable (which may be a desired
effect in some cases).<br/>
The "snapshot\_saving\_flag" can be ommited for normal (MCX0) files, that
parameter is used only for special (MCX1) files (see Snapshot Notes for
details).<br/>
Caution: DoExecute fails (and returns r0=unchanged) when ComFlags.9=1 (which
indicates that communications are enabled, and that the Pocketstation is
believed to be docked to the PSX). ComFlags.9 can be forcefully cleared by
calling SetComOnOff(0), or it can be updated according to the current
docking-state by calling SetComOnOff(1) or SenseAutoCom().<br/>

#### SWI 16h - GetDirIndex()
Returns the dir\_index for the currently executed file. If that value is zero,
ie. if there is no file executed, ie. if the function is called by the GUI,
then it does instead return the "alternate" dir\_index (as set via SWI 15h).<br/>

#### SWI 15h - MakeAlternateDirIndex(flag,dir\_index)  out: alt\_dir\_index (new/old)
Applies the specified dir\_index as "alternate" dir\_index (for being retrieved
via SWI 16h for whatever purpose). The dir\_index is applied only when flag=1,
and only if dir\_index is 0=none, or if it is equal to the dir\_index of the
currently executed file (ie. attempts to make other files being the "alternate"
one are rejected). If successful, the new dir\_index is returned, otherwise the
old dir\_index is returned (eg. if flag=0, or if the index was rejected).<br/>

#### SWI 12h - TestSnapshot(dir\_index)
Tests if the specified file contains a load-able snapshot, ie. if it does have
the "SC" and "MCX1" IDs in the title sector, and the 01h,00h,"SE" ID in the
snapshot header. If so, it returns r0=1, and otherwise returns r0=0.<br/>

#### Snapshot Notes (MCX1 Files)
Snapshots are somewhat automatically loaded/saved when calling DoExecute:<br/>
If the old file (the currently executed file) contains "SC" AND "MCX1" IDs in
the title sector, then the User Mode CPU registers and User RAM at 200h..7FFh
are automatically saved in the files snapshot region in FLASH memory, with the
snapshot\_saving\_flag being applied as bit0 of the 0xh,00h,"SE" ID of the
snapshot header).<br/>
If the new file (specified in dir\_index) contains load-able snapshot data (ie.
if it has "SC" and "MCX1" IDs in title sector, and 01h,00h,"SE" ID in the
snapshot region), then the BIOS starts the saved snapshot data (instead of
restarting the executable at its entrypoint). Not too sure if that feature is
really working... the snapshot loader seems to load User RAM from the wrong
sectors... and it seems to jump directly to User Mode return address... without
removing registers that are still stored on SWI stack... causing the SWI stack
to underflow after loading one or two snapshots...?<br/>



##   Pocketstation SWI Date/Time/Alarm Functions
#### SWI 0Ch - SetBcdDateTime(date,time)
Sets the time and date, the parameters are having the same format as SWI 0Dh
and SWI 0Eh return values (see there). The SWI 0Ch return value contains only
garbage (r0=RTC\_DATE/10000h).<br/>

#### SWI 0Dh - GetBcdDate()
```
  0-7   Day     (01h..31h, BCD)
  8-11  Month   (01h..12h, BCD)
  16-31 Year    (0000h..9999h, BCD)
```
Returns the current date, the lower 24bit are read from RTC\_DATE, the century
in upper 8bit is read from Kernel RAM.<br/>

#### SWI 0Eh - GetBcdTime()
```
  0-7   Seconds     (00h..59h, BCD)
  8-15  Minutes     (00h..59h, BCD)
  16-23 Hours       (00h..23h, BCD)
  24-31 Day of week (1=Sunday, ..., 7=Saturday)
```
Returns the current time and day of week, read from RTC\_TIME.<br/>

#### SWI 13h - GetPtrToAlarmSetting()
Returns a pointer to a 64bit value in Kernel RAM, the upper word (Bit32-63)
isn't actually used by the BIOS, except that, the bu\_cmd FUNC3 does transfer
the whole 64bits. The meaning of the separate bits is:<br/>
```
  0-7   Alarm Minute    (00h..59h, BCD)
  8-15  Alarm Hour      (00h..23h, BCD)
  16    Alarm Enable    (0=Off, 1=On)
  17    Button Lock     (0=Normal, 1=Lock) (pressing all 5 buttons in GUI)
  18-19 Volume Shift    (0=Normal/Loud, 1=Medium/Div4, 2=Mute/Off)
  20-22 Not used        (should be zero)
  23    RTC Initialized (0=Not yet, 1=Yes, was initialized from within GUI)
  24-31 Not used        (should be zero)
  32-63 Pointer to 8x8 BIOS Charset (characters "0"..."9" plus strange symbols)
```
The RTC hardware doesn't have a hardware-based alarm feature, instead, the
alarm values must be compared with the current time by software. Alarm is
handled only by the GUI portion of the BIOS. The Kernel doesn't do any alarm
handling, so alarm won't occur while a game is executed (unless the game
contains code that handles alarm).<br/>
Games are usually using only the lower 16bit of the charset address, ORed with
04000000h (although the full 32bit is stored in RAM).<br/>
```
  CHR(00h..09h) = Digits "0..9"
  CHR(0Ah) = Space " "
  CHR(0Bh) = Colon ":"
  CHR(0Ch) = Button Lock (used by Final Fantasy 8's Chocobo World)
  CHR(0Dh) = Speaker Medium; or loud if followed by chr(0Eh)
  CHR(0Eh) = Speaker Loud; to be appended to chr(0Dh)
  CHR(0Fh) = Speaker Off
  CHR(10h) = Battery Low (used by PocketMuuMuu's Cars)
  CHR(11h) = Alarm Off
  CHR(12h) = Alarm On
  CHR(13h) = Memory Card symbol
```



##   Pocketstation SWI Flash Functions
#### SWI 10h - FlashWritePhysical(sector,src)
Writes 80h-bytes at src to the physical sector number (0..3FFh, originated at
08000000h), and does then compare the written data with the source data.
Returns 0=okay, or 1=failed.<br/>

#### SWI 03h - FlashWriteVirtual(sector,src)
The sector number (0..3FFh) is a virtual sector number (originated at
02000000h), the function uses the F\_BANK\_VAL settings to translate it to a
physical sector number, and does then write the 80h-bytes at src to that
location (via the FlashWritePhysical function). Returns 0=okay, or 1=failed (if
the write failed, or if the sector number exceeded the filesize aka the
virtually mapped memory region).<br/>

#### SWI 0Ah - FlashReadSerial()
Returns the 32bit value from the two 16bit F\_SN registers (see F\_SN for
details).<br/>

#### SWI 0Fh - FlashWriteSerial(serial\_number)    ;old BIOS only!
Changes the 32bit F\_SN value in the "header" region of the FLASH memory. The
function also rewrites the F\_CAL value (but it simply rewrites the old value,
so it's left unchanged). The function isn't used by the BIOS, no idea if it is
used by any games. No return value (always returns r0=0).<br/>
This function is supported by the old "061" version BIOS only (the function is
padded with jump opcodes which hang the CPU in endless loops on newer "110"
version).<br/>

#### SWI 18h - FlashReadWhateverByte(sector)
Returns [8000000h+sector\*80h+7Eh] AND 00FFh. Purpose is totally unknown... the
actual FLASH memory doesn't contain any relevant information at that locations
(eg. the in the directory sectors, that byte is unused, usually zero)... and,
reading some kind of status or manufacturer information would first require to
command the hardware to output that info...?<br/>



##   Pocketstation SWI Useless Functions
#### SWI 00h - Reset()   ;don't use, destroys RTC settings
Reboots the pocketstation, similar as when pressing the Reset button. Don't
use! The BIOS bootcode does (without any good reason) reset the RTC registers
and alarm/century settings in RAM to Time 00:00:00, Date 01 Jan 1999, and Alarm
00:00 disabled, so, after reset, the user would need to re-enter these values.<br/>
Aside from the annoying destroyed RTC settings, the function is rather
unstable: it does jump to address 00000000h in RAM, which should usually
redirect to 04000000h in ROM, however, most pocketstation games are programmed
in C language, where "pointer" is usually pronounced "pointer?" without much
understanding of whether/why/how to initialize that "strange things", so
there's a good probability that one of the recently executed games has
accidently destroyed the reset vector at [00000000h] in battery-backed RAM.<br/>

#### SWI 14h - GetPtrToPtrToSwiTable()
Returns a pointer to a word in RAM, which contains another pointer which
usually points to SWI table in ROM. Changing that word could be (not very)
useful for setting up a custom SWI table in FLASH or in RAM. When doing that,
one must restore the original setting before returning control to the GUI or to
another executable (the setting isn't automatically restored).<br/>



##   Pocketstation BU Command Summary
The Pocketstation supports the standard Memory Card commands (Read Sector,
Write Sector, Get Info), plus a couple of special commands.<br/>

#### BU Command Summary
```
  50h  Change a FUNC 03h related value or so
  51h  N/A
  52h  Standard Read Sector command
  53h  Standard Get ID command
  54h  N/A
  55h  N/A
  56h  N/A
  57h  Standard Write Sector command
  58h  Get an ID or Version value or so
  59h  Prepare File Execution with Dir_index, and Parameter
  5Ah  Get Dir_index, ComFlags, F_SN, Date, and Time
  5Bh  Execute Function and transfer data from Pocketstation to PSX
  5Ch  Execute Function and transfer data from PSX to Pocketstation
  5Dh  Execute Custom Download Notification Function   ;via SWI 01h with r0=3
  5Eh  Get-and-Send ComFlags.bit1,3,2
  5Fh  Get-and-Send ComFlags.bit0
```
Commands 5Bh and 5Ch can use the following functions:<br/>
```
  FUNC 00h - Get or Set Date/Time
  FUNC 01h - Get or Set Memory Block
  FUNC 02h - Get or Set Alarm/Flags
  FUNC 03h - Custom Function 3              ;via SWI 17h, GetPtrToFunc3addr()
  FUNC 80h..FFh - Custom Functions 80h..FFh ;via Function Table in File Header
```



##   Pocketstation BU Standard Memory Card Commands
For general info on the three standard memory card commands (52h, 53h, 57h),
and for info on the FLAG response value, see:<br/>
[Memory Card Read/Write Commands](controllersandmemorycards.md#memory-card-readwrite-commands)<br/>

#### BU Command 52h (Read Sector)
Works much as on normal memory cards, except that, on the Pocketstation, the
Read Sector command return 00h as dummy values; instead of the "(pre)" dummies
that occur on normal memory cards.<br/>
The Read Sector command does reproduce the strange delay (that occurs between
5Ch and 5Dh bytes), similar as on normal original Sony memory cards, maybe
original cards did (maybe) actually DO something during that delay period, the
pocketstation BIOS simply blows up time in a wait loop (maybe for compatibility
with original cards).<br/>

#### BU Command 53h (Get ID)
The Get ID command (53h) returns exactly the same values as normal original
Sony memory cards.<br/>

#### BU Command 57h (Write Sector)
The Write Sector command has two new error codes (additonally to the normal
47h="G"=Good, 4Eh="N"=BadChecksum, FFh=BadSector responses). The new error
codes are (see below for details):<br/>
```
  FDh Reject write to Directory Entries of currently executed file
  FEh Reject write to write-protected Broken Sector region (sector 16..55)
```
And, like Read Sector, it returns 00h instead of "(pre)" as dummy values.<br/>

#### Write Error Code FDh (Directory Entries of currently executed file)
The FDh error code is intended to prevent the PSX bootmenu (or other PSX games)
to delete the currently executed file (which would crash the pocketstation -
once when the deleted region gets overwritten by a new file), because the PSX
bootmenu and normal PSX games do not recognize the new FDh error code the
pocketstation does additionally set FLAG.3 (new card), which should be
understood by all PSX programs.<br/>
The FDh error code occurs only on directory sectors of the file (not on its
data blocks). However, other PSX games should never modify files that belong to
other games (so there should be no compatibility problem with other PSX
programs that aren't aware of the file being containing currently executed
code).<br/>
However, the game that has created the executable pocketstation file must be
aware of that situation. If the file is broken into a Pocketstation Executable
region and a PSX Gameposition region, then it may modify the Gameposition stuff
even while the Executable is running. If the PSX want to overwrite the
executable then it must first ensure that it isn't executed (eg. by retrieving
the dir\_index of the currently executed file via BU Command 5Ah, and comparing
it against the first block number in the files FCB at the PSX side; for file
handle "fd", the first block is found at "[104h]+fd\*2Ch+24h" in PSX memory).<br/>

#### Write Error Code FEh (write-protected Broken Sector region, sector 16..55)
The write-protection is enabled by ComFlags.bit10 (which can be set/cleared via
BU Command 5Dh). That bit should be set before writing Pocketstation
excecutables (the Virtual Memory banking granularity is 2000h bytes, which
allows to map whole blocks only, but cannot map single sectors, which would be
required for files with broken sector replacements).<br/>
Unlike Error FDh, this error code doesn't set FLAG.3 for notifying normal PSX
programs about the error (which is no problem since normally Error FEh should
never occur since ComFlags.10 is usually zero). For more info on ComFlags.10,
see SWI 0Bh aka ClearComFlagsBit10(), and BU Command 5Dh.<br/>



##   Pocketstation BU Basic Pocketstation Commands
#### BU Command 50h (Change a FUNC 03h related value or so)
```
  Send Reply Comment
  81h  N/A   Memory Card Access
  50h  FLAG  Send Command 50h
  VAL  00h   Send new [0CAh], receive length of following data (00h)
```
Might be somehow related to FUNC 03h...?<br/>

#### BU Command 58h (Get an ID or Version value or so)
```
  Send Reply Comment
  81h  N/A   Memory Card Access
  58h  FLAG  Send Command 58h
  (0)  02h   Send dummy/zero, receive length of following data (02h)
  (0)  01h   Send dummy/zero, receive whatever value           (01h)
  (0)  01h   Send dummy/zero, receive another value            (01h)
```

#### BU Command 59h (Prepare File Execution with Dir\_index, and Parameter)
```
  Send Reply Comment
  81h  N/A   Memory Card Access
  59h  FLAG  Send Command 59h
  (0)  06h   Send dummy/zero, receive length of following data (06h)
  NEW  OLD   Send new dir_index.8-15, receive old dir_index.8-15
  NEW  OLD   Send new dir_index.0-7, receive old dir_index.0-7
  PAR  (0)   Send exec_parameter.0-7, receive dummy/zero
  PAR  (0)   Send exec_parameter.8-15, receive dummy/zero
  PAR  (0)   Send exec_parameter.16-23, receive dummy/zero
  PAR  (0)   Send exec_parameter.24-31, receive dummy/zero
```
The new dir\_index can be the following:<br/>
```
  0000h..000Fh --> Request to Start GUI or File (with above parameter bits)
  0010h..FFFDh --> Not used, acts same as FFFFh (see below)
  FFFEh --> Request to Destroy RTC and Start GUI (with parameter 00000000h)
  FFFFh --> Do nothing (transfer all bytes, but don't store the new values)
```
Upon dir\_index=0000h (Start GUI) or 0001..000Fh (start file), a request flag in
ComFlags.11 is set, the GUI does handle that request, but the Kernel doesn't
handle it (so it must be handled in the game; ie. check ComFlags.11 in your
mainloop, and call DoExecute when that bit is set, there's no need to call
PrepareExecute, since that was already done by the BU Command).<br/>
Caution: When dir\_index=0000h, then \<param\> should be a value that does
NOT erase the RTC time/date (eg. 10h or 20h) (most other values do erase the
RTC, see SWI 08h for details).<br/>
Upon dir\_index=FFFEh, a similar request flag is set in ComFlags.30, and, the
Kernel (not the GUI) does handle that request in its FIQ handler (however, the
request is: To reset the RTC time/date and to start the GUI with uninitialized
irq/svc stack pointers, so this unpleasant and bugged feature shouldn't ever be
used). Finally, dir\_index=FFFFh allows to read the current dir\_index value
(which could be also read via BU Command 5Ah).<br/>

#### BU Command 5Ah (Get Dir\_index, ComFlags, F\_SN, Date, and Time)
```
  Send Reply Comment
  81h  N/A   Memory Card Access
  5Ah  FLAG  Send Command 5Ah
  (0)  12h   Send dummy/zero, receive length of following data (12h)
  (0)  INDX  Send dummy/zero, receive curr_dir_index.bit8-15   (00h)
  (0)  INDX  Send dummy/zero, receive curr_dir_index.bit0-7    (00h..0Fh)
  (0)  FLG   Send dummy/zero, receive ComFlags.bit0            (00h or 01h)
  (0)  FLG   Send dummy/zero, receive ComFlags.bit1            (00h or 01h)
  (0)  FLG   Send dummy/zero, receive ComFlags.bit3            (00h or 01h)
  (0)  FLG   Send dummy/zero, receive ComFlags.bit2            (00h or 01h)
  (0)  SN    Send dummy/zero, receive F_SN.bit0-7              (whatever)
  (0)  SN    Send dummy/zero, receive F_SN.bit8-15             (whatever)
  (0)  SN    Send dummy/zero, receive F_SN.bit16-23            (whatever)
  (0)  SN    Send dummy/zero, receive F_SN.bit24-31            (whatever)
  (0)  DATE  Send dummy/zero, receive BCD Day                  (01h..31h)
  (0)  DATE  Send dummy/zero, receive BCD Month                (01h..12h)
  (0)  DATE  Send dummy/zero, receive BCD Year                 (00h..99h)
  (0)  DATE  Send dummy/zero, receive BCD Century              (00h..99h)
  (0)  TIME  Send dummy/zero, receive BCD Second               (00h..59h)
  (0)  TIME  Send dummy/zero, receive BCD Minute               (00h..59h)
  (0)  TIME  Send dummy/zero, receive BCD Hour                 (00h..23h)
  (0)  TIME  Send dummy/zero, receive BCD Day of Week          (01h..07h)
```
At midnight, the function may accidently return the date for the old day, and
the time for the new day.<br/>

#### BU Command 5Eh (Get-and-Send ComFlags.bit1,3,2)
```
  Send Reply Comment
  81h  N/A   Memory Card Access
  5Eh  FLAG  Send Command 5Eh
  (0)  03h   Send dummy/zero, receive length of following data (03h)
  NEW  OLD   Send new ComFlags.bit1, receive old ComFlags.bit1 (00h or 01h)
  NEW  OLD   Send new ComFlags.bit3, receive old ComFlags.bit3 (00h or 01h)
  NEW  OLD   Send new ComFlags.bit2, receive old ComFlags.bit2 (00h or 01h)
```

#### BU Command 5Fh (Get-and-Send ComFlags.bit0)
```
  Send Reply Comment
  81h  N/A   Memory Card Access
  5Fh  FLAG  Send Command 5Fh
  (0)  01h   Send dummy/zero, receive length of following data (01h)
  NEW  OLD   Send new ComFlags.bit0, receive old ComFlags.bit0 (00h or 01h)
```



##   Pocketstation BU Custom Pocketstation Commands
#### BU Command 5Bh (Execute Function and transfer data from Pocketstation to PSX)
```
  Send Reply Comment
  81h  N/A   Memory Card Access
  5Bh  FLAG  Send Command 5Bh
  FUNC FFh   Send Function Number, receive FFh (indicating variable length)
  (0)  LEN1  Send dummy/zero, receive length of parameters (depending on FUNC)
  ...  (0)   Send parameters (LEN1 bytes), and receive dummy/zero
   <-------- at this point, the function is executed for the first time
  (0)  LEN2  Send dummy/zero, receive length of data (depending on FUNC)
  (0)  ...   Send dummy/zero, receive data (LEN2 bytes) from pocketstation
  (0)  FFh   Send dummy/zero, receive FFh
   <-------- at this point, the function is executed for the second time
```
See below for more info on the FUNC value and the corresponding functions.<br/>

#### BU Command 5Ch (Execute Function and transfer data from PSX to Pocketstation)
```
  Send Reply Comment
  81h  N/A   Memory Card Access
  5Ch  FLAG  Send Command 5Ch
  FUNC FFh   Send Function Number, receive FFh (indicating variable length)
  (0)  LEN1  Send dummy/zero, receive length of parameters (depending on FUNC)
  ...  (0)   Send parameters (LEN1 bytes), and receive dummy/zero
   <-------- at this point, the function is executed for the first time
  (0)  LEN2  Send dummy/zero, receive length of data (depending on FUNC)
  ...  (0)   Send data (LEN2 bytes) to pocketstation, receive dummy/zero
  (0)  FFh   Send dummy/zero, receive FFh
   <-------- at this point, the function is executed for the second time
```
See below for more info on the FUNC value and the corresponding functions.<br/>

#### BU Command 5Dh (Execute Custom Download Notification Function)
Can be used to notify the GUI (or games that do support this function) about
following "download" operations (or uploads or other BU commands).<br/>
BU commands are handled inside of the kernels FIQ handler, that means both IRQs
and FIQs are disabled during a BU command transmission, so any IRQ or FIQ based
audio frequency generators will freeze during BU commands. To avoid distorted
noise, it's best to disable sound for the duration specified in bit0-7. If the
PSX finishes before the originally specified duration has expired, then it can
resend this command with bit8=1 to notify the pocketstation that the "download"
has completed.<br/>
```
  Send Reply Comment
  81h  N/A   Memory Card Access
  5Dh  FLAG  Send Command 5Dh
  (0)  03h   Send dummy/zero, receive length of following data (03h)
  VAL  (0)   Send receive value.16-23 (whatever), receive dummy/zero
  VAL  (0)   Send receive value.8-15 (download flags), receive dummy/zero
  VAL  (0)   Send receive value.0-7 (download duration), receive dummy/zero
```
The Download Notification callback address can be set via SWI 01h,
SetCallbacks(3,proc), see there for details. At kernel side, the function
execution is like so:<br/>
```
  If value.8-15 = 00h, then ComFlags.bit10=1, else ComFlags.bit10=0.
  If download_callback<>0 then call download_callback with r0=value.0-23.
```
In the GUI, the bu\_cmd\_5dh\_hook/callback handles parameter bits as so (and
games should probably handle that bits in the same fashion, too):<br/>
```
  bit0-7  download duration   (in whatever units... 30Hz, RTC, seconds...?)
  bit8    download finished   (0=no, 1=yes, cancel any old/busy duration)
  bit9-23 not used by gui
```
If PSX games send any of the standard commands (52h,53h,57h) to access the
memory card without using command 5Dh, then GUI automatically sets the duration
to 01h (and pauses sound only for that short duration).<br/>

#### FUNC 00h - Get or Set Date/Time (FUNC0)
LEN1 is 00h (no parameters), and LEN2 is 08h (eight data bytes):<br/>
```
  DATE  Get or Send BCD Day         (01h..31h)
  DATE  Get or Send BCD Month       (01h..12h)
  DATE  Get or Send BCD Year        (00h..99h)
  DATE  Get or Send BCD Century     (00h..99h)
  TIME  Get or Send BCD Second      (00h..59h)
  TIME  Get or Send BCD Minute      (00h..59h)
  TIME  Get or Send BCD Hour        (00h..23h)
  TIME  Get or Send BCD Day of Week (01h..07h)
```
At midnight, the function may accidently return the date for the old day, and
the time for the new day.<br/>

#### FUNC 01h - Get or Set Memory Block (FUNC1)
LEN1 is 05h (five parameters bytes):<br/>
```
  ADDR  Send Pocketstation Memory Address.bit0-7
  ADDR  Send Pocketstation Memory Address.bit8-15
  ADDR  Send Pocketstation Memory Address.bit16-23
  ADDR  Send Pocketstation Memory Address.bit24-31
  LEN2  Send Desired Data Length (00h..80h, automatically clipped to max=80h)
```
LEN2 is variable (using the 5th byte of the above parameters):<br/>
```
  ...   Get or Send LEN2 Data byte(s), max 80h bytes
```
Can be used to write to RAM (and eventually also to I/O ports; when you know
what you are doing). In the read direction it can read almost anything: RAM,
BIOS ROM, I/O Ports, Physical and Virtual FLASH memory. Of which, trying to
read unmapped Virtual FLASH does probably (?) cause a Data Abort exception (and
crash the Pocketstation), so that region may be read only if a file is loaded
(check that dir\_index isn't zero, via BU Command 5Ah, and, take care not to
exceed the filesize of that file).<br/>
BUG: When sending more than 2 data bytes in the PSX-to-Pocketstation direction,
then ADDR must be word-aligned (the BIOS tries to handle odd destination
addresses, but when doing that, it messes up the alignment of another internal
pointer).<br/>

#### FUNC 02h - Get or Set Alarm/Flags (FUNC2)
LEN1 is 00h (no parameters), and LEN2 is 08h (eight data bytes):<br/>
```
  DATA  Get or Send Alarm.bit0-7,   Alarm Minute    (00h..59h, BCD)
  DATA  Get or Send Alarm.bit8-15,  Alarm Hour      (00h..23h, BCD)
  DATA  Get or Send Alarm.bit16-23, Flags, see SWI 13h, GetPtrToAlarmSetting()
  DATA  Get or Send Alarm.bit24-31, Not used (usually 00h)
  DATA  Get or Send Alarm.bit32-39, BIOS Charset Address.0-7
  DATA  Get or Send Alarm.bit40-47, BIOS Charset Address.8-15
  DATA  Get or Send Alarm.bit48-55, BIOS Charset Address.16-23
  DATA  Get or Send Alarm.bit56-63, BIOS Charset Address.24-31
```
Changing the alarm value while the GUI is running works only with some
trickery: For a sinister reason, the GUI copies the alarm setting to User RAM
when it gets started, that copy isn't affected by FUNC2, so the GUI believes
that the old alarm setting does still apply (and writes that old values back to
Kernel RAM when leaving the GUI). The only workaround is:<br/>
Test if the GUI is running, if so, restart it via Command 59h (with
dir\_index=0, and param=0120h or similar, ie. with param.bit8 set), then execute
FUNC2, then restart the GUI again (this time with param.bit8 zero).<br/>

#### FUNC 03h - Custom Function 3 (aka FUNC3)
LEN1 is 04h (fixed) (four parameters bytes):<br/>
```
  VAL   Send Parameter Value.bit0-7
  VAL   Send Parameter Value.bit8-15
  VAL   Send Parameter Value.bit16-23
  VAL   Send Parameter Value.bit24-31
```
LEN2 is variable (depends on the return value of the 1st function call):<br/>
```
  ...   Get or Send LEN2 Data byte(s)
```
The function address can be set via SWI 17h, GetPtrToFunc3addr(), see there for
details.<br/>
Before using FUNC 03h one must somehow ensure that the desired file is loaded
(and that it does have initialized the function address via SWI 17h, otherwise
the pocketstation would crash).<br/>
The FUNC3 address is automatically reset to 0000h when (if) SWI 05h
(SenseAutoCom) senses new docking.<br/>
Note: The POC-XBOO circuit uses FUNC3 to transfer TTY debug messages.<br/>

#### FUNC 80h..FFh - Custom Function 80h..FFh
LEN1 is variable (depends on the LEN1 value in Function Table in File Header):<br/>
```
  ...   Send LEN1 Parameter Value(s), max 80h bytes (destroys Kernel when >80h)
```
LEN2 is variable (depends on the return value of the 1st function call):<br/>
```
  ...   Get or Send LEN2 Data byte(s), max 80h bytes (clipped to max=80h)
```
The function addresses (and LEN1 values) are stored in the Function Table FLASH
memory (see Pocketstation File Header for details).<br/>
```
      ;above LEN1 should be 00h..80h (the parameters are stored
      ;in a 80h-byte buffer in kernel RAM, so len LEN1=81h..FFh would
      ;destroy the kernel RAM that is located after that buffer)
```
Before using FUNC 80h..FFh one must somehow ensure that the desired file is
loaded (ie. that the function table with the desired functions is mapped to
flash memory; otherwise the pocketstation would crash).<br/>

#### First Function Call (Pre-Data)
Incoming parameters on 1st Function Call:<br/>
```
  r0=flags (09h=Pre-Data to PSX, or 0Ah=Pre-Data from PSX)
  r1=pointer to parameter buffer (which contains LEN1 bytes) (in Kernel RAM)
```
Return Value on 1st Function Call:<br/>
```
  r0 = Pointer to 64bit memory location (or r0=00000000h=Failed)
```
That 64bits are:<br/>
```
  0-31    BUF2 address of data buffer (src/dst)
  32-63   LEN2 (00000000h..00000080h) (clipped to max 00000080h if bigger)
```
dst is written in 8bit units<br/>
src is read in 16bit units (and then split to 8bit units)<br/>

#### Second Function Call (Post-Data)
Incoming parameters on 2nd Function Call:<br/>
```
  r0=flags (11h=Post-Data to PSX, 12h=Post-Data from PSX; plus 04h if Bad-Data)
  r1=pointer to data buffer (which contains LEN2 bytes) (BUF2 address)
```
Return Value on 2nd Function Call:<br/>
```
  There's no return value required on 2nd call (although the kernel
  functions seem to return the same stuff as on 1st call).
```

#### Function flags (r0)
For each function, there is only one single function vector which is called for
both To- and From-PSX, and both Pre- and Post-Data, and also on errors. The
function must decipher the flags in r0 to figure out which of that operations
it should handle:<br/>
```
  0    To-PSX   (when used by Command 5Bh)
  1    From-PSX (when used by Command 5Ch)
  2    Error occurred during Data transfer
  3    Pre-Data
  4    Post-Data
  5-31 Not used (zero)
```
There are only six possible flags combinations:<br/>
```
  09h Pre-Data to PSX
  0Ah Pre-Data from PSX
  11h Post-Data to PSX
  12h Post-Data from PSX
  15h Post-Bad-Data to PSX
  16h Post-Bad-Data from PSX
```
The kernel doesn't call FUNC 03h if the Error bit is set (ie. Post-Bad-Data
needs to be handled only by FUNC 80h..FFh, not by FUNC 03h.)<br/>



##   Pocketstation File Header/Icons
#### Pocketstation File Content
Pocketstation files consists of the following elements (in that order):<br/>
```
  PSX Title Sector              ;80h bytes
  PSX Colored Icon(s)           ;(hdr[02h] AND 0Fh)*80h bytes
  Pocketstation Saved Snapshot  ;800h bytes if hdr[52h]="MCX1", else 0 bytes
  Pocketstation Function Table  ;(hdr[57h]*8+7Fh) AND NOT 7Fh bytes
  Pocketstation File Viewer Mono Icon     ;hdr[50h]*80h bytes
  Pocketstation Executable Mono Icon List ;hdr[56h]*8 bytes
  Body (Pocketstation Executable Code/Data, PSX Game Position, Exec-Icons)
```
The Title sector contains some information about the size of the above regions,
but not about their addresses (ie. to find a given region, one must compute the
size of the preceeding regions).<br/>

#### Special "P" Filename in Directory Sector
For pocketstation executables, the 7th byte of the filename must be a "P" (for
other files that location does usually contain a "-", assuming the file uses a
standard filename, eg. "BESLES-12345abcdefgh" for a Sony licensed european
title).<br/>

#### Special Pocketstation Entries in the Title Sector at [50h..5Fh]
```
  50h 2  Number of File Viewer Mono Icon Frames (or 0000h=Use Exec-Icons)
  52h 4  Pocketstation Identifier ("MCX0"=Normal, "MCX1"=With Snapshot)
  56h 1  Number of entries in Executable Mono Icon List (01h..FFh)
  57h 1  Number of BU Command 5Bh/5Ch Get/Set Functions (00h..7Fh, usually 00h)
  58h 4  Reserved (zero)
  5Ch 4  Entrypoint in FLASH1 (ie. Fileoffset plus 02000000h) (bit0=THUMB)
```
In normal PSX files, the region at 50h..5Fh is usually zerofilled. For more
info on the standard entries in the Title Sector (and for info on Directory
Entries), see:<br/>
[Memory Card Data Format](controllersandmemorycards.md#memory-card-data-format)<br/>

#### Snapshot Region (in "MCX1" Files only)
For a load-able snapshot the Snapshot ID must be 01h,00h,"SE", the Kernel uses
snapshots only once (after loading a snapshot, it forcefully changes the ID to
00h,00h,"SE" in FLASH memory).<br/>
```
  000h  r1..r12 (ie. without r0)
  030h  r13_usr (sp_usr)
  034h  r14_usr (lr_usr)
  038h  r15     (pc)
  03Ch  psr_fc
  040h  Snapshot ID (0xh,00h,"SE")
  044h  unused (3Ch bytes)
  200h  Copy of user RAM at 200h..7FFh
```
For MCX1 files, snapshots can be automatically loaded and saved via the SWI
09h, DoExecute function (the snapshot handling seems to be bugged though; see
SWI 09h for details).<br/>

#### Function Table (FUNC 80h..FFh)
The table can contain 00h..7Fh entries, for FUNC 80h..FFh. Each entry occupies
8 bytes:<br/>
```
  00h 4   LEN1 (00000000h..00000080h) (destroys Kernel RAM if bigger)
  04h 4   Function Address (bit0 can be set for THUMB code)
```
If the number of table entries isn't a multiple of 10h, then the table should
be zero-padded to a multiple of 80h bytes (the following File Viewer Mono Icon
data is located on the next higher 80h-byte boundary after the Function Table).<br/>
For details see BU Commands 5Bh and 5Ch.<br/>

#### File Viewer Mono Icon
Animation Length (0001h..any number) (icon frames) is stored in hdr[50h], for
the File Viewer Icon, the Animation Delay is fixed (six 30Hz units per frame).<br/>
The File Viewer Icon is shown in the Directory Viewer (which is activated when
holding the Down-button pressed for some seconds in the GUI screen with the
speaker and memory card symbols, and which shows icons for all files, including
regular PSX game positions, whose colored icons are converted without any
contrast optimizations to unidentify-able dithered monochrome icons). If the
animation length of the File Viewer Icon is 0000h, then the Directory Viewer
does instead display the first Executable Mono Icon.<br/>
Each icon frame is 32x32 pixels with 1bit color depth (32 words, =128 bytes),<br/>
```
  1st word = top-most scanline, 31st word = bottom-most scanline
  bit0 = left-most pixel, bit31 = right-most pixel (0=white, 1=black)
```
A normal icon occupies 80h bytes, animated icons have more than one frame and
do occupy N\*80h bytes.<br/>

#### Executable Mono Icon List
The number of entries in the Executable Mono Icon List is specified in hdr[56h]
(usually 01h). Each entry in the Icon List occupies 8 bytes:<br/>
```
  00h 2  Animation Length (0001h..any number) (icon frames)
  02h 2  Animation Delay (N 30Hz units per icon frame)
  04h 4  Address of icon frame(s) in Virtual FLASH (at 02000000h and up)
```
The icon frame(s) can be anywhere on a word-aligned location in the file Body
(as specified in the above Address entry), the format of the frame(s) is the
same as for File Viewer Mono Icons (see there).<br/>
The Executable Icons are shown in the Executable File Selection Menu (which
occurs when pressing Left/Right buttons in the GUI). Pressing Fire button in
that menu starts the selected executable. If the Icon List has more than 1
entry, then pressing Up/Down buttons moves to the previous/next entry (this
just allows to view the corresponding icons, but doesn't have any other
purpose, namely, the current list index is NOT passed to the game when starting
it).<br/>
The Executable Mono Icon List is usually zero-padded to 80h-bytes size
(although that isn't actually required, the following file Body could start at
any location).<br/>

#### Entrypoint
The whole file (including the header and icons) gets mapped to 02000000h and
up. The entrypoint can be anywhere in the file Body, and it gets called with a
parameter value in r0 (when started by the GUI, that parameter is always zero,
but it may be nonzero when the executable was started by a game, ie. the
\<param\> from SWI 08h, PrepareExecute, or the \<param\> from BU
Command 59h).<br/>
Caution: Games (and GUI) are started with the ARM CPU running in Non-privileged
User Mode (however, there are several ways to hook IRQ/FIQ handlers, and from
there one can switch to Privileged System Mode).<br/>

#### Returning to the GUI
Games should always include a way to return to the GUI (eg. an option in the
game over screen, a key combination, a watchdog timer, and/or the docking
signal) (conventionally, games should prompt Exit/Continue when holding Fire
pressed for 5 seconds), otherwise it wouldn't be possible to start other games
- except by pushing the Reset button (which is no good idea since the bizarre
BIOS reset handler does reset the RTC time for whatever reason).<br/>
The kernel doesn't pass any return address to the entrypoint (neither in R14,
nor on stack). To return control to the GUI, use SWI functions
PrepareExecute(1,0,GetDirIndex()+30h), and then DoExecute(0).<br/>



##   Pocketstation File Images
Pocketstation files are normally stored in standard Memory Card images,<br/>
[Memory Card Images](controllersandmemorycards.md#memory-card-images)<br/>

#### Pocketstation specific files
Aside from that standard formats, there are two Pocketstation specific formats,
the "SC" and "SN" variants. Both contain only the raw file, without any
Directory sectors, and thus not including a "BESLESP12345"-style filename
string. The absence of the filename means that a PSX game couldn't (re-)open
these files via filenames, so they are suitable only for "standalone"
pocketstation games.<br/>

#### Pocketstation .BIN Files ("SC" variant)
Contains the raw Pocketstation Executable (ie. starting with the "SC" bytes in
the title sector, followed by icons, etc.), the filesize should be padded to a
2000h-byte block boundary.<br/>

#### Pocketstation .BIN Files ("SN" variant)
This is a strange incomplete .BIN file variant which starts with a 4-byte ID
("SN",00h,00h), which is directly followed by executable code, without any
title sector, and without any icons.<br/>
```
  It seems as if the file (including the 4-byte ID) is intended to be
  mapped to address 02000000h, and that the entrypoint is fixed at
  02000004h (in ARM state).
  Since the File doesn't have a valid file header with "SC" and "MCXn" IDs,
  it won't be recognized by real hardware, the PSX BIOS would treat it as
  a corrupted/deleted file, the Pocketstation BIOS would treat it as a
  non-executable file.
  So, that fileformat is apparently working only on whatever emulators,
  apparently on the one developed by SN Systems.
  If one should want to use that files on real hardware, one could add
  a 2000h byte stub at the begin of the file; with valid headers, and
  with a small executable that remaps the "SN" stuff to 02000000h via
  the F_BANK_VAL registers.
  Ah, and the "SN" files seem to access RAM at 01000000h and up, unknown
  if RAM is mirrored to that location on real hardware, reportedly that
  region is unused... and doesn't contain RAM...?
    Some games use The Undefined Instruction for TTY Output.
    Most games do strange 8bit writes to LCD_MODE+0 and LCD_MODE+1
    The games usually don't allow to return to the GUI (except by Reset).
```
The filesize is don't care (no padding to block, sector, word, or halfword
boundaries required).<br/>



##   Pocketstation XBOO Cable
This circuit allows to connect a pocketstation to PC parallel port, allowing to
upload executables to real hardware, and also allowing to download TTY debug
messages (particulary useful as the 32x32 pixel LCD screen is way too small to
display any detailed status info).<br/>

#### POC-XBOO Circuit
Use a standard parallel port cable (with 36pin centronics connector or 25pin DB
connector) and then build a small adaptor like this:<br/>
```
  Pin CNTR  DB25          Pocketstation          _______________________
  ACK 10    10  --------- 1 JOYDTA              |       |       |       |
  D0  2     2   --------- 2 JOYCMD              | 9 7 6 | 5 4 3 |  2 1  | CARD
  GND 19-30 18-25 ------- 4 GND                 |_______|_______|_______|
  D1  3     3   --------- 6 /JOYSEL              _______________________
  D2  4     4   --------- 7 JOYCLK              |       |       |       |
  PE  12    12  --------- 9 /JOYACK (/IRQ7)     | 9 8 7 | 6 5 4 | 3 2 1 | PAD
  NC -------------------- 8 /JOYGUN (/IRQ10)     \______|_______|______/
  NC -------------------- 3 7.5V (rumble.supply)
  SUPPLY.5V --|>|---|>|-- 5 3.5V (VCC) (eg. PC's +5V via two 1N4001 diodes)
  SUPPLY.0V ------------- 4 GND (not needed when same as GND on CNTR/DB25)
```
The circuit is same as for "Direct Pad Pro" (but using a memory card connector
instead of joypad connector, and needing +5V from PC power supply instead of
using parallel port D3..D7 as supply). Note: IRQ7 is optional (for faster/early
timeout).<br/>

#### POC-XBOO Upload
The upload function is found in no$gba "Utility" menu. It does upload the
executable and autostart it via standard memory card/pocketstation commands
(ie. it doesn't require any special transmission software installed on the
pocketstation side).<br/>
Notes: Upload is overwriting ALL files on the memory card, and does then
autostart the first file. Upload is done as "read and write only if different",
this provides faster transfers and higher lifetime.<br/>

#### POC-XBOO TTY Debug Messages
TTY output is conventionally done by executing the ARM CPU's Undefined Opcode
with an ASCII character in R0 register (for that purpose, the undef opcode
handler should simply point to a MOVS PC,LR opcode).<br/>
That kind of TTY output works in no$gba's pocketstation emulation. It can be
also used via no$gba's POC-XBOO cable, but requires some small customization in
the executable:<br/>
First of, the executable needs "TTY+" ID in some reserved bytes of the title
sector (telling the xboo uploader to stay in transmission mode and to keep
checking for TTY messages after the actual upload):<br/>
```
  TitleSector[58h] = "TTY+"
```
With that ID, and with the XBOO-hardware being used, the game will be started
with with "TTY+" in R0 (notifying it that the XBOO hardware is present, and
that it needs to install special transmission handlers):<br/>
```
 ;------------------
 .data?
 org  200h
 ...
 tty_bufsiz equ 128  ;max=128=fastest (can be smaller if you are short of RAM)
 func3_info:                                       ;\ ;\
  func3_buf_base     dd 0   ;fixed="func3_buf"     ;  ;  func3_info+00h
  func3_buf_len      dd 0   ;range=0..128          ;/ ;  func3_info+04h
  func3_stack        dd 0                             ;  func3_info+08h
  func3_buffer:      defs tty_bufsiz                  ;/ func3_info+0Ch
 ptr_to_comflags     dd 0
 ...
 .code
 ...
 ;------------------
 tty_wrchr:   ;in: r0=char
  dd      0e6000010h ;=undef opcode            ;-Write chr(r0) to TTY
  bx      lr
 ;------------------
 init_tty:  ;in: r0=param (from entrypoint)
  ldr     r1,=2B595454h ;"TTY+"                ;\check if xboo-cable present
  cmp     r1,r0                                ; (r0=incoming param from
  beq     @@tty_by_xboo_cable                  ;/executable's entrypoint)
 ;- - -
  mov     r1,0                                 ;\dummy und_handler
  ldr     r2,=0e1b0f00eh  ;=movs r15,r14       ; (just return from exception,
  str     r2,[r1,04h]  ;und_handler            ;/for normal cable-less mode)
  b       @@finish
 ;---
 @@tty_by_xboo_cable:
  swi     17h  ;GetPtrToFunc3addr()            ;\
  ldr     r1,=(tty_func3_handler AND 0ffffh)   ; init FUNC3 aka TTY handler
  strh    r1,[r0]                              ;/
  ldr     r1,=func3_info                       ;\
  mov     r0,0                             ;\  ; mark TTY as len=empty
  str     r0,[r1,4]        ;func3_buf_len  ;/  ; and
  add     r0,r1,0ch ;=func3_buffer         ;\  ; init func3 base
  str     r0,[r1,0]        ;func3_buf_base ;/  ;/
  mov     r1,0                                 ;\
  ldr     r2,=0e59ff018h  ;=ldr r15,[pc,NN]    ;
  str     r2,[r1,04h]  ;und_handler            ; special xboo und_handler
  add     r2,=tty_xboo_und_handler             ;
  str     r2,[r1,24h]  ;und_vector             ;/
 @@finish:
  swi     06h ;GetPtrToComFlags()              ;\
  ldr     r1,=ptr_to_comflags                  ; get ptr to ComFlags
  str     r0,[r1]                              ;/
  bx      lr
 ;------------------
 tty_xboo_und_handler:   ;in: r0=char
  ldr     r13,=func3_info ;aka sp_und          ;-base address (in sp_und)
  str     r12,[r13,8] ;func3_stack             ;-push r12
 @@wait_if_buffer_full:                        ;\
  ldr     r12,=ptr_to_comflags                 ; ;\exit if execute file request
  ldr     r12,[r12]  ;ptr to ComFlags          ; ; ComFlg.Bit11 ("bu_cmd_59h"),
  ldr     r12,[r12]  ;read ComFlags            ; ; ie. allow that flag to be
  tst     r12,1 shl 11  ;test bit11            ; ; processed by main program,
  bne     @@exit                               ; ;/without hanging here
  ldrb    r12,[r13,4] ;func3_buf_len           ; wait if buffer full
  cmp     r12,tty_bufsiz                       ; (until drained by FIQ)
  beq     @@wait_if_buffer_full                ;/
  mov     r12,1bh+0c0h  ;mode=und, FIQ/IRQ=off ;\disable FIQ (no COMMUNICATION
  mov     cpsr_ctl,r12                         ;/interrupt during buffer write)
  ldrb    r12,[r13,4]  ;func3_buf_len          ;\
  add     r12,1        ;raise len              ; write char to buffer
  strb    r12,[r13,4]  ;func3_buf_len          ; and raise buffer length
  add     r12,0ch-1    ;=func3_buffer+INDEX    ;
  strb    r0,[r13,r12] ;append char to buf     ;/
 @@exit:
  ldr     r12,[r13,8]  ;func3_stack            ;-pop r12
  movs    r15,r14        ;return from exception (and restore old IRQ/FIQ state)
 ;------------------
 tty_func3_handler:   ;in: r0=flags, r1=ptr
  tst     r0,10h  ;test if PRE/POST data (pre: Z, post: NZ)
 ;ldreq   r1,[r1]   ;read 32bit param (aka the four LEN1 bytes of FUNC3)
  ldr     r0,=func3_info   ;ptr to two 32bit values (FUNC3 return value)
  movne   r1,0                           ;\for POST data: mark buffer empty
  strne   r1,[r0,4] ;func3_buf_len=0     ;/
  bx      lr                             ;-for PRE data: return r0=func3_info
```
Usage: Call "init\_tty" at the executable's entrypoint (with incoming R0 passed
on). Call "tty\_wrchr" to output ASCII characters.<br/>
Note: The TTY messages are supported only in no$gba debug version (not no$gba
gaming version).<br/>
