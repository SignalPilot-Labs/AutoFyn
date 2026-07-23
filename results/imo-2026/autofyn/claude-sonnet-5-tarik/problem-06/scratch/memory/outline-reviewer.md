ALWAYS: check whether a "definitional device" a new approach builds on (e.g. a
custom Tight(n)/witness-set) is secretly forced to a trivial value by a
constraint already baked into the problem's own recursive definition — compute
it directly on a small simulated example before trusting the outline's prose.
Caught a fatal flaw this way on imo-2026-06 round 1: an approach defined
Tight(n) via "no later index shares a prime with a_i," but the problem's own
recursion forces gcd(a_i,a_{i+1})>1 for every i, so the set degenerated to a
singleton for a content-free reason, and the outline's next step (bounding
needed primes by that set) was a non-sequitur even granting the (trivial)
claim. (round 1)

ALWAYS: for sequence/recursive-definition problems, actually run the greedy
process in python (math.gcd, small loop) for the stress-test input the
outliner names, rather than trusting its reported simulation results at face
value — cheap (seconds) and either confirms or contradicts specific outline
claims (e.g. "collapses to single dominant prime" for a1=21/55 was
confirmed this way in round 1).

ALWAYS: when the outliner itself flags "these approaches may all hit the same
wall," don't reflexively RETHINK the whole field — CLAUDE.md says sharing a
target lemma via genuinely different routes (existence-proof vs.
explicit-construction vs. bound-without-structure) is legitimate diversity.
Instead cut only approaches with an independent, provable flaw, keep the
mechanistically-distinct survivors, and explicitly pre-warn the orchestrator
in the report about what evidence next round would justify forcing a truly
different framing (e.g. "if both X and Y report the identical stuck
inequality next round, that's the trigger").

NEVER: assume `results/<id>/approaches/<slug>.md` files exist just because the
outliner's report describes them in detail — round 1 of imo-2026-06 had an
outliner that wrote a full report to /tmp/round-1/proof-outliner.md but left
results/<id>/approaches/ empty. Check with `ls`/`find` before writing "read
each approach file" review notes as if the files were read; note the gap in
the report so builders know to seed the files themselves.

NEVER: treat "each recruitment event resolves a specific earlier index
permanently" as sufficient to prove a *global* recruitment-finiteness claim —
it only bounds recruitments *per index*; with infinitely many indices over
time, the total count is unbounded unless the outline also states an explicit
rate inequality (recruitment rate vs. resolution rate). Push outlines that
skip this step to state the actual quantities being compared, not just the
per-index mechanism.

ALWAYS: when an outliner "corrects" a numerically-refuted definition (e.g.
round 1's H_n bug), re-derive/re-test the NEW definition too, don't assume the
correction actually fixed the root cause — round 2 of imo-2026-06 retargeted
H_n (any co-occurring prime, refuted) to B := "primes dividing infinitely many
a_n" (claimed finite), but this is ALSO false: for any periodic-difference
sequence a_{n+T}=a_n+L, every prime q coprime to L that divides one term of a
fixed residue class a_r+kL divides infinitely many terms of it (density 1/q,
periodic in k) — so B is essentially cofinite, not finite. Verified both by a
short rigorous argument and numerically (unbounded growth, no leveling, on the
already-solved a_1=15 case). The fix moved the same "too-permissive filter"
bug down one level instead of fixing it. General lesson: any proposed
"backbone/persistent set" definition for this problem shape must be tested
against the SAME already-solved small case the previous definition was
refuted on, not just checked for internal plausibility.

ALWAYS: when multiple approaches converge on the same open target lemma but
one approach (often the newest/riskiest one, opened for mechanism diversity)
uses a DIFFERENT formalization of that target, test each formalization
independently before assuming they're equivalent — they often aren't, and the
newest one can turn out to be the only correct one. On imo-2026-06 round 2,
`persistent-backbone-monovariant`'s canonical-minimal-witness set
w(i,j)=min(rad(a_i)∩rad(a_j)) was empirically exactly right (exhaustively
{2,3,5} across all ~4.5M pairs up to n=3000 for a_1=15, stable early even on
the hard a_1=247 case) while the sibling's "equivalent" B was false. A cheap
exhaustive/dense small-case computation (smallest-prime-factor of pairwise
gcd, not sympy factorint, for speed) settles this fast.

ALWAYS: for "persistent divisor" / "backbone" style claims, prefer a
notion tied to a CAUSAL/EXTREMAL role (dominant prime in a pigeonhole
argument, or minimal common witness between two specific terms) over a
notion tied to raw frequency ("divides infinitely many terms" or "ever
co-occurs") — frequency-based notions are systematically too permissive for
this problem shape (both round 1's H_n and round 2's B failed this way);
extremal/minimal notions (canonical witness, dominant-prime argmax) are the
pattern that has held up so far.

ALWAYS: when an outline reduces a hard target to sub-claim X via a clean,
checkable algebra chain (e.g. "if omega(a_n)=O(1) then dominant-prime is
O(1)"), separately check whether X, even if proved, actually implies the
FULL target or only a *necessary* fragment of it — round 3 of imo-2026-06 had
two sibling outlines (persistent-backbone-monovariant, forced-primes-well-
ordering) both reduce cleanly to a growth-rate sub-claim that only bounds
WHICH primes are ever "dominant"/"forced" (necessity), while the actual
target (a finite covering set H hitting EVERY pair, not just consecutive
steps) additionally needs a sufficiency argument that neither outline even
sketched a mechanism for — flagged as CHANGES REQUESTED, not waved through
just because the algebra chain itself was correct.

ALWAYS: when the outline-reviewer's copy-mechanism spawns two siblings on the
same target via nominally different techniques (e.g. induction vs.
well-ordering), check whether their OPEN sub-lemmas secretly need the same
missing analytic bridge fact (not just the same target statement) — if so,
this is weaker diversity than it looks, even though it's still permitted per
CLAUDE.md (a target lemma via genuinely different routes is legitimate). On
imo-2026-06 round 3, both siblings' hard step reduced to an unstated bridge
between "count of newly-recruited/forced primes" and "omega(a_n) growth,"
just applied in opposite logical directions — write an explicit trigger for
the orchestrator ("if both report the identical stuck bridge next round,
stop iterating on this pair specifically") rather than either RETHINKing a
sound-technique outline prematurely or silently ignoring the overlap.

ALWAYS: independently re-verify at least one numerical claim per approach
file yourself (cheap Python, exact arithmetic) even when a math-explorer
report already backs it with many test cases — spot-checking on a FRESH,
previously-untested input (not one of the explorer's own listed cases) is
worth the ~1 minute cost and catches silent overfitting to the tested set;
round 3 did this for both `F_M` (forced-primes) and `H_K` (explicit-window)
on fresh a_1 values (91, 1073) neither prior report had used, both confirmed.

ALWAYS: when an outline splits a hard target into two labeled sub-lemmas
("(a) bounded X, (b) bounded Y ⟹ conclusion"), actually write out, in code or
by hand, EVERY way the underlying process can change state, and check each
sub-lemma's literal definition covers its share — don't accept "if (a) and
(b) both hold, then..." at face value just because each sub-lemma individually
sounds plausible. On imo-2026-06 round 5, `imprint-automaton-periodicity`'s
"Bounded Core Family" (a) was defined to bound only radical values that ever
TRIGGER a collapse (r≥1 removal event); it silently omitted values that are
inserted and simply never later dominated (permanent survivors, r=0 events
with no future removal). A 5-line python simulation (count insert-events vs.
collapse-events vs. surviving-inserts) found a case (`a_1=91`) with ZERO
collapse events yet 3 permanently-surviving values — i.e. (a) was vacuously
true while the thing Step 3 actually needed bounded was untouched. This class
of gap (a sub-lemma quietly covers only one branch of a case split, e.g. only
the "event fires" case and not the "event never fires but the entity still
accumulates" case) is cheap to catch with a state-transition tally in Python
before the builder invests in writing the full argument around it.

NEVER: assume a "verbatim adaptation" claim (e.g. "the certified proof only
uses finiteness of the universe, not that it's a prefix, so it transfers to a
restricted/local universe") is true just because it sounds plausible — trace
through the cited proof's actual steps line-by-line and confirm none of them
implicitly used prefix/ordering structure. Did this for
`forced-primes-well-ordering`'s channel-localized Corollary W3′ transfer
claim (round 5) — confirmed correct by re-deriving the localized proof
directly, not by trusting the outline's assertion.

ALWAYS: when independently re-simulating a "minimal/inclusion-minimal
antichain accumulates over time" claim (e.g. 𝓥_S = union of every value ever
locally-minimal), track the actual domination/removal dynamics (insert,
check subset-of-existing, remove supersets) — do NOT approximate it as "the
set of all realized values with the target property," which silently
includes values that were dominated/never-minimal and wildly inflates the
count. Caught myself doing exactly this on imo-2026-06 round 6 (got 1037
"elements" for a_1=247's S={13} channel via a buggy V.add() that fired on
every realized radical, not just newly-minimal ones; the correct simulation,
gating the add on `not is_dominated`, gave the correct answer of 3, matching
the explorer's claim exactly). Always sanity-check a "channel freezes /
never changes" claim against a KNOWN correctly-simulated baseline (e.g. the
already-solved a_1=15 case) before trusting either the explorer's number or
your own quick script.

ALWAYS: when 4 sibling outlines all attack the same shared gap and none is
individually RETHINK-worthy, still read each OPEN sub-lemma's actual
mechanism (not just its name) side-by-side — two of them can be near-
verbatim the same attempted bridge (identical certified ingredients,
identical density/pigeonhole combination logic) even when their outline
prose uses different vocabulary ("chain count" vs "companion-event count").
When found (imo-2026-06 round 6: persistent-backbone-monovariant's
Growth-Budget Lemma and imprint-automaton-periodicity's Companion-Count
Bound both reduce to "Lemma FOM's fan-size bound + Lemma 1's linear growth,
via a pointwise-to-cumulative pigeonhole" — the exact bridge already flagged
insufficient in isolation in rounds 3-4), trim the build set below the full
sibling count (CLAUDE.md's "few strongest, normally 1-3" licenses this) by
deferring — not cutting — the weaker-Elo/more-redundant one, rather than
building both and discovering the identical wall twice in one round.

ALWAYS: when an outline reduces target X to open hypothesis Y via a new
mechanism (e.g. sunflower-bundle-closure round 8's Delta-system route to
Lambda_S-finiteness via (UB_S)), explicitly check whether Y is trivially
EQUIVALENT to X (making the "reduction" a circular restatement, like this
workspace's earlier H=rad(L_per) and Pool Lemma traps) by testing both
directions by hand: does X ALSO trivially imply Y? On imo-2026-06 round 8,
checked whether Lambda_S-finite trivially gives (UB_S) (sup bundle size
bounded) -- it does NOT, because (UB_S) as stated ranges over ALL realized
indices in I_S, not just the ones that ever reach the minimal antichain, so
a dominated/never-minimal index could carry an unboundedly large bundle even
while Lambda_S stays finite. This one-directional-only check is what
distinguishes real progress from a relabeling; do it explicitly, don't just
trust the outline's own "this is not circular" assertion.

ALWAYS: when a math-explorer proves a "target A is a proper subset of /
insufficient for target B" claim (e.g. imo-2026-06 round 8's thread-
unification explorer showing permanent-bundle-count is a proper subset of
full V_S-finiteness, since transient antichain members are uncounted),
verify the claim with a concrete counterexample from the explorer's own
regenerated data (not just its prose) before accepting a same-round outline
that retargets an approach away from A and toward B -- round 8's explorer
supplied an exact transient instance (a_1291's bundle, alive n=1291 to
n=2575) that a permanent-only argument provably never touches; this is a
much stronger form of insurance against overclaiming than a general
sufficiency argument alone.

ALWAYS: when an outline reframes "hypothesis X (sufficient for the whole
problem) is likely false" as GOOD news because X was never proved necessary,
verify this with two checks before approving: (1) grep the certifying lemma
file's literal statement for a one-way arrow vs an iff (round 9's
theorem-UBS-sufficiency.md is genuinely `⟹`, not `⟺` — confirmed by reading
the file, not trusting the outline's paraphrase); (2) actually test the
NEW target claim the outline pivots to (e.g. "every term/pair still touches a
small fixed set H") with fresh code on the SAME hard case that broke the old
hypothesis — round 9's plain small-window candidate looked perfect on two
easy cases (a_1=247, 2747, zero violations to n~500k) but had a concrete,
cheap-to-find counterexample on the one hard case (a_1=21528751, violation at
n=596 vs n=863, needing a bridge prime the outline hadn't anticipated) — a
review that only re-ran the explorer's own two tested cases would have missed
this. Always add the workspace's own designated "hardest case" to any
re-verification even if the outline/explorers didn't test it there.

ALWAYS: when an outline states a sub-lemma as `|A_n|=o(N)` (or any
asymptotic-vanishing claim) but the "Watch out" section of the SAME outline
already hints a weaker bound (e.g. "just needs a lower bound, not an exact
rate") would suffice, actually measure the quantity directly (a few
checkpoints across a 5-10x range is enough) before approving the stronger
literal form — round 9's sunflower-bundle-closure needed `|I_{P1}|=o(N)`
(density→0) but measurement showed a STABLE POSITIVE density (~11.6%/~2.0%,
identical at every checkpoint from N=50k to N=500k) on both tested cases, the
opposite of o(N); the argument survives by substituting the correct weaker
claim ("density bounded away from 1", which the same data proves), but
building the literal o(N) form as scoped would have wasted a full round on a
false sub-lemma. This is the round 2 "H_n"/wrong-quantifier-direction bug
recurring in a new guise — always re-derive which DIRECTION of bound the
final contradiction/conclusion actually needs, independent of how the
outline's Skeleton section phrases it.

ALWAYS: when an outline's skeleton invokes a previously-certified lemma
"directly" on a new object, re-read that lemma's EXACT stated hypothesis
(not the outline's paraphrase) and check whether a fact ALREADY certified
elsewhere in this same workspace makes that hypothesis likely false for the
new object. Round 10's sunflower-bundle-closure invoked the certified
Δ-system Dichotomy Lemma (hypothesis: family of sets each of size ≤ FIXED M)
on companion-bundle families Q_S — but this same workspace's own
theorem-UBS-false-case-II (round 9) proves companion-bundle SIZE is
unbounded for at least some core, and a fresh independent simulation
confirmed real, still-growing bundle size (6→7 past n=400k) on the EXACT
core (a_1=247, S={13}) the round's field targets. Also constructed a cheap
explicit counterexample (nested sets F_n={1,...,n}) proving the dichotomy's
conclusion genuinely fails without the bounded-size hypothesis (neither a
pairwise-disjoint nor a sunflower infinite sub-family exists) — so this is a
real, not merely technical, precondition. The outline never checked this;
catching it pre-build (rather than after a builder writes 200 lines on top
of a misapplied citation) is exactly what the outline review step is for.

NEVER: assume an approach whose "genuinely different mechanism" framing
sounds distinct from its siblings actually has distinct OPEN content —
read the outline's final open-gap step literally and check whether any
proposed sub-option is already self-refuted by data cited earlier in the
SAME outline. Round 10's explicit-window-backbone-construction proposed two
options for its Step 3; option (b) was explicitly noted, by the outline's
own citation of this round's H100-stabilization explorer, to be non-viable
(realized-signature count does not saturate even at N=160M) — leaving only
option (a), which turned out to be verbatim the same "pin the greedy rule's
forced intersection to a bounded window" gap already being attacked by two
siblings in different vocabulary. Defer (don't build) such a slug in favor
of siblings offering genuinely new content that round, per the round-6 Rule
on this exact redundancy pattern.

ALWAYS: when an outline claims two differently-scoped variants of a
definition (e.g. a "local, competitors-restricted-to-a-subset" antichain
vs. a "global" one) satisfy a subset/superset relationship that a proof
depends on, verify it with a SIDE-BY-SIDE simulation tracking both objects
on the same generated sequence, not just a hand proof — round 11 of
imo-2026-06 did this for fk's `(MRS_S)` (local antichain `M_n^S`, competitors
drawn only from `I_S`) vs. the already-certified global `𝓥_S`: the
one-directional containment (global-restricted ⊆ local) held on every test,
but the local antichain was found genuinely STRICTLY larger on 3 of 6 tested
proper cores of the hardest instance (`a_1=21528751`) — confirming the two
objects are NOT interchangeable and that the harder-looking one is exactly
the one the outline needed, not a relabeling. Cheap (~1 minute) and catches
both "the mechanism doesn't actually hold" and "these are secretly the same
thing" failure modes at once.

ALWAYS: when an outline "legitimately scopes down" a previously-proven-
equi-hard target (e.g. "prove X only for objects in structural sub-case Y"
instead of "for every object"), check whether sub-case Y is actually a
material restriction in the WORST CASE, not just nominally narrower — round
11 of imo-2026-06 found that "cores appearing in doubly-infinite pairs"
could, once there are ≥2 infinite proper cores (the generic case), still be
EVERY infinite proper core, i.e. no real narrowing at all. This doesn't
sink the outline (the scoping is still legitimate because the downstream
consumer is a strictly weaker per-pair lemma, not the banned whole-`𝓥`
assembly), but it must be flagged as a residual risk for the builder to
report honestly rather than silently discover mid-build.

ALWAYS: when a sibling outline "restates the identical [lemma X] statement"
from another approach and proposes to apply it to a NEW scope/case-split
that a same-round explorer defined, re-check X's literal preconditions
against the exact data that defined the new scope's boundary — a scope
defined as "the cases where X's precondition FAILS" makes "restate X and
apply it here" structurally vacuous by construction, not just hard. Caught
this on imo-2026-06 round 12: `sunflower-inadmissibility-toolkit` defined
"Case A" as pairs where a per-class companion-set backbone is nonempty AND
exactly realized, and explicitly ceded "Case B" (the complement) to two
siblings; one sibling (`forced-primes-well-ordering`) then proposed to
"restate the identical Backbone Permanence Lemma" and bridge it to Case B
— but Case B is *by definition* where the backbone is empty or not
exactly realized, so for one of its two target instances (`a_1=247`,
confirmed both sides literally `\varnothing` from the 2nd realized member
through N=30000, fresh Python) there was nothing to prove permanent and
nothing to bridge to. A ~2-minute Python check (compute the backbone for
both sides of both named instances) caught this cleanly before the builder
would have spent a full round on a vacuous target.

ALWAYS: when a new outline claims target X is "provably weaker" than the
field's current target Y and cites a Step-0 audit ruling out specific named
prior refutations, don't stop once those NAMED refutations check out — grep
the whole lemmas/ directory and every currently-live sibling approach file
for ANY other already-certified result about X specifically (not just Y),
including ones the outline's own audit didn't think to check. On
imo-2026-06 round 13, `core-antichain-content-freeze` correctly ruled out
two named blockers ((UB_S) refutation, global-recruiter-finiteness) for its
target "𝓥_S finite for every core," but never checked the round-6
Multi-Companion Reduction Proposition + round-11 No-Shortcut Corollary —
both already certified, and the latter is literally quoted as a standing
"do NOT pursue this as a shortcut" warning inside a currently-live sibling
approach file (`forced-primes-well-ordering.md` §J) — which together prove
X is EQUI-HARD to FCBC (not weaker) for any core with a realized
multi-companion bundle, a fact already confirmed for the workspace's own
hardest concrete instance. A targeted grep for the exact target's name
across `lemmas/*.md` and sibling `approaches/*.md` (not just the files the
outline itself cites) takes ~2 minutes and would have caught this before
the audit was even drafted — cheap-kill it (RETHINK, unregistered) rather
than approve on the strength of a partial audit.

ALWAYS: when an outline adapts a crux by paraphrase ("Claim 2 says...",
UNVERIFIED per the explorer's own caveat), pull the crux's actual JSON entry
yourself (`past_problems_database.json`/`past_crux_moves_database.json`,
filter by `problem_id`) before trusting the paraphrase — round 15's
`aimo-0030` adaptation turned out to have the FULL official solution text,
including "Comment 2/3" (the exact recursive construction + mod-P
periodicity claim the outline needed), sitting verbatim in the `solutions`
field; reading it directly showed the outline's hardest-looking steps
(Claims 1-3, Main Dichotomy) are a translation task, not a from-scratch
discovery task, materially changing the risk assessment from what the
paraphrase alone conveyed. Also: when an outline's own "prose bridge"
between a crux's framing (e.g. a game's recursive good/bad classification)
and the target problem's native objects (e.g. a directly-defined greedy
sequence) is asserted but never proven, try to prove it yourself by hand
(it is often a short induction) rather than waving it through as "just
vocabulary" — this is exactly the kind of silently-missing load-bearing
lemma CLAUDE.md's rigor rules are meant to catch, and it is usually cheap
to close directly from the problem's own recursive definition.

ALWAYS: when an outline's "sanity check" step names specific expected
numbers (e.g. "verify this reproduces T=8, L=30"), actually compute them —
don't accept the description at face value even when it cites an already-
certified fact. Round 15's crux-adaptation outline's Step 6 claimed its own
formula would "reproduce T=8,L=30 exactly" for a_1=15, but the formula
(L:=P=product of ALL primes <= a_1) necessarily gives L=30030, T=8008 —
consistent with (an exact 1001x multiple of) the certified minimal period,
but literally NOT equal to the stated numbers. A ~2-minute direct
computation caught a wording bug that would have derailed the builder
(who'd get "wrong" numbers from a correct formula and might wrongly
conclude the whole approach broken) — flag the corrected expectation
explicitly rather than leaving the builder to discover the discrepancy
mid-build.
