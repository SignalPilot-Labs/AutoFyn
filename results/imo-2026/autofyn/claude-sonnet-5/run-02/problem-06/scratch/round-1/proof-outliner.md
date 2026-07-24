## imo-2026-06

Population is fresh (round 1): four new approaches, all genuinely different top-level
framings for the whole claim, sharing only two "free" building blocks that any correct
proof must use (proved outright, not gaps): (i) for n ≥ 2, gcd(a_n,a_1) > 1 so P(a_n)
meets the fixed finite set Q = P(a_1); (ii) once a finite load-bearing prime set S ⊇ Q
and modulus L = ∏S are secured, a CRT + deterministic-cyclic-map + pigeonhole argument
gives eventual periodicity with period T = |{good residues mod L}| and step L (routine,
not a gap). All four approaches differ in HOW they attack the genuinely hard step —
proving S is finite — using four distinct mechanisms: extremal set theory, explicit
constructive induction, analytic/counting contradiction, and combinatorial charging.
None of the four fully closes this step yet; that is expected for round 1 on an IMO P6.

---

hypergraph-transversal: new
Target: exist T,L with a_{n+T}=a_n+L for all n (the full claim).
Technique: intersecting-family / hypergraph transversal — track the antichain of
inclusion-minimal prime-signatures M_n; argue M_n stabilizes via a monovariant
potential; finish with CRT + finite cyclic pigeonhole.
Skeleton:
  1. gcd(a_n,a_1)>1 for n≥2 — by hypothesis with i=1.
  2. M_n = minimal antichain of {P(a_1),...,P(a_n)}; a candidate m is legal iff P(m)
     hits every set in M_n — by superset-closure of "shares a prime."
  3. [GAP] finiteness of the eventual prime support S with M_n stabilizing to a fixed
     antichain M ⊆ 2^S — proposed via a potential Φ_n on M_n, incomplete.
  4. CRT: legality of m for n≥n_0 depends only on m mod L, L=∏S — by knowledge_base.md
     "Modular arithmetic, CRT."
  5. Deterministic cyclic map on the finite good-residue set G mod L ⟹ period
     T=|G|, step L, for n≥n_0 — by pigeonhole/determinism.
  6. [GAP] extend the periodic identity back to n=1 (problem demands it for every n,
     not just eventually) — finite check, not yet done.
Key lemmas:
  - Q=P(a_1) finite and meets every later term — because i=1 case of the hypothesis.
  - Minimal-antichain transversal equivalence — because hitting a subset's minimal
    elements hits all its supersets.
  - Finiteness of S — because (conjectured) a monovariant potential on antichain
    structure, combined with a density argument against infinite fresh-prime
    recruitment; NOT proved.
Open gaps: step 3 (finiteness of S, the true crux) and step 6 (n=1 boundary).
Cases to cover: |Q|=1 (trivial), |Q|≥2 (genuinely hard).
Watch out for: conflating "M_n has few elements" with "M_n's elements use few primes."

covering-system-construction: new
Target: same full claim.
Technique: explicit constructive strong induction — build S and L one prime at a time
via an algorithmic recruitment rule with quantitative gap bounds, contrasting with the
abstract extraction of hypergraph-transversal.
Skeleton:
  1. Free fact Q=P(a_1) finite — same as above.
  2. Build S_0=Q, S_1,... by adjoining the smallest prime witnessing any
     "disjoint-Q-pattern pair" obstruction found in the greedy sequence so far.
  3. [GAP] termination of this recruitment process at a finite S_J — proposed via
     primorial growth (W_j≥2W_{j-1}) outpacing new-obstruction creation, needing a
     gap-length-vs-primorial-growth inequality (candidate tool: Bertrand's-postulate-
     style windowing) — not proved.
  4. CRT reduction + explicit computable n_0=n_0(J) — routine given step 3.
  5. Cyclic pigeonhole on good residues mod L=∏S — same finish mechanism as
     hypergraph-transversal but here n_0,T,L are (in principle) explicitly computable.
  6. [GAP] n=1 boundary, same caveat as hypergraph-transversal.
Key lemmas:
  - Free bound on Q — same mechanism.
  - Finite termination of core recruitment — because primorial growth per adjunction
    should outpace new obstruction creation IF a gap-bound inequality holds
    (unestablished).
  - CRT + cyclic pigeonhole finish — routine.
Open gaps: step 3 (the quantitative inequality) and step 6.
Cases to cover: |Q|=1, |Q|=2 (work out a_1=15,35 fully as template), |Q|≥3 (a_1=1001).
Watch out for: assuming "2 is always recruited first" without proof; separating
incidental primes (irrelevant) from load-bearing primes in S.

