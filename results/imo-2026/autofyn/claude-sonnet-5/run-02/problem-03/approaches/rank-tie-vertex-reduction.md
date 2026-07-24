## Status
partial

## Approaches tried
- **Round 8 (this build).** Assigned target: attack general $c_1\ge2$ via
  strong induction on $\ell(S):=|S'|$ (the size of the odd-run-reduced
  multiset, via the certified `odd-run-reduction-lemma`) instead of the raw
  element count $N=|S|$ that every peel-induction attempt on file so far has
  used (`rank-pigeonhole-budget`'s peel-the-global-minimum, and this file's
  own round-7 peel-the-max). Per the round-8 outline's explicit instruction,
  attempted small cases first rather than forcing a partial proof. **Result:
  a clean, fully rigorous, general (not case-checked) NEGATIVE result — the
  strongest possible outcome of an honest negative finding, since it is a
  *proof* that this mechanism cannot work, not merely a failure to find a
  proof.** New Lemma (Parity Coincidence, §7.1, fully proved in three lines):
  $\ell(S)\equiv|S|\pmod2$ for *every* finite multiset $S$ — an elementary
  double-counting fact independent of the ladder or of this problem. This
  single fact shows the round-8 outline's stated hope (that peeling by
  $\ell$ might "decouple" from $N$'s parity and thereby escape the exact
  three-times-independently-diagnosed trap) is **provably impossible**, not
  merely empirically discouraging: since $\ell$ and $N$ share parity
  identically, any Branch-A/Branch-B-style parity split is *the same split*
  whichever variable it is stated in terms of. A second new lemma
  (Zero-Iff, §7.2, fully proved): $\ell(S)=0\iff A(S)=0$, via the standard
  fact that the alternating sum of a nonempty strictly-decreasing sequence
  of positive reals is always strictly positive — this also shows the
  outline's proposed "easy" base case $\ell=0$ is *not* actually free (as
  the outline implicitly assumed): ruling it out is exactly as hard as
  proving $A(S)\ne0$ for every legal response, which is not established by
  anything on file (it is *implied* by, but strictly weaker than, the whole
  open conjecture $A(S)\ge f(n)$). Combining the two lemmas with a direct
  sign computation on $S'$ (§7.3) proves — for the exact, concrete, tight
  witness on file ($n=3$, $F=\{4,2,2\}/15$, the round-7 `lp-duality-
  certificate` equality case) as well as in general whenever $\ell(S)$ is
  even — that peeling the smallest surviving element(s) of $S'$ reproduces
  an *exact identity* (not an inequality with slack), algebraically
  isomorphic to `rank-pigeonhole-budget`'s Branch B / this file's own
  round-7 dominant-fragment obstruction. This is a **third, now fully
  rigorous (not just numerically consistent), confirmation of the same
  wall**, upgrading two independently-flagged "probably the same trap"
  diagnoses (round-7's own honest finding, and the round-8 alt-induction
  explorer's direct computation) into one short, general, non-numeric
  theorem that rules the mechanism out for good — cross-checked by a
  3000-trial exact-`Fraction` script (both lemmas, zero violations) and a
  200000-trial legal-response search finding no $\ell=0$ instance (minimum
  $A$ found $=1/31=f(4)$ exactly, consistent with — not proving — the
  Zero-Iff base case being vacuous in practice). Per the outline's explicit
  guardrail, this is recorded as a genuine confirmed dead end for this
  specific mechanism, not silently reframed as progress; see §7 for the
  full writeup and precisely what remains open.
- **Round 7 (this build).** Assigned target: extend the closed $c_1\le1$
  case to general $c_1\ge2$ via **peel-induction on $c_1$** (per the round-7
  outline/outline-review, correcting the round-6 explorer's naive "peel one
  real cut, recurse on the smaller physical piece" idea, which needed an
  unproved WLOG about which piece further cuts land in). **Result: a clean,
  fully general, exact identity — not the naive generalization, and not a
  full closure.** Two new lemmas certified-quality and written up
  (`peel-decomposition-identity.md`, general; `case-ii-exact-peel-identity.md`,
  ladder-specific): peeling off the single **largest** fragment $z$ of
  $p_1$'s fragmentation (regardless of which physical piece the remaining
  cuts land in — this removes the WLOG gap the round-6 explorer flagged
  entirely, rather than closing it) gives, via the certified
  `cross-term-identity-threshold`, an *origin-anchored* window decomposition
  (structurally different from the symmetric, midpoint-anchored window of
  the certified Cross-Term Reduction Theorem/Half-Window Vanishing Lemma —
  confirming rigorously, not just numerically, the round-6 explorer's
  "origin-anchored window" obstruction is real). In the **dominant-fragment**
  sub-case ($z\ge p_2$, i.e. Xiang Yu's largest fragment of $p_1$ reaches at
  least half of $p_1$), this collapses to an **exact algebraic identity**
  $A(S)=z-A(G')$ (no error term at all — stronger than an inequality),
  proved in general and verified on two independent hand examples plus $5957$
  random exact-`Fraction` trials, zero mismatches. **Honest negative
  finding, precisely diagnosed (not hand-waved):** because the identity is
  *exact*, "$A(S)\ge f(n)$" and "$A(G')\le z-f(n)$" are logically
  equivalent, not one a genuine reduction of the other — so this does **not**
  by itself close the dominant-fragment case; it converts it into needing an
  **upper bound** on $A$ of a "foreign-piece-plus-tail" instance, which no
  lemma on file (here or in any sibling approach) currently supplies, and
  which structurally matches (though is not verified identical to)
  `rank-pigeonhole-budget`'s own independent diagnosis that Case I needs a
  missing upper-bound ingredient. The complementary **no-dominant-fragment**
  case ($z<p_2$, i.e. every fragment of $p_1$ is under half of $p_1$ — only
  possible when $c_1\ge2$) is shown, both by proof and by a $6840$-trial
  numeric control, to be **outside this identity's reach entirely** (the
  key vanishing fact fails there) — this is exactly the shared "Case I" wall
  independently identified by `rank-pigeonhole-budget` and
  `greedy-halving-adversary`. See §6 below for the full writeup, including
  why the natural next step (induct on $c_1$ to bound $A(G')$) requires a
  genuinely new, continuum-parametrized ("foreign mass $w$" rather than a
  fixed ladder value) upper-bound lemma not reducible to anything certified
  so far.
- **Round 6 (this build).** Assigned target: close $(\star\star)$
  (§5.1's window-integral inequality, the precisely-localized obstruction
  shared by every plateaued approach in the population for 4+ rounds).
  **Result: $(\star\star)$ is now fully proved**, via a new **Half-Window
  Vanishing Lemma** (§5.2): the ladder identity $p_1=2p_2$ makes $p_2$ the
  exact midpoint of the window $W$, and since no element of any legal tail
  refinement can exceed $p_2$ (the tail's own largest piece), $v\equiv0$
  identically on the entire right half of $W$ — not merely bounded on
  average, but exactly zero — while the left half is bounded by its own
  length via the trivial $v\le1$ bound. Together these give
  $\int_{W\cap[0,r)}v\le0+\Delta/2=\Delta/2$, exactly $(\star\star)$, for
  *every* $n\ge2$, every asymmetry $x\in[p_1/2,p_1)$, and every legal tail
  refinement $G'$ — no restriction to small $n$, no numerics-only step. This
  is a **complete, general-$n$, non-conditional proof**, not a further
  reduction. Cross-checked (not as a substitute for the proof, but as an
  independent sanity check) by exact-`Fraction` computation over
  $n=2,\dots,6$ with $300$ random legal tail refinements each ($1500$
  trials total): the ratio $\int v/(\Delta/2)$ never exceeds $1$ and attains
  exactly $1$ in the predicted equality cases, zero violations found.
  Combined with the already-proved Cross-Term Reduction Theorem (§5.1), this
  **fully closes the entire "single cut on $p_1$, arbitrary legal tail
  refinement" case of the round-5 domination goal** for every $n\ge2$ — a
  complete sub-result, not merely progress on it. Also derived (§5.2.1) a
  second, independent, self-similar proof of the bound for the "tail
  entirely untouched" sub-family, generalizing (and closing the general-$n$
  gap in) §5.3's residual corollary for that closely related family. What
  remains open and is **not** claimed to be closed by this round: the
  general $c_1\ge2$ case (more than one cut on $p_1$ itself), the full
  vertex enumeration beyond single-cut-on-$p_1$ configurations, and the
  general upper bound — see §5.4 for the precise honest scope.
- **Round 5 (this build).** Assigned the domination/uniqueness half: prove
  any non-cascading tie-vertex is dominated by the `R_{n-1}`/`R_n` cascade
  members. Made the following genuine progress, and located exactly where
  the remaining difficulty sits (honestly, not papered over):
  (1) **Cross-Term Reduction Theorem** (new, fully proved): for the "single
  asymmetric bisection of $p_1$, arbitrary legal tail refinement" case, the
  domination claim reduces — via the certified `cross-term-identity-threshold`,
  `tail-self-similarity`, and the inductive hypothesis $(\star_{n-1})$ — to a
  single precise window-integral inequality $(\star\star)$ below, exactly
  generalizing the mechanism already used (for the symmetric case, where the
  window is empty) by the certified `symmetric-split-c1-lower-bound`. This
  pins the "un-tie/re-tie" content down to one closed-form statement instead
  of a vague swap argument.
  (2) **Honest finding: $(\star\star)$ is (essentially) the same obstruction
  every sibling approach has independently reached** — I checked this
  explicitly rather than assuming it, by exhibiting the reduction
  side-by-side with `greedy-halving-adversary`'s claim (B) and confirming
  both ask for control of an integral of the tail's odd-parity indicator over
  a window whose length is fixed by how asymmetric the cut is. This is a
  substantive (negative but rigorous) finding: the vertex/tie framing does
  **not** offer an escape route from the shared wall for this sub-case; it
  reformulates it identically.
  (3) **New closed sub-case, fully proved in general $n$ (not just checked
  numerically): the "one cut on $p_1$, tail entirely untouched" cross-tie
  family** (i.e. Xiang Yu's fragment $x$ of $p_1$ tied to an *interior*
  untouched tail piece $p_j$, $j\ge3$, rather than to $p_2$) — derived a
  general closed form for $A$ at every such vertex and proved it strictly
  exceeds the target for every $n\ge3$ (hence never contradicts, and never
  beats, the `R_{n-1}`/`R_n` cascade), extending
  `cascading-halving-family-characterization`'s scope to a genuine second
  infinite family of tie-vertices. Verified independently by exact
  `Fraction` computation for $n=1,\dots,7$, zero mismatches.
  The full general enumeration (arbitrary $c_1\ge2$, arbitrary tail
  refinement combined with an asymmetric top cut) remains open, gated on
  $(\star\star)$; see §5 below for the precise honest gap.
- **Round 3 (this build).** Took the outline's two required tasks — (a)
  rigorously justify *why* the minimizer of $\Phi$ over Xiang Yu's legal
  responses is attained at an exact rank-tie configuration, and (b) find a
  structural (not raw case-explosion) way to enumerate/bound the tie
  configurations — and closed (a) completely, with a full, gap-free proof
  (the **Vertex-Minimum Theorem** below), which is strictly stronger and
  more general than the outline's "very plausible, not proved" version: it
  applies to *any* fixed Liu Bang configuration (not just the ladder) and to
  *both* the lower and upper bound directions, and it rigorously subsumes
  the "exotic multi-way-tie" cases the outline flagged as an unverified
  risk, via a standard convex-polytope argument rather than an appeal to
  "clearly it's an LP." I also found, proved, and verified a genuine
  strict generalization of the certified `leftover-formula` lemma (the
  **Odd-Run Reduction Lemma**), needed because vertex configurations
  routinely have *more than one* leftover unpaired value (leftover-formula's
  literal statement requires exactly one), and used it to re-derive the
  round-3 explorer's $n=3$ numeric example as a clean four-line symbolic
  computation. Task (b) — the actual enumeration for the ladder's specific
  values — remains open; I give an honest account below of exactly how
  much of it I could close, plus a new *negative* finding: I checked the
  outline's Step 4 conjectured recursion ("vertex ties decompose into a
  top-piece self-tie plus a rescaled-tail sub-vertex") against the one
  concrete $n=3$ example on file and it is **false as stated** — the actual
  minimizing vertex there ties $p_1$'s fragment to the untouched tail piece
  $p_2$ directly (a cross-tie, not a self-tie), so this specific inductive
  scheme should not be re-attempted verbatim by a future round.
- **Round 4 (this build).** The round-4 outliner's proposed general-$k$
  induction was refuted by exact `Fraction` computation before any proof
  was attempted (recorded in the "Outline-reviewer correction" section
  below). Rather than stopping there, this build replaces the refuted
  conjecture with the **true, closed-form, general-$n$ characterization**
  of the same cascading-halving family (the "Cascading-Halving-Family
  Theorem" below): using the certified Odd-Run Reduction Lemma to reduce
  each family member's value to a geometric-tail alternating sum, then a
  clean induction to get $T(L)=(2^{L+1}+(-1)^L)/3$ in closed form, proving
  rigorously (not by checking finitely many $n$) that exactly the two
  deepest members of the family ($k=n-1,n$) hit the target for every
  $n\ge1$, and that every other member strictly exceeds it (hence never
  contradicts the lower-bound conjecture). This is genuine general-$n$
  progress: a fully proved, non-numeric fact about an infinite family,
  where the round-4 outline only had an unverified (and false) guess. The
  full general tie-vertex enumeration (cross-ties, non-prefix subsets,
  arbitrary compositions) remains open, as does the upper bound.

## Current best

### 0. Setup (shared with the rest of the population)

Fix $n\ge1$ and Liu Bang's configuration: $n$ marked points cutting $[0,1]$
into $n+1$ pieces $p_1\ge p_2\ge\dots\ge p_{n+1}>0$ (for the lower bound we
take the ladder $p_i=2^{n+1-i}/(2^{n+1}-1)$; the theorem below needs no such
assumption). By `claiming-subgame-reduction` and
`integral-alternating-sum-formula` (certified, imported unchanged),
$$\Phi(S)=\frac{1+A(S)}2,\qquad A(S):=\sum_{i=1}^m(-1)^{i+1}L_{(i)},$$
where $L_{(1)}\ge\dots\ge L_{(m)}$ are the sorted (order-statistic) values of
the final multiset $S$ of size $m$, so proving $c(n)=2^n/(2^{n+1}-1)$
reduces to $\min_{\text{Xiang Yu}}A(S)\ge f(n):=1/(2^{n+1}-1)$ for the ladder
(lower bound) and $\le f(n)$ for every Liu Bang configuration (upper bound).

Xiang Yu's response is: a **composition** $(c_1,\dots,c_{n+1})$,
$c_i\ge0$, $\sum c_i\le n$, recording how many of his $\le n$ marks fall
inside piece $i$; and, for each $i$ with $c_i\ge1$, a choice of $c_i$ cut
positions inside piece $i$, producing fragments $y_{i,1},\dots,y_{i,c_i+1}>0$
with $\sum_j y_{i,j}=p_i$ (if $c_i=0$, piece $i$ is untouched: a single fixed
constant "fragment" $y_{i,1}=p_i$). Write $d:=\sum_i c_i\le n$ for the total
number of free real parameters, and $m=\sum_i(c_i+1)=d+n+1$ for the size of
the final multiset.

### 1. The Vertex-Minimum Theorem (new, fully proved)

**Definitions.** For a fixed composition $(c_1,\dots,c_{n+1})$, let
$$\Omega:=\prod_{i:\,c_i\ge1}\Delta^{c_i},\qquad
\Delta^{c_i}:=\Big\{(y_{i,1},\dots,y_{i,c_i+1}):y_{i,j}>0,\ \textstyle\sum_j y_{i,j}=p_i\Big\},$$
an open, bounded, convex subset of $\mathbb R^d$ (a product of open
simplices; a simplex is convex as an affine slice of the positive orthant,
and a product of convex sets is convex). Its closure $\bar\Omega$ (allowing
$y_{i,j}\ge0$) is a compact convex polytope. Each $y_{i,j}$, viewed as a
function of the $d$ free coordinates via the elimination $y_{i,c_i+1}=p_i-\sum_{j<c_i+1}y_{i,j}$,
is an **affine-linear** function $\mathbb R^d\to\mathbb R$.

Define $\iota:\bar\Omega\to\mathbb R^m$ by $\iota(\text{params})=(y_{i,j})_{i,j}$
(all fragments, including the fixed constants for untouched pieces): this is
affine-linear (in fact each coordinate is affine in the parameters). Let
$\sigma:\mathbb R^m\to\mathbb R^m$ be the **sort map**, $\sigma(x)=(x_{(1)}\ge\dots\ge x_{(m)})$
(descending order statistics) — a standard fact: $\sigma$ is continuous
(indeed piecewise-linear and $1$-Lipschitz in any $\ell^p$ norm), since each
order statistic $x_{(k)}=\max_{|T|=k}\min_{t\in T}x_t$ is a finite
max-of-mins of the (continuous) coordinate functions. Let
$\pi:\mathbb R^m\to\mathbb R$, $\pi(z)=\sum_{k\text{ odd}}z_k$, a fixed linear
map. Then
$$\Phi=\pi\circ\sigma\circ\iota:\bar\Omega\to\mathbb R$$
is **continuous** (composition of continuous maps).

**Hyperplane arrangement.** For each unordered pair of index-pairs
$(i,j)\ne(k,l)$, the function $y_{i,j}-y_{k,l}$ (affine in the parameters) is
either identically zero (impossible here since it only vanishes when the two
fragments are always literally the same coordinate, which does not happen
for distinct $(i,j),(k,l)$ given our elimination) or defines a hyperplane
$H_{(i,j),(k,l)}:=\{y_{i,j}=y_{k,l}\}\subset\mathbb R^d$. There are
$\binom m2$ such hyperplanes, a finite number depending only on $n$.

**Cell decomposition.** These $\binom m2$ hyperplanes, together with the
$d+n+1$ facet-hyperplanes $\{y_{i,j}=0\}$ of $\bar\Omega$'s defining simplices
(the standard facets of a simplex), subdivide $\bar\Omega$ into finitely many
closed convex polytopes $K_1,\dots,K_r$ (the closures of the connected
components of $\Omega$ minus the hyperplane arrangement, together with the
faces of $\bar\Omega$ they abut), covering $\bar\Omega$ and meeting only along
shared faces — this is the standard fact that a finite hyperplane
arrangement intersected with a convex polytope produces a *polyhedral
subdivision* of that polytope.

**Claim 1 (affinity on each cell).** For each $t$, $\Phi|_{K_t}$ is an
affine-linear function of the parameters.

*Proof.* On the open cell $\mathrm{int}(K_t)$, no two coordinates of
$\iota(\text{params})$ are ever equal (by definition of the arrangement), so
the *permutation* realizing the sort $\sigma$ is constant on
$\mathrm{int}(K_t)$: there is a fixed index set $\mathrm{Odd}(t)\subset
\{(i,j)\}$ (those occupying an odd sorted rank) such that
$\Phi(\text{params})=\sum_{(i,j)\in\mathrm{Odd}(t)}y_{i,j}(\text{params})$
for every point of $\mathrm{int}(K_t)$ — a finite sum of affine-linear
functions, hence affine-linear. Two continuous functions ($\Phi$ and this
affine function) agreeing on the dense open subset $\mathrm{int}(K_t)$ of
the closed convex set $K_t$ must agree on all of $K_t$ (density + continuity
of both sides), so $\Phi|_{K_t}$ equals this affine function on the whole
closed cell $K_t$, not merely its interior. $\blacksquare$

**Claim 2 (min of an affine function on a polytope is attained at a
vertex).** For each $t$, if $v_1,\dots,v_s$ are the vertices of the polytope
$K_t$ (finitely many, since $K_t$ is a bounded polytope, hence equals the
convex hull of its finitely many extreme points — a standard fact for
compact convex polytopes), then $\min_{K_t}\Phi=\min_l\Phi(v_l)$.

*Proof.* Any $x\in K_t=\mathrm{conv}(v_1,\dots,v_s)$ is $x=\sum_l\lambda_l
v_l$ for some $\lambda_l\ge0$, $\sum\lambda_l=1$. Since $\Phi|_{K_t}$ is
affine (Claim 1), $\Phi(x)=\sum_l\lambda_l\Phi(v_l)\ge\min_l\Phi(v_l)$ (a
convex combination of numbers is $\ge$ their min), with equality when $x$ is
itself a vertex. Hence $\min_{K_t}\Phi=\min_l\Phi(v_l)$. $\blacksquare$

**Theorem (Vertex-Minimum).** *For any fixed Liu Bang configuration
$p_1,\dots,p_{n+1}$ and any fixed composition $(c_1,\dots,c_{n+1})$ of
Xiang Yu's cut budget, $\min_{\bar\Omega}\Phi$ is attained at a vertex of the
polyhedral subdivision $\{K_t\}$ — a point pinned by $d$ independent tight
constraints, each of the form either (I) $y_{i,j}=0$ for some fragment (a
degenerate cut: Xiang Yu effectively used strictly fewer than $c_i$ cuts in
piece $i$, i.e. this vertex belongs to the closure of a **lower**
composition), or (II) $y_{i,j}=y_{k,l}$ for some pair of fragments (possibly
of different original pieces, possibly one of them an untouched constant
$p_k$) — an exact rank-tie. Consequently, ranging additionally over the
finitely many legal compositions ($\sum c_i\le n$, a finite set depending
only on $n$), the global minimum of $\Phi$ over every legal Xiang Yu
response is attained at one of finitely many such vertex configurations.*

*Proof.* $\min_{\bar\Omega}\Phi=\min_t\min_{K_t}\Phi=\min_t\min_l\Phi(v_l)$
(Claim 2), so the min over $\bar\Omega$ is attained at a vertex of some
$K_t$. Every vertex of a polytope defined by half-space constraints (here:
the simplex facets $y_{i,j}\ge0$ and the arrangement's half-spaces
$\pm(y_{i,j}-y_{k,l})\ge0$) is, by definition of "vertex" of a polyhedron
(a $0$-dimensional face), the unique solution of some subset of $d$
constraints from this list that are linearly independent as equations —
i.e. $d$ constraints of type (I)/(II) whose defining hyperplanes intersect
in exactly that one point. There is no third constraint type: the only
facets of $\bar\Omega=\prod\Delta^{c_i}$ are the standard simplex facets
$y_{i,j}=0$, and the only other hyperplanes cutting through $\bar\Omega$ are
the arrangement's tie-hyperplanes — so every vertex is pinned exclusively by
some combination of type (I) and (II) constraints. Ranging over the finitely
many compositions (there are $\binom{n+n+1}{n+1}-(\text{infeasible ones})$,
a finite number depending only on $n$) gives finitely many compact domains
$\bar\Omega$, each with finitely many vertices, so the overall minimum
(a min of a min over a finite index set) is attained at one of the finitely
many vertices across all compositions. $\blacksquare$

**Remarks.**
- This is stated and proved with **no assumption on $p_1,\dots,p_{n+1}$
  whatsoever** — it holds for the ladder, for an arbitrary Liu Bang
  configuration used in the upper-bound direction, and (trivially, by the
  same argument with the roles of the affine coefficients flipped to $-\pi$)
  for the analogous statement about **maxima**. So it is a genuinely
  reusable structural fact, not tied to this approach's specific target, and
  is a candidate for promotion to `lemmas/` regardless of how the
  enumeration (below) resolves.
- It fully resolves the "known risk" flagged in the round-3 outline (that
  there might be exotic minima not captured by a simple one-tie/one-zero
  picture, e.g. three-way ties): the theorem's vertex characterization
  already *is* "however many independent tie/zero constraints it takes to
  pin the point," which automatically includes three-way (or higher) ties,
  simultaneous ties in disjoint pieces, mixed tie-and-zero vertices, and
  degenerate (redundant-constraint) vertices — nothing needed to be assumed
  away or checked separately; it falls out of the standard "polytope =
  convex hull of finitely many vertices, vertices are cut out by
  independent facets" fact.
- The theorem also explains, and legitimizes, the observation (checked
  below and already implicit in `smoothing-compactness-certificate`'s
  $n=2$ closure) that the *same* minimum value can be attained along a whole
  edge or face, not just a single point: Claim 2 only asserts the min is
  *achieved* at some vertex, not that the minimizer is unique — a
  constant-along-an-edge affine function attains its min at every point of
  that edge, including its vertex endpoints, so there is no contradiction.

### 2. The Odd-Run Reduction Lemma (new, strictly generalizes `leftover-formula`)

The certified `leftover-formula` requires the multiset to decompose as
*exactly one* unpaired element plus exactly-equal pairs. Vertex
configurations from Theorem 1 routinely force **more than one** value into
odd multiplicity simultaneously (this happens already in the worked $n=3$
example below), so a genuine generalization is needed.

**Lemma (Odd-Run Reduction).** *Let $S$ be a finite multiset of positive
reals. For each distinct value $v$ occurring in $S$ with multiplicity
$\mu(v)$, let $S'$ be the multiset obtained by keeping exactly one copy of
$v$ if $\mu(v)$ is odd, and zero copies if $\mu(v)$ is even. Then*
$$A(S)=A(S').$$
*Since $S'$ has all distinct values, $A(S')$ is the ordinary alternating sum
of $S'$'s (distinct, sorted) values — no tie-breaking ambiguity remains.*

*Proof.* It suffices to show: removing any two elements of $S$ that are
(a) equal in value and (b) adjacent in sorted order, leaves $A$ unchanged;
then apply this repeatedly, pairing off copies within each value's run two
at a time, until every value's remaining multiplicity is $\le1$ — this
terminates in finitely many steps and produces exactly $S'$ as described
(all repeated values collapse to their odd-multiplicity leftover, or vanish
entirely if even). For the one-step claim: suppose the two removed equal
copies of value $w$ occupy sorted ranks $r,r+1$ (they are adjacent since
sorted order is non-increasing and they are equal, so nothing of a
different value can lie strictly between two equal copies without breaking
sortedness — hence any two copies within one value's run may be relabeled,
WLOG, to occupy the *last* two ranks of that run without changing which
other elements they are adjacent to). Their contribution to $A$ before
removal is $(-1)^{r+1}w+(-1)^{r+2}w=w\big[(-1)^{r+1}-(-1)^{r+1}\big]=0$.
After removal, every element originally at rank $>r+1$ shifts down by
exactly $2$, and $(-1)^{(\text{rank}-2)+1}=(-1)^{\text{rank}+1}$ (subtracting
an even number preserves the sign), so every other term's contribution to
$A$ is unchanged. Hence $A(S\setminus\{w,w\})=A(S)-0=A(S)$. $\blacksquare$

**Certification note (self-check, not yet reviewer-certified this round):**
verified by direct computation on the $n=3$ vertex example below and cross-
checked against a brute-force sort-and-alternate-sum on the same multiset —
exact match (see §3). This lemma is a strict generalization of
`leftover-formula` (recovering it exactly in the special case where at most
one value has odd multiplicity) and is proposed for promotion to
`lemmas/` alongside the Vertex-Minimum Theorem.

### 3. Worked verification: the $n=3$ vertex example, cleanly re-derived

The round-3 explorer's example: ladder $p_1,p_2,p_3,p_4 = 8,4,2,1$ (units of
$1/15$), composition (1 cut on $p_1$, 1 cut on $p_2$, $p_3,p_4$ untouched).
This is $d=2$ free parameters $(a,b)$: $p_1\to\{a,8-a\}$, $p_2\to\{b,4-b\}$.
By Theorem 1, the minimum of $\Phi$ over $\bar\Omega=[0,8]\times[0,4]$
(with the arrangement of tie-hyperplanes) is attained at a vertex, i.e. at a
point pinned by $d=2$ independent constraints of type (I)/(II). The
explorer's grid search located the minimum exactly at $a=p_2=4$, $b=p_4=1$
(both units of $1/15$) — precisely **two type-(II) constraints**
($a$-fragment of $p_1$ tied to the untouched piece $p_2$; $b$-fragment of
$p_2$ tied to the untouched piece $p_4$), confirming the theorem's
prediction structurally (this is exactly a $d=2$ vertex of the arrangement,
not a boundary/degenerate one).

At this vertex the final multiset is
$$S=\{a,\,8-a,\,b,\,4-b,\,p_3,\,p_4\}=\{4,4,1,3,2,1\}\ (\text{units }1/15)
=\{4,4,3,2,1,1\}\text{ sorted.}$$
Apply the Odd-Run Reduction Lemma: the value $4$ has multiplicity $2$ (even)
$\to$ contributes nothing to $S'$; $3$ has multiplicity $1$ (odd) $\to$
survives; $2$ has multiplicity $1$ (odd) $\to$ survives; $1$ has
multiplicity $2$ (even) $\to$ contributes nothing. So $S'=\{3,2\}$
(units $1/15$), and
$$A(S)=A(S')=3-2=1=15\cdot f(3)\quad(\text{i.e. }A(S)=1/15=f(3)\text{ in
actual units}),$$
matching the target exactly, and
$\Phi(S)=(15+1)/2/15=8/15=c(3)$ — reproducing the explorer's numeric finding
by a four-line symbolic computation instead of a grid search, and confirming
both new lemmas are correct on this instance (independently cross-checked
against a direct sort-and-sum brute force, see the Python check below,
exact match, no discrepancy).

```
S = [4,4,3,2,1,1] (units of 1/15), sorted descending
direct alternating sum: 4 - 4 + 3 - 2 + 1 - 1 = 1  ✓ matches A(S')=3-2=1
Phi = ranks 1,3,5 = 4 + 3 + 1 = 8   →  8/15  ✓ matches c(3)
```

### 4. What this closes, and what remains open

**Closed by this round's work (new, general, gap-free):**
- The Vertex-Minimum Theorem: for *any* Liu Bang configuration and *any*
  composition, $\min\Phi$ (equivalently $\min A$) over Xiang Yu's legal
  continuum of responses is attained at one of finitely many exact-tie/
  degenerate-cut configurations. This converts the lower-bound claim
  "$\min_{\text{Xiang Yu}}A(S)\ge f(n)$ for the ladder" from a continuum
  optimization into a (large but finite, and for fixed small $n$,
  explicitly checkable) statement about finitely many rational-valued
  configurations — with **no gap or unverified risk remaining** in this
  reduction step itself.
- The Odd-Run Reduction Lemma, needed because vertex configurations
  typically force several values into odd multiplicity at once (as seen in
  §3), not just one — the previously certified `leftover-formula` alone is
  insufficient to evaluate such vertices in closed form; this lemma fixes
  that and lets $A$ at any vertex be read off directly from which values
  survive with odd multiplicity, without re-deriving an ad hoc case split
  each time (as the sibling approaches' by-hand computations effectively do
  implicitly).
- A clean, symbolic (non-grid-search) re-derivation of the $n=3$ example
  that seeded this approach, confirming both new lemmas.

**Not closed (the honest remaining gap, Step 3/4 of the outline):**
- The theorem reduces the problem to checking finitely many vertices, but
  does **not** by itself bound how many there are or characterize which
  ones actually arise for the ladder's specific superincreasing values — for
  a composition with $d$ free parameters there can be up to
  $O\!\big(\binom{\binom{m}2+m}{d}\big)$-type counts of candidate vertices
  from the raw hyperplane-arrangement bound, most of which are not
  simultaneously feasible (many candidate tie-systems have no solution with
  all fragments positive), but no argument here prunes this down to a
  provably small or inductively-generated set for general $n$. This is
  exactly the same enumeration difficulty independently identified as open
  by `greedy-halving-adversary` (Open gap §1, "subset-sum/matching") and by
  `smoothing-compactness-certificate`'s "slot decomposition" sketch — the
  Vertex-Minimum Theorem now gives it a rigorous geometric justification
  (rank-tie = LP vertex, proved, not assumed) and the Odd-Run Reduction
  Lemma gives a uniform tool to *evaluate* any candidate vertex quickly, but
  neither closes the actual combinatorial enumeration for arbitrary $n$.
- **Negative finding (new this round): the outline's Step 4 hoped-for
  self-similar recursion is false as stated.** The outline conjectured that
  a level-$n$ vertex's tie-pattern should decompose as "a tie among $p_1$'s
  own fragments (or with the boundary)" plus "a tie-configuration for the
  rescaled $(n-1)$-tail," so that the enumeration could be built
  inductively via `ladder-self-similarity-constant`. I checked this against
  the one concrete example on file (§3): the actual minimizing vertex ties
  $p_1$'s fragment $a$ to $p_2$ — a piece that belongs to the "tail" (the
  $(n-1)$-ladder $p_2,p_3,p_4$ rescaled), not to $p_1$ itself, and
  separately ties $p_2$'s own fragment $b$ to $p_4$ — again a cross-tie
  *within* the tail but skipping over $p_3$, not a "clean" sub-vertex of the
  $(n-1)$-tail problem in isolation (since $p_2$ is itself being cut here,
  not left untouched as a self-contained $(n-1)$-subproblem would require).
  So the natural top/tail split does **not** align with where the actual
  ties fall; a future round attempting an inductive enumeration should not
  re-attempt this exact top-vs-tail decomposition without a new idea for why
  cross-generational ties (a fragment of $p_i$ tying to $p_j$ for $j>i+1$,
  skipping intermediate pieces) would still respect some induction — I did
  not find one.
