#   GPU Functions
#### A(48h) - SendGP1Command(gp1cmd)
Writes [1F801814h]=gp1cmd. There's no return value (r2 is left unchanged).<br/>

#### A(49h) - GPU\_cw(gp0cmd)      ;send GP0 command word
Calls gpu\_sync(), and does then write [1F801810h]=gp0cmd. Returns the return
value from the gpu\_sync() call.<br/>

#### A(4Ah) - GPU\_cwp(src,num) ;send GP0 command word and parameter words
Calls gpu\_sync(), and does then copy "num" words from [src and up] to
[1F801810h], src should usually point to a command word, followed by num-1
parameter words. Transfer is done by software (without DMA). Always returns 0.<br/>

#### A(4Bh) - send\_gpu\_linked\_list(src)
Transfer an OT via DMA. Calls gpu\_sync(), and does then write
[1F801814h]=4000002h, [1F8010F4h]=0, [1F8010F0h]=[1F8010F0h] OR 800h,
[1F8010A0h]=src, [1F8010A4h]=0, [1F8010A8h]=1000401h. The function does
additionally output a bunch of TTY status messages via printf. The function
doesn't wait until the DMA is completed. There's no return value.<br/>

#### A(4Ch) - gpu\_abort\_dma()
Writes [1F8010A8h]=401h, [1F801814h]=4000000h, [1F801814h]=2000000h,
[1F801814h]=1000000h. Ie. stops GPU DMA, and issues GP1(4), GP1(2), GP1(1).
Returns 1F801814h, ie. the I/O address.<br/>

#### A(4Dh) - GetGPUStatus()
Reads [1F801814h] and returns that value.<br/>

#### A(46h) - GPU\_dw(Xdst,Ydst,Xsiz,Ysiz,src)
Waits until GP1.R.Bit26 is set (unlike gpu\_sync, which waits for Bit28), and
does then [1F801810h]=A0000000h, [1F801810h]=YdstXdst, [1F801810h]=YsizXsiz,
and finally transfers "N" words from [src and up] to [1F801810h], where "N" is
"Xsiz\*Ysiz/2". The data is transferred by software (without DMA) (by code
executed in the uncached BIOS region with high waitstates, so the data transfer
is very SLOW).<br/>
Caution: If "Xsiz\*Ysiz" is odd, then the last halfword is NOT transferred, so
the GPU stays waiting for the last data value.<br/>
Returns [SP+04h]=Ydst, [SP+08h]=Xsiz, [SP+0Ch]=Ysiz, [SP+10h]=src+N\*4, and
R2=src=N\*4.<br/>

#### A(47h) - gpu\_send\_dma(Xdst,Ydst,Xsiz,Ysiz,src)
Calls gpu\_sync(), writes [1F801810h]=A0000000h, [1F801814h]=4000002h,
[1F8010F0h]=[1F8010F0h] OR 800h, [1F8010A0h]=src, [1F8010A4h]=N\*10000h+10h
(where N="Xsiz\*Ysiz/32"), [1F8010A8h]=1000201h.<br/>
Caution: If "Xsiz\*Ysiz" is not a multiple of 32, then the last halfword(s) are
NOT transferred, so the GPU stays waiting for that values.<br/>
Returns R2=1F801810h, and [SP+04h]=Ydst, [SP+08h]=Xsiz, [SP+0Ch]=Ysiz.<br/>

#### A(4Eh) - gpu\_sync()
If DMA is off (when GP1.R.Bit29-30 are zero): Waits until GP1.R.Bit28=1 (or
until timeout).<br/>
If DMA is on: Waits until D2\_CHCR.Bit24=0 (or until timeout), and does then
wait until GP1.R.Bit28=1 (without timeout, ie. may hang forever), and does
then turn off DMA via GP1(04h).<br/>
Returns 0 (or -1 in case of timeout, however, the timeout values are very big,
so it may take a LOT of seconds before it returns).<br/>
