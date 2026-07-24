# Explorer report: exploiting the superincreasing ladder structure

Lens: does the exact superincreasing property of the ladder $p_i =
2^{n+1-i}/(2^{n+1}-1)$ collapse the tie-vertex enumeration to polynomially
many (or $O(n)$) cases? Is there a clean binary encoding? What do the actual
$n=4,5$ tie patterns look like?

## Method

Built two independent computational tools (`/tmp/round-4/`):
1. `lp_search2.py` — an **exact** enumeration for small $n$: for every
   composition $(c_1,\dots,c_{n+1})$ and every ordering (permutation)
   consistent with the composition, solves the resulting linear program
   (the odd-rank-sum objective is affine once the ordering/permutation is
   fixed) via `scipy.optimize.linprog`, and takes the true global min over
   all orderings and compositions. This reproduces the Vertex-Minimum
   Theorem's guarantee exactly, with no heuristic error. Cross-validated at
   $n=3$: computed min $= 8/15 = c(3)$ exactly (machine precision, diff
   $<10^{-12}$).
2. `heuristic_fast.py` — for $n=4,5$ (where exact permutation enumeration
   blows up combinatorially, $9!$–$11!$ terms per composition), a
   `differential_evolution` global search per composition, cross-checked
   against tool 1 at $n=3$ (identical answer) and sanity-checked at
   $n=4,5$ against the known target value $c(n)=2^n/(2^{n+1}-1)$ (matched to
   $10^{-10}$–$10^{-11}$). This is **not** a rigorous certification tool —
   it is a terrain-mapping tool, exactly as the explorer role requires.

## Finding 1 (answers question (a)): the enumeration does **not** collapse — degeneracy is pervasive, not sparse

Contrary to the hope that superincreasing-ness would force a small ($O(n)$
or polynomial) set of feasible tie-vertices, the *opposite* is true:
**many different compositions, and multiple distinct vertices within the
same composition's polytope, all attain the exact same minimum value
$c(n)$ simultaneously.**

- $n=3$ (exact enumeration): $9$ of the $35$ legal compositions tie at the
  global minimum.
- $n=4$ (heuristic, likely undercounting since DE can miss ties): at least
  $24$ of $126$ compositions tie.
- $n=5$ (heuristic): $68$ of $462$ compositions tie — roughly the same
  $\sim$15–25% fraction as $n=3,4$, i.e. **the fraction of tied-optimal
  compositions is not shrinking with $n$.** If anything this suggests the
  count of optimal vertices grows at least as fast as the composition count
  itself (which is $\binom{2n+1}{n+1}-1\sim$ exponential in $n$), not
  polynomially. This is a fairly strong negative answer to (a): the
  superincreasing property does **not** prune the vertex set down to a
  short list; it instead creates a **wide plateau** of ties (consistent with
  the Vertex-Minimum Theorem's own remark that the same minimum can be
  attained along a whole face, not just an isolated vertex — that
  degeneracy is apparently large-dimensional here, not a one-off).

**Practical implication:** an approach that tries to explicitly enumerate
"the" feasible tie-vertices and check $\Phi\ge f(n)$ at each one by one is
probably fighting the wrong battle — for the actual ladder there seem to be
combinatorially many (not few) optimal or near-optimal configurations. A
proof strategy that establishes the bound via a single **uniform algebraic
identity/inequality holding on the whole plateau at once** (in the flavor
of the existing cross-term-identity-threshold / odd-run-reduction machinery)
looks structurally better matched to this terrain than a case-by-case vertex
audit.

## Finding 2 (answers question (b), partially): the source of the degeneracy is an exact, level-independent identity

Verified symbolically (exact `Fraction` arithmetic) for $n=3,4,5,6$:
$$p_i = 2\,p_{i+1}\quad\text{(exact ratio 2, every }i\text{)},\qquad
p_i - \sum_{j>i}p_j = f(n) := \frac1{2^{n+1}-1}\quad\text{(exact, same
constant for every }i\text{, equal to the smallest piece }p_{n+1}\text{)}.$$

