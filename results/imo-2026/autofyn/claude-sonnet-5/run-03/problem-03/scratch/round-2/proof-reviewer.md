# Proof review — imo-2026-03, round 2

Reviewed all three built approaches. Problem: determine $c(n)$, the largest
value Liu Bang (LB) can guarantee in the two-phase stick-marking game.
Conjectured/strongly-evidenced answer (unchanged from round 1, not in
dispute this round): $c(n) = 2^n/(2^{n+1}-1)$. None of the three approaches
claims `solved` this round; all self-report `partial`, correctly.

I independently re-derived and numerically/symbolically re-checked the
single load-bearing new claim in each file (not just read the prose) using
`python3` (exact `Fraction` arithmetic where relevant, randomized brute
force elsewhere). Details below.

---

## 1. `greedy-reduction-geometric`

**Builder's claim:** new Lemma 4 ("greedy-floor guarantee against an
arbitrary opponent"), fully proved; plus a documented counterexample
showing a "Q-priority" static strategy fails to close Lower-bound Case 2.

**Verification.**
- Re-derived Lemma 4's induction from scratch (base cases $m=0,1$;
  inductive step reduces by 2 elements per full round, reusing only the
  purely combinatorial inequality $(\ast)$ from the Greedy-Optimality
  proof, which does not depend on optimality of either player). The proof
  is valid: Player 1 greedy vs. arbitrary Player 2 still nets
  $\ge\mathrm{OddSum}(N)$. This is a real, nontrivial strengthening of the
  certified Greedy-Optimality Lemma (one-sided vs. two-sided optimality).
- Re-ran the $n=3$, $r_3=8/15$ equal-4-way-split counterexample by exact
  game-tree search (`Fraction` arithmetic, full minimax over the Q-priority-
  constrained LB strategy vs. optimal XY): got **exactly $7/15$** for the
  Q-priority-forced floor, and **exactly $9/15$** for the true unconstrained
  value — both match the builder's claims to the digit. $7/15 < c(3) =
  8/15 < 9/15$, confirming the gap is real and the dead end is genuine
  (not an artifact of a computational slip).
- All previously-certified lemmas (Greedy-Optimality, Reduction, Peeling,
  Case 1, $n=0,1$) are untouched this round and remain valid (re-read, no
  regressions).

**Gap remaining (unchanged in kind, narrowed in scope):** Case 2 for
$n\ge2$ (XY spends $\ge1$ cut on LB's largest piece) is still open; the
general upper bound for arbitrary LB partitions is still open. The round's
contribution is a real new lemma plus a real, verified negative result
(rules out an entire proof strategy family) — genuine progress, no gap
closed in the target theorem itself.

**Verdict: CHANGES REQUESTED.** True Status: `partial` (matches builder's
self-report — no overclaim). Gap to close next: the true interleaved
piecewise-linear / tie-block analysis of Case 2 (the outline's original
plan, not yet executed), now informed by the confirmed fact that no static
priority order can substitute for it.

---

## 2. `self-similar-induction-on-n`

**Builder's claim:** "Element Bound" lemma (new); full proof of the $j=1$
slice of the lower-bound induction for *arbitrary* splits and *arbitrary*
tail refinements (strictly more general than round 1's exact-bisection-only
result); a precisely stated missing "Lemma X′" diagnosing why the method
cannot reach $j\ge2$.

**Verification.**
- Element Bound ($\mathrm{OddSum}(S)\ge x$ for any $x\in S$): re-derived
  independently via a shorter route (peel $\max(S)\ge x$ directly via the
  certified Peeling Lemma) — agrees with the builder's longer case-split
  proof. Both correct.
- The $j=1$ theorem's algebra (Steps 1a–1d: tail-max bound, global-max
  identification, peeling $t_1$, two-way case split on $t_2$ vs.
  $s_1=\max(S)$ using Element Bound in one branch and the inductive
  hypothesis $T(m-1)$ in the other) was checked line by line and is
  correct; the reduction to "$\mathrm{OddSum}(\{t_2\}\cup S)\le R$" and its
  proof in both sub-cases is sound.
