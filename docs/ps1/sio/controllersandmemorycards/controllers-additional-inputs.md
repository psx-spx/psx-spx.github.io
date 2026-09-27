#   Controllers - Additional Inputs
#### Reset Button
PSX only (not PSone). Reboots the PSX via /RESET signal. Probably including for
forcefully getting through the WHOLE BIOS Intro, making it rather
useless/annoying? No idea if it clears ALL memory during reboot?<br/>

#### CDROM Shell Open
Status bit of the CDROM controller. Can be used to sense if the shell is opened
(and also memorizes if the shell was opened since last check; allowing to sense
possible disk changes).<br/>

#### PocketStation
Memory Card with built-in LCD screen and Buttons (which can be used as
miniature handheld console). However, when it is connected to the PSX, the
buttons are vanishing in the cartridge slot, so the buttons cannot be used as
additional inputs for PSX games.<br/>

#### Serial Port PSX only (not PSone)
With an external adaptor (voltage conversion), the serial port can be used
(among others) to connect a RS232 Serial Mouse. Although, most or all
commercial games with mouse input are probably (?) supporting only Sony's Mouse
(on the controller port) (rather than standard RS232 devices on the serial
port).<br/>

#### TTY Debug Terminal
If present, the external DUART can be used for external keyboard input, at the
BIOS side, this is supported as "std\_in".<br/>
