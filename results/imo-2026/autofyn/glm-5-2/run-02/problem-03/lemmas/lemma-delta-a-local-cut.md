# ΔA closed form for a local cut

**Statement.** Let `q_1 ≥ q_2 ≥ … ≥ q_M` be the current sorted pieces with
alternating advantage sum `A = Σ_i (−1)^{i+1} q_i` (1-indexed; sign of `q_i` is
`(−1)^{i+1}`). Refine by splitting the rank-`r` piece `q_r` into two pieces
`a ≥ b` that land at **adjacent ranks r, r+1** in the new sorted order (the
*local* case: `q_{r−1} ≥ a ≥ b ≥ q_{r+1}`). Let
`T = Σ_{i > r} (−1)^{i+1} q_i` be the old tail alternating sum (ranks `> r`,
with their GLOBAL rank signs). Then the change in the alternating sum is

`ΔA = 2·((−1)^r · b − T)`.

For non-local cuts (a sub-piece jumps past a neighbour), the tail re-indexes
differently and this closed form does not apply directly.

**Derivation.** The rank-`r` term `(−1)^{r+1} q_r = (−1)^{r+1}(a + b)` is replaced
by `(−1)^{r+1} a + (−1)^{r+2} b = (−1)^{r+1}(a − b)`, a change of
`(−1)^{r+1}·(−2b) = 2b·(−1)^r`. The tail (ranks `> r`) shifts by one rank,
flipping every sign, so the new tail contribution is `−T`, a change of `−2T`.
Total: `ΔA = 2b·(−1)^r − 2T = 2·((−1)^r b − T)`. ∎

**Why this matters.** The `−2T` term is the **parity-flip-on-tail** obstruction:
splitting a piece at rank r flips the sign of every tail piece, so a "bisect the
largest" move does not reduce to a clean half-scaled residual game — the tail's
parity is scrambled. This is the load-bearing reason the per-mark monovariant /
one-mark value-recursion approach (see `approaches/induct-one-mark.md`, Lemma U
gap) fails: the value recursion `1/f(n+1) = 1 + 1/(2 f(n))` is per-ROUND (both
players add a mark), not per-Xiang-mark, and a single Xiang mark cannot achieve
the full recursion step because of the `−2T` parity flip.

**Verification.** Stress-tested on 4954 local-cut trials (random sorted
multisets, random adjacent-rank splits): 0 mismatches between the predicted
`ΔA` and the actual `alt(new) − alt(old)`.

**Knowledge-base tools.** Invariants & monovariants (linearization of the
alternating sum under refinement).

**Where proved.** `approaches/induct-one-mark.md`, "Lemma L / General-n claim."
