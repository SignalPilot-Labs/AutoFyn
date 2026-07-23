# Theorem V / Theorem V-MRS (𝓥 finite ⟺ Hypothesis (MRS)) — merged certification

## Status

Certified `solved`-quality (sorry-free), **unconditional**. This is a pure
equivalence between two ways of stating the same open target — it does
**not** prove (MRS) itself, which remains open (see
`lemmas/lemma-MS-minimal-radical-stabilization-sufficiency.md`).

## Provenance (independently proved twice, round 5)

Both `persistent-backbone-monovariant.md` (as **Theorem V**) and
`imprint-automaton-periodicity.md` (as **Theorem V-MRS**) proved, this same
round, the identical statement below, via two structurally different but
both-correct routes. The proof-reviewer independently re-derived both
routes from scratch (round 5) and confirms they agree and are each valid.
Certifying as one shared lemma so future rounds cite a single canonical
statement instead of two parallel ones.

## Notation

`P_i:=rad(a_i)`. For `n≥1`, `M_n⊆{1,…,n}` is the set of `n`-minimal indices
(Lemma W3, `lemmas/lemma-W2-W3-patch-and-minimal-radical-reduction.md`):
`i∈M_n` iff `i≤n` and no `k∈{1,…,n}` has `P_k⊊P_i`. `𝓜_n:={P_i:i∈M_n}` (a
finite antichain of finite prime-sets). **Hypothesis (MRS)**: `∃N_0` with
`𝓜_n=𝓜_{N_0}` for all `n≥N_0`. `𝓥:=⋃_{n≥1}𝓜_n` (every radical value ever
realized as `n`-minimal, at any finite `n`).

## Statement

`𝓥` is finite **if and only if** (MRS) holds.

## Proof (Route 1 — persistent-backbone-monovariant's "Interval Lemma" route)

**No-Resurrection Lemma.** Fix a finite prime set `C`. If some `k≥1` has
`P_k⊊C`, then `C∉𝓜_m` for every `m≥k`. *Proof:* if `C∈𝓜_m` for `m≥k`, then
`C=P_i` for some `i∈M_m`, so no index in `{1,…,m}` has radical `⊊P_i=C`; but
`k≤m` and `P_k⊊C` — contradiction. ∎

**Interval Lemma.** For `v∈𝓥`, `A_v:={n≥1:v∈𝓜_n}` is a contiguous interval
`[n_v,∞)` or `[n_v,e_v)` (`n_v:=\min A_v`). *Proof:* let
`E_v:={n>n_v:v∉𝓜_n}`. If `E_v=∅`, done (case (i)). Else `e_v:=\min E_v`; the
realizing index `i` of `v` at `n_v` (`i≤n_v<e_v`) must fail `e_v`-minimality
(else `v∈𝓜_{e_v}`, contradicting `e_v∈E_v`), so some `k≤e_v` witnesses
`P_k⊊v`; by No-Resurrection, `v∉𝓜_c` for all `c≥e_v`. Minimality of `e_v`
gives `v∈𝓜_n` for all `n_v≤n<e_v`. So `A_v=[n_v,e_v)`. ∎

**(⇒)** If `𝓥` finite, for each `v∈𝓥` let `m_v:=n_v` (case (i)) or `e_v`
(case (ii)); `N_0:=\max_{v∈𝓥}m_v` is finite. For `n≥N_0` and any `v∈𝓥`,
membership `v∈𝓜_n` depends only on the case, not on `n` — so `𝓜_n=𝓜_{N_0}`
for all `n≥N_0`: (MRS) holds.

**(⇐)** If (MRS) holds with index `N_0`, `𝓥=⋃_{n=1}^{N_0}𝓜_n` (terms
`n>N_0` add nothing new), a finite union of finite sets (`|𝓜_n|≤n`), hence
finite. ∎

## Proof (Route 2 — imprint-automaton-periodicity's "permanent survivor"
route, independently re-derived, agrees)

Let `𝓖:={C=P_i \text{ (some }i≥1\text{)} : \text{no }j≥1\text{ has
}P_j⊊C}` (globally minimal values). **Lemma PS.** `C` is a *permanent
survivor* (`C∈𝓜_n` for all `n≥N`, some `N`) iff `C∈𝓖`. (⇐: no witness
anywhere means no witness in any `{1,…,n}`, so once realized `C` stays
`n`-minimal forever. ⇒: if `C∉𝓖`, a global witness `j` exists; taking
`n'≥\max(N,j)` gives a contradiction with `C`'s realizing index being
`n'`-minimal.) **Lemma NR** (No-Resurrection, same fact as above, derived
directly from the `n`-minimality definition): if `C∉𝓖`, witnessed by `j`,
then `C∉𝓜_n` for all `n≥j`.

**(⇒)** Same argument as Route 1.

**(⇐)** If `𝓥` finite: `𝓖⊆𝓥` (Lemma PS ⇐ gives each `C∈𝓖` enters `𝓜_i` at
its realizing index `i`), so `𝓖` is finite, `𝓖={C_1,…,C_r}` with
first-appearance indices `i_1,…,i_r`; `𝓥∖𝓖={D_1,…,D_s}` finite, each with a
Lemma-NR witness `j_{D_t}`. `N_0:=\max` of all these (finite) indices works:
for `n≥N_0`, every `C_u∈𝓜_n` (Lemma PS) and every `D_t∉𝓜_n` (Lemma NR), so
`𝓜_n=𝓖` for all `n≥N_0`. ∎

## Independent re-verification (proof-reviewer, round 5)

Re-derived both routes from scratch by hand, confirmed each internally
consistent and non-circular, and confirmed they prove the *same* statement
about the *same* object `𝓥` (both approaches use the identical definition
`𝓥:=⋃_{n≥1}𝓜_n`). The key subtlety independently checked: `𝓜_n` is a set of
**values**, and a single value can in principle be realized by multiple
distinct indices — verified that both proofs' domination arguments are
insensitive to this (the domination/`n`-minimality condition depends only on
the *value* `C`, not on which particular index realizes it, so "leaving
`𝓜_n`" always has a value-level witness, never an index-level artifact).

Also re-verified numerically (fresh Python, `sympy.primefactors`, exact
greedy simulation): `a_1=91` (Lemma NR/PS's exact target case — zero
collapse events, 3 permanent survivors `{2,7},{2,13},{7,13}`, all `∈𝓖`,
confirmed stable from `n=3` through `n=3000`); `a_1=247` (Case-II
stabilization confirmed).

## Certification

Certified `solved`-quality, unconditional. Supersedes citing
`persistent-backbone-monovariant`'s Theorem V or `imprint-automaton-
periodicity`'s Theorem V-MRS separately — future rounds should cite this
merged file. Does **not** prove (MRS); the open content is finiteness of `𝓥`
(equivalently, per `theorem-CD-core-decomposition-and-lemma-TC.md`,
finiteness of `𝓥_S` for each of the `≤2^k-2` remaining proper nonempty cores
`S⊊P_1`).

## Source

`results/imo-2026-06/approaches/persistent-backbone-monovariant.md` and
`results/imo-2026-06/approaches/imprint-automaton-periodicity.md` (both
round 5, independently).
