# Lemma: Two-Variable Reflection Bound

**Status:** CERTIFIED (round 19, proof-reviewer). Independently re-derived by hand (all 3 cases)
and re-verified computationally (30,000 fresh integer trials + 20,000 fresh fractional trials,
`0` failures; plus the builder's own 462-tuple exhaustive grid and 19,894-trial random sweep) before
certification.

## Statement

For real `b_0, w, w_1` with `0 <= b_0 <= w_1` and `0 <= w <= w_1`:
```
w_1 - |b_0 - w|  >=  |b_0 - (w_1 - w)|.
```

## Proof

Write `L := w_1 - |b_0-w|` and `R := |b_0-(w_1-w)|`. Split exhaustively on the sign of `b_0-w`, and
(when `b_0>w`) further on the sign of `b_0-(w_1-w)`:

- **`b_0<=w`:** `L = (w_1-w) + b_0`, a sum of two nonnegatives (`w_1-w>=0` since `w<=w_1`;
  `b_0>=0`). For any `p,q>=0`, `p+q>=|p-q|`. With `p:=w_1-w`, `q:=b_0`: `L>=|(w_1-w)-b_0|=R`.
- **`b_0>w` and `b_0<=w_1-w`:** `L=w_1-b_0+w`, `R=(w_1-w)-b_0`. `L-R=2w>=0`.
- **`b_0>w` and `b_0>w_1-w`:** `L=w_1-b_0+w`, `R=b_0-w_1+w`. `L-R=2(w_1-b_0)>=0` (using `b_0<=w_1`).

The three cases are exhaustive and boundary-consistent (using `<=`/`>` throughout, no double
counting). In every case `L>=R`. $\blacksquare$

## Scope

Fully general and standalone — no reference to any particular 3-element list or to Two-Touch/
Three-Touch specifically. Both hypotheses (`b_0<=w_1`, `0<=w<=w_1`) are load-bearing: dropping
`w<=w_1` gives 100% failure (3000/3000, tested), and the KEEP hypothesis `b_0<=w_1` is used
elsewhere (in the application, not in this lemma's own proof) — this lemma's own proof only uses
`0<=b_0<=w_1` and `0<=w<=w_1` as stated.

## Origin / application

Proved in `potential-weighting-upper-bound.md` §33.1 (round 19 build), used to close 2 of the 5
per-term bounds (`i=2,3`) in §33.3's proof of Two-Touch's KEEP `b_0<=w_1` sub-case at `|W|=3`
(§33.2's target `(*)`, `w_1-ThreeTouch(b_0,rest) >= TwoTouch(b_0,W)`). Reusable by any future
approach comparing a "keep-`b_0`-and-`w`" candidate against a "match-`b_0`-against-`w_1-w`"
candidate for a peeled maximum `w_1`.

## Verification

`/tmp/round-19-build/verify_32.py` (builder, exact `Fraction`, 462-tuple exhaustive grid +
19,894-trial random sweep, plus 2 negative controls both at 100% failure). Independently
re-verified by this review: `/tmp/round-19-review/verify_potential.py` (30,000 fresh integer
trials + 20,000 fresh fractional trials, `0` failures, both hand-derivation and fresh code agree).
