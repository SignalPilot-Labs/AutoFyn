## imo-2026-03 (Lower-Bound lens: bucket(iii) Opening D + INC containment base)

---

### Distinct openings surfaced this round

**Opening D-1 (INC containment base via D1 + ΣQ'−ΣR'' ≥ 1):**
In the INC sub-case of bucket(iii), S_Q ⊆ S_R forces max(Q) ≤ max(R) (proven below). This gives ΣQ'−ΣR'' = 1 + (max(R)−max(Q)) ≥ 1. D1 (certified) then closes the INC containment base A(Q'∪R'') ≥ 1 whenever max|g_{Q',R''}| ≤ 1: A ≥ |ΣQ'−ΣR''| ≥ 1. Verified: 168/175 (96%) of n=4 INC bucket(iii) configs are closed by D1 directly via this route. The other 7 (max|g|=2, all have max(Q)=max(R)=7) are closed by Sub-3a on Q'∪R'' (verified for all 7). This is a NON-MUTUAL-INDUCTION proof of the INC containment base, needing only: (a) max(Q) ≤ max(R) forced by INC, (b) D1 (already certified), (c) Sub-3a (already certified) for the residual 7 cases.

**Opening D-2 (charge accumulation formula: GAP residual A ≥ 2):**
In the GAP (non-containment) residual after K1/K2/Sub-3a/D1, ALL configs have max|g| ∈ {2,3} and A ≥ 2 (verified: n=3 one residual config A=3; n=4 residual ~630 configs all A ≥ 2). The formal charge argument: write ∫g = ∫_{g odd} g + ∫_{g even} g = 1. Let A_+, A_− = measure of {g=1}, {g=−1}; B_+, B_− = measure of {g=2}, {g=−2}. Then (A_+−A_−) + 2(B_+−B_−) = 1. The A ≥ 2 bound would follow from: A_+ + A_− ≥ 2. From (A_+−A_−) = 1−2(B_+−B_−) and A = A_++A_−, the claim A ≥ 2 is equivalent to A_+ ≥ 1 or A_− ≥ 1 (at least one of the g=±1 regions has measure ≥ 1). This is strongly suggested by Sub-3a failure + budget constraint. The charge framework is correct; the formal proof of A ≥ 2 (or just A ≥ 1) in the residual is the open step.

**Opening D-3 (budget-breakpoint count forces A ≥ 1 in residual):**
In bucket(iii): g has at most |Q|+|R| ≤ 2n+1 breakpoints across n dyadic levels. With Sub-3a failing (every level has both odd-g and even-g sub-intervals), each level contains ≥ 1 breakpoint. For max|g|=2 (one "bad" level with a g=±2 excursion), the budget forces the "bad region" to be bounded in extent. Specifically, in the n=3 residual: the single bad region has measure exactly 0.25 (one piece at value 3, contributing g=−2 on [3,3.25)). The compensating odd-g regions sum to A=3 >> 1. For n=4 the non-tight margin is even larger (A ≥ 2, gap ≥ 1). This strongly suggests a budget-count argument closes the residual, but the exact form is open.

---

### Computational findings (key, verified)

**INC max(Q) ≤ max(R) is FORCED:**
If max(Q) > max(R) in bucket(iii), then for x = (max(Q)+max(R))/2: N_Q(x) = 1 (odd, only max(Q) exceeds x) and N_R(x) = 0 (even, no R-piece exceeds max(Q) > x). INC condition (N_Q odd → N_R odd) fails. So INC implies max(Q) ≤ max(R). This makes ΣQ'−ΣR'' = 1+(max(R)−max(Q)) ≥ 1. CLEAN, provable, no induction needed.

**D1 coverage of INC configs (n=4, proper G3 refinements):**
- Total INC bucket(iii) configs: 175
- Closed by D1 (max|g| ≤ 1, uses ΣQ'−ΣR'' ≥ 1): 168 (96%)
- Residual (max|g| = 2): 7 configs, all with A(Q∪R) = A(R)−A(Q) ≥ 3
- All 7 residual: max(Q) = max(R) = 7, R = {7,4,2,1,1}
- For all 7: Sub-3a fires on Q'∪R'' (the I_3=[4,8) level has only one piece > 4, giving N_{P'}=1 odd throughout [4, max(Q'∪R'')), ≥ 1 measure)

**A(R)−A(Q) minimum in INC bucket(iii): 3/2, NOT 1:**
The INC containment base is NON-TIGHT at n=4 (min A = 3/2 > 1). This means any proof that works gets a margin. The tight cases (diff = 3/2) all have max|g| = 1 and are closed by D1 with ΣQ'−ΣR'' = 3/2.

**GAP residual (n=3,4) statistics:**
- n=3 GAP residual after K1+K2+Sub-3a+D1: 1 config, A=3, max|g|=2
  - Q=[3,2.75,2.25], R=[3.75,3.25]. g-profile: g=+1 on [0,2.25), g=0 on [2.25,2.75), g=−1 on [2.75,3), g=−2 on [3,3.25), g=−1 on [3.25,3.75).
  - even_int = −0.5 (g=−2 on [3,3.25)), odd_int = +1.5. A=3. Charge: the g=−2 excursion has measure 0.25 and contributes −0.5 to ∫g; the g=±1 regions compensate with +1.5, giving A=3 >> 1.
- n=4 GAP residual (with proper G3 refinements and Sub-3a): ~629 configs, all A ≥ 2, max|g| ∈ {2,3}

**n=3 INC bucket(iii): ZERO configs exist:**
G2={1,2,4} has 3 pieces (odd). With cR ≥ 1 cuts of G2: |R| ∈ {4,5,...}. For |Q| odd (|Q|≥3 needed since 2 parts summing to 8 with each <4 is impossible): INC at x=0+ requires N_R(0+) = |R| odd. With 1 cut: |R|=4 (even) → INC fails. With 2 cuts: |R|=5 (odd) but budget cQ+cR ≤ n=3 with cQ≥2 (|Q|≥3) gives cQ+cR ≥ 4 > 3. Budget exceeded. So NO INC configs exist in n=3 bucket(iii) — INC first appears at n=4. This explains why the n=3 anchor proof (B2* at n=3) did NOT see any INC configs.

---

### Key structural insight for Opening D INC case

For the INC sub-case of bucket(iii), the containment base A(Q'∪R'') ≥ 1 follows by a 2-step argument requiring NO mutual induction:

1. **ΣQ'−ΣR'' ≥ 1**: From INC forcing max(Q) ≤ max(R), get ΣQ'−ΣR'' = (ΣQ−max(Q)) − (ΣR−max(R)) = (2^n−max(Q)) − (2^n−1−max(R)) = 1+(max(R)−max(Q)) ≥ 1.

2a. **D1 closes max|g_{Q',R''}| ≤ 1 cases**: Certified D1 gives A(Q'∪R'') ≥ |ΣQ'−ΣR''| ≥ 1.

2b. **Sub-3a closes max|g_{Q',R''}| ≥ 2 cases** (7 configs, n=4): when max(Q)=max(R), Q'∪R'' has one dominant piece (the largest piece from Q, being close to 7 < 8 = 2^{n-1}), so the I_3=[4,8) dyadic level contains exactly that one piece, giving N_{P'}=1 (odd) throughout (largest piece to 2^{n-1}), firing Sub-3a with measure ≥ 1. This is a structural property: if max(Q)=max(R)=μ ∈ (4,8), then in Q'∪R'' the only piece > 4 is μ (from Q'; R'' has max(R'')=max(R\{μ}) ≤ 4). So N_{Q'∪R''}(x) = 1 (odd) for all x ∈ (4, μ), giving measure ≥ μ−4 > 0. If μ > 5, measure > 1 and Sub-3a fires on I_3.

**HOWEVER**: Need to check: is max(Q) = max(R) the ONLY non-D1 INC case pattern, or can max(Q) < max(R) also give max|g_{Q',R''}| ≥ 2? From n=4 data: all 7 non-D1 cases have max(Q)=max(R). This might be provable: if max(Q) < max(R), the g jump at max(Q) contributes −1 (Q-piece boundary) and g just below max(Q) is higher by 1 than just above. With max(R) > max(Q), there are fewer R-pieces near max(Q) (since max(R) is the top). This combination may force max|g_{Q',R''}| ≤ 1 when max(Q) < max(R). A general proof of this would remove the case 2b entirely.

---

### Candidate techniques

- **D1 (certified R10)** + the ΣQ'−ΣR'' ≥ 1 observation: closes INC containment base for 96% of configs.
- **Sub-3a (certified)** for the residual 7 non-D1 INC cases (dominant piece in high dyadic level).
- **Level-charge accumulation (Opening D-2)**: framework for GAP residual; needs either A ≥ 2 or budget-based argument to close it.
- **Budget-breakpoint count**: in bucket(iii), ≤ 2n+1 breakpoints across n levels. With Sub-3a failing (≥1 breakpoint per level) and max|g|=2 (one bad region), the parity-flip structure forces compensating odd-g measure ≥ 1.

---

### Knowledge-base entries to use

- Lemma D1 (certified R10): `lemmas/D1-small-discrepancy-kill.md` — main tool for INC cases.
- Lemma M0/M (certified): integral representation A = measure(S_Q △ S_R), merge identity.
- K1/K2 cheap-kills (certified R9): `lemmas/dyadic-cheap-kills.md`.
- Sub-3a (implicit in `lemmas/dyadic-level-parity.md`).
- REFL-gen (certified R7): `lemmas/ll-reflection-identity-gen.md` — for double-REFL structure.

---

### Prior progress

n=3 bucket(iii): FULLY CLOSED (R9). D1 certified (R10), closes 96% of n=4 INC. GAP residual n=4: A ≥ 2, max|g| ∈ {2,3}. INC containment base: D1+Sub-3a covers all n=4 cases. OPEN: GAP residual formal proof (Opening D A ≥ 1 or A ≥ 2), general n INC base (d1+sub3a pattern unverified for n=5+).

---

### Dead ends (do not retry)

- {Claim_R, T_R} mutual induction for INC containment base: REFUTED R10 (O1 witness, not descent-closed). Do NOT reopen.
- max(Q) < 2^{n-1} ⟹ A ≥ 2: FALSE (B3 tight, Q={3,3,2} R={2,2,2,1} gives A=1). Do NOT reimport.
- K2 for INC cases: CIRCULAR (K2 fires iff A(R)−A(Q)≥1, which IS the claim). Not a proof.
- "∫g = 1 alone forces A ≥ 1": INSUFFICIENT obstruction (g≡2 on [0,0.5) gives ∫g=1, A=0). Do NOT claim this alone proves A ≥ 1 in the residual.

---

### Small-case / intuition notes (conjectured unless marked proved)

- [PROVED] n=3 INC bucket(iii): 0 INC configs exist (budget+parity impossibility).
- [PROVED] INC forces max(Q) ≤ max(R) in bucket(iii).
- [PROVED for n=4] D1+Sub-3a close all 175 INC bucket(iii) n=4 configs.
- [CONJECTURE, n=4 verified] When max|g_{Q',R''}| ≥ 2 in INC bucket(iii), it's precisely when max(Q) = max(R), and Sub-3a on Q'∪R'' always fires with measure ≥ max(Q)−4 ≥ 1 (for max(Q)∈(5,8) in n=4). This gives a clean general-n handle for n≥4: if max(Q)=max(R)=μ ∈ (2^{n-2}+1, 2^{n-1}), then I_{n-1}=[2^{n-2},2^{n-1}) has measure 2^{n-2} ≥ 1 and exactly 1 piece (μ from Q') > 2^{n-2}, giving N_{P'}=1 (odd) throughout [2^{n-2}, μ), measure μ−2^{n-2} ≥ 1.
- [CONJECTURE] For GAP residual: A ≥ 2 always (not just A ≥ 1). The charge argument gives A_+ + A_− ≥ 2 from (A_+−A_−) + 2(B_+−B_−) = 1 combined with budget constraints. Formal proof would close bucket(iii) GAP completely.
- [OBSERVATION] n=3 GAP residual (1 config): even_int = −0.5, A = 3. The even-|g| excursion (g=−2 on a 0.25-length interval) pushes ∫g down, and the compensating odd-g regions have A=3 >> 1. This is typical of the non-tight character.

---

### Clearest path to closing bucket(iii) general n

**For INC sub-case**:
Theorem (non-inductive): Let Q partition 2^n into parts all < 2^{n-1}, R refine G_{n-1} with max(R)<2^{n-1}, and S_Q ⊆ S_R. Then A(Q∪R) ≥ 1.
Proof: (1) INC forces max(Q) ≤ max(R). Let q=max(Q), r=max(R), Q'=Q\{q}, R'=R\{r}. (2) ΣQ'−ΣR' = 1+(r−q) ≥ 1. (3a) If max|g_{Q',R'}| ≤ 1: D1 gives A(Q'∪R') ≥ ΣQ'−ΣR' ≥ 1. Then REFL-gen: A(Q∪R) = q − A(Q'∪R) ... wait, but q = max(Q) ≤ r = max(R), so max of Q∪R is r. Apply REFL-gen removing r from R first: A(Q∪R) = r − A(Q∪R'). Then remove q from Q: A(Q∪R') = q − A(Q'∪R'). So A(Q∪R) = r − q + A(Q'∪R'). We need A(Q'∪R') ≥ 1 − (r−q)... if r>q this gives target < 1. HMMMM. So the containment base IS A(Q'∪R') ≥ 1−(r−q), NOT ≥ 1! Let me recheck.

CORRECTION: A(Q∪R) = r − A(Q∪R') [from REFL removing r] = r − (q − A(Q'∪R')) [from REFL removing q] = r − q + A(Q'∪R'). So A(Q∪R) ≥ 1 iff A(Q'∪R') ≥ 1−(r−q). Since r ≥ q: 1−(r−q) ≤ 1. So we need A(Q'∪R') ≥ 1−(r−q) ≤ 1.

But if r > q by a lot (r−q ≥ 1), then A(Q'∪R') ≥ 0 (trivially true!) → A(Q∪R) = r−q+A(Q'∪R') ≥ r−q ≥ 1. So large-gap (r−q ≥ 1) is trivially closed.

If r−q < 1: need A(Q'∪R') ≥ 1−(r−q) ∈ (0,1). Since ΣQ'−ΣR'' = 1+(r−q) in my earlier computation... wait I need to recompute. The REFL reduction gives A(Q∪R) = r−q+A(Q'∪R'), and Q'=Q\{q}, R'=R\{r}. ΣQ' = ΣQ−q = 2^n−q. ΣR' = ΣR−r = 2^n−1−r. ΣQ'−ΣR' = 1+(r−q). For r−q < 1: ΣQ'−ΣR' ∈ (1,2). And we need A(Q'∪R') ≥ 1−(r−q) ∈ (0,1).

D1 on Q'∪R': if max|g| ≤ 1 → A(Q'∪R') ≥ |ΣQ'−ΣR'| = 1+(r−q) > 1−(r−q) (since 2(r−q) > 0 for r>q). So D1 gives A(Q'∪R') ≥ 1+(r−q) ≥ 1 > 1−(r−q). ✓

So D1 on Q'∪R' (when max|g|≤1) gives A(Q'∪R') ≥ 1+(r−q), and then A(Q∪R) = r−q+A(Q'∪R') ≥ r−q+1+(r−q) = 1+2(r−q) ≥ 1. ✓

And for max|g_{Q',R'}| ≥ 2: the 7 exceptional n=4 cases have r−q=0 (r=q=7) and Sub-3a fires.

So the complete argument for INC bucket(iii) is:
- If r−q ≥ 1: A(Q∪R) = (r−q) + A(Q'∪R') ≥ r−q ≥ 1. (TRIVIAL)
- If r−q ∈ [0,1): apply double-REFL to get A(Q∪R) = (r−q) + A(Q'∪R').
  - If max|g_{Q',R'}| ≤ 1: D1 gives A(Q'∪R') ≥ 1+(r−q). Total A(Q∪R) ≥ 1+2(r−q) ≥ 1. ✓
  - If max|g_{Q',R'}| ≥ 2: Sub-3a (check if max(Q'∪R') = q = r = μ ∈ (2^{n-2}+1,2^{n-1}) → I_{n-1} region gives Sub-3a). CONJECTURE for general n; proved n=4.

**This is the most promising direction to brief the outliner**: the INC containment base can be closed by D1 (dominant) + trivial case (r−q≥1) + Sub-3a for the small residual, with NO mutual induction needed.

**For GAP sub-case**: Opening D framework is set up correctly, but the formal A ≥ 1 proof for the residual (max|g|=2, Sub-3a fails) is still open. The A ≥ 2 empirical observation suggests the budget + level-parity constraints force a stronger bound. Needs more thought.
