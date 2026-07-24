## Status
solved (round 29: the `a_1=13q` subfamily theorem is fully proved — literal
`T=1,L=13` periodicity from `n=1` for every prime `q>13`,
`q\notin\mathrm{Bad}(13)=\{17,19,23,47\}`, by instantiating the certified
`p`-uniform machinery from `a1-pq-subfamily-theorem` at `p=13`, building the
explicit 132-cell `(j,r)` table, using the certified Universal Look-Back
Witness Identity's `r=1` corollary to close the `r=1` column's `k=0` layer
unconditionally, closing the remaining 120 cells' `k=0` layer and all 132
cells' `k\ge1` layer with the certified Legendre-Sieve/Primorial-Floor
toolkit, and hand-verifying every one of the 4 genuine exceptions plus
explicitly resolving the one moot duplicate-band cell for `q=19` — the same
template as the certified `a1-5q`, `a1-7q`, and `a1-11q` theorems, scaled to
`p=13`. See "Full proof" below.)

## Approaches tried
- (round 29, outline) Instantiate the certified `p`-uniform machinery at
  `p=13`, exactly mirroring `a1-11q-subfamily-theorem.md`'s Steps 0-8. Two
  independent explorers (round 28 simulation-only, round 29 full
  table/threshold pass) confirmed `\mathrm{Bad}(13)=\{17,19,23,47\}` and a
  build-ready 132-cell table. Not built.
- (round 29, outline-reviewer) Independently re-derived `\mathrm{Bad}(13)`
  via a from-scratch greedy simulator over every prime `q\in(13,20000)`,
  exact match, including the deviation indices/values; approved as
  build-ready, flagging the `q=19` moot-cell claim as the one point requiring
  an explicit (not asserted) proof.
- (round 29, this build) Instantiated the full machinery at `p=13`: built
  the 132-cell `(j,r,s_0,K_0)` table (`sympy.mod_inverse`); closed the 12
  `r=1` cells' `k=0` layer for free via the certified Universal Look-Back
  Corollary; computed `Q_1(j,r)` for the remaining 120 cells, found exactly
  **112** below-threshold `(j,r,q)` candidates, resolved 107 by explicit
  witness search and found exactly **5** with no witness — the 4 genuine
  exceptions `(4,4,17),(6,6,19),(8,8,47),(10,10,23)` (matching
  `\mathrm{Bad}(13)` exactly) plus the moot duplicate `(12,6,19)`, whose
  vacuity is explicitly proved (not asserted) by direct simulation showing
  `q=19`'s real sequence already deviates at the smaller index `n_0=2` via
  `(6,6,19)`, so `a_3\ne13(19+2)` and the `(12,6)` band's premise `H(3)`
  never holds; verified all 4 genuine exceptions are permanent via full
  factorization hand-checks; derived the `p=13` `s^*=5` threshold
  `(s+1)!\ge25+\tfrac{13}{17}2^{s+1}(s+2)`, reducing the `k\ge1` residual
  band to `k\in\{1,\dots,11\}` and, sweeping all `132\times11=1452`
  cell/`k` combinations, found exactly **29** below-threshold
  `(j,r,k,q)` quadruples — **19 moot** (`q\in\mathrm{Bad}(13)`) and **10
  non-moot** (`q\in\{29,31,37,41,43,53,59,61\}`), all 10 resolved by
  explicit witness search. **Result: the theorem is now completely proved.**

## Current best

### Target (now proved — see Full proof)
For every prime `q>13` with `q\notin\{17,19,23,47\}`, and `a_1=13q`:
`a_n=13(q+n-1)` for every `n\ge1` — literal `T=1,L=13` periodicity from
`n=1`.

## Full proof

### 0. Setup and imported machinery

Fix a prime `q>13`, `q\notin\{17,19,23,47\}`, and `a_1=13q`. Strong-induction
hypothesis at step `n`, `H(n)`: `a_i=13(q+i-1)` for `i=1,\dots,n`. In
particular `13\mid a_i` for every such `i`, and — since `13,q` are distinct
primes — `P(a_1)=\{13,q\}`.

We use, without re-derivation, the following results, each certified in this
workspace for a general odd prime `p` (so their `p=13` instantiations below
require no new proof, only substitution):

- **Lemma 1 (Generalized gcd-difference Witness Lemma,
  `lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md`).** For
  `N:=a_n+j`, `j\in\{1,\dots,12\}`, under `H(n)`: `\gcd(N,a_n)=\gcd(N,j)`.
- **Lemma 2 (Generalized `K_0`-Boundedness, `p=13`,
  `lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md`).** For
  `j\in\{2,\dots,12\}` and prime `q>13` with `q\equiv r\pmod{13}`
  (`r\in\{1,\dots,12\}`), the first index `n_0(j,r;q)` with `q\mid(a_{n_0}+j)`
  satisfies `K_0(j,r):=(a_{n_0}+j)/q=13+s_0(j,r)`, where
  `s_0(j,r)\in\{1,\dots,12\}` is the unique solution of `s_0\cdot r\equiv
  j\pmod{13}`, and `n_0(j,r;q)=1+(s_0(j,r)q-j)/13`.
- **Lemma 3 (Legendre Sieve Gap Bound, `lemmas/legendre-sieve-gap-bound.md`).**
  For integer `M\ge2` with `\rho:=\omega(M)`, any window of `L\ge2^\rho(\rho+1)`
  consecutive integers contains one coprime to `M`.
