# Math-explorer report: lower-bound residual gaps (imo-2026-03, round 7)

Lens: the two residual lower-bound gaps — `self-similar-induction-on-n`'s
Theorem 2' (the narrowed self-similar window + Branch I.B) and
`greedy-reduction-geometric`'s Theorem 7' sub-problems (Insertion-Robustness,
Level-Absorption). All claims below are backed by exact `Fraction` (rational)
arithmetic scripts, not floats-only — code kept in `/tmp/scout*.py`,
`/tmp/verify*.py` on this box if anyone wants to rerun them.

## 1. IMPORTANT: a real formalization gap found in `L0(ℓ,ε)` as literally stated

The round-6 write-up (`self-similar-induction-on-n.md`, "Round 6: toward
Theorem 2'", also mirrored in the certified lemma
`lemmas/theorem2gen-bounds-and-l0-reduction.md`) states:

> **`L0(ℓ,ε)`:** for every finite multiset `C` with `sum(C)=2^ℓ+ε` and
> `max(C)≤2^ℓ-ε`, `OddSum(C∪Γ_{ℓ-1}) ≥ 2^ℓ`.

**This statement, taken literally with no bound on the number of parts of
`C`, is FALSE.** Exact rational counterexample found (verified by direct
`Fraction` computation, not approximate):

- `ℓ=2`, `ε=1/10`. `C = {2, 5649/10000, 1407/2500, 9723/10000}` (4 parts,
  `sum(C)=41/10=2^2+1/10` ✓, `max(C)=2 ≤ 2^2-1/10=39/10` ✓).
  `Γ_{ℓ-1}=Γ_1={2,1}`.
  Full sorted multiset: `(2, 2, 1, 9723/10000, 5649/10000, 1407/2500)`.
  `OddSum = 2+1+5649/10000+... ` — exact value `35649/10000 = 3.5649 < 4 = 2^ℓ`.
  **Target violated.**

The reason: `C` has 4 parts here, but tracing back through the
peel-of-`b1` reduction, `B={b1}∪C` then has **5** parts, exceeding the
original problem's cut budget (`B` must partition `2^m` into `≤m+1` parts,
i.e. `C` must have `≤m=ℓ+1` parts). `L0(ℓ,ε)`'s displayed statement omits
this cut-budget/piece-count constraint entirely — it is implicit in the
surrounding prose ("actual refinement... using `≤k` cuts") but not written
into the boxed statement, so a reader (or a future prover) attempting to
close `L0(ℓ,ε)` exactly as stated would be attempting to prove something
**false**.

**With the correct constraint restored** (`C` has `≤ℓ+1` parts, matching the
inherited cut budget), I reran the identical search (piece count capped at
`ℓ+1`) across `ℓ=2,3,4`, `ε∈{0.1,...,0.9}`, sampling `c1` across the residual
window `(2^{ℓ-1}-1+ε, 2^{ℓ-1}+1-ε)`, with thousands of random-shape trials
per point (exact `Fraction` arithmetic): **zero violations**, margins
positive throughout (smallest found ≈0.05 at `ℓ=2,ε=0.1,c1≈2`), consistent
with the file's own belief that the residual window is true but tight.