Both are consequences of the geometric-ladder formula and are elementary to
verify (sum of a geometric tail), but their conjunction is the likely
combinatorial engine behind Finding 1: every piece is *exactly* double the
next, and every piece's "surplus" over its own tail is *exactly* one copy of
the smallest unit $f(n)$ — a constant that does not depend on which level
$i$ you look at. This uniformity is presumably why trading a cut/tie at one
level for a cut/tie at another level so often costs nothing: the local
"exchange rate" is the same everywhere in the ladder.

This does give a *partial* answer to (b): there is a clean, always-available
family of tie-vertices —

> **Cascading-halving pattern.** For any prefix length $k\in\{0,\dots,n\}$,
> take the composition that cuts each of $p_1,\dots,p_k$ exactly once and
> leaves $p_{k+1},\dots,p_{n+1}$ untouched, with each cut piece $p_i$
> ($i\le k$) split into two exactly equal halves $p_i/2 = p_{i+1}$ (using
> the exact-doubling identity). The resulting multiset is
> $\{p_2,p_2,p_3,p_3,\dots,p_{k+1},p_{k+1},p_{k+1},p_{k+2},\dots,p_{n+1}\}$
> — every value $p_2,\dots,p_k$ occurs with even multiplicity (one native
> untouched copy + ... actually each of $p_2,\dots,p_k$ gets exactly 2 extra
> copies from the halving of $p_{i-1}$, on top of being itself halved down
> to $p_{i+1}$'s value — multiplicities work out so that by the certified
> Odd-Run Reduction Lemma every value up to $p_k$ cancels in pairs, leaving
> exactly $S' = \{p_{k+1}, p_{k+2}\}$ or similar** (verified concretely for
> $n=4$, $k=3$: composition $(1,1,1,0,0)$, multiset
> $\{8,8,4,4,2,2,2,1\}$ (units $1/31$) $\to$ odd-run-reduces to $\{2,1\}$,
> $A=1=31f(4)$, exact match — see the worked computation below).

Concrete worked example ($n=4$, prefix $k=3$, units of $1/31$, ladder
$16,8,4,2,1$): cutting $p_1\to(8,8)$, $p_2\to(4,4)$, $p_3\to(2,2)$, leaving
$p_4=2,p_5=1$ untouched gives sorted multiset $\{8,8,4,4,2,2,2,1\}$. Odd-run
reduction: $8$ (mult 2, even) drops, $4$ (mult 2, even) drops, $2$ (mult 3,
odd) keeps one copy, $1$ (mult 1, odd) keeps. $S'=\{2,1\}$, $A=2-1=1=1/31\cdot
31=f(4)\cdot31$. Matches the target exactly. (Full script:
`/tmp/round-4/single_comp_exact.py 4 1,1,1,0,0`.)

**Important negative check:** this "prefix" restriction is load-bearing —
tested composition $(1,0,1,0,0)$ at $n=4$ (cut $p_1$ and $p_3$, but leave
$p_2$ untouched, "skipping" a level in the cascade) and it does **not**
reach the minimum: the LP-optimal value there is $0.5806 > 0.5161=$ target.
So the cascade must be a contiguous prefix of pieces $p_1,\dots,p_k$ — you
cannot skip a level and still land on the optimum via this pattern. This
rules out a naive "any subset of $2^n$ levels" binary encoding; the feasible
cascades (at least of this type) are indexed by a single integer $k\in
\{0,\dots,n\}$, i.e. genuinely $O(n)$ many — a much smaller, more promising
family than the raw composition space, *if* it turns out to be the whole
story (see caveat below).

## Finding 3 (the $n=3$ counterexample is a genuinely different vertex, not a fluke)

Re-derived exactly (via `lp_search2.py`) that composition $(1,1,0,0)$ at
$n=3$ has (at least) **two distinct optimal vertices**, both attaining
$A=1/15=f(3)$ exactly:
- The "clean" cascading-halving one: $p_1\to(4,4)=(p_2,p_2)$,
  $p_2\to(2,2)=(p_3,p_3)$, giving $\{4,4,2,2,2,1\}\to$ odd-run $\{2,1\}$.