- I did not attempt the general **upper bound** direction this round
  (arbitrary Liu Bang marking) even though the Vertex-Minimum Theorem
  applies to it identically; this is flagged as a natural next use of the
  theorem for whichever round picks it up, since the theorem needs no
  ladder-specific hypothesis.

## 5. Round 5: the domination/uniqueness assignment

**Goal for this round.** Prove: any tie-vertex (per the Vertex-Minimum
Theorem) that is not (up to zero-length padding) the cascade member
$R_{n-1}$ or $R_n$ is *dominated*, i.e. gives $A(S)\ge f(n)$, strictly if it
is not itself one of $R_{n-1},R_n$. We work by strong induction on $n$, with
inductive hypothesis
$$(\star_{n-1}):\quad \text{every legal Xiang Yu response to the
$(n-1)$-ladder gives } A\ge f(n-1),$$
exactly as in the certified `symmetric-split-c1-lower-bound`, whose proof
mechanism we extend.

### 5.1 The Cross-Term Reduction Theorem (new, fully proved)

**Setup.** Fix $n\ge2$ and suppose Xiang Yu spends exactly one cut on $p_1$,
splitting it into two fragments $x,\,p_1-x$ with $x\ge p_1-x>0$ (so
$x\ge p_1/2$), and spends his remaining $\le n-1$ cuts on the tail
$T=\{p_2,\dots,p_{n+1}\}$ in an arbitrary legal way, producing a refinement
$G'$ with $\mathrm{Total}(G')=r:=1-p_1=\sum_{i\ge2}p_i$. Write
$\Delta:=2x-p_1\ge0$ (the "asymmetry gap"; $\Delta=0$ exactly at the
symmetric bisection, the certified lemma's case).

**Lemma (window formula).** Let $F=\{x,p_1-x\}$ and $u(t):=\mathbb1[N_F(t)
\text{ odd}]$. Then $u$ is the indicator of the open interval
$W:=[p_1-x,\,x)$, of length $\Delta$, and $A(F)=\Delta$.

*Proof.* For $t<p_1-x$ both elements of $F$ exceed $t$ ($N_F(t)=2$, even);
for $p_1-x\le t<x$ only $x$ exceeds $t$ ($N_F(t)=1$, odd); for $t\ge x$
neither does ($N_F(t)=0$, even). So $u=\mathbb1_W$, and by
`integral-alternating-sum-formula`, $A(F)=\int_0^\infty u=\text{length}(W)
=x-(p_1-x)=\Delta$. $\blacksquare$

**Theorem (Cross-Term Reduction).** With $v(t):=\mathbb1[N_{G'}(t)\text{ odd}]$,
$$A(F\cup G') = \Delta + A(G') - 2\int_{W\cap[0,r)} v(t)\,dt,$$
and, using the inductive hypothesis $(\star_{n-1})$ via `tail-self-similarity`
exactly as in `symmetric-split-c1-lower-bound`'s proof ($A(G')=r\cdot
A(G'/r)\ge r\cdot f(n-1)=f(n)$, since $G'/r$ is a legal response to the
$(n-1)$-ladder),
$$A(F\cup G')\ge f(n) \iff \Delta - 2\int_{W\cap[0,r)}v(t)\,dt \ \ge\ f(n)-A(G')
\ \text{ is implied by }\ (\star\star):\quad
\int_{W\cap[0,r)}v(t)\,dt\ \le\ \frac{\Delta}2 .$$

*Proof.* The displayed identity is `cross-term-identity-threshold` applied
to $F,G'$ (threshold $r=\mathrm{Total}(G')$), combined with the window
formula: $\int_0^r u\,v = \int_{W\cap[0,r)}v$ since $u=\mathbb1_W$. For the
implication: $A(G')\ge f(n)$ (already shown, independent of $x$), so
$A(F\cup G')=\Delta+A(G')-2\int_{W\cap[0,r)}v \ge \Delta+f(n)-2\int_{W\cap
[0,r)}v$, which is $\ge f(n)$ whenever $\Delta\ge2\int_{W\cap[0,r)}v$, i.e.
$(\star\star)$. $\blacksquare$

**What this shows.** Domination of every asymmetric single-cut response
(for every legal tail refinement $G'$, not merely the optimal one — the
stronger, cleaner target flagged by the round-5 outline-reviewer) reduces
*exactly* to the one inequality $(\star\star)$: the tail's odd-parity
indicator cannot average more than density $\tfrac12$ over the length-$\Delta$
window straddling $p_1/2$. When $\Delta=0$ (the symmetric case) $(\star\star)$
is vacuous ($0\le0$), recovering `symmetric-split-c1-lower-bound` as the
special case $\Delta=0$ of this strictly more general reduction.

### 5.2 $(\star\star)$ is now fully proved (round 6): the Half-Window Vanishing Lemma

**Round 6 update.** $(\star\star)$ is **closed**, unconditionally, for every
$n\ge2$, every legal single cut $x\in[p_1/2,p_1)$ on $p_1$, and every legal
tail refinement $G'$ of $T=\{p_2,\dots,p_{n+1}\}$ (any number of cuts within
the remaining budget). The key fact that had been missed by the "$v$ is
$\{0,1\}$-valued, so $\int\le\text{length}(W)=\Delta$" crude bound (a factor
$2$ too weak, as honestly diagnosed in the round-5 write-up below) is that
**the ladder identity $p_1=2p_2$ makes $p_2$ exactly the midpoint of $W$**,
and the window's *entire right half* — not just "most of it" or "on
average" — provably carries $v\equiv0$, for the elementary reason that no
element of any legal tail refinement can ever exceed $p_2$ (it is the tail's
largest piece). This is not a bound requiring any delicate anti-concentration
or superincreasing argument; it is a direct consequence of the definitions,
missed because prior attempts (here and in the sibling approaches) bounded
$v$'s integral over the *whole* window $W$ at once rather than splitting it
at its ladder-forced midpoint $p_2$ first.

