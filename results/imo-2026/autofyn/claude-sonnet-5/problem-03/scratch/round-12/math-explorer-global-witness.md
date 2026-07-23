# Math-explorer report — round 12 — lens: GLOBAL/INJECTIVE WITNESS CONSTRUCTION for Sharp Argmin Recovery (SAR)

**Scope note (per role):** this is exploration/terrain-scouting, not a proof attempt. All code is
exact-integer Python (no floats), archived at `/tmp/round-12/work-gw/` (moved off the default
`/tmp/round-12/work/` path after discovering mid-run that a parallel explorer this round was
already using it — see "Housekeeping" at the end).

## 1. Context absorbed

Read `results/imo-2026-03/current.md`, `results/imo-2026-03/approaches/potential-weighting-upper-bound.md`
(§13 for the OPT/TAGGED formalism, §16 in full for SAR/Forced-Swap/the three round-11 negative
results), and `results/imo-2026-03/lemmas/forced-swap-inequality.md`. Independently re-implemented
`OPT_sigma(B,Z)` and a generalized `TAGGED_multi(B,Z,splits)` (allowing an arbitrary *set* of
forbidden split points, not just one — needed for the recursive experiment below) from the prose
definitions in §13.2/§16.1, then validated the harness against the file's own documented `|B|=3`
SAR counterexample (`B=(0,6,4), Z=(10,8,5,4,3,1)`: reproduced `A_1=1`, `A_{3,k}` values
`(1,1,0,1,2)`, `A_{3,k*}=0`, `B_{3,k*}=1` — bit-for-bit match) before trusting it for anything new.

**The bottleneck, restated precisely (from §16 and the round-11 diagnosis):** SAR (recovery at the
*same* global-argmin match partner) is heavily corroborated at `|B|<=1` but unproved; local-repair
mechanisms (Forced Swap Inequality, averaging) are proven insufficient; SAR's naive generalization
to arbitrary background size is FALSE at `|B|=3`; and a naive one-step "compatible winner" induction
(GML) is FALSE even at `|B|<=1`, because it only checks compatibility *at the top level*, not
recursively. The round-11 builder's own flagged next step: *characterize precisely which
`(background, list, split)` triples arise from repeatedly peeling an argmin branch of a
`|B|<=1`-seeded instance (not arbitrary triples), and show recovery holds specifically on that
narrower family.* This round's work is a direct, computational attack on exactly that question.

## 2. Idea 1 (dead end, quickly ruled out): naive multi-split chain accumulation

First attempt: build a chain of instances by repeatedly peeling the max element and its global-argmin
match partner, accumulating one forbidden split per level into a generalized
`TAGGED_multi(B_d, Z_d, splits_d)`, and check whether this ever fails. Implemented in
`chain_test.py`. Result: **0 failures in ~5000 chains**, but this is a weak/uninformative test — in
every chain, the recursion almost always terminates after **at most one** triggered (MATCH-based)
level, because (as §2 below found) the very next level's own trichotomy essentially never triggers
again. So this experiment mostly just re-confirmed SAR's own single-level result via a different
code path; it did not probe deep chains because deep chains basically don't arise. Superseded by
the sharper, more informative experiment below. **Not a promising independent mechanism by itself
— retire this framing, but keep the underlying `tagged_multi` generalization (it is reused below and
is a genuinely useful reusable piece of infrastructure for any future recursive-invariant attempt.)**

## 3. Idea 2 (promising — the main finding): the "Match Self-Limiting" / "No-Second-Trigger" phenomenon

**Motivating question:** the round-11 diagnosis worries that a correct SAR-closing invariant must
certify compatibility "all the way down" the recursion — but *how far down does it actually need to
go?* If the SAR-triggering event (MATCH strictly beating DELETE/KEEP) essentially never recurs
immediately after it fires once, the "how deep" problem could be close to vacuous.

**Precise candidate statement tested:**

