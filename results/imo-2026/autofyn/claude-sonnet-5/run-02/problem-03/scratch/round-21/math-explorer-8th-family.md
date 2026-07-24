## imo-2026-03 — 8th-mechanism scouting for case (b2)

### Terrain recap (what's confirmed, what's still open)

Case (b2) := the box `T/D_n < p2 < a_nT/2` (with `p1<T/2`) in the general
upper-bound target `c(n)<=a_n` for arbitrary Liu Bang markings. This is the
sole remaining open region after case (a) (`p2>=a_nT/2`, closed via Theorem
B recursive sufficient condition) and case (b1) (`p2<=T/D_n`, closed via the
Max Domination Lemma). Case (b2) has **7 confirmed-dead mechanism
families** on file (verified each is a real, reasoned dead end, not just an
unlucky attempt — see "What NOT to retry" below).

Both fronts of the whole problem (front 1 = lower bound / Claim B, front 2 =
case (b2) / upper bound) now bottom out on some form of **vertex
enumeration**: front 1 needs an upper bound on `A(S_{>v})` over legal
responses `S`, evaluated at LP-polytope vertices; front 2 needs, for
*every* marking `p` in the box, at least one legal Xiang-Yu vertex response
with `Φ<=a_nT`. The standing machinery (`vertex-minimum-theorem`,
`per-piece-vertex-decomposition-theorem`, `odd-run-reduction-lemma`) already
proves: for **fixed** `p`, `Φ_min(p)` is attained at a vertex of Xiang Yu's
response polytope, and at that vertex every fragment coordinate is an
**affine function of `p`** (Cramer's rule on the tie/zero linear system).
This fact is proved and certified but has only ever been *used* pointwise
(one `p` at a time, or to characterize Xiang Yu's freedom) — nobody has yet
exploited it as a fact about how `Φ_min` varies **as `p` itself varies**.
That's the opening below.

### Candidate mechanism 1 (primary): Local-Concavity / Chamber-Vertex Maximization over Liu Bang's own marking `p`

**Why this is genuinely different from the two already-dead "vary `p`"
mechanisms (Danskin/concavity, boundary-continuity):**

- Danskin/concavity (dead, round 18) tried to prove `g(t) = Φ_min(p1,p2,t)`
  is **globally concave** as Liu Bang's own free tail marking `t` varies
  continuously, holding `p1,p2` fixed — refuted by an explicit V-shaped
  interior local minimum at `p3=p1-p2` (matching ∓1/2 slopes both sides).
  The refutation is a genuine non-concavity **across a chamber boundary**
  (the point `p3=p1-p2` is exactly where Xiang Yu's optimal response
  switches combinatorial type).
- Naive boundary-continuity (dead) tried to propagate the already-closed
  case (a)/(b1) boundary values into case (b2) by continuity alone, with no
  slack to work with.
- **What's actually true, and unused:** within a single **fixed chamber**
  (i.e. a maximal region of `p`-space over which Xiang Yu's optimal
  response has one fixed combinatorial tie/zero pattern — the same vertex
  "type" from `vertex-minimum-theorem`), the value `Φ_min(p)` restricted to
  that chamber IS exactly affine in `p` (it's the vertex-coordinate formula
  from `per-piece-vertex-decomposition-theorem`, composed with the
  certified `odd-run-reduction-lemma` evaluation — both already proved,
  ladder-agnostic). An affine function on a chamber is trivially concave
  *on that chamber*; the failure Danskin found is a **cross-chamber**
  phenomenon (the V-shape sits exactly at the wall between two chambers),
  not a failure of local affinity within one chamber. This is a much
  weaker, essentially free claim compared to Danskin's global concavity —
  it needs no new inequality, only bookkeeping of which linear system
  Cramer's rule uses.

**The concrete new mechanism:** for the purpose of bounding
`sup_{p in case(b2) box} Φ_min(p)`, decompose case (b2)'s box into the
(finitely many, since determined by the same finite hyperplane arrangement
already certified to exist) chambers of the `p`-space arrangement. On each
chamber, `Φ_min(p)` restricted to that chamber is affine in `p`, so its
**maximum over (chamber ∩ box)** is attained at an extreme point of that
intersection — a point where either (i) `p1=T/2`, `p2=T/D_n`, or
`p2=a_nT/2` (a case-(b2)-box facet) is tight, or (ii) two of the chamber's
own defining tie/zero constraints on Xiang Yu's response become
degenerate/coincide (a chamber-wall vertex). **This reduces "bound
`Φ_min(p)` for every `p` in a continuum box" to "check `Φ_min(p*)<=a_nT` at
a finite (if large) list of explicit second-order vertices `p*`"** —
exactly the same style of reduction the vertex-minimum-theorem already gave
for Xiang Yu's response, applied one level up to Liu Bang's own marking.
This is a genuinely different top-level target than any of the 7 dead
mechanisms: it is not an explicit-strategy construction (peel/bisect), not
a weighted combination of strategy values, not a constraint-side LP dual,
not a global smoothness/derivative argument, and not a probabilistic
wrapper. It is a **local convexity + extreme-point** argument, composing
already-certified machinery in a way nobody has tried.

**Structural evidence this is the right target, not a dead end in
disguise:** the two known near-tight case-(b2) witnesses on file (round
14/15's `n=3` "flat-face" witness and `n=4` "pinned-tie" witness) are
*already* described in the approach file as sitting on a flat face / at a
pinned tie — i.e., they already look like chamber-boundary points, not
generic interior points. That is consistent with the chamber-vertex
maximization framing: if the true global sup over the whole box is attained
at such boundary points (as the local-affine-on-chambers structure would
predict), the existing hard witnesses are exactly where this new mechanism
would look first.

**What still needs to be built (gaps for the outliner, not attempted
here):** (a) a rigorous general argument that the case-(b2) box intersected
with a chamber is itself a polytope with finitely many vertices — should
follow directly from `per-piece-vertex-decomposition-theorem`'s hyperplane
description, but needs writing out; (b) a bound on *how many* chamber
vertices exist as a function of `n` (this is the real risk — if it's
exponential in `n` with no further structure, this only converts one hard
enumeration into another, "easier in kind" but not obviously "easier in
size"); (c) an actual evaluation of `Φ` at the resulting vertex family
against `a_nT`, which is where the real work will be. Recommend scoping the
first build attempt to `n=3,4` explicitly (small chamber counts, matches
the two known witnesses) before attempting general `n`.

### Candidate mechanism 2 (secondary, weaker lead): Recursive/generating-function structure of the chamber arrangement itself

Distinct idea, offered as a second, less-developed opening: instead of
attacking case (b2)'s *values*, attack the **combinatorial type count** of
the chamber arrangement as `n` grows, since `D_n=2^{n+1}-1` and
`a_n=2^n/D_n` have a specific dyadic/near-Mersenne shape. If the chamber
arrangement (Liu Bang-side, per candidate 1) has a clean recursive rule as
`n -> n+1` (e.g. "insert one new smallest piece, which either merges into
an existing tie-class or creates one new chamber wall"), a generating-
function argument in `n` might let one bound `sup_p Φ_min(p)` by induction
on the *chamber count/shape*, not on inequality values — this is the kind
of technique the dispatch flagged (algebraic/generating-function methods),
and would be a genuinely different top-level target from all 7 dead
mechanisms and from candidate 1. This is much less concrete than candidate
1 — no witness or partial computation supports it yet, it is offered purely
as a structurally-motivated alternative if candidate 1 stalls. Note:
`integer-lattice-reduction`'s binary/carry mechanism is already a *confirmed
dead end*, but that was about denominators of individual vertex
*coordinates* (Rationality/D·L-denominator facts), not about counting or
recursing on chamber *types* — these are different objects, so candidate 2
is not simply a resurrection of that dead end, though the outliner should
double-check this distinction carefully before building on it (the line is
thin).

### Cheap-kill / cheap-sanity checks to run before committing to candidate 1

- Verify computationally (small `n=2,3`) that `Φ_min(p)` really is affine
  in `p` *within* a fixed chamber (should be immediate from
  `per-piece-vertex-decomposition-theorem`, but confirm no silent
  chamber-boundary crossing corrupts the check).
- Count chambers intersecting case (b2)'s box at `n=3,4` by brute enumeration
  (exact-Fraction, reuse existing R14.3/R12.5 probe scripts) to get an
  honest first read on whether the chamber count stays small (favorable) or
  explodes (would flag candidate 1 as likely too expensive to close in
  general `n`, though still useful for closing more `n` cases incrementally).
- Check whether the two known near-tight witnesses are literally chamber
  *vertices* under this framing (not just "near" a flat face informally) —
  if so, that's strong corroborating evidence this is the right target.

### Knowledge-base / crux-corpus notes

- `knowledge_base.md` has no majorization/Schur/rearrangement-specific
  entry; the closest generic entries are "Piecewise-concavity smoothing"
  (line 20) and the standard-inequalities list (AM-GM/Cauchy-Schwarz/Schur,
  line 33) — neither is a strong analog for candidate 1 (which is an
  LP/polytope-vertex argument, not a classical inequality).
- Crux corpus: searched `combinatorics` subtopics `extremal-principle`,
  `games-and-strategy`, `inequalities-SOS-and-convexity` for
  majorization/smoothing/rearrangement techniques. `aimo-0146` (exchange-
  smoothing a sorted integer sequence to a few extremal profiles, then
  hand-check) is the closest technique-level analog — **but it was already
  identified and used successfully in this project** (round 8's
  `exchange-smoothing-vertex-maximization`, applied to Xiang Yu's fragment
  multiset `F`, not to Liu Bang's marking `p`). Candidate 1 above is the
  natural "apply the same style of argument one level up, to `p` instead
  of `F`" — not a fresh corpus find, but a legitimate reuse of an
  already-validated technique family in a new place. `aimo-0197`
  ("reduce a global rearrangement constraint to a bounded-distance perfect
  matching") and `aimo-0560` ("surrogate adversary") were also checked —
  `aimo-0560` is the already-confirmed-dead surrogate-adversary family
  (round 19/`surrogate-adversary-dead-end.md`), and `aimo-0197`'s
  bipartite-matching/Hall's-theorem structure has no natural translation
  here (there is no bipartite "assignment" structure in the cake-cutting
  game). **No genuinely new corpus crux found beyond what's already on
  file**; candidate 1 is a from-scratch structural idea, not a corpus
  transplant, and should be described to the outliner as such.

### What NOT to retry (7 confirmed-dead mechanism families for case (b2), verified against source files this round)

1. **Peel/bisect/recurse-plus-full-IH** (rounds 13–14): both "peel `p1`
   vs `p2` + full IH" and "bisect `p1` + full IH" have exact zero-slack
   thresholds coinciding with or strictly inside already-closed regions —
   see `lemmas/peel-and-bisect-ih-dead-ends.md`.
2. **Weighted-combination / Convex-Combination Futility Theorem**
   (round 17): no weighting rule over any family of explicit primal
   strategy values can certify more than the plain pointwise minimum —
   `lemmas/convex-combination-futility-theorem.md`.
3. **Naive boundary continuity** (pre-round-18): propagating case (a)/(b1)
   boundary closures into case (b2) by continuity alone fails, no slack.
4. **Danskin/concavity** (round 18): global concavity of `Φ_min` in Liu
   Bang's own tail marking is false (explicit V-shaped local min at
   `p3=p1-p2`) — but see candidate 1 above, which deliberately does *not*
   need global concavity, only within-chamber affinity.
5. **Surrogate-adversary / majorization** (round 19): the worst-tail
   near-ratio-2 majorization heuristic is not a valid universal reduction
   — `lemmas/surrogate-adversary-dead-end.md`.
6. **Constraint-side LP duality** (round 19): weak duality can only ever
   certify the *wrong direction* (a lower bound on `Φ_min`, never the
   needed upper bound) — `lemmas/duality-direction-impossibility-theorem.md`.
   Note this is orthogonal to candidate 1: candidate 1 is a **primal**
   extreme-point argument (maximize `Φ_min(p)` over `p`), not a dual
   certificate, so the impossibility theorem's direction argument does not
   apply to it.
7. **Probabilistic method / randomized strategy** (round 20): the
   Convex-Combination Futility Theorem's proof generalizes verbatim to any
   probability measure including continuous ones, so `E[Φ]<=a_nT` can
   never be easier than the direct `min_x Φ(x)<=a_nT` — no rule cited
   explicitly yet in `lemmas/`, but documented in `current.md` round 20 and
   `run_state.md` Rules.

### Prior progress on front 2 (case b2), for context

Best coverage so far: `bisect-top-k-lemma` (~5–13% of witnesses),
`cross-piece-sign-assignment-identity` (closes both known specific hard
witnesses exactly), `alternating-gap-cross-lemma` (small marginal gain).
No general-`n` closure exists. Front 1 (Claim B / lower bound) is
independent and has its own open items (Theorem 35's "p3-is-cut" branch,
the ε=1 bridge-correction gap flagged by round 20's reviewer) — not this
report's focus per dispatch (routed to the p3-cut-branch explorer lens).

### Small-case / intuition notes (conjectural, not proved)

- Conjecture (from structural reasoning above, not computed this round):
  the sup of `Φ_min(p)` over case (b2)'s box, for fixed `n`, is attained at
  a `p` where at least one box-facet constraint (`p1=T/2`, `p2=T/D_n`, or
  `p2=a_nT/2`) is tight **and** Xiang Yu's optimal response has an
  additional internal tie — i.e. a genuine "corner" of the two-level
  vertex structure, consistent with both on-file near-tight witnesses being
  described as flat-face / pinned-tie configurations. This is a plausible
  but unverified prediction the outliner/builder should check computationally
  before investing in the general proof.
