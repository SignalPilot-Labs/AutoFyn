# Theorem 5.1 (Master Conditional Theorem) — periodicity from n=1, given FCBC

This certifies the full round-3 chain of `intersecting-family-covering-construction`:
Lemma A (Universal Hitting), Corollary 3.1 (Coincidence Lemma), Lemma B
(single-cycle structure of Good), and Theorem 5.1 itself. Together these
prove: **if a finite covering set `H` exists (hypothesis `(†')`, the Finite
Covering Backbone Conjecture), then `a_{n+T}=a_n+L` for *every* `n≥1`**
(not merely eventually), with explicit `T=|Good|≤L` and `L_per=L=lcm(H)`
exactly.

## Setup

Fix a finite covering set `H` (i.e. `H∩rad(a_i)∩rad(a_j)≠∅` for **every**
`1≤i<j` of the whole infinite sequence — this unrestricted quantification is
essential). Let `L:=lcm(H)`, `σ(i):=rad(a_i)∩H`. Import (already certified,
generalized version): **Theorem 2.2** — `a_{n+1}=min{x>a_n: x hits Σ_n}`
where `Σ_n:={σ(1),…,σ(n)}` and "`x` hits `S`" means `(rad(x)∩H)∩S≠∅` for
every `S∈S`. Let `Σ_∞:=⋃_{n≥1}Σ_n` (finite, `≤2^{|H|}-1`, since it is the
image of `j↦σ(j)` into a finite universe).

## Lemma A (Universal Hitting)

**Statement.** For every `n,j≥1`, `σ(n)∩σ(j)≠∅`; in particular every `σ(n)`
is nonempty and `a_n` hits `Σ_∞` for every `n≥1`.

**Proof.** If `j=n`, apply `(†')` to the pair `(n,n+1)` to get
`rad(a_n)∩rad(a_{n+1})∩H≠∅`, hence `σ(n)⊇` this set `≠∅`. If `j≠n`, let
`p:=min(n,j)<q:=max(n,j)`; `(†')` applied to `(p,q)` gives
`rad(a_p)∩rad(a_q)∩H≠∅`, i.e. `σ(p)∩σ(q)≠∅`, i.e. `σ(n)∩σ(j)≠∅`
(intersection symmetric, labels are just `n,j` in some order). `∎`

This is a direct, near-immediate consequence of `(†')`'s **unrestricted**
quantification over all pairs of the infinite sequence (not just pairs with
one index bounded by `n`) — the key structural fact the rest of the theorem
exploits.

## Corollary 3.1 (Coincidence Lemma)

**Statement.** For every `n≥1`,
`a_{n+1} = min{x>a_n : x hits Σ_n} = min{x>a_n : x hits Σ_∞}`.

**Proof.** First equality is Theorem 2.2. For the second: `Σ_n⊆Σ_∞`, so
"hits `Σ_∞`" is at least as strong a requirement, giving
`min{x>a_n:x hits Σ_∞} ≥ min{x>a_n:x hits Σ_n} = a_{n+1}`. Conversely, by
Lemma A, `a_{n+1}` itself hits `Σ_∞` (apply Lemma A with index `n+1`), and
`a_{n+1}>a_n`, so `a_{n+1}` is a candidate for the left minimum, giving
`min{x>a_n:x hits Σ_∞} ≤ a_{n+1}`. Equality follows. `∎`

**Consequence.** Since "hits `Σ_∞`" depends only on `x mod L`, define
`Good := {r∈ℤ/Lℤ : some representative hits Σ_∞}` (nonempty: `0∈Good`, since
a multiple of `L` has `rad(x)⊇H`). Writing `r_n:=a_n mod L`,
`a_{n+1}-a_n=g(r_n)` for **every** `n≥1` (no "eventually" needed), where
`g(r):=min{d≥1:(r+d) mod L∈Good}`. By Lemma A, `r_n∈Good` for every `n≥1`.

## Lemma B (single-cycle structure)

Define `G(r):=(r+g(r)) mod L`, so `G(r)∈Good` for every `r`, and
`r_{n+1}=G(r_n)`.

**Statement.** Let `m:=|Good|`, enumerated `g_1<g_2<⋯<g_m` in `{0,…,L-1}`.
Then `G(g_k)=g_{k+1}` for `k<m`, and `G(g_m)=g_1=0`. Hence `G` restricted to
`Good` is a bijection, a single `m`-cycle.

