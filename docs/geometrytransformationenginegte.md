#   Geometry Transformation Engine (GTE)
[GTE Overview](geometrytransformationenginegte.md#gte-overview)<br/>
[GTE Registers](geometrytransformationenginegte.md#gte-registers)<br/>
[GTE Saturation](geometrytransformationenginegte.md#gte-saturation)<br/>
[GTE Opcode Summary](geometrytransformationenginegte.md#gte-opcode-summary)<br/>
[GTE Coordinate Calculation Commands](geometrytransformationenginegte.md#gte-coordinate-calculation-commands)<br/>
[GTE General Purpose Calculation Commands](geometrytransformationenginegte.md#gte-general-purpose-calculation-commands)<br/>
[GTE Color Calculation Commands](geometrytransformationenginegte.md#gte-color-calculation-commands)<br/>
[GTE Division Inaccuracy](geometrytransformationenginegte.md#gte-division-inaccuracy)<br/>



##   GTE Overview
#### GTE Operation
The GTE doesn't have any memory or I/O ports mapped to the CPU memory bus,
instead, it's solely accessed via coprocessor opcodes:<br/>
```
  mov  cop0r12,rt          ;-enable/disable COP2 (GTE) via COP0 status register
  mov  cop2r0-63,rt        ;\write parameters to GTE registers
  mov  cop2r0-31,[rs+imm]  ;/
  mov  cop2cmd,imm25       ;-issue GTE command
  mov  rt,cop2r0-63        ;\read results from GTE registers
  mov  [rs+imm],cop2r0-31  ;/
  jt   cop2flg,dest        ;-jump never  ;\implemented (no exception), but,
  jf   cop2flg,dest        ;-jump always ;/flag seems to be always "false"
```
GTE (memory-?) load and store instructions have a delay of 2 instructions, for
any GTE commands or operations accessing that register. Any? That's wrong!<br/>
GTE instructions and functions should not be used in<br/>
```
  - Delay slots of jumps and branches
  - Event handlers or interrupts (sounds like nonsense?) (need push/pop though)
```
If an instruction that reads a GTE register or a GTE command is executed before
the current GTE command is finished, the CPU will hold until the instruction
has finished. The number of cycles each GTE instruction takes is shown in the
command list.<br/>

#### GTE Command Encoding (COP2 imm25 opcodes)
```
  31-25  Must be 0100101b for "COP2 imm25" instructions
  20-24  Fake GTE Command Number (00h..1Fh) (ignored by hardware)
  19     sf - Shift Fraction in IR registers (0=No fraction, 1=12bit fraction)
  17-18  MVMVA Multiply Matrix    (0=Rotation. 1=Light, 2=Color, 3=Reserved)
  15-16  MVMVA Multiply Vector    (0=V0, 1=V1, 2=V2, 3=IR/long)
  13-14  MVMVA Translation Vector (0=TR, 1=BK, 2=FC/Bugged, 3=None)
  11-12  Always zero                        (ignored by hardware)
  10     lm - Saturate IR1,IR2,IR3 result (0=To -8000h..+7FFFh, 1=To 0..+7FFFh)
  6-9    Always zero                        (ignored by hardware)
  0-5    Real GTE Command Number (00h..3Fh) (used by hardware)
```
The MVMVA bits are used only by the MVMVA opcode (the bits are zero for all
other opcodes).<br/>
The "sf" and "lm" bits are usually fixed (either set, or cleared, depending on
the command) (for MVMVA, the bits are variable) (also, "sf" can be changed for
some commands like SQR) (although they are usually fixed for most other
opcodes, changing them might have some effect on some/all opcodes)?<br/>

#### GTE Data Register Summary (cop2r0-31)
```
  cop2r0-1   3xS16 VXY0,VZ0              Vector 0 (X,Y,Z)
  cop2r2-3   3xS16 VXY1,VZ1              Vector 1 (X,Y,Z)
  cop2r4-5   3xS16 VXY2,VZ2              Vector 2 (X,Y,Z)
  cop2r6     4xU8  RGBC                  Color/code value
  cop2r7     1xU16 OTZ                   Average Z value (for Ordering Table)
  cop2r8     1xS16 IR0                   16bit Accumulator (Interpolate)
  cop2r9-11  3xS16 IR1,IR2,IR3           16bit Accumulator (Vector)
  cop2r12-15 6xS16 SXY0,SXY1,SXY2,SXYP   Screen XY-coordinate FIFO  (3 stages)
  cop2r16-19 4xU16 SZ0,SZ1,SZ2,SZ3       Screen Z-coordinate FIFO   (4 stages)
  cop2r20-22 12xU8 RGB0,RGB1,RGB2        Color CRGB-code/color FIFO (3 stages)
  cop2r23    4xU8  (RES1)                Prohibited
  cop2r24    1xS32 MAC0                  32bit Maths Accumulators (Value)
  cop2r25-27 3xS32 MAC1,MAC2,MAC3        32bit Maths Accumulators (Vector)
  cop2r28-29 1xU15 IRGB,ORGB             Convert RGB Color (48bit vs 15bit)
  cop2r30-31 2xS32 LZCS,LZCR             Count Leading-Zeroes/Ones (sign bits)
```

#### GTE Control Register Summary (cop2r32-63)
```
  cop2r32-36 9xS16 RT11RT12,..,RT33 Rotation matrix     (3x3)        ;cnt0-4
  cop2r37-39 3x 32 TRX,TRY,TRZ      Translation vector  (X,Y,Z)      ;cnt5-7
  cop2r40-44 9xS16 L11L12,..,L33    Light source matrix (3x3)        ;cnt8-12
  cop2r45-47 3x 32 RBK,GBK,BBK      Background color    (R,G,B)      ;cnt13-15
  cop2r48-52 9xS16 LR1LR2,..,LB3    Light color matrix source (3x3)  ;cnt16-20
  cop2r53-55 3x 32 RFC,GFC,BFC      Far color           (R,G,B)      ;cnt21-23
  cop2r56-57 2x 32 OFX,OFY          Screen offset       (X,Y)        ;cnt24-25
  cop2r58 BuggyU16 H                Projection plane distance.       ;cnt26
  cop2r59      S16 DQA              Depth queing parameter A (coeff) ;cnt27
  cop2r60       32 DQB              Depth queing parameter B (offset);cnt28
  cop2r61-62 2xS16 ZSF3,ZSF4        Average Z scale factors          ;cnt29-30
  cop2r63      U20 FLAG             Returns any calculation errors   ;cnt31
```



##   GTE Registers
Note in some functions format is different from the one that's given here.<br/>

#### Matrix Registers
```
  Rotation matrix (RT)   Light matrix (LLM)     Light Color matrix (LCM)
  cop2r32.lsbs=RT11      cop2r40.lsbs=L11       cop2r48.lsbs=LR1
  cop2r32.msbs=RT12      cop2r40.msbs=L12       cop2r48.msbs=LR2
  cop2r33.lsbs=RT13      cop2r41.lsbs=L13       cop2r49.lsbs=LR3
  cop2r33.msbs=RT21      cop2r41.msbs=L21       cop2r49.msbs=LG1
  cop2r34.lsbs=RT22      cop2r42.lsbs=L22       cop2r50.lsbs=LG2
  cop2r34.msbs=RT23      cop2r42.msbs=L23       cop2r50.msbs=LG3
  cop2r35.lsbs=RT31      cop2r43.lsbs=L31       cop2r51.lsbs=LB1
  cop2r35.msbs=RT32      cop2r43.msbs=L32       cop2r51.msbs=LB2
  cop2r36     =RT33      cop2r44     =L33       cop2r52     =LB3
```
Each element is 16bit (1bit sign, 3bit integer, 12bit fraction). Reading the
last elements (RT33,L33,LB3) returns the 16bit value sign-expanded to 32bit.<br/>

#### Translation Vector (TR) (Input, R/W?)
```
  cop2r37 (cnt5) - TRX - Translation vector X (R/W?)
  cop2r38 (cnt6) - TRY - Translation vector Y (R/W?)
  cop2r39 (cnt7) - TRZ - Translation vector Z (R/W?)
```
Each element is 32bit (1bit sign, 31bit integer).<br/>
Used only for MVMVA, RTPS, RTPT commands.<br/>

#### Background Color (BK) (Input?, R/W?)
```
  cop2r45 (cnt13) - RBK - Background color red component
  cop2r46 (cnt14) - GBK - Background color green component
  cop2r47 (cnt15) - BBK - Background color blue component
```
Each element is 32bit (1bit sign, 19bit integer, 12bit fraction).<br/>

#### Far Color (FC) (Input?) (R/W?)
```
  cop2r53 (cnt21) - RFC - Far color red component
  cop2r54 (cnt22) - GFC - Far color green component
  cop2r55 (cnt23) - BFC - Far color blue component
```
Each element is 32bit (1bit sign, 27bit integer, 4bit fraction).<br/>

#### Screen Offset and Distance (Input, R/W?)
```
  cop2r56 (cnt24) - OFX - Screen offset X
  cop2r57 (cnt25) - OFY - Screen offset Y
  cop2r58 (cnt26) - H   - Projection plane distance
  cop2r59 (cnt27) - DQA - Depth queing parameter A.(coeff.)
  cop2r60 (cnt28) - DQB - Depth queing parameter B.(offset.)
```
The X and Y values are each 32bit (1bit sign, 15bit integer, 16bit fraction).<br/>
The H value is 16bit unsigned (0bit sign, 16bit integer, 0bit fraction). BUG:
When reading the H register, the hardware does accidently \<sign-expand\>
the \<unsigned\> 16bit value (ie. values +8000h..+FFFFh are returned as
FFFF8000h..FFFFFFFFh) (this bug applies only to "mov rd,cop2r58" opcodes; the
actual calculations via RTPS/RTPT opcodes are working okay).<br/>
The DQA value is only 16bit (1bit sign, 7bit integer, 8bit fraction).<br/>
The DQB value is 32bit (1bit sign, 7bit integer, 24bit? fraction).<br/>
Used only for RTPS/RTPT commands.<br/>

#### Average Z Registers (ZSF3/ZSF4=Input, R/W?) (OTZ=Result, R)
```
  cop2r61 (cnt29) ZSF3 |  0|ZSF3 1,3,12| Z3 average scale factor (normally 1/3)
  cop2r62 (cnt30) ZSF4 |  0|ZSF4 1,3,12| Z4 average scale factor (normally 1/4)
  cop2r7       OTZ (R) |   |OTZ 0,15, 0| Average Z value (for Ordering Table)
```
Used only for AVSZ3/AVSZ4 commands.<br/>

#### Screen XYZ Coordinate FIFOs
```
  cop2r12 - SXY0  rw|SY0 1,15, 0|SX0 1,15, 0| Screen XY fifo (older)
  cop2r13 - SXY1  rw|SY1 1,15, 0|SX1 1,15, 0| Screen XY fifo (old)
  cop2r14 - SXY2  rw|SY2 1,15, 0|SX2 1,15, 0| Screen XY fifo (new)
  cop2r15 - SXYP  rw|SYP 1,15, 0|SXP 1,15, 0| SXY2-mirror with move-on-write
  cop2r16 - SZ0   rw|          0|SZ0 0,16, 0| Screen Z fifo (oldest)
  cop2r17 - SZ1   rw|          0|SZ1 0,16, 0| Screen Z fifo (older)
  cop2r18 - SZ2   rw|          0|SZ2 0,16, 0| Screen Z fifo (old)
  cop2r19 - SZ3   rw|          0|SZ3 0,16, 0| Screen Z fifo (new)
```
SX,SY,SZ are used as Output for RTPS/RTPT. Additionally, SX,SY are used as
Input for NCLIP, and SZ is used as Input for AVSZ3/AVSZ4.<br/>
The SZn Fifo has 4 stages (required for AVSZ4 command), the SXYn Fifo has only
3 stages, and a special mirrored register: SXYP is a mirror of SXY2, the
difference is that writing to SXYP moves SXY2/SXY1 to SXY1/SXY0, whilst writing
to SXY2 (or any other SXYn or SZn registers) changes only the written register,
but doesn't move any other Fifo entries.<br/>

#### 16bit Vectors (R/W)
```
  Vector 0 (V0)         Vector 1 (V1)       Vector 2 (V2)       Vector 3 (IR)
  cop2r0.lsbs - VX0     cop2r2.lsbs - VX1   cop2r4.lsbs - VX2   cop2r9  - IR1
  cop2r0.msbs - VY0     cop2r2.msbs - VY1   cop2r4.msbs - VY2   cop2r10 - IR2
  cop2r1      - VZ0     cop2r3      - VZ1   cop2r5      - VZ2   cop2r11 - IR3
```
All elements are signed 16bit. The IRn and VZn elements occupy a whole 32bit
register, reading these registers returns the 16bit value sign-expanded to
32bit. Note: IRn can be also indirectly accessed via IRGB/ORGB registers.<br/>

#### Color Register and Color FIFO
```
  cop2r6  - RGBC  rw|CODE |B    |G    |R    | Color/code
  cop2r20 - RGB0  rw|CD0  |B0   |G0   |R0   | Characteristic color fifo.
  cop2r21 - RGB1  rw|CD1  |B1   |G1   |R1   |
  cop2r22 - RGB2  rw|CD2  |B2   |G2   |R2   |
  cop2r23 - (RES1)  |                       | Prohibited
```
RES1 seems to be unused... looks like an unused Fifo stage... RES1 is
read/write-able... unlike SXYP (for SXYn Fifo) it does not mirror to RGB2, nor
does it have a move-on-write function...<br/>

#### Interpolation Factor
```
  cop2r8   IR0   rw|Sign       |IR0 1, 3,12| Intermediate value 0.
```
Used as Output for RTPS/RTPT, and as Input for various commands.<br/>

#### XX...
```
  cop2r24  MAC0  rw|MAC0 1,31,0            | Sum of products value 0
```

#### XX...
```
  cop2r25  MAC1  rw|MAC1 1,31,0            | Sum of products value 1
  cop2r26  MAC2  rw|MAC2 1,31,0            | Sum of products value 2
  cop2r27  MAC3  rw|MAC3 1,31,0            | Sum of products value 3
```

#### cop2r28 - IRGB - Color conversion Input (R/W)
Expands 5:5:5 bit RGB (range 0..1Fh) to 16:16:16 bit RGB (range 0000h..0F80h).<br/>
```
  0-4    Red   (0..1Fh) (R/W)  ;multiplied by 80h, and written to IR1
  5-9    Green (0..1Fh) (R/W)  ;multiplied by 80h, and written to IR2
  10-14  Blue  (0..1Fh) (R/W)  ;multiplied by 80h, and written to IR3
  15-31  Not used (always zero) (Read only)
```
After writing to IRGB, the result can be read from IR3 after TWO nop's, and
from IR1,IR2 after THREE nop's (for uncached code, ONE nop would work). When
using IR1,IR2,IR3 as parameters for GTE commands, similar timing restrictions
might apply... depending on when the specific commands use the parameters?<br/>

#### cop2r29 - ORGB - Color conversion Output (R)
Collapses 16:16:16 bit RGB (range 0000h..0F80h) to 5:5:5 bit RGB (range
0..1Fh). Negative values (8000h..FFFFh/80h) are saturated to 00h, large
positive values (1000h..7FFFh/80h) are saturated to 1Fh, there are no overflow
or saturation flags set in cop2r63 though.<br/>
```
  0-4    Red   (0..1Fh) (R)  ;IR1 divided by 80h, saturated to +00h..+1Fh
  5-9    Green (0..1Fh) (R)  ;IR2 divided by 80h, saturated to +00h..+1Fh
  10-14  Blue  (0..1Fh) (R)  ;IR3 divided by 80h, saturated to +00h..+1Fh
  15-31  Not used (always zero) (Read only)
```
Any changes to IR1,IR2,IR3 are reflected to this register (and, actually also
to IRGB) (ie. ORGB is simply a read-only mirror of IRGB).<br/>

#### cop2r30 - LZCS - Count Leading Bits Source data (R/W)
#### cop2r31 - LZCR - Count Leading Bits Result (R)
Reading LZCR returns the leading 0 count of LZCS if LZCS is positive and the
leading 1 count of LZCS if LZCS is negative. The results are in range 1..32.<br/>

#### cop2r63 (cnt31) - FLAG - Returns any calculation errors.
See GTE Saturation chapter.<br/>



##   GTE Saturation
Maths overflows are indicated in FLAG register. In most cases, the result is
saturated to MIN/MAX values (except MAC0,MAC1,MAC2,MAC3 which aren't
saturated). For IR1,IR2,IR3 many commands allow to select the MIN value via
"lm" bit of the GTE opcode (though not all commands, RTPS/RTPT always act as if
lm=0).<br/>

#### cop2r63 (cnt31) - FLAG - Returns any calculation errors.
```
  31   Error Flag (Bit30..23, and 18..13 ORed together) (Read only)
  30   MAC1 Result larger than 43 bits and positive
  29   MAC2 Result larger than 43 bits and positive
  28   MAC3 Result larger than 43 bits and positive
  27   MAC1 Result larger than 43 bits and negative
  26   MAC2 Result larger than 43 bits and negative
  25   MAC3 Result larger than 43 bits and negative
  24   IR1 saturated to +0000h..+7FFFh (lm=1) or to -8000h..+7FFFh (lm=0)
  23   IR2 saturated to +0000h..+7FFFh (lm=1) or to -8000h..+7FFFh (lm=0)
  22   IR3 saturated to +0000h..+7FFFh (lm=1) or to -8000h..+7FFFh (lm=0)
  21   Color-FIFO-R saturated to +00h..+FFh
  20   Color-FIFO-G saturated to +00h..+FFh
  19   Color-FIFO-B saturated to +00h..+FFh
  18   SZ3 or OTZ saturated to +0000h..+FFFFh
  17   Divide overflow. RTPS/RTPT division result saturated to max=1FFFFh
  16   MAC0 Result larger than 31 bits and positive
  15   MAC0 Result larger than 31 bits and negative
  14   SX2 saturated to -0400h..+03FFh
  13   SY2 saturated to -0400h..+03FFh
  12   IR0 saturated to +0000h..+1000h
  0-11 Not used (always zero) (Read only)
```
Bit30-12 are read/write-able, ie. they can be set/reset by software, however,
that's normally not required - all bits are automatically reset at the begin of
a new GTE command.<br/>
Bit31 is apparently intended for RTPS/RTPT commands, since it triggers only on
flags that are affected by these two commands, but even for that commands it's
totally useless since one could as well check if FLAG is nonzero.<br/>
Note: Writing 32bit values to 16bit GTE registers by software does not trigger
any overflow/saturation flags (and does not do any saturation), eg. writing
12008900h (positive 32bit) to a signed 16bit register sets that register to
FFFF8900h (negative 16bit).<br/>



##   GTE Opcode Summary
#### GTE Command Summary (sorted by Real Opcode bits) (bit0-5)
```
  Opc  Name   Clk Expl.
  00h  -          N/A (modifies similar registers than RTPS...)
  01h  RTPS   15  Perspective Transformation single
  0xh  -          N/A
  06h  NCLIP  8   Normal clipping
  0xh  -          N/A
  0Ch  OP(sf) 6   Outer product of 2 vectors
  0xh  -          N/A
  10h  DPCS   8   Depth Cueing single
  11h  INTPL  8   Interpolation of a vector and far color vector
  12h  MVMVA  8   Multiply vector by matrix and add vector (see below)
  13h  NCDS   19  Normal color depth cue single vector
  14h  CDP    13  Color Depth Que
  15h  -          N/A
  16h  NCDT   44  Normal color depth cue triple vectors
  1xh  -          N/A
  1Bh  NCCS   17  Normal Color Color single vector
  1Ch  CC     11  Color Color
  1Dh  -          N/A
  1Eh  NCS    14  Normal color single
  1Fh  -          N/A
  20h  NCT    30  Normal color triple
  2xh  -          N/A
  28h  SQR(sf)5   Square of vector IR
  29h  DCPL   8   Depth Cue Color light
  2Ah  DPCT   17  Depth Cueing triple (should be fake=08h, but isn't)
  2xh  -          N/A
  2Dh  AVSZ3  5   Average of three Z values
  2Eh  AVSZ4  6   Average of four Z values
  2Fh  -          N/A
  30h  RTPT   23  Perspective Transformation triple
  3xh  -          N/A
  3Dh  GPF(sf)5   General purpose interpolation
  3Eh  GPL(sf)5   General purpose interpolation with base
  3Fh  NCCT   39  Normal Color Color triple vector
```
Unknown if/what happens when using the "N/A" opcodes?<br/>

#### GTE Command Summary (sorted by Fake Opcode bits) (bit20-24)
The fake opcode number in bit20-24 has absolutely no effect on the hardware, it
seems to be solely used to (or not to) confuse developers. Having the opcodes
sorted by their fake numbers gives a more or less well arranged list:<br/>
```
  Fake Name   Clk Expl.
  00h  -          N/A
  01h  RTPS   15  Perspective Transformation single
  02h  RTPT   23  Perspective Transformation triple
  03h  -          N/A
  04h  MVMVA  8   Multiply vector by matrix and add vector (see below)
  05h  -          N/A
  06h  DCPL   8   Depth Cue Color light
  07h  DPCS   8   Depth Cueing single
  08h  DPCT   17  Depth Cueing triple (should be fake=08h, but isn't)
  09h  INTPL  8   Interpolation of a vector and far color vector
  0Ah  SQR(sf)5   Square of vector IR
  0Bh  -          N/A
  0Ch  NCS    14  Normal color single
  0Dh  NCT    30  Normal color triple
  0Eh  NCDS   19  Normal color depth cue single vector
  0Fh  NCDT   44  Normal color depth cue triple vectors
  10h  NCCS   17  Normal Color Color single vector
  11h  NCCT   39  Normal Color Color triple vector
  12h  CDP    13  Color Depth Que
  13h  CC     11  Color Color
  14h  NCLIP  8   Normal clipping
  15h  AVSZ3  5   Average of three Z values
  16h  AVSZ4  6   Average of four Z values
  17h  OP(sf) 6   Outer product of 2 vectors
  18h  -          N/A
  19h  GPF(sf)5   General purpose interpolation
  1Ah  GPL(sf)5   General purpose interpolation with base
  1Bh  -          N/A
  1Ch  -          N/A
  1Dh  -          N/A
  1Eh  -          N/A
  1Fh  -          N/A
```
For the sort-effect, DCPT should use fake=08h, but Sony seems to have
accidently numbered it fake=0Fh in their devkit (giving it the same fake number
as for NCDT). Also, "Wipeout 2097" accidently uses 0140006h (fake=01h and
distorted bit18) instead of 1400006h (fake=14h) for NCLIP.<br/>

#### Additional Functions
The LZCS/LZCR registers offer a Count-Leading-Zeroes/Leading-Ones function.<br/>
The IRGB/ORGB registers allow to convert between 48bit and 15bit RGB colors.<br/>
These registers work without needing to send any COP2 commands. However, unlike
for commands (which do automatically halt the CPU when needed), one must insert
dummy opcodes between writing and reading the registers.<br/>



##   GTE Coordinate Calculation Commands
#### COP2 0180001h - 15 Cycles - RTPS - Perspective Transformation (single)
#### COP2 0280030h - 23 Cycles - RTPT - Perspective Transformation (triple)
RTPS performs final Rotate, translate and perspective transformation on vertex
V0. Before writing to the FIFOs, the older entries are moved one stage down.
RTPT is same as RTPS, but repeats for V1 and V2. The "sf" bit should be usually
set.<br/>
```
  IR1 = MAC1 = (TRX*1000h + RT11*VX0 + RT12*VY0 + RT13*VZ0) SAR (sf*12)
  IR2 = MAC2 = (TRY*1000h + RT21*VX0 + RT22*VY0 + RT23*VZ0) SAR (sf*12)
  IR3 = MAC3 = (TRZ*1000h + RT31*VX0 + RT32*VY0 + RT33*VZ0) SAR (sf*12)
  SZ3 = MAC3 SAR ((1-sf)*12)                           ;ScreenZ FIFO 0..+FFFFh
  MAC0=(((H*20000h/SZ3)+1)/2)*IR1+OFX, SX2=MAC0/10000h ;ScrX FIFO -400h..+3FFh
  MAC0=(((H*20000h/SZ3)+1)/2)*IR2+OFY, SY2=MAC0/10000h ;ScrY FIFO -400h..+3FFh
  MAC0=(((H*20000h/SZ3)+1)/2)*DQA+DQB, IR0=MAC0/1000h  ;Depth cueing 0..+1000h
```
If the result of the "(((H\*20000h/SZ3)+1)/2)" division is greater than 1FFFFh,
then the division result is saturated to +1FFFFh, and the divide overflow bit
in the FLAG register gets set; that happens if the vertex is exceeding the
"near clip plane", ie. if it is very close to the camera (SZ3\<=H/2), exactly
at the camara position (SZ3=0), or behind the camera (negative Z coordinates
are saturated to SZ3=0). For details on the division, see:<br/>
[GTE Division Inaccuracy](geometrytransformationenginegte.md#gte-division-inaccuracy)<br/>
For "far plane clipping", one can use the SZ3 saturation flag (MaxZ=FFFFh), or
the IR3 saturation flag (MaxZ=7FFFh) (eg. used by Wipeout 2097), or one can
compare the SZ3 value with any desired MaxZ value by software.<br/>
Note: The command does saturate IR1,IR2,IR3 to -8000h..+7FFFh (regardless of lm
bit). When using RTP with sf=0, then the IR3 saturation flag (FLAG.22) gets set
\<only\> if "MAC3 SAR 12" exceeds -8000h..+7FFFh (although IR3 is saturated
when "MAC3" exceeds -8000h..+7FFFh).<br/>

#### COP2 1400006h - 8 Cycles - NCLIP - Normal clipping
```
  MAC0 =   SX0*SY1 + SX1*SY2 + SX2*SY0 - SX0*SY2 - SX1*SY0 - SX2*SY1
```
The sign of the result indicates whether the polygon coordinates are arranged
clockwise or anticlockwise (ie. whether the front side or backside is visible).
If the result is zero, then it's neither one (ie. the vertices are all arranged
in a straight line). Note: The GPU probably renders straight lines as invisble
0 pixel width lines?<br/>

#### COP2 158002Dh - 5 Cycles - AVSZ3 - Average of three Z values (for Triangles)
#### COP2 168002Eh - 6 Cycles - AVSZ4 - Average of four Z values (for Quads)
```
  MAC0 =  ZSF3*(SZ1+SZ2+SZ3)       ;for AVSZ3
  MAC0 =  ZSF4*(SZ0+SZ1+SZ2+SZ3)   ;for AVSZ4
  OTZ  =  MAC0/1000h               ;for both (saturated to 0..FFFFh)
```
Adds three or four Z values together and multplies them by a fixed point value.
The result can be used as index in the GPU's Ordering Table (OT).<br/>
[GPU Depth Ordering](graphicsprocessingunitgpu.md#gpu-depth-ordering)<br/>
The scaling factors would be usually ZSF3=N/30h and ZSF4=N/40h, where "N" is
the number of entries in the OT (max 10000h). SZn and OTZ are unsigned 16bit
values, for whatever reason ZSFn registers are signed 16bit values (negative
values would allow a negative result in MAC0, but would saturate OTZ to zero).<br/>



##   GTE General Purpose Calculation Commands
#### COP2 0400012h - 8 Cycles - MVMVA(sf,mx,v,cv,lm)
Multiply vector by matrix and vector addition.<br/>
```
  Mx = matrix specified by mx  ;RT/LLM/LCM - Rotation, light or color matrix
  Vx = vector specified by v   ;V0, V1, V2, or [IR1,IR2,IR3]
  Tx = translation vector specified by cv  ;TR or BK or Bugged/FC, or None
```
Calculation:<br/>
```
  MAC1 = (Tx1*1000h + Mx11*Vx1 + Mx12*Vx2 + Mx13*Vx3) SAR (sf*12)
  MAC2 = (Tx2*1000h + Mx21*Vx1 + Mx22*Vx2 + Mx23*Vx3) SAR (sf*12)
  MAC3 = (Tx3*1000h + Mx31*Vx1 + Mx32*Vx2 + Mx33*Vx3) SAR (sf*12)
  [IR1,IR2,IR3] = [MAC1,MAC2,MAC3]
```
Multiplies a vector with either the rotation matrix, the light matrix or the
color matrix and then adds the translation vector or background color vector.<br/>
The GTE also allows selection of the far color vector (FC), but this vector is
not added correctly by the hardware: The return values are reduced to the last
portion of the formula, ie. MAC1=(Mx13\*Vx3) SAR (sf\*12), and similar for MAC2
and MAC3, nethertheless, some bits in the FLAG register seem to be adjusted as
if the full operation would have been executed. Setting Mx=3 selects a garbage
matrix (with elements -60h, +60h, IR0, RT13, RT13, RT13, RT22, RT22, RT22).<br/>

#### COP2 0A00428h+sf\*80000h - 5 Cycles - SQR(sf) - Square vector
```
  [MAC1,MAC2,MAC3] = [IR1*IR1,IR2*IR2,IR3*IR3] SHR (sf*12)
  [IR1,IR2,IR3]    = [MAC1,MAC2,MAC3]    ;IR1,IR2,IR3 saturated to max 7FFFh
```
Calculates the square of a vector. The result is, of course, always positive,
so the "lm" flag for negative saturation has no effect.<br/>

#### COP2 170000Ch+sf\*80000h - 6 Cycles - OP(sf,lm) - Outer product of 2 vectors
```
  [MAC1,MAC2,MAC3] = [IR3*D2-IR2*D3, IR1*D3-IR3*D1, IR2*D1-IR1*D2] SAR (sf*12)
  [IR1,IR2,IR3]    = [MAC1,MAC2,MAC3]                        ;copy result
```
Calculates the cross product of two signed 16bit vectors. Note: D1,D2,D3 are
meant to be the RT11,RT22,RT33 elements of the RT matrix "misused" as vector.
lm should be usually zero.<br/>

#### LZCS/LZCR registers - ? Cycles - Count-Leading-Zeroes/Leading-Ones
The LZCS/LZCR registers offer a Count-Leading-Zeroes/Leading-Ones function.<br/>



##   GTE Color Calculation Commands
#### COP2 0C8041Eh - 14 Cycles - NCS - Normal color (single)
#### COP2 0D80420h - 30 Cycles - NCT - Normal color (triple)
#### COP2 108041Bh - 17 Cycles - NCCS - Normal Color Color (single vector)
#### COP2 118043Fh - 39 Cycles - NCCT - Normal Color Color (triple vector)
#### COP2 0E80413h - 19 Cycles - NCDS - Normal color depth cue (single vector)
#### COP2 0F80416h - 44 Cycles - NCDT - Normal color depth cue (triple vectors)
In: V0=Normal vector (for triple variants repeated with V1 and V2),
BK=Background color, RGBC=Primary color/code, LLM=Light matrix, LCM=Color
matrix, IR0=Interpolation value.<br/>
```
  [IR1,IR2,IR3] = [MAC1,MAC2,MAC3] = (LLM*V0) SAR (sf*12)
  [IR1,IR2,IR3] = [MAC1,MAC2,MAC3] = (BK*1000h + LCM*IR) SAR (sf*12)
  [MAC1,MAC2,MAC3] = [R*IR1,G*IR2,B*IR3] SHL 4          ;<--- for NCDx/NCCx
  [MAC1,MAC2,MAC3] = MAC+(FC-MAC)*IR0                   ;<--- for NCDx only
  [MAC1,MAC2,MAC3] = [MAC1,MAC2,MAC3] SAR (sf*12)       ;<--- for NCDx/NCCx
  Color FIFO = [MAC1/16,MAC2/16,MAC3/16,CODE], [IR1,IR2,IR3] = [MAC1,MAC2,MAC3]
```

#### COP2 138041Ch - 11 Cycles - CC(lm=1) - Color Color
#### COP2 1280414h - 13 Cycles - CDP(...) - Color Depth Que
In: [IR1,IR2,IR3]=Vector, RGBC=Primary color/code, LCM=Color matrix,
BK=Background color, and, for CDP, IR0=Interpolation value, FC=Far color.<br/>
```
  [IR1,IR2,IR3] = [MAC1,MAC2,MAC3] = (BK*1000h + LCM*IR) SAR (sf*12)
  [MAC1,MAC2,MAC3] = [R*IR1,G*IR2,B*IR3] SHL 4
  [MAC1,MAC2,MAC3] = MAC+(FC-MAC)*IR0                   ;<--- for CDP only
  [MAC1,MAC2,MAC3] = [MAC1,MAC2,MAC3] SAR (sf*12)
  Color FIFO = [MAC1/16,MAC2/16,MAC3/16,CODE], [IR1,IR2,IR3] = [MAC1,MAC2,MAC3]
```

#### COP2 0680029h - 8 Cycles - DCPL - Depth Cue Color light
#### COP2 0780010h - 8 Cycles - DPCS - Depth Cueing (single)
#### COP2 0x8002Ah - 17 Cycles - DPCT - Depth Cueing (triple)
#### COP2 0980011h - 8 Cycles - INTPL - Interpolation of a vector and far color
In: [IR1,IR2,IR3]=Vector, FC=Far Color, IR0=Interpolation value, CODE=MSB of
RGBC, and, for DCPL, R,G,B=LSBs of RGBC.<br/>
```
  [MAC1,MAC2,MAC3] = [R*IR1,G*IR2,B*IR3] SHL 4          ;<--- for DCPL only
  [MAC1,MAC2,MAC3] = [IR1,IR2,IR3] SHL 12               ;<--- for INTPL only
  [MAC1,MAC2,MAC3] = [R,G,B] SHL 16                     ;<--- for DPCS/DPCT
  [MAC1,MAC2,MAC3] = MAC+(FC-MAC)*IR0
  [MAC1,MAC2,MAC3] = [MAC1,MAC2,MAC3] SAR (sf*12)
  Color FIFO = [MAC1/16,MAC2/16,MAC3/16,CODE], [IR1,IR2,IR3] = [MAC1,MAC2,MAC3]
```
DPCT executes thrice, and reads the R,G,B values from RGB0 (ie. reads from the
Bottom of the Color FIFO, instead of from the RGBC register) (the CODE value is
kept read from RGBC as usually), so, after DPCT execution, the RGB0,RGB1,RGB2
Fifo entries are modified.<br/>

#### COP2 190003Dh - 5 Cycles - GPF(sf,lm) - General purpose Interpolation
#### COP2 1A0003Eh - 5 Cycles - GPL(sf,?) - General Interpolation with base
```
  [MAC1,MAC2,MAC3] = [0,0,0]                            ;<--- for GPF only
  [MAC1,MAC2,MAC3] = [MAC1,MAC2,MAC3] SHL (sf*12)       ;<--- for GPL only
  [MAC1,MAC2,MAC3] = (([IR1,IR2,IR3] * IR0) + [MAC1,MAC2,MAC3]) SAR (sf*12)
  Color FIFO = [MAC1/16,MAC2/16,MAC3/16,CODE], [IR1,IR2,IR3] = [MAC1,MAC2,MAC3]
```
Note: Although the SHL in GPL is theoretically undone by the SAR, 44bit
overflows can occur internally when sf=1.<br/>

#### Details on "MAC+(FC-MAC)\*IR0"
```
  [IR1,IR2,IR3] = (([RFC,GFC,BFC] SHL 12) - [MAC1,MAC2,MAC3]) SAR (sf*12)
  [MAC1,MAC2,MAC3] = (([IR1,IR2,IR3] * IR0) + [MAC1,MAC2,MAC3])
```
Note: Above "[IR1,IR2,IR3]=(FC-MAC)" is saturated to -8000h..+7FFFh (ie. as if
lm=0), anyways, further writes to [IR1,IR2,IR3] (within the same command) are
saturated as usually (ie. depening on lm setting).<br/>

#### Details on "(LLM\*V0) SAR (sf\*12)" and "(BK\*1000h + LCM\*IR) SAR (sf\*12)"
Works like MVMVA command (see there), but with fixed Tx/Vx/Mx parameters, the
sf/lm bits can be changed and do affect the results (although normally both
bits should be set for use with color matrices).<br/>

#### Notes
The 8bit RGB values written to the top of Color Fifo are the 32bit MACn values
divided by 16, and saturated to +00h..+FFh, and of course, the older Fifo
entries are moved downwards. Note that, at the GPU side, the meaning of the RGB
values depends on whether or not texture blending is used (for untextured
polygons FFh is max brightness) (for texture blending FFh is double brightness
and 80h is normal brightness).<br/>
The 8bit CODE value is intended to contain a GP0(20h..7Fh) Rendering command,
allowing to automatically merge the 8bit command number, with the 24bit color
value.<br/>
The IRGB/ORGB registers allow to convert between 48bit and 15bit RGB colors.<br/>
Although the result of the commands in this chapter is written to the Color
FIFO, some commands like GPF/GPL may be also used for other purposes (eg. to
scale or scale/translate single vertices).<br/>



##   GTE Division Inaccuracy
#### GTE Division Inaccuracy (for RTPS/RTPT commands)
Basically, the GTE division does (attempt to) work as so (using 33bit maths):<br/>
```
  n = (((H*20000h/SZ3)+1)/2)
```
alternatly, below would give (almost) the same result (using 32bit maths):<br/>
```
  n = ((H*10000h+SZ3/2)/SZ3)
```
in both cases, the result is saturated about as so:<br/>
```
  if n>1FFFFh or division_by_zero then n=1FFFFh, FLAG.Bit17=1, FLAG.Bit31=1
```
However, the real GTE hardware is using a fast, but less accurate division
mechanism (based on Unsigned Newton-Raphson (UNR) algorithm):<br/>
```
  if (H < SZ3*2) then                            ;check if overflow
    z = count_leading_zeroes(SZ3)                ;z=0..0Fh (for 16bit SZ3)
    n = (H SHL z)                                ;n=0..7FFF8000h
    d = (SZ3 SHL z)                              ;d=8000h..FFFFh
    u = unr_table[(d-7FC0h) SHR 7] + 101h        ;u=200h..101h
    d = ((2000080h - (d * u)) SHR 8)             ;d=10000h..0FF01h
    d = ((0000080h + (d * u)) SHR 8)             ;d=20000h..10000h
    n = min(1FFFFh, (((n*d) + 8000h) SHR 16))    ;n=0..1FFFFh
  else n = 1FFFFh, FLAG.Bit17=1, FLAG.Bit31=1    ;n=1FFFFh plus overflow flag
```
the GTE's unr\_table[000h..100h] consists of following values:<br/>
```
  FFh,FDh,FBh,F9h,F7h,F5h,F3h,F1h,EFh,EEh,ECh,EAh,E8h,E6h,E4h,E3h ;\
  E1h,DFh,DDh,DCh,DAh,D8h,D6h,D5h,D3h,D1h,D0h,CEh,CDh,CBh,C9h,C8h ; 00h..3Fh
  C6h,C5h,C3h,C1h,C0h,BEh,BDh,BBh,BAh,B8h,B7h,B5h,B4h,B2h,B1h,B0h ;
  AEh,ADh,ABh,AAh,A9h,A7h,A6h,A4h,A3h,A2h,A0h,9Fh,9Eh,9Ch,9Bh,9Ah ;/
  99h,97h,96h,95h,94h,92h,91h,90h,8Fh,8Dh,8Ch,8Bh,8Ah,89h,87h,86h ;\
  85h,84h,83h,82h,81h,7Fh,7Eh,7Dh,7Ch,7Bh,7Ah,79h,78h,77h,75h,74h ; 40h..7Fh
  73h,72h,71h,70h,6Fh,6Eh,6Dh,6Ch,6Bh,6Ah,69h,68h,67h,66h,65h,64h ;
  63h,62h,61h,60h,5Fh,5Eh,5Dh,5Dh,5Ch,5Bh,5Ah,59h,58h,57h,56h,55h ;/
  54h,53h,53h,52h,51h,50h,4Fh,4Eh,4Dh,4Dh,4Ch,4Bh,4Ah,49h,48h,48h ;\
  47h,46h,45h,44h,43h,43h,42h,41h,40h,3Fh,3Fh,3Eh,3Dh,3Ch,3Ch,3Bh ; 80h..BFh
  3Ah,39h,39h,38h,37h,36h,36h,35h,34h,33h,33h,32h,31h,31h,30h,2Fh ;
  2Eh,2Eh,2Dh,2Ch,2Ch,2Bh,2Ah,2Ah,29h,28h,28h,27h,26h,26h,25h,24h ;/
  24h,23h,22h,22h,21h,20h,20h,1Fh,1Eh,1Eh,1Dh,1Dh,1Ch,1Bh,1Bh,1Ah ;\
  19h,19h,18h,18h,17h,16h,16h,15h,15h,14h,14h,13h,12h,12h,11h,11h ; C0h..FFh
  10h,0Fh,0Fh,0Eh,0Eh,0Dh,0Dh,0Ch,0Ch,0Bh,0Ah,0Ah,09h,09h,08h,08h ;
  07h,07h,06h,06h,05h,05h,04h,04h,03h,03h,02h,02h,01h,01h,00h,00h ;/
  00h    ;<-- one extra table entry (for "(d-7FC0h)/80h"=100h)    ;-100h
```
Above can be generated as "unr\_table[i]=min(0,(40000h/(i+100h)+1)/2-101h)".<br/>
Some special cases: NNNNh/0001h uses a big multiplier (d=20000h), in practice,
this can occur only for 0000h/0001h and 0001h/0001h (due to the H\<SZ3\*2
overflow check).<br/>
The min(1FFFFh) limit is needed for cases like FE3Fh/7F20h, F015h/780Bh, etc.
(these do produce UNR result 20000h, and are saturated to 1FFFFh, but without
setting overflow FLAG bits).<br/>
