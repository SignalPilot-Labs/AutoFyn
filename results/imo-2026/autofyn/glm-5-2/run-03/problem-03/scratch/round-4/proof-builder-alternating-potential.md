# Round-4 proof-builder — alternating-potential (imo-2026-03)

## Target owned
The **G1-ii** sub-case of the shared lower-bound wall G1 (`M = 2^{n−1}` unique-largest fragment of `2^n`, rest's piece `2^{n−1}` SPLIT — no Case-C tie to peel), via the band-parity / t-axis decomposition lens. Approach file: `results/imo-2026-03/approaches/alternating-potential.md` (edited in place).

## What I closed / reduced

### 1. Band-parity lens = Lemma-4 re-lensing (confirmed, NOT a bypass)
Decomposing `D = ∫[j odd]` into dyadic-tower bands re-derives Lemma 4 (`D = M − D_{R'}` where `R'` = all non-M pieces) in band language. The "cheap kill" for Case A (`2^n` unsplit) is `D_{R'} ≤ total(R') = 2^n − 1 ⟹ D ≥ 1`. For G1-ii, the band reduction gives `D = 2^{n−1} − D_{R'}`, target `D_{R'} ≤ 2^{n−1} − 1`; the trivial bound `D_{R'} ≤ max(R') < 2^{n−1}` is short by an arbitrarily small `ε`, so the "shave 1 unit" wall persists. **Recorded as alternative bookkeeping, not a bypass** — consistent with the explorer's and reviewer's honest caveats. Do NOT chase a band-parity bypass.

### 2. G1-ii r = 2 sub-case: CLOSED (subsumed by Case B)
When `2^n → 2^{n−1} + 2^{n−1}` (one split) and the rest's `2^{n−1}` is split, the two `2^{n−1}` fragments form a parity-neutral equal pair (`+2 · 1_{[0,2^{n−1})}` is even, hence parity-neutral by the parity-integral lemma). Removing the pair gives `D = D_{R_0} ≥ 1` by `G1(n−1)`. This is the `M = g_2 = 2^{n−1}` boundary of Case B (Case-B bound `D = 2^n − D_{R_0} − 2 E_1` with `E_1 = 2^{n−1} − D_{R_0}` saturates to `D = D_{R_0}`). Verified exact-rational n=3. No separate argument needed; Case B covers it.

### 3. G1-ii r ≥ 3 sub-case: REDUCED to G1-i (conditional)
**Lemma (G1-ii ⟹ G1-i, perturbation/continuity, §3.7).** Perturb `M = 2^{n−1} → 2^{n−1} + ε` (reduce F's total by ε, keep R_0 unchanged). The perturbed config lands in a valid G1-i config (`M > 2^{n−1}`, rest's `2^{n−1}` split — allowed in G1-i). `D = ∫[j odd]` is continuous in ε (piecewise-linear; at ε = 0 the sort order is stable because `M = 2^{n−1}` is STRICTLY largest in G1-ii). Hence `D(G1-ii) = lim_{ε→0+} D(G1-i perturbed) ≥ 1` once G1-i holds. Verified computationally (n=3,4: D continuous across sort-boundary crossings; near-degenerate G1-ii configs approach D = 1 linearly from above, boundary = Case C).

This is a genuine, rigorous REDUCTION (G1-ii is the `M → 2^{n−1}` boundary of G1-i), NOT an unconditional closure. Conditional on `dyadic-induction` certifying G1-i this round.

## Lemma upgrade / cross-check
- No new lemma certified this round (the G1-ii ⟹ G1-i reduction is CONDITIONAL on G1-i, so it is not yet a standalone certified lemma). Offered as promotable `lemmas/g1ii-reduction.md` only IF the reviewer finds the conditional reduction reusable — it becomes load-bearing the moment `dyadic-induction` certifies G1-i.
- Cross-check with `splits-inequality.md`: the r=2 sub-case being Case B's boundary is a clean consistency check (Case B's bound saturates exactly at `M = g_2 = 2^{n−1}`).

## Named gaps remaining
- **GAP-L (shared, lower bound) — NARROWED.** G1-ii is now a conditional reduction to G1-i (§3.7), not an independent open sub-case. Remaining open: G1-i (`M > 2^{n−1}`), G1-iii (all fragments < `2^{n−1}`), and the multi-split non-tie overlap bound `2C ≥ D_{R_0} + D_F + 1 − M` (the shared crux). All owned by `dyadic-induction` this round.
- **GAP-U (upper bound, general n): CONCEDED** (round 2, unchanged). No concrete Φ escaping the factor-of-2 wall. Carried by `pairing-charging`, `minimax-strategy-family`.

## Spec concerns
None. The outline's watch-out ("band-parity is a RE-LENSING, not a bypass") is confirmed correct — I did not chase a bypass. The outline's framing of G1-ii as this approach's owned sub-case and dyadic-induction owning G1-i/iii is the right complementary split; the §3.7 perturbation reduction is the concrete link between them (G1-ii = boundary of G1-i). The single-gap dependency on G1-i is acceptable because the two approaches own DIFFERENT sub-cases (complementary, not duplicated — no single-gap trap).

## Status
`partial`. The approach's rigorous reusable contributions: D-reformulation, parity-XOR toggle lemma (certified), peeling lemma + corollary (certified), lower-bound construction + n=1, and the round-4 G1-ii ⟹ G1-i reduction (conditional). G2 upper bound conceded (sound). G1 full closure pending `dyadic-induction`'s G1-i certification.
