## imo-2026-03 — scouting the "Lemma X'" gap (j≥2 in self-similar-induction-on-n)

### Summary of the diagnosis I re-verified
Read `current.md`, `approaches/self-similar-induction-on-n.md` (Step 3), and
`lemmas/element-bound-and-j1-theorem.md`. Round 2's obstruction claim checks
out: peeling the top-fragment $a_1$ (when it dominates) reduces the $j=2$
target to needing $\mathrm{OddSum}(\{a_2,a_3\}\cup S)\le R$, and the natural
next peel is **not** guaranteed to hit an element of $\{a_2,a_3\}$ — it can
just as well hit the tail's own untouched top piece $s_1=2^{m-1}=T/2$ (this
is the generic case, not an edge case: e.g. $m=3$, minimal example found
below has $a_1\approx4.24>4=s_1$, but after peeling $a_1$ the very next max
is $s_1=4$, not $a_2$ or $a_3$). So the "peel one A-fragment then use
$T(m-1)$" template genuinely breaks down starting at the *second* peel, for
a structural reason, not a proof gap.

### Numeric probes (Python, brute/random search — all conjectural evidence, not proof)

1. **The target bound itself holds with correct budget.** For $j=2$ splits
   of $\Gamma_m$'s top piece with the *correctly restricted* tail budget
   ($\le m-2$ cuts), random search over $m=2,3,4,5$ (1,000,000 trials) found
   minimum $\mathrm{OddSum}-2^m = 0.0$ (attained, never negative). Confirms
   $T(m,j{=}2)$ is true, not just conjectured to be provable — the gap is
   purely in the *proof method*, matching round 2's framing.
   - Earlier control run with an *incorrectly inflated* tail budget (a bug
     in my first script, allowing $m-1$ tail cuts instead of $m-2$ when
     $j=2$) DID find a violation ($\mathrm{OddSum}=3.51<4$ at $m=2$). This
     is not a counterexample to the theorem — it's outside the actual rules
     — but it is a useful sanity flag: **the true statement is fragile to
     the exact budget accounting** ($k-j\le m-j$, not $\le m-1$), so any
     future write-up of $T(m,k)$ for $j\ge2$ must track the budget
     bookkeeping as carefully as round 2 did for $j=1$.

