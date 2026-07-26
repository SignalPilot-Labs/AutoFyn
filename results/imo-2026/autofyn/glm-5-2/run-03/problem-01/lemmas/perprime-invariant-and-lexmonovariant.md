# Lemma: per-prime gcd invariant $d_p$ and the $(\Omega,K)$ lex monovariant

## Source
Proved in full in `results/imo-2026-01/approaches/perprime-gcd-lexmonovariant.md`, Steps 1–3 (round 1).

## Statement

Consider the blackboard process on 2026 integers $>1$ where a move replaces two entries $m,n>1$ by $\gcd(m,n)$ and $\operatorname{lcm}(m,n)/\gcd(m,n)$.

**(A) Per-prime move action.** For any prime $p$, if the chosen entries have $p$-valuations $\alpha,\beta$, the move sends $(\alpha,\beta)\to(\min(\alpha,\beta),\,|\alpha-\beta|)$ and leaves all other $p$-valuations untouched.

**(B) Invariant.** For each prime $p$, the quantity $D_p:=\gcd(v_p(a_1),\dots,v_p(a_{2026}))$ (convention $\gcd(x,0)=x$) is invariant under every move. In particular $D_p=d_p$ (its initial value) at every reachable state.

**(C) Monovariant.** With $\Omega:=\sum_i\Omega(a_i)$ (total prime-factor multiplicity, completely additive) and $K:=\#\{i:a_i>1\}$, every legal move strictly decreases $(\Omega,K)$ lexicographically. The drop equals:
- Case $g=\gcd(m,n)=1$ (coprime): $\Omega$ unchanged, $K\to K-1$.
- Case $g>1$, $m\ne n$: $\Omega\to\Omega-\Omega(g)$ (drop $\Omega(g)\ge 1$), $K$ unchanged.
- Case $g>1$, $m=n$: both drop.

(The three cases are exhaustive; $g=1$ with $m=n$ is impossible since $m=n>1\Rightarrow g>1$.)

## Key identity used
$\gcd(\min(\alpha,\beta),|\alpha-\beta|)=\gcd(\alpha,\beta)$ — the Euclidean step.
$\Omega$-drop when $g>1$: $\Omega(m)+\Omega(n)-\Omega(g)-\Omega(\operatorname{lcm}/\gcd)=\Omega(g)$ (derived either by complete additivity or per-prime as $\sum_p\min(v_p(m),v_p(n))$).

## Status
Proved in full (reviewer-pending certification). Reusable by any approach to imo-2026-01 that needs the per-prime invariant, termination, or both.
