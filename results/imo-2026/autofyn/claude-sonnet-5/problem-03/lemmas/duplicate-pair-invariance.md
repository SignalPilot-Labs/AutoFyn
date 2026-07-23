# Lemma P (duplicate-pair invariance) and Lemma P-zero

**Certified by:** proof-builder, approach `dyadic-cascade-induction`, round 2.

This version is **more general** than the "even multiplicity" form originally conjectured
in the outline: it holds for the removal of *any* two equal-valued elements from a sorted
multiset, regardless of how many total copies of that value are present.

## Setup

For a finite sorted (non-increasing) sequence `M = (m_1 ≥ m_2 ≥ … ≥ m_K)` of nonnegative
reals, define
```
e(M) := Σ_{i=1}^K (−1)^{i+1} m_i     (odd ranks positive, even ranks negative).
```
By Lemma G (`lemmas/greedy-reduction.md`), if `M` is the final multiset of piece lengths
after all cuts, then `e(M) = L − X` where `L, X` are Liu Bang's and Xiang Yu's totals under
optimal alternating claiming. So bounding `e` is equivalent to bounding `L−X`.

## Lemma P

**Statement.** Suppose `m_p = m_q = x` for some `1 ≤ p < q ≤ K` (two elements of `M` with
equal value `x`; note that since `M` is sorted, every entry with index between `p` and `q`
must also equal `x` — see proof). Let `M'` be the sequence obtained from `M` by deleting the
two entries at positions `p` and `q` (any two equal-valued entries, not necessarily
adjacent). Then
```
e(M') = e(M).
```

**Proof.** Since `M` is non-increasing and `m_p = m_q = x` with `p<q`, for every `i` with
`p ≤ i ≤ q` we have `m_p ≥ m_i ≥ m_q`, i.e. `x ≥ m_i ≥ x`, so `m_i = x`. Thus all `L_0 := q−p+1`
entries at positions `p,…,q` equal `x` (a contiguous "run" of the value `x`).

Split the sum defining `e(M)` into three parts: the **head** `A := Σ_{i<p} (−1)^{i+1} m_i`
(positions before the run, untouched by the deletion), the **block**
`B := Σ_{i=p}^{q} (−1)^{i+1} m_i = x · Σ_{i=p}^{q} (−1)^{i+1}`, and the **tail**
`C := Σ_{i>q} (−1)^{i+1} m_i`.

*Block sum.* `Σ_{i=p}^{q} (−1)^{i+1}` is an alternating sum of `L_0` consecutive `±1`'s
starting with sign `(−1)^{p+1}`; telescoping in pairs, this equals `(−1)^{p+1}` if `L_0` is
odd and `0` if `L_0` is even. So `B = x·(−1)^{p+1}·[L_0 \text{ odd}]`.

Now delete the two chosen entries (at *any* two positions inside `[p,q]`, say `p ≤ p_1 < p_2
≤ q` — since all these entries have the same value `x`, which two are removed does not
affect the multiset of *values* left in the run, so we may take them to be the last two
positions of the run without loss of generality for the value bookkeeping). Effects:

- **Head** (`positions < p`): untouched — contributes `A` again.
- **Run remainder**: the block shrinks to `L_0 − 2` copies of `x`, still occupying
  positions starting at `p` (they slide down to fill positions `p,…,p+L_0−3`). Its
  contribution is `B' = x·(−1)^{p+1}·[(L_0−2) \text{ odd}]`. Since `L_0−2` and `L_0` have the
  *same parity*, `[(L_0-2)\text{ odd}] = [L_0 \text{ odd}]`, so `B' = B`.
- **Tail** (`positions > q`): exactly 2 elements were removed, both at position `≤ q`, so
  every tail position shifts down by exactly 2. Shifting a position by 2 preserves its
  parity, hence preserves the sign `(−1)^{i+1}` attached to each tail value — so the tail's
  contribution is unchanged: `C' = C`.

Hence `e(M') = A + B' + C' = A + B + C = e(M)`. ∎

*(Remark: this is why the removed positions need not be rank-adjacent — the elements
strictly between two equal-valued removed entries are forced, by sortedness, to equal the
same value `x`, so the "run" computation above already accounts for them; the parity
argument goes through for the whole run at once, not merely for two adjacent ranks.)*

## Lemma P-zero (corollary, in `e = L − X` form)

Lemma P **is** the statement "removing (or, reading it backwards, inserting) a pair of
equal-valued elements leaves `e = L − X` exactly unchanged" — no separate argument about `L`
and `X` individually is needed. In particular:

- If a move (a cut) creates two new equal-valued pieces `{x,x}` that occupy two positions of
  the sorted multiset, then `e(\text{after}) = e(\text{multiset with that pair deleted})`
  exactly.
- Applying Lemma P twice removes two *different* value-pairs with no interaction (the second
  application's "head/block/tail" decomposition is computed on the multiset already reduced
  by the first removal; since the argument only used sortedness and equal value within a
  run, it composes without extra cross terms).

## Use

This lemma is the mechanical engine behind the upper-bound induction: whenever Xiang Yu's cut
creates a pair of equal pieces, `e` after the cut equals `e` of the *residual* multiset with
that pair struck out, with **no leftover correction term**, allowing induction on the
residual (fewer pieces / fewer remaining cuts).