**Proof.** For `k<m`: for `d=1,…,g_{k+1}-g_k-1`, `g_k+d∈(g_k,g_{k+1})`, not
in `Good` (no element of the sorted list strictly between consecutive
elements); at `d=g_{k+1}-g_k`, `g_k+d=g_{k+1}∈Good`. So `g(g_k)=g_{k+1}-g_k`,
`G(g_k)=g_{k+1}`.
For `k=m`: `g_1=0∈Good` (shown above), and no element of `Good` lies in
`{g_m+1,…,L-1}` (`g_m` is the max). For `d=1,…,L-g_m-1`, `g_m+d` in that
range, not in `Good`; at `d=L-g_m`, `(g_m+d) mod L=0=g_1∈Good`. So
`g(g_m)=L-g_m`, `G(g_m)=0=g_1`. `∎`

**Note (important, correctly avoided by the source).** `G` is **not**
injective on all of `ℤ/Lℤ` in general — e.g. `Good={0,5}⊂ℤ/10ℤ` gives
`G(1)=G(2)=G(3)=G(4)=5`. Only the restriction to `Good` is a bijection; this
is what is proved and used, not the (false) stronger claim.

## Theorem 4.1 (No pre-period) and Theorem 5.1 (exact periodicity)

**Statement (4.1).** `r_{n+T}=r_n` for every `n≥1`, `T:=m=|Good|`.

**Proof.** `r_1∈Good` (Lemma A). Writing `r_1=g_{k_0}`, induction using
`r_{n+1}=G(r_n)` and Lemma B gives `r_n=g_{k_0+(n-1) mod m}` for every `n≥1`;
hence `r_{n+T}=g_{k_0+(n+T-1) mod m}=g_{k_0+(n-1) mod m}=r_n` (since `T=m`).
`∎`

**Statement (5.1, Master Conditional Theorem).** `a_{n+T}=a_n+L` for
**every** `n≥1`.

**Proof.** `a_{n+T}-a_n=Σ_{j=0}^{T-1}(a_{n+j+1}-a_{n+j})=Σ_{j=0}^{T-1}g(r_{n+j})`.
Write `x_k:=g(r_k)`; by Theorem 4.1, `x_{k+T}=x_k` for every `k≥1`. The
window sum `Σ_{j=0}^{T-1}x_{n+j}` telescopes to a constant independent of
`n` (shifting the window by one adds `x_{n+T}` and removes `x_n`, equal by
periodicity). Evaluating at `n=1`: `r_1,…,r_T` is `g_{k_0},…,g_{k_0+T-1}`
(indices mod `m=T`), a complete traversal of `Good`, each element visited
exactly once. So the constant equals `Σ_{k=1}^m g(g_k) = Σ_{k=1}^{m-1}
(g_{k+1}-g_k) + (L-g_m) = (g_m-g_1)+(L-g_m) = L-g_1 = L` (using `g_1=0`).
`∎`

## Source

`results/imo-2026-06/approaches/intersecting-family-covering-construction.md`
(round 3), Parts 3–5.

## Certification

Independently re-derived from scratch by the reviewer, every step checked:
Lemma A's use of `(†')`'s unrestricted quantifier (correct, non-circular);
Corollary 3.1's min-of-nested-sets argument (correct); Lemma B's case
analysis including the `k=m` wraparound (correct, `g_1=0` established
separately and correctly used); the telescoping-sum argument in Theorem 5.1
(correct). The claimed "`Good={0,5}` in `ℤ/10ℤ`" counterexample to full-domain
injectivity was independently checked by hand and confirmed correct
(`G(1)=G(2)=G(3)=G(4)=5`), confirming the source correctly avoided the false
stronger claim. Independently re-verified numerically on all 8 reported
cases (`a_1∈{9,15,35,65,105,143,221,1001}`), including `a_1=35,65` (which
broke round 2's naive mechanism due to using a non-covering `H`): using the
exact `H`, `L`, `T` values reported, `r_1∈Good` holds, and `a_{n+T}=a_n+L`
holds exactly for every tested `n` (checked up to `N=1600` terms), zero
exceptions, matching every entry in the source's table.

No gaps found. Certified `solved`-quality (sorry-free), **conditional** on
hypothesis `(†')` (existence of a finite covering set `H` covering every
pair of the entire infinite sequence — this is exactly and only the Finite
Covering Backbone Conjecture, the population's remaining Gap 1). This
completely closes "Gap 2" (periodicity from `n=1`, not just eventually) for
the whole problem, strictly superseding the previously-certified
`theorem-2.4-conditional-eventual-periodicity.md` (which only gave
eventual periodicity from some `N_2`, `T≤L` a bound, `L_per` unspecified).
The moment `(†')` is established by any sibling approach, this theorem
completes the entire proof of IMO 2026 P6 for Case II (Case I is already
unconditionally solved via Lemma S′), and hence the whole problem.
