# Proof review — imo-2026-03, round 3

Reviewed three built slugs independently, per CLAUDE.md's per-approach
routing (not one verdict for all three). Also read all prior lemma files in
`results/imo-2026-03/lemmas/` and `current.md` for context, and cross-checked
the two independently-derived "vertex" theorems against each other and
against the one concrete $n=3$ example on file.

---

## 1. `self-similar-bracketing`

**Status (self-reported): partial. Reviewer agrees.**

**What's actually proved (Lemma B1):** the rescaled-ladder Xiang-Yu strategy
at $c=n$ (fragment $p_1$ into a rescaled copy of the whole $n$-ladder, leave
the tail untouched) produces a final multiset whose sorted order is the exact
alternation $q_1>p_2>q_2>\dots>p_{n+1}>q_{n+1}$, giving $\Phi=p_1(n)$ exactly.
I re-derived both numerator inequalities from scratch:
- $q_i-p_{i+1} = 2^{n-i}/D>0$ (trivial),
- $p_{i+1}>q_{i+1}\iff 2^{n+1}-1>2^n\iff 2^n>1$ (true for all $n\ge1$).

Both check out with no hidden step; the parity/position bookkeeping ($q_i$ at
odd rank $2i-1$, $p_{i+1}$ at even rank $2i$) is correct and I verified it
against the file's own $n=2$ numeric example ($q=(16,8,4)/49$, tail
$(14,7)/49$, sorted $16>14>8>7>4$ — matches). **This lemma is correct and
gap-free.** Certified as `lemmas/rescaled-ladder-c-equals-n-achievability.md`.

