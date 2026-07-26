# close-encounter-lemma

*Certified by proof-reviewer, round 1. Proven in `results/imo-2026-05/approaches/orbit-close-encounter.md` (Step 3) and `results/imo-2026-05/approaches/gm-lipschitz-partition.md` (Step 4).*

## Statement

Let `A = {a + np : n ≥ 0}`, `B = {b + mq : m ≥ 0}` with `p, q > 0` be two unbounded forward arithmetic progressions. Then for every `ε > 0` there exist `n, m ≥ 0` with

$$|A_n - B_m| \le \epsilon, \qquad \min(A_n, B_m) \to \infty$$

(i.e. arbitrarily large `ε`-close encounters), **provided** either (i) `p/q ∉ ℚ`, or (ii) `p/q ∈ ℚ` and `ε ≥ δ₀`, where `δ₀ := min_{k ∈ ℤ} |a − b + k·d| ∈ (0, d/2]` with `d := gcd(p, q)`, and `a ≢ b (mod d)`.

If `p/q ∈ ℚ` and `a ≡ b (mod d)`, the two progressions **collide** (`A_n = B_m` for some `n, m`).

## Proof

**Case (i): `p/q ∉ ℚ`.** The sequence of fractional parts `{((a + np) − b)/q}_{n ≥ 0}` is dense (equidistributed) in `[0, 1)` by **Kronecker / Weyl equidistribution** (`knowledge_base.md`). For any `N` there exists `n ≥ N` with `{((a+np)−b)/q} ∈ [0, ε/q] ∪ [1 − ε/q, 1)`. Taking `m := ⌊((a+np)−b)/q⌋ ≥ 0` (for `n` large enough), `|(a+np) − (b + mq)| ≤ ε`, and `A_n = a + np → ∞`.

**Case (ii): `p/q ∈ ℚ`.** Write `p = Pd`, `q = Qd` with `gcd(P, Q) = 1` and `d = gcd(p, q)`. Then `A ⊆ a + dℤ` and `B ⊆ b + dℤ`.

- *Same residue class* (`a ≡ b mod d`): `(a − b)/d =: k_0 ∈ ℤ`. By **Bézout's identity** (`knowledge_base.md`), `gcd(P, Q) = 1` gives integers `n_0, m_0` with `n_0 P − m_0 Q = −k_0`; the full solution family is `(n_0 + tQ, m_0 + tP)` for `t ∈ ℤ`. For `t → +∞`, both `n, m ≥ 0`, and `A_n = B_m` (collision).

- *Distinct residue classes* (`a ≢ b mod d`): The cyclic distance between residue classes is `δ₀ = min_{k∈ℤ} |a − b + kd| ∈ (0, d/2]`. Pick `k_* ∈ ℤ` with `a − b + k_* d = ±δ₀`. We seek `n, m ≥ 0` with `A_n − B_m = a − b + d(Pn − Qm) = ±δ₀`, i.e. `Pn − Qm = k_*`. By Bézout, one integer solution `(n_0, m_0)` exists; the full family is `(n_0 + Qℓ, m_0 + Pℓ)` for `ℓ ∈ ℤ`. Taking `ℓ → +∞` makes both `n, m → +∞` (since `P, Q > 0`); for `ℓ` large enough, `n, m ≥ 0`. For these, `|A_n − B_m| = δ₀ ≤ ε`, and `min(A_n, B_m) → ∞`. ∎

## Note

When applied with `p = c_a, q = c_b` (positive values of `g`), the hypothesis `ε ≥ δ₀` is satisfied for `ε = c_a/2` because `d = gcd(c_a, c_b) ≤ c_a` (since `d | c_a`), so `δ₀ ≤ d/2 ≤ c_a/2 = ε`.
