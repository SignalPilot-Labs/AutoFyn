# Approach: realizer-index-joint-double-count

Target: the FULL theorem (IMO 2026 P6). Via the certified chain the theorem reduces to the
**magnitude bound** — the primes occurring in ⊆-minimal supports `𝓐_∞` are bounded by an
`a₁`-only constant (≡ Crux / Finite Alphabet ≡ E4 cardinality bound). Once the magnitude bound
holds, `𝓐_∞` is finite (certified Reduction, `enumeration-and-transversal.md`) and §4–§5 of
`redundant-constraint-antichain` give `a_{n+T}=a_n+L` for all `n≥1` with `T=|ρ(A)|`, `L=∏Π`.

This slug attacks the magnitude bound directly by a contradiction on the JOINT system of first
realizers of minimal supports, using a **two-anchor witness scaffold** and then attempting an
`a₁`-only upper bound on the realizer-pair spread (Lemma J).

## Status
partial

## Approaches tried
- **Round 5 — two-anchor witness scaffold (NEW, proved rigorously) + Lemma J negative result.**
  Steps 1–4 of the skeleton (anchor collapse, two-anchor separation of the private-witness pair,
  realizer pair with `q_k∣(t_k−t'_k)`) are fully proved from certified E3 / R1 / R2 / Anchor L1 /
  Distance–prime L3 — see **Current best §A**. This is genuinely new reusable structure and is
  proposed for certification (Promotable lemma **TAS**). The closing gap **Lemma J** (an `a₁`-only
  upper bound on the spread `|t_k−t'_k|`) is shown to be **ILLUSORY as an independent lever**: by
  unique factorization `t_k−t'_k = q_k·(A_k−B_k)` with `A_k≠B_k` a forced nonzero integer, so any
  `a₁`-only spread bound *is* the magnitude bound `q_k≤C(a₁)` (proved in **Current best §B**). The
  joint/relational "bound the difference not the endpoints" leverage does not exist; concrete
  window routes to it fork into the R4-forbidden sub-support-realization lever. Recorded as a
  certified NEGATIVE result. Status of the slug's closing move: RETHINK-finding (the last un-forked
  opening is, on inspection, forked/circular). Scaffold survives as certifiable shared structure.

## Current best

Certified infrastructure used (all UNCONDITIONAL, do not assume the Crux):
`free-lemmas.md` (L1 Anchor, L3 Distance–prime), `enumeration-and-transversal.md`
(E1, E2(⇒), E3, Reduction), `realizer-value-pincer.md` (R1, R2), `size-bound-reduction.md` (E4).

Notation. `F(x)=primes(x)`; `𝓕={F(a_n):n≥1}`; `𝓐_∞` = the ⊆-minimal elements of `𝓕`;
`A={c≥1 : F(c) meets every G∈𝓐_∞}`; `P=primes(a₁)` (finite); `∏G=∏_{p∈G}p` (squarefree radical);
`u(G)` = smallest term of the sequence whose support is `G`; `p_max(G)=max G`.

### §A. Two-anchor witness scaffold — PROVED (steps 1–4)

**Contradiction hypothesis (H).** The magnitude bound fails: the set of primes occurring in
⊆-minimal supports is unbounded, i.e.
`sup_{G∈𝓐_∞} p_max(G) = ∞`. Equivalently (certified Reduction), `𝓐_∞` is infinite.

Fix an infinite sequence `G'_1,G'_2,…∈𝓐_∞` with `p_max(G'_k)→∞`.

**Step 1 (well-posed).** Each `G'_k∈𝓐_∞` is the support `F(a_i)` of some term `a_i`
(definition of `𝓐_∞ ⊆ 𝓕`). By **Anchor L1** the term `a_i` has a prime factor in `P`, so
`G'_k∩P ≠ ∅`. Define `α(G'_k) := min(G'_k∩P) ∈ P` (well-defined; `P` finite totally ordered).

**Step 2 (anchor collapse — fix `p*`).** `P` is finite, the index set infinite, so by
Pigeonhole some value `p*∈P` satisfies `α(G'_k)=p*` for infinitely many `k`. Restrict to that
subsequence and relabel it `G_1,G_2,…`; thus `p*∈G_k` for all `k`. A subsequence of a sequence
tending to `∞` still tends to `∞`, so `p_max(G_k)→∞`; write `q_k:=p_max(G_k)`. Discard the
finitely many indices with `q_k≤p*` (allowed since `q_k→∞`); for the retained indices
`q_k>p*≥2`. In particular `p*≠q_k` and both `p*,q_k∈G_k`, so `|G_k|≥2` and `q_k=p_max(G_k)`.
(This also disposes of the `|G|=1` worry: an anchored support with unbounded max prime cannot be
a single prime.)

**Step 3 (two-anchor separation — fix a second anchor `p**`).** Apply certified **E3** to the
pair `(G_k, q_k)` with `q_k∈G_k`: there is a private witness `H_k := G_{q_k} ∈ 𝓐_∞` with
`G_k∩H_k = {q_k}`.

