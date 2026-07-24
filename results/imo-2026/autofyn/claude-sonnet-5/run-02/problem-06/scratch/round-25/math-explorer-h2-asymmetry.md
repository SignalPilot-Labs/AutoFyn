## imo-2026-06 (lens: H2 seed asymmetry — large-scale re-simulation of a_1=11305 vs a_1=4807)

### Method
Wrote a new, faster simulator (`/tmp/round-25/fastsim2.py`): SPF-sieve-based factorization (numpy
sieve up to a generous bound, ~5-15M) instead of trial division, plus the same per-prime bigint
bitmask legality test used by prior rounds (`cov = OR of prime_bits[p] over p|c`; `c` legal iff
`cov & full_mask == full_mask`). Sanity-checked against round-24's numbers before trusting it: at
`n=25000,50000,400000` for `a_1=11305` it reproduces `335,402,702` distinct extended-`S_0`-types
**exactly**, and matches round-24's `4807` figures (`132,150,...,200` at the same checkpoints)
exactly. `S_0` used, per the certified Finite Core Theorem / round-19's construction, unchanged
from prior rounds: `S_0(4807)={2,3,5,7,11,19,23,73,127}` (|S_0|=9), `S_0(11305)=
{2,3,5,7,13,17,19,23,29,37,43,101}` (|S_0|=12).

**Environment constraint found and worked around:** background (`nohup`/`setsid`/`disown`)
processes are silently killed once the issuing `Bash` tool call returns (this sandbox does not let
child processes outlive the call) — confirmed by three failed background-launch attempts whose
processes vanished from `/proc` between calls despite `nohup`+`disown`. Worked around by running
each simulation **synchronously inside one `Bash` call** with the 600s-cap `timeout`, accepting
whatever checkpoint is reached before the wall-clock budget runs out — data survives via the
stdout log even if the process is later killed, since the report lines are `flush=True`'d as
computed.

