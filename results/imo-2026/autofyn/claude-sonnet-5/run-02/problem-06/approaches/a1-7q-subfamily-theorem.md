## Status
solved (round 27: the `a_1=7q` subfamily theorem is fully proved — literal
`T=1,L=7` periodicity from `n=1` for every prime `q\ge11`, `q\notin
\mathrm{Bad}(7)=\{11,13\}`, by instantiating the certified `p`-uniform
machinery from `a1-pq-subfamily-theorem` at `p=7`, building the explicit
30-cell `(j,r)` table, closing it with the certified Legendre-Sieve/
Primorial-Floor toolkit, and hand-verifying every residual candidate — the
same template as the certified `a1-5q-subfamily-theorem`, scaled to `p=7`.
See "Full proof" below.)

## Approaches tried
- (round 26, outline only) Proposed the `a_1=7q` target, `q\ge11` prime,
  via the same certified `p`-uniform machinery instantiated at `p=7`
  (30 cells instead of `a1-5q`'s 12). Held out of round 26's build set for
  capacity reasons only.
- (round 27, this build) Instantiated the certified `p`-uniform reduction
  (`lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md`,
  Case-(a)/(b) split) at `p=7`: built the full 30-cell `(j,r)` table
  (`j\in\{2,\dots,6\}`, `r\in\{1,\dots,6\}`), computed the `k=0`
  sufficient-window thresholds `Q_1(7,j,r)` for all 30 cells, resolved
  every one of the 29 below-threshold `k=0` candidates by explicit witness
  search (27 resolve, exactly 2 genuine exceptions: `(j,r,q)=(4,4,11)` and
  `(6,6,13)`, matching `\mathrm{Bad}(7)=\{11,13\}`), derived a fresh
  `s^*=5` threshold (analogous to `a1-5q`'s, with the `p=7`-specific
  constants `K_0\le13`, `q\ge11`) for the `k\ge1` generic closure, isolated
  the residual band `k\in\{1,\dots,17\}` (using the exact computation that
  `\omega(K(k))\le3` throughout, forced by `K(k)\le132<720=6!`), reduced
  the resulting below-threshold list to 20 `(j,r,k,q)` quadruples (all with
  `q\in\{11,13,17,19,23\}`), showed 11 of these are moot (`q\in\{11,13\}`,
  already excluded/deviated by the `k=0` step), and resolved the remaining
  9 genuine quadruples with explicit witnesses. **Result: the theorem is
  now completely proved.**

## Current best

### Target (now proved — see Full proof)
For every prime `q\ge11` with `q\notin\{11,13\}`, and `a_1=7q`:
`a_n=7(q+n-1)` for every `n\ge1` — literal `T=1,L=7` periodicity from
`n=1`.

## Full proof

### 0. Setup and imported machinery

Fix a prime `q\ge11`, `q\notin\{11,13\}`, and `a_1=7q`. Strong-induction
hypothesis at step `n`, `H(n)`: `a_i=7(q+i-1)` for `i=1,\dots,n`. In
particular `7\mid a_i` for every such `i`, and — since `7,q` are distinct
primes — `P(a_1)=\{7,q\}`.

We use, without re-derivation (both certified in
`lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md`, proved
there for a general odd prime `p`):

- **Lemma 1 (Generalized gcd-difference Witness Lemma).** For `N:=a_n+j`,
  `j\in\{1,\dots,6\}`, under `H(n)`: `\gcd(N,a_n)=\gcd(N,j)`.
- **Lemma 2 (Generalized `K_0`-Boundedness, `p=7`).** For `j\in\{2,\dots,6\}`
  and prime `q>7` with `q\equiv r\pmod7` (`r\in\{1,\dots,6\}`), the first
  index `n_0(j,r;q)` with `q\mid(a_{n_0}+j)` satisfies
  `K_0(j,r):=(a_{n_0}+j)/q=7+s_0(j,r)`, where `s_0(j,r)\in\{1,\dots,6\}`
  is the unique solution of `s_0\cdot r\equiv j\pmod7`, and
  `n_0(j,r;q)=1+(s_0(j,r)q-j)/7`.

We also reuse verbatim two further certified, `p`-independent lemmas
(originally from the `a1-3q` closure):

- **Lemma 3 (Legendre Sieve Gap Bound, `lemmas/legendre-sieve-gap-bound.md`).**
  For integer `M\ge2` with `r:=\omega(M)`, any window of `L\ge2^r(r+1)`
  consecutive integers contains one coprime to `M`.
- **Lemma 4 (Primorial Floor Bound, `lemmas/primorial-floor-bound.md`).**
  If `\omega(M)=r` then `M\ge(r+1)!`.

### 1. Base case and the `j=1,7` bands

`n=1`: `a_1=7q=7(q+1-1)`, by definition.

Assume `H(n)`. We show `a_n+1,\dots,a_n+6` are all illegal and `a_n+7` is
legal, forcing `a_{n+1}=a_n+7=7(q+n)`, i.e. `H(n+1)`.

**`a_n+1` illegal.** `\gcd(a_n+1,a_n)=1` (consecutive integers), witnessed
by `i=n`.

**`a_n+7` legal.** `a_n+7=7(q+n-1)+7=7(q+n)`. For every `i\le n`,
`\gcd(a_n+7,a_i)\ge\gcd(7(q+n),7(q+i-1))\ge7>1` (both multiples of `7`, by
`H(n)`).

### 2. Illegality of `a_n+j`, `j\in\{2,\dots,6\}`: the Case (a)/(b) split

Fix `j\in\{2,\dots,6\}` and `N:=a_n+j=7(q+n-1)+j`. Since `1\le j\le6`,
`N\equiv j\not\equiv0\pmod7`, so `7\nmid N`.

**Case (a): `q\nmid N`.** Any common divisor of `N` and `a_1=7q` divides
`7q`; since `7\nmid N` and `q\nmid N`, the only such divisor is `1`:
`\gcd(N,a_1)=1` — illegal, witnessed by `i=1`.

**Case (b): `q\mid N`.** Write `N=qK`, `K:=N/q\in\mathbb Z_{>0}`. For
`i=1`: `\gcd(N,a_1)=\gcd(N,7q)\ge q>1`, never a witness here. For
`2\le i\le n`: since `\gcd(N,7)=1`, writing `m:=q+i-1`,
`\gcd(N,a_i)=\gcd(N,m)=\gcd(qK,m)`. So Case-(b) illegality of `a_n+j`
reduces to finding, in the window `m=q+1,\dots,q+n-1` (length `L:=n-1`,
`i=2,\dots,n`), an integer coprime to `N=qK`.

By Lemma 2, the Case-(b) indices for band `j`, residue `r:=q\bmod7`, are
exactly `n=n_0(j,r)+kq`, `k=0,1,2,\dots`, with `K(k):=K_0(j,r)+7k`.

### 3. The 30-cell table (`p=7`)

Solving `s_0\cdot r\equiv j\pmod7` for each `(j,r)`, `j\in\{2,\dots,6\}`,
`r\in\{1,\dots,6\}` (30 cells):

| `j\backslash r` | `1` | `2` | `3` | `4` | `5` | `6` |
|---|---|---|---|---|---|---|
| `2` | `s_0=2,K_0=9` | `s_0=1,K_0=8` | `s_0=3,K_0=10` | `s_0=4,K_0=11` | `s_0=6,K_0=13` | `s_0=5,K_0=12` |
| `3` | `s_0=3,K_0=10` | `s_0=5,K_0=12` | `s_0=1,K_0=8` | `s_0=6,K_0=13` | `s_0=2,K_0=9` | `s_0=4,K_0=11` |
| `4` | `s_0=4,K_0=11` | `s_0=2,K_0=9` | `s_0=6,K_0=13` | `s_0=1,K_0=8` | `s_0=5,K_0=12` | `s_0=3,K_0=10` |
| `5` | `s_0=5,K_0=12` | `s_0=6,K_0=13` | `s_0=4,K_0=11` | `s_0=3,K_0=10` | `s_0=1,K_0=8` | `s_0=2,K_0=9` |
| `6` | `s_0=6,K_0=13` | `s_0=3,K_0=10` | `s_0=2,K_0=9` | `s_0=5,K_0=12` | `s_0=4,K_0=11` | `s_0=1,K_0=8` |

(Every diagonal cell `j=r` gives `s_0=1,K_0=8` exactly, matching the
certified Diagonal Characterization Lemma from `a1-pq-subfamily-theorem`.
Independently computed via `sympy.mod_inverse` this round and cross-checked
cell by cell against the round-27 math-explorer's and outline-reviewer's
independent recomputations — exact match, all three derivations agree.)

### 4. Closing `k=0`

**Sufficient-window criterion.** If `n_0(j,r)-1\ge K_0(j,r)`, the window
`m=q+1,\dots,q+n_0-1` (length `n_0-1`, all `<2q` since `n_0\le q`, hence
automatically coprime to `q`) contains a full residue system mod
`K_0(j,r)`, hence an integer coprime to `K_0(j,r)` — a witness.
Substituting the explicit affine formula for `n_0`, this holds for every
prime `q\equiv r\pmod7` with
`q\ge Q_1(7,j,r):=\dfrac{7(K_0(j,r)+1)+j}{s_0(j,r)}`.

Computing `Q_1` for all 30 cells:

| `(j,r)` | `Q_1` | `(j,r)` | `Q_1` | `(j,r)` | `Q_1` |
|---|---|---|---|---|---|
| `(2,1)` | `36` | `(3,1)` | `80/3\approx26.67` | `(4,1)` | `22` |
| `(2,2)` | `65` | `(3,2)` | `94/5=18.8` | `(4,2)` | `37` |
| `(2,3)` | `79/3\approx26.33` | `(3,3)` | `66` | `(4,3)` | `17` |
| `(2,4)` | `21.5` | `(3,4)` | `101/6\approx16.83` | `(4,4)` | `67` |
| `(2,5)` | `50/3\approx16.67` | `(3,5)` | `36.5` | `(4,5)` | `19` |
| `(2,6)` | `93/5=18.6` | `(3,6)` | `87/4=21.75` | `(4,6)` | `27` |
| `(5,1)` | `96/5=19.2` | `(6,1)` | `52/3\approx17.33` | | |
| `(5,2)` | `103/6\approx17.17` | `(6,2)` | `83/3\approx27.67` | | |
| `(5,3)` | `89/4=22.25` | `(6,3)` | `38` | | |
| `(5,4)` | `82/3\approx27.33` | `(6,4)` | `97/5=19.4` | | |
| `(5,5)` | `68` | `(6,5)` | `22.5` | | |
| `(5,6)` | `37.5` | `(6,6)` | `69` | | |

For each cell, the primes `q\equiv r\pmod7`, `q\ge11`, with `q<Q_1(j,r)`
give exactly **29** below-threshold `k=0` candidates
(`(j,r,q)`, independently confirmed by the round-27 math-explorer and
outline-reviewer, each with an independent script):

`(2,1,29)`; `(2,2,23)`; `(2,2,37)`; `(2,3,17)`; `(2,4,11)`; `(2,6,13)`;
`(3,3,17)`; `(3,3,31)`; `(3,3,59)`; `(3,4,11)`; `(3,5,19)`; `(3,6,13)`;
`(4,2,23)`; `(4,4,11)`; `(4,4,53)`; `(4,6,13)`; `(5,3,17)`; `(5,4,11)`;
`(5,5,19)`; `(5,5,47)`; `(5,5,61)`; `(5,6,13)`; `(6,2,23)`; `(6,3,17)`;
`(6,3,31)`; `(6,4,11)`; `(6,5,19)`; `(6,6,13)`; `(6,6,41)`.

**Direct resolution of every below-threshold `k=0` candidate.** For each
triple above, `n_0=1+(s_0q-j)/7`, `N=a_{n_0}+j=qK_0`; we search
`i=1,\dots,n_0` for `\gcd(N,a_i)=1` with `a_i=7(q+i-1)`:

- `(2,1,29)`: `n_0=9,N=261`. Witness `i=3` (`a_3=7\cdot31=217`,
  `\gcd(261,217)=1`).
- `(2,2,23)`: `n_0=4,N=184`. Witness `i=3` (`a_3=175`,
  `\gcd(184,175)=1`).
- `(2,2,37)`: `n_0=6,N=296`. Witness `i=3` (`a_3=273`,
  `\gcd(296,273)=1`).
- `(2,3,17)`: `n_0=8,N=170`. Witness `i=3` (`a_3=133`,
  `\gcd(170,133)=1`).
- `(2,4,11)`: `n_0=7,N=121`. Witness `i=2` (`a_2=84`,
  `\gcd(121,84)=1`).
- `(2,6,13)`: `n_0=10,N=156`. Witness `i=5` (`a_5=119`,
  `\gcd(156,119)=1`).
- `(3,3,17)`: `n_0=3,N=136`. Witness `i=3` (`a_3=133`,
  `\gcd(136,133)=1`).
- `(3,3,31)`: `n_0=5,N=248`. Witness `i=3` (`a_3=231`,
  `\gcd(248,231)=1`).
- `(3,3,59)`: `n_0=9,N=472`. Witness `i=3` (`a_3=427`,
  `\gcd(472,427)=1`).
- `(3,4,11)`: `n_0=10,N=143`. Witness `i=2` (`a_2=84`,
  `\gcd(143,84)=1`).
- `(3,5,19)`: `n_0=6,N=171`. Witness `i=2` (`a_2=140`,
  `\gcd(171,140)=1`).
- `(3,6,13)`: `n_0=8,N=143`. Witness `i=2` (`a_2=98`,
  `\gcd(143,98)=1`).
- `(4,2,23)`: `n_0=7,N=207`. Witness `i=3` (`a_3=175`,
  `\gcd(207,175)=1`).
- `(4,4,11)`: `n_0=2,N=88`. **No witness among `i=1,2`** — genuine
  exception (see §5).
- `(4,4,53)`: `n_0=8,N=424`. Witness `i=3` (`a_3=385`,
  `\gcd(424,385)=1`).
- `(4,6,13)`: `n_0=6,N=130`. Witness `i=5` (`a_5=119`,
  `\gcd(130,119)=1`).
- `(5,3,17)`: `n_0=10,N=187`. Witness `i=2` (`a_2=126`,
  `\gcd(187,126)=1`).
- `(5,4,11)`: `n_0=5,N=110`. Witness `i=3` (`a_3=7(11+2)=91`,
  `\gcd(110,91)=1`, since `110=2\cdot5\cdot11` and `91=7\cdot13` share no
  prime factor).
- `(5,5,19)`: `n_0=3,N=152`. Witness `i=3` (`a_3=7\cdot21=147`,
  `\gcd(152,147)=1`, since `152=2^3\cdot19` and `147=3\cdot7^2`).
- `(5,5,47)`: `n_0=7,N=376`. Witness `i=3` (`a_3=343`,
  `\gcd(376,343)=1`).
- `(5,5,61)`: `n_0=9,N=488`. Witness `i=3` (`a_3=7\cdot63=441`,
  `\gcd(488,441)=1`, since `488=2^3\cdot61` and `441=3^2\cdot7^2`).
- `(5,6,13)`: `n_0=4,N=117`. Witness `i=2` (`a_2=98`,
  `\gcd(117,98)=1`).
- `(6,2,23)`: `n_0=10,N=230`. Witness `i=5` (`a_5=189`,
  `\gcd(230,189)=1`).
- `(6,3,17)`: `n_0=5,N=153`. Witness `i=3` (`a_3=133`,
  `\gcd(153,133)=1`).
- `(6,3,31)`: `n_0=9,N=279`. Witness `i=2` (`a_2=224`,
  `\gcd(279,224)=1`).
- `(6,4,11)`: `n_0=8,N=132`. Witness `i=3` (`a_3=7\cdot13=91`,
  `\gcd(132,91)=1`, since `132=2^2\cdot3\cdot11` and `91=7\cdot13`).
- `(6,5,19)`: `n_0=11,N=209`. Witness `i=2` (`a_2=140`,
  `\gcd(209,140)=1`).
- `(6,6,13)`: `n_0=2,N=104`. **No witness among `i=1,2`** — genuine
  exception (see §5).
- `(6,6,41)`: `n_0=6,N=328`. Witness `i=3` (`a_3=301`,
  `\gcd(328,301)=1`).

(All 29 `\gcd` computations above were carried out exactly, using the
explicit values `a_i=7(q+i-1)` and `N=qK_0`, and independently
cross-checked this round by exact integer computation, via a script
re-verifying every one of the 29 witness/exception determinations against
a from-scratch `gcd` search.)

So every below-threshold `k=0` candidate resolves by an explicit witness
**except exactly two**: `(j,r,q)=(4,4,11)` at `n_0=2`, and `(6,6,13)` at
`n_0=2`. Every prime `q\equiv r\pmod7,q\ge11` not listed above already
satisfies `q\ge Q_1(j,r)`, hence closes automatically by the
sufficient-window criterion. **The `k=0` case is now completely settled**
for every `q\ge11,q\notin\{11,13\}`, with the two exceptional primes
identified exactly.

### 5. `\mathrm{Bad}(7)=\{11,13\}` are genuine, permanent exceptions

**`q=11`** (`j=4,r=4,n_0=2`): `N=a_2+4=88=2^3\cdot11`. Under `H(2)`,
`a_1=77=7\cdot11` (shares `11` with `N`), `a_2=84=2^2\cdot3\cdot7` (shares
`2` with `N`). No witness among `i=1,2` ⟹ `a_2+4=88` is legal. We must
also check `a_2+1,a_2+2,a_2+3` are illegal: `a_2+1=85=5\cdot17`,
`\gcd(85,77)=1` — illegal via `i=1`; `a_2+2=86=2\cdot43`,
`\gcd(86,77)=1` — illegal via `i=1`; `a_2+3=87=3\cdot29`,
`\gcd(87,77)=1` — illegal via `i=1`. So the least legal successor of
`a_2=84` is `88`, forcing `a_3=88`, **not** the predicted `7(11+2)=91`:
`H(3)` fails. `q=11` is a genuine, permanent exception.

**`q=13`** (`j=6,r=6,n_0=2`): `N=a_2+6=104=2^3\cdot13`. Under `H(2)`,
`a_1=91=7\cdot13` (shares `13`), `a_2=98=2\cdot7^2` (shares `2`). No
witness among `i=1,2` ⟹ `a_2+6=104` is legal. Checking
`a_2+1,\dots,a_2+5`: `a_2+1=99=3^2\cdot11`, `\gcd(99,91)=1` — illegal via
`i=1`; `a_2+2=100=2^2\cdot5^2`, `\gcd(100,91)=1` — illegal via `i=1`;
`a_2+3=101` (prime), `\gcd(101,91)=1` — illegal via `i=1`; `a_2+4=102=
2\cdot3\cdot17`, `\gcd(102,91)=1` — illegal via `i=1`; `a_2+5=103`
(prime), `\gcd(103,91)=1` — illegal via `i=1`. So the least legal
successor of `a_2=98` is `104`, forcing `a_3=104`, **not** the predicted
`7(13+2)=105`: `H(3)` fails. `q=13` is a genuine, permanent exception.

**Independent numerical confirmation.** Direct greedy re-simulation (fresh
script, literal legality rule) for every prime `q\in[11,2000)`, `60` terms
each: matches `a_n=7(q+n-1)` in every term for every prime except
`q=11,13`, which deviate exactly at `n=3` (`a_3=88\ne91`; `a_3=104\ne105`)
— matching the mechanism above digit for digit. (This was independently
re-verified by both the round-27 math-explorer and the round-27
outline-reviewer with separate scripts.)

### 6. Closing `k\ge1`

Fix a Case-(b) index `n=n_0(j,r)+kq`, `k\ge1`. As derived in §2,
`K(k)=K_0(j,r)+7k`, `N=qK(k)`, and a witness exists whenever the window
`m=q+1,\dots,q+n-1` (length `L:=n-1=n_0-1+kq\ge kq\ge11k`, using `q\ge11`
and `n_0\ge1`) contains an integer coprime to `M:=qK(k)`. By Lemma 3, this
holds once `L\ge2^{r^*}(r^*+1)`, `r^*:=\omega(qK(k))\le\omega(K(k))+1`.

**Threshold `s^*=5` for the large-`\omega(K)` regime.** Suppose
`s:=\omega(K(k))\ge5`. By Lemma 4, `K(k)\ge(s+1)!`. Since
`K_0(j,r)\le13` for every cell (the §3 table has `K_0\in\{8,\dots,13\}`),
`7k=K(k)-K_0(j,r)\ge(s+1)!-13`. We claim
`(s+1)!\ge13+\tfrac{7}{11}\cdot2^{s+1}(s+2)` for every `s\ge5`:

- *Base case `s=5`:* `6!=720`; RHS `=13+\tfrac7{11}\cdot64\cdot7=13+
  \tfrac{3136}{11}=13+285.0\overline{90}=298.0\overline{90}`; `720\ge
  298.09`. ✓.
- *Inductive step `s\to s+1` (`s\ge1`, hence valid from `s=5` on):* if
  `(s+1)!\ge13+\tfrac7{11}2^{s+1}(s+2)` then, multiplying by `(s+2)>0`,
  `(s+2)!\ge13(s+2)+\tfrac7{11}2^{s+1}(s+2)^2`. We need
  `(s+2)!\ge13+\tfrac7{11}2^{s+2}(s+3)`. It suffices that
  `13(s+2)-13+\tfrac7{11}2^{s+1}\bigl[(s+2)^2-2(s+3)\bigr]\ge0`, i.e.
  `13(s+1)+\tfrac7{11}2^{s+1}(s^2+2s-2)\ge0`. Since `s^2+2s-2\ge0` for
  `s\ge1` (`=1\ge0` at `s=1`, increasing thereafter) and `13(s+1)>0`, both
  terms are `\ge0`. ✓.

So `(s+1)!\ge13+\tfrac7{11}2^{s+1}(s+2)` for all `s\ge5`, giving
`7k\ge(s+1)!-13\ge\tfrac7{11}2^{s+1}(s+2)`, i.e. `11k\ge2^{s+1}(s+2)`.
Since `r^*\le s+1` and `x\mapsto2^x(x+1)` is increasing,
`2^{r^*}(r^*+1)\le2^{s+1}(s+2)\le11k\le L`: **Lemma 3 applies**, giving a
witness, whenever `\omega(K(k))\ge5` — no further restriction on `k,j,r,q`
needed.

**Generic bound for `\omega(K(k))\le4`.** Then `r^*\le5`, so
`2^{r^*}(r^*+1)\le2^5\cdot6=192`. Since `L\ge11k`, `L\ge192` once
`k\ge18` (`11\cdot18=198\ge192`; `11\cdot17=187<192`). So **for every
`k\ge18`**, either `\omega(K(k))\ge5` (handled above) or
`\omega(K(k))\le4` (this generic bound applies, since `k\ge18`): in both
cases Lemma 3 gives a witness, uniformly across every cell and every
admissible `q`.

**The residual band `k\in\{1,\dots,17\}`.** For `k\le17`, `K(k)=K_0+7k\le
13+119=132<720=6!`; by Lemma 4 (contrapositive), `\omega(K(k))\ge5`
would force `K(k)\ge720`, impossible — so `\omega(K(k))\le4`
automatically throughout this range. Direct computation of
`K(k)=K_0+7k` and `\omega(K(k))` for `K_0\in\{8,\dots,13\}`, `k=1,\dots,17`
(102 values total, `K_0` shared by all cells with that value) shows
`\omega(K(k))\le3` throughout this entire residual band (verified by
direct factorization of every one of the 102 values).

Using the exact, tighter bound `2^{\omega(K(k))+1}(\omega(K(k))+2)` (not
the crude `192`) per `(j,r,k)` combination, and solving `L(q)\ge` this
bound (with `L(q)=n_0(j,r)-1+kq` an explicit, strictly increasing affine
function of `q`) gives an explicit threshold
`q_{\mathrm{thresh}}(j,r,k)` for each of the `30\times17=510` cell/`k`
combinations. Direct computation of all 510 thresholds finds that only
**20** `(j,r,k,q)` combinations have any prime below threshold:

`(2,2,1,23)`; `(2,4,1,11)`; `(3,3,1,17)`; `(3,4,1,11)`; `(3,5,3,19)`;
`(3,6,1,13)`; `(4,2,3,23)`; `(4,3,1,17)`; `(4,4,1,11)`; `(4,4,2,11)`;
`(4,6,2,13)`; `(5,3,1,17)`; `(5,4,2,11)`; `(5,5,1,19)`; `(5,6,3,13)`;
`(6,3,3,17)`; `(6,4,2,11)`; `(6,5,1,19)`; `(6,6,1,13)`; `(6,6,2,13)`.

**11 of these 20 are moot: `q\in\{11,13\}`.** By §5, `q=11,13` are
already established to deviate from the closed form at `n_0=2,2`
respectively (with `H(n)` failing already at `n=3`); every listed
instance with `q\in\{11,13\}` has `n=n_0(j,r)+kq\ge3` far in excess of the
point of deviation (explicitly: `(2,4,1,11)\Rightarrow n=7+11=18`;
`(3,4,1,11)\Rightarrow n=10+11=21`; `(3,6,1,13)\Rightarrow n=8+13=21`;
`(4,4,1,11)\Rightarrow n=2+11=13`; `(4,4,2,11)\Rightarrow n=2+22=24`;
`(4,6,2,13)\Rightarrow n=6+26=32`; `(5,4,2,11)\Rightarrow n=5+22=27`;
`(5,6,3,13)\Rightarrow n=4+39=43`; `(6,4,2,11)\Rightarrow n=8+22=30`;
`(6,6,1,13)\Rightarrow n=2+13=15`; `(6,6,2,13)\Rightarrow n=2+26=28`; all
`\ge13\ge3`), so `H(n)` does not hold at these `n` for `q=11,13` — these
instances are vacuous for the theorem's scope (which excludes `q=11,13`
from the outset).

