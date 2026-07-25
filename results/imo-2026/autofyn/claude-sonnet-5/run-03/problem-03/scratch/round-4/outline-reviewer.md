# Outline review — round 4 — imo-2026-03

Reviewed `/tmp/round-4/proof-outliner.md` against `results/imo-2026-03/current.md`,
all `approaches/*.md`, all `lemmas/*.md`, `knowledge_base.md`, and CLAUDE.md's
rigor rules. Spot-checked the load-bearing new claims numerically in Python
(shown below). All five approaches — four revisions + one new — are sound
enough to build; none is a fatal restatement of a killed mechanism.

## self-similar-induction-on-n — CHANGES REQUESTED (approved to build)

Target: `T(m)` for `m≥3` (lower bound, general case), retargeting the `j≥2`
inductive step away from the peel+scalar mechanism Proposition C proved
circular, toward a global AltSum-budget argument.

- The `AltSum` reformulation (`OddSum=(sum+AltSum)/2`) is genuinely
  elementary — a 2x2 linear solve of `Odd+Even=sum`, `Odd-Even=AltSum` — no
  issue.
- Correctly does **not** resurrect Proposition C: the outline explicitly
  flags that the new "local change formula" must track the full signed
  window, not collapse to a scalar, which is exactly the collapse that made
  the old mechanism circular. Good self-awareness, keep the builder honest
  to this constraint.
- The genuinely open step (Aggregate budget bound: summed `|ΔAltSum|` over
  `≤m` cuts `<` slack) is honestly flagged as unproved and is the real
  content — no hand-wave, no bare "then it follows."
- Watch: "Local AltSum-change formula" is claimed elementary but unproved;
  builder should nail this down first as a lemma with the stated mechanism
  (insertion re-signs only the affected window) before attempting the
  aggregate bound, since an error here would silently corrupt the aggregate
  step.

## greedy-reduction-geometric — CHANGES REQUESTED (approved to build)

Target: TOP-ONLY outside Dominant-Chain + general Case 2, scoped down to a
large-violation-depth `d` sub-case using EvenSum-superadditivity.

- Verified the claimed dual algebraically: Lemma S (certified) gives
  `OddSum(A∪B)≤OddSum(A)+OddSum(B)`; since `Odd+Even=sum` on both sides,
  subtracting gives `EvenSum(A∪B)≥EvenSum(A)+EvenSum(B)` immediately — the
  "new import" is a correct one-line consequence of an already-certified
  lemma, not a fresh unverified claim.
- Honestly scopes to "large `d` relative to `j`" and explicitly commits to
  documenting where the residual step fails outside that sub-case, rather
  than overclaiming full generality — meets the "prove, don't conjecture"
  rule.
- Watch (flagged in outline itself, and I concur): the builder must not
  quietly fall back to "peel again + single scalar bound" for the residual
  outside the covered sub-case — that is Proposition C's exact mechanism.
  Reviewer should check this at build time.

## universal-halving-adversary — CHANGES REQUESTED (approved to build)

Target: the single remaining upper-bound region (`p1<1/2`,
`p_{n+1}>1/(2^{n+1}-1)`) via a Suffix-Match Insertion Lemma generalizing the
certified Theorem 4 (General Insertion Lemma) to partial duplication.

- The mechanism (partial duplication of the bottom `t` values of `R`,
  parity/block-counting argument) is a plausible direct generalization of an
  already-certified, already-numerically-verified identity (Theorem 4) — not
  a new unrelated technique, so the risk is contained.
- Case coverage for the new lemma (`t=0`, `t=|R|`, interior) is explicitly
  listed and both boundary cases are checked against existing results
  (`t=0` should degenerate to bisection, `t=|R|` should reduce to Theorem
  2/4) — good practice, catches a broken formula early.
- The "top-only optimality restricted to the balanced region" is correctly
  imported as an unproved working hypothesis, not as a citable fact, with an
  explicit note that it still needs `dyadic-potential-invariant` to prove it
  — correctly avoids a silent cross-slug dependency violation.

## dyadic-potential-invariant — CHANGES REQUESTED (approved to build)

Target: rescoped Restricted Exchange Lemma, balanced region only, replacing
the killed literal (unrestricted) Cut-Reallocation Exchange Lemma.

