## Status
partial (new, round 3 — skeleton)

## Approach: amortized-parity

**Framing (third, distinct from both siblings).** Neither an explicit one-shot XY strategy
(direct-constructive) nor a config-space extremal argument (extremal-config), but a
**sequential greedy monovariant with amortized budget accounting**, in the style of the
dyadic-covering game aimo-0019 ("bound a cumulative resource by a linear potential"). XY
places its n cuts one at a time; a single potential Ψ tracks progress, and an amortized
argument shows n cuts always drive Ψ to its target.

Work with the parity form (Lemma R2, certified): O = 1/2 + (1/2)·μ{N(t) odd}, so the
upper bound O ≤ c(n) = 2^n/D is exactly

    **Ψ := μ{ t : N(t) odd } ≤ 1/D.**

Answer (same): c(n) = 2^n/(2^{n+1}−1), D = 2^{n+1}−1.

## Shared imports (certified / reusable)
- **Lemma G1** (greedy = odd-ranked) — certified.
- **Lemma R2** (O = 1/2 + ½·μ{N odd}) — certified. Turns the goal into Ψ ≤ 1/D.
- For the LOWER bound: import direct-constructive's construction + L1 (boundary-crossing) +
  L2 (exchange). This approach's DISTINCT spine is the UPPER bound via Ψ.

## Skeleton

1. **Per-cut change formula (the monovariant step).** Cutting a piece of length L into
   {L_min ≤ L_max} changes Ψ by
     ΔΨ = (μ{[0,L_min): N even} − μ{[0,L_min): N odd})
          + (μ{[L_max, L): N even} − μ{[L_max, L): N odd}),
   ranging in [−2L_min, +L_min]. Each cut adds one piece, flipping N by +1 on the two
   sub-intervals it creates; the sign of each contribution is set by the current parity of
   N there. (Derive cleanly from R1/R2 layer-cake.)

2. **Greedy XY rule.** XY repeatedly cuts the piece / location that maximises the DECREASE
   of Ψ (most negative ΔΨ), i.e. cut across regions currently of ODD N so both new
   sub-intervals flip odd→even. Formalise "there always exists a cut with ΔΨ ≤ −(current
   excess)/(remaining budget)" — the amortized guarantee.

3. **Amortized potential bound.** Define Φ_t = Ψ_t − (remaining marks)·δ for a suitable
   per-mark decrement rate δ tied to the dyadic ladder (δ ~ 1/D scaled). Show Φ is a
   supermartingale under the greedy rule: each cut reduces Ψ by at least the "fair share"
   of the remaining excess, so after n cuts Ψ ≤ 1/D. Mechanism: LB starts with ≤ n+1
   pieces, so N(0) ≤ n+1 and the initial odd-region measure is bounded; the ladder
   structure caps how much odd measure any single cut must remove, giving the linear
   accounting (aimo-0019 analog: ink on [0,x] ≤ 3x).

4. **Möbius-map reading of the budget (cross-check).** Each halving of the top piece maps
   the residual value v ↦ 2v/(2v+1); n iterations from v = 1 reach 2^n/D. This confirms n
   marks is exactly the right budget (not a coincidence — it is the amortized decrement
   rate of step 3 read multiplicatively).

5. **Assemble.** Ψ ≤ 1/D after ≤ n greedy cuts ⟹ O ≤ c(n) for every LB config (uniform in
   the Case-A / Case-B split — the greedy rule needs no case distinction). Combine with the
   imported lower bound ⟹ c(n) = 2^n/D. Verify n=1,2,3.

## Key lemmas (claim + mechanism)

- **Lemma A1 (per-cut formula).** ΔΨ ∈ [−2L_min, +L_min] with the explicit sign formula of
  step 1, because a cut flips N by 1 on the two created sub-intervals and Ψ counts
  odd-parity measure. — clean, derivable from R1/R2.
- **Lemma A2 (greedy sufficiency, load-bearing).** Under the greedy "cut across the largest
  odd-N region" rule, each of XY's n cuts reduces the excess (Ψ − 1/D) by at least its fair
  amortized share, so n cuts suffice to reach Ψ ≤ 1/D. Mechanism: the ≤ n+1 initial pieces
  bound N(0) ≤ n+1, and the dyadic gaps prevent odd-N regions from being smaller than the
  per-mark decrement — a linear-potential/amortized argument (aimo-0019).
- **Lemma A3 (budget = n via Möbius map).** The multiplicative decrement per halving is
  v ↦ 2v/(2v+1), fixed iterate 2^n/D after n steps — the same n-mark budget, read
  multiplicatively; a consistency certificate for A2's rate δ.

## Open gaps
- **A2 (greedy amortized sufficiency)** — HIGH RISK / load-bearing. The explorer flagged
  that NO clean uniform per-cut lower bound on |ΔΨ| exists for arbitrary configs; the
  amortized (not per-cut) accounting is the way around this — must be made rigorous. This
  is the analog of the direct-constructive Case-B wall, attacked by a different mechanism.
- A1 is routine; A3 is a cross-check, not load-bearing.
- Lower bound imported from direct-constructive (L1/L2).

## Cases to cover
- Verify the greedy rule reaches Ψ ≤ 1/D numerically for random LB configs n=2,3,4
  (falsification of A2's sufficiency) BEFORE proving.
- Configs with a dominant piece (a_1 > 1/2) vs. no dominant piece (a_1 ≤ 1/2) — the greedy
  rule should handle both without a case split; confirm.
- Initial config already satisfying Ψ ≤ 1/D (XY passes).

## Watch out for
- **Same-wall risk:** if the amortized bound A2 cannot be proved and degrades to "check
  each config," this collapses to U1 by another name. The distinct value is the AMORTIZED
  (potential-based) accounting — keep it a genuine linear-potential argument, not a
  per-config check. Run the numerical greedy-sufficiency test first.
- Ψ is a measure, not attained at a discrete optimum; handle the ε→0 open-cut supremum.
- The per-mark decrement rate δ must be chosen so Φ is a true supermartingale AND reaches
  the target in exactly ≤ n steps — tie it to the dyadic ladder via A3.

## Current best
The parity-form target Ψ ≤ 1/D (via certified R2) and the per-cut change formula (A1) are
clean. The load-bearing amortized sufficiency (A2) is conjectural and must pass the greedy
numerical test before investment; if it holds, the upper bound follows uniformly across all
LB configs with no Case-A/B split, a genuinely different route to the wall.
