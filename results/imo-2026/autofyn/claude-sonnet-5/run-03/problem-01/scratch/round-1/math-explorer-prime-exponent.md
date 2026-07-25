## imo-2026-01 (lens: prime-exponent / linear-algebra-over-integers)

### The exact per-prime action of a move
Fix a prime p. If x = v_p(m), y = v_p(n) are the p-adic valuations of the two chosen
numbers, then v_p(gcd(m,n)) = min(x,y) and v_p(lcm(m,n)/gcd(m,n)) = max(x,y) - min(x,y) = |x-y|.
So **a move sends the exponent pair (x,y) -> (min(x,y), |x-y|)** for every prime p
simultaneously (using each prime's own current values at the two chosen board
positions, but the same pair of positions for all primes at once — this is the
"coupling" the lens asked me to watch for: you cannot pick different position-pairs
for different primes in one move).

This is literally **one step of the subtractive Euclidean algorithm** applied to the
pair (x,y), for every prime in parallel, always keyed on the same two board slots.

### Monovariant for part (a) — verified correct, ready to use
For a single prime and pair (x,y) with a = min(x,y), b = max(x,y):
old sum of squares x^2+y^2 = a^2+b^2; new sum of squares = a^2 + (b-a)^2 = 2a^2+b^2-2ab.
Difference (old − new) = a(2b−a) ≥ 0, since b ≥ a ≥ 0 (so 2b−a ≥ b ≥ a ≥ 0), **with
equality iff a = 0**, i.e. iff min(x,y) = 0 for that prime, i.e. iff that prime does
not divide gcd(m,n).

Hence, summing over **all primes and all 2026 board positions**, define
`S = Σ_positions Σ_primes v_p(entry)^2`. S is non-increasing under every move, and
strictly decreases iff gcd(m,n) > 1 (some shared prime). If gcd(m,n) = 1, S is
unchanged, but the two numbers m,n become 1 and mn — the **count C of entries > 1
strictly decreases by 1** in that case (and also strictly decreases whenever m = n,
since then gcd=lcm/gcd... actually when m=n, gcd=m, lcm/gcd=1, again C drops).

So the lexicographic pair (S, C) — both non-negative integers — **strictly decreases
every single move** (either S drops when gcd(m,n)>1, or S is flat and C drops by
exactly 1 when gcd(m,n)=1). Bounded below by (0,0)/(0,1), so the process terminates
in finitely many moves. This is a clean, fully rigorous route to part (a); I did not
find any gap in it. It uses only the KB's generic "Invariants & monovariants" entry
(knowledge_base.md line 117, 191) — no exotic machinery needed.

*(Note: at the very end C=1 is the stopping state per the problem statement, not
C=0 — the lex-decreasing argument still applies since C=1 is a valid floor and the
process must stop once no two entries >1 remain, i.e. once C≤1; termination is what's
needed, not C reaching 0.)*

### Conjectured / numerically-confirmed closed form for M (part b)
Per prime p, the pairwise operation (x,y) -> (min(x,y), |x-y|) preserves the
**ordinary integer gcd of the pair**: gcd(min(x,y), |x-y|) = gcd(x,y) (standard
Euclidean-algorithm fact). Since overall gcd of a multiset is associative/decomposable
(gcd(a, x, y, b, ...) = gcd(a, gcd(x,y), b, ...)), **the integer gcd of the full
multiset of 2026 exponents {v_p(a_1),...,v_p(a_2026)} is invariant under every move**,
for every prime p independently (convention: gcd(0,...,0)=0, gcd(0,k)=k).

At termination, exactly one board entry M is > 1 and the rest are 1, so for each
prime p the terminal exponent multiset is {0,0,...,0, v_p(M)} whose gcd is v_p(M)
itself. Since that gcd equals the invariant initial gcd:

  **v_p(M) = gcd( v_p(a_1), v_p(a_2), ..., v_p(a_2026) )**  (ordinary integer gcd of
  the exponents, treating absent primes as exponent 0), i.e.

  **M = ∏_p p^{ gcd_i( v_p(a_i) ) }**

This is a genuinely different quantity from gcd(a_1,...,a_2026) — that would use
min_i v_p(a_i), not gcd_i v_p(a_i). Example that separates them: board {2,3}: gcd of
numbers = 1, but v_2-exponents are {1,0} with integer-gcd 1, v_3-exponents {0,1} with
integer-gcd 1, giving M = 2·3 = 6 — and indeed {2,3} -> {1,6} in one move, matching
the simulation exactly.

**I numerically verified this formula against brute-force random simulation** (python,
`gcd`/`lcm` step function, uniformly random legal move each step until ≤1 entry >1),
across boards of size 2 up to 27, random entries, and many random play orders per
board (10-20 trials each): **in every single trial the simulated terminal M matched
the predicted closed form exactly**, and the number of moves to termination stayed
small (≤ ~2×(board size)ish), consistent with the (S,C) monovariant bound. This is
strong (but still empirical/conjectural, not yet a proof) evidence that
`M = ∏_p p^{gcd(v_p(a_1),...,v_p(a_2026))}` is the correct and order-independent
answer.

