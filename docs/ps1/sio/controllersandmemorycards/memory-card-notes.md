#   Memory Card Notes
#### Sony PSX Memory Cards
Sony has manufactured only 128KByte memory cards for PSX, no bigger/smaller
ones.<br/>

#### Sony PS2 Memory Cards
A special case would be PS2 cards, these are bigger, but PS2 cards won't fit
into PSX cards slots (unless when cutting an extra notch in the card edge
connector), a PSX game played on a PS2 console could theoretically access PS2
cards (if it supports the different directory structure on that cards).<br/>

#### Third Party Cards with bigger capacity
Some third party cards contain larger memory chips, however, the PSX
games/kernel are supporting only regular 128Kbyte cards, so the extra memory
can be used only by dividing it into several 128Kbyte memory card images.<br/>
Selecting a different memory card image can be done by a switch or button on
the card, or via joypad key combinations (joypad/card are sharing the same
signals, so the card could watch the traffic on joypad bus, provided that the
MIPS CPU is actually reading the joypad).<br/>

#### Third Party Cards with bigger capacity and Data Compression
Some cards are additionally using data compression to increase the card
capacity, but that techinque is having rather bad reputation and could result
in data loss. For example, if a game has allocated four blocks on the memory
card, then it'll expect to be able to overwrite that four blocks at any time
(without needing to handle "memory card full" errors), however, if the card is
full, and if the newly written data has worse compression ratio, then the card
will be unable to store the new game position (and may have already overwritten
parts of the old game position). As a workaround, such cards may use a LED to
warn users when running low on memory (ideally, there should be always at least
128Kbytes of free memory).<br/>

#### Joytech Smart Card Adaptor
The smart card adaptor plugs into memory card slot, and allows to use special
credit card-shaped memory cards. There don't seem to be any special features,
ie. the hardware setup does just behave like normal PSX memory cards.<br/>

#### Datel VMEM (virtual memory card storage on expansion port)
The Datel/Interact VMEM exists as standalone VMEM cartridge, and some Datel
Cheat Devices do also include the VMEM feature. Either way, the VMEM connects
to expansion port, and contain some large FLASH memory, for storing multiple
memory cards on it. Unknown, how that memory is accessed (maybe it must be
copied to a regular memory card, or maybe they've somehow hooked the Kernel (or
even the hardware signals?) so that games could directly access the VMEM?<br/>

#### Passwords (instead of Memory Cards)
Some older games are using passwords instead of memory cards to allow the user
to continue at certain game positions. That's nice for people without memory
card, but unfortunately many of that games are restricted to it - it'd be more
user friendly to support both passwords, and, optionally, memory cards.<br/>

#### Yaroze Access Cards (DTL-H3020)
The Yaroze Access Card connects to memory card slot, the card resembles regular
memory cards, but it doesn't contain any storage memory. Instead, it does
merely support a very basic Access Card detection command:<br/>
```
  Send Reply Comment
  21h  N/A?  Probably replies HighZ (ie. probably reads FFh)?
  53h  0xh?  Replies unknown 8bit value (upper 4bit are known to be zero)?
```
Ie. when receiving 21h as first byte, it replies by an ACK, and does then
output 0xh as response to the next byte.<br/>
Without the Access Card, the Yaroze Bootdisc will refuse to work (the disc
contains software for transferring data to/from PC, for developing homebrew
games).<br/>

#### Pocketstation (Memory Card with built-in LCD screen and buttons)
[Pocketstation](../pocketstation.md)<br/>
