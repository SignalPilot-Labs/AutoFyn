## imo-2026-03 — lens: attack (†) directly

### Exact statement of (†) (Branch B, N even), from `rank-pigeonhole-budget.md` §4.8–4.9
Setup: $\tau=(\tau_1,\dots,\tau_m)$ ratio-2 superincreasing ($\tau_i=2\tau_{i+1}$), $R(\tau)=\sum\tau_i$.
$F$ a "Case I" partition of $s\in(0,2\tau_1]$ into $k\le m+1$ positive parts, $\max F\le\tau_1$.
Target (equivalent to Claim (A)'s Case I, via $A=\mathrm{Total}-2E$): $E(F\cup\tau)\le R(\tau)$ (4.3),
where $E(S)$ = sum of $S$'s even-sorted-rank elements.

Peel-the-global-minimum strong induction on $N:=m+k$: remove $\mu:=\min(F\cup\tau)$.
- Branch A ($\mu=\tau_m$): **fully closed** (both $k\le m$ via IH, and the $k=m+1$ boundary via
  Half-Bound Lemma + identity $R(\tau)+\tau_m=2\tau_1$).
- Branch B ($\mu=\min(F)<\tau_m$, i.e. the global min is an $F$-fragment strictly below the tail's
  floor): if $N$ odd, closes trivially ($\mu$ sits at an odd rank, doesn't touch $E$). **If $N$ even
  — this is exactly $(\dagger)$** — removing $\mu$ shifts it out of an *even* rank, so
  $E(S)=E(F'\cup\tau)+\mu$ where $F'=F\setminus\{\mu\}$; the plain IH only gives
  $E(F'\cup\tau)\le R(\tau)$, but we need the sharper $E(F'\cup\tau)\le R(\tau)-\mu$. Plain induction
  doesn't supply that extra $\mu$ of slack. One candidate strengthened invariant
  ($\delta=\min(S)\cdot[N\text{ even}]$) was tried and refuted at the base case ($m=1,k=1$, $s$
  close to $\tau_1$) — do not retry verbatim.

### Distinct openings found this round

**1. (Most promising) Exchange-smoothing / LP-vertex reduction on the maximization of $E(F\cup\tau)$ directly — bypass the peel-induction entirely.**
For *fixed* $m,k,s,\tau$, $E(F\cup\tau)$ is (within any fixed relative-order region of the $k+m$
values) a **linear** functional of $F$'s free simplex coordinates (the $F_i$ sum to the fixed $s$):
it is literally "sum of whichever elements land at even sorted rank." So maximizing $E$ over the
simplex $\{F: \sum F_i=s,\ 0\le F_i\le\tau_1\}$ is a linear-objective-over-polytope problem, and its
maximum is attained at a **vertex** — exactly the situation the population's already-certified
`vertex-minimum-theorem` (and `odd-run-reduction-lemma` for evaluating $A$/$E$ at a tie-vertex) was
built for, just applied to $E$-maximization over $F$ instead of $\Phi$-minimization over Xiang Yu's
whole response. At a vertex, either two $F$-values are tied to each other, one $F$-value is tied to
$0$ (degenerates $k\to k-1$) or to $\tau_1$ (degenerates to Branch-A-adjacent structure), pinning
finitely many configuration types that can be evaluated in closed form. This would let (†) be
resolved by a **finite enumeration of vertex types** instead of a two-branch parity induction —
a genuinely different mechanism from peel-the-min, likely to sidestep the exact parity obstruction
that stalls it (since it never removes a single element and asks about resulting rank parity; it
instead directly characterizes maximizers).
- **Crux-corpus transplant, strongly analogous**: `aimo-0146` (2017-mathematicians/S(G) problem,
  subtopics `extremal-principle`/`double-counting`). Its exact mechanism: *"Maximize a fixed
  weighted sum of a sorted nonnegative sequence under a sum constraint by exchange-smoothing weight
  toward the higher-coefficient positions until the free coordinates equalize and the tail drains,
  then enumerate the few surviving profiles."* Concretely: if $x_i>x_{i+1}\ge x_{j-1}>x_j$ for
  $i<j$ among the free sorted coordinates, replacing $(x_i,x_j)\to(x_i-1,x_j+1)$ strictly increases
  the weighted sum $\sum a_ix_i$ (weights $a_i$ decreasing in $i$) while preserving the sum
  constraint — repeating this smoothing collapses to a few extremal "plateau" profiles that are then
  checked by hand. This maps almost directly onto (†)'s structure: $E(F\cup\tau)=\sum(\text{rank-}
  r\text{ value})\cdot[r\text{ even}]$ is exactly a weighted sum of the sorted merged sequence with a
  0/1 weight pattern, and $F$'s coordinates are the free ones. I recommend the outliner adapt this
  exchange-smoothing lemma directly (it is a self-contained, purely combinatorial two-line argument,
  reusable without modification) rather than re-deriving vertex enumeration from scratch — it is a
  faster route to the same conclusion as the vertex-minimum-theorem application above, and the two
  are essentially the same idea (LP-vertex = terminal point of exchange-smoothing).
- Note: the population's existing $F^*$ construction (§2 of `rank-pigeonhole-budget.md`: repeated
  pairs $p_i,p_i$ plus a repeated triple at the bottom) is *exactly* the shape exchange-smoothing
  predicts as an extremal "plateau" profile (adjacent equal values) — a strong structural hint this
  route is on the right track, not just superficially similar.

**2. Peel-both-ends simultaneously (tried by hand this round, found to reproduce the OLD obstruction — flag as tried-and-not-useful, don't re-attempt naively).**
Instead of peeling only $\mu=\min(F)$, remove both $\max(S)=\tau_1$ (assuming generic, no tie) and
$\mu$ together in one step. Since they sit at global ranks $1$ and $N$, removing both shifts the
middle block down by exactly 1 (only the max's removal causes a shift), giving, when $N$ is even:
$$E(S) = \mu + O(S''),\qquad S'':=S\setminus\{\tau_1,\mu\}\ (\text{size }N-2),$$
i.e. old-rank-2..N-2 (even) map onto new odd ranks of $S''$, so $E(S)$ relates to the **odd**-rank
sum of $S''$, not $E(S'')$. Converting via $O=(\mathrm{Total}+A)/2$ turns the target back into
needing an **upper bound on $A(S'')$** — i.e., this reproduces exactly the old obstruction (4.1)
that peel-the-min was specifically designed to avoid. **Do not pursue this "peel both ends at once"
variant** — it's a strictly worse reformulation than the single-min peel already on file.

**3. Boundary-continuity idea (untested, flagged as a candidate, not verified).** Branch B requires
$\mu<\tau_m$ strictly; Branch A is exactly $\mu=\tau_m$ and is fully closed. If one can show slack
$R(\tau)-E(F\cup\tau)$ is continuous in $\mu$ (obviously true, it's a finite sum) and, more usefully,
*monotonic* in $\mu$ near the boundary $\mu\to\tau_m^-$ (e.g. via a directional-derivative/local
exchange argument showing decreasing $\mu$ while keeping $s$ fixed by redistributing the freed mass
elsewhere in $F$ can only decrease $E$, i.e. Branch A's boundary is the *worst* case as $\mu\to\tau_m$
from below), then (†) would follow from Branch A's already-proven closure by a limiting/perturbation
argument rather than more induction. I did not verify monotonicity — numerics below only confirm
slack stays nonnegative, not the monotonicity claim; this needs to be checked before building on it.

### Cheap-kill / structural pruning
- Numerically confirmed (my own independent script, exact `Fraction`, 20000+5510 filtered Branch-B
  N-even trials, $m\le6$): slack $R(\tau)-E(F\cup\tau)$ is **always $\ge0$** in this regime, minimum
  observed $1/34$; **the tightest cases found are all $m=1,k=1$ (the base case itself)**, where
  slack $=\tau_1-s\to0$ as $s\to\tau_1$ — i.e. the "hardest" instances are the already-proven base
  case, not some deep new configuration. A separate float/Nelder-Mead local-search minimization
  (multistart, $m=2..6$, $k=m$ i.e. $N=2m$) found local minima at slack $=2\tau_m$ exactly for each
  $(m,k=m)$ pair tested — consistent, not proved; worth double-checking with exact rationals if the
  outliner wants a sharper conjectured closed form for the worst case.
- No parity/pigeonhole argument found that kills $(\dagger)$ outright in one line; the structural
  fact worth exploiting is that $(\dagger)$ always has $k\ge2$ (needs $F$ to have a genuine "second
  smallest" element structurally distinct from $\tau_m$), so $F'$ after peeling always still has
  $\ge1$ part — no degenerate-empty-$F'$ edge case to worry about separately in this branch (unlike
  Branch A's $s'=0$ sub-case in §3 Case II).

### Candidate technique(s) for the outliner
1. **Primary recommendation**: import/adapt `vertex-minimum-theorem` + `odd-run-reduction-lemma`
   (already certified in this project) to directly characterize the maximizer of $E(F\cup\tau)$ over
   Case-I partitions as a finite vertex enumeration, powered by the exchange-smoothing lemma from
   `aimo-0146` (stated above, fully self-contained, adapt-not-cite). This targets (†) — indeed all
   of Case I — in one stroke rather than casework on parity of $N$.
2. Fallback if (1) stalls: strengthen the peel-the-min induction hypothesis itself. The needed
   invariant is of the form $E(F\cup\tau)\le R(\tau)-\delta(F,\tau)$ with $\delta$ preserved through
   *both* Branch A and Branch B; $\delta=\min(S)\cdot[N\text{ even}]$ is refuted (see above) — a
   next natural guess, untested here: $\delta$ depending on $k$ (number of remaining $F$-parts) or
   on $s-k\mu$ (excess mass above the trivial floor), but this needs care since the base case
   ($k=1$) has $\delta=0$ forced (slack $=\tau_1-s$ can be arbitrarily small, no room for a positive
   $\delta$ there) — any $\delta$ must vanish at $k=1$.

### Knowledge-base entries to use
- `integral-alternating-sum-formula` (defines $A$, used for the $A\ge0$/Half-Bound facts).
- Certified lemmas already in `results/imo-2026-03/lemmas/`: `vertex-minimum-theorem`,
  `odd-run-reduction-lemma`, `sharp-dominant-removal-identity`, `half-bound-lemma`,
  `case-ii-closure-theorem`, `ladder-self-similarity-constant`.
- `knowledge_base.md` generic entries on LP/vertex-of-polytope extremal arguments and
  exchange/smoothing arguments for sorted sequences, if present — worth the outliner double-checking
  the exact entry name there (I did not find a KB entry more specific than the crux transplant
  above; the crux is the sharper, more directly-applicable source here).

### Analogous past problems (cruxes)
- **`aimo-0146`** (combinatorics, `extremal-principle`/`double-counting`) — best match by far. Crux:
  exchange-smoothing to maximize a rank-weighted sum of a sorted sequence under a sum constraint,
  collapsing to few extremal "plateau" profiles. Directly transplantable to maximizing $E(F\cup\tau)$
  over Case-I partitions $F$ (same shape: rank-dependent weight, sorted sequence, fixed-sum
  constraint).
- Checked `aimo-0114` (min-max parity forcing via one extremal structure) and several
  `coloring-and-parity` cruxes (aimo-0074, aimo-0080) — these use parity-forcing but on a different
  kind of object (paths/tilings, not rank-alternating sums of a merged multiset); not genuinely
  analogous to (†)'s specific rank-parity issue, so I do not recommend transplanting them.
- No crux found that resolves a "peel-the-extremum, need one extra unit of slack on a parity
  boundary" gap directly — this specific shape of obstruction appears to be a genuine gap in the
  corpus's coverage of this pattern, which is why the exchange-smoothing route (attacking the
  maximization directly, sidestepping the induction's parity bookkeeping) looks like the more
  promising route than trying to patch the induction.

### Prior progress
See `results/imo-2026-03/approaches/rank-pigeonhole-budget.md` §4.8–4.9: Case I of Theorem GC($m$)
(equivalently Claim (A)'s Case I) is fully closed except for exactly $(\dagger)$. Achievability (§2)
and Case II (§3) are fully closed for all $n$. This is the sole open item standing between the
current state and closing the whole lower-bound (modulo Claim (B), owned by
`greedy-halving-adversary`, and the general upper bound, currently only closed for $n\le2$).

### Dead ends (do not retry)
- $\delta=\min(F\cup\tau)\cdot[N\text{ even}]$ as a strengthened invariant — refuted at the base case
  (already on file, §4.9 item 2).
- "Splitting a fragment never increases $E$" monotonicity — refuted with an explicit counterexample
  (already on file, §4.10).
- **New this round**: "peel both the global max and global min simultaneously" — reproduces the old
  upper-bound-on-$A(S'')$ obstruction that peel-the-min was designed to avoid; not useful as stated
  (see opening 2 above). Do not re-attempt this exact simultaneous double-peel.

### Small-case / intuition notes (conjecture, not proof)
- My own independent 20000+5510-trial exact-`Fraction` search over Branch-B-$N$-even instances
  ($m\le6$) found zero violations of (4.3), consistent with the population's existing 223,000-trial
  result — no new counterexample found, (†) still looks true.
- The globally tightest margins found are all at the $m=1,k=1$ base case ($N=2$), where slack
  $=\tau_1-s\to0$; deeper ($N\ge4$) Branch-B-even instances all showed comfortably positive slack in
  both uniform-random and float-optimization (Nelder-Mead, multistart) searches — mild evidence that
  $(\dagger)$'s "hard part" is not really at large $N$ but is fully captured by the already-proven
  base case, supporting the boundary-continuity idea (opening 3) as plausible, though unverified.
- Local-search minima at $(m,k=m)$ landed suspiciously close to slack $=2\tau_m$ exactly for
  $m=2,\dots,6$ — an unverified numeric pattern (float precision, not exact-fraction-confirmed) that
  could be worth pinning down exactly if the outliner wants a candidate closed-form worst case to
  aim a direct proof at.
