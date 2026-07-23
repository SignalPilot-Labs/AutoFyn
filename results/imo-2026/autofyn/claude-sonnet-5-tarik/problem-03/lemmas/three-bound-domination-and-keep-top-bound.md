# Lemmas: Three-Bound Domination, and Keep-Top Bound

**Status:** CERTIFIED (round 15, proposed by `potential-weighting-upper-bound` §24.2/§24.3;
independently re-verified from scratch by the round-15 proof-reviewer — own fresh `Fraction`-exact
harness, `200,000/200,000` (Three-Bound Domination, fully arbitrary triples) and `0` failures across
`308` genuine `h=0`-triggered `q=3` base-generator instances (Keep-Top Bound, in its actual use
context), plus independent symbolic re-derivation of both proofs). Both are fully proved, elementary,
general-purpose facts about the `e_{\mathrm{sorted}}` function used throughout
`potential-weighting-upper-bound.md`.

Throughout, `e_{\mathrm{sorted}}(S)` denotes the sorted-descending alternating sum of a finite
multiset `S` of nonnegative reals (`e(S)=s_1-s_2+s_3-\dots`, the standard function from the certified
`lemmas/duplicate-pair-invariance.md` / Lemma P), and for a 3-element multiset
`e_{\mathrm{sorted}}(\{x,y,z\})=\max-\mathrm{mid}+\min$.

## Lemma (Three-Bound Domination)

**Statement.** For any nonnegative reals `x,y,z`:
```
min(x, |x-y|, |x-z|)  <=  e_sorted({x,y,z}).
```

**Proof.** Let `M\ge\mathrm{md}\ge m` be `\{x,y,z\}` sorted descending, so
`e_{\mathrm{sorted}}(\{x,y,z\})=M-\mathrm{md}+m`. Case-split on which of `x,y,z` equals `x` in rank:

- If `x=M` (the largest): `\{y,z\}=\{\mathrm{md},m\}$ in some order, so
  `\{|x-y|,|x-z|\}=\{M-\mathrm{md},M-m\}`. Hence `\min(x,|x-y|,|x-z|)\le M-\mathrm{md}\le
  M-\mathrm{md}+m` (since `m\ge0`), matching the target exactly.
- If `x=m` (the smallest): `\min(x,|x-y|,|x-z|)\le x=m\le M-\mathrm{md}+m` (since `M\ge\mathrm{md}`
  gives `M-\mathrm{md}\ge0`).
- If `x=\mathrm{md}` (the middle): `\{y,z\}=\{M,m\}` in some order, so
  `\{|x-y|,|x-z|\}=\{M-\mathrm{md},\mathrm{md}-m\}`. Hence `\min(x,|x-y|,|x-z|)\le M-\mathrm{md}\le
  M-\mathrm{md}+m`.

These three cases are exhaustive (by rank of `x` among the three values) and mutually exclusive, so
the bound holds unconditionally. `\blacksquare`

**Remark (application).** This rules out "keep both remaining elements of a 2-element residual list"
(`A_1\le e_{\mathrm{sorted}}(\{b_0,u_1,u_2\})`) as an independently useful candidate bound in
`potential-weighting-upper-bound.md`'s generalized `A_1`-bound family (§24.2): it is always dominated
by the simpler "delete-all-but-one" family `\{x,|x-y|,|x-z|\}` (here `x=b_0`, `y=u_1`, `z=u_2`), so it
never adds information beyond bounds already available. It does **not**, by itself, resolve the `q=4`
MATCH-branch gap — it only eliminates one candidate direction for closing it.

## Lemma (Keep-Top Bound)

**Statement.** At any `(C,W,+1)` (in the sense of `potential-weighting-upper-bound.md` §13.2/§17.2)
with `C=\{c_1,c_2\}` and `h=0` (i.e. `c_1,c_2<w_1:=\max(W)`, so neither background element exceeds
`W`'s own maximum):
```
OPT_{+1}(C,W)  <=  w_1 - |c_1-c_2|.
```

**Proof.** The selection "keep `w_1`, delete every other element of `W`" is a valid candidate for
`OPT_{+1}(C,W)$'s minimization, with value `e_{\mathrm{sorted}}(\{c_1,c_2,w_1\})`. Since `h=0` means
`w_1` is strictly the largest of `\{c_1,c_2,w_1\}`,
`e_{\mathrm{sorted}}(\{c_1,c_2,w_1\})=w_1-\max(c_1,c_2)+\min(c_1,c_2)=w_1-|c_1-c_2|`. Since
`OPT_{+1}(C,W)` is a minimum over all selections and this is one particular selection,
`OPT_{+1}(C,W)\le w_1-|c_1-c_2|`. `\blacksquare`

**Remark (application).** Applied at a genuine `\mathcal F` base generator's `A_{3,k^*}$
(`C=\{b_0,d_{k^*}\}`, `W=Z_1`, `w_1=\max(Z_1)`) this gives `M\le w_1-D_{k^*}`, i.e.
`w_1\ge M+D_{k^*}`, one ingredient (not the full proof) of `potential-weighting-upper-bound.md`'s
still-open Gap 1b base case (`w_1\ge2D_{k^*}`). The lemma itself holds for any `q` (any size of `W`),
not only the `\mathrm{rest}=\emptyset` singleton case it was originally found to sharpen.

## Verification

Independently re-derived and re-verified by the round-15 proof-reviewer with fresh, independently
written code:
- **Three-Bound Domination:** `200,000/200,000` fully arbitrary `(x,y,z)` random trials (integers
  `0`–`1000`), `0` violations; symbolic proof independently re-derived by hand before running any
  code, matches the file's own case split exactly.
- **Keep-Top Bound:** tested in its actual use context — built genuine `q=3` `\mathcal F` base
  generators (real trigger `M<A_1`, real global argmin `k^*`), restricted to the `h=0` sub-case,
  `308/308` (out of `1728` triggered instances total, `v_{\max}\in\{1,\dots,50\}`) satisfy the bound
  with `0` violations; in the same sweep, independently confirmed the **exact `q=3` dichotomy**
  identity `M=\min(D_{k^*},w_1-D_{k^*})` (not itself promoted to a standalone lemma — narrow scope,
  a one-line consequence of "a singleton list has exactly two candidate selections," declined for
  certification per the same reasoning the round-13 reviewer applied to the Coincidence Identity) and
  the base-case fact `M=D_{k^*}` (DELETE beats KEEP) holds in all `308/308` genuine `h=0` instances —
  strong corroboration of, but not a proof of, `potential-weighting-upper-bound.md`'s still-open Gap
  1b base case.

## Used by

- `potential-weighting-upper-bound.md` §24.2 (Three-Bound Domination — rules out one candidate
  direction for the `q=4`/`q\ge5` generalized `A_1`-bound family, Gap 1a); §24.3 (Keep-Top Bound —
  one ingredient of the still-open Gap 1b base case reduction).
