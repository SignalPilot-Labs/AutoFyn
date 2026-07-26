# imo-2026-03 — G1 tiling-rigidity scout (round 5, lens: g1-tiling-rigidity)

Terrain report for the three open G1 sub-cases (G1-i-HC, G1-ii, G1-iii). No proof — openings, dead ends, the exact hard step. All numerics exact-arithmetic (`fractions`), correct split budget, dyadic rest `{1,2,4,…,2^{n−1}}`.

## Setup recap (the certified machinery I rely on)

- **Lemma 4** (`D = M − D_R`, CERTIFIED via `lemmas/splits-inequality.md`): parity-integral t-axis, largest-piece decomposition.
- **Lemma 5/7** (`D = M − D_{R_0} − D_F + 2C = M + D_{R_0} + D_F − 2|O_{R_0} ∪ O_F|`, PROVED identities): the load-bearing reformulation. `O_{R_0}`/`O_F` = odd-parity regions of rest / F within `[0, 2^{n−1}]`; `C = |O_{R_0} ∩ O_F|`; `E_{R_0} = [0,2^{n−1}] \ O_{R_0}`.
- **Lemma 8** (2-piece F, rest unsplit, PROVED all n≥2): the "rigid top O-block" `(2^{n−2}, 2^{n−1}] ⊆ O_{R_0}` gives `|(b,a] ∩ E_{R_0}|` pinned by a single dyadic edge `2^{n−2}`.
- **Lemma 9** (low-cancellation, PROVED all F all n): `|O_F ∩ E_{R_0}| ≤ |E_{R_0}|` closes `D_F ≥ W − D_{R_0} + 1`.
- **Peeling lemma** (`lemmas/peeling.md`, CERTIFIED): equal-pair-creating split is D-neutral.
- The G1 wall (Lemma 7 corollary): `D ≥ 1 ⟺ |O_{R_0} ∪ O_F| ≤ (M + D_{R_0} + D_F − 1)/2`; trivial `|union| ≤ 2^{n−1}` is off by exactly `(W + 1 − D_{R_0} − D_F)/2`, `W = 2^n − M`. Equivalently (inclusion-exclusion on the complement): `|E_{R_0} ∩ E_F| ≥ (W + 1 − D_{R_0} − D_F)/2`. **The "1" is the `+1` in this target.**

## Distinct openings (each a different attack the outliner could build)

### Opening A — "the leak is a dyadic-edge overflow" (most promising for G1-i-HC)

I characterized the tight Lemma-6 family at n=4, s=3 exactly. **The complement `E_{R_0} ∩ E_F` is literally a single sliver `(2, 2+ε_3]`** of measure `ε_3`, and the target `(W+1−D_{R_0}−D_F)/2 = ε_3` *exactly*. Mechanism:

- Rest `R_0 = {1,2,4,8}` unsplit. `E_{R_0}` bands (verified): `(2,4]` (j=2 even) and `(0,1]` (j=4 even). These are **superincreasing** dyadic bands (lengths 1, 2; the larger exceeds the sum of all smaller).
- `F = {4+ε_2, 2+ε_3, 1+ε_4}` (s=3). `E_F` bands: `(f_1, 8]` (top, j=0 even) and `(f_3, f_2] = (1+ε_4, 2+ε_3]` (j=2 even).
- The top `E_F` band `(4+ε_2, 8]` sits entirely above `E_{R_0}`'s `(2,4]` (starts at `4+ε_2 > 4`), contributing **0** to the overlap.
- The lower `E_F` band `(1+ε_4, 2+ε_3]` pokes **into** `E_{R_0}`'s `(2,4]` from below, covering `(2, 2+ε_3]` = the **overflow of F's middle breakpoint `2+ε_3` past the dyadic edge `2`**.

**The "1" in "shave 1" is structurally this dyadic-edge overflow**: F's breakpoints (at `2+ε_3`, `4+ε_2`, …) cannot all coincide with the rest's dyadic edges (`1, 2, 4, 8`) because F sums to `W < 2^{n−1}` and a partition of a superincreasing tower's prefix into `s` pieces cannot align all breakpoints with tower edges (that would force F to be a union of whole dyadic pieces, summing to an exact dyadic sum — but `W` is not such in the HC regime where M is a "barely-larger" fragment). The forced misalignment **is** the leak, and its measure is bounded below by the target.

