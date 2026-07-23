# Lemma SR (Self-Realized Core Shortcut)

**Source.** `results/imo-2026-06/approaches/sunflower-bundle-closure.md`
(round 8, §2). Depends only on the already-certified No-Resurrection Lemma
(part of `lemmas/theorem-V-veto-finite-iff-MRS.md`) and the definitions in
`lemmas/theorem-CD-core-decomposition-and-lemma-TC.md`.

## Statement

Fix a proper nonempty core `S⊊P_1`. If `S` is itself **realized** in the
sense of `lemmas/lemma-ERD-realized-blocked-dichotomy.md` (some index `n_0`
has `rad(a_{n_0})=S` exactly), then `𝓥_S` is finite; explicitly
`𝓥_S⊆{S}∪⋃_{n=1}^{n_0-1}𝓜_n`, a finite set.

## Proof

Let `C∈𝓥_S` with `C≠S`. Since `S=C∩P_1⊆C` always (by definition of `𝓥_S`,
`S(C)=C∩P_1=S`) and `C≠S`, `S⊊C` strictly. Since `C∈𝓥`, `C∈𝓜_n` for some
`n≥1` (definition of `𝓥` as the union of `𝓜_n`). If `n≥n_0`:
`rad(a_{n_0})=S⊊C`, so the No-Resurrection Lemma (dominating witness
`k:=n_0≤n`) gives `C∉𝓜_n`, a contradiction. So `n<n_0`, i.e.
`n∈{1,…,n_0-1}`, giving `C∈𝓜_n⊆⋃_{n=1}^{n_0-1}𝓜_n`. Hence every element of
`𝓥_S` other than `S` itself lies in the fixed finite set
`⋃_{n=1}^{n_0-1}𝓜_n` (a union of `n_0-1` finite sets). `∎`

**No hypothesis beyond `S` being realized is used** — in particular no
companion-bundle-size or witness-existence hypothesis plays any role.

## Certification

Fully proved, from already-certified facts, no circularity. Independently
re-verified by the round-8 proof-reviewer (re-derived from scratch, no gap).
General-purpose: applies to any proper core in any instance of this
problem's hypotheses. Certified `solved`-quality.

**Cross-approach synergy (proof-reviewer finding, round 8).** Combined with
`lemmas/lemma-ERD-realized-blocked-dichotomy.md`, this lemma shows that the
"existence of a core-avoiding witness for `S`" open sub-lemma flagged by
both `persistent-backbone-monovariant`'s and `forced-primes-well-ordering`'s
round-8 outlines is **not actually needed as an independent hypothesis**:
for any proper core `S`, either `S` is realized (in which case this Lemma
closes `𝓥_S`-finiteness directly, with no witness needed at all) or `S` is
blocked (in which case the Realized–Blocked Dichotomy Lemma supplies a
witness `j_3` automatically, with no separate existence proof required).
`persistent-backbone-monovariant`'s round-8 "open gap (1)" (general
core-avoiding-witness existence) is therefore fully dissolved by combining
this Lemma with its own already-certified RBD Lemma — see
`current.md`'s Round 8 update for the full argument. This does not, by
itself, close `persistent-backbone-monovariant`'s remaining open hypothesis
NIBC, nor does it change the "transient bundles are invisible" finding —
only the witness-existence sub-lemma is dissolved.
