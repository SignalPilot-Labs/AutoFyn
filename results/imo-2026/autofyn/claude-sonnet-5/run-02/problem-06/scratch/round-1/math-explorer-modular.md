## imo-2026-06

- Distinct openings (modular/congruence-class lens):
  1. **Intersecting-family-of-prime-sets framing.** For every n, the condition
     "gcd(a_{n+1},a_i)>1 for all i≤n" is exactly: the sets of prime divisors
     P(a_1), P(a_2), ... form a *pairwise-intersecting family*. In particular
     the i=1 instance is unconditional and elementary: for every n≥2,
     gcd(a_n,a_1)>1, so **a_n is divisible by some prime factor of a_1** — this
     holds for ALL n, not just eventually, and it is a genuinely proved fact
     (immediate from the hypothesis with i=1), not a conjecture. This bounds
     the "seed" prime set Q=P(a_1) (finite, size ≤ log2(a_1)) a priori, and
     frames the whole problem as: an infinite pairwise-intersecting family of
     finite prime-sets, each containing a member of Q, subject to a greedy
     "smallest available integer" selection rule. This is a genuinely
     different top-level target than "prove primes stabilize by growth-rate
     argument": it's closer to extremal set theory / Helly-type reasoning on
     intersecting families, which might let the outliner attack "finiteness
     of ever-used primes" via a counting/covering argument on Q rather than a
     raw density argument.
  2. **Direct congruence/CRT-covering framing** (the assigned lens). Conjecture:
     there is a finite locked prime set S ⊇ Q (Q from opening 1, possibly with
     extra "helper" primes not dividing a_1) and an index n0 such that for all
     n>n0, a_n is divisible by at least one prime in S, AND the pattern of
     which primes are used to satisfy each pairwise gcd condition becomes
     eventually determined purely by residues mod L := lcm of the locked prime
     powers actually used (empirically L is just the squarefree product of S,
     the "primorial" of the locked set in all cases checked). Concretely: past
     n0, whether an integer m qualifies as the next term reduces to a check
     depending only on m mod L (once "already used" bookkeeping also becomes
     periodic mod L), giving strict eventual periodicity of the gap sequence
     with period T·(number of terms per residue block) and step L.
  3. **State-compression / pigeonhole-on-finite-state framing** (see crux
     aimo-0678 below): instead of proving prime-set finiteness first, define
     an auxiliary "signature" state per index n — e.g. (which residues mod a
     growing candidate L have already been consumed within the current block)
     — and show this signature, suitably normalized, lives in a bounded/finite
     set once a threshold invariant (a monovariant, analogous to `w_n` in
     aimo-0678) stabilizes. Two occurrences of the same state force periodicity
     by determinism of the greedy rule. This sidesteps needing to *characterize*
     S explicitly — only that *some* finite bookkeeping state repeats.
  4. **Growth-rate / density framing** (mentioned for completeness, not the
     assigned lens): a_n divisible by a prime ≤ some bound forces a_n to lie
     in a set of positive density; comparing "number of integers ≤ x divisible
     by ≥1 of the current prime set" against the actual count of terms ≤ x
     could bound how many distinct primes can ever be introduced (each new
     prime "costs" relative density but the greedy rule always wants the
     smallest available integer, biasing toward reusing cheap small primes).
     This is the likely engine behind why the prime set is finite, but making
     it rigorous (opening the outliner would need) requires quantifying "how
     much a genuinely-new large prime factor costs" vs "reusing an existing
     locked prime," which is the hard step.

- Candidate technique(s): CRT / modular arithmetic (KB "Modular arithmetic,
  CRT"), pigeonhole on a finite state space (used generically in KB
  "Pigeonhole / extremal principle" and in the analogous crux below),
  monovariant/invariant tracking (KB "Invariants & monovariants"), intersecting
  families / covering-system style casework. No KB entry names "covering
  system" explicitly — the closest is "Modular arithmetic, CRT" (KB Number
  Theory section) which should be cited generically for the CRT combination
  step once the locked prime set is fixed.

