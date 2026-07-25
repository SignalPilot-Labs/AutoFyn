## imo-2026-03 — lens: the general lower-bound gap (Case 2)

**Gap statement recalled.** LB fixes the geometric partition $r_i=2^i/(2^{n+1}-1)$,
$i=0,\dots,n$. Need: for *every* way XY spends its $\le n$ cuts (any
distribution among the $r_i$'s, any split values), the resulting multiset
has $\mathrm{OddSum}\ge c(n)=r_n$. Case 1 (no cut on $r_n$) is proved
(`lemmas/dominant-piece-lower-bound.md`). Case 2 (some cut(s) land on $r_n$)
is open for $n\ge2$.

### Numerical exploration (all labeled conjecture/evidence, not proof)

Used `numpy`/`scipy` (Nelder-Mead, many random restarts, and exact rational
checks at small $n$) to search the *worst* (OddSum-minimizing) response over
all cut-count allocations and all split values, for $n=2,3,4$.

1. **Global minimum over all cut allocations equals exactly $c(n)$.**
   Exhaustive grid over cut-count vectors $(m_0,\dots,m_n)$, $\sum m_i=n$,
   at $n=3$: the minimum OddSum over every allocation, optimized over split
   values, is exactly $8/15=c(3)$, matching the claimed lower bound with
   equality (never below). Confirms the conjecture numerically but is not
   a proof.
2. **Concentrating cuts on the top piece is (weakly) optimal for XY.**
   Allocations that put all $n$ cuts on $r_n$ reach the target exactly;
   splitting cuts between $r_n$ and other pieces never does better than
   $c(n)$ and is sometimes strictly worse for XY (e.g. $n=3$: putting cuts
   on lower pieces alone gives $2/3$ or $19/30$, well above target). Several
   *different* allocations (not just all-on-top) also hit the floor exactly
   — e.g. at $n=3$: $(m_0,m_1,m_2,m_3)=(0,0,1,2)$ and $(1,0,1,1)$ both reach
   $8/15$ too, so the extremal configuration is **not unique** — there is a
   whole family attaining equality. This suggests any proof will need to
   handle a plateau of tie cases, not a single extremal split.
3. **Local-min / plateau structure of the top-piece split.** Fixing all $n$
   cuts on $r_n$ only, and starting from the exact "self-similar" split
   $q_i=r_n\cdot 2^i/(2^{n+1}-1)$ (the ratio LB itself uses, found in round 1),
   a fine sweep along a one-parameter family of perturbations (transfer
   $t$ between two fragments, sum fixed) shows OddSum as a function of $t$
   is **piecewise linear**: flat at some value above target, then strictly
   decreasing, then **flat exactly at the target value $c(n)$ over a whole
   interval of $t$** (checked at $n=3$: flat at $0.6$, decreasing, flat at
   $8/15\approx0.5333$ for $t\in[0.058,0.24]$ and presumably beyond).
   So the minimum is attained on an interval/face, not an isolated point —
   the extremal splits form a region, likely characterized by a specific
   fragment becoming tied in value with some $r_i$ (a rank-boundary tie),
   after which further perturbation doesn't change OddSum because it only
   moves mass within one "rank block." This matches exactly the kind of
   tie the certified lemma `tie-neutrality-and-first-mover-half.md`
   (Lemma A, generalized block form) is built to handle — **this looks like
   the right tool to formalize the plateau**, not previously connected to
   this specific gap in the write-ups I read.
4. **The function is neither globally convex nor globally concave** in the
   transfer parameter (numerically: second differences change sign), so a
   naive "OddSum is convex in the split, hence minimized at an extreme
   point of the split simplex" argument does **not** work as stated — this
   rules out the simplest possible closing move and should be flagged as a
   dead end *before* it's tried, not after.
5. Equal ("uniform") subdivision of $r_n$ is *not* extremal — it gives a
   strictly higher OddSum than the self-similar split (e.g. $n=3$: equal
   split gives $0.6$, self-similar split gives exactly $8/15=0.5333$) —
   confirms the round-1 finding that no simple "aggregate" or "spread"
   heuristic (majorization-style "most spread wins") identifies the worst
   case; the specific *geometric ratio* matters, not just how many pieces
   or how equal they are.

### Distinct openings for the outliner

- **(A) Reduce to top-piece-only splits first, then attack that
  sub-problem.** Numerical evidence (point 2 above) supports a genuinely
  provable-looking sub-lemma: *"among all ways to distribute $\le n$ cuts,
  concentrating all cuts on $r_n$ is weakly worst for LB (minimizes
  OddSum), for any fixed number of cuts spent."* If this sub-lemma can be
  proved (e.g. by an exchange argument: moving a cut from a smaller piece
  to the largest piece never increases XY's damage — this feels close to
  provable via the Peeling Lemma applied recursively, comparing "cut spent
  on $r_i$, $i<n$" vs "cut spent on $r_n$" and showing the latter dominates
  by an exchange), it would collapse Case 2 to the single question: for
  splitting $r_n$ alone into $\le n+1$ arbitrary fragments (rest of the
  partition untouched), is OddSum(fragments $\cup$ untouched rest) $\ge
  c(n)$ always? This is a strictly smaller, more tractable claim than the
  full Case 2.
- **(B) Prove the plateau/tie characterization directly.** Since minimum is
  attained on a face (point 3), try to show: *any* split of $r_n$ can be
  continuously deformed (moving mass between two fragments, using the
  Tie-neutrality lemma to control the crossing points) toward the
  self-similar split without ever *decreasing* OddSum, terminating either
  at the self-similar split itself or at a tie-boundary where a fragment
  exactly equals some $r_i$ — then finitely many "boundary" configurations
  need to be checked by hand/induction. This uses `tie-neutrality-and-first-
  mover-half.md`'s generalized block form as the mechanism for the flat
  segments, and would give a genuinely new inductive structure not
  attempted by any of the 3 live approaches' write-ups (which reason via
  either aggregate bounds — refuted — or a specific chosen split).
