## imo-2026-03

- Distinct openings:
  1. **Cardinality-Constrained Half-Sum Lemma (new, most promising).** All
     numeric evidence (see below) suggests that the true fix for the
     odd-excess ($e=1$, $k\ge2$) outside-window residual is NOT a
     different constant in the existing algebraic bound, but a genuinely
     sharper lower bound on $\mathrm{OddSum}(R\cup\Gamma_{k-1})$ that uses
     $\mathrm{GT}(m)$'s own cardinality cap $|R|\le m$ (equivalently
     $|D|\le m+1$) — something the certified cap-free Half-Sum Corollary
     ($\mathrm{OddSum}(N)\ge\mathrm{sum}(N)/2$) structurally cannot supply,
     since it is tight (attained) by any even-count all-equal multiset,
     which the cap can rule out as infeasible. Concretely: fixing
     $\mathrm{sum}(R)=S$, $\max(R)\le\mathrm{cap}:=2^{k-1}$, $|R|\le m$,
     the *minimal feasible count* is $n_0=\lceil S/\mathrm{cap}\rceil$; when
     $n_0$ is forced odd (or more generally when no legal $n\le m$ achieves
     an exact even/near-equal split), $\mathrm{OddSum}(R)$ must exceed
     $S/2$ by a quantifiable slack tied to $n_0$'s parity/near-tightness.
     This slack is exactly what the current proof's Claim B is missing at
     $a_1$ near $2^k$. This is a genuinely different lemma to prove
     (extremal count-constrained minimization of OddSum, not the constant-count-free Half-Sum bound), not a bypass of the same wall.
  2. **Direct full-target verification (not via the LB/T split at all).**
     Skip the Half-Sum-Corollary route entirely for the residual case and
     directly bound $\mathrm{OddSum}(D\cup\Gamma_{m-1})$ using an
     extremal/greedy argument on the *whole* multiset (not the decomposed
     $R\cup\Gamma_{k-1}$ piece) — since the decomposition is exactly where
     slack is lost (the corrected chain plus Half-Sum bound stacks two
     independently-loose steps). A one-shot extremal argument on the
     capped multiset might close the gap with less bookkeeping.
  3. **Boundary-is-attained, not exceeded: prove equality holds in the
     literal limit $a_1\to2^k$ under the cap, then handle the interior of
     $[2^{k-1}+1,2^k]$ separately by monotonicity in the *actual* (not
     bound-only) OddSum.** Numeric evidence (below) shows the actual
     minimal value approaches the target from above as $a_1\to2^k^-$,
     suggesting the true worst point (under the cap) is the endpoint
     itself, with equality, not a strict violation anywhere in the closed
     range $(2^{k-1},2^k]$ — i.e. the "$\ge$" in the theorem's conclusion
     may need to become "$\ge$ with equality only at $a_1=2^k$" rather
     than strict, but no rescoping of the domain is evidently needed once
     the cap is used correctly.

- Candidate technique(s): extremal/vertex-style minimization of a
  piecewise-linear rank-sum (OddSum) over a simplex with cardinality AND
  magnitude caps — akin to the LP-vertex reasoning already used elsewhere
  in this proof (`lp-duality-split-polytope`'s Perfect-Tie-Family /
  Mass-Constraint machinery) but applied here to $R\cup\Gamma_{k-1}$
  instead of the split-polytope. A "forced-parity-of-count" argument
  (pigeonhole on $\lceil S/\mathrm{cap}\rceil$) is the natural mechanism.

- Cheap-kill candidates: check whether the minimal-count formula
  $n_0=\lceil S/\mathrm{cap}\rceil$ and its parity alone (without needing
  the exact extremal shape) already gives enough slack via a crude bound
  $\mathrm{OddSum}(R)\ge S/2+\tfrac1{2n}(n\cdot\mathrm{cap}-S)$-style
  correction (an "all near-cap plus small remainder" construction) — if
  this crude correction already dominates $T_{\mathrm{odd}}$'s shortfall
  algebraically for every $(k,e{=}1,a_1\in[2^{k-1}+1,2^k])$, that is a
  cheap, closed-form fix requiring no new extremal-shape proof, only a
  clean pigeonhole count argument. This should be tried before any
  heavier LP-vertex machinery.

- Knowledge-base entries to use: none of `knowledge_base.md`'s generic
  entries were separately checked this pass (time budget), but internally
  the relevant certified tools are the **Half-Sum Corollary** and **Large-
  Sum Closure Theorem** (`lemmas/half-sum-corollary-and-large-sum-closure-
  theorem.md`), the **Even-target Companion Peeling identity and corrected
  $e$-fold $q=0$-chain** (`lemmas/even-target-companion-peeling-and-
  corrected-qzero-chain.md`), and the **Monotonicity Reduction Lemma**
  (`lemmas/monotonicity-reduction-and-unified-threshold-pair-peeling.md`).
  A **new** lemma (Cardinality-Constrained Half-Sum Lemma, or a "Forced-
  Odd-Count Slack Lemma") is what's missing and should be built new, not
  retrieved.

- Analogous past problems (cruxes): searched `combinatorics` /
  `games-and-strategy` and `extremal-principle` subtopics (205 cruxes).
  Best partial analogue: **aimo-0012** — "For a smallest-$k$/minimal-count
  answer, exhibit an extremal instance of equal values tuned so no two can
  share a part, forcing the matching lower bound" (all-equal-value tuning
  to hit a tight lower bound exactly) — the same flavor as the "all-equal
  elements are optimal for a sum-rank bound" mechanism suspected here, but
  it is a different problem shape (a covering/count problem, not a
  rank-alternating-sum bound) — a loose structural analogy only, not a
  transferable proof step. No crux found that directly handles
  "cardinality-capped minimization of an alternating/rank-sum given a
  magnitude cap" — this appears to be genuinely bespoke to this problem's
  own machinery; report this honestly to the outliner (no strong match).