- Cheap-kill candidates:
  - The Q = P(a_1) fact above (proved, not conjectured) — an immediate,
    rigorous a priori bound on one necessary ingredient of the eventual
    locked-prime set. Cheap and should anchor whichever approach is chosen.
  - Parity/size check: a_1 itself, if prime or a prime power (Q singleton),
    forces the WHOLE sequence to be exactly the multiples of that one prime
    from a_1 onward (T=1, L=p) — trivial case, confirmed numerically (a_1=2,
    3, 4, 5, 6, 7, 10, 12 all gave straight arithmetic progressions). Any
    general proof must handle this as the degenerate base case, but it also
    means the "interesting" combinatorics only kicks in when a_1 has ≥2
    distinct prime factors.

- Knowledge-base entries to use:
  - "Modular arithmetic, CRT" (Number Theory) — combine residues once the
    locked prime set/period is known.
  - "Order of an element, Fermat/Euler … eventual periodicity of products of a
    sequence mod m" (Number Theory) — general eventual-periodicity-mod-m
    pattern, directly on point for framing the conclusion.
  - "Linear recurrences … sequences are eventually periodic mod m" (Number
    Theory) — same family of results, cite for the general principle that a
    process with finite state is eventually periodic.
  - "Pigeonhole / extremal principle" and "Invariants & monovariants"
    (Combinatorics / General Proof Methods) — the generic engine for turning
    "finite state + determinism" into periodicity, exactly as used in the
    aimo-0678 crux below.

