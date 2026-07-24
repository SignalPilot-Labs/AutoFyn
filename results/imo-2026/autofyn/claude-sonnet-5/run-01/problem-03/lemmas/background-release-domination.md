# Lemma: Background-Release Domination (strengthened)

**Status:** CERTIFIED (round 15, proposed by `potential-weighting-upper-bound` §24.4, strengthening
a weaker capped form proposed by the round-15 proof-outliner in §23.2; independently re-verified from
scratch by the round-15 proof-reviewer — own fresh `Fraction`-exact harness, `0/3000` (`csize`≤4,
`wsize`≤4) plus a wider `0/1500` sweep (`csize`≤5, `wsize`≤5), both signs `\sigma=\pm1`, plus
independent reproduction of the file's own four worked examples exactly before trusting the harness
for anything new). Fully proved, no `\mathcal F`-provenance restriction needed.

## Statement

Let `OPT_\sigma(C,W)` denote (per `potential-weighting-upper-bound.md` §13.2, the Generalized
Multi-Background Peeling Lemma's own setup) the `\sigma`-optimal (minimum if `\sigma=+1`, maximum if
`\sigma=-1`) value of `e(C\cup K\text{-values}\cup M\text{-differences})` over **all** selections
`(K,D,M)` of a list `W` (Keep/Delete/Match, no crossing restriction), for a fixed external background
multiset `C` (deleted elements of `W` contribute nothing).

For **any** background `C` with `|C|\ge1`, **any** list `W`, and **any** `y\in C` (writing
`C':=C\setminus\{y\}`):
```
OPT_{+1}(C,W)  >=  OPT_{+1}(C', W u {y})          (releasing y from the background into the free list)
OPT_{-1}(C,W)  <=  OPT_{-1}(C', W u {y})           (the sigma=-1 dual)
```
No `\min`/`\max` with `e(C)` is needed — this is a strictly stronger, fully unconditional form (the
originally-proposed capped form `OPT_{+1}(C,W)\ge\min(OPT_{+1}(C',W\cup\{y\}),e(C))` follows trivially
from it, since `\min(X,e(C))\le X` whenever `X` is the true lower bound established here).

## Proof

Fix `C`, `W`, `y\in C`, `C'=C\setminus\{y\}`. Every selection `(K,D,M)` of `W` (with background `C`
fixed) corresponds to exactly one selection of the bigger list `W\cup\{y\}` (background `C'`) obtained
by keeping the same Keep/Delete/Match structure on `W`'s own elements and additionally placing `y`
into the Keep set: `(K\cup\{y\}, D, M)`. This is a valid selection of `W\cup\{y\}$ (it is one of the
choices `OPT_{+1}(C',W\cup\{y\})` optimizes over), and its value is
```
e(C' \cup (K\cup\{y\})\text{-values} \cup M\text{-differences}) = e(C'\cup\{y\}\cup K\text{-values}\cup M\text{-differences}) = e(C\cup K\text{-values}\cup M\text{-differences})
```
(using `C'\cup\{y\}=C`) — **identical** to the value the same `(K,D,M)` gives as a selection of `W`
with background `C`. So the map `(K,D,M)\mapsto(K\cup\{y\},D,M)$ is a value-preserving bijection from
`W`'s full selection space onto the sub-space of `W\cup\{y\}`'s selection space in which `y` is forced
to lie in `K`. Consequently
```
OPT_{+1}(C,W) = \sigma\text{-opt over }W\text{'s full space} = \sigma\text{-opt over the "}y\in K\text{"-restricted sub-space of }OPT_{+1}(C',W\cup\{y\})\text{'s own search space}.
```
`OPT_{+1}(C',W\cup\{y\})` itself minimizes over the *full* (strictly larger, since `y` may now also be
placed in `D` or matched to some element of `W`) search space. Minimizing over a superset can only give
a value `\le` minimizing over any particular subset of it, so
```
OPT_{+1}(C',W\cup\{y\}) <= OPT_{+1}(C,W),
```
which is exactly the claimed inequality. For `\sigma=-1`, the identical bijection applies, but now
`OPT_{-1}(C',W\cup\{y\})` **maximizes** over the larger space, so maximizing over a superset gives a
value `\ge` maximizing over any subset: `OPT_{-1}(C',W\cup\{y\})\ge OPT_{-1}(C,W)`. `\blacksquare`

## Remarks

- Same proof shape as the certified Shrink-List Monotonicity Lemma (`shrink-list-monotonicity.md`):
  both are one-line search-space-inclusion arguments. Shrink-List shrinks the free list `W` (deleting
  an element costs nothing); this lemma grows the free list by releasing a background element into it
  (the released element can now also be deleted or matched, options it never had while pinned in the
  background) — a structurally different move, not a restatement.
- **Two natural ways to chain this lemma into a closing argument for Gap 1a (`potential-weighting-
  upper-bound.md`'s central open item) were tested and REFUTED this round — do not re-attempt either:**
  (a) full telescoping to a background-free bound degenerates to the trivial Empty-Background value and
  is too lossy (`\approx38\%$ violations of the actually-needed target); (b) a single-release direct
  chain comparing the released quantity against `A_1` is false in general (swapping a list element for
  its derived difference is not monotone, `\approx16\%` violations, concrete witness
  `z=[6,4,1],b_0=7,l=1`). See `potential-weighting-upper-bound.md` §23.2/§24.4 for the exact
  counterexamples. The lemma itself is correct and general-purpose; only these two specific uses of it
  are dead ends.

## Verification

Independently re-derived and re-verified by the round-15 proof-reviewer with fresh, independently
written code (not reusing the builder's or outliner's harness): `0/3000` violations (`\sigma=+1` and
`\sigma=-1` both checked, `|C|\in\{1,\dots,4\}`, `|W|\in\{0,\dots,4\}`, half-integer alphabet up to 6),
extended to `0/1500` at `|C|\le5,|W|\le5$, alphabet up to 10 — no violation found at any scale tested.
Corroborates, but is not needed to trust, the direct one-line proof above. Independently reproduces the
builder's own `0/18{,}000` (`\sigma=+1`) and `0/18{,}000` (`\sigma=-1`) figures in substance (different
sampling, same conclusion).

## Used by

- Not yet load-bearing for any open gap in `potential-weighting-upper-bound.md` (both natural chaining
  routes into Gap 1a are dead, see Remarks) — recorded as a general-purpose, reusable fact about moving
  a background element into/out of a free list, for any future approach or gap that needs it.
