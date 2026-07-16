# imo-2026-03 — Lower-Bound Frontal Lens

## The Gap in Precise Terms

Lemma LL, Case t≥2, A(Q)>0. Q partitions 2^n into t+1≥3 positive parts (A(Q)>0), R refines G_{n-1}={1,2,...,2^{n-1}} with A(R)≥1 and max(R)≤2^{n-1}, total cuts t+(|R|-n)≤n. Need: A(Q∪R)=A(Q)+A(R)-2B ≥ 1.

## Finding 1: The 34/286 LL-Partial Failures Are NOT Near-1 Cases

**VERIFIED** (n=3 grid, step=1/4, 28 failures with R_list): All 28 cases where LL-partial bound (b+|a-A(R)|) equals 0 have true A(Q∪R) ≥ 2. They are NOT hard — they fail the bound because the bound computes b=0 and |A(Q)-A(R)|=0, but the true overlap B is 0 (disjoint S_Q and S_R), giving A(Q∪R)=A(Q)+A(R)≥1+1=2.

**Crucial correction to prior report**: The 34 failing cases are large-A(Q∪R) configurations (≥2), not near-1. The LL-partial bound is merely too conservative there (gives 0 when truth ≥ 2).

## Finding 2: The ACTUAL Tight Cases (A(Q∪R)=1) Come in Two Flavors

Computed for n=3, valid total-cuts constraint:

**Flavor A** (handled by LL-partial): max(Q)>2^{n-1} so b>0. Example: Q={5,2,1}, R=G_2={4,2,1}: b=1, a=2, A(R)=3, bound=1+|2-3|=0... wait, bound=b+|a-A(R)|=1+|2-3|=2. Actually LL-partial handles these correctly.

**Flavor B** (case b=0, A(Q)=A(R)): Q={4,5/2,3/2}, R=G_2. A(Q)=3=A(R)=3, B=5/2, A(Q∪R)=1. LL-partial gives b+|a-A(R)|=0+|3-3|=0 — fails! But A(Q∪R)=1.

S_Q=[0,3/2)∪[5/2,4), S_R=[0,1)∪[2,4). Symmetric difference: S_Q\S_R=[1,3/2) (measure 1/2) and S_R\S_Q=[2,5/2) (measure 1/2). Total=1. Exactly tight.

**Flavor C** (S_Q⊆S_R, B=A(Q)): Q={4,3,1}, R=G_2. A(Q)=2, A(R)=3, B=2, A(Q∪R)=1. Here A(R)-A(Q)=1 exactly.

## Finding 3: Inclusion Gap Lemma (VERIFIED for n=3,4)

**CLAIM** (verified 0 violations, n=3 grid step=1/4 with valid cuts; n=4 t=1,2 grid step=1/2, 2700 configs):

*When S_Q ⊆ S_R (i.e., B = A(Q)) under the valid total-cuts constraint, A(R) ≥ A(Q) + 1.*

Consequence: A(Q∪R) = A(R) - A(Q) ≥ 1. Exactly tight at Q={4,3,1}, R=G_2 (A(R)-A(Q)=1).

**Why this holds** (structural argument for n=3): S_Q ⊆ S_{G_2}=[0,1)∪[2,4) forces q3≤1, q2≥2, q1≤4 (otherwise N_Q is odd above max(G_2)=4). With q1+q2+q3=8, these constraints give A(Q)=8-2q2≤8-6=2=A(G_2)-1. So A(G_2)-A(Q)≥1. For refinements R of G_2 with A(R)≥1: when S_Q⊆S_R, measure(S_R\S_Q) ≥ 1 (CONJECTURE for general n — verified but not yet proved).

**Why it fails without the cuts constraint** (found violations for t=3 with extra cuts on G_{n-1}): R={4,2,1/2,1/2} (2 cuts on G_2) with S_Q⊆S_R gives A(R)-A(Q)<1. The total-cuts constraint is essential.

## Finding 4: Formula A(Q∪R) = A(Q_A∪R) + 2(q3-F)

For t=2, Q={q1,q2,q3}, form Q_A={q1,q2+q3} (the t=1 merged version).

**Formula** (VERIFIED, 0 errors): A(Q∪R) = A(Q_A∪R) + 2(q3-F)

where F = measure(([0,q3)∪[q2,q2+q3)) ∩ S_{Q_A∪R}) is the measure of the "flip region" intersected with the S-set of the merged config.

The flip region [0,q3)∪[q2,q2+q3) is exactly the region where N changes parity when splitting q2+q3→{q2,q3}.

