## imo-2026-03

### Task given
Scout for a top-level framing that does NOT go through "reduce to multiset
minimax of OddSum, then bound the minimax." Evaluate `dyadic-potential-invariant`
concretely, and check the crux corpus for potential/exchange techniques from
alternating-choice / cutting games that could give a single end-to-end argument.

### Verdict: no genuinely independent framing exists; the current field's split
into (reduction) + (two minimax bounds) is close to forced by the problem's
literal rules, not an artifact of one technique choice. `dyadic-potential-invariant`
as currently written is not that independent route either — and its central
technical claim (local per-split monotonicity of OddSum) is **false**, refuted
by direct computation below. Details follow.

### Why the reduction is close to unavoidable
The claiming phase's rule (alternately claim any unclaimed piece, maximize
own total) has a value on any *fixed* multiset of pieces that is a completely
determined, provably-correct number: the sum of the odd-ranked pieces in
descending order (`greedy-optimality-oddsum`, already reviewer-certified).
Any correct proof of the two-phase game — however it is packaged in prose,
whether as "potential function," "adversary strategy," or "casework" — must,
at the point where the marking phases end, correctly account for this same
number. So "OddSum of the eventual cut multiset" is not a technique choice
one approach made and another can route around; it is what the claiming
phase's payoff *is*. A "fresh framing" can change how the two marking phases
are analyzed (global casework vs. self-similar recursion vs. explicit
adversary response vs. a potential-based argument), but it cannot avoid
determining, directly or indirectly, the same combinatorial quantity. This is
why all three live approaches converge on the same reduction independently —
it is forced, not a shared blind spot.

### Testing dyadic-potential-invariant's crux claim
The approach's step 2 ("local split monotonicity") claims: splitting any one
piece of a multiset can only help LB (never decrease OddSum), with the
credit-weight machinery designed to "absorb" any rank-shift caused by the
split. I tested this directly (Python, exact simulation of OddSum before/after
a single random split of a random piece in an already-partitioned multiset):

```
before 0.9160 after 0.6693 delta -0.2467
before 0.9349 after 0.6137 delta -0.3212
before 0.9258 after 0.5537 delta -0.3722
before 0.7492 after 0.5728 delta -0.1764
```
(20-trial run; several trials show OddSum dropping sharply after a single
split — e.g. splitting a dominant piece into two roughly equal children can
demote both children below pieces that were previously "even-ranked," pulling
several other pieces' parity/rank down a cascade, not just a local
absorption.) **This refutes step 2 as literally stated**: there is no
per-split, locally-absorbable monotonicity — the effect of a single cut on
OddSum is global (depends on the full sorted order of all pieces, not a
bounded neighborhood around the split), exactly as the approach file's own
"Watch out for" paragraph already flagged as the main risk. This is a clean
cheap-kill: the approach's crux mechanism as designed cannot work; any
potential-based rescue would need a genuinely global (not per-piece, not
per-split-local) potential, and the approach file's own step 5 already
concedes that "achieving" the credits likely re-derives the OddSum
characterization anyway — i.e., even a repaired version most likely
collapses into a repackaging of `greedy-reduction-geometric`'s open gaps,
not an independent route.

### Crux corpus search (combinatorics: games-and-strategy, extremal-principle,
invariants-and-monovariants; filtered for stick/interval/cake/claim/piece
keywords)
- **aimo-0117** (already cited by the approach file) — Dutch TST stone-value
  game. Crux: assign a two-sided dyadic/geometric sequence of values so the
  single largest strictly exceeds the sum of all others, and separately,
  maintain the invariant "the largest played value is currently in my box"
  through an explicit induction that survives *any* single adversary move
  each round (not a static potential, but a per-round restorable claim).
  Genuinely analogous to the *lower-bound / achievability* side only (LB's
  geometric construction dominance, `2^n > 2^0+...+2^{n-1}`) — already fully
  used by all three live approaches' equality witnesses. Does not help with
  the open gaps (which are about XY's or LB's *responses*, not the seed
  construction).
- **aimo-0196** (2012-flavor coin-circle game) — crux: "size-weighted
  sub-interval as potential, strictly lowered by the adversary regardless of
  opponent's response" — same general shape as `universal-halving-adversary`'s
  program (an XY response that provably lowers a target quantity no matter
  how LB plays), but the underlying game (coins moving between boxes on a
  circle) is structurally too different (no sorted-rank/claiming mechanic)
  to transplant a specific construction; it confirms the *style* already in
  use, not a new framing.
