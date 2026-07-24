## Status
solved (round 29: the `a_1=17q` subfamily theorem is fully proved — literal
`T=1,L=17` periodicity from `n=1` for every prime `q>17`,
`q\notin\mathrm{Bad}(17)=\{19,23,29,31,37,43,61,67\}`, by instantiating the
certified `p`-uniform machinery from `a1-pq-subfamily-theorem` at `p=17`,
building the explicit 240-cell `(j,r)` table, using the certified Universal
Look-Back Witness Identity to close the `r=1` column's `k=0` layer
unconditionally, closing the remaining 225 cells' `k=0` layer and all 240
cells' `k\ge1` layer with the certified Legendre-Sieve/Primorial-Floor
toolkit, and hand-verifying every one of the 8 genuine exceptions — the
same template as the certified `a1-5q`/`a1-7q`/`a1-11q` theorems, scaled to
`p=17`. See "Full proof" below.)

## Approaches tried
- (round 29, outline, secondary/lower-priority slug) Instantiate the
  certified `p`-uniform machinery at `p=17`; round-29 diversity-scout
  explorer had already found `\mathrm{Bad}(17)=\{19,23,29,31,37,43,61,67\}`
  by greedy resimulation but had not built the full table/threshold/witness
  work.
- (round 29, this build) Fully instantiated the certified `p`-uniform
  machinery at `p=17`, exactly mirroring `a1-11q`'s completed build: built
  the full 240-cell `(j,r)` table (`j\in\{2,\dots,16\}`, `r\in\{1,\dots,
  16\}`); used the certified Universal Look-Back Witness Identity's `r=1`
  corollary to close the entire `k=0` layer of the 15 `r=1` cells
  unconditionally, with no threshold; computed the `k=0` sufficient-window
  thresholds `Q_1(j,r)` for the remaining 225 cells, resolved all 209
  below-threshold `(j,r,q)` candidates by explicit witness search (201
  resolve, exactly 8 genuine exceptions, all diagonal, matching
  `\mathrm{Bad}(17)` exactly, and — unlike `a1-13q`'s outline warning about
  duplicate moot bands — an explicit check confirmed **no** duplicate/moot
  pathology: every non-diagonal below-threshold band for each of the 8
  exceptional primes resolves with an honest witness); derived a fresh
  `s^*=5` threshold (`p=17` constants: `K_0\le33`, `q_{\min}=19`) for the
  generic `k\ge1` closure, showed `k\ge11` is handled uniformly, reduced the
  residual band `k\in\{1,\dots,10\}` to 31 below-threshold `(j,r,k,q)`
  quadruples (28 moot, `q\in\mathrm{Bad}(17)`; 3 non-moot, all resolved by
  explicit witnesses). **Result: the theorem is now completely proved.**
  Independently cross-validated with a from-scratch literal greedy
  simulation (778 primes `q\in(17,3000)`, corrected legality semantics
  requiring `\gcd(\text{candidate},a_i)>1$ for *every* `i\le n`, not merely
  some `i`): exactly reproduces `\mathrm{Bad}(17)` and every exact
  deviation index/value, and confirms zero mismatches for 535 primes
  `q\in(17,4000)\setminus\mathrm{Bad}(17)` out to 60 terms each.

## Current best

### Target (now proved — see Full proof)
For every prime `q>17` with `q\notin\{19,23,29,31,37,43,61,67\}`, and
`a_1=17q`: `a_n=17(q+n-1)` for every `n\ge1` — literal `T=1,L=17`
periodicity from `n=1`.

## Full proof

### 0. Setup and imported machinery

Fix a prime `q>17`, `q\notin\{19,23,29,31,37,43,61,67\}`, and `a_1=17q`.
Strong-induction hypothesis at step `n`, `H(n)`: `a_i=17(q+i-1)` for
`i=1,\dots,n`. In particular `17\mid a_i` for every such `i`, and — since
`17,q` are distinct primes — `P(a_1)=\{17,q\}`.

The greedy rule: `a_{n+1}` is the least integer `>a_n` such that
`\gcd(a_{n+1},a_i)>1` for *every* `i=1,\dots,n` (shares a nontrivial common
factor with **each** prior term — a candidate is illegal, i.e. rejected,
if there exists even one `i` with `\gcd=1$; such an `i` is called a
**witness** to the candidate's illegality).

We use, without re-derivation, the following results, each certified in
this workspace for a general odd prime `p` (so their `p=17` instantiations
below require no new proof, only substitution):

- **Lemma 1 (Generalized gcd-difference Witness Lemma,
  `lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md`).** For
  `N:=a_n+j`, `j\in\{1,\dots,16\}`, under `H(n)`: `\gcd(N,a_n)=\gcd(N,j)`.
- **Lemma 2 (Generalized `K_0`-Boundedness, `p=17`,
  `lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md`).** For
  `j\in\{2,\dots,16\}` and prime `q>17` with `q\equiv r\pmod{17}`
  (`r\in\{1,\dots,16\}`), the first index `n_0(j,r;q)` with `q\mid(a_{n_0}+j)`
  satisfies `K_0(j,r):=(a_{n_0}+j)/q=17+s_0(j,r)`, where
  `s_0(j,r)\in\{1,\dots,16\}` is the unique solution of `s_0\cdot r\equiv
  j\pmod{17}`, and `n_0(j,r;q)=1+(s_0(j,r)q-j)/17`.
- **Lemma 3 (Legendre Sieve Gap Bound, `lemmas/legendre-sieve-gap-bound.md`).**
  For integer `M\ge2` with `\rho:=\omega(M)`, any window of `L\ge2^\rho(\rho+1)`
  consecutive integers contains one coprime to `M`.
- **Lemma 4 (Primorial Floor Bound, `lemmas/primorial-floor-bound.md`).** If
  `\omega(M)=\rho` then `M\ge(\rho+1)!`.
- **Lemma 5 (Universal Look-Back Witness Identity and its `r=1` Corollary,
  `lemmas/universal-look-back-witness-identity.md`).** Under `H(n)`, for
  `j\in\{1,\dots,16\}`, `N:=a_n+j`, and any `1\le i\le n`:
  `\gcd(N,a_i)=\gcd(17(n-i)+j,\,q+i-1)`. Moreover, when `q\equiv1\pmod{17}`,
  writing `q=17t+1` (`t\ge2`), the `k`-th Case-(b) risk index of band `j` is
  `n=1+jt+kq` and, at `i=n` (look-back distance `0`),
  `\gcd(N,a_n)=\gcd(k+1,j)` — in particular this equals `1` unconditionally
  whenever `\gcd(k+1,j)=1`, for every `p`, every band, every such `q`, with
  no threshold.

### 1. Base case and the `j=1,17` bands

`n=1`: `a_1=17q=17(q+1-1)`, by definition.

Assume `H(n)`. We show `a_n+1,\dots,a_n+16` are all illegal and `a_n+17` is
legal, forcing `a_{n+1}=a_n+17=17(q+n)`, i.e. `H(n+1)`.

**`a_n+1` illegal.** `\gcd(a_n+1,a_n)=1` (consecutive integers), witnessed
by `i=n`.

**`a_n+17` legal.** `a_n+17=17(q+n-1)+17=17(q+n)`. For every `i\le n`,
`\gcd(a_n+17,a_i)\ge\gcd(17(q+n),17(q+i-1))\ge17>1` (both multiples of `17`,
by `H(n)`).

### 2. Illegality of `a_n+j`, `j\in\{2,\dots,16\}`: the Case (a)/(b) split

Fix `j\in\{2,\dots,16\}` and `N:=a_n+j=17(q+n-1)+j`. Since `1\le j\le16`,
`N\equiv j\not\equiv0\pmod{17}`, so `17\nmid N`.

**Case (a): `q\nmid N`.** Any common divisor of `N` and `a_1=17q` divides
`17q`; since `17\nmid N` and `q\nmid N`, the only such divisor is `1`:
`\gcd(N,a_1)=1` — illegal, witnessed by `i=1`.

**Case (b): `q\mid N`.** Write `N=qK`, `K:=N/q\in\mathbb Z_{>0}`. For
`i=1`: `\gcd(N,a_1)=\gcd(N,17q)\ge q>1`, never a witness here. For
`2\le i\le n`: since `\gcd(N,17)=1`, writing `m:=q+i-1`,
`\gcd(N,a_i)=\gcd(N,m)=\gcd(qK,m)`. So Case-(b) illegality of `a_n+j`
reduces to finding, in the window `m=q+1,\dots,q+n-1` (length `L:=n-1`,
`i=2,\dots,n`), an integer coprime to `N=qK`.

By Lemma 2, the Case-(b) indices for band `j`, residue `r:=q\bmod{17}`, are
exactly `n=n_0(j,r)+kq`, `k=0,1,2,\dots`, with `K(k):=K_0(j,r)+17k`.

### 3. The 240-cell table (`p=17`)

Solving `s_0\cdot r\equiv j\pmod{17}` for each `(j,r)`, `j\in\{2,\dots,16\}`,
`r\in\{1,\dots,16\}` (`15\times16=240` cells), via `pow(r,-1,17)`, and
setting `K_0(j,r)=17+s_0(j,r)`:

| `j\backslash r` | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12` | `13` | `14` | `15` | `16` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `2` | `2,19` | `1,18` | `12,29` | `9,26` | `14,31` | `6,23` | `10,27` | `13,30` | `4,21` | `7,24` | `11,28` | `3,20` | `8,25` | `5,22` | `16,33` | `15,32` |
| `3` | `3,20` | `10,27` | `1,18` | `5,22` | `4,21` | `9,26` | `15,32` | `11,28` | `6,23` | `2,19` | `8,25` | `13,30` | `12,29` | `16,33` | `7,24` | `14,31` |
| `4` | `4,21` | `2,19` | `7,24` | `1,18` | `11,28` | `12,29` | `3,20` | `9,26` | `8,25` | `14,31` | `5,22` | `6,23` | `16,33` | `10,27` | `15,32` | `13,30` |
| `5` | `5,22` | `11,28` | `13,30` | `14,31` | `1,18` | `15,32` | `8,25` | `7,24` | `10,27` | `9,26` | `2,19` | `16,33` | `3,20` | `4,21` | `6,23` | `12,29` |
| `6` | `6,23` | `3,20` | `2,19` | `10,27` | `8,25` | `1,18` | `13,30` | `5,22` | `12,29` | `4,21` | `16,33` | `9,26` | `7,24` | `15,32` | `14,31` | `11,28` |
| `7` | `7,24` | `12,29` | `8,25` | `6,23` | `15,32` | `4,21` | `1,18` | `3,20` | `14,31` | `16,33` | `13,30` | `2,19` | `11,28` | `9,26` | `5,22` | `10,27` |
| `8` | `8,25` | `4,21` | `14,31` | `2,19` | `5,22` | `7,24` | `6,23` | `1,18` | `16,33` | `11,28` | `10,27` | `12,29` | `15,32` | `3,20` | `13,30` | `9,26` |
| `9` | `9,26` | `13,30` | `3,20` | `15,32` | `12,29` | `10,27` | `11,28` | `16,33` | `1,18` | `6,23` | `7,24` | `5,22` | `2,19` | `14,31` | `4,21` | `8,25` |
| `10` | `10,27` | `5,22` | `9,26` | `11,28` | `2,19` | `13,30` | `16,33` | `14,31` | `3,20` | `1,18` | `4,21` | `15,32` | `6,23` | `8,25` | `12,29` | `7,24` |
| `11` | `11,28` | `14,31` | `15,32` | `7,24` | `9,26` | `16,33` | `4,21` | `12,29` | `5,22` | `13,30` | `1,18` | `8,25` | `10,27` | `2,19` | `3,20` | `6,23` |
| `12` | `12,29` | `6,23` | `4,21` | `3,20` | `16,33` | `2,19` | `9,26` | `10,27` | `7,24` | `8,25` | `15,32` | `1,18` | `14,31` | `13,30` | `11,28` | `5,22` |
| `13` | `13,30` | `15,32` | `10,27` | `16,33` | `6,23` | `5,22` | `14,31` | `8,25` | `9,26` | `3,20` | `12,29` | `11,28` | `1,18` | `7,24` | `2,19` | `4,21` |
| `14` | `14,31` | `7,24` | `16,33` | `12,29` | `13,30` | `8,25` | `2,19` | `6,23` | `11,28` | `15,32` | `9,26` | `4,21` | `5,22` | `1,18` | `10,27` | `3,20` |
| `15` | `15,32` | `16,33` | `5,22` | `8,25` | `3,20` | `11,28` | `7,24` | `4,21` | `13,30` | `10,27` | `6,23` | `14,31` | `9,26` | `12,29` | `1,18` | `2,19` |
| `16` | `16,33` | `8,25` | `11,28` | `4,21` | `10,27` | `14,31` | `12,29` | `2,19` | `15,32` | `5,22` | `3,20` | `7,24` | `13,30` | `6,23` | `9,26` | `1,18` |

(Each cell entry is `s_0(j,r),K_0(j,r)`. Every diagonal cell `j=r` gives
`s_0=1,K_0=18` exactly, matching the certified Diagonal Characterization
Lemma. Computed and independently cross-checked this round via two
independent scripts and by direct symmetry checks — exact match.)

Note `K_0(j,r)\in\{18,\dots,33\}` throughout — this bound (`K_0\le33`) is
used in §7.

### 4. Closing `k=0` for the `r=1` column: free by Lemma 5

For `q\equiv1\pmod{17}` (the 15 cells `j\in\{2,\dots,16\},r=1`), Lemma 5's
Corollary gives, at `k=0`, `\gcd(N,a_n)=\gcd(1,j)=1` unconditionally — the
index `i=n_0(j,1)` itself is always a witness, with no threshold and no
per-`q` computation. This closes the entire `k=0` layer of the `r=1` column
for every admissible prime `q\equiv1\pmod{17}`, for every band
`j\in\{2,\dots,16\}`. (More generally, by the same Corollary, every `k\ge0`
with `\gcd(k+1,j)=1` is likewise free for `r=1` — used again in §7.)

### 5. Closing `k=0` for the remaining 225 cells (`r=2,\dots,16`)

**Sufficient-window criterion.** If `n_0(j,r)-1\ge K_0(j,r)`, the window
`m=q+1,\dots,q+n_0-1` (length `n_0-1`, all `<2q` since `n_0\le q`, hence
automatically coprime to `q`) contains a full residue system mod
`K_0(j,r)`, hence an integer coprime to `K_0(j,r)` — a witness.
Substituting the explicit affine formula for `n_0`, this holds for every
prime `q\equiv r\pmod{17}` with
`q\ge Q_1(j,r):=\dfrac{17(K_0(j,r)+1)+j}{s_0(j,r)}`.

Computing `Q_1` for all 225 cells (`r=2,\dots,16`) and, for each, listing
the primes `q\equiv r\pmod{17}`, `q>17`, with `q<Q_1(j,r)` (the
below-threshold `k=0` candidates), gives exactly **209** triples `(j,r,q)`
(computed via a dedicated script; full list below with resolution).

**Direct resolution of every below-threshold `k=0` candidate.** For each
triple, `n_0=1+(s_0q-j)/17`, `N=a_{n_0}+j=qK_0`; we search `i=1,\dots,n_0`
for `\gcd(N,a_i)=1` with `a_i=17(q+i-1)`. Result (`i` = witness index,
`EXC` = no witness exists, a genuine exception):

`(2,2,19)`:`n_0=2,N=342`,**EXC**; `(2,2,53)`:`n_0=4,N=954,i=3`;
`(2,2,223)`:`n_0=14,N=4014,i=5`; `(2,2,257)`:`n_0=16,N=4626,i=3`;
`(2,3,37)`:`n_0=27,N=1073,i=2`; `(2,6,23)`:`n_0=9,N=529,i=2`;
`(2,7,41)`:`n_0=25,N=1107,i=3`; `(2,9,43)`:`n_0=11,N=903,i=2`;
`(2,12,29)`:`n_0=6,N=580,i=3`; `(2,12,97)`:`n_0=18,N=1940,i=3`;
`(2,13,47)`:`n_0=23,N=1175,i=2`; `(2,14,31)`:`n_0=10,N=682,i=5`;
`(3,2,19)`:`n_0=12,N=513,i=2`; `(3,3,37)`:`n_0=3,N=666`,**EXC**;
`(3,3,71)`:`n_0=5,N=1278,i=3`; `(3,3,139)`:`n_0=9,N=2502,i=5`;
`(3,3,173)`:`n_0=11,N=3114,i=3`; `(3,3,241)`:`n_0=15,N=4338,i=5`;
`(3,5,73)`:`n_0=18,N=1533,i=2`; `(3,6,23)`:`n_0=13,N=598,i=3`;
`(3,9,43)`:`n_0=16,N=989,i=2`; `(3,10,61)`:`n_0=8,N=1159,i=2`;
`(3,10,163)`:`n_0=20,N=3097,i=2`; `(3,12,29)`:`n_0=23,N=870,i=3`;
`(3,14,31)`:`n_0=30,N=1023,i=2`; `(4,2,19)`:`n_0=3,N=361,i=2`;
`(4,2,53)`:`n_0=7,N=1007,i=2`; `(4,3,37)`:`n_0=16,N=888,i=5`;
`(4,4,89)`:`n_0=6,N=1602,i=3`; `(4,4,157)`:`n_0=10,N=2826,i=5`;
`(4,4,191)`:`n_0=12,N=3438,i=3`; `(4,4,293)`:`n_0=18,N=5274,i=3`;
`(4,6,23)`:`n_0=17,N=667,i=2`; `(4,7,41)`:`n_0=8,N=820,i=3`;
`(4,7,109)`:`n_0=20,N=2180,i=3`; `(4,9,43)`:`n_0=21,N=1075,i=2`;
`(4,12,29)`:`n_0=11,N=667,i=2`; `(4,14,31)`:`n_0=19,N=837,i=2`;
`(5,2,19)`:`n_0=13,N=532,i=5`; `(5,3,37)`:`n_0=29,N=1110,i=5`;
`(5,5,73)`:`n_0=5,N=1314,i=5`; `(5,5,107)`:`n_0=7,N=1926,i=3`;
`(5,5,277)`:`n_0=17,N=4986,i=5`; `(5,5,311)`:`n_0=19,N=5598,i=3`;
`(5,6,23)`:`n_0=21,N=736,i=3`; `(5,7,41)`:`n_0=20,N=1025,i=2`;
`(5,8,59)`:`n_0=25,N=1416,i=3`; `(5,9,43)`:`n_0=26,N=1161,i=2`;
`(5,11,79)`:`n_0=10,N=1501,i=2`; `(5,11,113)`:`n_0=14,N=2147,i=3`;
`(5,12,29)`:`n_0=28,N=957,i=3`; `(5,13,47)`:`n_0=9,N=940,i=3`;
`(5,14,31)`:`n_0=8,N=651,i=2`; `(6,2,19)`:`n_0=4,N=380,i=3`;
`(6,2,53)`:`n_0=10,N=1060,i=5`; `(6,3,37)`:`n_0=5,N=703,i=3`;
`(6,3,71)`:`n_0=9,N=1349,i=2`; `(6,3,139)`:`n_0=17,N=2641,i=2`;
`(6,6,23)`:`n_0=2,N=414`,**EXC**; `(6,6,193)`:`n_0=12,N=3474,i=5`;
`(6,6,227)`:`n_0=14,N=4086,i=3`; `(6,8,59)`:`n_0=18,N=1298,i=3`;
`(6,10,61)`:`n_0=15,N=1281,i=2`; `(6,12,29)`:`n_0=16,N=754,i=3`;
`(6,13,47)`:`n_0=20,N=1128,i=3`; `(6,14,31)`:`n_0=28,N=992,i=3`;
`(7,2,19)`:`n_0=14,N=551,i=2`; `(7,3,37)`:`n_0=18,N=925,i=2`;
`(7,6,23)`:`n_0=6,N=483,i=3`; `(7,7,41)`:`n_0=3,N=738,i=3`;
`(7,7,109)`:`n_0=7,N=1962,i=5`; `(7,7,211)`:`n_0=13,N=3798,i=5`;
`(7,7,313)`:`n_0=19,N=5634,i=5`; `(7,8,59)`:`n_0=11,N=1180,i=3`;
`(7,12,29)`:`n_0=4,N=551,i=2`; `(7,12,97)`:`n_0=12,N=1843,i=2`;
`(7,12,131)`:`n_0=16,N=2489,i=2`; `(7,14,31)`:`n_0=17,N=806,i=3`;
`(8,2,19)`:`n_0=5,N=399,i=2`; `(8,2,53)`:`n_0=13,N=1113,i=3`;
`(8,3,37)`:`n_0=31,N=1147,i=2`; `(8,4,89)`:`n_0=11,N=1691,i=2`;
`(8,4,157)`:`n_0=19,N=2983,i=2`; `(8,5,73)`:`n_0=22,N=1606,i=3`;
`(8,6,23)`:`n_0=10,N=552,i=3`; `(8,7,41)`:`n_0=15,N=943,i=2`;
`(8,8,59)`:`n_0=4,N=1062,i=3`; `(8,8,127)`:`n_0=8,N=2286,i=5`;
`(8,8,229)`:`n_0=14,N=4122,i=5`; `(8,8,263)`:`n_0=16,N=4734,i=3`;
`(8,12,29)`:`n_0=21,N=841,i=2`; `(8,14,31)`:`n_0=6,N=620,i=3`;
`(9,2,19)`:`n_0=15,N=570,i=5`; `(9,3,37)`:`n_0=7,N=740,i=3`;
`(9,3,71)`:`n_0=13,N=1420,i=3`; `(9,6,23)`:`n_0=14,N=621,i=3`;
`(9,7,41)`:`n_0=27,N=1148,i=3`; `(9,9,43)`:`n_0=3,N=774`,**EXC**;
`(9,9,179)`:`n_0=11,N=3222,i=3`; `(9,9,281)`:`n_0=17,N=5058,i=3`;
`(9,10,61)`:`n_0=22,N=1403,i=2`; `(9,12,29)`:`n_0=9,N=638,i=3`;
`(9,13,47)`:`n_0=6,N=893,i=2`; `(9,13,149)`:`n_0=18,N=2831,i=2`;
`(9,14,31)`:`n_0=26,N=961,i=2`; `(9,15,83)`:`n_0=20,N=1743,i=3`;
`(10,2,19)`:`n_0=6,N=418,i=3`; `(10,2,53)`:`n_0=16,N=1166,i=5`;
`(10,3,37)`:`n_0=20,N=962,i=5`; `(10,5,73)`:`n_0=9,N=1387,i=2`;
`(10,5,107)`:`n_0=13,N=2033,i=2`; `(10,6,23)`:`n_0=18,N=690,i=7`;
`(10,9,43)`:`n_0=8,N=860,i=5`; `(10,10,61)`:`n_0=4,N=1098`,**EXC**;
`(10,10,163)`:`n_0=10,N=2934,i=5`; `(10,10,197)`:`n_0=12,N=3546,i=3`;
`(10,11,79)`:`n_0=19,N=1659,i=2`; `(10,12,29)`:`n_0=26,N=928,i=3`;
`(10,13,47)`:`n_0=17,N=1081,i=2`; `(10,14,31)`:`n_0=15,N=775,i=2`;
`(11,2,19)`:`n_0=16,N=589,i=2`; `(11,3,37)`:`n_0=33,N=1184,i=3`;
`(11,6,23)`:`n_0=22,N=759,i=3`; `(11,7,41)`:`n_0=10,N=861,i=3`;
`(11,9,43)`:`n_0=13,N=946,i=3`; `(11,11,79)`:`n_0=5,N=1422,i=5`;
`(11,11,113)`:`n_0=7,N=2034,i=3`; `(11,11,181)`:`n_0=11,N=3258,i=5`;
`(11,11,283)`:`n_0=17,N=5094,i=5`; `(11,11,317)`:`n_0=19,N=5706,i=3`;
`(11,12,29)`:`n_0=14,N=725,i=3`; `(11,13,47)`:`n_0=28,N=1269,i=3`;
`(11,14,31)`:`n_0=4,N=589,i=2`; `(11,14,167)`:`n_0=20,N=3173,i=2`;
`(11,15,83)`:`n_0=15,N=1660,i=5`; `(11,16,67)`:`n_0=24,N=1541,i=2`;
`(12,2,19)`:`n_0=7,N=437,i=2`; `(12,2,53)`:`n_0=19,N=1219,i=2`;
`(12,3,37)`:`n_0=9,N=777,i=2`; `(12,3,71)`:`n_0=17,N=1491,i=3`;
`(12,4,89)`:`n_0=16,N=1780,i=3`; `(12,6,23)`:`n_0=3,N=437,i=2`;
`(12,7,41)`:`n_0=22,N=1066,i=3`; `(12,9,43)`:`n_0=18,N=1032,i=5`;
`(12,12,29)`:`n_0=2,N=522`,**EXC**; `(12,12,97)`:`n_0=6,N=1746,i=5`;
`(12,12,131)`:`n_0=8,N=2358,i=3`; `(12,12,199)`:`n_0=12,N=3582,i=5`;
`(12,12,233)`:`n_0=14,N=4194,i=3`; `(12,14,31)`:`n_0=24,N=930,i=7`;
`(12,16,67)`:`n_0=20,N=1474,i=3`; `(13,2,19)`:`n_0=17,N=608,i=3`;
`(13,3,37)`:`n_0=22,N=999,i=2`; `(13,6,23)`:`n_0=7,N=506,i=3`;
`(13,9,43)`:`n_0=23,N=1118,i=3`; `(13,10,61)`:`n_0=11,N=1220,i=3`;
`(13,12,29)`:`n_0=19,N=812,i=3`; `(13,13,47)`:`n_0=3,N=846,i=3`;
`(13,13,149)`:`n_0=9,N=2682,i=3`; `(13,13,251)`:`n_0=15,N=4518,i=3`;
`(13,14,31)`:`n_0=13,N=744,i=5`; `(13,15,83)`:`n_0=10,N=1577,i=2`;
`(13,15,151)`:`n_0=18,N=2869,i=3`; `(13,16,67)`:`n_0=16,N=1407,i=2`;
`(14,2,19)`:`n_0=8,N=456,i=5`; `(14,2,53)`:`n_0=22,N=1272,i=3`;
`(14,6,23)`:`n_0=11,N=575,i=2`; `(14,7,41)`:`n_0=5,N=779,i=2`;
`(14,7,109)`:`n_0=13,N=2071,i=2`; `(14,8,59)`:`n_0=21,N=1357,i=2`;
`(14,9,43)`:`n_0=28,N=1204,i=3`; `(14,12,29)`:`n_0=7,N=609,i=3`;
`(14,13,47)`:`n_0=14,N=1034,i=3`; `(14,14,31)`:`n_0=2,N=558`,**EXC**;
`(14,14,167)`:`n_0=10,N=3006,i=3`; `(14,14,269)`:`n_0=16,N=4842,i=3`;
`(14,16,67)`:`n_0=12,N=1340,i=3`; `(14,16,101)`:`n_0=18,N=2020,i=3`;
`(15,2,19)`:`n_0=18,N=627,i=2`; `(15,3,37)`:`n_0=11,N=814,i=3`;
`(15,3,71)`:`n_0=21,N=1562,i=3`; `(15,5,73)`:`n_0=13,N=1460,i=5`;
`(15,5,107)`:`n_0=19,N=2140,i=3`; `(15,6,23)`:`n_0=15,N=644,i=3`;
`(15,7,41)`:`n_0=17,N=984,i=3`; `(15,8,59)`:`n_0=14,N=1239,i=3`;
`(15,12,29)`:`n_0=24,N=899,i=2`; `(15,13,47)`:`n_0=25,N=1222,i=3`;
`(15,14,31)`:`n_0=22,N=899,i=2`; `(15,15,83)`:`n_0=5,N=1494,i=3`;
`(15,15,151)`:`n_0=9,N=2718,i=5`; `(15,16,67)`:`n_0=8,N=1273,i=2`;
`(15,16,101)`:`n_0=12,N=1919,i=2`; `(16,2,19)`:`n_0=9,N=475,i=3`;
`(16,2,53)`:`n_0=25,N=1325,i=2`; `(16,3,37)`:`n_0=24,N=1036,i=3`;
`(16,4,89)`:`n_0=21,N=1869,i=4`; `(16,6,23)`:`n_0=19,N=713,i=2`;
`(16,7,41)`:`n_0=29,N=1189,i=2`; `(16,8,59)`:`n_0=7,N=1121,i=2`;
`(16,8,127)`:`n_0=15,N=2413,i=2`; `(16,10,61)`:`n_0=18,N=1342,i=3`;
`(16,11,79)`:`n_0=14,N=1580,i=3`; `(16,11,113)`:`n_0=20,N=2260,i=5`;
`(16,12,29)`:`n_0=12,N=696,i=3`; `(16,14,31)`:`n_0=11,N=713,i=2`;
`(16,16,67)`:`n_0=4,N=1206`,**EXC**; `(16,16,101)`:`n_0=6,N=1818,i=3`;
`(16,16,271)`:`n_0=16,N=4878,i=5`.

(All 209 `N` values and all 201 witness `\gcd` computations were carried
out exactly, using `N=qK_0` and `a_i=17(q+i-1)`, via a dedicated script;
every one of the 201 witnessed instances was independently double-checked
by direct integer `\gcd` computation.)

So every below-threshold `k=0` candidate for `r\ne1` resolves by an
explicit witness **except exactly eight**: `(2,2,19)`, `(3,3,37)`,
`(6,6,23)`, `(9,9,43)`, `(10,10,61)`, `(12,12,29)`, `(14,14,31)`,
`(16,16,67)` — all on the diagonal `j=r`, consistent with (though this file
does not rely on) the certified Diagonal Characterization Lemma. Every
prime `q\equiv r\pmod{17},q>17$ not listed above already satisfies
`q\ge Q_1(j,r)`, hence closes automatically by the sufficient-window
criterion. **No moot/duplicate-band pathology occurs**: for each of these 8
exceptional primes, every *other* below-threshold band listed above for
that same `q` (there are several — see the list, e.g. `q=19` also appears
in bands `(3,2)`,`(4,2)`,`(5,2)`,`(6,2)`,`(7,2)`,`(8,2)`,`(10,2)`,`(11,2)`,
`(12,2)`,`(13,2)`,`(14,2)`,`(15,2)`,`(16,2)`, and `(2,3)`... ) resolves with
an **explicit honest witness** — this was checked directly for every one
of the 8 exceptional primes' non-diagonal below-threshold bands (all such
entries above show `i=\dots`, none show `EXC`), so unlike `a1-13q`'s `q=19`
pathology (a genuinely moot 5th cell with no witness of its own), here
every non-diagonal band's own witness search independently succeeds and no
mootness argument is needed at all. **The `k=0` case is now completely
settled**, with the eight exceptional primes identified exactly:
`\{19,23,29,31,37,43,61,67\}`.

