## Within-Chamber Affinity Theorem (conditional) + Singular-Case Proposition

**Source:** `approaches/lp-duality-certificate.md`, "Round 20 build" section
(content added in round 21's build, despite the internal "Round 20"
heading label — cosmetic mislabeling only, flagged, does not affect
correctness).
**Status:** CERTIFIED (proof-reviewer, round 21), as a conditional theorem
plus a companion proposition narrowing (but not eliminating) its
hypothesis's scope. **Does NOT close case (b2)** — infrastructure only.

### Setup

Fix a composition $\mathbf c=(c_1,\dots,c_m)$ and a full combinatorial
type $(\mathbf c,\tau,\pi)$: for each piece $i$ with $c_i\ge1$, a
partition of its $c_i+1$ slots into pinned slots (each targeting either
the constant $0$ or a specific slot of another piece) and a tied group of
size $q_i$ with common unknown value $v_i$; plus a compatible total
pre-order $\pi$ on all slots. Let $I=\{i: c_i\ge1, q_i\ge1\}$, $k=|I|$.

### The joint linear system

Mass conservation on each $i\in I$ gives a row
$q_iv_i+\sum_{j\in I}n_{ij}v_j = p_i-\sum_{j\notin I}n_{ij}p_j$, where
$q_i,n_{ij}$ are pure slot/pin-target counts depending only on $\tau$
(never on $p$'s numeric value). Stacking gives $M(\tau)\mathbf v=Np$,
$M(\tau)\in\mathbb R^{k\times k}$ type-dependent and $p$-independent,
right-hand side linear (homogeneous) in $p$.

### Theorem (Within-Chamber Affinity, conditional)

If $M(\tau)$ is invertible, then for every $p$ in the chamber
$U(\mathbf c,\tau,\pi)$, $\mathbf v(p)=M(\tau)^{-1}Np$ is the unique
realizing solution, every slot value is a fixed linear function of $p$,
and $\Phi_{\min}(p)=T(p)-E(F^*(p))$ is affine (linear) in $p$ throughout
$U$.

### Proposition (singular case)

If $M(\tau)$ is singular with left null functionals $\phi_1,\dots,\phi_d$:
either (i) some $\phi_rN\ne0$, forcing $U\subseteq\{p:\phi_r(Np)=0\}$, a
proper hyperplane — so $U$ has empty interior and cannot be a genuine open
chamber; or (ii) every $\phi_rN\equiv0$ (an unruled-out residual
algebraic-coincidence sub-case, reduced to a finite per-type check, not
shown impossible in general).

### Verification

Proof-reviewer independently re-derived the row structure of $(\dagger)$
(mass-conservation rows forced-linear in $p$ with pure-count, $p$-independent
coefficients; confirmed no hidden $p$-dependence smuggled into $M(\tau)$)
and confirmed the standard linear-algebra argument (unique solution under
invertibility $\Rightarrow$ affine dependence on the right-hand side) is
correctly executed with no gaps. The singular-case dichotomy (range/null-space
argument) is also standard and correctly executed.

### Scope note — what this does NOT establish

This is necessary infrastructure only. It does **not** enumerate the
finitely many chambers/types for general $n$, does **not** evaluate
$\Phi_{\min}$ at any extreme point against the target $a_nT$, and does
**not** rule out case (ii) above in general. Case (b2) of the general
upper bound (`lp-duality-certificate`'s own top-level target) remains
open. A genuine amber-flag numerical signal (chamber/type density growing
from $\approx28\%$ at $n=3$ to $\approx64\%$ at $n=4$ inside case (b2)'s
box, composition-level sampling) is recorded as a risk indicator for
whether a general-$n$ closure via this route stays tractable — reported
honestly, not a disproof.
