# Domination Lemma

**Statement.** With `(a_n)` as in the problem, for every `n\ge1`, let `x:=a_{n+1}`
and let `q_1,\dots,q_r` be the distinct prime factors of `x` (`r=\omega(x)`). For a
prime `q`, let `D_n(q):=|\{i\le n : q\mid a_i\}|`. Then
`\sum_{j=1}^r D_n(q_j)\ge n`, hence `\max_{1\le j\le r}D_n(q_j)\ge n/r\ge n/\log_2 a_{n+1}`
(using `\omega(a_{n+1})\le\log_2 a_{n+1}`, since each of the `r` distinct prime
factors of `a_{n+1}` is `\ge2`, so `a_{n+1}\ge2^r`).

**Proof.** By admissibility of `x=a_{n+1}`, for every `i\in\{1,\dots,n\}`,
`\gcd(x,a_i)>1`, i.e. some prime factor `q_j` of `x` divides `a_i`; equivalently,
`i\in S_j:=\{i\le n:q_j\mid a_i\}` for at least one `j\in\{1,\dots,r\}`. So
`\{1,\dots,n\}=\bigcup_{j=1}^r S_j`, and by finite subadditivity of cardinality,
`n=|\{1,\dots,n\}|\le\sum_{j=1}^r|S_j|=\sum_{j=1}^r D_n(q_j)`. The pigeonhole/averaging
inequality `\max_jD_n(q_j)\ge\frac1r\sum_jD_n(q_j)\ge n/r` follows. $\blacksquare$

**Interpretation.** At every step `n`, admissibility of `a_{n+1}` forces at least one
of its own prime factors to already divide a `1/\omega(a_{n+1})`-fraction of the
previous terms `a_1,\dots,a_n`.

**Source.** Proved in full in `approaches/backbone-existence-crt.md`, Section 4.

**Certification.** Purely combinatorial (union bound + averaging pigeonhole); no
hypotheses beyond the problem's own definition and `\omega(m)\le\log_2 m`
(elementary). No gaps. Certified `solved`-quality (sorry-free) by the round-1
proof-reviewer.

**Cross-approach use.** Combined with Lemma 1 (also certified in this folder), this
lemma unconditionally resolves gap (a) of `backbone-existence-crt.md`'s open-gap
list (growth control making the dominant-prime count diverge); see the "Important
cross-approach consequence" note in `lemma-1-uniform-gap-bound.md`. Gap (b)
(concentration onto finitely many distinct dominant primes across all `n`) is not
addressed by this lemma alone and remains open.
