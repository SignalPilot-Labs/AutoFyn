## Status
unsolved

## Approaches tried
(none yet — new approach, round 1)

## Current best
Shared background (f(f(y))=2f(y)-y, f(y)>=y, injectivity) as in the other approaches.
This approach's distinct idea is a genuine extremal-principle finish (sup/inf of S,
Pigeonhole/extremal-principle KB entry) rather than a subdivision or monotonicity
argument — outlined below, open gap flagged.

## Full proof
(not yet — partial)

---

## Outline (for the builder)

Target: same as the other approaches — determine all f: R_{>0}->R_{>0} satisfying the
sandwich; claim f(x)=x+c, c>=0.

Technique: **extremal principle (sup/inf argument)**, KB "Pigeonhole / extremal
principle: for existence, take the maximal or minimal ... configuration and derive a
contradiction from extremality." Distinct mechanism: rather than bounding
S(x)-S(y) directly for arbitrary x,y (as in quadratic-difference-chaining) or using
order-preservation of orbits (as in monotonicity-first), fix attention on the *extremal
value* of S over all of R_{>0} and show that extremality itself is contradicted unless
S is constant everywhere.

Skeleton:
1. Shared background as in quadratic-difference-chaining steps 1-4: (A),(B),
   f(f(y))=2f(y)-y, f(y)>=y (so S(x):=f(x)-x >= 0 for all x), injectivity.
2. **Import the (KEY) two-sided bound** (certified once by quadratic-difference-
   chaining's builder, reusable per CLAUDE.md's lemma-cache rule; if not yet certified,
   this approach's builder must re-derive it — it is a 6-line algebra computation, see
   quadratic-difference-chaining step 5):
     -(x-y)^2/(4f(x)) <= S(x)-S(y) <= (x-y)^2/(4f(y))   for all x,y>0.     (KEY)
3. **Extremal argument on a bounded sub-range.** Fix any closed bounded interval
   I=[p,q] subset R_{>0} with 0<p<q. Since S restricted to I need not a priori be
   continuous, use the INFIMUM (not minimum) m_I := inf_{x in I} S(x) >= 0 and pick a
   sequence x_n in I with S(x_n) -> m_I. For any fixed y in I, apply (KEY) with
   x=x_n: S(x_n)-S(y) <= (x_n-y)^2/(4f(y)) <= (q-p)^2/(4p) (bounded, since f(y)>=y>=p
   on I). Take n->infinity: m_I - S(y) <= (q-p)^2/(4p) for ALL y in I — this alone is
   not yet strong enough (doesn't force equality); the extremal principle needs
   *shrinking* the interval, not just using one fixed I. Refine: for ANY two points
   x,y in R_{>0}, apply step 3's argument to the interval I=[min(x,y),max(x,y)] and
   iterate: since (KEY) applied to x_n (near the infimum on I) and a SECOND sequence
   y_n in I approaching the supremum M_I := sup_{x in I} S(x) gives, by the same
   token, M_I - m_I <= lim (x_n-y_n)^2/(4 f(one of them)); since x_n,y_n both range
   over the *same fixed* bounded interval I, (x_n-y_n)^2 does NOT vanish in general
   (they need not converge to the same point) — so this naive extremal comparison on
   a fixed interval does not immediately force M_I=m_I. **This is the actual open gap**:
   the extremal argument must be sharpened, most likely by choosing I to shrink to a
   single point (I_k = [x-1/k, x+1/k] for fixed x, k->infinity) so that BOTH the near-
   inf and near-sup sequences are forced to lie within I_k, making (x_n-y_n)^2 -> 0
   automatically as k->infinity (since diam(I_k) -> 0), which would show sup and inf
   of S *on I_k* converge to the same value as k->infinity, i.e. S is continuous at
   every point with that common value equal to S(x) itself (a form of "S has no jump
   discontinuities," which combined with (KEY) applied globally, not just locally,
   should then pin S(x) = S(y) for every x,y by a further global comparison). The
   builder must carry this refinement through rigorously — it is essentially a
   restatement of the same subdivision idea as quadratic-difference-chaining but
   phrased as local-continuity-forces-global-constancy rather than direct telescoping;
   if it does not simplify beyond quadratic-difference-chaining's already-complete
   subdivision argument, this approach should explicitly defer to / copy that
   approach's step 6 rather than reinvent a weaker version.
4. **Necessity conclusion** (once S shown constant): f(x)=x+c, c>=0.
5. **Sufficiency**: identical (x-y-c)^2>=0 identity check as in the other approaches.

Key lemmas (claim + mechanism):
  - (KEY) imported/re-derived as above.
  - S is locally constant near every point (open gap) — because shrinking the
    comparison interval to a point forces the (x_n-y_n)^2 term in (KEY) to vanish,
    squeezing the local sup and inf of S together.
  - Global constancy from local constancy — because R_{>0} is connected (an interval),
    so a function that is locally constant everywhere on a connected domain is
    globally constant (topological fact, standard, cite as "connectedness argument").

Open gaps:
  - Step 3's shrinking-interval refinement is sketched but not completed rigorously —
    this is the single largest gap in this approach. The builder should attempt it,
    but should recognize this approach is likely to converge to (or be strictly
    weaker/more convoluted than) quadratic-difference-chaining's direct subdivision
    argument; if so, prefer marking this approach RETHINK and consolidating effort on
    quadratic-difference-chaining rather than duplicating the same result via a more
    complicated route.

Cases to cover: none.

Watch out for:
  - The infimum m_I may not be attained (S need not be continuous a priori) — always
    argue via sequences approaching the inf/sup, never assume a minimizer exists.
  - Do not conflate "S locally constant" with "S continuous" — local constancy is the
    stronger, directly useful fact here; don't under-claim by only proving continuity.
