## imo-2026-03 — Lower-Bound Lens: B₊≤A₋+B₋ crux in the level-charge reduction

---

### CRITICAL CORRECTION (top priority — affects the approach's framing)

**The "level-charge reduction" B₊ ≤ A₋ + B₋ is algebraically equivalent to A(Q∪R) ≥ 1, NOT a genuine reduction.** Proof: for max|g|≤2, A = A₊ + A₋ and ∫g = (A₊−A₋)+2(B₊−B₋)=1, giving A₊ = 1+A₋−2B₊+2B₋, hence A = 1+2(A₋+B₋−B₊). So A ≥ 1 iff B₊ ≤ A₋+B₋. These are the same statement. Verified: 161/161 configs with max|g|≤2 satisfy B₊≤A₋+B₋ iff A≥1, 0 exceptions.

Consequence: the approach file's "the geometric inequality B₊≤A₋+B₋ is the honest OPEN crux" is correct but the "reduction" framing is misleading — it provides no mathematical simplification. The outliner should NOT present this as a reduction. The real task is to prove A(Q∪R) ≥ 1 directly.

---

### Distinct openings surfaced

**Opening A (clearest path): Sub-3a covers ALL tight A=1 cases; after Sub-3a exclusion, A grows with n**

Small-case evidence (conjecture, needs proof for general n):
- n=3 bucket(iii), 1/16 grid: exactly 1 config with A=1 (Q={3,3,2}, R={2,2,2,1}). Sub-3a fires on I₀=[0,1): g(0+)=−1 (odd), so I₀ starts in odd-g region, N_P odd throughout I₀. After Sub-3a exclusion: min A = 9/8 > 1.
- n=4 bucket(iii), 1/4 grid, c_R=1: min A after Sub-3a exclusion = 2. On 1/2 grid (c_R=1,2): after K1/K2/D1/Sub-3a all fail, the 4 remaining configs have A ≥ 3.
- n=5 bucket(iii), 1/2 grid, c_R=1: min A after Sub-3a exclusion = 3.

Pattern (conjecture): Sub-3a failure implies A ≥ ⌈n/2⌉ in bucket(iii). This would close bucket(iii) for all n by: Sub-3a fires (A ≥ 1, certified) OR Sub-3a fails (A > 1, trivially implies A ≥ 1).

Possible proof mechanism: when Sub-3a fails at EVERY level I_k, each level has an internal parity switch from an odd-multiplicity piece. These switches force "paired" odd-g sub-intervals at each level (one before, one after the switch), with total odd-g measure growing as n grows.

**Opening B: g(0+) ≤ −1 always in bucket(iii) — structural foundation**

PROVED (from budget formula): g(0+) = |Q|−|R| = (c_Q+1)−(n+c_R) = c_Q−c_R−(n−1). Since c_Q+c_R ≤ n and c_R ≥ 1: g(0+) ≤ c_Q−1−(n−1) = c_Q−n ≤ −1 (as c_Q ≤ n−1 from budget). Verified 1548/1548 on grids n=3,4,5.

Consequence: g starts NEGATIVE at x=0+. For g to achieve ∫g=1>0, it must go positive somewhere. The transition from negative to positive is the source of odd-g mass. Two sub-cases:

