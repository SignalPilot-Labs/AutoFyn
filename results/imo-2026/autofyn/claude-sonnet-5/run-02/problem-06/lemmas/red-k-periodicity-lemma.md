## Lemma: Right-Extension Determinism ⟹ Eventual Periodicity (Lemma B, certified)

**Source.** `subword-complexity-periodicity`, round 12. Independently re-verified
by the proof-reviewer (round 12). A fully general, problem-independent fact about
sequences over a finite alphabet — the concrete pigeonhole + induction mechanism
underlying the "if `p(k₀) ≤ k₀` then eventually periodic" direction of the
Morse–Hedlund theorem, carried out explicitly rather than cited by name.

**Depends on.** Nothing problem-specific — pure combinatorics on words plus the
infinite pigeonhole principle (`knowledge_base.md`, "Pigeonhole / extremal
principle").

**Setup.** Let `x = (x_1, x_2, x_3, …)` be any infinite sequence over a finite
alphabet `Σ`. For `k ≥ 1` and `i ≥ 1` write `W_k(i) := (x_i, x_{i+1}, …,
x_{i+k-1})`. Say `x` satisfies **Right-Extension Determinism at level `k`**
(`RED_k`) if: for all `i < j`, `W_k(i) = W_k(j)` implies `x_{i+k} = x_{j+k}`.

**Lemma.** If `RED_k` holds for `x` for some `k ≥ 1`, then `x` is eventually
periodic: there exist `N ≥ 1` and `T ≥ 1` with `x_{n+T} = x_n` for all `n ≥ N`.

**Proof.** Since `Σ^k` is finite (`|Σ|^k` elements) and there are infinitely many
positions `i = 1,2,3,…`, the map `i ↦ W_k(i)` cannot be injective (infinite
pigeonhole): there exist `i < j` with `W_k(i) = W_k(j)`. Fix such `i, j` and set
`T := j - i ≥ 1`.

*Claim:* `x_{i+m} = x_{j+m}` for every `m ≥ 0`. Proof by strong induction on `m`.
- Base cases `0 ≤ m ≤ k-1`: exactly the hypothesis `W_k(i) = W_k(j)`.
- Inductive step: let `m ≥ k-1` and suppose `x_{i+m'} = x_{j+m'}` for every
  `0 ≤ m' ≤ m`. In particular for `m' = m-k+1, …, m` (all `≥ 0` since `m ≥ k-1`).
  Setting `i' := i+m-k+1`, `j' := j+m-k+1` (so `j'-i' = j-i = T > 0`, `i' < j'`),
  this says `W_k(i') = W_k(j')`. Applying `RED_k` to `i' < j'` gives
  `x_{i'+k} = x_{j'+k}`, i.e. `x_{i+m+1} = x_{j+m+1}`, the case `m'=m+1`.

By induction the claim holds for all `m ≥ 0`. Hence `x_n = x_{n+T}` for every
`n ≥ i`. Take `N := i`. ∎

**Corollary (RED_1 ⟹ RED_k monotonicity).** If `RED_1` holds for `x`, then `RED_k`
holds for `x` for every `k ≥ 1`. *Proof:* if `W_k(i) = W_k(j)` then in particular
`x_{i+k-1} = x_{j+k-1}`; applying `RED_1` to `(i+k-1, j+k-1)` gives
`x_{i+k} = x_{j+k}`. ∎ So `RED_1` is the strongest member of this family and larger
`k` gives a strictly weaker hypothesis.

**Status.** Correct, complete, no gaps, fully unconditional and fully general (no
dependence on this problem's structure at all). Independently re-derived by the
reviewer — the sliding-window strong induction is valid, `i',j'` remain legitimate
positions (`i' ≥ i ≥ 1`) at every step. Certified as a standalone reusable
combinatorics-on-words tool, usable both within this problem and by unrelated
problems needing this exact mechanism.
