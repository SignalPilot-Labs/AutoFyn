# Math-explorer report — upper-bound balanced-region residual (round 7)

Lens: the two open upper-bound gaps in `universal-halving-adversary`
(Existence Theorem for the residual 4–35% after best-of-{k=1,k=2}
Anchor-Merge) and `lp-duality-split-polytope` (a crude polynomial lower
bound on the triangular family's single-piece-floor excess over 1/2, to
finish the general-n Multi-Piece Necessity theorem). Scouting only — no
proof attempted. All claims below are numerical evidence from fresh
scripts (not re-derivations of the certified lemmas), meant to guide next
round's outliner/builder.

## 1. `lp-duality-split-polytope`: strong numeric lead for a crude bound

**Setup.** Certified `lemmas/target-excess-identity.md` shows proving
`floor(n) > c(n)` for the triangular family reduces to proving
`excess(n) := floor(n) - 1/2 > 1/(2(2^{n+1}-1))` — an exponentially small
threshold. The file's round-6 data (`n=3..6`, exact) showed `excess(n)` is
only polynomially small but found no closed form and rejected a
3-point-fit conjecture `excess(n) = 1/((n+1)(n+2))` (fails at n=6).

**What I did.** Re-derived `excess(n)` numerically for `n=3..16` via
independent multistart Nelder–Mead search over every `(idx, m)` (piece
choice × fragment count), cross-checked against the file's 4 exact values
(n=3,4,5,6: matched `11/20, 8/15, 11/21, 15/28` to 6 decimals) — so the
heuristic search is reliable. Then compared `excess(n)` against
`delta(n) := 1/D_n = 2/((n+1)(n+2))`, the family's AP common difference.

**Finding — clean step pattern.** The ratio `excess(n)/delta(n)` is *not*
noisy; it is a slowly, weakly-increasing step function:

```
n:      3   4   5   6   7   8   9  10  11  12  13  14  15  16
ratio: 0.5 0.5 0.5 1.0 1.0 1.5 1.5 1.5 2.0 2.0 2.5 2.5 3.0 3.0
```

i.e. `excess(n) = ratio(n) * 2/((n+1)(n+2))` with `ratio(n)` **weakly
increasing** and **never below `0.5`** across all 14 tested values (block
sizes 3,2,3,2,2,2,... — consistent with the file's own diagnosis that the
exact mechanism is a non-smooth, number-theoretic function of which
landmark subsets sum to `p_idx`). The refuted 3-point conjecture is
exactly the `n=3,4,5` value of `ratio=0.5` frozen as if constant; the real
`ratio(n)` grows roughly linearly (~`n/6`), so `excess(n) ~ Θ(1/n)`, not
`Θ(1/n^2)` as the file's round-6 note guessed — this is worth correcting
in the file.

**Candidate crude lemma (not proved, strong numeric support, 14/14
consistent):**
$$\mathrm{excess}(n) \;\ge\; \frac{1}{(n+1)(n+2)} \qquad\text{for all } n\ge3,$$
i.e. the *inequality* form of the already-rejected equality conjecture.
This is far more than sufficient: combined with the certified
`target-excess-identity.md`, it closes the general-`n` theorem outright,
since `1/((n+1)(n+2))` is polynomial and the required threshold
`1/(2(2^{n+1}-1))` is exponential — already beaten by two orders of
magnitude at `n=6` (`0.05` vs `0.008`) and the gap widens rapidly.

**Why this looks tractable, not just numerically true.** The exact
equality case (`ratio=0.5`) is realized at `n=3,4,5` and is the file's own
certified exact computation, so a `≥` proof only needs to rule out `ratio`
ever dropping *below* `0.5` — a one-sided bound, weaker than pinning the
exact minimizer or the exact `ratio(n)` formula. This plausibly sidesteps
the "number-theoretic, non-smooth" obstruction the file correctly
identified for the *exact* formula: an inequality can be loose everywhere
`ratio(n)>0.5` and only needs to be tight at the (apparently recurring)
worst case. I did **not** find a proof mechanism for the `≥1/2` floor on
`ratio(n)` — that is the concrete open task for next round's builder — but
candidate routes worth trying:
  - Direct AltSum argument: show any single-piece split of the AP family
    leaves at least "half an AP step" (`delta(n)/2`) of unavoidable
    alternating-sum imbalance, via a parity/pigeonhole argument on how a
    removed AP term's mass can redistribute among the sort order (in the
    style of the certified `dominant-chain` / `doubling-lemma` arguments
    already in the project, which prove similar "half credit" facts for
    even-length ties).
  - Restrict to the extremal case `idx=1` (splitting the top piece) first,
    since numeric search always picks `idx∈{0,2,4,...}` (0-indexed) i.e.
    an odd position — never an even one — across all 14 instances; this
    parity pattern (which piece is ever optimal to split) might itself be
    provable and would cut the case analysis roughly in half.

