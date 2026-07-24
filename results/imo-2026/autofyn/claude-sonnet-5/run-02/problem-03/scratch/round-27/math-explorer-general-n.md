## imo-2026-03 (lens: generalizing MaxCeil exhaustive enumeration past n=7)

### (a) Shape-count growth — does it blow up, and is there a pattern?

`MaxCeil(m)`'s **top-cut branch** (§7.13 of `rank-pigeonhole-budget.md`) is
defined on a length-$m$ ratio-2 tail $\sigma$, budget $\le m-2$ cuts, with
$\ge1$ cut forced onto $\sigma_1$. The number of exhaustive
cut-*distribution shapes* $(c_1,\dots,c_m)$, $c_1\ge1$, $\sum c_i\le m-2$,
is exactly (verified by direct stars-and-bars re-derivation, matching the
file's own counts at $m=3,4$):
$$\#\text{shapes}(m) = \binom{2m-3}{m}.$$
Values: $m=3{:}1,\ m=4{:}5,\ m=5{:}21,\ m=6{:}84,\ m=7{:}330,\ m=8{:}1287,\
m=9{:}5005$ (verified by direct computation, `python3 -c "from math import
comb; ..."`). **This is genuine combinatorial (binomial) explosion, not
linear** — the technique used at $m=3,4$ (enumerate every shape, close each
by hand with a mechanism-specific sorted-order computation) is flatly
infeasible past $m\approx5$–$6$ as a hand proof; it would need to become an
automated/uniform argument, not a bigger case list, to have any hope for
general $m$.

**But the shape count is the wrong thing to worry about first** — see (b).

### (b) Can the Index-Chain Identity turn this into a clean induction instead of case-by-case blowup?

**No — and this is the single most important finding of this lens.** The
Index-Chain Identity (§7.11, `MinFloor(ℓ) ≡ (⋆_{ℓ-1})`, proved as a genuine
*equivalence*, not a one-directional implication, via the
`alternating-sum-scaling` rescaling bijection) shows that `MaxCeil(ℓ)`'s
**top-untouched branch** reduces exactly to `MinFloor(ℓ-1) = (⋆_{ℓ-2})`.
Since `(⋆_k)` is *itself* the project's central open general lower-bound
statement one level down (unconditionally certified only for $k=1,2$; open
for $k\ge3$), this means:

- `MaxCeil(ℓ)`'s top-untouched branch is unconditionally free **iff
  $\ell\le4$** — for $\ell\ge5$ it is not "hard to enumerate," it is
  **literally, provably equivalent** (not just similar in flavor) to
  proving the master lower bound $(\star_{\ell-2})$, $\ell-2\ge3$.
- So `MaxCeil(5)` (the very next instance, $n=8$) does not even get past
  its *easy* branch without first closing $(\star_3)$ — which is exactly
  the general-$n$ lower bound at level 3, i.e. essentially the same open
  problem `greedy-halving-adversary`'s even-multiplicity-tie gap is
  independently trying to close (see (c)).

Consequently there is **no available shortcut induction that avoids this
wall**: the Index-Chain Identity does not let you bypass the master
obstruction, it proves you cannot — the equivalence is exact (via a scaling
bijection, both directions), so no amount of clever casework on the
top-untouched branch alone can substitute for actually proving $(\star_k)$
for larger $k$.

**A genuinely separate, more promising structural observation** (new this
round, not previously written up): re-examining §7.13's five shapes shows
every one is closed using *only* `sharp-dominant-removal-identity`
(peeling the current global max) applied **exactly twice in a row**, plus
the trivial, unconditional `Fact 2` ($A\le\mathrm{Total}$) at the second
peel — never $(\star_k)$ for $k\ge3$. Concretely: if $S$ has a "2-deep
dominance chain" (a strict global max $f_1$, and within $S\setminus\{f_1\}$
another strict max $f_2$), then
$$A(S)=f_1-f_2+A(S\setminus\{f_1,f_2\})\ \le\ f_1-f_2+\mathrm{Total}(S\setminus\{f_1,f_2\}),$$
and by mass conservation this upper bound collapses to *exactly*
$\sigma_1-\sigma_m$ whenever $f_1,f_2$ are the two most massive pieces —
this is why every one of the five $m=4$ shapes closes with equality
approached only at the degenerate (top-untouched) boundary. This
"Double-Dominant-Peel + Fact-2" mechanism is a genuine candidate for a
**uniform** (not case-by-case) closure of the **top-cut branch only**, for
general $m$ — it uses no $(\star_k)$ input at all, so it is not blocked by
the same wall as the top-untouched branch. Whether every shape at general
$m$ admits *some* 2-deep dominance chain (possibly requiring
case-splitting on which two elements are peeled, as shape $(1,1,0,0)$
needed) is untested for $m\ge5$ and is the concrete, well-scoped open
question for a future round on this specific sub-target — it is a
combinatorial claim about superincreasing sequences under arbitrary
cut-distributions, not a re-encounter of the central obstruction, and
would be a genuinely new, reusable general lemma if it can be shown to
generalize.

