# Lemma CB (Core Blocking)

**Source.** `results/imo-2026-06/approaches/sunflower-bundle-closure.md` §8.2
(round 11). Depends on: already-certified Lemma NIDF
(`lemmas/lemma-XC-NIDF-FT-cross-companion-transversal.md`, part (a)) and
Lemma ERD-C (`lemmas/lemma-ERD-realized-blocked-dichotomy.md`).

## Statement

Let `S,S'` be disjoint nonempty cores (`S,S'\subseteq P_1`) with
`I_S,I_{S'}` both nonempty (in particular, for either side of any
doubly-infinite disjoint core pair in the sense of `theorem-SW-
stabilization-sufficiency.md`). Then, in the sense of Lemma ERD-C's
dichotomy: **`S` is blocked (never realized as some index's exact
radical), and symmetrically `S'` is blocked.**

## Proof

Suppose toward a contradiction that `S` is realized: some index `n_0\ge1`
has `P_{n_0}=S` exactly (`P_i:=\mathrm{rad}(a_i)`). Since `S\subseteq P_1`,
`P_{n_0}\cap P_1=S\cap P_1=S`, so `n_0\in I_S`. By Lemma NIDF part (a)
(hypotheses: `S,S'` disjoint nonempty cores with `I_S,I_{S'}\ne\varnothing`
— satisfied here), `\mathrm{comp}(a_i)\ne\varnothing` for every `i\in I_S`,
in particular for `i=n_0`. But `\mathrm{comp}(a_{n_0})=P_{n_0}\setminus
P_1=S\setminus P_1=\varnothing` (since `S\subseteq P_1`). This gives
`\varnothing\ne\varnothing`, a contradiction. Hence `S` is not realized;
by Lemma ERD-C's exhaustive dichotomy (applied to `C:=S`, which needs no
hypothesis beyond `S` being a nonempty finite set of primes), `S` is
blocked. The `S'` case is symmetric (exchange `S,S'` throughout; Lemma
NIDF(a)'s hypotheses and conclusion are stated symmetrically in `S,S'`).
`\blacksquare`

## Verification

Independently re-derived and re-checked numerically by the round-11
proof-reviewer on both mandatory instances (own generator, `sympy`
factorization): `a_1=247`, `(S,S')=(\{13\},\{19\})`, and
`a_1=21528751`, `(S,S')=(\{103\},\{197\})` — in both cases neither `S`
nor `S'` is ever realized as an exact radical among the generated terms,
and `\mathrm{comp}(a_i)` is nonempty for every `i` in the respective
index class, exactly as the proof predicts (no counterexample sought or
found; the proof itself is unconditional and does not depend on these
specific instances).

## Scope / usage note

This lemma removes a case split for any future construction on a
doubly-infinite disjoint core pair `(S,S')`: the "realized" branch of
Lemma ERD-C applied to either bare core `S` or `S'` **never occurs**, so
the "blocked" branch (and hence the Escape-Confinement Lemma's
single-witness mechanism) is unconditionally available on both sides.
It does **not** by itself resolve Conjecture (JW) or the Stabilization
Conjecture — see `sunflower-bundle-closure.md` §8.3–8.4 for the honestly
reported remaining gap (Cross-Permanent-Inadmissibility) that persists
even after this simplification.
