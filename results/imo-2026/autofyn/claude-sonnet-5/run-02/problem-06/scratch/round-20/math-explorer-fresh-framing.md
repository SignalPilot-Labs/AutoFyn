## imo-2026-06 — 5th fresh-framing sweep (rounds 13/15/17/19 found nothing new; this is the follow-up)

### Distinct openings considered, with honest verdicts

**1. Priority-argument / finite-injury requirement-satisfaction (computability theory).**
Structurally examined: a finite-injury argument needs (a) a countable list of
requirements, (b) a well-ordered priority, and (c) genuine *freedom* at each stage
to act on behalf of a requirement, with a proof that higher-priority actions injure
lower-priority ones only finitely often. Our sequence has **zero degrees of
freedom**: `a_1` fixes the entire sequence via the deterministic greedy rule, so
there is no "construction" happening that a priority argument could steer — we are
proving a property of an already-fully-determined object, not building one. If one
tries to dress FAH itself up as "requirement k: the k-th occurrence of the
persistent type is captured by witness prime q," the needed fact ("only finitely
many occurrences are captured by a DIFFERENT prime," i.e. finite injury) is *exactly*
cofinite FAH restated — and the needed injury bound is exactly the open content of
H1/H2 (boundedness of `N(S_k)`). **Collapses into the standing H1/H2 hypotheses —
not a new mechanism, just new vocabulary for the same open gap.**

**2. Computability/decidability framing as an obstruction, or as an
effective-transfinite-induction proof style.** Two sub-versions considered:
(a) "Is FAH undecidable, hence unprovable by elementary means" — even if true this
would not help produce an IMO-style proof (the problem is asserted provable; an
undecidability finding would only be a meta-remark, not a proof route), and there
is no actual undecidability structure here (no encoded halting problem; the greedy
rule is primitive recursive and every finite prefix is *computable*, just not
obviously *analyzable* in closed form). (b) "Kleene recursion theorem /
self-referential construction" style techniques build an object that refers to its
own future computation — not applicable, since our object is already given by an
explicit rule, nothing to construct self-referentially. **Both sub-versions are
dead on arrival: no genuine computability-theoretic structure is present beyond
"the rule is computable," which was never in doubt and buys nothing new.**

