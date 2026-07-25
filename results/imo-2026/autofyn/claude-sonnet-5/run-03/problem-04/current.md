## Status
solved

## Approaches tried
- `shave-and-halve-forcing.md` — partial. Proved θ>90° defense and the full
  "if" direction for even n via Altitude+Shave, but left odd n≥3 and the
  general "only if" (θ≤90°, non-divisor) open. Correct as far as it goes;
  superseded (not contradicted) by `ngon-arc-reduction.md`'s unified
  treatment.
- `mod-theta-invariant.md` — partial. Proved the full "only if" direction in
  one unified argument ("property P" invariant, 4-case algebra) and proved a
  genuine *obstruction*: pure shave/up-shave ("forced") moves alone can never
  finish the "if" direction from a θ-multiple-avoiding start. Correctly left
  the "if" direction open, correctly flagged that a non-forced move is
  structurally necessary.
- `maximal-safe-set-fixedpoint.md` — partial. Built a rigorous safety-game
  (Wₖ/S) formalization, reproved θ>90° defense and the n=2 base case inside
  it, and independently proved the same forced-move obstruction as
  `mod-theta-invariant.md` (Down-shave/Up-shave alone cannot finish "if").
  Correctly left the "if" direction (needs a non-forced move) and the general
  "only if" open within its own framework.
- `ngon-arc-reduction.md` — **solved**. Supplies exactly the missing
  ingredient the other three approaches identified as necessary but did not
  construct: a single non-forced cut (the "residue-alignment move", Lemma 3)
  that forces BOTH children to acquire a θ-multiple angle whenever the
  parent has none, closing the "if" direction for all n≥3 (n=2 handled
  separately by the classical altitude move). Combined with a clean
  disjoint-bad-residue-sets argument closing the "only if" direction for all
  non-divisor θ (superseding the θ>90°-only argument of the sibling files),
  this gives a complete, gap-free proof of both directions. Verified by the
  proof-reviewer: every lemma re-derived and checked algebraically by hand,
  every load-bearing claim (Lemma 3's "both children forced good", the
  disjoint-bad-sets claim, all 6 vertex/labelling permutations) checked by
  exact-`Fraction` randomized simulation (thousands of trials, zero
  discrepancies), and the *entire* strategies (both directions) simulated
  end-to-end as real game trees (2600 trials for "if", 60×40 adversarial
  moves for "only if") with zero failures.

## Current best
See Full proof below — the characterization is fully established.

## Full proof

**Answer.** Mulan has a winning strategy if and only if θ = 180°/n for some
integer n ≥ 2.

*(The following is the proof from `approaches/ngon-arc-reduction.md`,
reviewed and independently verified; see that file for the complete
line-by-line writeup. Cut Formula, Shave Lemma, and the Residue-Alignment
Move / No-Multiple-Invariant lemmas are also certified standalone in
`results/imo-2026-04/lemmas/`.)*

Throughout, angles are real numbers in degrees; for a triangle write its
angle-triple as (A,B,C), A+B+C=180. For real x, ρ(x) = x − θ⌊x/θ⌋ ∈ [0,θ) is
the residue of x mod θ; x is a **θ-multiple** if ρ(x)=0.

### Cut Formula (Lemma 0)
If Mulan cuts a triangle with angles X (vertex R), Y (vertex P), Z (vertex
Q) from a point P' on side PQ to R, with t = ∠PRP' ∈ (0,X), the two
resulting triangles are child1 = (Y, t, 180−Y−t), child2 = (Z, X−t, Y+t);
every t ∈ (0,X) is achieved by exactly one legal cut point, and every legal
move of the game has this form for some choice of vertex R and labelling.
(Elementary triangle angle-sum / supplementary-angle argument; full proof in
`lemmas/cut-formula.md`.)

