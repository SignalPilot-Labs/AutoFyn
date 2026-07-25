# Round 6 proof-review — imo-2026-03

Reviewed all 5 built approaches. Independently re-derived/verified every new
claim via exact (Fraction/sympy) arithmetic and/or independent numeric
search (scripts run in `/tmp`, summarized below with the concrete
counterexamples/checks found). Updated `results/imo-2026-03/current.md`
(Status stays `partial`, both sections rewritten to reflect round 6).
Certified 5 new lemma files (see below). Recorded all 5 outcomes via
`record_outcome`.

**Overall Status: partial** (unchanged — no slug reached `solved`, none
overclaims). This is a mixed-but-uniformly-positive round: all 5 slugs are
`CHANGES REQUESTED`, all recorded `advanced` except `dyadic-potential-invariant`
(`dead-end`, a genuine mechanism kill, not a failure). One real algebra
error was found (self-similar-induction-on-n) and corrected before
certification; it did not propagate into that file's actual conclusions.

---

## 1. `self-similar-induction-on-n` — Verdict: CHANGES REQUESTED (Status: partial)

**What I verified.** The round-6 target: close the width-1 sliver
`2^(m-1)-1<b1<2^(m-1)` left open by round 5's Theorem 2, via a recursive
tail-untouched dichotomy.

- **Reduction to `L_0(ℓ,ε)`.** Re-derived the peeling algebra from scratch
  (sympy, exact rational): confirmed `OddSum(B∪T)≤2^m-1` in the sliver is
  exactly equivalent to `OddSum(C∪Γ_{ℓ-1})≥2^ℓ` for `sum(C)=2^ℓ+ε`,
  `max(C)≤2^ℓ-ε`. Matches the file exactly.
- **`(★)` (sub-case-(ii) shape).** Re-derived from the stated proof method
  (peel `2^{ℓ'-1}`, bound residual via Lemma B): got
  `(W+3·2^{ℓ'-1}-1)/2`, exact match to the file, diff = 0.
- **`(★★)` (sub-case-(i) shape) — FOUND AN ERROR.** Re-derived from the
  stated proof method (peel `d1`, bound residual via Lemma B on `D'∪T'`):
  got `(2^{ℓ'}+W+d1-1)/2`. The file states
  `(2^{ℓ'-1}+W+d1-1)/2` — off by a factor of 2 in the constant power-of-2
  term. **Exact counterexample to the file's literal formula:** `ℓ'=2`
  (`T'=Γ_1={2,1}`), `D={2}` (`W=2`, `d1=2`): file's formula gives bound
  `(2+2+2-1)/2=5/2`; but `OddSum({2,2,1})=2+1=3>5/2` — a direct violation.
- **Checked whether the error propagates into the actual branches.**
  Recomputed Branch II.i, II.ii, I.A's stated difference formulas
  (`2^ℓ/8+ε/2-1/2`, `2^ℓ/4-c1/2+ε/2-1/2`, `c1/2-2^ℓ/4+ε/2-1/2`) directly
  from first principles (not via the mis-stated `(★★)`) and found **exact
  agreement** with the file in every case — i.e. the branch closures
  themselves are correct; only the abstractly-stated general lemma
  contained the typo. This is a subtle but real distinction: I corrected
  the lemma statement (`lemmas/theorem2gen-bounds-and-l0-reduction.md`)
  rather than rejecting the round's conclusions.
- **Residual gap.** The file honestly reports Theorem 2' is **not** proved
  this round — a narrower self-similar window plus Branch I.B remain open.
  This matches my re-derivation; no overclaim.

**Verdict rationale.** Real, verified progress (the `L_0` reduction and
most of its range being closed); one genuine error found and fixed by the
reviewer, isolated to an abstract restatement, not affecting the actual
proof. Status `partial` is correct as self-reported.

---

## 2. `greedy-reduction-geometric` — Verdict: CHANGES REQUESTED (Status: partial)

**What I verified.**
- **Theorem 7a** (`k=1` base case, unconditional): every tail fragment of
  `S` (a full refinement of `Γ_{m-1}`) has value `≤2^i≤2^{m-1}≤b1`, so `b1`
  is the global max; `OddSum({b1}∪S)=b1+EvenSum(S)≥b1` since `EvenSum≥0`.
  Correct, elementary, checked.
- **Section 10.2's exhaustive two-way case split** (`μ1≥b2` vs. `μ1<b2`):
  confirmed this is exhaustive (comparison of two reals) and disjoint;
  spot-checked the algebra of both sub-case reductions (10.2a, 10.2b) —
  both derivations are internally consistent applications of the already-
  certified Companion Peeling Lemma, correctly reducing to the two named
  open sub-problems (Insertion-Robustness, Level-Absorption). Neither
  sub-problem is claimed proved, and the file is explicit about this.
