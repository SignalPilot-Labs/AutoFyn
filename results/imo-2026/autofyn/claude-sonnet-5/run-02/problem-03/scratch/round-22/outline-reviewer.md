# Outline-reviewer report — round 22

Read `/tmp/round-22/proof-outliner.md`, the "Round 22 outline" sections
appended to all three live approach files, and `current.md`'s certified
state (round-21 recap: Theorem 34's corrected identity, `rank-pigeonhole-
budget`'s verified-milestone §7.5 n=3 closure of the true ε-corrected
target, and the reviewer-flagged Theorem 35b algebra bug in
`greedy-halving-adversary`). No new approach was opened this round; the
outliner kept all three live slugs, advancing each in place. All three
outlines pass review — none doomed, none circular, no missing cases
glossed over. Field stays at 3.

## 1. `greedy-halving-adversary` — Theorem 35b algebra fix: VERIFIED CORRECT

Checked the claimed one-line fix directly. By definition $f(m)=1/(2^{m+1}-1)$
and the file's own $D_{n-3}:=2^{n-2}-1$ (line 3944), so
$f(n-3)=1/(2^{(n-3)+1}-1)=1/(2^{n-2}-1)=1/D_{n-3}$ **exactly**. Hence
$D_{n-3}\cdot f(n-3)=1$ identically — the fix (dropping the false
$2^{n-3}$ numerator, concluding $A(T')\ge f(n)$ with no extra factor and
no need for `tail-self-similarity`'s cross-level identity) is correct
algebra, not a hand-wave.

Checked for silent downstream reliance on the old, stronger, false bound:
grepped the whole file for `D_{n-3}` and `f(n-3)` — the only three
occurrences are all inside the now-fixed Theorem 35b passage itself (proof
line, the fix annotation, and the fixed conclusion). Theorem 35a$'$ (which
the outline claims cites Theorem 35b's sub-range 2) and the "Status of Case
(a)" recap do not independently re-derive or restate the false factor
anywhere — confirmed by direct reading, not just the file's own claim.
**No downstream citation site relied on the stronger false bound.** Item 1
is closed as claimed.

The round-22 forward target (Theorem 36 Case (b), $n\ge5$, induction-tower
reframing) is a genuine, non-circular next step, correctly distinguished
from Theorem 35b's fixed argument (explicitly flagged as a two-level drop,
not a same-level identity, so the builder is told not to pattern-match).
The secondary target (verify $\epsilon(v)\equiv0$ on Theorem 35b's own
range) is cheap and well-scoped, with round-21's explicit caveat honored
(not assumed, flagged for a one-line check). Sound outline.

## 2. `rank-pigeonhole-budget` — redirect: SOUND, NON-CIRCULAR SCOPE-DOWN

The claimed algebraic identification (substituting Theorem 34 (corrected)'s
$s-p_2=-f(n)$ into this file's own $(\sharp')$ reproduces sibling's
$(\Diamond')$ term for term) is a real, checkable equivalence, not an
assumption — and the outline correctly does **not** claim closure from it
this round, since the sibling's own fix (Theorem 35b/36 extension) isn't
finished yet. This is the load-bearing distinction: claiming §7.6 closes
now would be circular/premature (borrowing an unfinished result as if
already discharged); scoping it as "write the conditional corollary now,
close it later" is exactly right and matches CLAUDE.md's rigor rules
("prove, don't conjecture"). The two concrete deliverables (§7.7 corollary
stub, independent $n=4$ numeric cross-check) are both genuinely new,
cheap, and not a re-attempt of the already-shown-weaker §7.6
vertex-enumeration route — the explicit "do not re-attempt §7.6" instruction
is correctly grounded in this round's own finding (algebraic-floor route is
the one that has actually closed instances), not asserted from nowhere.
No circularity found.

## 3. `lp-duality-certificate` — $p$-space Chamber-Vertex Theorem: SOUND MECHANISM, ONE UNFLAGGED SUBTLETY

The core mechanism — $\Phi_{\min}$ affine on chamber $U$ (via the already-
certified `within-chamber-affinity-theorem`) $\Rightarrow$ minimized on a
polytope at a vertex — is a standard, valid fact (linear/affine functional
on a compact convex polytope attains its extremum at an extreme point);
citing `vertex-minimum-theorem`'s underlying convex-geometry fact by name
rather than re-deriving it is appropriate reuse, and the outline correctly
does *not* claim the theorem transfers verbatim (new constraint set (a)/(b)/
(c), explicitly built from scratch). The type-optimality condition (c)'s
own dependency on *every neighboring type's* $M(\tau')$ invertibility is
explicitly flagged as an inherited hypothesis, not silently assumed — good,
this is exactly the kind of leap CLAUDE.md's rigor rules forbid glossing
over, and the outline doesn't.

**Boundedness/closedness — checked directly, per the assigned task.** The
outline does *not* simply assume $U$ itself is bounded; it explicitly works
with $U\cap\mathrm{Box}$, correctly recognizing $U$'s own defining
half-spaces (a)/(b)/(c) don't by themselves bound $p$. This is the right
instinct. However: (i) $U$'s defining inequalities as stated are all
non-strict ($\ge$, $\le$), so $U$ is closed — fine. (ii) But "Box" itself,
as defined elsewhere in this file for case (b2) (line ~4077:
`$T/D_n<p_2<a_nT/2$, $p_1<T/2$`), uses **strict** inequalities — an open
set. $U\cap\mathrm{Box}$ with an open Box is **not** guaranteed compact or
even closed, so "every extreme point... is pinned by tight instances of
(a)/(b)/(c)... or a Box wall is hit" is imprecise as stated: a Box wall
under strict inequalities is never actually *attained* inside the open
region, only approached. This doesn't kill the mechanism (the standard fix
— work with the closure $\overline{\mathrm{Box}}$, prove the affine
inequality there including its now-attained boundary, then note by
continuity it holds on the open interior too, with boundary points
corresponding to degenerate/adjacent cases (b1)/(b3) handled elsewhere) but
the outline's own Concrete build steps (1–4) don't spell this out — it is
exactly the kind of "quietly assumes closed/bounded" gap the task asked to
flag. **Recommendation for the builder, not a blocker for this round's
outline:** when Step 1 writes out the explicit inequality list, use the
closure of case (b2)'s box (non-strict inequalities) for the vertex
argument, and treat the strict-inequality boundary explicitly as "shared
with an adjacent case, not a new case" rather than leaving it implicit.
This is a fixable precision issue, not a fatal flaw — Target 1 stays in the
build set, with this flagged as a required precision fix during the build.
Target 2 is correctly scoped as a numeric conjecture test, not a proof, with
an honest negative-finding instruction if it fails — sound.

## Ranking

No new approach registered (field unchanged: 3 slugs). Ranked head-to-head
against last-recorded (round-21) outcomes via `update_ranking`
(clears `stale`, which all three carried): `rank-pigeonhole-budget`
(verified-milestone, unconditional $n=3$ closure of the true target) beats
both siblings; `greedy-halving-adversary` (real bug found+fixed, partial
progress) beats `lp-duality-certificate` (conditional theorem only, no
closure this round). Resulting Elo: `rank-pigeonhole-budget` 1789.0,
`greedy-halving-adversary` 1699.1, `lp-duality-certificate` 1542.7.

## Build set

All three outlines are sound, non-circular, and target genuinely different
terrain (Theorem 36 induction-tower extension; conditional corollary +
independent numeric cross-check; new $p$-space vertex theorem with a
flagged precision fix for the builder). Dispatch one proof-builder per slug.

build set: greedy-halving-adversary, rank-pigeonhole-budget, lp-duality-certificate
