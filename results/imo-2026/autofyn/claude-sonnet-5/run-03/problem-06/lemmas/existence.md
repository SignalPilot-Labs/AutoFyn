## Lemma (Well-definedness / existence of the greedy sequence)

Let $(a_n)$ be defined by: $a_1 > 1$ a fixed positive integer, and for $n \ge 1$,
$a_{n+1}$ is the smallest integer $> a_n$ with $\gcd(a_{n+1}, a_i) > 1$ for every
$i = 1, \ldots, n$. Then for every $n \ge 1$, $a_{n+1}$ exists (the defining
candidate set is nonempty, hence has a least element by well-ordering), and the
sequence is well-defined and strictly increasing.

### Proof
Fix $n \ge 1$. For each $i = 1,\ldots,n$ choose a prime $p_i \mid a_i$ (possible
since $a_i > 1$), and let $N$ be the product of the distinct primes among
$p_1,\ldots,p_n$. Every multiple of $N$ is divisible by each $p_i$, hence has
$\gcd > 1$ with each $a_i$, $i \le n$. The multiples of $N$ exceeding $a_n$ form
an infinite set (indeed an infinite arithmetic progression $a_n' , a_n'+N,
a_n'+2N,\ldots$ where $a_n'$ is the least multiple of $N$ exceeding $a_n$), all
lying in the candidate set $\{m > a_n : \gcd(m,a_i)>1 \ \forall i \le n\}$. This
candidate set, being a nonempty set of positive integers, has a least element by
well-ordering; that element is $a_{n+1}$. $\blacksquare$

### Provenance
Proved identically (independently) in `approaches/active-set-stabilization.md`
(Lemma 0) and `approaches/state-compactness-pigeonhole.md` (Lemma 0). Certified
by the proof-reviewer, round 1, as fully rigorous and reusable — depends only on
the problem's own definition, no other lemma required.
