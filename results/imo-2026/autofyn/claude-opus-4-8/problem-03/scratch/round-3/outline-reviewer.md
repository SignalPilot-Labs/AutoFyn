# Outline Review — imo-2026-03 (Round 3)

Answer under review: c(n) = 2^n/(2^{n+1}−1), D = 2^{n+1}−1. Field-wide wall: the XY upper
bound U1, now split into Case A (a_{n+1} ≤ 1/D, closed by Lemma H) and Case B (all pieces >
1/D, open). I ran both kill-switches the outliner attached to the two new approaches.

## Verdicts

### direct-constructive — APPROVE (revise; build it)
Leader, Elo 1558, partial/live. The revision is sound:
- **Dropping the circular integral is correct.** The lower-bound explorer's algebra (∫⌊(N_F−N_I)/2⌋dt ≡ 2^n − O) is right; that formulation was a rename, not a reduction. No revised step leans on it any longer. Good.
- **Lemma H (Case A) is solid and independently confirmed.** I verified numerically that the optimal XY min-Ψ equals a_{n+1} on Case-A configs (e.g. a=(0.612,0.360,0.028) → optimal Ψ = 0.02809 = a_3), matching O = 1/2 + a_{n+1}/2. Case A is genuinely closed by the halve-n-largest strategy. The singleton-at-odd-rank argument is valid.
- **L1 (boundary-crossing route)** has a concrete mechanism (O = ΣF = 2^n constant on the interleaving region; each boundary crossing raises O by 2(I_k − f_j) > 0; cut-count k ≤ n load-bearing), numerically verified n=2..5. The k=n+1 counterexample (O=7.5<8) confirms the cut bound is essential and must be used.
- **L2 (confine-to-R_n exchange)** has numerical support (n=2,3,4,5) and a stated exchange mechanism.

Open gaps are CHANGES-REQUESTED-level, not fatal. Genuine hard core: **Case B, sub-case B2 (a_1 ≤ 1/2, all pieces in (1/D, 1/2])** — the builder should concentrate effort there; the boundary-crossing L1 middle-fragment split (dyadic-gap argument) is the other hard sub-step. Watch the ε→0 open-cut supremum in Lemma I.

### extremal-config — RETHINK / CUT (concavity kill-switch FIRED)
The whole distinct worth of this approach is **Lemma E1: global concavity of g(a) = min_XY O**. The approach's own "watch out for" states that without independent concavity, "max at a*" is just U1 renamed (same wall). **E1 is numerically FALSE.** With an accurate XY minimizer (Nelder-Mead multistart over all cut-allocations; validated by g(a*) exact and max_a g = c(n) clean), a 1-D slice between two configs at n=2 gives an interior **valley**:
```
t:   0.0    0.1    0.3    0.5    0.7    0.9    1.0
g:  0.539  0.548  0.530  0.502  0.526  0.537  0.526
```
g(0.5)=0.502 < (g(0)+g(1))/2 = 0.532 (deficit 0.03). A concave function cannot dip below the chord midpoint. This is robust, not minimizer noise. E1 is dead; the fallback ("smoothing/exchange toward a*") is exactly the max-at-a* = U1+L1 restatement the approach warned against. **Collapses to the odd-sum-measure wall — cut, not registered.** (The extremal *target* max_a g = g(a*) = c(n) IS numerically true, but the concavity *method* to reach it is gone, so nothing distinct survives.)

### amortized-parity — RETHINK / CUT (greedy-sufficiency kill-switch FIRED)
Load-bearing claim **Lemma A2: the greedy "cut across the largest odd-N region" rule reaches Ψ ≤ 1/D in n cuts, provable by an amortized supermartingale Φ = Ψ − (remaining)·δ.** **A2 is numerically FALSE.** Even with a fully refined continuous split optimizer, the myopic greedy fails 7–12% of configs, sometimes catastrophically:
```
a=(0.612,0.360,0.028): greedy Ψ=0.204  vs  optimal Ψ=0.028 ≤ 1/7 ✓
a=(0.620,0.352,0.028): greedy Ψ=0.227  vs  optimal Ψ=0.028 ✓
a=(0.594,0.365,0.041): greedy Ψ=0.143  vs  optimal Ψ=0.041 ✓
```
The configs are fine (optimal XY reaches the target); the greedy RULE fails. Crucially, the winning play on these is halve-n-largest, whose first cut *increases* Ψ before the second reduces it — so no Ψ-decrease supermartingale can certify it, gutting the amortized mechanism. The approach's own "same-wall risk" note applies: to actually win it must adopt direct-constructive's Lemma H strategy, and it offers nothing new for Case B. **Cut, not registered.**

## Diversity flag for the orchestrator
This round put two genuinely-different framings on Case B (config-space concavity saddle; amortized greedy monovariant) and **BOTH were refuted by their own numerical kill-switches** — a good outcome (cheap kills before a wasted build), but it leaves the field collapsed to direct-constructive alone. The refuted-framing graveyard is now: game-separation induction (false), concavity of g (false), amortized greedy (false), potential-duality Φ (vacuous). Next round's outliner needs a Case-B framing distinct from ALL of these. Candidate not yet tried: a direct *strategy* for Case B that mixes halvings with one asymmetric tiny-fragment cut (upper-bound explorer Opening B/D) — this is strategy-based like direct-constructive but is a concrete new sub-lemma for B2, not a new global framing. A truly orthogonal framing remains genuinely open.

## Ranking (updated, stale cleared)
direct-constructive 1558 (leader, partial/live) > potential-duality 1474 (unbuilt, not refuted) > induction-recursion 1468 (dead-end, engine refuted). Comparisons: direct-constructive > both; potential-duality > induction-recursion (unbuilt-but-not-refuted beats a refuted engine). The two new approaches were cut and NOT registered.

build set: direct-constructive