**The remaining 9 non-moot instances**, all with `q\in\{17,19,23\}`,
resolved by explicit witness search over the full range `i=1,\dots,n`:

- `(2,2,1,23)`: `n_0=4,n=27,K=15,N=345=q\cdot15`. `a_4=7(23+3)=182`,
  `\gcd(345,182)=1` — **witness `i=4`**.
- `(3,3,1,17)`: `n_0=3,n=20,K=15,N=255`. `a_3=7(17+2)=133`,
  `\gcd(255,133)=1` — **witness `i=3`**.
- `(3,5,3,19)`: `n_0=6,n=63,K=30,N=570`. `a_5=7(19+4)=161`,
  `\gcd(570,161)=1` — **witness `i=5`**.
- `(4,2,3,23)`: `n_0=7,n=76,K=30,N=690`. `a_7=7(23+6)=203`,
  `\gcd(690,203)=1` — **witness `i=7`**.
- `(4,3,1,17)`: `n_0=15,n=32,K=20,N=340`. `a_3=7(17+2)=133`,
  `\gcd(340,133)=1` — **witness `i=3`**.
- `(5,3,1,17)`: `n_0=10,n=27,K=18,N=306`. `a_3=133`,
  `\gcd(306,133)=1` — **witness `i=3`**.
- `(5,5,1,19)`: `n_0=3,n=22,K=15,N=285`. `a_4=7(19+3)=154`,
  `\gcd(285,154)=1` — **witness `i=4`**.
