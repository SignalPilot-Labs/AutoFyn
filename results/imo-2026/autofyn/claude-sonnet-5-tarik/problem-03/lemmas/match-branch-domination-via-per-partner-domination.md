# Lemma: Match-Branch-Domination-via-Per-Partner-Domination

**Status:** CERTIFIED (round 18, proof-reviewer), **narrower than the builder's submitted statement** —
see "Scope note" below for the clause that was rejected.

Proposed in `potential-weighting-upper-bound.md` §29.1/§30.1 (round 18). Independently re-verified by the
proof-reviewer via fresh code (`/tmp/check_gap.py` and direct re-derivation of every cited ingredient)
before certification.

## Statement

Fix a Two-Touch peeling instance: singleton background `b0>=0`, sorted list `W=(w1>=...>=wq)`,
`w1=max(W)`, `rest:=W\{w1}`. For a partner `w_j \in rest`, write `d_j:=w1-w_j`,
`MATCH_j := OPT_{+1}(\{b0,d_j\}, rest\{w_j\})`, `A1 := OPT_{+1}(\{b0\}, rest)` (Two-Touch's DELETE
branch), `D_j := |b0-d_j| = e(\{b0,d_j\})`, and `TT := TwoTouch(\{b0\},W)` (Two-Touch's closed-form
candidate value, the min over its finite candidate list, §26.1 of the approach file).

**Conditional only on Gap 1a's Per-Partner Domination Lemma** (`A_{3,l} >= min(A1,D_l)`, certified
unconditionally for `q<=3`, open/corroborated for `q>=4`, no trigger or argmin hypothesis needed) **at
the specific size `q=|W|` and index `l=j`**:
```
MATCH_j >= TT
```

## Proof

Under the identification `B0={b0}`, `Z0=W`, `l=j` (a literal renaming, not an analogy — `A_{3,l}` and
`MATCH_j` denote the same object), Per-Partner Domination reads `MATCH_j = A_{3,j} >= min(A1,D_j)`. Two
already-certified facts bound both terms below by `TT`:
1. `A1 >= TT`: this is the **inductive step** of the Two-Touch strong induction on `|W|` (candidate-set
   inclusion: `TwoTouch({b0},rest)`'s candidate list is a strict subset of `TwoTouch({b0},W)`'s, so a
   `min` over the subset is `>=` a `min` over the full set; combined with the induction hypothesis that
   Two-Touch's full equality already holds at the strictly smaller size `|rest|=|W|-1`). **It is
   available only once Two-Touch is already fully closed at size `|W|-1`** — at `|W|=3` this is the
   already-certified base case `|W|<=2`, so no open dependency there, but at general `q` this requires
   the rest of the joint Two-Touch/Three-Touch induction to already be closed at every smaller level
   (see Scope note).
2. `D_j >= TT`: trivial — `D_j=e(\{b0,d_j\})` is by definition one member of `TwoTouch`'s own candidate
   list, so the list's own minimum cannot exceed it.

Hence `min(A1,D_j) >= TT`, and Per-Partner Domination gives `MATCH_j = A_{3,j} >= min(A1,D_j) >= TT`. ∎

## Scope note — what this Lemma does NOT establish (do not overclaim)

The builder's submitted statement additionally claimed: "Consequently, at `|W|<=3`, Two-Touch
(`OPT_{+1}({b0},W)=TT`) is unconditionally, fully proved." **This additional clause is REJECTED — it is
not established by this Lemma or by anything else on file.** To conclude `OPT_{+1}({b0},W)=TT` at
`|W|=3` via the DELETE/KEEP/MATCH trichotomy, one needs **all three** branches `>=TT`: this Lemma (plus
F1/F2) gives DELETE and MATCH; the KEEP branch's `b0>w1` sub-case is separately unconditional (§26.5(c));
but the KEEP branch's `b0<=w1` sub-case at `|W|=3` requires the inequality
```
w1 - ThreeTouch(b0, rest) >= TwoTouch({b0}, W)          (|rest|=2)
```
which is **not** supplied by the certified Three-Touch base-case Lemma B
(`lemmas/max-element-triple-identity-and-threetouch-basecase.md` — that lemma only gives the *value*
`OPT_{-1}({b0},rest)=ThreeTouch(b0,rest)`, not this comparison against `TT`). This specific inequality is,
as of round 18, only numerically corroborated (reviewer: `0` failures across `>14,000` fresh trials
including a genuinely exhaustive small grid and a true-brute-force-`OPT` check, widened up to `vmax=500`;
builder/round-17 file: `0/1,239`) — **not proved**. "Two-Touch fully proved for `|W|<=3`" is therefore
**not** a valid consequence of this Lemma; only "Two-Touch's MATCH branch is closed at `|W|=3` (and, at
whatever `q` Per-Partner Domination is proved, at that `q` too)" is certified.

At general `q>=4`: this Lemma's conclusion `MATCH_j>=TT` requires Per-Partner Domination at that `q`
(open) AND, via ingredient 1, that Two-Touch is already fully closed at `|W|-1` — which itself needs the
same joint machinery (Three-Touch's own MATCH branch, Per-Partner Domination) closed at every level below
`|W|-1`. Any future use of this Lemma at general `q` must verify this level-ordering explicitly.

**UPDATE (round 19, proof-builder + proof-reviewer):** the missing inequality flagged above
(`w1-ThreeTouch(b0,rest) >= TwoTouch({b0},W)` at `|rest|=2`) is now **fully proved** —
`potential-weighting-upper-bound.md` §33 (Two-Variable Reflection Bound + 5-term case analysis),
independently re-derived and certified by the round-19 proof-reviewer (see
`lemmas/two-variable-reflection-bound.md` and `current.md`'s round-19 entry). Combined with this
Lemma (MATCH), the pre-existing unconditional `b0>w1` KEEP formula, and the DELETE-branch induction
using the already-certified `|W|<=2` base case, **"Two-Touch fully, unconditionally proved for
`|W|<=3`" is now a genuinely established consequence** — the missing ingredient identified above is
discharged. This does NOT extend to `q>=4` (Per-Partner Domination and the KEEP `b0<=w1` case split
both remain open there).

## Computational corroboration

Re-derived independently (proof-reviewer, fresh code) and cross-checked against the builder's own
`/tmp/round-18-build/t_verify_301.py`, `t_verify_F3.py`: trichotomy identity `0/400` random + `0/625`
exhaustive; Per-Partner Domination restated in these variables `0/1,837` random + `0/9,375` exhaustive
(`q=4` grid). All reproduce exactly.
