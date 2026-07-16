# Build report — ll-dyadic-symdiff (Round 8)

**Problem:** imo-2026-03 (IMO 2026 P3). **Slug target:** LB via measure(S_Q△S_R)≥1.
**This round:** push the REFINED-R branch (the LB-completeness piece the anchor T(ℓ) leaves open).
**Status:** partial (unchanged flip; genuine new closed content + honest residual).

## What I closed / advanced (all rigorous)

1. **General-`R` core (Cases 1/2/Sub-3a are R-agnostic).** Made explicit and proven that Cases 1, 2,
   Sub-3a of the three-way split close `A(Q∪R) ≥ 1` for **any** `R` with `max(R) ≤ 2^{n−1}`,
   `A(R) ≥ 1` — using only `S_R ⊆ [0,2^{n−1})`, the piece list of `P`, and dyadic levels; **no
   `G_{n−1}`-band structure** (no SET IDENTITY, no top-band decomposition). Assembled from the three
   certified lemmas `ll-case1-high-interval`, `parity-piece-count`, `dyadic-level-parity`.
   **Coverage: 340/371 refined configs at n=3 (91.6%), 0 violations.**

2. **Budget-reduction lemma (new).** Refined `R` (`c_R ≥ 1`) ⟹ `|Q| ≤ n` (from joint budget
   `c_Q + c_R ≤ n`). Structural constraint on the residual.

3. **Double-REFL for a refined `R` with the top piece `2^{n−1}` uncut (new).** The anchor double-REFL
   proof never used `R = G_{n−1}` beyond `max(R)=2^{n−1}` and `max(R∖{2^{n−1}}) ≤ 2^{n−2}`. For any
   refined `R` with the top piece uncut, `R' := R∖{2^{n−1}}` refines `G_{n−2}`, so (I-ref)
   `A(Q∪R)=2^{n−1}−A(Q∪R')` and (II-ref) `A(Q∪R)=2^{n−1}−q_1+A(Q'∪R')` hold (certified REFL then
   REFL-gen), closing **B3a-ref** (`q_1 ≤ 2^{n−2}`) and **B3b-ref** (`2^{n−2}<q_1≤2^{n−1}−1`) for **all
   `n`**, reducing the rest to `(B2*)-ref` `A(Q'∪R') ≥ 1`.

4. **Refined-`R` residual breakdown (exhaustive, 3 buckets).** After the core, the residual (31/371 at
   n=3) splits into: (i) `max(Q) ≥ 2^{n−1}` [27] → Lemma REFL (R-agnostic) → *GAP-A refined-R*
   `A(Q'∪R) ≤ μ−1`; (ii) `max(Q) < 2^{n−1}`, top uncut [2] → double-REFL → *(B2\*)-refined-R'*; (iii)
   `max(Q), max(R) < 2^{n−1}` (top cut) [2] → **no reflection anchor**, genuine hard residual.

## Honest residual (NOT claimed closed)
- Buckets (i),(ii): alternating-tail `+1` crux family, but with a **refined** `R`/`R'`. Per the
  refinedR explorer + tight case `R={4,4,4,2,1}, Q={5,5,4,2}` (n=4, `S_Q=[2,4)⊄S_{G_3}`), these are
  **genuinely separate** from the anchor `T(ℓ)`; NOT claimed inherited. No refined-`R` SET IDENTITY /
  top-band analogue exists (confirmed).
- Bucket (iii) top-cut refined `R`: true no-anchor residual, nonempty (2/371 at n=3, both non-tight A=2).

## Numeric checks (all bounded <20s, joint cut budget `#Q+#R ≤ n` enforced, n=3 ½-grid)
- Target `A(Q∪R) ≥ 1`: **0 violations** over all 371 refined configs; min A over residual = 1.
- Core coverage: Case 1 = 241, Case 2 = 48, Sub-3a = 51 (=340), 0 violations.
- Residual buckets: (i) 27 [REFL identity + `A(Q'∪R)≤μ−1` hold, 0 viol], (ii) 2 [(I-ref),(II-ref) 0
  mismatch], (iii) 2 [both A=2].
- Double-REFL top-uncut over all 35 branch-B3 refined configs: (I-ref),(II-ref) 0 mismatches;
  B3a-ref/B3b-ref close (6), only B3c-ref/(B2\*)-ref residual (9).

## Guardrails respected
- Did NOT re-import the false "`max(Q)<2^{n−1}⟹A≥2`" (B3 tight at A=1).
- Did NOT assume a refined-`R` analogue of the SET IDENTITY / top-band decomposition.
- Did NOT claim Sub-3b refined `R` closed — left as honest residual (buckets ii-residual, iii).
- Did NOT merge with ll-inclusion-gap; this stays a rival complete LB attempt.
- Did NOT hand-edit `.ranking.json`.

## Promotable lemmas (for reviewer certification)
- **General-`R` core of Lemma LL** (Cases 1/2/Sub-3a hold for any `max(R)≤2^{n−1}`).
- **Budget-reduction lemma** (refined `R` ⟹ `|Q| ≤ n`).
- **Double-REFL for refined `R` with top piece uncut** ((I-ref),(II-ref); B3a-ref/B3b-ref close all n).
(Lemma REFL, REFL-gen, dyadic-level-parity, ll-case1-high-interval already certified — imported.)

## Spec concerns
None.
