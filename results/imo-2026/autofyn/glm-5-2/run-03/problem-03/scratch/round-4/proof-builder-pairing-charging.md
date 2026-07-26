# Round 4 proof-builder: pairing-charging (G2-flat n≥3)

## Did I find a VERIFIED adaptive Xiang construction for n=3 flat configs (caps D ≤ 1/D_n)?

YES. The naive surplus-chain was FALSIFIED first (outline-reviewer's confirmed gap:
for n=3 the (n−1)-mark chain leaves p_4 UNPAIRED, giving D = |r_2 − p_4| = |2p_1 − 1|
(NOT r_2); 18050/30000 configs fail; and the chain is non-executable for genuinely
flat configs where p_1 − p_2 < p_3). ALL 2-mark chain variants collapse to the single
value |2p_1 − 1| (arithmetic identity r_2 − p_c = 2p_1 − 1 regardless of which
pieces are matched). The chain family is DEAD for G2-flat.

The CORRECT construction: **peel once (Lemma 3, certified) + apply the certified
n=2 menu to the 3-piece rest** (≤3 marks total).
- Mechanism: Lemma 3 makes the split-to-match pair (p_j, p_j) parity-neutral,
  so D_final = D_rest EXACTLY on the 3-piece rest {p_i − p_j} ∪ {two others}.
  Then the n=2 menu (§6.3, certified) on the rest uses ≤2 marks; the rest total
  T = 1 − 2 p_j, and the n=2 theorem gives D_rest = min(c, |2a−T|, a−b, b−c).
- Six peel choices (i,j); take the min.

VERIFICATION: 40k+ flat-regime n=3 configs (random + near-dyadic-boundary +
uniform + spiky-flat), 0 failures; max construction D = 0.0662 < 1/15; TIGHT
at the dyadic boundary (8/15,4/15,2/15,1/15): construction gives exactly D = 1/15
(peel p_1→p_2, rest {4/15,2/15,1/15}, n=2 menu min = 1/15). Continuous into
the spiky regime (Lemma 4 gives D = p_4 at the boundary, also = 1/15).

## Did I generalize to n≥3 and write the proof? Proof sketch.

PARTIALLY. I proved a clean inductive handle (Lemma 5) and 2 of 3 sub-cases for n=3;
the very-flat residual is verified-but-unproved.

Lemma 5 (peel-once + (n−1)-bound, the inductive upper-bound handle):
  peel p_1 → p_j (1 mark) + (n−1)-mark bound on rest ⇒ D ≤ (1 − 2 p_j)/D_{n−1}.
  ≤ 1/D_n  ⟺  p_j ≥ g_{n−1} = 2^{n−1}/D_n  (arithmetic identity).
  This closes the regime "some p_j ≥ g_{n−1}" for EVERY n, conditional on the
  (n−1)-bound (inductive; base n=2 certified).

n=3 sub-cases:
  Case A (p_2 ≥ 4/15 = g_2): peel p_1→p_2, D ≤ (1−8/15)/7 = 1/15. PROVED.
  Case B (p_3 ≥ 4/15, p_2 < 4/15): peel p_1→p_3, D ≤ 1/15. PROVED.
  Case C (p_2, p_3 < 4/15; "very flat", p_1 > 2/5): the loose bound T/7 fails.
    VERIFIED via the 3-peel subfamily {p_1→p_2, p_1→p_4, p_2→p_3} × full n=2 menu
    (30k Case-C configs, 0 failures, max 0.0646 < 1/15). But the 12-expression
    sort-regime casework (each n=2-menu member is piecewise-linear across ≤3
    sort-regimes of the rest triple) is NOT proved — OPEN GAP.

General-n status: the peel-once + (n−1)-bound pattern inducts cleanly for the
"some p_j ≥ g_{n−1}" regime at every n (Lemma 5). The very-flat residual
(all p_j < g_{n−1}) is the generalized crux; for n=3 it is Case C (verified);
for n ≥ 4 it is open and unverified.

## Named gap(s) remaining

- **G2-flat Case C (n=3, very-flat sub-case `p_2, p_3 < 4/15`):** the 3-peel
  subfamily {p_1→p_2, p_1→p_4, p_2→p_3} × full n=2 menu is VERIFIED
  (0 failures / 30k, max 0.0646 < 1/15, tight at dyadic) but the 12-expression
  sort-regime casework is UNPROVED. This is the immediate next target.
- **G2-flat very-flat residual for n ≥ 4:** unverified, unproven. The
  construction PATTERN (peel once + (n−1) full menu) is the right inductive
  shape, but each level's very-flat sub-case needs its own casework.
- **G1-general (lower bound, n ≥ 3):** shared, imported from
  `splits-inequality.md` (partial — Cases A/B/C; multi-split overlap bound open).

## Spec concerns

YES — the outliner's surplus-chain telescope is FUNDAMENTALLY FLAWED for n≥3:
it leaves p_{n+1} unpaired (D = |2p_1−1|, not r_{n−1}), and it is non-executable
for flat configs. Route back to outliner: replace "surplus-chain telescope"
with "peel-once + (n−1)-full-menu" as the G2-flat mechanism for ALL n≥3 work.
The correct construction is config-adaptive (min over 6 peels × full menu),
not a single chain. The LP-duality explorer's note is consistent: the flat
regime needs per-config adaptive pure strategies (the integrality gap is the
value of Xiang's information), and peel+n-menu IS such an adaptive pure strategy.

## Per-role rule learned
ALWAYS run the falsification sweep BEFORE attempting a proof of any "chain/telescope"
construction — the n=3 surplus-chain looked clean algebraically but failed 60% of
configs because it left the smallest piece unpaired (a sort-parity issue the algebra
hid). Verify D-formulas by direct sort-computation, not just chain algebra.