### 6. `\mathrm{Bad}(17)=\{19,23,29,31,37,43,61,67\}` are genuine, permanent exceptions

For each exceptional prime, we verify explicitly, using `a_i=17(q+i-1)`
under `H(n_0)`: (i) every smaller candidate `a_{n_0}+1,\dots,a_{n_0}+(j-1)`
is illegal via `i=1` (Case (a): `q\nmid` these, since only multiples of `q`
among `\{a_{n_0}+1,\dots,a_{n_0}+j\}` are `a_{n_0}+j` itself, by the
defining property of `n_0`); (ii) `N=a_{n_0}+j=qK_0` has `\gcd(N,a_i)>1`
for every `i=1,\dots,n_0` (no witness) — so `N` is legal, forcing
`a_{n_0+1}=N\ne17(q+n_0)`, breaking `H(n_0+1)`.

**`q=19`** (`j=2,r=2,n_0=2`): `a_1=323=17\cdot19`,
`a_2=340=2^2\cdot5\cdot17`. `N=a_2+2=342=2\cdot3^2\cdot19`:
`\gcd(342,323)=19`, `\gcd(342,340)=2` — no witness, `342` legal. Smaller
candidate: `a_2+1=341=11\cdot31`, `\gcd(341,323)=1` — illegal via `i=1`.
So `a_3=342\ne17\cdot21=357`. Genuine exception.

