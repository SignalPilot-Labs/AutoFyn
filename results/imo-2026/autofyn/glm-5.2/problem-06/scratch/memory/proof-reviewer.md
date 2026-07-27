# proof-reviewer role memory

ALWAYS: verify greedy-sequence / transversal-cycle claims with python3+sympy before certifying (the conditional theorem for IMO 2026 P6 was confirmed exactly on a1=15,30,429; the a1=30 antichain-correction was confirmed). (round 1)

ALWAYS: when multiple approaches share the same conditional pipeline, judge the shared lemmas once and credit the verified-milestone to the cleanest statement; mark the others partial unless they close an additional gap. (round 1)

NEVER: accept a "promote new prime grows density" argument without checking the monotonicity direction — for transversal valid sets, adding a minimal support SHRINKS the valid set, so density does not grow with |P|. (round 1)

ALWAYS: recompute load-bearing computational claims (mtp monotonicity, gap bounds, common⊆P(a1), specific seed values like a1=175 mtp=21) on the builder's seeds PLUS a few adversarial ones — they have checked out every round so far but a single wrong number (e.g. α's "47 promotions" for a1=273, actually 57) can hide in a non-load-bearing illustration (round 2).

ALWAYS: when a lemma's FORMAL STATEMENT is correct but its REMARKS overclaim (e.g. freeze-lock calling a one-direction implication an "equivalence"), certify the statement and strike/qualify the remark rather than rejecting the whole lemma (round 2).

ALWAYS: trace the new-minimal argument in freeze-type lemmas through the edge case P(a_{n+1}) = P(a_j) for j ≤ n (equal support already present) — this is the case most likely to be glossed; it resolves via "then P(a_{n+1})∈M_n which contains p, contradiction" (round 2).

NEVER: accept "by symmetry / similarly / it follows / clearly" in a transversal-family-shrinking argument — the direction (subset vs superset of transversals under refinement) is easy to get backwards; demand the explicit per-member case check (round 2).

WATCH: the freeze regime (F) is NOT just the trivial even/prime-power collapses — odd composite seeds like a1=273=3·7·13 land in regime (F) (a prime factor persists common, greedy locks to gap p, AP hits p^k). Do not dismiss the freeze branch as vacuous (round 2).

NEVER: accept "W1 (witness carries a small prime) ⟹ mtp bounded" — it is FALSE. W1 bounds only one factor of the witness product; the witness may carry a large cofactor (counterfamily T*={5,97}, p*=5: W1 holds, product 485>30=primorial(5)). The bound mtp≤primorial(p*) needs SPT (every MINIMAL carries a small prime, making the small-prime SET a transversal), not W1. Hunt for this conflation in any SPT-based approach (round 129).

NEVER: accept "SPT closes the wall (M finite)" — SPT bounds mtp (GAP-1) but NOT P_ess (GAP-3). The abstract antichain {{2,q}:q>p* prime} is pairwise-intersecting, satisfies SPT (min=2≤p*), yet has unbounded P_ess. SPT alone does not force finiteness; a crash-eviction/Cov mechanism is additionally needed (round 129).

ALWAYS: verify a self-refutation is honest (not a cover) by reproducing a counterexample seed computationally AND confirming the narrowing-to-broader-wall is real (the refuted lemma's conclusion genuinely fails, and the replacement wall is a superset). pstar's Lemma C-ref (a1=35 terminal Cov={5}⊊P(a1)={5,7}) checked out (round 129).

ALWAYS: check whether the minimals are pairwise-intersecting before accepting a "straggler meets {2,p} ⟹ p∈straggler" argument — it holds because each minimal M∈M_n equals some P(a_k) (it is a minimal MEMBER of F_n), so pairwise-intersection of the terms transfers directly to the minimals. Verified 0 violations on 8 seeds (round 129).

ALWAYS: when a builder claims an equality-promotion (a_{n+1}=mtp-multiple) is dominated, REFUTE it — the mtp-witness T* is a transversal of M_n, NOT a member, so P(a_{n+1})⊇T* does NOT dominate (domination needs a member as subset). Equality-promotions are genuine new minimals. Verify T*∉M_n computationally (round 129).

NEVER: extract a lemma to lemmas/ just because run_state says it was "certified" — verify the file actually exists; common-primes-bounded and Sat-criterion were claimed certified r2 but had no lemma file until r129 extraction (round 129).

ALWAYS: for imo-2026-06, the large-prime descent's Piece A is the UNCONDITIONAL elementary form "$x$ appears $\iff \gcd(x,a_i)>1$ for every $\prec$-minimal $a_i<x$" (no-skip greedy + $\prec$-minimal set reduction). Do NOT cite the GAP-conditional `universal-membership-no-transient`/`transversal-residue-characterization` inside the descent — they define $L,V$ from $\mathcal M$ and would make the finiteness proof circular (round 130).
NEVER: claim $\prec$-minimal supports $=\mathcal M$ (both inclusions) for imo-2026-06 — Direction A (every $\prec$-minimal support $\in\mathcal M$) is FALSE (a1=30,429,273,210,46189,323,385: a later term appears with a strictly smaller support, subsuming an earlier $\prec$-minimal). Only Direction B ($\mathcal M\subseteq\{\prec\text{-minimal supports}\}$) is true, and it is the only direction the descent needs (round 130).
ALWAYS: when verifying a descent/induction proof empirically, test the witness CONSTRUCTION (does $q^k c$ land in $[a_1,a_n)$, rad-divide, appear earlier?), not just the conclusion — testing only the conclusion on seeds where large primes never appear (e.g. a1=46189, a1^2=2.1e9) gives a vacuous pass. Pick a seed with small $a_1^2$ threshold (a1=15, threshold 225) so hundreds of large-prime-carrying terms exercise the mechanism (round 130).
