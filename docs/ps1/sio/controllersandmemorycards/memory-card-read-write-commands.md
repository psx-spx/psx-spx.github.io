#   Memory Card Read/Write Commands
#### Reading Data from Memory Card
```
  Send Reply Comment
  81h  N/A   Memory card address
  52h  FLAG  Send Read Command (ASCII "R"), Receive FLAG Byte
  00h  5Ah   Receive Memory Card ID1
  00h  5Dh   Receive Memory Card ID2
  MSB  (00h) Send Address MSB  ;\sector number (0..3FFh)
  LSB  (pre) Send Address LSB  ;/
  00h  5Ch   Receive Command Acknowledge 1  ;<-- late /ACK after this byte-pair
  00h  5Dh   Receive Command Acknowledge 2
  00h  MSB   Receive Confirmed Address MSB
  00h  LSB   Receive Confirmed Address LSB
  00h  ...   Receive Data Sector (128 bytes)
  00h  CHK   Receive Checksum (MSB xor LSB xor Data bytes)
  00h  47h   Receive Memory End Byte (should be always 47h="G"=Good for Read)
```
Non-sony cards additionally send eight 5Ch bytes after the end flag.<br/>
When sending an invalid sector number, original Sony memory cards respond with
FFFFh as Confirmed Address (and do then abort the transfer without sending any
data, checksum, or end flag), third-party memory cards typically respond with
the sector number ANDed with 3FFh (and transfer the data for that adjusted
sector number).<br/>

#### Writing Data to Memory Card
```
  Send Reply Comment
  81h  N/A   Memory card address
  57h  FLAG  Send Write Command (ASCII "W"), Receive FLAG Byte
  00h  5Ah   Receive Memory Card ID1
  00h  5Dh   Receive Memory Card ID2
  MSB  (00h) Send Address MSB  ;\sector number (0..3FFh)
  LSB  (pre) Send Address LSB  ;/
  ...  (pre) Send Data Sector (128 bytes)
  CHK  (pre) Send Checksum (MSB xor LSB xor Data bytes)
  00h  5Ch   Receive Command Acknowledge 1
  00h  5Dh   Receive Command Acknowledge 2
  00h  4xh   Receive Memory End Byte (47h=Good, 4Eh=BadChecksum, FFh=BadSector)
```

#### Get Memory Card ID Command
```
  Send Reply Comment
  81h  N/A   Memory card address
  53h  FLAG  Send Get ID Command (ASCII "S"), Receive FLAG Byte
  00h  5Ah   Receive Memory Card ID1
  00h  5Dh   Receive Memory Card ID2
  00h  5Ch   Receive Command Acknowledge 1
  00h  5Dh   Receive Command Acknowledge 2
  00h  04h   Receive 04h
  00h  00h   Receive 00h
  00h  00h   Receive 00h
  00h  80h   Receive 80h
```
This command is supported only by original Sony memory cards. Not sure if all
sony cards are responding with the same values, and what meaning they have,
might be number of sectors (0400h) and sector size (0080h) or whatever.<br/>

#### Invalid Commands
```
  Send Reply Comment
  81h  N/A   Memory card address
  xxh  FLAG  Send Invalid Command (anything else than "R", "W", or "S")
```
Transfer aborts immediately after the faulty command byte, or, occasionally
after one more byte (with response FFh to that extra byte).<br/>

#### FLAG Byte
The initial value of the FLAG byte on power-up (and when re-inserting the
memory card) is 08h.<br/>
Bit3=1 is indicating that the directory wasn't read yet (allowing to sense
memory card changes). For some strange reason, bit3 is NOT reset when reading
from the card, but rather when writing to it. To reset the flag, games are
usually issuing a dummy write to sector number 003Fh, more or less
unneccessarily stressing the lifetime of that sector.<br/>
Bit2=1 seems to be intended to indicate write errors, however, the write
command seems to be always finishing without setting that bit, instead, the
error flag may get set on the NEXT command.<br/>
Note: Some (not all) non-sony cards also have Bit5 of the FLAG byte set.<br/>

#### Timings
IRQ7 is usually triggered circa 1500 cycles after sending a byte (counted from
the begin of the first bit), except, the last byte doesn't trigger IRQ7, and,
after the 7th byte of the Read command, an additional delay of circa 31000
cycles occurs before IRQ7 gets triggered (that strange extra delay occurs only
on original Sony cards, not on cards from other manufacturers).<br/>
There seems to be no extra delays in the Write command, as it seems, the data
is written on the fly, and one doesn't need to do any write-busy handling...
although, theoretically, the write shouldn't start until verifying the
checksum... so it can't be done on the fly at all...?<br/>

#### Notes
Responses in brackets are don't care, (00h) means usually zero, (pre) means
usually equal to the previous command byte (eg. the response to LSB is MSB).<br/>

Memory cards are reportedly "Flash RAM" which sounds like bullshit, might be
battery backed SRAM, or FRAM, or slower EEPROM or FLASH ROM, or vary from card
to card...?<br/>
