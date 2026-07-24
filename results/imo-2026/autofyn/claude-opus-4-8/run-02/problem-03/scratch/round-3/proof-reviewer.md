# Proof-reviewer — round 3, imo-2026-03

Problem: IMO 2026 P3. Answer `c(n) = 2^n/(2^{n+1}−1)`, `D_n = 2^{n+1}−1` (pinned, confirmed).
The problem is a "find the largest c" — needs BOTH a lower bound (Liu Bang guarantee, GAP-L) and
an upper bound (Xiang Yu strategy, GAP-U). Two slugs reviewed independently below.

---

## Slug 1: alternating-sum-threshold-potential  (owns GAP-U)

**Verdict: CHANGES REQUESTED. True Status: partial (GAP-U itself = verified milestone).**

Builder claims GAP-U (upper bound `c(n) ≤ 2^n/D_n`) is COMPLETELY closed. I scrutinized hard and
**concur: GAP-U is closed and rigorous** (one trivial edge patched by me). The approach's overall
Status is correctly `partial` because it imports the lower bound (GAP-L) from the sibling, which
is not yet complete — so this slug does not solve the whole problem, hence not APPROVE.

Load-bearing step re-derived from scratch and independently verified:

- **DELETE/SUBTRACT reduction** — valid. I checked the invariant "full multiset = visible
  multiset ∪ equal-valued invisible pairs" is preserved by both operations, each is one cut,
  mass-conserving, drops visible count by 1, and when visible = single piece, P1 gives
  `f = that value`. Correct.
- **Lemma A (delete-subtract-reachability): `g_{m−1}(P) ≤ φ(P)`** — correct, with ONE edge gap I
  found and patched. In the all-±1 branch the proof does "SUBTRACT `(a_p,a_q)`" but if
  `a_p = a_q` this is `d=0`, an invalid endpoint cut, and "reach a single piece" fails. Fix
  (verified, now in the lemma file): choose the minimiser with **fewest nonzero coordinates**;
  then a cross-pair `a_p ≠ a_q` always exists (else zeroing an equal `+/−` pair gives a nonzero
  minimiser of the same value with fewer nonzeros — contradiction), so `d>0`. The `φ(P)=0` case
  is met by stopping (`f≥0`). Conclusion unaffected. **Numeric: 0 violations / 3000** (incl.
  all-equal / d=0 configs).
- **Lemma B (subset-sum-pigeonhole): `φ(P) ≤ s/(2^m−1)`** — correct. The cell phrasing has a
  trivial endpoint imprecision (the full-set sum `s` sits at the boundary); the airtight form is
  sorted-consecutive-gaps: `2^m` sums incl. `0` and `s`, `2^m−1` gaps summing to `s`, min gap
  `≤ s/(2^m−1)`. Verified: worst ratio exactly 1.0, dyadic tight, `n≤5`.
- **Invariant (I) `g_b(P) ≤ s/D_b` for all `m ≤ b+1`** — complete. Cases `b≥m` (bisect all ⇒ all
  values even multiplicity ⇒ `f=0`) and `b=m−1` (`g_{m−1} ≤ φ ≤ s/(2^m−1) = s/D_{m−1} = s/D_b`)
  exhaust `b≥m−1`. **The round-2 "middle regime" is genuinely dissolved** — no amortisation
  needed. At `b=n, s=1`: `M* ≤ 1/D_n`, so `c(n) ≤ 2^n/D_n`. **Numeric invariant check: 0
  violations / 3000** over random `(b≤5, m≤b+1)` using a proper atomic-move search (per my role
  rule — not naive random cuts).

Scores: Correctness 9.5/10 (one patchable edge), Completeness 9.5/10, Progress 10/10 (an entire
bound closed; the largest single advance of the run).

Lemmas certified: **subset-sum-pigeonhole** (clean) and **delete-subtract-reachability** (after
my fewest-nonzero-minimiser patch) — both now `CERTIFIED` in `results/imo-2026-03/lemmas/`.

Gap remaining for this slug to reach `solved`: only GAP-L (owned by the sibling). Also: fold the
d=0 patch and the sorted-gaps phrasing into the approach's `## Full proof` narrative.

---

## Slug 2: self-similar-recursion  (owns GAP-L)

