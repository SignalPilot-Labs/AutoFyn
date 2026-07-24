## Statement

Let $p_i(n)=2^{n+1-i}/(2^{n+1}-1)$ ($i=1,\dots,n+1$) be the $n$-ladder,
$r(n):=1-p_1(n)$, and $f(n):=1/(2^{n+1}-1)$ (the target value of the
alternating-sum functional $A$). Then for every $n\ge1$:
$$f(n) = p_1(n) - r(n), \qquad f(n) = r(n)\cdot f(n-1).$$

## Proof

Direct algebra: $p_1(n)-r(n) = \frac{2^n}{2^{n+1}-1}-\frac{2^n-1}{2^{n+1}-1}
=\frac{1}{2^{n+1}-1}=f(n)$. And $r(n)\cdot f(n-1) =
\frac{2^n-1}{2^{n+1}-1}\cdot\frac{1}{2^n-1}=\frac{1}{2^{n+1}-1}=f(n)$. See
`results/imo-2026-03/approaches/self-similar-potential-certificate.md`,
Lemma A. This corrects an earlier broken guess (the naive recursion
$\Psi_n=M-\Psi_{n-1}$, which silently conflated the unscaled and rescaled
tail values); the correct self-similar recursion for the *target constant*
uses the scaling identity $A(\lambda S)=\lambda A(S)$
(`alternating-sum-scaling`), not a bare subtraction.

## Certification note (proof-reviewer, round 2)

Independently re-derived by direct fraction algebra for $n=1,\dots,7$ in a
script — exact match in every case, including the $n=1$ boundary
(`r(1)=1/3`, `f(0)=1` by convention, product `=1/3=f(1)`, consistent).
Certified correct — a small but useful bookkeeping identity for any future
induction on $n$.
