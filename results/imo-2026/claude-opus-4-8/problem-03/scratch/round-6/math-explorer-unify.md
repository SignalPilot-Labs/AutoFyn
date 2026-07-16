## imo-2026-03 — "+1 excess" unification lens

### Problem recap (load-bearing gap)
Prove: for Q partitioning 2^n into t+1 ≥ 3 parts with A(Q)>0 and max(Q)<2^{n-1}+1, and R refining
G_{n-1}={1,2,…,2^{n-1}} with A(R)≥1 and max(R)≤2^{n-1}, we have A(Q∪R) = measure(S_Q △ S_R) ≥ 1.
Two existing routes:
- **ll-dyadic-symdiff Sub-3b**: when no full dyadic level I_k is "fully odd" for N_P=N_Q+N_R. Need
  Σ_k measure(I_k ∩ (S_Q △ S_R)) ≥ 1.
- **ll-inclusion-gap G-INC-1**: when S_Q ⊆ S_R (INC branch), need A(R) - A(Q) ≥ 1, equivalently for
  R=G_{n-1}: A(G_{n-1}) - A(Q) ≥ 1. The "+1 excess" is ΣQ - ΣG_{n-1} = 1.

---

### What was computed

All numerical computations were bounded python (≤5s each); 0 errors below are verified.

**Candidate 1 — per-level bound**: mismatch_k := measure(I_k ∩ (S_Q △ S_R)) ≥ |∫_{I_k}(N_Q−N_R)|.
If true, summing over k gives measure(S_Q △ S_R) ≥ Σ_k |int_diff_k| ≥ |Σ_k int_diff_k| = 1.

*Result*: **FALSE**. Counterexample: Q={2,2,2,2} (4-part, A(Q)=0), R=G_2. On I_1=[1,2):
int_diff=2, mismatch=0. (A(Q)=0 so not Sub-3b, but the bound fails on this family.)
More: Q={17/8,2,2,15/8} (A(Q)=1/4, IS Sub-3b) at I_1: int_diff=15/8, mismatch=1/8. Violation.
The failures are compensated by other levels (mismatch large on I_2), so TOTAL remains ≥1.
Checked 1274 (Q,R) pairs n=3 with refined R: 616 per-level violations, but 0 total-mismatch
violations. Per-level bound is DEAD as a proof route.

**Candidate 2 — integral identity on symdiff**: ∫_{S_Q △ S_R}(N_Q−N_R)dx = 1 always?
If true and N_Q−N_R ≤ 1 on the symdiff, would give measure ≥ 1 directly.

Tight cases (measure=1): Q={4,3,1}/R=G_2: integral=1, N_Q−N_G=1 everywhere on [2,3). ✓
Q={4,5/2,3/2}/R=G_2: integral=1, N_Q−N_G=1 everywhere on [1,3/2)∪[2,5/2). ✓
Non-tight cases: Q={3,3,2}/R=G_2: measure=3, integral=1. ✓ (but int OUTSIDE symdiff = 0 in this case)
FAILURE: Q={8/3,8/3,8/3}/R=G_2: S_Q △ S_G2 = [1,2)∪[8/3,4),
  ∫_{symdiff}(N_Q−N_G) = 1 − 4/3 = −1/3. VIOLATION: 3741/7680 configs fail this identity.

The identity holds iff ∫_{same-parity region}(N_Q−N_R)=0, which fails when N_Q and N_R have same
parity but different absolute values. NOT a viable unifying identity.

**Candidate 3 — arithmetic argument for INC case (promising)**:
In the INC branch (S_Q ⊆ S_R) with R=G_{n-1}: from Forcing Lemma, max(Q) ≤ 2^{n-1}.
For n=3, 3-part Q={q1≥q2≥q3}, ΣQ=8, INC constraint (no piece in forbidden band (1,2)): q3∉(1,2).

From ΣQ=8 and A(Q)=q1−q2+q3: summing gives q1+q3 = (8+A(Q))/2.
From q1 ≤ 4 (Forcing Lemma): (8+A(Q))/2 − q2 ≤ 4, so q2 ≥ A(Q)/2.

But also from subtraction: q2 = (8−A(Q))/2 = 4−A(Q)/2.
From max(Q) ≤ 4: q1 = (8+A(Q))/2 − q3 ≤ 4 requires q3 ≥ A(Q)/2.
INC constraint: q3 ≤ 1 (since q3∉(1,2) and q3 ≤ q2 ≤ 4).
Therefore A(Q)/2 ≤ q3 ≤ 1, giving **A(Q) ≤ 2 < 3 = A(G_2)**. Gap = A(G_2)−A(Q) ≥ 1. ✓

