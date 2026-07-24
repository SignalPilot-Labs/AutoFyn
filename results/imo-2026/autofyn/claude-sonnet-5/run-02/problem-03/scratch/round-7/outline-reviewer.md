# Outline-reviewer report, round 7 — IMO-2026-03

## Context read
`/tmp/round-7/proof-outliner.md`, `/tmp/round-7/math-explorer-c1-extension.md`,
`/tmp/round-7/math-explorer-lp-duality.md`, the full current text of
`approaches/rank-tie-vertex-reduction.md` (§5.1–5.4 in full),
`approaches/rank-pigeonhole-budget.md` (in full), `approaches/lp-duality-
certificate.md`, `results/imo-2026-03/current.md`, and `.ranking.json`.
No new approach files are proposed this round (the outliner explicitly chose
not to open a fourth framing, judging the three live cracks worth pushing
further first) — so no `register_approach`/`copy_approach` calls this round,
only re-ranking and a build set.

## The load-bearing question: is "Case I = general-$c_1$ gap" a true equivalence?

This is the outline's central claim (§0) and it drives all three approaches'
task assignments, so I checked it directly rather than taking it on faith,
per the assignment.

**Part 1 (true, verified).** `rank-pigeonhole-budget.md`'s Lemma 1 ("if
$f_i,f_j>p_2$ then $f_i+f_j>2p_2=p_1\ge\sum f_k$, contradiction") uses only
positivity and $p_1=2p_2$ — nothing in the proof restricts the fragment
count. It genuinely holds for $F$ with *any* number of parts, i.e. any
$c_1$. **Confirmed, no restriction to correct.**

**Part 2 (overstated).** The outline says extending Theorem GC($m$) from the
literal untouched ratio-2 tail $\tau$ to an arbitrary *legal refinement* $G'$
of the tail is "a concrete, bounded task." I re-read the GC($m$) induction
(rank-pigeonhole-budget.md §3): every step — the base case's $s\le 2a$
domain, the inductive step's $s'<\tau_1=2\tau_2$ bound feeding the next
level's domain $s'\in(0,2\tau_2]$ — depends on $\tau$ being an *exact*
ratio-2 superincreasing sequence, not merely "decreasing and $\le p_2$." A
legal refinement $G'$ is not superincreasing at all (a tail piece cut into
three fragments breaks the doubling relation completely), so GC($m$)'s
induction skeleton does not transfer by substitution — a genuinely new
induction (or a reduction showing refinements never help/hurt relative to
the unrefined tail, i.e. an analogue of the still-unproven Claim (B) from
`greedy-halving-adversary`) would be needed. This is real, useful next work,
but it is a materially harder ask than "import GC($m$) with $\tau\to G'$" —
flagged for the builder so this isn't treated as a one-line substitution.

**Part 3 (checked by direct computation — the outline's claim does not
survive as stated).** The outline identifies rank-pigeonhole's Case I with
"the residual `rank-tie-vertex-reduction`'s round-6 explorer hit... (the
origin-anchored window failure in that report's §2)." I tested this against
the explorer's own concrete data point (`math-explorer-c1-extension.md` §1–2,
$n=3$, $c_1=2$, tail untouched, fragments $(y_1,y_2,y_3)=(4,2,2)/15$, which
*is* a genuine Case I instance since $y_1=p_2=4/15$ exactly, boundary
included). The explorer found the **naive per-window decoupled bound**
($\int uv\le A(F)/2$, the direct analogue of $(\star\star)$) **fails** at
this vertex by a factor of 1.5 ($\int u v=3/15$ vs. bound $2/15$). I then
directly evaluated `rank-pigeonhole-budget`'s actual Case I inequality (4.1)
at the *same* vertex: $\tau=(p_2,p_3,p_4)=(4,2,1)/15$, $s=p_1=8/15=2\tau_1$
(boundary), $\tau''=(p_3,p_4)=(2,1)/15$, $R(\tau'')=3/15$. Inequality (4.1)
requires $A(F\cup\tau'')\le R(\tau'')+2\tau_1-s=3/15+8/15-8/15=3/15$. Direct
computation: $F\cup\tau''=\{4,2,2,2,1\}/15$, sorted alternating sum
$4-2+2-2+1=3$, i.e. $A(F\cup\tau'')=3/15$. **Inequality (4.1) holds, with
equality** — exactly at the point where the naive decoupled bound the
explorer tested *fails*. This proves (4.1) and the explorer's "naive
per-window sufficient condition" are **not the same statement** — (4.1) is a
genuinely different (and, at this data point, correct) reduction, not a
restatement of the explorer's refuted bound. **Verdict: the specific
identification with the explorer's origin-anchored-window failure is false;
the broader claim that Case I and the general-$c_1$ gap are conceptually the
same underlying obstruction (the "no single dominant fragment to peel"
regime) is directionally right and worth keeping, but "literally the same
open inequality" overclaims a syntactic identity that isn't there.** Both
builders should independently verify their own target inequality on
concrete vertices (as I just did) rather than assuming the sibling's write-up
transfers verbatim.

