# Certified lemmas — two-anchor witness scaffold (TAS) + joint-spread guardrail (JSC)

Certified round 5 (proof-reviewer). Source: `approaches/realizer-index-joint-double-count.md` §A/§B
and `approaches/redundant-constraint-antichain.md` §13.2. Both UNCONDITIONAL (do NOT assume the
Crux). Built only on certified L1 (Anchor), E3 (private witness), R1 (realization), L3
(Distance–prime), and the Pigeonhole principle. Notation: `𝓐_∞` = ⊆-minimal prime-supports;
`P = primes(a₁)`; `∏G` = squarefree radical; `p_max(G)=max G`; `u(G)` = smallest term with support
exactly `G`.

## TAS (Two-Anchor Witness Separation).
Assume `a₁` is **not a prime power** (i.e. `|P| ≥ 2`) and the magnitude bound fails, i.e.
`sup_{G∈𝓐_∞} p_max(G) = ∞` (equivalently `𝓐_∞` infinite). Then there exist two **fixed** distinct
primes `p*, p** ∈ P`, an infinite index set, and for each retained `k` a pair `G_k, H_k ∈ 𝓐_∞` with
`q_k := p_max(G_k) → ∞` such that

  `G_k ∩ H_k = {q_k}`,  `p* ∈ G_k ∖ H_k`,  `p** ∈ H_k ∖ G_k`,  `p*, p**, q_k` pairwise distinct.

Moreover, writing `t_k := u(G_k)`, `t'_k := u(H_k)`, both are **genuine, distinct terms** of the
sequence and `q_k ∣ (t_k − t'_k)`, so `|t_k − t'_k| ≥ q_k → ∞`. For all large `k` (where
`∏G_k ≥ q_k ≥ a₁`, `∏H_k ≥ q_k ≥ a₁`) one has `t_k = ∏G_k`, `t'_k = ∏H_k`.

*Proof.* Fix `G'_1,G'_2,… ∈ 𝓐_∞` with `p_max(G'_k) → ∞`. Each meets `P` (L1); `P` finite, so by
Pigeonhole a fixed `p* ∈ P` lies in infinitely many; restrict, relabel `G_k`, so `p* ∈ G_k` and
(subsequence of →∞) `q_k := p_max(G_k) → ∞`; discard the finitely many `k` with `q_k ≤ p*`, so
`q_k > p*` and `|G_k| ≥ 2`. Apply E3 to `(G_k, q_k)`: a private witness `H_k ∈ 𝓐_∞` with
`G_k ∩ H_k = {q_k}`. Then `p* ∉ H_k` (else `p* ∈ G_k∩H_k={q_k}`, forcing `p*=q_k`, false). By L1
`H_k ∩ P ≠ ∅`; since `p* ∉ H_k` the witness carries a prime of `P∖{p*}` (**here `|P|≥2` is used**);
Pigeonhole over the finite set `P∖{p*}` fixes `p** ∈ P∖{p*}` in infinitely many `H_k`; restrict,
relabel; discard `k` with `q_k ≤ p**`. Then `p** ∈ H_k∖G_k` (if `p** ∈ G_k` then
`p** ∈ G_k∩H_k={q_k}`, contradicting `p**≠q_k`), and `p*,p**,q_k` are pairwise distinct. By R1,
`t_k=u(G_k)`, `t'_k=u(H_k)` are terms; distinct since `G_k≠H_k`. `F(t_k)∩F(t'_k)=G_k∩H_k={q_k}` so
`q_k ∣ t_k`, `q_k ∣ t'_k`, and L3 gives `q_k ∣ (t_k−t'_k)`, `t_k≠t'_k`, hence `|t_k−t'_k| ≥ q_k`. For
large `k`, `∏G_k ≥ q_k ≥ a₁` so R1 gives `u(G_k)=∏G_k`, likewise `u(H_k)=∏H_k`. ∎

Remark (prime-power case). If `|P|=1`, say `P={p*}`, then every support meets `{p*}`, so `p*∈G` for
all `G∈𝓐_∞`; `{p*}` is realizable as a term ((p*)^k≥a₁) hence `{p*}∈𝓐_∞`, forcing `𝓐_∞={{p*}}`
finite — the Crux holds outright (prime-power lock). So TAS's `|P|≥2` hypothesis loses no generality.

## JSC (Joint-Spread Collapse — NEGATIVE guardrail).
Under TAS, for all large `k`,

  `t_k − t'_k = q_k·(A_k − B_k)`,  `A_k := ∏(G_k∖{q_k})`,  `B_k := ∏(H_k∖{q_k})`,  with `A_k ≠ B_k`.

Consequently `|t_k − t'_k|` is a **nonzero multiple of `q_k`**, and **any** `a₁`-only upper bound
"`|t_k − t'_k| ≤ C(a₁)` for infinitely many `k`" **entails** "`q_k ≤ C(a₁)` for infinitely many `k`"
= the magnitude bound. Hence the realizer-pair spread `|t_k−t'_k|` is **not an independent lever**:
bounding it from above by an `a₁`-only constant is logically at least as strong as the Crux itself.

*Proof.* `t_k=∏G_k=q_k·A_k`, `t'_k=∏H_k=q_k·B_k`. The prime sets `G_k∖{q_k}` and `H_k∖{q_k}` are
disjoint (`G_k∩H_k={q_k}`), so `A_k,B_k` are products over disjoint prime sets; `p*∣A_k` (as
`p*∈G_k∖{q_k}`) while `p*∤B_k` (as `p*∉H_k`), so `A_k≠B_k`, `|A_k−B_k|≥1`. Thus
`|t_k−t'_k|=q_k|A_k−B_k|≥q_k`, and `|t_k−t'_k|≤C(a₁)` ⟹ `q_k≤C(a₁)`. ∎

**Scope of the guardrail (what is and is NOT certified).** The *identity* above and the implication
"spread bound ⟹ magnitude bound" are certified theorems. The broader slogan that *every* concrete
window/double-count route to a spread bound "forks to the R4-forbidden sub-support-realization move"
is NOT a formal theorem (no formal definition of "every route"); it is recorded only as a heuristic
observation, companion to the R4 Collapse guardrail (`anchor-partition.md`). JSC certifies the
concrete negative: the joint-spread of the two-anchor witness pair carries no leverage beyond the
magnitude bound. It does NOT close E5″.
