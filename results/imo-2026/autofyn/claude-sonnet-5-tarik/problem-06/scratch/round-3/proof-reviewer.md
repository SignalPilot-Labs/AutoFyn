# Proof review — imo-2026-06, round 3

Reviewed all 4 built approaches independently. Problem statement confirmed
identical to `imo-2026-06` in `problems.jsonl` (task `proof_only`, no
numeric-answer requirement, so "verify final answer" rigor rule does not
apply — the requirement is a fully rigorous existence proof of `T,L`).

Verdicts are per-approach, per CLAUDE.md's routing (not a single whole-round
verdict).

---

## 1. intersecting-family-covering-construction — Verdict: **CHANGES REQUESTED**

Status claimed by builder: `partial`. **Confirmed correct** — this is the
honest label; the file does not overclaim `solved` even though it closes a
major gap.

### The load-bearing claim, independently re-derived

Theorem 5.1 (Master Conditional Theorem): **conditional on `(†')`** (a finite
set of primes `H` exists with `H∩rad(a_i)∩rad(a_j)≠∅` for *every* pair `i<j`
of the whole infinite sequence — i.e. FCBC), `a_{n+T}=a_n+L` holds for
**every** `n≥1`, with explicit `T=|Good|≤L` and `L_per=L=lcm(H)` exactly.

I re-derived every step from scratch, independently of the write-up:

- **Lemma A (Universal Hitting).** Trivial but load-bearing: `(†')`
  quantifies over *all* pairs `i<j` of the infinite sequence unrestricted
  (not just `i<j≤n`), so applying it to `(min(n,j),max(n,j))` directly gives
  `σ(n)∩σ(j)≠∅` for *every* `n,j`. I checked this uses no hidden induction —
  it really is a one-step consequence of `(†')`'s quantifier scope. Correct.
- **Corollary 3.1.** `min{x>a_n:x hits Σ_n} = min{x>a_n:x hits Σ_∞}`. The
  "≥" direction is trivial monotonicity (`Σ_n⊆Σ_∞`); the "≤" direction uses
  Lemma A to show `a_{n+1}` (already known via Theorem 2.2 to equal the
  left-hand min) is itself a valid candidate for the right-hand min. I
  verified the sandwich argument gives exact equality, not just an
  inequality. Correct. This is the genuinely novel move: it removes the
  "eventually" from the previously-certified Theorem 2.4 by showing
  `a_{n+1}` was hitting the *fixed*, `n`-independent target family `Σ_∞`
  all along, not just the partial `Σ_n`.
- **Lemma B.** I independently re-derived the claim that `G` restricted to
  `Good` is a single `|Good|`-cycle, including the wraparound case `k=m`
  (uses `g_1=0`, separately established since a multiple of `L` trivially
  hits everything). I hand-checked the file's own disclosed counterexample
  to the *stronger*, false claim ("`G` injective on all of `ℤ/Lℤ`") —
  `Good={0,5}⊂ℤ/10ℤ` — by direct computation: `g(1)=4,g(2)=3,g(3)=2,g(4)=1`
  all give `G=5`, confirming `G(1)=G(2)=G(3)=G(4)=5`, genuinely
  non-injective on the full domain. The file correctly does NOT attempt this
  stronger (false) claim and instead proves only the restriction to `Good`
  is bijective, which is what Theorem 5.1 actually needs. This is exactly
  the right scoping and shows real care, not a near-miss.
- **Theorem 5.1.** Telescoping-sum argument, checked line by line — correct,
  including the `L_per=L` exact computation (not just a bound), which
  strictly improves on the previously-certified Theorem 2.4.

### Independent numerical re-verification

