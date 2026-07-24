## Status
solved for `a=1,...,5` (all prime `q≥7` outside an explicit, tiny, `a`-dependent
finite exceptional set: `a=1`: `q≠5`; `a=2`: `q∉{5,11}`; `a=3,4,5`: `q≠5`) —
this round's build, closing the outline. The general-`a` architecture is
proven (existence of the finite residual band is established for every fixed
`a≥1` via an elementary, effective procedure), but the residual band itself
is only explicitly computed and hand-verified through `a=5`; see "Open gap
for general `a`" below for the precise honest scope limit. Overall workspace
Status (H1/FAH, H2) is untouched by this subfamily result.

## Approaches tried
- (round 24, outline only) Proposed `a_1=3^a*q` as the correct generalization
  axis (small-prime exponent, opposite of the stuck `a1-3qk` large-prime
  exponent axis). Numeric support for `a=1..5`.
- (round 24, this build) Derived the exact `K_0(q,a)` formula, found and
  fixed a load-bearing bug in a naive transplant of the certified `a1-3q`
  witness identity (the shift is `3^{a-1}q`, not `q`, for `a>1` — see below),
  closed the full induction for `a=1,...,5` using the certified Legendre
  Sieve Gap Bound and Primorial Floor Bound (generalized to an arbitrary
  additive constant), found and confirmed the single genuine exception
  `a=2,q=11` (matches the outline's numeric flag exactly, with an exact
  mechanism-level proof of why it breaks, not just a numeric observation),
  and confirmed by independent simulation (`a=1..5`, `q<200` primes, 40 terms
  each, zero mismatches outside the one flagged exception; direct
  confirmation `a_5=110≠111` for `a=2,q=11`).

## Current best

### Setup
Fix `a≥1` and a prime `q≥7`, `q≠3` (so `P(a_1)=\{3,q\}`, two distinct primes).
Let `a_1=3^a q`. Strong induction hypothesis `H(n)`:
`a_i = 3^a q + 3(i-1)` for `i=1,\dots,n` (so `3\mid a_i` for every such `i`).

### Part 1 — steps that transplant verbatim from `a1-3q` (mechanism uses only
`P(a_1)=\{3,q\}` and `3\mid a_1`, not the numeric value of `a_1`)

**(0) Base case** `n=1`: `a_1=3^a q` by definition.

**(1) `a_n+1` illegal.** `\gcd(a_n+1,a_n)=1` (consecutive integers) — illegal
via `i=n`.

**(2) `3\nmid(a_n+2)`.** Since `3\mid 3^a q=a_1` (as `a\ge1`) and `3\mid3(i-1)`
for every `i`, `3\mid a_i` for all `i\le n` by `H(n)`; in particular `3\mid a_n`,
so `a_n+2\equiv2\pmod3`.

**(3) Illegality of `a_n+2`, Case (a): `q\nmid(a_n+2)`.** Any common divisor of
`a_n+2` and `a_1=3^a q` divides `3^a q`, hence is built from the primes
`\{3,q\}` (the only primes dividing `3^a q`, since `q\ne3` is prime). By (2),
`3\nmid(a_n+2)`; by the Case-(a) hypothesis `q\nmid(a_n+2)`. So
`\gcd(a_n+2,a_1)=1` — illegal via `i=1`.

**(4) Illegality of `a_n+2`, Case (b), sub-case `n` odd (Parity Witness,
re-derived — cleaner than the `a=1` derivation since it does not need to pass
through `q+n`).** Let `N:=a_n+2=3^a q+3n-1`. Since `3^a` is odd (odd`^`
anything is odd; more simply, `3` is odd and a product of odd numbers is odd)
and `q` is an odd prime, `3^a q` is odd. And `3n` has the same parity as `n`.
So `N = (\text{odd}) + 3n - 1 \equiv (\text{even}) + 3n \pmod2`, i.e. `N`'s
parity equals the parity of `3n`, i.e. of `n`. In particular, **`n` odd
`\Rightarrow N` odd `\Rightarrow \gcd(N,2)=1`.** By `H(n)`, `a_n=N-2`, so
`\gcd(N,a_n)=\gcd(N,N-2)=\gcd(N,2)` (the standard identity
`\gcd(x,y)=\gcd(x,x-y)` applied with `x=N,y=a_n`). Hence for `n` odd,
`\gcd(N,a_n)=1` — illegal via `i=n`. This holds for **every** `a\ge1`,
uniformly, with no case split on `q` or `k`.

