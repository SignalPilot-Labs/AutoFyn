# Proof-reviewer — imo-2026-03, Round 6

Two approaches built and reviewed independently. Both are correct advances and both are honestly
**partial**. No overclaims found; the builders' stated statuses match reality.

---

## Approach 1: direct-constructive

**Verdict: CHANGES REQUESTED. True Status: partial.** (Builder marked partial — correct.)

Scores: Correctness 10/10, Completeness/rigor 8/10 (two honest gaps remain), Progress 9/10
(confined lower bound fully closed — the round-5 refuted step is genuinely repaired).

### LOWER bound — confined case §4.2.7: VERIFIED CLOSED

I re-derived the load-bearing pieces from scratch rather than trusting the write-up:

1. **Directional derivative** A′₊(e_a − e_b) = (−1)^{G(g_a)} + (−1)^{Geq(g_b)} (up-move uses
   G=#{strictly above}, down-move uses Geq=#{≥}). Independently verified in exact arithmetic over
   5·10^4 multisets **including tie-laden/clustered configs** (round-5 rule: never validate on
   generic samples only). 0 mismatches — the formula holds AT ties, which is exactly where the
   minimiser lives.

2. **Case 1 (w_1 ≤ 2^{n−2})** is a direct sorted-alternating-sum bound A ≥ v_1 − v_2 = 2^{n−2} ≥ 1
   (n ≥ 3), needing no receiver/donor argument. **The two round-5 counterexamples
   ({2,10/3,10/3,11/3,11/3}, {2,7/2,7/2,7/2,7/2}) land here** (max frag ≤ 4 = 2^{n−2}); I confirmed
   A = 5 for the first. This is the genuine repair: the false "receiver exists" claim is never
   invoked at those clustered points.

3. **Case 2 (2^{n−2} < w_1 < 2^{n−1})**: w_1 is a **named receiver by counting** (only the intact
   2^{n−1} exceeds it ⟹ G(w_1)=1), NOT an existence claim — valid at ties. Minimality ⟹ no positive
   donor (Geq even). Sub-cases (2a) N_tot odd ⟹ intact 1 at bottom odd rank ⟹ A ≥ 1; (2b) N_tot even,
   f_min > 1 ⟹ flat-then-descent-past-I* contradicts minimality unless a=1 boundary reached first
   (A ≥ 1); (2c) N_tot even, f_min ≤ 1 ⟹ flat move to a minimiser with one fewer positive fragment
   and N_tot flipped odd ⟹ (2a). I checked each sub-case is valid, the dichotomy on w_1 ∈ (0,2^{n−1}]
   is exhaustive, and the **flat-move termination** weight m = #{positive fragments} is genuinely
   strictly decreasing with floor 2 = a=1 boundary — the round-5 "degenerate flat-move face" loose
   end is genuinely gone.

4. **Global check:** min_Δ A = 1 exactly, 0 failures over 2·10^5 random + clustered a=0 configs each
   n = 3,4,5.

The confined lower bound A ≥ 1 on Δ is **closed**. → **CERTIFIED** `lemmas/DyadicLower-confined.md`.

### UPPER bound — IH(4) §6.2: VERIFIED CLOSED (through q=4)

- **IH-reducible** (pure conditional): re-derived S − max(b_1,2b_2) = min(S−b_1, S−2b_2); confirmed
  both reduced instances have sum strictly below the exact IH(q−1) boundary (2^{q−1}−1)/D and all
  pieces > 1/D. The "gap-preservation hole" is a non-issue: IH(q−1) carries **no gap condition**
  (IH(3)'s proof is an exhaustive gap-case split covering all instances), so cutting b_1 at b_2 need
  not preserve a gap. No bundled empirical %. → **CERTIFIED** `lemmas/IH-reducible.md`.
- **IH4-flat** (pure conditional): re-derived b_2 < 4/D from S − max ≥ 7/D, and both sign sub-cases
  of b_3 + b_4 − b_2 with explicit δ-choice. Full IH(4) closure (reducible ∪ flat, complementary and
  exhaustive) verified 0 fails / worst A·D ≤ 1 over 8·10^4 exact hard-regime configs at
  D = 15,31,63,127. → **CERTIFIED** `lemmas/IH4-flat.md`.
- IH(4) is proven for **hard-regime** q=4 instances only, but that is exactly what the n=4 B1-large
  application needs (after halving a_1, the residual inherits the hard-regime gaps), and it reduces
  only to IH(3)-general (gap-free, proven), so the chain is valid.

### Honest gaps (why still partial)

- **L2 (lower):** XY spending cuts *outside* R_n. §4.4 reduces it to the same simplex but the
  exchange step is unwritten. This is the sole remaining lower-bound residual — genuinely open.
- **Upper general n:** IH(q ≥ 5) flat residual + B2 (handed to the sibling approach).

---

## Approach 2: upper-general-cascade

**Verdict: CHANGES REQUESTED. True Status: partial.** (Builder marked partial — correct.)

Scores: Correctness 10/10, Completeness/rigor 7/10 (the open core is honestly the whole general-n
upper bound), Progress 7/10 (IH(4) closed; a sound negative result on IH+(m)).

- **IH-reducible / IH4-flat**: same lemmas as approach 1 (this file states them slightly more
  carefully with the explicit "case (ii) via CaseB-Reduction 2" branch — redundant but not wrong,
  since IH(q−1) is gap-free). Verified as above. Theorem UB (IH(q) for all q ≤ 4) is correct.
- **IH+(m) dual-bound refutation — SOUND, don't penalize.** I checked the fixed-point obstruction:
  any single pair-cancel move on a flat residual leaves active sum = S − max(b_1,2b_2) ≥
  (2^{q−1}−1)/D, i.e. at or above the IH(q−1) boundary, never strictly inside; and the geometric
  config b_k = 2^{q−k}/D is a fixed point of halve-max with A = 1/D throughout. So the extra max
  bound shrinks one resource but the sum bound does not shrink at all — the dual bound cannot descend.
  This is a correct structural argument; leaving IH(q ≥ 5) + B2 open is the honest, correct call.
- **B2 (a_1 ≤ c(n)):** partial double-cancel entry covers a_2 + a_3 > 2^{n−1}/D; the near-equal
  small-pieces sub-region is genuinely open. No overclaim.

**Diversity note (for the orchestrator):** its distinctive differentiator (IH+(m)) is now dead, so
upper-general-cascade shares direct-constructive's pair-creation move-set on the same wall. If
IH(q ≥ 5) has not moved by round 8, a genuinely different upper-bound framing (global-extremal /
compactness that handles interior valleys, or a bounded multi-level collapse) is needed.

---

## Certifications this round

Admitted to `lemmas/` (all re-derived and machine-checked, no bundled empirical %):
- `DyadicLower-confined.md` — confined lower bound A ≥ 1 on Δ (REPLACES the refuted round-5
  Descent/receiver-existence claim, which never entered `lemmas/`).
- `IH-reducible.md` — pure-conditional one-step reduction to IH(q−1).
- `IH4-flat.md` — q=4 flat-residual leaf; with IH-reducible closes IH(4).

Round-5 Descent Lemma + Receiver-existence parity lemma: **REFUTED / not certified** (receiver-
existence false at clustered vertices); superseded by DyadicLower-confined.

---

## Goal Progress (for Eval History)

- **Status: partial** (unchanged flip-wise, but real structural progress). Both live approaches
  advanced; recorded via ranker as `advanced` (elo direct-constructive 1648.0, upper-general-cascade
  1650.2 — Elo deltas applied by the outline-reviewer's pairwise pass, not here).
- **CLOSED this round:** (1) the **confined lower bound** A ≥ 1 on Δ — the round-5 refuted
  receiver-existence step is genuinely repaired by the dyadic two-case split (verified at clustered
  configs, which is where the round-5 refutation lived); (2) the **Case-B hard-regime upper bound
  through q = 4** (IH(1)–IH(4)). 3 lemmas certified.
- **STILL OPEN (blocks solved):** **L2** (lower — XY cuts outside R_n; the confined case is done, the
  exchange/confinement step is unwritten) and **U1** (upper — IH(q ≥ 5) flat residual + B2 near-equal
  sub-region). The upper bound is complete only for n ≤ 4 (B1-large); B2 complete only for n ≤ 2.
- **Refuted this round (negative result, valuable):** the IH+(m) dual-bound descent route
  (fixed-point obstruction) — do not re-attempt in that form.
- **Next round:** (lower) route a builder at **L2** — the exchange inequality is now the ONLY thing
  between here and a fully closed lower bound. (upper) IH(q ≥ 5) needs a genuinely different framing
  (global-extremal / bounded multi-level collapse); the pair-creation cascade has bottomed out and
  both approaches now share it — consider opening ≥1 far-apart framing if it stalls again.
