# Build report — cross-substitution-fixed-point, round 1

Status: **partial**

Wrote the full, rigorous base layer (FE `f(f(y))=2f(y)-y`, injectivity, `g(y):=f(y)-y` orbit
structure `f^{(k)}(y)=y+kg(y)`, `g\ge0`, sufficiency of `f(x)=x+c` for `c\ge0`), and re-derived
Tool A/B `(x-y)^2 \ge 4f(y)(g(x)-g(y))` from scratch (verified algebraically by hand and with
sympy, matching the outline-reviewer's independent check exactly).

Main new result this round: found a cleaner way to run the outline's "second orbit instance"
programme — feed Tool A directly with iterated orbit points `x_m=f^{(m)}(x_0)`, `y_n=f^{(n)}(y_0)`
to get a two-parameter family `(x_0+mp_0-y_0-nq_0)^2 \ge 4(y_0+(n+1)q_0)(p_0-q_0)` for all
`m,n\ge0`, where `p_0=g(x_0), q_0=g(y_0)`. When `q_0>0` and `p_0/q_0` is irrational, the RHS is
bounded below by a fixed positive constant, while a from-scratch pigeonhole (Dirichlet/Kronecker)
density lemma shows `m,n\ge0` can be chosen to force the LHS below that constant — a genuine
contradiction, proving `g(x_0)=g(y_0)` in this sub-case. This is a complete, self-contained
sub-proof (Case 1 in the file), including a fully worked pigeonhole proof of the density lemma
(not cited as a black box) that correctly handles both signs of the discovered small step.

**Open gap (explicit, not papered over):** the mechanism needs two incommensurable orbit step
sizes for density. It does not close (a) `q_0=0` (a fixed point of `f`, where the second orbit
collapses to one point, leaving only one free integer parameter — insufficient for density), or
(b) `q_0>0` with `p_0/q_0` rational (where `\{mp_0-nq_0\}` is a discrete subgroup, not dense). I
tried several substitute finite combinations (Tool B, third auxiliary points) for both sub-cases
and could not close them in the time available. These are recorded honestly as the remaining gap;
Status is `partial`, not `solved`.

Promotable to `lemmas/`: Lemmas 1-4 (base layer, likely already duplicated across sibling
approaches — reviewer should dedupe), Tool A/B (shared load-bearing tool with `extremal-sup-inf`),
and the from-scratch Kronecker/Dirichlet pigeonhole density Lemma 5 (general-purpose, reusable
beyond this problem).

File: `/home/agentuser/repo/results/imo-2026-05/approaches/cross-substitution-fixed-point.md`