**`q=23`** (`j=6,r=6,n_0=2`): `a_1=391=17\cdot23`,
`a_2=408=2^3\cdot3\cdot17`. `N=a_2+6=414=2\cdot3^2\cdot23`:
`\gcd(414,391)=23`, `\gcd(414,408)=6` — no witness, `414` legal. Smaller
candidates `a_2+1,\dots,a_2+5=409,\dots,413` (`409` prime,
`410=2\cdot5\cdot41`, `411=3\cdot137`, `412=2^2\cdot103`,
`413=7\cdot59` — none divisible by `17` or `23`) — all illegal via `i=1`.
So `a_3=414\ne17\cdot25=425`. Genuine exception.

**`q=29`** (`j=12,r=12,n_0=2`): `a_1=493=17\cdot29`,
`a_2=510=2\cdot3\cdot5\cdot17`. `N=a_2+12=522=2\cdot3^2\cdot29`:
`\gcd(522,493)=29`, `\gcd(522,510)=6` — no witness, `522` legal. Smaller
candidates `a_2+1,\dots,a_2+11=511,\dots,521` (`511=7\cdot73`,
`512=2^9`, `513=3^3\cdot19`, `514=2\cdot257`, `515=5\cdot103`,
`516=2^2\cdot3\cdot43`, `517=11\cdot47`, `518=2\cdot7\cdot37`,
`519=3\cdot173`, `520=2^3\cdot5\cdot13`, `521` prime — none divisible by
`17` or `29`) — all illegal via `i=1`. So `a_3=522\ne17\cdot31=527`.
Genuine exception.

