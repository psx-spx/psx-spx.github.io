#   GTE Pipeline Timings
[Overview](gtepipelinetimings.md#overview)<br/>
[Methodology](gtepipelinetimings.md#methodology)<br/>
[Result tables](gtepipelinetimings.md#result-tables)<br/>
[Patterns](gtepipelinetimings.md#patterns)<br/>
[Caveats and methodology limits](gtepipelinetimings.md#caveats-and-methodology-limits)<br/>



##   Overview
Each GTE instruction has a documented total cycle count, but games have
historically treated the period between issuing a `cop2 imm25` opcode and
its completion as opaque - the SDK and most documentation only say "do not
modify input registers while a GTE instruction is in flight". In practice
the GTE samples each input register at a deterministic offset within
that execution window. After the latch, the input register file is no
longer read by the in-flight op and is safe to overwrite.

This page documents, for each (instruction, input register), the smallest
number `N` of nops between the GTE op and an `MTC2`/`CTC2` to that input
register such that the `MTC2`/`CTC2` does **not** change the GTE's
output. That `N` is the practical "instruction slots required between
the cop2 op and the next write to this input" - the actionable number a
developer needs to know if they want to overlap CPU work with GTE work.

All numbers are hardware-verified on a single SCPH-5501 console. Other
PSX revisions have not been measured; some 1-2 cycle drift is plausible
across silicon revisions.



##   Methodology
The premise: `MTC2`/`CTC2` does not stall while a GTE instruction is in
flight (the CPU continues issuing instructions immediately). The write
reaches the GTE's register file after a small fixed delay. By varying
the number of CPU instructions between the cop2 op and a perturbing
`MTC2`/`CTC2`, the read site of any given input register becomes
visible: the smallest `N` at which the perturbation no longer affects
the output is the latch boundary.

For each (instruction, register) pair, the test runs:
```
  scene_setup           ; reset all GTE inputs to a known baseline
  cop2 op_imm           ; fire the GTE instruction
  nop  x N              ; vary N from 0 upward
  mtc2 canary, $reg     ; perturb the target register
  nop  x 60             ; let the GTE complete
  mfc2 ...              ; read RGB FIFO, MAC, IR, FLAG, SXY/SZ FIFOs
```
The result is compared against a **baseline** captured by running the
same shape with the perturbing write happening long after the GTE
completes (80 nops of drain before `MTC2`).

A **canary-pre sanity check** also runs: writing the canary BEFORE the
cop2 op confirms that the canary value would change the result if it
landed in time during execution. This pinpoints cases where the chosen
canary value happens to produce the same saturated output as the
baseline (which would otherwise look like a false N=0 boundary).

Each sweep runs twice with the first iteration discarded for icache
warmup, and CPU IRQs are masked across the sweep so a stray interrupt
cannot stretch the gap between the cop2 op and the perturbing `MTC2`.

The full test source is in pcsx-redux at
[`src/mips/tests/gte-latency*/`](https://github.com/nicolasnoble/pcsx-redux/tree/main/src/mips/tests).



##   Result tables
Boundary `N` is the smallest number of nops between `cop2 imm25` and an
`MTC2`/`CTC2` to the listed register at which the perturbation no
longer affects any GTE output. `N=0` means the register was already
read by the time the very first nop slot would have run - it is safe
to clobber the register from one instruction after the cop2 op onward.

A dash (-) means the instruction does not read that register.

####   Perspective transforms

| Input register | RTPS (15c) | RTPT (23c) |
|----------------|-----------:|-----------:|
| VXY0 / VZ0     |       0/0  |       0/0  |
| VXY1 / VZ1     |        -   |       3/0  |
| VXY2 / VZ2     |        -   |       2/0  |
| RT11RT12       |          0 |          2 |
| RT13RT21       |          0 |          4 |
| RT22RT23       |          0 |          4 |
| RT31RT32       |          0 |          0 |
| RT33           |          0 |          0 |
| TRX / TRY / TRZ|     0/0/0  |     1/4/1  |
| OFX / OFY      |       1/0  |       5/4  |
| H              |          1 |          5 |
| DQA            |          4 |          7 |
| DQB            |          3 |          6 |

####   Lighting (single-vertex)

| Input register | NCS (14c) | NCCS (17c) | NCDS (19c) |
|----------------|----------:|-----------:|-----------:|
| VXY0 / VZ0     |      0/0  |       0/1  |       0/1  |
| RGBC           |       -   |          3 |          3 |
| L11L12         |          0 |          0 |          0 |
| L13L21         |          0 |          0 |          0 |
| L22L23         |          0 |          0 |          0 |
| L31L32         |          0 |          0 |          0 |
| L33            |          0 |          0 |          0 |
| LR1LR2         |          2 |          2 |          2 |
| LR3LG1         |          1 |          1 |          1 |
| LG2LG3         |          1 |          1 |          1 |
| LB1LB2         |          2 |          2 |          2 |
| LB3            |          3 |          3 |          3 |
| RBK / GBK / BBK|     0/2/1  |       0/2/1|       0/2/1|
| RFC / GFC / BFC|       -    |       -    |     2/3/4  |

####   Lighting (triple-vertex)

| Input register | NCT (30c) | NCCT (39c) | NCDT (44c) |
|----------------|----------:|-----------:|-----------:|
| VXY0 / VZ0     |      0/2  |       0/2  |       0/0  |
| VXY1 / VZ1     |      0/1  |       0/1  |       0/1  |
| VXY2 / VZ2     |      1/3  |       3/3  |       3/4  |
| RGBC           |       -   |         12 |         15 |
| L11L12         |          0 |          1 |          1 |
| L13L21         |          0 |          0 |          0 |
| L22L23         |          3 |          3 |          3 |
| L31L32         |          0 |          1 |          2 |
| L33            |          0 |          1 |          2 |
| LR1LR2         |          6 |          5 |          5 |
| LR3LG1         |          3 |          3 |          4 |
| LG2LG3         |          8 |          8 |          7 |
| LB1LB2         |          8 |          7 |          7 |
| LB3            |          6 |          5 |          5 |
| RBK / GBK / BBK|     8/9/9  |     9/6/9  |     7/7/7  |
| RFC / GFC / BFC|       -    |       -    |    13/14/14|

####   Color

| Input register | CC (11c) | CDP (13c) |
|----------------|---------:|----------:|
| RGBC           |        0 |         1 |
| IR0            |       -  |         2 |
| IR1 / IR2 / IR3|   1/2/2  |     2/3/2 |
| LR1LR2         |        0 |         0 |
| LR3LG1         |        0 |         0 |
| LG2LG3         |        0 |         0 |
| LB1LB2         |        1 |         1 |
| LB3            |        0 |         0 |
| RBK / GBK / BBK|   0/0/0  |     0/0/0 |
| RFC / GFC / BFC|     -    |     0/2/0 |

####   Depth-cue

| Input register | DPCS (8c) | DPCT (17c) | DCPL (8c) | INTPL (8c) |
|----------------|----------:|-----------:|----------:|-----------:|
| RGBC           |         0 |        -   |         0 |        -   |
| RGB0           |       -   |          4 |       -   |        -   |
| RGB1           |       -   |          4 |       -   |        -   |
| RGB2           |       -   |          0 |       -   |        -   |
| IR0            |         1 |          4 |         0 |          1 |
| IR1 / IR2 / IR3|       -   |        -   |     1/0/1 |      0/1/0 |
| RFC / GFC / BFC|     0/0/0 |      1/2/3 |     0/0/0 |      0/0/0 |

####   Math

| Input register | SQR (5c) | OP (6c) | NCLIP (8c) |
|----------------|---------:|--------:|-----------:|
| IR1 / IR2 / IR3|    0/0/1 |   0/1/0 |        -   |
| RT11RT12       |        - |       0 |        -   |
| RT22RT23       |        - |       0 |        -   |
| RT33           |        - |       0 |        -   |
| SXY0           |        - |       - |          0 |
| SXY1           |        - |       - |          1 |
| SXY2           |        - |       - |          1 |

####   Misc

| Input register | AVSZ3 (5c) | AVSZ4 (6c) | GPF (5c) | GPL (5c) |
|----------------|-----------:|-----------:|---------:|---------:|
| SZ0            |       -    |          0 |       -  |       -  |
| SZ1 / SZ2 / SZ3|      0/0/0 |      0/0/0 |       -  |       -  |
| ZSF3 / ZSF4    |     0 / -  |     - / 0  |       -  |       -  |
| IR0            |       -    |        -   |        0 |        0 |
| IR1 / IR2 / IR3|       -    |        -   |    0/0/0 |    0/0/0 |
| MAC1/2/3       |       -    |        -   |       -  |    0/0/0 |

####   MVMVA

MVMVA is parameterized over (mx, v, cv); 8 cycles regardless of
parameter selection. Three documented parameter combinations were
probed:

| Input register | (RT, V0, TR) | (LL, V0, BK) | (LC, IR, BK) |
|----------------|-------------:|-------------:|-------------:|
| VXY0 / VZ0     |        0/0   |        0/2   |        -     |
| IR1 / IR2 / IR3|        -     |        -     |     1/0/1    |
| Selected matrix|       all 0  |   max 1      |    max 1     |
| TR / BK        |     0/0/0    |    0/0/0     |    0/0/0     |



##   Patterns

####   The GTE snapshots its inputs early
For nearly every instruction, every input register has a boundary in
the first ~4 cycles. The GTE essentially snapshots its input register
file at the start of execution and works from internal pipeline storage
afterward. From the developer's perspective, the documented per-instruction
cycle count is misleading as a "do not touch the inputs" window: the
"actually reading the inputs" window is much shorter.

####   Triple-vertex variants extend the boundary by ~3 nops
NCCT, NCT, NCDT, RTPT, DPCT all push V2's boundary 2-4 nops later than
single-vertex variants. The GTE walks V0 -> V1 -> V2 over the first
several cycles before the matrix multiplies start in earnest.

####   RGBC for NCCT-class triples latches mid-execution
Unlike the matrices and BK (latched in the first ~4 cycles), RGBC for
NCCT, NCDT latches at cycle 12-15. The first sub-pass's color stage is
the read site. The sweep also shows a clean two-step transition: at one
N value the V0 result reverts to baseline (V0's color stage finished
reading RGBC); at the next N value the V1 and V2 results revert
together. This suggests the hardware reads RGBC twice during a
triple-vertex op - once for V0, once covering V1+V2 - rather than
re-reading per sub-pass.

####   Depth-queue inputs latch latest among RTPS inputs
DQA / DQB are read at cycle 3-4 of RTPS (cycle 6-7 of RTPT). They are
used at the end of the projection pipeline to compute IR0 from depth.

####   Far Color (FC) latching depends on instruction
DPCS, DCPL, INTPL all latch FC by N=0 (depth-cue is the bulk of these
8-cycle ops, and FC is read very early). NCDS / NCDT spread the reads
across the per-vertex depth-cue stages and push the boundary out
(NCDT BFC = 14). DPCT shows progressive boundaries 1/2/3 for RFC/GFC/BFC,
matching its per-channel pipelining.



##   Caveats and methodology limits

####   icache layout sensitivity
Boundaries fluctuate by 1-2 nops between code-layout variants of the
test (the alignment of the probe block within the icache page matters).
The numbers in this table reflect a single test build's results;
treat single-cycle differences as noise.

####   Single-console caveat
All measurements are from one SCPH-5501. Other PSX revisions (PAL, late
SCPH, PSone, PS2 backwards-compat) have not been verified. The
short-instruction `N=0` results should be very stable; the long
instructions and triple variants are more likely to drift between
silicon revisions.

####   Saturation collapse
If the canary perturbation drives the output to the same saturated
value as the baseline (e.g. canary saturates IR to 0x7fff which is the
same as baseline IR), the test would report a false N=0 boundary. The
canary-pre sanity check catches this and forces the test to fail
loudly. The canary values used here are chosen smaller than the
baseline so the perturbed pipeline produces a distinguishable result.

####   "Doesn't affect output" vs "internal latch cycle"
The boundary measures when the GTE finished reading the register *as
observable through the output*. If a register is read into an internal
pipeline that gets multiplied by zero (e.g., `R12` multiplied against
`V0_X = 0`), the test reports `N=0` because no perturbation can change
the output - even if the GTE is internally still reading `R12` later.
The methodology measures the practical "safe to clobber" cycle, not
the internal hardware read schedule.

####   `LWC2` excluded
`LWC2` is excluded from the methodology. The memory-side latency (DRAM
controller, BIU state) would smear the boundary measurement. `MTC2` is
the clean probe because the CPU-to-COP2 path is deterministic.

####   GAS does not auto-insert nops
Verified by disassembling the probe code: `cop2 imm25; .rept N\n nop\n .endr; mtc2`
emits exactly N nops between the cop2 op and the mtc2. The
psyq SDK's habit of conservatively padding `cop2` with surrounding nops
does not apply to inline assembly using `.rept`.
