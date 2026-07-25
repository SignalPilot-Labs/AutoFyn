## imo-2026-01 (lens: primewise decoupling)

### Setup confirmed
For each prime p, v_p(gcd(m,n)) = min(v_p(m),v_p(n)) and v_p(lcm(m,n)/gcd(m,n)) =
max(v_p(m),v_p(n)) - min(v_p(m),v_p(n)). So a single board move on positions i,j
acts, **simultaneously and independently for every prime p**, on the pair of
p-exponents (a,b) := (v_p(entry_i), v_p(entry_j)) via
T(a,b) = (min(a,b), max(a,b)-min(a,b)). The coupling across primes is only
*which two board positions get chosen* at each step — the transformation itself,
for a fixed prime, depends only on that prime's own current exponents at those two
positions. This decoupling is exact, not approximate — verified below it causes no
problem for termination or for the final value, for a subtle reason explained
under "pitfalls."

### The per-prime game and its invariant
Fix p and look at the multiset of 2026 exponents (nonneg integers, most typically 0).
T(a,b) = (min,max-min) is exactly the subtractive/Euclidean step: gcd(min(a,b),
max(a,b)-min(a,b)) = gcd(a,b). Hence **g_p := gcd of the entire multiset of
2026 exponents (with the usual convention gcd(0,x)=x) is invariant under every
move**, for every prime p — this is a per-prime conserved quantity, the direct
analogue of "gcd is preserved by the subtractive Euclidean algorithm."

Sum behaves as a monovariant: new sum = min + (max-min) = max(a,b) ≤ a+b, strict
inequality iff min(a,b) > 0. So Σ(exponents) for a fixed prime is non-increasing,
strictly decreasing exactly when *both* a,b > 0 (i.e. when p divides both m and n
in the original board move).

### What this buys for the two parts

**Conjectured value of M (verified numerically, see below):**
M = ∏_p p^{g_p}, where g_p = gcd(v_p(a_1),...,v_p(a_2026)) computed from the
*initial* board. This is emphatically NOT gcd(a_1,...,a_2026) (which would use
min of exponents) nor lcm — it's a genuinely different multiplicative invariant
(gcd of the exponent sequence, prime by prime). Confirmed by direct simulation
(randomized move order, 100 trials each) on 8 test boards — every trial converges
to exactly one active number, always equal to the predicted ∏ p^{g_p}. E.g.
[4,6,10] → 30, [8,12,18] → 6, [9,27,81,3] → 3, [100,150,75,50,25] → 150. This is
strong (conjectural, not yet proved) confirmation the per-prime gcd is the right
invariant and the right closed form for the answer.

**Part (b) (uniqueness of M) becomes nearly free once decoupling + invariant are
established**, and resolves the one apparent worry about decoupling for free:
At a *terminal* board state (no move possible), by definition at most one
position has value > 1; call it position i* with value M (if it exists). Every
other position has value 1, i.e. exponent 0 for *every* prime simultaneously —
there is only one physical slot i* where any prime's mass can be nonzero, because
the terminal condition is about the whole number at each slot, not about a single
prime. So for every prime p, the terminal exponent-multiset is (2025 zeros, one
value e_p at slot i*), whose gcd is simply e_p. Since g_p is invariant throughout
the whole process, e_p = g_p is forced for every p, regardless of which slot i*
ends up being the survivor and regardless of the move sequence. Hence M =
∏ p^{g_p} is pinned down completely independent of Confucius's choices — this
is the cleanest route to (b) and sidesteps needing any argument that "different
primes concentrate at the same slot by coincidence": they don't coincide by luck,
they're forced to because the terminal state has literally only one slot > 1 for
the whole board, and every prime's leftover exponent must live in that slot or be
0 elsewhere.

