## imo-2026-03

Round-8 strategy. TWO concrete openings both explorers converged on close the two remaining
load-bearing gaps: (LB) the shared anchor crux T(ℓ)=GAP-A=G-INC-1=B2* by a *mutual* strong
induction; (UB) the residual gap case (p₁≤Σ/2) by an R3-cascade with the exact potential A=Σ−2p₁
and the identity D_b−2(2^b−1)=1. Verified this round (bounded, budget-enforced): D_b−2(2^b−1)=1 for
b=1..7 (exact); m=3 gap potential A=Σ−2p₁<Σ/D_b, 0 violations / 2539 gap configs. Field = 3 advances
(no new slug warranted — the population already spans both bounds by rival routes; the highest-value
move is to cash the two openings, not dilute builder slots). The two stuck approaches
(alternating-sum-value, extremal-smoothing) stay live but are NOT nominated this round (S1 route
de-prioritized by both explorers; slots better spent on the converging routes).

---

ll-inclusion-gap: advance
Target: The problem's full claim c(n)=2^n/(2^{n+1}−1); this slug owns the LOWER bound via the
  containment/non-containment split, and this round closes the shared anchor crux for ALL n.
Technique: Extend the existing certified two-step strong induction n→n−2 (Steps 10–13) from a
  single-claim induction on Claim(n,ε) into a SIMULTANEOUS MUTUAL induction on the PAIR
  {Claim(n,ε), T(n)}, closing residual lemma T(ℓ) for all ℓ. Same engine (SET IDENTITY
  `S_{G_{n−1}}∩[0,2^{n−2})=S_{G_{n−3}}` + ΣQ-free top-band decomposition), same base cases.
Skeleton (this round's build target — the T(n) inductive step + h=0 write-ups):
  1. Restate T(n): for INC P (S_P⊆S_{G_{n−1}}), |P|≤n+1, ΣP∈(2^n−1,2^n), prove O_P≤O_{G_{n−1}};
     equivalently deficit_top+M ≥ 1−τ with τ=2^n−ΣP∈(0,1) — by the certified top-band decomposition.
  2. h≥4 IMPOSSIBLE for T(n): four parts each ≥2^{n−2} sum to ≥4·2^{n−2}=2^n>ΣP — arithmetic
     contradiction (ΣP<2^n). So only h∈{0,2} occur in T(n) — one line.
  3. h=0 case (T and Claim both): all parts <2^{n−2} ⟹ S_P∩I_{n−1}=∅ ⟹ δ_top=0 ⟹
     deficit_top=2^{n−2}≥1≥1−τ (resp. ≥1−ε for Claim). Fills BOTH the flagged unwritten Claim h=0
     sub-case (reachable n≥5) and T's h=0 — one line each.
  4. h=2 case: q₁≥q₂ the two parts ≥2^{n−2}; a=2^{n−1}−q₁≥0, b=q₂−2^{n−2}≥0, deficit_top=a+b,
     ε'=a−b−τ, ΣP_lo=2^{n−2}+ε'. Sub-case 2a (a+b≥1−τ): done. 2b-i (ε'≥0, so ε'<1): apply
     Claim(n−2,ε') [IH, ε'∈[0,1)], M≥1−ε', total ≥ (a+b)+(1−ε')=1+2b+τ≥1−τ. 2b-ii (ε'∈(−1,0)):
     apply T(n−2) [IH], M≥1+ε', total ≥ (a+b)+(1+ε')=1+2a−τ≥1−τ.
  5. The critical bound ε'>−1 in 2b-ii: from the 2b hypothesis a+b<1−τ and a≥0, b<1−τ, so
     ε'=a−b−τ > −b−τ > −(1−τ)−τ = −1. Hence ΣP_lo∈(2^{n−2}−1,2^{n−2}) — exactly T(n−2)'s window.
     NEVER invoke Claim with ε<0 (certified FALSE); 2b-ii uses T, not Claim.
  6. Step-13 accounting: bases Claim(1,·),Claim(2,·),T(1),T(2) proved (Step 11). Mutual strong
     induction: each level-n step invokes only level-(n−2) claims. ⟹ Claim(n,ε) AND T(n) for all n
     ⟹ G-INC-1=Claim(n,0) unconditionally for ALL n (anchor R=G_{n−1}).
  7. (Secondary, if builder has room) G-INC-2 (refined R, first nontrivial n=4): induction on the
     number of extra XY cuts c_R. Base c_R=0 = G-INC-1 (now closed all n). Step: cutting R₀-piece p
     into {p₁,p₂} flips S_R by ([0,p₂)∪[p₁,p)); split on whether S_Q meets the flipped region
     (Case A: S_Q⊆S_{R₀}, apply IH; Case B: S_Q meets flip, budget c_Q≤n−1 ⟹ |Q|≤n gives a direct
     symdiff-mass bound).
