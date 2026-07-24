## Lemma: Vacuous/Weak Self-Absorption Lemma (certified, round 17)

**Source.** `self-absorbing-by-construction`, round 17 build. Independently
re-derived in full by the round-17 proof-reviewer; no gap found.

**Depends on.** Only the definitions already fixed by the certified stack:
`Q := P(a_1)`, the base type `τ(n) := P(a_n) ∩ Q`, the Persistent-Type
Pigeonhole (`persistent-type-pigeonhole.md`, giving the finite threshold
`N(Q)`), and the absorption operator `S⁺ := S ∪ ⋃_{j=1}^{N(S)} P(a_j)` from
`self-absorbing-core-theorem.md`. Fully unconditional — no FAH hypothesis, no
open hypothesis of any kind.

**Statement.** If `N(Q) ≤ 1`, then `S_0 := Q` is self-absorbing (`Q⁺ = Q`),
and hence the absorption chain `S_0 ⊆ S_1 ⊆ ...` (via `S_{k+1} := S_k⁺`) is
constant, terminating in **zero** rounds with terminal core `S* = Q` and
`N(S*) = N(Q) ≤ 1`. In particular, the Termination Criterion Lemma's
hypothesis (boundedness of `(N(S_k))_k`) holds trivially in this case.

**Proof.** Two mutually exclusive, exhaustive cases (`N(Q)` is a specific
nonnegative integer, so `N(Q) ≤ 1` means exactly `N(Q) = 0` or `N(Q) = 1`).

- `N(Q) = 0`: `⋃_{j=1}^{0} P(a_j)` is a union over the empty index range
  `{j : 1 ≤ j ≤ 0}`, hence `= ∅`. So `Q⁺ = Q ∪ ∅ = Q` — self-absorption holds
  vacuously (the defining condition "`P(a_j) ⊆ Q` for `j=1,...,N(Q)`" is true
  because it quantifies over an empty range).
- `N(Q) = 1`: `⋃_{j=1}^{1} P(a_j) = P(a_1) = Q` (the last equality is the
  very definition of `Q`). So `Q⁺ = Q ∪ Q = Q` — self-absorption holds
  automatically (the range is nonempty, but the single required containment
  `P(a_1) ⊆ Q` is immediate from the definition of `Q`).

In both cases `Q⁺ = Q`, so by induction `S_k = Q` for every `k ≥ 0`: the
absorption chain is constant from the start, terminating at `k = 0` with
`S* = Q`, `N(S*) = N(Q) ≤ 1`. ∎

**What this resolves.** Gives the sharp, minimal sufficient condition
(`N(Q) ≤ 1`, not just the a priori stronger `N(Q) = 0`) for hypothesis H2
(absorption-chain termination, `n1-periodicity-reconciliation`) to hold
outright, with the smallest possible terminal core `S* = Q` — no enlargement
of the core needed. Reduces the remaining content, in this case, to exactly
standard FAH at `S* = Q` (hypothesis H1 alone).

**What this does NOT resolve (honest, not overclaimed).** Whether `N(Q) ≤ 1`
holds for every `a_1 > 1` is the open **NTBT conjecture**
(`self-absorbing-by-construction.md` §3) — NOT established by this lemma or
anywhere else in the workspace. This lemma is a one-way sufficient condition,
proved unconditionally; it does not by itself establish that the sufficient
condition's hypothesis is ever met beyond the trivial verification on
specific numeric seeds recorded in the source file.

**Verification note (round 17 proof-reviewer, CERTIFIED).** Independently
re-derived both cases from scratch; the proof is a direct, gap-free unpacking
of the definitions of `Q`, the absorption operator, and `N(S)`. No
circularity, no smuggled step. The union-indexing edge case (`N(Q)=0` giving
an empty union) and the definitional identity `P(a_1) = Q` (`N(Q)=1` case)
were both checked explicitly and hold as claimed. **Certified**, no changes
to the mathematical content.
