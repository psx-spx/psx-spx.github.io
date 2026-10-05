#   CDROM Functions
#### General File Functions
CDROMs are basically accessed via normal file functions, with device name
"cdrom:" (which is an abbreviation for "cdrom0:", anyways, the port number is
ignored).<br/>
[File Functions](file-functions.md#file-functions)<br/>
[File Execute and Flush Cache](file-execute-and-flush-cache.md#file-execute-and-flush-cache)<br/>
Before starting the boot executable, the BIOS automatically calls _96_init(), so
the game doesn't need to do any initializations before using CDROM file
functions.<br/>

#### Absent CD-Audio Support
The Kernel doesn't include any functions for playing Audio tracks. Also,
there's no BIOS function for setting the XA-ADPCM file/channel filter values.
So CD Audio can be used only by directly programming the CDROM I/O ports.<br/>

#### Asynchronous CDROM Access
The normal File functions are always using synchroneous access for CDROM (ie.
the functions do wait until all data is transferred) (unlike as for memory
cards, accessmode.bit15 cannot be used to activate asynchronous cdrom access).<br/>
However, one can read files in asynchrouneous fashion via CdGetLbn,
CdAsyncSeekL, and CdAsyncReadSector. CDROM files are non-fragmented, so they
can be read simply from incrementing sector numbers.<br/>

#### A(A4h) - CdGetLbn(filename)
Returns the first sector number used by the file, or -1 in case of error.<br/>
BUG: The function accidently returns -1 for the first file in the directory
(the first file should be a dummy entry for the current or parent directory or
so, so that bug isn't much of a problem), if the file is not found, then the
function accidently returns garbage (rather than -1).<br/>

#### A(A5h) - CdReadSector(count,sector,buffer)
Reads \<count\> sectors, starting at \<sector\>, and writes data to
\<buffer\>. The read is done in mode=80h (double speed, 800h-bytes per
sector). The function waits until all sectors are transferred, and does then
return the number of sectors (ie. count), or -1 in case of error.<br/>

#### A(A6h) - CdGetStatus()
Retrieves the cdrom status via CdAsyncGetStatus(dst) (see there for details;
especially for cautions on door-open flag). The function waits until the event
indicates completion, and does then return the status byte (or -1 in case of
error).<br/>

#### A(78h) - CdAsyncSeekL(src)
Issues Setloc and SeekL commands. The parameter (src) is a pointer to a 3-byte
sector number (MM,SS,FF) (in BCD format).<br/>
The function returns 0=failed, or 1=okay. Completion is indicated by events
(class=F0000003h, and spec=20h, or 8000h).<br/>

#### A(7Ch) - CdAsyncGetStatus(dst)
Issues a GetStat command. The parameter (dst) is a pointer to a 1-byte location
that receives the status response byte.<br/>
The function returns 0=failed, or 1=okay. Completion is indicated by events
(class=F0000003h, and spec=20h, or 8000h).<br/>
Caution: The command acknowledges the door-open flag, but doesn't automatically
reload the path table (which is required if a new disk is inserted); if the
door-open flag was set, one should call a function that does forcefully load
the path table (like cd).<br/>

#### A(7Eh) - CdAsyncReadSector(count,dst,mode)
Issues SetMode and ReadN (when mode.bit8=0), or ReadS (when mode.bit8=1)
commands. count is the number of sectors to be read, dst is the destination
address in RAM, mode.bit0-7 are passed as parameter to the SetMode command,
mode.bit8 is the ReadN/ReadS flag (as described above). The sector size (for
DMA) depends on the mode value: 918h-bytes (bit4=1, bit5=X), 924h-bytes
(bit4=0, bit5=1), or 800h-bytes (bit4,5=0).<br/>
Before CdAsyncReadSector, the sector number should be set via
CdAsyncSeekL(src).<br/>
The function returns 0=failed, or 1=okay. Completion is indicated by events
(class=F0000003h, and spec=20h, 80h, or 8000h).<br/>

#### A(81h) - CdAsyncSetMode(mode)
Similar to CdAsyncReadSector (see there for details), but issues only the
SetMode command, without any following ReadN/ReadS command.<br/>

#### A(94h) - CdromGetInt5errCode(dst1,dst2)
Returns the first two response bytes from the most recent INT5 error:
[dst1]=status, [dst2]=errorcode. The BIOS doesn't reset these values in case of
successful completion, so the values are quite useless.<br/>

#### A(54h) or A(71h) - \_96\_init()
#### A(56h) or A(72h) - \_96\_remove()  ;does NOT work due to SysDeqIntRP bug
#### A(90h) - CdromIoIrqFunc1()
#### A(91h) - CdromDmaIrqFunc1()
#### A(92h) - CdromIoIrqFunc2()
#### A(93h) - CdromDmaIrqFunc2()
#### A(95h) - CdInitSubFunc()  ;subfunction for _96_init()
#### A(9Eh) - SetCdromIrqAutoAbort(type,flag)
#### A(A2h) - EnqueueCdIntr()  ;with prio=0 (fixed)
#### A(A3h) - DequeueCdIntr()  ;does NOT work due to SysDeqIntRP bug
Internally used CDROM functions for initialization and IRQ handling.<br/>
