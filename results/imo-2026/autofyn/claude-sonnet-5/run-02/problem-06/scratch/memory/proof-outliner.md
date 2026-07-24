ALWAYS: before writing a "for free / unconditional" claim derived from a certified
lemma, re-derive it line by line from the lemma's actual quantifiers — a lemma proving
"a_n shares AT LEAST ONE prime of S with EACH of several disjoint requirements" does
NOT imply "the total number of distinct extra primes a_n uses is bounded," a tempting
but false strengthening; if caught mid-draft, retract in place with a visible
correction rather than deleting the error, since the retraction itself documents the
real difficulty for the builder (round 2, imo-2026-06, greedy-exchange-cost-potential).
NEVER: revise two or more existing stuck approaches with the SAME newly-found fix in
the same round just because both share the identical crux gap — pick the
highest-Elo/most-precise one to carry the new mechanism and leave the others
explicitly stale/low-priority with a note to import the fix once proved; patching
duplicates wastes builder slots that should go to genuine population diversity (round
2, imo-2026-06: amortized-charging-budget and covering-system-construction shared gap
(†), only the latter was revised).
ALWAYS: when an explorer flags a prior round's "dead end" (e.g. round 19's
"a_1=p*q definitively refuted" for imo-2026-06) as actually dating from BEFORE a
key toolkit (Legendre Sieve Gap Bound/Primorial Floor Bound, certified round 22)
existed, re-read the original finding's exact scope before treating it as a
blanket veto — a negative result about "no naive closed-form threshold exists"
is a much narrower claim than "no proof via any future toolkit exists"; write the
correction explicitly into the new approach's skeleton (not just trust the
explorer) so a future round doesn't re-flag the same stale dead-end citation
(round 25, imo-2026-06, a1-pq-subfamily-theorem).
ALWAYS: when a crux-mining explorer surfaces a new monovariant transplant (e.g.
imo-2026-06 round 14's aimo-0134 integer-average monovariant), before writing the
skeleton, pre-check the 1-2 most "obvious" candidate integer statistics yourself
against the certified stack — one will often turn out to be either (a) already-
certified content restated (e.g. a monotone type-count = Persistent-Type Pigeonhole)
or (b) circular (a monotone quantity whose boundedness IS the open gap itself, e.g.
recruited-core size for gap (†)). Recording these as dead-on-arrival IN the new
approach's skeleton (not skipping the check) gives the builder a real, narrower
search target instead of an unconstrained "find an invariant" task, and prevents
re-discovering the same two traps next round (round 14, imo-2026-06).
ALWAYS: when a dispatch explicitly demands a "genuinely different framing, not just
a reroute of the same wall" for a crux several proof STYLES have already failed on
(e.g. imo-2026-06 round 7's FAH, after existential/pigeonhole mechanisms were
diagnosed dead by a certified negative meta-lemma), design the new approach to
target the SAME top-level claim via a structurally different kind of argument
(e.g. an exact algebraic fixed-point/recursion identity vs. existential
pigeonhole) rather than vague "try something else" — give it a concrete starting
candidate object with a checkable first step, and explicitly flag the honest risk
that it may reduce back to the old crux; a speculative-but-concrete skeleton beats
a hand-wavy "explore this direction" one even when no working invariant is known
yet (round 7, imo-2026-06, scalar-well-ordering-lock-in importing aimo-0678).
ALWAYS: treat a "this conjecture was retracted as a computational bug, now
revived with 18/18 confirming seeds" finding as provisional, not settled — round 4
revived imo-2026-06's "V=∅ always" claim this way, and round 5's explorer found 4
fresh counterexamples (a1=187,209,247,385) on the very first batch of seeds outside
the original 18, each needing exactly one recruitment round with a genuine Singleton
F'. When a prior round's "bug fix" flips a falsified claim back to "confirmed," widen
the NEXT round's numerical dragnet immediately (different seed family, not just more
of the same) before building heavy machinery on the revived claim (round 5, imo-2026-06).
ALWAYS: when dispatch explicitly asks for a "genuinely new framing" to break a
shared-gap plateau (e.g. a monovariant/potential framing borrowed from a crux corpus
entry), check whether the source crux's recurrence shape actually matches the target
problem (bounded vs. unboundedly-growing sequence) before transplanting its exact
potential function — if the shapes differ, adapt the underlying idea (e.g. "track a
per-term cost/recruitment quantity" instead of "track the raw sequence value") rather
than forcing a literal but inapplicable analogy (round 2, imo-2026-06: aimo-0678's
bounded coupled-gcd/lcm recurrence doesn't directly donate a potential to our linearly
growing sequence).
ALWAYS: when two rival "new mechanism" openings from different explorer lenses
converge on the SAME missing sub-step (e.g. round 8's "canonicality of q*:=min(F'∩F'')
vs. an alternative candidate prime r" surfacing independently from both a
fixed-witness-divisor-chain mechanism and an occurrence-order-induction mechanism for
imo-2026-06's FAH), assign them to two DIFFERENT sibling approaches anyway (they are
genuinely different top-level induction/construction structures, not the same proof
written twice) but explicitly flag in both skeletons that they share one open
sub-lemma and instruct whichever builder resolves it first to have the other import
it rather than re-deriving independently (round 8, imo-2026-06).
NEVER treat "induction on a monovariant across different seed instances" (e.g. strong
induction on |Q|=ω(a_1) via a seed-reduction/coupling lemma) as a technique-variant of
a within-instance recruitment-stage well-ordering that already died for a "refinement
manufactures new smaller witnesses" reason — the two have different logical structure
(no refinement operation exists when the induction variable is which SEED you started
from) even though both are "induct on a shrinking quantity"; this makes it legitimate
population diversity, not a reroute of the same wall, but ALWAYS require the builder's
first task be a cheap numerical cross-check of the coupling claim on 2-3 small seeds
before investing in the general lemma, since the claim itself (relating a full seed's
type-partition to a reduced seed's) has never been tested by anyone in this workspace
(round 8, imo-2026-06).
ALWAYS: before opening a speculative new "boundedness/density of occurrence gaps"
lemma as an independent target to break a plateau (e.g. imo-2026-06 round 10's
candidate "Return-Time Boundedness Lemma"), trace whether its only plausible proof
route reduces to a fact ALREADY PROVED equivalent to the open crux itself (here,
`reversible-transition-map`'s round-5 certified equivalence "S-sufficiency ⟺ V=∅").
If the only certified fact about the relevant object gives mere infinitude (e.g.
Persistent-Type Pigeonhole gives no density/gap bound), a gap-boundedness claim
almost certainly needs exactly the machinery the open crux would supply — do not
open it as a separate approach; instead build any new mechanism using ONLY the
magnitude/growth facts that are unconditionally certified (e.g. the Bounded Gap
Lemma's linear ceiling), and document the rejected circular target explicitly in
the sibling approach that avoids it, so no future round re-proposes it naively
(round 10, imo-2026-06).
ALWAYS: when a math-explorer surfaces a crux-corpus template (e.g. aimo-0680's
AP-identity squeeze) whose literal mechanism needs a global algebraic identity the
target problem's own recursive definition structurally lacks (existential/
minimality search vs. closed-form recurrence), do not transplant the template
literally — substitute the one piece of exact global structure the problem DOES
have (here, the Bounded/Generalized Bounded Gap Lemma's linear magnitude ceiling)
in place of the missing identity, and scope the resulting "adapted" mechanism as a
new, honestly-unproved key lemma rather than claiming the transplant itself is a
proof (round 10, imo-2026-06).
ALWAYS: before dispatching a new "cofinite instead of literal zero-exception" reframing
of a stuck hypothesis (e.g. imo-2026-06's FAH), re-derive from the actual downstream
proof step whether the weaker cofinite form truly suffices — don't just trust an
explorer's claim. Here it did: an "S-extended-persistent type" is defined as one
occurring infinitely often, so a finite exception set to a divisibility claim is
automatically absorbed into the existing "eventually" threshold with zero extra work,
making cofinite genuinely sufficient (round 9, imo-2026-06, verified line-by-line
against covering-system-construction Step 8.5's proof before writing the outline).
ALWAYS: when mandated to break a multi-round shared-gap plateau (e.g. imo-2026-06
round 12's "genuinely new corridor" requirement after 14 dead mechanisms), a
reformulation that is logically EQUIVALENT to the open crux (e.g. Morse-Hedlund
subword-complexity ⟺ eventual periodicity) still counts as a valid plateau-break IF
it brings a structurally different TOOLSET (pumping/pigeonhole on windows vs.
divisibility-witness recruitment) — but the outline must say so explicitly and give
the builder a WEAKER sub-target than the equivalent-to-crux one wherever possible
(e.g. "finitely many ambiguous windows" instead of "zero ambiguous windows" = FAH)
so the round doesn't just rediscover the same wall in new notation (round 12,
imo-2026-06).
ALWAYS: after 7+ consecutive rounds stuck on one crux (e.g. imo-2026-06's FAH,
16 mechanisms dead), if an explorer surfaces a genuinely untried toolkit (e.g.
idempotent ultrafilters / Hindman's Central Sets Theorem) but explicitly flags
the honest risk it may only deliver a weaker property (IP-density, not cofinite/
universal), scope the new approach's skeleton to target the SPECIFIC upgrade
that would be new (e.g. "infinitely often" -> "syndetic/bounded-gap", not
directly "cofinite") with an explicit separate bridging step, and instruct the
builder to cheap-check the upgrade on a known seed before building the full
machinery — this avoids sinking a round into unfamiliar formalism (absent from
knowledge_base.md) only to rediscover the same existential-vs-universal wall
(round 13, imo-2026-06).
ALWAYS: when a plateaued problem has a genuinely SEPARATE secondary gap that's
sat untouched for many rounds while all builder effort chases the primary crux
(e.g. imo-2026-06's "periodicity from n=1 literally," untouched since round 5),
open a dedicated approach for it explicitly conditional on the primary gap —
this is legitimate population diversity (a different wall entirely) and can
yield real progress even while the primary crux stays stuck; just require the
skeleton to state plainly it does not and cannot close the primary gap, to
avoid the Status field misleadingly implying more progress than made (round 13,
imo-2026-06).
NEVER let a small, cheap, genuinely provable negative fact (e.g. explorer's
concretely-verified "restart the greedy process at a later index" is invalid)
sit as prose in an explorer report — fold it into the highest-relevance existing
approach as a narrowly-scoped one-task revision (not a re-attempt of that
approach's dead FAH mechanism) so it gets formally proved and certified,
preventing future rounds from re-losing time to the same invalid induction
shape under a new name (round 13, imo-2026-06).
ALWAYS: when an explorer finds a genuine but narrow elementary sub-family theorem
(e.g. 2|a_1 forces trivial T=1 periodicity with no FAH needed), register it as its
OWN new approach with a target explicitly scoped to that subfamily (not the general
claim) — it is real Elo-worthy content even though it doesn't touch the main crux,
and keeps it from being buried inside a conditional-writeup approach where its
completeness could get conflated with the still-open general case (round 16, imo-2026-06).
ALWAYS: when a logically-distinct sub-gap (confirmed not equivalent to the main
crux, e.g. self-absorbing-core termination vs FAH) has fresh numeric evidence of
being comparably hard (e.g. no observed stabilization within 15,000 sampled terms
on the standard hard seeds), still open a dedicated new approach for its most
concrete untried sub-lemma (e.g. one-prime-at-a-time monotonicity) rather than
folding it into the same stalled main-crux approach — but instruct the builder to
report a clean negative result if it stalls, not force a claim (round 16, imo-2026-06).
ALWAYS: before trusting a discouraging numeric non-stabilization result on a
long-transient greedy/absorption process (e.g. imo-2026-06's H2 core-termination
lens), re-run at 2-4x the sample window before treating it as evidence of genuine
non-termination — round 16's "a_1=11305 doesn't stabilize within 15,000 terms"
flipped to "stabilizes cleanly at N(S_0)=0" once round 17 re-ran to 20,000-30,000
terms; the earlier result was a sampling-window artifact, not a structural signal
(round 17, imo-2026-06).
ALWAYS: after 3+ consecutive rounds of dedicated fresh-whole-problem-framing
sweeps (imo-2026-06 rounds 13, 15, 17) all independently find zero new corridors
for the SAME crux, treat this as strong evidence the general-mechanism well is
exhausted and shift outline effort toward (a) attacking a logically-distinct
secondary hypothesis (e.g. H2 vs H1) with a genuinely different quantity than
any previously-killed one, and (b) consolidating/auditing the current best
partial result as an explicit hedge deliverable — do not force a 19th direct
mechanism onto the same crux just to fill a build slot (round 17, imo-2026-06).
ALWAYS: when a fresh-framing explorer surfaces a crux-corpus technique whose
conclusion is structurally WEAKER than the target (e.g. round 18's aimo-0866
triangle-forcing pigeonhole gives "a bi-colored triangle exists," not
directly FAH's "every two persistent types intersect"), still open it as a
new approach but write the skeleton's open-gap section around the SPECIFIC
adaptation step (nested double-witness pigeonhole -> cross-witness
common-prime forcing) as the one genuinely unproved key lemma, and mandate a
cheap numeric check on 2-3 already-canonical hard seeds (not fresh seeds) as
the builder's first task before any general-proof attempt — this keeps a
speculative-but-concrete skeleton from silently becoming an overclaim (round
18, imo-2026-06, triangle-consistency-pigeonhole).
NEVER let a "resolved numeric exception" finding from an explorer just patch
the flagged approach's evidence text without ALSO explicitly re-stating, in
the same skeleton, which counting/pigeonhole corridors for the adjacent open
sub-gap (here H2) were separately found exhausted THIS round — bundling the
positive numeric update with the negative corridor-exhaustion finding in one
revise keeps both permanent facts in one place instead of losing the
negative one to a future round re-trying it (round 18, imo-2026-06,
self-absorbing-by-construction).
ALWAYS: when an audit/insurance-lens explorer finds a narrow subfamily
theorem that is "already implicit in the workspace but never separately
certified" (e.g. round 18's a_1=p^k for ANY prime p, not just p=2), open it
as its OWN new approach even though it looks like a trivial generalization
of an already-APPROVE'd lemma — per the round-16 precedent, this is real
Elo-worthy, cheap, low-risk insurance content, and keeps the certified-lemma
record from silently under-claiming what's actually already proved (round
18, imo-2026-06, prime-power-seed-periodicity-theorem).
ALWAYS: when a fresh-framing explorer's most useful output is a NEGATIVE
meta-generalization of an already-certified obstruction (e.g. round 19's
"Selection-Rule Class-Blindness applies to ALL statistical methods, not just
density/sieve — second-moment, Borel-Cantelli, Fourier too"), fold it as a
certification step inside the highest-relevance existing consolidation
approach (here n1-periodicity-reconciliation) rather than opening a standalone
approach for it — it closes a whole future-search family in one lemma and is
real Elo-worthy content even though it proves nothing new positive (round 19,
imo-2026-06).
ALWAYS: when proposing a "density/anatomy-of-integers" attack on an
existential gap (e.g. round 19's Two-Sided Singleton Witness existence
question), explicitly flag in the skeleton itself whether the mechanism's own
"finite alphabet" sub-claim is actually true — a fixed witness index does give
a genuinely fixed finite alphabet (reuse the certified Confined-GCD Lemma),
but do not let the outline imply infinitude-of-singleton-occurrences is
already established just because low but nonzero absolute counts were
observed in a finite window; require the builder's first task to be a direct
check of infinitude vs. finite-count-so-far before any general proof attempt
(round 19, imo-2026-06).
ALWAYS: when a subfamily theorem's proof only used a variable's *prime support*
(e.g. P(a_1)={3,q}), not its numeric value, most steps transplant verbatim to a
generalized target (a_1=3q -> 3q^m); but flag explicitly which steps DO use the
actual numeric value (finite hand-checked exceptional tables, small-window CRT
witnesses) and require those to be re-derived from scratch per generalization, not
copy-pasted, since the residue-class bookkeeping being m-independent does not mean
the specific integers being gcd-checked are (round 23, imo-2026-06, a1-3qk).
ALWAYS: when opening a "direct/non-inductive" attack on a target an inductive
technique family was proven dead on (e.g. H2's core self-absorption after
Proposition 3 killed one-prime-at-a-time chain induction), explicitly name in the
skeleton the exact certified lemma whose conclusion is tempting to over-read (e.g.
Bounded Witness Lemma's "at least one shared prime with EACH disjoint witness") and
state in the outline itself that it does NOT imply the stronger "no extra primes
outside the core" claim needed — put the false-strengthening trap in the outline so
the builder doesn't rediscover it the hard way (round 23, imo-2026-06, direct-s0).
ALWAYS: when a certified p-uniform machinery approach (e.g. a1-pq-subfamily-theorem)
leaves per-parameter instantiation as its only gap, and an explorer confirms a specific
small parameter's numeric exception set (e.g. Bad(5)={7,13,19}) matches the same
"minimal-window" shape as an already-solved instance, revise/spin off a dedicated
per-value approach (not a generic advance of the parent) — the mechanical table-build
is a near-certain APPROVE, distinct Elo-worthy content, exactly mirroring how a1-3q^2/
a1-3q^3 were split off from a1-3qk while the parent stayed partial (round 26, imo-2026-06).
NEVER treat a numeric scan (even one independently reproduced by two agents to a large
bound) as sufficient to advance a per-p subfamily theorem to "ready to build as solved"
without flagging that the analytic/sieve closure (ruling out exceptions beyond the
scanned range) is the actual remaining rigor gap — write this explicitly as the open
gap in the skeleton, don't let "numerically confirmed" quietly stand in for "proved"
(round 26, imo-2026-06, a1-5q/a1-7q-subfamily-theorem).
ALWAYS: when a per-p subfamily theorem's r=1 corollary is later shown (by
an explorer) to be provably UNIQUE among all residues r (not just
empirically special), fold the uniqueness proof into the SAME approach
file as a "why no shortcut exists for other r" narrowing — this both
certifies real new content and explicitly redirects future rounds away
from hunting for a second unconditional residue via the same witness
mechanism, rather than leaving the uniqueness as a passing explorer
remark that a later round might waste a build slot re-discovering (round
28, imo-2026-06, a1-pq-subfamily-theorem r-generalization).
ALWAYS: once a fresh-whole-problem-framing sweep for the SAME crux has
found nothing new for 3+ consecutive rounds AND a second lens (audit/
consolidation) independently confirms the "well is exhausted at current
technique level," do not dispatch a 25th/26th direct-mechanism attempt —
instead revise the existing disprove-oriented approach (fah-counterexample
-hunt for imo-2026-06) toward a genuinely NEW sub-target within it (here:
probing the OTHER open hypothesis's own implicit assumption — H2's core-
stabilization — rather than re-running the same |Q|>=3 sweep a 3rd time),
and explicitly instruct a first-ever search for a literally-conserved
(not merely bounded) invariant, since no explorer across 24+ rounds has
proposed even one candidate for that specific object (round 30,
imo-2026-06).
