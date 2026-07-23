# Channel Splitting Lemma (two-sided channel stabilization ⟺ two one-sided ones)

## Status

Certified `solved`-quality (sorry-free), unconditional.

## Statement

Fix a channel `\{S,S'\}` (notation as in `channel-assembly-theorem.md`).
Define the single-class antichain `M_n^S:=\{i∈I_S∩[1,n]:\text{no
}k∈I_S∩[1,n]\text{ has }rad(a_k)⊊rad(a_i)\}`, `𝓜_n^S:=\{rad(a_i):i∈M_n^S\}`
(the ordinary minimal-radical antichain construction restricted to the
subsequence `(a_i)_{i∈I_S}` alone — domination comparisons use **only**
other indices in `I_S`, not the full index range `[1,n]` and not `I_{S'}`).
Then for **every** `n≥1`: `𝓜_n^{(S,S')}=𝓜_n^S⊔𝓜_n^{S'}` (disjoint union).
Consequently `(LMRS_{S,S'})⟺(MRS_S)∧(MRS_{S'})`, where `(MRS_S)`: `𝓜_n^S` is
eventually constant.

## Proof

Every `T∈𝓜_n^{(S,S')}` is `rad(a_i)` for `i∈M_n^{(S,S')}⊆J∩[1,n]`; since
`I_S,I_{S'}` are disjoint, exactly one of `i∈I_S`, `i∈I_{S'}` holds, giving
`T∩P_1∈\{S,S'\}` and a partition `𝓐_n⊔𝓑_n` of `𝓜_n^{(S,S')}`.

*No cross-side domination.* If `i∈I_S`, `k∈I_{S'}`, and
`rad(a_k)⊆rad(a_i)`, intersecting with `P_1` gives `S'⊆S`; disjointness
forces `S'=∅`, contradiction. Symmetrically for the other direction. So
domination between `I_S` and `I_{S'}` never occurs in either direction.

*Consequence.* For `i∈I_S∩[1,n]`: `i∈M_n^{(S,S')}` iff no `k∈J∩[1,n]`
dominates it; by the above, only `k∈I_S∩[1,n]` can possibly dominate `i`,
so this is equivalent to `i∈M_n^S`. Hence `M_n^{(S,S')}∩I_S=M_n^S`, giving
`𝓐_n=𝓜_n^S`; symmetrically `𝓑_n=𝓜_n^{S'}`. So
`𝓜_n^{(S,S')}=𝓜_n^S⊔𝓜_n^{S'}` for every `n`. The eventual-constancy
equivalence follows immediately: `𝓜_n^S` is recoverable from
`𝓜_n^{(S,S')}` by the fixed rule `T↦[T∩P_1=S]`, so joint constancy implies
constancy of each side; conversely eventual constancy of both sides at
indices `N_1,N_2` gives joint constancy at `\max(N_1,N_2)`. ∎

## Independent re-verification (proof-reviewer, round 5)

Re-derived the "no cross-side domination" argument and the antichain
splitting from scratch — correct, short, no gap.

Independently re-implemented (fresh Python, `sympy.primefactors`, no reuse
of the builder's script) all three antichains (`𝓜_n^{(S,S')}`, `𝓜_n^S`,
`𝓜_n^{S'}`) and checked the identity `𝓜_n^{(S,S')}=𝓜_n^S⊔𝓜_n^{S'}` at
multiple checkpoints for:
- `a_1=247` (`P_1=\{13,19\}`): `𝓜_n^{\{13\}}` and `𝓜_n^{\{19\}}` both
  stabilize to 3-element antichains at `n∈\{50,200,1000,3000,6000\}` — exact
  match with the joint antichain (6 elements) at every checkpoint.
- `a_1=2747` (`P_1=\{41,67\}`): `𝓜_n^{\{41\}}` stabilizes to
  `\{\{2,41\},\{3,41\},\{7,41\}\}` at the **exact** position `154` claimed
  by the source file; `𝓜_n^{\{67\}}` stabilizes to `\{\{2,3,7,67\}\}` at
  position `0`; joint union `H^{(41,67)}=\{2,3,7,41,67\}` matches exactly.

Both independent checks reproduce the source file's numbers exactly, zero
discrepancies.

## Caution flagged by the proof-reviewer (round 5, does not affect this
lemma's certification)

The source file's round-5 §E investigation of `a_1=21528751` mislabels its
reported "single-class antichain `𓜓_n^{\{103\}}`" data: the numbers
reported there (`1103→8` collapse at `n≈27831`, further changes to
`n≈44966`) match, almost index-for-index, an **independent re-computation
of the plain GLOBAL antichain `𓜓_n`** (no class restriction at all), not
the properly `I_S`-restricted local antichain as this Lemma defines it. The
proof-reviewer independently computed the **correctly** `I_{\{103\}}`-
restricted local antichain for `a_1=21528751` (fresh Python, verified
against the fast/slow-algorithm agreement check on `a_1=91`,`247`,`2747`
first) and found a **different**, cleaner trajectory: the local antichain
grows to `1092` elements and collapses **directly to `3`** (not `8`, and
with no further changes through at least `n=30000`, not the reported
`8→9` at `n≈29214` or lateral swap at `n≈44966`). This is a factual
correction to the *numerical report* in `forced-primes-well-ordering.md`
§E, not to this certified Lemma (whose deductive proof is verified correct
independently of that specific example) — see
`results/imo-2026-06/current.md` round-5 update and the proof-reviewer's
round-5 report for detail. Future rounds should not cite the `a_1=21528751`
"local `\{103\}`" numbers from the source file without recomputing them.

## Certification

Certified `solved`-quality, unconditional. General-purpose: applies to any
disjoint nonempty `S,S'⊆P_1` for any sequence satisfying this problem's
hypotheses.

## Source

`results/imo-2026-06/approaches/forced-primes-well-ordering.md` (round 5).
