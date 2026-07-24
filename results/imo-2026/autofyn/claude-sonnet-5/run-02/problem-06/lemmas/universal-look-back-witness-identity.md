## Lemma: Universal Look-Back Witness Identity, and its `r=1` Corollary (CERTIFIED, round 27)

**Source.** `a1-pq-subfamily-theorem`, round 27. Independently re-verified
in full by the round-27 proof-reviewer.

**Depends on (certified).**
`lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md` (uses the
same setup: `a_1=pq`, induction hypothesis `H(n)`, and the `K_0`-boundedness
constants `s_0(j,r)`, `n_0(j,r;q)`).

### Lemma (Universal Look-Back Witness Identity)

**Statement.** Fix odd prime `p`, prime `q>p`, `a_1=pq`, and suppose the
strong induction hypothesis `H(n)`: `a_i=p(q+i-1)` holds for `i=1,\dots,n`.
For `j\in\{1,\dots,p-1\}`, let `N:=a_n+j`. Then for every `i\in\{1,\dots,n\}`,
```
gcd(N,a_i) = gcd( p(n-i)+j , q+i-1 ).
```

**Proof.** `N-a_i = (p(q+n-1)+j) - p(q+i-1) = p(n-i)+j =: M`. By
`gcd(x,y)=gcd(y,x-y)`, `gcd(N,a_i)=gcd(a_i,M)=gcd(p(q+i-1),M)`. Since
`M\equiv j\pmod p` and `0<j<p`, `\gcd(M,p)=\gcd(j,p)=1` (`p` prime). Hence,
since `p` and `M` are coprime, `\gcd(p(q+i-1),M)=\gcd(q+i-1,M)` (standard
fact: `\gcd(b,c)=1\Rightarrow\gcd(ab,c)=\gcd(a,c)`). Combining,
`\gcd(N,a_i)=\gcd(q+i-1,\,p(n-i)+j)`. `\blacksquare`

**Consistency with the certified Generalized gcd-difference Witness
Lemma.** At `i=n` (look-back distance `0`), the identity gives
`\gcd(N,a_n)=\gcd(j,\,q+n-1)`. This is consistent with (not a
contradiction of) the certified `\gcd(N,a_n)=\gcd(N,j)`: since
`\gcd(p,j)=1` (`j<p`, `p` prime), `\gcd(N,j)=\gcd(p(q+n-1)+j,j)=
\gcd(p(q+n-1),j)=\gcd(q+n-1,j)` by the same coprime-scaling fact, matching
the new identity's `i=n` specialization exactly.

### Corollary (`r=1` unconditional closure)

**Setup.** Fix odd prime `p`, prime `q\equiv1\pmod p`, `q>p`. Write
`q=pt+1`; since `q` is odd (prime `>2`) and `p` is odd, `t` is forced even,
`t\ge2`. By the certified `K_0`-Boundedness Lemma at `r=1`, `s_0(j,1)=j`
exactly (no modular reduction needed, since `j\in\{2,\dots,p-1\}` is
already in the residue range), so the `k`-th Case-(b) risk index of band
`j` is `n=n_0(j)+kq=1+jt+kq`.

**Statement.** For every `k\ge0`, taking `i=n` (look-back distance `0`) in
the identity above gives
```
gcd(N,a_n) = gcd(j, q+n-1) = gcd(k+1, j).
```
In particular: (i) at `k=0`, `\gcd(N,a_n)=\gcd(1,j)=1` always — `i=n` is
an unconditional witness for the illegality of `a_n+j`, for every `p`,
every band `j`, every admissible `q\equiv1\pmod p`, with no threshold and
no per-`p` computation. (ii) More generally, whenever `\gcd(k+1,j)=1`
(not just `k=0`), the same witness applies unconditionally.

**Proof.** `q+n-1=q+jt+kq=(k+1)q+jt`. Since `jt\equiv0\pmod j`,
`\gcd(j,(k+1)q+jt)=\gcd(j,(k+1)q)`. Since `q` is prime and `q>p>j` (so
`q\nmid j`), `\gcd(q,j)=1`; hence `\gcd(j,(k+1)q)=\gcd(j,k+1)` by the same
coprime-scaling fact. `\blacksquare`

**Independent verification (this review).** (1) Re-derived the identity's
algebra from scratch and confirmed the coprime-scaling step
(`\gcd(b,c)=1\Rightarrow\gcd(ab,c)=\gcd(a,c)`) is a standard, valid fact,
applied correctly in both the general identity and the `r=1` corollary. (2)
Independently checked the general identity against **66,976** direct
`(p,q,j,n,i)` instances (`p\in\{5,7,11,13\}`, `q<p+400` prime,
`j\in\{1,\dots,p-1\}`, `n\le7`, `i\le n`, computing `a_i=p(q+i-1)`
directly): **zero mismatches**. (3) Independently checked the `r=1`
corollary's closed form `\gcd(N,a_n)=\gcd(k+1,j)` against 30 sampled
`(p,q,j,k)` instances (`p\in\{5,7,11,13\}`, `q\equiv1\pmod p` prime,
`t\in\{2,4,\dots,38\}`, `j\in\{2,\dots,p-1\}`, `k\in\{0,\dots,4\}`), all
exact matches. (4) Independently confirmed the file's auxiliary claim that
look-back distance `d=k+1` (`i=n-(k+1)`) is **never** a witness (the
identity gives `\gcd(N,a_i)=K(k):=p(k+1)+j>1` always) against 20 further
sampled instances, exact match in every case.

**Status.** Correct, complete, fully general (works for every odd prime
`p`, every `j\in\{1,\dots,p-1\}`, every look-back distance, and — for the
Corollary — every `q\equiv1\pmod p$). The Corollary gives a genuine,
unconditional (threshold-free, per-`p`-computation-free) closure of the
entire `k=0` layer of the `r=1` residue class for the general `a_1=pq`
family, plus every `(j,k)` cell with `\gcd(k+1,j)=1`. **Does NOT** resolve
the residual `k\ge1,\gcd(k+1,j)>1` cells — this remains open (see
`a1-pq-subfamily-theorem` for the honestly-scoped residual gap). Certified
as a standalone, reusable, general-purpose lemma.
