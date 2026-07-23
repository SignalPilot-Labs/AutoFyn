# Local No-Resurrection/Interval/Equivalence Theorem, Subset Lemma, No-Shortcut Corollary

**Source.** `results/imo-2026-06/approaches/forced-primes-well-ordering.md`
§J (round 11). Depends on: already-certified Theorem CD
(`lemmas/theorem-CD-core-decomposition-and-lemma-TC.md`), Theorem V /
No-Resurrection Lemma (`lemmas/theorem-V-veto-finite-iff-MRS.md`), Λ_S-
Reduction Lemma and Multi-Companion Reduction Proposition
(`lemmas/lemma-lambda-S-reduction-and-single-companion-finiteness.md`),
Permanent Bundle Lemma (`lemmas/lemma-permanent-bundle.md`).

## Setup

Fix a proper core `S\subsetneq P_1` with `I_S` infinite. `M_n^S:=\{i\in
I_S\cap[1,n]:$ no `k\in I_S\cap[1,n]` has `\mathrm{rad}(a_k)\subsetneq
\mathrm{rad}(a_i)\}` (the *local* `n`-minimal indices, competitors drawn
only from `I_S`, not all of `[1,n]`). `\mathcal M_n^S:=\{\mathrm{rad}
(a_i):i\in M_n^S\}`. `(MRS_S)`: `\exists n^*` with `\mathcal M_n^S=
\mathcal M_{n^*}^S` for all `n\ge n^*`. `\mathcal V_S^{\mathrm{loc}}:=
\bigcup_{n\ge1}\mathcal M_n^S`.

## Local No-Resurrection Lemma

**Statement.** If `C=\mathrm{rad}(a_i)` for some `i\in I_S`, and some
`k\in I_S` has `\mathrm{rad}(a_k)\subsetneq C`, then `C\notin\mathcal
M_m^S` for every `m\ge k`.

**Proof.** If `C\in\mathcal M_m^S` for some `m\ge k`, then `C=\mathrm{rad}
(a_j)` for `j\in M_m^S\subseteq I_S\cap[1,m]`, with no `l\in I_S\cap[1,m]`
having `\mathrm{rad}(a_l)\subsetneq C`. But `k\in I_S`, `k\le m`, so
`k\in I_S\cap[1,m]`, and `\mathrm{rad}(a_k)\subsetneq C` — contradiction.
`\blacksquare` (Exact restriction of the certified global No-Resurrection
Lemma's proof to the competitor pool `I_S`.)

## Local Interval Lemma

**Statement.** For `v\in\mathcal V_S^{\mathrm{loc}}`, `A_v^S:=\{n\ge1:
v\in\mathcal M_n^S\}` is a contiguous interval `[n_v,\infty)` or
`[n_v,e_v)`, `n_v:=\min A_v^S`.

**Proof.** `n_v` exists by well-ordering. If `E_v^S:=\{n>n_v:v\notin
\mathcal M_n^S\}=\varnothing`, `A_v^S=[n_v,\infty)`. Else `e_v^S:=\min
E_v^S` exists; minimality gives `A_v^S\supseteq[n_v,e_v^S)`; for `c\ge
e_v^S`, the realizing index `i\le n_v<e_v^S` of `v` must have been
dethroned by some `k\in I_S\cap[1,e_v^S]` with `\mathrm{rad}(a_k)
\subsetneq v`, so the Local No-Resurrection Lemma gives `v\notin\mathcal
M_c^S` for all `c\ge e_v^S`. `\blacksquare`

## Local Equivalence Theorem

**Statement.** `(MRS_S)\iff\mathcal V_S^{\mathrm{loc}}` finite.

**Proof.** `(\Leftarrow)`: for finite `\mathcal V_S^{\mathrm{loc}}`, let
`m_v` be the right endpoint description of `A_v^S` (from the Interval
Lemma) and `n^*:=\max_v m_v` (finite max over a finite set); for `n\ge
n^*`, membership of every `v` in `\mathcal M_n^S` is fixed, giving
`\mathcal M_n^S=\mathcal M_{n^*}^S`. `(\Rightarrow)`: freeze index `n^*`
gives `\mathcal V_S^{\mathrm{loc}}=\bigcup_{m=1}^{n^*}\mathcal M_m^S`, a
finite union of finite sets. `\blacksquare` (Exact local analogue of the
certified global Theorem V.)

## Subset Lemma

**Statement.** `\mathcal V_S\subseteq\mathcal V_S^{\mathrm{loc}}` for
every proper core `S` (no hypothesis on `I_S` infiniteness needed).

**Proof.** `C\in\mathcal V_S\Rightarrow C\in\mathcal M_n` for some `n`,
realized by `i\in M_n\subseteq\{1,\dots,n\}$, `C\cap P_1=S` so `i\in I_S`.
Global minimality (no `k\in\{1,\dots,n\}` dominates `C`) is a stronger
requirement than local minimality (no `k\in I_S\cap[1,n]\subseteq
\{1,\dots,n\}` dominates `C`), so `i\in M_n^S`, giving `C\in\mathcal
M_n^S\subseteq\mathcal V_S^{\mathrm{loc}}`. `\blacksquare`

