## imo-2026-06

n1-periodicity-reconciliation: revise
Target: the WHOLE problem (a_{n+T} = a_n + L for all n >= 1, cyclic-pigeonhole
finish), attacking specifically the secondary "n=1 literal periodicity" gap that
sits downstream of FAH (this approach is explicitly conditional on FAH/Cofinite
FAH throughout, per its own honest framing — it does not attempt the main crux).
Technique: Self-Absorbing Core construction (an enlarged core S* that absorbs
every early transient term's full factorization up to the Extended-Persistent-
Type-Pigeonhole threshold N(S*)), combined with the minimality of the greedy
choice a_{n+1} to force the actual term into the enlarged eligible-residue set
G*.
Skeleton:
  1. Import (conditionally) FAH/Cofinite FAH and the certified CRT + cyclic-
     pigeonhole finish (`covering-system-construction` Step 5): eventual
     periodicity a_{n+T} = a_n + L for n >= some finite threshold — already
     established given FAH.
  2. Define the self-absorbing core S* (round 13's construction): S* absorbs
     every prime factor of every one of the finitely many early transient
     terms' factorizations, up to the Extended-Persistent-Type-Pigeonhole
     threshold N(S*).
  3. Define G* := the broader eligible-residue set at S* — "residues mod L*
     (L* := prod of S*) that MEET every persistent type," strictly broader than
     Step 5's original G := {sig(r) : sig(r) IS itself a persistent type}.
  4. **THE GAP TO FIX THIS ROUND — re-derive "combining both parts" for G*
     from scratch, not by citing Step 5.** Step 5's own proof of "the actual
     a_{n+1} lands in G, and G is sufficient" was run for the NARROW G, using
     the same-base/overlapping-base/disjoint-base trichotomy on Step 5's
     specific witness data. That trichotomy argument must be RE-RUN, verbatim
     in structure but against G*'s broader membership test ("meets some
     persistent type" instead of "sig(r) IS a persistent type"), because G*'s
     sufficiency direction is easier (a strictly larger set is easier to be
     sufficient) but its "real term lands inside" direction is NOT automatic
     from a proof about the smaller G — a term could a priori land in G*\G
     without any witness saying it must. Concretely: show (i) sufficiency —
     every residue in G* is legal at S* (an easier consequence of the
     trichotomy, since G* is defined by weaker containment); (ii) landing —
     minimality of a_{n+1} plus FAH at S* rules out any smaller G*-non-member
     candidate being legal, by re-running the trichotomy (same-base /
     overlapping-base / disjoint-base) directly against G*'s test, not
     against G's.
  5. Once (4) is filled: a_{n+T*} = a_n + L* for n >= N(S*), a genuinely
     broader-core reconciliation than Step 5 alone gives, resolving the named
     obstruction (an early transient term's idiosyncratic factorization
     disqualifying an otherwise-eligible residue).
  6. Leave explicitly open (do not attempt this round, report honestly if
     still open): (a) existence/termination of a self-absorbing S* itself
     (does the absorption process converge to a finite S*?); (b) whether
     N(S*) can be taken to be 0 (needed for LITERAL n=1 periodicity, not just
     eventual).
Key lemmas (claim + mechanism):
  - Self-Absorbing Core Theorem, G*-version — because minimality of the
    greedy choice a_{n+1} (it is the SMALLEST legal candidate) combined with
    FAH at the enlarged core S* forces the real term to satisfy G*'s
    (broader) test: any smaller candidate failing the test must be illegal,
    which the re-run trichotomy (not a citation) must show directly, since G*
    is a strictly different set from Step 5's G in general.
Open gaps: step 4 (the re-derivation itself) is the entire open gap this
round; steps 6(a),6(b) remain open sub-gaps to flag honestly, not resolve.
Cases to cover: the trichotomy's three branches (same-base, overlapping-base,
disjoint-base) must each be checked against G*'s test, not assumed to
transfer unchanged from the G-version.
Watch out for: re-introducing the same hand-wave-by-citation bug in a new
guise — the fix must show its work for G* specifically, referencing Step 5's
LEMMAS (e.g. individual sufficiency facts) but not its CONCLUSION (which was
stated only for G).

