# Channel Assembly Theorem (local channel stabilization ⟹ global FCBC)

## Status

Certified `solved`-quality (sorry-free), unconditional **given** its
antecedent `(LMRS_{S,S'})` for every channel (that antecedent is itself
open — see `results/imo-2026-06/current.md`).

## Notation

`P_1:=rad(a_1)`, `k:=ω(a_1)`. For `i≥1`, `G_i:=rad(a_i)∩P_1` (nonempty by
Lemma P). For nonempty `S⊆P_1`, `I_S:=\{i:G_i=S\}` (a partition of `ℕ` into
`≤2^k-1` classes). A **channel** is an unordered pair `\{S,S'\}` of disjoint
nonempty subsets of `P_1` (`≤3^k` of them). For channel `\{S,S'\}`,
`J:=I_S∪I_{S'}`; `M_n^{(S,S')}⊆J∩[1,n]` are the `(n,S,S')`-minimal indices
(no `k∈J∩[1,n]` has `rad(a_k)⊊rad(a_i)`); `𝓜_n^{(S,S')}` the corresponding
value-antichain. **Hypothesis `(LMRS_{S,S'})`**: `𝓜_n^{(S,S')}` is
eventually constant, `=:𝓜_∞^{(S,S')}`, `H^{(S,S')}:=⋃𝓜_∞^{(S,S')}`.

## Statement

If `(LMRS_{S,S'})` holds for **every** channel of `P_1` (a fixed, finite,
`≤3^k`-size family determined by `a_1` alone), then
`H:=P_1∪⋃_{\{S,S'\}}H^{(S,S')}` is a finite set satisfying FCBC:
`H∩rad(a_i)∩rad(a_j)≠∅` for every `1≤i<j`.

## Proof

*Local Corollary W3′* (verbatim adaptation of the certified global Corollary
W3′, replacing `\{1,…,n\}` by `J∩[1,n]`): for every `n` and `i_0∈J∩[1,n]`,
there is `j^*∈M_n^{(S,S')}` with `rad(a_{j^*})⊆rad(a_{i_0})`.

*Local Lemma MS* (verbatim adaptation of the certified global Lemma MS): if
`(LMRS_{S,S'})` holds, `H^{(S,S')}` is finite and covers every pair `i≠j`
in `J` — via Local Corollary W3′ (every `i∈J` is dominated by some
`S_i∈𝓜_∞^{(S,S')}`) plus pairwise intersection of `𝓜_∞^{(S,S')}`'s elements
(each is `rad(a_k)` for an actual index `k`; distinct elements intersect by
the already-certified global Lemma P′, applied to the pair of underlying
indices).

*Assembly.* `H` is finite (finite union, `≤3^k` terms, of finite sets `P_1`
and each `H^{(S,S')}`). Fix `i<j`; suppose `H∩rad(a_i)∩rad(a_j)=∅`. Since
`P_1⊆H`, the already-certified **Lemma FH**
(`lemmas/lemma-FH-uncovered-pair-localization.md`) gives `G_i∩G_j=∅`. Since
`G_i,G_j` are nonempty and disjoint subsets of `P_1`, `\{G_i,G_j\}` is a
channel; `i,j∈J:=I_{G_i}∪I_{G_j}`. By hypothesis `(LMRS_{G_i,G_j})` holds,
so Local Lemma MS gives `H^{(G_i,G_j)}∩rad(a_i)∩rad(a_j)≠∅`; since
`H^{(G_i,G_j)}⊆H`, this contradicts the assumption. So `H` covers every
pair. ∎

## Independent re-verification (proof-reviewer, round 5)

Re-derived the local domination lemma, local Lemma MS, and the assembly
step from scratch — each is a faithful, valid restriction/reuse of the
already-certified global machinery (Corollary W3′, Lemma MS, Lemma P′,
Lemma FH), with no hidden dependency between distinct channels' hypotheses
(each channel's construction only references indices in its own `J` and
the unconditional global Lemma P′). No gap found.

## Certification

Certified `solved`-quality, conditional (on `(LMRS_{S,S'})` for every
channel — itself reduced further by the Channel Splitting Lemma, see
`channel-splitting-lemma.md`). General-purpose: applies to any sequence
satisfying this problem's hypotheses (Lemma P/P′), not specific to any
particular `a_1`.

## Source

`results/imo-2026-06/approaches/forced-primes-well-ordering.md` (round 5).
