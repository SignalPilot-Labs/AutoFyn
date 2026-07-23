## Status
partial

**(proof-reviewer, round 4 note — FORMALLY RETIRED.)** Per the round-4 outliner's
recommendation (below) and the reviewer's independent verification, this slug's Step A
("tie-or-degenerate lemma" + iterated-cuts Corollary) has been merged with
`dyadic-cascade-induction`'s §3 into a single canonical certified lemma,
`lemmas/vertex-lemma.md`. **This slug is retired as an independent whole-attempt** — do not
dispatch a builder to it again unless a future outliner identifies a genuinely new,
non-redundant target distinct from what `dyadic-cascade-induction` §2c already covers (full
n=2 Case (ii) closure) and what `lemmas/vertex-lemma.md` already covers (the single-cut/
joint-optimum vertex fact). Any future citation of "the vertex lemma" or "tie-or-degenerate
lemma" by any sibling approach (e.g. `concavity-minimax-duality` §8) should point to
`lemmas/vertex-lemma.md`, not to this slug file.

**(proof-outliner, round 4 note — RETIRED as an independent whole-attempt slug; recommend
lemma promotion instead of further building.)** This approach has been stalled since round 2
(no round-3 builder activity) while its own remaining gaps (global coverage of the full Case
(ii) region, pinning the `a_2/a_3=2` recursive condition, general `n`) have effectively been
superseded: `dyadic-cascade-induction` §2c already gives a **complete, unconditional** closure
of the entire n=2 Case (ii) region by direct casework (not merely a local neighborhood of the
dyadic point, and not conditional on importing "`g(\text{dyadic})=1/7`" the way this file's
Step C is), so continuing this slug's own route to "extend local uniqueness across the full
Case (ii) region" would only re-derive, by a narrower and more conditional method, a result
the population already has in full. Per CLAUDE.md ("never re-attempt a solved problem" /
diversify rather than duplicate), this slug does not diversify the field further and is
retired as an independent attempt. **Two pieces of this file's content remain genuinely
valuable and should be promoted:**
1. **Step A, the "tie-or-degenerate lemma"** (piecewise-linearity of a single cut, XY's optimal
   cut position is always a tie/bisection/degenerate limit) is **general-purpose and fully
   proved**, but it is essentially the *same statement* as `dyadic-cascade-induction`'s own
   §3 "vertex lemma" (both say: a single cut's value, as a function of cut position, is
   piecewise linear with breakpoints exactly at ties/self-bisections, so the minimizer is
   always a breakpoint or a degenerate limit) — proved independently, by two different builders,
   in two different rounds, with slightly different framing (this file's version explicitly
   proves the "Corollary (iterated cuts)" extension to multiple simultaneous cuts, which
   `dyadic-cascade-induction`'s §3 states as a consequence but does not prove in as much
   detail). **Recommend the reviewer certify ONE canonical lemma file
   (`lemmas/vertex-lemma.md`)** merging the cleanest parts of both write-ups (this file's Step
   A for the iterated-cuts corollary, `dyadic-cascade-induction` §3 for the base single-cut
   statement), rather than carrying two redundant near-duplicate proofs across the population.
2. **Step C's convex-hull/gradient certificate technique** (`λ=(2/7,1/7,4/7)`, the "0 in the
   strict interior of the active gradients' convex hull ⟹ unique local max of a min-of-affines
   function" criterion) is a reusable proof *pattern*, already flagged as a "Promotable lemma"
   in this file's own section below — worth keeping on record (it does not need a separate
   certification, since it is a standard convex-analysis fact, but the concrete worked
   computation for this problem's `f1,f2,f3` at the dyadic point is a citable artifact any
   future locally-scoped concavity argument — e.g. a future revival of
   `concavity-minimax-duality`'s abandoned restricted-domain salvage, if ever separately
   pursued — could import directly instead of re-deriving).

**No further builder dispatch recommended for this slug this round or future rounds**, unless
a future outliner identifies a genuinely new, non-redundant target for it distinct from what
`dyadic-cascade-induction` already covers.