integer-monovariant-difference-identity: new
Target: the WHOLE problem — eventual periodicity a_{n+T} = a_n + L — attacked
via a genuinely different top-level mechanism: an integer-valued monotone
bounded statistic of the greedy process forced eventually constant by
integrality, then inverted by a difference identity to recover the exact
term value, bypassing "which prime recurs" entirely (adapted from crux
`aimo-0134`, independently verified this round: aimo-0134's proof is
b_k := (a_1+...+a_k)/k, shown integer (k | partial sum by the rule's own
definition) and shown to satisfy (k+1)b_{k+1} = k b_k + a_{k+1} <= k b_k + k
since a_{k+1} <= k, giving b_{k+1} < b_k + 1, hence (by integrality)
b_{k+1} <= b_k; a non-increasing sequence of nonnegative integers is
eventually constant; then a_k = (k+1)b_{k+1} - k b_k recovers a_k = b for
k >= the stabilization index).
Technique: monovariant-from-averaged-partial-sums + difference-identity
inversion (crux aimo-0134, `size-bounding-and-descent` /
`sequences-and-recurrences`).
Skeleton:
  1. **Honesty check before building (done here, must be re-verified by the
     builder, not assumed):** aimo-0134's monotonicity proof crucially uses
     that its terms are BOUNDED by the index (a_{k+1} <= k), which is what
     converts the per-step inequality into "< b_k + 1" and then, via
     integrality, "<= b_k". Our a_n are UNBOUNDED (a_n -> infinity, only the
     GAPS g_n = a_{n+1}-a_n are bounded, by the certified Bounded Gap Lemma:
     1 <= g_n <= a_1). So the literal transplant (average the a_n's
     themselves) fails outright — the running average of a_n grows without
     bound. The correct object to average is the GAP sequence, not the terms.
  2. Define b_n := (g_1 + ... + g_n)/n = (a_{n+1}-a_1)/n, the running average
     gap. This is generally NOT an integer and has no obvious per-step
     inequality forcing monotone descent (unlike aimo-0134's b_k, which is
     forced integer by the per-step rule's own divisibility construction —
     our rule has no such built-in "correction toward a multiple of n"
     structure). This is the load-bearing design question the builder must
     resolve or refute: find an integer-valued (or otherwise
     integrality-exploitable) statistic S_n of the gap sequence with (a) a
     genuine per-step inequality forcing monotonicity, sourced from the
     ACTUAL legality rule (gcd(a_{n+1}, a_i) > 1 for all i <= n, a_{n+1}
     minimal), not assumed by analogy; and (b) a difference identity
     recovering g_n (or a_n) exactly once S_n stabilizes.
  3. **Two natural candidates checked in advance, both rejected — do not
     re-propose either without a genuinely new ingredient:**
     (a) S_n := |𝒫_n|, the count of distinct (extended-)persistent types
     visited among indices 1..n. This is monotone non-decreasing and bounded
     (by the alphabet size, already certified via Persistent-Type Pigeonhole)
     — but its eventual constancy is EXACTLY the already-certified
     Persistent-Type Pigeonhole (every index eventually lands in the fixed
     set 𝒫), not new content, and by itself gives no periodicity (existence-
     shaped, same wall).
     (b) S_n := |S_n^core|, the size of the running recruited-prime core
     after n steps of the recruitment process (`covering-system-
     construction` Step 4c). This is monotone non-decreasing by construction
     (recruitment only adds primes) — but whether it is BOUNDED (i.e., the
     recruitment process terminates) is LITERALLY gap (†) itself. Framing
     "prove S_n^core eventually constant via integrality" is circular here:
     integrality of a set-size statistic gives no help proving boundedness;
     boundedness IS the open question. This candidate restates the crux, it
     does not bypass it.
  4. Given (3), the builder's job is to search for a THIRD candidate integer
     statistic, genuinely derived from the gap sequence or the growth rate,
     not equivalent to (a) or (b) above, with an honest per-step inequality
     proof (not assumed by analogy to aimo-0134). If no such statistic is
     found after a genuine, documented search, report RETHINK honestly (a
     negative but informative result, consistent with the plateau-break
     rule's intent to diversify the population, not guarantee success).
Key lemmas (claim + mechanism): none proved yet — this is an exploratory
opening; the "mechanism" to find IS the open gap. The two rejected candidates
above are recorded as dead-on-arrival so no future round re-derives them.
Open gaps: the entire construction (step 2/4) — does a bounded, monotone,
INTEGER statistic of the gap sequence exist with a genuine per-step
inequality (not by analogy) forcing its descent? This is honestly unresolved;
this approach may die this round if the search comes up empty, which is
itself useful information (rules out the aimo-0134 transplant family
entirely, a 16th mechanism).
Cases to cover: none yet (exploratory).
Watch out for: assuming an inequality "by analogy" to aimo-0134 without
deriving it from the ACTUAL rule (gcd > 1, minimality) — the source crux's
inequality comes from a specific structural fact (a_{k+1} <= k) that has no
counterpart here; any claimed monotonicity must cite the Bounded Gap Lemma or
another certified fact, not assert a generic "averages tend to decrease"
intuition.

covering-system-construction: advance
Target: the WHOLE problem via the covering-system / recruitment-process
framing (Free Facts -> Finite Core Theorem -> S₀-level recruitment ->
CRT + cyclic-pigeonhole finish), contingent on closing gap (†) (V = ∅ at
every stage of the recruitment process).
Technique: covering systems / CRT + pigeonhole on persistent divisor types,
per the certified stack (`finite-core-theorem.md`,
`generalized-bounded-witness-lemma.md`, `canonical-refinement-lemma.md`,
`monotonicity-of-resolution.md`, etc.).
Skeleton: unchanged from the current certified state (see `current.md`
"Current best" #1-9, #11-12); no new step proposed this round.
Key lemmas: all already certified; no new lemma proposed this round.
Open gaps: gap (†) (V = ∅, equivalently FAH/Cofinite FAH/EEA) remains the
sole blocker, now with 15 confirmed-dead mechanisms against it. Nominated
for ranking continuity per usual practice, not for new work this round
(the round's genuinely new material goes into the two approaches above).
Cases to cover: none new.
Watch out for: do not re-attempt any of the 15 confirmed-dead mechanisms
(full list in `current.md` Rules history) under this approach's banner.

greedy-exchange-cost-potential: advance
Target: the WHOLE problem via the exchange/witness-prime-pigeonhole framing
(cost potential, Extended Persistent-Type Pigeonhole, No-Restart Lemma),
independently converging on the same crux (†) as covering-system-
construction.
Technique: integer cost/witness-prime pigeonhole + exchange argument, per
the certified stack (`single-witness-prime-pigeonhole.md`,
`no-restart-lemma.md`, `extended-persistent-type-pigeonhole.md`).
Skeleton: unchanged from the current certified state; no new step proposed
this round.
Key lemmas: all already certified (most recently the No-Restart Lemma,
round 13); no new lemma proposed this round.
Open gaps: gap (†), same as above, still open.
Cases to cover: none new.
Watch out for: do not re-attempt CRT-glue/competitor-construction (14th
dead mechanism) or exact-valuation-monovariant induction (falsified this
round by the valuation-lens explorer via the a_1=11305 rogue-pair
non-monotonicity counterexample — the Confined-GCD divisor class g_n is
NOT absorbing, jumps away and reverts) under this approach's banner.

build set: n1-periodicity-reconciliation, integer-monovariant-difference-identity, covering-system-construction, greedy-exchange-cost-potential
