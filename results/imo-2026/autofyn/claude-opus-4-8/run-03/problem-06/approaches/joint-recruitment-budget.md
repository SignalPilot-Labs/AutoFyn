# joint-recruitment-budget — global rejection-stream accounting (NEW pole, R6)

## Status
partial

This slug was seeded as the last unexhausted joint-accounting thread (opening 5 of the
joint-potential explorer): a **global** monovariant that reads the greedy *rejection stream*
(the skipped candidates — the choices), attributing a **disjoint** per-recruit cost to each newly
recruited large prime, aiming to contradict "infinitely many recruits" against a bounded-rate
budget. Per the outline-reviewer gate (`/tmp/round-6/outline-reviewer.md` §2) the positive route
**provably forks**. This file therefore delivers the honest, run-advancing outcome the dispatch
authorized: the framing is set up rigorously and the fork is certified as a **permanent negative
guardrail — the Rejection-Budget Dichotomy** — closing this thread the way JSC/Collapse closed the
spread and sub-support levers. It does NOT close E5″, and it does not attempt the forbidden lever.

## Approaches tried
- **joint-recruitment-budget (R6, NEW far-framing pole)** — RETHINK as a positive route to E5″;
  redirected to certify the negative guardrail. Setup (rejection stream + O(N) budget) is sound and
  rests on certified facts (no-transient, E1/E2, Gap-bound L2). The intended closing step (a disjoint
  per-recruit cost with cost→∞ contradicting the budget) is **proven impossible by the
  Rejection-Budget Dichotomy** below: the budget is exactly Φ_N = a_N − a₁ − (N−1) = O(N), and any
  disjoint attribution satisfies Σ|C_q| ≤ Φ_N **tautologically**, so cardinality bounds recruit *rate*
  but never recruit *count* — no contradiction with Π infinite is reachable. The only ways to force a
  per-recruit cost →∞ each fork into a proven-dead lever (Horn A degenerate / Horn B = JSC-spread /
  vocabulary = R4-Collapse). Numerics verified (a₁∈{375,385,867,105}, N=400). Certified negative
  guardrail; Status honestly partial (no solve). No overclaim.

## Current best

The furthest correct progress of this pole is a **certified negative theorem** (a guardrail), together
with the rigorous accounting framing that produces it. Nothing here closes E5″; the value is that it
permanently maps out and closes the joint-rejection-budget thread.

Throughout: `a₁,a₂,…` is the greedy sequence (`a_{n+1}` = smallest integer `> a_n` coprime-nontrivially
to every earlier term); `s` its (certified fixed) successor map; `M := rad(a₁)`; `A` the admissible set;
`𝓐_∞` the ⊆-minimal prime-supports; `Π := ⋃_{G∈𝓐_∞} G`; the **Crux** ("Finite Alphabet") is
"`𝓐_∞` finite ⟺ Π finite," and its live open form is **E5″** (a minimal `G` with `∏G ≥ a₁` has
`∏(G∖{p_max}) < a₁`). Certified assets cited: **no-transient** (`a_{n+1}=s(a_n)` ∀n≥1,
`no-transient-fixed-successor.md`); **E1** (`{a_n}=A∩[a₁,∞)`) and **E2** (supports are ⊆-minimal
transversals; admissibility ⟺ meeting every `G∈𝓐_∞`) (`enumeration-and-transversal.md`); **Gap-bound
L2** (each gap `a_{n+1}−a_n ≤ M`, `a_n=Θ(n)`) (`free-lemmas.md`); **R1** (`∏G` is a term when `∏G≥a₁`)
(`realizer-value-pincer.md`); **TAS/JSC** (`two-anchor-scaffold.md`); **anchor-partition Collapse**
(`anchor-partition.md`); **monovariant obstruction** (density(A)→positive limit while Π infinite,
`monovariants-and-obstruction.md`).

### 1. The framing (sound, on certified facts)

**The rejection stream.** For each `n ≥ 1` set
```
    R_n := { c ∈ ℤ : a_n < c < a_{n+1} }.
```
By no-transient, `a_{n+1}=s(a_n)` is the *smallest* admissible integer exceeding `a_n`; hence every
`c ∈ R_n` is **inadmissible**. By E1/E2 (admissibility ⟺ meeting every `G∈𝓐_∞`), each `c∈R_n` **misses**
some ⊆-minimal support: there is `F(c) ∈ 𝓐_∞` with `gcd(c, ∏F(c)) = 1`. Fix one such `F(c)` per `c`.
Define the **rejection stream below `a_N`**:
```
    𝓡_N := ⋃_{n=1}^{N-1} R_n     (a set of distinct integers in (a₁, a_N)).
```
This is a *choice-reading* object: it records exactly which candidates the greedy rule rejected and
(via `F`) which support each was blocked by — not any statistic of the admissible set `A_n` alone.

