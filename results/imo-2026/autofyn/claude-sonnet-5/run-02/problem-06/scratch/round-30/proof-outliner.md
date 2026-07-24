## imo-2026-06

a1-19q-subfamily-theorem: new
Target: the problem's actual claim (existence of T,L with a_{n+T}=a_n+L for
all n), restricted to the a_1 = 19q subfamily (q any prime > 19), proved
literally with T=1, L=19 from n=1.
Technique: direct instantiation of the certified p-uniform machinery
(Generalized K_0-Boundedness + gcd-difference Witness Lemma; Legendre
Sieve Gap Bound; Primorial Floor Bound; Universal Look-Back Witness
Identity r=1 corollary; Diagonal Characterization + First-Risk Theorem)
at p=19 — the identical 10/10-successful template used at p=3,5,7,11,13,17.
Skeleton:
  1. Copy the symbolic §0-§8 reduction verbatim from
     `a1-pq-subfamily-theorem.md`, substituting p=19: build the
     (p-2)x(p-1) = 17x18 = 306-cell (j,r) table via
     s_0(j,r) = j*r^{-1} mod 19, K_0(j,r) = 19+s_0(j,r) — by
     Generalized K_0-Boundedness Lemma.
  2. Close the r=1 column's k=0 layer unconditionally, for free, via the
     certified Universal Look-Back Witness Identity's r=1 corollary
     (gcd(N,a_n)=gcd(j,k+1), no per-q computation needed) — already proved
     general in `a1-pq-subfamily-theorem.md`.
  3. For every remaining (j,r,k) cell, find the sufficient-window
     threshold via the Legendre Sieve Gap Bound (g(M)<=2^ω(M)(ω(M)+1)) +
     Primorial Floor Bound (ω(M)=r ⟹ M>=(r+1)!), reducing to a finite
     below-threshold candidate set — mechanical scale-up, same bound
     shape as p=17's build.
  4. Resolve each below-threshold candidate via an explicit gcd witness;
     collect the residual genuine exceptions.
  5. Report the exceptional set explicitly: Bad(19) = {23, 29, 31, 37, 43,
     53, 73} (7 primes, all on the diagonal j=r, all with K_0=20=2^2*5,
     matching the Diagonal Characterization Lemma's prediction
     s_0(j,r)=1 ⟺ j=r) — verified by direct greedy simulation to q=20000
     (2254 primes, zero deviations beyond these 7).
  6. Prove each of the 7 diagonal exceptions rigorously (not just
     numerically) using the explorer's elementary closed-form argument:
     on the diagonal, s_0=1, K_0=20, and the Case-(b) window is the
     consecutive-integer interval {q+1,...,q+n_0-1} of length
     n_0-1=(q-r)/19-... — check parity (q odd ⟹ q+1 even ⟹ shares
     factor 2 with 20) for window length 1 (q=23,29,31,37: gives the
     "first representative in each diagonal residue class is bad" fact
     with zero casework), and mod-5 divisibility of the remaining window
     elements for length 2-3 windows (q=43,53: q+2≡0 mod 5; q=73: window
     {74,75,76}, 75=3·5^2). This turns the 7 hand-checks into one uniform
     2-paragraph elementary argument instead of 7 separate ad hoc checks.
  7. Conclude: for every prime q > 19, q ∉ Bad(19), the sequence starting
     at a_1=19q has literal T=1, L=19 periodicity from n=1 — same
     assembling argument (Literal n=1 Periodicity Theorem machinery,
     specialized here to not even need FAH/H1/H2 since p is prime and the
     construction is self-contained, exactly as in a1-5q/7q/11q/13q/17q).
Key lemmas (claim + mechanism):
  - Bad(19) = {23,29,31,37,43,53,73} exactly — because every one of the
    306 (j,r,k) cells outside these 7 is resolved either by the r=1
    corollary (free), the sieve/primorial threshold (finite check), or
    (on the diagonal) the elementary parity/mod-5 argument in step 6; the
    7 named primes are exactly where the diagonal window is small AND
    every element of the window shares a factor with K_0=20=2^2·5.
  - Diagonal exceptions always land at K_0=p+1 — because on the diagonal
    j=r, s_0(j,r)=1 identically (Diagonal Characterization Lemma), so
    K_0=p+s_0=p+1 by the Generalized K_0-Boundedness Lemma, independent
    of q.
