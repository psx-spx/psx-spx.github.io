
# Home

## **IMPORTANT UPDATE**

On the 20th of August 2022, Martin surprisingly released a new version of this documentation. While this fork will try to incorporate the changes, one important footnote that got added is the following:

> I am homeless in [Hamburg](https://problemkaputt.de/homeless.htm), please help me out!

The authors of this fork thought that this deserves more than a footnote, hence this notice here.

## Home

This is a conversion/edition of Martin "nocash" Korth's Playstation specs document originally hosted at [https://problemkaputt.de/psx-spx.htm](https://problemkaputt.de/psx-spx.htm). See [https://github.com/psx-spx/psx-spx.github.io#readme](https://github.com/psx-spx/psx-spx.github.io#readme) for more details.<br />
You can also download this website as a [single-page pdf](psx-spx.pdf).

Martin is a difficult individual to reach (see [https://problemkaputt.de/email.htm](https://problemkaputt.de/email.htm), especially the part about gmail), and so far, any attempt at contacting him about collaborating on this document failed.

Therefore, no copyright or license have been properly acquired to republish and alter this document. However, since this repository will accept and proceed to issue corrections, amendments, and additions to the original work, the [fair use and derivative work doctrine](https://en.wikipedia.org/wiki/Derivative_work) is believed to be applicable in this case.

An important detail to know about this current document, as well as the original from Martin, is that it isn't a clean room reverse engineering project, as some people may seem to believe or repeat. A good chunk of the original document has been either directly copy/pasted from the confidential code and documentation from Sony, or summarized and rephrased. As this document isn't clean room, any work derived from it shouldn't be considered clean, and anyone saying otherwise is misguided at best. The reference source material, code, and documentation used to make this document can be found at [https://psx.arthus.net/sdk/Psy-Q/](https://psx.arthus.net/sdk/Psy-Q/)

To discuss the contents of this document, or hang out with likely minded people on development, hacking, and reverse engineering of Sony's first console, feel free to [join the PSX.Dev Discord Server](https://discord.gg/QByKPpH).

## How to read this

This is a reference. Each page describes one piece of hardware and assumes you came
with a question about it. If you did not, read [Memory Map](memorymap.md),
[I/O Map](iomap.md) and [CPU Specifications](cpuspecifications.md) first, then
[Interrupts](interrupts.md), [DMA Channels](dmachannels.md) and [Timers](timers.md)
before any peripheral page. The GPU, MDEC, SPU, CDROM and expansion port each have a
DMA channel of their own, and their pages do not stop to explain what that means. The
index below is grouped in that order.

### The parentheses

The section above says where this text came from, so two voices share most pages:
material quoted or paraphrased from Sony's documentation and from other people's work,
and Martin's notes on that material. The notes are usually the parentheses.

A parenthesis ending in a question mark marks doubt, and nothing more. It is not a
notation, and its form tells you nothing about what kind of doubt it is. These pages
carry several hundred of them in almost as many distinct phrasings, plus 75 occurrences
of a bare `(?)` with no wording at all. Two from the GTE page do unrelated jobs:

```
#### Background Color (BK) (Input?, R/W?)
```

asks something a short test program on a console can answer, while

```
- Event handlers or interrupts (sounds like nonsense?) (need push/pop though)
```

argues with guidance quoted from Sony, and settling it means deciding who was right.

The annotations are staying. Which claims someone doubted, and when, is part of how
this document was built. They come out one at a time by being answered: the parenthesis
is replaced with the answer and with how it was measured. The open ones are filed as
[issues](https://github.com/psx-spx/psx-spx.github.io/issues), and the ones tagged
[good first issue](https://github.com/psx-spx/psx-spx.github.io/labels/good%20first%20issue)
can be closed with a short program on a real console.

## The pages

### Start here

[Memory Map](memorymap.md)<br/>
[I/O Map](iomap.md)<br/>
[CPU Specifications](cpuspecifications.md)<br/>

### Buses, timing and traps

Read these before any peripheral page.

[Interrupts](interrupts.md)<br/>
[DMA Channels](dmachannels.md)<br/>
[Timers](timers.md)<br/>
[Memory Control](memorycontrol.md)<br/>
[Partial Word Writes](partialwordwrites.md)<br/>
[Unpredictable Things](unpredictablethings.md)<br/>

### Graphics

GPU is DMA2 and DMA6, MDEC is DMA0 and DMA1.

[Graphics Processing Unit (GPU)](graphicsprocessingunitgpu.md)<br/>
[Geometry Transformation Engine (GTE)](geometrytransformationenginegte.md)<br/>
[GTE Pipeline Timings](gtepipelinetimings.md)<br/>
[Macroblock Decoder (MDEC)](macroblockdecodermdec.md)<br/>

### Sound

SPU is DMA4.

[Sound Processing Unit (SPU)](soundprocessingunitspu.md)<br/>

### Disc

The drive is DMA3.

[CDROM Drive](cdromdrive.md)<br/>
[CDROM Format](cdromformat.md)<br/>
[CDROM File Formats](cdromfileformats.md)<br/>
[CDROM Video CDs (VCD)](cdromvideocdsvcd.md)<br/>
[CDROM Internal Info on PSX CDROM Controller](cdrominternalinfoonpsxcdromcontroller.md)<br/>

### Ports and peripherals

The expansion port is DMA5.

[Controllers and Memory Cards](controllersandmemorycards.md)<br/>
[Pocketstation](pocketstation.md)<br/>
[Serial Interfaces (SIO)](serialinterfacessio.md)<br/>
[Expansion Port (PIO)](expansionportpio.md)<br/>
[Pinouts](pinouts.md)<br/>

### System software

[Kernel (BIOS)](kernelbios.md)<br/>

### Other hardware

[Arcade Cabinets](arcadecabinets.md)<br/>
[Konami System 573](konamisystem573.md)<br/>
[Cheat Devices](cheatdevices.md)<br/>
[PSX Dev-Board Chipsets](psxdevboardchipsets.md)<br/>
[PSX Dev-Board Protocol](psxdevboardprotocol.md)<br/>
[Hardware Numbers](hardwarenumbers.md)<br/>

### About

[About &amp; Credits](aboutcredits.md)<br/>

