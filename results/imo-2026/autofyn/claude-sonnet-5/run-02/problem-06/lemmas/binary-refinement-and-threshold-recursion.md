# Binary Refinement Lemma + Threshold Recursion Bound Lemma (certified round 16)

**Source.** `approaches/core-growth-monotonicity.md`, round 16 build.
Independently re-derived and re-verified step-by-step (both lemmas' full
proofs re-checked line by line; a sanity computation run on `a_1=175`
confirming the qualitative partition-into-two-index-sets structure) by the
round-16 proof-reviewer. No gap found in either lemma.

**Setup (recalled).** Fix finite `S ⊇ Q = P(a_1)`. For `n ≥ 1`,
`ρ_S(n) := P(a_n) ∩ S`. By the certified Extended Persistent-Type Pigeonhole,
there is a finite nonempty set `𝒫'(S)` of S-persistent types (occurring at
infinitely many indices) with `Exc(S) := {n : ρ_S(n) ∉ 𝒫'(S)}` finite;
`N(S) := max(Exc(S) ∪ {0})`.

## Binary Refinement Lemma

**Statement.** Let `p ∉ S` be a prime, `S' := S ∪ {p}`. For every `n`:
`ρ_{S'}(n) = ρ_S(n)` or `ρ_S(n) ∪ {p}`, and `ρ_{S'}(n) ∩ S = ρ_S(n)`.
Consequently, writing `π: X ↦ X ∩ S`: (a) `π(𝒫'(S')) ⊆ 𝒫'(S)`; (b) `π`
restricted to `𝒫'(S')` is surjective onto `𝒫'(S)`, each `B ∈ 𝒫'(S)` having 1
or 2 preimages, a subset of `{B, B∪{p}}`.

**Proof.** `S' = S ⊔ {p}` (disjoint since `p∉S`) gives
`ρ_{S'}(n) = ρ_S(n) ∪ (P(a_n)∩{p})`, which is `ρ_S(n)` if `p∤a_n` and
`ρ_S(n)∪{p}` if `p|a_n`; intersecting with `S` gives the second display.
(a): if `X ∈ 𝒫'(S')` (infinite `I_X`), every `n∈I_X` has `ρ_S(n)=X∩S`, so
`X∩S ∈ 𝒫'(S)`. (b): fix `B∈𝒫'(S)`, infinite `I_B`; partition
`I_B = I_B^0 ⊔ I_B^1` by `p∤a_n` / `p|a_n`; since a finite∪finite union is
finite, at least one part is infinite, giving at least one preimage of `B`
in `𝒫'(S')`; "at most two" is immediate since only `B, B∪{p}` restrict to `B`
under `π`. ∎

## Threshold Recursion Bound Lemma

**Statement.** With `S,p,S'` as above, for `B ∈ 𝒫'(S)` define, using
`I_B, I_B^0, I_B^1` from the Binary Refinement Lemma's proof:
`M_B := 0` if both `I_B^0, I_B^1` infinite; `M_B := max(I_B^1)` (0 if empty)
if `I_B^0` infinite and `I_B^1` finite; `M_B := max(I_B^0)` (0 if empty) if
`I_B^1` infinite and `I_B^0` finite. (Well-defined: at least one part is
infinite by the Binary Refinement Lemma, so exactly one case applies.) Then
`N(S') ≤ max(N(S), max_{B∈𝒫'(S)} M_B)`.

**Proof.** For `n > N(S)`, `B := ρ_S(n) ∈ 𝒫'(S)`. Case both parts infinite:
both `B, B∪{p} ∈ 𝒫'(S')`, so `ρ_{S'}(n)` (which is one of the two) is always
in `𝒫'(S')` — no exception. Case `I_B^0` infinite, `I_B^1` finite: `B∈𝒫'(S')`
but `B∪{p}∉𝒫'(S')` (its occurrence set is `⊆ I_B^1`, finite); if `n∈I_B^0` no
exception, if `n∈I_B^1` an exception but `n ≤ max(I_B^1) = M_B`. Symmetric
case handled identically. Hence every exceptional `n` for `S'` satisfies
`n ≤ N(S)` or `n ≤ M_{ρ_S(n)} ≤ max_B M_B`. ∎

**Scope / honest limitation (not resolved by this lemma).** This does NOT
bound `M_B` itself, nor does it resolve sub-gap (H2) (boundedness of
`N(S_k)` along the true absorption chain, which enlarges the core by many
primes' full factorizations at once, not one prime at a time). The
companion Proposition 3 in `core-growth-monotonicity.md` (a "two consistent
extensions" argument, in the spirit of a basic fact about infinite 0/1
sequences — whether a binary sequence is eventually-constant-tail 0 or has
infinitely many 1's is not decidable from any finite prefix) shows `M_B`
itself is, in the same sense as `N(S)`, not computable from bounded-prefix
data; this argument is essentially toolkit-independent (a general fact
about infinite sequences, not merely "no certified tool in this workspace
computes it") and is recorded here as a standing caution, not certified as
a separate portable lemma file (it is a diagnostic about an approach
family, matching the round-7 Lemma F / round-10 Escape-Cost-Vacuity-style
precedent for when such statements are recorded vs certified).

**Reusable content.** First exact structural relation between `N(S)` at two
cores differing by a single prime; usable by any future attempt at
bounding `N(S_k)` along the absorption chain (sub-gap H2), though it alone
does not resolve H2.
