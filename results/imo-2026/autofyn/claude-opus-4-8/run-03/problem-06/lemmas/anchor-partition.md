# Certified lemmas — anchor partition + sub-support non-transversality

Certified round 4 (proof-reviewer). Source: `approaches/residual-anchor-peeling.md`.
UNCONDITIONAL; build on certified Anchor L1 (`free-lemmas.md`), E2(⇒), and Lemma 11.0
(`size-bound-reduction.md`). `P = primes(a₁)`, `𝓐_∞` = ⊆-minimal supports, `Π = ⋃𝓐_∞`.

## Lemma A (Anchor-Partition equivalence).
For `G∈𝓐_∞` set `α(G) := min(G∩P)` (well-defined: Anchor L1 gives `G∩P≠∅`, and `P` is finite
totally ordered). The fibers `𝓐_∞^{(p)} := {G : α(G)=p}` partition `𝓐_∞ = ⨆_{p∈P}𝓐_∞^{(p)}`, and
with `Q_p := ⋃_{G∈𝓐_∞^{(p)}}G`:

>  `Π` finite  ⟺  every `Q_p` finite  ⟺  every fiber `𝓐_∞^{(p)}` finite.

*Proof.* `α` is a well-defined map into the finite set `P`; its fibers partition `𝓐_∞`.
`Π = ⋃_{p∈P}Q_p`, a finite union, so finite iff each `Q_p` finite. `Q_p` finite ⟹ fiber is a
family of subsets of a finite set, hence finite; conversely fiber finite ⟹ finite union of finite
sets `Q_p` finite. ∎

This is a NEW unconditional equivalent form of the Finite-Alphabet crux, decomposing it over the
finite anchor set `P`. (Verified: `a₁=375` gives `𝓐_∞^{(3)}={{2,3},{3,5},{3,7,19}}`,
`𝓐_∞^{(5)}={{2,5,7},{2,5,19}}` — reproduced by independent simulation.)

## Lemma (Sub-support non-transversality — guardrail).
If `𝓗 ⊆ 𝓐_∞` is infinite with a common core `B` (`B ⊆ G` for all `G∈𝓗`), then `B` is NOT a
transversal of `𝓐_∞`. Equivalently: no proper sub-support of a minimal support is ever realized
as a term.

*Proof.* Each `G∈𝓗` is a minimal support with `B⊊G` (an infinite antichain `𝓗` cannot equal `B`).
If `B` were a transversal, certified Lemma 11.0 gives `G₀∈𝓐_∞` with `B⊇G₀`; then every `G∈𝓗` has
`G⊇B⊇G₀`, and the antichain property forces `G=G₀`, so `𝓗⊆{G₀}` is finite — contradiction. ∎

**Guardrail value.** Any pole hoping to "force a dominating common sub-support term" to collapse an
infinite family is, by this lemma, requiring that common sub-support to be a transversal — which an
infinite family forbids. Such a plan is attacking E5 itself, not bypassing it. This upgrades the
"shared-wall" diagnosis to a theorem: the anchor-partition pole (residual-anchor-peeling) provably
reduces, via the E4 chain-descent restarted from `B`, to `sup_{G∈𝓐_∞}|G|<∞` (E5).