I wrote fresh Python (not reusing the builder's code) to: (1) simulate the
true greedy sequence for `a_1∈{9,15,35,65,105,143,221,1001}`; (2) build the
exact `H` values reported in the file's table; (3) exhaustively check `H`
covers all pairs among the first 1600 terms; (4) compute `L`, `Σ_∞`, `Good`,
`T` from first principles (not copying the file's numbers); (5) check
`a_{n+T}=a_n+L` for every `n` up to `1600-T`. **Result: exact match to the
file's table in every column (`H`, `L`, `T`), zero periodicity failures**,
for all 8 cases including `a_1=35,65` — the two cases that broke round 2's
naive mechanism (confirmed: round 2's `H` was not a genuine covering set for
these, e.g. for `a_1=35` the pair `(a_3,a_4)=(42,45)` fails `{2,5,7}`-coverage;
with a genuine covering `H` the mechanism works perfectly).

### Overclaim check

The file explicitly and repeatedly labels `(†')`/FCBC as "not addressed in
this file... assigned to sibling approaches" and keeps Status `partial`.
This is the single most important overclaim check for this file (a builder
closing a major conditional theorem is exactly the situation where "solved"
might be mistakenly claimed) — **no overclaim found.** The "headline" framing
("Gap 2 is now CLOSED COMPLETELY") is accurate: Gap 2 (periodicity-from-`n=1`)
really is fully closed, conditionally, and the file says so precisely, never
implying the *whole problem* is solved.

### Verdict

**CHANGES REQUESTED.** Status is genuinely `partial` (correct, not an
overclaim) — real, gap-free, independently-reproduced progress (Theorem 5.1),
with exactly one gap remaining across the *entire* problem: FCBC itself,
explicitly and correctly out of scope for this file. This is the strongest
single result the population has produced across all 3 rounds.

---

## 2. persistent-backbone-monovariant — Verdict: **CHANGES REQUESTED**

Status claimed: `partial`. Confirmed correct.

### Re-derivation

Key Lemma (`ω`-bound): conditional on `ω(a_n)≤M` for all `n`, the Domination
Lemma's dominant prime `q*(n) ≤ M(a_1+L)` for all `n≥2`. I re-derived this
from `D_{n-1}(q*)≥(n-1)/r` (Domination Lemma) combined with
`D_{n-1}(q*)≤a_{n-1}/q*` (pigeonhole on multiples) and `a_{n-1}/(n-1)≤a_1+L`
(Lemma 1). Algebra checks out exactly as claimed — a genuine three-line
consequence of two already-certified lemmas, no gap.

Propositions ND1, ND2 (the two natural sufficiency bridges from a finite `Q`
of dominant primes to an actual FCBC covering set both fail): I independently
recomputed every `D_n(q)` value cited on the `a_1=221` and `a_1=375` traces
via fresh Python (factoring each term from scratch, not reusing the file's
factorizations). **Exact match**: `D_1(13)=1`, `D_3(17)=2` (unique max, `3`
excluded from `Q`) for ND1; `D_2(19)=0`, `D_6(19)=1` (both below threshold)
for ND2. Both negative results hold up.

### Assessment

Genuine, verified progress narrowing exactly how the necessity-only Key
Lemma cannot (by two natural mechanisms) be upgraded to sufficiency. Core
FCBC conjecture remains open. This matches the outline-reviewer's specific
request this round (attack the necessity→sufficiency bridge directly) and
the builder honestly reports failure of both attempts rather than papering
over the gap. No RETHINK — the `ω`-boundedness framing is not shown
impossible, only that these two specific mechanisms fail; a density-based
exploratory direction is honestly flagged as unproven, not misrepresented as
a result.

**Verdict: CHANGES REQUESTED.**

---

## 3. forced-primes-well-ordering — Verdict: **CHANGES REQUESTED**

Status claimed: `partial`. Confirmed correct. New approach this round
(copy-branch of persistent-backbone-monovariant per the outline-reviewer's
explicit copy mechanism, distinct technique).

### Re-derivation

- **Lemma FN**: trivial, correct one-line consequence of the covering
  definition.
- **Lemma FX** (disjoint-imprint necessity): proof by contradiction, checked
  — correct. I independently recomputed the two numerical examples cited
  (`a_1=221` pair `(4,5)`: `G_4=rad(255)∩{13,17}={17}`,
  `G_5=rad(260)∩{13,17}={13}`, disjoint; `a_1=375` pair `(3,7)`:
  `G_3=rad(380)∩{3,5}={5}`, `G_7=rad(399)∩{3,5}={3}`, disjoint) — exact
  match.
- **Lemma FX2** and the channel-bound corollary (`≤3^{ω(a_1)}` channels):
  checked, correct, elementary.
- **Generalized Lemma C**: same proof template as the already-certified
  Lemma C, applied to an arbitrary infinite index subsequence — checked,
  correct, no new subtlety versus the original.
- **Conditional Markov density bound**: `Σ_q D_N(q)=Σ_{i≤N}ω(a_i)≤NM_0`
  (double-counting, correct) `⟹` `|{q:D_N(q)≥N/M_0}|≤M_0^2` — correct
  averaging argument. The accompanying "cycling primes" obstruction analysis
  (why this pointwise bound cannot control the union over all `N`) is
  correctly reasoned, not just asserted: a prime's density can drop below a
  rising threshold even though its raw count is non-decreasing.

### Assessment

This is a genuinely new, correct, non-trivial structural reduction (FCBC ⟺
finitely many independent channel questions, most of which are already
resolved), plus two more mechanisms tried and rigorously ruled out. Matches
the outline-reviewer's request for a "precise quantitative bridge" rather
than a vague plausibility claim. Core FCBC ("Lemma FF") remains open, honestly
reported as such.

**Verdict: CHANGES REQUESTED.**

---

## 4. explicit-window-backbone-construction — Verdict: **CHANGES REQUESTED**

Status claimed: `partial`. Confirmed correct. First build this round (was
opened but not built in round 2, `expanded:0` before this round).

### Re-derivation

**Lemma W1 (Equivalence Lemma)**, the most important new result here: FCBC
⟺ the window Key Lemma (`∃K` with `H_K` covering). I checked the
`(⇒)` direction step by step: `H':=H∩Π` (Π = all primes ever appearing) is
finite, nonempty (via pair `(1,2)`), and itself covering (any witnessing
prime for a pair automatically lies in `Π`, hence in `H'`); then
`K:=max_{p∈H'}μ(p)` (well-defined by well-ordering, `H'` finite) gives
`H'⊆H_K`, hence `H_K` covers. No circularity, no gap — a clean, correct
biconditional. This is a genuinely valuable unifying result: it formally
proves the three "Gap-1" approaches are attacking the *identical*
proposition (not three related-but-different ones), which is useful
knowledge for future rounds (any one closing FCBC closes all three, via this
explicit conversion).

**Lemma W2 (Patch Lemma)** and **Lemma W3 (Minimal Radical Reduction
Lemma)**: both checked line by line, both correct and unconditional
(no FCBC dependence). W3 in particular is a clean piece of independent
structural content about the recursive definition itself.

### Independent numerical re-verification

I wrote fresh Python to compute the minimal sufficient `K` for the same 10
of 11 tested `a_1` values (all except `4199`, to save time), using an
independent construction (`H_K:=∪_{m≤K}rad(a_m)`, exhaustive pairwise check
via distinct realized signatures). **Exact match to the file's table for
every one of the 10 values checked** (`15→K=2`, `65→K=3`, `91→K=2`,
`105→K=2`, `143→K=3`, `221→K=4`, `247→K=4`, `375→K=3`, `1073→K=3`,
`4087→K=2`), confirming the falsification of "`K=K(ω(a_1))` alone" (`ω(a_1)=2`
gives `K∈{2,3,4}` across different `a_1`, so no such formula can exist).

### Assessment

Genuine progress: a real unifying equivalence result plus two more
structural lemmas, plus a correctly-verified falsification of a natural
simplifying conjecture, plus an honest diagnostic (wrong-direction
monotonicity of the natural candidate monovariants) explaining exactly why
the approach's own originally-envisioned mechanism cannot work internally.
The approach does not claim victory anywhere it hasn't earned it. Core
Key Lemma/FCBC remains open.

**Verdict: CHANGES REQUESTED.** (Not RETHINK: the approach's core target
(window construction) is now proven equivalent to the shared FCBC target, so
it is not a dead framing — it merges productively with the sibling
approaches rather than being invalidated.)

---

## Certified lemmas (new this round)

All independently re-derived/re-verified as described above; all held to
the full bar (sorry-free, statement no stronger than what was actually
proved, conditional hypotheses stated explicitly where present). Written to
`results/imo-2026-06/lemmas/`:

1. `lemma-omega-bound-key-lemma.md` — Key Lemma (ω-bound), conditional on
   `ω(a_n)=O(1)`.
2. `proposition-ND1-ND2-domination-mechanisms-insufficient.md` —
   unconditional negative results (two Domination-Lemma-based sufficiency
   mechanisms both fail).
3. `lemma-FN-FX-FX2-forced-primes-reduction.md` — unconditional channel
   reduction of FCBC (`≤3^{ω(a_1)}` independent sub-questions, finite-class
   channels resolved for free).
4. `lemma-C-generalized-subsequence.md` — unconditional generalization of
   Lemma C to arbitrary index subsequences, plus the flagged negative finding
   (extended-imprint-overlap conjecture false, `a_1=247`).
5. `lemma-conditional-markov-density-bound.md` — conditional averaging bound
   plus its permanent "pointwise, not cumulative" disclaimer.
6. `lemma-W1-equivalence-key-lemma-FCBC.md` — unconditional: window
   construction ⟺ FCBC.
7. `lemma-W2-W3-patch-and-minimal-radical-reduction.md` — unconditional Patch
   Lemma and Minimal Radical Reduction Lemma.
8. `theorem-5.1-master-conditional-theorem.md` — the round's headline result:
   conditional on FCBC, `a_{n+T}=a_n+L` for every `n≥1` exactly (Lemma A,
   Corollary 3.1, Lemma B, Theorem 4.1/5.1 all included and certified
   together as one coherent chain).

No submitted lemma was rejected — all held up under independent
re-derivation and (where numerical claims were made) independent
re-simulation with fresh code.

## current.md

Rewritten (reviewer-owned) to reflect the round-3 state: Status remains
`partial`, but the "Current best" section now states precisely that the
entire problem reduces to one gap (FCBC), with Case I unconditionally solved
and Case II fully solved *conditional on FCBC* via Theorem 5.1. This is a
materially sharper statement of the remaining work than round 2's current.md
(which still listed two independent gaps). File at
`results/imo-2026-06/current.md`.

## Population-level assessment for next round

The problem is not solved: FCBC (equivalently the Key Lemma / Lemma FF) is
the single remaining gap, attacked this round by 3 independent techniques,
none successful, but real narrowing achieved by all 3 (channel reduction,
two more ruled-out sufficiency mechanisms, an equivalence unifying the whole
Gap-1 sub-population, a falsified simplifying conjecture). Given
`explicit-window-backbone-construction`'s Lemma W1 proves all three
approaches are literally the same target, next round's outliner should
seriously consider whether continuing to run three separate techniques on
the identical proposition still counts as framing-diversity (per CLAUDE.md's
"single-gap trap" warning) or whether a genuinely different angle on FCBC
itself (not just a different bookkeeping scheme for the same necessity/
sufficiency split) is now overdue — all three current techniques bottom out
on essentially the same "pointwise/necessity information doesn't give
cumulative/sufficiency information" wall (explicitly identified as the same
obstruction in both persistent-backbone-monovariant's ND1/ND2 and
forced-primes-well-ordering's Markov-bound analysis this round).
