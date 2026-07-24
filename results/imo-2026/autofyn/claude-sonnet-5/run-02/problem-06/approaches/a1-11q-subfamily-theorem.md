## Status
solved (round 28: the `a_1=11q` subfamily theorem is fully proved — literal
`T=1,L=11` periodicity from `n=1` for every prime `q>11`,
`q\notin\mathrm{Bad}(11)=\{13,17,19,31,37,43\}`, by instantiating the
certified `p`-uniform machinery from `a1-pq-subfamily-theorem` at `p=11`,
building the explicit 90-cell `(j,r)` table, using the certified round-27
Universal Look-Back Witness Identity to close the `r=1` column's `k=0`
layer unconditionally, closing the remaining 81 cells' `k=0` layer and all
90 cells' `k\ge1` layer with the certified Legendre-Sieve/Primorial-Floor
toolkit, and hand-verifying every one of the 6 genuine exceptions — the
same template as the certified `a1-5q` and `a1-7q` theorems, scaled to
`p=11`. See "Full proof" below.)

## Approaches tried
- (round 28, math-explorer subfamily-extension lens) Fresh from-scratch
  greedy simulation, every prime `q\in(11,6000)`, 80 terms/pair: found
  `\mathrm{Bad}(11)=\{13,17,19,31,37,43\}` (6 exceptions), every one landing
  on a diagonal band (`j=r`), each deviating at a small index
  `n\in\{3,4,5\}`.
- (round 28, outline-reviewer) Independently re-derived the same
  `\mathrm{Bad}(11)` set via its own script, confirmed all six diagonal, and
  APPROVEd the outline as build-ready (mechanical instantiation of
  already-thrice-proved machinery, no new technique risk).
- (round 28, this build) Instantiated the certified `p`-uniform machinery at
  `p=11`: built the full 90-cell `(j,r)` table (`j\in\{2,\dots,10\}`,
  `r\in\{1,\dots,10\}`); used the certified Universal Look-Back Witness
  Identity's `r=1` corollary to close the entire `k=0` layer of the 9
  `r=1` cells unconditionally, with no threshold; computed the `k=0`
  sufficient-window thresholds `Q_1(j,r)` for the remaining 81 cells,
  resolved all 76 below-threshold `(j,r,q)` candidates by explicit witness
  search (70 resolve, exactly 6 genuine exceptions, all diagonal, matching
  `\mathrm{Bad}(11)` exactly); derived a fresh `s^*=5` threshold (`p=11`
  constants: `K_0\le21`, `q\ge13`) for the generic `k\ge1` closure, showed
  `k\ge15` is handled uniformly, reduced the residual band `k\in\{1,\dots,
  14\}` to 29 below-threshold `(j,r,k,q)` quadruples (24 moot, `q\in
  \mathrm{Bad}(11)`; 5 non-moot, all resolved by explicit witnesses).
  **Result: the theorem is now completely proved.**

## Current best

### Target (now proved — see Full proof)
For every prime `q>11` with `q\notin\{13,17,19,31,37,43\}`, and `a_1=11q`:
`a_n=11(q+n-1)` for every `n\ge1` — literal `T=1,L=11` periodicity from
`n=1`.

## Full proof

### 0. Setup and imported machinery

Fix a prime `q>11`, `q\notin\{13,17,19,31,37,43\}`, and `a_1=11q`.
Strong-induction hypothesis at step `n`, `H(n)`: `a_i=11(q+i-1)` for
`i=1,\dots,n`. In particular `11\mid a_i` for every such `i`, and — since
`11,q` are distinct primes — `P(a_1)=\{11,q\}`.

We use, without re-derivation, the following results, each certified in
this workspace for a general odd prime `p` (so their `p=11` instantiations
below require no new proof, only substitution):

- **Lemma 1 (Generalized gcd-difference Witness Lemma,
  `lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md`).** For
  `N:=a_n+j`, `j\in\{1,\dots,10\}`, under `H(n)`: `\gcd(N,a_n)=\gcd(N,j)`.
- **Lemma 2 (Generalized `K_0`-Boundedness, `p=11`,
  `lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md`).** For
  `j\in\{2,\dots,10\}` and prime `q>11` with `q\equiv r\pmod{11}`
  (`r\in\{1,\dots,10\}`), the first index `n_0(j,r;q)` with `q\mid(a_{n_0}+j)`
  satisfies `K_0(j,r):=(a_{n_0}+j)/q=11+s_0(j,r)`, where
  `s_0(j,r)\in\{1,\dots,10\}` is the unique solution of `s_0\cdot r\equiv
  j\pmod{11}`, and `n_0(j,r;q)=1+(s_0(j,r)q-j)/11`.
