## imo-2026-06 (mechanics lens)

- **Distinct openings** (mechanics-flavored, not full proofs):
  1. **"Sentinel prime cover" opening.** Empirically, for every start `a_1` the whole
     sequence is covered by a small finite set `S` of primes in the sense that
     *every* term `a_n` (from `n=1` on) is divisible by at least one prime of `S`
     (verified for `a_1=1001=7·11·13`: `{2,7}`, `{2,11}`, `{2,13}` and even
     `{7,11,13}` alone all work as covers over the first 2000 terms — the cover is
     not unique/minimal, several finite sets work). If one can prove such a cover
     exists and is *eventually necessary and sufficient* (i.e. that from some point
     on, "divisible by some prime in `S`" is exactly the admissibility condition,
     because every earlier term already shares a prime of `S`), the tail of the
     sequence reduces to a purely arithmetic/greedy problem on residues mod
     `M = lcm(S)` (or `∏S`), which is finite-state and hence eventually periodic
     by pigeonhole on residue-state. This looks like the load-bearing mechanism.
  2. **"Finite state via residues mod growing modulus" opening.** Track, at each
     step, the vector of residues of `a_n` modulo the primes used so far. Because
     new large primes only get introduced finitely often (see cheap-kill below),
     eventually no new prime is ever needed again, and the "state" (residue mod a
     *fixed* modulus `M`, together with which of finitely many earlier terms still
     impose a live constraint) becomes finite. Two states with the same finite
     data force a shift-copy of the process → periodicity of the difference
     sequence. This is the mechanism the outliner should try to make rigorous
     (pigeonhole over a finite state space of "current gap-pattern mod M").
  3. **"Only finitely many primes ever get introduced" opening.** A candidate
     finite-ness lemma: once the terms so far collectively "cover" a growing
     interval well enough (every sufficiently large integer near `a_n` is already
     forced to share a factor with some early term through overlapping prime
     memberships), no new prime is ever recruited past some point `N_0`; from then
     on `a_{n+1}` is chosen using only primes already in play. This is the crux
     fact that needs its own proof (a counting/density argument: numbers avoiding
     all currently-used primes get rarer, while the "gap to next candidate" stays
     bounded because Bertrand/CRT-type density arguments guarantee a hit inside a
     bounded window using only the current prime set).

- **Candidate technique(s):** Chinese Remainder Theorem / residues mod a finite
  modulus (kb: "Modular arithmetic, CRT" entry), pigeonhole on a finite state
  space (kb: pigeonhole entry), Bertrand's postulate style density/interval
  arguments to bound gaps once the prime set is fixed, and an inclusion–exclusion
  / density count (sieve-style) to show that "numbers coprime to all primes in a
  finite set `S`" have positive density, hence the greedy process, forced to only
  ever use primes actually present among early terms, cannot skip forever without
  eventually revisiting the same finite state.

- **Cheap-kill candidates:**
  - **Gap boundedness for a fixed working prime set.** Once the admissibility test
    is "share a factor with each of finitely many fixed numbers `a_1,...,a_k`"
    (each with finitely many prime factors), by CRT there exist arbitrarily dense
    witnesses — in fact an explicit residue mod `∏(primes of a_1,...,a_k)` that is
    divisible by (say) the smallest prime factor of each `a_i` simultaneously is
    forced, giving an a priori bound on `a_{n+1}-a_n` in terms only of the primes
    used so far. This is a cheap way to rule out the gaps blowing up before a new
    prime is even needed.
  - **Parity/small-prime dominance check:** numerically 2 (or another small prime
    already present in `a_1`) tends to become universal quickly whenever `a_1` is
    even or a multiple of a small prime; that case (2 | a_1) collapses trivially to
    an eventually-constant-difference (often period 1) sequence — worth flagging
    as the "easy sub-case" so the outliner can dispose of it fast and focus effort
    on the genuinely multi-prime starts (products of two or more mid-size primes,
    none of which is 2).

- **Knowledge-base entries to use:** "Modular arithmetic, CRT" (combining residues
  across a fixed finite prime set — likely the backbone of the periodicity
  argument), "Bertrand's postulate" (guaranteeing a prime/witness in a bounded
  range — candidate for bounding how far ahead the next admissible number can be),
  "Divisor analysis" entry (gcd structure, bounding a finite search by size — used
  for bounding the gap search). Dirichlet's theorem (primes in AP) is a plausible
  but so-far-unconfirmed candidate for proving new primes get introduced only
  finitely often. Zsigmondy is NOT obviously relevant here (no `aⁿ−bⁿ` structure).