**The budget is O(N).** Since the `R_n` are the disjoint gap-interiors,
```
    |𝓡_N| = Σ_{n=1}^{N-1} (a_{n+1} − a_n − 1) = (a_N − a₁) − (N−1) =: Φ_N,
```
a telescoping identity. By Gap-bound L2 each gap `a_{n+1}−a_n ≤ M`, so
```
    Φ_N ≤ (M−1)(N−1) = O(N).                                    (BUDGET)
```
`Φ_N` is precisely the cumulative gap-deficit / density quantity: `Φ_N/N → M·(1 − density(A)) `-type
positive constant. This is the pole's total resource.

**The intended (forbidden) closing route.** When a new largest prime `q` is first recruited (first
appears in some `G_q∈𝓐_∞`; its realizer `∏G_q` is a genuine term by R1), one wants to attach a **cost
set** `C_q ⊆ 𝓡_N` of rejected candidates, defined so that **distinct recruits get disjoint cost sets**,
with `|C_q| ≥ c_q` and `c_q → ∞` as `q → ∞`. Then if Π is infinite there are recruits `q_1<q_2<⋯`, and
```
    Σ_k |C_{q_k}| ≤ |𝓡_N| = Φ_N = O(N)   while (allegedly) LHS → ∞ faster than N,
```
a contradiction ⇒ Π finite ⇒ (Reduction Lemma + no-transient) the theorem. **This route provably
cannot be completed.** The obstruction is Theorem RBD below.

### 2. Theorem (Rejection-Budget Dichotomy — certified negative guardrail)

> **Setup.** Assume `a₁` is not a prime power (`|P|≥2`); the prime-power case `|P|=1` is disposed of
> outright by the certified TAS prime-power lock (`{p*}∈𝓐_∞` forces `𝓐_∞={{p*}}`, Crux holds, nothing
> to prove). Suppose, for contradiction toward the pole's goal, Π is infinite. Let `q ↦ C_q ⊆ 𝓡_N` be
> **any** assignment of pairwise-disjoint cost sets to the recruits `q` whose realizer `∏G_q < a_N`
> (so all recruits are eventually captured as `N→∞`).
>
> **(a) Tautology (certified core).** For every `N`,
> ```
>     Σ_q |C_q| ≤ |𝓡_N| = Φ_N ≤ (M−1)(N−1).                     (★)
> ```
> **(b) No contradiction from disjointness (certified core).** Consequently, if the recruits up to `a_N`
> are `q_1<⋯<q_{r(N)}` with `|C_{q_k}| ≥ c_k` and `c_k → ∞`, then `Σ_{k=1}^{r(N)} c_k ≤ (M−1)(N−1)`.
> This bounds the recruitment **rate** but **not** the recruitment **count** `r(N)`: since `c_k → ∞`, it
> merely forces `r(N)` to grow *sub-linearly* in `N`, which is **fully consistent with `r(N) → ∞`**
> (Π infinite). No contradiction is reachable from `(★)` and `c_k → ∞` alone.
> **(c) Every route to `c_q → ∞` forks** into a proven-dead lever (Horns A / B / vocabulary below).

*Proof of (a).* The `C_q` are pairwise-disjoint subsets of the finite set `𝓡_N`; the cardinality of a
disjoint union is the sum of cardinalities and is `≤ |𝓡_N|`. The equality and the bound are (BUDGET). ∎

*Proof of (b).* `(★)` gives `Σ_{k=1}^{r(N)} c_k ≤ (M−1)(N−1)`. Fix any threshold `T`; since `c_k→∞`
there is `K_T` with `c_k ≥ T` for `k ≥ K_T`. For the recruits with `K_T ≤ k ≤ r(N)`,
`T·(r(N) − K_T) ≤ Σ c_k ≤ (M−1)(N−1)`, whence
```
    r(N) ≤ K_T + (M−1)(N−1)/T.
```
This is an *upper* bound on `r(N)` of the form `O(N/T)` — i.e. `(★)` forces the recruit count to grow at
most linearly, and (letting `T→∞` along a diagonal) *sub*-linearly. It never forces `r(N)` bounded.
An infinite Π with sparse large-prime recruitment realizes exactly a sub-linear unbounded `r(N)`: the
certified obstruction family `{p*, q_k}` (`monovariants-and-obstruction.md`) has infinitely many
recruits `q_k→∞` yet density(A)→a positive limit, i.e. `Φ_N = Θ(N)` with `r(N)→∞` sub-linearly. Hence
`(★)` + `c_k→∞` is *satisfiable* with Π infinite; it is not a contradiction. ∎

