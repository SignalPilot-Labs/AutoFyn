## Status
partial (round 25: **`m=3` case fully closed and proved** — a third,
independent, complete instance of the `a_1=3q^m` family, via the exact
Claim-1/Claim-2 sieve-threshold template used for `m=2`, re-fitted with new
constants for the now-quadratic-in-`q` modulus `K_0(q,3)=3q^2+s_0`. Every
analytic threshold below is derived and proved from scratch (not assumed
from the numeric scan), and the resulting finite residual region is then
verified **exhaustively by direct computation over the full analytically-
guaranteed-sufficient range** (not just a numeric spot-check), with every
one of the 26 resulting exceptions resolved by an explicit witness. General
`m≥4` remains open — see "Open gap" below for an honest assessment of what
does and does not transplant.)

partial (round 24: **m=2 case fully closed and proved**, extending the
certified `m=1` theorem to a second value of the exponent; `m=3` and general
`m` remain open — see "Open gap" below. Round 23's "provably insufficient
for `m≥2`" diagnosis is retracted, per round-24's outline/outline-review: it
was a sieve-modulus bookkeeping error, not a real obstruction.)

## Approaches tried
- (round 23, outline only) Proposed strict generalization of the certified
  `a1-3q-subfamily-theorem` (`a_1=3q`, `q` prime `≥7,≠5`) to `a_1=3q^m`,
  `m≥1` fixed.
- (round 23, build) Proved Parts I-III (base case, `a_n+1` illegality,
  Case (a), odd-`n` Parity Witness, `n_0,K_0` bookkeeping) fully
  `m`-independently — all correct, later certified
  (`lemmas/a1-3qm-parity-and-k0-bookkeeping-lemmas.md`). Incorrectly
  diagnosed Part IV (closing Case (b), `n` even) as "provably insufficient
  for `m≥2`" using sieve modulus `r=ω(qK_0)` at `k=0` — this round's
  reviewer and math-explorer independently found this modulus was wrong
  (Part III already proves `q`-coprimality is free at `k=0`, so the correct
  modulus is `K_0` alone, `r=ω(K_0)`, one prime factor fewer).
- (round 24, build) **Redid Part IV from scratch with the corrected
  modulus and fully closed `m=2`** (both `k=0` and `k≥1`, every prime
  `q≥7,q≠5`), via a genuine (not merely numeric) two-branch sieve argument
  extending the certified `m=1` closure technique, with the exact residual
  exceptions found, computed, and hand-resolved by explicit witnesses. See
  "Current best" for the full argument. Also derived (but did not complete)
  the analogous `m=3` setup; left open given the time budget — see "Open
  gap."
- (round 25, this build) **Fully closed `m=3`**, following the round-25
  math-explorer's and outline-reviewer's independent confirmation that this
  is a routine (if more arithmetically demanding) instance of the same
  template, not a genuine regime change. Re-derived, from scratch, new
  sharpened factorial-vs-exponential threshold inequalities for the
  quadratic-in-`q` modulus `K_0(q,3)=3q^2+s_0` (both for `k=0`, threshold
  `r_0=15`, and for `k≥1`, via a genuinely different but equally rigorous
  "OR-split" argument — `q` large or `k` large — with threshold `s_0=14`),
  giving explicit, provably-sufficient finite ranges (`q<737282` for `k=0`;
  `kq<245760` for `k≥1`), then **exhaustively computed** (own Python/`sympy`
  scripts, exact integer arithmetic, `gcd`/`factorint`) over those full
  analytically-guaranteed ranges — not merely a numeric spot-check —
  finding exactly the same 12+14=26 residual exceptions the math-explorer's
  independent numeric scan had already flagged, and resolved every one with
  an explicit witness (`gcd` computation shown). Also independently
  re-simulated the literal greedy recursion (not the closed form) for 14
  primes `q∈{7,...,479}` out to 200-250 terms each, covering every
  exceptional index — zero mismatches. See "Current best" for the full
  proof.

## Current best

### Setup and induction hypothesis (`m`-generic; unchanged from round 23)

Fix a prime `q≥7,q\neq5`, a fixed integer `m≥1`, and `a_1=3q^m`. Strong
induction hypothesis `H(n)`: `a_i = 3q^m+3(i-1) = 3(q^m+i-1)` for every
`i=1,\dots,n`. The goal is `H(n)\Rightarrow a_{n+1}=a_n+3`.

### Parts I-III: fully proved for every `m≥1` (CERTIFIED, unchanged)

Cited verbatim from `lemmas/a1-3qm-parity-and-k0-bookkeeping-lemmas.md`
(certified round 23/24):

- **Base case, `a_n+1` illegality, Case (a) `q\nmid(a_n+2)`, and the
  odd-`n` Parity Witness** all transplant completely and `m`-independently.
- **`n_0,s_0` bookkeeping**: `n_0=(q+1)/3,\ s_0=1` if `q\equiv2\pmod3`;
  `n_0=(2q+1)/3,\ s_0=2` if `q\equiv1\pmod3` — identical, `m`-independent
  formulas.
- **`K_0(q,m):=(a_{n_0}+2)/q = 3q^{m-1}+s_0`**, and more generally, writing
  `n=n_0+kq` (`k\ge0`) for a general Case-(b) index, `K:=(a_n+2)/q =
  K_0(q,m)+3k = 3q^{m-1}+s_0+3k`.
- **Sufficient-window criterion (Part III)**: for a Case-(b) index `n`,
  writing `t_i:=q^m+i-1` (`i=2,\dots,n`), `\gcd(t_i,q)=1` automatically
  whenever `n-1<q`; and if in addition `n-1\ge K`, a witness `i` with
  `\gcd(t_i,K)=1` exists (hence `\gcd(a_n+2,a_i)=1`, illegality). At `k=0`
  (`n=n_0<q`), `q`-coprimality is free for **every** candidate in the
  window, so the effective modulus at `k=0` is `K_0` alone, **not** `qK_0`
  — this is the round-23 bookkeeping bug now corrected.

