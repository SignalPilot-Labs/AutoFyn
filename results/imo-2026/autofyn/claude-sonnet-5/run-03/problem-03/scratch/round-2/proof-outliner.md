## imo-2026-03

All four approaches share the certified reduction (`lemmas/reduction-to-multiset-minimax.md`)
and Greedy-Optimality (`lemmas/greedy-optimality-oddsum.md`): the problem is
$$c(n)=\max_{p_1,\dots,p_k>0,\ k\le n+1,\ \sum p_i=1}\ \min_{\text{refinement, }\le n\text{ cuts}}\ \mathrm{OddSum}(\text{multiset}),$$
conjectured (and proved for $n=0,1$) to equal $2^n/(2^{n+1}-1)$, attained by
$p_i=2^i/(2^{n+1}-1)$. The freshframing explorer confirmed no top-level
framing avoids this reduction — it is forced by the problem's literal rules,
not a technique choice — so all revisions below stay inside it and attack the
two remaining shared gaps (lower-bound Case 2; general upper bound) with new
mechanisms surfaced this round, per the lowerbound/upperbound explorers.

---

### greedy-reduction-geometric: revise

Target: full problem, both directions (this file's job this round: close
**Lower-bound Case 2** — when XY spends cuts on LB's own geometric top piece
$r_n$, prove $\mathrm{OddSum}\ge c(n)$ for *every* split, every $n\ge2$).

Technique: two-stage reduction — an **exchange argument** to reduce "any cut
allocation" to "all cuts on $r_n$ alone," then a **piecewise-linear /
tie-block** analysis of splits of $r_n$ alone, using the certified
generalized Tie-neutrality block lemma. (Opening (A)+(B) from
`math-explorer-lowerbound.md`.)

