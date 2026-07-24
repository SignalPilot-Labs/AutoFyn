## imo-2026-03

### Reconciliation note (read before builders touch greedy-halving-adversary)

The two round-32 explorers disagree about the vertex "$c=t\in S''$, Case
(ii): $q_2$ untouched in $S''$, $t\ne q_2$" of `greedy-halving-adversary`'s
$h(m)$ residual. Verdict after tracing both reports' actual arguments:
**`math-explorer-punctured-maxceil.md` is correct and should be followed.**
It is the only report that actually did the algebra for this *specific*
vertex; `math-explorer-maxceil5.md`'s "genuinely different, harder, untouched
object" characterization is a general pattern-matching caution (correctly
warning not to assume *all* "punctured tail" objects are cheap) but was
written without checking this vertex's specific slack, and does not
contradict the punctured-maxceil explorer's derivation once traced:

- The object is $A(S''\setminus\{t,q_2\})$ where $S''\setminus\{q_2\}$ is a
  legal refinement of the ratio-2 tail $\{q_3,\dots,q_{m+1}\}$ (length
  $m-1$), and $t$ is one further point removed.
- Mass is refinement-invariant: $\mathrm{Total}(S''\setminus\{q_2\}) =
  \mathrm{Total}(\{q_3,\dots,q_{m+1}\}) = 2q_3-q_{m+1} = q_2-f(m)$ exactly
  (ladder telescoping identity, same pattern already used one index up for
  $q_1-\mathrm{Total}(S'')=f(m)$ in Theorem 42's proof — not a new lemma,
  a shifted-index re-derivation).
- Removing $t>0$ strictly decreases mass: $\mathrm{Total}(S''\setminus
  \{t,q_2\}) = (q_2-f(m))-t < q_2-f(m)$.
- By the elementary fact $A(S)\le\mathrm{Total}(S)$ (Fact 2, already used
  informally in `rank-pigeonhole-budget.md` §5.2 but never extracted as a
  standalone lemma file), $A(S''\setminus\{t,q_2\}) \le \mathrm{Total}
  (S''\setminus\{t,q_2\}) < q_2-f(m)$ — proving $(\dagger)$ with strict
  slack $t$, for **every** $m\ge3$, unconditionally, no case split on
  whether $t$ is a whole rung or a split fragment, no restriction on cut
  count, and **no dependence on $\mathrm{MaxCeil}(m\ge5)$ or the Necessity
  Theorem**.
- This is genuinely a *different, easier* vertex than Case (i)'s "split-rung
  fragment removed" sub-case, which targets the *tight* bound $q_3-f(m)$
  (no factor-2 slack, since the dominant peel there is only $q_3$, not
  $q_2=2q_3$) and correctly does reduce to $\mathrm{MaxCeil}(m-1)$ — that
  one remains open for $m\ge6$ and is untouched by this closure. The two
  "punctured" objects only *look* similar; do not conflate them.

Conclusion for the outline below: close Case (ii) via the elementary
Fact-2/mass-conservation argument (cheap, no vertex enumeration needed);
leave Case (i)'s split-rung sub-case and the shared $c=x\equiv
\mathrm{MaxCeil}(m\ge5)$ vertex exactly as previously scoped.

---

