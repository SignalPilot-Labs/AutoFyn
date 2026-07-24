# Round 8 outline review — imo-2026-03

## Context verified before review
- Re-read `results/imo-2026-03/current.md` and the two round-8 explorer reports
  (`math-explorer-dagger-attack.md`, `math-explorer-alt-induction.md`). Both
  independently confirm (†) (Branch B, N even, of `rank-pigeonhole-budget`'s
  peel-the-global-minimum induction) is an **exact algebraic identity with the
  target itself**, not a smaller sub-claim — the alt-induction explorer proved
  this directly by substitution, and separately showed "peel two elements"
  reproduces the same wall one level down. Both explorers independently confirm
  `lp-duality-certificate`'s bounded/context-free atom vocabulary is
  structurally incapable of covering the tight $c_1=2$ witness
  ($n=3$, $F=\{4,2,2\}/15$, exact equality) without smuggling in $A(G')$'s exact
  recursive value — i.e. any fix is the induction in disguise. I independently
  re-ran a 15k-trial exact-`Fraction` search of the abstract Case-I target
  $E(F\cup\tau)\le R(\tau)$ (own script, not reused from either explorer) and
  found **zero violations**, minimum slack $10873/5000000>0$ — consistent with
  (†) being true, so the population is chasing a real theorem, not a phantom.
- Cross-checked the citation to `lp-duality-certificate.md` §6/§7.4 (Type
  III/IV atoms, the floor-vs-exact diagnosis) — matches the outline's
  restatement exactly.
- All four slugs the outline touches (`rank-pigeonhole-budget`,
  `rank-tie-vertex-reduction`, `greedy-halving-adversary`,
  `lp-duality-certificate`) are already-registered population members; no new
  registration needed. No copy requested this round.

## Per-approach verdicts

### rank-pigeonhole-budget — revise — **APPROVE**
Target: close Claim (A) Case I in full (subsumes (†)) via exchange-smoothing
maximization of $E(F\cup\tau)$ over the simplex of legal $F$, reusing
`vertex-minimum-theorem` (min→max direction) and an aimo-0146 exchange-
smoothing transplant.
- Technique is sound and *genuinely different* from the peel-induction that
  both explorers proved circular: it never removes a single element and asks
  about resulting rank parity, so it structurally sidesteps the diagnosed
  disease. The "$E$ is linear within a fixed order-type region" claim is
  correct (rank-position weight is a 0/1 indicator, locally constant as long
  as relative order is unchanged) — I re-derived this by hand, it holds.
- The "reuse, not re-derive" claim about `vertex-minimum-theorem` applying to
  the max direction is correct: the underlying fact (affine functional on a
  compact polytope attains extrema only at vertices) has no min-specific
  step. The outline explicitly flags this to be *verified*, not assumed, by
  the builder — good, keep that instruction.
- Genuine open gap, correctly flagged (not hidden): whether the
  exchange-smoothing terminal set exactly coincides with the LP-vertex set
  (standard, but must be stated precisely) and full enumeration for general
  $m$. Also flagged: must correctly encode the $k\le m+1$ budget as a
  polytope facet (round 6 already showed the unrestricted version is false) —
  good, this is exactly the trap both explorers separately warned about
  (accidentally dropping this constraint produces spurious counterexamples).
- Structural encouragement: the certified achievability construction $F^*$
  (pairs-cancel-plus-leftover-triple) is exactly the "plateau" shape
  exchange-smoothing predicts — a real consistency check, not decoration.
No fixable gaps beyond what's already flagged; approve as scoped.

### rank-tie-vertex-reduction — revise — **APPROVE (exploratory)**
Target: general $c_1\ge2$, via strong induction on $\ell(S):=|S'|$ (odd-run-
reduced size) instead of raw $N$.
- This is honestly the most speculative of the four — the outline itself
  states the inductive step (5) is "new content, not yet derived by anyone"
  and instructs the builder to attempt small cases *first* and report a clean
  negative result if it reproduces the same trap, rather than force a partial
  proof. That is the correct discipline given the population's track record
  (three independent "exact identity, not a reduction" diagnoses already on
  file under different names).
- Mechanism is genuinely distinct: peeling by reduced-size can drop $\ell$ by
  0 or 2 per removed element (not always 1), decoupling parity from raw
  count — a real structural difference from the diagnosed obstruction, not
  cosmetic. Worth a scoped attempt.
- Risk correctly flagged: may hit a symmetric wall one level down; the
  outline explicitly requires this be recorded as a genuine third
  confirmation if found, not silently reframed. Approve with that guardrail
  intact.

