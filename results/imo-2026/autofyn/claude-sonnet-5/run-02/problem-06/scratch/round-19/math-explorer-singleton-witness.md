## imo-2026-06

- Distinct openings:
  1. **Direct existence attack via density/anatomy-of-integers.** Since a_n grows
     only linearly (certified Bounded/Generalized Bounded Gap Lemma), a_n has
     O(log a_n) prime factors; the out-of-core cofactor a_n / (S0-part) is, for a
     "generic" bounded-core S0, very often a single prime (classical
     smooth-number/largest-prime-factor phenomenon). This suggests attempting a
     genuine density LOWER BOUND on the rate of singleton-signature occurrences
     within a persistent type, then a second pigeonhole layer to force a common
     prime across both sides' singleton-occurrence subsequences. Genuinely new
     ingredient (no smooth-number/analytic apparatus exists yet in this
     workspace) — see caveats below on why this is harder than it looks once S0
     is actually the terminal/properly-recruited core.
  2. **Test the hypothesis directly on many new seeds, not just 4807/11305**,
     to see whether the existence pattern is a lucky coincidence of two examples
     or a robust phenomenon — done this round (see Small-case notes). Result:
     robust at *under-recruited* cores, uninformative at the genuinely hard
     (properly-recruited, low-singleton-rate) cores beyond the two known seeds,
     because building a THIRD genuinely-hard test seed requires faithfully
     replicating the Finite Core Theorem's own recruitment process, which this
     round's attempt showed is nontrivial and easy to get wrong (see Cheap-kill
     candidates / dead ends).
  3. **Reduce the existence question to a strictly weaker, possibly more
     tractable "infinitely-often" claim first.** The certified Generalized
     Bounded Witness Lemma's Corollary already gives: for ANY fixed witness m of
     type B, some single prime q in the fixed finite set F'_{A,B} := P(a_m)\S0
     divides infinitely many A-occurrences (via ordinary infinite pigeonhole).
     This is NOT the same as "some A-occurrence has singleton signature {q}" —
     it only says q divides infinitely many A-occurrences among possibly several
     other escaping primes at each one. Closing the gap between "q divides
     infinitely many" and "q is the SOLE escaping prime for at least one
     occurrence, matched on both sides" is the real content of the open
     hypothesis; no certified lemma currently bridges it.
  4. **Weaken the Theorem's own target**: ask whether Cofinite FAH can be forced
     using only the (already-certified) "q divides infinitely many A-occurrences"
     fact directly, bypassing the singleton-signature machinery entirely. Not
     attempted in depth this round (out of this lens's mandate) but worth
     flagging to the outliner as a possible alternate route that sidesteps the
     existence question altogether rather than trying to prove it.

- Candidate technique(s): anatomy-of-integers / smooth-number density heuristics
  (new to this workspace, not yet formalized); iterated pigeonhole via the
  certified Generalized Bounded Witness Lemma / Confined-GCD Lemma / Double-
  Witness Nested Pigeonhole Lemma (all already certified, reusable building
  blocks, but none currently reach "singleton" as opposed to "divides").

- Cheap-kill candidates: none obvious for refuting the existence hypothesis (I
  found zero counterexamples anywhere tested, see below); the closest thing to a
  cheap kill is the *methodological* one: naive full-factorization recruitment
  (fold a persistent type's whole witness factorization into S0 every round)
  does NOT reproduce the workspace's actual minimal terminal cores (verified
  directly — it inflates 4807's known 6-prime core to 17+ primes and 98
  "persistent" types when re-run from scratch), so any future round's claim of
  a "new hard |F'|,|F''|≥2 seed" must show its core is actually low-singleton-
  rate like the two known ones, not just large.

- Knowledge-base entries to use: none of the generic `knowledge_base.md` entries
  add anything beyond what's already cited in the approach file (pigeonhole,
  CRT). This is a workspace-internal-lemma question, not a fresh KB lookup.

- Analogous past problems (cruxes): none found. This existence question (do
  singleton out-of-core signatures occur, and do they coincide across two
  disjoint residue classes of a greedy sequence) is a bespoke arithmetic
  question about this specific construction; I did not find a crux-corpus entry
  resembling "prove a positive density / occurrence of a single-prime cofactor
  in a constrained integer sequence" that would transplant here (this matches
  memory rule 21's finding that aimo-0016/aimo-0051 are the closest general
  analogs in the corpus, and both are about the DIFFERENT existential-to-
  universal promotion gap, already tried and stuck, not this narrower
  existence-of-matching-witnesses question).