- **Lemma 3 (Legendre Sieve Gap Bound, `lemmas/legendre-sieve-gap-bound.md`).**
  For integer `M\ge2` with `\rho:=\omega(M)`, any window of `L\ge2^\rho(\rho+1)`
  consecutive integers contains one coprime to `M`.
- **Lemma 4 (Primorial Floor Bound, `lemmas/primorial-floor-bound.md`).** If
  `\omega(M)=\rho` then `M\ge(\rho+1)!`.
- **Lemma 5 (Universal Look-Back Witness Identity and its `r=1` Corollary,
  `lemmas/universal-look-back-witness-identity.md`).** Under `H(n)`, for
  `j\in\{1,\dots,10\}`, `N:=a_n+j`, and any `1\le i\le n`:
  `\gcd(N,a_i)=\gcd(11(n-i)+j,\,q+i-1)`. Moreover, when `q\equiv1\pmod{11}`,
  writing `q=11t+1` (`t` even, `t\ge2`), the `k`-th Case-(b) risk index of
  band `j` is `n=1+jt+kq` and, at `i=n` (look-back distance `0`),
  `\gcd(N,a_n)=\gcd(k+1,j)` — in particular this equals `1` unconditionally
  whenever `\gcd(k+1,j)=1`, for every `p`, every band, every such `q`, with
  no threshold.

### 1. Base case and the `j=1,11` bands

`n=1`: `a_1=11q=11(q+1-1)`, by definition.

Assume `H(n)`. We show `a_n+1,\dots,a_n+10` are all illegal and `a_n+11` is
legal, forcing `a_{n+1}=a_n+11=11(q+n)`, i.e. `H(n+1)`.

**`a_n+1` illegal.** `\gcd(a_n+1,a_n)=1` (consecutive integers), witnessed
by `i=n`.

**`a_n+11` legal.** `a_n+11=11(q+n-1)+11=11(q+n)`. For every `i\le n`,
`\gcd(a_n+11,a_i)\ge\gcd(11(q+n),11(q+i-1))\ge11>1` (both multiples of
`11`, by `H(n)`).

### 2. Illegality of `a_n+j`, `j\in\{2,\dots,10\}`: the Case (a)/(b) split

Fix `j\in\{2,\dots,10\}` and `N:=a_n+j=11(q+n-1)+j`. Since `1\le j\le10`,
`N\equiv j\not\equiv0\pmod{11}`, so `11\nmid N`.

**Case (a): `q\nmid N`.** Any common divisor of `N` and `a_1=11q` divides
`11q`; since `11\nmid N` and `q\nmid N`, the only such divisor is `1`:
`\gcd(N,a_1)=1` — illegal, witnessed by `i=1`.

**Case (b): `q\mid N`.** Write `N=qK`, `K:=N/q\in\mathbb Z_{>0}`. For
`i=1`: `\gcd(N,a_1)=\gcd(N,11q)\ge q>1`, never a witness here. For
`2\le i\le n`: since `\gcd(N,11)=1`, writing `m:=q+i-1`,
`\gcd(N,a_i)=\gcd(N,m)=\gcd(qK,m)`. So Case-(b) illegality of `a_n+j`
reduces to finding, in the window `m=q+1,\dots,q+n-1` (length `L:=n-1`,
`i=2,\dots,n`), an integer coprime to `N=qK`.

By Lemma 2, the Case-(b) indices for band `j`, residue `r:=q\bmod{11}`, are
exactly `n=n_0(j,r)+kq`, `k=0,1,2,\dots`, with `K(k):=K_0(j,r)+11k`.

### 3. The 90-cell table (`p=11`)

Solving `s_0\cdot r\equiv j\pmod{11}` for each `(j,r)`, `j\in\{2,\dots,10\}`,
`r\in\{1,\dots,10\}` (90 cells), via `sympy.mod_inverse`, and setting
`K_0(j,r)=11+s_0(j,r)`:

