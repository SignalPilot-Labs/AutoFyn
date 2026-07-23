# Lemma D/M (operation-sequence reformulation of Xiang Yu's cutting phase)

**Certified by:** proof-reviewer, round 3, from approach `potential-weighting-upper-bound`
(originally proved by that approach's round-3 builder).

**Depends on:** Lemma P (`lemmas/duplicate-pair-invariance.md`).

## Statement

Let `A = (a_1≥…≥a_k)` be Liu Bang's opening multiset (`k≤n+1` pieces, `n` cuts available to
Xiang Yu). For a finite multiset of nonnegative reals `B`, define two operations:

- `D(x)` for `x∈B`: replace `B` by `B\{x}` (remove one copy of the value `x`).
- `M(x,y)` for `x,y∈B` with `x≥y` (as two elements of the multiset `B`, possibly equal in
  value but distinct as elements): replace `B` by `(B\{x,y})∪\{x-y\}` (remove one copy each
  of `x,y`, insert one copy of `x-y`).

Then:
1. **Each operation is realizable by exactly one of Xiang Yu's cut points** — `D(x)` by
   bisecting the physical piece of length `x` into two length-`x/2` pieces; `M(x,y)` by
   cutting the physical piece of length `x` at distance `y` from one end, producing pieces
   of length `y` and `x-y`.
2. **After the operation, `e` computed on the new active multiset `B'` equals `e` computed
   on the true full physical multiset** (all real pieces, including the "cancelled"
   duplicate copies) — because in both cases the operation creates a pair of equal-valued
   physical pieces (the two halves in `D`, or the new length-`y` piece and the pre-existing
   length-`y` piece in `M`), and by Lemma P, deleting any two equal-valued entries from a
   sorted multiset leaves `e` exactly unchanged.
3. Consequently, for **any** legal sequence of `≤n` such operations starting from `A`, the
   resulting `e` (computed on the final active multiset by the ordinary alternating-rank-sum
   formula) equals the true `e = L-X` of the real final dissection under the corresponding
   Xiang Yu response.

## Proof

(1) is immediate from the definitions (each operation specifies exactly one cut point).

For (2): in the `D(x)` case, before the cut the active multiset (as physical pieces)
contained one copy of `x`; after, it contains two copies of `x/2` in its place. These two
copies are equal-valued, so Lemma P applies with the "before" multiset (physical pieces
before the cut, with the two copies of `x/2` in place of `x`'s slot after cutting) — more
precisely: let `M := ` physical multiset after the cut (contains two copies of `x/2` where
`x` used to be), `M' := ` `M` with those two `x/2` entries deleted. `M'` is identical to "all
physical pieces except the one that was split" — the same set obtained by deleting `x` itself
from the multiset *before* the cut. By Lemma P, `e(M) = e(M')`, i.e. `e(\text{after}) =
e(\text{before multiset with }x\text{ deleted})` — exactly the effect of the `D(x)` operation
on the active multiset.

In the `M(x,y)` case: before the cut, the physical multiset contains one copy of `x` and
(separately) one copy of `y`; after, the copy of `x` is replaced by two new pieces of length
`y` and `x-y`, so the physical multiset now contains **two** copies of `y` (the original
untouched one, plus the new one) together with the new `x-y` piece and everything else
unchanged. The two copies of `y` are equal-valued, so Lemma P gives `e(\text{after}) =
e(\text{after multiset with the two }y\text{-copies deleted})`, and that reduced multiset is
exactly "everything except the original `x` and `y`, plus the new `x-y`" — exactly the effect
of `M(x,y)` on the active multiset.

This proves the single-operation case of (2). For sequences, apply this equality inductively:
after each operation, the *current* active multiset's `e`-value equals the *true* physical
multiset's `e`-value at that point in the cut sequence (by the single-operation argument,
applied to the actual physical multiset present at that step, which by the inductive
hypothesis has the correct `e`); since this holds after every operation, it holds after the
final one, proving (3). ∎

## Consequence

Xiang Yu's achievable values under `≤n` cuts include (as a **subset**, not necessarily all)
every value `e(B_{\text{final}})` obtainable by applying `≤n` legal D/M operations starting
from `A`; in particular `g(A,n) := \min` over such sequences of `e(B_{\text{final}})` is
always an **upper bound** for the true value Xiang Yu can force Liu Bang's `e` down to. This
is not claimed to capture Xiang Yu's *entire* strategy space in general (whether every
jointly-optimal multi-cut response reduces to a D/M sequence is a separate, open structural
question — see `dyadic-cascade-induction`'s vertex-lemma discussion), only that D/M sequences
are always *achievable*, which is all that is needed for upper-bound arguments.

## Verification

Independently re-derived and re-checked by the proof-reviewer, round 3: the single-operation
argument was re-verified symbolically (matches Lemma P's certified statement exactly, applied
twice with the correct multiset identifications), and the reformulation was exercised via an
independent exhaustive Python implementation (exact `fractions.Fraction` arithmetic) reproducing
the approach file's own worked examples (the `m=3` Rule-1 counterexample trace, `37/500` exactly,
and the improved D/M sequence achieving `1/500`), with no discrepancy found.

## Reusable by

Any approach in this population needing to reason about Xiang Yu's achievable cutting
strategies as a combinatorial operation sequence rather than raw geometric cut positions — in
particular, `dyadic-cascade-induction`'s Case (i)/(ii) strategies and its lower-bound §5
Branch B analysis are literally special cases of D/M sequences and could be reframed through
this lemma to shorten future write-ups.