**3. A sharper, genuinely new diagnostic (not previously stated this precisely):
"the sequence is fully deterministic, so 'two legal continuations of the same
finite prefix' is a claim that must be independently constructed, not assumed."**
This directly examines and generalizes round 19's finding on
`n1-periodicity-reconciliation`'s §7 Generalized Class-Blindness Obstruction
(found circular: it assumed "both continuations are a priori consistent" as a
premise, when that is exactly H1's open content). Tracing through the *entire*
confirmed-dead list under this lens: Borel–Cantelli/probabilistic,
ultraproduct/compactness, and any Baire-category/genericity argument (a natural
"6th fresh framing" candidate I considered and rejected before writing it up) **all
implicitly require an ensemble of "possible" tails consistent with a fixed finite
prefix** — a probability space, an ultrafilter of scenarios, a comeager set of
completions. But for THIS recursion, given `a_1`, the *entire* infinite sequence is
already uniquely pinned down: there is exactly one legal completion, not a space of
them. So none of these frameworks even have a legitimate ensemble to operate on
unless one is separately constructed (e.g. by varying `a_1` over a class of seeds
sharing the same core `S_0` — which is exactly what the certified CRT-glue/
competitor-construction family already tried and found magnitude-infeasible, 8+
orders of magnitude overshoot). This is not merely "these techniques are hard here"
— it is a structural reason (determinism ⟹ no free ensemble) that explains, in one
line, why the whole "compare against a hypothetical alternate scenario"
super-family (Borel–Cantelli, compactness/ultraproduct, LP-duality relaxation, and
now Baire-category/genericity, which I am adding to the confirmed-dead-on-arrival
list for the same reason) keeps failing on the same wall: they all smuggle in an
indeterminacy the recursion doesn't have. **This is a genuine (if modest) new
finding: it should be handed to the outliner as a standing meta-rule — any future
gap-closing argument premised on "two scenarios consistent with the same data" must
supply an actual construction (e.g. two distinct `a_1` seeds, verified computationally
to share a long common core/prefix and then diverge) or it is invalid by
construction, not merely unproven.**

**4. o-minimality / tame geometry.** Requires definable sets in an ordered
structure (typically `(R, <, +, ·)` or expansions) with a cell-decomposition /
finiteness theorem. The problem's data is purely combinatorial-arithmetic
(divisibility, gcd, primes) — there is no natural real-closed-field or o-minimal
expansion that captures "gcd(x,y)>1" as a definable relation with the needed tame
finiteness properties (divisibility is not first-order definable in RCF at all; it
lives in Presburger/Peano arithmetic territory, which is the OPPOSITE of tame —
undecidable/complex, not o-minimal). **No applicable structure. Dead on arrival,
confirmed by direct structural check, not just intuition.**

**5. Model theory / nonstandard analysis (ultrapower `*N`, transfer principle,
overspill).** Considered as "genuinely different from ultraproduct/compactness" —
but on inspection it is not: taking a nonstandard extension and using overspill to
get a nonstandard bound is exactly the analytic content of the already-tried and
confirmed-dead compactness/ultraproduct approach (a nonstandard model of the
integers IS an ultraproduct construction). **Collapses into the already-confirmed-
dead ultraproduct/compactness mechanism; same wall (existential-to-universal
promotion gap — a transfer/overspill argument gives "for all standard N there is
a nonstandard bound" which is precisely the class-blind pigeonhole shape already
diagnosed as vacuous).**

**6. Spectral/operator-theoretic on the shift map, beyond transfer-operator.**
Considered Perron–Frobenius / random-walk-on-residues framings distinct from the
already-dead transfer-operator approach — but any such spectral method needs a
FINITE (or at least tractable) state space for the "residue class" random walk,
and the certified diagnosis (Termination Criterion Lemma, round 15; Threshold
Recursion Bound Lemma's Prop 3, round 16) is precisely that no finite-state
abstraction of the process is currently known to exist independent of the open H2
hypothesis — the state space itself (which core, which persistent types) is only
finite IF H2 already holds. **Collapses into H2; not independently attackable
without first resolving what it needs as an input.**

**7. Well-founded ordinal descent / term-rewriting-termination style (Dershowitz–
Manna multiset/lexicographic path orderings) — genuinely distinct TECHNIQUE from
priority arguments and from pigeonhole, flagged as literally untried by name in the
confirmed-dead list.** This is the one candidate I'd call worth a real (but
low-confidence) shot, and only for **H2** (absorption-chain termination), not H1
(FAH) directly. The idea: instead of trying to compute or bound `N(S_k)` (which
round 16's Prop 3 shows is not determined by any finite-prefix-computable
statistic), assign each core-enlargement step a value in a well-founded order
(e.g., a multiset of "outstanding obligations") and show it strictly decreases,
without needing an explicit numeric bound. However, tracing through *why* Prop 3
kills the numeric-bound approach — "an infinite 0/1 legality-history sequence is
never decided by any finite prefix, so no finite-prefix-computable functional of
the process can be proven non-increasing along the ACTUAL realized process without
already knowing the tail" — this obstruction is not really about numeric bounds
specifically; it applies to *any* would-be monotone/well-founded assignment built
from finite-prefix data, ordinal-valued or not. **I expect (but did not fully
verify — this is a one-line-flag, not a worked-out refutation) that a literal
Dershowitz–Manna-style construction here would need the same missing ingredient
(a provably-decreasing measure derived from data the recursion doesn't expose in
finite time), so it likely reduces to Prop 3's wall too — but this is the one
item on this list that is not a pure relabeling and could genuinely be tried for
one round on H2 specifically before being marked dead, since "ordinal/well-founded
descent" as a *named* technique has not appeared in the 20+-mechanism dead list.**

### Cheap-kill candidates
None obvious beyond what's certified. No new parity/pigeonhole/injection idea
surfaced this sweep that isn't already a repackaging of a dead mechanism.

### Knowledge-base entries
`knowledge_base.md` is a generic 247-line KB (Algebra, Linear Algebra, Number
Theory, Combinatorics, Geometry, General Proof Methods, Monotone Subsequences,
Heuristics, Meta-Strategy) — confirmed by direct grep: **it contains zero entries**
on computability, decidability, model theory, nonstandard analysis, o-minimality,
ergodic theory, or priority arguments. Nothing new to cite from it this round; all
of this problem's certified machinery so far comes from the workspace's own
lemma files (`lemmas/*.md`), not from `knowledge_base.md` directly.

### Analogous past problems (crux corpus)
Searched `number_theory`/`combinatorics` cruxes for keywords `eventual`,
`periodic`, `greedy`, `priority`, `requirement`, `forcing`, `diagonal`,
`stabiliz`, `cofinite`, `absorb`, `recruit` across all 2434 entries.
- **`aimo-0009`** (ISL/IMO-style: monotone periodically-extended sequence bound)
  — technique: "minimal-index counterexample + periodicity forbids a residue
  window, forcing a jump by a full period." Superficially the closest match in
  *shape* (minimal-counterexample-plus-periodicity), but **not actually
  analogous**: that problem is GIVEN periodicity of the sequence as a hypothesis
  and derives a numeric bound from it; our problem must PROVE eventual
  periodicity itself, with periodicity as the unknown, not the premise. The
  technique doesn't transfer because there is no periodicity fact yet to invoke.
- **`aimo-0077`** (game-terminates-on-a-finite-board): technique "assume
  non-termination forces a repeating state cycle in a FINITE state space, take
  the minimal object touched in the cycle, contradict via a forced smaller
  action." Relevant *in spirit* to H2 (does the core-enlargement/absorption
  process terminate) but requires an a priori **finite** state space, which is
  exactly what is NOT known to exist for our process independent of H2 itself —
  same circularity as items 6/7 above. Not directly usable without first
  resolving H2's own open content.