| `j\backslash r` | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` |
|---|---|---|---|---|---|---|---|---|---|---|
| `2` | `2,13` | `1,12` | `8,19` | `6,17` | `7,18` | `4,15` | `5,16` | `3,14` | `10,21` | `9,20` |
| `3` | `3,14` | `7,18` | `1,12` | `9,20` | `5,16` | `6,17` | `2,13` | `10,21` | `4,15` | `8,19` |
| `4` | `4,15` | `2,13` | `5,16` | `1,12` | `3,14` | `8,19` | `10,21` | `6,17` | `9,20` | `7,18` |
| `5` | `5,16` | `8,19` | `9,20` | `4,15` | `1,12` | `10,21` | `7,18` | `2,13` | `3,14` | `6,17` |
| `6` | `6,17` | `3,14` | `2,13` | `7,18` | `10,21` | `1,12` | `4,15` | `9,20` | `8,19` | `5,16` |
| `7` | `7,18` | `9,20` | `6,17` | `10,21` | `8,19` | `3,14` | `1,12` | `5,16` | `2,13` | `4,15` |
| `8` | `8,19` | `4,15` | `10,21` | `2,13` | `6,17` | `5,16` | `9,20` | `1,12` | `7,18` | `3,14` |
| `9` | `9,20` | `10,21` | `3,14` | `5,16` | `4,15` | `7,18` | `6,17` | `8,19` | `1,12` | `2,13` |
| `10` | `10,21` | `5,16` | `7,18` | `8,19` | `2,13` | `9,20` | `3,14` | `4,15` | `6,17` | `1,12` |

(Each cell entry is `s_0(j,r),K_0(j,r)`. Every diagonal cell `j=r` gives
`s_0=1,K_0=12` exactly, matching the certified Diagonal Characterization
Lemma. Independently cross-checked this round via `sympy.mod_inverse` and
by direct brute-force search for `n_0,K_0` on sample cells — exact match,
consistent with the outline-reviewer's independent recomputation.)

Note `K_0(j,r)\in\{12,\dots,21\}$ throughout — this bound (`K_0\le21`) is
used in §6.

### 4. Closing `k=0` for the `r=1` column: free by Lemma 5

For `q\equiv1\pmod{11}` (the 9 cells `j\in\{2,\dots,10\},r=1`), Lemma 5's
Corollary gives, at `k=0`, `\gcd(N,a_n)=\gcd(1,j)=1` unconditionally — the
index `i=n_0(j,1)` itself is always a witness, with no threshold and no
per-`q` computation. This closes the entire `k=0` layer of the `r=1` column
for every admissible prime `q\equiv1\pmod{11}`, for every band
`j\in\{2,\dots,10\}`. (More generally, by the same Corollary, every `k\ge0`
with `\gcd(k+1,j)=1` is likewise free for `r=1` — used again in §6.)

### 5. Closing `k=0` for the remaining 81 cells (`r=2,\dots,10`)

**Sufficient-window criterion.** If `n_0(j,r)-1\ge K_0(j,r)`, the window
`m=q+1,\dots,q+n_0-1` (length `n_0-1`, all `<2q` since `n_0\le q`, hence
automatically coprime to `q`) contains a full residue system mod
`K_0(j,r)`, hence an integer coprime to `K_0(j,r)` — a witness.
Substituting the explicit affine formula for `n_0`, this holds for every
prime `q\equiv r\pmod{11}` with
`q\ge Q_1(j,r):=\dfrac{11(K_0(j,r)+1)+j}{s_0(j,r)}`.

Computing `Q_1` for all 81 cells (`r=2,\dots,10`) and, for each, listing the
primes `q\equiv r\pmod{11}`, `q>11`, with `q<Q_1(j,r)` (the below-threshold
`k=0` candidates), gives exactly **76** triples `(j,r,q)` (independently
computed this round via a dedicated script; full list below with
resolution).

**Direct resolution of every below-threshold `k=0` candidate.** For each
triple, `n_0=1+(s_0q-j)/11`, `N=a_{n_0}+j=qK_0`; we search `i=1,\dots,n_0`
for `\gcd(N,a_i)=1` with `a_i=11(q+i-1)`. Result (`i` = witness index,
`EXC` = no witness exists, a genuine exception):

