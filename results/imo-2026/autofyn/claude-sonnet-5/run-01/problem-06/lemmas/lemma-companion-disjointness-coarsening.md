# Companion-Disjointness Coarsening Lemma (+ Bucket-Exclusion Corollary)

**Source.** `results/imo-2026-06/approaches/forced-primes-well-ordering.md`
(round 6, §F). Depends on the already-certified Lemma P′
(`lemmas/lemma-P-prime-pairwise-intersecting.md`) and the
Permanent-Inadmissibility Lemma
(`lemmas/lemma-permanent-inadmissibility.md`).

## Setup

Fix a proper nonempty core `S⊊P_1`. `G_i:=rad(a_i)∩P_1` (nonempty for every
`i`, Lemma P). `I_S:={i:G_i=S}`. For any index `j`,
`comp(a_j):=rad(a_j)∖P_1`.

## The Coarsening Lemma

**Statement.** Suppose there exist indices `j_1≠j_2` with
`G_{j_1}∩S=G_{j_2}∩S=∅` and `comp(a_{j_1})∩comp(a_{j_2})=∅`, with both
`comp(a_{j_1})`, `comp(a_{j_2})` nonempty. Then for **every** `i∈I_S` (at
any index, past or future), there exist `p∈comp(a_{j_1})`,
`p'∈comp(a_{j_2})` with `{p,p'}⊆rad(a_i)`. Consequently every
`T∈𝓜_n^S` (for every `n`) satisfies `T⊇S∪\{p,p'\}` for some
`(p,p')∈comp(a_{j_1})×comp(a_{j_2})` — i.e. the antichain refines a fixed
finite set of at most `|comp(a_{j_1})|·|comp(a_{j_2})|` "coarse buckets"
`𝒦:={S∪\{p,p'\} : p∈comp(a_{j_1}), p'∈comp(a_{j_2})}`.

**Proof.** Fix `i∈I_S`, so `rad(a_i)=S∪Q` for `Q:=rad(a_i)∖P_1` (disjoint
from `P_1`). By Lemma P′, `gcd(a_i,a_{j_1})>1`, i.e.
`rad(a_i)∩rad(a_{j_1})≠∅`. Expanding:
`rad(a_i)∩rad(a_{j_1}) = (S∩G_{j_1}) ∪ (S∩comp(a_{j_1})) ∪ (Q∩G_{j_1}) ∪ (Q∩comp(a_{j_1}))`.
`S∩G_{j_1}=∅` (hypothesis); `S∩comp(a_{j_1})=∅` (`S⊆P_1`,
`comp(a_{j_1})∩P_1=∅`); `Q∩G_{j_1}=∅` (`Q∩P_1=∅`, `G_{j_1}⊆P_1`). So
`Q∩comp(a_{j_1})≠∅`: some `p∈comp(a_{j_1})∩Q`. Symmetrically with `j_2`:
some `p'∈comp(a_{j_2})∩Q`. Since `comp(a_{j_1})∩comp(a_{j_2})=∅`, `p≠p'`,
and both lie in `rad(a_i)=S∪Q`. So `rad(a_i)⊇S∪\{p,p'\}` as claimed. The
antichain statement follows since `𝓜_n^S⊆{rad(a_i):i∈I_S}`. ∎

**Degenerate-case remark.** If `comp(a_{j_1})=∅` while `G_{j_1}∩S=∅`, the
same computation gives `rad(a_i)∩rad(a_{j_1})=∅` for any `i∈I_S`,
contradicting Lemma P′ — so if such `j_1` exists, `I_S=∅` (the core is never
realized; `(MRS_S)` holds vacuously). This case is excluded by the standing
hypothesis `I_S≠∅`.

## Bucket-Exclusion Corollary

**Statement.** For a coarse bucket `κ={p,p'}∈𝒦`, if there exists an index
`j_3` with `rad(a_{j_3})∩(S∪κ)=∅`, then the bare value `S∪κ` is never
realized as an exact radical at any index `>j_3`.

**Proof.** Direct application of the Permanent-Inadmissibility Lemma with
`C:=S∪κ`. ∎

## Independent verification (proof-reviewer, round 6, fresh code and hand
computation — own sequence simulation, not reused from the builder's script)

**Refutation check (the outline's literal single-witness criterion).**
Re-generated `a_1=247`'s first 7 terms exactly:
`247,260,266,273,285,312,342` with radicals
`{13,19},{2,5,13},{2,7,19},{3,7,13},{3,5,19},{2,3,13},{2,3,19}`. Confirmed
`a_3` (`rad={2,7,19}`) does **not** block `{2,13}` (shares `2`) or `{7,13}`
(shares `7`) — a single witness is genuinely insufficient, confirming the
outline's literal Step 2 is false as stated.

**Coarsening Lemma, `a_1=247`, `S={13}`.** `j_1=3` (`comp={2,7}`), `j_2=5`
(`comp={3,5}`), disjoint. `𝒦={2,3},{2,5},{3,7},{5,7}` (as bare values
`{2,3,13},{2,5,13},{3,7,13},{5,7,13}`). Independently confirmed: `{2,5,13}`
realized at `a_2=260`; `{3,7,13}` at `a_4=273`; `{2,3,13}` at `a_6=312`;
`{5,7,13}` **never** realized through `n=6000` (checked directly), and is
permanently blocked from index 7 onward since `rad(a_7)={2,3,19}` is
disjoint from `{5,7,13}` — confirmed exactly, matching the Bucket-Exclusion
Corollary.

**Non-freeze check, `a_1=2747`, `S={41}`.** Independently generated all 6000
terms and enumerated every `j` with `G_j∩\{41\}=∅` through `n=400`:
`comp(a_j)` is `{2,3,7}` at `j=3,54,103,154,254,305,355` and `{2,3,5,7}` at
`j=205` — **no two are disjoint** (all contain `{2,3,7}`), confirming the
Coarsening Lemma's hypothesis genuinely fails here. Independently
reconstructed the local antichain history for `S={41}`: collapses to
`{3,41}` at `n=13`, `{2,41}` at `n=14`, then grows a fan `{7,q,41}` for
`q∈{11,13,17,19,23,29,31,37}` before a single collapse at `n=163` to the
final 3-element antichain `{2,41},{3,41},{7,41}` — exactly matching the
source, including the exact value `a_163=11767=T_{\{7,41\}}` (independently
computed via smooth-number search: the least integer of the form
`7^a·41^b>2747` is `11767`).

All numerical claims reproduce exactly.

**Honest scope note (matches the source's own diagnosis).** This Lemma
gives a real, unconditional structural reduction whenever its hypothesis
holds, but does **not** by itself prove `(MRS_S)`: the Bucket-Exclusion
Corollary blocks only a bucket's *bare* value, not proper supersets within
it, and ruling those out requires a cross-bucket domination argument not
established in general. Do not cite this Lemma as equivalent to "the
channel freezes."

## Certification

Both the Coarsening Lemma and the Bucket-Exclusion Corollary independently
re-derived and re-verified (proof + numerics, two independent examples,
zero discrepancies) by the round-6 proof-reviewer. Certified
`solved`-quality; the honest scope note is retained as part of the
certification (not a defect, an accurate boundary of what is proved).