- Prior progress: Two-Sided Singleton Witness Theorem (§3 of
  `triangle-consistency-pigeonhole.md`) is fully proved and correctly explains
  both a_1=4807 and a_1=11305. Its hypothesis (existence of matching singleton
  witnesses) is the open residual.

- Dead ends (do not retry):
  - Same-Type Triangle Vacuity mechanism (§2 of the same file) — confirmed dead,
    re-verified reasoning holds (Free Facts on two same-type witnesses only
    certifies what the type's own in-core primes already give).
  - Do not attempt to construct a "properly recruited" new hard seed by folding
    every persistent type's full witness factorization into S0 each round — this
    round confirmed concretely (re-running from scratch) that this over-
    recruits by an order of magnitude relative to the workspace's actual
    minimal terminal cores, so any core built this way is not a faithful test of
    the hard regime.
  - Do not treat "many disjoint persistent types at an ad hoc small core (e.g.
    Q ∪ {2,3,5,7,11,13}) have matching singleton witnesses" as evidence for the
    general existence hypothesis without the caveat below — it is a much easier
    regime (see Small-case notes).

- Small-case / intuition notes (all labeled conjecture/empirical, not proof):
  - Re-verified from scratch (fixed a sign-flip bug in a first draft of the
    simulator — legality is gcd>1 with EVERY prior term, not gcd==1 — before
    trusting any output) that both known hard seeds show matching singleton
    witnesses with the SAME prime on both sides at their actual recruited cores:
    a_1=4807, S0={2,3,5,11,19,23}: A'={3,5,19} has 12/32 ≈ 37.5% singleton
    occurrences at q=17 (checked to n=20000); B'={2,11} has 26/452 ≈ 5.8%
    singleton occurrences, also q=17. a_1=11305, S0={2,3,5,7,13,17,19,23,29,
    37,43,101}: A'={2,5} has 36/614 ≈ 5.9% singleton at q=11; B'={3,7} has
    18/206 ≈ 8.7% singleton, also q=11. Both fully consistent with the
    approach file's report (small count discrepancies only from window size).
  - Tested the existence hypothesis on 7 brand-new seeds beyond 4807/11305
    (385, 1001, 2431, 4199, 7429, 17017, 15015 — products of 3-4 medium primes,
    the same structural family) at an ad hoc core S0 := Q ∪ {2,3,5,7,11,13}
    (NOT the true minimal terminal core — see caveat). Result: across all 9
    seeds tested this way, EVERY disjoint-persistent-type pair found (514 pairs
    total) has at least one shared singleton-witness prime on both sides — zero
    counterexamples. This is genuinely new data (no prior round tested beyond
    the same two seeds, per memory rule 16) and is mildly encouraging, BUT:
  - **Important corrective finding**: at this ad hoc core, singleton
    occurrences are NOT rare — they are the dominant case (85-92% of all
    occurrences of a persistent type are singleton, e.g. a_1=4807 type
    {2,3,11}: 1986/2280 ≈ 87% singleton, with 549 DISTINCT singleton primes
    observed). With hundreds of distinct primes appearing as singleton
    witnesses on each side out of a shared universe of "small excluded primes,"
    a shared prime is close to statistically inevitable (birthday-paradox-style
    pigeonhole) — this is NOT the same phenomenon as the genuinely hard case,
    where singleton occurrences are rare (5-37%, as in the two real hard seeds)
    because the core is actually large/properly recruited and has absorbed most
    of the "easy" escaping primes. So this round's 9-seed, 514-pair "100% match"
    result should be read as: the phenomenon is at least plausible and no
    counterexample exists anywhere tested, but it does NOT constitute new
    evidence at the genuinely hard difficulty level — it is evidence at an
    easier regime that (via Singleton-Side FAH alone, since most occurrences
    are already directly singleton) likely doesn't even need the two-sided
    upgrade to close FAH for those particular under-recruited pairs in the
    first place.
  - Conjecture, clearly labeled: the existence of matching singleton witnesses
    is plausible in general via a density/anatomy-of-integers mechanism (the
    escaping cofactor of a linearly-growing integer against a fixed finite core
    is frequently a single prime), but no rigorous density LOWER BOUND exists
    for this specific greedy-constrained sequence (as opposed to a generic
    integer sequence), and the bound would need to survive at the genuinely
    small-escape-rate, properly-recruited terminal core, not just at an
    artificially small one — this is a real, not yet closed, gap, and I found
    no mechanism in the certified lemma stack that reaches it.