Numeric spot-check (random legal refinements of the top-cut branch, exact
`Fraction` arithmetic, no violations found — evidence only, not proof):
target ratio $\mathrm{worst}/(\sigma_1-\sigma_m)$ stayed $<1$ at
$m=3,\dots,7$ (30000 random trials each; ratios $0.9997, 0.9993, 0.9910,
0.9621, 0.9398$ — random sampling under-hits the true tight vertex as $m$
grows, consistent with round-8's documented lesson that uniform random
composition search undersamples the extremal vertex, so these numbers are
weak positive evidence only, not a refutation-search).

### (c) Does general-$n$ MaxCeil closure interact with the even-multiplicity-tie gap?

**Yes, directly and provably** — this is the key cross-front finding.
`greedy-halving-adversary`'s round-26 even-multiplicity-tie gap (Theorem 40
closed the odd-multiplicity sub-case of Theorem 37's non-maximal-tie
enumeration; even-multiplicity is "the project's central obstruction," per
`run_state.md` round 26) is, in substance, an attempt to prove the general
lower bound $(\star_n)$ (equivalently $L(n)$ in `current.md`'s round-23
audit language) unconditionally for all $n$. Via the Index-Chain Identity:

- **If** `greedy-halving-adversary` (or any other front) closes
  $(\star_k)$ unconditionally for some new $k\ge3$, this **immediately and
  for free** (via §7.11's exact equivalence, no new work) unlocks
  `MaxCeil(k+2)`'s top-untouched branch — i.e. closing the even-
  multiplicity-tie gap at level $n=k$ directly hands `rank-pigeonhole-
  budget` a free extension of (7.9.1) two levels of $m$ further, *provided*
  the top-cut branch (a separate, likely-tractable combinatorial task, see
  (b)) is also closed at that $m$.
- **Conversely**, `rank-pigeonhole-budget` proving `MaxCeil(m)` for some
  $m\ge5$ in full (both branches) would, by the same equivalence run in
  reverse, constitute a proof of $(\star_{m-2})$ — i.e. it would **be** a
  proof of the general lower bound one level down, not merely progress
  toward it. This means the "generalize MaxCeil past $n=7$" front and the
  "close the even-multiplicity-tie gap" front are **not independent
  sub-projects that can be pursued in parallel and later combined** — they
  overlap exactly on the top-untouched branch, which is literally the same
  unproven statement in two notations. Effort should not be duplicated
  attacking $(\star_k)$ directly in both files; only the top-cut branch's
  peel-mechanism generalization (b) is genuinely separate/new work for the
  `rank-pigeonhole-budget` front.

This sharpens (not merely confirms) round 25/26's diagnosis: it is now a
**proved equivalence** (via an explicit scaling bijection, both directions
of implication), not just an observed pattern that "multiple fronts have
converged on tie-vertex/cut-distribution enumeration."

### Distinct openings
1. **Prove the Double-Dominant-Peel + Fact-2 mechanism generalizes to
   arbitrary $m$** for `MaxCeil(m)`'s top-cut branch specifically — a
   self-contained combinatorial claim (does every legal cut-distribution
   shape with $\ge1$ cut on $\sigma_1$ admit a 2-deep dominance chain, up
   to a bounded number of case splits independent of $m$?) that provably
   does **not** require $(\star_k)$ for $k\ge3$, hence is not blocked by
   the central obstruction. This is the one genuinely open, tractable-
   looking sub-target from this lens.
2. **Do not pursue "MaxCeil(m) for general $m$" as a standalone route to
   the general lower bound** — its top-untouched branch is an exact
   restatement of $(\star_{m-2})$, so closing it in general *is* closing
   the central obstruction, not a shortcut around it.
3. If `greedy-halving-adversary` succeeds on the even-multiplicity-tie gap
   for a specific small $n=k$ (even if not all $n$), that result should be
   **imported directly** via the Index-Chain Identity to instantly extend
   `MaxCeil`'s top-untouched branch to $\ell=k+2$ — cite §7.11, no
   re-derivation needed.

### Candidate technique(s)
- Double-Dominant-Peel + Fact-2 generalization (new candidate, untested
  past $m=4$) for the top-cut branch.
- Direct attack on $(\star_3)$ (general lower bound at $n=3$'s "one level
  down" instance) is the real bottleneck for both fronts — but this is
  already what `greedy-halving-adversary`'s even-multiplicity-tie work is
  attempting; no new technique surfaced by this lens for that piece.

### Cheap-kill candidates
- Before hand-enumerating $m=5$'s 21 shapes: first check whether the
  top-untouched branch even opens (it needs $(\star_3)$, unproved) — if
  not closed, `MaxCeil(5)` cannot be fully closed this round regardless of
  top-cut-branch progress, so effort is better spent either (i) proving
  the top-cut branch's general mechanism (task 1 above, useful whenever
  $(\star_3)$ eventually closes) or (ii) working directly on $(\star_3)$
  itself rather than on `MaxCeil(5)`'s shell.
- Shape count $\binom{2m-3}{m}$: an immediate pigeonhole/symmetry
  reduction — shapes are related by which single "extra" cut position(s)
  receive budget beyond the mandatory one on $\sigma_1$; grouping by
  "number of distinct additional indices touched" ($0,1,2,\dots$) collapses
  many shapes into a much smaller number of *qualitative* families (as
  seen in §7.13, shapes $(1,0,1,0)$ and $(1,0,0,1)$ used verbatim the same
  proof template) — worth formalizing as "shapes touching $\le2$ distinct
  tail indices always close via Double-Dominant-Peel; only shapes touching
  $\ge3$ distinct indices are genuinely new territory," rather than
  re-deriving every shape from scratch.

### Knowledge-base entries to use
None of `knowledge_base.md`'s generic entries were newly implicated by this
lens beyond what's already cited in the approach file (`sharp-dominant-
removal-identity`, `Fact 1`/`Fact 2`, `alternating-sum-scaling`, standard
LP-vertex/finite-case-enumeration principle already used project-wide).

### Analogous past problems (cruxes)
Not re-queried this round — prior rounds (1, 4) already checked
combinatorics/games-and-strategy/extremal-principle/processes-and-
algorithms subtopics and found no strong direct analog for this problem's
central obstruction; this lens's finding (an index-chain rescaling
equivalence between two "different-looking" open statements) is an
internal structural fact about the project's own machinery, not something
that maps onto a corpus crux move.

### Prior progress
`MaxCeil(3)` ($n=6$) and `MaxCeil(4)$ ($n=7$) fully, unconditionally closed
(round 26, `rank-pigeonhole-budget` APPROVE for its own Claim (A) scope;
(7.9.1) resolved through $n=7$ only, not Claim A itself which was already
fully closed earlier). See `results/imo-2026-03/approaches/rank-pigeonhole-budget.md`
§7.11–7.13.

### Dead ends (do not retry)
- Do not attempt to close `MaxCeil(ℓ)`'s top-untouched branch for
  $\ell\ge5$ by any means other than first proving $(\star_{\ell-2})$
  directly — the Index-Chain Identity is a proved *equivalence*, so no
  clever restatement/case-split can evade it (this round's finding,
  strengthens round 26's diagnosis from "not yet certified" to "provably
  requires the same open statement").
- The mis-direction bug already flagged in §7.10.4 (naively trying to
  close `MaxCeil`'s case-(i) branch via `Fact 2` alone, supplying an upper
  bound where a lower bound is needed) — already caught and documented,
  do not re-attempt.

### Small-case / intuition notes (conjectural, numeric evidence only)
- Random legal-refinement sampling (exact `Fraction`, 30000 trials each)
  found zero violations of `MaxCeil(m)`'s top-cut-branch target at
  $m=3,\dots,7$, with the achieved max approaching but not exceeding the
  target — consistent with (but not proof of) the conjecture that the
  top-cut branch holds for all $m$, independent of $(\star_k)$'s status.
  Random sampling under-hits the true extremal vertex as $m$ grows (known
  project lesson, round 8/25), so this is weak evidence only — a targeted
  vertex/coordinate-ascent search (as round 25 used successfully) would be
  needed for a real stress test at $m=5,6$ before trusting the conjecture
  further.
