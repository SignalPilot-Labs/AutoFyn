# Round 10 proof-review — imo-2026-06 (IMO 2026 P6)

Problem: prove eventual periodicity of the gap sequence a_{n+T}=a_n+L. Long-standing
crux (rounds 6–10): Joint Cofinite FAH / the Successor Claim (a specific canonical
prime q* eventually always divides a_n for one extended-persistent type, given it
divides an earlier same-type occurrence). Three approaches built this round, each
attacking FAH via a genuinely different mechanism; all three produced honest,
verified negative results plus real certifiable byproduct lemmas. No approach
overclaimed `solved`; all Status labels in the source files matched what was
actually proved once checked.

## 1. covering-system-construction — Verdict: CHANGES REQUESTED (Status: partial)

Dispatched mechanism: "Growth-Forced Divisibility," an aimo-0680-style magnitude
squeeze using the Bounded/Generalized Bounded Gap Lemma quantitatively (Step 11).

**Load-bearing step re-derived from scratch.** The Sandwich Genericity Theorem
(`n-m ≤ a_n-a_m ≤ (n-m)·a_1` for ALL index pairs, no type/class dependence) is a
two-line telescoping of (i) strict monotonicity (`a_{i+1}≥a_i+1`, immediate from the
greedy "smallest integer >a_i" definition) and (ii) the already-certified Bounded Gap
Lemma (`a_{i+1}≤a_i+a_1`). I re-derived this independently — correct, trivial,
unconditional, no gap.

The Escape-Cost Vacuity Theorem ("no argument built solely from class-blind premises
can output a class-sensitive conclusion") is a determinism-of-deduction /
substitution argument: since none of the premises (Sandwich Genericity, the static
definition of D_bad) take divisor-class data `g_n` as an input, any deduction from
them applied to a fixed pair of index values `(n_j,n_j')` produces the same output
regardless of what divisor classes those indices happen to carry — so the conclusion
cannot depend on class equality/repetition. I re-derived this line by line; it is
logically valid, if informal in the sense of not using a fully formalized proof
calculus (acceptable — matches the rigor level of prior accepted "obstruction"
results like the round-9 Witness Discontinuity Obstruction).

**Certification decision.** Unlike the round-3 Lemma F / round-6 Lemma I precedent
("diagnostic about the CURRENT certified toolkit, not portable, keep in-file"), the
Escape-Cost Vacuity Theorem is phrased and proved as a toolkit-INDEPENDENT general
principle (any class-blind fact, defined intrinsically, not by enumerating today's
lemma list) — it remains true as new class-blind lemmas get certified in future
rounds. This matches the portability bar the round-9 Witness Discontinuity
Obstruction was certified under, so I certified it (with a note explaining the
distinction from the non-portable precedent, so future rounds don't get confused
about why this one differs).

**Numeric check (Step 11.5).** Re-verified a_1=4807 at the properly-recruited core
`S₀={2,3,5,11,19,23}`: `F'={17}`, `F''={13,17}`, `q*=17`, `D_bad={13}`; only 9
A'-occurrences and 136 B'-occurrences found up to N=6000, all with `q*|a_n` (E=∅,
E_sym=∅) — matches the builder's report exactly; correctly flagged as inconclusive
for the Escape-Cost Lemma's premise (no repeat-bad-class events to test), not a
counterexample to FAH itself. No fabricated/wrong numbers found.

**Assessment.** Correct, honest, no overclaim. Real progress: a tenth FAH mechanism
cleanly retired via a rigorous impossibility proof (not just a failed search), plus
two new certifiable general lemmas.

## 2. greedy-exchange-cost-potential — Verdict: CHANGES REQUESTED (Status: partial)

Dispatched mechanism: quantitative "Escape-Budget" attack on the Successor Claim.

**Window Resolution Lemma re-derived from scratch.** Claim: for any rogue pair
(A',B'), infinitely many consecutive A'-occurrence index gaps exceed 1. Proof: fix
n_0 in the infinite set of B'-occurrences past the first A'-occurrence; n_0 falls
strictly inside some gap (n_j,n_{j+1}) of the A'-occurrence sequence (since
ρ(n_0)=B'≠A'); this gives n_{j+1}-n_j≥2 for that j; since each individual gap
interval is finite, infinitely many distinct B'-occurrences force infinitely many
distinct such j. I independently reimplemented this with a fresh trial-division
greedy-sequence generator on a_1=4807, S₀={2,3,5,7,11,19,23}, A'={3,5,19}: found 4
occurrences (indices 6, 561, 1114, 2223), all 3 consecutive gaps > 1 — confirms the
abstract proof concretely. Certified.

