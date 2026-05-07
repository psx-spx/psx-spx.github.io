#   Partial-Word Writes to MMIO

[Overview](partialwordwrites.md#overview)<br/>
[Methodology](partialwordwrites.md#methodology)<br/>
[On-die MMIO behavior](partialwordwrites.md#on-die-mmio-behavior)<br/>
[SBUS behavior](partialwordwrites.md#sbus-behavior)<br/>
[Summary table](partialwordwrites.md#summary-table)<br/>
[Practical implications](partialwordwrites.md#practical-implications)<br/>
[Caveats](partialwordwrites.md#caveats)<br/>



##   Overview
The MIPS R3000A asserts byte-enable signals on `sb`/`sh`/`swl`/`swr`
stores, but the PS1's bus fabric does not honor them as a programmer
would expect on RAM. The result is that partial-word writes to
hardware registers behave very differently from partial-word writes
to RAM, and the exact behavior depends on which bus the target
register sits on:

- **On-die MMIO** (IRQ control at `0x1F801070-77h`, DMA control
  registers at `0x1F8010F0-F7h`, GPU control, MDEC, etc.) sits on
  the 32-bit data fabric internal to the CPU package. Byte enables
  are ignored; partial-word stores latch a shifted source word in
  full.
- **SBUS** (SPU, CD-ROM, BIOS ROM, Expansion 1/2) is an off-die
  system bus whose data path width is per-device, configured via
  bit 12 of each device's Delay/Size register (see
  [Memory Control](memorycontrol.md)). CD-ROM and BIOS ROM are
  configured as 8-bit; SPU is configured as 16-bit; expansion
  ports can use either. For a 32-bit CPU access, the bus interface
  unit decomposes the access into either 2 (16-bit device) or 4
  (8-bit device) consecutive transactions, keeping `!CS` active
  and stepping the address. The SPU specifically latches halfwords
  whenever `SBUS./WR0` strobes; `SBUS./WR1` alone is ignored.

The practical upshot is that idioms like "write one byte of a
register" do not work for hardware registers, and an `sw` to a
16-bit SPU register also writes the neighboring register.

All numbers below are hardware-verified on a single SCPH-5501.
The SBUS rules below were measured against SPU registers only;
behavior at CD-ROM and BIOS ROM (8-bit-configured) is expected
to differ in the number of transactions per access and has not
been measured here.



##   Methodology
For each (target register, op, byte offset, baseline pattern,
source pattern) the test:

```
  set_baseline(target, baseline)        ; full-width store
  $a2 = source                          ; distinguishable bytes
  <op> $a2, off(target_addr)            ; verbatim asm trampoline
  result = readback(target)             ; full-width load
```

Three baselines (`0x00000000`, `0xFFFFFFFF`, `0x11223344`) and
two source patterns (`0xAABBCCDD`, `0xFEDCBA98`) per (target,
op, offset) triple. The asm trampolines force the exact opcode
the C compiler would otherwise legalize. Misaligned `sh` traps
are caught by an installed AdES handler that records the trap
and skips the faulting instruction.

Targets:

- `IMASK` (`0x1F801074`): on-die, 32-bit, low 11 bits valid.
- `DPCR`  (`0x1F8010F0`): on-die, 32-bit, all bits R/W. The
  cleanest readback target.
- `SPU_VOL_MAIN_LEFT` (`0x1F801D80`): SBUS, 16-bit, R/W after
  muting the SPU. Neighbor is `SPU_VOL_MAIN_RIGHT` at `+2`.
- Voice 0 left volume (`0x1F801C00`): SBUS, 16-bit. Confirms
  the behavior is a property of the bus path, not of any
  individual SPU register.



##   On-die MMIO behavior
For 32-bit on-die registers the CPU drives a shifted source word on
the 32-bit data bus and the decoder latches the entire word,
regardless of which byte enables are asserted.

The shift is determined by the op and the byte offset:

| op    | bus value driven on `D[31:0]` |
|-------|-------------------------------|
| `sw`  | `src`                         |
| `sb +N`  | `src << (N * 8)`           |
| `sh +0`  | `src`                      |
| `sh +2`  | `src << 16`                |
| `swl +N` | `src >> ((3 - N) * 8)`     |
| `swr +N` | `src << (N * 8)`           |

Example with `src = 0xAABBCCDD` against `DPCR`:

| op     | offset | got after readback |
|--------|--------|--------------------|
| `sw`   | +0     | `0xAABBCCDD`       |
| `sb`   | +0     | `0xAABBCCDD`       |
| `sb`   | +1     | `0xBBCCDD00`       |
| `sb`   | +2     | `0xCCDD0000`       |
| `sb`   | +3     | `0xDD000000`       |
| `sh`   | +0     | `0xAABBCCDD`       |
| `sh`   | +2     | `0xCCDD0000`       |
| `swl`  | +0     | `0x000000AA`       |
| `swl`  | +1     | `0x0000AABB`       |
| `swl`  | +2     | `0x00AABBCC`       |
| `swl`  | +3     | `0xAABBCCDD`       |
| `swr`  | +0     | `0xAABBCCDD`       |
| `swr`  | +1     | `0xBBCCDD00`       |
| `swr`  | +2     | `0xCCDD0000`       |
| `swr`  | +3     | `0xDD000000`       |

In every case the register is fully overwritten with the bus
value. The pre-write contents do not contribute - results are
identical with baselines `0x00000000`, `0xFFFFFFFF`, and
`0x11223344`. Byte enables do not gate the latch.

`IMASK` follows the same pattern in its 11 valid bits. The
upper 21 bits read as `0xBF800xxx`, the upper half of the
IMASK address itself echoing on open-bus lanes during the
read phase.

Misaligned `sh` (`+1` and `+3`) traps with `cause=0x10000014`
(ExcCode 5, AdES). The exception fires before the bus
transaction; the register is unchanged.



##   SBUS behavior
The SBUS is the off-die system bus shared by SPU
(`SBUS./CS4`), CD-ROM (`/CS5`), BIOS ROM (`/CS2`), and
Expansion 1/2 (`/CS0`, `/CS3`). Address lines are
`SBUS.A[23:0]`. Data lines are `SBUS.D[15:0]`, but each
device is independently configured as 8-bit or 16-bit
via bit 12 of its Delay/Size register (see
[Memory Control](memorycontrol.md)): an 8-bit device uses
only `SBUS.D[7:0]`. Write strobes are `SBUS./WR0` (lower
byte of halfword) and `SBUS./WR1` (upper byte).
`SBUS./WR1` is wired only to the expansion port and not
to other SBUS devices; the SPU and the 8-bit devices do
not consume it.

Because the SBUS data path is at most 16 bits wide, a
32-bit CPU access cannot fit in one bus cycle. The bus
interface unit (BIU) decomposes each CPU access into a
sequence of consecutive transactions: 2 transactions for
a 32-bit access on a 16-bit device, 4 transactions for
the same on an 8-bit device, with `!CS` held active and
the address stepped between transactions.

The rules in this section were measured against SPU
registers (16-bit configured). The 16-bit-bus dispatch
rules apply unchanged for any 16-bit-configured SBUS
device that latches on `/WR0`. The 8-bit case (CD-ROM,
BIOS ROM) was not measured here and would be a separate
matrix.

###   BIU dispatch rules

**Number of transactions:**

- 4-byte CPU access (`sw`, `swl +3`, `swr +0`): TWO transactions,
  one per halfword.
- 1-, 2-, or 3-byte access (`sb`, `sh`, all other `swl`/`swr`):
  ONE transaction, at the halfword containing the lowest enabled
  byte. Bytes outside that halfword are silently dropped.

**Strobe assertion per issued halfword:**

- 1-byte access (`sb`, `swl +0`, `swr +3`): asserts only `/WR0`
  or `/WR1` per the addressed lane (lane 0 or lane 2 -> `/WR0`;
  lane 1 or lane 3 -> `/WR1`).
- 2-or-more-byte access: asserts BOTH `/WR0` and `/WR1` on each
  issued halfword, regardless of which CPU-side lanes were
  enabled within it.

**SPU latch rule:** the SPU latches the full 16 bits of `SBUS.D`
into the addressed register whenever `/WR0` strobes. `/WR1`
strobing alone does nothing.

###   SBUS writes to MAINVOL_L

Test target: `SPU_VOL_MAIN_LEFT` at `0x1F801D80`. Neighbor:
`SPU_VOL_MAIN_RIGHT` at `0x1F801D82`. Source `0xAABBCCDD`,
baseline `0x0000` for both registers.

| op       | bytes | issued halfword  | strobe       | bus halfword | reg got | neighbor got |
|----------|-------|------------------|--------------|--------------|---------|--------------|
| `sh +0`  | 2     | low (MAINVOL_L)  | both         | `0xCCDD`     | `0xCCDD`| `0x0000`     |
| `sb +0`  | 1     | low              | `/WR0` only  | `0xCCDD`     | `0xCCDD`| `0x0000`     |
| `sb +1`  | 1     | low              | `/WR1` only  | `0xDD00`     | `0x0000`| `0x0000`     |
| `sb +2`  | 1     | high (MAINVOL_R) | `/WR0` only  | `0xCCDD`     | `0x0000`| `0xCCDD`     |
| `sb +3`  | 1     | high             | `/WR1` only  | `0xCC00`     | `0x0000`| `0x0000`     |
| `swl +0` | 1     | low              | `/WR0` only  | `0x00AA`     | `0x00AA`| `0x0000`     |
| `swl +1` | 2     | low              | both         | `0xAABB`     | `0xAABB`| `0x0000`     |
| `swl +2` | 3     | low              | both         | `0xBBCC`     | `0xBBCC`| `0x0000`     |
| `swl +3` | 4     | both             | both x2      | both         | `0xCCDD`| `0xAABB`     |
| `swr +0` | 4     | both             | both x2      | both         | `0xCCDD`| `0xAABB`     |
| `swr +1` | 3     | low              | both         | `0xDD00`     | `0xDD00`| `0x0000`     |
| `swr +2` | 2     | high             | both         | `0xCCDD`     | `0x0000`| `0xCCDD`     |
| `swr +3` | 1     | high             | `/WR1` only  | `0xDD00`     | `0x0000`| `0x0000`     |

Reading the table:

- `sb +1` and `sb +3` are silent no-ops because their single
  transaction asserts only `/WR1`, which the SPU does not
  consume. The register is unchanged regardless of baseline.
- `sb +2` lands in MAINVOL_R, not MAINVOL_L. A "byte 2" address
  decodes to the high halfword on SBUS, so the transaction
  targets MAINVOL_R.
- `swl +2` writes 3 bytes (bytes 0+1+2). The lowest enabled byte
  is byte 0, so the transaction issues at the low halfword. The
  byte 2 portion that would have spanned into MAINVOL_R is
  silently dropped.
- `swr +1` symmetrically writes 3 bytes (bytes 1+2+3) and issues
  at the low halfword. The byte 2+3 portion that would have
  spanned into MAINVOL_R is dropped.
- `swr +0` (full 32-bit access) splits into two transactions and
  hits both registers. This is why an `sw` to a 16-bit SPU
  register also clobbers its neighbor.

The behavior is identical when the target is voice 0 left volume
at `0x1F801C00`. It is a property of the SBUS path, not of the
specific register.

When `/WR0` strobes, the entire 16-bit SBUS data halfword lands
in the addressed register, even on `sb`. With baseline `0xFFFF`
and source `0xAABBCCDD`, an `sb +0` produces got `0xCCDD`, not
`0xFFDD` - the high byte of the register is overwritten by the
high byte of the bus data, even though the byte-enable was only
on lane 0. The SPU does not byte-mask within a halfword.



##   Summary table
Per-op behavior at every byte offset, for the two bus types.
"latch full word/halfword" means the register is overwritten
with the full bus payload regardless of byte enables. "drop"
means the register is unchanged.

| op   | offset | on-die 32-bit MMIO          | SBUS 16-bit-configured (e.g. SPU)       |
|------|--------|-----------------------------|-----------------------------------------|
| `sw` | +0     | full word latched           | both halfwords latched (incl. neighbor) |
| `sh` | +0     | full word, hi half from bus | low halfword latched                    |
| `sh` | +2     | full word, lo half from bus | high halfword latched (in neighbor)     |
| `sh` | +1/+3  | AdES                        | AdES                                    |
| `sb` | +0     | full word latched           | low halfword latched                    |
| `sb` | +1     | full word latched           | drop                                    |
| `sb` | +2     | full word latched           | high halfword latched (in neighbor)     |
| `sb` | +3     | full word latched           | drop                                    |
| `swl`| +0     | full word latched           | low halfword latched                    |
| `swl`| +1     | full word latched           | low halfword latched                    |
| `swl`| +2     | full word latched           | low halfword latched (byte 2 dropped)   |
| `swl`| +3     | full word latched           | both halfwords latched                  |
| `swr`| +0     | full word latched           | both halfwords latched                  |
| `swr`| +1     | full word latched           | low halfword latched (bytes 2+3 dropped) |
| `swr`| +2     | full word latched           | high halfword latched (in neighbor)     |
| `swr`| +3     | full word latched           | drop                                    |



##   Practical implications

- Setting one byte of a 32-bit MMIO register via `sb` does not
  work. The whole register is overwritten.
- Read-modify-write idioms like `*reg |= mask` work as expected
  when `reg` is typed as `volatile uint32_t *` for an on-die
  32-bit register, or `volatile uint16_t *` for an SPU register:
  the compiler emits a matching-width load and store, and the
  partial-word rules above never come into play. The hazard is
  aliasing an MMIO register through a different-width pointer
  (e.g., a `volatile uint8_t *` to a 32-bit register) - the load
  is harmless but the store becomes an `sb` and clobbers the
  entire register per the rules above.
- `sw` to a 16-bit SPU register also writes the neighboring
  register. Use `sh` for single-register writes.
- `sb` to the high byte of a halfword in any SBUS region (lane
  1 or lane 3 within the addressed word) is a silent no-op on
  the SPU. Other SBUS devices (CD-ROM, BIOS ROM) may behave
  differently; only the SPU was tested directly.
- `swl` and `swr` to MMIO are well-defined but not particularly
  useful for register access: they latch a shifted source
  identical to `sb`/`sh` patterns, and on SBUS they drop bytes
  that span halfword boundaries.
- Misaligned `sh` (`+1`/`+3`) AdES-traps cleanly without
  modifying the target register.



##   Caveats

- Hardware-verified on a single retail SCPH-5501. Other PSX
  revisions have not been measured. The on-die MMIO behavior
  is expected to be identical across revisions; the SBUS
  dispatch rules are properties of the bus interface unit on
  the CPU die and should also be revision-stable, but the
  per-strobe SPU latch behavior may differ on SPU revisions
  shipped in other consoles.
- Only IMASK, DPCR, and SPU registers (MAINVOL_L and voice 0
  volumes) were tested directly. The on-die behavior is
  expected to apply uniformly to all on-die MMIO; the SBUS
  behavior is expected to apply to other 16-bit-configured
  SBUS devices but has not been verified there. CD-ROM and
  BIOS ROM are 8-bit-configured (Delay/Size bit 12 = 0) so the
  number of transactions per CPU access differs - their write
  semantics were not measured.
- GPU GP0/GP1 (VBUS, 32-bit, single decoded address bit, no
  byte masking) and timer mode registers (R/W with side
  effects) were not tested.
