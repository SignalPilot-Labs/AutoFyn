## imo-2026-01

### Headline finding (computational, verified extensively): the formula for M

Write `v_p(x)` for the p-adic valuation. For each prime `p`, define
`d_p = gcd( v_p(x_1), v_p(x_2), ..., v_p(x_2026) )` — the gcd of the exponent of
`p` across **all 2026 board numbers** (with the convention `gcd(0,0,...,0)=0`,
i.e. a prime dividing no board number contributes nothing, and `gcd` of a
multiset containing zeros equals the gcd of the nonzero entries, consistent
with `gcd(a,0)=a`).

**Conjecture (very strong computational evidence, not yet proved):**
`M = ∏_p p^{d_p}`.

This is emphatically **not** `lcm` of the initial numbers (that uses `max` per
prime, not `gcd`) — I first guessed lcm and it is wrong. Examples that kill the
lcm-guess and confirm the gcd-of-exponents formula:

- `[4,6,9]`: lcm = 36, but every simulated run terminates at `M=6`.
  `v_2` across the three numbers: `(2,1,0)`, gcd `= 1`. `v_3`: `(0,1,2)`, gcd
  `=1`. Formula gives `2^1·3^1=6`. Matches.
- `[8,12,18]` → `M=6` (lcm would be 72). `v_2=(3,2,1)` gcd 1, `v_3=(0,1,2)` gcd 1.
- `[100,45,60,36]` → `M=60` (lcm would be 900). `v_2=(2,0,2,2)` gcd 2,
  `v_3=(0,2,1,2)` gcd 1, `v_5=(2,0,1,0)` gcd 1. `2^2·3·5=60`. Matches.
- `[30,12,45,7]` → `M=210` (lcm would be 1260). Matches formula exactly.
- `[2,3,5,7]` (pairwise coprime) → `M=210=lcm`, consistent since with disjoint
  supports gcd-of-exponents and max-of-exponents coincide (each nonzero
  exponent list is a single 1, gcd=1=max).

I ran a stress test: 15 random instances with `N` between 4 and 9, entries up
to 60, simulating a **fully random legal move order** to termination each
time. Formula matched the simulated terminal `M` in all 15/15 cases (script:
`/tmp/sim.py`, `/tmp/sim2.py` — python3, sympy `factorint`). Also confirmed
move-order independence directly: 30 random move orders per test case in the
first batch always converged to the identical single value.

### Why this is true — the mechanism (this IS the real "sorting/confluence" content, but it's an invariant, not literally a sorting network)

Per-prime, a move on positions `i,j` with `v_p` values `(a,b)` replaces them
with `v_p(gcd) = min(a,b)` and `v_p(lcm/gcd) = |a-b|`. So **each prime's
exponent lane undergoes exactly the classical two-term subtractive-Euclidean
step** `(a,b) -> (min(a,b), |a-b|)`, applied *at the same two board slots*
simultaneously for every prime (this is the coupling that ties primes
together — a single move is one comparator applied in parallel across all
prime "lanes").

The key elementary fact: `gcd(min(a,b), |a-b|) = gcd(a,b)` (standard Euclidean
identity). Combined with associativity of gcd, this gives, for each fixed
prime `p`:

`gcd_{over all board positions}( v_p(x) )` is **invariant under every move**
— because a move only touches two positions' `v_p` values `a,b`, replacing
them by `min(a,b), |a-b|` whose pairwise gcd equals `gcd(a,b)`, so the gcd of
the whole multiset (= gcd of gcd(rest), a, b) is unchanged.

This is a clean, per-prime **exact invariant**, stronger and more direct than
a "sorting network" framing. (My assigned lens asked me to explore a
sorting-network/comparator angle — the "comparator" intuition is real: the
per-prime step is a genuine two-input comparator `(a,b)->(min,|a-b|)`, and a
move is literally a parallel application of the *same* comparator position
across every prime's lane simultaneously. But the right invariant to prove
part (b) is not "rank order settles" — it's this gcd invariant, which is
exact and elementary, no majorization/confluence machinery needed.)

