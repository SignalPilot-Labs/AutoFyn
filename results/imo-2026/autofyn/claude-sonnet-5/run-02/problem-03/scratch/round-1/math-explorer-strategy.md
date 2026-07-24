## imo-2026-03 (lens: direct strategy construction from first principles)

### Key reduction lemma (verified, not yet write-proven)
Given a FIXED final multiset of piece lengths, the alternating "claim any unclaimed
piece to maximize own total sum" game (Liu Bang first) has value: sort pieces
descending L_1 ≥ L_2 ≥ ... ≥ L_m; the unique optimal play for BOTH players is
greedy (always take the current largest remaining piece), and the outcome is
Liu Bang = Σ_{i odd} L_i, Xiang Yu = Σ_{i even} L_i. Piece *identity/position*
is irrelevant — only the multiset of lengths matters, since claiming has no
adjacency/positional constraint. I confirmed this by exact brute-force minimax
over random small piece sets (up to 7 pieces, 2000 trials) vs. the greedy formula
— always matched (script: sorted-descending-alternation always equals true
minimax). This lemma is the load-bearing simplification: the whole problem
reduces to a *pure interval-cutting* combinatorial game — Liu Bang picks ≤n
points, Xiang Yu picks ≤n points to minimize Σ_{odd rank} of the final
piece-length multiset, and we want max over Liu Bang of min over Xiang Yu.
(This lemma should still be proven rigorously in the outline — the exchange-argument
proof is short: an inductive/exchange argument on "always take the max remaining
element is weakly dominant for the mover, for both players, since payoffs are
additive with no cross-term other than which pieces are already gone.")

### Conjectured answer (strong numerical evidence)
**c(n) = 2^n / (2^{n+1} − 1).**

Matches n=1 → 2/3, n=2 → 4/7, n=3 → 8/15 (all numerically confirmed below).

### Distinct openings
1. **Xiang-Yu-side (upper bound) opening**: for ANY Liu Bang configuration of
   ≤ n points (≤ n+1 pieces), Xiang Yu's strategy is to *bisect* (split exactly
   in half) a well-chosen subset of Liu Bang's pieces using his ≤ n points —
   NOT necessarily the largest pieces, and NOT necessarily "make total piece
   count even." The right target set is discovered by matching Liu Bang's
   worst-case config: when Liu Bang uses the geometric config (sizes
   2^n,...,2^1,2^0)/(2^{n+1}-1), Xiang Yu's matching best response (numerically
   verified, value exactly equal to the top piece 2^n/(2^{n+1}-1)) bisects
   pieces in a way that reproduces the *same* geometric ratio-2 self-similar
   structure at a finer scale — i.e. this configuration is essentially a fixed
   point of the bisection operation. The natural general Xiang Yu strategy to
   conjecture/prove for the upper bound: repeatedly halve the *largest* not-yet-
   halved piece is close but NOT exactly optimal for asymmetric configs (see
   below); the real invariant to hunt for is potential-function/exchange style:
   show that for any Liu Bang piece multiset, Xiang Yu can always force
   Σ_{odd rank} ≤ 2^n/(2^{n+1}−1) by a bisection strategy that greedily reduces
   the "excess" of the current largest piece over the target ratio.
2. **Liu-Bang-side (lower bound / construction) opening**: Liu Bang marks
   EXACTLY n points (not fewer) creating n+1 pieces in **geometric ratio 2**:
   sizes 2^n, 2^{n-1}, …, 2, 1 (in units of 1/(2^{n+1}−1)). This is a genuinely
   different-in-kind construction from "n+1 near-equal pieces" (which is
   strictly worse — see cheap-kill below) or "one big piece + rest tiny." The
   robustness intuition: no single piece is disproportionately valuable
   relative to the pieces below it (each is exactly double the next), so any
   bisection Xiang Yu performs on piece k just produces two pieces of size
   equal to piece k+1 — i.e. bisecting doesn't create any *new* size class,
   it just duplicates an existing rung of the geometric ladder. This
   self-similarity is very likely the actual reason the construction is
   optimal (a "no free lunch" structural argument for Xiang Yu), and is the
   natural target for a clean inductive proof (induct on n, or induct on the
   ladder rungs, using a potential function Σ 2^{-i} L_i type argument).
