## imo-2026-06

renormalization-induction-on-seed: revise
Target: eventual periodicity a_{n+T}=a_n+L (whole problem), now sharpened
via a new concrete sub-target — the "p=3 Near-Total Lock Theorem": for
every a_1 with min R(a_1)=3 and 5∤a_1, a_n = a_1+3(n-1) for all n≥2
(T=1, L=3, transient of length 1). This is a genuinely new, non-parity
mechanism (all parity mechanisms are exhausted: Odd-Anchor Lemma +
a_1=45 weak-fallback counterexample, both certified). It mirrors the
already-solved Even-Seed Universal Lock Theorem's proof shape one level
up: p=2 has 0 non-trivial in-between candidates (free via Minimum Gap
Lemma), p=3 has exactly 1 non-trivial in-between candidate (a_n+2) to
rule out.
Technique: direct extension of the certified General-a2-Formula and
Third-Term-Dichotomy-Lemma machinery to a full permanent-lock induction
for p=3 specifically, rather than the general omega(a_1)-induction.
Skeleton:
  1. a_2 = a_1+3 — by general-a2-formula.md (p=3).
  2. Key Necessity Lemma (new): if 3 | a_i for i=1..n, then a_{n+1}≠a_n+3
     requires gcd(a_n+2,a_1)>1 — because a_n+2≡2 mod 3 (3∤ it), and
     a_n+1 is free-excluded by the Minimum Gap Lemma, so a_n+2 is the
     only intervening candidate, and its legality against i=1 forces a
     shared prime with a_1 other than 3. Reproves the prime-power case
     a_1=3^k as a free corollary.
  3. Key Sufficiency-side gap (open, the hard step): for R(a_1)={3}∪S,
     5∉S, show the necessary condition of step 2 is never realized
     simultaneously against ALL intermediate locked terms, for any q∈S
     with q≥7 — while it IS realized for q=5 (the a_1=15 exception).
     Candidate distinguishing invariant to test: q<2p (p=3) i.e. q=5 is
     the unique prime below 2p=6 other than p itself.
  4. Exceptional family (5|a_1): characterize beyond the single
     hand-verified a_1=15 instance (check at least one more, e.g. a_1=45
     or 75, for consistency before generalizing).
Key lemmas (claim + mechanism):
  - Necessity Lemma — because 3 never divides a_n+2 under the locked
    hypothesis, so index-1 legality must route through another prime of
    R(a_1).
  - Sufficiency non-collision claim (OPEN) — conjectured combinatorial
    achievability of the compound gcd-survival condition only for q=5,
    never q≥7, needs an explicit residue-class or size argument.
Open gaps: step 3 (hard direction) and step 4 (exceptional family beyond
a_1=15) are both unproved.
Cases to cover: R(a_1)={3} (closed, corollary); R(a_1)={3,q}, q≥7 prime
(target); ≥3-prime seeds with 3∈R(a_1), 5∉R(a_1) (untested by explorer,
flag explicitly); 5|a_1 (exceptional family).
Watch out for: do not assume the p=11 "no proximity threshold" refutation
(explorer finding) automatically kills the q<2p candidate for p=3 — that
refutation was about a different mechanism (blanket proximity for a
different prime p); re-derive from raw p=3 data, don't transfer blindly.

state-compactness-pigeonhole: revise
Target: eventual periodicity (whole problem), via the Generalized
Multiple-of-r Realization Lemma — extends this approach's own certified
multiple-of-r-realization.md (only covers r | rad(a_1)) to a genuinely
recruited prime r ∈ Nec\R(a_1), using the Nec-finiteness explorer's
CRT-positive-density opening, explicitly guarded against the circularity
trap the explorer itself flagged (density among integers ≠ realization by
the greedy sequence).
Technique: CRT/inclusion-exclusion density argument + an explicit
quantitative bridge to the bounded-gap-constrained greedy sequence
(not a bare existence/density citation).
Skeleton:
  1. Fix r ∈ Nec\R(a_1) witnessing pair (a_i,a_j); let E be the finite
     contamination set from contamination-dichotomy-and-reduction.md.
  2. CRT-density step (free): multiples of r avoiding all primes in E
     have density ∏_{s∈E}(1-1/s)>0 — standard inclusion-exclusion.
  3. Bridging step (OPEN, the real gap): show the greedy sequence, forced
     to advance by ≤ rad(a1) each step (bounded-gap-via-rad-a1.md /
     sharpened-bounded-gap-lemma.md), must hit a clean multiple of r at a
     bounded index — NOT merely that clean multiples exist with positive
     density among all integers.
  4. Assembly (OPEN, separate sub-gap): repeat step 1-3 for each element
     of Nec\R(a_1) in recruitment order, checking exclusion sets stay
     compatible across primes, to conclude Q_min is self-sufficient.
