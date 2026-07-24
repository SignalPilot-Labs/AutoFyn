## imo-2026-01

### The per-prime move, worked out exactly
Fix a prime `p`. For any two board entries `m, n` at positions `i,j`, write `a = v_p(m)`, `b = v_p(n)`
(the p-adic valuations). Since `v_p(gcd(m,n)) = min(a,b)` and `v_p(lcm(m,n)) = max(a,b)`, the new pair
of valuations at positions `i,j` is
```
(a,b)  -->  ( min(a,b), max(a,b) - min(a,b) )  =  ( min(a,b), |a-b| ).
```
All *other* positions' valuations at `p` are untouched. Crucially, **the same pair of positions
(i,j) is transformed simultaneously for every prime p** — a single board-move is one common
transposition-pair applied across all primes at once; you cannot choose a different pairing per
prime. This is the coupling: the per-prime processes are not independent random walks, they are
locked together by the shared choice of positions.

### Key invariant (found and numerically confirmed): gcd of the valuation multiset
The pairwise map `(a,b) -> (min(a,b), |a-b|)` is exactly one step of the subtractive Euclidean
algorithm, and it **preserves `gcd(a,b)`** (standard fact: `gcd(a-b,b) = gcd(a,b)`, and
`gcd(min(a,b),|a-b|) = gcd(a,b)` in both orderings). Consequently, for the *entire* multiset of
valuations at `p` across all 2026 positions,
```
gcd( v_p(x_1), ..., v_p(x_2026) )
```
is invariant under every move: writing the global gcd as `gcd( gcd(v_i,v_j), other v_k's )`, the
inner `gcd(v_i,v_j)` is unchanged by the move and the other `v_k` are untouched, so the whole
expression is unchanged (using associativity of gcd over a multiset, and the convention
`gcd(x,0)=x`).

**This invariant, if the termination in part (a) is granted, immediately gives part (b) (and
pins down the value of M):** once the process halts with only one entry `M > 1` (all others `=1`),
the valuation multiset at `p` is `(0,...,0, v_p(M))`, whose gcd is just `v_p(M)`. Hence
```
v_p(M) = gcd( v_p(a_1), ..., v_p(a_2026) )   for every prime p,
```
i.e. **M = ∏_p p^{gcd_i v_p(a_i)}** is an explicit, move-independent formula in the *original*
2026 numbers. This is choice-independence (part b) directly from the invariant, with no need to
compare two different move sequences — both reach the *same* invariant value.

Verified numerically: wrote a Python simulation (`gcd`/`lcm` swap process) and ran 30 random
starting multisets of 2–6 numbers, each with 20 different random move orders; every run's final
`M` matched the predicted formula `∏_p p^{gcd of valuations}` exactly (see transcript in this
session — 100% match, no failures). This is strong conjecture-level evidence, not a proof, but the
underlying gcd-invariance argument above is a genuine algebraic identity (not just pattern-matching)
so this is very likely the actual crux.

### Termination (part a): candidate monovariants
Two natural non-increasing quantities, both provably monotone from the same per-prime valuation
picture:
1. **`Ω(∏ board)` = total number of prime factors with multiplicity of the product of all board
   entries.** Per prime p, the pairwise move sends `(a,b) -> (min,|diff|)`, and
   `min(a,b) + |a-b| = max(a,b) ≤ a+b`, with **equality iff min(a,b)=0** (i.e. `p` does not divide
   `gcd(m,n)`). Summing over all primes: `Ω` of the touched pair goes from `Ω(m)+Ω(n)` down to
   `Ω(lcm(m,n)) ≤ Ω(m)+Ω(n)`, strictly less whenever `gcd(m,n) > 1`, unchanged iff `gcd(m,n)=1`.
   So Ω(∏ board) is non-increasing, bounded below by 0, and strictly decreases on any move with
   `gcd(m,n)>1`.
2. **Count of entries `>1`.** If `gcd(m,n)=1`, the move replaces `m,n` (both >1) with `1` and `mn`
   (a single entry >1) — the count of entries `>1` strictly decreases by exactly 1. If
   `gcd(m,n)>1`, the count can stay the same (generic case) — but Ω decreases instead.

**Combined monovariant:** the lexicographic pair `(Ω(∏ board), #{entries > 1})` strictly decreases
at *every* single move (case gcd>1: first coordinate drops; case gcd=1: first coordinate constant,
second strictly drops). Since this pair lives in `ℕ×ℕ` with the lexicographic well-order, the
process must terminate after finitely many moves — this is the clean route to part (a). (Also
worth noting as a check: the *total product* of all board entries is non-increasing and invariant
exactly on gcd=1 moves — a secondary sanity monovariant, consistent with `M ≤ ∏ a_i`, equality iff
every move along the way happened to be a coprime merge — but this is not needed for termination.)

