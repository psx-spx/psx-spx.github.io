# Pop'n Controllers
Controllers used for Konami's Pop'n Music series. At least a few different
versions of the controller (Pop'n Controller, Pop'n Controller 2, larger
arcade-size version, possibly others and in different color variations) have
been released for the PS1 and PS2. Unknown if the controllers released in the
PS2 era have any additional commands not present in the original Pop'n
Controller, but they are supposedly fully compatible with PS1 Pop'n Music games.

Pop'n Controllers report as digital controllers (ID byte 41h), but the left,
right, and down d-pad controls are not connected to any physical buttons and are
always reported as pressed (in the first transferred button byte, bits 5-7 are
always 0). Pop'n Music games check these bits to determine if a Pop'n Controller
is connected and will change the in-game controls accordingly if so.
