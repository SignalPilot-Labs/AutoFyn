## imo-2026-03

greedy-reduction-geometric: new
Target: c(n) = 2^n/(2^{n+1}-1) for all n ≥ 0 (full compute_and_prove claim).
Technique: Two-phase minimax reduction — exchange-argument greedy-optimality
lemma for alternating claiming over a fixed multiset, collapsing the
problem to a pure combinatorial-geometry minimax over piece-length
partitions, plus an explicit geometric (1,2,4,...,2^n) construction for the
lower bound.
Skeleton:
  1. Greedy-optimality lemma: alternating-claim value over any fixed
     multiset = sum of odd-ranked (descending) pieces — by induction on
     multiset size with an exchange/coupling argument.
  2. Position-irrelevance: only the length-multiset (not spatial order)
     matters, since splitting is a purely local length operation.
  3. Reduction to: LB picks ≤n+1 pieces (max), XY splits ≤n further
     (min), payoff = odd-rank sum.
  4. Lower bound: LB's geometric partition 2^0,...,2^n (scaled by
     1/(2^{n+1}-1)) guarantees ≥ 2^n/(2^{n+1}-1) against any XY response —
     by strong induction on n using the dominance identity
     2^n > 2^0+...+2^{n-1}.
  5. Upper bound (OPEN): any LB partition can be forced down to
     ≤ 2^n/(2^{n+1}-1) by XY — the hard, currently open direction; this
     approach cross-references `universal-halving-adversary` and
     `dyadic-potential-invariant` for candidate mechanisms and will import
     a certified upper-bound lemma from either if proved.
Key lemmas (claim + mechanism):
  - Greedy-optimality — because an exchange/coupling argument shows no
    deviation from "take current max" can strictly help either player.
  - Position-irrelevance — splitting is a length-only local operation.
  - Dominance inequality 2^n > 2^n - 1 — standard geometric series
    identity; needs care in step 4 for the case XY splits the top piece
    itself (not just the smaller ones).
Open gaps: greedy lemma not yet written up rigorously (tie-handling);
step 4's "XY splits the top piece" sub-case unresolved; step 5 (universal
upper bound) is the central open gap of the whole problem.
Cases to cover: n=0 base case; split-top-piece vs split-smaller-piece in
step 4; LB using fewer than n points in step 5.
Watch out for: do not let spatial ordering of LB's pieces (e.g.
"bit-reversal" vs "increasing" orderings reported by different explorers)
be treated as materially different constructions — by position-irrelevance
they are the same multiset and hence the same value.

