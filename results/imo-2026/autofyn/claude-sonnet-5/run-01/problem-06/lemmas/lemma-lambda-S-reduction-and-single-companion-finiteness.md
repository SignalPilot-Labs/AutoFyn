# Λ_S-Reduction Lemma, Single-Companion Finiteness Lemma, Multi-Companion Reduction Proposition

**Source.** `results/imo-2026-06/approaches/persistent-backbone-monovariant.md`
(round 6). Depends on: already-certified Generalized Lemma C
(`lemmas/lemma-C-generalized-subsequence.md`), Lemma P′
(`lemmas/lemma-P-prime-pairwise-intersecting.md`), Theorem CD
(`lemmas/theorem-CD-core-decomposition-and-lemma-TC.md`).

## Notation

Fix a proper nonempty core `S⊊P_1`. `𝓥_S` is the set of all radical values
ever inclusion-minimal with `P_1`-imprint exactly `S` (Theorem CD notation).
`J_S := {j≥1 : rad(a_j)∩S=∅}` (the *S-avoiding index set*).
`Q_S := {q prime, q∉P_1 : ∃i≥1, rad(a_i)=S∪{q}}` (primes ever realized as
the *sole* companion of `S`).

## Λ_S-Reduction Lemma

**Statement.** `Λ_S := ⋃_{C∈𝓥_S} (C∖S)`. Then `𝓥_S` is finite **iff** `Λ_S`
is finite.

**Proof.**
`(⇒)` If `𝓥_S` is finite, `Λ_S` is a union of finitely many finite sets
`C∖S`, hence finite.
`(⇐)` Suppose `Λ_S` finite. Every `C∈𝓥_S` has `S(C)=S`, so `S⊆C`, giving
`C=S∪(C∖S)` with `C∖S⊆Λ_S`. So `𝓥_S ⊆ {S∪Q : Q⊆Λ_S}`, a set of size
`2^{|Λ_S|}` (finite). A subset of a finite set is finite. ∎

## Single-Companion Finiteness Lemma

**Statement.** If `J_S` is infinite, then `Q_S` is finite; explicitly,
`Q_S ⊆ D∖P_1` where `D := ⋂_{j∈J_S} rad(a_j)`, a fixed finite set with
`|D| ≤ ω(a_{j_1})` (`j_1:=min J_S`).

**Proof.** List `J_S={j_1<j_2<⋯}`. Apply the Generalized Lemma C to
`I:=J_S`: `C^{J_S}_m := ⋂_{l=1}^m rad(a_{j_l})` is non-increasing and
stabilizes at some finite `m_0`, `C^{J_S}_m=D` for `m≥m_0`.

*Claim: `D=⋂_{j∈J_S} rad(a_j)` (the full infinite intersection).* For
`l≤m_0`: `D⊆rad(a_{j_l})` directly. For `l>m_0`: stabilization gives
`D=D∩rad(a_{j_l})`, so `D⊆rad(a_{j_l})`. Hence `D⊆⋂_{j∈J_S}rad(a_j)`; the
reverse inclusion is immediate (full intersection ⊆ partial intersection
over the first `m_0` indices `=D`). So equality holds, and
`D⊆rad(a_{j_1})` gives `|D|≤ω(a_{j_1})`.

Now let `q∈Q_S`: some index `i` has `rad(a_i)=S∪{q}`. Since `S≠∅`,
`rad(a_i)∩S=S≠∅`, so `i∉J_S`, hence `i≠j` for every `j∈J_S`. By Lemma P′,
`gcd(a_i,a_j)>1` for every `j∈J_S`, i.e. `(S∪{q})∩rad(a_j)≠∅`. Since
`S∩rad(a_j)=∅` (`j∈J_S`), the nonempty intersection must come from `{q}`,
i.e. `q∈rad(a_j)` for every `j∈J_S`, so `q∈D`. Also `q∉P_1` (definition of
`Q_S`). Hence `Q_S⊆D∖P_1`. ∎

**Independent numerical verification (proof-reviewer, round 6, fresh code,
own sequence simulation, not reused from the builder's script).**
- `a_1=2747`, `S={41}` (`P_1={41,67}`): `J_S` has 118 elements among the
  first 6000 terms, `D={2,3,7,67}`, predicted `Q_S⊆D∖P_1={2,3,7}`; direct
  search of all 6000 terms for radicals `{q,41}` gives exactly
  `Q_S={2,3,7}` — **exact match**.
- `a_1=247`, `S={13}` (`P_1={13,19}`): `J_S` has 2074 elements, `D={19}`,
  predicted `Q_S⊆∅`; direct search gives `Q_S=∅` — exact match.
- `a_1=247`, `S={19}`: symmetric, `J_S` has 3228 elements, `D={13}`,
  predicted `Q_S⊆∅`; direct search gives `Q_S=∅` — exact match.

All three checks reproduce the builder's claimed exact matches independently.

## Multi-Companion Reduction Proposition

**Statement.** Let `Q` be a finite set of primes with `Q∩(P_1∪S)=∅` and
`|Q|≥2`, and suppose some index `i` has `rad(a_i)=S∪Q`. Then
`Q∩rad(a_j)≠∅` for every `j∈J_S`.

**Proof.** Since `S≠∅`, `i∉J_S`, so `i≠j` for `j∈J_S`; Lemma P′ gives
`gcd(a_i,a_j)>1`, i.e. `(S∪Q)∩rad(a_j)≠∅`. Since `S∩rad(a_j)=∅` (`j∈J_S`),
the nonempty intersection comes from `Q`. ∎

**Why this does not extend the Single-Companion mechanism (honest scope
note, not a gap in this proposition itself).** For `|Q|=1`, this recovers
the single-companion result (a fixed element in every `rad(a_j)`, `j∈J_S`
— exactly the hypothesis Generalized Lemma C's stabilization needs). For
`|Q|≥2`, the conclusion only forces `Q` to *hit* each `rad(a_j)` — possibly
via a different element for each `j` — which is a finite covering/hitting-set
condition on the infinite family `{rad(a_j):j∈J_S}`, i.e. a local, restricted
instance of the Finite Covering Backbone Conjecture itself. The Generalized
Lemma C mechanism does not apply to a hitting-set condition (only to
fixed-intersection stabilization), so this proposition does **not** extend
to multi-companion bundles — it precisely proves that any such extension is
of the same order of difficulty as FCBC itself.

**Second honest gap (unresolved).** "`J_S` is infinite" is not proved for a
general proper core `S⊊P_1` — verified numerically in every core tested
(`J_S` in the thousands, still growing) but not established in general.

## Certification

All three statements independently re-derived and, for the two exact-match
numerical claims, independently re-simulated from scratch by the round-6
proof-reviewer with fresh code — zero discrepancies. No circularity, no
overclaiming (the honest scope notes accurately describe what is and is not
established). Certified `solved`-quality for the three proved statements;
the two flagged gaps (multi-companion extension, `J_S` infinitude in
general) remain open and are not claimed as proved.
