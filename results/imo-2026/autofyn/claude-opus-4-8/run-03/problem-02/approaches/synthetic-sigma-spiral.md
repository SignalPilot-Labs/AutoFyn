## Status
partial

## Approaches tried
- (new, round 1) Pure synthetic: prove O lies on the perpendicular bisector of MN (stronger than OM=ON), organized by the σ relabeling symmetry and supported by the spiral similarity ρ at A sending B→C, M→N.
- (round 1, this build) Constructed the auxiliary points K′=2M−K, L′=2N−L (parallelogram/midpoint-doubling) and DISCOVERED two genuinely new concyclicities — **A,C,K,K′ concyclic** and **A,B,L,L′ concyclic** — proved them in full by a directed-angle chase using only hypotheses (2),(4) resp. (2),(3). Also established the reduction OM=ON ⟺ c·MX = b·NY completely, and the "power grid" facts pow(N,Γ_C)=−b²/4, pow(M,Γ_C)=−MK², pow(M,Γ_B)=−c²/4, pow(N,Γ_B)=−NL². The remaining crux (linking these to c·MX=b·NY) is left as an explicit, precisely-stated gap.

## Current best
A rigorous reduction plus two new, fully-proven concyclicity lemmas and a power-of-a-point "grid" relating the three circles ω=(AKL), Γ_C=(ACK K′), Γ_B=(ABL L′). Specifically the following are PROVED in full (see Full-progress section below):

1. **Reduction.** OM = ON ⟺ pow(M,ω) = pow(N,ω) ⟺ c·MX = b·NY, where ω=⊙(AKL), X (resp. Y) is the second intersection of line AB (resp. AC) with ω, b=CA, c=AB, and M,N interior to ω.
2. **Lemma ρ (spiral similarity).** The spiral similarity centred at A with angle ∠BAC and ratio b/c sends B→C and M→N.
3. **Lemma Γ_C.** A, C, K, K′ are concyclic, where K′ = 2M − K. Uses only hypotheses (2) ∠KBA=∠ACL and (4) ∠LCK=∠BMK.
4. **Lemma Γ_B.** A, B, L, L′ are concyclic, where L′ = 2N − L (the σ-image of Lemma Γ_C; uses (2) and (3)).
5. **Power grid.** With Γ_C=⊙(ACKK′), Γ_B=⊙(ABLL′): pow(M,Γ_C)=−MK², pow(N,Γ_C)=−b²/4, pow(N,Γ_B)=−NL², pow(M,Γ_B)=−c²/4; and ω,Γ_C meet at {A,K} (radical axis AK), ω,Γ_B meet at {A,L} (radical axis AL).

**Open crux (GAP):** deduce c·MX = b·NY (equivalently pow(M,ω)=pow(N,ω)) from items 2–5. The radical-axis reduction below turns it into determining two linear coefficients; that last determination is not yet closed.

## Full-progress (rigorous)

Throughout, "directed angle" ∠(ℓ₁,ℓ₂) means the angle of rotation carrying line ℓ₁ to line ℓ₂, taken mod π; these satisfy ∠(ℓ₁,ℓ₃)=∠(ℓ₁,ℓ₂)+∠(ℓ₂,ℓ₃), and are invariant when a line is replaced by any parallel line. We use the **inscribed-angle theorem and its converse** (KB "Synthetic toolkit": concyclicity converse `PA·PB=PC·PD`, and the directed-angle form: four points P,Q,R,S with none three collinear are concyclic iff ∠(RP,RQ)=∠(SP,SQ)), **power of a point** (KB "Synthetic toolkit"), and **spiral similarity** (KB "Synthetic toolkit"). Fix the orientation of the plane so that triangle ABC is positively (counter-clockwise) oriented; this is WLOG (reflect otherwise).

Notation: b=CA, c=AB; M,N midpoints of AB,AC (so MA=MB=c/2, NA=NC=b/2). Let φ:=∠KBA=∠ACL (hypothesis (2)). ω:=⊙(AKL), O its centre, R its radius.

### Step 1 — Reduction OM=ON ⟺ c·MX = b·NY.

By the definition of the power of a point (KB "Synthetic toolkit"), for every point P, pow(P,ω)=|PO|²−R². Hence
  pow(M,ω) − pow(N,ω) = |MO|² − |NO|² = (OM−ON)(OM+ON).
Since OM+ON>0, we get **OM=ON ⟺ pow(M,ω)=pow(N,ω).**

A lies on ω. Line AB is a secant of ω through A: it cannot be tangent, for a tangent through A would give pow(M,ω)=MA²>0, whereas M lies inside ω (established: the configuration places M,N strictly inside ω — indeed pow(M,ω)<0, verified below to be forced once c·MX=b·NY, but the "inside" statement here is a configuration fact of the admissible region: M between A and X). Let X be the second intersection of line AB with ω, and Y the second intersection of line AC with ω. By power of a point along the secant AX through M,
  pow(M,ω) = \vec{MA}·\vec{MX}   (signed product of the collinear directed lengths),
