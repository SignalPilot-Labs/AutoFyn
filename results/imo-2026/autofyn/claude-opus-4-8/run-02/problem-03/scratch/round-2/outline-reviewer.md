# Outline review — imo-2026-03 (IMO 2026 P3), round 2

Two open cruxes for the whole field: GAP-L (LB, Case 2) and GAP-U (UB, all n). Shared
certified base (Lemma 0 endgame-greedy, layer-cake `f=M`, matching form, P1–P4) is sound and
reused correctly by all approaches. I re-ran the load-bearing numerics before ranking.

## Numeric sanity checks (independent, this round)
- `f(W_m)` telescopes exactly `1,1,3,5,11,21` and the n=4 cascade `[1,2,4,8,16]→…` gives
  `[11,5,3,1,1]` — matches the explorer/outliner claim digit-for-digit.
- **Exchange-lemma base direction confirmed:** for `W_n` (n=2,3,4) the minimum of `f` over
  *all* single-cut placements (piece × offset grid) equals exactly `f(W_{n-1})`, and it is
  achieved by cutting the **top** piece; no non-top cut beats it. This is real support for the
  restricted (not blanket) exchange lemma — the direction the induction needs holds at k=1.

## self-similar-recursion — CHANGES REQUESTED (build; the lead)
Verdict: sound technique, strongest lead, cleanly closes GAP-L in principle. Not RETHINK.
- GAP-L: the strengthened invariant `f(≤k cuts on W_m) ≥ f(W_{max(m-k,0)})` (k=m=n ⇒ `f≥1`)
  genuinely **unifies Case 1 and Case 2** — this is a real structural gain over the round-1
  top-vs-R split, and the telescoping is numerically exact. Good.
- **Load-bearing gap (be explicit, do NOT wave through):** the induction on k relocates GAP-L
  onto the EXCHANGE LEMMA, and the honest content is that the IH must be proved **for the whole
  class of partially-cascaded odd-multiplicity dyadic staircases**, not just for `W_m`. After
  XY's first cut the multiset is no longer `W`-shaped, so "apply IH to `W_{m-1}`" is only valid
  because the P1 cancellation collapses `{2^m}∪W_{m-1}` back to a `W_{m-1}`-shaped set — that
  collapse must be shown to hold (and the invariant maintained) for every reachable
  intermediate multiset and every cut, not just the bisect-top cascade. The builder must state
  and prove the exchange lemma over that class; the mechanism (Lemma 3 flip-set ⊆ piece length,
  top odd-band lives on `t∈[2^{m-1},2^m)` so only a top cut can lower the high band) is stated
  and is the right mechanism, but it is currently an argument sketch, not a proof. Prove it;
  do not restate the numeric check as the proof.
- Explicitly forbidden: the blanket "non-max cut never helps" (FALSE, 28k counterexamples) —
  the file already flags this; keep the restricted version only.
- GAP-U: the regime split (dominant `a_1≥Σ(rest)` ⇒ forced top-cut, branch on `a_1>2a_2`;
  balanced ⇒ adaptive stop keyed to `1/D_b`) is a coherent recursion and correctly explains why
  fixed "bisect n times" overshoots. Remaining gap: the residual-accounting closure to exactly
  `1/D_n` and the stopping-test correctness are not yet proved — flag as the GAP-U crux the
  builder must close, and watch the top-heavy `[1,ε,…]` configs where iterated-top-match died.

## alternating-sum-threshold-potential — CHANGES REQUESTED (build; distinct mechanism)
Verdict: right technique (matching duality, certified `f = min-weight matching cost`), a
genuinely different mechanism from self-similar — a **one-shot dual certificate**, no induction
on budget. Keep it far from self-similar on that axis.
- GAP-L crux: construct the dyadic-level price `φ` with (i) `φ(u)+φ(v) ≤ |u−v|` for all present
  pairs, (ii) `Σφ` monovariant-up under cuts, (iii) `Σφ(W_n)=1`. The monovariance claim ("a cut
  only adds level-crossings") is the load-bearing step and is plausible but **unproven** — the
  builder must verify feasibility holds uniformly over *every* ≤n-cut refinement, not just at
  `W_n`. Real risk (self-flagged in the file): if `φ` collapses to re-deriving `f` by induction,
  the approach is not far enough from self-similar and should pivot to the explicit-primal GAP-U
  half only. Acceptable to build as-is with that fallback stated.
- GAP-U: explicit slot-matching (existence, not optimality) is a legitimately easier target than
  proving optimality — good. Prove the constructed cost telescopes to `≤ 1/D_n` including
  top-heavy markings.
- Do NOT pursue bare LP duality on cut *positions* (non-concave, re-sorting kinks — recorded
  dead end); duality is on the fixed post-cut multiset only. File already respects this.

## game-value-recursion — APPROVE (registered; the diversity seed)
Verdict: the only approach that genuinely **leaves the layer-cake framing** — recursion in the
game value via strategy-stealing + turn-by-turn dyadic-domination invariant, adversarial move
ordering, never reduces to scalar `f`. This is exactly the "different framing" the orchestrator
asked for to break the single-gap trap. Registered at cold-start Elo. Not a fragment: its
top-level target is the full claim `c(n)=2^n/D_n`, both bounds from one recursion.
- Honest, correctly-flagged risk: its crux is the **BUDGET NON-FUNGIBILITY** lemma (an adaptive
  XY who watches one region before allocating cuts gains nothing over greedy-attack-the-largest),
  which the new-framing explorer identified as *possibly the true combinatorial obstruction of
  the whole problem*. It may genuinely fail. That is acceptable for a diversity seed: even if it
  stalls it isolates the "adaptivity gains nothing" lemma as a named target the other two
  framings also implicitly need — high option value.
- Guardrails the builder must respect (from the file/explorers): the bare `f ≥ 2·max−Σ`
  inequality is TRUE but too weak once the top is subdivided (max shrinks, bound goes slack) —
  do NOT resubmit it for Case 2; the invariant must be tracked recursively per dyadic level, not
  once globally. Base n=1 and the fixed-point algebra `2·2^n/D_n−1 = 1/D_n` are certified.

## majorization-smoothing — retire (not built; not registered anew)
Agree with the outliner: the one-shot majorization certificate is provably non-monotone
(round-1 dead end), its P1–P4 toolkit is fully absorbed into the two revised approaches. Stays
in the population (never hard-retired) but out of this round's build set. Its Elo now sits last.

## Field-diversity note (for the orchestrator)
self-similar-recursion and alternating-sum-threshold-potential still **share the layer-cake
reduction** (`f = M = matching cost`); they diverge only in *mechanism* (budget induction vs.
one-shot dual), so they are moderately close and could hit a related wall. game-value-recursion
is the one framing that leaves that reduction entirely — it is the intended hedge against the
single-gap trap. If both revises stall on their respective certificates next round, escalate
the game-value framing (or seed a fourth, even-further framing) rather than routing around the
same reduction.

## Ranking (folded)
self-similar-recursion 1546 (advanced; GAP-L cascade numerically exact — lead) >
alternating-sum-threshold-potential 1541 (partial; firm foundations, distinct dual mechanism) >
game-value-recursion 1485 (new; genuinely diverse but crux may be the true obstruction) >
majorization-smoothing 1428 (partial; non-monotone certificate, retired).

build set: self-similar-recursion, alternating-sum-threshold-potential, game-value-recursion