greedy-halving-adversary: revise
Target: $c(n) = 2^n/(2^{n+1}-1)$ for every $n$ (the whole problem), via the
combinatorial reduction $c(n)=\max_{\text{marking}}\min_{\text{response}}
A(S)$.
Technique: strong induction on $n$ via the certified Vertex-Minimum Theorem
+ exchange-smoothing, decomposing Xiang Yu's response into $h(m)$'s named
sub-cases (untouched top, single cut on $q_1$/tail untouched, simultaneous
$q_1$-cut and tail refinement).
Skeleton:
  1. Restate $(\dagger)$: Case (ii) of vertex $c=t\in S''$ ("$q_2$ untouched
     in $S''$, $t\ne q_2$") reduces via `sharp-dominant-removal-identity`
     (since $q_2$ strictly dominates the rest of $S''$) to
     $A(S''\setminus\{t,q_2\}) \le q_2-f(m)$ — by the reconciliation above.
  2. Extract and certify **Fact 2** ($A(S)\le\mathrm{Total}(S)$, any finite
     multiset $S$) as a standalone lemma file (it is used informally in
     `rank-pigeonhole-budget.md` §5.2 and is about to be reused across
     files by name) — proof: group $S$'s sorted elements into consecutive
     pairs, each pair contributes $\ge0$ to the alternating sum being
     $\le$ the pair's own total, telescoping to $A(S)\le\mathrm{Total}(S)$.
  3. Re-derive the shifted-index ladder telescoping identity
     $\mathrm{Total}(\{q_3,\dots,q_{m+1}\}) = q_2-f(m)$ (same mechanism as
     Theorem 42's $q_1-\mathrm{Total}(S'')=f(m)$, one index down) — by
     $\sigma_1=2\sigma_2$ recursion applied to the tail starting at $q_3$.
  4. Combine: mass conservation under refinement gives
     $\mathrm{Total}(S''\setminus\{q_2\})=q_2-f(m)$ for *any* legal
     refinement (any cut count), and removing $t>0$ strictly decreases
     it; apply Fact 2 to close $(\dagger)$ for every $m\ge3$,
     unconditionally.
  5. Update the $h(m)$ residual bookkeeping: after this closure, the
     "simultaneous $q_1$-cut and tail-refinement" piece of $h(m)$ has only
     two vertices open — $c=x$ for $m\ge5$ (identical, term-for-term, to
     `rank-pigeonhole-budget`'s $\mathrm{MaxCeil}(m\ge5)$'s $c=x$ vertex —
     do NOT re-derive, cite the sibling directly and coordinate) and Case
     (i)'s "split-rung fragment removed" sub-case ($\equiv\mathrm{MaxCeil}
     (m-1)$, open for $m\ge6$).
  6. Check explicitly whether $h(3)$'s entire "simultaneous-cuts" piece is
     now fully closed: at $m=3$, the $c=x$ vertex needs only
     $\mathrm{MaxCeil}(3)$ (already certified, round 26) and the split-rung
     sub-case needs only $\mathrm{MaxCeil}(2)$-level facts (also within
     certified range) — if both check out, $h(3)$ is fully closed this
     round, a concrete near-term win worth confirming with an explicit
     computation, not just citing the pattern.
Key lemmas (claim + mechanism):
  - Fact 2, $A(S)\le\mathrm{Total}(S)$ — because grouping any sorted
    multiset into consecutive pairs bounds the alternating sum by the
    total (each pair's odd-rank element is $\le$ the pair's sum).
  - Shifted ladder telescoping identity $\mathrm{Total}(\text{tail from }
    q_3) = q_2-f(m)$ — because the ratio-2 recursion $\sigma_1=2\sigma_2$
    telescopes exactly the same way one index down as it does at the top.
Open gaps: after step 6, $c=x$ ($m\ge5$) and Case (i)'s split-rung
sub-case ($m\ge6$) remain open; both are shared/entangled with
`rank-pigeonhole-budget`'s $\mathrm{MaxCeil}(m\ge5)$ — coordinate, do not
duplicate.
Cases to cover: $m=3$ boundary check (step 6) must be verified explicitly,
not assumed from the pattern of earlier boundary checks.
Watch out for: do NOT attempt $(\dagger)$ via $\mathrm{MaxCeil}(m-1)$
itself (re-deriving the tight bound first) — the Fact-2/mass argument
bypasses that entirely; do NOT conflate Case (ii) (this round's closure)
with Case (i)'s split-rung sub-case (different slack, different fate,
genuinely needs $\mathrm{MaxCeil}(m-1)$).

---

lp-duality-certificate: revise
Target: general-$n$ upper bound $c(n)\le a_nT$ for arbitrary Liu Bang
markings (this round's instance: $n=4$).
Technique: Farkas-style exhaustive finite-chamber covering (per-branch
nonnegative-combination infeasibility certificates), transplanting the
already-solved $n=3$ case-(b2) precedent
(`lemmas/case-b2-n3-covering-closure.md`) to the residual box
$\mathcal R' = \{p_2\le p_1<15T/31,\ T/31<p_2<8T/31\}$.
Skeleton:
  1. Restate the $n=3$ case-(b2) template precisely: 5 named chambers +
     an exhaustive branch case-split (on the relative order/size of the
     pieces and which chamber's formula is smallest) + a Farkas-style
     nonnegative-linear-combination certificate per branch proving
     $\Phi\le a_3T$ is implied by that branch's defining inequalities,
     with zero numerics in the final proof.
  2. Assemble $\mathcal R'$'s chamber family from what's already certified:
     every named $n=4$ chamber (Half-Complement Pin, Double-Bisect-Pin,
     Triple-Pin, Double-Pin-Pair) is an instance of the general
     `partition-chamber-theorem` — no new chamber *shape* is needed, only
     the existing instances plus (optionally) new instances from step 3.
  3. If step 2's family leaves gaps in the exhaustive branch case-split
     (i.e. some region of $\mathcal R'$ has no branch where a chamber's
     Farkas certificate closes), derive the "leave-2-untouched" 3-element
     extension of Half-Complement Pin (host $q_1$ pinned against all but
     two pieces $j,k$, leaving $Q=\{\rho,q_j,q_k\}$ with an explicit
     3-way case split on which of $\rho,q_j,q_k$ is largest/smallest) —
     this is already covered in principle by `partition-chamber-theorem`
     but its closed form and feasibility region are not yet worked out.
  4. For each branch of the case-split, write the Farkas certificate:
     express $a_4T-\Phi_{\text{chamber}}\ge0$ as a nonnegative combination
     of the branch's defining linear inequalities (mirroring the exact
     bookkeeping style of `case-b2-n3-covering-closure.md`).
  5. Prove the branch case-split is exhaustive over $\mathcal R'$ (every
     point of the box satisfies at least one branch's hypotheses) —
     this must be an explicit logical argument (e.g. by the ordering of
     finitely many linear thresholds), not a sampling check.
Key lemmas (claim + mechanism):
  - Leave-2-untouched closed form (new, to derive): $\Phi = $ explicit
    3-case formula on $Q=\{\rho,q_j,q_k\}$ — because it is
    `partition-chamber-theorem` instantiated with 2 untouched singletons,
    and $A(Q)$ on a 3-element set has exactly 3 orderings.
  - Farkas certificate per branch — because $a_4T-\Phi$ is an affine
    function of the free coordinates on each branch's polytope, and
    nonnegativity on a polytope defined by finitely many linear
    inequalities is exactly a nonnegative-combination (Farkas) fact —
    the same mechanism `case-b2-n3-covering-closure.md` already used.
Open gaps: the exhaustive branch case-split for $\mathcal R'$ is not yet
written; the leave-2-untouched closed form is not yet derived.
Cases to cover: at minimum, the known tight witnesses $p_1/T\approx0.379$
(Triple-Pin) and $p_1/T\approx0.467$ (Double-Pin-Pair) must each land
inside a named branch with a valid certificate — use these as the first
sanity checks on any proposed branch case-split.
Watch out for: the cut-budget bug the explorer caught — any chamber
formula must respect $\le n=4$ cuts over 5 pieces (e.g. "bisect all 5
pieces" needs 5 cuts and is illegal); enforce this explicitly in every
branch definition, not just numerically. Numeric-only "100% coverage" is
NOT sufficient — this exact residual has already produced two false
coverage claims (rounds 29-30) that an adversarial exact-fraction search
later refuted; require an actual Farkas certificate before reporting
closure.

---

rank-pigeonhole-budget: revise
Target: general-$n$ lower bound via $\mathrm{MaxCeil}(m)$/$(\star_k)$
family (this round's instance: $\mathrm{MaxCeil}(5)$).
Technique: (a) free corollary write-up via the certified §7.10.4
untouched-top reduction + $(\star_3)=\mathrm{MinFloor}(4)$'s round-31 full
closure; (b) vertex-enumeration (same toolbox that closed $(\star_3)$) on
$\mathrm{MaxCeil}(5)$'s top-cut, $\sigma_2$-touched residual, now with
$(\star_3)$ available as a positive ingredient.
Skeleton:
  1. Promote §7.10.4's "untouched-top branch $\equiv \mathrm{MinFloor}
     (\ell-1)$" reduction to a standalone certified lemma, stated for
     general $\ell$ (its only blocker — $\mathrm{MinFloor}$ being only
     partially closed — is now gone since $(\star_3)=\mathrm{MinFloor}(4)$
     closed in round 31).
  2. Instantiate at $\ell=5$: $\mathrm{MaxCeil}(5)$'s top-untouched branch
     $\equiv \mathrm{MinFloor}(4) = (\star_3)$, already fully proved (both
     directions, all 20 shapes) — this closes half of $\mathrm{MaxCeil}(5)$
     essentially for free; write this up explicitly rather than leaving it
     implicit.
  3. For the harder half — the top-cut branch's $\sigma_2$-touched
     residual (§7.15's subject) — enumerate its legal shapes: $\le
     (m-2)=3$ cuts over 5 pieces $(\sigma_1,\dots,\sigma_5)$ with $\sigma_1$
     necessarily cut and $\sigma_2$ necessarily touched, the same style of
     census that produced $(\star_3)$'s 20 maximal shapes.
  4. Close each shape via the same toolbox: `vertex-minimum-theorem` +
     `odd-run-reduction-lemma` + `sharp-dominant-removal-identity` +
     `pair-insertion-ordering-lemma` + Fact 2 — and for any shape whose
     reduction lands on a length-4 ratio-2 tail one level down, use
     $(\star_3)=\mathrm{MinFloor}(4)$'s certified 20-shape result directly
     as a positive tool (not merely as a satisfied necessary condition per
     the Necessity Theorem).
  5. Do NOT re-attempt the "cheap two-peel + Fact 2" route directly on
     (7.15.1) itself — the Necessity Theorem already proves this reduces
     algebraically to $z_1\ge\sigma_2$, false for any genuine split; any
     new mechanism here must be different from what closed
     $\sigma_2$-untouched and $\mathrm{MaxCeil}(3)/(4)$.
Key lemmas (claim + mechanism):
  - §7.10.4 general-$\ell$ untouched-top reduction — because
    `sharp-dominant-removal-identity` applied to $\sigma_1$ (which
    strictly dominates the untouched-top-branch's remaining mass)
    converts $A(\text{top-untouched shape})$ into $\sigma_1-A(\text{rest})$,
    which is exactly $\mathrm{MinFloor}(\ell-1)$'s target restated.
  - $\mathrm{MaxCeil}(5)$ top-untouched branch = $(\star_3)$ — because the
    reduction above at $\ell=5$ lands exactly on $\mathrm{MinFloor}(4)$,
    which is fully proved.
Open gaps: the $\sigma_2$-touched residual's shape census (step 3) is not
yet enumerated; individual shapes not yet closed. This is genuinely
entangled with `greedy-halving-adversary`'s $h(5)$'s $c=x$ vertex (same
object) — coordinate, do not duplicate that specific piece.
Cases to cover: the full shape enumeration for $\le3$-cut, $\sigma_1$-cut,
$\sigma_2$-touched configurations over 5 pieces — expect this to be
larger than $(\star_3)$'s 20-shape census (more pieces, comparable
budget); budget builder time accordingly, and it is acceptable to leave
some shapes open this round if honestly reported.
Watch out for: the Necessity Theorem is one-directional (necessity, not
sufficiency) — satisfying its necessary condition (now guaranteed by
$(\star_3)$'s closure) does NOT itself close the residual; a genuinely new
sufficiency argument is still required for the general (non-$\varepsilon
\to0$) $\sigma_2$-touched case.