**Not done / caveat.** This is heuristic-numeric (Nelder–Mead), not exact
rational arithmetic, for `n=7..16` (only `n≤6` are exact-certified). A
next step before trusting the `≥0.5` floor further is either (a) exact
rational verification via the certified Single-Piece-Split Vertex Lemma
for `n=7,8,9` to confirm `ratio=1.0,1.5` exactly (cheap, same method the
file already used for n=5,6), or (b) directly attempt the AltSum
pigeonhole argument above. I recommend (a) first as a 1-round sanity gate
before investing in the general proof.

## 2. `universal-halving-adversary`: residual is concentrated near p1→1/2

**Setup.** The file's General `k`-Anchor-Merge Lemma (certified
`lemmas/singleton-interleaving-and-k-anchor-merge.md`) closes 65–96% of
the residual "large-gaps-everywhere" balanced region via best-of-{k=1,k=2},
with `k=3` proved *not* monotonically better. Residual: 4–35%, unclear
structure.

**What I did.** Wrote an independent generator for random balanced,
gap-dominant partitions (`p1<1/2`, every consecutive gap
`>1/(2^{n+1}-1)`, full budget `k0=n+1` pieces) and an independent
brute-force best-of-{disjoint pairings, k=1..3} Anchor-Merge evaluator
(exact `Fraction` arithmetic), for `n=3..7`, 300 random trials each.
Caveat: my random generator is **not** measure-matched to the file's own
sampling (my fail rates, 29–57%, run higher and, unlike the file's
non-monotone 4–35%, rise with `n` — likely a sampling-bias artifact, e.g.
over-representing large-`p1` instances at higher `n`; this is a fresh,
cruder script, not a reproduction of the file's numbers). Do not treat my
percentages as a correction to the file's — only the *structural* finding
below, which was checked directly, is trustworthy.

**Finding — clean threshold in `p1`.** Bucketing 3000 random `n=5`
instances by `p1` and computing the best-of-{k=1,k=2} failure rate:

```
p1~0.25: 12.4% fail
p1~0.30: 18.0% fail
p1~0.35: 22.9% fail
p1~0.40: 45.6% fail
p1~0.45: 84.4% fail
p1~0.50: 100.0% fail   (boundary, p1→1/2)
```

Failure rate rises sharply and monotonically as `p1 → 1/2⁻`, essentially
saturating to 100% right at the boundary. Every hand-inspected failing
instance had `p1 ∈ [0.37, 0.47]` and full budget `k0=n+1`. This strongly
suggests the residual 4–35% is **not** uniformly spread over the balanced
region but concentrated in a `p1`-near-`1/2` boundary layer — which is
suggestive because the file's own upper-bound proof *already* closes
`p1∈[1/2,c(n)]` unconditionally (the adjacent regime, just past the
boundary). This raises a natural next-round question: is there a
continuity/limiting argument, or a boundary-layer-specific construction
(e.g. treat the top piece's near-1/2 mass specially, similar to how the
`p1≥1/2` case is already handled), that extends the closed `p1≥1/2` proof
technique into the `p1<1/2` boundary layer, rather than trying to make
Anchor-Merge itself work there? This looks like a more promising route
than searching for a `k≥4` Anchor-Merge variant (which the `k=3`
non-monotonicity result already makes suspect — no evidence larger `k`
generically helps).

**Dead-end-adjacent finding.** In my (differently-sampled) trials,
`kmax=3` never rescued a single instance that `kmax=2` failed (fail counts
identical at every `n`) — consistent with, and independently corroborating
from a different random sample, the file's own `k=3` non-monotonicity
finding. This reinforces: don't spend next round's budget on `k=3,4,...`
Anchor-Merge variants as a generic fix; the boundary-layer / different-
mechanism idea above looks more promising.

## Summary of recommendations for next round

1. **`lp-duality-split-polytope`** (most promising, concrete): verify
   `ratio(7),ratio(8),ratio(9)` exactly via the certified Single-Piece-
   Split Vertex Lemma (cheap, mirrors the file's own n=5,6 method), then
   attempt to prove `excess(n) ≥ 1/((n+1)(n+2))` — an inequality, not the
   refuted equality — via a direct AltSum/pigeonhole argument in the style
   of the certified `dominant-chain`/`doubling-lemma` "half-credit" proofs.
   If this lands, combined with `target-excess-identity.md` it closes the
   entire general-`n` upper-bound theorem for the triangular family.
2. **`universal-halving-adversary`**: redirect the Existence Theorem
   search away from larger-`k` Anchor-Merge variants (numerically
   unpromising, corroborating the file's own k=3 finding) and toward a
   boundary-layer argument for `p1` near `1/2⁻`, possibly reusing/adapting
   the already-closed `p1∈[1/2,c(n)]` construction by continuity.
