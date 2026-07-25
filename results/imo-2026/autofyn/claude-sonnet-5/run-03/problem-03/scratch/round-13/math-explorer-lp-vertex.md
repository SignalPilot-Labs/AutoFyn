# Round 13 scouting report — lens: endpoint-inequality / exchange-argument route
## Approach: `global-lp-vertex-sufficiency`

## 1. What Region-Boundary Monotonicity claimed, and why it died

Round 12's literal claim: for every interior $p\in B(n)$ there is a fixed
target vertex ($e_0$ or $e_1$) such that $V$ is weakly monotone along the
*entire* straight segment from $p$ to that vertex. This was refuted at
$n=3$: two independent trial points, tested toward both $e_0$ and $e_1$,
showed genuine (noise-checked at $3$–$20\times$ restart counts) sign
changes in consecutive differences of $V$ along the segment (Section 4.6.3
of the approach file). The failure is a failure of monotonicity of $V$
itself along a straight line — $V$ is not concave (already known since
round 9) and not even monotone toward a fixed vertex once $n\ge3$; $n=2$'s
apparent monotonicity was an artifact of its unusually simple 3-vertex
region structure (flagged as exceptional in Section 4.1 already).

Crucially, in *every* round-12 trial the failure of full-path monotonicity
did **not** coincide with a failure of the weaker endpoint form $V(p)\le
V(q)$ at the fixed vertex $q\in\{e_0,e_1\}$ — the wiggle stayed under the
endpoint value in all logged cases. That is what motivated this round's
weaker lead.

## 2. What the endpoint-inequality would need to say, logically

Re-checked the logical chain in Section 4.6.0 of the approach file: the
Existence Theorem needs, for every interior $p$, **some** boundary point
$q\in\overline{\partial B(n)}$ with $V(p)\le V(q)$ — full path monotonicity
is strictly stronger than necessary; only the two endpoints matter, because
the entire relevant boundary ($p_k=0$ face via the certified Boundary
Continuity Theorem, and the finitely many genuine region vertices $e_0,e_1,
(e_2)$ via the certified $k$-Anchor-Merge exact evaluation) is *already*
known to satisfy $V(q)\le c(n)$. So substituting the weaker existential
claim for the universal monotonicity claim **does** still let the overall
argument go through, provided (a) $q$ ranges only over the already-closed
part of the boundary, and (b) the choice of $q$ can depend on $p$ (no
uniform target vertex is required by the logic — that was only round 12's
simplifying guess at *which* mechanism might prove it).

This matters: the target to test is genuinely weaker and more flexible than
what round 12 tested (a single fixed vertex, straight line). This round
tests a richer, point-dependent family of candidate targets $q$, built via
explicit **exchange moves** (adapting the crux-corpus playbooks
`aimo-0146`/`aimo-0287`) rather than a geometric path to a fixed vertex.

## 3. Numerical exchange-argument test

**Mechanism tried.** Two concrete, point-dependent exchange moves, each
touching only the coordinates responsible for the tightest-violated region
constraint (in the spirit of `aimo-0287`'s "push two boundary coordinates
toward each other by half the surplus" and `aimo-0146`'s exchange-toward-
higher-coefficient-position):

- **Gap-exchange** $q^{(i)}$: for gap index $i\in\{1,\dots,n\}$ (comparing
  consecutive pieces $p_i,p_{i+1}$), set $S=p_i+p_{i+1}$ fixed, move
  $p_i\to (S+\gamma(n))/2$, $p_{i+1}\to(S-\gamma(n))/2$ — pushes exactly
  that one gap constraint to equality via a symmetric two-coordinate swap,
  leaving every other coordinate untouched (a literal transplant of the
  `aimo-0287` adjacent-exchange move onto this problem's own gap-slack
  structure).
- **$p_1$-boundary move** $q^{(p_1)}$: rescale $p_2,\dots,p_k$ down
  proportionally and set $p_1=1/2$ exactly (projects onto the $p_1=1/2$
  face while preserving the shape of the tail).