## Approaches tried
- (round 1) new approach, outline only, nothing established yet.
- (round 2) **This round's work.** Carried out the bounded n=2 (3-piece, 2-parameter)
  hand/exact-fraction computation the outline called for, restricted to Case (ii)
  (a1 < 2a2). Concrete results (all exact-fraction verified, no floats in the final
  claims):
  1. Proved a general **"tie-or-degenerate" structural lemma**: XY's optimal placement
     of a single cut, holding everything else fixed, always either creates an exact
     tie (the new piece equals another current piece, or the two pieces produced by
     the cut equal each other) or degenerates (cut position → an endpoint, i.e. an
     unused cut). This is proven in full below (not just asserted) and is a genuinely
     new, promotable lemma — it is the rigorous version of "XY's active response
     pattern is locally constant" that the outline's Step 2 needed, and it directly
     explains *why* the third move family the outline-reviewer flagged (splitting a1
     to double-match two other pieces at once) is a legitimate elementary move: it is
     just two matching-ties applied to the two cuts of a single piece, not a
     genuinely new phenomenon outside the tie framework.
  2. Using this lemma, enumerated 15 candidate 2-cut response patterns for XY at n=2
     (bisections, single matches, the double-match, and "match-then-bisect-remainder"
     combinations) and computed each one's exact e = L−X formula by hand. Found that
     the outline-reviewer's flagged "richer move" (match a1 to a2 with one cut, then
     bisect the *remainder* a1−a2 with the second cut) gives a clean new formula
     e = a3 that is NOT one of the outline's two named canonical moves, and IS
     sometimes strictly better for XY than both "bisect a1" and "match a1→a2" (e.g. at
     (a1,a2,a3) = (4/7, 8/25, 19/175) it gives e=19/175 ≈ 0.109, beating "match a1→a2"
     ≈ 0.143). This confirms the outline-reviewer's finding was correct and
     substantive, not a false alarm.
  3. Despite this, at the dyadic point (4/7,2/7,1/7) itself, all of the 15 enumerated
     candidates give e ≥ 1/7, with exactly **three** tied at exactly 1/7: "bisect a1"
     (e=a2−a3), "match a1→a2" (e=|2a1−1|), and "match-then-bisect-remainder"
     (e=a3) — see the exact computation below.
  4. Proved (via a convex-analysis subgradient argument on the concave, piecewise-affine
     function h := min of these three candidate formulas, restricted to the 2-parameter
     region a1+a2+a3=1) that the dyadic point is the **unique, strict** maximizer of h
     over the region where the three formulas' validity conditions hold (a neighborhood
     of the dyadic point within Case (ii), see below) — a genuinely new, rigorous
     local-uniqueness result, not merely numerical evidence.
  5. Combined with the (imported) fact that no XY response can beat e=1/7 at the exact
     dyadic point — the "hard direction" of the theorem, shared prerequisite with
     `dyadic-cascade-induction`'s Case (i)/(ii) upper-bound argument — this yields a
     complete proof of **local uniqueness of the ratio-2 point within Case (ii), in a
     neighborhood of the dyadic point**. Global uniqueness over the *entire* Case (ii)
     region, and the case a2/a3 ratio (needed for full n=2), and the whole general-n
     argument, remain open — see Current best / gaps below.

## Current best

**(round 3, outliner note — light touch, this approach's own route is unchanged.)** This
round's alt-framing explorer confirmed your Step C certificate (`λ=(2/7,1/7,4/7)`, gradient-
hull interior-point argument) is exactly the missing piece for a REVIVED sibling approach,
`concavity-minimax-duality`: IF global concavity of `g` over the whole n=2 domain can be
proved (numerically well-supported this round, 0 violations across 34 test pairs, but not
yet proved), your local certificate promotes automatically to a full global-uniqueness proof
via the standard convex-analysis fact "a concave function's strict local max is its unique
global max" — bypassing `dyadic-cascade-induction`'s casework entirely. Your own next task is
unchanged (close gaps 1-2 below: extend local uniqueness across the FULL Case (ii) region,
not just this neighborhood, and pin the `a_2/a_3=2` condition) — this is valuable
independently of whether `concavity-minimax-duality`'s global concavity proof succeeds, both
as a fallback and as a partial step toward the same global-coverage goal by direct extension
rather than a concavity shortcut.

**Setup and notation.** For n=2, LB's partition is three pieces a1≥a2≥a3≥0,
a1+a2+a3=1 (normalize the stick to length 1; S=1 is WLOG by scaling). Write
g(a1,a2,a3) for XY's best-response value: the minimum, over every way XY can place
his ≤2 remaining cut points, of L = (sum of odd-ranked pieces in the final sorted
multiset), where "odd/even rank" (1st, 3rd, 5th,... vs 2nd, 4th,...) determines who
claims each piece under optimal alternating claiming (Lemma G — greedy/exchange
argument, standard and shared with `dyadic-cascade-induction`: since the claiming
phase is an alternating-pick game on a fixed finite multiset with LB first, "always
take the current largest remaining piece" is optimal for both players simultaneously,
by an exchange/domination induction on multiset size — swapping any suboptimal pick
for the current max weakly increases the mover's own total and weakly decreases what
is left for the opponent). Write e := L − X = 2L − 1 (X = sum of even-ranked pieces,
S=1). LB wants to choose a to maximize g; the target value for this problem is
c(2) = 4/7, i.e. e(2) = 1/7, attained (as is imported from the lower-bound/
construction direction of the theorem, shared prerequisite) by exactly the dyadic
partition (4/7,2/7,1/7).

