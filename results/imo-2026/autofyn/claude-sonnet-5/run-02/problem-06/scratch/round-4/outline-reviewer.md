## imo-2026-06 — outline review, round 4

### Verification method
I ran direct computer simulations (trial-division factorization, greedy sequence
generation, 1500-3000 terms) on the two seeds this run's population already treats
as canonical stress tests, a_1=175 (Q={5,7}, the round-3 falsifying seed for "zero
rounds") and a_1=35 (Q={5,7}, the round-2 falsifying seed for "universal glue
prime"), specifically to pressure-test both of this round's new key lemmas before
they reach a builder. Full script available on request; key outputs quoted below.

---

### covering-system-construction (revise, PUCL) — **CHANGES REQUESTED, with a
serious flaw isolated in Step 3 that must be fixed or dropped, not built as
written**

**Step 2 (PUCL itself) — plausible, not falsified, worth attempting.** I tested
the literal claim ("fixed nonempty core C_A ⊆ S such that every occurrence of
base type A, from its first occurrence onward, carries at least one prime of
C_A") on a_1=175: with C_{7}=C_{5}={2,3}, **zero misses across all 1226
occurrences of base type {7} and all 920 occurrences of base type {5}**, from
each type's very first occurrence. This is consistent with the joint-family
explorer's independent a_1=35 finding (type {7}'s occurrences always carry
*both* 2 and 3; type {5}'s occurrences always carry *at least one* of {2,3}).
So PUCL step 2 is a reasonable, not-yet-falsified target — the builder may
attempt it.

**Step 3 (the Corollary) is a non sequitur, and it is directly falsified by
data already on record.** The outline claims: "if A, B disjoint... C_A ∩ C_B ≠
∅ ... gives A′ ∩ B′ ⊇ (a fixed prime of C_A∩C_B) for EVERY extended-persistent
refinement A′, B′ of A, B — this would close V = ∅ completely and
unconditionally... bypassing the canonical/non-canonical distinction
entirely." This does **not** follow from PUCL as stated, because PUCL only
guarantees a *disjunctive* hitting property per occurrence (some prime of
C_A present), not that every occurrence's exact S₀-signature contains all of
C_A. Concretely, for a_1=175 with C_{7}=C_{5}={2,3} (verified above): the
already-documented rogue pair from `current.md` — extended type **{2,7}**
(a specific {7}-occurrence using only prime 2 from {2,3}, not 3) and extended
type **{3,5}** (a specific {5}-occurrence using only prime 3, not 2) — are
still genuinely disjoint as sets, **even though C_7 ∩ C_5 = {2,3} ≠ ∅.**
This is the exact same rogue pair that forced recruiting prime 13 in round 3.
So Step 3 as literally written, if a builder tried to prove it, would either
(a) fail, or worse (b) if pushed through sloppily, would resurrect the
falsified "zero further recruitment rounds" claim in disguise — since Step 3
explicitly claims to close V = ∅ "completely and unconditionally" using only
primes of S (no recruitment), which is precisely what round 3's a_1=175
computation refuted. **This is exactly the restated-old-falsified-claim risk
flagged in the dispatch — confirmed present, not merely a hypothetical
risk.**

**Required fix:** the builder must not attempt Step 3 as written. Either (a)
replace it with a correctly-scoped claim about how the *specific* extended
refinements interact (not marginal per-base-type cores), or (b) report that
PUCL, even if step 2 is fully proved, does not by itself close (†) — a
`witness-depth-bound`-style scope finding — and redirect. PUCL step 2 alone is
not useless (it is a real, unfalsified structural fact and may still be a
building block for a correctly-scoped joint-family argument), but it must be
built with this warning attached and Step 3 flagged as currently false, not as
a formality to fill in.

---

### greedy-exchange-cost-potential (revise, Round Resolution Lemma) —
**CHANGES REQUESTED, with a falsified over-claim to rescope before building**

The literal statement — "q divides EVERY sufficiently large A-type term (not
merely the infinitely many A′_0-type ones)... the recruitment PERMANENTLY
resolves the WHOLE base-type pair (A, B)" — is **falsified** by direct
computation on a_1=175: 13 divides only **176/1226 (~14%)** of ALL base-type-{7}
occurrences and **132/920 (~14%)** of ALL base-type-{5} occurrences, including
when restricted to the confirmed-periodic tail (n > 500): 146/1022 and
109/767 respectively — nowhere near "every sufficiently large A-type term."
The claim as stated conflates the *base* type (all refinements) with the
specific *extended-persistent* type actually witnessed in the rogue pair.

**The correctly-scoped, still-supported version**: restricted to the *specific*
extended-persistent type {2,7} (not the whole base type {7}) and {3,5} (not
the whole base type {5}), 13 divides every single occurrence with zero
exceptions — confirmed independently by the joint-family explorer both in the
tail (67/67, 50/50) and from each type's first occurrence (n=3, n=5 onward,
well before the eventual period sets in, so this is not simply a restatement
of periodicity). This narrower claim is a much better, not-yet-falsified
target.

