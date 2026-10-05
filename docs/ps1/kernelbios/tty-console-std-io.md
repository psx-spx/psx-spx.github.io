#   TTY Console (std\_io)
#### A(3Fh) - Printf(txt,param1,param2,etc.) - Print string to console
```
  in:  A0                     Pointer to 0 terminated string
       A1,A2,A3,[SP+10h..]    Argument(s)
```
Prints the specified string to the TTY console. Printf does internally use
"putchar" to output the separate characters (and expands char 09h and
0Ah accordingly).<br/>
The string can contain C-style escape codes (prefixed by "%" each):<br/>
```
  c         display ASCII character
  s         display ASCII string
  i,d,D     display signed Decimal number (d/i=default32bit, D=force32bit)
  u,U       display unsigned Decimal number (u=default32bit, U=force32bit)
  o,O       display unsigned Octal number (o=default32bit, O=force32bit)
  p,x,X     display unsigned Hex number (p=lower/force32bit, x=lower, X=upper)
  n         write 32bit/16bit string length to [parameter] (default32bit)
```
Additionally, following prefixes (inserted between "%" and escape code):<br/>
```
  + or SPC  show leading plus or space character in positive signed numbers
  NNN       fixed width (for padding or so) (first digit must be 1..9) (not 0)
  .NNN      fixed width (for clipping or so)
  *         variable width (using one of the parameters) (negative=ending_spc)
  .*        variable width
  -         force ending space padding (in case of width being specified)
  #         show leading "0x" or "0X" (hex), or ensure 1 leading zero (octal)
  0         show leading zero's
  L         unknown/no effect?
  h,l       force 16bit (h=halfword), or 32bit (l=long/word)
```
The force32bit codes (D,U,O,p,l) are kinda useless since the PSX defaults to
32bit parameters anyways. The force16bit code (h) may be useful as "%hn"
(writeback 16bit value), otherwise it's rather useless, unless signed 16bit
parameters have garbage in upper 16bit, for unsigned 16bit parameters it
doesn't work at all (accidently sign-expands 16bit to 32bit, and then displays
that signed 32bit value as giant unsigned value). Printf supports only octal,
decimal, and hex (but not binary).<br/>

#### A(3Eh) or B(3Fh) - puts(src) - Write string to TTY
```
  in: R4=address of string (terminated by 00h)
```
Like "printf", but doesn't resolve any "%" operands. Empty strings are handled
in a special way: If R4 points to a 00h character then nothing is output (as
one would expect it), but, if R4 is 00000000h then "\<NULL\>" is output
(only that six letters; without appending any CR or LF).<br/>

#### A(3Dh) or B(3Eh) - gets(dst) - Read string from TTY (keyboard input)
```
  in: r4=dst (pointer to a 128-byte buffer) - out: r2=dst (same is incoming r4)
```
Internally uses "getchar" to receive the separate characters (which are
thus masked by 7Fh). The received characters are stored in the buffer, and are
additionally sent back as echo to the TTY via std\_out\_putc.<br/>
The following characters are handled in a special way: 09h (TAB) is replaced by
a single SPC. 08h or 7FH (BS or DEL) are removing the last character from the
buffer (unless it is empty) and send 08h,20h,08h (BS,SPC,BS) to the TTY. 0Dh or
0Ah (CR or LF) do terminate the input (append 00h to the buffer, send 0Ah to
the TTY, which is expanded to 0Dh,0Ah by the std\_out\_putc function, and do then
return from the gets function).<br/>
The sequence 16h,NNh forces NNh to be stored in the buffer (even if NNh is a
special character like 00h..1Fh or 7Fh). If the buffer is full (circa max 125
chars, plus one extra byte for the ending 00h), or if an unknown control code
in range of 00h..1Fh is received without the 16h prefix, then 07h (BELL) is
sent to the TTY.<br/>

#### A(3Bh) or B(3Ch) - getchar() - Read character from TTY
Reads one character from the TTY console, by internally redirecting to
"read(0,tempbuf,1)". The returned character is ANDed by 7Fh (so, to read a
fully intact 8bit character, "read(0,tempbuf,1)" must be used instead of
this function).<br/>

#### A(3Ch) or B(3Dh) - putchar(char) - Write character to TTY
Writes the character to the TTY console, by internally redirecting to
"write(1,tempbuf,1)". Char 09h (TAB) is expanded to one or more SPC
characters, until reaching the next tabulation boundary (every 8 characters).
Char 0Ah (LF) is expanded to 0Dh,0Ah (CR,LF). Other special characters (which
should be handled at the remote terminal side) are 08h (BS, backspace, move
cursor one position to the left), and 07h (BELL, produce a short beep sound).<br/>

#### C(13h) - FlushStdInOutPut()
Closes and re-opens the std\_in (fd=0) and std\_out (fd=1) file handles.<br/>

#### C(1Bh) - KernelRedirect(ttyflag)  ;PS2: ttyflag=1 causes SystemError
Removes, re-mounts, and flushes the TTY device, the parameter selects whether
to mount the real DUART-TTY device (r4=1), or a Dummy-TTY device (r4=0), the
latter one sends any std\_out to nowhere. Values other than r4=0 or r4=1 do
remove the device, but do not re-mount it (which might result in problems).<br/>
Caution: Trying to use r4=1 on a PSX that does not has the DUART hardware
installed causes the BIOS to hang (so one should first detect the DUART
hardware, eg. by writing two different bytes to Port 1F802020h.1st/2nd access,
and the read and verify that two bytes).<br/>

#### Activating std\_io
The std\_io functions can be enabled via C(1Bh) KernelRedirect(ttyflag), the
BIOS is unable to detect the presence of the TTY hardware, by default the BIOS
bootcode disables std\_io by setting the initial KernelRedirect value at
[A000B9B0h] to zero, this is hardcoded shortly after the POST(E) output:<br/>
```
  call    output_post_r4        ;\output POST(E)
  +mov    r4,0Eh                ;/
  mov     r1,0A0010000h         ;\set [0A000B9B0h]=0 ;TTY=dummy/off
  call    reset_cont_d_3        ; and call reset_cont_d_3
  +mov    [r1-4650h],0          ;/
```
assuming that R28=A0010FF0h, the last 3 opcodes of above code can be replaced
by:<br/>
```
  mov     r1,1h                 ;\set [0A000B9B0h]=1 ;TTY=duart/on
  call    reset_cont_d_3        ; and call reset_cont_d_3
  +mov    [r28-4650h-0ff0h],r1  ;/
```
with that patch, the BIOS bootcode (and many games) are sending debug messages
to the debug terminal, via expansion port, see:<br/>
[DEV8 Dual Serial Port (for TTY Debug Terminal)](../pio/expansionportpio.md#dev8-dual-serial-port-for-tty-debug-terminal)<br/>
Note: The nocash BIOS automatically detects the DUART hardware, and activates
TTY if it is present.<br/>

#### B(49h) - PrintInstalledDevices()
Uses printf to display the long and short names from the DCB of the currently
installed devices. Doesn't do anything else. There's no return value.<br/>

#### Note
Several BIOS functions are internally using printf to output status
information, timeout, and error messages, etc. So, trying to close the TTY file
handles (fd=0 and fd=1) would cause such functions to work unstable.<br/>
