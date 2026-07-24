# Round 19 proof-review — imo-2026-06

Overall workspace Status: **partial** (unchanged). No approach reaches
`solved` this round; the run's 2 certified floor-deliverable subfamily
theorems (`2|a_1`, `a_1=p^k`) and the Master Conditional Theorem chain (H1
FAH, H2 core-termination) are unchanged. All 4 built approaches this round
verdict **CHANGES REQUESTED**, with `core-growth-monotonicity` additionally
flagged `dead-end` for the sub-target it attacked (its lemma content is fine,
but the specific mechanism this round hit the standing Prop-3 wall again).

## (1) n1-periodicity-reconciliation

**§8 (floor-deliverable audit).** Pure citation/consolidation of Theorems A
(`2|a_1`) and B (`a_1=p^k`), correctly scoped (states exact overlap `a_1=2^k`
and exactly what is NOT covered). No new content, no gap. Fine as-is.

**§7 (Generalized Class-Blindness Obstruction) — genuine gap found, NOT
certified.** The file proposes a strict generalization of the certified
`escape-cost-vacuity.md` / `density-argument-vacuity-corollary.md` results
to any "window-computable statistic" Φ(N), covering density, second moment,
Borel–Cantelli, finite-Fourier/character-sum coefficients, and LP-relaxation
in one meta-argument. I re-derived the two certified predecessors from
scratch to establish the actual bar these must clear:

- `escape-cost-vacuity.md`: premises are, BY DEFINITION, functions of only
  the fixed indices `(n_j, n_{j'})` and `a_1` — they structurally cannot
  reference the realized divisor-class datum `g_n` at all. So "two scenarios
  give the identical premise value" is a tautology that follows immediately
  from the definition of "class-blind" — no construction is needed.
- `density-argument-vacuity-corollary.md`: same shape — its `C(X)` is a pure
  Mertens-type ambient count over ALL integers in a window, again
  structurally excluding realized-sequence data by definition.

§7's new `Φ(N)` is defined (§7.1) over `W(N)`, which explicitly **includes
the realized legality/occurrence Boolean history** — actual observed data
from the (for fixed `a_1`, deterministic) greedy process. For the "two
scenarios" step to work here, one needs two genuinely different, both
fully-legal completions of the *same* finite prefix of the *same*
deterministic recursion, agreeing through the window and diverging after.
The proof's only justification for this ("nothing in the recursive
definition... forces a UNIQUE outcome... this is exactly the open content of
H1 itself, so by definition of 'open', both continuations are a priori
consistent") is **circular**: it assumes, as a premise, that the tail is not
determined by the prefix, which is exactly the open content it is trying to
use to prove impossibility of proof. No concrete pair of legal continuations
(or pair of `a_1` values reproducing the same window data with divergent
tails) is ever exhibited — unlike what a faithful generalization of the two
certified predecessors would require.

I attempted to patch this myself: restricting Φ to genuinely ambient,
ancestor-decoupled-from-realized-data statistics (matching the actual scope
of the two certified predecessors) DOES give a correct, easy corollary — but
that restricted version does not actually cover the four named method
families as claimed in §7.1, since density, second moment, finite-Fourier
coefficients, and LP-relaxation objective values, as the file itself defines
them, are explicitly built from realized occupation/occurrence counts, not
from purely ambient data. So the correct version is strictly weaker than
what §7.3 claims to have closed off.

**Verdict on this lemma: NOT certified.** This is a real, load-bearing gap
(not a stylistic nitpick) — the four families are not yet formally ruled out
by this argument, though the underlying suspicion they are all dead (per
20+ prior confirmed-dead mechanisms) is not contradicted, only unproven by
this specific write-up. Recommend either (a) an explicit two-instance
construction (e.g., two different `a_1` seeds producing identical window
data but provably divergent tails, or a proof that such a pair must exist),
or (b) restricting the theorem's scope to genuinely ambient statistics only
and honestly noting the restriction does not cover all four named families.

**Overall verdict: CHANGES REQUESTED** (Status `partial`). H1/H2 untouched.

## (2) triangle-consistency-pigeonhole

**§5.1 (`ω(a_n) = O(log n)` bound).** Correct, trivial, independently
re-derived (`a_n ≥ 2^{ω(a_n)}`, combined with the already-certified Bounded
Gap Lemma `a_n ≤ n·a_1`). **Certified**
(`lemmas/elementary-omega-bound.md`).

**§5.2 (extended computational check).** Honestly reported as consistent-
with-but-not-proof-of infinitude; no overclaim.

