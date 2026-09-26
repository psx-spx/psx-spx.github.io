#   BIOS Memory Map
#### BIOS ROM Map (512Kbytes)
```
  BFC00000h Kernel Part 1  (code/data executed in uncached ROM)
  BFC10000h Kernel Part 2  (code/data relocated to cached RAM)
  BFC18000h Intro/Bootmenu (code/data decompressed and relocated to RAM)
  BFC64000h Character Sets
```

#### BIOS ROM Header/Footer
```
  BFC00100h Kernel BCD date  (YYYYMMDDh)
  BFC00104h Console Type     (see Port 1F802030h, Secondary IRQ10 Controller)
  BFC00108h Kernel Maker/Version Strings (separated by one or more 00h bytes)
  BFC7FF32h GUI Version/Copyright Strings (if any) (separated by one 00h byte)
```

#### BIOS RAM Map (1st 64Kbytes of RAM) (fixed addresses mainly in 1st 500h bytes)
```
  00000000h 10h    Garbage Area (see notes below)
  00000010h 30h    Unused/reserved
  00000040h 20h    COP0 debug-break vector (not used by Kernel) (in KSEG0)
  00000060h 4      RAM Size (in megabytes) (2 or 8)
  00000064h 4      Unknown (set to 00000000h)
  00000068h 4      Unknown (set to 000000FFh)
  0000006Ch 14h    Unused/reserved
  00000080h 10h    Exception vector (actually in KSEG0, ie. at 80000080h)
  00000090h 10h    Unused/reserved
  000000A0h 10h    A(nnh) Function Vector
  000000B0h 10h    B(nnh) Function Vector
  000000C0h 10h    C(nnh) Function Vector
  000000D0h 30h    Unused/reserved
  00000100h 58h    Table of Tables (BIOS Control Blocks) (see below)
  00000158h 28h    Unused/reserved
  00000180h 80h    Command line argument from SYSTEM.CNF; BOOT = fname argument
  00000200h 300h   A(nnh) Jump Table
  00000500h ...    Kernel Code/Data (relocated from ROM)
  0000Cxxxh ...    Unused/reserved
  0000DF80h 80h    Used for BIOS Patches (ie. used by games, not used by BIOS)
  0000DFFCh 4      Response value from Intro/Bootmenu
  0000E000h 2000h  Kernel Memory; ExCBs, EvCBs, and TCBs allocated via B(00h)
```

#### User Memory (not used by Kernel)
```
  00010000h ...    Begin of User RAM (Exefile, Data, Heap, Stack, etc.)
  001FFF00h ...    Default Stacktop (usually in KSEG0)
  1F800000h 400h   Scratchpad (Data-Cache mis-used as Fast RAM)
```

#### Table of Tables (see BIOS Control Blocks for details)
Each table entry consists of two 32bit values; containing the base address, and
total size (in bytes) of the corresponding control blocks.<br/>
```
  00000100h  ExCB Exception Chain Entrypoints (addr=var, size=4*08h)
  00000108h  PCB  Process Control Block       (addr=var, size=1*04h)
  00000110h  TCB  Thread Control Blocks       (addr=var, size=N*C0h)
  00000118h  -    Unused/reserved
  00000120h  EvCB Event Control Blocks        (addr=var, size=N*1Ch)
  00000128h  -    Unused/reserved
  00000130h  -    Unused/reserved
  00000138h  -    Unused/reserved
  00000140h  FCB  File Control Blocks         (addr=fixed, size=10h*2Ch)
  00000148h  -    Unused/reserved
  00000150h  DCB  Device Control Blocks       (addr=fixed, size=0Ah*50h)
```
File handles (fd=00h..0Fh) can be simply converted as fcb=[140h]+fd\*2Ch.<br/>
Event handles (event=F10000xxh) as evcb=[120h]+(event AND FFFFh)\*1Ch.<br/>

#### Garbage Area at Address 00000000h
The first some bytes of memory address 00000000h aren't actually used by the
Kernel, except for storing some garbage at that locations. However, this
garbage is actually important for bugged games like R-Types and Fade to Black
(ie. games that do read from address 00000000h due to using uninitialized
pointers).<br/>
Initially, the garbage area is containing a copy of the 16-byte exception
handler at address 80h, but the first 4-bytes are typically smashed (set to
00000003h from some useless dummy writes in some useless CDROM delays). Ie. the
16-bytes should have these values:<br/>
```
  [00000000h]=3C1A0000h  ;<-- but overwritten by 00000003h after soon
  [00000004h]=275A0C80h  ;<-- or 275A0C50h (in older BIOS)
  [00000008h]=03400008h
  [0000000Ch]=00000000h
```
For R-Types, the halfword at [0] must non-zero (else the game will do a DMA to
address 0, and thereby destroy kernel memory). Fade to Black does several
garbage reads from [0..9], a wrong byte value at [5] can cause the game to
crash with an invalid memory access exception upon memory card access.<br/>
