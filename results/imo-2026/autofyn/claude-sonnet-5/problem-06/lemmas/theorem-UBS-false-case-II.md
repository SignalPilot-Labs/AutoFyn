# Theorem: `(UB_S)` is impossible for every proper core simultaneously, in
Case II (unconditional refutation of the round 4–8 target)

**Source.** `results/imo-2026-06/approaches/sunflower-bundle-closure.md`
(round 9, §6). Depends on: `lemmas/theorem-UBS-sufficiency.md` (the
`(UB_S)⟹` whole-problem chain, hence `(UB_S)⟹` exact periodicity via
Theorem 5.1/Lemma MS/Theorem V/Theorem CD-Lemma TC/Λ_S-Reduction Lemma, all
previously certified), `lemmas/lemma-1-uniform-gap-bound.md` (Growth Lemma,
`a_n≤a_1+(n-1)·rad(a_1)`, unconditional), Lemma P (`P_1⊆rad(a_n)` for all
`n`, round 1). No dependence on any of the round 8 Δ-system/pigeonhole
machinery beyond the already-certified sufficiency chain.

## Statement

**Case II** = no prime divides every `a_n` (equivalently `k:=|P_1|≥2`, since
`k=1` forces Case I by Lemma P). In Case II:

1. **Imprint Periodicity Lemma.** If `a_{n+T}=a_n+L` for every `n≥1` (exact
   periodicity, `T,L` fixed positive integers), then `n∈I_{P_1}`
   (`P_1⊆rad(a_n)`) is an exactly `τ`-periodic property of `n`, for a fixed
   `τ:=\mathrm{lcm}(τ_p:p∈P_1)` where `τ_p:=T` if `p∣L`, else `τ_p:=pT`.
   Consequently `I_{P_1}` has an exact density `|R|/τ` for a fixed
   `R⊆\{0,…,τ-1\}`.
2. **Corrected Density Sub-Lemma.** In Case II, under the same hypothesis
   (exact periodicity), `R≠\{0,…,τ-1\}` (else some `p_1∈P_1` would divide
   every `a_n`, contradicting Case II), hence there is a fixed `c=1/(2τ)>0`
   with `|I_{P_1}∩[1,N]|≤(1-c)N` for all `N≥2τ²`.
3. **Euler's classical divergence** (1737): `S(X):=Σ_{p≤X}1/p→∞`.
4. **Landau Count Lemma** (Turán's 1934 elementary second-moment proof):
   for fixed `k≥0`, `A_k(X):=|\{m≤X:ω(m)≤k\}|=o(X)`.
5. **Main Theorem.** In Case II, it is impossible for `(UB_S)` to hold for
   every proper nonempty core `S⊊P_1` simultaneously. Equivalently,
   `sup_{n∉I_{P_1}}ω(a_n)=∞` always in Case II.

## Proof

**(1) Imprint Periodicity Lemma.** Fix `r∈\{1,…,T\}`. By induction on `m`
using exact periodicity, `a_{r+mT}=a_r+mL` for every `m≥0` (`(†)`). Fix a
prime `p`. By `(†)`, `p∣a_{r+mT}⟺mL≡-a_r (mod p)`.
- If `p∣L`: the congruence reads `0≡-a_r (mod p)`, independent of `m` — so
  "`p∣a_{r+mT}`" holds for all `m` or none, determined by `r` alone, i.e.
  period `T` in `n`.
- If `p∤L`: `L` is invertible mod `p`, so exactly one residue `m_0(r) (mod
  p)` satisfies the congruence; "`p∣a_{r+mT}`" holds iff `m≡m_0(r) (mod
  p)`. Since replacing `m` by `m+p` preserves this (as `p≡0 mod p`), this
  gives period `pT` in `n`, uniformly over all `r` (i.e. not merely within
  one residue class mod `T`, but as a period of the whole property "`p∣a_n`"
  on `ℕ`).

Either way "`p∣a_n`" has period `τ_p` dividing `T` or `pT` as stated. Let
`τ:=\mathrm{lcm}(τ_p:p∈P_1)` (finite lcm of `k=|P_1|` values). The
conjunction `P_1⊆rad(a_n)` (i.e. `n∈I_{P_1}`) has period dividing `τ`,
giving the periodic characterization with `R:=\{(r-1)\bmod τ:r∈I_{P_1}\}`.
Standard periodic-density fact: `|I_{P_1}∩[1,N]|=|R|⌊N/τ⌋+O(τ)→` density
`|R|/τ`. **Independently verified** (proof-reviewer, round 9): the
mod-arithmetic step-by-step (periodicity of "`p∣a_n`" with the stated period
formula, both `p∣L` and `p∤L` sub-cases) reproduced exactly on a toy
periodic sequence (`T=3,L=30`) for `p∈\{2,3,5,7,11,13\}`.

**(2) Corrected Density Sub-Lemma.** If `R=\{0,…,τ-1\}` then every `n∈
I_{P_1}`, so any fixed `p_1∈P_1` (nonempty since `k≥1`) divides every `a_n`
— contradicting Case II. So `|R|≤τ-1`; a `τ`-periodic set with `≤τ-1`
populated residues per block of `τ` gives, for `N≥2τ²`,
`|I_{P_1}∩[1,N]|≤(1-1/τ)N+(τ-1)≤(1-c)N` with `c=1/(2τ)` (elementary
arithmetic, checked exactly).

**(3) Euler's divergence.** Standard elementary proof (smooth/rough-number
split): if `S(X)≤C` for all `X`, pick `r` with tail `Σ_{i>r}1/p_i<1/4`.
Every `n≤N` is either "rough" (has a prime factor `>p_r`, count `<N/4` by
the tail bound) or "`p_r`-smooth" (`n=p_1^{e_1}⋯p_r^{e_r}`, count
`≤(⌊log_2N⌋+1)^r=o(N)` for fixed `r`). Total `<N/2` for large `N`,
contradicting the exhaustive split summing to exactly `N`.

