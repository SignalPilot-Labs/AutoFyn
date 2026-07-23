# Lemma W2 (Patch Lemma) and Lemma W3 (Minimal Radical Reduction Lemma)

Notation as in `lemma-W1-equivalence-key-lemma-FCBC.md`.

## Lemma W2 (Patch Lemma)

**Statement.** Fix `K≥1` and suppose `H_K∩P_i∩P_j=∅` for some `i<j`. Then
`i>K`, and setting `K':=i`, `H_{K'}∩P_i∩P_j≠∅`.

**Proof.** If `i≤K`, then `P_i⊆H_K`; by Lemma P′, `P_i∩P_j≠∅`, and any
element of this set lies in `P_i⊆H_K`, contradicting `H_K∩P_i∩P_j=∅`. So
`i>K`. Now with `K':=i`, `P_i⊆H_{K'}` (since `i≤K'`), and by Lemma P′ again
`P_i∩P_j≠∅`; any element of it lies in `H_{K'}∩P_i∩P_j`. `∎`

**Discussion.** Every individual coverage failure of `H_K` is repairable by
one explicit enlargement; this isolates the open content of the Key Lemma to
"only finitely many repairs are ever needed" (still open — the natural
candidate monovariants `|H_K|`, `2^{|H_K|}-1` are non-decreasing in `K`, the
wrong direction for a Lemma-C-style finite-descent argument; this is a
diagnostic finding, not a proof that no monovariant exists).

## Lemma W3 (Minimal Radical Reduction Lemma)

**Statement.** Fix `n≥1`. Call `i∈{1,…,n}` *n-minimal* if there is no
`k∈{1,…,n}` with `P_k⊊P_i`. Let `M_n` be the set of `n`-minimal indices.
Then for every positive integer `x`: `[gcd(x,a_i)>1 ∀i≤n] ⟺ [gcd(x,a_i)>1
∀i∈M_n]`.

**Proof.** `(⇒)` trivial since `M_n⊆{1,…,n}`.

`(⇐)` Suppose `gcd(x,a_i)>1` for every `i∈M_n`. Fix arbitrary `i_0∈{1,…,n}`.
Let `S:={k∈{1,…,n}:P_k⊆P_{i_0}}` (nonempty, `i_0∈S`). Choose `j*∈S`
minimizing `|P_{j*}|`. If `j*∉M_n`, some `k∈{1,…,n}` has `P_k⊊P_{j*}⊆P_{i_0}`,
so `k∈S` with `|P_k|<|P_{j*}|`, contradicting minimality — so `j*∈M_n`.
Hence `gcd(x,a_{j*})>1`: some `p∈P_{j*}` divides `x`. Since `P_{j*}⊆P_{i_0}`,
`p∈P_{i_0}`, i.e. `p∣a_{i_0}`, so `gcd(x,a_{i_0})≥p>1`. As `i_0` was
arbitrary, done. `∎`

**Discussion.** Unconditional structural fact (no FCBC dependence): the
admissibility check at each step only depends on the inclusion-minimal
radicals seen so far. Does **not** by itself bound anything — `|M_n|` was
observed (numerically, not part of this certification) to keep growing with
`n` for `a_1=221` (`|M_{199}|=42`).

**Source.** `results/imo-2026-06/approaches/explicit-window-backbone-construction.md`
(round 3).

**Certification.** Both proofs independently re-derived and checked line by
line (elementary combinatorial arguments, no numerical dependency, correctly
using already-certified Lemma P′). No gaps. Certified `solved`-quality
(sorry-free), unconditional. Reusable general structural facts, independent
of whether FCBC is ever resolved.
