# Explorer report — imo-2026-01 (Confucius gcd/lcm blackboard)

## 0. Problem / bookkeeping

- `problems.jsonl`: domain `number_theory`, task `proof_only`, `answer_type: none`,
  `difficulty_level: "medium"`, `difficulty_rating: 5`. (Lower than the repo's
  usual "hard" bar, but run_state.md records an explicit user override making
  this the sole Goal for this run — noted, not re-litigated here.)
- No `results/imo-2026-01.md` existed. I created one with `## Status: unsolved`,
  empty `Approaches tried` / `Current best` (per instructions I did **not**
  attempt or outline the proof there — see file for the skeleton).
- No prior round progress exists anywhere (fresh problem).

## 1. Knowledge-base entries that bear on this problem

From `knowledge_base.md`:

- **"Invariant / monovariant"** (General Proof Methods): "find a quantity that
  never changes (or only moves one way) to prove reachability/unreachability or
  termination." This is the literal technique needed for **both** parts: a
  monovariant for (a) termination, an invariant for (b) order-independence.
- **"Invariants & monovariants"** (Combinatorics section): same idea, filed
  under combinatorics — confirms this problem's true genre is "invariant/
  monovariant on a process," not standard multiplicative number theory, even
  though `problems.jsonl` files it as `number_theory`.
- **Meta-Strategy** bullet: "a multiplicity or `v_p` count" as a one-move
  structural kill. This is exactly the right lever — see §5, the whole problem
  cracks open by looking at `v_p` (p-adic valuation) of each board entry,
  independently per prime.
- **"Divisor analysis"** (Number Theory): "gcd structure ... bounding a finite
  search by size" — generic pointer to gcd-structure reasoning, weakly relevant.
- **"Induction" / "Infinite descent"** (General Proof Methods / Vieta jumping &
  descent): relevant only in the loose sense that termination is a descent-style
  argument (a strictly-decreasing positive-integer potential); no actual Vieta
  jumping or induction-on-a-constructed-object is needed.
- Nothing in Modular arithmetic/CRT, LTE, Zsigmondy, Hensel, orders/primitive
  roots is relevant — this is not a "solve a congruence" or "prime order" problem
  despite being filed as number theory.

## 2. Crux corpus search (see `crux_moves_documentation.md` schema: `technique`,
`how_used`, `domain`, `subtopic` in `past_crux_moves_database.json`; `problem` /
`solutions` in `past_problems_database.json`, joined by `problem_id`)

Filtered `domain=number_theory` on subtopics `invariants-and-monovariants`
(only 2 hits total in NT — this genre is filed mostly under **combinatorics**
in this corpus, 181 `invariants-and-monovariants` + 48 `processes-and-algorithms`
hits there), `divisibility-and-gcd`, `p-adic-valuation`, `size-bounding-and-descent`,
`games-and-strategy`. Also grepped both databases directly for `gcd(`+`lcm(`
co-occurring and for `blackboard`+`replace`/`erase`.

**Honest verdict: no genuinely analogous crux.** Nothing in the corpus performs
a repeated pairwise gcd/lcm exchange on a multiset with an order-independent
terminal value. The closest hits are same-genre, different-mechanics — useful
only as *style* confirmation, not as adaptable steps:

- **`aimo-0917`** (IMO SL 2020, combinatorics/invariants-and-monovariants) —
  blackboard starts with 2020 copies of 1; a move erases `x,y` and writes
  `x+y` or `|x-y|`; game ends when one number dominates the sum of the rest or
  all are 0. Crux: track each survivor's "range" (how many original 1's it
  descends from) as a conserved weight, then use `S_2(a+b) ≤ S_2(a)+S_2(b)`
  (binary digit-sum subadditivity) to lower-bound the final count. **Structurally
  the closest "blackboard, repeatedly combine two entries" problem in the
  corpus**, but it's a 2-player adversarial game (min-max value), reduces board
  size by 1 each move (our problem keeps the board size fixed at 2026, hiding
  "dead" 1's), and its invariant (binary weight) doesn't transfer. Useful only
  as a reminder of the "conserved per-survivor weight" proof shape.
- **`aimo-0236`** (USAMO 2023/4, combinatorics/invariants-and-monovariants) —
  Alice replaces `n` with `n+a`, Bob replaces even `n` with `n/2`; forced
  termination. Crux: `S = Σ v_2(x)` (sum of 2-adic valuations over the board) is
  the monovariant that forces termination in the relevant regime. **Good style
  match for part (a)**: a sum-of-`v_p` monovariant is exactly the flavor of
  potential I found below (§5.1), independently confirming that "sum of a
  p-adic-valuation-like quantity across the board" is a natural termination
  potential for blackboard problems — but the game mechanics (adversarial,
  addition-based) are unrelated.
- **`aimo-0563`** (IMO SL 2022 C6, combinatorics/invariants-and-monovariants) —
  `n` piles of 1 pebble; move: take equal counts from two piles, form a new
  pile; find the minimum achievable number of nonempty piles (answer: 1 if `n`
  is a power of 2, else 2). Crux: a fixed odd `m>1` dividing all pile sizes
  propagates *backward* through the move, so it's a genuine "invariant pins
  down the reachable terminal values" argument — same **shape** as what part
  (b) needs (an invariant that survives every move and reads off directly at
  the end), but the actual invariant (an odd divisor) and the operation
  (equal-subtraction merge) don't match ours at all.
- **`aimo-0678`** (IMO SL 2015 N4) is the only crux anywhere in the corpus whose
  `how_used` text contains both `gcd(` and `lcm(` — but it's about eventual
  periodicity of the 2-term recurrence `a_{n+1}=gcd(a_n,b_n)+1`,
  `b_{n+1}=lcm(a_n,b_n)-1`, not a multiset reduction. Not usable beyond noting
  it's a "frozen sum in a special regime" trick (loosely similar in flavor to
  tracking `Φ` below).