- **Lemma 4 (Primorial Floor Bound, `lemmas/primorial-floor-bound.md`).** If
  `\omega(M)=\rho` then `M\ge(\rho+1)!`.
- **Lemma 5 (Universal Look-Back Witness Identity and its `r=1` Corollary,
  `lemmas/universal-look-back-witness-identity.md`).** Under `H(n)`, for
  `j\in\{1,\dots,12\}`, `N:=a_n+j`, and any `1\le i\le n`:
  `\gcd(N,a_i)=\gcd(13(n-i)+j,\,q+i-1)`. Moreover, when `q\equiv1\pmod{13}`,
  writing `q=13t+1` (`t` even, `t\ge2`), the `k`-th Case-(b) risk index of
  band `j` is `n=1+jt+kq` and, at `i=n` (look-back distance `0`),
  `\gcd(N,a_n)=\gcd(k+1,j)` — in particular this equals `1` unconditionally
  whenever `\gcd(k+1,j)=1`, for every `p`, every band, every such `q`, with
  no threshold.

### 1. Base case and the `j=1,13` bands

`n=1`: `a_1=13q=13(q+1-1)`, by definition.

Assume `H(n)`. We show `a_n+1,\dots,a_n+12` are all illegal and `a_n+13` is
legal, forcing `a_{n+1}=a_n+13=13(q+n)`, i.e. `H(n+1)`.

**`a_n+1` illegal.** `\gcd(a_n+1,a_n)=1` (consecutive integers), witnessed
by `i=n`.

**`a_n+13` legal.** `a_n+13=13(q+n-1)+13=13(q+n)`. For every `i\le n`,
`\gcd(a_n+13,a_i)\ge\gcd(13(q+n),13(q+i-1))\ge13>1` (both multiples of
`13`, by `H(n)`).

### 2. Illegality of `a_n+j`, `j\in\{2,\dots,12\}`: the Case (a)/(b) split

Fix `j\in\{2,\dots,12\}` and `N:=a_n+j=13(q+n-1)+j`. Since `1\le j\le12`,
`N\equiv j\not\equiv0\pmod{13}`, so `13\nmid N`.

**Case (a): `q\nmid N`.** Any common divisor of `N` and `a_1=13q` divides
`13q`; since `13\nmid N` and `q\nmid N`, the only such divisor is `1`:
`\gcd(N,a_1)=1` — illegal, witnessed by `i=1`.

**Case (b): `q\mid N`.** Write `N=qK`, `K:=N/q\in\mathbb Z_{>0}`. For
`i=1`: `\gcd(N,a_1)=\gcd(N,13q)\ge q>1`, never a witness here. For
`2\le i\le n`: since `\gcd(N,13)=1`, writing `m:=q+i-1`,
`\gcd(N,a_i)=\gcd(N,m)=\gcd(qK,m)`. So Case-(b) illegality of `a_n+j`
reduces to finding, in the window `m=q+1,\dots,q+n-1` (length `L:=n-1`,
`i=2,\dots,n`), an integer coprime to `N=qK`.

By Lemma 2, the Case-(b) indices for band `j`, residue `r:=q\bmod{13}`, are
exactly `n=n_0(j,r)+kq`, `k=0,1,2,\dots`, with `K(k):=K_0(j,r)+13k`.

### 3. The 132-cell table (`p=13`)

Solving `s_0\cdot r\equiv j\pmod{13}` for each `(j,r)`, `j\in\{2,\dots,12\}`,
`r\in\{1,\dots,12\}` (132 cells), via `sympy.mod_inverse`, and setting
`K_0(j,r)=13+s_0(j,r)`:

| `j\backslash r` | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `2` | `2,15` | `1,14` | `5,18` | `7,20` | `3,16` | `9,22` | `4,17` | `10,23` | `6,19` | `8,21` | `12,25` | `11,24` |
| `3` | `3,16` | `8,21` | `1,14` | `4,17` | `11,24` | `7,20` | `6,19` | `2,15` | `9,22` | `12,25` | `5,18` | `10,23` |
| `4` | `4,17` | `2,15` | `10,23` | `1,14` | `6,19` | `5,18` | `8,21` | `7,20` | `12,25` | `3,16` | `11,24` | `9,22` |
| `5` | `5,18` | `9,22` | `6,19` | `11,24` | `1,14` | `3,16` | `10,23` | `12,25` | `2,15` | `7,20` | `4,17` | `8,21` |
| `6` | `6,19` | `3,16` | `2,15` | `8,21` | `9,22` | `1,14` | `12,25` | `4,17` | `5,18` | `11,24` | `10,23` | `7,20` |
| `7` | `7,20` | `10,23` | `11,24` | `5,18` | `4,17` | `12,25` | `1,14` | `9,22` | `8,21` | `2,15` | `3,16` | `6,19` |
| `8` | `8,21` | `4,17` | `7,20` | `2,15` | `12,25` | `10,23` | `3,16` | `1,14` | `11,24` | `6,19` | `9,22` | `5,18` |
| `9` | `9,22` | `11,24` | `3,16` | `12,25` | `7,20` | `8,21` | `5,18` | `6,19` | `1,14` | `10,23` | `2,15` | `4,17` |
| `10` | `10,23` | `5,18` | `12,25` | `9,22` | `2,15` | `6,19` | `7,20` | `11,24` | `4,17` | `1,14` | `8,21` | `3,16` |
| `11` | `11,24` | `12,25` | `8,21` | `6,19` | `10,23` | `4,17` | `9,22` | `3,16` | `7,20` | `5,18` | `1,14` | `2,15` |
| `12` | `12,25` | `6,19` | `4,17` | `3,16` | `5,18` | `2,15` | `11,24` | `8,21` | `10,23` | `9,22` | `7,20` | `1,14` |

