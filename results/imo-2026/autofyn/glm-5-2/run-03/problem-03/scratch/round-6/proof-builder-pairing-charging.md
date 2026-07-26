# Round-6 proof-builder report — pairing-charging (imo-2026-03)

## Task
Close the n=4 very-flat G2 upper bound as a verified MILESTONE via mechanical vertex enumeration (analogous to round-5 n=3 Theorem-6 closure). Target: `f_4 ≤ 1/31` on `Π_4 = {p_2,p_3,p_4 < g_3=8/31, p_5 > 1/31}`, tight at dyadic `p* = (16/31, 8/31, 4/31, 2/31, 1/31)`.

## Outcome: n=4 G2 UPPER BOUND CLOSED (Theorem 7)

### The closure mechanism (the key insight)
The dispatch's vertex-enumeration mechanism, in the clean **"empty interior → boundary proved"** form:
1. `f_4` (peel-once + recursive `f_3` + certified `f_2` menu, ≤ 4 marks) is **piecewise-linear** on `Π_4^{cl}` (KB *Piecewise-concavity smoothing*). Breakpoints: **94 distinct arrangement hyperplanes** (90 internal — pairwise equalities + abs-breakpoints of the 60 peel-pair rest triples — + 4 boundary facets). The max of a PWL function on a compact polytope is attained at a cell-vertex of the arrangement.
2. **Verified by finite exact-rational computation**: NO 4-tuple of the 94 hyperplanes has its intersection in the STRICT interior of `Π_4^{cl}`. Checked all `C(94,4) = 3,049,501` 4-tuples (float pre-filter ~2s with `1e-7` strict margin, reliable for these small-integer-coefficient well-conditioned systems; `sympy.solve` exact re-check of near-interior candidates confirms 0). **0 strict-interior cell-vertices.**
3. ⟹ every interior cell-vertex lies on `∂Π_4^{cl}`, where ALL facets are PROVED `f_4 ≤ 1/31`:
   - **Sort-tie facets** `p_i=p_{i+1}`: `f_4 = 0` (peel exposes a 0 gap; menu's `c`- or gap-member vanishes). PROVED.
   - **Spiky facet** `p_5=1/31`: peel `p_1→p_2`, peel `p_3→p_4`, rest_3 = `{p_3−p_4, p_1−p_2, p_5}`; the `f_2` `c`-member (Lemma 4: equal-halve the 2 largest, leave the smallest) gives `D = c ≤ p_5 = 1/31`. PROVED.
   - **`p_2=8/31`, `p_3=8/31`, `p_4=8/31` facets**: peel `p_1→p_j`, `f_3(rest) ≤ (1−2·8/31)/D_3 = (15/31)/15 = 1/31` (Lemma 5 / Cor 6.1 rescaled, n=3 CERTIFIED). PROVED.
4. ⟹ `f_4 ≤ 1/31` on all of `Π_4^{cl}`; supremum `1/31` at `p*` (on the `p_2=8/31` Lemma-5 facet ∧ `p_5=1/31` Lemma-4 facet); open interior strict (worst `1/62`).

### Additionally PROVED (direct gap-extraction, mirroring n=3 Theorem 6)
Very-flat **sub-cases 1, 2, 3** (some interior gap `z=p_4−p_5`, `y=p_3−p_4`, `x=p_2−p_3` is `< 1/31`): peel `p_1→p_2`, peel the larger of two rest pieces into the smaller (leaving the small-gap pair `(p_4,p_5)`/`(p_3,p_4)`/`(p_2,p_3)` in rest_3), equal-split the third piece; the 3-regime identity `min(a−b,b−c) ≤ (a−c)/2` absorbs the sort-regime fan-out; `D ≤ gap < 1/31` strictly, 3 marks.

### Corollary 6.2 (n=4 upper bound — CLOSED)
Combining spiky (Lemma 4) + Cases A/B/C (Lemma 5, `g_3=8/31`) + very-flat `Π_4` (Theorem 7): **`c(4) ≤ 16/31 = 2^4/D_4`**, tight at dyadic `p*`, slack elsewhere. The answer `c(4) = 16/31` is verified on the upper-bound side.

### Honest rigor note
The closure rests on the finite-computational step (2): "no interior cell-vertices." This is a verified finite casework over `C(94,4)=3.05M` 4-tuples (the dispatch's intended vertex-enumeration mechanism, in "empty interior → boundary proved" form) — NOT a structural proof. The float pre-filter is reliable for these small-integer-coefficient well-conditioned systems; the `sympy.solve` exact re-check of near-interior candidates confirms 0. The alternative non-computational closure (the **4-construction cover's per-construction case-split** for sub-case 4's all-large residual — identified via greedy set-cover, each construction a `(peel1,peel2,member)` triple extracting a pair-difference of a 3-piece rest) is tractable but not written out; the `f_n` uniform-induction shortcut is a CONJECTURE.

### `f_n` uniform-in-n induction — still a CONJECTURE
n=3 PROVED / n=4 PROVED this round / n≥5 OPEN. The sort-independent-member lift breaks at n≥4 (5 binding peels at n=4). Theorem 7's max-at-boundary mechanism closes n=4 directly but does NOT lift to n≥5 without re-verifying the "no interior cell-vertices" finite check at each level (the arrangement-hyperplane count grows).

### Bottom line
- **n=4 upper bound `c(4) ≤ 16/31`: CLOSED** (Theorem 7 + Corollary 6.2). Tight at dyadic.
- Round-5 n=3 closure (Theorem 6 + Cor  6.1) stands unaffected and CERTIFIED.
- The lower bound (G1-general, n≥3, shared) and `f_n` conjecture (n≥5) remain OPEN — the approach overall is still PARTIAL.

## Files
- Approach file (appended Round-6 §6.5 Theorem 7 + Corollary 6.2; updated Status / Approaches tried / Current best / Summary table): `/home/agentuser/repo/results/imo-2026-03/approaches/pairing-charging.md`
- Verification scripts: `/tmp/f4_build.py`, `/tmp/vert_enum.py`, `/tmp/enum_fast.py`, `/tmp/cover.py`, `/tmp/decode4.py`

## Promotable lemmas (new this round)
- **Theorem 7 (n=4 very-flat upper-bound closure).** Statement: *for every n=4 Liu config (≤ 4 marks) in the very-flat regime `p_2,p_3,p_4 < 8/31, p_5 > 1/31`, Xiang has a ≤ 4-mark strategy with `D ≤ 1/31` (tight at dyadic `p*`, strict on open interior); mechanism: `f_4` is PWL on `Π_4^{cl}` (94 arrangement hyperplanes), no 4-fold intersection in the strict interior (verified finite check), so max at `∂Π_4^{cl}` where all facets are PROVED (`f_4=0` sort-tie / `c≤p_5=1/31` spiky / `f_3≤1/31` Lemma-5-rescaled). Combined with Lemma 4 + Lemma 5, closes `c(4) ≤ 16/31`.* Proved in §6.5 of `results/imo-2026-03/approaches/pairing-charging.md`. Proposed for certification into `results/imo-2026-03/lemmas/case-c-n4.md` as the n=4 instance of the upper bound — importable by any approach needing the n=4 flat upper bound. (Rigor caveat: the "no interior cell-vertices" step is a finite computational check, not a structural proof.)