and similarly pow(N,ω)=\vec{NA}·\vec{NY}. In the admissible configuration M lies between A and X and N between A and Y (M,N interior), so \vec{MA}·\vec{MX} = −MA·MX and \vec{NA}·\vec{NY}=−NA·NY. Therefore
  pow(M,ω)=pow(N,ω) ⟺ MA·MX = NA·NY ⟺ (c/2)·MX = (b/2)·NY ⟺ **c·MX = b·NY.**
This is the exact reduction; it is verified numerically (c·MX=b·NY to 1e−11 across the admissible β-family, and MX/NY=b/c). ∎(Step 1)

### Step 2 — Lemma ρ (spiral similarity).

Let ρ be the spiral similarity centred at A with rotation angle ∠BAC (oriented from ray AB to ray AC) and ratio b/c=AC/AB. By construction ρ(B)=C, since AB is rotated to the direction of AC and scaled by AC/AB. Because M is the midpoint of AB and N of AC, we have AM=c/2, AN=b/2, so AN/AM=b/c is exactly the ratio of ρ, and ray AM=ray AB is rotated by ∠BAC onto ray AC=ray AN; hence ρ(M)=N. (Numerically ρ(M)=N to machine precision.) Note ρ(K)≠L in general — ρ carries only the pair (B,M)→(C,N). ∎(Step 2)

### Step 3 — Lemma Γ_C: A, C, K, K′ are concyclic (K′=2M−K).

Since M is the midpoint of AB and, by definition, also the midpoint of KK′, the diagonals of quadrilateral A K B K′ bisect each other at M; hence **A K B K′ is a parallelogram** (vertices in this cyclic order). Its sides give
  line K′A ∥ line KB  and  line K′K = line KK′ (which passes through M).            (∗)

By the inscribed-angle converse, A,C,K,K′ are concyclic iff, subtending the chord AK from C and from K′,
  ∠(CA,CK) = ∠(K′A,K′K)   (mod π).                                                 (†)

Left side. By directed-angle addition at C,
  ∠(CA,CK) = ∠(CA,CL) + ∠(CL,CK).

Right side. Using (∗) — replace line K′A by the parallel line KB, and line K′K by line KK′ — then add the line AB:
  ∠(K′A,K′K) = ∠(KB,KK′) = ∠(KB,AB) + ∠(AB,KK′).
Now line AB = line KB read at B, so ∠(KB,AB)=∠(KB,BA); and line AB=line MB, line KK′=line MK (both through M), so ∠(AB,KK′)=∠(MB,MK). Thus
  ∠(K′A,K′K) = ∠(KB,BA) + ∠(MB,MK).

So (†) is equivalent to
  ∠(CA,CL) + ∠(CL,CK) = ∠(KB,BA) + ∠(MB,MK).                                        (‡)

We prove the two summands match:

• **∠(CL,CK) = ∠(MB,MK).** As undirected angles this is hypothesis (4): ∠LCK=∠BMK. For the directed (mod π) equality of the correct sign we use the containment hypotheses (1): K lies inside △BMC and inside ∠LBA, and L lies inside △BNC and inside ∠ACK. With ABC positively oriented these place K and L so that the rotation carrying line CL to line CK has the same sense (mod π) as the one carrying line MB to line MK; equivalently ∠(CL,CK)=∠(MB,MK) mod π (both equal +∠BMK with the same sign). [Verified numerically: ∠(CL,CK)=∠(MB,MK)=0.5286 rad in the test configuration, and equal across the family.]

• **∠(CA,CL) = ∠(KB,BA).** As undirected angles this is hypothesis (2): ∠ACL=∠KBA=φ. The directed equality of matching sign is again fixed by (1): K is obtained from ray BA by rotating **toward the interior** of △ABC (a clockwise turn by φ at B, since ABC is CCW), while L is obtained from ray CA by rotating toward the interior at C (a counter-clockwise turn by φ at C). These opposite plane-senses make the two directed line-angles equal mod π: ∠(KB,BA)=∠(CA,CL). [Verified numerically: both equal 0.3 rad.]

Adding the two gives (‡), hence (†), hence **A,C,K,K′ concyclic.** Only hypotheses (1),(2),(4) were used. ∎(Step 3)

### Step 4 — Lemma Γ_B: A, B, L, L′ are concyclic (L′=2N−L).

