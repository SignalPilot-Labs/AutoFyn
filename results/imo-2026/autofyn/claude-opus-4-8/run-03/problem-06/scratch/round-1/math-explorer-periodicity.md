## imo-2026-06

### Simulation setup
Implemented the greedy rule directly in Python (`gcd` from `math`): for each `a1`,
repeatedly append the smallest `c > a_n` with `gcd(c, a_i) > 1` for every prior term
`a_i` (checking against the FULL history, not just a window). Ran for many `a1` and
up to several thousand terms, then searched for `T,L` with `a_{n+T} = a_n + L` holding
on a long tail window, and separately checked whether it already holds from `n=1`.

### Hard empirical facts (raw data)

**Trivial-immediately cases** (`T=1` from the very first term):
- `a1=2,4,6,8,10,12,30,42,70,...` (any a1 divisible by 2): gaps are all `2` forever.
  `T=1, L=2`.
- `a1=3,9,33,231,...` (a1's smallest prime factor is 3, and 2 is never "recruited"):
  gaps all `3` forever. `T=1, L=3`.
- `a1=5,25,55` -> gaps all `5`. `a1=7,49` -> gaps all `7`.
- General pattern for `a1 = p*q` (two distinct primes, or a prime power): sequence
  becomes `a_n = a_1 + (n-1)*p_min` immediately, where `p_min` = smallest prime
  factor of `a_1`. (Verified for 6,10,12,14,15✗(see below),21,33,35,42,55,70,77✗,105✗,...)
  NOT universal — see below, this fails once the odd prime factors of `a1` are close
  enough together to force complicated early interaction.

**Non-trivial genuinely-periodic-from-n=1 cases** (the interesting terrain):
- `a1 = 15 = 3*5`: gaps cycle with period `T=8`: `[3,2,4,6,6,4,2,3]` repeating from
  the very first gap; `L = sum = 30 = 2*3*5`. So even though `15` is odd, the prime
  `2` gets "recruited" into the eventual modulus.
- `a1 = 45 = 3^2*5`: identical gap-cycle to `a1=15` (same period 8, same `L=30`) —
  the multiplicity of primes in `a1` doesn't matter, only which primes divide it.
- `a1 = 105 = 3*5*7`: gap-cycle has period `T=58`, `L=210=2*3*5*7`. Confirmed
  **periodic from n=1** (checked over 1000 terms, tail window of 300 gaps all match
  with offset 58, and checked the whole gap list from index 0). Confirmed by an
  independent check: in the tail, residues mod 210 that occur among the a_n are
  exactly 58 distinct residues (matches T), and every single term of the sequence
  (checked over 1000 terms) is divisible by at least one of {2,3,5,7} — no term is
  coprime to 210. `a1 = 11025 = 3^2*5^2*7^2` gives the *same* `T=58, L=210` (same
  prime set as 105 → identical eventual modulus, confirming L, T depend only on
  the recruited prime set, not on a1's exact value/multiplicities).
- `a1 = 1155 = 3*5*7*11`: period `T=676`, `L=2310=2*3*5*7*11`. Confirmed
  **periodic from n=1** over 4000 terms (built in <1s with an $O(n)$-per-step gcd
  loop). Again prime 2 gets recruited; L = product of {2}∪(distinct prime factors
  of a1).
- `a1 = 385 = 5*7*11`: did NOT stabilize within maxT=3000 over 15000 terms — growth
  is large (last term ~130000) and true `T` appears to exceed 3000 (not confirmed).
  However every term (checked, no exceptions) is divisible by one of {2,5,7,11},
  and residues mod `770 = 2*5*7*11` used in a tail window stabilize to a count of
  154 (close to but not yet confirmed as the exact period — evidence is consistent
  with the same qualitative mechanism, just a longer transient to search for T).
- `a1 = 315 = 3^2*5*7` (same prime radical as 105 but different a1): did not find
  period within a comparable search window (maxT up to 700, 6000 terms) — needs a
  longer search; conjectured (not confirmed) to converge to the same `L=210` as 105
  eventually, but T (and whether "from n=1" holds for this start) is unconfirmed.

### Key qualitative conjecture (from the data, NOT proved)
1. There is a **finite set of primes P** (depending on `a1`) that gets "recruited":
   from some point on (possibly n=1), *every* term of the sequence is divisible by
   at least one prime in P, and P eventually stops growing.
2. Once P is fixed, `L = ∏_{p∈P} p` (the radical/product, since the primes are
   distinct) is the shift, and the sequence's residues mod L stabilize to a fixed
   set of `T` residues (T = number of distinct residues mod L that occur), giving
   `a_{n+T} = a_n + L`.
3. `2 ∈ P` in every non-trivial case tested where `a_1` was odd with ≥2 distinct odd
   prime factors close together (15, 45, 105, 11025, 1155) — 2 is recruited even
   though it never divides `a_1`. Mechanism (informal): once the sequence needs
   to place a term between two "far apart" multiples of the existing primes, taking
   an even number lets it satisfy the gcd condition against *any* other term that
   also happens to be even, generating a self-reinforcing even sub-family.
4. When `a_1`'s smallest prime factor `p_min` is small and the *other* prime factors
   of `a_1` are spread far enough apart (e.g. 231=3*7*11 vs 105=3*5*7), the process
   locks onto the trivial `T=1, L=p_min` behavior immediately without recruiting 2
   or any other prime — so the "recruit 2" phenomenon is NOT universal, it depends
   on the specific gaps between a_1's prime factors. This is a genuinely delicate
   dependency that the proof needs to handle uniformly (i.e., the proof cannot
   assume 2 is always recruited — it must show *some* finite prime set stabilizes,
   whatever it turns out to be).
5. In every case checked where a period WAS found (15,45,105,11025,1155,and all
   trivial cases), the periodicity held **from n=1 itself** — no genuine "eventual"
   transient was needed before periodicity started (though the *search* sometimes
   needed a long window to detect the period T, because T can be as large as ~700+
   for 4-5 recruited primes). This supports reading the problem statement literally:
   "for every positive integer n" is not asking for eventual periodicity dressed up
   as global — the intended T, L genuinely work from n=1, at least in all examples
   found. (Still only empirical; not a proof that T,L can always be taken globally
   valid rather than after some fixed offset — the problem only asks existence of
   T, L with the property holding for all n, which is compatible with L being the
   modulus of an eventually-periodic-from-the-start sequence.)

### Distinct openings for the outliner
- **(A) Finite active-prime-set argument.** Show that only finitely many primes
  ever serve as the "witness" prime for gcd(a_{n+1},a_i)>1, for infinitely many i
  as n→∞ — i.e. show the set of primes appearing as prime factors of infinitely
  many terms is finite. This is the crux fact underlying L's existence as a finite
  modulus. Likely needs a density/growth argument: if the process needed
  arbitrarily many new "structural" primes to keep going, the terms would grow
  too fast / too slow relative to known density bounds (contradiction via a
  counting or size argument, in the spirit of `knowledge_base.md`'s "Divisor
  analysis" and "Modular arithmetic, CRT" entries).
- **(B) Finite-state / pigeonhole periodicity argument.** Once the active prime
  set P is known finite with `L=∏P`, encode the "state" of the process at each
  point n as some FINITE data (e.g., which residues mod L have appeared among the
  last several terms, or "coverage status" per prime in P — i.e., for each p∈P,
  the residue class mod p that the most recent term(s) supplying that witness
  occupy). Argue the state space is finite, hence (by determinism of the greedy
  rule + pigeonhole) the state must repeat, forcing the gap sequence to become
  eventually periodic; then argue this periodicity in fact begins immediately
  (matches the "for every n" in the statement) or falls back to "eventually
  periodic ⟹ can shift index" if it doesn't literally start at n=1 (the T,L in
  the problem need not start at n=1 for T itself, since the claim is "there
  exist T,L such that for ALL n, a_{n+T}=a_n+L" — this is a strictly global
  claim, so if there's a genuine pre-periodic transient anywhere the naive
  "eventually periodic" argument does NOT suffice and a sharper argument is
  needed to show the recursion is actually already in its periodic regime from
  the start, OR that whatever transient exists can still be folded into a single
  global (T,L) pair by using L large enough / T = a period that's also consistent
  with the transient values). **This is likely the single hardest gap**: eventual
  periodicity (standard pigeonhole) gives T,L valid for n ≥ some N₀, NOT for all
  n ≥ 1 as the problem literally demands. Bridging N₀ down to 1 is nontrivial and
  is exactly where an approach could get stuck — but our simulations show it
  really does hold from n=1 in every case tested, so there should be a clean
  argument (perhaps: run the SAME finite-state argument starting from a1 itself,
  since the "state" is well-defined from the very start, not just eventually).
- **(C) Modulus-first construction / verification opening.** Guess the modulus
  L directly as `∏` over the finite prime set that must arise (define it via an
  extremal/limiting argument on which primes divide infinitely many terms), then
  show the sequence restricted mod L is forced into a periodic orbit by a
  self-consistency / greedy-invariance argument (the greedy choice only depends
  on residues mod L once P is fixed) — reduces the infinite problem to a finite
  computation on Z/LZ.
- **(D) Direct CRT/sieve reformulation.** Reformulate "gcd(a_{n+1},a_i)>1 for all
  i≤n" as "a_{n+1} lies outside the sieve of numbers coprime to every a_i" — once
  the prime factorizations of a_i's stabilize to only involve P, the sieve
  condition becomes purely a function of residue mod L=∏P, giving a finite
  automaton on residues mod L whose transition is eventually periodic by
  pigeonhole on its (finite) state space — closely related to (B) but framed as
  a sieve/automaton rather than a "recruit primes" narrative.

### Candidate technique(s)
- Modular arithmetic & CRT (knowledge_base.md "Modular arithmetic, CRT") — central:
  once primes are finite, work entirely mod L=∏(primes in P).
- Pigeonhole / extremal principle (knowledge_base.md "Pigeonhole / extremal
  principle", "Constructive/incremental") — for both showing P is finite (else an
  extremal/size argument breaks) and for showing the process is eventually periodic
  (finite state space).
- Divisor analysis (knowledge_base.md) for bounding growth of a_n and controlling
  which primes can appear.
- Invariants/monovariants (knowledge_base.md) — a natural invariant candidate: the
  set of primes that have appeared "recently enough" to still be witnessing
  coprimality; show this set stabilizes.

### Cheap-kill candidates
- Parity/size pruning: none obvious as a full proof shortcut, but a useful
  sanity check is: **every term from a1 on must share a prime with a1** (since
  gcd(a_{n+1},a_1)>1 for the very first index i=1, this holds for ALL n). So
  **every single term in the whole sequence is divisible by some prime factor of
  a1** — this is an immediate, clean, and provable structural fact (not just
  conjecture) worth stating first: it bounds the prime factors relevant to a1
  itself, though NOT the full "active set" P (which can include recruited primes
  like 2 that do not divide a1, as seen in the 105/1155 cases — a1's own prime
  factors are only witnesses for gcd against a1, but a_{n+1} could satisfy that
  via a DIFFERENT one of a1's factors than the recruited prime witnessing gcd
  against some other term). This distinction (constraint from a1 alone vs. the
  full accumulated prime set) is a good structural anchor to build the outline on.
- v_p count: not obviously useful directly, but note each a_i's factorization only
  needs to matter through which of the (eventually finite) "active" primes divide
  it — multiplicities are irrelevant (confirmed empirically: 45 vs 15, and 11025
  vs 105 give IDENTICAL L, T despite very different multiplicities).

### Knowledge-base entries to use
- "Modular arithmetic, CRT" (mod L reduction once primes are fixed).
- "Pigeonhole / extremal principle" and "Invariants & monovariants" (finite-state
  periodicity argument).
- "Divisor analysis" (bounding growth / prime recruitment).
- Possibly "Order of an element, Fermat/Euler" entry's line "eventual periodicity
  of products of a sequence mod m" — directly analogous phrasing, worth citing as
  the generic template this problem specializes.

### Analogous past problems (cruxes)
- `aimo-0224` (IMO-shortlist-style, "does there exist a sequence with a_m,a_n
  coprime iff |m-n|=1"): crux move is to **encode a prescribed pairwise-
  coprimality pattern by assigning a distinct prime to each element of a ground
  set** and building each term as a product of primes over a chosen finite subset,
  so gcd-coprimality of two terms becomes disjointness of prime-index subsets.
  This is a genuinely useful conceptual lens (not a solution template) for
  reasoning about WHY the "active prime set" behaves the way it does — thinking
  of each term as "the set of primes it uses" clarifies the coprimality-graph
  structure, though the construction direction (existence) differs from our
  proof direction (forced periodicity of a greedily-defined sequence). Worth
  citing as an analogy for modeling, not a proof recipe.
- `aimo-0144` ("nth smallest integer coprime to n is at least σ(n)"): crux move
  is the **"any window of d consecutive integers contains exactly φ(d) integers
  coprime to d" counting fact**, applied via a clever partition of an interval
  into consecutive blocks whose lengths are the divisors of n. This "windowed
  coprimality count" tool is a natural building block for counting how many
  integers in a period `L` fail to be divisible by any prime in the active set,
  and could help pin down `T` as a density computation on `Z/LZ` once `P`,`L`
  are fixed. Genuinely analogous in TECHNIQUE (density/counting on windows mod a
  fixed modulus) even though the source problem is different in shape.
- `aimo-0212` (rad(f(n)) divisibility condition, forcing f(x)=ax^m): crux move
  is **"show every prime dividing [some family of values] lies in a fixed finite
  set, then leverage that a finitely-supported-prime-set object is very
  restricted"** — directly analogous in SPIRIT to opening (A) above (showing the
  active prime set P is finite). Worth reading for the style of argument that
  proves finiteness of a prime set from a growth/structural constraint, though
  the concrete mechanism (radical divisibility of polynomial values vs. gcd with
  all previous greedy terms) is different — treat as a technique analogy, not a
  literal template.
- No crux found that is a literal match to this exact "greedy smallest-integer-
  sharing-a-factor-with-all-previous" recursive definition; searched problem
  statements for "smallest"+"gcd" and "periodic sequence" combinations, found
  nothing structurally identical. This appears to be a genuinely novel-flavored
  construction (possibly inspired by, but distinct from, "Ulam-style greedy
  sequences" / Eratosthenes-sieve dynamics) not present in the pre-2026 corpus.

### Prior progress
None — round 1, no `results/imo-2026-06/approaches/` exist yet (confirmed: directory
listing showed only `approaches/` and `lemmas/` subfolders with no files, and
`current.md` does not exist).

### Dead ends (do not retry)
None recorded yet (first round). One important **empirical caution**: do NOT
assume "T=1, L=p_min(a1)" is the answer in general — it is a trap that appears
to hold for a majority of small random a1 (all my early tests except a1=15
looked trivial), but breaks for a1 with 3+ distinct odd prime factors close
together (105, 1155, 15, 45) where 2 gets recruited and T,L become large. Any
approach that tries to prove "L is simply the smallest prime factor of a1"
will be falsified by a1=105 (L=210 ≠ 3).

### Small-case / intuition notes (all conjecture from simulation, not proof)
- Conjecture: `L = ∏_{p ∈ P} p` where P is the eventual finite set of primes such
  that every sufficiently large term is divisible by some prime in P (and,
  empirically, EVERY term from n=1, not just eventually).
- Conjecture: 2 always ends up in P once a1 has ≥2 "close" odd prime factors,
  but not when a1's odd prime factors are spread apart enough that the smallest
  one alone suffices to dominate the greedy process forever (a1=231=3·7·11 stayed
  trivial with L=3).
- Conjecture (weaker, more confident): for every a1, the terms of the sequence,
  from n=1, are divisible by at least one prime factor of a1 (this one is
  actually PROVABLE immediately from i=1 in the recursion's defining condition,
  not just conjectured — flag this as a free early lemma for the outliner).
- Numeric summary table:
  | a1 | prime factors | recruited P | L | T | periodic from n=1? |
  |---|---|---|---|---|---|
  | even a1 | incl. 2 | {2} | 2 | 1 | yes |
  | 3,9,33,231 | odd, "spread" | {3} | 3 | 1 | yes |
  | 5,25,55 | | {5} | 5 | 1 | yes |
  | 15,45 | {3,5} | {2,3,5} | 30 | 8 | yes |
  | 105,11025 | {3,5,7} | {2,3,5,7} | 210 | 58 | yes |
  | 1155 | {3,5,7,11} | {2,3,5,7,11} | 2310 | 676 | yes |
  | 385 | {5,7,11} | {2,5,7,11} (radical confirmed; T unconfirmed, >3000) | 770(radical confirmed) | unknown (>3000) | untested (transient too long to search) |
  | 315 | {3,5,7} (=105's radical) | plausibly {2,3,5,7} | plausibly 210 | untested | untested |
