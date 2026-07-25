## imo-2026-01

NOTE: problems.jsonl lists `difficulty_level: "medium"` (`difficulty_rating: 5`) for this
problem, not `hard` — flagging per CLAUDE.md's "hard only" scope, but proceeding since I was
explicitly dispatched to this problem_id. `results/imo-2026-01/` is empty (no approaches,
lemmas, or current.md yet — this is the first round).

### The real invariant (this is the key finding of this lens)

Work per-prime. For a prime `p` and integer `x`, write `v_p(x)` for its exponent. A move
replaces `(m,n)` by `(g,L) = (gcd(m,n), lcm(m,n)/gcd(m,n))`. Per prime `p`, with
`a=v_p(m), b=v_p(n)`:
`v_p(g) = min(a,b)`, `v_p(L) = max(a,b) - min(a,b) = |a-b|`.

So **for each fixed prime, a move applies exactly one step of the *subtractive Euclidean
algorithm*** to the pair of exponents at the two chosen positions (all other positions'
exponents for that prime are untouched). The classical identity `gcd(min(a,b), |a-b|) =
gcd(a,b)` (standard Euclidean-algorithm invariant, true even when one of a,b is 0, since
gcd(0,x)=x) means:

**Invariant:** for every prime `p`, `g_p := gcd(v_p(a_1), …, v_p(a_2026))` (gcd of the
p-adic valuations across ALL 2026 board entries, current at any point in the process) is
*exactly preserved* by every move — not just non-increasing, but literally constant. Proof
sketch: `g_p` = gcd of (local pair's gcd) and (gcd of the untouched rest); the local pair's
gcd is preserved by the Euclidean step, so the whole thing is preserved.

This is **stronger and more useful than the naive candidates listed in the assigned lens**:
- Global product `∏ a_i`: NOT invariant — verified it only stays fixed when `gcd(m,n)=1`
  (coprime pick) and strictly decreases (divides by `gcd(m,n)`) whenever `gcd(m,n)>1`.
  It is a genuine termination monovariant but does NOT by itself pin down M (it only
  bounds M above by the initial product, with possible strict drops along the way).
- Sum of exponents `Ω_total = Σ_i Σ_p v_p(a_i)`: also NOT invariant. Computed exactly:
  `Ω(new pair) = Ω(m) + Ω(n) − Ω(gcd(m,n))`, so total `Ω` is non-increasing, strictly
  decreasing exactly when `gcd(m,n) > 1`, constant exactly when `m,n` coprime. Verified
  numerically (e.g. (12,18): Ω 6→4; (7,15) coprime: Ω 3→3 constant; (9,9): Ω 4→2).
- **`g_p` (gcd of exponents), by contrast, IS a true invariant (equality, not just
  monotone)** — this is the right quantity, and it directly determines the final M.

### Consequence: M is forced and computable

At a terminal state (no move possible ⇒ at most one board entry is `>1`), every prime's
exponent multiset is all-zero except possibly one entry (the survivor's). Since gcd of a
multiset that is all-zero-except-one-entry equals that one entry, and `g_p` is invariant
throughout, **the surviving number's `v_p` exponent must equal `g_p` computed from the
*original* board**, for every prime. Hence

  **M = ∏_p p^{g_p}, where g_p = gcd{v_p(a_1), …, v_p(a_2026)} over the original 2026
  numbers (gcd(0,...,0)=0 by convention if p never divides any a_i, contributing p^0=1).**

This is independent of the order/choice of moves by construction — settles part (b)
immediately, given part (a).

Part (a) — existence of exactly one survivor — needs (i) termination, (ii) not-all-collapse
-to-1. Both follow from the tools above:
- **Termination:** lexicographic potential `(Ω_total, K)` where `K` = number of entries
  `>1`, ordered by `Ω_total` first then `K`, strictly decreases every move: if
  `gcd(m,n)>1`, `Ω_total` strictly drops; if `gcd(m,n)=1` (so `m≠n`, since `m=n>1` has
  `gcd=m>1`), `Ω_total` is unchanged but one of the two results is exactly `1`
  (`gcd=1`), so `K` strictly drops. (Also checked the `m=n` case separately: `L=1`, so
  `Ω_total` drops there too — no case is missed.) Both components are non-negative
  integers, so the process is well-founded ⇒ terminates in finitely many moves.
- **Not all become 1:** since every `g_p` is invariant, and the original board has all
  entries `>1`, pick any prime `p` dividing `a_1`; then `g_p = gcd(v_p(a_1),0,…,0) =
  v_p(a_1) > 0` (gcd with zeros is the nonzero value), so `M = ∏ p^{g_p} ≥ p^{v_p(a_1)} >
  1`. So the terminal state cannot be all-1's; combined with "at most one survivor," it
  must be exactly one.

This single invariant (`g_p`, per prime) essentially proves BOTH parts of the problem in
one stroke — it's the strongest candidate technique found by this lens.

### Numerical verification (conjecture confirmed empirically, not yet a citation-grade proof)

Wrote a Python simulator (random legal move sequences on small boards, `math.gcd` +
`sympy.factorint`) and compared the final survivor against `M_pred = ∏_p p^{gcd of
original valuations}` across 20 random boards (sizes 3–6, values 2–60), 15 independent
random move-orders each. **All 300 runs matched exactly** (survivor == predicted M every
time; e.g. board `[50,58,28,4,18,34]` → M=1552950 regardless of order). This strongly
supports (but does not itself prove) the invariant argument above, which is a clean
algebraic proof, not just empirical.

### Distinct openings for the outliner

1. **Per-prime gcd-of-exponents invariant `g_p`** (this report's main finding) — proves
   both (a) and (b) together via one clean lemma (Euclidean-step preserves pairwise gcd,
   hence preserves the whole-multiset gcd). Likely the cleanest full solution route.
2. **Lexicographic monovariant `(Ω_total, K)`** for termination alone (part a only) — a
   standalone, simpler argument if the outliner wants to split termination from the value
   of M, but this alone does NOT establish part (b); needs the `g_p` invariant (or an
   equivalent) on top.
3. **Global product monovariant** — weaker, only gives an upper bound on M and
   termination-adjacent intuition; not sufficient alone, and could mislead (a "dead end"
   if pursued in isolation as *the* proof of (b), since product is not invariant).
4. A slicker equivalent framing: think of each prime's exponent vector as living
   through a "sorting-network-like" Euclidean process; note the *sum* invariant `g_p`
   is really "the process, per prime, is exactly a multi-item Euclidean algorithm run in
   parallel across all 2026 slots," which is a recognizable/citable pattern
   (`Invariants & monovariants`, `Divisor analysis` in the KB) worth naming explicitly in
   the writeup for rigor (cite the Euclidean gcd identity `gcd(a,b)=gcd(min(a,b),|a-b|)`
   explicitly).

### Candidate technique(s)
Invariant/monovariant method (KB: "Invariants & monovariants", combinatorics section;
"Invariant / monovariant" under General Proof Methods; "Divisor analysis" and "Modular
arithmetic, CRT" under Number Theory for the per-prime decomposition). The core fact
needed is the elementary Euclidean identity `gcd(a,b) = gcd(min(a,b), |a-b|)`, not
explicitly named as a KB entry but a standard consequence of the Euclidean algorithm
(closely related to LTE/`v_p` bookkeeping already in the KB).

### Cheap-kill candidates
None needed — the `g_p` invariant is a full structural proof, not a search/bound. The
"not-all-1" cheap check (pick any prime dividing any original entry, `g_p>0` for it) is
itself a one-line pigeonhole-free argument, already folded into part (a) above.

### Knowledge-base entries to use
- "Invariants & monovariants" (Combinatorics section) and "Invariant / monovariant"
  (General Proof Methods) — directly the technique.
- "Modular arithmetic, CRT" / prime-factorization decomposition idea (Number Theory) —
  motivates working prime-by-prime.
- "Divisor analysis" (gcd structure) — the Euclidean identity used is in this spirit.

### Analogous past problems (cruxes)
Searched `past_crux_moves_database.json` filtered to `domain=number_theory`,
`subtopic` in {`invariants-and-monovariants`, `p-adic-valuation`, `divisibility-and-gcd`}
(173 cruxes), and separately grepped `past_problems_database.json` for
"blackboard"+"gcd"/"replace"+"board" problems. Found no problem that is a genuine analog
of this specific "replace (m,n) by (gcd, lcm/gcd)" board process — the closest hits
(`aimo-0678`: a coupled recurrence `a_{n+1}=gcd+1, b_{n+1}=lcm-1` with sum invariant;
`aimo-0684`: an lcm-based modular indistinguishability argument) are superficially
gcd/lcm-flavored but not structurally analogous (different operation, different goal).
**Conclusion: none genuinely analogous found in the corpus** — this problem's exact
gcd/(lcm/gcd) replacement operation, and its reduction to a per-prime Euclidean process,
appears to be a fresh construction not matched by the corpus.

### Prior progress
None — `results/imo-2026-01/` had no approaches or current.md before this round; this is
the first exploration.

### Dead ends (do not retry)
- Trying to prove part (b) using *only* the global product monovariant (it is not
  invariant — it strictly drops on non-coprime moves — so it bounds M above but does not
  determine M exactly; any approach resting solely on "the product is conserved" is
  factually wrong and should be corrected/discarded).
- Trying to prove part (b) using *only* total Ω (sum of all exponents) as an invariant —
  same issue, it is a monovariant (non-increasing), not invariant, so cannot alone pin
  down M.

### Small-case / intuition notes
- Numerically confirmed (conjecture, backed by the algebraic argument above which is
  actually a proof, not just conjecture) that `M = ∏_p p^{gcd(v_p(a_1),…,v_p(a_2026))}`
  for every tested random board, independent of move order (300/300 matches across 20
  boards × 15 orders each).
- Small hand examples: `{4,4}` → forced move (only legal pair) gives `(gcd=4, L=1)` →
  M=4 = 4^{gcd(2,2)} = 4^2... wait `gcd(v_2(4),v_2(4))=gcd(2,2)=2`, so predicted
  `2^2=4`. Matches.
- `{6,10}`: `gcd=2,L=15`; new board `{2,15}` → next move forced: `gcd(2,15)=1`,
  `L=30`; final `{1,30}` → M=30. Predicted: `v_2`: gcd(1,1)=1→2^1=2; `v_3`: gcd(1,0)=1→3^1=3;
  `v_5`: gcd(0,1)=1→5^1=5; product=2·3·5=30. Matches.
