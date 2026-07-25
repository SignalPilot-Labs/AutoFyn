## imo-2026-03 (lens: Sigma-shape functionals in `global-lp-vertex-sufficiency`)

### What the Sigma-shape functionals precisely are (re-derived from the file)

Setting: balanced region $\overline{B(n)}$, $k=n+1$ pieces. By the certified
Global Vertex Lemma, for every $p$, $V(p)=\min_{\sigma\in\Sigma(n,k),\
x_\sigma(p)\ge0}\mathrm{OddSum}(x_\sigma(p)\cup\text{untouched }p_j)$, where a
**shape** $\sigma$ is: a cut-allocation $\mathbf m=(m_1,\dots,m_k)$,
$\sum m_i\le n$; for each split piece $i$ ($m_i\ge1$) a set-partition of its
$m_i+1$ fragment-slots into blocks, one block per split piece designated
**free**, the rest pinned to a value in $\{0,p_1,\dots,p_k\}\setminus\{p_i\}$
($k$ choices). $x_\sigma(p)$ is then affine in $p$ (pinned blocks literal,
free block solved from $\sum(\text{fragments})=p_i$).

$L$ (the finite functional list driving the vertex/cell reduction) =
{every coordinate of every $x_\sigma(p)$} $\cup$ {every branch-comparison
difference $f_\sigma(p)-f_\tau(p)$, $\sigma,\tau\in\Sigma$} $\cup$ {the region's
own $n+2$ functionals: $p_1-\tfrac12$, the $n$ gap slacks, and $p_k$}.
$Q$ = solutions of every $(k-1)$-subset of $L$ set to $0$. $Q_{\mathrm{region}}$
(now fully closed) = the sub-list drawn only from the last group.
**$\Sigma$-shape functionals = everything else in $L$**: (a) validity
boundaries $x_\sigma(p)_j=0$ (a fragment or the free-block formula hits its
lower bound), and (b) branch-comparison boundaries $f_\sigma(p)=f_\tau(p)$
(the point where the optimal *response shape* switches). $Q\setminus
Q_{\mathrm{region}}$ = every candidate vertex arising from $(k-1)$-subsets
that include at least one such functional (mixed subsets are the generic
case: most vertices of $L$'s arrangement lie on 1 region functional + $(n-1)$
$\Sigma$-shape functionals, or similar mixes).

**A found inconsistency worth flagging to the outliner/builder.** Section
1, item 1's literal English defines the shape's degrees of freedom as **"a
single free block... designated among all blocks across the whole shape"**
(i.e. one free block total, regardless of how many pieces are split). But
the very next paragraph's proof (and the cited Two-Piece-Split Vertex
Lemma) requires **"free block, one per piece $i$ that is actually
split"** — each split piece needs its own free block to absorb its own
independent sum-equality, or the linear system is generically
over-determined/inconsistent. These two sentences in the same file
contradict each other. The terser certified lemma
(`lemmas/global-vertex-lemma-and-lipschitz-continuity.md`) is vague enough
("cut allocation + block partition + pin assignment") to not directly
carry the bug, but whoever formalizes $\Sigma(n,k)$ precisely to bound
$|\Sigma|$ must use the **one-free-block-per-split-piece** version (matching
the proof and the two-piece special case), not the literal item-1 sentence.
Flag this explicitly so the builder doesn't silently inherit the wrong
(too-restrictive, single-free-block) reading, which would undercount
$\Sigma$ and could invalidate the vertex characterization for $\ge2$
simultaneously split pieces.

**A second, unresolved subtlety (not previously flagged in the file):**
$f_\sigma(p):=\mathrm{OddSum}(x_\sigma(p)\cup\text{untouched})$ is only
literally *affine* in $p$ if the **internal sort order** of the fragment/
untouched values named by $\sigma$ stays fixed. Nothing in $\sigma$'s
combinatorial data (cut-allocation + block partition + pin assignment)
pins this order; $L$'s definition as written (fragment coordinates +
inter-branch differences $f_\sigma-f_\tau$) does **not** include the
*intra*-branch pairwise coordinate differences needed to make each
$f_\sigma$ genuinely affine on a cell. Either (i) this is implicitly fixed
because the pin-value structure forces a generic order that never flips
within one shape's validity region (would need proof), or (ii) $L$ needs a
further enlargement (all pairwise differences of $x_\sigma(p)$'s own
coordinates, and of each coordinate vs. each untouched $p_j$) to make
Lemma 4.1's "cell-wise constancy" argument actually go through for
$f_\sigma$ itself, not just for validity/between-branch comparisons. This
is worth a targeted check before trusting any $|\Sigma|/|L|$ bound.