**From t=1 proof**: A(Q_A∪R)≥1 always (already proved). So A(Q∪R)=A(Q_A∪R)+2(q3-F)≥1 iff A(Q_A∪R)≥1+2(F-q3)^+.

When A(Q_A∪R)=1: verified F=0 always (flip region disjoint from S_{Q_A∪R}), giving A(Q∪R)=1+2q3>1.
When A(Q_A∪R)>1: the slack A(Q_A∪R)-1≥2(F-q3)^+ is needed.

This induction-on-t approach is **not circular for the t=2 step** (reduces to the certified t=1 case), but the inequality A(Q_A∪R)≥1+2(F-q3)^+ is itself LL restated — circular for general t.

## Finding 5: Candidate New Tools

**Tool 1: Two-Stage Proof** (most promising for t=2 specifically)

Split into Sub-Case B1 (S_Q⊆S_R) and Sub-Case B2 (S_Q⊄S_R):
- B1: Use Inclusion Gap Lemma → A(R)-A(Q)≥1. Need a PROOF of "S_Q⊆S_R ⟹ A(R)≥A(Q)+1 for valid refinements R."
- B2: S_Q⊄S_R means ∃x∈S_Q\S_R. measure(S_Q\S_R)>0. Claim: measure(S_Q△S_R)≥1. Sub-claim: measure(S_Q\S_R)+measure(S_R\S_Q)≥1, which holds if measure(S_R\S_Q)≥1-measure(S_Q\S_R). This sub-claim links A(R)-B to A(Q)-B+A(R)-A(Q)+... still needs work.

**Tool 2: Exploit the specific structure of S_R for G_{n-1} refinements**

S_{G_{n-1}} is an alternating union of dyadic intervals [2^{j},2^{j+1}) for j≡n (mod 2) plus [0,1) if n odd. This "dyadic alternating" structure means measure(S_R ∩ I) for any interval I has strong constraints from the piece sizes.

Concretely: for any interval I⊆[0,2^{n-1}) of length L, if I∩S_{G_{n-1}}≠∅ and I∩complement(S_{G_{n-1}})≠∅, then one of the two has measure ≥ something related to the dyadic scale.

This could be formalized as: for refinements R of G_{n-1}, the S_R-"density" in any interval is controlled by the dyadic structure.

**Tool 3: Strengthened IH**

Instead of just A(R)≥1, strengthen to: for any interval [a,b]⊆[0,2^{n-1}), measure(S_R∩[a,b])≤b-a-1/2^{n-1} OR measure(S_R∩[a,b])≥1/2^{n-1}. This would let us bound B-A(Q)/2 in terms of the structure.

CONJECTURE (not verified): The right strengthened IH is: for R refining G_{n-1} with ≤m cuts, A(R)≥1 AND measure(S_R\I)≥1 for the specific interval I=S_Q∩[0,2^{n-1}) when S_Q⊆S_{G_{n-1}}. This would directly give A(R)-A(Q)≥1 in Sub-Case B1.

**Tool 4: Directly bound measure(S_Q△S_R) using the symmetric difference structure**

A(Q∪R) = measure(S_Q△S_R). The alternating structure of both S_Q (from a t-cut partition) and S_R (from G_{n-1} refinement) means their symmetric difference has a minimum measure determined by the "alignment cost" of two such structures.

For t=2: S_Q has 2 intervals (generically). S_R has 2 intervals (for G_{n-1} uncut, which is the hardest case). Their symmetric difference has 4 intervals in the tight case (each of measure 1/2). Total = 1. The minimum is always attained when the intervals of S_Q and S_R are "almost aligned" but shifted by 1 unit.

## Smallest Failing Configuration (Precise Numbers)

**Tight case for LL, Sub-case t=2, A(QUR)=1** (VERIFIED):
- n=3, Q={4, 3, 1} (q1=4=2^{n-1}, q2=3, q3=1). A(Q)=2.
- R=G_2={4,2,1} (uncut). A(R)=3.
- S_Q=[0,1)∪[3,4). S_R=[0,1)∪[2,4).
- B=measure(S_Q∩S_R)=1+1=2. A(QUR)=2+3-4=1. 
- Observation: S_Q⊆S_R (since [0,1)⊆[0,1) and [3,4)⊆[2,4)). A(R)-A(Q)=1. Tight!