Key lemmas (claim + mechanism):
  - T(n) closes G-INC-1 for all n — because T is the exact ε<0 companion that sub-case 2b-ii of
    Claim needs, and h≥4 cannot occur in T (ΣP<2^n) so T's step is strictly simpler than Claim's;
    the mutual IH {Claim(n−2),T(n−2)} closes both simultaneously.
  - ε'>−1 in 2b-ii — because the 2b hypothesis a+b<1−τ with a,b≥0 forces b<1−τ, and ε'=a−b−τ.
  - h=0 ⟹ deficit_top=2^{n−2}≥1 — because no part reaches band I_{n−1}, so the whole top band is a
    deficit; trivially ≥1≥1−τ.
Open gaps after this round: G-INC-2 (refined R, general n — the c_R induction is a *plan*, not yet
  built) and G-GAP (this slug's non-containment branch, largely untouched — ll-dyadic-symdiff is the
  rival route that covers non-containment natively).
Cases to cover: h∈{0,2} for T(n) (h≥4 impossible); within h=2: 2a, 2b-i, 2b-ii. h=0 write-up for
  Claim(n,ε) too. Base cases T(1),T(2),Claim(1,·),Claim(2,·) already certified — cite, don't reprove.
Watch out for: (i) do NOT strengthen Claim to ε<0 in 2b-ii — that path is certified FALSE
  (Q_lo={1.9,1.5}); 2b-ii must call T(n−2). (ii) The mutual induction's dependency chain must be
  stated (T(3)←T(1),Claim(1); T(4)←T(2),Claim(2); T(5)←T(3),Claim(3); …) so strong induction is
  visibly well-founded. (iii) Keep the JOINT CUT BUDGET |P|≤n+1 in every numeric spot-check
  (unbudgeted grids fabricate spurious violations). (iv) G-INC-2 is genuinely separate — it is NOT
  inherited from the anchor (tight case R={4,4,4,2,1},Q={5,5,4,2} has S_Q=[2,4)⊄S_{G₃}); don't claim
  it for free.

---

geometric-selfsimilar: advance
Target: The problem's full claim c(n)=2^n/(2^{n+1}−1); this slug owns the UPPER bound, and this round
  closes the sole remaining upper-bound residual (the gap case, distinct X, p₁≤Σ/2) for all m.
Technique: An actual-A potential via an R3-cascade XY strategy (NOT an SB-monotone reduction — that is
  certified-dead). XY repeatedly cuts the current largest piece at the next piece's length (a
  parity-invisible pair), tracking A(final)=Σ−2p₁; the exact identity D_b−2(2^b−1)=1 turns the gap
  condition into A<Σ/D_b. Base m=3 (one cut), induction on m for m≥4.
