# proof-outliner report — round 21, imo-2026-03

## Inputs read

- `results/imo-2026-03/current.md` (Status: `partial`, round-20 verdicts on
  both live approaches: CHANGES REQUESTED on each).
- `results/imo-2026-03/approaches/self-similar-induction-on-n.md` (6036
  lines pre-edit; General Cardinality-Constrained Half-Sum Lemma is the
  open target, general $k$, verified $k=2$ + numerics $k=3,4,5$).
- `results/imo-2026-03/approaches/global-lp-vertex-sufficiency.md` (4052
  lines pre-edit; $n=2$ Existence Theorem fully closed both directions
  round 20; $n=3$ open, two natural 2-cut pairings refuted).
- `/tmp/round-21/math-explorer-canonical-form.md` — scouted (not proved) a
  pigeonhole+pairing route for the general-$k$ GCH lower bound: reduces
  the open claim to three steps (pigeonhole: every feasible canonical
  form has ≥1 active item; pairing: any nonempty active-Γ-subset
  alternating sum is ≥1 automatically; and the one genuinely open case,
  a single active free value interleaved among the Γ-levels — same shape
  as the already-solved $k=2$ case). Exhaustive (not sampled) exact-
  `Fraction` search $k=2,\dots,8$ found zero counterexamples and an exact
  tight family throughout $S\in[2^k,2^k+1)$.
- `/tmp/round-21/math-explorer-n3-casesplit.md` — tested 6 new $n=3$
  single-mechanism constructions (double-cascade, shift-down, skip-$p_2$,
  skip-$p_3$, cascade, full-cascade, trisection) against dense/exhaustive
  region scans; all fail somewhere; even a per-point best-of-eight oracle
  (including the 2 round-20 constructions) leaves a strict positive
  residual excess, exactly $1/15$, at the explicit corner
  $p^\dagger=(6/15,5/15,4/15,0)$, $g_1=g_2=\gamma_3=1/15$. Flags an
  untested idea: use $n=3$'s spare third cut to touch $p_4$ itself near
  this corner, as part of a genuine two-region case-split (not another
  global construction).
- `/tmp/round-21/math-explorer-plateau-check.md` — verdict: **no dead
  plateau**; both approaches have distinct, real, converging next steps
  (not repeatedly hitting the same wall). No orchestrator/reviewer flag
  of "field collapsed to one framing" in rounds 16–20. If a 3rd slot is
  wanted as a hedge, recommends (B) an explicit LP-duality dual-
  certificate route for `lp-duality-split-polytope` (never literally
  attempted in 13 rounds — all past work there was primal constructions
  plus a shadow-price heuristic) over (A) a fooling-set/double-counting
  transplant, but does **not** recommend opening it this round absent a
  real plateau.

## Decisions this round

**No new approach opened.** Per CLAUDE.md ("do not open a new approach
unless truly justified") and the plateau-check explorer's explicit
finding of no shared-wall plateau — both live approaches have distinct,
concrete, certified-progress-bearing next steps this round, not vague
casting-about. Reserving the LP-duality-certificate idea (option B) as
the flagged fallback if either live approach stalls for 2+ more rounds
without progress on its newly sharpened target below.

**Both live approaches revised in place** with concrete, sharpened
outline steps (edited directly into their approach files, "Round 21
target" sections appended):

### 1. `self-similar-induction-on-n` — canonical-form pigeonhole+pairing route

Added a 3-step outline (Step A pigeonhole: every feasible canonical-form
$R''$ has $\ge1$ active item, argued rigorously including non-integer
$S$, not just the explorer's integer-$S$ sketch; Step B pairing: any
nonempty active-Γ-subset alternating sum is $\ge1$ via adjacent-pair
telescoping, stated as a clean sub-lemma — candidate name **Active-Γ-
Subset Alternating Sum Lemma**; Step C, the genuinely open case, single
active free value interleaved among active Γ-levels — either a
domination/exchange generalization of the certified **General Pairwise
Reduction Lemma**, or direct casework generalizing the fully-closed
$k=2$ instance). Explicitly flagged: Step C is NOT to be assumed closed
by the numerics — the explorer's finding that Step B's bound always
dominates it is a numeric pattern, not a proof. This supersedes, if it
closes, the round-18 "needs a two-parameter family" diagnosis, since it's
a direct counting argument rather than induction on $k$.

### 2. `global-lp-vertex-sufficiency` — two-region case-split for $n=3$

Added a concrete two-region outline: **Region I** (near-degenerate corner
where $p_4\to0$, both top gaps at floor $\gamma_3$) handled by a new
3-cut construction that uses the spare third cut to split/tie $p_4$
itself to $g_1$ or $g_3$ (the explorer's flagged, untested idea) — must
verify exactly at $p^\dagger=(6/15,5/15,4/15,0)$ and throughout a real
neighborhood, not just the point. **Region II** (interior) handled by
construction C (double-cascade, best performer, argmin at $\approx80\%$
of sampled points) or the $p_2,p_3$-tied pairing A on its own feasible
sub-region. Mandatory boundary-matching requirement stated explicitly: an
exact inequality defining the region split, checked to jointly cover all
of $B(3)$ with no gap, and Region I's construction checked against the
whole region, not just the corner. Explicitly listed all 8 refuted
single-mechanism constructions (A, B, C, D, E, F, G, K, trisection) as
not to be re-tried as standalone universal answers — only C and A remain
usable as the Region II piece.

## Approach state (no other approaches touched this round)

Dormant/dead, not revised: `discharging-neighbor-transfer` (retired,
round 16), `dyadic-potential-invariant` (dead, majorization counterexample
round 6), `greedy-reduction-geometric`, `layer-cake-parity-reframing`,
`lp-duality-split-polytope` (dormant since round 18, flagged fallback
only), `reciprocal-potential-induction-on-n` (dead, round 16),
`structured-randomization-upper-bound` (dead, round 12),
`universal-halving-adversary`.

## Field for the outline-reviewer

Two live approaches, each with a freshly sharpened, concrete next-step
outline (no vague casework, no re-hash of refuted constructions):

build set: self-similar-induction-on-n, global-lp-vertex-sufficiency