**This approach's target for n=2, Case (ii) (a1 < 2a2):** prove that (4/7,2/7,1/7)
— which sits exactly ON the boundary a1=2a2 between Case (i) and Case (ii) — is the
*unique* point at which g attains the value 1/7, at least locally, forcing any
would-be optimal LB partition to satisfy a1=2a2 exactly (ruling out the open region
a1<2a2 as containing a competing or tied maximizer).

### Step A. The tie-or-degenerate lemma (proved in full; promotable)

**Lemma (single-cut optimal position).** Fix a finite multiset of "background"
piece values and consider replacing one background piece of length ℓ by two new
pieces (t, ℓ−t), t ∈ (0,ℓ), everything else held fixed. Let L(t) denote the
resulting value (sum of odd-ranked pieces of the full sorted multiset). Then:
(a) L(t) is continuous and piecewise linear on (0,ℓ), with slope in {−2,−1,0,1,2}
constant between consecutive "critical values" of t — namely the values where t or
ℓ−t crosses a background piece's value, or where t = ℓ−t (i.e. t=ℓ/2);
(b) consequently, the infimum of L over t ∈ (0,ℓ) is approached either at a critical
value (a tie: the new piece t, or ℓ−t, equals some other current piece's value, or
the bisection t=ℓ/2) or in the degenerate limit t→0 or t→ℓ (an unused cut).

*Proof.* As t increases, the value "t" increases at rate +1 and the value "ℓ−t"
decreases at rate −1; every other piece in the multiset is unaffected. The sorted
rank of "t" among all pieces changes by exactly one position each time t crosses a
fixed background value (or the co-moving value ℓ−t); the same holds for "ℓ−t". Away
from any such crossing, the combinatorial rank assignment (hence which pieces are
odd/even-ranked) is locally constant, so on each open sub-interval between
consecutive crossings, dL/dt is constant and equals ε_t − ε_{ℓ−t}, where ε_t = 1 if
"t"'s current rank is odd (contributes to L) else 0, and ε_{ℓ−t} = 1 if "ℓ−t"'s
current rank is odd else 0 (since d/dt[value "t"] = +1 and d/dt[value "ℓ−t"] = −1,
and L only picks up odd-ranked pieces). This constant lies in {−1,0,1}. [If instead
one tracks L as sum of odd ranks directly without separating by which of t, ℓ-t is
odd, the same conclusion holds; the ± 2 case mentioned above does not in fact occur
here since only two values move, one up one down, each contributing at most ±1 —
correcting the general statement to slope ∈ {−1,0,1}, which is all that is used
below.] On a sub-interval where the slope is a nonzero constant s, L(t) is strictly
monotonic, so its infimum over the closed sub-interval is attained at whichever
endpoint is favored by the sign of s — i.e. at a critical value bounding that
sub-interval, or (if the sub-interval touches t=0 or t=ℓ) in the limit t→0 or t→ℓ.
On a sub-interval where s=0, L is constant, so every point (including the endpoints)
attains the infimum. In every case, inf L is attained at a critical value or in a
boundary limit. Since XY minimizes L, this proves the claim. ∎

**Corollary (iterated cuts).** For XY placing several cuts (in our n=2 case, up to
two), holding all cuts but one fixed, the lemma applies to the remaining free cut;
hence at a joint optimum, *every one* of XY's cuts individually sits at a tie (with
a current background piece, with another of XY's new pieces, or a self-bisection) or
is degenerate (contributes a vanishingly small piece, equivalent in the limit to an
unused cut, by continuity of L in the cut positions). This is exactly the
justification for restricting the search for XY's optimal 2-cut response, at n=2, to
the finite list of "matching / bisecting" combinatorial patterns enumerated in Step B
— **including** the outline-reviewer's flagged "double match" (splitting a1 with two
ties in succession: first tying one new piece to a2, then tying the *other* new
piece, from the remaining sub-length, to a3) and the "match-then-bisect" pattern
(one tie to a2, the other a self-bisection of the remainder) — both of which are
literal instances of this lemma's two cuts each individually satisfying the
tie-or-bisect condition, not an exception to it.

