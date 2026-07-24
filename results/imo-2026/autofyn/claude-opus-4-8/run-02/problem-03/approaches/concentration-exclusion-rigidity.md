# Approach: concentration-exclusion-rigidity (imo-2026-03, IMO 2026 P3)

## Status
partial

## Approaches tried
- Round 6 (new, skeleton): registered the Cramer + single-column-concentration framing; step 2 used a
  cross-piece "mass exchange" — flagged infeasible by the outline-reviewer (product of simplices has
  no cross-piece moves; a tie-preserving direction would need `ker U≠0`, contradicting S-core).
- Round 7 (this round): **recast step 2 as the certified tie-breaking cut-slide argument** (Lemma I +
  imported Moves M2/M3), which provably stays in the minimizer set `G`. Proved rigorously: (i) the
  concentration mechanism `column = m·e_k ⇒ m∣det U` (cofactor expansion); (ii) the **Concentration
  Exclusion Theorem** — the ONLY concentrated column (`m·e_k`, `m≥2`) that can survive at the Φ-max
  minimizer is `m=2`, and every such surviving one is an **invisible** matched pair (`s_j=0`); (iii)
  the fatal unshared instance `{2,4/3,4/3,4/3,1}` gets its OWN exclusion (odd `m=3` ⇒ M3), genuinely
  distinct from self-similar's Lemma BD; (iv) a **Reduction Lemma** that peels every invisible `2·e_k`
  column together with its piece-row, preserving `f` exactly and reducing to a strictly smaller
  distinct-powers instance with NO concentration (`det U = ±2·det U'`, the factor 2 cancelling
  numerator and denominator in Cramer). All four verified numerically (`sympy`/`numpy`) on
  `{2,4/3,4/3,4/3,1}`, on the `n=3` even-concentration minimizer `{3,3,2,2,2,2,1}`, and on synthetic
  square systems. **Honest new negative finding:** even `m=2` concentration DOES occur at genuine
  S-core minimizers and makes the maximal-minor gcd even (`gcd=2` at `{3,3,2,2,2,2,1}`), so
  "benign-U = det/gcd `±1`" is FALSE as literally stated — the correct invariant is benign-ness of the
  **visible** (`s_j≠0`) reduced subsystem. Two gaps remain open (below).

## Current best

A rigorous, minimality-driven reduction of the whole obstruction to a **no-concentration visible
subsystem**, with the concentration obstruction itself fully characterised and (for the odd/fatal
case) fully excluded. Precisely:

- The concentration mechanism `column j = m·e_k ⇒ m∣det U` is proved (cofactor expansion).
- **Concentration Exclusion Theorem (proved):** at the tied non-degenerate Φ-max minimizer, the only
  surviving `m≥2` concentrated column is `m=2`, and it is always an invisible matched pair (`s_j=0`).
  Odd concentration (in particular the fatal `{2,4/3,4/3,4/3,1}`, `m=3`) is excluded by the certified
  tie-breaking cut-slide Move M3.
- **Reduction Lemma (proved):** every invisible `2·e_k` column peels off together with its piece-row,
  leaving `f` unchanged and a strictly smaller distinct-powers, concentration-free instance.

**Open gap 1 (the residual, honestly recorded):** benign-ness of the reduced *visible,
concentration-free* subsystem — its determinant is `±1` (square) / its maximal minors are coprime
(rectangular). This is step 3; it is NOT re-asserted here. What is genuinely new is that after the
Reduction Lemma the subsystem has NO concentrated column, so the `±1`-pivot claim, if true, no longer
competes with even matched pairs. **Open gap 2 (Positivity):** the visible numerator `Σ_{visible} s_i
det U_i ≠ 0`. Both are shared with the two live routes (they are the same minimality⇒benign-U wall).

## Setup and imported facts

Throughout, `f(P)=Σ_i σ_i b_i` is the alternating sum of the multiset `P` sorted descending
(`b_1≥b_2≥…`), `σ_i=(−1)^{i+1}`. Write `D_n=2^{n+1}−1`. The upper bound `c(n)≤2^n/D_n` is certified.
The lower bound reduces (certified) to:

> **(LBL).** Every refinement of `W_n={2^0,…,2^n}` using `≤n` cuts has `f≥1`.