### Distinct openings for the outliner

1. **Restricted-shape sufficiency (the file's own top priority, and the
   most concrete).** Section 5's numeric finding — a 3-simultaneously-split
   shape (splitting $p_1,p_2,p_3$ each into 3, tying against the untouched
   tail) clears $c(6)$ at the one catalogued hard $n=6$ instance by
   $50\times$ the margin of the 2-piece/Subset-Tie tools — suggests trying
   to prove: **the optimal response shape always has a bounded number of
   simultaneously-split pieces** (e.g. $\le3$, or $\le$ some small function
   of $n$), which would let $\Sigma$ be replaced by a much smaller
   sub-family $\Sigma_{\le3}(n,k)$ that might have a tractable closed-form
   count/classification. This sidesteps full classification of $\Sigma$.
2. **Monotonicity-instead-of-vertex-enumeration (a genuinely different
   framing, not explored yet).** Rather than reducing $V$'s max over
   $\overline{B(n)}$ to vertices of the whole $L$-arrangement, try to show
   directly (via an exchange/coupling argument on the *construction* side,
   not the LP side) that **moving $p$ toward the region's own boundary
   (shrinking a gap toward $\gamma(n)$, or pushing $p_1\to1/2$) can only
   weakly decrease $V(p)$** — a one-directional monotonicity claim far
   weaker than concavity, that if true would force the true maximizer to
   already lie in the closure of the region-only boundary, i.e. in
   $Q_{\mathrm{region}}$ (already fully closed!), making the whole
   $\Sigma$-classification unnecessary. This is a distinct attack:
   construction-side monotonicity instead of LP-vertex bookkeeping. Not
   attempted by any approach so far. Caution: concavity AND quasi-concavity
   are both already refuted along one specific interior line (see Dead
   Ends below), so a *global* line-monotonicity claim is false; a *narrow*
   per-coordinate-direction claim (only moving toward the region's own
   facets, not arbitrary lines) is the only version not yet ruled out.
