# Lemma L3 (cleanness invariant / Shan-Yu closure) — CERTIFIED (round 1)

**Statement.** Suppose 180 ∉ θℤ (equivalently 180/θ ∉ ℤ; θ may be irrational). Call a triple *clean* if none of its three angles lies in θℤ = {mθ : m ∈ ℤ}. If the current triple is clean, then for EVERY legal Mulan move (any attacked vertex, any t in (0, attacked angle)) at least one of the two children (per Lemma L0) is clean.

**Proof.** Step 3b of `approaches/residue-divisibility-characterization.md` = Lemma 2A of `approaches/circle-group-quotient.md`: if both children were dirty then, since P, Q ∉ θℤ, we need (t ≡ 0 or t ≡ Q + R) and (t ≡ R or t ≡ −P) mod θ; each of the four combinations forces R ≡ 0, P ≡ 0, Q ≡ 0, or P + Q + R = 180 ≡ 0 (mod θ) — all contradictions. Independently verified by exact-fraction search at θ = 55, 80, 100, 170, 179, 270/7 over all residue-critical t.

**Consequence.** With a clean initial triangle (which exists whenever 180 ∉ θℤ: isoceles (ε, ε, 180 − 2ε) avoiding a finite excluded set), Shan-Yu survives forever — the necessity direction of the problem.
