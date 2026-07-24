## Lemmas: `a_1=3^a q` Toolkit — Generalized Primorial Floor Corollary,
Corrected Witness Identity, and `q=5` Uniform Exclusion (CERTIFIED, round 24)

**Source.** `a1-3aq-subfamily-theorem`, round 24. Independently re-verified
in full by the round-24 proof-reviewer, including an independent exhaustive
computational re-derivation of the entire residual-band closure (own
`sympy`/direct script, not merely re-reading the builder's algebra).

**Depends on (certified).** `lemmas/primorial-floor-bound.md`,
`lemmas/legendre-sieve-gap-bound.md`.

### 1. Generalized Primorial Floor Corollary

**Statement.** Fix `C≥0` and let `s_1≥1` be any integer with
`(s_1+1)! ≥ (3/7)·2^{s_1+1}(s_1+2)+C`. Then `(s+1)! ≥ (3/7)·2^{s+1}(s+2)+C`
for every `s≥s_1`.

**Proof.** Induction on `s≥s_1`, identical in structure to the certified
Primorial Floor Bound's corollary (base case `5`), with the constant `C`
carried through unchanged: the inductive step never used the specific value
`5`, only that `(s+2)^2≥2(s+3)` for `s≥1` and `C(s+2)≥C`. Re-derived and
confirmed correct by this review.

### 2. Corrected witness identity for `a_1=3^a q`, general `a≥1`

**Statement.** For `a_1=3^a q` (`a≥1`, `q` prime, `q≥7,q≠3`), writing
`a_i/3 = 3^{a-1}q+(i-1)` for `i≤n` under the induction hypothesis
`H(n): a_i=3^a q+3(i-1)`, the correct sieve window for a Case-(b) index
`n=n_0+kq` is `{cq+1,...,cq+(n-1)}` with `c:=3^{a-1}` — **not**
`{q+1,...,q+(n-1)}` (the naive transplant of the `a=1` window, which is
wrong for `a≥2` and can silently produce a false witness, e.g. at `a=2,q=11,
k=0`: the naive window gives `i=3⟹m_3=13`, `gcd(13,10)=1`, a FALSE witness,
since the true window is `{34,35,36}` at `c=3`, none coprime to `K_0=10`).

**Independent verification.** Re-derived the algebra
`a_n+2=q(3^a+s_0+3k)=q(K_0(a)+3k)` and the reduction
`gcd(N,a_i)=gcd(qK, cq+(i-1))` from scratch; confirmed the naive-window
false-witness claim directly by computation
(`gcd(13,10)=1` while the true candidates `{34,35,36}` all share a factor
with `K_0=10`).

### 3. `q=5` uniform exclusion parity mechanism

**Statement.** For every `a≥1`, `a_1=3^a·5` fails literal `T=1,L=3`
periodicity: at `k=0`, the unique window candidate `m_2=5·3^{a-1}+1` and
`K_0(a)=3^a+1` are both always even (since `3^a,3^{a-1}` are odd for
`a≥1`), so no witness exists, breaking the induction at `n=3`.

**Independent verification.** Re-derived the parity argument from scratch
(odd+1=even, odd·odd=odd, odd+1=even) and confirmed by direct simulation
for `a=1,...,5` that the sequence genuinely deviates from the conjectured
closed form starting at `n=3` in every case (e.g. `a=1`: `a_3=20≠21`;
`a=2`: `a_3=50≠51`).

### 4. Residual-band closure (`a=1,...,5`), independent re-derivation

This review independently and exhaustively re-ran the entire residual-band
sieve-bound check (own script, not reusing the builder's) for
`a=1,...,5`, `k<k_thresh(a)` (`k_thresh(1,2,3)=12`, `k_thresh(4,5)=28`, all
independently recomputed and matching the builder's table exactly), across
both branches `K_0(a)∈{3^a+1,3^a+2}` and primes `q<2000`: found exactly **86**
instances where the crude Legendre bound fails, and for every one of them
searched exhaustively for a genuine witness `i` — **exactly one** instance
has no witness: `a=2, K_0=10 (q≡2 mod 3), k=0, q=11` — matching the
builder's sole flagged exception exactly, digit for digit.

**Status.** All four items correct, complete, unconditional, independently
re-verified from scratch by fresh computation. Reusable by any future
subfamily proof needing the same factorial-vs-exponential comparison with a
different additive constant (e.g. `a_1=3^a q^m` combining both
generalization axes), the corrected witness-window identity for
`a_1=c·q` families with `c` a higher power of a core prime, or the `q=5`
parity-exclusion mechanism for `a_1=c·q` families with `c` odd.
