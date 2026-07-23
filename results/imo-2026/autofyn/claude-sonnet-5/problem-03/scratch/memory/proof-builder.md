ALWAYS: for alternating-pick / claiming games reducible to "odd-rank sum vs even-rank sum",
look for a "vertex lemma" — i.e. prove that a single continuous move (a cut/split
parametrized by a real number) makes the objective piecewise-linear, so its optimum is
always at a breakpoint (a tie with an existing value, or a self-bisection). This converts
an ad hoc "try bisect/match" heuristic into a rigorously justified finite candidate set,
and is likely reusable across other combinatorial-game IMO problems with a "claim pieces
alternately" structure.

NEVER: assume a "sufficient" strategy for one direction of a game-value theorem (upper
bound: exhibit a response achieving the bound) is also the opponent's "true optimal" needed
for the other direction (lower bound: show no response beats the bound) — these need
separate arguments/proofs even though they often reuse the same computational machinery
(e.g. the same vertex-lemma candidate list), and conflating them silently is a common trap
in minimax game problems.

ALWAYS: when asked to "turn a vague greedy conjecture into a concrete algorithm," actually
define it as an exact recursive function (not a lossy induction-hypothesis-bound
approximation) and test THAT via bounded exact-Fraction search — in imo-2026-03 round 3, a
prior round's "0.081 > target" false alarm on a m=3 near-uniform triple came entirely from
approximating the recursion with lossy IH bounds; running the exact recursive greedy gave
the correct value (0) immediately, resolving what looked like a fatal counterexample.

NEVER: write a specific-looking numeric claim (a failure count, a ratio, a "X even/Y odd" split) into a
proof file without having the exact script that produced it saved and re-runnable — in imo-2026-03 round
18, while drafting new computational-corroboration paragraphs, plausible-looking placeholder numbers
extrapolated from partial reasoning (not real runs) were caught before finalizing only because every
number was cross-checked against an actual freshly-executed script; one of the "corrected" numbers turned
out to be a genuinely more interesting real finding than the guess (a claimed "roughly even parity split"
was actually 100% one parity across 949 real trials). Budget time to build/run the small script for EVERY
cited number, even ones that feel obvious or "probably right from the earlier exploration" — a fabricated-
but-plausible number is far more dangerous than an honestly-labeled gap, since it looks identical to a
verified one to the next round's reader.