- *`p*∉H_k`.* We have `p*∈G_k` and `p*≠q_k` (Step 2). If `p*∈H_k` then `p*∈G_k∩H_k={q_k}`,
  forcing `p*=q_k` — contradiction. Hence `p*∉H_k`.
- *A second anchor exists in `H_k`.* `H_k∈𝓐_∞` is the support of a term, so by **Anchor L1**
  `H_k∩P≠∅`; pick `p'_k∈H_k∩P`. Since `p*∉H_k` we have `p'_k≠p*`, i.e. `p'_k∈P∖{p*}`.
- *Fix it by Pigeonhole.* `P∖{p*}` is finite and the retained index set infinite, so some
  `p**∈P∖{p*}` satisfies `p**∈H_k` for infinitely many `k`. Restrict to that subsequence and
  relabel. Discard the finitely many indices with `q_k≤p**` (allowed, `q_k→∞`), so `p**≠q_k`.

*Net separation.* For every retained `k`, the three primes `p*, p**, q_k` are pairwise distinct
(`p*≠p**` since `p**∈P∖{p*}`; `q_k>p*` and `q_k>p**`), and

- `p* ∈ G_k∖H_k` (`p*∈G_k`, `p*∉H_k`);
- `p** ∈ H_k∖G_k` (`p**∈H_k`; if `p**∈G_k` then `p**∈G_k∩H_k={q_k}`, contradicting `p**≠q_k`);
- `q_k ∈ G_k∩H_k`, the **unique** common prime.

Both anchors `p*,p**` are FIXED elements of the finite set `P`, independent of `k`.

**Step 4 (realizer pair).** Set `t_k := u(G_k)` and `t'_k := u(H_k)`. By certified **R1**, since
`G_k,H_k∈𝓐_∞`, both `t_k` and `t'_k` are genuine terms of the sequence, with `F(t_k)=G_k`,
`F(t'_k)=H_k`. They are distinct terms because `G_k≠H_k` (e.g. `p*∈G_k∖H_k`). Now
`F(t_k)∩F(t'_k)=G_k∩H_k={q_k}`, so `gcd(t_k,t'_k)=q_k^{m}` for some `m≥1`; in particular
`q_k∣t_k` and `q_k∣t'_k`. By **Distance–prime L3** (a shared prime divides the difference of two
distinct terms),
`q_k ∣ (t_k−t'_k)` and `t_k≠t'_k`, hence

  `|t_k − t'_k| ≥ q_k → ∞.`  (★)

Steps 1–4 are complete and rigorous. This is the new structural content of the slug and is
proposed for certification below (**TAS**).

To close the proof one would need an `a₁`-only UPPER bound contradicting (★):

> **Lemma J (target).** `|t_k − t'_k| ≤ C(a₁)` for infinitely many `k`.

With Lemma J, (★) gives `q_k ≤ C(a₁)` on an infinite set, contradicting `q_k→∞`; the magnitude
bound follows, `𝓐_∞` is finite, and §4–§5 finish the theorem. **Lemma J is NOT proved.** §B shows
why the pitched "relational joint-spread" route to it cannot work.

### §B. Lemma J is illusory — certified NEGATIVE result (the closing lever is forked/circular)

**Claim (Joint-Spread Collapse).** Under the scaffold of §A, any `a₁`-only upper bound on the
realizer-pair spread is logically *at least as strong as* the magnitude bound it was meant to
reduce to. Precisely: for all large `k`,

  `t_k − t'_k = q_k·(A_k − B_k)` with `A_k − B_k` a **nonzero integer**,  (†)

so `|t_k−t'_k| ≥ q_k`, and consequently *any* statement "`|t_k−t'_k|≤C(a₁)` for infinitely many
`k`" (Lemma J) *entails* "`q_k≤C(a₁)` for infinitely many `k`" = the magnitude bound. Hence
Lemma J supplies no decoupling and is not an independent lever.

*Proof of (†).* Since `q_k∈G_k` and `q_k→∞`, we have `∏G_k ≥ q_k ≥ a₁` for all large `k`; by
certified **R1**, `u(G_k)=∏G_k`, so `t_k=∏G_k` is squarefree. Likewise `q_k∈H_k` gives
`∏H_k≥q_k≥a₁`, so `t'_k=∏H_k` is squarefree. Write

  `A_k := ∏(G_k∖{q_k})`,  `B_k := ∏(H_k∖{q_k})`,

so `t_k = q_k·A_k` and `t'_k = q_k·B_k`, whence `t_k−t'_k = q_k·(A_k−B_k)`. The two prime sets
underlying `A_k` and `B_k` are DISJOINT:

  `(G_k∖{q_k}) ∩ (H_k∖{q_k}) ⊆ (G_k∩H_k)∖{q_k} = {q_k}∖{q_k} = ∅`,

