## imo-2026-06

- Distinct openings (all under the "prime-witness graph/covering" framing assigned):
  1. **Covering-hypergraph view.** For each n, the requirement "gcd(a_{n+1},a_i)>1 for ALL i=1..n"
     means: the *set of primes dividing a_{n+1}* must intersect the prime-factor set of
     *every single earlier term*, not just one. Model this as: place a hyperedge for each
     term's prime-factor set; a_{n+1} is admissible iff its prime set is a "transversal"
     (hits every earlier hyperedge). This is exactly the same encoding as crux `aimo-0447`
     (grid of gcd's filled by a witness prime per cell) — but there the goal is a **lower
     growth bound** forced by *too many* transversal primes needed; here we want the dual
     fact that the transversal-prime demand **stabilizes to a bounded/periodic structure**
     rather than blowing up.
  2. **"Anchor prime of a_1" opening.** If a_1 is a prime power p^k, EVERY future term is
     forced to be a multiple of p (since gcd(a_{n+1},a_1)>1 and a_1's only prime factor is p),
     which collapses the whole problem trivially: the sequence becomes exactly p,2p,3p,4p,...
     (verified computationally, see below) — T=1, L=p immediately. This is a clean, fully
     provable special case that could seed an induction/reduction: show general a_1 reduces,
     after finitely many steps, to "some prime becomes an eventual anchor for a sub-family",
     or more precisely to a *bounded set* of anchor primes acting jointly.
  3. **Finite covering-set + CRT-periodicity opening (the main mechanism, see below).**
     Conjecture: there is a finite set of primes H (H ⊇ primes dividing a_1, plus finitely
     many "helper" primes recruited during a finite transient) such that (a) from some N₀ on,
     every a_n (n≥N₀) is divisible by at least one prime in H, and (b) the residues of a_n
     mod L := ∏_{p∈H} p (or lcm) that occur form a *fixed, pairwise-compatible* set that,
     once established, is self-sustaining forever by the greedy rule. Then periodicity
     T,L falls out because CRT makes divisibility-by-H a period-L phenomenon, and the
     specific admissible residue subset mod L is forced to repeat once it first repeats
     (a finite-state / pigeonhole argument, matching crux `aimo-0678`'s "reduce the unbounded
     coordinate mod the lcm of the bounded coordinate's values, turn the process into a
     finite-state map" pattern, and `aimo-0982`'s "sampling index mod the period" idea).
  4. **Dichotomy / contradiction opening.** Split into: either (i) infinitely many *distinct*
     primes are each used to satisfy the gcd condition for infinitely many indices (i.e. H
     as above is infinite), or (ii) H is finite. Try to derive a contradiction from (i) via a
     counting/density argument in the flavor of `aimo-0447`'s prime-counting sum
     (Σ_p ⌈N/p⌉² style bound) — i.e. show that if too many distinct "load-bearing" primes were
     needed, the greedy minimal choice would be forced to jump by more than what's actually
     observed (gaps stay small/bounded in every experiment run, see below), or would need
     ω(a_n) → ∞, contradicting an achievable-growth bound. This is the least explored opening
     and probably the hardest gap — flagged as open territory, not attempted here.

- Candidate technique(s): finite-state pigeonhole / eventual periodicity of a bounded-range
  recurrence (KB "Linear recurrences ... eventually periodic mod m", generalized here to a
  covering condition instead of a literal recurrence); CRT to assemble a periodic residue
  pattern from independent prime conditions; minimal-counterexample / extremal choice
  (greedy always picks smallest admissible candidate — a genuine monovariant/extremal
  principle); "Bertrand's postulate"-style prime density bounds if the dichotomy opening
  (4) is pursued to rule out unboundedly many load-bearing primes.

- Cheap-kill candidates:
  - **Prime-power a_1 is trivial** (opening 2): a one-line disposal of that sub-case, worth
    stating explicitly so the outline doesn't waste effort re-deriving it.
  - **v_2 / parity is not universally forced**: computationally, 2 is *not* always in the
    eventual covering set structurally required — e.g. a_1=21=3·7 locks into "all multiples
    of 3" (T=1, L=3) without prime 2 ever being load-bearing; so any approach assuming "2
    always wins" is wrong. Only report as an observation, not a valid pruning shortcut.
  - **ω(a_n) (number of distinct prime factors) stays small and bounded** in every run tried
    (max observed 4–5 over 400+ terms across 5 different starting values) — this is a
    *cheap empirical filter*: if an approach's argument requires ω(a_n) → ∞, it is very
    likely on the wrong track and should be deprioritized quickly.
  - **max gap stays bounded** (observed max gaps 2–14 across all tested starts, no growth
    trend over 400–3000 terms) — another quick empirical sanity check for any bound claimed
    in a sub-argument.

- Knowledge-base entries to use:
  - "Modular arithmetic, CRT" (combine independent prime-divisibility conditions into one
    periodic residue-mod-L structure).
  - "Order of an element, Fermat/Euler" / "Linear recurrences ... eventually periodic mod m"
    (general template: finite state ⇒ eventual periodicity by pigeonhole).
  - "Pigeonhole / extremal principle" and "Invariants & monovariants" (the greedy minimality
    of a_{n+1} is itself an extremal choice / monovariant-adjacent structure worth exploiting
    directly, e.g. a_{n+1} ≤ a_n + (something bounded by the current covering-prime set)).
  - "Divisor analysis" (gcd structure, consecutive-integer coprimality) for bounding gaps.
  - "Bertrand's postulate" is a plausible tool if a density/counting argument (opening 4) is
    needed to bound how many small primes can be "load-bearing" at once, though no concrete
    fit is confirmed yet — flag as speculative.
  - NOT directly useful here (checked and ruled out as centerpieces): LTE, Zsigmondy,
    Vieta jumping, Dirichlet primes-in-AP (none of the observed mechanism needs manufacturing
    a prime in a residue class — the primes involved are always small and already present).

- Analogous past problems (cruxes):
  - **`aimo-0447`** (ISL-flavored: prove gcd(a+i,b+j)>1 for all i,j∈{0..n} forces
    min{a,b} > (cn)^{n/2}). Crux move: build an (n+1)×(n+1) grid, put a witness prime in
    each cell (i,j) dividing gcd(a+i,b+j), then bound how many cells small primes can occupy
    (Σ_p ⌈N/p⌉² style) to show most witnesses must be large primes, forcing a and b huge.
    **Genuinely analogous**: it is the *same encoding* (prime-covering of an all-pairs gcd
    condition) as our problem's requirement "a_{n+1} shares a factor with every earlier a_i."
    The direction of the inequality is reversed (they prove growth is forced large; we need
    eventual boundedness/periodicity of the *witness prime set*), but the grid/covering
    machinery is the most on-point transferable tool found in the corpus.
  - **`aimo-0678`** (coupled recurrence (a_n,b_n) with a_n bounded ⇒ reduce b_n mod
    lcm(a_n-values) ⇒ finite state space ⇒ eventual periodicity by pigeonhole). Crux
    move is the clean template for "collapse an unbounded coordinate to a finite state via a
    fixed modulus, then invoke pigeonhole on the finite state space to get periodicity" —
    structurally the shape I expect the final periodicity argument in our problem to take,
    once a finite covering-prime set H (hence modulus L=∏H) is established.
  - **`aimo-0421`** (infinite set S of integers, pigeonhole on gcd values since gcd(a,·) is a
    divisor of the fixed a, hence takes finitely many values). Weaker analogy but the same
    "gcd against a fixed element has bounded range, pigeonhole over an infinite family" idea
    could be reused for a sub-lemma (e.g. gcd(a_1, a_n) stabilizing — cf. also `aimo-0477`
    below).
  - Also worth the outliner's attention (secondary): **`aimo-0477`** — "Track gcd(fixed term,
    current term); v_p nondecreasing per prime ⇒ divisor chain stabilizes" — a reusable
    micro-lemma pattern (gcd(a_1, a_n) is non-decreasing along a divisor lattice bounded by
    a_1, so it stabilizes) that could underlie why the finite covering set H exists at all.
  - Not a match: `aimo-0224` (constructing a sequence with prescribed pairwise-coprimality
    via disjoint index-sets of primes) — that's a *construction* problem in the reverse
    direction (design a sequence), not a structural-forcing argument; noted but not
    recommended as a template.

- Prior progress: none (fresh workspace, round 1, no approaches registered yet).

- Dead ends (do not retry): none recorded yet (first round).

- Small-case / intuition notes (all empirical / conjectural, verified only by simulation up
  to n≈400–3000 for several starting values via direct greedy Python simulation, gcd via
  Euclidean algorithm — NOT a proof):
  - If a_1 is even, the sequence *immediately* becomes all even numbers (a_n = a_1 + 2(n-1)),
    T=1, L=2 — trivial, verified for a_1 ∈ {2,4,6,8,10,12,30,210}.
  - If a_1 is an odd prime power p^k, the sequence is forced to be exactly the multiples of p
    (p, 2p, 3p, ...) from a_2 on (since a_1's unique prime factor p must divide every later
    term) — T=1, L=p — trivial, verified for a_1 ∈ {3,5,7,9,25,49,55(wait 55=5·11, still
    T=1,L=5 — needs re-checking, see caveat below)}.
  - **Caveat/open question**: a_1=55=5·11 (two distinct primes) *still* empirically locked to
    T=1, L=5 (pure multiples of 5) rather than needing a richer covering set — i.e. having
    ≥2 prime factors in a_1 does NOT guarantee a nontrivial multi-prime periodic structure;
    sometimes one prime "wins" the greedy race outright and the other becomes irrelevant
    after the very first step. Contrast with a_1=15=3·5 or a_1=35=5·7, which DO produce
    richer multi-prime periodic patterns (T=8,L=30 and T=34,L=210 respectively). The outliner
    should treat "does a single prime end up dominating trivially, or does a genuine
    multi-prime residue-covering structure emerge" as a case split that any general proof
    must handle uniformly — the mechanism (finite covering set H, CRT residues mod
    L=∏H) is conjectured to unify both, with |H|=1 being the degenerate sub-case.
  - For genuinely multi-prime cases the empirical period data is: a_1=15 ⇒ T=8, L=30,
    H={2,3,5}; a_1=45,75 (same H) ⇒ same T=8,L=30; a_1=35 ⇒ T=34, L=210, H={2,3,5,7}
    (note: 3 is a "helper" prime not dividing a_1=35 at all, yet ends up load-bearing);
    a_1=105=3·5·7 ⇒ T=58, L=210, H={2,3,5,7}; a_1=77=7·11 ⇒ T=18, L=154, H={2,7,11};
    a_1=91=7·13 ⇒ T=20, L=182, H={2,7,13}; a_1=65=5·13 ⇒ T=58, L=390, H={2,3,5,13}
    (again 3 is a helper prime absent from a_1). **Conjecture**: L is always the product of
    (i) the (odd) primes dividing a_1, plus (ii) a small bounded number of extra "helper"
    primes (2 always shows up as a helper whenever it's not already forced; 3 shows up as a
    helper in some cases where a_1 lacks both 2 and 3) recruited during a finite transient.
  - Every term a_n (n large) in every multi-prime example checked is divisible by **at least
    one prime of H**, confirmed by direct factorization for hundreds of consecutive terms in
    two cases (a_1=15, a_1=35) — this is the strongest direct evidence for the "finite
    covering set" mechanism (opening 3 above), though the *mechanism forcing H to be finite*
    (rather than growing forever) is NOT yet understood/proved — this is the actual hard gap
    the outliner needs a real argument for, and where the crux `aimo-0447` grid-counting
    style (or a dichotomy per opening 4) is the most promising lead found.
  - ω(a_n) (count of distinct prime factors) stayed in the range 3–5 across all runs, never
    trending upward over hundreds of terms — consistent with (but not proof of) H being
    finite and bounded gaps.