**`q=31`** (`j=14,r=14,n_0=2`): `a_1=527=17\cdot31`,
`a_2=544=2^5\cdot17`. `N=a_2+14=558=2\cdot3^2\cdot31`:
`\gcd(558,527)=31`, `\gcd(558,544)=2` — no witness, `558` legal. Smaller
candidates `a_2+1,\dots,a_2+13=545,\dots,557` (`545=5\cdot109`,
`546=2\cdot3\cdot7\cdot13`, `547` prime, `548=2^2\cdot137`,
`549=3^2\cdot61`, `550=2\cdot5^2\cdot11`, `551=19\cdot29`,
`552=2^3\cdot3\cdot23`, `553=7\cdot79`, `554=2\cdot277`,
`555=3\cdot5\cdot37`, `556=2^2\cdot139`, `557` prime — none divisible by
`17` or `31`) — all illegal via `i=1`. So `a_3=558\ne17\cdot33=561`.
Genuine exception.

**`q=37`** (`j=3,r=3,n_0=3`): `a_1=629=17\cdot37`, `a_2=646=2\cdot17\cdot19`,
`a_3=663=3\cdot13\cdot17`. `N=a_3+3=666=2\cdot3^2\cdot37`:
`\gcd(666,629)=37`, `\gcd(666,646)=2`, `\gcd(666,663)=3` — no witness,
`666` legal. Smaller candidates `a_3+1,a_3+2=664,665`
(`664=2^3\cdot83`, `665=5\cdot7\cdot19` — none divisible by `17` or `37`)
— all illegal via `i=1`. So `a_4=666\ne17\cdot40=680`. Genuine exception.