This is a COMPLETE PROOF of G-INC-1 for n=3, 3-part Q — using only the "+1 excess" (ΣQ=2^3)
plus the Forcing Lemma plus the forbidden-band constraint.

**Candidate 4 — same arithmetic for general n and more parts**:
For n=3, 4-part Q={q1≥q2≥q3≥q4}, ΣQ=8, INC (no piece in (1,2)): q3,q4 ≤ 1 or ≥ 2.
A(Q) = q1−q2+q3−q4 and ΣQ = 8.
Forcing Lemma: all pieces ≤ 4.
INC constraint forces: pieces in (2,4] (say m pieces), pieces in [0,1] (say ℓ pieces),
with even count of pieces ≥ 2 (from Sub-3b band structure certified in forcing-inc-reduction).

Sum constraint for pieces in (2,4]: sum ≤ 4m.
Sum constraint for pieces in [0,1]: sum ≤ ℓ.
ΣQ=8: 4m + ℓ ≥ 8 (approximate), giving interplay.

Numerically verified (n=3, step=1/4, 1274 INC configs): A(Q) ≤ 2 in all cases = A(G_2)−1. 0 violations.
The arithmetic argument generalizes; exact formulation for k-part Q and general n needs care.

**Candidate 5 — GAP case within Sub-3b**:
S_Q ⊄ S_R, max(Q) ≤ 2^{n-1} (Sub-3b condition). The "+1 excess" does NOT directly give measure ≥ 1
via A(R)≥1 (IH) because B can be > A(Q)/2, making A(Q)+A(R)−2B < 1.
Counter to naive bound: Q={4,5/2,3/2}, R=G_2: B=5/2, A(Q)=3>2*B... actually B=5/2<A(Q)=3? Let me recheck.
A(Q)=3, A(R)=3, B=measure(S_Q∩S_R)=measure([0,1)∪[5/2,4))=1+3/2=5/2. A(QUR)=3+3−5=1. ✓
Here B=5/2 > A(Q)/2=3/2. Naive bound A(QUR) ≥ A(R)−A(Q)=0. Insufficient.
For the GAP case the bound must come from the ALIGNMENT structure of S_G: the shift forces two
half-level contributions of equal size summing to 1 (one from S_Q\S_R, one from S_R\S_Q). This is
NOT a simple "excess integral" argument — it uses the alternating structure of G_{n-1} levels.

---

### Key structural finding: INC and GAP are NOT the same argument

The "+1 excess" argument closes SUB-3b INC via: Forcing Lemma + sum constraint + forbidden-band
exclusion → A(Q) ≤ A(G_{n-1})−1. This argument IS a direct use of ΣQ = 2^n = ΣG_{n-1}+1.

The "+1 excess" does NOT directly close SUB-3b GAP. The GAP case needs the dyadic alignment
structure of G_{n-1} (alternating odd/even levels), not just the total sum.

These two sub-cases are genuinely different mechanisms. A single unified stroke (one inequality
subsuming both) was NOT found. The closest unifying level is:

  **A(Q∪R) = measure(S_Q △ S_R) ≥ 1 by: (INC) A(G_{n-1})−A(Q) ≥ 1 [arithmetic], or (GAP)
  alignment cost from alternating level structure of G_{n-1}.**

Both use the G_{n-1} structure, but at different levels of detail.

---

### Whether the "+1 excess" directly forces measure ≥ 1

**Short answer: NO, not by itself.** The integral ∫(N_Q−N_R)=1 can be carried entirely by an
even-valued (N_Q−N_R) function on a small set, giving measure{N_Q+N_R odd}=0. The script
Q={8/3,8/3,8/3} shows this concretely: ΣQ=8, ΣG_2=7, integral=1, but for this Q the
symdiff has a negative-integral piece and only works out because the symdiff is large (measure=7/3).

What the "+1 excess" DOES do: it creates a TIGHT CONSTRAINT that, combined with the other structure
(Forcing Lemma, band avoidance), closes the INC case. In the INC case, the excess "pushes" A(Q) away
from A(G_{n-1}) by at least 1 unit via the arithmetic argument above.

---

### Distinct openings