At halt, no move is possible, i.e. fewer than 2 entries are `>1`. To rule out the terminal state
being "all entries = 1" (zero survivors), use the invariant: for any prime `p` dividing some
original `a_i`, `gcd_i v_p(a_i) ≥ 1` (gcd of a multiset of naturals not all zero, when at least one
is positive, is itself ≥1), and this gcd is invariant, so at every point in the process some entry
still carries a positive valuation at p — in particular at the end `v_p(M) ≥ 1`, so `M>1`. So the
terminal state has *exactly* one entry `>1`, not zero.

### Cheap-kill / structural notes
- Working per-prime cleanly **decouples the Diophantine mess of gcd/lcm into pure integer
  arithmetic on valuations** — no need to argue about actual integer factorizations directly, only
  about the multiset-of-exponents evolution. This is the main structural win of this lens.
- The coupling across primes (same position-pair for every prime simultaneously) matters only for
  *part (a)*'s bookkeeping (need one shared monovariant, Ω(∏), that aggregates over all primes at
  once — you cannot argue "prime p's sub-process terminates" independently per prime, since a
  move might not touch prime p at all, e.g. if `m,n` are coprime to `p`). For *part (b)* the
  coupling is irrelevant: the invariant `gcd_i v_p(a_i)` holds prime-by-prime regardless of which
  positions get chosen, precisely because the *same* pairwise transform hits whichever two
  positions are chosen, and gcd-preservation is proven per pair regardless of who's paired with whom.
