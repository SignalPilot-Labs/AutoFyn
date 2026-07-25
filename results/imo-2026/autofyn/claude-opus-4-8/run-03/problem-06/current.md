# imo-2026-06 — tracking

## Status
solved

The Finite-Alphabet crux — the sole open gap after a 6-round plateau — is now **proved
unconditionally** by the **fresh-prime Rescale-Witness** lever. TWO independent approaches closed
it this round and were both verified by the reviewer:

- `key-term-first-appearance` (APPROVE) — a fully self-contained proof via a dynamic
  first-occurrence "key-term filter"; imports only the certified free lemmas L1–L4 and re-derives
  forward-admissibility, domination, the rescale-witness, key-term finiteness, and the full
  periodicity endgame from scratch. This is the canonical Full proof recorded below.
- `redundant-constraint-antichain` (APPROVE) — its new §15 proves the same Crux directly and feeds
  the previously-certified §4–§5 (`A`-residue) endgame. Independent confirmation of the same lever.

The load-bearing lever (re-derived from scratch, not cited): a **key term** `x` above the threshold
`C = q₀·a₁` (`q₀ = max P(a₁)`) cannot carry a **fresh** prime `p` (one absent from every earlier key
term). Removing `p` and rescaling by a small anchor prime `q ∈ P(x)∩P(a₁)∖{p}` yields a genuine
**earlier** term `y ∈ [a₁, C)` with support `P(x)∖{p} ⊊ P(x)`, dominating `x` — contradicting `x`
being key. The witness `y` is realized *locally* (it need only meet the finitely many terms already
emitted below it, via forward-admissibility + domination + freshness), so the argument stays off the
certified R4-Collapse guardrail; and the removed prime is **fresh, never `p_max`**, so it stays off
the certified R5-JSC/E3 obstruction. Hence only finitely many primes occur in key-term supports,
so the support alphabet `Π` is finite, giving the crux and then periodicity.

Explicit answer: `a_{n+T} = a_n + L` for **every** `n ≥ 1`, with `L = ∏_{p∈Π} p` and
`T = |{c ∈ [a₁, a₁+L) : c is a term}|`. Verified for `a₁ = 375`: `Π = {2,3,5,7,19}`, `L = 3990`,
`T = 852` — matching the run's independently certified value.

## Approaches tried
- **key-term-first-appearance** — SOLVED (R7, APPROVE). Self-contained fresh-prime Rescale-Witness
  route; bypasses the E4/E5/E5″/𝓐_∞ antichain machinery entirely. Canonical Full proof below.
- **redundant-constraint-antichain** — SOLVED (R7, APPROVE). §15 closes the Crux directly with the
  same lever, feeding the certified §4–§5 endgame. The whole 6-round reduction chain
  (no-transient ⇒ E1/E2/E3 ⇒ E4 ⇒ Crux ⇒ theorem) is retained as provenance but no longer needed:
  §15 supplies the Crux unconditionally.
- **joint-recruitment-budget** — RETHINK (R6). Certified negative guardrail (Rejection-Budget
  Dichotomy): a disjoint per-recruit cost from the O(N) rejection stream bounds recruit RATE not
  COUNT. `lemmas/rejection-budget-dichotomy.md`.
- **realizer-index-joint-double-count** — RETHINK (R5). Lemma J (joint-spread) proven illusory:
  `t−t′ = q(A−B)`, `A,B` coprime ⇒ spread bound = magnitude bound. Salvage `two-anchor-scaffold.md`.
- **residual-anchor-peeling** — RETHINK (R4). Proven to collapse to E5 (non-transversal-sub-support
  lever reproduces E4 chain-descent). Salvage `anchor-partition.md`.
- **value-stream-double-freeze** — RETHINK (R3). Automaton framing collapses to Π-finite.
- **monovariant-witness-descent** — RETIRED (R4). A_n-only statistics frozen by obstruction family.
- **anomaly-count-terminates** — DEAD (R1). M-threshold confinement lemma false (a₁=375: 19∣L, M=15).

## Current best
RESOLVED. The theorem is proved outright. See the Full proof.