**Conclusion: do not force any of these as a template.** They only corroborate
that the right *category* of tool (a monovariant potential for termination, a
provably-backward/forward invariant for uniqueness) is correct; none supplies
the actual invariant, which had to be derived from scratch (§5).

## 3. Assessment of the user's seed framing

The seed says: *"Write the entries currently on the board as `x_1,...,x_2026`.
Entries equal to 1 remain on the board, but they cannot be selected for a
subsequent move."*

This is **correct and safe**, but it is a restatement of the rules, not a lever.
It correctly identifies one true fact — call it Fact 0: *once a position hits 1
it is frozen forever* (a move only ever touches two positions both currently
`>1`, so a position already at 1 is never chosen again and never changes again).
This fact is real and is exactly what makes `c := #{positions with value > 1}`
into a well-defined, non-increasing counter (see §5.1) — so the seed is "on the
promising track" in the sense that the count of live (`>1`) positions is indeed
part of the right potential function. But by itself it says nothing about *why*
the process must stop (a monovariant/potential is still needed — `c` alone can
stay constant for many moves in a row, see §5.1) or about *what value* survives
(needs a second, multiplicative/valuation-based invariant, see §5.2). **The
natural next step the proof needs is: (1) a quantity that strictly decreases on
every move (not just "eventually"), to prove termination, and (2) a quantity
attached to the whole board that is exactly preserved by every move, so that
reading it off at the end (when the board is `1,...,1,M`) pins down `M`.**
Both of these are the real content of the problem; the seed doesn't yet reach
either.

## 4. Cheap-kill / pruning checks

- **`N = 2026` appears to carry no special number-theoretic role.** I could
  find no reason the argument would need `N` even, `N ≡ anything`, etc. — the
  termination/invariance argument (§5) goes through verbatim for any `N ≥ 1`
  (trivial for `N=1`: no legal move exists, `M = x_1`). Treat "2026" as flavor
  only; a proof attempt that tries to extract meaning from 2026's factorization
  is very likely a wrong track. Worth flagging so the outliner doesn't spend
  time there.
- **`N=2` sanity check (no real choice exists):** with only two numbers, there
  is only one possible move each turn (positions 1,2), so "independent of
  choices" is vacuous/trivial for `N=2` — useful only as a base case /
  sanity-check of the general-`N` invariant formula (§5.2), not as part of the
  real proof (which needs `N` arbitrary with genuine branching).
- **Pairwise-coprime starting numbers** are an easy warm-up: every first move
  is forced to have `gcd=1` (whichever pair you pick), producing `(1, mn)`;
  by induction the whole process is forced and `M = x_1 x_2 \cdots x_{2026}`
  (ordinary product) — this is the degenerate case of the general formula in
  §5.2 (when supports are disjoint, "gcd of exponents across the board" only
  ever sees one nonzero term per prime, so it just returns that exponent,
  i.e. the general invariant collapses to the product). Good sanity check, not
  a distinct proof path.
- **A single shared prime is enough to keep it alive:** if prime `p` divides
  even one starting number, `p` must divide `M` (see §5.1's persistence
  argument) — this immediately kills any hope that "generic" boards end at
  `M=1`, so nobody should waste time trying to show the board can fully
  collapse to all-ones.

