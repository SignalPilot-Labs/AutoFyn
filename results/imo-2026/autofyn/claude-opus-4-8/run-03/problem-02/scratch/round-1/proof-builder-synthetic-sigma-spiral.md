# Build report — synthetic-sigma-spiral (imo-2026-02), round 1

Status: **partial** (real, substantial progress; crux left as an explicit gap).

## What I proved in full
1. **Reduction (Step 1):** OM=ON ⟺ pow(M,ω)=pow(N,ω) ⟺ c·MX=b·NY. Clean power-of-a-point; identical in content to pow-reduction-trig's spine but derived independently. Numerically c·MX=b·NY to 1e−11.
2. **Lemma ρ (Step 2):** spiral similarity at A (angle ∠BAC, ratio b/c) sends B→C, M→N. Routine, complete.
3. **TWO NEW CONCYCLICITIES (Steps 3–4) — the headline finding:**
   - **A, C, K, K′ concyclic**, K′=2M−K (reflection of K over M). Proven by directed-angle chase using ONLY hypotheses (1),(2),(4). Mechanism: A K B K′ is a parallelogram (M bisects AB and KK′), so line K′A ∥ KB and line K′K passes through M; then ∠(CA,CK)=∠(CA,CL)+∠(CL,CK) matches ∠(K′A,K′K)=∠(KB,BA)+∠(MB,MK) termwise via (2) and (4).
   - **A, B, L, L′ concyclic**, L′=2N−L (σ-image). Uses (1),(2),(3).
   These are exactly the auxiliary points the explorer/outliner flagged (K′=2M−K), and the concyclicity the field was told did NOT exist among the 7 given points — it appears precisely once K′,L′ are added. Verified across the β-family and across 3 different triangles.
4. **Power grid (Step 5):** pow(M,Γ_C)=−MK², pow(N,Γ_C)=−b²/4, pow(N,Γ_B)=−NL², pow(M,Γ_B)=−c²/4; ω∩Γ_C={A,K}, ω∩Γ_B={A,L}. All verified numerically.

## The open crux (GAP)
Deduce c·MX=b·NY from items 1–5. I reduced it (radical-axis decomposition, eq. (♦)) to a single scalar identity: with f−g_C=k_C·δ_{AK} (affine, vanishing on line AK=radical axis of ω,Γ_C),
  f(M)−f(N) = (b²/4 − MK²) + k_C·(δ_{AK}(M)−δ_{AK}(N)) = 0.
What remains: evaluate the radical-axis constant k_C (normal offset between centres of ω and Γ_C) and the two signed distances to line AK, then verify cancellation (plus its σ-mirror). NOT closed.

Key warning confirmed numerically: MK≠NL and pow(M,Γ_C)=−MK²≠−NL²=pow(N,Γ_B), so the crux is genuinely "balanced," NOT MK=NL. The k_C, k_B radical-axis coefficients must do the balancing — any attempt to finish by a termwise congruence will fail.

## Spec concerns / notes for reviewer & next round
- **Rigor caveat in Step 3:** the directed-angle sign (choosing +φ vs −φ, i.e. ∠(KB,BA)=∠(CA,CL) rather than =−) is justified from the containment hypothesis (1) + fixed CCW orientation of ABC. I argued it and backed each equality with a numeric check, but a reviewer may want the orientation argument tightened into a betweenness lemma. The concyclicity ITSELF is solid (verified across family and multiple triangles); only the prose justification of the mod-π sign is the softer part.
- **Promotable:** Lemmas Γ_C, Γ_B, ρ, R are all fully proven and worth certifying into results/imo-2026-02/lemmas/. Γ_C/Γ_B are new synthetic structure not present in the other approaches and could feed pow-reduction-trig or a future approach (they give MK, NL and the −b²/4, −c²/4 powers cleanly).
- **Diversity value:** this route now owns a distinct mechanism (parallelogram concyclicities + radical grid) far from the trig/coordinate routes. If it can close the (♦) coefficient step next round it yields the short human-checkable proof the reviewer hoped for. Recommend: next-round outliner give this slug a targeted push on evaluating k_C (centre-offset of ω vs Γ_C) OR pivot to finishing c·MX=b·NY by computing MX via the inscribed angle ∠AXK=∠ALK in ω together with Lemma Γ_C's grip on K.
- No dead ends introduced; all prior warnings (ρ(K)≠L, no 7-point concyclicity, MK≠LN) respected and re-confirmed.