### "If" direction: θ = 180°/n, n≥2 integer ⟹ Mulan wins
- **n=2 (θ=90°).** From any triangle with no right angle, at least two
  angles are acute; dropping the altitude from the third vertex to the
  opposite side lands strictly inside that side (both projections are
  positive since both base angles are acute, and their sum is exactly the
  base length), and both resulting children contain a 90° angle at the foot.
  Mulan wins in exactly one move.
- **n≥3, Shave Lemma.** If some angle is X = kθ (k≥1 integer), cutting at
  t=θ forces (on pain of an immediate loss) Shan-Yu into a triangle with
  that vertex now at (k−1)θ; iterating finishes in k−1 more forced moves
  (full proof in `lemmas/shave-lemma.md`).
- **n≥3, Residue-Alignment Lemma (the new move).** If no angle is a
  θ-multiple and some angle X exceeds θ, a single explicit cut (parameter
  t = θ − ρ(Y) at the X-vertex, Y one of the other two angles) forces BOTH
  possible children to already contain a θ-multiple angle jθ with
  1≤j≤n−1 (full proof, with all bounds verified, in
  `lemmas/residue-alignment-move.md`).
- **Assembly.** Given any starting triangle with no angle = θ: if some
  angle is a θ-multiple kθ (k≥2, since k=1 would already be a win), Shave
  finishes in k−1≤n−2 moves. Otherwise, by pigeonhole (three angles each
  <θ would sum to <3θ≤180 for n≥3, contradiction) some angle exceeds θ, and
  Residue-Alignment forces a θ-multiple angle jθ (1≤j≤n−1) into whichever
  child Shan-Yu keeps; Shave then finishes in ≤n−2 more moves. Either way
  Mulan wins in at most n−1 moves, against every Shan-Yu choice throughout.

### "Only if" direction: θ ≠ 180°/n for any integer n≥2 ⟹ Shan-Yu wins
Write r₀ = 180 mod θ; θ=180/n for some integer n≥2 iff r₀=0, so the case to
handle is r₀≠0. Define property 𝓘: "no angle is a θ-multiple". A property-𝓘
triangle exists for every θ (a one-parameter family with only countably many
"bad" parameter values, avoided by an uncountable-vs-countable cardinality
argument). If the current triangle has 𝓘 and Mulan cuts vertex X (others
Y,Z) at any t∈(0,X): writing r_X,r_Y,r_Z∈(0,θ) for the (nonzero, by 𝓘)
residues and s=ρ(t), child1=(Y,t,180−Y−t) is "bad" (has a θ-multiple angle)
exactly when s∈{0, (r₀−r_Y) mod θ}, and child2=(Z,X−t,Y+t) is bad exactly
when s∈{r_X, (−r_Y) mod θ}. Checking all four possible coincidences between
these two 2-element sets, each forces either r_X≡0, r_Y≡0, r_Z≡0 (mod θ) —
contradicting 𝓘 — or r₀≡0 (mod θ) — contradicting r₀≠0. So the two bad-sets
are disjoint, hence s cannot lie in both, hence at least one child retains
𝓘. Shan-Yu opens with a property-𝓘 triangle and always keeps a 𝓘-child; by
induction 𝓘 (hence "no angle = θ") holds forever, so the game never
terminates in Mulan's favor. (Full case-by-case algebra and an independently
phrased equivalent proof — "property P", 4-case algebra — are in
`lemmas/no-multiple-invariant.md`, `approaches/ngon-arc-reduction.md` §2, and
`approaches/mod-theta-invariant.md` Lemma 1.)

### Conclusion
$$\text{Mulan has a winning strategy} \iff \theta = \dfrac{180^\circ}{n}\ \text{for some integer } n\ge2.$$

**Verification.** Both directions are proofs (not mere sanity checks); the
proof-reviewer additionally re-derived the load-bearing algebra by hand and
confirmed it by randomized exact-`Fraction` simulation, including full
game-tree simulation of the actual strategies end-to-end (thousands of
trials, both directions, n ranging 2–14 and non-divisor θ both above and
below 90°), with zero discrepancies.