Because this quantity is manifestly independent of Confucius's choices from the
start (it's a function only of the original board), proving "the invariant gcd_i
v_p(a_i) per prime is preserved by every move, and the terminal state's single
survivor's exponent equals that invariant" is exactly what's needed for part (b) —
this can likely be built into the SAME framework as the part (a) monovariant proof
(one clean per-prime Euclidean-algorithm argument handles both parts together,
possibly even more efficiently than treating them as separate lemmas).

### What's still unclear / the remaining gap
- The invariance of gcd_i(v_p(a_i)) is easy (one line: gcd(min(x,y),|x-y|)=gcd(x,y)
  plus associativity of gcd over a multiset). The real content still to nail down is
  the **coupling across primes**: part (a) guarantees a single board slot ends up >1,
  but part (b)'s formula requires that for EVERY prime p, the surviving nonzero
  exponent sits in that SAME slot M (not that each prime independently reduces to a
  single nonzero slot, possibly different slots per prime). This is automatically
  true once you know only one board entry overall is >1 at the end (proved by part
  a), since if some prime p's exponent were 0 at that slot, M's value would not
  include p — but the invariant gcd_i v_p(a_i) could still be nonzero even if the
  final single number doesn't carry prime p... Need to double check: does the
  argument show ALL of a given prime's "mass" migrates to the surviving slot, or only
  that gcd is preserved? Actually the closed form derivation above is airtight given
  ONLY that (1) gcd of exponent-multiset is a per-move invariant, and (2) at
  termination the exponent-multiset for prime p is all-zero except possibly one
  position (M's), because M is the only entry >1 — if p does not divide M, then
  ALL positions have exponent 0 for p at termination, so gcd_i v_p(a_i) = gcd(0,...,0)
  = 0, forcing p never divided any board entry an gcd for that prime to begin with...
  wait that's only valid IF the invariant truly is preserved through non-move-related
  reasoning. This step needs to be double-checked carefully by the outliner/builder:
  the gcd-invariance argument as I stated needs verifying that it truly is preserved
  when the pair (x,y) touched is a SUBSET of the full multiset and other elements are
  untouched — yes, gcd(a,b,c,...) = gcd(gcd(a,b), c, ...) is standard, so replacing
  (a,b) by (gcd(a,b)-preserving pair) leaves the total gcd unchanged; this is correct
  and needs no further caveat. I flag it only because it is the crux step and must be
  stated + proved explicitly and rigorously by the outliner (small, clean lemma).
- Termination bound (part a) I'm confident is airtight; still needs writing up with
  full case coverage (gcd(m,n)>1 case and gcd(m,n)=1 case, plus the m=n subcase which
  is really the gcd(m,n)=m=n>1 case where S strictly drops since a=min=m>0).

### Knowledge-base entries to use
- `knowledge_base.md` line 117, 191: **Invariants & monovariants** — generic pointer,
  matches directly (sum-of-squares-of-exponents monovariant + gcd-of-exponents
  invariant).
- No p-adic valuation / lifting-the-exponent / CRT entries in the KB are a close fit
  beyond the basic "valuation" framing itself (this problem is really an invariant/
  monovariant problem dressed in number-theoretic language, not a valuation-lifting
  problem).

### Crux corpus search (number_theory: invariants-and-monovariants, p-adic-valuation,
divisibility-and-gcd, processes-and-algorithms)
- Searched all four subtopics for gcd/lcm-swap, sorting-network, Euclidean-subtraction,
  or "min/diff pairwise reduction" themes. **No close analogue found.** The closest
  hits were about gcd(2^M+1,2^N+1)=2^gcd(M,N)+1 (aimo-0632, exponent-gcd identity
  flavor, same *spirit* of "gcd distributes over an operation" but not a swap-process
  problem) and aimo-0324 ("Assign each board position the squarefree part... use as
  monovariant for a game" — a genuinely different game, not a gcd/lcm swap network).
  Nothing in the corpus directly matches Confucius's specific gcd/lcm replacement
  rule; this problem's core trick (view each prime's exponent-pair update as a
  subtractive-Euclidean step, invariant = gcd of the whole exponent multiset) appears
  to be a from-scratch construction rather than an adaptable crux. Report this
  honestly to the outliner: **no strong crux match — build the argument directly.**

### Prior progress
None — this is round 1, no approaches exist yet in `results/imo-2026-01/`.

### Dead ends
None yet recorded (nothing tried before this round).

### Small-case / intuition notes (labeled conjecture, backed by simulation)
- Conjecture (strongly evidenced numerically, not yet proved): for the original
  2026-number board, `M = ∏_p p^{gcd(v_p(a_1),...,v_p(a_2026))}`, independent of
  play order. Verified by brute-force random simulation on ~17 random boards
  (sizes 2–27, random values up to 50, 10–20 random-order trials each): 100% match
  between predicted and simulated M in every trial.
- Move count to termination stayed small in simulation (order of board size), which
  is consistent with — but doesn't replace — the rigorous (S,C) lexicographic
  monovariant bound derived above.
- Special case sanity checks: all-equal board (e.g. {2,2,2,3}) still matches formula;
  boards containing 1 pairwise-coprime numbers work; boards with a common factor
  shared by all numbers work (e.g. {100,75,60,5}, gcd=5 divides all, M=60 which is
  NOT simply the gcd — formula correctly captures the more refined per-prime gcd-of-
  exponents structure rather than just "gcd of all numbers").