`(2,2,13)`:`n_0=2,N=156,`**EXC**; `(2,2,79)`:`n_0=8,N=948,i=5`;
`(2,2,101)`:`n_0=10,N=1212,i=3`; `(2,6,17)`:`n_0=7,N=255,i=3`;
`(2,7,29)`:`n_0=14,N=464,i=3`; `(2,8,19)`:`n_0=6,N=266,i=5`;
`(2,8,41)`:`n_0=12,N=574,i=3`; `(3,2,13)`:`n_0=9,N=234,i=5`;
`(3,3,47)`:`n_0=5,N=564,i=3`; `(3,3,113)`:`n_0=11,N=1356,i=3`;
`(3,6,17)`:`n_0=10,N=289,i=2`; `(3,7,29)`:`n_0=6,N=377,i=2`;
`(3,7,73)`:`n_0=14,N=949,i=2`; `(3,8,19)`:`n_0=18,N=399,i=2`;
`(3,9,31)`:`n_0=12,N=465,i=2`; `(4,2,13)`:`n_0=3,N=169,i=2`;
`(4,4,37)`:`n_0=4,N=444,`**EXC**; `(4,4,59)`:`n_0=6,N=708,i=3`;
`(4,4,103)`:`n_0=10,N=1236,i=5`; `(4,6,17)`:`n_0=13,N=323,i=2`;
`(4,8,19)`:`n_0=11,N=323,i=2`; `(5,2,13)`:`n_0=10,N=247,i=2`;
`(5,4,37)`:`n_0=14,N=555,i=2`; `(5,5,71)`:`n_0=7,N=852,i=3`;
`(5,5,137)`:`n_0=13,N=1644,i=3`; `(5,6,17)`:`n_0=16,N=357,i=3`;
`(5,7,29)`:`n_0=19,N=522,i=3`; `(5,8,19)`:`n_0=4,N=247,i=2`;
`(5,8,41)`:`n_0=8,N=533,i=2`; `(5,9,31)`:`n_0=9,N=434,i=3`;
`(5,9,53)`:`n_0=15,N=742,i=3`; `(6,2,13)`:`n_0=4,N=182,i=3`;
`(6,3,47)`:`n_0=9,N=611,i=2`; `(6,6,17)`:`n_0=2,N=204,`**EXC**;
`(6,6,61)`:`n_0=6,N=732,i=5`; `(6,6,83)`:`n_0=8,N=996,i=3`;
`(6,6,127)`:`n_0=12,N=1524,i=5`; `(6,7,29)`:`n_0=11,N=435,i=3`;
`(6,8,19)`:`n_0=16,N=380,i=3`; `(7,2,13)`:`n_0=11,N=260,i=5`;
`(7,6,17)`:`n_0=5,N=238,i=3`; `(7,7,29)`:`n_0=3,N=348,i=3`;
`(7,7,73)`:`n_0=7,N=876,i=5`; `(7,7,139)`:`n_0=13,N=1668,i=5`;
`(7,8,19)`:`n_0=9,N=304,i=3`; `(7,9,31)`:`n_0=6,N=403,i=2`;
`(7,9,53)`:`n_0=10,N=689,i=2`; `(7,10,43)`:`n_0=16,N=645,i=2`;
`(8,2,13)`:`n_0=5,N=195,i=2`; `(8,4,37)`:`n_0=7,N=481,i=2`;
`(8,4,59)`:`n_0=11,N=767,i=2`; `(8,6,17)`:`n_0=8,N=272,i=3`;
`(8,8,19)`:`n_0=2,N=228,`**EXC**; `(8,8,41)`:`n_0=4,N=492,i=3`;
`(8,8,107)`:`n_0=10,N=1284,i=3`; `(8,10,43)`:`n_0=12,N=602,i=3`;
`(9,2,13)`:`n_0=12,N=273,i=4`; `(9,3,47)`:`n_0=13,N=658,i=5`;
`(9,4,37)`:`n_0=17,N=592,i=3`; `(9,6,17)`:`n_0=11,N=306,i=3`;
`(9,7,29)`:`n_0=16,N=493,i=2`; `(9,8,19)`:`n_0=14,N=361,i=2`;
`(9,9,31)`:`n_0=3,N=372,`**EXC**; `(9,9,53)`:`n_0=5,N=636,i=3`;
`(9,9,97)`:`n_0=9,N=1164,i=5`; `(9,10,43)`:`n_0=8,N=559,i=2`;
`(10,2,13)`:`n_0=6,N=208,i=3`; `(10,5,71)`:`n_0=13,N=923,i=2`;
`(10,6,17)`:`n_0=14,N=340,i=3`; `(10,7,29)`:`n_0=8,N=406,i=3`;
`(10,8,19)`:`n_0=7,N=285,i=4`; `(10,8,41)`:`n_0=15,N=615,i=3`;
`(10,9,31)`:`n_0=17,N=527,i=2`; `(10,10,43)`:`n_0=4,N=516,`**EXC**;
`(10,10,109)`:`n_0=10,N=1308,i=5`; `(10,10,131)`:`n_0=12,N=1572,i=3`.

(All 76 `N` values and all 70 witness `\gcd` computations were carried out
exactly, using `N=qK_0` and `a_i=11(q+i-1)`, via a dedicated script; every
one of the 70 witnessed instances was independently double-checked by
direct integer `\gcd` computation.)