## 5. Small-case / intuition notes — **conjectural, numerically verified, not a
proof** (this is the material to hand to the outliner; I did not write it up
as a formal multi-lemma proof, per role scope)

**Key reformulation (the actual unlock).** Fix a prime `p`. For a move on
`m,n`, let `x=v_p(m), y=v_p(n)` (`p`-adic valuations). Since `gcd`/`lcm`
correspond to coordinatewise `min`/`max` on prime exponents,
`v_p(\gcd(m,n)) = \min(x,y)` and `v_p(\operatorname{lcm}(m,n)/\gcd(m,n)) =
\max(x,y)-\min(x,y) = |x-y|`. **So every move, viewed one prime at a time, is
the same elementary transform `(x,y) \mapsto (\min(x,y), |x-y|)` applied
independently to each prime's exponent-multiset, always at the same pair of
board positions.** This decoupling is the crux of the whole problem; everything
below follows from analyzing this transform.

### 5.1 Termination (part a) — candidate monovariant

Let `c` = number of board positions currently `> 1`, and `Φ` = product of all
2026 current board entries (a positive integer). Per move on `m,n` (with
`g=\gcd(m,n)`, new pair `(g,\,mn/g^2)`):

- `Φ_{\text{new}} = Φ_{\text{old}}/g` (strict decrease iff `g>1`).
- **Corrected dichotomy for `c`** (verified against 20,000 random `(m,n)`
  pairs, 0 exceptions — my first hand-derivation of the boundary was wrong and
  I caught it by recomputing, see below): `c` drops by exactly 1 iff `g=1` **or**
  `m=n`; otherwise (`g>1` and `m≠n`) `c` is unchanged. (Note: `g>1` and `m≠n`
  includes the case where the smaller divides the larger, e.g. `m=4,n=8`,
  `g=4`, new pair `(4,2)` — both still `>1`, so `c` does *not* drop there; I
  initially mis-stated this boundary as "`1<g<\min(m,n)` strictly," which is
  false — `m=4,n=8` has `g=\min(m,n)=4` exactly and still gives `c` unchanged.
  Recorded here so the outliner doesn't repeat that slip.)
- Candidate potential `Ψ := Φ \cdot 2^{c}`. Case check: `g=1` ⟹ `Ψ` halves;
  `g>1,m=n` ⟹ `Ψ` drops by factor `2g ≥ 4`; `g>1,m≠n` ⟹ `Ψ` drops by factor
  `g ≥ 2`. **In all cases `Ψ` strictly at-least-halves.** Verified by direct
  simulation logging `Ψ` before/after every individual move across 200 random
  trials (1718 total moves checked): 0 violations of "`Ψ_{\text{after}} ≤
  Ψ_{\text{before}}/2}`". Since `Ψ` is always a positive integer, it can halve
  at most `\log_2(Ψ_{\text{initial}})` times ⟹ **finite termination**, and the
  process can only stop when `c ≤ 1` (a move is legal exactly when `c ≥ 2`,
  since any two `>1` entries may be combined with no other precondition).
- **Ruling out `c=0`** (all entries collapse to 1) needs a separate argument:
  fix any prime `p \mid x_1` (exists since `x_1>1`). Check by 3 cases (`p`
  divides neither / exactly one / both of the chosen `m,n`) that "`p` divides
  at least one current board entry" is preserved by every move — in the
  "exactly one" case (say `p\mid m`, `p\nmid n`), `v_p(|x-y|) = x > 0` so `p`
  persists onto the `\operatorname{lcm}/\gcd` output; in the "both" case, `p`
  persists onto the `\gcd` output. So this is a genuine move-invariant, true
  initially (witnessed by `x_1`), hence true at the end — but `1` is not
  divisible by `p`, so the surviving `M` must be (forcing `c=1` exactly, not 0).

This gives a full termination argument in outline (potential `Ψ` for finiteness
+ a persistence invariant to rule out the empty case) — **conjectural / not
written up rigorously by me**, but every piece above has been either checked
exhaustively for small ranges or stress-tested numerically; I believe this
converts to a real proof with modest, mostly casework, effort.

### 5.2 Order-independence of `M` (part b) — candidate invariant

Elementary lemma (checked exhaustively for all `x,y \in \{0,\dots,59\}`, 0
exceptions — this one I could also prove by hand in 2 lines via the standard
subtractive-Euclidean-algorithm identity `\gcd(a,b)=\gcd(a,b-a)`):
`\gcd(\min(x,y), |x-y|) = \gcd(x,y)`.

Define, for positive integers `a,b`, `a \oplus b :=` the integer whose
`p`-adic valuation is `\gcd(v_p(a), v_p(b))` for every prime `p` (finite
support, well-defined by unique factorization; `a \oplus 1 = a` since
`v_p(1)=0` and `\gcd(k,0)=k`). Applying the elementary lemma prime-by-prime to
`x=v_p(m), y=v_p(n)` gives, for every move: **`m \oplus n = \gcd(m,n) \oplus
(\operatorname{lcm}(m,n)/\gcd(m,n))`** — i.e. a move preserves the `\oplus`-value
of the exact pair it touches. Since `\oplus` is built prime-by-prime from
`\gcd` (commutative, associative on `\mathbb{Z}_{\ge0}`), `\oplus` itself is
commutative and associative on the whole board, so the *whole-board*
combination `x_1 \oplus x_2 \oplus \cdots \oplus x_{2026}` is unchanged by any
single move (isolate the touched pair via associativity; untouched entries
don't move). At the end the board is `1,\dots,1,M`, and `1` is the identity
for `\oplus`, so the whole-board combination equals `M` exactly. **Hence `M =
x_1 \oplus x_2 \oplus \cdots \oplus x_{2026}`, a formula fixed entirely by the
*original* board — independent of every choice Confucius makes.** This is the
whole content of part (b), reduced to: (i) the elementary lemma above, (ii)
associativity/commutativity of `\oplus` (immediate from that of `\gcd`), (iii)
noting `1` is the identity.

**Numerical verification of the whole conjecture (process + formula), not
just the pieces:** simulated the full process with uniformly random legal
move choices, 30 independent random move-orders per test case, across 11
diverse starting multisets (sizes 2–5: coprime tuples, prime-power tuples,
repeated-equal-entries, mixed composite numbers up to `2^6\cdot3^5` etc.).
**Every trial's terminal `M` matched the closed-form prediction exactly, and
matched across all 30 different random orders per case** — e.g.
`[8,12,20]\to M=30` (in 5–7 moves depending on order), `[100,75,50,40,8]\to
M=30` (11–15 moves), `[576,1944,500,189,2310]\to M=2310` (13–22 moves). Note
**the number of moves is *not* invariant** (only `M` is) — worth flagging so
nobody mistakes "number of moves" for a second invariant to prove.

### 5.3 Refuted guesses (dead ends — do not retry)

- **`M = \gcd(x_1,\ldots,x_{2026})`** (naive overall board gcd): false. Example
  `(4,8)`: process forces `\to(4,2)\to(2,2)\to(2,1)`, so `M=2`, but
  `\gcd(4,8)=4 \ne 2`. Also, the *running* overall gcd of the whole board is
  **not even an invariant during the process** once `N\ge3` — example
  `(128,64,32)` (as `2`-exponents `(7,6,5)`, overall gcd `=32=2^5`): combining
  `128,64\to(64,2)` gives board `(64,2,32)`, overall gcd `=2`, i.e. it can drop
  from `2^5` to `2^1` in a single move. Don't pursue "board gcd" as the
  invariant.
- **`M = \operatorname{lcm}(x_1,\ldots,x_{2026})`**: false for the same `(4,8)`
  example (`\operatorname{lcm}=8\ne2`).
- **Number of moves as an invariant**: false — varies by move order even for
  fixed starting data (see §5.2 numbers above).

## Summary for the outliner

- Part (a): monovariant `Ψ = Φ\cdot2^c` (product of board × 2^(count of live
  entries)) for finite termination, plus a single-prime "persistence" argument
  to rule out the board collapsing to all-1's. Both pieces are elementary case
  checks (few cases each), not deep.
- Part (b): the `\oplus` operation (coordinatewise `\gcd` of `p`-adic
  valuations) is preserved on the touched pair every move (via the standard
  Euclidean identity `\gcd(\min(x,y),|x-y|)=\gcd(x,y)`), hence — by
  associativity/commutativity of `\oplus`, inherited from `\gcd` — the
  whole-board `\oplus`-combination is a true invariant, and it evaluates to `M`
  at the end because `1` is the `\oplus`-identity. This simultaneously gives an
  explicit formula for `M` in terms of the original 2026 numbers.
- Both directions are strongly supported by exhaustive small-range checks of
  the two elementary lemmas and by full-process randomized simulation (330
  runs total, 0 mismatches against the closed-form prediction) — but I have
  **not** written this up as a rigorous, fully-cased proof; that is the
  outliner's/builder's job. Flag clearly to the builder: the "corrected
  dichotomy" boundary in §5.1 is subtle (I got it wrong on first pass by hand)
  and needs a careful, explicit 3-way case split (`g=1` / `g>1,m=n` /
  `g>1,m\ne n`) rather than a size-based shortcut like "`g<\min(m,n)`".
