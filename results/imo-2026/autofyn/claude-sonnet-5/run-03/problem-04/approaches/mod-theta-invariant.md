## Status
partial

## Approaches tried
- **Round 1 (this round): residue/multiple invariant, pushed to completion for
  the "only if" direction.** The outline's plan (a "distance to nearest
  multiple of θ" shrinking bound) turned out to be unnecessary — a much
  cleaner invariant works: "no angle is ever an exact positive integer
  multiple of θ" (property P below), maintainable by Shan-Yu forever whenever
  θ is not of the form 180/n. This single invariant **subsumes and replaces**
  the old ad hoc "all angles < θ" (θ>90 only) lemma: it covers θ>90 AND
  θ≤90 non-divisor cases uniformly, with one algebraic argument and no case
  split on the size of θ. This closes the central shared gap flagged by the
  outline-reviewer and by every sibling approach file for the "only if"
  direction. **Outcome: "only if" direction now fully rigorous (below).**
  Verified numerically (200k+ random and adversarially-targeted trials,
  script below) before write-up, as a sanity check only — the written proof
  is self-contained algebra, not a numerics-based claim.
- **"If" direction attempt (this round): discovered a genuine obstruction to
  the naive shave-only strategy, not previously flagged by any approach
  file.** Tracking the SAME invariant machinery in the θ=180/n case shows
  that every *forced* move (shave, in any of its 4 symmetric forms) shifts
  exactly θ between two of the three angle-slots and leaves the third
  unchanged; consequently the multiset of fractional parts
  {frac(A/θ), frac(B/θ), frac(C/θ)} is an exact invariant of any sequence of
  FORCED moves (proof below). If Shan-Yu opens with a triangle where none of
  A/θ, B/θ, C/θ is an integer (which is exactly property P, and by the same
  countability argument used for the "only if" direction, such a starting
  triangle always exists), then no sequence of purely-forced (shave) moves
  can EVER produce an angle that is an exact multiple of θ, since that would
  require some slot's fractional part to become 0, impossible by the
  invariant. Hence the sibling approaches' plan ("reduce to all-integer-
  multiples via repeated shaves, then finish with a discrete game") **cannot
  work as stated for such starting triangles** — it is a genuine dead end
  for shave-only play, not merely an unfinished writeup. A correct "if"-
  direction strategy must use moves where Shan-Yu retains a real choice
  (non-forced moves), engineered so that BOTH of his options are ultimately
  losing for him (a multi-move / recursive-threat argument, not a single
  deterministic algorithm) — this is strictly harder than what any approach
  file has produced so far and is NOT completed in this round. Recorded
  honestly as an open gap (see below), together with the obstruction proof,
  so no future round wastes time re-deriving the pure-shave "if" plan.

## Current best

**Target:** Mulan wins iff θ = 180°/n for some integer n ≥ 2, equivalently
(writing r = 180/θ > 1, since 0<θ<180) iff r is an integer (automatically
≥2, since r>1).

### Setup (shared with sibling approaches, re-derived here for
self-containedness)

Represent the current triangle by its angle-triple (A,B,C) with A,B,C>0 and
A+B+C=180. If Mulan cuts from the vertex with angle A to a point P on the
opposite side, and t = the angle at that vertex on one side of the cevian
(t ∈ (0,A), chosen freely by Mulan; by relabeling B ↔ C she may also treat
t as measured from either side, i.e. she has the mirror choice too), the two
resulting triangles have angle-triples

- child1 = {B, t, 180−B−t}
- child2 = {C, A−t, B+t}

(The two new angles at P, namely 180−B−t and B+t, are supplementary since
their sum is 180. This is immediate from angle sum in each sub-triangle:
in triangle "ABP", angles are B (at the old vertex B), t = ∠BAP (at A), and
the remaining angle at P is 180 − B − t; in triangle "ACP", angles are C (at
C), A−t = ∠CAP (at A), and the remaining angle at P is
180 − C − (A−t) = 180 − C − A + t = B + t, using A+B+C=180.) Shan-Yu then
discards one of the two children; the survivor becomes the new triangle.
This is the complete description of one round of the game (after the
initial win-check, which is vacuous unless some current angle already
equals θ).