So every below-threshold `k=0` candidate for `r\ne1` resolves by an
explicit witness **except exactly six**: `(2,2,13)`, `(4,4,37)`,
`(6,6,17)`, `(8,8,19)`, `(9,9,31)`, `(10,10,43)` — all on the diagonal
`j=r`, consistent with (though this file does not rely on) the certified
Diagonal Characterization Lemma. Every prime `q\equiv r\pmod{11},q>11` not
listed above already satisfies `q\ge Q_1(j,r)`, hence closes automatically
by the sufficient-window criterion. **The `k=0` case is now completely
settled**, with the six exceptional primes identified exactly:
`\{13,17,19,31,37,43\}`.

### 6. `\mathrm{Bad}(11)=\{13,17,19,31,37,43\}` are genuine, permanent exceptions

For each exceptional prime, we verify explicitly, using `a_i=11(q+i-1)`
under `H(n_0)`: (i) every smaller candidate `a_{n_0}+1,\dots,a_{n_0}+(j-1)`
is illegal via `i=1` (Case (a): `q\nmid` these, since only multiples of `q`
among `\{a_{n_0}+1,\dots,a_{n_0}+j\}` are `a_{n_0}+j` itself, by the
defining property of `n_0`); (ii) `N=a_{n_0}+j=qK_0` has `\gcd(N,a_i)>1`
for every `i=1,\dots,n_0` (no witness) — so `N` is legal, forcing
`a_{n_0+1}=N\ne11(q+n_0)`, breaking `H(n_0+1)`.

**`q=13`** (`j=2,r=2,n_0=2`): `a_1=143=11\cdot13`, `a_2=154=2\cdot7\cdot11`.
`N=a_2+2=156=2^2\cdot3\cdot13`: `\gcd(156,143)=13`, `\gcd(156,154)=2` — no
witness, `156` legal. Smaller candidate: `a_2+1=155=5\cdot31`,
`\gcd(155,143)=1` — illegal via `i=1`. So `a_3=156\ne11\cdot14=154+11=165`.
Genuine exception.