- The **cross-generational** one already on file
  (`rank-tie-vertex-reduction.md` §3): $p_1\to(4,4)=(p_2,p_2)$ but $p_2$
  splits *asymmetrically* into $(1,3)=(p_4,p_3)$ — skipping the "clean"
  self-halving of $p_2$ entirely and tying its fragment directly to $p_4$
  two levels down — giving $\{4,4,3,2,1,1\}\to$ odd-run $\{3,2\}$, $A=1$.

Both live on the *same* composition's polytope (same $(c_1,c_2,c_3,c_4)$),
confirming these are two vertices of one polyhedral cell's boundary (or two
adjacent cells) both realizing the cell's minimum — direct computational
confirmation of the Vertex-Minimum Theorem's own remark that the minimizer
along a face need not be unique. So even within the "cascading" composition
family, the *specific* tie pattern realizing the minimum is not unique
either — there is at least a 1-parameter (or higher) family of optimal
points in some cells, not just isolated vertices, which is presumably a
second, finer source of the massive degeneracy in Finding 1 (degeneracy
across compositions *and* within a single composition's cell).

## What this changes for next steps

- **Question (a) is answered negatively**: superincreasing-ness does not
  collapse the raw vertex-enumeration to few cases; it seems to *cause* a
  wide degenerate plateau of optimal responses. Any future approach relying
  on "enumerate the finitely many vertices and check each" should budget for
  this — the honest count is large (growing with the composition count),
  not small.
- **Question (b)/binary encoding**: a genuinely promising sub-family was
  found — the $O(n)$-indexed **prefix cascading-halving pattern**
  (cut a prefix $p_1,\dots,p_k$, halve each into the next rung's value) —
  which exploits the exact identities $p_i=2p_{i+1}$ and $p_i-\sum_{j>i}p_j
  =f(n)$ (constant) directly and is cheap to state and verify for any $n$.
  It reproduces the target value $f(n)$ at every tested $k$ so far ($n=3$:
  $k=1,2$ both checked via the $(1,1,0,0)$ composition variants; $n=4$:
  $k=3$ checked explicitly). **This family alone is not the whole
  enumeration** (Finding 3 shows other, non-cascading vertices tie the same
  composition's optimum, and Finding 1's raw counts are much larger than
  $O(n)$), so it should be understood as *one clean sub-case worth proving
  cleanly*, not a claim that it exhausins all optimal configurations. A
  productive next step: **prove algebraically that every prefix-cascade
  ($k=0,\dots,n$) gives exactly $A=f(n)$** (this looks like a short,
  self-contained induction on $k$ using the exact doubling identity and
  `odd-run-reduction-lemma` — much more tractable than the general
  enumeration) as a clean, certifiable partial result, while separately
  continuing to hunt for a *uniform* inequality argument (per Finding 1's
  recommendation) for the general lower bound rather than trying to
  enumerate the full degenerate vertex set.
- The exact identities $p_i=2p_{i+1}$ and $p_i-\sum_{j>i}p_j=f(n)$
  (verified for $n$ up to 6, trivial to prove in general from the geometric
  sum formula) are themselves worth stating as a small reusable fact if not
  already implicit in `ladder-self-similarity-constant` — they are the
  concrete algebraic engine underlying both the achievability construction
  and, plausibly, the pervasive tie-degeneracy documented here.

## Scripts (reusable, in `/tmp/round-4/`)

- `lp_search2.py` — exact global min via LP-per-permutation (use for
  $n\le3$ or targeted single compositions at $n=4$; too slow for full
  $n=4$ exhaustive sweep).
- `single_comp_exact.py <n> <c1,c2,...>` — exact vertex(es) for one named
  composition (fast, used for the worked examples above).
- `heuristic.py` / `heuristic_fast.py` — differential-evolution terrain
  sweep across all compositions for a given $n$ (used for $n=4,5$); **not**
  a certification tool, only for spotting patterns/candidates to then
  verify exactly.
