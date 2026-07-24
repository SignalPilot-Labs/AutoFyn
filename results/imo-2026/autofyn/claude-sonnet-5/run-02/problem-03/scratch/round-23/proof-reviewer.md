# Round 23 proof-review — imo-2026-03

## Verdicts (per CLAUDE.md's per-approach routing)

- **greedy-halving-adversary: CHANGES REQUESTED** (partial). Theorem 37 is
  correct and honestly scoped; the "does not terminate" diagnostic is a
  real structural finding, not hand-waving.
- **rank-pigeonhole-budget: CHANGES REQUESTED** (partial, for this round's
  addendum — Claim (A) itself remains `solved`/APPROVE, untouched). The
  Single-Insert-Point Vertex Lemma is correct, general, and genuinely
  independent of the sibling's Vertex-Minimum Theorem route.
- **lp-duality-certificate: CHANGES REQUESTED** (partial). The scope
  correction is properly folded in with no residual overclaim; Chamber A2
  is a correct new building block; case (b2) at n=3 remains open.

None RETHINK, none APPROVE this round. `current.md`'s top-level `## Status`
remains `partial`.

## What I checked and how

### 1. greedy-halving-adversary — Theorem 37 + diagnostic finding
Read the full round-23 section (lines 4890–5155). Theorem 37: $B=\{a,b\}\cup
T'$ reduced to $B=\{p_4,p_4\}\cup T''$ at the symmetric-split/$p_4$-untouched
vertex, $A(B)=A(T'')$ via `pair-cancellation-identity` (correct: an exact
pair always occupies two consecutive sorted ranks, contributes 0 regardless
of parity), then $A(T'')\ge f(n)$ via `general-cross-level-rescaling-lemma`
($k=4$, so $m=n-4$: consistent index arithmetic, $\{p_5,\dots,p_{n+1}\}$ is
genuinely an $(n-4)$-ladder) plus $(\star_{n-4})$. The "unconditional for
$n\le6$" scoping is correct: $(\star_1),(\star_2)$ are the only two fully
established, unconditional $L(m)$ statements on record (both directions of
$c(1),c(2)$ — importantly, for $n=2$ *all 10* cut-distribution compositions
were closed, i.e. this really is the unrestricted $L(2)$, not just Claim
A/B's restricted sub-families). I independently re-verified Theorem 37 by
writing a fresh exact-`Fraction` script generating legal budget-respecting
refinements $T''$ (respecting per-piece boundaries and the $n-4$ cut cap) at
$n=4,\dots,8$: zero violations, tight (margin exactly 0) at $n=4,5,6,7$,
matching the file's own $n=5,6$ tightness claim and extending it. The
vertex-minimum-theorem is used only as motivation for which vertex to try —
Theorem 37 itself is proved directly and stands regardless of whether this
is the true global minimizer, and the file is explicit that it is not
claiming global minimality. This is accurate, not an overclaim.

The diagnostic ("$b$ ties with $T'$'s own max" doesn't terminate): traced
the argument by hand — if $T'$ splits $p_4$ into $(c_1,c_2,\dots)$ with
$\max(T')=c_1$, the pair-cancellation residual is $\{c_2,\dots\}\cup(\text
{rest of }T')$, which is not a rescaled ladder since $c_2$ is an arbitrary
fragment value, not one of the ladder's own breakpoints — so
`general-cross-level-rescaling-lemma` genuinely does not apply. This is a
correct, concrete structural finding, not a vague "seems hard."

### 2. rank-pigeonhole-budget — Single-Insert-Point Vertex Lemma
Read §7.8 in full (lines 1181–1330) and the certified lemma file. The
piecewise-affine-slope-$\pm1$ proof is elementary and correct (fixed sorted
rank $j+1$ on each open sub-interval between breakpoints, contributing
$(-1)^jb$; continuity extends to closed sub-intervals; a nonconstant affine
function on a closed interval attains extrema only at endpoints). I
independently re-verified this with a fresh 2000-trial exact-`Fraction`
script (random $T$, random box $[0,M]$, breakpoint-min vs. dense-sample
check): zero violations. The proof never invokes `vertex-minimum-theorem` or
any LP/compactness machinery — it is a genuinely self-contained,
single-variable argument, confirming the claimed independence from the
sibling's whole-polytope application of the general theorem. Steps 2–3
(closing $b=0$ and $b=p_4$-untouched conditionally) reach, via this
independent route, literally the same content as the sibling's Theorem 37
(Step 3 is essentially a second proof of Theorem 37) — a genuine,
non-circular cross-check in the spirit of round 3's two independent proofs
of the Vertex-Minimum Theorem, not a restatement dressed up as new. The two
residual sub-cases are honestly reported as recoupling to the same open
obstruction.

### 3. lp-duality-certificate — scope-correction + Chamber A2
Read the full round-23 build (lines 4828–5152) and the edited
`lemmas/p-space-chamber-vertex-theorem.md` in full. The scope-correction to
item 3 is done correctly: the statement itself now says only $p_2\le
T/D_n$ is unconditional for every $n$, $p_1\ge T/2$ only for $n\le3$, and
case (a) is conditional on the standing induction hypothesis — this matches
what the round-22 reviewer's correction note demanded, and the note is
explicitly marked "addressed in round 23" and folded into the main text
rather than left standing as a separate contradiction. I read both the
restated item 3 and the "Honest scope" section side by side: they are
mutually consistent, no residual overclaim.

Chamber A2: I independently re-derived the closed form
$\Phi_{A2}=(p_1+p_2)/2+p_3$ by hand from the sorted-rank assignment (tied
pair $\{p_2,v\}$ at ranks 1–2, confirming the file's own self-correction of
an earlier arithmetic slip that misplaced the pair at ranks 2 and 4) and
hand-verified the reported worst vertex $p=(2/5,4/15,4/15,1/15)$ exactly:
$T=1$, $w=(p_1-p_2)/2=1/15=p_4$ (wall W5 tight), $\Phi_{A2}=3/5$,
$g_{A2}=8/15-3/5=-1/15$ — matches the file's corrected LP run exactly. The
file's honest self-correction of its own LP wall-encoding bug (caught mid-
round) is real and properly retracted the incorrect intermediate claim
rather than leaving it standing. Case (b2) at $n=3$ is correctly reported
as not closed; the new finding that composition $(2,0,0,0)$ hosts two
distinct optimal types (Chamber A, Chamber A2) in different sub-regions,
and that neither chamber's own feasibility region is individually a
sufficient cover, is a genuine (and non-trivial, upward-revising) structural
finding, not an artifact.

## Actions taken
- Updated `results/imo-2026-03/current.md`: appended a full Round 23 entry
  under `## Approaches tried` (Status remains `partial`, unchanged).
- Recorded outcomes via `mcp__approach-ranker__record_outcome` for all three
  slugs (all `partial`, round 23).
- Certified 2 new lemma files that were described as "certified"/
  "promotable" in `lp-duality-certificate.md` but not yet written to
  `lemmas/`: `chamber-a2-p1-tied-to-p2-pair.md`,
  `feasibility-suffices-for-upper-bound.md`. Confirmed
  `single-insert-point-vertex-lemma.md` (already present) is correct as
  written — no edits needed. Confirmed `p-space-chamber-vertex-theorem.md`'s
  edit is sound and complete — no further edits needed.

## Net project state
No change to the overall `imo-2026-03` Status: `partial`. Case (b)'s "$v\ge
a$" branch of Claim (B) now has one vertex closed by two independent
routes (genuine convergence, not duplication); case (b2)'s general upper
bound remains open at $n=3$ with a sharpened (harder-than-thought) picture
of what closing it requires. All three approaches remain live and should
continue next round.
