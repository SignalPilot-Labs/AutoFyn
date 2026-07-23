# Proof review — imo-2026-03, round 2

Reviewed independently: (1) `results/imo-2026-03/approaches/dyadic-cascade-induction.md`,
(2) `results/imo-2026-03/approaches/elementary-exchange-smoothing.md`, plus the two newly
certified lemma files and `current.md`. Verification method: re-derived the load-bearing
steps by hand and cross-checked with independent brute-force / numpy computation (not
reusing any of the builders' code), on top of reading every proof step for logical gaps.

---

## 1. Lemma G (`lemmas/greedy-reduction.md`) — CERTIFY

**Statement checked:** under optimal alternating claiming on a fixed sorted multiset
(mover 1 first), mover 1's total = sum of odd-ranked entries, mover 2's = sum of
even-ranked entries, and "claim the current max" is optimal throughout.

**Verification:** Implemented an independent exact backward-induction game-tree solver
(memoized recursion over subsets, `v(S) = sum(S) - min_{x in S} v(S\{x})`) and compared its
output against the claimed closed form (`sum of odd-ranked entries`) on 200 random
instances, sizes 1–7: max absolute error `5.3e-15` (float roundoff only). Separately verified
that removing the *current maximum* is always a minimizer of `v(S\{x_j})` (the greedy-move
optimality claim) on 200 more random instances: 100% pass.

**Proof read:** the induction is standard and correctly executed — the key inequality
`x_1+x_3+…+x_{2t-1} ≥ x_2+x_4+…+x_{2t}` (termwise from sortedness) is exactly what's needed
and is proved, not asserted. No gap found. This is a correct, standard, and now
rigorously-proved fact (Zermelo/backward-induction cited correctly for well-definedness).

**Verdict: certify as-is.**

## 2. Lemma P (`lemmas/duplicate-pair-invariance.md`) — CERTIFY

**Statement checked:** deleting any two entries of equal value from a sorted multiset
leaves `e := L−X` (odd-rank sum minus even-rank sum) exactly unchanged.

**Verification:** Independent brute-force check on 500 random instances (sizes 2–8, forcing
one duplicated value): max absolute error `1.8e-15`. The head/block/tail decomposition in
the proof is correct: the block's alternating-sign contribution depends only on the parity
of the run length (invariant under removing 2 elements), and the tail shifts by exactly 2
positions (parity-preserving), so no cross term survives. No gap found; the claimed
generalization beyond "even-multiplicity run" (any two equal entries suffice) is correctly
argued via the "everything between two equal values is forced equal by sortedness" remark.

**Verdict: certify as-is.**

Both lemmas are self-contained, problem-independent, general-purpose facts — correctly
scoped for the shared lemma cache.

---

## 3. `dyadic-cascade-induction` — n=2 upper-bound closure

**Case (i) (`a_1≥2a_2`).** Form (B) (`e≤a_1/2^m`, all `m`) is a clean induction via Lemma P
on the bisection-created duplicate pair — correct. The "gap 5" top-level closure at `n=2`
(exact 2-element residual formula reducing the top-level optimization to maximizing
`min(a_3,a_2-a_3)` subject to `a_1≥2a_2`, `a_1+a_2+a_3=1`) — I independently re-derived this
via a direct constrained numerical sweep (parametrize by `R=a_2+a_3`, scan `a_2` over its
admissible range): **found max exactly `0.142857… ≈ 1/7`, attained at
`(a_1,a_2,a_3)=(0.5714,0.2857,0.1429) = (4/7,2/7,1/7)`**, matching the hand derivation
exactly, including the unique attainment point. The proof's own honest mid-course
correction (flagging that form (B) does *not* generically imply form (A), with a genuine
counterexample `(0.99,0.005,0.005)`) is itself correct — I verified `a_1/2^2=0.2475 > 1/7`
there while the true `e` is `0` (duplicate `a_2=a_3` collapses via Lemma P to the empty
residual) — so the caveat is real and the fix (using the exact residual formula specific to
`n=2`, not the lossy generic IH bound) is the right one and is fully worked out.

**Case (ii) (`a_1<2a_2`).** The vertex lemma (piecewise-linearity of a single cut, reducing
XY's search to finitely many "match/bisect" candidates) is proved correctly — the argument
(rank changes only when a moving value crosses a fixed value or its paired value) is sound
and is essentially the same fact independently derived in `elementary-exchange-smoothing`'s
Step A, which cross-validates it. The 4 sign sub-regimes of
`F=min(level1(a_2,a_3), level1(a_1-a_2,a_3))` were re-derived and checked independently:
after correcting my own first sweep (which initially omitted the sortedness constraint
`a_2≥a_3` and produced a false violation), a properly-constrained random sweep of hundreds
of thousands of points in each of the four regimes gives max values `0.0909`, sup
`0.1429` (not attained), `0.1111`, sup `0.1429` (not attained) — matching the claimed
`1/11`, `1/7` (boundary-only), `1/9`, `1/7` (boundary-only) exactly. I also independently
verified the two named attained points `(5/11,4/11,2/11)` (`F=1/11`) and `(4/9,3/9,2/9)`
(`F=1/9`) by direct substitution.

**Global cross-check.** Independently of the above (not using any of the builder's
formulas), I wrote a from-scratch numpy brute-force search over the *entire* upper-bound
game at `n=2`: for every candidate LB opening `(a_1,a_2,a_3)` on a fine simplex grid, computed
the true minimum achievable `e` over **all** of XY's possible 0/1/2-cut configurations
(single cut on one piece, two cuts on two different pieces, two cuts on one piece into
three parts), via dense grids refined to `n_grid≈150–300`. Result: the maximum over the
whole simplex of this true minimum is `1/7`, attained (uniquely, up to grid resolution)
exactly at `(4/7,2/7,1/7)`; no simplex point exceeds `1/7`. This independently corroborates
the builder's claimed closure of both Case (i) and Case (ii) for `n=2` — a genuinely
different verification path (whole-game brute force, not the same case-split).

**Conclusion:** I found no error in the n=2 upper-bound proof. The casework is complete
(both cases, all sub-regimes), the "sufficient strategy, not necessarily optimal" framing
is logically sound (only achievability of `e≤1/7` is needed for the upper-bound direction,
not exact optimality — correctly noted by the builder), and every exact numeric claim I
spot-checked or bulk-verified matches. The proof is honest about what is *not* closed:
the lower-bound direction (even at `n=2`) and generalization to `n≥3` — both explicitly
and correctly left open, not glossed over. Status `partial` (not `solved`) is the correct
self-assessment; the builder does not overclaim.

**Minor items, not proof-breaking:** (a) item 4 in the open-gaps list ("using fewer than
full cut budget never helps" handled ad hoc, not as a general lemma) is a legitimate,
correctly-flagged loose end but does not affect the n=2 closure since it's exhibited
explicitly everywhere it's used. (b) The recursion check `e_n=e_{n-1}/(2+e_{n-1})` is
presented as a motivating consistency check, not a proof step — correctly not overclaimed
as doing real work.

**Verdict: CHANGES REQUESTED.** Status `partial` is correct (matches the builder's own
claim — no overclaiming found). Real, substantial, independently-verified progress: the
entire n=2 upper-bound direction is now closed, on top of two certified general lemmas.
Gap to close next: (1) the n=2 lower-bound direction (prove `(4/7,2/7,1/7)` actually
resists every XY response, not just spot-checked), (2) generalize both directions to
`n≥3` — flagged by the builder as needing a genuinely different (recursive/self-similar)
argument since the `n=2` techniques rely on the small fixed piece count.

---

## 4. `elementary-exchange-smoothing` — local uniqueness near the dyadic point

**Tie-or-degenerate lemma (Step A).** Same content and same correct proof idea as
`dyadic-cascade-induction`'s vertex lemma (independently derived); no gap.

**Candidate formulas (Step B).** Re-derived `f1=a_1+2a_2-1` (`=a_2-a_3`), `f2=2a_1-1`,
`f3=a_3` from scratch by re-sorting the claimed final multisets under the stated branch
conditions (`a_1≥1/2`, `a_1/2≥a_3`, Case (ii) `a_1<2a_2`): all three match. Verified all
three equal exactly `1/7` at the dyadic point (`f1=f2=f3=2/7`, `1/7`, `1/7` respectively —
checked by substitution).

**Convex-hull certificate (Step C).** Independently re-solved
`λ_1(1,2)+λ_2(2,0)+λ_3(-1,-1)=0`, `Σλ_i=1`: get `λ=(2/7,1/7,4/7)`, all strictly positive,
matching the claimed certificate exactly (cross-checked by back-substitution:
`(2/7)(1,2)+(1/7)(2,0)+(4/7)(-1,-1)=(0,0)` ✓).

**General theory check.** The claim "`0` in the strict interior of the convex hull of the
active gradients at `x_0` ⟹ `x_0` is the unique global maximizer of the concave
min-of-affine-functions `h` over the whole domain" is a standard and correct fact from
polyhedral concave-function theory; I re-derived it from scratch (via the standard
polar-cone/separating-hyperplane characterization of interior points, plus the one-variable
concave-restriction argument for upgrading "strict local max" to "unique global max"). The
"finite min of affine functions is concave" fact used is also elementary and I verified it
directly (`min_i(A_i+B_i) ≥ min_i A_i + min_i B_i` pointwise, hence exact equality for
affine `f_i` under `f_i(λx+(1-λ)y)=λf_i(x)+(1-λ)f_i(y)` gives the concavity inequality for
`h`). The citation to KB's "Piecewise-concavity smoothing" entry is a loose/approximate
citation (that KB entry is about a related but not identical construction) — a minor
citation-precision issue, not a substantive gap, since the fact itself is elementary and is
effectively re-derived (not merely asserted) in the file.

**Numerical cross-check.** Independently scanned a `101×101` grid of `(a_1,a_2)` in a
`±0.05` box around `(4/7,2/7)`, restricted to the same branch region used in the proof:
`h < 1/7` strictly at every point except the dyadic point itself (max found `0.1419 < 1/7`),
consistent with the claimed strict local uniqueness.

**Domain/scope subtlety, checked carefully.** The dyadic point sits exactly on the Case
(i)/(ii) boundary (`a_1=2a_2`), not in the interior of the open Case (ii) region. I checked
whether this invalidates the "unique global max" argument: it does not, because the
interior-of-gradient-hull condition gives a strictly negative directional derivative in
*every* direction in the ambient plane (not just directions feasible for a sub-case), so
restricting further to strict Case (ii) only strengthens (weakens the claim needed, i.e., it's
still valid) — the conclusion correctly reduces to "no point strictly inside Case (ii) near
the dyadic point beats or ties it," which is what's claimed. No gap here — this was worth
checking but the builder's framing survives scrutiny.

**Open/conditional items, correctly disclosed by the builder (not hidden):**
1. The whole argument is conditional on the (separately unproven) fact
   `g(dyadic)=1/7` exactly — i.e., that no XY response beats `1/7` at the dyadic point
   itself. Without this, `h(dyadic)=1/7` (established directly) only gives `g(dyadic)≤1/7`,
   not the equality needed to conclude `g` is *strictly smaller* everywhere else nearby.
   This is exactly the same open "lower bound at n=2" gap that `dyadic-cascade-induction`
   also flags as unproved — a shared, honestly-named dependency, not new hand-waving.
2. Coverage is only a neighborhood of the dyadic point within one branch region of Case
   (ii) — global coverage of all of Case (ii), the a_2/a_3 ratio, and general `n` are all
   explicitly left open.

**Conclusion:** the mathematical content of Steps A–C is correct as far as I can verify —
I found no logical or computational error, and the scope claimed (local, conditional
uniqueness) matches exactly what is proved; no overclaiming.

**Verdict: CHANGES REQUESTED.** Status `partial` is correct. This is real progress: a
different, complementary derivation (concave-analysis framing, genuinely distinct from
`dyadic-cascade-induction`'s casework) that independently corroborates the same extremal
point and sub-region behavior. Gaps to close next: (1) prove `g(dyadic)=1/7` (the shared
lower-bound gap — likely the highest-value next step, since closing it here also closes
part of `dyadic-cascade-induction`'s open gap), (2) extend the branch region to cover all
of Case (ii) (not just a neighborhood of the dyadic point), (3) the analogous `a_2/a_3`
ratio argument, (4) general `n`.

---

## 5. Overall `current.md` status

Confirmed: neither approach claims the general-`n` theorem, and neither claims the
lower-bound direction even at `n=2`. Both explicitly self-report Status `partial`, which
matches my independent assessment. **Overall problem status correctly remains `partial`,
not `solved`.** `current.md` has been updated to record: both certified lemmas, the fully
closed `n=2` upper-bound direction (`dyadic-cascade-induction`), the conditional local
uniqueness result (`elementary-exchange-smoothing`), and the three concrete open gaps
(lower bound at `n=2`; general `n≥3` for both directions; Case (i)'s general-`m` form-(A)
promotion).

## Ranking

`record_outcome` called for both slugs with outcome `advanced` (real, verified progress —
neither dead-ended, neither trivially "solved"; both closed real gaps this round: full n=2
upper bound + 2 certified lemmas for `dyadic-cascade-induction`; a correct conditional local
uniqueness result for `elementary-exchange-smoothing`).

## Verdicts

- **`dyadic-cascade-induction`: CHANGES REQUESTED.** True Status: `partial` (matches
  builder's claim). Gap: n=2 lower bound + general n.
- **`elementary-exchange-smoothing`: CHANGES REQUESTED.** True Status: `partial` (matches
  builder's claim). Gap: unproven `g(dyadic)=1/7` import, restricted domain, general n.

Lemma certification: **Lemma G — certified. Lemma P — certified.** Both written correctly
in `results/imo-2026-03/lemmas/`, no changes needed.
