#   BIOS Joypad Functions
#### Pad Input
Joypads should be initialized via InitPAD2(buf1,22h,buf2,22h), and StartPAD2().
The main program can read the pad data from the buf1/buf2 addresses (including
Status, ID1, button states, and any kind of analogue inputs). For more info on
ID1, Buttons and analogue inputs, see<br/>
[Controllers and Memory Cards](../sio/controllersandmemorycards/index.md)<br/>
Note: The BIOS doesn't include any functions for sending custom data to the
pads (such like for controlling rumble motors).<br/>

#### B(12h) - InitPAD2(buf1, siz1, buf2, siz2)
Memorizes the desired buf1/buf2 addresses, zerofills the buffers by using the
siz1/siz2 buffer size values (which should be 22h bytes each). And does some
initialization on the PadCardIrq element (but doesn't enqueue it, that must be
done by a following call to StartPAD2), and does set the "pad\_enable\_flag", that
flag can be also set/cleared via InitCARD2(pad\_enable), where it selects if the
Pads are kept handled together with Memory Cards. buf1/buf2 are having the
following format:<br/>
```
  00h      Status (00h=okay, FFh=timeout/wrong ID2)
  01h      ID1    (eg. 41h=digital_pad, 73h=analogue_pad, 12h=mouse, etc.)
  02h..21h Data   (max 16 halfwords, depending on lower 4bit of ID1)
```
Note: InitPAD2 does initially zerofill the buffers, so, until the first IRQ is
processed, the initial status is 00h=okay, with buttons=0000h (all buttons
pressed), to fix that situation, change the two status bytes to FFh after
calling InitPAD2 (or alternately, reject ID1=00h).<br/>
Once when the PadCardIrq is enqueued via StartPAD2, and while "pad\_enable\_flag"
is set, the data for (both) Pad1 and Pad2 is read on Vblank interrupts, and
stored in the buffers, the IRQ handler stores up to 22h bytes in the buffer
(regardless of the siz1/siz2 values) (eg. a Multitap adaptor uses all 22h
bytes).<br/>

#### B(13h) - StartPAD2()
Should be used after InitPAD2. Enqueues the PadCardIrq handler, and does
additionally initialize some flags.<br/>

#### B(14h) - StopPAD2()
Dequeues the PadCardIrq handler. Note that this handler is also used for memory
cards, so it'll "stop" cards, too.<br/>

#### B(15h) - PAD\_init2(type, button\_dest, unused, unused)
This is an extremely bizarre and restrictive function - don't use! The function
fails unless type is 20000000h or 20000001h (the type value has no other
function). The function uses "buf1/buf2" addresses that are located somewhere
"hidden" within the BIOS variables region, the only way to read from that
internal buffers is to use the ugly "PAD_dr()" function. For
some strange reason it FFh-fills buf1/buf2, and does then call
InitPAD2(buf1,22h,buf2,22) (which does immediately 00h-fill the previously
FFh-filled buffers), and does then call StartPAD2().<br/>
Finally, it does memorize the "button\_dest" address (see
PAD_dr() for details on that value). The two unused parameters
have no function, however, they are internally written back to the stack
locations reserved for parameter 2 and 3, ie. at [SP+08h] and [SP+0Ch] on the
caller's stack, so the function MUST be called with all four parameters
allocated on stack. Return value is 2 (or 0 if type was disliked).<br/>

#### B(16h) - PAD\_dr()
This is a very ugly function, using the internal "buf1/buf2" values from
"PAD_init2" and the "button\_dest" value that was passed to that
function.<br/>
If "button\_dest" is non-zero, then this function is automatically called by the
PadCardIrq handler, and stores it's return value at [button\_dest] (where it may
be read by the main program). If "button\_dest" is zero, then it isn't called
automatically, and it \<can\> be called manually (with return value in R2),
however, it does additionally write the return value to [button\_dest], ie. to
[00000000h] in this case, destroying that memory location.<br/>
The return value itself is useless garbage: The lower 16bit contain the pad1
buttons, the upper 16bit the pad2 buttons, of which, both values have reversed
byte-order (ie. the first button byte in upper 8bit). The function works only
with controller IDs 41h (digital joypad) and 23h (nonstandard device). For
ID=23h, the halfword is ORed with 07C7h, and bit6,7 are then cleared if the
analogue inputs are greater than 10h. For ID=41h the data is left intact. Any
other ID values, or disconnected joypads, cause the halfword to be set to FFFFh
(same as when no buttons are pressed), that includes newer analogue pads
(unless they are switched to "digital" mode).<br/>
