#   Overview
#### BIOS CDROM Boot
The main purpose of the BIOS is to boot games from CDROM, unfortunately, before
doing that, it displays the Sony intro. It's also doing some copy protection
and region checks, and refuses to boot unlicensed games, or illegal copies, or
games for other regions.<br/>

#### BIOS Bootmenu
The bootmenu shows up when starting the Playstation without CDROM inserted. The
menu allows to play Audio CDs, and to erase or copy game positions on Memory
Cards.<br/>

#### BIOS Functions
The BIOS contains a number of more or less useful, and probably more or less
inefficient functions that can be used by software.<br/>
No idea if it's easy to take full control of the CPU, ie. to do all hardware
access and interrupt handling by software, without using the BIOS at all?<br/>
Eventually the BIOS functions for accessing the CDROM drive are important, not
sure how complicated/compatible it'd be to access the CDROM drive directly via
I/O ports... among others, there might be different drives used in different
versions of the Playstation, which aren't fully compatible with each other?<br/>

#### BIOS Memory
The BIOS occupies 512Kbyte ROM with 8bit address bus (so the BIOS ROM is rather
slow, for faster execution, portions of it are relocated to the first 64K of
RAM). For some very strange reason, the original PSX BIOS executes all ROM
functions in uncached ROM, which is incredible slow (nocash BIOS uses cached
ROM, which does work without problems).<br/>
The first 64Kbyte of the 2Mbyte Main RAM are reserved for the BIOS (containing
exception handlers, jump tables, other data, and relocated code). That reserved
region does unfortunately include the "valuable" first 32Kbytes (valuable
because that memory could be accessed directly via [R0+immediate], without
needing to use R1..R31 as base register).<br/>
