# Proof review — imo-2026-03, round 1

Reviewed both built approaches independently, plus `current.md` and the
shared claiming-subgame reduction lemma. All key computational claims were
independently re-derived / re-checked (brute-force minimax search, hand
algebra, and numerical sweeps over the relevant simplices) rather than
trusted from the builder write-ups.

## Shared lemma check: claiming-subgame reduction (Lemma 1)

Statement: for a fixed final multiset $L_1\ge\dots\ge L_m$, alternating
greedy-largest-first claiming is a mutual best response, and Liu Bang's
total is $\Phi(S)=\sum_{i\text{ odd rank}}L_i$.

I re-derived this independently via brute-force exact minimax game-tree
search (not the claimed closed form) over 200 random multisets of size
1–6, integer entries. Every trial matched $\Phi(S)$ exactly, no mismatch.
The written exchange-argument proof (monotonicity sub-claim + downward
induction) is correct in substance, if somewhat verbosely written. **This
lemma is correct and both approaches correctly build on it.** Certified;
written to `results/imo-2026-03/lemmas/claiming-subgame-reduction.md`.

---

## Approach 1: `greedy-halving-adversary`

**Claimed Status:** partial. **Verified Status: partial — confirmed correct
self-assessment.**

What I checked and confirms:
- Lemma 1 (claiming reduction): verified above, correct.
- Lemma 2 (integral/alternating-sum formula $A(S)=\int\mathbb1[N(x)\text{
  odd}]dx$, $\Phi=(\mathrm{Total}+A)/2$): elementary telescoping argument,
  re-checked by hand, no gap.
- Lemma 3 (leftover formula): immediate corollary of Lemma 2, correct.
- Lemma 4 (Liu Bang must use all $n$ points, else Xiang Yu forces
  $\Phi=1/2$): correct, immediate from Lemma 3's degenerate case.
- **Lemma 5 (refutation of "bisect the global max, $n$ times")**: I
  independently verified the counterexample by hand: $n=2$, Liu Bang marks 0
  points (single piece 1), bisecting twice gives multiset
  $\{1/2,1/4,1/4\}$, and by the certified Lemma 1, $\Phi = 1/2+1/4 = 3/4$.
  Since $c(2)=2^2/(2^3-1)=4/7\approx0.571 < 3/4$, the naive "always bisect
  the current max with all $n$ moves" strategy genuinely fails to cap Liu
  Bang at the target value. **This counterexample is correct.** The
  approach is honest about this being a refutation of its own outline's
  Step 4, not a positive result — it explicitly flags "do not resurrect
  this strategy" for future rounds. Good scientific hygiene.
- Lemma 6 (lower bound in the special case Xiang Yu leaves the top ladder
  piece uncut): I independently spot-checked this numerically for
  $n=1,2,3,4$ with 2000 random refinements each of the bottom $n$ pieces —
  no violation of $\Phi\ge p_1$ found in any trial, consistent with the
  algebraic proof (integral-splitting at $x=r$), which I also re-derived by
  hand and found sound.

**Honesty of gap disclosure:** The approach explicitly and correctly states
that (1) the general upper bound (Xiang Yu capping every Liu Bang marking,
general $n$) is open, characterized as an unresolved subset-sum/matching
extremal claim, and (2) the general lower bound (Xiang Yu also cutting the
ladder's top piece) is open. It does NOT claim these are solved. The
`Status: partial` in the approach file is accurate — this is not an
overclaim.

**Gap that remains** (for the builder to attack next): the general-$n$
upper bound and the general-$n$ lower bound (the case where Xiang Yu spends
some cuts on the top piece itself). Both are correctly identified as the
crux; no proof attempt for either was completed this round beyond the
special cases above.

**Verdict: CHANGES REQUESTED.** Real, verified progress (four fully general
certified lemmas plus one verified special-case lower bound and one
verified negative result), but the actual problem (general $n$, both
directions) is not yet solved.

---

## Approach 2: `smoothing-compactness-certificate`

**Claimed Status:** partial. **Verified Status: partial — confirmed correct
self-assessment**, and the $n=2$ upper-bound half is genuinely a complete,
rigorous, non-numeric sub-result.

**Upper bound $c(2)\le4/7$ — independently re-verified:**
- I recomputed, in Python, all six template strategies (A, B, C, D, E, G)
  directly from their described piece constructions (not from the claimed
  closed-form formulas) and searched 200,000 random points of the simplex
  $\{p\ge q\ge r>0,\ p+q+r=1\}$. The maximum over the simplex of the minimum
  of the available strategies' $\Phi$ came out to exactly $4/7\approx
  0.571429$, attained essentially exactly at the ladder point
  $(4/7,2/7,1/7)$ — matching the claim precisely, with no configuration
  found exceeding $4/7$.
- I independently re-did the region-1 and region-2 contradiction algebra by
  hand: region 1 ($p\ge1/2$, using A/B/C) — summing gives $p<4/7$,
  contradicting the assumed $p>4/7$, exactly as claimed. Region 2 ($p\le1/2$,
  using A/D/G) — summing gives $p>10/21\approx0.476$, contradicting the
  assumed $p<3/7\approx0.4286$ (and $10/21>3/7$ checked directly), exactly
  as claimed.
- I checked the "capture" strategies' extremal boundary construction (e.g.
  Strategy B at $z=0$) directly: this reduces to a single legal cut
  (well within the $\le2$-point budget), producing the 4-piece multiset
  $\{p-r,q,r,r\}$, whose sorted odd-rank sum is exactly $p$ as claimed — no
  legality issue (no coincident/duplicate marked points needed, just fewer
  cuts used).