**Growing-Constraint Obstruction re-derived.** Two parts: (a) the Escape-Budget
Lemma's premise IS true (any skipped q*-multiple strictly between two actual
sequence terms must be illegal against some earlier index, by the same
minimum-of-a-set argument as confined-competitor-construction's tautology — I
re-checked this case split, correct); (b) the illegality witness index i(c) for a
candidate near the right end of the window can range up to n_{j+1}-1, and since the
Window Resolution Lemma shows n_{j+1}-n_j is not uniformly bounded, this witness pool
is unboundedly growing across j — not a single fixed index the way Confined-GCD's
n_B is. I confirmed none of Free Facts / Confined-GCD / the Gap Lemmas constrain a
generic intermediate index's factorization — correct, matches Lemma I's original
diagnosis via an independent route. Correctly NOT certified as a portable lemma
(explicitly toolkit-contingent, matches Lemma F/I precedent; builder's own honest
labeling agrees) — I concur with this non-certification decision.

**Return-Time Boundedness data** (max gap 503→670 as N grows 4000→6000 for a sparse
extended type) is reported honestly as inconclusive-but-suggestive-against, not
overclaimed as a falsification of anything. No issue found.

**Assessment.** Correct, honest, no overclaim. Real progress: eleventh FAH mechanism
retired via a two-part proof (premise proved true, then proved uninformative), plus
one new certified general lemma.

## 3. confined-competitor-construction — Verdict: RETHINK (Status: unsolved, as
labeled) — with an important scope correction on lemma certification

Dispatched mechanism: construct an explicit competitor `c` (round-to-nearest
q*-multiple), prove it fully legal against all earlier terms, derive a contradiction
with greedy minimality — the "confined" twin of round-7's dead Lemma K, this time
using the Confined-GCD Lemma's controlled alphabet.

**Minimality Tautology Lemma re-derived from scratch.** For n≥2, any integer c with
c>a_{n-1} and gcd(c,a_i)>1 for all i<n satisfies c≥a_n. This is a direct, one-line
unpacking of the problem's own definition ("a_n is the SMALLEST integer >a_{n-1}
satisfying [condition]" — c is by hypothesis a member of the same set a_n minimizes
over, so a_n≤c). No gap, no hidden step, fully correct and unconditional. Corollary:
no integer strictly between a_{n-1} and a_n can be fully legal against every earlier
term — also immediate and correct.

**Applied correctly to this round's outline.** The file's Case (ii) analysis (c<a_n_j
⟹ c cannot be fully legal, so the outline's "Controlled-Competitor Legality" claim is
provably false whenever it would matter) is a correct, careful application. This
specific round's dispatched mechanism (Steps 2–3, which explicitly needs FULL
legality of c to reach its intended contradiction) is genuinely and permanently dead,
as claimed.

**Overclaim found (this is the substantive finding of this review).** The file's
"Watch out for" and "Promotable lemmas" sections state the Lemma kills "this whole
family of competitor-construction mechanisms... regardless of how the competitor is
built or which certified lemmas are recruited to control its factorization" and
claims it "retroactively explains" and forecloses round-7's Lemma K entirely. I
checked this against Lemma K's actual (still-standing, certified) content: Lemma K's
proof structure does NOT try to prove full legality of its constructed competitor and
derive a direct contradiction — its useful branch (b) instead extracts information
from the GUARANTEED existence of a blocking index j₀ (gcd(c,a_{j₀})=1) and tries to
use that fact productively. This is a genuinely different proof shape from "prove
full legality, get contradiction," and the Minimality Tautology Lemma — which only
proves full legality is impossible — says nothing about whether blocking-index-based
reasoning can succeed. (Round 7's own diagnosis of why Lemma K didn't close FAH was a
DIFFERENT reason — uncontrolled identity of the blocking index — not "full legality
is impossible," so the two findings are complementary, not the same result restated.)
This is a real overclaim in the file's summary language (the worked mathematical
argument in "Application to this round's outline" itself stays within correct scope
throughout — only the broader marketing language in "Watch out for"/"Promotable
lemmas" overreaches).

**Resolution.** Certified the Lemma and Corollary exactly as proved, with an explicit
scope-narrowing note in `lemmas/minimality-tautology-lemma.md` clarifying it rules
out only "full-legality-then-contradiction" competitor constructions (permanently,
for any construction rule), NOT blocking-index-extraction mechanisms like Lemma K —
so future rounds don't misread the reach of this result and wrongly avoid a
still-viable (if so far unsuccessful) proof shape.

**Assessment.** The round's dispatched mechanism is genuinely, rigorously dead — RETHINK
is the correct verdict, matching the file's own Status: unsolved label (no overclaim
of `solved` or even `partial` progress toward closing FAH). The one issue found was a
scope overclaim in the summary/guidance language, not an error in the proved
mathematics — corrected via the certified lemma's scope note rather than rejecting
the file's core finding.

