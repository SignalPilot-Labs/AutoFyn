# Approach: anomaly-count-terminates

## Status
unsolved — **the approach as framed is refuted by a concrete counterexample**
(`a_1 = 375`). The two load-bearing claims (confinement `p|L ⇒ p ≤ M`, and
finiteness of `>M` sole-witness "anomalies") are FALSE. The free lemmas and the
finite-state *reduction shape* survive and are proved below; the crux must be
re-planned with a finite structural-prime set `S` that is **not** bounded by `M`.

## Approaches tried
- **Round 1 (build): M-threshold anomaly framing — REFUTED.** Simulated the greedy
  process and the anomaly count with the intended threshold `M = ∏ primes(a_1)` over
  all seeds `a_1 ∈ {2,…,700}` and several 3-prime seeds. Found `a_1 = 375`
  (`P={3,5}`, `M=15`) where a prime `q = 19 > M` is a **sole witness at a
  hand-checkable step** and, from a 4000-term computation, `19 | L`. This kills
  confinement and anomaly-finiteness (details in **Refutation** below). Recorded so
  no one retries the `≤ M` cutoff.
- Free lemmas (Anchor, Gap bound, Distance–prime) — **proved in full**, still valid.
- General finite-state reduction (finite modulus ⇒ eventual periodicity, injectivity
  ⇒ pure period from the modulus onward) — **proved in full**, valid but its
  hypothesis (finite `S`) is the open crux and is NOT `S ⊆ {p ≤ M}`.

## Current best

### Free lemmas (all proved)

Notation. For a term `a_i`, write `F_i := primes(a_i)`. A positive integer `c` is
*admissible at stage `n`* iff `gcd(c, a_i) > 1` for every `i ≤ n`, equivalently iff
`c` shares a prime with every `F_i`, `i ≤ n`. Then `a_{n+1} = min{ c > a_n : c
admissible at stage n }`. Put `P := primes(a_1)` and `M := ∏_{p∈P} p = rad(a_1)`
(so `M | a_1`, hence `M ≤ a_1`).

**Lemma 1 (Anchor).** Every term has a prime factor in `P`.
*Proof.* For `m ≥ 2`, the defining condition at index `i = 1` gives
`gcd(a_m, a_1) > 1`, so `a_m` and `a_1` share a prime, which lies in `P`. And `a_1`
itself is a product of primes of `P`. ∎

**Lemma 2 (Gap bound; linear growth).** `a_{n+1} − a_n ≤ M` for all `n`; hence
`a_1 + (n−1) ≤ a_n ≤ a_1 + (n−1)M`, i.e. `a_n = Θ(n)`.
*Proof.* Let `c` be the least multiple of `M` with `c > a_n`; then
`a_n < c ≤ a_n + M`. For each `i ≤ n`, Lemma 1 gives a prime `p ∈ P` with `p | a_i`;
also `p | M | c`, so `gcd(c, a_i) ≥ p > 1`. Thus `c` is admissible at stage `n`, so
`a_{n+1} ≤ c ≤ a_n + M`. The lower bound is `a_{n+1} > a_n` (strictly increasing). ∎

**Lemma 3 (Distance–prime).** If a prime `q` divides `a_i` and `a_j` with `i ≠ j`,
then `q | (a_i − a_j)`, so `q ≤ |a_i − a_j|`.
*Proof.* `q | a_i` and `q | a_j` ⇒ `q | (a_i − a_j)`; and `a_i − a_j ≠ 0` since terms
are distinct, so `q ≤ |a_i − a_j|`. ∎

### General reduction (proved; hypothesis is the open crux)

**Reduction Lemma.** Suppose there exist a finite set `S` of primes, with
`K := ∏_{p∈S} p`, a fixed nonempty set of residues `U ⊆ Z/KZ`, and an index `N₀`
such that: for every `n ≥ N₀` and every integer `c` with `a_n < c ≤ a_n + M`,
```
c is admissible at stage n  ⟺  (c mod K) ∈ U .
```
Then there exist `T, L` with `a_{n+T} = a_n + L` for all `n ≥ N₀`.

