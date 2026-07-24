# math-explorer report — alternative-framing lens (round 4)

## Context absorbed

Read `current.md` and all seven approach files. The obstruction is now
extremely well localized (three independent framings hit the *same* fact):

> **The core open fact.** Fix the ladder `p_1 > p_2 ≥ ... ≥ p_{n+1}` (sum 1,
> superincreasing: `p_i = 2^{n+1-i}/(2^{n+1}-1)`). Xiang Yu fragments the top
> piece `p_1` into `F = {f_1 ≥ f_2 ≥ ... ≥ f_{c+1}}` (dominant fragment `f_1`,
> "small fragments" `F' = F \ {f_1}`) and independently refines the tail into
> `G'` (sum `r = 1-p_1`). Write `A(·)` for the sum of odd-sorted-rank pieces
> (`Φ`). The stalled step (`greedy-halving-adversary`, Prop. 10) needs:
> `2∫₀ʳ u'(x)v(x)dx ≥ A(F') + A(G') - (f_1 - r) + a_n`, where `u'` and `v` are
> the odd-parity indicator functions of `F'` and `G'` on `[0,r)` — i.e. a
> **positive-correlation / anti-concentration bound between two
> independently-optimized parity-indicator functions**. Equivalently
> (`rank-tie-vertex-reduction`, `exchange-argument-extremal-response`): a
> **finite but uncharacterized enumeration of feasible tie-vertices**, where
> the minimizing vertex routinely **cross-ties** a fragment of `p_1` directly
> to a tail piece rather than splitting cleanly top/tail.

Per the repo's shared-gap-plateau rule, I did **not** try to patch this
inequality directly (that's the 4th independent framing hitting the same
wall). Instead I searched for genuinely different top-level architectures,
including a targeted crux-corpus pass on `games-and-strategy`,
`extremal-principle`, and `invariants-and-monovariants` subtopics for
superincreasing/majorization/blocking-game techniques (per the assigned
lens). Three cruxes turned out to be unusually good structural matches —
reported below as concrete techniques, not citations (per repo rules, every
borrowed step must still be re-proven from scratch).

## Crux-corpus findings (genuinely different techniques, not tried yet)

**1. `aimo-0117` (Dutch olympiad, stone-game with two capacity-limited
boxes) — the "superincreasing + defer-commitment invariant" move.**
Jesse plays powers of two `2^0, 2^{-1}\text{ or }2^1, ...` (a *two-sided*
superincreasing sequence) and maintains, by direct induction on the move
count (NOT by any continuum/LP argument), the invariant **"the largest power
played so far sits in the black box after my move."** He proves the
invariant is self-restoring: if the opponent moved the current-largest into
the white box, Jesse's box has a free slot and he immediately plays the next
larger power there; otherwise he plays the next *smaller* power (location
irrelevant) to preserve the option to protect the largest again. At the end,
`2^j > 2^{j-1}+...+2^{-i}` closes it (2), the exact superincreasing
inequality our ladder also relies on.

This is structurally the closest crux to our problem: it is an alternating
adversarial game on a **superincreasing sequence built move-by-move**, closed
by a **hand-built invariant about "who holds the current extremal element,"**
never by writing down a minimum-over-a-continuum and analyzing its vertices.
**Candidate approach for us:** reformulate Liu Bang's ladder not as a fixed
target multiset to defend abstractly, but as a sequence Liu Bang "builds"
adaptively against Xiang Yu's revealed cuts (in the claiming-subgame, both
sets of marks are fixed before claiming starts, so this needs adaptation —
but the *invariant technique* transfers): prove directly, by strong induction
on the number of pieces claimed so far, that Liu Bang can maintain "my
running total, plus the sum of all not-yet-claimed pieces weighted
favorably, dominates a fixed reference bound" — i.e. hunt for a **potential
function on partial claiming-sequences** (not on the final multiset) whose
value is monotone and whose endpoint gives `Φ ≥ a_n` directly, sidestepping
the parity-indicator-correlation inequality entirely. This is different in
kind from the existing self-similar-potential-certificate approach (round
1–2), which built a potential on the *final* multiset's structure; this one
would build a potential on the *claiming order* / turn sequence, à la
aimo-0117's per-move invariant.

