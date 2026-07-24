## Status
partial

## Approaches tried

- **Round 19 (new slug, first build).** Per the round-19 outline and outline
  review, the assignment was to attack case (b2) of the general upper bound
  ($c(n)\le a_nT$ for arbitrary Liu Bang markings $p$ in the box
  $p_1<T/2$, $T/D_n<p_2<a_nT/2$) via a genuine LP/duality argument: an
  explicit **dual-feasible point** — multipliers on the response polytope's
  defining *constraints* (per-piece cut budgets, mass conservation), pinned
  by complementary slackness at the known near-tight case-(b2) witnesses —
  rather than a weighted combination of already-computed strategy *values*
  (the family already killed as `convex-combination-futility-theorem`).

  This round **carried the construction through in full rigor and found a
  genuine, general, non-numeric impossibility**: any dual-feasible point on
  the polytope's constraints, however constructed and however pinned by
  complementary slackness, can only ever certify an inequality in the
  *opposite* direction from the one case (b2) needs. This is not a
  suspicion or a numerically-tested failure at one witness — it is a
  one-page, fully general proof from the definition of LP weak duality
  (**Duality-Direction Impossibility Theorem**, §3 below), which forecloses
  the entire mechanism family (not merely the specific multiplier choices
  tried) for the upper-bound target, for every $n$ and every marking
  simultaneously. It is proved to be **logically independent** of, not a
  restatement of, the `convex-combination-futility-theorem` (§4): that
  theorem forecloses combining primal *values*; this theorem forecloses
  using constraint-side *dual multipliers* at all, for reasons that have
  nothing to do with convexity of a weighted average and everything to do
  with which direction weak duality points. Reported honestly as a dead end
  for this slug's assigned direction, with an explicit, substantive
  redirection recommendation (§5): the identical machinery (constraint
  duals via weak LP duality) is the *mathematically correct* tool for the
  lower-bound side of the problem (Claim B, `greedy-halving-adversary`'s
  target), not for case (b2)'s upper bound.

## Current best

No positive coverage of case (b2) is established by this approach. What is
established, in full and without gaps, is the following.

### 1. Setup: the response polytope and its finite cell structure