Given this constraint and the round's ~60 min budget, the achieved scale is: **`a_1=4807` to
n=1,000,000** (single synchronous run, ~500s), **`a_1=11305` to n=750,000** (two independent
synchronous runs, both reaching n=750,000 in ~136-139s and agreeing exactly, `806` types; a third
attempt targeting n=1,000,000 was killed by the 420s timeout before reaching that checkpoint —
so 750,000 is the reliable frontier for `11305` this round, short of the "millions" target but a
genuine ~2x extension past round 24's 400,000-term frontier).

### Raw data (cumulative distinct extended-`S_0`-type count vs n)

`a_1=4807`: n=25k,50k,100k,200k,300k,400k,500k,750k,1000k →
types = 132,150,165,181,192,200,208,216,220.

`a_1=11305`: n=25k,50k,100k,200k,300k,400k,500k,750k →
types = 335,402,481,584,651,702,737,806.

### 1. Does the arrival rate taper (H2-supportive) or keep growing ~sqrt(N)?

**Answer: neither seed shows literal `~sqrt(N)` growth once measured correctly, and both DO
decelerate — but at very different rates, so the seed-asymmetry flag from round 24 is real but its
diagnosis needs correcting.**

Round 24 fit a single global power law `T(N) ~ C·N^p` from `n=25000` onward and reported `p`
"flat near 0.51-0.57" for `11305`. That global fit is contaminated by the steep early-transient
growth (the first ~50-100k terms recruit types fast for any seed). Recomputing the **local**
(consecutive-checkpoint) exponent `p_local = log(T2/T1)/log(N2/N1)` gives a much more accurate,
un-contaminated picture:

- `4807` local exponent: `50k→100k: 0.138`, `100k→200k: 0.134`, `200k→300k: 0.146`,
  `300k→400k: 0.142`, `400k→500k: 0.176`, `500k→750k: 0.093`, `750k→1000k: 0.064`.
  **Clear late deceleration** — the exponent roughly halves between the 500k mark and the 1M mark
  (0.14ish plateau, then a sharp drop to 0.09, then 0.06). This is the signature of genuine
  convergence toward a finite limit (or at least a much-slower-than-power-law tail), not sqrt
  growth.
- `11305` local exponent: `50k→100k: 0.259`, `100k→200k: 0.280`, `200k→300k: 0.268`,
  `300k→400k: 0.262`, `400k→500k: 0.218`, `500k→750k: 0.221`. **Mild deceleration
  (0.26-0.28 → 0.22) but then flattens out**, not the sharp late-stage collapse seen in `4807`.

So: `11305` is NOT literally flat at `~0.5` (round 24's number) — corrected local exponent is
`~0.22-0.28`, i.e. slower than `sqrt(N)` even at its most bullish reading — but it is also NOT yet
showing `4807`'s late-stage collapse toward 0 at the same scale (750k vs 4807's 1M). The honest
read: **both seeds are decelerating; `4807` decelerates faster and has already dropped to a small
exponent (0.06-0.09) by n=1M, while `11305` is still sitting at a moderate, only mildly-decreasing
exponent (~0.22) at n=750k.** Whether `11305`'s exponent keeps drifting toward 0 given another
order of magnitude of runway, or asymptotes to a positive constant (genuine unbounded but
sub-sqrt growth), is **not resolved** by this round's reach (750k is not far enough past the point
where `4807`'s own collapse only became visible, ~500k-1M).

### 2. If it keeps growing, is there a concrete growth-rate estimate?

At the current frontier (n≤750,000), `11305`'s type count is consistent with (not exclusively
identified as) a power law `T(N) ≈ C·N^{0.22-0.25}` for some constant `C`; a rough fit gives
`C≈402/50000^0.25≈402/14.94≈27` giving `T(N)≈27·N^{0.24}`, which at `N=750000` predicts
`27·750000^{0.24}≈27·29.9≈807` — matches the observed `806` almost exactly, so this is a decent
local fit, **but it is explicitly NOT distinguishable, at this scale, from a slowly-saturating
function that merely looks power-law over this range** (e.g. `T(N) = A - B/N^{0.05}` type curves
can mimic a slowly-drifting power exponent over one order of magnitude). No conclusion beyond
"exponent currently ≈0.22-0.25 and drifting down slowly" is defensible from this data.

### 3. Structural explanation for the 4807 vs 11305 difference

Factored the seeds (via `sympy.factorint`, this round): `Q(4807)=P(4807)={11,19,23}` (`|Q|=3`),
`Q(11305)=P(11305)={5,7,17,19}` (`|Q|=4`). The certified Finite Core Theorem's enlarged cores are
`|S_0(4807)|=9` vs `|S_0(11305)|=12` — i.e. `11305`'s core is **1/3 larger**. Since an "extended
type" is (a subset of) `P(a_n)∩S_0`, the raw combinatorial space of possible extended types scales
like `2^{|S_0|}`: `2^9=512` for `4807` vs `2^{12}=4096` for `11305` — an **8x larger** nominal state
space (though realized types are a much smaller, structurally-constrained subset of this — observed
counts are `220` and `806` respectively, i.e. `43%` and `20%` of the naive `2^{|S_0|}` bound, so the
realized fraction is actually smaller for `11305`, not larger, but the absolute headroom is far
greater). This is a plausible, purely structural (not dynamical) explanation for why `11305`'s
convergence — if H2 is true and it does converge — would need a much longer runway than `4807`'s:
more base persistent types (`|Q|=4` vs `3`) recruit a bigger enlarged core via the Finite Core
Theorem's construction, and a bigger core has combinatorially more possible new "extended-type"
labels to still be discovering at any given `N`, even if the *rate relative to the size of its own
state space* is comparable across seeds. This is a **plausible qualitative account, not a proof** —
no attempt was made this round to quantify "rate relative to `2^{|S_0|}`" as a normalized statistic
across seeds (a natural follow-up: track `T(N)/2^{|S_0|}` or `T(N)/(\text{realized-type ceiling})`
instead of raw `T(N)`, which would partially control for this size difference and might reveal the
two seeds are on a much closer normalized trajectory than the raw counts suggest).