- **Analogous past problems (cruxes):** No crux in the corpus is a close structural
  match to this specific "greedy pairwise-gcd sequence" problem. The closest hits
  from `number_theory` / `sequences-and-recurrences` and `divisibility-and-gcd`
  subtopics:
  - `aimo-0224` (NT, divisibility/coding): "assign a distinct prime to each element
    of a ground set, define terms as products of primes over subsets, so gcd
    coprimality of two terms becomes disjointness" — same *flavor* (primes-as-tags
    encoding a coprimality/gcd pattern) but it's a construction problem, not a
    forced-structure proof; only a loose analogy for how to think about "which
    primes are tied to which terms."
  - `aimo-0611` (NT, zsigmondy-and-primitive-divisors): "prove a term grows larger
    than the product of all earlier terms, so some prime must appear in it to a
    strict power" — relevant only as a *technique pattern* (bounding when new
    primes must appear because growth outpaces existing prime budget), useful if
    the outliner wants to bound how many distinct primes can ever appear.
  - `aimo-0982` (NT, modular-arithmetic-and-CRT / orders-and-primitive-roots): "to
    prove a digit subsequence sampled at moving indices is eventually periodic,
    track the sampling index modulo the period of the source's eventually-periodic
    behavior" — same *shape* of conclusion (derive eventual periodicity from a
    finite modular state), worth reading for the periodicity-transfer technique,
    though the source problem (digit sequences, powers of 2 mod m) is otherwise
    unrelated.
  None of these is a strong match; I would not force any of them as a template —
  they offer technique fragments (prime-tagging, growth-forces-new-prime,
  modular-state periodicity), not a solution shape to adapt wholesale.

- **Prior progress:** none — `results/imo-2026-06/` has empty `approaches/` and
  `lemmas/` dirs and no `current.md` yet; this is the first round of exploration.

- **Dead ends (do not retry):** none recorded yet (no prior approaches exist to
  check).

- **Small-case / intuition notes (all conjectural, from numeric experiments,
  `python3` greedy simulation up to a few thousand terms):**
  - If `a_1` is itself a prime `p` or has 2 as a factor (e.g. `a_1 ∈
    {2,3,4,5,6,7,10,12,30,...}`), the sequence *immediately* becomes a pure
    arithmetic progression `a_n = a_1 + (n-1)·d` with `T=1` from the very first
    term (`d` = smallest prime factor of `a_1`, e.g. `a_1=2→d=2`, `a_1=3→d=3`,
    `a_1=15→` NOT this trivial case, see below).
  - Composite starts with **two or more odd prime factors and no factor of 2**
    show genuinely nontrivial pre-periodic behavior before locking into a longer
    period: e.g. `a_1=15=3·5` → diffs eventually cycle with `T=8`, `L=30
    (=2·3·5)`; `a_1=45=3²·5` → same `T=8, L=30`; `a_1=105=3·5·7` → `T=58, L=210
    (=2·3·5·7)`; `a_1=77=7·11` → `T=18, L=154 (=2·7·11)`; `a_1=91=7·13` → `T=20,
    L=182 (=2·7·13)`; `a_1=1001=7·11·13` → `T=282, L=2002 (=2·7·11·13)`.
    **Conjectural pattern:** `L` always equals `2` times the product of the *odd*
    primes dividing `a_1` (i.e. the primorial-like product `2·rad_odd(a_1)`),
    with prime `2` always eventually recruited even when `2 ∤ a_1` at the start.
  - Counter-nuance found for `a_1=143=11·13`: the period eventually collapses to
    `T=1, L=22=2·11` — the prime `13`, though present in `a_1`, becomes
    *unnecessary* in the long run because every later term ends up divisible by 2
    or 11 anyway (checked explicitly on the first 40 terms: every single term is
    divisible by 2 or 11, even the ones that also happen to carry a 13). So the
    "final sentinel prime set" is **not simply "primes dividing a_1"** — it can be
    a strict subset (13 drops out) or can strictly need the newly-recruited 2. In
    general the eventual `L` is not always `2·rad_odd(a_1)` — it depends on which
    primes actually remain load-bearing, a fact that needs an honest proof rather
    than pattern-matching from a1's factorization.
  - Gaps `a_{n+1}-a_n` stayed bounded (never observed to grow past a couple
    hundred) in all tested cases up to `a_1 ≈ 1000`, consistent with the
    conjectured eventual periodicity, but this is only checked numerically, not
    proved.
  - The **cover set is not unique**: for `a_1=1001` both `{2,7}` and `{7,11,13}`
    (i.e. sets not containing 2!) work as covers of the whole sequence — so "2
    becomes universal" is not a forced law, just a common outcome; a fully
    general proof must handle sequences where 2 never becomes a sentinel.
