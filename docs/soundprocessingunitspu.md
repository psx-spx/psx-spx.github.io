#   Sound Processing Unit (SPU)
[SPU Overview](soundprocessingunitspu.md#spu-overview)<br/>
[SPU ADPCM Samples](soundprocessingunitspu.md#spu-adpcm-samples)<br/>
[SPU ADPCM Pitch](soundprocessingunitspu.md#spu-adpcm-pitch)<br/>
[SPU Volume and ADSR Generator](soundprocessingunitspu.md#spu-volume-and-adsr-generator)<br/>
[SPU Voice Flags](soundprocessingunitspu.md#spu-voice-flags)<br/>
[SPU Noise Generator](soundprocessingunitspu.md#spu-noise-generator)<br/>
[SPU Control and Status Register](soundprocessingunitspu.md#spu-control-and-status-register)<br/>
[SPU Memory Access](soundprocessingunitspu.md#spu-memory-access)<br/>
[SPU Interrupt](soundprocessingunitspu.md#spu-interrupt)<br/>
[SPU Reverb Registers](soundprocessingunitspu.md#spu-reverb-registers)<br/>
[SPU Reverb Formula](soundprocessingunitspu.md#spu-reverb-formula)<br/>
[SPU Reverb Examples](soundprocessingunitspu.md#spu-reverb-examples)<br/>
[SPU Unknown Registers](soundprocessingunitspu.md#spu-unknown-registers)<br/>



##   SPU Overview
#### SPU I/O Port Summary
```
  1F801C00h..1F801D7Fh - Voice 0..23 Registers (eight 16bit regs per voice)
  1F801D80h..1F801D87h - SPU Control (volume)
  1F801D88h..1F801D9Fh - Voice 0..23 Flags (six 1bit flags per voice)
  1F801DA2h..1F801DBFh - SPU Control (memory, control, etc.)
  1F801DC0h..1F801DFFh - Reverb configuration area
  1F801E00h..1F801E5Fh - Voice 0..23 Internal Registers
  1F801E60h..1F801E7Fh - Unknown?
  1F801E80h..1F801FFFh - Unused?
```

#### SPU Memory layout (512Kbyte RAM)
```
  00000h-003FFh  CD Audio left  (1Kbyte) ;\CD Audio before Volume processing
  00400h-007FFh  CD Audio right (1Kbyte) ;/signed 16bit samples at 44.1kHz
  00800h-00BFFh  Voice 1 mono   (1Kbyte) ;\Voice 1 and 3 after ADSR processing
  00C00h-00FFFh  Voice 3 mono   (1Kbyte) ;/signed 16bit samples at 44.1kHz
  01000h-xxxxxh  ADPCM Samples  (first 16bytes usually contain a Sine wave)
  xxxxxh-7FFFFh  Reverb work area
```
As shown above, the first 4Kbytes are used as special capture buffers, and, if
desired, one can also use the Reverb hardware to capture output from other
voice(s).<br/>
The SPU memory is not mapped to the CPU bus, it can be accessed only via I/O,
or via DMA transfers (DMA4).<br/>

#### Voices
The SPU has 24 hardware voices. These voices can be used to reproduce sample
data, noise or can be used as frequency modulator on the next voice. Each voice
has it's own programmable ADSR envelope filter. The main volume can be
programmed independently for left and right output.<br/>

#### Voice Capabilities
All 24 voices are having exactly the same capabilities(?), with the exception
that Voice 1 and 3 are having a special Capture feature (see SPU Memory map).<br/>
There seems to be no way to produce square waves (without storing a square
wavefrom in memory... although, since SPU RAM isn't connected to the CPU bus,
the "useless" DMA for square wave data wouldn't slowdown the CPU bus)?<br/>

#### Additional Sound Inputs
External Audio can be input (from the Expansion Port?), and the CDROM drive can
be commanded to playback normal Audio CDs (via Play command), or XA-ADPCM
sectors (via Read command), and to pass that data to the SPU.<br/>

#### Unstable and Delayed I/O
The SPU occassionally seems to "miss" I/O writes (not sure if that can be fixed
by any Memory Control settings?), a stable workaround is too write all values
twice (except of course, Fifo writes). The SPU seems to process written values
at 44100Hz rate (so it may take 1/44100 seconds (300h clock cycles) until it
has actually realized the new value).<br/>

#### Mono/Stereo Audio Output
The standard PSX Audio cables have separate Left/Right signals, that is good
for stereo TVs, but, when using a normal mono TV, only one of the two audio
signals (Left or Right) can be connected. PSX programs should thus offer an
option to disable stereo effects, and to output an equal volume to both cables.<br/>

#### SPU Bus-Width
The SPU is connected to a 16bit databus. 8bit/16bit/32bit reads and 16bit/32bit
writes are implemented. However, 8bit writes are NOT implemented: 8bit writes
to ODD addresses are simply ignored (without causing any exceptions), 8bit
writes to EVEN addresses are executed as 16bit writes (eg. "movp r1,12345678h,
movb [spu\_port],r1" will write 5678h instead of 78h).<br/>



##   SPU ADPCM Samples
The SPU supports only ADPCM compressed samples (uncompressed samples seem to be
totally unsupported; leaving apart that one can write uncompressed 16bit PCM
samples to the Reverb Buffer, which can be then output at 22050Hz, as long as
they aren't overwritten by the hardware).<br/>

#### 1F801C06h+N\*10h - Voice 0..23 ADPCM Start Address (R/W)
This register holds the sample start address (not the current address, ie. the
register doesn't increment during playback).<br/>
```
  15-0   Startaddress of sound in Sound buffer (in 8-byte units)
```
Writing to this register has no effect on the currently playing voice.<br/>
The start address is copied to the current address upon Key On.<br/>

#### 1F801C0Eh+N\*10h - Voice 0..23 ADPCM Repeat Address (R/W)
If the hardware finds an ADPCM header with Loop-Start-Bit, then it copies the
current address to the repeat addresss register.<br/>
If the hardware finds an ADPCM header with Loop-Stop-Bit, then it copies the
repeat addresss register setting to the current address; that, \<after\>
playing the current ADPCM block.<br/>
```
  15-0  Address sample loops to at end (in 8-byte units)
```
Normally, repeat works automatically via the above start/stop bits, and
software doesn't need to deal with the Repeat Address Register. However,
reading from it may be useful to sense if the hardware has reached a start bit,
and writing may be also useful in some cases, eg. to redirect a one-shot sample
(with stop-bit, but without any start-bits) to a silent-loop located elsewhere
in memory.<br/>

#### Sample Data (SPU-ADPCM)
Samples consist of one or more 16-byte blocks:<br/>
```
  00h       Shift/Filter (reportedly same as for CD-XA) (see there)
  01h       Flag Bits (see below)
  02h       Compressed Data (LSBs=1st Sample, MSBs=2nd Sample)
  03h       Compressed Data (LSBs=3rd Sample, MSBs=4th Sample)
  04h       Compressed Data (LSBs=5th Sample, MSBs=6th Sample)
  ...       ...
  0Fh       Compressed Data (LSBs=27th Sample, MSBs=28th Sample)
```

#### Flag Bits (in 2nd byte of ADPCM Header)
```
  0   Loop End    (0=No change, 1=Set ENDX flag and Jump to [1F801C0Eh+N*10h])
  1   Loop Repeat (0=Force Release and set ADSR Level to Zero; only if Bit0=1)
  2   Loop Start  (0=No change, 1=Copy current address to [1F801C0Eh+N*10h])
  3-7 Unknown    (usually 0)
```
Possible combinations for Bit0-1 are:<br/>
```
  Code 0 = Normal     (continue at next 16-byte block)
  Code 1 = End+Mute   (jump to Loop-address, set ENDX flag, Release, Env=0000h)
  Code 2 = Ignored    (same as Code 0)
  Code 3 = End+Repeat (jump to Loop-address, set ENDX flag)
```

#### Looped and One-shot Samples
The Loop Start/End flags in the ADPCM Header allow to play one or more sample
block(s) in a loop, that can be either all block(s) endless repeated, or only
the last some block(s) of the sample.<br/>
There's no way to stop the output, so a one-shot sample must be followed by
dummy block (with Loop Start/End flags both set, and all data nibbles set to
zero; so that the block gets endless repeated, but doesn't produce any sound).<br/>

#### SPU-ADPCM vs XA-ADPCM
The PSX supports two ADPCM formats: SPU-ADPCM (as described above), and
XA-ADPCM. XA-ADPCM is decompressed by the CDROM Controller, and sent directly
to the sound mixer, without needing to store the data in SPU RAM, nor needing
to use a Voice channel.<br/>
The actual decompression algorithm is the same for both formats. However, the
XA nibbles are arranged in different order, and XA uses 2x28 nibbles per block
(instead of 2x14), XA blocks can contain mono or stereo data, XA supports only
two sample rates, and, XA doesn't support looping.<br/>



##   SPU ADPCM Pitch
#### 1F801C04h+N\*10h - Voice 0..23 ADPCM Sample Rate (R/W) (VxPitch)
```
  0-15  Sample rate (0=stop, 4000h=fastest, 4001h..FFFFh=usually same as 4000h)
```
Defines the ADPCM sample rate (1000h = 44100Hz). This register (and PMON) does
affect only the ADPCM sample frequency (but not on the Noise frequency, which
is defined - and shared for all voices - in the SPUCNT register).<br/>

#### 1F801D90h - Voice 0..23 Pitch Modulation Enable Flags (PMON)
Pitch modulation allows to generate "Frequency Sweep" effects by mis-using the
amplitude from channel (x-1) as pitch factor for channel (x).<br/>
```
  0     Unknown... Unused?
  1-23  Flags for Voice 1..23 (0=Normal, 1=Modulate by Voice 0..22)
  24-31 Not used
```
For example, output a very loud 1Hz sine-wave on channel 4 (with ADSR volume
4000h, and with Left/Right volume=0; unless you actually want to output it to
the speaker). Then additionally output a 2kHz sine wave on channel 5 with
PMON.Bit5 set. The "2kHz" sound should then repeatedly sweep within 1kHz..3kHz
range (or, for a more decent sweep in 1.8kHz..2.2kHz range, drop the ADSR
volume of channel 4).<br/>

#### Pitch Counter
The pitch counter is adjusted at 44100Hz rate as follows:<br/>
```
  Step = VxPitch                  ;range +0000h..+FFFFh (0...705.6 kHz)
  IF PMON.Bit(x)=1 AND (x>0)      ;pitch modulation enable
    Factor = VxOUTX(x-1)          ;range -8000h..+7FFFh (prev voice amplitude)
    Factor = Factor+8000h         ;range +0000h..+FFFFh (factor = 0.00 .. 1.99)
    Step=SignExpand16to32(Step)   ;hardware glitch on VxPitch>7FFFh, make sign
    Step = (Step * Factor) SAR 15 ;range 0..1FFFFh (glitchy if VxPitch>7FFFh)
    Step=Step AND 0000FFFFh       ;hardware glitch on VxPitch>7FFFh, kill sign
  IF Step>3FFFh then Step=4000h   ;range +0000h..+3FFFh (0.. 176.4kHz)
  Counter = Counter + Step
```
Counter.Bit12 and up indicates the current sample (within a ADPCM block).<br/>
Counter.Bit3..11 are used as 8bit gaussian interpolation index.<br/>

#### Maximum Sound Frequency
The Mixer and DAC supports a 44.1kHz output rate (allowing to produce max
22.1kHz tones). The Reverb unit supports only half the frequency.<br/>
The pitch counter supports sample rates up to 176.4kHz. However, exceeding the
44.1kHz limit causes the hardware to skip samples (or actually: to apply
incomplete interpolation on the 'skipped' samples).<br/>
VxPitch can be theoretically 0..FFFFh (max 705.6kHz), normally 4000h..FFFFh are
simply clipped to max=4000h (176.4kHz). Except, 4000h..FFFFh could be used with
pitch modulation (as they are multiplied by 0.00..1.99 before clipping; in
practice this works only for 4000h..7FFFh; as values 8000h..FFFFh are mistaken
as signed values).<br/>

#### 4-Point Gaussian Interpolation
Interpolation is applied on the 4 most recent 16bit ADPCM samples
(new,old,older,oldest), using bit4-11 of the pitch counter as 8bit
interpolation index (i=00h..FFh):<br/>
```
  out =       ((gauss[0FFh-i] * oldest) SAR 15)
  out = out + ((gauss[1FFh-i] * older)  SAR 15)
  out = out + ((gauss[100h+i] * old)    SAR 15)
  out = out + ((gauss[000h+i] * new)    SAR 15)
```
The Gauss table contains the following values (in hex):<br/>
```
  -001h,-001h,-001h,-001h,-001h,-001h,-001h,-001h ;\
  -001h,-001h,-001h,-001h,-001h,-001h,-001h,-001h ;
  0000h,0000h,0000h,0000h,0000h,0000h,0000h,0001h ;
  0001h,0001h,0001h,0002h,0002h,0002h,0003h,0003h ;
  0003h,0004h,0004h,0005h,0005h,0006h,0007h,0007h ;
  0008h,0009h,0009h,000Ah,000Bh,000Ch,000Dh,000Eh ;
  000Fh,0010h,0011h,0012h,0013h,0015h,0016h,0018h ; entry
  0019h,001Bh,001Ch,001Eh,0020h,0021h,0023h,0025h ; 000h..07Fh
  0027h,0029h,002Ch,002Eh,0030h,0033h,0035h,0038h ;
  003Ah,003Dh,0040h,0043h,0046h,0049h,004Dh,0050h ;
  0054h,0057h,005Bh,005Fh,0063h,0067h,006Bh,006Fh ;
  0074h,0078h,007Dh,0082h,0087h,008Ch,0091h,0096h ;
  009Ch,00A1h,00A7h,00ADh,00B3h,00BAh,00C0h,00C7h ;
  00CDh,00D4h,00DBh,00E3h,00EAh,00F2h,00FAh,0101h ;
  010Ah,0112h,011Bh,0123h,012Ch,0135h,013Fh,0148h ;
  0152h,015Ch,0166h,0171h,017Bh,0186h,0191h,019Ch ;/
  01A8h,01B4h,01C0h,01CCh,01D9h,01E5h,01F2h,0200h ;\
  020Dh,021Bh,0229h,0237h,0246h,0255h,0264h,0273h ;
  0283h,0293h,02A3h,02B4h,02C4h,02D6h,02E7h,02F9h ;
  030Bh,031Dh,0330h,0343h,0356h,036Ah,037Eh,0392h ;
  03A7h,03BCh,03D1h,03E7h,03FCh,0413h,042Ah,0441h ;
  0458h,0470h,0488h,04A0h,04B9h,04D2h,04ECh,0506h ;
  0520h,053Bh,0556h,0572h,058Eh,05AAh,05C7h,05E4h ; entry
  0601h,061Fh,063Eh,065Ch,067Ch,069Bh,06BBh,06DCh ; 080h..0FFh
  06FDh,071Eh,0740h,0762h,0784h,07A7h,07CBh,07EFh ;
  0813h,0838h,085Dh,0883h,08A9h,08D0h,08F7h,091Eh ;
  0946h,096Fh,0998h,09C1h,09EBh,0A16h,0A40h,0A6Ch ;
  0A98h,0AC4h,0AF1h,0B1Eh,0B4Ch,0B7Ah,0BA9h,0BD8h ;
  0C07h,0C38h,0C68h,0C99h,0CCBh,0CFDh,0D30h,0D63h ;
  0D97h,0DCBh,0E00h,0E35h,0E6Bh,0EA1h,0ED7h,0F0Fh ;
  0F46h,0F7Fh,0FB7h,0FF1h,102Ah,1065h,109Fh,10DBh ;
  1116h,1153h,118Fh,11CDh,120Bh,1249h,1288h,12C7h ;/
  1307h,1347h,1388h,13C9h,140Bh,144Dh,1490h,14D4h ;\
  1517h,155Ch,15A0h,15E6h,162Ch,1672h,16B9h,1700h ;
  1747h,1790h,17D8h,1821h,186Bh,18B5h,1900h,194Bh ;
  1996h,19E2h,1A2Eh,1A7Bh,1AC8h,1B16h,1B64h,1BB3h ;
  1C02h,1C51h,1CA1h,1CF1h,1D42h,1D93h,1DE5h,1E37h ;
  1E89h,1EDCh,1F2Fh,1F82h,1FD6h,202Ah,207Fh,20D4h ;
  2129h,217Fh,21D5h,222Ch,2282h,22DAh,2331h,2389h ; entry
  23E1h,2439h,2492h,24EBh,2545h,259Eh,25F8h,2653h ; 100h..17Fh
  26ADh,2708h,2763h,27BEh,281Ah,2876h,28D2h,292Eh ;
  298Bh,29E7h,2A44h,2AA1h,2AFFh,2B5Ch,2BBAh,2C18h ;
  2C76h,2CD4h,2D33h,2D91h,2DF0h,2E4Fh,2EAEh,2F0Dh ;
  2F6Ch,2FCCh,302Bh,308Bh,30EAh,314Ah,31AAh,3209h ;
  3269h,32C9h,3329h,3389h,33E9h,3449h,34A9h,3509h ;
  3569h,35C9h,3629h,3689h,36E8h,3748h,37A8h,3807h ;
  3867h,38C6h,3926h,3985h,39E4h,3A43h,3AA2h,3B00h ;
  3B5Fh,3BBDh,3C1Bh,3C79h,3CD7h,3D35h,3D92h,3DEFh ;/
  3E4Ch,3EA9h,3F05h,3F62h,3FBDh,4019h,4074h,40D0h ;\
  412Ah,4185h,41DFh,4239h,4292h,42EBh,4344h,439Ch ;
  43F4h,444Ch,44A3h,44FAh,4550h,45A6h,45FCh,4651h ;
  46A6h,46FAh,474Eh,47A1h,47F4h,4846h,4898h,48E9h ;
  493Ah,498Ah,49D9h,4A29h,4A77h,4AC5h,4B13h,4B5Fh ;
  4BACh,4BF7h,4C42h,4C8Dh,4CD7h,4D20h,4D68h,4DB0h ;
  4DF7h,4E3Eh,4E84h,4EC9h,4F0Eh,4F52h,4F95h,4FD7h ; entry
  5019h,505Ah,509Ah,50DAh,5118h,5156h,5194h,51D0h ; 180h..1FFh
  520Ch,5247h,5281h,52BAh,52F3h,532Ah,5361h,5397h ;
  53CCh,5401h,5434h,5467h,5499h,54CAh,54FAh,5529h ;
  5558h,5585h,55B2h,55DEh,5609h,5632h,565Bh,5684h ;
  56ABh,56D1h,56F6h,571Bh,573Eh,5761h,5782h,57A3h ;
  57C3h,57E2h,57FFh,581Ch,5838h,5853h,586Dh,5886h ;
  589Eh,58B5h,58CBh,58E0h,58F4h,5907h,5919h,592Ah ;
  593Ah,5949h,5958h,5965h,5971h,597Ch,5986h,598Fh ;
  5997h,599Eh,59A4h,59A9h,59ADh,59B0h,59B2h,59B3h ;/
```
The PSX table is a bit different as the SNES table: Values up to 3569h are
smaller as on SNES, the remaining values are bigger as on SNES, and the width
of the PSX table entries is 4bit higher as on SNES.<br/>
The PSX table is slightly bugged: Theoretically, each four values
(gauss[000h+i], gauss[0FFh-i], gauss[100h+i], gauss[1FFh-i]) should sum up to
8000h, but in practice they do sum up to 7F7Fh..7F81h (fortunately the PSX sum
doesn't exceed the 8000h limit; meaning that the PSX interpolations won't
overflow, which has been a hardware glitch on the SNES).<br/>

#### Waveform Examples
```
  Incoming ADPCM Data ---> Interpolated Data
   _   _   _   _
  | | | | | | | |           .   .   .   .    Nibbles=79797979, Filter=0
  | | | | | | | |     ---> / \ / \ / \ / \   HALF-volume ZIGZAG-wave
  | |_| |_| |_| |_            '   '   '   '
   ___     ___
  |   |   |   |              .'.     .'.     Nibbles=77997799, Filter=0
  |   |   |   |       --->  /   \   /   \    FULL-volume SINE-wave
  |   |___|   |___         '     '.'     '.
   _______                     ___
  |       |                  .'   '.         Nibbles=77779999, Filter=0
  |       |           --->  /       \        SQUARE wave (with rounded edges)
  |       |_______         '         '.____
   _____         _             __
  |     |_     _|            .'  ''.    .'   Nibbles=7777CC44, Filter=0
  |       |___|       --->  /       '..'     CUSTOM wave-form
  |                        '
   ___     __
  |   |___|  |    _         \ ! /  .  \ ! /  Nibbles=77DE9HZK, Filter=V
  |_     ____|  _|    --->  - + -  +  - + -  SOLAR STORM wave-form
  __|   |______|___         / ! \  '  / ! \
```




##   SPU Volume and ADSR Generator
#### 1F801C08h+N\*10h - Voice 0..23 Attack/Decay/Sustain/Release (ADSR) (32bit)
```
  ____lower 16bit (at 1F801C08h+N*10h)___________________________________
  15    Attack Mode       (0=Linear, 1=Exponential)
  -     Attack Direction  (Fixed, always Increase) (until Level 7FFFh)
  14-10 Attack Shift      (0..1Fh = Fast..Slow)
  9-8   Attack Step       (0..3 = "+7,+6,+5,+4")
  -     Decay Mode        (Fixed, always Exponential)
  -     Decay Direction   (Fixed, always Decrease) (until Sustain Level)
  7-4   Decay Shift       (0..0Fh = Fast..Slow)
  -     Decay Step        (Fixed, always "-8")
  3-0   Sustain Level     (0..0Fh)  ;Level=(N+1)*800h
  ____upper 16bit (at 1F801C0Ah+N*10h)___________________________________
  31    Sustain Mode      (0=Linear, 1=Exponential)
  30    Sustain Direction (0=Increase, 1=Decrease) (until Key OFF flag)
  29    Not used?         (should be zero)
  28-24 Sustain Shift     (0..1Fh = Fast..Slow)
  23-22 Sustain Step      (0..3 = "+7,+6,+5,+4" or "-8,-7,-6,-5") (inc/dec)
  21    Release Mode      (0=Linear, 1=Exponential)
  -     Release Direction (Fixed, always Decrease) (until Level 0000h)
  20-16 Release Shift     (0..1Fh = Fast..Slow)
  -     Release Step      (Fixed, always "-8")
```
The Attack phase gets started when the software sets the voice ON flag (see
below), the hardware does then automatically go through Attack/Decay/Sustain,
and switches from Sustain to Release when the software sets the Key OFF flag.<br/>

#### 1F801D80h - Mainvolume left
#### 1F801D82h - Mainvolume right
#### 1F801C00h+N\*10h - Voice 0..23 Volume Left
#### 1F801C02h+N\*10h - Voice 0..23 Volume Right
Fixed Volume Mode (when Bit15=0):<br/>
```
  15    Must be zero      (0=Volume Mode)
  0-14  Voice volume/2    (-4000h..+3FFFh = Volume -8000h..+7FFEh)
```
Sweep Volume Mode (when Bit15=1):<br/>
```
  15    Must be set       (1=Sweep Mode)
  14    Sweep Mode        (0=Linear, 1=Exponential)
  13    Sweep Direction   (0=Increase, 1=Decrease)
  12    Sweep Phase       (0=Positive, 1=Negative)
  7-11  Not used?         (should be zero)
  6-2   Sweep Shift       (0..1Fh = Fast..Slow)
  1-0   Sweep Step        (0..3 = "+7,+6,+5,+4" or "-8,-7,-6,-5") (inc/dec)
```
Sweep is another Volume envelope, additionally to the ADSR volume envelope
(unlike ADSR, sweep can be used for stereo effects, such like blending from
left to right).<br/>
Sweep starts at the current volume (which can be set via Bit15=0, however,
caution - the Bit15=0 setting isn't applied until the next 44.1kHz cycle; so
setting the initial level with Bit15=0, followed by the sweep parameter with
Bit15=1 works only if there's a suitable delay between the two operations).
Once when sweep is started, the current volume level increases to +7FFFh, or
decreases to 0000h.<br/>
Sweep Phase should be equal to the sign of the current volume (not yet tested,
in the negative mode it does probably "increase" to -7FFFh?). The Phase bit
seems to have no effect in Exponential Decrease mode.<br/>

#### 1F801DB0h - CD Audio Input Volume (for normal CD-DA, and compressed XA-ADPCM)
#### 1F801DB4h - External Audio Input Volume
```
  0-15  Volume Left   (-8000h..+7FFFh)
  16-31 Volume Right  (-8000h..+7FFFh)
```
Note: The CDROM controller supports additional CD volume control (including
ability to convert stereo CD output to mono, or to swap left/right channels).<br/>

#### Envelope Operation depending on Shift/Step/Mode/Direction
```
  AdsrCycles = 1 SHL Max(0,ShiftValue-11)
  AdsrStep = StepValue SHL Max(0,11-ShiftValue)
  IF exponential AND increase AND AdsrLevel>6000h THEN AdsrCycles=AdsrCycles*4
  IF exponential AND decrease THEN AdsrStep=AdsrStep*AdsrLevel/8000h
  Wait(AdsrCycles)              ;cycles counted at 44.1kHz clock
  AdsrLevel=AdsrLevel+AdsrStep  ;saturated to 0..+7FFFh
```
Exponential Increase is a fake (simply changes to a slower linear increase rate
at higher volume levels).<br/>

#### 1F801C0Ch+N\*10h - Voice 0..23 Current ADSR volume (R/W)
```
  15-0  Current ADSR Volume  (0..+7FFFh) (or -8000h..+7FFFh on manual write)
```
Reportedly Release can go down to -1 (FFFFh), but that isn't true; and release
ends at 0... or does THAT depend on an END flag found in the sample-data?<br/>
The register is read/writeable, writing allows to let the ADSR generator to
"jump" to a specific volume level. But, ACTUALLY, the ADSR generator does
overwrite the setting (from another internal register) whenever applying a new
Step?!<br/>

#### 1F801DB8h - Current Main Volume Left/Right
#### 1F801E00h+voice\*04h - Voice 0..23 Current Volume Left/Right
```
  0-15  Current Volume Left  (-8000h..+7FFFh)
  16-31 Current Volume Right (-8000h..+7FFFh)
```
These are internal registers, normally not used by software (the Volume
settings are usually set via Ports 1F801D80h and 1F801C00h+N\*10h).<br/>

#### Note
Negative volumes are phase inverted, otherwise same as positive.<br/>



##   SPU Voice Flags
#### 1F801D88h - Voice 0..23 Key ON (Start Attack/Decay/Sustain) (KON) (W)
```
  0-23  Voice 0..23 On  (0=No change, 1=Start Attack/Decay/Sustain)
  24-31 Not used
```
Starts the ADSR Envelope, and automatically initializes ADSR Volume to zero,
and copies Voice Start Address to Voice Repeat Address.<br/>

#### 1F801D8Ch - Voice 0..23 Key OFF (Start Release) (KOFF) (W)
```
  0-23  Voice 0..23 Off (0=No change, 1=Start Release)
  24-31 Not used
```
For a full ADSR pattern, OFF would be usually issued in the Sustain period,
however, it can be issued at any time (eg. to abort Attack, skip the Decay and
Sustain periods, and switch immediately to Release).<br/>

#### 1F801D9Ch - Voice 0..23 ON/OFF (status) (ENDX) (R)
```
  0-23  Voice 0..23 Status (0=Newly Keyed On, 1=Reached LOOP-END)
  24-31 Not used
```
The bits get CLEARED when setting the corresponding KEY ON bits.<br/>
The bits get SET when reaching an LOOP-END flag in ADPCM header.bit0.<br/>

#### R/W
Key On and Key Off should be treated as write-only (although, reading returns
the most recently 32bit value, this doesn't doesn't provide any status
information about whether sound is on or off).<br/>
The on/off (status) (ENDX) register should be treated read-only (writing is
possible in so far that the written value can be read-back for a short moment,
however, thereafter the hardware is overwriting that value).<br/>



##   SPU Noise Generator
#### 1F801D94h - Voice 0..23 Noise mode enable (NON)
```
  0-23  Voice 0..23 Noise (0=ADPCM, 1=Noise)
  24-31 Not used
```

#### SPU Noise Generator
The signed 16bit output Level is calculated as so (repeated at 44.1kHz clock):<br/>
```
  Wait(1 cycle)          ;at 44.1kHz clock
  Timer=Timer-NoiseStep  ;subtract Step (4..7)
  ParityBit = NoiseLevel.Bit15 xor Bit12 xor Bit11 xor Bit10 xor 1
  IF Timer<0 then NoiseLevel = NoiseLevel*2 + ParityBit
  IF Timer<0 then Timer=Timer+(20000h SHR NoiseShift)  ;reload timer once
  IF Timer<0 then Timer=Timer+(20000h SHR NoiseShift)  ;reload again if needed
```
Note that the Noise frequency is solely controlled by the Shift/Step values in
SPUCNT register (the ADPCM Sample Rate has absolutely no effect on noise), so
when using noise for multiple voices, all of them are forcefully having the
same frequency; the only workaround is to store a random ADPCM pattern in SPU
RAM, which can be then used with any desired sample rate(s).<br/>



##   SPU Control and Status Register
#### 1F801DAAh - SPU Control Register (SPUCNT)
```
  15    SPU Enable              (0=Off, 1=On)       (Don't care for CD Audio)
  14    Mute SPU                (0=Mute, 1=Unmute)  (Don't care for CD Audio)
  13-10 Noise Frequency Shift   (0..0Fh = Low .. High Frequency)
  9-8   Noise Frequency Step    (0..03h = Step "4,5,6,7")
  7     Reverb Master Enable    (0=Disabled, 1=Enabled)
  6     IRQ9 Enable (0=Disabled/Acknowledge, 1=Enabled; only when Bit15=1)
  5-4   Sound RAM Transfer Mode (0=Stop, 1=ManualWrite, 2=DMAwrite, 3=DMAread)
  3     External Audio Reverb   (0=Off, 1=On)
  2     CD Audio Reverb         (0=Off, 1=On) (for CD-DA and XA-ADPCM)
  1     External Audio Enable   (0=Off, 1=On)
  0     CD Audio Enable         (0=Off, 1=On) (for CD-DA and XA-ADPCM)
```
Changes to bit0-5 aren't applied immediately; after writing to SPUCNT, it'd be
usually recommended to wait until the LSBs of SPUSTAT are updated accordingly.
Before setting a new Transfer Mode, it'd be recommended first to set the "Stop"
mode (and, again, wait until Stop is applied in SPUSTAT).<br/>

#### 1F801DAEh - SPU Status Register  (SPUSTAT) (R)
```
  15-12 Unknown/Unused (seems to be usually zero)
  11    Writing to First/Second half of Capture Buffers (0=First, 1=Second)
  10    Data Transfer Busy Flag          (0=Ready, 1=Busy)
  9     Data Transfer DMA Read Request   (0=No, 1=Yes)
  8     Data Transfer DMA Write Request  (0=No, 1=Yes)
  7     Data Transfer DMA Read/Write Request ;seems to be same as SPUCNT.Bit5
  6     IRQ9 Flag                        (0=No, 1=Interrupt Request)
  5-0   Current SPU Mode   (same as SPUCNT.Bit5-0, but, applied a bit delayed)
```
When switching SPUCNT to DMA-read mode, status bit9 and bit7 aren't set
immediately (apparently the SPU is first internally collecting the data in the
Fifo, before transferring it).<br/>
Bit11 indicates if data is currently written to the first or second half of the
four 1K-byte capture buffers (for CD Audio left/right, and voice 1/3). Note:
Bit11 works only if Bit2 and/or Bit3 of Port 1F801DACh are set.<br/>
The SPUSTAT register should be treated read-only (writing is possible in so far
that the written value can be read-back for a short moment, however, thereafter
the hardware is overwriting that value).<br/>



##   SPU Memory Access
#### 1F801DA6h - Sound RAM Data Transfer Address
```
  15-0  Address in sound buffer divided by eight
```
Used for manual write and DMA read/write SPU memory. Writing to this registers
stores the written value in 1F801DA6h, and does additional store the value
(multiplied by 8) in another internal "current address" register (that internal
register does increment during transfers, whilst the 1F801DA6h value DOESN'T
increment).<br/>

#### 1F801DA8h - Sound RAM Data Transfer Fifo
```
  15-0  Data (max 32 halfwords)
```
Used for manual-write. Not sure if it can be also used for manual read?<br/>

#### 1F801DACh - Sound RAM Data Transfer Control (should be 0004h)
```
  15-4   Unknown/no effect?                       (should be zero)
  3-1    Sound RAM Data Transfer Type (see below) (should be 2)
  0      Unknown/no effect?                       (should be zero)
```
The Transfer Type selects how data is forwarded from Fifo to SPU RAM:<br/>
```
  __Transfer Type___Halfwords in Fifo________Halfwords written to SPU RAM__
  0,1,6,7  Fill     A,B,C,D,E,F,G,H,...,X    X,X,X,X,X,X,X,X,...
  2        Normal   A,B,C,D,E,F,G,H,...,X    A,B,C,D,E,F,G,H,...
  3        Rep2     A,B,C,D,E,F,G,H,...,X    A,A,C,C,E,E,G,G,...
  4        Rep4     A,B,C,D,E,F,G,H,...,X    A,A,A,A,E,E,E,E,...
  5        Rep8     A,B,C,D,E,F,G,H,...,X    H,H,H,H,H,H,H,H,...
```
Rep2 skips the 2nd halfword, Rep4 skips 2nd..4th, Rep8 skips 1st..7th.<br/>
Fill uses only the LAST halfword in Fifo, that might be useful for memfill
purposes, although, the length is probably determined by the number of writes
to the Fifo (?) so one must still issue writes for ALL halfwords...?<br/>
Note:<br/>
The above rather bizarre results apply to WRITE mode. In READ mode, the
register causes the same halfword to be read 2/4/8 times (for rep2/4/8).<br/>

#### SPU RAM Manual Write
- Be sure that [1F801DACh] is set to 0004h<br/>
- Set SPUCNT to "Stop" (and wait until it is applied in SPUSTAT)<br/>
- Set the transfer address<br/>
- Write 1..32 halfword(s) to the Fifo<br/>
- Set SPUCNT to "Manual Write" (and wait until it is applied in SPUSTAT)<br/>
- Wait until Transfer Busy in SPUSTAT goes off (that, AFTER above apply-wait)<br/>
For multi-block transfers: Repeat the above last three steps (that is rarely
done by any games, but it is done by the BIOS intro; observe that waiting for
SPUCNT writes being applied in SPUSTAT won't work in that case (since SPUCNT
was already in manual write mode from previous block), so one must instead use
some hardcoded delay of at least 300h cycles; the BIOS is using a much longer
bizarre delay though).<br/>

#### SPU RAM DMA-Write
- Be sure that [1F801DACh] is set to 0004h<br/>
- Set SPUCNT to "Stop" (and wait until it is applied in SPUSTAT)<br/>
- Set the transfer address<br/>
- Set SPUCNT to "DMA Write" (and wait until it is applied in SPUSTAT)<br/>
- Start DMA4 at CPU Side (blocksize=10h, control=01000201h)<br/>
- Wait until DMA4 finishes (at CPU side)<br/>

#### SPU RAM Manual-Read
As by now, there's no known method for reading SPU RAM without using DMA.<br/>

#### SPU RAM DMA-Read (stable reading, with [1F801014h].bit24-27 = nonzero)
- Be sure that [1F801014h] is set to 220931E1h (bit24-27 MUST be nonzero)<br/>
- Be sure that [1F801DACh] is set to 0004h<br/>
- Set SPUCNT to "Stop" (and wait until it is applied in SPUSTAT)<br/>
- Set the transfer address<br/>
- Set SPUCNT to "DMA Read" (and wait until it is applied in SPUSTAT)<br/>
- Start DMA4 at CPU Side (blocksize=10h, control=01000200h)<br/>
- Wait until DMA4 finishes (at CPU side)<br/>

#### SPU RAM DMA-Read (unstable reading, with [1F801014h].bit24-27 = zero)
Below describes some dirt effects and some trickery to get around those dirt
effects.<br/>
```
  Below problems (and workarounds) apply ONLY if [1F801014h].bit24-27 = zero.
  Ie. below info describes what happens when [1F801014h] is mis-initialized.
  Normally one should set [1F801014h]=220931E1h (and can ignore below info).
```
With [1F801014h].bit24-27=zero, reading SPU RAM via DMA works glitchy:<br/>
The first received halfword within each block is FFFFh. So with a DMA blocksize
of 10h words (=20h halfwords), the following is received:<br/>
```
  1st block:   FFFFh, halfwords[00h..1Eh]
  2nd block:   FFFFh, halfwords[20h..3Eh]
  etc.
```
that'd theoretically match the SPU Fifo Size, but, because of the inserted
FFFFh value, the last Fifo entry isn't received, ie. halfword[1Fh,3Fh] are
lost. As a workaround, one can increase the DMA blocksize to 11h words, and
then the following is received:<br/>
```
  1st block:   FFFFh, halfwords[00h..1Eh], twice halfword[1Fh]
  2nd block:   FFFFh, halfwords[20h..3Eh], twice halfword[3Fh]
  etc.
```
this time, all data is received, but after the transfer one must still remove
the FFFFh values, and the duplicated halfwords by software. Aside from the
\<inserted\> FFFFh values there are occassionaly some unstable halfwords
ORed by FFFFh (or ORed by other garbage values), this can be fixed by using
"rep2" mode, which does then receive:<br/>
```
  1st block:   FFFFh, halfwords[00h,00h,..0Eh,0Eh], triple halfword[0Fh]
  2nd block:   FFFFh, halfwords[10h,10h,..1Eh,1Eh], triple halfword[1Fh]
  etc.
```
again, remove the first halfword (FFFFh) and the last halfword, and, take the
duplicated halfwords ANDed together. Unstable values occur only every 32
halfwords or so (probably when the SPU is simultaneously reading ADPCM data),
but do never occur on two continous halfwords, so, even if one halfword was
ORed by garbage, the other halfword is always correct, and the result of the
ANDed halfwords is 100% stable.<br/>
Note: The unstable reading does NOT occur always, when resetting the PSX a
couple of times it does occassionally boot-up with totally stable reading,
since there is no known way to activate the stable "mode" via I/O ports, the
stable/unstable behaviour does eventually depend on internal clock
dividers/multipliers, and whether they are starting in sync with the CPU or
not.<br/>
Caution: The "rep2" trick cannot be used in combination with reverb (reverb
seems to be using the Port 1F801DACh Sound RAM Data Transfer Control, too).<br/>



##   SPU Interrupt
#### 1F801DA4h - Sound RAM IRQ Address (IRQ9)
```
  15-0  Address in sound buffer divided by eight
```
See also: SPUCNT (IRQ enable/disable/acknowledge) and SPUSTAT (IRQ flag).<br/>

#### Voice Interrupt
Triggers an IRQ when a voice reads ADPCM data from the IRQ address.<br/>
Mind that ADPCM cannot be stopped (uh, except, probably they CAN be stopped, by
setting the sample rate to zero?), all voices are permanently reading data from
SPU RAM - even in Noise mode, even if the Voice Volume is zero, and even if the
ADSR pattern has finished the Release period - so even inaudible voices can
trigger IRQs. To prevent unwanted IRQs, best set all unused voices to an
endless looped dummy ADPCM block.<br/>
For stable IRQs, the IRQ address should be aligned to the 16-byte ADPCM blocks.
If if the IRQ address is in the middle of a 16-byte ADPCM block, then the IRQ
doesn't seem to trigger always (unknown why, but it seems to occassionally miss
IRQs, even if the block gets repeated several times).<br/>

#### Capture Interrupt
Setting the IRQ address to 0000h..01FFh (aka byte address 00000h..00FFFh) will
trigger IRQs on writes to the four capture buffers. Each of the four buffers
contains 400h bytes (=200h samples), so the IRQ rate will be around 86.13Hz
(44100Hz/200h).<br/>
CD-Audio capture is always active (even CD-Audio output is disabld in SPUCNT,
and even if the drive door is open). Voice capture is (probably) also always
active (even if the corresponding voice is off).<br/>
Capture IRQs do NOT occur if 1F801DACh.bit3-2 are both zero.<br/>

#### Reverb Interrupt
Reverb is also triggering interrupts if the IRQ address is located in the
reverb buffer area. Unknown \<which\> of the various reverb read(s) and/or
reverb write(s) are triggering interrupts.<br/>

#### Data Transfers
Data Transfers (usually via DMA4) to/from SPU-RAM do also trap SPU interrupts.<br/>

#### Note
IRQ Address is used by Metal Gear Solid, Legend of Mana, Tokimeki Memorial 2,
Crash Team Racing, The Misadventures of Tron Bonne, and (somewhat?) by Need For
Speed 3.<br/>



##   SPU Reverb Registers
#### Reverb Volume and Address Registers (R/W)
```
  Port      Reg   Name    Type    Expl.
  1F801D84h spu   vLOUT   volume  Reverb Output Volume Left
  1F801D86h spu   vROUT   volume  Reverb Output Volume Right
  1F801DA2h spu   mBASE   base    Reverb Work Area Start Address in Sound RAM
  1F801DC0h rev00 dAPF1   disp    Reverb APF Offset 1
  1F801DC2h rev01 dAPF2   disp    Reverb APF Offset 2
  1F801DC4h rev02 vIIR    volume  Reverb Reflection Volume 1
  1F801DC6h rev03 vCOMB1  volume  Reverb Comb Volume 1
  1F801DC8h rev04 vCOMB2  volume  Reverb Comb Volume 2
  1F801DCAh rev05 vCOMB3  volume  Reverb Comb Volume 3
  1F801DCCh rev06 vCOMB4  volume  Reverb Comb Volume 4
  1F801DCEh rev07 vWALL   volume  Reverb Reflection Volume 2
  1F801DD0h rev08 vAPF1   volume  Reverb APF Volume 1
  1F801DD2h rev09 vAPF2   volume  Reverb APF Volume 2
  1F801DD4h rev0A mLSAME  src/dst Reverb Same Side Reflection Address 1 Left
  1F801DD6h rev0B mRSAME  src/dst Reverb Same Side Reflection Address 1 Right
  1F801DD8h rev0C mLCOMB1 src     Reverb Comb Address 1 Left
  1F801DDAh rev0D mRCOMB1 src     Reverb Comb Address 1 Right
  1F801DDCh rev0E mLCOMB2 src     Reverb Comb Address 2 Left
  1F801DDEh rev0F mRCOMB2 src     Reverb Comb Address 2 Right
  1F801DE0h rev10 dLSAME  src     Reverb Same Side Reflection Address 2 Left
  1F801DE2h rev11 dRSAME  src     Reverb Same Side Reflection Address 2 Right
  1F801DE4h rev12 mLDIFF  src/dst Reverb Different Side Reflect Address 1 Left
  1F801DE6h rev13 mRDIFF  src/dst Reverb Different Side Reflect Address 1 Right
  1F801DE8h rev14 mLCOMB3 src     Reverb Comb Address 3 Left
  1F801DEAh rev15 mRCOMB3 src     Reverb Comb Address 3 Right
  1F801DECh rev16 mLCOMB4 src     Reverb Comb Address 4 Left
  1F801DEEh rev17 mRCOMB4 src     Reverb Comb Address 4 Right
  1F801DF0h rev18 dLDIFF  src     Reverb Different Side Reflect Address 2 Left
  1F801DF2h rev19 dRDIFF  src     Reverb Different Side Reflect Address 2 Right
  1F801DF4h rev1A mLAPF1  src/dst Reverb APF Address 1 Left
  1F801DF6h rev1B mRAPF1  src/dst Reverb APF Address 1 Right
  1F801DF8h rev1C mLAPF2  src/dst Reverb APF Address 2 Left
  1F801DFAh rev1D mRAPF2  src/dst Reverb APF Address 2 Right
  1F801DFCh rev1E vLIN    volume  Reverb Input Volume Left
  1F801DFEh rev1F vRIN    volume  Reverb Input Volume Right
```
All volume registers are signed 16bit (range -8000h..+7FFFh).<br/>
All src/dst/disp/base registers are addresses in SPU memory (divided by 8),
src/dst are relative to the current buffer address, the disp registers are
relative to src registers, the base register defines the start address of the
reverb buffer (the end address is fixed, at 7FFFEh). Writing a value to mBASE
does additionally set the current buffer address to that value.<br/>

#### 1F801D98h - Voice 0..23 Reverb mode aka Echo On (EON) (R/W)
```
  0-23  Voice 0..23 Destination (0=To Mixer, 1=To Mixer and to Reverb)
  24-31 Not used
```
Sets reverb for the channel. As soon as the sample ends, the reverb for that
channel is turned off... that's fine, but WHEN does it end?<br/>
In Reverb mode, the voice seems to output BOTH normal (immediately) AND via
Reverb (delayed).<br/>

#### Reverb Bits in SPUCNT Register (R/W)
The SPUCNT register contains a Reverb Master Enable flag, and Reverb Enable
flags for External Audio input and CD Audio input.<br/>
When the Reverb Master Enable flag is cleared, the SPU stops to write any data
to the Reverb buffer (that is useful when zero-filling the reverb buffer;
ensuring that already-zero values aren't overwritten by still-nonzero values).<br/>
However, the Reverb Master Enable flag does not disable output from Reverb
buffer to the speakers (that might be useful to output uncompressed 22050Hz
samples) (otherwise, to disable the buffer output, set the Reverb Output volume
to zero and/or zerofill the reverb buffer).<br/>



##   SPU Reverb Formula
#### Reverb Formula
```
  ___Input from Mixer (Input volume multiplied with incoming data)_____________
  Lin = vLIN * LeftInput    ;from any channels that have Reverb enabled
  Rin = vRIN * RightInput   ;from any channels that have Reverb enabled
  ____Same Side Reflection (left-to-left and right-to-right)___________________
  [mLSAME] = (Lin + [dLSAME]*vWALL - [mLSAME-2])*vIIR + [mLSAME-2]  ;L-to-L
  [mRSAME] = (Rin + [dRSAME]*vWALL - [mRSAME-2])*vIIR + [mRSAME-2]  ;R-to-R
  ___Different Side Reflection (left-to-right and right-to-left)_______________
  [mLDIFF] = (Lin + [dRDIFF]*vWALL - [mLDIFF-2])*vIIR + [mLDIFF-2]  ;R-to-L
  [mRDIFF] = (Rin + [dLDIFF]*vWALL - [mRDIFF-2])*vIIR + [mRDIFF-2]  ;L-to-R
  ___Early Echo (Comb Filter, with input from buffer)__________________________
  Lout=vCOMB1*[mLCOMB1]+vCOMB2*[mLCOMB2]+vCOMB3*[mLCOMB3]+vCOMB4*[mLCOMB4]
  Rout=vCOMB1*[mRCOMB1]+vCOMB2*[mRCOMB2]+vCOMB3*[mRCOMB3]+vCOMB4*[mRCOMB4]
  ___Late Reverb APF1 (All Pass Filter 1, with input from COMB)________________
  Lout=Lout-vAPF1*[mLAPF1-dAPF1], [mLAPF1]=Lout, Lout=Lout*vAPF1+[mLAPF1-dAPF1]
  Rout=Rout-vAPF1*[mRAPF1-dAPF1], [mRAPF1]=Rout, Rout=Rout*vAPF1+[mRAPF1-dAPF1]
  ___Late Reverb APF2 (All Pass Filter 2, with input from APF1)________________
  Lout=Lout-vAPF2*[mLAPF2-dAPF2], [mLAPF2]=Lout, Lout=Lout*vAPF2+[mLAPF2-dAPF2]
  Rout=Rout-vAPF2*[mRAPF2-dAPF2], [mRAPF2]=Rout, Rout=Rout*vAPF2+[mRAPF2-dAPF2]
  ___Output to Mixer (Output volume multiplied with input from APF2)___________
  LeftOutput  = Lout*vLOUT
  RightOutput = Rout*vROUT
  ___Finally, before repeating the above steps_________________________________
  BufferAddress = MAX(mBASE, (BufferAddress+2) AND 7FFFEh)
  Wait one 22050Hz cycle, then repeat the above stuff
```

#### Notes
The values written to memory are saturated to -8000h..+7FFFh.<br/>
The multiplication results are divided by +8000h, to fit them to 16bit range.<br/>
All memory addresses are relative to the current BufferAddress, and wrapped
within mBASE..7FFFEh when exceeding that region.<br/>
All data in the Reverb buffer consists of signed 16bit samples. The Left and
Right Reverb Buffer addresses should be choosen so that one half of the buffer
contains Left samples, and the other half Right samples (ie. the data is
L,L,L,L,... R,R,R,R,...; it is NOT interlaced like L,R,L,R,...), during
operation, when the buffer address increases, the Left half will overwrite the
older samples of the Right half, and vice-versa.<br/>
The reverb hardware spends one 44100h cycle on left calculations, and the next
44100h cycle on right calculations (unlike as shown in the above formula, where
left/right are shown simultaneously at 22050Hz).<br/>

#### Reverb Disable
SPUCNT.bit7 disables writes to reverb buffer, but reads from reverb buffer do
still occur. If vAPF2 is zero then it does simply read "Lout=[mLAPF2-dAPF2]"
and "Rout=[mRAPF2-dAPF2]". If vAPF2 is nonzero then it does additionally use
data from APF1, if vAPF1 and vAPF2 are both nonzero then it's also using data
from COMB. However, the SAME/DIFF stages aren't used when reverb is disabled.<br/>

#### Bug
vIIR works only in range -7FFFh..+7FFFh. When set to -8000h, the multiplication
by -8000h is still done correctly, but, the final result (the value written to
memory) gets negated (this is a pretty strange feature, it is NOT a simple
overflow bug, it does affect the "+[mLSAME-2]" addition; although that part
normally shouldn't be affected by the "\*vIIR" multiplication). Similar effects
might (?) occur on some other volume registers when they are set to -8000h.<br/>

#### Speed of Sound
The speed of sound is circa 340 meters per second (in dry air, at room
temperature). For example, a voice that travels to a wall at 17 meters
distance, and back to its origin, should have a delay of 0.1 seconds.<br/>



##   SPU Reverb Examples
#### Reverb Examples
Below are some Reverb examples, showing the required memory size (ie. set Port
1F801DA2h to "(80000h-size)/8"), and the Reverb register settings for Port
1F801DC0h..1F801DFFh, ie. arranged like so:<br/>
```
  dAPF1  dAPF2  vIIR   vCOMB1 vCOMB2  vCOMB3  vCOMB4  vWALL   ;1F801DC0h..CEh
  vAPF1  vAPF2  mLSAME mRSAME mLCOMB1 mRCOMB1 mLCOMB2 mRCOMB2 ;1F801DD0h..DEh
  dLSAME dRSAME mLDIFF mRDIFF mLCOMB3 mRCOMB3 mLCOMB4 mRCOMB4 ;1F801DE0h..EEh
  dLDIFF dRDIFF mLAPF1 mRAPF1 mLAPF2  mRAPF2  vLIN    vRIN    ;1F801DF0h..FEh
```
Also, don't forget to initialize Port 1F801D84h, 1F801D86h, 1F801D98h, and
SPUCNT, and to zerofill the Reverb Buffer (so that no garbage values are output
when activating reverb). For whatever reason, one MUST also initialize Port
1F801DACh (otherwise reverb stays off).<br/>

#### Room (size=26C0h bytes)
```
  007Dh,005Bh,6D80h,54B8h,BED0h,0000h,0000h,BA80h
  5800h,5300h,04D6h,0333h,03F0h,0227h,0374h,01EFh
  0334h,01B5h,0000h,0000h,0000h,0000h,0000h,0000h
  0000h,0000h,01B4h,0136h,00B8h,005Ch,8000h,8000h
```

#### Studio Small (size=1F40h bytes)
```
  0033h,0025h,70F0h,4FA8h,BCE0h,4410h,C0F0h,9C00h
  5280h,4EC0h,03E4h,031Bh,03A4h,02AFh,0372h,0266h
  031Ch,025Dh,025Ch,018Eh,022Fh,0135h,01D2h,00B7h
  018Fh,00B5h,00B4h,0080h,004Ch,0026h,8000h,8000h
```

#### Studio Medium (size=4840h bytes)
```
  00B1h,007Fh,70F0h,4FA8h,BCE0h,4510h,BEF0h,B4C0h
  5280h,4EC0h,0904h,076Bh,0824h,065Fh,07A2h,0616h
  076Ch,05EDh,05ECh,042Eh,050Fh,0305h,0462h,02B7h
  042Fh,0265h,0264h,01B2h,0100h,0080h,8000h,8000h
```

#### Studio Large (size=6FE0h bytes)
```
  00E3h,00A9h,6F60h,4FA8h,BCE0h,4510h,BEF0h,A680h
  5680h,52C0h,0DFBh,0B58h,0D09h,0A3Ch,0BD9h,0973h
  0B59h,08DAh,08D9h,05E9h,07ECh,04B0h,06EFh,03D2h
  05EAh,031Dh,031Ch,0238h,0154h,00AAh,8000h,8000h
```

#### Hall (size=ADE0h bytes)
```
  01A5h,0139h,6000h,5000h,4C00h,B800h,BC00h,C000h
  6000h,5C00h,15BAh,11BBh,14C2h,10BDh,11BCh,0DC1h
  11C0h,0DC3h,0DC0h,09C1h,0BC4h,07C1h,0A00h,06CDh
  09C2h,05C1h,05C0h,041Ah,0274h,013Ah,8000h,8000h
```

#### Half Echo (size=3C00h bytes)
```
  0017h,0013h,70F0h,4FA8h,BCE0h,4510h,BEF0h,8500h
  5F80h,54C0h,0371h,02AFh,02E5h,01DFh,02B0h,01D7h
  0358h,026Ah,01D6h,011Eh,012Dh,00B1h,011Fh,0059h
  01A0h,00E3h,0058h,0040h,0028h,0014h,8000h,8000h
```

#### Space Echo (size=F6C0h bytes)
```
  033Dh,0231h,7E00h,5000h,B400h,B000h,4C00h,B000h
  6000h,5400h,1ED6h,1A31h,1D14h,183Bh,1BC2h,16B2h
  1A32h,15EFh,15EEh,1055h,1334h,0F2Dh,11F6h,0C5Dh
  1056h,0AE1h,0AE0h,07A2h,0464h,0232h,8000h,8000h
```

#### Chaos Echo (almost infinite) (size=18040h bytes)
```
  0001h,0001h,7FFFh,7FFFh,0000h,0000h,0000h,8100h
  0000h,0000h,1FFFh,0FFFh,1005h,0005h,0000h,0000h
  1005h,0005h,0000h,0000h,0000h,0000h,0000h,0000h
  0000h,0000h,1004h,1002h,0004h,0002h,8000h,8000h
```

#### Delay (one-shot echo) (size=18040h bytes)
```
  0001h,0001h,7FFFh,7FFFh,0000h,0000h,0000h,0000h
  0000h,0000h,1FFFh,0FFFh,1005h,0005h,0000h,0000h
  1005h,0005h,0000h,0000h,0000h,0000h,0000h,0000h
  0000h,0000h,1004h,1002h,0004h,0002h,8000h,8000h
```

#### Reverb off (size=10h dummy bytes)
```
  0000h,0000h,0000h,0000h,0000h,0000h,0000h,0000h
  0000h,0000h,0001h,0001h,0001h,0001h,0001h,0001h
  0000h,0000h,0001h,0001h,0001h,0001h,0001h,0001h
  0000h,0000h,0001h,0001h,0001h,0001h,0000h,0000h
```
Note that the memory offsets should be 0001h here (not 0000h), otherwise
zerofilling the reverb buffer seems to fail (maybe because zero memory offsets
somehow cause the fill-value to mixed with the old value or so; that appears
even when reverb master enable is zero). Also, when not using reverb, Port
1F801D84h, 1F801D86h, 1F801D98h, and the SPUCNT reverb bits should be set to
zero.<br/>



##   SPU Unknown Registers
#### 1F801DA0h - Some kind of a read-only status register.. or just garbage..?
```
  0-15 Unknown?
```
Usually 9D78h, occassionaly changes to 17DAh or 108Eh for a short moment.<br/>
Other day: Usually 9CF8h, or occassionally 9CFAh.<br/>
Another day: Usually 0000h, or occassionally 4000h.<br/>

#### 1F801DBCh - 4 bytes - Unknown? (R/W)
```
  80 21 4B DF
```
Other day (dots = same as above):<br/>
```
  .. 31 .. ..
```

#### 1F801E60h - 32 bytes - Unknown? (R/W)
```
  7E 61 A9 96 47 39 F9 1E E1 E1 80 DD E8 17 7F FB
  FB BF 1D 6C 8F EC F3 04 06 23 89 45 C1 6D 31 82
```
Other day (dots = same as above):<br/>
```
  .. .. .. .. .. .. .. .. .. .. .. .. .. .. 7B ..
  .. .. .. .. .. .. .. .. 04 .. .. .. .. .. .. 86
```

The bytes at 1F801DBCh and 1F801E60h usually have the above values on
cold-boot. The registers are read/write-able, although writing any values to
them doesn't seem to have any effect on sound output. Also, the SPU doesn't
seem to modify the registers at any time during sound output, nor reverb
calculations, nor activated external audio input... the registers seem to be
just some kind of general-purpose RAM.<br/>



