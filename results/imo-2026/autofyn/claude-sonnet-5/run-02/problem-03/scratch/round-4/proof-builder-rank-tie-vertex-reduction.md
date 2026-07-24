# Build report — rank-tie-vertex-reduction (round 4)

## What was done

Read the outline-reviewer's correction already recorded in the approach
file: the round-4 outline's claim ("cascading-halving hits the target for
every prefix length $k\in\{0,\dots,n\}$") was verified false by exact
`Fraction` arithmetic before build, with only $k=n-1,n$ confirmed to work
for $n=1,\dots,6$. Rather than leaving this as a numeric table, this build
produces a full, closed-form, general-$n$ proof of the corrected claim:

**Cascading-Halving-Family Theorem.** For the ladder $p_i=2^{n+1-i}/D$
($D=2^{n+1}-1$) and the response $R_k$ that cuts $p_1,\dots,p_k$ each into
two exact halves (producing two copies of the next rung, since
$p_i/2=p_{i+1}$), the resulting multiset $S_k$ satisfies
$$D\cdot A(S_k) = T(L) = \frac{2^{L+1}+(-1)^L}{3},\qquad L:=n-k,$$
so $A(S_k)=f(n)=1/D$ **iff** $L\in\{0,1\}$, i.e. $k\in\{n-1,n\}$, with
$A(S_k)$ strictly larger for every $k\le n-2$.

Proof route: (1) bookkeeping shows $S_k$ has $p_2,\dots,p_k$ at multiplicity
2, $p_{k+1}$ at multiplicity 3, $p_{k+2},\dots,p_{n+1}$ at multiplicity 1;
(2) the certified **Odd-Run Reduction Lemma** collapses this to the plain
alternating sum of the ladder's own tail $\{p_{k+1},\dots,p_{n+1}\}$; (3) a
short induction (geometric-series recurrence $T(L)=2^L-T(L-1)$) gives the
closed form; (4) elementary bounds show $T(L)>1$ for all $L\ge2$ and
$T(0)=T(1)=1$.

Also proved, as a corollary: $T(L)$ is non-decreasing (strictly for
$L\ge1$), so **no member of this family ever violates the lower-bound
conjecture** ($A(S_k)\ge f(n)$ always, with equality exactly at the two
predicted points) — the family is a clean, fully-settled sub-piece of the
larger open tie-vertex enumeration.

Every nontrivial numeric claim was checked with exact `Fraction` arithmetic
(no floats) for $n=1,\dots,8$, both against a direct sort-and-alternate-sum
on the raw multiset and against the odd-run-reduced form, before being
asserted in the writeup — zero mismatches.

## Where this leaves the approach

- Status remains `partial`. This closes one clean infinite sub-family
  (all $n$, all prefix lengths $k$) of the tie-vertex enumeration in closed
  form — a genuine general-$n$ result, not a numeric pattern — but the full
  enumeration (cross-ties as in the existing §3 $n=3$ example, non-prefix
  subsets of cut pieces, mixed multi-way ties, arbitrary compositions) is
  still open, as is the general upper bound.
- New lemma proposed for certification:
  `results/imo-2026-03/lemmas/cascading-halving-family-characterization.md`.
- Updated `results/imo-2026-03/approaches/rank-tie-vertex-reduction.md`:
  added a new "Round 4 build" section with the full theorem and proof, a
  round-4 bullet under "Approaches tried," and updated the "Full proof"
  absent-note to reference it. Did not touch `current.md` (reviewer-owned).

## Honest gaps

- Did not attempt the full general tie-vertex enumeration beyond this one
  sub-family.
- Did not attempt the upper-bound direction.
- The theorem only shows this family's two survivors *tie* the conjectured
  target; it does not independently prove they are the *global* minimum
  over all Xiang Yu responses (that would require ruling out every other
  vertex type too, which remains the open problem).
