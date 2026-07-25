## imo-2026-03

global-lp-vertex-sufficiency: revise
Target: the whole problem's upper bound direction — for every $n$ and every
LB partition $p$ (in particular every $p$ in the balanced region
$\overline{B(n)}$), some XY response achieves $\mathrm{OddSum}\le c(n)$,
i.e. $V(p)\le c(n)$ everywhere, completing the Existence Theorem and hence
$c(n)=2^n/(2^{n+1}-1)$'s upper-bound half.
Technique: finite hyperplane-arrangement / cell-wise-affine-vertex reduction
(already certified, concavity-free) narrowed to a *bounded-split-piece-count*
sufficiency argument, per this round's explorer's Opening 1 — replace full
classification of $\Sigma(n,k)$ (shown super-exponential, hence a dead end as
a direct route) by proving the true maximizer never needs more than a small,
fixed number of simultaneously-split pieces.
Skeleton:
  1. **Mandatory first step, textual/logical fix (no new math, must be done
     before any builder touches $\Sigma$-classification):** correct Section
     1, item 1's "one free block... across the whole shape" sentence to read
     "one free block **per split piece**" — matching the proof paragraph, the
     cited Two-Piece-Split Vertex Lemma, and the actual mechanism used
     everywhere else in the file. This is a one-sentence textual fix but is
     load-bearing: the explorer found the literal wrong reading would
     undercount $\Sigma$ and invalidate the vertex characterization for
     $\ge2$ simultaneously-split pieces. Builder must re-verify the corrected
     reading against the certified lemma file
     (`lemmas/global-vertex-lemma-and-lipschitz-continuity.md`) and the Two-
     and Single-Piece-Split Vertex Lemmas before proceeding.
  2. **Resolve the second flagged subtlety before trusting any cell-affineness
     claim**: check whether $L$ (the functional list) needs the *intra-branch*
     pairwise coordinate differences added — i.e. for a fixed shape $\sigma$,
     do all pairwise differences among $x_\sigma(p)$'s own coordinates (and
     between each coordinate and each untouched $p_j$) already have constant
     sign on every cell of the *existing* $L$-arrangement, or can the internal
     sort order used to compute $f_\sigma(p)=\mathrm{OddSum}(\cdots)$ flip
     within one shape's own validity region? Builder should either (i) prove
     the order is already pinned by validity + branch-comparison functionals
     already in $L$ (a genuine short lemma, likely via the pin-value structure
     forcing genericity), or (ii) explicitly enlarge $L$ with these pairwise
     differences and re-verify Lemma 4.1/4.2 hold verbatim (they use only
     finiteness+affineness of $L$, so this should be routine once (ii) is
     chosen) — do not silently assume (i) without a proof.
  3. **Restricted-shape sufficiency (the main new target, Opening 1):** prove
     that the true maximizer $p^*$'s optimal XY response never needs more
     than $s_0$ simultaneously-split pieces for some small fixed $s_0$ (try
     $s_0=3$ first, per Section 5's numerically-confirmed 3-piece witness at
     $n=6$ clearing $c(6)$ by $50\times$ the margin of any 2-piece tool).
     Mechanism to try: an exchange/local-improvement argument on the
     *construction* side — given any XY response with $>s_0$ split pieces
     achieving some value $V_0$, show a response with $\le s_0$ split pieces
     achieves $\le V_0$ as well (a genuine "more pieces never strictly
     necessary beyond $s_0$" claim), OR a direct closed-form generalization of
     Section 5's numeric witness (crux: the generalized Subset-Tie /
     $k$-Anchor-Merge pattern — tie each fragment of $s_0$ split pieces
     against one untouched tail piece, dump the residual into one singleton),
     proved exactly and shown to clear $c(n)$ at every point of
     $\overline{B(n)}$, not just the one catalogued instance.
  4. **If step 3's bounded-count claim is proved:** $\Sigma_{\le s_0}(n,k)$
     (only shapes with $\le s_0$ split pieces) replaces $\Sigma(n,k)$ in the
     Finite-Cell Theorem; its growth is polynomial in $n$ (fixed $s_0$ bounds
     the combinatorial blowup), making the vertex/candidate enumeration
     tractable in closed form, completing the Existence Theorem.
Key lemmas (claim + mechanism):
  - **Free-block-per-split-piece correction** — because the linear system
    characterizing a vertex needs one degree-of-freedom absorber per
    independent piece-sum equality; one split piece contributes exactly one
    such equality regardless of how many other pieces are split.
  - **Bounded split-count sufficiency (the crux, unproved)** — conjectured
    because $\mathrm{OddSum}$'s marginal gain from splitting an $(s_0{+}1)$-th
    piece, once $s_0$ pieces are already tied against tail landmarks, is
    provably $\le$ the gain achievable by re-tuning the existing $s_0$-piece
    split's own free parameters (an exchange argument, not yet written down).