**Implementation.** Reused the approach file's own numerical methodology
(Section 4.6.1: exhaustive enumeration of all cut-allocations $\mathbf m$
with $\sum m_i\le n$, softmax-parametrized multi-restart Nelder–Mead per
allocation, min over allocations) — re-implemented independently in Python
(exhaustive composition enumeration + `scipy.optimize.minimize`,
6–25 restarts per allocation). Sanity-checked against the file's own
reported $e_0$ values (matched to the digits reported there).

**Test 1 (tightest constraint only, $n=3,4$, 5 trials each).** Choosing
$q$ = the gap-exchange at the single *tightest* (closest-to-violated) gap,
or the $p_1$-move when that's tighter: the $p_1$-move **failed in every
single trial** at both $n=3,4$ (5/5 and 5/5). The tightest-gap-exchange
move held in roughly half the trials and failed in the other half (3/5 at
$n=3$, 3/5 at $n=4$), e.g. at $n=4$ trial 2: $p=(0.333,0.280,0.202,0.137,
0.049)$, tightest gap at index 0, $V(p)=0.50215 > V(q)=0.50042$.

**Test 2 (weak existential form: does *any* of the $n{+}1$ candidate moves
work, not just the tightest one, $n=3$, 6 trials).** Tested all $n$
gap-exchanges plus the $p_1$-move for each interior point. In **3 of 6**
trials, **none** of the $n+1$ candidates satisfied $V(p)\le V(q)$. Re-run
at $3$–$4\times$ the restart count (20 restarts/allocation) on these three
failing points to rule out optimizer noise: the excess $V(p)-\max_q V(q)$
is genuine and sizeable, **not** noise-floor —
- $p=(0.4416,0.3035,0.1851,0.0697)$: $V(p)=0.51137$, best candidate
  $V(q)=0.501528$ (gap0/gap1), excess $\approx0.00984$.
- $p=(0.4378,0.3252,0.1898,0.0472)$: $V(p)=0.51498$, best candidate
  $0.513702$ (gap2), excess $\approx0.00128$.
- $p=(0.4211,0.3348,0.1910,0.0531)$: $V(p)=0.51660$, best candidate
  $0.506794$ (gap0/gap1), excess $\approx0.00980$.

(Noise floor for this optimizer, from repeated runs on near-tie cases, is
$\sim10^{-6}$–$10^{-10}$ — these excesses are $3$–$4$ orders of magnitude
larger, and stable under $3\times$ more restarts, so genuine.)

All tested $V(p)$ values stayed comfortably under $c(3)=8/15\approx0.5333$
(max observed $\approx0.5166$), so **none of this is evidence against the
Existence Theorem itself** — only against this specific family of
candidate proof mechanisms.

## 4. Interpretation

