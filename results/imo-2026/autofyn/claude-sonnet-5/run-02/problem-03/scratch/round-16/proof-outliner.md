# Round 16 outline: two revised-in-place fronts

No new top-level approaches opened this round. Per the orchestrator's
instruction, both `greedy-halving-adversary` and `lp-duality-certificate`
have concrete, non-exhausted next steps identified by this round's
explorers, so the field stays at two fronts, each revised in place.

---

## Front 1 — `greedy-halving-adversary` (revise in place)

### Where it stands
Round 15 (Proposition 30 + `upper-truncation-identity`) collapsed three
previously-separate-looking open items (item 1 ≡ item 2, the ℓ(F)=1 "v<s"
branch; item 3, the ℓ(F)=2/P≠∅/τ_P≥p_3 branch) into **one** precisely named
open quantity:

> **Target Q.** An upper bound on $A(R'_{>v})$, where $R'$ is an arbitrary
> legal $\le(n-2)$-cut refinement of the rescaled $(n-2)$-ladder tail
> $\{p_3,\dots,p_{n+1}\}$, and $v\in(0,s)$ is an arbitrary real threshold
> ($R'_{>v} := \{r\in R' : r>v\}$).

By `tail-self-similarity` this is scale-invariant: it is literally "bound
$A(S_{>v})$ for $S$ an arbitrary legal $(n-2)$-ladder response and $v$
arbitrary," recursively self-similar at every depth — which is exactly why
every induction-flavored attempt so far (peel-the-max, peel-the-min,
peel-by-$\ell(S)$, band-occupancy) has stalled: Target Q needs an *upper*
bound on a reduced instance, but the population's only tools produce
*lower* bounds ($L(n-k)$-type statements).

### Confirmed dead ends — do NOT re-attempt this round
(All independently re-verified by the round-16 truncation-bound explorer;
listed here so the builder does not re-spend budget re-deriving them.)

1. `max-domination-lemma` alone ($A(S)\le\max(S)$): substituting
   $A(R'_{>v})\le\max(R')\le s$ back into Proposition 30's target makes
   the resulting bound **go negative** for small $v$ — computed explicitly,
   not just asserted.
2. `triangle-bound-for-a` + `max-domination-lemma` combined ("Target B"
   from round 15): refuted by direct computation; ~92% failure rate on
   random trials, and where it doesn't outright fail the margin is
   razor-thin (0.002–0.14×f(n) at $n=3,4$), not the "generous 17×f(n)
   slack" an earlier outline assumed. Whatever closes Target Q must be
   close to sharp, not slack-absorbing.
3. `ratio-2-spacing-lemma` / `last-element-bound`: proven, in two
   independent rounds (13 and this round's explorer), **not to transfer**
   — their proofs need the raw, untouched ratio-2 spacing of an *unrefined*
   ladder sequence; $R'_{>v}$'s elements are already-cut fragments, which
   need not satisfy that spacing at all. Do not attempt a "fix" that tries
   to force this transfer; it is a structural mismatch, not a missing
   epsilon.
4. Peel-induction on $\ell(S)$ or on multiset size, naive whole-mass
   bounds, binary-digit/carry transplants, fixed-ratio bijective pairing:
   all already on the run's permanent "never retry" list from earlier
   rounds (Parity Coincidence Lemma; `integer-lattice-reduction`;
   `bijective-mersenne-pairing`).

### This round's target: direct vertex/LP-extremal characterization of Target Q

Per the round-16 truncation-bound explorer's top recommendation (candidate
(a)): attack $\max_S A(S_{>v})$ **directly as an extremal/vertex
enumeration problem**, not via an inductive lower-bound composition. This
is modeled on the one confirmed instance in this project's own history of
breaking an identical "only lower-bound machinery available" plateau: the
round 5→6 transition, where `lp-duality-certificate`'s vertex/LP framing
(not a sharper induction) broke a 4-round stall on $(\star\star)$.

**Concrete plan for the builder:**

