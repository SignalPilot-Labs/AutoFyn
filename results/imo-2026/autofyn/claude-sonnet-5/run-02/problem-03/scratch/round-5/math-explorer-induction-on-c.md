## imo-2026-03

### Method used
Wrote an exact-`Fraction` implementation of the certified **Vertex-Minimum
Theorem** (`lemmas/vertex-minimum-theorem.md`): for a fixed composition
$(c_1,\dots,c_{n+1})$ of Xiang Yu's cut budget, enumerated *every* candidate
vertex (every $d$-subset of the finite list of "fragment=0" and
"fragment=fragment" tie-hyperplanes, $d=\sum c_i$), solved the linear system
exactly (rational Gaussian elimination, no floats anywhere), kept only
feasible solutions (all fragments $\ge0$), and evaluated $A$ by direct
sort-and-alternate-sum. This is a *complete* search per the certified
theorem — not a numeric sample — so for each $n$ tested this is a rigorous,
computer-verified (not merely suggestive) determination of
$\min_{\text{Xiang Yu}} A(S)$ for every composition, hence for every value of
$c$ (cuts landing in the top piece $p_1$). Code: `/tmp/round-5/probe2_lib.py`
(library), `probe2.py`/`probe4c.py`/`probe5.py` (drivers). Ran $n=3,4$ to
completion; $n=5$ timed out (combinatorial explosion of $d$-subsets) even
after 9+ minutes — not pursued further given the round budget.

### Headline finding (numeric-exhaustive, not conjecture-by-sampling)
For $n=3$ ($D=15$, target $f(3)=1/15$) and $n=4$ ($D=31$, target
$f(4)=1/31$), computed $A_{\min}(c):=\min$ over **all** compositions with
exactly $c$ cuts on $p_1$ and the rest distributed (in every way) over the
tail, of $\min_{\text{that composition}}A(S)$ — i.e. every legal Xiang Yu
response with exactly $c$ real-or-degenerate cuts forced onto $p_1$:

```
n=3 (D=15, target 1/15):
  c=0: A_min = 4/15   (comp (0,0,1,1); NOT the target — strictly worse for Xiang Yu)
  c=1: A_min = 1/15 = target   (comp (1,1,0,0))
  c=2: A_min = 1/15 = target   (comp (2,0,0,0), degenerate: one p1-fragment = 0)
  c=3: A_min = 1/15 = target   (comp (3,0,0,0), degenerate: two p1-fragments = 0)

n=4 (D=31, target 1/31):
  c=0: A_min = 8/31   (NOT the target)
  c=1: A_min = 1/31 = target   (comp (1,1,1,0,0))
  c=2: A_min = 1/31 = target   (comp (2,0,1,0,0), degenerate)
  c=3: A_min = 1/31 = target   (comp (3,0,0,0,0), degenerate)
  c=4: A_min = 1/31 = target   (comp (4,0,0,0,0), degenerate)
```

Pattern of $A_{\min}(0)$: $4/15=2^2 f(3)$, $8/31=2^3f(4)$ — i.e.
$A_{\min}(0)=2^{n-1}f(n)$, strictly $>f(n)$ for every $n$ tested.

