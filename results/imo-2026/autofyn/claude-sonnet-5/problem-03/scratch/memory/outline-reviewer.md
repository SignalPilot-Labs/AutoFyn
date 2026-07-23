ALWAYS: when several approaches share one reduction lemma (e.g. a greedy/exchange lemma reducing
a game to order statistics), check whether that shared lemma is itself low-risk (a near-forced,
standard fact) before flagging it as a single-gap-trap violation — sharing a truly load-bearing
*prerequisite* lemma across whole-attempt approaches is fine and is what the shared lemmas/
cache is for; the real trap is when multiple approaches share the same *hard, unresolved*
structural claim deeper in the proof (round 1: three of four approaches leaned on the same
unproven "XY's response is piecewise-affine/finitely-patterned" claim — that's the sharing worth
flagging, not the shared greedy-reduction lemma).

ALWAYS: check approach files for cross-references to lemma/approach filenames that don't actually
exist in this round's file set (leftover names from earlier drafts) and flag them to builders
explicitly — cheap to catch, wastes builder time if missed (round 1).

NEVER: default the build set to all registered approaches just because none is a RETHINK — pick
the 1-3 strongest per CLAUDE.md and bench the more exploratory/underdeveloped ones (no concrete
lemma or algebra yet) for a later round once the concrete ones either succeed or stall (round 1).

ALWAYS: when an outline claims a game-theoretic "adversary's canonical move" (e.g. "XY
bisects" / "XY matches piece i to piece j") is sufficient to cover a case, brute-force
check with a small script over ALL of the adversary's combinatorial options (not just the
named 1-2 moves) on a few concrete instances -- for imo-2026-03 this found a third response
family (splitting one piece to simultaneously match TWO other existing pieces) that beats
both named canonical moves in some instances, which the outline had missed; this didn't
invalidate the upper-bound direction (which only needs SOME sufficient strategy) but would
have broken a sibling approach relying on "the" locally-optimal pattern for a uniqueness/
smoothing argument (round 2).

ALWAYS: distinguish "needs *a* sufficient strategy" from "needs the *true optimal*
strategy" when multiple approaches share one mechanism/lemma -- an upper-bound-by-
explicit-strategy approach only needs the former (weaker, easier) while a smoothing/
uniqueness/concavity approach needs the latter (stronger, harder); approaches that look
like they "reduce to the same computation" per the outline may actually differ in this
exact way, and treating them as equally hard is a mistake worth catching before both
builders duplicate effort on what looks like, but isn't, the identical gap (round 2).

ALWAYS: check whether a "hedge"/alternate-technique approach still stands as a
self-contained whole attempt (own construction/lower-bound sketch in its own words) or has
quietly become "the same gap as approach X, not independently open" -- the latter is the
single-slice-of-one-proof trap CLAUDE.md forbids even when the file wasn't literally split
on purpose; bench it from the build set rather than paying for redundant builder effort on
an approach that has converged onto an identical remaining computation (round 2).

