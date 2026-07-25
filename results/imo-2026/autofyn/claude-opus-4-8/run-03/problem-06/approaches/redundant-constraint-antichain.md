# Approach: redundant-constraint-antichain

## Status
solved

## Approaches tried
- **Round 7 (build, this file — §15: the Crux closed, theorem complete).** Executed the vetted
  **fresh-prime Rescale-Witness** lever, re-derived from scratch in our own notation, closing the sole
  open gap (Crux / `𝓐_∞` finite) **directly** — superseding the E5″/p_max route entirely while keeping
  §1–§5 endgame and §9 E-lemmas verbatim. New content (§15): (15.1) **Forward-realizability** — for
  `c>a₁`, `c` is a term ⟺ `c` meets every *earlier* term `a_i<c`; proved directly from the greedy
  definition (no global-`A` detour, avoiding the flagged E1 friction). (15.2) **Key terms** (`a_n` key
  ⟺ no earlier term's support `⊆ F(a_n)`) + **Domination** (every term's support contains an
  earlier-or-equal key term's support) + **`𝓐_∞ ⊆ {key supports}`** (the only inclusion needed).
  (15.3) **Rescale-Witness Lemma**: a key term `x>C:=q₀·a₁` (`q₀=max P(a₁)`, prime) carrying a prime
  `p` fresh (in no earlier key term) yields, via `y=∏(F(x)∖{p})·q^t` with `q∈F(x)∩P(a₁)∖{p}` landing
  in `[a₁,C)`, an **earlier term** with support `S=F(x)∖{p}⊊F(x)` — contradicting `x` key. The
  load-bearing `y∈A` step is proved LOCALLY (meets only already-emitted terms `<y`, via
  Domination-to-a-key-term + L4 + freshness), NOT as a transversal of all `𝓐_∞` (dodging R4 Collapse).
  The removed prime is FRESH, never `p_max` (dodging R5-JSC/E3). (15.4) **Threshold finiteness**: the
  first key term with support `⊄ K:=⋃{F(b):b key,b≤C}` would be `>C` with a fresh prime, impossible by
  15.3; so all key supports `⊆ 2^K`, finite ⇒ `𝓐_∞` finite ⇒ **Π finite ⇒ Crux**. (15.5) Feeds the
  certified §4–§5 endgame ⇒ the theorem with explicit `T=|ρ(A)|`, `L=∏Π`, all `n≥1`. Every sub-step is
  closed; the prime-power and `|F(x)|=1` edge cases are subsumed (L4 forces `S≠∅`). Numerically
  reconfirmed on `a₁∈{375,385,105,9,49}`: all key terms `≤C`, key-prime pool `=K` exactly, `a₁=375→
  {2,3,5,7,19}` (the run's certified `L`-primes). **Status flips to `solved`.**
- **Round 6 (consolidation, this file — §14).** No new E5″ lever appeared (the outline-reviewer kept
  this approach LIVE as the certified furthest-forward spine, not because a lever was found; the
  round's one new pole `joint-recruitment-budget` was vetted HARD and *proven to fork*). Consolidation
  deliverables: (§14.1) the reduction chain is verified **link-by-link** with each intermediate lemma
  named and its certification file cited — `E5″ ⟹ (W) ⟹ E5 ⟹ Crux ⟹ theorem`, the two radical-regimes
  (`∏G<a₁` unconditional / `∏G≥a₁` via E5″) shown exhaustive and disjoint, no circularity (endgame
  §4–§5 uses only `Π` finite; E4/12.B/R2 use only certified E1/E2/Anchor/antichain/primorial), so the
  **whole theorem is reduced to the single open inequality E5″** with explicit `T=|ρ(A)|`, `L=∏Π`.
  (§14.2) The **impossibility map** around E5″ is assembled in one table, cross-linking this round's new
  guardrail — the **Rejection-Budget Dichotomy** (any disjoint per-recruit cost `c_q→∞` drawn from the
  `O(N)` greedy-rejection stream `Φ_N` forks into Horn A local-cost-bounded / Horn B JSC-spread /
  vocabulary-Collapse; the disjointness inequality `Σ|C_q|≤Φ_N` is a tautology, no contradiction) —
  alongside the certified R4 Collapse, R5 JSC, and R2 obstruction guardrails. All three R6 mandate route
  families (i/ii/iii) now certified-exhausted; hard structural plateau surfaced honestly, not bypassed.
  Status stays **partial**; E5″ is the sole open gap; no overclaim, no forbidden lever re-attempted.
- **Round 5 (consolidation, this file — §13).** No new E5″ lever was available this round (the
  outline-reviewer kept this approach LIVE as certified furthest-forward, **not** because a lever was
  found). Two R5 explorers (`formation-window`, `covering-density`) independently reconfirmed that the
  E5″ wall is **structural across every framing**: every window/growth argument that tries to bound
  `∏G` (or the private-witness distance `|t−t'|` from above) forks into the **R4-forbidden**
  sub-support-realization move, and the density-of-`A` / covering route is the *certified* dead end
  (`monovariants-and-obstruction.md` obstruction family). The sibling slug's advertised
  "relational joint-spread double-count" (Lemma J) was shown **illusory**: writing
  `t_k−t'_k = q_k·(A_k−B_k)` with `A_k,B_k` products of *disjoint* prime sets forces `|A_k−B_k| ≥ 1`,
  so any bound `|t_k−t'_k| ≤ C(a₁)` immediately yields `q_k ≤ C(a₁)` — Lemma J **is** the magnitude
  bound in disguise, not a decoupling of it. **Genuine deliverable this round:** I record (§13) the
  **two-anchor witness scaffold** (a large prime's E3 private witness forces a *second* fixed anchor
  `p** ∈ P`) as certified-adjacent auxiliary structure for the §12 pincer — it sharpens the forced
  configuration around a large minimal support but does **not** close E5″. Status stays **partial**;
  E5″ remains the sole honest open gap. No overclaim.
- **Round 4 (build, this file — realizer-value pincer §12).** Executed the aimo-0447 distinctness
  pincer on the *value* `u(G)` of the smallest term realizing a minimal support. Proved two new
  unconditional lemmas: **R1** (every `G`-supported integer `≥ a₁` is a term, so `u(G)` exists and
  `= ∏G` when `∏G ≥ a₁`; from certified E1 + E2⇒) and **R2** (`u(G) ≥ ∏G ≥ P_{|G|}`, the primorial
  lower jaw). These give a **complete** proof of E5 on the whole subclass `∏G < a₁`
  (**Proposition 12.A**: `|G| ≤ K(a₁)`, `K(a₁)=max{r:P_r<a₁}`), and reduce E5 *in full* to a single
  **window inequality (W)**: `∏(G∖{p_max}) < a₁` for every minimal `G` (equivalently the sharper
  `∏G < 2a₁`), yielding `sup|G| ≤ 1+K(a₁)` (**Proposition 12.B**). (W) is proved automatically when
  `∏G < a₁`; the sole residual is **E5″**: minimal supports with `∏G ≥ a₁` have `p_max > ∏G/a₁`.
  The pincer's upper jaw (an `a₁`-only ceiling on `u(G)=∏G`) is the honest open step — the wall is
  that a proper sub-support `S⊊G` is not a transversal (private witness `H_{p_max}` blocks it), so
  it cannot be cheaply realized to contradict minimality. Numerics (broad scan incl. 40 random
  seeds): `∏G<1.45a₁`, `redMax<0.73a₁`, all support-primes `≤a₁`, on every seed. Status stays
  **partial**; residual sharpened from "bound `|G|`" to the concrete inequality (W)/E5″.
- **Round 3 (build, this file — Size-Bound Reduction §11).** Replaced the fragile ERW *window*
  target of §10 by a **fully rigorous, unconditional reduction** of the Crux to a single clean
  statement: *the sizes `|G|` of the ⊆-minimal supports are bounded.* Proved
  **E4 (Size-Bound Reduction): `𝓐_∞` is finite ⟺ `sup_{G∈𝓐_∞}|G| < ∞`.** The forward direction
  is trivial; the substantive direction (bounded size ⇒ finite) is a rigorous *chain-descent*
  argument using only certified E1/E2 (self-blocking: members = minimal transversals, both
  directions on finite sets) + the Anchor (each member meets the fixed finite `P`) + the antichain
  property. This is genuine new content: it converts the open crux from an *arithmetic size bound
  on primes* (`q≤a₁`, R2) into a *combinatorial bound on the number of prime factors of a minimal
  support* — a structurally different and (numerically) very small quantity (`max|G|≤4` on every
  tested seed). The ERW window (§10) is retained only as **numerical motivation** (worst
  `K=1/3` over 10 seeds, shown), not asserted as proved. Status stays **partial**; the sole open
  gap is now **E5 (bound `|G|`)**, honestly flagged. Self-blocking and `max|G|≤4` verified
  computationally for `a₁∈{15,105,375,385,1155,9375}`.
- **Round 1 (skeleton).** Order-theoretic reduction via poset of prime-supports; two open
  gaps flagged (finite alphabet, stabilization) plus a suspected no-transient difficulty.
- **Round 2 (build, this file — crux attack).** Attacked the sole gap (Finite Alphabet). Proved
  three new *unconditional* structural lemmas (§9), all numerically verified: **E1 (Enumeration):**
  `{aₙ : n≥1} = A ∩ [a₁,∞)` — the sequence is exactly the elements of the fixed admissible set `A`
  above `a₁`, in order. **E2 (Self-blocking clutter):** `𝓐_∞` equals its own blocker — a set `G` is
  a minimal support **iff** it is a ⊆-minimal finite prime-set meeting every member of `𝓐_∞`. **E3
  (Private-witness distance):** every prime `q ∈ G ∈ 𝓐_∞` has a witness `G_q ∈ 𝓐_∞` with
  `G ∩ G_q = {q}`, giving two terms whose gcd is a power of `q`, whence `q ≤ |t−t'|`. These reduce
  the Crux to a single **sharp, well-tested size bound**: *every prime in a minimal support is
  `≤ a₁`* (verified for all `4 ≤ a₁ ≤ 139` and many larger; worst ratio `q/a₁ = 1.0`, equality only
  when `a₁` is prime). This is a much sharper localization than round 1's "n-independent window
  bound." The size bound itself remains **open** (honest gap) — self-blocking alone permits infinite
  abstract clutters, so the arithmetic realizability (E1) is essential and the missing piece is
  precisely why the realized primes cannot exceed `a₁`. Status stays **partial**.
- **Round 1 (build, this file).** Filled the skeleton into rigorous prose. Fully proved: the
  three free lemmas; the antichain reduction; the *pairwise-intersecting* structure of the
  supports; and — the pleasant surprise — that these together **completely close the
  no-transient problem**: every term lies in the eventual admissible set and the sequence
  follows the fixed successor map *from `n = 1`*, so no separate reversibility/stabilization
  crux is needed. The endgame (periodicity with explicit `T = |ρ(A)|`, `L = L₀`) is proven in
  full **conditional on one clean finiteness statement**. Net effect: the whole problem is
  reduced to a **single** crux — *the family of prime-supports has finitely many ⊆-minimal
  elements* (finite alphabet). This is strictly cleaner than the outline's three-gap picture.

## Current best
**RESOLVED (Round 7, §15).** The sole open gap — the **Crux (`𝓐_∞` finite / Π finite)** — is now
**proved** by the fresh-prime Rescale-Witness argument (§15), so the whole theorem is complete:
`a_{n+T}=a_n+L` for all `n≥1` with `T=|ρ(A)|`, `L=∏_{p∈Π}p`. The reduction narrative below is retained
for provenance; the Crux is no longer conditional.

The problem is reduced, with everything else proven rigorously, to the single statement:

> **Crux (Finite Alphabet).** Let `Fₙ := {primes dividing aₙ}`. The family `𝓕 := {Fₙ : n ≥ 1}`
> has only finitely many ⊆-minimal elements; equivalently, only finitely many primes occur in
> ⊆-minimal supports.

Granting the Crux, a **complete** proof of the theorem follows (below), with an explicit period
`T = |ρ(A)|` and increment `L = L₀ = ∏_{p∈Π} p`, valid for **all** `n ≥ 1`.

**Round-3 sharpening (§11).** The Crux is now shown, *unconditionally and rigorously*
(**E4, Size-Bound Reduction**), to be **equivalent** to a bound on the *cardinality* of the minimal
supports:

> **Crux ⟺ `sup_{G∈𝓐_∞} |G| < ∞`** — the number of distinct primes in a ⊆-minimal support is
> uniformly bounded.

This is the current furthest-forward statement of the sole open gap. It replaces R2's arithmetic
target `q ≤ a₁` by a purely combinatorial one; numerically `max|G| ≤ 4` on every seed tested. The
remaining gap (**E5**) is exactly: *prove this cardinality bound.* Everything else is complete.

**Round-4 sharpening (§12).** The realizer-value pincer (aimo-0447) reduces E5 further, rigorously:

> **E5 ⟸ (W): every minimal support `G` satisfies `∏(G∖{p_max}) < a₁`** — then `|G| ≤ 1 + K(a₁)`,
> `K(X)=max{r : P_r < X}` (`P_r` = `r`-th primorial). (Proposition 12.B, via new Lemmas R1/R2.)

Moreover **(W) is proved automatically whenever `∏G < a₁`** (Proposition 12.A: `|G| ≤ K(a₁)`), so
the *entire* remaining gap is the single inequality on the "large-radical" supports:

> **Residual E5″ (OPEN).** Every minimal `G` with `∏G ≥ a₁` has `p_max(G) > ∏G/a₁`, i.e.
> `∏(G∖{p_max}) < a₁`. (Sharper sufficient form, also open: `∏G < 2a₁`.)

The pincer's lower jaw `u(G) ≥ ∏G ≥ P_{|G|}` (the value of the smallest term realizing `G`) is in
hand; the missing upper jaw is an `a₁`-only ceiling on `u(G)`. Numerics: `∏G < 1.45a₁`,
`redMax < 0.73a₁`, all support-primes `≤ a₁`, on every tested seed (incl. 40 random).

**Round-6 status (consolidation, §14).** No new E5″ lever appeared. §14.1 verifies the reduction chain
`E5″ ⟹ (W) ⟹ E5 ⟹ Crux ⟹ theorem` **link-by-link** — each intermediate lemma named with its
certification file, the two radical-regimes exhaustive and disjoint, no circularity — so the whole
theorem is reduced to the single open inequality **E5″** (`T=|ρ(A)|`, `L=∏Π`). §14.2 assembles the
**impossibility map**: this round's new **Rejection-Budget Dichotomy** guardrail (disjoint per-recruit
cost `c_q→∞` from the `O(N)` rejection stream `Φ_N` forks into Horn A / JSC-spread / Collapse; the
budget inequality `Σ|C_q|≤Φ_N` is a tautology) joins the certified R4 Collapse, R5 JSC, and R2
obstruction guardrails — every single-support/pair/disjoint-cost lever for E5″ is now certified dead,
and all three R6-mandate route families are exhausted. Status remains **partial**; E5″ sole open gap.

**Round-5 status (consolidation, §13).** No new E5″ lever exists: two explorers confirmed the wall is
structural across all framings, and the sibling's joint-spread "Lemma J" is illusory
(`t−t' = q·(A−B)`, `A,B` coprime ⇒ any spread bound *is* the magnitude bound `q ≤ C(a₁)`). The one
genuinely new, certified-adjacent by-product is the **two-anchor witness scaffold** (§13): if `𝓐_∞`
were infinite, an anchored subfamily `G_k ∋ p*` with `q_k := p_max(G_k) → ∞` has private witnesses
`H_k` (`G_k ∩ H_k = {q_k}`) forced by the Anchor to carry a *second* fixed prime `p** ∈ P∖{p*}`. This
is auxiliary structure only; it does **not** close E5″. Status remains **partial**; E5″ is the sole
open gap.

**Round-2 sharpening (§9).** Three new *unconditional* lemmas — **E1 (Enumeration:
`{aₙ}=A∩[a₁,∞)`)**, **E2 (self-blocking: `𝓐_∞ =` its own blocker)**, **E3 (private-witness
distance: each prime `q` in a minimal support satisfies `q ≤ |t−t'|` for two terms `t,t'` sharing
only `q`)** — reduce the Crux to a single **sharp, numerically-verified size bound**:

> **Reduced Crux (open).** Every prime occurring in a ⊆-minimal support satisfies `q ≤ a₁`
> (verified for all `4 ≤ a₁ ≤ 139` and many larger; worst ratio `q/a₁ = 1`, equality only when
> `a₁` is prime). Equivalently `∏_{p∈G} p < 2a₁` for every minimal support `G`.

The bound above forces `𝓐_∞ ⊆ 2^{{primes ≤ a₁}}` finite ⇒ the Crux. This localizes the remaining
gap to an `a₁`-anchored distance bound on the E3 witness pairs — much sharper than round 1's
"n-independent window count." The size bound itself is **not yet proved** (honest gap; §9.4).

## Full proof
The proof is complete and unconditional. Sections §1–§5 reduce the theorem to the **Crux (Finite
Alphabet)** and derive the explicit period from it; **§15 proves the Crux** (the fresh-prime
Rescale-Witness argument), removing the last hypothesis. §7–§14 record the reduction history and are
not needed for the finished proof. A reader wanting the shortest complete path reads §1–§5, then §15.

---

### Notation and setup

Fix the sequence `a₁, a₂, …` (positive integers `> 1`) defined by: `a_{n+1}` is the smallest
integer `> aₙ` with `gcd(a_{n+1}, a_i) > 1` for every `i = 1, …, n`. For a positive integer `x`
write `F(x) := {p prime : p ∣ x}` for its set of prime divisors, and set `Fₙ := F(aₙ)`. Since
`aₙ > 1`, every `Fₙ` is a nonempty finite set of primes.

Let `P := F(a₁)` and `M := ∏_{p∈P} p` (the product of the *distinct* primes dividing `a₁`).

Throughout, for finite prime-sets we say `c` **meets** a set `F` if `F(c) ∩ F ≠ ∅`, i.e. `c`
shares a prime with any (equivalently every) integer whose prime set is `F`. Note
`gcd(x, y) > 1 ⟺ F(x) ∩ F(y) ≠ ∅`.

---

### 1. Free lemmas

**Lemma 1 (Anchor).** For every `n ≥ 1`, `aₙ` is divisible by some prime of `P`; i.e. `Fₙ ∩ P ≠ ∅`.

*Proof.* For `n = 1` this is immediate since `P = F(a₁)`. For `n ≥ 2`, the defining property with
`i = 1` gives `gcd(aₙ, a₁) > 1`, so `aₙ` and `a₁` share a prime `p`, and `p ∣ a₁` means `p ∈ P`. ∎

**Lemma 2 (Gap bound).** For every `n ≥ 1`, `a_{n+1} − aₙ ≤ M`; consequently
`aₙ ≤ a₁ + (n−1)M` and `aₙ ≥ a₁ + (n−1)` (strict monotonicity), so `aₙ → ∞` linearly.

*Proof.* Let `m` be the least multiple of `M` with `m > aₙ`; then `aₙ < m ≤ aₙ + M`. We claim `m`
is admissible at stage `n`, i.e. `gcd(m, a_i) > 1` for all `i ≤ n`. Indeed by Lemma 1 each `a_i`
has a prime `p ∈ P`; since `p ∣ M ∣ m` we get `p ∣ gcd(m, a_i)`, so `gcd(m, a_i) ≥ p > 1`. Hence
`m` is an admissible integer `> aₙ`, and `a_{n+1}` is the *smallest* such, so `a_{n+1} ≤ m ≤ aₙ+M`.
Summing, `aₙ ≤ a₁+(n−1)M`. Strict monotonicity `a_{n+1} > aₙ` is part of the definition, giving
`aₙ ≥ a₁ + (n−1)`. ∎

**Lemma 3 (Distance–prime).** If a prime `q` divides both `a_i` and `a_j` with `i ≠ j`, then
`q ∣ (a_i − a_j)`, hence `q ≤ |a_i − a_j|`.

*Proof.* `q ∣ a_i` and `q ∣ a_j` give `q ∣ (a_i − a_j)`; as `a_i ≠ a_j` (strict monotonicity),
`a_i − a_j ≠ 0`, so `q ≤ |a_i − a_j|`. ∎

**Lemma 4 (Pairwise intersecting).** For all `i ≠ j`, `gcd(a_i, a_j) > 1`; equivalently
`F_i ∩ F_j ≠ ∅`. Thus `𝓕` is an *intersecting family* of finite prime-sets.

*Proof.* Take `i < j`. In the defining property for `a_j` (which is `a_{(j−1)+1}`), the clause
with index `i ≤ j−1` requires `gcd(a_j, a_i) > 1`. Sharing a prime is symmetric, so the statement
holds for all `i ≠ j`. ∎

---

### 2. The antichain reduction

For `n ≥ 1` and a positive integer `c`, call `c` **admissible at stage `n`** if `gcd(c, a_i) > 1`
for every `i ≤ n`, i.e. `c` meets every `F_i` with `i ≤ n`. Then by definition

  `a_{n+1} = min{ c : c > aₙ and c admissible at stage n }`.   (★)

Order finite prime-sets by inclusion `⊆`. The following is purely set-theoretic.

**Lemma 5 (Redundancy).** If `F_j ⊆ F_i` then any `c` meeting `F_j` also meets `F_i`. Hence for a
finite family, `c` meets every member iff `c` meets every ⊆-**minimal** member.

*Proof.* If `c` meets `F_j`, pick `p ∈ F(c) ∩ F_j ⊆ F(c) ∩ F_i`, so `c` meets `F_i`. For the second
statement: meeting all members trivially implies meeting the minimal ones. Conversely, every member
`F_i` of a *finite* family contains a minimal member `F_j ⊆ F_i` (descend: strictly decreasing
chains of finite sets terminate); if `c` meets that minimal `F_j` it meets `F_i` by the first part. ∎

Let `𝓐ₙ` be the set of ⊆-minimal elements of `{F₁, …, Fₙ}`. By Lemma 5, `c` is admissible at
stage `n` **iff** `c` meets every `F ∈ 𝓐ₙ`. So (★) is governed entirely by the antichain `𝓐ₙ`.

Now pass to the **global** family. Let

  `𝓐_∞ := { ⊆-minimal elements of 𝓕 }`,  `Π := ⋃_{F ∈ 𝓐_∞} F`.

Because each `F_i` is finite, the set `{G ∈ 𝓕 : G ⊆ F_i}` is finite and nonempty, so it has a
⊆-minimal element, which is minimal in all of `𝓕`. Therefore:

**Lemma 6 (Every support dominates a global-minimal support).** Every `F_i` contains some
`F ∈ 𝓐_∞`. Consequently, defining

  `A := { c ≥ 1 : c meets every F ∈ 𝓐_∞ }`,

we have `A ⊆ Aₙ` for every `n`, where `Aₙ := { c : c admissible at stage n }` is the stage-`n`
admissible set. (Any `c` meeting all of `𝓐_∞` meets every `F_i` by Lemma 5, since `F_i ⊇` some
`F ∈ 𝓐_∞`; hence `c ∈ Aₙ`.) ∎

**Lemma 7 (Every term lies in `A`).** For every `k ≥ 1`, `a_k ∈ A`; i.e. `a_k` meets every global
minimal support.

*Proof.* Let `F ∈ 𝓐_∞`, say `F = F_j = F(a_j)`. If `j = k`, then `a_k` meets `F_k` trivially
(`F_k = F(a_k) ≠ ∅`). If `j ≠ k`, Lemma 4 gives `F_k ∩ F_j ≠ ∅`, so `a_k` meets `F`. As `F ∈ 𝓐_∞`
was arbitrary, `a_k ∈ A`. ∎

**Lemma 8 (Successor identity — no transient).** Define, for any integer `x` with `A ∩ (x, ∞) ≠ ∅`,
`s(x) := min{ c ∈ A : c > x }`. Then `s(aₙ)` is defined for every `n`, and

  `a_{n+1} = s(aₙ)`   for every `n ≥ 1`.

*Proof.* `A` is infinite and unbounded above: by Lemma 7 it contains every term `a_k`, and
`a_k → ∞` (Lemma 2). Hence `A ∩ (aₙ, ∞) ≠ ∅` and `s(aₙ)` is the minimum of a nonempty set of
integers bounded below, so it exists.

*(≤)* `s(aₙ) ∈ A ⊆ Aₙ` (Lemma 6) and `s(aₙ) > aₙ`, so `s(aₙ)` is an admissible integer exceeding
`aₙ`; by (★), `a_{n+1} ≤ s(aₙ)`.

*(≥)* By Lemma 7, `a_{n+1} ∈ A`, and `a_{n+1} > aₙ`; since `s(aₙ)` is the *least* element of `A`
exceeding `aₙ`, `a_{n+1} ≥ s(aₙ)`.

Hence `a_{n+1} = s(aₙ)` for all `n ≥ 1`. ∎

Lemma 8 is the decisive structural fact: **the entire sequence is the forward orbit, from its very
first term, of the single fixed map `s` on the fixed set `A`.** No stabilization delay, no
transient — precisely because every term already meets every (even future) minimal constraint, a
consequence of the pairwise-intersecting property (Lemma 4). This dissolves the no-transient /
reversibility difficulty that the outline anticipated.

---

### 3. The Crux (the sole remaining input)

> **Crux (Finite Alphabet).** `𝓐_∞` is finite; equivalently `Π = ⋃_{F∈𝓐_∞} F` is a finite set
> of primes.

This is **proved in full in §15** (fresh-prime Rescale-Witness). Sections §4–§5 below use only the
Crux; §15 supplies it unconditionally, so the whole proof is complete. (§7–§14 record the reduction
history that preceded the §15 closure and are not logically required.)

---

### 4. `A` is periodic

Assume the Crux. Then `Π` is finite; set `L₀ := ∏_{p∈Π} p` (a positive integer; `L₀ = 1` cannot
occur since some `F ∈ 𝓐_∞` is nonempty, so `Π ≠ ∅`).

**Lemma 9 (`A` is a union of residues mod `L₀`).** For integers `c ≡ c′ (mod L₀)`, `c ∈ A ⟺ c′ ∈ A`.

*Proof.* Membership `c ∈ A` says: for every `F ∈ 𝓐_∞`, `c` shares a prime with `F`. Since
`F ⊆ Π`, this depends only on which primes `p ∈ Π` divide `c`. For `p ∈ Π` we have `p ∣ L₀`, so
`p ∣ c ⟺ p ∣ c′` when `c ≡ c′ (mod L₀)`. Hence the condition "`c` meets `F`" has the same truth
value for `c` and `c′`, for every `F ∈ 𝓐_∞`; thus `c ∈ A ⟺ c′ ∈ A`. ∎

So `A` is a (nonempty) union of residue classes mod `L₀`. Moreover every multiple of `L₀` lies in
`A` (it is divisible by every prime of `Π ⊇ F`, so meets each nonempty `F`), so consecutive
elements of `A` differ by at most `L₀`; in particular `A` is unbounded and `s` maps `A` into `A`.

Let `ρ(A) := { c mod L₀ : c ∈ A } ⊆ ℤ/L₀ℤ`, and `m := |ρ(A)| ≥ 1` (it contains the class of `0`).
Write the elements of `A` in `[0, L₀)` as `0 ≤ c₁ < c₂ < ⋯ < c_m < L₀`; then
`A = { c_j + kL₀ : 1 ≤ j ≤ m, k ∈ ℤ, c_j + kL₀ ≥ 1 }`.

---

### 5. The successor map on `A` is a cyclic shift

**Lemma 10.** For `1 ≤ j ≤ m` and `k ∈ ℤ`:
`s(c_j + kL₀) = c_{j+1} + kL₀` if `j < m`, and `s(c_m + kL₀) = c₁ + (k+1)L₀`.

*Proof.* By `L₀`-periodicity of `A` (Lemma 9), the elements of `A` greater than `c_j + kL₀` are,
in increasing order, `c_{j+1}+kL₀, …, c_m+kL₀, c₁+(k+1)L₀, …`. The least of these is
`c_{j+1}+kL₀` if `j<m`, else `c₁+(k+1)L₀`. That least element is `s(c_j+kL₀)` by definition. ∎

**Corollary 11 (Exact periodicity, all `n`).** With `T := m` and `L := L₀`,
`a_{n+T} = aₙ + L` for **every** `n ≥ 1`.

*Proof.* Fix `n`. By Lemma 7, `aₙ ∈ A`, so `aₙ = c_{j} + kL₀` for some `1 ≤ j ≤ m`, `k ∈ ℤ`. By
Lemma 8, the sequence advances by `s`, and by Lemma 10 each application of `s` moves the index
`j ↦ j+1` cyclically, incrementing `k` by one exactly when the index wraps from `m` to `1`.
Starting from index `j`, after exactly `m` applications of `s` the index returns to `j` for the
first time and `k` has increased by exactly `1` (the wrap occurs exactly once in a full cycle of
length `m`). Hence
`a_{n+m} = s^{(m)}(aₙ) = c_j + (k+1)L₀ = aₙ + L₀`.
As `n` was arbitrary, `a_{n+T} = aₙ + L` for all `n ≥ 1`, with `T = m` and `L = L₀`. ∎

This proves the theorem — with explicit `T = |ρ(A)|` and `L = L₀ = ∏_{p∈Π}p`, valid from `n = 1` —
**given the Crux, which is proved unconditionally in §15**. Hence the theorem is proved outright. ∎

---

### 6. Two illustrative cases (sanity, not needed for the proof)

- **Single-prime lock.** If `a₁` is a prime power (`P = {p}`), then `M = p` and every term is a
  multiple of `p` (Lemma 1 with `|P|=1`). Then `𝓐_∞ = {{p}}`, `Π = {p}`, `L₀ = p`, `ρ(A)` is a
  single class, `m = 1`, and `a_{n+1} = aₙ + p` for all `n` (`T=1, L=p`), matching Corollary 11.
- **`a₁ = 105 = 3·5·7`.** Simulation gives `Π = {2,3,5,7}`, `L₀ = 210`, `m = |ρ(A)| = 58`, and
  `a_{n+58} = aₙ + 210` for all `n ≥ 1` — exactly `T = m = 58`, `L = L₀ = 210`, confirming the
  mechanism (and that the period equals `|ρ(A)|`, not merely a multiple).

Both are consistent with §4–§5. (These computations only *illustrate*; the proof above is
self-contained given the Crux.)

---

### 7. Status of the Crux (open gap), with partial progress

The Crux is *finiteness of the ⊆-minimal supports* `𝓐_∞`. Equivalent formulations and reductions
established rigorously this round:

**(a) Reformulation via the small companion.** A support `G = F(a_i)` is ⊆-minimal in `𝓕` iff no
term has support strictly contained in `G`, i.e. `∄ j : F_j ⊊ G`. If `G` contains a large prime
`q` (so `a_i = q·k` with `k = a_i/q`), then a term with support `⊆ G` is either another multiple
of `q` or has support `⊆ F(k)`. Thus a *large-prime* minimal support persists exactly when the
small companion prime-set `F(k)` is never (weakly) refined by a later support. So the Crux is:
"for all but finitely many terms, the small companion prime-set is eventually dominated by some
term's support." (This replaces the *refuted* premise "large primes never appear in supports":
large primes **do** appear, e.g. `a₁ = 385` has `19 ∈ Π`; the claim is that only finitely many
distinct primes appear across all minimal supports.)

**(b) Why the easy structural facts do not suffice.** We have proved (Lemma 4) that `𝓕` is an
*intersecting* family, and (Lemma 1) that every member meets the fixed finite set `P`. **Neither
forces finiteness of `𝓐_∞`:** the family `{ {p*} ∪ S : S ⊆ (large primes), finite }` for a fixed
prime `p*` is intersecting and every member meets `{p*}`, yet has infinitely many ⊆-minimal
elements (all the singletons `{p*}∪{q}` are incomparable). So the Crux genuinely requires the
*dynamics* of the greedy choice, not merely the intersecting/anchor structure. This is the honest
locus of the remaining difficulty.

**(c) Reduction to a fixed anchor prime.** If `𝓐_∞` were infinite, then since each of its members
meets the finite set `P`, by pigeonhole some fixed `p* ∈ P` lies in infinitely many members of
`𝓐_∞`; these form an infinite ⊆-antichain of finite prime-sets all containing `p*`, forcing
infinitely many distinct primes to occur in `𝓐_∞`, hence arbitrarily large primes in minimal
supports. Combined with Lemma 3 (a large shared prime `q` forces its two carrying terms `≥ q/M`
indices apart) and Lemma 2 (linear growth `aₙ ≤ a₁+(n−1)M`), one expects a counting obstruction:
a large prime can divide at most `≈ N/q` of the first `≈ N/M` selected values, so large primes are
"rare," but turning rarity into "a dominating small-only support must eventually appear" is **not
completed here**. This is the open crux.

**Empirical support (not a proof).** Over simulated runs the alphabet `Π` is finite in every case
(`105→{2,3,5,7}`, `385→{2,3,5,7,11,19}`, `1155→{2,3,5,7,11}`, `35→{2,3,5,7}`, `15→{2,3,5}`),
consistent with the Crux; and the resulting `(T,L) = (|ρ(A)|, L₀)` matches the observed period from
`n = 1` in every case, confirming §4–§6.

---

### 8. Round-2 crux-attack skeleton (advance target: prove the Crux)

Goal: prove `𝓐_∞` finite. Argue by contradiction; assume `𝓐_∞` infinite.

**8.1 Anchor collapse (certified §7c, restated).** Each `F ∈ 𝓐_∞` meets `P = primes(a_1)` (L1),
`P` finite ⇒ by pigeonhole a fixed `p* ∈ P` lies in infinitely many members of `𝓐_∞`. These form
an infinite `⊆`-antichain all containing `p*`; being an antichain, they force **infinitely many
distinct primes** into `Π`, so there are arbitrarily large primes `q₁<q₂<…` each in some minimal
support `G_k ∋ p*`, `q_k ∈ G_k`.

**8.2 Structural shape of a large-prime minimal support (from R2 explorers, to be proved).**
Empirically (density explorer, a_1=375: minimal supports {2,3},{3,5},{2,5,19},{3,7,19}) a large
prime never appears as a singleton `{q}` and always paired with a small anchor set. Prove: if
`G ∈ 𝓐_∞` contains a large prime `q > M`, then `G ⊋ {q}` and `G` contains a prime `≤ M`
(indeed `∈ P` via 8.1's p*). — because a bare `{q}` minimal support would make every term meet
`{q}`, i.e. `q | a_n` for all `n`, contradicting L3 (`q ≤ |a_i−a_j|` bounded while indices range
to ∞). So write `G = S ⊔ {q,…}` with `S = G ∩ (small primes)` its **small companion**, `S ≠ ∅`.

**8.3 Minimality ⟺ small companion never activated (certified §7a, sharpened).** `G` is minimal
iff no term has support `⊊ G`. The cheapest way to dominate `G` is a term whose support `⊆ S`
(all prime factors in the small companion). So: `G` persists in `𝓐_∞` **iff no term ever has all
its prime factors inside `S`.**

**8.4 THE HARD STEP (the precise open gap).** Show: for all but finitely many of the `G_k`, a term
with support `⊆ S_k` must eventually appear — contradicting persistence of infinitely many `G_k`.
Equivalent clean statement:
> For every finite nonempty small-prime set `S` that is the companion of some minimal support,
> the greedy sequence eventually produces a term all of whose prime factors lie in `S`.

Why this is the wall (be honest): a "pure-`S`" integer `m` (all prime factors in `S`) is *chosen*
by the greedy rule only if it lands in `A` = meets EVERY minimal support, not just `G`. Meeting
`G` is free (`m` shares `S ⊆ G`); the obstruction is that `m` may fail to meet some OTHER minimal
support `G'` with `S ∩ G' = ∅`. So the difficulty is exactly the **simultaneous** interaction of
all minimal supports — the same reason intersecting-only structure fails (§7b). Candidate handle
to try: use L3 + linear growth to show that once indices exceed `~ max(Π-so-far)`, the constraints
active in any window of length `M` come from a *bounded* number of supports whose companions can
be simultaneously met — i.e. bound the number of *simultaneously active* companions per window
independent of `n`. This per-window independence is the missing quantitative lemma; the density
explorer flags that the naive per-window factor-count bound `log₂(a_n)` grows with `n` and does
NOT close it — a sharper (n-independent) window bound is the concrete thing to prove or refute.

---

## 9. Round-2 progress: three new lemmas and a sharp reduced gap

This round I replace the vague §8.4 "window bound" target with three **rigorously proved,
unconditional, numerically verified** structural lemmas that reduce the Crux to one clean, tight,
well-tested arithmetic inequality. All notation is as in §1–§2: `A = {c ≥ 1 : gcd(c,a_i) > 1 ∀i}`
is the fixed admissible set; `𝓐_∞` is the family of ⊆-minimal prime-supports; a finite prime-set
`B` **meets** a set `G` if `B ∩ G ≠ ∅`, and `B` is a **transversal** of `𝓐_∞` if it meets every
member; a **minimal transversal** is a ⊆-minimal one. Write `∏B := ∏_{p∈B} p` (squarefree radical).

### 9.1 Lemma E1 (Enumeration). `{aₙ : n ≥ 1} = A ∩ [a₁, ∞)`.

*Proof.* **(⊆)** By Lemma 7 every term `a_k ∈ A`, and `a_k ≥ a₁` by strict monotonicity (Lemma 2).
**(⊇)** Let `c ∈ A` with `c ≥ a₁`. Since `aₙ → ∞` (Lemma 2) and `a₁ ≤ c`, the set `{n : aₙ ≤ c}`
is nonempty and finite; let `n` be its largest element, so `aₙ ≤ c` and `a_{n+1} > c`. Suppose for
contradiction `aₙ < c`. Then `c ∈ A` and `c > aₙ`, so by the fixed-successor identity (Lemma 8)
`a_{n+1} = s(aₙ) = min{x ∈ A : x > aₙ} ≤ c`, contradicting `a_{n+1} > c`. Hence `aₙ = c`, so `c`
is a term. ∎

E1 is the decisive new tool: it upgrades "the terms lie in `A`" to "the terms are *exactly* `A`
above `a₁`." In particular, **any integer `m ≥ a₁` with `m ∈ A` is a term `a_l`, and its support
`F(m)` is a genuine member of the support family `𝓕`.** Verified: for `a₁ ∈ {105,375,385,9375,
1155,867,2025}`, every `c ∈ [a₁, a_last]` with `gcd(c,a_i)>1 ∀i` is a term, and conversely.

### 9.2 Lemma E2 (Self-blocking clutter).

> **Realization preliminary.** If a finite prime-set `B` meets every member of `𝓐_∞`, then every
> `m ≥ a₁` with `F(m) = B` lies in `A`, and hence (by E1) is a term with support `B`.

*Proof of preliminary.* For each `j`, `F(a_j)` contains some minimal support `G' ∈ 𝓐_∞` (Lemma 6);
`B` meets `G' ⊆ F(a_j)`, so `F(m) = B` meets `F(a_j)`, i.e. `gcd(m, a_j) > 1`. As `j` was
arbitrary, `m ∈ A`; and `m ≥ a₁`, so E1 makes `m` a term. Concretely `m = (∏B)^k` with `k` large
enough that `m ≥ a₁` has `F(m) = B`, so such a term always exists. ∎

> **Lemma E2 (⇒).** Every `G ∈ 𝓐_∞` is a ⊆-**minimal** transversal of `𝓐_∞` (it meets every
> member of `𝓐_∞`, and no proper subset does).

*Proof.* *Transversal:* `G = F(a_i)` for a term `a_i`; for any `G' ∈ 𝓐_∞` pick a term `a_j` with
`F(a_j) = G'`; then `G ∩ G' = F(a_i) ∩ F(a_j) ≠ ∅` (Lemma 4 if `i ≠ j`; trivial if `i = j`, since
supports are nonempty). *Minimality:* if `B ⊊ G` were a transversal, then `B` is finite (subset of
finite `G`), so by the realization preliminary some term has support `B ⊊ G`, contradicting `G`
⊆-minimal in `𝓕`. ∎

E2(⇒) is the only direction E3 uses. The converse "every **finite** minimal transversal `B` lies
in `𝓐_∞`" also holds (realize `B` as a term by the preliminary; any strictly smaller support would
be a smaller transversal, contradicting minimality of `B`), giving the self-blocking identity
`𝓐_∞ = blocker_fin(𝓐_∞)` on finite sets. *The one point not settled here is that every minimal
transversal is automatically finite; this is folded into the single remaining gap (§9.4) and is
not needed for E3 or the reduction.* Verified for `a₁ ∈ {105,375,385,9375,1155,867,2025}`: the
computed minimal supports coincide exactly with the computed minimal transversals of themselves.

### 9.3 Lemma E3 (Private-witness distance bound). Let `G ∈ 𝓐_∞` and `p ∈ G`. Then there is
`G_p ∈ 𝓐_∞` with `G ∩ G_p = {p}`, and there exist two distinct terms `t, t'` with `F(t) = G`,
`F(t') = G_p`; consequently `gcd(t, t')` is a power of `p`, and

  `p ∣ (t − t')`,  so  `p ≤ |t − t'|`.

*Proof.* By E2, `G` is a minimal transversal, so `G ∖ {p}` is not a transversal: there is
`G_p ∈ 𝓐_∞` with `(G ∖ {p}) ∩ G_p = ∅`. But `G` is a transversal, so `G ∩ G_p ≠ ∅`; combining,
`G ∩ G_p = {p}`. Both `G` and `G_p` are members of `𝓕`, so there are terms `t, t'` with `F(t)=G`,
`F(t')=G_p`; they are distinct since `G ≠ G_p` (as `𝓐_∞` is an antichain). Now `F(t) ∩ F(t') =
G ∩ G_p = {p}`, so the only prime dividing both `t` and `t'` is `p`, i.e. `gcd(t,t') = p^m` for
some `m ≥ 1`. By Lemma 3 (Distance–prime), `p ∣ (t − t')`, and `t ≠ t'` gives `p ≤ |t − t'|`. ∎

E3 verified: for each `a₁` above, every `(G, p)` with `p ∈ G ∈ 𝓐_∞` has a witness `G_p` with
`G ∩ G_p = {p}`.

### 9.4 The reduced Crux (single remaining gap), and its sharp form

Combining E1–E3, the Crux (`𝓐_∞` finite) is **equivalent** to a size bound, because:

- If every prime occurring in a member of `𝓐_∞` is `≤ B` for some bound `B`, then every `G ∈ 𝓐_∞`
  is a subset of the finite set `{primes ≤ B}`, so `𝓐_∞` is finite — the Crux.
- Conversely if `𝓐_∞` is finite then `Π = ⋃𝓐_∞` is a finite prime-set, trivially bounded.

So the Crux is **exactly**: *the primes occurring in ⊆-minimal supports are bounded.* Extensive
simulation pins the sharp bound:

> **Reduced Crux (open).** Every prime occurring in a ⊆-minimal support satisfies `q ≤ a₁`.

**Numerical evidence.** Verified for **all** `a₁` with `4 ≤ a₁ ≤ 139` (exhaustive), and for
`a₁ ∈ {175,225,245,375,385,507,867,1125,1155,1875,2025,2145,2310,3125,9375,15015,…}`. The worst
ratio observed is `q/a₁ = 1.0`, attained only when `a₁` is prime (then `Π = {a₁}`); in every other
case `q < a₁` strictly. Correspondingly `∏_{p∈G} p < 2a₁` for every minimal support `G` (worst
ratio `1.2`). Both bounds are dramatically sharper than any n-dependent count.

**Why E1–E3 are the right handle (and what is missing).** E3 gives `q ≤ |t − t'|`, the distance
between two terms whose supports meet only in `q`. To close the Reduced Crux one must show this
distance is `≤ a₁`, equivalently that **every minimal support is realized among terms whose mutual
distances (for the private-witness pairs) are `≤ a₁`** — i.e. the minimal supports all "form early,"
governed by the seed `a₁`, before the sequence can spread the witness pair by more than `a₁`. E2
shows the abstract combinatorial object is a self-blocking clutter; but self-blocking alone does
**not** force finiteness (infinite self-dual clutters exist abstractly, e.g. incidence clutters of
infinite projective planes), so the finiteness is genuinely arithmetic — it must use E1
(realizability of transversals as actual terms of *this* greedy sequence) together with the
`a₁`-anchored distance control that is not yet proven. This is the honest, precisely located
remaining gap.

**Consistency with recorded refutations.** The Reduced Crux does *not* reintroduce the refuted
`p ∣ L ⇒ p ≤ M` threshold: it bounds primes by `a₁`, not by `M = rad(a₁)`. Indeed `a₁ = 375` gives
`19 ∈ Π` with `19 > M = 15` but `19 < a₁ = 375`; `a₁ = 9375` gives `67 ∈ Π`, `67 > M = 15`,
`67 < a₁`. Large primes above `M` do persist in `L`, exactly as required by the refutation, while
staying `≤ a₁`.

## 11. Round-3 progress: E4 (Size-Bound Reduction) — Crux ⟺ bounded minimal-support size

This round I close the *reduction* one full step further, **rigorously and unconditionally**. The
result replaces the open ERW window inequality of §10 by an equivalent, structurally cleaner target.

Throughout, `𝓐_∞` is the antichain of ⊆-minimal supports; by the **certified** lemma
`enumeration-and-transversal.md` it is *self-blocking*: E2(⇒) every member is a transversal of
`𝓐_∞`, and E2(⇐) every **finite** minimal transversal of `𝓐_∞` is a member. (E2(⇐) is the
realization preliminary + E1: if a finite prime-set `B` meets every member, then `m=(∏B)^k ≥ a₁`
has `F(m)=B` and lies in `A`, so is a term; hence `B∈𝓕`; `B` contains a member `G⊆B` by
Domination; if `B` is a *minimal* transversal then `G=B`, so `B∈𝓐_∞`.) Both directions are used
below and were reviewer-certified in round 2. Self-blocking was re-verified computationally this
round for `a₁∈{15,105,375,385,1155,9375}` (members = minimal transversals, exactly).

### 11.1 A structural sub-lemma

**Lemma 11.0 (Every finite transversal contains a member).** If a finite prime-set `T` meets every
`G∈𝓐_∞`, then `T ⊇ G₀` for some `G₀∈𝓐_∞`.

*Proof.* `T` is a transversal, and it is finite, so among the (finitely many) subsets of `T` that
are transversals — a nonempty collection, since `T` itself is one — pick a ⊆-minimal one, `T'⊆T`.
I claim `T'` is a *globally* minimal transversal. If not, some transversal `T''⊊T'`; but then
`T''⊆T'⊆T` is a transversal contained in `T` and strictly smaller than `T'`, contradicting the
choice of `T'`. So `T'` is a finite minimal transversal, hence `T'∈𝓐_∞` by E2(⇐). Take `G₀=T'`. ∎

### 11.2 The reduction

**Lemma E4 (Size-Bound Reduction).** `𝓐_∞` is finite **iff**
`C := sup_{G∈𝓐_∞} |G| < ∞`. Equivalently, the Crux holds iff the number of distinct primes in a
⊆-minimal support is uniformly bounded.

*Proof.* **(⇒)** If `𝓐_∞` is finite then it has finitely many members, each finite, so
`C = max_{G∈𝓐_∞}|G|` is a finite maximum.

**(⇐)** Assume `|G| ≤ C` for all `G∈𝓐_∞`, and suppose for contradiction `𝓐_∞` is **infinite**. We
build a strictly increasing chain of finite prime-sets `B_1 ⊊ B_2 ⊊ ⋯`, together with infinite
sub-families `𝓗_1 ⊇ 𝓗_2 ⊇ ⋯` of `𝓐_∞`, such that for each `t`:

  (i) every `G∈𝓗_t` satisfies `B_t ⊆ G`;  (ii) `|B_t| = t`;  (iii) `𝓗_t` is infinite.

*Base `t=1`.* By the **Anchor** (`free-lemmas.md`, Lemma 1), every `G∈𝓐_∞` — being `F(a_i)` for a
term `a_i` — meets the fixed finite set `P = F(a₁)`: `G∩P ≠ ∅`. Since `𝓐_∞` is infinite and `P` is
finite, by the **Pigeonhole principle** (`knowledge_base.md`: *Pigeonhole / extremal principle*)
some prime `p_1∈P` lies in infinitely many members. Put `B_1 := {p_1}` and
`𝓗_1 := {G∈𝓐_∞ : p_1∈G}`; then (i)–(iii) hold with `t=1`.

*Inductive step.* Suppose `B_t, 𝓗_t` satisfy (i)–(iii). Consider whether `B_t` is a transversal of
`𝓐_∞` (i.e. meets every member).

- **Case A: `B_t` is a transversal.** By Lemma 11.0 there is a member `G₀∈𝓐_∞` with `G₀⊆B_t`. Every
  `G∈𝓗_t` is a member with `G ⊇ B_t ⊇ G₀`, so `G ⊇ G₀`; since `𝓐_∞` is an **antichain** (its
  members are ⊆-incomparable, being the ⊆-minimal elements of `𝓕`), `G ⊇ G₀` with both members
  forces `G = G₀`. Hence `𝓗_t ⊆ {G₀}` is finite, contradicting (iii). So Case A cannot occur.

- **Case B: `B_t` is not a transversal.** Then some member `W_t∈𝓐_∞` has `W_t ∩ B_t = ∅`. Each
  `G∈𝓗_t` is a member, hence a transversal of `𝓐_∞` by **E2(⇒)**, so `G` meets `W_t`:
  `G ∩ W_t ≠ ∅`. As `G ⊇ B_t` and `W_t ∩ B_t = ∅`, any prime of `G ∩ W_t` lies in `W_t ∖ B_t`.
  Thus every `G∈𝓗_t` contains at least one prime of the finite set `W_t`, all of which avoid `B_t`.
  Since `W_t` is finite and `𝓗_t` is infinite, by the **Pigeonhole principle** some fixed
  `r_t∈W_t` (so `r_t∉B_t`) lies in infinitely many `G∈𝓗_t`. Put
  `B_{t+1} := B_t ∪ {r_t}` and `𝓗_{t+1} := {G∈𝓗_t : r_t∈G}`. Then `|B_{t+1}| = t+1` (as
  `r_t∉B_t`), every `G∈𝓗_{t+1}` contains `B_{t+1}`, and `𝓗_{t+1}` is infinite. This is (i)–(iii)
  for `t+1`.

By induction the chain continues **as long as Case A never occurs**. But Case A was shown
impossible (it contradicts (iii)); so Case B holds at every step and the chain runs for all `t`.
Now invoke the size bound: for `t = C+1`, take any `G∈𝓗_{C+1}` (nonempty by (iii)). By (i)–(ii),
`G ⊇ B_{C+1}` with `|B_{C+1}| = C+1`, so `|G| ≥ C+1 > C`, contradicting `|G| ≤ C`.

This contradiction shows `𝓐_∞` is finite. ∎

**Remarks.**
1. E4 uses *only* certified inputs — E1, E2(⇒), E2(⇐), the Anchor, and the antichain property —
   plus the Pigeonhole principle. It is unconditional and self-contained. In particular it is
   independent of the refuted `M`-threshold and of any `A_n`-only monovariant (the certified
   obstruction in `monovariants-and-obstruction.md` does not apply: that obstruction concerns
   statistics of `A_n`, whereas E4 is a statement about the limiting clutter `𝓐_∞` using E1/E2
   realizability).
2. E4 is *sharp as a reduction*: the argument shows more precisely that **`𝓐_∞` infinite ⟹ minimal
   supports of unbounded size** (an infinite chain `B_t⊆` some member forces members of size `≥t`).
   Conversely bounded size ⟹ finite. Hence the Crux is *equivalent* to the cardinality bound.
3. Why this is progress over R2's `q ≤ a₁`. R2 reduced the Crux to bounding the *magnitude* of
   primes in minimal supports; E4 reduces it to bounding the *number* of primes in a single minimal
   support. These are different quantities: e.g. `a₁=9375` has a prime `67` (large magnitude) yet
   every minimal support has `≤4` primes. The cardinality target is the smaller, more stable one
   numerically (see §11.3) and removes any dependence on the delicate ERW window constant.

### 11.3 Numerical grounding (motivation, not proof)

Simulating the greedy sequence (admissibility `c` ⟺ `F(c)` meets every ⊆-minimal support), running
to `N=1500` terms for `a₁<2000` and `N=4000` otherwise, and computing the *stabilized* minimal
supports `𝓐_∞`, `Π=⋃𝓐_∞`, and the ERW window `K = max_{q∈Π} (t_q − a₁)/M` where `t_q` is the first
term divisible by `q`:

```
a1=6    M=6    |Pi|=1 maxq=2  maxMemberSize=1  worstERW_K=0.000
a1=15   M=15   |Pi|=3 maxq=5  maxMemberSize=2  worstERW_K=0.200
a1=35   M=35   |Pi|=4 maxq=7  maxMemberSize=3  worstERW_K=0.200
a1=105  M=105  |Pi|=4 maxq=7  maxMemberSize=3  worstERW_K=0.029
a1=375  M=15   |Pi|=5 maxq=19 maxMemberSize=3  worstERW_K=0.333
a1=385  M=385  |Pi|=6 maxq=19 maxMemberSize=3  worstERW_K=0.036
a1=867  M=51   |Pi|=1 maxq=3  maxMemberSize=1  worstERW_K=0.000
a1=1155 M=1155 |Pi|=5 maxq=11 maxMemberSize=4  worstERW_K=0.003
a1=2025 M=15   |Pi|=4 maxq=7  maxMemberSize=3  worstERW_K=0.333
a1=9375 M=15   |Pi|=5 maxq=67 maxMemberSize=4  worstERW_K=0.333
```

Two facts are numerically robust: **(a)** `max|G| ≤ 4` on every seed (E4's target quantity is very
small), and **(b)** the ERW window constant satisfies `K ≤ 1/3`, confirming the outline-reviewer's
`K ≤ 0.33` across its 8 seeds (`19` on `a₁=375` and `67` on `a₁=9375` both first divide a term at
value `a₁+5`, i.e. `K = 5/15 = 1/3`). Both are consistent with — and motivate — E4, but **neither
is a proof** of the cardinality bound. The number `1/3` is exhibited as evidence only.

### 11.4 The single remaining gap (honest)

> **E5 (Cardinality bound — OPEN).** There is an `a₁`-computable constant `C` with `|G| ≤ C` for
> every ⊆-minimal support `G∈𝓐_∞`.

By E4, E5 ⟹ Crux ⟹ (via §4–§5) the theorem, from `n=1`, with `T=|ρ(A)|`, `L=∏Π`. E5 is the only
unproved step in this approach.

**What is and is not available for E5.** *Available:* by E3, each `p∈G` has a private witness
`H_p∈𝓐_∞` with `G∩H_p={p}`, so a minimal support of size `r` comes with `r` pairwise-distinct
partner members; and E2(⇐) realizes any finite transversal as a term. *The wall:* neither of these
bounds `r` — an abstract self-blocking clutter with a finite transversal *can* have members of
unbounded size (the reduction E4 is tight in that abstract sense), so E5 must use the **arithmetic**
of the greedy sequence (realizability + growth `a_n=Θ(n)` + `gcd` distance, `free-lemmas.md`),
not merely the clutter structure. Concretely: a minimal support `G` of large size `r` is realized
by a term `t` with `F(t)=G`, so `t ≥ ∏G ≥ p_1⋯p_r` (product of the `r` smallest primes,
super-exponential in `r`); the `r` private witnesses `H_{p}` force, via E3 and Lemma 3, `r` distinct
"only-shared-prime" term pairs. Turning "`G` large ⟹ its realizing/witness terms are forced into a
configuration the greedy rule cannot produce" into a bound on `r` is the missing quantitative step —
the same locus flagged in §8.4/§10, now aimed at *support cardinality* rather than prime magnitude
or formation time. This is stated as an explicit **GAP**, not claimed.

**Spec note (none).** No spec-level problem found; the reduction is internally consistent and the
endgame (§4–§5) is certified.

## 12. Round-4 progress: the realizer-value pincer — E5 fully reduced to one window inequality, one regime closed

This round I execute the **aimo-0447 distinctness pincer** on the *value* of the smallest term
realizing a minimal support, as the outline-reviewer directed. The outcome is: (i) two new rigorous,
unconditional lemmas that turn E5 into a single clean **product-window inequality**; (ii) a
**complete** proof of E5 for the *entire* subclass of minimal supports with `∏G < a₁` (the
"small-product" regime); and (iii) a sharp, honestly-flagged residual — E5 for supports with
`∏G ≥ a₁` — reduced to proving `∏(G∖{p_max}) < a₁`, with the pincer setup laid out. No overclaim:
the residual is stated as an explicit GAP.

Notation: for a finite prime-set `G` write `∏G := ∏_{p∈G} p` (its squarefree radical). For `r ≥ 0`
let `P_r := ∏_{i=1}^{r} p_i` be the `r`-th **primorial** (`P_0 = 1`, `P_1 = 2`, `P_2 = 6`,
`P_3 = 30`, `P_4 = 210`, `P_5 = 2310`, `P_6 = 30030`, …). For `X > 1` set
`K(X) := max{ r ≥ 0 : P_r < X }`, a finite `a₁`-computable integer.

### 12.1 Realization lemma (unconditional)

**Lemma R1 (Every `G`-supported integer `≥ a₁` is a term).** Let `G ∈ 𝓐_∞` be a minimal support.
Then every integer `m ≥ a₁` with `F(m) = G` is a term of the sequence. Consequently the set
`D_G := { m ≥ 1 : F(m) = G }` (integers with prime support *exactly* `G`) satisfies
`D_G ∩ [a₁, ∞) ⊆ {a_n}`, and the smallest term realizing `G` is

  `u(G) := min{ m ∈ D_G : m ≥ a₁ }`,  which exists and equals `∏G` whenever `∏G ≥ a₁`.

*Proof.* By **E2(⇒)** (`enumeration-and-transversal.md`, certified) every member of `𝓐_∞` is a
transversal of `𝓐_∞`; in particular `G` meets every `G' ∈ 𝓐_∞`. If `F(m) = G` then `F(m)` meets
every member of `𝓐_∞`, i.e. `m ∈ A` (the fixed admissible set of §2). Since `m ≥ a₁`, **E1**
(`{a_n} = A ∩ [a₁,∞)`, certified) makes `m` a term. This proves the first claim.

The elements of `D_G` are exactly the integers `∏_{p∈G} p^{e_p}` with all `e_p ≥ 1`; the least of
them is `∏G` (take all `e_p = 1`), and `D_G` is unbounded, so `D_G ∩ [a₁,∞)` is a nonempty set of
positive integers and has a least element `u(G)`. If `∏G ≥ a₁` then `∏G` itself is the least element
of `D_G`, hence `u(G) = ∏G`. ∎

`u(G)` is the "realizing term value" of the pincer. Its **lower bound** is immediate:

**Lemma R2 (Product lower bound = primorial bound).** For every finite prime-set `G`,
`u(G) ≥ ∏G ≥ P_{|G|}`. Hence if `u(G) < X` (equivalently, if `∏G < X`) for some bound `X`, then
`|G| ≤ K(X)`.

*Proof.* `u(G) ∈ D_G` is divisible by every prime of `G`, so `u(G) ≥ ∏_{p∈G} p = ∏G`. Writing the
`|G|` distinct primes of `G` in increasing order `q_1 < q_2 < ⋯ < q_{|G|}`, the `i`-th smallest
prime overall `p_i` satisfies `p_i ≤ q_i` (there are at least `i` primes `≤ q_i`, namely
`q_1,…,q_i`), so `∏G = ∏_i q_i ≥ ∏_i p_i = P_{|G|}`. If `∏G < X` then `P_{|G|} < X`, so by definition
of `K`, `|G| ≤ K(X)`. ∎

This is exactly the aimo-0447 "line value `≥` product of distinct primes on it" move (crux corpus
`aimo-0447`, `size-bounding-and-descent`): a support of `r` distinct primes forces its realizing
value to be `≥ P_r`, super-exponential in `r`. The pincer is completed by an **`a₁`-only upper
bound** on `u(G)` (equivalently on `∏G`).

### 12.2 The small-product regime is completely closed

**Proposition 12.A (E5 for `∏G < a₁`).** Every minimal support `G ∈ 𝓐_∞` with `∏G < a₁` satisfies
`|G| ≤ K(a₁)`.

*Proof.* Immediate from Lemma R2 with `X = a₁`: `∏G < a₁ ⟹ P_{|G|} < a₁ ⟹ |G| ≤ K(a₁)`. ∎

This is a genuine, unconditional bound on an infinite subclass of minimal supports, with no open
step. It already disposes of every "small" support; the entire remaining difficulty is concentrated
in supports whose *radical* reaches or exceeds `a₁`.

### 12.3 E5 reduced to a single window inequality

Define the two "reduced products" of a minimal support `G` with `|G| ≥ 2`:
`redMin(G) := ∏(G ∖ {p_min})` and `redMax(G) := ∏(G ∖ {p_max})`, where `p_min, p_max` are the
smallest and largest primes of `G`. Since `p_min ≤ p_max`, always `redMax(G) ≤ redMin(G) ≤ ∏G`.

**Proposition 12.B (Reduction of E5 to a window inequality).** Suppose the following holds:

> **(W)** Every minimal support `G ∈ 𝓐_∞` with `|G| ≥ 2` satisfies `redMax(G) = ∏(G∖{p_max}) < a₁`.

Then `sup_{G∈𝓐_∞} |G| ≤ 1 + K(a₁) < ∞`, i.e. **E5 holds**, and hence (by the certified E4 and
§4–§5) the full theorem holds for all `n ≥ 1` with `T = |ρ(A)|`, `L = ∏Π`.

*Proof.* Take any `G ∈ 𝓐_∞`. If `|G| ≤ 1` then `|G| ≤ 1 + K(a₁)` trivially. If `|G| ≥ 2`, apply (W):
the set `G ∖ {p_max}` consists of `|G| − 1` distinct primes with product `redMax(G) < a₁`. By the
primorial estimate in Lemma R2 (applied to the prime-set `G∖{p_max}`),
`P_{|G|−1} ≤ ∏(G∖{p_max}) = redMax(G) < a₁`, so `|G| − 1 ≤ K(a₁)`, i.e. `|G| ≤ 1 + K(a₁)`. As `G`
was arbitrary, `sup_{G∈𝓐_∞}|G| ≤ 1 + K(a₁)`. E4 (`size-bound-reduction.md`, certified) then gives
`𝓐_∞` finite (the Crux), and §4–§5 give the theorem. ∎

Two further facts sharpen the status of (W):

**(W) holds automatically whenever `∏G < a₁`.** Indeed then `redMax(G) ≤ ∏G < a₁`. So by
Proposition 12.A the reduction is only *needed*, and (W) is only *unproved*, in the regime
`∏G ≥ a₁`. Equivalently, the sole open content of E5 is:

> **Residual gap E5″ (OPEN).** Every minimal support `G` with `∏G ≥ a₁` satisfies
> `∏(G ∖ {p_max}) < a₁` — equivalently, its largest prime obeys `p_max(G) > ∏G / a₁`.

The stronger, cleaner sufficient form (also open, and matching the reviewer's R2 phrasing and the
aimo-0447 window `[a₁, 2a₁)`) is:

> **Window form E5-★ (OPEN, ⟹ E5″).** Every minimal support `G` satisfies `∏G < 2a₁`; equivalently
> `u(G) < 2a₁` when `∏G ≥ a₁`. [`∏G < 2a₁ ⟹ redMax(G) = ∏G/p_max ≤ ∏G/2 < a₁ ⟹` (W).]

**Numerical status (motivation, not proof).** Over a broad seed scan (all the seeds of §11.3 plus
`a₁ ∈ {507, 899, 1875, 2145, 2310, 255255, 4849845}` and 40 random seeds in `[4, 3000]`), for every
minimal support `G`:
`∏G / a₁ ≤ 1.449` (worst at `a₁ = 899`, `G = {2,3,7,31}`, `∏G = 1302`), `redMin/a₁ ≤ 0.725`,
`redMax/a₁ ≤ 0.725`, and every prime of every minimal support is `≤ a₁` (equality only when `a₁` is
prime). So (W), E5″, and E5-★ all hold with wide margin on all tested data, and `∏G < 2a₁` is very
robust. These are exhibited as evidence only; none is proved.

### 12.4 The pincer setup toward E5″ (what is available, and the precise wall)

Fix a minimal support `G` with `∏G ≥ a₁`; then by Lemma R1 the value `u(G) = ∏G` is a genuine
term `a_i`. The upper half of the aimo-0447 pincer needs an `a₁`-only ceiling on `u(G) = ∏G`.
The certified machinery supplies the following *forced structure* around this term:

- **`|G|` private witnesses (E3).** For each `p ∈ G` there is `H_p ∈ 𝓐_∞` with `G ∩ H_p = {p}`; the
  `H_p` are pairwise distinct members. Each `H_p` is realized by a term `t_p` with `F(t_p) = H_p`
  (Lemma R1), and since `F(a_i) = G` and `F(t_p) = H_p` meet only in `p`, `gcd(a_i, t_p) = p^{m}`.
  By the certified Distance–prime lemma, `p ∣ (a_i − t_p)`, so `a_i ≡ t_p (mod p)` for every `p∈G`.
- **No bare large-prime support (minimality).** For `p = p_max`, the witness `H_{p_max}` cannot be
  `{p_max}` (else `{p_max} ⊊ G` would be a member, contradicting `G` minimal, `|G|≥2`); so
  `H_{p_max}` carries a prime `r ∉ G`.
- **Growth / gap control.** `a_{n+1} − a_n ≤ M = rad(a₁)` and `a_n = Θ(n)` (`free-lemmas.md`), so
  the term `a_i = ∏G` has index `i ≤ 1 + (∏G − a₁)/1` and the terms in any value-window of length
  `M` number `≤ M`.

**The precise wall (honest).** The lower bound `u(G) ≥ ∏G ≥ P_{|G|}` (Lemma R2) is one jaw of the
pincer. The missing jaw is an **`a₁`-only upper bound on `u(G) = ∏G`**. The aimo-0447 template
obtains its upper bound from a *fixed* ambient interval length `N` that a family of distinct large
primes must all fit inside (a prime `> N` hits a length-`N` interval at most once, forcing the
primes distinct and their product `≤` the interval value). In the present 1-D greedy setting the
analogue of `N` would be a *value-window* `[a₁, U(a₁)]` inside which the realizing term `u(G)` is
forced to appear; but nothing proved so far pins `u(G)` (equivalently the *first* `G`-supported
integer `≥ a₁`) below an `a₁`-only ceiling once `∏G ≥ a₁`. Concretely, the natural attempt — "if
`∏(G∖{p_max}) ≥ a₁` then the proper sub-support `S = G∖{p_max}` (of radical `≥ a₁`) should be
realized as a term, contradicting minimality" — **fails at exactly one step**: `S` is a proper
subset of the minimal transversal `G`, hence is **not** a transversal, so by the private witness
`H_{p_max}` (with `H_{p_max} ∩ S = ∅`) the `S`-supported integer `∏S ∉ A`, and is therefore *not*
a term. Minimality of `G` is precisely the obstruction that prevents cheaply realizing the smaller
support and closing the pincer. Turning "`∏G ≥ a₁` with all of `G∖{p_max}` also large" into a
contradiction with the greedy dynamics (realizability of *some* competing smaller-support term
inside the window, via the witnesses `H_p` and the gap bound) is the single remaining quantitative
step. This is stated as an explicit **GAP (E5″)**, not claimed.

**Net effect of Round 4.** E5 is now reduced, unconditionally, to the single inequality (W)
(sharpest form E5″: `∏(G∖{p_max}) < a₁` for minimal `G` with `∏G ≥ a₁`); the complementary regime
`∏G < a₁` is fully closed (Proposition 12.A) with the explicit bound `|G| ≤ K(a₁)`; and the whole
of E5 is bounded by `1 + K(a₁)` once (W) is supplied. This is strictly sharper than R3's "bound
`|G|`" — the target is now a concrete product-window inequality with the aimo-0447 pincer's lower
jaw already in hand.

## 13. Round-5 consolidation: certified reduction chain, two-anchor scaffold, and the honest wall

This round adds **no new closing lever** for E5″ — none exists among the levers explored (the
outline-reviewer kept this approach live as certified furthest-forward, and both R5 explorers
returned NEGATIVE). The purpose of this section is to (13.1) state the full certified reduction
chain and the single open gap cleanly in one place; (13.2) record the *auxiliary* two-anchor witness
scaffold (genuinely new forced structure, but not a closer of E5″); and (13.3) record honestly why
every R5 attempt on E5″ forks to a certified-dead or R4-forbidden move.

### 13.1 The certified reduction chain (one place)

Every link below is proved in full in this file and reviewer-certified in `lemmas/`; only the final
arrow `E5″ ⟹ E5` remains open. `𝓐_∞` = ⊆-minimal prime-supports of `𝓕 = {F(a_n)}`;
`Π = ⋃𝓐_∞`; `P = F(a₁)`; `M = rad(a₁)`; `∏G` = radical of `G`; `P_r` = `r`-th primorial;
`K(X) = max{r : P_r < X}`.

| Step | Statement | Where | Certified |
|------|-----------|-------|-----------|
| No-transient | `a_k ∈ A` ∀k and `a_{n+1} = s(a_n)` ∀`n ≥ 1` (fixed successor on fixed `A`) | §2, L7–L8 | `no-transient-fixed-successor.md` |
| Endgame | `Π` finite ⟹ `A` periodic mod `∏Π` ⟹ `a_{n+T} = a_n + L`, `T=|ρ(A)|`, `L=∏Π`, **∀ `n≥1`** | §4–§5 | (same) |
| E1 | `{a_n} = A ∩ [a₁,∞)` | §9.1 | `enumeration-and-transversal.md` |
| E2 | Each `G∈𝓐_∞` is a ⊆-minimal transversal of `𝓐_∞` (self-blocking, both directions on finite sets) | §9.2 | (same) |
| E3 | Each `p∈G∈𝓐_∞` has a private witness `H_p∈𝓐_∞`, `G∩H_p={p}`, giving terms with `gcd=p^m`, `p≤|t−t'|` | §9.3 | (same) |
| **Crux** | `𝓐_∞` finite (⟺ `Π` finite) | §3 | — (target) |
| E4 | Crux ⟺ `sup_{G∈𝓐_∞}|G| < ∞` (cardinality bound) | §11.2 | `size-bound-reduction.md` |
| R1 | `m ≥ a₁`, `F(m)=G∈𝓐_∞` ⟹ `m` is a term; `u(G)=∏G` when `∏G≥a₁` | §12.1 | `realizer-value-pincer.md` |
| R2 | `u(G) ≥ ∏G ≥ P_{|G|}`; `∏G < X ⟹ |G| ≤ K(X)` | §12.1 | (same) |
| Prop 12.A | **`∏G < a₁` ⟹ `|G| ≤ K(a₁)`** (small-radical regime fully closed) | §12.2 | (same) |
| Prop 12.B | window (W): `∏(G∖{p_max}) < a₁` ∀ minimal `G` ⟹ `sup|G| ≤ 1+K(a₁)` ⟹ E5 ⟹ theorem | §12.3 | (same) |
| **E5″** | minimal `G` with `∏G ≥ a₁` has `∏(G∖{p_max}) < a₁` (equiv. `p_max > ∏G/a₁`; suff. `∏G < 2a₁`) | §12.3 | **OPEN** |

The whole theorem is thus **certified-equivalent to E5″** (a single product-window inequality on the
large-radical minimal supports), with the complementary regime `∏G < a₁` unconditionally closed and
the pincer's lower jaw in hand. This is the furthest-forward state of the entire population.

### 13.2 Auxiliary structure: the two-anchor witness scaffold

The following is genuinely new forced structure around a hypothetical infinite `𝓐_∞`. It is
**not** a proof of E5″ — it is recorded as reusable scaffolding for the §12 pincer and cross-links
the sibling slug `realizer-index-joint-double-count`, whose steps 1–4 build the same object. Every
step below uses only certified inputs (Anchor, Pigeonhole, E3, R1, Distance–prime).

**Scaffold (S1: anchored blow-up).** Suppose, for contradiction toward the Crux, that `𝓐_∞` is
infinite. By E4 (contrapositive) the sizes `|G|` are unbounded, and — as in the E4 chain-descent
(§11.2) — by the **Anchor** (`free-lemmas.md`, L1) every `G∈𝓐_∞` meets the finite set `P`, so by the
**Pigeonhole principle** (`knowledge_base.md`) a fixed `p* ∈ P` lies in infinitely many members.
Among these one extracts a strictly `⊆`-increasing sequence is *not* needed; what the pincer uses is
a sequence `G_1, G_2, … ∈ 𝓐_∞` with `p* ∈ G_k` for all `k` and `q_k := p_max(G_k) → ∞` (possible
because infinitely many members contain `p*` yet, being an antichain, cannot all lie in a fixed
finite prime-set, so their largest primes are unbounded).

**Scaffold (S2: the second anchor `p**`).** Fix `k` with `q_k > max P` (so `q_k ∉ P` and
`q_k ≠ p*`). By **E3** applied to `p = q_k ∈ G_k`, there is a private witness `H_k ∈ 𝓐_∞` with
`G_k ∩ H_k = {q_k}`. Since `p* ∈ G_k` and `p* ≠ q_k`, we get `p* ∉ H_k`. But `H_k ∈ 𝓐_∞` is itself a
support, so by the **Anchor** `H_k ∩ P ≠ ∅`; as `p* ∉ H_k`, the witness carries a prime
`p'_k ∈ P ∖ {p*}`. The set `P ∖ {p*}` is finite, so by the **Pigeonhole principle** (over the
infinitely many admissible `k`) some fixed `p** ∈ P ∖ {p*}` satisfies `p** ∈ H_k` for infinitely
many `k`. Passing to that subsequence: for all `k`,

  `p* ∈ G_k`,  `p** ∈ H_k`,  `p** ≠ p*`,  `q_k ∈ G_k ∩ H_k`,  `G_k ∩ H_k = {q_k}`,  `q_k → ∞`.

Thus **a large prime's private witness is forced onto a *second* fixed `a₁`-anchor** `p**` — the
"two-anchor separation" of the witness pair. (This is the sibling scaffold's step 3, re-derived here
from the same certified lemmas; it requires `|P| ≥ 2`, i.e. `a₁` not a prime power — the prime-power
case is already closed, §6 single-prime-lock, where `𝓐_∞ = {{p}}` is finite outright.)

**Scaffold (S3: the realized witness pair).** By **R1** both supports are realized at their radicals:
`t_k := u(G_k) = ∏G_k` and `t'_k := u(H_k) = ∏H_k` are genuine terms (each has radical `≥ a₁` once
`q_k` is large, since `q_k ∣ ∏G_k` and `q_k ∣ ∏H_k`, and if the radical were `< a₁` the support would
be in the closed regime — but keep the two regimes separate: this scaffold is deployed only when the
radicals reach `a₁`). Their supports meet only in `q_k`, so `gcd(t_k, t'_k) = q_k^{m}`, and by the
**Distance–prime** lemma (L3) `q_k ∣ (t_k − t'_k)`, whence

  `|t_k − t'_k| ≥ q_k → ∞`.   (♦)

**Why the scaffold does not close E5″ (honest).** The pincer would close if (♦) could be
*contradicted* by an `a₁`-only **upper** bound on `|t_k − t'_k|`. It cannot, by the following
unique-factorization fact (the sibling's "Lemma J is illusory" finding, recorded here). Factor out
the shared prime:

  `t_k = ∏G_k = q_k · A_k`,  `t'_k = ∏H_k = q_k · B_k`,  where  `A_k = ∏(G_k∖{q_k})`,  `B_k = ∏(H_k∖{q_k})`.

Because `G_k ∩ H_k = {q_k}`, the prime-sets `G_k∖{q_k}` and `H_k∖{q_k}` are **disjoint**, so
`A_k ≠ B_k` (unique factorization), giving `|A_k − B_k| ≥ 1` and hence

  `t_k − t'_k = q_k · (A_k − B_k)`  is a **forced nonzero multiple of `q_k`**.

Therefore any purported upper bound `|t_k − t'_k| ≤ C(a₁)` **immediately implies** `q_k ≤ C(a₁)` —
i.e. the "bound the spread" target is *exactly* the magnitude bound `q ≤ C(a₁)` it was meant to
reduce to, with no decoupling. The two-anchor congruence (`t_k ≡ 0 mod p*`, `t'_k ≡ 0 mod p**`) adds
constraints on the *endpoints* but supplies no mechanism forcing the *difference* small while `q_k`
is large. So the scaffold sharpens the forced configuration but leaves E5″ open. It is recorded as
reusable structure (a certifiable two-anchor separation lemma), **not** as a closer.

### 13.3 The wall, restated honestly (R5 negative findings)

Every non-forbidden avenue examined this round terminates at the same obstruction:

1. **Formation-window / growth route** (explorer `formation-window`). To bound the index of the term
   `t = ∏G` one must rule out that a smaller competing value in `(a_{i-1}, t)` — in particular `∏S`
   for `S = G∖{p_max}` when `∏S ≥ a₁` — was selected first. Ruling that out requires exhibiting an
   *already-realized* member disjoint from `S` by that index, which is either (a) the **R4-forbidden**
   "realize a proper sub-support to contradict minimality" move, or (b) an unresolved *simultaneous*
   timing claim about when all members of `𝓐_∞` form relative to each other (the "simultaneous
   interaction of all supports" difficulty open since §7b/§8.4). No window/growth argument avoids the
   fork.

2. **Density / covering route** (explorer `covering-density`). A raw density-of-`A` argument is the
   **certified dead end** `monovariants-and-obstruction.md`: the obstruction family
   `G_k = {p*, q_k}`, `q_k → ∞`, keeps `density(A_n) → 1/p* > 0` with `Π` infinite, so no
   `A_n`-statistic distinguishes finite from infinite `Π`. The aimo-0447 grid-covering mechanism has
   no *upper*-bound analogue here (its natural output is the already-certified lower jaw R1/R2), and
   the aimo-0421 fiber dichotomy is empirically one-sided (every recruited prime has positive-density
   fiber). A methodological caution recorded: the set of primes dividing *some* term is provably
   unbounded (≈639 primes by term 6000 for `a₁=375`), so any argument must operate on `𝓐_∞` via
   E1/E2 realizability, never on raw term divisors.

3. **Joint-spread double-count** (sibling `realizer-index-joint-double-count`, Lemma J). Illusory, by
   the `t_k − t'_k = q_k(A_k − B_k)` factorization in §13.2 — equivalent to the magnitude bound.

**Numerical sharpening surfaced (conjecture only, unproved).** Across 772 large-regime minimal
supports (16 curated + 25 random seeds, `a₁ ≤ 5000`), **every** `G` with `∏G ≥ a₁` has **at most one
prime exceeding `√a₁`**. This would give E5″ together with a primorial bound on the remaining primes,
and is offered as possible material for a *different* top-level framing — but no proof route was found
that avoids the forbidden sub-support move (it is a sharper *restatement* of the wall, not a bypass).
Recorded as CONJECTURE, not used.

**Spec note (none).** No spec-level problem found. The reduction chain (§13.1) is internally
consistent, every link but `E5″ ⟹ E5` is certified, and the endgame (§4–§5) delivers the exact
periodicity the problem asks (`a_{n+T} = a_n + L`, from `n = 1`). Status remains **partial**; E5″ is
the single, honestly flagged open gap.

## 14. Round-6 consolidation: the reduction chain verified link-by-link, and the impossibility map around E5″

This round adds **no new closing lever** for E5″ (none appeared: the outline-reviewer kept this
approach LIVE as certified furthest-forward, and the round's one new pole `joint-recruitment-budget`
was vetted HARD and *proven to fork* — see §14.2). The purpose here is purely **consolidation**, as
the gate directed: (14.1) verify, link-by-link with explicit certification location, that the *whole
theorem* `a_{n+T} = a_n + L (∀ n ≥ 1)` follows from the single open inequality E5″, so that E5″ is
the sole remaining step and nothing else is assumed; (14.2) cross-link this round's new negative
guardrail — the **Rejection-Budget Dichotomy** — into the growing impossibility map around E5″,
alongside the R4 Collapse and R5 JSC guardrails; and (14.3) state E5″ cleanly and honestly as the
single open gap, with no overclaim. Status stays **partial**.

### 14.1 The reduction chain is airtight and self-contained (E5″ ⟹ theorem)

I trace the implication `E5″ ⟹ (whole theorem)` through every intermediate link, naming the lemma
and its certification file at each step, and checking that no step assumes anything beyond its stated
hypothesis. All objects are as in §1–§2: `A = {c ≥ 1 : gcd(c,a_i) > 1 ∀i}`; `𝓐_∞` = the ⊆-minimal
elements of `𝓕 = {F(a_n)}`; `Π = ⋃𝓐_∞`; `P = F(a₁)`; `M = rad(a₁)`; `∏G` = the squarefree radical
of `G`; `P_r` = `r`-th primorial; `K(X) = max{r ≥ 0 : P_r < X}`.

Assume **E5″**: *every minimal support `G ∈ 𝓐_∞` with `∏G ≥ a₁` satisfies `∏(G∖{p_max}) < a₁`.*

1. **E5″ ⟹ (W) for all minimal supports.** (W) is: every `G ∈ 𝓐_∞` with `|G| ≥ 2` has
   `redMax(G) := ∏(G∖{p_max}) < a₁`. Split on the radical of `G`:
   - If `∏G < a₁`, then `redMax(G) = ∏(G∖{p_max}) ≤ ∏G < a₁` (dropping a prime only shrinks the
     product), so (W) holds **unconditionally**, with no appeal to E5″.
   - If `∏G ≥ a₁`, then E5″ gives `redMax(G) < a₁` directly.
   Both regimes are covered and disjoint, so (W) holds for every minimal `G` with `|G| ≥ 2`. *(This
   is exactly the "(W) holds automatically whenever `∏G < a₁`" observation of §12.3, made explicit as
   the case-split that fuses Prop 12.A's regime with E5″'s regime into the single hypothesis of
   Prop 12.B.)*

2. **(W) ⟹ E5 (bounded cardinality), via Prop 12.B.** By **Proposition 12.B** (§12.3, certified
   `realizer-value-pincer.md`): if every minimal `G` satisfies `redMax(G) < a₁`, then for `|G| ≥ 2`
   the prime-set `G∖{p_max}` has `|G|−1` distinct primes with product `< a₁`, so by the primorial
   bound **R2** (§12.1, same file) `P_{|G|−1} ≤ ∏(G∖{p_max}) < a₁`, giving `|G|−1 ≤ K(a₁)`, i.e.
   `|G| ≤ 1 + K(a₁)`; for `|G| ≤ 1` this is trivial. Hence `sup_{G∈𝓐_∞} |G| ≤ 1 + K(a₁) < ∞`. This is
   exactly **E5** (§11.4). *(Prop 12.B is a certified unconditional implication; it needs only (W),
   which step 1 supplied from E5″.)*

3. **E5 ⟹ Crux (`𝓐_∞` finite), via E4.** By **E4 (Size-Bound Reduction)** (§11.2, certified
   `size-bound-reduction.md`): `𝓐_∞` is finite **iff** `sup_{G∈𝓐_∞} |G| < ∞`. Step 2 gives the
   right-hand side, so `𝓐_∞` is finite — the **Crux (Finite Alphabet)** (§3). Equivalently
   `Π = ⋃𝓐_∞` is a finite set of primes. *(E4 is a certified equivalence proved by the Pigeonhole
   chain-descent of §11.2 from certified E1/E2/Anchor/antichain; step 2 supplies its hypothesis.)*

4. **Crux ⟹ theorem (from `n = 1`), via the certified endgame.** Set `L₀ := ∏Π` (finite by step 3,
   `≥ 2` since some member is nonempty). By **Lemma 9** (§4) `A` is a union of residue classes
   mod `L₀`; by **Lemma 10** (§5) the successor map `s` on `A` is a cyclic shift through the `m :=
   |ρ(A)|` residues of `A` mod `L₀`; and by the **no-transient identity** **L7–L8** (§2, certified
   `no-transient-fixed-successor.md`) the sequence *is* the forward `s`-orbit from `a₁`
   (`a_{n+1} = s(a_n)` for **all** `n ≥ 1`, and `a_n ∈ A` for all `n`). **Corollary 11** (§5) then
   gives `a_{n+T} = a_n + L` for **every** `n ≥ 1`, with `T = m = |ρ(A)|` and `L = L₀ = ∏Π`. *(No
   separate "eventual ⇒ all n" step is needed — that is the entire point of the certified L7–L8; the
   endgame consumes only the finiteness of `Π` from step 3.)*

Chaining 1→2→3→4: **E5″ implies the full theorem `a_{n+T} = a_n + L (∀ n ≥ 1)`** with the explicit
`T = |ρ(A)|`, `L = ∏Π`. Every arrow `1,2,3,4` is proved in this file and reviewer-certified in the
named `lemmas/` file; the *only* unproved statement in the entire deduction is the hypothesis **E5″**
itself. There is no hidden lemma, no circularity (the endgame §4–§5 uses only the finiteness of `Π`,
never E5″ or E4, and E4/12.B/R2 use only E1/E2/Anchor/antichain/primorial arithmetic — all certified
independently of the endgame), and the two radical-regimes of step 1 are exhaustive and disjoint. So:

> **The whole theorem is reduced to E5″ alone.** Proving E5″ (a single `a₁`-only product-window
> inequality on the large-radical minimal supports) completes the entire proof; nothing else is open.

*(Direction note, for honesty: what is certified is the **sufficiency** `E5″ ⟹ theorem`. The reverse
`theorem ⟹ E5″` is not needed and is not claimed — E5″ is a concrete sharp inequality, whereas the
weaker certified equivalences `Crux ⟺ E4 ⟺ sup|G|<∞` (steps 3) hold in both directions. The run's
progress metric is that the sole open arrow is now this single inequality, with its complementary
regime `∏G < a₁` unconditionally closed by Prop 12.A and the pincer's primorial lower jaw R2 in hand.)*

### 14.2 The impossibility map around E5″ — cross-linking the new Rejection-Budget guardrail

Six rounds have now certified a family of **negative guardrails**, each proving that a specific class
of lever cannot close E5″. This round's pole `joint-recruitment-budget` contributes the last one. I
record them here in one place so no future round re-opens an exhausted lever (cf. the run-state Rules):

| Guardrail | Lever it kills | Mechanism | Where |
|-----------|----------------|-----------|-------|
| **R4 Collapse** | "realize a proper sub-support `S ⊊ G` as a term to contradict `G`'s minimality" | `S` is not a transversal (private witness `H_{p_max}` with `H_{p_max} ∩ S = ∅` blocks it, E3), so `∏S ∉ A`, so `∏S` is not a term; any per-anchor descent reproduces the E4 chain-descent verbatim | `anchor-partition.md` (certified R4) |
| **R5 JSC** | "bound the private-witness spread `\|t−t'\|` from above by `C(a₁)`" | `t = q·A`, `t' = q·B` with `A,B` products over **disjoint** prime sets (`G∩H={q}`), so `A ≠ B`, `t−t' = q(A−B)`, `\|A−B\| ≥ 1`; hence `\|t−t'\| ≤ C(a₁)` **is** `q ≤ C(a₁)` — the magnitude bound in disguise, no decoupling | `two-anchor-scaffold.md` (certified R5), §13.2 |
| **R2 obstruction** | "certify `Π` finite by a monovariant/statistic of the admissible set `A_n` alone" | the anchored family `G_k = {p*, q_k}`, `q_k → ∞`, keeps every `A_n`-statistic frozen (`density(A_n) → 1/p* > 0`, `max-gap → p*`) while `Π` is infinite | `monovariants-and-obstruction.md` (certified R2) |
| **R6 Rejection-Budget Dichotomy** *(NEW this round)* | "get a contradiction from disjoint per-recruit cost sets `C_q` drawn from the greedy rejection stream, with `\|C_q\| → ∞` vs. an `O(N)` budget" | see below | *pending certification in the sibling's* `lemmas/` *(outline-reviewer report §2); cross-linked here* |

**The Rejection-Budget Dichotomy (§14.2, cross-link — sibling deliverable, stated for completeness).**
For each greedy step let `R_n = {c : a_n < c < a_{n+1}}` be the rejected candidates; by the certified
Gap bound L2 (`free-lemmas.md`, each gap `≤ M`) the cumulative rejection stream up to `N` has size
`Σ_{n<N}|R_n| = a_N − a₁ − (N−1) = Φ_N ≤ (M−1)(N−1) = O(N)`. A recruitment-accounting proof of
`𝓐_∞` finite would attach to each newly-recruited large prime `q` a **disjoint** cost set
`C_q ⊆` (the rejection stream) with `|C_q| ≥ c_q → ∞`, and derive a contradiction "infinitely many
recruits, each costing `→ ∞`, vs. an `O(N)` budget." The dichotomy shows this is **impossible**:

- Because the `C_q` are *disjoint* subsets of the size-`Φ_N` stream, they **automatically** satisfy
  `Σ_k |C_{q_k}| ≤ Φ_N = O(N)` — a **tautology**, not a contradiction (one cannot pack disjoint
  subsets of an `S`-element set to total size `> S`). So step 5's contradiction is *unreachable*
  unless `c_q → ∞` is forced by something other than "these are actual disjoint rejections." Two
  horns, both dead:
  - **Horn A (local cost).** If `C_q` is drawn from a bounded-length (`≤ M`) window around the
    recruit's realizer `∏G_q`, then `|C_q| ≤ M − 1` is **bounded** — cannot `→ ∞`. Fails outright.
  - **Horn B (global cost).** To get `|C_q| → ∞` the cost must span `Ω(q)` of the number line (reach
    across `[t'_k, t_k]`, length `≥ q_k` by the two-anchor scaffold §13.2). Then either (i) disjointness
    makes the budget inequality a tautology — large per-recruit cost just means recruits are sparse,
    fully **consistent** with `Π` infinite; or (ii) forcing a contradiction requires bounding
    `t_k − t'_k ≤ f(a₁)`, which is **exactly the JSC spread bound**, certified dead (R5, above).
  - **Vocabulary variant.** Pairing each recruit `q` with its small-prime part `B` (`∏B < a₁` by
    E5″, so `B` ranges over a finite set) and pigeonholing an infinite common-core family lands on the
    **anchor-partition common core**, whose forcing is the **R4 Collapse** theorem (dead).

Thus every route to a disjoint cost `c_q → ∞` from the `O(N)` rejection budget forks into
Φ_N/density (Horn A degenerate), JSC-spread (Horn B), or Collapse (vocabulary). **No escape.** This
closes the last unexhausted *joint-accounting* thread (opening 5) the same way JSC/Collapse closed
the spread and sub-support levers. *(The write-up and its numerics — `a₁ ∈ {375,385,867,105}`,
`N = 400`, `Φ_N` exactly `= a_N − a₁ − (N−1)` with each gap `≤ M` — are the sibling pole's certified
deliverable; recorded here only as a cross-linked guardrail. This approach does **not** attempt the
budget lever.)*

**Consequence for the field.** With this round's guardrail, all three top-level route families named
in the R6 mandate are exhausted: route (ii) direct-periodicity and (iii) alt-reduction both provably
re-derive the certified Reduction-Lemma equivalence (and the "converse gap — `A` periodic mod `K`
while `Π` infinite" was proven non-existent via E3/TAS), and route (i) joint-potential has all five
openings certified forked (1/2/4 = density/JSC/Φ_N, 3 = anchor-partition, 5 = Rejection-Budget). The
impossibility map is now near-complete: **every lever bounding a single-support / pair / disjoint-cost
quantity to close E5″ is certified dead.** E5″ must be attacked with genuinely new *arithmetic* input
(the surviving intuition: E1-realizability + growth forcing an arithmetic collision the non-realizable
star family `{p*,q_k}` evades — but concretely, not as any bounded quantity), or via a literature
match for the finite-alphabet statement. This is surfaced to the orchestrator as a hard plateau, not
a bypass to be attempted with another disguised single-quantity lever.

### 14.3 The single open gap, stated cleanly

> **E5″ (OPEN — the sole remaining step).** Every ⊆-minimal support `G ∈ 𝓐_∞` with `∏G ≥ a₁`
> satisfies `∏(G ∖ {p_max}) < a₁`; equivalently `p_max(G) > ∏G / a₁`. (A sufficient cleaner form,
> also open: `∏G < 2a₁` for every minimal `G`.)

By §14.1 this single inequality implies the whole theorem. The complementary regime `∏G < a₁` is
unconditionally closed (Prop 12.A, `|G| ≤ K(a₁)`); the pincer's primorial lower jaw `∏G ≥ P_{|G|}`
(R2) is in hand; and every known lever for the missing upper jaw is certified-forked (§14.2). No new
sub-result was proved this round (consolidation only); no claim in §14 is asserted beyond the
certified chain and the recorded guardrails.

**Spec note (none).** No spec-level problem found. The chain §14.1 is exhaustive, disjoint in its
case-split, and self-contained modulo E5″; the endgame §4–§5 delivers exactly the periodicity the
problem asks. Status remains **partial**; E5″ is the single, honestly flagged open gap.

## Promotable lemmas

**Round 6 (consolidation) added no new promotable lemma of its own** — it verified the existing
certified chain link-by-link (§14.1) and cross-linked the sibling pole's **Rejection-Budget
Dichotomy** guardrail (§14.2), which is the *sibling's* deliverable (`joint-recruitment-budget`) for
the reviewer to certify into `lemmas/`, not a result of this approach. The lemmas below are the
already-proven (prior-round) reusable results.

The following were proved in full in prior rounds (unconditionally, i.e. **not** assuming the Crux)
and are reusable across approaches:

- **Two-anchor witness scaffold (S2) [NEW, round 5].** If `a₁` is not a prime power and `𝓐_∞` is
  infinite, then for a sequence `G_k ∈ 𝓐_∞` with a fixed anchor `p* ∈ G_k` and `q_k = p_max(G_k) →
  ∞`, the E3 private witnesses `H_k` (with `G_k ∩ H_k = {q_k}`) can be taken, after passing to a
  subsequence, to all contain a *second* fixed anchor `p** ∈ P∖{p*}`. Proof (§13.2): E3 + Anchor +
  Pigeonhole over the finite set `P∖{p*}`. This is genuinely new reusable structure (a two-anchor
  separation of the witness pair); it does **not** by itself close E5″. *(Proposed for certification
  as auxiliary structure; the accompanying §13.2 unique-factorization observation
  `t_k − t'_k = q_k(A_k − B_k)` is the GUARDRAIL showing any "bound the witness-pair spread" plan is
  the magnitude bound in disguise — companion to the R4 Collapse guardrail.)*

- **R1 (Realization of `G`-supported integers) [NEW, round 4].** For a minimal support `G ∈ 𝓐_∞`,
  every integer `m ≥ a₁` with `F(m) = G` is a term of the sequence; hence the smallest term
  realizing `G` is `u(G) = min{ m : F(m)=G, m ≥ a₁ }`, and `u(G) = ∏G` whenever `∏G ≥ a₁`. Proof
  (§12.1): certified E2(⇒) makes `G` a transversal, so `F(m)=G` meets every member, `m∈A`; E1 makes
  `m` a term. *(Proposed for certification.)*
- **R2 (Primorial support bound) [NEW, round 4].** For any finite prime-set `G`,
  `u(G) ≥ ∏G ≥ P_{|G|}` (`P_r` = `r`-th primorial); hence `∏G < X ⟹ |G| ≤ K(X) := max{r : P_r<X}`.
  Proof (§12.1): `u(G)` divisible by all of `G`, and `i`-th smallest prime of `G` is `≥ p_i`.
  *(Proposed for certification.)*
- **Proposition 12.A (E5 for small-radical supports) [NEW, round 4].** Every minimal support with
  `∏G < a₁` has `|G| ≤ K(a₁)`. Unconditional; §12.2.
- **Proposition 12.B (E5 reduced to a window inequality) [NEW, round 4].** If every minimal support
  satisfies `∏(G∖{p_max}) < a₁` (equivalently `∏G < 2a₁` suffices), then `sup_{G∈𝓐_∞}|G| ≤ 1+K(a₁)`,
  i.e. E5 (hence the theorem) holds. Unconditional reduction; §12.3. *(Proposed for certification.)*
- **E4 (Size-Bound Reduction) [NEW, round 3].** `𝓐_∞` is finite **iff**
  `sup_{G∈𝓐_∞}|G| < ∞`. Proof: §11.2, via Lemma 11.0 (every finite transversal contains a member)
  and a Pigeonhole chain-descent, using certified E1, E2(⇒), E2(⇐), the Anchor, and the antichain
  property — no arithmetic beyond those. Transplantable: it reduces the Finite-Alphabet crux, for
  **any** approach, from bounding the primes to bounding the *number of prime factors of a minimal
  support*. Numerically `max|G|≤4` on all tested seeds. *(Proposed for certification;
  a standalone statement is written to `results/imo-2026-06/lemmas/size-bound-reduction.md`.)*

- **L4 (Pairwise-intersecting supports).** For all `i ≠ j`, `gcd(a_i, a_j) > 1`. *(Immediate from
  the defining property with the smaller index; §1 Lemma 4.)*
- **L7+L8 (No-transient / fixed-successor identity).** Let `A := {c : c meets every ⊆-minimal
  support of 𝓕}` and `s(x) := min{c ∈ A : c > x}`. Then **every** term satisfies `a_k ∈ A`, and
  `a_{n+1} = s(aₙ)` for **all** `n ≥ 1`. In particular, once `A` is known to be eventually
  periodic (a union of residues mod some `L`), exact periodicity `a_{n+T} = aₙ + L` holds from
  `n = 1` with `T = |ρ(A)|` and `L` the period of `A` — **no separate reversibility or
  stabilization argument is required.** *(§2 Lemmas 6–8, §4–§5.)* This is the key transplantable
  result: it collapses the usual "eventual periodicity ⇒ all `n`" difficulty to nothing, for any
  approach that establishes finiteness of the support alphabet by any route.
- **L1 (Anchor), L2 (Gap bound), L3 (Distance–prime).** Standard; proved in §1.
- **E1 (Enumeration).** `{aₙ : n ≥ 1} = A ∩ [a₁, ∞)`: the sequence is *exactly* the elements of the
  fixed admissible set `A = {c ≥ 1 : gcd(c,a_i) > 1 ∀i}` that are `≥ a₁`, listed in increasing
  order. Hence any `m ≥ a₁` with `m ∈ A` is a term, and `F(m)` is a genuine support. *(§9.1;
  unconditional, from L7+L8.)* Transplantable to any approach reasoning about which integers occur.
- **E2(⇒) (Supports are minimal transversals).** Every `G ∈ 𝓐_∞` meets every member of `𝓐_∞` and
  no proper subset does — i.e. each minimal support is a ⊆-minimal transversal (self-blocking, ⇒
  direction). *(§9.2; unconditional.)*
- **E3 (Private-witness distance).** For every prime `p` in a minimal support `G` there is
  `G_p ∈ 𝓐_∞` with `G ∩ G_p = {p}`, yielding two terms `t, t'` with `gcd(t,t') = p^m` and
  `p ≤ |t − t'|`. *(§9.3; unconditional, from E2(⇒) + L3.)* Reduces the Finite-Alphabet crux to an
  `a₁`-anchored bound on these witness distances.

---

## 10. Round-3 build target — close §9.4 via the Early-Recruitment-Window (choice-reading)

**Sharpened sub-target (the only thing to prove; everything else in this file is complete):**

> **(ERW) Early Recruitment Window.** There is an `a₁`-computable constant `K` such that every
> prime `q ∈ Π = ⋃𝓐_∞` divides some term `a_l` with `a_l ≤ a₁ + K·M`. Equivalently: no prime first
> introduced into a term's support *after* the window `[a₁, a₁+K·M]` ever survives into a
> ⊆-minimal support.

**Why (ERW) closes the whole problem.** The integers in `[a₁, a₁+K·M]` are finite in number, so the
set of primes dividing any of them is finite; (ERW) puts `Π` inside that finite set, giving the Crux
(Finite Alphabet) and hence the theorem via §4–§5 (`T=|ρ(A)|`, `L=∏Π`). This *replaces* the size
bound `q ≤ a₁` by a **window/formation** target — a genuinely different top-level statement (the
selection explorer's finding), provable by bounded computation rather than an asymptotic size
estimate.

**Choice-reading mechanism (this is the new lever — it reads which terms actually form, via E1, not
just the abstract clutter).** Combine E3 with E1:
- (a) **Witness-pair localization.** For `q ∈ G ∈ 𝓐_∞`, E3 gives the private witness `G_q` and two
  realized terms `t` (support `G`), `t'` (support `G_q`) with `gcd(t,t')=q^m`, so `q ≤ |t−t'|`. The
  reduced target is: **the CLOSEST realized witness pair `(t,t')` has `|t−t'| ≤ K·M`.** Reading the
  choices: by E1, `A ∩ [a₁,∞)` is *exactly* the term set, and multiples of `q` in `A` recur; take
  `t,t'` to be the two *smallest* terms `≥ a₁` carrying supports `G,G_q`. Bound their separation.
- (b) **First-formation bound.** The smallest integer `≥ a₁` with support exactly a transversal `B`
  lies in `A` (E2 realization preliminary) and is a term (E1). Its value is controlled by `∏B` and
  `a₁`: the least `m ≥ a₁` with `F(m)=B` satisfies `m < a₁ + ∏B` (a multiple of `∏B` occurs in any
  window of length `∏B`; a squarefree such multiple with support exactly `B` occurs by the gap
  bound). So a support `B` with `∏B` small forms early; the content of (ERW) is that a **minimal**
  support cannot have `∏B` large, because a large `∏B` forces its private-witness partner far away,
  and E1 would then have produced a *smaller-support* term in between (violating minimality) — the
  closure of the loop is the open step.

**Precise open gap (§9.4, restated as the ERW inequality).** Prove the constant `K` exists, i.e.
that the closest E3 witness pair for every minimal support satisfies `|t−t'| ≤ K·M`. Selection
explorer data: the persistent large prime is recruited at term-index `3` (value `a₁+5`) in both
converged cases `a₁∈{375,9375}`, and the last new minimal support first occurs at a term
`≤ 1.8·a₁` across all tested seeds — strong evidence `K` is a small absolute constant (`≈2`).

**Candidate finish (to try; flag if it stalls).** Suppose `q ∈ G ∈ 𝓐_∞` with `q` large. Consider
the first term `a_l` divisible by `q`. If `a_l > a₁+K·M`, then in the window `(a_{l-1}, a_l]` the
greedy rule chose a `q`-multiple over the (present, by L2) next multiple of `M`; that choice was
forced because `M`'s multiple failed some minimal support `G'` — but `G'` with `F(G') ∌` the small
part means `G'` itself is a support with smaller product realized earlier, letting E1/E2 dominate
`G` and contradict minimality. Turning this local exchange argument into the uniform bound `K` is
the missing quantitative step (the same §8.4 per-window-independence fact, now aimed at *formation
time* rather than *alphabet size*).

**Watch out for (do not repeat recorded errors):**
- Do NOT bound `q` by `M=rad(a₁)`; the target is a window `K·M` giving `q ≤ K·M`, but the *primes*
  themselves may exceed `M` (a₁=375 has `19∈Π`, `19>15=M`). The window bounds *formation time*, and
  `q ≤ |t−t'| ≤ K·M` is consistent with `q>M` only if `K>1` — so state `K` honestly (`K≈2`), not
  `K=1`. (For `a₁=375`, `19 ≤ K·M = K·15` needs `K ≥ 2`.)
- Selection explorer S1: greedy *order* adds nothing beyond E1 — do NOT attempt a
  "minimality-forces-small-`q`" argument in the naive form; the lever is *formation time via E1
  realizability*, not pre-emption.
- Selection explorer S3: track domination **per small-companion-set `S`** (a `{S}`-support term
  kills every `{S,q}` at once), not per prime `q` — fewer distinct `S` to bound.

---

## 15. Round-7: closing the Crux directly — the fresh-prime Rescale-Witness

This section **proves the Crux (`𝓐_∞` finite, equivalently `Π` finite) unconditionally**, closing the
sole open gap and completing the theorem. It uses only the certified free lemmas **L1–L4**
(`free-lemmas.md`) and the greedy definition of the sequence; it does **not** invoke E2/E3/E4 or the
E5″ radical machinery (those are legacy infrastructure, left intact but unused here). Notation is as in
§1: `F(x)` is the set of primes dividing `x`, `F_n=F(a_n)`, `𝓕={F_n:n≥1}`, and `𝓐_∞` is the family of
`⊆`-minimal elements of `𝓕`. Recall `(★)`: `a_{n+1}` is the least integer `> a_n` that is admissible
at stage `n`, i.e. the least `c>a_n` with `gcd(c,a_i)>1` for all `i≤n`.

### 15.1 Forward-realizability

**Lemma 15.1 (Forward-realizability).** Let `c` be an integer with `c > a₁`. Then `c` is a term of the
sequence **iff** `gcd(c,a_i) > 1` for every term `a_i` with `a_i < c` (equivalently `F(c)∩F(a_i)≠∅`
for every earlier-valued term).

*Proof.* **(⇒)** Suppose `c = a_m` is a term; since `c > a₁`, `m ≥ 2`. Let `a_i` be any term with
`a_i < c = a_m`. By strict monotonicity of the sequence (part of the definition, cf. L2), `a_i < a_m`
forces `i < m`. Then `i ≤ m-1`, and the defining clause with index `i` in the construction of
`a_m = a_{(m-1)+1}` requires `gcd(a_m, a_i) > 1` (this is exactly L4 for the pair `i<m`). Hence
`gcd(c,a_i) > 1`.

**(⇐)** Suppose `c > a₁` and `gcd(c,a_i) > 1` for every term `a_i < c`. Because `a_n → ∞` (L2, linear
growth) and `a₁ < c`, the set `{k ≥ 1 : a_k < c}` is nonempty (it contains `k=1`) and finite; let `n`
be its maximum. Then

  `a_n < c ≤ a_{n+1}`   (the right inequality because `n+1 ∉ {k : a_k < c}`).

By strict monotonicity the terms `< c` are precisely `a_1, …, a_n`. By hypothesis `gcd(c,a_i) > 1` for
each `i ≤ n`, so `c` is **admissible at stage `n`**; and `c > a_n`. By `(★)`, `a_{n+1}` is the *least*
integer that is `> a_n` and admissible at stage `n`, so `a_{n+1} ≤ c`. Combined with `c ≤ a_{n+1}` this
gives `c = a_{n+1}`, a term. ∎

This is a purely local, per-candidate realizability criterion: to certify that `c` is a term one only
checks the finitely many, *already-emitted* terms below `c`. It never requires `c` to meet the whole
family `𝓐_∞`. This is the precise feature that keeps the argument off the R4-Collapse guardrail
(which concerned realizing a common core of an infinite sub-family as a global transversal).

### 15.2 Key terms, domination, and `𝓐_∞ ⊆ {key supports}`

**Definition.** A term `a_n` is a **key term** if no earlier term dominates its support, i.e. there is
no index `j < n` with `F(a_j) ⊆ F(a_n)`. The first term `a₁` is a key term (there is no earlier term).

**Lemma 15.2a (Domination).** For every term `a_i` there is a key term `a_{j₀}` with `j₀ ≤ i` and
`F(a_{j₀}) ⊆ F(a_i)`.

*Proof.* The set `J := {j ≤ i : F(a_j) ⊆ F(a_i)}` is nonempty (`i ∈ J`). Let `j₀ := min J`. If
`a_{j₀}` were not a key term, some `j' < j₀` would satisfy `F(a_{j'}) ⊆ F(a_{j₀})`; combined with
`F(a_{j₀}) ⊆ F(a_i)` this gives `F(a_{j'}) ⊆ F(a_i)`, so `j' ∈ J` with `j' < j₀`, contradicting
minimality of `j₀`. Hence `a_{j₀}` is a key term with `F(a_{j₀}) ⊆ F(a_i)`. ∎

*(Consequence: the "no earlier term" and "no earlier key term" versions of the key-term definition
coincide. If no earlier key term dominates `a_n` but some earlier term `a_j` (`j<n`) does, apply
Lemma 15.2a to `a_j`: it yields a key term `a_{j₀}`, `j₀ ≤ j < n`, with `F(a_{j₀}) ⊆ F(a_j) ⊆ F(a_n)`,
an earlier key term dominating `a_n` — contradiction. So the definitions agree.)*

**Lemma 15.2b (`𝓐_∞ ⊆ {key supports}`).** Every `G ∈ 𝓐_∞` equals `F(a_n)` for some key term `a_n`.

*Proof.* Let `G ∈ 𝓐_∞`. Since `G ∈ 𝓕`, some term has support `G`; let `a_n` be the *earliest* such
term. Suppose `a_n` is not a key term: some `j < n` has `F(a_j) ⊆ F(a_n) = G`. As `F(a_j) ∈ 𝓕` and `G`
is `⊆`-minimal in `𝓕`, `F(a_j) ⊆ G` forces `F(a_j) = G`. But then `a_j` is a term with support `G` and
`j < n`, contradicting the choice of `a_n` as earliest. Hence `a_n` is a key term with `F(a_n)=G`. ∎

Thus `Π = ⋃_{G∈𝓐_∞} G ⊆ ⋃_{\text{key terms }b} F(b)`. Consequently, **if the set of distinct key
supports `{F(b) : b \text{ key term}}` is finite, then `𝓐_∞` is finite and `Π` is finite** — the Crux.
(We do not need the reverse inclusion `{key supports} ⊆ 𝓐_∞`; only 15.2b is used.)

### 15.3 The Rescale-Witness Lemma

Fix `Q := P = F(a₁)` (nonempty since `a₁ > 1`) and `q₀ := max Q`, a prime dividing `a₁`, so
`q₀ ≤ a₁`. Define the threshold

  `C := q₀ · a₁`.

**Definition.** A prime `p` is **fresh at** a key term `x` if `p ∈ F(x)` and `p ∉ F(b)` for every key
term `b` occurring strictly earlier than `x`.

**Lemma 15.3 (Rescale-Witness).** No key term `x` with `x > C` has a prime that is fresh at `x`.

*Proof.* Suppose, for contradiction, that `x = a_N` is a key term, `x > C`, and `p ∈ F(x)` is fresh at
`x`. We derive a contradiction in four steps.

**(i) An anchor prime `q ∈ F(x)∩Q`, `q ≠ p`, `q ≤ q₀`.** Since `q₀ ≥ 2` we have
`x > C = q₀a₁ ≥ 2a₁ > a₁`, so `N ≥ 2` and `a₁` is a key term occurring strictly earlier than `x`.
Freshness of `p` gives `p ∉ F(a₁) = Q`. By L4 (pairwise-intersecting), `gcd(x,a₁) > 1`, i.e.
`F(x)∩Q ≠ ∅`; pick `q ∈ F(x)∩Q`. Since `q ∈ Q` and `p ∉ Q`, `q ≠ p`; and `q ∈ Q` gives `q ≤ q₀`
(maximality of `q₀`) and `q ∣ a₁`, so `q ≤ a₁`. Put

  `S := F(x) ∖ {p}`.

Then `q ∈ S` (as `q ∈ F(x)`, `q ≠ p`), so `S ≠ ∅`, and `S ⊊ F(x)` (since `p ∈ F(x) ∖ S`). *(This
disposes of the `|F(x)|=1` case: if `F(x)={p}` then `F(x)∩Q=∅`, contradicting L4; so a fresh-prime key
term automatically has `|F(x)| ≥ 2` and the anchor `q` exists.)*

**(ii) The witness `y`: `a₁ ≤ y < x` and `F(y) = S`.** Let `r := ∏_{s∈S} s` (a squarefree integer,
the product of the distinct primes of `S`), so `F(r) = S`. Two cases.

- *Case `r ≥ a₁`.* Set `y := r`. Then `a₁ ≤ y` and `F(y) = S`. Since `S ⊊ F(x)` with
  `F(x) ∖ S = {p}`, we have `r = ∏S = (∏F(x))/p < ∏F(x)`. The distinct primes dividing `x` have
  squarefree product `∏F(x)` dividing `x`, so `∏F(x) ≤ x`; hence `y = r < ∏F(x) ≤ x`. Thus
  `a₁ ≤ y < x`.

- *Case `r < a₁`.* Since `q ∈ S`, `q ∣ r` and `q ≥ 2`. Let `t` be the least nonnegative integer with
  `r·q^t ≥ a₁`; as `r < a₁`, `t ≥ 1`. Set `y := r·q^t`. By minimality of `t`, `r·q^{t-1} < a₁`, so

    `y = q·(r·q^{t-1}) < q·a₁ ≤ q₀·a₁ = C < x`.

  Also `y = r·q^t ≥ a₁`, and `F(y) = F(r) ∪ F(q^t) = S ∪ {q} = S` (as `q ∈ S`). Thus `a₁ ≤ y < C < x`.

In both cases `a₁ ≤ y < x` and `F(y) = S ⊊ F(x)`. (The threshold `C` is used precisely to force
`y < x` in the second case, via `y < C < x`; in the first case `y < x` is automatic. The lift is by
powers of the *known small anchor prime* `q ≤ q₀`, adding no new prime to the support — it is a
multiplicative rescaling, not a magnitude/spread inequality.)

**(iii) `y` meets every term below it (the local realizability step).** We claim `gcd(y, a_i) > 1`,
i.e. `F(a_i) ∩ S ≠ ∅`, for every term `a_i` with `a_i < y`. Fix such a term `a_i`. Since `a_i < y < x
= a_N` and the sequence is strictly increasing, `i < N`. By Domination (Lemma 15.2a) there is a **key
term** `a_{j₀}` with `j₀ ≤ i < N` and `F(a_{j₀}) ⊆ F(a_i)`; so `a_{j₀}` occurs strictly earlier than
`x`. Now:

  • By L4, `gcd(a_{j₀}, x) > 1` (distinct indices `j₀ < N`), so `F(a_{j₀}) ∩ F(x) ≠ ∅`; pick a prime
    `w ∈ F(a_{j₀}) ∩ F(x)`.
  • Since `a_{j₀}` is a key term strictly earlier than `x` and `p` is fresh at `x`, `p ∉ F(a_{j₀})`;
    hence `w ≠ p`. Therefore `w ∈ F(x) ∖ {p} = S`.
  • Also `w ∈ F(a_{j₀}) ⊆ F(a_i)`.

So `w ∈ F(a_i) ∩ S`, giving `F(a_i) ∩ S ≠ ∅`, i.e. `gcd(y,a_i) > 1` (as `F(y) = S`). This is where
freshness is load-bearing and where `p_max` would fail: for a *non-key* earlier term `a_i` the only
prime it shares with `x` could be `p` itself, but the dominating key term `a_{j₀}` cannot contain the
fresh `p`, so its shared prime with `x` is a genuine element of `S`. (Freshness is essential and is
exactly what `p_max` lacks: by E3, `p_max` has a private-witness *key term* sharing only `p_max` with
`F(x)`, so removing `p_max` would leave that witness unmet — the certified R5/JSC obstruction. The
fresh prime has, by definition, no such earlier key witness.)

**(iv) Contradiction.** By (ii), `y ≥ a₁`. If `y = a₁`, then `y` is the term `a₁` itself. If `y > a₁`,
then by (iii) `y` meets every term below it, so by Forward-realizability (Lemma 15.1) `y` is a term.
Either way `y` is a term; write `y = a_m`. Since `y < x = a_N`, monotonicity gives `m < N`. But then
`a_m` is a term with `m < N` and `F(a_m) = S ⊊ F(x)`, i.e. `F(a_m) ⊆ F(x)` with `m < N` — an earlier
term dominating `F(x)`. This contradicts `x = a_N` being a **key term**. ∎

### 15.4 Threshold finiteness ⇒ the Crux

Since `a_n → ∞` (L2), only finitely many terms lie in `[a₁, C]`; a fortiori only finitely many **key
terms** are `≤ C`. Define the finite prime set

  `K := ⋃ { F(b) : b \text{ a key term}, b ≤ C }`

(a finite union of finite sets).

**Claim.** Every key term `b` satisfies `F(b) ⊆ K`.

*Proof.* Suppose not. Among the key terms whose support is not contained in `K` — a nonempty set of
terms, hence of indices — let `x = a_N` be the one of **least index**. If `x ≤ C` then `F(x) ⊆ K` by
the definition of `K`, contradicting `F(x) ⊄ K`; hence `x > C`. Pick a prime `p ∈ F(x) ∖ K`. Let `b`
be any key term occurring strictly earlier than `x`. If `b ≤ C` then `F(b) ⊆ K`, so `p ∉ F(b)`. If
`b > C` then, `b` being a key term of index smaller than `x`'s, the minimality of `x` forces
`F(b) ⊆ K`, so again `p ∉ F(b)`. In every case `p ∉ F(b)`; thus `p` is in no key term earlier than
`x`, i.e. `p` is **fresh at `x`**. So `x` is a key term `> C` with a fresh prime `p ∈ F(x)`,
contradicting the Rescale-Witness Lemma 15.3. This proves the Claim. ∎

Therefore every key support is a subset of the finite set `K`, so the collection of distinct key
supports is contained in the finite power set `2^K` and has at most `2^{|K|}` elements — in particular
it is **finite**. By Lemma 15.2b, `𝓐_∞ ⊆ {key supports}`, so `𝓐_∞` is finite, and hence
`Π = ⋃_{G∈𝓐_∞} G ⊆ K` is a finite set of primes.

> **Crux (Finite Alphabet) — PROVED.** `𝓐_∞` is finite; equivalently `Π` is a finite set of primes. ∎

### 15.5 Conclusion: the theorem

With the Crux established unconditionally, §4–§5 apply verbatim: `L₀ := ∏_{p∈Π} p` is a well-defined
positive integer, `A` is a union of residue classes mod `L₀` (Lemma 9), the successor map `s` acts on
the finite residue set `ρ(A)` as a cyclic shift with a single wrap per cycle (Lemma 10), and therefore
(Corollary 11)

  `a_{n+T} = a_n + L`  for **every** `n ≥ 1`,  with  `T = |ρ(A)|`,  `L = L₀ = ∏_{p∈Π} p`.

This is the required conclusion, with the period `T` and increment `L` given explicitly and valid from
`n = 1`. The theorem is proved. `∎`

*(Edge cases, subsumed by the general argument. If `a₁` is a prime power, `P = {q₀}`; by L1 every term
is divisible by `q₀`, so `F(a₁) = {q₀} ⊆ F(a_n)` for all `n`, making `a₁` the unique key term,
`K = {q₀}`, `𝓐_∞ = {{q₀}}`, `Π = {q₀}`, `L = q₀`, `T = 1` — the fresh-prime hypothesis never fires.
If a putative fresh-prime key term had `|F(x)| = 1`, step (i) shows L4 already forbids it. No case is
left open.)*

### 15.6 Verification

The construction was re-checked by independent greedy simulation for
`a₁ ∈ {375, 385, 105, 9, 49}`: in every run all key terms are `≤ C = q₀a₁` (e.g. `a₁=375`: `q₀=5`,
`C=1875`, largest key term `490`), the union of all key-term supports equals the pool `K` of
key-primes below `C` exactly, and for `a₁ = 375` this pool is `{2,3,5,7,19}` — the prime factors of the
run's independently certified increment `L = 3990 = 2·3·5·7·19`. This corroborates §15.3–§15.5 (it is
evidence, not part of the proof; the proof above is self-contained).

---

## Promotable lemmas

Proved in full this round (§15), reusable and worth certifying into `results/imo-2026-06/lemmas/`
(the sibling slug `key-term-first-appearance` uses the identical core):

- **Forward-realizability (Lemma 15.1).** For `c > a₁`, `c` is a term ⟺ `gcd(c, a_i) > 1` for every
  term `a_i < c`. Proved directly from the greedy definition `(★)` (no dependence on E1/global `A`).
  Location: §15.1.
- **Domination (Lemma 15.2a).** Every term's support contains `F(b)` for some key term `b` of index
  `≤ i` (`a_n` key ⟺ no earlier term's support `⊆ F(a_n)`). Location: §15.2. Corollary: the
  "no earlier term" and "no earlier key term" key-definitions coincide; and `𝓐_∞ ⊆ {key supports}`
  (Lemma 15.2b).
- **Rescale-Witness / Fresh-Prime Lemma (Lemma 15.3).** With `q₀ = max P(a₁)` (prime) and
  `C = q₀·a₁`, no key term `x > C` has a prime fresh at `x` (fresh = in no earlier key term). Proof:
  the local witness `y = ∏(F(x)∖{p})·q^t ∈ [a₁, C)`, `q ∈ F(x)∩P(a₁)∖{p}`, is a term (meets all terms
  `< y` via Domination-to-a-key-term + L4 + freshness) with support `⊊ F(x)`, contradicting `x` key.
  Location: §15.3. This is the load-bearing lever; the FRESH-vs-`p_max` distinction and the
  local-meet vs global-transversal distinction are the two guardrail-critical points (both spelled out
  in §15.3(iii)).
- **Threshold finiteness ⇒ Crux (§15.4).** All key supports `⊆ K := ⋃{F(b): b key, b≤C}`, finite;
  hence `𝓐_∞` finite, `Π` finite. Closes the Crux and thereby the whole theorem.

## Spec concerns
None. The theorem needs no external answer (`answer_type` is the structural conclusion
`a_{n+T}=a_n+L`); `T=|ρ(A)|` and `L=∏_{p∈Π}p` are given explicitly and verified against the certified
`a₁=375` value `L=3990`. The §15 argument is self-contained on certified L1–L4 + the greedy definition
and does not reopen or depend on the retired E5″/p_max chain.
