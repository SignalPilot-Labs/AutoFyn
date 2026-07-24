# Lemma: measure-form-bf-invisibility (Lemma UBI-1)

**Certified round 8** (unified-residual-budget-induction). Reviewer-verified.

## Statement
For any finite multiset `P` of positive reals let `f(P)=Σ_i(-1)^i a_i` (values sorted descending,
`i=0,1,…`) be the alternating sum, and `M(P)=measure{t>0 : #{x∈P : x>t} is odd}` the layer-cake
measure. Then `f(P)=M(P)` (certified `layer-cake-alt-sum`), and for every value `v>0` and every
even integer `2m≥2`,
```
    f(P ∪ {v}^{2m}) = f(P).
```
That is, adjoining (or deleting) an even-multiplicity block of any single value leaves `f` exactly
unchanged — with NO adjacency, rank-ordering, or distinct-powers hypothesis.

## Proof
Write `g_P(t)=#{x∈P : x>t}`. Adding `2m` copies of `v` gives `g_{P'}(t)=g_P(t)+2m·𝟙[t<v]`, which
differs from `g_P(t)` by an even number for every `t`. Hence `g_{P'}(t)≡g_P(t) (mod 2)` for all `t`,
so `{t:g_{P'}(t) odd}={t:g_P(t) odd}` and `M(P')=M(P)`. With `f=M` this gives `f(P')=f(P)`. ∎

## Relation to prior lemmas
Strictly generalises and simplifies the certified `odd-block-formula` and `symmetric-odd-block-move`:
it is the definitive "even blocks are `f`-invisible" statement, needing none of their block-adjacency
/ rank / distinct-power side-conditions. Complements `matched-pair-invisibility` (the `2m=2` case).

## Verification
- `f=M` on 3000 random rational multisets: 0 mismatches.
- `f(P∪{v}^{2m})=f(P)` on 3000 random cases (random `v`, `m∈{1,2,3}`): 0 mismatches.
- `f({8/3,8/3,8/3,8/3,2,4/3,1}) = f({2,4/3,1}) = 5/3` (exact).
(`/tmp/verify8.py`.)

## Caveat on use (recorded dead-end, NOT part of the lemma)
The peel `f(P)=f(P∖{v}^{2m})` is an `f`-preserving *isomorphism of difficulty*, not a reduction: the
even-reduced class `C={P_odd}` satisfies `min_C f = min_{refinements} f` (identity map + preservation),
so "prove `f≥1` on `C`" is logically equivalent to the original residual, not weaker; and for a shared
non-power-of-two block (`v=2^k/3`) the peeled complement has a non-dyadic total, so it is not a `W_m`
refinement and no induction hypothesis type-checks. Do not use UBI-1 as a complement-induction
finisher (proven insufficient, round 8).