*Proof.* Fix `n ≥ N₀`. By Lemma 2 the successor `a_{n+1}` lies in `(a_n, a_n + M]`,
so by hypothesis `a_{n+1}` is the least `c > a_n` with `(c mod K) ∈ U`. This value,
and in particular the gap `a_{n+1} − a_n`, depends only on the residue `a_n mod K`
(it is the cyclic distance from `a_n mod K` to the next element of `U`). Hence the
residue sequence `r_n := a_n mod K` (`n ≥ N₀`) obeys `r_{n+1} = h(r_n)` for the
fixed map `h : U → U`, `h(r) = ` "the next `U`-residue strictly after `r`" (well
defined and `U`-valued because `a_{n+1}` is admissible, so `r_{n+1} ∈ U`; and
`r_{N₀+1},… ∈ U`).

`h` is the **cyclic-successor map** on the finite cyclically-ordered set `U`, hence a
bijection of `U`: if `h(r_1) = h(r_2) = s` with `r_1 ≠ r_2` in `U`, then one of
`r_1, r_2` — say `r_2` — lies strictly between `r_1` and `s` on the cycle, so
`r_2 ∈ U` would be a `U`-residue between `r_1` and its next `U`-residue `s`,
contradiction. A bijection of a finite set has every orbit a cycle, so
`(r_n)_{n≥N₀}` is **purely periodic**: with `T := |orbit of r_{N₀}|` we get
`r_{n+T} = r_n` for all `n ≥ N₀`.

Now `a_{n+T} − a_n ≡ r_{n+T} − r_n ≡ 0 (mod K)`, so `a_{n+T} − a_n` is a multiple of
`K` for every `n ≥ N₀`. Consider `D_n := a_{n+T} − a_n > 0`. Telescoping the gap
formula and using periodicity of residues, `D_{n+1} − D_n = (a_{n+1+T} − a_{n+1}) −
(a_{n+T} − a_n) = g(r_{n+T}) − g(r_n)` where `g(r)` is the (residue-determined) gap;
since `r_{n+T} = r_n`, this is `0`. Hence `D_n` is constant `= L` for `n ≥ N₀`, and
`a_{n+T} = a_n + L` for all `n ≥ N₀`. ∎

**Remark (finite-state pigeonhole, unconditional half).** Even without the full
"⟺ `U`" hypothesis, the *set of distinct small-support types* `{F_i ∩ {p≤M}}` is a
monotone-increasing family of nonempty subsets of the finite set `{p ≤ M}` (nonempty
by Lemma 1), so it stabilises after some `N₁` (a subset of a finite power set can
increase only finitely often). This is the part the reviewer called "automatic." It
does **not** by itself yield the `U`-hypothesis, because a stabilised small support
`{p≤M}∩F_i` can still be met by an admissible `c` through a **large** prime rather
than through a small one (this is exactly what the counterexample exploits).

### Refutation of the M-threshold framing (the load-bearing failure)

**Counterexample.** Take `a_1 = 375 = 3·5³`. Then `P = {3,5}`, `M = 15`. The greedy
sequence begins
```
375, 378, 380, 384, 390, 396, 399, 402, …
```
with `380 = 2²·5·19`, `396 = 2²·3²·11`, `399 = 3·7·19`, `400 = 2⁴·5²` (all
verifiable by hand).

*(i) An anomaly with a `> M` sole witness genuinely occurs.* At `n = 6`
(`a_6 = 396`), the successor is `a_7 = 399`. The term `a_3 = 380 = 2²·5·19` has
small support `{2,5}`. But `399` is odd and `5 ∤ 399`, so `399` shares with `380`
**only** the prime `19`, and `19 > M = 15`. The value predicted using only
`≤ M`-witnessable constraints is `400` (`= 2⁴·5²`, which meets `380` via `2,5`); the
greedy successor `399 < 400` **because** the large prime `19` is a sole witness. So
"`>M` sole-witness steps" (anomalies) are **not absent** — the reviewer's simulated
"0 anomalies on every seed" simply missed this rare seed.

