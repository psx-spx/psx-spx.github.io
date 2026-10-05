#   Other Commands
#### GP0(1Fh) - Interrupt Request (IRQ1)
```
  1st  Command           (Cc000000h)                    ;GP1.R.24
```
Requests IRQ1. Can be acknowledged via GP1(02h). This feature is rarely used.<br/>
Note: The command is used by Blaze'n'Blade, but the game doesn't have IRQ1
enabled, and the written value (1F801810h) looks more like an I/O address,
rather than like a command, so not sure if it's done intentionally, or if it is
just a bug.<br/>

#### GP0(03h) - Unknown?
Unknown. Doesn't seem to be used by any games. On v2 GPUs, unlike the "NOP"
commands, GP0(03h) takes up space in the FIFO, so it is apparently not a NOP
there. On v0 GPUs it doesn't, and behaves like GP0(00h).<br/>

#### GP0(00h) - NOP (?)
This command doesn't take up space in the FIFO: while a VRAM-to-VRAM transfer
is busy, GP0(00h) is removed from the FIFO without waiting for the transfer,
and dozens of them in a row leave it empty rather than full. So, either the command is ignored (or, if
it has a function, it is executed immediately, even while the transfer is
busy). By contrast, GP0(01h), GP0(1Fh), GP0(E1h), GP0(E2h) and GP0(E6h) are
queued behind the transfer and fill the FIFO like drawing commands.<br/>
...<br/>
GP0(00h) unknown, used with parameter = 08A16Ch... or rather 08FDBCh ... the
written value seems to be a bios/ram memory address, anded with 00FFFFFFh...
maybe a bios bug?<br/>
GP0(00h) seems to be often inserted between texture page and rectangle commands,
maybe it acts as a NOP, which may be required between that commands, for timing
reasons...?<br/>
GP0(00h) with parameter 000000h, FFFFFFh or 08A16Ch changes nothing in GPUSTAT,
nothing in any of the GP1(10h) internal registers, and nothing in VRAM, on both
v0 and v2 GPUs. That is the whole of the state the GPU exposes for readback, so
whatever the command does, it leaves no observable trace. This says nothing
about the timing question above.<br/>

#### GP0(04h..1Eh,E0h,E7h..EFh) - Mirrors of GP0(00h) - NOP (?)
Like GP0(00h), these commands don't take up space in the FIFO, on v0 and v2
GPUs alike. So, maybe, they are same as GP0(00h), however, the Drawing
Area/Offset commands GP0(E3h..E5h) don't take up FIFO space either, so not
taking up FIFO space doesn't neccessarily mean that the command has no
function.<br/>
None of these changes GPUSTAT, any GP1(10h) internal register, or VRAM either,
on v0 or v2, for the same three parameters, so on that surface they are
indistinguishable from GP0(00h) and from each other, and they behave the same
in the FIFO as well.<br/>
