# Outline-reviewer report — round 4, IMO-2026-03

## What I did

Read `current.md`, all seven existing approach files
(`greedy-halving-adversary`, `smoothing-compactness-certificate`,
`self-similar-bracketing`, `rank-tie-vertex-reduction`,
`exchange-argument-extremal-response`, `self-similar-potential-certificate`,
`induction-first-move-reduction`), the ranking sidecar, and the round-4
outline (`/tmp/round-4/proof-outliner.md`) plus both round-4 explorer
reports.

## Numeric spot-check (as instructed, before trusting any new
numerically-checkable claim)

Verified with exact `Fraction` arithmetic (no floating point), $n=1..6$,
using the ladder $p_i = 2^{n+1-i}/(2^{n+1}-1)$:

- **`p_i = 2p_{i+1}` and `p_i - sum_{j>i} p_j` = constant across `i` (for
  fixed `n`).** Both confirmed true exactly — the algebraic engine behind
  `rank-pigeonhole-budget`'s Step 1 restatement and the cascading-halving
  family is sound. No problem found here.
- **The outliner's claimed generalization for `rank-tie-vertex-reduction`'s
  next step — "for every `k ∈ {0,...,n}`, the prefix cascading-halving
  composition attains `A = f(n)` exactly" — is FALSE.** Direct computation
  (building the cascaded multiset and computing the odd-rank sum exactly)
  shows this only holds for the top two prefix lengths, `k = n-1, n`; every
  shorter prefix (`k ≤ n-2`) gives a strictly larger `A`, e.g. at `n=5`,
  `k=0,1,2,3` all fail (values `2/3, 4/7, 34/63, 11/21` vs target `32/63`),
  only `k=4,5` match. This traces to the outliner over-generalizing the
  round-4 explorer's own (accurate, narrower) claim — the explorer only
  ever tested `k` values at or near the top of the range and never asserted
  the full range works. **This is exactly the kind of catch flagged by
  round 2's broken-telescoping-recursion precedent.** I corrected this
  in-file (`rank-tie-vertex-reduction.md`, new "Outline-reviewer correction"
  section) with the true, narrower claim and a concrete next step (induct
  top-down on `n-k` over just the two working prefix lengths, then separately
  investigate why shorter prefixes stop being optimal at all — likely because
  a different, non-cascading vertex takes over). The builder on this slug
  should follow the corrected version, not the outliner's original
  "every k" instruction.
- `rank-pigeonhole-budget`'s own skeleton makes no other numerically-testable
  claim yet (Step 2's pigeonhole lemma is stated qualitatively, not as a
  concrete formula) — nothing to falsify there before build; flagged this
  in the seeded approach file for the builder's own awareness.
- `claiming-order-invariant`'s candidate invariant (Step 2) is explicitly a
  first guess, not yet checked even against the on-file `n=3` example — no
  numeric claim to verify yet; the outline itself assigns the first builder
  task as exactly this cheap check.

## Retirement call: `self-similar-bracketing`

**Confirmed.** Round 3's Proposition B2 rigorously refutes this approach's
load-bearing premise (that `c=n` minimality is a free/easy endpoint); no fix
was found by either round-4 explorer, and inventing one would require
solving the same obstruction `rank-pigeonhole-budget` now targets directly.
Lemma B1 (exact achievability at `c=n`) remains correct and stays certified
(`rescaled-ladder-c-equals-n-achievability`), so nothing proved is lost.
Excluded from the build set; kept on record (not deleted), ranked below the
live field to reflect the refuted framing.

## Registrations

- **`rank-pigeonhole-budget`** (new, `register_approach`): discrete
  majorization/pigeonhole recast of Prop. 10's cross-term inequality
  (`aimo-0718`-style), targeting the exact located gap from a genuinely
  different toolbox than the four framings already stuck on it. Approach
  file seeded at `approaches/rank-pigeonhole-budget.md`.
- **`claiming-order-invariant`** (branch of `self-similar-potential-certificate`,
  `copy_approach`): retargets that approach's certificate philosophy at
  claiming *order* rather than final-multiset structure
  (`aimo-0117`-style), inheriting its Elo/history as a peer. Lower
  confidence than slug 1 per the explorer's own ranking; kept for framing
  diversity. Approach file seeded at `approaches/claiming-order-invariant.md`.
  `self-similar-potential-certificate` itself is left untouched and stays
  registered (its certified lemmas — scaling identity, above-threshold
  formula, budget monotonicity, the negative mass-bound-insufficiency
  result — remain valid and reusable) but is not in this round's build set.

## Ranking (head-to-head, posted via `update_ranking`)

Best-first after this round's comparisons:

1. `greedy-halving-adversary` — 1576.7 (top; most concrete two-pronged next
   step: identity-specific substitution attempt, then fallback to importing
   `rank-pigeonhole-budget`)
2. `smoothing-compactness-certificate` — 1563.8 (strongest fully-certified
   milestone, `c(2)=4/7` both directions non-numeric; concrete general-`n`
   template-generalization next step using the corrected cascading family)
3. `rank-tie-vertex-reduction` — 1543.8 (two fully certified general
   theorems this round; corrected, narrower next step in hand)
4. `rank-pigeonhole-budget` — 1529.6 (new; highest-promise new framing,
   unbuilt, targets the exact plateau gap from a different toolbox)
5. `exchange-argument-extremal-response` — 1481.9 (live; SDR/Hall's-theorem
   idea assigned as next step, cheap Hall's-condition test against the
   on-file `n=3` example)
6. `self-similar-bracketing` — 1462.0 (**retired from build set**, premise
   refuted, no fix found)
7. `claiming-order-invariant` — 1461.3 (new branch; speculative,
   lowest-confidence per explorer's own ranking, kept for diversity)

(`self-similar-potential-certificate` and `integer-lattice-reduction` remain
registered but untouched this round, not part of the build set.)

## Build set

Five slugs: the strongest live approach on each of the two established
framings (`greedy-halving-adversary`, `smoothing-compactness-certificate`),
the two LP-vertex-family approaches with fresh certified theorems/corrected
next steps (`rank-tie-vertex-reduction`, and — for diversity budget — not
`exchange-argument-extremal-response` this round, deferred to next round
since its SDR idea is a cheap/fast test better run once pigeonhole's
results are in), the new headline far-framing entry
(`rank-pigeonhole-budget`), and one diversity pick from the second new
entry (`claiming-order-invariant`) per the shared-gap-plateau rule.

build set: rank-pigeonhole-budget, rank-tie-vertex-reduction, greedy-halving-adversary, smoothing-compactness-certificate, claiming-order-invariant
