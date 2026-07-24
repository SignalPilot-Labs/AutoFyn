# Scouting report: is there a genuine Jacobsthal-type tool for a1-3q Case (b), n even, k>=1?

## 1. The exact gap, restated precisely

From `results/imo-2026-06/approaches/a1-3q-subfamily-theorem.md` (items (5) and
"OPEN GAP"): fix prime `q>=7, q!=5`, `a_1=3q`. At a Case-(b) index `n = n_0+kq`
(`k>=1`, `n` even), write `N := a_n+2 = qK` with `K = K_0+3k` (`K_0 in {4,5}`
fixed by `q mod 3`). The candidate witnesses are `i=2,...,n`, giving
`m := q+i-1` ranging over the window `q+1,...,q+n-1` (length `n-1`). Since
`gcd(N,a_i)=gcd(N,3m)=gcd(N,m)` (as `3∤N`), and `N=qK`, we need some `m` in
the window with `gcd(m,qK)=1`. The window length `n-1` is *provably* `>= K`
(proved unconditionally in the file, item (5) last bullet) — but it is
**not** provably `>= rad(qK)`, which is what a literal "any `d` consecutive
integers contain `phi(d)` coprime-to-`d` ones, so a full period suffices"
pigeonhole would need. The gap is exactly: **does a window of length `~n-1`
(known to be `>= K` but not `>= rad(qK)`) always contain an integer coprime
to `qK`?** This is a gap-between-coprime-residues question — i.e. a
Jacobsthal-function-shaped question for the modulus `qK`, restricted to a
window starting at `q+1`.

## 2. Search of knowledge_base.md and the crux corpus

- `knowledge_base.md`: **no** hits for "Jacobsthal", "primorial", "smooth
  number", "rough number", "covering congruence", or any generic
  gap-between-coprimes theorem. The KB's gcd/pigeonhole material is all
  elementary single-window "any `d` consecutive integers contain `phi(d)`
  coprime residues" style, i.e. exactly the naive bound already shown
  insufficient here.
- Crux corpus (`past_crux_moves_database.json`, 2434 cruxes): **zero** hits
  for "Jacobsthal" anywhere. Closest matches by keyword (`coprime to`,
  `consecutive integers`, `window of length`, `gap between`):
  - `aimo-0144` (modular-arithmetic-and-CRT / size-bounding-and-descent):
    "any window of `d` consecutive integers contains exactly `phi(d)`
    coprime-to-`d` integers" — this is precisely the naive bound already
    proved too weak in the approach file. Not new.
  - `aimo-0511` (p-adic-valuation): bounds the number of distinct
    `p`-adic valuations in an AP via a "unique maximal-valuation term"
    argument — a genuinely different flavor of gap argument (not
    Jacobsthal), doesn't transfer.
  - `aimo-0577` (size-bounding-and-descent): "any `a` successive values
    `x,x+d,...,x+(a-1)d` with `gcd(a,d)=1` form a complete residue system
    mod `a`, so exactly one is divisible by `a`" — again the naive
    full-period pigeonhole, not a sharper gap bound.
  - `aimo-0421`: pigeonhole on gcd values taking finitely many values —
    unrelated (different problem shape).
  - No crux in the corpus addresses multi-prime-modulus gap bounds sharper
    than the single-window pigeonhole. **Conclusion: neither retrieval
    resource contains a Jacobsthal-type tool, off the shelf.**

## 3. Numeric test: is Jacobsthal's actual gap size small enough to matter, and is there an elementary bound that could substitute?

I computed the true Jacobsthal function `g(n)` (max gap between consecutive
integers coprime to `n`, over one full period) exactly, by direct sieve, for
`n` = primorial(k) (the worst-case-for-its-size modulus, product of the
first `k` primes — the extremal case for a given number of distinct prime
factors `omega(n)=k`):

```
omega=1  n=2         g(n)=2    2^(omega+1)=4
omega=2  n=6         g(n)=4    2^(omega+1)=8
omega=3  n=30        g(n)=6    2^(omega+1)=16
omega=4  n=210       g(n)=10   2^(omega+1)=32
omega=5  n=2310      g(n)=14   2^(omega+1)=64
omega=6  n=30030     g(n)=22   2^(omega+1)=128
omega=7  n=510510    g(n)=26   2^(omega+1)=256
omega=8  n=9699690   g(n)=34   2^(omega+1)=512
```

(These match the known OEIS A048670 values, confirming the sieve is
correct.) Two things fall out of this:

- **The true gap function is dramatically smaller than the modulus itself**
  (`g(n) ~ O(omega(n))` empirically in this range, definitely
  `o(n)` and even `o(rad(n))`) — consistent with the file's own finding
  that a witness at `i=9` was found against a modulus with `rad ~
  1.16e13`. This is real, correct, and explains the phenomenon: the naive
  "window `>= rad(qK)`" requirement is enormously pessimistic; the true
  requirement is only "window `>= g(qK)`", and `g(qK)` grows only like
  (conjecturally/provably) `omega(qK)^2 (log omega(qK))^2` or better
  (Iwaniec's unconditional bound), i.e. **doubly-logarithmically slowly**
  in `qK`.
- **There is a genuinely elementary (non-Iwaniec) weaker bound available**:
  `g(n) <= 2^{omega(n)}` (or `2^{omega(n)+1}`, depending on the exact
  convention/off-by-one), provable by a simple induction on the number of
  distinct prime factors — each new prime `p` added to the modulus can at
  most double the worst-case gap (standard elementary sieve/CRT induction:
  splitting a gap-free window in two using divisibility by the new prime).
  This is "olympiad-legal" (no analytic number theory, just induction +
  CRT), unlike Iwaniec's sharper `O(omega^2 log^2 omega)` bound which
  needs genuine sieve theory (Selberg sieve / large-sieve-type input) and
  is **not** something a from-scratch proof in this project could invoke
  without proving it first (a project unto itself, well beyond "name your
  tools" — it is a deep, non-elementary theorem).

## 4. Does the elementary `2^{omega(n)}` bound actually suffice here?

Tested against the specific structural constraints of this problem: window
length is `n-1 = n_0-1+kq`, growing **linearly in `k` with slope `q`**,
while `K = K_0+3k` grows linearly in `k` with slope `3`, so `omega(qK) =
omega(K)` (as `gcd(q,K)` — not generally 1, but `omega` grows at most like
`omega(K) <= C log(K)/log log(K)` for any integer, by the standard
"smallest number with `omega` prime factors is the primorial" argument).
Concretely: even the crude bound `2^{omega(K)}` grows **only
sub-polynomially** in `k` (since `omega(K) = O(log k / log log k)`, so
`2^{omega(K)} = k^{o(1)}`), while the window grows **linearly** in `k`
(`~qk`). So for every fixed `q`, there is some threshold `k^*(q)` beyond
which `window(k) = n_0-1+kq` provably exceeds `2^{omega(K(k))}` for all
`k>=k^*(q)` — i.e. **the elementary bound closes the case for all
sufficiently large `k`,automatically, no adversarial construction can beat
it asymptotically.** I did NOT verify computationally that `k^*(q)` is
small enough to make the *finitely many remaining small-`k` cases*
checkable by hand for a general `q` (this would need, for each `q`, an
explicit finite check of `k=1,...,k^*(q)-1`, and `k^*(q)` was not computed
here) — this is the residual work, not something I attempted (out of
scope: "scout, don't prove").

## 5. Verdict

- **No off-the-shelf Jacobsthal-function statement or crux exists in either
  retrieval resource** — the KB and crux corpus only contain the naive
  single-window pigeonhole (`aimo-0144`, `aimo-0577` style), already known
  insufficient.
- **A genuinely elementary substitute exists and is plausible-adaptable**:
  the crude bound `g(n) <= 2^{omega(n)}`, provable by elementary
  induction/CRT (no deep sieve theory needed), combined with the fact that
  `omega(K)` can grow only like `O(log k/loglog k)` while the available
  window grows linearly in `k` — this gives an asymptotic-in-`k` argument
  that plausibly closes "Case (b), n even, k>=1" for all `k` past some
  finite (per-`q`) threshold, reducing the open gap to a **finite check**
  for each `q` (not yet carried out).
- **The sharper Iwaniec-type bound (`O(omega^2 log^2 omega)`)** that
  actually explains the very small observed witness (`i=9` against
  `omega=11`) is a genuine deep theorem (sieve-theoretic), not provable
  from scratch within olympiad/project scope, and should NOT be invoked as
  a "named tool" per the project's rigor rules — only the crude
  `2^{omega(n)}` elementary bound is legitimately available to a builder.
- **Recommendation for next round's outliner/builder**: attempt to (a)
  prove the elementary `g(n)<=2^{omega(n)}` bound from scratch (short
  induction, should be a clean lemma), (b) make the "`window(k) >
  2^{omega(K(k))}` for `k>=k^*(q)`" comparison rigorous and explicit in `q`
  (bounding `omega(K)` via `K <= K_0+3k` and the standard "least integer
  with `r` prime factors is `>= primorial(r)`" fact), and (c) explicitly
  check the finitely many remaining small `k` for each residue class of
  `q mod 3` (may need `q`-uniform reasoning or an additional trick,
  since `k^*(q)` could depend on `q`). This looks tractable — a real
  candidate to close the file's final gap — but was not attempted here
  (scouting only, per assignment).

## Numeric evidence files
All computation was done inline in this session; no external files were
written besides this report.
