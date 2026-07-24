# Theorem SW (Stabilization Sufficiency): FCBC reduces to doubly-infinite
disjoint-core-pair witnesses

**Source.** `results/imo-2026-06/approaches/intersecting-family-covering-
construction.md` (round 9, Part 8). Depends on: the already-certified
Theorem CD (`lemmas/theorem-CD-core-decomposition-and-lemma-TC.md`, core
decomposition, `≤2^k-1` nonempty cores), Lemma P′
(`lemmas/lemma-P-prime-pairwise-intersecting.md`), and the already-certified
Finite-Class Direct Covering lemma
(`lemmas/finite-imprint-class-direct-covering.md`).

## Statement

Write `k:=|P_1|`. Every index `i` has a well-defined nonempty core
`S(i):=rad(a_i)∩P_1⊆P_1` (Theorem CD); `I_S:=\{i:S(i)=S\}` partitions `ℕ`.
For an unordered pair of nonempty `S,S'⊆P_1` (possibly `S=S'`), call it
*disjoint* if `S∩S'=∅`, and (when disjoint) *doubly-infinite* if both
`I_S,I_{S'}` are infinite.

**Stabilization Conjecture** (open, this file's residual target): for every
doubly-infinite disjoint pair `\{S,S'\}` (at most `\binom{2^k-1}{2}` such
pairs, fixed once `a_1` is fixed), there is a **finite** `W_{S,S'}` with
`rad(a_i)∩rad(a_j)∩W_{S,S'}≠∅` for every `i∈I_S,j∈I_{S'}`.

**Theorem SW.** If the Stabilization Conjecture holds for every
doubly-infinite disjoint core pair, then FCBC holds — explicitly,
`H:=P_1∪⋃_{S:|I_S|<∞}H_S∪⋃_{\{S,S'\}\text{ doubly-infinite}}W_{S,S'}`
(finite, at most `(2^k-1)+\binom{2^k-1}{2}` further finite sets beyond
`P_1`) satisfies `H∩rad(a_i)∩rad(a_j)≠∅` for every `1≤i<j`. Consequently,
via the already-certified Theorem 5.1, `a_{n+T}=a_n+L` for every `n≥1`.

**Lemma SW1** (intersecting cores are automatic). If `S(i)∩S(j)≠∅`, then
`P_1∩rad(a_i)∩rad(a_j)⊇S(i)∩S(j)≠∅` (since `S(i)⊆rad(a_i)∩P_1`, likewise
`S(j)`).

**Lemma SW3** (Peeling, generalizes Finite-Class Direct Covering). For any
disjoint core pair `(S,S')` and any **finite** `F⊆I_S` (not requiring `I_S`
finite), `H_F:=⋃_{i∈F}rad(a_i)` is finite and
`H_F∩rad(a_i)∩rad(a_j)≠∅` for every `i∈F`, `j≠i` (in particular every
`j∈I_{S'}`).

## Proof

**Lemma SW1.** Immediate from `S(i)⊆rad(a_i)∩P_1`, `S(j)⊆rad(a_j)∩P_1`: any
element of `S(i)∩S(j)` lies in `P_1∩rad(a_i)∩rad(a_j)`.

**Lemma SW3.** Identical to the certified Finite-Class Direct Covering
lemma's proof with `F` in place of `I_S`: `H_F` is a finite union of finite
sets (finite by hypothesis on `F`, not on `I_S`), and for `i∈F,j≠i`,
`rad(a_i)⊆H_F` together with Lemma P′ (`rad(a_i)∩rad(a_j)≠∅`) gives the
result — finiteness of `I_S` was never used beyond making the union finite,
which a finite `F` gives equally well.

**Theorem SW.** `H` is a union of `P_1` and at most `(2^k-1)+\binom{2^k-
1}{2}` further finite sets (Theorem CD bounds the number of cores by
`2^k-1`, hence the number of finite-`I_S` sets `H_S` by the same bound, and
the number of unordered core pairs by `\binom{2^k-1}{2}`), hence finite.
Fix `1≤i<j`, `S:=S(i)`, `S':=S(j)` (both nonempty by Theorem CD). Exactly
one of:
- **`S∩S'≠∅`** (includes `S=S'`, since cores are always nonempty): Lemma
  SW1 gives `P_1∩rad(a_i)∩rad(a_j)≠∅`, and `P_1⊆H`.
- **`S∩S'=∅`, one of `I_S,I_{S'}` finite** (say `I_S`, the other case is
  symmetric): the certified Finite-Class Direct Covering lemma (applied
  with this `S`, `i∈I_S`, `j≠i`) gives `H_S∩rad(a_i)∩rad(a_j)≠∅`, and
  `H_S⊆H`.
- **`S∩S'=∅`, both `I_S,I_{S'}` infinite** (doubly-infinite disjoint pair):
  the Stabilization Conjecture's hypothesis gives
  `W_{S,S'}∩rad(a_i)∩rad(a_j)≠∅`, and `W_{S,S'}⊆H`.

These three cases are exhaustive (first split on `S∩S'≠∅` vs `=∅`; if
`=∅`, split on finiteness of `I_S,I_{S'}`, a well-defined dichotomy for
each fixed core) and each gives `H∩rad(a_i)∩rad(a_j)≠∅`. So `H` satisfies
`(†')`/FCBC; Theorem 5.1 finishes. `∎`

## Independent re-verification (proof-reviewer, round 9)

- Re-derived the 3-case split by hand: confirmed it is exhaustive and
  non-overlapping in application (case chosen by `S∩S'` then finiteness),
  and confirmed the special case `S=P_1` (or `S'=P_1`) always falls in
  Case 1 automatically (`P_1∩S'=S'≠∅` for any nonempty `S'`), so the "top
  core is free" fact (Lemma TC) is correctly subsumed without special
  casing.
- Checked the imported Finite-Class Direct Covering lemma's statement
  applies to *any* nonempty `S` (not just proper cores) — confirmed from
  its own certified file, no hidden restriction.
- Independently reproduced the numerical Stabilization-Conjecture evidence
  with a fresh, from-scratch generator (own minimal-radical-antichain
  implementation, validated against brute force on `a_1∈\{15,247,2747\}`
  before trusting it at scale): for `a_1=247`, `(S,S')=(\{13\},\{19\})`,
  `N=8000`, found `|I_{13}|=4305,|I_{19}|=2764`, and confirmed
  `W=\{2,3,5,7\}` covers all `11{,}899{,}020` cross pairs with **zero**
  failures — consistent with (a subset of) the builder's own larger
  `N=60000`/`669`M-pair check. Also independently reproduced the
  `a_1=21528751` bridge-prime-`97` finding (§ below, shared with sibling
  `explicit-window-backbone-construction`): `a_{596}` has radical
  `\{2,3,5,7,97,1061\}` (core `\{1061\}`), `a_{863}` has radical
  `\{11,97,103,197\}` (core `\{103,197\}`), `\gcd(a_{596},a_{863})=97`
  exactly — matches both sibling files' independent claims exactly.
- Found no gap in Theorem SW's proof or the case split; the Stabilization
  Conjecture itself is correctly and honestly left open.

## Certification

Certified `solved`-quality (sorry-free) for Theorem SW, Lemma SW1, Lemma
SW3 as stated (the Stabilization Conjecture itself is NOT certified — it
remains an open hypothesis, numerically well-supported but unproved).
Reusable: any future approach that proves the Stabilization Conjecture for
even one `a_1`'s finite list of doubly-infinite disjoint core pairs
finishes that instance's whole problem via this theorem plus Theorem 5.1.
