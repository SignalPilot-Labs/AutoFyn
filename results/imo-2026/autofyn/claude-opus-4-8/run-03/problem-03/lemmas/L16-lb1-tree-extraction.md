# Lemma L16 — LB1 tree-extraction signed-sum lower bound (+ L17 dyadic Δ)

**Status:** CERTIFIED (proof-reviewer, round 6). Independently verified: 0 violations over
n=1..4, 400 random ≤n-split refinements of dyadic A each; edge cases traced by hand.

**L16 (LB1).** For A = {a_1,…,a_m} with m = n+1 parts and every refinement B reachable by ≤ n
XY-splits, S(B) ≥ Δ(A), where Δ(A) := min over ε∈{−1,0,1}^m, ε≠0, of |Σ_i ε_i a_i|.

**Proof.** Sort B descending; S(B) = Σ_{i}(b_(2i−1)−b_(2i)) [+ b_(N) if N odd] = Σ_e d_e over
edges of a multigraph G: vertices = the m parts + a dummy δ (a_δ:=0), so V = n+2; one edge per
consecutive pair {parent(b_(2i−1)),parent(b_(2i))} with gap d_e = b_(2i−1)−b_(2i), and a
singleton edge {parent(b_(N)),δ} (d_e=b_(N)) if N odd. E = ⌈N/2⌉; since N = (n+1)+s, s≤n,
N ≤ 2n+1 so E ≤ n+1 < n+2 = V. Then Σ_c(v_c−e_c) = V−E ≥ 1 and each connected component has
v_c−e_c ≤ 1 (=1 iff tree), so #tree-components ≥ V−E ≥ 1. A tree component with a real part
exists: no part-vertex is isolated (each has ≥1 piece = ≥1 incidence); if N odd δ has degree 1
(not isolated) so no lone-δ tree; if N even, N≤2n ⟹ E≤n ⟹ V−E≥2 ⟹ ≥2 tree components, at most
one lone δ. Take such a tree K, 2-color it σ:K→{±1}. **Edge-length identity** (valid because K is
a union of components, so every edge incident to K has both endpoints in K, and every piece of a
part in K is one incidence of one edge in K): Σ_{v∈K} σ(v)a_v = Σ_{e∈K}(σ(u_e)L_e+σ(w_e)ℓ_e).
Each tree edge joins the two color classes, so each term = ±(L_e−ℓ_e) = ±d_e, giving
|Σ_{v∈K}σ(v)a_v| ≤ Σ_{e∈K} d_e ≤ Σ_{all e} d_e = S(B). Set ε_p=σ(p) on part-vertices of K, 0
elsewhere (δ drops, a_δ=0); ε≠0 since K has a real part, so Δ(A) ≤ |Σ ε_i a_i| ≤ S(B).
(Self-loops are 1-cycles, never in a tree component.) ∎

**L17 (LB2, dyadic Δ).** For a_i = 2^{i−1}/D_n (i=1..n+1), D_n=2^{n+1}−1: Σ a_i = 1 and
Δ(A) = 1/D_n. **Proof.** Δ = (1/D_n)·min|Σ ε_i 2^{i−1}| over nonzero ε∈{−1,0,1}^{n+1}. Let j be
the top nonzero index: |Σ_{i<j}ε_i 2^{i−1}| ≤ 2^{j−1}−1 < 2^{j−1}, so the sum is a nonzero
integer, |·| ≥ 1; equality by ε=(1,0,…,0). ∎

Depends on: L4 (for S(B)=Σ d_e via the consecutive pairing).
</content>
