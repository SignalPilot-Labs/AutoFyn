## imo-2026-03 — lens: inequality (7.9.1) in rank-pigeonhole-budget §7.9

### What (7.9.1) actually is, precisely restated
Setup (from `results/imo-2026-03/approaches/rank-pigeonhole-budget.md` §7.9,
verified by re-reading, not re-derived from scratch): in the T'-cuts-p4,
b=c2 sub-case, T'=\{c1,c2\}∪T''' with c1≥c2>0, c1+c2=p4 (so c1∈[p4/2,p4)),
and **T''' is a legal refinement of the tail \{p5,...,p_{n+1}\} using ≤n-5
cuts**. The needed bound is
$$A(T''')\ \le\ c_1-f(n).\tag{7.9.1}$$

### 1. What T''' actually is — characterized precisely
T''' is **not** an arbitrary multiset. \{p5,...,p_{n+1}\} is itself an exact
rescaled copy of the unit **(n-3)-ladder** (`general-cross-level-rescaling-lemma`,
k=4 gives λ4·unit-(n-4)-ladder for \{p5,...\}; equivalently it is the tail one
level further down than p4). Writing m := n-3 (the tail's own length) and
k := n-5 = m-2, **T''' is exactly a legal Xiang-Yu response to an
m-element ladder using only m-2 of its full m-cut budget** (2 cuts short
of the maximum). This is structurally *identical in shape* to the objects
`greedy-halving-adversary`'s Claim B machinery already targets (bound on
A of a budget-capped legal refinement of a ladder), and to the general
upper-bound target `lp-duality-certificate` has been chasing for the
*arbitrary*-marking case — except here the marking is fixed to be a pure
ladder, which is the easier (already-partially-solved-elsewhere) regime.
So (7.9.1) is not a free-standing mystery inequality — it is a
budget-capped Claim-B-shaped statement with a specific numerical deficit
of exactly 2 cuts from full budget.

### 2. Numerical verdict: (7.9.1) is TRUE and appears to be an exact IDENTITY (tight equality), not a strict inequality with slack
Checked with exact `Fraction` arithmetic (no floats) for n=5..14 at the
hardest point (symmetric split c1=c2=p4/2, since a larger c1 only makes
the right side bigger and is easier):
- n=5,6: with T''' left fully untouched (budget 0/1 barely used),
  A(T''')=c1-f(n) EXACTLY.
- n=7,8: exhaustive/near-exhaustive search over ALL cut-count compositions
  among the m tail pieces, each optimized with `scipy.differential_evolution`
  (many restarts, high precision, exact-Fraction cross-check at the winning
  configuration) finds the **true global maximum of A(T''') equals c1-f(n)
  to machine precision** (residual ~1e-18), achieved by putting **all**
  n-5 spare cuts on the tail's **second** element (p6), leaving p5 and
  p7,...,p_{n+1} completely untouched.
- n=9,10: repeated the full composition sweep (126 and more compositions,
  each globally optimized) — same result: true max = c1-f(n) exactly
  (margin 0 to numerical precision), same winning shape (all cuts on p6
  alone).
- n=9 exact-Fraction spot check: c1-f(n)=1/33; DE's found optimum
  = 0.0303030303...=1/33 exactly.
- **Exact rational vertex identification at n=8** (fine grid + exact
  Fraction re-scoring): the optimal 3-cut split of p6 produces fragments
  \{1/2555, 1/511, 2/511, 24/2555\}·(nothing, these are absolute values);
  crucially **two of the four fragments exactly tie p7=2/511 and p8=1/511**
  (existing tail values) — i.e. the maximizer is a genuine LP/tie vertex
  in the sense of the project's certified Vertex-Minimum/Maximum Theorem,
  not an arbitrary interior point.

**Honest scope of this evidence**: this is strong numerical/computational
evidence (exact-Fraction-verified at the winning point, global-optimizer-
verified for the search itself) that (7.9.1) is TRUE with equality as the
tight case — not a proof. The DE optimizer is a heuristic global search;
I did not prove no composition beats the p6-only-cuts vertex. But the
consistency across n=7,8,9,10 (four independent full sweeps, same winning
structure each time, exact match to the target down to the last digit)
is much stronger than a single spot-check.

**Suggested fix / gap-closing direction (not attempted, per role
boundaries):** since the extremal configuration is (a) all spare budget
concentrated on ONE non-dominant tail piece (p6), (b) an exact LP/tie
vertex (fragments tie existing tail values), this looks directly amenable
to the SAME machinery already certified in this project: apply
`vertex-minimum-theorem`/`single-insert-point-vertex-lemma` dualized to
the MAX direction (exactly the dualization `exchange-smoothing-vertex-
maximization` already performed once, round 8, to close Claim A's Case I)
to the restricted polytope "vary only p6's own split, rest of the tail
fixed." If a max-direction vertex theorem pins the optimum to concentrating
cuts on a single element and evaluates it via `odd-run-reduction-lemma`,
(7.9.1) would follow as a genuine sharp identity — likely a bounded,
tractable sub-problem (only ONE tail element is free, not the whole tail),
much smaller in scope than the standing general cross-piece vertex
enumeration obstruction.

### 3. Overlap with the parallel T'-cuts-p4 exploration this round
(7.9.1)'s content — "bound A of a budget-capped legal refinement of a
ladder tail" — is *exactly* the shape of `greedy-halving-adversary`'s
long-running Claim B target (Truncated Alternating Sum Ceiling,
Upper-Truncation Identity, Theorem 32, Theorem 35a/35b, all bound
A(refinement)-type quantities for ladder tails under a cut-budget cap).
Flag this overlap explicitly to the outliner: **do not let two builders
independently re-derive the same budget-capped-ladder-refinement bound
under two different names.** Concretely worth checking next round: does
substituting v := c1, tail := \{p5,...,p_{n+1}\}, budget := n-5 into
`greedy-halving-adversary`'s already-certified Truncated Alternating Sum
Ceiling / Upper-Truncation-Identity machinery directly produce (7.9.1),
or a corrected/tightened version of it? (I confirmed the *cheap* form of
the Ceiling, A(S)≤v+2A(S_{>v}), is too weak here since S_{>v}=∅ at v=c1
just gives A(T''')≤c1, missing the -f(n) sharpening — so the *literal*
Ceiling lemma alone doesn't close it, matching rank-pigeonhole-budget's
own finding that cheap bounds fail; but the *sharper* machinery
underlying Theorem 32/35a — which explicitly builds in the ladder's
recursive structure via induction hypotheses $(\star_m)$ — has not yet
been tried on this specific object and is the most promising existing
toolkit to reuse rather than reinvent.)