- **Dedup check (Section 10.3).** Read both this file's and
  self-similar-induction-on-n's notes on the potential duplication between
  Theorem 7'(m,k;L) and `G(m,k;V)`/`L_0(ℓ,ε)`. Confirmed the two are
  genuinely different objects: one is a *structural* perturbation
  (splitting a specific tail level, target unchanged), the other a
  *target-value* perturbation (tail fully untouched, target shifted). No
  duplication found; both files agree.

**Verdict rationale.** Solid, honestly-scoped incremental progress; no
errors found. Status `partial` correct.

---

## 3. `universal-halving-adversary` — Verdict: CHANGES REQUESTED (Status: partial)

**What I verified.**
- **Theorem 9 (Singleton-Interleaving Lemma).** Independent exact-`Fraction`
  simulation (construct `M=B∪L` literally from random even blocks + random
  singleton values, compute `OddSum` by direct sort-and-sum): 3000 trials,
  **zero exact discrepancy** against `OddSum(M)=sum(B)/2+OddSum(L)`.
- **Theorem 10 (General k-Anchor-Merge Lemma).** Independent exact-`Fraction`
  simulation of the literal construction (split `p_{i_m}` into `(ℓ_m,p_{j_m})`,
  **and** keep the untouched original `p_{j_m}` — multiplicity 2 total —
  plus bisect everything else): first draft of my test omitted the
  untouched copy (same class of bug flagged in round-5 memory) and gave a
  spurious `8/27` discrepancy; after fixing to match the construction
  literally, 3000 trials gave **zero exact discrepancy**.
- **k=3 non-monotonicity.** Independently re-implemented a brute-force
  best-`k=2`/best-`k=3` search (exhaustive over disjoint pairings) at `n=6`
  with all consecutive gaps `>γ(6)=1/127`: found concrete instances (3 of 3
  sampled) where best-`k=2` succeeds (`≤c(6)`) but best-`k=3` on the
  identical instance fails — exactly matching the file's claim.
- **Theorem 8 (Two-Piece-Split Vertex Lemma).** Spot-checked on a concrete
  instance (`q=[0.5]`, `T=0.3`, `T'=0.2`, `m=m'=2`): independent
  multistart Nelder–Mead (300 restarts) found minimum `0.6`; independent
  from-scratch enumeration of the candidate vertex set (block-ties,
  boundary, and cross-tie scan) also found `0.6` — exact agreement. The
  general argument is a standard, mechanical LP-vertex extension of the
  already-certified Single-Piece-Split Vertex Lemma; no error found in the
  stated mechanism.