**Part (b) essentially falls out immediately once part (a) is known:** if
termination leaves exactly one board entry `M>1` and all others `=1`, then for
each prime `p`, the board's multiset of `v_p` values is `{0,0,...,0,v_p(M)}`,
whose gcd is `v_p(M)` (by the `gcd(x,0)=x` convention, or `0` if `M` doesn't
contain `p`). Since this gcd equals the invariant `d_p` fixed from the start,
`v_p(M) = d_p` for every prime, forcing `M = ∏ p^{d_p}` — a value depending
only on the initial board, not on Confucius's choices. So (b) reduces to
proving the single invariant lemma above, which is a two-line Euclidean-gcd
argument.

### Part (a): termination — what I found, still a genuine gap

- **Total `Ω` (number of prime factors with multiplicity, i.e. `Σ_i Ω(x_i)`
  summed over the whole board) is itself invariant**, not just monovariant:
  for a chosen pair `(m,n)`, `Ω(gcd)+Ω(lcm/gcd) = Σ_p min(a_p,b_p) + Σ_p
  |a_p-b_p| = Σ_p max(a_p,b_p) `. Since `max(a,b) ≤ a+b` with equality iff
  `min(a,b)=0`, summing over all primes: `Ω(gcd)+Ω(lcm/gcd) ≤ Ω(m)+Ω(n)`, with
  **equality exactly when `gcd(m,n)=1`** (no prime shared). So `Σ Ω(x_i)` over
  the board is non-increasing, strictly decreasing whenever the chosen pair
  shares a common prime factor, and unchanged (but the *values* still change —
  they get "combined") when the chosen pair is coprime.
- Because total `Ω` is bounded below by 0 and only changes by taking
  non-negative integer steps, it cannot decrease infinitely often — but this
  alone doesn't finish termination, because a run could in principle choose
  coprime pairs forever without decreasing `ΣΩ`, while never becoming
  "stuck." Need a secondary monovariant. Candidate found: for a pair
  `(m,n)` with `A=Ω(m), B=Ω(n)`, the new pair `(g, A+B-g)` with `g=Ω(gcd(m,n))
  ≤ min(A,B)` **majorizes** `(A,B)` (spreads it further apart), with
  **strict** spread (sum of squares of `Ω(x_i)` over the whole board strictly
  increases) unless `g = min(A,B)`, which happens iff `m | n` or `n | m`.
  Sum of squares of `Ω(x_i)` is bounded above (total `ΣΩ` is fixed/non-
  increasing, so sum of squares ≤ (total)²), giving a bounded monotone
  quantity — but the "divides" case (`m|n`) is a loophole where sum-of-squares
  doesn't strictly increase even though the actual numbers change (e.g.
  `(m,n)=(2,4)` are already gcd/lcm-stable in one sense, but `(m, n/m)` = `(2,
  2)`, a genuine new state). This edge case needs to be closed with a further
  argument (e.g. that the total number of board entries `>1` cannot increase,
  is a nonincreasing integer sequence bounded below by 1, and use a lexicographic
  or well-ordering combination of (# entries `>1`, ΣΩ, Σ(Ω)²) to force strict
  decrease at each step under an appropriate combined ordering) — I did **not**
  work this out rigorously; flagging it as the gap for part (a).

### Distinct openings for the outliner

1. **Direct invariant + reduction (recommended primary route).** Prove the
   per-prime gcd invariant `d_p` (two-line Euclidean argument) first; this
   immediately gives part (b) *given* part (a). Then attack part (a)
   separately with a monovariant (candidate: total `ΣΩ(x_i)` non-increasing,
   refine with sum-of-squares / lexicographic tie-break for the `m|n` edge
   case, or find a cleaner single potential function — e.g. `Σ_i Ω(x_i)^2` or
   number of unordered pairs `(i,j)` with `gcd(x_i,x_j)>1`).
2. **Comparator/sorting-network framing (weaker, exploratory).** View each
   prime lane as undergoing repeated applications of the 2-input comparator
   `(a,b)->(min(a,b),|a-b|)` at synchronized positions across primes; this
   reframes as a token/chip process but doesn't obviously simplify beyond
   opening 1 — the gcd invariant already gives the clean answer, so this
   framing is mostly useful as *intuition*, not as the actual proof vehicle.
3. **Bound on number of moves for part (a).** Since `ΣΩ(x_i)` is fixed at
   `ΣΩ(initial numbers)` and only the "spread" (sum of squares) can increase
   and is bounded by `(ΣΩ)²`, one can likely get an explicit finite bound on
   the number of moves (useful if the problem wants an explicit bound, though
   the statement here only asks for finiteness).

### Cheap-kill candidates
- None needed — no contradiction/parity trick kills this outright; it is a
  genuine construction + invariant problem. The "cheap kill" here is exactly
  the invariant found above, which does most of part (b)'s work almost for
  free once part (a) is granted.

### Knowledge-base entries to use
- `## Number Theory` — "Divisor analysis" entry (gcd structure) is the closest
  named KB entry but doesn't state this exact identity; the load-bearing fact
  (`gcd(min(a,b),|a-b|)=gcd(a,b)`) is elementary and should be proved inline,
  citing the Euclidean algorithm identity `gcd(a,b)=gcd(a-b,b)`.
- `## General Proof Methods` / any "Invariants & monovariants" combinatorics
  entry — the general heuristic (find a preserved quantity under the move) is
  exactly the KB's "Invariants & monovariants" bullet under Combinatorics;
  cite that as the meta-technique.
- `## Monotone Subsequences...` section not directly relevant here (that's for
  sequence/patience-sort problems, different flavor).

### Analogous past problems (cruxes)
- Searched crux corpus for `domain=number_theory` filtered by keywords
  "gcd"+"lcm" together (11 hits) and by `subtopic=invariants-and-monovariants`
  (2 hits) and `subtopic=p-adic-valuation` (57 hits, skimmed). **None are a
  close structural match.** The nearest thematic hit, `aimo-0324` (Amy/Bob
  blackboard game using the squarefree-part function `S(n)` as a
  monovariant), is a genuinely different game (subtraction/power moves, not
  gcd/lcm replacement) — same *flavor* of "define an arithmetic function of
  the board number as monovariant" but not an analogous crux move to copy. I
  do not recommend forcing this match. **Verdict: no strong analogous crux
  found**; this problem's core trick (gcd-of-exponents invariant under the
  `(a,b)->(min,|a-b|)` comparator) appears to be a fresh construction not
  well-represented in the pre-2026 corpus as searched.

