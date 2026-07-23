# Lemma XC (Cross-Companion Reduction) + Lemma NIDF + Lemma FT (Finite One-Sided Transversal)

**Source.** `approaches/sunflower-bundle-closure.md`, §7.1–7.3 (round 10).

**Purpose.** Resolves the round-10 outline-reviewer's mandatory Step-0 gap for
`sunflower-bundle-closure`'s attempted use of the certified Δ-system Dichotomy
Lemma (`lemma-delta-system-dichotomy.md`, which requires a uniform size bound `M`
on the family of companion sets — not established, and per `theorem-UBS-false-
case-II.md`, likely false for some cores). These three lemmas require **no**
size-boundedness hypothesis on the companion-set family at all.

## Setup

Fix disjoint nonempty cores `S,S'\subseteq P_1` with `I_S,I_{S'}\ne\varnothing`
(nonempty; Lemma FT additionally needs both infinite). Write
`\mathrm{comp}(a_i):=\mathrm{rad}(a_i)\setminus P_1`, `S(i):=\mathrm{rad}(a_i)\cap
P_1` (Theorem CD's core map).

## Lemma XC (Cross-Companion Reduction) — unconditional, fully proved

**Statement.** For any `i,j` with `S(i)\cap S(j)=\varnothing`: `\mathrm{rad}(a_i)
\cap\mathrm{rad}(a_j)=\mathrm{comp}(a_i)\cap\mathrm{comp}(a_j)`.

**Proof.** `\mathrm{rad}(a_i)=S(i)\sqcup\mathrm{comp}(a_i)`,
`\mathrm{rad}(a_j)=S(j)\sqcup\mathrm{comp}(a_j)` (disjoint, since
`\mathrm{comp}(\cdot)\cap P_1=\varnothing` by definition). Expanding the
intersection into 4 cross-terms, the `S(i)\cap S(j)$ term vanishes by hypothesis,
the two mixed terms (`S(i)\cap\mathrm{comp}(a_j)`, `\mathrm{comp}(a_i)\cap S(j)`)
vanish since `S(\cdot)\subseteq P_1` and `\mathrm{comp}(\cdot)\cap P_1=\varnothing`;
only `\mathrm{comp}(a_i)\cap\mathrm{comp}(a_j)` survives. $\blacksquare$

## Lemma NIDF (Nonempty Companions, No Infinite Disjoint Sub-family) — unconditional, fully proved

**Statement.** (a) `\mathrm{comp}(a_i)\ne\varnothing` for every `i\in I_S`, and
symmetrically for `I_{S'}`. (b) `\{\mathrm{comp}(a_i):i\in I_S\}` contains no
infinite pairwise-disjoint sub-family; symmetrically for `I_{S'}`.

**Proof.** (a) Fix `j_0\in I_{S'}`. By the already-certified Lemma P′,
`\mathrm{rad}(a_i)\cap\mathrm{rad}(a_{j_0})\ne\varnothing` for every `i`; by Lemma
XC (`S(i)=S`, `S(j_0)=S'` disjoint), `\mathrm{comp}(a_i)\cap\mathrm{comp}(a_{j_0})
\ne\varnothing`, so `\mathrm{comp}(a_i)\ne\varnothing`. (b) Suppose `L\subseteq I_S`
infinite with `\{\mathrm{comp}(a_i)\}_{i\in L}` pairwise disjoint. Fix `j_0\in
I_{S'}`. By (a)'s argument, `\mathrm{comp}(a_{j_0})\cap\mathrm{comp}(a_i)\ne
\varnothing` for every `i\in L`; choose `w_i` in this intersection. If `i\ne i'`
in `L`, `w_i\ne w_{i'}` (else the common value lies in `\mathrm{comp}(a_i)\cap
\mathrm{comp}(a_{i'})=\varnothing`). So `i\mapsto w_i` injects `L` into the *fixed,
finite* set `\mathrm{comp}(a_{j_0})`, forcing `|L|<\infty`, a contradiction.
$\blacksquare$

**Key feature.** No hypothesis on the size of `\mathrm{comp}(a_i)` *uniformly over*
`i\in I_S` is used — only that the *single fixed* set `\mathrm{comp}(a_{j_0})` is
finite, which is automatic (radical of one integer). This is what makes the lemma
immune to the unresolved `(UB_S)`/companion-bundle-size-boundedness question.

## Lemma FT (Finite One-Sided Transversal) — unconditional, fully proved

**Statement.** For a doubly-infinite disjoint core pair `(S,S')`, there exist
finitely many `i_1,\dots,i_r\in I_S` (`r\ge1`) with `\mathrm{comp}(a_{i_1}),\dots,
\mathrm{comp}(a_{i_r})` pairwise disjoint, such that `U_S:=\mathrm{comp}(a_{i_1})
\cup\dots\cup\mathrm{comp}(a_{i_r})` (finite) meets `\mathrm{comp}(a_i)` for
**every** `i\in I_S`. Symmetrically, a finite `U_{S'}` meets `\mathrm{comp}(a_j)`
for every `j\in I_{S'}`.

**Proof.** Greedy maximal packing: build a pairwise-disjoint sub-collection of
`\{\mathrm{comp}(a_i):i\in I_S\}` by repeatedly adjoining any `\mathrm{comp}(a_i)`
disjoint from the union so far, until no further index can be added. By Lemma
NIDF(b), this process cannot run infinitely (an infinite run would produce an
infinite pairwise-disjoint sub-family), so it terminates at some finite `r\ge1`.
At termination (maximality), every `i\in I_S` has `\mathrm{comp}(a_i)` intersecting
`U_S:=\bigcup_{k=1}^r\mathrm{comp}(a_{i_k})` — else the process would not have
stopped. `U_S` is a finite union of finitely many finite sets, hence finite.
$\blacksquare$

**Corollary.** `W:=U_S\cup U_{S'}` is finite and meets every `\mathrm{comp}(a_i)$,
`i\in I_S`, **and** every `\mathrm{comp}(a_j)`, `j\in I_{S'}`, **separately** (one
side at a time — not yet the joint Stabilization-Conjecture condition).

## What is NOT established (open — Conjecture (JW))

Lemma FT does **not** give the Stabilization Conjecture: it only guarantees each
side separately meets its own witness pool, not that the *same* element of
`W=U_S\cup U_{S'}` is shared by both `a_i` and `a_j` for a given cross pair
`(i,j)`. The builder correctly and precisely diagnoses (§7.4 of the source file)
that a natural refinement attempt reduces exactly to a new rigidity question
(whether the witness `u` linking `a_i` to a representative `a_{i_k}` can always be
taken equal to the witness `w` linking `a_{i_k}` to `a_j`) which is **not**
resolved by the purely combinatorial tools used here. This is recorded as
**Conjecture (JW)**, honestly open.

## Certification

Certified `solved`-quality (sorry-free, unconditional): all three lemmas (XC, NIDF,
FT) are complete, elementary proofs with no gaps or hidden hypotheses.

**Independently re-verified by the round-10 proof-reviewer** (fresh generator, own
greedy-sequence simulation, not reused from the builder's script):
- `a_1=247`, `(S,S')=(\{13\},\{19\})`, `n=20000`: reproduced `|I_{13}|=10764`,
  `|I_{19}|=6910` exactly; reproduced the greedy transversal
  `U_{13}=\{2,3,5,7\}` (representatives at indices 2,4 with companions `\{2,5\}`,
  `\{3,7\}`) and `U_{19}=\{2,3,5,7\}` (representatives at indices 3,5, companions
  `\{2,7\}`, `\{3,5\}`) exactly, bit-for-bit; independently checked all
  `10764\times6910=74{,}379{,}240` cross pairs against `W=U_{13}\cup U_{19}=
  \{2,3,5,7\}`, zero violations.
- `a_1=21528751`, `(S,S')=(\{103\},\{197\})`, `n=6000`: reproduced `|I_{103}|=5857`,
  `|I_{197}|=102` exactly; reproduced the representative indices and companion
  sets exactly (`U_{103}=\{2,3,7,13,19,41,193,2297,2549\}`,
  `U_{197}=\{2,3,7,1301\}`); independently checked all `5857\times102=597{,}414`
  cross pairs against `W=U_{103}\cup U_{197}`, zero violations (also confirmed
  the small candidate `\{2,3,5,7,11,13\}` alone gives zero violations on this
  specific pair). **Minor discrepancy noted, not affecting correctness:** the
  source file states `|W|=12` primes for this instance; the correct count of the
  union as constructed is `10` (`\{2,3,7,13,19,41,193,1301,2297,2549\}`) — an
  arithmetic slip in the write-up, not a proof error; flagged for the builder to
  correct next round.

**Open, not to be treated as proved:** Conjecture (JW) (equivalently: upgrading
Lemma FT's separate one-sided coverage to the joint two-sided Stabilization
Conjecture). This is the sole remaining gap of this approach.