(Each cell entry is `s_0(j,r),K_0(j,r)`. Every diagonal cell `j=r` gives
`s_0=1,K_0=14` exactly, matching the certified Diagonal Characterization
Lemma. Independently cross-checked by direct `sympy.mod_inverse` computation
and by the round-29 explorer's independent script — exact match.)

Note `K_0(j,r)\in\{14,\dots,25\}` throughout (max entry `25`) — this bound
is used in §7.

### 4. Closing `k=0` for the `r=1` column: free by Lemma 5

For `q\equiv1\pmod{13}` (the 11 cells `j\in\{2,\dots,12\},r=1`), Lemma 5's
Corollary gives, at `k=0`, `\gcd(N,a_n)=\gcd(1,j)=1` unconditionally — the
index `i=n_0(j,1)` itself is always a witness, with no threshold and no
per-`q` computation. This closes the entire `k=0` layer of the `r=1` column
for every admissible prime `q\equiv1\pmod{13}`, for every band
`j\in\{2,\dots,12\}`. (More generally, by the same Corollary, every `k\ge0`
with `\gcd(k+1,j)=1` is likewise free for `r=1` — used again in §7.)

### 5. Closing `k=0` for the remaining 120 cells (`r=2,\dots,12`)

**Sufficient-window criterion.** If `n_0(j,r)-1\ge K_0(j,r)`, the window
`m=q+1,\dots,q+n_0-1` (length `n_0-1`, all `<2q` since `n_0\le q`, hence
automatically coprime to `q`) contains a full residue system mod
`K_0(j,r)`, hence an integer coprime to `K_0(j,r)` — a witness.
Substituting the explicit affine formula for `n_0`, this holds for every
prime `q\equiv r\pmod{13}` with
`q\ge Q_1(j,r):=\dfrac{13(K_0(j,r)+1)+j}{s_0(j,r)}`.

Computing `Q_1` for all 120 cells (`r=2,\dots,12`) and, for each, listing the
primes `q\equiv r\pmod{13}`, `q>13`, with `q<Q_1(j,r)` (the below-threshold
`k=0` candidates), gives exactly **112** triples `(j,r,q)` (computed via a
dedicated script; full list below with resolution).

**Direct resolution of every below-threshold `k=0` candidate.** For each
triple, `n_0=1+(s_0q-j)/13`, `N=a_{n_0}+j=qK_0`; we search `i=1,\dots,n_0`
for `\gcd(N,a_i)=1` with `a_i=13(q+i-1)`. Result (`i` = witness index,
`EXC` = no witness exists):

`(2,2,41)`:`n_0=4,N=574,i=3`; `(2,2,67)`:`n_0=6,N=938,i=3`;
`(2,3,29)`:`n_0=12,N=522,i=3`; `(2,4,17)`:`n_0=10,N=340,i=3`;
`(2,5,31)`:`n_0=8,N=496,i=3`; `(2,6,19)`:`n_0=14,N=418,i=3`;
`(2,10,23)`:`n_0=15,N=483,i=3`; `(3,3,29)`:`n_0=3,N=406,i=3`;
`(3,3,107)`:`n_0=9,N=1498,i=3`; `(3,4,17)`:`n_0=6,N=289,i=2`;
`(3,4,43)`:`n_0=14,N=731,i=2`; `(3,6,19)`:`n_0=11,N=380,i=3`;
`(3,8,47)`:`n_0=8,N=705,i=3`; `(3,8,73)`:`n_0=12,N=1095,i=2`;
`(3,10,23)`:`n_0=22,N=575,i=2`; `(3,11,37)`:`n_0=15,N=666,i=5`;
`(4,2,41)`:`n_0=7,N=615,i=3`; `(4,2,67)`:`n_0=11,N=1005,i=2`;
`(4,3,29)`:`n_0=23,N=667,i=2`; `(4,4,17)`:`n_0=2,N=238,`**EXC**;
`(4,4,43)`:`n_0=4,N=602,i=3`; `(4,4,173)`:`n_0=14,N=2422,i=5`;
`(4,5,31)`:`n_0=15,N=589,i=2`; `(4,6,19)`:`n_0=8,N=342,i=5`;
`(4,10,23)`:`n_0=6,N=368,i=3`; `(5,3,29)`:`n_0=14,N=551,i=2`;
`(5,4,17)`:`n_0=15,N=408,i=3`; `(5,5,31)`:`n_0=3,N=434,i=3`;
`(5,5,83)`:`n_0=7,N=1162,i=3`; `(5,5,109)`:`n_0=9,N=1526,i=3`;
`(5,6,19)`:`n_0=5,N=304,i=3`; `(5,6,71)`:`n_0=17,N=1136,i=3`;
`(5,9,61)`:`n_0=10,N=915,i=2`; `(5,10,23)`:`n_0=13,N=460,i=5`;
`(5,11,37)`:`n_0=12,N=629,i=2`; `(6,2,41)`:`n_0=10,N=656,i=3`;
`(6,2,67)`:`n_0=16,N=1072,i=3`; `(6,3,29)`:`n_0=5,N=435,i=3`;
`(6,4,17)`:`n_0=11,N=357,i=3`; `(6,5,31)`:`n_0=22,N=682,i=5`;
`(6,6,19)`:`n_0=2,N=266,`**EXC**; `(6,6,71)`:`n_0=6,N=994,i=3`;
`(6,6,97)`:`n_0=8,N=1358,i=3`; `(6,6,149)`:`n_0=12,N=2086,i=3`;
`(6,8,47)`:`n_0=15,N=799,i=2`; `(6,10,23)`:`n_0=20,N=552,i=3`;
`(7,3,29)`:`n_0=25,N=696,i=3`; `(7,4,17)`:`n_0=7,N=306,i=3`;
`(7,4,43)`:`n_0=17,N=774,i=5`; `(7,5,31)`:`n_0=10,N=527,i=2`;
`(7,6,19)`:`n_0=18,N=475,i=3`; `(7,7,59)`:`n_0=5,N=826,i=3`;
`(7,7,137)`:`n_0=11,N=1918,i=3`; `(7,7,163)`:`n_0=13,N=2282,i=3`;
`(7,10,23)`:`n_0=4,N=345,i=4`; `(7,10,101)`:`n_0=16,N=1515,i=3`;
`(7,11,37)`:`n_0=9,N=592,i=3`; `(8,2,41)`:`n_0=13,N=697,i=2`;
`(8,3,29)`:`n_0=16,N=580,i=3`; `(8,4,17)`:`n_0=3,N=255,i=3`;
`(8,4,43)`:`n_0=7,N=645,i=2`; `(8,6,19)`:`n_0=15,N=437,i=2`;
`(8,7,59)`:`n_0=14,N=944,i=3`; `(8,8,47)`:`n_0=4,N=658,`**EXC**;
`(8,8,73)`:`n_0=6,N=1022,i=3`; `(8,8,151)`:`n_0=12,N=2114,i=3`;
`(8,10,23)`:`n_0=11,N=437,i=2`; `(9,3,29)`:`n_0=7,N=464,i=3`;
`(9,4,17)`:`n_0=16,N=425,i=2`; `(9,5,31)`:`n_0=17,N=620,i=3`;
`(9,6,19)`:`n_0=12,N=399,i=2`; `(9,9,61)`:`n_0=5,N=854,i=5`;
`(9,9,113)`:`n_0=9,N=1582,i=3`; `(9,9,139)`:`n_0=11,N=1946,i=3`;
`(9,9,191)`:`n_0=15,N=2674,i=3`; `(9,10,23)`:`n_0=18,N=529,i=2`;
`(9,11,37)`:`n_0=6,N=555,i=2`; `(9,11,89)`:`n_0=14,N=1335,i=3`;
`(10,2,41)`:`n_0=16,N=738,i=3`; `(10,4,17)`:`n_0=12,N=374,i=3`;
`(10,5,31)`:`n_0=5,N=465,i=2`; `(10,5,83)`:`n_0=13,N=1245,i=4`;
`(10,6,19)`:`n_0=9,N=361,i=2`; `(10,10,23)`:`n_0=2,N=322,`**EXC**;
`(10,10,101)`:`n_0=8,N=1414,i=3`; `(10,10,127)`:`n_0=10,N=1778,i=3`;
`(10,10,179)`:`n_0=14,N=2506,i=3`; `(11,3,29)`:`n_0=18,N=609,i=3`;
`(11,4,17)`:`n_0=8,N=323,i=2`; `(11,4,43)`:`n_0=20,N=817,i=2`;
`(11,5,31)`:`n_0=24,N=713,i=2`; `(11,6,19)`:`n_0=6,N=323,i=2`;
`(11,8,47)`:`n_0=11,N=752,i=3`; `(11,8,73)`:`n_0=17,N=1168,i=3`;
`(11,10,23)`:`n_0=9,N=414,i=3`; `(11,11,37)`:`n_0=3,N=518,i=3`;
`(11,11,89)`:`n_0=7,N=1246,i=5`; `(11,11,167)`:`n_0=13,N=2338,i=3`;
`(11,11,193)`:`n_0=15,N=2702,i=3`; `(11,12,103)`:`n_0=16,N=1545,i=2`;
`(12,2,41)`:`n_0=19,N=779,i=2`; `(12,3,29)`:`n_0=9,N=493,i=2`;
`(12,4,17)`:`n_0=4,N=272,i=3`; `(12,4,43)`:`n_0=10,N=688,i=3`;
`(12,5,31)`:`n_0=12,N=558,i=5`; `(12,6,19)`:`n_0=3,N=285,`**EXC (moot,
see §6)**; `(12,6,71)`:`n_0=11,N=1065,i=3`; `(12,6,97)`:`n_0=15,N=1455,
i=2`; `(12,10,23)`:`n_0=16,N=506,i=3`; `(12,11,37)`:`n_0=20,N=740,i=3`;
`(12,12,103)`:`n_0=8,N=1442,i=5`; `(12,12,181)`:`n_0=14,N=2534,i=3`.

(All 112 `N` values and all 107 witness `\gcd` computations were carried
out exactly, using `N=qK_0` and `a_i=13(q+i-1)`, via a dedicated script.)

So every below-threshold `k=0` candidate for `r\ne1` resolves by an
explicit witness **except exactly five**: `(4,4,17)`, `(6,6,19)`,
`(8,8,47)`, `(10,10,23)`, and `(12,6,19)`. The first four are genuine
exceptions, all on the diagonal `j=r`; the fifth, `(12,6,19)`, is not a
second, independent exception for `q=19` — it is a moot duplicate cell,
proved so in §6.

### 6. The `q=19` moot duplicate-band cell `(12,6)`

`q=19\equiv6\pmod{13}`, so `q=19` lies in residue class `r=6`, and there are
**two** below-threshold `k=0` cells with `r=6` for `q=19`: `(6,6,19)`
(`n_0=2`) and `(12,6,19)` (`n_0=3`), both with no witness by §5's
computation. We must show `(12,6,19)` is not a genuine second exception,
because its underlying premise — `H(3)` holding for the real sequence — is
never satisfied.

By §7 below, `(6,6,19)` is verified to be a genuine, permanent exception:
the real sequence deviates from the closed form `a_n=13(q+n-1)` exactly at
`n=n_0+1=3`, with `a_3=266\ne13(19+2)=273`. Thus the closed-form value
`a_3=273` — which is exactly the value `H(3)` asserts — never occurs in the
real greedy sequence for `q=19`. The `(12,6)` band's analysis (§5's
`n_0=3,N=285` computation) is carried out *under the hypothesis* `H(3)`
(i.e. assuming `a_3=13(19+2)=273` and asking whether `a_3+12=285` is
legal); since this hypothesis is never realized by the actual sequence for
`q=19`, the `(12,6,19)` cell's conclusion (no witness within `H(3)`'s
window) never applies to any real deviation event — it describes a
counterfactual continuation of the sequence that is preempted by the
earlier, genuine deviation at `n=2\to3` via `(6,6,19)`.

