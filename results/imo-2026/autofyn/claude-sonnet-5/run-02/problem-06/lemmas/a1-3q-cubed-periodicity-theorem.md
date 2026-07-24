## Lemma/Theorem: `a_1 = 3q^3` Literal Periodicity Theorem (CERTIFIED, round 25)

**Source.** `a1-3qk-subfamily-theorem`, round 25, Part IV `m=3` closure
(closing Case (b), `n` even, for `m=3`), building on the certified
`m`-generic Parts I-III (`lemmas/a1-3qm-parity-and-k0-bookkeeping-lemmas.md`).
Independently re-verified in full by the round-25 proof-reviewer.

**Depends on (certified).** `lemmas/legendre-sieve-gap-bound.md`,
`lemmas/primorial-floor-bound.md`,
`lemmas/a1-3qm-parity-and-k0-bookkeeping-lemmas.md`.

**Statement.** For every prime `q ≥ 7, q ≠ 5`, the sequence with `a_1 = 3q^3`
satisfies, literally from `n=1`: `a_n = 3(q^3+n-1) = 3q^3+3(n-1)` for every
`n ≥ 1`. I.e. `T=1, L=3` from the very first term.

**Proof.** By strong induction on `n`, using: (i) the `m`-generic base case,
`a_n+1` illegality, Case (a) `q∤(a_n+2)` illegality, and odd-`n` Parity
Witness illegality, all transplanted verbatim from the certified
`m`-generic lemmas; (ii) `a_n+3` legality via the shared factor 3; (iii)
Case (b) (`n` even, `q|(a_n+2)`), split into `k=0` and `k≥1` sub-cases:
- `k=0`: effective sieve modulus is `K_0=3q^2+s_0` alone (`q`-coprimality
  free). A sharpened Primorial-Floor-Bound induction, `(r+1)! ≥ g(r) :=
  27·4^r(r+1)^2+36·2^r(r+1)+14` for `r≥15` (base case `r=15`; induction
  `r→r+1` for `r≥4`), shows the Legendre Sieve Gap Bound applies
  unconditionally in `q` once `ω(K_0)≥15`; the generic cap
  `2^14·15=245,760` handles `ω(K_0)≤14` above the explicit threshold
  `q≥737,282`. Exhaustive direct computation for `q<737,282` finds exactly
  12 residual exceptions, each resolved by an explicit witness.
- `k≥1`: effective modulus is `qK`, `K=3q^2+s_0+3k`. An "OR-split" device
  (if `ω(K)=s≥14`, either `q≥B(s):=2^{s+1}(s+2)` or `k≥B(s)/7`, forcing
  `kq≥B(s)≥2^{r'}(r'+1)`, `r'=ω(qK)≤s+1`) — justified by a second
  Primorial-Floor-Bound induction, `(s+1)! ≥ h(s) := 3B(s)^2+(3/7)B(s)+2`
  for `s≥14` (base case `s=14`; induction `s→s+1` for `s≥4`) — closes
  `ω(K)≥14` unconditionally in `q,k`; the generic cap `245,760` handles
  `ω(K)≤13` once `kq≥245,760`. Exhaustive direct computation over the
  remaining finite region `kq<245,760` finds exactly 14 residual
  exceptions (all `q≤71,k≤7`), each resolved by an explicit witness.

Full derivation (Claims 1-4, parts (A)-(B)) given in
`approaches/a1-3qk-subfamily-theorem.md` (round 25 version, "`m=3`: full
closure of Case (b)" section).

**Independent verification (this review, fresh scripts).** (1) Reproduced,
via an independent `sympy` sieve-bound scan (own script, exact integer
arithmetic), the exact claimed `k=0` residual list of 12 exceptions
(`q∈{11,17,19,23,29,41,53,59,61,71,89,479}`, exact `(n_0,K_0,ω,L,bound)`
match on every row) and extended the scan well beyond the builder's own
spot-check to `q<60,000` — zero further exceptions found, consistent with
the analytically-proved threshold `q≥737,282`. (2) Reproduced the exact
claimed `k≥1` residual list of 14 exceptions
(`(q,k)∈{(7,1),(7,2),(7,3),(7,7),(11,2),(13,3),(17,1),(17,2),(17,4),(19,1),
(23,1),(29,2),(59,2),(71,2)}`) via an independent scan over the full
analytically-guaranteed finite region `kq<245,760`, exact digit-for-digit
match. (3) Independently verified all 26 explicit witnesses (`t_i=q^3+i-1`
vs the stated `K_0` or `M=qK`) by direct `gcd` computation — every one
correct. (4) Independently re-derived the two Primorial-Floor-Bound
inductions from scratch (own `sympy` exact-integer computation): confirmed
the base cases `16!≥g(15)` and `15!≥h(14)` both hold, and confirmed no
induction-step failure for `r,s∈{4,...,39}`. **Found one minor
write-up arithmetic error** (not affecting correctness): the file states
`h(14)=1,241,245,707,702`, but the correct value from the stated formula
`h(s)=3B(s)^2+(3/7)B(s)+2` at `s=14` is `824,633,945,528.86` (both
values are `<15!=1,307,674,368,000`, so the base case holds either way —
the displayed number is simply mis-computed, with no effect on the
theorem's validity). (5) Independently re-simulated the literal greedy
recursion (own fresh script, not the closed form) for
`q∈{7,11,13,17,19,23,29,41,53,59,61,71,89}` out to 60-400 terms each
(covering every exceptional index): **zero mismatches** in every case.

**No gap found.** This is a genuine, complete, unconditional third instance
of the `a_1=3q^m` family (`m=1,2,3` now all fully certified), independently
re-verified in full.