- Analogous past problems (cruxes):
  1. **aimo-0678** (IMO Shortlist 2015, France) — "Suppose a_0,b_0≥2,
     a_{n+1}=gcd(a_n,b_n)+1, b_{n+1}=lcm(a_n,b_n)-1; prove (a_n) is eventually
     periodic." This is the single best analog found: same *shape* of claim
     (eventual periodicity of an integer sequence built from a greedy/gcd-lcm
     rule), and its crux move is exactly the modular/state-compression idea:
     Solution 1 defines a monovariant `w_n` = smallest value ≥ a_n not
     dividing s_n = a_n+b_n, proves `w_n` non-increasing hence eventually
     constant = w, then shows `g_n = gcd(w, s_n)` is eventually constant too,
     giving an explicit repeating cycle. Solution 2 is even closer to the
     assigned lens: bound `a_n` (finite range), take `M = lcm` of all values
     `a_n` ever takes, reduce `b_n mod M` to `r_n`, and show the pair
     `(a_n, r_n)` — living in a **finite** set — is stepped forward by a
     **deterministic** map, so pigeonhole on repeated pairs forces eventual
     periodicity. This "reduce to a finite (bounded value, residue mod M)
     state pair, argue determinism, pigeonhole" pattern is the crux move to
     adapt: in our problem the analogous finite state would need to package
     (recent history mod L, which residues mod L are "already used" in the
     current block) — but unlike aimo-0678, `a_n` itself is UNBOUNDED here
     (it's the gap/period we want, not the value), so the state must be built
     from *residues* and *usage bookkeeping*, not from a_n directly. This is
     a real gap to close, not a direct transplant.
  2. **aimo-0447** (essentially ISL/IMO-flavor, "gcd(a+i,b+j)>1 for all
     i,j∈{0,...,n} ⟹ min{a,b} > (cn)^{n/2}") — relevant only as a *sibling*
     structural fact: it shows that families forced to have pairwise gcd>1
     across a whole grid must be seeded by large primes / grow fast, via a
     prime-counting argument (grid of primes, each prime covers few cells,
     PNT bound). Its technique (place a witness prime in each cell, bound how
     many cells one prime can cover, count) is the kind of "covering by
     primes" combinatorics that could be adapted to bound how many *new*
     primes the greedy sequence can introduce — but the setup (grid, not a
     1-D increasing greedy sequence) is different enough that this is a
     structural cousin, not a template to copy directly.
  - No other crux in the corpus (searched number_theory subtopics
    modular-arithmetic-and-CRT, divisibility-and-gcd, sequences-and-recurrences,
    induction-and-construction, and a keyword sweep for "intersect") was a
    close match; most "intersecting family" hits were combinatorics/geometry
    problems about literal set/line intersections, not divisor-set families.

- Prior progress: none — round 1, workspace empty.

- Dead ends (do not retry): none recorded yet (first round).

- Small-case / intuition notes (all conjecture from direct computation, not
  proof):
  - Built the actual sequence in Python (gcd-based greedy) for several
    seeds. When a_1 is a prime or prime power, Q is a singleton and the
    sequence is trivially the arithmetic progression of multiples of that
    prime from step 1 (T=1, L=p). E.g. a_1=2 ⟹ all evens; a_1=5 ⟹ all
    multiples of 5.
  - For a_1 with ≥2 distinct prime factors the behavior is richer and
    genuinely eventually periodic in the gaps, confirming the theorem
    numerically:
    - a_1=15 (=3·5): diffs immediately periodic with T=8, L=30=2·3·5. The
      locked prime set is exactly {2,3,5} (every term divisible by 2, 3, or
      5 — verified by factoring the first 60 terms) even though 2 does not
      divide a_1; 2 gets "recruited" as a cheap helper prime.
    - a_1=35 (=5·7): T=34, L=210=2·3·5·7 — locked set is the full primorial
      of {2,3,5,7}, again recruiting 2 and 3 beyond a_1's own primes {5,7}.
    - a_1=143 (=11·13): T=64, L=858=2·3·11·13 — locked set {2,3,11,13}.
    - a_1=1001 (=7·11·13): T=282, L=2002=2·7·11·13 — locked set {2,7,11,13}
      **excludes 3** (unlike the a_1=143 case), showing the locked set is not
      simply "a_1's primes plus all small primes" — it's sensitive to which
      helper primes are actually needed/cheapest, so characterizing S
      requires real argument, not a generic small-primes heuristic.
    - Verified directly (definitional, not just empirical) that for every n≥2,
      a_n shares a prime factor with a_1 specifically — checked by factoring
      terms in the a_1=1001 run: every term divisible by 7, 11, or 13.
    - L in every non-trivial case observed so far equals the **squarefree
      product (primorial) of the locked prime set**, never a higher prime
      power multiple — consistent with a conjectural "L = product of locked
      primes" shape for the theorem's L, though T itself doesn't match a
      simple closed form I found (checked T vs φ(L): matches for L=30 (T=8=
      φ(30)) but NOT for L=2002 (T=282 ≠ φ(2002)=720) or L=858 (T=64 vs
      φ(858)=240) — so "T=φ(L)" is false in general; T's value needs its own
      argument, likely counting how many of the "eligible" residues mod L
      actually get selected by the greedy rule per block, not all of them
      (e.g. for L=30 only 8 of the 22 non-coprime-to-30 residues mod 30
      appear in the repeating diff-pattern, so the periodic block is a
      genuine subset, not "all multiples of the locked primes").
  - Overall picture: the eventual periodicity phenomenon is real and robust
    across seeds (matches the theorem's claim), the locked prime set is
    always a finite superset of P(a_1) plus a few small "helper" primes, and
    L is (conjecturally, in all tested cases) the squarefree product of that
    locked set — but exactly which helper primes join, and the precise value
    of T, are seed-dependent and not captured by any simple closed form found
    by this exploration; a full proof needs to (a) show finiteness of the
    locked prime set rigorously (the hard step — no clean argument found yet,
    growth-rate/density heuristic in opening 4 is the most promising avenue),
    and (b) show that past stabilization the selection process becomes an
    eventually-periodic walk on residues mod L (openings 2–3 give two
    different routes to formalize this second step once (a) is granted).