ALWAYS: independently brute-force/grid-check a "dominance" or "X's move never helps"
sub-claim buried inside a larger induction skeleton (not just the skeleton's headline
claim) -- e.g. a lower-bound induction's "cutting the top piece more than once never
beats bisecting it once" is a DIFFERENT claim from "which single-cut tie/bisect position
is best," and the outline may only state and defend the latter while silently needing the
former too; a cheap grid search (few hundred lines of Python) either surfaces a real
missing case or gives genuine corroborating evidence to hand the builder (round 3,
imo-2026-03: multi-cut-on-a1 was unaddressed in a lower-bound skeleton's Branch B).

ALWAYS: when an outline restates a *lower-bound* (universal-over-all-adversary-strategies)
claim in terms of a *reformulation lemma* that was originally certified/proved only for an
*upper-bound* (existential/sufficient-strategy) use, re-read the certified lemma file's own
"Consequence"/scope section verbatim -- it may explicitly disclaim completeness ("not
claimed to capture the entire strategy space... only that these are always achievable")
even while the new outline's Step 0 asserts a flat equivalence ("X's response IS EXACTLY a
sequence of these operations"). This exact substitution (sufficiency-for-upper-bound lemma
silently repurposed as completeness-for-lower-bound) is a subtle, easy-to-miss overclaim
that both an outliner and multiple explorers can miss in the same round; catching it only
requires re-reading the lemma file's own caveats side-by-side with the new skeleton's Step 0
language, not new computation (round 4, imo-2026-03: Lemma D/M, certified sufficient-only for
achievability, was silently treated as complete/exact in two sibling lower-bound skeletons'
Step 0 in the same round).

ALWAYS: when a new candidate potential/monovariant Φ is proposed for a game-lower-bound proof
(properties P1 normalization / P2 monovariance / P3 floor), test P2 against the SIMPLEST
possible move (one operation) applied to the exact normalization point (P1's own state)
FIRST, before any tabulation against "known tie data" the outline suggests -- this is a 2-line
computation that can kill a candidate immediately and far more decisively than the outline's
own anticipated failure mode ("false for arbitrary/unreachable multisets"); a candidate that
fails on the canonical extremal trajectory itself is dead on arrival, not merely "needs
restriction to a reachable subclass" (round 4, imo-2026-03: Φ:=S(M)/(2^|M|-1) failed
immediately under a bisect operation on D_2's own dyadic point, decreasing 1/7→1/15, while
holding under a match operation on the same point -- a sharper, cheaper diagnosis than the
outline's own "known caveat" anticipated).

ALWAYS: when an outline's "stress test" claims a converse-flavored pattern from a SMALL sample
(e.g. "5/5 non-superincreasing sequences admitted shortcuts, confirming X is load-bearing"),
re-run the same generator with a fresh, larger sample of your own before trusting the framing --
a 5-sample anecdote can read as "condition A is necessary" when it is only evidence condition A
is sufficient; round 5 (imo-2026-03) found the outline's own sample was 5/5 (100%) but an
independent 15-sample re-run found only 6/15 (40%) admitted a shortcut on non-superincreasing
sequences -- the underlying mathematical claim (strict superincreasing ⟹ no shortcut,
sufficiency only) was still correct and didn't need the wording changed for soundness, but a
"the property is EXACTLY what's needed" (two-sided) framing would have been a real overclaim;
catching this only cost one extra script run with a different seed and larger N.

ALWAYS: independently re-implement the outline's own numeric harness from scratch (fresh code,
not the outliner's script) and push its verification range BEYOND what the outline itself
tested (e.g. one or two more values of the scaling parameter, or a somewhat larger random
sample) rather than merely reproducing the same range -- this costs little extra time when the
state space is small/bounded, and either (a) surfaces a break the outline's narrower test
missed, or (b) hands the builder genuinely new corroborating evidence beyond what's already on
file (round 5, imo-2026-03: independently extended a min-ops-to-zero BFS from the outline's
m≤5 to m≤7, and a policy stress-test from the outline's m≤6 to m≤8, both clean, both now
citable as fresh evidence, not just a re-check).

ALWAYS: when two sibling approach files divide a problem's natural case split between them
(e.g. one owns Case (i), the other Case (ii), each with a one-paragraph "import pointer"
deferring to the other's UNPROVEN result instead of a certified lemma), flag this explicitly
as bordering CLAUDE.md's "one proof split across slugs" trap even if each file's own induction
skeleton is nominally general enough to attempt either case -- it is not automatically a
RETHINK (the mechanisms can be genuinely different techniques, and the case split can track a
real mathematical dichotomy rather than an arbitrary convenience partition), but it must be
named in the report and watched: don't let a third approach join the same split, and don't let
an "import pointer" to an unproven sibling result become permanent (round 5, imo-2026-03:
dyadic-cascade-induction defers general-m Case (ii) to potential-weighting-upper-bound's
unproven §6; judged acceptable this round but flagged for future rounds to watch).

ALWAYS: when a dispatch explicitly asks you to verify a new DP/induction mechanism "genuinely
replaces" a previously-dead local-exchange technique (not just rebrands it), trace the SAME
counterexample the explorer used through the new mechanism by hand and check which of the
multiple tied-optimal witnesses the new recursion can/cannot express -- this both confirms the
new mechanism is structurally different (it captures a witness the dead technique never could)
AND usually surfaces the exact sub-case still open (the one witness the recursion also can't
yet express), which is more precise than trusting the outline's own prose description of "the
open gap" (round 6/7, imo-2026-03: reconstructing counterexample Y=(43,33,20,16,11,8,2), b=2's
two tied optima through potential-weighting-upper-bound's new non-crossing-DP §8 showed one
witness fits cleanly via the inside/outside split while the other requires an inside-outside
crossing arc -- confirming the DP is a genuine upgrade, not a rehash, while also making the
"outside-crossing-arc" gap concrete rather than a vague prose phrase).

ALWAYS: when an outline proposes extending an already-certified "forced value" chain (e.g.
g(1)=1, g(2)=2 forced by a weak-duality argument) to the next integer, do the one extra
algebra step yourself before approving -- it is cheap (reuses the certified lemma's own
inequality/Lipschitz-bound machinery) and either corroborates the outline's plan is feasible or
independently locates exactly where the forcing stops, turning "check if it generalizes" from an
unverified task into a task with real, cited supporting evidence for the build set (round 7,
imo-2026-03: hand-derived g(3)=3 forced via reachable witness {3,2} plus Lemma B, then showed
g(4) is NOT pinned by the same technique, independently corroborating the file's own "informal
slack at g(4)" note before the builder spends effort on it).

ALWAYS: when an outline's induction reduces a branch to "a fresh same-gap `(size-1)`-instance"
by inserting a newly-computed derived value into a reduced list, test BOTH readings computationally
before approving: (a) treating the derived value as an ordinary, further-selectable/matchable
element of the new list (i.e. literally calling the same recursive function on it), and (b)
treating it as a FIXED value contributing via block-extraction, with only the untouched original
elements remaining selectable. These can give different answers -- reading (a) is systematically
too permissive (silently allows an extra operation the original one-shot/flat definition forbids)
and will UNDERSHOOT the true optimum, breaking the branch-decomposition identity; reading (b) is
usually the mathematically correct one but the outline's own prose ("new list Y''... reduces to a
same-gap instance") often reads exactly like (a). A cheap ~40-line brute-force script with random
small instances resolves which reading is intended and whether the outline's own wording risks
misleading a builder into the wrong (over-permissive) one (round 8, imo-2026-03:
potential-weighting-upper-bound's §10 MATCH-branch reduction -- reading (a) gave 3 mismatches in
60 trials, reading (b) gave 0 mismatches in 80 trials; the underlying math was sound but the
prose was exactly ambiguous enough to invite the wrong reading, which is also literally the trap
the section's own "Watch out for" note warns against).

ALWAYS: when an outline gives a concrete illustrative numeric example for a "reachable state"
claim (e.g. "at m=k, the minimizer is (specific tuple)"), check TWO cheap invariants before
trusting it: (1) does the element count match what the claimed number of operations from the
claimed starting multiset would produce (each D/M-style operation changes count by a fixed,
known amount -- a mismatch means the example requires zero operations, forcing it to equal the
start state exactly); (2) does the total sum obey the operation's monotonicity (e.g. D/M
operations here are non-sum-increasing) relative to the claimed start. Both checks are one-line
arithmetic and can decisively prove an illustrative example is fabricated/miscalculated without
running any search (round 8, imo-2026-03: concavity-minimax-duality's claimed "m=6 minimizer"
had 7 elements, which forces 0 operations from D_6, i.e. must equal D_6 exactly -- but its sum
(99) didn't match D_6's sum (127), proving it unreachable; this undermined the section's own
motivating evidence for its central mechanism even though the section's headline numeric
conclusion independently re-verified as still true via a fresh BFS).

ALWAYS: when an outline's narrative-only revision (no new lemma, just a "scope correction") claims
two sibling proof branches (e.g. Case (i)/Case (ii) of one induction) are welded into a single joint
induction rather than independently generalizable, trace the actual inductive-step proof text itself
(not just the narrative summary) to confirm it literally invokes the FULL induction hypothesis (both
branches) at the lower level, applied to an ARBITRARY residual not guaranteed to fall back into the
same branch -- this is a cheap text-tracing check (no computation needed) that distinguishes a correct
"these facts rise and fall together" claim from a sneaky one-sided overclaim, and also confirms the
narrative correctly frames the consequence as conditional ("once X closes, Y closes too") rather than
asserting the joint result is already established (round 9, imo-2026-03: dyadic-cascade-induction's
round-9 note claiming "general n>=4 is not a separate frontier" checked out exactly this way -- §2d's
proof literally invokes "the strong induction hypothesis at level m-1 -- both forms (A) and (B)" on an
arbitrary residual, confirming Case (i) is welded to Case (ii), and the note's own conditional framing
was accurate, not an overclaim).

ALWAYS: when an outline reduces a whole remaining gap to "one clean structural claim X" via a stated
short elementary implication (e.g. "structural invariant X => target inequality, 5 lines"), re-derive
that implication yourself from the definitions BEFORE trusting the outline's own derivation, and then
separately verify X numerically on real reachable states (not just the implication in the abstract) --
this catches both a subtly wrong implication AND a genuine but differently-scoped numeric claim in one
pass; pushing the numeric check one level beyond what the outline/explorer already ran (cheap when the
state space is a BFS with exponential-looking but actually modest growth) both corroborates and gives
fresh, citable evidence (round 9, imo-2026-03: independently re-derived concavity-minimax-duality's
"Distinct-Bucket + Integer-Preservation => e_g*(M)>=ceil(|M|/2)>=1" implication from scratch, confirmed
it is in fact a near-trivial consequence of "bucket = level set", then independently re-ran the BFS to
m=7 (18537 states, matching the file's own count) with 0 collisions and 0 inequality violations).

ALWAYS: when a certified lemma's disjointness/invariant claim is stated for "simultaneously
active" objects in one formalism, but a new outline section silently reuses it for objects that
may exist at DIFFERENT times along the same construction (e.g. cut-pieces produced at different
stages of a multi-cut strategy), flag this as an unproved strengthening even if it is highly
plausible (e.g. via an easy laminar-family/ancestor-descendant argument) -- require the builder
to state and prove the extension explicitly rather than cite the original certified lemma
verbatim, since the literal certified statement does not cover it (round 8, imo-2026-03:
dyadic-cascade-induction's #X>=2 even bucket reused superincreasing-no-early-zero.md's
"simultaneously-active tokens are pairwise disjoint" invariant (I1) for cycle-participant pieces
that need not all be active at the same time -- inherited unflagged from round 7's own honest-gap
writeup, worth catching explicitly this round).

ALWAYS: when an outline proposes a "fix a canonical/frozen optimal witness and locally repair it"
mechanism (e.g. uncross one optimal selection's matching in place, holding all other structure
fixed) as a NEW replacement for a just-killed mechanism of the exact same logical shape (a prior
"local exchange on a fixed support" dead end), independently push the outline's own numeric
verification range PAST what it reports BEFORE trusting the "0 failures in the needed regime"
claim -- these witness-repair claims are exactly the shape that keeps failing in this project
(round 6/7's general-budget local exchange; round 9's unconditional MATCH-aggregate; round 9's
claimed 500/500 |B|<=1 generalization; round 10's own |B|>=2 generalization) because the TRUE
optimal witness's identity (which elements participate) is not always locally stable -- a single
extra value of the outer parameter (e.g. list size p one larger than what the outline tested) can
surface a real counterexample a smaller sweep missed, including at the induction's own BASE CASE,
not just deep in the general step (round 10, imo-2026-03: outline's own "204+ zero-failure
instances at b=p-1, p=2..8" for the new Fixed-Support Uncrossing Conjecture was contradicted by a
fresh sweep at the SAME p range, seeds only -- found a hand-verifiable base-case (|M|=2)
counterexample Y=(7,5,4,4,3,1),b=5: OPT=0 but both non-crossing re-pairings of the same crossing
witness's support give 2 and 4, both >0 -- while the underlying top-level target OPT=NC itself
remained true via a DIFFERENT non-crossing witness, exactly diagnosing that the mechanism, not the
theorem, is what's false).

ALWAYS: when checking a "restrict to full budget" patch for a witness-repair conjecture that fails
under budget slack, first check the elementary index identity relating cost/support-size/budget
(e.g. |K|+|D|+2|M|=p, cost=|D|+|M|=b) to see whether "full budget used" structurally forces the
problematic substructure (e.g. |M|<=1, which can never cross) to vanish -- if so, the patch makes
the conjecture VACUOUS (untestable, hence useless as a proof step) rather than a genuine fix, and
this is a one-line arithmetic check, not a new computation (round 10, imo-2026-03: cost=b=p-1
forces |M|<=1 via the identity, so "full-budget-only" trivializes the Fixed-Support Uncrossing
Conjecture instead of rescuing it -- the real content unavoidably lives in the slack (cost<b)
regime, exactly where the counterexamples are).

ALWAYS: when an outline reconciles two conflicting explorer claims by observing "condition X (h=1)
is EXACTLY the event Y (w1 lies weakly between two other values)", check whether the outline's own
follow-up "Conjectured Lemma" designed to rule out Y actually restates it with the SAME
quantifier strength (weak/closed-interval vs. strict/open-interval) -- a lemma stated as "strictly
between" can silently fail to rule out the boundary/tie case that a "weakly between" original
diagnosis required, leaving a real (if likely-fixable) logical gap between what's proved and what's
needed; hunt for the tie case explicitly with a targeted hill-climb minimizing the gap toward 0
before accepting the reconciliation as airtight (round 13, imo-2026-03: the No-Gap Lemma's literal
"strictly between" wording doesn't formally exclude w1 exactly equal to an endpoint, which would
still produce h=1; my own adversarial search found a best gap of 1, never 0, corroborating but not
proving the needed stronger statement -- flagged as a precision fix for Gap 1a, not fatal).

ALWAYS: when an outline proposes a "piecewise-linear in one frozen coordinate, minimum at a
breakpoint" mechanism (the technique that already closed the all-cycles gap via the Vertex Lemma) for
a NEW target whose two sides are themselves defined by the SAME recursion one level down (e.g.
`OPT_{+1}(C,rest)`/`OPT_{-1}(C,rest)` inside a Sum Bound), check whether the outline's "enumerate the
finitely many breakpoint types" step is a flat, one-level case check or is explicitly framed as a
strong induction on the recursion depth/list size -- a flat enumeration of top-level tie types is
almost always incomplete, since breakpoints can also arise from ties buried inside the inner
recursion itself; this is a cheap logical-structure check (re-read the proposed step, ask "does this
list cover ties at every depth or only the outermost one?"), not a new computation, and is exactly
the same shape of gap that the Vertex Lemma/Shared-Value Cycle-Breaking Lemma's own induction (not a
flat check) was needed to close previously in this same problem (round 14, imo-2026-03: Sum Bound's
3-breakpoint-type list needed exactly this fix -- added an in-place note that a builder must run it
as an induction on `|rest|`, with the 3 types as only the base-case classification, not the whole
proof).

ALWAYS: when an outline reports an exact numeric family/witness (asymptotic or finite) as evidence a
new conjecture's tightness or breakpoint-type diagnosis is correct, independently re-derive the SAME
family with fresh code and check it reproduces the outline's own reported numbers to several decimal
places / exact fractions, THEN separately re-derive the structural claim about the witness (e.g. "this
witness is a KEEP=DEL tie" or "this family is an A_1-branch tie") -- a bit-for-bit numeric match alone
is necessary but not sufficient corroboration of the diagnosis (round 14, imo-2026-03: reproduced the
Sum Bound's asymptotic family gap/ratio values to 4 decimals AND independently confirmed the claimed
mechanism -- that A_1's own two branches tie exactly at the family's boundary, both equal to b_0 --
giving real corroboration beyond a numeric match alone).

ALWAYS: when an outline claims a "sharp truth-boundary" for a recursive/positional lemma (e.g. "holds
at scope X, ~N% failure the instant a specific sub-condition of X is dropped"), rebuild the EXACT
same test from scratch with your own harness, testing exhaustively over ALL alternatives to the
dropped sub-condition (not a single arbitrary substitute) before trusting the reported failure rate --
a single differently-scoped or wrong-root test can produce a spurious "sharp boundary" story that
doesn't survive a careful redo, and getting this wrong sends the builder toward an unnecessarily
restrictive (or simply incorrect) hypothesis (round 15, imo-2026-03: §23.1 claimed dropping the
"true global argmin" restriction one level deeper in the half-step lemma reproduces round 14's ~15%
failure rate; my fresh exhaustive-over-all-partners test, using a genuinely triggered top-level base
generator, found 0 violations for EVERY partner at that level, not just the argmin one -- the ~15%
figure did not reproduce, most likely contaminated by the same wrong-root bug the explorer's own
report admits catching earlier in the identical investigation).

ALWAYS: when an outline says "case q=k closes mechanically/directly by extending the already-proved
q=k-1 technique," check separately whether EACH branch of that case's own trichotomy (not just the
one branch a fresh finding happened to trivialize) actually has the needed bounds available at that
size -- a combinatorial fact that trivializes one branch (e.g. MATCH becomes a plain evaluation with
empty residual) does not by itself establish the OTHER branches (DELETE/KEEP) still close with only
the smaller case's exact bounds; the larger case's search space is bigger and may need bounds the
outline has explicitly deferred to a "later, harder" case (round 15, imo-2026-03: q=4's MATCH
sub-case is correctly shown trivial via a counting argument, but the outline's "q=4 closes directly,
likely mechanical" framing was not separately checked for the DELETE/KEEP branches, which may need
the very "generalized A_1-bound family" the build order explicitly defers to q>=5 only).

ALWAYS: when independently re-verifying a "compare a computed optimal witness against a derived
value" construction (e.g. "let c := argmin over the optimal witness ξ*'s elements..."), first check
whether the optimal witness is UNIQUE at your test instances before trusting your own harness's
result — a brute-force optimizer that explores "delete" branches before "keep/match" branches (or
any other exploration order) will silently and systematically pick the emptiest/first-found tied
witness, which can make an argmin-over-witness-elements construction spuriously undefined or
vacuous across nearly 100% of trials even though the underlying mathematical claim may be fine; this
is a tie-breaking artifact of the harness, not evidence against the claim, and should be reported as
a genuine SPECIFICATION gap (does the claim mean "for every optimal witness" or "for some canonical
one," and what happens at the degenerate/empty-witness boundary) rather than either a silent pass or
a false failure (round 16, imo-2026-03: attempting to re-verify Gap 1c's Step-3 nearest-neighbor
construction found ξ* was empty in ~100% of naive brute-force trials, purely because "delete" was
explored first in the recursion — this sharpened, but did not refute, the outline's own honest
"not yet independently re-verified" flag on that construction).

ALWAYS: when an outline's proof cites a fact as "the certified exact dichotomy" or similar, grep the
actual named lemma file's own text for whether that specific sub-claim was really promoted to
certified status or only mentioned/confirmed in passing (e.g. inside a "Verification" section as
corroboration for a DIFFERENT certified lemma, then explicitly "declined for certification" as too
narrow) — citing an uncertified-but-true fact as if it were a pre-existing certified lemma is a
minor wording overclaim worth flagging (fix the citation, not the math) even when, as here, the
underlying fact independently re-verifies cleanly and the surrounding proof is otherwise airtight
(round 16, imo-2026-03: Gap 1b's base-case proof cited "the certified exact q=3 dichotomy
(lemmas/three-bound-domination-and-keep-top-bound.md)" but that file's own text explicitly declined
to certify the dichotomy identity itself, certifying only Three-Bound Domination and Keep-Top Bound
separately — the combination is still true and cheap to re-derive, but the citation should say so).

ALWAYS: when an outline claims "proving lemma X at general parameter q hands you sibling lemma Y's
inductive step for free" via a shared closed-form substitution, separately check (a) whether the
one-step algebraic substitution is a pure tautology (cheap, verify directly) and (b) whether the
"for free at every recursion depth" part actually needs X's hypothesis (e.g. a trigger/global-argmin
condition tied to one specific top-level instance) to hold at EVERY sub-node the induction visits, or
only along a single fixed descent chain from one instance — these are different-strength claims and
the file's own prose can conflate them even when the underlying math, read carefully, only needs the
weaker one; trace it by hand as a strong induction on the shared recursion and confirm which quantifier
is actually load-bearing before approving (round 17, imo-2026-03: Gap 1b's Sum Bound target was shown
to be algebraically identical, via the certified KEEP-branch closed form at h=0, to half of Gap 1a's
Deletion-Suffices-for-k* at the matching depth -- correct as a tautology, and correct as a shared
induction target PROVIDED the same external top-level A1 is threaded through every depth, which the
file itself flags via a negative control, not something I had to discover from scratch, but worth
re-deriving to confirm the flagged caveat is the only one).

ALWAYS: when a file's own construction reuses a symbol (e.g. `xi*`, "the optimal witness") across
multiple sections written in different rounds, check whether every section's usage refers to the SAME
side of the target inequality (LHS-optimal witness vs. RHS-optimal witness are NOT interchangeable) --
a silent drift is easy to miss because the surrounding algebra can still be internally consistent within
each section even when the label conflicts across sections, and it will actively mislead a builder who
trusts the label over re-deriving from context (round 17, imo-2026-03: `xi*` was introduced as "the
LHS-optimal witness" in one section but used as "the RHS-optimal witness" in later sections building the
xi*=empty and duplicate-pair-collapse cases -- the math in each section was correct once resolved by
cross-reading, but the label itself needs fixing before the confusion compounds).
ALWAYS: when a file claims a positional/insertion sub-fact "appears independent of X" (e.g. a
tie-break choice) and calls it "unconditional" or "a fact about M and d alone," test it BOTH within
genuine scope-family provenance AND with the same construction shape but arbitrary/non-provenance
inputs before trusting the "alone" framing — independence-from-one-parameter (the tested thing) is
not the same as independence-from-provenance (an untested, easily-conflated claim); build your own
from-scratch scope-family generator (trigger + global-argmin descent) rather than reusing an
explorer's, since this is exactly the kind of easy-to-miss overreach that has recurred repeatedly on
this problem (No-Gap Lemma, half-step lemma, Deletion-Suffices, Sum Bound) (round 18, imo-2026-03:
§29.3's delta_d>=0 held 0/155 within genuine F-provenance but failed 178/1050 (~17%) once provenance
was dropped even with the identical construction shape — a real, previously-unflagged clarification,
not a refutation of the sub-target itself).

ALWAYS: when a round's new lemma (A) reduces one open item to an already-standing gap (B) at the
SAME induction index/size, separately check whether B's own already-suggested (even if optional)
proof route leans on A itself at a size ONE LEVEL SMALLER — if so, this is a legitimate joint
induction only when explicitly built level-by-level (smaller instance of A feeds size-n instance of
B feeds size-n instance of A), and is silently circular if either lemma is later proved as a flat
"for all sizes" statement; this check is cheap (re-read both lemmas' own index/size dependencies)
and should be flagged as a "Watch out for" addition even when the round's actual new proof is 100%
correct as written, since the risk is in a NOT-YET-WRITTEN future proof, not the current one (round
18, imo-2026-03: Two-Touch's MATCH branch reduces to Per-Partner Domination at the SAME size n
(§29.1), while Per-Partner Domination's own suggested general-q route (§25.2) may use Two-Touch's
closed form at size n-1 — a well-founded joint induction only if built in that exact order, not
flagged anywhere in the file despite the analogous Two-Touch/Three-Touch mutual induction having
been explicitly checked for well-foundedness in round 17).
