# Proof-builder report — imo-2026-03, slug upper-general-cascade (round 7)

Status: **partial** (advanced). File: `results/imo-2026-03/approaches/upper-general-cascade.md`.

## 1. Arithmetic correction made (the flagged overclaim)

The double-cancel entry's IH(n−1) reduction threshold was stated as 2^{n−1}/D. **This is wrong by a
factor 3/2** (50% too small). Corrected derivation, now in the file:

  1 − 2(a_2+a_3) < (2^{n−1}−1)/D ⟺ a_2+a_3 > (2^{n+1}−2^{n−1})/(2D) = 3·2^{n−1}/(2D) = **3·2^{n−2}/D**.

Consequences recorded honestly:
- The geometric config a_k = 2^{n+1−k}/D sits **exactly** on the corrected threshold
  (a_2+a_3 = 2^{n−1}/D + 2^{n−2}/D = 3·2^{n−2}/D); after double-cancel its active sum is exactly the
  IH(n−1) *boundary* (non-strict) — the marginal/tight case.
- The true double-cancel residual (a_2+a_3 ≤ 3·2^{n−2}/D) is **nonempty for n ≥ 3** (empty only n ≤ 2).
  The prior "B2 settled for n ≤ 2 for the right reason" was right only *vacuously* — now corrected.
- I also found the double-cancel move silently assumed **a_1 − a_2 ≥ a_3** (needed to place the 2nd
  cut); that extra hypothesis is now stated. So the entry covers even less than "above threshold."

## 2. What I PROVED this round (real advance)

**Lemma GreedyCascade (new, certifiable, uniform in n).** For sorted positive lengths b_1 ≥ … ≥ b_p
with Σ b_i = 1 and **b_1 ≥ 1/2**, XY with p−1 cuts cancels b_2,…,b_p in matched pairs (cut the running
leftover r_j at b_{j+1}; legality r_j ≥ b_{j+1} follows from b_1 ≥ 1/2 ≥ 1−b_1 ≥ b_2+…+b_{j+1}) and
leaves the single leftover r_p = 2b_1 − 1. By Lemma X (certified), **A = 2b_1 − 1**. Hence with
b_1 ≤ c(n): **A ≤ 2c(n) − 1 = 1/D**.

This **closes B2-large (1/2 ≤ a_1 ≤ c(n)) for ALL n** with an explicit closed-form n-cut strategy —
the first uniform-in-n slice of B2. It is *not* a q-induction (dodges the r6 fixed-point obstruction)
and needs no gap conditions.

Verification (rigorous proof stands alone; these are checks):
- Both prior residual witnesses close: n=3 {47/90,31/135,43/270,4/45} (a_1=47/90 ≥ 1/2) → A = 2/45 <
  1/15; n=5 {32/63,…} (a_1 = c(5)) → A = 1/63 = 1/D exactly (boundary/tight).
- 0 failures over 1917 exact random B2 configs with a_1 ∈ [1/2, c(n)], n = 2..7.

## 3. What remains OPEN (honest gap)

The B2 residual is now the single clean condition **a_1 < 1/2** (B2-small, no dominant piece). There
GreedyCascade's domination fails. Partial coverage: the corrected double-cancel closes the sub-region
{a_1−a_2 ≥ a_3, a_2+a_3 > 3·2^{n−2}/D} but only for n ≤ 5 (IH(n−1) proved only through q=4). The rest
of a_1 < 1/2 is open. Min-A search confirms A ≤ 1/D is *achievable* everywhere tested (e.g. n=3
(2/5,3/10,1/5,1/10) → A = 0 via 2 fragment cuts), consistent with the answer, but the strategies are
**adaptive** with no closed form. **B2-small is the same fragment-cascade wall as the IH(q ≥ 5) flat
residual** — the two open faces of one wall.

Answer to the outliner's targeted question ("does near-equality force a consecutive gap ≤ 1/D, hence
CaseB-Reduction 2?"): **No.** In the hard regime all gaps > 1/D by hypothesis, and near-equality does
not manufacture a ≤ 1/D gap among the *original* pieces; the closing strategies use genuine fragment
cuts (splitting at non-piece lengths), not whole-piece cancellation. So the residual does **not**
reduce to an already-closed case in general.

## 4. Spec / diversity concerns

- The two remaining open upper-bound faces (IH(q≥5) flat; B2-small a_1<1/2) are provably the same
  adaptive fragment-cascade wall. If `upper-vertex-reduction`'s global-max reframe (step 2–3 PL /
  max-at-vertex) is made rigorous, it would subsume BOTH faces at once — that is the highest-value
  upper-bound bet. The cascade family (this slug + direct-constructive) has now extracted its clean
  closed-form regions (Case A / B1-large q≤4 / B2-large a_1≥1/2); the leftover is genuinely adaptive
  and unlikely to yield to another closed-form cascade.
- No overclaim: Status stays **partial**. B2-large closed for all n; B2-small honestly open.

## Promotable
- **Lemma GreedyCascade** — recommend certification (pure conditional, derived from certified Lemma X,
  machine-checked exactly). Closes B2-large for all n.
