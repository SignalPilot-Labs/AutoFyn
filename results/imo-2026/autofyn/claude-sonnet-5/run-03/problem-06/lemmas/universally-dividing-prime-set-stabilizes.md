## Lemma (Universally-dividing prime set stabilizes)

For $n\ge1$, let $U_n:=\{p\in R(a_1):p\mid a_i\text{ for every }1\le i\le
n\}$. Then $(U_n)$ is a non-increasing sequence of subsets of the fixed
finite set $R(a_1)$, hence stabilizes: there is $n_0$ and $U_\infty$ with
$U_n=U_\infty$ for all $n\ge n_0$.

### Proof
"$p$ divides all of $a_1,\dots,a_{n+1}$" implies "$p$ divides all of
$a_1,\dots,a_n$", so $U_{n+1}\subseteq U_n$. A non-increasing chain of
subsets of a fixed set of size $\omega(a_1)$ can strictly decrease at most
$\omega(a_1)$ times, so it is eventually constant. $\blacksquare$

### Insufficiency (kept as a caveat)
$U_\infty$ can miss primes that matter for the eventual period $L$: for
$a_1=35$, $5\notin U_\infty$ (it stops dividing every term after $a_2=40$
fails once $a_3=42$ appears), yet the eventual period $L=210=2\cdot3\cdot
5\cdot7$ still has $5\mid L$ — $5$ recurs periodically (not universally).
So $U_\infty$ alone cannot finish the problem; it is a free but weak
invariant, superseded in usefulness by
`prefix-support-stabilization.md`'s residue-tracking generalization.

### Provenance
Proved in `approaches/frozen-invariant-monovariant.md`, §1 (Lemma 1),
carried over from the round-5-opening draft, unchanged. Independently
re-derived by the proof-reviewer; elementary, no gap.
