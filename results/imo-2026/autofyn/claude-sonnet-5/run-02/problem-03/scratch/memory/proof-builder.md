ALWAYS: when an outline claims "N shapes" via a stated combinatorial
formula, evaluate that formula yourself before building — if it disagrees
with the stated N (e.g. a "sum_{b=0}^{k} C(b+m-1,m-1)" formula for "at
most k cuts over m pieces" actually gives a LARGER count than the smaller
"exactly k cuts" count C(k+m-1,m-1) the outline meant), don't just adopt
the smaller number silently: explicitly derive and state the closure
argument (cite the vertex-minimum-theorem's "family (I): fragment=0
belongs to the closure of a lower composition" clause) for why enumerating
only the smaller "exactly-k" set, ON ITS CLOSED DOMAIN, still covers the
larger "at-most-k" legal space — and separately, before trusting an
outline's claimed short list of "the only tight/dangerous cases," verify
by independent exact (rational, not float) vertex enumeration; a smaller
random-search sample can systematically undercount tied cases (measure-
zero exact ties are unlikely to be hit by random sampling), and an outline
built on that undercount will mis-scope the remaining hard work (round 28,
imo-2026-03, rank-pigeonhole-budget: outline claimed 20 shapes via a
formula that actually gives 35, and claimed only 2 "tight" shapes when
exact enumeration found 7 — the true gap was 3x larger than scoped).

ALWAYS: when a coverage measurement (bisect-subset-lemma / n=3 chamber
style) leaves a real gap (e.g. 93% covered), hunt the new chamber shape by
running the exhaustive small-shape search (here: "bisect 2 pieces + pin 1
of the remaining to another, leave the last untouched") ONLY against the
specific uncovered points, then reverse-engineer + prove the closed form
via the already-certified iterated pair-insensitivity-corollary (3
applications collapse a 5+ element fragment multiset to a 2-element
alternating sum |a-b| instantly) — this is much faster than guessing
shapes blind and produces a fully proved (not numeric) new chamber family
in one pass; always re-verify with EXACT Fraction arithmetic at the final
combined-coverage stage, since a first float-based coverage check
produced 2 spurious "near-miss" uncovered points that vanished exactly
under Fraction re-computation (round 29, imo-2026-03, lp-duality-
certificate, Double-Bisect-Pin Theorem, n=4).

ALWAYS: when asked to test a "new induction variable" (e.g. |S'| instead of
raw N) to escape a diagnosed parity trap, first check for an elementary
identity forcing the new variable's parity to equal the old one's (e.g.
sum-of-multiplicities-mod-2 = count-of-odd-multiplicities-mod-2, a 3-line
proof) before attempting the actual induction step — if such an identity
holds, the "decoupling" hope is provably dead and you can deliver a clean,
general, non-numeric negative result instantly instead of grinding through
casework that was doomed from the start. (round 8, imo-2026-03,
rank-tie-vertex-reduction: proved ℓ(S)≡|S| (mod 2) always, which alone
rules out peel-induction-on-ℓ as an escape from the shared parity wall.)

ALWAYS: when redirected from a dead-end lower-bound certificate to a
"generalize the n=2 template mechanism" upper-bound task, don't just
generalize the SAME templates (already shown to fail at n=3 by a prior
round) — instead look for exact, unconditional pair-cancellation-style
identities (via the certified pair-cancellation-identity/leftover-formula)
that hold for EVERY n with no case restriction, then combine several of
them greedily (take the true min) and stress-test with BOTH random
Fraction sampling AND adversarial scipy differential_evolution search
before writing up a domain-closure claim — a 3-strategy family can look
almost-complete (zero violations in casual random testing) yet have a
genuine, small-denominator exact counterexample findable by brute grid
search; adding one more general identity (e.g. "bisect both the largest
and smallest piece simultaneously") found by inspecting what the
adversarial search's actual argmin strategy was closed every witness this
round found. Still report as a conjecture (Status partial), not solved —
zero violations in search is evidence, not proof. (round 8, imo-2026-03,
lp-duality-certificate: Theorems A-D, general-n exact identities for the
upper bound c(n)<=a_n.)

ALWAYS: when an outline hands you a case split with a cut/point budget
restriction baked into the case (e.g. "G' uses <= n-2 cuts"), make sure any
numeric verification script actually enforces that budget cap, not just the
algebraic case condition (e.g. "v >= s") — an uncapped script found spurious
violations of a conditional-on-induction-hypothesis bound (Proposition 24,
imo-2026-03, round 10) purely because the test allowed more cuts than the
lemma's hypothesis permits, which looked like a proof bug but was actually a
test bug; re-deriving the algebra by hand first (it matched) and then fixing
the budget cap in the script resolved it in minutes instead of wasting time
distrusting a correct proof.

ALWAYS: when closing one branch of a multi-branch open case (e.g. "v>=p2 and
G' cuts p2, with the induced split having l=1 and residual >= tail's own
second piece"), try re-applying the SAME already-certified exact-truncation
mechanism (safe-window + single-residual-indicator + cross-term-identity)
one level down on the rescaled sub-ladder before reaching for a fresh
technique — this can close a branch completely UNCONDITIONALLY (no
induction hypothesis needed at all) purely from the trivial A<=Total bound
plus the ladder's doubling identity p_i=2p_{i+1}, which is a stronger result
than the conditional-on-(star_{n-2}) closures nearby (imo-2026-03, round 10,
Proposition 25) — always check whether the "obvious" weaker trivial bound
already suffices before assuming a case needs the full recursive machinery.

ALWAYS: when an outline suggests a "reformulation is equivalent to X" claim
without proof, check it against the odd-run-reduction/general-multiset facts
already certified before writing it up as an equivalence -- often it is only
a *sufficient* strategy family (one special shape among many that could
achieve the target), not a logical equivalence; state the corrected,
weaker-but-true version instead of repeating the outline's overclaim
verbatim. Also, when asked to "attempt a construction from scratch," a
concrete explicit greedy algorithm (e.g. repeatedly cut-and-match the two
largest current fragments) can often be proven, in full, to be a genuine
general *identity* (always legal, exact closed form via repeated
pair-cancellation) even when the specific selection rule inside it
provably fails to hit the target on some input -- report the identity as a
certified reusable lemma and the rule's failure as a separate, honest
dead-end record, rather than discarding the whole construction. (round 10,
imo-2026-03, lp-duality-certificate: Iterated Greedy-Peel Construction
matched both known hard witnesses exactly but failed ~48% of random
markings and the n=4 equal-pieces marking outright.)

ALWAYS: when consolidating several separately-proved conditional sub-lemmas
(each conditional on "the theorem holds one/two levels down") into one
unified induction, explicitly trace which sub-lemma needs which recursion
depth (n-1 vs n-2) before claiming a combined base case — a claim like "base
case n<=4 already unconditionally closed" may only be true for the SHALLOWER
dependency's branches; branches needing the DEEPER dependency (n-1, not n-2)
only bottom out one n earlier (n<=3, not n<=4). Get this bookkeeping exactly
right rather than inheriting an outline-reviewer's summary verbatim
(imo-2026-03, round 11).

NEVER: assume a cut-budget-capped bound (e.g. "max A(G') over <=n-2 cuts")
transfers to a larger budget (n-1) just because "more cuts only helps the
adversary" sounds monotone in the wrong direction for what you need — larger
budget makes the quantity you're trying to UPPER-bound only get WORSE
(easier for the adversary to push up), so a bound proved at a smaller budget
does not cover the larger-budget case; check literally which cut-count fact
(e.g. "ell(F)=1 implies c>=2") produced the budget cap before reusing it for
a different ell(F) value with a different minimal cut count (imo-2026-03,
round 11, ℓ(F)=2's mixed-regime sub-case needs budget n-1, one more than
Proposition 21's (†) supplies).

ALWAYS: when a prior round's outline/approach claims "both known hard
witnesses require X" as justification for abandoning a restricted strategy
family, re-verify that claim by exhaustively enumerating the family's own
already-certified finite vertex characterization (a genuine proof, not
numerics) before repeating it — one of two "hard witnesses" on file for
imo-2026-03's upper bound turned out to actually be solved by the
restricted family itself (a p=0,k=3 equal-trisection vertex, exactly
matching an earlier round's ad hoc discovery), so the abandonment
justification was only half-true; only the OTHER witness was a genuine
counterexample. A cheap Python brute-force over the finite characterized
family (not a random/adversarial search) settles this exactly and can
overturn an inherited false premise before building further on it (round
11, imo-2026-03, lp-duality-certificate).

ALWAYS: when dispatched to build only the "cheap, already-approved" steps
of a multi-step outline after the outline-reviewer rejected the harder
steps by exhaustive brute-force, still spend remaining budget on the
reviewer's named redirect target rather than stopping after the cheap
lemmas — even an honest, non-closing attempt (quantify how generic the
still-open residual actually is; test one more natural greedy candidate
and refute it with an exact witness) is valuable, reusable diagnostic
content for the next round, and is exactly what "an honest partial is
worth more than fake solved" means in practice (round 12, imo-2026-03,
lp-duality-certificate: certified Equal-Pieces Closure + Spare-Cut
Bisection Corollary, then found via a fresh 4000-trial exact-Fraction
check that the "residual" the outline treated as ~66%-of-cases is
actually ~100% of generic (no built-in symmetry) markings — a materially
different, more honest calibration of how much the cheap lemmas actually
cover).

ALWAYS: when a certified lemma's PROOF already uses a wider/corrected
object (e.g. a reference set that includes 0) than its own boxed STATEMENT
claims, the fix is often just to restate the statement to match the proof
— re-derive nothing, but do add an independent cross-check (here, a small
new "harmlessness" lemma showing the added case introduces no new values,
only new descriptions of already-covered ones) so the fix is doubly
verified, not just a wording patch trusted on faith (round 11,
imo-2026-03, lp-duality-certificate: Zero-Pin Harmlessness Lemma).

ALWAYS: when asked to bound how A(S) changes as ONE coordinate of a fixed
background multiset varies continuously (not "split one element into
two," which is Lemma-14-style), derive the formula fresh from the general
cross-term identity (A(F∪G)=A(F)+A(G)-2∫u_Fv_G) by treating the moving
coordinate as its own singleton multiset {t}: this gives an explicit,
piecewise-linear-in-t closed form whose derivative is 1-2·(background's
own odd-parity indicator at t) — cheap to derive, and lets you prove a
whole continuum of cases at once via a monotonicity/boundary argument
(reduce "holds for every t in an interval" to "holds at one endpoint")
instead of casework on t (round 12, imo-2026-03, Proposition 26).

NEVER: assume a nested case (e.g. "P nonempty" inside an ℓ(F)=2 split)
"safely inherits" an existing bound just because the object it produces
has the same algebraic shape as something already proved — check whether
the existing proved fact is a lower bound or an upper bound on that exact
quantity; needing the OTHER direction is a genuinely new, not-yet-easier
requirement even though it "looks like the same case" (round 12,
imo-2026-03: the P≠∅ residual of sub-case (c) needed an UPPER bound on
A(F2∪G'), but Propositions 20-24 only ever prove LOWER bounds on that
identical quantity — not automatically inherited despite same shape).

ALWAYS: when asked to test/prove a "peel target existence" or similar
dichotomy lemma for this problem's general upper bound, check FIRST
whether a completely induction-free bound exists using the elementary
fact A(S)<=max(S) for any sorted multiset (a 4-line regrouping proof,
telescoping alternating sums into max minus a sum of nonneg gaps) applied
to the UNTOUCHED tail after a single bisection of p1 (Theorem C) — this
gives a genuinely new, zero-induction-hypothesis sufficient condition
(p2<=T/D_n) that is disjoint from every other sufficient region on file,
cheap to derive, and immediately narrows a vague open dichotomy to a
precisely bounded residual band. (round 13, imo-2026-03,
lp-duality-certificate: Max Domination Lemma + p2-threshold corollary.)

NEVER: assume a "peel-then-bisect" or "peel-then-dominate" 2-cut hybrid
construction (peel p1 against p2 via one-step-peel-identity, then bisect
the residual's own max) universally closes the general upper bound just
because it's a natural composition of two already-certified identities —
refuted by exact witness (round 13, imo-2026-03: ~10% failure rate over
3000 Fraction trials, some overshoots by orders of magnitude at n=6). Each
new "natural greedy hybrid" needs its own stress test before being trusted
as a closer, even when built entirely from certified building blocks.

ALWAYS: when hunting for a missing chamber/strategy at a specific flagged
counterexample point, run a real numeric optimizer (scipy Nelder-Mead,
softmax-parametrized fragment splits, multi-restart) over ALL legal cut
compositions up to the budget, not just the composition types a prior
round already tried — then REVERSE-ENGINEER the closed form from the
optimizer's fragment values by pattern-matching them against the OTHER
pieces (e.g. "one p2-fragment ≈ 0.1667 = p3 exactly" means "pin p2's cut
to match p3"). This routinely finds a clean, provable closed-form chamber
in minutes that no amount of guessing-from-composition-shape would find.
Once found, isolate the general mechanism as its own tiny reusable
corollary (e.g. "bisecting/pinning any two matched values erases them
from the alternating sum A, regardless of coincidental ties elsewhere —
a 3-line consequence of odd-run-reduction-lemma via parity alone") rather
than re-deriving casework per chamber — this made 4 new chamber formulas
provable with a single shared lemma instead of 4 separate derivations,
and let a Farkas-certificate covering proof (nonneg combination of the
"all chambers fail" hypotheses collapsing to a manifestly false constant,
solved by matching coefficients so variable terms cancel) close a gap
that had stumped 3 prior rounds (round 27, imo-2026-03,
lp-duality-certificate: Pair-Insensitivity Corollary + Gap-Filler
4-chamber family, closing p1>=T/2 & T/15<p2<4T/15, completing c(3)<=8/15).
Also: when sanity-checking a NEW result against the FULL claim (all
regimes combined), keep any crude/simplified stand-in for an already-
separately-certified OTHER regime's bound clearly separate — a quick
approximation of a different regime's optimal strategy can produce false
"violations" that are artifacts of the approximation, not the new result;
filter the sanity check to exactly the new result's own claimed region
before treating any violation as real.

ALWAYS: when proving a chained/inductive identity (e.g. "bisecting k top
pieces cancels k pairs"), work out the cleanest single-shot argument
FIRST on scratch paper/mentally before writing prose — a first attempt at
an incremental (element-by-element) induction step can wrongly require an
unstated domination hypothesis (e.g. "the newly-bisected element dominates
the rest of the reference multiset") that doesn't actually hold in
general; the already-certified pair-cancellation-identity needs NO
domination/ordering hypothesis at all, so the correct proof is a direct
k-step chain of that identity applied to arbitrary reference multisets,
not an incremental single-element removal-and-reinsert argument. Caught
and fully replaced a multi-paragraph false-start (three superseded "let me
try again" sub-arguments) with the clean 6-line chain before finalizing —
per the standing rule to never leave abandoned attempts in the written
proof, always do a final pass specifically re-reading any freshly-written
induction proof for leftover "correct/final version below" markers before
submitting (round 14, imo-2026-03, lp-duality-certificate, Bisect-Top-k
Lemma).

NEVER: assume a "weighted/convex combination of several already-exhibited
explicit strategy values" can certify an upper bound on a MIN beyond what
the plain pointwise minimum of those same strategies already certifies —
this is not a heuristic risk but a provable impossibility: since
Phi_min(p) is itself a minimum, and min(A,B)<=any convex combination of
A,B, any weighted combination lambda*A+(1-lambda)*B exceeds the target
whenever BOTH A and B do (elementary convexity), for ANY lambda, fixed or
adaptive. Proved this in general (Convex-Combination Futility Theorem,
round 17, imo-2026-03, lp-duality-certificate) after a reviewer flagged a
literal "solve lambda by equating to target" mechanism as circular — the
deeper fact is that NO lambda-selection rule of any kind escapes this,
not just the equate-to-target one. When a round's outline proposes
combining several exhibited upper-bound witnesses via weights to extend
coverage, check this impossibility FIRST (a 5-line proof) before
attempting any specific lambda derivation — it settles the whole
mechanism family in one shot, honestly reported as a negative result
rather than spending the round on doomed lambda searches. LP-duality-style
weighting IS the correct tool for LOWER bounds (bounding a min from below
via a dual-feasible weighting over the adversary's move space) — not for
upper bounds on a min, which must be witnessed by one explicit strategy.

ALWAYS: when a two-threshold combined identity (A(F1∪G')-A(F2∪G')-style,
via an exact identity like Lemma 25) needs a "two-threshold floor" lemma,
decompose the reference multiset's odd-parity integral into exactly THREE
pieces at the two thresholds (I0=[0,v2), I1=[v2,v1), I2=[v1,T)) and bound
each with its OWN easy same-direction bound (I0<=v2, I1>=0, I2<=T-v1) rather
than trying to combine two single-threshold floor-lemma outputs (which only
ever gives lower bounds at each threshold separately, the wrong direction
for a subtracted term) — this composes cleanly IF AND ONLY IF the interval
[v1,T) is a genuine nonnegative-length interval (v1<=T); dropping that
hypothesis breaks the I2<=T-v1 bound outright (T-v1 goes negative while
I2>=0 stays valid), so state and use the v1<=T hypothesis explicitly rather
than assuming the "obvious" generalization extends past it — verified via
an exact counterexample when the hypothesis was dropped without also
re-imposing the game's own mass-conservation constraint (round 17,
imo-2026-03, greedy-halving-adversary, Two-Threshold Truncated Alternating
Sum Floor / Theorem 32). This closed a genuinely large (v1<=s) sub-range of
ell(F)=2 sub-case (b) unconditionally, in one round, exactly matching what
the outline-reviewer predicted ("not a routine 2-line lemma, but tractable
with the right decomposition") rather than either blindly trusting the
outline's guessed constant or giving up and reporting zero progress.

ALWAYS: when converting a floating-point/sampling LP "covering family"
result into a rigorous exact proof, write a small exact Fourier-Motzkin
elimination in Python (Fraction arithmetic, eliminate variables one at a
time, track which original constraints combine into each derived row) over
each case-split branch — this both (a) proves infeasibility outright
(reaching a manifestly false "0 < const<=0" row) and (b) with a tracked
certificate dict, extracts a SHORT (3-5 term) explicit nonnegative Farkas
combination per branch that can be verified by hand term-by-term, which is
exactly what "the written proof must stand on its own" requires — don't
just report "LP says infeasible," derive and print the actual combination
and re-verify it by hand in the proof text. Also: an apparent "boundary
counterexample" found only via a floating-point epsilon-margin LP is often
NOT a real gap — re-evaluate it in EXACT arithmetic first; it may be a
degenerate multi-way tie where one of the covering family's OTHER
chambers already succeeds with g=0 exactly, meaning it was never inside
any "all chambers fail" branch to begin with (round 25, imo-2026-03,
lp-duality-certificate: closed case (b2) at n=3 fully this way, and the
explorer's flagged boundary vertex turned out to be a genuine triple-tie
success point, not a gap, once evaluated exactly).

ALWAYS: when a proposed "Liu Bang's own marking freedom" reduction fixes
several leading pieces (e.g. p1,p2) and only lets a suffix vary, remember
the feasible region for the varying suffix is itself constrained by the
SORTED-ORDER hypothesis of the fixed prefix (e.g. p3<=p2 forces an upper
bound, p3>=p4=s-p3 forces a lower bound p3>=s/2) — a naive test witness
chosen without checking p2>=s/2 can produce an EMPTY feasible interval
(caught this immediately via a sanity numeric script before wasting
effort; fixed by picking p1,p2 satisfying 3p2+p1>=T). Always derive and
print the actual feasible interval bounds before sweeping (round 18,
imo-2026-03, lp-duality-certificate).

ALWAYS: when asked to reuse an already-certified "vertex-maximization/
exchange-smoothing" machinery as an independent cross-check on a SIBLING
approach's open target, first check whether the target's polytope is
structurally the same shape as the one the machinery was built for (e.g.
"fragments of ONE stick summing to a fixed total" vs. "independent
refinements of SEVERAL distinct fixed pieces sharing one total cut
budget") — the per-piece mass-conservation case genuinely changes the
argument (perturbations can only trade mass within one piece, not across
pieces, so a rigorous adaptation needs a "freeze all other pieces, the
restriction of any joint maximizer must itself be a one-piece maximizer"
argument, which is valid but can re-introduce cross-piece tie-vertices —
report this honestly as a re-encountered obstruction rather than silently
assuming the single-stick lemma transplants verbatim). Also: before
building any vertex/enumeration argument, test the elementary "drop all
structure" bound first (e.g. A(S)-2A(S_{>v})<=v with NO ladder/mass
constraints) via a quick 300k-trial random Fraction search — if it's true
in full generality it is worth stating as its own reusable lemma (dual to
an already-certified "floor" lemma proved the same way), even if it turns
out too weak alone to close the real target; this is cheap and gives a
genuine reusable artifact even when the harder budget-specific closure
isn't reached this round (round 19, imo-2026-03, rank-pigeonhole-budget).
ALWAYS: when fixing a case-boundary bug, restate the strict-vs-non-strict inequality convention explicitly at the top of the case split (e.g. "tau_{>v2} uses strict >") before listing cases — this makes exhaustiveness/disjointness at each boundary point independently checkable by the reviewer without re-deriving it (round 20, imo-2026-03 rank-pigeonhole-budget).
ALWAYS: when a budget-capped sub-object (T' in a "reframe the residual as a legal (n-2)-ladder response" plan) has budget 0 or 1 at the specific n values being asked for, check FIRST whether that pins the sub-object completely (0 free cuts = untouched, forced exact value) before invoking any induction/rescaling machinery — often the "small n" case collapses to a single-free-parameter finite computation that is strictly easier and fully unconditional, bypassing the induction hypothesis the outline planned to need (round 20, imo-2026-03, greedy-halving-adversary: n=4's Case (b) had budget exactly 1, forcing T' untouched, so direct finite algebra closed it with no IH at all).

ALWAYS: when a prior round's diagnosis says "this needs a genuine upper bound on A(whole-block-X), the central obstruction" because a naive route bounded A(X∪{new}) via triangle-inequality + trivial-bound-on-X-as-one-lump, try instead computing the target EXACTLY via insert-element-identity after first SPLITTING X at the new element's own rank into (elements above, elements below) — apply the trivial per-piece bound to each half SEPARATELY rather than to X as a whole. This recovers strictly more slack (the two routes coincide only when one half is empty) and can fully close a gap that looked like it needed the project's central obstruction, when actually it only needed a finer decomposition of the same trivial bound (round 27, imo-2026-03, greedy-halving-adversary: closed the even-multiplicity-tie residual this way — Theorem 41 — after round 26's whole-lump approach failed by exactly one factor of t*).
ALWAYS: when a sibling file names a "TRUE" target (e.g. an ε-corrected inequality like (♯')) as distinct from a weaker target already closed, explicitly re-derive/import the exact algebraic reduction chain (don't just re-run the old proof) — the extra correction term often needs a strictly tighter case-hypothesis bound (e.g. v2<p3 instead of v2>0) that was available all along but unused (round 21, imo-2026-03 rank-pigeonhole-budget).
NEVER: silently assume a weaker inequality's case split "just extends" to a strictly stronger target without checking where the two targets actually differ (locate exactly via a parity/band fact) — always verify which sub-cases are literally unaffected before reusing their old proofs verbatim (round 21, imo-2026-03).


ALWAYS: when a Key Lemma is described as a "direct consequence" of an already-certified per-piece/per-object vertex theorem but actually needs a JOINT system across multiple objects simultaneously (e.g. each piece is individually a vertex relative to the others, but the whole vector's dependence on an outer parameter needs solving the coupled linear system across all pieces at once), write out the joint system explicitly: identify which rows are mass-conservation (outer-parameter-linear RHS) vs. tie/pin rows (parameter-independent coefficients), then PROVE (don't assert) that the coefficient matrix's invertibility is what "chamber" well-posedness actually requires, and separately show non-invertibility forces the region to have empty interior (a wall, not a chamber) except for a precisely-isolated residual algebraic-coincidence case, which should be flagged open rather than swept in (round 21, imo-2026-03, lp-duality-certificate, Within-Chamber Affinity Theorem).ALWAYS: when asked to close a "residual object one level down" (e.g. {c}∪S recursed from an already-closed vertex like Theorem 37's), first check whether the SMALLEST scale instance (here m=1, forced by a zero/near-zero cut budget) makes the general vertex family collapse to exactly the two "boundary" vertex types (c=0, c=top-with-top-untouched) that the analogous higher-level theorem already proved a recipe for — this can close a genuinely new smallest case (n=5 here) fully and unconditionally in one round even though the general-m case stays open; also ALWAYS stress-test any "top-tie always dominates deeper ties" shortcut before relying on it — a direct exact-Fraction test (both on arbitrary multisets and on genuine legal ladder-refinement S) showed deeper (3rd/5th-rank) ties DO beat the top-tie/box-endpoint "base trio" in a real fraction of legal cases, refuting the shortcut and correctly narrowing the round's claim to only the two rigorously-closed vertex types (round 24, imo-2026-03, greedy-halving-adversary, Theorem 38/h(m)).
ALWAYS: when an outline asks you to "cheaply test" whether an object like
{c}∪S (c a free real number bounded only by an interval, S a legal
refinement of a fixed-total-mass ladder) is literally a legal response to
some smaller ladder instance (so a standing induction bound could apply by
direct substitution), check mass conservation FIRST as a one-line
decisive test: Total({c}∪S)=c+Total(S) is strictly increasing/injective
in c, while any single fixed ladder instance has a FIXED total mass, so
the identification can hold for at most one isolated value of c, never
for a whole interval — this converts a vague "probably doesn't transfer"
into an actual proved impossibility (worth stating as its own reusable
lemma) in under 10 minutes, and pins down exactly which single vertex (the
one point where mass happens to match, usually where c ties an existing
element enabling odd-run cancellation first) is the ONLY place a
substitution-style shortcut can ever work (round 25, imo-2026-03,
greedy-halving-adversary, Proposition 39 / Mass-Conservation Obstruction).

ALWAYS: when odd-run-reduction cancels a value with multiplicity 3 spanning
3 different pieces (e.g. an untouched piece plus a tie from each of two
OTHER pieces' fragments, all equal), do not assume "which piece owns the
1 survivor" needs resolving — A(M) only depends on M''s sorted VALUES, not
piece attribution, so this ambiguity is harmless whenever you only need
A(M)/Phi (not each individual q_i); only individual q_i's require resolving
it. Also ALWAYS distinguish "sufficient" from "necessary" when using
max(x,y)>=(x+y)/2 to combine two chambers' g-values into one region-covering
bound: a negative sum does NOT imply both chambers fail (checked and found
a concrete counterexample where sum<0 but one term was still >=0), so a
sum<0 finding only means "this cheap bound doesn't apply here," not "no
chamber in the pair works here" (round 24, imo-2026-03, lp-duality-certificate).

ALWAYS: when an outline proposes "prove a Restriction Lemma that the
extremal configuration concentrates on a single element, then dualize a
1-D vertex lemma," first execute the reduction by hand on the actual
target inequality (peel the dominant/untouched top element via
sharp-dominant-removal-identity, reduce via mass-conservation identities
like R(sigma)+sigma_last=2*sigma_1) before trying to prove the
Restriction Lemma itself — this often reveals that "concentrate on one
element" is not literally the missing step; instead the target splits
cleanly into a "top element untouched" branch (closable in ONE line by
the fully general, unconditional A<=Total fact once you get the
direction right) and a "top element itself gets cut" branch (the
genuinely open one), which is a strictly narrower and more precisely
located gap than the outline's original framing. When doing this, always
sanity-check EVERY peel step's direction twice (does the reduced target
need an upper or lower bound on the residual?) — a first-pass attempt
here wrongly concluded Fact 2 (A<=Total) closed a branch that actually
needed the opposite direction (a genuine lower-bound theorem,
MinFloor(ell-1)); catching this before writing it up avoided a false
"solved" claim (round 25, imo-2026-03, rank-pigeonhole-budget, MinFloor/
MaxCeil reduction of inequality (7.9.1)).

ALWAYS: when an outline-reviewer flags "mechanism X (rank-split + peel via
sharp-dominant-removal-identity) needs an anchor that UNCONDITIONALLY
dominates the tail it's peeled from, and that domination isn't automatic
in the sub-case where the adversary can cut the anchor itself," don't try
to force the general case — first check whether the certified lemma's
proof is already anchor/tail-agnostic (i.e. stated in abstract w>max(X)
terms, not baked-in ladder constants); if so, the fix is a clean scope
restriction (prove only the "anchor untouched" sub-case) plus an abstract
restatement of the mechanism (rename p4,T'',f(n) to w,X,g) — this closes
real new territory (e.g. h(m)'s q1-untouched branch for every m at once)
without overclaiming the still-open "anchor gets cut" branch, which is a
legitimate, reviewer-anticipated partial result, not a dead end (round 28,
imo-2026-03, greedy-halving-adversary, Lemma A / Theorem 42).

ALWAYS: when an outline-reviewer flags "lemma X only proves slope +-1 for
a single free coordinate against a FIXED rest, but the outline applies it
to a mass-conserving coupled pair (e.g. f2,f3 with f2+f3=C fixed)," do not
try to patch the single-coordinate lemma — instead prove a small,
self-contained elementary sorted-rank lemma from scratch for the coupled
object directly (e.g. "insert x into {p,q,w} where p+q=C is a conserved
pair and w is a fixed reference between/above the pair": the KEY trick is
that q<=w<=p (or w>=p>=q) PINS the sorted order of {p,q,w} regardless of
the free coordinate x, so inserting x is then just an ordinary 4-way
trichotomy with an exact closed form per case) — this is far cheaper than
invoking the general vertex-minimum-theorem machinery for what is really
an elementary <=4-element computation, and produces a clean reusable
lemma with two mirrored forms (w between the pair vs. w above/below it)
that generalizes across multiple shapes with the same structure (round 29,
imo-2026-03, rank-pigeonhole-budget, Pair-Insertion Ordering Lemma).
ALWAYS: when an outline literally states a chamber/strategy formula
(e.g. "leave the rest untouched, gives Phi=(T+|residual|)/2"), plug in
the outline's own witness/example FIRST via a direct exact-Fraction
computation of the literal fragment multiset before writing up the
proof — this catches an outline authoring a formula that silently
assumed a DIFFERENT (fuller-budget) strategy than the one it described in
words ("leave untouched" vs. the correct "bisect with the spare cut"),
where the two differ by exactly the untouched piece's own alternating-
sum contribution; the general n-level-deep "pin k pieces to k targets,
handle the rest" mechanism is best proved ONCE as a fully general
"Partition Chamber Theorem" (partition all m indices into blocks, each
size>=2 block has a host cut to match the rest exactly leaving only its
own residual, singleton blocks either untouched [contribute their own
value] or bisected [contribute nothing] via pair-insensitivity-corollary)
rather than re-deriving each named instance (Bisect-Subset,
Double-Bisect-Pin, Triple-Pin, ...) from scratch — this both fixes outline
bugs for free (the corrected formula falls out of the general theorem
automatically) and gives a reusable lemma that subsumes several
previously-separate certified chamber families in one shot (round 30,
imo-2026-03, lp-duality-certificate, Partition Chamber Theorem).
NEVER trust a coverage claim measured only against the SAME chamber
family being tested, even at 100% over tens of thousands of exact trials
— a genuinely thin (e.g. 1/899-margin) exact gap in an untested-for-
completeness family can and did survive 50,000+ random exact-Fraction
trials in a prior round before being found by a targeted numeric-
optimizer search; when asked to retract such a claim, retract ONLY the
coverage claim, not the individually-proved chamber formulas within that
family (they usually remain correct) — keep the retraction narrowly
scoped to what was actually refuted (round 30, imo-2026-03,
lp-duality-certificate).

ALWAYS: when a shape has TWO independently-split "conservation groups"
(e.g. one piece split into a triple summing to a fixed total, another into
a pair summing to a different fixed total) plus finitely many fixed
constants, and a linear branch-tree case-split threatens to drop a
cross-group joint-feasibility constraint (caught in a prior round as a
spurious near-violation), don't keep patching the branch tree — instead
cite the general vertex-minimum-theorem directly and enumerate its
*complete, exhaustively-justified* finite vertex family (every triple of
the shape's legal "fragment=0"/"two values tied" hyperplanes, argued by
hand that no other such event is combinatorially possible given the
fixed-sum constraints) in exact rational arithmetic, evaluating A by
direct sorting at each vertex. The feasibility filter applied uniformly
to every candidate vertex automatically enforces the cross-group
constraint for all vertices at once, closing what looked like a deep
branch-tree gap in one clean pass (round 31, imo-2026-03,
rank-pigeonhole-budget: closed shapes (1,2,0,0) and (2,1,0,0), the last
2 of MinFloor(4)'s 6 residual shapes, via 36+27 exact vertices, zero
violations, all hand-verifiable by sorting).
ALWAYS: when asked to prove a finite-chamber-family covers a box and the
project has a history of false coverage claims (imo-2026-03, rounds
29-30), actively SEARCH for a counterexample against the assembled family
before attempting any Farkas certificate — if one is found, immediately
run an independent unrestricted numeric optimization (all legal cut-count
compositions, not just named chambers) at that exact point to distinguish
"family is incomplete" (true minimum still beats target, so no Farkas
proof over this family can exist — correctly do not attempt one) from "the
theorem itself may be false" (true minimum also fails — a serious finding
requiring escalation). This ordering — assemble, actively adversarially
search, diagnose which case, only then attempt a certificate or honestly
report incompleteness — is much cheaper than writing a doomed Farkas
argument over a family later shown incomplete (round 32, imo-2026-03,
lp-duality-certificate: found an exact counterexample near a box corner,
confirmed via scipy Nelder-Mead multi-start that a new (2,0,0,0,2)-cut
shape beats the target there, so correctly reported the family as
incomplete rather than forcing a certificate).

ALWAYS: when a "punctured tail" object (a legal refinement with one
specific element deleted) needs only a LOOSE bound (not the tight
MaxCeil/MinFloor value), check first whether the deleted element's
dominant "parent" value gives enough slack that the trivial pair
A(S)<=Total(S) + refinement-invariant mass conservation + the ladder's own
geometric telescoping sum already closes it outright — this bypasses
vertex enumeration and any MaxCeil(m-1)-style induction entirely, and is a
genuinely different (cheaper) mechanism from the "tight, no-slack" sibling
sub-case that looks superficially similar (same "S'' minus one element"
shape) but needs the sharp bound instead. Also: when checking whether a
small-index base case (e.g. m=3) of a general vertex family is fully
closed, don't assume the general open sub-case's difficulty transfers down
unchanged — a tiny cut-budget (here, exactly 1 cut over 3 rungs) can make
the "genuinely open in general" shape collapse to a small, exhaustively
by-hand-computable enumeration, closing the specific small case completely
even while the general-m case stays open (round 32, imo-2026-03,
greedy-halving-adversary: closed h(m)'s vertex c=t in S'' Case (ii) for all
m via Fact 2 + mass conservation, then found h(3) itself fully closes since
its only 1-cut-budget "split-rung" Type A collapses to a 4-case hand
computation).
