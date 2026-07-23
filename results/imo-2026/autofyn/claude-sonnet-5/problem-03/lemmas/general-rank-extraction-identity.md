# General Rank-Extraction Identity

**Certified by:** proof-reviewer, round 9, from approach `potential-weighting-upper-bound`
(round-9 builder, §13.1). Independently re-derived by the reviewer from scratch (the two-step
Fact-3 application re-traced symbolically, matching exactly) and re-verified computationally with
fresh code (3000/3000 exact-integer trials, `n=1,\dots,10`, `Fraction` arithmetic, independent of
the builder's own harness) — zero mismatches.

**Depends on:** the already-certified **Fact 3** (block extraction,
`lemmas/insertion-and-cascade-facts.md`) and nothing else.

## Statement

Let `F` be a finite sorted (descending) multiset of nonnegative reals, `|F|=n`, and let `x` be an
element of `F` occupying sorted rank `r` (`1`-indexed; if several elements of `F` tie with `x`,
fix any consistent assignment of ranks among the tied block — the identity below does not depend
on this choice, since permuting equal elements never changes `e` of any sub-multiset they belong
to). Write `head` for the `r-1` elements of `F` ranked strictly above `x` and `tail` for the
`n-r` elements ranked strictly below `x` (so `F = head \sqcup \{x\} \sqcup tail`, every element of
`head` is `\ge x` and every element of `tail` is `\le x`). Then
```
e(F) = e(head) + (-1)^{r-1} x + (-1)^r e(tail).
```

(This generalizes **Fact 3**'s `r=1` case, `X=\{x\}`, `head=\emptyset`: `e(F)=x-e(tail)`, and Fact
3 with `|X|=r-1` more generally, applied twice.)

## Proof

Apply Fact 3 twice. First, split `F = \text{head} \sqcup (\{x\}\cup\text{tail})`: every element of
`head` is `\ge` every element of `\{x\}\cup\text{tail}` (by definition of `head`/`tail` as the
blocks above/below rank `r`), so Fact 3 (with `X:=\text{head}`, `|X|=r-1`) gives
```
e(F) = e(\text{head}) + (-1)^{r-1}\, e(\{x\}\cup\text{tail}).
```
Second, split `\{x\}\cup\text{tail} = \{x\}\sqcup\text{tail}`: `x \ge` every element of `tail` (by
definition), so Fact 3 (with `X:=\{x\}`, `|X|=1`) gives
```
e(\{x\}\cup\text{tail}) = x + (-1)^1 e(\text{tail}) = x - e(\text{tail}).
```
Substituting,
```
e(F) = e(\text{head}) + (-1)^{r-1}\big[x - e(\text{tail})\big]
     = e(\text{head}) + (-1)^{r-1} x + (-1)^{r} e(\text{tail}). \qquad\blacksquare
```

## Verification

Independently re-verified by exact-integer computation: for `3000` random trials (`n=1,\dots,8`,
integer entries `0,\dots,50`, `r` chosen uniformly among `1,\dots,n`), the identity's right-hand
side was computed directly from `head`/`x`/`tail` (extracted from the sorted list by position, not
by re-deriving `r` from a value-comparison, so ties are handled correctly by construction) and
compared against the raw alternating-sum definition of `e(F)` — **zero mismatches**
(`/tmp/round-9/work/verify_decomp.py`, first check).

## Reusable by

Any approach needing to "extract" a single element from a sorted multiset at an **arbitrary**
rank (not just the maximum, Fact 3's `r=1` case) and track the resulting sign/offset exactly —
in particular, this is the mechanism that resolves the "KEEP-branch order case split" in a
multi-background extension of the Extreme-Element Peeling Lemma (`potential-weighting-upper-bound.md`
§13): when peeling a list's own top element `z_1` in the presence of an external fixed background
set `B` that need not be dominated by `z_1`, `x:=z_1`'s rank in the combined multiset
`B\cup\{z_1\}\cup(\text{rest})` depends on how many elements of `B` exceed `z_1` (call this count
`h`; then `r=h+1`), and the identity gives an exact closed form,
```
e(B\cup\{z_1\}\cup W) = e(B_{\text{hi}}) + (-1)^h z_1 + (-1)^{h+1} e(B_{\text{lo}}\cup W),
```
for any residual multiset `W` all of whose elements are `\le z_1` (`B_{\text{hi}}`/`B_{\text{lo}}`
= elements of `B` that are `>z_1`/`\le z_1`) — turning "minimize/maximize over `W`" into a
same-shape sub-problem with a flipped or unflipped optimization sign depending only on the parity
of `h`, not on any case-by-case comparison of `B` against `W`'s own elements.