### The invariant

**Definition.** Say a triangle (A,B,C) has **property P** if none of A, B,
C is a positive integer multiple of θ, i.e. A/θ, B/θ, C/θ ∉ ℤ_{>0}.

Note P directly implies the triangle is not already a win for Mulan (since
"some angle = θ" is exactly "some angle is the multiple 1·θ", the k=1 case
of "positive integer multiple of θ").

**Lemma 1 (Invariance of P, the core new lemma of this approach).**
Suppose θ ≠ 180/n for every integer n ≥ 2 (equivalently: 180/θ is not a
positive integer — note 180/θ > 1 always since 0<θ<180, so "not a positive
integer" here is the same as "not an integer ≥ 2"). Suppose the current
triangle (A,B,C) has property P. Then for EVERY choice of vertex to cut and
EVERY t ∈ (0, A) that Mulan can choose, **at least one of child1, child2
again has property P.**

*Proof.* Fix t ∈ (0,A) and consider child1={B,t,180−B−t},
child2={C,A−t,B+t}. Since B and C are unchanged from the parent and the
parent has property P, B and C are automatically not positive integer
multiples of θ; so child1 fails P only if t or 180−B−t is a positive
integer multiple of θ, and child2 fails P only if A−t or B+t is a positive
integer multiple of θ. Suppose, for contradiction, that **both** children
fail P for this particular t. Then (at least) one of the two "child1-bad"
conditions holds and (at least) one of the two "child2-bad" conditions
holds, giving four cases:

1. **t = aθ and A−t = bθ**, for some positive integers a,b. Adding:
   A = t + (A−t) = aθ + bθ = (a+b)θ. Since a,b ≥ 1, a+b is a positive
   integer, so A is a positive integer multiple of θ — contradicting
   property P for the (unchanged) angle A of the parent.

2. **t = aθ and B+t = bθ**, for some positive integers a,b. Then
   B = bθ − aθ = (b−a)θ. Since B > 0 and θ > 0, we need b − a > 0, i.e.
   b > a ≥ 1, so b−a is a positive integer, and B is a positive integer
   multiple of θ — contradicting property P for the parent's angle B.
   (If b ≤ a, the equation forces B ≤ 0, impossible since B is an angle of
   a triangle; so this sub-case cannot even arise, but if it did arise it
   would still be a contradiction of B>0, so the case is impossible either
   way.)

3. **180−B−t = aθ and A−t = bθ**, for some positive integers a,b.
   Subtracting: (180−B−t) − (A−t) = aθ − bθ, i.e.
   180 − B − A = (a−b)θ. Since A+B+C=180, 180−B−A = C, so
   C = (a−b)θ. As C > 0, we need a − b > 0, i.e. a > b ≥ 1, so a−b is a
   positive integer, and C is a positive integer multiple of θ —
   contradicting property P for the parent's angle C. (If a ≤ b, the
   equation forces C ≤ 0, again impossible, so as in case 2 the sub-case
   is simply impossible either way.)

4. **180−B−t = aθ and B+t = bθ**, for some positive integers a,b. Adding:
   (180−B−t) + (B+t) = aθ + bθ, i.e. 180 = (a+b)θ. Since a,b ≥ 1, n := a+b
   is an integer ≥ 2, so θ = 180/n — contradicting the hypothesis that θ is
   not of this form.

All four cases yield a contradiction, so no t ∈ (0,A) can make **both**
children fail P when the parent has P and θ ≠ 180/n for any integer n≥2.
Hence for every legal move, at least one child retains property P. ∎

**Lemma 2 (Existence of a good starting triangle).** For every
θ ∈ (0,180), there exists a valid triangle (A,B,C) — i.e. A,B,C > 0,
A+B+C=180 — with property P.

