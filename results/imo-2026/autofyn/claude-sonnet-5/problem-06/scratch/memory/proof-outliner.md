ALWAYS: read `.autofyn/approach_ranker.py`'s module docstring once per run if
unsure which MCP tool belongs to which role — it documents the full
sample/register/copy/record/update division of labor precisely (round 1).

ALWAYS: for an existence-of-periodicity problem, check whether the statement
requires the relation to hold "for every n" (from n=1) vs. only "eventually" —
a pigeonhole/finite-state argument only natively gives eventual periodicity, so
if the problem demands it from n=1, bake an explicit backward-sharpening step
into every approach's skeleton rather than letting the gap hide inside "then
periodicity follows" (imo-2026-06, round 1).

ALWAYS: when explorers converge on one dominant framing (e.g. "finite backbone
+ CRT"), still diversify the *mechanism* attacking that framing's hard lemma
across approaches (density-counting vs. constructive strong induction vs.
extremal descent), not just relabel the same abstract pigeonhole argument
three times — genuinely different proof techniques for the same target lemma
count as real diversity, not the single-gap trap, as long as each is a
complete rival top-level route (round 1).

NEVER: let an approach's skeleton assert a specific numeric backbone formula
(e.g. "backbone = rad(a_1) ∪ {2,3}") as if proven — explorer simulation on
imo-2026-06 refuted this for a_1=247 (needs an unpredicted extra prime 7); keep
backbone/helper-set existence as an open gap with an honest mechanism sketch,
not a guessed closed form (round 1).

ALWAYS: numerically test your own new lemma claims (small Python script) before
writing them into an approach file, even at the outline stage — drafting a
"Global Intersection Collapse" lemma for imo-2026-06 round 2, I initially
claimed an explicit bound N_0<=|P_1|+1 on the stabilization index; a 10-line
sympy/gcd check (a_1=65) showed N_0=4 > |P_1|+1=3, i.e. the bound was false
(confused "at most k strict decreases" with "index of first decrease bounded
by k+1" — a sequence can stay constant arbitrarily long between decreases).
Caught before writing to disk only because I tested it; the corrected, honest
lemma (finite stabilization exists, no small explicit bound) is still useful.
Outline-stage claims are not exempt from this check just because "the builder
will prove it properly" (round 2).

ALWAYS: when an explorer numerically refutes a *definition* used by a live
approach (not just a step), retarget the approach's Section/Step that used
that definition explicitly in the revision, rather than only patching the
proof strategy around it — imo-2026-06's backbone-existence-crt round-1
Section 3 defined "backbone finiteness" via literal H_n (any prime ever
co-occurring in a gcd witness pair), which round-2 exploration proved
unbounded even in an already-solved case (2948 incidental primes for a_1=15).
The fix was reformulating the *target claim* itself (persistent-divisor
primes B, not ever-co-occurring primes) before revising any step that used
it — patching Step 3's mechanism without fixing the false Section-3
definition first would have wasted another round (round 2).

ALWAYS: diagnose *why* a refuted definition failed before designing its
replacement — the imo-2026-06 H_n bug was "accepts any common prime of two
already-fixed integers" instead of "canonical/minimal witness"; verifying this
diagnosis with one more Python check (min(rad(a_i)∩rad(a_j)) for the actual
counterexample pair) both confirmed the fix and directly suggested the
correct replacement notion (canonical minimal witness w(i,j)) for a new
approach's skeleton, rather than guessing at a repair (round 2).

ALWAYS: when two logically independent sub-obstructions jointly constitute
one gap (e.g. imo-2026-06 Gap 2 = "coincidence lemma" + "no-pre-period
injectivity" — neither alone gives periodicity-from-n=1), keep them as
sequential steps inside ONE approach's skeleton rather than splitting them
into rival slugs — they are complementary, not alternative, routes, so
splitting them would violate the single-gap-trap rule in spirit (each half
would look "incomplete" alone and neither is a genuine rival top-level
attempt). Reserve the copy/new-slug mechanism for cases where two mechanisms
each independently suffice to close the SAME gap, not for cases where two
mechanisms must both succeed together (round 3).

ALWAYS: re-run the outline-reviewer-validated target's stress tests at wider
scale before trusting it for another round — round-2's `W`-finiteness target
(already downgraded to a weaker "Finite Covering Backbone Conjecture" that
round-2 believed W's finiteness would still trivially imply) was found
numerically FALSE this round at larger M (a_1=4199, |W| still growing past 21
primes with no plateau at M=15000) even though it looked stable in round 2's
smaller-M tests. When a math-explorer reports a target "looks bounded" from
only a few thousand terms, budget a later round to push the same check an
order of magnitude further before any approach's skeleton leans on it (round
3, imo-2026-06).

NEVER: assume a necessity lemma (e.g. "F ⊆ H for every valid covering H,
because F's primes are the unique witness for some pair") also proves
sufficiency (F itself, or a bounded augmentation, covers every pair) — these
are logically independent directions and conflating them lets a builder
silently claim a stronger result than what's proved. Flag both directions
explicitly as separate open items in the skeleton (round 3, imo-2026-06,
forced-primes-well-ordering and explicit-window-backbone-construction both
have this exact necessity/sufficiency split).

ALWAYS: when a field of approaches has converged onto ONE target (e.g.
Hypothesis (MRS) certified sufficient for the whole problem via a bridge
lemma), diversify by MECHANISM across the population, not by re-opening
sham alternative targets — a fresh-framing explorer that finds "every
bypass collapses back to the same target" is a genuine, useful negative
result, not a sign to force a new slug. Concretely for imo-2026-06 round 5:
kept 3 live approaches on the identical target (MRS)/FCBC but gave them
provably distinct formal machinery (Dershowitz-Manna multiset order over
collapse events; a permanent-domination/event-counting argument on a static
union of ever-minimal values; a channel-localized divide-and-conquer into
≤3^ω(a_1) independent sub-problems) — each is a genuinely different proof
route even though all three are known (round 4) to converge on the same
explicit numerical answer if any one succeeds. Do not manufacture a 4th
slug with a "fresh" top-level framing just to hit a target approach count
when the fresh-framing explorer already proved no bypass exists (round 5).

ALWAYS: numerically re-derive a claimed closed-form BEFORE writing it into
a skeleton, even when an explorer's report already states it — round 5's
imo-2026-06 explorer's fan/collapse mechanism described a threshold T_C
"least value with radical exactly C" but gave an example (T_C=2·61²=7442)
inconsistent with the naive closed form T_C=∏_{p∈C}p (=122, which is <a_1
and can never appear as a term of an increasing sequence starting above
a_1). A 10-line Python check caught this before it propagated into 3
approach files; the corrected definition T_C:=min{x>a_1 : rad(x)=C} matched
the example exactly. Explorer prose can encode a correct phenomenon with a
wrong formula attached — verify the formula independently, not just the
phenomenon (round 5).

ALWAYS: when dispatch instructs "persist approach files directly, verify
with ls" (as round 6's did), write/Edit the actual approaches/<slug>.md
prose files yourself with Write/Edit — this does NOT conflict with the
round-1 rule that the outliner lacks register_approach (the MCP tool that
writes the Elo/ranking sidecar .ranking.json); those are two different
artifacts. Prepend a "## Round N Outline (proof-outliner directive)"
section right after "## Status" (matching the exact pattern already used by
rounds 3-5 in this workspace) for a revised approach, and write the full
file-contract skeleton (Status/Approaches tried/Current best/Open gaps) for
a brand-new slug — then `ls` every touched file before finishing (round 6).

NEVER: let a "recursive/nested absorption resembles a smaller instance of
the same problem" observation stand as a sufficient condition by itself —
explorers repeatedly flag this shape (imo-2026-06 rounds 5-6, the fan/
generation/companion-count language) as circular unless paired with an
actual well-founded reduction (e.g. a genuine induction on a measure bounded
by a FIXED finite quantity like |P_1|, with an explicit map from depth-d
unknowns to depth-(d-1) knowns). When outlining such an approach, write the
induction skeleton but explicitly flag "resemblance ≠ reduction" as the gap,
naming the two concrete obstacles (no fixed ambient set one level down;
non-uniform bundling shape) rather than letting the builder paper over them
(round 6).

ALWAYS: when an explorer PROVES (not just observes) that a live approach's
literal current target is a proper subset of the true master gap — e.g.
round 8's thread-unification explorer showed "permanent bundle count"
(persistent-backbone-monovariant's round-7 target) ignores the still-open
transient-member count, so closing it would NOT close Λ_S-finiteness —
retarget that approach's Step explicitly in the revision and say so in
plain language ("Step X's old target is insufficient, retarget to Y"), not
just append new content on top; otherwise the builder keeps reporting
progress against a target proven not to matter (round 8, imo-2026-06).

ALWAYS: when 2+ live approaches turn out, this round, to need the identical
unproved existence sub-lemma (e.g. "does a core-avoiding witness always
exist for every proper core S"), name it as ONE shared prerequisite in every
affected approach file ("prove once, cite from both/all") rather than
letting each builder rediscover or reprove it independently — cheaper, and
keeps the outline-reviewer's picture of "how many genuinely distinct open
facts remain" accurate (round 8, imo-2026-06).

NEVER: let a numerically-verified pairwise-disjoint-family pigeonhole bound
(e.g. "any pairwise-disjoint family of realized bundles has size ≤ small
constant") stand as if it closes a total-finiteness target — a bound on
disjoint sub-families does not bound total family size unless paired with
a dichotomy that also handles the non-disjoint (sunflower/common-core)
case; keep the pigeonhole lemma and the completion (Δ-system dichotomy or
equivalent) as visibly separate skeleton steps so the gap that remains open
is not accidentally hidden inside a "corollary" that only handles one branch
(round 8, imo-2026-06).

ALWAYS: when an explorer reports a hypothesis is "very likely FALSE" via
much-deeper simulation, check whether that hypothesis was ever proved
NECESSARY for the target or only SUFFICIENT before treating this as a
problem-wide crisis — imo-2026-06 round 9: `(UB_S)` (bundle-SIZE
boundedness) looked very likely false at n~4x10^5, but it was only ever a
SUFFICIENT condition for FCBC (pairwise-witness existence), never proved
necessary; re-reading the SAME numerical data with that distinction in mind
flipped its interpretation from "bad news" to direct evidence FOR a small
explicit FCBC witness set (0/1.3M terms avoided a fixed 6-prime set). A
refuted sufficient condition kills that one route, not the target itself —
always re-examine whether a strictly weaker route (already on record,
possibly abandoned earlier as "less tractable") survives the refutation
untouched (round 9).

ALWAYS: when reviving a long-stuck approach (5+ rounds unexpanded) with a
genuinely new mechanism, prepend the new directive but do not delete the
old "do not re-attempt X" warnings from prior rounds' directives already in
the file — a builder reading only the newest section could otherwise
resurrect a mechanism already proved to fail (e.g. explicit-window-
backbone-construction's round-3 finite-descent-on-`|H_K|` dead end,
still needed even though round 9's directive targets a completely
different mechanism) (round 9, imo-2026-06).

ALWAYS: re-read a standing "NEVER re-attempt X in any form" Rule's own
justification text before treating it as blocking a NARROWER, differently-
constructed use of X-adjacent machinery — round 10's Rule "never re-attempt
(MRS)/𝓥_S-finiteness/(UB_S)" was justified specifically as retiring "the
...-VIA-COMPANION-BUNDLE-SIZE program," i.e. (UB_S) (bundle SIZE bound) was
only ever a SUFFICIENT, never necessary, route to (MRS)/𝓥_S-finiteness
(per the file's own theorem-UBS-sufficiency.md one-directional chain) — so
(UB_S)-false does not itself refute (MRS)/𝓥_S-finiteness, only that one
route to it. This is the same necessary-vs-sufficient trap the round-9 Rule
itself warns about, but here applied recursively to the Rule's own scope.
Practical resolution used this round: avoided the ambiguity entirely by
building 4 fresh approaches that target the Stabilization Conjecture via
genuinely NEW, non-circular mechanisms (density/pigeonhole magnitude bound;
finite-alphabet covering-design; well-ordering/minimal-counterexample;
cross-family Δ-system) that never invoke (MRS_S)/𝓥_S-finiteness as a
hypothesis — sidestepping the tension rather than resolving it, and
flagging the tension explicitly in the outline for the outline-reviewer to
judge independently (round 10, imo-2026-06).

ALWAYS: before accepting an explorer's "this narrower hypothesis survived
the refutation, it's a different quantity" claim as clearance to pursue it
as a general (for-every-core/for-every-index) target, trace it all the way
through the ALREADY-CERTIFIED downstream bridge chain to see what proving
it in full generality would imply for the WHOLE problem — round 11's
`(MRS_S)` (per-core antichain freeze) genuinely is untouched by round 9's
`(UB_S)`-refutation (confirmed: different quantity, minimal generators vs.
bundle size), but a one-line check (freeze at `n^*` ⟹ finite union of
antichains ⟹ `𝓥_S` finite, feeding the UNCONDITIONAL rest of the certified
`theorem-UBS-sufficiency.md` bridge that needs `(UB_S)` only once) showed
`(MRS_S)`-for-*every*-core would re-derive the entire already-abandoned
round 4-8 `(MRS)`/`𝓥`-finiteness program (round 6's Multi-Companion
Reduction Proposition already proved that equi-hard to FCBC). The correct,
narrower target restricts the sub-hypothesis to only the specific finite
set of objects (here: the cores of one doubly-infinite pair) that the
CURRENT reduction actually needs, not the general/global form the old
banned program used — outline that restriction explicitly, don't let the
approach silently drift back to the general form (round 11).

ALWAYS: when a problem's single remaining gap has converged across every
approach (e.g. imo-2026-06's Stabilization Conjecture, round 10, forced by
the already-certified Theorem SW), diversify the population by giving each
revised approach a structurally different PROOF TECHNIQUE for that same
target (analytic/pigeonhole; finite combinatorics/covering-design;
well-ordering/minimal-counterexample; extremal set theory) rather than
either (a) manufacturing a sham alternative top-level target, or (b)
letting 2+ approaches share the literal same mechanism under different
names — reuse each approach's own already-certified machinery (Domination
Lemma, S^+, Δ-system Dichotomy Lemma, H_100 empirics) as the seed for its
assigned distinct mechanism, so the diversity is genuine rather than
cosmetic (round 10, imo-2026-06).

ALWAYS: when an explorer finds a clean CASE SPLIT of a stuck gap (e.g.
imo-2026-06 round 12's jw-rigidity explorer splitting Conjecture (JW) into
"backbone exists" (5/7 tested pairs, closeable via an already-certified
cheap lemma) vs. "no backbone" (2/7, the true hard residual)), route the
easy case to ONE approach and hand the genuinely-hard residual to TWO
independent-mechanism approaches (reusing each's own already-built
toolkit) rather than spreading all approaches thin across the whole
unsplit gap — this concentrates rival techniques exactly where the
population still needs them, and is not the single-gap trap because each
approach still targets the WHOLE problem end to end via the same
already-certified reduction chain, only the SCOPE of its own remaining
open lemma narrows (round 12, imo-2026-06).

ALWAYS: before pivoting a stuck approach onto a superficially-similar new
target surfaced by another explorer, explicitly verify (or have the
revision state clearly as an open check) that the stuck approach's own
already-certified NEGATIVE result (e.g. imo-2026-06's No-Shortcut
Corollary, proving (MRS_S) equi-hard to an abandoned target) does NOT
also apply to the new target — two explorers independently confirming
"this is a logically different, strictly weaker object, not touched by
that equi-hardness proof" was the exact check that made the round-12
pivot of forced-primes-well-ordering safe; skipping this check risks
silently re-attempting a target already proven equivalent to a dead one
under a new name (round 12, imo-2026-06).

ALWAYS: when a standing "NEVER re-attempt X" Rule's own summary text uses
"equivalently"/"3 successive names for the same family" to describe a
refutation, re-read the ACTUAL CERTIFIED PROOF (not the Rule's gloss)
before treating the whole family as dead — round 13's imo-2026-06 audit
found the round-9 Rule banning "(MRS)/𝓥_S-finiteness/(UB_S) — equivalently
..." actually only refutes `(UB_S)` (its proof-by-contradiction uses
`B<∞`, literal content of `(UB_S)`'s own definition, not derivable from
`𝓥_S`-finiteness alone; `theorem-UBS-sufficiency.md` states only `(UB_S)
⟹ 𝓥_S finite`, a one-directional sufficiency, never `⟺`). A refuted
SUFFICIENT mechanism does not refute the TARGET it was aimed at — this is
the same trap round-9's own Rule warns against, but here the trap was
embedded in the Rule's own summary phrasing, not in a new explorer claim.
When reopening such a target, write the full re-derivation into the
approach file as a Step 0 and flag it explicitly "needs outline-reviewer
verification" rather than either (a) silently trusting the Rule's gloss
or (b) silently overriding it without evidence (round 13, imo-2026-06).

ALWAYS: when a proven Subset/containment relation exists between the
CURRENT live approaches' target and an EASIER, already-abandoned target
(e.g. imo-2026-06's certified Subset Lemma `𝓥_S ⊆ 𝓥_S^loc`, showing the
population drifted from the easier global object to the strictly harder
local one not because the easier one was refuted, but because its one
known proof mechanism died), treat reviving the easier target with a
GENUINELY NEW mechanism as legitimately diverse from the current field —
not a repeat of a dead approach — since success there would bypass every
live approach's target at once. Distinguish this from round-7's
`global-recruiter-finiteness` dead end (a core-INDEPENDENT reformulation,
proven equivalent-not-easier by a 3-line finite-union argument): a
per-core-decomposition framing of the same easier target is NOT covered
by that equivalence proof (round 13, imo-2026-06).

ALWAYS: when 3 parallel math-explorers converge on the SAME certified
mechanism (round 14: Lemma WF) applied 3 different ways, separate them
into (a) a cheap corollary/naming pass (near-zero risk, do first, e.g.
"Multi-Singleton Forcing" as a named Corollary of an already-certified
theorem), (b) low-risk concrete-instance closures reusing that corollary
(each a fresh, near-template-following build), and (c) a high-risk
general-existence attempt for the underlying conjecture across ALL
instances — do not let (c)'s speculative content block or dilute (a)/(b),
and do not let (a)/(b)'s success be mistaken for progress on (c) (round
14, imo-2026-06).

ALWAYS: distinguish a refuted UPPER BOUND ("sup of some quantity over a
whole class is infinite") from a claim about EXISTENCE or FREQUENCY of
small values within that same class — round 14's imo-2026-06 witness-
chaining generalization needs only that infinitely many/some class
members have a SMALL companion set, which `theorem-UBS-false-case-
II.md`'s refutation of a UNIFORM bound (`sup=∞`) does not touch at all
(sup=∞ is fully consistent with liminf being small, or small values
recurring with positive density) — flag this explicitly as a distinct,
still-open sub-question rather than either (a) assuming the old
refutation blocks the new weaker claim, or (b) assuming the weaker claim
is free just because it "sounds smaller" (round 14, imo-2026-06).

ALWAYS: when an explorer report claims to have "caught and fixed" its own
error mid-derivation (round 14's 4199-channels explorer, a witness-core-
disjointness mistake), do not just relay the claim — write an explicit
per-witness/per-channel disjointness re-check into the outline's skeleton
and flag it under "Watch out for" as needing independent re-verification
by the builder, since a self-reported fix is not the same as a reviewed
one (round 14, imo-2026-06).

ALWAYS: when a low-index-witness mechanism (e.g. Lemma WF) only requires
the witness's core to be disjoint from a TARGET class's core — not that
the witness come from one of the two "sides" of the pair being closed —
actively search for witnesses drawn from a THIRD, unrelated class (valid
whenever `|P_1|≥3`) before concluding a pair "resists" closure; round
14's imo-2026-06 case showed two explorers reached opposite conclusions
on the same pairs of `a_1=4199` because one searched only within-pair
witnesses (Multi-Singleton Forcing, found no closure) while the other
also searched the third disjoint core class and found an immediate
trivial closure via a shared witness that constrains both target classes
at once (round 14, imo-2026-06).

ALWAYS: when 2+ explorers independently surface the SAME crux-corpus
match with a claim it could bypass the whole apparatus (round 15's
`aimo-0030`/"Ana and Banana" — verbatim-identical recursive rule to
imo-2026-06), open it as ONE new all-or-nothing approach with every
borrowed step explicitly labeled "RECON ONLY (not yet re-proved)" vs.
"already re-derived from scratch" — do not let the excitement of a
big potential shortcut collapse the rest of the population; pair it
with 2-3 approaches continuing the cheapest available incremental
progress (here: a 1-line "Common-Recruiter Reuse" corollary that
closed 4 more channels of the workspace's hardest recurring instance
for free) so a failed/incomplete recon round still leaves the
population better off than before (round 15, imo-2026-06).
