# proof-builder — round 3 — dyadic-induction — imo-2026-03

## What I proved this round

Advanced G1 (the shared lower-bound wall: `D ≥ 1/D_n` for Liu's dyadic config after ≤ n Xiang splits) substantially, via strong induction on n with the parity-integral t-axis as the engine (Route B per the round-2 outline-reviewer). Rigorous progress:

1. **Largest-piece decomposition (Lemma 4, PROVED, all n).** For any final multiset with largest piece `M` and rest `R`: `D = M − D_R` (D_R = D of R). Proof via the parity-integral t-axis: on `(max(R), M]` only M contributes (j=1, odd); on `[0, max(R)]` M's +1 flips the rest's parity. Verified 3000 trials (n=2,3), 0 errors. This is the load-bearing structural identity for the whole G1 induction.

2. **G1 Case A (2^n unsplit, PROVED, all n).** `D = 2^n − D_rest`, `D_rest ≤ total(rest) = D_{n−1} = 2^n − 1` (universal `D ≤ total`). `D ≥ 1`. ✓

3. **G1 Case B (2^n split EXACTLY ONCE, PROVED, all n).** `2^n → M + g_2` (M ≥ 2^{n−1} ≥ g_2), rest `{1,…,2^{n−1}}` with ≤ n−1 splits. Derived the exact formula `D = 2^n − D_rest − 2·E_1` where `E_1 = ∫_0^{g_2} [j_rest even]`. Bound `E_1 ≤ ∫_0^{2^{n−1}} [j_rest even] = 2^{n−1} − D_rest` (sub-measure) ⟹ `D ≥ D_rest ≥ 1` by G1(n−1). Verified 20k trials, 0 failures; the formula matches direct computation exactly. This subsumes the n=1 and n=2 (0/1-mark) base cases previously proved.

4. **G1 Case C (2^n split, largest fragment M = 2^{n−1}, rest's 2^{n−1} UNSPLIT — the "tie" case, PROVED, all n).** The two `2^{n−1}`'s (fragment M + rest's piece) form an equal pair; the CERTIFIED peeling lemma (`lemmas/peeling.md`) removes it D-neutrally: `D = D_{R'}`. R' = (dyadic (n−2) with ≤ n+1−r splits) ∪ F (other fragments of 2^n, summing 2^{n−1}). Reinterpret R' as the (n−1)-dyadic config with piece 2^{n−1} refined into F (r−2 splits) and {1,…,2^{n−2}} with ≤ n+1−r splits; total ≤ n−1 splits. By G1(n−1), `D_{R'} ≥ 1`. ✓ Verified 20k trials (incl. r=2 equal-halving and r ≥ 3), 0 failures.

5. **Multi-split structural formula (Lemma 5, PROVED identity).** For 2^n split into M, g_2,…,g_r (M ≥ 2^{n−1} unique largest), rest with ≤ n+1−r ≤ n−1 splits: `D = M − D_rest − D_F + 2 C`, where D_F = D of F = {g_2,…,g_r} (standalone) and C = ∫_0^{2^{n−1}} [j_rest odd]·[j_F odd] (overlap of odd-parity regions). Verified 3000 trials, 0 errors. **Corollary:** `D ≥ 1 ⟺ 2 C ≥ D_rest + D_F + 1 − M`.

6. **Tight config family (Lemma 6, PROVED — sharpness).** `2^n → {2^{n−1}+ε_1, 2^{n−2}+ε_2, …, 1+ε_n}` with `ε_i ≥ 0`, `Σ ε_i = 1`, rest `{2^{n−1},…,1}` unsplit ⟹ sorted interleaves as pairs ⟹ `D = Σ ε_i = 1` (tight). Equal-halving is the ε_i=0 degenerate. Confirmed by 80k-trial n=3 random search: min `D = 1` exactly. This identifies the handle (the bound is sharp, the gap is the overlap inequality).

## Is G1-general closed?

**No — partially closed.** Cases A (2^n unsplit), B (2^n split once), C (2^n split, M=2^{n−1} tie) are PROVED for ALL n, by strong induction. Combined with the n=2 exhaustive brute-force (which covers the n=2 two-mark case directly), this FULLY closes G1 for n ≤ 2, and closes the three structural sub-cases above for every n.

The REMAINING GAP is the multi-split NON-TIE cases:
- **(G1-i)** 2^n split into r ≥ 3 fragments with M > 2^{n−1} (strict, unique largest).
- **(G1-ii)** M = 2^{n−1} (fragment of 2^n) but rest's 2^{n−1} is SPLIT (no tie).
- **(G1-iii)** 2^n split into r ≥ 3 fragments, all < 2^{n−1} (rest contains the full sum 2^n, not a (n−1)-dyadic config).

The open crux is proving the overlap bound `2 C ≥ D_rest + D_F + 1 − M` (Lemma 5 corollary). I verified three naive bounds are all too loose (recorded in the file to prevent retry): (a) sub-measure `C ≤ D_F` lands strictly short; (b) XOR-sum / triangle `D_R ≤ D_rest + W` gives `D ≥ 2M − D_rest − 2^n`, useless at M = 2^{n−1}; (c) the Case-B bound `D ≥ D_rest` is FALSE for multi-split (tight config has `D = 1 < D_rest` typically — e.g. n=3 `{4.37, 4, 2.08, 2, 1.55, 1}`, `D = 1`, `D_rest = 3`). The statement is TRUE (verified n=2,3,4 brute-force); the overlap inequality is the unproved step.

## Was `lemmas/splits-inequality.md` created?

**Yes — as a PARTIAL lemma.** Written to `/home/agentuser/repo/results/imo-2026-03/lemmas/splits-inequality.md`, documenting the full conjecture, the PROVED Cases A/B/C (all n, importable by siblings), the PROVED Lemma 4 (largest-piece decomposition) and Lemma 5 (multi-split formula) identities, and the explicit named GAP (G1-i/ii/iii) with the overlap bound `2 C ≥ …` as the open crux. Siblings can import the proven sub-cases; the gap remains open.

## Gaps remaining

1. **G1 multi-split non-tie (G1-i/ii/iii):** the overlap bound `2 C ≥ D_rest + D_F + 1 − M` for the multi-split non-tie cases. Numerics confirm `D ≥ 1` throughout; the proof of the overlap inequality is the open crux. The tight config family (Lemma 6) saturates the exact bound, confirming the bound is sharp and identifying where the proof must be tight.
2. **G2 (upper bound, general n):** unchanged — conceded (peeling-on-n dead, confirmed by round-1/2 outline-reviewer numerics). Carried by sibling approaches (`pairing-charging` direct partition, `minimax-strategy-family` regime enumeration).

## Computational note

All computations bounded per the anti-stuck rules: ≤ 80k trials per script, n ≤ 4, each script < 5s. Exact-arithmetic (`fractions`). Used computation to VERIFY proved identities (Lemmas 4, 5, Cases A/B/C formulas) and to CONFIRM the tight config family — not as a proof step.

## Per-role rule learned

When a clean inductive sub-case (single-split Case B) closes but the multi-split generalization does not, FIRST derive the exact structural identity (Lemma 5: `D = M − D_rest − D_F + 2C`) before attempting the bound — the identity tells you precisely which inequality (the overlap `2 C ≥ …`) is the crux, and identifies the tight config (Lemma 6) that saturates it, preventing wasted effort on naive bounds (sub-measure, triangle, `D ≥ D_rest`) that are all too loose.