- Correctly narrower domain (balanced region has no dominant top piece),
  distinct from the counterexample structure that killed the literal lemma
  (round 3's counterexample exploited a dominance gap between `8` and `4`) —
  this is a genuinely different claim, not a resurrection.
- Outline explicitly mandates the numeric stress test as the *first* builder
  task, before any proof attempt — follows the standing rule (round 3's
  burn: an abstract dual/exchange claim must be tested before being built
  on). Good.
- Low cost, high value: if the numeric test fails, the builder documents a
  second dead end cheaply; if it passes, this closes real remaining upper-
  bound ground. Worth including in the build set despite being the lowest
  current Elo / weakest track record.

## layer-cake-parity-reframing — APPROVE, register (new)

Target: `T(n)` for all `n` via a genuinely different top-level framing
(threshold/layer-cake decomposition, per-piece additive) that does not peel
a max element at all — directly answers CLAUDE.md's plateau-break
requirement, since the two peel-based approaches have hit the same
Proposition-C-shaped wall for 2 straight rounds.

- I independently re-verified the claimed Layer-cake identity
  `OddSum-EvenSum = ∫ 1[N(t) odd] dt` numerically (5 random multisets, sizes
  2-5, values in (0,5), fine discretization): matched to the discretization
  error in every case (e.g. `1.55123` vs `1.55126`; `2.10456` vs `2.10457`).
  The identity is correct and elementary as claimed (swap sum/integral,
  telescoping alternating-sign coefficient argument) — safe for the builder
  to formalize as step 1.
- Per-piece additivity (step 2) is a direct consequence of "a fragment of
  `p_i` can never exceed `p_i`" — correct and does structurally sidestep
  Proposition C's top-piece-vs-rest asymmetry, since every piece is treated
  identically in this framing. This is the real diversity-of-thought value:
  it is not a variant of peel+scalar, it is additive over pieces/thresholds.
  Genuinely distinct from all four other approaches' mechanisms.
- Steps 4-5 (budget-to-measure bound) are honestly flagged as entirely
  unstarted and are where the real difficulty must reappear — no hand-wave,
  correctly identified as the hard step.
- Outline mandates a numeric sanity check (does the reformulated
  optimization reproduce `c(n)` at small `n`) before further investment —
  correctly wary that the parity-reduction (step 3) could silently discard
  information XY needs; flagged explicitly as a thing to verify, not assume.
- This is a whole attempt at the lower-bound half of the problem (same
  scope convention the population has used since round 1 — lower-bound-only
  and upper-bound-only slugs importing the other side's certified result via
  the shared lemma cache), not a slice of a sibling's proof. No single-gap-
  trap concern.

## Diversity check

Population now spans three genuinely distinct mechanism families for the
lower bound: (a) peel+aggregate-signed-budget (self-similar-induction-on-n),
(b) exact-identity decomposition + superadditivity on a scoped sub-case
(greedy-reduction-geometric), (c) per-piece additive layer-cake, no peeling
at all (layer-cake-parity-reframing) — a real break from the 2-round plateau,
not just a relabeling. The upper-bound side has two mechanisms (exact-
identity generalization in universal-halving-adversary; exchange/majorization
in dyadic-potential-invariant), also distinct. No approach repeats a
recorded dead end (static Q-priority, static tail-priority, literal
Cut-Reallocation Exchange, Lemma X') — checked each outline's skeleton by
name.

## Dead ends avoided

Confirmed none of the five outlines invoke: Lemma X' (killed round 3), the
literal unrestricted Cut-Reallocation Exchange Lemma (killed round 3), the
static Q-priority or tail-priority claiming strategies (killed rounds 2-3),
or Proposition C's peel+scalar mechanism under a new name (self-similar and
greedy-reduction-geometric both explicitly guard against this in their own
"Watch out for" sections, and their skeletons match the guard).

## Ranking

Registered `layer-cake-parity-reframing` (cold start). Ran `update_ranking`
anchoring the new approach against established siblings (not just against
itself), consistent with dead-end/advanced signal from `current.md`:
`universal-halving-adversary` beats every other live approach (most
certified content, closest to closing its remaining region, conditional
Theorem 5 already in hand); the two peel-family approaches
(`self-similar-induction-on-n`, `greedy-reduction-geometric`) draw each
other (same wall, symmetric progress this round); `layer-cake-parity-
reframing` draws both of them (fresh but independently verified identity,
directly targets their shared wall from outside it) and loses only to the
leader; `dyadic-potential-invariant` loses every comparison (still the sole
`dead-end` last outcome, weakest track record), which is expected and does
not exclude it from this round's build set given its new work is a cheap,
well-scoped numeric test.

Resulting order (best first): `universal-halving-adversary` (1610.5),
`greedy-reduction-geometric` (1529.5), `self-similar-induction-on-n`
(1515.9), `layer-cake-parity-reframing` (1497.1), `dyadic-potential-
invariant` (1346.9).

## Build set

All five have concrete, checkable, non-doomed content this round — the
population is at a genuine plateau-break point (new framing verified,
existing approaches scoped past their prior circular wall) and each
builder's task is cheap to falsify if wrong (numeric tests mandated first
for the riskiest claims: dyadic-potential-invariant's Restricted Exchange
Lemma, layer-cake-parity-reframing's step-3 equivalence check). Build all
five in parallel, one builder per slug.

build set: universal-halving-adversary, greedy-reduction-geometric, self-similar-induction-on-n, layer-cake-parity-reframing, dyadic-potential-invariant
