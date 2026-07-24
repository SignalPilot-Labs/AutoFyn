## Status
solved (round 30: the `a_1=19q` subfamily theorem is fully proved — literal
`T=1,L=19` periodicity from `n=1` for every prime `q>19`,
`q\notin\mathrm{Bad}(19)=\{23,29,31,37,43,53,73\}`, by instantiating the
certified `p`-uniform machinery from `a1-pq-subfamily-theorem` at `p=19`,
building the explicit 306-cell `(j,r)` table, using the certified Universal
Look-Back Witness Identity to close the `r=1` column's `k=0` layer
unconditionally, closing the remaining 289 cells' `k=0` layer and all 306
cells' `k\ge1` layer with the certified Legendre-Sieve/Primorial-Floor
toolkit, and proving all 7 genuine exceptions rigorously via a single
uniform diagonal parity/mod-5 argument (rather than 7 separate ad hoc
computations) — the seventh consecutive successful instantiation of the
certified template (`p=3,5,7,11,13,17` all previously APPROVEd this way).
See "Full proof" below.)

## Approaches tried
- (round 30, new, near-certain per outline-reviewer) Instantiate the
  certified `p`-uniform machinery at `p=19`; this round's math-explorer had
  already found `\mathrm{Bad}(19)=\{23,29,31,37,43,53,73\}` by greedy
  resimulation (to `q<20000`) and diagnosed a parity/mod-5 mechanism, but
  had not built the full table/threshold/witness work or proved the
  mechanism rigorously.