> **No-Second-Trigger (candidate, NOT proved).** Let `(B_0,Z_0)` have `|B_0|<=1`. Suppose peeling
> `z_1:=max(Z_0)` triggers (`M_opt := min_l A_{3,l} < A_1`) at a *global* argmin `k^*`. Let
> `C_1 := B_0 \cup \{z_1-z_{k^*}\}`, `W_1 := Z_0\setminus\{z_1,z_{k^*}\}`. Then peeling `w_1:=\max(W_1)`
> in the instance `(C_1,W_1)` **never has its own MATCH branch strictly beat its own DELETE branch**,
> i.e. `\mathrm{OPT}_{+1}(C_1,W_1\setminus\{w_1\}) \le \min_m \mathrm{OPT}_{+1}(C_1\cup\{w_1-w_m\}, W_1\setminus\{w_1,w_m\})`,
> for **every** tied global argmin `k^*` at the top level.

**Why this would matter if true:** it directly targets the round-11 diagnosis. If MATCH is never
the *unique* winner one level after a SAR-trigger, then constructing a full non-crossing witness
never needs a "recovery" mechanism beyond depth 1 at all — at depth 2 one can always fall back to
DELETE/KEEP (which trivially never introduce a crossing arc), sidestepping the arbitrary-background
generalization that is known FALSE (`|B|=3` counterexample) entirely, because that regime is simply
never *reached* along the legitimate recursive path.

**Testing methodology and an honestly-recorded self-caught bug.** The first version of the stress
test (`no_second_trigger_stress.py`) had a **sign error**: it defined `margin := A_1' - M_{opt}'`
and flagged `margin<0` as a "violation." This is backwards — `margin<0` means `A_1' < M_{opt}'`, i.e.
DELETE actually *wins* (the safe case), while a genuine violation (MATCH strictly beating DELETE)
is `margin>0`. The bug produced a large, alarming list of false "violations" on the first run;
hand-tracing the very first one (`B_0=(19,), Z_0=(20,14,4,3)`: `A_1'=2`, `M_{opt}'=12`, so DELETE
wins by 10, not a violation) caught the error before it was reported as a finding. Fixed and
re-run — recorded here per this repo's own convention of documenting self-caught bugs (cf. round 4,
round 11's own such notes).

**Results after the fix, exact-integer, all reproducible:**
- Direct scan (`no_second_trigger_stress.py`'s `scan`, two independent seeds): `q=4,...,10`,
  background seed size `0` or `1`, value ranges up to `150`, **every** tied global argmin `k^*`
  checked (not just one per instance) — **`2152 + 2825 = 4977` direct checks, `0` violations**;
  worst (most-negative, i.e. most-safely-DELETE-winning) margin found was `-111`.
- Adversarial hill-climbing (mirroring the round-11 builder's own technique for stress-testing
  SAR itself): `24` independent runs (`q=5,6,7,8`, `300` iterations each, `~7200` evaluated
  perturbed states), each explicitly trying to *maximize* the margin toward a positive (violating)
  value — **best margin found across all runs: exactly `0`** (an exact tie), **never strictly
  positive**. No violation found by directed search either.
- **Total: ~12,000 evaluations combined, 0 confirmed violations of the corrected statement.**

**Important negative control (rules out a simpler false generalization):** is "MATCH never beats
DELETE" simply a raw fact about *any* background of size `<=2`, regardless of how it arose?
**No** — `arbitrary_bg2_test.py` checked arbitrary (not legitimately-derived) background-size-`2`
instances directly and found MATCH strictly beats DELETE in **`28%`** of triggering checks (`1677/6000`
at `|B|=2`, rising to `37%` at `|B|=3`). So the safety is **not** a generic small-background fact —
it is specific to the *legitimate derivation* (background element `= z_1 - z_{k^*}` where `z_1` is
the true top-level max and `k^*` the true global argmin over *all* partners), exactly the kind of
"specific narrower family, not arbitrary triples" distinction the round-11 diagnosis called for.

## 4. Important caveat found this round: safety requires a specific tie-breaking rule, not depth-independence for free

`depth3_probe.py` checked: in the (rare) instances where level 2 is an **exact tie**
(`M_{opt}'=A_1'`), what if an adversary *forces* the MATCH branch to be taken anyway (rather than
falling back to the safe DELETE/KEEP branch) and peels one level further? **Result: genuine
violations DO appear at depth 3 under this forced tie-break** (multiple examples found, e.g.
`B_0=(5,), Z_0=(7,3,2,2,1,0)`: level-1 trigger, level-2 exact tie at `(C_1,W_1)=((5,5),(3,2,1,0))`,
forcing MATCH there leads to `(C_2,W_2)=((5,5,1),(1,0))` with `A_1''=1 > M_{opt}''=0` — a real
strict violation one level further in).

**Interpretation:** this is not evidence against the mechanism — it precisely characterizes what a
correct recursive witness-construction algorithm must do: **whenever DELETE/KEEP ties MATCH, the
construction must canonically prefer DELETE/KEEP**, never MATCH, to stay inside the safe family.
Since a tie means DELETE/KEEP already achieves the *same* value, this costs nothing and is exactly
the kind of "canonical global rule" the round's lens asked for (not a local repair — a *rule for
resolving the recursive choice itself*, applied uniformly at every level). **The candidate closing
statement is therefore: "No-Second-Trigger" (§3) + "canonical delete/keep-over-match tie-break at
every level" together are (numerically) sufficient to build a full witness recursively without ever
needing an arbitrary-background-size recovery lemma — but only the first component (No-Second-Trigger
itself) was stress-tested at depth 2 as a genuine strict inequality; the *combination*, all the way
to arbitrary depth, was only spot-checked one level further (depth 3, and only via the adversarial
forced-tie experiment, which is a check of what goes wrong *without* the rule, not a positive
confirmation *with* it at depth >=3). A future round should directly stress-test the combined
construction (No-Second-Trigger strict inequality + canonical tie-break) recursively to full depth
on larger `q`, not just to depth 2–3.**