- Independently re-verified the *result* (not just the proof) by randomized
  brute-force search over splits and tail refinements: for $m=2$, minimum
  found $\mathrm{OddSum}=4.0$ (target $\ge4$, tight — matches the claimed
  equality-attaining boundary); for $m=3$ (tail refined with up to $m-1=2$
  cuts via a random recursive splitter), minimum found $\approx8.001$
  (target $\ge8$). No violation in 200,000 random trials at each $m$.
- The three-way-tie resolution (previously flagged as the round-1 gap) is
  now handled via the certified generalized Tie-neutrality block lemma,
  explicitly instantiated with the correct block ($t_1,t_2,s_1$ tied at
  $T/2$, block length 3, first mover gets $\lceil3/2\rceil=2$ copies) —
  this is a correct, complete closing of the previously-identified gap, not
  a restatement of it.
- Lemma X′'s statement (needing $\mathrm{EvenSum}(S')\ge T'/2$ to conclude
  $\mathrm{EvenSum}(A'\cup S')\ge T'$, the dual of the $j=1$ mechanism) is
  precisely and correctly extracted as the obstruction: the one-sided
  inductive hypothesis $T(m-1)$ (a lower bound on $\mathrm{OddSum}$ of the
  *whole* tail) genuinely gives only an *upper* bound on
  $\mathrm{EvenSum}$ of a sub-multiset with an element already removed and
  the mover flipped — the wrong direction. This diagnosis is correct and a
  useful, honest sharpening (not hand-waved as "similarly" or "clearly").

**Gap remaining:** $j\ge2$ (hence $T(m)$ for $m\ge2$) is not established;
the induction still only climbs to $m=1$ in full generality. The upper
bound direction is not addressed at all by this approach (as before).

**Verdict: CHANGES REQUESTED.** True Status: `partial` (matches
self-report). This is a genuine advance: closes an entire previously-open
sub-case ($j=1$, general split/refinement) with a correct, generalizable
method and turns a vague "$j\ge2$ open" into a precise missing-lemma
statement (Lemma X′) that the next round can attack directly instead of
re-discovering the obstruction.

---

## 3. `universal-halving-adversary`

**Builder's claim:** Doubling Lemma ($\mathrm{OddSum}(R\cup R)=\mathrm{sum}(R)$,
fully general); Generalized Duplicate-the-Rest (exact identity
$\mathrm{OddSum}=p_1$ for *any* LB partition with $p_1\ge S$, not just the
geometric one), closing the upper-bound regime $p_1\in[1/2,c(n)]$ for all
$n$.

**Verification.**
- Doubling Lemma: re-derived the "even-length block, any starting rank,
  splits evenly" argument from scratch — correct (pairing consecutive
  ranks $(e,e+1),(e+2,e+3),\dots$ always gives one odd, one even, for a
  block of even length regardless of $e$'s own parity). Brute-force
  checked over 2000 random integer multisets (sizes 1–6): exact match in
  every trial, no floating-point-only tolerance needed (I used exact
  arithmetic).
- Theorem 2 (Generalized duplicate-the-rest): the two-case split
  ($\ell$ absent from vs. equal to some $R$-value) is exhaustive (a real
  number either equals one of finitely many distinct values or none — no
  third option), and both cases' block-counting arguments (odd/even rank
  of $\ell$'s own position or merged block) are correct on inspection.
  Independently brute-force checked over 5000 random partitions with
  $p_1\ge S$ (varying $n=1,\dots,5$): max discrepancy $1.1\times10^{-16}$,
  i.e. exact up to floating-point noise. This is a real, strict
  generalization of the previously-certified geometric-only identity.