- `(6,3,3,17)`: `n_0=5,n=56,K=30,N=510`. `a_3=133`,
  `\gcd(510,133)=1` — **witness `i=3`**.
- `(6,5,1,19)`: `n_0=11,n=30,K=18,N=342`. `a_5=7(19+4)=161`,
  `\gcd(342,161)=1` — **witness `i=5`**.

(Every one of these 9 was checked by exact integer computation: `N=qK`
was verified to equal `a_n+j` exactly for the stated `n`, and
`\gcd(N,a_i)` computed exactly, confirming `\gcd=1` in each case.)

**Conclusion of §6.** For every prime `q\ge11,q\notin\{11,13\}`, every
band `j\in\{2,\dots,6\}`, and every `k\ge1`: a Case-(b) witness for the
illegality of `a_n+j` (`n=n_0(j,r)+kq`) exists — either via Lemma 3
directly (`k\ge18`, or `k\le17` with `q\ge q_{\mathrm{thresh}}(j,r,k)`), or
via one of the 9 explicit witnesses above. This closes Case (b), `k\ge1`,
completely, for every `q` in the theorem's scope.

### 7. Assembly

Combining §1 (base case, `a_n+1` illegal, `a_n+7` legal), §2 (Case (a)
illegality), §4 (`k=0` closure for `q\notin\{11,13\}`), and §6 (`k\ge1`
closure for every admissible `q`): for every prime `q\ge11,
q\notin\{11,13\}` and every `n\ge1` with `H(n)` holding, `a_n+1,\dots,
a_n+6` are all illegal and `a_n+7` is legal, so minimality of the greedy
rule forces `a_{n+1}=a_n+7=7(q+n)=7(q+(n+1)-1)`, establishing `H(n+1)`.