**Direct confirmation by greedy simulation.** Computing the true sequence
for `a_1=13\cdot19=247`: `a_1=247`, `a_2=260`, and at `n=2` the candidates
`a_2+1,\dots,a_2+5=261,\dots,265` are checked: `261=3^2\cdot29`,
`262=2\cdot131`, `263` (prime), `264=2^3\cdot3\cdot11`, `265=5\cdot53` — none
shares a factor with `a_1=247=13\cdot19` or `a_2=260=2^2\cdot5\cdot13`
(direct factorization, none divisible by `13` or `19`), so all five are
illegal; `a_2+6=266=2\cdot7\cdot19` is legal (`\gcd(266,247)=19`). Hence
`a_3=266`, **not** `273`. The true sequence never again equals
`13(19+n-1)` for `n\ge3` (this is the genuine exception, verified fully in
§7), so `H(3)` (which would require `a_3=273`) is false for every
subsequent step, and the `(12,6,19)` band's window computation — which
presupposes `H(3)` — never governs an actual step of the real sequence.

**No other prime among the 112 below-threshold candidates has this
duplicate-band pathology.** Scanning the full triple list in §5: the only
prime `q` appearing in more than one of the five no-witness (`EXC`) entries
is `q=19` (appearing in `(6,6,19)` and `(12,6,19)`); every other prime
(`17,47,23`) appears in exactly one `EXC` entry. Hence `q=19` is the unique
prime requiring this moot-cell argument, and it has now been given in full.

