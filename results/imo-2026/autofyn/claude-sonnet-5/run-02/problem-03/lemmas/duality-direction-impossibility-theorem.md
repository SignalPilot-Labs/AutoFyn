## Duality-Direction Impossibility Theorem (new, round 19, certified by reviewer)

**Context.** Case (b2) of the general upper bound $c(n)\le a_nT$ (arbitrary
Liu Bang markings $p$ in the box $p_1<T/2$, $T/D_n<p_2<a_nT/2$) is the sole
remaining open region of the general upper bound. This lemma forecloses an
entire mechanism family for it: certifying $\Phi_{\min}(p)\le a_nT$ via a
dual-feasible point on the constraints (mass conservation, per-piece cut
budgets) of Xiang Yu's response polytope.

**Weak Duality Theorem (standard, restated and proved here since absent
from `knowledge_base.md`).** For the LP
$$\text{(P)}\quad\max_{f\ge0}\langle w,f\rangle\ \text{ s.t. }\ Cf\le d,\
Af=b,$$
and its dual
$$\text{(D)}\quad\min_{\lambda\ge0,\mu\text{ free}}\langle d,\lambda\rangle
+\langle b,\mu\rangle\ \text{ s.t. }\ C^{\mathsf T}\lambda+A^{\mathsf T}\mu
\ge w,$$
for every (P)-feasible $f$ and every (D)-feasible $(\lambda,\mu)$,
$$\langle w,f\rangle\ \le\ \langle d,\lambda\rangle+\langle b,\mu\rangle.$$

*Proof.* $C^{\mathsf T}\lambda+A^{\mathsf T}\mu-w\ge0$ (dual feasibility)
and $f\ge0$ give $\langle C^{\mathsf T}\lambda+A^{\mathsf T}\mu-w,f\rangle
\ge0$, i.e. $\langle w,f\rangle\le\langle\lambda,Cf\rangle+\langle\mu,Af
\rangle=\langle\lambda,Cf\rangle+\langle\mu,b\rangle\le\langle\lambda,d
\rangle+\langle\mu,b\rangle$, using $Af=b$ exactly (equality constraint,
so the sign of $\mu$ is irrelevant) and $Cf\le d,\lambda\ge0$ in the last
step. $\blacksquare$

**Duality-Direction Impossibility Theorem.** Every dual-feasible point on
the constraints of Xiang Yu's response-polytope LP — for any legal cut
composition $c$, any chamber $\pi$ of the finite hyperplane arrangement
that linearizes the rank-alternating-sum objective $E$, any $n$, any
marking $p$, and any rule for choosing the multipliers (fixed, or pinned
by complementary slackness at any witness, single or per-cell) — can only
ever certify an **upper** bound on $\max_FE(F)$ (equivalently a **lower**
bound on $\Phi_{\min}(p)$). It can never certify a **lower** bound on
$\max_FE(F)$ (equivalently the **upper** bound on $\Phi_{\min}$ that case
(b2) needs, $\max_FE(F)\ge(1-a_n)T$).

*Proof.* Immediate application of Weak Duality to each chamber LP
$V_\pi(p,c)$, then taking $\max_{c,\pi}$ of both sides of the resulting
family of one-directional inequalities $V_\pi(p,c)\le U_{c,\pi}$ (maximizing
preserves $\le$ termwise, regardless of whether the $U_{c,\pi}$ come from
one common dual point or a per-cell family). $\blacksquare$

**Provenance and verification.** First proved in
`approaches/minimax-lp-response-polytope.md` §§2-3 (round 19, new slug).
Independently re-derived by the proof-reviewer from the two-line weak-duality
computation; the argument is elementary, standard, and correct — dual
feasibility ($C^{\mathsf T}\lambda+A^{\mathsf T}\mu\ge w$, $\lambda\ge0$) is
asymmetric by construction and there is no alternative sign convention that
reverses the direction of the inequality it certifies.

**Consequence.** This is a sixth confirmed-dead mechanism family for case
(b2)'s upper bound (after peel/bisect/recurse-plus-full-IH, weighted-
combination-of-values, boundary continuity, Danskin/concavity, and
surrogate/majorization) — logically independent of
`convex-combination-futility-theorem` (that theorem forecloses combining
already-exhibited primal *values*; this theorem forecloses using
constraint-side dual *multipliers* at all, for a reason having nothing to
do with convexity of an average). No future round should attempt a
constraint-dual argument for case (b2)'s upper bound. The identical
machinery (constraint duals via weak LP duality) *is* mathematically
well-typed for **Claim (B)**'s lower-bound residual (a genuine lower bound
on $\Phi_{\min}$ against the ladder marking specifically) — recommended as
the honest redirection for any future slug attacking that target with LP
duality.