The heart is thus: **cardinality of a disjoint budget bounds the recruitment rate, never the total
number of recruits.** To manufacture a contradiction one would need `c_k` to grow at least linearly in
the recruit *index* (making `Σ_{k≤r} c_k` super-linear in `r`), i.e. each recruit's cost must scale with
the *global* recruit count so far — a global coupling that disjoint *local* rejections structurally
cannot supply. The only mechanisms that even make `c_q → ∞` are the following, and each is a dead lever.

*Proof of (c) — the three horns.*

- **Horn A (bounded local-window cost — degenerate).** The outline's concrete proposal takes `C_q` to be
  the rejected candidates in a **length-`≤M` window topping out at the realizer `∏G_q`**, i.e.
  `C_q ⊆ (∏G_q − M, ∏G_q) ∩ 𝓡_N`. Any real interval of length `< M` contains at most `M−1` integers,
  so
  ```
      |C_q| ≤ M − 1     for every recruit q.                    (HORN-A)
  ```
  The cost is bounded by the fixed `a₁`-only constant `M−1`; `c_q ↛ ∞`. The intended step 4 fails
  outright. (This is fully rigorous — a window of `a₁`-bounded length carries an `a₁`-bounded number of
  rejections, independent of `q`.)

- **Horn B (global cost spanning the number line).** To get `|C_q| → ∞` the cost set must occupy a
  region of length `→ ∞`. The only canonical `→∞`-length region attached to a recruit `q_k` (with
  `q_k→∞`) is the interval between its two **TAS** anchor-realizers: by TAS (`|P|≥2`, `𝓐_∞` infinite)
  there are fixed anchors `p*,p**∈P` and, for each retained `k`, terms `t_k=∏G_k`, `t'_k=∏H_k` with
  `q_k ∣ (t_k−t'_k)` and `|t_k−t'_k| ≥ q_k → ∞`. Take `C_{q_k} ⊆ 𝓡_N ∩ [\min(t_k,t'_k), \max(t_k,t'_k)]`.
  Two sub-cases, both dead:
  - **(i) disjoint intervals ⇒ (★) is a tautology.** If the interval costs are pairwise disjoint, then
    by (a), `Σ_k |C_{q_k}| ≤ Φ_N = O(N)`. Large per-recruit cost merely means the recruit intervals tile
    a `Θ(N)`-length stretch of the number line, each consuming `≥ q_k` of it, so `Σ_k q_k = O(N)` — which
    is **consistent** with `q_k → ∞` sparse (fewer recruits per unit length). No contradiction: exactly
    case (b).
  - **(ii) cap the interval length ⇒ JSC.** To instead force a contradiction one must claim the interval
    *cannot* be that long — bound `|t_k − t'_k| ≤ f(a₁)`. By **JSC** (`two-anchor-scaffold.md`),
    `t_k − t'_k = q_k(A_k − B_k)` with `A_k, B_k` products over disjoint prime sets, so `A_k ≠ B_k` and
    `|t_k−t'_k| ≥ q_k`; hence `|t_k−t'_k| ≤ f(a₁)` ⟹ `q_k ≤ f(a₁)` = **the magnitude bound = the Crux
    itself** (certified dead, R5). Circular.

- **Vocabulary variant (finite recruitment vocabulary ⇒ R4 Collapse).** The explorer's alternative
  phrasing ("recruitment consumes a globally finite vocabulary"): each recruit `q` pairs with a
  small-prime part `B = G_q ∖ {p_max}`, and one assumes `B` ranges over a *finite* set (so cost accrues
  per fresh vocabulary item). But "`B` bounded" is `∏B < a₁` = **E5″ itself** — the very statement to be
  proved (circular). Granting it, Π infinite + finite `B`-vocabulary ⇒ (Pigeonhole) an infinite subfamily
  with a **common core `B`**; this is precisely the **anchor-partition common core**, and forcing a
  `B`-term to close the count is the **R4 Collapse theorem** (`anchor-partition.md`): the common core is a
  proper sub-support, hence not a transversal, so no dominating `B`-term is realizable — the argument
  reproduces the E4/E5 chain-descent verbatim (certified dead, R4).

Every route to `c_q → ∞` with disjoint costs from the `Φ_N = O(N)` rejection budget thus forks into
Horn A (degenerate/bounded), Horn B(i) (tautological, no contradiction), Horn B(ii) (= JSC, dead), or
the vocabulary variant (= R4 Collapse, dead). **No escape.** ∎

### 3. Scope of the guardrail (what is and is NOT certified)

Exactly as JSC scoped itself, I separate the certified content from the heuristic slogan:

- **Certified (theorems):** (a) the tautology `(★)`, (b) its consequence that a disjoint per-recruit
  budget bounds recruitment *rate* but never *count* — so no disjoint attribution from `𝓡_N` can
  contradict Π infinite by cardinality; (HORN-A) the `M−1` bound on any bounded-window cost; and the two
  reductions Horn B(ii)⟶JSC and vocabulary⟶Collapse (each a pointer to an already-certified negative).
  These make the intended positive route **provably unavailable**.
