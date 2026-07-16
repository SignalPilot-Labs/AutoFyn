## imo-2026-03

Context: answer c(n)=2^n/(2^{n+1}−1) CONFIRMED. Certified imports available to every slug:
Lemma G (greedy=odd-index, val=(T+A)/2), Lemma M0 (A=measure{N odd}), Lemma M (merge:
A(X∪Y)=A(X)+A(Y)−2B), single-cut flip, LL t=1 (single cut), Regime A shadow (val=A_1≤c(n)),
Lemma P (odd count + all pieces ≥1 ⇒ A≥1), extremal framework (upper ⇐ S1, LL-independent).
The lower bound is COMPLETE except **Lemma LL, t≥2, A(Q)>0** (3-round plateau). The upper bound
is COMPLETE except Regimes B (A_1<1/2) and C (A_1>c(n)). Every slug below is a whole attempt at
c(n) importing the above; the slugs differ in their distinctive route to the OPEN gap.

Notation for LL: Q partitions 2^n into t+1≥3 positive parts, A(Q)>0; R refines G_{n−1}={1,…,2^{n−1}}
with A(R)≥1 and M:=max(R)≤2^{n−1}; total cuts t+(|R|−n)≤n. S_Q={x:N_Q odd}, S_R={x:N_R odd}.
By Lemma M, **A(Q∪R)=measure(S_Q △ S_R)**; goal is measure(S_Q △ S_R)≥1.

---

geometric-selfsimilar: advance
Target: c(n)=2^n/(2^{n+1}−1) — Liu Bang can guarantee ≥c(n) and Xiang Yu can hold him to ≤c(n).
Technique: Lemma-G reduction + geometric self-similar induction; THIS ROUND advance the UPPER bound
Regime B (A_1<1/2) — the closest independent deliverable (per R4 report, n=2 essentially done).
Skeleton (Regime B, the build target; rest of approach already partial/certified):
  1. n=2 Regime B (m=3, A_1<1/2), full formalization — by two exhaustive sub-cases:
     · B1 (A_1 ≥ 1−c(2)=3/7): XY one cut of A_1 at A_2 → pieces {A_2,A_2,A_1−A_2,A_3}. Since
       A_1−A_2<A_3≤A_2 (because A_1−A_2<½−A_2≤A_3), sorted [A_2,A_2,A_3,A_1−A_2], val=A_2+A_3=1−A_1≤4/7.
     · B2 (A_1<3/7): XY two cuts — A_1 at ε (small), A_3 at A_3/2. The paired A_3/2's are even
       everywhere (invisible to A); ε cancels; val=A_1+A_3/2≤(3A_1+1)/4≤4/7 (using A_3≤(1−A_1)/2,
       A_1<3/7). — by Lemma G + Lemma M0 parity accounting.
  2. General-n Regime B induction (m pieces, A_1<1/2) — by the same B1/B2 split at threshold 1−c(n):
     · B1 (A_1≥1−c(n)): one cut of A_1 at A_2 ⇒ val=1−A_1≤c(n); sorted-order lemma for m>3 pieces.
     · B2 (A_1<1−c(n)): ≥2 cuts, recurse on the (n−1)-cut sub-instance; base = n=2 B2.
Key lemmas (claim + mechanism):
  - Regime B1: val=1−A_1≤c(n) whenever A_1≥1−c(n) — because cutting the max at A_2 makes A_2 the
    doubled top, and the median-level sum of the sorted list is exactly 1−A_1 (Lemma G on the
    explicit sorted order, which needs A_1−A_2<A_3 to place the residual last).
  - Regime B2: val=A_1+A_m/2 — because halving the smallest piece contributes an even pair (A-invisible)
    and the ε-cut of A_1 cancels; then A_1+A_m/2≤(1+(m−1)A_1)/m·… ≤c(n) via A_m≤(1−A_1)/(m−1).