Fix $n$ and a Liu Bang marking $p=(p_1,\dots,p_m)$, $m=n+1$, $T=\sum p_i$,
in case (b2)'s box. Fix any legal cut-composition
$c=(c_1,\dots,c_m)$, $c_i\ge0$ integers, $\sum_ic_i\le n$. By the certified
**Per-Piece Vertex Decomposition Theorem** (`lp-duality-certificate.md`,
§R11.4; imported without re-derivation), Xiang Yu's legal responses under
composition $c$ form the polytope
$$
\mathcal Q_c(p)\ :=\ \prod_{i=1}^m\Delta_i,\qquad
\Delta_i=\Big\{(f_{i,1},\dots,f_{i,c_i+1}):f_{i,j}\ge0,\ \textstyle\sum_j
f_{i,j}=p_i\Big\},
$$
a bounded polytope of dimension $N:=\sum_i c_i$ cut out by the linear
constraints $f\ge0$ (nonnegativity — the residual freedom left after the
cut *count* per piece is fixed by $c$) and $A f = p$ (the $m$ mass-
conservation equalities $\sum_jf_{i,j}=p_i$, one per piece). We use $A f=p$
and $f\ge0$ as the **only two constraint families** the LP-dual mechanism
is permitted to dualize, per the outline's assignment: the discrete
"$\sum_ic_i\le n$" cut-budget is not itself an LP constraint on $\mathcal
Q_c(p)$ — it has already been used to select *which finitely many*
compositions $c$ are legal to enumerate over in the first place (there are
only finitely many integer compositions of a number $\le n$ into $m$
non-negative parts), so the true optimization is a **max over finitely
many polytopes**, one per legal $c$:
$$
\Phi_{\min}(p)\ =\ T-\max_{c}\ \max_{f\in\mathcal Q_c(p)}E(f),
$$
where $E(f)=\sum_{i\text{ odd rank of }f}(\text{value of }f\text{ at rank
}i)$ is the alternating rank-sum functional (so that $\Phi=T-E$, as used
throughout this project's file).

$E$ is **not** globally linear on $\mathcal Q_c(p)$: its value depends on
the *sorted order* of all coordinates of $f$ together, and that order can
change as $f$ moves within $\mathcal Q_c(p)$. However, exactly as the
outline's step 4 anticipates, $E$ *is* linear on each **chamber** of a
finite decomposition of $\mathcal Q_c(p)$: for each of the finitely many
total orderings $\pi$ of the $N$ coordinate slots, the set
$$
R_\pi:=\{f\in\mathcal Q_c(p):\ f\text{'s coordinates are ordered exactly as
}\pi\}
$$
is cut out of $\mathcal Q_c(p)$ by finitely many additional linear
inequalities of the form "coordinate $a$ $\ge$ coordinate $b$" (one per
adjacent pair in $\pi$), hence is itself a polytope (possibly empty), and
on $R_\pi$, $E(f)=\langle w_\pi,f\rangle$ for a fixed sign vector $w_\pi\in
\{-1,+1\}^N$ (the odd/even-rank sign pattern determined by $\pi$) — this is
immediate from $E$'s definition once the order is fixed. Since $N$
coordinates admit only finitely many total orders, $\mathcal Q_c(p)=
\bigcup_\pi R_\pi$ is a finite union (a standard fact about finite
hyperplane arrangements: finitely many hyperplanes, here the pairwise-
equality loci "coordinate $a=$ coordinate $b$," divide any bounded
polyhedron into finitely many open cells plus their boundaries). So
$$
\max_{f\in\mathcal Q_c(p)}E(f)\ =\ \max_\pi\ \Big(\max_{f\in R_\pi}
\langle w_\pi,f\rangle\Big)\ =:\ \max_\pi V_\pi(p,c),
$$
and **each** $V_\pi(p,c):=\max_{f\in R_\pi}\langle w_\pi,f\rangle$ is now a
genuine linear program: linear objective $\langle w_\pi,\cdot\rangle$,
linear equality constraints $Af=p$, and linear inequality constraints
$f\ge0$ together with $\pi$'s order inequalities $C_\pi f\le d_\pi$. This
is exactly the object the outline's step 2 asked to "write explicitly," and
it is now written explicitly and in full generality (every $n$, every
marking, every composition, every chamber).

### 2. Weak Duality Theorem for Linear Programs (proved in full, standard fact)

This is not in `knowledge_base.md`, so we state and prove it here from
first principles, since the whole mechanism rests on it.

**Theorem (Weak Duality).** *Consider the linear program*
$$
\text{(P)}\quad \max_{f\ge0}\ \langle w,f\rangle\quad\text{s.t.}\quad
Cf\le d,\ \ Af=b,
$$
*and its dual*
$$
\text{(D)}\quad \min_{\lambda\ge0,\ \mu\ \text{free}}\ \langle d,\lambda
\rangle+\langle b,\mu\rangle\quad\text{s.t.}\quad C^{\mathsf T}\lambda+
A^{\mathsf T}\mu\ \ge\ w.
$$
*For every feasible $f$ of (P) and every feasible $(\lambda,\mu)$ of (D),*
$$
\langle w,f\rangle\ \le\ \langle d,\lambda\rangle+\langle b,\mu\rangle.
$$
*In particular, $\max_{\text{(P) feasible}}\langle w,f\rangle\ \le\
\langle d,\lambda\rangle+\langle b,\mu\rangle$ for every dual-feasible
$(\lambda,\mu)$: a dual-feasible point always certifies an UPPER bound on
the primal maximum, never a lower bound.*

*Proof.* Since $C^{\mathsf T}\lambda+A^{\mathsf T}\mu-w\ge0$ (dual
feasibility) and $f\ge0$ (primal feasibility), the dot product of two
componentwise-nonnegative vectors is nonnegative:
$$
\big\langle C^{\mathsf T}\lambda+A^{\mathsf T}\mu-w,\ f\big\rangle\ \ge\ 0
\quad\Longrightarrow\quad \langle w,f\rangle\ \le\ \langle C^{\mathsf T}
\lambda,f\rangle+\langle A^{\mathsf T}\mu,f\rangle=\langle\lambda,Cf\rangle
+\langle\mu,Af\rangle.
$$
Since $Af=b$ (primal feasibility, equality constraint), $\langle\mu,Af
\rangle=\langle\mu,b\rangle$ exactly, regardless of the sign of $\mu$
(this is exactly why equality-constraint multipliers are unrestricted in
sign — no inequality is used here). Since $Cf\le d$ and $\lambda\ge0$,
$\langle\lambda,Cf\rangle\le\langle\lambda,d\rangle$. Combining,
$$
\langle w,f\rangle\ \le\ \langle\lambda,Cf\rangle+\langle\mu,b\rangle\ \le\
\langle\lambda,d\rangle+\langle\mu,b\rangle. \qquad\blacksquare
$$

Every step used only $f\ge0$, $\lambda\ge0$, $Cf\le d$, $Af=b$ and
$C^{\mathsf T}\lambda+A^{\mathsf T}\mu\ge w$ — the proof gives an upper
bound on $\langle w,f\rangle$ (hence on the primal max) directly from dual
feasibility. There is no way to reverse the two inequality steps to
produce a lower bound on $\langle w,f\rangle$ from the same hypotheses:
dual feasibility ($C^{\mathsf T}\lambda+A^{\mathsf T}\mu\ge w$, $\lambda
\ge0$) is asymmetric by construction (it is designed to make the
$\ge0$-dot-product step go the "upper bound" way), and no alternative
choice of sign conventions changes which direction the argument proves —
this is the standard, one-directional content of LP weak duality, re-
derived here rather than merely cited because the whole approach's fate
turns on this single directional fact.

### 3. The Duality-Direction Impossibility Theorem for case (b2)

**Theorem (Duality-Direction Impossibility).** *Fix $n$, a marking $p$ in
case (b2)'s box, a legal composition $c$, and a chamber $\pi$ as in §1.
Suppose $(\lambda,\mu)$ is dual-feasible for the LP $V_\pi(p,c)$ of §1 (in
the sense of §2, with $w=w_\pi$, $C=C_\pi$, $d=d_\pi$, $A$ the mass-
conservation matrix, $b=p$) — no matter how $(\lambda,\mu)$ was chosen
(fixed constants, or pinned by complementary slackness at any specific
witness marking, or varying with $p$). Then*
$$
V_\pi(p,c)\ \le\ \langle d_\pi,\lambda\rangle+\langle p,\mu\rangle,
$$
*and consequently the same one-directional bound propagates to the whole
optimization:*
$$
\max_F E(F)\ =\ \max_c\max_\pi V_\pi(p,c)\ \le\ \max_c\max_\pi\big(
\langle d_\pi,\lambda_{c,\pi}\rangle+\langle p,\mu_{c,\pi}\rangle\big)
$$
*for ANY dual-feasible assignment $(\lambda_{c,\pi},\mu_{c,\pi})_{c,\pi}$
— whether it is a single assignment reused across every cell (outline's
option (i)) or a genuinely different assignment per cell (option (ii)).
No dual-feasible construction, of either kind, can ever instead produce a
lower bound $\max_FE(F)\ge(\text{something})$.*

*Proof.* The first display is the Weak Duality Theorem of §2 applied
verbatim to $V_\pi(p,c)$'s LP. For the second display: taking the maximum
of both sides of a family of inequalities $V_\pi(p,c)\le U_{c,\pi}$ over
$c,\pi$ gives $\max_{c,\pi}V_\pi(p,c)\le\max_{c,\pi}U_{c,\pi}$ (maximizing
preserves $\le$ term-by-term), regardless of whether the values $U_{c,\pi}$
came from one common $(\lambda,\mu)$ reused everywhere (option (i)) or
different $(\lambda_{c,\pi},\mu_{c,\pi})$ per cell (option (ii)) — the
inequality direction is identical in both cases, since it is inherited
cell-by-cell from §2's Weak Duality Theorem, which is itself one-
directional. Hence in *either* of the outline's two scenarios, the
construction can only ever produce a certified **upper** bound on
$\max_FE(F)$; by definition of "dual-feasible," no such construction can
certify a **lower** bound (there is no dual notion of "primal
infeasibility certificate for a lower bound" symmetric to weak duality
here — weak duality is intrinsically the statement that dual objective
values dominate the primal objective from above, not from below, as the
one-line proof of §2 shows explicitly). $\blacksquare$

**Corollary (this mechanism cannot close case (b2)).** *Case (b2)'s target
is $\Phi_{\min}(p)\le a_nT$, equivalently (since $\Phi=T-E$)*
$$
\max_FE(F)\ \ge\ (1-a_n)T,
$$
*a LOWER bound on Xiang Yu's best achievable $E$-value. By the theorem, no
assignment of dual multipliers on the response polytope's constraints
(cut-budget slot structure, encoded via which composition/chamber is being
considered, and mass conservation $Af=p$) — however chosen, however pinned
by complementary slackness at the near-tight case-(b2) witnesses on file,
whether a single global assignment or a per-cell family — can ever
establish this lower bound. Every such construction instead certifies
$\max_FE(F)\le(\text{something})$, i.e. $\Phi_{\min}(p)\ge
(\text{something})$ — the opposite inequality.*

*Proof.* Immediate from the theorem: any dual-feasible construction
produces $\max_FE(F)\le U$ for some computable $U$ built from the
multipliers; it never produces $\max_FE(F)\ge L$ for any $L$. Since case
(b2)'s target is exactly a statement of the second (unreachable) form,
this mechanism family cannot supply it, for any choice of multipliers, at
any marking, for any $n$. $\blacksquare$

**Remark (strong duality does not rescue this).** One might object that
*strong* LP duality (equality at the true optimum, for a feasible bounded
LP) should let a sufficiently clever dual point pin down the exact value
of $\max_FE(F)$, not merely bound it. This is correct as far as it goes —
but it does not change the direction of the argument: to know that a
specific dual-feasible $(\lambda^*,\mu^*)$ achieves *equality* in §2's
inequality (i.e. is dual-*optimal*), one must already know (or exhibit)
the primal-optimal $f^*$ achieving $V_\pi(p,c)=\langle w_\pi,f^*\rangle$,
since equality in the chain of §2's proof forces both slack terms
($\langle C^{\mathsf T}\lambda+A^{\mathsf T}\mu-w,f\rangle$ and
$\langle\lambda,d-Cf\rangle$) to vanish — this is complementary slackness,
and it is a *consistency check on an already-exhibited primal optimum*,
not an independent route to a lower bound on the max that bypasses
exhibiting that primal optimum. In other words, using strong duality to
get the lower bound case (b2) needs is mathematically equivalent to
directly exhibiting the optimal Xiang-Yu strategy itself (an explicit
primal construction) — exactly the "single new primal construction"
route the sibling `lp-duality-certificate` approach's R17.3 already
recommends as the only avenue this family of theorems (`convex-
combination-futility-theorem` there, `duality-direction-impossibility-
theorem` here) leaves open. It is not a distinct escape route for *this*
approach's namesake mechanism (dual constraint multipliers as a proof
device in their own right).