**§5.3 (sieve/anatomy-of-integers obstruction).** A sound, carefully argued
methodological diagnosis: known sieve techniques (Brun/Selberg,
Hardy–Ramanujan/Erdős–Kac) require an explicit closed-form target sequence
with independently computable/CRT-combinable local densities; the
persistent-type index set `X_A` and out-of-core cofactor `w_n` here are
defined only implicitly via the entire greedy legality history, with no
known closed form. This is correctly NOT framed as a formal theorem, only as
a documented obstruction (matching the Lemma-F/Lemma-I "diagnostic, not
portable" precedent) — appropriately not certified as a standalone lemma,
kept as in-file documentation.

**Also certified this round** (independently re-verified in full, re-derived
every proof step from scratch, and re-ran both cited computational checks on
`a_1=4807` and `a_1=11305` matching every reported number exactly), the
three round-18 lemmas that had been left uncertified pending further use:

- `lemmas/double-witness-nested-pigeonhole.md` — correct two-fold
  application of Confined-GCD + elementary infinite pigeonhole.
- `lemmas/same-type-triangle-vacuity.md` — correct instance of the
  Same-Type Free-Facts Vacuity phenomenon applied to the specific "triangle"
  quantity `e := gcd(a_{m_A},a_{m_A'})`; confirmed genuinely distinct
  content from the already-certified `same-type-free-facts-vacuity.md`
  (that lemma is the general phenomenon statement; this one is its specific
  instantiation against the outline's dispatched mechanism, which kills that
  specific construction).
- `lemmas/two-sided-singleton-witness-theorem.md` — correct, conditional
  (on an explicit, precisely-stated existence hypothesis), direct two-fold
  application of the already-certified Singleton-Side FAH Lemma at
  non-canonical witnesses (legitimate — that Lemma's own proof never
  requires the earliest occurrence). Fully explains both of the workspace's
  only two known properly-recruited-core hard rogue-pair seeds; existence
  hypothesis itself remains genuinely open (confirmed distinct from, not a
  restatement of, the main FAH crux).

**Overall verdict: CHANGES REQUESTED** (Status `partial`). H1's existence
hypothesis (matching singleton witnesses) remains open.

## (3) core-growth-monotonicity

**§5.0.** Correctly and honestly identifies the round's dispatched "weaker
existential H2 target" as NOT new content (verbatim the standing sub-gap (a)
of the certified Self-Absorbing Core Theorem) — no overclaim.

**§5.1 (Monotone Chain Reformulation Lemma).** Re-derived from scratch:
`S_M := S_0 ∪ ⋃_{j≤M} P(a_j)` is explicit and monotone; if `N(S_M) ≤ M` then
`⋃_{j≤N(S_M)} P(a_j) ⊆ ⋃_{j≤M} P(a_j) ⊆ S_M`, so `S_M⁺ = S_M`. Correct,
one-line, fully unconditional. **Certified**
(`lemmas/monotone-chain-reformulation-lemma.md`).

**§6 (Proposition 4) and §7 (Proposition 5).** Both re-checked: (a) the
"finite base-type alphabet forces stabilization" hope fails because Binary
Refinement can split persistent types without bound as more primes are
adjoined (no certified cap on `|𝒫'(S_M)|` independent of `M`); (b) the
per-prime Threshold Recursion Bound iterated along the `S_M` chain
re-invokes Prop 3's non-constructivity of `M_B` verbatim (Prop 3 was stated
generically for any finite core and one adjoined prime, so this reuse is
legitimate, not smuggled); (c) the converse (does an arbitrary self-
absorbing `S**` get captured by the `S_M` family?) genuinely fails since
monotonicity of self-absorption under enlargement is not established by
anything certified. All three are honest, correctly-scoped negative
findings — no gap found in the negative reasoning itself.

**Overall verdict: CHANGES REQUESTED** (Status `partial` for the file
overall — a genuinely new, certified reformulation lemma was produced), but
recorded to the ranker as a further-confirmed **dead end for this specific
attack style** (adjoin-one-prime-at-a-time / bounded-prefix-data), since the
round's own dispatched target hit the identical wall a third time.

## (4) self-absorbing-by-construction

Independently reimplemented the greedy sequence from scratch (SPF-sieve +
per-prime bitmask, same style as the round-18 third script) for both new
seeds.

- `a_1=510510` (`|Q|=7`): exactly reproduced the reported first occurrences
  at window 65000 (`{2,3,5,11,13,17}` at `n=36466`; `{2,3,7,11,13,17}` at
  `n=51052`) and confirmed both recur by window 200000
  (`36466,72931,109396,145861,182326`, constant gap 36465;
  `51052,102103,153154`, constant gap 51051). Exact match, no discrepancy.
- `a_1=209370`: found and corrected a **minor mislabeling**: the file
  claims the second single-occurrence type at `n=34896` is `{2,3,5,7,997}`
  (i.e. `Q` itself), but the actual type at `n=34896` is `{2,5,7,997}`
  (missing prime `3`) — a distinct, proper sub-type. Exhaustive re-check at
  window 60000 confirms exactly two single-occurrence types exist:
  `{2,3,5,7,997}` at `n=1` and `{2,5,7,997}` at `n=34896` (not two copies of
  `Q`). This does not affect the round's qualitative conclusion — both types
  are independently confirmed to recur by window 300000
  (`{2,3,5,7,997}` at `1,104686,209371`; `{2,5,7,997}` at
  `34896,69791,139581,174476,244266`), leaving zero surviving singles,
  exactly as the file claims — but the specific type-identity in the file's
  prose is inaccurate and should be corrected (done in `current.md`).

**Overall verdict: CHANGES REQUESTED** (Status `partial`). NTBT remains open,
no overclaim on the central conjecture; the numeric record is substantively
correct with one small documentation fix needed.

## Lemma certifications this round

Certified (5 new files):
- `lemmas/elementary-omega-bound.md`
- `lemmas/double-witness-nested-pigeonhole.md`
- `lemmas/same-type-triangle-vacuity.md`
- `lemmas/two-sided-singleton-witness-theorem.md`
- `lemmas/monotone-chain-reformulation-lemma.md`

NOT certified: the Generalized Class-Blindness Obstruction (§7 of
`n1-periodicity-reconciliation`) — genuine circularity gap identified above;
kept in the approach file, not promoted, pending a fix (either a concrete
two-instance construction or an honestly-narrower scope).

## current.md

Updated `## Status` (new round-19 paragraph prepended before the round-18
entry) and `## Approaches tried` (4 new bullets prepended) with the full
findings above. Workspace-level Status remains `partial`.

## Ranker

`record_outcome` called for all 4 slugs: `n1-periodicity-reconciliation`
(partial), `triangle-consistency-pigeonhole` (partial),
`core-growth-monotonicity` (dead-end for this round's specific sub-target
attack, though its lemma content is a genuine keep), `self-absorbing-by-
construction` (partial).
