# Proof-outliner report — round 4, IMO-2026-03

## Context absorbed

Read `current.md`, all seven approach files
(`greedy-halving-adversary`, `smoothing-compactness-certificate`,
`self-similar-potential-certificate`, `self-similar-bracketing`,
`rank-tie-vertex-reduction`, `exchange-argument-extremal-response`,
`induction-first-move-reduction` — the last never registered/built, still
sitting outside `.ranking.json`, and left untouched below), the ranking
sidecar, and both round-4 explorer reports
(`/tmp/round-4/math-explorer-superincreasing.md`,
`/tmp/round-4/math-explorer-altframing.md`).

**State of the plateau.** Four independent framings (mass/cross-term bound,
self-similar bracketing, LP-vertex via rank-tracking, LP-vertex via
minimizer-fixing) all reduce to the same open fact: characterizing/bounding
$\Phi$ at the feasible tie-vertices for general $n$, equivalently Prop. 10's
cross-term inequality
$2\int_0^r u'v\,dx \ge A(F')+A(G')-(f_1-r)+a_n$. Round 4's explorers add two
hard facts that change the shape of the next attack:

- **Superincreasing lens:** vertex enumeration does *not* collapse to $O(n)$
  cases — the fraction of tied-optimal compositions stays ~15–25% at every
  tested $n$, and even a single composition's cell can host multiple
  distinct optimal vertices (a genuinely "cross-generational" tie
  co-existing with a "clean" one). A brute enumeration is fighting the wrong
  battle. But there is a clean $O(n)$-indexed **prefix cascading-halving
  sub-family** (cut a prefix $p_1,\dots,p_k$, each split exactly into two
  copies of the next rung, via the exact identities $p_i=2p_{i+1}$ and
  $p_i-\sum_{j>i}p_j=f(n)$ constant) that hits the target exactly at every
  tested $k$ — a tractable, certifiable partial result even though it is
  not the whole enumeration.
- **Alt-framing lens:** the crux corpus supplies a technique from a
  genuinely different toolbox for the *exact same* located gap — recast
  Prop. 10's cross-term as a **discrete majorization/pigeonhole** statement
  (à la `aimo-0718`), replacing the continuum integral correlation with a
  counting argument about how many of Xiang Yu's cuts can land in nested
  ladder sub-intervals. Also flags an `aimo-0117`-style claiming-order
  invariant and a speculative SDR/pairing argument as secondary, more
  distant options.

Per the shared-gap-plateau rule, this round's field puts the pigeonhole
recast on the table as the required "far from LP-vertex/mass-accounting"
entry, alongside concrete, explorer-informed next steps for the strongest
live approaches, and an explicit retirement recommendation for the one
approach whose premise is now refuted with no fix found.

---

## Field of approaches (7 slugs: 1 new headline, 1 new speculative
(via revise of a stuck slug), 4 advance, 1 retire)

### 1. NEW — `rank-pigeonhole-budget` (headline new-framing entry)

**Target.** Same as all approaches: `c(n) = 2^n/(2^{n+1}-1)`, both
directions, general $n$. This slug's job is narrower: **close Prop. 10's
Missing Inequality** (equivalently, the general lower bound for $c\ge1$) by
a discrete counting argument instead of a continuum integral, importing all
already-certified shared lemmas (`claiming-subgame-reduction`,
`cross-term-identity-threshold`, `odd-run-reduction-lemma`,
`vertex-minimum-theorem`) rather than re-deriving them.

**Technique (spine).** Recast the two "budgets" Xiang Yu splits between —
$c$ cuts spent fragmenting $p_1$ into $F=\{f_1\ge\dots\ge f_{c+1}\}$, and
$n-c$ cuts spent refining the tail into $G'$ — as a **blocking budget
against nested sub-intervals of the ladder**, and prove a pigeonhole
domination lemma in the style of `aimo-0718`'s "adversary can lock at most
$r$ chests, so the $j$ smallest for $j>r$ cannot all be locked."

