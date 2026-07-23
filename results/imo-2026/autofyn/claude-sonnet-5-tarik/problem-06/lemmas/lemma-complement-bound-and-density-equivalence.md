# Lemma CB (Complement Bound), Proposition CB-2 and Corollary CB-3 (Density-Equivalence)

**Source.** `results/imo-2026-06/approaches/intersecting-family-covering-
construction.md` Part 10.1–10.2 (round 11). Depends on: already-certified
Theorem CD (`lemmas/theorem-CD-core-decomposition-and-lemma-TC.md`).

## Lemma CB (Complement Bound) — statement

Let `k:=|P_1|`. Every index `n\ge1` has a well-defined core `S(n)\subseteq
P_1` (Theorem CD), taking at most `2^k-1` distinct values, and
`\{I_S:S\text{ a core}\}` partitions `\mathbb N` exactly. Let `\mathcal
T_\infty:=\{S:I_S\text{ infinite}\}`, `F:=\sum_{S:I_S\text{ finite}}
|I_S|` (a fixed finite integer, at most `2^k-1` finite terms). Then for
every `N\ge1`:
`N-F\ \le\ \sum_{S\in\mathcal T_\infty}|I_S\cap[1,N]|\ \le\ N.`

**Proof.** Partitioning `[1,N]` by core, `\sum_{S\text{ core}}|I_S\cap
[1,N]|=N`. Splitting by `\mathcal T_\infty` vs. its complement:
`\sum_{S\in\mathcal T_\infty}|I_S\cap[1,N]|=N-\sum_{S\notin\mathcal
T_\infty}|I_S\cap[1,N]|`, and `0\le\sum_{S\notin\mathcal T_\infty}
|I_S\cap[1,N]|\le F` (each finite-class term is capped by its own total
size). `\blacksquare`

**Honest scope note.** This is an identity on the *sum* of infinite-class
densities; it places no constraint on any individual `|I_S\cap[1,N]|`
(explicit counterexample-style illustration: squares vs. non-squares is a
bona fide two-class partition with one class of density `0`).

## Proposition CB-2 (Density-Equivalence) — statement

Standing hypothesis: `\mathcal T_\infty=\{S,S'\}` exactly (the *only* two
infinite-class cores). Enumerate `I_S=\{s_1<s_2<\cdots\}`; for `i=s_k\in
I_S`, `\rho(i):=k/i`; `J_i:=|I_{S'}\cap[1,i)|`. Then
`\liminf_{i\in I_S,i\to\infty}J_i/i=1-\limsup_{i\in I_S,i\to\infty}
\rho(i)`. Consequently `(PD_{S,S'})` (`\exists c>0,i_0` with `J_i/i\ge c`
for all `i\in I_S,i\ge i_0`) holds iff `\limsup_{i\in I_S}\rho(i)<1`.

**Proof.** For `i=s_k\in I_S`: `|I_S\cap[1,i]|=k`, `|I_{S'}\cap[1,i]|=
J_i` (as `i\notin I_{S'}`). Lemma CB at `N=i` (valid since `\mathcal
T_\infty=\{S,S'\}`): `i-F\le k+J_i\le i`. Set `e_i:=i-k-J_i\in[0,F]`.
Then `J_i/i=1-\rho(i)-e_i/i`, and `e_i/i\to0`. Since adding a
vanishing sequence to `\rho(i)` does not change its `\limsup`,
`\liminf_{i\in I_S}J_i/i=1-\limsup_{i\in I_S}\rho(i)`. `\blacksquare`

## Corollary CB-3 — statement

`\limsup_{i\in I_S}\rho(i)=\overline d(I_S):=\limsup_{N\to\infty}
|I_S\cap[1,N]|/N` (ordinary upper natural density).

**Proof.** For `N\ge s_1`, let `s_k\le N` be the largest element of `I_S`
below `N`; `|I_S\cap[1,N]|/N=k/N\le k/s_k=\rho(s_k)`, giving
`\overline d(I_S)\le\limsup_{i\in I_S}\rho(i)`. Conversely every `\rho(i)`
(`i\in I_S`) is a special case (`N=i`) of the defining sequence for
`\overline d(I_S)`, giving the reverse inequality. `\blacksquare`

**Consequence.** In the `|\mathcal T_\infty|=2` case, `(PD_{S,S'})\iff
\overline d(I_S)<1` — a one-class statement, with no reference to
`I_{S'}` beyond being `I_S`'s complement up to the fixed finite `F`.

## Verification

Independently re-derived all three statements from scratch by hand
(standard real-analysis limsup/liminf manipulations, no numerical check
needed for an exact identity of this kind — confirmed the algebra of the
`e_i/i\to0` squeeze and the `N`-vs-`i` maximal-predecessor argument in
Corollary CB-3 are both correct and complete, no missing case). Confirmed
the squares/non-squares counterexample to the "Complement Bound alone
suffices" naive inference is valid (squares have natural density `0`,
non-squares density `1`, both are literal partition classes).

## Scope / usage note

This is a genuine, complete reduction (in the special `|\mathcal T_\infty|
=2` case) of the two-sided density hypothesis `(PD_{S,S'})` to a one-sided
upper-density bound on `I_S` alone — but it is explicitly a *negative*
finding for the purpose the round-11 outline hoped for: no argument
currently in this workspace (Lemma CB itself, Lemma RD, or the Magnitude
Bound Corollary) supplies a bound on `\overline d(I_S)` away from `1`.
`(PD_{S,S'})` remains open; do not treat this reduction as closing it.