## Full proof

### 0. Statement and notation

Let `a₁ > 1` be an integer and define `(aₙ)_{n≥1}` by the greedy rule
`a_{n+1} = min{ c > aₙ : gcd(c, a_i) > 1 for every i with 1 ≤ i ≤ n }`.
We prove there exist positive integers `T, L` with `a_{n+T} = aₙ + L` for every `n ≥ 1`.

The rule is well-defined and the sequence is infinite: the least multiple of `rad(a₁)` exceeding
`aₙ` is always a valid candidate (Lemma L2), so the minimum is over a nonempty set; the sequence is
strictly increasing by construction.

For an integer `x > 1` write `P(x)` for its set of prime divisors. Then for `x, y > 1`,
`gcd(x,y) > 1 ⟺ P(x) ∩ P(y) ≠ ∅`  (∗).
Set `Q := P(a₁)`, `q₀ := max Q` (a prime, `q₀ ∣ a₁` so `q₀ ≤ a₁`), `M := rad(a₁) = ∏_{p∈Q} p`. Let
`𝓢 := {aₙ : n ≥ 1}` be the value set; since the sequence is strictly increasing, `n ↦ aₙ` is a
bijection onto `𝓢`, every element of `𝓢` is `≥ a₁`, and `a₁ = min 𝓢`. An integer is a **term** iff
it lies in `𝓢`. For terms, `a_i < a_j ⟺ i < j`.

### 1. Free lemmas (certified: `lemmas/free-lemmas.md`)

**L1 (Anchor).** Every term `aₙ` has a prime factor in `Q = P(a₁)`.
*Proof.* `n=1`: `a₁`'s primes are `Q`. `n≥2`: the clause `i=1` gives `gcd(aₙ, a₁) > 1`; by (∗) a
common prime lies in `Q`. ∎

**L2 (Gap bound / growth).** `a_{n+1} − aₙ ≤ M` for all `n`; hence `aₙ → ∞`.
*Proof.* Let `c` be the least multiple of `M` with `c > aₙ`; then `aₙ < c ≤ aₙ + M`. For each
`i ≤ n`, L1 gives `p ∈ Q` with `p ∣ a_i`, and `p ∣ M ∣ c`, so `gcd(c, a_i) ≥ p > 1`. Thus `c` is
admissible at stage `n`, so `a_{n+1} ≤ c ≤ aₙ + M`. Strict monotonicity gives
`aₙ ≥ a₁ + (n−1) → ∞`. ∎

**L4 (Pairwise-intersecting).** `gcd(a_i, a_j) > 1` for all `i ≠ j`; i.e. `P(a_i) ∩ P(a_j) ≠ ∅`.
*Proof.* For `i < j`, the defining property of `a_j = a_{(j−1)+1}` includes the clause `i ≤ j−1`
requiring `gcd(a_j, a_i) > 1`. Symmetry gives all `i ≠ j`. ∎

(L3, the distance–prime lemma, is not needed for this route.)

### 2. Forward-admissibility

**Lemma FA.** For an integer `c > a₁`: `c` is a term ⟺ `gcd(c, a_i) > 1` for every term `a_i < c`.

*Proof.* **(⇒)** If `c = a_m` is a term (`m ≥ 2` as `c > a₁`), every term `a_i < c` has `i < m`, and
L4 gives `gcd(a_m, a_i) > 1`.
**(⇐)** Suppose `c > a₁` and `gcd(c, a_i) > 1` for every term `a_i < c`. Since `aₙ → ∞` (L2) and
`a₁ < c`, `{n : aₙ < c}` is nonempty (contains `1`) and finite; let `m := max{n : aₙ < c}`, so `a_m`
is the largest term below `c`. First, `a_{m+1} ≥ c`: otherwise `a_{m+1}` is a term with
`a_m < a_{m+1} < c`, contradicting maximality of `a_m`. Second, `c` is admissible at stage `m`:
`c > a_m`, and for every `i ≤ m`, `a_i ≤ a_m < c` is a term `< c`, so the hypothesis gives
`gcd(c, a_i) > 1`. Hence `c` is a candidate in the minimum defining `a_{m+1}`, so `a_{m+1} ≤ c`.
Combined with `a_{m+1} ≥ c`: `a_{m+1} = c`, a term. ∎