**2. `aimo-0718` (ISL Israel, treasure-chest gem game) — the "majorization
sandwich against a rank-bounded blocking adversary" move.**
The problem: Elisa greedily adds to the smallest unlocked chest; a fairy
locks at most `r = t mod n` chests. The crux move proves a **domination
lemma by pure pigeonhole on sorted ranks** ("the `j` smallest chests for
`j > r` cannot all be locked, since only `r` are locked, so the greedy
minimum is dominated by every chest at sorted-rank `> r`") and then wraps a
**majorization argument**: constructs an explicit reference sequence
(here a round-robin arithmetic progression) that provably majorizes the real
sorted sequence for all time, and reads off the answer from the reference's
fixed spread — entirely avoiding computing the real process's extremes by
calculus.

**Candidate approach for us:** `Φ(S) = sum of odd-sorted-rank elements of S`
is exactly a **fixed linear functional of a sorted vector** — precisely the
kind of object majorization inequalities control (this functional is a
partial-Schur-type functional: sum of every other order statistic).
Instead of parametrizing Xiang Yu's continuum of legal cut-responses and
finding the minimizing vertex (the LP-vertex approach, already tried three
ways), **directly majorize the achievable final sorted multiset by a fixed
reference multiset for every legal Xiang Yu response**, and show the
reference's `Φ`-value already hits `a_n = 2^n/(2^{n+1}-1)`. Concretely: try
to prove
`(achieved sorted multiset S)` is majorized (in the *finite, comparable-sum*
sense — both sum to 1) **from below in the relevant partial sums** by the
ladder's own sorted multiset shifted/regrouped, using a **rank-pigeonhole
lemma analogous to aimo-0718's**: "for any legal Xiang Yu cut composition,
among the `k` largest pieces of Liu Bang's ladder pieces overlapping a given
interval, at most `(cuts spent by Xiang Yu in that interval)` many can be
removed/split away from odd rank, so at least `k - (cuts spent)` of them
retain odd rank" — turning the "cross-term/anti-concentration" analytic
inequality (which has resisted four framings) into a **counting/pigeonhole
statement about how many cut-points Xiang Yu can spend inside any given
sub-interval of the ladder**, which is intrinsically discrete and may be far
more tractable than the continuous parity-correlation integral. This is
promising specifically *because* the located gap (Prop. 10's missing
inequality) is already an inequality about how much two "budgets" (cuts on
`p_1` vs cuts on the tail) can conspire — exactly the shape of aimo-0718's
"adversary can block at most `r`, so pigeonhole among the `r+1` smallest"
argument, but transplanted from a *time*-indexed blocking budget to a
*cut-count* budget. This is a genuinely different proof technique
(discrete majorization/pigeonhole vs. continuum integral correlation) even
though it targets the same final inequality — it may succeed where the
integral approach stalled because it never needs to reason about `u'` and
`v` as functions of a continuous variable `x` at all, only about counts of
cuts landing in nested sub-intervals `[p_{i+1}+...+p_{n+1}, 1]` of the
ladder.

**3. `aimo-0019`/`aimo-0141` — "distinct powers of two, largest exceeds sum
of rest" as a *reusable bounding lemma*, not a new architecture.** Both
cruxes independently invoke the plain superincreasing inequality
`2^j > 2^{j-1}+...+2^{-i}` as a one-line closing move after a separate
structural argument does the real work. This confirms the superincreasing
property itself is *not* the hard part anywhere in the corpus — consistent
with our finding that `c=0` and the achievability halves are easy, and that
the hard part is always the "who gets forced to concede which piece" combinatorial
structure, not the arithmetic of the ladder. Useful mainly as reassurance:
don't spend more rounds trying to squeeze the ladder arithmetic itself
harder; the difficulty is genuinely combinatorial/game-structural.

## Non-corpus candidate: strategy-stealing / pairing on the claiming subgame

Independent of the corpus, one architecture not yet tried by any approach:
a **direct pairing/strategy-stealing argument on the claiming subgame**
itself (distinct from all six existing approaches, which all attack `Φ`'s
minimum as a function of the *cut* multiset). The claiming subgame (once
cuts are fixed) is: `2m` pieces (or however many), players alternately claim,
Liu Bang first, each maximizing own total; the value is exactly the sum of
odd-sorted-rank pieces (already proved, shared lemma). Consider instead
**pairing up pieces directly by an explicit combinatorial rule tied to the
ladder's geometric structure** (e.g., pair each small fragment of `p_1`
with a same-or-larger-indexed tail piece it could "shadow"), and argue via
an **exchange/domination argument on the pairing** (not on parity-indicator
integrals) that Liu Bang's claimed total in the paired game is at least
`a_n` — i.e., **construct an explicit injective (not necessarily
measure-theoretic) map from Xiang Yu's tail-refinement pieces into
"already-dominated-by-Liu-Bang" slots**, closer in spirit to a Hall's-theorem
/ system-of-distinct-representatives argument (cf. `knowledge_base.md`'s
"Multiset partitions & power-sum matching (Prouhet–Tarry–Escott flavor)"
entry, line ~120–123: "split into a system of distinct representatives for
X") than to LP-vertex or integral machinery. This is speculative — I did not
find a corpus crux that solves an *identical* shape — but it is a genuinely
different toolkit (combinatorial matching / SDR existence) from all six
live approaches, so it satisfies the "far from the current field" mandate
even if its odds are unclear.

## Recommendation ranked by promise

1. **Discrete majorization/pigeonhole recast of Prop. 10's missing
   inequality** (crux `aimo-0718`-style): highest promise, because it attacks
   the *exact* located gap with a technique from a different toolbox
   (discrete counting vs. continuous integral correlation), so it could
   close the plateau rather than just relocate it. Concretely actionable:
   an outliner could write this as a new approach `rank-pigeonhole-budget`
   with the skeleton: (a) restate `A(F')+A(G')` vs cross-term in terms of
   how many of Xiang Yu's `c` cuts on `p_1` and `n-c` cuts on the tail land
   in each of the `n` nested ladder sub-intervals; (b) prove a pigeonhole
   lemma bounding, for each sub-interval, how many odd-rank pieces Xiang Yu
   can "steal" given his cut budget there; (c) sum across sub-intervals to
   recover `a_n` as a floor, mirroring aimo-0718's per-index domination +
   global majorization sandwich.
2. **Claiming-order potential function** (crux `aimo-0117`-style): a
   structurally different but higher-risk architecture — needs inventing
   an adaptive-order potential for a game whose cuts are actually fixed
   in advance (unlike aimo-0117's genuinely sequential play), so the
   translation is not immediate; worth one outline attempt only if (1)
   stalls again.
3. **SDR/pairing argument on the claiming subgame directly**: genuinely
   different toolkit, lowest confidence of success, good "far from the
   field" diversity pick if the outline-reviewer wants a second, more
   speculative line alongside (1).

## Not recommended

Do not spin up a fourth variant of mass/LP-vertex/self-similar-potential
accounting — three independent rounds already triangulated on the identical
obstruction from that toolbox family; a fourth would very likely just
relocate the same wall (this is exactly the shared-gap-plateau pattern the
orchestrator rules warn about).
