## Lemma (Set-theoretic / static reformulation of greedy acceptance)

Let $(a_n)_{n\ge1}$ be the problem's greedy sequence, $R(m)$ the set of
distinct prime divisors of $m$, and for $m > a_1$ define
$$\mathrm{Good}(m) :\iff \gcd(m, a_i) > 1 \text{ for every } i \ge 1 \text{ with } a_i < m.$$
Then for every integer $m > a_1$:
$$m \in \{a_n : n \ge 1\} \iff \mathrm{Good}(m).$$

### Proof
($\Rightarrow$) Suppose $m = a_n$ for some $n$; since $m > a_1$ and $(a_n)$
is strictly increasing, $n \ge 2$. For any $i \ge 1$ with $a_i < m = a_n$,
strict monotonicity forces $i \le n-1$. The defining property of the
sequence, applied at step $n-1$, gives $\gcd(a_n, a_i) > 1$ for every
$i = 1,\dots,n-1$; in particular for our $i$. Hence $\mathrm{Good}(m)$ holds.

($\Leftarrow$) Suppose $\mathrm{Good}(m)$ holds for some $m > a_1$. Since
$a_1 < m$ and $a_n \to \infty$, the set $\{n \ge 1 : a_n < m\}$ is a nonempty
finite set; let $n$ be its largest element, so $a_n < m$ and (by maximality)
$a_{n+1} \ge m$. We show $m = a_{n+1}$.

Suppose, for contradiction, $m \neq a_{n+1}$; combined with $a_{n+1} \ge m$
this gives $a_n < m < a_{n+1}$. By definition $a_{n+1}$ is the smallest
integer exceeding $a_n$ satisfying $\gcd(\cdot, a_i) > 1$ for every
$i = 1,\dots,n$. Since $m$ is a smaller such candidate (exceeding $a_n$, less
than $a_{n+1}$), minimality forces $m$ to fail this condition: there is
$i_0 \in \{1,\dots,n\}$ with $\gcd(m, a_{i_0}) = 1$. But $a_{i_0} \le a_n < m$,
so $i_0$ witnesses $a_{i_0} < m$ and $\gcd(m,a_{i_0})=1$, contradicting
$\mathrm{Good}(m)$. Hence $m = a_{n+1}$. $\blacksquare$

### Provenance
Proved in `approaches/state-compactness-pigeonhole.md`, round 2, as
"Proposition B." Self-contained, depends only on well-definedness /
monotonicity of the sequence (`lemmas/existence.md`). Verified by the
proof-reviewer, round 2: the two-directional argument is correct and
non-circular (does not assume the periodicity target).

### Use
Converts membership in the accepted set (a recursively/order-defined
notion) into a static predicate that can be analyzed set-theoretically —
e.g. as a union of residue classes once a self-sufficiency hypothesis is
granted (see `lemmas/periodicity-of-residue-class-union.md`).
