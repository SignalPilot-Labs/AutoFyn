# Round-4 proof-outliner field — imo-2026-03 (Chu-Han war)

Target claim (whole problem): `c(n) = 2^n/(2^{n+1}−1)`, via BOTH a lower bound (Liu's dyadic config forces `D ≥ 1/D_n` after any ≤ n Xiang splits) AND an upper bound (for arbitrary Liu marks, a Xiang strategy holds `D ≤ 1/D_n`), with tight construction. Two open walls: **G1** (lower, n≥3) = overlap bound `2C ≥ D_{R_0}+D_F+1−M`; **G2** (upper, n≥3) = flat regime `p_{n+1} > 1/D_n`. Certified imports available: `greedy-alternating`, `parity-integral`, `peeling`, `equal-halve-n-largest`, `splits-inequality` (PARTIAL — Cases A/B/C + Lemma 5 identity).

---

## dyadic-induction: REVISE
Target: whole problem (lower bound G1-general is this approach's load-bearing gap; upper bound G2 conceded and imported from siblings once they close).
Technique: parity-integral `D = ∫[j odd]` + **union-measure / dyadic-tiling rigidity** (measure-extremizer Opening A), replacing the loose XOR-overlap chase. The Lemma-5 identity `D = M + D_{R_0} + D_F − 2|O_{R_0} ∪ O_F|` (verified exact) turns G1 into "shave exactly 1 unit off the trivial union bound `|union| ≤ 2^{n−1}`"; the trivial bound is off by exactly 1 because `O_{R_0}` is a rigid alternating-dyadic-interval tiling whose complement is a superincreasing block pattern that `O_F` (odd region of a ≤ n-piece partition of `W`) cannot tile perfectly.
Skeleton:
  1. Import `lemmas/parity-integral.md`, `lemmas/peeling.md`, `lemmas/splits-inequality.md` (Cases A/B/C + Lemma 5 identity). Re-state the gap as the union bound `|O_{R_0} ∪ O_F| ≤ (M + D_{R_0} + D_F − 1)/2`.
  2. **G1-i (M > 2^{n−1}, unique largest):** exploit that `O_{R_0}` = union of alternating dyadic intervals `[2^k, 2^{k+1})` (k of the right parity), a fixed tiling of `[0, 2^{n−1}]`. Its complement is a superincreasing-block pattern (each complement block > sum of smaller complement blocks). `O_F ⊆ [0, W]` is the odd-parity set of a partition of `W ≤ 2^{n−1}` into ≤ n real pieces. Prove `O_F` cannot cover the complement perfectly: at each dyadic edge `2^k`, the superincreasing gap forces a deficit ≥ 1 unit cumulatively. — by inclusion–exclusion + the superincreasing-block structure of the complement.
  3. **G1-ii (M = 2^{n−1}, rest's 2^{n−1} SPLIT, no tie):** re-derive the union bound with `max(R) < 2^{n−1}` (top band shifts); same tiling argument on the shifted support. — by the parity-integral top-band shift + tiling deficit.
  4. **G1-iii (all fragments of 2^n < 2^{n−1}):** largest final piece comes from a smaller original; reinterpret the whole config as an `(n−1)`-dyadic instance with the sum-`2^n` fragments folded into the rest, reduce to G1(n−1). — by reduction + induction.
  5. **Tight case (Lemma 6 family):** verify the bound saturates with deficit exactly 1 via `ε_i`-interleaving bookkeeping at the dyadic edges. — exact arithmetic.
  6. G2 (upper) stays conceded; import a sibling's certified upper bound for the flat regime when available.
Key lemmas (claim + one-line mechanism):
  - `|O_{R_0} ∪ O_F| ≤ (M + D_{R_0} + D_F − 1)/2` — because `O_{R_0}` is a rigid alternating-dyadic tiling whose superincreasing complement blocks cannot be perfectly covered by the odd region of any ≤ n-piece partition of `W` (each dyadic edge `2^k` leaks ≥ its superincreasing surplus).
  - G1-iii reduction — because when all fragments of `2^n` are `< 2^{n−1}`, the largest final piece is `2^{n−1}` (or its sub-piece) and the config re-sorts to an `(n−1)`-dyadic instance with ≤ n−1 effective splits on the smaller tower.
Open gaps: the "deficit ≥ 1" bookkeeping at the dyadic edges (G1-i,ii); the G1-iii reduction's split accounting; G2 (conceded, imported).
Cases to cover: G1-i (M > 2^{n−1}), G1-ii (M = 2^{n−1}, rest split), G1-iii (all fragments < 2^{n−1}).
Watch out for: the union-measure bound is a RESTATEMENT of the overlap bound (measure-extremizer explorer concedes this) — the win must come from the dyadic-tiling rigidity making the "deficit ≥ 1" bookkeeping clean, NOT from a new inequality. The tight Lemma-6 family is measure-zero; the proof must be exact (interleaving), not approximate. Do NOT retry the three naive bounds (sub-measure `C ≤ D_F`, XOR-sum triangle, `D ≥ D_{R_0}`) — all recorded too loose.

## pairing-charging: ADVANCE
Target: whole problem; this approach's defining crux is G2-flat (n≥3, `p_{n+1} > 1/D_n`). Lower bound G1 imported from `splits-inequality` once certified.
Technique: explicit adaptive n-mark **pairing/domino partition** + **unique-worst-at-dyadic** structural handle (proved n=2 by minimax-strategy-family §4; conjectured n≥3). The n=2 M5 split-to-match member giving `|2p_1−1|` (surplus telescope) is the generalization seed.
Skeleton:
  1. Import `greedy-alternating`, `parity-integral`, `peeling`, `equal-halve-n-largest` (closes spiky regime `p_{n+1} ≤ 1/D_n` for all n), `splits-inequality` (Cases A/B/C; G1 gap shared).
  2. **G2-flat, n≥3:** for Liu configs with `p_{n+1} > 1/D_n` (flat), construct an adaptive n-mark Xiang reply that drives `D ≤ 1/D_n`. Two prongs to advance:
     (a) **Surplus-chain telescope:** generalize the n=2 M5 split-to-match move `p_1 → p_2 + (p_1−p_2)` (creates a copy of `p_2`, peeling-neutrality removes the pair, surplus `p_1−p_2` telescopes). For n≥3, chain: split `p_1 → p_2 + r_1`, `r_1 → p_3 + r_2`, …, creating copy-pairs `(p_2,p_2),(p_3,p_3),…` that cancel in D, leaving a final lone surplus `r_{n−1}` whose size is forced ≤ `1/D_n` by the flat-regime constraint `p_{n+1} > 1/D_n` plus the sum constraint. — by peeling lemma iterated + the flat-config surplus bound.
     (b) **Unique-worst-at-dyadic for n≥3:** if proved, the construction only needs to be TIGHT at dyadic and slack elsewhere; this localizes the casework. Attack by the same `Σ (gaps) = 1/D_n` accounting that proved n=2.
  3. n=2 upper bound (PROVED) and Lemma 4 (spiky regime, all n) stand as the certified partial upper bound.
  4. G1 lower bound: keep proved Cases A/B + n=2; import full `splits-inequality` once the multi-split overlap bound (sibling dyadic-induction) closes.
Key lemmas:
  - Surplus-chain telescope: a chain of split-to-match moves `p_1 → p_2 + r_1 → …` creates `n−1` copy-pairs (D-neutral by peeling) and a final lone `r_{n−1} = p_1 − p_2 − p_3 − … − p_n`; in the flat regime `p_{n+1} > 1/D_n` + sum constraint `Σ p_i = 1` force `r_{n−1} ≤ 1/D_n`. — because `r_{n−1} = 1 − p_{n+1} − 2Σ_{i<n} p_i ... ` (the chain identity) and the flat constraint pins the surplus.
  - Unique-worst-at-dyadic (n≥3): the dyadic config is the unique maximizer of `min_Xiang D`. — by the same `Σ`-slack = `1/D_n` accounting that proved n=2 in minimax-strategy-family §4.
Open gaps: the surplus-chain telescope's exact D-formula for non-equal splits (does the lone surplus land at an odd rank for arbitrary Liu configs?); the unique-worst-at-dyadic proof for n≥3; the full G1 import dependency.
Cases to cover: flat regime `p_{n+1} > 1/D_n` (sub-cased by how flat — near-uniform vs moderately superincreasing); < n Liu marks.
Watch out for: the surplus chain may NOT land the lone at an odd rank for arbitrary (non-dyadic) Liu configs — the rank-parity argument of Lemma 4 relies on n equal pairs; a chain of split-to-match moves creates pairs of UNEQUAL pieces `(p_i, copy of p_i)` only if the copy equals the original (it does — split-to-match makes them equal). Verify the rank argument transfers. A fixed 1–2-mark menu is VERIFIED insufficient for n=3 (0.097 > 1/15); the chain MUST use all n marks.

## minimax-strategy-family: REVISE
Target: whole problem; this approach's distinctive crux is G2-flat via a minimax over an adaptive family with non-pairing ties at dyadic (n=2 PROVED with M3/M5 non-pairing ties). Lower bound G1 imported.
Technique: **minimax over an adaptive n-mark family** whose members' D-values are regime-independent (parity-XOR) and tie at dyadic. The n=2 M5 split-to-match member is the seed for an n-mark **split-to-match chain** that telescopes surplus to `1/D_n`.
Skeleton:
  1. **FIX the M2 XOR-derivation bug** (reviewer-flagged, round 3): re-derive M2's D-value by direct sort-computation (correct value `p_1 − p_2`, NOT `p_1 − p_3`); reconcile §3.1 derivation + §3 menu statement + §3.2 contradiction table to the correct `p_1 − p_2`. One-line XOR fix `0⊕0=0` (not 1) on `[p_3,p_2)`. — by direct sort-computation per the per-role rule (verify toggle/XOR by sorting).
  2. n=2 upper bound (theorem stands; M2's menu entry corrected to `p_1−p_2`, contradiction proof unchanged since §3.2 already used `p_1−p_2`).
  3. **G2-flat n≥3 (the crux):** generalize the M5 split-to-match move to a chain `p_1 → p_2 + r_1`, `r_1 → p_3 + r_2`, … (n−1 marks, creating `n−1` copy-pairs that cancel, lone `r_{n−1}`). The family member's D-value = `r_{n−1}` (regime-independent by parity-XOR, like M5's `|2p_1−1|`). Add a "barely-split the largest" member and an "equal-halve n-largest" member (Lemma 4, `D = p_{n+1}`). The minimax over {lone-surplus `r_{n−1}`, `p_{n+1}`, …} ≤ `1/D_n` by a generalization of the n=2 2-case contradiction.
  4. **Unique-worst-at-dyadic n≥3** (conjecture; proved n=2 §4): if proved, the family is tight only at dyadic.
  5. G1 lower bound: import `splits-inequality` once certified.
Key lemmas:
  - Split-to-match chain D-value: the chain `p_1 → p_2+r_1 → p_3+r_2 → …` gives `D = r_{n−1}` regime-independently — because each copy-pair `(p_i, copy)` is D-neutral (peeling lemma), leaving the lone `r_{n−1}` at an odd rank (the chain creates `n−1` equal pairs + 1 lone, mirroring Lemma 4's structure).
  - Minimax ≤ `1/D_n`: in the flat regime `p_{n+1} > 1/D_n`, the chain surplus `r_{n−1}` is small (≤ `1/D_n`); in the spiky regime `p_{n+1} ≤ 1/D_n`, Lemma 4 closes. So `min(r_{n−1}, p_{n+1}) ≤ 1/D_n`. — by the sum constraint splitting the regimes.
Open gaps: the chain's lone-rank-parity for non-dyadic configs (does it always land odd?); the minimax contradiction proof for n≥3 (generalize the n=2 2-case); unique-worst-at-dyadic n≥3; M2 bug fix.
Cases to cover: flat vs spiky regime; n-mark chain vs fewer marks.
Watch out for: the chain uses n−1 marks, leaving 1 mark slack — that slack must be assigned (e.g. a barely-split to break ties) or the family undershoots the budget. The fixed 1–2-mark menu is verified insufficient for n=3 — the chain MUST be the n-mark adaptive member. The M2 fix is load-bearing for the n=2 theorem's internal consistency but does NOT change the n=2 bound value (the menu and contradiction already used the correct `p_1−p_2`).

## collapse-theorem: NEW
Target: whole problem; attacks G2 (the upper bound) from **Liu's side** via a minimax/convexity ("worst Liu = dyadic" collapse) argument, GENUINELY ORTHOGONAL to pairing. G1 lower bound imported from `splits-inequality`.
Technique: **flattening / Robin-Hood lemma on Liu's config** — prove that transferring mass from Liu's largest piece to his smallest (making the config less superincreasing) does NOT increase `min_Xiang D`. Iterating, the maximizer of `min_Xiang D` is at the most-superincreasing extreme = the dyadic config, where `min_Xiang D = 1/D_n` (G1 / equal-halve-n-largest). Hence `max_Liu min_Xiang D = 1/D_n`, folding G2 into G1.
Skeleton:
  1. Import `greedy-alternating`, `parity-integral`, `equal-halve-n-largest` (gives `min_Xiang D(dyadic) = 1/D_n`, the floor of the collapse), `splits-inequality` (G1).
  2. **Flattening lemma (the load-bearing hard step):** for Liu configs `P = (p_1 ≥ … ≥ p_{n+1})`, let `P'` be a Robin-Hood perturbation: `p_1 → p_1 − δ`, `p_{n+1} → p_{n+1} + δ` (δ small, preserving sort). Then `min_Xiang D(P') ≤ min_Xiang D(P)`. — mechanism: the Xiang reply that minimized D on P, applied to P', gives a D-value no larger, because flattening shrinks the odd-position surplus (the largest piece contributes at odd rank; shrinking it reduces the maximum achievable surplus faster than the smallest-piece growth can compensate). Concretely: via the parity-integral, `D_Xiang(P)` is a min-of-linear-forms in the piece lengths; flattening the largest piece reduces every linear form with a +`p_1` coefficient by δ, while the +`p_{n+1}` coefficient forms gain δ; the min-of-forms is concave-ish in the flattening direction (TBD — this is the risk).
  3. **Iterate to the extreme:** the flattening lemma pushes the maximizer to the boundary of the Liu-config simplex where further flattening is impossible. The most-superincreasing extreme is the dyadic config (largest > sum of rest, by exactly `1/D_n`). At dyadic, `min_Xiang D = 1/D_n` (equal-halve-n-largest, tight). So `max_Liu min_Xiang D = 1/D_n`.
  4. Combine: upper bound `c(n) ≤ 2^n/D_n` follows; lower bound by G1 (imported).
  5. If the flattening lemma fails, the approach dies honestly — flag as high-risk, no partial credit on G2.
Key lemmas:
  - Flattening lemma: `min_Xiang D` is non-decreasing under superincreasing-ification of Liu's config (Robin-Hood in reverse). — because `D_Xiang(P) = min_s D(P, s)` is a min of linear forms in `P`, and the dyadic direction is the superincreasing extreme where the min is largest.
  - Maximixer-at-dyadic: the flattening-monotone functional attains its max at the most-superincreasing config = dyadic. — by iterating the flattening lemma to the simplex boundary (Robin-Hood to the extreme).
Open gaps: the flattening lemma itself (the min-of-linear-forms monotonicity — HIGH RISK, minimax theorems are often harder than the inequality); the boundary characterization (is dyadic really the unique most-superincreasing extreme, or are there other boundary maximizers?).
Cases to cover: Liu configs at the simplex boundary (degenerate piece configs); ties in the sort order.
Watch out for: this is a minimax theorem and may be STRICTLY HARDER than G2 itself (the explorer's honest warning). The flattening monotonicity is NOT verified numerically in a clean form (explorer could not confirm within budget). If the min-of-linear-forms is NOT monotone in the flattening direction, the approach dies — do NOT paper over. Distinctiveness: this is the ONLY approach attacking G2 without constructing a Xiang partition; it stays far from pairing.

## alternating-potential: ADVANCE
Target: whole problem; upper bound CONCEDED (factor-of-2 wall, sound, do not retry). Lower bound G1 advanced via a **band-parity / t-axis decomposition** lens (telescoping-potential explorer Opening C) — a fresh angle on the shared G1 gap, distinct from dyadic-induction's XOR-overlap chase.
Technique: **band-parity decomposition of the parity integral** — decompose `D = ∫[j odd] dt` into bands `(g_{k−1}, g_k]` (dyadic-tower units). At Liu's unsplit dyadic config, band k has length `2^{k−1}/D_n` and `j = k`, contributing `2^{k−1}/D_n · [k odd]`; `D_init = (1/D_n)·Σ_{k odd} 2^{k−1} ≥ 1/D_n` trivially. Xiang's splits fragment the bands; G1 = "at least one odd band above the bottom survives fragmentation."
Skeleton:
  1. Import `parity-integral`, `peeling`, `splits-inequality` (Cases A/B/C + Lemma 5 identity).
  2. **Band-parity cheap kill for Case A:** `D_init = (1/D_n)·Σ_{k odd} 2^{k−1} ≥ 1/D_n` (at least the bottom band `k=0` is odd). Short-circuits Case A structurally. — by direct band decomposition.
  3. **G1-ii band handle (split rest):** when the rest's `2^{n−1}` is split, the band `(g_{n−2}, g_{n−1}]` fragments; prove the fragmented parity still leaves an odd-band survivor at level ≥ 1. — by the even-rank-insertion sub-lemma (proved round 1) + band-parity survival.
  4. **Unification with the overlap bound:** the multi-split fragmentation reduces to the SAME overlap bound `2C ≥ D_{R_0}+D_F+1−M` in band language (explorer concedes this is a re-lensing, not a bypass). Keep as a cross-check / alternative bookkeeping for the G1-ii sub-case specifically, where the band-parity survival may be cleaner than the XOR-overlap form.
  5. G2 upper bound: conceded (factor-of-2 wall, sound); carried by siblings.
Key lemmas:
  - Band-parity survival: after ≤ n splits of the dyadic config, at least one odd band above the bottom survives at level ≥ 1, so `D ≥ 1/D_n`. — because each split fragments one band but the superincreasing structure ensures the odd-parity telescope `Σ_{k odd} 2^{k−1} → ≥ 1` survives (equivalent to the overlap bound, restated).
  - Even-rank-insertion (proved round 1): handles the "split the largest once, rest unsplit" sub-case — by direct rank-parity.
Open gaps: the band-parity survival proof for multi-split (reduces to the overlap bound — explorer concedes NOT a bypass); G2 (conceded).
Cases to cover: G1-ii (split rest) is this approach's specific target sub-case; other G1 sub-cases imported from `splits-inequality`.
Watch out for: the band-parity route is a RE-LENSING of the overlap bound, not a bypass (telescoping-potential explorer concedes this). Its value is cleaner bookkeeping for the G1-ii split-rest sub-case, NOT a new wall-cracker. Do NOT retry linear potentials (factor-of-2 wall, confirmed dead). Do NOT retry aimo-0019's amortized-linear template (no dyadic-distinctness analog). The approach's main contribution is the certified lower-bound machinery (peeling corollary, even-rank-insertion) already in the bank.

---

## Field-level diversity note

The field stays broad and does NOT collapse to pairing. Of the five approaches: **dyadic-induction** (G1 via parity-integral + union-measure/tiling), **alternating-potential** (G1 via band-parity t-axis decomposition) attack the LOWER bound via two different lenses on the same overlap wall (XOR-overlap vs band-parity). **pairing-charging** (G2 via explicit adaptive domino partition), **minimax-strategy-family** (G2 via minimax over an adaptive split-to-match chain family, with non-pairing ties at dyadic), and **collapse-theorem** (G2 via Liu-side minimax/flattening — NO Xiang partition constructed) attack the UPPER bound via three genuinely different mechanisms. The collapse theorem is the field's genuinely orthogonal G2 route (the only one that does not build a Xiang partition); minimax-strategy-family's split-to-match chain is non-pairing (the n=2 proof already showed M3/M5 non-pairing ties at dyadic). The two G1 attacks use different frames (XOR-overlap bookkeeping vs band-parity survival) on different sub-cases (dyadic-induction owns G1-i/iii; alternating-potential owns G1-ii split-rest). No two approaches share the same gap-fill on the same sub-case (single-gap trap avoided). The field's risk concentration is the flattening lemma of collapse-theorem (high-risk, may die) — if it dies, the field still has pairing + minimax-family on G2 and dyadic-induction on G1.
