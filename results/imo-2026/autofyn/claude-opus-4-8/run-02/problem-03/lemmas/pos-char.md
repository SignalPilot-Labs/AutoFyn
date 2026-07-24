# Lemma POS-CHAR (f=0 ⟺ all-even) — CERTIFIED round 7

Source: `dual-integer-certificate` §4. Reviewer independently re-derived and numerically verified.
Unconditional (holds for ANY finite multiset of positive reals) — reusable by every approach.

## Statement
For a finite multiset `P` of positive reals with alternating sum `f(P)=Σ_r σ_r a_r`
(`a_1≥a_2≥…≥a_T` sorted descending, `σ_r=(-1)^{r+1}`):
`f(P)=0` **iff** every distinct value of `P` has even multiplicity ("all-even").
Moreover if `T=|P|` is odd then `f(P) ≥ a_T > 0`.

## Proof
- **`T` even.** `f = Σ_{i=1}^{T/2}(a_{2i-1}-a_{2i})`, each term `≥0` (nonincreasing). So `f≥0`, with
  equality iff `a_{2i-1}=a_{2i}` for every `i`. Equality in every consecutive pair means each distinct
  value's block of equal ranks starts at an odd rank and has even length: if some block had odd length,
  its last element sits at an even rank and the next (different) value starts at the following odd rank,
  making that pair unequal. Hence equality ⟺ every block even length ⟺ all-even. Conversely all-even
  gives sorted `v_1,v_1,v_2,v_2,…` and every pair cancels, `f=0`.
- **`T` odd.** `f = Σ_{i=1}^{(T-1)/2}(a_{2i-1}-a_{2i}) + a_T ≥ a_T > 0`. And odd `T` forces some value
  to have odd multiplicity, so `P` is not all-even. ∎

## Verification (reviewer, independent)
- 200,000 random rational multisets (values `p/q`, sizes 1–8): `f=0 ⟺ all-even` and `T` odd `⟹ f>0`
  held with **0 mismatches**.

## Use
Collapses "Positivity" (`f(P*)≠0`) to a single combinatorial statement — the **Budget Lemma**: no
`≤n`-cut refinement of `W_n` is all-even. In particular it **eliminates the odd-cancellation branch**
(a signed sum of `≥3` distinct odd-block values vanishing): `f` is a sum of nonnegative pair-gaps, so
`f=0` forces every pair-gap zero, i.e. all-even. Reusable by all three routes.
