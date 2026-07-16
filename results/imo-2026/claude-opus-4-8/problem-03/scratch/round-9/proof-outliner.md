## imo-2026-03

Answer (fixed, verified): c(n) = 2^n/(2^{n+1}−1). Do NOT re-derive. The LB anchor crux
(T(ℓ)=G-INC-1=GAP-A=B2*, R=G_{n−1}) is PROVEN UNCONDITIONALLY for all n (certified
`t-ell-mutual-induction`) — DO NOT re-open or re-push it. Each residual below is one of three
well-isolated open pieces; the run is close. Field = advance the three live residual routes, plus one
new convergence slug that unifies the two refined-R LB residuals onto a single target.

Global anti-stuck for every builder: bounded (<20s) python with incremental prints only if needed;
ALWAYS enforce the JOINT CUT BUDGET (#Q-cuts + #R-cuts ≤ n, resp. |X| ≤ b+1) in every numeric check —
unbudgeted grids fabricate spurious violations. Time-box, emit steadily.

---

ll-inclusion-gap: advance
Target: c(n)=2^n/(2^{n+1}−1) — full LB (Lemma LL, t≥2) via the inclusion split S_Q⊆S_R, with anchor
INC branch already closed (G-INC-1 all n). This round: close **G-INC-2** (refined R, first nontrivial
n=4), the refined-R INC branch, so the whole INC branch of LL is unconditional.
Technique: the explorer's structural split of the extra cut into flipped intervals F=F_lo∪F_hi, with a
clean n→n−2 top-band induction where h is even and a direct case analysis where h is odd (equal split).
Skeleton (G-INC-2: R = G_{n−1} with c_R≥1 extra cuts, S_Q⊆S_R, ΣQ=2^n, |Q|≤n ⟹ A(Q)≤A(R)−1):
  1. Cheap kill — cuts that do not decrease A: if the extra cut has f+ ≥ f− (so A(R) ≥ A(G_{n−1})) and
     the flip stays inside S_{G_{n−1}} (S_R ⊆ S_{G_{n−1}}, i.e. f+ = 0), then S_Q ⊆ S_R ⊆ S_{G_{n−1}}
     and certified G-INC-1 gives A(Q) ≤ A(G_{n−1})−1 ≤ A(R)−1. — by G-INC-1 (`t-ell-mutual-induction`).
     Builder: verify the exact side condition; this removes all "increasing-A / non-decreasing" cuts.
  2. Lower-band cut (cut of piece 2^{k_0}, k_0 ≤ n−3): top-band decomposition with A(R) in place of
     A(G_{n−1}) (S_R∩[2^{n−2},2^{n−1}) = full band, so deficit_top unchanged ≥0; h even by
     Parity-Condition since N_R(2^{n−2}−0)=2): A(R)−A(Q) = deficit_top + [A(R_lo)−A(Q_lo)] ≥ 0 + 1,
     the bracket ≥1 by G-INC-2 at level n−2 (R_lo = G_{n−3} with the same lower-band cut, S_{Q_lo}⊆S_{R_lo}).
     — by `top-band-decomposition` + strong induction n→n−2. Bases n=2 (Forcing ⟹ Q={2,2}, A=0) and
     n=4 (direct). NO T-companion needed here (unlike the anchor).
  3. Equal-split top cut (a=2^{n−2}, so R={2^{n−2},2^{n−2}} ∪ G_{n−3}, A(R)=A(G_{n−2}), N_R(2^{n−2}−0)=3
     ODD ⟹ h may be odd, Parity-Condition does NOT fire): direct case analysis. Q-parts in
     (2^{n−2},2^{n−1}) occur in equal pairs {s,s} (even multiplicity, from N_R(x)=0 even for x∈(2^{n−2},2^{n−1}))
     contributing 0 to A; remaining parts ≤2^{n−2} give A(Q)=p_1−p_2 = width of the single forbidden band
     of G_{n−1} that S_{Q-remaining} lies in. — by Parity-Condition + arithmetic. Key: p_1−p_2 ≤
     max forbidden-band width ≤ 2^{n−3} ≤ A(G_{n−2})−1 = A(R)−1 (since A(G_{n−2})=(2^{n−1}+(−1)^{n−2})/3 ≥
     2^{n−3}+1 for n≥4).
  4. Non-equal top cut (a∈(0,2^{n−2}), h even): modified decomposition A(R)−A(Q) =
     (2^{n−2}−a−δ_top) + [A(R_lo)−A(Q_lo)] ≥ 0 + 1, R_lo = G_{n−3} △ [0,a). — subdivide on a≥1 (flip is a
     genuine sub-interval, R_lo a lower-level refinement, use G-INC-2 at n−2) vs a<1 (flip inside the
     bottom piece; careful separate sub-case). The f+ ≥ f− part of this is already killed in step 1.
Key lemmas (claim + mechanism):
  - G-INC-2 lower-band descent — because with h even the top band is untouched, deficit_top ≥ 0, and the
    lower half is a strictly smaller refined-R INC instance, so n→n−2 closes with NO T-companion.
  - Equal-split spread bound — because parts above 2^{n−2} cancel in pairs, and the INC constraint pins
    the residual spread into one forbidden band of width ≤ 2^{n−3} ≤ A(G_{n−2})−1.
Open gaps: step 3 general-n arithmetic "max forbidden-band width ≤ A(G_{n−2})−1"; step 4 a<1 sub-case;
G-GAP (non-containment, refined R) is still separate — covered by ll-dyadic-symdiff's bucket (iii) below.
Cases to cover: lower-band cut (k_0≤n−3); equal-split top cut (a=2^{n−2}); non-equal top cut (a<2^{n−2}),
sub-split a≥1 vs a<1; plus the f+≥f− cheap-kill.
Watch out for: h is NOT always even (equal-split gives h=3 odd — verified Q={5,5,4,2}, R={4,4,4,2,1}),
so step 3 must NOT invoke Parity-Condition at the 2^{n−2} threshold; max(Q) ≤ max(R) is FALSE (tight case
has max(Q)=5>max(R)=4 — use Forcing max(Q)≤2^{n−1} only); NO SET IDENTITY analogue for refined R.

---

ll-dyadic-symdiff: advance
Target: c(n)=2^n/(2^{n+1}−1) — full LB (Lemma LL, t≥2) via direct measure(S_Q△S_R)≥1, R-agnostic core
(Cases 1/2/Sub-3a) already closed for any R. This round: close **bucket (iii)** = top-CUT refined R
(max(Q)<2^{n−1} AND max(R)<2^{n−1}), plus the shared **(B2*)-ref** target.
Technique: disjoint cheap-kill + double-REFL telescoping (alternately reflect at max(Q), max(R)) that
cancels both maxima and reduces bucket (iii) to a smaller (B2*)-ref-type object (explorer Openings A/C/D,
verified on a concrete n=3 instance).
Skeleton:
  1. Cheap kill — disjoint sub-case: if S_Q∩S_R=∅ then A = A(Q)+A(R) ≥ A(R) ≥ 1. — by
     measure(S_Q△S_R)=A(Q)+A(R) when disjoint (certifiable immediately; covers the near-tight limit,
     9/42 n=3 configs).
  2. Double-REFL telescoping: with M_Q=max(Q), M_R=max(R), apply REFL-gen (`ll-reflection-identity-gen`,
     needs only max(R)≤max reflected piece) alternately: remove M_Q then M_R (or vice versa), giving
     A(Q∪R) = M_Q − M_R + A(Q'∪R''), valid when M_Q≥M_R≥max(Q'). — by two applications of REFL-gen.
     Sub-split: M_Q ≫ M_R (RHS < 1, slack — closes directly) vs M_Q ≈ M_R (both ≈2^{n−1}−ε, reduces to
     A(Q'∪R'') ≥ 1, a smaller refined system = (B2*)-ref target).
  3. (B2*)-ref: A(Q'∪R') ≥ 1 for R' refining G_{n−2} with top piece uncut — the refined-R alternating-tail.
     Prove by iterating the double-REFL reduction with a termination argument (pieces exhaust / become
     integer-aligned), bottoming out on the certified R-agnostic Cases 1/2/Sub-3a or the disjoint kill.
     — by REFL telescoping + well-founded descent on Σ of the reflected system.
  4. n=3 base (bucket iii): |Q|=3 odd ⟹ S_Q⊇[0,ε); |R|=4 even ⟹ S_R⊉[0,ε); so S_Q⊄S_R structurally
     (parity of piece counts), the INC formula is inapplicable — direct casework on |Q|=3,|R|=4, ΣP=15,
     min A=3/2. — by piece-count parity at x=0+ (`dyadic-level-parity` style) + exhaustive casework.
Key lemmas (claim + mechanism):
  - Double-REFL cancellation — because reflecting at max(Q) then max(R) (REFL-gen, relaxed hyp
    max(R)≤μ) produces A(Q∪R)=M_Q−M_R+A(Q'∪R''); when M_Q≈M_R the ±cancel and the target survives as a
    strictly smaller refined system (verified: Q=[15/4,13/4,1], R=[15/4,2,1,1/4] chains to A(Q'∪R'')=3/2).
  - (B2*)-ref termination — because each REFL step strictly reduces Σ of the reflected multiset, so the
    telescoping halts at a certified R-agnostic case or the disjoint kill.
Open gaps: (B2*)-ref general n (termination of the REFL telescoping is the load-bearing step); the
M_Q≈M_R tight sub-case of step 2 depends on step 3.
Cases to cover: disjoint; M_Q≫M_R (slack); M_Q≈M_R (→(B2*)-ref); the three n≥4 budget splits
(c_Q,c_R)∈{(2,1),(2,2),(3,1)}; the (c_Q=2,c_R=1) sub-case where S_Q⊆S_R IS possible (overlaps G-INC-2).
Watch out for: "max(Q)<2^{n−1} ⟹ A≥2" is FALSE (tight A=3/2); direct REFL-gen without follow-up only
reduces to the GAP-A crux and does NOT close by itself; NO SET IDENTITY for refined R; the ∫(N_Q−N_R)=1
integral bound is provably insufficient. Termination of the telescoping is NOT automatic — prove it.

---

geometric-selfsimilar: advance
Target: c(n)=2^n/(2^{n+1}−1) — full UPPER bound (leader). Anchor UB pieces (Regimes A/B1, sum-bound
reframe, m≤3 gap case) all certified. This round: close the **m≥4 gap case** (distinct X, m=|X|≥4,
p₁≤Σ/2, p₂<τ/2, budget b, |X|≤b+1), the whole remaining upper bound.
Technique: one-step lookahead **complement cut** — XY cuts p₁ at offset p₁−pⱼ (NOT pⱼ), creating an
invisible pair {pⱼ,pⱼ}; this reduces m=4 to m=3 at budget b−1, closed by the certified Lemma R4. The
deterministic R3-cascade (cut at pⱼ) is REFUTED (creates a triple pⱼ, odd parity) — must use p₁−pⱼ.
Skeleton:
  1. Setup: gap case, choose j∈{2,3,4}. XY cuts p₁ at p₁−pⱼ → pieces (pⱼ, p₁−pⱼ); with existing pⱼ this
     is a pair {pⱼ,pⱼ} (parity-invisible, cancels in A). — by the alternating-sum pair cancellation
     (`sum-bound-reductions` R1). Sub-instance sub = X\{p₁,pⱼ} ∪ {p₁−pⱼ}, m=3, budget b−1, Σ'=Σ−2pⱼ.
  2. max(sub) ≤ Σ'/2: p₁−pⱼ ≤ p₁−pⱼ and p₁≤Σ/2 ⟹ p₁−pⱼ ≤ (Σ−2pⱼ)/2 = Σ'/2, so Case A.A never applies
     to sub — sub is a genuine m=3 case. — by p₁≤Σ/2 arithmetic.
  3. Apply certified Lemma R4 (`gap-case-m3-closure`) to sub when it is a gap case: A(sub-final) = Σ'−2·max(sub),
     explicit. When sub is NOT a gap case (pⱼ small ⟹ Σ'≈Σ ⟹ p₂≥τ'/2), R3 applies to sub directly, then
     Case A.A / 2-piece closes. — by R4 / R3 (`sum-bound-reductions`).
  4. Bound A(final) < Σ/D_b using gap conditions, per sub-case:
     - complement p₂, Case α (p₁−p₂≥p₃): A=Σ−2p₁, need p₁>Σ(D_b−1)/(2D_b) i.e. p₄<Σ/(2D_b).
     - complement p₂, Case β (p₁<p₂+p₃): A=Σ−2p₂−2p₃, need p₂+p₃>Σ(D_b−1)/(2D_b).
     - complement p₄, sub-not-gap: R3-then-close, A small (verified 0/small on near-equal APs).
  5. Conclude: min over j∈{2,3,4} gives a valid XY strategy ⟹ μ(X,b) ≤ Σ/D_b. (Fallback: averaging —
     Σ_j A(j) < 3Σ/D_b ⟹ min_j < Σ/D_b, bypassing per-case algebra.)
Key lemmas (claim + mechanism):
  - Complement-cut parity — because cutting p₁ at p₁−pⱼ (not pⱼ) makes exactly TWO copies of pⱼ, an
    invisible pair, whereas cutting at pⱼ makes THREE (odd, uncancelled) — this single bit of lookahead
    is why optimal μ obeys the bound while the deterministic cascade fails.
  - m=4 → m=3 descent — because after the pair forms, sub has exactly 3 pieces, max ≤ Σ'/2, budget b−1,
    so the certified Lemma R4 gives the exact A formula; the gap conditions then force A < Σ/D_b.
Open gaps: the algebraic bounds in step 4 (Sub-targets 1/2/3: p₄<Σ/(2D_b) in Case α; p₂+p₃>Σ(D_b−1)/(2D_b)
in Case β; the sub-not-gap regime); proving that at least one j∈{2,3,4} always lands < Σ/D_b (min_j, or
the averaging bound).
Cases to cover: for each j∈{2,3,4}: Case α vs Case β; sub-is-gap vs sub-not-gap (pⱼ small); m=4 exactly
(then m≥5 by the same descent, m→m−1 per complement cut, terminating at the certified m=3).
Watch out for: the SB-obstruction is NOT a contradiction here — it says the SB bound for the sub is
looser, but the ACTUAL A can still be < Σ/D_b; use the actual-A formula (R4), never an SB-monotone step
(certified dead R7). Do NOT use the deterministic cut-at-pⱼ cascade (REFUTED R8, 18385/29234 violations).
Budget: sub needs |sub|=3 ≤ b, OK since |X|≤b+1 and m=4 ⟹ b≥3.

---

refined-r-alt-tail: new
Target: c(n)=2^n/(2^{n+1}−1) — full LB. A UNIFYING refined-R attempt: the anchor's two routes (INC,
GAP) both converged onto T(ℓ) which then closed everything; this slug does the same for refined R —
reduce BOTH refined-R residuals (G-INC-2 and bucket (iii)/(B2*)-ref) onto ONE target T_R (refined-R
alternating-tail) and attack T_R by a mutual induction generalizing the certified anchor one. This is a
distinct route (single principled induction) and a hedge in case the two ad-hoc casework routes above
stall on their equal-split / a<1 / termination sub-cases.
Technique: {Claim_R(n,ε), T_R(n)} mutual strong induction, the refined-R generalization of certified
`t-ell-mutual-induction`, with the effective anchor A(R) replacing A(G_{n−1}).
Skeleton:
  1. Reduction (concrete, mostly verified): show every refined-R LB residual reduces to T_R.
     - G-INC-2 lower-band cut → top-band decomp with A(R) → T_R / Claim_R at level n−2 (from
       ll-inclusion-gap step 2).
     - bucket (iii) → double-REFL cancellation → (B2*)-ref = T_R (from ll-dyadic-symdiff steps 2–3,
       verified on Q=[15/4,13/4,1], R=[15/4,2,1,1/4]).
     — by `top-band-decomposition` (A(R) form) + `ll-reflection-identity-gen`.
  2. State T_R(n): O_P ≤ O_R for refined R with A(R)≥1, max(R)≤2^{n−1}, budget-reduced |P| (|Q|≤n when
     c_R≥1, certified budget-reduction). Claim_R(n,ε): A(Q) ≤ A(R)−1+ε, ε∈[0,1).
  3. Bases n≤3 direct (G-INC-2 vacuous at n=3; bucket iii n=3 casework from ll-dyadic step 4).
  4. Inductive step n→n−2: mirror the certified anchor step (h∈{0,2}, target 1−τ<1, 2b-i→Claim_R(n−2,ε'),
     2b-ii→T_R(n−2), ε'=a−b∈[0,1) never negative). — by mutual induction.
Key lemmas (claim + mechanism):
  - Refined-R reduction convergence — because the same double-REFL / top-band identities that reduced the
    anchor routes to T(ℓ) apply with A(R) in place of A(G_{n−1}), collapsing G-INC-2 and bucket (iii)
    onto the single target T_R (mirrors the R6 anchor convergence onto G-INC-1).
Open gaps (load-bearing, honestly flagged): the anchor step used the SET IDENTITY
S_{G_{n−1}}∩[0,2^{n−2})=S_{G_{n−3}}, which has NO refined-R analogue (S_R∩[0,2^{n−2})=S_{G_{n−3}}△flip).
The descent identity relating the lower half of S_R to a level-(n−3) refined system is UNKNOWN and is the
central obstruction. The equal-split top cut gives odd h (Parity-Condition breaks), needing a separate
base/branch (the direct case analysis from ll-inclusion-gap step 3). If no descent identity is found this
round, this slug's deliverable is the (valuable) convergence of step 1 with T_R isolated as the one gap —
the same posture that preceded the anchor breakthrough.
Cases to cover: G-INC-2 side (S_Q⊆S_R) and bucket-iii side (S_Q⊄S_R) both routed to T_R; equal-split
odd-h branch handled directly, not by the induction.
Watch out for: do NOT assume the SET IDENTITY or top-band decomposition transfer to refined R (they are
G_{n−1}-specific — both explorers confirm); do NOT strengthen Claim_R to ε<0 (FALSE, as for the anchor);
this slug OVERLAPS the two advances above by design — its distinct value is a single induction vs ad-hoc
casework, so if the outline-reviewer judges it redundant, drop it in favor of advancing the two routes.