**Conclusion.** `\mathrm{Bad}(13)=\{17,19,23,47\}` exactly — four genuine
exceptions, with `q=19`'s apparent second no-witness cell correctly
identified as vacuous rather than double-counted.

### 7. `\mathrm{Bad}(13)=\{17,19,23,47\}` are genuine, permanent exceptions

For each exceptional prime, we verify explicitly, using `a_i=13(q+i-1)`
under `H(n_0)`: (i) every smaller candidate `a_{n_0}+1,\dots,a_{n_0}+(j-1)`
is illegal via `i=1` (Case (a): `q\nmid` these, since the only multiple of
`q` among `\{a_{n_0}+1,\dots,a_{n_0}+j\}` is `a_{n_0}+j` itself, by the
defining property of `n_0`); (ii) `N=a_{n_0}+j=qK_0` has `\gcd(N,a_i)>1`
for every `i=1,\dots,n_0` (no witness) — so `N` is legal, forcing
`a_{n_0+1}=N\ne13(q+n_0)`, breaking `H(n_0+1)`.

**`q=17`** (`j=4,r=4,n_0=2`): `a_1=221=13\cdot17`, `a_2=234=2\cdot3^2\cdot13`.
`N=a_2+4=238=2\cdot7\cdot17`: `\gcd(238,221)=17`, `\gcd(238,234)=2` — no
witness, `238` legal. Smaller candidates `a_2+1,a_2+2,a_2+3=235,236,237`
(`235=5\cdot47`, `236=2^2\cdot59`, `237=3\cdot79` — none divisible by `13`
or `17`) — all illegal via `i=1`. So `a_3=238\ne13\cdot19=247`. Genuine
exception.

**`q=19`** (`j=6,r=6,n_0=2`): `a_1=247=13\cdot19`, `a_2=260=2^2\cdot5\cdot13`.
`N=a_2+6=266=2\cdot7\cdot19`: `\gcd(266,247)=19`, `\gcd(266,260)=2` — no
witness, `266` legal. Smaller candidates `a_2+1,\dots,a_2+5=261,\dots,265`
(`261=3^2\cdot29`, `262=2\cdot131`, `263` prime, `264=2^3\cdot3\cdot11`,
`265=5\cdot53` — none divisible by `13` or `19`) — all illegal via `i=1`.
So `a_3=266\ne13\cdot21=273`. Genuine exception.