**Skeleton.**
1. **Restate the target inequality as nested-interval counting.** For each
   $i=1,\dots,n$, let $I_i = [\,\sum_{j>i}p_j,\ \sum_{j\ge i}p_j\,)$ be the
   $i$-th ladder sub-interval (length $p_i$). Xiang Yu's $n$ total cut
   points partition into however many fall in each $I_i$; write $x_i\ge0$
   for the count of his cuts landing inside $I_i$ (so $\sum x_i \le n$, and
   his split between fragmenting-$p_1$ vs refining-tail from Prop. 10
   corresponds to $x_1$ vs $\sum_{i>1}x_i$). Re-derive $A(F\cup G')$'s
   dependence on $(x_1,\dots,x_n)$ using the certified
   `odd-run-reduction-lemma` (already handles arbitrary simultaneous ties),
   so the objective becomes a function of the *counts* $x_i$, not of
   continuous cut positions — this is the discretization step.
2. **Pigeonhole domination lemma (the crux, new).** Prove: for any $i$, if
   $x_i$ is small relative to the number of pieces Liu Bang's ladder places
   in or below $I_i$, then at least $(\text{ladder pieces at level}\ge i) -
   x_i$ of them retain odd sorted rank in the final multiset — a direct
   transplant of `aimo-0718`'s "$j$ smallest chests, $j>r$ locked, so $\ge
   j-r$ survive" argument, with "locked chest" $\to$ "cut point landing in
   this sub-interval" and "chest count" $\to$ "ladder pieces at this level."
   This is the step that must actually be proved from scratch (per repo
   rules, the crux is a hint to adapt, not to cite) — it is NOT the same
   statement as `aimo-0718`'s, only structurally analogous; the exact
   quantifiers (what counts as "surviving" when a cut both splits a piece
   AND changes its rank) must be worked out for this problem's specific
   odd-rank-sum objective.
3. **Majorization sandwich.** Construct the reference sequence: the ladder's
   own sorted multiset, and show the actually-achieved sorted multiset is
   majorized from below (in the relevant partial sums, i.e. $\Phi\ge$
   reference's $\Phi$) using Step 2's per-level domination, summed across
   all $n$ levels — mirroring `aimo-0718`'s round-robin reference-majorizes-
   real-process argument, adapted to this problem's static (not
   time-indexed) setting.
4. **Recover $a_n=2^n/(2^{n+1}-1)$ as the floor.** Show the majorization
   sandwich's lower bound, summed via the pigeonhole counts and Xiang Yu's
   budget constraint $\sum x_i\le n$, evaluates exactly to $a_n$ — a direct
   computation using the ladder's geometric ratio, cross-checked against
   the $n=1,2$ closed cases and the $n=3$ tie example
   (`rank-tie-vertex-reduction.md` §3 / this round's Finding 3) as sanity
   checks before claiming the general case.
5. **Tightness check.** Confirm the sandwich is tight exactly at Liu Bang's
   ladder (not merely an inequality that happens to hold at the ladder but
   is loose elsewhere) — needed since this is a *max over Liu Bang
   configurations* problem, so a lower bound that isn't achieved at the
   ladder specifically doesn't finish the "= " half of the theorem.

**Key lemmas to import (do not re-derive):**
`claiming-subgame-reduction`, `odd-run-reduction-lemma`,
`vertex-minimum-theorem`, `cross-term-identity-threshold` (for
cross-checking Step 1's restatement against the existing integral form).

**Open gaps (all of them — new slug):** Step 2 (the pigeonhole domination
lemma itself — genuinely unproved, this is the whole ballgame), Step 3
(the majorization sandwich mechanics), Step 4 (the exact floor computation),
Step 5 (tightness). Flag explicitly: if Step 2 turns out to be exactly as
hard as Prop. 10 restated in different language (a real risk — the
explorer calls this "promising" but concedes it is speculative), the
builder must report that honestly rather than force a proof through.

**Watch out for:** this must not become a fifth continuum-integral
argument in discrete clothing — if the builder finds themselves re-deriving
$\int u'v$ under a new name, that is a sign the recast didn't actually
change toolboxes and should be reported as such.

---

### 2. NEW (via REVISE of the stuck `self-similar-potential-certificate`
slug) — retarget as `claiming-order-invariant`

**Why revise this slug specifically.** `self-similar-potential-certificate`
(elo 1473.4, lowest of the live population) already tried a
*potential-function* architecture and found the natural mass-based
potential provably insufficient (round 2's negative result). Its own
framing — a certificate tied to structure, not to a global integral — is
philosophically closest to the `aimo-0117` claiming-order-invariant idea the
alt-framing explorer surfaced, so redeploying this slug (rather than
opening an 8th file) keeps the population size in check while giving it a
genuinely different mechanism to try, per the "revise a stuck approach"
option in the workflow.

**Target.** Same overall claim. This slug's distinguishing idea: build the
potential/invariant on the **claiming order** (the sequence in which pieces
get claimed in the already-reduced claiming-subgame), not on the final
multiset's structure — a structurally different induction variable from
every other live approach.

**Technique (spine).** Adapt `aimo-0117`'s per-move invariant
("the largest power played so far sits in the protected box after my
move," self-restoring by induction on move count) to the claiming-subgame.
Caveat, stated up front: unlike `aimo-0117`, both players' full mark sets
are fixed *before* claiming starts here (this is a static combinatorial
game on a fixed multiset, not a genuinely sequential move-by-move
mark-placement game), so the invariant must be re-targeted at the *order of
claims*, not at move-by-move mark choices — unlike `aimo-0117`, there is no
adaptive marking left to exploit at this stage.

**Skeleton.**
1. Import `claiming-subgame-reduction` (shared lemma): claiming a fixed
   multiset alternately, each maximizing own total, gives Liu Bang exactly
   the sum of odd-sorted-rank pieces — this is the game we invariant-hunt
   on.
2. **Candidate invariant.** After Liu Bang's $k$-th claim, "the largest
   not-yet-claimed piece is smaller than Liu Bang's running total minus
   Xiang Yu's running total, scaled by a $k$-dependent factor tied to the
   ladder's self-similarity constant" — i.e., a running-total domination
   invariant, checked by strong induction on claim number, analogous to
   `aimo-0117`'s "largest power sits in the protected box."
3. **Base case.** $k=0$ (before any claims): trivial statement about the
   full ladder.
4. **Inductive step.** Show the invariant is self-restoring across one
   round of (Liu Bang claims greedily, Xiang Yu claims greedily) — this is
   the actual content to prove, and is currently completely open (no
   candidate invariant has been checked even numerically yet).
5. **Endpoint.** Show the invariant, at the last claim, forces
   $\Phi\ge a_n$ directly — sidestepping Prop. 10's cross-term/vertex
   machinery entirely if it works.

**Open gaps:** everything — Step 2's invariant is a first guess, not yet
even checked against the $n=3$ tie example
(`rank-tie-vertex-reduction.md` §3) for consistency. First builder task:
check the candidate invariant (or a corrected version of it) against that
concrete $n=3$ instance before attempting a general proof — cheap
sanity-check, high information value.

**Risk assessment (explicit, per explorer's own ranking):** this is the
*lower-confidence* of the two new entries — the explorer ranked it #2,
behind the pigeonhole recast, precisely because the translation from a
genuinely sequential game (`aimo-0117`) to this problem's fixed-marks
game is not immediate. Include it in the field for diversity; the
outline-reviewer should weigh it accordingly against slug 1.

---

### 3. ADVANCE — `rank-tie-vertex-reduction` (elo 1512.4)

**Next step (concrete, from Finding 1–3 of the superincreasing explorer).**
Do NOT attempt the raw enumeration this round (Finding 1 shows it is large,
not small). Instead:
1. **Prove the prefix cascading-halving sub-family cleanly**: for every
   $k\in\{0,\dots,n\}$, the composition cutting exactly $p_1,\dots,p_k$ each
   into two copies of the next rung ($p_i\to(p_{i+1},p_{i+1})$) attains
   $A=f(n)=a_n(2^{n+1}-1)$ exactly — by induction on $k$, using the exact
   identities $p_i=2p_{i+1}$, $p_i-\sum_{j>i}p_j=f(n)$ (both verified by the
   explorer for $n\le6$, elementary from the geometric-sum formula, worth
   stating as a small reusable fact alongside `ladder-self-similarity-
   constant` if not already implicit there) plus the certified
   `odd-run-reduction-lemma` to collapse the even-multiplicity runs. This
   is a genuinely tractable, self-contained partial result (unlike the full
   enumeration) and should be certified as its own reusable lemma if it
   closes cleanly.
2. **Explicitly reconcile with Finding 3**: the same composition can have a
   second, "cross-generational" optimal vertex (already on file in this
   approach's §3) — the builder must show the prefix-cascade result and the
   cross-generational result are *both* valid instances attaining the same
   floor, not competing claims, and should not overclaim that the cascade
   family is exhaustive.
3. Leave the full enumeration/characterization as still open, but now with
   one clean certified sub-case in hand plus a documented reason (Finding 1)
   why brute-force enumeration is not the productive next move — recommend
   any future builder on this slug pivot toward importing
   `rank-pigeonhole-budget`'s result (once available) rather than continuing
   raw enumeration.

**Open gaps:** the cascading-halving induction itself (new, should be
quick); the general characterization (still fully open, explicitly
deprioritized in favor of slug 1's pigeonhole recast).

---

### 4. ADVANCE — `exchange-argument-extremal-response` (elo 1481.4)

**Why keep it distinct from slug 3** (its sibling, same Vertex-Minimum
Theorem): rather than duplicate the cascading-halving work, give this slug
the alt-framing explorer's third, most speculative candidate — the
**SDR/Hall's-theorem pairing argument** — since this approach's existing
machinery (fixing a minimizer, deriving *local* swap/exchange conditions)
is already close in spirit to a matching argument, making it the natural
home for this idea rather than a fresh slug.

**Next step.** Attempt to construct an explicit injective map from Xiang
Yu's tail-refinement pieces into "already-dominated-by-Liu-Bang" slots
(per `knowledge_base.md`'s SDR/Prouhet–Tarry–Escott entry), using the
already-proved `pair-cancellation-identity` and Corollary E4 as the local
building blocks, and check Hall's condition against the concrete $n=3$
cross-generational tie example (shared with slug 3) as the first test
case. Flag clearly if Hall's condition provably fails on that example — a
fast, cheap way to kill this line early rather than let it linger.

**Open gaps:** existence of the SDR itself (wholly open, genuinely
speculative per the explorer's own risk rating — lowest-confidence of the
"live" advances this round, kept for diversity, not because it is
favored).

---

### 5. ADVANCE — `greedy-halving-adversary` (elo 1564.8, top of population)

**Next step.** Two options, both cheap to attempt before committing a full
round:
1. Re-express Prop. 10's Missing Inequality using this round's new exact
   identities ($p_i=2p_{i+1}$, $p_i-\sum_{j>i}p_j=f(n)$) restricted to the
   ladder's specific geometry — these weren't available when Prop. 10 was
   first stated in round 2, and may simplify the correlation bound enough
   to close it directly (this is NOT a fifth generic mass-bound attempt —
   it is testing whether the *exact* ladder identities, not a generic
   subset-sum bound, close the specific gap; the explorer's "don't try
   another mass bound" warning targeted generic bounds, not
   identity-specific substitution).
2. If (1) doesn't close it within the round, this slug's builder should
   explicitly wait on / import `rank-pigeonhole-budget`'s result rather
   than re-attempting the integral directly a fifth time — record this as
   the fallback, not a parallel independent attempt.

**Open gaps:** Prop. 10's Missing Inequality (unchanged), now with two
named next moves instead of one vague "keep trying."

---

### 6. ADVANCE — `smoothing-compactness-certificate` (elo 1545.7)

**Next step.** $c(2)=4/7$ is fully closed (both directions, non-numeric) —
the strongest fully-certified base case in the run. Generalize the
6-template LP-contradiction argument to general $n$ using the **prefix
cascading-halving family** (slug 3) as a natural candidate set of templates
for arbitrary $n$ (the $n=2$ templates were found by exhaustive case
analysis over the small composition space; for general $n$, the
cascading family gives an infinite but $O(n)$-indexed candidate template
list to start from, rather than re-deriving templates from scratch). This
is a genuinely new, concrete next step this round (previously the approach
had only "a sketch of what a template-family generalization would need").

**Open gaps:** whether the $O(n)$ cascading templates are *sufficient* to
run the LP-contradiction argument for general $n$, or whether additional
templates (e.g. covering the cross-generational ties from Finding 3) are
needed — open, first thing the builder should check.

---

### 7. RETIRE (recommend dropping from active build set) —
`self-similar-bracketing` (elo 1541.4)

**Why.** Round 3 proved (Prop. B2) that the approach's core premise — "the
$c=n$ endpoint is free/easy, so bracket the interior between two easy
endpoints" — is false: $c=n$ minimality embeds the identical open
cross-term obstruction. Lemma B1 (exact achievability at $c=n$) remains
correct and is already certified/reusable
(`rescaled-ladder-c-equals-n-achievability`), so nothing proved is lost by
retiring the *framing*. No fix to the bracketing idea itself was found by
either explorer this round, and inventing one would essentially require
solving the same obstruction slug 1 is now targeting directly.

**Recommendation to outline-reviewer.** Do not include in this round's
build set. Keep the file/slug on record (do not delete — CLAUDE.md's
population model keeps a dead-ended approach's record for future
reference) but mark it de-facto inactive unless a future round surfaces a
genuine alternative bracketing invariant. This is a clean instance of "when
the population's shared gap plateaus, kill the framing that's shown to be
structurally unfixable rather than let it linger at high elo on the
strength of an old, now-superseded partial result."

---

## Summary table

| slug | action | new framing? | risk |
|---|---|---|---|
| `rank-pigeonhole-budget` | NEW | yes — discrete majorization, far from LP-vertex/mass field | medium-high, but targets exact located gap |
| `claiming-order-invariant` (revise of `self-similar-potential-certificate`) | NEW (revise) | yes — claiming-order potential, far from final-multiset framings | high (speculative, explorer's own #2 ranking) |
| `rank-tie-vertex-reduction` | advance | no (same family) | low-medium — cascading-halving sub-proof looks tractable |
| `exchange-argument-extremal-response` | advance | no (same family), but new SDR angle | high (speculative) |
| `greedy-halving-adversary` | advance | no (same family), new identity-specific attempt | medium |
| `smoothing-compactness-certificate` | advance | no (same family), general-$n$ template extension | medium |
| `self-similar-bracketing` | **retire from build set** | — | premise refuted, no fix found |

**Recommended build set (for outline-reviewer to confirm/adjust):**
`rank-pigeonhole-budget`, `rank-tie-vertex-reduction`,
`greedy-halving-adversary`, `smoothing-compactness-certificate`, and, if
builder budget allows a 5th, `claiming-order-invariant` (speculative
diversity pick) or `exchange-argument-extremal-response` (speculative SDR
pick) — `self-similar-bracketing` excluded per the retirement
recommendation above.

build set: rank-pigeonhole-budget, rank-tie-vertex-reduction, greedy-halving-adversary, smoothing-compactness-certificate, claiming-order-invariant
