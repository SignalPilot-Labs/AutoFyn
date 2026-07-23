# Freeze-Confinement Domination Lemma and the `S^+` Necessity + Finiteness Lemma

**Source.** `results/imo-2026-06/approaches/forced-primes-well-ordering.md`
(round 8, §H, Steps 1 and 4). Depends on the already-certified
`lemma-C-generalized-subsequence.md` (Generalized Lemma C) and the local
antichain machinery of §A/§B of the same file (Local Corollary W3′-style
minimality argument).

## Freeze-Confinement Domination Lemma

**Setup.** Fix a proper core `S⊊P_1` with `I_S` infinite.
`M_n^S:={i∈I_S∩[1,n] : no k∈I_S∩[1,n] has rad(a_k)⊊rad(a_i)}`,
`𝓜_n^S:={rad(a_i):i∈M_n^S}`. Hypothesis `(MRS_S)`: `∃n^*` with
`𝓜_n^S=𝓜_{n^*}^S` for all `n≥n^*`.

**Statement.** If `(MRS_S)` holds with freeze index `n^*`, then for
**every** `i∈I_S` (not merely indices past `n^*`), there exists
`C'∈𝓜_{n^*}^S` with `rad(a_i)⊇C'`.

**Proof.** Fix `i∈I_S`. Let `n:=max(i,n^*)≥n^*`, so by `(MRS_S)`,
`𝓜_n^S=𝓜_{n^*}^S`. Let `T:={k∈I_S∩[1,n]:rad(a_k)⊆rad(a_i)}`; `i∈T`
(`i≤n`, trivial reflexivity), so `T` is finite and nonempty. Choose
`j^*∈T` minimizing `|rad(a_{j^*})|`. If `j^*∉M_n^S`, some `k∈I_S∩[1,n]`
has `rad(a_k)⊊rad(a_{j^*})⊆rad(a_i)`; then `k∈T` with strictly smaller
radical size, contradicting minimality of `j^*`. So `j^*∈M_n^S`, giving
`rad(a_{j^*})∈𝓜_n^S=𝓜_{n^*}^S`; set `C':=rad(a_{j^*})⊆rad(a_i)`. `∎`

## `S^+` Necessity + Finiteness Lemma

**Definition.** `S^+:=⋂_{i∈I_S}rad(a_i)`.

**Statement.** (a) Every exactly-realized bare value `C=rad(a_i)`,
`i∈I_S`, satisfies `C⊇S^+`. (b) If `I_S` is infinite, `S^+` is finite;
explicitly, listing `I_S={i_1<i_2<⋯}` and `C_m:=⋂_{l=1}^m rad(a_{i_l})`,
there is a finite `m_0` with `C_m=S^+` for all `m≥m_0`, and
`|S^+|≤ω(a_{i_1})`.

**Proof.** (a) Immediate from the definition of intersection. (b)
One-line application of the already-certified Generalized Lemma C to
`I:=I_S`: `C_m` is non-increasing and bounded below, so it stabilizes at
some finite `m_0`, and the stabilized value equals the full infinite
intersection `S^+` by the same argument used for `D_S`
(`lemmas/lemma-lambda-S-reduction-and-single-companion-finiteness.md`).
`∎`

**Note.** Both lemmas inherit, unproved, the standing open hypothesis
"`I_S` infinite for a general proper core `S`" (not established in general;
verified case-by-case).

## Certification

Both statements independently re-derived from scratch by the round-8
proof-reviewer (Freeze-Confinement Domination Lemma: hand-checked the
minimality argument, no gap; `S^+` Lemma: direct application of the
already-certified Generalized Lemma C, no gap). Independently re-simulated
`a_1=21528751,S={1061}` from scratch (fresh generator, exact `sympy`
factorization, no reuse of the builder's cache) and reproduced **exactly**:
`|I_S|=19`, the same 19 indices `{280,596,3741,7201,10658,14118,17577,
21037,24495,27954,31413,34872,38332,41791,45250,48710,52169,55627,59086}`,
every one of the 19 radicals cited by the source (including the two
outliers `a_{280}={2,3,7,11,1061}` and `a_{596}={2,3,5,7,97,1061}`), and
`S^+={2,3,7,1061}` — a full, independent, exact reproduction of the
source's central numeric table, zero discrepancies. Certified
`solved`-quality (unconditional part (a); part (b) conditional only on the
already-flagged standing "`I_S` infinite" hypothesis, consistent with how
`D_S`/`Q_S` are already certified elsewhere in this workspace).