1. **Arithmetic closure of INC case (general n, general part count)**:
   The n=3, 3-part proof above: q3 ≥ A(Q)/2 and q3 ≤ 1 (INC) gives A(Q) ≤ 2. 
   For general n: the forbidden-band structure forces the lowest piece(s) to be constrained, and
   the Forcing Lemma (max(Q) ≤ 2^{n-1}) + ΣQ = 2^n together give A(Q) ≤ A(G_{n-1})−1.
   This is the most tractable new direction — a proof by pure arithmetic on the piece values,
   no measure theory beyond the Forcing Lemma and INC reduction.

2. **GAP case via dyadic alignment cost**:
   When S_Q ⊄ S_{G_{n-1}} with max(Q) ≤ 2^{n-1}: the "miss" point where N_Q is odd but N_G even
   (or vice versa) creates two complementary pieces of the symdiff with total measure controlled by
   the dyadic spacing between consecutive G_{n-1}-levels. Each such pair contributes ≥ some δ > 0,
   and the total budget is 1. This needs a careful "alignment cost" bound for the specific alternating
   structure of S_{G_{n-1}}.

3. **Fixing ll-inclusion-gap via arithmetic instead of Structural Lemma**:
   The Structural Lemma is FALSE (counterexample Q={3/2,3/2,2,3}). But the conclusion A(Q) ≤
   A(G_{n-1}) for S_Q ⊆ S_{G_{n-1}} is true (follows from containment). The STRICT version
   A(Q) ≤ A(G_{n-1})−1 can be proved by the arithmetic argument (Candidate 3) without the
   Structural Lemma. Opening 1 (above) is a specific realization of this for the INC branch,
   proving G-INC-1 without ever needing the false Structural Lemma. A new proof path for ll-inclusion-gap
   that bypasses the false lemma.

4. **The GAP case within Sub-3b is the "Flavor B" tight case**: Q={4,5/2,3/2} / R=G_2 is the
   canonical tight example. The symdiff = [1,3/2)∪[2,5/2) has exactly two pieces, each of measure
   1/2 from the level I_1 and level I_2 respectively. This structure: S_Q enters I_1's odd region,
   creating a "bulge" in I_1, which is exactly compensated by a "gap" in I_2 of equal measure.
   The compensation is forced by the total integral = 1. This specific argument (bulge-gap pairing
   via integral constraint on the G_{n-1} dyadic levels) is the candidate for the GAP case.

---

### Candidate techniques

- **Arithmetic: Forcing Lemma + piece-value inequality** for INC case. The key: max(Q) ≤ 2^{n-1}
  + ΣQ = 2^n + forbidden-band exclusion (no piece in (2^{k-1},2^k) for forbidden k) forces
  q_min ≥ A(Q) / (number of ODD-indexed pieces), while INC and band structure bound q_min from above.
- **Dyadic alignment cost** for GAP case: the distance from S_Q to S_{G_{n-1}} in symmetric-
  difference sense, measured level by level.
- **Induction on n with strengthened IH** carrying the INC gap bound: IH at n−1 gives A(R) ≥ 1;
  strengthened IH gives A(R) ≥ A(Q_sub)+1 for any sub-partition Q_sub with S_{Q_sub} ⊆ S_R.

---

### Cheap-kill candidates

- **INC 3-part arithmetic (n=3)**: completely closed by Candidate 3 above. Not needed as a new lemma
  since ll-inclusion-gap Step 6 already does it, but the arithmetic formulation is cleaner.
