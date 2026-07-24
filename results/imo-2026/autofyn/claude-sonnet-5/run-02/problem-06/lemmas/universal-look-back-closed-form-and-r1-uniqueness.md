# Lemma: Universal Look-Back Closed Form (all `r`) and the Uniqueness of `r=1` Theorem (round 28)

**Source.** `a1-pq-subfamily-theorem`, round 28 build.

**Depends on (certified).**
`lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md` (the
`K_0`-boundedness relation `p(n_0-1)+j=s_0(j,r)\cdot q`, `s_0(j,r)\in
\{1,\dots,p-1\}` the unique solution of `s_0\cdot r\equiv j\pmod p`) and
`lemmas/universal-look-back-witness-identity.md` (the identity
`\gcd(N,a_i)=\gcd(p(n-i)+j,\,q+i-1)`, and in particular at look-back
distance `0`: `\gcd(N,a_n)=\gcd(j,q+n-1)`).

## Setup

Fix odd prime `p`, `a_1=pq` (`q>p` prime), strong induction hypothesis
`H(n)`: `a_i=p(q+i-1)` for `i\le n`. For `j\in\{2,\dots,p-1\}`,
`r\in\{1,\dots,p-1\}`, and `q` prime with `q\equiv r\pmod p`, `q>p`, recall
`s_0(j,r)\in\{1,\dots,p-1\}` and `n_0(j,r;q)` (the first, `k=0`, Case-(b)
occurrence of band `j`), satisfying the exact relation
```
p(n_0-1)+j = s_0(j,r)\cdot q.                                     (★)
```
For `k\ge0`, the `k`-th Case-(b) occurrence of band `j` is at
`n=n_0(j,r;q)+kq`.

## Lemma 1 (Universal Look-Back Closed Form, all `r`)

**Statement.** Define
```
c(p,j,r) := ( s_0(j,r) \cdot p^{-1}_j ) \bmod j,
```
where `p^{-1}_j` is the inverse of `p` modulo `j` (exists: `\gcd(p,j)=1`
since `p` is prime and `0<j<p`). Then `c(p,j,r)` depends only on `p,j,r`
(not `q`), and for every `k\ge0`, at the `k`-th Case-(b) occurrence of band
`j`,
```
gcd(N,a_n) = gcd( j, (k+1+c(p,j,r)) \bmod j ).
```

**Proof.** Reduce (★) mod `j` (using `j\equiv0\pmod j`):
`p(n_0-1)\equiv s_0(j,r)\cdot q\pmod j`. Since `\gcd(p,j)=1`, multiply by
`p^{-1}_j`:
```
n_0-1 \equiv s_0(j,r)\,p^{-1}_j\,q \equiv c(p,j,r)\cdot q \pmod j,     (‡)
```
where the last step uses `s_0(j,r)\,p^{-1}_j\equiv c(p,j,r)\pmod j` by
definition of `c`, and congruence of a factor propagates through
multiplication.

