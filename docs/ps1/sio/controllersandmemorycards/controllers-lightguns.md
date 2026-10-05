#   Lightguns
There are two different types of PSX lightguns (which are incompatible with
each other).<br/>

#### Namco Lightgun (GunCon)
Namco's Cinch-based lightguns are extracting Vsync/Hsync timings from the video
signal (via a cinch adaptor) (so they are working completely independed of
software timings).<br/>
[Lightguns - Namco (GunCon)](controllers-lightguns-namco-guncon.md#lightguns-namco-guncon)<br/>

#### Konami Lightgun (IRQ10)
Konami's IRQ10-based lightguns are using the lightgun input on the controller
slot (which requires IRQ10/timings being properly handled at software side).<br/>
[Lightguns - Konami Justifier/Hyperblaster (IRQ10)](controllers-lightguns-konami-justifier-hyperblaster-irq10.md#lightguns-konami-justifierhyperblaster-irq10)<br/>
The IRQ10-method is reportedly less accurate (although that may be just due to
bugs at software side).<br/>

#### Third-Party Lightguns
There are also a lot of unlicensed lightguns which are either IRQ10-based, or
Cinch-based, or do support both.<br/>
For example, the Blaze Scorpion supports both IRQ10 and Cinch, and it does
additionally have a rumble/vibration function; though unknown how that rumble
feature is accessed, and which games are supporting it).<br/>

#### Lightgun Games
[Lightguns - PSX Lightgun Games](controllers-lightguns-psx-lightgun-games.md#lightguns-psx-lightgun-games)<br/>

#### Compatibilty Notes (IRQ10 vs Cinch, PAL vs NTSC, Calibration)
Some lightguns are reportedly working only with PAL or only with NTSC games
(unknown which guns, and unknown what is causing problems; the IRQ10 method
should be quite hardware independed, the GunCon variant, too, although
theoretically, some GunCon guns might have problems to extract Vsync/Hsync from
either PAL or NTSC composite signals).<br/>
Lightguns from different manufacturers are reportedly returning slightly
different values, so it would be recommended to include a calibration function
in the game, using at least one calibration point (that would also resolve
different X/Y offsets caused by modifying GP1 display control registers).<br/>
Lightguns are needing to sense light from the cathode ray beam; as such they
won't work on regions of the screen that contain too dark/black graphics.<br/>