- Spot-checked the two worked "still open" examples by direct arithmetic:
  $(0.6,0.35,0.05)$ at $n=2$ with the "bisect $p_1$ and bisect $p_2$"
  response gives exactly $0.525 < 4/7$ (confirmed); the $(0.4,0.35,0.25)$
  bisect-$p_1$-only response gives exactly $0.55 < 4/7$ (confirmed) — the
  builder's honest self-correction mid-file (initially mis-flagging this as
  a counterexample, then catching and correcting the arithmetic error
  before finalizing) is itself a good sign of genuine self-checking rather
  than a red flag; I re-verified the corrected value independently and it
  is right.
- The pruning-lemma discussion (LB always uses full budget) is honestly
  left open with a real counterexample to the naive monotonicity argument
  ($k=1$ value $1/2$ vs. a $k=2$ refinement giving the *same* $1/2$, not
  strictly more) — this is correct: the refinement $\{1/2,1/2\}$ indeed
  gives XY's optimal response value $1/2$ under the certified $n=1$
  formula, so the naive "any refinement weakly helps" claim is genuinely
  false as stated, though the builder correctly notes this doesn't
  necessarily block $c(n)$ itself from being attained by a full-budget
  partition (LB just needs *some* good partition, not that all refinements
  help).

**Gap remaining:** the regimes $p_1>c(n)$ and $p_1<1/2$ are still open, with
honest, checked worked examples for both showing a single-piece cut is not
always enough and no universal rule was found. The pruning lemma is
explicitly unproved.

**Verdict: CHANGES REQUESTED.** True Status: `partial` (matches
self-report). Genuine advance: the previous round's geometric-only
"duplicate-the-rest" identity is now a fully general theorem covering an
entire regime ($p_1\in[1/2,c(n)]$) for arbitrary partitions — a real
generalization, not a restatement, and it is the general-partition
analogue that `greedy-reduction-geometric`'s own geometric-construction
"self-similar split" equality witness needed.

---

## Certified lemmas (new this round)

All three certified to `results/imo-2026-03/lemmas/` after independent
re-derivation/verification (see above):

1. `lemmas/greedy-floor-against-arbitrary-opponent.md` — Lemma 4 from
   `greedy-reduction-geometric`, with an explicit caveat (also verified)
   that it does not license naive static-priority splitting.
2. `lemmas/element-bound-and-j1-theorem.md` — Element Bound + the general
   $j=1$ theorem from `self-similar-induction-on-n`.
3. `lemmas/doubling-lemma-and-generalized-duplicate-the-rest.md` —
   Theorem 1 (Doubling Lemma) + Theorem 2 (Generalized duplicate-the-rest)
   from `universal-halving-adversary`.

No lemma was rejected this round — all three sets of claims held up under
independent re-derivation and computational stress-testing.

## `current.md`

Updated: Status remains `partial`. Consolidated "Current best" now
reflects all three round-2 advances (Lemma 4 + dead-end documentation;
the general $j=1$ theorem + precise Lemma X′ obstruction; the general
upper-bound regime $[1/2,c(n)]$ closure) and narrows the two remaining
open gaps precisely: (1) lower bound for $j\ge2$ (missing Lemma X′, and a
confirmed-dead static-priority route), (2) upper bound for $p_1>c(n)$ and
$p_1<1/2$.

## Recorded outcomes

All three: `advanced` (real progress — new certified lemmas, a gap
narrowed with a precise missing-piece diagnosis, and/or a documented dead
end that prunes future search — but the target theorem is not closed for
any of them).

## Summary verdicts

- `greedy-reduction-geometric`: **CHANGES REQUESTED**, Status: `partial`.
- `self-similar-induction-on-n`: **CHANGES REQUESTED**, Status: `partial`.
- `universal-halving-adversary`: **CHANGES REQUESTED**, Status: `partial`.

No approach reached `solved`; the problem `imo-2026-03` remains `partial`
overall, per `results/imo-2026-03/current.md`.
