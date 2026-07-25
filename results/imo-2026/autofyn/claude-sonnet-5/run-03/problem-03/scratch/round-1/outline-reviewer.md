# Outline review — imo-2026-03, round 1

Problem: stick-division game; determine c(n) such that Liu Bang (LB, marks
≤n points, moves first at claim time) can guarantee ≥ c(n) against any
Xiang Yu (XY, marks ≤n points) response. Claimed answer across all four
approaches: **c(n) = 2^n/(2^{n+1}-1)**.

## Sanity checks performed

1. **n=1 numeric verification (independent of the outline).** Brute-force
   grid search over LB's single cut point `a` and XY's best single response
   split, using the "greedy claim = sum of odd-ranked pieces" rule, gives
   best `a ≈ 0.332` (matches LB's claimed 1/3 construction) and value
   `≈ 0.6670`, matching `2/3 = 2^1/(2^2-1)` to 3 decimal places. This
   independently corroborates both the closed-form target and the
   greedy-optimality lemma that all four approaches rely on (explicitly or
   implicitly).
2. **n=3 numeric stress test of the "leveling" adversary
   (`universal-halving-adversary`, step 2).** I implemented XY's proposed
   algorithm exactly as specified — repeatedly split the current largest
   piece `q_1` into `(q_2, q_1-q_2)` (or bisect if tied) — against LB's
   geometric construction `(1,2,4,8)/15`. Result: **0.6**, identical to the
   already-recorded blind-bisection dead end, NOT the target `8/15 ≈
   0.5333`. A separate randomized search over all ways to spend 3 cuts
   found the true minimizing response: **splitting the top piece (8/15)
   alone, three times, into 4 sub-pieces** (never touching the smaller
   pieces, never "pairing" with `q_2`), achieving exactly `8/15`. So the
   specific "leveling" mechanism as written in the outline is **numerically
   refuted** — it reproduces the same failure as blind bisection, not a
   fix for it. This is a concrete, checkable fact for the builder, not a
   vague warning.

## Per-approach verdicts

### greedy-reduction-geometric — APPROVE
Sound two-part reduction: greedy-optimality (alternating claim over a fixed
multiset = sum of odd-ranked pieces) is the standard, provable-by-exchange
fact for this class of "claim-any-remaining-item" games, and
position-irrelevance (only the length-multiset matters) is immediate from
the rules. Both lemmas were exercised successfully in my n=1 check.
Lower-bound construction (1,2,4,...,2^n) is right and the "top piece
dominates the sum of the rest" mechanism (`2^n > 2^n-1`) is a correct,
standard identity — the only flagged subtlety (XY splitting the top piece
itself) is real and correctly flagged as unresolved. Step 5 (upper bound
for *arbitrary* LB partitions) is legitimately the hard direction of the
whole problem and is honestly marked open rather than hand-waved — this is
acceptable for a round-1 outline. No fatal flaw. This is the field's
backbone: the other three approaches all lean on its lemmas or its target
formula.
Issues to close while building: (1) write up the greedy-optimality
exchange argument rigorously, including the tie-handling case explicitly
(does the *value* stay invariant when two pieces tie, not just the
split?); (2) the "XY splits the top piece" sub-case in step 4 needs an
actual argument, not a deferral; (3) once the greedy-optimality and
lower-bound lemmas are proved, certify them into `lemmas/` so
`universal-halving-adversary` (and any future approach) can import them
without re-deriving — this is the sanctioned way to share content across
approaches without collapsing them into "one proof split into pieces."

### universal-halving-adversary — CHANGES REQUESTED
Right general target (attack the dominant piece rather than blind
bisection, which is a recorded dead end) but the *specific* mechanism
proposed (leveling: pair `q_1` with `q_2`, recurse) is now numerically
refuted at n=3 (see check #2 above) — it silently degenerates into the
same failure mode as blind bisection once the pieces become tied at
`q_1=q_2` after one level-off, and never reaches `8/15`. My search shows
the actual winning move is to keep splitting the *same* top piece multiple
times (self-similarly) rather than pairing it off with the runner-up and
moving on. Builder must not proceed with the leveling algorithm as
literally specified; redesign the adversary response around "recursively
subdivide the currently-dominant piece" (closer in spirit to a scaled copy
of the *same* construction LB used — worth explicitly comparing against
`self-similar-induction-on-n`'s framing, since that approach's recursive
structure may supply the right shape for this adversary move). Tie-
neutrality lemma (step 3) is correct and reusable regardless. On
structure: this approach imports its lower bound from
`greedy-reduction-geometric` rather than proving it independently — that
is acceptable *only* via the certified `lemmas/` cache (once
`greedy-reduction-geometric`'s lower-bound lemma is reviewer-certified),
not as a standing cross-file assumption; until then this file's own
Status must stay `partial` even if the upper-bound half is completed, as
already noted.
Issues to close: (1) discard/redesign the leveling mechanism per the
n=3 refutation above; (2) verify any replacement mechanism against the
same n=3 numeric target (8/15) before attempting a general induction; (3)
keep Status `partial` pending the imported lower-bound lemma.

### dyadic-potential-invariant — CHANGES REQUESTED
Legitimate distinct framing (single potential/monovariant over the whole
game, KB: "Invariants & monovariants") rather than a variant of the
multiset-reduction technique — good for diversity. But it is the least
concrete approach in the field: the credit weight `w(p)` / rank-potential
`ρ(p)` are not defined precisely enough to state a checkable inequality,
and the central claim (local split-monotonicity) is flagged by the
outliner itself as possibly false. This is acceptable to keep in the
population (round 1, genuinely different route) but not yet in strong
shape to build efficiently. The outline itself already flags the real
risk: step 5 (credits are achieved) may force this to reduce back to
`greedy-reduction-geometric`'s same odd-rank characterization, at which
point it stops being an independent route and should be reported as such
rather than forced through.
Issues to close: (1) pin down `w(p)`/`ρ(p)` concretely for n=0,1 first
(matching my n=1 numeric result, `c(1)=2/3` at split `1/3`) before
attempting the general local-monotonicity claim; (2) explicitly test the
local-monotonicity inequality on the n=1 case (does a single split of
either piece really never decrease Φ?) as a first checkable step; (3) if
no clean local (per-split) invariant survives this concrete check, report
the collapse rather than continue — per the outline's own stated
abandon-condition.

### self-similar-induction-on-n — APPROVE
Genuinely different top-level route: induction on the point-budget n over
the *whole* game rather than a static multiset reduction. The naive
single-parameter recursion was correctly checked and refuted (gives 1
instead of 2/3 at n=1 — consistent with my independent n=1 computation
showing 2/3 is correct), and the fix (two-parameter recursion `c(m,k)`
tracking XY's allocation between the reserved piece and the residual) is
a sound response to a real subtlety, not hand-waving. The entire content
of the approach (solving `c(m,k)`) is still open, which is fine for round
1 — it's clearly flagged as the whole remaining gap, not buried.
Issues to close: (1) define `c(m,k)` precisely (LB has m points, XY has
k≤m) and verify small cases (m=k=1, m=1,k=0) against my n=1 numeric
target before attempting the general minimax; (2) confirm whether the
optimal reserved-piece length `t` depends on `k` as flagged; (3) do not
regress to the refuted single-parameter recursion.

## Diversity assessment

The four approaches are reasonably diverse in framing, not just technique
variants of one reduction: (1) is a static multiset-minimax reduction, (2)
is a dedicated explicit-algorithm attack on the upper-bound half of (1),
(3) is a global potential/monovariant argument avoiding the multiset
reduction entirely, (4) is an induction-on-n / strategy-stealing argument
also avoiding the multiset reduction as a free-standing lemma. (1) and (2)
share a dependency (2 imports 1's lower bound) but this is via the
sanctioned `lemmas/` cache mechanism, not a hidden fragment-split, and (2)
targets a different technical direction (universal adversary vs.
construction) than (1)'s own attempted step 5. No approach here repeats a
dead end already recorded in `current.md` (there are none yet — first
round). The one real risk flagged: (2) and (3) both ultimately reduce to
finding *some* adversary/monotonicity mechanism for the same upper-bound
gap that (1) also attempts in step 5 — if all three stall on that shared
wall, next round's outliner should be pushed toward a genuinely different
upper-bound mechanism (e.g., the self-similar recursive-subdivision idea
surfaced by my n=3 search) rather than more variants of "sort and attack
the largest piece."

## Ranking

Registered all four approaches at cold-start Elo and ranked via
`update_ranking` using the evidence above: `greedy-reduction-geometric`
and `self-similar-induction-on-n` win over both `universal-halving-
adversary` (whose core mechanism is now numerically refuted) and
`dyadic-potential-invariant` (least concrete); `universal-halving-
adversary` still edges `dyadic-potential-invariant` for having a concrete,
checkable (if currently wrong) algorithm rather than an undefined
potential. Resulting order: `greedy-reduction-geometric` (1531) ≈
`self-similar-induction-on-n` (1530) > `universal-halving-adversary`
(1486) > `dyadic-potential-invariant` (1453).

## Build set

Build the top three this round. `dyadic-potential-invariant` is held back
(registered, ranked, not built) until its potential/weights are made
concrete — pursuing it now risks a wasted round on an undefined object;
its builder slot is better spent letting the outliner (or the builder of
one of the other three) sharpen the credit-weight definition first.
`universal-halving-adversary`'s builder should redesign the adversary
mechanism per the n=3 refutation above rather than attempt to patch the
leveling algorithm.

build set: greedy-reduction-geometric, self-similar-induction-on-n, universal-halving-adversary
