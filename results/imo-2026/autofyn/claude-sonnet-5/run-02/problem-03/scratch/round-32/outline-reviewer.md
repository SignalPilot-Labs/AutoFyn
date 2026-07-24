## imo-2026-03 — outline review, round 32

### 0. Independent re-derivation of the reconciliation claim (Case (ii) of h(m)'s vertex c=t∈S'')

I re-derived this from scratch against the actual object in
`greedy-halving-adversary.md` lines 7239–7309 (not just the outliner's
restatement) and ran an independent exact-`Fraction` simulation.

**The object.** Case (ii) fixes $q_2$ untouched in $S''$ and $t\ne q_2$
removed. $S''=\{q_2\}\cup R$ where $R$ is a legal $\le(m-2)$-cut refinement
of the length-$(m-1)$ tail $\{q_3,\dots,q_{m+1}\}$ (full budget carries
over since none was spent on $q_2$). Via `sharp-dominant-removal-identity`
the target reduces to $(\dagger)$: $A(R\setminus\{t\})\le q_2-f(m)$.

**The argument, checked line by line:**
- Mass is refinement-invariant: $\mathrm{Total}(R)=\mathrm{Total}
  (\{q_3,\dots,q_{m+1}\})$ for *any* cut count — trivially true (splitting
  preserves sum).
- Ladder telescoping: for a ratio-2 tail, $\sum_{i=3}^{m+1}q_i =
  q_3(2-2^{-(m-2)}) = 2q_3-q_{m+1}$. Since $q_2=2q_3$ and (per line 7182 of
  the file) $q_{m+1}=f(m)$ exactly, this is $q_2-f(m)$. Verified this is
  the *same* file's own definitions, not a new assumption.
- Fact 2 ($A(S)\le\mathrm{Total}(S)$ for any multiset of nonnegative
  reals): $A(S)=O(S)-E(S)\le O(S)\le O(S)+E(S)=\mathrm{Total}(S)$ — this
  is already inline in `rank-pigeonhole-budget.md` line 873, just not yet
  a standalone lemma file, exactly as the outline says.
- Removing $t>0$ (piece lengths are positive) strictly decreases mass:
  $\mathrm{Total}(R\setminus\{t\})=(q_2-f(m))-t$.
- Combine: $A(R\setminus\{t\})\le\mathrm{Total}(R\setminus\{t\})=
  (q_2-f(m))-t<q_2-f(m)$. This **is** $(\dagger)$, with strict slack $t$.

I ran an independent script (random ratio-2 ladders $m=3..9$, random legal
refinements $R$ of the tail with $\le(m-2)$ cuts randomly distributed,
random $t\in R$ removed, 3000 trials each): **zero violations**, and the
observed max of $A(R\setminus t)$ sat comfortably below $q_2-f(m)$ in
every trial, consistent with the proved strict bound. **The reconciliation
note's claim is correct**: this vertex closes unconditionally for every
$m\ge3$ via Fact 2 + mass conservation alone, with no dependence on
$\mathrm{MaxCeil}(m\ge5)$ or the Necessity Theorem.

**Why the two explorers disagreed, resolved.** `math-explorer-maxceil5.md`
describes the same-named object ("q2 untouched, t≠q2") as "not a legal
refinement of any clean ratio-2 tail at any rescaling, so neither the
$(\star_k)$ family nor `single-rung-removal-closed-form` apply directly" —
this is true but is not a contradiction: it correctly rules out the tight
$(\star_k)$-family machinery, but doesn't consider (or rule out) the
cruder Fact-2/mass-conservation bypass, which works precisely *because*
this vertex has a full factor-of-$\sim2$ slack ($q_2=2q_3$, and an extra
point $t$ is removed on top). `math-explorer-punctured-maxceil.md` is the
only report that actually traced this specific vertex's algebra, and it
holds up. The outliner's verdict (follow punctured-maxceil, treat
maxceil5's caution as a correct *general* pattern-matching warning that
doesn't apply to *this* specific vertex) is correct, and the note properly
preserves maxceil5's warning for the genuinely different, still-open
"split-rung fragment removed" sub-case of Case (i) (which does need the
tight bound $q_3-f(m)$, no slack, and correctly remains tied to
$\mathrm{MaxCeil}(m-1)$). **No fix needed here — approve as reconciled.**

### 1. greedy-halving-adversary — revise — APPROVE

