## Lemma: Two-Sided Singleton Witness Theorem (CERTIFIED, round 19 — content from round 18)

**Source.** `triangle-consistency-pigeonhole`, round 18, §3. Independently
re-verified by the round-19 proof-reviewer, including independent
reproduction of both computational checks below.

**Depends on (certified).** `singleton-side-fah.md` (applied twice, with
non-canonical/non-earliest witnesses on each side — legitimate since that
Lemma's own proof only ever uses that the witness index is *some* fixed
index of the required type, not that it is the earliest one);
`cofinite-sufficiency-lemma.md` (Cofinite FAH suffices for the existing
finish).

**Setup.** `(A,B)` a rogue pair at core `S_0`.

**Statement (conditional on an explicit existence hypothesis).** Suppose
there exist an index `x_1` with `ρ(x_1)=B` and `P(a_{x_1})\S_0={q}`
(singleton), and an index `x_2` with `ρ(x_2)=A` and `P(a_{x_2})\S_0={q}` —
the SAME prime `q`. Then `q | a_n` for every `n>x_1` with `ρ(n)=A`, and
`q | a_n` for every `n>x_2` with `ρ(n)=B`. In particular Cofinite FAH holds
for `(A,B)` with witness `q`.

**Proof.** The first conclusion is Singleton-Side FAH applied with far-side
witness `n_B := x_1` (its hypothesis `F''={q}` holds by assumption); the
second is Singleton-Side FAH's symmetric statement with far-side witness
`n_A := x_2`. Both are direct citations, no new machinery. Since `X_A, X_B`
are infinite, `X_A ∩ [1,x_1]` and `X_B ∩ [1,x_2]` are finite, so all but
finitely many occurrences of each side are covered; Cofinite Sufficiency
gives Cofinite FAH for the pair. ∎

**Verification (independently reproduced by this review).** On `a_1=4807`
(`S_0={2,3,5,11,19,23}`, `A'={3,5,19}`, `B'={2,11}`): canonical witness
`n_A=6` has `F'_6={17}`; among `B'`-occurrences to `n=8000`, `x_1=72` has
singleton signature `{17}`. Applying the theorem with `q=17`: zero
exceptions among 13 `A'`- and 180 `B'`-occurrences sampled. On `a_1=11305`
(`S_0={2,3,5,7,13,17,19,23,29,37,43,101}`, `A'={2,5}`, `B'={3,7}`): canonical
`n_B=4` has `F''_4={11}`; `x_2=103` (an `A'`-occurrence) has singleton
signature `{11}`. Applying with `q=11`: zero exceptions among 247
`A'`-occurrences and 79-80 `B'`-occurrences (a one-count discrepancy,
immaterial to the zero-exception claim).

**Scope note.** The hypothesis (existence of a matching pair of singleton
out-of-core witnesses) is a genuine, unproved, narrower existence question —
NOT shown equivalent to (nor a restatement of) the general FAH crux. It is
strictly weaker than requiring the *canonical* witnesses to be singleton,
since any later occurrence may serve.

**Status.** Correct, complete, and non-circular GIVEN its stated existence
hypothesis (which remains open — this is a conditional theorem, matching the
workspace's precedent for conditional lemmas such as `self-absorbing-core-
theorem.md`). Fully explains both of the workspace's only two known
properly-recruited-core hard rogue-pair test seeds. Certified as a
standalone reusable conditional theorem.
