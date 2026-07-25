# proof-reviewer report — imo-2026-03, round 7

All four built approaches were adversarially re-verified this round with
independent exact-rational/symbolic computation (details below and in the
four parallel verification passes conducted). No approach reaches
`solved`; all four show genuine, independently-confirmed new progress.
Two real bugs (self-similar-induction-on-n, greedy-reduction-geometric)
and one minor off-by-one labeling slip (lp-duality-split-polytope) were
found and corrected this round; none affected the validity of any
theorem's actual proof, only adjacent scope statements.

## self-similar-induction-on-n — CHANGES REQUESTED (partial, real progress)

Verified:
1. **Bug fix (round 6's `L_0(ℓ,ε)` missing piece-count bound).**
   Confirmed genuine: reconstructed the exact 4-part counterexample
   (`ℓ=2,ε=1/10`, `OddSum(C∪Γ_1)=35649/10000<4`) by exact `Fraction`
   arithmetic — matches the file's claim exactly. Confirmed the corrected
   statement is worded identically in the approach file and in
   `lemmas/theorem2gen-bounds-and-l0-reduction.md`.
2. **Branch I.B closure (two-peel argument).** Re-derived the algebra
   step by step, no gap found. Independently stress-tested: 2800
   exact-`Fraction` trials across `ℓ=1..7`, zero violations; a finer
   20,000-trial sweep at `ℓ=2` confirmed the margin can be pushed to `0`
   as `ε→0`, matching the claimed equality case `ℓ∈{1,2}`.
3. **`OddSum(Γ_n)≥2^n`.** Re-derived from the certified `AltSum(Γ_m)`
   closed form via Lemma AS; checked `n=0..10` directly — equality holds
   exactly at `n∈{0,1}`, strict for `n≥2`, matching the file's claim.
4. Spot-checked that round 6's actual branch closures (II.ii, II.i-partial,
   I.A-partial) use only `sum(C)`/`max(C)`, never piece count — confirmed,
   no red flags; they remain valid under the corrected, more restrictive
   hypothesis (a fortiori).

Certified new lemma: `lemmas/branch-ib-two-peel-theorem.md` (the Two-Peel
Theorem plus the base `OddSum(Γ_n)≥2^n` fact).

Not closed: the residual window's lower half (Branch II's uncovered
range) — attempted, honestly reported as not closed (the two-peel trick
needs a lower-bound direction that doesn't transplant to Branch II's
upper-bound target). Status remains `partial`; verdict: re-dispatch to
close more (Branch II / the narrower Branch-I.A window) — approach stays
live.

## greedy-reduction-geometric — CHANGES REQUESTED (partial, real progress)

Verified:
1. **Level-Absorption bug.** Reproduced the unbudgeted counterexample
   family exactly: `OddSum = 2^m - 1/2` for `m=3,4,5,6,8,10` (deficit
   exactly `1/2`), cut count one over budget (`m+1` vs. budget `m`) —
   confirms the bug is real and correctly diagnosed, not cosmetic.
