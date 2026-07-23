# Corollary W3′ (domination by the minimal-radical antichain) and Lemma MS
(Minimal-Radical Stabilization ⟹ FCBC)

## Notation

`P_i:=rad(a_i)`. For `n≥1`, `M_n⊆{1,…,n}` is the set of `n`-minimal indices
(Lemma W3, already certified in
`lemmas/lemma-W2-W3-patch-and-minimal-radical-reduction.md`). Define
`𝓜_n:={P_i : i∈M_n}` (the set of *distinct radical values* realized by the
`n`-minimal indices — a finite antichain of finite prime-sets under `⊆`).

**Hypothesis (MRS)** (NOT proved — this is the open content flagged below):
there exists `N_0≥1` with `𝓜_n=𝓜_{N_0}` for every `n≥N_0`. Write
`𝓜_∞:=𝓜_{N_0}` and `H:=⋃_{S∈𝓜_∞}S`.

## Corollary W3′

**Statement.** For every `n≥1` and every `i_0∈{1,…,n}`, there exists
`j*∈M_n` with `P_{j*}⊆P_{i_0}`.

**Proof.** Extracted verbatim from the already-certified proof of Lemma W3's
`(⇐)` direction, isolating the part that does not use the `gcd(x,a_i)>1`
hypothesis. Let `S:={k∈{1,…,n}:P_k⊆P_{i_0}}`; `i_0∈S` so `S≠∅`. Choose
`j*∈S` minimizing `|P_{j*}|`. If `j*∉M_n`, some `k∈{1,…,n}` has
`P_k⊊P_{j*}⊆P_{i_0}`, so `k∈S` with `|P_k|<|P_{j*}|`, contradicting
minimality of `j*`. Hence `j*∈M_n`, and `P_{j*}⊆P_{i_0}` by construction.
`∎`

This uses no new hypothesis; it is a standalone restatement of already
certified material, isolated because Lemma MS needs it in this explicit
form.

## Lemma MS

**Statement.** If (MRS) holds, then `H` (as defined above) is a finite
covering set: `H∩P_i∩P_j≠∅` for **every** `1≤i<j` of the whole infinite
sequence — i.e. `H` satisfies FCBC / hypothesis `(†')` of the certified
Theorem 5.1 (`lemmas/theorem-5.1-master-conditional-theorem.md`) exactly.

**Proof.**

*Step 1 (every index is dominated by `𝓜_∞`).* Fix any `i≥1`. Let
`n:=max(i,N_0)≥N_0`, so `𝓜_n=𝓜_∞` by (MRS). Apply Corollary W3′ with this
`n` and `i_0:=i` (valid since `i≤n`): there is `j*∈M_n` with `P_{j*}⊆P_i`.
Since `j*∈M_n`, `P_{j*}∈𝓜_n=𝓜_∞`. So every `i≥1` has `P_i⊇S_i` for some
`S_i∈𝓜_∞`.

*Step 2 (`𝓜_∞` is pairwise intersecting).* Each `S∈𝓜_∞` equals `P_k` for
some actual index `k`. Given `S,S'∈𝓜_∞` with `S=P_k`, `S'=P_{k'}`: if
`S=S'`, `S∩S'=S≠∅` (radicals of integers `>1` are nonempty). If `S≠S'` then
`k≠k'`, and the already-certified **Lemma P′** (pairwise global
intersection, `lemmas/lemma-P-prime-pairwise-intersecting.md`) gives
`gcd(a_k,a_{k'})>1`, i.e. `P_k∩P_{k'}≠∅`, i.e. `S∩S'≠∅`.

*Step 3 (`H` covers every pair).* Fix `i<j`. By Step 1, `P_i⊇S_i`, `P_j⊇S_j`
for some `S_i,S_j∈𝓜_∞`. By Step 2, `S_i∩S_j≠∅`; pick `p∈S_i∩S_j`. Then
`p∈S_i⊆H`, `p∈S_i⊆P_i`, `p∈S_j⊆P_j`, so `p∈H∩P_i∩P_j`. As `i<j` were
arbitrary, `H` covers every pair. `∎`

**Corollary (MS + Theorem 5.1).** If (MRS) holds, `H` satisfies `(†')`, so
the already-certified Theorem 5.1 gives `a_{n+T}=a_n+L` for every `n≥1`
(`T=|Good|`, `L=lcm(H)`) — i.e. (MRS) alone (via Lemma MS and Theorem 5.1)
finishes the **entire** problem for Case II.

## Independent re-verification (reviewer, round 4)

Re-derived both proofs from scratch by hand — no gaps found; Corollary W3′
is a faithful, correctly-isolated sub-argument of the certified Lemma W3
proof, and Lemma MS's three-step argument is a correct, non-circular
consequence of Corollary W3′ and Lemma P′ alone.

Independently re-implemented the simulator from scratch (fresh Python, exact
integer factorization via `sympy.primefactors`, matching the problem's exact
recursive definition) and reproduced, with zero discrepancies:
- `a_1=15`: `𝓜_∞` stabilizes at `n=3`, `H={2,3,5}`.
- `a_1=221`: stabilizes at `n=6`, `H={2,3,5,13,17}`.
- `a_1=247,375,65,105`: matching `H` values, all confirmed by exhaustive
  pairwise-coverage check up to `N=600` (`179,700` pairs each, zero
  failures) and by the domination check (every `P_i`, `i≤600`, contains some
  element of `𝓜_∞`, zero failures).
- `a_1=4087`: independently reproduced the non-monotone "collapse" of
  `|𝓜_n|` reported in the source file: sizes climb `1,2,…,17,17,17,17`
  through `n=53` (with `H_{53}` an 18-prime set), then collapse in one step
  to `|𝓜_{54}|=3`, `H_{54}={2,61,67}` — exact match, including the specific
  prime sets, confirming this is a genuine phenomenon of the sequence, not a
  simulator artifact.

**Cross-approach finding (new, reviewer, round 4).** The `H` produced by
this construction coincides exactly, in every case checked
(`15,221,247,375,4087,4199`), with the independently-constructed set
`F∪P_1` from `forced-primes-well-ordering` (round 4) — three structurally
unrelated constructions (window search `H_K`, minimal-radical-antichain
union, forced/uniquely-shared-prime union) landing on the identical explicit
finite set in every tested case. See `current.md` round-4 update for
discussion.

## Status of the hypothesis

**(MRS) is NOT proved.** It is verified numerically with zero exceptions on
12 diverse `a_1` values (source file) and independently re-confirmed here on
6 of them, but no proof is offered or certified. In particular, the natural
Lemma-C-style monotone-descent strategy provably fails: `|𝓜_n|` is **not**
monotonic in `n` (the `a_1=4087` collapse above), so any proof of (MRS)
needs a genuinely new argument, not a transplant of Lemma C's technique.

## Source

`results/imo-2026-06/approaches/imprint-automaton-periodicity.md` (round 4).

## Certification

Lemma MS and Corollary W3′ are certified `solved`-quality (sorry-free) as a
**conditional** result: "(MRS) ⟹ FCBC" is fully, unconditionally proved.
Certified in the same sense as Theorem 5.1 is certified conditional on
`(†')` — this lemma removes one further layer, showing (MRS) alone (a single
concrete, numerically-testable finiteness/stabilization statement) suffices
to invoke Theorem 5.1 and finish the entire problem. (MRS) itself remains
open and is NOT certified; any future round citing this lemma must not
conflate "Lemma MS is certified" with "(MRS) is proved."