**(4) Landau Count Lemma (Turán 1934).** Using only `⌊y⌋≤y`, `⌊y⌋≥y-1`, and
elementary double-counting: `Σ_{m≤X}ω(m)=Σ_{p≤X}⌊X/p⌋` (mean identity) and
`Σ_{m≤X}ω(m)²=Σ_{p≤X}⌊X/p⌋+Σ_{p≠q≤X}⌊X/(pq)⌋≤XS(X)+XS(X)²` (second-moment
identity, ordered-pair count of common divisors). Combining gives
`Σ_{m≤X}(ω(m)-S(X))²≤3XS(X)`. For `m` with `ω(m)≤k` and `S(X)>k`,
`(ω(m)-S(X))²≥(S(X)-k)²`, so `A_k(X)(S(X)-k)²≤3XS(X)`. Taking `X` large
enough that `S(X)>2k` (possible by (3)) gives `A_k(X)≤12X/S(X)→o(X)` as
`X→∞`. **Independently verified** (proof-reviewer, round 9): the mean and
second-moment identities checked to hold *exactly* (not just
asymptotically) at `X=2000` by direct enumeration (`Σω(m)=4454=Σ⌊X/p⌋` and
`Σω(m)²=11104=Σ⌊X/p⌋+Σ_{p≠q}⌊X/(pq)⌋`, both exact matches); the derived
bound `(4)` checked to hold at `X=2×10⁶` for `k=1,2` (the only `k` with
`S(X)>k` reached at that `X`, since `S(X)` grows like `log log X`).

**(5) Main Theorem.** Suppose, toward a contradiction, `(UB_S)` holds for
every proper core `S⊊P_1` in Case II. By `theorem-UBS-sufficiency.md`, this
gives `B:=sup_{n∉I_{P_1}}ω(a_n)<∞` and (via the certified chain) exact
periodicity `a_{n+T}=a_n+L` for every `n≥1`. By (1)–(2), there is fixed
`c=1/(2τ)>0` with `|I_{P_1}^c∩[1,N]|≥cN` for `N≥2τ²`. By the Growth Lemma,
`a_n≤X_N:=a_1+(N-1)·rad(a_1)=O(N)` for `n≤N`. The `≥cN` values
`\{a_n:n∈I_{P_1}^c∩[1,N]\}` are pairwise distinct (strictly increasing
sequence), each `≤X_N`, each with `ω(a_n)≤B`; hence `A_B(X_N)≥cN`. But by
(4), `A_B(X_N)=o(X_N)=o(N)`. So `cN≤o(N)`, i.e. `c≤o(1)→0`, contradicting
`c` fixed and positive. Hence the standing assumption is false. `∎`

**Non-circularity note.** This is a standard proof by contradiction: the
assumption `(UB_S)`-for-every-`S` yields *two* consequences via already-
certified, one-directional implications (`B<∞` directly, and exact
periodicity `(⋆)` via the certified sufficiency chain) — it does not assume
the conclusion being disproved. The Density Sub-Lemma is derived *from*
`(⋆)` (itself a consequence of the standing assumption), not assumed
independently; combined with the *unconditional* Landau Count Lemma and
Growth Lemma, the two consequences of the standing assumption are shown
mutually inconsistent. No step uses `(UB_S)` to prove `(UB_S)` or its
negation directly.

## Scope

Refutes `(UB_S)` as a route to the whole problem (retires the round 4–8
`(UB_S)`/`(MRS)`/`𝓥_S`-finiteness-via-companion-bundle-size program
unconditionally, for every `a_1` in Case II). Does **not** refute FCBC
(strictly weaker, per the already-certified Lemma W1 — FCBC only needs a
fixed prime set to hit every pair, not a bundle-size bound) nor resolve the
whole problem.

## Independent re-verification (proof-reviewer, round 9)

- Re-derived the Imprint Periodicity Lemma's mod-`p` case split by hand and
  confirmed it on a toy periodic sequence (own Python, `T=3,L=30`, 6 primes
  tested, all periods matched the formula exactly).
- Re-derived and exactly numerically checked the mean and second-moment
  identities underlying the Landau Count Lemma (`X=2000`, exact match to
  the integer) and the derived Chebyshev-type bound `(4)` (`X=2×10⁶`,
  `k=1,2`, bound held).
- Re-checked the Corollary's arithmetic (`c=1/(2τ)`, threshold `N≥2τ²`) by
  hand, exact match.
- Confirmed no circularity: the argument derives two consequences of one
  hypothesis and shows they conflict, using only previously-certified
  one-directional implications plus two independent classical facts proved
  from scratch this round.
- Found no gap. Certified `solved`-quality (self-contained modulo the
  already-certified `theorem-UBS-sufficiency.md` chain and Lemma 1).

## Certification

Certified `solved`-quality (sorry-free), as a standalone refutation result.
Reusable by any future approach: `(UB_S)`, `(MRS)`, and `𝓥_S`-finiteness
(for a proper core, as a route to the whole problem) must never be
re-attempted in any form going forward.