- **NOT a formal theorem (heuristic, honestly flagged):** the slogan that Horns A/B/vocabulary
  *exhaust every conceivable attribution rule*. There is no formal quantifier over "all attribution
  rules." What IS structural and certified is that `(★)` holds for **any** disjoint attribution
  *regardless of the rule*, so the cardinality obstruction — rate-not-count — is rule-independent; that
  is the permanent content. Any future attempt must therefore either (i) abandon disjointness (then `(★)`
  gives nothing, but overlap must be paid for elsewhere), or (ii) supply a cost `c_q` growing with the
  *global* recruit index via genuinely new arithmetic — not from the rejection budget.

**This does NOT close E5″.** It certifies that the joint-rejection-budget thread — the last
unexhausted joint-accounting opening — cannot close it.

### 4. Numerical verification (concrete anchor)

Independent simulation (greedy rule, `N=400`) for the four canonical seeds
`a₁ ∈ {375, 385, 867, 105}` confirms the budget identity and the `O(N)` bound underlying `(★)`:

| a₁  | M=rad(a₁) | max gap (≤M?) | Φ_N = Σ(gap−1) | a_N−a₁−(N−1) | equal? | (M−1)(N−1) | Φ_N≤bound? | Φ_N/N |
|-----|-----------|---------------|----------------|--------------|--------|------------|------------|-------|
| 375 | 15        | 6  (yes)      | 1466           | 1466         | yes    | 5586       | yes        | 3.665 |
| 385 | 385       | 14 (yes)      | 3044           | 3044         | yes    | 153216     | yes        | 7.610 |
| 867 | 51        | 3  (yes)      | 798            | 798          | yes    | 19950      | yes        | 1.995 |
| 105 | 105       | 6  (yes)      | 1046           | 1046         | yes    | 41496      | yes        | 2.615 |

So (i) `Φ_N = a_N − a₁ − (N−1) = Σ(gap−1)` exactly (the telescoping budget identity); (ii) each gap
`≤ M` (Gap-bound L2), giving `Φ_N ≤ (M−1)(N−1) = O(N)` — the scarce linear budget of `(★)`; and
(iii) `Φ_N/N` stays bounded away from `0` and `∞` (positive density limit), so recruits arrive at a
*positive but bounded* rate — the exact regime in which `(★)` permits `r(N)→∞` with no contradiction
(case (b) / the obstruction family). The computation stands only as a check; the guardrail is proved
above from certified lemmas, not from the numerics.

### 5. Cross-link

This guardrail joins JSC (`two-anchor-scaffold.md`) and R4 Collapse (`anchor-partition.md`) as the
third certified negative around E5″. With it, the joint-potential lens is fully mapped: openings 1/2/4
(density/JSC-spread/Φ_N) and 3 (anchor-partition) and now 5 (rejection-budget) are all closed. The
leader `redundant-constraint-antichain` §13 should cross-link it as the certified cheap-kill outcome of
this pole. E5″ remains the single open arrow of the whole problem.

## Promotable lemmas

- **Rejection-Budget Tautology (RBT).** For the greedy sequence, the rejection stream below `a_N` is
  `𝓡_N = ⋃_{n<N}\{c: a_n<c<a_{n+1}\}` with `|𝓡_N| = Φ_N = a_N − a₁ − (N−1) = Σ_{n<N}(gap_n − 1) ≤
  (M−1)(N−1) = O(N)` (via telescoping + Gap-bound L2). Any pairwise-disjoint family `\{C_q⊆𝓡_N\}` of
  per-recruit cost sets satisfies `Σ_q|C_q| ≤ Φ_N`. Proved in §2(a) above from certified L2/E1/E2/
  no-transient.
- **Rejection-Budget Dichotomy (RBD — negative guardrail).** Under `|P|≥2` and Π infinite, no disjoint
  per-recruit attribution from `𝓡_N` can contradict Π infinite: `(★)` bounds the recruitment *rate*
  `Σc_k=O(N)` (hence `r(N)=O(N/T)` for every threshold `T`), never the recruitment *count*, which may
  →∞ sub-linearly (realized by the certified obstruction family). Every mechanism forcing per-recruit
  cost →∞ forks into a bounded local window (Horn A, `|C_q|≤M−1`), a tautological disjoint span
  (Horn B(i)), the certified JSC spread bound (Horn B(ii)), or the certified R4 Collapse (vocabulary).
  Proved in §2 above. Scope: the tautology, the rate-not-count consequence, Horn A, and the two
  reductions are certified; the "exhausts all rules" slogan is heuristic (flagged §3), exactly as JSC.
  Companion to `two-anchor-scaffold.md` (JSC) and `anchor-partition.md` (Collapse). Does NOT close E5″.