- **(C) Attack via the merge/interleaving structure explicitly** (what
  `greedy-reduction-geometric` Section 4 flags as needed): write the merged
  sorted sequence's OddSum as a sum over *rank-blocks* determined by how
  the $n+1-j$ fragments of $r_n$ interleave with the untouched
  $r_0,\dots,r_{n-1}$, and set up strong induction on $n$ using the fact
  that $r_0,\dots,r_{n-1}$ is *itself* the geometric-$(n-1)$ construction
  scaled by $R=c(n)-r_0$ — i.e. push the self-similar-induction-on-n
  approach's recursion through to the fully general split, using the
  now-certified tie-neutrality block lemma to close its documented j=1
  three-way-tie gap as a template for the general-$j$ case.
- **(D) Revive dyadic-potential-invariant with a narrower target.** Its
  central "local split monotonicity" claim is currently undesigned/unverified
  and flagged by round 1 as the riskiest approach. Given the plateau finding
  (point 3), a potential/credit argument built around rank *blocks* (not
  single pieces) might be salvageable — but this is speculative; do not
  invest heavily unless (A)-(C) stall again.

### Cheap-kill candidates
- Global convexity of OddSum in the split parameters: **refuted**
  numerically (point 4) — do not let a builder waste a round rediscovering
  this.
- "Most spread among fragments is worst for LB" (majorization-style):
  **refuted** (point 5, equal split is not extremal) — already flagged in
  round 1 as well; independently re-confirmed here.
- "Sum of top two elements of the merge $\ge r_n$" as an aggregate
  sufficient condition: already refuted in `greedy-reduction-geometric.md`
  Section 4 with an explicit $n=3$ counterexample — do not retry.

### Knowledge-base entries to use
- `lemmas/dominant-piece-lower-bound.md` (Global-max peeling identity) —
  the base tool; needs to be applied *recursively/inductively* for Case 2,
  not just once.
