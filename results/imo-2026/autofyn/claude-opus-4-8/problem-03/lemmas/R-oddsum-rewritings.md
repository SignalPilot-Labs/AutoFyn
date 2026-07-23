# Lemmas R1/R2 — odd-sum rewritings (certified round 2)

For a fixed multiset of pieces sorted decreasingly with total length 1, let
N(t) = #{pieces of length > t} (a decreasing step function of t ≥ 0), and let
O = Σ_{i odd} r_i (odd-ranked sum), E = Σ_{i even} r_i, A = O − E (= alternating sum).

**Lemma R1 (layer-cake).** O = ∫_0^∞ ⌈N(t)/2⌉ dt and E = ∫_0^∞ ⌊N(t)/2⌋ dt.

*Proof.* For fixed t the pieces of length > t are exactly ranks 1,…,N(t); among these there
are ⌈N(t)/2⌉ odd ranks. An odd-ranked piece r_i is counted in ⌈N(t)/2⌉ exactly for t < r_i,
so ∫_0^∞ ⌈N(t)/2⌉ dt = Σ_{i odd} r_i = O. Same for E with ⌊·⌋. ∎

**Lemma R2 (parity form).** With total length 1,
  O = 1/2 + (1/2)·μ{ t ≥ 0 : N(t) odd },
where μ is Lebesgue measure; equivalently O = (1 + A)/2 with A = μ{N(t) odd}.

*Proof.* ⌈N/2⌉ = N/2 + (1/2)·[N odd]. By R1, O = (1/2)∫N dt + (1/2)∫[N odd] dt =
(1/2)·1 + (1/2)·μ{N odd}. Since O + E = 1 and O − E = A, O = (1+A)/2, so A = μ{N odd}. ∎

**Consequence.** For the target c(n) = 2^n/D (D = 2^{n+1}−1): since 2^n/D − 1/2 = 1/(2D),
  O ≥ 2^n/D ⟺ A = μ{N odd} ≥ 1/D,   O ≤ 2^n/D ⟺ μ{N odd} ≤ 1/D.

**Subsumes** the "AltSum reformulation" of approach induction-recursion (O = (1+AltSum)/2 is
exactly O = (1+A)/2 here).

**Verification.** O computed directly vs O = 1/2 + (1/2)μ{N odd} agree to 1e-9 on 3000
random normalised configs (sizes 1–8).

**Certification.** Reviewer-verified round 2. Both statements correct, proofs sorry-free.
Admitted to shared cache.