2. **Lemma X′ as literally stated is FALSE in general.** I tested the
   round-2 write-up's precise statement — "if $\mathrm{sum}(A')=T'$ and
   $\mathrm{EvenSum}(S')\ge T'/2$ then $\mathrm{EvenSum}(A'\cup S')\ge T'$"
   — against random multisets $A',S'$ (no structural restriction beyond the
   hypothesis). Found explicit counterexamples, e.g.
   $A'=[9.76,5.17,5.18]$ ($T'=20.11$), $S'=[10.18,14.47]$
   ($\mathrm{EvenSum}(S')=10.18\ge T'/2=10.05$, hypothesis satisfied), but
   $\mathrm{EvenSum}(A'\cup S')=15.37<T'=20.11$ — a clear violation. This
   held even after adding the natural extra restriction $\max(A')\le T'/2$
   (motivated by "$A'$'s elements are all $\le T/2$" in our setting):
   still found violations (e.g. $\mathrm{EvenSum}(A'\cup S')=21.08<T'=25.92$
   with $\max(A')=9.80\le T'/2=12.96$).
   - **Conclusion: Lemma X′ is not just unproved, it is false as an
     abstract statement about arbitrary multisets.** Any true replacement
     must exploit much more of the *specific* geometric/superincreasing
     structure of $\Gamma_{m-1}$ (e.g. that $S$ actually comes from
     refining a superincreasing sequence with $\le m-1$ cuts, giving it a
     rigid internal shape, not just one scalar EvenSum bound) — a purely
     sum-based "dual lemma" is the wrong level of generality and is a
     documented dead end, not merely unattempted.

3. **A tempting bypass — "splitting the top piece further only hurts
   XY" (an exchange/monotonicity idea) — is also FALSE.** I tested whether
   merging two of the $j=2$ top-fragments back together (making it a $j=1$
   split with the same tail) always weakly *increases* OddSum (i.e.
   whether finer splitting could only help LB, so $j=1$'s already-proved
   bound would dominate and $j\ge2$ would be free). Counterexample found:
   at $m=4$, a 3-way split gave $\mathrm{OddSum}=16.26$ vs. the 2-way merge
   giving $22.65$ — splitting further can cost LB nearly $6.4$. So the
   $j=1$ bound does **not** automatically dominate $j=2$; the extra cuts
   genuinely open new adversarial power for XY, even though (per point 1)
   the bound $2^m$ still empirically survives it. **This rules out a naive
   exchange-lemma shortcut** ("more cuts on top piece is never better for
   XY") as a route to close the induction — a real, checked dead end worth
   recording so no future approach wastes a round re-deriving it.

### Distinct openings for the outliner
- **(a) Track a positional/rank invariant through peeling, not just a
  scalar bound.** The real failure mode (point 2 above) is that a bare
  EvenSum-of-$S'$ bound loses all information about *which* elements of
  $S'$ are large — exactly the elements that can jump ahead of $A'$ in the
  global sort. A viable fix is to strengthen $T(m-1)$ itself to also
  control the tail's own **second- and third-ranked elements individually**
  (not just its OddSum total), i.e. induct on a vector of bounds
  $(\text{rank-1 elt} \le 2^{m-1},\ \text{rank-2 bound}, \dots)$ rather
  than a single OddSum inequality. This is a genuine strengthening of the
  induction hypothesis, in the spirit of Pólya's "induction loading"
  (`knowledge_base.md`, Problem-Solving Heuristics) and structurally
  resembles the two-part (before/after) invariant technique used in the
  crux corpus for `aimo-0236` (maintain a threshold valid both before and
  after the opponent's move, restorable every round) — worth adapting: a
  "before-peel / after-peel" two-sided bound on the *current global max of
  the remaining tail*, not just its total.
- **(b) Abandon peeling-by-size; induct on total piece count / total cuts
  directly with a genuinely two-sided hypothesis from the start** (as the
  approach file's own Step 3 already flags as the honest target, but
  without a concrete $U(m)$). Given point 2's counterexample, any such
  $U(m)$ **must** be tied to the specific recursive self-similarity
  $\Gamma_{m-1}\setminus\{\text{top}\}=\Gamma_{m-2}$ (scaled), not to a
  generic sum-based inequality — e.g. try proving simultaneously, by one
  induction on $m$: (i) $\mathrm{OddSum}\ge2^m$ under $\le m$ cuts
  (existing target) AND (ii) a *matching* statement about
  $\mathrm{OddSum}$ of $\Gamma_m$ **with its own top piece removed and
  replaced by an adversarial insertion of foreign elements up to a fixed
  total budget** — i.e. build the two-sidedness into the *object* (a
  "$\Gamma_m$-with-a-hole" family), not as an abstract EvenSum axiom on
  arbitrary $S'$.
- **(c) Full-interleaving direct argument (no peeling at all).** Since
  point 1 confirms the bound is numerically tight and exact ($=2^m$, not
  just $\ge$) at many boundary configurations, consider directly analyzing
  the descending global sort as a merge of two sorted sequences (top
  fragments $A$, sorted descending; tail elements $S$, sorted descending)
  and computing $\mathrm{OddSum}$ of a merge via a closed-form "number of
  $A$-elements strictly ahead of a threshold" counting argument — this is
  the same direction `greedy-reduction-geometric`'s Exchange
  Lemma/piecewise-linearity route is independently pursuing (see
  `current.md`); the two approaches may be convergent and could share a
  merge-counting lemma once developed. Not yet attempted by either
  approach in a general form.
- **(d) Reformulate as a potential-function argument instead of
  induction on $m$ at all** — e.g. define $\Phi(M)=\mathrm{OddSum}(M) -
  \max(M)/2 - \dots$ or similar and show cuts on the top piece cannot
  decrease $\Phi$ below a threshold. Not explored numerically this round;
  flagged as untested but plausible given the SOS/potential techniques in
  `knowledge_base.md` ("Piecewise-concavity smoothing", "Invariants &
  monovariants").

### Candidate technique(s)
- Two-sided / dual invariant maintained through alternating moves — direct
  structural analogue in the crux corpus: `aimo-0236` (two-part
  before/after induction to keep a valuation threshold alive through both
  players' moves). Worth reading in full if the outliner pursues opening
  (a) or (b) — the "maintain stronger bound before opponent's move, weaker
  bound after, self-restoring" pattern is exactly the shape of invariant
  this gap needs.
- Superincreasing-sequence dominance: `aimo-0019`'s crux ("bound a family
  of dyadic-length pieces of pairwise distinct sizes by twice the largest,
  via the geometric sum of distinct negative powers of two") is the same
  flavor of fact already used implicitly in Step 1a/1b of the certified
  $j=1$ theorem (splitting never increases a piece past its parent's
  value, and $\Gamma_m$'s superincreasing structure caps the tail's max at
  $T/2$). Confirms this structural fact is standard and safe to keep
  reusing, but doesn't by itself supply the missing dual bound.
- `aimo-0117` (Dutch box game: dyadic geometric sequence where the largest
  value strictly dominates the sum of the rest) is thematically the
  closest crux to the whole problem's flavor (alternating-claim game on a
  geometric/dyadic sequence, adversary can move pieces between "boxes")
  but its winning strategy (maintain "largest power is in the target box"
  by reacting only to whether the opponent moved that specific piece) does
  not directly transfer — the two-phase stick-cutting game's adversary
  structure (XY chooses *where to cut*, not which box to move a piece to)
  is different enough that this is a thematic analogue, not a technique
  transfer.

### Cheap-kill candidates
None obvious for closing $j\ge2$ directly — but point 3's negative result
(exchange/merging monotonicity is false) is itself a cheap kill: it
prunes an entire family of "reduce $j\ge2$ to $j=1$ via merging" attempts
before anyone spends a round trying to formalize it.

### Knowledge-base entries to use
- "Induction loading / strengthening the hypothesis" (Problem-Solving
  Heuristics) — directly the recommended next move (opening (a)/(b)).
- "Invariants & monovariants" (Combinatorics section) — for opening (d),
  a potential-function alternative to peeling induction.
- "Piecewise-concavity smoothing" — possibly adaptable if the outliner
  wants to attack the merge/interleaving problem (opening (c)) via an
  extremal/smoothing argument on the split points $a_1,\dots,a_{j+1}$
  treating the objective as piecewise-linear in each split parameter
  (OddSum of a fixed combinatorial rank-order is linear in the pieces;
  the rank order itself only changes at finitely many breakpoints where
  two elements are equal) — this could formalize "the worst case is at a
  breakpoint / tie configuration," consistent with all the numeric minima
  found above landing exactly on boundary/tie configurations.

### Analogous past problems (cruxes)
- `aimo-0236` (blackboard game, Alice adds $a$/Bob halves): crux move
  "two-part induction showing threshold holds both before AND after each
  opponent move" is the best structural analogue for building the missing
  two-sided invariant (opening (a)/(b)). Not a technique transfer of the
  *content* (different game), but the *shape* of the needed lemma matches
  closely.
- `aimo-0117` (Jesse/Tjeerd box game): thematic analogue (dyadic/geometric
  sequence, alternating claim-like structure, an adversary that can
  perturb the assignment) but the move structure differs enough that it's
  not directly adaptable — worth a second look if a future round pursues
  opening (c)'s merge/interleaving argument, since the "single largest
  value dominates the rest" dyadic fact is reused in both.
- `aimo-0019` (paint game): only the superincreasing-sum sub-fact
  ("bound a family of dyadic pieces by twice the largest") is reusable,
  already implicitly present in the certified $j=1$ theorem.
- No crux found that directly supplies a ready-made "dual EvenSum" or
  "two-sided OddSum/EvenSum sandwich" lemma for a claiming game on an
  arbitrary refined multiset — this appears to be genuinely novel content
  the population must derive itself.

### Prior progress
As documented in `current.md` / `lemmas/element-bound-and-j1-theorem.md`:
$j=0$ (any $k$) and $j=1$ (arbitrary split, arbitrary tail, given
$T(m-1)$) are fully proved and certified. $T(1)$ is fully closed. $j\ge2$
is open for all $m\ge2$.

### Dead ends (do not retry)
1. **Lemma X′ as literally stated** ("$\mathrm{EvenSum}(S')\ge T'/2
   \Rightarrow \mathrm{EvenSum}(A'\cup S')\ge T'$" for arbitrary positive
   multisets $A',S'$) — **disproved by explicit numeric counterexample**
   this round (see point 2), even under the natural extra restriction
   $\max(A')\le T'/2$. Any replacement lemma must use much more structure
   than a scalar EvenSum bound on $S'$.
2. **Exchange/monotonicity shortcut** ("merging top-piece fragments back
   together, i.e. reducing $j$, only helps LB / splitting only helps XY
   weakly") — **disproved by explicit numeric counterexample** this round
   (point 3): finer top-piece splits can cost LB substantially more OddSum
   than the corresponding coarser split, even though the final $2^m$ bound
   still (empirically) survives. Do not attempt to close $j\ge2$ by
   reducing it to the already-proved $j=1$ case via a merging argument.
3. (Carried from round 2, still valid) Static-priority "Q vs. rest"
   composite strategies — proved insufficient by exact game-tree
   counterexample in `greedy-reduction-geometric`.

### Small-case / intuition notes (conjectural, from numeric search)
- The bound $\mathrm{OddSum}\ge2^m$ for $j=2$ appears **tight and attained
  exactly** at boundary/tie configurations in every $m=2,\dots,5$ trial —
  consistent with the overall conjecture $c(n)=2^n/(2^{n+1}-1)$ and with
  the geometric partition being genuinely extremal (not just a good
  choice with slack).
- At the minimal configurations found, the top-fragment $a_1$ typically
  exceeds $T/2$ only slightly (e.g. $a_1\approx4.24$ vs. $T/2=4$ at
  $m=3$), and the *second* global-max element is consistently the tail's
  own untouched top piece $s_1=2^{m-1}$, not a second fragment of $A$ —
  i.e., the worst case for XY is to barely dominate with $a_1$, then let
  the tail's own structure do the rest of the "damage." This suggests
  opening (a)/(b) (tracking the tail's own top element explicitly through
  the induction) is likely the more promising route of the two openings
  above, over trying to force a rank-agnostic sum lemma.
