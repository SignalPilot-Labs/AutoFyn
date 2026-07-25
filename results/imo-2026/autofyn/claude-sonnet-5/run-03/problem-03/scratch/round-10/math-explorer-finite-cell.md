## imo-2026-03 (lens: Finite-Cell Affine-Vertex Reduction fix + AltSum cross-feed)

### What I did
Read `current.md`, `approaches/global-lp-vertex-sufficiency.md` (Sections 1–6, the
found gap and its diagnosis) and `approaches/lp-duality-split-polytope.md`
(Round 9: General Consecutive-Block AltSum Formula, Bottom-Block-Doubling,
the 2-piece-insufficiency finding), plus
`lemmas/consecutive-block-altsum-and-bottom-block-doubling.md` and
`lemmas/singleton-interleaving-and-k-anchor-merge.md`. Then I **computed
exactly** (sympy, exact `Fraction`/`Rational`, no floats) the vertex set
contributed by just the *region-defining* part of $L$ — i.e. $\{p_1-\tfrac12,\
p_i-p_{i+1}-\gamma(n)\ (i=1,\dots,n),\ p_k\}$ — for $n=2,3,4,5,6$, and did a
numeric (Nelder–Mead multi-restart, same method the round-9 builder used) check
of $V(q)$ at the two "genuinely new" (non-boundary-degenerate) vertices for
$n=3,4$.