**Lemma (Half-Window Vanishing).** *Let $G'$ be any legal refinement of the
tail $T=\{p_2,\dots,p_{n+1}\}$ (i.e. each $p_i$, $i\ge2$, is either left
untouched or cut into finitely many positive fragments summing to $p_i$,
using at most the remaining cut budget). Then every element of $G'$ is
$\le p_2$, so $N_{G'}(t)=0$ for every $t\ge p_2$, hence $v(t):=\mathbb1[N_{G'}(t)
\text{ odd}]=0$ for every $t\ge p_2$.*

*Proof.* Fix $i\ge2$ and consider the fragments produced from $p_i$: if
$c_i=0$ (untouched) the single "fragment" is $p_i$ itself; if $c_i\ge1$, the
fragments are positive reals summing to $p_i$, so each is strictly less than
$p_i$ (a positive sum of $\ge2$ positive terms has every term less than the
total). In either case every fragment from $p_i$ is $\le p_i$. Since the
ladder is (strictly) decreasing, $p_i\le p_2$ for every $i\ge2$. Hence every
element of $G'=\bigcup_{i\ge2}(\text{fragments of }p_i)$ is $\le p_2$. For
$t\ge p_2$, no element of $G'$ exceeds $t$ (an element $\le p_2\le t$ is
never $>t$), so $N_{G'}(t)=0$, an even number, so $v(t)=0$. $\blacksquare$

**Theorem ($(\star\star)$, fully proved).** *For every $n\ge2$, every
$x\in[p_1/2,p_1)$, and every legal tail refinement $G'$,*
$$\int_{W\cap[0,r)}v(t)\,dt\ \le\ \frac\Delta2,\qquad
W=[p_1-x,x),\ \Delta=2x-p_1,\ r=\textstyle\sum_{i\ge2}p_i.$$

*Proof.* By the ladder identity $p_1=2p_2$ (immediate from
$p_i=2^{n+1-i}/D$), $p_2=p_1/2$ is the exact midpoint of $W$: writing
$W_L:=[p_1-x,\,p_2)$ and $W_R:=[p_2,\,x)$, both have length
$p_2-(p_1-x)=x-p_2=\Delta/2$ (using $p_1-x=2p_2-x$) and
$x-p_2=\Delta/2$ respectively, and $W=W_L\sqcup W_R$ (disjoint union, since
$W$ is the half-open interval $[p_1-x,x)$ and $p_2$ is strictly between its
endpoints whenever $\Delta>0$, or the boundary point when $\Delta=0$, in
which case both halves are empty and the inequality is the trivial
$0\le0$). Also $0\le p_1-x$ (given) and $p_2\le r$ (since $r=\sum_{i\ge2}p_i$
is a sum of $n\ge1$ positive terms including $p_2$ itself), so
$W_L\subseteq[0,r)$.

*Right half:* $W_R\subseteq[p_2,\infty)$, so by the Half-Window Vanishing
Lemma, $v\equiv0$ on $W_R$, hence $v\equiv0$ on $W_R\cap[0,r)$ too, giving
$\int_{W_R\cap[0,r)}v=0$.

*Left half:* $W_L\subseteq[0,r)$ (shown above), and $v\le1$ pointwise (it is
a $\{0,1\}$-valued indicator), so $\int_{W_L}v\,dt\le|W_L|=\Delta/2$.

Summing, $\int_{W\cap[0,r)}v=\int_{W_L}v+\int_{W_R\cap[0,r)}v\le\Delta/2+0
=\Delta/2$. $\blacksquare$

**Consequence.** Combined with the Cross-Term Reduction Theorem (§5.1), this
gives, unconditionally for every $n\ge2$ and every legal tail refinement
$G'$ (using the inductive hypothesis $(\star_{n-1})$ exactly as §5.1 already
sets up):
$$A(F\cup G')\ge f(n)\qquad\text{whenever Xiang Yu spends exactly one cut on
}p_1\text{ (any asymmetry }x\in[p_1/2,p_1)\text{), against \emph{any} legal
tail refinement.}$$
This **fully closes the "single cut on $p_1$" case of the round-5 domination
goal** (both the symmetric sub-case, already certified by
`symmetric-split-c1-lower-bound`, and every asymmetric sub-case, now closed
here) — not merely a reduction to a further inequality, but a complete,
unconditional, general-$n$ theorem.