- **`aimo-0184`** (greedy-minimal recursion `x = 1 + S(x)` matched against a
  candidate set via an exact closed-form counting identity): interesting
  greedy-minimality shape, but its crux move depends on an EXACT closed-form
  formula for the defining sum (`floor((c/b)^{1/k})` partition-counting
  identity) that has no analogue here — our recursion's "legality" predicate
  (gcd > 1 against all prior terms) has no known closed form, which is precisely
  the obstruction the workspace's `triangle-consistency-pigeonhole` (round 19)
  diagnosed for the sieve/anatomy-of-integers route. Not transferable.
- No crux in the corpus uses a literal priority-argument, forcing-construction,
  or computability-style requirement-satisfaction technique for a periodicity or
  eventual-behavior claim — searched explicitly for `forcing`, `priority`,
  `requirement`, `diagonal` and found no matches of that flavor; the closest
  "diagonal" hits (`aimo-0187`) are algebraic substitution tricks, unrelated.

### Prior progress
Unchanged from `current.md`: Status `partial`. Floor deliverable (2|a_1 fully
solved; a_1=p^k fully solved, overlap = 2^k) certified. H1 (FAH) and H2
(absorption-chain termination) both remain open, now reduced to exactly these two
named hypotheses via the certified Master Conditional Theorem. Newest sharpest
open residuals: the Two-Sided Singleton Witness Theorem's existence hypothesis
(H1-adjacent) and the H2 existential sub-target (does *some* self-absorbing core
exist at all). 5 lemmas newly certified in round 19 (see current.md for names).

### Dead ends (do not retry — reconfirmed or newly diagnosed this round)
- Everything on the 20+-mechanism list in the dispatch prompt (gcd-pigeonhole,
  magnitude/sandwich, CRT-glue, sieve/density/Mertens, automaton/graph-walk,
  Ramsey/ultrafilter, p-adic valuation monovariants, class-blind statistics,
  Morse-Hedlund/EEA, ultraproduct/compactness, per-prime indicator decomposition,
  transfer-operator, LP-duality, generating functions, probabilistic/
  Borel-Cantelli, extremal graph theory, character-sums, anatomy-of-integers).
- **Newly folded into the same dead family this round** (not previously named
  explicitly, now diagnosed and should be added to the standing list): Baire-
  category/genericity arguments, and nonstandard-analysis/overspill arguments —
  both require a nonexistent ensemble of "possible tails," exactly the same
  structural defect that kills Borel–Cantelli and ultraproduct/compactness (see
  opening #3/#5 above).
- Priority-argument/finite-injury framing and computability/decidability framing:
  examined fresh this round, found to be pure relabelings of H1/H2 or structurally
  inapplicable (no genuine freedom/undecidability content present) — add to the
  dead list as "considered and diagnosed, not just skipped."
- o-minimality/tame geometry: no applicable structure at all (divisibility isn't
  o-minimally definable) — dead on arrival.

### Small-case / intuition notes
No new numeric experiment was run this round (this sweep was structural/framing
reconnaissance per the dispatch, not a new-mechanism build); all prior numeric
evidence in `current.md` (zero FAH counterexamples across 50+ seeds at properly-
recruited cores) stands unchanged and is not contradicted by anything found here.

### Honest bottom line for the outliner
This 5th fresh-framing sweep found **no new mechanism that survives structural
scrutiny** for FAH (H1) itself. The one item worth a genuine (low-confidence) shot
is **#7, well-founded ordinal/ multiset-order descent (Dershowitz–Manna style),
aimed specifically at H2** (chain termination), not H1 — it is a technique name
not previously on the dead list, though I suspect on inspection it will hit the
same "no finite-prefix-computable monotone measure" wall that killed round 16's
Threshold Recursion Bound Lemma (Prop 3). The clearest actionable, non-technique
finding is **#3**: a sharpened standing meta-rule for the outliner/reviewer — any
future approach that argues via "two scenarios/continuations consistent with the
same observed data" (this pattern recurs across several of the dead mechanisms,
most recently round 19's circular Generalized Class-Blindness Obstruction) must
supply an actual two-seed (or two-index) construction verified to share data and
diverge, because the recursion is fully deterministic and such non-uniqueness is
never a free assumption here. This should be treated as a standing pre-build
screening check, in the same spirit as the round-11 CRT Magnitude Obstruction
pre-build screen.
