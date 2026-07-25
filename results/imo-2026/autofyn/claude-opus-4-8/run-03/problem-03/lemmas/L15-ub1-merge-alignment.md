# Lemma L15 — UB1 merge-alignment refinement (upper-bound engine)

**Status:** CERTIFIED (proof-reviewer, round 6). Independently verified: 0 failures over
n=1..5, 200+ random A each, exact `Fraction` — both `S(B) ≤ |Σ(S)−Σ(T)|` AND cut count ≤ m−1.

**Statement.** Let A = {a_1,…,a_m}, Σ a_i = 1, and S,T ⊆ {1,…,m} disjoint, (S,T)≠(∅,∅). Then
XY has a refinement B of A, using at most m−1 splits, with S(B) ≤ |Σ(S)−Σ(T)|
(Σ(S)=Σ_{i∈S}a_i).

**Proof.** WLOG Σ(S) ≥ Σ(T). Let L = {1,…,m}∖(S∪T). XY: (a) bisect each leftover a_i (i∈L)
into two equal halves (|L| splits, |L| cost-0 twin pairs); (b) lay the S-parts as a block on
[0,Σ(S)] with boundaries at the S-partial-sums and the T-parts as a block on [0,Σ(T)] with
boundaries at the T-partial-sums; cut BOTH blocks at the union C of all boundaries lying in
[0,Σ(T)]. In each cell of C the S-block and T-block each have exactly one sub-piece of the same
length, giving q matched equal pairs (cost 0 each). The S-mass in (Σ(T),Σ(S)] forms overhang
pieces of total mass Σ(S)−Σ(T). By **L4** (min-pairing), S(B) ≤ cost of the explicit partition
{twin pairs (0) + matched pairs (0) + overhang paired among themselves}; the overhang cost is
Σ_{pairs}|u−v| + (≤1 singleton) ≤ Σ(overhang mass) = Σ(S)−Σ(T) (using |u−v| ≤ u+v). Hence
S(B) ≤ Σ(S)−Σ(T) = |Σ(S)−Σ(T)|. **Cut budget:** (a) |L| = m−|S|−|T|; (b) cuts on S-parts occur
only at T-derived interior points ≤ |T|; cuts on T-parts only at S-derived interior points
S_1,…,S_{|S|−1} (since S_{|S|}=Σ(S)≥Σ(T)) ≤ |S|−1. Total ≤ (m−|S|−|T|)+|T|+(|S|−1) = m−1.
The case T=∅ (leave S whole as overhang, bisect the rest) gives S(B) ≤ Σ(S), ≤ m−|S| ≤ m−1
splits. ∎

Depends on: L4.
</content>
</invoke>