**`q=23`** (`j=10,r=10,n_0=2`): `a_1=299=13\cdot23`,
`a_2=312=2^3\cdot3\cdot13`. `N=a_2+10=322=2\cdot7\cdot23`:
`\gcd(322,299)=23`, `\gcd(322,312)=2` — no witness, `322` legal. Smaller
candidates `a_2+1,\dots,a_2+9=313,\dots,321` (`313` prime, `314=2\cdot157`,
`315=3^2\cdot5\cdot7`, `316=2^2\cdot79`, `317` prime, `318=2\cdot3\cdot53`,
`319=11\cdot29`, `320=2^6\cdot5`, `321=3\cdot107` — none divisible by `13`
or `23`) — all illegal via `i=1`. So `a_3=322\ne13\cdot25=325`. Genuine
exception.

**`q=47`** (`j=8,r=8,n_0=4`): `a_1=611=13\cdot47`,
`a_2=624=2^4\cdot3\cdot13`, `a_3=637=7^2\cdot13`, `a_4=650=2\cdot5^2\cdot13`.
`N=a_4+8=658=2\cdot7\cdot47`: `\gcd(658,611)=47`, `\gcd(658,624)=2`,
`\gcd(658,637)=7`, `\gcd(658,650)=2` — no witness, `658` legal. Smaller
candidates `a_4+1,\dots,a_4+7=651,\dots,657` (`651=3\cdot7\cdot31`,
`652=2^2\cdot163`, `653` prime, `654=2\cdot3\cdot109`, `655=5\cdot131`,
`656=2^4\cdot41`, `657=3^2\cdot73` — none divisible by `13` or `47`) — all
illegal via `i=1`. So `a_5=658\ne13\cdot51=663`. Genuine exception.

**Independent numerical confirmation.** A direct greedy re-simulation
(literal legality rule, checking every prior term, not an "exists"
shortcut) for every prime `q\in(13,5000)` in this build, and independently
extended to `q\in(13,20000)` by the round-29 outline-reviewer, matches
`a_n=13(q+n-1)` in every term for every prime except
`q\in\{17,19,23,47\}`, each deviating exactly at the index established
above, with the exact deviating value confirmed (`a_3=238,266,322` for
`q=17,19,23`; `a_5=658` for `q=47`). No further exceptions found up to
`q=20000`.

### 8. Closing `k\ge1` (all 132 cells)

Fix a Case-(b) index `n=n_0(j,r)+kq`, `k\ge1` (any `r\in\{1,\dots,12\}`; for
`r=1` we only need this when `\gcd(k+1,j)>1`, since `\gcd(k+1,j)=1` is
already free by Lemma 5). As derived in §2, `K(k)=K_0(j,r)+13k`, `N=qK(k)`,
and a witness exists whenever the window `m=q+1,\dots,q+n-1` (length
`L:=n-1=n_0-1+kq\ge kq\ge17k`, using `q\ge17` — the least admissible prime
for `p=13` — and `n_0\ge1`) contains an integer coprime to `M:=qK(k)`. By
Lemma 3, this holds once `L\ge2^{\rho^*}(\rho^*+1)`,
`\rho^*:=\omega(qK(k))\le\omega(K(k))+1`.

**Threshold `s^*=5` for the large-`\omega(K)` regime.** Suppose
`s:=\omega(K(k))\ge5`. By Lemma 4, `K(k)\ge(s+1)!`. Since `K_0(j,r)\le25`
for every cell (§3 table, max entry `25`), `13k=K(k)-K_0(j,r)\ge(s+1)!-25`.
We claim `(s+1)!\ge25+\tfrac{13}{17}\cdot2^{s+1}(s+2)` for every `s\ge5`:

- *Base case `s=5`:* `6!=720`; RHS
  `=25+\tfrac{13}{17}\cdot64\cdot7=25+\tfrac{5824}{17}=25+342.58\overline{82}
  =367.58\overline{82}`; `720\ge367.59`. ✓.
- *Inductive step `s\to s+1` (`s\ge1`, valid from `s=5` on):* if
  `(s+1)!\ge25+\tfrac{13}{17}2^{s+1}(s+2)` then, multiplying by `(s+2)>0`,
  `(s+2)!\ge25(s+2)+\tfrac{13}{17}2^{s+1}(s+2)^2`. We need
  `(s+2)!\ge25+\tfrac{13}{17}2^{s+2}(s+3)`. It suffices that
  `25(s+2)-25+\tfrac{13}{17}2^{s+1}\bigl[(s+2)^2-2(s+3)\bigr]\ge0`, i.e.
  `25(s+1)+\tfrac{13}{17}2^{s+1}(s^2+2s-2)\ge0`. Since `s^2+2s-2\ge0` for
  `s\ge1` (`=1\ge0` at `s=1`, increasing thereafter) and `25(s+1)>0`, both
  terms are `\ge0`. ✓.