This closes the outline's Step 2 gap **as a general structural fact** (every
combinatorial response pattern XY could ever use is built from ties/bisections), but
it does **not** by itself tell us *which* tie-pattern is XY's actual minimizer for a
given a — that requires comparing the finitely many resulting candidate values, done
next.

### Step B. Explicit n=2, Case (ii) candidates (exact fractions, hand-derived)

For a1≥a2≥a3≥0, a1+a2+a3=1, a1<2a2 (Case ii), the following XY response patterns are
all valid instances of Step A's tie-lemma. Each formula below was derived by hand by
sorting the resulting multiset (fixing the branch a1/2 ≥ a3, valid at and near the
dyadic point since there a1/2=a2=2/7>1/7=a3) and computing L−X directly; each was
cross-checked with exact `Fraction` arithmetic (not floats) at multiple sample points
including the dyadic point itself and (4/7, 8/25, 19/175):

- **f1 := "bisect a1"** — split a1 into (a1/2,a1/2). Sorted a2,a1/2,a1/2,a3 (using
  a1/2<a2, i.e. Case ii, and a1/2≥a3). L=a2+a1/2, X=a1/2+a3, so
  **e = a2 − a3.**
- **f2 := "match a1→a2"** — split a1 into (a2, a1−a2); since a1<2a2 (Case ii),
  a1−a2 < a2, so the new piece a1−a2 sits below a2. In the branch a1≥1/2 (so that
  a1−a2 ≥ a3, i.e. a1 ≥ a2+a3 = 1−a1): sorted a2,a2,a1−a2,a3, giving L=a2+(a1−a2)=a1,
  X=a2+a3=1−a1, so **e = 2a1 − 1.** (In the complementary branch a1<1/2, an
  analogous computation gives e=1−2a1=|2a1−1|; only the a1≥1/2 branch is used near
  the dyadic point, where a1=4/7>1/2.)
- **f3 := "match a1→a2, then bisect the remainder"** — first tie one new piece to
  a2 (splitting off a2, remainder r := a1−a2), then bisect r with the second cut
  into (r/2, r/2). Resulting multiset {a2 (new), r/2, r/2} replacing a1, together
  with the untouched a2, a3: {a2,a2,r/2,r/2,a3}. Since r=a1−a2<a2 (Case ii),
  r/2 < a2, so a2,a2 are the top two ranks regardless of where r/2 falls relative to
  a3. Whether r/2 ≥ a3 or r/2 < a3, direct computation of both branches gives the
  **same** value: L−X = a3 exactly (verified both algebraically and by exact
  fraction at (4/7,8/25,19/175): e = a3 = 19/175, matching the code computation).
  So **e = a3.**
- (f4 := "bisect a3": split a3 into (a3/2,a3/2); sorted a1,a2,a3/2,a3/2, giving
  **e = a1 − a2.** This is *not* tied for the minimum at the dyadic point — there it
  equals 2/7 > 1/7 — but is included because it is the actual minimizer away from
  the dyadic point, e.g. at (0.4,0.36,0.24) where it gives e=0.04, beating f1,f2,f3.)

At the dyadic point (a1,a2,a3)=(4/7,2/7,1/7): f1 = a2−a3 = 1/7; f2 = 2a1−1 = 1/7;
f3 = a3 = 1/7 — **all three tie exactly at 1/7**, while f4 = a1−a2 = 2/7 is slack
(not competitive there). An additional 11 further candidate patterns (double
matches, trisections, combined bisections — bisect a2, bisect a3, trisect each
piece, double-tie a1 to two copies of a2, etc.) were also computed by hand/exact
fraction at the dyadic point; none goes below 1/7 (see computation log; all equal
1/7 or exceed it). This is consistent with (but, absent the general theorem, does
not by itself *prove*) g(dyadic) = 1/7 exactly.

### Step C. Local uniqueness via concavity/subgradient argument (rigorous, new)

Treat (a1,a2) as the two free parameters (a3 = 1−a1−a2), and define, on the region
where the branch conditions above hold (a1≥1/2, a1/2≥a3 — both true at, and by
continuity in a neighborhood of, the dyadic point):
  h(a1,a2) := min(f1,f2,f3) = min(a1+2a2−1, 2a1−1, 1−a1−a2).