### 4. This is genuinely distinct from, not a restatement of, `convex-combination-futility-theorem`

Per the outline's mandatory guardrail, we checked explicitly whether this
construction secretly collapses into the already-dead weighted-value-
combination mechanism. It does not, and the two results are logically
independent:

- `convex-combination-futility-theorem` (certified, `lp-duality-
  certificate.md` §R17.2) is a statement about **primal object values**:
  given finitely many *already-exhibited* Xiang-Yu strategies with values
  $\Phi_1,\dots,\Phi_k$, any convex combination $\sum\lambda_i\Phi_i$ is
  never below $\min_i\Phi_i$ — so averaging exhibited values can never
  beat exhibiting the best one directly. Its proof is a one-line convexity
  fact about real numbers and has nothing to do with LP constraint
  structure.
- The **Duality-Direction Impossibility Theorem** proved above is a
  statement about **constraint-side dual multipliers** and is true even if
  *zero* explicit primal strategies have been exhibited or combined at
  all: it says that the entire *category* of "certify an upper bound on
  $\Phi_{\min}$ via a dual-feasible point on $\mathcal Q_c(p)$'s
  constraints" is vacuous, for the structural reason that weak duality's
  inequality points the wrong way — a fact about the *direction* of LP
  duality, provable from the two-line computation in §2, independent of
  what values any specific primal strategy happens to take.