and further (certified) to the single residual: `f≥1` at a **tied non-degenerate Φ-max minimizer
`P*`** of `f` over the product of simplices `K=∏_{k=0}^{n}Δ_k`, `Δ_k` fixing the total length `2^k` of
piece `k`. We import verbatim, from `results/imo-2026-03/lemmas/`:

- **(S-core)** `phimax-trivial-kernel`: with distinct values `w_1>…>w_p`, classes `C_j`, incidence
  matrix `U` (`(n+1)×p`, `U_{k,j}=μ_{k,j}=` number of sub-pieces of piece `2^k` equal to `w_j`), one
  has `Uw=b` with `b=(2^0,…,2^n)^{\!T}` and `ker U={0}` (full column rank, so `p≤n+1`).
- **(BF)** `odd-block-formula`: `f=Σ_j s_j w_j` where `s_j=Σ_{i∈\text{ranks of }C_j}σ_i`. For a tie-block
  occupying consecutive ranks `[a_j,b_j]` (`b_j−a_j+1=|C_j|`), `s_j=σ_{a_j}` if `|C_j|` is odd and
  `s_j=0` if `|C_j|` is even. Call `C_j` **visible** if `s_j≠0` (equivalently `|C_j|` odd) and
  **invisible** otherwise.
- **(I)** `cut-slide-derivative`: increasing a sub-piece `q` of block `l` by `ε` (it rises to the
  block's top rank `a_l`) changes `f` by `σ_{a_l}ε`; decreasing it by `ε` (it falls to the bottom rank
  `b_l`) changes `f` by `−σ_{b_l}ε`. Both are exact one-sided derivatives valid at ties.
- **(M2)** `two-invisible-pairs-mult-bound`: at `P*`, `μ_{k,j}≤3` for every `k,j`.
- **(M3)** `symmetric-odd-block-move`: at `P*`, if `|C_j|` is odd then `μ_{k,j}≤1` for every piece `k`.

Since `μ_{k,j}∈ℤ_{≥0}` and `b∈ℤ^{n+1}`, `U` and `b` are integer. When `p=n+1` (**square case**) `U` is
invertible (S-core), Cramer's rule gives `w_j=det(U_j)/det(U)` with `U_j:=U` with column `j` replaced
by `b`, hence by (BF)

> **(Cramer).**  `f·det(U)=Σ_j s_j·det(U_j)∈ℤ`,  a ratio of integers, `w_j` and `f` rational.

So `f≥1` requires control of `det(U)` (square) or the gcd of maximal minors (rectangular): this is the
common wall the non-integrality explorer proved unavoidable. This approach attacks the ONE structure
that breaks that control — a **concentrated value-class**.

## Step 1 — the concentration mechanism (proved)

**Definition.** Class `C_j` is **concentrated** if its column of `U` is `m·e_k` for some piece `k` and
integer `m≥2`; equivalently all `m=|C_j|` copies of `w_j` lie in the single piece `2^k` and `w_j`
occurs in no other piece (`μ_{l,j}=0` for `l≠k`, `μ_{k,j}=m`).

**Lemma 1 (concentration divides the determinant).** In the square case, if `C_j` is concentrated with
column `m·e_k`, then `m∣det(U)`, hence `|det(U)|≥m≥2`.

*Proof.* Expand `det(U)` along column `j`: `det(U)=Σ_{i=1}^{n+1}U_{i,j}\,\mathrm{cof}_{i,j}`, where
`\mathrm{cof}_{i,j}=(−1)^{i+j}M_{i,j}` and `M_{i,j}` is the `(i,j)` minor. Since column `j` is `m·e_k`,
`U_{i,j}=0` for `i≠k` and `U_{k,j}=m`, so `det(U)=m·\mathrm{cof}_{k,j}`. The cofactor is a determinant
of an integer matrix, hence an integer; thus `m∣det(U)`. As `ker U={0}`, `det(U)≠0`, so
`|det(U)|=m·|\mathrm{cof}_{k,j}|≥m≥2`. ∎

This is exactly the benign-U breaker: any surviving `m≥2` concentration forces `|det U|≥2`.
**Verified** on the certified non-minimizer `{2,4/3,4/3,4/3,1}` (`W_2`, piece `4` cut into thirds):
the `4/3`-column is `[0,0,3]^{\!T}=3·e_3`, `det(U)=3`, `3∣3`, and indeed `f=5/3`, `f·det(U)=5∈ℤ`.