**Verdict: CHANGES REQUESTED. True Status: partial (matches builder's honest self-assessment).**

Builder honestly flags a residual. I verified the new lemmas are rigorous and tie-safe, the
degenerate induction is sound, and the flagged residual is indeed the ONLY remaining gap.

- **Lemma I (cut-slide-derivative, valid at ties)** — correct. Re-derived the block-contribution
  algebra: increasing a tied piece sends it to rank `a_l` (slope `σ_{a_l}=s^↑`); decreasing sends
  it to rank `b_l` (slope `−σ_{b_l}=−s^↓`). Numerically confirmed (measured `−1`, `+1` on a
  3-way-tie config, matching the formula).
- **Lemma J (tie-free non-degenerate minimizer ⇒ monochromatic)** — correct. Tie-free ⇒ blocks
  size 1 ⇒ `s^↑=s^↓=σ`. Interior (non-degenerate) local min ⇒ both slide slopes `≥0` ⇒
  `σ(q_i)=σ(q_{i+1})` for adjacent sub-pieces ⇒ each original piece monochromatic ⇒
  `f = Σ ε_k 2^k`, an odd integer `≥0` ⇒ `f ≥ 1`. Sound.
- **Degenerate leg** — sound. A length-0 sub-piece means the configuration is realizable with
  `≤ N−1` cuts, handled by the strong induction on cut count `N` (base `W_n`, integer, `f≥1`).
- **Residual is the only gap** — confirmed. The global minimizer (Weierstrass) is either tie-free
  non-degenerate (Lemma J), degenerate (IH), or **non-degenerate pinned at a rank tie**. The last
  is open. The builder's example `{4/3,4/3,4/3,2,1}` is a genuine refinement of `W_2`
  (`Σ=7=D_2`, 2 cuts), `f = 5/3 ∉ ℤ` (verified), so the odd-integer floor does not reach it, and
  P1-deletion of `{v,v}` removes mass `2v`, breaking the dyadic conservation. The residual
  inequality `f ≥ 1` is numerically true (`min=1`, `n≤4`) but unproven. No overclaim: the
  builder's Status `partial` and its residual description are accurate.

Scores: Correctness 9.5/10, Completeness 7.5/10 (real residual), Progress 8.5/10 (continuous case
reduced from "all non-integer vertices" to "tied non-degenerate vertices" only).

Lemmas certified: **cut-slide-derivative** (Lemma I) and **tiefree-minimizer-monochromatic**
(Lemma J) — both now in `results/imo-2026-03/lemmas/`.

Gap to attack next round: `f ≥ 1` at a non-degenerate minimizer pinned purely at a rank tie
(stable P1 matched pair `{v,v}`, `v` arbitrary real). P1-deletion is obstructed (breaks
conservation); needs a `W_n`-specific argument at tied non-degenerate vertices. Do NOT reintroduce
parity-of-pieces (dead, d=3) nor the blanket "cutting a non-max piece never helps XY" (FALSE).

---

## Goal progress (raw notes)

- **current.md updated**: Status remains **partial**. GAP-U marked CLOSED; GAP-L reduced to the
  single "tied non-degenerate vertex" residual. No `## Full proof` assembled — the problem is not
  solved (one lower-bound residual open).
- **Milestone**: the UPPER BOUND `c(n) ≤ 2^n/D_n` is now fully proven and certified. This is the
  first bound (beyond `n=1`) to be completely closed. Only the GAP-L residual stands between the
  workspace and a full `solved`.
- **Lemmas cache now 12**: added `subset-sum-pigeonhole`, `delete-subtract-reachability` (patched),
  `cut-slide-derivative`, `tiefree-minimizer-monochromatic`.
- **Ranking**: self-similar-recursion Elo 1584 (advanced) > alternating-sum-threshold-potential
  1550 (verified-milestone). Both live, both CHANGES REQUESTED.
- **Next round**: single focus — close the GAP-L tied-non-degenerate-vertex residual on
  self-similar-recursion (the ONLY gap left in the whole problem); if closed, assemble the full
  proof (GAP-U is done and certified) → candidate for `solved`. Keep alternating-sum-threshold as
  the certified GAP-U source. Consider whether a fresh framing can attack the tied-vertex residual
  (e.g. a perturbation/exchange that removes the tie without raising f, or bounding f directly at
  matched-pair-pinned vertices).
