## Lemmas: `m`-generalized Parity Witness and `n_0,K_0` Bookkeeping for
`a_1 = 3q^m` (CERTIFIED, round 23)

**Source.** `a1-3qk-subfamily-theorem`, round 23 build, Part I item (4) and
Part II. Independently re-derived and re-verified by the round-23
proof-reviewer.

**Setting.** `a_1 = 3q^m`, `q` an odd prime `q ≥ 7, q ≠ 5`, `m ≥ 1` a fixed
integer. Strong-induction hypothesis at step `n`: `a_i = 3(q^m+i-1)` for
`i = 1,…,n` (so `3 | a_i` and `P(a_1) = {3,q}` for every such `i`, any `m`).
This strictly generalizes the certified `a_1=3q` lemma pair
(`lemmas/a1-3q-parity-and-k0-window-lemmas.md`), which is exactly the `m=1`
case.

### Lemma 1 (`m`-generalized Parity Witness)

**Statement.** If `n` is odd, then `i = n` witnesses the illegality of
`a_n+2` (`gcd(a_n+2,a_n) = 1`), independent of whether `q | (a_n+2)` and
independent of `m`.

**Proof (reviewer's corrected derivation — the approach file's own write-up
contains a sign slip in one intermediate clause; the *statement* and final
conclusion are correct, re-derived cleanly here).** Set `N := a_n+2 =
3(q^m+n)-1`. Since `gcd(x,y)=gcd(x,x-y)`, `gcd(N,a_n) = gcd(N,N-a_n) =
gcd(N,2)`. As `3(q^m+n)` and `q^m+n` share parity, `N` is odd iff `q^m+n` is
even. Since `q` is an odd prime, `q^m` is odd for every `m ≥ 1` (an odd
number to any positive integer power is odd, by induction on the exponent:
`q^1` odd; if `q^{k}` odd then `q^{k+1}=q\cdot q^k` is odd·odd = odd).
Hence `q^m+n` is even iff `n` is **odd** (odd+odd=even, odd+even=odd) — so
`N` is odd iff `n` is odd. Therefore, for `n` odd, `N` is odd, `gcd(N,2)=1`,
so `gcd(N,a_n)=1`: illegal via `i=n`. ∎

(Numerically spot-checked: `q=7,m=1,n=1`: `N=3·8-1=23`, odd, `n` odd —
consistent; `n=2`: `N=26`, even, `n` even — consistent.)

### Lemma 2 (`m`-generalized `n_0, K_0` bookkeeping)

**Statement.** The first Case-(b) index `n_0` (least `n` with `q|(a_n+2)`,
equivalently `q|(3n-1)`, since `a_1 \equiv 0 \pmod q` for every `m \ge 1`)
satisfies the **same, `m`-independent** closed forms as the certified `m=1`
lemma: `n_0=(q+1)/3, s_0:=(3n_0-1)/q=1` if `q\equiv2\pmod3`; `n_0=(2q+1)/3,
s_0=2` if `q\equiv1\pmod3`. However the associated modulus
`K_0(q,m) := (a_{n_0}+2)/q` is **not** `m`-independent: writing
`a_n+2 = 3q^m+q(s_0+3k)` for `n=n_0+kq`, one gets
`K_0(q,m) = 3q^{m-1}+s_0`, so `K_0(q,m) \in \{4,5\}` exactly at `m=1`
(matching the certified `m=1` theorem) but `K_0(q,m) = \Theta(q^{m-1})`
(grows with `q`) for `m\ge2`.

**Proof.** The `n_0,s_0` formulas follow purely from `a_1\equiv0\pmod q`
(true for every `m\ge1`) exactly as in the certified `m=1` case (elementary
case split on `q \bmod 3`). For `K_0`: `3n-1 = 3n_0-1+3kq = qs_0+3kq`, so
`a_n+2 = 3q^m+3n-1 = 3q^m+q(s_0+3k) = q\bigl(3q^{m-1}+s_0+3k\bigr)`, giving
`K_0(q,m)+3k` with `K_0(q,m)=3q^{m-1}+s_0` as claimed. ∎

**Reviewer verification.** Independently re-derived both closed forms from
scratch; confirmed by direct computation the `m=1` reduction
(`q=7\Rightarrow(n_0,K_0)=(5,5)`; `q=11\Rightarrow(4,4)`, matching the
certified `m=1` theorem's own numbers) and spot-checked `K_0(q,m)` for
`m=2,3` against the formula across primes `q\in[7,200)` — exact match in
every case (`sympy`-verified).

**Status.** Both lemmas correct, complete, unconditional (within the stated
`a_1=3q^m` setting and inductive hypothesis). Neither closes the full
`a_1=3q^m` theorem (Case (b), `n` even, remains open for `m\ge2` — see
`approaches/a1-3qk-subfamily-theorem.md` and the round-23 proof-reviewer
report for why the approach file's own diagnosis of *why* it is open is
itself flawed and needs correction). Reusable self-contained tools for any
future round attacking `a_1=3q^m`-type or similarly-shaped seeds.