## Step 2 — Concentration Exclusion Theorem (proved via tie-breaking cut-slide, stays in `G`)

The load-bearing content. It replaces the round-6 cross-piece "mass exchange" (which was infeasible in
`K`) by the certified **tie-breaking** cut-slide, a genuine feasible direction in a single simplex
`Δ_k` that provably keeps the point in the minimizer set `G` (or forces a strict `f`-descent / `Φ`-rise).

**Move M3, re-derived in full (the recast).** Suppose piece `2^k` contributes `μ_{k,j}≥2` copies of
`v:=w_j`, and `|C_j|=:μ` is **odd**. Take two of those copies; for small `s>0` grow one to `v+s` and
shrink the other to `v−s`, keeping the remaining `μ−2` copies at `v`. This move lives inside the single
simplex `Δ_k` (the sum of piece `k`'s sub-pieces is unchanged: `+s−s=0`), so it is a feasible line in
`K`, and for `|s|` small all lengths stay positive and no other distinct value enters the open interval
`(v−s,v+s)`. Hence the `μ` copies still occupy the same consecutive block of ranks `[a_j,a_j+μ−1]`,
with `v+s` now at the top rank `a_j` and `v−s` at the bottom rank `a_j+μ−1`. By Lemma I the block's
contribution changes by

  `Δf = σ_{a_j}·s + (−σ_{a_j+μ−1})·(−s)·(-1)`  — concretely, `Δf = s(σ_{a_j} − σ_{a_j+μ−1})`.

Since `μ` is odd, `a_j` and `a_j+μ−1` differ by the **even** number `μ−1`, so
`σ_{a_j}=σ_{a_j+μ−1}` and `Δf=0`: `f` is **exactly flat**, so the entire small segment lies in the
minimizer set `G`. But `Φ=Σx_i^2` changes only through the two moved copies, by
`(v+s)^2+(v−s)^2−2v^2=2s^2>0`, strictly increasing. Because `s=0` is interior to the feasible flat
segment and `Φ` is strictly increasing on it, `P*` is not `Φ`-maximal — contradiction. Therefore an
odd-size block has `μ_{k,j}≤1` for every piece `k`. ∎  (This is the certified Move M3; here it is
written out as the tie-breaking, stays-in-`G` mechanism the review requested. Verified: on
`{2,4/3,4/3,4/3,1}` the split `{4/3+s,4/3,4/3−s}` keeps `f=5/3` exactly and raises `Φ` by `2s^2`.)

**Theorem 2 (Concentration Exclusion).** At the tied non-degenerate Φ-max minimizer `P*`, every
concentrated class has `m=2`, and every such class is **invisible** (`s_j=0`). Equivalently: no
**visible** class is concentrated.

*Proof.* Let `C_j` be concentrated with column `m·e_k`, so `μ_{k,j}=m=|C_j|`.
- By **M2**, `μ_{k,j}≤3`, so `m∈{2,3}`.
- If `m=3` (odd), **M3** forces `μ_{k,j}≤1`, contradicting `μ_{k,j}=3`. Excluded.
- Hence `m=2`. Then `|C_j|=2` is even, so by (BF) `s_j=0`: the class is invisible.
Thus a concentrated class has `m=2` and `s_j=0`; contrapositively, a visible class (`s_j≠0`, `|C_j|`
odd) is never concentrated. ∎

**The unshared/fatal case, its OWN argument.** The reviewer flagged that the fatal instance
`{2,4/3,4/3,4/3,1}` (value `4/3` present ONLY in piece `4`, column `3·e_3`) must not be silently
handed to self-similar's Gap B. It is not: `4/3` is concentrated with **odd** `m=3`, so Theorem 2
excludes it directly through M3's tie-breaking cut-slide + strict-`Φ` contradiction — a
variational/Φ-maximality argument, structurally distinct from Lemma BD's degenerate-competitor
construction. (Self-similar's genuine Gap B is the *shared* even case, where `v=2^k/3` also occurs in
another piece so the global block is not this odd unshared block; that case is NOT reached by Theorem
2 and is not claimed here.) This closes the unshared-concentration case completely.

**The `m=2` carve-out (allowed).** A surviving concentration is a matched pair `{v,v}` alone in one
piece (column `2·e_k`, `s_j=0`). It is stable: by Lemma I, splitting `{v,v}→{v+s,v−s}` (both slide
directions) changes `f` by `s(σ_{a_j}−σ_{a_j+1})=2σ_{a_j}s`, an upward V-kink `Δf=2|s|>0` provided the
block starts at an odd rank (forced by minimality, else one direction descends). So it cannot be split
without leaving `G`; it is a genuine, allowed feature of minimizers. **Verified:** the `n=3` minimizer
`{3,3,2,2,2,2,1}` (piece `8={3,3,2}`, so `3` is a `2·e_8` matched pair, `f=1`) has both splits of
`{3,3}` giving `f=51/50>1` (upward), confirming the carve-out; and its maximal-minor gcd is `2`, not
`1` (see below).

## Step 3 — Reduction Lemma: peel every invisible concentration (proved)

Theorem 2 leaves exactly one obstruction to `|det U|=1`: invisible `2·e_k` matched-pair columns, which
each contribute a factor `2` (Lemma 1). We show these cancel out of `f` entirely.

**Lemma 3 (peeling).** Let `C_j` be an invisible concentrated class, column `2·e_k`. Then in the
square case
  `det(U)=(−1)^{k+j}·2·det(U')`, where `U'` is `U` with row `k` and column `j` deleted;
and, writing `w'` for `w` restricted to indices `≠j` and `b'=(2^l)_{l≠k}`, one has `U'w'=b'`, so `w'_i
= det(U'_i)/det(U')` for every `i≠j`, and the value is **unchanged**: `w_i=w'_i`. Consequently

  `f = Σ_{i:\,s_i≠0} s_i\,w_i = Σ_{i≠j:\,s_i≠0} s_i·\frac{det(U'_i)}{det(U')}`,

a Cramer expression for the **strictly smaller** instance `(U',b')` — one fewer piece, one fewer value,
still a distinct-powers-of-two RHS, and (by Theorem 2, applied after removal) with the removed
concentration gone.

*Proof.* Cofactor expansion of `det(U)` along column `j=2e_k` gives `det(U)=2·(−1)^{k+j}M`, `M:=`minor
deleting row `k`, col `j` `=det(U')`. For a visible index `i≠j`, `U_i` replaces column `i` by `b` but
retains column `j=2e_k`; expanding `det(U_i)` along that column gives `det(U_i)=2·(−1)^{k+j}M_i`, where
`M_i` is `det(U_i)` minus row `k`, col `j` `=det(U'_i)` (the reduced matrix with its `i`-th column set
to `b'`). Hence `w_i=det(U_i)/det(U)=M_i/M=det(U'_i)/det(U')`. Finally, because `C_j` is concentrated
in piece `k` only (`μ_{l,j}=0` for `l≠k`), each surviving equation `l≠k` reads
`Σ_{i≠j}μ_{l,i}w_i=2^l`, i.e. `U'w'=b'` with `w'_i=w_i`; the value of each visible `w_i` is literally
unchanged. Since `det(U)≠0`, `M=det(U')≠0`, so `U'` is invertible and the Cramer expressions are
valid. ∎

**Verified** numerically two ways: (a) on synthetic square integer systems with a planted `2·e_k`
column, `|det U|=2|det U'|` and `w_i` agree to machine precision between the full and reduced Cramer
ratios; (b) on the actual `n=3` minimizer `{3,3,2,2,2,2,1}` the maximal-minor gcd of the `4×3`
incidence is `2` (from value `3`'s `2·e_8` column), confirming even concentration genuinely lowers
benign-ness while leaving `f=1` because the offending class is invisible.

**Corollary.** Iterating Lemma 3 removes every invisible concentrated column. The result is a smaller
distinct-powers instance `(U^\star,b^\star)` with the SAME `f`, whose incidence matrix has NO
concentrated column at all, and on which `f=Σ_{i\,\text{visible}}s_i\,det(U^\star_i)/det(U^\star)`.

## Step 4 — what remains (honest gaps, NOT asserted)

After Steps 1–3 the residual is exactly:

> **(Gap 1 — benign visible subsystem).** The concentration-free reduced incidence `U^\star` (distinct
> powers-of-two RHS) has `|det U^\star|=1` (square) / coprime maximal minors (rectangular).

> **(Gap 2 — Positivity).** The visible numerator `Σ_{i\,\text{visible}}s_i\,det(U^\star_i)≠0`.

Given Gaps 1–2, Cramer gives `f=Σ s_i det(U^\star_i)/det(U^\star)∈ℤ` and `f≠0`; with `f≥0` (certified)
this yields `f≥1`, hence (LBL) and, with the certified upper bound, `c(n)=2^n/D_n`. **These two gaps
are the same minimality⇒benign-U wall the two live routes bottom out on** (Gap 1 ≡ Gap A/Gap D at
minimizers, Gap 2 ≡ Positivity). This approach does not close them; its contribution is to have
(a) removed the concentration obstruction cleanly and (b) shown it is invisible and peelable, so the
`±1`-pivot claim of Gap 1 now operates on a genuinely concentration-free system. The `±1`-pivot itself
is **not** re-asserted here — earlier drafts hid the wall behind "each non-concentrated class
contributes a `±1` pivot"; the honest statement is Gap 1 above.

**Rectangular caveat.** For `p<n+1`, Lemmas 1 and 3 hold with `det` replaced by the relevant maximal
minor: an invisible concentrated column `2·e_k` divides every maximal minor that uses row `k`, and the
peeling deletes row `k` and column `j` to reduce to a `(p−1)`-column instance. The gcd statement of
Gap 1 is the rectangular target. Full rectangular bookkeeping is not carried out here.

## Cases to cover — status
- Concentration `m=3` (odd, e.g. the `5/3` structure `{2,4/3,4/3,4/3,1}`): **CLOSED** (Theorem 2 / M3).
- Concentration `m≥4`: **CLOSED** (M2 gives `m≤3`).
- Concentration `m=2` (bisection/matched pair): **carved out as allowed**; peeled by Lemma 3;
  contributes `0` to `f` and cancels from Cramer. Handled.
- Square `p=n+1`: mechanism + reduction fully proved. Rectangular `p<n+1`: minor-gcd analogue stated,
  full bookkeeping OPEN.
- Positivity: OPEN (Gap 2).

## Why this is genuinely different from the other two routes
It targets the single-column concentration obstruction with Cramer/cofactor arithmetic plus the
tie-breaking cut-slide — not primal cycle-rank (self-similar) nor the dual λ-lattice
(dual-integer-certificate). Its decisive positive content this round is the **Concentration Exclusion
Theorem** (odd concentration is impossible at a Φ-max minimizer, the fatal instance dies here without
appeal to Gap B) and the **Reduction Lemma** (even concentration is invisible and peels off with `f`
preserved). Its decisive negative content is the honest finding that even matched pairs make the
maximal-minor gcd even, so the naive "benign-U" statement must be taken on the reduced visible system.

## Promotable lemmas
- **Concentration divides the determinant (Lemma 1).** Statement: in the square incidence `U` of the
  Φ-max minimizer, a class with column `m·e_k` forces `m∣det(U)`, so `|det U|≥m`. Proof: cofactor
  expansion along the column. (Proved above; verified on `{2,4/3,4/3,4/3,1}`.)
- **Concentration Exclusion Theorem (Theorem 2).** Statement: at the Φ-max minimizer every concentrated
  class has `m=2` and is invisible (`s_j=0`); no visible class is concentrated; the odd unshared
  instance `{2,4/3,4/3,4/3,1}` is excluded via M3. Proof: M2 + M3 + parity of `s_j`. (Proved above.)
- **Invisible-concentration peeling (Lemma 3).** Statement: an invisible `2·e_k` column satisfies
  `det U=±2 det U'` and its removal (with row `k`) preserves every visible `w_i` and the value `f`,
  reducing to a smaller distinct-powers concentration-free instance. Proof: cofactor cancellation of the
  factor `2` between numerator and denominator. (Proved above; verified numerically, square + `n=3`.)

## Full proof
Not present — Status is `partial` (Gaps 1 and 2 open; benign visible subsystem + Positivity remain).
