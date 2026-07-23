# Facts 3, 4, 5 — block extraction, single-insertion bound, chain-cancellation

**Certified by:** proof-reviewer, round 4, from approach `dyadic-cascade-induction`
(round-4 builder, §5.2'' Part B). Independently re-derived and verified by the reviewer
(exact-`Fraction` random trials for Facts 3/4, an independent from-scratch recursive
construction for Fact 5 — all passed with no violations, see Verification below).

**Depends on:** the definition `e(M) := Σ_i (-1)^{i+1} m_i` for a sorted descending multiset
`M`, and the already-certified `lemmas/dominant-extraction.md` (Facts 1, 2) and
`lemmas/duplicate-pair-invariance.md` (Lemma P).

## Statement

**Fact 3 (block extraction).** Let `F` be a sorted (descending) multiset that splits as
`F = X ⊔ Y` (disjoint multiset union) where every element of `X` is `≥` every element of `Y`
(so, in `F`'s sorted order, `X`'s elements occupy the top `|X|` ranks, followed by `Y`'s).
Then
```
e(F) = e(X) + (-1)^|X| · e(Y).
```
(Generalizes Fact 2, the special case `|X|=1`.)

**Fact 4 (single-insertion bound).** Let `Y` be a sorted multiset of nonnegative reals and
`x ≥ 0`. Let `Z := Y ∪ {x}` (insert one copy of `x`, re-sort). Then
```
|e(Z) - e(Y)| ≤ x.
```

**Fact 5 (chain-cancellation / ceiling achievability).** For any finite multiset of
nonnegative reals `{y_1,…,y_L}` (`L≥0`), there is an explicit sequence of exactly `L`
physical cuts (applied only to fragments of these `L` pieces) producing a final multiset with
`e(final) = 0` exactly.

**Corollary (ceiling achievability).** For any sorted `M=(x_1≥…≥x_K≥0)`, `K≥1`, using exactly
`K-1` cuts (applied only to `x_2,…,x_K`, `x_1` untouched), `e(final) = x_1 = max(M)` exactly
— i.e. Fact 2's ceiling is always exactly attainable within the natural cut budget, never
merely approached.

## Proof

**Fact 3.** Write `X=(x_1≥…≥x_p)`, `Y=(y_1≥…≥y_q)`; by hypothesis `F`'s sorted order is
exactly `x_1,…,x_p,y_1,…,y_q`. Then
`e(F) = Σ_{i=1}^p(-1)^{i+1}x_i + Σ_{j=1}^q(-1)^{p+j+1}y_j = e(X) + (-1)^p e(Y)`. ∎

**Fact 4.** Let `x` land at sorted rank `r` in `Z`. Split `Y = head ⊔ tailseq`, `head` = `Y`'s
top `r-1` elements (all `>x`, unaffected by the insertion), `tailseq` = `Y`'s remaining
`K-r+1` elements (all `≤x`). In `Z`, `head` is unchanged, `x` sits at rank `r`
(sign `(-1)^{r+1}`), and every element of `tailseq` shifts down one rank, flipping its sign.
Writing `tail := Σ_{i≥r}(-1)^{i+1}y_i` (`Y`'s own indexing), `e(Z) = e(Y) - 2·tail +
(-1)^{r+1}x`. Since `tail = (-1)^{r+1} e_0(tailseq)` (fresh indexing on the suffix),
`e(Z)-e(Y) = (-1)^{r+1}[x - 2e_0(tailseq)]`. By Fact 1, `e_0(tailseq)≥0`; by Fact 2,
`e_0(tailseq) ≤ max(tailseq) ≤ x`. So `x - 2e_0(tailseq) ∈ [-x,x]`, giving
`|e(Z)-e(Y)| ≤ x`. ∎

**Fact 5**, by induction on `L`. `L=0`: `e(∅)=0` vacuously. `L=1`: bisect `y_1` into
`(y_1/2,y_1/2)`, a direct 2-term computation gives `e=0`, using 1 cut. `L≥2` (IH: claim holds
for `L-1`): relabel `a:=y_1≥b:=y_2`. Cut `a` into `(b,a-b)` (1 cut, valid since
`0≤a-b<a`, `b≤a`). This creates a duplicate pair `{b,b}` with the original `y_2=b`; by Lemma
P, `e({a-b,b,b,y_3,…,y_L}) = e({a-b,y_3,…,y_L})`, an `(L-1)`-element list of real pieces. By
the IH, `L-1` further cuts (on fragments of `a-b,y_3,…,y_L` only) achieve `e=0` on this list.
Composing (the first pair's cancellation and the IH's cancellations act on disjoint physical
pieces, so they compose without interaction, as noted in Lemma P's "Use" section), the true
final `e` of the whole `L`-cut construction is `0`. Total cuts: `1+(L-1)=L`. ∎

**Corollary.** Apply Fact 5 to `{x_2,…,x_K}` (`L=K-1` elements, `K-1` cuts), driving its own
`e`-contribution to exactly `0`. Every fragment produced is `≤ max(x_2,…,x_K)=x_2≤x_1`, so
`x_1` (untouched) remains the maximum of the true final sorted multiset throughout. By Fact 2
(exact identity), `e(final) = x_1 - e(rest-final) = x_1 - 0 = x_1`. ∎

## Verification

Independently re-verified by the proof-reviewer, round 4:
- Fact 3: 2000 random `(X,Y)` trials (exact `Fraction`, dominance constraint enforced), no
  violation.
- Fact 4: 5000 random `(Y,x)` trials (exact `Fraction`), `|e(Z)-e(Y)| ≤ x` held in every trial.
- Fact 5: an independent from-scratch recursive construction (implementing the induction
  literally) tested on 2000 random multisets of size 0–7, `e(final)=0` exactly in every trial,
  mass conserved.

## Reusable by

Any approach reasoning about how `e` changes under insertion, block-extraction, or
cut-budget-limited modification of a sorted multiset — e.g. `potential-weighting-upper-bound`'s
D/M policy search, or any future attempt at `dyadic-cascade-induction`'s open Step 4
(multi-cut-inside-a-dominant-piece gap). **Caveat, honestly recorded:** Fact 4's insertion
bound is proved but was shown (by `dyadic-cascade-induction`, concrete instance `m=4,i=3`) to
be *too lossy* on its own to close that open gap (it gives a useless negative bound
`-5/31` against a true minimum of `+3/31`) — it remains a correct, general, reusable fact for
other purposes. Fact 5 is a **negative/diagnostic** result for that same gap: it proves the
"residual stays safely below its ceiling" proof strategy cannot work in general, since the
ceiling is always exactly reachable within budget — this rules out a whole class of future
naive arguments and should not be re-attempted in that form.