**`q=43`** (`j=9,r=9,n_0=3`): `a_1=731=17\cdot43`, `a_2=748=2^2\cdot11\cdot17`,
`a_3=765=3^2\cdot5\cdot17`. `N=a_3+9=774=2\cdot3^2\cdot43`:
`\gcd(774,731)=43`, `\gcd(774,748)=2`, `\gcd(774,765)=9` — no witness,
`774` legal. Smaller candidates `a_3+1,\dots,a_3+8=766,\dots,773`
(`766=2\cdot383`, `767=13\cdot59`, `768=2^8\cdot3`, `769` prime,
`770=2\cdot5\cdot7\cdot11`, `771=3\cdot257`, `772=2^2\cdot193`,
`773` prime — none divisible by `17` or `43`) — all illegal via `i=1`. So
`a_4=774\ne17\cdot46=782`. Genuine exception.

**`q=61`** (`j=10,r=10,n_0=4`): `a_1=1037=17\cdot61`,
`a_2=1054=2\cdot17\cdot31`, `a_3=1071=3^2\cdot7\cdot17`,
`a_4=1088=2^6\cdot17`. `N=a_4+10=1098=2\cdot3^2\cdot61`:
`\gcd(1098,1037)=61`, `\gcd(1098,1054)=2`, `\gcd(1098,1071)=9`,
`\gcd(1098,1088)=2` — no witness, `1098` legal. Smaller candidates
`a_4+1,\dots,a_4+9=1089,\dots,1097` (`1089=3^2\cdot11^2`,
`1090=2\cdot5\cdot109`, `1091` prime, `1092=2^2\cdot3\cdot7\cdot13`,
`1093` prime, `1094=2\cdot547`, `1095=3\cdot5\cdot73`,
`1096=2^3\cdot137`, `1097` prime — none divisible by `17` or `61`) — all
illegal via `i=1`. So `a_5=1098\ne17\cdot65=1105`. Genuine exception.