- Prior progress: Sub-case (i) is certified closed (Round 17, reviewer-
  verified) for: all even $e\ge2$ (whole range), the width-1 window itself
  at every $e\ge1$, the vacuous $(k,e)=(1,1)$ case, and (per the certified
  Large-Sum/Half-Sum tools) odd $e\ge3$ unconditionally (cap-free) for
  every $k\ge1$. The **only** remaining gap is odd $e=1$, $k\ge2$, $a_1\in
  [2^{k-1}+1,2^k]$ (outside the window) — exactly the case this report
  targets.

- Dead ends (do not retry):
  - Round 16's one-step $q{=}0$ telescoping ($\mathrm{Odd}\to\mathrm{Odd}$)
    — false, corrected in Round 17 to the coupled Odd/Even two-term
    recursion. Do not resurrect the one-step form.
  - Using the cap-free Half-Sum Corollary alone at $a_1$ near $2^k$ for
    $e=1$ — confirmed here (see numeric findings) to be genuinely too weak:
    the bound $\mathrm{LB}_{\mathrm{odd}}$ itself dips below $T_{\mathrm
    {odd}}$ there, and an actual cap-free counterexample exists ($k{=}2$,
    $a_1{=}494/125$, $\mathrm{OddSum}=122753/16235\approx7.56<8$). Any
    approach that tries to rescue Claim B by re-tuning constants in the
    *same* cap-free Half-Sum-based bound will fail — a cap-free fix does
    not exist (the counterexample is real and unconditional).

- Small-case / intuition notes (all conjectural — exact-`Fraction`
  numeric search, not proof; own scripts, fresh this round):
  - **The cap-free counterexample is real** — re-verified independently:
    $a_1=494/125\in(2^{k-1},2^k]=(2,4]$ at $k=2$; $\mathrm{sum}(R)=506/125$
    required; the round-17 counterexample's $R$ has $|R|=4>m+1-1=3$
    (i.e. $|D|=5>m+1=4$), so it is excluded once $\mathrm{GT}(m)$'s own
    cardinality cap ($|D|\le m+1$, i.e. $|R|\le m=3$) is enforced.
  - **With the cap enforced ($|R|\le m$), extensive randomized
    exact-rational search (thousands of trials per point, own fresh
    script) found ZERO violations** of $\mathrm{OddSum}(D\cup\Gamma_{m-1})
    \ge2^m$ for $(k,e)=(1,1),(2,1),(3,1),(4,1)$, scanning $a_1$ densely
    across the *entire* claimed range $(2^{k-1},2^k]$, including right at
    the endpoint $a_1=2^k$ and at fine resolution approaching it from
    below ($a_1=3.99,3.999$-style points for $k=2$). This corroborates
    round 17's own $145{,}546$-trial finding at $(k,e)=(2,1)$ and extends
    it to $k=1,3,4$.
  - **At the literal endpoint $a_1=2^k$** (a single feasible construction:
    $R$ forced to be $n=2$ copies of $\mathrm{cap}=2^{k-1}$ when $S=2^k$
    exactly divides evenly, e.g. $k=1,2$; more generally the search's
    found minimum), the minimal $\mathrm{OddSum}$ found equals the target
    $2^m$ **exactly** (diff $=0$, no slack, no violation) for $k=1,2,3$ —
    conjecturally this is the *true* extremal point, i.e. the corrected
    inequality is tight with **equality attained exactly at $a_1=2^k$**,
    not merely approached.
  - **The margin shrinks monotonically to $0$ as $a_1\to2^k^-$** in every
    scan performed (e.g. $k{=}2$: diff shrinks from $+0.48$ at $a_1{=}3.05$
    down to $+0.006$ at $a_1{=}3.99$; $k{=}3$: from $+1.98$ at
    $a_1{=}4.05$ down to $+0.012$ at $a_1{=}7.99$), consistent with a
    single tight worst point at the closed endpoint rather than a
    violation region strictly inside $[2^{k-1}+1,2^k]$.
  - **The minimizing count found by the search consistently sits near the
    cap's own upper limit** ($n=m$ for $k=2,3$; $n=4<m=5$ for $k=4$'s
    coarser search — not confirmed exhaustive), consistent with the
    "forced-parity/near-tight-count" mechanism proposed in Opening 1 above:
    the cardinality cap keeps forcing a count that is *not* the
    Half-Sum-optimal even/near-equal split, producing exactly the
    positive slack observed.
  - **Conjecture to hand to the outliner**: the corrected, capped Claim B
    is TRUE as stated (no rescoping of the $a_1$-range needed) once proved
    via a genuinely cardinality-aware extremal lemma; the existing
    cap-free algebraic route (Half-Sum Corollary applied without using
    $|R|\le m$) is structurally incapable of proving it and should be
    replaced, not patched, in the next build.
