# imo-2026-03 — G2-upper lens (pairing mechanism / upper-bound wall)

Scouting the **Xiang upper bound for ARBITRARY Liu marks**: prove `D := S_odd − S_even ≤ 1/D_n` (`D_n = 2^{n+1}−1`) for every Liu config, using ≤ n Xiang marks. Answer `c(n) = 2^n/D_n` is verified; the wall is the arbitrary-marks upper bound. All claims below are supported by exact rational/parity argument + numerics; conjectures labelled.

## Distinct openings (each a different attack the outliner could build)

1. **Parity-integral XOR framework (the cleanest handle).** `D = ∫_0^∞ [j(t) odd] dt` (certified `lemmas/greedy-alternating.md`-adjacent, proved in dyadic-induction §2). A split of piece `p` into `u ≥ v` changes `j(t)` by `+1` on `[0,v)`, `0` on `[v,u)`, `−1` on `[u,p)`. Hence it **toggles parity** on `[0,v) ∪ [u,p)` (two intervals of length `v` each). Equal-split (`v=u=p/2`) toggles `[0,p)`; barely-split (`v→0`) toggles `≈∅`. So `D_final = ∫(f ⊕ h)` where `f = [j_Liu odd]` and `h = XOR of split-toggles`. This reduces the upper bound to: *choose ≤ n splits whose toggle-XOR drives `∫(f⊕h) ≤ 1/D_n`.* Concrete, computable, and bypasses the sorted-order interleaving mess. This is the frame to build a charging argument in.

2. **Peeling lemma (the additivity result — VERIFIED, unconditional).** Split `p_1 → p_{n+1} + (p_1 − p_{n+1})`. The two `p_{n+1}`'s (new + original) contribute `+2` to `j(t)` on `[0, p_{n+1})`, which is *even*, so **parity is unchanged**: `D_final = D_rest` EXACTLY, where `rest = {p_2,…,p_n, p_1 − p_{n+1}}` (n pieces, total `1 − 2 p_{n+1}`). Verified on 9 configs (incl. dyadic n=2,3 and non-dyadic, incl. `p_1 < 2 p_{n+1}` cases — the "no interleaving" condition I first assumed is NOT needed; the parity argument is unconditional). Generalizes: split `p_1 → p_j + (p_1 − p_j)` for ANY `j`, creating pair `(p_j, p_j)`, `D_final = D_rest` on `rest = {all pieces except p_1, p_j} ∪ {p_1 − p_j}`. This is the one place where D is genuinely additive, and it's the natural inductive step.

3. **Strategy A (Y-split the largest, D = smallest piece).** Split `p_1` (using n marks) into `p_2 + p_3 + … + p_n + h + h` with `h = (p_1 − Σ_{2..n} p_i)/2 = (2 p_1 + p_{n+1} − 1)/2`. Pairs `(p_2,p_2),…,(p_n,p_n),(h,h)` are internally equal ⇒ always adjacent in sorted order ⇒ each cancels in D. Leftover = `p_{n+1}`. **D = p_{n+1}, always valid** (needs only `h ≥ 0`, i.e. `2 p_1 + p_{n+1} ≥ 1`). Tight at dyadic (`p_{n+1} = 1/D_n`).

4. **Strategy B′ (1-mark barely-match, D = |2 p_1 − 1|).** Split `p_1 → p_2 + (p_1 − p_2)` (1 mark). Pairs `(p_2, p_2)` (new + original) cancel; remaining two pieces `(p_1 − p_2)` and `p_3` (plus deeper pieces) pair up. For n=2 this gives `D = |p_3 − (p_1 − p_2)| = |1 − 2 p_1|`. **Always valid, no `p_1 ≥ 1/2` condition** (the prior "Strategy B needs p_1 ≥ 1/2" was too narrow — B′ achieves `|2 p_1 − 1|` for all p_1 with 1 mark). Tight at dyadic (`|2·2^n/D_n − 1| = 1/D_n`).