Key lemmas: CRT-density-of-clean-multiples (free, elementary); Generalized
Realization Lemma (steps 1-3, OPEN, the hard part).
Open gaps: step 3 (density-to-realization bridge) and step 4 (assembly)
are both unproved.
Cases to cover: none beyond general prime r; MUST sanity-check any
explicit bound produced in step 3 against the a1=35409 outlier (witness
index 95 for prime 23, from this round's Nec-finiteness explorer) — if
the bound is smaller than 95 for that instance, the argument is wrong.
Watch out for: do not present CRT-density alone as a finish — this is
exactly the circularity trap contamination-dichotomy-and-reduction.md
already flagged; the write-up must include the explicit bridging step.

active-set-stabilization: revise
Target: eventual periodicity (whole problem), via a direct
counting/second-moment bound on |Nec| globally (not per-prime) — a
genuinely different mechanism from state-compactness-pigeonhole's
per-prime CRT-density route, both attacking the same Nec-finiteness gap
(per the population rule: split two different mechanisms for one shared
gap across two different files).
Technique: growth bound (linear term size from bounded-gap-via-rad-a1.md)
+ a double-counting/averaging argument (Zsigmondy-flavored inspiration
only, does not transplant literally) bounding the number of distinct
primes that can ever witness a singleton pairwise intersection.
Skeleton:
  1. a_N = O(N) — free, from the fixed constant gap bound rad(a1).
  2. Counting step (OPEN, the hard mechanism): derive an explicit bound
     f(N) on the number of distinct Nec-witnessing primes among the
     first N terms, and show f(N) does not grow without bound as
     N→∞ (i.e., Nec itself, not just its restriction to a finite prefix,
     is finite) — a bound merely growing with N is NOT sufficient.
  3. Assembly (OPEN): combine with Nec-Necessity Lemma + Contamination
     Dichotomy's self-sufficiency criterion to conclude Q_min is
     self-sufficient.
Key lemmas: Growth bound (free); Distinct-witness counting bound f(N)
(OPEN, untried, promise explicitly unclear per the explorer — proposed,
not validated).
Open gaps: step 2 (deriving f(N) and proving it doesn't diverge) is the
central open gap of this revision; step 3 unattempted.
Cases to cover: none, uniform argument.
Watch out for: do not conflate "bounded count up to index N" (trivial,
grows with N) with "bounded total count over all N" (the actual target);
verify this counting mechanism does not silently collapse into the
already-refuted Redundancy Growth Lemma (ρ(n)≥2 per-index argument) under
a different name — this must be a genuinely aggregate/global argument.

covering-system-construction-exchange: new
Target: eventual periodicity (whole problem), via construction-first +
exchange/local-optimality, inverting every other live approach's
existence-via-pigeonhole/minimality/induction order of attack. Opened per
CLAUDE.md's plateau-break rule after the plateau-break explorer proved
scalar-difference-pigeonhole/majorization structurally cannot progress
without already knowing (T,L)/Q.
Technique: adaptive construction of a candidate prime set Q* (grown one
obstruction at a time, licensed by minimality of the greedy rule) plus
a first-deviation/minimality contradiction argument.
Mandatory cheap-kill check performed this round (by the outliner,
Python exact-integer simulation, 60 terms each): true Nec for a1=35 is
{2,3,5,7}, for a1=99 is {2,3,5,11}, for a1=375 is {2,3,5,7,19} — the
recruit 19 for a1=375 (rad=15) has NO evident closed-form threshold in
rad(a1) alone, which is a genuine warning sign (any naive density-
threshold construction would just re-derive jacobsthal-covering-bound's
already-deprioritized Λ^(K) mechanism under a new name). The approach is
kept open ONLY conditioned on attempting the adaptive/exchange framing
(not a closed-form guess).
Skeleton:
  1. Adaptive construction of Q*_k, starting from R(a1), adjoining the
     smallest prime resolving each already-observed (bounded) obstruction
     — licensed by soundness-and-exact-correctness.md.
  2. Termination Lemma (OPEN, central gap, structurally equivalent to
     jacobsthal-covering-bound's un-derived K(a1) boundedness): show the
     adaptive process reaches a finite, permanently self-sufficient Q*.
  3. Exchange/local-optimality finish (conditional on step 2): first
     deviation from the Q*-induced periodic pattern contradicts
     minimality of the greedy choice.
Key lemmas: adaptive well-definedness (free, each step responds only to
already-observed obstructions); Termination Lemma (OPEN — no mechanism
found yet, must be genuinely new or this collapses to the dead
jacobsthal mechanism); exchange contradiction (conditional, standard
minimal-witness shape, cf. aimo-0077/aimo-0514, though neither
transplants directly since both need an a priori finite state space that
here is exactly what step 2 must supply).
Open gaps: step 2 is the load-bearing, completely open gap, honestly
equivalent in difficulty to every other approach's central gap.
Cases to cover: none identified yet; if step 2 needs casework by
omega(a1) or min R(a1), must be made explicit.
Watch out for: if after one build attempt no genuinely new termination
mechanism is found (i.e. it only reproduces jacobsthal-covering-bound's
"no a priori K(a1) bound" finding), mark RETHINK rather than keep
grinding a re-skinned dead mechanism.

scalar-difference-pigeonhole / scalar-difference-majorization: deprioritize (no build this round)
Per the plateau-break explorer's independent re-verification (confirmed
by this outliner): both forks have proved, across rounds 5-6, that every
route to close their own syndeticity/majorization gap reduces to "first
know Q/(T,L)" — a genuine structural dead end for this framing, matching
CLAUDE.md's plateau-break criterion (3 rounds, same wall from different
angles). Round-7 deprioritization notes appended to both approach files;
certified lemmas remain reusable. Not recommended for this round's build
set; revisit only if a genuinely new substitute-divisibility idea (the
aimo-0680-style Mechanism B) surfaces.

## Nominations for the outline-reviewer
Recommended build set: renormalization-induction-on-seed,
state-compactness-pigeonhole, active-set-stabilization,
covering-system-construction-exchange. Recommend NOT building
scalar-difference-pigeonhole or scalar-difference-majorization this round
(deprioritized, structural dead end proved by the plateau-break explorer)
— final call on skipping them left to the outline-reviewer per the
"reviewer always runs, ranks every round" rule, but this outliner's
assessment is that grinding either further without a new substitute-fact
idea would not add signal.