1. Treat $S \mapsto A(S_{>v})$ as a functional over the compact polytope of
   legal $(n-2)$-ladder responses $S$ (fixed threshold $v$; if useful, also
   let $v$ range over a finite set of "tie-adjacent" candidate values, since
   the polytope's combinatorics only change at tie points).
2. Apply the already-certified **`vertex-minimum-theorem`** (proved with no
   ladder-specific assumption baked into its *argument structure*, only its
   application) to conclude the maximum of this functional over the legal
   polytope is attained at a vertex — a point pinned by finitely many
   "fragment = 0" / "fragment = fragment" tie constraints — exactly as it
   already does for $A(S)$ itself. **New work required, not a citation:**
   the existing vertex enumerations on file
   (`per-piece-vertex-decomposition-theorem`, `rank-tie-vertex-reduction`)
   were built for $A(S)$ or $A(F\cup G)$, i.e. functionals of the *whole*
   multiset — not for $A(S_{>v})$, a functional of a *threshold-truncated
   sub-object*. The builder must show (or find a genuine obstruction to)
   the same vertex-attainment argument transplants to a truncated
   functional: does restricting to $\{r>v\}$ preserve
   piecewise-linearity/convexity in the fragment coordinates needed for the
   standard LP-vertex argument, or does the truncation introduce a
   non-convex kink at $r=v$ that breaks the argument? This is the first
   thing to nail down, honestly, before enumerating anything.
3. If the vertex-attainment step transplants: use the already-certified
   **`odd-run-reduction-lemma`** to evaluate $A(S_{>v})$ in closed form at
   each vertex type (it already handles closed-form evaluation at any
   tie-vertex, including simultaneous multi-way ties — exactly the tool
   needed once the search is reduced to a finite vertex family).
4. Enumerate the resulting (hopefully small, since $v$-truncation is an
   extra constraint on top of the legal-refinement polytope) vertex family
   for small $n$ first ($n=3,4$, i.e. the rescaled $(n-2)$-ladder at
   $n-2=1,2$) to get a concrete closed-form or numeric ceiling on
   $\max A(S_{>v})$, then attempt to generalize.
5. Report honestly whatever is found: a genuine closed-form bound on Target
   Q (best case), a partial vertex characterization with the enumeration
   left open for larger $n$ (expected/acceptable partial progress, matching
   the project's usual granularity), or a rigorous demonstration that the
   truncation breaks vertex-attainment (an honest negative result,
   valuable in itself since it would redirect the whole front).

**Explicitly out of scope this round** (per the explorer's report, flagged
as secondary/more speculative): candidate (b), differentiating $v\mapsto
A(S_{>v})$ as a step function and bounding its total variation via the
*unrefined* piece-boundary ratio-2 structure. Worth a time-boxed side
attempt only if the builder has slack after (a), since it is a genuinely
different lever (reuses `cross-term-identity-threshold` /
`general-ladder-dominance` in a new combination) and diversifies within the
front — but (a) is the primary target and should get the bulk of the
budget. Do not spend time on candidate (c) (recursing
`upper-truncation-identity` on $R'$ itself) alone — round 15 already
correctly diagnosed this as relabeling the same problem one level down, not
progress, unless it's used as a supporting step inside (a) or (b).

**Build set entry:** `greedy-halving-adversary`, target = vertex/LP-extremal
characterization of $\max A(S_{>v})$ (Target Q), reusing
`vertex-minimum-theorem` + `odd-run-reduction-lemma`; explicit non-goals
listed above must not be re-attempted.

---

## Front 2 — `lp-duality-certificate` (revise in place)

### Where it stands
Open Gap 1 (general upper bound $c(n)\le a_n$ for arbitrary markings) is
closed for case (a) (conditional) and case (b1) (unconditional, Max
Domination Lemma corollary). **Case (b2)** ($p_1<T/2$,
$T/D_n<p_2<a_nT/2$) remains open. Round 15 built the Cross-Piece
Sign-Assignment Identity and the Alternating Gap-Cross Lemma; the latter
has a confirmed sign bug (root cause: the tail prefactor must be
$(-1)^{j'}$ where $j'$ counts *actually-split* pairs, not $(-1)^j$ over
*all* pairs $j$ — verified independently by this round's case-(b2) explorer
by hand on two examples, including the on-file $(45,45,31,27)$
counterexample).

### Task 1 — fix the sign bug (hygiene, cheap, do first, do not overinvest)
Re-derive `alternating-gap-cross-lemma` with the correct prefactor
$(-1)^{j'}$, $j' = |\{i\le j : p_{2i-1}>p_{2i}\}|$ (count of pairs actually
split, not all pairs). This is essentially a copy-paste re-derivation of
`cross-piece-sign-assignment-identity`'s own Step 2 rank-count bookkeeping,
not new mathematics — the explorer independently confirmed the buggy
$(-1)^j$ version agrees with the correct one exactly when $j'\equiv
j\pmod2$ (even number of untouched/equal pairs), so the previously-reported
numerics (which happened to sample mostly that sub-case) are not
retroactively invalidated, just imprecisely justified. Re-verify with a
fresh exact-`Fraction` script including deliberately-constructed cases with
an *odd* count of equal pairs (the sub-population the bug actually
affects) — prior verification scripts likely under-sampled this case.
**Explicitly do not expect this to move case (b2)'s numeric coverage** —
three independent reasons (feasibility test unaffected by the sign;
already-negligible affected sub-population is measure-zero under generic
sampling; the whole family is bottlenecked by the same crude
max-domination tail bound as Bisect-Top-$k$, already at ~0% marginal
coverage at $n=4,5$) all converge on this being a certification-hygiene
fix, not a coverage expansion. Certify the corrected lemma and move on —
do not spend further rounds tuning this specific family.

### Task 2 (primary target) — mechanism (A): recursive-image escape argument
The real effort should go here. **Claim to investigate:** a marking in
case (b2) at level $n$, after one step of the already-certified Theorem
C′/B$_k$ recursive identity (peel or bisect $p_1$, recurse on the
$(m-1)$-piece tail), generically lands in case (a) or case (b1) **one
level down** ($n-1$), even though the top-level marking itself sits in
case (b2). This is structurally different from every mechanism tried so
far: prior attempts all bound $A(\text{tail})$ or $\Phi(\text{tail})$
crudely in one shot; this instead asks where the recursion's *image*
lands, reusing the already-proved, unconditional, general-$n$
`telescoping-threshold-identity` ($a_{n-1}=a_n/(2(1-a_n))$) for the
threshold algebra.

**Why there is real room here (not just hope):** case (b2) at level $n$ is
defined purely in terms of $p_1,p_2,T$ ($T/D_n<p_2<a_nT/2$). After one
Theorem-C′ step, the new "level $n-1$" instance's own case membership is
governed by the *new* $p_2$ — which is the *original* $p_3$ — against a
*different* threshold ($a_{n-1}T'/2$ where $T'=T-p_1<T$, and $a_{n-1}<a_n$
since $a_k$ is increasing). Case (b2)'s defining window says nothing about
$p_3$ at all, so there is no a priori reason the recursive image must stay
in case (b2) — the two conditions live on genuinely different variables.

**Mandatory first step before any proof attempt (cheap, ~1 script,
required per the explorer's recommendation and the orchestrator's
diversity-of-effort concern):** run a numeric diagnostic — for random
case-(b2) markings at $n=4,5$, compute whether the recursive image after
one Theorem-C′/B$_k$ step lands in case (a), (b1), or stays in (b2) one
level down. This is a fast falsifiability check with three possible honest
outcomes, each of which tells the next step what to do:
- **Generically escapes (strong majority land in (a)/(b1)):** proceed to
  look for the two-line "cannot satisfy case-(b2)'s inequality at two
  consecutive levels for generic reasons" monovariant argument the explorer
  flagged as the promising shape (the window width $(T/D_n, a_nT/2)$
  scales geometrically with $n$; look for a clean algebraic reason the
  *same* marking's $p_2,p_3$ can't both sit inside their respective windows
  simultaneously).
- **A nonempty adversarial family stays in (b2) at every level:** this is
  itself a valuable, honestly-reportable *negative* result (symmetric to
  how the certified `half-window-vanishing-lemma` broke a plateau by
  finding the exact structural reason a window vanishes) — narrows the
  problem to exactly that family rather than leaving case (b2) an
  unstructured blob, and should be written up as such rather than treated
  as a failed round.
- **Mixed / no clean pattern:** report the diagnostic honestly and fall
  back to Task 3 below for this round, deferring the escape argument to a
  future round with a sharper numeric picture.

**Explicit non-goal:** do not claim a proof of "case (b2) escapes
generically" from numerics alone — a full proof needs either (i) the
monovariant argument above, or (ii) the explicit adversarial-family
negative result; either is acceptable output for the round, numerics alone
are not (per the project's own rigor rules on conjecture vs. proof).

### Task 3 (fallback only, if Task 2 stalls) — mechanism (B): exact vertex enumeration in case (b2)'s box for small $n$
Per the explorer's lower-confidence secondary candidate: run the **exact**
finite vertex enumeration of the already-certified
`per-piece-vertex-decomposition-theorem`'s joint vertex family, restricted
to markings satisfying case (b2)'s box constraints specifically (not the
whole simplex, which round 11/12 already showed times out / has no
tail-agnostic closure), for small fixed $m$ (e.g. $n=3,4$). Because the box
is lower-dimensional and bounded, the vertex family may be small enough to
enumerate exhaustively and check against $a_nT$ by direct algebra. This
does not resolve the R11.5/R12.5-diagnosed general obstruction (no
tail-structure-agnostic replacement for `ratio-2-spacing-lemma`/
`last-element-bound`), but could convert "case (b2) genuinely open" into
"case (b2) closed for $n\le4$, open for larger $n$" — a real, if narrow,
narrowing in the same spirit as the project's existing $n\le3$/$n\le4$
partial closures elsewhere. Only pursue this if Task 2's diagnostic comes
back mixed/inconclusive or the escape argument proof stalls mid-round;
otherwise Task 2 is the priority use of build budget.

**Build set entry:** `lp-duality-certificate`, targets = (1) sign-bug fix
and certification of `alternating-gap-cross-lemma` [cheap, do first], (2)
primary: case-(b2) recursive-image escape argument via
`telescoping-threshold-identity` + Theorem C′/B$_k$, starting with the
mandatory numeric diagnostic, (3) fallback only: exact vertex enumeration
restricted to case (b2)'s box for $n=3,4$.

---

## Build set (both slugs)

- `greedy-halving-adversary` — vertex/LP-extremal characterization of
  $\max A(S_{>v})$ (Target Q), per Front 1 above.
- `lp-duality-certificate` — sign-bug fix + case-(b2) recursive-image
  escape argument (primary), exact small-$n$ vertex enumeration (fallback),
  per Front 2 above.

No new approaches opened this round; both fronts have concrete,
non-exhausted next steps per this round's two explorer reports, so the
"open a genuinely different framing" rule is not triggered this round.
