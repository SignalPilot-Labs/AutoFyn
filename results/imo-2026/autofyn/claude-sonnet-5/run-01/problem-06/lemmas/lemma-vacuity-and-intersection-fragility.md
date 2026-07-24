# Vacuity Proposition and Intersection-Fragility Proposition

**Source.** `results/imo-2026-06/approaches/forced-primes-well-ordering.md`
(round 8, §H, Step 5). Negative results: rule out a specific candidate
sufficiency fix (`S^{++}`) for the `S^+` Necessity + Finiteness Lemma's
gap. General-purpose, elementary set theory, reusable to rule out similar
future "intersection-based recruiter set" proposals.

## Vacuity Proposition

**Statement.** Fix a proper core `S`, `S^+:=⋂_{i∈I_S}rad(a_i)`, and for a
finite prime set `κ`, `S^{++}_κ:=⋂_{i∈I_S,\,κ⊆rad(a_i)}rad(a_i)`. If
`κ⊆S^+`, then `S^{++}_κ=S^+` identically.

**Proof.** Since `S^+⊆rad(a_i)` for every `i∈I_S` (definition of `S^+`),
`κ⊆S^+⊆rad(a_i)` holds for every `i∈I_S` — i.e. the restricting condition
`κ⊆rad(a_i)` used to define `S^{++}_κ` is satisfied by *every* `i∈I_S`, not
a proper subset. Hence
`S^{++}_κ=⋂_{i∈I_S,\,κ⊆rad(a_i)}rad(a_i)=⋂_{i∈I_S}rad(a_i)=S^+`. `∎`

## Intersection-Fragility Proposition

**Statement.** Let `I` be any subset of `ℕ` and `q` a prime. If
`q∉rad(a_i)` for even one `i∈I`, then `q∉⋂_{k∈I}rad(a_k)`.

**Proof.** Immediate: `q∉rad(a_i)⇒q∉⋂_{k∈I}rad(a_k)`, since the
intersection is a subset of `rad(a_i)`. `∎`

**Consequence.** No pure-intersection invariant over an index subclass
(`S^+`, `S^{++}_κ`, or the already-certified `D_S`) can ever recover a prime
absent from even one member of the relevant subclass, no matter how large or
"typical" that subclass is otherwise — a structural limitation of the entire
family, not a fixable defect of one specific construction.

## Certification

Both propositions are short, elementary, and correct — independently
re-derived by the round-8 proof-reviewer, no gap. Independently
re-verified numerically on the source's motivating instance
(`a_1=21528751,S={1061}`, fresh computation, see
`lemmas/lemma-freeze-confinement-domination-and-Splus.md`'s independent
`S^+={2,3,7,1061}` reproduction): the missing prime `11` fails to divide
`rad(a_{596})` (`={2,3,5,7,97,1061}`), confirming `11∉S^+` exactly as the
Intersection-Fragility Proposition predicts, and confirming (via the
Vacuity Proposition) that `S^{++}_{\{2,3,1061\}}=S^+` identically since
`{2,3}⊆S^+`. Certified `solved`-quality. Genuine, useful negative content:
rules out an entire family of candidate sufficiency fixes for the `S^+`
gap, not just the one instance tested.