Skeleton:
  1. Base m=3, gap case (distinct p₁>p₂>p₃, p₁≤Σ/2, at any budget b≥2, m=3≤b+1 by budget invariant):
     XY cuts p₁ at offset p₂ → invisible pair {p₂,p₂}, effective pieces {p₁−p₂, p₃}. Since p₁≤Σ/2:
     p₃=Σ−p₁−p₂ ≥ Σ/2−p₂ ≥ p₁−p₂, so p₃ is the larger effective piece and A(final)=p₃−(p₁−p₂)=Σ−2p₁.
  2. Gap condition p₂+p₃<τ=Σ·2^b/D_b ⟹ p₁=Σ−p₂−p₃>Σ−τ=Σ(2^b−1)/D_b. Hence
     A=Σ−2p₁<Σ−2Σ(2^b−1)/D_b=Σ·[D_b−2(2^b−1)]/D_b=Σ/D_b, using the identity D_b−2(2^b−1)=1 (verified
     b=1..7 exact). ⟹ (SB) μ(X,b)≤Σ/D_b strictly. Base CLOSED, 1 cut used.
  3. Induction on m (m≥4, budget b≥m−1): apply ONE R3 step to the gap-case largest piece → effective
     X' with m−1 pieces at budget b−1. Carry the potential A(final)≤Σ−2p₁_orig throughout.
     - Case A (p₁−p₂≥p₃, p₁'=p₁−p₂): sub-instance satisfies p₁'=p₁−p₂ ≤ Σ/2−p₂ = (Σ−2p₂)/2 = Σ'/2,
       so p₁'≤Σ'/2 persists (proved algebraically). Recurse.
     - Case B (p₃>p₁−p₂, p₁'=p₃): effective largest p₃<p₂<τ/2; two R3 steps give
       A=(Σ−2p₂)−2p₃=Σ−2(p₂+p₃)≤Σ−2p₁ (since p₂+p₃>p₁ in Case B), strictly smaller than the Case-A
       bound — the cascade over-cancels, making Case B easier.
  4. In every branch A(final)≤Σ−2p₁_orig<Σ/D_b (step 2's inequality is on the ORIGINAL Σ,p₁,b).
     Budget: m−1 cuts ≤ b by the |X|≤b+1 invariant. ⟹ (SB) for the whole gap case, all m.
  5. Assemble: with Regime A (shadow), B1 (partial-shadow), B at n=2, R1/R2/R3 reductions, Case A.A
     (p₁>Σ/2, certified) already closing every non-gap branch, this closes the LAST upper-bound gap
     ⟹ full upper bound μ(X,b)≤Σ/D_b for all LB configs ⟹ V≤c(n).
Key lemmas (claim + mechanism):
  - m=3 gap ⟹ A=Σ−2p₁<Σ/D_b — because one parity-invisible cut leaves the single leftover Σ−2p₁,
    and the gap bound p₁>Σ(2^b−1)/D_b plus the exact identity D_b−2(2^b−1)=1 collapse it to Σ/D_b.
  - The R3 cascade preserves p₁'≤Σ'/2 (Case A) — because p₁≤Σ/2 ⟹ p₁−p₂≤(Σ−2p₂)/2=Σ'/2; and Case B
    strictly lowers A below the Case-A value, so the potential Σ−2p₁ dominates in both.
Open gaps after this round: Case B's persistence of the gap/sub-threshold hypotheses across the
  cascade needs a fully rigorous invariant (the explorer verified 102 configs / 0 violations but flags
  Case B "may need sub-casework") — this is the one non-trivial step for the builder to nail.
Cases to cover: m=3 base; m≥4 step Case A (p₁−p₂≥p₃) and Case B (p₃>p₁−p₂); confirm budget m−1≤b at
  every level; confirm distinctness is not needed for the bound (equal pieces only help via R1).
Watch out for: (i) do NOT reach for SB-monotone / partial-shadow chaining — certified DEAD
  (sb-obstruction: gap-case steps break the SB invariant); the whole point is that A=Σ−2p₁ is an
  ACTUAL-A potential, not an Σ-based one. (ii) Verify the effective-piece ordering (which piece is
  larger after the cut) in Case A vs B — the sign of A depends on it. (iii) Enforce the budget
  invariant m≤b+1 so m−1 cuts are legal. (iv) Keep every numeric check budget-enforced and <20s.

---

ll-dyadic-symdiff: advance
Target: The problem's full claim c(n)=2^n/(2^{n+1}−1); this slug owns the LOWER bound via the direct
  measure(S_Q△S_R)≥1 route (native non-containment), and this round pushes the REFINED-R branch that
  the anchor T(ℓ) does not cover.
Technique: Reuse the general (anchor-independent) Cases 1/2/Sub-3a — which bound measure(S_Q△S_R)≥1
  for ANY R with max(R)≤2^{n−1}, using no G_{n−1}-specific structure — and attack the residual
  refined-R Sub-3b with the budget reduction c_R≥1 ⟹ c_Q≤n−1 ⟹ |Q|≤n.
Skeleton:
  1. Note that once T(ℓ) closes for all n (ll-inclusion-gap this round), the ANCHOR B2*=GAP-A residual
     is closed; the remaining lower-bound work for a complete proof is REFINED R (R a proper
     refinement of G_{n−1}, i.e. XY cuts more finely). This slug covers it via measure symdiff.
  2. Case 1 (max(Q)≥2^{n−1}+1): certified ll-case1-high-interval — S_Q covers [2^{n−1},max(Q))
     disjoint from S_R⊆[0,2^{n−1}); measure ≥1. Holds for ANY R. Import.
  3. Case 2 (odd piece count, all pieces ≥1): certified dyadic-level-parity / Lemma P; A≥1. Any R.
  4. Sub-3a (some full dyadic level fully odd in S_Q△S_R): certified. Any R.
  5. Sub-3b refined R (residual, no fully-odd level, max(Q)≤2^{n−1}): use the budget reduction. With
     c_R≥1 extra R-cuts, XY spent cuts refining, so |Q|≤n (not n+1) — push more configs into Sub-3a,
     and handle the tight residual via the double-REFL formula A(Q∪R)=max(Q)−q₁+A(Q'∪R') adapted to
     the refined R's own band structure (REFL-gen relaxes the hypothesis to max(R)≤μ=max(Q), already
     certified — it does NOT require R=G_{n−1}).
Key lemmas (claim + mechanism):
  - Cases 1/2/Sub-3a are R-agnostic — because each bounds measure(S_Q△S_R) using only S_Q's structure
    (a high interval, an odd count, a fully-odd dyadic level) and the containment S_R⊆[0,2^{n−1}),
    never the specific bands of G_{n−1}.
  - Budget reduction |Q|≤n for refined R — because the JOINT cut budget #Q+#R≤n and c_R≥1 leave
    ≤n−1 Q-cuts, hence ≤n Q-pieces; fewer pieces make the fully-odd-level (Sub-3a) pigeonhole easier.
Open gaps after this round: the tight refined-R Sub-3b instances where even the reduced budget leaves
  no fully-odd level — these need the refined-R adaptation of double-REFL and are the honest residual.
Cases to cover: max(Q)≥2^{n−1}+1 (Case 1); odd count (Case 2); fully-odd level (Sub-3a); residual
  Sub-3b refined R. Confirm exhaustiveness (no orphaned band) as in the anchor proof.
Watch out for: (i) do NOT re-import the false "max(Q)<2^{n−1}⟹A≥2" step (B3 is tight at A=1,
  Q={3,3,2},R={2,2,2,1}). (ii) The SET IDENTITY and top-band decomposition are G_{n−1}-specific — do
  NOT assume a refined-R analogue exists (explorer confirms none is known). (iii) Enforce the joint
  cut budget in every numeric check. (iv) This slug and ll-inclusion-gap are RIVAL complete LB
  attempts (measure-symdiff vs inclusion split), not two halves of one proof — do not merge them.

---

Field summary for the reviewer: 3 advances, no new slug.
  - ll-inclusion-gap (advance): CLOSE T(ℓ) for all n by mutual {Claim,T} induction + h=0 write-ups
    ⟹ G-INC-1 anchor for ALL n; secondary G-INC-2 c_R-induction. Biggest single win (kills the shared
    LB anchor crux). Highest priority.
  - geometric-selfsimilar (advance): CLOSE the upper-bound residual gap case (p₁≤Σ/2) via the R3
    cascade actual-A potential A=Σ−2p₁ + the identity D_b−2(2^b−1)=1; m=3 base + induction on m.
    Second-highest priority (last upper-bound gap).
  - ll-dyadic-symdiff (advance): push REFINED-R (Cases 1/2/3a general + budget reduction) — the LB
    completeness piece the anchor T(ℓ) leaves open.
Not nominated (stay live, not built): alternating-sum-value, extremal-smoothing (S1 route
  de-prioritized by both explorers; builder slots reserved for the converging routes).