## Lemma certification summary (round 10)
- **Certified:** `lemmas/sandwich-genericity-theorem.md` — unconditional, trivial,
  re-verified.
- **Certified:** `lemmas/escape-cost-vacuity.md` — unconditional, general
  toolkit-independent screening principle, re-verified; certification note added
  explaining why this differs from the non-portable Lemma-F/Lemma-I precedent.
- **Certified:** `lemmas/window-resolution-lemma.md` — unconditional, re-verified
  both abstractly and via an independent fresh numeric simulation.
- **Certified with scope-narrowing note (new file, was previously only proposed
  in-file):** `lemmas/minimality-tautology-lemma.md` — the Lemma and Corollary as
  literally stated are correct and certified; the source file's broader "kills the
  whole competitor-construction family" claim is explicitly NOT certified and is
  flagged as an overclaim in current.md and the lemma file's own scope note.
- **Not certified (correctly, by the builder's own choice, precedent-consistent):**
  Growing-Constraint Obstruction (`greedy-exchange-cost-potential`) — toolkit-
  contingent diagnostic, matches the Lemma F/I precedent; I agree with keeping it
  in-file only.

## current.md
Updated: `## Status` header now leads with the round-10 summary (all three
mechanisms retired, tenth/eleventh/twelfth dead ends, crux unchanged); appended a
full `## ROUND 10` section with per-approach verdicts, lemma certification list, and
next-round guidance (also filled a round-9 file-maintenance gap: the "ROUND 9
section" the Status header had referenced was never actually appended to current.md
in round 9 — added a short note pointing to where that content actually lives, no
technical content was lost). No `## Full proof` section added — Status remains
`partial`, correctly.

## Net assessment
No approach reaches `solved`. All three verdicts: covering-system-construction
CHANGES REQUESTED, greedy-exchange-cost-potential CHANGES REQUESTED,
confined-competitor-construction RETHINK. Four new lemmas certified (one with an
important scope correction). The crux (Joint Cofinite FAH / the Successor Claim) is
unchanged in substance but now independently confirmed dead-ends by three
structurally different techniques (algebraic-magnitude, quantitative-window,
definitional-competitor) converging on Lemma I's round-6 diagnosis — this is a
genuine four-consecutive-round plateau on the same underlying wall (rounds 7-10 all
found new mechanisms hitting the identical "no class-sensitive / cross-occurrence
information source" obstruction), which per CLAUDE.md's plateau-breaking guidance
should trigger a genuinely different top-level framing next round, not another
variant technique against the same wall. Recorded as next-round guidance in
current.md, along with one concrete unexplored idea (a Lemma-K-style blocking-index
mechanism using Confined-GCD's finite alphabet to control the BLOCKING term rather
than the candidate — not yet attempted, and not foreclosed by any of this round's
three negative results).

Files touched: `/home/agentuser/repo/results/imo-2026-06/current.md`,
`/home/agentuser/repo/results/imo-2026-06/lemmas/sandwich-genericity-theorem.md`,
`/home/agentuser/repo/results/imo-2026-06/lemmas/escape-cost-vacuity.md`,
`/home/agentuser/repo/results/imo-2026-06/lemmas/window-resolution-lemma.md`,
`/home/agentuser/repo/results/imo-2026-06/lemmas/minimality-tautology-lemma.md`
(new).
