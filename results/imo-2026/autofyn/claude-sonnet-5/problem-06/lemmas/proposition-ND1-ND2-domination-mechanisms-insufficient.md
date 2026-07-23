# Propositions ND1 and ND2 (Domination-Lemma-based FCBC mechanisms are insufficient)

Two negative results, proved by explicit hand computation on already-certified
traces, ruling out the two most natural ways to try to turn the (conditional)
Key Lemma (ω-bound) into an actual Finite Covering Backbone Conjecture (FCBC)
covering set.

## Proposition ND1

**Statement.** On the certified `a_1=221` trace
(`a_1,…,a_5 = 221,234,238,255,260`), let `Q` be the set built from the
Domination Lemma's *unique per-step maximizer* at each of the first three
steps (together with `rad(a_1)`). Then `H := Q ∪ rad(a_1)` does **not**
satisfy the FCBC covering property: the pair `(i,j)=(2,4)` has
`rad(a_2)∩rad(a_4) = {3}` (its unique common prime), but `3 ∉ H`.

**Proof (verified independently by the reviewer, exact match).**
`rad(a_1)={13,17}`, `rad(a_2)={2,3,13}`, `rad(a_3)={2,7,17}`,
`rad(a_4)={3,5,17}`, `rad(a_5)={2,5,13}`.
- `n=1`: `D_1(2)=0, D_1(3)=0, D_1(13)=1`. Unique maximizer `q*(2)=13`.
- `n=2`: `D_2(2)=1, D_2(7)=0, D_2(17)=1`. Tie between `2` and `17`.
- `n=3`: `D_3(3)=1, D_3(5)=0, D_3(17)=2`. Unique maximizer `q*(4)=17`.

So `Q ⊆ {2,13,17}` regardless of the `n=2` tie-break, and
`H = Q∪{13,17} ⊆ {2,13,17}`; in particular `3∉H`. But
`rad(a_2)∩rad(a_4) = {2,3,13}∩{3,5,17} = {3}`, so `H∩rad(a_2)∩rad(a_4)=∅`.
`∎`

## Proposition ND2

**Statement.** On the certified `a_1=375` trace
(`a_1,…,a_7 = 375,378,380,384,390,396,399`), let `Q' := {q : ∃n≥1, q∣a_{n+1},
D_n(q)·ω(a_{n+1}) ≥ n}` (every prime meeting the Domination Lemma's averaged
threshold at the step where it is tested, not just the unique per-step
maximizer). Then `H' := Q'∪rad(a_1)` (restricted to data available through
`n=7`) does **not** cover the pair `(3,7)`: `rad(a_3)∩rad(a_7)={19}`
(unique common prime), but `19∉H'` through `n=7`.

**Proof (verified independently by the reviewer, exact match).**
`rad(a_3)=rad(380)={2,5,19}`, `rad(a_7)=rad(399)={3,7,19}`, intersection
`{19}`. The only two steps testing `19` (i.e. where `19` first divides a
newly-admitted term) are `n=2` (testing `a_3=380`) and `n=6` (testing
`a_7=399`).
- `n=2`: `D_2(19)=0` (neither `375` nor `378` is divisible by `19`);
  threshold `2/ω(a_3)=2/3`; `0<2/3`, fails.
- `n=6`: previous terms `375,378,380,384,390,396`; only `380` is divisible by
  `19`, so `D_6(19)=1`; `ω(a_7)=ω(399)=3`; threshold `6/3=2`; `1<2`, fails.

So `19∉Q'` (restricted to data through `n=7`), and since `rad(a_1)={3,5}`
also excludes `19`, `H'` fails to cover `(3,7)`. `∎`

**Combined consequence.** Neither the literal per-step Domination-Lemma
maximizer nor its natural broadening to "meets the averaged threshold" gives
a valid FCBC covering set, even conditional on the (still-open) hypothesis
`ω(a_n)=O(1)`. Any future FCBC mechanism must not rely on either construction
as stated.

**Source.** `results/imo-2026-06/approaches/persistent-backbone-monovariant.md`
(round 3), Propositions ND1, ND2.

**Certification.** Independently re-verified by the reviewer via direct
Python computation (exact integer factorization) reproducing every `D_n(q)`
value and radical claimed; exact match in all cases. No gaps. Certified
`solved`-quality (sorry-free), unconditional negative results (they do not
depend on the open `ω(a_n)=O(1)` hypothesis holding — they show the
mechanisms fail even where they are best-defined).