- Skeleton steps 1–4 (Case (ii) closure) verified above; sound and
  correctly scoped (Case (i)'s split-rung sub-case explicitly NOT
  conflated — good, this is the exact trap flagged in the dispatch).
- Step 2 (extracting Fact 2 as a standalone lemma) is legitimate
  bookkeeping — Fact 2 is already used informally (line 873 of the
  sibling file) and is about to be cited by name from a second file;
  extracting it avoids a future "which file owns this" ambiguity.
- Step 3's shifted-index ladder identity is a genuine one-line
  re-derivation of an already-used mechanism (Theorem 42's
  $q_1-\mathrm{Total}(S'')=f(m)$), not a new unproven lemma — confirmed
  by my own computation above.
- Step 5's citation of the sibling's $\mathrm{MaxCeil}(m)$ for vertex
  $c=x$ is already independently verified as a genuine term-for-term
  identity (both explorer reports and the file itself, lines 7176–7190,
  confirm this from both sides) — correctly not re-derived.
- Step 6 (checking whether $h(3)$'s simultaneous-cuts piece is now fully
  closed) is appropriately hedged as "worth confirming... not just
  assumed," not asserted — good practice given this project's history of
  caught false-closure claims.
- No dead end repeated; no case skipped in the part being closed this
  round (Case (ii) is a clean, exhaustive sub-case of the vertex's own
  case split, disjoint from Case (i) by construction — "$q_2$ untouched
  and $t\ne q_2$" vs. "$q_2\notin W$ as an exact value").
- Minor note for the builder (not blocking): when writing the standalone
  Fact 2 lemma file, state the nonnegativity-of-elements hypothesis
  explicitly (it's used implicitly today) since it will now be cited by
  name from two files.

### 2. lp-duality-certificate — revise — APPROVE

- The $n=3$ case-(b2) precedent (`lemmas/case-b2-n3-covering-closure.md`)
  is a real, reviewer-certified Farkas-covering closure — I read it in
  full. Its history is instructive and the outline correctly absorbs the
  lesson: that lemma's own round-26 near-miss (an attempted
  generalization was refuted because a chamber's closed form silently
  relied on an ordering assumption, $p_1<T/2$, not explicit in the
  Farkas certificates themselves) is exactly the failure mode this
  outline's step 5 guards against by demanding the branch case-split be
  proved exhaustive "by an explicit logical argument... not a sampling
  check." Good — this is the right lesson drawn from the right precedent.
- The plan's structure (assemble from existing certified chamber
  instances first, derive the new "leave-2-untouched" 3-element extension
  only if gaps remain) is a reasonable, incremental order of attack, not
  an overclaim.
- The "Watch out" section explicitly reiterates the cut-budget bug the
  round-32 explorer caught (illegal 5-cut "bisect all 5 pieces" chamber
  producing a spurious clean coverage result) and the round 29–30
  false-coverage history — both correctly treated as live risks to guard
  against, not resolved issues.
- Sanity check: both known hard witnesses ($p_1/T\approx0.379$,
  $\approx0.467$) are confirmed (by the explorer, cross-checked against
  the file) to lie inside $\mathcal R'$ and are named as required
  landing tests for any proposed branch case-split — appropriate.
- No fatal flaw found in the transplant; the technique (Farkas
  nonnegative-combination infeasibility certificates over a finite,
  exhaustive branch case-split) is exactly the right tool for this kind
  of "does a finite named-chamber family cover a box" question, and has
  a working, reviewer-certified precedent one dimension down.

### 3. rank-pigeonhole-budget — revise — APPROVE