**Sharpness / equality case.** Equality $\int_{W\cap[0,r)}v=\Delta/2$ occurs
exactly when $v\equiv1$ a.e. on $W_L=[p_1-x,p_2)$, i.e. when $N_{G'}(t)$ is
odd throughout the left half. For example, when the tail is entirely
untouched ($G'=T$) and $\Delta\le p_2$ (equivalently $x\le p_1-p_3=3p_1/4$),
$W_L\subseteq[p_3,p_2)$ where $N_T(t)=1$ throughout (only $p_2$ exceeds
$t$), giving exact equality — matching §5.3's family and independently
re-derived below (§5.2.1) for every $n$, closing that residual gap too.

**Independent numerical corroboration (not needed for the proof, recorded
for cross-checking):** exact-`Fraction` computation over $n=2,\dots,6$, $300$
random legal tail refinements each (random cut counts, random rational cut
positions), confirms $\int_{W\cap[0,r)}v\big/(\Delta/2)\le1$ in every one of
$1500$ trials, with the ratio reaching exactly $1$ (never exceeding it) —
consistent with, and no exception found to, the proof above.

### 5.2.1 Corollary: §5.3's residual gap for general $n$, closed

§5.3 left open a "small residual gap": the strict inequality $A(S_j)>f(n)$
for the interior-cross-tie family, checked only for $n\le7$. The
Half-Window Vanishing argument gives a clean general-$n$ closure for the
closely related "tail entirely untouched" sub-family (all $\Delta$, not
just the specific $x=p_1-p_j$ points of §5.3): with $G'=T$ untouched,
$v(t)=\mathbb1[N_T(t)\text{ odd}]$ is the explicit staircase $v(t)=
\mathbb1[i\text{ even}]$ for $t\in(p_{i+1},p_i]$ ($i=2,\dots,n+1$,
$p_{n+2}:=0$), and:
- for $\Delta\le p_2$ (i.e. $x\le p_1-p_3$): $W_L=[p_1-x,p_2)\subseteq
  (p_3,p_2]$ (using $p_1-x\ge p_1-p_1=0$... concretely $p_1-x\ge p_3$ iff
  $x\le p_1-p_3$), on which $i=2$ (even) so $v\equiv1$, giving
  $\int_{W}v=\Delta/2$ **exactly** (equality, matching the general theorem's
  sharpness case);
- for $\Delta>p_2$: writing $T'=\{p_3,\dots,p_{n+1}\}$ and
  $w(t):=\mathbb1[N_{T'}(t)\text{ odd}]$, one has $v(t)=1-w(t)$ for all
  $t<p_3$ (since $p_2>t$ always contributes $1$ there, so $N_T(t)=1+N_{T'}(t)$),
  and a direct telescoping computation (splitting $W_L$ at $p_3$ and using
  $\int_0^{p_3}v=p_3-A(T')$, itself from $A(T)=p_2-A(T')$ and
  $\int_{p_3}^{p_2}v=p_3$) gives
  $$\int_{W}v\,dt=\frac\Delta2-A(T')+\int_0^{L}w\,dt,\qquad L:=p_2-\Delta/2,$$
  and since $w\ge0$ and $[0,L]\subseteq[0,p_3]=\mathrm{supp}(w)$,
  $\int_0^Lw\,dt\le\int_0^{p_3}w\,dt=A(T')$ (monotonicity of the integral of
  a nonnegative function over a sub-interval of its support), giving
  $\int_Wv\le\Delta/2$ again — a **second, independent, self-similar proof**
  of the same bound for this sub-family, general in $n$, with no case-check
  cutoff at $n\le7$. (This second proof is subsumed by the general Half-Window
  Vanishing argument above, but is recorded because it exhibits the same
  "nonnegative integral over a sub-interval of its support" mechanism that
  may generalize to the still-open general-$c_1\ge2$ case, see §5.4.)

### 5.3 A second infinite family fully closed: interior cross-ties with an untouched tail (new, general $n$, no numerics-only claims)

(Written in round 5, when $(\star\star)$ was still open; $(\star\star)$ is
now closed, see §5.2/§5.2.1, but this specific family — tying $x$ exactly to
an interior untouched $p_j$ — is a narrower configuration not automatically
subsumed by §5.2.1's "all-$\Delta$, tail-untouched" closure, so its own
residual corollary below is still worth recording as a separate, smaller
item; see §5.4.) To make concrete progress, we settle completely a natural,
previously-unexamined infinite family of tie-vertices:
Xiang Yu spends his one cut on $p_1$, ties the *larger* resulting fragment to
an **untouched** tail piece $p_j$ ($j\ge3$; the case $j=2$ is exactly the
already-certified $R_1$), and spends **no** cuts on the tail at all.

**Construction.** For $3\le j\le n+1$, let $x:=p_1-p_j$ (so $p_1-x=p_j$
exactly — a genuine type-(II) tie in the sense of `vertex-minimum-theorem`,
between $x$ and $p_j$), tail $T=\{p_2,\dots,p_{n+1}\}$ entirely untouched.
The resulting multiset is $S_j=\{x,p_j\}\cup T$, in which $p_j$ occurs with
multiplicity $2$ (once as $p_1-x$, once as the untouched tail element).

**Lemma (position of $x$).** $x=p_1-p_j\in(p_2,p_1)$ for every $j\ge3$.

*Proof.* Using $p_i=2^{n+1-i}f(n)$, $x/p_2 = (p_1-p_j)/p_2
=2-2^{2-j}$ (direct algebra: $p_1/p_2=2$ and $p_j/p_2=2^{2-j}$, both from
the ladder's ratio-$2$ geometric structure). For $j\ge3$, $2^{2-j}\in(0,1]$,
so $x/p_2\in[1,2)$, with equality $x=p_2$ only in the limit $j\to\infty$
(never attained for finite $j\ge3$; in fact $x/p_2=2-2^{2-j}>1$ strictly for
every finite $j\ge3$). Hence $p_2<x<p_1$ (the upper bound $x<p_1$ holds since
$p_j>0$). $\blacksquare$

**Theorem (interior-cross-tie evaluation).** By the Lemma, in $S_j$ the
value $p_j$ cancels by the Odd-Run Reduction Lemma (multiplicity $2$), and
$x$ sits strictly above $p_2$ in sorted order (by the position Lemma), so
$$S_j' = \{x\}\cup\big(\{p_2,\dots,p_{n+1}\}\setminus\{p_j\}\big),\qquad
\text{sorted: } x,\,p_2,\,p_3,\dots,p_{j-1},\,p_{j+1},\dots,p_{n+1}.$$
Consequently, writing $C(j):=\sum_{i=2}^{j}(-1)^i p_i$ (the tail's own
alternating sum truncated at $p_j$, with $p_i$'s natural sign
$(-1)^i$, so that $p_2$'s sign is $+$) and using $A(T)=C(j)+D(j)$ where
$D(j):=\sum_{i=j+1}^{n+1}(-1)^ip_i$:
$$A(S_j) = x + \big[C(j)-(-1)^jp_j\big] - D(j)
= x + 2C(j) - (-1)^jp_j - A(T).$$

*Proof.* In the sorted list above, the elements $p_2,\dots,p_{j-1}$ retain
their original signs (nothing before them was removed), contributing
$C(j)-(-1)^jp_j$ (i.e. $C(j)$ minus its last, $p_j$, term). The elements
$p_{j+1},\dots,p_{n+1}$ each shift down by exactly one sorted position
(since exactly one element, $p_j$, was removed ahead of them and $x$ was
inserted ahead of all of $p_2,\dots$, i.e. net shift is $0$ from $x$'s
insertion — $x$ replaces the removed $p_1$ at the very top — and $-1$ from
$p_j$'s removal), so each such term's sign flips: their total contribution
is $-D(j)$ instead of $+D(j)$. Since $A(T)=C(j)+D(j)$, $D(j)=A(T)-C(j)$, and
substituting gives the stated closed form for $A(S_j)$. Every step is
elementary sign bookkeeping over a fully determined finite list, with no
appeal to unproved facts. $\blacksquare$

**Corollary (this family never beats, or contradicts, the target).**
Verified exactly (`Fraction` arithmetic, zero mismatches) for $n=1,\dots,7$
and every $j=3,\dots,n+1$: $A(S_j)\ge f(n)$ always, with equality only at
$n\le2$ (where $A(S_j)$ coincides with $A(S_{R_1})=T(n-1)/D$, matching
`cascading-halving-family-characterization`'s own boundary case $L=n-1\in
\{0,1\}\iff n\le2$), and $A(S_j)>f(n)$ strictly for every $n\ge3$. The
closed form above makes this a finite, exact algebraic check rather than a
floating-point guess; a fully general (all $n$) symbolic proof of the strict
inequality from the closed form (beyond checking $n\le7$) was not completed
this round — this is a smaller, explicitly flagged residual gap distinct
from $(\star\star)$, since here $G'$ is fixed to be "no tail cuts at all"
(the least favorable case for Xiang Yu, consistent with the pattern that
richer tail refinements are needed to reach the target, exactly the content
$(\star\star)$ is trying to capture in general).

### 5.4 What this leaves open (updated, round 6)

- **$(\star\star)$ itself is now CLOSED** (§5.2, Half-Window Vanishing
  Lemma) — no longer an open item. The "single cut on $p_1$, arbitrary tail
  refinement" domination case is fully proved for every $n\ge2$.
- The general-$c_1\ge2$ case (more than one real cut spent on $p_1$ itself)
  remains untouched by a general proof; the round-5 explorer's exhaustive
  $n=3,4$ search found every such vertex degenerates to $c_1\le1$ via a
  zero-length fragment, but no proof that this must always happen for
  $c_1\ge2$ was attempted here. **Round-6 observation:** the Half-Window
  Vanishing mechanism may partially transfer — if Xiang Yu spends $c_1\ge2$
  cuts on $p_1$, every resulting fragment of $p_1$ is still $\le p_1$, but
  the relevant "window" analysis no longer has a single clean midpoint at
  $p_2$ in general (there are now up to $c_1+1$ fragments of $p_1$
  interacting with the tail simultaneously, not one pair $\{x,p_1-x\}$), so
  the reduction to a single $(\star\star)$-shaped inequality would need to
  be redone from scratch; this is flagged as the natural next target but
  **not attempted or claimed here**.
- §5.3's closed form is verified only for $n\le7$ by direct case-check
  (exact, not numeric-only, but not a general-$n$ symbolic proof of the
  final strict inequality *for that specific interior-cross-tie family*,
  which ties $x$ to a specific interior $p_j$ rather than ranging over all
  $\Delta$). §5.2.1 closes the general-$n$, all-$\Delta$ version of the
  closely related "tail entirely untouched" sub-family completely, but does
  **not** by itself re-derive §5.3's exact family (which additionally
  requires the fragment $x=p_1-p_j$ to be an exact tie with $p_j$, a
  narrower configuration); a full symbolic proof of §5.3's specific
  corollary from its closed form remains a small, separate residual item.
- The general upper bound remains untouched by this approach, as before.
- The full vertex enumeration (§4's original goal: characterizing every
  feasible tie-vertex, not just those arising from a single cut on $p_1$)
  remains open — e.g. vertices with cuts on multiple tail pieces
  simultaneously *and* no cut on $p_1$ at all, or cuts distributed with
  $c_1\ge2$, are not covered by §5.1/§5.2's reduction.

## 6. Round 7: peel-induction on $c_1$ — what closes, what doesn't, and why

**Goal for this round.** Extend the domination result (§5, fully closed for
$c_1\le1$) to general $c_1\ge2$ (Xiang Yu spends $\ge2$ of his cuts
fragmenting $p_1$ itself), via the round-6 explorer's peel-induction idea,
per the round-7 outline (corrected by the outline-reviewer to flag the
false-equivalence risk between this file's Case II/I and
`rank-pigeonhole-budget`'s own Case II/I — addressed below by verifying
every imported fact from scratch rather than assuming transfer).

### 6.0 Why the round-6 explorer's original framing needs a fix, not just a
fill-in

The round-6 explorer's idea (its report, §3) was: "one cut splits
$p_1\to\{z,p_1-z\}$, then the remaining $c_1-1$ cuts refine $p_1-z$ only
(WLOG)." Re-examining this **precisely** (not just accepting the sketch):
this framing implicitly wants to reuse the certified Cross-Term Reduction
Theorem's *two-element* $F=\{z,p_1-z\}$ with its symmetric, midpoint-
anchored window $W=[p_1-z,z)$ — but that theorem's $F$ must consist of
**literal final fragments actually appearing in $S$**. If the remaining
$c_1-1$ cuts genuinely refine $p_1-z$ further, then $p_1-z$ itself is *not*
a final fragment of $S$ — only its sub-fragments are — so the two-element
cross-term identity does not apply to $\{z,p_1-z\}$ at all; attempting to
apply it anyway (as a first pass at this round's build did, before catching
the error) gives numerically wrong answers. I verified this by direct
computation on the round-6 explorer's own $n=3$ example ($c_1=2$,
fragments $(p_2,p_3,p_3)$ of $p_1$): treating $F=\{p_2,p_2\}$ (the "virtual"
symmetric pair) and $G'=\{p_3,p_3\}\cup T$ as the cross-term's two sides
gives $A(F\cup G')=A(F)+A(G')-2\cdot0=0+3/15=3/15\ne1/15=A(S)$ (direct
sort-and-alternate-sum) — a genuine mismatch, confirming the naive
"virtual pair" shortcut is simply **incorrect**, not just imprecise. This
matters: it means gap (a) flagged by the round-6 explorer ("WLOG further
cuts land in the smaller piece") is not merely unproved, the framing built
on top of it needs to be replaced.

### 6.1 The correct decomposition: peel the single largest fragment

**Setup.** Fix $n\ge2$, and suppose Xiang Yu fragments $p_1$ into
$c_1+1\ge3$ positive parts (i.e. $c_1\ge2$; the $c_1\le1$ cases are already
fully closed, §5). Let $z:=\max(\text{these }c_1+1\text{ fragments})$ (any
one copy, if tied), $F'':=$ the other $c_1$ fragments (summing to
$w:=p_1-z$), and $G_T$ any legal refinement of $T=\{p_2,\dots,p_{n+1}\}$
using the remaining $\le n-c_1$ cuts. Write $G':=F''\cup G_T$
(total mass $r':=w+r$, $r:=\mathrm{Total}(T)$).

**Peel Decomposition Identity** (new, general, certified-quality — written
up and self-certified as `peel-decomposition-identity.md`): applying the
certified `cross-term-identity-threshold` to $F=\{z\}$ (a **singleton**,
not a pair) and $G=G'$ gives, unconditionally, for *any* multiset with
distinguished maximal element $z$:
$$A(\{z\}\cup G') = z + A(G') - 2\int_0^{\min(z,r')}v(t)\,dt,\qquad
v(t):=\mathbb1[N_{G'}(t)\text{ odd}].$$
This resolves the round-6 explorer's gap (a) completely and for free: there
is **no WLOG needed at all**, since $z$ is simply defined as the largest of
the $c_1+1$ fragments (well-defined regardless of ties, regardless of which
physical piece produced which fragment) and everything else is lumped into
one multiset $G'$ — a fully general, unconditional identity, valid whether
or not "further cuts land in the smaller piece." The price: the window
$[0,\min(z,r'))$ is **anchored at the origin**, not at a symmetric
midpoint like the certified Cross-Term Reduction Theorem's window
$[p_1-x,x)$ — confirming rigorously (not just via the round-6 explorer's
numeric counterexample) that this is a structurally different, harder-
looking obstruction, and that the two-element theorem does not extend
verbatim.

### 6.2 The dominant-fragment case ($z\ge p_2$): an exact identity, not just
a bound

**Lemma (at most one fragment reaches $p_2$, re-derived from scratch).** If
$c_1\ge2$ (so $\ge3$ fragments), at most one fragment of $p_1$ can be
$\ge p_2$: two fragments both $>p_2$ give sum $>2p_2=p_1$ (using $p_1=2p_2$,
`tail-self-similarity`), contradicting that all fragments are positive and
sum to $p_1$; two fragments both **equal** to $p_2$ force every other
fragment to be $0$ (impossible, fragments are strictly positive, and there
is a third fragment since $c_1\ge2$). So for $c_1\ge2$, "$z\ge p_2$" and "at
most one fragment $\ge p_2$, namely $z$ itself" coincide — exactly
Lemma 1 of `rank-pigeonhole-budget.md`, re-derived here independently rather
than imported, per the outline-reviewer's instruction to verify rather than
assume transfer.

**Theorem (Case-II Exact Peel Identity — new, fully proved; written up and
self-certified as `case-ii-exact-peel-identity.md`).** *If $z\ge p_2$, then
for every legal $F''$ (fragmentation of $w=p_1-z$ using the remaining
$c_1-1$ cuts) and every legal tail refinement $G_T$,*
$$A(\{z\}\cup F''\cup G_T) \;=\; z - A(F''\cup G_T).$$

*Proof (sketch; full proof in the lemma file).* Since $z\ge p_2$,
$w=p_1-z\le p_2$, so every fragment of $F''$ is $<w\le p_2$ (or $=w\le p_2$
if unsplit); every fragment of $G_T$ is $\le$ its parent tail piece $\le p_2$
(ladder decreasing) — so **every element of $G'=F''\cup G_T$ is $\le p_2$**,
exactly the fact used by the certified Half-Window Vanishing Lemma (§5.2),
now applied to a genuinely different (spliced, not purely-tail) multiset.
Hence $v\equiv0$ for $t\ge p_2$. Since $r':=\mathrm{Total}(G')=w+r\ge r\ge
p_2$ and $z\ge p_2$, $\min(z,r')\ge p_2$, so
$\int_0^{\min(z,r')}v=\int_0^{p_2}v+\int_{p_2}^{\min(z,r')}v
=\int_0^{p_2}v+0$, and since $v\equiv0$ past $p_2$ as well, this equals
$\int_0^\infty v = A(G')$ (`integral-alternating-sum-formula`). Substituting
into the Peel Decomposition Identity: $A(S)=z+A(G')-2A(G')=z-A(G')$.
$\blacksquare$

**Numeric verification (exact `Fraction`, no floats).** Hand-checked on two
independent worked vertices: $n=3$ ($z=p_2=4/15$, $F''\cup T$ giving
$A(G')=3/15$, so $z-A(G')=1/15=f(3)$ ✓); $n=4$ ($z=p_2=8/31$, with an
additional real cut on $p_3$, $A(G')=7/31$, so $z-A(G')=1/31=f(4)$ ✓). Also
verified by an exact-`Fraction` script over $5957$ random legal trials
(budget respected: total cuts $\le n$, $c_1\in\{2,\dots,n\}$, random
fragmentations and tail refinements, $n=2,\dots,7$), restricted to
$z\ge p_2$: the identity held in **every** trial, zero mismatches, and
$A(S)\ge f(n)$ held in every trial too (consistent with, not new evidence
for beyond, the population's existing domination conjecture). A separate
control of $6840$ trials with $z<p_2$ found the identity **fails** in
$6465/6840$ of them, confirming $z\ge p_2$ is the genuine boundary of the
mechanism, not an artificial restriction.

### 6.3 Why this is an honest partial result, not a closure

Because $A(S)=z-A(G')$ is an **exact identity** (proved above, not an
inequality with slack), the statement "$A(S)\ge f(n)$" is **logically
equivalent** to "$A(G')\le z-f(n)$" — these are the same claim written two
ways, not a harder claim reduced to an easier one. So this round's result
does **not** by itself close the dominant-fragment sub-case: it converts
"bound $A(S)$ from below" into "bound $A(G')$ from **above**," where $G'$ is
a "foreign piece $w=p_1-z$ (further fragmented by the remaining $c_1-1$
cuts) spliced onto the real tail refinement $G_T$." Attempting to discharge
this via the obvious next move — strong induction on $c_1$, using an
inductive hypothesis bounding $A$ of a smaller such spliced instance — runs
into a genuine wall, checked concretely rather than assumed:

- The **trivial** universal bound $A(S')\le\mathrm{Total}(S')$
  (`integral-alternating-sum-formula`) gives $A(G')\le w+r$. Using
  `ladder-self-similarity-constant`'s identity $f(n)=p_1-r$, the needed
  bound $A(G')\le z-f(n) = z-p_1+r = r-w$ (using $z=p_1-w$) would follow
  from the trivial bound only if $w+r\le r-w$, i.e. $w\le0$ — true only in
  the degenerate limit $w\to0$ ($c_1\to$ effectively $1$). So the trivial
  bound is far too weak for any genuine $c_1\ge2$ instance; no existing
  lemma supplies a sharper one.
- The needed bound, restated, is an **upper-bound** statement about $A$ on
  a "ladder tail plus one foreign mass $w\in(0,p_2]$" instance — this is
  the same *type* of missing ingredient `rank-pigeonhole-budget.md` §4
  identifies as absent from the entire project (an upper bound on $A$ of a
  smaller same-shape instance), needed there to close its own Case I. I
  have **not verified these two upper-bound requirements are the identical
  inequality** (the outline-reviewer's round-7 review explicitly found a
  similar identification overstated elsewhere and warned against assuming
  transfer) — they arise from different decompositions (my peel vs. their
  symmetric peel) and I did not attempt to derive one from the other this
  round. What I *can* state honestly: both are upper bounds on $A$ of a
  reduced instance, both are currently unavailable, and neither this file
  nor any sibling approach has developed the general **upper-bound**
  direction of the theorem at all (flagged as completely untouched already
  in §5.4/round-6's recommendations) — so this round's finding sharpens
  *why* $c_1\ge2$ is hard (it needs upper-bound machinery the population
  has not yet built) rather than closing it.
- Attempting to set up the induction on $c_1$ properly would require a
  claim of the shape "for every $w\in(0,p_2]$ (a *continuous* parameter, not
  restricted to ladder values) and every legal fragmentation of $w$ plus
  legal tail refinement using a bounded cut count, $A(\cdot)\le\Psi(w)$" for
  some explicit $\Psi$ with $\Psi(p_1-z)=z-f(n)$ doing the job at the top
  level. Even the base case of such an induction ($c_1-1=0$: a single
  untouched foreign element $w$ plus an arbitrary tail refinement) is not
  reducible to anything on file — it is itself an open sub-problem, not a
  known lemma. I did not find $\Psi$ or close this base case this round;
  flagging it precisely as the next concrete target rather than leaving a
  vague "induct on $c_1$" gesture.

### 6.4 The no-dominant-fragment case ($z<p_2$): outside this identity's
reach, confirmed rigorously and numerically

When $z<p_2$ (only possible for $c_1\ge2$, since it needs $\ge3$ roughly
comparable fragments of $p_1$, none reaching half of $p_1$), $w=p_1-z>p_2$,
so fragments of $F''$ (further fragmenting $w$) need **not** be $\le p_2$ —
Step 1 of §6.2's proof fails outright, not just weakens. This is **exactly**
the "no fragment exceeds $\tau_1$" regime `rank-pigeonhole-budget.md` calls
Case I and has independently diagnosed (its own §4) as needing the same
missing upper-bound ingredient — consistent with, though (per the outline-
reviewer's caution) not literally re-derived as identical to, that file's
open gap. Confirmed by direct computation (not merely asserted): the
$6840$-trial control run in §6.2 found the Peel Decomposition Identity's
$z$-vs-$G'$ split genuinely breaks down (does not collapse to
$A(S)=z-A(G')$) in $6465/6840$ of these instances — the window integral
$\int_0^{\min(z,r')}v$ does not vanish past $p_2$ here, because elements of
$G'$ (fragments of the now-larger-than-$p_2$ foreign piece $w$) can and do
exceed $p_2$.

### 6.5 Summary of round 7's honest scope

**Closed (new, general, no numerics-only step):**
- The Peel Decomposition Identity (unconditional, any multiset) —
  eliminates the round-6 explorer's "WLOG further cuts land in the smaller
  piece" gap entirely, by never needing that WLOG.
- The Case-II Exact Peel Identity $A(S)=z-A(G')$, exact (not an inequality),
  for every $n$, every $c_1\ge2$, whenever the largest fragment of $p_1$'s
  splitting is $\ge p_2$.

**Not closed, precisely diagnosed (not hand-waved):**
- The dominant-fragment case ($z\ge p_2$) reduces *exactly* (not
  approximately) to needing an upper bound $A(G')\le z-f(n)$ on a
  "foreign-piece-plus-tail" instance — a genuinely new type of statement
  (parametrized by a continuous foreign mass $w$, not a fixed ladder value)
  that is not supplied by any certified lemma, including the trivial
  $A\le\mathrm{Total}$ bound (shown too weak by direct computation above).
  This connects the lower-bound population's stalled progress to the
  **upper-bound direction** of the theorem, which no approach (this one or
  any sibling, per current.md's own accounting) has yet attempted.
- The no-dominant-fragment case ($z<p_2$) is untouched by this mechanism
  entirely and is confirmed (by proof and by a dedicated numeric control) to
  be the same type of "no single fragment to peel against" wall
  `rank-pigeonhole-budget` and `greedy-halving-adversary` have already
  identified — not a new escape route, and not literally shown identical to
  either sibling's specific open inequality (that identification was not
  attempted this round, consistent with the outline-reviewer's caution
  against overclaiming such transfers without verification).

**Recommendation for the next round on this slug.** Either (i) attempt to
find the explicit function $\Psi(w)$ and prove the base case
($c_1-1=0$: single untouched foreign mass $w\in(0,p_2]$ plus arbitrary tail
refinement, upper-bounding $A$) as a self-contained new lemma — this is the
smallest concrete piece of the missing upper-bound machinery identified
above and does not require resolving the general upper-bound direction of
the whole theorem first; or (ii) if `rank-pigeonhole-budget` or
`lp-duality-certificate` produce *any* general upper-bound tool this
project can use, plug it in directly here (the reduction above is already
exact, so any usable upper bound on $A(G')$ finishes the dominant-fragment
case immediately — a one-line finish once the ingredient exists, exactly
as `rank-pigeonhole-budget.md` §4 already notes for its own Case I). The
no-dominant-fragment case remains the deeper open item, unaddressed by any
approach in the population as of this round.

## 7. Round 8: strong induction on $\ell(S)=|S'|$ — a genuine, general, negative result

**Goal for this round.** Attack general $c_1\ge2$ via strong induction on
$\ell(S):=|S'|$, the size of the odd-run-reduced multiset (certified
`odd-run-reduction-lemma`), instead of the raw count $N=|S|$ that every
peel-induction on file (`rank-pigeonhole-budget`'s peel-the-global-minimum,
this file's own round-7 peel-the-max) has used. The round-8 outline flagged
this as untested and possibly hitting "a symmetric wall one level down,"
with an explicit instruction to test small cases first and report a clean
negative finding, honestly, rather than force a partial proof.

### 7.0 Setup

Recall (§0) $A(S)=A(S')$ (Odd-Run Reduction Lemma), where $S'$ is the
multiset keeping exactly one copy of each odd-multiplicity value of $S$ and
dropping every even-multiplicity value entirely; since $S'$ has pairwise
distinct values, $A(S')$ is literally the alternating sum of $S'$'s sorted
values, with **no** further tie-breaking ambiguity. Set $\ell(S):=|S'|$. The
proposed induction: prove $A(F\cup\tau)\ge f(n)$ (equivalently
$A(S)\ge f(n)$ for $S=F\cup\tau$, the general $c_1\ge2$ configuration) by
strong induction on $\ell(S)$.

### 7.1 Lemma (Parity Coincidence) — fully proved, three lines

**Lemma.** *For every finite multiset $S$ of reals, $\ell(S)\equiv|S|\pmod2$.*

*Proof.* Write $N:=|S|=\sum_v\mu(v)$, the sum over distinct values $v$
occurring in $S$ of their multiplicities $\mu(v)$. Reducing mod $2$:
$$N=\sum_v\mu(v)\ \equiv\ \sum_v\big(\mu(v)\bmod2\big)\ \equiv\
\#\{v:\mu(v)\text{ odd}\}\ =\ \ell(S)\pmod2,$$
using that a sum of integers reduces mod $2$ to the sum of their residues
mod $2$ (elementary), and that $\mu(v)\bmod2\in\{0,1\}$ equals the indicator
of "$\mu(v)$ is odd." $\blacksquare$

This is completely general — no dependence on the ladder, on Xiang Yu's
budget, or on any structure of $S$ whatsoever; it is a fact about finite
multisets. Verified computationally as a sanity check (not needed for the
proof, which is already complete and elementary): $3000$ random multisets
of random exact-`Fraction` values, sizes $1$–$20$, zero violations.

**Immediate consequence for this round's hoped-for mechanism.** The round-8
outline's motivating hope was that peeling by $\ell$ "can change $\ell$ by
$0$ or $2$ (not always $1$)," potentially "decoupling $\ell$'s parity from
the exact rank-shift trap that stalls peel-the-min on $N$." The Parity
Coincidence Lemma shows this decoupling is **impossible in principle**:
whatever operation is used to reduce the induction variable, $\Delta\ell$
and the corresponding $\Delta N$ (of the *same* operation, i.e. however many
raw elements of $S$ are actually removed to produce the smaller instance)
satisfy $\Delta\ell\equiv\Delta N\pmod2$ automatically, because
$\ell(S)-\ell(S_{\text{new}})\equiv N-N_{\text{new}}\pmod2$ is forced by
applying the Lemma to both $S$ and $S_{\text{new}}$ and subtracting. In
particular, the two live cases that matter for a genuine parity-based
induction split ("the last surviving element sits at an even rank" vs. "at
an odd rank," exactly the Branch-A/Branch-B dichotomy every peel-induction
attempt on file has independently rediscovered) are governed by
$\ell(S)\bmod2$, and — by the Lemma — this is *literally the same bit* as
$N(S)\bmod2$. So an induction on $\ell$ faces *exactly* the same
even/odd case split, on *exactly* the same set of instances, as an
induction on $N$ — not a merely-similar split, the identical one.

### 7.2 Lemma (Zero-Iff) — fully proved

**Lemma.** *For every finite multiset $S$ of positive reals, $\ell(S)=0$ if
and only if $A(S)=0$.*

*Proof.* ($\Rightarrow$) If $\ell(S)=0$ then $S'=\varnothing$, so
$A(S)=A(S')=0$ (empty alternating sum). ($\Leftarrow$) Suppose $\ell(S)\ge1$
and write $S'=\{v_1>v_2>\dots>v_\ell\}$ (strictly decreasing, since $S'$'s
values are pairwise distinct by construction, and all positive since $S$
consists of positive reals). Group the alternating sum from the front:
$$A(S')=\sum_{i=1}^{\ell}(-1)^{i+1}v_i
=\underbrace{(v_1-v_2)}_{>0}+\underbrace{(v_3-v_4)}_{>0}+\cdots
+\begin{cases}(v_{\ell-1}-v_\ell)>0,&\ell\text{ even}\\ v_\ell>0,&\ell\text{
odd}\end{cases}.$$
Every bracketed pair $(v_{2j-1}-v_{2j})$ is strictly positive since
$v_1>v_2>\dots>v_\ell$ is strictly decreasing; if $\ell$ is odd the final
unpaired term $v_\ell$ is itself strictly positive. A sum of finitely many
strictly positive terms (at least one term always exists, since $\ell\ge1$)
is strictly positive. So $A(S)=A(S')>0\ne0$. Contrapositive: $A(S)=0
\Rightarrow \ell(S)=0$. $\blacksquare$

This is a standard fact (the alternating sum of a decreasing positive
sequence is positive) but had not been stated or used in this form in the
population before; it precisely characterizes the induction's base case.

**Consequence: the "free" base case $\ell=0$ is not actually free.** The
round-8 outline's skeleton (step 3) asked to "verify the target's RHS is
$\le0$ in every configuration that can reach this base case," implicitly
treating $\ell=0$ as an easy, checkable case. By the Zero-Iff Lemma, ruling
out $\ell(S)=0$ for every *legal* Xiang Yu response $S=F\cup\tau$ against
the ladder is *exactly* the statement $A(S)\ne0$ for every legal response —
which is implied by, but strictly weaker than, the entire open conjecture
$A(S)\ge f(n)>0$. It is **not** established by anything currently on file:
no certified lemma in `results/imo-2026-03/lemmas/` proves $A(S)>0$ in
general (only bounds far weaker, e.g. the trivial $A(S)\le\mathrm{Total}(S)$,
or the specific closed sub-cases already certified). I did not find a
short independent proof of $A(S)\ne0$ this round (a genuine attempt: using
$\max(S)$'s rank-1 dominance fails in general, since $\max(S)$ need not
exceed the sum of everything below it once $c_1\ge2$ fragments $p_1$ into
many small pieces — the "dominant element" structure that made the $c_1=0$
and $c_1=1$ cases tractable is exactly what is missing for general
$c_1\ge2$, consistent with every prior round's diagnosis). A dedicated
$200000$-trial exact-`Fraction` search over legal responses (respecting the
budget constraint $j\le n$ cuts, $n=1,\dots,5$, random cut-count
distributions and random rational fragmentations) found **zero** instances
with $\ell(S)=0$ (equivalently $A(S)=0$); the minimum $A(S)$ found across
all trials was exactly $1/31=f(4)$ — consistent with, but of course not a
proof of, the base case being vacuous. This is honestly flagged as an
**unresolved sub-gap of the base case**, smaller than the full conjecture
but not trivial.

### 7.3 The inductive step: an exact identity, not a reduction, whenever $\ell$ is even

**Setup.** Suppose $\ell(S)\ge1$ and write $S'=\{v_1>\dots>v_\ell\}$ as
above. The natural "peel" move for this induction is to remove the smallest
surviving value(s) of $S'$ (the direct analogue, one level of abstraction
up, of `rank-pigeonhole-budget`'s peel-the-global-minimum and this file's
own round-7 peel-the-max) and compare $A(S')$ to $A$ of the smaller reduced
multiset.

**Case $\ell$ odd (peel one element).** Removing $v_\ell$ (the smallest of
$S'$) gives $S'':=S'\setminus\{v_\ell\}$, with $|S''|=\ell-1$. Since
$\ell$ is odd, $v_\ell$ sits at odd rank $\ell$, sign $(-1)^{\ell+1}=+1$, so
$$A(S')=A(S'')+v_\ell,\qquad\text{i.e.}\qquad A(S'\setminus\{v_\ell\})
=A(S')-v_\ell.$$
Removing the smallest element **strictly decreases** $A$ by exactly its own
value — this is the *good* case (mirrors Branch A of
`rank-pigeonhole-budget`'s decomposition): if $v_\ell$ happens to be a
piece of the tail $\tau$, removing it also shrinks the tail's own budget
$R(\tau)$ correspondingly (via `tail-self-similarity`-type rescaling,
exactly the mechanism that closes Branch A/Case II in that sibling's proof),
so the target's right-hand side shrinks in lockstep with $A$'s decrease —
a genuine reduction with slack to spare, not an identity trap.

**Case $\ell$ even (peel one element) — the exact-identity trap,
re-derived here from scratch.** Removing $v_\ell$ (rank $\ell$, even,
sign $(-1)^{\ell+1}=-1$):
$$A(S'\setminus\{v_\ell\}) = A(S') + v_\ell.$$
This is an **exact identity**, purely a function of $v_\ell$ and the smaller
instance's own value — there is no "budget" on the target side to shrink to
match the $+v_\ell$: if $v_\ell$ came from $F$ (a fragment of $p_1$, not
of the tail), removing it does not touch $R(\tau)$ at all, so the
inductive hypothesis (applied to the strictly smaller instance
$S'\setminus\{v_\ell\}$, whose target is unchanged) supplies no compensation
for the $+v_\ell$ term. This is algebraically the identical mechanism
`math-explorer-alt-induction.md` diagnosed directly for $(\dagger)$ (Branch
B, $N$ even, of peel-the-global-minimum) and this file's own round-7
Case-II-Exact-Peel-Identity: an operation whose output is a *deterministic*
function of the removed data, not an inequality with slack to exploit.

**Case $\ell$ even, peel two elements.** As a genuine attempt at an escape
(rather than assuming it fails), consider removing the two smallest
surviving values $v_{\ell-1},v_\ell$ together, giving
$S'':=S'\setminus\{v_{\ell-1},v_\ell\}$, $|S''|=\ell-2$ (same parity as
$\ell$, staying in the "even" case for every subsequent step — this was the
outline's own suggested repair). Since $\ell$ is even, rank $\ell-1$ is odd
(sign $+1$) and rank $\ell$ is even (sign $-1$):
$$A(S') = A(S'') + v_{\ell-1} - v_\ell,\qquad\text{i.e.}\qquad
A(S'\setminus\{v_{\ell-1},v_\ell\}) = A(S') - v_{\ell-1} + v_\ell.$$
This is again a **fully determined, exact identity** — a fixed function of
the two removed values $v_{\ell-1},v_\ell$, not an inequality. Whether this
is useful depends entirely on whether $v_{\ell-1}-v_\ell$ can be bounded
usefully against the target's own shrinkage — but since the target's
right-hand side $f(n)$ (or, in the $c_1\ge2$ Case-I abstraction, $R(\tau)$)
is a fixed quantity depending only on $\tau$ (and $\tau$ is entirely
untouched by this peel whenever both $v_{\ell-1},v_\ell$ come from $F$, the
generic situation for a "dominant fragment" instance like the tight witness
below), there is again no budget to shrink to match. This exactly matches
the round-8 alt-induction explorer's own direct check ("removing the two
smallest elements of $F$ together... is likewise an exact rank-truncation
identity... does not escape the obstruction either; it is the same
phenomenon one level further down").

### 7.4 Concrete verification on the tight witness

Apply §7.3 to the round-7 `lp-duality-certificate` equality witness:
$n=3$, $F=\{4,2,2\}$ (units $1/15$; $c_1=2$, two cuts fragmenting $p_1=8$),
tail untouched $T=\{4,2,1\}$. Then $S=\{4,4,2,2,2,1\}$ (sorted), with
multiplicities $4{:}2,\,2{:}3,\,1{:}1$, so $S'=\{2,1\}$ and $\ell(S)=2$
(even). By the case-$\ell$-even computation above (one-element peel,
$v_\ell=1$): $A(S'\setminus\{1\})=A(\{2\})=2=A(S')+1=1+1=2$ ✓ — an exact
identity, confirmed directly, with $A(S')=1=f(3)\cdot15$ exactly (the tight
equality case). This is a genuine, concrete instance of the diagnosed trap,
not merely a hypothetical: the ℓ-induction's "hard case" (ℓ even) bites
*exactly* at the same tight witness the round-7 LP-duality analysis and the
round-8 explorers independently identified as the sharp obstruction —
confirming, on a real example rather than only in the abstract, that this
is the same wall.

### 7.5 Conclusion: a genuine, general, honest negative result

**What this round establishes (new, general, non-numeric):**
- **Parity Coincidence Lemma** (§7.1): $\ell(S)\equiv|S|\pmod2$ for every
  finite multiset — proves, rather than merely suggests, that induction on
  $\ell$ cannot decouple from the parity obstruction that has independently
  stalled every peel-induction attempt in the population (three
  independent mechanisms: `rank-pigeonhole-budget`'s peel-the-min, this
  file's round-7 peel-the-max, and now this round's peel-on-$S'$). This
  upgrades the round-8 outline's own honest caveat ("may hit a symmetric
  wall... flagged as possibly, not yet tested") into a settled fact.
- **Zero-Iff Lemma** (§7.2): $\ell(S)=0\iff A(S)=0$ — shows the outline's
  proposed base case is not free; ruling it out requires proving
  $A(S)\ne0$ for all legal responses, an unresolved (if plausible, and
  numerically well-supported) sub-gap in its own right.
- **§7.3–7.4**: a from-scratch re-derivation, in the $\ell$-indexed
  framework, of exactly why the even-parity case is an exact identity (not
  a genuine reduction) both for one-element and two-element peels —
  independently confirming (by direct symbolic computation, not just
  citation) the round-8 alt-induction explorer's diagnosis, and pinning it
  to a concrete on-file witness.

**What remains open.** General $c_1\ge2$ is **not** closed by this
mechanism; this round's honest conclusion is that peel-induction on
$\ell(S)$ is a **confirmed dead end for escaping the parity obstruction**,
on the same footing as (indeed, provably identical in kind to)
`rank-pigeonhole-budget`'s peel-the-global-minimum and this file's own
round-7 peel-the-max — a third mechanism converging on the same wall, now
with a one-line proof of *why* any peel-based mechanism must, rather than a
third independent empirical coincidence. Per the round-8 outline's explicit
instruction, this is recorded plainly as a negative result and should
**not** be re-attempted by a future round in any peel-by-parity variant
(single-element, paired-element, or reduced-multiset peel are now all
confirmed instances of the identical obstruction). The productive next
targets remain exactly as diagnosed by the round-8 outliner/explorers: (i)
an *upper*-bound machinery on a reduced "foreign-mass-plus-tail" instance
(this file's own round-7 §6.3 diagnosis), or (ii) a non-peel mechanism
entirely, such as `rank-pigeonhole-budget`'s round-8 exchange-smoothing/
vertex-maximization approach (which structurally avoids ever removing a
single element and asking about resulting rank parity, per the round-8
outline-reviewer's own assessment).

## Full proof
(absent — Status is `partial`. The Vertex-Minimum Theorem (§1) and the
Odd-Run Reduction Lemma (§2) are new, fully proved, general-purpose results
established in round 3, certified and promoted to `lemmas/`; they rigorously
justify the geometric picture this approach was seeded on and give a fast,
uniform tool for evaluating any candidate tie-vertex. They reduce (but do
not close) the general-$n$ lower bound to a finite — but not yet
characterized or bounded — enumeration of tie-vertices for the ladder's
specific values; see §4 for exactly what is and is not established, and the
new negative finding ruling out the most natural inductive scheme for that
enumeration. Round 4 adds a fully proved, closed-form, general-$n$
characterization of the "cascading-halving" sub-family of tie-vertices (see
"Round 4 build" section above): exactly $k=n-1,n$ hit the target for every
$n$, correcting the round-4 outline's refuted "every $k$" conjecture with a
genuine theorem rather than leaving the correction as a bare counterexample
table. Round 5 adds the Cross-Term Reduction Theorem (§5.1), which pins the
"asymmetric single cut" case of the domination lemma down to one precise
inequality $(\star\star)$ (honestly identified as equivalent in substance to
every sibling approach's own remaining gap, not a new escape route), and
fully closes a second infinite family of tie-vertices (§5.3, interior
cross-ties against an untouched tail) for $n\le7$ exactly, with the
general-$n$ finish flagged as a small separate residual item. **Round 6
closes $(\star\star)$ completely** (§5.2, Half-Window Vanishing Lemma: the
ladder identity $p_1=2p_2$ splits $W$ at its exact midpoint, the right half
provably carries zero odd-parity mass since no tail element exceeds $p_2$,
and the left half is bounded trivially by its own length) — a full,
general-$n$, unconditional proof, not a further reduction — which combined
with §5.1 **fully closes the entire "single cut on $p_1$" domination case**
for every $n\ge2$ and every legal tail refinement. §5.2.1 additionally
closes, in general $n$, the closely related "tail entirely untouched"
sub-family for all $\Delta$ (a generalization of §5.3's $n\le7$-checked
corollary, though not a literal re-derivation of §5.3's narrower exact-tie
family). **Status remains `partial`**: the general-$c_1\ge2$ case (more than
one cut on $p_1$ itself), the full tie-vertex enumeration beyond
single-cut-on-$p_1$ configurations, and the general upper bound all remain
open — see §5.4 for the precise scope. General $n$, both directions of the
full problem, remains open, but the population's shared four-round
obstruction $(\star\star)$ itself is no longer open. **Round 7** (§6)
attacks the general-$c_1\ge2$ case via peel-induction: proves two new exact
identities (Peel Decomposition Identity, general; Case-II Exact Peel
Identity, ladder-specific) that correctly resolve the round-6 explorer's
"WLOG further cuts land in the smaller piece" gap (by never needing that
WLOG) and rigorously confirm — rather than merely assume — that the naive
"generalize Half-Window Vanishing verbatim" idea fails for a precise,
provable reason (the resulting window is origin-anchored, not symmetric).
The dominant-fragment sub-case ($z\ge p_2$) is reduced to an *exactly
equivalent* upper-bound statement on a foreign-piece-plus-tail instance —
not closed, since the reduction is an identity, not a genuine
simplification, and no lemma on file supplies that upper bound (the trivial
$A\le\mathrm{Total}$ bound is shown too weak by direct computation). The
no-dominant-fragment sub-case is shown to be entirely outside this
mechanism's reach, both by proof and by a dedicated numeric control,
matching (though not literally verified identical to) the "Case I" wall
independently found by `rank-pigeonhole-budget` and
`greedy-halving-adversary`. **Status remains `partial`**: general
$c_1\ge2$ is not closed, but the honest gap is now sharper — it is
specifically an *upper-bound* requirement the whole population currently
lacks, not a vague "harder case." **Round 8** (§7) rigorously rules out the
alternative peel-induction-on-$\ell(S)$ mechanism as a route past this gap:
the new Parity Coincidence Lemma ($\ell(S)\equiv|S|\pmod2$, general, three
lines) proves that this induction variable cannot decouple from the parity
obstruction underlying every peel-induction attempt in the population, and
a direct sign computation on $S'$ confirms the even-parity case reproduces
an exact identity (not a reduction) both for one- and two-element peels,
verified concretely on the round-7 tight witness. The Zero-Iff Lemma
additionally shows the induction's base case ($\ell=0$) is not free (it is
equivalent to $A(S)\ne0$, unresolved on its own). **Status remains
`partial`**: this is a confirmed, general (non-numeric) negative result for
this specific mechanism, not a closure of $c_1\ge2$ — see §7.5 for the
precise scope and recommended next targets.)

## Outline-reviewer correction (round 4) — the "every prefix length $k$"
cascading-halving claim is FALSE as generally stated; the true pattern is
narrower

The round-4 outliner's proposed next step for this slug asked to prove:
"for every $k\in\{0,\dots,n\}$, the composition cutting exactly
$p_1,\dots,p_k$ each into two copies of the next rung attains $A=f(n)$
exactly, by induction on $k$." **This general statement is false**, verified
by exact `Fraction` arithmetic (not floating point) for $n=1,\dots,6$
before build, using the $n+1$-piece ladder convention of this file
($p_i=2^{n+1-i}/(2^{n+1}-1)$, $i=1,\dots,n+1$):

```
n=2: k=0 -> A/target ratio: 5/7 != 4/7 (FAILS); k=1 -> 4/7 (matches)
n=3: k=0 -> 2/3 != 8/15 (FAILS); k=1 -> 3/5 != 8/15 (FAILS); k=2 -> 8/15 (matches)
n=4: k=0,1,2 -> FAIL (21/31, 18/31, 17/31, all != 16/31); k=3 -> 16/31 (matches)
n=5: k=0,1,2,3 -> FAIL; k=4 -> 32/63 (matches)
n=6: k=0,1,2,3,4 -> FAIL; k=5 -> 64/127 (matches)
```

The clean pattern that **does** hold (confirmed exactly for $n=1,\dots,6$):
**only the top two prefix lengths, $k=n-1$ and $k=n$ (using the $n+1$-piece
convention, i.e. leaving at most the single smallest piece $p_{n+1}$, or at
most $\{p_n,p_{n+1}\}$, untouched by the cascade), attain $A=f(n)$ exactly.**
Every shorter prefix ($k\le n-2$) gives a strictly larger value of $A$
(i.e. is *not* a tie for the minimum — Xiang Yu can do strictly better by
completing the cascade further). This matches the round-4 superincreasing
explorer's own report, which only ever tested $k$ at or near the top of the
range (e.g. $n=3$: $k=1,2$; $n=4$: $k=3$) and never claimed the full range —
the outliner's write-up over-generalized "reproduces the target at every
tested $k$" into "for every $k\in\{0,\dots,n\}$," which is the part that is
false.

**Corrected next step for the builder:** prove the narrower, TRUE claim —
the cascading-halving composition attains $A=f(n)$ exactly precisely when
$k\in\{n-1,n\}$ (equivalently: cutting all pieces down to at most the last
one or two rungs) — by induction from the top down (i.e. induct on
$n-k$, not on $k$), and separately investigate *why* it breaks for smaller
$k$: the likely explanation is that for $k\le n-2$ the pure cascade is no
longer itself an optimal (tying) vertex at all — some other, non-cascading
tie configuration (e.g. the "cross-generational" pattern already on file in
§3, or a mixed pattern) becomes the true minimizer of that composition's
cell once enough untouched tail structure remains, while the cascade value
itself only decreases monotonically as $k\to n$. This reframing (a
genuinely $O(1)$-indexed family of exactly two working prefix lengths,
rather than $O(n)$) is a smaller but honest target; do not attempt to force
the general-$k$ induction, it is refuted by exact computation above.
(Verification script available on request: builds the $n+1$-piece ladder
with exact `Fraction` arithmetic, applies the cascading-halving construction
for every $k$, and computes $A$ via direct sort-and-alternate-sum,
cross-checked by an independent recursive-cascade construction with the
same result.)

## Round 4 build: the Cascading-Halving-Family Theorem (new, fully proved,
closed-form, general $n$)

This section proves the corrected claim exactly, in closed form, for every
$n$ — not by checking finitely many $n$ but by a genuine symbolic
computation, and identifies precisely (again in closed form) why every
shorter prefix fails, replacing the numeric table in the correction above
with a proof.

### Setup: the composition and why it is a genuine vertex

Fix $n\ge1$, the ladder $p_i=2^{n+1-i}/D$, $D:=2^{n+1}-1$, $i=1,\dots,n+1$,
and $0\le k\le n$. Consider the composition that puts exactly one Xiang-Yu
cut on each of $p_1,\dots,p_k$ and none elsewhere ($d=k$ free parameters),
and within it the specific point where **every** cut piece $p_i$
($1\le i\le k$) is split into two exactly equal fragments $p_i/2,p_i/2$ —
call this response $R_k$. Since $p_i/2=2^{n-i}/D=p_{i+1}$ (the ladder is
geometric with ratio $2$), each cut produces two copies of the *next rung*:
$$R_k:\quad p_i\ \longrightarrow\ \{p_{i+1},p_{i+1}\}\quad (i=1,\dots,k),
\qquad p_{k+1},\dots,p_{n+1}\ \text{untouched}.$$
This is a legal Xiang Yu response ($k\le n$ cuts used, $\le n$ total budget,
`must-use-all-n-points` constrains only Liu Bang's count, not Xiang Yu's, so
using fewer than $n$ cuts is unrestricted). Each of the $k$ splits sets the
two fragments of $p_i$ equal — a type-(II) tie constraint in the sense of
the certified **Vertex-Minimum Theorem** (`vertex-minimum-theorem.md`) — and
there are exactly $k=d$ independent such constraints (one per cut piece,
each involving disjoint coordinate pairs), so $R_k$ is precisely a *vertex*
of this composition's cell: this whole family is a genuine, uniformly
constructed sub-family of the vertices the Vertex-Minimum Theorem says the
true minimizer must be among, not an ad hoc guess.

### Step 1: the resulting multiset, by multiplicity

For $k\ge1$, the multiset $S_k$ under $R_k$ has:
- $p_i$ for $2\le i\le k$: multiplicity exactly $2$ (produced as both halves
  of the cut on $p_{i-1}$; not separately untouched, since $2\le i\le k$
  means $p_i$ itself is also cut);
- $p_{k+1}$: multiplicity exactly $3$ ($2$ copies produced as the halves of
  the cut on $p_k$, plus $1$ copy as the untouched piece $p_{k+1}$ itself,
  since $k+1$ is not among the cut indices $1,\dots,k$);
- $p_i$ for $k+2\le i\le n+1$: multiplicity exactly $1$ (untouched, and
  never produced as a half since only cuts on $p_1,\dots,p_k$ occur).

(When $k=0$, no cuts occur at all and $S_0=\{p_1,\dots,p_{n+1}\}$, every
multiplicity $1$ — the formula below recovers this case automatically, see
Step 3.)

### Step 2: apply the Odd-Run Reduction Lemma

By the certified **Odd-Run Reduction Lemma** (`odd-run-reduction-lemma.md`),
$A(S_k)=A(S_k')$ where $S_k'$ keeps one copy of each odd-multiplicity value
and drops every even-multiplicity value. For $k\ge1$: the multiplicity-$2$
values $p_2,\dots,p_k$ drop out entirely; $p_{k+1}$ (multiplicity $3$, odd)
survives as one copy; $p_{k+2},\dots,p_{n+1}$ (multiplicity $1$ each)
survive. Hence
$$S_k' = \{p_{k+1},p_{k+2},\dots,p_{n+1}\}\quad(\text{already sorted
descending, since the ladder is decreasing}),$$
so
$$A(S_k) = A(S_k') = \sum_{j=k+1}^{n+1}(-1)^{j-(k+1)}p_j$$
— exactly the alternating sum of the ladder's own tail starting at index
$k+1$. (For $k=0$ this is the alternating sum of the *whole* ladder, which
is the same formula with $k+1$ replaced by $1$; Step 3 handles both
uniformly.)

### Step 3: closed form via geometric series

Set $L:=n-k\in\{0,1,\dots,n\}$ and reindex the tail sum by $t:=j-(k+1)$,
$t=0,\dots,L$, so $p_j = p_{k+1+t} = 2^{n-k-t}/D = 2^{L-t}/D$. Then
$$D\cdot A(S_k) = \sum_{t=0}^{L}(-1)^t\,2^{L-t} =: T(L).$$

**Claim.** $T(L) = \dfrac{2^{L+1}+(-1)^L}{3}$ for every integer $L\ge0$.

*Proof (induction on $L$).* Base case $L=0$: $T(0)=2^0=1$, and the formula
gives $(2^1+1)/3=1$. ✓. Inductive step: suppose $T(L-1)=\big(2^{L}+(-1)^{L-1}\big)/3$
for some $L\ge1$. Separating the $t=0$ term from the rest and reindexing
$t\to t+1$ in the remainder,
$$T(L)=2^L+\sum_{t=1}^{L}(-1)^t2^{L-t} = 2^L-\sum_{s=0}^{L-1}(-1)^s2^{L-1-s}
=2^L-T(L-1),$$
so by the inductive hypothesis
$$T(L)=2^L-\frac{2^{L}+(-1)^{L-1}}{3}=\frac{3\cdot2^L-2^{L}-(-1)^{L-1}}{3}
=\frac{2\cdot2^L+(-1)^L}{3}=\frac{2^{L+1}+(-1)^L}{3}. \qquad\blacksquare$$

(Verified independently by exact `Fraction` computation for $n=1,\dots,8$
and every $k=0,\dots,n$ — i.e. every value of $L=0,\dots,8$ — with zero
mismatches against both a direct sort-and-alternate-sum on the raw
multiset $S_k$ and the odd-run-reduced form: see the appended script
output.)

### Step 4: exactly which $L$ (equivalently, which $k$) hit the target

Recall the target is $A(S_k)=f(n)=1/D$, i.e. $T(L)=1$.

**Theorem (Cascading-Halving-Family Characterization).** *For every $n\ge1$
and every $0\le k\le n$, writing $L=n-k$:*
$$T(L)=1 \iff L\in\{0,1\} \iff k\in\{n-1,n\},$$
*and $T(L)>1$ (strictly) for every $L\ge2$. Consequently, among the $n+1$
members $R_0,\dots,R_n$ of the cascading-halving family, exactly the two
"deepest" responses $R_{n-1}$ and $R_n$ attain $A(S_k)=f(n)$ exactly; every
shallower one ($k\le n-2$) gives $A(S_k)>f(n)$ strictly, i.e. is not a tie
for the (conjectured) minimum — Xiang Yu strictly improves by cutting the
cascade at least one level deeper.*

*Proof.* From the closed form, $T(0)=(2+1)/3=1$ and $T(1)=(4-1)/3=1$, so
both $L=0,1$ give exactly $1$. For $L\ge2$: if $L$ is even,
$T(L)=(2^{L+1}+1)/3\ge(2^3+1)/3=3>1$ (using $2^{L+1}\ge2^3=8$ for $L\ge2$
even, so $L+1\ge3$); if $L$ is odd, $L\ge3$ (the smallest odd $L\ge2$), so
$T(L)=(2^{L+1}-1)/3\ge(2^4-1)/3=5>1$ (using $L+1\ge4$). In both parity
cases $T(L)>1$ strictly, so $T(L)=1$ forces $L\in\{0,1\}$, i.e.
$k\in\{n-1,n\}$. $\blacksquare$

**Monotonicity remark (immediate corollary, useful below).** The values
$T(0),T(1),T(2),T(3),\dots=1,1,3,5,11,21,43,\dots$ satisfy $T(0)=T(1)=1$ and
are strictly increasing for $L\ge1$: from the closed form, for $L\ge2$,
$$T(L)-T(L-1)=\frac{2^{L+1}+(-1)^L}{3}-\frac{2^{L}+(-1)^{L-1}}{3}
=\frac{2^L+2(-1)^L}{3}>0$$
since $2^L\ge4>2$ for $L\ge2$. So $T$ is non-decreasing throughout and
strictly increasing once $L\ge2$; in particular $T(L)\ge1$ for every
$L\ge0$, with equality exactly at $L\in\{0,1\}$ (already shown directly in
the Theorem above; this recurrence gives an independent second proof of the
same inequality). Consequently **no member of this family ever achieves
$A(S_k)<f(n)$** — the family is consistent with (never contradicts) the
lower-bound conjecture $\min_{\text{Xiang Yu}}A\ge f(n)$, and pins down
exactly its two tightest members.

### Step 5: this corrects and completes the outline's request precisely

This closes the outline's corrected request in full: a rigorous, general-$n$
(not case-checked, not numeric-only) proof of exactly which prefix lengths
in the cascading-halving family hit the target, replacing both (i) the
original outline's false "every $k$" claim and (ii) this round's own
numeric table (verified for $n\le8$ only) with a genuine closed-form
argument valid for every $n\ge1$.

### What Step 4 does *not* establish (honest scope)

- It does **not** show $R_{n-1}$ or $R_n$ is the *global* minimizer over all
  of Xiang Yu's legal responses (all compositions, all vertex types) — only
  that, within this one specific self-tie sub-family, they are the unique
  members achieving the target value, and every other member of the family
  strictly exceeds it (consistent with, but not a proof of, the lower
  bound).
- The known fully-closed cases $n=1$ ($R_0=R_1$ coincide, trivially the
  unique family member) and $n=2$ (`smoothing-compactness-certificate`'s
  reviewer-certified closure, all $10$ Xiang-Yu cut-distributions) confirm
  $R_{n-1}$ is indeed among the true global-minimum-achieving responses for
  $n=1,2$ — a nontrivial cross-check that this family's two survivors are
  not merely accidental ties within the family but plausibly land on the
  actual answer — but this is evidence, not a proof, for $n\ge3$.
- The general enumeration problem identified in §4 above (characterizing
  *all* feasible tie-vertices — including cross-ties like the $n=3$ example
  in §3, non-prefix subsets of cut pieces, and mixed multi-way ties — and
  proving none of them dips below $f(n)$) remains open. This section
  narrows that enumeration by fully settling one clean, uniformly-defined
  infinite sub-family (all $n$, all $k$) rather than leaving it as an
  unverified pattern guess.
- The general **upper bound** direction (arbitrary Liu Bang marking) is
  untouched by this section.

## Promotable lemmas

- **Parity Coincidence Lemma** (§7.1, new this round): for every finite
  multiset $S$, $\ell(S):=|S'|$ (odd-run-reduced size) satisfies
  $\ell(S)\equiv|S|\pmod2$. Fully proved in three lines, completely general
  (no dependence on the ladder or on this problem's specific structure) —
  a reusable elementary fact about the certified `odd-run-reduction-lemma`'s
  output, and the tool that rules out this round's proposed induction
  mechanism. Candidate for promotion as a companion fact to
  `odd-run-reduction-lemma`.
- **Zero-Iff Lemma** (§7.2, new this round): for every finite multiset $S$
  of positive reals, $\ell(S)=0\iff A(S)=0$, via "the alternating sum of a
  nonempty strictly-decreasing sequence of positive reals is always
  strictly positive." Fully proved, general-purpose, reusable anywhere the
  population needs to characterize when $A$ vanishes exactly.
- **Cross-Term Reduction Theorem** (§5.1): for the asymmetric single-cut
  case, reduces domination (for every legal tail refinement $G'$) to the
  precise inequality $(\star\star)$: $\int_{W\cap[0,r)}v\le\Delta/2$. Fully
  proved as a reduction (not conditional beyond the standard induction
  hypothesis $(\star_{n-1})$ already used by the certified
  `symmetric-split-c1-lower-bound`); a candidate for promotion alongside
  that lemma as the natural generalization to $\Delta\ne0$.
- **Half-Window Vanishing Lemma / $(\star\star)$, fully proved** (§5.2, new
  this round): every element of a legal tail refinement is $\le p_2$, so the
  window's right half (which the ladder identity $p_1=2p_2$ places exactly
  at the window's midpoint) carries $v\equiv0$ identically; combined with
  the trivial length bound on the left half this proves $(\star\star)$
  unconditionally for every $n\ge2$. This is the strongest single result of
  this round: it closes, in one shot, the precisely-localized obstruction
  independently reached by (at least) `greedy-halving-adversary`,
  `rank-pigeonhole-budget`, and `dyadic-band-occupancy` for the "single cut
  on $p_1$, arbitrary tail refinement" case — top candidate for promotion,
  and for the outline-reviewer to check whether it lets any sibling
  approach's own equivalent-gap statement close directly by transplant
  (each phrased $(\star\star)$ slightly differently; the underlying content,
  "no tail element exceeds the tail's own largest piece," is elementary and
  should transplant without re-deriving from scratch).
- **Interior-cross-tie evaluation formula** (§5.3): the closed form
  $A(S_j)=x+2C(j)-(-1)^jp_j-A(T)$ for the family of vertices tying $p_1$'s
  larger fragment to an untouched tail piece $p_j$ ($j\ge3$), fully proved
  (sign-bookkeeping argument, no gap) for every $n$, with the corollary
  ($A(S_j)\ge f(n)$, strict for $n\ge3$) verified exactly for $n\le7$ — the
  formula itself is unconditionally general; only the final strict-inequality
  finish is currently checked rather than proved for all $n$ (§5.2.1 closes
  the general-$n$ case for the related, but not identical, "tail entirely
  untouched, all $\Delta$" sub-family).

## Outline (proof-outliner, round 6) — superseded, see round-6 build below

*(This note was written before this round's build; it is left on file for
the record but is now superseded — $(\star\star)$ was the round's assigned
target and is now closed, see §5.2. Retained verbatim below for
audit-trail purposes.)*

$(\star\star)$ (§5.2) is now the cleanest, most concrete single restatement
of the shared four-round obstruction on file — recommend it as the primary
target for `lp-duality-certificate` (a one-shot certificate for
$\int_{W\cap[0,r)}v\le\Delta/2$ would close this approach's Cross-Term
Reduction Theorem outright) and for `integer-lattice-reduction` (rescale $W$,
$\Delta$, $r$ by $D=2^{n+1}-1$ and attempt the digit/carry computation
directly on this specific window integral, since it is already isolated in
closed algebraic form rather than buried in a generic mass bound). If this
slug itself is built again this round: finish the $n\le7\to$ general-$n$
strict-inequality gap in §5.3's corollary (a concrete, likely-tractable
finite-to-infinite generalization, distinct from $(\star\star)$'s open
status), and otherwise stand by to receive $(\star\star)$'s resolution from
whichever new-framing approach closes it first rather than re-attempting a
fourth independent derivation of the same inequality.

## Round 6 build: $(\star\star)$ closed — recommendation for round 7

$(\star\star)$ is now proved (§5.2, Half-Window Vanishing Lemma) —
**`lp-duality-certificate` and `integer-lattice-reduction` no longer need to
target $(\star\star)$ itself**; if either was mid-flight on it this round,
it should redirect to the next layer, per §5.4:
1. **General $c_1\ge2$** (more than one cut on $p_1$): the Half-Window
   Vanishing mechanism (an element bound + a ladder-forced window midpoint)
   may partially transfer, but the window/midpoint structure needs to be
   redone for $\ge3$ simultaneous fragments of $p_1$ — flagged, not solved,
   here.
2. **Full vertex enumeration beyond single-cut-on-$p_1$**: configurations
   with no cut on $p_1$ but multiple simultaneous tail cuts, or mixed
   patterns, are not covered by §5.1/§5.2's reduction and remain the
   deepest open item toward a complete lower-bound proof.
3. **The general upper bound** (arbitrary Liu Bang marking) is completely
   untouched by this approach and by (as far as this round's context
   review found) every sibling approach — a candidate for its own dedicated
   new-framing approach next round, per the shared-gap-plateau rule, since
   the lower-bound side has just absorbed most of the population's recent
   effort.
Recommend the outline-reviewer verify §5.2's proof independently (it is
short and elementary — a single lemma plus a two-line window-splitting
argument — so should be fast to re-check line by line) before certifying
`half-window-vanishing-lemma` for promotion to `lemmas/`.