### Prior progress
None — round 1, workspace was empty (`results/imo-2026-01/` had no
`current.md` or approaches yet at time of writing).

### Dead ends (do not retry)
- **`M = lcm(all initial numbers)`** — my first natural guess, refuted by
  direct simulation (e.g. `[4,6,9]` gives lcm 36 but every simulated
  termination gives `M=6`). Do not use lcm-of-all as the answer.
- Pure per-prime independent "sort exponents into slots" framing without the
  gcd invariant does not by itself explain move-order-independence cleanly —
  the gcd invariant is the clean route; don't spend a round trying to build a
  full "sorting network confluence" (Batcher/odd-even, Church-Rosser
  rewriting) argument from scratch, since the actual invariant is much
  shorter and elementary.

### Small-case / intuition notes (all labeled conjecture except the invariant identity, which is a proved elementary fact)
- **Proved (elementary, not just conjectured):** for a single prime `p`,
  `gcd(min(a,b), |a-b|) = gcd(a,b)`, hence `d_p := gcd` over the whole board of
  `v_p(x_i)` is exactly invariant under every move. This is a rigorous
  one-line fact (standard Euclidean-algorithm identity), safe for the
  outliner to use directly as a lemma.
- **Conjectured (strong computational evidence, 15/15 random stress tests +
  8 hand examples, all matching exactly, but not yet proved rigorously that
  termination always yields exactly this single value without a full proof of
  part (a)):** `M = ∏_p p^{d_p}`. Given the invariant lemma is proved, this
  reduces entirely to proving part (a) (termination with exactly one entry
  `>1`), after which part (b)'s value is forced automatically as shown above.
- Termination itself (part a) is not yet nailed down rigorously by my
  exploration — flagged as the remaining gap, with a concrete monovariant
  candidate (`ΣΩ(x_i)`, refined by sum-of-squares / divisibility edge case)
  for the outliner to develop.
