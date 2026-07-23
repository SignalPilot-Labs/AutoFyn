# Non-concavity of the true value function g at n=2 (negative result)

**Certified by:** proof-reviewer, round 3, from approach `concavity-minimax-duality`
(round-3 builder).

**Depends on:** Lemma G (`lemmas/greedy-reduction.md`), the elementary fact `e≥0` (Fact 1,
`lemmas/dominant-extraction.md`).

This is a **negative result**: recorded here (rather than only inside one approach's file)
so that no future approach in this population wastes effort trying to prove global concavity
of the true n=2 value function `g` — it is false, with an explicit, exact counterexample.

## Statement

Let `g(a_1,a_2,a_3) := \min_{\text{XY's ≤2 cuts}} e(\text{final multiset})` be Xiang Yu's true
best-response value (not a sufficient-strategy proxy), for Liu Bang openings `a_1\ge a_2\ge
a_3\ge0`, `a_1+a_2+a_3=1`, at `n=2` (`e := L-X` per Lemma G). Then **`g` is not concave** on
this domain: `g(1/2,t,1/2-t) = 0` exactly for every `t\in(1/4,1/2)`, while at
`t=3/10`, the points
```
p_1 = (12/25, 3/10, 11/50), p_2 = (13/25, 3/10, 9/50)
```
(whose midpoint is exactly `(1/2,3/10,1/5)`) satisfy `g(p_1) = g(p_2) = 1/25`, so
```
g(\text{midpoint}) = 0 < 1/25 = (g(p_1)+g(p_2))/2,
```
a direct, exact violation of the concavity inequality `g(\text{midpoint}) \ge
(g(p_1)+g(p_2))/2`.

## Proof

**The dip (`g=0` on the segment).** At `a_1=1/2=t+(1/2-t)=a_2+a_3`, Xiang Yu splits `a_1`
with a *single* cut into `(a_2,a_3)` exactly, using 1 of its 2 available cuts. This yields
final multiset `\{a_2,a_3,a_2,a_3\}$; sorted (`a_2>a_3$ since `t>1/4`): `a_2,a_2,a_3,a_3`, so
`e = (a_2+a_3)-(a_2+a_3) = 0`. Since `e\ge0` always (Fact 1) and this strategy attains `0`,
`g(1/2,t,1/2-t)=0$ exactly, for every `t\in(1/4,1/2)`.

**Strict positivity at `p_1,p_2`.** Exhaustive case analysis over the number `k\in\{0,1,2\}`
of Xiang Yu's genuinely-used cuts (a cut producing a zero-length piece is equivalent to an
unused cut):
- `k=0`: final `=\{a_1,a_2,a_3\}$, all distinct, 3 (odd) pieces; direct computation gives
  `e=2/5>0$ at both `p_1,p_2`.
- `k=2$ (both cuts genuine): final multiset always has exactly 5 (odd) pieces, all strictly
  positive; for any sorted `x_1\ge\dots\ge x_5>0`, `e=(x_1-x_2)+(x_3-x_4)+x_5\ge x_5>0`
  (Fact 1's pairing argument, with the final unpaired term now strictly positive). So
  `e>0` for **every** `k=2` configuration — `e=0` is never attained by any 2-genuine-cut
  strategy, and in fact no `k=2` configuration was found (by direct search) beating `1/25`.
- `k=1$ (the only case that can give `e=0`, since 4 is even): a 4-element final multiset
  ties into two equal pairs in one of two ways — bisection (the two untouched originals are
  equal, impossible here since `a_1,a_2,a_3$ are pairwise distinct at `p_1,p_2$) or the cut
  piece equals the sum of the two untouched pieces. Checking all 3 choices of which piece is
  cut, in both cases (`p_1,p_2$), none of the three "sum" equalities holds, so `e=0` is never
  attained. The exhaustive breakpoint (vertex-lemma) enumeration over all 3 cut choices gives
  minimum exactly `1/25` (attained, cutting `a_1` and matching to `a_3`).

Combining, and using continuity/compactness of the (bounded, closed) cut-position space to
rule out any `k=2` limiting configuration doing better than the attained `k=1` minimum:
`g(p_1)=g(p_2)=1/25` exactly.

**The violation.** `(p_1+p_2)/2 = (1/2,3/10,1/5)`, and `g` there is `0 < 1/25 =
(g(p_1)+g(p_2))/2`, violating concavity. ∎ A second, independent instance (region
`a_2\ge2a_3`, at `a_2=2/5`) confirms this is not a one-off: `g(1/2,2/5,1/10)=0` while nearby
points along `a_1` give `g\in\{1/25,2/25\}>0`.

## Verification

Independently re-derived and re-checked by the proof-reviewer, round 3: the dip computation
(`e=0` at `M_t`), the `k=0,1,2` exhaustive case analysis at `p_1,p_2` (all arithmetic redone
in exact `fractions.Fraction`), and a 200,000-trial random search over `k=2` configurations at
`p_1` (found no value below `1/25`, corroborating the attained minimum) all matched the
approach file's claims exactly.

## Consequence / scope

This kills, definitively, any proof strategy for the n=2 upper bound that relies on **global**
concavity of the true value function `g` over the whole n=2 domain. It does **not** affect
`elementary-exchange-smoothing`'s local certificate (that argument uses a different,
genuinely-concave function `h := \min(f_1,f_2,f_3)` — a min of exactly 3 globally-fixed affine
formulas, honestly concave by the standard "min of affine is concave" fact — as an upper bound
on `g`, not `g` itself; `h`'s concavity does not depend on `g`'s, and was independently
re-checked numerically here on 200,000 random points in its claimed domain, max found `≈0.1418
<1/7`, consistent with no violation). It also does not affect `dyadic-cascade-induction`'s
direct n=2 casework proof, which never invokes concavity. A **narrower** claim — concavity of
`g` restricted to `a_1\ge1/2` only — is *not* refuted by this specific counterexample (whose
`p_1=(12/25,\dots)` has `a_1=12/25<1/2`, outside that restricted domain) and remains an open,
unexplored possibility for a future approach, distinct from (and not a simple continuation of)
this negative result.
