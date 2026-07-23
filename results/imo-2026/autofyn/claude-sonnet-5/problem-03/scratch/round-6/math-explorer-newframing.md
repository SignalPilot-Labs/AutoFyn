## imo-2026-03

### Summary of my lens
Dispatched to scout a whole-problem framing genuinely far from the shared field
(Lemma G order-statistic reduction → D/M-operation / physical-cut casework). Conclusion
up front: **every candidate "genuinely different" framing I could construct either (a)
collapses provably into a wall the population has already hit (global concavity /
Schur-convexity, Sion's minimax), or (b) is isomorphic to the population's current
leading open sub-problem (the non-crossing-matching+deletion conjecture / the self-similar
recursion), just described in different words.** I verified both equivalences concretely
below (not just asserted). This is itself useful negative information per the dispatch's
point 3 — it means the "shared framing" is not actually a *choice* the population made
that could be swapped out cheaply; Lemma G (greedy = optimal in the alternating-claim
subgame) is a forced, already-proved fact about the INNER game, and the real diversity
axis is in how the OUTER minimax over cuts is analyzed, where I could not find a route
that avoids re-deriving essentially the same content. I did find one genuinely-untried
sub-idea (LP-relaxation + integrality-gap framing for the isolated k=m+1 tight case) that
is techniquewise distinct, though it targets the same isolated sub-problem as
`potential-weighting-upper-bound`'s non-crossing conjecture — worth flagging as a possible
6th distinct technique on that specific gap, not a whole-problem alternative.

### Distinct openings I tested (with verdicts)

**1. Self-similar recursion in n directly: `c(n) = 2c(n-1)/(2c(n-1)+1)`.**
Algebraically confirmed exact for the conjectured closed form (verified by fraction
arithmetic n=1..7, see below) — this recursion is a true fact ABOUT THE ANSWER, and comes
from the dyadic construction's own self-similarity: removing `D_n`'s top piece
`2^n/(2^{n+1}-1)` leaves the remaining `n` pieces equal to `D_{n-1}` rescaled by
`(2^n-1)/(2^{n+1}-1)`. **But**: turning this into an independent proof route requires
showing the TRUE game value (not just the conjectured closed form) satisfies this
recursion — i.e. that it is WLOG optimal for Liu Bang to "wall off" a dominant piece and
recurse on the residual as an untouched (n-1)-mark sub-game. Proving that WLOG-optimality
is *exactly* the still-open question of whether Xiang Yu's cuts landing inside the
dominant piece can ever help him beyond the target — i.e. it is a restatement of the
existing "all-cycles"/multi-cut-inside-dominant-piece gap (`dm-completeness-partial.md`,
`superincreasing-no-early-zero.md`'s remaining caveat), not an independent route. **Verdict:
equivalent to the existing gap, already correctly declined once (round 5); do not re-open
as a "new" slug.**

**2. Majorization / Schur-convexity of `e(M) = alternating sum of sorted M` as a global
tool for the lower bound (treating the whole final partition abstractly, no D/M language,
no physical-cut casework).** Tested directly: is `e` Schur-convex (monotone under
majorization) on sorted compositions of a fixed sum? Exact counterexample at k=3:
`(1/2,1/2,0)` majorizes `(1/3,1/3,1/3)` (partial sums 1/2≥1/3, 1≥2/3 — confirmed
computationally), yet `e(1/2,1/2,0)=0 < e(1/3,1/3,1/3)=1/3`. So `e` is **not**
Schur-convex once `k≥3`. This failure is exactly the duplicate-pair-collapse phenomenon
(Lemma P: a tied pair contributes 0 to `e`) — i.e. the SAME underlying mechanism that
already kills global concavity of `g` (certified dead end,
`lemmas/non-concavity-of-g-at-n2.md`). **Verdict: not an independent framing — it is the
non-concavity dead end wearing different clothes (majorization language instead of
concavity language). Do not recommend as a fresh slug.**

**3. "Xiang Yu's whole strategy = for each Liu-Bang piece, leave it alone or subdivide it
further" + direct matching/scheduling analysis of the resulting alternating-claim game
(dispatch's explicit check #2).** I traced this precisely against the population's own
content: this is *exactly* the already-isolated tight case `k=m+1` sub-problem that
`potential-weighting-upper-bound` is attacking via its "chain-prefix + one-shot tail" +
"non-crossing matching + deletion" conjecture (§7 of that file) — allocating a cut budget
across the `m+1` original pieces and analyzing the resulting global sort IS the
matching/scheduling framing, already built, already stress-tested (560+ generic +160
Case-ii-specific + 400 further trials, zero mismatches, still unproved). **Verdict:
genuinely the same framing already in the population, not a new one** — confirms the
dispatch's suspicion. It would not give a shorter path; it *is* the current leading
open item.

**4. LP/game duality (Sion's minimax) on the whole sequential game.** Already tried and
killed (round 3, `concavity-minimax-duality`): this is a *sequential* (Stackelberg)
game, not simultaneous, so Sion's minimax theorem doesn't even apply without independent
justification — confirmed as a standing per-role rule (`/tmp/memory/math-explorer.md` #11).
**Verdict: dead end, do not revive.**

**5. Entropy/information-theoretic bound.** Considered but discarded as implausible: the
target `2^n/(2^{n+1}-1)` is an exact rational tied to a specific superincreasing/dyadic
combinatorial structure, not an asymptotic rate; an entropy argument would naturally give
only an asymptotic or non-tight bound, not the exact extremal value with a matching
construction required by CLAUDE.md's "solved" bar. Not pursued further — flagged as
low-plausibility rather than tested to failure.

### One genuinely new (if narrow) idea worth flagging
**LP relaxation + integrality-gap framing for the isolated `k=m+1` tight case.** Instead of
searching for the exact optimal *matching/deletion* policy (current non-crossing conjecture),
relax "allocate `m` cuts among `m+1` pieces, each piece optimally split by its allotted
cuts" to a continuous/fractional LP over cut-allocations, solve the (separable, and
possibly closed-form via Fact 2/Fact 3 of `insertion-and-cascade-facts.md`) LP explicitly,
then bound the integrality gap between the LP optimum and the true integer-cut combinatorial
optimum. This is a genuinely different *technique* (LP relaxation + rounding bound, in the
spirit of the KB's linear-algebra-method / extremal-principle entries) from both the
lookahead family (dead) and the non-crossing-matching conjecture (unresolved) — but it
targets the SAME isolated sub-problem (`k=m+1`), so it is a new tool for the shared gap,
not a whole-problem-diverse 5th slug on its own. I did not build or test this (out of scope
for exploration, and it needs the LP to actually be tractable/closed-form, unverified) —
flagging as a lead, not a result.

### Candidate technique(s)
None beyond what's already certified/in-flight in the population's files. The forced
foundation (Lemma G: greedy = optimal in the alternating-claim subgame) is not something a
different top-level framing can avoid — it is a proven fact about the inner game, not a
choice of proof strategy. Genuine diversity for this problem lives entirely in HOW the
outer minimax over Liu Bang's/Xiang Yu's cut choices is bounded, and I found the two live
open sub-problems (upper-bound `k=m+1` tight case; lower-bound "all-cycles" caveat) to be
the actual bottlenecks that any "new" framing eventually reduces to.

### Cheap-kill candidates
None new found this round (Schur-convexity's cheap kill — the `(1/2,1/2,0)` vs
`(1/3,1/3,1/3)` counterexample above — is itself a cheap kill of opening #2, already used).

### Knowledge-base entries relevant
- **Hall's marriage theorem / SDR** (`knowledge_base.md` Combinatorics section) — considered
  for a matching-based repackaging of the claim-order argument; concluded not applicable
  beyond what Lemma G already gives (Lemma G's greedy-optimality proof doesn't need Hall's
  theorem, and a Hall's-theorem-flavored argument on the `k=m+1` tight case would just be
  the non-crossing-matching conjecture, already in-population).
- **Extremal graph theory / dyadic-bucket decomposition**, **Invariants & monovariants** —
  already the load-bearing tools behind the certified lemmas (superincreasing-no-early-zero,
  slack-collapse); no new entry identified.
- No linear-algebra-method or generating-functions KB entry matches this problem's structure
  closely enough to suggest a fresh mechanism (checked; the KB's linear-algebra entries are
  about quadratic forms / manifolds, not discrete allocation LPs).

### Analogous past problems (cruxes)
Searched `past_crux_moves_database.json` filtered to `domain=combinatorics`,
`subtopic=games-and-strategy` (40 cruxes) plus `extremal-principle` (166) and
`linear-algebra-method` (16); also full-text-searched `past_problems_database.json` for
stick/interval/cutting/alternating-claim game statements.
- **`aimo-0117`** (Jesse/Tjeerd stone-box game) — already the crux behind the population's
  dyadic construction ("assign values as a two-sided geometric sequence so the largest value
  exceeds the sum of all others"). Confirmed still the best match in the corpus; no new
  insight beyond what's already exploited.
- **`aimo-0196`** — already adapted by `concavity-minimax-duality` for its potential/monovariant
  attempt on the lower bound ("frozen this turn" trick). Confirmed still the right adaptation
  for that specific open item; not a new whole-problem framing.
- No crux in the corpus matches the literal "mark points on a stick / cut / alternately claim
  whole pieces" structure — the closest surface-level matches (`aimo-0717` strip-cutting,
  `aimo-0663` number-choosing game, `aimo-0461` knight-placement game) were read and are
  **not genuinely analogous**: `aimo-0717` is a modular-labeling reconstruction problem with
  no adversarial claiming; `aimo-0663`/`aimo-0461` are impartial/blocking games with no
  continuous-quantity claiming structure. None recommended as a crux import beyond the two
  already in use.

### Prior progress
See `results/imo-2026-03/current.md` (unchanged by me — I did not build). As of round 5:
lower bound fully proved for every `m` in the D/M-sequence-restricted sense
(Superincreasing No-Early-Zero Lemma), modulo the "all-cycles" D/M-completeness caveat;
upper bound reduced to the single tight case `k=m+1` (Slack Collapse), with the
"non-crossing matching+deletion" conjecture proposed but unproved for that case.

### Dead ends (confirmed/reconfirmed this round, do not retry)
- Global concavity of `g` (round 3, certified dead) — and its majorization/Schur-convexity
  restatement (opening #2 above, newly confirmed dead this round via the same underlying
  duplicate-pair mechanism).
- Sion's minimax theorem / simultaneous-game LP duality on this sequential Stackelberg game
  (round 3, confirmed dead, reconfirmed applicable-scope check this round).
- The self-similar `c(n)` recursion as an INDEPENDENT proof route (declined round 5; this
  round I traced exactly why — it's a restatement of the still-open multi-cut/all-cycles gap,
  not a shortcut around it).
- The "leave-alone-or-subdivide + matching/scheduling" framing the dispatch asked me to check
  is confirmed **isomorphic** to `potential-weighting-upper-bound`'s already-in-flight
  non-crossing-matching+deletion conjecture for the `k=m+1` case — not a new opening.

### Small-case / intuition notes (labeled as conjecture where unproved)
- Confirmed exactly (fraction arithmetic, n=1..7): `2^n/(2^{n+1}-1) = 2c(n-1)/(2c(n-1)+1)`
  where `c(n-1)=2^{n-1}/(2^n-1)` — a true algebraic identity of the conjectured closed form,
  consistent with (but not a proof of) the self-similar structure of the dyadic construction.
- Confirmed exactly: `e(1,0,0)=1`, `e(1/2,1/2,0)=0`, `e(1/3,1/3,1/3)=1/3`, with
  `(1/2,1/2,0)` majorizing `(1/3,1/3,1/3)` — a clean, minimal witness that `e` is not
  Schur-convex once 3 elements are involved, reusable if any future approach proposes a
  majorization-based mechanism.