Each of f1, f2, f3 is an honest affine function of (a1,a2), so **h is concave** (a
finite minimum of affine functions is concave — standard fact of convex analysis,
KB "Piecewise-concavity smoothing" / general convexity toolkit). Since each fi is
the e-value of an *actual* strategy available to XY, and g(a) is defined as XY's
best (minimal) achievable e, we have the trivial but crucial inequality
  **g(a1,a2,a3) ≤ h(a1,a2)** for every a in the region where f1,f2,f3 are valid.

*Gradients.* ∇f1 = (1,2), ∇f2 = (2,0), ∇f3 = (−1,−1) (as functions of (a1,a2), with
a3 eliminated).

*Claim: 0 lies in the strict interior of the convex hull of {∇f1,∇f2,∇f3}.* Solve
λ1∇f1+λ2∇f2+λ3∇f3 = 0 with λ1+λ2+λ3=1: componentwise, λ1+2λ2−λ3=0 and
2λ1−λ3=0. From the second equation λ3=2λ1; substituting into the first:
λ1+2λ2−2λ1=0 ⟹ 2λ2=λ1 ⟹ λ2=λ1/2. Then λ1+λ1/2+2λ1 = 1 ⟹ (7/2)λ1=1 ⟹ λ1=2/7,
λ2=1/7, λ3=4/7. All three are strictly positive and sum to 1, so 0 is a strict
convex combination of the three gradients, i.e. lies in the interior of their
convex hull (a point with all-positive barycentric weights relative to a
non-degenerate triangle of three vectors in the plane is an interior point of that
triangle, since none of the two-point sub-hulls — line segments — can contain the
origin exactly at a point with the third weight >0 unless the origin actually needs
that third vertex, which is exactly what "all λi>0" encodes). [Independently
cross-checked numerically: solving the same two linear equations for λ gives
λ=(2/7,1/7,4/7), confirmed by direct back-substitution: (2/7)(1,2)+(1/7)(2,0)+
(4/7)(−1,−1) = (2/7+2/7−4/7, 4/7+0−4/7) = (0,0). ✓.]

*Consequence.* Because h is concave and 0 lies in the interior of the convex hull
of the gradients of the pieces that attain h's value at (a1,a2)=(4/7,2/7) (namely
f1,f2,f3, all equal to 1/7 there, per Step B), standard convex-analysis theory of
polyhedral (min-of-affine) concave functions gives: the directional derivative of h
at this point in any unit direction d is
  h'((4/7,2/7); d) = min(∇f1·d, ∇f2·d, ∇f3·d),