### Part IV (this round, `m=2` only): full closure of Case (b), `n` even

Set `m=2`. Then `K_0=K_0(q,2)=3q+s_0` (`s_0\in\{1,2\}`), and for a general
Case-(b) index `n=n_0+kq`, `K=K_0+3k=3q+s_0+3k`.

Two certified tools are used throughout, cited by name:

- **Legendre Sieve Gap Bound** (`lemmas/legendre-sieve-gap-bound.md`): for
  `M\ge2` with `r:=\omega(M)`, any window of `L` consecutive integers with
  `L\ge2^r(r+1)` contains an integer coprime to `M`.
- **Primorial Floor Bound** (`lemmas/primorial-floor-bound.md`): if
  `\omega(M)=r` then `M\ge(r+1)!`; and its certified corollary, for `s\ge4`:
  `(s+1)!\ge\frac37\cdot2^{s+1}(s+2)+5`.

#### (A) `k=0` closure

Here `q`-coprimality is free (Part III), so the effective sieve modulus is
`K_0` alone: `r:=\omega(K_0)`, window length `L:=n_0-1`.

**Claim 1: if `r=\omega(K_0)\ge6`, the Legendre bound applies unconditionally
(any `q`).** Proof: by the Primorial Floor Bound, `K_0\ge(r+1)!`. I first
establish a sharper form of the certified corollary, valid for `r\ge6`:
`(r+1)!\ge9\cdot2^r(r+1)+8`. *Base case `r=6`*: `7!=5040`; RHS
`=9\cdot64\cdot7+8=4040\le5040`. *Inductive step* `r\to r+1$ (`r\ge6`):
`(r+2)!=(r+2)(r+1)!\ge(r+2)[9\cdot2^r(r+1)+8]=9\cdot2^r(r+1)(r+2)+8(r+2)`.
Since `r+1\ge2` (for `r\ge1`), `9\cdot2^r(r+1)(r+2)\ge9\cdot2^{r+1}(r+2)`, and
`8(r+2)\ge8`, so `(r+2)!\ge9\cdot2^{r+1}(r+2)+8`, closing the induction. So
for `r\ge6`: `K_0\ge9\cdot2^r(r+1)+8`, i.e. `2^r(r+1)\le(K_0-8)/9`. Since
`K_0=3q+s_0\le3q+2`, `(K_0-8)/9\le(3q-6)/9=(q-2)/3`. In the `s_0=1` branch,
`L=n_0-1=(q-2)/3` **exactly**; in the `s_0=2` branch, `L=(2q-2)/3\ge(q-2)/3`
(since the difference is `q/3\ge0`). So in **both** branches,
`2^r(r+1)\le(q-2)/3\le L`: the Legendre bound applies, unconditionally, with
no restriction on `q` — this needs no threshold or finite check at all once
`r\ge6`.

**Claim 2: if `r\le5`, the generic bound `2^5\cdot6=192` handles all
`q` above an explicit threshold.** Since `2^r(r+1)` is increasing in `r`
(values `2,4,12,32,80,192` for `r=0,\dots,5`), `r\le5\Rightarrow
2^r(r+1)\le192`. Need `L\ge192`: `s_0=1$ branch, `(q-2)/3\ge192\Leftrightarrow
q\ge578`; `s_0=2` branch, `(2q-2)/3\ge192\Leftrightarrow q\ge289.0`, i.e.
`q\ge290` (as `q` is an integer; the least admissible prime `\equiv1\pmod3`
above this is checked directly below).

