# Proof-reviewer report — imo-2026-01 (round 1)

Reviewed two independent candidate complete proofs. Both are correct and complete. Every
load-bearing step re-derived from scratch and cross-checked computationally (sympy/python):
per-prime move law over 2000 random pairs; `gcd(min(a,b),|a−b|)=gcd(a,b)` exhaustively for
0≤a,b<30; unique survivor = `∏_p p^{g_p}` over 3000 random boards × 15 random move-orders; the
Lemma 5 `{4,6,9}` reduct by hand.

---

## Approach 1: `perprime-valuation` — APPROVE (Status: solved)

Builder-recorded Status `solved` is CORRECT.

Verification of the five scrutiny points:
- (i) **Per-prime move law (Lemma 1).** `v_p(d)=min(a,b)` and `v_p(e)=max−min=|a−b|` correctly derived
  from unique factorization; integrality `gcd|lcm` proven (`gcd(m,n)|mn/gcd(m,n)`). Valuation-0 edge case
  `{0,0}↦{0,0}` addressed. Correct.
- (ii) **Termination monovariant (Lemma 2).** `ΔΩ_tot=−Ω(gcd(m,n))≤0`, strict iff `gcd>1`; the `gcd=1`
  branch shown to drop `C` by exactly 1 (`{m,n}→{1,mn}`, `mn>1`). Lex order on ℕ×ℕ is a genuine
  well-order and the no-infinite-descent argument is given correctly. STRICT decrease holds in BOTH
  branches. Correct.
- (iii) **Exactly one (not zero) survivor.** `C≤1` from termination; `C≥1` from a prime with `g_p≥1`
  (some initial entry >1) surviving invariance. Rules out all-ones. Correct.
- (iv) **`g_p` invariance.** `gcd(min(a,b),|a−b|)=gcd(a,b)` (Lemma 3, subtractive Euclid, zero edge cases
  covered) plus the associativity/commutativity list-fold (Lemma 4) correctly lift the one-pair identity
  to the full-board invariant. Gcd-with-0 conventions used consistently. Correct.
- Value `M=∏_p p^{g_p}` read off the terminal `{M,1,…,1}` via `g_p=v_p(M)`, tied back to the initial
  board. Answer requirement (none — proof-only) satisfied; explicit `M` bonus and verified.

No skipped cases, no hand-waving, all invoked facts named. Complete and rigorous.
Scores — Correctness 10/10, Completeness/rigor 10/10, Progress: from empty to a full self-contained proof.
Outcome recorded: `verified-milestone`.

---

## Approach 2: `descent-induction` — APPROVE (Status: solved)

Builder-recorded Status `solved` is CORRECT.

Shares Lemmas 1–3 with Approach 1 (identical, correct). The distinctive machinery:
- **Lemma 4 (disjoint moves commute).** Correct — a move reads/writes only its two cells.
- (v) **Lemma 5 (3-cell / share-one critical pair).** This is the crux and it is closed correctly and
  NON-circularly. From `B'` a maximal sequence restricted to `{X,Y,Z}` terminates (lex monovariant) with
  ≤1 of the three cells >1; the `g_p^{XYZ}` invariant forces the survivor value to be exactly
  `s=∏_p p^{gcd(v_p x,v_p y,v_p z)}`, so the reduct is the EXPLICIT board `{s,1,1}` on the three cells.
  Same from `B''`. Both reach the same value-multiset `W`, an explicit common reduct — the argument does
  NOT assume "normal forms are unique," so no circularity. Verified on `{4,6,9}` (s=6, both branches meet
  at `{2,3,6}`).
- **Descent induction (§7).** Well-founded induction on `(Ω_tot,C)`; principle (R) sound (both `V,V'` have
  measure `<μ(B)`, so IH applies). The three critical-pair cases (`|∩|=2/1/0`) are disjoint and
  exhaustive and each is closed. Not circular; the induction rests on well-foundedness from Lemma 2.

One point checked and cleared: the proof treats board equality as equality of the VALUE multiset
(position labels are explicitly "bookkeeping only"). Under this reading — which is the stated model and
the only sensible one, since the move does not fix which cell receives gcd vs lcm/gcd — `W_1=W_2` and
`B'=B''` in the identical-move case hold. The claim `T(B)` singleton is about value-multisets; part (b)
only needs the surviving value `M`, which is what is delivered. Consistent throughout.

No skipped cases, no hand-waving, all facts named. Complete and rigorous.
Scores — Correctness 10/10, Completeness/rigor 10/10, Progress: full independent proof via a different
(confluence-by-descent) route.
Outcome recorded: `verified-milestone`.

---

## Certified promotable lemmas
Written to `results/imo-2026-01/lemmas/`:
- `perprime-move-step.md` (Lemma 1) — certified.
- `gp-valuation-invariant.md` (Lemma 3 identity + full-board invariant + closed form) — certified.
- `lex-monovariant-termination.md` (Lemma 2) — certified.
- `three-cell-joinability.md` (Lemma 5, explicit non-circular reduct) — certified.

## current.md
Created (did not previously exist): Status `solved`, Full proof populated (perprime-valuation as primary,
descent-induction noted as an independent second proof).

## Verdicts
- `perprime-valuation`: **APPROVE** (solved)
- `descent-induction`: **APPROVE** (solved)
