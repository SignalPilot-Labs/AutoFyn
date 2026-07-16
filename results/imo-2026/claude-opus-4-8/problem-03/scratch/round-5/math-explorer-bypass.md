# imo-2026-03 — Bypass Explorer Report (LOWER-BOUND BYPASS lens)

## Problem
c(n) = 2^n/(2^{n+1}-1). Both bounds must be proved.  
THE SINGLE LOAD-BEARING GAP: **LL t≥2 with A(Q)>0** — prove A(Q∪R) ≥ 1 when Q partitions 2^n into ≥3 parts (A(Q)>0) and R refines G_{n-1} with A(R)≥1, max(R)≤2^{n-1}.

---

## Distinct openings surfaced

### Opening 1 (VERIFIED VIABLE — partial): Split max(Q) vs 2^{n-1}+1

- **Sub-case max(Q) ≥ 2^{n-1}+1**: b = max(Q) - 2^{n-1} ≥ 1. Since S_R ⊆ [0,2^{n-1}) is entirely disjoint from S_Q ∩ [2^{n-1}, max(Q)) = [2^{n-1}, max(Q)), the symmetric difference measure(S_Q △ S_R) ≥ b ≥ 1. **DONE for this sub-case.** No Q-R interaction needed.

- **Sub-case max(Q) ≤ 2^{n-1}** (b=0): ALL Q-pieces ≤ 2^{n-1}, so S_Q ⊆ [0, 2^{n-1}). This is the hard residual.

Numerically confirmed (n=3,4 grids): the hard case max(Q) ≤ 2^{n-1} includes all tight cases. The easy case (b≥1) covers ~42% of the n=3 grid (VERIFIED, step 1/6).

### Opening 2 (VERIFIED VIABLE — partial): Lemma P coverage

When total final piece count |Q∪R| = (t+1)+|R| is ODD and all pieces ≥ 1: Lemma P (certified) gives A(Q∪R) ≥ min(piece) ≥ 1 immediately.

This covers the sub-case t + cuts_R ≡ n (mod 2) [odd total cuts make odd total count 2n+1] with min(Q) ≥ 1.

Coverage (n=3, t=2 grid): Lemma P alone covers ~16.6% of configs. Combined with b≥1 case: the HARD RESIDUAL is configurations where count is even AND max(Q) ≤ 2^{n-1}.

**New lemma needed**: LL for EVEN piece count + all pieces ≥ 1. Tight case: Q=[4,2,2], R=G_2={1,2,4} (n=3). Count=6 (even), all≥1. A(Q∪R) = 1 exactly. VERIFIED (S_Q △ S_R = [1,2), measure=1).

### Opening 3 (NEW KEY INSIGHT — not yet a proof): Symmetric difference of S_Q and S_R

A(Q∪R) = measure(S_Q △ S_R). The tight cases (n=3,4 fully checked) all satisfy:

| Configuration | S_Q △ S_R |
|---|---|
| Q=[3,3,2], R={1,2,2,2} | [0,1), measure=1 |
| Q=[4,5/2,3/2], R=G_2 | [1,3/2)∪[2,5/2), measure=1/2+1/2=1 |
| Q=[6,5,5], R={6,2,2,2,2,1} | [0,1), measure=1 |
| Q=[6,6,4], R={4,4,4,2,1} | [1,2), measure=1 |

PATTERN (CONJECTURE): S_Q △ S_R always has measure ≥ 1, and in tight cases the symmetric difference lies within a DYADIC interval [2^{j-1}, 2^j) from G_{n-1}'s structure.

**CLAIM (not yet proved)**: For Q partitioning 2^n and R refining G_{n-1}, the symmetric difference S_Q △ S_R always has measure ≥ 1.

The KEY STRUCTURAL FACT: sum(Q) - sum(R) = 2^n - (2^n-1) = 1 ALWAYS. So ∫(N_Q - N_R)dx = 1 identically. This integral being 1 does NOT directly imply measure{S_Q △ S_R} ≥ 1 for general step functions, but with the specific structure of G_{n-1} it seems to force it.

### Opening 4 (CONJECTURE, needs proof): Budget constraint blocks S_Q = S_R

The potential "danger" configuration is S_Q = S_R (giving A=0). This is BLOCKED by the budget: if S_Q = S_R then N_Q - N_R is always even, so ∫(N_Q - N_R)dx = ∫(even integers)dx. But this integral is 1 (odd). 

Wait: ∫(even integers)·dx CAN equal 1 (e.g., if f=2 on [0,1/2)). So the pure parity argument doesn't block S_Q = S_R. HOWEVER, the numerical search (n=3 fine grid, n=4 medium grid) confirms S_Q △ S_R never has measure 0. The STRUCTURE preventing this must come from the specific dyadic shape of G_{n-1}.

**CONJECTURE**: For Q partitioning 2^n and R refining G_{n-1} with t + cuts_R ≤ n, S_Q ≠ S_R (the odd-cover sets are always distinct). Moreover, their symmetric difference has measure ≥ 1.