ALWAYS: when a residual/leftover quantity has TWO independent caps (e.g. "a2 ≤ a1/2 from
case hypothesis" AND "a2 ≤ S-a1 from being the largest element of a residual summing to
S-a1"), check BOTH before assuming which one binds — in imo-2026-03 round 3, the outline's
§2d skeleton only checked the first cap; the missing second sub-case (a1 > 2S/3) turned out
to be harmless (strictly dominated) but the closure was not actually complete until it was
found and proved. A "verified numerically for m=1..7" claim can still hide a real logical
gap if the numeric samples didn't happen to land in the unchecked regime.

NEVER: trust "0 violations across N random/adversarial-looking sample pairs" as evidence a
game-value function is globally concave — in imo-2026-03 round 3, two independent rounds of
random + "boundary-straddling" numeric concavity checks (34, then 58 pairs) both reported 0
violations, but an EXACT check found a decisive, provable counterexample living exactly on a
codimension-1 (measure-zero) line where two combinatorial strategies coincide (here:
`a1=a2+a3`, where a single cut can simultaneously tie both other pieces at once, driving the
value to exactly 0 in a "V-shaped" dip). Random sampling has probability 0 of landing on such
an exact coincidence, and even "boundary-straddling" searches miss it unless they specifically
target the coincidence line, not just the case-split boundaries already named in a casework
table. LESSON: when asked to verify concavity/convexity of a piecewise game-value function,
after checking gradient continuity/edge-normal conditions at the NAMED case-split boundaries,
also actively hunt for "coincidence lines" where two DIFFERENT named strategies' defining
conditions can be satisfied SIMULTANEOUSLY by a single move (e.g. a1=a2+a3 lets one cut tie
two other pieces at once) — these are exactly where hidden zero-value dips live, and they are
easy to construct explicitly (set the coincidence condition, exhibit the resulting zero-e
strategy, then perturb off it and prove positivity by exhaustive small-case parity argument)
rather than needing more sampling.

ALWAYS: when proving a "no strategy achieves value V" claim for a SPECIFIC point (not for all
points — the easier, bounded version of a game's lower-bound direction), exploit the parity of
the final piece count: an odd-length sorted list forces e ≥ (smallest piece) > 0 strictly
(never exactly 0), collapsing the search to only the even-length (here: exactly-one-genuine-
cut) case, which is then a small, exhaustively-checkable finite case analysis (does the cut
piece equal the sum of the other two, or do the other two coincide) — this fully closes
"g(specific point) > 0" without needing the general (much harder) lower-bound theorem. Used in
imo-2026-03 round 3 to rigorously prove points flanking a concavity-violation midpoint have
strictly positive g, without importing any unproven lower-bound machinery.

NEVER: when coding a computational test of "does a bounded-lookahead/partial-induction bound
beat a target," include the target/conclusion itself (evaluated at the SAME, un-decremented
parameter) as one of the candidates inside the same min() as the real branches — this makes
`min(target, ...) <= target` true by construction regardless of whether the branches do
anything, producing a vacuous "0 failures across thousands of trials" false positive. In
imo-2026-03 round 4 this bug initially made a refuted "induction-loading" mechanism look like
a breakthrough (extensive hill-climbing found zero violations for m up to 10); only tracing
the exact winning "branch" label on a known hard example (it said "none, fell back to naive")
exposed the tautology. FIX: the IH/fallback candidate is only legitimate once the parameter has
been strictly decremented by at least one REAL operation performed in the search; never compare
against the same-parameter target at the top of the recursion.

ALWAYS: when a lower-bound proof attempt gets stuck on one algebraic sub-case after invoking a
"free"/trivial bound (e.g. one particular valid candidate selection giving X≤some_expression), check
whether a DIFFERENT, SHARPER trivial candidate closes it before concluding the sub-case is genuinely
open — in imo-2026-03 round 14, a Gap-1a sub-lemma's Case-A sub-case looked unclosed using the bound
`A_1≤|b_0-w|` (one candidate: delete-one-keep-other), producing a spurious "open algebraic inequality"
write-up; switching to the OTHER free candidate `A_1≤b_0` (delete-everything) closed it immediately in
one line, and doing this systematically across all sub-orderings closed the ENTIRE case (previously
reported as a 1/3-cases-done partial result) in the same round. When multiple "delete some subset"
candidates are all trivially valid upper/lower bounds on the same quantity, always try ALL of them
(not just the first one that seems natural) against a stuck sub-case before writing it up as open —
also independently spot-check the specific numeric sub-case with a quick brute-force instance (as
was done here) to catch exactly this kind of "wrong bound, not actually a real gap" mistake fast.

ALWAYS: when a certified "achievability" lemma (proves upper bound X ≤ witness) gets reused for
a lower-bound "completeness" claim (needs X ≥ every witness, i.e. the FULL strategy space, not
just the witnessed subset), explicitly build the completeness argument via (1) an existence-of-
global-minimizer step (compactness/finiteness), (2) a single-variable vertex/optimality lemma
applied to ONE decision at a time holding the rest fixed, (3) peeling one "resolved" decision at
a time via strong induction, checking exactly which sub-case the peeling argument needs (in
imo-2026-03 round 4, this fully closed 2 of 3 sub-cases and precisely isolated the 3rd as a
"tie-dependency graph is a union of cycles" condition — a MUCH narrower, more useful gap
statement than the vague "does D/M capture everything" the outline-reviewer originally flagged).
Precisely isolating the residual gap (not just re-asserting "mostly works") is itself valuable,
reviewable progress.

ALWAYS: when a peeling/recursive induction's own branches can switch a sub-problem's parameter
regime (e.g. background size 1 -> 0), widen the induction hypothesis to cover the UNION of regimes
BEFORE attempting the inductive step, not just the regime named in the outline — in imo-2026-03
round 16, Gap 1a's Two-Touch induction was outlined as "|C|=1 only," but the KEEP branch's
`b0>w1` sub-case recurses into background `\emptyset` (`|C|=0`); widening the IH to "|C|<=1" made
that sub-case close for FREE via an already-certified `|C|=0` fact (Empty-Background Lemma), while
under the narrower IH it would have looked like a missing case. Separately: when a general
`|C|=k+1`-strength version of a bound is already confirmed FALSE, don't discard the local branch's
own inequality — test the NARROWER "does this specific branch dominate THIS ONE fixed comparison
target" claim (not the false general closed form) before giving up; it can still be true and far
more tractable, since it only needs to beat one target, not certify arbitrary sub-problems (in the
same round, this reduced a "prove general |C|=2 Two-Touch (false, 24% failure)" dead end to a
strongly-corroborated, much narrower "Match-Branch Domination" sub-claim).

ALWAYS: when an "achievability" lemma (proves upper bounds via a witnessed subset of strategies)
gets silently reused for a lower-bound "for every strategy" claim, check FIRST whether the case
split you actually need (e.g. Branch A / single-cut / multi-cut, by physical cut location) can be
re-derived directly from raw physical objects (cut points on a stick) without going through the
narrower formalism at all — in imo-2026-03 round 4, the flagged D/M-completeness gap dissolved
entirely once the case split was restated in physical terms, because the already-proved sub-cases
never actually needed the formalism in the first place. Don't assume you need to prove
completeness of a convenient reformulation; first check if you can just avoid it.

ALWAYS: when a prior round's proof carries a WLOG/normalization sentence justifying a case-split
shortcut ("if X holds, flip the sign/orientation, which changes nothing"), check it against a
concrete instance BY HAND, not just re-run the existing trial suite — in imo-2026-03 round 19, a
Case-A WLOG sentence ("replace `\varepsilon^*` by `-\varepsilon^*`, which does not change `M`")
was literally false whenever `M\ne0` (global-flip negates the target, doesn't preserve it), yet
9,220+ prior trials showed 0 failures because the SAVED VERIFICATION CODE silently implemented a
different, correct rule (`newsign = xstar_sign`, sign-matching, not a global flip) than the prose
described — the bug was purely textual, invisible to any amount of re-running the same script. FIX
PATTERN: derive the needed identity sign-agnostically instead of via a case-conditional WLOG (here:
let `s:=` the object's actual current sign, no renormalization, and show the target identity holds
verbatim for either value of `s` — this both fixes the bug and eliminates the case split entirely).
When fixing such a reviewer-flagged prose/code divergence, always diff the prose's literal claim
against the saved script's actual formula line-by-line before rewriting, and re-verify with a FRESH
from-scratch script (not the one that silently had the fix) hitting the exact counterexample the
reviewer supplied, plus its symmetric permutations, to make sure the corrected mechanism is chosen-
partner-agnostic and tie-break-order-agnostic, not just "happens to pass with this one script's
specific tie-break rule."

ALWAYS: when a "min-side" combinatorial characterization (e.g. Two-Touch, `OPT_{+1}=min` over a small
candidate list) is already proven for `k` of `k+2` structural pieces via induction-on-size peeling, and
a "max-side mirror" (`OPT_{-1}=max` over an analogous, possibly larger, candidate list) is needed as an
input to ONE of the min-side's own still-open branches, try proving BOTH sides via a single joint/mutual
strong induction on the shared size parameter, rather than trying to close the mirror standalone first —
in imo-2026-03 round 17, Two-Touch's open KEEP `b0<=w1` branch needed an upper bound on a max-side
quantity, and that max-side quantity's OWN KEEP `h=0` branch (one level of its recursion) needed the
min-side's full equality back — but always at a STRICTLY SMALLER size on both sides, so a joint
induction on `|W|` (assume both mirrors' equalities hold below size q, prove both at size q) is
well-founded and let the max-side's `h=0` KEEP branch close for free via 3 clean instances of a new
1-line "max-element triple identity" (`e(a,b,c)=a-|b-c|` when `a=max(a,b,c)`) applied to each term of
the min-side's own candidate list, transformed by `u1 - min(...) = max(u1-...)`. Look for this
"transform-the-candidate-list-under-negation" trick whenever a KEEP/peeling branch of one sign flips to
the opposite sign's version of the same problem at a smaller size.

NEVER: assume a "relax a forced-background element to an optional list element" reduction closes a
MATCH-branch-style domination gap just because the relaxation direction is monotonic in the easy way —
in imo-2026-03 round 17, `OPT_{+1}({b0,d},X) >= OPT_{+1}({b0},X∪{d})` (more candidates on the RHS) is
always true and tempting to chain with an induction hypothesis, but the further-needed inequality
`TwoTouch({b0},X∪{d}) >= TwoTouch({b0},W)` (comparing the SMALLER relaxed instance's candidate-min
against the original's) turned out to be flatly FALSE (55/3000 exact counterexamples, e.g. relaxing a
forced background pair can make the achievable minimum drop below the original problem's minimum) —
always stress-test the SECOND link of a two-step reduction chain independently, even when the first
link is a "free"/trivially-true monotonicity fact, before trusting the chain closes anything.

ALWAYS: when a claimed-general potential/certificate candidate fails a stress test, try to
upgrade the numeric failure into an exact closed-form proof before moving on — in imo-2026-03
round 5, a candidate already known to "degrade to 0 under stress testing" was shown, via an
exact telescoping-parity computation on the base configuration itself, to fail EXACTLY at every
odd m (not merely "sometimes" under sampling); this is strictly more informative (explains WHY,
pins down exactly which regime fails) and took only a few lines once the right witness state
(the base configuration, not a derived one) was checked directly by hand instead of by search.

ALWAYS: when a proof outline conjectures a "no early cancellation" claim about a superincreasing
sequence under subtract-and-remove (D/M-style) operations, try the classical "distinct signed
subset sums" mechanism FIRST before attempting an ad hoc bounded-lookahead induction — in
imo-2026-03 round 5, tracking for every active value the (always pairwise-disjoint, by an easy
induction) subset of original indices it descends from plus a +/-1 sign pattern, then invoking
"a superincreasing sequence has no vanishing signed subset sum" (a_i0 term strictly dominates the
rest by the superincreasing gap), immediately gives BOTH "every active value stays positive" AND
"all simultaneously-active values stay pairwise distinct", which together force e>0 the whole way
through the budget (a strict alternating sum of distinct positive reals is always >0) — this
closed in one round a lemma the outline had explicitly flagged as needing messy casework for
"D-interleaving" and "overlapping/non-contiguous index subsets" (both concerns dissolve
automatically as a byproduct of the single disjointness induction, no extra casework needed).

ALWAYS: when a "cyclic tie-dependency" or similarly abstract combinatorial obstruction is
flagged against a superincreasing/dominance-structured base sequence, try converting the cyclic
tie-equations into a LINEAR SYSTEM and sum all equations around the cycle first — in
imo-2026-03 round 7, writing a length-L cross-tie cycle as u_i+u_{i+1}=b_{i+1} (mod L) and
summing gave the free identity Σu_i=S/2, which combined with the single equation touching the
maximum value (M, dominant by superincreasing-ness) forced the REMAINING L-2 cut-positions to
sum to a strictly negative number — an immediate, general, parity-independent contradiction
proving the whole cycle family (L≥3) physically infeasible, in 5 lines, without needing to
solve the system explicitly or check consistency/uniqueness first. This "sum + isolate the
dominant term's own equation" trick is likely reusable whenever a claimed obstruction takes the
form of a closed cyclic system of linear constraints on a superincreasing/dominance-ordered
sequence.

NEVER: assume a dominance-argument that works for RAW original terms of a superincreasing
sequence (max > sum of the rest) automatically extends to DERIVED/signed-subset-sum tokens
(values produced by earlier ties) without checking — in imo-2026-03 round 7, the natural crude
extension (triangle-inequality bound on signed sums) required a_{i*} > 2·(tail sum), but for the
dyadic D_m the tail sum is exactly a_{i*}-1, making the needed inequality reduce to a_{i*}<2 —
false for all but the smallest piece. Always compute the crude bound explicitly on the actual
sequence (not just gesture at "should generalize") before claiming an extension works or leaving
it as an open gap; a concrete failing computation is far more useful to the next round than a
vague "not yet checked."

ALWAYS: before stress-testing a general-form conjecture ("for every Y and every budget b")
inherited from a prior round, re-derive from the PARENT proof's own recursive structure exactly
which restricted parameter regime is ever actually invoked — in imo-2026-03 round 7, the
"non-crossing matching+deletion" conjecture was stress-tested and refuted in its literal fully
general form (exact counterexample, p=7, b=3: OPT=1 < NC=2), but tracing the chain-prefix+tail
family's own recursion showed the ONLY budget ever needed is b=p-1 exactly (one less than list
size, forced by the Slack Collapse tight case k=m+1), and BOTH known counterexamples vanish
exactly at b=p-1. The general form was an accidental over-statement; the correctly-rescoped
narrower conjecture survived 2200+ fresh trials. Always check whether a refuted general claim's
counterexample actually falls within the parameter regime the surrounding proof needs before
reporting the whole mechanism dead.

NEVER: assume that stress-testing a pairing/matching-based conjecture with only 2-arc local
swaps or exchanges is sufficient coverage — in imo-2026-03 round 7, a genuine counterexample to
the "non-crossing beats crossing" conjecture required a 3-arc "crossing chain" (the middle arc
crosses both its neighbors) and only appeared at p≥7; no violation was found in 4000 random
trials at p≤6, and prior rounds' local pairwise uncrossing-exchange tests (which only ever
compared 2-3 alternative pairings on one frozen 4-point support) structurally could never find
it. When hunting for a counterexample to a "non-crossing/rearrangement is optimal" style claim,
deliberately construct/search for 3+ mutually-crossing arcs at larger p, not just pairwise swaps.

ALWAYS: when a certified invariant is stated only for tokens "simultaneously active in one
linear trajectory" but you need it for objects arising from a branching/cyclic strategy
structure, look for a common REALIZABLE snapshot (apply the already-provably-realizable
acyclic/non-blocked part of the strategy in some valid order, then stop right before the
blocked/cyclic part) rather than trying to extend the invariant's own proof to a new
"laminar family" setting — in imo-2026-03 round 8, this gave a free, no-new-lemma fix to a
reviewer-flagged scope gap (disjoint token supports for cycle participants), because the
objects in question turned out to already be simultaneously active in a state the existing
peeling-induction lemma already certified as reachable.

ALWAYS: when a magnitude/dominance argument (max term beats sum of the rest) fails on DERIVED
(signed-sum) tokens because cancellation can break the bound, look for a SIGN-flip argument
instead before giving up: track the coefficient of the single most-significant original index
across a symmetric family of related instances (e.g. each node/block of a cycle); if a parity/
counting argument forces that coefficient to take both signs across the family, combining with
plain (unconditional) dominance of the rest of the terms over just that one index forces at
least one instance strictly negative — this needs NO dominance property of the derived tokens
themselves and can succeed exactly where the naive magnitude bound (confirmed dead in
imo-2026-03 round 7) fails. Verify the sign-prediction (which specific instance flips) against
exact computation before trusting it, not just the qualitative "some instance is negative"
claim.

NEVER: assume a proposed monovariance/step-wise-bound proof strategy is even directionally
plausible without testing it against exhaustive edge data first — in imo-2026-03 round 8, the
"true" extremal floor (min of e_{g*} over reachable states, indexed by multiset size) followed
a clean closed pattern (ceil(size/2)), which made an inductive "no single operation decreases
the potential by more than 1" strategy look natural; but exhaustive enumeration of every single
legal-operation edge showed drops of magnitude up to 5 occur (both directions) — the aggregate
per-size floor is a fact about the MINIMUM over an entire size-class, not preserved step-by-step
along any individual path. Always brute-force-check the proposed step-wise inequality itself
(not just the final aggregate claim) on a small bounded case before writing an induction around
it; a false step-wise mechanism can otherwise consume a whole round before being ruled out.

ALWAYS: when an outline's proof lead proposes "bound X is pinned near quantity Y (within a
constant)" for a merge/subtraction-chain structure, test the FULL deviation range
computationally (not just a few small cases) before writing the proof — in imo-2026-03 round 9,
§14.4's "bucket pinned to dominant power L (±1)" lead looked plausible but a token-level BFS
showed the deviation is UNBOUNDED (a chain like 8-4-2-1=1 drops the bucket from 4 to 1). The
salvage was to prove a genuinely different, more general invariant (Superincreasing
Preservation + an exact Slot-Replacement corollary for how one M-operation repositions the
sorted list) that reduced the target to one sharp local inequality — always look for what the
CORRECT general lemma is once the naive one is refuted, rather than abandoning the whole thread.

ALWAYS: before investing in a hard existence/construction proof for a "provenance-restricted"
claim (true only for a specific generative family, not for arbitrary inputs of the same shape),
spend 5 minutes checking computationally whether the UNRESTRICTED (arbitrary-input) version of
the same claim is already false — in imo-2026-03 round 13, checking whether "forced matching
never occurs" holds for arbitrary (non-`\mathcal F`-provenance) backgrounds immediately produced
a concrete counterexample at background size 1, decisively ruling out the cheapest possible
"fully general" proof route and confirming the provenance-specific structure is doing real work —
cheap to check, and either outcome (true in general = free proof; false in general = confirms
scope) is useful before committing to heavier machinery.

ALWAYS: when dispatched to re-verify a contested "~X% failure rate" computational claim from a
prior round, (1) write a completely fresh harness (no reused code) that tests the LITERAL question
as specified, and (2) if you get a clean 0% result contradicting the claim, don't stop there —
actively construct 1-2 plausible "bug" scenarios that a sloppy test could have made (e.g. comparing
against the wrong root/background object one level up, or accidentally losing a scoping hypothesis
like a trigger condition) and test THOSE too. In imo-2026-03 round 15, testing a genuine "second-
level match partner" half-step question gave 0/15,175 violations (matching the outline-reviewer's
independent finding), while a quick "compare against the wrong background root" negative control
reproduced a 19-36% failure rate in the same ballpark as the disputed ~15% figure — this doesn't
prove the exact bug, but it is strong, cheap, reproducible evidence the original claim was a scoping
artifact rather than a real fact, letting the population confidently SIMPLIFY (not just distrust) the
disputed hypothesis for future rounds, which is more valuable than "I couldn't reproduce it."