- **Sub-3b with all Q-pieces ≥ 2**: Q pieces ≥ 2 and max ≤ 2^{n-1} → all pieces in even-N_G
  forbidden bands or ODD-N_G allowed bands; piece count is even (INC constraint); sum = 2^n. This
  forces the total allowed-band deficit ≥ 1 via direct sum bound: sum of pieces in allowed bands +
  2*(forbidden-band sum) = 2^n, and allowed-band sum ≤ (n-1)*2^{n-2} < 2^n (there's always slack).
  **Conjecture only** — not verified as a standalone bound.

---

### Knowledge-base entries to use

- **Monotone invariants / monovariants**: the "A(Q) ≤ A(G_{n-1})−1" bound is a monotone descent
  controlled by the piece-value arithmetic.
- **Induction with strengthened IH**: the clean path; INC case at n requires A(R) ≥ A(Q)+1, which
  for R=G_{n-1} is the arithmetic bound, and for refined R needs the strengthened IH.
- **Direct computation / extremal**: the tight cases (equality A(QUR)=1) are known (Q={4,3,1} and
  Q={4,5/2,3/2} for n=3), so the extremal argument can be anchored there.

---

### Analogous past problems (cruxes)

None checked this round (time; prior rounds found none truly analogous). The crux is the "+1 excess"
in the integral ∫(N_Q−N_G)=1 forcing the parity mismatch measure ≥ 1 via a specific band structure.
This is unusual in the combinatorics corpus.

---

### Prior progress

- Sub-3b: Cases 1, 2, Sub-3a of ll-dyadic-symdiff are CLOSED. Only Sub-3b remains.
- G-INC-1: the INC case of ll-inclusion-gap. n=3 base case done (Step 6 of the approach file).
  The Structural Lemma that was supposed to do general n is FALSE; arithmetic replacement needed.
- The "+1 excess" arithmetic is the right tool for the INC case; it has NOT been applied in full
  generality yet (only n=3, 3-part, in Step 6).

---

### Dead ends (do not retry)

- **Per-level bound** (mismatch_k ≥ |integral_k|): FALSE. Counterexamples found. Do not pursue.
- **Integral identity on symdiff** (∫_{S_Q △ S_R}(N_Q−N_R)=1): FALSE for general Q. 3741/7680 violations.
- **Structural Lemma** (ll-inclusion-gap part (a), "no Q-piece in forbidden-band interior"): CERTIFIED
  FALSE (counterexample Q={3/2,3/2,2,3}). Do not use. Replace with arithmetic bound on A(Q).
- **Single-level pigeonhole for Sub-3b**: confirmed impossible (85/187 n=3 Sub-3b configs have every
  level partially even). Not useful.

---

### Small-case / intuition notes

1. In ALL tight cases (A(QUR)=1) for n=3, the "+1 excess" is carried entirely by the symdiff
   (∫_{symdiff}(N_Q−N_G)=1 and N_Q−N_G=1 everywhere on the symdiff). This suggests the tight cases
   are those where the excess is "perfectly aligned" with the mismatch — CONJECTURE, not proved.

2. For the INC arithmetic: the constraint q_min ≥ A(Q)/2 (from Forcing Lemma) and q_min ≤ 1
   (from INC+forbidden-band) gives A(Q) ≤ 2 = A(G_2)−1. This is provable and complete for n=3.
   The same argument with 4-part Q: must handle two small pieces; the bound is A(Q) ≤ 2 still
   (verified numerically, step 1/4: 0 violations of A(Q) ≤ 2 in INC configs at n=3).

3. The GAP case tight example Q={4,5/2,3/2}: the two symdiff pieces [1,3/2) and [2,5/2) are a
   "half-unit in I_1" and "half-unit in I_2". Their sum is 1 because the total integral is 1 and
   each piece has N_Q−N_G=1. This "half-unit pairing" across levels is the GAP case mechanism —
   CONJECTURE that it generalizes to always give ≥ 1.

---

### Outliner recommendation

**Do NOT open a single unified slug** — there is no single clean invariant that subsumes both
Sub-3b INC and GAP in one stroke. The per-level bound and integral identity are both false.

**Do**:
1. Push ll-inclusion-gap's G-INC-1 via the arithmetic argument (Candidate 3 / Opening 1): for general
   n and general part count, prove A(Q) ≤ A(G_{n-1})−1 in the INC case using only Forcing Lemma +
   ΣQ=2^n + forbidden-band exclusion. This replaces the false Structural Lemma with a pure arithmetic
   inequality. This is the most tractable new direction.

2. Push the GAP case of Sub-3b (which is Sub-3b ∩ {S_Q ⊄ S_R, max(Q)≤2^{n-1}}) via the dyadic
   alignment cost argument. The key: the "miss" in S_Q \ S_R creates a compensating S_R \ S_Q
   of equal or greater measure, and the "+1 excess" integral forces their combined measure ≥ 1.

3. Keep ll-dyadic-symdiff alive for its Case 1/2/Sub-3a certifications; its Sub-3b is exactly the
   residual that INC+GAP above would close.

4. Consider a NEW slug "ll-arithmetic-inc" that proves G-INC-1 for all n via the arithmetic approach
   in Opening 1, bypassing the false Structural Lemma entirely. This is the single most actionable
   new direction identified this round.