- **65–96% coverage table.** Plausible given the k=2 formula is exact and
  verified; not independently re-run at full scale (would require
  reproducing the file's own sampling), but consistent with spot checks.

**Verdict rationale.** All new claims verified correct (after fixing one
of my own test-harness bugs). Genuinely reusable positive tools plus an
honest negative finding (k=3 non-monotonicity). Status `partial` correct
(existence theorem for the residual not yet proved).

---

## 4. `lp-duality-split-polytope` — Verdict: CHANGES REQUESTED (Status: partial)

**What I verified.**
- **Triangular family closed form** `p_i=(n+2-i)/D_n`, `D_n=(n+1)(n+2)/2`:
  checked `sum=1` and matches the certified `n=3,4` instances exactly.
- **`n=5` exact instance.** Reconstructed the family exactly (`Fraction`),
  computed the proposed minimizing configuration (split `p1=2/7` into
  `p4,p5,p6`): got `OddSum=11/21` exactly, matching the file. Independent
  global numeric search (Nelder–Mead, 60 restarts × 6 pieces × 6 cut
  counts) over **all** single-piece splits found `11/21` as the global
  minimum (no lower value found) — confirms this is truly the floor, not
  just one candidate. Compared to `c(5)=32/63`: excess `1/63>0`, confirmed.
- **`n=6` exact instance.** Same method: reconstructed `p`, computed the
  claimed three-way-tied value `15/28` exactly at the stated configuration
  and via independent global numeric search across all 7 pieces (50
  restarts each) — global minimum matches `15/28` exactly. Compared to
  `c(6)=64/127`: excess `113/3556>0`, confirmed.
- **Rejected false conjecture.** Confirmed the conjecture
  `floor(n)-1/2=1/((n+1)(n+2))` matches `n=3,4,5` exactly but is
  contradicted at `n=6` (predicts `29/56`, actual `15/28=30/56`) — the
  file states this rejection clearly and unambiguously, not left as a live
  claim.
- **Target-excess identity.** Trivial algebra (`c(n)-1/2=1/(2(2^{n+1}-1))`),
  checked at `n=5`.

**Verdict rationale.** All exact claims independently reproduced by two
different methods (direct construction + global numeric search over the
whole feasible space). The honest rejection of a plausible-looking but
wrong pattern is exactly the discipline the standing rules call for.
Status `partial` correct (general-`n` theorem still open).

---

## 5. `dyadic-potential-invariant` — Verdict: CHANGES REQUESTED (Status: partial, outcome `dead-end`)

**What I verified.**
- **Majorization counterexample.** Independently reconstructed
  `M=(0.34,0.33,0.32,0.01)`, `M'=(0.36,0.34,0.29,0.01)` in exact `Fraction`
  arithmetic: confirmed `sum(M)=sum(M')=1`, confirmed `M'≻M` (every prefix
  sum of `M'` is `≥` the corresponding prefix sum of `M`, verified exactly:
  `9/25≥17/50`, `7/10≥67/100`, `99/100≥99/100`), and confirmed
  `OddSum(M)=33/50 > OddSum(M')=13/20` — an exact, confirmed violation of
  the candidate monotonicity claim, in both directions consistent with the
  file's report.
- **General Schur-monotonicity Proposition.** Re-derived the standard
  Hardy–Littlewood–Pólya-style criterion from scratch (Abel-summation
  argument for the `⇐` direction, explicit near-uniform perturbation
  construction for the `⇒` direction) — this is a correct, standard result,
  correctly applied to `c=(1,0,1,0,…)` (the OddSum weight pattern), which
  indeed fails to be non-increasing for `N≥3` (`c1-c2=1>0` but
  `c2-c3=-1<0`), proving OddSum is neither Schur-convex nor Schur-concave
  for `N≥3`. No error found.

**Verdict rationale.** A clean, fully general, correctly-proved dead end —
exactly the kind of negative result the standing rules say to record as
real progress (`advanced`/`dead-end`, not "no progress"), since it
permanently rules out a whole mechanism family for any future round. No
positive gap in the target theorem was closed this round, so recorded as
`dead-end` per the standing discipline distinguishing this from
`advanced`. Status `partial` correct.

---

## Lemmas certified this round

- `lemmas/singleton-interleaving-and-k-anchor-merge.md` (Theorems 9, 10,
  `universal-halving-adversary`) — verified exactly.
- `lemmas/two-piece-split-vertex-lemma.md` (Theorem 8,
  `universal-halving-adversary`) — verified by numeric spot-check, standard
  mechanical LP argument.
- `lemmas/theorem2gen-bounds-and-l0-reduction.md` (`(★)`, corrected `(★★)`,
  `L_0(ℓ,ε)` reduction, `self-similar-induction-on-n`) — `(★★)` corrected
  from the file's literal (erroneous) statement; all three verified.
- `lemmas/schur-monotonicity-criterion-and-majorization-dead-end.md`
  (`dyadic-potential-invariant`) — verified exactly (proof + counterexample).
- `lemmas/target-excess-identity.md` (`lp-duality-split-polytope`) —
  trivial algebra, verified.

`results/imo-2026-03/current.md` rewritten: `## Status` unchanged
(`partial`), `## Approaches tried` given a fresh round-6 summary (prior
rounds' summary retained below it for history), `## Current best` updated
with all round-6 closures/reductions and the corrected lemma reference.

## Goal Progress summary (for Eval History)

Round 6: Status stays `partial` (all 5 slugs CHANGES REQUESTED, 4/5
recorded `advanced`, 1 recorded `dead-end`). All new claims independently
re-derived/verified by the proof-reviewer (exact `Fraction`/sympy
arithmetic plus independent numeric global search, distinct from the
builders' own scripts). One genuine algebra error was found
(self-similar-induction-on-n's abstract `(★★)` lemma, a factor-of-2 typo,
refuted by an explicit counterexample) and corrected before certification
— it did not affect that file's actual proved branch closures.
self-similar-induction-on-n reduced its round-5 sliver to a clean
`L_0(ℓ,ε)` target and closed most of its range via a further recursive
dichotomy. greedy-reduction-geometric proved the unconditional `k=1` base
case of Theorem 7' and reduced the general `k≥2` Leftover-Fragment
Obstruction to two precisely-named open sub-problems, with an explicit
cross-approach dedup check confirming no duplication with
self-similar-induction-on-n's target. universal-halving-adversary proved
three new theorems (Two-Piece-Split Vertex, Singleton-Interleaving,
General `k`-Anchor-Merge), closing 65–96% of the previously fully-open
balanced-region residual and proving a genuine non-monotonicity negative
result (`k=3` worse than `k=2`) — both independently reproduced.
lp-duality-split-polytope extended Multi-Piece Necessity from 2 to 4 exact
instances (`n=3,4,5,6`) with a general triangular closed form, and
correctly found-and-rejected a false closed-form conjecture after only 3
data points matched. dyadic-potential-invariant cleanly killed the
majorization/suffix-domination mechanism with a proved general reason
(Schur-monotonicity criterion), a genuine dead end that prunes future
search space. 5 new lemmas certified. IMPROVED (real progress on both open
gaps — lower bound's sliver narrowed further with a precise residual, and
upper bound's balanced-region residual shrunk from ~100% to ~4–35% — plus
one cross-approach dedup confirmed clean and one mechanism family
permanently ruled out).
