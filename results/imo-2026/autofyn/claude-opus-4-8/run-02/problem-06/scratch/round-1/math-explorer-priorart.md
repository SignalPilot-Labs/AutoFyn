## imo-2026-06

### Prior-art scouting: transferable techniques (ranked)

**1. [Strongest match] aimo-0678 (ISL/IMO "gcd/lcm coupled sequences eventually periodic") — state-space collapse via a bounded auxiliary quantity + reduction mod a fixed modulus.**
- Problem: a_{n+1}=gcd(a_n,b_n)+1, b_{n+1}=lcm(a_n,b_n)-1; prove (a_n) eventually periodic.
- Crux chain (three moves, all in `past_crux_moves_database.json`):
  1. *Freeze an invariant on a "calm" regime*: while a_n | b_n, the sum s_n=a_n+b_n is exactly conserved and a_n just increments — gives a fixed target to compare against.
  2. *Min-of-a-set monovariant*: W_n = {m ≥ a_n : m ∤ s_n}, w_n = min W_n, proved non-increasing ⟹ eventually constant ⟹ (a_n) is bounded, hence takes finitely many values.
  3. *Mod-M state compression*: once a_n is bounded, let M = lcm of all values a_n ever takes; track b_n mod M instead of b_n itself. The pair (a_n, b_n mod M) lives in a **finite** set and the recurrence shows (a_{n+1}, b_{n+1} mod M) is a **function** of (a_n, b_n mod M) alone. Finitely many states + deterministic transition ⟹ eventually periodic by pigeonhole (two equal states force everything between to repeat).
- **How this maps onto P6**: the target claim (∃ T, L with a_{n+T} = a_n + L, i.e. periodic *differences*, not periodic values — a_n itself is strictly increasing and unbounded) is exactly the "eventually periodic increments" flavor of aimo-0678's conclusion. The natural adaptation: find a bounded/eventually-constant auxiliary object (candidate: the *set of primes actually needed to cover a_1,...,a_n at the current step*, or the residue pattern of a_n modulo the lcm of the "active" primes) and show the transition (current state) → (next gap, next state) is a function of a finite state, forcing eventual periodicity of the gap sequence a_{n+1}-a_n. This is the strongest structural analogy in the corpus for this problem.

**2. aimo-0503 (gcd(a_i,a_{i+1}) > a_{i-1} ⟹ a_n ≥ 2^n) — gcd-divides-difference gap bound.**
- Crux: gcd(a_i,a_{i+1}) | (a_{i+1}-a_i) since gcd divides both terms, hence divides their difference; combined with strict increase this lower-bounds the gap by the gcd.
- **Adaptation**: in P6, gcd(a_n, a_{n+1}) | (a_{n+1}-a_n) too (standard fact), giving a lower bound on the gap a_{n+1}-a_n in terms of whichever prime factor is shared. Useful as a cheap structural fact when bounding gap sizes, but this problem's real difficulty is the *upper* bound on gaps / minimality of a_{n+1}, which this crux doesn't attack directly — supporting fact only, not the crux move itself.

**3. aimo-0447 ("gcd(a+i,b+j)>1 for all i,j in an (n+1)×(n+1) grid ⟹ min{a,b} > (cn)^{n/2}") — prime-covering-a-grid counting argument.**
- Crux: place in cell (i,j) a prime p | gcd(a+i,b+j); a single prime p can occupy only ⌈N/p⌉² cells (since p divides ≤⌈N/p⌉ terms of an N-term interval); summing 1/p² over small primes shows small primes cover < half the grid, forcing > N²/2 cells to hold "large" primes (> εn²); then in some row/column ≥ N/2 of these large primes must be **distinct** (two equal large primes p would need p | difference of two terms < p, impossible), giving a lower bound on a+i (or b+j) as a product of ≥ N/2 distinct large primes.
- **Adaptation**: P6's defining condition is structurally the *transpose* of this grid condition — for a_{n+1} to work, it must share a prime with EACH of a_1,...,a_n (a 1×n "row" of the same grid, with the roles of "the n previous terms" playing the column index). The interval-counting technique ("a prime p can hit at most ⌈(window length)/p⌉ terms of an arithmetic-progression-like set") is the natural tool for proving that only *finitely many primes* are ever needed to cover all gaps once the sequence stabilizes (i.e., primes larger than the eventual period L can be shown to be irrelevant / never freshly required past some point). This is a strong candidate for the "why do only finitely many primes matter eventually" step.

