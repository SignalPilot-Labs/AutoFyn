## imo-2026-06

- Distinct openings (genuinely different top-level framings, not just technique variants
  of the current stuck field):

  **D1 — "Universal cheap witness prime" (recommended primary new opening).**
  Instead of trying to prove the abstract combinatorial statement (†) ("any two
  disjoint-base-type extended-persistent types intersect as subsets of S_0") directly by
  set-theoretic pigeonhole, target a SHARPER, more concrete claim suggested strongly by
  numerics (see below): there is often a single distinguished extra prime p* (empirically
  = the smallest prime not dividing a_1, when a_1 has no small prime factors) such that,
  beyond a finite threshold, EVERY term of the sequence that is not already "full type"
  (divisible by all of Q = P(a_1)) is divisible by p*. If provable, this makes (†) trivial
  (every extended-persistent type contains p*, so all pairwise intersections are
  automatic — no case analysis over refinements needed at all) and gives directly
  L = p*·∏Q, with G/T built from a much simpler 2-level type space (full-Q-type vs.
  not-full, crossed with Q-subtype) instead of the general 2^{S_0} lattice. The
  mechanism to actually prove "p* is eventually forced on every non-full term" should be
  a **minimality/greedy-exchange argument** (an idea gestured at but never carried out in
  `density-sieve-contradiction`'s step 4, "each new recruited prime pays for itself"): if
  a term needed a large fresh prime q instead of the cheap p* to satisfy compatibility
  with an earlier disjoint-type term, a smaller candidate that instead used p* should
  already have been available and legal (since being ≡0 mod p* is a much denser, cheaper
  condition than being divisible by some specific larger prime), contradicting that
  a_{n+1} is chosen as the SMALLEST legal integer. **This uses greedy minimality**, which
  none of the three round-1 approaches actually invoke beyond the Bounded Gap Lemma
  (a_{n+1} ≤ a_n + a_1) — that is the genuine gap in technique space, not just in problem
  framing, and is why this route can plausibly close (†) where set-only pigeonhole
  cannot.

  **D2 — "Recurrent primes" reframing (organizing object swap).** Define
  R := {p prime : p | a_n for infinitely many n} (the set of "recurrent primes"),
  instead of working with "persistent types" (subsets of Q) and their extensions. Two
  sub-claims replace the whole persistent-type/extended-type machinery: (i) R is finite;
  (ii) beyond some threshold, every a_n is divisible by some prime of R. This is a
  cleaner top-level target because it side-steps the type-refinement bookkeeping
  entirely — it asks directly "which primes divide infinitely many terms", not "which
  finite subsets of Q ∪ S occur infinitely often". The crux corpus entry `aimo-0421`
  (see below) uses exactly this kind of "finite fiber" pigeonhole (gcd-with-a-fixed-
  element takes finitely many values ⟹ pigeonhole on an infinite index set) and is a
  reasonable technique donor for proving (i), though the source problem's structure
  (arbitrary infinite set with prescribed gcd inequalities) is not a tight analogy for
  (ii), which is the genuinely new content needed here.

  **D3 — Dense-Q vs sparse-Q case split (a scoping move, not a full proof).** Numerics
  (below) show the "universal single witness prime" phenomenon (D1) is clean and strong
  when Q = P(a_1) is missing small primes (e.g. Q = {7,11}, {5,7,11,13}), but breaks down
  — no single prime dominates the recruited pool — when Q already contains several small
  primes (e.g. a_1 = 30, Q = {2,3,5}; a_1 = 210, Q = {2,3,5,7}). Recommend the outliner
  scope an approach that (a) proves the full result in the sparse-Q case via D1's clean
  mechanism, then (b) separately argues the dense-Q case reduces to a SMALLER sparse-type
  subproblem (e.g. by working only with the sub-family of terms of "deficient" type,
  i.e. missing at least one prime of Q, and noting Q itself already supplies enough
  density there) — genuinely different case-split strategy from anything in the current
  field, which treats all cases uniformly via one abstract type lattice.

- Candidate technique(s): greedy-minimality / exchange argument (smallest-legal-integer
  ⟹ no under-cutting alternative existed) as the mechanism to prove a distinguished cheap
  witness prime is eventually forced; CRT + finite-state cyclic pigeonhole (unchanged,
  shared final step with the existing field); pigeonhole on finite-valued gcd fibers
  (`aimo-0421`-style) as a secondary tool for the "recurrent primes are finite" claim.

- Cheap-kill candidates: check, for each a_1 tested, whether Q already contains a "small"
  prime (2 or 3) — if so, D1's clean single-witness mechanism likely does NOT apply
  directly and the approach must fall back to D3's case split or the general (†); this is
  a fast structural filter (just factor a_1) the builder should run before committing to
  D1 as the sole mechanism.

- Knowledge-base entries to use: `knowledge_base.md` "Pigeonhole / extremal principle",
  "Modular arithmetic, CRT", "Order of an element, Fermat/Euler: periodicity of aⁿ mod m;
  eventual periodicity of products of a sequence mod m" (directly analogous shape to the
  claim needed here — periodicity of a deterministic rule mod a fixed modulus).

- Analogous past problems (cruxes):
  - `aimo-0421` (number_theory, divisibility-and-gcd) — closest technical analogy for the
    "finitely many primes can be recurrent" sub-claim (D2-(i)): its crux "gcd of a fixed
    element with a varying one takes only finitely many values (divisors of the fixed
    element), so pigeonhole over an infinite family forces repeats" and "when every prime
    divides only finitely many elements of an infinite set, only finitely many elements
    fail to be coprime to a fixed pair" are the right shape of tool, though the source
    problem (construct a "balanced triangle" of gcds in an infinite set) is not a tight
    match for our eventual-periodicity target — treat as a technique donor, not a direct
    template.
  - `aimo-0514` (combinatorics, processes-and-algorithms / invariants-and-monovariants) —
    the crux "a deterministic process is reversible (bijective on a finite state space),
    forcing the orbit to be purely (not just eventually) periodic" is conceptually
    relevant to the field's still-open "extend periodicity back to n=1" secondary gap: if
    an analogous reversibility/bijectivity could be established for the eventual
    residue-cycling map here, it might resolve that gap for free instead of via a
    case-by-case finite check. Worth flagging to the outliner as a possible mechanism for
    the SECONDARY gap, though the forward map here (smallest legal integer) is not
    obviously invertible (multiple predecessors could map to the same state), so this is
    a weaker analogy — flag as "worth a 10-minute check", not a load-bearing plan.
  - `aimo-0212` (number_theory, divisibility-and-gcd) — "show every prime dividing a
    polynomial's values lies in a fixed finite set, then invoke..." — same general shape
    (finite-prime-support arguments) as our Finite Core Theorem, but the actual mechanism
    (Fermat's little theorem exponent collapsing) doesn't transfer; listed only for
    completeness, not recommended as a technique donor.

- Prior progress: see `results/imo-2026-06/current.md` for the full unconditional
  chain (Free Facts, Bounded Gap Lemma, Persistent-Type Pigeonhole, Bounded Witness
  Lemma, Finite Core Theorem — all certified in `results/imo-2026-06/lemmas/`). The
  single blocking gap (†) is precisely stated there. Nothing in this report
  contradicts or reproves that chain; D1/D2/D3 are alternative ROUTES TO CLOSE (†) or
  bypass it, to be layered on top of (or run in parallel with) the existing chain, not
  a replacement for it.

- Dead ends (do not retry): the `hypergraph-transversal` approach's own Step 3 (a
  monovariant/potential-function argument for finiteness of S via Φ_n = Σ 2^{-min(B)})
  is under-specified and the approach file itself flags it doesn't close the loop
  without an "auxiliary growth argument" — do not re-attempt this exact potential
  function; it re-derives the same finiteness question the covering-system approach
  already solved cleanly (Finite Core Theorem) by a different, successful route
  (bounded witness pigeonhole, not a monovariant). The `density-sieve-contradiction`
  approach's raw sieve/Mertens sub-route (step 3) is flagged by its own author as
  probably intractable to make rigorous (modulus-growing-with-n density estimates); its
  step 4 ("each new recruited prime pays for itself") is NOT a dead end — it is exactly
  the idea D1 above develops further using minimality, so the builder should treat
  density-sieve-contradiction's step 4 as a live seed, not abandon it.

- Small-case / intuition notes (all CONJECTURE from numerics, not proof):
  - a_1=15 (Q={3,5}): extra prime recruited is exactly {2}; every type-{3} term is
    always (100% of 1500 sampled occurrences) exactly extended-type {2,3}; every
    type-{5} term is always exactly {2,5} (750/750). No refinement splitting observed
    at all — strong evidence for D1 in this case.
  - a_1=1155 (Q={3,5,7,11}, four disjoint singleton types all persistent): extra prime
    is again {2} essentially universally (2 divides 2500/2500 sampled non-a_1 terms);
    each singleton base type maps to a UNIQUE extended refinement (its own prime plus 2),
    with zero exceptions across hundreds of occurrences per type — again strongly
    supports D1's "single cheap universal witness" picture in the sparse-Q regime.
  - a_1=5005 (Q={5,7,11,13}): here 3 is ALSO recruited (appears in 1000/2999 extra-prime
    hits, alongside 2 in ~2998/2999), and each singleton base type genuinely SPLITS into
    two extended refinements (e.g. type {5} occurs 1016 times total, splitting into
    {2,5} 677 times and {2,3,5} 339 times) — i.e., (†)'s worried-about refinement
    splitting DOES occur in practice, but empirically it is harmless: every single one of
    the 8 observed refinements (2 base types × up to 2 refinements, times 4 base types)
    contains the prime 2, so all pairwise intersections trivially hold via 2. This is the
    cleanest concrete evidence that (†) is TRUE and that the reason it's true is a single
    dominant recruited prime, not a delicate multi-way combinatorial reconciliation —
    exactly the D1 mechanism.
  - a_1=30 (Q={2,3,5}) and a_1=210 (Q={2,3,5,7}): when Q itself already contains the
    smallest primes, NO single extra prime dominates the recruited pool (counts spread
    thinly across 7,11,13,17,19,23,... with the top only ~14% of occurrences for a_1=30)
    — the D1 mechanism (single universal cheap witness) does NOT obviously apply here in
    its clean form; this is the genuinely harder regime and is exactly why D3 (case split
    sparse-Q vs. dense-Q) is proposed rather than claiming D1 alone finishes the problem.
  - All numerics were generated by direct greedy simulation in Python (sympy factorint +
    the actual defining recurrence), not analytically derived — label all of the above
    as conjecture/evidence, not proof.