### Opening 5 (POTENTIALLY CLEAN — new direction): Equal-pair cancellation + sub-instance reduction

A(Q∪R) = A(Q∪R with equal pairs cancelled). In all tight cases, after cancelling equal pieces, the remainder P' has A(P') = 1.

n=3 tight case 1: P={3,3,2,2,2,2,1}. Cancel (3,3),(2,2),(2,2): P'={1}. A=1.
n=4 even-count: P={6,6,4,4,4,4,2,1}. Cancel (6,6),(4,4),(4,4): P'={2,1}. A=2-1=1.
n=3 tight case 2: P={4,4,5/2,3/2,2,1}. Cancel (4,4): P'={5/2,2,3/2,1}. A=5/2-2+3/2-1=1.

The "leftover" P' after cancelling all equal pairs always has A(P')=1. CONJECTURE.

**Why this matters**: If P'={5/2,2,3/2,1}, this corresponds to Q'={5/2,3/2} partitioning 4=2^{n-1} with t'=1 cut and R'=G_1={2,1}=G_{n-2}. So A(P') = A(Q'∪R') = LL for n-1 with t'=1 (ALREADY CERTIFIED as LL t=1). This is a **self-similar recursive structure**!

The equal-pair cancellation reduces the LL t≥2 case to a smaller LL instance. This could be the key bypass: prove that after cancelling the largest equal pair (which always exists — the largest piece of G_{n-1} is 2^{n-1} and XY's cut of 2^n can always produce a piece equal to max(R)), the remainder reduces to a smaller LL instance.

**CAVEAT**: This only works when Q has a piece EXACTLY equal to an R-piece. In general, Q-pieces and R-pieces need not be equal. The cancellation argument requires exact equality, which is not guaranteed.

### Opening 6 (VIABLE for even-count case): Interval [1,2) structural argument

For the EVEN-COUNT hard case (all pieces ≥ 1, count even, max(Q) ≤ 2^{n-1}):

The smallest G_{n-1} piece is 1 = 2^0. If the 1-piece is NOT cut by XY (min(R) = 1):
- N_R at x=1-ε: N_R = |R| (all pieces ≥ 1)
- N_R at x=1+ε: N_R = |R|-1 (the 1-piece drops out)

So N_R changes parity at x=1. For EVEN |R|: N_R = |R| (even) just below 1, and |R|-1 (odd) just above 1. So [1, ...) starts in S_R.

Now if N_Q(x) is EVEN on the interval [1, 2): N_{Q∪R}(x) = N_Q(x) + N_R(x) = even + odd = ODD on [1,2). So [1,2) ⊆ S_{Q∪R} and A(Q∪R) ≥ 1. Done!

**When is N_Q even on ALL of [1,2)?** When the number of Q-pieces in (1,2) is even (since N_Q changes at Q-piece boundaries). If Q has an EVEN number of pieces with values in (1,2), then N_Q starts even at x=1+ε and ends even at x=2-ε.

This covers: Q with 0 or 2 or 4 pieces in (1,2). The hard case is when Q has 1, 3, ... (odd number of) pieces in (1,2).

**Partial coverage**: This gives A ≥ 1 when:
- Even count + min(R)=1 (1-piece uncut) + EVEN number of Q-pieces in (1,2).

This requires more casework but could be combined with other arguments.

---

## Candidate techniques

1. **Symmetric difference / measure-theoretic approach**: A(Q∪R) = measure(S_Q △ S_R). Prove this ≥ 1 using the integral constraint ∫(N_Q - N_R)dx = 1 plus the step-function structure.

2. **Dyadic-interval analysis**: Track the contribution to A(Q∪R) from each dyadic interval [2^{k-1}, 2^k) of G_{n-1}'s structure. Show at least one interval contributes ≥ 1 (or they collectively sum ≥ 1).

3. **Equal-pair cancellation + self-similar induction**: If the largest G_{n-1} piece 2^{n-1} appears in both Q (after some cuts) and R, cancel to get a smaller LL sub-instance.

4. **Budget-tracking with strengthened IH**: Track (t, cuts_R) explicitly in the induction, using A(R) ≥ A_min(n, cuts_R) with A_min > 1 when cuts_R < n-1.

---

## Cheap-kill candidates

- **b ≥ 1 case**: max(Q) ≥ 2^{n-1}+1 → A(Q∪R) ≥ b ≥ 1 directly (contributes ~42% of n=3 configs). **Write as a separate sub-lemma to reduce scope of remaining gap.**

- **Parity + all-large**: Lemma P (certified) covers odd-count + all-pieces ≥ 1 (~17% more).

- **A(Q)=0 case**: Already handled (b=0 sub-case in LL-partial: when A(Q)=0, A(Q∪R) ≥ A(R) ≥ 1).

Together, these cheap kills reduce the open gap to: max(Q) ∈ (2^{n-1}, 2^{n-1}+1) with b ∈ (0,1), PLUS max(Q) ≤ 2^{n-1} with count even and Q-pieces potentially small.

---

## Knowledge-base entries to use

- **Invariants & monovariants**: For the integral invariant ∫(N_Q - N_R)dx = 1.
- **Direct proof / induction**: The geometric induction itself; strengthened IH is the key technique.
- **Pigeonhole / extremal**: For finding a dyadic interval that contributes ≥ 1 to the symmetric difference.
- **Double counting**: The integral identity sum(Q) - sum(R) = 1 = ∫(N_Q - N_R)dx relates to the A formula.

---

## Analogous past problems (cruxes)

The crux corpus was not queried in detail for this round (time constraints), but the relevant subtopics are:
- combinatorics / `games-and-strategy` (measure games)
- combinatorics / `invariants-and-monovariants` (the A-invariant)
- combinatorics / `induction-and-construction` (the geometric self-similar structure)

These are already the foundations of existing approaches. No better analogy was found through structural exploration.

---

## Prior progress

- **CERTIFIED**: LL t=0 (Case 1), LL t=1 (single cut), upper bound Regime A (shadow), extremal framework, Lemma P, greedy-odd-index, alt-sum-integral.
- **OPEN SHARED GAP**: LL t≥2 with A(Q)>0. True numerically for n=3 (all 7680 configs at step 1/6), n=4 (1363 G_3 refinements × Q grid). Minimum = 1 always. Tight cases fully characterized above.

---

## Dead ends (do not retry)

- **Merge-decomposition bound b + |a - A(R)| ≥ 1**: INSUFFICIENT. 34/286 configs (n=3 grid) fail this bound while true A ≥ 1. Already recorded.
- **Parity Lemma P alone**: Only covers ~17% of configs (odd count + all pieces ≥ 1). Even-count cases with all pieces ≥ 1 are NOT covered.
- **Monotonicity of cuts on Q**: More Q-cuts can DECREASE A (not monotone). Cannot peel one Q-cut and apply IH directly.
- **Potential-decrease greedy XY (for upper bound)**: Recorded dead-end, do not revisit.
- **"A(Q) ≥ A(R)+1 always"**: FALSE.
- **b≥1 as the sole bypass**: b = 0 in many tight cases (max(Q) = 2^{n-1} exactly). Need separate argument.

---

## Small-case / intuition notes

**VERIFIED** (by computation):
- n=3, t=2, all (Q,R) with Q partitioning 8 into 3 parts and R refining G_2 with ≤1 cut, step 1/6: min A(Q∪R) = 1. Tight cases include Q=[3,3,2]/R={1,2,2,2} (count 7=ODD, Lemma P applies) and Q=[4,2,2]/R=G_2 (count 6=EVEN, Lemma P fails, b=0).

- n=4, t=2, Q partitioning 16 into 3 parts (step 1/3), R refining G_3 with ≤2 cuts (step 1/3): min A(Q∪R) = 1. Tight cases: Q=[6,5,5]/R={6,2,2,2,2,1} (count 9=ODD, Lemma P applies) and Q=[6,6,4]/R={4,4,4,2,1} (count 8=EVEN, Lemma P fails).

**CONJECTURE** (not proved):
- The symmetric difference S_Q △ S_R always contains a "unit interval" [a, a+1) for some a ∈ [0, 2^{n-1}) from the dyadic structure of G_{n-1}. In tight cases this is literally [0,1) or [1,2).
- Equal-pair cancellation always reduces Q∪R to a smaller sub-instance of the same LL claim.
- measure(S_Q △ S_R) ≥ 1 is equivalent to LL, and might follow from a deeper structural argument about the interplay of G_{n-1}'s dyadic levels with Q's partition structure.

**KEY INVARIANT** (VERIFIED): sum(Q) - sum(R) = 2^n - (2^n-1) = 1 always. This is ∫₀^{2^{n-1}} (N_Q - N_R)dx = 1. The symmetric difference measure is the A quantity; the integral being 1 gives no direct lower bound on measure{N_Q+N_R odd} without further structure.

**STRUCTURAL INSIGHT FOR THE OUTLINER**: The cleanest potential approach is a THREE-WAY CASE SPLIT:
1. max(Q) ≥ 2^{n-1}+1: b ≥ 1, easy.
2. max(Q) ≤ 2^{n-1}, count odd, all pieces ≥ 1: Lemma P.
3. max(Q) ≤ 2^{n-1}, count even (OR some piece < 1): Need a new argument targeting the SPECIFIC DYADIC INTERVAL [2^{j-1}, 2^j) of G_{n-1} that ends up in S_Q △ S_R.

For case 3: the MOST PROMISING DIRECTION is the "unit interval in [1,2)" argument (Opening 6 above), which works when the 1-piece of G_{n-1} is uncut and Q has an even number of pieces in (1,2). The remaining sub-sub-case (1-piece cut or Q has odd count of pieces in (1,2)) requires further analysis.
