# Outline Review — imo-2026-03, Round 5

Two candidates put up: **direct-constructive** (ADVANCE, skeletons for both open gaps) and
**dyadic-carry-upper** (NEW far framing for the Case-B wall, gated on a kill-switch). I re-ran the
numerics myself before judging.

---

## direct-constructive — ADVANCE  →  CHANGES REQUESTED (build)

Sound spine, both gap skeletons carry a real, numerically-verified mechanism. Build it.

### Verified the outliner's refutation claims (task-required)
- **Opening-1 absolute threshold `b_1 > 2^{q-2}/D` is INSUFFICIENT** — confirmed: 73166/126216
  q=4 feasible configs have `b_1 > 4/D` yet `S − b_1 ≥ 7/D` (halving `b_1` leaves an oversized,
  invalid IH(3) sum). The outliner's replacement by the **relative** threshold
  `S − max(b_1, 2b_2) < (2^{q-1}−1)/D` is the correct engine. Good catch — do NOT let the builder
  regress to the absolute bound.
- **Opening-5 plain Euclidean cascade FAILS** — confirmed: 37456/125931 q=4 configs give cascade
  residual `> 1/D`. The strategy must be adaptive, not a fixed cascade.
- **Adaptive one-step coverage** — confirmed ~94% covered, ~6% flat residual (7458/126155). Matches
  the outliner's honest "~4.5%" open sub-core. The flat two-cut residual and B2 are correctly left
  as EXPLICIT open sub-gaps, not overclaimed.

### GAP (★) LOWER — Descent Lemma: APPROVE as skeleton
- Descent-pair existence (odd-rank positive donor + even-rank receiver at every a=0 interior config
  with A>1) reproduced: **0/41675** failures at n=3. Mechanism is airtight numerically and matches
  explorer Opening A + aimo-0146/0330 analogues.
- Logic is valid: A piecewise-affine on the compact a=0 region; a strict decreasing direction at
  every interior point with A>1 ⟹ no interior local min ⟹ min on the boundary (fragment=0 face →
  fewer-fragment induction; fragment=2^{n-1} face → a=1 cascade, A=1). Case coverage is complete.
- **Build watch-outs (must be written, not hand-waved):**
  1. **Vertex/zero-mass donor branch.** At a genuine vertex some `g_j = 0`; if every odd-ranked
     fragment is zero, the config sits on a fragment-count boundary face — settle it by the
     fewer-fragment induction, NOT by asserting a positive-mass donor. State this branch explicitly.
  2. **The fewer-fragment induction is load-bearing.** "Reduce to lower fragment count, closed by
     the same induction" needs the inductive statement (A ≥ 1 for k ≤ n fragments summing to 2^n,
     all < 2^{n-1}) stated precisely with its base case, not deferred as "then it follows."
  3. Keep ε within the current arrangement cell (no rank crossing) so A is genuinely affine along
     each move; the descent is a sequence of within-cell moves. Do not invoke Lemma S as a global
     min (local only).
- Dyadic-charging (Opening C) is a legitimate independent fallback if the vertex branch stalls; keep
  it documented, build the descent first.

### GAP U1 UPPER — corrected IH(q) adaptive reduction: APPROVE as skeleton
- Mechanism sound (Lemma H pair-cancellation for the halve/cut move; relative sum threshold is the
  fix). Writable now for the ~94% region; flat two-cut residual and B2 correctly flagged partial.
- **Build watch-out:** the adaptive rule reduces to IH(q−1) only when the residual sum fits the
  budget — the builder must verify the reduced instance still has all pieces > 1/D (the two-cut/
  cut-at-b_2 move needs `b_1 − b_2 > 1/D`, which holds since gaps > 1/D). Do not claim IH(q) fully
  closed; mark the flat residual + B2 as open.

---

## dyadic-carry-upper — NEW  →  RETHINK (CUT: not registered, not built)

Killed at the gate. Three independent reasons, any one fatal:

1. **Same move-set as direct-constructive → a rename, not a far framing.** The outliner states the
   framing "ALLOWS fragment cascades (a piece may be cut, then its residual cut again)" — that is
   the identical strategy class direct-constructive's Lemma I / adaptive reduction already uses.
   Lemma X already gives `A = μ(XOR of prefix intervals)`; "binary-carry telescoping" is a different
   analysis *vocabulary* for the SAME quantity and the SAME cuts. Per the run_state rule
   (approaches differing only in technique share one wall), this is too close — it hits the U1 wall
   identically.

2. **Its concrete crux is numerically REFUTED.** The carry lemma's claim — "the residual after
   telescoping distinct dyadic toggles is ≤ the smallest level ≤ 1/D" — is exactly the statement
   that the (dyadic) cascade residual ≤ 1/D. My run: the fixed cascade residual exceeds 1/D on
   **37456/125931** q=4 hard-regime configs (30%). The only repair is adaptive cuts at computed
   non-dyadic values — which is direct-constructive's route. Same wall, one telescope-step later.

3. **The proposed kill-switch is vacuous.** "Min XOR toggle-measure over cuts at dyadic-aligned
   points ≤ 1/D" passes trivially because dyadic points are dense and μ(XOR) is continuous in cut
   position — so dyadic cuts approximate the *general* optimum to arbitrary precision. Passing that
   test proves nothing about the binary-carry *mechanism*; it certifies only that XY *can* win
   (never in dispute), exactly the density-vs-mechanism vacuity the outliner itself flagged. This is
   the round-4 trap in reverse: a kill-switch that cannot fail is not a gate.

Do not register or build. A future distinct Case-B route must change the **move-set or the target**
(not just the analytic vocabulary over the same fragment cascades) and must differ from the whole
graveyard (game-separation, concavity-of-g, amortized-greedy, potential-duality, caseB-matching,
and now dyadic-carry).

---

## Field diversity note (for the orchestrator)

The field has collapsed to ONE live framing (direct-constructive) plus dead/parked rivals. Every
Case-B rival proposed since round 3 has died because the hard regime provably requires fragment
cascades, and any "new" cascade framing is a rename that shares the U1 wall. This is expected and
not alarming *this* round: the two open gaps each now have a concrete, numerically-airtight
mechanism inside direct-constructive, so the win is to CLOSE them, not to open a sixth framing that
will hit the same wall. If direct-constructive's flat-residual/B2 sub-core stalls for another 2+
rounds, THEN the orchestrator should commission a genuinely different *object* (e.g. a
duality/LP-certificate on the achievable-XOR polytope, not another cascade analysis).

## Ranking (updated, stale cleared)
direct-constructive 1623 (live, advancing, closest to solved) > caseB-matching 1529 (dead-end,
salvaged certified lemmas) > potential-duality 1441 (parked, vacuity risk, never built) >
induction-recursion 1406 (dead engine).

build set: direct-constructive