using `G_k∩H_k={q_k}` from Step 3. By the two-anchor separation, `p*∈G_k∖{q_k}` so `p*∣A_k`,
while `p*∉H_k` so `p*∤B_k`. Hence `A_k≠B_k`, i.e. `A_k−B_k≠0` and `|A_k−B_k|≥1`. This proves
(†); in particular `|t_k−t'_k|=q_k·|A_k−B_k|≥q_k`, recovering (★). ∎

*Consequence.* Suppose Lemma J held with an `a₁`-only constant `C(a₁)`: `|t_k−t'_k|≤C(a₁)` for
infinitely many `k`. By (†), `q_k ≤ q_k·|A_k−B_k| = |t_k−t'_k| ≤ C(a₁)` for those `k`. That is
exactly the magnitude bound on `q_k`. So proving Lemma J requires *already* proving the target;
there is no "bound the difference while the endpoints run away" — the shared-prime congruence
`t_k≡t'_k (mod q_k)` forces the spread to be a *multiple* of `q_k`, and a nonzero multiple of a
large number is large. The advertised relational leverage is illusory. ∎

**Fork check (why no concrete route rescues J).** The certified chain
(`enumeration-and-transversal.md` Reduction, `size-bound-reduction.md` E4) makes the magnitude
bound EQUIVALENT to the Crux and to `sup|G|<∞`. By §B, Lemma J ⟹ magnitude bound, so Lemma J is
equivalent to the Crux; its only concrete proof routes must bound `∏G_k` (equivalently a first
realizer `u(G_k)`), which is precisely the circular/forbidden zone flagged in memory rule 11 and
the R4 Collapse theorem (`anchor-partition.md` guardrail): any route that argues "in the index
window `[i(H_k), i(G_k)]` the greedy rule rejected a smaller `G_k`- or `H_k`-sub-support" realizes
a proper sub-support and collapses verbatim to the R4-forbidden sub-support-realization lever. The
static two-anchor resource `ℤ/(p*p**)` bounds nothing: it is a fixed finite object with no
identified mechanism to constrain the unbounded quantity `q_k·(A_k−B_k)`. This confirms the
outline-reviewer's finding: **the last un-forked opening is, on inspection, forked/circular.**

### Net position

- **Proved this round (new, certifiable):** the two-anchor witness scaffold §A — a private witness
  of the large prime `q_k` excludes `G_k`'s small anchor `p*` yet must meet `P`, forcing a fixed
  second anchor `p**`; the realizer pair then satisfies `|t_k−t'_k|≥q_k→∞`.
- **Open gap:** Lemma J (the `a₁`-only spread bound), and §B proves it is not an independent lever
  (it equals the magnitude bound; window routes fork to the R4-forbidden lemma). The slug therefore
  does NOT close the magnitude bound.
- **No overclaim on E5″:** nothing here advances the companion-radical form; the leader
  `redundant-constraint-antichain` remains the certified furthest-forward.

## Promotable lemmas

**TAS (Two-Anchor Witness Separation) — proposed for certification.** *Assume the magnitude bound
fails, i.e. `sup_{G∈𝓐_∞}p_max(G)=∞`. Then there exist a fixed pair of distinct primes
`p*,p**∈P=primes(a₁)`, an infinite index set, and for each index a pair `G_k,H_k∈𝓐_∞` with
`q_k:=p_max(G_k)→∞`, such that `G_k∩H_k={q_k}`, `p*∈G_k∖H_k`, `p**∈H_k∖G_k`; and, writing
`t_k=u(G_k)`, `t'_k=u(H_k)`, both are distinct terms of the sequence with `q_k∣(t_k−t'_k)`, hence
`|t_k−t'_k|≥q_k→∞`. Moreover `t_k=∏G_k`, `t'_k=∏H_k` for all large `k`, so
`t_k−t'_k=q_k(A_k−B_k)` with `A_k=∏(G_k∖{q_k})`, `B_k=∏(H_k∖{q_k})` products over disjoint prime
sets and `A_k≠B_k`.* Proof: §A + §B above, from certified Anchor L1, E3, R1, Distance–prime L3
and Pigeonhole. UNCONDITIONAL (does not assume the Crux).

**JSC (Joint-Spread Collapse — NEGATIVE result) — proposed for certification.** *Under TAS, any
`a₁`-only upper bound "`|t_k−t'_k|≤C(a₁)` for infinitely many `k`" (Lemma J) entails
"`q_k≤C(a₁)` for infinitely many `k`", i.e. the magnitude bound. Hence the realizer-pair spread is
not an independent lever: bounding it is equivalent to (at least as hard as) the Crux, and every
concrete window route to it collapses to the R4-forbidden sub-support-realization lemma.* Proof:
§B identity `t_k−t'_k=q_k(A_k−B_k)` with `A_k−B_k≠0`. This certifies the outliner's contingency
clause: the joint-spread opening is forked/circular.