universal-halving-adversary: new
Target: same c(n) = 2^n/(2^{n+1}-1), but this approach is dedicated
entirely to the hard upper-bound direction (LB's lower bound is imported
from `greedy-reduction-geometric` once certified).
Technique: Explicit constructive adversary algorithm ("leveling":
neutralize the current largest piece by shaving off exactly the
second-largest, creating a tie-neutral pair, rather than blind bisection)
+ strong induction on piece count. Chosen specifically because blind
bisection is a RECORDED DEAD END (explorer verified it under-forces LB to
0.6 instead of 8/15 at n=3).
Skeleton:
  1. Import greedy-optimality lemma (LB's value = odd-rank sum).
  2. Define XY's leveling algorithm precisely: given sorted pieces
     q_1≥q_2≥..., split q_1 into (q_2, q_1-q_2) creating a tie-neutral pair,
     OR bisect q_1, depending on a threshold rule (generalizing the n=1
     bisect-vs-shave crossover at x=1/3).
  3. Tie-neutrality lemma: equal-length pieces occupy consecutive sort
     ranks, hence always split exactly 1–1 regardless of context.
  4. Charging induction on piece count: each neutralized pair contributes
     exactly half its length to LB; recurse on the residual with one fewer
     XY move; show total ≤ 2^n/(2^{n+1}-1).
  5. Sanity check against the n=3 numeric counterexample from the
     computation explorer to confirm the leveling algorithm (not blind
     bisection) reproduces 8/15.
Key lemmas (claim + mechanism):
  - Tie-neutrality — consecutive ranks in an alternating claim always
    alternate owners.
  - Leveling dominance (UNPROVEN CRUX) — shaving off exactly q_2 from q_1
    is the safest single split for XY, converting the most dangerous
    asymmetry into a neutral pair plus a strictly smaller residual.
Open gaps: the exact threshold rule for level-vs-bisect at k≥3 pieces is
undetermined; step 4's induction is only sketched; budget correctness
(never needs >n splits) unverified.
Cases to cover: LB uses <n+1 pieces; base case k=1; case q_1=q_2 (no room
to level, must bisect).
Watch out for: this approach proves ONLY the upper bound — must not be
marked `solved` standalone; Status stays `partial` until paired with a
certified lower bound from another approach.

dyadic-potential-invariant: new
Target: same c(n) = 2^n/(2^{n+1}-1), proved via a single running
potential/credit invariant tracked through the ENTIRE two-phase game,
rather than through the two-lemma (greedy + minimax) decomposition used by
the other approaches. This is the framing directly requested per dispatch:
adapt aimo-0117's dyadic-dominance crux move as the *central* technique,
not just a construction hint.
Technique: Potential-function / monovariant argument (KB: "Invariants &
monovariants"), borrowing aimo-0117's "top value strictly exceeds sum of
rest" mechanism but applied dynamically, split-by-split, rather than
statically to one fixed partition.
Skeleton:
  1. Define potential Φ = LB's claimed total + Σ credit weights w(p) over
     unclaimed pieces, seeded to equal T = 2^n/(2^{n+1}-1) at the start of
     XY's marking phase under LB's optimal construction.
  2. Local split-monotonicity claim: splitting any single piece cannot
     decrease Φ from LB's perspective — the crux inequality, analogous to
     but distinct from (and harder than) the static dominance identity.
  3. LB's marking-phase bound: geometric construction seeds Φ ≥ T.
  4. XY's marking phase (≤n splits) cannot drive Φ below T — by induction
     on remaining XY moves using step 2.
  5. Claiming phase realizes Φ: LB's actual greedy claim total matches the
     credit-weight sum exactly (re-deriving the odd-rank fact as a
     byproduct, not a prerequisite).
Key lemmas (claim + mechanism):
  - Local split monotonicity (UNPROVEN CRUX, entirely open) — the dyadic
    credit weights are designed so no single split can shift more value
    past LB than the credits absorb.
  - Dominance identity 2^n > 2^n-1 — seeds the initial potential.
Open gaps: precise definition of the rank-potential ρ(p)/credit w(p) not
yet pinned down; step 2 is completely open and may be false as stated;
step 5 risks collapsing back into a repackaging of the
`greedy-reduction-geometric` upper-bound gap — builder must watch for and
report this collapse rather than force it through.
Cases to cover: n=0,1 calibration; split creating two same-side vs
straddling pieces (likely the crux case split for step 2).
Watch out for: riskiest approach in the field — if no clean per-split
local monotonicity exists (the true invariant may be inherently global),
downgrade/abandon within 1-2 rounds rather than pursue indefinitely.

self-similar-induction-on-n: new
Target: same c(n) = 2^n/(2^{n+1}-1), proved by a direct
exchange-argument/induction-on-n over the WHOLE game (marking + claiming
together) — this is the framing requested per dispatch that avoids going
through the general greedy-claiming lemma as a free-standing citable fact;
whatever local alternating-claim facts are needed are proved in situ.
Technique: Strong induction on n via strategy-stealing: LB reserves one
piece and recurses its remaining n-1 points on the residual stick,
generalized to a two-parameter recursion c(m,k) (LB has m points, XY has
k≤m) because XY is free to spend part of its budget attacking the reserved
piece rather than committing fully to the residual.
Skeleton:
  1. Base case n=0: c(0)=1=2^0/(2^1-1). ✓
  2. Inductive hypothesis: c(n-1,·) known for all k ≤ n-1.
  3. LB reserves top piece of length t, plays certified (n-1)-strategy on
     residual (1-t).
  4. Model XY's allocation: XY spends j∈{0,...,n} points on the reserved
     piece and n-j on the residual; LB's total = (odd-rank share of the
     split reserved piece) + (1-t)·c(n-1, n-j).
  5. Solve the resulting minimax over t and j; verify it reduces to
     2^n/(2^{n+1}-1) at the diagonal c(n,n).
Key lemmas (claim + mechanism):
  - Two-parameter generalization is necessary — because the naive
    single-parameter recursion c(n) = t + c(n-1)(1-t) was checked and
    REFUTED (does not match n=1 data: gives 1 instead of 2/3) since it
    wrongly assumes XY commits its full budget to the residual.
  - Reserved-piece sub-game for small j — explicit small computations
    (essentially redoing the n=0,1,2 numeric base cases symbolically).
Open gaps: the two-parameter recursion c(m,k) is not yet defined or solved
— this is the entire content of the approach; even if solved, must verify
it actually yields 2^n/(2^{n+1}-1) at k=m=n; optimal reserved length t may
itself depend on k, adding a minimax-within-minimax layer.
Cases to cover: every XY allocation j from 0 to n; boundary case j=n (XY
spends everything on the reserved piece).
Watch out for: do NOT silently fall back to the refuted single-parameter
recursion (LB reserves and residual is independently played to c(n-1)) —
that specific simplification is a recorded dead end for this approach.