Whether `c` is a term is decided purely by the terms *already emitted below `c`* — a local
criterion derived directly from the greedy rule, with no reference to any global admissible set.

### 3. Key terms and Domination

Process terms in index order and select **key terms** by first occurrence:
`aₙ` is a key term ⟺ no key term `b = a_j` with `j < n` satisfies `P(b) ⊆ P(aₙ)`.
Equivalently, for every earlier key term `b`, `P(b) ⊄ P(aₙ)`. Since `a₁` has no earlier term, `a₁`
is always a key term. Write `𝓚` for the set of key terms; a key term `b = a_j` is **earlier** than a
key term `x = a_m` if `j < m`.

**Lemma DOM (Domination).** For every term `aₙ` there is a key term `b` of index `≤ n` with
`P(b) ⊆ P(aₙ)`.
*Proof.* If `aₙ` is key, take `b = aₙ`. Otherwise, by the key-term definition there is an earlier key
term `b = a_j` (`j < n`) with `P(b) ⊆ P(aₙ)`. ∎

**Lemma DIST (Distinct supports).** Distinct key terms have distinct supports.
*Proof.* Let `b = a_j`, `b′ = a_{j′}` be key terms with `j < j′` and `P(b) = P(b′)`. Then
`P(b) ⊆ P(b′)` with `b` an earlier key term, so `a_{j′}` fails the key condition — contradiction. ∎

### 4. Threshold and the Fresh-Prime Rescale-Witness Lemma

Set the **threshold** `C := q₀ · a₁`. A prime `p` is **fresh at** a key term `x` if `p ∈ P(x)` and
`p ∉ P(b)` for every key term `b` earlier than `x`.

**Lemma RW (Rescale-Witness).** No key term `x` with `x > C` contains a prime fresh at `x`.

*Proof.* Suppose for contradiction `x = a_m` is a key term with `x > C` and `p` is fresh at `x`.
Since `x > C = q₀a₁ ≥ a₁` we have `m ≥ 2`, so `a₁` is a key term earlier than `x`; freshness forces
`p ∉ P(a₁) = Q`.

**(i) Anchor `q`.** By L4, `gcd(x, a₁) > 1`, so by (∗) pick a prime `q ∈ P(x) ∩ Q`. Then `q ≤ q₀`
(as `q ∈ Q`) and `q ≠ p` (as `q ∈ Q`, `p ∉ Q`). Put `S := P(x) ∖ {p}`, `r := ∏_{s∈S} s`. Since
`q ∈ P(x)`, `q ≠ p`, we have `q ∈ S`, so `S ≠ ∅` and `P(r) = S`. As `{p}` and `S` partition `P(x)`,
`rad(x) = p·r`; since `rad(x) ≤ x`, `r = rad(x)/p ≤ x/p < x`  (4.1).
*(This disposes of `|P(x)|=1`: if `P(x)={p}` then `P(x)∩Q=∅`, contradicting L4; so a fresh-prime key
term has `|P(x)| ≥ 2` and the anchor `q` exists.)*

**(ii) Witness `y` with `a₁ ≤ y < x` and `P(y) = S`.**
*Case A: `r ≥ a₁`.* Set `y := r`. Then `a₁ ≤ y`, `P(y) = S`, and `y = r < x` by (4.1).
*Case B: `r < a₁`.* Since `q ≥ 2`, `r·q^t → ∞` in `t` and `r·q⁰ = r < a₁`. Let `t ≥ 1` be least with
`r·q^t ≥ a₁`; by minimality `r·q^{t−1} < a₁`. Set `y := r·q^t = q·(r·q^{t−1})`. Then
`a₁ ≤ y = q·(r·q^{t−1}) < q·a₁ ≤ q₀·a₁ = C < x`. As `q ∈ S`, multiplying by powers of `q` adds no new
prime: `P(y) = P(r) ∪ {q} = S`.
In both cases `a₁ ≤ y < x` and `P(y) = S = P(x)∖{p} ⊊ P(x)`.

