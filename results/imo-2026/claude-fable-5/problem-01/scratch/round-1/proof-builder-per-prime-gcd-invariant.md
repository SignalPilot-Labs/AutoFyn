# Build report — round 1 — imo-2026-01 — slug: per-prime-gcd-invariant

Status written: **solved**. File: results/imo-2026-01/approaches/per-prime-gcd-invariant.md

## What I closed (all three outlined GAPs)
- GAP 1 (rigor of L1–L4): Lemma 1 (valuations of gcd/lcm and of a move) proved from the
  divisibility criterion of the Fundamental Theorem of Arithmetic — gcd and lcm constructed
  explicitly as prod p^min / prod p^max, and lcm/gcd shown integral before subtracting
  valuations. Multiset-gcd conventions (gcd of all-zero = 0; common divisors of T = divisors of
  gcd(T), proved via the lcm(d,e) trick, not asserted) stated before use. Lemma 4 (Euclidean
  subtraction with zeros) proved via equality of common-divisor SETS, which handles all four
  exponent cases (a=b>0, a!=b>0, one zero, both zero) uniformly and explicitly.
- GAP 2 (assembly): invariance of g_p is a formal induction on the move count (Corollary after
  Lemma 5); termination is strict lex descent (Lemma 2) plus an inline proof of
  well-foundedness of lex order on N x N (Lemma 3) — not cited bare.
- GAP 3 (C never increases, incl. m = n): Lemma 2 shows Delta S = -Omega(gcd(m,n)) exactly, and
  the two cases gcd>1 (covers m=n, outputs (m,1)) vs gcd=1 (outputs (1,mn), C drops by exactly
  1) are exhaustive and disjoint; strictness of the lex decrease is argued explicitly in each
  case, per the outline-reviewer's minor note.

Also covered: Step 0 (outputs are positive integers, lcm/gcd is an integer — needed before any
valuation subtraction), the terminal-shape reading of "continues while possible", the
not-all-ones half of (a) via g_p >= 1, and part (b) with the explicit choice-free formula
M = prod_p p^{gcd_i v_p(a_i)}, verified on the {4,6} example by hand.

Reviewer's tripwires respected: termination uses only the single global (S,C) monovariant (no
per-prime counter); nowhere is coprimality of the two outputs claimed or used; per-prime
reasoning appears only in the invariance argument, where it is legitimate (a move changes two
positions and acts as (min, |diff|) at every prime simultaneously).

## Independent check (not a proof step)
Fresh python run (my own code): 300 random boards (sizes 2–7, entries 2–200), random full runs;
asserted at EVERY move that (S,C) strictly lex-decreases, and at termination that exactly one
entry > 1 and it equals prod_p p^{gcd_i v_p(a_i)}. 0 failures.

## Gaps remaining
None known. The one place the reviewer should scrutinize hardest: the multiset-gcd conventions
paragraph (common divisors of T = divisors of gcd(T) via the lcm trick) and the simultaneity
remark in Lemma 5 (the two multisets are all-zero simultaneously since a=b=0 iff
min=|a-b|=0).

## Promotable lemmas (for reviewer certification into results/imo-2026-01/lemmas/)
- Move-valuation lemma (Lemma 1) — reusable by newman-confluence for its exponent case checks.
- Euclidean subtraction identity with zeros (Lemma 4).
- Lex well-foundedness on N x N (Lemma 3) — reusable for any termination argument here.

## Spec concerns
None. `answer_type` is none (proof-only); the explicit formula for M is stated as a byproduct,
not claimed as a required numeric answer. 2026 plays no role beyond the bound C <= 2026, noted.
