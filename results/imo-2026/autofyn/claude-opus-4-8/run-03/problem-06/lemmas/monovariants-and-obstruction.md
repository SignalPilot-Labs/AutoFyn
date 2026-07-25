# Certified monovariants A, B + A_n-only Obstruction (round 2)

Source: `monovariant-witness-descent`. Reviewer-verified round 2 (proofs re-derived; density and
max-gap re-simulated for a₁=375: density 0.467→0.410→0.283→0.274→…(non-increasing, floor 1/M=1/15),
max-gap 3→3→6→6→… freezes at 6; obstruction density 1/2+(1/2)∏1/q_k confirmed 0.667→0.533→0.505→…).

Notation: A_n = {c : gcd(c,a_i)>1 ∀i≤n}, a union of residue classes mod D_n=∏(primes dividing
some a_i, i≤n); M=rad(a₁).

## Lemma A (density monovariant). δ_n:=density(A_n) is non-increasing, δ_n≥1/M>0, and
δ_{n+1}=δ_n ⟺ A_{n+1}=A_n (equality detects a non-recruitment exactly).
*Proof.* A_{n+1}=A_n∩{c:c meets F_{n+1}}⊆A_n ⇒ monotone density. Multiples of M ⊆ A_n (L1:
each F_i has p∈P, p|M) ⇒ δ_n≥1/M. A_n∖A_{n+1} is a union of residues mod D_{n+1}; nonempty ⇒
density ≥1/D_{n+1}>0. ∎

## Lemma B (max-gap monovariant). γ_n∈{1,…,M} (largest gap between consecutive elements of the
periodic set A_n) is non-decreasing and ≤M, hence eventually constant (well-ordering).
*Proof.* Multiples of M present ⇒ γ_n≤M. A_{n+1}⊆A_n deletes points ⇒ gaps only enlarge ⇒ γ
non-decreasing. Non-decreasing integer sequence bounded above stabilizes. ∎

## Obstruction (A_n-only statistics cannot certify the Crux). CONCRETE, rigorous witness:
fix a prime p* and primes q_1<q_2<…; G_k={p*,q_k}, 𝓖_n={G_1,…,G_n},
A(𝓖_n)={c:∀k≤n, p*|c or q_k|c}. Then 𝓖 is intersecting (share p*), anchored (all ∋ p*), every
G_k is ⊆-minimal (distinct 2-sets, no singleton) so Π(𝓖)={p*,q_1,q_2,…} is INFINITE; yet
density(A(𝓖_n)) = 1/p* + (1−1/p*)∏_{k≤n}1/q_k → 1/p* (converges, never freezes) and max-gap ≤ p*
(non-decreasing, freezes in finite time). So density-freeze / max-gap-freeze / any statistic
computed from A_n alone is consistent with Π infinite.
*Status of the meta-claim.* The CONCRETE family above is rigorous and verified. The broader slogan
"no monovariant that is a function of A_n alone can prove the Crux" is a heuristic reading of it,
not a formal theorem (there is no formal definition of "monovariant"); treat it as a cautionary
negative result, not a certified impossibility theorem.

## Consequence (honest). Density (A) converges but need not freeze (recruitment costs →0 as a
convergent series); max-gap (B) freezes but does not bound recruitment. The Crux needs the greedy
CHOICE dynamics a_n, not a set-statistic of A_n. This coincides with the antichain §7b caution.
