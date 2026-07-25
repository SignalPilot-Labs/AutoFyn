# Certified lemmas — realizer-value pincer (R1, R2, Prop 12.A, Prop 12.B)

Certified round 4 (proof-reviewer). Source: `approaches/redundant-constraint-antichain.md` §12.
All are UNCONDITIONAL (do not assume the Crux). They build only on certified E1, E2(⇒)
(`enumeration-and-transversal.md`), certified E4 (`size-bound-reduction.md`), and elementary
number theory. Notation: `∏G = ∏_{p∈G} p` (squarefree radical); `P_r = ∏_{i=1}^r p_i` the r-th
primorial (`P_0=1,P_1=2,P_2=6,P_3=30,P_4=210,…`); `K(X) = max{r≥0 : P_r < X}`; `𝓐_∞` the
⊆-minimal supports; `A = {c : F(c) meets every G∈𝓐_∞}`.

## R1 (Realization of G-supported integers).
For `G∈𝓐_∞`, every integer `m ≥ a₁` with `F(m)=G` is a term of the sequence. Hence the smallest
term realizing `G` is `u(G) = min{m ∈ D_G : m ≥ a₁}` where `D_G = {m : F(m)=G}`; it exists, and
`u(G) = ∏G` whenever `∏G ≥ a₁`.

*Proof.* By certified E2(⇒), `G` meets every member of `𝓐_∞`. If `F(m)=G` then `F(m)` meets every
member, so `m∈A`; with `m≥a₁`, certified E1 (`{a_n}=A∩[a₁,∞)`) makes `m` a term. `D_G` = integers
`∏_{p∈G}p^{e_p}`, `e_p≥1`; its least element is `∏G`. If `∏G≥a₁` then `∏G` is the least element of
`D_G∩[a₁,∞)`, so `u(G)=∏G`. ∎

## R2 (Primorial support lower bound).
For any finite prime-set `G`, `u(G) ≥ ∏G ≥ P_{|G|}`. Consequently `∏G < X ⟹ |G| ≤ K(X)`.

*Proof.* `u(G)∈D_G` is divisible by every prime of `G`, so `u(G)≥∏G`. Writing `G`'s primes
increasingly `q_1<⋯<q_{|G|}`, the i-th smallest prime overall `p_i ≤ q_i` (there are ≥ i primes
`≤ q_i`), so `∏G = ∏q_i ≥ ∏p_i = P_{|G|}`. If `∏G<X` then `P_{|G|}<X`, so `|G|≤K(X)` by
monotonicity of `P_r`. ∎ (Independently verified numerically: `∏G≥P_{|G|}` holds on all seeds.)

## Prop 12.A (E5 for the small-radical regime — UNCONDITIONAL, fully closed).
Every minimal support `G∈𝓐_∞` with `∏G < a₁` satisfies `|G| ≤ K(a₁)`.

*Proof.* Apply R2 with `X=a₁`. ∎ This is a complete bound on the infinite subclass `{∏G < a₁}`,
with no open step.

## Prop 12.B (Reduction of E5 to a window inequality — UNCONDITIONAL implication).
If **(W)**: every `G∈𝓐_∞` with `|G|≥2` satisfies `∏(G∖{p_max}) < a₁`, then
`sup_{G∈𝓐_∞}|G| ≤ 1+K(a₁) < ∞`, i.e. E5 holds; by certified E4 the Crux holds, and the theorem
follows (from `n=1`, `T=|ρ(A)|`, `L=∏Π`).

*Proof.* For `|G|≥2`, `G∖{p_max}` has `|G|−1` primes with product `< a₁` by (W); R2 gives
`P_{|G|−1} ≤ ∏(G∖{p_max}) < a₁`, so `|G|−1 ≤ K(a₁)`. For `|G|≤1` trivial. ∎

Note (W) holds automatically when `∏G<a₁` (then `∏(G∖{p_max})≤∏G<a₁`), so the ONLY unproved
content is the residual **E5″ (OPEN)**: every minimal `G` with `∏G≥a₁` has `∏(G∖{p_max}) < a₁`.
Sufficient stronger open form: `∏G < 2a₁`. Numerically (independent sim, round 4): on seeds
`{15,105,375,385,1155,9375}` every minimal `G` has `∏G/a₁ ≤ 1.09`, `∏(G∖{p_max})/a₁ ≤ 0.20`,
all support-primes `≤ a₁`. E5″ is NOT proved.
