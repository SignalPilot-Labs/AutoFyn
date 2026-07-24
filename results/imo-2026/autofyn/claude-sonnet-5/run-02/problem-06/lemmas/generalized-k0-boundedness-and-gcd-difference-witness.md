## Lemmas: Generalized `K_0`-Boundedness and Generalized gcd-Difference
Witness Lemma (for `a_1 = pq`, `p` an arbitrary fixed odd prime) (CERTIFIED,
round 25)

**Source.** `a1-pq-subfamily-theorem`, round 25. Independently re-verified
in full by the round-25 proof-reviewer.

### Lemma 1 (Generalized gcd-difference Witness Lemma)

**Statement.** Fix odd prime `p`, prime `q>p`, `a_1=pq`, and suppose the
strong induction hypothesis `a_i=p(q+i-1)` holds for `i=1,\dots,n`. For
`N:=a_n+j`, `j\in\{1,\dots,p-1\}`: `\gcd(N,a_n)=\gcd(N,j)`. In particular,
whenever `\gcd(N,j)=1`, index `i=n` witnesses the illegality of `a_n+j`.

**Proof.** One line: `\gcd(N,a_n)=\gcd(a_n+j,a_n)=\gcd(a_n+j,(a_n+j)-a_n)=
\gcd(N,j)`, using the standard identity `\gcd(x,y)=\gcd(x,x-y)`.

Strictly generalizes the certified `a1-3q` Parity Witness Lemma (the `j=2`
instance: `\gcd(N,2)=1\iff N` odd).

### Lemma 2 (Generalized `K_0`-Boundedness for `a_1=pq`)

**Statement.** Fix odd prime `p`, `j\in\{2,\dots,p-1\}`. For prime `q>p`
with `q\equiv r\pmod p` (`r\in\{1,\dots,p-1\}`), the first Case-(b)
occurrence of band `j` (the least `n_0` with `q\mid(a_{n_0}+j)`, in the
induction of Lemma 1's setting) satisfies `K_0(j,r):=(a_{n_0}+j)/q=
p+s_0(j,r)`, where `s_0(j,r)\in\{1,\dots,p-1\}` is the unique solution of
`s_0\cdot r\equiv j\pmod p` — a constant depending only on `p,j,r`, **never**
on `q`'s magnitude. Explicitly, `n_0(j,r;q)=1+(s_0(j,r)q-j)/p`, an affine,
strictly increasing function of `q`.

**Proof.** Case-(b) indices for band `j` satisfy `q\mid(p(n-1)+j)`. Since
`\gcd(p,q)=1`, `n\mapsto p(n-1)+j \bmod q` is a bijection on residues mod
`q`, so exactly one `n_0\in\{1,\dots,q\}` per cycle of `q` consecutive `n`
satisfies this; write `p(n_0-1)+j=s_0q`. Then `s_0\ge1` (numerator
positive, a multiple of `q`) and `s_0\le p-1` (since `n_0\le q` gives
`p(n_0-1)+j\le p(q-1)+j<pq`, using `j<p`). Reducing `p(n_0-1)+j=s_0q` mod
`p` gives `j\equiv s_0 q\equiv s_0 r\pmod p`, pinning `s_0` exactly as the
unique element of `\{1,\dots,p-1\}` with `s_0 r\equiv j\pmod p` (inverse
exists as `\gcd(r,p)=1`). Solving `p(n_0-1)+j=s_0q` for `n_0` gives the
stated affine formula.

**Independent verification (this review, fresh script).** Independently
re-derived the modular-inverse formula (`s_0 = j\cdot r^{-1} \bmod p`,
mapped into `\{1,\dots,p-1\}`) via `sympy.mod_inverse`, computed the full
table for `p=5` (all 12 `(j,r)` pairs), and cross-checked every entry
against a from-scratch brute-force search (own script, distinct method: for
an explicit smallest admissible prime `q` in each residue class, directly
searched for the least `n` with `q\mid(a_n+j)` and computed `K_0=(a_n+j)/q`)
— **exact match on all 12 entries** (e.g. `p=5,j=2,r=2,q=7`: formula gives
`s_0=1,K_0=6`; brute force gives `n_0=2,K_0=6`, matching). Also
independently re-verified the `p=3` specialization reproduces the certified
`a1-3q` theorem's constants (`K_0\in\{4,5\}`,
`n_0=(q+1)/3` or `(2q+1)/3`) exactly. No gap found in either lemma.

**Note on scope.** These two lemmas are the fully-proved, `p`-uniform
machinery underlying the `a1-pq-subfamily-theorem` approach. They do **not**
by themselves pin down the finite exceptional set `Bad(p)` for any specific
`p\ge5` (that requires an additional, not-yet-carried-out per-`p` finite
computation, exactly as `q=5` had to be found by hand for `p=3`) — see that
approach file for the honest scope statement.