5. **Strategy C (equal-split one piece, leave two unsplit, D = |p_a − p_b|).** Equal-split `p_k` (1 mark), leave `p_a, p_b` unsplit. Parity-XOR gives `D_final = |p_a − p_b|` (clean derivation via the XOR framework: `s_S = f ⊕ [p_a > t] ⊕ [p_b > t]`, so `f ⊕ s_S = [p_a > t] ⊕ [p_b > t]`, measure `|p_a − p_b|`). Uses only 1 mark; Xiang can pick the closest pair.

6. **The dyadic config is the unique tight point (conjecture, strong numerics).** Maximin grid search (60×60 Liu, 200-grid Xiang) for n=2 found worst Liu `≈ (0.573, 0.280, 0.146)` ≈ dyadic `(4/7, 2/7, 1/7)`, Xiang-best `D ≈ 0.1438 ≈ 1/7`. So the upper bound is tight ONLY at dyadic; everywhere else there is slack. This means: the proof must be *exactly tight at dyadic* (no slack) and *loose elsewhere* — a construction that is loose at dyadic is dead.

7. **Recursion route (1/c(n) = 1/c(n−1) + 1/2^n) — DOES peeling realize it?** The recursion is arithmetically exact (certified dyadic-induction §3). Peeling-smallest realizes `D_final = D_rest` (exact), and by induction `D_rest ≤ (1 − 2 p_{n+1})/D_{n-1}`. This is ≤ `1/D_n` iff `p_{n+1} ≥ c(n)/2 = 2^{n-1}/D_n`. So peeling+induction closes the bound **only when the smallest piece is large** (`≥ c(n)/2`). For dyadic n=3 (`p_4 = 1/15 < 4/15 = c(3)/2`), peeling-smallest gives `D_rest = 1/3 ≫ 1/15` — the induction is *too loose* to be tight at dyadic. **The recursion is NOT realized by peeling-smallest for n ≥ 3.** A different recursive step (or a stronger inductive hypothesis capturing the rest's structure) is needed.

## Candidate technique(s)

- **Parity-integral + XOR-toggle charging** (opening 1): the cleanest reduction; the proof burden is "choose splits whose toggle-XOR caps `∫(f⊕h)`." Name: `D = ∫[j odd]` (KB: *Double counting* / *Invariants & monovariants*).
- **Equal-pair peeling + induction** (opening 2): the only exact-additivity handle. Tight bound needs a stronger hypothesis than "worst-case rest."
- **Adaptive strategy menu + case analysis** (openings 3–5): proved to suffice for n=2 (see below), but INSUFFICIENT for n ≥ 3.
- **Amortized potential / linear-invariant** (a la aimo-0019, opening 1 crux): maintain a potential `Φ ≤ α·(progress)` across splits, charge each toggle against the budget `1/D_n`. Most promising for a UNIFIED n-general argument.

## Cheap-kill candidates

- **The dyadic config pins the target exactly** — any upper-bound argument must reproduce `D = 1/D_n` there with zero slack. This kills any "≤ with slack" construction (e.g. the alternating-potential dyadic-decrement dead-end that capped `D ≤ 1/2^n`, factor-2 short).
- **n=2 menu check (VERIFIED):** `min(p_3, |2 p_1−1|, |p_2−p_3|, |p_1−p_2|, |p_1−p_3|) ≤ 1/7` over a 600² grid, worst `0.1417 ≤ 1/7` at the dyadic point. So for n=2 the simple menu {A, B′, C-variants} SUFFICES and is tight at dyadic. (A proof for n=2 is thus a finite casework on which strategy wins.)
- **n=3 menu FAILS:** same menu over n=3 gives worst `0.099 > 1/15 = 0.0667` (ratio 1.48) at a non-dyadic config `≈ (0.41, 0.30, 0.20, 0.10)`. So n ≥ 3 *cannot* be closed by a fixed menu of 1–2-mark strategies; it needs the full n-mark adaptive refinement or a unified potential.

## Knowledge-base entries to use

- **Invariants & monovariants** (the parity-integral `D = ∫[j odd]` is the invariant; toggles are the moves).
- **Double counting** (the XOR-toggle accounting: count `∫(f⊕h)` two ways).
- **Constructive vs. existence** — the upper bound needs a *constructive* Xiang strategy (exhibit the marks), not just existence.
- **Induction** (structural, on n) — the peeling recursion; but see circularity trap below.
- **Pigeonhole / extremal** (for the menu sufficiency at n=2: among 3 pieces two are within `1/7`-range of some strategy).

## Analogous past problems (cruxes)

1. **aimo-0388** (coins into two equal stacks, `|diff| ≤ 50/51`). Crux: *"Split a sorted sequence into two stacks by pairing consecutive elements so each pair's contribution to the difference is a non-positive gap, leaving only isolated boundary terms."* This is the EXACT mechanism of `D = Σ(a_{2k−1} − a_{2k}) + leftover` (deficit-of-adjacent-pairs + leftover). The analogy: aimo-0388 pairs the GIVEN sorted multiset; our Xiang gets to REFINE it (split) to engineer the pairs. Strongest structural analogy found.
2. **aimo-0596** (1024 cards, XOR/involution pairing). Crux: *"Pair the ground set by a fixed nonzero translation `X ↦ X△B`; any transversal's XOR lands in `{0, B}`; responder mirrors with the partner."* Analogy: the parity-XOR framework (opening 1) is the measure-theoretic cousin — responder (Xiang) picks toggles (splits) to drive the parity-XOR into a 2-element coset of small measure. The "responder answers with the involution-partner" structure maps to "Xiang answers Liu's piece with a matching split."
3. **aimo-0019** (painting game on the real line with dyadic intervals). Crux: *"Maintain a linear potential bounding cumulative resource by a constant times progress, proved by amortized induction that charges each frontier advance against the pieces it absorbs"* (potential `ink ≤ 3·x_r`). Analogy: a linear potential `D ≤ α·(something)` maintained across Xiang's splits, charging each toggle against the budget `1/D_n`. This is the template for a UNIFIED n-general charging argument (vs. the menu that fails for n=3). Closest in *spirit* (dyadic intervals + amortized potential) even if the game differs.
4. **aimo-0461** (knight/queen placement, `K = 100`). Crux: *"Partition the conflict graph into small identical components each holding ≤ 1 piece; responder occupies the antipodal vertex in the same component."* Analogy: partition the level range into "domino" intervals, Xiang's mark is the antipodal response. Already cited in pairing-charging §4.2; the antipodal-response structure maps to the parity-toggle pairs `[0,v) ∪ [u,p)` (two antipodal intervals of the split).

(Note: aimo-0117, already used for the LOWER bound via "dyadic tower, largest exceeds sum of rest," is NOT a candidate for the upper bound — it's Liu's side.)

## Prior progress (current best, G2-specific)

- **n=1 upper bound FULLY PROVED** (pairing-charging §4.1, dyadic-induction §5.1): two-regime dichotomy, `c(1)=2/3`. The n=1 case IS the pairing mechanism in cleanest form (equal-split if `A ≥ 2/3`, barely-split otherwise).
- **D-reduction PROVED**: `S_odd ≤ 2^n/D_n ⟺ D ≤ 1/D_n`. Pins the exact charging target.
- **Parity-integral reformulation PROVED** (dyadic-induction §2): `D = ∫[j(t) odd] dt`. The cleanest handle for the upper bound (opening 1).
- **Recursion identity PROVED**: `1/c(n) = 1/c(n−1) + 1/2^n`. Arithmetically exact; realizing it via a strategy is the open crux.
- **G2-general OPEN for n ≥ 2** (built only for n=1). The pairing-charging approach's defining bet; honestly flagged as "if no construction exists for arbitrary marks, the approach dies."

## Dead ends (do not retry)

- **Surrogate-adversary restricted strategies** (R_n, R_n', threshold-gated): all falsified for n ≥ 2, collapse to pairing. (round 1, surrogate builder+reviewer.)
- **Naive dyadic-decrement telescope** (alternating-potential's distinctive crux): caps `D ≤ 1/2^n`, factor-2 short of `1/D_n ≈ 1/2^{n+1}`. CONFIRMED dead-end. (round 1.)
- **Equal-halving as the assumed minimizer for the upper bound**: numerics show the optimal Xiang split is UNEQUAL on dyadic n=2 (`4/7 → 0.425 + 0.146`, not `2/7 + 2/7`) and pairing-like on random configs. NEVER assume equal-split; derive split points. (round 1, reviewer.)
- **A fixed menu of 1–2-mark strategies for n ≥ 3**: VERIFIED insufficient (n=3 worst `0.099 > 1/15`). Do NOT attempt to close n ≥ 3 with {A, B′, C} alone — need the full n-mark refinement or a unified potential.
- **Peeling-smallest + naive worst-case induction for n ≥ 3**: the inductive bound `(1 − 2 p_{n+1})/D_{n-1}` is LOOSE (dyadic n=3 gives `D_rest = 1/3` vs target `1/15`). Peeling is exact for the split (`D_final = D_rest`), but the induction hypothesis is too weak. A stronger hypothesis (capturing that the rest config is *derived*, not worst-case) is required.

## Small-case / intuition notes (conjectures, labelled)

- **Conjecture (tight point):** the dyadic config `(1,2,…,2^n)/D_n` is the UNIQUE maximizer of Xiang's best `D` (= `1/D_n`). Strong numerics for n=2 (worst Liu ≈ dyadic). Implies: any correct upper-bound proof is tight EXACTLY at dyadic and loose elsewhere — slack is fine, but dyadic must be hit with equality.
- **Conjecture (peeling + Strategy A/B′ combine to close n=2):** verified by grid that `min(p_3, |2 p_1−1|, |p_a − p_b|) ≤ 1/7` for all n=2 Liu. A rigorous n=2 proof is a finite casework. (For n ≥ 3 the analogous claim is FALSE — need richer strategies.)
- **Intuition for the unified n-general proof:** the recursion `1/c(n) = 1/c(n−1) + 1/2^n` is a *parallel/harmonic* combination (`c(n) = c(n−1)·2^n/(c(n−1)+2^n)`). This suggests Xiang's strategy *parallel-combines* a "c(n−1)-density sub-problem" (mass `2^n/(c(n−1)+2^n)`, handled by induction) with a "2^n-density piece" (mass `c(n−1)/(c(n−1)+2^n)`, paired off contributing 0 to D). Realizing this split cleanly (despite D's non-additivity) is the crux — the peeling lemma is the one place additivity holds for free, so the parallel combination should be built AROUND a peeling step.
- **Circularity trap (per dispatch):** a partition that only works for the dyadic config is dead. The strategies A, B′, C, and the peeling lemma all work for ARBITRARY Liu marks (verified on non-dyadic configs: `D_final = D_rest` holds unconditionally; `D = p_{n+1}`, `D = |2 p_1−1|`, `D = |p_a−p_b|` hold for all configs). What makes a partition work for ALL configs is the **parity-unchanged property** (an equal pair contributes `+2` to `j`, even, parity-neutral) — this is config-independent. The gap is not circularity of any single strategy; it is that no FIXED strategy always hits `1/D_n` for n ≥ 3, so the proof must ADAPT (choose strategy by regime) or use a unified potential.
- **Most promising route to a rigorous arbitrary-marks upper bound:** (a) SHORT-TERM — close n=2 via the {A, B′, C} casework (finite, verified sufficient); (b) LONG-TERM — build the amortized-potential argument (a la aimo-0019) on the parity-integral XOR framework, with the peeling lemma as the inductive engine and a strengthened hypothesis that captures the rest config's structure. The recursion `1/c(n) = 1/c(n−1) + 1/2^n` is the target the potential must realize.

## Where it risks circularity

- A proof that says "peel, then by induction `D_rest ≤ 1/D_n`" is **circular** unless the inductive hypothesis is STRONGER than the original claim (the rest has structure: its largest piece `p_1 − p_j` is derived from Liu's, not arbitrary). The naive hypothesis "any n-piece config has `D ≤ 1/D_{n-1}`" is too weak (gives `(1−2p_j)/D_{n-1}`, loose). The outliner must either (i) find a strengthened hypothesis that transfers tightly, or (ii) abandon the peeling-induction for a direct amortized-potential argument.
- A construction that uses ALL n marks only on `p_1` (Strategy A / B generalized) risks being tight ONLY at dyadic and loose elsewhere — but that's actually FINE (slack elsewhere is allowed); the risk is the reverse, being loose at dyadic.
