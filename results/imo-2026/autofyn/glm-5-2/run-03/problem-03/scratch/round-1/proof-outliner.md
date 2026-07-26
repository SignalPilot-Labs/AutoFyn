# Proof-outliner report — imo-2026-03 (IMO 2026 P3, Chu-Han war)

**Round 1. Field: 4 new approaches** (workspace was empty). All target the WHOLE problem end-to-end: answer `c(n) = 2^n/(2^{n+1}−1)`, with greedy-alternating lemma + lower bound (Liu Bang) + upper bound (Xiang Yu).

## Consensus the field is built around
- **Answer (conjectured, verified exactly n=1,2,3):** `c(n) = 2^n/(2^{n+1}−1) = 1/(2 − 2^{−n})`. Recursion `1/c(n) = 1/c(n−1) + 1/2^n`, i.e. `D_n = 2D_{n−1}+1`, `D_n = 2^{n+1}−1`.
- **Shared load-bearing lemma (must prove from scratch):** greedy-alternating claim lemma — Liu = odd-position sum of descending-sorted pieces. Explorer game-theory proved it airtight (strong induction on m; removing the largest minimizes opponent's `O_rest` because `a_{2j−1} ≥ a_{2j}` pairwise). Once reviewer certifies, importable by all approaches.
- **Shared lower-bound construction:** Liu marks at cumulative dyadic `(2^k−1)/D_n`, pieces `1:2:4:…:2^n` over `D_n`; largest `2^n/D_n` exceeds sum of rest `(2^n−1)/D_n` (crux aimo-0117 mechanism).
- **Shared lower-bound crux (G1, all approaches):** the splits-inequality lemma — after any ≤ n Xiang splits of the dyadic multiset, `S_odd ≥ 2^n/D_n` (equiv. alternating sum `D = S_odd − S_even ≥ 1/D_n`); equality at Xiang's equal-halving. This is the deepest technical crux of the LOWER bound but is tractable (numerics confirm, equal-halving is the unique `D`-preserving move).
- **The bottleneck is the UPPER bound** (Xiang Yu caps arbitrary Liu Bang marks at `≤ 2^n/D_n`). The four approaches differ in how they attack this upper bound — genuinely different framings, so they do not share one wall.

## Field of approaches

### dyadic-induction: new
**Idea:** Induction on n driven by `1/c(n) = 1/c(n−1) + 1/2^n`. Lower bound: dyadic construction + "largest exceeds sum of rest" + splits-inequality lemma. Upper bound: Xiang Yu uses ONE mark to peel off a piece of density `1/2^n`, reducing to the `(n−1)`-game; two regimes (largest piece above/below threshold = equal-split vs barely-split), matching the proven n=1 base.
**Technique (spine):** structural induction on n; crux aimo-0117 for the lower-bound dyadic forcing.
**Key lemmas:**
- Greedy-alternating lemma (shared).
- Largest-exceeds-sum-of-rest — because `2^n > 2^n − 1` forces the dyadic top to rank 1 (odd).
- Splits-inequality lemma (G1) — because equal-halving is the unique `D`-preserving split; any unequal split raises `D`.
- Peeling-recursive lemma (G2) — because `D_n = 2D_{n−1}+1` lets one mark convert density `1/2^n` into a pair, reducing to the `(n−1)` instance.
**Hard gap (bottleneck):** G2 — the inductive peeling step. Pin the threshold, prove the recursion falls out, prove the barely-split (Regime B) accounting. This is where the approach most likely stalls.
**Kills:** if no single-mark reduction achieves the recursion `1/c(n)=1/c(n−1)+1/2^n`, the inductive upper bound is dead.
**Cruxes/KB:** aimo-0117; KB *Induction*, *Constructive vs existence*, *Invariants & monovariants*.

### pairing-charging: new
**Idea:** Upper bound via a DIRECT combinatorial charging scheme — no induction on n, no recursion. For arbitrary Liu marks, Xiang Yu partitions the stick into n "response dominoes" + one leftover; answers Liu's mark in each domino with the antipodal mark (aimo-0461 form); each domino's pair contributes a bounded deficit `δ_k` to `D = S_odd − S_even`; the deficits telescope to `1/D_n`, giving `D ≤ 1/D_n` i.e. `S_odd ≤ 2^n/D_n` in one shot.
**Technique (spine):** direct combinatorial charging / double-counting; crux form templates aimo-0115 (domino pairing) and aimo-0461 (antipodal response in a partition).
**Key lemmas:**
- Greedy-alternating lemma (shared).
- Partner-piece charging — Xiang's mark in a domino creates a partner `≥ p − δ`, pair contributes `≤ δ` to `D`.
- Domino-surplus telescope — per-domino deficits form a dyadic series summing to `1/D_n`.
- Antipodal-response legality — each domino is an interval; antipodal mark is interior and distinct.
**Hard gap (bottleneck):** G2 — defining the domino partition for ARBITRARY Liu marks (not just the dyadic config — otherwise circular), pinning the per-domino deficit, proving the telescope equals `1/D_n` EXACTLY (slack means a loose bound).
**Kills:** no domino partition exists for arbitrary Liu marks yielding the deficit bound; or the telescope sums to `> 1/D_n` (weak) or `< 1/D_n` (contradicts lower bound).
**Cruxes/KB:** aimo-0115, aimo-0461; KB *Pigeonhole/extremal*, *Double counting*, *Invariants & monovariants*.

### surrogate-adversary: new
**Idea:** Upper bound via a RESTRICTED, fully-specified Xiang Yu strategy `R_n` ("repeatedly equal-split the current largest piece") + a potential `Φ = S_odd − S_even`. Prove `R_n` caps `Φ` at `1/D_n` for any Liu config via a monovariant. Since real Xiang Yu has full freedom (⊇ `R_n`), the cap transfers UP. Distinct from dyadic-induction (no recursion, no peeling) and from pairing-charging (no domino partition; bound from a monovariant on piece sizes, not pairwise charging).
**Technique (spine):** explicit restricted strategy + potential/monovariant; crux aimo-0560 (surrogate adversary, weaker-minimizer direction — transfers up to real) and aimo-0262 (monovariant).
**Key lemmas:**
- Greedy-alternating lemma (shared).
- Equal-split surrogate `R_n` is a restriction of real Xiang Yu — cap transfers up (after aimo-0560 weaker-minimizer direction).
- Potential `Φ = S_odd − S_even` — `S_odd = (1+Φ)/2`, capping `Φ` caps Liu.
- Config-dependent decrement lemma (G2, the crux) — each equal-split of the largest piece `a_1` removes `≈ a_1/2` from `Φ`; prove `Σ a_{1,k} ≥ 2(Φ_0 − 1/D_n)`.
**Hard gap (bottleneck):** G2 — the config-dependent decrement. The per-split `ΔΦ ≈ a_1/2` is NOT a clean dyadic telescope; bounding `Σ a_{1,k}` below by `2(Φ_0 − 1/D_n)` for arbitrary Liu config is the approach's whole bet.
**Kills:** `Σ a_{1,k}` has no uniform lower bound in terms of `Φ_0`; or `R_n` does not cap Liu at `2^n/D_n` for some config (falsifiable by a numeric sweep).
**Cruxes/KB:** aimo-0560 (weaker-minimizer direction), aimo-0262; KB *Invariants & monovariants*, *Extremal principle*.

### alternating-potential: new
**Idea:** Reframe the WHOLE problem around the alternating sum `D = a_1 − a_2 + a_3 − …`. Since `S_odd = (1+D)/2`, the claim `c(n) = 2^n/D_n` is equivalent to **`D = 1/D_n` is the tight value of the alternating sum after optimal play.** Lower bound: Liu's dyadic config forces `D ≥ 1/D_n` (self-reproducing invariant, aimo-0262). Upper bound: Xiang's marks drive `D` down to `≤ 1/D_n` (potential cap). Both bounds through ONE lens — symmetric, distinct from the other three.
**Technique (spine):** alternating-sum reformulation + self-reproducing invariant (lower) / potential cap (upper); crux aimo-0262 (self-reproducing invariant), aimo-0596 (alternating-sum pinning to a coset).
**Key lemmas:**
- Greedy-alternating lemma + `D` reformulation — `S_odd = (1+D)/2`.
- Equal-split-preserves-`D` (lower crux, G1) — two halves of an equal split land in consecutive ranks and cancel.
- `D`-driving-down lemma (upper crux, G2) — splitting the largest odd-rank piece removes its contribution; a dyadic-decrement schedule brings `D` to `≤ 1/D_n` in n marks.
- Universal `D ≥ 0` — `a_{2k−1} ≥ a_{2k}` pairwise (the `1/2` floor).
**Hard gap (bottleneck):** G2 — the `D`-driving-down schedule. The naive dyadic telescope gives `D ≤ 1/2^n`, but the target is `1/D_n ≈ 1/2^{n+1}` — a factor-of-2 gap. Must be resolved: either `D_0 < 1` for the worst Liu config, or decrements are `1/2^{k+1}`-scaled, or (speculative, heavy) a three-gap/Kronecker argument (KB Three-gap theorem).
**Kills:** the `D`-driving-down lemma cannot reach `1/D_n` in n marks (factor-of-2 gap unbridgeable); equal-split-preserves-`D` is false.
**Cruxes/KB:** aimo-0262, aimo-0596; KB *Invariants & monovariants*, *Three-gap theorem* (speculative fallback), *Induction*.

## COPY request
**copy-of surrogate-adversary → surrogate-adversary-thresholded.** The surrogate-adversary upper bound has TWO viable restricted-strategy gap-fills worth running in parallel:
- `R_n`: always equal-split the current largest piece (clean monovariant, but the per-split decrement is config-dependent and may not telescope).
- `R_n'`: equal-split the largest UNLESS it is below a threshold `2^n/D_n`, in which case barely-split and stop (matches the proven n=1 base case exactly, where the barely-split branch is essential).

These are genuinely different mechanisms (clean monovariant vs threshold-gated hybrid) for the same upper-bound gap; both should run so we learn which closes. Recommend the reviewer branch a twin.

## Nomination for advancement
All four are new this round; nominate **all four for the build set** (one builder each). Priority order for gap-filling:
1. **G1 (shared lower-bound crux, splits-inequality lemma)** — once proven and reviewer-certified as a shared lemma in `results/imo-2026-03/lemmas/`, it benefits ALL FOUR approaches. Highest leverage. Any builder can own it; certify it as `splits-inequality` lemma.
2. **G2 upper-bound cruxes** — the four approaches each attack this differently; let all four run so the outline-reviewer can rank which upper-bound framing is closest. The upper bound is the IMO-difficulty half; diversity here is the whole point.
3. **Greedy-alternating lemma** — certify as a shared lemma `greedy-alternating` (explorer already proved it airtight); all approaches import it.

## Diversity check (framing, not technique)
- dyadic-induction: upper via recursion on n.
- pairing-charging: upper via one-shot combinatorial charging (no induction).
- surrogate-adversary: upper via restricted strategy + monovariant (no recursion, no partition).
- alternating-potential: upper via alternating-sum potential cap (single lens for both bounds).

No two share an upper-bound wall: recursion / charging / restricted-strategy-monovariant / alternating-sum-cap. If one upper bound dies, the other three are unaffected.

## Bottleneck honestly
The **upper bound** is the IMO-difficulty half. The lower bound (G1) is shared and tractable (numerics + the equal-halving-is-unique-minimizer structure make an induction on splits very plausible). The upper bound has NO approach with a proven mechanism yet — only numerics and conjectured strategies. Expect the first rounds to certify G1 and the greedy lemma (raising all approaches to `partial`), while the upper-bound G2 cruxes are where the real fight is.