**Note.** This containment can be strict: on `a_1=21528751`, `S=\{197\}`,
`\mathcal V_S=\varnothing` while `\mathcal M_n^S` already has (at
`n=400{,}000`) 3 elements — `(MRS_S)` is a genuinely stronger requirement
than `\mathcal V_S`-finiteness, not a restatement of it.

## No-Shortcut Corollary

**Statement (general form).** For any proper core `S` with `I_S`
infinite that has a certified realized permanent multi-companion bundle
`Q` of size `\ge2` (in the sense of the Permanent Bundle Lemma), `(MRS_S)`
entails (via `(MRS_S)\Rightarrow\mathcal V_S^{\mathrm{loc}}$ finite
`\Rightarrow` (Subset Lemma) `\mathcal V_S` finite `\Leftrightarrow$
(Λ_S-Reduction Lemma) `\Lambda_S` finite) resolving the Multi-Companion
Reduction Proposition's hitting-set target for `S`, already certified to
be of the same order of difficulty as FCBC itself.

**Concrete instance.** `S=\{103,197\}`, `Q=\{11,97\}` (a1=21528751):
`\{103,197,11,97\}` is a certified permanent bundle (Permanent Bundle
Lemma), hence `\{11,97\}\subseteq\Lambda_{\{103,197\}}`, and since
`|Q|=2\ge2`, the Multi-Companion Reduction Proposition applies (not the
easier `|Q|=1` case). So establishing `(MRS_{\{103,197\}})` would resolve
this equi-hard-to-FCBC hitting-set condition.

## Verification

Independently re-derived every proof above line-by-line (no gaps found;
each is a faithful, correctly-scoped restriction/analogue of an
already-certified global lemma to the competitor pool `I_S`). Independently
re-simulated: (a) `\{103,197,11,97\}` is realized at index 862 (0-indexed)
of the generated `a_1=21528751` sequence (value `21650497`) — confirms the
concrete instance is non-vacuous; (b) `|I_{\{1061\}}|=4`, `|I_{\{103,197\}}|
=40` within `n\le8000` and both classes continuing to grow at increasing
indices, consistent with (not a proof of) both being infinite, as this
round's setup assumes.

## Scope / usage note

The Local Equivalence Theorem and Subset Lemma are pure structural facts,
reusable for any proper core with `I_S` infinite; they do **not** prove
`(MRS_S)` itself, which remains open. The No-Shortcut Corollary is a
genuine negative result: it proves (not merely observes) that closing
`(MRS_S)` for a core with a known size-`\ge2` permanent bundle cannot
bypass the workspace's already-flagged hardest open sub-problem. Future
approaches should not expect `(MRS_S)`-for-a-single-core to be an easier
route to Stabilization than the hitting-set target itself, for any core
with such a bundle.
