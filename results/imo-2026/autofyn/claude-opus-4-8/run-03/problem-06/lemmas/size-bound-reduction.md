# Lemma E4 (Size-Bound Reduction) — CERTIFIED (round 3)

Source approach: `redundant-constraint-antichain` §11. Reviewer-certified round 3:
chain-descent re-derived by hand; each step (Anchor base, Case A impossibility via Lemma 11.0,
Case B pigeonhole) verified. Non-vacuity confirmed — the obstruction family `{p*,q_k}` (bounded
size, infinite) is correctly excluded because it violates self-blocking (`{p*}` is a minimal
transversal but not a member), so E4's E2(⇐) hypothesis genuinely fails there; real greedy
`𝓐_∞` DO satisfy E2(⇐) (verified: members = minimal transversals exactly for
`a₁∈{375,9375}`), so for real sequences bounded size ⟹ finite.
Reduces the Finite-Alphabet crux to a bound on the *cardinality* of ⊆-minimal supports.
Numerically checked (self-blocking + `max|G|≤4`) for `a₁∈{6,15,35,105,375,385,867,1155,2025,9375}`.

Note on E2(⇐): the certified file `enumeration-and-transversal.md` states the *realization
preliminary* (finite B meeting every member ⇒ realized as a term). E2(⇐) ("every finite minimal
transversal is a member") is the immediate consequence used here: realize the transversal T' as a
term, so T'∈𝓕; by Domination T'⊇G₀∈𝓐_∞; G₀ is itself a transversal (E2⇒) and G₀⊆T', so
T'-minimality forces G₀=T', i.e. T'∈𝓐_∞. This one-line derivation is sound and is what E4 invokes.

## Setup / certified prerequisites
Greedy sequence `a₁,a₂,…` (ints `>1`), `a_{n+1}=min{c>a_n : gcd(c,a_i)>1 ∀i≤n}`.
`F(x)={primes|x}`, `F_n=F(a_n)`, `𝓕={F_n}`, `𝓐_∞ = ⊆-minimal elements of 𝓕`,
`A={c≥1 : c meets every G∈𝓐_∞}`, `Π=⋃𝓐_∞`. `P=F(a₁)`. Uses the CERTIFIED lemmas:
- **Anchor** (`free-lemmas.md`): every `G∈𝓐_∞` meets `P` (finite).
- **Antichain**: `𝓐_∞` is a ⊆-antichain (its members are the ⊆-minimal elements of `𝓕`).
- **E1, E2(⇒), E2(⇐)** (`enumeration-and-transversal.md`): `{a_n}=A∩[a₁,∞)`; every member of
  `𝓐_∞` is a transversal of `𝓐_∞` (meets every member); and every **finite** minimal transversal
  of `𝓐_∞` is a member of `𝓐_∞` (self-blocking on finite sets).

A finite prime-set `T` is a **transversal** if `T∩G≠∅` for every `G∈𝓐_∞`.

## Lemma 11.0 (Every finite transversal contains a member)
If a finite prime-set `T` is a transversal, then `T⊇G₀` for some `G₀∈𝓐_∞`.

*Proof.* Among subsets of `T` that are transversals (nonempty: `T` is one), pick a ⊆-minimal one
`T'⊆T`. If some transversal `T''⊊T'` existed, `T''⊆T'⊆T` would be a smaller transversal inside `T`,
contradicting minimality of `T'`; so `T'` is a finite minimal transversal, hence `T'∈𝓐_∞` by
E2(⇐). Take `G₀=T'`. ∎

## Lemma E4 (Size-Bound Reduction)
`𝓐_∞` is finite ⟺ `C:=sup_{G∈𝓐_∞}|G|<∞`.

*Proof.* (⇒) finitely many finite sets have a finite max cardinality.

(⇐) Assume `|G|≤C` for all `G∈𝓐_∞` and, for contradiction, `𝓐_∞` infinite. Build
`B_1⊊B_2⊊⋯` and infinite `𝓗_1⊇𝓗_2⊇⋯⊆𝓐_∞` with, for each `t`: (i) `B_t⊆G` ∀`G∈𝓗_t`;
(ii) `|B_t|=t`; (iii) `𝓗_t` infinite.

*Base.* Every `G∈𝓐_∞` meets finite `P` (Anchor); `𝓐_∞` infinite ⇒ by Pigeonhole some `p₁∈P`
lies in infinitely many members. `B_1={p₁}`, `𝓗_1={G∈𝓐_∞:p₁∈G}`.

*Step `t→t+1`.*
- If `B_t` is a transversal: by Lemma 11.0, `G₀⊆B_t` for some member `G₀`. Every `G∈𝓗_t` has
  `G⊇B_t⊇G₀`; antichain ⇒ `G=G₀`; so `𝓗_t⊆{G₀}` finite — contradicts (iii). So this case never
  happens.
- Else `B_t` misses some member `W_t` (`W_t∩B_t=∅`). Each `G∈𝓗_t` is a transversal (E2(⇒)), so
  meets `W_t`; as `G⊇B_t` and `W_t∩B_t=∅`, the shared prime is in `W_t∖B_t`. `W_t` finite,
  `𝓗_t` infinite ⇒ Pigeonhole gives `r_t∈W_t∖B_t` in infinitely many `G∈𝓗_t`. Set
  `B_{t+1}=B_t∪{r_t}` (size `t+1`), `𝓗_{t+1}={G∈𝓗_t:r_t∈G}` infinite. (i)–(iii) hold.

The first bullet is impossible, so the second always applies and the chain runs for every `t`.
For `t=C+1`, any `G∈𝓗_{C+1}` (nonempty) has `G⊇B_{C+1}`, so `|G|≥C+1>C` — contradiction. Hence
`𝓐_∞` is finite. ∎

## Consequence
Combined with the certified endgame (`no-transient-fixed-successor.md`): if
`sup_{G∈𝓐_∞}|G|<∞` then `Π` is finite and `a_{n+T}=a_n+L` for ALL `n≥1` with `T=|ρ(A)|`,
`L=∏_{p∈Π}p`. Thus the whole problem reduces to the **cardinality bound**
`sup_{G∈𝓐_∞}|G|<∞` (OPEN; the sole remaining gap of the approach).

## Sharp form
The (⇐) proof in fact shows: `𝓐_∞` infinite ⟹ minimal supports of *unbounded* cardinality.
So the Crux is EQUIVALENT to `sup|G|<∞`.