**Required fix:** rescope the Round Resolution Lemma to talk about the
specific extended-persistent refinements A′_0, B′_0 involved in the witnessed
rogue pair, not the whole base-type pair (A, B). The first-bad-round
minimality proof strategy may still be viable at this narrower scope; the
builder must state the corrected, narrower target explicitly before
attempting the proof, and must not claim the broader "whole base-type pair"
version.

---

### uniform-core-direct-induction (new) — **RETHINK: not a genuinely diverse
framing, and duplicates PUCL's exact target and mechanism**

Despite being labeled "a structurally different top-level route" and "a
genuinely new framing," its actual content is a technique variant of PUCL:
same target object (a fixed finite core per persistent base type, valid from
first occurrence), same engine (Generalized Bounded Gap Lemma's "explicit
competing candidate" used to bound a_n and compare against the greedy choice),
same finish (CRT over the union of per-type cores, explicitly imported from
`covering-system-construction` Step 5). The stated difference — "local,
step-by-step invariant maintenance" vs. PUCL's "one-shot global witness
comparison" — is a proof-technique distinction, not a difference in what is
being proved or why it's true. This is precisely the pattern flagged in
round 3 (`current.md` Rules: "NEVER register/build an approach whose only
difference from a live approach is proof technique on the identical residual
sub-lemma").

Worse, this approach's skeleton never states the actual crux at all: it
jumps from "if the local induction closes, every base type A gets a fixed
core D_A" (step 3) straight to "Direct finish: CRT... exactly as Step 5"
(step 4), with **no corollary addressing how two disjoint base types' cores
D_A, D_B actually force their specific occurrences' refinements to
intersect.** That is exactly the step PUCL's Step 3 attempts and — per the
computation above — gets wrong. A builder assigned this slug would either (a)
independently rediscover the identical false corollary PUCL has (wasting a
build slot re-deriving the same mistake under a new name, the exact
duplication risk memory rule #2 warns about), or (b) silently omit it and
produce an unsound "proof" that never actually checks disjoint-type
reconciliation. Neither outcome is useful.

**Verdict: RETHINK.** Do not register; do not build this round. If the
"local, tighter, step-by-step" comparison idea has genuine value, fold it into
`covering-system-construction`'s builder instructions as an alternative proof
strategy FOR PUCL step 2 (not a separate top-level approach), and any next
round's genuinely-new framing should target the missing joint/simultaneous
mechanism directly (e.g., the aimo-0680-style "infinite-index-set →
all-indices" upgrade the joint-family explorer flagged as the closest
structural analogue, or the rescoped Round Resolution Lemma above) rather than
another per-type-core construction dressed differently.

---

### density-sieve-contradiction, hypergraph-transversal
No change proposed this round; correctly left stale and out of the build set
again (both cold, Elo lowest, no new content).

### Diversity assessment (per CLAUDE.md mandate)
The live field remains two closely-related framings on the identical residual
gap V (covering-system-construction's witness/covering language and
greedy-exchange-cost-potential's cost/exchange language) — both independently
converged on essentially the same missing ingredient this round (a
joint/simultaneous "infinitely-many → all, restricted to the specific witnessed
extended type" upgrade), which is a genuine positive signal about where the
crux actually lives, not a diversity failure per se. But the population has
now had **three consecutive rounds** (2, 3, 4) where every live approach
bottoms out on variants of the same wall. The rejected
uniform-core-direct-induction confirms the risk CLAUDE.md warns about: it is
easy to mistake a technique variant for a new framing. If round 5 still
doesn't close V after the two rescoped lemmas above are attempted, the next
outliner should be pushed hard toward a framing genuinely far from
"witness/exchange on individual occurrences" — e.g., a global counting/density
argument over whole residue classes mod a candidate L (attacking periodicity
directly rather than via the extended-type/recruitment apparatus at all).

### Ranking
Ran `update_ranking` comparing the two active approaches against the stale/dead
population members (both win convincingly) and each other (marked a draw —
both surfaced a falsified over-claim in their round-4 target this review, of
comparable severity; covering-system-construction remains the Elo leader from
its longer track record). No new approach registered (uniform-core-direct-induction
is RETHINK, never registered per protocol). Updated Elo: covering-system-construction
≈1660, greedy-exchange-cost-potential ≈1607, witness-depth-bound ≈1484 (unchanged
build status, dead-end), amortized-charging-budget ≈1446, density-sieve-contradiction
≈1404, hypergraph-transversal ≈1398.

### Instructions for this round's builders
- `covering-system-construction`: attempt PUCL Step 2 (fixed hitting-set core
  per base type) as a real, unfalsified lemma, but treat Step 3 (the
  Corollary) as **currently false** — do not attempt to prove it as written;
  either find a correctly-scoped replacement tied to specific extended-type
  refinements (not marginal per-base-type cores) or report the scope failure
  precisely, the way `witness-depth-bound` did last round.
- `greedy-exchange-cost-potential`: rescope the Round Resolution Lemma from
  "q resolves the whole base-type pair (A,B)" (falsified: only ~14% of
  base-type occurrences on a_1=175) to "q resolves the specific witnessed
  extended-persistent types A′_0, B′_0" (supported: 100% on all tested
  windows, including from first occurrence). Attempt the first-bad-round
  minimality proof at this narrower, corrected scope.

build set: covering-system-construction, greedy-exchange-cost-potential