**The claimed self-correction (Proposition B2) — verified correct.** The
approach argues that Lemma B1 only shows the $c=n$ min is $\le p_1$
(achievability); the matching lower bound ($\ge p_1$, i.e. minimality) is
*not* a free corollary of "it's the other extreme from $c=0$" — applying the
certified `cross-term-identity-threshold` at the fixed threshold
$r(n)=\mathrm{Total}(\text{tail})$ shows dropping the (always $\ge0$) cross
term is insufficient for the same structural reason
`greedy-halving-adversary`'s Proposition 10 already found insufficient for
general $c$ (nothing stops $A(F)$ from being pushed toward its own trivial
max while the cross term stays small). I checked this reasoning line by line;
it is a valid diagnostic argument (not a rigorous impossibility proof, and
the file does not claim it is one — it correctly claims only "this is not an
easier sub-problem"). **This correction is real and important**: the round-3
outline's premise ("both endpoints are easy, bracket the interior") is false.
The reused $n=1,2$ minimality closures (citing `greedy-halving-adversary`'s
direct $n=1$ computation and `smoothing-compactness-certificate`'s
`(2,0,0)` composition for $n=2$) are correctly cited — I independently
confirmed the `(2,0,0)` case in `smoothing-compactness-certificate.md` gives
$\Phi\ge4$ in every sub-case with equality only in case `(1,1,1)`, consistent
with what's claimed here.

**Gap:** the approach's actual target — the interior $1\le c\le n-1$ — has
**zero new progress**. No invariant (outline Step 3) or exchange/monotonicity
argument (Step 4) was found or even precisely stated. Worse, the approach's
own Proposition B2 shows the underlying bracketing *strategy* rests on a
false premise (the endpoints are not both "free"), which is a structural
problem with the outline, not just an incomplete step.

**Verdict: CHANGES REQUESTED**, with a strong recommendation that the next
round's outliner re-plan this slug's framing rather than simply push forward
on Steps 3/4 as originally conceived — the endpoint-bracketing idea itself is
now shown to be at least as hard as the general problem. (Recorded as
outcome "partial" via the ranker, with this framing caveat in the note,
since CLAUDE.md's RETHINK/CHANGES-REQUESTED split hinges on whether the
approach can still work "as set up" — Lemma B1 is a genuine, reusable
contribution, so the slug is not dead, but its core strategic premise needs
revision.)

---

## 2. `rank-tie-vertex-reduction`

**Status (self-reported): partial. Reviewer agrees.**

**Vertex-Minimum Theorem — verified correct, no gap found.** I checked each
step: (a) $\bar\Omega$ (product of closed simplices) is compact; $\Phi$ is
continuous as a composition of an affine map, the sort map (continuous —
each order statistic is a finite max-of-mins of continuous coordinates), and
a linear functional — correct. (b) On each open cell of the hyperplane
arrangement the sorted permutation is locally constant, so $\Phi$ restricted
to the cell is a fixed affine combination of coordinates; the
density-plus-continuity argument correctly extends this to the closed cell
(this step is done more carefully here than in the sibling
`exchange-argument-extremal-response`, which asserts affineness on the
closure with less justification — same conclusion, less rigor shown). (c)
Minimum of an affine function on a polytope at a vertex, and every vertex
pinned by $d$ independent type-(I)/(II) constraints — standard convex/LP
geometry, correctly invoked. No gap.

**Odd-Run Reduction Lemma — verified correct.** I re-derived the one-step
adjacent-pair-cancellation argument independently: two adjacent equal copies
at sorted ranks $r,r+1$ contribute $(-1)^{r+1}w+(-1)^{r+2}w=0$, and removing
them shifts every later rank down by $2$ (preserving sign parity), so $A$ is
unchanged; iterating collapses each value's run to its odd-multiplicity
leftover. I additionally ran a 20000-trial exact-`Fraction` script
independently confirming $A(S)=A(S')$ for random multisets with repeated
values — zero mismatches. This is a genuine, correct strict generalization
of `leftover-formula` (recovers it exactly when at most one value is odd).
Certified as `lemmas/odd-run-reduction-lemma.md`.

**Worked $n=3$ example — verified correct**, and I cross-checked it
independently against `exchange-argument-extremal-response`'s hand
computation of the *same* instance (composition: 1 cut on $p_1$, 1 cut on
$p_2$, $p_3,p_4$ untouched, vertex $a=p_2,b=p_4$): both reduce the same
multiset $\{4,4,3,2,1,1\}$ (units $1/15$) to leftover $\{3,2\}$, giving
$A=1=15a_3$ — exact match between two independently-built approaches. This
is a strong, genuine cross-check, not just self-consistency.

**Negative finding (outline's Step-4 recursion) — verified as a real,
correctly-argued refutation**, not overclaimed: the claimed vertex ties
$p_1$'s fragment directly to $p_2$ (a cross-generational tie), not a clean
top/tail split, so the natural "self-tie + rescaled sub-vertex" induction
does not apply to this instance as stated. Correctly flagged as a scheme not
to re-attempt verbatim, not as "the enumeration is impossible."

**Gap:** the actual enumeration of feasible tie-vertices for the ladder's
specific values, general $n$, is untouched this round (honestly reported as
such). This is the main remaining gap and matches what the other approaches
converge on.

**Verdict: CHANGES REQUESTED.** Two new, fully rigorous, general-purpose
lemmas were produced and are certified; the approach's core machinery is
sound; the target enumeration is real, unfinished work for a future round.

---

## 3. `exchange-argument-extremal-response`

**Status (self-reported): partial. Reviewer agrees.**

**Lemma E1 (minimizer exists) — correct**, routine compactness + continuity,
no issues.

**Lemma E2 (pair cancellation) — correct**, and I verified it independently
via the parity-of-$N_S(x)$ argument (adding $\{a,a\}$ changes $N_S(x)$ by an
even amount $0$ or $2$ for every $x$, hence doesn't change the parity that
$A$ depends on by `integral-alternating-sum-formula`). Ran a 20000-trial
`Fraction` check — zero mismatches. Certified as
`lemmas/pair-cancellation-identity.md`.

**Theorem E3 (vertex reduction) — correct in substance**, essentially the
same claim and proof idea as the sibling's Vertex-Minimum Theorem (same
standard convex-polytope/LP-vertex mechanics), though the writeup here is
slightly less careful about the open-cell-to-closed-cell extension (asserted
rather than justified via the continuity/density argument the sibling gives
explicitly) — a minor exposition gap, not a substantive error, since the
underlying fact is true and the sibling's proof covers it. Not counted as a
blocking issue since the fact itself is independently verified correct by
the parallel derivation.

**Corollary E4 — honestly flagged its own gap** (does the $k$-tie vertex
always decompose into a disjoint perfect matching of pairs, or can genuine
multi-way ties break the clean cancellation?). **Reviewer finding: this gap
is already closed** by the sibling `rank-tie-vertex-reduction`'s Odd-Run
Reduction Lemma, which handles *any* multiplicity pattern, not just disjoint
pairs, with no extra bookkeeping needed. This should be imported directly
next round rather than re-derived — flagged prominently in `current.md`.

**Worked $n=3$ verification — correct**, and matches the sibling's
independent computation of the same instance exactly (see above).

**Gap:** general enumeration for arbitrary $n$, and the general upper bound,
both untouched — honestly reported as open, no overclaiming.

**Verdict: CHANGES REQUESTED.** Genuinely different technique (fix a
minimizer + LP-vertex geometry, no global integral formula) from the
measure-theoretic field, reaching the same underlying wall independently —
consistent with, and a good example of, CLAUDE.md's "different framing, may
fail for its own reasons" expectation. Two new lemmas certified
(`pair-cancellation-identity`; the vertex-reduction theorem itself merged
into the shared `vertex-minimum-theorem.md` alongside the sibling's version,
since they are the same fact proved twice, independently).

---

## Lemmas certified this round

- `lemmas/vertex-minimum-theorem.md` — merges `rank-tie-vertex-reduction`'s
  Vertex-Minimum Theorem and `exchange-argument-extremal-response`'s Lemma
  E1/Theorem E3 (same fact, two independent proofs, cross-verified on a
  shared $n=3$ instance).
- `lemmas/odd-run-reduction-lemma.md` — from `rank-tie-vertex-reduction`,
  strictly generalizes `leftover-formula`.
- `lemmas/pair-cancellation-identity.md` — from
  `exchange-argument-extremal-response`, the elementary building block
  underlying the Odd-Run lemma.
- `lemmas/rescaled-ladder-c-equals-n-achievability.md` — from
  `self-similar-bracketing`'s Lemma B1 (achievability only; explicitly
  scoped to exclude the unproved minimality direction).

`current.md` updated to integrate all six approaches (three round-1/2 plus
these three round-3 builds) without erasing prior content.

## Goal Progress

Status remains `partial`; $n=1,2$ fully closed both directions (unchanged
milestone from round 2). Round 3 adds two independently-proved, certified,
general-purpose structural theorems (vertex-minimum + odd-run reduction) that
convert the general-$n$ lower bound from a continuum optimization into a
finite (but not yet characterized) vertex-enumeration problem, reached
independently by two genuinely different routes, plus a corrective finding
(self-similar-bracketing) that closes off a previously-assumed-easy shortcut
(the $c=n$ endpoint is not actually free). No approach reached `solved` this
round; four independent framings (cross-term bound, bracketing,
rank-tie-vertex, exchange-argument-vertex) now converge on the same
underlying combinatorial enumeration/anti-concentration wall for general
$n\ge3$ — increasingly strong evidence the remaining gap is a genuine open
combinatorial fact, not an artifact of any one approach's method.