**Recommendation for next round's builder/outliner:** before attempting to
close `L0(ℓ,ε)` (or the residual window within it), the statement must be
amended to explicitly say "`C` has at most `ℓ+1` parts" (or equivalently
carry the cut-budget parameter through explicitly, as `G(m,k;V)` does in
`self-similar-induction-on-n`'s own earlier trichotomy section). This is
the same class of bug as the round-6 `(★★)` typo the reviewer already
caught — an abstractly-stated tool missing a hypothesis that the concrete
branch applications happened to respect. It should be fixed in the lemma
file alongside the `(★★)` correction already there.

## 2. The residual window `c1∈(2^{ℓ-1}-1+ε, 2^{ℓ-1}+1-ε)`, with the correct piece cap

With the piece-count bug fixed, I searched for the tightest instances across
`ℓ=2,3,4` and `ε=0.1,...,0.9`, at multiple points in the window. Findings:

- No violations at any tested point (margins strictly positive, smallest
  ≈0.05, at the window's interior near `c1≈2^{ℓ-1}` and small `ε`).
- Margins shrink toward the window's own boundary values `c1→2^{ℓ-1}-1+ε`
  and `c1→2^{ℓ-1}+1-ε` are actually *not* where slack is tightest in my
  search — the tightest point found is near `c1=2^{ℓ-1}` itself (the window's
  center, exactly where Branch I/II split), consistent with the window being
  precisely the boundary between the two peeling directions.
- The margin does **not** vanish as fast as `ε→1` alone would suggest by a
  naive `(1-ε)`-width argument; it stays comfortably `>0` even at `ε=0.9`
  (window nearly empty) in every instance found. This is consistent with
  the claim being true with real (if small) slack, not sitting exactly on
  a second boundary — i.e. this does **not** look like another exactly-tight
  extremal sliver requiring yet one more level of the identical dichotomy.

**What this suggests for closing it.** Since the true minimizer sits at
`c1≈2^{ℓ-1}` — exactly the point where the peeling method must choose
between "peel `c1`" (Branch I) and "peel `2^{ℓ-1}`" (Branch II) — a plain
one-more-level application of the same two-way dichotomy will again fall
short right at this boundary, for the same structural reason Lemma B alone
falls short at the original sliver: **near the split point, neither
candidate max value dominates by enough margin for a single Lemma-B-style
bound to close it.** The mechanism that *did* work at the analogous
boundary in the base case was **not** another application of the
dichotomy — it was Theorem 1's `m=2,j=2` hand computation, which used the
**full order-statistics profile** (median of the residual three elements),
not just a peel-and-Lemma-B bound. This suggests the right next move for
the residual window is the same kind of finite order-statistics
computation (tracking the second-largest element of `C`, not just `c1`),
rather than a third level of the "peel-then-Lemma-B" recursion — recursing
the identical mechanism a third time is likely to hit the identical
boundary problem at a new sub-window, an infinite regress the round-6
write-up itself already flags as a risk ("the residual window has the
same self-similar shape... needs a genuine multi-level induction").

## 3. Branch I.B (`C` has ≥2 elements `≥2^{ℓ-1}`) — looks like the easy case, not the hard one

Numerically tested (exact rational, correct piece cap) across `ℓ=2..5`,
`ε=0.1,0.5,0.9`: **found comfortably positive margins, growing with `ℓ`**
(e.g. `ℓ=3`: margin ≈1.03 regardless of `ε`; `ℓ=5`: margin ≈5.0-5.25). This
is a *much* larger margin than the residual-window case (≈0.05-0.1), and it
grows with `ℓ` rather than staying tight. This is a strong hint that
**Branch I.B is not actually a hard case** — it was left unaddressed purely
for lack of round-6 time, not because it is numerically delicate.

Structural reason this is plausible: if `C` has two elements `c1,c1'≥2^{ℓ-1}`,
then `sum(C)≥2·2^{ℓ-1}=2^ℓ`, but `sum(C)=2^ℓ+ε<2^ℓ+1`, so the *rest* of `C`
(beyond these two elements) has total mass `<1-（c1+c1'-2^ℓ)≤1`, i.e. very
constrained. A direct two-peel argument (peel `c1`, then peel `c1'` against
the tail, à la the Two-Level Half-Bound Lemma but applied to `C`'s own top
two elements rather than the merged multiset's) looks like it should close
this case outright, matching the large observed margins. **Recommend a
proof-builder attempt Branch I.B directly next round** — it looks tractable
and separate from the genuinely-hard boundary window in §2.

## 4. Insertion-Robustness (Open Sub-Problem A, `greedy-reduction-geometric`)

Tested by building near-equality Theorem-7-style instances and inserting an
extra multiset `R1` (various shapes, `1..7` pieces, random compositions,
exact rational sums) with `max(R1)≤μ1` on top. With `k'=1` (single dominant
element `b2` vs. full untouched tail `Γ_{mm1-1}`), the Theorem-7 slack is
**always exactly `EvenSum(T)`** (a constant, independent of `b2` — since the
peel-of-`b2` identity makes `OddSum({b2}∪T)=b2+EvenSum(T)` exactly), so this
particular family never gets numerically tight and insertion never came
close to violating the bound in my tests (worst margin found stayed at the
baseline `EvenSum(T)` or above, growing with `L`). This matches, but does not
extend beyond, the round-6 preamble's own numeric reconnaissance (which
already tested the harder `k=2`, `b1=b2=2^{m-1}` zero-slack boundary
directly and found margin `≤0` — i.e. no violation — at every `m` tested).
**I did not find a counterexample to Insertion-Robustness in the time
available**, and the round-6 preamble's search (a strictly harder,
zero-slack instance) is stronger evidence than what I added here. My
contribution is mainly negative-but-consistent: no new attack surface
found; the `k=1` family is not where a counterexample would show up (it has
a constant, non-tight margin by construction), so any future numeric attack
on Insertion-Robustness should target `k'≥2` near-equality instances
directly (as round 6 already started), not the `k'=1` case.

## 5. Level-Absorption (Open Sub-Problem B) — not separately stress-tested

I did not get to an independent numeric test of Sub-Problem B this round
(time budget). It is worth flagging that Sub-Problem B's target
`OddSum(B''∪{μ1}∪R1∪S'')≥b2+sum(B'')` has a different flavor from Sub-Problem
A: the inserted mass `{μ1}∪R1` (summing to a full `2^{m-1}`) must *supply*
the deficit `b2` rather than merely "not hurt." Given Sub-Problem A already
looks well-supported and Sub-Problem B is comparatively unexplored, I'd
recommend a dedicated numeric pass on Sub-Problem B specifically before a
proof-builder commits time to it.

## Summary / recommendations for next round

1. **Fix the `L0(ℓ,ε)` piece-count omission first** (§1) — this is a
   genuine bug (not just a style issue) in the current write-up/certified
   lemma; a builder trying to close the literal statement will be trying to
   prove a false theorem. Cheap fix: add "`C` has `≤ℓ+1` parts" to the
   boxed statement in both the approach file and the lemma file.
2. **Branch I.B looks tractable and separate** (§3) — comfortable numeric
   margins, growing with `ℓ`, suggest a direct two-peel argument closes it;
   good target for a proof-builder next round, likely cheaper than the
   residual window.
3. **The residual window (§2) is the genuinely hard part** — tightest right
   at `c1=2^{ℓ-1}`, the Branch I/II split point, with small but nonzero
   margin (not shrinking to an exact second boundary). Recommend attacking
   it with an order-statistics argument (second-largest element of `C`,
   analogous to Theorem 1's `m=2,j=2` median computation) rather than a
   third level of the same peel-then-Lemma-B dichotomy, which is likely to
   hit the identical boundary problem one level down.
4. **Insertion-Robustness**: no counterexample found, but my test family was
   too weak (constant-margin `k'=1` case); round 6's own `k'=2` zero-slack
   test remains the strongest evidence and should be extended/repeated
   rather than treated as settled.
5. **Level-Absorption**: unexplored this round — recommend a numeric pass
   before committing builder time.
