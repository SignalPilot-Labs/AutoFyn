# Proof-builder report — slug `rank-tie-vertex-reduction`, round 6

## Assignment
Close (or make maximal progress on) inequality (★★) in §5.1 of
`results/imo-2026-03/approaches/rank-tie-vertex-reduction.md`:
$\int_{W\cap[0,r)}v(t)\,dt\le\Delta/2$, the window-integral inequality
independently identified as the shared four-round obstruction across the
approach population (`greedy-halving-adversary`'s claim (B),
`rank-pigeonhole-budget`'s band-occupancy minimization, and this slug's own
Cross-Term Reduction Theorem all ask for the same fact).

## Result: (★★) is now fully proved, unconditionally, for every n ≥ 2

New **Half-Window Vanishing Lemma**: every element of any legal tail
refinement $G'$ of $T=\{p_2,\dots,p_{n+1}\}$ is $\le p_2$ (each piece's
fragments are $\le$ that piece, and the ladder is decreasing), so
$N_{G'}(t)=0$ for every $t\ge p_2$, hence $v(t):=\mathbb1[N_{G'}(t)\text{
odd}]=0$ for every $t\ge p_2$.

Since the ladder identity $p_1=2p_2$ makes $p_2$ the **exact midpoint** of
the window $W=[p_1-x,x)$, split $W=W_L\sqcup W_R$ at $p_2$ (each half length
$\Delta/2$): the Lemma gives $v\equiv0$ on $W_R=[p_2,x)$ exactly (not just on
average), while $v\le1$ trivially on $W_L=[p_1-x,p_2)\subseteq[0,r)$. Summing:
$$\int_{W\cap[0,r)}v = \underbrace{\int_{W_L}v}_{\le\ \Delta/2} +
\underbrace{\int_{W_R\cap[0,r)}v}_{=\ 0} \ \le\ \Delta/2.$$

This is a complete, elementary, general-$n$ proof — not a further reduction.
The oversight in prior rounds was bounding $v$'s integral over the *whole*
window at once (giving the crude, factor-2-too-weak bound $\le\Delta$
mentioned in the round-5 write-up), rather than splitting at the
ladder-forced midpoint $p_2$ first, where half the window is provably zero
for an elementary reason (no tail element can exceed the tail's own largest
piece $p_2$).

**Corroboration (not needed for the proof, done for cross-checking):** exact
`Fraction` computation, $n=2,\dots,6$, 300 random legal tail refinements
each (random cut counts and random rational cut positions), 1500 trials
total — ratio $\int v/(\Delta/2)$ never exceeds 1, reaches exactly 1 in the
predicted equality cases (tail untouched, $\Delta\le p_2$), zero violations.

## Consequences written into the file

- Combined with the already-certified Cross-Term Reduction Theorem (§5.1),
  this **fully closes the entire "single cut on $p_1$, arbitrary legal tail
  refinement" case of the round-5 domination goal**, for every $n\ge2$ —
  a complete sub-result (both the symmetric case, already certified by
  `symmetric-split-c1-lower-bound`, and every asymmetric case, closed here).
- A new §5.2.1 gives a second, independent, self-similar proof of the bound
  for the "tail entirely untouched" sub-family (using a nonnegative-integral-
  over-a-subinterval argument), generalizing §5.3's residual corollary
  (previously verified only for $n\le7$) to all $n$ for that closely related
  family — flagged as a partial, not full, closure of §5.3's own specific
  residual (§5.3's family additionally requires an exact tie to an interior
  $p_j$, a narrower configuration not automatically covered).
- §5.4 rewritten to reflect (★★) is closed; new open items listed: general
  $c_1\ge2$ (more than one cut on $p_1$), full vertex enumeration beyond
  single-cut-on-$p_1$ configurations, and the general upper bound.
- New "Promotable lemmas" entry for the Half-Window Vanishing Lemma,
  flagged as the top candidate for promotion and for checking whether
  sibling approaches' equivalent-gap statements (`greedy-halving-adversary`
  claim (B), `rank-pigeonhole-budget`'s band-occupancy claim) can be closed
  by direct transplant of the same elementary observation ("no tail element
  exceeds the tail's own largest piece") rather than independent re-proof.
- Old round-6-outliner note (recommending (★★) as the target for
  `lp-duality-certificate` / `integer-lattice-reduction`) marked superseded
  in place (kept for audit trail), with a new round-7-facing recommendation
  section pointing at the three remaining open items above.

## Status
Left as `partial` (the overall problem — general $n$, both directions — is
still open: general $c_1\ge2$, full vertex enumeration, and the upper bound
remain unclosed). But the shared crux gap (★★) that this round was
specifically assigned is now fully closed, which is a genuine and
significant advance for the whole population, not just this slug —
recommend the outline-reviewer/proof-reviewer verify §5.2's short elementary
proof promptly and consider whether it lets other approaches' equivalent
open claims close by direct transplant.

File updated: `results/imo-2026-03/approaches/rank-tie-vertex-reduction.md`
(sections 5.2, 5.2.1, 5.3 header note, 5.4, Approaches tried, Full proof,
Promotable lemmas, and a new round-6/round-7 outline note all revised).
