# Approach: monovariant-witness-descent

## Status
partial

## Idea in one line
Transplant the extremal/monovariant closing move of IMO 2015 SL N4 (crux corpus `aimo-0678`):
prove eventual periodicity of this greedy sequence NOT by an antichain/order argument but by an
integer statistic of the state that is monotone and range-bounded, hence frozen by well-ordering,
and read the finite modulus off the frozen value.

## Approaches tried
- **round 1 (skeleton):** proposed the transplant with three unconstructed gaps (G1 freezing
  invariant, G2 witness monotonicity, G3 recruitment descent). Reviewer flagged the naive
  first-failure witness `w_n=min{t: a_n+t∉A}` as DEGENERATE (constant 1 on a₁=375). CHANGES REQUESTED.
- **round 2 (this build):** the naive witness is confirmed dead; replaced it with TWO genuinely
  non-degenerate, numerically-verified monovariants **on the admissible set** `A_n` (density and
  max-gap), both proved monotone + range-bounded. **But a rigorous obstruction lemma (the p*-family)
  proves that *no* monovariant that is a function of `A_n` alone can close the crux** — density
  converges without ever freezing, max-gap freezes in finite time but does not bound recruitment,
  and both behave identically on a hypothetical infinite-Π family. Outcome: genuine non-degenerate
  monovariants built (satisfying the reviewer's demand) + a *proved* meta-obstruction that
  redirects the route; the crux itself is NOT closed. Honest gap `G-dyn` isolated: a monovariant
  must read the greedy **choice** values `a_n`, not just `A_n`. No overclaim.

## Current best

### Framing (all citations certified in `lemmas/`)
Notation as in the certified lemmas: `F_n=primes(a_n)`, `P=primes(a_1)`, `M=rad(a_1)=∏_{p∈P}p`.
For a stage `n` let
- `𝓕_n = {F_1,…,F_n}`, `𝓐_n =` its ⊆-minimal elements, and
- `A_n = {c≥2 : gcd(c,a_i)>1 ∀ i≤n} = {c : c meets every F∈𝓐_n}` (the stage-`n` admissible set).

`A_n` is a union of residue classes modulo `D_n := ∏(primes dividing some a_i, i≤n)` (membership
of `c` depends only on which of these primes divide `c`), so it is periodic and has a well-defined
natural density. By the certified **no-transient/fixed-successor lemma**, `a_{n+1}=s(a_n)` for all
`n≥1` and `A_n ↓ A := {c : c meets every F∈𝓐_∞}`; and by the certified **endgame**,
> if `Π := ⋃_{F∈𝓐_∞}F` is finite then `a_{n+T}=a_n+L` for ALL `n≥1` with `L=∏Π`, `T=|ρ(A)|`.

So the whole problem is the **Crux: `Π` is finite.** A step `n` is a **recruitment** if
`A_{n+1} ⊊ A_n` (the new constraint `F_{n+1}` genuinely cuts `A_n`). `Π` is finite **iff** the set
of primes ever appearing in a ⊆-minimal support is finite.

### Lemma A (density monovariant — proved). 
Let `δ_n := density(A_n)`. Then:
1. `δ_{n+1} ≤ δ_n` (non-increasing).
2. `δ_n ≥ 1/M > 0` (bounded below), so `δ_n ↓ δ_∞ ≥ 1/M`.
3. `δ_{n+1} = δ_n ⟺ A_{n+1}=A_n` (equality detects a non-recruitment exactly).

*Proof.* (1) `A_{n+1} = A_n ∩ {c : c meets F_{n+1}} ⊆ A_n`; density is monotone under inclusion of
periodic sets. (2) Every multiple of `M` meets every `F_i`: by the certified **Anchor lemma (L1)**
each `F_i` contains a prime `p∈P`, and `p|M`, so `p` divides any multiple of `M`; hence
`{M,2M,3M,…}⊆A_n`, giving `δ_n ≥ 1/M`. (3) `A_n∖A_{n+1}` is a union of residue classes mod `D_{n+1}`;
a nonempty such union has density `≥ 1/D_{n+1} > 0`, so `δ_{n+1}=δ_n` forces `A_n∖A_{n+1}=∅`. ∎

`δ_n` is **non-degenerate**: numerically (a₁=375) it takes values `0.467→0.283→0.273→0.220→0.214`,
strictly dropping at each real recruitment and floor `1/M=0.0667` — it is NOT pinned at the floor.

### Lemma B (max-gap monovariant — proved; a genuine finite-time freeze). 
Since `{M,2M,…}⊆A_n`, consecutive elements of the periodic set `A_n` differ by at most `M`; let
`γ_n ∈ {1,…,M}` be the largest gap between consecutive elements of `A_n` (over one period `D_n`).
Then:
1. `γ_{n+1} ≥ γ_n` (non-decreasing): passing from `A_n` to `A_{n+1}⊆A_n` deletes points, which can
   only merge/enlarge gaps, never shrink the maximum.
2. `γ_n ≤ M` (bounded above).
3. Hence, by well-ordering of the integers, `(γ_n)` is eventually **constant**: there is a finite
   `N` and `Γ*≤M` with `γ_n=Γ*` for all `n≥N`.

*Proof.* (1)–(2) as stated (multiples of `M` always present). (3) A non-decreasing integer sequence
bounded above stabilizes. ∎

`γ_n` is **non-degenerate and genuinely freezes** (not merely converges): numerically (a₁=375)
`γ_n: 3→6→6→…` — it moves, then freezes at `6` in finite time. This is exactly the ℕ-valued
well-ordering monovariant `aimo-0678` uses in spirit (a bounded integer statistic forced constant).

### The wall, made rigorous — Obstruction Lemma (proved). 
**No monovariant that is a function of `A_n` alone can prove the Crux.** Concretely, there is an
infinite family of finite prime-sets `𝓖={G_k}_{k≥1}` that is pairwise-intersecting, anchored at a
fixed prime, has `A(𝓖_n)`-density and `A(𝓖_n)`-max-gap both eventually frozen, yet whose union of
⊆-minimal supports is infinite.

*Construction & proof.* Fix a prime `p*` and an increasing prime sequence `q_1<q_2<⋯`. Put
`G_k={p*,q_k}` and `𝓖_n={G_1,…,G_n}`, `A(𝓖_n)={c : ∀k≤n, p*|c or q_k|c}`.
- *Intersecting & anchored:* every two `G_k` share `p*`; all contain `p*`.
- *Minimality persists:* the `G_k` are distinct 2-element sets and the family contains no singleton,
  so no `G_j⊊G_k`; every `G_k` is ⊆-minimal. Thus `Π(𝓖)=⋃_kG_k={p*,q_1,q_2,…}` is **infinite**.
- *A-monovariants freeze:* `A(𝓖_n)⊇{multiples of p*}`, so max-gap `≤p*` and (being non-decreasing
  and integer-bounded) it freezes at `p*` in finite time. Density
  `= 1/p* + (1-1/p*)∏_{k≤n}(1/q_k) → 1/p*`, a non-increasing sequence bounded below, converging.
  (Verified: `p*=2` gives density `0.667→0.533→0.500→0.500`, max-gap `≤2`, while `Π` is infinite.)

Since every quantity computable from `A_n` (density, max-gap, count of residue classes mod any fixed
modulus, gap multiset, …) evolves on `𝓖` exactly as it could on a real sequence yet `Π(𝓖)=∞`, such a
quantity cannot certify `Π` finite. **The Crux therefore requires the greedy DYNAMICS** — which
integers `a_n` are actually chosen — not a set-statistic of `A_n`. (This matches, and re-derives from
the monovariant side, the antichain approach's §7b counterexample and the `aimo-0224` cautionary
note: intersecting+anchored structure alone is consistent with infinite `Π`.) ∎

### Consequence for this route (honest)
- Density (Lemma A) converges but **never freezes** on the p*-type structure: each recruitment costs
  positive density but the costs can `→0` (a convergent series with infinitely many terms), so
  stabilization of `δ_n` does **not** bound the number of recruitments. This is the exact failure
  the reviewer predicted for a density monovariant.
- Max-gap (Lemma B) **does** freeze in finite time, but its freezing does **not** stop recruitment
  (on `a₁=375` it freezes at `n=3` while a new prime `19` enters at `n=7` and density still drops at
  `n=26`; on the p*-family it freezes while infinitely many primes still enter). So Lemma B, though a
  genuine well-ordering monovariant, controls the gap geometry but not the alphabet.

### The precise remaining gap (G-dyn)
What is needed is a monovariant that reads the **choices** `a_n`, engineered so the p*-degeneracy is
impossible. The Crux is equivalent to the distilled **dynamical statement**:

> **(G-dyn)** There is no fixed prime `p*` and infinite set of distinct primes `{q_k}` such that
> infinitely many terms `a_{j_k}` have `F(a_{j_k})` a ⊆-minimal support containing `p*` and `q_k`
> with `q_k→∞`. Equivalently: for each `p*∈P`, only finitely many distinct primes `q` occur in a
> ⊆-minimal support together with `p*`.

By the certified **Anchor + pigeonhole** (`P` finite, every minimal support meets `P`), `Π` finite is
*equivalent* to (G-dyn) over the finitely many anchors `p*∈P`. (G-dyn) is what the greedy rule must
forbid; the Obstruction Lemma shows no purely-`A_n` monovariant can supply it. **This gap is left
explicitly open and is NOT claimed as proved.** The natural next handle is a monovariant built from
the certified **Distance–prime lemma (L3)** applied to the chosen values (a large prime `q` shared by
two terms forces those terms `≥q` apart, hence `≥q/M` apart in index by linear growth), turned into a
strictly-descending integer at each new large-prime recruitment — this construction is not yet found.

## Full proof
Not present — Status partial. The Crux (Π finite) is not closed by this route; see G-dyn. Two
non-degenerate monovariants (Lemmas A, B) and a proved obstruction (no `A_n`-only monovariant can
work) are established.

## Promotable lemmas
- **Density monovariant (Lemma A):** `δ_n=density(A_n)` is non-increasing, `≥1/M`, and
  `δ_{n+1}=δ_n ⟺ A_{n+1}=A_n`. Proved in full above. Reusable as a recruitment detector for ANY
  approach.
- **Max-gap monovariant (Lemma B):** `γ_n∈{1,…,M}` (largest gap of `A_n`) is non-decreasing and
  bounded by `M`, hence freezes in finite time. Proved in full above.
- **A_n-monovariant Obstruction Lemma:** an explicit infinite intersecting anchored family `{p*,q_k}`
  on which all `A_n`-statistics freeze/converge while `Π` is infinite; hence no monovariant depending
  only on `A_n` can prove `Π` finite — the Crux needs the greedy choice dynamics. Proved in full
  above. This is a certifiable *negative* result that saves future rounds from A_n-only monovariants.

---

## Round-3 build target (G-dyn) — per-small-companion-set descent on the CHOICES

The Obstruction Lemma bars `A_n`-statistics; this build reads the greedy **choices** `a_n`. The new
mechanism is the selection-explorer **S3 sharpening**: domination happens **per small-companion-set
`S`**, not per prime `q` — a single term with support `⊆ S` kills *every* minimal support `{S,q}` for
all `q` seen so far, in one stroke. So the right object to descend is the set of *pending small
companions*, which is finite once the small-prime part of `Π` is controlled.

**Setup (all certified).** For a minimal support `G ∈ 𝓐_∞` containing a large prime, write
`G = S(G) ⊔ L(G)` with `S(G) = G ∩ {primes ≤ M}` its **small companion** and `L(G)` its large
primes (§8.2 shows `S(G) ≠ ∅`). Call `S` **realized** at stage `n` if some term `a_j` (`j ≤ n`) has
`F(a_j) ⊆ S`. By §8.3 (certified), a minimal support `G` persists in `𝓐_∞` **iff** `S(G)` is never
realized.

**Descent object.** Let `𝒫_n :=` the set of small companions `S` that are (i) the companion of some
minimal support already seen in `𝓐_n` and (ii) not yet realized at stage `n` — the **pending
companions**. Define the integer statistic
`Φ_n := (number of distinct pending companions in 𝒫_n)`. Reading choices: each **recruitment** of a
new large-prime minimal support `{S,q}` can only *add* the companion `S` (bounded pool, below); each
**domination** event (a chosen term `a_j` with `F(a_j) ⊆ S`) *removes* `S` and, by S3, kills the
whole `{S,·}` family at once.

**Target (G-dyn, restated).** Show `𝒫_n` is drawn from a **finite pool** and every pending companion
is eventually realized by an actual chosen term, so `Φ_n` cannot support infinitely many distinct
large primes ⇒ `Π` finite ⇒ theorem via the certified endgame.

**Key lemma to prove (the wall).**
> **(K-real) Every pending small companion is realized in bounded time.** If `S` is the small
> companion of a minimal support, the greedy sequence eventually chooses a term `a_j` with all prime
> factors in `S` (`F(a_j) ⊆ S`).

*Mechanism / why it should hold (choice-reading).* A "pure-`S`" integer `m = (∏S)^k ≥ a₁` lies in
`A` **iff** it meets every OTHER minimal support `G'` — i.e. `S ∩ G' ≠ ∅` for all `G' ∈ 𝓐_∞`. By E1
such an `m` is then a term. So (K-real) ⟺ *some pure-`S` power meets every minimal support*. The
obstruction is a `G'` with `S ∩ G' = ∅`. But by S3 the companions form a finite pool (candidate:
subsets of primes `≤ M`, of which there are `≤ 2^{π(M)}`), so the pending set is finite; combine with
the certified **distance–prime L3** (a large prime `q ∈ G'` shared with the `q`-carrying term forces
those terms `≥ q` apart, hence large-`q` supports are "spread out" and cannot all simultaneously
block every window) to force a realizing window. **This finiteness-of-companion-pool + realizing-
window bound is the open step.**

**Descent conclusion (given K-real).** With a finite companion pool and every companion realized in
bounded time, only finitely many distinct companions `S` ever pend, and each hosts (before its
domination) finitely many large primes within the L3 distance budget of a bounded window ⇒ `Π`
finite. `Φ_n` then reaches `0` in finite time and stays there (no new companion after the pool is
exhausted), the well-ordering freeze that the naive density/max-gap monovariants could not deliver.

**Distinctness from `value-stream-double-freeze` (keep the field far apart).** This route **counts
recruitments** to bound the *alphabet* `Π` (target: `Π` finite, then invoke endgame); the
double-freeze route **pins the cycle** of the gap-word directly (target: periodicity, `Π`-finite as a
by-product) and never counts recruitments. Different descent object, different target — they do not
share a gap.

**Watch out for.**
- The companion pool being `⊆ 2^{primes ≤ M}` is a *conjecture* — a companion could in principle
  contain a prime in `(M, ?]`; §8.2 only gives `S(G)` contains a prime of `P`. Prove/refute the pool
  bound before relying on it (numerically: check whether any minimal-support companion has a prime
  `> M` across seeds `{375,385,9375,15015}`).
- Do NOT slide back to an `A_n`-statistic (certified dead): `Φ_n` must be read off the *chosen terms*
  (which `F(a_j) ⊆ S` have actually occurred), not off the admissible set `A_n`.
- L3 gives `q ≤ |t−t'|`, an index/value distance — not directly a bound on how many `q` pend; the
  quantitative "realizing window" step is the honest gap, do not hand-wave it.