- `lemmas/tie-neutrality-and-first-mover-half.md` — Lemma A's generalized
  block form is, per this exploration, the natural tool to formalize the
  plateau/tie structure found numerically (point 3); currently
  under-exploited outside the specific j=1 gap in self-similar-induction.
- `lemmas/reduction-to-multiset-minimax.md` — unchanged, foundational.
- `knowledge_base.md`'s standard-inequalities entry (rearrangement/AM-GM
  family) is too coarse by itself (matches the refuted convexity/aggregate
  attempts above); no other KB entry looked more specific to this gap.

### Analogous past problems (cruxes)
- `aimo-0117` (Dutch TST, "Jesse en Tjeerd") — subtopic
  games-and-strategy: crux move "assign values as a two-sided
  geometric/dyadic sequence so the single largest value strictly exceeds
  the sum of all the others." This is exactly the dominant-piece mechanism
  already extracted into `dominant-piece-lower-bound.md` and is the
  inspiration for the (currently stalled) `dyadic-potential-invariant`
  approach. It is a real analogy for Case 1 but does **not** by itself
  address Case 2 (splitting the dominant piece) — I looked at the corpus
  broadly (games-and-strategy, invariants-and-monovariants,
  extremal-principle subtopics) and found no crux that handles "split the
  largest element of a geometric sequence and re-rank" specifically; this
  step appears to be genuinely novel to this problem.
- `aimo-0146` (combinatorics, extremal-principle/double-counting) — crux
  "maximize a fixed weighted sum of a sorted sequence under a sum
  constraint by exchange-smoothing weight toward the higher-weight side."
  Same general flavor (weighted sum of a sorted sequence, exchange
  argument) as opening (A)/(B) above — worth reading as a template for
  how an exchange/smoothing argument is normally written up, but the
  weight structure there (monotone weights) is simpler than OddSum's
  alternating (1,0,1,0,...) weights, so it is not a drop-in solution.
- No crux found that closes a "split the max piece of a fixed geometric
  sequence and prove a rank-sum floor" style gap directly — this really
  does look like the paper's own hard step, not a known trick.

### Prior progress
See `results/imo-2026-03/current.md` — reduction, Case 1, and $n=0,1$ fully
proved; Case 2 (this gap) and the general upper bound remain open. Nothing
in this exploration closes Case 2, but points 1–3 above give concrete,
numerically-grounded structure (the plateau, and the reduction-to-top-piece-
only conjecture) that no prior approach file documents explicitly.

### Dead ends (do not retry)
- Aggregate/global convexity of OddSum in split parameters (refuted here,
  point 4).
- "Most spread is worst" / majorization heuristic (refuted, round 1 and
  reconfirmed here, point 5).
- "Top-two-elements-sum $\ge r_n$" aggregate bound (refuted in
  `greedy-reduction-geometric.md`, reconfirmed consistent here).
- Pure bisection / unconditional self-similar-split-everywhere as a
  *universal* XY rule (that's the upper-bound gap, not this one, but
  already refuted in round 1 — listed for completeness, not to be
  re-tried under this gap either).

### Small-case / intuition notes (all conjecture, numerically checked only)
- The worst case for XY, restricted to spending all its cuts on $r_n$
  alone, is (at least among local perturbations, $n=2,3,4,5$ checked) the
  exact self-similar split $q_i=r_n\cdot 2^i/(2^{n+1}-1)$ — a genuine local
  minimum of OddSum, confirmed by perturbation sweeps with no
  OddSum-decreasing direction found in 2000+ random perturbation trials
  per $n$.
- The minimizing set is not a single point but an interval/face (point 3);
  multiple distinct cut-allocations reach the exact floor $c(n)$ (point 2).
  Any inductive proof should expect to handle this plateau, not a unique
  extremizer — this is likely why previous "identify the one worst
  response and prove it's worst" attempts stalled.
- No evidence found (up to $n=5$, extensive random + gradient search) of
  any XY response beating $c(n)$ — consistent with (but not proof of) the
  closed form $c(n)=2^n/(2^{n+1}-1)$ standing.