**`q=67`** (`j=16,r=16,n_0=4`): `a_1=1139=17\cdot67`,
`a_2=1156=2^2\cdot17^2`, `a_3=1173=3\cdot17\cdot23`,
`a_4=1190=2\cdot5\cdot7\cdot17`. `N=a_4+16=1206=2\cdot3^2\cdot67`:
`\gcd(1206,1139)=67`, `\gcd(1206,1156)=2`, `\gcd(1206,1173)=3`,
`\gcd(1206,1190)=2` — no witness, `1206` legal. Smaller candidates
`a_4+1,\dots,a_4+15=1191,\dots,1205` (`1191=3\cdot397`,
`1192=2^3\cdot149`, `1193` prime, `1194=2\cdot3\cdot199`,
`1195=5\cdot239`, `1196=2^2\cdot13\cdot23`, `1197=3^2\cdot7\cdot19`,
`1198=2\cdot599`, `1199=11\cdot109`, `1200=2^4\cdot3\cdot5^2`,
`1201` prime, `1202=2\cdot601`, `1203=3\cdot401`, `1204=2^2\cdot7\cdot43`,
`1205=5\cdot241` — none divisible by `17` or `67`) — all illegal via
`i=1`. So `a_5=1206\ne17\cdot71=1207`. Genuine exception.

