# Outline review — round 30, imo-2026-03

Reviewed the 3 revised outlines in `/tmp/round-30/proof-outliner.md` against
`results/imo-2026-03/current.md` (round 29 state), the 3 live approach files,
the 3 round-30 explorer reports, and `knowledge_base.md`. All three are
`revise` on already-live, already-registered slugs — no new approach to
register this round.

## 1. rank-pigeonhole-budget — APPROVE

**Target:** close (star_3)=MinFloor(4)'s 6 residual shapes; this round attacks
$(2,0,0,1)$'s $f_1\ge4$ regime plus opens a route for the other 4.

- **Case splits exhaustive.** Step 2's split $f_1\ge5$ (trivial, half-bound
  lemma) vs $f_1\in(4,5)$ is exhaustive of the residual $f_1\ge4$ domain. The
  further $f_2>2$ vs $f_2\le2$ split inside that is likewise exhaustive
  (covers all of $(f_2,f_3,2,e,f)$'s possibilities once $f_1$ is peeled twice).
  No missing case.
- **Double-Pair Ordering Lemma — correctly flagged as an open gap, not
  smuggled in as proved.** The outline explicitly says "proved from scratch
  (not cited, since it does not exist yet)" and lists it under Open gaps. I
  independently re-verified the explorer's numeric claim that a clean 4-case
  piecewise-linear closed form governs $A(\{x_1,x_2,y_1,y_2\})$ for two
  independent conservation pairs (spot check, exact `Fraction`, matches the
  claimed structure: it's the same sort-order-trichotomy argument that already
  worked for the certified Pair-Insertion Ordering Lemma, just with the fixed
  reference removed). This is legitimate new-but-tractable content, not
  circular — the mechanism (finitely many sort orders, each giving a linear
  formula in the free coordinate) is the same proof *technique* already
  certified, applied to a structurally distinct object (no fixed reference
  point). Approve as a build target.
- **Forced-Dominance Fact.** Elementary and correct: splitting a positive
  quantity two ways always leaves a part $\ge$ half, and the ladder ratio
  $\pi_i=2\pi_{i+1}$ turns "$\ge\pi_i/2$" into "$\ge\pi_{i+1}$." No issue.
- **Reuse of vertex-minimum-theorem + odd-run-reduction-lemma for
  $(1,1,0,1),(1,1,1,0)$ (3-independent-pair shapes)** is not circular — these
  are both already-certified, fully general theorems (finite-vertex reduction
  + closed-form tie evaluation), being invoked on a genuinely reduced
  finite-parameter residual (3–4 free coordinates after the forced-dominance
  peel), not asked to prove anything new about themselves. This is a sound,
  legitimate shortcut (per the explorer's own honest note that it's likely
  cheaper than a bespoke 3-pair lemma) rather than hand-waving — it still
  requires the builder to actually enumerate and evaluate every tie-vertex of
  the residual, which is real work, just delegated to certified machinery
  instead of a fresh elementary lemma.
- **$(1,2,0,0)/(2,1,0,0)$'s extra "which free top dominates" branch** ($f_1$
  vs. free pair's top $a$) is a genuine new case split, correctly identified
  as not automatically resolved (neither $f_1\ge8/3$ nor $a\ge2$ forces
  dominance over the other) — the outline doesn't paper over this, it names
  it as an extra branch to add.

No fatal flaw found. Build.

## 2. greedy-halving-adversary — CHANGES REQUESTED (concrete bug found, fixable before/during build)

**Target:** close Vertex 5 of $h(m)$'s single-cut-on-$q_1$/tail-untouched
piece, $m\ge3$.

- **Step 1–3 (peel $q_1-x$, cite `single-insert-point-vertex-lemma`'s SLOPE
  fact on $g(x):=A(\{x\}\cup T)$, $T$ fixed) is legitimate and NOT the same
  false shortcut flagged in round 29.** The round-29 dead end was applying the
  lemma "one coordinate at a time" to a *mass-conserving pair* $\{x_1,x_2\}$
  with $x_1+x_2$ fixed (wrong slope, $\pm2$ not $\pm1$). Here $x$ is peeled
  apart from $q_1-x$ first (via `sharp-dominant-removal-identity`, turning the
  pair into $F(x)=(q_1-x)-g(x)$), and the lemma is then applied to $g(x)$ where
  $x$ really is the *single* free coordinate against a genuinely fixed rest
  $T$ — exactly the lemma's licensed hypothesis. I independently verified the
  resulting monotonicity claim numerically (exact `Fraction`, $m=6$, every
  $t\in$tail, dense grid on $x\in(0,q_1/2)$): $F(x)$ is non-increasing in every
  case, zero violations, matching the claimed $F'\in\{-2,0\}$ mechanism. This
  step is sound.
- **Step 4/5 contains a genuine numerical bug: the claimed equality
  "$t=q_2$ reduces exactly to $A(\mathrm{tail})=f(m)$" is FALSE for $m\ge4$
  and its generalized form in Step 5 ("the two-gap sum is minimized at
  $t=q_2$, giving $f(m)$... for every $t$, $t=q_2$ giving equality") is a
  false claim as stated for general $m$.** I computed the boundary value
  ($x\to q_1/2$, so $\{x,q_1-x\}\to\{q_2,q_2\}$) directly and exactly for
  $m=3,\dots,8$:
  - The correct reduction (via pair-cancellation) is
    $A(\{q_2,q_2\}\cup(\mathrm{tail}\setminus\{q_2\}))=A(\mathrm{tail}
    \setminus\{q_2\})$ — **not** $A(\mathrm{tail})$ as literally written (a
    labeling slip: "tail" in the outline's step 4 should read
    "$\mathrm{tail}\setminus\{t\}$," the object already named $T$ in step 1).
  - More importantly, this value equals $f(m)$ **only at $m=3$**
    ($1/15=f(3)$, exact match) — for every $m\ge4$ it is *strictly larger*
    than $f(m)$ (e.g. $m=4$: $3/31$ vs. $f(4)=1/31$; $m=5$: $5/63$ vs.
    $f(5)=1/63$; $m=6$: $11/127$ vs. $f(6)=1/127$ — growing slack, not
    shrinking to equality). $t=q_2$ **is** still numerically confirmed to be
    the worst (minimizing) choice of $t$ at the boundary for every $m$ tested
    — that part of the diagnosis is fine — but it does **not** attain
    equality with $f(m)$ except at the single base case $m=3$ (which matches
    Vertex 4's own already-established tightness pattern, "tight only in the
    limit $x\to q_1/2^-$ at $m=3$" — the outline conflated Vertex 4's known
    $m=3$ tight case with a claimed general-$m$ equality at Vertex 5).
  - **Consequence for the build:** Step 5 as literally written ("prove the
    two-gap sum is minimized... at $t=q_2$... equality" for every $m$) asks
    the builder to prove a **false** identity for $m\ge4$. The builder must
    instead prove the correct, weaker, still-sufficient statement: the
    boundary value is $\ge f(m)$ for every $t$ (strict for $m\ge4$, tight only
    at $m=3$), which is exactly what's actually needed to close Vertex 5 —
    no equality is required anywhere except the already-established $m=3$
    base case. This does not kill the approach (Opening 1's monotonicity
    argument is real and does all the necessary work of collapsing the
    continuum in $x$ to one boundary check), but the false equality claim
    must be corrected before the builder wastes effort chasing it.
- Step 6's "global min = $f(m)$ exactly" should likewise be softened to
  "global min $\ge f(m)$, with equality only at the already-known $m=3$ base
  case" — consistent with the whole induction only ever needing a lower bound,
  never a matching upper bound, at this step.

**Verdict: CHANGES REQUESTED.** Build with the correction: replace Step
4/5's false general equality claim with the correct inequality-only
statement (numerically confirmed by both the explorer and this review); the
monotonicity mechanism (Steps 1–3) is sound and should proceed as outlined.

## 3. lp-duality-certificate — APPROVE

**Target:** retract the refuted 60-chamber coverage claim; introduce and
scope the Triple-Pin Theorem.

- **Retraction is correct and mandatory-first, as written.** The round-30
  explorer's counterexample ($p=(11,7,6,3,2)/29$, all 60 chambers give
  $\Phi=15/29>a_4T=16/31$ by exactly $1/899$) is a genuine, exact,
  interior-of-$\mathcal R$ violation, independently reproduced by the
  explorer via two methods (closed-form chamber formulas and direct
  sort-and-alternating-sum). The outline's step 1 explicitly retracts the
  overclaim and forbids carrying it into `current.md` — correct discipline,
  matching this project's own repeated lesson (rounds 24–27) about not
  trusting "100% empirical coverage" from sampling within an untested-for-
  completeness family.
- **Triple-Pin Theorem is well-posed, not another premature "covers
  everything" claim.** Its formula
  $\Phi=(T+|p_m-p_a-p_b-p_c|)/2$ is the natural one-level-deeper
  generalization of the already-certified Bisect-Subset
  ($\Phi=(T+A(R))/2$) and Double-Bisect-Pin ($\Phi=(T+|p_k-p_l-p_r|)/2$)
  formulas, and the outline correctly scopes its proof mechanism as "3
  iterated applications of `pair-insensitivity-corollary`" — the same
  mechanism, one level deeper, not a new unproved primitive. Feasibility
  (cut budget) checks out: trisecting $p_m$ to match 3 targets costs 2 cuts,
  leaving 2 spare for $n=4$, matching the outline's own budget note. The
  outline does **not** claim this closes coverage of $\mathcal R$ — step 5
  explicitly requires a *fresh* outer-minimization re-measurement (not
  reusing the family's own restricted sampling) before any coverage claim is
  trusted, and step 6 explicitly defers the Farkas argument until genuine
  100% coverage is established, "not force a premature Farkas attempt on a
  family already known to be incomplete." This directly incorporates the
  explorer's own methodological warning (a family can only ever report on
  itself) and is exactly the right discipline given the second surviving
  counterexample (the still-uncharacterized 4th chamber type) that the
  explorer found even after adding Triple-Pin.
- Step 4's instruction to attempt (but not force) reverse-engineering the 4th
  chamber type, with an explicit "do NOT invent an unverified formula"
  guardrail, is appropriately scoped as best-effort, not a hard requirement.

No fatal flaw found. Build.

## Diversity note

All three approaches remain scoped sub-targets of the same overall lower-
/upper-bound program (not a shared-gap plateau — each is attacking a
different, disjoint residual: (star_3)'s 6 shapes, $h(m)$'s Vertex 5, and
$n=4$'s upper-bound chamber census). This is legitimate continued narrowing,
not a collapse to one framing; no diversification action needed this round.

## Ranking

Registered: none new (all three slugs already in the population).
`update_ranking` run comparing the round-30 build-set trio against each
other and against dormant siblings (`rank-tie-vertex-reduction`,
`smoothing-compactness-certificate`, `self-similar-potential-certificate`),
anchored on round-29's verified outcomes (all three advanced with real,
independently-reviewed progress and no overclaim; `rank-pigeonhole-budget`
and `lp-duality-certificate` rated marginally ahead of
`greedy-halving-adversary` this round given the bug found above). Updated
Elo: rank-pigeonhole-budget 1720.2 > lp-duality-certificate 1719.3 >
greedy-halving-adversary 1644.6 > rank-tie-vertex-reduction 1568.1 >
smoothing-compactness-certificate 1527.7 > self-similar-potential-certificate
1412.8 (others unaffected/dead-end, not touched this round).

build set: rank-pigeonhole-budget, greedy-halving-adversary, lp-duality-certificate
