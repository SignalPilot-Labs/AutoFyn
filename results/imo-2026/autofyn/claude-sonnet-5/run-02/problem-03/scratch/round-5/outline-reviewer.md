## imo-2026-03 — round 5 outline review

### Context check
current.md confirms the crux gap after round 4 is exactly the domination /
anti-concentration inequality (*) (equivalently claim (A)+(B) below), and that
`cascading-halving-family-characterization`, `general-n-cascade-achievability`,
`sharp-dominant-removal-identity`, `tail-self-similarity`,
`symmetric-split-c1-lower-bound`, `vertex-minimum-theorem`,
`odd-run-reduction-lemma`, `pair-cancellation-identity` are all certified and
reusable. All five outlined approaches correctly cite these rather than
re-deriving. `run_state.md` Rules confirm: the false peel-recursion
`c(n)=p+c(n-1)(1-p)` is a permanent dead end, and `induction-first-move-reduction`
was never registered.

---

### greedy-halving-adversary — advance — **CHANGES REQUESTED**
Sound continuation. Targets claim (B) (tail-refinement-never-helps) via a
surrogate-undo argument, correctly imports the certified
`sharp-dominant-removal-identity` / `odd-run-reduction-lemma` /
`tail-self-similarity` rather than re-deriving. The mechanism (undo one tail
cut at a time, finite induction on cut count, each undo step justified by
tail's own (n-1)-ladder self-similarity) is a legitimate proof strategy, not
circular. Open gap (the surrogate-undo inequality itself) is honestly flagged
as unproved-only-numeric — correctly not oversold. The "Watch out for" note
(claim (B) must hold for *every* F, not just the assumed-optimal one, unless
proved monotone) is the right thing to be worried about; make sure the
builder actually addresses this rather than silently fixing F.

### rank-pigeonhole-budget — advance — **CHANGES REQUESTED**
Targets claim (A) via an explicit band-decomposition of `A(F∪T)`. The
skeleton is plausible (peel bands by `sharp-dominant-removal-identity`,
matches Case A's known collapse), but step 2 (the band decomposition formula
for general partition shapes of F within a band) and step 3 (the
minimization itself) are both explicitly un-derived, only sketched. This is
weaker than greedy-halving-adversary's specificity but is a fair claim(A)
attempt — approve to proceed, but the builder must actually derive the
band formula in step 2, not just assert it "collapses like Case A."

### rank-tie-vertex-reduction — advance — **CHANGES REQUESTED**
Targets the domination/uniqueness claim via vertex enumeration, guided by a
genuine exhaustive n=3,4 computational finding (every winning vertex reduces
to `R_{n-1}` after removing padding). The "un-tie/re-tie" reduction move
(step 2) is the right kind of mechanism (local swap justified by
`odd-run-reduction-lemma` + `pair-cancellation-identity`), but its
termination/potential-function argument is not yet pinned down and the
finding is n=3,4 only (n≥5 timed out) — flag this explicitly to the builder:
do not claim the induction is "clearly" going to generalize past n=4 without
either a genuine potential function or a structural (non-enumerative)
argument.

### dyadic-band-occupancy — new — **APPROVE** (registered)
A genuinely different lever (generating-function/step-function band
counting, coarser than rank-pigeonhole-budget's per-band decomposition) for
claim (A). Correctly flagged by its own outline as needing a hand-check for
n=2,3 before committing to the general derivation — good discipline, keep
that gate as a first build step. Real technical risk (both key lemmas
undeclared in full generality) but worth a build slot given it's the one
approach in this round attacking with non-LP machinery. Watch-out note about
possibly collapsing into rank-pigeonhole-budget is correctly self-aware;
if the builder finds this, it should report it rather than silently
duplicate effort.

### induction-first-move-reduction — revise — **RETHINK, not registered**
This is the approach flagged for extra scrutiny, and it fails scrutiny: its
"achievability, no further recursive algebra needed" claim (step 2) is
**factually false as stated**, and the falsification is the same *category*
of error as the round-1 dead end (a false one-move shortcut), not merely
superficially similar naming.

Verified directly (exact-Fraction computation, script below):
```
R_k(n) defined per cascading-halving-family-characterization:
  cut p_1,...,p_k each into two copies of the next rung, leave p_{k+1..n+1} untouched.
n=3: k=1 (bisect ONLY p_1) gives A = 1/5   ≠ target a_3 = 1/15
     k=2 (= R_{n-1}, cuts p_1 AND p_2)     gives A = 1/15 = target  ✓
n=4: k=1 gives 5/31, k=2 gives 3/31, k=3(=R_{n-1}) gives 1/31 = target
n=5,6: same pattern — only k=n-1 or k=n hit the target, k=1 never does for n≥3.
```
The outline's step 2 explicitly claims Xiang Yu spends "*exactly one* unit
of budget as a symmetric bisection of `p_1`... never more real cuts on
`p_1`" and that the resulting multiset "`{p_2,p_2,p_3,...,p_{n+1}}`" **is**
`R_{n-1}`. Two compounding errors:
1. Bookkeeping: bisecting `p_1` alone (one cut) merges with the *untouched*
   tail `T ∋ p_2`, giving `p_2` at multiplicity **3** (two halves + the
   tail's own `p_2`), not multiplicity 2 as written — this is exactly `R_1`
   in the certified family's own notation, not `R_{n-1}`.
2. Substance: `R_1` (one cut, k=1) only hits the target when `L=n-k=n-1∈{0,1}`,
   i.e. `n≤2`. For `n≥3` it is *strictly larger* than `a_n` (confirmed above:
   n=3 gives 1/5 vs target 1/15) — so "one bisection of `p_1`, tail
   untouched" is simply **not** an optimal/achieving Xiang Yu response for
   n≥3. Reaching the actual `R_{n-1}` vertex requires cutting `p_1` through
   `p_{n-1}` — i.e. spending `n-1` of Xiang Yu's `n` cuts, the full cascade —
   which is exactly the recursive content the outline claims to have
   eliminated ("no further recursive algebra is needed on the achievability
   side").

This is not a cosmetic labeling slip to wave through with a one-line
correction: the entire selling point of this approach ("achievability is
direct substitution, only domination needs induction") rests on the false
claim that one cut suffices. Once corrected to say achievability is via the
*full* R_{n-1} cascade (which IS legitimately non-recursive, since
`general-n-cascade-achievability` already proves it in closed form for
every n directly) — that citation is fine and the achievability half is
actually already closed, just not by the mechanism described. But as
written the step is wrong, and given this is explicitly the same failure
mode (a false "single first move settles it" shortcut) that got the round-1
version of this exact slug name refused, I am not willing to wave it through
as a fixable typo under time pressure. **Do not register or build this
slug this round.** Send back to the outliner with the exact fix required:
replace step 2 with "Xiang Yu's achieving response is the full `R_{n-1}`
cascade (cut `p_1,...,p_{n-1}`, using `n-1` of his `n` cuts) — already
proved to hit `a_n` exactly, non-recursively, via the certified
`general-n-cascade-achievability`; the domination lemma (step 3) remains
the only open content, identical to the sibling gap." If the outliner
re-submits with that fix next round, it can be evaluated fresh (not
poisoned by this round's error) — but it should not be assumed to add any
independent value beyond re-packaging the same domination lemma every other
approach in this round is also chasing.

---

### Diversity note (shared-gap plateau)
Four of the five outlined approaches (greedy-halving-adversary,
rank-pigeonhole-budget, rank-tie-vertex-reduction, and the rejected
induction-first-move-reduction) are now explicitly converging on the *same*
domination/anti-concentration fact, stated three different ways. This is
consistent with `run_state.md`'s Next-note calling round 5 a legitimate
"converging round," and I agree it's appropriate for one more round given the
gap is now sharply localized and each approach owns a genuinely different
sub-piece or mechanism (integral surrogate-undo vs. band decomposition vs.
vertex un-tie/re-tie). `dyadic-band-occupancy` is the only approach this
round attacking with a materially different technique (generating-function
counting vs. LP-vertex machinery). **If round 6 still has not closed (*) or
the domination lemma, escalate per the shared-gap-plateau rule**: put a
genuinely far-from-the-field approach on the table (e.g. a bijective/
injective mapping argument or a direct induction using a stronger
multi-parameter invariant), not another variant of vertex/band/integral
accounting on the same target fact.

---

### Ranking
Registered `dyadic-band-occupancy` (cold-start 1500 → 1513.8 after
comparisons). Ran 10 head-to-head comparisons anchoring the newcomer against
established siblings and refreshing stale flags on all four advanced
approaches. Post-round elo (best-first):
1. greedy-halving-adversary — 1603.8
2. rank-tie-vertex-reduction — 1575.1
3. rank-pigeonhole-budget — 1530.4
4. dyadic-band-occupancy — 1513.8 (new)
5. exchange-argument-extremal-response — 1469.6
6. claiming-order-invariant — 1447.8 (dead-end)
7. self-similar-bracketing — 1447.7
8. self-similar-potential-certificate — 1447.5
9. integer-lattice-reduction — 1373.7 (never built)

(`smoothing-compactness-certificate`, the approach owning the general-n
*upper*-bound direction, was not touched by this round's outline and so not
re-ranked here; it remains live in the population at its prior elo and
should be picked up again once the lower-bound domination lemma closes or a
round is free to revisit the upper bound.)

---

build set: greedy-halving-adversary, rank-tie-vertex-reduction, rank-pigeonhole-budget, dyadic-band-occupancy