- Parity / small cases: `n=2`ka numbers `(m,n)`: one move, `M = gcd(m,n)·(lcm/gcd) = lcm(m,n)`, and
  indeed `lcm(m,n) = ∏ p^{max(v_p(m),v_p(n))}` — but wait, our formula says `gcd` of valuations, not
  max! Check with `n=2`: multiset of valuations at `p` is just `{a,b}`, `gcd(a,b)`, so predicted
  `M = ∏ p^{gcd(v_p(m),v_p(n))} = gcd(m,n)` overall?? Let's recheck against the direct one-move
  computation: `M = gcd(m,n) · lcm(m,n)/gcd(m,n) = lcm(m,n)`. But the invariant formula would need
  `gcd(a,b)` per prime to equal `v_p(lcm)=max(a,b)` — these disagree in general (e.g. a=2,b=5:
  gcd=1, max=5). **This looks like a contradiction — flag this as needing re-examination**: for
  `n=2` numbers there is only ONE move possible (the two entries), so the process is forced, and
  the result is definitionally `lcm(m,n)`, yet the "invariant" I derived would predict
  `∏ p^{gcd(v_p(m),v_p(n))} = gcd(m,n)`. Only one of these can be right. Re-derivation: for `n=2`,
  the global gcd of the *two-entry* valuation multiset `{a,b}` is `gcd(a,b)`, and my claimed
  invariance says this equals `v_p(M)` at the end where the multiset is `{v_p(g), v_p(l/g)}` with
  `g=gcd(m,n), l/g = lcm/gcd`; entries there are `min(a,b)` and `|a-b|`, and `gcd(min(a,b),|a-b|)
  = gcd(a,b)` — consistent — **but the terminal state for n=2 still has TWO entries** (both `g` and
  `l/g` are on the board — the process only continues if ≥2 entries are `>1`; if BOTH `g>1` and
  `l/g>1` the process is *not* done, another move fires!). So my example computation above (n=2:
  32,3) happened to have gcd=1 so it finished in one move giving `M=lcm=96=32·3`. **For the general
  n=2 case where gcd(m,n)>1 initially, the process does NOT stop after one move** — it keeps going
  (e.g. m=8,n=4: gcd=4,lcm/gcd=2, board becomes {4,2}, both >1, continue: gcd=2,lcm/gcd=2, board
  {2,2}, continue: gcd=2,lcm/gcd=1, board {2,1} — stop, M=2). Check formula: v_2(8)=3,v_2(4)=2,
  gcd(3,2)=1, so predicted M=2^1=2. **Matches!** So my "flag" above was a false alarm from
  conflating "one move" with "process terminates in one move" — the n=2 case is NOT generally
  one move; it iterates until one side hits 1, and the fully-reduced result is genuinely
  `∏ p^{gcd(v_p(m),v_p(n))}`, i.e. **M = gcd(m,n)** when there are only 2 numbers total (not
  lcm(m,n) as I mistakenly said) — the `32,3` example only looked like `lcm` because `gcd(32,3)=1`
  and `lcm(m,n)=m·n/gcd(m,n)=mn` when coprime, which for that example coincides with `M` only
  because gcd=1 forces immediate 1-move termination with `M = mn = lcm`. **General 2-number case:
  M = gcd(m,n)`, confirmed by direct Euclidean-algorithm reasoning (repeatedly replacing (a,b) by
  (min,|diff|) on valuations is literally the subtractive Euclidean algorithm, which converges to
  (gcd(a,b), 0) i.e. one entry becomes p^0=1) — this is a clean, fully worked sub-case an outliner
  can use as the base case / sanity check.**

### Candidate technique(s) / knowledge-base entries
- **Invariants & monovariants** (Combinatorics section, knowledge_base.md) — directly the named
  technique; both halves of the problem are textbook instances (invariant for uniqueness/value,
  monovariant for termination).
- **Divisor analysis / gcd structure**, **Modular arithmetic, CRT** entries are the generic NT
  entries but not load-bearing here — the real content is elementary (Euclidean algorithm on
  exponents), not modular arithmetic per se.
- Note for the outliner: this problem is fundamentally about the **subtractive Euclidean algorithm
  applied simultaneously, prime by prime, to exponent vectors** — reducible to "prove gcd(a,b) is
  invariant under (a,b)->(min,|a-b|)" (one line) plus "prove Ω(∏)+count monovariant terminates"
  (short, elementary). No deep machinery (LTE, Zsigmondy, Hensel) is needed.

### Analogous past problems (crux corpus)
Searched `number_theory` subtopics `invariants-and-monovariants`, `p-adic-valuation`,
`divisibility-and-gcd` (173 cruxes) and `combinatorics` `processes-and-algorithms` (48 cruxes) for
board/replace-pair processes. **No crux is a close match to this exact gcd/lcm-swap process.**
The closest surface-level analogue is `aimo-0836` (China, board with numbers `1..n`, move erases
`a,b` and writes `a+b` and `|a-b|` if not already present) — same flavor of "replace two board
numbers by a sum-like and a difference-like pair," and `|a-b|` is structurally the same subtractive
step that appears in our per-prime valuation transform — but the actual operation, invariants, and
question (can exactly 2 remain, vs. must exactly 1 remain / is it unique) are different enough that
it should be read only for flavor, not treated as a template to adapt. `aimo-0324` (Amy/Bob
`n -> n^k` / `n-a^2` game using squarefree-part `S(n)` as monovariant) is a nice example of a
"squarefree-part invariant" but not directly transferable. Overall: **no strong crux match; the
invariant/monovariant pair described above should be derived directly rather than adapted from a
retrieved solution.**

### Prior progress
None — this is round 1, `results/imo-2026-01/approaches/` and `/lemmas/` are both empty.

### Dead ends
None yet recorded (no approaches exist yet). One thing to flag for the outliner so it isn't
mis-stated: **M is NOT simply `lcm(a_1,...,a_2026)`** (my first guess) — a direct 3-number
simulation (4, 8, 3) gives `M=6`, not `lcm(4,8,3)=24`. Also **M is NOT simply `gcd(a_1,...,a_2026)`**
in general for n>2 — e.g. (4,8,3) has `gcd=1` but `M=6≠1`. The correct closed form is the
per-prime-gcd-of-valuations formula above; do not let the outliner default to plain lcm or plain
gcd of the initial numbers.

### Small-case / intuition notes (conjectural, numerically verified)
- **Conjecture (strong, algebraically motivated + 30/30 random trials confirm, various move
  orders each):** `M = ∏_p p^{gcd_i(v_p(a_i))}`, equivalently the largest `d` such that
  `d | a_i^{k_i}`-type statement is awkward to phrase directly, but concretely: for each prime,
  raise it to the gcd of its exponents across all 2026 numbers, and multiply over all primes
  dividing at least one `a_i`.
- Two-number sanity check: `M = gcd(m,n)` (the process is literally the subtractive Euclidean
  algorithm run to completion on the valuation vector, prime by prime).
- Sanity check with all-equal numbers `a_1=...=a_2026=k`: gcd of valuations = each `v_p(k)` itself
  (gcd of `v_p(k)` repeated 2026 times is `v_p(k)`), so predicted `M=k`, plausible (any two equal
  entries -> gcd=k, lcm/gcd=1, so pairs immediately collapse to 1, and by induction everything
  collapses to a single `k`) — consistent.