Skeleton:
1. **Exchange Lemma.** For the geometric partition, moving one cut from any
   $r_i$ ($i<n$) to $r_n$ weakly decreases $\mathrm{OddSum}$ (weakly worse
   for LB) — by comparing the two resulting multisets rank-by-rank (a
   cut spent splitting $r_n$ can demote at most the fragments of $r_n$
   itself past untouched lower pieces, while a cut spent on $r_i$ only
   perturbs ranks strictly below $r_n$'s own rank, which by Case 1's
   domination argument never touches LB's guaranteed floor at rank 1).
   Consequence: it suffices to prove the bound when **all $n$ cuts land on
   $r_n$**, since any other allocation gives $\mathrm{OddSum}$ at least as
   large.
2. **Piecewise-linearity of $\mathrm{OddSum}$ in the split of $r_n$.**
   Parametrize splits of $r_n$ into $n+1$ positive fragments
   $q_0,\dots,q_n$ summing to $r_n$. As the $q_i$ vary continuously, the
   sorted order of the full multiset $\{q_0,\dots,q_n\}\cup\{r_0,\dots,r_{n-1}\}$
   changes only at codimension-1 walls where some $q_i$ ties some $r_j$
   (or another $q_{i'}$); between walls, $\mathrm{OddSum}$ is a fixed linear
   functional of the $q_i$ (a 0/1-weighted sum determined by the fixed
   sort order), hence **piecewise linear with breakpoints exactly at
   ties** — matching the explorer's numeric finding (point 3,
   `math-explorer-lowerbound.md`) and ruling out the previously-tried
   convexity shortcut (already refuted, do not retry).
3. **Minimum-value floor at every breakpoint face, by induction on $n$.**
   At any tie-boundary, invoke the generalized Tie-neutrality block lemma
   (`lemmas/tie-neutrality-and-first-mover-half.md`, Lemma A's block form)
   to compute $\mathrm{OddSum}$ exactly on that face as a rank-determined
   sum, independent of tie-breaking. Show every breakpoint face's value is
   $\ge c(n)$: the two extreme faces are (i) the self-similar split
   $q_i=r_n\cdot2^i/(2^{n+1}-1)$, which gives exactly $c(n)$ (already
   proved, `universal-halving-adversary`'s duplicate-the-rest computation
   is the same identity run in reverse), and (ii) all other breakpoint
   faces reduce, via the untouched tail being exactly the geometric-$(n-1)$
   construction scaled by $R=c(n)-r_0$, to an $(n-1)$-level instance of the
   *same* claim by the inductive hypothesis — formalize this reduction
   precisely (which piece of the tail plays the role of "top" at each
   face) rather than asserting it.
4. Combine 1–3: for any XY cut allocation, $\mathrm{OddSum}\ge$ (value for
   all-cuts-on-top) $\ge \min$ over breakpoint faces $\ge c(n)$.

Key lemmas (claim + mechanism):
  - Exchange Lemma — because a cut on $r_i$ ($i<n$) can only perturb ranks
    strictly below the dominant piece's rank, while $r_n$'s split is the
    only lever that can threaten rank 1 itself; formal proof needed via
    the Peeling Lemma applied to both scenarios.
  - Piecewise-linearity with breakpoints at ties — because $\mathrm{OddSum}$
    is a fixed 0/1-selection linear functional of the multiset between
    sort-order changes, and sort order changes only at coordinate
    equalities.
  - Inductive floor at breakpoints — because the untouched tail
    $r_0,\dots,r_{n-1}$ is literally $R\cdot$(geometric-$(n-1)$
    construction), so any face reduces to the $(n-1)$ case by scale
    invariance (`lemmas/reduction-to-multiset-minimax.md`'s scale-invariance
    corollary).

Open gaps: Exchange Lemma (step 1) not yet proven, only motivated; the
breakpoint induction (step 3) needs the reduction made precise at every
face, not just the two extremes — the explorer found the extremal set is a
*plateau*, not a point, so "check the endpoints" is not automatically
sufficient without checking the whole face is covered by the inductive
argument.

Cases to cover: the plateau of multiple distinct extremal allocations found
numerically (point 2, lowerbound explorer) — the proof must show *every*
point on the minimal face is $\ge c(n)$ (with equality only on the specific
faces identified), not just exhibit one minimizer.

Watch out for: convexity/aggregate shortcuts are refuted (do not retry);
the "top-two-elements-sum" and "most spread" heuristics are refuted
(do not retry, see lowerbound explorer's Dead ends).

---

### self-similar-induction-on-n: revise

Target: full problem via whole-game recursion (this file's job: close the
documented $j=1$ three-way-tie gap rigorously, and extend to general $j$ via
a genuine nested induction). (Opening (C) from `math-explorer-lowerbound.md`.)

Technique: strong induction on $m$ (the recursion parameter), using the
Global-max Peeling Lemma repeatedly plus the certified generalized
Tie-neutrality block lemma to handle all ties exactly.

Skeleton:
1. **Close the $j=1$ gap.** Redo the $j=1$ (top bisected into $T/2,T/2$)
   computation invoking `lemmas/tie-neutrality-and-first-mover-half.md`
   Lemma A's block form explicitly at the point where $T/2$ ties the tail's
   own top piece $2^{m-1}$: the tie occupies two consecutive ranks
   regardless of which physical copy is "LB's bisected half" vs "the tail's
   own piece," so the value is rank-determined and the previously-flagged
   ambiguity is resolved with no case split needed — write this out fully
   (the mechanism is already certified; only the specific instantiation was
   missing).
2. **General $j\ge2$: nested induction via repeated peeling.** For XY
   spending $j$ cuts on the top piece $T=2^m$ (arbitrary fragment values)
   and $m-j$ cuts on the tail, apply the Global-max Peeling Lemma
   repeatedly: at each step, remove the current largest unclaimed piece
   $g$ (whichever fragment or tail-piece currently tops the sort), giving
   $\mathrm{OddSum}(M)=g+\mathrm{EvenSum}(M\setminus\{g\})$, and recurse on
   $M\setminus\{g\}$ with the mover switched. This produces a fully general
   recursive decomposition, not tied to a specific split shape.
3. **The genuinely new difficulty: bound $\mathrm{EvenSum}$ of the
   remainder from *below*, which requires an *upper* bound on
   $\mathrm{OddSum}$ of the remainder at intermediate steps** (since
   $\mathrm{EvenSum}(M')=\mathrm{sum}(M')-\mathrm{OddSum}(M')$). This means
   the induction must carry **two-sided** bounds (both a proven upper bound
   $\mathrm{OddSum}(M')\le U(m')$ and the target lower bound
   $\mathrm{OddSum}(M')\ge c(m')\cdot\mathrm{sum}(M')$) through the
   recursion simultaneously — a strictly stronger inductive hypothesis than
   round 1's one-sided statement. State and attempt this two-sided
   induction explicitly; if $U(m')$ cannot be pinned down tightly enough
   (e.g. $U(m')=\mathrm{sum}(M')$ trivially is too weak), report this as
   the specific blocking sub-gap rather than leaving it implicit.
4. Ground the induction at the $j=0$ base case (already proven, Case 1
   lemma) and at $n=0,1$ (already proven exactly).

Key lemmas (claim + mechanism):
  - Generalized Tie-neutrality block instantiation for the $j=1$ case —
    because the two tied values ($T/2$ and $2^{m-1}$) are numerically
    identical by the geometric construction's own arithmetic, so they
    occupy consecutive ranks and split 1–1 regardless of tie-break choice.
  - Repeated Peeling recursion — because $\mathrm{OddSum}(M)=g+\mathrm{EvenSum}(M\setminus g)$
    holds for any multiset with $g=\max(M)$, applicable at every step, not
    just once.
  - Two-sided induction requirement (new this round) — because a lower
    bound on $\mathrm{OddSum}$ of the *original* multiset unwinds, via
    Peeling, into needing an *upper* bound on $\mathrm{OddSum}$ of a
    sub-multiset one level down; a purely one-sided inductive hypothesis is
    structurally insufficient, which is *why* round 1's approach stalled at
    $j\ge2$ without saying so explicitly.

Open gaps: step 3's two-sided induction is new and entirely open — no upper
bound $U(m')$ has been formulated or verified yet. If it turns out
intractable, this approach's most valuable output may end up being exactly
this diagnosis (report clearly) plus the closed $j=1$ gap, deferring the
lower-bound Case 2 to `greedy-reduction-geometric`'s exchange-argument route
instead.

Cases to cover: $j=0$ (proved), $j=1$ (closeable this round via step 1),
$j\ge2$ general (open, step 2–3).

Watch out for: do not silently drop back to a one-sided bound partway
through the recursion — that is exactly the gap that made round 1's write-up
incomplete; state explicitly at each recursive step which bound (upper or
lower) is being invoked and on which sub-multiset.

---

### universal-halving-adversary: revise

Target: full problem (this file's job: close the **general upper bound** —
an XY response, $\le n$ cuts, forcing $\mathrm{OddSum}\le c(n)$ against
*every* LB partition, $n\ge2$). (Openings (2) and (3) from
`math-explorer-upperbound.md`.)

Technique: generalize "duplicate-the-rest" from a single top-vs-rest match
to a **recursive tie-matching algorithm** across all ranks, using the
certified Tie-neutrality block lemma; keep the **surrogate-adversary**
technique (crux `aimo-0560`) as a documented backup mechanism.

Skeleton:
1. **Certify the pruning lemma first** (cheap, flagged independently by
   both explorers): LB's optimum always uses its full budget ($k=n+1$
   pieces). Prove via a direct exchange/continuity argument: given a
   $k<n+1$-piece partition, LB can always weakly improve by an
   infinitesimal split of one piece into two (this only refines the
   multiset, and refining a piece while holding the rest fixed can only
   weakly increase $\mathrm{OddSum}$ against any *fixed* refinement rule —
   needs a from-scratch inequality, not assumed). This shrinks the upper-
   bound problem to sorted lists $p_1\ge\cdots\ge p_{n+1}>0$ exactly.
2. **Recursive tie-matching algorithm.** Given sorted $p_1\ge\cdots\ge p_{n+1}$
   and budget $n$, define XY's response recursively from the top: scan
   ranks $1,2,\dots$; whenever $p_i$ and $p_{i+1}$ are not already tied,
   spend one cut splitting $p_i$ to create a value tied with $p_{i+1}$ (or
   with the sum of several trailing pieces, generalizing "duplicate-the-
   rest" — the exact target value to split off is the open design
   parameter, guided by the explorer's finding that XY should "create as
   many Tie-neutrality-eligible matched pairs as possible," point 2 of
   `math-explorer-upperbound.md`), then recurse on the remaining unmatched
   suffix with one less cut available. Each created tie-block is handled
   exactly (no hand-waving) by the certified Tie-neutrality block lemma.
3. **Inductive budget/value accounting.** Prove by strong induction on $n$
   that this algorithm never exceeds its $n$-cut budget and always achieves
   $\mathrm{OddSum}\le c(n)$ — the inductive step must show that after
   matching off the top block, the residual sub-problem (fewer pieces,
   fewer cuts, rescaled total) satisfies the $(n-1)$-level bound by
   hypothesis, with an explicit accounting identity (analogous to
   `greedy-reduction-geometric`'s telescoping computation) tying the
   matched block's contribution plus the residual's inductive bound to
   $c(n)$ exactly.
4. **Backup: surrogate-adversary mechanism** (crux `aimo-0560`, opening 3).
   If step 2–3 stalls, define a surrogate XY with a relaxed move
   ("merge-claim": may treat any two pieces as pre-tied for accounting
   purposes without physically cutting), show the surrogate's value is a
   provable upper bound on the real XY's achievable value (since a real
   cut can approximate any merge-claim to within $\epsilon$, and
   $\mathrm{OddSum}$ is continuous in the piece lengths), and show the
   surrogate's minimax reduces to a simpler, more tractable combinatorial
   optimization (e.g. a matching/majorization problem with no budget
   granularity issues) that can be bounded by $c(n)$ directly.

Key lemmas (claim + mechanism):
  - Pruning lemma — because refining a piece into two (holding total fixed)
    weakly increases the refiner's own optimal claim value under best
    response, by a continuity/exchange argument to be proven from scratch
    (not yet done, despite being "obviously true" numerically).
  - Recursive matching's per-block budget bound — because each tie-block,
    once created, is settled exactly and independently by the Tie-
    neutrality block lemma, so the recursion's cut cost is additive across
    blocks.
  - Surrogate domination — because any merge-claim can be realized as a
    limit of actual $\epsilon$-splits, and $\mathrm{OddSum}$ is continuous,
    so the surrogate's guaranteed value is achievable (up to $\epsilon$,
    hence exactly by a compactness/limiting argument) by the real XY.

Open gaps: the exact target value each cut should split off in step 2 is
undesigned — this is genuinely new content, must be numerically stress-
tested (per repo Rule) against the known counterexamples
$(0.5,0.3,0.2)$ at $n=2$ and the near-balanced $(0.45,0.45,0.1)$ case
*before* being written up as a lemma. Step 4 is wholly untested and should
only be pursued if step 2–3 stalls.

Cases to cover: near-tied top pieces (matching should do nothing there,
per the explorer's finding); a clear-outlier top piece (matching should
degenerate to duplicate-the-rest); intermediate regimes (the hard case, not
covered by either extreme).

Watch out for: do NOT re-try "look only at $p_1$" threshold rules — refuted
twice now (round 1 and reconfirmed by upperbound explorer at
$(0.5,0.3,0.2)$); the algorithm must inspect multiple ranks.

---

### dyadic-potential-invariant: revise (reframe — low priority, exploratory)

The freshframing explorer **numerically refuted** this approach's core
mechanism (local per-split monotonicity of $\mathrm{OddSum}$ under a
credit-weight potential): splitting a piece can *decrease* OddSum sharply
and globally (explicit counterexamples, deltas up to $-0.37$), so step 2 of
the round-1 skeleton is dead as stated and must not be attempted again in
that form. Per dispatch, this file is revised — not dropped outright — to
the one genuinely distinct idea surfaced this round: a **minimax-duality
certificate** unifying both bounds. This is explicitly speculative;
treat as the lowest-priority member of the field and drop for good next
round if it produces no concrete inequality.

Target: full problem, both directions simultaneously, via one certificate
object rather than two separately-built arguments.

Technique: von-Neumann-style minimax duality / certificate argument.

Skeleton:
1. Take the geometric partition's own alternation pattern as the
   certificate: $w=(w_0,\dots,w_n)\in\{0,1\}^{n+1}$, $w_i=1$ iff LB claims
   $r_i$ under the greedy rule (odd rank in the geometric sequence's own
   sort, i.e. $w_i=1$ for $i=n,n-2,n-4,\dots$).
2. Attempt to construct a **coupling/majorization inequality**: for any
   reachable final multiset $M$ (from any LB partition under best-response
   XY), match $M$'s elements against the geometric sequence's elements
   (length-for-length, e.g. by matching sorted order) and show
   $\mathrm{OddSum}(M)\le\sum w_i r_i=c(n)$ via a term-by-term domination —
   this is the central unproven claim; no candidate inequality has been
   written down or numerically checked yet.
3. Symmetrically attempt the lower-bound direction from the same $w$: show
   $w$ also certifies that the geometric partition's own value against any
   XY response is $\ge c(n)$ (this direction is *already proven* by
   `greedy-reduction-geometric`'s Case 1 + the duplicate-the-rest identity
   — so step 3 is really "re-derive the known result from the certificate,"
   a sanity check that the certificate object is coherent, not new work).

Key lemmas (claim + mechanism): the coupling/majorization inequality of
step 2 is entirely undesigned — flagged explicitly as the single unproven
crux, high risk, not yet checked even numerically.

Open gaps: everything in step 2. If constructing this certificate turns
out to require re-deriving the OddSum minimax facts directly (as the
freshframing explorer warns is likely), the builder must report this
collapse explicitly and leave Status honestly at `unsolved` for this file
rather than force a proof.

Cases to cover: none yet identified — design work only this round.

Watch out for: do not resurrect the refuted local-split-monotonicity
mechanism (step 2 of the round-1 skeleton) under a different name; if the
builder finds itself re-deriving a per-split inequality, that is the dead
mechanism recurring and should be abandoned immediately, not patched.

---

build set: greedy-reduction-geometric, self-similar-induction-on-n, universal-halving-adversary, dyadic-potential-invariant