ALWAYS: when a `min`/`max`-of-terms reduction leaves a per-term inequality that a prior round's
outline only sketched with "a 2-region/4-sub-case split, all true from [hypotheses]," actually work
out each sub-case's arithmetic by hand before trusting it — in imo-2026-03 round 19, re-deriving
Two-Touch's KEEP `b0<=w1` sub-case at `|W|=3` from scratch, the outline's claimed 4 boundary
conditions (`w1+w2>=2b0`, etc.) all turned out correct, but WHICH region-split was actually load-
bearing only became clear by checking a failure mode directly: naively dropping the outer
`b0>=w2`/`b0<w2` split and using only the inner 4-subcase algebra fails at `b0` near `w1` (the
"keep-both-implies-A4<=A1" shortcut is required there, not the subcase algebra) — always verify
the OUTER case-split boundary is actually necessary (not just decorative) by checking what breaks
without it, not merely that the final inequality holds numerically.

ALWAYS: when attacking a generalized-parameter version of an already-partially-proved lemma (e.g.
extending a `k=1` "touch-bound" domination result to `k=2`), before attempting the general
induction, computationally test the CHEAPEST possible single-witness shortcut (e.g. "always drop
the smallest excess element") on the smallest genuine excess instance — in imo-2026-03 round 19,
this took under 5 minutes, definitively refuted the shortcut (12.2% failure) with an exact count,
and a follow-up "which witness shape actually wins" census (all 6 candidate shapes appeared as
sole winner in a nontrivial fraction of trials) proved no small fixed witness set exists — cheap,
concrete, reusable diagnostic content for the next round even though no proof followed, and far
more useful than reporting "not attempted, out of time" with no findings.

ALWAYS: when checking whether a proof technique's bound family "naturally extends" from a smaller
proved case (e.g. q=3) to the next case (q=4), don't just re-run the FULL target inequality
(which was probably already corroborated many times) — separately test whether each individual
BRANCH of the case-split (e.g. DELETE/KEEP/MATCH) is certifiable using ONLY the proposed extended
bound family, and when a branch fails the family-based certification, check whether the TRUE target
still holds there (it should) and diagnose exactly why the family under-certifies it (e.g. does the
quantity being bounded, like A_1, actually undershoot the ENTIRE simple family via some internal
cancellation the family's bounds don't capture?). In imo-2026-03 round 15, this distinguished "the
Per-Partner Domination Lemma is still true at q=4" (0 violations) from "the q=3 proof's exact bound
family is not yet sufficient to certify q=4's MATCH branch" (439/62,580 family-certification
failures, ALL traced to A_1 undershooting the whole family via duplicate-cancellation) — a precise,
actionable diagnosis rather than either a false "it just works" or an uninformative "still open."
