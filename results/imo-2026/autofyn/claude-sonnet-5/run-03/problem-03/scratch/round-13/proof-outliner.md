# Round 13 outline — IMO-2026-03

Plateau check (this round's math-explorer-plateau-check.md) confirms the two
remaining top-level gaps — GT($m$) at general $m$ (gap (a) of the shared
Branch-I.A window, owned by `self-similar-induction-on-n`) and the
$\Sigma$-shape Existence-Theorem gap (owned by `global-lp-vertex-
sufficiency`) — are **not** the same obstruction (different index, different
geometry, no literal reduction either direction) and no fresh top-level
framing is warranted. **No new approach opened this round.** All four live
approaches revised in place; the two deprioritized-but-not-dead ones
(`lp-duality-split-polytope`, `greedy-reduction-geometric`) get brief
pointers; `universal-halving-adversary`, `dyadic-potential-invariant`,
`layer-cake-parity-reframing` stay untouched (no genuine new lead surfaced
for them this round); `structured-randomization-upper-bound` stays RETHINK/
dead, not reopened.

---

## 1. `self-similar-induction-on-n` (revise — primary target)

**Status:** partial (Elo 1492.06, last_outcome partial/CHANGES REQUESTED,
round 12).

**Round 12 recap.** GT($m$) — the General Theorem, $|D|\le m+1$,
$\max(D)\le2^m$, $\mathrm{sum}(D)<3\cdot2^{m-1}$ ⟹
$\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge\min(\mathrm{sum}(D),2^m)$ — is proved
in full for $m=0,1,2,3$ via a two-level case split ($p:=\#\{a_i>2^{m-1}\}$,
then within $p=0$, $r:=\#\{a_i>2^{m-2}\}$), closing gap (a) of the shared
Branch-I.A window at $\ell=1,2,3,4$ (level $\ell$ is $m=\ell-1$). This
round's explorer (`math-explorer-general-l.md`) pins down *exactly* why the
$m\le3$ mechanism does not extend by literal repetition: the "$r=0$
residual" (all-tiny, still $m+1$ pieces) is infeasible for $m\le3$ but
provably **feasible from $m=4$ on** (Feasibility Lemma, exact threshold),
and the depth needed to reach a vacuous base case at the bottom of the
dyadic ladder grows like $\lceil\log_2(m+1)\rceil$ — an unbounded (though
explicit and slow-growing) recursion, not a fixed 2-level case split. The
explorer's numerics (§3) additionally show the true extremal $D$ at every
tested $m$ (up to $m=6$, reliably) is **tied-pair-shaped** (Theorem-W
witness family), not many-tiny-pieces-shaped — i.e. the case-split's
difficulty is a proof-method artifact, not evidence the bound is actually
hard to reach at the $r=0$ boundary.

**Round 13 target: close GT($m$) for all $m\ge0$ by ONE of Routes A–D
below, in priority order.** Whichever closes first ends this gap
(equivalently the corollary — Branch-I.A window gap (a) at *every* $\ell$,
not just $\ell\le4$) in full generality.

### Route B (primary — exchange-smoothing pin to Theorem-W shape)

Formalize the exchange move suggested by the explorer (§4 Route B, §7
step 1): let $D^*$ minimize
$f(D):=\mathrm{OddSum}(D\cup\Gamma_{m-1})-\min(\mathrm{sum}(D),2^m)$ subject
to $|D|\le m+1$, $\max(D)\le2^m$, fixed $\mathrm{sum}(D)<3\cdot2^{m-1}$
(want $f(D)\ge0$ always). Show: if two coordinates of $D^*$ are both
"generic" (strictly interior — not $0$, not the cap $2^m$, not exactly
tied with a $\Gamma_{m-1}$-block value), a small paired exchange
$a_i\to a_i+t$, $a_j\to a_j-t$ is weakly non-increasing in $f$ for one sign
of $t$ — a standard rearrangement/majorization move (crux corpus
`aimo-0146`: exchange weight toward the higher-coefficient sorted position;
`aimo-0119`: minimality-based single-transfer non-improvement, simpler
first-pass template). This forces $D^*$'s coordinates to collapse onto
$\{0,\ \mathrm{cap},\ \text{tied with a}\ \Gamma\text{-value}\}$ — i.e. a
finite, $m$-independent parameter family (matching
`lemmas/theorem-w-window-endpoint-witness.md`'s witness shape
$\{2^{m}\}\cup(\Gamma_{m-2}\setminus\{1\})\cup\{r,r\}$-style tied pair).
GT($m$) then reduces to checking $f\ge0$ on that single low-parameter
family by direct algebra/induction on $m$ — no case-split depth issue at
all, because the family's parameter count doesn't grow with $m$.
**Gap to close:** (i) the exchange-move sign argument itself (must handle
$\mathrm{OddSum}$'s rank/parity dependence carefully — a coordinate swap can
change which rank is odd/even, unlike a smooth functional; this is the
crux of why the move needs to be proved from scratch, not assumed by
analogy to `aimo-0146`'s original problem), (ii) the boundary/degenerate
cases where $D^*$ has $<2$ generic coordinates to exchange, (iii) closing
the resulting finite family by direct computation, general $m$.
Before investing fully in the proof, re-run the explorer's hill-climb with
proper simulated annealing at $m=7,8,9,10$ (the $m\ge7$ numbers in this
round's report are flagged as possibly non-converged) to make sure the
target shape is right before proving it.

### Route C (secondary — check for a free ride from sibling LP-vertex machinery)

Per the explorer's §4 Route C / §7 step 3: scout (quick, before committing
full effort to Route B) whether `global-lp-vertex-sufficiency`'s or
`lp-duality-split-polytope`'s already-certified cell-wise-affine /
vertex-sufficiency reduction (their Affine-Rank Lemma +
Vertex-Attainment Lemma, `lemmas/affine-rank-and-vertex-attainment-middle-
regime.md`, or `lemmas/finite-cell-vertex-reduction-and-region-
classification.md`) applies directly to $\mathrm{OddSum}(D\cup\Gamma_{m-1})$
as a piecewise-linear objective over the $D$-polytope (fixed $k\le m+1$,
cap $2^m$, fixed sum) — since $\mathrm{OddSum}$ is affine in $D$ once the
sort order (cell) is fixed, this machinery may hand Route B's conclusion
(minimizer at a vertex = finite $m$-independent family) for free, without
re-deriving the exchange argument from scratch. If this pans out quickly,
prefer it (it reuses certified content); if not within a bounded scouting
effort, fall back to Route B's direct exchange-argument proof.

### Route A/D (fallback — direct closed-form induction on depth)

If B/C stall: prove a single uniform two-parameter statement
$\mathrm{GT}(m,j)$ — $|D|\le m+1$ (count cap *not* shrunk), $\max(D)\le
2^{m-j}$ (value cap shrunk by $j$ dyadic levels) ⟹ same conclusion — by
induction on $m+j$ (or on $j$ for fixed $m$), making the "extra piece-count
slack" from round 12's diagnosis the explicit inductive quantity instead of
rediscovering a fresh Feasibility Lemma by hand at every depth. The
peeling-identity chain (Global-max Peeling + Companion Peeling against
$2^{m-1},2^{m-2},\dots,2^{m-j}$) already generalizes mechanically per the
explorer's own R1/R2 computations; the remaining work is (a) writing that
generalization as one lemma indexed by $j$, and (b) closing the final
$j=\lceil\log_2(m+1)\rceil$ base case's algebra uniformly in $m$. Crux
`aimo-0084` (strengthen the target into a uniform peel-one-object-at-a-time
induction, expect a few $m$-independent boundary cases surviving by hand)
is the template. Crux `aimo-0156` (split into two self-similar smaller
copies + one connector, constant depth) is worth a quick look as an
alternative reformulation of the peeling recursion that might avoid the
$\log m$ depth issue altogether, but do not chase it if B/A/D above are
progressing — it would require re-deriving the peeling identities in a
genuinely different shape.

**Do not re-attempt:** literal hand-extension of the $m\le3$ two-level case
split to $m=4,5,6,\dots$ one at a time — round 12 tried this, the explorer
confirms it never terminates (depth grows like $\log_2 m$).

---

## 2. `global-lp-vertex-sufficiency` (revise — primary target)

**Status:** partial (Elo 1536.14, CHANGES REQUESTED, round 12).

**Round 12/13 recap.** Region-Boundary Monotonicity (fixed-vertex,
straight-line path monotonicity) is **refuted** (round 12, confirmed
genuine not noise). The weaker endpoint-inequality substitution — for every
interior $p$, *some* boundary point $q$ (region-geometry-chosen or
otherwise) with $V(p)\le V(q)$, $q$ ranging only over the already-closed
$Q_{\mathrm{region}}$ — remains logically sufficient (explorer confirms the
chain in §2: full path-monotonicity was always stronger than necessary).
This round's explorer tested two concrete **region-geometry-driven**
exchange mechanisms (gap-exchange à la `aimo-0287`, $p_1$-boundary move) at
$n=3,4$, including the maximally weak existential form (any of $n+1$
candidates). **All region-geometry-driven mechanisms fail**: the $p_1$-move
fails in every trial; even the weak existential form fails at 3/6 tested
interior points, with genuine (non-noise, $10^3$–$10^4\times$ noise floor)
excess up to $\approx0.017$. This rules out the whole *region-slack-based*
family of candidate mechanisms, not just round 12's single fixed vertex.

**Round 13 target: build $q$ from the optimal adversary response
$\sigma^*(p)$ itself, not from region geometry.** Per the explorer's §7
(the one mechanism not yet tried by any round): take $p^*$'s minimizing
cut-allocation/shape $\sigma^*$ (exactly known via the certified Global
Vertex Lemma, `lemmas/global-vertex-lemma-and-lipschitz-continuity.md`);
identify which of $\sigma^*$'s pinned-fragment tie/equality constraints is
**closest to breaking** as $p$ moves (an adversary-side tightest-slack, not
a region-side one); construct $q$ by pushing $p$ in the direction that
makes exactly that tie exact — a response-side exchange, structurally
analogous to `aimo-0287`'s adjacent-pair move but applied to $\sigma^*$'s
combinatorial structure rather than to $p$'s own coordinates. **Concrete
steps:**
1. Formalize "which tie is closest to breaking": at $p$, $\sigma^*(p)$
   satisfies a set of tie equalities (from the vertex characterization);
   define the slack of each as a signed distance to violation, and let $q$
   be the point where the smallest-slack tie is pushed to exactly $0$
   (i.e. exactly reached), holding other coordinates fixed via the same
   affine relation used in the Global Vertex Lemma.
2. Test numerically first (reuse this round's explorer's independent
   Python re-implementation, already validated against the file's own
   $e_0$ values) before writing any proof: does $V(p)\le V(q)$ hold at the
   same $n=3,4$ trial points (including the three points that broke every
   region-geometry mechanism this round)? If it also fails, this closes
   off exchange arguments as a class and the approach should pivot back to
   direct $\Sigma(n,k)$ classification (Sections 1–4.4, already fully
   closed for $Q_{\mathrm{region}}$) as the only remaining route — report
   that honestly rather than searching for a fourth exchange variant.
3. If it survives numerically, formalize the proof: show the response-side
   push is weakly non-decreasing for $V$ by an exchange/rearrangement
   argument on $\sigma^*$'s tie structure (not on $p$'s raw coordinates),
   and confirm $q$ always lands in $\overline{\partial B(n)}$ (the
   already-certified-closed part of the boundary) via the Boundary
   Continuity Theorem.

**Secondary/deprioritized (only if the above stalls):**
fragment-vs-fragment tying generalization of the Singleton-Interleaving
Lemma to chain-tie fragments across different split pieces — unchanged
soft-negative signal (clearing-$s$ grows with $n$), not attempted with a
real proof yet, lowest priority per both this round's and last round's
explorers.

---

## 3. `lp-duality-split-polytope` (brief revised target)

**Status:** partial (Elo 1607.45, CHANGES REQUESTED, round 12). No genuine
new lead surfaced for this approach specifically this round — its own
Perfect-Tie-Family Characterization (round 12) is complete for the
sub-family it covers, and the general fragment-vs-fragment question is now
explicitly deprioritized (see §2 above) pending the response-side exchange
route's outcome. **Round 13 target:** stand by; if `global-lp-vertex-
sufficiency`'s response-side exchange (§2) needs the exact vertex/tie
structure of $\sigma^*(p)$ formalized in LP-duality terms (this file's
native language — dual variables, split-polytope vertices), be ready to
contribute that machinery on request. No independent proof work assigned
this round; do not spend a build on searching further bounded construction
families at $e_0$ (two independent techniques, Mass-Constraint and
Perfect-Tie, already rule those out — explorer and round-12 outliner both
confirm this is exhausted).

---

## 4. `greedy-reduction-geometric` (brief revised target)

**Status:** partial (Elo 1633.48, CHANGES REQUESTED, round 12). This
approach's only open piece — gap (a) of the shared Branch-I.A window,
i.e. $\mathrm{OddSum}(D_0\cup\Gamma_{\ell-2})\ge2^{\ell-1}$ for every
admissible $D_0$ — is **exactly** GT($m$) at general $m$ (confirmed twice:
this file's own §16.6 "confirmed by two independent routes... the same
recursive-in-$\ell$ statement," and the plateau-check explorer's formal
restatement in a common language). **Round 13 target: no independent work
this round — this approach's gap closes automatically if/when
`self-similar-induction-on-n`'s Route B/C/A/D (§1 above) closes GT($m$) for
general $m$.** If a build slot is available and `self-similar-induction-
on-n` is still mid-attempt, this file's Elementwise Monotonicity Lemma
(§16.1, certified) may be directly reusable inside whichever route succeeds
(e.g. Route B's exchange argument, when peeling/comparing $D_0$'s elements
against $\Gamma$-block levels) — flagged as a possible cross-approach
lemma reuse, not a new independent target.

---

## 5. Untouched this round

`universal-halving-adversary`, `dyadic-potential-invariant`,
`layer-cake-parity-reframing` — no genuine new lead surfaced for any of
them in this round's three explorer reports; leave as-is, deprioritized.
`structured-randomization-upper-bound` — RETHINK/dead (Expectation
Obstruction Theorem, round 12), not reopened; plateau-check explorer's §2
independent-consideration of a lower-bound-direction probabilistic
argument found no promising new angle and explicitly recommends against
reopening.

---

## Build set

build set: self-similar-induction-on-n, global-lp-vertex-sufficiency