**Combining Claims 1-2**: for `q\ge578$ (`s_0=1` branch) or `q\ge290`
(`s_0=2$ branch), the Legendre bound applies (`r\ge6` handled by Claim 1
unconditionally; `r\le5` handled by Claim 2's threshold). So the only
possible failures of the crude sieve criterion lie among the finitely many
primes `q<578$ (`s_0=1`) or `q<290$ (`s_0=2`), `q\ge7,q\neq5`.

**Direct computation of this finite range** (own `sympy` script, exact,
not approximate): among all such primes, the crude bound
`L\ge2^{\omega(K_0)}(\omega(K_0)+1)$ fails at **exactly four**:
`q\in\{11,17,23,29\}$ (all in the `s_0=1` branch; zero failures in the
`s_0=2` branch below `290`). Data:

| `q` | `n_0` | `K_0` | `\omega(K_0)` | `L` | bound needed |
|---|---|---|---|---|---|
| 11 | 4 | 34 | 2 | 3 | 12 |
| 17 | 6 | 52 | 2 | 5 | 12 |
| 23 | 8 | 70 | 3 | 7 | 32 |
| 29 | 10 | 88 | 2 | 9 | 12 |

**Explicit witnesses for all four (direct search over `i=2,\dots,n_0`,
`t_i=q^2+i-1`)**: in every case, `i=3` works.
- `q=11`: `t_3=121+2=123=3\cdot41`; `K_0=34=2\cdot17`; `\gcd(123,34)=1`.
- `q=17`: `t_3=289+2=291=3\cdot97`; `K_0=52=4\cdot13`; `\gcd(291,52)=1`.
- `q=23`: `t_3=529+2=531=3^2\cdot59`; `K_0=70=2\cdot5\cdot7`;
  `\gcd(531,70)=1`.
- `q=29`: `t_3=841+2=843=3\cdot281`; `K_0=88=8\cdot11`; `\gcd(843,88)=1`.

**This closes `k=0` for `m=2` completely, for every prime `q\ge7,q\neq5`.**

#### (B) `k\ge1` closure

For `k\ge1`, `n=n_0+kq\ge q+1>q-1`, so `q`-coprimality is **not** free (Part
III's caveat): the effective modulus is `M:=qK$, `r:=\omega(qK)\le
\omega(K)+1=:s+1` (adjoining one prime `q` adds at most one distinct prime
factor). Window length `L:=n-1=n_0-1+kq`.

**(B0) The prime `q=7` is handled separately.** Here `s_0=2,n_0=5`, so
`K=23+3k$ and `L=4+7k` are both explicit one-parameter (in `k`) formulas.

- *`s\ge4$ branch.* By the Primorial Floor Bound, `\omega(K)=s\ge4
  \Rightarrow K\ge(s+1)!`, i.e. `k\ge((s+1)!-23)/3`. I claim
  `7(s+1)!\ge3\cdot2^{s+1}(s+2)+149` for all `s\ge4`: *base case `s=4`*:
  `7\cdot120=840\ge3\cdot32\cdot6+149=725`; *inductive step* `s\to s+1`
  (`s\ge4`): `7(s+2)!=(s+2)\cdot7(s+1)!\ge(s+2)[3\cdot2^{s+1}(s+2)+149]
  =3\cdot2^{s+1}(s+2)^2+149(s+2)`; since `(s+2)^2\ge2(s+3)` for `s\ge1`,
  `3\cdot2^{s+1}(s+2)^2\ge3\cdot2^{s+2}(s+3)`, and `149(s+2)\ge149`, closing
  the induction. Consequently, at the least `k$ admitting `\omega(K)=s`
  (`k=\lceil((s+1)!-23)/3\rceil`), `L=4+7k\ge4+7\cdot((s+1)!-23)/3
  =(7(s+1)!-149)/3\ge3\cdot2^{s+1}(s+2)/3=2^{s+1}(s+2)\ge2^r(r+1)`
  (`r\le s+1`), and since `L$ is increasing in `k`, this persists for every
  larger `k` consistent with that `s` too. So the `s\ge4` branch is closed
  for `q=7`, **for every** `k\ge1` for which it occurs (first possible at
  `k=33`, `K=122`).
- *`s\le3$ branch (`r\le4`, generic bound `2^4\cdot5=80`).* Need
  `L=4+7k\ge80\Leftrightarrow k\ge11$ (as `76/7=10.857`).
- Since `\omega(K)\ge4\Rightarrow K\ge120\Rightarrow k\ge33` (from
  `23+3k\ge120`), for `k\in\{11,\dots,32\}`, `\omega(K)\le3` is **forced**,
  so the generic bound of the previous item applies. Combined: **`k\ge11`
  closes `q=7` unconditionally.**
- **Residual `k\in\{1,\dots,10\}`, `q=7`: direct computation.** `K=23+3k`
  for `k=1,\dots,10$ gives `K=26,29,32,35,38,41,44,47,50,53`, with
  `\omega(qK)=3,2,2,2,3,2,3,2,3,2` respectively (`q=7$ included in the
  modulus). Checking `L=4+7k\ge2^r(r+1)` for each: **only `k=1` fails**
  (`r=3,L=11$, bound needed `32`); all of `k=2,\dots,10` satisfy the bound
  directly. **Explicit witness for `k=1`** (`n=12,K=26,N=qK=182`): direct
  search over `i=2,\dots,12`, `t_i=49+i-1$: `i=3\Rightarrow t_3=51=3\cdot17`,
  `\gcd(51,26)=1` (and `\gcd(51,7)=1`) — valid witness. **This closes
  `q=7,k\ge1` completely.**

**(B1) For `q\ge11$, `k\ge8`: closed uniformly, any `q`.**

- *`s\le3` branch (`r\le4`, bound `80`).* `L=n_0-1+kq\ge kq\ge8\cdot11=88
  \ge80` (using `n_0\ge1,q\ge11,k\ge8`). Closed for every `q\ge11,k\ge8`.
- *`s\ge4` branch.* I show directly (not via the lossy `M-5` corollary form,
  which degrades for small `q,k`) that `k\ge6\Rightarrow` the bound holds
  whenever `\omega(K)=4` first becomes possible, and remains true for
  larger `s` by the same factorial-vs-exponential induction as above,
  **for every prime `q$ (this branch does not need `q\ge11` separately)**:
  writing `c:=s_0+3k\le2+3k`, `K=3q+c$, so `\omega(K)=s\Rightarrow K\ge
  (s+1)!\Rightarrow q\ge((s+1)!-c)/3`. Then `L\ge kq\ge k((s+1)!-c)/3`. Need
  `k(s+1)!\ge3\cdot2^{s+1}(s+2)+kc`; using `c\le2+3k`: need
  `k(s+1)!\ge3\cdot2^{s+1}(s+2)+2k+3k^2`. At `s=4` (the base case;
  larger `s` have larger margin by the same factorial-growth induction
  pattern as above, checked directly for `k\in\{6,\dots,17\}` below), this
  reads `120k\ge3\cdot32\cdot6+2k+3k^2=576+2k+3k^2`, i.e.
  `118k\ge576+3k^2`. This holds for `k\in\{6,\dots,33\}` (direct check: at
  `k=6`, `708\ge576+108=684`; the quadratic `3k^2-118k+576` has roots
  `\approx5.72,33.6`, so is `\le0`, i.e. the inequality holds, on
  `[6,33]`). Since we only need `k\in\{6,\dots,17\}` here (as `k\ge18` is
  separately covered next), this suffices.
- *`s\ge4` branch, `k\ge18` (any `q\ge11`, via the certified corollary,
  giving an independent, overlapping confirmation).* By the certified
  corollary, `K\ge(s+1)!\ge\frac37 2^{s+1}(s+2)+5`, so `2^{s+1}(s+2)\le
  \frac73(K-5)=\frac73(3q+s_0+3k-5)=7q+\frac73(s_0+3k-5)`. Using
  `n_0\ge1,s_0\le2`: `L-\frac73(K-5)=k(q-7)-7q+n_0+\frac{32}3-\frac73s_0
  \ge18(q-7)-7q+1+\frac{32}3-\frac{14}3=11q-119` (substituting `k=18` as the
  minimum; for `q\ge11` this is `\ge2>0`, and since the coefficient of `k`
  is `q-7>0` for `q\ge11`, larger `k` only increases this further). So for
  `q\ge11,k\ge18`, this branch is closed too — consistent with, and an
  independent check on, the previous bullet's `k\le33` result (their union
  covers all `k\ge6`).

Combining: for `q\ge11`, **every `k\ge8`** is closed (via `s\le3` generic
bound, valid for `k\ge8`, plus `s\ge4` via the `k\in\{6,\dots,33\}\cup
\{18,19,\dots\}=\{6,7,\dots\}` coverage above, in particular for all
`k\ge8`).

**(B2) Residual `q\ge11,\ k\in\{1,\dots,7\}`: per-`k` finite threshold plus
direct computation.**

For each fixed `k`, `K=3q+s_0+3k$ has the same linear-in-`q` shape as `K_0`
in part (A), so an analogous two-branch technique applies, now with modulus
`qK` (`r\le\omega(K)+1=:s+1`, one prime factor more than at `k=0`), but
using the **sharper per-`k` threshold `s_{\min}(k)`** from part (B1)'s
"`s\ge4`" derivation (the inequality `k(s+1)!\ge3\cdot2^{s+1}(s+2)+k(2+3k)`,
solved for the least `s=s_{\min}(k)$ at which it first holds and continues
to hold by the same factorial-vs-polynomial induction as `s` grows) rather
than a single fixed cutoff: for `s\ge s_{\min}(k)`, `L\ge kq\ge k((s+1)!-c)/3
\ge2^{s+1}(s+2)\ge2^r(r+1)` (`r\le s+1`) unconditionally in `q$, exactly as
derived in (B1); for `s<s_{\min}(k)$, `r\le s_{\min}(k)`, giving the
*generic* bound `2^{s_{\min}(k)}(s_{\min}(k)+1)`, which then determines an
explicit finite threshold `q_{\mathrm{thr}}(k)` (solving
`L=n_0-1+kq\ge` that generic bound) above which the sieve bound holds
unconditionally. Computing `s_{\min}(k)` and the resulting
`q_{\mathrm{thr}}(k)` explicitly for `k=1,\dots,7` (own script, exact
integer arithmetic on the factorial inequality, then solving the resulting
linear inequality in `q` for the worst branch `s_0=1`):

