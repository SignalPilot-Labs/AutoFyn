## Status
solved (round 26: the `a_1=5q` subfamily theorem is fully proved — literal
`T=1,L=5` periodicity from `n=1` for every prime `q\ge7`, `q\notin
\mathrm{Bad}(5)=\{7,13,19\}` — by instantiating the certified `p`-uniform
machinery from `a1-pq-subfamily-theorem` at `p=5`, building the explicit
12-cell `(j,r)` table, closing it with the certified Legendre-Sieve/
Primorial-Floor toolkit, and hand-verifying every residual candidate. See
"Full proof" below.)

## Approaches tried
- (round 23, outline only, SUPERSEDED) Proposed a bespoke "j-generalized
  Parity Witness" mechanism (`\gcd(a_n+j,a_n)=\gcd(a_n+j,j)`, re-derived per
  `j` from scratch). Superseded — round 25's `a1-pq-subfamily-theorem`
  already proved a strictly more general, certified version of this exact
  identity (Generalized gcd-difference Witness Lemma), uniform in `p`.
- (round 26, this build) Instantiated the certified `p`-uniform reduction
  (`lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md`,
  together with the Case-(a)/(b) split derived in `a1-pq-subfamily-theorem`)
  at `p=5`: built the 12-cell `(j,r)` table (`j\in\{2,3,4\}`,
  `r\in\{1,2,3,4\}`), computed the `k=0` sufficient-window thresholds
  `Q_1(5,j,r)`, resolved every below-threshold `k=0` candidate by explicit
  witness search (finding exactly three genuine exceptions, matching
  `\mathrm{Bad}(5)=\{7,13,19\}` predicted by the round-26 explorer/outline-
  reviewer numeric scans), derived a fresh `s^*=5` threshold (the `p=5`
  analogue of the certified `a1-3q` closure's `s\ge4` threshold) for the
  `k\ge1` generic closure via the certified Legendre Sieve Gap Bound +
  Primorial Floor Bound, tabulated the residual band `k\in\{1,\dots,27\}`
  exactly, and resolved every one of the resulting below-threshold
  `(j,r,k,q)` quadruples with an explicit witness (all five non-moot cases
  resolve at `i=3`). **Result: the theorem is now completely proved.**

## Current best

### Target (now proved — see Full proof)
For every prime `q\ge7` with `q\notin\{7,13,19\}`, and `a_1=5q`:
`a_n=5(q+n-1)` for every `n\ge1` — literal `T=1,L=5` periodicity from
`n=1`.

## Full proof

### 0. Setup and imported machinery

Fix a prime `q\ge7`, `q\notin\{7,13,19\}`, and `a_1=5q`. Strong-induction
hypothesis at step `n`, `H(n)`: `a_i=5(q+i-1)` for `i=1,\dots,n`. In
particular `5\mid a_i` for every such `i`, and — since `5,q` are distinct
primes — `P(a_1)=\{5,q\}`.

We use, without re-derivation (both certified in
`lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md`, proved
there for a general odd prime `p`, and independently re-verified by the
round-25 proof-reviewer, including an explicit cross-check of the full
`p=5` table against brute force):

- **Lemma 1 (Generalized gcd-difference Witness Lemma).** For
  `N:=a_n+j`, `j\in\{1,\dots,4\}`, under `H(n)`: `\gcd(N,a_n)=\gcd(N,j)`.
- **Lemma 2 (Generalized `K_0`-Boundedness, `p=5`).** For `j\in\{2,3,4\}`
  and prime `q>5` with `q\equiv r\pmod5` (`r\in\{1,2,3,4\}`), the first
  index `n_0(j,r;q)` with `q\mid(a_{n_0}+j)` satisfies `K_0(j,r):=
  (a_{n_0}+j)/q=5+s_0(j,r)`, where `s_0(j,r)\in\{1,2,3,4\}` is the unique
  solution of `s_0\cdot r\equiv j\pmod5`, and
  `n_0(j,r;q)=1+\bigl(s_0(j,r)q-j\bigr)/5`.

We also use two further certified, self-contained lemmas from the `a1-3q`
closure (both `p`-independent statements about integers, reused verbatim):

- **Lemma 3 (Legendre Sieve Gap Bound, `lemmas/legendre-sieve-gap-bound.md`).**
  For integer `M\ge2` with `r:=\omega(M)`, any window of `L\ge2^r(r+1)`
  consecutive integers contains one coprime to `M`.
- **Lemma 4 (Primorial Floor Bound, `lemmas/primorial-floor-bound.md`).**
  If `\omega(M)=r` then `M\ge(r+1)!`.

### 1. Base case and the `j=1,5` bands

`n=1`: `a_1=5q=5(q+1-1)`, by definition.

Assume `H(n)`. We show `a_n+1,a_n+2,a_n+3,a_n+4` are all illegal and
`a_n+5` is legal, forcing `a_{n+1}=a_n+5=5(q+n)`, i.e. `H(n+1)`.

**`a_n+1` illegal.** Consecutive integers are coprime: `\gcd(a_n+1,a_n)=1`
— witnessed by `i=n`.

**`a_n+5` legal.** `a_n+5=5(q+n-1)+5=5(q+n)`. For every `i\le n`,
`\gcd(a_n+5,a_i)\ge\gcd\bigl(5(q+n),5(q+i-1)\bigr)\ge5>1` (both multiples of
`5`, by `H(n)`).

### 2. Illegality of `a_n+j`, `j\in\{2,3,4\}`: the Case (a)/(b) split

Fix `j\in\{2,3,4\}` and set `N:=a_n+j=5(q+n-1)+j`. Since `1\le j\le4`,
`N\equiv j\not\equiv0\pmod5`, so `5\nmid N`.

**Case (a): `q\nmid N`.** Any common divisor of `N` and `a_1=5q` divides
`5q`; since `5\nmid N` and (this case) `q\nmid N`, the only divisor of `5q`
dividing `N` is `1`: `\gcd(N,a_1)=1` — illegal, witnessed by `i=1`.

**Case (b): `q\mid N`.** Write `N=qK`, `K:=N/q\in\mathbb Z_{>0}`. For
`i=1`: `\gcd(N,a_1)=\gcd(N,5q)\ge q>1`, so `i=1` is never a witness here.
For `2\le i\le n`: `a_i=5(q+i-1)`; since `\gcd(N,5)=1`,
`\gcd(N,a_i)=\gcd(N,q+i-1)`. Writing `m:=q+i-1`: if `m<2q` (i.e.
`i-1<q`), `\gcd(m,q)=\gcd(i-1,q)=1`, so `\gcd(N,m)=\gcd(qK,m)=\gcd(K,m)`
(removing the coprime factor `q` cleanly). **In general (any `i`, not just
`m<2q`):** `\gcd(N,a_i)=\gcd(N,m)=\gcd(qK,m)`, so a witness at index `i`
exists iff `m=q+i-1` is coprime to `M:=qK=N`.

So: Case-(b) illegality of `a_n+j` reduces to finding, in the window
`m=q+1,\dots,q+n-1` (length `L:=n-1`, corresponding to `i=2,\dots,n`), an
integer coprime to `N=qK`.

By Lemma 2, the Case-(b) indices for band `j`, residue class `r:=q\bmod5`,
are exactly `n=n_0(j,r)+kq`, `k=0,1,2,\dots`, with `K(k):=K_0(j,r)+5k`.

### 3. The 12-cell table (`p=5`)

Solving `s_0\cdot r\equiv j\pmod5` for each `(j,r)`, `j\in\{2,3,4\}`,
`r\in\{1,2,3,4\}` (12 cells), gives:

| `j` | `r=1` | `r=2` | `r=3` | `r=4` |
|---|---|---|---|---|
| `2` | `s_0=2,K_0=7` | `s_0=1,K_0=6` | `s_0=4,K_0=9` | `s_0=3,K_0=8` |
| `3` | `s_0=3,K_0=8` | `s_0=4,K_0=9` | `s_0=1,K_0=6` | `s_0=2,K_0=7` |
| `4` | `s_0=4,K_0=9` | `s_0=2,K_0=7` | `s_0=3,K_0=8` | `s_0=1,K_0=6` |

(Independently checked against brute force: for the least admissible
prime `q\equiv r\pmod5` in each of the 12 classes, directly simulating
`a_n=5(q+n-1)` and searching for the least `n_0` with `q\mid(a_{n_0}+j)`
reproduces every `(n_0,K_0)` pair predicted by the formula, exactly.)

### 4. Closing `k=0`

**Sufficient-window criterion.** If `n_0(j,r)-1\ge K_0(j,r)`, the window
`m=q+1,\dots,q+n_0-1` (`n_0-1` consecutive integers, all `<2q` since
`n_0\le q`, hence automatically coprime to `q`) has length `\ge K_0(j,r)`,
so it contains a full residue system mod `K_0(j,r)`, hence an integer
coprime to `K_0(j,r)` — a witness. Substituting the explicit affine
formula for `n_0`, this holds for every prime `q\equiv r\pmod5` with
`q\ge Q_1(5,j,r):=\dfrac{5(K_0(j,r)+1)+j}{s_0(j,r)}`.

Computing `Q_1` for all 12 cells:

| `(j,r)` | `Q_1` | `(j,r)` | `Q_1` | `(j,r)` | `Q_1` |
|---|---|---|---|---|---|
| `(2,1)` | `21` | `(3,1)` | `16` | `(4,1)` | `13.5` |
| `(2,2)` | `37` | `(3,2)` | `13.25` | `(4,2)` | `22` |
| `(2,3)` | `13` | `(3,3)` | `38` | `(4,3)` | `16.33` |
| `(2,4)` | `15.67` | `(3,4)` | `21.5` | `(4,4)` | `39` |

For each cell, the primes `q\equiv r\pmod5`, `q\ge7`, with `q<Q_1(j,r)`
are exactly:

`(2,1)`: `\{11\}`; `(2,2)`: `\{7,17\}`; `(2,3)`: `\emptyset`;
`(2,4)`: `\emptyset`; `(3,1)`: `\{11\}`; `(3,2)`: `\{7\}`;
`(3,3)`: `\{13,23\}`; `(3,4)`: `\{19\}`; `(4,1)`: `\{11\}`;
`(4,2)`: `\{7,17\}`; `(4,3)`: `\{13\}`; `(4,4)`: `\{19,29\}`.

**Direct resolution of every below-threshold `k=0` candidate.** For each
pair above, compute `n_0`, `N=a_{n_0}+j=qK_0`, and search `i=1,\dots,n_0`
for `\gcd(N,a_i)=1`:

- `(j,r,q)=(2,1,11)`: `n_0=5`, `N=77`. `a_2=55`, `\gcd(77,55)=11`;
  `a_3=60`, `\gcd(77,60)=1` — **witness `i=3`**.
- `(2,2,7)`: `n_0=2`, `N=42`. `a_1=35,\gcd(42,35)=7`; `a_2=40,
  \gcd(42,40)=2`. **No witness among `i=1,2`.**
- `(2,2,17)`: `n_0=4`, `N=102`. `a_3=5(17+2)=95,\gcd(102,95)=1` —
  **witness `i=3`**.
- `(3,1,11)`: `n_0=7`, `N=88`. `a_3=5(11+2)=65,\gcd(88,65)=1` —
  **witness `i=3`**.
- `(3,2,7)`: `n_0=6`, `N=63`. `a_2=5(7+1)=40,\gcd(63,40)=1` —
  **witness `i=2`**.
- `(3,3,13)`: `n_0=3`, `N=78`. `a_1=65,\gcd(78,65)=13`;
  `a_2=70,\gcd(78,70)=2`; `a_3=75,\gcd(78,75)=3`. **No witness among
  `i=1,2,3`.**
- `(3,3,23)`: `n_0=5`, `N=138`. `a_3=5(23+2)=125,\gcd(138,125)=1` —
  **witness `i=3`**.
- `(3,4,19)`: `n_0=8`, `N=133`. `a_2=5(19+1)=100,\gcd(133,100)=1` —
  **witness `i=2`**.
- `(4,1,11)`: `n_0=9`, `N=99`. `a_3=5(11+2)=65,\gcd(99,65)=1` —
  **witness `i=3`**.
- `(4,2,7)`: `n_0=3`, `N=49`. `a_2=5(7+1)=40,\gcd(49,40)=1` —
  **witness `i=2`**.
- `(4,2,17)`: `n_0=7`, `N=119`. `a_2=5(17+1)=90,\gcd(119,90)=1` —
  **witness `i=2`**.
- `(4,3,13)`: `n_0=8`, `N=104`. `a_3=5(13+2)=75,\gcd(104,75)=1` —
  **witness `i=3`**.
- `(4,4,19)`: `n_0=4`, `N=114`. `a_1=95,\gcd(114,95)=19`;
  `a_2=5(19+1)=100,\gcd(114,100)=2`; `a_3=5(19+2)=105,\gcd(114,105)=3`.
  **No witness among `i=1,2,3`.**
- `(4,4,29)`: `n_0=6`, `N=174`. `a_3=5(29+2)=155,\gcd(174,155)=1` —
  **witness `i=3`**.

So every below-threshold `k=0` candidate is resolved by an explicit
witness **except three**: `(j,r,q)=(2,2,7)`, `(3,3,13)`, `(4,4,19)`, at
`n_0=2,3,4` respectively. Since `q\ge Q_1(j,r)` closes every other prime in
each class automatically (by the sufficient-window criterion above), and
every prime `q\equiv r\pmod5, q\ge7` not listed above already satisfies
`q\ge Q_1(j,r)`, **the `k=0` case is now completely settled**: it closes
for every `q\ge7,q\notin\{7,13,19\}`, with the three exceptional primes
identified exactly.

### 5. Closing `k\ge1`

Fix a Case-(b) index `n=n_0(j,r)+kq`, `k\ge1`. As derived in §2,
`K(k)=K_0(j,r)+5k`, `N=qK(k)`, and a witness exists whenever the window
`m=q+1,\dots,q+n-1` (length `L:=n-1\ge kq\ge7k`, using `q\ge7` and
`n_0\ge1`) contains an integer coprime to `M:=qK(k)`. By Lemma 3, this
holds once `L\ge2^{r^*}(r^*+1)`, `r^*:=\omega(qK(k))\le\omega(K(k))+1`
(adjoining at most the one prime `q`).

**Threshold `s^*=5` for the large-`\omega(K)` regime.** Suppose
`s:=\omega(K(k))\ge5`. By Lemma 4, `K(k)\ge(s+1)!`. Since `K_0(j,r)\le9`
for every cell (the table in §3 shows `K_0\in\{6,7,8,9\}`),
`5k=K(k)-K_0(j,r)\ge(s+1)!-9`. We claim `(s+1)!\ge9+\tfrac57\cdot
2^{s+1}(s+2)` for every `s\ge5`:

- *Base case `s=5`:* `6!=720`; RHS `=9+\tfrac57\cdot2^6\cdot7=9+320=329`;
  `720\ge329`. ✓.
- *Inductive step `s\to s+1` (`s\ge1`, so valid from `s=5` on):* if
  `(s+1)!\ge9+\tfrac57 2^{s+1}(s+2)` then, multiplying by `(s+2)>0`,
  `(s+2)!\ge9(s+2)+\tfrac57 2^{s+1}(s+2)^2`. We need
  `(s+2)!\ge9+\tfrac57 2^{s+2}(s+3)`. It suffices that
  `9(s+2)-9+\tfrac57 2^{s+1}\bigl[(s+2)^2-2(s+3)\bigr]\ge0`, i.e.
  `9(s+1)+\tfrac57 2^{s+1}(s^2+2s-2)\ge0`. Since `s^2+2s-2\ge0` for
  `s\ge1` (`1+2-2=1\ge0` at `s=1`, increasing thereafter) and `s+1>0`,
  both terms are `\ge0`. ✓.

So `(s+1)!\ge9+\tfrac57 2^{s+1}(s+2)` for all `s\ge5`, giving
`5k\ge(s+1)!-9\ge\tfrac57 2^{s+1}(s+2)`, i.e. `7k\ge2^{s+1}(s+2)`. Since
`r^*\le s+1`, `2^{r^*}(r^*+1)\le2^{s+1}(s+2)\le7k\le L`: **Lemma 3
applies**, giving a witness, whenever `\omega(K(k))\ge5` — no further
restriction on `k`, `j`, `r`, or `q` needed.

**Generic bound for `\omega(K(k))\le4`.** Then `r^*\le5`, so
`2^{r^*}(r^*+1)\le2^5\cdot6=192`. Since `L\ge7k`, `L\ge192` once `k\ge28`
(`7\cdot28=196\ge192`). So **for every `k\ge28`**, either
`\omega(K(k))\ge5` (handled above) or `\omega(K(k))\le4` (this generic
bound applies): in both cases Lemma 3 gives a witness, uniformly across
every cell and every admissible `q`.

**The residual band `k\in\{1,\dots,27\}`.** For `k\le27`, `K(k)=K_0+5k
\le9+135=144<720=6!`; by Lemma 4 (contrapositive), `\omega(K(k))\ge5`
would force `K(k)\ge720`, impossible — so `\omega(K(k))\le4` automatically
throughout this range (no case is missed). Direct computation of
`K(k)=K_0+5k` and `\omega(K(k))` for `K_0\in\{6,7,8,9\}`, `k=1,\dots,27`
(108 values) shows `\omega(K(k))\le3` throughout this entire residual
band (verified by direct factorization of every one of the 108 values).
Using the generic bound `r^*\le\omega(K(k))+1\le4`,
`2^{r^*}(r^*+1)\le2^4\cdot5=80` for every one of these `(K_0,k)` pairs,
and solving `L(q)\ge80` (with `L(q)=n_0(j,r)-1+kq` an explicit, strictly
increasing affine function of `q` for fixed `j,r,k`) gives an explicit
threshold `q_{\mathrm{thresh}}(j,r,k)` for each of the `12\times27=324`
cell/k combinations; by monotonicity of `L(q)` in `q`, every prime
`q\equiv r\pmod5` with `q\ge q_{\mathrm{thresh}}(j,r,k)` is closed
automatically.

Direct computation of all 324 thresholds (using the exact, tighter bound
`2^{\omega(K(k))+1}(\omega(K(k))+2)`, not just the crude `80`, in every
cell) finds that only **13** of the 324 `(j,r,k)` combinations have any
prime below threshold, and every listed prime is one of `\{7,11,13,17,
19\}`:

`(2,1,1)`: `\{11\}`; `(2,2,1)`: `\{7\}`; `(2,2,3)`: `\{7\}`;
`(2,2,4)`: `\{7\}`; `(2,3,1)`: `\{13\}`; `(3,1,2)`: `\{11\}`;
`(3,2,1)`: `\{7,17\}`; `(3,2,3)`: `\{7\}`; `(3,4,1)`: `\{19\}`;
`(4,1,1)`: `\{11\}`; `(4,2,1)`: `\{7,17\}`; `(4,2,3)`: `\{7\}`;
`(4,2,7)`: `\{7\}`.

**Every instance with `q\in\{7,13,19\}` is moot.** These `q` are already
established (§4) to deviate from the closed form at their respective
`n_0=2,3,4`; once the sequence has deviated, `H(n)` no longer holds for
`n` beyond that point, so no Case-(b), `k\ge1` occurrence for these three
primes is ever actually reached under the hypothesis `H(n)` — these
listed instances (all with `k\ge1`, hence `n>n_0`) are vacuous for the
theorem's scope (which excludes `q\in\{7,13,19\}` from the outset).
Concretely: for `q=7`, `n_0=2`; the flagged `k\ge1` instances above (in
cells `(2,2),(3,2),(4,2)`) all have `n=n_0+kq\ge2+7=9>2`. For `q=13`,
`n_0=3` (cell `(3,3)`); the flagged instance `(2,3,1)` has
`n=n_0(2,3)+13=11+13=24>3`. For `q=19`, `n_0=4` (cell `(4,4)`); the
flagged instance `(3,4,1)` has `n=n_0(3,4)+19=8+19=27>4`. So none of
these apply to the theorem's actual claim.

**The remaining five non-moot instances,** all with `q\in\{11,17\}$,
resolved by explicit witness search over the full range `i=1,\dots,n`:

- `(j,r,k,q)=(2,1,1,11)`: `n=16`, `N=132=q\cdot K`, `K=12`. `a_3=60,
  \gcd(132,60)=12`... checking systematically, `a_3=5(11+2)=65`
  wait recompute: `a_i=5(q+i-1)=5(11+i-1)=5(10+i)`. `a_3=65`,
  `\gcd(132,65)=1` — **witness `i=3`**.
- `(3,1,2,11)`: `n=29`, `N=198`, `K=18`. `a_3=65`, `\gcd(198,65)=1` —
  **witness `i=3`**.
- `(4,1,1,11)`: `n=20`, `N=154`, `K=14`. `a_3=65`, `\gcd(154,65)=1` —
  **witness `i=3`**.
- `(3,2,1,17)`: `n=31`, `N=238`, `K=14`. `a_3=5(17+2)=95`,
  `\gcd(238,95)=1` — **witness `i=3`**.
- `(4,2,1,17)`: `n=24`, `N=204`, `K=12`. `a_3=95`, `\gcd(204,95)=1` —
  **witness `i=3`**.

(Every one of these five was independently recomputed directly:
`N=qK(k)` was checked to equal `a_n+j` exactly for the stated `n`, and
`\gcd(N,a_3)` was computed by hand/exact arithmetic in each case,
confirming `\gcd=1`.)

**Conclusion of §5.** For every prime `q\ge7,q\notin\{7,13,19\}`, every
band `j\in\{2,3,4\}`, and every `k\ge1`: a Case-(b) witness for the
illegality of `a_n+j` (`n=n_0(j,r)+kq`) exists — either via Lemma 3
directly (`k\ge28`, or `k\le27` with `q\ge q_{\mathrm{thresh}}(j,r,k)`),
or via one of the five explicit witnesses above. This closes Case (b),
`k\ge1`, completely, for every `q` in the theorem's scope.

### 6. Assembly

Combining §1 (base case, `a_n+1` illegal, `a_n+5` legal), §2 (Case (a)
illegality), §4 (`k=0` closure for `q\notin\{7,13,19\}`), and §5 (`k\ge1`
closure for every admissible `q`): for every prime `q\ge7,q\notin
\{7,13,19\}$ and every `n\ge1` with `H(n)` holding, `a_n+1,\dots,a_n+4`
are all illegal and `a_n+5` is legal, so minimality of the greedy rule
forces `a_{n+1}=a_n+5=5(q+n)=5(q+(n+1)-1)`, establishing `H(n+1)`.

By strong induction, `H(n)` holds for every `n\ge1`:
`$$a_n=5(q+n-1)\quad\text{for all }n\ge1,$$`
i.e. literal `T=1,L=5` periodicity from `n=1`, for every prime `q\ge7`,
`q\notin\{7,13,19\}`. **This proves the theorem.** `∎`

### 7. `\mathrm{Bad}(5)=\{7,13,19\}` are genuine, permanent exceptions

For each of `q\in\{7,13,19\}`, §4 exhibited the precise mechanism: at the
first Case-(b) occurrence of the relevant band (`n_0=2,3,4` respectively),
the finite window of available witness candidates `i=1,\dots,n_0` is
**exhausted with no coprime index** — every candidate `a_i` shares a
prime factor with `N=a_{n_0}+j`:

- **`q=7`** (`n_0=2,j=2`): `N=42=2\cdot3\cdot7`. `a_1=35=5\cdot7`
  (shares `7`), `a_2=40=2^3\cdot5$ (shares `2`). No witness ⟹ `a_2+2=42`
  is legal; since `a_2+1=41` is illegal (consecutive), `a_3=42`, breaking
  the pattern (predicted `a_3=45`).
- **`q=13`** (`n_0=3,j=3`): `N=78=2\cdot3\cdot13`. `a_1=65=5\cdot13`
  (shares `13`), `a_2=70=2\cdot5\cdot7` (shares `2`), `a_3=75=3\cdot5^2`
  (shares `3`). No witness ⟹ `a_3+3=78` legal; `a_3+1,a_3+2` both illegal
  (`a_3+1=76$ consecutive; `a_3+2=77=7\cdot11`, `5\nmid77`, `13\nmid77`,
  so Case (a) applies, `\gcd(77,a_1)=\gcd(77,65)=1$ — illegal via `i=1`).
  So `a_4=78`, breaking the pattern (predicted `80`).
- **`q=19`** (`n_0=4,j=4`): `N=114=2\cdot3\cdot19`. `a_1=95=5\cdot19`
  (shares `19`), `a_2=100=2^2\cdot5^2` (shares `2`), `a_3=105=3\cdot5\cdot7`
  (shares `3`). No witness ⟹ `a_4+4=114` legal; `a_4+1,a_4+2,a_4+3` all
  illegal (`a_4+1=110` consecutive; `a_4+2=112=2^4\cdot7`, `5\nmid112`,
  `19\nmid112`, Case (a), `\gcd(112,95)=1` via `i=1`; `a_4+3=113` prime,
  `5\nmid113,19\nmid113`, Case (a), `\gcd(113,95)=1` via `i=1`). So
  `a_5=114`, breaking the pattern (predicted `115`).

This is a complete, mechanism-level (not merely numeric) proof that
`q=7,13,19` are genuine, permanent exceptions to the `T=1,L=5` literal
periodicity claim, in exact analogy with the certified `a1-3q` theorem's
`q=5` exclusion (a small finite witness window, exhausted with no
coprime candidate).

**Independent numerical confirmation.** Direct greedy re-simulation
(fresh script, correct legality rule: `a_{n+1}` least integer `>a_n` with
`\gcd(a_{n+1},a_i)>1` for every `i\le n`) for every prime `q\in[7,2000)`,
`60` terms each: **matches** `a_n=5(q+n-1)` in every term for every prime
except `q=7,13,19`, which deviate exactly at `n=3,4,5$ respectively
(`a_3=42\ne45`; `a_4=78\ne80`; `a_5=114\ne115`) — matching the mechanism
above exactly, digit for digit.

## Promotable lemmas

**`p=5` `K_0`-boundedness table (12 cells).** The explicit table in §3
above (`s_0(j,r),K_0(j,r)$ for all `j\in\{2,3,4\},r\in\{1,2,3,4\}`),
derived by direct instantiation of the certified Generalized
`K_0`-Boundedness Lemma at `p=5`, independently cross-checked against
brute force. Reusable by any future approach needing the `a_1=5q$ or
`a_1=5q^m$-type family's exact constants without re-deriving the
modular-inverse computation.

**`s^*=5` threshold and its induction (§5).** The inequality
`(s+1)!\ge9+\tfrac57\cdot2^{s+1}(s+2)` for `s\ge5`, proved by an explicit
base case and induction (using `s^2+2s-2\ge0$ for `s\ge1`, the same
sub-fact used in the certified Primorial Floor Bound's own corollary).
This is the `p=5`-specific analogue of the certified `a1-3q` closure's
`s\ge4` threshold (there the bound used `K_0\le5`; here `K_0\le9$, which
is why the threshold shifts from `s^*=4` to `s^*=5`). Reusable as a
template for any future `a1-pq`-family closure at other values of `p`
(the threshold `s^*(p)` will need re-deriving against the specific
`\max K_0=2p-1` for that `p`, but the induction structure transfers
directly).

**`Bad(5)=\{7,13,19\}`, proved genuine (§7).** The exact mechanism-level
exclusion proof (finite witness window exhausted with no coprime
candidate) for all three exceptions, fully explicit (not merely a numeric
observation). Reusable as the certified `a_1=5q` companion to the
certified `a1-3q` theorem, and as the base case confirming the round-26
"Minimal-Window Necessity" pattern noted in `a1-pq-subfamily-theorem`
(all three exceptions occur at `s_0(j,r)=1$ cells: `(2,2)`,`(3,3)`,`(4,4)`
— the minimal-`K_0=6$ cells — consistent with, though this file does not
attempt to prove, that conjecture).
