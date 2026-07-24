## imo-2026-06

type-alphabet-counting-bound: new
Target: the problem's actual claim (∃ T,L with a_{n+T}=a_n+L for all n), attacked via
  closing hypothesis H2 (absorption-chain termination) inside the certified Master
  Conditional Theorem (H1=FAH + H2=termination ⟹ full periodicity, `n1-periodicity-
  reconciliation` §2). This approach's scope is explicitly H2 only; H1/FAH is untouched
  (17+ confirmed-dead mechanisms; 3 consecutive fresh-framing sweeps, rounds 13/15/17,
  found nothing — do not re-attempt H1 here).
Technique: combinatorial pigeonhole on the TYPE-ALPHABET SIZE |𝒫'(S)| (a set-size
  quantity, bounded by 2^{|S|}-1) as a monovariant for the number of absorption ROUNDS,
  instead of the index-based quantities N(S)/M_B that round 16 proved non-constructive
  (`lemmas/binary-refinement-and-threshold-recursion.md`, Proposition 3). This is the
  round-17 H2-lens explorer's flagged "genuinely different, untried angle" (opening 6).
Skeleton:
  1. Recall: Termination Criterion Lemma — the absorption chain S_0⊆S_1⊆... terminates
     iff (N(S_k))_k is bounded — by `lemmas/termination-criterion-lemma.md`.
  2. Recall: Binary Refinement Lemma — adjoining one prime to S splits each
     S-persistent type into ≤2 S'-persistent types — by
     `lemmas/binary-refinement-and-threshold-recursion.md`.
  3. NEW key step: instead of asking "is N(S_k) bounded" (an index, proven
     non-constructive to bound via M_B), ask "does the absorption PROCESS itself run
     for only finitely many rounds k, as counted by k, not by the index N(S_k)?" — these
     are logically different questions: boundedness of the round-COUNT k is a priori a
     weaker requirement than boundedness of the threshold VALUES N(S_k) (a bounded
     number of rounds does not require each round's threshold to be small, only that
     rounds stop happening). Verify carefully whether "chain stabilizes at some finite
     k_0" (finitely many DISTINCT S_k, i.e., eventually S_{k_0}=S_{k_0+1}=...) is
     actually equivalent to the Termination Criterion Lemma's boundedness statement, or
     a genuinely different/weaker target — this equivalence-check is itself an open
     gap the builder must resolve FIRST, since if it is not equivalent, this whole
     branch may (like round 15's "logically distinct object" finding for H2 vs FAH)
     open real new room.
  4. If step 3 confirms a genuinely weaker target, attack it via: since |𝒫'(S_k)| is
     bounded by 2^{|S_k|}-1 and (by the recruitment-corollary of the Generalized
     Bounded Witness Lemma, `lemmas/generalized-bounded-witness-lemma.md`) each round
     that actually recruits a NEW prime does so in response to a specific
     currently-unresolved disjoint-base-type pair, bound the total number of rounds
     by the total number of base-type pairs |𝒫(Q)|·(|𝒫(Q)|-1)/2 (finite, since 𝒫(Q) is
     finite by Persistent-Type Pigeonhole) PROVIDED each round permanently resolves at
     least one pair and no round can "unresolve" a previously-resolved pair — the
     latter is exactly the content of the already-certified Monotonicity of Resolution
     Lemma (`lemmas/monotonicity-of-resolution.md`). State this explicitly as the
     candidate Round-Count Finiteness Lemma.
  5. Honestly flag: step 4's mechanism is the SAME machinery `covering-system-
     construction` already has for gap (†)/FAH (H1) itself — if the round-count bound
     for H2's absorption chain reduces, on inspection, to literally the same
     "recruit primes for base-type pairs" process, this approach may turn out to be
     H1-equivalent in disguise, not H2-specific. The builder's FIRST task (before any
     other work) is to determine, precisely, whether the absorption chain's rounds
     (indexed by k, growing S_k to absorb early exceptional indices) are the SAME
     rounds as FAH's recruitment rounds (growing S₀ to resolve disjoint-type pairs) —
     per round 15's certified finding these were shown to be logically DISTINCT
     objects (N(S) measures onset-of-persistence timing; FAH is about intersection).
     If genuinely distinct, redo step 4's bound using ONLY H2-native quantities (not
     borrowing FAH's pair-resolution count).
Key lemmas (claim + mechanism):
  - Round-Count Finiteness Lemma (candidate, NOT yet proved): the absorption chain has
    only finitely many DISTINCT stages k — because each stage that changes S_k does so
    to resolve a specific structural deficiency, and the pool of possible deficiencies
    is drawn from a finite alphabet (𝒫'(S) bounded by 2^{|S|}-1, or the pair-count
    above) — mechanism to be nailed down per step 3/5.
Open gaps: whether "finitely many rounds" is a genuinely weaker/different target than
  "N(S_k) bounded" (step 3, must be resolved first, could kill the whole approach if
  they turn out equivalent to the already-non-constructive M_B question); whether the
  round-count bound is H2-native or secretly reduces to H1/FAH (step 5).
Cases to cover: none (this is a single structural claim, not casework).
Watch out for: the round-16 M_B non-constructivity trap — re-deriving a disguised
  version of M_B under new notation would not be progress; the builder must show the
  new quantity is DEMONSTRABLY different (e.g. bounded by a finite alphabet size
  independent of magnitude) before claiming novelty.

self-absorbing-by-construction: new
Target: the problem's actual claim, attacked via a SUFFICIENT structural condition
  that trivializes H2 for a broad, concretely-describable sub-case (mirroring how
  `even-a1-full-periodicity-theorem` trivialized H1 for 2|a_1) — explicitly a
  restricted/partial theorem, not a general resolution of H2.
Technique: direct construction — force self-absorption by DEFINITION rather than by
  discovering it, using the finiteness already certified in the Finite Core Theorem.
  Motivated by the round-17 H2-lens explorer's fresh numeric finding: on 9/9 resolvable
  seeds (|Q|≤4), the absorption chain terminates IMMEDIATELY at round 0 with S_0=Q
  itself already self-absorbing (N(S_0)=0) — strong evidence a simple sufficient
  condition exists, though not yet a proof.
Skeleton:
  1. Recall Finite Core Theorem: an explicit finite S built from finitely many witness
     terms a_{m_1},...,a_{m_r} (r ≤ |𝒫(Q)|), each with a fixed finite index — by
     `lemmas/finite-core-theorem.md`.
  2. Define S_0' := S ∪ Q ∪ ⋃_{j=1}^{M} P(a_j), where M := max(m_1,...,m_r) (the
     largest witness index used to build S). S_0' is finite (finite union of finite
     sets) and ⊇ Q.
  3. Key claim (Self-Absorption-by-Construction Lemma): S_0' is self-absorbing with
     N(S_0') ≤ M — i.e., EVERY index j ≤ M automatically has P(a_j) ⊆ S_0' (true by
     construction, step 2), so the only work needed is to verify the Extended
     Persistent-Type Pigeonhole's exceptional-index threshold for S_0' does not exceed
     M — i.e. that no index j > M is an exception under S_0'. This is the genuine open
     step: does enlarging S to include ALL early factorizations (not just the
     Finite Core Theorem's targeted witness primes) actually push the pigeonhole
     threshold down to ≤ M, or can it push it UP (a new, larger exceptional index
     appearing precisely because S_0' is bigger)? Must be checked, not assumed — this
     is exactly the phenomenon the round-16 Binary Refinement Lemma's non-monotone
     threshold recursion warns about.
  4. If step 3's claim holds (even only "generically" — e.g. whenever the witness
     terms a_{m_1},...,a_{m_r} pairwise share enough structure that no NEW exceptional
     index is created), state and prove the precise sufficient condition, and package
     it as a restricted theorem: "if [condition X holds for a_1], then H2 holds with
     S* = S_0', unconditionally" — leaving H1 (FAH at S_0') as the only remaining
     hypothesis for that sub-case (same shape as how 2|a_1 removed H1 but left H2 open
     in round 16 — this is the mirror-image partial result).
  5. If step 3's claim genuinely fails in general (a concrete counterexample where
     S_0' creates a NEW, larger exception), report this as an honest negative finding
     — do not force a claim, per memory rule (round 16): a clean negative result on
     this sub-question is still valuable, since it would show self-absorption is not
     simply "throw in more early data" and sharpen what a real H2 proof needs.
Key lemmas (claim + mechanism):
  - Self-Absorption-by-Construction Lemma (candidate): S_0' as built in step 2 is
    self-absorbing with threshold ≤ M — because every j ≤ M is absorbed by
    CONSTRUCTION (trivial), and the only nontrivial content is whether j > M can still
    exceptionally fail to have persistent extended type w.r.t. S_0' — must be checked
    computationally first (mandatory pre-build check, 3-5 seeds including a_1=175,
    4807, 11305) before any general claim is written.
Open gaps: whether step 3's threshold-preservation claim is true at all (mandatory
  numeric pre-check); if true only generically, the precise sufficient condition X.
Cases to cover: none beyond the generic/exceptional dichotomy in step 5.
Watch out for: do not conflate "S_0' self-absorbing" with "S_0' resolves FAH" — this
  approach targets H2 only; H1 (FAH at S_0') stays a separate, still-open hypothesis
  even if this lemma succeeds.

n1-periodicity-reconciliation: advance
Target: the problem's actual claim, via the certified Master Conditional Theorem
  (H1=FAH + H2=absorption-chain termination ⟹ full periodicity from n=1).
Technique: consolidation/audit — no new mechanism attempted on H1 or H2 this round
  (matching this round's 3-consecutive-plateau finding on H1, and the two new H2
  attempts above already covering fresh H2 ground).
Skeleton (this round's task):
  1. Produce a single, polished "Best Currently Provable Statement" section merging
     (a) the fully unconditional, certified 2|a_1 subfamily theorem (T=1, L=2, from
     n=1, `lemmas/even-seed-literal-periodicity-theorem.md`) and (b) the Master
     Conditional Theorem's reduction of the general case to exactly H1+H2 — stated as
     one coherent deliverable, explicit about what is proved outright vs. what remains
     conditional.
  2. Re-audit the full citation chain (Free Facts → Persistent-Type Pigeonhole →
     Finite Core Theorem → Extended Persistent-Type Pigeonhole → Self-Absorbing Core
     Theorem → Universal Early Intersection Lemma → Literal n=1 Periodicity Theorem →
     Monotonicity of Resolution) end to end ONE more time, specifically checking for
     any step that might have been affected by round 16's Binary Refinement / Threshold
     Recursion findings (these were added AFTER the chain was first assembled — confirm
     no citation in the existing chain implicitly assumed constructivity of N(S)/M_B
     that round 16 later disproved).
  3. If the two new H2 approaches above (type-alphabet-counting-bound,
     self-absorbing-by-construction) produce a genuine partial result this round,
     integrate it as a THIRD disclosed sub-case in the writeup (mirroring how 2|a_1
     was integrated for H1) rather than waiting for a future round.
Key lemmas: none new required — pure audit/consolidation of already-certified content.
Open gaps: H1 (FAH) and H2 (termination) remain the two named open hypotheses; this
  task does not attempt to close either, only to verify and present the reduction
  honestly as the run's hedge deliverable if neither closes further.
Cases to cover: none.
Watch out for: do not let "writeup" polish drift into overclaiming — the Status must
  stay explicitly `partial` for the general case; only the 2|a_1 subfamily is `solved`.

covering-system-construction: advance
Target: the problem's actual claim, via the standing recruitment-process/FAH route.
Technique: unchanged (recruitment-process induction toward Joint FAH at S_0).
Skeleton (this round's task — bookkeeping only, no new FAH mechanism dispatched):
  1. Kept live for ranking continuity as the highest-Elo approach; no new mechanism is
     assigned this round given 3 consecutive fresh-framing sweeps (rounds 13, 15, 17)
     found nothing new for FAH and the restricted-family lens (round 17) confirmed no
     shortcut exists via seed structure either.
  2. If builder time remains after the three approaches above, the ONE remaining
     concrete fallback target flagged since round 12 is still available: attack the
     single-divisor-class question in the |F''|=2, multiplicity-1 case directly (the
     Reduced-Alphabet Corollary's `|D_bad(q*)|=1` collapse on the standard hard seeds,
     a_1=4807, 11305) as a bespoke fixed-integer divisibility-persistence question —
     but this is optional/low-priority, not the main task this round.
Key lemmas: none new required this round.
Open gaps: Joint FAH itself (18 confirmed-dead mechanisms so far); the bespoke
  |F''|=2 single-divisor-class question is unattempted as a standalone target.
Cases to cover: none.
Watch out for: do not spend a full build slot re-deriving already-dead mechanisms;
  if the bespoke single-divisor-class sub-task is attempted, it must be a genuinely
  new argument, not a restatement of any of the 18 dead mechanisms.