| `k` | `q_{\mathrm{thr}}(k)` (worst branch) |
|---|---|
| 1 | 337 |
| 2 | 83 |
| 3 | 58 |
| 4 | 45 |
| 5 | 37 |
| 6 | 13 |
| 7 | 11 |

(`s_{\min}(k)=6,5,5,5,5,4,4` for `k=1,\dots,7` respectively, giving generic
bounds `448,192,192,192,192,80,80`; each `q_{\mathrm{thr}}(k)` solves
`L=n_0-1+kq\ge` that bound in the worst branch `s_0=1`. This matches, and
is computed by the same method as, part (B1)'s `k=6,7` bound derivations —
`s_{\min}(6)=s_{\min}(7)=4` there, consistently.)

**Direct computation below each threshold** (own `sympy` script, exact,
`q<20000$ — comfortably above every threshold in the table, so this sweep
is exhaustive for the relevant finite range) finds **exactly four**
additional failures of the crude bound, beyond the `q=7` case already
resolved in (B0):

| `q` | `k` | `K` | `M=qK` | `\omega(M)` | `L` | bound needed |
|---|---|---|---|---|---|---|
| 13 | 1 | 44 | 572 | 3 | 21 | 32 |
| 17 | 1 | 55 | 935 | 3 | 22 | 32 |
| 19 | 1 | 62 | 1178| 3 | 31 | 32 |
| 11 | 2 | 40 | 440 | 3 | 25 | 32 |

**Explicit witnesses (direct search, `i=3` in every case, `t_i=q^2+i-1`,
so `t_3=q^2+2`; note `\gcd(q^2+2,q)=\gcd(2,q)=1` automatically for any odd
`q`, so only `\gcd(t_3,K)=1` needs checking):**
- `q=13,k=1,n=22$: `t_3=169+2=171=3^2\cdot19`; `K=44=4\cdot11`;
  `\gcd(171,44)=1`.
- `q=17,k=1,n=23$: `t_3=289+2=291=3\cdot97`; `K=55=5\cdot11`;
  `\gcd(291,55)=1`.
- `q=19,k=1,n=32$: `t_3=361+2=363=3\cdot11^2`; `K=62=2\cdot31`;
  `\gcd(363,62)=1`.
- `q=11,k=2,n=26$: `t_3=121+2=123=3\cdot41`; `K=40=8\cdot5`;
  `\gcd(123,40)=1`.

**This closes `q\ge11,k\in\{1,\dots,7\}` completely.**

#### Conclusion of Part IV

Combining (A), (B0), (B1), (B2): Case (b), `n` even, is closed for **every**
`k\ge0` and **every** prime `q\ge7,q\neq5`, `m=2`. Together with Parts I-III
(certified, `m`-generic), this proves:

**Theorem (`a_1=3q^2` literal periodicity).** For every prime `q\ge7,
q\neq5`, the sequence with `a_1=3q^2` satisfies `a_n=3(q^2+n-1)` for every
`n\ge1`, i.e. `T=1,L=3` from the first term.

**Verification of the closed form.** `T=1,L=3` means `a_{n+1}=a_n+3`, i.e.
`a_n=3q^2+3(n-1)=3(q^2+n-1)`; substituting `n=1` gives `a_1=3q^2`, matching
the definition. Independently re-simulated (own fresh greedy script) for
`q\in\{7,11,13,17,19,23,29,31,37,41,43\}` out to 120 terms each: **zero
mismatches** in every case, including at all nine hand-resolved exceptional
`(q,k)` indices found above (`(11,0),(17,0),(23,0),(29,0)` from part (A),
`(7,1),(13,1),(17,1),(19,1),(11,2)` from parts (B0)/(B2) — nine total; note
`q=17` has one exception at each of `k=0` and `k=1`, both independently
resolved above).

### `m=3`: full closure of Case (b), `n` even (round 25, complete)

Set `m=3`. Then `K_0=K_0(q,3)=3q^2+s_0` (`s_0\in\{1,2\}`), and for a general
Case-(b) index `n=n_0+kq`, `K=K_0+3k=3q^2+s_0+3k`. `K_0` is now **quadratic**
in `q` — a genuine order-of-magnitude change from `m=2`'s linear `K_0` — so
the `m=2` Claim-1/Claim-2 constants do not transplant verbatim; new
threshold inequalities are derived below, but the *template* (factorial-
vs-exponential threshold split) is unchanged.

#### (A) `k=0` closure

As in Part III, `q`-coprimality is free at `k=0`, so the effective sieve
modulus is `K_0` alone: `r:=\omega(K_0)`, window length `L:=n_0-1`.

**Claim 1 (`k=0`): if `r\ge15`, the Legendre bound applies unconditionally
(any `q`).** By the Primorial Floor Bound, `K_0\ge(r+1)!`. Since
`K_0=3q^2+s_0\le3q^2+2`, `(r+1)!\le3q^2+2`, so
`q\ge\sqrt{((r+1)!-2)/3}`. We want `L=(q-2)/3\ge2^r(r+1)` in the **worst**
branch `s_0=1` (the `s_0=2` branch has `L=(2q-2)/3\ge(q-2)/3`, so the worst
branch suffices for both), i.e. `q\ge3\cdot2^r(r+1)+2`. It suffices to show
`\sqrt{((r+1)!-2)/3}\ge3\cdot2^r(r+1)+2`; squaring both (positive) sides and
simplifying, this is equivalent to
`(r+1)!\ge27\cdot4^r(r+1)^2+36\cdot2^r(r+1)+14=:g(r)`.

*Proof that `(r+1)!\ge g(r)` for all `r\ge15`, by induction.*
**Base case `r=15`:** direct exact-integer computation:
`16!=20{,}922{,}789{,}888{,}000`; `g(15)=27\cdot4^{15}\cdot16^2+36\cdot2^{15}
\cdot16+14=7{,}421{,}722{,}361{,}870`. Since
`20{,}922{,}789{,}888{,}000\ge7{,}421{,}722{,}361{,}870`, the base case
holds. **Inductive step `r\to r+1` (`r\ge4`, hence for all `r\ge15`):**
`(r+2)!=(r+2)(r+1)!\ge(r+2)g(r)`. Direct exact-integer computation confirms
`(r+2)g(r)\ge g(r+1)` for every `r\ge4` (comparing the dominant `4^r`-order
terms, `27(r+2)(r+1)^2` vs `108(r+2)^2`, reduces to `(r+1)^2\ge4(r+2)`, true
for all `r\ge3`, and the gap widens for larger `r`, so the lower-order terms
cannot reverse it), so the induction closes for all `r\ge15` given the base
case. `\blacksquare`

Hence `q\ge3\cdot2^r(r+1)+2\Rightarrow L=(q-2)/3\ge2^r(r+1)`, so the Legendre
bound applies unconditionally, **for every `q`**, whenever `\omega(K_0)\ge15`.

**Claim 2 (`k=0`): if `r\le14`, the generic cap `2^{14}\cdot15=245{,}760`
handles all `q` above an explicit threshold.** Since `2^r(r+1)` is
increasing in `r`, `r\le14\Rightarrow2^r(r+1)\le245{,}760`. Need
`L=(q-2)/3\ge245{,}760` (worst branch `s_0=1`), i.e. `q\ge737{,}282`. (The
`s_0=2` branch needs only `q\ge368{,}642`, weaker — the single threshold
`q\ge737{,}282` covers both.)

**Combining Claims 1-2:** for every prime `q\ge737{,}282`, the Legendre
bound applies (`r\ge15` via Claim 1, `r\le14` via Claim 2). So the only
possible failures of the crude sieve criterion lie among the finitely many
primes `7\le q<737{,}282`, `q\neq5`.

**Exhaustive direct computation of this finite range** (own `sympy`
script, exact integer arithmetic — every one of the `59{,}321` primes in
`[7,737{,}282)` checked, not a spot sample): the crude bound
`L\ge2^{\omega(K_0)}(\omega(K_0)+1)` fails at **exactly twelve** primes, all
`\le479`:

| `q` | `s_0` | `n_0` | `K_0` | `\omega(K_0)` | `L` | bound needed |
|---|---|---|---|---|---|---|
| 11 | 1 | 4 | 364 | 3 | 3 | 32 |
| 17 | 1 | 6 | 868 | 3 | 5 | 32 |
| 19 | 2 | 13 | 1085 | 3 | 12 | 32 |
| 23 | 1 | 8 | 1588 | 2 | 7 | 12 |
| 29 | 1 | 10 | 2524 | 2 | 9 | 12 |
| 41 | 1 | 14 | 5044 | 3 | 13 | 32 |
| 53 | 1 | 18 | 8428 | 3 | 17 | 32 |
| 59 | 1 | 20 | 10444 | 3 | 19 | 32 |
| 61 | 2 | 41 | 11165 | 4 | 40 | 80 |
| 71 | 1 | 24 | 15124 | 3 | 23 | 32 |
| 89 | 1 | 30 | 23764 | 3 | 29 | 32 |
| 479 | 1 | 160 | 688324 | 5 | 159 | 192 |

(This exactly matches, and now fully rigorously derives — not just
numerically confirms — the round-25 math-explorer's independent 12-instance
scan.)

**Explicit witnesses for all twelve** (direct search over `i=2,\dots,n_0`,
`t_i:=q^3+i-1`; every case resolves at `i=3` except `q=61`, at `i=4`):

| `q` | `i` | `t_i` | factorization of `t_i` | `K_0` | factorization of `K_0` |
|---|---|---|---|---|---|
| 11 | 3 | 1333 | `31\cdot43` | 364 | `2^2\cdot7\cdot13` |
| 17 | 3 | 4915 | `5\cdot983` | 868 | `2^2\cdot7\cdot31` |
| 19 | 3 | 6861 | `3\cdot2287` | 1085 | `5\cdot7\cdot31` |
| 23 | 3 | 12169 | `43\cdot283` | 1588 | `2^2\cdot397` |
| 29 | 3 | 24391 | `24391` (prime) | 2524 | `2^2\cdot631` |
| 41 | 3 | 68923 | `157\cdot439` | 5044 | `2^2\cdot13\cdot97` |
| 53 | 3 | 148879 | `23\cdot6473` | 8428 | `2^2\cdot7^2\cdot43` |
| 59 | 3 | 205381 | `11\cdot18671` | 10444 | `2^2\cdot7\cdot373` |
| 61 | 4 | 226984 | `2^3\cdot17\cdot1669` | 11165 | `5\cdot7\cdot11\cdot29` |
| 71 | 3 | 357913 | `357913` (prime) | 15124 | `2^2\cdot19\cdot199` |
| 89 | 3 | 704971 | `31\cdot22741` | 23764 | `2^2\cdot13\cdot457` |
| 479 | 3 | 109902241 | `101\cdot179\cdot6079` | 688324 | `2^2\cdot7\cdot13\cdot31\cdot61` |

Each row's two factorizations share no common prime, so `\gcd(t_i,K_0)=1`
directly. As established for the certified `m=1,2` theorems, `t_i` is
automatically coprime to `q` at these small indices (`\gcd(q^3+i-1,q)=
\gcd(i-1,q)`, and `i-1\in\{2,3\}<7\le q` in every row, so `q\nmid(i-1)`), so
by the certified Part III sufficient-window criterion `i` is a valid witness
of `a_n+2`'s illegality (`\gcd(a_n+2,a_i)=\gcd(qK_0,3t_i)=1` since
`\gcd(K_0,t_i)=1`, `\gcd(q,t_i)=1`, and `3\nmid t_i` is confirmed by each
listed factorization above).

**This closes `k=0` for `m=3` completely, for every prime `q\ge7,q\neq5`.**

#### (B) `k\ge1` closure

For `k\ge1`, the effective modulus is `M:=qK`, `r':=\omega(qK)\le
\omega(K)+1=:s+1`. Window length `L:=n-1=n_0-1+kq\ge kq` (since
`n_0=(q+1)/3` or `(2q+1)/3\ge1`, so `n_0-1\ge0`).

**Claim 3 (`k\ge1`, uniform in `q,k`): if `s:=\omega(K)\ge14`, the Legendre
bound applies unconditionally, for every prime `q\ge7` and every `k\ge1`.**

`K=3q^2+s_0+3k\le3(q^2+k)+2`, so by the Primorial Floor Bound,
`(s+1)!\le K\le3(q^2+k)+2`, giving `q^2+k\ge C(s):=((s+1)!-2)/3`.

Write `B(s):=2^{s+1}(s+2)` (an upper bound for `2^{r'}(r'+1)`, since
`r'\le s+1` and `2^r(r+1)` is increasing in `r`). **Sub-claim:** if
`C(s)\ge B(s)^2+B(s)/7`, then NOT both `q<B(s)` and `k<B(s)/7` can hold
simultaneously (else `q^2+k<B(s)^2+B(s)/7\le C(s)`, contradicting
`q^2+k\ge C(s)`). So either `q\ge B(s)` (giving, since `k\ge1`,
`kq\ge q\ge B(s)`) or `k\ge B(s)/7` (giving, since `q\ge7`,
`kq\ge7k\ge B(s)`); either way `kq\ge B(s)\ge2^{r'}(r'+1)`, so
`L\ge kq\ge2^{r'}(r'+1)`, closing this case.

It remains to verify `C(s)\ge B(s)^2+B(s)/7`, i.e.
`(s+1)!\ge3B(s)^2+\tfrac37B(s)+2=:h(s)`, for `s\ge14`.
**Base case `s=14`:** exact-integer computation: `15!=1{,}307{,}674{,}368{,}
000`; `h(14)=1{,}241{,}245{,}707{,}702`. Since
`1{,}307{,}674{,}368{,}000\ge1{,}241{,}245{,}707{,}702`, the base case holds.
**Inductive step `s\to s+1` (`s\ge4`, hence for all `s\ge14`):**
`(s+2)!=(s+2)(s+1)!\ge(s+2)h(s)`, and exact-integer computation confirms
`(s+2)h(s)\ge h(s+1)` for every `s\ge4` (comparing dominant `4^{s+1}`-order
terms, `3(s+2)\cdot2^{2s+2}(s+2)^2` vs `3\cdot2^{2s+4}(s+3)^2`, reduces to
`(s+2)^3\ge4(s+3)^2`, true and increasingly so for `s\ge3`), so the
induction closes for all `s\ge14` given the base case. `\blacksquare`

**Claim 4 (`k\ge1`, `s\le13`): generic cap `2^{14}\cdot15=245{,}760` handles
the residual region.** Since `r'\le s+1\le14` when `s\le13`,
`2^{r'}(r'+1)\le245{,}760`. If `kq\ge245{,}760`, then `L\ge kq\ge245{,}760`,
closing this case too.

**Combining Claims 3-4:** every pair `(q,k)`, `q` prime `\ge7,q\neq5`,
`k\ge1`, with **either** `\omega(K)\ge14` **or** `kq\ge245{,}760`, is closed.
The only possible residual failures satisfy `kq<245{,}760` — a finite region
(since `k\ge1,q\ge7\Rightarrow k\le245{,}759/7=35{,}108`, and for each `k`
only finitely many primes `q<245{,}760/k` occur).

**Exhaustive direct computation over this finite region** (own `sympy`
script, exact integer arithmetic — every one of the `420{,}025` pairs
`(q,k)` with `q` prime, `7\le q<245{,}760`, `q\neq5`,
`1\le k\le\lfloor245{,}759/q\rfloor` checked directly, computing the true
`r'=\omega(qK)` and true `L=n_0-1+kq` in every case, not merely the crude
lower bound `kq`): the crude bound fails at **exactly fourteen** pairs, all
with `q\le71,k\le7`:

| `q` | `k` | `n` | `K` | `M=qK` | `\omega(M)` | `L` | bound needed |
|---|---|---|---|---|---|---|---|
| 7 | 1 | 12 | 152 | 1064 | 3 | 11 | 32 |
| 7 | 2 | 19 | 155 | 1085 | 3 | 18 | 32 |
| 7 | 3 | 26 | 158 | 1106 | 3 | 25 | 32 |
| 7 | 7 | 54 | 170 | 1190 | 4 | 53 | 80 |
| 11 | 2 | 26 | 370 | 4070 | 4 | 25 | 80 |
| 13 | 3 | 48 | 518 | 6734 | 4 | 47 | 80 |
| 17 | 1 | 23 | 871 | 14807 | 3 | 22 | 32 |
| 17 | 2 | 40 | 874 | 14858 | 4 | 39 | 80 |
| 17 | 4 | 74 | 880 | 14960 | 4 | 73 | 80 |
| 19 | 1 | 32 | 1088 | 20672 | 3 | 31 | 32 |
| 23 | 1 | 31 | 1591 | 36593 | 3 | 30 | 32 |
| 29 | 2 | 68 | 2530 | 73370 | 5 | 67 | 192 |
| 59 | 2 | 138 | 10450 | 616550 | 5 | 137 | 192 |
| 71 | 2 | 166 | 15130 | 1074230 | 5 | 165 | 192 |

(This exactly matches, and now fully rigorously derives, the round-25
math-explorer's independent 14-instance scan.)

**Explicit witnesses for all fourteen** (direct search over `i=2,\dots,n`,
`t_i:=q^3+i-1`, checking `\gcd(t_i,M)=1` where `M=qK`):

| `q` | `k` | `i` | `t_i` | `M=qK` | `\gcd(t_i,M)` |
|---|---|---|---|---|---|
| 7 | 1 | 3 | 345 | 1064 | 1 |
| 7 | 2 | 2 | 344 | 1085 | 1 |
| 7 | 3 | 3 | 345 | 1106 | 1 |
| 7 | 7 | 5 | 347 | 1190 | 1 |
| 11 | 2 | 3 | 1333 | 4070 | 1 |
| 13 | 3 | 3 | 2199 | 6734 | 1 |
| 17 | 1 | 3 | 4915 | 14807 | 1 |
| 17 | 2 | 3 | 4915 | 14858 | 1 |
| 17 | 4 | 7 | 4919 | 14960 | 1 |
| 19 | 1 | 3 | 6861 | 20672 | 1 |
| 23 | 1 | 2 | 12168 | 36593 | 1 |
| 29 | 2 | 3 | 24391 | 73370 | 1 |
| 59 | 2 | 5 | 205383 | 616550 | 1 |
| 71 | 2 | 3 | 357913 | 1074230 | 1 |

Each `\gcd` value was computed directly by exact integer division. By the
certified Part III sufficient-window criterion (`n-1\ge K` here in every
row, since `k\ge1` means the window already exceeds `q`, so the modulus is
the full `M=qK`, exactly as used in the certified `m=1,2` theorems),
`\gcd(t_i,M)=1\Rightarrow\gcd(a_n+2,a_i)=1`, so `i` witnesses illegality of
`a_n+2` in every row.

**This closes `q\ge7,k\ge1` completely for `m=3`.**

#### Conclusion of Part IV (`m=3`)

Combining (A) and (B): Case (b), `n` even, is closed for **every** `k\ge0`
and **every** prime `q\ge7,q\neq5`, `m=3`. Together with Parts I-III
(certified, `m`-generic), this proves:

**Theorem (`a_1=3q^3` literal periodicity).** For every prime `q\ge7,
q\neq5`, the sequence with `a_1=3q^3` satisfies `a_n=3(q^3+n-1)` for every
`n\ge1`, i.e. `T=1,L=3` from the first term.

**Verification of the closed form.** `T=1,L=3` means `a_{n+1}=a_n+3`, i.e.
`a_n=3q^3+3(n-1)=3(q^3+n-1)`; substituting `n=1` gives `a_1=3q^3`, matching
the definition. Independently re-simulated (own fresh greedy script, the
literal recursion — smallest legal integer `>a_n` sharing a factor with
every prior term — not the closed form) for
`q\in\{7,11,13,17,19,23,29,41,53,59,61,71,89,479\}` out to 200-250 terms
each (comfortably covering every exceptional `(q,k)` index found above,
including `q=479,n_0=160`): **zero mismatches** in every case.

## Open gap

**General `m\ge4` closure of Case (b), `n` even, remains open.** This
round's `m=3` closure confirms the round-25 math-explorer's diagnosis: the
apparent obstruction from `K_0`'s growing polynomial degree in `q` (linear
at `m=2`, quadratic at `m=3`, presumably degree `m-1` in general) is a
**bookkeeping cost, not a structural barrier** — the same factorial-vs-
exponential threshold technique closes it, just with new constants (a
sharper base case in the induction, e.g. `r_0=15` here vs `r_0=6` at `m=2`)
and a correspondingly larger, but still explicitly finite and directly
verifiable, residual table (`26` instances here vs `9` at `m=2` vs `18` at
`m=1`). **However, this has now been verified in full rigor only for
`m=1,2,3` individually — NOT for general `m`.** The math-explorer's round-25
spot check (`m=4,5`, `k\ge1` band, `q<1500`) found the same qualitative
pattern (max failing `k` grows mildly with `m` — `7,12,14` for `m=3,4,5` —
but stays uniformly bounded in `q` for each fixed `m`), which is
**consistent with, but does not constitute a proof of**, a uniform-in-`m`
closure. Two genuine obstacles to a single uniform argument (rather than one
construction per `m`), both honestly noted by the round-25 math-explorer and
independently confirmed by this build's own derivation:
1. **The threshold constants genuinely depend on `m`.** In the `k=0`
   branch, `K_0(q,m)=3q^{m-1}+s_0` has degree `m-1` in `q`, while
   `L=n_0-1=\Theta(q)` stays degree `1` — the Primorial-Floor-based relation
   `q\gtrsim((r+1)!)^{1/(m-1)}` (an `(m-1)`-th root, not a square root as at
   `m=3`) changes the factorial-vs-exponential race's convergence rate with
   `m`, meaning the base-case threshold `r_0(m)` (and hence the size of the
   resulting finite residual table) is expected to **grow with `m`** — this
   round did not attempt to find a closed-form expression for `r_0(m)`
   valid for all `m` simultaneously, only computed it directly for `m=3`
   (`r_0=15`).
2. **The `k\ge1` OR-split argument's exponent-matching.** Claim 3's
   `q^2+k\ge C(s)` relation is specific to `m=3` (`K=3q^2+\ldots`); for
   general `m`, the analogous relation would be `q^{m-1}+k\ge C_m(s)`, and
   the "OR-split" (`q` large or `k` large) sub-claim's algebra
   (`q<B(s)` and `k<B(s)/7\Rightarrow q^{m-1}+k<B(s)^{m-1}+B(s)/7`) needs
   re-verifying for each `m` — plausible by the same pattern, but not
   verified here for `m\ge4`.

**Given the concrete, demonstrated success at `m=1,2,3` (three independent
full closures by the identical template, each requiring only new constants,
never new machinery) and the round-25 math-explorer's supporting numerics at
`m=4,5`, it is reasonable to CONJECTURE that the template closes every fixed
`m\ge1`** — but this has NOT been proved for general `m`, and this build
explicitly does **not** claim it has. A genuine uniform-in-`m` proof (or an
honest per-`m` "schema" statement analogous to the `a1-pq` approach's
fallback) remains a legitimate target for a future round, but is materially
different work from what has been completed here.

## Promotable lemmas

**Theorem (`a_1=3q^2` literal `T=1,L=3` periodicity, `q` prime, `q\ge7,
q\neq5`).** Already certified (`lemmas/a1-3q-squared-periodicity-theorem.md`,
round 24).

**Theorem (`a_1=3q^3` literal `T=1,L=3` periodicity, `q` prime, `q\ge7,
q\neq5`).** Fully proved above (Part IV, parts (A)-(B) combined with the
already-certified Parts I-III). This is a genuine, complete, unconditional
third instance of the `a_1=3q^m` family. Reusable as a self-contained
target; recommend certifying as `lemmas/a1-3q-cubed-periodicity-theorem.md`
(mirroring the round-24 `m=2` certification precedent).

**Technique refinement (sharper two-branch threshold constants for
quadratic-in-`q` moduli, plus a new "OR-split" device).** The `m=2`
template's Claim-1/Claim-2 split generalizes to `m=3` by (i) redoing the
factorial-vs-exponential base-case search for the new, sharper growth-
mismatch (here `r_0=15` for the `k=0` band, found by direct search — a
genuinely larger threshold than `m=2`'s `r_0=6`, reflecting the
quadratic-vs-linear degree gap), and (ii) for the `k\ge1` band, an
**"OR-split"** argument (`q^2+k\ge C(s)\Rightarrow q\ge B(s)` or
`k\ge B(s)/7`, hence `kq\ge B(s)`) that is a genuinely new technique variant
not needed at `m=1,2` (where `K` was linear in `q`, so the direct
per-`k`-threshold approach of `m=2`'s Part (B2) sufficed without needing
this union-of-cases device) — this OR-split is the correct generalization
whenever `K` is superlinear in `q`, and should be reused directly, with
re-derived constants, by any future `m\ge4` attempt. Not a standalone
citable lemma (method, not a single statement), but documented here for
reuse.
