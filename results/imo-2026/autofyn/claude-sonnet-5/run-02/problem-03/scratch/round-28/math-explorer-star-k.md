## imo-2026-03 — lens: (star_k), k>=3, the shared bottleneck

### What (star_k) precisely claims
Definition (rank-pigeonhole-budget.md, §7.11, line ~1925-1933; consistent with
greedy-halving-adversary's own use, e.g. Proposition 13's `(star_{n-1})`):
for the **unit ratio-2 ladder** of length k+1, `pi = (pi_1,...,pi_{k+1})`,
`pi_i = 2 pi_{i+1}`, and **every** legal Xiang-Yu response `U` using `<=k`
cuts distributed **in any pattern whatsoever** across all k+1 elements
(no restriction to cutting only pi_1; the fully general one-level statement):
```
(star_k):   A(U) >= pi_{k+1}
```
where A is the certified alternating-sum-of-sorted-values functional
(`Phi(S) = (Total(S)+A(S))/2`, Lemma 2). Via `sharp-dominant-removal-identity`
style scaling this is equivalent to `Phi(U) >= c(k)` for the *specific*
k-ladder marking — i.e. **(star_k) is exactly the achievability
(lower-bound) half of c(k), restricted to the ladder construction itself**
(not a general-marking claim — that's the separate, already-closed-at-n=3
upper bound front). rank-pigeonhole-budget's §7.11 Index-Chain Identity
*proves* (not just observes) `MinFloor(l) = (star_{l-1})` via an explicit
rescaling bijection (any ratio-2 tail of length k+1 is `lambda * pi` for a
unique `lambda>0`, and legal-refinement + A are both scale-equivariant).

