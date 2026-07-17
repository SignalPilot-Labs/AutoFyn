# Outline review — Round 3, imo-2026-06

## Field-level notes

- Ranking sidecar did not exist (round 1 ended without summary); I registered all three slugs this round: `greedy-clique-closure`, `small-prime-core`, `wqo-domination`. Ranking updated (see below).
- The threshold correction (z = a_1, not rad(a_1), not p_max) is real and load-bearing. I re-verified: for a_1 = 48 the sequence is 48, 50, 52, 54, 56, … and 56 = 2^3·7 is a term, so the rad-threshold companion construction fails exactly as the outliner says. The outliner's "Watch out" items correctly quarantine this.
- Empirical check: SCPL (every pair of terms shares a prime ≤ a_1) holds on 80 terms for a_1 ∈ {15, 48, 105}, including the non-squarefree case. No contradiction with the strategy.
- I traced the streamlined descent (Step 4 a–g) by hand: the Companion Lemma's two cases (t = 0: x = m_0 | a, m_0 ≤ a/q < a; t ≥ 1: x < p·a_1 < pq ≤ a) are correct given pq | a with p, q distinct; the two uses of minimality (strong IH on larger index for step e, minimal i for step g via disjointness c) do not circle. The skeleton is valid.

## small-prime-core — CHANGES REQUESTED (build)

Right technique, whole attempt, every step has a stated mechanism, and the crux now has a checkable descent plan. HIGH confidence is justified. Fixable issues the builder must close while writing:

1. **Notation clash in Step 3' (valid-below-are-terms).** V_n is defined as {m > a_n : gcd(m, a_i) > 1, i ≤ n}, so "V_n ∩ [a_1, a_n] = {a_1, …, a_n}" is vacuously empty as written. Define a separate constraint set W_n = {m ≥ a_1 : gcd(m, a_i) > 1 for i ≤ n} (no lower bound in m) and state the lemma for W_n; step (f) of the descent must use W_{i-1}, splitting x_i ∈ [a_1, a_{i-1}] (a term, by the lemma) vs x_i ∈ (a_{i-1}, a_i) (contradicts greedy minimality of a_i). The logic is fine; the symbols are not.
2. In step (f), spell out why (a_{i-1}, a_i) contains no W_{i-1}-valid element other than a_i (greedy chose a_i as the least valid element > a_{i-1}), and note x_i < a_i strictly, so x_i lands at or below a_{i-1}.
3. Step 6: write the per-window counting fully (shift-by-M order isomorphism, exactly |R| elements per window inside [a_1, ∞), anchored at a_1 ∈ A) — no "clearly".
4. Include the a_1-prime/prime-power remark and both companion cases as the outline promises.

## wqo-domination — CHANGES REQUESTED (build)

A whole attempt with the same SCPL crux (deliberate, independently re-derived) and a genuinely different endgame (minimal antichain E_∞ in the finite poset 2^Q, domination of large-prime constraints via the ∏ p^N-is-a-term trick). Step 3's domination argument is sound given SCPL and Reduction. Issues:

1. Same notation fix as above (it imports Steps 1–3'').
2. Step 3: prove "∏_{p∈σ(a_k)} p^N is a term for N large" explicitly — it needs BOTH that the product is in V_∞ (every a_i shares a small prime with a_k by SCPL) AND ≥ a_1 (choose N), then Reduction. Don't hand-wave.
3. Correctly avoids the recorded WQO-on-P_fin dead end — only 2^Q for finite Q is used. Keep it that way.

**Shared-gap acknowledgment:** the two build slugs share the SCPL crux by design. This is a controlled single-gap bet, not a trap: the descent plan has been hand-verified at skeleton level, two independent write-ups are error-catching redundancy for the one critical step, and `greedy-clique-closure` is retained live as the out-of-framing hedge. Acceptable this round. If the descent breaks under proof review, next round MUST diversify framings, not re-route within SCPL.

## greedy-clique-closure — HOLD (agree with outliner)

Live, not built. Its density/first-moment route to |E_∞| < ∞ is the only non-SCPL framing in the field and is the correct insurance. Its crux is strictly harder than the descent as things stand, so building it now would waste a builder; if SCPL survives review it is superseded, if not it gets the B^N-is-a-term ammunition next round. Do not convert it to SCPL.

## Ranking (recorded via update_ranking)

1. `small-prime-core` — Elo 1531. Sharpest plan, complete mechanisms, corrected threshold.
2. `wqo-domination` — Elo 1500. Same crux, independent endgame; slightly longer route.
3. `greedy-clique-closure` — Elo 1469. Live hedge; crux (density finiteness) still unattacked.

## Cuts

None. All three are whole attempts at the full claim; no approach repeats a recorded dead end (Q = P(a_1), P_fin-WQO, and prime-stabilization are all explicitly quarantined in the outlines).

## Shared lemma plan

The `lemmas/` certify-once list (clique, reduction, valid-below-are-terms, companion, scpl, periodic-enumeration) is well-chosen. Whichever builder finishes the descent first proposes `scpl.md`; the reviewer certifies; the other imports. Note the valid-below lemma must be stated with the W_n constraint set per issue 1 above.

build set: small-prime-core, wqo-domination
