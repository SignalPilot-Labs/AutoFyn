# Outline review — imo-2026-03 (round 1)

Conjecture `c(n) = 2^n/(2^{n+1}−1)` verified exact for n=1..5; the **upper bound** (universal Xiang forcing strategy) is the real gap. Four upper-bound routes proposed. I tested the load-bearing lemmas of each with exact-rational small-case computation before judging.

## Per-approach verdicts

### `induct-one-mark` — APPROVE-new
Strong induction on n via a one-mark reduction factoring `1/f(n+1) = 1 + 1/(2 f(n))`, templated on the verified n=1 two-mode (bisect/sliver) base case. This is the most direct and natural framing of the upper bound: the value recursion IS the inductive signature, and the n=1 base case exhibits exactly the bisect (M large) vs sliver (M small) decomposition that the recursion factors into ("+1" secured unit + half-scaled residual). The approach honestly flags the load-bearing gap (the one-mark reduction lemma: constructing Xiang's first mark and proving the residual is an (n)-instance at half scale) AND the parity-flip hazard (splitting the largest piece flips the parity of every subsequent piece, inflating Liu — the reduction must account for this, not ignore it). No fatal flaw: the technique is capable of proving the claim, the skeleton is valid, and the gap is genuine but not circular. The parity flip is a real obstacle the builder must handle, flagged upfront.

### `potential-linearize` — RETHINK (fatal: core lemma is false)
**The per-mark linear-advance lemma is false, verified at n=1.** The arithmetic of the Möbius linearization is correct: `u = −1/A`, `u(n) = −D(n)`, `u(n+1) = 2u(n)−1` — but this is the recursion for the **game VALUE** `A(n) = 1/D(n)`, where one "step" corresponds to adding a mark to BOTH players (the value recursion `f(n+1) = 2f(n)/(2f(n)+1)` relates n+1 marks-each to n marks-each). The outline conflates this value recursion with a **per-Xiang-mark monovariant on arbitrary partitions**, which does not hold:

- **As written (`u' ≥ 2u−1`):** trivially true but gives a LOWER bound on Liu (u bounded below = A bounded below = Liu bounded below), the opposite of the upper bound the approach needs. The outline's own wording ("u grows in magnitude") contradicts `u' ≥ 2u−1` (which bounds u from above, limiting magnitude growth).
- **As corrected for the upper bound (`u' ≤ 2u−1`, i.e. `A' ≤ A/(A+2)`):** FALSE. n=1, dyadic Liu config (pieces 2/3, 1/3, `A = 1/3`): Xiang's bisect gives `A' = 1/3`, but `A/(A+2) = 1/7`. `1/3 > 1/7`. n=1, non-dyadic (pieces 3/4, 1/4, `A = 1/2`): bisect gives `A' = 1/4`, but `A/(A+2) = 1/5`. `1/4 > 1/5`. The sliver mode is worse: `A' = A` (no decrease at all — Liu is bounded via `Liu = 1−a ≤ 2/3`, not via A dropping to the target).

Xiang's single mark cannot achieve the full value-recursion step because the recursion's "one step" is a FULL round (both players add a mark), not just Xiang's mark. The game target `A' ≤ 1/D(n)` IS achieved by Xiang, but NOT via the linear rule `A' ≤ A/(A+2)` — the linear rule demands A drop far below the game target at every intermediate step, which it doesn't. The linearization is an arithmetic identity for the value, not a per-partition monovariant. **This framing cannot be built as stated; it must be re-planned.** Suggested direction for the outliner: keep the Möbius linearization as a *bookkeeping* device for the value recursion, but drop the per-mark-potential claim — the upper bound must be argued at the value level (induction or matching), not via a per-mark partition monovariant.

### `pairing-partner` — APPROVE-new
Structural/matching framing: decompose `A = Σ(p_{2k−1} − p_{2k})` (consecutive sorted pairs) and show Xiang's marks realize a pairing with total excess ≤ 1/D(n), with the dyadic pair-pile `(2^n,2^n, 2^{n−1},2^{n−1}, …, 3, 2, 1, 1)` as the extremal certificate (excess exactly `1/D(n)`, verified). The approach correctly distinguishes itself from the dead-ended naive equal-pairing (which gives the wrong `(n+1)/(2n+1)` and ignores the shred-the-small mode ii) and uses the dyadic-ratio pair-pile instead. Hall's marriage theorem is a real, applicable tool for the matching-condition verification. The gap (partner-construction for arbitrary Liu configs, not just dyadic) is genuine and hard, and the approach honestly flags that the pairing may only be achievable on dyadic configs — but no fatal flaw: the decomposition is exact, the certificate is clean, and the Hall step is a legitimate rigorous path. This is a genuinely different route from the induction (its gap is the partner-construction lemma, not the one-mark reduction lemma), so the two do not share a wall.

### `surrogate-snap` — RETHINK (fatal: domination lemma is false)
**The domination lemma `payoff(L*, S) ≥ payoff(L, S)` for the same Xiang mark-set S is FALSE, verified at n=1.** The dyadic config L* IS the saddle (Liu's best *guaranteed* config: `c(L*) = 2/3 > c(L) = 5/8` for `L = (1/4, 3/4)`), but "best guaranteed" ≠ "pointwise dominates." Computation (exact rational, n=1):

| Xiang mark x | oddsum(L=(1/4,3/4)) | oddsum(L*=(1/3,2/3)) | L* ≥ L? |
|---|---|---|---|
| 1/10 | 17/20 = 0.85 | 23/30 ≈ 0.767 | **FALSE** |
| 1/3 | 3/4 | 2/3 | **FALSE** |
| 1/2 | 3/4 | 2/3 | **FALSE** |
| 9/10 | 3/4 | 2/3 | **FALSE** |

For the majority of Xiang marks, Liu does *worse* on L* than on L. The pointwise domination fails in the wrong direction. The underlying reason (flagged but not resolved by the outliner): the odd-rank sum is a SIGNED alternating sum, not a symmetric convex function of the piece multiset, so standard majorization/Schur-convexity does not apply — and in fact the required monotonicity is genuinely absent. The surrogate-adversary reduction (aimo-0560 crux) requires the surrogate to be pointwise ≥ damaging; here the dyadic config is *less* damaging to Liu for most individual marks. **This framing cannot yield the upper bound as set up.** Suggested direction: abandon the pointwise-domination route; if a surrogate argument is desired, the surrogate must dominate in the *minimax* sense (which is just the saddle property = the original problem), not pointwise.

## Diversity check
The two survivors (`induct-one-mark`, `pairing-partner`) are genuinely far apart: induction-on-n via a one-mark recursion factorization vs. a structural Hall-matching on consecutive pair-excesses. Their gaps (one-mark reduction lemma vs. partner-construction lemma) are distinct and neither reduces to the other; if one bottoms out the other does not share its wall. The field does not collapse to one framing.

## Registered slugs
- `induct-one-mark` — APPROVE-new, registered (cold-start Elo 1500).
- `pairing-partner` — APPROVE-new, registered (cold-start Elo 1500).
- `potential-linearize` — RETHINK, NOT registered (false core lemma).
- `surrogate-snap` — RETHINK, NOT registered (false domination lemma).

## Ranking
Two cold-start approaches, both at 1500. `induct-one-mark` ranks above `pairing-partner`: the induction is the most direct framing of the upper bound (the value recursion IS the inductive signature), and the n=1 two-mode base case gives a clean, verified template for the builder to generalize. `pairing-partner` is a strong structural cross-check but its partner-construction for arbitrary configs is vaguer (the dyadic certificate is clean, but the Hall-condition verification for non-dyadic configs is less clearly tractable). Both viable; the gap is the upper bound and both attack it from different angles.

## Build set
The upper bound is THE gap; both surviving routes attack it from genuinely different angles and builders run in parallel (one per slug, each owns its own file, no collision). Emit both.

build set: induct-one-mark, pairing-partner
