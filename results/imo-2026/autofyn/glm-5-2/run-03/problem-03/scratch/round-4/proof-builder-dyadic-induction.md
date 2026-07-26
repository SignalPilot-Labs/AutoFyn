# Round-4 proof-builder — dyadic-induction (imo-2026-03)

## Sub-cases closed this round

1. **G1-i, 2-piece F / rest-unsplit (Lemma 8, PROVED, all n ≥ 2).** When `2^n → M + a + b` (3 fragments, `M > 2^{n−1}` strict, rest `{1,…,2^{n−1}}` unsplit; total splits = 2 ≤ n), `D ≥ 1`. Mechanism: the union-measure reformulation (Lemma 7, exact) rewrites the bound as `b + |(b,a] ∩ E_{R_0}| ≤ T_n = (2^n − 1 − D_{R_0})/2`. The **rigid top O-block** `(2^{n−2}, 2^{n−1}] ⊆ O_{R_0}` (only the rest's piece `2^{n−1}` survives there, `j = 1` odd) gives `b + |(b,a] ∩ E_{R_0}| ≤ 2^{n−2}` via a 2-case split on whether `a ≤ 2^{n−2}` (interval fits below the top O-block) or `a > 2^{n−2}` (the part above `2^{n−2}` lies entirely in `O_{R_0}`, contributing 0 to `E`). Then `2^{n−2} ≤ T_n` for `n ≥ 3` (since `D_{R_0} ≤ 2^{n−1} − 1`), equality at `n = 3`. This **closes the n=3 tight Lemma-6 family** (where F has 2 pieces) and the entire 2-piece-F regime at every `n ≥ 4` (slack there).

2. **Low-cancellation regime (Lemma 9, PROVED, all F, all n).** The trivial overlap bound `|O_F ∩ E_{R_0}| ≤ |E_{R_0}|` yields `D ≥ 1` whenever `D_F ≥ W − D_{R_0} + 1` (F has little internal cancellation; covers single-piece F = Case B and 2-piece F with small smaller-fragment). This dispatches the "easy" half of the multi-piece F case cleanly.

3. **Union-measure reformulation (Lemma 7, PROVED identity).** `D = M + D_{R_0} + D_F − 2|O_{R_0} ∪ O_F|`; the wall is "shave 1 unit off the trivial union bound `|union| ≤ 2^{n−1}`," forced by the rigid alternating-dyadic tiling of `O_{R_0}`. This is the measure-extremizer explorer's Opening A, now recorded as a proved identity in the lemma bank.

## Did splits-inequality.md upgrade to FULL PROVED?

**No.** It remains **PARTIAL** (status updated to "PARTIAL, advanced"). Lemmas 7, 8, 9 were added as proved components, but the **high-cancellation, multi-piece-F** regime (G1-i with `s ≥ 3` pieces in F, the `n ≥ 4` Lemma-6 tight family territory) plus G1-ii (split rest) and G1-iii (near-tie, all fragments of `2^n` small) remain open. The trivial overlap bound (Lemma 9) and the 2-piece argument (Lemma 8) both fail there: the truth lies strictly between the two trivial caps `|O_F ∩ E_{R_0}| ≤ min(|E_{R_0}|, D_F)`, and capturing it needs the rigid-tiling / `O_F`-breakpoint interaction, which I could not close in budget.

## Exact named gaps remaining

- **GAP-G1-i-HC** (high-cancellation multi-piece F, rest unsplit): prove `|O_F ∩ E_{R_0}| ≤ (M − D_{R_0} + D_F − 1)/2` for `s ≥ 3`-piece F with small `D_F`. Verified TRUE (`n = 2..6`, correct split budget; tight at `n = 3, 4` via multi-piece F = Lemma-6 family). The 2-piece Lemma 8 argument does not extend: with `s ≥ 3`, `O_F` is a union of `≥ 1` intervals (not a single interval), and the "top O-block" trick (which used that `O_F` is a single interval ending at `a`) no longer pins the geometry. The superincreasing gap structure of `E_{R_0}` must play against `O_F`'s `s−1 ≥ 2` breakpoints — the unproved step.
- **GAP-G1-ii** (M = `2^{n−1}` fragment, rest's `2^{n−1}` SPLIT): Lemma 5's top band shifts (`max(R_0) < 2^{n−1}`); the tiling deficit must be re-derived on the shifted support. Verified TRUE; proof open.
- **GAP-G1-iii** (all fragments of `2^n < 2^{n−1}`): the outline's "reduce to G1(n−1)" is **flawed** — the rest `R = {2^n`'s fragments`} ∪ {1,…,2^{n−2}}` has total `3·2^{n−1} − 1 ≠ D_{n−1}`, so it is NOT a dyadic `(n−1)` config and `G1(n−1)` does not transfer. This is a near-tie regime (`m_1 = 2^{n−1} − ε`), as tight as the Lemma-6 family. Verified TRUE numerically; proof open.
- **GAP-G2** (upper bound, general n): unchanged from round 3 (conceded; the minimax/pairing routes are owned by siblings).

## Spec concerns

- **G1-iii reduction is unsound as outlined.** The outliner's skeleton step 4 ("reinterpret as `(n−1)`-dyadic instance with the sum-`2^n` fragments folded into the rest, reduce to G1(n−1)") is incorrect: the folded rest is not a dyadic `(n−1)` config (wrong total). Route back to the outliner: G1-iii should be re-framed as a near-tie regime symmetric to G1-i (largest piece `2^{n−1}` from rest, `2^n`'s largest fragment `m_1 = 2^{n−1} − ε` just below), not as a clean induction. The statement is still TRUE (numerics), but the proof route needs re-thinking.
- **No flaw in the 2-piece proof.** The "rigid top O-block" mechanism is clean and exact (verified tight at `n = 3`, slack `n ≥ 4`); this is a genuine partial closure.

## Verification summary (all exact-arithmetic, correct split budget)

- Lemma 8 (2-piece F): 5k trials each `n = 3..6` → worst slack 0 at `n=3` (213 tight), 0 at `n=4` (8 tight), positive `n ≥ 5`. Tight `n=3` configs = Lemma-6 family.
- Lemma 7 (union identity): 8k trials, 0 error.
- Full G1 with correct budget (`≤ n` splits): `n = 3..6`, no counterexample to `D ≥ 1` (confirms prior rounds after fixing a budget bug that had produced false violations).
