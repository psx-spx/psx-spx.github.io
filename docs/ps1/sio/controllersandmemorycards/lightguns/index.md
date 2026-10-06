#   Lightguns
There are two different types of PSX lightguns (which are incompatible with
each other).<br/>

#### Namco Lightgun (GunCon)
Namco's Cinch-based lightguns are extracting Vsync/Hsync timings from the video
signal (via a cinch adaptor) (so they are working completely independed of
software timings).<br/>
[Namco GunCon](namco-guncon.md#namco-guncon)<br/>

#### Konami Lightgun (IRQ10)
Konami's IRQ10-based lightguns are using the lightgun input on the controller
slot (which requires IRQ10/timings being properly handled at software side).<br/>
[Konami Justifier/Hyperblaster (IRQ10)](konami-justifier-hyperblaster.md#konami-justifierhyperblaster-irq10)<br/>
The IRQ10-method is reportedly less accurate (although that may be just due to
bugs at software side).<br/>

#### Third-Party Lightguns
There are also a lot of unlicensed lightguns which are either IRQ10-based, or
Cinch-based, or do support both.<br/>
For example, the Blaze Scorpion supports both IRQ10 and Cinch, and it does
additionally have a rumble/vibration function; though unknown how that rumble
feature is accessed, and which games are supporting it).<br/>

#### Lightgun Games
Some games are working only with IRQ10 or only with Cinch, some games support
both methods:<br/>
```
  Area 51 (Mesa Logic/Midway) (IRQ10)
  Crypt Killer (Konami) (IRQ10)
  Die Hard Trilogy 1: (Probe Entertainment) (IRQ10)
  Die Hard Trilogy 2: Viva Las Vegas (n-Space) (IRQ10/Cinch)
  Elemental Gearbolt (Working Designs) (IRQ10/Cinch)
  Extreme Ghostbusters: Ultimate Invasion (LSP) (Cinch)
  Galaxian 3 (Cinch)
  Ghoul Panic (Namco) (Cinch)
  Gunfighter: The Legend of Jesse James (Rebellion) (Cinch)
  Judge Dredd (Gremlin) (Cinch)
  Lethal Enforcers 1-2 (Konami) (IRQ10)
  Maximum Force (Midway) (IRQ10/Cinch)
  Mighty Hits Special (Altron) (EU/JPN) (Cinch)
  Moorhuhn series (Phenomedia) (Cinch)
  Point Blank 1-3 (Namco) (Cinch)
  Project Horned Owl (Sony) (IRQ10)
  Rescue Shot (Namco) (Cinch)
  Resident Evil: Gun Survivor (Capcom) (JPN/PAL versions) (Cinch)
  Silent Hill (IRQ10) ("used for an easter egg")
  Simple 1500 Series Vol.024 - The Gun Shooting (unknown type)
  Simple 1500 Series Vol.063 - The Gun Shooting 2 (unknown type)
  Snatcher (IRQ10)
  Sporting Clays (Charles Doty) (homebrew with buggy source code) (IRQ10/Cinch)
  Star Wars Rebel Assault II (IRQ10)
  Time Crisis, and Time Crisis 2: Project Titan (Namco) (Cinch)
```
Note: The RPG game Dragon Quest Monsters does also contain IRQ10 lightgun code
(though unknown if/when/where the game does use that code).<br/>

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
