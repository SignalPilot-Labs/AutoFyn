# Layer-cake identity for e, and Non-crossing inside/outside independence

**Certified by:** proof-reviewer, round 7, from approach `potential-weighting-upper-bound`
(round-7 builder, §9.1, §9.2/"Promotable lemmas"). Independently re-derived (both proofs
re-checked step-by-step from scratch) and independently re-verified computationally (2000
random exact-`Fraction` trials for the layer-cake identity) by the reviewer.

**Depends on:** nothing beyond the elementary definition of `e` (alternating sum of a sorted
descending list) and, for the second lemma, the definition of a "selection" (partition into
kept/deleted/matched-pair indices) and "non-crossing" from `potential-weighting-upper-bound.md`
§9.2.

## Statement

**Lemma (Layer-cake identity).** For a sorted descending list `x_1\ge x_2\ge\dots\ge x_n\ge0`
(`x_{n+1}:=0`), define `N(t):=\#\{i:x_i>t\}`. Then
```
e(x_1,\dots,x_n):=\sum_{i=1}^n(-1)^{i+1}x_i = \int_0^\infty \mathbb{1}[N(t)\text{ is odd}]\,dt.
```

**Lemma (Non-crossing inside/outside independence).** Fix a sorted list `Y=(y_1\ge\dots\ge
y_p)` and a globally non-crossing selection containing the matched pair `(1,j)`. Then no other
matched pair of the selection has one endpoint in `I=\{2,\dots,j-1\}` and the other in
`O=\{j+1,\dots,p\}`; consequently the selection's restriction to `I` and to `O` are each
themselves valid non-crossing selections, independently, and conversely any pair of non-crossing
selections on `I` and `O` glues (with the pair `(1,j)`) to a globally non-crossing selection on
all of `Y`.

## Proof

**Layer-cake.** On the interval `t\in[x_{i+1},x_i)`, exactly `x_1,\dots,x_i` exceed `t`, so
`N(t)=i` throughout, an interval of length `x_i-x_{i+1}\ge0`. Hence
`\int\mathbb1[N(t)\text{ odd}]dt=\sum_{i\text{ odd}}(x_i-x_{i+1})`. This equals
`\sum_i(-1)^{i+1}x_i` for every `n`, proved by induction on `n`: base `n=1` both sides `=x_1`;
inductive step splits on the parity of `n`, in each case matching the new term
`\pm x_{n+1}` added to both sides identically (full case-by-case algebra in the source file,
re-derived and confirmed by the reviewer).

**Non-crossing inside/outside independence.** If a pair `(i',o')` has `i'\in I,o'\in O`, then
`1<i'<j<o'` is exactly the definition of crossing with `(1,j)`, contradicting global
non-crossingness — so no such pair exists, giving the forward direction. Conversely, pairs both
drawn from `I` (or both from `O`) don't cross by hypothesis on the sub-selections; a pair from
`I` and a pair from `O` have disjoint, non-interleaved index ranges (impossible to cross); and no
pair entirely within `I` or entirely within `O` crosses `(1,j)` (an inside pair is nested inside
`(1,j)`, an outside pair is disjoint from it) — so the glued selection is globally non-crossing.

## Verification

- Layer-cake identity: independently re-verified by 2000 random trials (`n=1..8`, exact
  `fractions.Fraction`, integer values `0..50`) comparing the direct alternating-sum formula
  against the interval-integral formula computed via the same case split — zero mismatches.
- Non-crossing inside/outside independence: elementary combinatorial fact, re-derived directly;
  no computation needed beyond confirming the crossing-condition algebra, which is immediate.

## Reusable by

Any approach needing (a) a threshold/coverage reformulation of `e` (layer-cake), useful for
arguments about `N(t)` directly rather than the raw alternating sum; or (b) a rigorous
non-crossing-partition DP recursion for a matching+deletion optimization on a sorted list
(inside/outside independence) — this is what makes such a DP an *exact* computation of the
non-crossing-restricted value `NC(Y,b)`, not merely a plausible heuristic decomposition.

**Scope note:** these two lemmas are general-purpose and fully proved; they do **not** by
themselves establish `OPT(Y,b)=NC(Y,b)` (the "non-crossing suffices" conjecture) — that
conjecture is FALSE in general (see `potential-weighting-upper-bound.md` §9.3's exact
counterexample `Y=(39,36,30,28,22,18,14),b=3`: `OPT=1<NC=2`, independently re-verified by the
reviewer via full enumeration, `925` selections). The correctly-scoped, still-open replacement
target is `OPT(Y,p-1)=NC(Y,p-1)` (budget exactly one less than list size) — see that file's §9.4
for the justification that this is the only budget the parent chain-prefix+tail construction
actually needs.
