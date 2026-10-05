#   PC File Server
#### DTL-H2000
Below BRK's are internally used in DTL-H2000 BIOS for two devices: "mwin:"
(Message Window) and "sim:" (CDROM Sim).<br/>

#### Caetla Blurb
Caetla (a firmware replacement for Cheat Devices) supports "pcdrv:" device, the
SN systems (=what?) device extension to access files on the drive of the pc.
This fileserver can be accessed by using the kernel functions, with the
"pcdrv:" device name prefix to the filenames or using the SN system calls.<br/>
The following SN system calls for the fileserver are provided. Accessed by
setting the registers and using the break command with the specified field.<br/>
The break functions have argument(s) in A1,A2,A3 (ie. unlike normal BIOS
functions not in A0,A1,A2), and TWO return values (in V0, and V1).<br/>

#### BRK(101h) - PCInit() - Inits the fileserver
No parameters.<br/>

#### BRK(102h) - PCCreat(filename, fileattributes) - Creates a new file on PC
```
  out: V0  0 = success, -1 = failure
       V1  file handle or error code if V0 is negative
```
Attributes Bits (standard MSDOS-style):<br/>
```
  bit0     Read only file (R)
  bit1     Hidden file    (H)
  bit2     System file    (S)
  bit3     Not used       (zero)
  bit4     Directory      (D)
  bit5     Archive file   (A)
  bit6-31  Not used       (zero)
```

#### BRK(103h) - PCOpen(filename, accessmode) - Opens a file on the PC
```
  out: V0  0 = success, -1 = failure
       V1  file handle or error code if V0 is negative
```

#### BRK(104h) - PCClose(filehandle) - Closes a file on the PC
```
  out: V0  0 = success, -1 = failure
       V1  0 = success, error code if V0 is negative
```

#### BRK(105h) - PCRead(filehandle, length, memory\_destination\_address)
```
  out: V0  0 = success, -1 = failure
       V1  number of read bytes or error code if V0 is negative.
```
Note: PCRead does not stop at EOF, so if you set more bytes to read than the
filelength, the fileserver will pad with zero bytes. If you are not sure of the
filelength obtain the filelength by PClSeek (A2=0, A3=2, V1 will return the
length of the file, don't forget to reset the file pointer to the start before
calling PCread!)<br/>

#### BRK(106h) - PCWrite(filehandle, length, memory\_source\_address)
```
  out: V0  0 = success, -1 = failure
       V1  number of written bytes or error code if V0 is negative.
```

#### BRK(107h) - PClSeek(filehandle, file\_offset, seekmode) - Change Filepos
seekmode may be from 0=Begin of file, 1=Current fpos, or 2=End of file.<br/>
```
  out: V0  0 = success, -1 = failure
       V1  file pointer
```