### 4. Knowledge base / crux corpus
`knowledge_base.md`'s Combinatorics / General Proof Methods / Extremal
Principle entries are the same generic vertex/extremal-optimization
entries already cited throughout this project (LP-vertex/exchange
argument, extremal principle) — nothing new beyond what's already in use.
No entry specifically addresses "maximize an alternating sum over a
budget-capped refinement of one element of a fixed multiset," which is
exactly the missing piece.

Crux corpus: consistent with round 4's finding (recorded in
`/tmp/memory/run_state.md` Rules) that games-and-strategy /
extremal-principle / processes-and-algorithms subtopics have **no**
strong direct analog for this superincreasing-ladder claiming game — I
did not find a new candidate this round either (spent limited time here
since this has been checked exhaustively in prior rounds with a
consistent negative result; re-querying the same subtopics would not add
information). If the outliner wants a corpus lead specifically for
"single-element budget-capped extremal splitting to tie existing values,"
that is closer to `pigeonhole` / `size-bounding-and-descent` in
combinatorics, but I did not find a matching crux this round given the
time budget — flagging as unexplored rather than exhausted.

### 5. Cheap-kill candidates
- **Symmetry/monotonicity check (done, negative)**: making c1 larger than
  c1=c2=p4/2 only shrinks the right side's slack requirement further in
  Liu Bang's favor (rhs=c1-f(n) grows), so the symmetric split is
  confirmed (not just assumed) to be the hardest case — no need to check
  asymmetric c1 separately once the symmetric case is closed.
- **Parity/size bound**: none obvious beyond the already-identified
  tie-vertex structure (§2 above).
- **Small-n exhaustive check**: n=5,6 are FULLY tight with T''' completely
  untouched (0 or 1 spare cut) — these are free/trivial cases already
  implicitly covered by rank-pigeonhole-budget's existing $(\star_{n-3})$
  induction machinery; only n≥7 genuinely exercises T'''-internal
  splitting.

### Summary for outliner
- (7.9.1) is TRUE (strong exact + numeric evidence, not proof) and TIGHT
  (equality, not slack) — this is good news: it should be provable as an
  exact identity/theorem in the same style as `Cascading-Halving-Family
  Theorem` or `Case I Closure Theorem`, not chased as an open-ended
  inequality.
- The extremal configuration is fully characterized numerically: concentrate
  ALL n-5 spare cuts on the tail's SECOND element p6 (not p5, not spread
  out); the resulting optimal split is a genuine tie-vertex (fragments tie
  existing tail values p7, p8, ...).
- This is structurally the SAME target as `greedy-halving-adversary`'s
  Claim B (budget-capped ladder-tail-refinement bound) — recommend the
  outliner route this to whichever builder has the freshest Claim-B
  machinery (Truncated Alternating Sum Ceiling / Upper-Truncation Identity
  / Theorem 32/35a lineage), reusing `single-insert-point-vertex-lemma`
  dualized to MAX (as `exchange-smoothing-vertex-maximization` was for
  Case I), rather than treating it as a from-scratch obstruction.
- No crux-corpus or knowledge-base analog beyond what's already cited
  project-wide; nothing new to import from outside.

### Candidate technique(s)
Dualize the certified max-direction vertex-maximization machinery
(`vertex-minimum-theorem` + `odd-run-reduction-lemma`, already dualized
once for Case I Closure Theorem) to the restricted 1-free-element polytope
("vary only p6's split, rest of tail fixed") via
`single-insert-point-vertex-lemma`'s technique (already proves vertices
are pinned to \{0, M, existing-fragment-ties\} for a *single* inserted
point — here generalize from 1 inserted point to k=n-5 inserted points
splitting one fixed element, all within an otherwise-untouched tail).

### Dead ends (do not retry)
- The cheap bound A(T''')≤Total(T''') — confirmed insufficient (already on
  file, re-confirmed here).
- The generic "refining a ratio-2 tail can only decrease A" monotonicity —
  already on file as FALSE in general (round 12+); do not re-invoke it as
  a shortcut for (7.9.1) specifically either (the true extremal
  configuration here is *interior* splitting on one element, not "leave
  untouched," so a blanket monotonicity claim would be the wrong shape
  even if it were true).

### Small-case / intuition notes (labeled conjectural)
Conjectured (numerically strong, not proved): for every n≥5,
$$\max_{T'''}A(T''')\ =\ c_1-f(n)\quad\text{exactly, at symmetric }c_1=p_4/2,$$
attained uniquely (up to the usual ladder symmetries) by putting the
entire spare budget n-5 on the tail's second element p6 and leaving every
other tail element untouched. This is a *conjecture based on exact-Fraction
identity checks at n=5,6 and global-optimizer + exact-Fraction spot checks
at n=7,8,9,10*, not a proof for general n.