**(3'') `a_n+3=3^a q+3n=3(3^{a-1}q+n)` legal.** For every `i\le n`, `a_i=3^a
q+3(i-1)` is a multiple of `3` (by (2)'s reasoning), and `a_n+3` is a
multiple of `3`; so `\gcd(a_n+3,a_i)\ge3>1` for every `i\le n` — legal
against every prior term. (This step needs only `a\ge1`, not the specific
value of `a`.)

So, in every case reducible to (1)–(4)+(3''), the induction closes exactly as
in the certified `a_1=3q` theorem. **The only genuinely new content is Case
(b), `n` even** (`q\mid(a_n+2)`), covered by Part 2 below.

### Part 2 — the new load-bearing content: Case (b), `n` even

**(5) Reduction of Case (b) to a residue condition mod `q`, independent of
`a`.** `a_n+2 = 3^a q+3n-1 \equiv 3n-1 \pmod q` (since `q\mid 3^a q`). So
Case (b) (`q\mid(a_n+2)`) holds exactly when `q\mid(3n-1)` — **the same
condition as in the `a=1` case**, independent of `a`. Since `\gcd(3,q)=1`
(`q\ne3`), `3` is invertible mod `q`, so `\{n : q\mid(3n-1)\}` is exactly one
residue class mod `q`; let `n_0\in\{1,\dots,q-1\}` be its least representative
(so all Case-(b) indices are `n=n_0+kq`, `k\ge0`). As in the certified proof:
`3n_0-1\in\{q,2q\}` (the only multiples of `q` in `\{2,\dots,3q-4\}`), giving
`s_0:=(3n_0-1)/q\in\{1,2\}`; explicitly `s_0=1,n_0=(q+1)/3` if `q\equiv2
\pmod3`, and `s_0=2,n_0=(2q+1)/3` if `q\equiv1\pmod3` (these are the only two
residues since `q\ne3`).

**(6) `K_0(q,a) := (a_{n_0}+2)/q` is `q`-INDEPENDENT — the key new fact.**
`a_{n_0}+2 = 3^a q + 3n_0-1 = 3^a q + s_0 q = q(3^a+s_0)`. So
`K_0(a) := 3^a+s_0 \in \{3^a+1,\ 3^a+2\}`, a constant depending only on `a`
and on `q\bmod3` — **not on the magnitude of `q`**. This proves, rather than
merely observes numerically, the outline's conjectured criterion:
`a_1=3^a q` keeps `K_0` bounded as `q\to\infty` for every fixed `a`, exactly
the opposite failure mode from `a_1=3q^m` (`m\ge2`), where the analogous
quantity grows linearly in `q`.

**(7) The correct witness identity for general `n=n_0+kq` (`k\ge0`) — where a
naive transplant of the `a=1` argument is WRONG for `a>1`.** Write
`K:=(a_n+2)/q`. As in (6)'s computation, `a_n+2 = 3^a q+3n_0-1+3kq =
q(3^a+s_0+3k) = q(K_0(a)+3k)`, so `K=K_0(a)+3k`. Set `N:=a_n+2=qK`; by (2)'s
argument `3\nmid N`. For `i\le n`, write `a_i=3\cdot(a_i/3)`, where, by
`H(n)`, `a_i/3 = 3^{a-1}q+(i-1)` (**not** `q+(i-1)` unless `a=1` — this is the
point where a literal copy of the `a=1` derivation fails: for `a=1`,
`3^{a-1}=1` and the two agree, but for `a\ge2` they differ, and using the
wrong one silently produces an incorrect "witness" that does not actually
exist, as verified below on `a=2,q=11`). Since `3\nmid N`,
`\gcd(N,a_i)=\gcd(N,a_i/3)=\gcd(qK,\,cq+(i-1))`, where `c:=3^{a-1}`. So: for
`i=2,\dots,n`, the quantity `m_i:=cq+(i-1)` ranges over the `L:=n-1`
**consecutive integers** `cq+1,\dots,cq+(n-1)`, and `a_n+2` is illegal iff
some `m_i` in this window is coprime to `M:=qK`.

**This is structurally identical to the certified `a1-3q` closure's sieve
setup** (a window of `L` consecutive integers required to contain an integer
coprime to `M=qK`) — the only difference is the window's *starting point*
(`cq+1` instead of `q+1`). Since the certified **Legendre Sieve Gap Bound**
(`lemmas/legendre-sieve-gap-bound.md`: any window of `L\ge2^r(r+1)`
consecutive integers, `r:=\omega(M)`, contains an integer coprime to `M`) is a
statement about *any* window of `L` consecutive integers regardless of
location, the entire closure machinery transplants — **provided one is
careful to use the correct window `cq+1,\dots,cq+(n-1)` when doing any
DIRECT (non-asymptotic) witness check**, which is exactly where a naive
transplant breaks (see the `a=2,q=11` exception below).

### (8) A generalized Primorial Floor Corollary (new, needed for `a\ge2`)

The certified **Primorial Floor Bound** (`lemmas/primorial-floor-bound.md`)
gives, unconditionally, `M\ge(r+1)!` whenever `\omega(M)=r`. Its stated
Corollary (`(s+1)!\ge\frac37 2^{s+1}(s+2)+5` for `s\ge4`) was proved by an
induction whose base case used the specific constant `5`. We need the same
inequality with a larger additive constant (since `K_0(a)=3^a+s_0` can exceed
`5` for `a\ge2`). The **same induction works for any constant `C\ge0`**:

**Generalized Primorial Floor Corollary.** Fix `C\ge0` and let `s_1\ge1` be
any integer with `(s_1+1)!\ge\frac37 2^{s_1+1}(s_1+2)+C`. Then
`(s+1)!\ge\frac37 2^{s+1}(s+2)+C` for every `s\ge s_1`.

*Proof.* Induction on `s\ge s_1`. Base case is the hypothesis. Inductive step
`s\to s+1` (`s\ge s_1\ge1`): `(s+2)!=(s+2)(s+1)!\ge(s+2)\left[\frac37
2^{s+1}(s+2)+C\right]` (by IH) `=\frac37 2^{s+1}(s+2)^2+C(s+2)`. Since
`(s+2)^2\ge2(s+3)` for all `s\ge1` (`(s+2)^2-2(s+3)=s^2+2s-2\ge1>0` at `s=1`,
and increasing thereafter as its derivative `2s+2>0`), `\frac37
2^{s+1}(s+2)^2\ge\frac37 2^{s+2}(s+3)`; and `C(s+2)\ge C` (as `s+2\ge1`).
Adding: `(s+2)!\ge\frac37 2^{s+2}(s+3)+C`, closing the induction. `\blacksquare`

This is the certified corollary's own proof with `5` replaced by a variable
`C` throughout — the induction never used the specific value `5` except as
the base case's target, so it generalizes verbatim.

### (9) Closing Case (b), `n` even, for `a=1,\dots,5`: the effective procedure

Fix `a\in\{1,\dots,5\}`. Let `K_0^{\max}(a):=3^a+2` (the larger of the two
branch values `3^a+1,3^a+2`, used uniformly so the same threshold covers both
branches). By exhaustive search (a finite computation, since factorials grow
without bound relative to `\frac37 2^{s+1}(s+2)`, as `(s+1)!/2^{s+1}=
\prod_{j=1}^{s+1}j/2\ge\frac12\left(\frac32\right)^{s-1}\to\infty` while
`2^{s+1}(s+2)/2^{s+1}=s+2` grows only linearly — so a base case `s_1(a)`
satisfying the hypothesis of (8) always exists and is found by direct
search), we compute the least `s_1(a)` with
`(s_1(a)+1)!\ge\frac37 2^{s_1(a)+1}(s_1(a)+2)+K_0^{\max}(a)`:

| `a` | `K_0^{\max}(a)` | `s_1(a)` | `B(a):=2^{s_1(a)}(s_1(a)+1)` | `k_{\mathrm{thresh}}(a):=\lceil B(a)/7\rceil` |
|---|---|---|---|---|
| 1 | 5 | 4 | 80 | 12 |
| 2 | 11 | 4 | 80 | 12 |
| 3 | 29 | 4 | 80 | 12 |
| 4 | 83 | 5 | 192 | 28 |
| 5 | 245 | 5 | 192 | 28 |

(`a=1` reproduces the certified `a1-3q` values exactly, a consistency check.)

**Case split for `n=n_0+kq`, `k\ge0`, `K:=K_0(a)+3k`, `s:=\omega(K)`, `r:=
\omega(qK)\le s+1`, `L:=n-1\ge kq` (for `k\ge1`; for `k=0`, `L=n_0-1`):**

- **If `s\ge s_1(a)`:** by (8) (with `C=K_0^{\max}(a)`), `K\ge(s+1)!\ge\frac37
  2^{s+1}(s+2)+K_0^{\max}(a)\ge\frac37 2^{s+1}(s+2)+K_0(a)`. Since
  `K=K_0(a)+3k`, this gives `3k\ge\frac37 2^{s+1}(s+2)`, i.e.
  `7k\ge2^{s+1}(s+2)\ge2^r(r+1)` (as `r\le s+1` and `x\mapsto2^x(x+1)` is
  increasing). For `k\ge1`, `L\ge kq\ge7k\ge2^r(r+1)`, so the **Legendre
  Sieve Gap Bound** applies directly: a witness exists. (Direct check for
  each `a\in\{1,\dots,5\}`: `\omega(K_0(a))\le2<s_1(a)`, so `s\ge s_1(a)`
  never occurs at `k=0`; this sub-case is vacuous for `k=0`, consistent with
  handling `k=0` in the table below.)
- **If `s<s_1(a)`:** then `r\le s_1(a)`, so `2^r(r+1)\le2^{s_1(a)}(s_1(a)+1)
  =B(a)`. If `k\ge k_{\mathrm{thresh}}(a)`, `L\ge7k\ge B(a)\ge2^r(r+1)`:
  Legendre applies directly. This leaves exactly `k\in\{0,1,\dots,
  k_{\mathrm{thresh}}(a)-1\}` — a **finite range depending only on `a`, not
  on `q`** — needing direct treatment.

**Residual range, both branches, `a=1,\dots,5`: exhaustive direct
verification.** For each `k\in\{0,\dots,k_{\mathrm{thresh}}(a)-1\}` and each
branch `K_0(a)\in\{3^a+1,3^a+2\}`, `K=K_0(a)+3k` is an explicit fixed integer
(independent of `q`), so `\omega(K)` is computed exactly; using the
GENERIC bound `r_{\mathrm{gen}}:=\omega(K)+1\ge r` (valid since `\omega(qK)
\le\omega(K)+1` regardless of whether `q\mid K`), we get an explicit,
`q`-independent bound `2^{r_{\mathrm{gen}}}(r_{\mathrm{gen}}+1)`, and (since
`L(q)` is an explicit strictly increasing affine function of `q` in each
branch: `L(q)=kq+n_0(q)-1`, with `n_0(q)=(q+1)/3` or `(2q+1)/3`) an explicit
threshold `q_{\mathrm{thresh}}(k,a)` past which `L(q)\ge2^{r_{\mathrm{gen}}}
(r_{\mathrm{gen}}+1)` automatically, by monotonicity of `L(q)` in `q`
(both branch slopes are positive since `k\ge0`). For every admissible prime
`q<q_{\mathrm{thresh}}(k,a)` in the correct residue class mod `3`, we
directly check whether the true `r_{\mathrm{actual}}:=\omega(qK)` already
satisfies `2^{r_{\mathrm{actual}}}(r_{\mathrm{actual}}+1)\le L(q)` (Legendre
applies with no further work); if not, we run an **exhaustive search** for a
witness `i\in\{2,\dots,n\}` directly (i.e. find `i` with `\gcd(K_0(a)+3k,\,
3^{a-1}q+(i-1))=1` — this is a finite, mechanical check on explicit small
integers, not an appeal to "clearly").

This procedure was carried out completely (via exact integer arithmetic) for
`a=1,\dots,5`. Result: **every single instance in the residual range has an
explicit witness found by direct search, except exactly one:**

**`a=2`, branch `K_0=3^2+1=10` (`q\equiv2\pmod3`), `k=0`, `q=11`.** Here
`n_0=(11+1)/3=4`, and the only candidates are `i=2,3,4` (window length
`L=3`). Direct check (`c=3^{a-1}=3`): `m_2=3\cdot11+1=34`, `m_3=35`,
`m_4=36`; `\gcd(10,34)=2`, `\gcd(10,35)=5`, `\gcd(10,36)=2` — **no witness in
`\{2,3,4\}`.** (Contrast: naively using the WRONG window `q+i-1=12,13,14`, as
a careless transplant of the `a=1` formula would, gives `\gcd(10,13)=1` and
falsely "finds" a witness at `i=3` — this is exactly the bug flagged at the
top of (7), and the reason a literal copy-paste of the `a=1` proof is
unsound for `a\ge2`.) Directly verifying against the true sequence: `a_1=99,
a_2=102,a_3=105,a_4=108`; `\gcd(110,99)=11`, `\gcd(110,102)=2`,
`\gcd(110,105)=5`, `\gcd(110,108)=2` — every `i\le4` has `\gcd(110,a_i)>1`,
so `110=a_4+2` **is legal**, forcing `a_5=110\ne111=3^2\cdot11+3\cdot4`. This
is confirmed by direct greedy simulation: `99,102,105,108,\mathbf{110},114,
120,126,132,135,\dots` — the pattern genuinely breaks at `n=5`, exactly as
the round-24 explorer found. **This is a genuine, permanent, mechanism-level
exception** (not a finite-search artifact): `a_1=9q` at `q=11` fails literal
`T=1,L=3` periodicity from `n=5` on.

Every other instance in the residual range (all `a=1,3,4,5` cases, and every
other `a=2` case) has an explicit, directly-verified witness. (This
independently reproduces, as a special case, the certified `a=1` residual
table's own three below-threshold instances `(k,K_0,q)=(1,5,7),(2,4,11),
(3,5,7)`, confirming the general procedure specializes correctly to the
already-certified theorem.)

### (10) Exclusion of `q=5`, for every `a\ge1` (uniform mechanism, generalizing
the certified `a=1` exclusion)

For `q=5\equiv2\pmod3`: `n_0=(5+1)/3=2`, branch `K_0(a)=3^a+1`. The window at
`k=0` is `i=2` only (`L=n_0-1=1`), i.e. `m_2=c\cdot5+1` (`c=3^{a-1}`).
**`K_0(a)=3^a+1` is always even** (`3^a` is odd for every `a\ge0`, `+1` makes
it even). **`m_2=5c+1` is always even** too (`c=3^{a-1}` is odd for `a\ge1`,
`5c` is odd, `+1` is even). So `\gcd(K_0(a),m_2)\ge2>1` for **every** `a\ge1`
— no witness exists at the unique candidate `i=2`, so `a_2+2` is legal, and
the induction is broken at `n=3` for every `a\ge1`. This is a complete,
mechanism-level (not merely observed) proof that `q=5` must be excluded for
every fixed `a\ge1`, generalizing the certified `a=1` exclusion (which is the
`a=1` instance of this same uniform parity fact).

### (11) Assembly and final statement

**Theorem.** Fix `a\in\{1,2,3,4,5\}`. Let `E(a):=\{5\}` if `a\in\{1,3,4,5\}`,
and `E(2):=\{5,11\}`. For every prime `q\ge7` with `q\notin E(a)` (and
`q\ne3`, automatic since `q\ge7`), the sequence with `a_1=3^a q` satisfies,
literally from `n=1`:
`a_n = 3^a q + 3(n-1)` for every `n\ge1`,
i.e. the problem's conclusion holds with `T=1, L=3` from the very first term.

**Proof.** By strong induction on `n`, using Parts 1–2 above: the base case is
(0); the inductive step shows `a_n+1,a_n+2` illegal and `a_n+3` legal, by (1),
(3''), and, for `a_n+2`: Case (a) by (3); Case (b) odd `n` by (4); Case (b)
even `n` by the case-split of (9) (Legendre Sieve Gap Bound directly, or the
explicit residual-range witness search), valid precisely because
`q\notin E(a)$ rules out the sole genuine failure (the `a=2,q=11` instance
found in (9), and the general `q=5` failure found in (10) — both already
excluded from the prime range `q\ge7,\ q\notin E(a)`). Since `a_n+1,a_n+2`
illegal and `a_n+3` legal, minimality of the greedy rule forces
`a_{n+1}=a_n+3`, completing `H(n+1)`. `\blacksquare`

**Verification of the answer.** `T=1,L=3` is exactly the closed form
`a_n=3^a q+3(n-1)`; `n=1` recovers `a_1=3^a q`, matching the definition.
Independently re-simulated (own script): for `a=1,\dots,5`, every prime
`q\in[7,200)` except `q=11$ at `a=2`, 40 terms each (`214` sequences,
`8560` checked terms): **zero mismatches**. For `a=2,q=11`: directly
simulated and confirmed `a_5=110\ne111=3^2\cdot11+3\cdot4$, exactly matching
the mechanism-level proof in (9).

### Open gap for general `a` (honest scope limit)

The architecture of Parts 1–2 (steps (0)–(8), the case split of (9), and the
`q=5` exclusion of (10)) is **fully general, valid for every fixed `a\ge1`**
— nothing in the derivation assumed `a\le5`. What is **not** established for
`a\ge6` is the explicit, hand-verified residual-range computation of (9):
for each new `a`, one must (i) compute `K_0^{\max}(a)=3^a+2`, (ii) find
`s_1(a)$ by the same finite search (guaranteed to terminate by the
elementary asymptotic argument in (9)), (iii) enumerate the finite residual
range `k<k_{\mathrm{thresh}}(a)$ and, for each, the finitely many admissible
primes below the corresponding `q_{\mathrm{thresh}}(k,a)`, and (iv) verify by
direct search that each has a genuine witness (or record it as a new
exception, as happened once for `a=2`). This is an **effective procedure**
(guaranteed to terminate and settle the question for any given `a`), so the
theorem is not conjectural for larger `a` in the sense of lacking a proof
strategy — but it has only actually been **carried out and hand/computer-
verified through `a=5`** in this round. A future round wishing to claim the
theorem for, say, `a=6,\dots,10` need only repeat step (9)'s finite
computation for those values; no new ideas are anticipated to be needed
(the growth rate of `K_0^{\max}(a)=3^a+2` versus the doubly-exponential
factorial bound in (8) guarantees `s_1(a)` grows very slowly, keeping the
residual range from exploding), but this has not been done and should not be
assumed solved without doing it.

## Promotable lemmas

**Generalized Primorial Floor Corollary** (Part (8) above): for any constant
`C\ge0` and any `s_1\ge1` with `(s_1+1)!\ge\frac37 2^{s_1+1}(s_1+2)+C`, the
inequality `(s+1)!\ge\frac37 2^{s+1}(s+2)+C` holds for every `s\ge s_1`.
Proved in full above (a direct generalization of the certified Primorial
Floor Bound's Corollary, whose induction step never used the specific
constant `5`). Reusable by any future subfamily proof needing the same
factorial-vs-exponential comparison with a different (possibly large)
additive constant — e.g. a future attempt at `a_1=3^a q^m` combining both
generalization axes would need exactly this generalized form.

**`q=5` uniform exclusion parity argument** (Part (10) above): for the whole
family `a_1=3^a q`, any `a\ge1`, `q=5` fails at the unique `k=0` window
candidate because `K_0(a)=3^a+1` and the sole candidate `m_2=5\cdot3^{a-1}+1`
are BOTH always even (since `3^a`, `3^{a-1}` are odd for every `a\ge1`) — a
clean, reusable mechanism for excluding `q=5` from any `a_1=c\cdot q` family
where `c` is an odd constant `\equiv2\pmod3$-adjacent branch has `K_0` even.
