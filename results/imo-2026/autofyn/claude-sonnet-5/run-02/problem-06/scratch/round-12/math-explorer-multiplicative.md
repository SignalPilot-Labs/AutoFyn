## imo-2026-06

- Distinct openings (this lens = deep multiplicative/valuation structure of a_1,
  beyond round 11's CRT-residue pass):
  1. **Exponent/valuation independence test** — checked computationally whether
     v_p(a_1) (as opposed to just membership p | a_1) has any bearing on the
     combinatorial legality structure. Verified the a priori algebraic fact: the
     legality predicate gcd(c, a_i) > 1 only ever tests *shared prime factors*,
     never exponents, so two seeds with the same radical Q = rad(a_1) but
     different exponents are playing "the same abstract game" only in the sense
     that Q is the same — but the actual numeric trajectory (which integer is
     smallest-legal at each step) still depends on a_1's exact magnitude, so
     exponents DO end up mattering operationally, just not through any gcd-type
     information channel. This is a clean but ultimately negative finding (see
     below) — it does NOT hand the toolkit any new identity-level lever, but it
     is a genuinely unexploited fact worth recording precisely (no prior round
     stated it this way).
  2. **Divisor-lattice / Möbius structure of a_1** — considered whether the poset
     of divisors of a_1 (or the lattice of subsets of Q under the "extended type"
     order already in use) admits a Möbius-inversion or inclusion-exclusion
     identity that could convert the existing "some prime of a fixed set divides
     a_n" existence facts into an identity-level count. Not pursued past the
     conception stage — the same-type-free-facts-vacuity and Density-Argument
     Vacuity Corollary already show that any purely combinatorial/counting
     aggregate over S₀ is class-blind, and a Möbius-type identity over the
     divisor lattice of a_1 is exactly such an aggregate (it would need to sum
     class-blind indicator data). Judged very likely to fall to the same
     Vacuity-Corollary argument if attempted; not built out further (respecting
     the "don't chase to the end" instruction), but flagged as untested and
     probably dead rather than promising.
  3. **Order-of-recruitment as a function of a_1's magnitude, not just Q** — the
     genuinely new empirical finding this round (see Small-case notes) is that
     which primes get recruited into the core S, and how MANY recruitment stages
     it takes, is NOT a function of Q alone: two seeds with identical Q can
     produce very differently-sized cores S₀ and wildly different transient
     lengths. This reinforces (does not contradict) round 11's finding that q is
     "dynamically, not algebraically, determined" — but sharpens it: it's not
     just q's *identity* that's dynamical, the entire *recruitment schedule*
     (which primes, how many rounds, how long the transient) is sensitive to
     a_1's exact value even at fixed Q. No new proof mechanism follows from this,
     but it is an important calibration fact for computational sanity-checking
     (see Cheap-kill / caution below).

- Candidate technique(s): None of the above yields a new proof mechanism for
  FAH/Cofinite FAH. This lens independently re-confirms round 11's verdict from
  a different angle (exponents/magnitude rather than residues/CRT-class) and
  should be read as complementary evidence, not a contradiction: the
  multiplicative structure of a_1 (whether read via residues, CRT class, or
  exponents/valuations) carries only S₀-level (type-membership) information,
  never intermediate-term identity information, consistent with the workspace's
  standing Rule (round 9/10/11): every certified tool gives existence or
  magnitude, never identity, and this includes every flavor of "structure of
  a_1" tried so far.

- Cheap-kill candidates: none obvious for closing FAH. However, a genuinely
  useful STRUCTURAL caution for the population's computational-evidence
  gathering: seeds with the same Q but non-squarefree a_1 (extra prime power
  factors) can produce a MUCH larger core S₀ and MUCH longer transients before
  periodicity is even reached — see a_1=315 = 3²·5·7 below, which fails to
  stabilize within 15,000 sampled terms despite |Q|=3 (comparable to a_1=105,
  which stabilizes by term ~1000 with T=58,L=210). Any future "0/N
  counterexamples" computational claim about FAH MUST report whether the tested
  window actually reached the periodic regime (not just ran N terms) — a claim
  of "0 counterexamples over N terms" on a seed like 315 could be entirely
  within the pre-periodic transient and uninformative. This is a concrete
  addition to the existing Rule (round 3/4) about witness-index depth not being
  a function of |Q| alone.

- Knowledge-base entries to use: none new identified this round beyond what's
  already certified in the workspace (Finite Core Theorem, Generalized Bounded
  Witness Lemma, Confined-GCD Lemma, Cofinite Sufficiency Lemma, Density-Argument
  Vacuity Corollary / Sandwich Genericity Theorem — this lens's negative finding
  for opening #2 above is a direct instance of the latter two, not a new
  application).

- Analogous past problems (cruxes): none newly surfaced this round beyond what
  round 10-11 already searched exhaustively (aimo-0477, aimo-0678, aimo-0680,
  aimo-0682, aimo-0016, aimo-0514, aimo-0030, aimo-0231 — all previously
  checked and found to rely on a closed-form algebraic recurrence or a global
  per-step divisibility identity this problem's greedy/existential definition
  lacks). Did not find a new corpus match specific to a_1-exponent/valuation
  structure — the crux corpus's modular-arithmetic-and-CRT entries (already
  searched by round 11) are the natural place such a match would live, and
  round 11 reports nothing transferable found there.

