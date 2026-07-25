## Lemma (Minimum Gap)

For every $n\ge1$: $a_{n+1}\ge a_n+2$ (the greedy sequence never has a
consecutive gap of exactly $1$).

### Proof
Let $m:=a_n+1$. Since $\gcd(a_n+1,a_n)=\gcd(1,a_n)=1$ (one step of the
Euclidean algorithm on consecutive integers), $m$ fails the defining
requirement $\gcd(a_{n+1},a_i)>1$ at $i=n$. Hence $m=a_n+1$ is not a valid
candidate for $a_{n+1}$, so $a_{n+1}\ne a_n+1$. Since $(a_n)$ is strictly
increasing (`lemmas/existence.md`), $a_{n+1}>a_n$ is an integer, so
$a_{n+1}\ge a_n+2$. $\blacksquare$

### Consequence
Sharpens `lemmas/bounded-gap-via-rad-a1.md` to the exact interval
$a_{n+1}-a_n\in[2,R]$ (with $R=\mathrm{rad}(a_1)$) for every $n\ge1$, with no
hypothesis on $a_1$ and no case split.

### Verification
Sanity-checked (not a proof step) by simulation: minimum observed gap over
$a_1=2,\dots,2999$ (60 terms each) is exactly $2$, never $1$.

### Provenance
Proved in `approaches/renormalization-induction-on-seed.md`, §7.1, round 5.
Independently re-derived by the proof-reviewer (three-line elementary
argument, no gap).