**`q=17`** (`j=6,r=6,n_0=2`): `a_1=187=11\cdot17`,
`a_2=198=2\cdot3^2\cdot11`. `N=a_2+6=204=2^2\cdot3\cdot17`:
`\gcd(204,187)=17`, `\gcd(204,198)=6` — no witness, `204` legal. Smaller
candidates `a_2+1,\dots,a_2+5 = 199,200,201,202,203`, each coprime to
`a_1=187=11\cdot17` (`199` prime, `200=2^3\cdot5^2`, `201=3\cdot67`,
`202=2\cdot101`, `203=7\cdot29` — none divisible by `11` or `17`) — all
illegal via `i=1`. So `a_3=204\ne11\cdot19=209$. Genuine exception.

**`q=19`** (`j=8,r=8,n_0=2`): `a_1=209=11\cdot19`,
`a_2=220=2^2\cdot5\cdot11`. `N=a_2+8=228=2^2\cdot3\cdot19`:
`\gcd(228,209)=19`, `\gcd(228,220)=4` — no witness, `228` legal. Smaller
candidates `a_2+1,\dots,a_2+7 = 221,\dots,227` (`221=13\cdot17`,
`222=2\cdot3\cdot37`, `223` prime, `224=2^5\cdot7`, `225=3^2\cdot5^2`,
`226=2\cdot113`, `227` prime — none divisible by `11` or `19`) — all
illegal via `i=1`. So `a_3=228\ne11\cdot21=231`. Genuine exception.

**`q=31`** (`j=9,r=9,n_0=3`): `a_1=341=11\cdot31`,
`a_2=352=2^5\cdot11`, `a_3=363=3\cdot11^2`. `N=a_3+9=372=2^2\cdot3\cdot31`:
`\gcd(372,341)=31`, `\gcd(372,352)=4`, `\gcd(372,363)=3` — no witness,
`372` legal. Smaller candidates `a_3+1,\dots,a_3+8 = 364,\dots,371`
(`364=2^2\cdot7\cdot13`, `365=5\cdot73`, `366=2\cdot3\cdot61`, `367` prime,
`368=2^4\cdot23`, `369=3^2\cdot41`, `370=2\cdot5\cdot37`, `371=7\cdot53` —
none divisible by `11` or `31`) — all illegal via `i=1`. So
`a_4=372\ne11\cdot33=363+11=374`. Genuine exception.

**`q=37`** (`j=4,r=4,n_0=4`): `a_1=407=11\cdot37`, `a_2=418=2\cdot11\cdot19`,
`a_3=429=3\cdot11\cdot13`, `a_4=440=2^3\cdot5\cdot11`.
`N=a_4+4=444=2^2\cdot3\cdot37`: `\gcd(444,407)=37`, `\gcd(444,418)=2`,
`\gcd(444,429)=3`, `\gcd(444,440)=4` — no witness, `444` legal. Smaller
candidates `a_4+1,a_4+2,a_4+3=441,442,443` (`441=3^2\cdot7^2`,
`442=2\cdot13\cdot17`, `443` prime — none divisible by `11` or `37`) — all
illegal via `i=1`. So `a_5=444\ne11\cdot41=440+11=451`. Genuine exception.

**`q=43`** (`j=10,r=10,n_0=4`): `a_1=473=11\cdot43`,
`a_2=484=2^2\cdot11^2`, `a_3=495=3^2\cdot5\cdot11`,
`a_4=506=2\cdot11\cdot23`. `N=a_4+10=516=2^2\cdot3\cdot43`:
`\gcd(516,473)=43`, `\gcd(516,484)=4`, `\gcd(516,495)=3`,
`\gcd(516,506)=2` — no witness, `516` legal. Smaller candidates
`a_4+1,\dots,a_4+9 = 507,\dots,515` (`507=3\cdot13^2`, `508=2^2\cdot127`,
`509` prime, `510=2\cdot3\cdot5\cdot17`, `511=7\cdot73`, `512=2^9`,
`513=3^3\cdot19`, `514=2\cdot257`, `515=5\cdot103` — none divisible by
`11` or `43`) — all illegal via `i=1`. So `a_5=516\ne11\cdot47=506+11=517`.
Genuine exception.

**Independent numerical confirmation.** Direct greedy re-simulation (fresh
script, literal legality rule) for every prime `q\in(11,6000)`, `80` terms
each: matches `a_n=11(q+n-1)` in every term for every prime except
`q\in\{13,17,19,31,37,43\}`, each of which deviates exactly at the index
established above, with the exact deviating value confirmed
(`a_3=156,204,228` for `q=13,17,19`; `a_4=372` for `q=31`; `a_5=444,516`
for `q=37,43`). (Independently reproduced by the round-28 math-explorer
and the round-28 outline-reviewer with separate scripts, and reconfirmed by
this build's own dedicated hand-check script above.)

### 7. Closing `k\ge1` (all 90 cells)

Fix a Case-(b) index `n=n_0(j,r)+kq`, `k\ge1` (any `r\in\{1,\dots,10\}`; for
`r=1` we only need this when `\gcd(k+1,j)>1`, since `\gcd(k+1,j)=1` is
already free by Lemma 5). As derived in §2, `K(k)=K_0(j,r)+11k`, `N=qK(k)`,
and a witness exists whenever the window `m=q+1,\dots,q+n-1` (length
`L:=n-1=n_0-1+kq\ge kq\ge13k`, using `q\ge13` — the least admissible prime
for `p=11` — and `n_0\ge1`) contains an integer coprime to `M:=qK(k)`. By
Lemma 3, this holds once `L\ge2^{\rho^*}(\rho^*+1)`,
`\rho^*:=\omega(qK(k))\le\omega(K(k))+1`.

**Threshold `s^*=5` for the large-`\omega(K)` regime.** Suppose
`s:=\omega(K(k))\ge5`. By Lemma 4, `K(k)\ge(s+1)!`. Since `K_0(j,r)\le21`
for every cell (§3 table, max entry `21`), `11k=K(k)-K_0(j,r)\ge(s+1)!-21`.
We claim `(s+1)!\ge21+\tfrac{11}{13}\cdot2^{s+1}(s+2)` for every `s\ge5`:

- *Base case `s=5`:* `6!=720`; RHS
  `=21+\tfrac{11}{13}\cdot64\cdot7=21+\tfrac{4928}{13}=21+379.08\overline{461538}
  =400.08\overline{461538}`; `720\ge400.08`. ✓.
- *Inductive step `s\to s+1` (`s\ge1`, valid from `s=5` on):* if
  `(s+1)!\ge21+\tfrac{11}{13}2^{s+1}(s+2)` then, multiplying by `(s+2)>0`,
  `(s+2)!\ge21(s+2)+\tfrac{11}{13}2^{s+1}(s+2)^2`. We need
  `(s+2)!\ge21+\tfrac{11}{13}2^{s+2}(s+3)`. It suffices that
  `21(s+2)-21+\tfrac{11}{13}2^{s+1}\bigl[(s+2)^2-2(s+3)\bigr]\ge0`, i.e.
  `21(s+1)+\tfrac{11}{13}2^{s+1}(s^2+2s-2)\ge0`. Since `s^2+2s-2\ge0` for
  `s\ge1` (`=1\ge0` at `s=1`, increasing thereafter) and `21(s+1)>0`, both
  terms are `\ge0`. ✓.

So `(s+1)!\ge21+\tfrac{11}{13}2^{s+1}(s+2)` for all `s\ge5`, giving
`11k\ge(s+1)!-21\ge\tfrac{11}{13}2^{s+1}(s+2)`, i.e.
`13k\ge2^{s+1}(s+2)`. Since `\rho^*\le s+1` and `x\mapsto2^x(x+1)` is
increasing, `2^{\rho^*}(\rho^*+1)\le2^{s+1}(s+2)\le13k\le L`: **Lemma 3
applies**, giving a witness, whenever `\omega(K(k))\ge5` — no further
restriction on `k,j,r,q` needed.

**Generic bound for `\omega(K(k))\le4`.** Then `\rho^*\le5`, so
`2^{\rho^*}(\rho^*+1)\le2^5\cdot6=192`. Since `L\ge13k`, `L\ge192` once
`k\ge15` (`13\cdot15=195\ge192`; `13\cdot14=182<192`). So **for every
`k\ge15`**, either `\omega(K(k))\ge5` (handled above) or `\omega(K(k))\le4`
(this generic bound applies): in both cases Lemma 3 gives a witness,
uniformly across every cell and every admissible `q`.

**The residual band `k\in\{1,\dots,14\}`.** For `k\le14`,
`K(k)=K_0+11k\le21+154=175<720=6!`; by Lemma 4 (contrapositive),
`\omega(K(k))\ge5` would force `K(k)\ge720`, impossible — so
`\omega(K(k))\le4` automatically throughout this range, and the exact
(not generic) bound `2^{\omega(K(k))+1}(\omega(K(k))+2)` (using
`\rho^*\le\omega(K(k))+1`) may be used per cell for a tighter threshold.

Using this exact per-cell bound and solving `L(q)\ge` it (with
`L(q)=n_0(j,r)-1+kq` an explicit, strictly increasing affine function of
`q`, giving `q_{\mathrm{thresh}}(j,r,k)=\dfrac{11\cdot\mathrm{bound}+j}
{s_0(j,r)+11k}`) for each of the `90\times14=1260` cell/`k` combinations
(skipping the `r=1` cells whenever `\gcd(k+1,j)=1`, already free by Lemma
5) finds that only **29** `(j,r,k,q)` combinations have any admissible
prime below threshold:

`(2,1,1,23)`; `(2,2,2,13)`; `(2,2,6,13)`; `(2,6,1,17)`; `(3,6,1,17)`;
`(3,10,1,43)`; `(4,1,1,23)`; `(4,2,1,13)`; `(4,2,2,13)`; `(4,6,1,17)`;
`(4,8,1,19)`; `(5,2,1,13)`; `(5,8,1,19)`; `(6,2,2,13)`; `(6,8,2,19)`;
`(6,9,1,31)`; `(7,2,2,13)`; `(8,1,1,23)`; `(8,2,1,13)`; `(8,2,5,13)`;
`(8,6,4,17)`; `(9,1,2,23)`; `(9,8,1,19)`; `(9,8,1,41)`; `(10,2,2,13)`;
`(10,2,4,13)`; `(10,4,1,37)`; `(10,6,2,17)`; `(10,8,1,19)`.

**24 of these 29 are moot: `q\in\{13,17,19,31,37,43\}=\mathrm{Bad}(11)`.**
By §6, each such `q` is already established to deviate from the closed
form at a small, explicit index and is excluded from the theorem's scope
by definition — so any `(j,r,k,q)` instance with `q\in\mathrm{Bad}(11)`
concerns a `q` outside the theorem's stated scope and does not need to be
resolved for the theorem to hold. (Explicitly: every entry above except
those five listed next has `q\in\{13,17,19,31,37,43\}$.)