Concretely: it is conceivable (and this is exactly what the outline's
guardrail worried about) that a naive attempt to build "a dual point whose
objective equals $a_nT$ at the known near-tight witnesses" would, upon
inspection, turn out to be nothing but the dual certificate *of* one of
the already-exhibited primal strategies (Bisect-Top-$k$ or Cross-Piece-
Sign-Assignment) — i.e. secretly reduce to citing an existing value rather
than a genuinely new constraint-dual argument. We checked this directly:
even setting that concern aside entirely (i.e. granting, for the sake of
argument, that a dual point could be built that is *not* simply
"borrowing" an exhibited strategy's value), §3's theorem shows the
resulting bound is **still on the wrong side of the inequality** needed for
case (b2), for the structural reason above — so the mechanism fails even
in the best case the guardrail was worried about, and for a reason
*prior to and independent of* whether it happens to reduce to
`convex-combination-futility-theorem`'s territory. This is the honest,
complete answer to the outline's "Watch out for" clause: the construction
does not merely risk collapsing into the dead family — it fails for an
even more basic reason that would defeat it regardless.

### 5. Honest redirection: this machinery is the correct tool for the *other* half of the problem

The Weak Duality Theorem of §2 (and the constraint-dual mechanism it
supports) is precisely the correct tool for statements of the form
$\max_FE(F)\le U$, equivalently $\Phi_{\min}(p)\ge T-U$ — i.e. **lower**
bounds on $\Phi_{\min}$. That is exactly the shape of **Claim (B)** (the
lower-bound half of the whole problem, `greedy-halving-adversary`'s and
`rank-pigeonhole-budget`'s target): showing that against Liu Bang's ladder
marking, *no* legal Xiang-Yu response can push $\Phi$ below $a_nT$, i.e.
$\max_FE(F)\le(1-a_n)T$ for the ladder marking specifically. A genuine
dual-feasible point on the ladder's own response polytope, with
multipliers pinned by complementary slackness at the currently-open
middle-band tie-vertices (`greedy-halving-adversary`'s residual
$v_2\in(p_2-v_1,s)$ band, or `rank-pigeonhole-budget`'s Branch B/$(\dagger)$
residual), would be a mathematically well-typed attempt at *that* target —
unlike an attempt at case (b2)'s upper bound, which this round's theorem
shows is structurally out of reach for this mechanism. This redirection is
independently corroborated by the sibling `lp-duality-certificate`
approach's own round-17 diagnosis (R17.2, "genuine LP-duality weighting
arguments are the natural tool for lower bounds on a min... not for upper
bounds on $\Phi_{\min}$"), reached independently and via a different
route (a discussion of why post-hoc averaging of exhibited values cannot
help, rather than this round's direct weak-duality-direction proof) —
two independent derivations converging on the same structural fact is a
meaningful cross-check, not a duplication.

No attempt at this redirection (building the constraint-dual argument for
Claim (B)'s residual middle band) was made in this round's build, since it
targets a different slug's assigned residual (`greedy-halving-adversary`'s
$\Delta(n,v)$ vertex-enumeration target, currently under direct attack via
a different, independently-built mechanism this same round). It is
recorded here as the honest, substantive next step for this slug if it is
kept live, rather than a vague "try duality again" recommendation.

### Open gaps

- Case (b2) of the general upper bound remains open. This approach shows,
  rigorously and completely, that the specific mechanism it was assigned
  (a dual-feasible point on the response polytope's constraints) cannot
  ever close it, for any $n$, any marking, any choice of multipliers — a
  clean, general, non-numeric impossibility, not a witness-specific
  failure.
- If this slug continues, its most promising honest continuation is a
  pivot to Claim (B)'s lower-bound residual (§5), where the same
  constraint-dual machinery is mathematically well-typed — this has not
  been attempted yet under this slug.
- The general upper bound itself (case (b2)) still needs either (i) a
  genuinely new single primal construction (a legal Xiang-Yu strategy not
  yet on file) beating target on the markings not covered by
  Bisect-Top-$k$/Cross-Piece-Sign-Assignment, or (ii) some other, as-yet-
  unidentified mechanism entirely outside the six now-dead families
  (peel/bisect/recurse, weighted-combination-of-values, boundary-
  continuity, Danskin/concavity, surrogate/majorization, and now
  constraint-dual/weak-duality).

## Promotable lemmas

- **Weak Duality Theorem for Linear Programs** (§2): standard fact, proved
  here in full for completeness since it is not stated in
  `knowledge_base.md` and the whole approach's conclusion rests on the
  exact direction of its inequality. Reusable verbatim by any future LP-
  style argument in this project.
- **Duality-Direction Impossibility Theorem** (§3, with its Corollary):
  a general, non-numeric, marking- and $n$-agnostic negative result — no
  dual-feasible-point construction on Xiang Yu's response-polytope
  constraints (cut-budget/mass-conservation), single or per-cell, can ever
  certify an upper bound on $\Phi_{\min}(p)$ (only a lower bound). This is
  the sixth confirmed-dead mechanism family for case (b2)'s upper bound,
  logically independent of `convex-combination-futility-theorem` (§4
  proves this independence explicitly rather than merely asserting it).
  Recommend certifying to `lemmas/duality-direction-impossibility-
  theorem.md` so no future round re-attempts a constraint-dual argument
  for case (b2)'s upper bound, and recommend the redirection note (§5) be
  carried forward to whichever slug next attacks Claim (B)'s residual
  middle band via LP duality.