### greedy-halving-adversary — advance — **APPROVE**
Target: the correctly-*restricted* Claim (B) — refining tail cuts on top of
however Xiang Yu splits $p_1$ never pushes $A$ below Claim (A)'s value $a_n$,
restricted to $F$ at/near Claim (A)'s optimum (NOT the unrestricted form,
which round 5 refuted with an exact counterexample, $n=2$, $F=\{p_1\}$,
splitting $p_3$: $3/7\to12/35$).
- Correctly distinguishes itself from the refuted general claim; the "Watch
  out for" section explicitly reminds the builder not to re-drift into the
  unrestricted form — good, since this is exactly the kind of mistake this
  project's memory records (a prior round on a different slug re-proposed a
  refuted shortcut under a new name).
- The safe-window structural lemma (ladder ratio-2 spacing bounds where
  Lemma 14's perturbation windows can land) is a real, checkable geometric
  fact, not hand-waved — $p_i>\sum_{j>i}p_j$ for a ratio-2 superincreasing
  sequence is elementary and correctly cited.
- Two explicitly-open, non-trivial gaps (the safe-window lemma itself; the
  ordering-independence of chained perturbations, explicitly flagged as
  *not* automatic) — honestly scoped as unconstructed, with a stated fallback
  (an explicit worst-case order) if commutativity fails. No overclaiming.

### lp-duality-certificate — revise (reframed target) — **APPROVE**
Redirect from the confirmed-dead-end Case-I lower-bound patching to the
general upper bound $c(n)\le a_n$ for arbitrary Liu Bang markings (only
closed for $n\le2$ so far).
- This is a legitimate pivot, not a same-mechanism retry: both explorers
  independently produced a *structural* no-go (not merely "not found yet")
  for extending Type III/IV to $c_1\ge2$ — the tight witness forces any valid
  certificate to be exactly tight, which requires the exact recursive value
  of $A(G')$, i.e. is the induction in disguise. The outline correctly stops
  asking this approach to patch that basis and moves it to a genuinely
  separate half of the theorem (upper bound vs. lower bound) where its LP/
  certificate machinery previously produced a real result ($n=2$, six
  templates).
- Appropriately scoped as exploratory ("only $n\le2$ fully closed, one ad hoc
  $n=3$ witness on file... an honest partial result is acceptable progress").
  Step 5 sensibly requires the general strategy to reduce to or dominate the
  known $n=3$ trisection witness as a sanity check before generalizing
  further — good discipline against a strategy family that looks right in
  the abstract but fails the one concrete case already on file.

## Diversity / shared-gap assessment
Three of the four (`rank-pigeonhole-budget`, `rank-tie-vertex-reduction`,
`greedy-halving-adversary`) still orbit the general lower bound's remaining
piece(s) (Case I / (†), $c_1\ge2$, and Claim B respectively), but via three
*mechanistically* distinct techniques (LP-vertex exchange-smoothing on a
direct maximization; induction on a different, structurally motivated
variable; perturbation-identity chaining under a ladder-specific geometric
bound) — consistent with this project's own established practice (memory
rule from round 1: shared *target*, genuinely different *mechanism*, is
acceptable diversity, especially once independent framings have already
converged on the same obstruction from 4+ directions, as documented in
rounds 2–7). `lp-duality-certificate`'s pivot to the upper bound is the
genuinely orthogonal fourth leg this round, correctly motivated by an actual
structural no-go rather than fatigue. I see no fatal collapse-to-one-
framing risk here; flagging for the record so next round's outliner keeps
watching it if all three lower-bound mechanisms stall again.

## Ranking
Registered field unchanged (no new slugs this round). Ranked head-to-head via
`update_ranking`, anchoring newer/stale entries to established dead-ends and
live siblings, and clearing `stale` on all touched approaches
(`rank-pigeonhole-budget`, `rank-tie-vertex-reduction`, `lp-duality-
certificate`, `bijective-mersenne-pairing`, `integer-lattice-reduction`).
Post-update order (best-first): `greedy-halving-adversary` (1634) >
`rank-tie-vertex-reduction` (1605) > `rank-pigeonhole-budget` (1587) >
`lp-duality-certificate` (1564) ≈ `smoothing-compactness-certificate` (1562)
> `bijective-mersenne-pairing` (1477, dead-end) > `dyadic-band-occupancy`
(1441) > `exchange-argument-extremal-response` (1436) >
`self-similar-potential-certificate` (1434) > `integer-lattice-reduction`
(1429, dead-end) > `self-similar-bracketing` (1410) > `claiming-order-
invariant` (1396, dead-end).

## Build set
All four outlined approaches are sound, correctly scoped, honestly flag their
open gaps with a stated mechanism (not a bare label), and target genuinely
different pieces/techniques. No RETHINK, no CHANGES REQUESTED — approve all
four for build this round.

build set: rank-pigeonhole-budget, rank-tie-vertex-reduction, greedy-halving-adversary, lp-duality-certificate
