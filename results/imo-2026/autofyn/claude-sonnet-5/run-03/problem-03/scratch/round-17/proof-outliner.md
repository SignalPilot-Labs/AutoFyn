## imo-2026-03

self-similar-induction-on-n: revise
Target: the problem's actual claim (Alice can guarantee $c(n)$; equivalently
$\mathrm{OddSum}(M)\ge c(n)$ for every legal adversary partition $p$ and every
legal response — this approach attacks the **lower-bound** direction via
GT($m$), the General Theorem that $\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge
\min(\mathrm{sum}(D),2^m)$ for every finite $D$, $|D|\le m+1$, $\max(D)\le2^m$).
Technique: strong induction on $m$, case split on $p:=\#\{a_i\in D:a_i>2^{m-1}\}$;
the residual sub-case (i) ($p=1$, called $q=1$ one level down, excess
$e:=m-k\ge1$) needs a chained peeling identity down $e$ levels.
Skeleton:
  1. **Re-verify the scope correction before anything else.** Confirm (as
     round 17's explorer did, and as I independently re-checked against the
     approach file's own boxed GT($m$) statement, lines ~3232-3237: hypothesis
     is $|D|\le m+1$) that round 16's refuting counterexample
     ($k=1,e=1,m=2$, $|D|=5>m+1=3$) is **out of GT($m$)'s own scope** — it
     refutes only round 16's over-generalized, count-unrestricted restatement
     of Step 0, not GT($m$) sub-case (i) itself. State this correction
     explicitly in the file before reproving anything (do not silently
     re-open a claim current.md calls "false" without first pinning down
     exactly what was false).
  2. **Adopt the coupled (OddSum,EvenSum) single-step alternation**, not the
     "Odd stays Odd" telescoping that failed in round 16. Writing
     $O_j:=\mathrm{OddSum}(D\cup\Gamma_{j-1})$, $E_j:=\mathrm{EvenSum}(D\cup
     \Gamma_{j-1})$: prove, directly from the certified $q=0$ clause of the
     Unified Threshold-Pair-Peeling Lemma
     (`lemmas/monotonicity-reduction-and-unified-threshold-pair-peeling.md`),
     the two single-step identities $O_j=2^{j-1}+E_{j-1}$ and $E_j=O_{j-1}$
     (valid whenever $\max(D)\le2^{j-1}$, i.e. $q=0$ at level $j$ alone).
  3. Chain these $e$ times from level $m$ down to level $k$ (valid throughout
     since $\max(D)=a_1\le2^k\le2^{j-1}$ for every $j\ge k+1$ in sub-case (i)
     by hypothesis), terminating at level $k$ with the companion pair
     $O_k=a_1+\mathrm{OddSum}(R\cup\Gamma_{k-2})$ (already certified) and the
     **new Even-target twin** $E_k=\mathrm{OddSum}(R\cup\Gamma_{k-1})$ (derive
     this from the general Rank-Shift Identity's $q=1$-odd-branch statement
     applied to the Even target — the explorer found this needs no new
     machinery, only applying an already-general certified lemma to a target
     it already covers).
  4. Prove the **Even-target Large-Sum Closure Theorem**: whenever
     $\mathrm{sum}(R)=2^m-a_1$ with $a_1\in(2^{k-1},2^k]$ (the width-1 window
     included), $\mathrm{OddSum}(R\cup\Gamma_{k-1})\ge2^k-a_1$ — the twin of
     the already-certified Odd-target Large-Sum Closure Theorem, by the same
     Half-Sum-Corollary technique
     (`lemmas/half-sum-corollary-and-large-sum-closure-theorem.md`).
  5. **Prove (not just numerically confirm) the telescoped-sum-vs-target
     inequality**: expand the $e$-fold chain explicitly as a sum of $2^{j-1}$
     terms for $j=k+1,\dots,m$ (which the explorer confirmed numerically
     telescopes to exactly $2^m-2^k$, not a "$2/3$-shortfall" — that was the
     explorer's own dead-end mis-framing, now corrected) plus the level-$k$
     base term ($O_k$ or $E_k$ depending on the parity of $e$), and show the
     total meets $\min(\mathrm{sum}(D),2^m)=2^m$ (since $\mathrm{sum}(D)=2^m$
     is the forced value along a pure $q=0$ chain). This is the one genuinely
     new algebraic step — write it as an explicit closed-form sum, not left
     as "numerically confirmed."
  6. Combine with the already-certified $p=2$ (Lemma P2, closes in one step)
     and $q\ge2$ (Rank-Shift Identity, certified) cases to conclude GT($m$)
     sub-case (i) is closed for every $k\ge1,e\ge1,a_1\in(2^{k-1},2^k]$,
     hence — modulo `Case-B(m,k)`'s own still-open $e=0$ sliver — advances
     $\mathrm{GT}(m)$ toward full closure for $m\ge4$.
Key lemmas (claim + mechanism):
  - Coupled single-step alternation ($O_j=2^{j-1}+E_{j-1}$, $E_j=O_{j-1}$) —
    because peeling the top (an odd global rank) of $D\cup\Gamma_{j-1}$ both
    contributes $2^{j-1}$ to Odd and converts the companion Even quantity one
    level down via the Companion Peeling Lemma; already certified machinery,
    just applied as a genuinely coupled pair instead of collapsed to one
    quantity.
  - Even-target Large-Sum Closure Theorem — because the same Half-Sum
    Corollary argument ($\mathrm{OddSum}(N)\ge\mathrm{sum}(N)/2$) that closed
    the Odd-target case applies verbatim to the Even target once $E_k$ is
    rewritten as an OddSum via the Rank-Shift Identity's $q=1$ branch.
  - Telescoped-sum identity sums to exactly $2^m-2^k$ — because each of the
    $e$ single alternation steps contributes its own $2^{j-1}$ term (no term
    is skipped by tracking the coupled pair correctly), recovering the full
    geometric sum $2^{m-1}+\cdots+2^k$.
Open gaps: step 5 (the explicit closed-form telescoped-sum-vs-target proof,
covering both $e$-even and $e$-odd termination cases) is the only remaining
unproved step; step 4 (Even-target twin) is a short mechanical adaptation not
yet written up. Both are precisely scoped per the explorer's report.
Cases to cover: parity of $e$ (terminates needing $O_k$ if $e$ even, $E_k$ if
$e$ odd) — both companion formulas must be stated and used.
Watch out for: (a) do not silently let $|D|$ grow past $m+1$ anywhere in the
chain — GT($m$)'s cap must be threaded through explicitly, not just checked
numerically; (b) do not repeat round 16's mistake of collapsing the coupled
(O,E) pair into a single self-recursive O-only relation; (c) the width-1
window's own boundary ($a_1\to2^{k-1}$ or $e=0$) is where the margin is near
zero (explorer found margin $\approx0.004$) — the builder must show the
algebra gives $\ge0$ there, not just "large slack" as claimed for other $e$.

global-lp-vertex-sufficiency: revise
Target: the problem's actual claim, upper-bound direction — for every legal
adversary partition $p$ in the balanced region, some legal response achieves
$\mathrm{OddSum}(M)\le c(n)$ (equivalently: the LP-vertex maximizer $V(p)$ of
the adversary's best defense never exceeds $c(n)$), via finite candidate-vertex
enumeration.
Technique: LP/compactness (existence of maximizer) + finite-cell affine-vertex
reduction (already certified) reducing the residual "$\Sigma$-shape" candidate
set $Q$ to a classification problem; this round's new mechanism is an
extremal-selection exchange argument adapted from crux `aimo-0119`.
Skeleton:
  1. **Cheap kill first** (mandatory, per project rule): before any proof
     investment, numerically test whether "the OddSum-minimizing legal
     response, tie-broken by fewest tied fragments, is stable under a
     single-fragment transfer from the largest tied group toward the
     smallest" (the aimo-0119-style extremal-selection + non-improvement
     mechanism) at the already-catalogued hard $n=3,4$ points (Section 7).
     If it fails outright, record as a fifth refuted mechanism and stop; if
     it survives, proceed to step 2.
  2. **First classify each hard point via the sweep-for-flatness test**
     (this round's genuinely new diagnostic finding): for each catalogued
     hard point, sweep the free split parameter within the winning cut
     allocation and check whether the within-branch tie is a sharp kink
     (width $\sim10^{-6}$, "Self-Bisection-Crossover" type) or a wide flat
     interval (width $\gg10^{-6}$, "Flat-Edge" type) — classify all 8
     catalogued points before writing any proof narrative, since the two
     phenomena need different top-level targets.
  3. **For Self-Bisection-Crossover points**: formalize the joint object —
     a piece bisecting itself exactly in half AND that bisection value
     coinciding with a rank-order crossover against a neighboring fragment
     — as two simultaneous equations (discrete branch choice + continuous
     tie value), and attempt the aimo-0119 exchange argument to pin down
     when this is forced to be the extremal shape.
  4. **For Flat-Edge points**: reframe the target — the true optimum may sit
     at an **endpoint of a continuum of tied optimal shapes**, not at an
     isolated vertex. Test in exact `Fraction` arithmetic (not float
     optimizer) whether hard point 1's maximizer status holds exactly at
     one of the flat edge's two endpoints (where the edge meets a third
     constraint) — this is a different formal object (a degenerate LP basis
     / face of $Q$, not a $0$-dimensional vertex) and needs its own
     existence-of-endpoint-attainment argument, not the vertex-enumeration
     machinery as currently stated.
  5. Filter out Zero-Removal-explained pseudo-ties (via the certified
     Zero-Removal Invariance Lemma) before counting "how many genuinely
     distinct branches tie" at any point — do not let a padded near-tie
     count as new phenomenology.
Key lemmas (claim + mechanism):
  - Self-Bisection-Crossover is a genuinely new joint mechanism, structurally
    different from all 4 refuted tie-topologies — because those tie
    fragments of two *different* pieces, while this ties a piece to *itself*
    at a value that is *also* a rank-order boundary; two coupled conditions,
    not a single construction family.
  - Flat-Edge points correspond to a degenerate LP basis (multiple optimal
    bases) at that cell — because a continuum of $x$ values re-optimizing a
    partner fragment attains the identical minimal value, which is exactly
    the LP-theoretic definition of basis degeneracy, not vertex collision.
Open gaps: everything beyond step 1's cheap-kill and step 2's classification
is new this round and unproved; steps 3 and 4 are two structurally different,
independent formalization tasks (do not conflate them — round 17's explorer
found they are genuinely distinct phenomena, not one family).
Cases to cover: classify each of the 8 catalogued hard points as
Self-Bisection-Crossover, Flat-Edge, or (if neither) something new; a point
found in neither category is a fresh open case, not automatically one of the
two.
Watch out for: (a) do not trust a low-restart-count float optimizer result
without a higher-restart re-check (round 16's own documented artifact);
(b) do not count Zero-Removal-padded ties as genuine branch degeneracy;
(c) an exact-arithmetic check is mandatory before building theory on the
Flat-Edge endpoint claim (currently float-only).

lp-duality-split-polytope: advance
Target: the problem's actual claim, upper-bound direction, restricted to the
region vertex $e_0$ — firming up whether $s<n-1$ active (split) pieces can
ever reach the universal floor $V=1/2$ exactly (secondary to the two gaps
above; the certified Perfect-Tie-Family Characterization already shows
$s=n-1$ suffices and is the only family among "perfect" zero-residual
constructions that attains $c(n)$).
Technique: exact-arithmetic verification of a Nelder-Mead-sourced numeric
lead, plus (if time allows) a Mass-Constraint-style counting/injection
argument mirroring the already-certified $\Pi\ge1/2$ technique.
Skeleton:
  1. Re-run the round-16 $s<n-1$ numeric lead ($n=8,9,10$, $s=n-2,n-3,n-4$)
     in exact rational arithmetic (`Fraction`/`sympy.Rational`), replacing
     the float Nelder-Mead, restricted to the already-documented legal-box
     constraints (avoiding the known negative-fragment optimizer artifact),
     to check whether the shrinking-margin trend is real or a float-precision
     artifact.
  2. If spare capacity remains: attempt to *derive* $s\ge n-1$ as necessary
     for hitting the floor exactly at $e_0$, via a counting argument
     structurally parallel to the certified Mass-Constraint Theorem
     ($\Pi\ge1/2$ forces $s>(n+1)/3$) — i.e. find the analogous mass/parity
     inequality that forces $s\ge n-1$, not just $s>(n+1)/3$.
Key lemmas (claim + mechanism):
  - (conjectural, not yet a lemma) $s<n-1$ never attains $V=1/2$ exactly at
    $e_0$ — if provable, likely via the same mass-counting technique as the
    Mass-Constraint Theorem, sharpened to force the tighter bound.
Open gaps: the whole necessity direction; currently only soft float evidence.
Cases to cover: none (single-vertex question).
Watch out for: this is explicitly non-critical-path (per round 17's
plateau-check) — do not let it consume a build slot at the expense of the
two gaps above; only dispatch if a builder has spare capacity this round.