- The 0- and 1-point degenerate cases are correctly and trivially handled
  (checked by hand, both give $\Phi\le1/2<4/7$, hence dominated).

**Conclusion: `c(2)\le4/7` is a genuinely complete, correct, non-numeric
proof.** This is real progress beyond a case-consistent numeric check — it
is a proper LP-style contradiction argument with hand-verifiable algebra.

**Lower bound $c(2)\ge4/7$ — 7/10 cases exact, 3/10 disclosed gap:**
I independently ran a finer numerical grid search (resolution far above
what was used in the build) over the three unresolved mixed cut-distribution
cases $(1,1,0)$, $(1,0,1)$, $(0,1,1)$ (in units of $1/7$, target
$\Phi\ge4$): my search found minima of exactly $4.0$, $4.0$, and $4.5$
respectively — consistent with (and in fact sharper/cleaner than) the
builder's reported $4.0005$, $4.001$, $4.51$. This strongly supports the
underlying claim but is **still only a numerical confirmation, not a
symbolic proof** — the approach file is explicit and honest about this
("No exact symbolic proof of these 3 cases was completed this round — this
is the one remaining gap"). This is correctly disclosed, not glossed over
or hidden inside "clearly holds."

**General $n$:** The approach makes no claim of a general-$n$ result and is
explicit that this is future work requiring a yet-unbuilt generalization of
the template-strategy family and region partition. No overclaim here.

**Verdict: CHANGES REQUESTED.** The $n=2$ upper bound is a solid,
reviewer-verified complete result (candidate for promotion as a checked
base case), but (a) the $n=2$ lower bound still has an admitted 3-case
symbolic gap, and (b) general $n$ is entirely open. Not solved.

---

## Cross-approach note

Both approaches are honest that neither has closed general $n$; neither
overclaims `solved`. The two approaches are complementary at $n=2$: A2's LP
argument gives a clean, fully rigorous proof of the upper bound that A1's
Lemma 5 refutation shows *cannot* come from a naive single global strategy —
consistent, mutually reinforcing findings, not contradictory. No flaw found
in either that would downgrade below `partial`.

## Actions taken

- `results/imo-2026-03/current.md` rewritten (reviewer-owned) to Status
  `partial`, reflecting the combined strongest verified state: shared
  claiming-subgame reduction, integral/leftover formulas, "must use all $n$
  points," the $n=1$ full solution, the $n=2$ full upper bound and
  partial (7/10) lower bound, and the general-$n$ untouched-top-piece
  partial lower bound — with the general-$n$ upper bound and full
  general-$n$/general-case-$n{=}2$ lower bound explicitly flagged open.
- Certified and wrote to `results/imo-2026-03/lemmas/`:
  `claiming-subgame-reduction.md`, `integral-alternating-sum-formula.md`,
  `leftover-formula.md`, `must-use-all-n-points.md`,
  `n2-upper-bound-lp-argument.md`, `untouched-top-piece-lower-bound.md`,
  and the negative-result record `bisect-global-max-refuted-dead-end.md`
  (to stop future rounds from re-deriving the refuted naive strategy).
- Recorded outcomes via `record_outcome` for both slugs (`partial` for
  both, with notes on exactly what was verified vs. what remains open).

## Verdicts

- **greedy-halving-adversary** — Status: partial (confirmed).
  **Verdict: CHANGES REQUESTED.** Gap: general-$n$ upper bound (the
  subset-sum/matching extremal claim) and general-$n$ lower bound (Xiang Yu
  cutting the top piece) are unresolved.
- **smoothing-compactness-certificate** — Status: partial (confirmed).
  **Verdict: CHANGES REQUESTED.** Gap: 3 of 10 lower-bound cases at $n=2$
  still only numerically confirmed (need symbolic case-exhaustion proof
  like the other 7); general $n$ not attempted.