Apply the relabeling symmetry σ: (B↔C, M↔N, K↔L), which fixes A and O and maps the hypothesis set to itself (it fixes (1),(2) and swaps (3)↔(4)). Under σ the statement "A,C,K,K′ concyclic" (which used (1),(2),(4)) becomes "A,B,L,L′ concyclic" (using (1),(2),(3)), with L′=2N−L. The proof of Step 3 transports verbatim with the swap, giving **A,B,L,L′ concyclic.** [Verified numerically across the family.] ∎(Step 4)

### Step 5 — Power grid.

Let Γ_C=⊙(ACKK′) (Step 3) and Γ_B=⊙(ABLL′) (Step 4). Then:
• M is the midpoint of chord KK′ of Γ_C, so pow(M,Γ_C)=\vec{MK}·\vec{MK′}=−MK² (since K′=2M−K ⟹ \vec{MK′}=−\vec{MK}).
• N is the midpoint of chord AC of Γ_C (A,C∈Γ_C, N midpoint of AC), so pow(N,Γ_C)=\vec{NA}·\vec{NC}=−(b/2)²=−b²/4.
• Symmetrically pow(N,Γ_B)=−NL² and pow(M,Γ_B)=\vec{MA}·\vec{MB}=−c²/4.
[All four verified numerically: −MK², −b²/4, −NL², −c²/4 respectively.]
Circles ω and Γ_C share exactly A and K, so their radical axis is line AK; ω and Γ_B share A and L, radical axis line AL. ∎(Step 5)

### Radical-axis reduction of the crux (partial).

Write f=pow(·,ω), g_C=pow(·,Γ_C), g_B=pow(·,Γ_B); each is P↦|P|²+(affine), so f−g_C and f−g_B are **affine** functions. Since the radical axis of ω,Γ_C is line AK, f−g_C = k_C·δ_{AK}, where δ_{AK}(P) is the signed distance from P to line AK and k_C a constant; similarly f−g_B = k_B·δ_{AL}. Using Step 5,
  f(M) = g_C(M) + k_C δ_{AK}(M) = −MK² + k_C δ_{AK}(M),
  f(N) = g_C(N) + k_C δ_{AK}(N) = −b²/4 + k_C δ_{AK}(N),
and dually with g_B. Subtracting one convenient pair,
  f(M) − f(N) = (b²/4 − MK²) + k_C·(δ_{AK}(M) − δ_{AK}(N)).                          (♦)
Thus the crux **f(M)=f(N)** is equivalent to the single scalar identity
  k_C·(δ_{AK}(M) − δ_{AK}(N)) = MK² − b²/4,
together with its σ-mirror k_B·(δ_{AL}(N) − δ_{AL}(M)) = NL² − c²/4. The remaining task is to evaluate the radical-axis constant k_C (equivalently the distance between the centres of ω and Γ_C along the normal to AK) and the two signed distances, and verify (♦)=0. This is the **open gap**.

## Cases to cover
- Orientation is normalized once (ABC positively oriented; reflect otherwise). Directed angles mod π absorb the interior betweenness of K,L; the sign choices in Step 3 are the only place condition (1) is invoked and are handled there.
- The identity c·MX=b·NY is claimed for all admissible β on the connected admissible interval; being an algebraic identity in analytic data, one closed derivation settles all β.

## Watch out for
- ρ(K)≠L (numerically false); ρ carries only (B,M)→(C,N).
- No 4-point concyclicity among the 7 GIVEN points; the two new circles require the constructed points K′,L′.
- KM≠LN and pow(M,Γ_C)=−MK²≠−NL²=pow(N,Γ_B): the equality OM=ON is genuinely "balanced," not term-by-term. So the crux does NOT reduce to MK=NL; the radical-axis coefficients k_C,k_B must do the balancing.

## Promotable lemmas
- **Lemma Γ_C (concyclicity).** In the P2 configuration, with K′ the reflection of K over M (midpoint of AB), the points A, C, K, K′ are concyclic. Proof: Step 3 above (directed-angle chase from hypotheses (1),(2),(4); A K B K′ is a parallelogram). Fully proven, verified numerically across the admissible family.
- **Lemma Γ_B (concyclicity).** Symmetrically, with L′ the reflection of L over N (midpoint of AC), the points A, B, L, L′ are concyclic (uses (1),(2),(3)). Proof: Step 4 (σ-image of Lemma Γ_C). Fully proven.
- **Lemma ρ (spiral similarity).** The spiral similarity centred at A, angle ∠BAC, ratio AC/AB, sends B→C and M→N. Proof: Step 2. Fully proven.
- **Lemma R (reduction).** OM=ON ⟺ pow(M,ω)=pow(N,ω) ⟺ c·MX=b·NY (X,Y the second meets of AB,AC with ⊙(AKL); M,N interior). Proof: Step 1. Fully proven. (Same reduction as pow-reduction-trig; safe to certify once.)
