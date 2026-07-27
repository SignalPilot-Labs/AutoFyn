## imo-2026-01 (lens: direct integer monovariant / invariant)

The move, rewritten: pick (m,n), let g=gcd(m,n), write m=gx, n=gy with gcd(x,y)=1.
Then the two replacements are `g` and `xy = (m/g)(n/g) = lcm(m,n)/gcd(m,n)`. So the
move is **(gx, gy) -> (g, xy)** with x,y coprime. The two outputs are coprime.
Equivalently, in p-exponents (α,β) -> (min(α,β), |α-β|): the Euclidean step.

### Distinct openings

1. **Opening A — termination + "exactly one >1" (fully valuation-free).**
   - *Monovariant (P, c) in lex order, P = product of all board numbers, c = # of
     positions >1.* The pair-product mn -> g·xy = lcm = mn/g, so P -> P/g
     (factor g≥1; strict iff gcd(m,n)>1). c never increases: a move on two >1
     positions yields (g, xy); c drops by 1 when g=1 (coprime -> (1,mn)) or when
     xy=1 (i.e. m=n -> (m,1)), else c is unchanged. Thus each move strictly
     decreases (P, c) lexicographically (P primary, c secondary). ℕ² lex is
     well-founded (P bounded below by 1, c by 0; when P constant, c drops by 1
     only finitely many times). => termination.
   - *Exactly-one via the radical invariant.* The set of prime divisors of the
     total product is invariant: primes(mn) = primes(m)∪primes(n) = primes(g)∪
     primes(xy) (since g·xy = lcm has the same prime support as mn). It is
     nonempty initially (2026 numbers >1), so the total product is >1 forever.
     At a terminal state at most one number is >1; product >1 forces exactly one
     >1. This proves (a) with NO exponent/valuation work.

2. **Opening B — part (b) via confluence (Newman's lemma), valuation-free.**
   - Termination (Opening A) + local confluence => global confluence (Newman) =>
     unique normal form => M independent of choices. Local confluence only needs
     the critical pairs: two moves sharing one position, i.e. a triple (a,b,c).
     For S1 = result of move(a,b) and S2 = result of move(a,c), show S1 and S2
     have a common reduct. Disjoint (non-overlapping) redexes commute trivially.
   - The triple critical-pair joinability is the HARD step; verified numerically
     over 20000 random triples (0 non-joinable) and over full boards (unique
     terminal across 25 random play orderings, 3000 boards, 0 failures). It must
     be proven by hand — a finite gcd/lcm algebra lemma on triples.
   - Honest weak point: the critical-pair lemma is the crux and is essentially
     the per-prime Euclidean confluence done in disguise; a hand proof likely
     reduces to case analysis on exponent triples (α,β,γ) of the Euclidean step
     (min/max/difference). So Opening B may import valuation thinking to prove
     the lemma, even though the PROOF STRUCTURE stays valuation-free.

3. **Opening C — part (b) via the direct invariant M = ∏ p^{gcd of exponents}
   (minimal, clean valuation use).** Likely the intended solution.
   - Define d_p = gcd over all board positions of v_p(a_i); M = ∏_p p^{d_p}.
   - *Invariance:* the move replaces the two p-exponents (α,β) by
     (min(α,β), |α-β|); gcd(min(α,β), |α-β|) = gcd(α,β) (Euclidean identity).
     So d_p, hence M, is invariant.
   - *Terminal value:* at the terminal state the only number >1 is T; its
     p-exponents are (v_p(T), 0,...,0), whose gcd is v_p(T). So d_p = v_p(T) and
     T = ∏ p^{d_p} = M. Since M is an invariant of the INITIAL board, T is
     choice-independent.
   - Self-contained and airtight. Its only number-theoretic ingredient is the
     standard v_p and the one-line Euclidean gcd identity.

### Candidate technique(s)
- Invariant / monovariant (lexicographic pair (P, c)) — KB "Invariants &
  monovariants" / "General Proof Methods: Invariant / monovariant".
- Euclidean-descent / gcd-of-exponents invariance (per-prime
  (min,difference) step) — KB "Divisor analysis: gcd structure",
  "Vieta jumping & infinite descent".
- (Opening B only) abstract rewriting / Newman's lemma (termination + local
  confluence => confluence => unique normal form). Not in KB; cite as standard
  rewriting-theory tool. The "local confluence = critical-pair joinability on
  triples" is the load-bearing crux.

### Cheap-kill candidates
- Pairs that share no position commute (trivial confluence) — halves the casework
  for Opening B to a single triple-critical-pair check.
- Radical/prime-support invariance kills the "could it terminate with all 1s?"
  worry for free (Opening A, exactly-one step).
- The m=n self-pair case is its own trivial sub-case (produces (m,1)) and should
  be pulled out of the main case split.

### Knowledge-base entries to use
- "Invariants & monovariants" (combinatorics section) — for (P, c).
- "Infinite descent" / "Vieta jumping" (number theory) — the per-prime Euclidean
  (min, |α−β|) descent underlies both Openings B and C.
- "Divisor analysis: gcd structure" — the move (gx,gy)->(g,xy), gcd(x,y)=1.
- "Invariants & monovariants" (general methods) — same.

### Analogous past problems (cruxes)
- `aimo-0236` — "Reduce a two-player termination question to a single p-adic
  threshold" / "invariant under a halving step by p-adic valuation." A
  blackboard process whose termination is settled by a p-adic / monovariant
  threshold: same flavor (board + multiplicative monovariant + p-adic descent),
  though the mechanics differ (add a fixed constant vs gcd/lcm). Weak analogue.
- `aimo-0324` — "Assign each board position the squarefree part and use it as a
  one-sided monovariant." Same shape: a board number, a multiplicative
  radical/squarefree invariant as monovariant. Weak-to-moderate analogue; the
  crux move (squarefree part never increases) is directly portable in spirit.
- No corpus crux matches the gcd/lcm Euclidean-on-exponents move itself; the
  load-bearing idea (per-prime (min,|α−β|) = Euclidean algorithm preserving the
  gcd of the exponent multiset) is standard but not represented as a named crux.

### Prior progress
None (round 1; workspace empty).

### Dead ends (do not retry)
None yet.

### Small-case / intuition notes (CONJECTURE, verified numerically not proven)
- M = ∏_p p^{gcd_i v_p(a_i)} is CONFIRMED on all tested boards and all random
  play orderings (3000 boards incl. a 2026-element board; 0 confluence failures;
  terminal always equals the formula). E.g. {12,18}->6; {8,27,216,4}->54;
  {6,10,15}->30; {100,1000,10}->10; {4,9,36}->36; all-2s (2026 of them)->2 in
  2025 moves.
- A fully valuation-free CHARACTERIZATION of M does not appear to exist: the
  per-prime "gcd of exponents" is not a lattice (meet/join = min/max)
  operation on the divisibility lattice, so it cannot be written as any
  gcd/lcm expression in the raw integers (gcd of all a_i gives MIN of
  exponents, not their gcd). Thus the "no prime factorization" aspiration is
  satisfiable for (a) and for (b)-uniqueness-via-confluence, but NOT for a
  direct closed-form description of M; Opening C must invoke v_p to name M.
  This is the central honest weak point of the lens: the integer monovariant
  route solves (a) cleanly and can solve (b) via confluence, but the most
  transparent proof of (b) (Opening C) is valuation-based.
- The process on a single prime's exponent multiset is exactly the
  subtraction-Euclidean algorithm run in parallel across primes; the number of
  moves is bounded but can be large (2026-board took ~4912 moves; all-2s took
  2025).
