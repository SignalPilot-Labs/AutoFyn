## imo-2026-06

- Distinct openings (genuinely different top-level framings, not variants of the same
  covering-system/persistent-type machinery that both round-1 approaches and the
  `density-sieve-contradiction` stub eventually reduce to):

  1. **Explicit integer monovariant / well-ordering framing** (seed: aimo-0678
     Solution 1). Instead of extracting an infinite family of "persistent types" and
     then trying to show any two disjoint ones reconcile on a shared finite core (gap
     †), define a SINGLE explicit integer-valued quantity attached to the state of the
     process at step n (e.g. something in the spirit of aimo-0678's `w_n = min{m ≥ a_n :
     m ∤ s_n}`, a "first failure point" statistic) and prove directly, by a short
     case-split on the recurrence's definition (not on abstract type combinatorics),
     that this quantity is non-increasing (or bounded above by a fixed constant
     depending only on a_1) as n grows. Non-increasing + integer + bounded below by
     well-ordering ⟹ eventually CONSTANT, at which point the process's local behavior is
     pinned to a genuinely finite combinatorial regime and periodicity drops out by a
     short finite pigeonhole (no covering system, no "extended type" bookkeeping). The
     key difference from the round-1 approaches: this looks for ONE scalar potential
     that is monotonic by direct computation from the recurrence, rather than trying to
     classify infinitely many "types" as a set-system and prove an intersection property
     about them. It may hit its OWN crux (finding the right potential function and
     proving monotonicity), but that crux is different in kind from (†) — it is a
     "does this specific quantity decrease" computation, not a "do two disjoint families
     intersect" combinatorial claim.
  2. **Bounded-window state-machine / de Bruijn framing.** Since Bounded Gap Lemma
     already gives a_{n+1} − a_n ≤ a_1 unconditionally, treat the process as a walk on
     states where state_n packages "recent legality-relevant data" (which of the last
     ~a_1 integers were skipped and why). If one can show the set of *distinct* states
     that occur is finite (this is really where the same finiteness content as gap (†)
     hides, so this framing does not evade the crux, only relabels it as "state-space
     finiteness" instead of "type intersection") — the finish is a bare pigeonhole
     (no CRT bookkeeping needed at all, since state already encodes residues). Useful
     mainly as a cleaner vocabulary for the SAME open gap, worth flagging to the
     outliner as an alternative phrasing, but I could not identify a route by which this
     avoids proving essentially the same finiteness fact as (†).
  3. **Direct primes-appear-infinitely-often dichotomy** (seed: aimo-0421). For each
     prime p, either p divides infinitely many a_n or only finitely many. Since every
     a_n (n≥2) is divisible by some prime of the FIXED finite set Q = P(a_1) (Free
     Facts), pigeonhole already forces some p ∈ Q to divide infinitely many a_n — this
     reproduces (does not surpass) the existing Persistent-Type Pigeonhole lemma; I do
     not see this dichotomy giving new leverage on (†) itself, so it's a confirmation of
     existing machinery rather than a fresh route. Flagging as explored-and-not-fruitful
     rather than a genuinely new opening.
  4. **Numerically-informed pitfall check**: the *total* set of primes ever dividing any
     a_1,...,a_n is NOT bounded as n → ∞ (verified below) — so any framing that tries to
     bound "all primes that ever appear" is attacking a false sub-claim. The correct
     (and only tractable) finiteness claim is about a much smaller, carefully-selected
     pool (the S of the Finite Core Theorem, or an analogous "core" in framing 1), not
     the literal union of all prime factors. Worth flagging explicitly to the outliner
     since a naive density/sieve argument (as in the density-sieve-contradiction stub,
     step 3) risks conflating these two different objects.

- Candidate technique(s): explicit monovariant/potential-function argument (well-ordering
  on ℤ_{≥0}, as in IMO 2015 SL N4 = aimo-0678) is the strongest genuinely-different
  lead; a state-machine/pigeonhole-on-finite-alphabet reframing is a secondary,
  more cosmetic alternative. Both ultimately need "eventually periodic" via a finite
  pigeonhole finish, matching `knowledge_base.md`'s "Linear recurrences: sequences are
  eventually periodic mod m" entry.

- Cheap-kill candidates: none obvious that avoid the finiteness crux entirely — but the
  numerical fact that the *total* prime-support set is unbounded (see below) is a
  useful cheap NEGATIVE-result check: it should be used to immediately reject any
  approach draft that tries to prove "only finitely many primes ever divide any a_n" as
  its core lemma (a plausible-looking but FALSE strengthening); the correct finiteness
  claim must be about a bounded/selected sub-pool (persistent-type witnesses, or an
  analogous small "core" from framing 1), never "all primes ever used."

- Knowledge-base entries to use: "Linear recurrences: sequences are eventually periodic
  mod m" (for the finish, once any finiteness/monovariant-stabilization claim is
  established); "Modular arithmetic, CRT" (for the residue-class bookkeeping in the
  finish, shared with the existing approaches); "Pigeonhole / extremal principle" (for
  the well-ordering / finite-state pigeonhole step in framing 1 and 2).

- Analogous past problems (cruxes):
  1. **aimo-0678** (IMO 2015 SL N4, `sequences-and-recurrences`... actually classified
     informally as an invariants problem) — "Prove the sequence (a_n) is eventually
     periodic" for a gcd/lcm-driven recurrence. Crux move: define an explicit integer
     statistic w_n = min{m ≥ a_n : m ∤ s_n} (s_n = a_n+b_n), prove it is NON-INCREASING
     by direct case analysis on the recurrence (not by extracting infinite families),
     hence eventually constant by well-ordering; then a SECOND auxiliary statistic
     g_n = gcd(w, s_n) is shown CONSTANT once w_n stabilizes, pinning the process to a
     fixed finite cycle. This is the closest genuine analog in the corpus: same
     conclusion shape (eventual periodicity of an integer sequence generated by a
     greedy/deterministic gcd-based rule), and its solution's STRUCTURE (an explicit
     monotone potential, not a covering-system/type-intersection argument) is exactly
     the alternative framing recommended above (opening 1). Its second solution also
     independently confirms the "reduce mod M = lcm of all values ever appearing, get a
     finite state space, pigeonhole on state pairs" finish used by all our current
     approaches — cross-validating that finish step as standard and sound.
  2. **aimo-0727** (IMO-SL, "Netherlands", divisibility sequence a_{k+1} | 2(a_1+...+a_k),
     infinitely many primes divide some term ⟹ every n divides some term) — crux move:
     define an auxiliary quotient b_k, show b_{k+1} ≤ b_k+1 (a "grows by at most 1" step
     bound) and derive UNBOUNDEDNESS of b_k from the hypothesis via a contrapositive
     ("if b_k were bounded, only finitely many primes could ever divide any a_k").
     Relevant as the *contrapositive mirror* of the direction our problem needs (we
     already have bounded gaps for free via Free Facts + Bounded Gap Lemma, so we do not
     need to derive boundedness this way) — but the mechanism of "define one monotone
     auxiliary integer sequence and control it by ±1 steps" is the same flavor as
     opening 1's proposed potential function. Worth showing the outliner as a template
     for HOW to search for the right potential (look for a quantity whose ±1-bounded-step
     behavior is forced directly by the greedy/smallest-integer definition).
  3. **aimo-0503** (gcd(a_i,a_{i+1}) > a_{i-1} ⟹ a_n ≥ 2^n) — not directly analogous in
     conclusion, but structurally similar in spirit: an induction with an exhaustive
     case-split on the exact ratio a_n/gcd(a_n,a_{n+1}) that gets progressively refined
     (chains of gcd's going back further and further) until every case is closed. If
     framing 1's potential function needs its own case analysis to prove monotonicity,
     this problem is a good template for how deep/exhaustive that casework can
     legitimately get without being a "gap" (i.e. it shows a fully-closed finite-depth
     casework of this style is achievable and expected at this difficulty level, not a
     sign the approach is broken).

- Prior progress: see `current.md` — Free Facts, Bounded Gap Lemma, Persistent-Type
  Pigeonhole, Bounded Witness Lemma, Finite Core Theorem are all certified and
  unconditional; both round-1 approaches (amortized-charging-budget,
  covering-system-construction) and the untouched density-sieve-contradiction stub all
  reduce to the same crux (†) (or an equivalent "gap-boundedness without circularity"
  formulation) — see current.md lines 45-52 for its cleanest statement. The
  hypergraph-transversal approach (round 1, sampled here) reaches an equivalent crux
  under different vocabulary (finiteness of the eventual minimal-antichain prime
  support S), confirming (†) is a genuine invariant of the problem, not an artifact of
  one framing — which is exactly the situation CLAUDE.md's "shared-gap plateau" rule
  warns about: 3+ approaches now hit the identical wall.

- Dead ends (do not retry): the density-sieve-contradiction stub's own step 3 (raw
  Mertens/sieve density estimate on windows) risks proving a FALSE strengthening — my
  numerical check below shows the total prime support genuinely grows without bound, so
  any density argument that implicitly treats "the working prime set" as eventually
  fixed-and-small is attacking the wrong finiteness claim; the stub's own step 4
  ("blocking types capped by |Q|") is essentially a restatement of Persistent-Type
  Pigeonhole (already certified) and does not by itself close (†) — it should not be
  re-litigated as if novel.

- Small-case / intuition notes (numerical, python/sympy, this session):
  - For a_1 = 15: verified eventual period T = 8 in the GAP sequence (a_{n+1}-a_n),
    stabilizing well before n=100 (consistent with current.md's independently-reported
    T=8, L=30).
  - For a_1 = 105: eventual gap-period T = 58 (found by brute-force periodicity search on
    the tail, n up to 400) — larger example confirming periodicity is robust across
    seeds with more prime factors (105 = 3·5·7, |Q|=3).
  - For a_1 = 231 (=3·7·11): degenerates to constant gap 3 eventually (T=1) — a good
    simple/base test case for any monovariant framing (opening 1) since the "eventual
    regime" here is as simple as possible (single persistent type dominates).
  - Total distinct-prime-support of {a_1,...,a_n} for a_1=105: grows roughly like n
    itself (sizes at n=20,40,...,300 were 10,13,16,...,42 — clearly unbounded, not
    converging), CONFIRMING that "all primes ever used" is an unbounded set — this is
    conjecture-by-finite-computation only (not proved for all n), but strong evidence
    that framing any approach around bounding the TOTAL prime support (rather than a
    cleverly-selected core subset, as the Finite Core Theorem already does correctly) is
    a dead end.