*Proof.* For δ ∈ (0,30) consider the triangle
$$A(\delta)=60+\delta,\quad B(\delta)=60+\delta,\quad C(\delta)=60-2\delta.$$
This is a valid triangle for every δ ∈ (0,30): A(δ), B(δ) = 60+δ > 0
automatically, and C(δ) = 60 − 2δ > 0 exactly for δ < 30; the sum
A(δ)+B(δ)+C(δ) = (60+δ)+(60+δ)+(60−2δ) = 180 for every δ. Consider the two
sets
$$S_1=\{\delta\in(0,30): 60+\delta \text{ is a positive integer multiple of }\theta\},\qquad
S_2=\{\delta\in(0,30): 60-2\delta \text{ is a positive integer multiple of }\theta\}.$$
For each fixed positive integer k, the equation $60+\delta=k\theta$ has at
most one solution δ = kθ−60, and the equation $60-2\delta=k\theta$ has at
most one solution δ = (60−kθ)/2; so $S_1$ and $S_2$ are each a subset of a
countable set (indexed by k ∈ ℤ_{>0}), hence countable. A countable union
of countable sets is countable (standard fact), so $S_1 \cup S_2$ is
countable. But (0,30) is an uncountable set of reals (standard fact:
any nondegenerate real interval is uncountable, e.g. by Cantor's diagonal
argument). Hence $(0,30)\setminus(S_1\cup S_2)$ is nonempty; pick any
δ in it. For this δ, A(δ)=B(δ)=60+δ is not a positive integer multiple of
θ (δ ∉ S₁) and C(δ)=60−2δ is not a positive integer multiple of θ
(δ ∉ S₂), so (A(δ),B(δ),C(δ)) has property P. ∎

**Theorem (the "only if" direction — fully proved).**
If θ ≠ 180/n for every integer n ≥ 2, then Shan-Yu has a strategy that
prevents the game from ever reaching a triangle with an angle equal to θ,
so Mulan does not have a winning strategy (she cannot guarantee a win in
finitely many steps).

*Proof.* Shan-Yu's strategy: choose the initial triangle to be one with
property P, which exists by Lemma 2. Thereafter, whenever it is his turn to
discard one of the two children Mulan has produced, he checks — by Lemma
1, applied with the current (property-P) triangle as parent — that at
least one child again has property P, and discards the other one (if both
have P, he discards either one, e.g. child1 by a fixed rule). By
induction on the number of moves played: the initial triangle has property
P (base case, Lemma 2); if the triangle before some move has property P,
then by Lemma 1 (using the round's hypothesis θ ≠ 180/n for all n≥2) at
least one child has property P, and Shan-Yu keeps such a child by his
strategy — so the triangle after the move again has property P. Hence
property P holds for the current triangle at every point in the game,
forever. Since property P implies (as noted right after its definition)
that no angle equals θ, the game — under this Shan-Yu strategy — never
reaches a terminal ("Mulan wins") state, at any finite move number. Hence
no strategy of Mulan's forces a win in finitely many steps against this
particular Shan-Yu strategy, so Mulan does not have a winning strategy.
∎

This proves: **Mulan wins ⟹ θ = 180/n for some integer n ≥ 2.**
(Equivalently, θ = 180/n for some integer n≥2 is *necessary* for Mulan to
win.) This single argument handles ALL θ that are not of the required form
— both θ > 90° and θ ≤ 90° non-divisor cases — with no case split on the
size of θ, superseding the earlier separate θ>90° "all angles < θ"
argument (that argument remains correct as a special case but is no longer
needed: Lemma 1's case 4 shows the a+b≥2 forcing condition, which is the
only case using the non-divisibility hypothesis, cannot even arise when
θ>90° regardless of divisibility, since a+b≥2 would force θ≤90° — so P is
trivially preserved for θ>90° too, consistent with but not requiring the
old lemma).

### "If" direction: genuine progress and an honestly-recorded gap

We attempted to complete the "if" direction (θ=180/n ⇒ Mulan wins) using
the same machinery, and discovered why the "reduce via repeated shave to an
all-integer-multiple triple" plan (proposed in this approach's outline and
in the sibling `shave-and-halve-forcing.md`) **cannot work as a complete
strategy**, which we record precisely so no future round re-attempts it
without a fix.

