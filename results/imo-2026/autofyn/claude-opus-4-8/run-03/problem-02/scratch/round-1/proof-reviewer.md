# Proof review — imo-2026-02 (IMO 2026 P2), round 1

Three approaches judged independently. I reran the load-bearing sympy certificate
(`/tmp/clean.py`) and wrote my own independent numeric probes (`/tmp/indep.py`,
`/tmp/signgap.py`).

---

## 1. coordinate-identity — VERDICT: CHANGES REQUESTED (Status: partial; builder's `solved` is an OVERCLAIM)

**Scores.** Correctness of the algebraic engine: high. Completeness/rigor: fails at one
load-bearing step. Progress: large.

**What is CORRECT and independently verified:**
- (d) Reduction OM=ON ⟺ T=0. Elementary (equal-height ⇒ perpendicular bisector of MN is
  vertical; Cramer for O_x). Numerically confirmed 2·O_x = M_x+N_x exactly on the family.
- Decoupling: EA = u·FL with FL quadratic in v only, EB = v·FK with FK quadratic in u only.
  Correct algebraic factorisation (the positive ray-length factor pulls out).
- (c) The EXACT ideal identity **a_K·a_L·T = a_L·QK·FK + QL·FL** with pseudo-division
  remainder R2 = 0. I reran `/tmp/clean.py`: all three residuals print exactly `0`
  (`aK*aL*T-(aL*QK*FK+QL*FL)=0`, `aK*T-(QK*FK+R1)=0`, `aL*R1-(QL*FL+R2)=0`, `R2=0`). Genuine.
- Non-degeneracy a_K·a_L = −¼|AB|²|CA|²W² with W a single sinusoid whose cosθ-coefficient
  h(p+q)>0: correct; the finite-zero-set + continuity closure of a_K a_L=0 is fine.

**The load-bearing GAP (this is why it is NOT solved):**
The whole proof rests on the admissible configuration satisfying the **directed** equations
FK=0, FL=0 (i.e. EA=Im[…]=0, EB=Im[…]=0). But the problem gives only **unsigned** angle
equalities. Unsigned equality gives arg-ratio = ±(the angle); Im[…]=0 needs the **+** sign
(orientation ε=+1). The builder justifies ε=+1 by "the numerical model confirms the
directed — not merely unsigned — equality" plus a one-line continuity remark that even
cites the **wrong** collinearity ("collinearity of L,B,K" — the relevant degeneracy for
condition A is L,N,C collinear, i.e. ∠LNC=0).

I proved this step is genuinely load-bearing and NOT automatic. In `/tmp/signgap.py`, at
θ=0.8 for triangle (p,q,a,h)=(3,5,0.7,4) the UNSIGNED equations are satisfied to residual
4e-15, yet the DIRECTED quantity EB = −0.566 ≠ 0 and OM−ON = 0.28 ≠ 0. That configuration
has L OUTSIDE △BNC (interiority fails); it is excluded only by the interiority hypothesis.
So "unsigned hypotheses ⟹ FK=FL=0" is FALSE in general and holds only on the correctly-
oriented interior region. The proof does not establish that the admissible region is
correctly oriented — it asserts it numerically. Under the repo rigor rules ("no
hand-waving", "prove don't conjecture", numerics are not proof) this is a real gap.

**To close (bounded, standard):** prove from K∈int△BMC, L∈int△BNC and "K inside ∠LBA",
"L inside ∠ACK" that the directed angle from ray BK to ray BL and from ray NC to ray NL
have equal sign (and the σ-mirror), i.e. ε=+1, so EA=EB=0. My sweep confirms the theorem
and reduction are TRUE on the admissible set, so closing this one step yields a full solve.

---

## 2. pow-reduction-trig — VERDICT: CHANGES REQUESTED (Status: partial — builder's claim is accurate)

Lemma 1 (origin-at-A reduction): rigorous and correct (elementary; CERTIFIED to
`lemmas/reduction-OMeqON.md`). Lemma 2 (O·K=|K|²/2): correct. Lemma 3 sub-triangle
law-of-sines lengths and constraints (★),(★★): derivations are correct standard
law-of-sines in △BMK, △BKC (and σ-images). The reduction chain to (‡) is complete.

GAP-2 (the balance identity E(β)≡0) is genuinely still open — verified only numerically
(|E|≤1.4e-13 on three triangles), no from-scratch symbolic derivation. Not secretly
closed. Builder's `partial` is honest and accurate.

---

## 3. synthetic-sigma-spiral — VERDICT: CHANGES REQUESTED (Status: partial — builder's claim is accurate)

Step 1 (reduction OM=ON ⟺ pow(M,ω)=pow(N,ω) ⟺ c·MX=b·NY): rigorous (CERTIFIED as the
reduction lemma). Step 2 (spiral similarity ρ): rigorous (CERTIFIED to
`lemmas/spiral-similarity-rho.md`).

Steps 3–4 (concyclicities A,C,K,K′ and A,B,L,L′, K′=2M−K, L′=2N−N): the concyclicities are
TRUE — I verified numerically (`/tmp/indep.py`) that the 4-point determinant vanishes to
1e-9 across the admissible family on 4 triangles. The parallelogram structure and the
directed-angle addition chase are sound. HOWEVER the two pivotal directed-angle sign
equalities (∠(CL,CK)=∠(MB,MK) and ∠(CA,CL)=∠(KB,BA), each "mod π, correct sign") are again
justified by "[Verified numerically …]" — the SAME orientation gap as approach 1. So as
written the concyclicity proofs are not fully rigorous; the sign must be pinned from the
containment hypotheses. I therefore did NOT certify Γ_C, Γ_B at the full bar (they are true
and close to rigorous, but carry the sign gap). The crux (c·MX=b·NY via the radical-axis
coefficients k_C,k_B) is genuinely open. Builder's `partial` is accurate.

---

## Certified lemmas
- `lemmas/reduction-OMeqON.md` — the OM=ON reduction (pow-reduction Lemma 1 / synthetic
  Step 1). Elementary, unconditional, correct.
- `lemmas/spiral-similarity-rho.md` — spiral similarity ρ: B↦C, M↦N. Correct.

NOT certified: the concyclicities Γ_C, Γ_B (true but proofs lean on numerically-justified
directed-angle signs); coordinate-identity's "decoupling" lemma (the algebraic
factorisation EA=u·FL is fine, but the iff to the unsigned hypothesis carries the sign gap).

## Cross-cutting note for next round
Two of three approaches (coordinate-identity, synthetic-sigma-spiral) bottom out on the
SAME wall: converting unsigned angle hypotheses to correctly-oriented directed equalities
via interiority. That single orientation lemma, proved once, would complete
coordinate-identity outright (its algebraic engine is verified) and make the synthetic
concyclicities fully rigorous. Highest-leverage target for round 2.