### 4. Does this suggest H2 is FALSE, or just slow to converge?

**Conclusion: the corrected numbers argue for "slow to converge," not "H2 is false."** Three points
support this over round 24's more alarmed framing:
- The literal `~sqrt(N)` claim for `11305` does not survive a proper local-exponent
  recomputation — the true local exponent (~0.22-0.28) is well below `0.5` even at its highest,
  and (per point 1) it IS decreasing, just more slowly than `4807`'s.
- `4807` itself looked "flat-ish" (local exponent ~0.13-0.18) all the way out to `n=500,000` and
  only started its sharp collapse toward 0 between `500k` and `1,000,000` — i.e. `4807`'s own
  convergence signature was invisible at the SAME scale (`500k`) where `11305` currently sits
  (`750k`). Since `11305` has a structurally larger state space (point 3), it is entirely
  consistent with H2 holding for both seeds that `11305`'s analogous collapse simply has not
  started yet at `n=750,000` and would appear somewhere past `n≈1-2M`, by direct analogy with how
  `4807`'s collapse only appeared past `n≈500k-1M`.
- No genuine structural obstruction to eventual convergence was found for `11305` this round (no
  new unbounded-growth mechanism, no counterexample construction) — this is purely a numeric
  deceleration-rate observation, and the observed deceleration, while slow, is present, not absent.

**However, this is NOT a proof or even strong evidence FOR H2 at `11305`** — it is a correction of
round 24's overly pessimistic reading (literal sqrt growth), replacing it with an honest "genuinely
inconclusive, but consistent with delayed convergence rather than divergence" verdict. A fully
convincing resolution would need either (a) computational reach well past `n=2-5M` for `11305`
(infeasible this round given the sandbox's background-process constraint — each synchronous call is
capped at ~600s wall-clock, and the simulator's apparent super-linear time-per-term growth, likely
driven by bigint bitmask width growing with `n` and by the widening candidate-search gaps at larger
`a_n`, makes reaching millions of terms non-trivial even with the SPF-sieve speedup), or (b) an
actual structural/analytic argument (not simulation) bounding the type-recruitment rate, which
remains completely absent from the certified lemma stack (per round 24's finding: "no lemma
anywhere in `lemmas/` currently bounds `P(a_j)\ S` from above").

### Recommendation to the outliner
- Do NOT treat `11305`'s numeric behavior as a counterexample-direction for H2 — the sqrt-growth
  reading that would have supported that framing does not survive a corrected local-exponent
  analysis.
- Do treat the size of the Finite-Core-Theorem-enlarged `S_0` (`|S_0|`, itself driven by `|Q|=|P(a_1)|`
  and the number of persistent base types) as a genuine seed-dependent scale parameter that likely
  controls how much runway is needed before any convergence becomes numerically visible — a future
  round wanting to test H2's existence hypothesis on `11305` specifically should either (a) push the
  simulation further (ideally with a checkpointing/resumable script, since this round's scripts
  restart from n=1 each call and the sandbox kills background jobs, wasting ~130-500s of
  recomputation per call), or (b) normalize by `2^{|S_0|}` or another size-adjusted statistic to make
  a fairer visual/quantitative comparison across seeds of different `|Q|`.
- The environment note (background processes die at Bash-call boundaries) is worth recording in
  `math-explorer` memory for any future round attempting multi-minute simulations.

### Scripts
`/tmp/round-25/fastsim2.py` — SPF-sieve simulator, reusable/extendable (add a checkpoint/resume
feature before the next large push). Raw logs: `/tmp/round-25/run_4807.log`,
`/tmp/round-25/run_11305_v3.log`, `/tmp/round-25/run_11305_v4.log`.
