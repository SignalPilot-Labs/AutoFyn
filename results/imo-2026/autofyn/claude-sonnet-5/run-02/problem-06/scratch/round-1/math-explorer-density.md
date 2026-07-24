## imo-2026-06 (lens: density / counting / extremal)

- Distinct openings (all reach the WHOLE claim, not a sub-lemma):
  1. **Intersecting-family + pigeonhole framing.** Let P(a_i) = set of primes dividing a_i.
     Because a_{n+1} is only accepted if gcd(a_{n+1},a_i)>1 for *every* i≤n, the sets
     {P(a_i)}_{i≥1} form an infinite family that is *pairwise intersecting by construction*
     (each new set meets all earlier ones, and induction gives all earlier pairs already
     meet). An infinite pairwise-intersecting family of finite sets over a countable ground
     set (here: primes) cannot avoid concentrating: fix P(a_1) (finite); every later P(a_i)
     must hit one of its |P(a_1)| elements, so by pigeonhole on this finite coloring some
     single prime p_1 divides infinitely many a_i. Iterating/refining this pigeonhole
     argument on the *residual* family (terms not hit by p_1) is a natural way to try to
     extract a small finite "hub set" S of primes that together intersect every a_i for i
     large — this is a counting/pigeonhole route to the finiteness-of-relevant-primes fact,
     avoiding the modular-covering-system framing entirely (no residue system is built by
     hand; the hub set is *extracted* from the sequence itself).
  2. **Density/sieve bound on gaps once a finite hub set is known.** If S = {p_1,...,p_k} is
     a finite set of primes such that every sufficiently early "problem" term (one whose
     prime set misses some p_j) is already resolved, then within any window of length
     P = p_1 p_2 ... p_k, inclusion–exclusion gives that a fixed positive density
     1 − ∏(1−1/p_i) of integers are divisible by at least one p_i in S; standard CRT sieve
     arguments (as in Bertrand's-postulate-style or Dirichlet-density style counting) then
     bound a_{n+1} − a_n ≤ P for n large. This is the piece of the KB's "divisor
     analysis / density" toolkit that applies directly and is the cheapest way to get
     **bounded gaps**, which is the real engine behind eventual periodicity.
  3. **Finite-state pigeonhole on (residue mod P, "recent window") once gaps are bounded.**
     Once gaps are bounded by some constant M and the relevant prime support is the fixed
     finite S, the "state" needed to determine a_{n+1} from a_n is essentially
     (a_n mod P, and which finitely many *exceptional early terms* still impose extra
     constraints). If, after finitely many terms, ALL constraints reduce to "a_{n+1} must
     be divisible by some prime of S compatible with a_n's own hub-membership", the process
     becomes a finite automaton on states = residues mod P (or mod 2P), and eventual
     periodicity follows by the pigeonhole principle on this finite state space (a state
     must repeat, and because the rule "pick smallest valid successor" is deterministic and
     depends only on the state, repetition of state forces repetition of the whole future
     gap-pattern). This is the natural finish once openings 1–2 are secured, and it is a
     genuinely different mechanism from a "prove modulus M works, verify by cases" covering
     construction — it is an extraction/pigeonhole argument, not a hand-built system.
  4. **Growth-rate / extremal counting cross-check.** a_n / n tends (numerically) to a
     constant c depending on the eventual hub set S (c = L/T in the periodic regime, i.e.
     the reciprocal of the density of "valid" integers). This gives an independent sanity
     check: once you conjecture the hub set S, predict c = P/(density of S-multiples in a
     period) and check it against a direct count of a_N/N for large N. Useful as a
     verification tool for the outliner/builder, not a proof step.

- Candidate technique(s): pigeonhole/extremal principle on an infinite pairwise-intersecting
  set family (KB "Pigeonhole / extremal principle", "Comparability/divisibility graphs"
  flavor), CRT + inclusion–exclusion sieve density bound (KB "Modular arithmetic, CRT",
  "Bertrand's postulate" as the template for "a prime/structured number exists in a bounded
  window"), finite-state pigeonhole to force eventual periodicity (KB "Linear recurrences:
  sequences are eventually periodic mod m" is the closest named KB entry — same shape of
  conclusion, worth citing even though the mechanism here is a custom finite automaton, not
  a linear recurrence).

- Cheap-kill candidates:
  - **Parity/hub split.** Numerically, once the sequence "locks in," essentially all terms
    are covered by either being even, or (among the odd ones) sharing one further fixed
    prime p* with all other odd terms — a 2-hub structure. Checking "is a_n even" is a cheap
    filter that immediately handles the (typically) majority of the pairwise-intersection
    burden; only the sparse odd subsequence needs the harder hub argument. Worth using as a
    first reduction in any approach.
  - **v_p / multiplicity count is not obviously useful here** (the problem is about which
    primes divide, not their exact power), so LTE / p-adic valuation tools are probably NOT
    the right hammer — flag this to avoid the outliner reaching for LTE by reflex.
  - **Size bound sanity check:** a_{n+1} − a_n ≤ (something like) the primorial of the
    currently-active hub primes is a cheap, checkable bound to test on any constructed hub
    set before trusting it.

- Knowledge-base entries to use: "Modular arithmetic, CRT" (§Number Theory), "Bertrand's
  postulate" (as the template for guaranteeing a witness in a bounded window via a
  structured density bound, not literally applicable but the right shape of argument),
  "Pigeonhole / extremal principle" and "Comparability / divisibility graphs" (§Combinatorics
  — treating {P(a_i)} as a hypergraph / intersecting family is exactly this KB entry's
  spirit), "Linear recurrences ... eventually periodic mod m" (§Number Theory, the closest
  named analogue of the target conclusion), "Constructive vs. existence" and
  "Invariants & monovariants" (§General Proof Methods — the eventual hub set / period is
  effectively an invariant that stabilizes).