**4. aimo-0224 ("does there exist a_n with gcd(a_m,a_n)=1 iff |m-n|=1?") — prime-tagging / disjoint-index-set encoding.**
- Crux: assign each element of S a distinct prime, define a_n as a product of primes over a chosen finite index set I_n, so gcd-coprimality becomes disjointness of index sets; then design I_n (arithmetic progressions with common difference 2, parity-split) to realize the target adjacency pattern.
- **Adaptation**: this is a *construction* technique (build a sequence with prescribed coprimality pattern), the reverse direction from P6 (P6's sequence is *given* by the greedy rule, not freely constructed). Useful mainly as intuition for how "each integer is tagged by which primes it needs to share with which prior terms" can be organized combinatorially — but it is not directly transferable as a proof technique here since P6 constrains us to the specific greedy a_{n+1}, we don't get to choose the covering pattern.

**5. aimo-0421 (infinite set S, pigeonhole on gcd values / prime fibers) — finite-vs-infinite prime-fiber dichotomy.**
- Crux: for a fixed a, {gcd(a,s): s ∈ S} is a finite set of divisors of a, so pigeonhole over an infinite S gives infinitely many s with the same gcd; alternately, split primes into those with infinite fiber (divide infinitely many elements of S) vs finite fiber.
- **Adaptation**: transferable *lemma pattern*, not crux move: in P6, for a fixed a_i, gcd(a_i, a_n) as n→∞ ranges over divisors of a_i (finitely many options) — this "finite value set" fact could support an argument that eventually the prime dependencies stabilize. Weak/generic transfer, listed for completeness.

**6. aimo-0982 (digit subsequence sampled at 2^n-indices of a rational is rational) — track an index modulo the period of an already-known eventually-periodic object.**
- Crux: to show a re-indexed sampling of an eventually-periodic sequence is again eventually periodic/rational, track the sampling index modulo the source's period.
- **Adaptation**: minor structural reminder that "compose an index map with an eventually-periodic base sequence" preserves eventual periodicity — could matter if the outline ends up expressing a_n via a periodic covering system sampled at shifted indices, but not a primary technique here.

### Knowledge-base entries to flag
- "Order of an element, Fermat/Euler: periodicity of a^n mod m; eventual periodicity of products of a sequence mod m" — directly the KB's compressed version of technique #1 above.
- "Linear recurrences ... sequences are eventually periodic mod m" — same family.
- "Bertrand's postulate" and "Dirichlet's theorem (primes in AP)" — candidates if the outline needs an explicit prime in a controlled range to seed a covering-system construction for the periodic tail.
- "Pigeonhole / extremal principle" — the generic finite-state pigeonhole that closes technique #1's periodicity conclusion.

### Small-case / numerical evidence (conjectural, computed via python `gcd` brute force this round)
- For **prime** a_1 (or more generally whenever a_1's only relevant prime factor p forces the greedy step trivially), the sequence looks deceptively like a pure AP a_n = a_1+(n-1)p for a long initial run — but this is NOT the general behavior; it can be an artifact of small search range.
- For a_1 = 15 (= 3·5), the difference sequence a_{n+1}-a_n is **immediately periodic** with period T=9 and differences (3,2,4,6,6,4,2,3,3) summing to L=30 (checked out to n=2000): i.e. a_{n+9} = a_n + 30 for all n in the tested range. This is concrete numerical support for the theorem's shape and shows the "trivial single-prime AP" is not the generic phenomenon — multiple primes (here 2,3, and eventually more?) interleave. Worth re-checking with sympy factorization of the periodic block's terms to see which primes recur in the stable regime — useful for the outliner to guess the structure of the eventual period (likely: finitely many "small" primes end up doing all the covering work, and L is a multiple of their product or lcm).
- Recommend the outliner/builder re-run and inspect several other composite seeds (e.g. 6, 10, 12, 21) at large n (~1000-5000 terms) to conjecture the general shape of (T, L) before committing to a specific construction in the periodicity argument.

### Dead ends / cautions
- None recorded yet in `results/imo-2026-06/` — `approaches/` and `current.md` are both empty; this is the first round of work on this problem. No prior "failed approach" to avoid.
- Caution for the outliner: do not assume the trivial "single smallest-prime-factor locks the whole sequence into one AP forever" pattern — numerically false in general (see a_1=15 above). Any approach built on "a_n mod p is eventually constant for the single smallest prime p of a_1" will likely break on multi-prime cases like this.

### Cheap-kill / structural facts worth stating up front
- gcd(a_n, a_{n+1}) always divides a_{n+1}-a_n (gcd divides both). Combined with a_{n+1}>a_n, this lower-bounds every gap by a proper divisor structure — cheap but not decisive alone.
- Once n ≥ 2, a_{n+1} must share a (possibly different) prime with **each** a_i, i ≤ n — this is a covering condition over n constraints simultaneously, not a single shared prime; the grid-counting idea (crux #3) is the natural tool to show only boundedly many *distinct* primes can be doing "fresh" work past some point, since primes larger than the eventual gap bound can divide at most one term in any long window.