Open gaps: the entire bounded-split-count sufficiency claim (step 3) is new
and unproved; the intra-branch order subtlety (step 2) is unresolved.
Cases to cover: $s_0=3$ primary target; if that fails numerically at larger
$n$, escalate to $s_0=4,5,\dots$ but flag if $s_0$ appears to grow with $n$
(would kill this route, per the explorer's growth-rate warning).
Watch out for: do NOT assume quasi-concavity or any global monotonicity of
$V(p)$ — both refuted this round (quasi-concavity via the round-9
counterexample's own three reported values). Do not silently reuse the
uncorrected "one free block total" reading anywhere downstream.

self-similar-induction-on-n: revise
Target: the whole lower-bound direction — for every $n$, LB's geometric
partition guarantees $\mathrm{OddSum}\ge c(n)$ against every XY refinement,
i.e. $T(n)$ holds for all $n$ (currently reduced to the still-open $j\ge2$
trichotomy: Case A circular/dead, Case B reduced-but-unproved, middle regime
untouched, plus gap (b)(ii)).
Technique: **genuine reframing, not a bypass** — per this round's explorer's
finding of a structural correspondence with global-lp-vertex-sufficiency's
machinery, treat $\mathrm{OddSum}(B\cup S)$ (for $B$ the split of the top
piece, $S$ the tail refinement) as **cell-wise affine in $B$** within a fixed
interleaving pattern between $B$'s and $S$'s sorted values, and reduce the
middle regime / Case B / gap (b)(ii) to a finite vertex enumeration — the
identical mechanism as the certified Finite-Cell Affine-Vertex Reduction
Theorem and Region-Vertex Classification Theorem, adapted (not cited
verbatim — the domain differs: fixed $S$, varying $B$ on a simplex of fixed
sum, vs. varying $p$) to this setting.
Skeleton:
  1. **Formalize the adaptation precisely** (this is new content, not a copy):
     fix the tail $S$ (or, for gap (b)(ii), fix $T$) and the piece-count $j+1$
     of $B$. For a fixed "interleaving cell" (a fixed relative rank pattern
     between $B$'s sorted coordinates and $S$'s sorted values), show
     $\mathrm{OddSum}(B\cup S)=\sum_{\text{odd merged rank}} (\text{that
     coordinate of }B\text{ or }S)$ is literally affine (in fact linear, 0/1
     coefficients) in $B$'s coordinates — a short direct proof from the
     definition of merged sort order, not requiring the heavier machinery
     global-lp-vertex-sufficiency needed (that approach's affineness required
     solving a free-block equation; here $B$'s coordinates ARE the free
     variables directly, sum-constrained to $V$, so this should be genuinely
     easier).
  2. **Vertex reduction:** since $B$ ranges over the polytope
     $\{\sum b_i=V,\ b_i>0,\ (\text{regime-specific bound like }b_1<2^{m-1}
     \text{ or }b_1\ge\mu),\ \le j{+}1\text{ parts}\}$ intersected with one
     interleaving cell (itself a polytope, cut out by the pairwise
     inequalities defining that rank pattern), and the objective is affine on
     each cell, the maximum over $B$ within a cell is attained at a vertex of
     that cell (same elementary polytope-vertex fact already proved in
     `lemmas/finite-cell-vertex-reduction-and-region-classification.md` —
     reuse the proof, it is domain-independent). Enumerate cells for small
     $j$ (start at $j=2,3$, matching the round's own numeric evidence that
     maximizers there are near-tied/vertex-like) and classify vertices
     exactly, evaluating $\mathrm{OddSum}$ at each via already-certified tools
     ($k$-Anchor-Merge Lemma, Companion Peeling Lemma).
  3. **Apply to the middle regime first** (the weakest link, currently zero
     reduction at all): show the middle regime's extremal $B$ (subject to
     $\mu\le b_1<2^{m-1}$) is a vertex of its cell, evaluate, and check
     $\ge2^m$ holds there by direct computation (small $j$, small $m$ first,
     then generalize the closed form as the $k$-Anchor-Merge/Region-
     Classification proofs did).
  4. **Apply to gap (b)(ii)** using the vertex + Single-Insertion Lemma
     combination the explorer proposed: at the piece-cap-saturated maximizer
     (a vertex with a specific tie pattern), show the "add mass to the
     smallest tied group" move stays within one cell (no rank crossing) as
     long as possible, and use the certified Single-Insertion Lemma to
     exactly quantify any unavoidable rank-crossing correction.
  5. **Cross-check against global-lp-vertex-sufficiency's cell-count growth
     finding**: before investing in full vertex classification for general
     $m,j$, check numerically/combinatorially whether this polytope family's
     cell count grows tamely (unlike $\Sigma(n,k)$'s confirmed super-
     exponential blowup) — if it also explodes, this reframing inherits the
     same tractability wall and should be scoped to small $j$ (matching
     Case B/middle-regime's typical $j\le3$ numeric extremal witnesses)
     rather than attempted in full generality.
Key lemmas (claim + mechanism):
  - **Cell-wise affineness of $\mathrm{OddSum}(B\cup S)$ in $B$** — because
    within one fixed merged-rank pattern, which coordinates of $B$ land at
    odd rank is fixed, so $\mathrm{OddSum}$ is literally a 0/1-linear
    functional of $B$'s coordinates (no free-block-solving step needed, since
    $B$'s own coordinates are already free, unlike global-lp-vertex-
    sufficiency's fragment-of-a-fixed-$p_i$ setting).
  - **Vertex-attainment of the cell-restricted maximum** — standard: max of
    an affine functional over a compact convex polytope cell is at a vertex
    (identical elementary proof already certified, reused verbatim here).
Open gaps: the entire vertex classification (steps 2-4) is new, unattempted
work; step 5's tractability check is a prerequisite sanity check, not yet
done.
Cases to cover: the full trichotomy (Case A already closed as circular —
do not re-attempt; Case B and the middle regime are the targets; gap (b)(ii)
is the piece-cap-saturated sub-case, treated separately in step 4).
Watch out for: do not conflate this with global-lp-vertex-sufficiency's own
$\Sigma(n,k)$ — the two are analogous in mechanism but operate on genuinely
different polytopes (fixed-$S$-varying-$B$ here vs. varying-$p$ there); a
correspondence under a "piece values <-> $p_i$" dictionary is *conjectured*
by the explorer but not verified — check this explicitly early, since if a
literal correspondence holds it may let results transfer directly instead of
needing independent re-derivation.

greedy-reduction-geometric: advance
Target: the whole lower-bound direction, specifically closing Level-
Absorption (Subcase (b) of Theorem 7'$(m,k;L)$'s inductive step) — the sole
remaining open sub-problem of the general interleaved joint Case 2.
Technique: direct reduction + case split (WLOG parameter elimination, then
peeling/induction on the two remaining regimes), reusing certified Theorem 7,
Theorem 7a, Theorem 13, and Companion Peeling.
Skeleton:
  1. **Adopt the free WLOG reduction found this round, immediately, at zero
     cost:** $b_2=2^{m-1}$ exactly (the general $b_2\in[2^{m-2},2^{m-1}]$
     case follows a fortiori, since $b_2$ only appears as the target's RHS
     and in $\max(P)<b_2$, both weakenings when $b_2$ shrinks). This drops
     one free parameter before any proof attempt.
  2. **Close Case B first (quick win, per explorer's numeric finding of
     substantial slack, worst margin $\approx0.34$ at $m=4$, zero near-ties
     found in 23,905 trials):** $\max(P)<2^{m-2}$. Try a direct
     Dominance-Chain / Theorem-13-insertion argument treating $2^{m-2}$ as
     the true dominant element of the merge (since it dominates all of $P$
     by hypothesis) and $P$ as "extra" mass inserted via the certified
     General Insertion Monotonicity (Theorem 13) on top of a Theorem-7a-style
     baseline computed on $\{2^{m-2}\}\cup S'''$ alone — check whether this
     baseline, which the peeling machinery should give cheaply, already
     clears $2^{m-1}$ once $P$'s full sum ($2^{m-1}$) is accounted via a
     second insertion step. This is the explorer's flagged "worth confirming/
     closing outright next round as a quick win."
  3. **Then attack Case A** ($\max(P)\ge2^{m-2}$, genuinely hard, confirmed
     by the explorer to inherit the identical peel+insert shortfall as the
     general problem — do not expect a cheap closure). Per the explorer's
     numeric localization, the true worst-case configurations have $|P|\ge3$
     in a near-geometric/self-similar shape (ratios near $1:2:4:8$), NOT
     $|P|=2$ — so any proof strategy must handle general $|P|$ from the start,
     not extrapolate from a 2-piece base case. Try the explorer's Opening 3:
     a Prefix-Run-Peeling-style decomposition (reusing certified Lemma 6)
     applied to $P$ itself as a two-tier object, tracking $q_2$ (second-
     largest of $P$) against $2^{m-3}$ (top of the $S'''$ tail) as the key
     interleaving comparison — the probe found the tight/zero-margin locus
     is exactly where $q_2$ is not small relative to $2^{m-3}$.
  4. **Do not retry** the structure-agnostic Split-Degradation bound or any
     variant of the Candidate Swap Lemma (both proved insufficient/false this
     round and last, including at the base case specifically) — any workable
     mechanism must extract a quantitative, rank-position-aware contribution
     from $P\setminus\{q_1\}$, confirmed necessary by direct computation.
Key lemmas (claim + mechanism):
  - **WLOG $b_2=2^{m-1}$** — because $b_2$ is monotone-favorable to shrink:
    proving the hardest instance suffices for all easier ones.
  - **Case B closure via dominant-element insertion** — because $2^{m-2}$
    dominates every element of $P$ by hypothesis, so treating $P$ as inserted
    mass on top of the $\{2^{m-2}\}\cup S'''$ baseline should only ever help,
    via the hypothesis-free Theorem 13.
  - **Case A's $q_2$-vs-$2^{m-3}$ interleaving condition** — because the
    numeric worst case's near-tightness specifically tracks whether $P$'s
    second-largest fragment out-ranks the tail's own second level, exactly
    the kind of comparison a Prefix-Run decomposition of $P$ itself (not just
    of $A\cup\Gamma$) can capture.
Open gaps: Case B's closure (step 2) and Case A's full proof (step 3) are
both new, unattempted.
Cases to cover: Case A ($\max(P)\ge2^{m-2}$) and Case B ($\max(P)<2^{m-2}$),
exhaustive by construction.
Watch out for: verify Case B's proposed mechanism against a fresh exact
stress test (per standing rule) before writing it up — "substantial slack
numerically" is evidence a cheap proof exists, not a guarantee any specific
mechanism works. Do not let Case A's proof accidentally assume $|P|=2$.

lp-duality-split-polytope: advance
Target: the whole upper-bound direction (this approach's Necessity+
Sufficiency picture for the triangular family is complete; its ongoing role
is as a tool/witness supplier to the general upper-bound direction, per
round 10's own "Next" note).
Technique: exact-arithmetic construction + scaling-identity toolkit, reused
by cross-approach citation.
Skeleton:
  1. **Directly test whether the Multi-Piece Sufficiency Theorem's
     construction pattern (splitting $n$ of $n+1$ landmarks, tying doubled/
     even-block-neutral fragments) generalizes beyond the triangular
     (AP-landmark) family** to the balanced region's genuinely worst-case
     partitions — in particular, check it (or a close variant) against
     global-lp-vertex-sufficiency's Section 5 catalogued $n=6$ hard instance
     and Opening 3 (its "direct exact-arithmetic upgrade" target), since both
     approaches are independently reaching for the same kind of "$\ge3$-
     simultaneously-split, even-block-neutral" construction family from
     different directions.
  2. **If a general (non-AP-specific) version of the Even-Block-Neutrality
     mechanism can be shown to apply at any point of the balanced region**
     (not just the triangular family — this round's own numeric check found
     it does NOT trivially transfer to LB's geometric partition, ratio
     $\approx1.0$ at the threshold), that would hand global-lp-vertex-
     sufficiency exactly the region-wide explicit construction its Opening 3
     is asking for. This is honestly a long shot per this round's own
     negative finding at LB's geometric partition — treat as a secondary,
     not primary, target.
  3. Otherwise, stay in tool-supplier mode: keep the Consecutive-Block AltSum
     Formula, Bottom-Block-Doubling, and Even-Block-Neutrality Lemma ready
     for citation by name (already certified), and do not duplicate
     global-lp-vertex-sufficiency's own vertex-classification effort.
Key lemmas (claim + mechanism): none new required if step 1/2 come up empty;
reuses certified `lemmas/consecutive-block-altsum-and-bottom-block-doubling.md`
and `lemmas/multi-piece-sufficiency-triangular-family.md` throughout.
Open gaps: whether the Even-Block-Neutrality construction mechanism
generalizes past AP-structured landmarks (step 2) — genuinely open, evidence
so far (one numeric check at LB's own partition) is negative.
Cases to cover: none new — this is an exploratory/tool-supply round.
Watch out for: do not overclaim a "region-wide construction" from the
triangular-family result — round 9/10 already established this family is
not shown to be (and likely is not) LB's actual extremal partition; keep the
scope note from round 10 intact.