**Part (a) needs two more ingredients, both clean under this framing:**
1. *Termination (finitely many moves).* Let Φ = Ω(∏ board entries) = Σ_i Ω(a_i)
   (Ω = number of prime factors with multiplicity). A move's effect on Φ is
   Σ_p max(a,b) vs Σ_p (a+b) for the chosen pair's exponents — Φ is non-increasing,
   strictly decreasing exactly when gcd(m,n) > 1 (equivalently when some prime
   divides both chosen numbers). When gcd(m,n)=1, Φ stays constant, but the
   number of active (>1) board entries strictly decreases by exactly 1 (m,n
   become 1, mn — one of these, "1", becomes permanently inert since inert
   entries can never be chosen again and can't become active again either,
   since 1's factors don't change under further moves elsewhere). The pair
   (Φ, #active) decreases lexicographically on every move, both coordinates
   bounded below (Φ≥0, #active≥0), so the process terminates — a standard
   monovariant/well-founded-descent argument (KB: "Invariants & monovariants").
2. *Never reaches 0 active entries.* Since every initial a_i > 1, some prime p₀
   divides some a_i, so g_{p₀} ≥ 1 (gcd of a multiset that has at least one
   positive entry, using gcd(0,x)=x convention, is ≥ 1). Since g_{p₀} is
   invariant, the exponent-multiset for p₀ can never become identically 0 (its
   gcd would then be 0 ≠ g_{p₀} ≥ 1), so the board can never reach the all-1s
   state. Combined with termination forcing ≤1 active entry, and this ruling
   out 0 active entries, exactly 1 active entry remains — that's (a).

### Pitfalls / what still needs rigor (not yet proved, just identified)
- The invariance of g_p (gcd of exponent multiset under T) needs a clean written
  proof: standard fact gcd(a,b) = gcd(min(a,b), max(a,b)-min(a,b)), but must be
  argued carefully that changing only *two* entries of a larger multiset preserves
  the *overall* multiset gcd (via gcd(whole multiset) = gcd(gcd of the two changed
  entries, gcd of the rest) — routine but must be stated, not hand-waved).
- The "inert entries stay inert forever" fact used in the termination monovariant
  (a board entry that becomes 1 never becomes >1 again) is true because moves only
  ever touch two entries >1 and the process only replaces the two chosen entries —
  an untouched 1 stays 1 forever; this is trivial from the rules but should be
  stated as a one-line remark, not asserted implicitly.
- Do not need the primes to be finite in any bounded sense — since only finitely
  many primes divide the (finite) initial product, all this is over a finite prime
  set; no issue.
- A subtlety to flag for the outliner: the definition of Φ = Ω(product) is
  equivalent to Σ_p Σ_i v_p(a_i); this can be phrased either "per prime" (matching
  this decoupled framing) or as one global quantity — both proofs are the same
  content, but the write-up should pick one voice and be consistent (prime-by-prime
  bookkeeping is more explicit/rigorous for the reviewer, more verbose).

### Candidate technique(s)
Prime factorization / p-adic valuation decomposition (KB: p-adic valuation
reasoning, "Invariants & monovariants" entry, "Divisor analysis" entry) combined
with the classical subtractive Euclidean algorithm gcd-invariance fact.

### Cheap-kill candidates
None needed — the per-prime gcd invariant essentially *is* the whole problem;
no extra pruning required. (One easy sanity/parity-style check used above: since
every a_i>1, at least one prime has positive invariant g_p, which is what rules
out the "board collapses entirely to 1s" failure mode — worth flagging to the
outliner as the one non-obvious part of (a).)

### Knowledge-base entries to use
- "Invariants & monovariants" (KB line ~117, ~191) — directly the technique for
  both the termination monovariant (Φ, #active) and the conserved quantity g_p.
- "Divisor analysis" (KB line ~86) — gcd structure background.
- p-adic valuation entries (LTE section, line ~67) — not LTE itself, but the
  general v_p toolkit this problem is built on (framing valuations as the atomic
  unit of the process).

### Analogous past problems (cruxes)
Searched crux corpus (`domain=number_theory`, subtopics `invariants-and-monovariants`,
`p-adic-valuation`, `divisibility-and-gcd`; also `domain=combinatorics`,
subtopic `invariants-and-monovariants`/`processes-and-algorithms`) and free-text
searched for "lcm"+"gcd" co-occurrence and "blackboard". No crux move in the
corpus targets a gcd/lcm-swap board process; the closest thematically is
`aimo-0662` (lcm/gcd chains on primes 2,3, subtopic extremal-principle /
induction-and-construction) but it is about constructing an extremal periodic
tower, not a convergence/invariant argument — not genuinely analogous, don't
force it. Several `invariants-and-monovariants` cruxes (`aimo-0230`,
`aimo-0294`, `aimo-0295`, `aimo-0193`) use the general pattern "count something
that only decreases + separately something that can't hit 0" which is
structurally the same *shape* of argument as what's needed here (termination +
non-collapse), but none are about gcd/lcm specifically — useful as a pattern
reference, not a source to cite content from. Overall: no strong analog exists;
this problem's specific mechanism (Euclidean-subtractive-step per exponent) is
not duplicated in the sampled corpus.

### Prior progress
None — round 1, no existing approaches/lemmas in results/imo-2026-01/.

### Dead ends (do not retry)
None recorded yet (first round).

### Small-case / intuition notes (conjectural, verified only numerically)
- Simulated the full process in Python (randomized move order, 100 trials per
  board) on 8 boards of size 3–5; every trial always ends with exactly one active
  entry, and it always equals ∏_p p^{gcd_i v_p(a_i)} — strong evidence for both
  parts (a) and (b) and for the closed-form answer, but this is simulation
  evidence only, not a proof.
- The final M is *not* gcd(a_1,...,a_n) (e.g. [4,6,10]: gcd=2 but M=30) — worth
  flagging so the outliner doesn't misstate the answer as the naive gcd.
- 2026 (the specific count of numbers) plays no role in the mechanism found here
  — the invariant/monovariant argument works for any n ≥ 2 numbers. This suggests
  2026 is a red herring / just flavor, not load-bearing; worth the outliner
  double-checking nothing in the problem secretly needs n=2026 (e.g. no lower
  bound like "n must be at least 2" — trivially true, n=2026≥2).