- Verified the cited §7.10.4 "untouched-top branch ⟺ MinFloor($\ell-1$)"
  reduction directly in the file (lines 3226–3259): it is proved (one
  line, `sharp-dominant-removal-identity` + Fact 2 + the ratio-2 tail
  identity $R(\sigma)+\sigma_\ell=2\sigma_1$), already "polarity-verified,"
  and its only stated blocker ("MinFloor only partially closed") is
  removed now that round 31 fully closed $(\star_3)=\mathrm{MinFloor}(4)$
  (confirmed directly in `current.md`, e.g. lines 2748–2843: "$(\star_3)=
  \mathrm{MinFloor}(4)$ now fully closed"). So Opening 1 (instantiating at
  $\ell=5$ to close $\mathrm{MaxCeil}(5)$'s top-untouched branch "for
  free") is a legitimate, cheap corollary, correctly identified as such
  and not yet banked.
- Step 3–4 (enumerate the $\sigma_2$-touched residual's shapes for
  $\mathrm{MaxCeil}(5)$, reusing the same toolbox that closed
  $(\star_3)$) is a sound, structurally-transferable plan; the outline
  correctly flags it may be a larger census than $(\star_3)$'s 20 shapes
  and explicitly permits leaving some shapes open if honestly reported —
  appropriate scoping, not an overclaim risk.
- Step 5 ("do NOT re-attempt cheap two-peel + Fact 2 directly on
  (7.15.1)") correctly cites the Necessity Theorem's own proof that this
  route provably reduces to the false inequality $z_1\ge\sigma_2$ — a
  genuine dead end correctly avoided, not re-litigated.
- The outline explicitly reminds the builder the Necessity Theorem is
  one-directional (its condition being satisfiable via $(\star_3)$'s
  closure does not imply sufficiency) — this guards against exactly the
  kind of overclaim this project's history shows it is prone to
  (rounds 29–30's false coverage claims). Good discipline.

### Cross-cutting checks

- **Whole-attempt check:** all three approaches still each target the
  full problem ($c(n)=2^n/(2^{n+1}-1)$ for every $n$) via their own
  established technique (explicit adversary strategy / LP-duality
  covering / rank-pigeonhole-budget vertex census) — none is a fragment
  of a shared proof split across slugs. This is the same acceptable
  framing-diversity structure noted in earlier rounds (three genuinely
  different mechanisms converging on the same target value, not the
  same wall). No rethink needed on this axis.
- **Shared-gap risk (flagged again, unresolved and structural, not new
  this round):** all three approaches are now entangled at the same
  deep object — $\mathrm{MaxCeil}(m\ge5)$ / the top-cut, $\sigma_2$-touched
  residual — which is *exactly* the shared wall the CLAUDE.md
  plateau-rule warns about. This round's work (Case (ii)'s closure, the
  free MaxCeil(5) top-untouched corollary) genuinely narrows the shared
  wall rather than routing around it, which is the right way to spend a
  round on a shared-gap plateau, but the population should not go
  another 2–3 rounds without at least one genuinely different framing
  being scouted for the general-$n$ obstruction (e.g. a compactness/
  extremal-vertex argument avoiding the shape-census approach entirely),
  per the standing CLAUDE.md guidance — noting this for next round's
  outliner, not blocking this round's build.
- **No dead ends repeated.** Checked against `lemmas/*dead-end*.md` and
  `current.md`'s "Approaches tried" — none of the three plans re-attempts
  a recorded dead end (band-invariance, bisect-global-max, the cheap
  two-peel + Fact 2 route on (7.15.1), the false 60-chamber coverage
  claim, etc. are all correctly avoided or explicitly cited as avoided).

### Ranking

All three live approaches (`rank-pigeonhole-budget`, `lp-duality-certificate`,
`greedy-halving-adversary`) are already registered and were `stale=true`
from round 31's outcomes. No new slugs opened this round (the outline is
pure "revise" on all three, per the reconciliation note governing
`greedy-halving-adversary`). Ranking anchored to round-31 evidence:
`rank-pigeonhole-budget`'s full, unconditional closure of $(\star_3)=
\mathrm{MinFloor}(4)$ (a complete sub-result, all 20 shapes, both
directions) is stronger, concrete evidence than the other two's honest
partial narrowings, so it ranks first; `lp-duality-certificate`'s
unconditional strip closure (Half-Complement Pin Theorem, arbitrary
$p_3,p_4,p_5$) and `greedy-halving-adversary`'s 2-of-5 vertex closure via
a new reusable induction step are comparably strong, both real advances
on different fronts — scored as a draw.

```
update_ranking(problem_id="imo-2026-03", comparisons=[
  {"winner": "rank-pigeonhole-budget", "loser": "lp-duality-certificate"},
  {"winner": "rank-pigeonhole-budget", "loser": "greedy-halving-adversary"},
  {"winner": "lp-duality-certificate", "loser": "greedy-halving-adversary", "draw": true}
])
```

No `register_approach` or `copy_approach` calls needed this round (no new
slug, no requested branch).

build set: rank-pigeonhole-budget, lp-duality-certificate, greedy-halving-adversary
