## Status
partial

## Approaches tried
- **greedy-halving-adversary** (round 28): per the outline-reviewer's flagged
  false-transfer risk (Theorem 40/41's rank-split mechanism needs an anchor
  unconditionally dominating the tail it is peeled from, not automatic once
  $S$ is free to cut $h(m)$'s own top piece $q_1$), restricted this round's
  target to the $q_1$-untouched sub-case (option (A) of the dispatch) and
  proved it in full for every $m\ge1$ at once: new **Lemma A** (a literal,
  general abstraction of Theorem 40/41 to arbitrary anchor/tail pairs
  $(w,X,g)$) and new **Theorem 42** ($h(m)$'s $q_1$-untouched sub-case
  closes unconditionally, every $m\ge1$, no per-$m$ casework). The
  complementary "$q_1$-cut" sub-case is honestly left open for $m\ge3$ (no
  domination anchor found there; the natural candidate ratio degenerates
  in the limit, mirroring the file's own round-26 "$c_2$-anchor"
  diagnosis) — $h(m)$ for $m\ge3$, and hence the "$T'$-cuts-$p_4$" branch
  of Case (b)'s "$v\ge a$" target, remain open, though the open territory
  is now precisely delimited. See
  `approaches/greedy-halving-adversary.md`, new "Round 28" section, for
  the full proof; Status of that approach file remains `partial`.
- **greedy-halving-adversary** (round 1–2): built the shared claiming-subgame
  reduction, an integral/alternating-sum formula, a "leftover formula," and a
  proof Liu Bang must use all n points. Refuted the naive "bisect the global
  max, n times" Xiang-Yu strategy (genuine counterexample). Proved the lower
  bound c(n)≥2^n/(2^{n+1}-1) for the sub-case where Xiang Yu leaves the top
  ladder piece untouched (c=0). Round 2: generalized this into two new
  reviewer-verified general lemmas — dominant-element-removal identity and a
  general cross-term identity at any threshold — valid for every split of
  Xiang Yu's budget between the top piece and the tail. These sharpen (but do
  not close) the open gap: for c≥1 the argument now stalls on one precise,
  numerically-supported but unproved cross-term/anti-concentration
  inequality (Proposition 10's "Missing inequality"), rather than a vague
  "subset-sum/matching" claim. **Round 4:** fixed a real gap in Proposition
  10 itself (a promised case split, $f_1\le r$, was never written out — now
  filled in), and proved by strong induction (new lemmas
  `tail-self-similarity`, `symmetric-split-c1-lower-bound`) that if Xiang Yu
  spends his $c=1$ cut on $p_1$ *symmetrically*, Liu Bang still gets
  $\ge p_1$ against *any* tail refinement — unconditionally true for $n=3$
  (since $c(2)=4/7$'s lower bound is already fully certified), and a valid
  recursive reduction for general $n$. Asymmetric $c=1$ splits and general
  $c\ge2$ remain open; numerically confirmed (not proved) that symmetric
  splits dominate asymmetric ones. Recommends importing
  `rank-pigeonhole-budget`'s result if that sibling approach closes the
  residual gap via its discrete recast. **Round 4 verdict: CHANGES
  REQUESTED** — reviewer independently re-verified Lemmas 10-12 and
  Proposition 13 by hand and by exact-`Fraction` computation (200000-trial
  search confirms $\Phi\ge8/15$ exactly at $n=3$ for the symmetric-split
  family); all three new lemmas (`tail-self-similarity`,
  `symmetric-split-c1-lower-bound`, plus the already-certified
  `sharp-dominant-removal-identity` reused from the sibling) certified.
- **smoothing-compactness-certificate** (round 1–2): abandoned continuous
  smoothing in favor of 6 explicit "template" Xiang-Yu strategies + an
  LP-style contradiction argument, giving a complete, non-numeric proof of
  c(2)≤4/7 in round 1. **Round 2: closed the 3 remaining n=2 lower-bound
  cut-distribution cases (1,1,0), (1,0,1), (0,1,1) exactly and symbolically**
  — reviewer independently re-verified these against direct sort-and-sum
  computation over tens of thousands of random rational instances with zero
  mismatches. **c(2) = 4/7 is now a fully rigorous, complete, non-numeric
  result, both directions — a genuine, reviewer-certified milestone.**
  General n is not attempted beyond a sketch of what a template-family
  generalization would need (open). **Round 4:** proved a fully general,
  non-numeric **General-$n$ Cascade Achievability Theorem** — the two
  boundary "cascading-halving" responses ($k=n-1,n$) attain $\Phi=a_n$
  exactly for every $n$, via a direct rank-position count (no induction, no
  numerics) — reviewer independently re-verified for $n=1,\dots,8$, zero
  mismatches; certified as `general-n-cascade-achievability`. Also an
  **honest negative finding**: attempted to extend the $n=2$
  six-template+LP-contradiction mechanism to $n=3$'s upper bound and found
  (reviewer independently re-verified by exact `Fraction` computation) a
  concrete configuration $(3/8,1/4,1/4,1/8)$ where all six templates fail
  (give $\Phi>8/15$) and only an ad hoc seventh strategy (trisect the top
  piece) achieves the true minimum $1/2<8/15$ — showing the general upper
  bound is genuinely harder to close than the $n=2$ mechanism suggested.
  **Reviewer verdict: CHANGES REQUESTED.**
- **self-similar-potential-certificate** (round 1 outline; round 2 first
  build): fixed a broken self-similar recursion the outline had proposed,
  proving instead the correct scaling identity f(n) = r(n)·f(n-1) and a
  general "above-threshold contribution" formula that reproduces the c=0
  lower-bound case cleanly. For c≥1 it derives a genuine negative result: the
  natural mass-based interleaving bound is *provably insufficient*, so this
  approach converges onto the same core combinatorial obstruction
  (rank-sensitive interleaving of Xiang Yu's top-piece fragments with his
  tail refinement) already identified by `greedy-halving-adversary`.
- **self-similar-bracketing** (round 3, new slug, built on the round-2
  self-similar work but reframed as bracketing the cut-budget split $c$
  between $c=0$ and $c=n$): gave a full, gap-free proof (Lemma B1) that the
  specific rescaled-ladder Xiang-Yu strategy at $c=n$ achieves $\Phi=p_1$
  *exactly*. **Then found and rigorously demonstrated (Proposition B2) that
  the outline's premise was wrong**: achieving $\Phi=p_1$ with one strategy
  at $c=n$ is not the same as $p_1$ being the *minimum* Xiang Yu can force
  there — that minimality direction embeds the identical unproved cross-term
  obstruction as the general problem (roles of $F,G$ swapped), so the "$c=n$
  endpoint" is not actually a free/easy endpoint as the round-3 outline
  assumed. Minimality at $c=n$ is nonetheless independently confirmed
  (reused, not re-derived) for $n=1,2$ via other certified work, and by
  numerics only for $n=3,4$. Zero progress on the interior $1\le c\le n-1$
  (the approach's actual target): no invariant or exchange-monotonicity
  argument was found. **Reviewer verdict: CHANGES REQUESTED / re-plan** — the
  new Lemma B1 is correct and reusable (certified as
  `rescaled-ladder-c-equals-n-achievability`), but the bracketing *strategy*
  itself is now shown to rest on a false premise; the next round should
  either find a genuinely different route to the interior or abandon
  bracketing-by-endpoints for this approach.
- **rank-tie-vertex-reduction** (round 3, new slug): proved, fully and
  rigorously (no gap), the **Vertex-Minimum Theorem**: for any fixed Liu Bang
  configuration and any fixed cut-allocation composition, the minimum (and by
  symmetry the maximum) of $\Phi$ over Xiang Yu's continuum of legal
  responses is attained at a vertex of a polyhedral cell decomposition — a
  point pinned by finitely many independent "fragment = 0" or "fragment =
  fragment" tie constraints — via a standard convex-polytope/LP-vertex
  argument. Also proved the **Odd-Run Reduction Lemma**, a genuine strict
  generalization of the certified `leftover-formula` (handles *any* number of
  simultaneously odd-multiplicity values, not just one), needed because
  vertex configurations routinely force several values into odd multiplicity
  at once. Reproduced the round-3 explorer's $n=3$ numeric example as a clean
  four-line symbolic computation using both new lemmas (exact match).
  **Negative finding:** checked the outline's Step-4 conjectured "self-tie
  plus rescaled-tail sub-vertex" inductive recursion against this $n=3$
  example and found it **false as stated** — the actual minimizing vertex
  ties $p_1$'s fragment directly to the tail piece $p_2$ (a cross-tie, not a
  clean top/tail split), so this exact inductive scheme should not be
  re-attempted verbatim. The actual enumeration of feasible tie-vertices for
  the ladder's specific values, for general $n$, remains open. **Reviewer
  verdict: CHANGES REQUESTED** — both new lemmas certified
  (`vertex-minimum-theorem`, `odd-run-reduction-lemma`); approach stays live,
  targeting the enumeration next. **Round 4:** the round-4 outline's "every
  prefix length $k$" cascading-halving conjecture was refuted by exact
  computation before build (correctly reported, not forced); replaced with
  a fully proved, closed-form **Cascading-Halving-Family Theorem**
  ($D\cdot A(S_k)=T(L)=(2^{L+1}+(-1)^L)/3$, $L=n-k$, exactly $L\in\{0,1\}$
  i.e. $k\in\{n-1,n\}$ hit the target, every $L\ge2$ strictly exceeds it) —
  reviewer independently re-derived and re-verified the closed form for
  $L=0,\dots,11$, zero mismatches. Genuine new general-$n$, non-numeric
  progress. **Reviewer verdict: CHANGES REQUESTED**; new lemma certified
  (`cascading-halving-family-characterization`). General enumeration
  (cross-ties, non-prefix subsets) and the upper bound remain open.
- **exchange-argument-extremal-response** (round 3, new slug, deliberately
  far from the measure-theoretic field per the shared-gap-plateau rule):
  proved, independently and via a genuinely different technique (fix a
  minimizer, derive local swap/exchange conditions from LP-vertex geometry,
  rather than writing a global integral formula first), the same
  vertex-reduction fact (**Lemma E1** existence of a minimizer,
  **Lemma E2** pair-cancellation identity, **Theorem E3** vertex reduction),
  plus a **Corollary E4** reducing the minimum to tie-cancellation for the
  "clean" (disjoint-pairing) vertex case. Independently re-derived, by hand
  and symbolically, the same $n=3$ tie example as `rank-tie-vertex-reduction`
  (exact match: $A=1/15=a_3$), a valuable cross-check between two
  independently-built approaches. **Honestly flagged its own gap**
  (Corollary E4 does not fully handle multi-way ties) — **this reviewer
  round found that gap is already closed by the sibling
  `odd-run-reduction-lemma`**, so the next builder on this slug can import
  that lemma directly instead of re-deriving multi-way-tie bookkeeping.
  General enumeration for arbitrary $n$ remains open, as does the general
  upper bound. **Reviewer verdict: CHANGES REQUESTED**; both new lemmas
  (`pair-cancellation-identity` certified as its own reusable fact,
  `vertex-minimum-theorem` merged with the sibling's version) certified.
- **rank-pigeonhole-budget** (round 4, new slug, discrete-counting toolbox
  per the shared-gap-plateau rule): proved a genuinely more general
  **sharp dominant-removal identity** ($A(\{f_1\}\cup T)=f_1-A(T)$ whenever
  $f_1>\max(T)$, strictly weaker than the certified
  `dominant-element-removal-identity`'s $f_1>\mathrm{Total}(T)$ hypothesis)
  and used it to collapse Proposition 10's Case A to a single clean
  inequality $(\star)$. **Honest negative finding:** the natural
  generic-multiset pigeonhole restatement of $(\star)$ (an `aimo-0718`-style
  "even-rank-sum dominates" claim) is **false** as a fact about arbitrary
  multisets — reviewer independently re-verified the counterexample
  ($F'=\{10\}$, $G'=\{1^{11}\}$: even-rank sum $=6<10=\mathrm{Total}(F')$).
  Case B ($f_1\le r$) is identified as the identical open $c=n$ minimality
  obstruction already on record from `self-similar-bracketing`, not a new
  gap. **Reviewer verdict: CHANGES REQUESTED**; new lemma certified
  (`sharp-dominant-removal-identity`).
- **claiming-order-invariant** (round 4, new slug, copied from
  `self-similar-potential-certificate` to try an `aimo-0117`-style "defer
  commitment" claiming-order invariant): found a **structural dead end**,
  rigorously argued, not just a failed guess — the marking stage is a
  one-shot Stackelberg game (no multi-round loop for such an invariant to
  maintain), and the claiming stage is already a fully-determined mechanical
  sort (`claiming-subgame-reduction`), so there is no remaining strategic
  freedom for a claiming-order invariant to exploit. Confirmed by a numeric
  check that the outline's candidate invariant fails at its very first step
  against the on-file $n=3$ example. No repair proposed, correctly — the
  reviewer confirms the diagnosis rules out any invariant of this shape, not
  just this particular guess. **Reviewer verdict: RETHINK** — do not
  re-attempt a claiming-order/defer-commitment framing for this problem;
  the recommended next target (per the approach's own write-up) is a
  pigeonhole/budget invariant over the one-shot *marking* stage instead.
- All approaches converge on the same underlying combinatorial obstruction —
  characterizing which finite tie-vertex/cut-distribution configurations are
  feasible and confirming $\Phi\ge p_1(n)$ (equivalently $A\ge f(n)$) at every
  one of them, for general $n$ — now reached independently from three
  directions (measure-theoretic cross-term bound, LP-vertex/tie enumeration
  from two different framings) with no approach yet closing it. This
  triangulation across genuinely different techniques (not just different
  lenses) is itself informative: it suggests the remaining difficulty is a
  real combinatorial fact about superincreasing sequences, not an artifact of
  any one approach's formalism.

- **Round 5 (all 4 built slugs, CHANGES REQUESTED, none RETHINK/APPROVE).**
  This round's assignment was to close inequality (*) via a two-claim
  decomposition — (A) fixed-tail single-multiset optimum, (B)
  tail-refinement-never-helps monotonicity. Result: **claim (B) as literally
  posed is FALSE** — `greedy-halving-adversary` found and rigorously
  verified (exact fractions, reviewer-reconfirmed) a genuine counterexample
  (n=2, $F=\{p_1\}$, splitting the tail's last piece $p_3$: $A$ strictly
  *decreases* from $3/7$ to $12/35$), refuting "refining the tail can only
  weakly increase $A$" for arbitrary $F$; the correct target is the weaker
  "refining the tail can never push $A$ below claim (A)'s value $a_n$,"
  itself unproved. New general **single-cut-perturbation identity**
  (Lemma 14) proved and certified, powering both this refutation and a
  strengthening of `symmetric-split-c1-lower-bound` (the $p_2$-split
  cross-term cancellation now holds for *every* split point, not only the
  symmetric one). `rank-tie-vertex-reduction` reduced its assigned
  domination sub-claim (asymmetric single cut on $p_1$) to a new residual
  inequality $(\star\star)$ via a certified **Cross-Term Reduction
  Theorem**, and *explicitly verified* $(\star\star)$ is the same
  obstruction every sibling approach has independently reached — a genuine
  convergence finding, not an escape route — while also fully closing a
  second infinite tie-vertex family (interior cross-ties against an
  untouched tail) in closed form (certified as an identity; the final
  "$\ge a_n$" corollary is checked only for $n\le7$, not proved for general
  $n$). `rank-pigeonhole-budget` **fully and unconditionally proved claim
  (A)'s achievability half** for every $n$ (explicit construction $F^*$,
  certified) and reduced its lower-bound half (Case II) via a genuine
  algebraic chain to a strictly smaller self-similar instance, unconditionally
  closing one entire sub-range; the remaining sub-range plus all of Case I
  stay open. **New slug `dyadic-band-occupancy`** (discrete/step-function
  toolbox) proved two fully general, certified reusable facts (a
  band-decomposition identity; a proof that the finite cut-budget is
  load-bearing — the cardinality-unbounded relaxation of claim (A) has
  minimum exactly $0$, not $a_n$) and rigorously **refuted its own assigned
  coarse "band-invariance" conjecture** via an exact counterexample,
  correctly diagnosing that its coarse per-band count/mass invariant cannot
  determine $A(F\cup T)$ (fine within-band position matters) — so this
  specific technique cannot close claim (A) without at least as much
  information as `rank-pigeonhole-budget`'s finer decomposition. All four
  independent framings this round (surrogate-undo/perturbation, cross-term
  window reduction, discrete case-split/self-similar reduction, and
  band-occupancy/integral-peeling) **landed on structurally the same wall**:
  an induction that needs an *upper* bound on $A$ of a reduced sub-instance,
  but only supplies a *lower* bound. This is now the fourth consecutive
  round (2, 3, 4, 5) in which independently-built approaches rediscover the
  same core obstruction under different names/framings — **this crosses the
  shared-gap-plateau threshold** (see Rules/Next below): round 6 should open
  at least one approach with a genuinely different framing (e.g. attacking
  the induction's *upper*-bound requirement directly, rather than another
  variant of "reduce to a smaller instance and hope for a lower bound").
  **8 new lemmas certified** (`single-cut-perturbation-identity`,
  `cross-term-reduction-theorem`, `interior-cross-tie-evaluation-formula`
  [closed form only, not its corollary], `claim-a-achievability-construction`,
  `even-rank-sum-phi-identity`, `band-decomposition-identity`,
  `claim-a-cardinality-is-essential`), plus 2 dead-end records
  (`refutation-of-tail-refinement-monotonicity`,
  `band-invariance-conjecture-refuted-dead-end`).

- **Round 6 (5 built slugs: 2 verified-milestone, 1 partial, 2 dead-end/RETHINK
  — the plateau is genuinely broken on one precisely-scoped sub-case).**
  This round opened two deliberately-distant new framings
  (`lp-duality-certificate`, `integer-lattice-reduction`,
  `bijective-mersenne-pairing`) per the shared-gap-plateau rule, alongside
  continued work on `rank-tie-vertex-reduction` and `rank-pigeonhole-budget`.
  **Headline result: `rank-tie-vertex-reduction` fully closes $(\star\star)$**
  — the window-integral inequality every plateaued approach had independently
  converged on for 4+ rounds — via a new **Half-Window Vanishing Lemma**: the
  ladder identity $p_1=2p_2$ places $p_2$ (the tail's own largest possible
  fragment value) exactly at the midpoint of the window $W$, so the window's
  right half provably carries zero odd-parity mass (no legal tail fragment
  can ever exceed $p_2$), while the left half is bounded trivially by its own
  length. **This reviewer independently re-derived the proof line by line
  and re-verified it by a fresh 2000-trial exact-`Fraction` simulation
  (built independently of the approach's own script) across $n=2,\dots,6$:
  zero violations.** The result is honestly and precisely scoped: it closes
  $(\star\star)$ only for the case Xiang Yu spends exactly **one** cut on
  $p_1$ ($c_1=1$, producing two fragments), against an **arbitrary** legal
  tail refinement — the general $c_1\ge2$ case (more than one cut on $p_1$
  itself) and the full tie-vertex enumeration beyond single-cut-on-$p_1$
  configurations remain explicitly open (§5.4 of the approach file), so this
  is real, verified, plateau-breaking progress on a precisely delimited
  sub-case, **not** a closure of the general lower bound. Separately,
  `rank-pigeonhole-budget` generalized its round-5 one-step reduction into a
  clean strong induction (**Theorem GC($m$)**) that **fully closes Case II
  of Claim (A) for every $n$, unconditionally** (no numerics needed); this
  reviewer independently re-verified it with a fresh 20000-trial exact-
  `Fraction` simulation of the theorem statement (built independently of the
  approach's own script), zero violations. Case II's counterpart, Case I,
  is precisely diagnosed as requiring an *upper* bound on $A$ of a smaller
  self-similar instance — shown to be equivalent in kind to the project's
  central obstruction, not a simpler residual — and remains open.
  `lp-duality-certificate` produced a complete, verified LP-dual certificate
  for all $17$ leaf cells of the fully-closed $n=2$ case, plus one consistency
  check one level into $n=3$; no general-$n$ certificate yet, and it is not
  yet known whether this framing structurally evades $(\star\star)$'s
  content or will simply re-encounter it in new notation. Two new framings
  are confirmed dead ends, both with fully verified (not merely asserted)
  falsifying computations: `integer-lattice-reduction`'s digit/carry
  transplant fails at two separate points (fragment denominators need not
  divide $D=2^{n+1}-1$ — explicit $4/21$ counterexample at $n=2$ — and exact
  bisection of a tail piece is not parity-invariant for the window integral —
  explicit $n=4$ example moving the integral from $5/31$ to $7/31$, the wrong
  direction); `bijective-mersenne-pairing`'s $2{:}1$ length-ratio pairing
  mechanism fails its own required generic (non-cascading) test case at
  $n=2$. Both leave reusable negative results (documented so no future round
  re-attempts these exact mechanisms) but no reusable positive lemmas beyond
  `integer-lattice-reduction`'s two rationality facts. **Net effect on the
  shared plateau:** the precise obstruction that had stalled 4+ rounds,
  $(\star\star)$, is no longer open **for the $c_1=1$ sub-case** — this is
  the first round since the plateau was declared that any approach has fully
  closed (rather than further reduced or reformulated) a piece of it. The
  general lower bound (all $c_1$, all tail refinements, all Liu Bang
  configurations) and the general upper bound remain open. **2 new lemmas
  recommended for certification/promotion** (`half-window-vanishing-lemma`,
  `case-ii-closure-theorem`), verified above; `cross-term-reduction-theorem`
  (already certified round 5) is the vehicle that makes the Half-Window
  result apply to the full domination claim.

## Current best

The game is rigorously reduced (via the claiming-subgame lemma) to a purely
combinatorial extremal problem on multisets:
$$c(n) = \max_{\text{Liu Bang's} \le n \text{ points}}\ \min_{\text{Xiang Yu's} \le n \text{ points}} \Phi(\text{final multiset}),\qquad \Phi(S)=\sum_{i\text{ odd rank}}L_i.$$
The conjectured answer $c(n) = 2^n/(2^{n+1}-1)$ (ladder construction
$p_i = 2^{n+1-i}/(2^{n+1}-1)$) is:
- **fully proved for $n=1$** ($c(1)=2/3$, both directions),
- **fully proved for $n=2$, both directions, zero numerics** (upper bound:
  round 1 six-template LP-contradiction argument; lower bound: all 10
  Xiang-Yu cut-distribution compositions against the ladder closed exactly)
  — this remains the strongest fully-closed base case,
- **proved for general $n$ only in the special lower-bound sub-case $c=0$**
  (Xiang Yu leaves the top ladder piece untouched), via two general, reusable
  identities (dominant-element-removal, cross-term-at-a-threshold),
- **round 3 adds two independent, fully rigorous general-purpose structural
  results** applicable to every composition and every $n$: the
  **Vertex-Minimum Theorem** (the continuum optimization over Xiang Yu's
  responses, for any fixed composition, is always attained at an exact-tie
  or degenerate-cut vertex — proved independently by two round-3 approaches
  via standard convex-polytope/LP-vertex theory) and the **Odd-Run Reduction
  Lemma** (evaluates $A$ at any such vertex in closed form, even when several
  values are simultaneously tied). Together these convert the "min over a
  continuum" difficulty into a "finite but not yet characterized/bounded
  enumeration" difficulty — a genuine reduction in kind, not just in
  language, cross-verified on a concrete $n=3$ instance by two independently
  built approaches with an exact match.
- **round 3 also closes (Lemma B1 / `rescaled-ladder-c-equals-n-
  achievability`) the exact achievability half of the "$c=n$" endpoint** (one
  specific Xiang-Yu strategy at $c=n$ attains $\Phi=p_1$ exactly, for every
  $n$) — **but also rigorously shows (Proposition B2) that the matching
  minimality half is not a free corollary**: it embeds the same open
  cross-term obstruction as the general problem. This corrects an
  over-optimistic premise in the round-3 outline and should prevent a future
  round from re-assuming "both endpoints are easy."
- **round 4 adds a fully proved, general-$n$, non-numeric closed-form
  characterization of the "cascading-halving" tie-vertex family**
  (`cascading-halving-family-characterization`): exactly the two deepest
  members ($k=n-1,n$) attain the target exactly (proved via
  `general-n-cascade-achievability`'s direct rank-count on the
  achievability side, and independently via the Odd-Run Reduction Lemma plus
  a geometric-series closed form $T(L)=(2^{L+1}+(-1)^L)/3$ on the
  lower-bound/vertex side); every shallower member strictly exceeds the
  target. This narrows, but does not close, the general tie-vertex
  enumeration.
- **round 4 also proves a genuinely new, general-$n$-conditional
  (unconditional at $n=3$) closed sub-case of the lower bound beyond $c=0$**:
  if Xiang Yu's one $c=1$ cut on $p_1$ is symmetric, Liu Bang still gets
  $\ge p_1$ against *every* legal tail refinement (`tail-self-similarity`,
  `symmetric-split-c1-lower-bound`) — reducing this sub-case to the identical
  lower-bound statement one level down via a clean self-similarity/rescaling
  argument. Since $c(2)=4/7$ is already fully closed, this makes $n=3$'s
  symmetric-$c=1$ case unconditionally proved; asymmetric splits and $c\ge2$
  remain open, with a concrete localized witness (an exact trade-off between
  the cross-term and the tail's own sub-optimality) showing why the natural
  monotonicity argument is not straightforwardly sign-definite.
- **round 4's discrete-counting attempt (`rank-pigeonhole-budget`)**
  collapses Proposition 10's Case A to a single clean inequality via a
  sharper, more general dominant-removal identity
  (`sharp-dominant-removal-identity`), and **honestly rules out** the most
  natural generic-multiset pigeonhole restatement of that inequality via an
  explicit counterexample — genuine progress in narrowing *how* any future
  proof of $(\star)$ must work (it must use the tail's specific
  superincreasing structure, not just totals), even though $(\star)$ itself
  remains open.
- **round 4's `claiming-order-invariant` attempt is a documented dead
  end**: a rigorous structural argument (not a vague hunch) rules out
  transplanting `aimo-0117`'s sequential "defer commitment" mechanism to
  this problem's one-shot Stackelberg marking stage and its already-fully-
  determined claiming-stage sort. This should prevent future rounds from
  re-attempting the same framing.
- the fully general upper bound (arbitrary $n$, arbitrary Liu Bang marking)
  and the fully general lower bound for $c\ge1$ (equivalently, characterizing
  and evaluating the feasible tie-vertices for general $n$) remain open. Four
  independent framings (mass/cross-term bound, self-similar
  bracketing, LP-vertex enumeration via rank-tracking, LP-vertex/exchange via
  minimizer-fixing) have now reached — from genuinely different starting
  points — either the same precise cross-term inequality or the same
  finite-but-uncharacterized vertex enumeration, which is strong evidence the
  remaining difficulty is a genuine, non-trivial combinatorial fact (in the
  flavor of "superincreasing sequences are optimal"), not an artifact of any
  one approach's machinery.

- **Round 6 fully closes the shared four-round plateau inequality
  $(\star\star)$ for the $c_1=1$ sub-case**: whenever Xiang Yu spends
  exactly one cut on $p_1$ (any asymmetry), the domination bound
  $A(F\cup G')\ge f(n)$ holds against *every* legal tail refinement $G'$,
  unconditionally, for every $n\ge2$ — reviewer-reverified by independent
  hand derivation and a fresh 2000-trial exact-`Fraction` simulation. This
  is a genuine, verified closure of a real sub-case of the general lower
  bound, not merely a further reduction — but it is explicitly scoped to
  $c_1=1$; the general $c_1\ge2$ case and the full tie-vertex enumeration
  (configurations not arising from a single cut on $p_1$) remain open. **This
  is the first round since the plateau was declared (rounds 2–5) that any
  approach has fully closed, rather than reformulated, a piece of the shared
  obstruction.**
- **Round 6 also fully closes Case II of Claim (A)** (`rank-pigeonhole-
  budget`'s discrete decomposition) for every $n$, unconditionally, via a
  clean strong induction (Theorem GC($m$)) — reviewer-reverified by an
  independent 20000-trial exact-`Fraction` simulation. Case II's counterpart,
  Case I, is now precisely diagnosed (not just left as a numeric gap) as
  requiring an *upper* bound on $A$ of a smaller self-similar instance —
  shown to be equivalent in kind to the general lower bound's central
  obstruction, so it is not a simpler residual of Claim (A).
- Two new round-6 framings (`integer-lattice-reduction`'s digit/carry
  transplant, `bijective-mersenne-pairing`'s $2{:}1$ length-ratio pairing)
  are confirmed dead ends with fully verified falsifying computations,
  correctly abandoned rather than iterated on further.

The fully general upper bound, the general $c_1\ge2$ lower-bound case, and
the full tie-vertex enumeration for arbitrary $n$ remain open.

- **Round 7 (all 3 built slugs, CHANGES REQUESTED, none RETHINK/APPROVE;
  this reviewer independently re-verified every new numeric/algebraic claim
  below by hand and by freshly-written exact-`Fraction` scripts, not the
  builders' own).** This round attacked the general $c_1\ge2$ case (the
  layer immediately past round 6's closed $c_1\le1$ result) from three
  angles at once. `rank-tie-vertex-reduction` proved two new exact
  identities — **Peel Decomposition Identity** (general, any multiset;
  trivial corollary of `cross-term-identity-threshold`) and
  **Case-II Exact Peel Identity** ($A(S)=z-A(G')$ exactly, whenever the
  largest fragment $z$ of $p_1$'s splitting is $\ge p_2$; re-verified
  10,138 independent random trials, zero mismatches) — but honestly
  diagnosed that, because the identity is *exact*, it converts
  "$A(S)\ge f(n)$" into the logically equivalent "$A(G')\le z-f(n)$," not
  a genuine reduction; the complementary no-dominant-fragment case
  ($z<p_2$) is confirmed outside this identity's reach entirely.
  `lp-duality-certificate` converted the certified Half-Window Vanishing
  Lemma into its own bounded-term certificate vocabulary for $c_1=1$ (a
  correct but essentially trivial repackaging), then pushed to $c_1=2$ and
  found (re-verified exactly: $n=3$, $F=\{4,2,2\}/15$, tail untouched)
  that the natural mechanical extension's sufficient condition
  $\int uv\le A(F)/2=2/15$ genuinely fails (actual value $3/15$) — while
  the true target $A(S)\ge f(3)$ still holds, with equality, because the
  tail's *exact* value ($3/15$) exceeds its inductive *floor* ($1/15$),
  slack this vocabulary's atoms cannot express. `rank-pigeonhole-budget`
  reformulated Case I as the self-contained one-level statement
  $E(F\cup\tau)\le R(\tau)$ and introduced a genuinely new **peel-the-
  global-minimum** mechanism (distinct from every prior peel-the-maximum
  argument in the population), rigorously closing two of three exhaustive
  branches for every $m$ (Branch A entirely, including a $k=m+1$ boundary
  argument via the new Half-Bound Lemma; Branch B when the total count
  $N=m+k$ is odd) and precisely isolating the sole remaining sub-case
  $(\dagger)$ (Branch B, $N$ even) — re-verified by an independent
  113,000-trial search, zero violations, with $(\dagger)$ itself
  genuinely exercised ($\approx26\%$ of legal trials). **Net effect:**
  three independent routes into the $c_1\ge2$/Case-I layer all converged,
  by three different mechanisms, on the same underlying fact — an
  *exact-value* (not floor) handle on a reduced tail/foreign-mass instance
  is what's missing — with `rank-pigeonhole-budget` producing the
  sharpest, most surgically narrowed open item to date ($(\dagger)$ alone,
  not an open-ended upper-bound requirement). No approach overclaimed;
  every honest gap was independently confirmed to be a real gap, not a
  reporting lapse. **7 new lemmas certified this round**
  (`peel-decomposition-identity`, `case-ii-exact-peel-identity`,
  `bounded-certificate-for-half-window-vanishing`, `half-bound-lemma`,
  `peel-minimum-branch-closure` [partial: Branch A + Branch B-odd only],
  plus 1 dead-end record `splitting-monotonicity-refuted-dead-end`), and
  **2 round-6 "recommended for certification" lemmas that had never
  actually been written to `lemmas/` were backfilled and certified this
  round** (`half-window-vanishing-lemma`, `case-ii-closure-theorem`) since
  round-7 work directly cited them as already certified.

- **Round 8 (4 built slugs: 1 APPROVE-at-own-scope [Claim (A) in full],
  3 CHANGES REQUESTED, none RETHINK).** This is the round's headline event:
  `rank-pigeonhole-budget` **closes Claim (A) completely, for every $n$,
  both directions, with zero remaining gaps** — the achievability half
  (§2, unconditional for every $n\ge1$) plus the full lower bound, Case II
  (already closed round 6, `case-ii-closure-theorem`) **and now Case I**
  (§5, this round's new **Case I Closure Theorem**), via a genuinely
  different mechanism than every peel-induction attempt on file: an
  **exchange-smoothing vertex-maximization** argument (dualizing the
  already-certified `vertex-minimum-theorem`'s exchange mechanism to a
  maximum) that reduces the continuum of legal $F$ to a small "pinned +
  one tied group" family, evaluated in closed form via `odd-run-reduction-
  lemma`, closed by two new elementary facts (a **Ratio-2 Spacing Lemma**,
  a **Last-Element Bound**) plus the already-certified `half-bound-lemma`.
  **This reviewer independently and adversarially re-verified every
  load-bearing piece from scratch, not just re-read the builder's own
  numerics:** (i) a fresh continuum optimization search (coordinate-ascent
  from many random starts, not vertex-restricted) confirms $\max_F
  E(F\cup\tau)$ never exceeds $R(\tau)$, margin $\to0$ (tight, matching the
  proof's claimed equality cases) — `/tmp/round-8/optimize_search.py`;
  (ii) exhaustive exact-`Fraction` re-derivation of all three branches
  (q-even, q-odd sub-case (a)/(b)) for $m=1,\dots,10$: zero violations
  across 9202 independently-enumerated configurations (matching the
  builder's own reported 6655-configuration check) —
  `/tmp/round-8/verify_57.py`; (iii) the Ratio-2 Spacing Lemma and
  Last-Element Bound re-derived exhaustively for $m\le10$ —
  `/tmp/round-8/verify_lemmas.py`; (iv) the identity $R(\tau)+\tau_m=2\tau_1$
  re-checked for $m=1,\dots,8$; (v) the achievability construction $F^\ast$
  re-verified exactly for $n=1,\dots,9$ — `/tmp/round-8/verify_achievability.py`,
  which also **independently confirmed a genuine correction**: $F^\ast$
  uses exactly $n$ cuts (Xiang Yu's *entire* budget), not $n-1$ as an
  earlier round's lemma-file prose stated (the identity itself was never
  wrong). No gap was found in §5's argument; **Claim (A) is certified as
  fully, rigorously closed for every $n\ge1$.** 5 new lemmas certified
  (`exchange-smoothing-vertex-maximization`, `ratio-2-spacing-lemma`,
  `last-element-bound`, `case-i-closure-theorem`, `claim-a-full-closure`).
  **Scoping — do not overclaim:** Claim (A) is only the sub-case where
  Xiang Yu spends his *entire* budget fragmenting $p_1$ and leaves the rest
  of the tail completely untouched. It is **not** the general lower bound
  and does **not** by itself solve `imo-2026-03`. The rank-pigeonhole-budget
  approach file's own header text ("Claim (B)... are proved by sibling
  approaches") is an **overclaim** the reviewer corrects here: Claim (B)
  (arbitrary tail refinement combined with any split of $p_1$) is **not**
  proved in general — see next paragraph — and the general upper bound is
  also not proved. The approach file's own "Open gaps" section, by
  contrast, states this accurately.
  - `greedy-halving-adversary` (Claim (B)'s owner) made real, verified
    progress but Claim (B) remains genuinely open where it matters most.
    New **Safe-Window Lemma** (every legal tail refinement stays $\le p_2$;
    reviewer-reverified, a clean induction) and new **Cross-Term Vanishing
    Lemma** (if Xiang Yu's split $F$ of $p_1$ is *fully paired*, $A(F)=0$
    and $A(F\cup G')=A(G')$ exactly for *every* legal tail refinement $G'$
    — reviewer independently re-verified with a fresh 3000-trial exact-
    `Fraction` script, zero mismatches) extend round 4's symmetric-only
    result to every fully-paired split, giving Proposition 16 (conditional,
    as Prop 13 was). **Crucially, and honestly reported:** the actual
    Claim-(A)-optimal witness $F^\ast$ is *not* fully-paired, and (per the
    reviewer-confirmed correction above) uses Xiang Yu's *entire* cut
    budget, so no tail-refinement budget is even available there — meaning
    restricted Claim (B) is vacuous exactly at Claim (A)'s tight optimum,
    but genuinely open for the general $F$ that mixes fewer cuts on $p_1$
    with tail refinement and has an unpaired residual (the case that
    matters for the full lower bound). 2 new lemmas certified
    (`safe-window-lemma`, `cross-term-vanishing-lemma`; Proposition 16
    itself not certified, since it is conditional).
  - `rank-tie-vertex-reduction` produced a rigorous, general **negative
    result** on the general $c_1\ge2$ case: a **Parity Coincidence Lemma**
    ($\ell(S)\equiv|S|\pmod2$ for every multiset, elementary, reviewer-
    reconfirmed) and a **Zero-Iff Lemma** ($\ell(S)=0\iff A(S)=0$, reviewer-
    reconfirmed) together *prove* — not just empirically suggest — that
    induction on $\ell(S)=|S'|$ (the odd-run-reduced size) cannot escape the
    exact same parity obstruction that has independently stalled
    peel-the-min (`rank-pigeonhole-budget`) and peel-the-max (this file's
    own round-7 attempt): the hard case is provably the same bit under any
    such induction variable, and the "free" base case $\ell=0$ is not
    actually free (equivalent to the still-open $A(S)\ne0$ fact). Confirmed
    concretely on the round-7 tight witness ($n=3$, $F=\{4,2,2\}/15$). This
    is a genuine, general, non-numeric dead-end proof — 1 new certified
    lemma file (`parity-coincidence-and-zero-iff-dead-end`) recording both
    facts and the diagnosis, so no future round re-attempts a peel-by-$\ell$
    variant.
  - `lp-duality-certificate` pivoted (as planned) to the general upper
    bound and produced **4 exact, unconditional closed-form identities**
    for arbitrary markings (Theorem A Full-Match, B One-Step-Peel, C
    Bisect-Top, D Bisect-Top-and-Bottom) — reviewer independently
    re-verified Theorems C and D's formulas against direct sort-and-sum
    computation, 2000 fresh random trials, zero mismatches
    (`/tmp/round-8/verify_lpdual.py`). Proved rigorous (non-numeric)
    sufficient conditions from each, combined by strong induction into a
    proven sub-domain $\mathcal D_m$ — honestly reported as covering only
    $\approx16$–$20\%$ of random configurations. The *combined* min-of-four
    strategy passes extensive numeric stress-testing (exhaustive $n=2$
    grid, $150{,}000+$ random/adversarial trials up to $n=6$, both known
    hard witnesses solved) but **no general-$n$ proof that the combination
    always suffices was completed** — correctly left open, not overclaimed.
    3 new lemmas certified in the approach file
    (`one-step-peel-identity`, `bisect-top-identity`,
    `bisect-top-bottom-identity` — not yet copied to `lemmas/` as
    standalone files by this reviewer since Theorem B's identity duplicates
    the already-certified peel/cross-term machinery in substance; Theorems
    C/D's exact formulas are new and reviewer-confirmed correct, recommend
    a future round backfill standalone lemma files for them if reused).
  **Net effect on the project:** Claim (A) — one of the two named pieces of
  the lower bound (per the round-5 explorer's decomposition) — is now a
  fully closed, non-numeric, reviewer-certified theorem for every $n$. The
  whole `imo-2026-03` problem is **not** solved: Claim (B) in general and
  the general upper bound both remain open, each with real (but partial)
  new progress this round. **Status remains `partial`.**

- **Round 9 (2 built slugs, both CHANGES REQUESTED, no RETHINK/APPROVE;
  reviewer independently re-verified every new identity/bound below with
  fresh exact-`Fraction` scripts, not the builders' own).**
  `greedy-halving-adversary` extended Claim (B) from the fully-paired family
  ($\ell(F)=0$) to the single-unpaired-residual family ($\ell(F)=1$): new
  **Lemma 19** (pointwise indicator $u_F\equiv\mathbb1[x<v]$ for
  $F=\{v\}\cup P$, $P$ exactly-paired — reviewer-reverified, 2000 trials,
  zero mismatches) and new **Proposition 20** (exact identity
  $A(F\cup G')=v-A(G')$ for $v\ge p_2$, no restriction on $G'$ — reviewer-
  reverified, 1200 trials across $n=2,\dots,5$, zero mismatches), which also
  **correctly refutes a flawed step in the round-9 outline** (a proposed
  "$\int_0^{p_2}v_{G'}\le p_2/2$" bound, independently confirmed false by
  the reviewer: at $n=3$ the untouched-tail value $1/5$ already exceeds
  $p_2/2=2/15$). New **Proposition 21** cleanly reduces the entire $v\ge p_2$
  sub-case to one inequality $(\dagger)$ via a cut-count argument. New
  **Proposition 22** closes $(\dagger)$ — and hence the whole $v\ge p_2$
  sub-case — conditionally (unconditional for $n\le4$, since it needs only
  the already-fully-closed lower bound at levels $0,1,2$) in the sub-case
  where the tail's own top piece $p_2$ is left uncut; reviewer independently
  re-verified the closed-form bound $\max A(G')=p_2-f(n)$ exactly for
  $n=3,4,5,6$ by a fresh 5000-trial exact-`Fraction` search (matching the
  builder's own $n=3,4$ checks and extending to $n=5,6$), including a
  20000-trial search over the *full* (not just $p_2$-uncut) $(\dagger)$
  domain at $n=3,4,5$ finding the same maximum — corroborating, not proving,
  that the uncovered "$G'$ cuts $p_2$" sub-case is not the true bottleneck.
  Honestly left open: that complementary sub-case of $(\dagger)$, and the
  entire $v<p_2$ case (correctly diagnosed as not reducible to the existing
  rescaling mechanism, since $v$ is not tied to the tail's own ladder
  scale). **4 new lemmas certified**
  (`single-residual-indicator`, `single-residual-exact-peel-identity`,
  `v-geq-p2-budget-reduction`; Proposition 22 not certified standalone per
  the builder's own honest flag, since it is only a conditional partial
  closure of $(\dagger)$).

  `lp-duality-certificate` pivoted (as its own round-8→9 arc intended) to
  formalizing Theorem C′ (bisect $p_1$, recurse optimally on the tail) into
  a full general-$n$ identity, and found a genuine, previously unflagged
  **structural dependency** in the outline's induction plan: closing the
  $p_1\ge T/2$ regime at level $n$ via Theorem C′ needs the *full*
  (both-regime) theorem $P(n)$ for an *arbitrary* tail one level down, not
  just its own $p_1\ge T/2$ half — so the two regimes cannot be closed
  independently past the point where the full theorem is already known.
  Reviewer confirms this diagnosis is correct and not a fixable oversight:
  it is a genuine coupling in the induction's hypothesis requirement (not an
  unfixable logical circularity, but a real "must close the other half
  first" dependency), verified by tracing exactly what Theorem C′'s proof
  needs. Consequently the $p_1\ge T/2$ regime is **rigorously and
  unconditionally closed only for $n\le3$** (using the already-certified
  `n2-upper-bound-lp-argument` as the base case $P(3)$) — reviewer
  independently re-verified this closure by a 200,000-trial exact-`Fraction`
  search over random 4-piece markings with $p_1\ge T/2$, zero violations of
  $\Phi_{\min}\le a_3T$. Also proved and reviewer-reverified in full: the
  **telescoping threshold identity** $a_{n-1}=a_n/(2(1-a_n))$ (general $n$,
  not a finite check); **Theorem B$_k$** (peel against any tail element,
  not just $p_2$); **Theorems D′, E** (bisect-top-and-bottom / bisect-top-
  two, recursive versions) and their exact threshold algebra, including a
  general (not just spot-checked) proof that the equal-pieces marking is
  never certified by Theorem D′'s IH-ceiling mechanism for any $n\ge2$. A
  **new witness** $(2/5,3/10,1/5,1/10)$ at $n=3$ was found to defeat both
  Theorem D′ and Theorem E (both give $0.55$) but is resolved exactly by
  Theorem B$_k$ with $k=4$ plus a further bisection, achieving $\Phi=1/2$
  exactly — reviewer independently re-verified this exact computation and,
  separately, ran a 300,000-trial randomized search over legal 3-cut
  strategies at this witness confirming no strategy beats $1/2$ (best found
  $0.5004$, consistent with $1/2$ being the true optimum). This is a
  genuine new triangulation with round 4/8's diagnosis that the $p_1<T/2$
  regime resists any single closed-form template. **6 new lemmas certified**
  (`bisect-top-recursive-identity`, `telescoping-threshold-identity`,
  `generalized-peel-identity`, `bisect-top-bottom-recursive-identity`
  [covers both Theorem D′ and Theorem E], `full-match-achievability`
  [Theorem A, backfilled from round 8 since round 9 builds on it directly]).

  **Net effect:** both approaches made genuine, verified, non-overclaimed
  progress this round, each honestly narrowing its own open item further
  (Claim (B) now closed for $\ell(F)\in\{0,1\}\cap\{v\ge p_2,\ p_2\text{
  uncut}\}$; the upper bound's $p_1\ge T/2$ regime now closed for $n\le3$).
  Neither closes its target in general; **Status remains `partial`.**

- **Round 10 (2 built slugs, both CHANGES REQUESTED, no RETHINK/APPROVE;
  reviewer independently re-derived/re-verified every new claim below with
  fresh exact-`Fraction` scripts of its own, not the builders' own, and in
  two places caught and fixed bugs in its *own* first-draft verification
  scripts before accepting or rejecting a result — see notes below).
  `greedy-halving-adversary` advanced restricted Claim (B)'s $\ell(F)=1$
  case further: new **Lemma 23** (general ladder dominance, $p_i>\sum_{j>i}
  p_j$ and $p_i=2p_{i+1}$ for every level $i$, not just $i=1$) and
  **Lemma 24** ($p_2-s=f(n)$) are exact two-line algebraic facts, reviewer
  independently re-derived and confirmed exactly for $n=1,\dots,8$. **New
  Proposition 25** closes one branch of $(\dagger)$'s $p_2$-cut complement
  **unconditionally** (no induction hypothesis): reviewer re-verified with a
  freshly-written script (12,000 trials, $n=3,\dots,6$) that *correctly
  respects individual tail-piece boundaries when generating a "legal
  refinement"* — the reviewer's first draft of this check ignored piece
  boundaries (treating the tail's total mass as freely re-composable) and
  spuriously found "violations" that vanished once corrected, a useful
  reminder that "legal refinement" means splitting each original piece
  independently, not any composition of the combined total. **New
  Proposition 24** closes the $v\in[s,p_2)$ sub-branch of the $v<p_2$ case
  (conditional on $(\star_{n-2})$, unconditional for $n\le4$): reviewer
  re-verified with a corrected script (16,000 trials, $n=3,4$) that also
  respects the exact cut-budget coupling between $F$'s own cut count and the
  tail's remaining budget (the first draft ignored this coupling and, like
  Proposition 25's check, found spurious violations that vanished once
  fixed) — zero violations once both the piece-boundary and budget
  couplings are honored. Both propositions' scoping is exactly as claimed
  (the open branches — $v<s$, the remaining $p_2$-cut-complement branches,
  $\ell(F)\ge2$ — are honestly listed as still open, not silently dropped).
  Sub-target 3 (the $\ell(F)$-Collapse Lemma) is honestly reported as
  attempted and not closed, consistent with the file's own Status. **4 new
  lemmas certified** (`general-ladder-dominance`, `level-2-dominance-
  identity`, `p2-cut-complement-branch-closure` [Proposition 25],
  `v-in-s-p2-closure` [Proposition 24, certified with its conditional
  status — unconditional only for $n\le4$ — preserved, not silently
  dropped]).

  `lp-duality-certificate` advanced both routes on the general upper
  bound's open $p_1<T/2$ regime. **Route B** produced a genuine new general
  **Iterated Greedy-Peel Construction** (always-legal, $\le n$ cuts, exact
  closed form $A(M)=v_{\text{final}}$) — reviewer independently re-verified
  the exact identity (3000 fresh trials, zero mismatches) and independently
  re-derived the reported counterexample (equal-pieces marking, $n=4$:
  $\Phi=3/5>16/31=a_4T$, exact match) plus an independent stress test (2000
  trials, uniform random compositions rather than the builder's own
  integer-ratio sampling) confirming a large failure rate (62% in the
  reviewer's independent sampling vs. the builder's reported 48% under a
  different sampling method) — both confirm the same qualitative dead end
  ("always match top two" is not a universal strategy), so the honestly-
  reported counterexample is corroborated, not merely trusted. The file's
  correction of the round-10 outline's "equivalent" claim to "sufficient,
  not equivalent" is independently confirmed valid (reviewer re-checked the
  cited witness $M'=\{5,4,4,1\}$: $A(M')=4\ne$ a single leftover value,
  confirming the odd-run-reduced set need not have size $\le1$). **Route A**
  produced a new **Simplex Exchange-Smoothing Vertex-Maximization Lemma**
  (dropping the box constraint from the certified
  `exchange-smoothing-vertex-maximization`) — reviewer's independent
  numerical check (finite-vertex-family enumeration vs. a fresh
  Nelder-Mead/random-search continuum optimizer, 15 random test cases)
  **found a genuine imprecision in the lemma's literal STATEMENT**: it
  restricts "pinned" coordinates to values in $\{\tau_1,\dots,\tau_r\}$
  only, omitting $0$ — but the lemma's own PROOF explicitly uses the
  reference set $R:=\{0,\tau_1,\dots,\tau_r\}$ (boundary case "(i) $f_j$
  hits $0$" is treated as a stopping condition throughout the proof). The
  reviewer exhibited a concrete case ($\tau=(3.798,1.115)$, $s=3.053$,
  $k=3$) where the true maximizer is $F=\{3.053,0,0\}$ (two coordinates
  pinned at $0$, one free) — **not** expressible in the literal statement's
  vertex family (which would require all $k-p$ "remaining" coordinates to
  share one common value, but here $0,0,3.053$ are not all equal, and $0$ is
  not in the allowed pin set) — and confirmed that adding $0$ to the
  allowed pin set repairs the statement exactly (with the fix, the
  vertex-family prediction matched the continuum optimizer's true maximum in
  all 15 test cases to numerical precision). This is a real, fixable gap in
  how the lemma is *stated* (not in the underlying mathematical mechanism,
  which the proof correctly establishes) — **not certified as currently
  written**; recommend the next round restate Lemma A.1 with the pin set
  $\{0,\tau_1,\dots,\tau_r\}$ and re-derive A.2/A.3's downstream restatement
  accordingly before relying on it further (A.2's own vertex-family
  statement has the identical omission and should be corrected at the same
  time). This does not affect anything already claimed complete this round,
  since A.3's finite optimization is explicitly left open regardless. **2
  new lemmas certified** (`iterated-greedy-peel-identity`,
  `greedy-top-two-matching-insufficiency` dead-end record); **1 lemma
  submitted but not certified** (`simplex-exchange-smoothing-vertex-
  maximization` — statement gap found, left in `lemmas/` with a reviewer
  correction note appended rather than deleted, so the next round can fix
  and re-submit rather than re-derive from scratch).

  **Net effect:** both approaches made real, independently-corroborated
  progress narrowing their respective open regimes further, and the
  reviewer's adversarial re-derivation caught (and, on two occasions in
  `greedy-halving-adversary`'s case, self-corrected past its own scripting
  bugs to reach) a correct verdict rather than trusting either builder's own
  numerics at face value; it also caught a real statement-level gap in a
  proposed lemma (`simplex-exchange-smoothing-vertex-maximization`) before
  certification. Neither approach closes its target in general; **Status
  remains `partial`.**

- **Round 11 (2 built slugs, both CHANGES REQUESTED, no RETHINK/APPROVE;
  reviewer independently re-derived/re-verified every new claim below with
  fresh scripts, not the builders' own).**

  `greedy-halving-adversary` consolidated Propositions 16, 20–25 into one
  unified strong-induction statement Theorem $P(n)$ (restricted Claim (B),
  $\ell(F)\le2$), holding whenever $L(n-1)$ and $L(n-2)$ (the full
  unrestricted lower bound one/two levels down) both hold — precisely
  tracing which branch needs which depth. New **Lemma 25** (a fully general,
  non-ladder exact identity $A(F\cup G)=A(G)+A(F_1\cup G)-A(F_2\cup G)$ for
  $\ell(F)=2$ splits) is correct — reviewer independently re-derived and
  re-verified it with a fresh 5000-trial exact-`Fraction` script (after first
  catching its own script bug: it initially used the wrong convention for
  $A$ — literal game value instead of the file's own alternating-sum
  $A(S)=\sum(-1)^{i+1}L_i$ — which spuriously produced near-100% mismatches;
  once corrected, zero mismatches). Used to case-split $\ell(F)=2$ into three
  sub-cases: **sub-case (a)** (both residuals $\ge p_2$) closes conditional
  only on $L(n-1)$; **sub-case (b)** and **sub-case (c)** (mixed regime)
  honestly reduce to precise, still-open instances of the $\ell(F)=1$
  obstruction, no new leverage. **Reviewer finding, a correction to the
  approach file's framing:** sub-case (a) is **vacuous for the ladder** —
  since $p_1=2p_2$ exactly (`general-ladder-dominance`) and
  $\mathrm{Total}(F)=p_1$ with $P\ge0$, requiring $v_1,v_2\ge p_2$ forces
  $v_1=v_2=p_2$ exactly, contradicting $v_1>v_2$ ($\ell(F)=2$'s own defining
  condition — equal values would make $\ell(F)=0$, not $2$). So no legal
  ladder configuration ever satisfies sub-case (a)'s hypothesis; its
  "closure" is a vacuously-true implication, not the substantive new content
  the approach file's header claims ("a genuinely new closed sub-case, same
  depth as $\ell(F)=0$"). This does not affect $P(n)$'s correctness (a
  vacuous branch trivially holds) but is an overclaim of significance that
  should be corrected in exposition next round. Separately, **$P(3)$'s claim
  of complete, unconditional closure at $n=3$ is correct** — reviewer
  independently reverified with a fresh 200,000-trial continuum random
  search over every legal $(F,G')$ with $\ell(F)\le2$ at $n=3$: zero
  violations, minimum found ($\approx0.06698$) consistent with the target
  $f(3)=1/15\approx0.06667$. This is genuine new progress (one clean
  statement, one new fully general identity, a precisely-traced recursion
  depth, and a newly fully-closed $n=3$ instance of restricted Claim (B))
  but does **not** establish $L(n)$ for any new $n$: $\ell(F)\ge3$ splits of
  $p_1$ remain completely untouched, and $P(n)$ for $n\ge4$ is conditional.
  **2 new lemmas certified** (`l2-general-exact-identity`,
  `p3-unified-restricted-claim-b-closure` — the latter certified for its
  overall $P(3)$ conclusion, explicitly *not* certifying "sub-case (a)" as
  meaningful standalone content per the vacuity finding above).

  `lp-duality-certificate` completed both round-11 tasks. **(a) Pin-set
  fix:** proved the general, elementary **Zero-Pin Harmlessness Lemma**
  (appending zero-valued elements changes no rank-sum quantity) and used it
  to give a corrected, fully-reproved **Simplex Vertex-Maximization Lemma**
  (pin set now $\{0,\tau_1,\dots,\tau_r\}$, matching what the original
  proof's exchange argument always used internally) — this genuinely closes
  the round-10 gap the reviewer had left uncertified. Reviewer independently
  re-verified with a fresh, more careful continuum optimizer (multi-start
  Nelder-Mead, tight tolerances) against the corrected finite vertex family
  over 20 fresh random test cases: zero mismatches (an initial quick
  single-start scan produced 3 spurious "mismatches" that were pure optimizer
  artifacts, not real gaps — corrected before concluding). **(b) Witness
  reclassification:** reviewer independently recomputed both on-file hard
  witnesses' cut-$p_1$-only optimum by brute-force enumeration and confirms
  the correction is right: $(3/8,1/4,1/4,1/8)$ **is** solved by a
  cut-$p_1$-only strategy (trisecting $p_1$ gives $\Phi=1/2\le8/15$ exactly,
  matching round 4's ad hoc discovery as a $k=3$ vertex of this family), while
  $(2/5,3/10,1/5,1/10)$ genuinely defeats every cut-$p_1$-only strategy
  (minimum $11/20=0.55>8/15$, reviewer-recomputed by independent brute-force
  vertex enumeration, exact match to the builder's figure) — only the latter
  witness is the correct citation for "Route A is insufficient in general."
  New **Per-Piece Vertex Decomposition Theorem** (dropping the "cut $p_1$
  only" restriction: at a global minimizer over an arbitrary composition,
  every piece's own split is independently a maximizer of the corrected
  Simplex Vertex-Maximization problem relative to the rest of the final
  multiset) is a genuine, marking-agnostic generalization — reviewer
  independently re-verified the standard "each block of a jointly-optimal
  product-space point is itself optimal" argument and spot-checked it
  numerically on a 3-piece mixed-composition marking. **Honestly left open,
  as anticipated**: evaluating this joint vertex family in closed form
  against $a_nT$ for an arbitrary marking — no tail-structure-agnostic
  analogue of the ladder-specific Ratio-2 Spacing Lemma / Last-Element Bound
  was found this round, and the crude $A\le\mathrm{Total}$ substitute is
  confirmed too weak (equal-pieces marking, mirroring why two prior
  mechanisms already failed there). **3 new lemmas certified**
  (`zero-pin-harmlessness-lemma`, `per-piece-vertex-decomposition-theorem`,
  and the corrected `simplex-exchange-smoothing-vertex-maximization` —
  superseding the round-10 version that was left uncertified).

  **Net effect:** both approaches made real, independently-corroborated
  progress; `lp-duality-certificate`'s round-10 gap is now genuinely closed
  and its witness-classification error corrected; `greedy-halving-
  adversary`'s consolidation is real but includes one vacuous sub-case
  mischaracterized as substantive (corrected here, does not affect
  correctness). Neither approach closes its target in general; **Status
  remains `partial`.**

- **Round 12 (2 built slugs, both CHANGES REQUESTED, no RETHINK/APPROVE;
  reviewer independently re-derived/re-verified every new claim below with
  fresh scripts, not the builders' own).**

  `greedy-halving-adversary` attacked the round-11-flagged gap in the
  $\ell(F)=2$ branch's mixed-regime sub-case (c). **New Proposition 26**
  fully closes sub-case (c) for the minimal-cut instance ($P=\varnothing$,
  $c=1$, the unique unequal two-fragment split of $p_1$), conditional only
  on $L(n-1)$ — the same recursion depth already used elsewhere in
  Theorem $P(n)$, introducing no new dependency. Mechanism: a from-scratch
  (not cited) continuous-coordinate closed form for $A(\{t\}\cup G')$ via
  the certified `cross-term-identity-threshold`, a monotonicity argument
  reducing the inequality on all of $(0,p_2)$ to its right endpoint
  $t=p_2$, and the certified `safe-window-lemma`'s exact truncation
  identity converting that endpoint check into precisely $L(n-1)$ applied
  to the rescaled tail. **Reviewer independently re-verified all four
  load-bearing pieces from scratch** (a fresh script, not the builder's):
  the final bound (7500 trials, $n=2,\dots,6$), the Lemma-25 sub-case-(c)
  identity (5000 trials), the endpoint truncation identity (2500 trials),
  and the monotonicity of $D(t)$ (4800 trials) — zero violations in all
  four checks. This is genuine, unconditional (modulo $L(n-1)$) new
  progress, correctly scoped: it does **not** extend to $P\ne\varnothing$
  ($c\ge3$), and the approach file gives a precise (not hand-waved)
  diagnosis of exactly why — the safe-window truncation is exact only at
  $t=p_2$, not at the shifted boundary $t^*=p_2-\mathrm{Total}(P)<p_2$ that
  $P\ne\varnothing$ forces, and the quantity needed there is exactly what
  Propositions 20–24 already analyze but only as a *lower* bound, never
  the *upper* bound sub-case (c) needs — a genuinely new open item, not a
  free corollary of existing machinery as the round-12 outline had hoped.
  Round-11's $P(3)$ full unconditional closure is reverified unaffected
  (at $n=3$, $P\ne\varnothing$ forces the entire budget onto $p_1$, forcing
  $G'=\tau$ with zero adversarial freedom — reduced to one finite
  computation, independently re-derivable). **1 new lemma certified this
  round** (`l2-subcase-c-p-empty-closure`, i.e. Proposition 26 — certified
  exactly for its stated scope, $P=\varnothing$ only).

  `lp-duality-certificate` was redirected by its own round-12 outline
  after the outline-reviewer confirmed by brute force that the planned
  "close every gap with one cut" pigeonhole construction fails
  ($\approx60\%$ at $n=3$, $\approx99.6\%$ at $n=4$) — correctly not built.
  Instead produced two new, fully general, unconditional, non-numeric
  lemmas: **Equal-Pieces Closure** (the all-equal-pieces marking is closed
  for every $n$ by a two-line 0-or-1-cut construction giving $\Phi=T/2<a_nT$)
  and **Spare-Cut Bisection Corollary** (whenever the certified Iterated
  Greedy-Peel Construction finishes with spare cut budget and a nonzero
  leftover, bisecting that leftover gives $\Phi=T/2<a_nT$, marking-agnostic).
  **Reviewer independently re-verified both from scratch:** Equal-Pieces
  Closure exactly for $n=0,\dots,7$ (`verify_lpdual.py`); the Spare-Cut
  Bisection Corollary via a from-scratch *physical* fragment-by-fragment
  simulation of the greedy-peel process (not just its abstract
  bookkeeping), 2400 random markings, $n=1,\dots,6$, zero mismatches in
  both the underlying identity and the corollary itself
  (`verify_sparecut2.py`). Then honestly quantified, rather than closed,
  the remaining general upper-bound gap: a fresh 4000-trial genericity
  check shows the residual case (greedy-peel uses full budget with zero
  mid-process ties) is the *generic* case for markings without exact
  symmetry (only 3/4000 trials had mid-process ties), a downward
  calibration of the outline's own more optimistic estimate; and a second
  natural candidate construction ("always bisect the current largest
  fragment", $n$ rounds) is refuted by an explicit exact witness ($n=2$,
  marking $(177,6/5,62/123)$: construction gives $\Phi=65561/492\approx
  133.3$, target $a_2T=439612/4305\approx102.1$ — reviewer independently
  recomputed this exact witness and confirms it precisely,
  `verify_r124.py`). **2 new lemmas certified this round**
  (`equal-pieces-closure`, `spare-cut-bisection-corollary`); the genericity
  calibration and the bisect-largest refutation are honest diagnostic
  findings, correctly not promoted to lemma status.

  **Net effect:** both approaches made real, independently-corroborated,
  non-overclaimed progress — one new sub-case of the lower bound closed at
  the theorem's existing recursion depth, and two new general closures of
  the upper bound for two more classes of marking (equal-pieces; any
  marking where greedy-peel leaves spare budget), plus two honestly
  negative/diagnostic findings narrowing the true remaining difficulty.
  Neither approach closes its target in general; **Status remains
  `partial`.**

- **Round 13 (2 built slugs, both CHANGES REQUESTED, no RETHINK/APPROVE;
  reviewer independently re-verified every new claim below with fresh
  exact-`Fraction` scripts of its own, not the builders' own).**

  `greedy-halving-adversary` attacked $(\dagger)$'s $p_2$-cut complement
  (the last open branch of restricted Claim (B)'s $\ell(F)=1$, $v\ge p_2$
  sub-case) via a new, fully general **Triangle Bound for $A$** (Lemma 27:
  $A(X)-A(Y)\le A(X\cup Y)\le A(X)+A(Y)$ for any two multisets $X,Y$,
  derived purely from the already-certified `cross-term-identity-threshold`
  + `integral-alternating-sum-formula`) — reviewer independently re-derived
  and re-verified with a fresh 20,000-trial exact-`Fraction` script
  (`/tmp/round-13/verify.py`), zero violations. Built on it, **Proposition
  28** proves, unconditionally (no induction hypothesis at all), that
  whenever $p_2$'s own induced split has a dominant fragment
  ($f_1\ge\mathrm{Total}(\text{rest})+s$), $A(F_2\cup R)\le p_2-A(R)$ —
  reviewer independently re-verified with a fresh 30,000-trial exact-
  `Fraction` script (`/tmp/round-13/verify_prop28.py`, 4,820 trials
  actually satisfying the dominance hypothesis), zero violations. **This is
  correctly scoped, not overclaimed**: the file's own text honestly flags
  that turning Proposition 28 into a *complete* closure of this branch of
  $(\dagger)$ still needs one more (not-yet-written-out) bookkeeping step
  combining it with the existing $(\star_{n-2})$-style recursive argument
  (mechanically identical to Proposition 22's, per the builder's own
  precise diagnosis) — reviewer confirms this residual step is real and
  correctly left open, not silently assumed. The complementary
  "no-dominant-fragment" branch (e.g. symmetric bisection of $p_2$) is
  honestly reported as genuinely open, diagnosed as the same difficulty as
  Claim (A)'s Case I but not solvable by verbatim transplant of
  `ratio-2-spacing-lemma`/`last-element-bound` (those need a raw, unrefined
  reference sequence; here the reference has already been cut) — a real,
  precise diagnosis, not hand-waving. The round-13 outline's third target
  ($\ell(F)=2$, $P\ne\varnothing$ shifted-reference sub-case) is honestly
  reported as attempted-but-not-completed (ran out of round budget before
  the shifted dominance threshold could be carried through), correctly not
  claimed as progress. **2 new lemmas certified**
  (`triangle-bound-for-a`, and Proposition 28 recorded as a documented
  partial result in the approach file, not separately promoted since its
  closure is admittedly incomplete).

  `lp-duality-certificate` attacked Open Gap 1 (the general upper bound)
  via the round-13 outline's Peel-Target Existence Lemma. Proved a new,
  fully general, elementary **Max Domination Lemma** ($A(S)\le\max(S)$ for
  any sorted multiset — a two-line telescoping-regroup argument) — reviewer
  independently re-derived and re-verified with a fresh 20,000-trial exact-
  `Fraction` script, zero violations. Used it to derive a genuinely new
  **unconditional** sufficient condition ($p_2\le T/D_n$ closes the upper
  bound with zero induction dependence, for every $n$ and every marking,
  via bisecting $p_1$ alone) — reviewer independently re-verified with a
  fresh 20,000-trial script (2,374 trials satisfying the threshold), zero
  violations. This correctly sharpens the outline's proposed binary
  dichotomy into an honest **trichotomy**: case (a) [conditional-on-IH,
  already known — reviewer confirms the transfer claim, since the cited
  Corollary's derivation never specialized to $k=2$], case (b1) [new,
  unconditional, genuinely disjoint from every prior sufficient region],
  case (b2) [a real, non-vacuous open region, with an explicit witness at
  $n=3$ verified to sit outside both other cases]. The natural 2-cut
  "peel-then-dominate" extension proposed to close case (b2) was tested and
  **correctly refuted** by an exact witness (a genuine negative result, not
  a repeat of round 12's refuted "bisect-largest-cascade" — structurally a
  different move family). **Open Gap 1 is honestly reported as not closed**
  — no overclaim. **2 new lemmas certified**
  (`max-domination-lemma`, `unconditional-p2-threshold-closure`).

  **Net effect:** both approaches produced genuinely new, unconditional,
  reviewer-verified general-purpose lemmas this round (Triangle Bound +
  Max Domination, both elementary and fully general, immediately reusable
  elsewhere), plus one new closed sub-case each (Proposition 28's
  dominant-fragment branch, modulo one flagged bookkeeping step; the
  $p_2\le T/D_n$ unconditional region) and one honestly-reported refuted
  construction (peel-then-dominate). Neither approach's own target
  ($(\dagger)$'s $p_2$-cut complement; Open Gap 1) is closed. **Status
  remains `partial`.**

- **Round 14 (2 built slugs, both CHANGES REQUESTED, no RETHINK/APPROVE;
  reviewer independently re-derived/re-verified every new claim below with
  fresh exact-`Fraction` scripts of its own, not the builders' own).**

  `greedy-halving-adversary`'s headline claim — that new **Theorem 29
  (Half-Dominance Split Bound)**, via a new **Lemma 29a (Symmetry
  Lemma)**, fully closes the round-13 `p2-Pinned-Dominance Lemma` in one
  shot (superseding Proposition 28) — is **verified correct, no gap
  found**. The reviewer independently re-derived Lemma 29a's two-case
  argument from scratch (case (i) $g_1<M/2$ trivial; case (ii)
  $g_1\ge M/2$ via the parity identity $u_{F_2}=1-u_{\mathrm{Rest}}$ on
  $[0,g_1)$ plus the elementary $A(S)\le\mathrm{Total}(S)$ bound) and
  re-verified with a fresh 20,000-trial exact-`Fraction` script (zero
  violations), then independently re-derived Theorem 29's proof
  (cross-term identity + a pointwise algebraic bound + Lemma 29a) and
  re-verified with a fresh 20,000-trial script over generic $M,F_2,R$ with
  $\max(R)\le M/2$ (zero violations). Confirmed the theorem's scope claim
  is honest: it is fully general (any $M$, any $R$ with $\max(R)\le M/2$)
  and the ladder enters *only* via the Corollary's input fact
  $\max(R)\le p_2/2$ (from `safe-window-lemma` one level down + Lemma
  23's $p_2=2p_3$) — cross-checked against the on-file non-ladder
  counterexample $\tau=\{49,2/5\}$, $m=203/4$: $\max(\tau)=49>m/2=203/8$,
  so the hypothesis genuinely fails there, exactly as the theorem
  requires (not contradicting it). This is a genuine, general-purpose,
  reusable closure of the last open branch of $(\dagger)$'s $p_2$-cut
  complement — real progress, correctly not overclaimed as closing the
  whole lower bound. **Second target, Proposition 29b** ($\ell(F)=2$,
  $P\ne\varnothing$, widening the threshold from the outline's anticipated
  $\tau_P\le f(n)$ to $\tau_P<p_3=p_2/2$ via `sharp-dominant-removal-
  identity`) is also **verified correct**: reviewer independently
  re-verified the "$P$'s exact pairs are parity-invisible even when
  unioned with an extra reference set" generalization (fresh 20,000-trial
  script), `sharp-dominant-removal-identity`'s hypothesis/conclusion
  (fresh 20,000-trial script), the algebraic chain
  $t^*=p_2-\tau_P>p_3\ge\max(G')$ under $\tau_P<p_3$, and an end-to-end
  simulation on the actual $n=5$ ladder (3000 valid random trials, zero
  violations of $A(F\cup G')\ge f(n)$). The complementary range
  $\tau_P\ge p_3$ is honestly and correctly left open (same "$v<s$"
  obstruction as Proposition 24) — not silently dropped. **3 new lemmas
  certified** (`symmetry-lemma-29a`, `half-dominance-split-bound`
  [Theorem 29 + Corollary], `proposition-29b-partial-closure`).

  `lp-duality-certificate` produced a genuine generalization, the
  **Bisect-Top-$k$ Lemma** ($k=1,\dots,n$, unconditional, strictly
  generalizing the certified `unconditional-p2-threshold-closure`'s
  $k=1$ case), proved via a clean $k$-step chain of
  `pair-cancellation-identity` applications plus `max-domination-lemma` —
  reviewer independently re-derived the chaining argument (valid since
  the pair-cancellation identity imposes no ordering/domination hypothesis
  between the injected pair and the reference multiset, so insertion
  order is immaterial) and re-verified with a fresh 7000-trial
  exact-`Fraction` script (zero violations), confirming it covers only
  $\approx10$–$26\%$ of case (b2), honestly reported as partial, not a
  closure. The two new **dead-end lemmas** (Peel-$p_1$-$p_2$-Plus-IH
  Zero-Slack Dead End: threshold $p_2\ge a_nT/2$ exactly; Bisect-$p_1$-
  Plus-IH Containment Dead End: threshold $p_1\ge a_nT$ exactly) are
  **independently re-derived algebraically from scratch** by the
  reviewer (not just re-run): solving both threshold equations exactly in
  `Fraction` arithmetic for $n=1,\dots,14$ confirms
  $\frac{a_n-a_{n-1}}{1-2a_{n-1}}=\frac{a_n}{2}$ and
  $\frac{a_n-a_{n-1}}{1/2-a_{n-1}}=a_n$ exactly in every case, matching
  the claimed zero-slack thresholds precisely — both dead-ends are
  correct, rigorous negative results (not just numeric refutations),
  correctly certified so no future round re-attempts either exact
  mechanism into case (b2). The round's third target (a vertex-restricted
  case-(b2) probe) is honestly reported as an incomplete, non-rigorous
  numeric diagnostic (weak evidence of slack, not a proof) — correctly
  not promoted beyond that status. **3 new lemmas certified**
  (`bisect-top-k-lemma`, `peel-and-bisect-ih-dead-ends` [both negative
  lemmas in one file]).

  **Net effect:** both approaches produced genuinely new, correctly-proved,
  reviewer-verified lemmas this round with no gaps found — one closes an
  entire previously-open branch of restricted Claim (B)'s recursion
  ($(\dagger)$'s $p_2$-cut complement, in full, via Theorem 29), the other
  sharpens and rigorously rules out two natural mechanisms for the upper
  bound's hardest remaining region (case (b2)). Neither approach's own
  top-level target (the full general lower bound; Open Gap 1 in full) is
  closed — case (b2) and the $\ell(F)=2$, $P\ne\varnothing$, $\tau_P\ge p_3$
  range both remain genuinely open, honestly reported as such in both
  approach files. **Status remains `partial`.**

- **Round 21.** `greedy-halving-adversary` proved a new general **Band-Parity
  Fact** (for any sorted-descending multiset, the truncation-parity
  indicator $\epsilon(v)$ is constant on each half-open band between
  consecutive elements — elementary, general, reviewer-verified, certified)
  and used it plus the certified `truncated-alternating-sum-floor` lemma to
  prove **Theorem 35a$'$**, closing the true $\epsilon$-corrected target
  $(\Diamond')$ (strictly stronger than the previously-closed $(\Diamond)$)
  throughout Theorem 35a's range $v\in[0,p_3)$: unconditionally on
  $v\in[0,s']$ (reviewer independently re-verified this sub-range exactly,
  by hand and by a 5000-trial exact-`Fraction` script over legal per-piece
  refinements, zero violations) and conditional on $(\star_{n-3})$ on
  $v\in(s',p_3)$. **Reviewer found a genuine algebra bug in the cited
  Theorem 35b** (round 19): its "cross-level identity" step computes
  $D_{n-3}\cdot f(n-3)=2^{n-3}$, but by definition $f(n-3):=1/D_{n-3}$ so
  $D_{n-3}\cdot f(n-3)=1$ identically — Theorem 35b's stated conclusion
  $A(T')\ge f(n)\cdot2^{n-3}$ is **false** as written (explicit
  counterexample: $n=4$, $T'=\{p_4,p_5\}$ untouched gives $A(T')=1/31=f(4)$,
  strictly less than the claimed $f(4)\cdot2=2/31$). This bug is
  **non-fatal**: the actually-needed, correctly-derivable weaker bound
  $A(T')\ge f(n)$ (exact equality at the untouched base case, verified
  by the reviewer to hold for all legal per-piece budgets $n=3,\dots,8$,
  5000+ trials, via the trivial identity $D_{n-3}f(n-3)=1$, no "cross-level
  identity" needed at all) is exactly what Theorem 35b's own use and
  Theorem 35a$'$'s sub-range 2 actually require, and both survive. Theorem
  35b needs a one-line correction (drop the false $2^{n-3}$ factor) before
  further reuse; flagged, not yet fixed. Steps 4 (Theorem 35b's own range)
  and 6 (Theorem 36's Case (b)) are honestly left open, as instructed — no
  overclaim found beyond the flagged Theorem 35b bug. **Band-Parity Fact
  certified**; Theorem 35a$'$ certified as a scoped, honest result but
  its citation chain needs the Theorem 35b fix noted above.

  `rank-pigeonhole-budget` proved the TRUE $\varepsilon$-corrected target
  $(\sharp')$ at $n=3$ in full (§7.5), superseding round 19/20's
  $(\sharp)$-only closure: using the Band-Parity Fact to locate
  $\varepsilon(v_2)=1$ exactly on the interior band $v_2\in[p_4,p_3)$,
  reducing $(\sharp')$ there to the clean inequality $v_1+v_2\le6p_4$,
  proved strictly by summing the two independent domain bounds
  $v_1<p_2=4p_4$ and $v_2<p_3=2p_4$. **Reviewer independently re-verified
  this closure exactly** (by hand and by a 200000-trial exact-`Fraction`
  script over the full domain, zero violations) — no bugs found, unlike
  the sibling's Theorem 35b. §7.6 (general $n\ge4$) is honestly left open,
  correctly re-encountering the project's central cross-piece tie-vertex
  obstruction. The file's own `Status: solved` header is correctly scoped
  to Claim (A) only (already APPROVEd round 8) — the new §7.5 result is
  explicitly an addendum that does not change Claim (A)'s status, and does
  not claim to close the whole imo-2026-03 problem.

  `lp-duality-certificate` proved the conditional **Within-Chamber Affinity
  Theorem** for case (b2)'s LP-vertex framing: if the joint tie/pin
  coefficient matrix $M(\tau)$ is invertible, $\Phi_{\min}$ is affine in
  $p$ on the corresponding chamber, via a from-scratch joint linear system
  $M(\tau)\mathbf v=Np$ with type-dependent ($p$-independent) coefficients
  in $M(\tau)$ and a linear-in-$p$ right-hand side — reviewer independently
  re-derived the row structure (mass-conservation rows are forced-linear in
  $p$, tie/pin coefficients are pure combinatorial counts) and confirmed the
  standard linear-algebra argument (unique solution when $M(\tau)$
  invertible $\Rightarrow$ linear in $p$) is sound. A companion Proposition
  proves $M(\tau)$ singular forces the type to have empty interior in
  $p$-space except for one honestly-isolated residual algebraic-coincidence
  sub-case (not ruled out, but reduced to a finite, per-type checkable
  condition) — this dichotomy argument is also correct (standard
  range/null-space reasoning). **Case (b2) itself is correctly NOT claimed
  closed** — affinity is necessary infrastructure only; the actual
  extreme-point evaluation against $a_nT$ is honestly reported as not
  attempted this round, and a genuine amber-flag chamber-count growth signal
  ($\approx28\%\to64\%$ density from $n=3$ to $n=4$) is reported, not
  glossed over. (Minor labeling note: this content is internally headed
  "Round 20 build" in the approach file though it was newly added this
  round — cosmetic mislabeling, does not affect the mathematical content.)

  **Net effect:** all three built approaches made genuine, independently
  verified progress with honest scoping; one real (non-fatal) algebra bug
  was found and flagged in `greedy-halving-adversary`'s Theorem 35b
  (inherited into this round's Theorem 35a$'$ citation). **Status remains
  `partial`** for the whole problem; Claim (A) (`rank-pigeonhole-budget`,
  round 8) remains the only fully closed top-level sub-target.

## Full proof
(absent — Status is `partial`. The problem asks for general $n$; only $n=1$
and $n=2$ are fully closed. See the approach files
`approaches/greedy-halving-adversary.md`,
`approaches/smoothing-compactness-certificate.md`,
`approaches/self-similar-potential-certificate.md`,
`approaches/self-similar-bracketing.md`,
`approaches/rank-tie-vertex-reduction.md`,
`approaches/exchange-argument-extremal-response.md`,
`approaches/rank-pigeonhole-budget.md`,
`approaches/claiming-order-invariant.md`, and
`approaches/dyadic-band-occupancy.md`
for full write-ups of everything proved (and, for `claiming-order-invariant`
and part of `dyadic-band-occupancy`'s own assigned technique, rigorously
ruled out) so far, and their Open gaps sections for exactly what remains for
general $n$. Certified reusable lemmas — including round 3's
`vertex-minimum-theorem`, `odd-run-reduction-lemma`,
`pair-cancellation-identity`, `rescaled-ladder-c-equals-n-achievability`,
and this round (round 4)'s new `sharp-dominant-removal-identity`,
`tail-self-similarity`, `symmetric-split-c1-lower-bound`,
`cascading-halving-family-characterization`, and
`general-n-cascade-achievability`, and this round (round 5)'s new
`single-cut-perturbation-identity`, `cross-term-reduction-theorem`,
`interior-cross-tie-evaluation-formula`, `claim-a-achievability-construction`,
`even-rank-sum-phi-identity`, `band-decomposition-identity`, and
`claim-a-cardinality-is-essential` — are in `results/imo-2026-03/lemmas/`,
alongside the earlier dominant-element-removal identity, general cross-term
identity, alternating-sum scaling, ladder self-similarity constant,
above-threshold formula, budget monotonicity, the full n=2 lower-bound
closure, and two round-5 dead-end records
(`refutation-of-tail-refinement-monotonicity`,
`band-invariance-conjecture-refuted-dead-end`). Round 6's
`half-window-vanishing-lemma` (closes $(\star\star)$ for $c_1=1$, every
$n\ge2$) and `case-ii-closure-theorem` (closes Case II of Claim (A) for
every $n$, Theorem GC($m$)) were certified in substance in round 6 but
their standalone lemma files were only written and certified this round
(round 7), backfilled to match round-7 work's direct citations of them.
Round 7 adds `peel-decomposition-identity`, `case-ii-exact-peel-identity`
(exact $A(S)=z-A(G')$ identity for the dominant-fragment sub-case of
general $c_1\ge2$, honestly not a reduction since it's an exact
reformulation), `bounded-certificate-for-half-window-vanishing` (a
correct repackaging, not new content), `half-bound-lemma`, and
`peel-minimum-branch-closure` (closes Branch A and Branch B-odd of Case I
for every $m$, leaving exactly one sub-case $(\dagger)$ — Branch B, $N$
even — as the sole open item of Claim (A)'s Case I), plus the dead-end
record `splitting-monotonicity-refuted-dead-end`.)

- **Round 15 (2 built slugs, both CHANGES REQUESTED, no RETHINK/APPROVE;
  reviewer independently re-verified every new claim below with fresh
  exact-`Fraction` scripts of its own, not the builders', and — significant
  this round — found and confirmed two real bugs, one in each slug's
  claimed material, going beyond simply re-running the builders' own
  numerics.**

  `greedy-halving-adversary` proved a new, fully general (non-ladder)
  **Upper-Truncation Identity**
  ($\int_v^\infty u_S=A(S_{>v})-v\cdot\epsilon(v)$, $\epsilon(v)$ the parity
  of $|S_{>v}|$) — reviewer independently re-derived and re-verified it from
  scratch (3000 fresh trials, zero mismatches) — and used it to prove
  **Proposition 30**, extending Proposition 24's exact formula for
  $A(F\cup G')$ from $v\ge s$ to *every* $v\in(0,p_2)$; reviewer
  independently re-verified Proposition 30's formula with a fresh script
  across $n=3,\dots,6$ (12000 trials total), zero mismatches. This reduces
  the whole "$v<s$" item to one precisely isolated open question (an upper
  bound on $A(R'_{>v})$), honestly left open (the trivial max-domination
  route is shown, by direct computation, to be far too weak). Separately,
  the round's "cheap quick win" target (item 3, $\tau_P\ge p_3$) was
  correctly shown **not** to be cheap: the outline's crude bound fails
  (reviewer independently confirmed $\psi(p_3)=1/5>p_3=2/15$ at $n=3$ by
  hand), and both attempted repair routes reduce to the identical open
  "top-truncated alternating sum" fact as Proposition 30's own gap —
  genuine unification of items 1, 2, 3 into one obstruction, not three.
  This diagnosis also **flagged a likely bug in the already-certified
  `proposition-29b-partial-closure.md`**; the reviewer investigated this
  independently and **confirms it is a real proof gap, not merely
  notational**: that lemma's Step 4 cites `safe-window-lemma` to get
  $\max(G')\le p_3$, but this is only true if $G'$ excludes $p_2$ — the
  lemma's own Statement text says $G'$ is a refinement of
  $\{p_3,\dots,p_{n+1}\}$ (excluding $p_2$), which cannot represent a
  physically complete final multiset ($p_2$ must appear somewhere). Once
  $G'$ is corrected to be the game-legal full tail (which can leave $p_2$
  untouched), $\max(G')=p_2>p_3$ and the cited step is false. **The
  reviewer ran an adversarial grid search ($n=3,\dots,7$, $p_2$ deliberately
  left untouched — the exact configuration that breaks the cited step) and
  found zero counterexamples to the lemma's stated conclusion itself**
  (tiny but strictly positive margins, $\approx0.002$–$0.004\times f(n)$ at
  $n=3,4$, matching the builder's own `margin_check.py` finding almost
  exactly) — so the theorem appears true, but **this specific proof does
  not establish it** for the game-legal reading of $G'$. `lemmas/
  proposition-29b-partial-closure.md` has been annotated with a "Reviewer
  correction (round 15)" section recording this; **do not treat it as
  closing any part of the $\tau_P<p_3$ branch** until a repaired proof
  (handling $\max(G')\le p_2$, not $p_3$) is supplied. 2 new lemmas
  certified this round (`upper-truncation-identity`; Proposition 30 is
  reviewer-verified but not written as a standalone lemma file, since it is
  local to this approach's induction chain); 1 previously-certified lemma
  downgraded (`proposition-29b-partial-closure` — proof gap confirmed, not
  retracted, since no counterexample to its conclusion was found).

  `lp-duality-certificate` proved the **Cross-Piece Sign-Assignment
  Identity** (general: apply `odd-run-reduction-lemma`, then regroup the
  tie-free alternating sum by originating piece; if each piece's surviving
  fragments share one rank parity, the piece contributes its whole
  surviving mass with that sign) — reviewer independently re-verified with
  a fresh 20000-trial script (7961 of the trials satisfied the
  monochromaticity hypothesis; zero mismatches on all of them) — and used
  it to **independently reconstruct and confirm both round-14 near-tight
  case-(b2) witnesses are unconditionally closed** (reviewer built its own
  explicit legal fragment constructions from scratch for both the $n=3$
  and $n=4$ witnesses and confirmed $\Phi$ exactly matches the predicted
  formula and beats $a_nT$ in both cases). This is genuine, verified
  progress. However, the companion **Alternating Gap-Cross Lemma**
  (derived from the Cross-Piece identity, meant to give a closed-form
  feasibility test for a new sufficient-condition family) has a **confirmed
  sign bug**: its tail prefactor $(-1)^j$ (counting *all* $j$ pairs,
  including ones left untouched by exact equality) is wrong whenever an odd
  number of such equal/untouched pairs are used — the reviewer found an
  exact counterexample (pieces $(45,45,31,27)$, $j=2$: actual $A(M)=4$,
  formula predicts $-4$) and diagnosed the root cause (an equal/untouched
  pair contributes $2$ ranks, an even, parity-preserving shift, not the $3$
  ranks — an odd, parity-flipping shift — every pair is assumed to
  contribute; the correct prefactor is $(-1)^{j'}$, $j'=$ number of
  *actually split* pairs). Neither headline witness closure uses this
  buggy configuration, so both stand; the lemma itself has been annotated
  "NOT certified as currently written" in `lemmas/alternating-gap-cross-
  lemma.md` pending a fix, and should not be relied on for markings with
  exactly-equal adjacent pieces until repaired. Case (b2) remains open in
  general; the honestly-quantified marginal coverage gain (a few points at
  $n=3$, none at $n=4,5$ in this round's sample) stands regardless of the
  bug, since neither witness closure depended on the buggy sub-case.

  **Net effect:** both approaches made genuine, independently-verified
  progress this round (Proposition 30's exact reduction; both case-(b2)
  witnesses now unconditionally closed rather than merely numerically
  probed) — but this round's adversarial review is also notable for
  finding two real, confirmed bugs (one a genuine proof gap in an
  already-certified sibling lemma, one a sign error in a brand-new lemma),
  neither of which invalidates this round's headline results but both of
  which must be tracked and fixed before further reliance. **Status remains
  `partial`.**

- **Round 16 (2 built slugs, both CHANGES REQUESTED, no RETHINK/APPROVE;
  reviewer independently re-derived/re-verified every new claim below with
  fresh exact-`Fraction` scripts of its own, not the builders' own).**

  `greedy-halving-adversary` closed the round-15 open item outright. New,
  fully general **Truncated Alternating Sum Floor**
  (`lemmas/truncated-alternating-sum-floor.md`: for any finite multiset $S$,
  total $T$, and any $v\in[0,T]$, $A(S)-2A(S_{>v})+2v\epsilon(v)\ge v-T$) is
  a genuinely correct, elementary two-line consequence of the certified
  `upper-truncation-identity` plus trivial $\{0,1\}$-valued integral
  bounds — reviewer independently re-derived the algebra line-by-line and
  re-verified with a fresh 50,000-trial exact-`Fraction` script of its own
  (arbitrary, non-ladder multisets), zero violations. Applied to
  Proposition 30, this gives **Theorem 31: the entire $\ell(F)=1$, $v<p_2$,
  $p_2$-untouched branch (round-15's items 1 and 2) is now closed
  unconditionally, for every $n\ge3$** — no recursive hypothesis at all,
  which also upgrades Proposition 24 to hypothesis-free. Reviewer
  independently re-verified this end-to-end with a *from-scratch* script
  (not the builder's own) using arbitrary (non-ladder-specific) $R'$ subject
  only to the dominance hypothesis $p_2>\mathrm{Total}(R')$: both
  Proposition 30's identity and Theorem 31's inequality held in 20,000/20,000
  trials each, zero violations. The file also **honestly corrects its own
  round-15 framing**: Target B (item 3, $\ell(F)=2$, $\tau_P\ge p_3$) is
  **not** the same obstruction as items 1/2 after all — the Floor-lemma
  trick fails there because the relevant truncation interval has length
  $\approx r=p_2+s$ (an order of magnitude too crude) rather than
  $\approx s$; this diagnosis is worked through algebraically, not merely
  asserted, and a concrete restart point (peel $p_2$ off first via
  `dominant-element-removal-identity`) is recorded. No overclaim found.
  **1 new lemma certified** (`truncated-alternating-sum-floor`).

  `lp-duality-certificate` completed all three round-16 tasks. **(1)** The
  round-15 sign bug in `alternating-gap-cross-lemma` is genuinely fixed,
  and the fix is deeper than the outline's prescribed one-line relabeling:
  both the gap-sum's own per-pair sign *and* the tail prefactor must be
  reindexed by a split pair's **rank among split pairs**, not its raw pair
  index — reviewer independently re-derived this and re-verified with two
  fresh scripts (the exact round-15 counterexample $(45,45,31,27)$, and a
  20,000-trial randomized construction with pairs of equal/split type
  interleaved at arbitrary positions in sorted order), zero mismatches in
  both. **(2)** The new negative lemma `recursive-image-escape-dead-end`
  (case-(a)/(b1) membership of the recursed image supplies zero coverage of
  case (b2), since that case's own ceiling $a_{n-1}T'$ is tight and hence
  not improvable from case-membership alone) is algebraically sound —
  reviewer independently re-checked the telescoping-threshold algebra this
  builds on and confirms it reproduces exactly the already-certified
  zero-slack thresholds from `peel-zero-slack-dead-end`/
  `bisect-containment-dead-end`; this is a genuine generalization (forecloses
  the whole family of "recurse then read off the sub-case" arguments, not
  just the two prior specific instances). **(3)** The Task-3 grid check
  (212/214 points at $n=3$) is, on inspection of the full file text (not
  just the build report), consistently and repeatedly labeled non-rigorous
  corroboration, explicitly **not** a closure claim, in every place it is
  discussed — no oversell found. Open Gap 1 (case (b2), the general upper
  bound) remains open. **1 new lemma certified**
  (`recursive-image-escape-dead-end`); `alternating-gap-cross-lemma`
  re-certified as corrected.

  **Net effect:** `greedy-halving-adversary` fully and unconditionally
  closes another entire named branch of restricted Claim (B)'s recursion
  (items 1+2, no induction hypothesis needed) while honestly retracting an
  over-broad round-15 unification claim about Target B; `lp-duality-
  certificate` delivers a correctly-fixed lemma (harder to fix than
  originally planned) plus a clean, sound negative result narrowing what
  any future closure of case (b2) can look like. Neither approach's
  top-level target (the general lower bound in full; Open Gap 1 in full)
  is closed. **Status remains `partial`.**

- **Round 17 (2 built slugs, both CHANGES REQUESTED, no RETHINK/APPROVE;
  reviewer independently re-verified every load-bearing claim below with
  fresh scripts of its own, not the builders' own, including one
  significant detour: the reviewer's first independent check of Theorem 32
  appeared to find systematic, large-margin violations in every trial —
  traced to the reviewer's own script using the wrong target constant for
  $A(\cdot)$ ($p_1$ instead of the correct $f(n)=2c(n)-1=1/(2^{n+1}-1)$,
  which is what $A$ of the *entire* final multiset must be compared against
  since $\Phi=(\mathrm{Total}+A)/2$ and $\mathrm{Total}=1$); once corrected
  to the file's own consistent convention, the claim was confirmed correct
  in 4873+8596 fresh trials, zero violations. This is recorded as a
  reviewer-process lesson, not a builder error — the file's own $f(n)$
  convention is internally consistent throughout and was not the source of
  the discrepancy.)**

  `greedy-halving-adversary` proved a new **Two-Threshold Truncated
  Alternating Sum Floor** lemma (elementary, general, no ladder structure;
  reviewer independently re-derived the 4-line proof and confirmed the
  hypothesis $v_1\le T$ is genuinely load-bearing — the bound $I_2\le T-v_1$
  is arithmetically false once $v_1>T$) and used it to prove **Theorem 32**:
  $\ell(F)=2$ sub-case (b) ($v_2<v_1<p_2$), restricted to $v_1\le s$ and
  $p_2$ untouched in $G'$, is closed **unconditionally**, for every $n\ge3$,
  with no cap on $R'$'s cut budget. **Reviewer independently re-derived
  Step 1's algebraic substitution (Lemma 25 + Proposition 30 at both $v_1$
  and $v_2$) from scratch by hand and confirmed it reduces to exactly
  $A(F\cup G')=p_2-A(R')-(v_1-v_2)+2\int_{v_2}^{v_1}u_{R'}$, matching the
  file's claim term-for-term**, then independently re-verified the full
  chain (Steps 1–3) with two fresh exact-`Fraction` scripts (one without,
  one with full game-legality/mass-conservation/cut-budget-coupling
  enforced), 4873 and 8596 trials respectively across $n=3,\dots,7$, using
  the file's own correct target convention: **zero violations**, including
  a targeted re-check of the complementary open range $v_1\in(s,p_2)$
  (8596 trials, also zero violations — consistent with, not proving, the
  file's own honest "not closed, diagnosed as the round-15/16 crux" report
  for that range). The diagnosis that $v_1>s$ reduces to the identical
  "upper bound on $A(R'_{>v})$" obstruction already on file from round
  15/16 (not a new gap) is independently plausible from the reviewer's own
  re-derivation of the algebra (the missing ingredient is exactly a lower
  bound on the middle-band integral $I_1$, which Step 2's one-sided bounds
  cannot supply once $v_1>s$) and is not contradicted by any numeric
  evidence found. The round also correctly self-corrects an overclaim in
  round 16's own prose (the "$0\ge v-s$ trivially" extension claim,
  arithmetically false for $v>s$) without retracting Theorem 31's own
  correctly-scoped boxed statement. **1 new lemma certified**
  (`two-threshold-truncated-alternating-sum-floor`).

  `lp-duality-certificate` proved the **Convex-Combination Futility
  Theorem**: for any fixed finite family of explicit Xiang-Yu strategy
  values $\Phi_1,\dots,\Phi_k$ and any weights $\lambda_i\ge0$ summing to
  $1$ (fixed or adaptively chosen, however derived), $\sum_i\lambda_i\Phi_i
  \le\theta \iff \min_i\Phi_i\le\theta$ — a weighted combination can never
  certify a marking the plain pointwise minimum doesn't already certify.
  **Reviewer independently re-derived the proof from scratch**: the
  forward direction is the trivial degenerate-weight case; the substantive
  direction is a one-line contrapositive (if every $\Phi_i>\theta$, then
  since weights are nonnegative and sum to $1$ with at least one strictly
  positive, $\sum_i\lambda_i(\Phi_i-\theta)>0$) — this is elementary,
  correct, and matches standard convexity facts (a convex combination of
  numbers is never below their minimum) with no gap. This is a genuine,
  correctly-scoped negative result (rules out an entire mechanism, not
  just the one $(\Phi_A,\Phi_B)$ pair numerically tested) that honestly
  does not claim any new coverage of case (b2) — the file's own "Honest
  conclusion" (R17.3) explicitly states case (b2) remains open and
  redirects future rounds toward either a genuine LP-dual lower-bound
  argument for Claim (B) or a brand-new primal construction, rather than
  overclaiming progress. **1 new lemma certified**
  (`convex-combination-futility-theorem`).

  **Net effect:** both builds delivered correct, reviewer-verified,
  honestly-scoped results — one further narrows restricted Claim (B)'s
  $\ell(F)=2$ sub-case (b) to a precisely-isolated residual range (not a
  full closure), the other rigorously forecloses an entire proof strategy
  for case (b2)'s upper bound without claiming any new positive coverage.
  Neither approach's top-level target is closed. **Status remains
  `partial`.**

- **Round 18 (2 built slugs, both CHANGES REQUESTED, no RETHINK/APPROVE;
  reviewer independently re-derived/re-verified every new claim below with
  fresh scripts and, for the concavity refutation, a genuinely independent
  optimizer/enumeration strategy, not the builder's own script).**

  `greedy-halving-adversary` narrowed restricted Claim (B)'s $\ell(F)=2$
  sub-case (b) further within the range Theorem 32 (round 17) left open
  ($v_1\in(s,p_2)$). New **Theorem 33** ($v_2\ge s$) is fully unconditional
  (no induction hypothesis, no cut-budget cap on $R'$) — proved via
  $u_{R'}\equiv0$ above $s$ (so the cross term vanishes identically),
  `max-domination-lemma`'s $A(R')\le\max(R')\le p_3$, and the elementary
  fact $s-p_3\ge f(n)$ for $n\ge3$ (equality only at $n=3$, with the chain
  remaining strict there because $v_1-v_2<f(n)$ strictly). **Reviewer
  independently re-derived this algebra by hand from scratch (confirmed the
  chain $A(R')+(v_1-v_2)<s$ term-for-term, including the $n=3$ boundary
  case) and independently re-verified both the underlying Step-1 identity
  (a fresh 20,000-trial exact-`Fraction` script, confirming it requires
  $p_2>\mathrm{Total}(R')$/dominance — an unstated-but-satisfied hypothesis
  in the ladder — and produces spurious mismatches without it, a useful
  scripting lesson) and Theorem 33 itself directly against the ladder (a
  fresh 12,000-trial script, $n=3,\dots,6$, zero violations, matching the
  builder's own reported margins).** New **Theorem 34** ($v_2<s$,
  $v_1+v_2\le p_2$) is conditional on $(\star_{n-2})$ (unconditional for
  $n\le4$, same status as Proposition 24) — reviewer independently
  re-derived its algebra (the interval split at $s$, the crude bound
  $J_0\le v_2$, and the final substitution using $A(R')\ge f(n)$) and
  re-verified with a fresh 12,000-trial script, zero violations. Both
  theorems are honestly scoped: the file explicitly identifies the
  remaining open middle band $v_2\in(p_2-v_1,s)$ as **not** closed, and its
  own diagnosis that the outline's proposed per-cut charging mechanism
  fails to close it (because an individual cut's sign contribution to the
  truncated sum depends on the global parity of other fragments, not a
  local property of that cut) is a genuine, correctly-reasoned negative
  finding, not an evasion. **2 new lemmas certified** (`theorem-33-
  v1-in-s-p2-v2-geq-s-closure`, `theorem-34-v1-in-s-p2-v2-lt-s-conditional-
  closure`).

  `lp-duality-certificate` executed the round-18 outline's mandated cheap
  $n=3$ gate check for the Tail Exchange Lemma / Danskin-smoothing
  mechanism (concavity of $g(t)=\Phi_{\min}(p_1,p_2,t)$ in Liu Bang's own
  free tail marking $t$, for case (b2)) and found the mechanism's required
  premise is **false**: an interior local minimum of $g$ at $p_3=p_1-p_2$
  on the on-file near-tight case-(b2) witness, flanked by strict increases
  on both sides — impossible for a concave function. **Reviewer
  independently re-verified this with a genuinely different, from-scratch
  script**: rather than reusing the builder's `differential_evolution`
  approach, the reviewer enumerated all cut-budget compositions across the
  4 pieces exhaustively (35 compositions for budget 3) and ran independent
  multi-restart Nelder–Mead optimization within each, at a fresh grid of
  $p_3$ values — reproducing the same qualitative V-shape (decreasing
  toward $p_3\approx0.1877\approx p_1-p_2$ down to $g=0.5$, then increasing
  back up to a local max near the on-file witness $p_3\approx0.2251$
  ($g\approx0.5158$), then decreasing again toward the far endpoint) and
  the same $\mp1/2$ slope signature on both sides of the kink
  ($g(0.17)-g(0.175)=0.0025$, $g(0.195)-g(0.190)=0.0025$, both over
  $\Delta p_3=0.005$, matching the builder's own reported values exactly).
  This is a genuine, independently-reproduced negative result, not an
  artifact of one optimizer or one script (per this project's rule on
  never trusting a single-optimizer refutation) — the concavity premise is
  confirmed false, and the file's honest conclusion (case (b2) remains
  open; a future Danskin-style argument would need to work chamber-by-
  chamber, not globally) is correct and not overclaimed. No new lemma was
  submitted for certification (correctly — the finding is a refutation
  tied to a specific witness, not a general reusable statement).

  **Net effect:** both builds delivered correct, reviewer-verified,
  honestly-scoped results this round — one further narrows restricted
  Claim (B)'s $\ell(F)=2$ sub-case (b) to a precisely isolated (and now
  even narrower) residual middle band, the other rules out a fourth
  distinct mechanism family for case (b2)'s upper bound (after peel/
  bisect/recurse, weighted-combination, and naive boundary continuity),
  with a solid independent numerical corroboration by the reviewer using a
  structurally different verification method. Neither approach's top-level
  target is closed. **Status remains `partial`.**

- **Round 19 (4 built slugs: `greedy-halving-adversary` CHANGES REQUESTED,
  `minimax-lp-response-polytope` [new slug] CHANGES REQUESTED,
  `lp-duality-certificate` CHANGES REQUESTED, `rank-pigeonhole-budget`
  CHANGES REQUESTED — no RETHINK, no APPROVE. Reviewer independently
  re-derived/re-verified every load-bearing claim below with fresh scripts,
  not the builders' own.**

  `greedy-halving-adversary` found and fixed a genuine bug in round-18's
  Theorem 34: the hypothesis "$R'$ uses $\le n-2$ cuts" is too generous —
  producing $F=\{v_1,v_2\}\cup P$ with $P$ nonempty and exactly-paired
  (required for $\ell(F)=2$ with $v_1+v_2<p_1$) costs $\ge3$ cuts on $p_1$
  (minimum piece count $2+2=4$ from $\{v_1,v_2\}$ plus one matched pair, so
  $\ge3$ cuts), leaving at most $n-3$, not $n-2$, for $R'$. **Reviewer
  independently re-derived this piece-counting argument from scratch (it
  is correct: producing $\ge4$ pieces from one stick requires $\ge3$ cuts)
  and independently re-verified, with a freshly written script (not the
  builder's), that (a) the claimed inequality $\Delta(n,v)\le v-f(n)$ has
  genuine counterexamples under the wrong $n-2$ cap at $n=3,4,5$ (own
  script found margins $-0.065,-0.029,-0.010$ respectively, matching the
  builder's independently) and (b) zero violations under the corrected
  $n-3$ cap for $n=3,\dots,6$ (own script, 3000 trials/$n$).** This
  correction is real, load-bearing, and now essential to Theorem 34's
  validity. Built on top of it, new **Theorem 35** closes target
  $(\Diamond)$ ($\Delta(n,v)\le v-f(n)$) **unconditionally for the "$p_3$
  untouched, $v<p_3$" sub-case (35a)** and **conditionally on
  $(\star_{n-3})$ for "$p_3$ untouched, $v\ge p_3$" (35b)** — reviewer
  hand-checked both proofs' algebra (Fact 1's alternating-sum
  nonnegativity, the doubling identity $p_2=2p_3$, and the cross-level
  scaling $D_{n-3}f(n-3)=2^{n-3}$) and found them correct. The "$p_3$ is
  cut" branch is honestly left fully open (not attempted), and the file
  explicitly flags an unclosed subtlety in the bridge from $\Delta(n,v)$
  back to the actual game quantity $A(F\cup G')$ when $\epsilon(v)=1$ (the
  odd-parity correction) — end-to-end correctness there is only
  numerically corroborated (4000 trials/$n$, zero violations), not proved
  algebraically. This is honestly reported, not glossed over, and matches
  reviewer's own reading of the gap. **New lemma certified: Truncated
  Alternating Sum Nonnegativity (Fact 1 of Theorem 35, reviewer-verified
  as an elementary, correct, standalone fact).**

  `minimax-lp-response-polytope` (new slug) proved a clean, general,
  non-numeric **Duality-Direction Impossibility Theorem**: LP weak duality
  is intrinsically one-directional (a dual-feasible point on the response
  polytope's constraints can only certify an upper bound on Xiang Yu's
  best achievable alternating-rank-sum, never the lower bound case (b2)'s
  upper-bound target actually needs), foreclosing constraint-side LP
  duality as a mechanism for case (b2) for every $n$ and marking
  simultaneously — a sixth confirmed-dead mechanism family, logically
  distinct from `convex-combination-futility-theorem` (which forecloses
  combining primal *values*, not constraint-side duals). **Reviewer
  independently re-derived the Weak Duality Theorem from scratch (the
  one-line proof is correct and standard) and confirms the corollary
  follows immediately** — case (b2) genuinely cannot be closed by any
  dual-feasible constraint-multiplier construction, this is not a
  witness-specific failure. Honest redirection: this machinery is
  well-typed for Claim (B)'s lower-bound residual instead, not attempted
  this round under this slug.

  `lp-duality-certificate` did consolidation/bookkeeping only this round:
  certified the surrogate/majorization mechanism as dead
  (`lemmas/surrogate-adversary-dead-end.md` — the ratio-2 ladder tail is
  not the true argmax tail, confirmed by differential-evolution search,
  drifting argmax ratio $\approx1.4$–$2.0$ across tested points, no
  low-dimensional closed form found) and itemized, case by case, that no
  prior certified closure implicitly assumed a fixed/ratio-2 worst tail —
  reviewer spot-checked this itemization against the cited proofs and
  found it accurate. No new positive coverage; no overclaim.

  `rank-pigeonhole-budget` (Claim (A) remains fully solved, unaffected;
  new work is an out-of-scope cross-check on the sibling's Claim-B
  target) proved a fully general **Truncated Alternating Sum Ceiling**
  ($A(S)-2A(S_{>v})\le v$ for any nonnegative multiset $S$, any $v\ge0$) —
  **reviewer independently re-derived and re-verified this from scratch
  (200,000 exact-`Fraction` trials, zero violations, equality attained
  exactly as claimed at $S=\{v\}$)** — and gave an unconditional,
  numerics-free proof that the corrected $n-3$ cap closes the residual
  middle band exactly at $n=3$ (where the cap forces $R'=\{p_3,p_4\}$ with
  zero adversarial freedom), via an exhaustive 3-case split on $v_2$
  vs.\ $p_3,p_4$. **Reviewer independently re-verified this case split by
  hand and by a fresh script, and found one minor, non-fatal boundary
  imprecision**: at the exact point $v_2=p_4$, the file's "$v_2\le p_4$"
  case computes $\tau_{>v_2}=\tau=\{p_3,p_4\}$ (both pieces "exceed"
  $v_2$), but at $v_2=p_4$ exactly, $p_4$ is not strictly greater than
  $v_2$, so $\tau_{>v_2}=\{p_3\}$ only, giving $\Delta=-3f(3)$, not the
  stated $-f(3)$. This does **not** break the theorem: the stated (wrong)
  value $-f(3)$ is *larger* than the true value $-3f(3)$, so proving the
  needed inequality for the (incorrectly computed) larger value is a
  strictly stronger — and still valid — claim than what the true value
  requires; the reviewer independently confirmed the true inequality holds
  at this boundary point too. The $n=3$ closure is genuine and rigorous,
  modulo this cosmetic fix the next round should make. General $n\ge4$ is
  honestly left open, re-encountering the standing cross-piece tie-vertex
  obstruction.

  **Net effect:** four genuinely new, correct results this round (a real
  bug fix with load-bearing consequences, a sixth mechanism ruled out for
  case (b2), a certified dead-end for the surrogate mechanism, and a
  rigorous $n=3$ base case for the middle band) — all independently
  re-verified by the reviewer with fresh scripts/hand computation, zero
  reviewer-found fatal errors (one cosmetic boundary imprecision, flagged
  above, does not affect any conclusion). Neither Claim (B)'s general
  middle band nor the general upper bound's case (b2) is closed. **Status
  remains `partial`** — the whole `imo-2026-03` problem (determine $c(n)$
  for all $n$, both directions) is not solved; only Claim (A) (a
  restricted lower-bound sub-case) and $n\le2$ in full are fully closed.

- **Round 20 (2 built slugs: `rank-pigeonhole-budget` — its own top-level
  target Claim (A) remains `solved`/APPROVE, unaffected; its round-20 §7.5
  contribution downgraded on review — and `greedy-halving-adversary`
  CHANGES REQUESTED. Reviewer independently re-derived every load-bearing
  claim from scratch with fresh scripts, not the builders' own.**

  `rank-pigeonhole-budget` fixed the round-19-flagged $v_2=p_4$ boundary
  bug in §7.5's $n=3$ middle-band closure (re-split as `v2≥p3`,
  `v2∈[p4,p3)` closed-left, `v2<p4`, matching the file's own strict-`>`
  convention). **Reviewer independently re-verified this narrow fix is
  correct**: the split is exhaustive/disjoint, and every one of the three
  case formulas (including the corrected value $\Delta(3,p_4)=-3f(3)$, not
  the old $-f(3)$) was re-derived by hand and confirmed by a fresh
  200,000-trial exact-`Fraction` script (zero violations). **However, the
  reviewer found a deeper, previously-uncaught gap**: the target $(\sharp)$
  this file works with, $\Delta(n,v_2)\le s-(v_1-v_2)$, is **not** the exact
  necessary-and-sufficient bridge to the true game quantity
  $A(F\cup G')\ge f(n)$ — re-deriving `greedy-halving-adversary`'s own exact
  bridge identity from scratch shows the correct target carries an extra
  $-2v_2\epsilon(v_2)$ term (exactly the sibling's own $(\Diamond')$ vs.
  $(\Diamond)$ distinction), which $(\sharp)$ omits. This is **not
  vacuous at $n=3$**: in §7.5's own "middle" sub-case $v_2\in[p_4,p_3)$,
  $|\tau_{>v_2}|=1$ is odd throughout, i.e. $\epsilon(v_2)=1$ on the *whole*
  sub-case, not isolated points. The reviewer independently checked (both
  by hand algebra and by a from-scratch end-to-end script constructing the
  actual game state $F=\{v_1,v_2,w,w\}$, $G'=\{p_3,p_4\}$ and computing
  $A(F\cup G')$ directly, ~122,000 trials restricted to this $\epsilon=1$
  zone) that the *true* target does hold there (zero violations, min margin
  ≈0.000136), but **§7.5's written proof does not establish this** — it
  proves the strictly weaker $(\sharp)$. **Net correction**: §7.5's
  "unconditional exact closure at $n=3$, no numerics needed" is downgraded
  to "closes $(\sharp)$ unconditionally (a real, correct, and useful
  narrowing); the true target's $\epsilon(v)=1$ instance — which is the
  entire middle sub-range at $n=3$ — is verified only numerically, the same
  honestly-flagged bridge gap the sibling reports for its own work, not
  previously caught in this file." This does not affect the file's own
  Status (`solved`, scoped to Claim (A), which §7 has never claimed to
  touch) — **Claim (A) remains fully closed, APPROVE stands.** New general
  lemma `truncated-alternating-sum-ceiling` (§7.1, re-verified round 19,
  reconfirmed here) remains certified.

  `greedy-halving-adversary` closed Theorem 35's "Case (b)" ($p_3$ is cut)
  branch at $n=3$ (vacuous — the corrected $n-3=0$ cut budget forbids
  splitting $p_3$ at all) and $n=4$ (new **Theorem 36**, unconditional,
  direct finite computation — budget $n-3=1$ forces $T'=\{p_4,p_5\}$
  untouched, leaving one free parameter $b$; two exhaustive sub-cases,
  five $v$-ranges each, all closed by exact algebra). **Reviewer
  independently re-derived the $n=3$ vacuity forcing from scratch (matches,
  and cross-consistent with the sibling's own independent $n=3$ forcing) and
  wrote a fresh, structurally independent verification script for $n=4$**:
  re-derived all ten closed-form sub-range formulas against direct
  sort-and-alternate computation (20,000 trials/sub-case, zero mismatches),
  confirmed the boundary tie $a=b=2u$ explicitly (exact equality at
  $v=2u$), and ran a separate fully-continuous 500,000-trial check (zero
  violations, min margin $\approx2.5\times10^{-6}>0$). **Theorem 36 is
  correct.** Combined with Theorem 35a (unconditional) and 35b (conditional
  on $(\star_1)$, itself unconditionally true), the target $(\Diamond)$
  (explicitly *not* the stronger $(\Diamond')$ — the file is consistently
  honest about this scoping throughout, no overclaim found) is fully closed
  at $n=4$. General $n\ge5$ remains open (Case (b)'s larger budget allows
  $T'$-cuts and multi-cut-on-$p_3$, neither reached this round), correctly
  and honestly scoped as such. **New lemma certified**:
  `theorem-36-case-b-n3-n4-closure` (scoped to $(\Diamond)$, not
  $(\Diamond')$, per the reviewer's cross-cutting finding below).

  **Cross-cutting finding (both fronts share one crux).** The
  reviewer's §1b discovery generalizes: `rank-pigeonhole-budget`'s
  $(\sharp)$ and `greedy-halving-adversary`'s $(\Diamond)$ are both the
  same $\epsilon=0$ special case of one exact bridge target
  $(\Diamond')$: $\Delta\le v-f(n)-2v\epsilon(v)$. Both siblings' $n=3$/$n=4$
  "closures" are numerically confirmed true end-to-end in the
  $\epsilon(v)=1$ zone but **not yet algebraically established** there —
  this is now the single, precisely-located remaining obstruction for the
  entire middle-band front at every level checked so far (not a vague
  residual; the $\epsilon=0$ special case is genuinely closed, mod the
  round-20 relabel fix, at $n=3,4$ on both fronts). **Next round should
  attack $(\Diamond')$'s $\epsilon=1$ case directly** (both files'
  $\epsilon=0$ machinery — Theorem 35a/35b/36, and §7.5's three-case split —
  are reusable building blocks for this, not to be re-derived), rather than
  re-deriving $(\sharp)$/$(\Diamond)$ again or advancing general-$n$ before
  this bridge is closed at the levels already reached.

  **Net effect.** One genuine bug found and fixed correctly (relabel), one
  deeper pre-existing gap uncovered (the $\epsilon$-bridge, now precisely
  named and shown non-vacuous even at already-"closed" levels), one new
  fully-verified unconditional theorem (Theorem 36, correctly scoped). No
  RETHINK — both approaches' core machinery remains sound and the newly
  found gap is a shared, well-defined next target, not a dead end. **Status
  remains `partial`.**

- **Round 22 (3 built slugs, all CHANGES REQUESTED, no RETHINK/APPROVE;
  reviewer independently re-derived/re-verified every load-bearing claim
  below with fresh scripts, not the builders' own — see
  `/tmp/round-22/proof-reviewer.md` for the full report). Note: this entry
  is appended chronologically after Round 20 (Round 21's own entry was
  misplaced earlier in this file, between Round 14 and Round 15 —
  a pre-existing formatting artifact, not a content error; not
  re-ordered here to keep this diff minimal).**

  `greedy-halving-adversary` proved five new pieces, all independently
  re-verified with no gaps found: the **General Cross-Level Rescaling
  Lemma** (a clean closed-form generalization of `tail-self-similarity`
  to any truncation depth $k$ — reviewer re-derived the algebra by hand
  and re-verified it exactly for $n=2,\dots,9$, all $k$, with a fresh
  script); **Theorem 36b** ($A(R')\ge f(n)$ for Theorem 35/36's whole
  object $R'$, uniformly across Case (a)/(b), conditional on
  $(\star_{n-2})$ — reviewer confirmed this correctly sidesteps the
  two-variable circularity Round 20 had ruled out, since it only invokes
  the one-variable hypothesis applied to the whole $R'$, and independently
  corroborated the conclusion numerically for $n=4,\dots,8$ with a
  freshly-written random-legal-refinement generator, margins matching the
  builder's own to the same order of magnitude); **Corollary 36c** (closes
  Case (b)'s $v\in(0,\min(R'))$ sub-range for every $n\ge5$ for the first
  time, conditionally — the first Case (b) coverage on record past $n=4$);
  the **Insert-Element Identity** (a genuinely general, non-ladder
  combinatorial identity, $A(\{b\}\cup T')=2A(T'_{>b})-A(T')+(-1)^jb$ —
  reviewer independently re-derived the proof and re-verified it with
  $20{,}000$ fresh exact-`Fraction` trials, zero mismatches, confirming it
  is a proved fact and not merely a numerically-corroborated conjecture),
  used to give a structural (not case-by-case) proof that Case (b)'s
  remaining "$v\ge a$" sub-range cannot be closed by any one-sided lower
  bound on $A(T')$ alone; and **Theorem 35b$'$** (closes "step 4" of the
  round-21 outline — the $\epsilon$-bridge on Theorem 35b's own range
  $v\ge p_3$ — by observing, correctly, that Theorem 35b's own proof
  already forces $R'_{>v}=\varnothing$ there, so $\epsilon\equiv0$ and
  $(\Diamond')$ collapses to the already-proved $(\Diamond)$ with zero new
  work; reviewer re-traced this line-by-line). No overclaiming found; Case
  (b)'s "$v\ge a$" endpoint and multi-cut-on-$p_3$ remain honestly open.
  **5 new lemmas certified**: `general-cross-level-rescaling-lemma`,
  `insert-element-identity`, `theorem-36b-whole-r-prime-lower-bound`
  (bundles Theorem 36b + Corollary 36c), `theorem-35b-prime-epsilon-
  vanishing`.

  `rank-pigeonhole-budget` proved, in §7.7, a genuine **biconditional**
  between its own target $(\sharp')$ (ranging over all admissible $v_1$ at
  fixed $v_2$) and the sibling's $(\Diamond')$ at that $v_2$, via the exact
  algebraic identity $\mathrm{marg}_{\sharp'}(v_1,v_2)=\mathrm{marg}_{
  \Diamond'}(v_2)+(p_2-v_1)$ (itself re-derived and confirmed correct by
  the reviewer): the easy ($\Leftarrow$) direction is immediate since
  $p_2-v_1>0$ throughout the domain; the substantive ($\Rightarrow$)
  direction is a genuine limit argument ($v_1\to p_2^-$) that the reviewer
  independently checked is valid (the right-hand side is affine in $v_1$
  with $\mathrm{marg}_{\Diamond'}(v_2)$ as its well-defined limit).
  Reviewer independently re-verified the identity itself with a fresh
  $50{,}000$-trial exact-`Fraction` script at $n=4$, zero mismatches. This
  is an honestly-scoped conditional corollary — it does **not** itself
  close $(\sharp')$, $(\Diamond')$, or §7.6's general-$n$ gap (both remain
  open pending the sibling's own extension past the $\epsilon=0$ case) —
  but it is a genuine, correctly-proved-both-directions equivalence, not a
  one-way sufficiency dressed up as more. No new standalone lemma
  certified this round (§7.7 is explicitly a conditional stub, not a
  closed result); Claim (A) remains `solved`/APPROVE, unaffected.

  `lp-duality-certificate` proved the **$p$-space Chamber-Vertex Theorem**
  (Lemma R22.1 + Theorem R22.2): for a full type with invertible $M(\tau)$,
  the chamber $U$ is a $p$-space polyhedron cut out by finitely many
  affine constraints, so $a_nT-\Phi_{\min}$ attains its minimum on any
  bounded slice at a vertex — reviewer independently confirmed the
  Minkowski–Weyl/convex-combination argument is sound and correctly scoped
  as conditional (invertibility, modulo R20.4's residual case, exactly as
  inherited from `within-chamber-affinity-theorem`). Also gave a genuine,
  correct fix for case (b2)'s strict-Box compactness worry via
  boundary-sharing with three adjacent regions, **and** an independently
  re-verified negative result (Target 2): the conjectured box-corner
  $\times$ tail-vertex dimension reduction is **false** — reviewer
  re-implemented the $n=3$ comparison from scratch with a differently
  parameterized optimizer and confirmed margin(unrestricted box)
  $\approx0.0205<$ margin(corner-restricted) $\approx0.0313$, matching the
  builder's numbers exactly, certified as the ninth confirmed-dead
  mechanism for case (b2). **However, the reviewer found a real overclaim**
  in the boundary-sharing Corollary (R22.2 / item 3 of
  `p-space-chamber-vertex-theorem`): it asserts all three Box walls are
  "already-unconditionally-closed" and that the fix is "unconditional and
  general... for every $n$" — but this directly contradicts the *same
  approach file's own* repeated, explicit record elsewhere (§4/"Round 9"):
  the $p_1\ge T/2$ regime is closed unconditionally **only for $n\le3$**
  (extending it needs the $p_1<T/2$ regime — case (b2) itself — closed one
  level down first), and case (a) $p_2\ge a_nT/2$ is explicitly labeled
  **"conditional, known"** elsewhere in the same file (it rests on the
  same standing strong-induction hypothesis as everything else in this
  project). Only the third wall (case (b1), $p_2\le T/D_n$, via the Max
  Domination Lemma) is genuinely unconditional for every $n$. This is a
  real citation-consistency bug (not a bug in the vertex theorem's own
  proof, items 1–2, which remain sound) — the Corollary, as stated for
  general $n$, is not actually established; it is only literally
  unconditional at $n\le3$, and conditional (on the same standing
  hypothesis) beyond that. **1 lemma certified with a correction note
  appended** (`p-space-chamber-vertex-theorem`, items 1–2 sound, item 3
  rescoped — not deleted, flagged for a round-23 fix), **1 lemma fully
  certified** (`box-corner-tail-vertex-decomposition-refuted`).

  **Net effect.** All three approaches made genuine, mostly correct,
  reviewer-verified progress this round; one real (non-fatal, easily
  fixed) citation-consistency overclaim was found and flagged in
  `lp-duality-certificate`'s new compactness-fix Corollary — a useful
  catch of exactly the "looks standard but has a subtle gap" pattern this
  project watches for, though here the gap is in cross-referencing the
  file's own prior results rather than in any new mathematics. No
  approach's own top-level target closes this round. **Status remains
  `partial`.**

- **Round 23 (3 built slugs, all CHANGES REQUESTED, none RETHINK/APPROVE;
  reviewer independently re-verified every new claim below with fresh
  exact-`Fraction` scripts and by-hand re-derivations, not the builders'
  own).**

  `greedy-halving-adversary` applied the certified Vertex-Minimum Theorem
  directly to the whole object $B=\{b\}\cup T'$ (Case (b)'s residual
  "$v\ge a$" branch) instead of decomposing through the Insert-Element
  Identity, and proved a new **Theorem 37**: the symmetric-split ($a=b=p_4$,
  forced by $p_3=2p_4$), $p_4$-untouched-by-$T'$ vertex satisfies
  $A(B)=A(T'')\ge f(n)$ via `pair-cancellation-identity` (two exact copies
  of $p_4$ cancel under odd-run reduction) plus the certified General
  Cross-Level Rescaling Lemma ($k=4$) and the standing hypothesis
  $(\star_{n-4})$ — unconditional whenever $n-4\le2$, i.e. $n\le6$ (since
  $(\star_1),(\star_2)$ are the only two full, unconditional $L(m)$
  closures on record; the round-23 "bundled audit" honestly confirms
  $(\star_3),(\star_4)$ are *not* yet certified unconditional, only
  numerically stress-tested, so Theorem 37 is genuinely conditional for
  $n\ge7$). **Reviewer independently re-verified Theorem 37** by writing a
  fresh exact-`Fraction` script generating legal budget-respecting
  refinements $T''$ of $\{p_5,\dots,p_{n+1}\}$ for $n=4,\dots,8$
  (3000 trials each): zero violations, with the bound exactly tight at
  $n=4,5,6,7$ — matching the theorem's own tightness claim at $n=5,6$ and
  extending the corroboration to $n=4,7,8$. This closes **exactly one
  member** of the vertex family for this branch — the file is explicit
  that it does not establish global minimality — and this reviewer
  confirms that scoping is accurate, not an overclaim. Separately, the
  file's **diagnostic finding** that the natural next vertex ($T'$ cuts
  $p_4$, $b$ tied to $T'$'s own top fragment) does not terminate is a real,
  traced structural argument (the pair-cancellation residual
  $\{c_2\}\cup(\text{rest})$ is not a rescaled ladder, since $c_2$ is an
  arbitrary fragment of $p_4$, not one of the ladder's own values — the
  same obstruction shape recurring one level down) — this reviewer
  independently re-traced the reduction and confirms it is a genuine
  diagnosis, not hand-waving disguised as one. The "bundled audit" of
  Theorems 33–36 at $n=3,4$ is honestly reported as incomplete (full case
  tree too large this round), with only the specific dependency chain
  Theorem 37 relies on re-derived (confirmed genuinely unconditional at
  $n\le6$) plus a fresh 200,000-trial stress test of the full undecomposed
  $L(3),L(4)$ (zero violations, correctly **not** claimed as a proof).
  **1 new lemma certified** (`Theorem 37`'s content is recorded in the
  approach file; no new standalone lemma file needed beyond the
  already-certified `pair-cancellation-identity` and
  `general-cross-level-rescaling-lemma` it composes).

  `rank-pigeonhole-budget` (Claim (A) remains `solved`/APPROVE, untouched
  by this addendum) independently attacked the identical target
  ($A(B)\ge f(n)$ for $B=\{b\}\cup T'$) via its own discrete/pigeonhole
  toolbox rather than the sibling's whole-object Vertex-Minimum Theorem
  application, per the round-3 precedent of independent re-derivation. New
  **Single-Insert-Point Vertex Lemma** (promoted to
  `lemmas/single-insert-point-vertex-lemma.md`): for any finite multiset
  $T$ and box $[0,M]$, $g(b):=A(\{b\}\cup T)$ is piecewise affine with
  slope $\pm1$ (never $0$) between consecutive breakpoints
  $\{0,M\}\cup(T\cap[0,M])$ — a self-contained one-line slope argument, no
  appeal to the general LP/compactness Vertex-Minimum Theorem anywhere in
  its proof, confirming genuine independence from the sibling's route.
  **Reviewer independently re-verified this lemma** with a fresh
  2000-trial exact-`Fraction` script (random $T$, random box $M$, dense
  interior sampling vs. breakpoint minimum): zero violations, confirming
  both the slope-$\pm1$ claim and the no-flat-interval claim. Applying the
  lemma pins $b$ to exactly 3 candidate types; **Step 2** ($b=0$) closes
  conditional on $(\star_{n-3})$ via the same rescaling-plus-induction
  mechanism (unconditional for $n\le5$); **Step 3** ($b=p_4$,
  $p_4$-untouched) closes conditional on $(\star_{n-4})$ — an independent
  derivation of literally the same content as the sibling's Theorem 37,
  reached from a genuinely different starting point (single-variable
  pinning first, vs. the sibling's whole-polytope application of the
  general theorem) — a valuable, non-circular cross-check, not a
  restatement. The 2 residual sub-cases (further-split $p_4$, or a tie
  with a generic interior $T'$-fragment) are honestly reported as
  recoupling to the same open cross-piece vertex-enumeration obstruction,
  matching the sibling's own diagnosis rather than escaping it.

  `lp-duality-certificate` completed the promised round-23 scope
  correction to `lemmas/p-space-chamber-vertex-theorem.md`'s item 3
  (the round-22-flagged overclaim): the corrected text now states
  precisely which of the three Box walls are unconditional (only $p_2\le
  T/D_n$, for every $n$) versus scoped to $n\le3$ ($p_1\ge T/2$) versus
  conditional on the standing induction hypothesis (case (a)). **Reviewer
  independently re-read both the restated item 3 and the "Honest scope"
  section and confirms they are now mutually consistent, with no residual
  overclaim standing anywhere in the current file text** — the round-22
  correction note is properly folded into the main statement rather than
  left as a contradicting appendix. New methodological finding
  (`feasibility-suffices-for-upper-bound`): proving the one-sided bound
  $\Phi_{\min}(p)\le a_nT(p)$ only needs a type to be *feasible* (satisfy
  conditions (a)+(b)), not the actual global minimizer (condition (c)) —
  reviewer confirms this is a correct, immediate consequence of the
  Chamber-Vertex Theorem's own proof (the ($\Leftarrow$) direction of Lemma
  R22.1 never uses (c)), reducing case (b2)'s closure to exhibiting a
  finite *covering* family of feasibility regions rather than a full
  type-competition enumeration — a genuine simplification, not a closure.
  New exact chamber **Chamber A2** (composition $(2,0,0,0)$, $p_1$ split as
  $(v,w,w)$ with $v$ pinned to the untouched $p_2$, $w=(p_1-p_2)/2$ tied to
  itself): closed form $\Phi_{A2}=(p_1+p_2)/2+p_3$ on wall $p_1\le
  p_2+2p_4$. **Reviewer independently re-derived this formula by hand**
  from the sorted-rank assignment (the tied pair $\{p_2,v\}$ occupies ranks
  1–2, not 2 and 4 as an earlier in-round draft mistakenly had it — the
  file's own self-correction, confirmed correct by this reviewer) and
  hand-verified the reported worst vertex $p=(2/5,4/15,4/15,1/15)$ exactly
  ($w=p_4=1/15$, $\Phi_{A2}=3/5$, $g_{A2}=8/15-9/15=-1/15$, matching the
  file's corrected LP run after its own self-caught wall-encoding bug).
  Case (b2) at $n=3$ is honestly **not closed** this round: a genuine new
  structural finding (one composition, $(2,0,0,0)$, hosts $\ge2$ distinct
  optimal types in different sub-regions — Chamber A and Chamber A2 — and
  neither chamber's own naive feasibility region is individually a
  sufficient cover) revises the expected chamber count upward and confirms
  the covering-family target is a genuine combinatorial task, not a
  small-patch fix. **2 new lemmas certified this round**
  (`chamber-a2-p1-tied-to-p2-pair`, `feasibility-suffices-for-upper-
  bound` — both written to `lemmas/` by this reviewer, having been
  described as "certified"/"promotable" in the approach file but not yet
  present as standalone lemma files).

  **Net effect.** All three approaches made genuine, independently
  re-verified, honestly-scoped progress this round — including two
  genuinely independent derivations (Vertex-Minimum-Theorem-first vs.
  single-variable-pinning-first) converging on the identical partial
  closure of Case (b)'s "$v\ge a$" branch, and a properly-resolved
  scope-correction with no residual overclaim in
  `lp-duality-certificate`. No approach's own top-level target (Claim (B)
  in general, the general upper bound) closes this round. **Status remains
  `partial`.**

- **Round 24 (3 built slugs, all CHANGES REQUESTED, no RETHINK/APPROVE;
  reviewer independently re-derived/re-verified every new claim below with
  fresh exact-`Fraction` scripts of its own).**

  `greedy-halving-adversary` attacked round 23's own diagnostic residual
  (the "$T'$-cuts-$p_4$" sub-case of Case (b)'s "$v\ge a$" branch) by
  recasting it as a standalone induction target $h(m)$. **New Theorem 38**
  proves $h(1)=f(1)$ **exactly, with a genuinely exhaustive case analysis**
  (verified independently by hand: at $m=1$ the tail budget forces $S$
  untouched, so $A(c)$ is a fully explicit 2-piece function of $c$ whose
  minimum, checked over its whole domain, is exactly $1$ at both
  endpoints) — this piece is correct and certified
  (`lemmas/theorem-38-h1-exhaustive-closure.md`). **However, the file's
  own "Open gaps" summary overclaims**: it states that combining Theorem
  38's $m=1$ corollary with round 23's Theorem 37 "fully, unconditionally
  closes" Case (b)'s **whole** "$v\ge a$" branch at $n=5$. This does not
  follow as written: Theorem 37 itself explicitly states (its own "Scope"
  paragraph, unchanged since round 23) that it establishes only **one**
  vertex of the "$T'$-leaves-$p_4$-untouched" family (the symmetric-split
  tie $b=p_4=\max(T')$) and does **not** rule out the joint
  $(b,T')$-minimizer instead having $b$ tied to a **non-maximal** element
  of $T'$ (e.g. a fragment produced when $T'$ splits $p_5$ or $p_6$
  instead of $p_4$) — exactly the "deeper-tie beats the top-tie" failure
  mode Theorem 38's **own** new numeric finding this round shows is real
  (a $3000$-trial search found deeper ties beating the base trio in
  $\approx46\%$ of arbitrary-reference-multiset trials, and in
  $\approx3.7\%$ of genuine legal-ladder-refinement trials at
  $m=2,\dots,5$). No argument on file rules this vertex type out for
  Theorem 37's own domain. The proof-reviewer independently stress-tested
  $n=5$ directly (two independent scripts, $200{,}000+$ random trials
  each, deliberately including $b$ tied to non-maximal $T'$-fragments)
  and found **zero violations** of $A(B)\ge f(5)$ — so the underlying
  claim is very likely true — but this corroborates the *result*, not the
  *written proof*, which has a genuine unaddressed case. **Verdict: the
  "$n=5$ full branch closure" claim is downgraded to unproved (numerically
  supported); Theorem 38's own $h(1)=f(1)$ result stands, certified.**
  The $m=2$ partial extension (one of three cut-branches closed by hand)
  and general $m\ge3$ are honestly left open, as reported.

  `lp-duality-certificate` derived, from scratch (not curve-fit to
  numerics), **6 new exact chambers**: Double-Sandwich-Below/Above (exact
  closed forms **and** exact two-sided feasibility regions — reviewer
  independently re-verified both with a fresh $20{,}000$-trial
  exact-`Fraction` script, zero mismatches), the general **Bisect-Subset
  Lemma** (strictly generalizes the certified `bisect-top-k-lemma` to
  arbitrary subsets, unconditional, reviewer-confirmed as a direct,
  non-curve-fit corollary of `cross-piece-sign-assignment-identity`),
  Triple-Pin, Chamber B1/B2 (completing round 23's half-finished Chamber
  B), and P1P2-tied-to-$p_3$ — reviewer independently re-verified all
  three of these too (after catching and fixing one bug in its own
  first-draft verification script for Chamber B1/B2 — the reviewer's
  script, not the proof, initially dropped the untouched copy of $p_2$;
  once fixed, $14{,}932$ in-region trials, zero mismatches). Assembled
  into a 20-member covering family tested on a $1577$-point deterministic
  grid and a $3351$-point random sample at $n=3$ case (b2): **zero
  uncovered points in either test.** Per the file's own honest, correctly
  self-scoped report (and confirmed by the reviewer — no overclaim
  found), this is strong sampling evidence but **not** a proof of
  exhaustive coverage — no finite-vertex/case-split argument establishing
  the family is a complete cover has been written. **Status for this
  target correctly remains unproved**, not solved.

  `rank-pigeonhole-budget` fixed the round-24 outline-reviewer's flagged
  direction bug via a careful breakpoint-by-breakpoint re-derivation
  (§7.9) of the "$T'$-cuts-$p_4$" sub-case's four candidate vertex types
  for $b$: $b=0$ (already closed via $(\star_{n-3})$), $b=p_4$ (shown, via
  a new general **Box-Endpoint Domination Fact**, to need no bound in
  either direction — reviewer independently re-derived this one-line
  affine-slope fact from scratch and confirms it, certified
  `lemmas/box-endpoint-domination-fact.md`), $b=c_1$ (a same-direction
  recursion, not the flagged bug), and $b=c_2$ (**the one genuine
  instance** of the flagged direction issue, reducing to a precise new
  inequality (7.9.1): $A(T''')\le c_1-f(n)$). The file **proves, by exact
  algebra, that (7.9.1) does NOT follow** from the certified cheap bound
  $A\le\mathrm{Total}$ (a concrete symbolic counterexample at the
  symmetric split, reviewer independently re-derived the same conclusion)
  and does not construct a proof of (7.9.1) itself — correctly left open,
  not closed. **Status-field note (no fix needed):** this approach's own
  file header says "Status: solved", but its own scope note explicitly
  and correctly restricts this to Claim (A) alone (proved complete since
  round 8), not the $T'$-cuts-$p_4$ addendum or the whole problem;
  `current.md`'s own top-level Status has already read `partial`
  throughout, so no correction was needed there.

  **Net effect.** Two genuine new certified lemmas/chamber families
  (`box-endpoint-domination-fact`, the six new `lp-duality-certificate`
  chambers, `theorem-38-h1-exhaustive-closure` restricted to its true
  $m=1$ scope) and one important downgrade (the claimed "$n=5$ full
  branch closure" is not yet established as written, though numerically
  very likely true) — a genuine adversarial catch, not a rubber stamp.
  **Status remains `partial`.**

- **Round 25 (3 built slugs, all CHANGES REQUESTED, no RETHINK/APPROVE;
  reviewer independently re-derived/re-verified every new claim below with
  fresh exact-arithmetic scripts of its own — Fraction/sympy.Rational, not
  the builders' own).**

  `greedy-halving-adversary` delivered two genuine, verified results:
  **Proposition 39** (Mass-Conservation Obstruction) rigorously *proves*
  (not merely re-asserts) that the outline's proposed "$h(m)$ as a
  disguised corollary of $(\star_{n-4})$ via literal substitution"
  shortcut is false, for a precise structural reason (an injectivity
  argument on total mass) — a clean, correct negative result, closing off
  the idea permanently. **Theorem 39** fully and unconditionally closes
  $h(2)\ge f(2)$ (the two remaining $q_2$-split and $q_3$-split branches
  of $m=2$, left open in round 24), extending the "$T'$-cuts-$p_4$"
  sub-case's closure from $n=5$ to $n=6$ — this reviewer independently
  re-derived every piecewise closed form and stress-tested them with
  $6000+$ fresh dense random exact-`Fraction` samples plus a $40{,}000$-
  trial randomized search (`/tmp/round-25/verify_theorem39.py`), zero
  mismatches; unlike Theorem 37, Theorem 39's technique is a *full
  continuum sweep* over $c$ (not a vertex-restricted argument), so it is
  not vulnerable to the "deep-tie" gap that affects Theorem 37. **However,
  the approach file's own "Open gaps" summary repeats an overclaim already
  flagged and downgraded in round 24**: it states that combining Theorem
  39 with Theorem 37 "fully, unconditionally closes" Case (b)'s *whole*
  "$v\ge a$" branch at $n=6$ (and restates the identical $n=5$ overclaim).
  This does not follow: Theorem 37 itself (covering the complementary
  "$T'$-untouched" sub-case) still has its own acknowledged,
  **unaddressed** gap — it establishes only one vertex ($b=p_4$ symmetric
  split) and does not rule out $b$ tied to a non-maximal element of
  $T''$ being the true global minimizer there — and this round's work did
  not touch that gap. **Verdict: Theorem 39/Proposition 39 certified
  (scoped precisely to the "$T'$-cuts-$p_4$" sub-case only); the "whole
  $v\ge a$ branch closed at $n=5/n=6$" claim is downgraded to unproved**,
  exactly as round 24 already established for $n=5$ — this round's
  extension to $n=6$ inherits the identical gap, uncorrected.

  `lp-duality-certificate` produced this round's highest-stakes and, on
  its own precise scope, **correct and fully verified** result: a genuine
  exact-arithmetic (Farkas-certificate) proof that the 5-chamber family
  covers case (b2)'s entire box at $n=3$ — reviewer independently
  re-derived all five chambers' failure/feasibility inequalities via
  `sympy.Rational` symbolic algebra, re-verified all six Farkas
  certificates from scratch (`/tmp/round-25/verify_farkas.py`, all six
  confirmed: LHS cancels to $0$, RHS sums to $0$, at least one strict
  constraint weighted positively in each), and cross-checked with
  $23{,}880$ fresh independent random exact-`Fraction` samples in the
  open box (zero uncovered points) plus a direct check of the boundary
  vertex $p^\ast=(2/5,4/15,1/5,2/15)$ (confirmed $g_{R22}(p^\ast)=0$
  exactly, so no separate disposal step is needed). **This is genuine,
  certifiable progress — `case-b2-n3-covering-closure`.** **However, the
  file's top-level claim ("this completes the general upper bound
  $c(3)\le8/15$ for every legal marking at $n=3$... Status upgraded to
  `solved` for the $n=3$ scope") is a real overclaim, not just an
  imprecise phrasing.** The file's own final combination cites only
  "case (a) ($p_1\ge T/2$)" and "case (b1) ($p_2\le T/D_3$)" alongside
  this round's case (b2) closure — but the file's own EARLIER text
  (twice, independently) defines "case (a)" as a genuinely **different**
  region, $p_2\ge a_3T/2$ *with* $p_1<T/2$ (distinct from $p_1\ge T/2$),
  closed via a separate mechanism (`generalized-peel-identity`/Theorem
  B$_k$, conditional on the already-closed $c(2)=4/7$). This region is
  neither cited nor re-verified in round 25's final combination. This
  reviewer confirmed by a fresh $500{,}000$-trial random search that the
  5-chamber family does **not**, on its own, cover this region (many
  violating witnesses found, e.g. near $(0.45,0.30,0.15,0.10)T$) — so as
  *written*, R25.1's proof does not establish the full $n=3$ upper bound.
  Separately, this reviewer spot-checked that the missing region is
  almost certainly still true and provable (Theorem B$_k$ with $k=2$,
  using the already-fully-closed $c(2)=4/7$ bound for the reduced tail,
  gives $\Phi\le8/15\cdot T$ at the specific witness checked) — so the
  underlying mathematical claim is very likely correct, but the round's
  write-up did not actually assemble/cite it. **Verdict: case (b2)'s own
  covering closure certified in full; the file's "n=3 fully solved"
  claim is downgraded — `current.md`'s Status remains `partial`, not
  advanced to a per-$n$ "solved" for $n=3$, pending an explicit citation
  fix (re-invoke `generalized-peel-identity`/Theorem B$_k$ for the
  $p_2\ge a_3T/2$, $p_1<T/2$ region) next round.**

  `rank-pigeonhole-budget` made real, honestly-scoped progress on
  (7.9.1): found the outline's proposed Restriction Lemma does not
  literally apply (a 1-dimensional "vary one already-fixed element"
  polytope cannot itself decide *which* tail element is cut), and
  replaced it with a from-scratch **MinFloor$(\ell)$/MaxCeil$(\ell)$
  joint reduction** — (7.9.1) is shown exactly equivalent to
  MaxCeil$(m)$, $m=n-3$ (equivalently $E(S)\ge\sigma_1/2$); MaxCeil's
  "top element untouched" branch reduces exactly to MinFloor$(\ell-1)$;
  and MinFloor's own "top element untouched" branch is closed
  **unconditionally for every $\ell\ge1$** via one clean line (the
  already-certified Fact 2 plus the identity $R(\sigma)+\sigma_\ell=
  2\sigma_1$) — a new, general, reusable partial result. This reviewer
  spot-checked the identity $R(\sigma)+\sigma_\ell=2\sigma_1$ (trivial
  geometric-series algebra, confirmed exactly), the Fact-2 argument, and
  the $\ell\le3$ hand computations — all correct. Both quantities' "top
  element is cut" branches are honestly left **open** for general
  $\ell$, matched by the file's own Status/scope text (header "solved"
  correctly and consistently scoped to Claim (A) only, unchanged since
  round 8 — no overclaim found anywhere in this file this round).
  **Verdict: genuine partial progress, correctly self-reported; (7.9.1)
  remains open.**

  **Net effect.** Two genuinely new, independently-certified lemmas
  (`theorem-39-h2-closure`, `proposition-39-mass-conservation-
  obstruction`) and one major new exact-arithmetic closure
  (`case-b2-n3-covering-closure`, scoped to case (b2)'s box at $n=3$ —
  itself a real milestone: the first fully rigorous, non-numeric closure
  of any $n=3$ sub-case's coverage-family problem on file) — but **two
  of the three approaches this round overclaimed their own combined
  conclusions** (both by omitting/conflating a sibling region's own
  still-needed citation, a genuinely different failure mode from a
  computational error): `greedy-halving-adversary` restated round 24's
  already-flagged "whole branch closed" overclaim one level further
  ($n=6$), and `lp-duality-certificate` introduced a new instance of the
  same failure mode (a missing/mislabeled region in its own final
  combination) while producing this round's strongest genuinely new
  result. Neither the general upper bound nor the general lower bound is
  established; the whole problem remains **`partial`**. **Recommend next
  round: (1) `lp-duality-certificate` fix the case(a)/case(b1)/case(b2)
  citation and explicitly re-verify the $p_2\ge a_3T/2$, $p_1<T/2$ region
  via `generalized-peel-identity` to genuinely complete $n=3$'s upper
  bound; (2) `greedy-halving-adversary` address Theorem 37's own
  non-maximal-tie gap (the actual remaining item for the "$v\ge a$"
  branch, distinct from the now-closed "$T'$-cuts-$p_4$" sub-case) before
  claiming any "whole branch closed" result again.**

- **Round 26 (3 built slugs; 1 verified-milestone / APPROVE
  (`rank-pigeonhole-budget`), 2 CHANGES REQUESTED (`lp-duality-certificate`,
  `greedy-halving-adversary`); reviewer independently re-derived every new
  claim below from scratch — index arithmetic, shape enumeration, Farkas
  certificates, and a fresh counterexample — not the builders' own scripts.**

  `rank-pigeonhole-budget` delivered this round's genuine, clean milestone.
  New §7.11 proves the **Index-Chain Identity**
  $\mathrm{MinFloor}(\ell)\equiv(\star_{\ell-1})$ via an explicit rescaling
  bijection; this reviewer independently re-derived both sides' exact
  statements (not just copied the file's), checked the bijection by hand at
  $\ell=2,3$, and cross-checked the length/budget convention against its
  prior use in §7.8 — no off-by-one, confirmed correct. New §7.12/§7.13
  then close $\mathrm{MaxCeil}(3)$ ($n=6$) and, more substantially,
  $\mathrm{MaxCeil}(4)$ ($n=7$) **fully, both branches, unconditionally**,
  via a genuine 5-shape cut-distribution enumeration (NOT the previously-
  flagged-insufficient Triangle-Bound shortcut) — this reviewer
  independently re-enumerated all cut-distribution tuples
  $(c_1,c_2,c_3,c_4)$ with $c_1\ge1,\ \sum c_i\le2$ from the stated rule and
  got exactly the same 5 shapes (no missing/duplicate shape), then
  recomputed each shape's bound by hand from the ladder $\sigma=(8,4,2,1)$,
  confirming $A\le7$ in every shape with the supremum $7$ genuinely attained
  in the limit. **This is the first fully-general, non-numeric closure of
  $\mathrm{MaxCeil}$ at $\ell=4$ ($n=7$) on file.** One minor cosmetic note
  (the triple-tie boundary at $a=4$ deserved a fuller write-up) does not
  affect correctness. **Verdict: APPROVE** — genuine progress, no gap found;
  general $\ell\ge5$ ($n\ge8$) remains open, honestly scoped as such.

  `lp-duality-certificate` fixed round 25's citation bug correctly (R26.1:
  case (a), $p_2\ge4T/15$, is genuinely closed by the Corollary to Theorem B
  with its hypothesis discharged, unconditionally and without any
  sortedness assumption, by the certified general
  `n2-upper-bound-lp-argument` — this reviewer re-derived the threshold
  algebra $a_3T/2=4T/15$ by hand and confirms the fix is real, not
  cosmetic) and the resulting three-way $p_2$-partition (b1)/(b2)/(a) is
  genuinely exhaustive and non-overlapping at both boundaries (R26.2,
  independently re-checked). **However, the round's "bonus" claim — that
  `case-b2-n3-covering-closure`'s domain can be widened to drop the
  $p_1<T/2$ restriction "for free," since none of the six Farkas
  certificates literally sum that hypothesis — is false as stated.** The
  Triple-Pin chamber's closed form $\Phi_{\text{TriplePin}}=T-p_1$ was
  itself derived (§R24.3) using $p_1<T/2$ to pin the order $v_3<p_4$; for
  $p_1\ge T/2$ this order can flip, and the true value there is
  $\Phi_{\text{TriplePin}}=\max(p_1,T-p_1)$, not $T-p_1$. This reviewer
  found and hand-verified a concrete counterexample in the widened region:
  $p=(3/5,\,9/40,\,29/200,\,3/100)$ (exact rationals, $T=1$, sorted,
  $p_1=3/5\ge T/2$, $p_2=9/40\in(T/15,4T/15)$) — recomputing all five
  chambers correctly, **all five fail or are infeasible** at this point
  (Bisect$\{1,4\}$, Bisect$\{1,2\}$, DS-Above all give $g_\tau<0$;
  Triple-Pin's corrected value gives $g_{\text{TP}}=8/15-3/5=-1/15<0$;
  R22.1.1 is infeasible since $p_2>p_3+p_4$). So the round-26 "bonus"
  widening does not hold, and consequently **R26.3's headline claim — a
  complete non-ladder-restricted proof of $c(3)\le8/15$ for every legal
  marking at $n=3$ — is not established**: the corner $p_1\ge T/2$,
  $T/15<p_2<4T/15$ is genuinely uncovered by the file's own mechanisms as
  written (the true minimum there may still be $\le8/15$ via some other
  strategy, but no proof of that is on file). **Verdict: CHANGES
  REQUESTED** — the citation fix (R26.1) and partition (R26.2) stand and
  are reusable, but the domain-widening bonus must be reverted (restore
  `case-b2-n3-covering-closure`'s $p_1<T/2$ hypothesis) and a genuinely new
  mechanism found for the $p_1\ge T/2$, $T/15<p_2<4T/15$ corner before the
  general-marking $n=3$ upper bound can be called complete.

  `greedy-halving-adversary` delivered a sound new result, **Theorem 40
  (Anchored Single-Tie Deletion Bound)**, closing the ODD-multiplicity-tie
  sub-case of Theorem 37's own non-maximal-tie gap, unconditionally for
  $n\ge5$, no induction — this reviewer independently re-checked the proof
  chain (`odd-run-reduction-lemma` + `sharp-dominant-removal-identity` +
  the trivial $A\le\mathrm{Total}$ bound + the ladder's telescoping mass
  identity) step by step: no hidden case, no hidden small-$n$ base case
  smuggled in, and the domination hypothesis $w>\max(X)$ it needs is
  genuinely automatic from the ladder's own doubling
  ($p_4=2p_5\ge2\max(X)$), not an extra unverified assumption. The
  even-multiplicity sub-case is honestly left open (correctly diagnosed as
  needing the project's central, still-missing upper bound), and the new
  Theorem 40 material itself is scrupulously scoped — every occurrence in
  the round-26 text explicitly says it closes only the odd-multiplicity
  tie vertex within Theorem 37's branch, not the whole "$v\ge a$" branch.
  **But the 3-round-running overclaim pattern is still not fully purged
  from the file**: immediately below this round's own correctly-scoped
  note ("Case (b)'s '$v\ge a$' branch as a whole remains open"), the
  **uncorrected round-24/25 status text still states** "Combined with
  Theorem 37 ..., Case (b)'s whole '$v\ge a$' branch is now fully,
  unconditionally closed at $n=5$" and, separately, "... at $n=6$ as well
  as $n=5$" — both false as stated (Theorem 37's own non-maximal-tie gap,
  even after Theorem 40, is only half-closed: odd-multiplicity yes,
  even-multiplicity no), and left standing in the file even though the
  round-26 outline itself explicitly warned against repeating exactly this
  pattern. **Verdict: CHANGES REQUESTED** — Theorem 40 is certified and
  reusable, but the stale round-24/25 "branch fully closed at $n=5/n=6$"
  lines must be struck or corrected before this file is clean.

  **Net effect.** One genuine, clean new milestone
  (`maxceil-4-full-closure`/index-chain identity, $\mathrm{MaxCeil}$ closed
  through $\ell=4$, $n=7$, both branches) and two real new lemmas/results
  that are certified in substance but whose host files each still contain
  one uncorrected defect: `lp-duality-certificate`'s general-marking $n=3$
  upper bound has a genuine remaining gap (the widened case (b2) does not
  actually cover $p_1\ge T/2$), and `greedy-halving-adversary` still carries
  stale round-24/25 overclaim text alongside this round's own honestly-
  scoped Theorem 40. Neither the general upper bound (any $n\ge4$) nor the
  general lower bound (any $c\ge1$ beyond the cases already closed) is
  established; the whole problem remains **`partial`**. **Recommend next
  round:** (1) `lp-duality-certificate` revert the case-(b2) domain
  widening (restore $p_1<T/2$) and open a genuinely new chamber/mechanism
  for $p_1\ge T/2,\ T/15<p_2<4T/15$; (2) `greedy-halving-adversary` strike
  or correct the stale "$v\ge a$ branch fully closed at $n=5/n=6$" lines
  (rounds 24/25) so the file no longer contradicts its own round-26
  diagnosis, and continue toward the even-multiplicity sub-case (the
  project's central obstruction); (3) `rank-pigeonhole-budget` push
  $\mathrm{MaxCeil}/\mathrm{MinFloor}$ past $\ell=4$ toward the still-open
  $(\star_k)$, $k\ge3$.**

- **Round 27 (3 built slugs: 1 APPROVE at own scope [`lp-duality-certificate`,
  the $n=3$ general-marking upper bound], 2 CHANGES REQUESTED, no RETHINK).**
  All three round-26 recommendations were attacked and each made genuine
  progress, but one new overclaim was found and corrected in-round.

  **`lp-duality-certificate`: MILESTONE — the general-marking $n=3$ upper
  bound $c(3)\le8/15$ is now fully, rigorously proved, no numerics
  load-bearing.** New **Gap-Filler four-chamber family** (Bisect$\{1,4\}$,
  Bisect$\{1,2\}$, Bisect$\{1,2,3\}$, Bisect1+Pin2to3), each chamber's
  closed form derived via a new, elementary, fully general **Pair-
  Insensitivity Corollary** of `odd-run-reduction-lemma`
  ($A(M\cup\{v,v\})=A(M)$ for any $M,v$ — a two-line parity argument, no
  genericity assumption), then two explicit Farkas-style nonnegative-
  combination certificates proving the four chambers jointly cover the
  exact residual region left open by rounds 24–26
  ($p_1\ge T/2,\ T/15<p_2<4T/15$). **This reviewer independently
  re-derived every piece from scratch**: re-derived both Farkas
  certificates by hand (Case (i)'s combination expands identically to
  $0$; Case (ii)'s expands identically to $-1.5u<0$ — both re-checked
  termwise), re-verified all four chamber formulas and the covering
  property with a fresh, independently-written script
  (28,699 exact-`Fraction` trials landing in the exact residual region,
  zero formula mismatches, zero coverage violations), and confirmed the
  new family resolves the specific witness
  $p=(3/5,9/40,29/200,3/100)$ that broke round 26's rejected "bonus"
  widening attempt (Chamber C succeeds there, $z\le u$). Also independently
  re-checked that case (a)'s citation (round 26's fix: peel $p_2$ via
  Theorem B, discharge the reduced 3-element instance via
  `n2-upper-bound-lp-argument`) genuinely imposes no restriction on $p_1$,
  and that the resulting four-regime case split — (b1) $p_2\le T/15$; (a)
  $p_2\ge4T/15$; middle strip $p_1<T/2$ (5-chamber family); middle strip
  $p_1\ge T/2$ (this round's 4-chamber family) — is exhaustive and
  non-overlapping. **No gap found. This closes a genuine sub-milestone:
  the $n=3$ upper-bound direction $c(3)\le8/15$ is fully solved for every
  legal marking** (the lower-bound/achievability direction at $n=3$, and
  the general upper bound for $n\ge4$, remain open and are not claimed
  here). 3 new lemmas certified (`pair-insensitivity-corollary`,
  `gap-filler-four-chamber-covering`).

  **`greedy-halving-adversary`: real, verified new theorem, but the file's
  own combination claim overclaimed and was corrected by this reviewer.**
  New **Theorem 41 (Even-Multiplicity Non-Maximal-Tie Closure)** closes
  the complementary half of round 26's Theorem 40 — via a sharper
  rank-split-at-$t^\ast$ decomposition (apply `insert-element-identity`
  exactly, then bound the two resulting halves $H,L$ *separately* by
  trivial per-piece bounds, rather than bounding $T''$ as one lump) —
  proving $A(B)\ge f(n)+t^\ast>f(n)$ unconditionally for every $n\ge5$,
  every legal $T''$, every even multiplicity $\mu\ge2$. **This reviewer
  independently re-derived the entire five-step chain by hand** (Rank-
  Split Formula, odd-run collapse of the even-multiplicity block, the
  Insert-Element-Identity substitution, the ladder mass identity, the two
  trivial per-piece bounds) and re-verified with a fresh, independently
  written exact-`Fraction` script (20,000 trials constructing genuine
  ladder tails with engineered even-multiplicity ties, zero violations) —
  Theorem 41 itself is correct and unconditional, exactly as claimed.
  **However, the file's own "Corollary" combining Theorem 41 with Theorem
  40 and Theorem 37 to claim the whole "$T'$-untouched" branch is now
  "closed unconditionally, for every $n\ge5$" is an overclaim**: Theorem
  37 (the pre-existing symmetric vertex $b=p_4$) is, by its own stated
  scope (unchanged this round), proved unconditionally only for $n\le6$
  and conditional on $(\star_{n-4})$ for $n\ge7$ — this round's work does
  not remove that conditionality, only the non-maximal-tie residual around
  it. **Reviewer corrected this in three places in the approach file**
  (top summary, the Corollary itself, the "Round 27 status" Open-gaps
  entry): the true, corrected statement is that the non-maximal-tie
  residual (odd- and even-multiplicity) is fully closed unconditionally
  for every $n\ge5$, but the "$T'$-untouched" branch **as a whole**
  (including Theorem 37's own vertex) is unconditionally closed only for
  $n\le6$, remaining conditional on $(\star_{n-4})$ for $n\ge7$ exactly as
  before. This is the same overclaim *pattern* flagged in rounds 24–26
  (combining a newly-closed piece with an older, more narrowly-scoped
  sibling result and dropping the sibling's own caveat) recurring in a new
  form; Theorem 41 itself is genuine, certified progress. 1 new lemma
  certified (`even-multiplicity-non-maximal-tie-closure`).

  **`rank-pigeonhole-budget`: genuine general-$m$ theorem plus an honest,
  rigorous Necessity finding correcting the outline's premise.** New
  **§7.14 ($\sigma_2$-Untouched Closure Theorem)**: for every $m\ge2$ and
  every legal top-cut shape with $\sigma_2$ untouched (no restriction on
  cut count anywhere else), $A(S)\le\sigma_1-\sigma_m$ — a fully general,
  budget-free theorem strictly generalizing 4 of the 5 shapes closed by
  hand at $m=4$ (round 26) to arbitrary $m$, via the same two-peel-plus-
  Fact-2 mechanism with no induction on $m$ and no shape enumeration. This
  reviewer independently re-derived both case branches (odd/even tied
  multiplicity at $\sigma_2$; the two-peel argument when $\sigma_1$'s
  dominant fragment exceeds $\sigma_2$) by hand and re-verified with a
  fresh script (20,000 random trials, $m=2,\dots,7$): zero violations.
  New **§7.15 (Necessity Theorem)**: proves, via a rigorous continuity/
  limiting argument on the family $S_\varepsilon=\{\sigma_1-\varepsilon,
  \varepsilon\}\cup Z\cup\tau$ as $\varepsilon\to0^+$, that closing the
  complementary ($\sigma_2$-touched) residual for $m\ge5$ in full
  generality *entails* a restricted instance of $(\star_{m-2})$ — the
  project's own central open obstruction — directly refuting the round-27
  outline's premise that this front is self-contained. This reviewer
  independently re-checked the continuity argument (a standard "limit of
  a non-strict inequality" fact) and the algebraic identification with
  $(\star_{m-2})$ via §7.11's already-certified Index-Chain Identity: no
  gap found. **Correctly and honestly scoped, not an overclaim**: this
  proves a genuine necessary-condition entanglement, not that $(7.9.1)$ is
  false or unprovable for $m\ge5$ — it precisely explains *why* the
  existing elementary-facts toolbox cannot close it there, without
  foreclosing a future proof of $(\star_k)$, $k\ge3$ itself. Does not
  affect Claim (A)'s own already-solved status. 2 new lemmas certified
  (`sigma2-untouched-closure-theorem`; the Necessity Theorem's Continuity
  Lemma is folded into the approach file, not separately certified as a
  standalone lemma per the builder's own framing).

  **Net effect.** One genuine sub-milestone (**$n=3$ upper bound
  $c(3)\le8/15$ fully solved**, non-numeric, reviewer-certified), one
  genuine new unconditional theorem with one overclaim caught and
  corrected in-round (Theorem 41), and one genuine general-$m$ theorem
  plus an honest, rigorous "why this is hard" finding (§7.14/§7.15).
  Neither the general upper bound ($n\ge4$) nor the general lower bound
  (general $n$, all of Case (b)'s "$v\ge a$" branch, or $(\star_k)$ for
  $k\ge3$) is established; the whole problem remains **`partial`**.
  **Recommend next round:** (1) `greedy-halving-adversary` push $h(m)$
  (the "$T'$-cuts-$p_4$" branch) past $m=2$ toward general $m\ge3$, the
  one remaining piece of Case (b)'s "$v\ge a$" branch within this file's
  scope; (2) `rank-pigeonhole-budget`, per its own §7.15, either attempt
  $(\star_3)$ directly (now precisely identified as necessary, not just
  sufficient, for $\mathrm{MaxCeil}(5)$) or continue extending the
  $\sigma_2$-untouched theorem's reach; (3) `lp-duality-certificate`
  pivot to $n=4$ (deferred every round since round 23) now that $n=3$'s
  upper bound is fully closed, or to the $n=3$ lower-bound/achievability
  direction to complete a genuinely full $n=3$ solve of the whole
  problem.**

- **Round 28 (3 built slugs: all CHANGES REQUESTED, no RETHINK, no
  APPROVE; reviewer independently re-verified every new claim below with
  fresh exact-`Fraction` scripts, not the builders' own).**

  **`lp-duality-certificate`: genuine new sub-result, honestly scoped.**
  Re-ran the certified Theorem C'/Theorem A argument (the exact n=3
  closure mechanism, section 4 of the approach file) one index up at
  n=4, now that round 27's P(4) (the complete, both-regime n=3 upper
  bound) supplies the one missing ingredient Theorem C' needs for an
  arbitrary 4-piece tail. New result: for every 5-piece marking with
  p_1>=T/2, Phi_min(.;4)<=a_4*T=16T/31 - fully proved, non-numeric,
  reusing only already-general-n machinery (`full-match-achievability`,
  `bisect-top-recursive-identity`, `telescoping-threshold-identity`).
  Reviewer independently re-derived the telescoping algebra
  (a_3=a_4/(2(1-a_4)), a_3(1-a_4)+a_4/2=a_4, both confirmed exactly by
  `Fraction` computation) and independently re-verified the domain
  partition [T/2,a_4T) union [a_4T,T) = [T/2,T) with no gap/overlap,
  plus the underlying Theorem A construction (2000 exact-`Fraction`
  trials, zero mismatches). No gap found. **Honestly scoped, not an
  overclaim:** the file's own Status header and R28.3 explicitly state
  this covers only the p_1>=T/2 half of n=4; the p_1<T/2 half is
  untouched and expected to need a fresh chamber census (per the
  round-28 explorer's density-growth signal), not attempted this round.
  Does not close c(4)<=16/31 in general. 1 new lemma certified
  (`p1-geq-half-closure-n4`).

  **`greedy-halving-adversary`: genuine general-m theorem, correctly
  scoped to the sub-case the outline-reviewer restricted it to.** Per
  the outline-reviewer's flagged false-transfer risk (Theorem 40/41's
  rank-split mechanism needs an anchor unconditionally dominating the
  tail it is peeled from - not automatic once S is free to cut h(m)'s
  own top piece q_1), the build restricted its target to the
  q_1-untouched sub-case and proved it in full for every m>=1 at once:
  new **Lemma A (General Anchored-Tie Bound, both parities)** - a
  literal, from-scratch abstraction of the certified Theorem 40/41
  mechanism to an arbitrary anchor/tail pair (w,X,g), using only
  w>max(X) and g=w-Total(X), no ladder structure - and new **Theorem
  42** (instantiating Lemma A with w=q_1, X=S'', and the ladder mass
  identity g=q_1-Total(S'')=f(m), combined with Theorem 38's existing
  c=0,q_1 vertex closures) giving a full, unconditional closure of
  h(m)'s q_1-untouched sub-case for every m>=1. **This reviewer
  independently re-derived Lemma A's proof by hand (both the odd- and
  even-multiplicity cases) and re-verified it with two fresh
  exact-`Fraction` scripts** - a general abstract test (50,000 trials,
  arbitrary w,X,t*, zero violations, minimum slack exactly 0, matching
  the proof's own tight case) and a direct ladder instantiation test of
  Theorem 42's full claim (m=1,...,5, legal cut-distributions on the
  tail generated per-piece, zero violations). No gap found in either
  Lemma A or Theorem 42. **The complementary "q_1-cut" sub-case is
  honestly and explicitly left open** for m>=3 - the file states plainly
  that no domination anchor was found there (the natural candidate
  ratio degenerates as the split approaches q_1/2, mirroring the file's
  own round-26 "c_2-anchor" diagnosis) and reports the search as
  unattempted-to-completion rather than claiming a negative result not
  yet proved. h(m) for m>=3 remains open; the open territory is now
  precisely delimited to the q_1-cut branches only. 1 new lemma
  certified (`general-anchored-tie-bound`).

  **`rank-pigeonhole-budget`: substantial, honestly-scoped progress on
  (star_3)=MinFloor(4); not closed.** First corrected the round-28
  outline's self-contradictory shape count (the outline's own
  stars-and-bars formula computes 35 - the count of "<=3 cuts"
  compositions - but its stated total was "20," which is instead
  C(6,3), the count of "*exactly* 3 cuts" compositions; reviewer
  independently re-derived both counts, C(7,4)=35 and C(6,3)=20,
  confirming the fix) and supplied the missing justification (via
  `vertex-minimum-theorem` part 2's family-(I) "zero fragment"
  tight-vertex clause) for why closing only the 20 exactly-budget-3
  shapes on their closed domains still proves the theorem for the full
  35-shape "<=3" space - a standard, correctly argued closure/padding
  argument. **Two new master theorems, fully proved and
  reviewer-reverified** (Master Theorem I: all 10 shapes with pi_1
  untouched, via one dominant-peel + Fact-2 argument; reviewer
  re-verified with 2000 fresh trials per shape, zero violations. Master
  Theorem II: all 3 shapes with one cut on pi_1 and pi_2 untouched, a
  2-3-level peel cascade uniform in how the remaining budget splits
  pi_3,pi_4; reviewer re-verified with 200,000 trials on the hardest
  residual sub-region, zero violations), plus shape (3,0,0,0) closed for
  free by direct citation of the already-certified `claim-a-full-
  closure` (it literally *is* Claim A at n=3) - reviewer confirms this
  citation is exact, not an analogy. This closes 14/20 shapes fully
  (both directions). **Genuine correction to the outline's own severity
  ranking:** exact vertex enumeration found 6 shapes (not the outline's
  claimed 2) attain A=1 exactly; achievability is proved by hand,
  uniformly, for all 6 (reviewer independently re-verified all six
  explicit constructions: correct per-piece arithmetic, each reduces via
  `odd-run-reduction-lemma` to {2,1}, A=1 exactly). **The matching lower
  bound on these 6 shapes' residual 3-free-parameter sub-region
  (f_1 in (3,4)-type) is honestly reported as open** - the file
  explicitly states the cheap peel-and-Fact technique provably fails
  there (a concrete boundary check where Fact 2 gives A<=5 against a
  needed <=1) and that only numeric vertex-enumeration evidence (not a
  hand proof) supports the conjectured value 1. **(star_3) is therefore
  NOT closed this round**; the file's own Status header correctly
  states "solved" only for Claim (A) (already closed round 8, unaffected
  by this round's separate §7.16 work on (star_3)) - no overclaim found.
  1 new lemma certified
  (`master-theorem-ii-single-split-untouched-second-piece`; Master
  Theorem I not separately certified as it is a special case of the
  already-noted `minfloor-untouched-top-closure` general theorem).

  **Net effect.** All three fronts made genuine, independently-verified,
  honestly-scoped progress; no overclaim found in any of the three files
  this round (a first in several rounds - rounds 24-27 each had at least
  one overclaim the reviewer had to correct). None of the three closes
  its own round-28 target in full: n=4's upper bound remains open for
  p_1<T/2; h(m) remains open for m>=3's q_1-cut branch; (star_3) remains
  open on 6 shapes' residual sub-region. **Status remains `partial`**
  for the whole problem. **Recommend next round:** (1)
  `rank-pigeonhole-budget` - attack the 6 shapes' residual
  3-free-parameter sub-region directly (now the single most precisely
  localized open item toward (star_3), with the extremal vertex and its
  value already identified numerically); (2) `greedy-halving-adversary`
  - the q_1-cut sub-case of h(m), m>=3, needs either a genuinely new
  domination mechanism or a case-split on how close the split is to
  q_1/2 (flagged but not attempted this round); (3)
  `lp-duality-certificate` - the p_1<T/2 regime of n=4, expected to
  need a fresh chamber census given the 28%->64% density-growth signal
  between n=3 and n=4.

- **Round 29 (3 built slugs, all CHANGES REQUESTED, no RETHINK, no
  APPROVE; reviewer independently re-verified every new claim below with
  fresh exact-`Fraction`/`sympy` scripts, not the builders' own).**

  **`rank-pigeonhole-budget`: fixes the outline-reviewer's flagged
  citation bug and closes 1 of 6, plus half of a 2nd, residual
  $(\star_3)$ shapes.** New **Pair-Insertion Ordering Lemma** (two
  forms, "between" $q\le w\le p$ and "above" $w\ge p\ge q$) gives an
  *exact* closed form for inserting one free value into a
  mass-conserving pair plus a reference value — the correct, from-scratch
  replacement for the outline's invalid citation of
  `single-insert-point-vertex-lemma` on a coupled pair (that lemma is
  proved only for a single free coordinate against a genuinely fixed
  rest; a mass-conserving pair moves at slope $\pm2$, not $\pm1$).
  Reviewer independently re-verified both forms exactly (200,000 trials
  each, zero mismatches). Applied it to **fully close shape $(2,0,1,0)$**
  (both directions, no residual) and **shape $(2,0,0,1)$'s $f_1<4$
  regime** (complementary regime $f_1\ge4$ still numerics-only). Reviewer
  independently re-derived, via `sympy`, all 8 of the case-by-case
  polynomial reductions used in these two closures (4 cases each) and
  confirmed every one matches the file's claimed simplified polynomial
  exactly; also independently re-verified both shapes' target inequality
  directly (300,000 trials each, min value exactly 1, matching the
  claimed tightness). No gap found. The other 4 residual shapes
  ($(1,1,0,1),(1,1,1,0),(1,2,0,0),(2,1,0,0)$) are honestly reported as
  untouched this round. 1 new lemma certified
  (`pair-insertion-ordering-lemma`).

  **`greedy-halving-adversary`: closes 4 of 5 vertex types of $h(m)$'s
  single-cut-on-$q_1$/tail-untouched piece, $m\ge3$; the 5th honestly
  open.** First supplies the vertex-pinning justification the
  outline-reviewer flagged as missing (invokes the certified
  `single-insert-point-vertex-lemma` correctly this time — one free
  coordinate $c$ against the genuinely fixed rest $S$ — to pin the
  minimizer to exactly 5 candidates $c\in\{0,q_1,x,q_1-x,t\in\text{tail}\}$
  before any anchored-tie bound is used), closing the flagged $c=0,c=w,
  c=q_1$ boundary gaps explicitly along the way. New **Insert-Bound
  Corollary** ($|A(\{y\}\cup T)-A(T)|\le y$, any finite multiset $T$, any
  $y\ge0$) is a one-line integration of the already-certified
  `single-insert-point-vertex-lemma`'s slope fact — reviewer independently
  re-verified it directly (200,000 trials, zero violations). Vertices
  1-4 ($c=0,q_1,x,q_1-x$, plus the full symmetric boundary $x=q_1/2$)
  are closed unconditionally for every $m\ge3$ via direct peels
  (`sharp-dominant-removal-identity`), pair-cancellation, citation of
  Theorem 42 one level down, and (Vertex 4) an explicit geometric-series
  evaluation of the untouched tail reducing to the elementary inequality
  $2^{m-1}\ge3+(-1)^{m-1}$ (true for every $m\ge3$). Reviewer
  independently re-derived this reduction and re-verified all 5 vertex
  types directly (not just via the file's own intermediate identities)
  with a fresh script spanning $m=3,\dots,8$ and a dense sweep of $x$ and
  every tail element $t$: zero violations, including at the honestly-open
  Vertex 5. **Vertex 5** ($c$ tied to a genuine non-degenerate tail
  element $t$) is correctly left open — the natural two-step argument
  provably loses a factor of $2x$ against a gain of only $t$, confirmed
  by the reviewer's own trace of the algebra, not merely asserted; only
  numeric corroboration (3000 trials/$m$) is offered, honestly flagged as
  not a proof. No overclaim found (a useful continuation of round 28's
  precise, non-overclaiming pattern on this file). 1 new lemma certified
  (`insert-bound-corollary`).

  **`lp-duality-certificate`: 3 free transplants close most of $n=4$'s
  upper bound; new Double-Bisect-Pin Theorem plus 100% empirical (not
  proof) coverage of the remaining residual box.** The three transplanted
  closures ($p_2\le T/31$, $p_2\ge8T/31$, $p_1\ge T/2$) are pure
  instantiations of already-general-$n$ lemmas with the threshold algebra
  re-derived from scratch — reviewer independently re-checked the
  arithmetic ($8T/31$ from $(a_3-a_4)T/(2a_3-1)$ matching $a_4T/2$). The
  residual $\mathcal R$ ($p_1<T/2$ and $T/31<p_2<8T/31$) is instantiated
  against the certified Bisect-Subset-Lemma (30 chambers, $\approx93\%$
  measured coverage) and a genuinely new **Double-Bisect-Pin Theorem**
  (bisect 2 pieces, pin 1 of the remaining 3 to another, leave the last
  untouched; closed form $\Phi=(T+|p_k-p_l-p_r|)/2$, 30 more chambers,
  proved via 3 iterated applications of the certified
  `pair-insensitivity-corollary`) — reviewer independently re-verified
  this exact formula (20,000 trials, zero mismatches). Combined, the
  60-chamber family gives 100% coverage on 30,000 fresh exact-`Fraction`
  trials, with a genuine diagnostic that no small subset of the pin
  family suffices (14+ distinct chambers each win somewhere). **Correctly
  and explicitly flagged as empirical, not a proof**: no Farkas-style
  exhaustive covering argument has been derived, consistent with this
  project's own rounds-24-26 lesson that clean numeric coverage has
  previously hidden a real exact-counterexample gap elsewhere. No
  overclaim found — the file's own Status header says `partial` and
  matches. 1 new lemma certified (`double-bisect-pin-family-n4`).

  **Net effect.** All three fronts made genuine, independently-verified,
  honestly-scoped progress; no overclaim found in any of the three files
  this round (continuing round 28's clean run). None closes its own
  round-29 target in full: $(\star_3)$ has 4 of 6 residual shapes still
  untouched (plus 1 half-open); $h(m)$'s single-cut-on-$q_1$ piece has
  1 of 5 vertex types still open, and the tail-refining complementary
  piece of the $q_1$-cut sub-case is entirely untouched; $n=4$'s upper
  bound residual box is empirically but not rigorously covered.
  **Status remains `partial`** for the whole problem. **Recommend next
  round:** (1) `rank-pigeonhole-budget` — apply the now-proven
  Pair-Insertion Ordering Lemma to the remaining 4 shapes
  ($(1,1,0,1),(1,1,1,0),(1,2,0,0),(2,1,0,0)$) and finish shape
  $(2,0,0,1)$'s $f_1\ge4$ regime by hand; (2) `greedy-halving-adversary`
  — Vertex 5 needs either a genuinely new mechanism (not a peel-and-bound
  on the punctured tail) or a proof that it cannot be closed by this
  route, plus the untouched tail-refining piece of the $q_1$-cut
  sub-case; (3) `lp-duality-certificate` — attempt the Farkas-style
  exhaustive covering argument for the 60-chamber family, or identify the
  true worst-case vertex/vertices of $\mathcal R$ directly.

- **Round 30 (3 built slugs, all CHANGES REQUESTED, no RETHINK, no
  APPROVE; reviewer independently re-verified every new claim below with
  fresh exact-`Fraction` scripts, not the builders' own).**

  **`rank-pigeonhole-budget`: 3 of the 4 remaining residual $(\star_3)$
  shapes fully closed by hand; the last 2 honestly left open with a
  sharper diagnosis.** Closed shape $(2,0,0,1)$'s remaining $f_1\ge4$
  branch (round 29 had already closed $f_1<4$) and shapes $(1,1,0,1)$,
  $(1,1,1,0)$ in full, both directions, via the round-29-certified
  Pair-Insertion Ordering Lemma plus `sharp-dominant-removal-identity`/
  `odd-run-reduction-lemma`, no new lemma needed. Reviewer independently
  re-verified: (i) a fresh 400,000-trial random search across all 5
  shapes (the 3 newly closed plus the still-open $(1,2,0,0)/(2,1,0,0)$),
  zero violations, minimum $\approx1$ on the closed shapes exactly as
  claimed; (ii) a targeted 20,000-trial exact-`Fraction` check of one
  specific sub-case (shape $(2,0,0,1)$, $f_1\in(4,5)$, $f_2>2$ strict)
  confirming the closed-form algebra exactly, zero violations. No gap
  found in the closed shapes. Shapes $(1,2,0,0)$ and $(2,1,0,0)$ are
  honestly reported as **not** closed — the file correctly diagnoses a
  genuinely new obstruction (no a priori dominance between $f_1$, the
  free $\pi_1$-triple's top, and $c$, the free $\pi_2$-pair's top, plus a
  joint-feasibility cross-constraint needed to close even one identified
  sub-sub-case) rather than claiming a false closure. $(\star_3)$ is now
  4 of 6 shapes fully closed (up from 2 of 6 at the start of the round);
  no lemma newly certified this round (only applications of
  already-certified facts).

  **`greedy-halving-adversary`: Vertex 5 of $h(m)$'s single-cut-on-$q_1$/
  tail-untouched piece fully closed for every $m\ge3$, correcting a false
  equality claim in the round's own outline along the way.** New
  **exact-slope monotonicity argument** (citing the already-certified
  `single-insert-point-vertex-lemma`'s $\pm1$-slope fact, not a new
  lemma) collapses the continuum in $x\in(0,q_1/2)$ to the single
  boundary point $x=q_1/2$; a new **closed-form "remove one rung"
  identity** $A(\mathrm{tail}\setminus\{a_p\})=f(m)(2^m+(-1)^p2^{m-p}
  +(-1)^m)/3$ evaluates that boundary exactly, uniformly in which tail
  element $t=a_p$ is tied. The file correctly identifies and fixes a bug
  in its own round-30 outline (which had wrongly claimed the boundary
  reduces to $A(\mathrm{tail})=f(m)$, an exact equality for every $m$ —
  false for every $m\ge4$; the true reduced object is
  $A(\mathrm{tail}\setminus\{t\})$, strictly exceeding $f(m)$ for
  $m\ge4$, equal only at $m=3$). Reviewer independently re-derived the
  closed form and re-verified it, plus the final inequality
  $2^m+(-1)^p2^{m-p}+(-1)^m\ge3$, by a fresh exact-`Fraction` script for
  $m=3,\dots,9$ and every $p=1,\dots,m$ (matching the builder's own
  $m=3,\dots,14$ check) and independently confirmed the monotonicity of
  $F(x)$ on a dense rational grid: zero mismatches/violations throughout.
  No gap found. **Correctly scoped, no overclaim**: this closes only the
  "single cut on $q_1$, tail completely untouched" piece; the
  complementary piece (simultaneous $q_1$-cut and tail-refinement) is
  honestly reported as fully open and entirely untouched this round, so
  $h(m)$ for $m\ge3$ overall remains open. 1 new lemma certified
  (`single-rung-removal-closed-form-and-vertex-5-closure`).

  **`lp-duality-certificate`: correctly retracts round 29's refuted
  "100% coverage" claim and proves a new, general, unifying Partition
  Chamber Theorem that closes both known counterexample witnesses.**
  First independently re-confirmed the round-30 explorer's exact
  counterexample ($p=(11,7,6,3,2)/29$, all 60 of round 29's chambers
  give $\Phi=15/29>16/31=a_4T$ by exactly $1/899$) and correctly
  retracted the false coverage claim in three places in the file (Status
  header, "Current best," and the round-29 write-up itself), explicitly
  preserving the individually-correct chamber formulas. New **Partition
  Chamber Theorem**: for any partition of the index set into blocks
  (each block of size $\ge2$ has one "host" cut to match the others
  exactly plus a residual; singletons are left untouched or bisected),
  $\Phi=(T+A(Q))/2$ where $Q$ collects the residuals and untouched
  singletons — proved via the certified `pair-insensitivity-corollary`
  alone, unifying `bisect-subset-lemma`, Double-Bisect-Pin, a corrected
  Triple-Pin (fixing a genuine formula bug in the round-30 outline that
  had omitted the untouched-vs-bisected distinction for the 5th piece),
  and a new Double-Pin-Pair family. Reviewer independently re-derived
  the proof and re-verified the general formula (1913 fresh exact-
  `Fraction` trials, $m=3,\dots,7$, random partitions/hosts/bisection
  choices — a broader sweep than the builder's own $m=5$-only check,
  zero mismatches) and both witness closures ($\Phi=1/2<16/31$ in each
  case, exact). No gap found. **Correctly and explicitly scoped, not an
  overclaim**: full coverage of the residual region $\mathcal R$ is
  honestly not re-claimed (only the two known witnesses are shown
  closed); the Farkas-style exhaustive covering argument, and whether
  the Partition Chamber family is itself exhaustive over all legal
  strategies, both remain open. 1 new lemma certified
  (`partition-chamber-theorem`; the Corrected Triple-Pin and
  Double-Pin-Pair instances are one-line special cases documented within
  it, not separately certified).

  **Net effect.** All three fronts made genuine, independently-verified,
  honestly-scoped progress, and (for the first time this run) one front
  performed a mandatory self-retraction of a previously-recorded false
  claim correctly and completely (`lp-duality-certificate`). No overclaim
  found in any of the three files this round (continuing rounds 28-29's
  clean run). None closes its own round-30 target in full: $(\star_3)$
  now has only 2 of 6 shapes open (down from 4); $h(m)$'s
  single-cut-on-$q_1$ piece is now fully closed, but the tail-refining
  complementary piece of the $q_1$-cut sub-case remains entirely
  untouched; $n=4$'s upper bound residual box has two known witnesses
  closed but no re-established coverage claim. **Status remains
  `partial`** for the whole problem. **Recommend next round:** (1)
  `rank-pigeonhole-budget` — attack shapes $(1,2,0,0)/(2,1,0,0)$'s
  cross-pair joint-feasibility obstruction directly (now the single
  most precisely diagnosed open item toward $(\star_3)$); (2)
  `greedy-halving-adversary` — the simultaneous $q_1$-cut-and-tail-
  refinement piece of $h(m)$'s $q_1$-cut sub-case needs a genuinely new
  mechanism, not yet attempted at all; (3) `lp-duality-certificate` — run
  a fresh outer-minimization (allocation-agnostic) search against the
  expanded Partition Chamber family before attempting any Farkas-style
  coverage proof, per the file's own methodological warning.

- **Round 31 (3 built slugs, all CHANGES REQUESTED, no RETHINK, no
  APPROVE; reviewer independently re-verified every new claim below with
  fresh, from-scratch exact-`Fraction` scripts, not the builders' own).**

  **`rank-pigeonhole-budget`: the last 2 of 6 residual $(\star_3)$
  shapes, $(1,2,0,0)$ and $(2,1,0,0)$, fully closed via exhaustive exact
  vertex enumeration — $(\star_3)=\mathrm{MinFloor}(4)$ now fully closed,
  all 20 maximal shapes, both directions.** Reviewer independently
  re-derived, from the shapes' own defining constraints (not copied from
  the file), the complete hyperplane families in both cases and got an
  *exact* match to the file's counts: 18 hyperplanes / 36 feasible
  vertices for $(2,1,0,0)$, 21 hyperplanes / 27 feasible vertices for
  $(1,2,0,0)$, both computed independently in exact `Fraction`/`sympy`
  rational arithmetic; minimum $A(U)=1$ over all vertices in both cases,
  matching the file's tables row for row at the tight vertices. Went
  further than a vertex-only re-derivation: ran a 2,000,000-trial
  continuum (non-vertex-restricted) random search over the full feasible
  region for each shape, confirming no interior point beats $A(U)=1$
  (min found $\approx1.0000015$, consistent with the true infimum being
  exactly 1) — this independently corroborates that the restriction to
  vertices (via the already-certified `vertex-minimum-theorem`) is itself
  valid, not just that the claimed vertex list is self-consistent. No gap
  found. The file's own Status header correctly scopes "solved" to Claim
  (A) only (already established in earlier rounds); this round's result
  is an honestly-labeled side-closure of $(\star_3)=\mathrm{MinFloor}(4)$,
  not a claim that the whole `imo-2026-03` problem or even Claim (A)'s
  own status changed. 1 new lemma certified
  (`minfloor-4-full-closure`).

  **`greedy-halving-adversary`: closes 2 of $h(m)$'s "simultaneous
  $q_1$-cut and tail-refinement" vertices ($c=q_1-x,c=q_1$) via a new,
  genuinely distinct strong-induction-on-$h(m-1)$ mechanism (unconditional
  at $m=3$, conditional for $m\ge4$); correctly cites the sibling's
  $\mathrm{MaxCeil}(m)$ for $c=x$ (verified a real term-for-term identity,
  not an analogy); partially advances the new $c=t\in S''$ vertex.**
  Reviewer independently re-verified the $IH(m-1)$ induction step at
  $m=3$ with a fresh exact-`Fraction` script (random legal $S''$
  refinements and $x$ values, including deterministic extreme/boundary
  configurations), zero violations against the correctly-scaled target
  (caught and fixed an initial scaling error in the reviewer's own first
  script — the correct unnormalized target at $D_3=15$ is $1$, not
  $1/15$; the corrected script confirmed the claim). Independently
  cross-checked the "$c=x\equiv\mathrm{MaxCeil}(m)$" citation by tracing
  both definitions from scratch: `rank-pigeonhole-budget`'s
  $\mathrm{MaxCeil}(\ell)$ (length-$\ell$ ratio-2 tail, top $\sigma_1$,
  bottom $\sigma_\ell$, every legal $\le(\ell-2)$-cut refinement,
  $A(S)\le\sigma_1-\sigma_\ell$) matches the vertex's own needed
  inequality $A(S'')\le q_2-f(m)$ term for term under $\ell=m$; this
  matches the outline-reviewer's own independent trace as well — genuine
  cross-approach leverage, not a citation of convenience. The new
  $c=t\in S''$ vertex is correctly reported as only partially closed:
  the "$t=q_2$, whole top rung untouched" sub-case is closed in full
  (verified the rescaling-to-$(\star_{m-2})$ argument); "split-rung
  fragment removed" has an incomplete reduction toward
  $\mathrm{MaxCeil}(m-1)$; "$q_2$ untouched, $t\ne q_2$" is honestly left
  fully open (reduces to an unaddressed "punctured $\mathrm{MaxCeil}$"
  object). Status `partial` is honestly scoped: $h(m)$ for $m\ge3$
  overall remains open even at $m=3$ (since $c=t\in S''$'s "$q_2$
  untouched, $t\ne q_2$" case is untouched). No gap or overclaim found.
  1 new lemma flagged by the builder for the $h(m-1)$-as-IH step but not
  separately certified this round (it is folded into and re-verified as
  part of the approach file's own narrative; recommend certifying on a
  future round once its statement is extracted standalone).

  **`lp-duality-certificate`: proves a new general Half-Complement Pin
  Theorem and a corollary closing the $n=4$ sub-strip $p_1\in
  [15T/31,T/2)$ unconditionally, for arbitrary $p_2,p_3,p_4,p_5$ within
  the residual $\mathcal R$'s bounds.** Reviewer independently re-derived
  the theorem's closed form $\Phi=\max(q_1,T-q_1)$ from the raw
  definitions (not via the file's own substitution steps) and, going
  further, built the *actual* 8-element fragment multiset the strategy
  produces (fragments of $p_1$ matching $p_3,p_4,p_5$ plus a residual,
  union the untouched $p_2,p_3,p_4,p_5$) and computed its alternating sum
  directly by full sorting — confirming from scratch (not merely
  re-deriving the file's own reduced-to-2-elements shortcut) that the
  full multiset's $A$ matches the reduced formula, and that feasibility
  ($2p_1+p_2\ge T$) holds automatically and $\Phi\le a_4T$ throughout,
  across 11,625 exact-`Fraction` trials targeted at the claimed region
  (zero violations). Checked the "no overlap/miscount" claim: the two
  previously-known hard witnesses ($p_1/T\approx0.379,0.467$) both lie
  below $15/31\approx0.4839$, confirmed by direct arithmetic, so they are
  correctly reported as outside the newly-closed strip — this is
  genuinely new territory, not a re-closure inflating the coverage count.
  Status `partial` is honest: the file explicitly and correctly states
  that $\mathcal R':=\{p_2\le p_1<15T/31,\ T/31<p_2<8T/31\}$ remains open
  and that full $n=4$ coverage is not established. No gap or overclaim
  found. 2 new lemmas proposed for certification
  (`half-complement-pin-theorem`, `n4-strip-closure-corollary`) — both
  certified this round (see Promotable lemmas note below).

  **Net effect.** All three fronts made genuine, independently-verified,
  honestly-scoped progress; no overclaim found in any of the three files
  this round (continuing rounds 28-30's clean run). $(\star_3)=
  \mathrm{MinFloor}(4)$ is now **fully closed** (a complete sub-result,
  not the whole problem); $h(m)$'s simultaneous-cuts piece has 2 of 5
  vertex types newly closed, with the residual narrowed to mostly
  $c=t\in S''$ plus the shared $c=x,m\ge5$ item; $n=4$'s upper bound
  residual shrinks from $\mathcal R$ to the strictly smaller $\mathcal
  R'$. **Status remains `partial`** for the whole problem. **Recommend
  next round:** (1) `rank-pigeonhole-budget` — with $(\star_3)$ fully
  closed, the natural next target is the general-$n$ $(\star_k)$,
  $k\ge3$, obstruction (shared with `greedy-halving-adversary`'s
  $h(m\ge5)$) rather than further $n=4$-specific casework; (2)
  `greedy-halving-adversary` — the "$q_2$ untouched, $t\ne q_2$" case
  needs a genuinely new "punctured $\mathrm{MaxCeil}$" object, and
  $\mathrm{MaxCeil}(m\ge5)$ remains the shared blocking item with the
  sibling file (coordinate, do not duplicate); (3)
  `lp-duality-certificate` — attempt a covering argument (Farkas-style or
  a new pin family) for the residual $\mathcal R'=\{p_2\le p_1<15T/31,\
  T/31<p_2<8T/31\}$, now a strictly smaller target than $\mathcal R$.

- **Round 32 (3 built slugs, all CHANGES REQUESTED, no RETHINK, no
  APPROVE; reviewer independently re-verified every new claim below with
  fresh exact-`Fraction`/`scipy` scripts of its own, not the builders'
  own).** `greedy-halving-adversary` closed $h(m)$'s vertex $c=t\in S''$
  Case (ii) ("$q_2$ untouched, $t\ne q_2$") **unconditionally for every
  $m\ge3$** via a new theorem combining an extracted standalone Fact 2
  ($A(S)\le\mathrm{Total}(S)$, elementary pairing proof), mass
  conservation under refinement, a shifted-index telescoping identity, and
  `sharp-dominant-removal-identity` — reviewer independently re-derived
  the telescoping identity by hand and re-verified the full inequality
  (3000-trial exact-`Fraction` search per $m=3,\dots,7$, zero violations).
  Combined with this and the previously-closed pieces, the builder claims
  **$h(3)$'s entire "simultaneous $q_1$-cut and tail-refinement" vertex
  piece is now fully closed** (modulo the standing $(\star_3)$ dependency)
  — reviewer independently re-derived the exhaustive 4-type ($0,A,B,C$)
  enumeration at $m=3$ and hand-verified the Type-A ($q_2$-split) closure
  exactly (matches the builder's claimed tight boundary $u=q_2/2$ giving
  equality $1/15$), confirming the claim holds with no gap. **Reviewer
  note (not a gap, a missed strengthening):** $(\star_3)=\mathrm{MinFloor}
  (4)$ is itself already fully, unconditionally certified as of round 31
  — so $h(3)$'s closure is in fact already unconditional, though the
  approach file's own text conservatively still calls it "modulo
  $(\star_3)$"; worth stating outright next round. $h(m)$ for $m\ge4$
  remains explicitly, correctly, not claimed closed (new shapes appear
  at $\ge2$-cut tail budgets). 1 new lemma certified this round
  (`hm-case-ii-punctured-tail-closure`; `fact-2-alternating-sum-leq-total`
  upgraded from proposed to certified).

  `rank-pigeonhole-budget` did the dispatched free corollary
  (§7.19.1, $\mathrm{MaxCeil}(5)$'s top-untouched branch) and then
  **achieved substantially more than dispatched**: two new fully general,
  ladder-free lemmas — **Max Bound** ($A(S)\le\max(S)$) and **Insertion
  Sandwich** ($|A(T\cup\{a\})-A(T)|\le a$) — combined into a **Master
  Theorem** ($\mathrm{MinFloor}(m-1)=(\star_{m-2})\Rightarrow
  \mathrm{MaxCeil}(m)$ **in full**, both branches, one unified two-case
  argument, explicitly a genuinely different mechanism from the
  two-peel+Fact-2 route §7.15's Necessity Theorem had already proved
  insufficient). Reviewer independently re-derived and verified Max
  Bound and Insertion Sandwich (50,000-trial exact-`Fraction` searches
  each, zero violations), independently re-checked the Master Theorem's
  two-case proof by hand (both cases correct, including the iterated
  Insertion-Sandwich telescoping step for $c_1\ge1$), and independently
  re-verified its $m=5$ instantiation with a fresh 300,000-trial
  exact-`Fraction` random+boundary search at $\sigma=(16,8,4,2,1)/31$:
  maximum $A(S)$ found is exactly $15$ (attained at a boundary
  configuration), never exceeded. Since $(\star_3)=\mathrm{MinFloor}(4)$
  is already certified (round 31), **$\mathrm{MaxCeil}(5)$ is now closed
  in full, unconditionally** — one level past round 26's $\mathrm{MaxCeil}
  (3),(4)$ — closing $(7.9.1)$ at $n=8$. The Master Theorem itself is
  honestly scoped as conditional on $(\star_{m-2})$ for general $m$ (not
  claimed unconditional beyond $m=5$). This is a genuinely new, reusable
  mechanism, no gap found. 3 new lemmas certified this round
  (`max-bound-fact`, `insertion-sandwich-lemma`,
  `maxceil-master-theorem` — certified with its conditional scope
  preserved exactly as stated, not overclaimed as general-$m$
  unconditional).

  `lp-duality-certificate` proved a new general **Leave-2-Untouched
  Theorem** (direct instantiation of the certified
  `partition-chamber-theorem` with two untouched singleton indices) —
  reviewer independently re-derived and verified the 3-branch closed
  form (1583-trial exact-`Fraction` re-check, zero mismatches) — and then
  **honestly refuted its own dispatch target**: an exact-arithmetic
  search inside the residual $\mathcal R'$ found a genuine witness where
  the full 120-chamber named family (all prior chambers plus this
  round's new one) simultaneously fails, ruling out a Farkas certificate
  over this family as *provably impossible*. Reviewer independently
  reproduced this finding to high precision: built the exact witness
  point $p/T\approx(0.481876,0.257766,0.155969,0.069213,0.035176)$,
  confirmed the named-family minimum is $\approx0.5162916>a_4T=
  16/31\approx0.5161290$ (matching the builder's number to 10 decimal
  places), and independently ran a from-scratch `differential_evolution`
  search over every legal cut-count composition (not the builder's own
  script) confirming the true unconstrained optimum is
  $\approx0.5005360$ (composition $(2,1,0,0,1)$, equivalent to the
  builder's reported $(2,0,0,0,2)$) — well below $a_4T$, so **not** a
  counterexample to $c(4)\le16/31$, just a genuine gap in this specific
  chamber family (a 3-fragment cut on $p_5$ simultaneous with a
  3-fragment cut on $p_1$, a shape absent from every chamber on file).
  This is exactly the right way to report a negative finding — no
  overclaim, no unsound Farkas attempt over an incomplete family.
  $\mathcal R'$ remains open. 1 new lemma certified this round
  (`leave-2-untouched-theorem`); 1 new dead-end record
  (`n4-120-chamber-family-incomplete-dead-end`).

  **Net effect.** All three fronts made genuine, independently-verified,
  honestly-scoped progress; no overclaim found in any of the three files
  this round (continuing rounds 28-31's clean run). $h(3)$'s
  "simultaneous-cuts" piece is now fully closed (all 5 vertex types);
  $\mathrm{MaxCeil}(5)$ (hence $(7.9.1)$ at $n=8$) is now fully closed,
  unconditionally, via a new general-purpose Master Theorem that will
  apply automatically at future $(\star_k)$ closures; $n=4$'s upper-bound
  residual family is proved genuinely incomplete (not just numerically
  hard) at $\mathcal R'$, redirecting future effort away from a doomed
  Farkas attempt over the current chamber family. **Status remains
  `partial`** for the whole problem. **Recommend next round:** (1) the
  shared $h(m\ge4)$/$\mathrm{MaxCeil}(m\ge6)$/$(\star_{k\ge4})$
  obstruction is now the single cleanest remaining lower-bound target —
  both `greedy-halving-adversary` and `rank-pigeonhole-budget` should
  coordinate on $(\star_4)$ directly, since the Master Theorem will
  immediately propagate any such closure to $\mathrm{MaxCeil}(6)$ and
  beyond; (2) `lp-duality-certificate` should attempt a new chamber
  family member covering the $(2,0,0,0,2)$-type simultaneous-multi-
  fragment-cut shape (reverse-engineered from this round's optimizer
  argmin) rather than another Farkas attempt over the existing family.