- Analogous past problems (cruxes):
  - `aimo-0886` (ISL 2015 N7 analogue in the corpus, subtopic divisibility-and-gcd /
    sequences-and-recurrences): "a_{n+2m} | a_n + a_{n+m} for all n,m ⟹ sequence eventually
    periodic." Genuinely analogous in *shape of conclusion* (eventual periodicity of an
    integer sequence defined by a divisibility/gcd-type local rule) though the local rule
    itself is very different (linear divisibility vs. gcd-with-all-predecessors). Its crux
    moves worth adapting: (a) first prove **boundedness** of a natural auxiliary quantity
    (there: the values a_n themselves; here: the candidate gap sizes / prime support size)
    via a pigeonhole-on-a-hypothetical-unbounded-witness contradiction; (b) "Lemma 2": for a
    fixed divisor/prime d, the set of indices i with d | a_i forms a highly structured
    (there: arithmetic-progression) pattern — the analogue here would be: for a fixed hub
    prime p, the indices with p ∤ a_i are eventually confined to a bounded/structured set,
    which is essentially the finiteness-of-exceptions fact opening 1 needs. (c) Final step:
    once finitely many "moduli" d_s are known, take D = product of all of them and get the
    period directly — matches opening 3's "P = primorial of hub set" plan almost exactly.
    This is the strongest single analogy found; recommend the outliner skim its full
    solution (in `past_problems_database.json`, `problem_id = aimo-0886`) for the
    boundedness-via-contradiction technique even though the problem body differs.
  - No other corpus entry found that shares the specific "gcd with ALL predecessors"
    construction; searched `divisibility-and-gcd`, `sequences-and-recurrences`, `pigeonhole`
    subtopics under number_theory by keyword ("gcd", "smallest", "consecutive") in both
    corpus files — only `aimo-0503`, `aimo-0648`, `aimo-0678` matched "gcd + sequence"
    loosely and none construct a "smallest integer satisfying pairwise gcd with all
    predecessors" rule; they are not close enough to recommend as models.

- Prior progress: none — this is round 1, workspace is empty.

- Dead ends (do not retry): none recorded yet (no approaches exist to check).

- Small-case / intuition notes (all CONJECTURE from numerics, python `math.gcd`
  brute-force construction, verified for several starting values up to a1≤231 and
  n up to 2000):
  - a1 = 2, 5, 7, 6, 10, 30 (already pairwise non-coprime with all future multiples of a
    single prime, or a1 with only 2 prime factors both ≤ some small bound) all give
    IMMEDIATE period T=1 with L = a1's smallest prime factor (or a1/its structure);
    e.g. a1=2 ⟹ a_n=2n (T=1,L=2, all even); a1=6 ⟹ gaps all 2 (T=1,L=2); a1=7 ⟹ gaps
    all 7 (T=1,L=7). These are the "trivial" cases where one prime instantly becomes
    the universal hub.
  - a1 = 15 (=3·5): period found at T=8, L=30 = 2·3·5. Verified by brute force to N=60.
    Structural check: a_1=15 is the ONLY odd term in the whole sequence (checked to
    n=60); every other term is even, so a single hub prime 2 handles all gcd
    constraints except against a_1 itself, which additionally forces "divisible by 3 or
    5" — matching L = 2·3·5 exactly.
  - a1 = 35 (=5·7): period found at T=34, L=210 = 2·3·5·7. Verified by brute force to
    n=2000 (not just small n) — periodicity is robust, NOT a small-n coincidence. Over
    2000 terms, 203 *distinct* primes appear as incidental factors (up to 1237!), but
    they do not disturb periodicity: they ride along as extra factors of numbers whose
    gcd-compatibility is already secured via {2,3,5,7}. Checked explicitly: every ODD
    term in the sequence (a sparse, seemingly infinite subsequence) is divisible by 5 —
    i.e. 5 is a second, non-trivial "hub" prime that appears to intersect every odd
    term, exactly the sunflower-core structure opening 1 is trying to extract. This is
    the sharpest piece of evidence for the "finite hub set" conjecture and the single
    fact most worth trying to prove rigorously first (it would likely crack the
    boundedness-of-relevant-primes step).
  - a1 = 21, 33, 231 (multiples of 3 with no other small prime factor structure below
    them) collapse immediately to T=1, L=3 — again a trivial single-hub case.
  - Growth rate: for a1=35, a_2000 ≈ 12375, giving a_n/n ≈ 6.19 ≈ L/T = 210/34 ≈ 6.18,
    consistent with the periodic-regime prediction and a useful numeric cross-check
    tool for the outliner.
  - Conjecture to hand to the outliner: **for every valid sequence, there is a finite
    set S of primes (the "hub set") and an integer N0 such that for all n > N0, a_n's
    membership is governed only by which primes of S divide it, all non-S prime factors
    are irrelevant bystanders, and moreover a small number of hub primes (often just 2,
    sometimes needing a second "odd-side" hub) suffice to certify pairwise intersection
    with the entire infinite tail** — this finiteness is the crux gap; once granted, the
    CRT/sieve density bound (opening 2) and finite-state pigeonhole (opening 3) are
    comparatively routine.