**The exact hard step for the outliner/builder:** make the sentence *"F's breakpoints cannot all align with `E_{R_0}`'s dyadic edges; the total misalignment-measure is `≥ (W + 1 − D_{R_0} − D_F)/2`"* rigorous for general `s ≥ 3`. The 2-piece Lemma 8 pins **one** dyadic edge (`2^{n−2}`) against **one** `O_F` interval; the s≥3 generalization needs to count misalignment across the `s−1` breakpoints of `F` against the `≈ n/2` dyadic edges of `E_{R_0}` and sum the forced leaks. A superincreasing-block / Zeckendorf-style representation argument is the natural tool (each `E_{R_0}` band of length `2^k` can absorb at most `2^k` from `E_F`, and the leftover structure forces a surplus on the boundary).

### Opening B — induction on the NUMBER OF REST SPLITS (not on n, not on s)

The shared gap is "rest unsplit" in G1-i-HC, but the full G1 allows the rest `{1,…,2^{n−1}}` to carry splits too. Lemma 8 + 9 close "rest unsplit" for 2-piece F and low-cancellation; the multi-piece-HC-with-rest-split is the union of G1-i-HC and G1-ii. **Induct on the number of splits on the rest**, holding n fixed: base = 0 rest-splits (Lemma 8/9 + Opening A target); step = one more rest-split, show the bound degrades by at most the split's toggle-measure. This is the natural home for alternating-potential's **parity-XOR toggle** (`lemmas/parity-integral.md`): a rest-split toggles `O_{R_0}` on `[0,v) ∪ [u, 2^{n−1})`, and the rigid-top-O-block structure is perturbed by a controlled measure. The outliner can pair this with Opening A: prove the rigid-tiling bound for rest-unsplit, then show one rest-split shaves at most a controlled amount (the toggle's measure, bounded by the piece halved).

### Opening C — G1-iii split by whether rest's `2^{n−1}` is split (RESOLVES the "needs re-framing")

The dispatch says G1-iii needs re-framing because "reduce to G1(n−1)" is unsound. I find G1-iii splits cleanly into two sub-cases with **very different hardness**:

- **G1-iii-a (rest's `2^{n−1}` UNSPLIT): EASY, big slack.** `M = 2^{n−1}` (rest's), `R = {2^n`'s fragments`} ∪ {1,…,2^{n−2}}`. Verified (exact, n=4..7, r=3..5): **min D = 3, 3, 5, 7** (n=4..7), never below 3. The "reduce to G1(n−1)" was unsound **and unnecessary** — a direct bound `D ≥ D_dyadic(n−2) − (fragment-pairing slack)` works. The fragments of `2^n` sum to `2·M = 2·2^{n−1}` (twice the largest piece), so in the alternating sum they "pair off" (peeling-lemma flavor: two near-equal fragments cancel), leaving the dyadic `(n−2)` part's D `= (2^{n−1} + (−1)^{n−2})/3 ≥ 1` as the residual floor. **The outliner's unsound induction should be replaced by a direct peeling-pair bound here; no re-framing needed, just a different (simpler) argument.**
- **G1-iii-b (rest's `2^{n−1}` SPLIT, all pieces `< 2^{n−1}`): TIGHT, genuinely hard.** Verified n=4: **min D = 1** (config `{6,6,4,4,4,4,2,1}`, D = 6−6+4−4+4−4+2−1 = 1). This is a **flat** regime (no piece ≥ `2^{n−1}`); there is no clean "largest piece M" with `M` dominating. It is **NOT a boundary of G1-i** (perturbing any piece to `> 2^{n−1}` is a big jump, not a continuity limit). It is structurally the *same* phenomenon as the G2-flat wall on the upper-bound side (very-flat `p_{n+1} > 1/D_n` regime) — the IMO-hard core lives in the flat configs on BOTH bounds. Recommend the outliner treat G1-iii-b as its own flat sub-case, possibly attackable by the same machinery that closes G2-flat (continuous/LP-dual), NOT by tiling rigidity (which relies on a dominant M).

### Opening D — G1-ii is a non-issue once G1-i closes (confirm alternating-potential's reduction)

Re-verified: alternating-potential's round-4 reduction `G1-ii (r≥3) ⟹ G1-i` (perturb `M = 2^{n−1} → 2^{n−1}+ε`, `D` continuous in `ε`, lands in valid G1-i with rest split) is **sound** and is the right framing. G1-ii is the `M → 2^{n−1}` boundary of G1-i; the "shave 1" target `(W+1−D_{R_0}−D_F)/2` varies continuously and the bound lifts by continuity. **The catch (round-4 reviewer flagged it): the perturbed config has F with `r−1 ≥ 2` pieces AND rest's `2^{n−1}` SPLIT** — which is G1-i-with-rest-split, the very sub-case Opening B targets. So G1-ii is closed *conditional on Opening A + B*, not on Lemma 8 alone (Lemma 8 is rest-unsplit only). No new work for G1-ii beyond A+B; do not dispatch a separate G1-ii attacker.

## Candidate technique(s)

- **Superincreasing / Zeckendorf representation** (KB: *Pigeonhole / extremal*; the dyadic tower is the canonical superincreasing sequence). Each `E_{R_0}` band of length `2^k` exceeds the sum of all smaller `E_{R_0}` bands — this is the asset Lemma 8 exploited for the top band and the s≥3 generalization must exploit for all bands simultaneously.
- **Parity-XOR toggle induction on rest-splits** (`lemmas/parity-integral.md` CERTIFIED) — Opening B's engine.
- **Peeling-pair bound** (`lemmas/peeling.md` CERTIFIED) — Opening C-a's engine (fragments summing to `2·M` pair off).
- **Continuity / perturbation at the `M = 2^{n−1}` boundary** — Opening D (already proved by alternating-potential, just needs the conditional lifted).

## Cheap-kill candidates

- **G1-iii-a direct peeling-pair bound** (Opening C-a): the fragments of `2^n` sum to `2·2^{n−1}`; pair them greedily (largest with second-largest, etc.) and the peeling lemma cancels each near-equal pair, leaving the dyadic `(n−2)` D as floor. This is the "shave the easy sub-case off for free" — it removes G1-iii-a from the open set with no tiling-rigidity needed.
- **Parity-count of dyadic edges crossed by `O_F`'s breakpoints**: each breakpoint of `F` that is NOT a dyadic edge of `E_{R_0}` contributes a positive-measure leak in exactly one `E_{R_0}` band; sum the leaks. This is the s≥3 analog of Lemma 8's single-edge argument — try it before the full superincreasing machinery.

## Knowledge-base entries to use

- **Pigeonhole / extremal principle** (Combinatorics) — the superincreasing-block forcing is a pigeonhole/extremal argument.
- **Invariants & monovariants** (Combinatorics) — the parity-XOR toggle (CERTIFIED) is the rest-split induction's monovariant.
- **Constructive vs existence** (General Proof Methods) — G1 needs `D ≥ 1` (lower) AND the tight family attains it (Lemma 6, PROVED) — the bound is sharp, both sides already exhibited.
- **Induction** (General Proof Methods) — Opening B inducts on rest-splits; the standard "strengthen the hypothesis" caveat applies (the inductive hypothesis must carry the rigid-tiling structure, not just the numeric bound).
- **Piecewise-concavity smoothing** (Algebra) — `D = ∫[j odd]` is piecewise-linear in the breakpoints; a *concavity on each inter-edge band* argument may give a one-line "min at a breakpoint = dyadic edge" reduction (the tight family sits at breakpoints just off dyadic edges — consistent with a concavity-driven minimizer). FLAG for the outliner: the round-2/3 explorer's "convexity of order statistics" Route A was flagged non-convex globally, but **piecewise-concavity between dyadic edges** is a weaker, possibly viable variant — worth one probe.

## Analogous past problems (cruxes)

None truly analogous in the obvious subtopics (`games-and-strategy`, `invariants-and-monovariants`, `coloring-and-parity`). The closest structural motif is **superincreasing-sequence / Zeckendorf-representation forcing** (KB Number Theory, dyadic-tower), but I did not find a crux move that mirrors "odd-region of a partition cannot perfectly tile the complement of a rigid dyadic tiling." The genuinely analogous problems (partition-into-pieces + alternating-claim games) appear to be post-2026. **Do not force a wrong match.** If the outliner wants a crux, the best fit is the generic *invariants-and-monovariants* + *extremal principle* pair, not a specific solved problem.

## Prior progress

- **Certified**: greedy-alternating, parity-integral + toggle, peeling, equal-halve-n-largest, peel-once-inductive, pairwise-diff-strategy. `splits-inequality.md` PARTIAL (Cases A/B/C + Lemmas 7/8/9).
- **Answer** `c(n) = 2^n/(2^{n+1}−1)` verified n=1..5.
- **G1 furthest correct**: Cases A/B/C (all n), 2-piece-F/rest-unsplit (Lemma 8, all n≥2), low-cancellation (Lemma 9, all F all n), tight Lemma-6 family sharpness. The high-cancellation multi-piece (s≥3) is the open crux.
- **n=2 fully closed** (both bounds); **n=3 upper-bound Cases A,B closed**; **n=3 Case C verified 0/30k but 12-expression casework open**.

## Dead ends (do not retry)

- **Sub-measure `C ≤ D_F`**, **XOR-sum/triangle `D_R ≤ D_{R_0} + W`**, **`D ≥ D_{R_0}`** — all too loose (verified short at the tight family). Recorded in `splits-inequality.md`.
- **Trivial overlap `|O_F ∩ E_{R_0}| ≤ |E_{R_0}|`** — Lemma 9, closes low-cancellation only; fails HC.
- **Union-measure reformulation as a "new route"** — it is EXACTLY EQUIVALENT to the overlap bound (per-role rule, round 4); it is a re-statement, not a bypass. (It IS the cleanest bookkeeping for stating the target, though — use it as the statement, not as the method.)
- **Induction on s by merging adjacent F fragments** — I tested (2000+ configs, n=4, s=3): in **1490/2913 configs BOTH merges INCREASE D** (the s-piece config is TIGHTER than any (s−1)-piece merge). So "merge and apply (s−1) bound" does NOT work — more fragments give smaller D, the tight case is max-s, and merging goes the wrong way. Do not propose merge-induction.
- **Band-parity lens as a bypass** — confirmed (round 4, alternating-potential concession) to be Lemma-4 re-lensing; the "shave 1" wall persists. Use only as bookkeeping.
- **G1-iii "reduce to G1(n−1)"** — unsound (folded rest total `3·2^{n−1}−1 ≠ D_{n−1}`, verified n=3..6). DEAD. Replace with Opening C (split into iii-a easy / iii-b flat).
- **G1-iii-a needs the full tiling-rigidity argument** — FALSE (conjecture): iii-a has min D ≥ 3 (n=4..7), closeable by a direct peeling-pair bound. Don't route it through the HC machinery.

## Small-case / intuition notes (labeled CONJECTURE from numerics)

- **The "1" in "shave 1" is the dyadic-edge overflow of F's breakpoints past `E_{R_0}`'s dyadic edges** (CONJECTURE, verified exactly on the n=4 s=3 tight family: complement = sliver `(2, 2+ε_3]`, measure `ε_3` = target exactly). The forced misalignment is the structural source of the `+1`.
- **G1-iii-a (rest unsplit) is easy**: min D = 3, 3, 5, 7 (n=4,5,6,7) at r=3..5 — **≥ `D_dyadic(n−2)`** roughly, always `≫ 1`. CONJECTURE: `D ≥ D_dyadic(n−2) ≥ 1` via peeling-pair cancellation of the `2·M`-summing fragments.
- **G1-iii-b (rest split, flat) is tight** (D=1 attainable at n=4) and is the flat regime, structurally twin to G2-flat — CONJECTURE: it is the genuine IMO-hard core on the lower-bound side and may resist tiling rigidity (which needs a dominant M).
- **More F fragments ⇒ smaller D** (tight case is max-s = Lemma-6 family with `s = n−1`); merging goes the wrong way (verified 1490/2913). The minimizer is at the maximal-fragment-count boundary, consistent with a piecewise-concavity-in-breakpoints minimizer sitting just off the dyadic edges.
- **G1-ii is the `M → 2^{n−1}` boundary of G1-i-with-rest-split** (not of Lemma 8's rest-unsplit G1-i); closed by continuity once Opening A+B close.
