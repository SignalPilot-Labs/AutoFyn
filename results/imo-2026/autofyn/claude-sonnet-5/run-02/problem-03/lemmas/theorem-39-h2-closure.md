# Lemma: Theorem 39 — full unconditional closure of $h(2)\ge f(2)$

**Source:** `approaches/greedy-halving-adversary.md`, round 25.

**Statement.** Let $q=(4,2,1)$ (the unit $2$-ladder in $f(2)$-units,
$\mathrm{Total}(q)=7=1/f(2)$), and define
$$h(2):=\inf\{A(\{c\}\cup S)\ :\ c\in(0,4],\ S\text{ a legal }(\le1)\text{-cut
refinement of }q\}.$$
Then $h(2)\ge1$ ($=f(2)$ in real scale), with equality attained exactly at
$c=4$ in the "$S$ untouched," "$q_1$-split," and "$q_2$-split" branches
(for every legal split parameter in the latter two), and strictly exceeded
throughout the open "$q_3$-split" branch.

**Proof sketch (full detail in the approach file).** Budget $\le1$ cut on a
3-piece ladder forces exactly 4 exhaustive, disjoint branches for $S$:
untouched, $q_1$-split, $q_2$-split, $q_3$-split. Round 24 closed the
untouched and $q_1$-split branches by hand. This round closes the
remaining two by a direct piecewise-linear-in-$c$ sweep across every
breakpoint of $S\cup\{c\}$ (not a vertex-restricted argument), for the
full continuum $c\in(0,4]$ and, within each branch, the full continuum of
the branch's own free split parameter ($y\in[1,2)$ for $q_2$-split,
$z\in[1/2,1)$ for $q_3$-split):
- $q_2$-split ($S=\{4,y,2-y,1\}$): $\min_c A=1$ for every $y\in[1,2)$,
  attained only at $c=4$.
- $q_3$-split ($S=\{4,2,z,1-z\}$): $\min_c A=3-2z>1$ strictly throughout
  (infimum $1$ approached only as $z\to1^-$, coinciding with the
  untouched-branch boundary).

**Independent verification (this reviewer, round 25).** Re-derived all
piecewise closed forms from scratch and checked them against $6000+$ dense
random exact-`Fraction` samples inside each open sub-interval of both
branches (zero mismatches), and checked the reported worst-case values
($1$ for $q_2$-split, $3-2z$ for $q_3$-split, both at $c=4$) against a
$40{,}000$-trial randomized search — see `/tmp/round-25/verify_theorem39.py`.

**Status.** Proved in full for $m=2$ ($n=6$), unconditional (no induction
hypothesis used — a direct, finite, exact computation). Does **not**
extend to $m\ge3$: the branch count grows combinatorially once the budget
exceeds $1$ cut, so this technique (direct exhaustive hand sweep) is not
claimed to scale further.

**Scope warning (important, added by reviewer).** This lemma closes only
the "$T'$-cuts-$p_4$" sub-case of Case (b)'s "$v\ge a$" branch at $n=6$.
It does **not**, combined with Theorem 37, establish that the *whole*
"$v\ge a$" branch is closed at $n=5$ or $n=6$ — Theorem 37 (covering the
complementary "$T'$-untouched" sub-case) has its own separate,
still-unaddressed gap (it proves only one vertex, $b=p_4$ symmetric
split, is a local closure; it does not rule out $b$ tied to a
non-maximal element of $T''$ being the true global minimizer within that
sub-case). See the round-25 proof-reviewer report for detail; do not cite
this lemma as closing more than its own stated scope.

**Certified by:** proof-reviewer, round 25 (Theorem 39 itself, and
Proposition 39, both correct; the approach file's combined "whole branch
closed" claim is explicitly NOT certified — see scope warning above).