*(ii) Confinement `p|L ⇒ p ≤ M` is FALSE.* Direct computation of 4000 terms shows
the sequence is periodic with `(T, L) = (852, 3990)`,
`3990 = 2·3·5·7·19`, and `a_{n+852} = a_n + 3990` holds on the entire computed range
(several full periods). Thus `19 | L` while `19 = 19 > 15 = M`. The prime `19`
divides 60 of the 852 terms per period and recurs as a sole witness every period, so
the number of `>M` anomalies is **infinite** (positive density ≈ 60/852).

*(iii) The "rigidity" upgrade is invalid.* The outline argued: a persistent
sole-witness `q` would satisfy `q | a_n` and `q | a_{n+T} = a_n + L`, forcing `q | L`
hence `q ≤ M`, a contradiction. The counterexample shows `q = 19` **does** divide
`L`, and `q | L` is *not* a contradiction — it is precisely the stable state. The
inference `q|L ⇒ q ≤ M` was the (false) confinement lemma smuggled back in. So the
mechanism intended to turn density-0 into finiteness does not exist; anomalies are
genuinely infinite here.

**Conclusion of the refutation.** The theorem's conclusion (periodicity) still holds
for `375`, so the *result* is fine; what fails is this approach's route. The correct
structural-prime set is `S = primes(L)` (here `{2,3,5,7,19}`), a **finite** set, but
it is **not** contained in `{p ≤ M}`. Any framing that thresholds "large" at
`M = ∏ primes(a_1)` — and in particular any use of the confinement lemma — is dead.

### What the crux really is (sharp gap statement)

The surviving target is exactly the hypothesis of the Reduction Lemma:

> **CRUX (corrected).** There is a **finite** set of primes `S` (necessarily
> `⊇ primes(L)`) and an index `N₀` such that for all `n ≥ N₀`, admissibility of
> candidates in `(a_n, a_n + M]` is decided by residue mod `K = ∏_{p∈S} p`.

Two independent sub-gaps, neither bounded by `M`:
- **GAP-A (finite alphabet).** Only finitely many distinct primes ever appear in a
  `⊆`-minimal support that is not eventually dominated — i.e. `primes(L)` is finite.
  The counterexample shows these can exceed `M` (19), so the finiteness must come
  from a mechanism other than "≤ M." *This is the same crux as
  `redundant-constraint-antichain`'s Crux Lemma 1; the two approaches collapse onto
  it once the `M`-threshold is discarded.*
- **GAP-B (constraint stabilisation + no residual large shortcuts).** For `n ≥ N₀`,
  every constraint `F_i` (including those met via a large prime of `S`) is captured
  by the fixed condition "residue mod `K ∈ U`," so no *new* large prime outside `S`
  ever becomes a sole witness after `N₀`. Equivalently: the large sole-witnesses that
  persist all lie in the finite set `S` and repeat periodically.

The reduction to periodicity from these is the proved Reduction Lemma. Extending the
period from `n ≥ N₀` down to `n = 1` (the problem demands `∀ n ≥ 1`) is a separate,
standard-but-nontrivial backward-determinism step, not attempted here.

## Full proof
Not present — Status is unsolved; the approach's crux is refuted as framed and the
corrected crux (GAP-A / GAP-B) is open.

## Promotable lemmas
- **Anchor** (Lemma 1): every term has a prime factor in `P = primes(a_1)`.
  Proved in full above. Reusable by all approaches.
- **Gap bound / linear growth** (Lemma 2): `a_{n+1} − a_n ≤ M := rad(a_1)`,
  `a_n = Θ(n)`. Proved in full above.
- **Distance–prime** (Lemma 3): shared prime `q | a_i, a_j` ⇒ `q ≤ |a_i − a_j|`.
  Proved in full above.
- **Reduction Lemma** (finite fixed modulus `K` + fixed admissible residue set `U`
  ⇒ periodicity for `n ≥ N₀`, via the cyclic-successor bijection on `U`). Proved in
  full above; framing-agnostic, reusable.
- **NEGATIVE result (promote as a recorded refutation, not a lemma):**
  Confinement "`p | L ⇒ p ≤ M`" is **false** (`a_1 = 375`: `19 | L = 3990`,
  `M = 15`). Both surviving approaches must drop any `M`-threshold on structural
  primes.
