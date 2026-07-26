# Round 6 outline-reviewer — imo-2026-03

## Gate verdicts (pre-build)

### two-regime-disjunctive (ADVANCE) — CHANGES REQUESTED
Targets `c(3)=8/15` end-to-end (Liu lower via certified `L(3)` + Xiang upper via the 7-cap closure of the `d<1/2` extreme sub-cases `w<−2α`/`z<−2α`). This is the HIGH-VALUE target and the only route that closes a third solved value this round.

Soundness checks:
- **7-cap claim verified.** I tested the 7-cap family `{a, b−a, c−b, d−c, |a+b−c|, |a+c−d|, |a+b−d|}` on 50k extreme-regime exact-rational configs (d<1/2 ∧ (w<−2α ∨ z<−2α)): **0 violations**, worst min-cap `< α`. The drop-one 6-cap (removing `|a+b−d|`) fails by ~0.002 above α on 30k configs — confirming the 7th cap is genuinely load-bearing and the round-5 "no 4–7-cap subfamily suffices" ruling is correctly overturned *when realizability is enforced* (round-5's census counted un-realizable cap *values* like `d−b−c`).
- **Skeleton logic valid.** Chain caps ⇒ `a>α,b>2α,c>3α,d>4α`; the 3 abs caps give 2³=8 OR-branches; `w<−2α` (i.e. `c<a+b−2α<a+b−α`) forces the `|a+b−c|` branch, halving to 4 sub-cases per sub-regime. The case-count is right and disjoint.
- **Load-bearing lemmas have mechanisms.** "7-cap always-realizable" via 2-mark bisect-and-match (pair equal fragments, leave the abs-difference as leftover; none requires `d≥b+c`); "8-sub-case contradiction" via the sign-forced branch collapse. Both are stated with reasons, not bare labels.

Gap to close while building: **the 8 analytic sub-case contradictions are not yet written** (the explorer verified 0 violations; the ≤4-line algebra per sub-case is the laborious but mechanical GAP). Watch the outliner's own flags: do NOT add `d−b−c` (un-realizable in `z<−2α`); do NOT use the gap-G sliver for the `z<−2α` half (requires `d≥b+c`, opposite). Sound, buildable.

### cell-complex-l3 (ADVANCE, D3 via 2-adic/determinant) — CHANGES REQUESTED
Targets general-n `L(n)` via a structural theorem (one theorem vs pairing-partner's two Hall matchings). Technique (Cramer's rule + 2-adic valuation of `0/±1`-determinants with power-of-2 RHS) is a real number-theoretic handle, genuinely different from Hall (determinant-level, not sum-level).

Concerns:
- **The load-bearing lemma "v_2(numerator) < v_2(L) at fractional vertices" is the whole bet.** The stated mechanism (dyadic RHS powers of two + `0/±1` rows make the alternating-sum numerator lose factors of 2 that L retains) is plausible but UNPROVEN — and the outliner concedes it is "not standard olympiad toolkit." The slack-grows-with-n evidence (0 violations n=3..7) is a green light, NOT a proof (per the round-5 rule "computationally 0 violations is not a proof substitute"). The builder must prove this number-theoretic lemma, not just observe it.
- **D3-dual shared-wall risk with U is flagged** by the outliner itself — acceptable as a watch-item; the lower/upper bounds run in opposite parity directions, so the shared *technique* does not collapse to a shared *wall*.
- Whole attempt at general-n L end-to-end. Skeleton steps follow validly.

### pairing-partner (ADVANCE, direct Hall injection) — CHANGES REQUESTED
Targets general-n `L(n)` via a sum-level Hall injection `φ` on merged-sort rank indices, bypassing the factor-of-2 inductive gap (verified 0 violations n=3..7, slack `o_R−e_M` grows with n). Technique (Hall/SDR + superincreasing-R identity) is right family.

Concerns:
- **Per-position bound FALSE** (`b=(4/3,4/3,4/3)` counterexample) — correctly flagged; the matching MUST be on the SUM over rank indices, not per-position. The injection `φ` is the load-bearing gap with a stated mechanism (superincreasing identity forces each even-rank M-subpiece dominated by some odd-rank R'-piece across the merged sort).
- **Branch 2 (m_1<a_1) general-n (H2) on the rest polytope** is open beyond n=3 (round-5 6-piece casework settles n=3 only). R-refined sub-cases (k≤n) where refinement breaks the superincreasing lever remain open.
- Whole attempt at general-n L. Skeleton valid; the two Hall matchings (H1, H2) are the fixable gaps.

### self-reproducing-invariant (NEW) — CHANGES REQUESTED
Targets general-n `U(n)` via aimo-0262 self-reproducing invariant on the pair-excess vector. Register this round.

**The single-gap-trap assessment (the dispatch's specific question).** The outliner's mitigation — "field the invariant as a FAMILY, use the certified S1/S3 slivers as the far-from-dyadic members so the family is heterogeneous, not one wall" — **does NOT genuinely separate** from two-regime. The S1/S3 slivers ARE two-regime-disjunctive's certified lemmas; importing them as the far-from-dyadic "family members" means that half of the proof = two-regime's wall. If two-regime's sliver casework fails, this approach's far-from-dyadic half dies with it. The mitigation is the single-gap-trap in disguise.

HOWEVER, the approach is not a pure single-gap-trap: the **near-dyadic half is genuinely independent**. The equality-locus `E_n` characterization (pair-pile reproduces on the dyadic + the ridge `R_e`, with compensating excesses `(1−e)+e=1`) is a structural insight NOT in two-regime, and the explorer's mirror probe (Opening 5) independently confirms `E_n` is exactly where the pair-pile/mirror witnesses `V(P)=α`. The near-dyadic mechanism would survive even if two-regime's far-from-dyadic casework failed.

Verdict: register and build, with explicit scope:
- (a) **Build the near-dyadic `E_n` self-reproduction** (the genuinely new, independent wall) — formalize the reproduction rule on `(e_1,…,e_n,ℓ)`, prove the pair-pile invariant caps `Σ e_i + ℓ ≤ α(n)` on `E_n` including the ridge.
- (b) **For far-from-dyadic, do NOT present the S1/S3 import as a separation** — that is a shared-wall dependency on two-regime. Either find a DIFFERENT mechanism (e.g. a potential `Ψ` on the pair-excess vector, or the D3-dual parity), or honestly scope the approach to near-dyadic + `E_n` and concede the far-from-dyadic half as a two-regime dependency.

The bare pair-pile does NOT reproduce with cap ≤ α off `E_n` (mirror overshoots to A=0.8 on extreme-dominant, probed dead) — so step 3's "enrichment" is mandatory, not optional.

### dyadic-halving-induction (RETIRE) — confirmed sunk
Central strict-decrease route falsified (ridge `R_e`, certified `lemma-ridge-falsification.md`); both harvestable lemmas (Φ=0 uniqueness, local-kink) already in cache; far-from-dyadic remnant overlaps two-regime. No live engine; the genuinely-different G2 successor is `self-reproducing-invariant`. Confirmed RETIRE — not registered, not in build set.

## Registration / copy actions
- `register_approach` for `self-reproducing-invariant` (NEW, APPROVED as CHANGES REQUESTED). [Tool call below.]
- No copy requested by the outliner this round.
- `dyadic-halving-induction` NOT registered (RETIRE — sunk).

## Ranking (head-to-head, anchored to last outcomes)

Comparisons (sure pairs only):
1. `two-regime-disjunctive` > `cell-complex-l3` — two-regime closes the high-value `c(3)` this round with a verified 7-cap; cell-complex's D3 is a hard open number-theoretic lemma.
2. `two-regime-disjunctive` > `pairing-partner` — closes a solved value vs open general-n Hall injection.
3. `pairing-partner` ≈ `cell-complex-l3` (draw) — both general-n L, both open; pairing-partner's slack-grows-with-n is a marginally greener light than the "non-standard" 2-adic lemma, but both are real bets → draw.
4. `cell-complex-l3` > `self-reproducing-invariant` — established verified-milestone vs NEW with a hard far-from-dyadic wall.
5. `pairing-partner` > `self-reproducing-invariant` — established advanced vs NEW.
6. `two-regime-disjunctive` > `self-reproducing-invariant` — closer to solved vs NEW general-n.
7. `self-reproducing-invariant` > `dyadic-halving-induction` — live NEW successor vs dead RETIRE.
8. `dyadic-halving-induction` > `induct-one-mark` — recent certified negative results (ridge falsification) vs dead central route since round 2.
9. `pairing-partner-transfer` > `induct-one-mark` — CK lemma harvested vs nothing (both sunk).

`update_ranking` call below clears stale flags on all compared approaches.

## Build set
`two-regime-disjunctive` (HIGH-VALUE: close U(3) → `c(3)=8/15` solved), `pairing-partner` (general-n L Hall injection), `cell-complex-l3` (general-n L D3 2-adic), `self-reproducing-invariant` (NEW general-n U, near-dyadic E_n focus).

build set: two-regime-disjunctive, pairing-partner, cell-complex-l3, self-reproducing-invariant