3. **Direct exact-arithmetic upgrade of Section 5's numeric witness.**
   Turn the $n=6$, 3-piece "generalized Subset-Tie" construction into an
   exact rational formula (the fragment pattern is visibly a clean
   "tie each fragment of the 3 split pieces against one untouched tail
   piece, dump the residual into one singleton" rule) and prove it in
   general $n$/general instance, by analogy with the already-certified
   $k$-Anchor-Merge Lemma mechanism used to close $Q_{\mathrm{region}}$'s
   genuine vertices. If a clean closed form generalizes, it may directly
   supply an upper bound at *every* point of the balanced region (bypassing
   vertex-enumeration entirely — a genuine additive construction covering
   the whole region, in the spirit of `lp-duality-split-polytope`'s
   Multi-Piece Sufficiency Theorem but region-wide rather than
   family-specific).
4. **Growth-rate impossibility check.** Given $|\Sigma(n,k)|$'s explosive
   growth (below), a full closed-form classification of all of $Q$ is very
   likely intractable as a route to a clean olympiad-style proof; this is
   evidence *for* openings 1–3 (find a shortcut) and *against* pursuing raw
   enumeration/classification of all of $\Sigma(n,k)$ as the main line.

### Cheap-kill candidates
None obvious for outright ruling out $\Sigma$-shape vertices in general —
but the growth-rate computation below is a cheap kill of the "just
enumerate/classify all of $\Sigma(n,k)$ for general $n$" plan specifically
(super-exponential, ruled impractical as a direct route).

### Knowledge-base entries to use
- `knowledge_base.md`'s "Linear Algebra" section (LP/polytope vertex facts)
  — already the basis of the certified Finite-Cell theorem; nothing new to
  add there.
- "General Proof Methods" / extremal-principle style arguments (push to an
  extreme configuration, then case-split) are the natural fit for Opening 2
  (monotonicity toward the region boundary) — a construction-side, not
  LP-side, extremal argument.
- No entry in `knowledge_base.md` addresses bounding vertex counts of
  hyperplane arrangements generated by combinatorial "shape" families
  directly; this remains a bespoke combinatorial-geometry gap specific to
  this problem's $\mathrm{OddSum}$ structure.

### Analogous past problems (cruxes)
Searched the corpus (`combinatorics`/`extremal-principle`,
`linear-algebra-method`, and general "vertex"/"polytope"/"LP" keyword
matches across all domains). The 168 keyword hits are almost entirely
graph-theoretic "vertex of a graph," not "vertex of a polytope/LP" — no
genuine match to the specific mechanism here (finite hyperplane
arrangement from a combinatorially-generated affine functional family,
bounding its cell/vertex count). Closest tangential match: **aimo-0013**
(`combinatorics/extremal-principle`, "cut off a single convex-hull vertex
from all remaining points with one line, since all other points lie
strictly on one side of a supporting line at that vertex") — the general
idea of "reduce a global extremal claim to a single supporting-hyperplane
argument at one boundary point" is philosophically close to what Opening 2
(monotonicity toward the region boundary) would need, but it's a distant
analogy, not a directly reusable technique. **No genuinely analogous
crux found** for the specific combinatorial-shape-vertex-counting problem
$|\Sigma(n,k)|$ itself — do not force a match.

### Prior progress
$Q_{\mathrm{region}}$ (the entire region-only candidate sub-list) is fully
classified and fully closed for all $n\ge2$, certified in
`lemmas/finite-cell-vertex-reduction-and-region-classification.md`. The
Finite-Cell Affine-Vertex Reduction Theorem itself (reducing $V$'s max to
*some* finite candidate set $Q\supseteq Q_{\mathrm{region}}$, no concavity
needed) is certified in the same file / in
`lemmas/global-vertex-lemma-and-lipschitz-continuity.md`. Nothing has yet
touched $Q\setminus Q_{\mathrm{region}}$.

### Dead ends (do not retry)
- **Concavity of $V(p)$**: refuted (round 9), a genuine sign-alternating
  second-difference counterexample at $n=2$ along an explicit line,
  deficit $\approx0.0102$.
- **Quasi-concavity of $V(p)$ along a general line — also refuted, newly
  noted this round** (not previously stated explicitly in the file, but
  follows immediately from the round-9 counterexample's own three reported
  values: $V=0.5146,\ 0.5022,\ 0.5102$ at three equally-spaced points; the
  midpoint value $0.5022$ is strictly *less than both* endpoints, i.e.
  $V(\text{midpoint})<\min(V(a),V(b))=0.5102$ — a quasi-concavity
  violation, verified by direct arithmetic on the already-reported numbers,
  no new computation needed to trust it). **Consequence: Opening 2 above
  cannot be a blanket "V is quasi-concave" claim** — it would have to be a
  narrower, direction-restricted monotonicity (only moving toward the
  region's own defining facets, not an arbitrary interior line), which the
  existing counterexample does not obviously rule out (the counterexample
  line's direction relative to the region's own facet normals was not
  checked here — worth checking before building on Opening 2).
- **"Just enumerate $\Sigma(n,k)$ for general $n$" as a proof route**: not
  previously tried, but the growth-rate computation below makes it a
  practical dead end for a closed-form general-$n$ proof (see below);
  restrict to Opening 1 (bounded split-piece-count sub-family) instead.

### Small-case / intuition notes (conjecture / numeric, labeled as such)
Computed $|\Sigma(n,k)|$ ($k=n+1$) exactly by direct combinatorial
enumeration (Stirling numbers of the second kind, per-piece count
$\sum_{b=1}^{m_i+1}S(m_i+1,b)\cdot b\cdot k^{b-1}$ for a piece split into
$m_i+1$ slots — $b$ = number of blocks, $b$ ways to pick the free block,
$k$ pin-choices per remaining block, using the corrected "one free block
per split piece" reading), summed over all cut-allocations
$\mathbf m$ with $\sum m_i\le n$:

| $n$ | $\lvert\Sigma(n,n+1)\rvert$ |
|---|---|
| 1 | 11 |
| 2 | 307 |
| 3 | 14,019 |
| 4 | 889,251 |
| 5 | 72,221,214 |

Ratio between consecutive $n$: $\approx28,\ 46,\ 63,\ 81$ — growing
roughly *linearly in $n$* itself, consistent with genuinely super-
exponential (factorial-like, driven by Bell numbers of up to $n+1$
elements) growth of $|\Sigma(n,k)|$, hence of $|L|\sim|\Sigma|+|\Sigma|^2$
(branch-comparison pairs) and of $|Q|\sim\binom{|L|}{n}$. **Conjecture
(numeric only, not proved):** no closed-form polynomial-in-$n$ bound on
$|\Sigma(n,k)|$ exists, reinforcing that a *direct* enumeration-based proof
of the Existence Theorem for general $n$ is not viable; the realistic
routes are Openings 1–3 above (bounded-split-count sufficiency, or a
region-boundary monotonicity bypass, or a region-wide explicit
construction), not full classification.