At `n=n_0+kq`: `q+n-1=q(k+1)+(n_0-1)\equiv q(k+1)+cq=q(k+1+c)\pmod j$ by
(‡). By the certified Universal Look-Back Witness Identity at look-back
distance `0`, `\gcd(N,a_n)=\gcd(j,q+n-1)=\gcd(j,q(k+1+c))`. Since `q$ is
prime and `q>p>j$, `q\nmid j`, so `\gcd(q,j)=1`, giving
`\gcd(j,q(k+1+c))=\gcd(j,k+1+c)=\gcd(j,(k+1+c)\bmod j)`. `\blacksquare`

**Consistency with the certified `r=1` corollary.** At `r=1`,
`s_0(j,1)=j` exactly (from `s_0\cdot1\equiv j\pmod p$, `s_0\in
\{1,\dots,p-1\}`, and `j` is already in that range). So `c(p,j,1)=(j\cdot
p^{-1}_j)\bmod j=0` (a multiple of `j` reduces to `0$ mod `j`),
recovering exactly `\gcd(N,a_n)=\gcd(j,k+1)`, the certified round-27
formula.

## Lemma 2 (Uniqueness of `r=1`)

**Statement.** Fix odd prime `p`. Among `r\in\{1,\dots,p-1\}`, `r=1` is
the unique residue with `c(p,j,r)=0` for every `j\in\{2,\dots,p-1\}`
simultaneously.

**Proof.**

*Reformulation.* Since `p^{-1}_j` is a unit mod `j`, multiplication by it
is a bijection on `\mathbb Z/j\mathbb Z`, sending `0` to `0` and only `0`
to `0`. Hence for any integer `s`: `(s\cdot p^{-1}_j)\bmod j=0 \iff
j\mid s`. So
```
c(p,j,r)=0 \iff j\mid s_0(j,r).                                    (§)
```

*(⟸) `r=1` works.* `s_0(j,1)=j` (shown above), so `j\mid s_0(j,1)$
trivially, for every `j`.

*(⟹) No `r\ne1` works — a single universal witness band `j=p-1`.* Fix
`r\in\{2,\dots,p-1\}`. Note `p-1\in\{2,\dots,p-1\}$ is a valid band since
`p\ge3\Rightarrow p-1\ge2`.

Let `\rho:=r^{-1}\bmod p\in\{1,\dots,p-1\}` (exists, `\gcd(r,p)=1`).
Inversion is a bijection of `\{1,\dots,p-1\}` (the nonzero residues mod
prime `p` form a group), and `1` is its own inverse, so `\rho=1\iff r=1`;
since `r\ne1$ here, `\rho\ne1`.

By definition, `s_0(p-1,r)$ is the unique element of `\{1,\dots,p-1\}`
with `s_0\cdot r\equiv p-1\equiv-1\pmod p`. Multiplying by `\rho`:
`s_0\equiv-\rho\equiv p-\rho\pmod p`. Since `\rho\in\{1,\dots,p-1\}`,
`p-\rho\in\{1,\dots,p-1\}$ too, and being the representative in that
range, `s_0(p-1,r)=p-\rho`.

Now `(p-1)\mid(p-\rho)`: both `p-1` and `p-\rho$ lie in `\{1,\dots,p-1\}`;
the only multiple of `p-1` in this interval is `p-1` itself (`0` is below
it; `2(p-1)=2p-2\ge p-1+1=p>p-1` for `p\ge2`, so `2(p-1)$ is above it).
Hence `(p-1)\mid(p-\rho)\iff p-\rho=p-1\iff\rho=1`. Since `r\ne1\Rightarrow
\rho\ne1$, we get `(p-1)\nmid(p-\rho)=s_0(p-1,r)`, i.e. by (§),
`c(p,p-1,r)\ne0`.

So for every `r\ne1` and every odd prime `p`, band `j=p-1` gives
`c(p,p-1,r)\ne0`, refuting "`c=0` for every `j`" for that `r`. Combined
with `(⟸)`, this proves Lemma 2. `\blacksquare`

## Independent numerical verification

Checked, own Python/`sympy` script, `p\in\{5,7,11,13,17,19,23,29,31,37,
41\}`, every `r\in\{2,\dots,p-1\}$: `c(p,p-1,r)\ne0$ in every case (matches
Lemma 2's `⟹` direction); every `j\in\{2,\dots,p-1\}` at `r=1$: `c(p,j,1)
=0$ in every case (matches Lemma 2's `⟸` direction). Also checked Lemma
1's closed form directly against `\gcd(j,(q+n-1)\bmod j)` for
`p\in\{5,7,11,13\}`, all bands, all `r`, 50 primes per class,
`k\in\{0,\dots,4\}`: exact match in every sampled instance (8500+
instances), consistent with the round-28 outline-reviewer's independent
8400-instance check.

## Scope / what these lemmas do NOT establish

- Lemma 2 shows only that **some** band `j` fails to have `c=0` for each
  `r\ne1`; it does not show `c(p,j,r)\ne0` for *every* `j` at a given
  `r\ne1` (indeed this need not hold — a given non-diagonal `r` can still
  have `c(p,j,r)=0` at some particular band `j\ne p-1`).
- Neither lemma shows that a cell with `c(p,j,r)\ne0` is a genuine
  exception of the recurrence — it only means the unconditional
  (threshold-free) look-back-0 witness does not apply there; the
  pre-existing per-`p` Legendre-Sieve/Primorial-Floor machinery may still
  supply a witness for all sufficiently large `q` in that cell, exactly as
  before Lemma 1/2 were derived. This is a bookkeeping simplification of
  which `(j,r,k)` cells are "at risk," not new closure leverage.
- The `k\ge1,\gcd(k+1,j)>1` residual for `r=1` (round 27's open gap)
  is untouched: Lemma 1 reduces to the certified round-27 formula there
  and adds no new witness mechanism.

## Status

Both lemmas fully proved, self-contained, general (every odd prime `p`,
every `j,r`), reusable by any future `a1-pq`-machinery work. Recommend
certification.
