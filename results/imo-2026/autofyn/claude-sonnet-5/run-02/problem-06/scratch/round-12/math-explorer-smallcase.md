## imo-2026-06 (lens: bespoke small-|F'|=2 / small-|Q| ad hoc fallback)

- **Distinct openings surfaced:**
  1. **Concretized single-bad-class reduction.** Reconstructed the exact |F'|≥2
     machinery on the two cited seeds (a_1=4807, a_1=11305) from scratch (own
     script, independent of any prior builder's code). For a_1=4807's rogue pair
     A'={3,19,5} vs B'={2,11} (n_A=6, n_B=7): F'' := P(a_{n_B})\S0 = {13,17}
     (the non-singleton side), but the OTHER side F' := P(a_{n_A})\S0 = {17}
     IS a singleton — so by the already-certified Singleton-Side FAH Lemma,
     the B'-side of Symmetric FAH is free for this pair; the only remaining
     open direction is the A'-side. Applying the certified Confined-GCD Lemma
     with b := 13^1·17^1 = 221 (from a_{n_B}=4862=2·11·13·17), Div(b) =
     {1,13,17,221}; g_n=1 is impossible (Free Facts), multiples of 17 (17,221)
     are the "good" classes, so **the entire literal-FAH exception set for this
     pair collapses to exactly ONE bad divisor class: g_n = 13**. This is a
     genuinely small, concrete residual target (rule out gcd(a_n,a_{n_B})=13
     exactly, for A'-type n>n_B), sharper than the general-|F'| framing. The
     same pattern holds for a_1=11305 (F'={11,103} on the non-singleton side,
     singleton {11} on the other — same D_bad-collapses-to-one-class shape).
  2. **"One side already free" observation.** Because Singleton-Side FAH already
     resolves whichever direction has a singleton far-side factor set, for many
     concrete rogue-pair instances in this workspace (checked a_1=4807's 12
     rogue-pair records, a_1=11305's 42) the genuinely open content per pair may
     already be *one-sided*, not the full two-sided Symmetric FAH the finish's
     Step 8.5 proof structure demands in general. This narrows what "closing
     the |F'|=2 case" would even need to prove, though it does not by itself
     close anything.
  3. Attempted, per the dispatch, to find a mechanism specific to |D_bad|=1
     (a single residual class) that could exploit finiteness of the alphabet in
     a way general |F'| cannot: e.g. applying Lemma H (Critical Prime Dichotomy)
     to the single prime 13 on a hypothetical exception a_n (13|a_n, 17∤a_n);
     or a magnitude/CRT argument confined to the tiny modulus 13. Both routes
     immediately re-enter already-mapped dead territory (see Dead ends below) —
     no genuinely new mechanism was found.

- **Candidate technique(s):** None beyond the already-certified Confined-GCD /
  D_bad finite-alphabet recast (already in the toolkit, certified round 9).
  The dispatch's hoped-for "extra structure vanishing at larger |F'|" does not
  materialize as a new proof shape — |F'|=2 only makes D_bad numerically small
  (often literally |D_bad|=1 after removing the impossible g_n=1 class and the
  already-singleton-resolved side), but the *mechanism* needed to rule out that
  one remaining class is identical in kind to what's needed for the general
  case, and has already been tried directly on these exact seeds.

- **Cheap-kill candidates:** none beyond what's already done. The natural
  cheap-kill (numerically check whether g_n ever equals the bad class) was run
  here: on a_1=4807's pair, 25 A'-occurrences sampled up to n≈20000, g_n ∈
  {17, 221} only — **zero occurrences of the bad class 13** — matching every
  prior round's "0 failures" finding. Purely confirmatory, not new.

- **Knowledge-base entries to use:** none new; this lens stays entirely within
  already-certified lemmas (`free-facts-gcd.md`, `confined-gcd-lemma.md`,
  `generalized-bounded-witness-lemma.md`, `singleton-side-fah.md`). No
  knowledge_base.md entry (Zsigmondy, LTE, Dirichlet, three-gap theorem, etc.)
  looks applicable to closing the single-residual-class target; this is a pure
  "does one specific prime always appear" combinatorial question, not an
  algebraic-identity or analytic-number-theory target that any KB tool bites on.

- **Analogous past problems (cruxes):** none beyond what prior rounds already
  found (aimo-0477, aimo-0611, aimo-0678, aimo-0680, aimo-0016, aimo-0514,
  aimo-0030 — all previously mined and already flagged as either dead-ended or
  structurally disanalogous per the ALWAYS/NEVER rules in memory). No new
  crux search was productive for this specific small-alphabet framing; the
  target ("prove a fixed prime divides every term of an infinite recurring
  subsequence, given only that it divides at least one of two divisor
  classes per term") does not match any crux move not already tried.

- **Prior progress:** unchanged from `current.md` round 11 — FAH/Symmetric FAH
  is the sole open crux, 14 general mechanisms confirmed dead across 6
  consecutive rounds, zero counterexamples anywhere. This lens adds one
  legitimate, small, honest clarification (the single-bad-divisor-class
  framing above) but does **not** find a route past the wall.

- **Dead ends (do not retry, and this lens independently re-confirms why):**
  - Lemma H (Critical Prime Dichotomy) applied to the lone residual prime
    (13, or 11 for the other seed) — already tested concretely on this exact
    a_1=4807 data in round 6/9 ("both candidate primes trivially land in the
    uninformative branch (a)"); nothing about |D_bad|=1 changes that, since
    Lemma H's branch selection depends on the specific integer a_n's other
    factors, not on the SIZE of the alphabet.
  - CRT-glue / small-modulus competitor construction confined to modulus 13
    (or 13·q*) — this is exactly the 14th mechanism (Minimal-Modulus
    Generalization, round 11), already proved dead in full generality
    (structural half) and magnitude-checked dead on a_1=4807 specifically
    (0/2499 gaps reach even the cheapest single-prime-of-Q modulus 187, let
    alone anything built from 13).
  - Escape-Budget / Successor Claim (round 10) and window-capacity counting
    (round 9, `cofinite-window-capacity-bound`) were BOTH run using exactly
    these two seeds (4807, 11305) as their primary test data, and both died
    at "infinite pigeonhole gives some infinite divisor-class, never
    exclusivity" (Lemma I's original diagnosis). Since D_bad collapsing to
    size 1 does not change the counting-theoretic shape of that obstruction
    (pigeonhole over 2 classes is exactly as uninformative as over k classes
    for proving ONE class is cofinite/empty), this obstruction applies
    verbatim to the |F'|=2 case — it was never a large-|F'| artifact.
  - Density/sieve arguments (round 11, `sieve-density-exception-bound`) — the
    certified Density-Argument Vacuity Corollary and Selection-Rule
    Class-Blindness observation apply regardless of alphabet size (they rule
    out any window-aggregate/counting statistic, which is exactly what a
    "there are only 2 bad classes so count them" argument would be).

- **Small-case / intuition notes (labeled conjecture where appropriate):**
  - Empirically (conjecture, not proof): for every rogue pair tested in this
    workspace across ~500+ cumulative seeds, literal FAH (zero exceptions,
    not just cofinite) appears to hold — the |F'|=2 seeds are no exception
    (0/25 and matching counts on 11305's analog). This is strong empirical
    support for the theorem itself, but gives no proof mechanism.
  - The |F'|=2 case is **not a separate, easier sub-problem** structurally —
    it is literally the same seeds (a_1=4807, 11305) the whole population has
    used as its canonical "genuinely open |F'|≥2" test bed since round 6.
    Scouting it as if it were unexplored terrain would be a mistake; it is the
    most heavily-explored terrain in the entire workspace.
  - The one clean new fact from this pass — D_bad often collapses to a single
    residual divisor class once the Singleton-Side FAH Lemma is applied to
    strip off the already-free direction — is real and could be recorded as a
    minor sharpening ("Reduced-Alphabet Corollary" of Confined-GCD +
    Singleton-Side FAH: for a rogue pair where one side's far-factor-set is
    singleton, the other side's FAH exception set is confined to divisors of
    the OTHER side's far-factor-set that are coprime to the recruited prime,
    generically small). This is a genuine, provable, certifiable *corollary*
    of two already-certified lemmas (trivial to prove — one line, combine
    Confined-GCD's Div(b) recast with Singleton-Side FAH's resolution of the
    companion side) — worth certifying as bookkeeping, but it is a
    **reformulation, not a new mechanism**, and does not by itself make
    progress on ruling out the remaining single class. I do not recommend
    building a whole round around it; if the outliner wants a cheap,
    low-risk lemma to certify while the real search continues elsewhere, this
    is available, but it should not be oversold as "narrowing the general
    claim" in the sense CLAUDE.md's fallback-lens guidance intended — round
    11 already effectively achieved the same narrowing (14 mechanisms, same
    wall) using these same seeds.
  - **Recommendation to the outliner:** this fallback lens, as literally
    specified (bespoke argument for |F'|=2), does not appear to open new
    terrain — it re-lands on the same wall via the same seeds already
    exhausted by 6 rounds of work. If round 12 wants a genuinely different
    fallback, consider instead: (a) a small-|Q| enumeration (|Q|=2 seeds like
    a_1=35, 15 — already partially explored in round 1 but never revisited
    with the FULL current certified toolkit) rather than small-|F'|, since
    |Q| bounds the number of base types and hence the total number of rogue
    pairs to check, which is a genuinely different finiteness parameter from
    |F'|; or (b) seriously pursue round 11's own top recommendation — an
    index-specific (not window-aggregate) analytic estimate on a SPECIFIC
    candidate's factorization near a SPECIFIC index, which is the one
    documented gap not yet closed off by any of the 14 dead mechanisms.