density-sieve-contradiction: new
Target: same full claim.
Technique: proof by contradiction using density/sieve counting (crux move borrowed
from aimo-0886's "boundedness via contradiction" pattern) — assume gaps are unbounded,
derive a counting contradiction; genuinely indirect/analytic vs. the two constructive
approaches above.
Skeleton:
  1. Free fact Q — same mechanism.
  2. Reduce target to: (a) gaps d_n bounded, (b) relevant primes confined to a finite S
     eventually — given both, finish via knowledge_base.md "Linear recurrences:
     eventually periodic mod m" (same CRT+pigeonhole mechanism as the other approaches).
  3. [GAP] gap-boundedness by contradiction: assume d_{n_j}→∞, sieve-count blocked
     integers in the window; the count needs an a priori cap on the number of distinct
     small primes among a_1,...,a_{n_j} without circularly re-invoking core finiteness —
     not resolved by raw Mertens-type estimate alone.
  4. Recommended sub-route: bound "blocking types" directly by |Q| (each a_i's
     Q-pattern is one of ≤2^|Q|-1 types; a candidate integer is blocked only by
     one of finitely many pattern-types), a combinatorial bound the builder should try
     BEFORE the raw analytic sieve estimate.
  5-6. Same CRT+pigeonhole finish and n=1-boundary caveat as the other approaches.
Key lemmas:
  - Free bound on Q — same mechanism.
  - Gap-boundedness by contradiction — because a sieve/density count of "good"
    integers in a window, once the working prime set is fixed, is positive-density;
    the missing, non-circular piece is capping the number of distinct load-bearing
    primes as a function of n.
  - CRT + pigeonhole finish — routine.
Open gaps: step 3/4 (gap-boundedness, non-circular) is the crux; step 6 n=1 boundary.
Cases to cover: |Q|=1 trivial; |Q|≥2 needs the sieve/blocking argument worked out for
a_1=15,35 as testbed first.
Watch out for: letting the "working prime set" implicitly grow with n while computing
a fixed-modulus density (invalidates the sieve bound); boundedness of gaps is weaker
than eventual strict periodicity — don't skip the pigeonhole upgrade step.

amortized-charging-budget: new
Target: same full claim.
Technique: amortized charging/accounting argument — assign each new load-bearing prime
recruitment a charge against a finite combinatorial budget (pairs/subsets of the fixed
set Q), bounding total recruitment events combinatorially rather than via extremal set
theory, explicit induction, or analytic density.
Skeleton:
  1. Free fact Q — same mechanism.
  2. Define "load-bearing" precisely: p becomes load-bearing when it is the unique
     necessary witness for some pair (i,j) not already covered by previously
     load-bearing primes.
  3. [GAP] finite total charge: charge each recruitment event to a distinct pair of
     Q-subsets (A,B); claim reconciliation is permanent (once witnessed, that
     pattern-pair never needs a new prime again) — the "permanence" subtlety (does a
     Q-pattern match truly force reuse of the SAME witness prime for the greedy
     sequence specifically?) is not proved.
  4. Fallback: charge to static minimal Q-patterns directly (bounded by 2^|Q|-1) if the
     dynamic pair-charging in step 3 can't be closed rigorously.
  5-6. Same CRT+pigeonhole finish and n=1-boundary caveat as the other approaches.
Key lemmas:
  - Free bound on Q — same mechanism.
  - Finite total recruitment via charging — because each recruitment event is charged
    to a distinct finite combinatorial object (subset-pair of Q), PROVIDED
    reconciliation is permanent; permanence not yet established.
  - CRT + pigeonhole finish — routine.
Open gaps: step 3 permanence claim (the crux, numerically testable against a_1=1001's
{2,7,11,13} recruitment data); step 6 n=1 boundary.
Cases to cover: |Q|=1 trivial; |Q|=2 (a_1=15) as permanence sanity check; |Q|≥3
(a_1=1001, which excludes 3 from S — check charging bound doesn't assume small |Q|).
Watch out for: conflating "a prime witnesses a pair once" with "it is the unique
witness forever" — relax the charging rule to "charge to the FIRST witness found,
reuse of ANY already-load-bearing prime doesn't create a new event" for robustness;
if this argument reduces to the same underlying inequality as density-sieve-
contradiction's step 3/4, flag the convergence rather than presenting them as fully
independent.

---

Notes for the outline-reviewer: all four approaches share two proved building blocks
(Q finiteness from i=1; CRT+pigeonhole finish given S finite) and diverge entirely on
the one genuinely hard step (proving S — the eventual load-bearing prime set — is
finite). This is intentional per the dispatch: the population is deliberately spread
across four distinct mechanisms (extremal/hypergraph, explicit/constructive,
analytic/sieve, combinatorial/charging) attacking that one hard step, rather than one
mechanism tried four ways, to avoid the single-gap trap while still making the shared
"easy" scaffolding explicit so builders don't waste effort re-deriving it independently.
Recommend the build set include at least covering-system-construction and
density-sieve-contradiction first (most concrete/tractable sub-routes proposed:
Bertrand-style windowing and |Q|-bounded blocking-types respectively), with
hypergraph-transversal and amortized-charging-budget close behind as they both hinge on
subtler structural claims (potential-function stabilization, and reconciliation
permanence) that likely need the concrete |Q|=2 case (a_1=15) worked out numerically-
then-rigorously first, before generalizing.