**Tight case for Flavor B** (VERIFIED):
- n=3, Q={4, 5/2, 3/2}. A(Q)=3.
- R=G_2={4,2,1}. A(R)=3.
- S_Q=[0,3/2)∪[5/2,4). S_R=[0,1)∪[2,4).
- B=5/2. A(QUR)=1. LL-partial gives 0. S_Q∩S_R=[0,1)∪[5/2,4), measure=5/2.
- S_Q△S_R=[1,3/2)∪[2,5/2), each piece measure 1/2, total 1.

## Candidate Lemma for the Outliner

**Lemma INC-GAP** (Inclusion Gap): If S_Q⊆S_R where Q is a (t+1)-part partition of 2^n with t≥1 and R is a refinement of G_{n-1} by ≤n-t cuts (A(R)≥1, max(R)≤2^{n-1}), then A(R)≥A(Q)+1 and hence A(Q∪R)≥1.

Proof outline: S_Q⊆S_R requires specific constraints on Q's pieces relative to G_{n-1}'s dyadic breakpoints. These force A(Q)≤A(R)-1. [Not yet fully proved for general n, but verified n=3,4.]

**Lemma SYM-DIFF** (Complementary case): If S_Q⊄S_R (the "miss" case), then measure(S_Q△S_R)≥1. [CONJECTURE — not verified independently but implied by LL holding with 0 violations.]

**Approach for outliner**: Split the proof into INC-GAP (S_Q⊆S_R) and SYM-DIFF (S_Q⊄S_R). The first is a gap/integrality argument using G_{n-1}'s structure; the second uses that any "miss" in S_Q∩S_R forces compensating mass in S_R\S_Q.

## Dead Ends Confirmed

- Merge-decomposition alone: insufficient (34/286 failures, confirmed).
- Parity Lemma P: only odd-piece-count + all≥1 configs, misses most cases.
- B≤A(Q)/2 for t=2: FALSE (many counterexamples: B=5/2 with A(Q)=3, so B=5A(Q)/6 > A(Q)/2).
- Claim "B>A(Q)/2 ⟹ A(R)≥A(Q)+1": FALSE without cuts constraint (counterexamples exist).
- Induction t→t-1 (peeling one Q-cut) naively: circular (reduces LL to LL).
- Formula A(QUR)=A(Q_AuR)+2(q3-F) for t=2 reduction: correct formula, but proving the inequality A(Q_AuR)≥1+2(F-q3) is again Lemma LL. Useful only if combined with more structure.

## Knowledge-Base Entries to Use

- **Invariants & monovariants**: the "alternating structure" of S_R is invariant under dyadic refinement in a strong sense.
- **Pigeonhole**: the 2 intervals of S_{G_{n-1}} partition [0,2^{n-1}) into "odd" and "even" regions; any S_Q spanning both forces a contribution to S_Q△S_R.
- **Constructive / incremental**: the INC-GAP proof can be done by tracking how S_Q must "fit inside" S_R.
- **Double counting**: A(Q∪R) = measure(S_Q△S_R); the two pieces S_Q\S_R and S_R\S_Q can be bounded separately.

## Analogous Past Problems (Cruxes)

- **aimo-0019** (combinatorics/invariants + games): Dyadic covering game on [0,1]. Crux: frontier advance charged against pieces absorbed, B maintains invariant "ink spent ≤ 3*progress." Analogy: the "dyadic alternating structure" of S_R is similar; both problems use geometric sums of dyadic-length pieces.
- **aimo-0117** (combinatorics/games): Geometric (dyadic) assignment — "the single largest value strictly exceeds the sum of all others." Directly analogous to G_n's dominance property and the "inclusion gap."

## Distinct Openings for the Outliner

1. **Two-Case + Inclusion Gap**: Prove INC-GAP (S_Q⊆S_R case, A(R)≥A(Q)+1 via G_{n-1} structure) + SYM-DIFF (S_Q⊄S_R case, measure of "miss" ≥ compensating slack). Most direct.

2. **Strengthened IH path**: Replace "A(R)≥1" with "A(R)≥1 AND measure(S_R\S_Q)≥1 when S_Q⊆S_{G_{n-1}}." Carries the information through the induction and closes INC-GAP directly.

3. **Convexity/rearrangement**: View A(Q∪R) as a bilinear function of indicator functions of S_Q and S_R; minimize over all valid Q and R simultaneously. The minimum is at Q=tight and R=G_{n-1} (empirically verified). Then prove minimality by a local perturbation argument.

4. **Parity + Minimum-piece argument**: For the specific t=2 case, track the total count of pieces (= t+1+|R|) and the minimum piece size to invoke Lemma P in a sub-case.
