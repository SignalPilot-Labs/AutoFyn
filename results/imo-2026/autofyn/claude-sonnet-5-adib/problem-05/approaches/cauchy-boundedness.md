## Status
unsolved

## Approaches tried
(none yet — new approach, round 1)

## Current best
Shared background (f(f(y))=2f(y)-y, f(y)>=y, injectivity) established as in the other
approaches. This approach's distinct idea — reformulate the constraint on S:=f(x)-x as
an approximate/bounded additive (Cauchy-type) functional inequality and invoke a
boundedness rigidity theorem — is outlined below but the precise additive inequality is
not yet fully derived; flagged as the open gap.

## Full proof
(not yet — partial)

---

## Outline (for the builder)

Target: same as the other approaches — determine all f: R_{>0}->R_{>0} satisfying the
sandwich; claim f(x)=x+c, c>=0.

Technique: **Cauchy-equation-style rigidity.** Distinct mechanism from both the
subdivision-chaining approach and the monotonicity approach: instead of a direct
quadratic bound or an order argument, show S(x):=f(x)-x satisfies (or can be squeezed
between) an *additive*-type relation on some structured subset of R_{>0} (e.g. along
sums x+y or along rational multiples), then invoke the classical rigidity fact that a
solution to Cauchy's functional equation that is bounded (here: bounded below by 0,
since S>=0) on any interval, or monotone, must be linear — which for an additive
function that is also bounded below everywhere forces it to be the zero function
(constant additive part), pinning S to a genuine constant. This is the "Cauchy +
regularity kills pathological solutions" template (KB "Functional equations: test
special values" generalizes to this rigidity fact; also related to KB "Invariants &
monovariants" since S(f(y))=S(y) is itself an invariance statement).

Skeleton:
1. Shared background: derive (A),(B),(*) f(f(y))=2f(y)-y, f(y)>=y, injectivity exactly
   as in quadratic-difference-chaining steps 1-4.
2. **From (*), define T(x) := S(f(x)) - S(x).** By construction of (*) (see
   quadratic-difference-chaining step 3), T(x)=0 identically along orbits — this
   is NOT yet the additive relation we want; the goal here is different: derive a
   relation between S(x+y)-ish quantities, not just orbit-invariance. The builder
   should look for a substitution that produces S evaluated at a SUM or an average of
   two independent variables (rather than at the composite f(x)). Candidate move:
   substitute x := y + t (t>0 free) into inequality (A) or (B) directly (not via f),
   expand in S(y+t), S(y), and isolate a bound of the shape
     |S(y+t) - S(y) - (something depending on t alone)| <= (error term),
   which if the error term can be shown to vanish as a genuine identity (not just an
   inequality with error) would give an exact or approximate Cauchy relation
   S(y+t) - S(y) = phi(t) for some function phi, from which additivity of phi (via a
   second substitution, e.g. comparing S(y+t1+t2) via two different orders) plus
   S>=0 (boundedness below) forces phi(t)=ct for a constant c, i.e. S itself is
   affine — combined with S>=0 for all x>0 forces the linear coefficient to be 0
   (else S would go negative for large or small x), leaving S constant = c>=0. This
   whole derivation (the exact form of the substitution and whether the error term
   really vanishes or only bounds an inequality — in which case use the KEY quadratic
   bound from quadratic-difference-chaining step 5 instead of a fresh derivation) is
   the OPEN GAP for the builder to carry out concretely, most likely by importing the
   already-derived (KEY) inequality
     -(x-y)^2/(4f(x)) <= S(x)-S(y) <= (x-y)^2/(4f(y))
   (certified in quadratic-difference-chaining, importable per CLAUDE.md's shared-
   lemma-cache rule once that approach's builder proves and the reviewer certifies it)
   and reinterpreting it as: "S restricted to any bounded interval is Lipschitz with
   constant -> 0 as the interval shrinks" i.e. S has vanishing derivative everywhere
   it is differentiable, standard real-analysis rigidity (if S is differentiable, (KEY)
   with y=x+h, h->0 gives (S(x+h)-S(x))/h = O(h) -> 0, so S'(x)=0 for all x, hence S
   is constant on each interval, hence globally constant by connectedness of R_{>0}).
   NOTE: this differentiability route needs S to be assumed differentiable OR upgraded
   to a genuine epsilon-delta argument without differentiability — the subdivision
   argument in quadratic-difference-chaining is the fully rigorous (no smoothness
   assumed) version of this same idea; this approach should be read as an alternative,
   possibly-simpler-if-it-works route via the classical "additive + bounded => linear"
   theorem, but if the additive relation cannot be cleanly extracted, this approach
   should defer to (or explicitly copy) the quadratic-difference-chaining lemma rather
   than force a weaker, calculus-only argument.
3. **Necessity conclusion.** Once S shown constant (c>=0): f(x)=x+c.
4. **Sufficiency.** Same as quadratic-difference-chaining step 8: (x-y-c)^2>=0 identity
   for both (A) and (B) under f(x)=x+c.

Key lemmas (claim + mechanism):
  - S(f(y))=S(y) (orbit invariance) — immediate restatement of (*); free, already
    established.
  - (Conjectural target, open gap) S(y+t)-S(y) is (approximately/exactly) independent
    of y — because a direct substitution x=y+t into (A)/(B), OR reuse of the (KEY)
    quadratic bound in the h->0 regime, should force the y-dependence of the
    difference to vanish; this is the crux the builder must actually carry out.
  - Boundedness rigidity: an additive function phi(t)=S(y+t)-S(y) (independent of y)
    with S>=0 everywhere forces phi linear with slope 0 — because a nonzero-slope
    additive function is unbounded on one side (standard Cauchy-equation fact:
    additive + bounded-below-on-a-ray => linear with the "wrong-sign" slope
    contradicts boundedness), hence S must be constant.

Open gaps:
  - The core derivation in step 2 (extracting a genuine additive relation, exact or in
    the limit, from the original sandwich) is NOT carried out — this is the single
    biggest gap in this approach, bigger than in the other two approaches, because it
    is not guaranteed the additive structure exists cleanly (the (KEY) bound from
    quadratic-difference-chaining is genuinely quadratic in (x-y), not linear — an
    additive Cauchy relation may not be the right structural fit at all). The builder
    should attempt it for at most one focused pass; if it does not yield a clean
    additive relation quickly, this approach should be marked RETHINK/merge into
    quadratic-difference-chaining rather than force it.

Cases to cover: none.

Watch out for:
  - Do not assume S is differentiable to shortcut the argument (the "S'(x)=0"
    heuristic in step 2 is illustrative only, not a valid final proof step without
    justifying differentiability, which is not given) — a rigorous finish must either
    find genuine exact additivity or fall back to the subdivision (epsilon-delta / no
    smoothness) argument from quadratic-difference-chaining.
