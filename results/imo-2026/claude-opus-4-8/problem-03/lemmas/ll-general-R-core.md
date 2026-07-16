# Lemma (General-R core of Lemma LL + budget-reduction, lower bound)

**Status:** CERTIFIED (proof-reviewer, round 8). Proposed by `ll-dyadic-symdiff`. Reviewer verified the
three sub-case proofs use only `max(R) ≤ 2^{n−1}` / `A(R) ≥ 1` / the piece list (no `G_{n−1}`-band
structure), and the budget-reduction arithmetic is immediate. Target `A(Q∪R) ≥ 1` holds 0-violation over
the n=3 refined grid (budget enforced).

## Budget-reduction lemma
Joint cut budget `c_Q + c_R ≤ n` with `c_Q = |Q| − 1`. If `R` is refined (`c_R ≥ 1`) then
`|Q| = c_Q + 1 ≤ (n − c_R) + 1 ≤ n`.

## General-R core (Cases 1 / 2 / Sub-3a are R-agnostic)
For `P = Q ∪ R` with `ΣQ = 2^n`, `max(R) ≤ 2^{n−1}` (hence `S_R ⊆ [0, 2^{n−1})`), `A(R) ≥ 1`, the
following prove `A(Q∪R) = measure(S_Q △ S_R) ≥ 1` using no structure of `R` beyond `S_R ⊆ [0,2^{n−1})`:

- **Case 1** (`max(Q) ≥ 2^{n−1} + 1`): the unique Q-part `μ > 2^{n−1}` gives `N_Q = 1` (odd) on
  `[2^{n−1}, μ)` while `N_R = 0` there, so `[2^{n−1}, μ) ⊆ S_Q △ S_R`, measure `≥ μ − 2^{n−1} ≥ 1`.
  (= certified `ll-case1-high-interval.md`.)
- **Case 2** (`|P|` odd, all pieces `≥ 1`): `A(P) ≥ 1` by certified `parity-piece-count.md` (Lemma P).
- **Sub-3a** (some full dyadic level `I_k` has `N_P` odd throughout): `I_k ⊆ S_P`, measure `≥ 1`
  (= certified `dyadic-level-parity.md`).

## Scope
This is an assembly of already-certified lemmas made R-general. The residual (Sub-3b: no fully-odd
level, even count) for **refined `R`** is NOT closed. Its reflection-based reduction (double-REFL for
refined `R` with the top piece `2^{n−1}` uncut, giving `A(Q∪R) = 2^{n−1} − q₁ + A(Q'∪R')`) closes
branches B3a-ref/B3b-ref for all `n`, but the crux residual `(B2*)-ref` `A(Q'∪R') ≥ 1` and the top-cut
bucket (no reflection anchor) remain open — the refined-R analogue of the shared LB crux.