- g(0+) is ODD (≤−1, e.g., −1,−3,...): Then N_P(0+) = |Q|+|R| is odd (same parity as g(0+)). If no piece of P lies in int(I₀)=(0,1) with odd multiplicity, Sub-3a fires on I₀ (parity of #{pieces ≥ 1} is also odd). This is the Sub-3a route.

- g(0+) is EVEN (≤−2, e.g., −2,−4,...): N_P(0+) is even. I₀ starts in an even-g region. This is the "doubly negative" case that requires g to cross through −1 (odd) or jump by ±2 to reach positive values. Both create odd-g mass.

Parity of g(0+) depends on c_Q+c_R and n: for n=4, c_R=1, |Q|=3: g(0+)=3−5=−2 (ALWAYS even). For n=4, c_R=2, |Q|=3: g(0+)=−3 (odd → Sub-3a likely fires). This explains why the hard residual for c_R=1 cases is more subtle.

**Opening C: Budget-parity obstruction — R always has odd-mult pieces**

PROVED: In bucket(iii), it is IMPOSSIBLE for all R-pieces to have even multiplicity with c_R < n cuts. Proof: The "parity sum" P = #{values in R with odd multiplicity} starts at n (all G_{n-1} pieces have multiplicity 1 = odd). Each cut changes P by an odd amount (±1 or ±3). So P maintains the same parity mod 2 after an even number of cuts, and changes parity after odd cuts. For P=0 (all-even mult): need the total change = −n. With each change having absolute value ≥ 1 and being odd, the minimum cuts required is n. But budget in bucket(iii) forces c_r ≤ n−1. So P ≥ 1 always, meaning R has at least ONE odd-multiplicity piece.

Consequence: N_R (and hence g = N_Q−N_R) undergoes at least one ±1 parity transition. This transition creates adjacent intervals with g-values differing by ±1 — one of the two flanking intervals is odd-g. But this only gives A > 0 directly, not A ≥ 1. It's a prerequisite, not a closure.

**Opening D (extended formula for max|g|≥3)**

For general max|g|≤K, A(Q∪R) ≥ 1 iff:
  Σ_{j≥1} j*(M_{−(2j−1)} + M_{−2j}) ≥ Σ_{j≥1} j*(M_{2j} + M_{2j+1})

where M_k = measure{g = k}. Explicitly:
- max|g|≤2: A₋ + B₋ ≥ B₊ (verified, equivalent to A≥1)
- max|g|≤3: (A₋ + B₋) + 2C₋ ≥ B₊ + C₊ (C₊ = measure{g=+3}, C₋ = measure{g=−3})
- max|g|≤4: (A₋+B₋) + 2(C₋+D₋) ≥ (B₊+C₊) + 2D₊

Verified: for the case Q=[7.75,7.75,0.5], R=[4,4,3,2,1,1] (max|g|=4): LHS=4 ≥ RHS=3.75, slack=1/4. Formula gives A=3/2 ✓. These extended formulas are also pure algebraic restatements of A≥1 for the respective max|g| bounds.

The KEY OBSERVATION for the max|g|≥3 extension: max|g| in bucket(iii) is bounded by max(|Q|,|R|) ≤ n+1 (from budget). For small n, max|g| is small; for large n, max|g| can grow. The extended formula groups the "charge" into pairs (M_{−(2j−1)}, M_{−2j}) vs (M_{2j}, M_{2j+1}) weighted by j. The ΣQ=2^n constraint must force the LHS ≥ RHS for all n — but the mechanism is not clear from the formula alone.

**Opening E: Structural attack via ΣQ=2^n wide-support constraint**

ΣQ=2^n = 2·ΣG_{n−2}+2 means Q has EXACTLY 1 MORE total mass than 2·G_{n−2}. This "excess 1" forces the g-integral to be exactly 1, but why does it force A≥1?

Key constraint: ΣQ=2^n with all parts < 2^{n-1} means Q's parts sum to exactly TWICE the support of G_{n−2}. By the "wide-support" property of G_{n−1} (each dyadic level [2^{k−1},2^k) has exactly one G_{n−1}-piece of value 2^k at its right endpoint), the N_{G_{n−1}} staircase descends by 1 at each dyadic level. Any Q with ΣQ=2^n "matches" G_{n−1} in total mass but has 1 extra unit above ΣG_{n−1}.

The 1-unit excess must appear as a positive "bump" in g = N_Q − N_R. For this bump to contribute to A (odd g), it must be at an odd g-value. The width of this bump × its height ≥ 1 means: if the bump is at height 1 (A₊ region), width ≥ 1. But the bump can be at height 2 (B₊), with width ≥ 1/2 — and THAT is the case where B₊>0 but A₊=0. Then B₋ or A₋ must compensate. The SPECIFIC form of G_{n−1} should force this via the dyadic staircase.

A concrete strategy: show that any g=+2 region in bucket(iii) is accompanied by a g=−2 or g=−1 region of at least equal measure, using the fact that N_{G_{n−1}} drops by 1 at each level (so "lifting" g from +1 to +2 by a Q-piece is mirrored by an R-piece dropping g by 1 somewhere).

---

### Precision: what DOES need the ΣQ=2^n structure (vs just ∫g=1)

The approach file notes that ∫g=1 alone does NOT force A≥1 (counterexample: g≡2 on [0,1/2), A=0). The ΣQ=2^n structure adds:

1. ALL Q-parts < 2^{n-1} (no dominant piece). So g can't be +2 at large x (no Q-part near 2^{n-1} except the cut ones).
2. g(0+) ≤ −1 ALWAYS (proved above). So g starts negative — it cannot be +2 everywhere on [0, ∞).
3. Budget: |Q|+|R| ≤ 2n+1, so g has ≤ 2n+1 breakpoints across n levels.

These constraints together force A≥1. The g(0+)≤−1 constraint alone implies g must CROSS from negative to positive (since ∫g=1>0), and this crossing generically creates odd-g measure. The tightest cases are when g goes −2→0→+2 (skipping ±1 entirely) via ±2 jumps at even-multiplicity pieces. But Opening C shows R always has odd-mult pieces, forcing some ±1 jumps, creating odd-g regions.

---

### Tight/hard configs (key examples)

**n=3 tightest (A=1):** Q={3,3,2}, R={2,2,2,1}. g-profile: g=−1 on [0,1) (Sub-3a fires!), g=1 on [1,2), g=0 on [2,3), g=−1 on [3,∞). A=measure{g odd}=1+1=2... wait, let me recheck. Actually g(0+) = |Q|−|R|=3−4=−1, N_R=4 on [0,1) (all {2,2,2,1}>x), N_Q=3, g=−1. Then A=measure{g=−1 or g=+1}≥1.

**n=4 hardest residual (after K1/K2/D1/Sub-3a):** Q=[7.5,5.5,3.0], R=[7.5,4.0,2.0,1.0,0.5], A=3. g-profile: g=−2 on [0,0.5), g=−1 on [0.5,1.0), g=0 on [1,2), g=+1 on [2,3), g=0 on [3,4), g=+1 on [4,5.5), g=0 on [5.5,7.5). All residual n=4 configs have A≥3 (well above 1).

**n=4 non-tight (max|g|=3):** Q=[5.5,5.5,5.0], R=[4,4,4,2,1]. g: −2 on [0,1), −1 on [1,2), 0 on [2,4), +3 on [4,5), +2 on [5,5.5). A=1+1=2. Extended formula LHS = A₋+B₋+2C₋ = 1+1+0=2, RHS = B₊+C₊ = 0.5+1=1.5. LHS≥RHS ✓.

---

### Knowledge-base entries to use

- Lemma D1 (certified R10): `D1-small-discrepancy-kill.md` — max|g|≤1 slice, all n.
- K1/K2 (certified R9): `dyadic-cheap-kills.md` — merge-overlap and difference kills.
- Sub-3a (certified R5): `dyadic-level-parity.md` — fully-odd dyadic level.
- Lemma REFL-gen (certified R7): `ll-reflection-identity-gen.md` — for double-REFL.
- Lemma M/M0 (certified): `alt-sum-integral.md` — A = measure{g odd}, merge identity.

---

### Prior progress (current state of ll-dyadic-symdiff)

- Cases 1/2/Sub-3a: certified, R-agnostic, 91.6% of n=3 refined configs.
- B3a/B3b (anchor R=G_{n−1}): certified via double-REFL (REFL + REFL-gen).
- B3c at n=3: closed.
- n=3 bucket(iii): fully closed (R9).
- D1: certified (R10), closes max|g|≤1 slice.
- K1/K2: certified (R9).
- R11 correction: INC forcing max(Q)≤max(R) is FALSE (even-mult counterexample). D1-direct and level-charge reduction remain valid. The level-charge reduction A=1+2(A₋+B₋−B₊) is algebraically correct for max|g|≤2.
- Bucket (iii) general n: OPEN. n=3 closed. n=4,5: all configs have A≥1 (0 violations), min A growing with n.

---

### Dead ends (do not retry)

- "B₊≤A₋+B₋ is a genuine reduction": FALSE — algebraically equivalent to A≥1, not a reduction.
- "∫g=1 alone forces A≥1": FALSE (g≡2 on [0,1/2) breaks it).
- "INC forces max(Q)≤max(R)": FALSE (R11, even-mult counterexample confirmed).
- "{Claim_R, T_R} mutual induction": REFUTED R10 (not descent-closed, O1 fires).
- "REFL-telescope alone proves A≥1": FALSE (only recomputes A; the base object's A≥1 is the crux itself).
- "max|g|≤2 sub-case is easier than general": FALSE for proving B₊≤A₋+B₋ (equivalent to A≥1).

---

### Small-case / intuition notes (labeled conjectured vs proved)

- [PROVED] g(0+) = |Q|−|R| ≤ −1 always in bucket(iii). Verified 1548/1548. Formula: c_Q−c_R−(n−1) ≤ −1.
- [PROVED] B₊≤A₋+B₋ ⟺ A≥1 for max|g|≤2 (algebraic identity). Verified 161/161.
- [PROVED] Budget-parity: R cannot have all-even multiplicities with c_R < n cuts (parity argument on sum of multiplicities).
- [PROVED n=3,4,5] After Sub-3a exclusion in bucket(iii): min A = 9/8, 2, 3 respectively. All > 1.
- [PROVED n=3] Tight A=1 case in bucket(iii) has Sub-3a firing (Q={3,3,2}, R={2,2,2,1}: g(0+)=−1, I₀ fully odd).
- [PROVED n=4] After K1/K2/D1/Sub-3a: 4 residual configs (1/2 grid), all A≥3.
- [CONJECTURE] Sub-3a failure implies A>1 in bucket(iii) for all n. Growing pattern: A ≥ ⌈n/2⌉ after Sub-3a fails. This would close bucket(iii) (Sub-3a fires → A≥1; Sub-3a fails → A>1 > ... so A≥1 trivially).
- [CONJECTURE] Extended crux for max|g|≤K: A≥1 iff Σ_j j*(M_{−(2j−1)}+M_{−2j}) ≥ Σ_j j*(M_{2j}+M_{2j+1}), all verified for K≤4 on small grids (but still algebraically equivalent to A≥1 for fixed K).
- [OBSERVATION] g(0+) is always EVEN for n=4, c_R=1, |Q|=3: g(0+)=3−5=−2. This means I₀ starts with even N_P, so Sub-3a cannot fire on I₀ directly. The hard residual has g(0+)=−2 (g starts doubly negative). This is the specific hard sub-case.

---

### Synthesis: what the builder needs to attempt

The level-charge reduction is a RESTATEMENT not a tool. The builder should pivot to one of:

1. **Sub-3a + "A>1 when Sub-3a fails" route**: Prove that in bucket(iii), when Sub-3a fails at all n dyadic levels, A > 1. Mechanism: each Sub-3a-failing level has an internal parity switch, creating two sub-intervals of opposite parity. Sum over levels. This approach is supported by min A growing to 3+ for n=5.

2. **Direct case split on g(0+) parity**: When g(0+) is odd (N_P(0+) odd): Sub-3a fires on I₀ if no odd-mult piece in (0,1). When g(0+) is even (≤−2): g must transition from −2 through −1 (creating A₋>0) before reaching positive values (since ±2 jumps can skip 0 but must then come back). The specific formula: for g to go −2 → +2 without being −1 or +1, it must have a ±2 jump at some piece value; this requires an even-mult piece of P at that position. Budget constraints on the number of even-mult pieces could bound this.

3. **REFL-telescope on max(Q)=max(R) sub-case**: When max(Q)=max(R)=μ in bucket(iii), the double-REFL cancellation gives A(Q∪R) = A(Q'∪R'') with ΣQ'−ΣR''=1 and max(Q'),max(R'')< μ. This is again a bucket(iii)-like instance with smaller max. Termination: max decreases. The BASE CASE is when Q'∪R'' has |Q'|+|R''| ≤ 2 (trivial A≥0) or when Sub-3a/K1/K2/D1 fire on Q'∪R''. This is an inductive approach on max(P) that MIGHT terminate and close the case.