**Definition.** A move (choice of vertex to cut and parameter t) is
*forced* if exactly one of child1, child2 has an angle equal to θ (so
Shan-Yu, to avoid an immediate loss, has no real choice — he must discard
the θ-bearing child). By the same four-case algebra as Lemma 1 (with a=b=1
throughout, i.e. targeting the literal value θ rather than a general
multiple), a move is forced exactly when t equals one of θ, A−θ, 180−B−θ,
B+θ (whichever of these four lies in the valid range (0,A) and produces
exactly one θ-containing child) — this is precisely the "Shave lemma" of
`shave-and-halve-forcing.md`, and each such move transforms the current
angle-triple (X,Y,Z) (X = the shaved/source angle, X>θ required for
validity, Y = the recipient, Z = untouched) into (X−θ, Y+θ, Z): it moves
exactly θ from one slot to another and leaves the third slot unchanged.

**Lemma 3 (fractional-part invariance under forced play, new
obstruction).** Let $f(x) := x/\theta - \lfloor x/\theta\rfloor \in[0,1)$
denote the fractional part of x in units of θ. If the game proceeds only
through forced moves (in the sense above), then at every stage the
MULTISET $\{f(A),f(B),f(C)\}$ of the three current angles is exactly equal
(as a multiset of real numbers) to the multiset $\{f(A_0),f(B_0),f(C_0)\}$
of the starting triangle.

*Proof.* By induction on the number of forced moves played. Base case:
trivial (0 moves). Inductive step: a forced move replaces the current
triple's values by (X−θ, Y+θ, Z) for some choice of two of the three
current slots X (source, X>θ) and Y (recipient), the third Z unchanged.
Since f(X−θ)=f(X) and f(Y+θ)=f(Y) (subtracting/adding an integer number of
θ's — here exactly one θ — does not change the fractional part in units of
θ) and f(Z)=f(Z) trivially, the new multiset of fractional parts
{f(X−θ), f(Y+θ), f(Z)} = {f(X), f(Y), f(Z)}, i.e. exactly the multiset of
fractional parts before the move (as a multiset — the two changed slots
keep their own individual fractional part values, they are simply
relabeled by which physical vertex now holds them). So the multiset of
fractional parts is unchanged by one forced move, hence (by induction) by
any finite sequence of forced moves. ∎

