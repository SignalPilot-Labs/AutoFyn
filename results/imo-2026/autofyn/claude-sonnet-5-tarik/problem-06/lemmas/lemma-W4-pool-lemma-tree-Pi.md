# Lemma W4 (the tree `T_Π` and the Pool Lemma)

## Notation

`P_i:=rad(a_i)`. For a fixed finite set of primes `Π` and `N≥1`, define
`𝒢_N(Π):={S⊆Π : S∩P_i∩P_j≠∅ for every 1≤i<j≤N}` (the subsets of `Π`
covering every pair among the first `N` terms).

## Lemma W4a (monotonicity)

**Statement.** For every `N≥1` and every finite `Π`, `𝒢_{N+1}(Π)⊆𝒢_N(Π)`.

**Proof.** If `S∈𝒢_{N+1}(Π)`, `S` covers every pair `i<j≤N+1`; in
particular every pair `i<j≤N` (a subset of the constraints), so `S∈𝒢_N(Π)`.
`∎`

## Lemma W4b (Pool Lemma)

**Statement.** FCBC holds if and only if there exists a finite set of
primes `Π` such that `𝒢_N(Π)≠∅` for every `N≥1`.

**Proof.**

`(⇒)` If `H` is a finite covering set, take `Π:=H`. For every `N`, `S:=H`
satisfies `S⊆Π` and covers every pair `i<j≤N` (a fortiori, since `H` covers
every pair unrestricted), so `H∈𝒢_N(Π)`.

`(⇐)` Suppose `Π` is finite with `𝒢_N(Π)≠∅` for every `N`. By Lemma W4a,
`(𝒢_N(Π))_{N≥1}` is a nested-decreasing sequence of subsets of the finite
set `2^Π`, so `(|𝒢_N(Π)|)_{N≥1}` is a non-increasing sequence of
non-negative integers bounded above by `2^{|Π|}` — hence eventually
constant (identical finite-descent technique to certified Lemma C). Let
`N_0` be a stabilization point: `𝒢_N(Π)=𝒢_{N_0}(Π)=:𝒢_∞` for all `N≥N_0`
(equal cardinality plus nestedness forces literal set equality, not just
equal size). `𝒢_∞≠∅` by hypothesis.

Pick any `S∈𝒢_∞`. Fix `i<j`; let `N:=max(N_0,j)≥N_0`, so `𝒢_N(Π)=𝒢_∞∋S`.
By definition of `𝒢_N(Π)`, `S` covers every pair `i'<j'≤N`; since `j≤N`,
`(i,j)` is among these, so `S∩P_i∩P_j≠∅`. As `i<j` were arbitrary, `S` is a
finite covering set, establishing FCBC. `∎`

**Discussion.** The `(⇐)` direction needs only elementary finite descent
(the node space `2^Π` is finite *in total*, not merely finitely branching
per level), no genuine use of the infinitary König's lemma. The `(⇒)`
direction is immediate (`Π:=H`), so this is a genuine **equivalence**, not a
one-directional reduction: proving "some finite `Π` works" is provably
exactly as hard as proving FCBC directly, not an easier intermediate
target. This is architectural clarification (a correct, complete,
finitely-branching tree formalization answering an outline-reviewer's
caveat), not progress on the difficulty of FCBC itself — the source file is
explicit and correct about this scoping.

## Independent re-verification (reviewer, round 4)

Re-derived Lemma W4a and W4b from scratch by hand; no gaps. Re-implemented
independently in Python (exact integer factorization, brute-force subset
enumeration) and reproduced, for `a_1=15`, `Π={2,3,5}`: `𝒢_N(Π)` is
nested-decreasing and stabilizes to the singleton `{2,3,5}}` (matching the
source's claimed `|Π|=3`, nonempty stabilized limit) — confirms the Lemma's
mechanics reproduce correctly on a concrete instance, in addition to the
hand-verified abstract proof.

## Source

`results/imo-2026-06/approaches/explicit-window-backbone-construction.md`
(round 4).

## Certification

Certified `solved`-quality (sorry-free), **unconditional**: Lemma W4a/W4b
hold for *any* fixed finite `Π`, with no dependency on FCBC or any other
open hypothesis. Reusable by any future approach wanting a precise,
checkable finite-branching/compactness formalization for FCBC. Note for
future rounds: this lemma proves the "does the tree architecture work"
question is fully closed (it does, given any `Π`) — the only remaining
content is, provably, exactly as hard as FCBC itself (existence of a
suitable `Π`), not a weaker sub-question. Do not treat Lemma W4 as narrowing
FCBC's difficulty; treat it only as a clean reformulation.