**(iii) `y` is a term.** If `y = a₁`, done. Otherwise `y > a₁`; by Lemma FA it suffices to show
`S ∩ P(a_i) ≠ ∅` for every term `a_i < y`. Fix such `a_i`. Since `y < x = a_m`, `a_i < a_m` gives
`i < m`, so `a_i` is a term earlier than `x`. By DOM there is a key term `b` of index `≤ i < m` with
`P(b) ⊆ P(a_i)`; `b` is a key term earlier than `x`. As `b, x` are distinct terms, L4 gives
`P(x) ∩ P(b) ≠ ∅`; pick `w ∈ P(x) ∩ P(b)`. Since `b` is an earlier key term and `p` is fresh at `x`,
`p ∉ P(b)`, so `w ≠ p`, hence `w ∈ P(x)∖{p} = S`. Thus `w ∈ S ∩ P(b) ⊆ S ∩ P(a_i)`, so
`S ∩ P(a_i) ≠ ∅`. By Lemma FA, `y` is a term.

*(Freshness is load-bearing, and is exactly what `p_max` lacks: a dominating key term `b` cannot
contain the fresh `p`, so its shared prime with `x` is a genuine element of `S`; removing `p_max`
instead could leave a private-witness term (sharing only `p_max` with `x`) unmet — the certified
R5/JSC obstruction. And `y` need only meet the finitely many already-emitted terms below it, never a
transversal of an infinite family — this keeps the argument off the R4-Collapse guardrail.)*

**(iv) Contradiction.** `y` is a term with `y < x = a_m`, so `y = a_ℓ`, `ℓ < m`. By DOM there is a
key term `b′` of index `≤ ℓ < m` with `P(b′) ⊆ P(y) = S ⊊ P(x)`. So `b′` is a key term earlier than
`x` with `P(b′) ⊆ P(x)`, contradicting the key condition for `x`. ∎

### 5. Finiteness of the key terms

Let `𝓚_{≤C} := {b ∈ 𝓚 : b ≤ C}`. By L2 only finitely many terms are `≤ C`, so `𝓚_{≤C}` is finite;
put `K := ⋃_{b∈𝓚_{≤C}} P(b)`, a finite set of primes.

**Claim.** Every key term's support is `⊆ K`.
*Proof.* Suppose not; among key terms with support `⊄ K`, let `x` have least index. Every earlier key
term then has support `⊆ K`. If `x ≤ C` then `x ∈ 𝓚_{≤C}`, so `P(x) ⊆ K` — contradiction; hence
`x > C`. Pick `p ∈ P(x) ∖ K`. For every earlier key term `b`, `P(b) ⊆ K` and `p ∉ K`, so `p ∉ P(b)`;
thus `p` is fresh at `x`. Lemma RW (`x > C`) gives a contradiction. ∎

So every key support lies in `2^K`; by Lemma DIST distinct key terms have distinct supports, hence
`|𝓚| ≤ 2^{|K|} < ∞`. **The set of key terms is finite.**

*(Degenerate check.)* If `a₁` is a prime power, `Q = {q₀}`, and by L1 every term `aₙ` has `q₀ ∈ P(aₙ)`,
so `P(a₁) = {q₀} ⊆ P(aₙ)` and `aₙ` is dominated — no later key term exists, `𝓚 = {a₁}`.

### 6. Endgame: finite prime pool ⇒ periodicity

Let `Π := ⋃_{b∈𝓚} P(b)` and `L := ∏_{p∈Π} p`. By §5, `𝓚` is finite, so `Π` is finite and `L` a
well-defined positive integer.