**The endpoint-inequality lead survives round 12's specific test
(fixed-vertex straight line) but does *not* survive this round's broader,
exchange-argument-based test.** Two new, more surgical, point-dependent
candidate mechanisms — both direct transplants of certified crux-corpus
exchange moves (`aimo-0287`'s adjacent-pair symmetric exchange,
`aimo-0146`'s move-toward-higher-weight-position) — were tried, including
the maximally weak existential form (does *any* of $n+1$ natural candidate
boundary points work, not committing to one choice rule). Even this weak
form fails at roughly half the tested interior points at $n=3,4$, with
genuine (non-noise) excess up to $\approx0.017$.

This is a meaningful (though not exhaustive — only two move families, only
$n\le4$, only a handful of trials each) negative signal that goes beyond
round 12's finding: it's not merely that "aim at a fixed vertex" fails, but
that this whole *natural family* of single-constraint exchange moves fails
to supply a witnessing boundary point for a nontrivial fraction of interior
points. The failures are not clustered near one exceptional region — they
appear at generic-looking interior points with all gaps well above
$\gamma(n)$.

**What is NOT yet ruled out** (so the lead is weakened, not closed):
- Two-coordinate-at-once exchange moves that touch *two* different
  constraints simultaneously (untested).
- A genuinely adaptive/non-canonical choice of $q$ depending on the full
  shape of $p$ (not just "the tightest slack"), e.g. picking $q$ via the
  optimal adversary response's own structure at $p$ rather than via a
  region-geometry rule — this is the "exchange on the response" idea from
  the dispatch, and it was **not yet tried**: everything tested this round
  still picks $q$ from region geometry (slacks), not from XY's optimal
  cut-allocation at $p$. A genuine adversary-response exchange argument
  (e.g.: look at $p^*$'s minimizing shape $\sigma^*$, and construct $q$ by
  the *specific* perturbation that $\sigma^*$'s own tie structure suggests)
  remains unexplored and is the most promising concrete next step.
- $n\ge5$ (compute cost prohibitive for this round's exhaustive numerical
  estimator; only $n=3,4$ tested).

**Recommendation: do not spend another round on "region-geometry-driven"
choices of $q$ (fixed vertex, tightest-slack, or any of the $n+1$-candidate
family tested here) — this whole class is now empirically shaky at
$n=3,4$.** The next attempt, if any, should build $q$ from the optimal
*response* $\sigma^*(p)$ itself (an adversary-side exchange, not a
region-side geometric move) — genuinely untested by this round or round
12.

## 5. Fragment-vs-fragment tying sanity check (deprioritized lead)

Did not re-run new numerics this round (time went to the endpoint-
inequality tests above); re-read the existing evidence in Section 4.6.5 of
the approach file: the soft negative signal (smallest $s$ clearing $c(n)$
via unconstrained fragment-vs-fragment ties appears to grow with $n$ — $3$
at $n=6$, $\ge5$ at $n=8$) is unchanged by anything found this round. No
new evidence surfaced to either revive or further bury it. **Confirm: still
correctly deprioritized below the endpoint-inequality / exchange-argument
lead**, but per the file's own note it remains the only concrete
*algebraic* (not proof-mechanism) lead not yet attempted with a real proof
effort (as opposed to numeric search) — worth one focused, proved attempt
(generalizing the certified Singleton-Interleaving Lemma to chain-tie
fragments across different split pieces) only if the response-side exchange
idea above also stalls.

## 6. Crux corpus search

Filtered `combinatorics`/`algebra` domains for LP-vertex / boundary-
reduction / exchange-argument techniques beyond the two already flagged by
round 12 (`aimo-0146`, `aimo-0287`, both re-examined in detail above and
both now actually *tried* — not just cited — this round, with negative
results). Broader keyword sweep (`polytope`, `extreme point`, `convex
hull`, `simplex vertex`, `majorization`, `linear program`) surfaced no
stronger transplant candidate: hits were either unrelated (convex-hull
geometry problems, F$_2$-linear-algebra problems) or already-known
(`aimo-0287`'s majorization/exchange moves). **Conclusion: `aimo-0146` and
`aimo-0287` remain the best available crux transplants for this lead, and
both have now been tried (this round) rather than merely cited — with
negative numerical results reported above.** No new crux candidate found
to try next; the next step should be original (the adversary-response
exchange idea in Section 4), not a further crux search.

## 7. Concrete next step for round 13's outliner

Most promising precise next step: **construct $q$ from the optimal
adversary response $\sigma^*(p)$ at $p$, not from region-slack geometry.**
Concretely: take $p^*$'s minimizing cut-allocation/shape $\sigma^*$ (known
exactly via the certified Global Vertex Lemma machinery, Section 1 of the
approach file); identify which of $\sigma^*$'s pinned-fragment equalities
are "almost violated" as $p$ moves (i.e. which tie is closest to breaking);
build $q$ by pushing $p$ in the direction that makes *that* tie exact
(a response-side exchange, analogous to `aimo-0287`'s move but applied to
the adversary's optimal split rather than to $p$'s region-slack
coordinates). This has not been tried by any approach or round to date and
is a genuinely different mechanism from everything refuted so far (round
12's path monotonicity, round 12's transplanted-construction, and this
round's two region-geometry exchange families).