## 5. What this round rules out vs. what it opens

**Ruled out / not promising:**
- Naive multi-split chain accumulation without first understanding *why* deep chains rarely form
  (§2) — uninformative on its own, superseded.
- "MATCH never beats DELETE at background size `<=2`" as a **generic**, origin-independent fact —
  **false** (`28%`/`37%` failure rates at arbitrary `|B|=2,3`). Any proof of No-Second-Trigger must
  use the *specific* algebraic relationship between `z_1` (global max), `k^*` (global argmin
  partner), and the residual — not a background-size argument alone.
- A depth-independent safety guarantee *without* a specified tie-breaking rule — false (§4).

**Promising, open, recommended as next round's primary build target:**
- The **No-Second-Trigger Lemma** (§3), precisely stated, survives ~12,000 combined direct and
  adversarial-search evaluations with zero violations — a new, structurally different (not
  local-repair, not averaging, not arbitrary-background) candidate mechanism, directly answering
  the round-11 diagnosis's own question about "how far down" a correct invariant must certify
  compatibility. **No proof attempted this round** (out of scope for the explorer role) — a
  concrete next step for a builder: try to derive it from the *global* argmin property the same
  way the certified Forced Swap Inequality does (i.e. chain `M_{opt}\le A_{3,l}` for the *specific*
  `l` corresponding to `w_1`'s position in the original `Z_0`, not just `k^*`'s own branch) — this
  round found (by hand-tracing two examples) that the simplest candidate reason ("the inserted
  background value `z_1-z_{k^*}` always dominates `w_1=\max(W_1)`") is **false** as a general
  explanation (counterexample: `B_0=(66,), Z_0=(98,96,33,17)`, `d=65 < w_1=96`, yet the lemma still
  held with margin `-77`) — so the true mechanism is subtler than simple domination and needs
  genuine proof work, not just a one-line bound.
- Combine with the canonical "prefer DELETE/KEEP over MATCH on ties" rule (§4) as the actual
  witness-construction recipe to propose for a build.

## 6. Housekeeping note

Mid-session, `/tmp/round-12/work/defs.py` (the default scratch path suggested by the dispatch
convention) was found overwritten by a concurrently-running parallel explorer using the same
default directory. All work in this report was moved to and redone in `/tmp/round-12/work-gw/` to
avoid further collision; that directory contains `defs.py`, `chain_test.py`, `level2_stats.py`,
`no_second_trigger_stress.py`, `depth3_probe.py`, `arbitrary_bg2_test.py`, all independently
runnable. Flagging this so the orchestrator can consider giving parallel explorers distinct scratch
subdirectories in future rounds' dispatch instructions.