So `(s+1)!\ge25+\tfrac{13}{17}2^{s+1}(s+2)` for all `s\ge5`, giving
`13k\ge(s+1)!-25\ge\tfrac{13}{17}2^{s+1}(s+2)`, i.e.
`17k\ge2^{s+1}(s+2)`. Since `\rho^*\le s+1` and `x\mapsto2^x(x+1)` is
increasing, `2^{\rho^*}(\rho^*+1)\le2^{s+1}(s+2)\le17k\le L`: **Lemma 3
applies**, giving a witness, whenever `\omega(K(k))\ge5` — no further
restriction on `k,j,r,q` needed.

**Generic bound for `\omega(K(k))\le4`.** Then `\rho^*\le5`, so
`2^{\rho^*}(\rho^*+1)\le2^5\cdot6=192`. Since `L\ge17k`, `L\ge192` once
`k\ge12` (`17\cdot12=204\ge192`; `17\cdot11=187<192`). So **for every
`k\ge12`**, either `\omega(K(k))\ge5` (handled above) or `\omega(K(k))\le4`
(this generic bound applies): in both cases Lemma 3 gives a witness,
uniformly across every cell and every admissible `q`.

**The residual band `k\in\{1,\dots,11\}`.** For `k\le11`,
`K(k)=K_0+13k\le25+143=168<720=6!`; by Lemma 4 (contrapositive),
`\omega(K(k))\ge5` would force `K(k)\ge720`, impossible — so
`\omega(K(k))\le4` automatically throughout this range, and the exact
(not generic) bound `2^{\omega(K(k))+1}(\omega(K(k))+2)` (using
`\rho^*\le\omega(K(k))+1`) may be used per cell for a tighter threshold.

Using this exact per-cell bound and solving `L(q)\ge` it (with
`L(q)=n_0(j,r)-1+kq` an explicit, strictly increasing affine function of
`q`, giving `q_{\mathrm{thresh}}(j,r,k)=\dfrac{13\cdot\mathrm{bound}+j}
{s_0(j,r)+13k}`) for each of the `132\times11=1452` cell/`k` combinations
(skipping the `r=1` cells whenever `\gcd(k+1,j)=1`, already free by Lemma
5) finds that only **29** `(j,r,k,q)` combinations have any admissible
prime below threshold:

`(2,4,1,17)`; `(2,5,2,31)`; `(2,7,1,59)`; `(3,4,1,17)`; `(3,4,1,43)`;
`(3,6,1,19)`; `(4,1,1,53)`; `(4,4,4,17)`; `(4,10,2,23)`; `(5,6,2,19)`;
`(5,11,1,37)`; `(6,4,1,17)`; `(6,4,3,17)`; `(6,6,4,19)`; `(6,8,1,47)`;
`(7,4,4,17)`; `(7,5,1,31)`; `(7,10,1,23)`; `(8,2,1,41)`; `(8,4,1,17)`;
`(9,3,2,29)`; `(9,6,1,19)`; `(9,6,3,19)`; `(10,4,1,17)`; `(10,9,1,61)`;
`(11,6,1,19)`; `(12,3,1,29)`; `(12,4,2,17)`; `(12,6,1,19)`.

**19 of these 29 are moot: `q\in\{17,19,23,47\}=\mathrm{Bad}(13)`.** By §7,
each such `q` is already established to deviate from the closed form at a
small, explicit index and is excluded from the theorem's scope by
definition — so any `(j,r,k,q)` instance with `q\in\mathrm{Bad}(13)`
concerns a `q` outside the theorem's stated scope and does not need to be
resolved for the theorem to hold. (Explicit tally, by direct scan of the
29-item list above: `q=17` accounts for 9 entries —
`(2,4,1),(3,4,1),(4,4,4),(6,4,1),(6,4,3),(7,4,4),(8,4,1),(10,4,1),(12,4,2)`;
`q=19` accounts for 7 entries —
`(3,6,1),(5,6,2),(6,6,4),(9,6,1),(9,6,3),(11,6,1),(12,6,1)`; `q=23`
accounts for 2 — `(4,10,2),(7,10,1)`; `q=47` accounts for 1 — `(6,8,1)`.
Total `9+7+2+1=19`, matching.)

**The remaining 10 non-moot instances**, all with
`q\in\{29,31,37,41,43,53,59,61\}` (none in `\mathrm{Bad}(13)`), resolved by
explicit witness search over the full range `i=1,\dots,n`:

- `(2,5,2,31)`: `n_0=8,n=70,K=42,N=1302=31\cdot42`. `a_7=13\cdot37=481`,
  `\gcd(1302,481)=1` — **witness `i=7`**.
- `(2,7,1,59)`: `n_0=19,n=78,K=30,N=1770=59\cdot30`. `a_3=13\cdot61=793`,
  `\gcd(1770,793)=1` — **witness `i=3`**.
- `(3,4,1,43)`: `n_0=14,n=57,K=30,N=1290=43\cdot30`. `a_5=13\cdot47=611`,
  `\gcd(1290,611)=1` — **witness `i=5`**.
- `(4,1,1,53)`: `n_0=17,n=70,K=30,N=1590=53\cdot30`. `a_7=13\cdot59=767`,
  `\gcd(1590,767)=1` — **witness `i=7`**.
- `(5,11,1,37)`: `n_0=12,n=49,K=30,N=1110=37\cdot30`. `a_5=13\cdot41=533`,
  `\gcd(1110,533)=1` — **witness `i=5`**.
- `(7,5,1,31)`: `n_0=10,n=41,K=30,N=930=31\cdot30`. `a_7=13\cdot37=481`,
  `\gcd(930,481)=1` — **witness `i=7`**.
