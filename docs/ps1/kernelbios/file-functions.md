#   BIOS File Functions
#### A(00h) or B(32h) - open(filename, accessmode) - Opens a file for IO
```
  out: V0  File handle (00h..0Fh), or -1 if error.
```
Opens a file on the target device for io. Accessmode is set like this:<br/>
```
  bit0     1=Read  ;\These bits aren't actually used by the BIOS, however, at
  bit1     1=Write ;/least 1 should be set; won't work when all 32bits are zero
  bit2     1=Exit without waiting for incoming data (when TTY buffer empty)
  bit9     0=Open Existing File, 1=Create New file (memory card only)
  bit15    1=Asynchronous mode (memory card only; don't wait for completion)
  bit16-31 Number of memory card blocks for a new file on the memory card
```
The PSX can have a maximum of 16 files open at any time, of which, 2 handles
are always reserved for std\_io, so only 14 handles are available for actual
files. Some functions (cd, testdevice, erase, undelete,
format, firstfile2, rename) are temporarily allocating 1 filehandle
(rename tries to use 2 filehandles, but, it does accidently use only 1
handle, too). So, for example, erase would fail if more than 13 file
handles are opened by the game.<br/>

#### A(01h) or B(33h) - lseek(fd, offset, seektype) - Move the file pointer
```
   seektype 0 = from start of file        (with positive offset)
            1 = from current file pointer (with positive/negative offset)
            2 = Bugs. Should be from end of file.
```
Moves the file pointer the number of bytes in A1, relative to the location
specified by A2. Movement from the eof is incorrect. Also, movement beyond the
end of the file is not checked.<br/>

#### A(02h) or B(34h) - read(fd, dst, length) - Read data from an open file
```
  out: V0  Number of bytes actually read, -1 if failed.
```
Reads the number of bytes from the specified open file. If length is not
specified an error is returned. Read per $0080 bytes from memory card (bu:) and
per $0800 from cdrom (cdrom:).<br/>

#### A(03h) or B(35h) - write(fd, src, length) - Write data to an open file
```
  out: V0  Number of bytes written.
```
Writes the number of bytes to the specified open file. Write to the memory card
per $0080 bytes. Writing to the cdrom returns 0.<br/>

#### A(04h) or B(36h) - close(fd) - Close an open file
Returns r2=fd (or r2=-1 if failed).<br/>

#### A(08h) or B(3Ah) - getc(fd) - read one byte from file
```
  out: R2=character (sign-expanded) or FFFFFFFFh=error
```
Internally redirects to "read(fd,tempbuf,1)". For some strange reason, the
returned character is sign-expanded; so, a return value of FFFFFFFFh could mean
either character FFh, or error.<br/>

#### A(09h) or B(3Bh) - putc(char,fd) - write one byte to file
Observe that "fd" is the 2nd paramter (not the 1st paramter as usually).<br/>
```
  out:  R2=Number of bytes actually written, -1 if failed
```
Internally redirects to "write(fd,tempbuf,1)".<br/>

