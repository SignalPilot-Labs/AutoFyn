## imo-2026-03 (lens: lp-duality-certificate Open Gap 1, case (b2))

Scope: case (b2) of the Peel-Target Existence trichotomy — $p_1<T/2$,
$T/D_n<p_2<a_nT/2$ — the sole open region of the general upper bound
$c(n)\le a_n$. Round 13 refuted a "peel-then-dominate" hybrid by exact
witness (~10% failure). Assignment: test whether a proper strong induction
on $n$ (reusing `telescoping-threshold-identity`) closes (b2), and whether
(b2)'s witness family has exploitable extra structure (e.g. a $p_3$
constraint) for a case-(a)-style dominant-tail-element argument.

### Distinct openings

1. **Algebraic (non-numeric) proof that the natural peel-and-recurse
   induction structurally cannot reach case (b2) at all** — not just that
   one hybrid variant fails (round 13's finding), but that *any* clean
   "peel $p_1$ against $p_2$, then apply the full inductive hypothesis
   $P(n-1)$ exactly (not a crude bound) to the residual" mechanism has an
   **exact** threshold of $p_2\ge a_nT/2$ — i.e. it closes exactly (and
   only) case (a), with zero slack past that boundary. I re-derived this
   by hand: requiring $p_2+a_{n-1}(T-2p_2)\le a_nT$ reduces, via the
   telescoping identity $2a_{n-1}-1=1/D_{n-1}$ and the already-certified
   algebra in Theorem B's corollary, exactly to $p_2\ge a_nT/2$. So a
   full-strength ($P(n-1)$, not just a crude domination bound) version of
   this induction step is *provably* incapable of covering any part of
   case (b2) — it is not an accident of round 13's weaker hybrid, it is
   structural. This should stop the outliner from re-trying any "peel
   $p_1$ vs $p_2$ + strengthen the recursion" variant; the threshold is
   fixed at $a_nT/2$ no matter how tightly the residual's IH is applied.

2. **Symmetric check on bisecting $p_1$ alone with the full IH** (Theorem
   C′ + exact $P(n-1)$, not the crude Max-Domination bound used in R13.2):
   threshold works out to $p_1\ge a_nT$ — a band *strictly inside*
   Theorem A's already-known $p_1\ge T/2$ region (since $a_n>1/2$), so this
   route contributes nothing new either, and in particular cannot reach
   case (b2) ($p_1<T/2<a_nT$). Confirms round 9's diagnosis that the two
   regimes are coupled, from the (b2) side specifically.

3. **New unconditional generalization of R13.2**: a **Bisect-Top-$k$
   Lemma**. For any $k$ with $0\le k\le\min(n,m-1)$, bisecting the top $k$
   pieces $p_1,\dots,p_k$ (using exactly $k\le n$ cuts, applying
   `pair-cancellation-identity` $k$ times to cancel each inserted equal
   pair) and leaving the tail $\{p_{k+1},\dots,p_m\}$ untouched gives
   $\Phi=(T+A(\text{tail}))/2\le (T+p_{k+1})/2$ by `max-domination-lemma`.
   Hence $\Phi\le a_nT$ **unconditionally, no induction, for any $k\le n$**
   whenever $p_{k+1}\le T/D_n$ — note the threshold $T/D_n$ is the *same*
   constant regardless of $k$ (it only depends on the overall target
   level $n$, since we compare directly against $a_nT$, not a reduced
   target). R13.2 is exactly the $k=1$ case. This is a genuinely new,
   clean, fully general lemma (elementary proof, no gaps) — I verified it
   exact-`Fraction`, $n=1,\dots,7$, 5717 hit-cases (random markings where
   some $k$ satisfies the threshold), **zero violations**.
4. **Coverage of case (b2) by this family is real but partial, not a
   closure**: random-sampling test (uniform random integer-ratio
   markings, $n=3,\dots,7$, 500–3000 case-(b2) samples per $n$) shows the
   Bisect-Top-$k$ family only rescues **5–13%** of case-(b2) witnesses (a
   witness is "covered" if *some* $k\le n$ has $p_{k+1}\le T/D_n$); the
   large majority of case-(b2) markings have every one of
   $p_2,\dots,p_{n+1}$ strictly above $T/D_n$, so no single tail piece is
   small enough to trigger this mechanism. Worth keeping as one more
   certified sufficient region (cheap, orthogonal to Theorem A/B/D,
   Equal-Pieces Closure, Spare-Cut Bisection Corollary) but it will not by
   itself close (b2).
5. **Numeric exploration of the true optimum in case (b2)** (scipy
   multi-start Nelder-Mead over all cut-count compositions, $n=3,4$,
   random case-(b2) witnesses): the actual minimum $\Phi$ Xiang Yu can
   force is comfortably below target in every witness tested (margin
   $\approx0.015$–$0.03$ at both $n=3$ and $n=4$, i.e., case (b2) is *not*
   numerically tight in the interior at these $n$, unlike some other
   sub-cases in this project's history). Crucially, **the winning cut
   allocation varies witness-to-witness** — $(1,0,1,0)$, $(2,1,0,0)$,
   $(1,3,0,0,0)$, $(2,0,1,0,1)$, etc. — with no single fixed template
   dominating. Optimal values cluster near $T/2$ regardless of $n$ or
   witness. This is consistent with (and reinforces, not merely repeats)
   round 10's "near-perfect pairing/matching" diagnosis
   (`refutation-of-tail-refinement-monotonicity`/leftover-formula framing,
   memory rule 18): the right mechanism for case (b2) is likely an
   **existence claim** ("a legal $\le n$-cut refinement exists that pairs
   almost everything up, leaving a small unpaired leftover"), not a
   single closed-form recursive formula or a fixed small strategy family.
6. **Adversarial worst-case search was attempted but did not complete**
   within the round budget (`scipy.optimize.differential_evolution` over
   the full marking simplex with a nested composition-search objective
   timed out at $n=4$) — so I was **not** able to locate a near-tight
   case-(b2) witness this round, or check whether the margin shrinks
   toward $0$ as $n\to\infty$. This is an honest gap in the numeric
   evidence, not a finding either way; a future round with more compute
   budget (or a smarter/cheaper vertex-restricted search reusing the
   already-certified Vertex-Minimum Theorem instead of a full continuum
   optimizer) should retry this specifically to locate the true worst
   case in (b2) and read off its structure.

### Candidate technique(s)

- The existence/pairing reformulation (round 10's leftover-formula idea)
  looks like the most promising route into case (b2) specifically, given
  finding (5) above — an explicit construction showing a near-perfect
  pairing always exists using $\le n$ cuts whenever $p_1<T/2$ and
  $p_2<a_nT/2$, would likely close it without needing the induction
  machinery that's now proven (finding 1) to top out exactly at case (a)'s
  boundary.
- Bisect-Top-$k$ (finding 3) is a cheap, certifiable, orthogonal
  sufficient condition worth adding to the toolkit regardless of whether
  it closes (b2) alone — it's a one-line generalization of an already
  certified lemma and immediately reusable.
- Vertex-restricted search (reuse `vertex-minimum-theorem`/
  `exchange-smoothing-vertex-maximization`, already proven marking-
  agnostic per round 10's finding) instead of a continuum optimizer would
  make the adversarial worst-case search in finding (6) tractable — this
  is a concrete, cheap next step, not a new mechanism.

### Cheap-kill candidates

None found this round beyond confirming the two natural "obvious" moves
(peel-p1-p2+IH, bisect-p1+IH) are dead structurally (findings 1–2) — worth
recording as dead ends so no future round re-derives them expecting a
different threshold.

### Knowledge-base entries to use

No new `knowledge_base.md` entries beyond what's already cited in the
approach file (`pair-cancellation-identity`, `max-domination-lemma`,
`telescoping-threshold-identity`, `bisect-top-identity`/Theorem C,
`vertex-minimum-theorem`). This problem's toolkit is entirely self-built;
`knowledge_base.md` generic entries were checked in earlier rounds and
found not to add new leverage here (per memory rule).

### Analogous past problems (cruxes)

Not re-queried this round (time budget spent on numeric experiments per
the assigned lens); memory records (round 1, confirmed again round 4) that
the `games-and-strategy` / `extremal-principle` / `processes-and-algorithms`
subtopics of the crux corpus have no strong direct analog for this
problem's specific two-stage cut-and-claim structure — treat as a
from-scratch construction, no crux transplant expected to help case (b2)
specifically either (its core content — an existence/pairing argument over
a superincreasing-like but not-strictly-superincreasing tail — is fairly
bespoke to this problem's exact alternating-sum functional).

### Prior progress

- Case (b1) ($p_2\le T/D_n$) closed unconditionally (`unconditional-p2-threshold-closure`, round 13).
- Case (a) ($p_2\ge a_nT/2$) closed conditionally on $P(n-1)$ for the specific reduced tail (Theorem B corollary, round 9/13).
- Case (b2) genuinely open; round 13's "peel-then-dominate" 2-cut hybrid refuted by exact witness.
- This round: **new certified-quality lemma** Bisect-Top-$k$ (generalizes R13.2, covers 5–13% of (b2) numerically, zero violations in 5717 exact-`Fraction` hit-cases) — recommend promoting to `lemmas/`.
- This round: **new structural (algebraic, not numeric) dead-end proof** that peel-$p_1$-vs-$p_2$+full-IH and bisect-$p_1$+full-IH both have exact thresholds landing exactly on case (a)'s / Theorem A's existing boundaries, with zero slack into (b2) — worth recording so no future round re-attempts either "strengthen the peel recursion" idea expecting it to reach (b2).

### Dead ends (do not retry)

- "Peel $p_1$ against $p_2$, then apply the exact/full inductive hypothesis $P(n-1)$ to the residual" — algebraically proven to have exact threshold $p_2\ge a_nT/2$, i.e. it recovers exactly case (a) and nothing more, no matter how the residual's bound is strengthened past the crude Max-Domination version already tried (this round's finding 1).
- "Bisect $p_1$ alone + full IH at $n-1$" — algebraically proven threshold $p_1\ge a_nT$, strictly inside the already-known Theorem A region $p_1\ge T/2$; contributes nothing new (this round's finding 2).
- (Carried over from round 13, still valid) the specific 2-cut "peel-then-dominate" hybrid construction — refuted by exact witness, ~10% failure rate.

### Small-case / intuition notes (conjectural, numeric only)

- At $n=3,4$, case-(b2) witnesses tested numerically all have a comfortable margin ($\Phi_{\min}$ roughly $0.015$–$0.03$ below $a_nT$) — case (b2) does not look numerically "knife-edge" tight at these small $n$, though a true adversarial search was not completed (finding 6), so this is weak, incomplete evidence, not a proof there's slack for all $n$.
- The optimal cut allocation at the true minimum varies witness-to-witness with no fixed pattern observed (finding 5) — this is evidence *against* a single closed-form template closing (b2), and evidence *for* an existence/pairing-style argument being the right shape of proof.
- No clean structural constraint between $p_3$ and $p_2$ was found at the (informally) near-tightest witnesses located this round (margins were not small enough, and the adversarial search that would locate genuinely tight witnesses did not finish) — this specific sub-question (does (b2)'s hardest witness family constrain $p_3$ relative to $p_2$ the way case (a)'s dominant-tail-element argument would want) remains **unresolved**, not refuted; a future round should prioritize the vertex-restricted adversarial search (see Candidate technique(s) above) to actually answer it.