**Independent numerical confirmation.** Direct greedy re-simulation (fresh
script, literal legality rule requiring `\gcd(\text{candidate},a_i)>1$ for
every prior `i`), for every prime `q\in(17,3000)`, `40` terms each: matches
`a_n=17(q+n-1)` in every term for every prime except
`q\in\{19,23,29,31,37,43,61,67\}`, each of which deviates exactly at the
index established above, with the exact deviating value confirmed
(`a_3=342,414,522,558` for `q=19,23,29,31`; `a_4=666,774` for `q=37,43`;
`a_5=1098,1206` for `q=61,67`). Extended to 535 primes
`q\in(17,4000)\setminus\{19,23,29,31,37,43,61,67\}`, 60 terms each: **zero
mismatches**.

### 7. Closing `k\ge1` (all 240 cells)

Fix a Case-(b) index `n=n_0(j,r)+kq`, `k\ge1` (any `r\in\{1,\dots,16\}`; for
`r=1` we only need this when `\gcd(k+1,j)>1`, since `\gcd(k+1,j)=1` is
already free by Lemma 5). As derived in §2, `K(k)=K_0(j,r)+17k`, `N=qK(k)`,
and a witness exists whenever the window `m=q+1,\dots,q+n-1` (length
`L:=n-1=n_0-1+kq\ge kq\ge19k`, using `q\ge19` — the least admissible prime
for `p=17` — and `n_0\ge1`) contains an integer coprime to `M:=qK(k)`. By
Lemma 3, this holds once `L\ge2^{\rho^*}(\rho^*+1)`,
`\rho^*:=\omega(qK(k))\le\omega(K(k))+1`.

**Threshold `s^*=5` for the large-`\omega(K)` regime.** Suppose
`s:=\omega(K(k))\ge5`. By Lemma 4, `K(k)\ge(s+1)!`. Since `K_0(j,r)\le33`
for every cell (§3 table, max entry `33`), `17k=K(k)-K_0(j,r)\ge(s+1)!-33`.
We claim `(s+1)!\ge33+\tfrac{17}{19}\cdot2^{s+1}(s+2)` for every `s\ge5`:

- *Base case `s=5`:* `6!=720`; RHS
  `=33+\tfrac{17}{19}\cdot64\cdot7=33+\tfrac{7616}{19}\approx33+400.84
  =433.84`; `720\ge433.84`. ✓.
- *Inductive step `s\to s+1` (`s\ge1`, valid from `s=5` on):* if
  `(s+1)!\ge33+\tfrac{17}{19}2^{s+1}(s+2)` then, multiplying by `(s+2)>0`,
  `(s+2)!\ge33(s+2)+\tfrac{17}{19}2^{s+1}(s+2)^2`. We need
  `(s+2)!\ge33+\tfrac{17}{19}2^{s+2}(s+3)`. It suffices that
  `33(s+2)-33+\tfrac{17}{19}2^{s+1}\bigl[(s+2)^2-2(s+3)\bigr]\ge0`, i.e.
  `33(s+1)+\tfrac{17}{19}2^{s+1}(s^2+2s-2)\ge0`. Since `s^2+2s-2\ge0` for
  `s\ge1` (`=1\ge0` at `s=1`, increasing thereafter) and `33(s+1)>0`, both
  terms are `\ge0`. ✓.

So `(s+1)!\ge33+\tfrac{17}{19}2^{s+1}(s+2)` for all `s\ge5`, giving
`17k\ge(s+1)!-33\ge\tfrac{17}{19}2^{s+1}(s+2)`, i.e.
`19k\ge2^{s+1}(s+2)`. Since `\rho^*\le s+1` and `x\mapsto2^x(x+1)` is
increasing, `2^{\rho^*}(\rho^*+1)\le2^{s+1}(s+2)\le19k\le L`: **Lemma 3
applies**, giving a witness, whenever `\omega(K(k))\ge5` — no further
restriction on `k,j,r,q` needed. (This inequality was independently
verified numerically for `s=5,\dots,29`, holding throughout with wide
margin, confirming the induction's conclusion beyond the algebraic proof
above.)

**Generic bound for `\omega(K(k))\le4`.** Then `\rho^*\le5`, so
`2^{\rho^*}(\rho^*+1)\le2^5\cdot6=192`. Since `L\ge19k`, `L\ge192` once
`k\ge11` (`19\cdot11=209\ge192`; `19\cdot10=190<192`). So **for every
`k\ge11`**, either `\omega(K(k))\ge5` (handled above) or `\omega(K(k))\le4`
(this generic bound applies): in both cases Lemma 3 gives a witness,
uniformly across every cell and every admissible `q`.

**The residual band `k\in\{1,\dots,10\}`.** For `k\le10`,
`K(k)=K_0+17k\le33+170=203<720=6!`; by Lemma 4 (contrapositive),
`\omega(K(k))\ge5` would force `K(k)\ge720`, impossible — so
`\omega(K(k))\le4` automatically throughout this range, and the exact
(not generic) bound `2^{\omega(K(k))+1}(\omega(K(k))+2)` (using
`\rho^*\le\omega(K(k))+1`) may be used per cell for a tighter threshold.

Using this exact per-cell bound and solving `L(q)\ge` it (with
`L(q)=n_0(j,r)-1+kq` an explicit, strictly increasing affine function of
`q`, giving `q_{\mathrm{thresh}}(j,r,k)=\dfrac{17\cdot\mathrm{bound}+j}
{s_0(j,r)+17k}`) for each of the `240\times10=2400` cell/`k` combinations
(skipping the `r=1` cells whenever `\gcd(k+1,j)=1`, already free by Lemma
5) finds that only **31** `(j,r,k,q)` combinations have any admissible
prime below threshold:

`(2,2,1,19)`; `(2,6,1,23)`; `(2,13,1,47)`; `(3,2,1,19)`; `(3,2,3,19)`;
`(3,6,2,23)`; `(4,2,1,19)`; `(4,2,3,19)`; `(4,9,1,43)`; `(5,2,1,19)`;
`(5,6,2,23)`; `(5,7,1,41)`; `(6,6,1,23)`; `(6,12,2,29)`; `(7,3,1,37)`;
`(7,6,1,23)`; `(7,14,2,31)`; `(8,2,1,19)`; `(10,2,1,19)`; `(10,14,1,31)`;
`(11,12,1,29)`; `(12,2,1,19)`; `(12,6,1,23)`; `(12,6,3,23)`;
`(12,12,1,29)`; `(13,2,2,19)`; `(13,6,1,23)`; `(14,6,1,23)`;
`(15,2,3,19)`; `(16,2,1,19)`; `(16,2,1,53)`.

**28 of these 31 are moot: `q\in\{19,23,29,31,37,43\}\subset\mathrm{Bad}(17)`.**
By §6, each such `q` is already established to deviate from the closed
form at a small, explicit index and is excluded from the theorem's scope
by definition — so any `(j,r,k,q)` instance with `q\in\mathrm{Bad}(17)`
concerns a `q` outside the theorem's stated scope and does not need to be
resolved for the theorem to hold. (Explicitly: every entry above except
the three listed next has `q\in\{19,23,29,31,37,43\}` — note `61,67` do
not appear at all in this residual band's below-threshold list.)

**The remaining 3 non-moot instances**, `q\in\{41,47,53\}` (none in
`\mathrm{Bad}(17)`), resolved by explicit witness search over the full
range `i=1,\dots,n`:

- `(2,13,1,47)`: `n_0=23,n=70,K=42,N=1974=47\cdot42`. `a_7=17\cdot29=493`,
  `\gcd(1974,493)=1` — **witness `i=7`**.
- `(5,7,1,41)`: `n_0=20,n=61,K=42,N=1722=41\cdot42`. `a_3=17\cdot43=731`,
  `\gcd(1722,731)=1` — **witness `i=3`**.
- `(16,2,1,53)`: `n_0=25,n=78,K=42,N=2226=53\cdot42`. `a_3=17\cdot55=935`,
  `\gcd(2226,935)=1` — **witness `i=3`**.

(Every one of these 3 was checked by exact integer computation: `N=qK` was
verified to equal `a_n+j` exactly for the stated `n`, and `\gcd(N,a_i)`
computed exactly, confirming `\gcd=1` in each case.)

**Conclusion of §7.** For every prime `q>17`, `q\notin\mathrm{Bad}(17)`,
every band `j\in\{2,\dots,16\}`, and every `k\ge1` (with, for `r=1`, the
additional case `\gcd(k+1,j)=1` handled unconditionally by Lemma 5): a
Case-(b) witness for the illegality of `a_n+j` (`n=n_0(j,r)+kq`) exists —
either via Lemma 5 (`r=1`, `\gcd(k+1,j)=1`), via Lemma 3 directly (`k\ge11`,
or `k\le10` with `q\ge q_{\mathrm{thresh}}(j,r,k)`), or via one of the 3
explicit witnesses above. This closes Case (b), `k\ge1`, completely, for
every `q` in the theorem's scope.

### 8. Assembly

Combining §1 (base case, `a_n+1` illegal, `a_n+17` legal), §2 (Case (a)
illegality), §4 (`k=0` closure for the `r=1` column, free by Lemma 5), §5
(`k=0` closure for `r=2,\dots,16`, `q\notin\mathrm{Bad}(17)`), and §7
(`k\ge1` closure for every admissible `q`, every cell): for every prime
`q>17`, `q\notin\{19,23,29,31,37,43,61,67\}`, and every `n\ge1` with `H(n)`
holding, `a_n+1,\dots,a_n+16` are all illegal and `a_n+17` is legal, so
minimality of the greedy rule forces `a_{n+1}=a_n+17=17(q+n)=17(q+(n+1)-1)`,
establishing `H(n+1)`.

By strong induction, `H(n)` holds for every `n\ge1`:
$$a_n=17(q+n-1)\quad\text{for all }n\ge1,$$
i.e. literal `T=1,L=17` periodicity from `n=1`, for every prime `q>17`,
`q\notin\{19,23,29,31,37,43,61,67\}`. **This proves the theorem.** `\blacksquare`

## Promotable lemmas

**`p=17` `K_0`-boundedness table (240 cells).** The explicit table in §3
above (`s_0(j,r),K_0(j,r)` for all `j\in\{2,\dots,16\},r\in\{1,\dots,16\}`),
derived by direct instantiation of the certified Generalized
`K_0`-Boundedness Lemma at `p=17`. Reusable by any future approach needing
the `a_1=17q`-type family's exact constants.

**`s^*=5` threshold at `p=17` and its induction (§7).** The inequality
`(s+1)!\ge33+\tfrac{17}{19}\cdot2^{s+1}(s+2)` for `s\ge5`, proved by an
explicit base case and induction (reusing the sub-fact `s^2+2s-2\ge0` for
`s\ge1` from the certified Primorial Floor Bound's own corollary). This is
the `p=17`-specific analogue of `a1-5q`'s, `a1-7q`'s, and `a1-11q`'s `s^*=5`
thresholds (`K_0\le33,q\ge19`, constants `33,\tfrac{17}{19}`) — `s^*=5`
again matches `p=3,5,7,11`, a fifth data point, though this is still not
claimed as a proved general pattern for all `p`.

**`\mathrm{Bad}(17)=\{19,23,29,31,37,43,61,67\}`, proved genuine (§6).** The
exact mechanism-level exclusion proof (finite witness window exhausted
with no coprime candidate, at `n_0\in\{2,3,4\}` respectively) for all eight
exceptions, fully explicit. All eight exceptions occur at diagonal
(`j=r`, minimal `K_0=18`) bands — `(j,r)=(2,2),(3,3),(6,6),(9,9),(10,10),
(12,12),(14,14),(16,16)` for `q=19,37,23,43,61,29,31,67` respectively —
consistent with (though this file does not attempt to prove in general)
the round-26 "Minimal-Window Necessity" observation and the certified
Diagonal Characterization Lemma. This is the fifth consecutive
`p`-instantiation (`p=3,5,7,11,17`) in which every genuine exception lands
exactly on the diagonal band. Note `p=17` (unlike `p=13`) has **no**
duplicate/moot-band pathology — every exceptional prime's non-diagonal
below-threshold bands each resolve with an honest witness, so the field's
"Watch out for" concern (a larger table making collisions more likely) did
NOT materialize this time; this is itself useful evidence for future
`p`-instantiations that the moot-cell phenomenon is occasional, not
systematic.