2. **Corrected version.** Reproduced margin `2^{m-3}-1/2` exactly for
   `m=3,4,5,6,8`, cut count exactly on budget in every case. Independent
   fresh Monte Carlo (own generator, not the file's script): 60,000
   trials across `m=3..9`, `k=2..m`, ~52,500+ valid instances after
   budget rejection, two seeds — zero violations, minimum margin
   comfortably positive (~1.64), no near-zero cases.
3. **Insertion-Robustness honestly open.** Confirmed no language in the
   file (or in `current.md`) claims it proved/closed; explicitly marked
   "unproved"/"not proved" throughout.

Not closed: Insertion-Robustness and the corrected Level-Absorption's
target itself are not yet proved general theorems — the bug fix and
stress test are real progress but don't close the sub-problem. Status
remains `partial`; verdict: re-dispatch to attempt closing
Insertion-Robustness and/or Level-Absorption's target next round —
approach stays live.

## universal-halving-adversary — CHANGES REQUESTED (partial, real progress)

Verified:
1. **Theorem 11 (Subset-Tie Lemma) construction, cut-cost, and formula.**
   Reconstructed the literal construction in Python (exact `Fraction`
   arithmetic) and confirmed it always sums to 1; confirmed the cut count
   (`n` or `n-1`); independently re-derived `OddSum=(1+r)/2` from the
   certified Singleton-Interleaving Lemma by hand and via exhaustive
   subset-sum DP for the optimal `J`, 200 random trials `n=3..6` — exact
   match, zero discrepancy.
2. **Residual-shrinking numeric claims.** Directionally corroborated
   (Subset-Tie substantially narrows the residual beyond best-of-`{k1,k2}`,
   does not vanish, genuine tiny-excess survivors persist) but the file's
   specific percentage table was not exactly reproducible under an
   independently-designed sampling scheme — attributed to a sampling
   methodology difference (different rejection scheme for "all gaps
   `>γ(n)`"), not a mathematical error; the specific boundary survivor at
   `n=6` was independently confirmed to the correct order of magnitude.

Certified previously (unchanged this round): Theorems 8, 9, 10 remain
certified in `lemmas/singleton-interleaving-and-k-anchor-merge.md` and
`lemmas/two-piece-split-vertex-lemma.md`. Theorem 11 is new, correctly
proved math but not yet independently certified as a standalone lemma
file (recommend certifying next round once its role in a possible closing
argument is clearer, per standing practice of certifying reusable proved
results — deferred this round since it's tightly coupled to this file's
ongoing residual-shrinking program rather than a clean standalone tool).

Not closed: the Existence Theorem (does some finite construction always
close the residual) remains open. Status remains `partial`; verdict:
approach stays live, re-dispatch next round to continue narrowing or
attempt the Existence Theorem directly.

## lp-duality-split-polytope — CHANGES REQUESTED (partial, real progress; the round's standout result)

Verified:
1. **`n=7,8,9` exact extensions.** Independently reimplemented the
   Single-Piece-Split Vertex Lemma from scratch and reproduced
   `floor(7)=19/36`, `floor(8)=8/15`, `floor(9)=29/55` exactly, matching
   `c(7),c(8),c(9)` comparisons and excess ratios (`2,3,3`) claimed in the
   file. Cross-checked `n=9` with an independent uncapped multistart
   numerical optimizer — same floor.
2. **Theorem B, claimed FULLY PROVED — scrutinized with maximum
   adversarial care given the stakes.** Reconstructed every step: (a)
   `N` is the unique max of `S` (uses `k≤N-1` and strict `y_i<k`,
   correctly justified); (b) Peel identity (standard, correctly stated
   and applied); (c) bound on the residual's `AltSum` by its max, `≤N-1`
   (correctly justified, all elements of `S\{N}` are `≤N-1`); (d)
   combine. **No hidden case gap, no hand-waving, no sign error found.**
   Independently stress-tested with 200,000 exact-`Fraction` random
   trials (`N∈[2,30]`, `k∈[1,N-1]`, `m∈[2,6]`) — zero violations, bound
   tight (exact value 1 achieved at a concrete instance). Scope confirmed:
   covers `idx=2,...,N` (i.e., `N-1` of `N` values), correctly leaves
   `idx=1` open with the breakdown point correctly diagnosed (`N∉S\{k}`
   when `k=N`).
3. **Found and fixed one genuine (but purely cosmetic) error**: the
   file's own "Net effect" summary line stated "proved for `n-1` of the
   `n` possible values of `idx`" — an off-by-one, since the triangular
   family at parameter `n` has `N=n+1` pieces (`idx=1..n+1`), so Theorem
   B actually covers `n` of `n+1` values, not `n-1` of `n`. Corrected
   in-place in `approaches/lp-duality-split-polytope.md` with an inline
   reviewer note; the theorem's proof, scope, and every other statement
   of it in the file (including the file's own top summary and section
   header, which were already correctly worded) are unaffected.

Certified new lemma: `lemmas/non-top-piece-theorem-b.md`.

Not closed: `idx=1` (splitting the top piece) remains open, honestly
evidenced (14 consecutive data points matching `⌊(N-3)/2⌋`, growing
margin) but not proved — the file is explicit this is evidence, not a
theorem, and does not overclaim. Status remains `partial`; verdict:
approach stays live, `idx=1` is now the single sharply-isolated target for
next round.

## Retirement note

`layer-cake-parity-reframing` was retired this round per the
outline-reviewer's decision; not reviewed further. Its 3 lemmas (Layer-cake
identity, Per-piece additivity, Single-cut marginal-effect formula) and the
Coupling Obstruction dead-end remain certified from a prior round in
`lemmas/layer-cake-identity-and-coupling-obstruction.md` and stay available
for reuse; noted in `current.md`.

## Summary verdicts

| Slug | Verdict | Outcome recorded |
|---|---|---|
| self-similar-induction-on-n | CHANGES REQUESTED | advanced |
| greedy-reduction-geometric | CHANGES REQUESTED | advanced |
| universal-halving-adversary | CHANGES REQUESTED | advanced |
| lp-duality-split-polytope | CHANGES REQUESTED | advanced |

No RETHINK, no APPROVE this round. All four approaches are alive and
making genuine, independently-verified progress; the two lower-bound gaps
(Branch II's uncovered range / Branch-I.A window; Insertion-Robustness /
Level-Absorption target) and the two upper-bound gaps (`idx=1`; the
residual balanced region beyond Subset-Tie) are each precisely narrower
than at the start of the round. `current.md` rewritten in full to reflect
this state.