**Consequence for the build set.** No wasted-effort risk from a *false*
premise causing duplicate work on a *broken* target — (4.1) checks out at
the one adversarial data point available. But there is a real risk of
wasted effort from treating the two files' Case I as fungible/interchangeable
when they aren't (pigeonhole's Case I is scoped to the *untouched* tail only,
whereas rank-tie-vertex ultimately needs arbitrary tail *refinement* too —
a strictly larger problem GC($m$)/§4 do not yet address). I've corrected the
task text below so `rank-tie-vertex-reduction`'s builder treats "cite §4" as
a starting point to adapt and re-verify, not a free import, and pursues the
peel-induction-on-$c_1$ idea (explorer §3) as the primary, independent route
(it does not depend on the Case I identification at all).

## Per-approach review

**`rank-tie-vertex-reduction` — KEEP, revise per above.** Round 6's
Half-Window Vanishing closure of $c_1=1$ is settled (verified-milestone,
untouched by this round). This round's task: (a) test, on concrete small
vertices first (not assumed), whether GC($m$)'s machinery extends to a
legal tail refinement $G'$, or locate precisely where the ratio-2 dependency
breaks (real outcome either way, per the outline's own framing); (b) pursue
the peel-induction-on-$c_1$ idea (explorer §3) as the primary route — it has
a clean base case ($c_1-1\in\{0,1\}$, already closed) and 100% agreement
with hand data across $n=2,3,4$; its one concrete gap is a new
self-similarity lemma for "ladder tail spliced with one foreign piece of
size $p_1-z$," which is scoped and checkable. Do not present Case I of
Claim (A) as a free citation — if it's invoked, re-derive/re-verify the
specific instance needed rather than asserting transfer.

**`lp-duality-certificate` — KEEP.** The round's plan (test whether the
Half-Window Vanishing proof's conclusion decomposes into a bounded-term-count
certificate for a genuine multi-cut tail refinement, not just the
already-checked boundary case) is concrete, cheap, and — per the approach's
own prior recommendation — decisive either way (bounded terms → real
ammunition for the refinement gap above; unbounded/per-piece terms → confirms
the framing re-encounters $(\star\star)$'s content, stop iterating it on the
general bound). No issues found with this round's plan.

**`rank-pigeonhole-budget` — KEEP.** Case II is fully closed (verified
milestone, untouched this round). This round's Case I plan has two
independent legs: (1) consume an upper-bound tool if either sibling produces
one (fine, not circular — it's conditional, not a wait-loop), and (2) an
unconditional, independent attempt via strengthening the induction hypothesis
with a matching upper envelope, tested against existing exact data before a
general proof is attempted. This is legitimate, bounded work regardless of
what the siblings do.

## Numeric sanity re-check
Re-verified by hand, independent of the outline's own claims: the Lemma 1
generalization algebra ($f_i+f_j>2p_2=p_1$ contradiction, any part count) —
correct; the $n=3$, $c_1=2$ vertex data ($y=(4,2,2)/15$ summing to $p_1=8/15$,
Case I instance) — correct; inequality (4.1) evaluated exactly at that vertex
— holds with equality, computed above. No false numeric claim found in this
round's outline beyond the overclaimed identity already flagged.

## Ranking
No new approaches to register. Ran `update_ranking` with 7 comparisons:
`rank-tie-vertex-reduction` draws `rank-pigeonhole-budget` (co-equal
front-runners on the shared wall, both verified-milestone last round);
`rank-tie-vertex-reduction` and `rank-pigeonhole-budget` both beat
`lp-duality-certificate` (narrower progress so far, still a single
consistency check); `lp-duality-certificate` beats the deprioritized
`dyadic-band-occupancy`; `rank-pigeonhole-budget` beats
`exchange-argument-extremal-response` (stale, no update since round 3);
`greedy-halving-adversary` and `rank-tie-vertex-reduction` draw (both
strong, holding position — `greedy-halving-adversary` not touched this
round); `smoothing-compactness-certificate` and `rank-pigeonhole-budget`
draw likewise. Resulting order (best-first):
1. `greedy-halving-adversary` (1599.3)
2. `rank-tie-vertex-reduction` (1585.6)
3. `rank-pigeonhole-budget` (1568.9)
4. `smoothing-compactness-certificate` (1564.8)
5. `lp-duality-certificate` (1538.2)
6. `dyadic-band-occupancy` (1463.6)
7. `exchange-argument-extremal-response` (1444.4)
(remaining stale/dead-end entries unchanged: `integer-lattice-reduction`,
`bijective-mersenne-pairing`, `claiming-order-invariant`,
`self-similar-potential-certificate`, `self-similar-bracketing`.)

## Build set rationale
Dispatch exactly the three approaches the outliner targeted this round —
`rank-tie-vertex-reduction`, `lp-duality-certificate`, `rank-pigeonhole-
budget` — each with the corrected task text above (in particular:
rank-tie-vertex's builder must independently re-verify any inequality it
imports from the sibling rather than treat the outline's "same wall" framing
as license to skip verification, and should prioritize the peel-induction-
on-$c_1$ route, which stands on its own regardless of the Case I
identification's precise scope). Not rebuilding `greedy-halving-adversary`
or `smoothing-compactness-certificate` this round — no new angle assigned
to either, consistent with round 6's precedent of not rebuilding without a
fresh angle.

build set: rank-tie-vertex-reduction, lp-duality-certificate, rank-pigeonhole-budget