- `(8,2,1,41)`: `n_0=13,n=54,K=30,N=1230=41\cdot30`. `a_3=13\cdot43=559`,
  `\gcd(1230,559)=1` — **witness `i=3`**.
- `(9,3,2,29)`: `n_0=7,n=65,K=42,N=1218=29\cdot42`. `a_3=13\cdot31=403`,
  `\gcd(1218,403)=1` — **witness `i=3`**.
- `(10,9,1,61)`: `n_0=19,n=80,K=30,N=1830=61\cdot30`. `a_7=13\cdot67=871`,
  `\gcd(1830,871)=1` — **witness `i=7`**.
- `(12,3,1,29)`: `n_0=9,n=38,K=30,N=870=29\cdot30`. `a_3=13\cdot31=403`,
  `\gcd(870,403)=1` — **witness `i=3`**.

(Every one of these 10 was checked by exact integer computation: `N=qK`
was verified to equal `a_n+j` exactly for the stated `n`, and `\gcd(N,a_i)`
computed exactly, confirming `\gcd=1` in each case.)

**Conclusion of §8.** For every prime `q>13`, `q\notin\mathrm{Bad}(13)`,
every band `j\in\{2,\dots,12\}`, and every `k\ge1` (with, for `r=1`, the
additional case `\gcd(k+1,j)=1` handled unconditionally by Lemma 5): a
Case-(b) witness for the illegality of `a_n+j` (`n=n_0(j,r)+kq`) exists —
either via Lemma 5 (`r=1`, `\gcd(k+1,j)=1`), via Lemma 3 directly (`k\ge12`,
or `k\le11` with `q\ge q_{\mathrm{thresh}}(j,r,k)`), or via one of the 10
explicit witnesses above. This closes Case (b), `k\ge1`, completely, for
every `q` in the theorem's scope.

### 9. Assembly

Combining §1 (base case, `a_n+1` illegal, `a_n+13` legal), §2 (Case (a)
illegality), §4 (`k=0` closure for the `r=1` column, free by Lemma 5), §5–6
(`k=0` closure for `r=2,\dots,12`, `q\notin\mathrm{Bad}(13)`, with the
`q=19` moot-cell duplicate explicitly resolved), §7 (permanence of the 4
genuine exceptions, excluding them from scope), and §8 (`k\ge1` closure for
every admissible `q`, every cell): for every prime `q>13`,
`q\notin\{17,19,23,47\}`, and every `n\ge1` with `H(n)` holding,
`a_n+1,\dots,a_n+12` are all illegal and `a_n+13` is legal, so minimality
of the greedy rule forces `a_{n+1}=a_n+13=13(q+n)=13(q+(n+1)-1)`,
establishing `H(n+1)`.

By strong induction, `H(n)` holds for every `n\ge1`:
$$a_n=13(q+n-1)\quad\text{for all }n\ge1,$$
i.e. literal `T=1,L=13` periodicity from `n=1`, for every prime `q>13`,
`q\notin\{17,19,23,47\}`. **This proves the theorem.** `\blacksquare`

## Promotable lemmas

**`p=13` `K_0`-boundedness table (132 cells).** The explicit table in §3
above (`s_0(j,r),K_0(j,r)` for all `j\in\{2,\dots,12\},r\in\{1,\dots,12\}`),
derived by direct instantiation of the certified Generalized
`K_0`-Boundedness Lemma at `p=13`. Reusable by any future approach needing
the `a_1=13q`-type family's exact constants.

**`s^*=5` threshold at `p=13` and its induction (§8).** The inequality
`(s+1)!\ge25+\tfrac{13}{17}\cdot2^{s+1}(s+2)` for `s\ge5`, proved by an
explicit base case and induction (reusing the sub-fact `s^2+2s-2\ge0` for
`s\ge1` from the certified Primorial Floor Bound's own corollary). This is
the `p=13`-specific analogue of `a1-5q`'s, `a1-7q`'s, and `a1-11q`'s `s^*=5`
thresholds — `s^*=5` again matches `p=3,5,7,11`, a fifth data point
(constants `K_0\le25,q\ge17`), still not claimed as a general pattern for
all `p`.

**`\mathrm{Bad}(13)=\{17,19,23,47\}`, proved genuine (§7), plus the general
moot-duplicate-cell resolution technique (§6).** The exact mechanism-level
exclusion proof (finite witness window exhausted with no coprime candidate,
at `n_0\in\{2,4\}` respectively) for all four exceptions, fully explicit.
All four exceptions occur at diagonal (`j=r`, minimal `K_0=14`) bands —
`(j,r)=(4,4),(6,6),(10,10),(8,8)` for `q=17,19,23,47` respectively —
consistent with the certified Diagonal Characterization Lemma (fifth
consecutive `p`-instantiation, `p=3,5,7,11,13`, in which every genuine
exception lands exactly on the diagonal band). Separately, §6 gives a
reusable template for resolving a "duplicate below-threshold `EXC` cell"
sharing residue `r` with an already-genuine diagonal exception: show the
duplicate band's premise `H(n_0)` is never realized by the true sequence
because a strictly earlier genuine deviation already occurred, then confirm
this is the *only* such duplicate in the full candidate list (no other
prime appears twice among the `EXC` entries). This template generalizes
beyond `p=13` to any future `p`-instantiation that produces a multi-band
`EXC` prime.