**Why k=1,2 are closed, k>=3 open (precise reason, not vague):** `(star_1)`
is `c(1)=2/3`'s lower bound, trivial (n=1, one possible cut). `(star_2)` is
exactly `c(2)=4/7`'s lower bound, closed by `smoothing-compactness-
certificate` rounds 1-2 via an **exhaustive finite case analysis** (10
legal-cut-distribution cases for n=2, each resolved by an explicit
computation/inequality, zero numerics load-bearing). `(star_3),(star_4),...`
have **no analogous exhaustive closure on file** — every approach that
touches them either (a) uses them as a hypothesis further up an induction
(Theorem 13, 24, 34, 36b, etc. throughout greedy-halving-adversary.md), or
(b) tried to *reduce* them to something smaller and failed (see Dead ends).
Nobody has yet directly attempted the same brute exhaustive-vertex-
enumeration technique that closed `(star_2)`, scaled up to `(star_3)`.

### Distinct openings (attacks not yet tried, and why they're new)

1. **Direct finite-shape / vertex enumeration on (star_3) itself, reusing
   the exact machinery that closed MaxCeil(3)/MaxCeil(4).** `(star_3)` =
   `MinFloor(4)`: a 4-piece ratio-2 ladder, budget <=3 cuts. This is the
   *same size class* of object as `MaxCeil(3)`/`MaxCeil(4)`
   (rank-pigeonhole-budget §7.12-13), which **were** closed by an
   exhaustive 5-shape cut-distribution enumeration (each shape resolved
   using `sharp-dominant-removal-identity` and other already-certified
   general facts) — but `MinFloor(4)` itself has *not* been attempted with
   this technique (the file only handles `MinFloor(2)`, `MinFloor(3)` via
   citation of the already-closed `c(1)`, `c(2)` theorems; §7.14's
   sigma2-untouched theorem is about MaxCeil, the dual quantity). By the
   Vertex-Minimum Theorem (certified, `lemmas/vertex-minimum-theorem.md`),
   the minimizer of `A(U)` is attained at a rank-tie/zero-fragment LP
   vertex, so this is a genuinely *finite* combinatorial object — I
   verified computationally (below) that with budget=3 on 4 pieces there
   are only 20 cut-distribution *shapes* (compositions of 3 into <=4
   parts across the 4 original pieces), a search space of the same order
   MaxCeil(3)/(4) already handled by hand. This is NOT a rescaling attempt
   (round 23's two dead-end proofs concern reducing `(star_k)` to a
   *smaller* self-similar instance of itself; direct exhaustive
   enumeration at the base size is a different, un-refuted route) and is
   NOT what §7.15's Necessity Theorem forecloses (that theorem shows the
   existing *elementary-facts toolbox cannot avoid* needing `(star_k)` —
   it does not say `(star_k)` itself can't be attacked directly by
   exhaustion).

2. **Strong induction on k with a genuinely different invariant: attack
   k=3 as a stepping stone with the specific tools already proven for the
   general-n front (Theorems 32-41) rather than through the MaxCeil/
   MinFloor abstraction.** Concretely: `(star_3)` is precisely "prove
   `L(3)` [the full undecomposed lower bound for the 3-ladder]." Round 23's
   `greedy-halving-adversary` bundled audit already traced that its own
   Theorems 33-36 chain is genuinely unconditional at n<=4 (bottoms out at
   `(star_0)/(star_1)`, both trivial) and ran a fresh 200k-trial stress
   test of the *undecomposed* target `L(3)`, `L(4)` with **zero
   violations, minimum margin observed exactly 0 at both** — i.e. the
   *pieces* built for the general induction, when specialized to n=3,
   already numerically cover it; what's missing is converting "the pieces
   I already have, applied at n=3" into one assembled, gap-free proof
   document — an assembly task, not a new-technique task. This is
   different from opening #1 (fresh brute enumeration) — it's "finish
   stitching what's already proved."

3. **LP/duality certificate specific to (star_3).** `lp-duality-
   certificate`'s whole apparatus (Farkas-style nonnegative-combination
   certificates, chamber families) was built for the *upper*-bound
   direction (`c(n)<=...`) but the same certificate machinery is directly
   applicable to a *lower*-bound target once dualized (minimize `A(U)`
   subject to legal-response constraints is itself an LP once the
   sorted-order case is fixed — this is exactly the Vertex-Minimum
   Theorem's own proof mechanism, already certified). No approach file
   has assembled an explicit Farkas certificate *for the lower-bound
   `(star_3)` target specifically* (all existing certificates target the
   n=3 upper bound, which is a different polytope/objective). This is a
   real gap in the population, not previously attempted for `(star_k)`.

### Cheap-kill candidates
- **Shape-count pigeonhole:** for `(star_k)`, budget k cuts across k+1
  pieces gives only `C(2k, k)` compositions-with-multiplicity-style
  shapes (exact count for k=3 verified computationally: 20 shapes) —
  small enough to enumerate exhaustively by computer first, then prove
  each shape's worst sub-vertex by hand only for the shapes that are
  numerically close to tight (most shapes tested were NOT tight — see
  numeric notes below — so the case split needed is much smaller than
  "all 20 shapes need a hard proof").
- Reuse **`sharp-dominant-removal-identity`**, **`triangle-bound-for-A`**,
  and **`max-domination-lemma`** as cheap first-pass eliminators per shape
  before invoking anything heavier — this is exactly the pattern that
  closed MaxCeil(3)/(4) fast.

### Knowledge-base entries to use
No `knowledge_base.md` entries beyond what's already cited throughout this
project were newly identified as relevant to `(star_k)` specifically (this
matches the standing project rule that the KB and crux corpus have no
direct analog for this problem overall, round 1).

### Analogous past problems (cruxes)
Queried `past_crux_moves_database.json` filtered to `domain=combinatorics`,
subtopics `games-and-strategy`, `extremal-principle`, `pigeonhole`,
`processes-and-algorithms` for alternating/rank/tie/budget/adversary/greedy
techniques (per dispatch). Closest surface matches (`aimo-0558`, IMO2022-P3
bounded-gap max-excess selection with alternating-block charging;
`aimo-0340`, pearl-string halving/greedy-cut process) were read in full and
are **not genuinely analogous** — `aimo-0558`'s greedy-charging argument
operates on a totally different combinatorial object (a fixed +-1 sequence,
no adversarial two-stage marking/claiming), and `aimo-0340`'s halving
process has no claiming-alternation or Phi-style min-max target. No entry
in the corpus resembles the specific structure here (fixed superincreasing
marking + adversarial refinement + alternating greedy-claim payoff). This
reconfirms the standing project finding (round 1, run_state Rules) that the
corpus has no load-bearing analog for this problem — do not spend further
budget searching it for `(star_k)` specifically.

### Prior progress
- `(star_1)`, `(star_2)` fully certified (cited, not to be re-derived).
- `(star_3)`: **not directly attempted** as its own target by any approach
  file to date — it only appears as a hypothesis consumed by higher-level
  theorems (Theorem 13/24/34/36b/37, MaxCeil's Necessity Theorem). The
  closest existing work is greedy-halving-adversary's round-23 "bundled
  audit," which is an honest partial numeric stress-test, not a proof
  (explicitly flagged as such in the file).
- §7.14 (sigma2-Untouched Closure Theorem, general m, unconditional, no
  `(star_k)` input) and §7.15 (Necessity Theorem, proves the *complementary*
  sigma2-touched top-cut residual for `MaxCeil(m>=5)` structurally requires
  `(star_{m-2})`) are both certified and directly relevant context but do
  not themselves attack `(star_k)`.

### Dead ends (do not retry)
- **Self-similar rescaling of `(star_k)` to a smaller `(star_m)` instance**
  — confirmed dead twice independently (round 23): (a) `proposition-39-
  mass-conservation-obstruction.md` proves *no* fixed embedding `{c}∪S`
  into a smaller ladder `L_k` can work for an open interval of `c` (mass-
  conservation/injectivity argument, general m, no gaps); (b) the general
  `h(m)`-as-`(star_k)`-corollary route is separately refuted. Do not
  propose "reduce `(star_3)` to `(star_2)` via a rescaling trick" — this
  exact idea has been tried and killed twice.
- Per dispatch: do not propose another rescaling/reduction variant of any
  kind for `(star_k)` k>=3 — this is the 3rd time it would be attempted.

### Small-case / intuition notes (numeric, exact-Fraction, NOT proofs)
Independently verified (fresh script, not reusing any builder's prior
script) with the exact 3-ladder `p=(8/15,4/15,2/15,1/15)`, budget 3 cuts:
- 200,000-trial random-response search over arbitrary cut placement found
  minimum `A(U)` = **exactly `1/15` = f(3)** (matches target exactly, zero
  violations) — consistent with round-23's finding. `(star_3)` looks true
  with **zero slack at the extremal vertex** (a genuinely tight boundary
  case, not comfortably-true-with-margin) — any proof will need to nail
  the exact extremal configuration(s), not just a loose bound.
- Enumerating the 20 possible cut-distribution *shapes* `(k1,k2,k3,k4)`,
  `sum=3`, `ki<=3` (script below) and doing 20,000 random trials per shape:
  the exact minimum `1/15` was hit (within float/rational search
  resolution) at shape `(3,0,0,0)` (all 3 cuts on `p1`, tail untouched —
  matches the already-certified `Case (a)`/Proposition-13-family vertex)
  and shape `(2,0,1,0)` (2 cuts on `p1`, 1 cut on `p3`, `p2,p4` untouched).
  Every other shape's random-search minimum stayed **strictly above**
  `1/15` (e.g. shapes touching `p2` heavily, like `(0,3,0,0)`, bottomed out
  around `0.33`-`0.35`, far from tight) — i.e. **most of the 20 shapes are
  not even numerically close to the tight case**, so a hand proof likely
  only needs to carefully handle 2-4 "dangerous" shapes (those touching
  `p1` and/or `p3` with a residual cut) and can dispatch the rest with a
  cheap uniform bound (e.g. `max-domination-lemma`/`triangle-bound-for-A`).
  This conjectured shape-severity ranking is evidence, not proof, and
  should be re-derived exactly (not just numerically) before being relied
  on structurally.
- Scripts used (ad hoc, not committed): `/tmp/star3_search.py`,
  `/tmp/star3_shapes.py` — exact-`Fraction` throughout, no floats in the
  final computation (floats only used to generate random cut positions,
  then converted to bounded-denominator Fractions).