**Important scope caveat, stated up front**: this is only the sub-piece of $L$
that does NOT depend on $\Sigma(n,k)$ (the shape-validity / branch-comparison
functionals from the Global Vertex Lemma). It answers "how does adding $p_k$
change the *region's own* corners" concretely, which is the specific gap the
reviewer found — but it does **not** enumerate the full $Q$ (which also needs
$(k-1)$-subsets drawn from $\Sigma$'s functionals). That remains the
"tractability of $|\Sigma(n,k)|$" obstruction, unaddressed by this round's
computation, exactly as `current.md` already flags.

### Exact computation: the region-only vertex set is small and linear in $n$

Enumerating all $\binom{n+2}{n}$ candidate $(k-1)$-subsets of the $(n+2)$-element
region functional list ($p_1-\tfrac12$, $n$ gaps, $p_k$), solving each, and
keeping the feasible/distinct ones:

| $n$ | $k$ | candidate subsets | distinct feasible vertices | # with $p_k=0$ |
|---|---|---|---|---|
| 2 | 3 | 6 | 3 | 0 |
| 3 | 4 | 10 | 5 (one degeneracy: 4 tag-combos collide at one point) | 3 |
| 4 | 5 | 15 | 8 | 6 |
| 5 | 6 | 21 | 10 | 8 |
| 6 | 7 | 28 | 12 | 10 |

For $n\ge4$ the pattern is **exactly $2n$ distinct vertices** (verified $n=4,5,6$;
$n=3$ has one accidental degenerate collision dropping it to 5, $n=2$ has 3 not 4
— small-$n$ boundary effects, not a growth-rate anomaly), splitting cleanly as:
- **2 vertices with $p_k>0$**: (a) $p_1=\tfrac12$ + all gaps but one tight; (b)
  every gap tight (no $p_1=\tfrac12$ constraint) — i.e. the "uniform AP-with-
  common-difference-$\gamma(n)$" configuration.
- **$2(n-1)$ vertices with $p_k=0$**: for each choice of "which one gap
  constraint is dropped," combined with either $p_1=\tfrac12$ or the remaining
  $n-1$ gaps tight, plus $p_k=0$.

Concretely at $n=6$: e.g. $p=(59/127,58/127,4/127,3/127,2/127,1/127,0)$ — a big
top jump then an exact AP tail $4,3,2,1,0$ (times $\gamma(6)=1/127$) — and
$p=(1/2,157/1524,\dots,97/1524)$ (all gaps at $\gamma(6)$, no $p_1$ constraint).

**Structural observation.** Every $p_k=0$ vertex is, by inspection, exactly a
$(k-1)=n$-piece configuration with one vanishing coordinate — i.e. a limit
point of the already-closed **slack-budget regime $k\le n$**. By the certified
**Lipschitz continuity of $V$** (`global-lp-vertex-sufficiency` Section 2,
already certified — $|V(p)-V(p')|\le\|p-p'\|_1$), $V$ at these boundary points
is controlled by (in the limit, equal to) $V$ of the corresponding $n$-piece
configuration, which the $k\le n$ closure already handles. **This suggests
$2(n-1)$ of the $2n$ region-only vertices need no fresh work at all** — they
reduce to already-proved territory via continuity, leaving only the **2**
non-degenerate vertices (the $p_1=\tfrac12$-anchored one and the "all gaps
uniformly tight" one) as genuinely new candidates from this sub-list. This is a
plausible reduction, not yet a proof — the reduction-via-continuity step itself
(taking the $p_k\to0^+$ limit rigorously and matching it to the $k\le n$
closure's exact statement) would need to be written out and checked against
however that closure is actually stated.

### Numeric check of $V$ at the 2 genuinely-new vertices ($n=3,4$)

Using the same multi-restart Nelder–Mead method the round-9 builder used
(Section 5 of its file), evaluated $V$ at both non-$p_k=0$ region-only vertices:

- $n=3$, $c(3)=8/15\approx0.5333$: both vertices give $V\approx0.5000$ exactly
  (best response: $\mathbf m=(2,0,1,0)$ or similar), margin $\approx0.0333=
  c(3)-\tfrac12$ exactly.
- $n=4$, $c(4)=16/31\approx0.5161$: both vertices again give $V\approx0.5000$
  exactly, margin $\approx0.0161=c(4)-\tfrac12$ exactly.

**Conjectural pattern (numeric only, 2 instances at 2 values of $n$, not
proved)**: these two "region-corner" vertices are numerically *easy* —
$V\approx\tfrac12$ is achieved, well inside $c(n)$, and the achieved margin
matches $c(n)-\tfrac12$ suspiciously exactly, suggesting a *trivial*
bisection-type response (e.g. a $k$-Anchor-Merge-style construction,
`lemmas/singleton-interleaving-and-k-anchor-merge.md`, Theorem 10, with all
$\ell_m=0$) already clears them, not requiring any elaborate $\Sigma$-shape
search. If this holds in general (unverified beyond 2 instances), the region's
own corners are *not* where the hard instances of the Existence Theorem live —
consistent with round 8/9's finding that hard "survivor" instances are
interior points found by more elaborate multi-piece ties (Section 5 of
`global-lp-vertex-sufficiency`), not simplex corners.

### Does the AltSum formula help?

**Yes, structurally, for the region-only corners** — but the connection is to
`lemmas/singleton-interleaving-and-k-anchor-merge.md` (Theorem 9/10) more
directly than to the Consecutive-Block AltSum Formula per se, because the
$p_k=0$-tail vertices have an *exact AP structure with common difference
$\gamma(n)$*, which is exactly the shape `lp-duality-split-polytope`'s
Consecutive-Block formula $\mathrm{Blk}(c,m)$ was built to compute. Concretely:
if a candidate response bisects most pieces and only "peels" the AP tail, the
tail's own contribution to $\mathrm{OddSum}$ (or the dual $\mathrm{AltSum}$
quantity used by the sibling approach) is exactly $\mathrm{Blk}(c,m)$ for
appropriate $c,m$ — i.e. **the AltSum machinery gives a plug-in exact formula
for evaluating (not just bounding) responses at exactly this class of
vertices**, once a shape/response is proposed. This is a genuine, concrete
tool to turn the numeric $V\approx0.5$ findings above into exact-arithmetic
proofs at these 2(+ the $2(n-1)$ boundary) vertices, by writing the numerically-
found near-bisection response in closed form and evaluating its exact
AltSum/OddSum via Theorem 9/10 or Blk($c,m$), rather than trusting Nelder–Mead.
**It does not help with the unbounded-$|\Sigma(n,k)|$ obstruction** — that
problem is about candidate vertices coming from the *shape* functionals
($x_\sigma$, $f_\sigma-f_\tau$), which are combinatorially about which
fragments get tied to which, not about the region's own AP-tail geometry; the
AltSum formula's domain (consecutive-integer / AP blocks) doesn't obviously
generalize to bound an *arbitrary* shape's affine formula.

### Distinct openings for the outliner
1. **Narrow fix + continuity shortcut.** Add $p_k$ to $L$ (as instructed);
   then argue the $2(n-1)$ boundary ($p_k=0$) vertices reduce via Lipschitz
   continuity to the already-closed $k\le n$ slack-budget regime, leaving only
   2 region-corner vertices per $n$ needing direct work — a genuinely smaller
   target than re-deriving the whole $(k-1)$-subset machinery from scratch.
   (Needs: precisely restating the $k\le n$ closure's exact hypotheses to
   confirm the limit argument applies verbatim.)
2. **Exact-arithmetic upgrade of the numeric $V\approx1/2$ finding.** Use
   Theorem 10 (General $k$-Anchor-Merge Lemma, certified) to produce an exact
   closed-form response at the 2 region-corner vertices for general $n$ (not
   just $n=3,4$ numerically) and prove $V\le c(n)$ there rigorously — likely a
   short, clean argument given the clean numeric pattern found.
3. **The real obstruction is elsewhere.** Both this round's computation and
   round 9's Section 5 finding point the same way: the region's simplex
   *corners* are easy; the hard "survivor" instances are interior,
   multi-piece-tie configurations. The outliner should not expect the
   $(k-1)$-subset vertex-fix to be the bottleneck — the bottleneck remains
   classifying/bounding $|\Sigma(n,k)|$, unaddressed by this scouting.

### Candidate technique(s)
Lipschitz-continuity boundary reduction (already certified, Section 2 of
`global-lp-vertex-sufficiency`) + General $k$-Anchor-Merge Lemma (Theorem 10,
certified) for the 2 non-degenerate region-corner vertices; Consecutive-Block
AltSum Formula (certified) as the exact-evaluation tool once a specific
tail-peeling response shape is proposed at an AP-structured vertex.

### Cheap-kill candidates
- Check whether the "all gaps tight" vertex (no $p_1=\tfrac12$) is provably
  dominated (in the Lipschitz sense, or literally) by the $p_1=\tfrac12$
  vertex or by an interior point — if so it can be dropped from the target
  list entirely.
- The $p_k=0$-vertex reduction-via-continuity idea above is itself a cheap
  potential kill of $2(n-1)$ of the $2n$ region-only vertices — cheap to state,
  not yet verified against the exact statement of the $k\le n$ closure lemma.

### Knowledge-base entries to use
None of `knowledge_base.md`'s generic entries were newly consulted this round
beyond what's already cited in the two approach files (LP vertex/extreme-point
facts, standard compactness/continuity). The relevant *project-internal*
lemmas are: `lemmas/global-vertex-lemma-and-lipschitz-continuity.md`,
`lemmas/singleton-interleaving-and-k-anchor-merge.md`,
`lemmas/consecutive-block-altsum-and-bottom-block-doubling.md`.

### Analogous past problems (cruxes)
Not queried this round — the terrain (LP vertex enumeration under a discrete
combinatorial minimax, hyperplane arrangements) is highly problem-specific to
this project's own machinery; a generic crux-corpus search is unlikely to add
value beyond what's already cited in the approach files (this was flagged as
"none obviously new" in prior rounds' explorer reports too, per `current.md`'s
lack of any crux citations in this approach's history).

### Prior progress
See `current.md` — Sections 1–4 of `global-lp-vertex-sufficiency` are fully
certified except the found gap (missing $p_k\ge0$ in $L$); this round's
computation is new (not previously done): the exact region-only vertex count,
its $p_k=0$/$p_k>0$ split, the continuity-reduction idea, and the numeric
$V\approx1/2$ check at the 2 non-degenerate vertices for $n=3,4$.

### Dead ends (do not retry)
- Concavity of $V(p)$ — retired for good (round 9, genuine counterexample).
- Treating the triangular family's landmarks as an already-catalogued cheap
  survivor for the arrangement — `lp-duality-split-polytope` round 9
  explicitly warns against this (2-piece responses provably fail to close it
  for large $n$).

### Small-case / intuition notes (all labeled conjecture where numeric)
- **Exact** (sympy, not conjecture): region-only vertex count is $2n$ for
  $n\ge4$ ($3$ at $n=2$, $5$ at $n=3$ due to a degenerate collision), split
  $2$ (with $p_k>0$) / $2(n-1)$ (with $p_k=0$).
- **Conjecture** (numeric, Nelder–Mead, 4 instances total across $n=3,4$): the
  2 non-degenerate region-corner vertices per $n$ are "easy," achieving
  $V\approx\tfrac12$ well under $c(n)$, with margin matching $c(n)-\tfrac12$
  suspiciously exactly — suggesting a simple closed-form bisection/anchor-merge
  response (not requiring elaborate $\Sigma$-shape search) proves the bound
  there. Not verified beyond $n=3,4$ or in exact arithmetic.
- **Conjecture** (structural, not yet formally checked against the exact
  statement of the $k\le n$ closure lemma): the $2(n-1)$ boundary ($p_k=0$)
  vertices reduce to that already-closed regime via Lipschitz continuity,
  needing no fresh $\Sigma$-enumeration work.