**The remaining 5 non-moot instances**, all with `q\in\{23,41\}` (neither
in `\mathrm{Bad}(11)`), resolved by explicit witness search over the full
range `i=1,\dots,n`:

- `(2,1,1,23)`: `n_0=5,n=28,K=24,N=552=23\cdot24`. `a_3=11\cdot25=275`,
  `\gcd(552,275)=1` — **witness `i=3`**.
- `(4,1,1,23)`: `n_0=9,n=32,K=26,N=598=23\cdot26`. `a_3=275`,
  `\gcd(598,275)=1` — **witness `i=3`**.
- `(8,1,1,23)`: `n_0=17,n=40,K=30,N=690=23\cdot30`. `a_7=11\cdot29=319`,
  `\gcd(690,319)=1` — **witness `i=7`**.
- `(9,1,2,23)`: `n_0=19,n=65,K=42,N=966=23\cdot42`. `a_3=275`,
  `\gcd(966,275)=1` — **witness `i=3`**.
- `(9,8,1,41)`: `n_0=30,n=71,K=30,N=1230=41\cdot30`. `a_3=11\cdot43=473`,
  `\gcd(1230,473)=1` — **witness `i=3`**.

(Every one of these 5 was checked by exact integer computation: `N=qK` was
verified to equal `a_n+j` exactly for the stated `n`, and `\gcd(N,a_i)`
computed exactly, confirming `\gcd=1` in each case.)

