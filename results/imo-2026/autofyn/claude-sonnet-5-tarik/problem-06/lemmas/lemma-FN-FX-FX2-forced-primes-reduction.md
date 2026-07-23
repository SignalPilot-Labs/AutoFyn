# Lemmas FN, FX, FX2 (forced-primes channel reduction)

Notation: `P_1 := rad(a_1)`, `k := |P_1| = ω(a_1)`. For `i≥1`, the
**`P_1`-imprint** `G_i := rad(a_i)∩P_1` (nonempty for every `i` by Lemma P).
For `M≥1`, `F_M := {p prime : ∃ 1≤i<j≤M, rad(a_i)∩rad(a_j)={p}}`; `F_M` is
non-decreasing in `M`, and `F := ⋃_{M≥1} F_M`.

## Lemma FN (necessity)

**Statement.** Every finite set `H` satisfying the FCBC covering property
(`H∩rad(a_i)∩rad(a_j)≠∅` for every `i<j`) contains `F`.

**Proof.** If `p∈F`, some pair `i<j` has `rad(a_i)∩rad(a_j)={p}`. If `H`
covers this pair, `H∩{p}≠∅`, so `p∈H`. `∎`

## Lemma FX (disjoint-imprint necessity for external forcing)

**Statement.** If `p∈F\P_1`, witnessed by `i<j` with `rad(a_i)∩rad(a_j)={p}`,
then `G_i∩G_j=∅`.

**Proof.** If `q∈G_i∩G_j`, then `q∈P_1` and `q∈rad(a_i)∩rad(a_j)={p}`, so
`q=p`; but `q∈P_1` while `p∉P_1` — contradiction. `∎`

**Corollary (finite channel bound).** Calling an ordered pair `(S,S')` of
nonempty disjoint subsets of `P_1` a *channel* (at most `3^k` channels, since
each of `P_1`'s `k` elements is independently in `S`, `S'`, or neither), every
`p∈F\P_1` is witnessed by a pair `(i,j)` whose imprints `(G_i,G_j)` form one
of these `≤3^k` channels. Hence `F` is finite iff `F_{S,S'}` (the forced
primes witnessed within channel `(S,S')`) is finite for each of the (at most
`3^k`, depending only on `a_1`) channels.

## Lemma FX2 (finite imprint classes are automatically resolved)

For nonempty `S⊆P_1`, let `I_S := {i≥1 : G_i=S}`.

**Statement.** If `I_S` is finite, then for every disjoint `S'`,
`F_{S,S'}∪F_{S',S} ⊆ ⋃_{i∈I_S} rad(a_i)`, a finite set.

**Proof.** If `p∈F_{S,S'}` witnessed by `i∈I_S,j∈I_{S'}` with
`rad(a_i)∩rad(a_j)={p}`, then `p∈rad(a_i)⊆⋃_{i'∈I_S}rad(a_{i'})`, finite
since `I_S` is finite. Symmetric for `F_{S',S}`. `∎`

**Consequence.** Since the (finitely many) classes `I_S` partition the
infinite index set `ℕ`, at least one class is infinite; every channel
touching a *finite* imprint class is already resolved. Only channels between
two *doubly-infinite* disjoint imprint classes remain open.

**Source.** `results/imo-2026-06/approaches/forced-primes-well-ordering.md`
(round 3).

**Certification.** Independently re-derived and checked line by line
(elementary set-theoretic arguments, no numerical dependency). The corollary
numeric example (`a_1=221`, pair `(4,5)`, `p=5`, `G_4={17}`, `G_5={13}`;
`a_1=375`, pair `(3,7)`, `p=19`, `G_3={5}`, `G_7={3}`) was independently
re-verified by the reviewer via direct computation, exact match. No gaps.
Certified `solved`-quality (sorry-free), unconditional structural results
(no open hypothesis used). Reduces "is `F` finite?" from an unbounded search
to at most `3^k` independent channel sub-questions, with the finite-class
channels already free. The remaining doubly-infinite-class channels are
still open (Gap 1 of the population).