and because 0 is in the *interior* of the hull of the three gradients, for every
d≠0 at least one of ∇f1·d, ∇f2·d, ∇f3·d is strictly negative (if all three were
≥0 simultaneously for some d≠0, then 0 could not be a strict positive combination
of the three gradients with all λi>0, since a nonnegative combination of vectors
each having ≥0 dot product with d must itself have ≥0 dot product with d, forcing
0·d=0, consistent — but the *interior* condition additionally rules out d lying in
the polar cone of any two of the three gradients alone, which is exactly what
strict positivity of all three λ's guarantees: geometrically, the origin being
strictly inside the triangle spanned by the three gradient endpoints means every
open halfplane through the origin contains at least one full gradient vector in its
strict interior, forcing that gradient's dot product with the halfplane's inward
normal direction to be strictly negative for the complementary direction — concretely,
this is the standard "strict local max of a min-of-affine-functions concave function
via 0 in the interior of the active gradient hull" criterion). Hence, since h is
concave, this point is the unique maximizer of h over the *entire* domain where f1,
f2, f3 are all simultaneously defined by the SAME formulas (i.e., wherever the
branch conditions a1≥1/2 and a1/2≥a3 hold) — concavity upgrades "strict local max"
to "unique global max over that whole domain," because a concave function cannot
have two distinct points with equal value unless it is constant along the segment
between them, which would force the directional derivative along that segment to
vanish at (4/7,2/7), contradicting the strict negativity just established in every
direction.

*Putting it together.* For any (a1,a2,a3) ≠ (4/7,2/7,1/7) in Case (ii) with a1≥1/2
and a1/2≥a3 (a neighborhood of the dyadic point, verified to contain it since there
a1=4/7≥1/2 and a1/2=2/7≥1/7=a3, both with room to spare):
  g(a1,a2,a3) ≤ h(a1,a2) < h(4/7,2/7) = 1/7 = g(4/7,2/7,1/7)
(the last equality importing the shared-prerequisite fact, established via the
lower-bound/construction direction of the theorem — not re-derived here — that the
dyadic partition achieves e = 1/7 exactly against XY's best response). Hence
**g is strictly smaller at every other point of this neighborhood than at the dyadic
point** — a clean, rigorous LOCAL uniqueness result for n=2, Case (ii), near the
dyadic point.

### What remains open (honest gaps)

1. **Global coverage of Case (ii).** The argument above is valid only where the
   branch conditions a1≥1/2 and a1/2≥a3 hold. Extending h's formula (with the
   complementary branches of f2 and f1) and re-running the same convex-hull
   argument over the *entire* Case (ii) region (down to a1 as small as a2, and a3
   up to a2) has not been done; it is a finite, bounded extension of the same
   method (a handful more branch cases, each still a 2-parameter affine-min
   problem) but was not completed this round due to time.
2. **The a2 vs a3 ratio.** This round's computation only pins down the a1/a2=2
   condition (Case ii is defined by the a1 vs a2 ratio). The symmetric argument
   that a2/a3 must also equal 2 (recursively) has not been carried out; it is
   expected to follow a similar but not identical pattern (the "residual" after
   peeling a1 is itself a 2-piece problem for a2,a3 alone, which may need its own,
   simpler, exchange lemma).
3. **Import of g(dyadic)=1/7 exactly.** This is the "no XY response beats e=1/7 at
   this specific point" fact, which is part of the theorem's lower-bound direction
   (shared prerequisite with `dyadic-cascade-induction`'s Case (i)/(ii) closure).
   It was independently sanity-checked here against 15 candidate patterns (Step B)
   all giving ≥1/7 at the dyadic point, which is consistent evidence but not a
   proof that literally no pattern beats it (the tie-or-degenerate lemma narrows
   XY's search space to ties/bisections, but there remain infinitely many
   *multi-level* tie chains — e.g. tying a piece to *another newly created* tied
   piece — that have not been exhaustively ruled out for this specific point,
   though intuitively unlikely to help further since 1/7 is the known/conjectured
   game value).
4. **General n.** Per this round's explicit safety instruction, no attempt was made
   to generalize the n=2 computation to general n; this is the natural next
   milestone (n=3, 4 free parameters, following the same tie-or-degenerate +
   concave-min-of-affine-functions method) but is out of scope for this round.
5. **Boundary/degenerate cases** (fewer than n+1 = 3 distinct positive pieces, i.e.
   a3=0 or a2=a3) are not yet addressed; expected to be handled by a short
   separate monotonicity argument ("more pieces weakly helps LB") per the original
   outline, not yet written up.

## Full proof
(not present — status is not solved; see Current best for the exact scope of what
is rigorously established: local uniqueness of the dyadic point within a
neighborhood in Case (ii) for n=2, conditional on one imported fact from the
lower-bound direction.)

## Promotable lemmas

- **Tie-or-degenerate lemma (Step A above).** Statement: for XY optimizing a single
  cut position t∈(0,ℓ) splitting a background piece of length ℓ into (t,ℓ−t), with
  all other pieces fixed, the value L(t) (sum of odd-ranked pieces) is piecewise
  linear with slope in {−1,0,1}, constant between consecutive points where t, or
  ℓ−t, crosses another current piece's value or where t=ℓ−t; consequently XY's
  optimal cut position is always at such a "tie" point or degenerates to an unused
  cut (t→0 or t→ℓ). Proved in full in Step A above (no gaps). This is a general
  fact (holds for any n, any background multiset), reusable by any approach that
  needs to justify restricting XY's response search to "matching/bisecting" moves
  instead of a continuum of cut positions — in particular it rigorously justifies
  why the outline-reviewer's flagged "double match" and "match-then-bisect" move
  families are legitimate (they are literal two-fold applications of this lemma)
  and not exceptions requiring separate treatment.
- **Min-of-affine-functions strict-uniqueness criterion (Step C above).** Statement:
  if h = min(f1,...,fk) with each fi affine on R^2, and at a point x0 the active set
  (fi(x0)=h(x0)) has gradients whose convex hull contains 0 in its *interior*, then
  x0 is the unique global maximizer of h. Standard convex analysis, but the
  worked derivation of the specific 2/7,1/7,4/7 convex-combination certificate for
  this problem's f1,f2,f3 at the dyadic point (Step C) is a reusable, concrete
  computation any other approach invoking a similar concavity/minimax structure
  (e.g. `concavity-minimax-duality`) could import directly rather than re-deriving.
