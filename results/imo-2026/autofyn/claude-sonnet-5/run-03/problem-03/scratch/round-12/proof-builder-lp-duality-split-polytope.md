# proof-builder report — slug `lp-duality-split-polytope`, round 12, imo-2026-03

## Task
Round-12 target (appended by outliner): attempt one focused, *proved*
fragment-vs-fragment tying construction at the hard vertex $e_0$ of
`global-lp-vertex-sufficiency`'s region-only vertex classification —
ties fragments of *different* split pieces to each other, structurally
evading the certified Mass-Constraint Theorem's obstruction (which only
covers ties to a *whole untouched piece*). Explorer found a soft negative
numeric signal (minimal clearing $s$ grows with $n$). Task: determine
whether a bounded construction exists (proved, not just searched), or
turn the negative signal into a genuine proved obstruction.

## Result: a complete, proved negative theorem for the natural "maximally
efficient" sub-family, honestly scoped as not covering the fully general case

**Setup used.** $e_0$ is a near-uniform arithmetic-progression partition
($p_i=p_{n+1}+(n+1-i)\gamma(n)$, $\gamma(n)=1/(2^{n+1}-1)$ exponentially
small), and the target excess $c(n)-\tfrac12=\gamma(n)/2$ is on the same
tiny scale as a single AP gap — a razor-thin threshold, not comparable to
the pieces' own $\Theta(1/n)$ sizes.

**Defined and analyzed "Perfect-Tie" constructions**: split pieces in a
set $S$ ($|S|=s$), tie *every* resulting fragment into an even-multiplicity
equal-value block using only fragments of $S$ itself (covers both
self-tie/bisection and genuine cross-piece fragment-vs-fragment tying;
excludes only the already-refuted tie-to-whole-untouched-piece family).
Via the certified Singleton-Interleaving Lemma (Theorem 9), this gives an
**exact** identity $\mathrm{OddSum}(M)=\tfrac12+\tfrac12\mathrm{AltSum}(U)$
depending only on which pieces are left untouched ($U$), not on the
internal tying pattern.

**New tool: Integer-Alternating-Sum Lower Bound Lemma** (elementary,
general-purpose, proved from scratch): for any $m$ distinct nonnegative
integers, $\mathrm{AltSum}\ge\lfloor m/2\rfloor$.

**Main theorem (proved in full, Section 12.4 of the approach file):**
within the Perfect-Tie family, the best achievable value at $e_0$ is
exactly $c(n)$ — **never strictly below** — and this is attained **only**
at $s=n-1$ (leaving exactly 2 pieces untouched); every smaller $s$
(whether the favorable or unfavorable parity of the untouched-set size)
provably exceeds $c(n)$. Consequently no fixed $s_0$ independent of $n$
ever suffices for this family. Independently verified in exact `Fraction`
arithmetic for $n=2,\dots,14$, every $s=0,\dots,n$ (117 instances,
brute-force over all $\binom{n+1}{s}$ active-set choices against the
literal constructed multiset, not just the closed-form): 100% exact
agreement, zero exceptions to the theorem's claim.

This is structurally independent of the round-11 Mass-Constraint Theorem
(disjoint construction family — no untouched piece's mass is ever
consumed as a tie target here — and a different proof technique: integer
combinatorics, not mass summation), so it is genuine new content, not a
restatement.

**Honest scope, verified numerically:** the Perfect-Tie restriction
(zero residual) is a proper sub-family of full fragment-vs-fragment
tying. An unrestricted numerical check (`scipy.optimize`, $n=6,s=3$)
found nonzero-residual constructions strictly beat the Perfect-Tie
optimum ($\approx0.5046$ vs. Perfect-Tie's exact $\approx0.5079$), though
still short of $c(6)\approx0.5039$ — consistent with, not contradicting,
the round's own numeric finding. **The fully general fragment-vs-fragment
question (nonzero residual, bounded $s$) remains open** — this round
does not claim to close it, only the natural maximally-efficient
sub-case, which is nonetheless a complete, rigorous, independently
verified result.

## What was NOT done
- No new lemma was self-certified into `lemmas/` (per instructions —
  left for the reviewer).
- The fully general fragment-vs-fragment family (arbitrary residual) is
  not resolved either way; flagged explicitly as open in the file
  (Section 12.5).
- No attempt was made to extend this to non-$e_0$ points of the region
  (out of scope for this round's dispatch).

## Recommendation
Combined with round 11's Mass-Constraint Theorem, this gives two
independent, disjoint, differently-proved negative results ruling out
bounded-piece-count named-tool families at $e_0$. Recommend
`global-lp-vertex-sufficiency` prioritize its Region-Boundary
Monotonicity route (Opening 2) over further search for a bounded
fragment-tying construction, as already suggested by the round-12
outliner. `lp-duality-split-polytope` Status remains `partial` (this is
a scoped contribution, not a resolution of the approach's overall
target).

File updated: `results/imo-2026-03/approaches/lp-duality-split-polytope.md`
(new "Round 12 update" summary near the top, full proof in new section
"Round 12: the Perfect-Tie-Family Exact Characterization at $e_0$" at the
end, Sections 12.0–12.6).