#### B(40h) - cd(name) - Change the current directory on target device
Changes the current directory on the specified device, which should be "cdrom:"
(memory cards don't support directories). The PSX supports only a current
directory, but NOT a current device (ie. after cd, the directory name may be
ommited from filenames, but the device name must be still included in all
filenames).<br/>
```
  in:  A0  Pointer to new directory path (eg. "cdrom:\path")
```
Returns 1=okay, or 0=failed.<br/>
The function doesn't verify if the directory exists. Caution: For cdrom, the
function does always load the path table from the disk (even if it was already
stored in RAM, so cd is causing useless SLOW read/seek delays).<br/>

#### B(42h) - firstfile2(filename,direntry) - Find first file to match the name
Returns r2=direntry (or r2=0 if no matching files).<br/>
Searches for the first file to match the specified filename; the filename may
contain "?" and "\*" wildcards. "\*" means to ignore ALL following characters;
accordingly one cannot specify any further characters after the "\*" (eg.
"DATA\*" would work, but "\*.DAT" won't work). "?" is meant to ignore a single
character cell. Note: The "?" wildcards (but not "\*") can be used also in all
other file functions; causing the function to use the first matching name (eg.
erase "????" would erase the first matching file, not all matching files).<br/>
Start the name with the device you want to address. (ie. pcdrv:) Different
drives can be accessed as normally by their drive names (a:, c:, huh?) if path
is omitted after the device, the current directory will be used.<br/>
A direntry structure looks like this:<br/>
```
  00h 14h Filename, terminated with 00h
  14h 4   File attribute (always 0 for cdrom) (50h=norm or A0h=del for card)
  18h 4   File size
  1Ch 4   Pointer to next direntry? (not used?)
  20h 4   First Sector Number
  24h 4   Reserved (not used)
```
BUG: If "?" matches the ending 00h byte of a name, then any further characters
in the search expression are ignored (eg. "FILE?.DAT" would match to
"FILE2.DAT", but accidently also to "FILE").<br/>
BUG: For CDROM, the BIOS includes some code that is intended to realize disk
changes during firstfile2/nextfile operations, however, that code is so bugged
that it does rather ensure that the BIOS does NOT realize new disks being
inserted during firstfile2/nextfile.<br/>
BUG: firstfile2/nextfile is internally using a FCB. On the first call to
firstfile2, the BIOS is searching a free FCB, and does apply that as "search
fcb", but it doesn't mark that FCB as allocated, so other file functions may
accidently use the same FCB. Moreover, the BIOS does memorize that "search
fcb", and, even when starting a new search via another call to firstfile2, it
keeps using that FCB for search (without checking if the FCB is still free). A
possible workaround is not to have any files opened during firstfile2/nextfile
operations.<br/>

#### B(43h) - nextfile(direntry) - Searches for the next file to match the name
Returns r2=direntry (or r2=0 if no more matching files).<br/>
Uses the settings of a previous firstfile2/nextfile command.<br/>

#### B(44h) - rename(old\_filename, new\_filename)
Returns 1=okay, or 0=failed.<br/>

#### B(45h) - erase(filename) - Delete a file on target device
Returns 1=okay, or 0=failed.<br/>

#### B(46h) - undelete(filename)
Returns 1=okay, or 0=failed.<br/>

#### B(41h) - format(devicename)
Erases all files on the device (ie. for formatting memory cards).<br/>
Returns 1=okay, or 0=failed.<br/>

#### B(54h) - \_get\_errno()
Indicates the reason of the most recent file function error (open,
lseek, read, write, close, _get_error, ioctl, cd,
testdevice, erase, undelete, format, rename). Use
_get_errno() ONLY if an error has occured (the error code isn't reset to zero
by functions that are passing okay). firstfile2/nextfile do NOT affect
_get_errno(). See below list of File Error Numbers for more info.<br/>

#### B(55h) - \_get\_error(fd)
Basically same as B(54h), but allowing to specify a file handle for which error
information is to be received; accordingly it doesn't work for functions that
do use 'hidden' internal file handles (eg. erase, or unsuccessful
open). Returns FCB[18h], or FFFFFFFFh if the handle is invalid/unused.<br/>

#### A(05h) or B(37h) - ioctl(fd,cmd,arg)
Used only for TTY.<br/>

#### A(07h) or B(39h) - isatty(fd)
Returns bit1 of the file's DCB flags. That bit is set only for Duart/TTY, and
is cleared for Dummy/TTY, Memory Card, and CDROM.<br/>

#### B(59h) - testdevice(devicename)
Whatever. Checks the devicename, and if it's accepted, calls a device specific
function. For the existing devices (cdrom,bu,tty) that specific function simply
returns without doing anything. Maybe other devices (like printers or modems)
would do something more interesting.<br/>

#### File Error Numbers for B(54h) and B(55h)
```
  00h okay (though many successful functions leave old error code unchanged)
  02h file not found
  06h bad device port number (tty2 and up)
  09h invalid or unused file handle
  10h general error (physical I/O error, unformatted, disk changed for old fcb)
  11h file already exists error (create/undelete/rename)
  12h tried to rename a file from one device to another device
  13h unknown device name
  16h sector alignment error, or fpos>=filesize, unknown seektype or ioctl cmd
  18h not enough free file handles
  1Ch not enough free memory card blocks
  FFFFFFFFh invalid or unused file handle passed to B(55h) function
```