By strong induction, `H(n)` holds for every `n\ge1`:
$$a_n=7(q+n-1)\quad\text{for all }n\ge1,$$
i.e. literal `T=1,L=7` periodicity from `n=1`, for every prime `q\ge11`,
`q\notin\{11,13\}`. **This proves the theorem.** `\blacksquare`

## Promotable lemmas

**`p=7` `K_0`-boundedness table (30 cells).** The explicit table in §3
above (`s_0(j,r),K_0(j,r)` for all `j\in\{2,\dots,6\},r\in\{1,\dots,6\}`),
derived by direct instantiation of the certified Generalized
`K_0`-Boundedness Lemma at `p=7`, independently cross-checked (this
approach's build, the round-27 math-explorer, and the round-27
outline-reviewer, three separate scripts, exact agreement). Reusable by
any future approach needing the `a_1=7q`-type family's exact constants.

**`s^*=5` threshold at `p=7` and its induction (§6).** The inequality
`(s+1)!\ge13+\tfrac7{11}\cdot2^{s+1}(s+2)` for `s\ge5`, proved by an
explicit base case and induction (reusing the sub-fact
`s^2+2s-2\ge0` for `s\ge1` from the certified Primorial Floor Bound's own
corollary). This is the `p=7`-specific analogue of `a1-5q`'s `s^*=5`
threshold (there `K_0\le9,q\ge7`, constants `9,\tfrac57`; here
`K_0\le13,q\ge11`, constants `13,\tfrac7{11}`) — the threshold value
`s^*=5` again comes out the same as `p=3,5`, though the constants differ;
this is not claimed as a general pattern for all `p`, only verified here.

**`\mathrm{Bad}(7)=\{11,13\}`, proved genuine (§5).** The exact
mechanism-level exclusion proof (finite witness window exhausted with no
coprime candidate, both at `n_0=2`) for both exceptions, fully explicit
(not merely a numeric observation). Both exceptions occur at diagonal
(`s_0=1,K_0=8`, the minimal-`K_0` cell) bands — `(j,r)=(4,4)` for `q=11`
and `(6,6)` for `q=13` — consistent with (though this file does not
attempt to prove in general) the round-26 "Minimal-Window Necessity"
observation noted in `a1-pq-subfamily-theorem`.
