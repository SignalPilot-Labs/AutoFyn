## Lemma (Multiple-of-$R$ Realization)

Let $R:=\mathrm{rad}(a_1)$. For every integer $x>a_1$ with $R\mid x$, $x$ is
an accepted term of the sequence, i.e. $x\in\{a_n:n\ge1\}$.

### Proof
Since $(a_n)$ is strictly increasing with $a_n\to\infty$
(`lemmas/existence.md`), $\{n\ge1:a_n<x\}$ is nonempty (contains $n=1$) and
finite; let $k$ be its maximum, so $a_k<x\le a_{k+1}$ (the right inequality
since $k$ is maximal).

$x$ is a legal candidate for the greedy step at $k$: for each $i\le k$, by
`lemmas/prime-factors-a1-cover-forever.md` some $p\in R(a_1)\cap R(a_i)$
exists; since $p\mid R\mid x$, $p$ is a common factor of $x,a_i$, so
$\gcd(x,a_i)\ge p>1$. This holds for all $i\le k$.

By minimality of the greedy definition, $a_{k+1}\le x$. Combined with
$a_{k+1}\ge x$, $a_{k+1}=x$, so $x\in\{a_n\}$. $\blacksquare$

### Strengthens
`lemmas/bounded-gap-via-rad-a1.md`, which only shows the next multiple of
$R$ is a legal *candidate*, not that it is *accepted*. This lemma pins down
the full arithmetic progression $\{kR:k\ge1,kR>a_1\}\subseteq\{a_n\}$
unconditionally.

### Verification
Independently re-simulated by the proof-reviewer for
$a_1\in\{15,21,35,45,63,105,375\}$ (800 terms each): zero missing multiples
of $R$ in every case.

### Provenance
Proved in `approaches/state-compactness-pigeonhole.md`, §12.1, round 5.
Independently re-derived by the proof-reviewer; no gap found.