3. **Alternative framing — potential/weight function opening**: define weight
   w(L) for a piece of length L such that the greedy alternating game total
   for Liu Bang, for the geometric ladder AND all its bisection-descendants,
   is invariant. Concretely: assign to piece of "rank" j in the ladder
   (size 2^{n-j}/(2^{n+1}-1)) the value 1 if j has liu-bang-favorable parity;
   this looks like it wants a 2-adic / binary-representation argument (each
   piece's size is a power of 2 over a fixed odd denominator 2^{n+1}-1) —
   worth checking if there's a clean bijective/potential argument using binary
   expansions, akin to a Nim-value or a weighting scheme showing Σ_{Liu Bang's
   pieces} = top piece value exactly, always, for the ladder and any subgame
   reachable from it by legal cuts.

### Candidate technique(s)
- Direct minimax / exchange-argument on the reduced "sorted-multiset alternation"
  game (see lemma above) — likely provable via a clean induction on number of
  pieces removed (a classical "greedy is optimal in a value-additive alternating
  selection game" argument; not adjacency-constrained, so simpler than typical
  "coins in a row" olympiad games).
- Self-similarity / fixed-point argument for the geometric-ratio-2 construction:
  induction on n (peel off the largest piece, argue the remaining subgame is
  the n−1 case up to relabeling).
- Invariant/monovariant hunting on Σ_{odd-rank pieces} under a single bisection
  move, to pin down Xiang Yu's exact optimal response structure.

### Cheap-kill candidates
- **Equal-pieces construction is dominated**: tested numerically — Liu Bang
  marking n+1 EQUAL pieces (1/(n+1) each) lets Xiang Yu push Liu Bang down to
  exactly 1/2 using far fewer than n points (for n=2, one single bisection of
  any piece already gets Xiang Yu to 1/2, using only 1 of his 2 points). Prune
  this direction immediately — equal splits are provably worse than the
  geometric-ratio-2 ladder (0.5 < 4/7). Do not re-explore "balanced Liu Bang"
  as a serious candidate.
- **"XY always attacks the smallest piece to flip parity" is NOT a universal
  Xiang Yu strategy** — it is effective against near-tied top pieces (e.g.
  Liu Bang (0.4,0.4,0.2) → XY bisects the smallest 0.2 piece, not the big
  ones, to get to 0.5) but is strictly worse than bisecting the top pieces
  against the geometric ladder or against skewed configs like (0.6,0.3,0.1)
  (numerically, XY's best response there bisects the TWO LARGEST pieces,
  giving 0.55, using both points — bisecting only the smallest gives only 0.65).
  So "which pieces Xiang Yu bisects" is configuration-dependent; the outliner
  should not assume a single fixed rule works for all Liu Bang configs — only
  claim it against the specific optimal ladder / whichever config is under
  the microscope for the upper-bound argument.
- Parity/counting cheap fact: total pieces = 1 + (Liu Bang's point count) +
  (Xiang Yu's point count) ≤ 2n+1; Liu Bang, moving first, gets exactly
  ⌈(#pieces)/2⌉ of the pieces by count (not value) under greedy play — useful
  bookkeeping but NOT by itself a tight bound (value matters far more than count,
  as the n=2 exploration shows: 3-piece and 5-piece configs both realize c(2)=4/7).

### Knowledge-base entries to use
- **Pigeonhole / extremal principle**, **Invariants & monovariants** (general
  combinatorics section) — for the self-similarity / fixed-point argument on
  the geometric ladder.
- **Constructive vs. existence**: "find largest c" needs BOTH the upper bound
  (Xiang Yu's spoiling strategy, general n) AND the matching construction
  (Liu Bang's geometric-ladder marking) — per CLAUDE.md rigor rules, both
  halves are mandatory for `solved`.
- **Problem-Solving Heuristics (Pólya)** — "solve a simpler case first," "look
  for self-similar / recursive structure" — directly what cracked this via
  n=1, n=2, n=3 computation.
- No number-theory / algebra KB entries are directly relevant; this is a pure
  combinatorial game/extremal-construction problem. The "games-and-strategy"
  crux subtopic is the right lens (see below) but I found no closely analogous
  cataloged crux (see next section).

### Analogous past problems (cruxes)
Searched `past_crux_moves_database.json` filtered to
`domain=combinatorics, subtopic=games-and-strategy` (39 entries) and scanned
`past_problems_database.json` for stick/interval/cutting/claiming games. **None
are genuinely analogous.** The 39 games-and-strategy cruxes are almost all
pairing/mirroring/invariant-parity strategies on discrete boards or token games
(e.g. aimo-0115 domino pairing, aimo-0663 component-counting pigeonhole,
aimo-0596 involution-pairing card game) — none involve a continuous stick,
alternating-claim-of-pieces-by-value game, or a two-phase
mark-then-claim structure. I did not force a match. If the outliner wants a
loose structural echo, aimo-0117 ("assign values as a two-sided geometric/dyadic
sequence so the single largest value strictly exceeds the sum of all others")
uses a similar *geometric/dyadic-ladder* construction idea (each term dominates
the sum of smaller ones) — worth a glance for the *proof technique* of showing
a geometric ladder is self-protecting, even though the underlying problem
(a game about played values, not stick-cutting) is different. Treat as a
technique echo, not a solved analog.

### Prior progress
None — round 1, fresh workspace (results/imo-2026-03/current.md is empty,
Status: unsolved, no approaches yet).

### Dead ends (do not retry)
- Equal-piece (balanced) Liu Bang marking — strictly dominated by the geometric
  ladder (see cheap-kill above); do not pursue as the optimal construction.
- Treating "Xiang Yu bisects the smallest piece to flip parity" as a universal
  optimal Xiang Yu strategy — it is only locally optimal for near-tied
  top-piece configurations, not in general (see cheap-kill above). A correct
  upper-bound proof needs Xiang Yu's strategy to be a function of the FULL
  Liu Bang configuration, not a fixed rule.
- (Not literally "tried and failed" yet since this is round 1 with no prior
  approaches — flagging these as traps discovered during exploration so the
  outliner doesn't waste a round on them.)

### Small-case / intuition notes (all labeled CONJECTURE / numerical evidence)
- n=1: **rigorously hand-derived** (not just numerical) — Liu Bang marks one
  point, WLOG piece sizes (x, 1−x) with x ≤ 1/2. Xiang Yu's best response is
  either "don't cut" (value 1−x) or "bisect the larger piece exactly in half"
  (value (1+x)/2 — I showed this is optimal among all single-cut positions on
  the big piece via a "maximize the median of the resulting 3 values" argument,
  and showed cutting the smaller piece x is always weakly worse for Xiang Yu
  than leaving it alone). Liu Bang then maximizes min(1−x,(1+x)/2) over x,
  attained at x=1/3 (where the two options tie), giving **c(1) = 2/3 exactly**,
  with final configuration THREE EQUAL pieces of 1/3 (Liu Bang gets 2 of 3
  by count AND exactly 2/3 by value). This is a fully rigorous mini-proof for
  n=1, reusable directly in the outline.
- n=2: numerical minimax search (Nelder-Mead multistart, 800+ restarts on the
  best candidates) found the geometric ladder (4/7, 2/7, 1/7) achieves
  Xiang-Yu-best-response = 4/7 exactly (matched to 1e-9), and no config found
  in a grid search beat 4/7 (best found via coarse grid: (0.58,0.28,0.14),
  converging to (4/7,2/7,1/7) under refinement). CONJECTURE: c(2) = 4/7.
- n=3: geometric ladder (8/15,4/15,2/15,1/15) numerically gives Xiang-Yu-best-
  response = 8/15 exactly (matched to 1e-9, 300+ restarts up to 3 extra XY
  points). CONJECTURE: c(3) = 8/15, consistent with formula 2^n/(2^{n+1}−1).
- General CONJECTURE (strong, from n=1,2,3 exact/near-exact matches):
  **c(n) = 2^n / (2^{n+1} − 1)**, with Liu Bang's optimal marking being the
  geometric ladder of n+1 pieces with lengths 2^n, 2^{n-1}, …, 2, 1 (in units
  of 1/(2^{n+1}−1)), and the extremal final configuration under optimal
  Xiang Yu play again reduces (self-similarly, by bisection) to a finer
  geometric-ladder-like multiset whose odd-rank sum still equals the top
  piece's value 2^n/(2^{n+1}−1). NOTE: I have NOT identified Xiang Yu's exact
  general-n optimal response strategy in closed form (only verified
  numerically for n≤3) — this is the key remaining gap for a full proof: (a)
  a clean description of Xiang Yu's universal spoiling strategy against the
  geometric ladder (which pieces to bisect, in what order, using ≤n points)
  that provably caps Liu Bang at exactly 2^n/(2^{n+1}−1); and (b) a general
  proof (not just numerics) that Xiang Yu can enforce this cap against *any*
  Liu Bang marking, not just the ladder — i.e. the true upper-bound argument
  for arbitrary Liu Bang configurations of ≤n points.