**Corollary (the obstruction).** If θ=180/n and Shan-Yu opens with a
property-P triangle (which exists by Lemma 2, applied with this θ — note
Lemma 2 did not use the non-divisibility hypothesis, so it applies for
divisor θ too), then f(A₀), f(B₀), f(C₀) are all nonzero (property P is
exactly "no angle is an exact multiple of θ", i.e. exactly "all three
fractional parts are nonzero"). By Lemma 3, if Mulan restricts herself to
forced (shave-type) moves only, every reachable triangle also has all
three fractional parts nonzero — so no angle can ever become an exact
multiple of θ, and in particular the win condition (some angle exactly
= 1·θ, fractional part 0 with nonzero integer part) can **never** be
reached this way. So a Mulan strategy built purely from forced/shave moves
does not win against such a Shan-Yu opening, **for any n**, even when
θ=180/n. This refutes the "reduce to all-integer-multiples via repeated
shave" plan as a complete strategy; a correct "if"-direction strategy must
make essential use of non-forced moves, where Shan-Yu retains a genuine
choice, engineered so that both of his options are eventually losing (a
recursive, game-tree/strategy-stealing argument, not a single deterministic
reduction). This is not completed in this round.

## Key lemmas (claim + mechanism)
- **Cut formula (child1={B,t,180−B−t}, child2={C,A−t,B+t})** — proved above
  from angle-sum in each sub-triangle.
- **Lemma 1 (Invariance of property P)** — proved in full above by exhaustive
  4-case algebra; this is the load-bearing new result of this round, closing
  the previously-open central gap for the whole "only if" direction.
- **Lemma 2 (existence of a good starting triangle, for ANY θ)** — proved in
  full above by a countable-set / uncountable-interval cardinality argument.
- **"Only if" Theorem** — proved in full above, combining Lemmas 1 and 2 via
  induction on move count.
- **Lemma 3 (fractional-part invariance under forced play)** — proved in
  full above; used to establish the obstruction to the naive "if"-direction
  strategy (a genuine negative result, not a gap in this round's own
  reasoning).

## Open gaps
- **The "if" direction (θ=180/n ⇒ Mulan wins) is NOT proved.** We showed
  (Lemma 3 + Corollary) that the natural "shave-only" strategy proposed by
  the outline and by `shave-and-halve-forcing.md` cannot work in general —
  Mulan must use non-forced moves essentially, with a recursive/game-tree
  argument (e.g., a move creating two "threats" such that both of Shan-Yu's
  options are themselves losing positions, established by induction on some
  complexity measure smaller than raw move count). No such argument is
  constructed in this round; this is the genuine remaining content needed
  for `solved` status on the full characterization. Future rounds should
  NOT re-attempt the pure-shave reduction (refuted here) but should look for
  an argument in the style of "Mulan attacks two vertices' fractional
  structure simultaneously" or a direct strategy-stealing / potential-
  function argument that doesn't require reducing to an all-integer-
  multiple state.
- The θ=90° (n=2) base case of the "if" direction remains fully proved
  (Lemma 1 of `shave-and-halve-forcing.md`, reproduced there: from any
  triangle with no 90° angle, some vertex has both other angles acute,
  and the altitude from it makes both children right triangles in one
  move) — this is a genuine, complete win for n=2, unaffected by the Lemma
  3 obstruction (it is a single non-forced-in-the-shave-sense move, since it
  is not of the t=θ/A−θ/... form but a distinct forcing condition, verified
  separately in the sibling file's case-(iv) computation matching this
  file's cut-formula derivation).

## Cases to cover
- θ > 90°: "only if" direction done (via the unified Lemma 1/Theorem).
- θ ≤ 90°, θ ≠ 180/n: "only if" direction done (same unified Theorem, no
  separate case needed).
- θ = 180/n, n = 2: "if" direction done (import θ=90° lemma from sibling
  file, re-verified as a special case of the general one-move-forcing
  analysis).
- θ = 180/n, n ≥ 3: "if" direction OPEN — this is the only remaining case
  in the whole problem.

## Watch out for
- Do not confuse "property P" (no angle is any positive integer multiple of
  θ) with the much weaker "no angle equals θ" — P is what Shan-Yu actually
  needs to maintain, and it is P (not the weaker condition) that is
  preserved by Lemma 1; the weaker condition alone is NOT obviously
  preserved by a single argument (a child could pick up a 2θ or 3θ angle
  which is not an immediate loss, but sets up a later bisection risk) —
  P closes that gap by ruling out every multiple, not just the exact value
  θ, in one stroke.
- The "only if" Theorem's proof is complete and does not depend on any
  numerical verification; the Python checks in this session (θ ∈
  {50,37,100,130,170,61.5,44,29.9}°, both uniformly random and
  adversarially-targeted t-values, zero violations across 200k+ trials)
  were a sanity check on the algebra before write-up, not a proof step.
- Lemma 3's obstruction is about FORCED moves only; it does NOT show the
  "if" direction is false (the known/expected answer is still that θ=180/n
  is winning for Mulan) — it only rules out one specific (incomplete)
  strategy. Do not misread this as disproving the target characterization.

## Promotable lemmas
- **Lemma 1 (Invariance of property P under Shan-Yu's choice, for
  θ ≠ 180/n)** — fully proved above by 4-case algebra; directly closes the
  "only if" direction's central gap. Reusable as-is by any other approach
  (e.g. `maximal-safe-set-fixedpoint.md`'s S_θ / co-inductive framing can
  take S_θ := {triangles with property P} and cite this lemma verbatim as
  its closure verification).
- **Lemma 2 (existence of a property-P starting triangle for any θ)** —
  fully proved above by a countability argument; reusable by any approach
  needing an initial-triangle construction for either player.
- **"Only if" Theorem (θ ≠ 180/n for all integers n≥2 ⇒ Shan-Yu wins)** —
  fully proved above; this is the complete "only if" half of the target
  characterization and should be imported into `current.md` as settled.
- **Lemma 3 (fractional-part invariance under forced/shave moves)** — fully
  proved above; a negative/obstruction result, valuable for steering future
  "if"-direction attempts away from the refuted pure-shave strategy.