**Lemma E (Key-transversal characterization).** For `c ≥ a₁`: `c` is a term ⟺ `gcd(c, b) > 1` for
every key term `b`.
*Proof.* **(⇒)** For a term `c = aₙ` and key term `b = a_j`: `j=n` gives `gcd(aₙ,aₙ) > 1`; `j≠n`
gives `gcd` `> 1` by L4. **(⇐)** If `c = a₁`, done. If `c > a₁`, take any term `a_i < c`; by DOM a
key term `b` has `P(b) ⊆ P(a_i)`, so `∅ ≠ P(c) ∩ P(b) ⊆ P(c) ∩ P(a_i)`, i.e. `gcd(c, a_i) > 1`. By
Lemma FA, `c` is a term. ∎

**Lemma RES (Residue-determined membership).** For `c ≥ a₁`, term-ness depends only on `c mod L`.
*Proof.* By Lemma E, `c ≥ a₁` is a term iff `P(c) ∩ P(b) ≠ ∅` for every key term `b`. Each
`P(b) ⊆ Π`, and for `p ∈ Π`, `p ∣ L`, so `p ∣ c ⟺ p ∣ (c mod L)`. Hence `{p ∈ Π : p ∣ c}` — and
thus the whole predicate — is a function of `c mod L`. ∎

Let `U ⊆ ℤ/Lℤ` be the residues `ρ` such that some (equivalently every) integer `c ≥ a₁` with
`c ≡ ρ` is a term. Then `𝓢 = {c ≥ a₁ : (c mod L) ∈ U}`  (6.1). `U` is nonempty: any multiple `c ≥ a₁`
of `L` meets every key term `b` (a prime `p ∈ P(b) ⊆ Π` divides `L ∣ c`), so `c` is a term by Lemma E
and `0 ∈ U`.

By (6.1)/RES, for every `c ≥ a₁`: `c ∈ 𝓢 ⟺ c + L ∈ 𝓢`  (6.2) (both `≥ a₁`, same residue).
Put `T := |U|`. In `[a₁, a₁+L)` there is exactly one representative of each residue class, all
`≥ a₁`, so `|𝓢 ∩ [a₁, a₁+L)| = |U| = T`  (6.3); these are the smallest `T` elements of `𝓢`, i.e.
`a₁, …, a_T`. The map `φ(c) = c + L` sends `𝓢` injectively, order-preservingly onto
`𝓢′ := {c ∈ 𝓢 : c ≥ a₁+L} = 𝓢 ∖ [a₁, a₁+L)` (onto: if `d ∈ 𝓢`, `d ≥ a₁+L`, then `d−L ≥ a₁` and
`d−L ∈ 𝓢` by (6.2), `φ(d−L)=d`). By (6.3), `𝓢′` is `𝓢` with its smallest `T` elements removed, so
its increasing enumeration is `a_{T+1} < a_{T+2} < ⋯`. Since `φ` is an order-isomorphism from
`𝓢 = (a_1 < a_2 < ⋯)` onto `𝓢′ = (a_{T+1} < a_{T+2} < ⋯)`, it sends the `k`-th smallest of `𝓢` to
the `k`-th smallest of `𝓢′`: `φ(a_k) = a_{T+k}`, i.e. `a_k + L = a_{T+k}`. Therefore

  **`a_{n+T} = aₙ + L` for every `n ≥ 1`**,  with `L = ∏_{p∈Π} p` and `T = |U| = |𝓢 ∩ [a₁, a₁+L)|`.

This completes the proof. ∎

### 7. Verification (`a₁ = 375`)

`Q = P(375) = {3,5}`, `q₀ = 5`, `C = 1875`. The first-occurrence key-term filter yields exactly six
key terms `𝓚 = {375, 378, 380, 384, 399, 490}`, all `≤ 1875` (confirming Lemma RW), with supports
`{3,5},{2,3,7},{2,5,19},{2,3},{3,7,19},{2,5,7}`, union `Π = {2,3,5,7,19}`, `L = 3990`. Counting
residues, `T = 852`. Independent greedy simulation confirms zero Lemma-E mismatches over the computed
range and zero violations of `a_{n+T} = aₙ + L`, matching the run's certified `(T, L) = (852, 3990)`.
Reconfirmed with the reviewer's own simulation on `a₁ ∈ {375, 385, 105, 9, 49}`: all key terms `≤ C`,
zero Lemma-E mismatches, `a₁=375 → (852, 3990)`.