### Answer to Q1 (induction on $c$: is there a clean monotone step?)
**No** — the shape is a cliff, not a smooth staircase. $A_{\min}(c)$ is
**constant** $=f(n)$ for every $c=1,\dots,n$ and strictly larger
($2^{n-1}f(n)$) only at $c=0$. There is no useful "$c\to c+1$ weakly
increases $A$" statement to prove, because there is nothing to increase: the
value simply doesn't move once $c\ge1$. Do **not** pursue a smooth
exchange/monotonicity induction on $c$ — the numerics rule it out as the
right shape (it would have to explain a flat line, which such an argument
usually can't produce cleanly). The real content is a **binary** fact
("$c=0$ is bad; $c\ge1$ is exactly as good as the best case can ever be"),
not a graded one.

### Answer to Q2 (self-similar structure in $c$, not just $n$) — the actual finding
Inspecting the **exact winning vertex** at $c=1$ for both $n=3,4$: it is
always "**bisect $p_1$ into two copies of $p_2$ (one real cut, symmetric),
then recurse optimally on the tail with the remaining $n-1$ cuts**" —
concretely the winning composition at $c=1$ is $(1,1,0,\dots,0)$ for $n=3$
and $(1,1,1,0,0)$ for $n=4$: i.e. it is **exactly the certified
$R_{n-1}$ member of `cascading-halving-family-characterization`**, not a new
configuration. Checked directly (`probe5.py`): 1 cut on $p_1$ **alone** (no
tail cuts) gives $A=1/5=3/15\ne1/15$ for $n=3$ — strictly worse than target
— so bisecting $p_1$ is *necessary but not sufficient*; the tail must
*also* be recursively cut optimally. This is precisely the recursive
structure already isolated by the certified `tail-self-similarity` lemma
(the rescaled tail is exactly the $(n-1)$-ladder, $p_1=2p_2$ exactly). So
the real "self-similarity in $c$" is not "$c$ relates to $c-1$ on a rescaled
sub-ladder" (that framing was already refuted by round 3) — it is:
**the *amount* of real budget the optimizer ever spends on $p_1$ itself is
always exactly $1$** (a symmetric bisection), and the recursion is entirely
in $n$ (via `tail-self-similarity`), not in $c$. All $c\ge2$ configurations
that hit the target do so only by **degenerating** the extra forced cuts on
$p_1$ to zero length (verified directly: at $c=2,3$ the winning vertex has
a literal $0$-length fragment of $p_1$), i.e. they collapse back to the
same $c=1$ solution, not a genuinely different 2-real-cut configuration.

### Answer to Q3 (which tie-vertices are actually minimizers)
Extremely narrow, not 15–25% of candidates: across every $c\ge1$ tested at
$n=3,4$, the minimizer is always (up to wasted zero-length padding) the
single member $R_{n-1}$ of the already-certified cascading family (bisect
$p_1,\dots,p_{n-1}$ each into the next rung, leave $p_n,p_{n+1}$ untouched).
No cross-tie vertex (of the kind found in the round-3 $n=3$ example — a
fragment of $p_1$ tied directly to $p_2$, skipping intermediate levels) ever
beats it; that earlier example ($a=p_2,b=p_4$ for a $(1,1,0,0)$-style
composition) is in fact *the same* vertex as $R_2$ once you notice
$a=p_1/2=p_2$ is the "bisect $p_1$" tie and $b=p_4$ is the *tail's own*
recursive optimum landing on the analogous tie one level down — i.e. it was
never really a "new" cross-tie pattern, just $R_{n-1}$ described in
different notation. Also directly checked (`probe5.py`) that asymmetric
single cuts, or cutting $p_1$ together with $p_3$ instead of $p_2$
(comp $(1,0,1,0)$), give strictly larger $A$ ($1/5$, not $1/15$) — confirming
the "symmetric bisection into the *next rung specifically*" is the unique
winning shape, not just "any single cut."

### Assessment: promising vs dead end
- **Induction on $c$ (as literally posed): a dead end** — confirmed by exact
  exhaustive computation, not just suspicion. There is no smooth monotone
  step to prove; recommend the outliner **not** build an approach around
  "vary $c$ from $0$ to $n$."
- **Genuinely promising alternative target, reachable from this same data:**
  reduce the whole lower bound to an **induction on $n$** (not $c$), of the
  shape: *"Xiang Yu's globally optimal response always spends its first
  unit of budget as a symmetric bisection of $p_1$ into two copies of $p_2$,
  and the remainder recursively optimally on the $(n-1)$-tail; any response
  that does not bisect $p_1$ this way (including $c=0$, and including
  asymmetric or multi-cut allocations on $p_1$) is strictly dominated."*
  This is very close to — arguably a direct generalization of — the
  already-certified `symmetric-split-c1-lower-bound` (which only compares
  the symmetric $c=1$ bisection against *all tail refinements*, for $n=3$
  unconditionally and general $n$ conditionally on $c(n-1)$). The missing
  piece to close the loop, per this round's numerics, is **not** a new
  cross-term inequality at all — it is an **exchange/domination lemma**:
  *any* allocation of Xiang Yu's budget to $p_1$ other than "exactly one
  symmetric bisection" is weakly dominated by (gives $A\ge$) the symmetric
  bisection followed by the recursively-optimal tail play. If provable in
  general (the $n=3,4$ exhaustive vertex search is strong evidence, not yet
  a proof), combined with `tail-self-similarity` this closes the general-$n$
  lower bound by clean induction on $n$, sidestepping the entire
  $c$-parametrized casework the population has been stuck on. This is a
  genuinely different top-level target from every live approach's current
  framing (all currently attack "$(*)$ for fixed $c$"; this reframes as
  "$p_1$'s own optimal treatment is forced, independent of $c$, so casework
  on $c$ was never the right variable").
- Caveat: $n=5$ could not be exhaustively checked in the time budget (the
  vertex search is combinatorially expensive — $O\!\binom{\text{\#hyperplanes}}{d}$
  exact linear solves). The $n=3,4$ evidence is exact and complete for those
  two cases, but is still only 2 data points beyond the already-known
  $n=1,2$; treat the "always exactly one bisection of $p_1$" claim as a
  strong conjecture pending either a general proof or a partial re-run at
  $n=5$ with a smarter (pruned) vertex search.

### Cheap-kill checks also run
- Confirmed no fragment/permutation degeneracy issue: every found vertex was
  cross-checked against direct sort-and-alternate-sum on the raw multiset
  (built into `A_of_vals`), not just the odd-run-reduced form.
- Confirmed $c=0$'s minimum ($2^{n-1}f(n)$) is consistent with, and in fact
  much sharper than, the already-certified `untouched-top-piece-lower-bound`
  (which only claims $\ge f(n)$) — the certified lemma is far from tight in
  this sub-case, which is fine (it was never claimed tight), but worth
  flagging: proving the sharper $2^{n-1}f(n)$ value in general is easy
  bookkeeping (Odd-Run Reduction Lemma on the untouched-top-piece family)
  and could be added as a strict-inequality corollary if useful, though it's
  not needed for the lower bound itself since $2^{n-1}f(n) > f(n)$ already
  gives what's needed for $c=0$.

## Knowledge-base / lemma pointers
- `vertex-minimum-theorem`, `odd-run-reduction-lemma` — used directly, exact
  computational engine for this probe.
- `tail-self-similarity`, `cascading-halving-family-characterization`,
  `symmetric-split-c1-lower-bound` — the numerics point straight back at
  these three as the load-bearing certified facts; the missing step is the
  domination/exchange lemma described above, not a new inequality family.
- No new crux-corpus lookup performed this round (out of scope for this
  probe's dispatch — focused entirely on the $c$-induction question per
  instructions); the sibling explorer(s) covering corpus retrieval should be
  consulted for that axis.

## Dead ends confirmed (do not retry)
- Smooth monotonicity/exchange induction directly on $c$ (holding $n$ fixed):
  refuted by exact exhaustive computation at $n=3,4$ — $A_{\min}(c)$ is flat
  for $c\ge1$, not increasing.
- Treating $c=2,3,\dots$ as genuinely different multi-cut allocations on
  $p_1$: every such "win" found is a degenerate relabeling of the $c=1$
  solution (a real cut plus zero-length padding), not new structure.