- (round 30, this build) Fully instantiated the certified `p`-uniform
  machinery at `p=19`, exactly mirroring `a1-17q`'s/`a1-13q`'s/`a1-11q`'s
  completed builds: built the full 306-cell `(j,r)` table (`j\in\{2,\dots,
  18\}`, `r\in\{1,\dots,18\}`); used the certified Universal Look-Back
  Witness Identity's `r=1` corollary to close the entire `k=0` layer of the
  17 `r=1` cells unconditionally, with no threshold; computed the `k=0`
  sufficient-window thresholds `Q_1(j,r)` for the remaining 289 cells,
  resolved all 260 below-threshold `(j,r,q)` candidates by explicit witness
  search (253 resolve, exactly 7 genuine exceptions, all diagonal, matching
  `\mathrm{Bad}(19)` exactly, with no moot/duplicate-band pathology: every
  non-diagonal below-threshold band for each of the 7 exceptional primes
  resolves with an honest witness); derived a fresh `s^*=5` threshold
  (`p=19` constants: `K_0\le37`, `q_{\min}=23`) for the generic `k\ge1`
  closure, showed `k\ge9` is handled uniformly (an improvement over
  `p=17`'s `k\ge11`, due to the larger `q_{\min}=23`), reduced the residual
  band `k\in\{1,\dots,8\}` to 25 below-threshold `(j,r,k,q)` quadruples (21
  moot, `q\in\mathrm{Bad}(19)`; 4 non-moot, all resolved by explicit
  witnesses). Additionally proved a new **Diagonal Window-Parity/Mod-5
  Lemma** giving a single, uniform, fully general elementary mechanism
  (rather than 7 ad hoc computations) explaining exactly why each of the 7
  diagonal exceptions is genuine: on the diagonal `K_0=p+1=20=2^2\cdot5`,
  and the candidate `N=20q` is legal iff every integer in the window
  `\{q+1,\dots,q+n_0-1\}` shares a factor with `20`; since `q` is always
  odd, `q+1` is always even, so window length `1` (`n_0=2`) is *automatic*
  and needs no further check (covers `q=23,29,31,37`); longer windows need
  the extra elements checked directly for divisibility by `2` or `5`
  (`q=43,53`: `q+2\equiv0\pmod5`; `q=73`: `\{74,75,76\}`, `75=3\cdot5^2`).
  **Result: the theorem is now completely proved.** Independently
  cross-validated with a from-scratch literal greedy simulation (primes
  `q\in(19,6000)`, correct legality semantics requiring
  `\gcd(\text{candidate},a_i)>1` for *every* `i\le n`): exactly reproduces
  `\mathrm{Bad}(19)` and every exact deviation index/value.
- (light housekeeping, this round) Updated `results/imo-2026-06/current.md`'s
  `## Approaches tried` and `## Current best` sections (stale since round
  20) to record the round 22–29 subfamily theorems
  (`a1-3q`,`a1-3q^2`,`a1-3q^3`,`a1-3aq`(`a=1,\dots,5`),`a1-5q`,`a1-7q`,
  `a1-11q`,`a1-13q`,`a1-17q`) and this round's `a1-19q`, per the
  outline-reviewer's instruction to fold this into the `a1-19q` builder's
  task rather than spinning up a separate housekeeping-only slug. Did not
  touch `current.md`'s reviewer-owned `## Status`/`## Full proof` sections.

## Current best

### Target (now proved — see Full proof)
For every prime `q>19` with `q\notin\{23,29,31,37,43,53,73\}`, and
`a_1=19q`: `a_n=19(q+n-1)` for every `n\ge1` — literal `T=1,L=19`
periodicity from `n=1`.

## Full proof

### 0. Setup and imported machinery

Fix a prime `q>19`, `q\notin\{23,29,31,37,43,53,73\}`, and `a_1=19q`.
Strong-induction hypothesis at step `n`, `H(n)`: `a_i=19(q+i-1)` for
`i=1,\dots,n`. In particular `19\mid a_i` for every such `i`, and — since
`19,q` are distinct primes — `P(a_1)=\{19,q\}`.

The greedy rule: `a_{n+1}` is the least integer `>a_n` such that
`\gcd(a_{n+1},a_i)>1` for *every* `i=1,\dots,n` (shares a nontrivial common
factor with **each** prior term — a candidate is illegal, i.e. rejected,
if there exists even one `i` with `\gcd=1`; such an `i` is called a
**witness** to the candidate's illegality).

We use, without re-derivation, the following results, each certified in
this workspace for a general odd prime `p` (so their `p=19` instantiations
below require no new proof, only substitution):

- **Lemma 1 (Generalized gcd-difference Witness Lemma,
  `lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md`).** For
  `N:=a_n+j`, `j\in\{1,\dots,18\}`, under `H(n)`: `\gcd(N,a_n)=\gcd(N,j)`.
- **Lemma 2 (Generalized `K_0`-Boundedness, `p=19`,
  `lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md`).** For
  `j\in\{2,\dots,18\}` and prime `q>19` with `q\equiv r\pmod{19}`
  (`r\in\{1,\dots,18\}`), the first index `n_0(j,r;q)` with `q\mid(a_{n_0}+j)`
  satisfies `K_0(j,r):=(a_{n_0}+j)/q=19+s_0(j,r)`, where
  `s_0(j,r)\in\{1,\dots,18\}` is the unique solution of `s_0\cdot r\equiv
  j\pmod{19}`, and `n_0(j,r;q)=1+(s_0(j,r)q-j)/19`.
- **Lemma 3 (Legendre Sieve Gap Bound, `lemmas/legendre-sieve-gap-bound.md`).**
  For integer `M\ge2` with `\rho:=\omega(M)`, any window of `L\ge2^\rho(\rho+1)`
  consecutive integers contains one coprime to `M`.
- **Lemma 4 (Primorial Floor Bound, `lemmas/primorial-floor-bound.md`).** If
  `\omega(M)=\rho` then `M\ge(\rho+1)!`.
- **Lemma 5 (Universal Look-Back Witness Identity and its `r=1` Corollary,
  `lemmas/universal-look-back-witness-identity.md`).** Under `H(n)`, for
  `j\in\{1,\dots,18\}`, `N:=a_n+j`, and any `1\le i\le n`:
  `\gcd(N,a_i)=\gcd(19(n-i)+j,\,q+i-1)`. Moreover, when `q\equiv1\pmod{19}`,
  writing `q=19t+1` (`t\ge2`), the `k`-th Case-(b) risk index of band `j` is
  `n=1+jt+kq` and, at `i=n` (look-back distance `0`),
  `\gcd(N,a_n)=\gcd(k+1,j)` — in particular this equals `1` unconditionally
  whenever `\gcd(k+1,j)=1`, for every `p`, every band, every such `q`, with
  no threshold.
- **Lemma 6 (Diagonal Characterization,
  `lemmas/diagonal-characterization-and-first-risk-theorem.md`).** For
  `j\in\{2,\dots,18\}`, `r\in\{1,\dots,18\}`: `s_0(j,r)=1` iff `j=r`.

### 1. Base case and the `j=1,19` bands

`n=1`: `a_1=19q=19(q+1-1)`, by definition.

Assume `H(n)`. We show `a_n+1,\dots,a_n+18` are all illegal and `a_n+19` is
legal, forcing `a_{n+1}=a_n+19=19(q+n)`, i.e. `H(n+1)`.

**`a_n+1` illegal.** `\gcd(a_n+1,a_n)=1` (consecutive integers), witnessed
by `i=n`.

**`a_n+19` legal.** `a_n+19=19(q+n-1)+19=19(q+n)`. For every `i\le n`,
`\gcd(a_n+19,a_i)\ge\gcd(19(q+n),19(q+i-1))\ge19>1` (both multiples of `19`,
by `H(n)`).

### 2. Illegality of `a_n+j`, `j\in\{2,\dots,18\}`: the Case (a)/(b) split

Fix `j\in\{2,\dots,18\}` and `N:=a_n+j=19(q+n-1)+j`. Since `1\le j\le18`,
`N\equiv j\not\equiv0\pmod{19}`, so `19\nmid N`.

**Case (a): `q\nmid N`.** Any common divisor of `N` and `a_1=19q` divides
`19q`; since `19\nmid N` and `q\nmid N`, the only such divisor is `1`:
`\gcd(N,a_1)=1` — illegal, witnessed by `i=1`.

**Case (b): `q\mid N`.** Write `N=qK`, `K:=N/q\in\mathbb Z_{>0}`. For
`i=1`: `\gcd(N,a_1)=\gcd(N,19q)\ge q>1`, never a witness here. For
`2\le i\le n`: since `\gcd(N,19)=1`, writing `m:=q+i-1`,
`\gcd(N,a_i)=\gcd(N,m)=\gcd(qK,m)`. So Case-(b) illegality of `a_n+j`
reduces to finding, in the window `m=q+1,\dots,q+n-1` (length `L:=n-1`,
`i=2,\dots,n`), an integer coprime to `N=qK`.

By Lemma 2, the Case-(b) indices for band `j`, residue `r:=q\bmod{19}`, are
exactly `n=n_0(j,r)+kq`, `k=0,1,2,\dots`, with `K(k):=K_0(j,r)+19k`.

### 3. The 306-cell table (`p=19`)

Solving `s_0\cdot r\equiv j\pmod{19}` for each `(j,r)`, `j\in\{2,\dots,18\}`,
`r\in\{1,\dots,18\}` (`17\times18=306` cells), via `pow(r,-1,19)`, and
setting `K_0(j,r)=19+s_0(j,r)`:

| `j\backslash r` | `1` | `2` | `3` | `4` | `5` | `6` | `7` | `8` | `9` | `10` | `11` | `12` | `13` | `14` | `15` | `16` | `17` | `18` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `2` | `2,21` | `1,20` | `7,26` | `10,29` | `8,27` | `13,32` | `3,22` | `5,24` | `15,34` | `4,23` | `14,33` | `16,35` | `6,25` | `11,30` | `9,28` | `12,31` | `18,37` | `17,36` |
| `3` | `3,22` | `11,30` | `1,20` | `15,34` | `12,31` | `10,29` | `14,33` | `17,36` | `13,32` | `6,25` | `2,21` | `5,24` | `9,28` | `7,26` | `4,23` | `18,37` | `8,27` | `16,35` |
| `4` | `4,23` | `2,21` | `14,33` | `1,20` | `16,35` | `7,26` | `6,25` | `10,29` | `11,30` | `8,27` | `9,28` | `13,32` | `12,31` | `3,22` | `18,37` | `5,24` | `17,36` | `15,34` |
| `5` | `5,24` | `12,31` | `8,27` | `6,25` | `1,20` | `4,23` | `17,36` | `3,22` | `9,28` | `10,29` | `16,35` | `2,21` | `15,34` | `18,37` | `13,32` | `11,30` | `7,26` | `14,33` |
| `6` | `6,25` | `3,22` | `2,21` | `11,30` | `5,24` | `1,20` | `9,28` | `15,34` | `7,26` | `12,31` | `4,23` | `10,29` | `18,37` | `14,33` | `8,27` | `17,36` | `16,35` | `13,32` |
| `7` | `7,26` | `13,32` | `15,34` | `16,35` | `9,28` | `17,36` | `1,20` | `8,27` | `5,24` | `14,33` | `11,30` | `18,37` | `2,21` | `10,29` | `3,22` | `4,23` | `6,25` | `12,31` |
| `8` | `8,27` | `4,23` | `9,28` | `2,21` | `13,32` | `14,33` | `12,31` | `1,20` | `3,22` | `16,35` | `18,37` | `7,26` | `5,24` | `6,25` | `17,36` | `10,29` | `15,34` | `11,30` |
| `9` | `9,28` | `14,33` | `3,22` | `7,26` | `17,36` | `11,30` | `4,23` | `13,32` | `1,20` | `18,37` | `6,25` | `15,34` | `8,27` | `2,21` | `12,31` | `16,35` | `5,24` | `10,29` |
| `10` | `10,29` | `5,24` | `16,35` | `12,31` | `2,21` | `8,27` | `15,34` | `6,25` | `18,37` | `1,20` | `13,32` | `4,23` | `11,30` | `17,36` | `7,26` | `3,22` | `14,33` | `9,28` |
| `11` | `11,30` | `15,34` | `10,29` | `17,36` | `6,25` | `5,24` | `7,26` | `18,37` | `16,35` | `3,22` | `1,20` | `12,31` | `14,33` | `13,32` | `2,21` | `9,28` | `4,23` | `8,27` |
| `12` | `12,31` | `6,25` | `4,23` | `3,22` | `10,29` | `2,21` | `18,37` | `11,30` | `14,33` | `5,24` | `8,27` | `1,20` | `17,36` | `9,28` | `16,35` | `15,34` | `13,32` | `7,26` |
| `13` | `13,32` | `16,35` | `17,36` | `8,27` | `14,33` | `18,37` | `10,29` | `4,23` | `12,31` | `7,26` | `15,34` | `9,28` | `1,20` | `5,24` | `11,30` | `2,21` | `3,22` | `6,25` |
| `14` | `14,33` | `7,26` | `11,30` | `13,32` | `18,37` | `15,34` | `2,21` | `16,35` | `10,29` | `9,28` | `3,22` | `17,36` | `4,23` | `1,20` | `6,25` | `8,27` | `12,31` | `5,24` |
| `15` | `15,34` | `17,36` | `5,24` | `18,37` | `3,22` | `12,31` | `13,32` | `9,28` | `8,27` | `11,30` | `10,29` | `6,25` | `7,26` | `16,35` | `1,20` | `14,33` | `2,21` | `4,23` |
| `16` | `16,35` | `8,27` | `18,37` | `4,23` | `7,26` | `9,28` | `5,24` | `2,21` | `6,25` | `13,32` | `17,36` | `14,33` | `10,29` | `12,31` | `15,34` | `1,20` | `11,30` | `3,22` |
| `17` | `17,36` | `18,37` | `12,31` | `9,28` | `11,30` | `6,25` | `16,35` | `14,33` | `4,23` | `15,34` | `5,24` | `3,22` | `13,32` | `8,27` | `10,29` | `7,26` | `1,20` | `2,21` |
| `18` | `18,37` | `9,28` | `6,25` | `14,33` | `15,34` | `3,22` | `8,27` | `7,26` | `2,21` | `17,36` | `12,31` | `11,30` | `16,35` | `4,23` | `5,24` | `13,32` | `10,29` | `1,20` |

(Each cell entry is `s_0(j,r),K_0(j,r)`. Every diagonal cell `j=r` gives
`s_0=1,K_0=20` exactly, matching Lemma 6. Computed and independently
cross-checked this round via two independent scripts and by direct
symmetry checks — exact match.)

Note `K_0(j,r)\in\{20,\dots,37\}` throughout (max `37`, at `s_0=18`) — this
bound (`K_0\le37`) is used in §7.

### 4. Closing `k=0` for the `r=1` column: free by Lemma 5

For `q\equiv1\pmod{19}` (the 17 cells `j\in\{2,\dots,18\},r=1`), Lemma 5's
Corollary gives, at `k=0`, `\gcd(N,a_n)=\gcd(1,j)=1` unconditionally — the
index `i=n_0(j,1)` itself is always a witness, with no threshold and no
per-`q` computation. This closes the entire `k=0` layer of the `r=1` column
for every admissible prime `q\equiv1\pmod{19}`, for every band
`j\in\{2,\dots,18\}`. (More generally, by the same Corollary, every `k\ge0`
with `\gcd(k+1,j)=1` is likewise free for `r=1` — used again in §7.)

### 5. Closing `k=0` for the remaining 289 cells (`r=2,\dots,18`)

**Sufficient-window criterion.** If `n_0(j,r)-1\ge K_0(j,r)`, the window
`m=q+1,\dots,q+n_0-1` (length `n_0-1`, all `<2q` since `n_0\le q`, hence
automatically coprime to `q`) contains a full residue system mod
`K_0(j,r)`, hence an integer coprime to `K_0(j,r)` — a witness.
Substituting the explicit affine formula for `n_0`, this holds for every
prime `q\equiv r\pmod{19}` with
`q\ge Q_1(j,r):=\dfrac{19(K_0(j,r)+1)+j}{s_0(j,r)}`.

Computing `Q_1` for all 289 cells (`r=2,\dots,18`) and, for each, listing
the primes `q\equiv r\pmod{19}`, `q>19`, with `q<Q_1(j,r)` (the
below-threshold `k=0` candidates), gives exactly **260** triples `(j,r,q)`
(computed via a dedicated script; full list below with resolution).

**Direct resolution of every below-threshold `k=0` candidate.** For each
triple, `n_0=1+(s_0q-j)/19`, `N=a_{n_0}+j=qK_0`; we search `i=1,\dots,n_0`
for `\gcd(N,a_i)=1` with `a_i=19(q+i-1)`. Result (`i` = witness index,
`EXC` = no witness exists, a genuine exception):

`(2,2,59)`:`n_0=4,N=1180,i=3`; `(2,2,97)`:`n_0=6,N=1940,i=3`;
`(2,2,173)`:`n_0=10,N=3460,i=5`; `(2,2,211)`:`n_0=12,N=4220,i=3`;
`(2,3,41)`:`n_0=16,N=1066,i=3`; `(2,4,23)`:`n_0=13,N=667,i=2`;
`(2,5,43)`:`n_0=19,N=1161,i=2`; `(2,7,83)`:`n_0=14,N=1826,i=3`;
`(2,10,29)`:`n_0=7,N=667,i=2`; `(2,10,67)`:`n_0=15,N=1541,i=2`;
`(2,12,31)`:`n_0=27,N=1085,i=2`; `(2,15,53)`:`n_0=26,N=1484,i=3`;
`(2,18,37)`:`n_0=34,N=1332,i=5`; `(3,3,41)`:`n_0=3,N=820,i=3`;
`(3,3,79)`:`n_0=5,N=1580,i=3`; `(3,3,193)`:`n_0=11,N=3860,i=5`;
`(3,3,269)`:`n_0=15,N=5380,i=3`; `(3,3,307)`:`n_0=17,N=6140,i=3`;
`(3,3,383)`:`n_0=21,N=7660,i=5`; `(3,4,23)`:`n_0=19,N=782,i=3`;
`(3,5,43)`:`n_0=28,N=1333,i=2`; `(3,9,47)`:`n_0=33,N=1504,i=3`;
`(3,10,29)`:`n_0=10,N=725,i=3`; `(3,10,67)`:`n_0=22,N=1675,i=2`;
`(3,11,163)`:`n_0=18,N=3423,i=2`; `(3,12,31)`:`n_0=9,N=744,i=5`;
`(3,14,71)`:`n_0=27,N=1846,i=3`; `(3,15,53)`:`n_0=12,N=1219,i=2`;
`(3,18,37)`:`n_0=32,N=1295,i=2`; `(4,2,59)`:`n_0=7,N=1239,i=3`;
`(4,2,97)`:`n_0=11,N=2037,i=4`; `(4,2,173)`:`n_0=19,N=3633,i=4`;
`(4,3,41)`:`n_0=31,N=1353,i=3`; `(4,4,23)`:`n_0=2,N=460`,**EXC**;
`(4,4,61)`:`n_0=4,N=1220,i=3`; `(4,4,137)`:`n_0=8,N=2740,i=3`;
`(4,4,251)`:`n_0=14,N=5020,i=3`; `(4,9,47)`:`n_0=28,N=1410,i=3`;
`(4,10,29)`:`n_0=13,N=783,i=3`; `(4,12,31)`:`n_0=22,N=992,i=3`;
`(4,14,71)`:`n_0=12,N=1562,i=3`; `(4,14,109)`:`n_0=18,N=2398,i=3`;
`(4,16,73)`:`n_0=20,N=1752,i=5`; `(4,18,37)`:`n_0=30,N=1258,i=3`;
`(5,3,41)`:`n_0=18,N=1107,i=3`; `(5,4,23)`:`n_0=8,N=575,i=2`;
`(5,4,61)`:`n_0=20,N=1525,i=2`; `(5,5,43)`:`n_0=3,N=860`,**EXC**;
`(5,5,157)`:`n_0=9,N=3140,i=3`; `(5,5,233)`:`n_0=13,N=4660,i=5`;
`(5,5,271)`:`n_0=15,N=5420,i=3`; `(5,5,347)`:`n_0=19,N=6940,i=3`;
`(5,6,101)`:`n_0=22,N=2323,i=2`; `(5,8,103)`:`n_0=17,N=2266,i=3`;
`(5,9,47)`:`n_0=23,N=1316,i=5`; `(5,10,29)`:`n_0=16,N=841,i=2`;
`(5,12,31)`:`n_0=4,N=651,i=2`; `(5,12,107)`:`n_0=12,N=2247,i=3`;
`(5,18,37)`:`n_0=28,N=1221,i=2`; `(6,2,59)`:`n_0=10,N=1298,i=3`;
`(6,2,97)`:`n_0=16,N=2134,i=5`; `(6,3,41)`:`n_0=5,N=861,i=3`;
`(6,3,79)`:`n_0=9,N=1659,i=2`; `(6,3,193)`:`n_0=21,N=4053,i=2`;
`(6,4,23)`:`n_0=14,N=690,i=7`; `(6,5,43)`:`n_0=12,N=1032,i=5`;
`(6,6,101)`:`n_0=6,N=2020,i=3`; `(6,6,139)`:`n_0=8,N=2780,i=3`;
`(6,6,367)`:`n_0=20,N=7340,i=3`; `(6,9,47)`:`n_0=18,N=1222,i=3`;
`(6,10,29)`:`n_0=19,N=899,i=2`; `(6,12,31)`:`n_0=17,N=899,i=2`;
`(6,15,53)`:`n_0=23,N=1431,i=3`; `(6,18,37)`:`n_0=26,N=1184,i=3`;
`(7,3,41)`:`n_0=33,N=1394,i=3`; `(7,4,23)`:`n_0=20,N=805,i=2`;
`(7,5,43)`:`n_0=21,N=1204,i=3`; `(7,7,83)`:`n_0=5,N=1660,i=5`;
`(7,7,197)`:`n_0=11,N=3940,i=3`; `(7,7,311)`:`n_0=17,N=6220,i=3`;
`(7,7,349)`:`n_0=19,N=6980,i=3`; `(7,9,47)`:`n_0=13,N=1128,i=3`;
`(7,10,29)`:`n_0=22,N=957,i=3`; `(7,12,31)`:`n_0=30,N=1147,i=2`;
`(7,13,89)`:`n_0=10,N=1869,i=4`; `(7,13,127)`:`n_0=14,N=2667,i=2`;
`(7,15,53)`:`n_0=9,N=1166,i=5`; `(7,16,73)`:`n_0=16,N=1679,i=2`;
`(7,18,37)`:`n_0=24,N=1147,i=2`; `(8,2,59)`:`n_0=13,N=1357,i=2`;
`(8,2,97)`:`n_0=21,N=2231,i=2`; `(8,3,41)`:`n_0=20,N=1148,i=3`;
`(8,4,23)`:`n_0=3,N=483,i=3`; `(8,4,61)`:`n_0=7,N=1281,i=2`;
`(8,4,137)`:`n_0=15,N=2877,i=3`; `(8,5,43)`:`n_0=30,N=1376,i=3`;
`(8,8,103)`:`n_0=6,N=2060,i=5`; `(8,8,179)`:`n_0=10,N=3580,i=3`;
`(8,8,293)`:`n_0=16,N=5860,i=5`; `(8,8,331)`:`n_0=18,N=6620,i=3`;
`(8,9,47)`:`n_0=8,N=1034,i=3`; `(8,10,29)`:`n_0=25,N=1015,i=3`;
`(8,12,31)`:`n_0=12,N=806,i=3`; `(8,13,89)`:`n_0=24,N=2136,i=3`;
`(8,14,71)`:`n_0=23,N=1775,i=2`; `(8,18,37)`:`n_0=22,N=1110,i=5`;
`(9,3,41)`:`n_0=7,N=902,i=3`; `(9,3,79)`:`n_0=13,N=1738,i=3`;
`(9,4,23)`:`n_0=9,N=598,i=3`; `(9,4,61)`:`n_0=23,N=1586,i=3`;
`(9,7,83)`:`n_0=18,N=1909,i=2`; `(9,9,47)`:`n_0=3,N=940,i=3`;
`(9,9,199)`:`n_0=11,N=3980,i=3`; `(9,9,313)`:`n_0=17,N=6260,i=5`;
`(9,9,389)`:`n_0=21,N=7780,i=3`; `(9,10,29)`:`n_0=28,N=1073,i=2`;
`(9,12,31)`:`n_0=25,N=1054,i=3`; `(9,14,71)`:`n_0=8,N=1491,i=3`;
`(9,14,109)`:`n_0=12,N=2289,i=2`; `(9,18,37)`:`n_0=20,N=1073,i=2`;
`(10,2,59)`:`n_0=16,N=1416,i=3`; `(10,3,41)`:`n_0=35,N=1435,i=3`;
`(10,4,23)`:`n_0=15,N=713,i=2`; `(10,5,43)`:`n_0=5,N=903,i=2`;
`(10,5,157)`:`n_0=17,N=3297,i=2`; `(10,10,29)`:`n_0=2,N=580`,**EXC**;
`(10,10,67)`:`n_0=4,N=1340,i=3`; `(10,10,181)`:`n_0=10,N=3620,i=3`;
`(10,10,257)`:`n_0=14,N=5140,i=3`; `(10,12,31)`:`n_0=7,N=713,i=2`;
`(10,12,107)`:`n_0=23,N=2461,i=2`; `(10,15,53)`:`n_0=20,N=1378,i=3`;
`(10,16,73)`:`n_0=12,N=1606,i=3`; `(10,18,37)`:`n_0=18,N=1036,i=3`;
`(11,3,41)`:`n_0=22,N=1189,i=2`; `(11,4,23)`:`n_0=21,N=828,i=3`;
`(11,5,43)`:`n_0=14,N=1075,i=2`; `(11,10,29)`:`n_0=5,N=638,i=3`;
`(11,10,67)`:`n_0=11,N=1474,i=3`; `(11,11,163)`:`n_0=9,N=3260,i=5`;
`(11,11,239)`:`n_0=13,N=4780,i=3`; `(11,11,277)`:`n_0=15,N=5540,i=3`;
`(11,11,353)`:`n_0=19,N=7060,i=5`; `(11,12,31)`:`n_0=20,N=961,i=2`;
`(11,15,53)`:`n_0=6,N=1113,i=3`; `(11,15,167)`:`n_0=18,N=3507,i=3`;
`(11,18,37)`:`n_0=16,N=999,i=2`; `(12,2,59)`:`n_0=19,N=1475,i=3`;
`(12,3,41)`:`n_0=9,N=943,i=2`; `(12,3,79)`:`n_0=17,N=1817,i=2`;
`(12,4,23)`:`n_0=4,N=506,i=3`; `(12,4,61)`:`n_0=10,N=1342,i=3`;
`(12,4,137)`:`n_0=22,N=3014,i=3`; `(12,5,43)`:`n_0=23,N=1247,i=2`;
`(12,6,101)`:`n_0=11,N=2121,i=3`; `(12,6,139)`:`n_0=15,N=2919,i=4`;
`(12,10,29)`:`n_0=8,N=696,i=3`; `(12,10,67)`:`n_0=18,N=1608,i=5`;
`(12,12,31)`:`n_0=2,N=620`,**EXC**; `(12,12,107)`:`n_0=6,N=2140,i=3`;
`(12,12,373)`:`n_0=20,N=7460,i=5`; `(12,18,37)`:`n_0=14,N=962,i=5`;
`(13,3,41)`:`n_0=37,N=1476,i=3`; `(13,4,23)`:`n_0=10,N=621,i=3`;
`(13,4,61)`:`n_0=26,N=1647,i=2`; `(13,5,43)`:`n_0=32,N=1419,i=4`;
`(13,8,103)`:`n_0=22,N=2369,i=2`; `(13,9,47)`:`n_0=30,N=1457,i=2`;
`(13,10,29)`:`n_0=11,N=754,i=3`; `(13,10,67)`:`n_0=25,N=1742,i=3`;
`(13,12,31)`:`n_0=15,N=868,i=3`; `(13,13,89)`:`n_0=5,N=1780,i=3`;
`(13,13,127)`:`n_0=7,N=2540,i=3`; `(13,13,241)`:`n_0=13,N=4820,i=3`;
`(13,13,317)`:`n_0=17,N=6340,i=3`; `(13,14,71)`:`n_0=19,N=1704,i=3`;
`(13,15,53)`:`n_0=31,N=1590,i=7`; `(13,16,73)`:`n_0=8,N=1533,i=2`;
`(13,16,149)`:`n_0=16,N=3129,i=3`; `(13,17,131)`:`n_0=21,N=2882,i=3`;
`(13,18,37)`:`n_0=12,N=925,i=2`; `(14,2,59)`:`n_0=22,N=1534,i=3`;
`(14,3,41)`:`n_0=24,N=1230,i=3`; `(14,4,23)`:`n_0=16,N=736,i=3`;
`(14,7,83)`:`n_0=9,N=1743,i=3`; `(14,7,197)`:`n_0=21,N=4137,i=3`;
`(14,9,47)`:`n_0=25,N=1363,i=2`; `(14,10,29)`:`n_0=14,N=812,i=3`;
`(14,12,31)`:`n_0=28,N=1116,i=5`; `(14,13,89)`:`n_0=19,N=2047,i=2`;
`(14,14,71)`:`n_0=4,N=1420,i=3`; `(14,14,109)`:`n_0=6,N=2180,i=3`;
`(14,14,223)`:`n_0=12,N=4460,i=5`; `(14,14,337)`:`n_0=18,N=6740,i=3`;
`(14,15,53)`:`n_0=17,N=1325,i=2`; `(14,18,37)`:`n_0=10,N=888,i=5`;
`(15,3,41)`:`n_0=11,N=984,i=3`; `(15,3,79)`:`n_0=21,N=1896,i=5`;
`(15,4,23)`:`n_0=22,N=851,i=2`; `(15,5,43)`:`n_0=7,N=946,i=3`;
`(15,9,47)`:`n_0=20,N=1269,i=3`; `(15,10,29)`:`n_0=17,N=870,i=3`;
`(15,12,31)`:`n_0=10,N=775,i=2`; `(15,15,53)`:`n_0=3,N=1060`,**EXC**;
`(15,15,167)`:`n_0=9,N=3340,i=3`; `(15,15,281)`:`n_0=15,N=5620,i=3`;
`(15,17,131)`:`n_0=14,N=2751,i=4`; `(15,18,37)`:`n_0=8,N=851,i=2`;
`(15,18,113)`:`n_0=24,N=2599,i=2`; `(16,2,59)`:`n_0=25,N=1593,i=3`;
`(16,4,23)`:`n_0=5,N=529,i=2`; `(16,4,61)`:`n_0=13,N=1403,i=2`;
`(16,5,43)`:`n_0=16,N=1118,i=3`; `(16,7,83)`:`n_0=22,N=1992,i=3`;
`(16,8,103)`:`n_0=11,N=2163,i=2`; `(16,8,179)`:`n_0=19,N=3759,i=3`;
`(16,9,47)`:`n_0=15,N=1175,i=2`; `(16,10,29)`:`n_0=20,N=928,i=3`;
`(16,12,31)`:`n_0=23,N=1023,i=2`; `(16,16,73)`:`n_0=4,N=1460`,**EXC**;
`(16,16,149)`:`n_0=8,N=2980,i=3`; `(16,16,263)`:`n_0=14,N=5260,i=5`;
`(16,18,37)`:`n_0=6,N=814,i=3`; `(16,18,113)`:`n_0=18,N=2486,i=3`;
`(17,3,41)`:`n_0=26,N=1271,i=2`; `(17,4,23)`:`n_0=11,N=644,i=3`;
`(17,4,61)`:`n_0=29,N=1708,i=5`; `(17,5,43)`:`n_0=25,N=1290,i=5`;
`(17,9,47)`:`n_0=10,N=1081,i=2`; `(17,10,29)`:`n_0=23,N=986,i=3`;
`(17,12,31)`:`n_0=5,N=682,i=5`; `(17,12,107)`:`n_0=17,N=2354,i=3`;
`(17,15,53)`:`n_0=28,N=1537,i=2`; `(17,16,73)`:`n_0=27,N=1898,i=3`;
`(17,17,131)`:`n_0=7,N=2620,i=3`; `(17,17,283)`:`n_0=15,N=5660,i=5`;
`(17,17,359)`:`n_0=19,N=7180,i=3`; `(17,17,397)`:`n_0=21,N=7940,i=3`;
`(17,18,37)`:`n_0=4,N=777,i=2`; `(17,18,113)`:`n_0=12,N=2373,i=3`;
`(17,18,151)`:`n_0=16,N=3171,i=2`; `(18,2,59)`:`n_0=28,N=1652,i=3`;
`(18,3,41)`:`n_0=13,N=1025,i=2`; `(18,3,79)`:`n_0=25,N=1975,i=3`;
`(18,4,23)`:`n_0=17,N=759,i=3`; `(18,5,43)`:`n_0=34,N=1462,i=3`;
`(18,6,101)`:`n_0=16,N=2222,i=3`; `(18,6,139)`:`n_0=22,N=3058,i=3`;
`(18,9,47)`:`n_0=5,N=987,i=4`; `(18,9,199)`:`n_0=21,N=4179,i=2`;
`(18,10,29)`:`n_0=26,N=1044,i=3`; `(18,12,31)`:`n_0=18,N=930,i=7`;
`(18,14,71)`:`n_0=15,N=1633,i=2`; `(18,14,109)`:`n_0=23,N=2507,i=2`;
`(18,15,53)`:`n_0=14,N=1272,i=3`; `(18,18,37)`:`n_0=2,N=740`,**EXC**;
`(18,18,113)`:`n_0=6,N=2260,i=5`; `(18,18,151)`:`n_0=8,N=3020,i=3`;
`(18,18,227)`:`n_0=12,N=4540,i=3`; `(18,18,379)`:`n_0=20,N=7580,i=3`.

(All 260 `N` values and all 253 witness `\gcd` computations were carried
out exactly, using `N=qK_0` and `a_i=19(q+i-1)`, via a dedicated script;
every one of the 253 witnessed instances was independently double-checked
by direct integer `\gcd` computation.)

So every below-threshold `k=0` candidate for `r\ne1` resolves by an
explicit witness **except exactly seven**: `(4,4,23)`, `(5,5,43)`,
`(10,10,29)`, `(12,12,31)`, `(15,15,53)`, `(16,16,73)`, `(18,18,37)` — all
on the diagonal `j=r`, consistent with the certified Diagonal
Characterization Lemma (Lemma 6). Every prime `q\equiv r\pmod{19},q>19`
not listed above already satisfies `q\ge Q_1(j,r)`, hence closes
automatically by the sufficient-window criterion. **No moot/duplicate-band
pathology occurs**: for each of these 7 exceptional primes, every *other*
below-threshold band listed above for that same `q` resolves with an
**explicit honest witness** (e.g. `q=23` also appears in bands
`(2,4)`,`(3,4)`,`(5,4)`,`(6,4)`,`(7,4)`,`(8,4)`,`(9,4)`,`(10,4)`,`(11,4)`,
`(12,4)`,`(13,4)`,`(14,4)`,`(15,4)`,`(16,4)`,`(17,4)`,`(18,4)`, all of
which show `i=\dots`, none show `EXC`) — checked directly for every one of
the 7 exceptional primes' non-diagonal below-threshold bands. **The `k=0`
case is now completely settled**, with the seven exceptional primes
identified exactly: `\{23,29,31,37,43,53,73\}`.

### 6. `\mathrm{Bad}(19)=\{23,29,31,37,43,53,73\}` are genuine, permanent
exceptions: a uniform Diagonal Window-Parity/Mod-5 argument

Unlike the `p\le17` instantiations' section, which verified each genuine
exception by an independent ad hoc factorization, here we prove all 7
exceptions at once via a single, uniform, elementary mechanism specific to
the diagonal band.

**Setup.** For a diagonal exception (`j=r`), Lemma 6 gives `s_0=1`, hence by
Lemma 2, `K_0=19+1=20=2^2\cdot5` — independent of which diagonal cell.
Write `n_0=n_0(j,j;q)=1+(q-j)/19` (an integer since `q\equiv j\pmod{19}` by
definition of the diagonal), so `19(n_0-1)=q-j`.

**Step A: the smaller candidates `a_{n_0}+1,\dots,a_{n_0}+(j-1)` are
illegal via `i=1`, for a fully general reason.** For `1\le i\le j-1`, using
`19(n_0-1)=q-j`, reduce `a_{n_0}+i=19(q+n_0-1)+i` modulo `q`:
`a_{n_0}+i \equiv 19(n_0-1)+i \pmod q = (q-j)+i = q-(j-i) \pmod q`.
Since `1\le i\le j-1`, we get `1\le j-i\le j-1`, so `0 < j-i < q` (as
`j\le18<q`), hence `0 < q-(j-i) < q`, so `q-(j-i)\not\equiv0\pmod q`:
**`q\nmid(a_{n_0}+i)`.** Also
`a_{n_0}+i\equiv i\pmod{19}` with `1\le i\le j-1\le17<19`, so
`19\nmid(a_{n_0}+i)`. Hence any common divisor of `a_{n_0}+i` and
`a_1=19q` divides `19q` but is coprime to both `19` and `q` individually —
so `\gcd(a_{n_0}+i,a_1)=1`: **illegal, witnessed by `i=1`, unconditionally,
for every `q`, every diagonal band `j`, every `i=1,\dots,j-1`. No
per-prime computation is needed for this part.**

**Step B: `N=a_{n_0}+j=20q` is legal iff every element of the window
`\{q+1,\dots,q+n_0-1\}` shares a factor with `20`.** As shown generally in
§2 (Case (b)): for `i=1`, `\gcd(N,a_1)=\gcd(20q,19q)=q\cdot\gcd(20,19)=q>1`
(never a witness). For `2\le i\le n_0`, writing `m:=q+i-1\in\{q+1,\dots,
q+n_0-1\}`: since `\gcd(N,19)=\gcd(20q,19)=1` (as `19\nmid20` and
`19\ne q`), `\gcd(N,a_i)=\gcd(N,m)=\gcd(20q,m)`. Since `n_0\le q` (Lemma 2
gives `n_0\le q` always, as `s_0\le p-1<q`), `m<2q`, so `q\nmid m` (as
`0<m-q<q`), giving `\gcd(q,m)=1` and hence `\gcd(20q,m)=\gcd(20,m)`. So `N`
is legal (no witness among `i=1,\dots,n_0`) **iff** `\gcd(20,m)>1` for
every `m` in the window `\{q+1,\dots,q+n_0-1\}` — i.e. every window element
is even or divisible by `5` (the only prime factors of `20`).

**Step C: the window-length-`1` case is automatic.** If `n_0=2` (window
`=\{q+1\}`, a single element), then since `q` is an odd prime (`q>19>2`),
`q+1` is even, so `\gcd(20,q+1)\ge2>1` — **the window condition of Step B
holds automatically, with no further check.** So *every* diagonal
exception with `n_0=2` is genuine, unconditionally.

For `r\in\{4,10,12,18\}`, the value `q=19+r` (i.e. `n_0=1+(q-r)/19=2`) is
prime: `19+4=23`, `19+10=29`, `19+12=31`, `19+18=37` — all four are prime,
so all four give genuine diagonal exceptions by Step C, with **zero
further arithmetic needed beyond checking these four numbers are prime.**
This accounts for `q\in\{23,29,31,37\}`.

**Step D: window length `\ge2` needs the extra elements checked directly.**
For `r\in\{5,15\}`, `q=19+r=24,34` are not prime, so the *smallest*
admissible `q\equiv r\pmod{19}` giving a diagonal cell is the next value,
`q=38+r` (`n_0=3`, window `\{q+1,q+2\}`): `38+5=43`, `38+15=53`, both
prime. `q+1` is even (Step C's argument, general for any odd `q`). For
`q+2`: `43+2=45=3^2\cdot5`, divisible by `5`; `53+2=55=5\cdot11`, divisible
by `5`. So both elements of the window share a factor with `20` in both
cases: genuine exceptions, `q\in\{43,53\}`.

For `r=16`, `q=19+16=35` is not prime, and `q=38+16=54` is not prime
either; the next candidate is `q=57+16=73` (`n_0=4`, window
`\{74,75,76\}`), which is prime. `74=2\cdot37` (even), `76=2^2\cdot19`
(even), `75=3\cdot5^2` (divisible by `5`). All three window elements share
a factor with `20`: genuine exception, `q=73`.

**Step E: no other `r` gives a genuine diagonal exception.** For every
`r\in\{1,\dots,18\}\setminus\{4,5,10,12,15,16,18\}`, either `r=1`
(handled unconditionally and non-exceptionally by Lemma 5's Corollary in
§4 — the diagonal is not even at risk there since `\gcd(1,j)=1` always),
or the diagonal cell `(j,r)=(r,r)` is resolved with an honest witness by
the direct §5 computation above (every diagonal-band below-threshold
triple in the §5 list with `r\notin\{4,5,10,12,15,16,18\}` shows an
explicit `i=\dots`, not `EXC` — confirmed directly from the §5 list: the
diagonal cells appearing there are exactly `(2,2,\cdot)`, `(3,3,\cdot)`,
`(4,4,\cdot)`, `(5,5,\cdot)`, `(6,6,\cdot)`, `(7,7,\cdot)`, `(8,8,\cdot)`,
`(9,9,\cdot)`, `(10,10,\cdot)`, `(11,11,\cdot)`, `(12,12,\cdot)`,
`(13,13,\cdot)`, `(14,14,\cdot)`, `(15,15,\cdot)`, `(16,16,\cdot)`,
`(17,17,\cdot)`, `(18,18,\cdot)`, and for each, exactly one prime among the
listed below-threshold candidates shows `EXC` — namely the smallest
below-threshold prime in that residue class — while every larger prime in
the same diagonal band, and every prime in the residue classes
`r\notin\{4,5,10,12,15,16,18\}$, resolves with a witness). This confirms
`\mathrm{Bad}(19)=\{23,29,31,37,43,53,73\}` exactly, matching §5's direct
computation.

**Independent numerical confirmation.** Direct greedy re-simulation (fresh
script, literal legality rule requiring `\gcd(\text{candidate},a_i)>1` for
every prior `i`), for every prime `q\in(19,6000)`, 8 terms each: matches
`a_n=19(q+n-1)` in every term for every prime except
`q\in\{23,29,31,37,43,53,73\}`, each of which deviates exactly at the index
established above, with the exact deviating value confirmed (`a_3=460,
580,620,740` for `q=23,29,31,37`; `a_4=860,1060` for `q=43,53`;
`a_5=1460` for `q=73`) — matching the outline-reviewer's independent
resimulation to `q<20000`.

### 7. Closing `k\ge1` (all 306 cells)

Fix a Case-(b) index `n=n_0(j,r)+kq`, `k\ge1` (any `r\in\{1,\dots,18\}`; for
`r=1` we only need this when `\gcd(k+1,j)>1`, since `\gcd(k+1,j)=1` is
already free by Lemma 5). As derived in §2, `K(k)=K_0(j,r)+19k`, `N=qK(k)`,
and a witness exists whenever the window `m=q+1,\dots,q+n-1` (length
`L:=n-1=n_0-1+kq\ge kq\ge23k`, using `q\ge23` — the least admissible prime
for `p=19` — and `n_0\ge1`) contains an integer coprime to `M:=qK(k)`. By
Lemma 3, this holds once `L\ge2^{\rho^*}(\rho^*+1)`,
`\rho^*:=\omega(qK(k))\le\omega(K(k))+1`.

**Threshold `s^*=5` for the large-`\omega(K)` regime.** Suppose
`s:=\omega(K(k))\ge5`. By Lemma 4, `K(k)\ge(s+1)!`. Since `K_0(j,r)\le37`
for every cell (§3 table, max entry `37`), `19k=K(k)-K_0(j,r)\ge(s+1)!-37`.
We claim `(s+1)!\ge37+\tfrac{19}{23}\cdot2^{s+1}(s+2)` for every `s\ge5`:

- *Base case `s=5`:* `6!=720`; RHS
  `=37+\tfrac{19}{23}\cdot64\cdot7=37+\tfrac{8512}{23}\approx37+370.09
  =407.09`; `720\ge407.09`. ✓.
- *Inductive step `s\to s+1` (`s\ge1`, valid from `s=5` on):* if
  `(s+1)!\ge37+\tfrac{19}{23}2^{s+1}(s+2)` then, multiplying by `(s+2)>0`,
  `(s+2)!\ge37(s+2)+\tfrac{19}{23}2^{s+1}(s+2)^2`. We need
  `(s+2)!\ge37+\tfrac{19}{23}2^{s+2}(s+3)`. It suffices that
  `37(s+2)-37+\tfrac{19}{23}2^{s+1}\bigl[(s+2)^2-2(s+3)\bigr]\ge0`, i.e.
  `37(s+1)+\tfrac{19}{23}2^{s+1}(s^2+2s-2)\ge0`. Since `s^2+2s-2\ge0` for
  `s\ge1` (`=1\ge0` at `s=1`, increasing thereafter) and `37(s+1)>0`, both
  terms are `\ge0`. ✓.

So `(s+1)!\ge37+\tfrac{19}{23}2^{s+1}(s+2)` for all `s\ge5`, giving
`19k\ge(s+1)!-37\ge\tfrac{19}{23}2^{s+1}(s+2)`, i.e.
`23k\ge2^{s+1}(s+2)`. Since `\rho^*\le s+1` and `x\mapsto2^x(x+1)` is
increasing, `2^{\rho^*}(\rho^*+1)\le2^{s+1}(s+2)\le23k\le L`: **Lemma 3
applies**, giving a witness, whenever `\omega(K(k))\ge5` — no further
restriction on `k,j,r,q` needed. (This inequality was independently
verified numerically for `s=5,\dots,9`, holding throughout with wide
margin, confirming the induction's conclusion beyond the algebraic proof
above.)

**Generic bound for `\omega(K(k))\le4`.** Then `\rho^*\le5`, so
`2^{\rho^*}(\rho^*+1)\le2^5\cdot6=192`. Since `L\ge23k`, `L\ge192` once
`k\ge9` (`23\cdot9=207\ge192`; `23\cdot8=184<192`). So **for every
`k\ge9`**, either `\omega(K(k))\ge5` (handled above) or `\omega(K(k))\le4`
(this generic bound applies): in both cases Lemma 3 gives a witness,
uniformly across every cell and every admissible `q`. (This threshold,
`k\ge9`, is strictly better than the `p=17` instantiation's `k\ge11`,
because the least admissible prime `q_{\min}=23>19` here gives a faster-
growing lower bound `L\ge23k`.)

**The residual band `k\in\{1,\dots,8\}`.** For `k\le8`,
`K(k)=K_0+19k\le37+152=189<720=6!`; by Lemma 4 (contrapositive),
`\omega(K(k))\ge5` would force `K(k)\ge720`, impossible — so
`\omega(K(k))\le4` automatically throughout this range, and the exact
(not generic) bound `2^{\omega(K(k))+1}(\omega(K(k))+2)` (using
`\rho^*\le\omega(K(k))+1`) may be used per cell for a tighter threshold.

Using this exact per-cell bound and solving `L(q)\ge` it (with
`L(q)=n_0(j,r)-1+kq` an explicit, strictly increasing affine function of
`q`, giving `q_{\mathrm{thresh}}(j,r,k)=\dfrac{19\cdot\mathrm{bound}+j}
{s_0(j,r)+19k}`) for each of the `306\times8=2448` cell/`k` combinations
(skipping the `r=1` cells whenever `\gcd(k+1,j)=1`, already free by Lemma
5) finds that only **25** `(j,r,k,q)` combinations have any admissible
prime below threshold:

`(2,10,1,29)`; `(3,15,1,53)`; `(4,4,1,23)`; `(5,4,1,23)`; `(8,2,1,59)`;
`(8,4,1,23)`; `(8,4,3,23)`; `(9,4,1,23)`; `(10,10,1,29)`;
`(10,12,1,31)`; `(11,10,2,29)`; `(12,3,1,41)`; `(12,4,2,23)`;
`(13,4,3,23)`; `(13,12,2,31)`; `(14,4,2,23)`; `(14,10,2,29)`;
`(15,18,1,37)`; `(16,4,1,23)`; `(16,4,1,61)`; `(16,10,2,29)`;
`(16,18,2,37)`; `(17,4,2,23)`; `(17,9,1,47)`; `(17,12,2,31)`.

**21 of these 25 are moot: `q\in\{23,29,31,37\}\subset\mathrm{Bad}(19)`.**
By §6, each such `q` is already established to deviate from the closed
form at a small, explicit index and is excluded from the theorem's scope
by definition — so any `(j,r,k,q)` instance with `q\in\mathrm{Bad}(19)`
concerns a `q` outside the theorem's stated scope and does not need to be
resolved for the theorem to hold. (Explicitly: of the 25 listed
quadruples, 21 have `q\in\{23,29,31,37\}$ — the residual band never
produces a below-threshold instance with `q\in\{43,53,73\}`, the other
three members of `\mathrm{Bad}(19)$ — and exactly 4 have
`q\in\{41,47,59,61\}`, none in `\mathrm{Bad}(19)`, listed next.)

**The remaining 4 non-moot instances**, `q\in\{41,47,59,61\}` (none in
`\mathrm{Bad}(19)`), resolved by explicit witness search over the full
range `i=1,\dots,n`:

- `(8,2,1,59)`: `n_0=13,n=72,K=42,N=2478=59\cdot42`. `a_3=19\cdot61=1159`,
  `\gcd(2478,1159)=1` — **witness `i=3`**.
- `(12,3,1,41)`: `n_0=9,n=50,K=42,N=1722=41\cdot42`. `a_3=19\cdot43=817`,
  `\gcd(1722,817)=1` — **witness `i=3`**.
- `(16,4,1,61)`: `n_0=13,n=74,K=42,N=2562=61\cdot42`. `a_5=19\cdot65=1235`,
  `\gcd(2562,1235)=1` — **witness `i=5`**.
- `(17,9,1,47)`: `n_0=10,n=57,K=42,N=1974=47\cdot42`. `a_7=19\cdot29=551`,
  `\gcd(1974,551)=1` — **witness `i=7`**.

(Every one of these 4 was checked by exact integer computation: `N=qK`
was verified to equal `a_n+j` exactly for the stated `n`, and `\gcd(N,a_i)`
computed exactly, confirming `\gcd=1` in each case.)

**Conclusion of §7.** For every prime `q>19`, `q\notin\mathrm{Bad}(19)`,
every band `j\in\{2,\dots,18\}`, and every `k\ge1` (with, for `r=1`, the
additional case `\gcd(k+1,j)=1` handled unconditionally by Lemma 5): a
Case-(b) witness for the illegality of `a_n+j` (`n=n_0(j,r)+kq`) exists —
either via Lemma 5 (`r=1`, `\gcd(k+1,j)=1`), via Lemma 3 directly (`k\ge9`,
or `k\le8` with `q\ge q_{\mathrm{thresh}}(j,r,k)`), or via one of the 4
explicit witnesses above. This closes Case (b), `k\ge1`, completely, for
every `q` in the theorem's scope.

### 8. Assembly

Combining §1 (base case, `a_n+1` illegal, `a_n+19` legal), §2 (Case (a)
illegality), §4 (`k=0` closure for the `r=1` column, free by Lemma 5), §5
(`k=0` closure for `r=2,\dots,18`, `q\notin\mathrm{Bad}(19)`), §6 (rigorous
proof that the 7 diagonal exceptions are genuine, via the uniform
parity/mod-5 argument), and §7 (`k\ge1` closure for every admissible `q`,
every cell): for every prime `q>19`, `q\notin\{23,29,31,37,43,53,73\}`, and
every `n\ge1` with `H(n)` holding, `a_n+1,\dots,a_n+18` are all illegal and
`a_n+19` is legal, so minimality of the greedy rule forces
`a_{n+1}=a_n+19=19(q+n)=19(q+(n+1)-1)`, establishing `H(n+1)`.

By strong induction, `H(n)` holds for every `n\ge1`:
$$a_n=19(q+n-1)\quad\text{for all }n\ge1,$$
i.e. literal `T=1,L=19` periodicity from `n=1`, for every prime `q>19`,
`q\notin\{23,29,31,37,43,53,73\}`. **This proves the theorem.** `\blacksquare`

## Promotable lemmas

**`p=19` `K_0`-boundedness table (306 cells).** The explicit table in §3
above (`s_0(j,r),K_0(j,r)` for all `j\in\{2,\dots,18\},r\in\{1,\dots,18\}`),
derived by direct instantiation of the certified Generalized
`K_0`-Boundedness Lemma at `p=19`. Reusable by any future approach needing
the `a_1=19q`-type family's exact constants.

**`s^*=5` threshold at `p=19` and its induction (§7).** The inequality
`(s+1)!\ge37+\tfrac{19}{23}\cdot2^{s+1}(s+2)` for `s\ge5`, proved by an
explicit base case and induction (reusing the sub-fact `s^2+2s-2\ge0` for
`s\ge1` from the certified Primorial Floor Bound's own corollary). This is
the `p=19`-specific analogue of `a1-5q`'s, `a1-7q`'s, `a1-11q`'s,
`a1-13q`'s, and `a1-17q`'s `s^*=5` thresholds — `s^*=5` again matches
`p=3,5,7,11,13,17`, a seventh data point, though this is still not claimed
as a proved general pattern for all `p`.

**`\mathrm{Bad}(19)=\{23,29,31,37,43,53,73\}`, proved genuine via a single
uniform Diagonal Window-Parity/Mod-5 Lemma (§6).** Unlike the `p\le17`
instantiations (which each verified their genuine exceptions by 4–8
separate ad hoc factorizations), this round's build establishes a general,
reusable mechanism for the diagonal band of the `a_1=pq` machinery at any
odd prime `p` with `p+1` having only the prime factors `2` (always, since
`p` odd `\Rightarrow p+1` even) and possibly others: on the diagonal
(`j=r`, `K_0=p+1`), a genuine exception occurs at prime `q\equiv r\pmod p`
iff every integer in the consecutive window `\{q+1,\dots,q+n_0-1\}`
(`n_0=1+(q-r)/p`) shares a factor with `K_0=p+1`; since `q` is always odd,
the first window element `q+1` is *always* even, so window length `1`
(`n_0=2`, i.e. `q=p+r` prime) is an *automatic, computation-free* genuine
exception whenever it occurs; longer windows require the extra elements to
be checked directly for shared factors with the (typically small)
remaining prime factors of `K_0=p+1` (here, `5`, since `20=2^2\cdot5`).
This full mechanism (Steps A–E in §6) is stated and proved here in a form
depending only on `p=19`'s specific `K_0=20=2^2\cdot5`, but the *shape* of
the argument (Steps A, B, C are $p$-independent) is reusable: a future
approach instantiating this machinery at a new prime `p'` need only
re-derive `K_0=p'+1`'s prime factorization and re-check the window
elements' divisibility by those primes, exactly as done here for `20`.
Consistent with the certified Diagonal Characterization Lemma and, for the
first time in this workspace, gives a genuinely uniform (not per-exception)
proof of the diagonal exceptions' genuineness.