- **aimo-0019** — dyadic-length frontier-painting game; superficially
  resembles "geometric sum of distinct negative powers of two" but the game
  mechanic (painting ahead of a frontier with an amortized linear potential)
  has no claiming/alternation/rank structure — not analogous.
- No crux in the corpus combines "alternating claim of sorted pieces" with a
  potential/weighting argument that proves both a lower and an upper bound
  from one certificate; games-and-strategy entries are dominated by
  pairing/mirroring (aimo-0066, aimo-0854, aimo-0596), blocking (aimo-0196,
  aimo-0445), and component-counting/pigeonhole liveness arguments
  (aimo-0663, aimo-0461) — none of these game shapes matches "sort a
  multiset, alternately claim, sum of odd ranks."

### A genuinely different high-level idea worth floating (not developed, not
a full route — flagged for the outliner to weigh)
Rather than splitting into two separate constructive gaps (Gap 1: LB's lower
bound holds against arbitrary XY; Gap 2: XY's upper bound holds against
arbitrary LB), consider recasting the value computation as a **minimax/LP
duality argument**: exhibit a single "certificate" — a weighting or dual
witness tied to LB's geometric partition $p_i = 2^i/(2^{n+1}-1)$ — that
simultaneously (a) proves no LB partition beats $c(n)$ against best XY
response (upper bound) and (b) proves the geometric partition attains
$c(n)$ against every XY response (lower bound), by exhibiting the same
object as playing both roles (à la von Neumann minimax: a value is
established once matching primal and dual strategies coincide). This is a
change of *proof architecture* (one certificate, not two case-built
arguments) rather than a change of top-level target — it still must resolve
into the same OddSum-based numbers, so it is not "independent" of the
reduction in the sense the dispatch asked about, but it is a genuinely
different attack from any of the three live approaches (none of which is
built around a duality/certificate object) and from the refuted
local-potential idea. This is speculative and unverified — I did not attempt
to construct the certificate; flagging only as a candidate direction if the
outliner wants a 4th, structurally distinct build-set member.

### Recommendation to outliner
1. Do not pursue `dyadic-potential-invariant` as currently written — its
   central mechanism is refuted (see numerical counterexamples above). If
   kept alive, it should be explicitly revised to a global (not per-split)
   invariant, and the outliner should be told this is very likely to
   collapse into `greedy-reduction-geometric`'s open gaps rather than being
   independent — treat as low priority / near-dead-end.
2. There is no evidence of a top-level framing that avoids the
   multiset-minimax reduction; it is closer to a restatement of the game's
   payoff than a technique choice. The "plateau" is a genuine mathematical
   difficulty (proving the two minimax directions), not a framing trap.
3. If the outliner wants field diversity per CLAUDE.md's plateau-break rule,
   the most promising *genuinely distinct* direction is a duality/certificate
   argument unifying both bounds (sketched above) rather than another
   variant of casework/induction/adversary-response — but this is unverified
   and should be treated as exploratory, not as a fix for the shared gap.

### Small-case / intuition notes (conjecture, not proof)
- Numerically re-confirmed (independent script) that splitting a piece can
  both raise and lower OddSum depending on where the split lands relative to
  the current sort order — consistent with the reviewer's existing finding
  that no "budget-free domination" shortcut exists.
- $1/c(n) = 2 - 2^{-n}$ (equivalent closed form to $c(n)=2^n/(2^{n+1}-1)$),
  giving the clean recursion $1/c(n) = 1/c(n-1) + 2^{-n}$, $1/c(0)=1$. This
  recursion is exactly the shape `self-similar-induction-on-n` is chasing
  (each level of recursion trims a factor of $2^{-n}$) — not a new
  observation but confirms that approach's telescoping target is the "right"
  algebraic shape, for whatever that's worth to the outliner in judging that
  approach's promise.

### Dead ends (confirmed / reconfirmed)
- `dyadic-potential-invariant`'s step 2 local split monotonicity: **refuted**
  by direct computation (see above) — do not attempt to prove it as stated.
- (Carried over, not re-verified but consistent with reviewer notes) "budget-
  free domination" argument, per `self-similar-induction-on-n`'s documented
  dead end — consistent with my numeric finding that a single split's effect
  on OddSum is not boundable by a fixed local rule.

### Prior progress
Unchanged from `current.md`: reduction fully proved; $n=0,1$ fully proved;
Case-1 lower bound proved; duplicate-the-rest exact response against the
geometric LB construction proved. Two open gaps as stated there (general
lower bound when XY cuts LB's own top piece, $n\ge2$; general upper bound
against arbitrary LB partitions, $n\ge2$). No change to this from my
exploration — I found no shortcut around either gap.