**Conclusion of §7.** For every prime `q>11`, `q\notin\mathrm{Bad}(11)`,
every band `j\in\{2,\dots,10\}`, and every `k\ge1` (with, for `r=1`, the
additional case `\gcd(k+1,j)=1$ handled unconditionally by Lemma 5): a
Case-(b) witness for the illegality of `a_n+j` (`n=n_0(j,r)+kq`) exists —
either via Lemma 5 (`r=1`, `\gcd(k+1,j)=1`), via Lemma 3 directly (`k\ge15`,
or `k\le14` with `q\ge q_{\mathrm{thresh}}(j,r,k)`), or via one of the 5
explicit witnesses above. This closes Case (b), `k\ge1`, completely, for
every `q` in the theorem's scope.

### 8. Assembly

Combining §1 (base case, `a_n+1` illegal, `a_n+11` legal), §2 (Case (a)
illegality), §4 (`k=0` closure for the `r=1` column, free by Lemma 5), §5
(`k=0` closure for `r=2,\dots,10`, `q\notin\mathrm{Bad}(11)`), and §7
(`k\ge1` closure for every admissible `q`, every cell): for every prime
`q>11`, `q\notin\{13,17,19,31,37,43\}`, and every `n\ge1` with `H(n)`
holding, `a_n+1,\dots,a_n+10` are all illegal and `a_n+11` is legal, so
minimality of the greedy rule forces `a_{n+1}=a_n+11=11(q+n)=11(q+(n+1)-1)`,
establishing `H(n+1)`.

By strong induction, `H(n)` holds for every `n\ge1`:
$$a_n=11(q+n-1)\quad\text{for all }n\ge1,$$
i.e. literal `T=1,L=11` periodicity from `n=1`, for every prime `q>11`,
`q\notin\{13,17,19,31,37,43\}`. **This proves the theorem.** `\blacksquare`

## Promotable lemmas

**`p=11` `K_0`-boundedness table (90 cells).** The explicit table in §3
above (`s_0(j,r),K_0(j,r)` for all `j\in\{2,\dots,10\},r\in\{1,\dots,10\}`),
derived by direct instantiation of the certified Generalized
`K_0`-Boundedness Lemma at `p=11`. Reusable by any future approach needing
the `a_1=11q`-type family's exact constants.

**`s^*=5` threshold at `p=11` and its induction (§7).** The inequality
`(s+1)!\ge21+\tfrac{11}{13}\cdot2^{s+1}(s+2)` for `s\ge5`, proved by an
explicit base case and induction (reusing the sub-fact `s^2+2s-2\ge0` for
`s\ge1` from the certified Primorial Floor Bound's own corollary). This is
the `p=11`-specific analogue of `a1-5q`'s and `a1-7q`'s `s^*=5` thresholds
(`K_0\le21,q\ge13`, constants `21,\tfrac{11}{13}`) — `s^*=5` again matches
`p=3,5,7`, though this is not claimed as a general pattern for all `p`, only
verified here (a fourth data point).

**`\mathrm{Bad}(11)=\{13,17,19,31,37,43\}`, proved genuine (§6).** The exact
mechanism-level exclusion proof (finite witness window exhausted with no
coprime candidate, at `n_0\in\{2,3,4\}` respectively) for all six
exceptions, fully explicit. All six exceptions occur at diagonal
(`j=r`, minimal `K_0=12`) bands — `(j,r)=(2,2),(6,6),(8,8),(9,9),(4,4),
(10,10)` for `q=13,17,19,31,37,43` respectively — consistent with (though
this file does not attempt to prove in general) the round-26 "Minimal-
Window Necessity" observation and the certified Diagonal Characterization
Lemma. This is the fourth consecutive `p`-instantiation (`p=3,5,7,11`) in
which every genuine exception lands exactly on the diagonal band.
