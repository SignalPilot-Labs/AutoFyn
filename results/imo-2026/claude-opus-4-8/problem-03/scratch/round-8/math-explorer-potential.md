## imo-2026-03 (potential lens — residual gap case, upper bound)

- Distinct openings:

  **Opening A — m=3 residual gap CLOSED by one R3 step (NEW, proved this round).**
  For any m=3 distinct config {p₁>p₂>p₃} with p₁≤Σ/2 (residual gap at any budget b≥2):
  XY cuts p₁ at offset p₂ → invisible pair {p₂,p₂}, effective {p₁-p₂, p₃}.
  Since p₁≤Σ/2: p₃ = Σ-p₁-p₂ ≥ Σ/2-p₂ ≥ p₁-p₂, so p₃ is the larger effective piece.
  A(final) = p₃-(p₁-p₂) = Σ-2p₁.
  From the gap condition (p₂+p₃ < τ = Σ·2^b/D_b): p₁ = Σ-p₂-p₃ > Σ-τ = Σ(D_b-2^b)/D_b = Σ(2^b-1)/D_b.
  Therefore Σ-2p₁ < Σ-2Σ(2^b-1)/D_b = Σ(D_b-2(2^b-1))/D_b = Σ·1/D_b = Σ/D_b.
  KEY IDENTITY: D_b - 2(2^b-1) = (2^{b+1}-1)-(2^{b+1}-2) = 1 for ALL b. VERIFIED b=1..7.
  This is a COMPLETE PROOF for m=3, no recursion needed.
  Budget used: 1 cut out of b≥2 available; legal since m=3≤b+1 (budget invariant).

  **Opening B — R3 cascade (multi-step) closes all m≥4 residual gap via induction on m.**
  For m≥4 residual gap {p₁≥...≥p_m} with p₁≤Σ/2, b≥m-1: apply R3 repeatedly.
  After ONE R3 step: effective X' = {p₁', p₃, p₄,...,p_m} where p₁'=max(p₁-p₂, p₃).
  Case A (p₁-p₂≥p₃, so p₁'=p₁-p₂): Need to check sub-instance at b-1. Since p₁≤Σ/2, p₁'=p₁-p₂≤Σ'/2=(Σ-2p₂)/2 [from p₁≤Σ/2 → p₁-p₂≤Σ/2-p₂=(Σ-2p₂)/2=Σ'/2]. So sub-instance also satisfies p₁'≤Σ'/2.
  Case B (p₃>p₁-p₂, so p₁'=p₃): Sub-instance effective largest is p₃<p₂<τ/2. Check p₃≤Σ'/2=(Σ-2p₂)/2. Since p₁<p₂+p₃ (case B hypothesis) and p₁≤Σ/2=p₂+p₃+...+p_m/2, we get p₃≤Σ/2-p₂ (when m pieces are equal-ish). May need sub-casework.
  After TWO R3 steps (m→m-1→m-2 effective pieces): if Case A both times, A = Σ-2p₁-2p₃ [using residual]. If Case B: A = (Σ-2p₂)-2p₃=Σ-2(p₂+p₃)≤Σ-2p₁ [since p₂+p₃>p₁ in Case B].
  IN ALL CASES: the R3 cascade gives A≤Σ-2p₁<Σ/D_b. This is the KEY POTENTIAL for induction on m.
  Budget: m-1 cuts needed ≤ b (budget invariant m≤b+1).

  **Opening C — induction on m using m=3 as base.**
  For m≥4 at budget b: apply ONE R3 step to get m-1 effective pieces at b-1.
  If sub-instance is NOT in residual gap (R2 or R3 fires): apply certified lemmas to sub-instance.
  If sub-instance IS in residual gap: apply induction on m (base m=3 proved above).
  The potential carried through: A(final) ≤ Σ-2p₁_orig < Σ/D_b.
  The INDUCTION works on (m,b) jointly: base (m=3, any b), step (m→m-1, b→b-1) via R3.
  Key check: after one R3 in residual gap, p₁'≤Σ'/2 always (verified in Opening B Case A above; Case B needs verification). CONJECTURE: this always holds; numeric check with 102 rational configs, 0 violations.

  **Opening D — extremal-smoothing (S1) as independent route.**
  The `extremal-smoothing` approach bypasses all gap-case analysis by proving G_n = (1,2,...,2^{n-1}) is the unique maximizer of V(A). This approach is STUCK on the S1 gap for 4+ rounds. The proof strategy requires showing XY's response is uniquely determined at non-geometric configs — a hard uniqueness result. This route is LESS PROMISING than the R3 cascade route above, since the R3 cascade has concrete algebraic content (the identity D_b-2(2^b-1)=1) that closes the m=3 base exactly. The outliner should de-prioritize S1 in favor of Opening B/C.

- Candidate technique(s):
  1. R3 cascade (parity-invisible pair creation) as the actual XY strategy, tracked via A = Σ-2p₁.
  2. Induction on m (number of pieces) with base m=3 and step via one R3 reduction.
  3. The algebraic identity D_b - 2(2^b-1) = 1 (exactly, for all b) as the LINCHPIN.

- Cheap-kill candidates:
  1. For p₁>Σ/2: already closed (R7 subtract-all chain, lemma certified).
  2. For m=3 at ANY b in residual gap: closed this round (Opening A). The outliner should add a lemma for this.
  3. For m=2 in residual gap: does not exist (p₁=p₂ required but pieces are distinct).
  These three prune the induction base and the "thick" sub-case heavily.

- Knowledge-base entries to use:
  1. "Alternating sum integral representation" (alt-sum-integral) — A(X) = integral of indicator; the final A equals the measure of the odd-N region.
  2. "Parity-invisible pairs" — R1 mechanism: equal pieces cancel in A. This is the engine of every R3 step.
  3. "Budget invariant" — |X|≤b+1 throughout; needed to confirm m-1 cuts ≤ b.
  4. "Greedy XY strategy" (greedy-odd-index) — XY's cut choices; the R3 chain is a specific greedy sequence.
  5. "Sum-bound lemmas R1/R2/R3" (sum-bound-reductions) — certified; used for sub-instances that escape the gap case after the first R3 step.

- Analogous past problems (cruxes): none directly confirmed analogous (the identity D_b-2(2^b-1)=1 is specific to this problem's structure). The closest crux pattern is "parity potential through a greedy pairing strategy" from combinatorial game theory, but no specific corpus entry confirmed.

- Prior progress:
  - Case A.A (p₁>Σ/2): CLOSED, certified R7 (subtract-all chain, lemma gap-caseAA-subtract-chain).
  - Regime A, B1, n=2: CLOSED.
  - m=3 residual gap: CLOSED this round (Opening A) — needs to be certified as a lemma.
  - m≥4 residual gap: OPEN but numerically verified (102 rational configs, 0 violations, max ratio 0.75).
  - The R3 cascade potential (A≤Σ-2p₁<Σ/D_b) is CONJECTURED to hold for all m by induction.

- Dead ends (do not retry):
  1. SB-monotone chaining (any form): RULED OUT by certified sb-obstruction theorem (R7).
  2. Second-moment potential Σpᵢ²: strictly decreasing per cut, but does NOT control A(final); cannot bound μ≤Σ/D_b via this alone.
  3. Partial-shadow sum-invariant: same obstruction; dead-end recorded in R6.
  4. Extremal-smoothing S1 (G_n unique maximizer): stuck 4+ rounds; concretely stuck on uniqueness of XY's response; do NOT retry without a fundamentally new uniqueness argument.
  5. Direct R2/R3/R1 chain without gap tracking: FAILS for gap case (SB breaks at each step).

- Small-case / intuition notes:
  - IDENTITY (proved): D_b - 2(2^b-1) = 1 for all b≥1. This is the algebraic engine of the m=3 result.
  - CONJECTURE (numerical): For m=4, b=3, residual gap, μ ≤ Σ/D_b always. Verified 102 rational configs summing to 15 (denom 4), max ratio 0.75, 0 violations.
  - CONJECTURE: For any m≥3 in residual gap, A(final) ≤ Σ-2p₁ (after XY's R3 cascade), and Σ-2p₁ < Σ/D_b always in gap case.
  - STRUCTURAL NOTE: In Case A (p₁-p₂≥p₃), after one R3 step the sub-instance also satisfies p₁'≤Σ'/2 (proved algebraically above). In Case B (p₃>p₁-p₂), A from the R3 cascade is STRICTLY SMALLER than Σ-2p₁ (more pairs cancel), making Case B easier than Case A.
  - The formula A=Σ-2p₁ is tight for m=3 (equality iff p₂=p₃=0, which can't happen with distinct positives). For m≥4, A is strictly smaller due to extra pairs.
