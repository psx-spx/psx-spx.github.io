#   Memory Card Functions
#### General File Functions
Memory Cards aka Backup Units (bu) are basically accessed via normal file
functions, with device names "bu00:" (Slot 1) and "bu10:" (Slot 2),<br/>
[File Functions](file-functions.md#file-functions)<br/>
Before using the file functions for memory cards, first call
InitCARD2(pad\_enable), then StartCARD2(), and then \_bu\_init().<br/>

#### File Header, Filesize, and Sector Alignment
The first 100h..200h bytes (2..4 sectors) of the file must contain the title
and icon bitmap(s). For details, see:<br/>
[Memory Card Data Format](../sio/controllersandmemorycards/memory-card-data-format.md#memory-card-data-format)<br/>
The filesize must be a multiple of 2000h bytes (one block), the maximum size
would be 1E000h bytes (when using all 15 blocks on the memory card). The
filesize must be specified when creating the file (ie. accessmode bit9=1, and
bit16-31=number of blocks). Once when the file is created, the BIOS does NOT
allow to change the filesize (unless by deleting and re-creating the file).<br/>
When reading/writing files, the amount of data must be a multiple of 80h bytes
(one sector), and the file position must be aligned to a 80h-byte boundary,
too. There's no restriction on fragmented files (ie. one may cross 2000h-byte
block boundaries within the file).<br/>

#### Poor Memcard Performance
PSX memory card accesses are typically super-slow. That, not so much because
the hardware would be slow, but rather because of improper inefficent code at
the BIOS side. The original BIOS tries to synchronize memory card accesses with
joypad accesses simply by accessing only one sector per frame (although it
could access circa two sectors). To the worst, the BIOS accesses Slot 1 only on
each second frame, and Slot 2 only each other frame (although in 99% of all
cases only one slot is accessed at once, so the access time drops to 0.5
sectors per frame).<br/>
Moreover, the memory card id, directory, and broken sector list do occupy 26
sectors (although the whole information would fit into 4 or 5 sectors) (a
workaround would be to read only the first some bytes, and to skip the
additional unused bytes - though that'd also mean to skip the checksums which
are unfortunately stored at the end of the sector).<br/>
And, anytime when opening a file (in synchronous mode), the BIOS does
additionally read sector 0 (which is totally useless, and gets especially slow
when opening a bunch of files; eg. when extracting the title/icon from all
available files on the card).<br/>

#### Asynchronous Access
The BIOS supports synchronous and asynchronous memory card access. Synchronous
means that the BIOS function doesn't return until the access has completed
(which means, due to the poor performance, that the function spends about 75%
of the time on inactivity) (except in nocash PSX bios, which has better
performance), whilst asynchronous access means that the BIOS function returns
immediately after invoking the access (which does then continue on interrupt
level, and does return an event when finished).<br/>
The file "read" and "write" functions act asynchronous when accessmode
bit15 is set when opening the file. Additionally, the A(ACh)
\_card\_load(port) function can be used to tell the BIOS to load
the directory entries and broken sector list to its internal RAM buffers (eg.
during the games title screen, so the BIOS doesn't need to load that data once
when the game enters its memory card menu). All other functions like erase
or format always act synchronous. The open/findfirst/findnext
functions do normally complete immediately without accessing the card at all
(unless the directory wasn't yet read; in that case the directory is loading in
synchronous fashion).<br/>
Unfortunately, the asynchronous response doesn't rely on a single callback
event, but rather on a bunch of different events which must be all allocated
and tested by the game (and of which, one event is delivered on completion)
(which one depends on whether function completed okay, or if an error
occurred).<br/>

#### Multitap Support (and Multitap Problems)
The BIOS does have some partial support for accessing more than two memory
cards (via Multitap adaptors). Device/port names "bu01:", "bu02:", "bu03:"
allow to access extra memory carts in slot1 (and "bu11:", "bu12:", "bu13:" in
slot2). Namely, those names will send values 82h, 83h, 84h to the memory card
slot (instead of the normal 81h value).<br/>
However, the BIOS directory\_buffer and broken\_sector\_list do support only two
memory cards (one in slot1 and one in slot2). So, trying to access more memory
cards may cause great data corruption (though there might be a way to get the
BIOS to reload those buffers before accessing a different memory card).<br/>
Aside from that problem, the BIOS functions are very-very-very slow even when
accessing only two memory cards. Trying to use the BIOS to access up to eight
memory cards would be very-extremly-very slow, which would be more annoying
than useful.<br/>

#### B(4Ah) - InitCARD2(pad\_enable)  ;uses/destroys k0/k1 !!!
#### B(4Bh) - StartCARD2()
#### B(4Ch) - StopCARD2()
#### A(55h) or A(70h) - \_bu\_init()

```
  --- Below are some lower level memory card functions ---
```

#### A(ABh) - \_card\_info(port)
#### B(4Dh) - \_card\_info\_subfunc(port)  ;subfunction for "\_card\_info"
Can be used to check if the most recent call to \_card\_write has completed
okay. Issues an incomplete dummy read command (similar to B(4Fh) -
\_card\_read). The read command is aborted once when receiving the status
byte from the memory card (the actual data transfer is skipped).<br/>

#### A(AFh) - card\_write\_test(port)  ;not supported by old CEX-1000 version
Resets the card changed flag. For some strange reason, this flag isn't
automatically reset after reading the flag, instead, the flag is reset upon
sector writes. To do that, this function issues a dummy write to sector 3Fh.<br/>

#### B(50h) - \_new\_card()
Normally any memory card read/write functions fail if the BIOS senses the card
change flag to be set. Calling this function tells the BIOS to ignore the card
change flag on the next read/write operation (the function is internally used
when loading the "MC" ID from sector 0, and when calling the card\_write\_test
function to acknowledge the card change flag).<br/>

#### B(4Eh) - \_card\_write(port,sector,src)
#### B(4Fh) - \_card\_read(port,sector,dst)
Invokes asynchronous reading/writing of a single sector. The function returns
1=okay, or 0=failed (on invalid sector numbers). The actual I/O is done on IRQ
level, completion of the I/O command transmission can be checked, among others,
via get/wait\_card\_status(slot) functions (with slot=port/10h).<br/>
In case of the write function, completion of the \<transmission\> does NOT
mean that the actual \<writing\> has completed, instead, write errors are
indicated upon completion of the \<next sector\> read/write transmission
(or, if there are no further sectors to be accessed; one can use \_card\_info to
verify completion of the last written sector).<br/>
The sector number should be in range of 0..3FFh, for some strange reason,
probably a BUG, the function also accepts sector 400h. The specified sector
number is directly accessed (it is NOT parsed through the broken sector
replacement list).<br/>

#### B(5Ch) - \_card\_status(slot)
#### B(5Dh) - \_card\_wait(slot)
Returns the status of the most recent I/O command, possible values are:<br/>
```
  01h=ready
  02h=busy/read
  04h=busy/write
  08h=busy/info
  11h=failed/timeout (eg. when no cartridge inserted)
  21h=failed/general error
```
\_card\_status returns immediately, \_card\_wait waits until a non-busy
state occurs.<br/>

#### A(A7h) - bufs\_cb\_0()
#### A(A8h) - bufs\_cb\_1()
#### A(A9h) - bufs\_cb\_2()
#### A(AAh) - bufs\_cb\_3()
#### A(AEh) - bufs\_cb\_4()
These five callback functions are internally used by the BIOS, notifying other
BIOS functions about (un-)successful completion of memory card I/O commands.<br/>

#### B(58h) - \_card\_chan()
This is a subfunction for the five bufs\_cb_\_xxx functions (indicating
whether the callback occured for a slot1 or slot2 access).<br/>

#### A(ACh) - \_card\_load(port)
Invokes asynchronous reading of the memory card directory. The function isn't
too useful because the BIOS tends to read the directory automatically in
various places in synchronous mode, so there isn't too much chance to replace
the automatic synchronous reading by asynchronous reading.<br/>

#### A(ADh) - \_card\_auto(flag)
Can be used to enable/disable auto format (0=off, 1=on). The \_bu\_init function
initializes auto format as disabled. If auto format is enabled, then the BIOS
does automatically format memory cards if it has failed to read the "MC" ID
bytes on sector 0. Although potentially useful, activating this feature is
rather destructive (for example, read errors on sector 0 might occur accidently
due to improperly inserted cards with dirty contacts, so it'd be better to
prompt the user whether or not to format the card, rather than doing that
automatically).<br/>

#### C(1Ah) - set\_card\_find\_mode(mode)
#### C(1Dh) - get\_card\_find\_mode()
Allows to get/set the card find mode (0=normal, 1=find deleted files), the mode
setting affects only the firstfile2/nextfile functions. All other file functions
are used fixed mode settings (always mode=0 for open, rename,
erase, and mode=1 for undelete).<br/>