Open gaps: the full 306-cell sieve/threshold closure for the ~299
non-diagonal cells is mechanical but must actually be carried out and
written up rigorously by the builder (not just asserted by analogy to
p=17); the 7 diagonal exceptions' rigorous elementary proof (step 6) must
be written out in full, not left as a numerical observation.
Cases to cover: r=1 (free via corollary); r≠1, diagonal (j=r, 7 named
exceptions); r≠1, non-diagonal (all resolved via sieve/threshold,
per-cell).
Watch out for: do not silently assume "matches p=17's pattern" in place of
actually re-deriving the p=19-specific sieve bound and gcd witnesses — per
the round-23/26 memory rule, only the *symbolic* machinery is p-uniform;
the specific integers (Bad(p), threshold table) must be freshly derived,
not copy-pasted. Also do not let the elementary parity/mod-5 argument
(step 6) silently claim to handle non-diagonal cells — it only applies to
the diagonal band's consecutive-integer window structure.

fah-counterexample-hunt: revise
Target: the problem's actual claim, attacked from the disprove side — a
genuinely different top-level target from all 30+ dead "prove FAH
directly" mechanisms. (If no counterexample is found even under this
sharper adversarial search, that is reported as further, more targeted,
corroborating evidence, not a proof — Status stays honestly `unsolved` on
this route unless a real counterexample or a real structural invariant is
found.)
Technique: two-pronged deliberate plateau-break, per the consolidation
explorer's own recommendation and the h1-fresh explorer's diagnosis that
"the only kind of mechanism not yet exhaustively refuted is a literally
conserved invariant, not a merely-bounded statistic":
  (a) Adversarial-seed search targeting the *implicit assumptions* of the
      already-certified positive machinery itself (Self-Absorbing Core
      Theorem's core-termination assumption; Universal Early Intersection
      Lemma's "pick m≠j in an infinite index set" step) rather than just
      re-running the same |Q|>=3/CRT-lopsided sweep as rounds 21-22.
  (b) A dedicated, first-ever search for an actual conserved (not merely
      bounded) invariant of the greedy recursion — distinct from every
      previously-tried monovariant/statistic (all of which were shown
      class-blind or non-monotone), because no explorer in 24 rounds has
      proposed even a *candidate* literally-conserved quantity.
Skeleton:
  1. Restate precisely what a genuine counterexample requires (per the
     approach file's own §1.3): either (i) an explicit seed with a
     structurally-proved permanent non-intersection of two disjoint
     extended-persistent types, or (ii) a rigorous structural argument —
     not a finite simulation window — showing some quantity stays
     invariant/partitioned forever.
  2. Prong (a): construct seeds deliberately designed so the core-closure
     process S_0 ⊆ S_1 ⊆ ... is forced to run through MANY absorption
     rounds before any candidate S* is even reached (e.g. seeds with 4-5
     small distinct prime factors chosen so each absorption round's forced
     new prime is itself small enough to trigger yet another round) — the
     goal is to probe whether S* itself might fail to stabilize (which
     would refute H2, not H1, but is a genuinely different failure mode
     never directly targeted by a counterexample-hunt before; prior hunts
     only tested S*-level FAH assuming S* already stabilized).
  3. For each such seed, run the direct literal-period detection tool
     (certified this workspace, round 21) to get an exact, not merely
     asymptotic, absorption-chain trace; report explicitly whether S_k
     stabilizes and at what k, and if it does, whether the resulting two
     largest disjoint base types show any sign of persistent imbalance.
  4. Prong (b): systematically enumerate candidate literally-conserved
     quantities distinct from all previously-refuted ones (which were all
     either counts/densities of occurrences, or size-of-core measures) —
     candidates to check first: (i) the multiset of *residues* a_n mod
     (each core prime) taken as a formal vector — is any single
     coordinate's parity/residue-class permanently fixed after core
     stabilization? (ii) an algebraic invariant of the *sequence of primes
     introduced* (e.g. does the order of first-appearance of core primes,
     as a permutation/sequence, satisfy any fixed recursive rule?). Test
     each candidate on 3-4 already-canonical seeds (4807, 11305, 187, 209)
     before any general claim.
  5. Report honestly: if (2)-(4) find nothing after genuine adversarial
     effort, record this as the sharpest available negative evidence to
     date (broader in scope — targeting H2's own core-stabilization
     assumption, not just H1's base-type intersection — than any prior
     round's counterexample hunt) and explicitly retire the "conserved
     invariant" search direction as exhausted if no candidate survives
     even a first plausibility check.
Key lemmas (claim + mechanism): none proved yet — this is a search, not a
proof; any genuine positive finding (a real counterexample, or a real
candidate invariant that survives step 4's check) is the deliverable.
Open gaps: everything — this is explicitly a disprove/discovery-oriented
approach, not a proof in progress.
Cases to cover: |Q|=2 (already exhaustively tested, do not re-run);
|Q|>=3/4/5 seeds (partially tested in round 21, extend); seeds engineered
specifically to stress S* stabilization (genuinely new this round, not
previously targeted).
Watch out for: per the approach file's own standing rule, a "no
counterexample found in N terms" result is NOT evidence of a proof and
must never be reported as one; and per the h1-fresh explorer's cheap-kill
note, any invariant candidate that only reads a count/density/statistic of
prior occurrences is pre-emptively dead (Ambient-Statistic Obstruction) —
do not waste builder time re-testing that shape, only genuinely different
formal objects (residue vectors, introduction-order permutations, etc.)
count as new.

a1-pq-subfamily-theorem: advance (low priority this round)
Target: the problem's actual claim, restricted to the general a_1=pq
subfamily (any odd prime p, any prime q>p, q outside a finite Bad(p)) —
literal T=1,L=p periodicity, uniform in p (not yet closed for general p).
Technique: same certified p-uniform machinery as above (Generalized
K_0-Boundedness, Legendre Sieve Gap Bound, Primorial Floor Bound,
Universal Look-Back Closed Form + r=1-Uniqueness Theorem).
Skeleton: unchanged from the certified round-28 state; no new angle was
found by any of this round's 3 explorers (consolidation explorer
confirmed both residual gaps are p-independent algebraic sub-questions,
not resolved by more per-p instances, and are not free/low-hanging).
Key lemmas: already certified — Universal Look-Back Closed Form,
Uniqueness of r=1 Theorem (both proved for ALL p, ALL r via the single
witness band j=p-1).
Open gaps (unchanged, both explicitly still open, do not force a fix this
round without a genuinely new idea):
  - general r≠1, k=0-layer closure (some band always fails to be
    unconditionally closed per the Uniqueness Theorem, but this does not
    by itself produce exceptions — still needs per-p sieve resolution or a
    genuinely new closed-form argument, neither found this round);
  - r=1, k>=1, gcd(k+1,j)>1 residual (untouched since round 27).
Cases to cover: none new this round.
Watch out for: do not spend a build slot trying to force either residual
gap closed without a concretely new idea — per this round's consolidation
audit, "extend to p=19/23" (a1-19q above) is the correct, honest way to
add certified content from this machinery right now, not a generalization
of the open p-uniform gaps. If a builder is assigned here, its only task
should be a light-touch housekeeping pass: append the 9 missing round
21-29 verdict entries to current.md's `## Approaches tried` section, and
update `## Current best` to name all 10 certified subfamily theorems
(2|a_1; a_1=p^k; a1-3q; a1-3q^2; a1-3q^3; a1-3aq a=1-5; a1-5q; a1-7q;
a1-11q; a1-13q; a1-17q), per the consolidation explorer's finding that
these two sections have drifted stale since round 20 — this should not
cost a full build slot on its own; fold it into whichever builder next
touches current.md (e.g. the a1-19q builder, once its own APPROVE is
recorded, or the proof-reviewer's own update pass).

Notes for the outline-reviewer: 3 live rival approaches proposed —
(1) a1-19q-subfamily-theorem is the near-certain 11th APPROVE (mechanical,
build-ready, matches 6/6 prior successful p-instantiations); (2)
fah-counterexample-hunt is the deliberate, CLAUDE.md-mandated plateau-break
after 24 consecutive plateau rounds on H1 — genuinely different top-level
target (disprove, not prove) and, within it, a genuinely new sub-target
(probe H2's own core-stabilization assumption, and hunt for a literally-
conserved invariant, neither previously attempted); (3) a1-pq-subfamily-
theorem is kept live but explicitly flagged low-priority/no-new-angle,
with its build slot (if any) restricted to housekeeping only, per the
explicit instruction not to force a residual-gap fix without genuine new
content. Recommended build set: a1-19q-subfamily-theorem,
fah-counterexample-hunt (both get full build effort); a1-pq-subfamily-
theorem only if a spare slot exists, restricted to the housekeeping task.