Open gaps: general-n B1 sorted-order casework for m>3; general-n B2 recursion + the algebraic bound
  A_1+A_m/2≤c(n) for A_1<1−c(n) at general m; Regime C (A_1>c(n)) remains open (not this round's target).
  LL t≥2 lower-bound gap remains (attacked in the two new slugs below).
Cases to cover: B1 vs B2 at each level; within B1 the sorted position of A_1−A_2 vs A_3,…,A_m.
Watch out for: the overlap B=0 claim in B2 must be checked, not asserted — the two small S-intervals
  [0,ε) and [A_m/2−ε,A_m/2) of the paired cut can only touch [0,ε), and A_2>ε keeps them clear of the
  upper S-interval; verify the ε's cancel exactly. Also m<n+1 (fewer pieces than cuts) is a free sub-case.

---

ll-dyadic-symdiff: new  (BYPASS of the a/b merge split — mandate 1 & 3)
Target: c(n)=2^n/(2^{n+1}−1), full claim; distinctive content = close the lower-bound gap LL t≥2 by a
  DIRECT structural bound on measure(S_Q △ S_R), never using the a/b two-sided merge decomposition or
  the peel-one-Q-cut induction (both recorded dead ends).
Technique: three-way case split on the structure of Q relative to the dyadic scale 2^{n−1}, proving
  measure(S_Q △ S_R)≥1 in each. Spine = pigeonhole on a single dyadic unit interval + Lemma P.
Skeleton:
  1. Reduce LL to measure(S_Q △ S_R)≥1 — by Lemma M (A(Q∪R)=A(Q)+A(R)−2B=measure(S_Q△S_R)). [import]
  2. CASE 1 — max(Q) ≥ 2^{n−1}+1 (b:=max(Q)−2^{n−1}≥1): S_Q ⊇ [2^{n−1},max(Q)) while S_R⊆[0,2^{n−1}),
     so these are disjoint and measure(S_Q\S_R) ≥ b ≥ 1. DONE. — by direct interval disjointness.
     [VALIDATED this round: 8310/8310 n=3 configs, A≥1.]
  3. CASE 2 — max(Q) ≤ 2^{n−1} AND total final piece count |Q|+|R| ODD, all pieces ≥1: Lemma P gives
     A(Q∪R)≥min piece ≥1. DONE. — by certified Lemma P. [import]
  4. CASE 3 — max(Q) ≤ 2^{n−1}, count EVEN (or some piece <1): the residual. Target a single dyadic unit
     interval [2^{j−1},2^{j}) inherited from G_{n−1} that lies entirely in S_Q △ S_R.
     · Sub-3a (1-piece of G_{n−1} uncut, |R| even, Q has an even # of pieces in (1,2)): N_R odd on [1,2)
       (drops from |R| to |R|−1 at x=1), N_Q even on [1,2) ⇒ N_{Q∪R} odd on all of [1,2) ⇒ [1,2)⊆S_{Q∪R},
       measure ≥1. — by parity bookkeeping at the dyadic breakpoint x=1.
     · Sub-3b (residual of 3a): the OPEN part of this slug — 1-piece cut, OR odd # of Q-pieces in (1,2).
Key lemmas (claim + mechanism):
  - Dyadic-interval lemma (Case 3 general form, CONJECTURE→to prove): for Q partitioning 2^n with
    max(Q)≤2^{n−1} and R a valid G_{n−1}-refinement, some dyadic level [2^{j−1},2^j) satisfies
    N_Q+N_R odd throughout it — because the invariant ∫(N_Q−N_R)=sum(Q)−sum(R)=1 (odd) forces a
    parity mismatch that, given G_{n−1}'s alternating dyadic S_R structure, localizes to one full level.
  - Case-1 disjointness — because S_R⊆[0,M)⊆[0,2^{n−1}) and S_Q covers [2^{n−1},max(Q)) whenever a
    single Q-part exceeds 2^{n−1} (at most one can, since ΣQ=2^n).
Open gaps: Sub-3b — the even-count residual where no single dyadic level is forced by the cheap parity
  move. [VALIDATED this round: naive even-count [1,2) test covers only 6348/13041 — genuinely partial,
  a real gap, NOT a closure.] This is the crux the slug must crack: prove the Dyadic-interval lemma, or a
  weaker "the mismatch mass is ≥1 across levels" summed bound.
Cases to cover: Case 1 / Case 2 / Case 3 (3a done, 3b open) — exhaustive by (max(Q) vs 2^{n−1}+1) then
  (count parity) then (1-piece cut? # Q-pieces in (1,2) parity).
Watch out for: the invariant ∫(N_Q−N_R)=1 does NOT by itself force measure(S_Q△S_R)≥1 (report Opening 4
  caveat: even step functions integrating to 1 exist) — the G_{n−1} dyadic structure is essential and
  must be used explicitly in the Dyadic-interval lemma; don't hand-wave "integral 1 ⇒ measure 1".

---

ll-inclusion-gap: new  (FRONTAL alternative for LL t≥2 — second viable way to fill the same gap)
Target: c(n)=2^n/(2^{n+1}−1), full claim; distinctive content = close LL t≥2 by splitting on the
  inclusion S_Q⊆S_R vs not, a different mechanism from ll-dyadic-symdiff.
Technique: two-case split — INC-GAP (containment ⇒ A(R)≥A(Q)+1) + SYM-DIFF (non-containment ⇒
  compensating mass ≥1). Spine = a gap/integrality argument from G_{n−1}'s dyadic breakpoints.
Skeleton:
  1. A(Q∪R)=measure(S_Q△S_R) [import Lemma M]. Split on whether S_Q⊆S_R.
  2. SUB-CASE B1 (S_Q⊆S_R, i.e. B=A(Q)): then A(Q∪R)=A(R)−A(Q); reduce LL to **A(R)≥A(Q)+1**.
     · S_Q⊆S_R⊆S_{G_{n−1}} forces Q's pieces to align with G_{n−1}'s dyadic breakpoints — e.g. for
       n=3, S_Q⊆[0,1)∪[2,4) forces q_min≤1, second≥2, giving A(Q)≤A(G_2)−1. Generalize via the
       dyadic breakpoint structure of S_{G_{n−1}}. — by an integrality/gap argument on Q's parts.
  3. SUB-CASE B2 (S_Q⊄S_R): ∃ mass in S_Q\S_R. Show measure(S_Q\S_R)+measure(S_R\S_Q)≥1 using that any
     "miss" of S_Q against S_R's dyadic-alternating structure forces a compensating full sub-interval
     of S_R\S_Q at the next dyadic scale. — by the dyadic-scale alignment cost of two S-structures.
Key lemmas (claim + mechanism):
  - INC-GAP: S_Q⊆S_R (valid refinement, total-cut constraint) ⇒ A(R)≥A(Q)+1 — because containment
    pins each Q-part into an S_{G_{n−1}} dyadic band, and ΣQ=2^n then caps A(Q) at A(G_{n−1})−1 while
    A(R)≥A(G_{n−1})−(cuts slack); the total-cut constraint t+cuts_R≤n is ESSENTIAL (fails without it —
    R={4,2,½,½} counterexample). [VERIFIED n=3,4, 0 violations by frontal explorer.]
  - SYM-DIFF: S_Q⊄S_R ⇒ measure(S_Q△S_R)≥1 — because the minimum "alignment shift" between a t-interval
    S_Q and G_{n−1}'s dyadic S_R is one full unit (tight cases are shifts by exactly 1, giving 4 pieces
    of measure ½ summing to 1).
Open gaps: the general-n proof of INC-GAP (the n=3 integrality argument must be lifted to arbitrary
  dyadic depth); the SYM-DIFF alignment-cost bound (verified true, no general proof yet).
Cases to cover: B1 (containment) vs B2 (non-containment) — exhaustive.
Watch out for: INC-GAP is FALSE without the total-cut constraint (frontal report) — the proof must
  consume the budget t+cuts_R≤n, not just "R refines G_{n−1}". The three tight "flavors" (S_Q⊆S_R with
  A(R)−A(Q)=1; A(Q)=A(R) with 4 half-intervals; disjoint) must all land ≥1.

---

extremal-smoothing: revise  (breadth on the LL-INDEPENDENT upper-bound route)
Target: c(n)=2^n/(2^{n+1}−1), full claim via the maximin/extremal upper bound (no per-config XY
  strategy), reducing the WHOLE upper bound to S1 (already certified as LL-independent).
Technique: replace the disproven "V globally concave ⇒ stationary=max" (dead end R3) with a
  **quasiconcavity** probe: show every super-level set {A∈Δ : V(A)≥v} is convex, so the unique interior
  critical structure at G_n is the global max.
Skeleton:
  1. V continuous on compact simplex Δ, max attained; V(G_n)=c(n) (replica). [import certified framework]
  2. NEW: test/prove V is quasiconcave on Δ — super-level sets convex ⇒ unique maximizer.
  3. Identify G_n as the maximizer via the first-order/exchange condition compatible with quasiconcavity.
Key lemmas (claim + mechanism):
  - Quasiconcavity of V — because V(A)=½(1+min_{XY} A(final)) and the inner min over XY responses of a
    piecewise-linear A(final) is a min of linear pieces (concave per cell); IF the cell structure is
    convexity-compatible, super-level sets are convex. [MUST be numerically checked first — NOT yet
    verified; if super-level sets are non-convex this route dies fast, which is itself useful signal.]
Open gaps: quasiconcavity is UNVERIFIED (upper-bound explorer flagged it as unchecked); the whole slug
  hinges on it. S1 has been stuck 3 rounds via other mechanisms.
Cases to cover: none (analytic).
Watch out for: this is a LONG-SHOT probe (S1 is a 3-round plateau) — its first deliverable is a bounded
  numeric check of super-level-set convexity for n=2,3; only invest in a proof if that passes. Do NOT
  re-table global concavity (disproven R3).

---

Recommended build-set priority (for the outline-reviewer): (1) geometric-selfsimilar [advance — the
concrete independent Regime-B gain], (2) ll-dyadic-symdiff [the mandated LL bypass], (3) ll-inclusion-gap
[second viable LL route]. extremal-smoothing revise is a lower-priority breadth probe; include only if
build capacity allows. All four keep the population broad across both bounds.
