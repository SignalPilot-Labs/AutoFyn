# Outline review — imo-2026-03 (round 4)

Context: whole problem is ONE gap from solved. UB `c(n) ≤ 2^n/D_n` fully certified. LB reduces to
**(LBL): for `W_n={2^0,…,2^n}` every ≤n-cut refinement has `f≥1`**, closed except the
non-degenerate rank-tied minimizer. Both candidate approaches attack that sole residual, from
opposite sides. I verified the two load-bearing facts computationally before judging:
- **Lemma BD (block-decomposition `= σ_a·f_block`) is exactly true** — `σ_{a+j-1}=σ_a(-1)^{j-1}`
  factors the sign out of a rank-contiguous band; confirmed numerically (direct block contribution
  `-4` = `σ_a·f_block`). One-line identity, sound.
- **The illustrative residual `{4/3,4/3,4/3,2,1}` (f=5/3) is NOT a minimizer** — it slides flat
  (5/3 on eps∈[0,1/3]) then strictly down to the exact floor f=1 at eps=2/3, verified in exact
  rational arithmetic. So the residual is a proof-writing gap (the tied vertex retracts onto
  already-closed cases), not a math obstruction. `min f = 1` reconfirmed for n=2,3.

Both approaches are **whole attempts** (each targets `c(n)` end-to-end, importing the certified UB
and closing the full LB), not one proof split across two slugs. Both correctly AVOID the flagged
trap: neither finishes the cross-tie by monochromaticity (they know non-monochromatic integer-f=1
minimizers exist), so neither commits the recorded error.

---

## self-similar-recursion — CHANGES REQUESTED (primary build; advance)

Right technique, mechanism-grounded. Steps 1–3 are largely in hand: minimizer via Weierstrass;
degenerate leg (cut-count induction) and tie-free leg (certified Lemma J) already closed; within-
piece ties killed by BD → simplex-vertex descent (explorers verified the symmetric split is a
saddle, exact `5/3−8δ` strict descent). The crux is **Step 4 (cross-piece ties)**, and it has two
genuinely open, correctly-flagged sub-gaps — build to close them:

- **(i) Lemma I′ (non-adjacent / chain slide).** Certified Lemma I covers only *adjacent* sub-piece
  slides. Step 4 needs a coordinated slide against a within-piece partner that may not be adjacent
  on the stick. This must be proved (the 1-parameter restriction of `f` is piecewise-affine with a
  telescoping slope) — do NOT invoke Lemma I on non-adjacent slides, it does not apply.
- **(ii) Cross-tie termination monovariant.** This is the load-bearing hole. A flat slide can FORM
  a new cross-tie (the residual example does exactly this at eps=1/3), so tie-count is not a naive
  monovariant. Per the standing role rule: a chamber descent that "terminates at a nice minimizer"
  hides its work in cross-tie constant-value walks — a bare "iterate, finitely many chambers" is
  NOT termination. Demand an explicit no-cycle / strict-drop-per-visit argument (finite chambers +
  `f` non-increasing + a lexicographic tie-multiplicity decrease that cannot cycle through flat
  moves). This is the real remaining content of the whole problem.
- **(iii)** Confirm the even-block strict-descent sign is uniform across block size `k` and rank
  parity — explorers checked only `k=3`; check `k=2,4,5` symbolically (cheap, do it in-build).

The even/odd tie-block dichotomy (σ_a−σ_b = 0 odd / ±2 even) and the "every cross-tie touches ≥1
cut piece" sub-claim (free from distinctness of `2^k`) are sound and give the needed internal
freedom. Skeleton is valid; the two open lemmas are correctly scoped, not hidden.

## block-recursion-tievertex — CHANGES REQUESTED (register + build as de-risking hedge)

New, registered at Elo 1500. Same reduction, same certified imports, same Lemma BD, same within-
piece handling as self-similar — that shared prefix is fine. It earns its place ONLY at the crux,
where it must stay genuinely distinct from self-similar's slide route. Two issues:

- **Its Step 4 is internally muddled and risks collapsing into self-similar.** The skeleton claims
  an *integer bottom-out* (fully-retracted cross-tie block-vertices are integer ⇒ Theorem F), but
  its own "Key lemmas" list then falls back on the SAME even/odd slide dichotomy + Lemma I′ +
  monovariant as self-similar. If it uses the slide route it is redundant. **Instruction: commit
  Step 4 to the integrality route** (LP-vertex reduction: a non-degenerate vertex pinned purely by
  cross-piece ties `x_i=x_j` and uncut equalities `x=2^k` is a rational vertex; show it is
  *integer*, then Theorem F closes it). This genuinely avoids the termination monovariant that is
  self-similar's wall — a real hedge (two different walls: integrality-proof vs no-cycle-proof).
- **The integrality claim currently has NO mechanism — a bare numeric conjecture (n=2,3).** "cross-
  tie block-vertices are integer in general" is stated without a reason it is true; per the
  lemma-mechanism rule this is an unverified hand-off. The builder must supply the mechanism (why
  the integer-coefficient tie/uncut linear system forces an integer, not merely rational, solution
  — {4/3,…} shows *within*-piece ties give non-integer vertices, so the argument must use that the
  vertex is purely cross-tie with no within-piece tie). If no mechanism is found, this route is
  doomed and the approach reduces to a redundant copy of self-similar — acceptable outcome for a
  hedge, but the builder should report that verdict rather than silently borrow the slide argument.

Verdict rationale: both belong in the build set. They share the reduction/BD prefix (proven) and
diverge exactly at the sole crux, from opposite directions (monotone slide-to-terminal vs
integrality-of-vertex). That is a legitimate de-risking hedge on a plateau that has sat on one
framing for 3 rounds — a wall on one route (termination monovariant) is sidestepped by the other
(integrality), and vice versa. block-recursion is NOT redundant *provided* it commits to the
integrality route as instructed; if it silently reuses self-similar's slide, it is.

## Field diversity note (for the orchestrator)

The field is still narrow: every live approach shares the layer-cake reduction and Lemma BD, and
both build targets bottom out on the SAME cross-piece-tie step, reached from two sides. This is an
acceptable hedge for a one-gap-from-solved problem, but if BOTH stall on the cross-tie again next
round, the two open levers to try are genuinely different: (a) a variational/tangent-cone KKT
finish (perturbation explorer, opening 3) making "no feasible descent direction ⇒ closed case"
fully rigorous, and (b) a genericity/perturbation argument that purely-cross coincidental ties are
non-generic. Both are noted here so next round's outliner can seed one if the crux holds.

## Ranking (updated, stale flags cleared on self-similar & alternating-sum)

1. self-similar-recursion — 1625.7 (lead; advanced; closest to whole-problem solve, crux mechanism-grounded)
2. alternating-sum-threshold-potential — 1569.8 (verified-milestone: UB certified; LB imported, not built this round)
3. block-recursion-tievertex — 1501.1 (new; hedge on the crux, integrality route pending a mechanism)
4. game-value-recursion — 1448.4 (dormant; no gap closed 2 rounds)
5. majorization-smoothing — 1355.0 (dormant; one-shot certificate provably fails)

build set: self-similar-recursion, block-recursion-tievertex
