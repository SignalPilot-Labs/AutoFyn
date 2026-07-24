## Outline review — round 7 — imo-2026-06

Field of 3 (2 revisions, 1 new): `greedy-exchange-cost-potential` (revise),
`covering-system-construction` (revise), `scalar-well-ordering-lock-in` (new).

---

### 1. greedy-exchange-cost-potential (revise) — Verdict: CHANGES REQUESTED (approve for build, with a mandatory checkpoint)

**Step 3 (Divisor-Restricted Pigeonhole)** — fine, a genuine free corollary of the certified
Generalized Bounded Witness Lemma's Corollary + finite pigeonhole. No issue.

**Step 2 (Two-Witness Intersection Uniqueness, |F'∩F''|=1) — this is the flagged risk, and
my assessment is it is NOT clearly escaping Lemma I's diagnosis; it is at serious risk of
being exactly the "direct Lemma H branch analysis" mechanism Lemma I already proved dead,
wearing new packaging.**

The claimed novelty is: apply Lemma H's dichotomy to *two* candidate primes p₁,p₂ ∈ F'∩F''
against the FIXED earliest witness a_{n_B} itself (rather than a hypothetical failing
successor), then argue the two branch-(b) witnessing indices i₁,i₂ "cannot be distinct
without contradicting minimality of n_B's own status as earliest B-occurrence."

This is precisely the same combinatorial configuration round 5's `greedy-exchange-cost-
potential` already analyzed and explicitly gave up on: "nothing in the certified stack
connects those witnessing indices to force a contradiction" (see
`results/imo-2026-06/current.md` ROUND 5 section, and the source file's own round-5 write-up
around line 700+: "two distinct primes q′,q″ ∈ F′ can each independently satisfy Lemma H's
branch (b) via different earlier witnessing indices i,i′ with no forced relationship").
The round-7 outline's proposed fix — "show that if i₁<i₂<n_B both critically witness distinct
primes against a_{n_B}, one of them already forces an earlier index with base type B,
contradicting n_B's minimality" — asserts the missing link but gives **no mechanism for why
a branch-(b) witnessing index (P(a_i)∩P(a_{n_B})={p} exactly) would have base type B at
all.** There is nothing in the certified Lemma H statement, or anywhere else in the
certified stack, connecting "unique-shared-prime witnessing index" to "has extended type B."
This is a load-bearing claim asserted without a mechanism — exactly the pattern CLAUDE.md
and this role's mandate flag as an unverified hand-off. The outline's own "Watch out (ii)"
paragraph admits this directly ("a priori consistent unless the earliness of n_B is actually
used to force a relationship between the two indices" — that relationship is not shown, only
hoped for).

**Verdict on step 2 specifically:** build it, but treat it as *presumptively* a 4th instance
of the dead "Lemma H branch analysis" mechanism unless the builder produces the actual
missing link (why a branch-(b) index must carry base type B, or some other genuine
new fact) in the first pass. If it fails — which is the likely outcome given the identical
round-5 wall — the builder must document the precise obstruction with Lemma-F/Lemma-I rigor
(this round's outline already commits to that fallback in step 6, good) rather than silently
dropping it or re-trying variants next round.

**Step 4 (Blocking-Data Bridging)** uses genuinely unused NEGATIVE (illegality) information
— this part is a legitimate new mechanism not covered by Lemma I's diagnosis (which only
inspected the four positive/existential tools). Buildable and worth attempting independent of
step 2's outcome, though it is stated conditional on step 2/q existing — the builder should
note whether step 4's argument can proceed with an ARBITRARY q ∈ F'∩F'' (not necessarily
unique) as a fallback if step 2 stalls, to avoid step 4 being wasted if step 2 fails.

Cases (n_A<n_B vs n_B<n_A): correctly flagged as needing an explicit check, not just asserted
symmetric — hold the builder to actually checking it, not asserting "by symmetry."

---

### 2. covering-system-construction (revise) — Verdict: CHANGES REQUESTED (approve for build)

Step 3 (Symmetric FAH mirroring) is appropriately hedged, not circular: it explicitly states
"SHOULD be a direct mirror" and then names the one place symmetry could break (transferring
the joint-Lemma-H argument to B'-occurrences after n_B) and instructs the builder to verify,
not assume. This does not assume what FAH needs to prove — it correctly treats Symmetric FAH
as depending on the sibling's step 2 output and flags the exact spot requiring a fresh check.
Good practice, and the alternate-note contingency (fall back to attempting Symmetric FAH from
FAH alone if Two-Witness Uniqueness isn't certified this round) correctly prevents this file
from stalling entirely if the sibling's step 2 fails per point 1 above.

**Diversity flag (do not let this slide unremarked): this approach and the sibling now share
literally the same crux mechanism** (the joint-Two-Witness/Lemma-H argument), just mirrored to
the two sides. This is not a new instance of the "shared-gap plateau" — it has been true since
round 6 (both approaches converge on FAH/Symmetric FAH) — but it is now MORE tightly coupled
this round since the sibling's step 2 is a direct import dependency of this file's step 3. If
step 2 fails as suspected above, both approaches inherit the identical wall on their primary
new content. `scalar-well-ordering-lock-in` (approach 3) is the only genuinely independent
line in the field this round — see below.

Step 5 (n=1 literal extension) is a legitimate, well-scoped, previously-untouched secondary
target with an honest mechanism (finite prefix check + lcm period-scaling), correctly flagged
as having real open content (residue alignment), not a formality. Approve.

---

### 3. scalar-well-ordering-lock-in (new) — Verdict: APPROVE, register and build

Genuinely different proof STYLE from the FAH/joint-dichotomy field: instead of trying to
promote an existential per-occurrence fact into a universal one (FAH's shape), it attempts an
exact algebraic recursive identity between successive stages' "recruited-prime part" scalars
g_k, in the style of aimo-0678's two-scalar mechanism. This is not a rebrand of FAH — it is a
different mechanism attempting to reach the same finite-termination conclusion by a different
route (bypassing "every occurrence" entirely if the recursive identity holds).

It has enough structure to be buildable, not just a slogan: w_k and g_k are concretely defined
(lex-first open pair's earliest witness value; product of recruited primes' valuations in that
witness), and step 4 states a specific, falsifiable target claim ("recruiting q_k against the
lex-first open pair forces q_k | a_{n_B'} for the NEXT stage's lex-first witness"). This is
checkable by direct simulation before any proof effort is spent — the builder should run this
check FIRST (per this workspace's established practice of numerically testing quantitative
claims before investing in a proof attempt).

The outline is honest about the risk (no concrete scalar verified yet, explicit warning not to
force-transplant aimo-0678's literal formulas, explicit acknowledgment that step 4 might turn
out to be a disguised form of Symmetric FAH — flagged as an acceptable but must-be-disclosed
outcome, not smuggled in as an independent bypass). This meets the bar for a real, honest new
approach, not an overclaimed slogan. It reuses the certified free content (open(k), Lemma G)
only as scaffolding, which is legitimate (that reduction is proven, not itself in question).

Register this new approach.

---

### Never-re-attempt list check

- Two-Witness Intersection Uniqueness (|F'∩F''|=1) is **not** a restatement of the falsified
  Universal Singleton Hypothesis (|F'|=1): it is the intersection of two DIFFERENT witnesses'
  outside-core sets, consistent with the |F'|=2 counterexample seed a_1=11305 used as its own
  supporting evidence (F'={11,103}, F''={11}, F'∩F''={11}, size 1 despite |F'|=2). Legitimate,
  distinct target — not a repeat.
- scalar-well-ordering-lock-in's well-ordering is on open(k) (already certified non-increasing
  via Collateral-Safety) plus a NEW algebraic scalar g_k — not the previously-dead witness-
  index/set-size descents (round 3's |A'|+|B'| measure, round 5's witness-index descent), which
  failed because their monovariants were not stage-monotone under refinement. Different object,
  not a repeat.
- No approach restates PUCL, universal-glue-prime/cost≤1, reversible-transition-map, or
  recruitment-round-charging's three dead candidates.

---

### Diversity assessment (for the orchestrator)

Approaches 1 and 2 are tightly coupled on the SAME new mechanism (joint Two-Witness/Lemma-H
argument) this round — a real risk that if it fails (which I judge likely, see above), both
approaches stall on the identical wall simultaneously, same as flagged in round 6's guidance.
Approach 3 is the genuine diversification this round asked for. If step 2 stalls again next
round, the orchestrator should escalate scalar-well-ordering-lock-in's relative priority and
consider seeding a second, even-more-independent line (e.g. a density/asymptotic-domination
crux search, per round-6's next-round guidance option (a)/(b)) rather than a third variant of
the joint-dichotomy mechanism.

---

build set: greedy-exchange-cost-potential, covering-system-construction, scalar-well-ordering-lock-in
