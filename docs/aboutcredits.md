#   About & Credits
#### Credits
GPU.TXT by doomed/padua; based on info from K-communications &
Nagra/Blackbag<br/>
GTE.TXT by doomed@c64.org / psx.rules.org<br/>
SPU.TXT by doomed@c64.org / psx.rules.org<br/>
CDINFO.TXT by doomed with big thanks to Barubary, who rewrote a large part<br/>
SYSTEM.TXT by doomed with thanx to Herozero for breakpoint info<br/>
PS\_ENG.TXT PlayStation PAD/Memory Interface Protocol by HFB03536<br/>
IDT79R3041 Hardware User's Manual by Integrated Device Technology, Inc.<br/>
IDTR3051, R3052 RISController User's Manual by Integrated Device Technology<br/>
PSX.\* by Joshua Walker (additional details in various distorted file formats)<br/>
LIBMIRAGE by Rok; info/source code for various cdrom-image formats<br/>
psxdev.ru; cdrom sub-cpu decapping<br/>

All the contributors to the [psx-spx.github.io](https://github.com/psx-spx/psx-spx.github.io/) repo who've helped update, correct and expand this information.

#### PSXSPX homepage
http://problemkaputt.de/psx.htm       no$psx emulator/debugger<br/>
http://problemkaputt.de/psx-spx.htm   psx specs in html formal<br/>
http://problemkaputt.de/psx-spx.txt   psx specs in text formal<br/>

#### Contact
http://problemkaputt.de/email.htm (spam-shielded)<br/>




##   Index
<A HREF="#contents">Contents</A><br/>
[Memory Map](memorymap.md)<br/>
[I/O Map](iomap.md)<br/>
[Graphics Processing Unit (GPU)](graphicsprocessingunitgpu.md)<br/>
[GPU I/O Ports, DMA Channels, Commands, VRAM](graphicsprocessingunitgpu.md#gpu-io-ports-dma-channels-commands-vram)<br/>
[GPU Render Polygon Commands](graphicsprocessingunitgpu.md#gpu-render-polygon-commands)<br/>
[GPU Render Line Commands](graphicsprocessingunitgpu.md#gpu-render-line-commands)<br/>
[GPU Render Rectangle Commands](graphicsprocessingunitgpu.md#gpu-render-rectangle-commands)<br/>
[GPU Rendering Attributes](graphicsprocessingunitgpu.md#gpu-rendering-attributes)<br/>
[GPU Memory Transfer Commands](graphicsprocessingunitgpu.md#gpu-memory-transfer-commands)<br/>
[GPU Other Commands](graphicsprocessingunitgpu.md#gpu-other-commands)<br/>
[GPU Display Control Commands (GP1)](graphicsprocessingunitgpu.md#gpu-display-control-commands-gp1)<br/>
[GPU Status Register](graphicsprocessingunitgpu.md#gpu-status-register)<br/>
[GPU Versions](graphicsprocessingunitgpu.md#gpu-versions)<br/>
[GPU Depth Ordering](graphicsprocessingunitgpu.md#gpu-depth-ordering)<br/>
[GPU Video Memory (VRAM)](graphicsprocessingunitgpu.md#gpu-video-memory-vram)<br/>
[GPU Texture Caching](graphicsprocessingunitgpu.md#gpu-texture-caching)<br/>
[GPU Timings](graphicsprocessingunitgpu.md#gpu-timings)<br/>
[GPU (MISC)](graphicsprocessingunitgpu.md#gpu-misc)<br/>
[Geometry Transformation Engine (GTE)](geometrytransformationenginegte.md)<br/>
[GTE Overview](geometrytransformationenginegte.md#gte-overview)<br/>
[GTE Registers](geometrytransformationenginegte.md#gte-registers)<br/>
[GTE Saturation](geometrytransformationenginegte.md#gte-saturation)<br/>
[GTE Opcode Summary](geometrytransformationenginegte.md#gte-opcode-summary)<br/>
[GTE Coordinate Calculation Commands](geometrytransformationenginegte.md#gte-coordinate-calculation-commands)<br/>
[GTE General Purpose Calculation Commands](geometrytransformationenginegte.md#gte-general-purpose-calculation-commands)<br/>
[GTE Color Calculation Commands](geometrytransformationenginegte.md#gte-color-calculation-commands)<br/>
[GTE Division Inaccuracy](geometrytransformationenginegte.md#gte-division-inaccuracy)<br/>
[Macroblock Decoder (MDEC)](macroblockdecodermdec.md)<br/>
[MDEC I/O Ports](macroblockdecodermdec.md#mdec-io-ports)<br/>
[MDEC Commands](macroblockdecodermdec.md#mdec-commands)<br/>
[MDEC Decompression](macroblockdecodermdec.md#mdec-decompression)<br/>
[MDEC Data Format](macroblockdecodermdec.md#mdec-data-format)<br/>
[Sound Processing Unit (SPU)](soundprocessingunitspu.md)<br/>
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
[Interrupts](interrupts.md)<br/>
[DMA Channels](dmachannels.md)<br/>
[Timers](timers.md)<br/>
[CDROM Drive](cdromdrive.md)<br/>
[CDROM Controller I/O Ports](cdromdrive.md#cdrom-controller-io-ports)<br/>
[CDROM Controller Command Summary](cdromdrive.md#cdrom-controller-command-summary)<br/>
[CDROM - Control Commands](cdromdrive.md#cdrom-control-commands)<br/>
[CDROM - Seek Commands](cdromdrive.md#cdrom-seek-commands)<br/>
[CDROM - Read Commands](cdromdrive.md#cdrom-read-commands)<br/>
[CDROM - Status Commands](cdromdrive.md#cdrom-status-commands)<br/>
[CDROM - CD Audio Commands](cdromdrive.md#cdrom-cd-audio-commands)<br/>
[CDROM - Test Commands](cdromdrive.md#cdrom-test-commands)<br/>
[CDROM - Test Commands - Version, Switches, Region, Chipset, SCEx](cdromdrive.md#cdrom-test-commands-version-switches-region-chipset-scex)<br/>
[CDROM - Test Commands - Test Drive Mechanics](cdromdrive.md#cdrom-test-commands-test-drive-mechanics)<br/>
[CDROM - Test Commands - Prototype Debug Transmission](cdromdrive.md#cdrom-test-commands-prototype-debug-transmission)<br/>
[CDROM - Test Commands - Read/Write Decoder RAM and I/O Ports](cdromdrive.md#cdrom-test-commands-readwrite-decoder-ram-and-io-ports)<br/>
[CDROM - Test Commands - Read HC05 SUB-CPU RAM and I/O Ports](cdromdrive.md#cdrom-test-commands-read-hc05-sub-cpu-ram-and-io-ports)<br/>
[CDROM - Secret Unlock Commands](cdromdrive.md#cdrom-secret-unlock-commands)<br/>
[CDROM - Video CD Commands](cdromdrive.md#cdrom-video-cd-commands)<br/>
[CDROM - Mainloop/Responses](cdromdrive.md#cdrom-mainloopresponses)<br/>
[CDROM - Response Timings](cdromdrive.md#cdrom-response-timings)<br/>
[CDROM - Response/Data Queueing](cdromdrive.md#cdrom-responsedata-queueing)<br/>
[CDROM Disk Format](cdromdrive.md#cdrom-disk-format)<br/>
[CDROM Subchannels](cdromdrive.md#cdrom-subchannels)<br/>
[CDROM Sector Encoding](cdromdrive.md#cdrom-sector-encoding)<br/>
[CDROM XA Subheader, File, Channel, Interleave](cdromdrive.md#cdrom-xa-subheader-file-channel-interleave)<br/>
[CDROM XA Audio ADPCM Compression](cdromdrive.md#cdrom-xa-audio-adpcm-compression)<br/>
[CDROM ISO Volume Descriptors](cdromdrive.md#cdrom-iso-volume-descriptors)<br/>
[CDROM ISO File and Directory Descriptors](cdromdrive.md#cdrom-iso-file-and-directory-descriptors)<br/>
[CDROM ISO Misc](cdromdrive.md#cdrom-iso-misc)<br/>
[CDROM File Formats](cdromdrive.md#cdrom-file-formats)<br/>
[CDROM Protection - SCEx Strings](cdromdrive.md#cdrom-protection-scex-strings)<br/>
[CDROM Protection - Bypassing it](cdromdrive.md#cdrom-protection-bypassing-it)<br/>
[CDROM Protection - Modchips](cdromdrive.md#cdrom-protection-modchips)<br/>
[CDROM Protection - Chipless Modchips](cdromdrive.md#cdrom-protection-chipless-modchips)<br/>
[CDROM Protection - LibCrypt](cdromdrive.md#cdrom-protection-libcrypt)<br/>
[CDROM Disk Images CCD/IMG/SUB (CloneCD)](cdromdrive.md#cdrom-disk-images-ccdimgsub-clonecd)<br/>
[CDROM Disk Images CDI (DiscJuggler)](cdromdrive.md#cdrom-disk-images-cdi-discjuggler)<br/>
[CDROM Disk Images CUE/BIN/CDT (Cdrwin)](cdromdrive.md#cdrom-disk-images-cuebincdt-cdrwin)<br/>
[CDROM Disk Images MDS/MDF (Alcohol 120%)](cdromdrive.md#cdrom-disk-images-mdsmdf-alcohol-120)<br/>
[CDROM Disk Images NRG (Nero)](cdromdrive.md#cdrom-disk-images-nrg-nero)<br/>
[CDROM Disk Image/Containers CDZ](cdromdrive.md#cdrom-disk-imagecontainers-cdz)<br/>
[CDROM Disk Image/Containers ECM](cdromdrive.md#cdrom-disk-imagecontainers-ecm)<br/>
[CDROM Subchannel Images](cdromdrive.md#cdrom-subchannel-images)<br/>
[CDROM Disk Images Other Formats](cdromdrive.md#cdrom-disk-images-other-formats)<br/>
[CDROM Internal Info on PSX CDROM Controller](cdrominternalinfoonpsxcdromcontroller.md)<br/>
[CDROM Internal HC05 Instruction Set](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-hc05-instruction-set)<br/>
[CDROM Internal HC05 On-Chip I/O Ports](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-hc05-on-chip-io-ports)<br/>
[CDROM Internal HC05 On-Chip I/O Ports - Extras](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-hc05-on-chip-io-ports-extras)<br/>
[CDROM Internal HC05 I/O Port Usage in PSX](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-hc05-io-port-usage-in-psx)<br/>
[CDROM Internal HC05 Motorola Selftest Mode](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-hc05-motorola-selftest-mode)<br/>
[CDROM Internal HC05 Motorola Selftest Mode (52pin chips)](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-hc05-motorola-selftest-mode-52pin-chips)<br/>
[CDROM Internal HC05 Motorola Selftest Mode (80pin chips)](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-hc05-motorola-selftest-mode-80pin-chips)<br/>
[CDROM Internal CXD1815Q Sub-CPU Configuration Registers](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-cxd1815q-sub-cpu-configuration-registers)<br/>
[CDROM Internal CXD1815Q Sub-CPU Sector Status Registers](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-cxd1815q-sub-cpu-sector-status-registers)<br/>
[CDROM Internal CXD1815Q Sub-CPU Address Registers](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-cxd1815q-sub-cpu-address-registers)<br/>
[CDROM Internal CXD1815Q Sub-CPU Misc Registers](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-cxd1815q-sub-cpu-misc-registers)<br/>
[CDROM Internal Commands CX(0x..3x) - CXA1782BR Servo Amplifier](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-commands-cx0x3x-cxa1782br-servo-amplifier)<br/>
[CDROM Internal Commands CX(4x..Ex) - CXD2510Q Signal Processor](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-commands-cx4xex-cxd2510q-signal-processor)<br/>
[CDROM Internal Commands CX(0x..Ex) - CXD2545Q Servo/Signal Combo](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-commands-cx0xex-cxd2545q-servosignal-combo)<br/>
[CDROM Internal Commands CX(0x..Ex) - CXD2938Q Servo/Signal/SPU Combo](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-commands-cx0xex-cxd2938q-servosignalspu-combo)<br/>
[CDROM Internal Commands CX(xx) - Notes](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-commands-cxxx-notes)<br/>
[CDROM Internal Commands CX(xx) - Summary of Used CX(xx) Commands](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-commands-cxxx-summary-of-used-cxxx-commands)<br/>
[CDROM Internal Coefficients (for CXD2545Q)](cdrominternalinfoonpsxcdromcontroller.md#cdrom-internal-coefficients-for-cxd2545q)<br/>
[CDROM Video CDs (VCD)](cdromvideocdsvcd.md)<br/>
[VCD ISO Basic Files (INFO, ENTRIES, AVSEQnn, ISO Filesystem)](cdromvideocdsvcd.md#vcd-iso-basic-files-info-entries-avseqnn-iso-filesystem)<br/>
[VCD ISO Playback Control PBC Files (PSD, LOT, ITEMnnnn)](cdromvideocdsvcd.md#vcd-iso-playback-control-pbc-files-psd-lot-itemnnnn)<br/>
[VCD ISO Search Files (SCANDATA, SEARCH, TRACKS, SPICONTX)](cdromvideocdsvcd.md#vcd-iso-search-files-scandata-search-tracks-spicontx)<br/>
[VCD ISO Misc files (CAPTnn, AUDIOnn, KARINFO, PICTURES, CDI)](cdromvideocdsvcd.md#vcd-iso-misc-files-captnn-audionn-karinfo-pictures-cdi)<br/>
[VCD MPEG-1 Multiplex Stream](cdromvideocdsvcd.md#vcd-mpeg-1-multiplex-stream)<br/>
[VCD MPEG-1 Video Stream](cdromvideocdsvcd.md#vcd-mpeg-1-video-stream)<br/>
[VCD MP2 Audio Stream](cdromvideocdsvcd.md#vcd-mp2-audio-stream)<br/>
[Inflate](cdromvideocdsvcd.md#inflate)<br/>
[Inflate - Core Functions](cdromvideocdsvcd.md#inflate-core-functions)<br/>
[Inflate - Initialization & Tree Creation](cdromvideocdsvcd.md#inflate-initialization--tree-creation)<br/>
[Inflate - Headers and Checksums](cdromvideocdsvcd.md#inflate-headers-and-checksums)<br/>
[Controllers and Memory Cards](controllersandmemorycards.md)<br/>
[Controller and Memory Card I/O Ports](controllersandmemorycards.md#controller-and-memory-card-io-ports)<br/>
[Controller and Memory Card Misc](controllersandmemorycards.md#controller-and-memory-card-misc)<br/>
[Controller and Memory Card Signals](controllersandmemorycards.md#controller-and-memory-card-signals)<br/>
[Controller and Memory Card Multitap Adaptor](controllersandmemorycards.md#controller-and-memory-card-multitap-adaptor)<br/>
[Controllers - Communication Sequence](controllersandmemorycards.md#controllers-communication-sequence)<br/>
[Controllers - Standard Digital/Analog Controllers](controllersandmemorycards.md#controllers-standard-digitalanalog-controllers)<br/>
[Controllers - Mouse](controllersandmemorycards.md#controllers-mouse)<br/>
[Controllers - Racing Controllers](controllersandmemorycards.md#controllers-racing-controllers)<br/>
[Controllers - Lightguns](controllersandmemorycards.md#controllers-lightguns)<br/>
[Controllers - Lightguns - Namco (GunCon)](controllersandmemorycards.md#controllers-lightguns-namco-guncon)<br/>
[Controllers - Lightguns - Konami Justifier/Hyperblaster (IRQ10)](controllersandmemorycards.md#controllers-lightguns-konami-justifierhyperblaster-irq10)<br/>
[Controllers - Lightguns - PSX Lightgun Games](controllersandmemorycards.md#controllers-lightguns-psx-lightgun-games)<br/>
[Controllers - Rumble Configuration](controllersandmemorycards.md#controllers-rumble-configuration)<br/>
[Controllers - Dance Mats](controllersandmemorycards.md#controllers-dance-mats)<br/>
[Controllers - Fishing Controllers](controllersandmemorycards.md#controllers-fishing-controllers)<br/>
[Controllers - I-Mode Adaptor (Mobile Internet)](controllersandmemorycards.md#controllers-i-mode-adaptor-mobile-internet)<br/>
[Controllers - Additional Inputs](controllersandmemorycards.md#controllers-additional-inputs)<br/>
[Controllers - Misc](controllersandmemorycards.md#controllers-misc)<br/>
[Memory Card Read/Write Commands](controllersandmemorycards.md#memory-card-readwrite-commands)<br/>
[Memory Card Data Format](controllersandmemorycards.md#memory-card-data-format)<br/>
[Memory Card Images](controllersandmemorycards.md#memory-card-images)<br/>
[Memory Card Notes](controllersandmemorycards.md#memory-card-notes)<br/>
[Pocketstation](pocketstation.md)<br/>
[Pocketstation Overview](pocketstation.md#pocketstation-overview)<br/>
[Pocketstation I/O Map](pocketstation.md#pocketstation-io-map)<br/>
[Pocketstation Memory Map](pocketstation.md#pocketstation-memory-map)<br/>
[Pocketstation IO Video and Audio](pocketstation.md#pocketstation-io-video-and-audio)<br/>
[Pocketstation IO Interrupts and Buttons](pocketstation.md#pocketstation-io-interrupts-and-buttons)<br/>
[Pocketstation IO Timers and Real-Time Clock](pocketstation.md#pocketstation-io-timers-and-real-time-clock)<br/>
[Pocketstation IO Infrared](pocketstation.md#pocketstation-io-infrared)<br/>
[Pocketstation IO Memory-Control](pocketstation.md#pocketstation-io-memory-control)<br/>
[Pocketstation IO Communication Ports](pocketstation.md#pocketstation-io-communication-ports)<br/>
[Pocketstation IO Power Control](pocketstation.md#pocketstation-io-power-control)<br/>
[Pocketstation SWI Function Summary](pocketstation.md#pocketstation-swi-function-summary)<br/>
[Pocketstation SWI Misc Functions](pocketstation.md#pocketstation-swi-misc-functions)<br/>
[Pocketstation SWI Communication Functions](pocketstation.md#pocketstation-swi-communication-functions)<br/>
[Pocketstation SWI Execute Functions](pocketstation.md#pocketstation-swi-execute-functions)<br/>
[Pocketstation SWI Date/Time/Alarm Functions](pocketstation.md#pocketstation-swi-datetimealarm-functions)<br/>
[Pocketstation SWI Flash Functions](pocketstation.md#pocketstation-swi-flash-functions)<br/>
[Pocketstation SWI Useless Functions](pocketstation.md#pocketstation-swi-useless-functions)<br/>
[Pocketstation BU Command Summary](pocketstation.md#pocketstation-bu-command-summary)<br/>
[Pocketstation BU Standard Memory Card Commands](pocketstation.md#pocketstation-bu-standard-memory-card-commands)<br/>
[Pocketstation BU Basic Pocketstation Commands](pocketstation.md#pocketstation-bu-basic-pocketstation-commands)<br/>
[Pocketstation BU Custom Pocketstation Commands](pocketstation.md#pocketstation-bu-custom-pocketstation-commands)<br/>
[Pocketstation File Header/Icons](pocketstation.md#pocketstation-file-headericons)<br/>
[Pocketstation File Images](pocketstation.md#pocketstation-file-images)<br/>
[Pocketstation XBOO Cable](pocketstation.md#pocketstation-xboo-cable)<br/>
[Serial Port (SIO)](serialportsio.md)<br/>
[Expansion Port (PIO)](expansionportpio.md)<br/>
[EXP1 Expansion ROM Header](expansionportpio.md#exp1-expansion-rom-header)<br/>
[EXP2 Dual Serial Port (for TTY Debug Terminal)](expansionportpio.md#exp2-dual-serial-port-for-tty-debug-terminal)<br/>
[EXP2 DTL-H2000 I/O Ports](expansionportpio.md#exp2-dtl-h2000-io-ports)<br/>
[EXP2 Post Registers](expansionportpio.md#exp2-post-registers)<br/>
[EXP2 Nocash Emulation Expansion](expansionportpio.md#exp2-nocash-emulation-expansion)<br/>
[Memory Control](memorycontrol.md)<br/>
[Unpredictable Things](unpredictablethings.md)<br/>
[CPU Specifications](cpuspecifications.md)<br/>
[CPU Registers](cpuspecifications.md#cpu-registers)<br/>
[CPU Opcode Encoding](cpuspecifications.md#cpu-opcode-encoding)<br/>
[CPU Load/Store Opcodes](cpuspecifications.md#cpu-loadstore-opcodes)<br/>
[CPU ALU Opcodes](cpuspecifications.md#cpu-alu-opcodes)<br/>
[CPU Jump Opcodes](cpuspecifications.md#cpu-jump-opcodes)<br/>
[CPU Coprocessor Opcodes](cpuspecifications.md#cpu-coprocessor-opcodes)<br/>
[CPU Pseudo Opcodes](cpuspecifications.md#cpu-pseudo-opcodes)<br/>
[COP0 - Register Summary](cpuspecifications.md#cop0-register-summary)<br/>
[COP0 - Exception Handling](cpuspecifications.md#cop0-exception-handling)<br/>
[COP0 - Misc](cpuspecifications.md#cop0-misc)<br/>
[COP0 - Debug Registers](cpuspecifications.md#cop0-debug-registers)<br/>
[Kernel (BIOS)](kernelbios.md)<br/>
[BIOS Overview](kernelbios.md#bios-overview)<br/>
[BIOS Memory Map](kernelbios.md#bios-memory-map)<br/>
[BIOS Function Summary](kernelbios.md#bios-function-summary)<br/>
[BIOS File Functions](kernelbios.md#bios-file-functions)<br/>
[BIOS File Execute and Flush Cache](kernelbios.md#bios-file-execute-and-flush-cache)<br/>
[BIOS CDROM Functions](kernelbios.md#bios-cdrom-functions)<br/>
[BIOS Memory Card Functions](kernelbios.md#bios-memory-card-functions)<br/>
[BIOS Interrupt/Exception Handling](kernelbios.md#bios-interruptexception-handling)<br/>
[BIOS Event Functions](kernelbios.md#bios-event-functions)<br/>
[BIOS Event Summary](kernelbios.md#bios-event-summary)<br/>
[BIOS Thread Functions](kernelbios.md#bios-thread-functions)<br/>
[BIOS Timer Functions](kernelbios.md#bios-timer-functions)<br/>
[BIOS Joypad Functions](kernelbios.md#bios-joypad-functions)<br/>
[BIOS GPU Functions](kernelbios.md#bios-gpu-functions)<br/>
[BIOS Memory Allocation](kernelbios.md#bios-memory-allocation)<br/>
[BIOS Memory Fill/Copy/Compare (SLOW)](kernelbios.md#bios-memory-fillcopycompare-slow)<br/>
[BIOS String Functions](kernelbios.md#bios-string-functions)<br/>
[BIOS Number/String/Character Conversion](kernelbios.md#bios-numberstringcharacter-conversion)<br/>
[BIOS Misc Functions](kernelbios.md#bios-misc-functions)<br/>
[BIOS Internal Boot Functions](kernelbios.md#bios-internal-boot-functions)<br/>
[BIOS More Internal Functions](kernelbios.md#bios-more-internal-functions)<br/>
[BIOS PC File Server](kernelbios.md#bios-pc-file-server)<br/>
[BIOS TTY Console (std_io)](kernelbios.md#bios-tty-console-stdio)<br/>
[BIOS Character Sets](kernelbios.md#bios-character-sets)<br/>
[BIOS Control Blocks](kernelbios.md#bios-control-blocks)<br/>
[BIOS Versions](kernelbios.md#bios-versions)<br/>
[BIOS Patches](kernelbios.md#bios-patches)<br/>
[Arcade Cabinets](arcadecabinets.md)<br/>
[Cheat Devices](cheatdevices.md)<br/>
[Cheat Devices - Datel I/O](cheatdevices.md#cheat-devices-datel-io)<br/>
[Cheat Devices - Datel DB25 Comms Link Protocol](cheatdevices.md#cheat-devices-datel-db25-comms-link-protocol)<br/>
[Cheat Devices - Datel Chipset Pinouts](cheatdevices.md#cheat-devices-datel-chipset-pinouts)<br/>
[Cheat Devices - Datel Cheat Code Format](cheatdevices.md#cheat-devices-datel-cheat-code-format)<br/>
[Cheat Devices - Xplorer Memory and I/O Map](cheatdevices.md#cheat-devices-xplorer-memory-and-io-map)<br/>
[Cheat Devices - Xplorer DB25 Parallel Port Function Summary](cheatdevices.md#cheat-devices-xplorer-db25-parallel-port-function-summary)<br/>
[Cheat Devices - Xplorer DB25 Parallel Port Command Handler](cheatdevices.md#cheat-devices-xplorer-db25-parallel-port-command-handler)<br/>
[Cheat Devices - Xplorer DB25 Parallel Port Low Level Transfer Protocol](cheatdevices.md#cheat-devices-xplorer-db25-parallel-port-low-level-transfer-protocol)<br/>
[Cheat Devices - Xplorer Versions](cheatdevices.md#cheat-devices-xplorer-versions)<br/>
[Cheat Devices - Xplorer Chipset Pinouts](cheatdevices.md#cheat-devices-xplorer-chipset-pinouts)<br/>
[Cheat Devices - Xplorer Cheat Code Format](cheatdevices.md#cheat-devices-xplorer-cheat-code-format)<br/>
[Cheat Devices - Xplorer Cheat Code and ROM-Image Decryption](cheatdevices.md#cheat-devices-xplorer-cheat-code-and-rom-image-decryption)<br/>
[Cheat Devices - FLASH/EEPROMs](cheatdevices.md#cheat-devices-flasheeproms)<br/>
[PSX Dev-Board Chipsets](psxdevboardchipsets.md)<br/>
[Hardware Numbers](hardwarenumbers.md)<br/>
[Pinouts](pinouts.md)<br/>
[Pinouts - Controller Ports and Memory-Card Ports](pinouts.md#pinouts-controller-ports-and-memory-card-ports)<br/>
[Pinouts - Audio, Video, Power, Expansion Ports](pinouts.md#pinouts-audio-video-power-expansion-ports)<br/>
[Pinouts - SIO Pinouts](pinouts.md#pinouts-sio-pinouts)<br/>
[Pinouts - Chipset Summary](pinouts.md#pinouts-chipset-summary)<br/>
[Pinouts - CPU Pinouts](pinouts.md#pinouts-cpu-pinouts)<br/>
[Pinouts - GPU Pinouts (for old 160-pin GPU)](pinouts.md#pinouts-gpu-pinouts-for-old-160-pin-gpu)<br/>
[Pinouts - GPU Pinouts (for new 208-pin GPU)](pinouts.md#pinouts-gpu-pinouts-for-new-208-pin-gpu)<br/>
[Pinouts - SPU Pinouts](pinouts.md#pinouts-spu-pinouts)<br/>
[Pinouts - DRV Pinouts](pinouts.md#pinouts-drv-pinouts)<br/>
[Pinouts - VCD Pinouts](pinouts.md#pinouts-vcd-pinouts)<br/>
[Pinouts - HC05 Pinouts](pinouts.md#pinouts-hc05-pinouts)<br/>
[Pinouts - MEM Pinouts](pinouts.md#pinouts-mem-pinouts)<br/>
[Pinouts - CLK Pinouts](pinouts.md#pinouts-clk-pinouts)<br/>
[Pinouts - PWR Pinouts](pinouts.md#pinouts-pwr-pinouts)<br/>
[Pinouts - Component List and Chipset Pin-Outs for Digital Joypad, SCPH-1080](pinouts.md#pinouts-component-list-and-chipset-pin-outs-for-digital-joypad-scph-1080)<br/>
[Pinouts - Component List and Chipset Pin-Outs for Analog Joypad, SCPH-1150](pinouts.md#pinouts-component-list-and-chipset-pin-outs-for-analog-joypad-scph-1150)<br/>
[Pinouts - Component List and Chipset Pin-Outs for Analog Joypad, SCPH-1200](pinouts.md#pinouts-component-list-and-chipset-pin-outs-for-analog-joypad-scph-1200)<br/>
[Pinouts - Component List and Chipset Pin-Outs for Analog Joypad, SCPH-110](pinouts.md#pinouts-component-list-and-chipset-pin-outs-for-analog-joypad-scph-110)<br/>
[Pinouts - Component List and Chipset Pin-Outs for Namco Lightgun, NPC-103](pinouts.md#pinouts-component-list-and-chipset-pin-outs-for-namco-lightgun-npc-103)<br/>
[Pinouts - Component List and Chipset Pin-Outs for Multitap, SCPH-1070](pinouts.md#pinouts-component-list-and-chipset-pin-outs-for-multitap-scph-1070)<br/>
[Pinouts - Memory Cards](pinouts.md#pinouts-memory-cards)<br/>
[Mods - Nocash PSX-XBOO Upload](pinouts.md#mods-nocash-psx-xboo-upload)<br/>
[Mods - PAL/NTSC Color Mods](pinouts.md#mods-palntsc-color-mods)<br/>
[About & Credits](aboutcredits.md)<br/>

[extracted from no$psx v2.0 documentation]<br/>
</BODY></HTML>