- Prior progress: none altered by this round's findings; current crux remains
  exactly as stated in current.md — FAH/Symmetric FAH (equivalently Cofinite
  FAH / the Successor Claim), 14 confirmed-dead mechanisms, 6 consecutive
  plateaued rounds (6–11).

- Dead ends (do not retry): reconfirms (via a different route — exponents
  rather than residues) round 11's verdict that a_1's multiplicative/CRT
  structure gives no new mechanism; do not re-dispatch a "multiplicative
  structure of a_1" lens again without a genuinely different sub-angle not
  covered by round 11 (residues/CRT-class) or this round (exponents/valuations,
  divisor-lattice/Möbius). Also do not propose a Möbius-inversion /
  inclusion-exclusion-over-divisor-lattice argument for FAH without first
  checking it against the certified Density-Argument Vacuity Corollary /
  Sandwich Genericity Theorem — it is very likely to be another instance of a
  class-blind aggregate, per the reasoning above (not built out to a formal
  refutation this round, flagged as a strong prior only).

- Small-case / intuition notes (all conjecture/empirical, verified this round
  by direct Python simulation, code in /tmp/round-12/probe.py, probe2.py,
  probe3.py):
  - CONFIRMED (structural fact, not just numeric): legality only ever tests
    gcd > 1 (shared primes), never exponents — so a_1's exponent data cannot
    enter the FAH mechanism through any gcd-based tool, matching the existing
    toolkit's structure.
  - Radical-matched pairs (15,45), (15,225), (6,12), (6,24), (6,72),
    (105,11025) all produced IDENTICAL base-type sequences for the first 40
    terms — mild positive evidence that "same Q usually looks the same early
    on."
  - COUNTEREXAMPLE to that pattern: (105, 315) — both Q={3,5,7} — diverge at
    n=11 (base type differs). a_1=105 recruits core S₀={2,3,5,7,11} (5 primes)
    and stabilizes fast (T=58, L=210) by ~1000 terms. a_1=315=3²·5·7 recruits a
    much larger core S₀={2,3,5,7,11,23,53} (7 primes, including two "large"
    primes 23, 53) and does NOT stabilize within 15,000 sampled terms (checked
    periods T up to 800 in multiple tail windows, none found). This is a
    genuine new data point (a_1=315 was not in any prior round's tested seed
    list) demonstrating a non-squarefree seed with small |Q|=3 but a
    dramatically longer transient than any previously-reported |Q|=3 seed —
    worth adding to the seed-testing playbook if a future round wants a
    stress-test case for computational FAH claims, though I did not push it far
    enough (would need N well beyond 15,000 terms, expensive with the current
    O(N²)-ish gcd-search generator) to determine whether it ultimately
    satisfies FAH or reveals a genuine violation. Flagging this as a concrete,
    cheap follow-up for a future round with more compute budget or a faster
    sequence generator (e.g. sieve-based candidate search instead of linear
    gcd scan) if the population wants fresh stress-test seeds.
