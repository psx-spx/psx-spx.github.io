#   I/O Map
#### DEV0
```
  1F000000h 80000h           Expansion Region (default 512 Kbytes, max 8 MBytes)
  1F000000h 100h             Expansion ROM Header (IDs and Entrypoints)
```
#### Scratchpad
```
  1F800000h 400h             Scratchpad (1K Fast RAM) (Data Cache mapped to fixed address)
```
#### System Bus Interface
```
  1F801000h 4    DEV0_?      DEV0 (PIO)      Base Address (usually 1F000000h)
  1F801004h 4    DEV8_?      DEV8 (debug)    Base Address (usually 1F802000h)
  1F801008h 4    DEV0_?      DEV0 (PIO)      Delay/Size   (usually 0013243Fh; 512Kbytes 8bit-bus)
  1F80100Ch 4    DEV1_?      DEV1 (debug)    Delay/Size   (usually 00003022h; 1 byte)
  1F801010h 4    DEV2_?      DEV2 (BIOS ROM) Delay/Size   (usually 0013243Fh; 512Kbytes 8bit-bus)
  1F801014h 4    DEV4_?      DEV4 (SPU)      Delay/Size   (usually 200931E1h)
  1F801018h 4    DEV5_?      DEV5 (CD-ROM)   Delay/Size   (usually 00020843h or 00020943h)
  1F80101Ch 4    DEV8_?      DEV8 (debug)    Delay/Size   (usually 00070777h; 128-bytes 8bit-bus)
  1F801020h 4    COM_DELAY   (00031125h or 0000132Ch or 00001325h)
```
#### Peripheral I/O Ports
```
  1F801040h 1/4  SIO0_DR     Joypad/Memory Card Data (R/W)
  1F801044h 4    SIO0_SR     Joypad/Memory Card Status (R)
  1F801048h 2    SIO0_MR     Joypad/Memory Card Mode (R/W)
  1F80104Ah 2    SIO0_CR     Joypad/Memory Card Control (R/W)
  1F80104Eh 2    SIO0_BR     Joypad/Memory Card Baudrate (R/W)
  1F801050h 1/4  SIO1_DR     Serial Port Data (R/W)
  1F801054h 4    SIO1_SR     Serial Port Status (R)
  1F801058h 2    SIO1_MR     Serial Port Mode (R/W)
  1F80105Ah 2    SIO1_CR     Serial Port Control (R/W)
  1F80105Ch 2    SIO1_?      Serial Port Internal Register (R/W)
  1F80105Eh 2    SIO1_BR     Serial Port Baudrate (R/W)
```
#### DRAM Controller
```
  1F801060h 4/2  DRAM_CTRL   (usually 00000B88h; 2MB RAM mirrored in first 8MB)
```
#### Interrupt Control
```
  1F801070h 2    I_STAT      Interrupt status register
  1F801074h 2    I_MASK      Interrupt mask register
```
#### DMA Registers
```
  1F80108xh      D0_*        Channel 0 - MDECin
  1F80109xh      D1_*        Channel 1 - MDECout
  1F8010Axh      D2_*        Channel 2 - GPU (lists + image data)
  1F8010Bxh      D3_*        Channel 3 - CDROM
  1F8010Cxh      D4_*        Channel 4 - SPU
  1F8010Dxh      D5_*        Channel 5 - PIO (Expansion Port)
  1F8010Exh      D6_*        Channel 6 - OTC (reverse clear OT) (GPU related)
  1F8010F0h 4    DPCR        DMA Control register
  1F8010F4h 4    DICR        DMA Interrupt register
  1F8010F8h 4    unknown
  1F8010FCh 4    unknown
```
#### Timers (aka Root counters)
```
  1F801100h 2    T0_COUNT    Timer 0 (dotclock) Current Value (R/W)
  1F801104h 2    T0_MODE     Timer 0 (dotclock) Mode (R/W)
  1F801108h 2    T0_COMP     Timer 0 (dotclock) Target Value (R/W)
  1F801110h 2    T1_COUNT    Timer 1 (hblank)   Current Value (R/W)
  1F801114h 2    T1_MODE     Timer 1 (hblank)   Mode (R/W)
  1F801118h 2    T1_COMP     Timer 1 (hblank)   Target Value (R/W)
  1F801120h 2    T2_COUNT    Timer 2 (sysclock) Current Value (R/W)
  1F801124h 2    T2_MODE     Timer 2 (sysclock) Mode (R/W)
  1F801128h 2    T2_COMP     Timer 2 (sysclock) Target Value (R/W)
```
#### CDROM Registers (Address.Read/Write.Index)
```
  1F801800h.R.*  HSTS        CD Index/Status Register (R)
  1F801801h.R.*  RESULT      CD Response Fifo (R)
  1F801802h.R.*  RDDATA      CD Data Fifo (R)
  1F801803h.R.0  HINTMSK     CD Interrupt Enable Register (R)
  1F801803h.R.1  HINTSTS     CD Interrupt Flag Register (R)

  1F801800h.W.*  ADDRESS     CD Index Register (Bit0-1 W)
  1F801801h.W.0  COMMAND     CD Command Register (W)
  1F801802h.W.0  PARAMETER   CD Parameter Fifo (W)
  1F801803h.W.0  HCHPCTL     CD Request Register (W)
  1F801801h.W.1  WRDATA      CD Sound Map Data (W)
  1F801802h.W.1  HINTMSK     CD Interrupt Enable Register (W)
  1F801803h.W.1  HCLRCTL     CD Interrupt Flag Register (W)
  1F801801h.W.2  CI          CD Sound Map Coding Info (W)
  1F801802h.W.2  ATV0        CD Audio Volume for Left-CD-Out to Left-SPU-Input (W)
  1F801803h.W.2  ATV1        CD Audio Volume for Left-CD-Out to Right-SPU-Input (W)
  1F801801h.W.3  ATV2        CD Audio Volume for Right-CD-Out to Right-SPU-Input (W)
  1F801802h.W.3  ATV3        CD Audio Volume for Right-CD-Out to Left-SPU-Input (W)
  1F801803h.W.3  ADPCTL      CD Audio Volume Apply Changes (by writing bit5=1)
```
#### GPU Registers
```
  1F801810h.W 4  GP0?        Send GP0 Commands/Packets (Rendering and VRAM Access)
  1F801810h.R 4  GP0?        Read responses to GP0(C0h) and GP1(10h) commands
  1F801814h.W 4  GP1?        Send GP1 Commands (Display Control)
  1F801814h.R 4  GPU_STAT    Read GPU Status Register
```
#### MDEC Registers
```
  1F801820h.W 4  MDEC_?      MDEC Command/Parameter Register (W)
  1F801820h.R 4  MDEC_?      MDEC Data/Response Register (R)
  1F801824h.W 4  MDEC_?      MDEC Control/Reset Register (W)
  1F801824h.R 4  MDEC_?      MDEC Status Register (R)
```
#### SPU Voice 0..23 Registers
```
  1F801Cx0h 2    VOLL        Voice 0..23 Volume Left
  1F801Cx2h 2    VOLR        Voice 0..23 Volume Right
  1F801Cx4h 2    PITCH       Voice 0..23 Sample Rate
  1F801Cx6h 2    SSA         Voice 0..23 Sample Start Address
  1F801Cx8h 2    ADSR1       Voice 0..23 ADSR Attack/Decay
  1F801CxAh 2    ADSR2       Voice 0..23 ADSR Sustain/Release
  1F801CxCh 2    ENVX        Voice 0..23 ADSR Current Volume
  1F801CxEh 2    LSAX        Voice 0..23 Loop Start Address
```
#### SPU Control Registers
```
  1F801D80h 2    MVOLL       Main Volume Left
  1F801D82h 2    MVOLR       Main Volume Right
  1F801D84h 2    EVOLL       Reverb Volume Left
  1F801D86h 2    EVOLR       Reverb Volume Right
  1F801D88h 2    KON0        Voice 0..15  Key ON (Start Attack/Decay/Sustain) (W)
  1F801D8Ah 2    KON1        Voice 16..23 Key ON (Start Attack/Decay/Sustain) (W)
  1F801D8Ch 2    KOF0        Voice 0..15  Key OFF (Start Release) (W)
  1F801D8Eh 2    KOF1        Voice 16..23 Key OFF (Start Release) (W)
  1F801D90h 2    PMON0       Voice 0..15  Channel FM (pitch lfo) mode (R/W)
  1F801D92h 2    PMON1       Voice 16..23 Channel FM (pitch lfo) mode (R/W)
  1F801D94h 2    NON0        Voice 0..15  Channel Noise mode (R/W)
  1F801D96h 2    NON1        Voice 16..23 Channel Noise mode (R/W)
  1F801D98h 2    EON0        Voice 0..15  Channel Reverb mode (R/W)
  1F801D9Ah 2    EON1        Voice 16..23 Channel Reverb mode (R/W)
  1F801D9Ch 2    ENDX0       Voice 0..15  Channel ON/OFF (status) (R)
  1F801D9Eh 2    ENDX1       Voice 15..23 Channel ON/OFF (status) (R)
  1F801DA0h 2                Unused? (R) or (W)
  1F801DA2h 2    ESA         Sound RAM Reverb Work Area Start Address
  1F801DA4h 2    IRQA        Sound RAM IRQ Address
  1F801DA6h 2    TSA         Sound RAM Transfer Start Address
  1F801DA8h 2    DATA        Sound RAM Data Write Fifo
  1F801DAAh 2    ATTR        SPU Attribute Register
  1F801DACh 2    RAM_CTRL?   Sound RAM Size Control
  1F801DAEh 2    STATX       SPU Status Register (R)
  1F801DB0h 2    AVOLL       I2SA (CD-ROM) Volume Left
  1F801DB2h 2    AVOLR       I2SA (CD-ROM) Volume Right
  1F801DB4h 2    BVOLL       I2SB (PIO) Volume Left
  1F801DB6h 2    BVOLR       I2SB (PIO) Volume Right
  1F801DB8h 2    MVOLXL      Current Main Volume Left
  1F801DBAh 2    MVOLXR      Current Main Volume Right
  1F801DBCh 4                Unused? (R/W)
```
#### SPU Reverb Configuration Area
```
  1F801DC0h 2    dAPF1       Reverb APF Offset 1
  1F801DC2h 2    dAPF2       Reverb APF Offset 2
  1F801DC4h 2    vIIR        Reverb Reflection Volume 1
  1F801DC6h 2    vCOMB1      Reverb Comb Volume 1
  1F801DC8h 2    vCOMB2      Reverb Comb Volume 2
  1F801DCAh 2    vCOMB3      Reverb Comb Volume 3
  1F801DCCh 2    vCOMB4      Reverb Comb Volume 4
  1F801DCEh 2    vWALL       Reverb Reflection Volume 2
  1F801DD0h 2    vAPF1       Reverb APF Volume 1
  1F801DD2h 2    vAPF2       Reverb APF Volume 2
  1F801DD4h 4    mSAME       Reverb Same Side Reflection Address 1 Left/Right
  1F801DD8h 4    mCOMB1      Reverb Comb Address 1 Left/Right
  1F801DDCh 4    mCOMB2      Reverb Comb Address 2 Left/Right
  1F801DE0h 4    dSAME       Reverb Same Side Reflection Address 2 Left/Right
  1F801DE4h 4    mDIFF       Reverb Different Side Reflection Address 1 Left/Right
  1F801DE8h 4    mCOMB3      Reverb Comb Address 3 Left/Right
  1F801DECh 4    mCOMB4      Reverb Comb Address 4 Left/Right
  1F801DF0h 4    dDIFF       Reverb Different Side Reflection Address 2 Left/Right
  1F801DF4h 4    mAPF1       Reverb APF Address 1 Left/Right
  1F801DF8h 4    mAPF2       Reverb APF Address 2 Left/Right
  1F801DFCh 4    vIN         Reverb Input Volume Left/Right
```
#### SPU Internal Registers
```
  1F801Exxh 2    VOLXL       Voice 0..23 Current Volume Left
  1F801Exxh 2    VOLXR       Voice 0..23 Current Volume Right
  1F801E60h 20h              Unused? (R/W)
  1F801E80h 180h             Unused? (Read: FFh-filled)
```
#### DEV8 (default 128 bytes, max 8 KBytes)
```
  1F802000h 80h              Expansion Region (8bit data bus, crashes on 16bit access?)
```
#### DEV8 - Dual Serial Port (for TTY Debug Terminal)
```
  1F802020h/1st    DUART Mode Register 1.A (R/W)
  1F802020h/2nd    DUART Mode Register 2.A (R/W)
  1F802021h/Read   DUART Status Register A (R)
  1F802021h/Write  DUART Clock Select Register A (W)
  1F802022h/Read   DUART Toggle Baud Rate Generator Test Mode (Read=Strobe)
  1F802022h/Write  DUART Command Register A (W)
  1F802023h/Read   DUART Rx Holding Register A (FIFO) (R)
  1F802023h/Write  DUART Tx Holding Register A (W)
  1F802024h/Read   DUART Input Port Change Register (R)
  1F802024h/Write  DUART Aux. Control Register (W)
  1F802025h/Read   DUART Interrupt Status Register (R)
  1F802025h/Write  DUART Interrupt Mask Register (W)
  1F802026h/Read   DUART Counter/Timer Current Value, Upper/Bit15-8 (R)
  1F802026h/Write  DUART Counter/Timer Reload Value,  Upper/Bit15-8 (W)
  1F802027h/Read   DUART Counter/Timer Current Value, Lower/Bit7-0 (R)
  1F802027h/Write  DUART Counter/Timer Reload Value,  Lower/Bit7-0 (W)
  1F802028h/1st    DUART Mode Register 1.B (R/W)
  1F802028h/2nd    DUART Mode Register 2.B (R/W)
  1F802029h/Read   DUART Status Register B (R)
  1F802029h/Write  DUART Clock Select Register B (W)
  1F80202Ah/Read   DUART Toggle 1X/16X Test Mode (Read=Strobe)
  1F80202Ah/Write  DUART Command Register B (W)
  1F80202Bh/Read   DUART Rx Holding Register B (FIFO) (R)
  1F80202Bh/Write  DUART Tx Holding Register B (W)
  1F80202Ch/None   DUART Reserved Register (neither R nor W)
  1F80202Dh/Read   DUART Input Port (R)
  1F80202Dh/Write  DUART Output Port Configuration Register (W)
  1F80202Eh/Read   DUART Start Counter Command (Read=Strobe)
  1F80202Eh/Write  DUART Set Output Port Bits Command (Set means Out=LOW)
  1F80202Fh/Read   DUART Stop Counter Command (Read=Strobe)
  1F80202Fh/Write  DUART Reset Output Port Bits Command (Reset means Out=HIGH)
```
#### DEV8 - Int/Dip/Post
```
  1F802000h 1   DTL-H2000: ATCONS STAT (R)
  1F802002h 1   DTL-H2000: ATCONS DATA (R and W)
  1F802004h 2   DTL-H2000: ATCONS DATA16 (R and W) (DECI command/bulk data words)
  1F802030h 1/4 DTL-H2000: Secondary IRQ10 Flags
  1F802032h 1   DTL-H2000: Whatever IRQ Control ?
  1F802040h 1   DTL-H2000: Bootmode "Dip switches" (R)
  1F802041h 1   PSX: POST (external 7 segment display, indicate BIOS boot status)
  1F802042h 1   DTL-H2000: POST/LED (similar to POST) (other addr, 2-digit wide)
  1F802070h 1   PS2: POST2 (similar to POST, but PS2 BIOS uses this address)
```
#### DEV8 - Nocash Emulation Expansion
```
  1F802060h Emu-Expansion ID1 "E" (R)
  1F802061h Emu-Expansion ID2 "X" (R)
  1F802062h Emu-Expansion ID3 "P" (R)
  1F802063h Emu-Expansion Version (01h) (R)
  1F802064h Emu-Expansion Enable1 "O" (R/W)
  1F802065h Emu-Expansion Enable2 "N" (R/W)
  1F802066h Emu-Expansion Halt (R)
  1F802067h Emu-Expansion Turbo Mode Flags (R/W)
```
#### DEV8 - PCSX-Redux Emulation Expansion
```
  1F802080h 4 Redux-Expansion ID "PCSX" (R)
  1F802080h 1 Redux-Expansion Console putchar (W)
  1F802081h 1 Redux-Expansion Debug break (W)
  1F802082h 1 Redux-Expansion Exit code (W)
  1F802084h 4 Redux-Expansion Notification message pointer (W)
```
#### DEV1 (default 1 byte, max 2 MBytes)
```
  1FA00000h - Not used by BIOS or any PSX games
  1FA00000h - POST3 (similar to POST, but PS2 BIOS uses this address)
```
#### BIOS Region (default 512 Kbytes, max 4 MBytes)
```
  1FC00000h 80000h           BIOS ROM (512Kbytes) (Reset Entrypoint at BFC00000h)
```
#### CW33300 CPU Configuration
```
  FFFE0130h 4    BCC         BIU/Cache Control
```

#### Coprocessor Registers
```
  COP0 System Control Coprocessor           - 32 registers (not all used)
  COP1 N/A
  COP2 Geometry Transformation Engine (GTE) - 64 registers (most are used)
  COP3 N/A
```
