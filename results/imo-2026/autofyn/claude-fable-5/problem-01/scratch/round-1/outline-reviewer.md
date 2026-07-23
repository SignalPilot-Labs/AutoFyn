# Outline review — round 1 — imo-2026-01

Field: two new approaches, both whole attempts at both parts (a) and (b). Genuinely
different framings — a conserved-quantity proof with an explicit formula for M vs a
rewriting-theoretic uniqueness-of-normal-form proof that never computes M. Their walls
are distinct (the invariant route has no analogue of the overlap-joinability crux), so
the field is not in the single-gap trap. No prior dead ends to check (fresh workspace);
the outliner correctly banned the recorded false framings (P exact invariant,
squarefree-kernel formula, "outputs are coprime").

Independent verification run this round (python, my own code, not the explorers'):

- 400 random boards (sizes 2–6), 8 random full runs each: terminal multiset identical
  across runs, exactly one entry > 1, and that entry equals prod_p p^{gcd_i v_p(a_i)}.
  0 failures.
- 150 random 3-element boards, EXHAUSTIVE branch over all move sequences: the terminal
  multiset is unique in every case. 0 failures. This is direct evidence for
  newman-confluence's L3 target statement (not a proof).

---

## per-prime-gcd-invariant — VERDICT: APPROVE

Whole attempt: yes (both parts, explicit M). Technique: exact invariant + strict lex
monovariant — squarely the right tool (KB: Invariants & monovariants), and the formula
survives my independent numerical test.

Skeleton audit:
- Step 1 (L1, valuations of a move): correct; max - min = |a-b| is exact.
- Step 2 (L2, (S,C) lex descent): Delta S = -Omega(gcd(m,n)) checks out; the coprime
  case drops C by exactly 1; C never increases since two entries > 1 are replaced by at
  most two entries > 1. Sound. The m = n case (outputs (m,1), gcd = m > 1, S drops) is
  covered in the case list — keep it in the write-up.
- Step 3 (terminal shape): correct reading of "continues while possible"; C <= 1.
- Step 4 (L3, g_p invariance): gcd(a,b) = gcd(min(a,b), |a-b|) is the Euclidean
  subtraction identity; gcd-associativity over untouched entries is valid. The stated
  conventions (gcd of all-zero multiset = 0, gcd(0,t) = t) are exactly the ones needed
  for step 6 to read off v_p(M). No circularity.
- Step 5 (not all ones): a_1 > 1 guarantees a prime with g_p >= 1; all-ones terminal
  board would give g_p = 0 — clean contradiction. This closes "exactly one", the half
  most outlines forget.
- Step 6 (part b): terminal valuation multiset {v_p(M), 0, ..., 0} has gcd v_p(M);
  invariance pins v_p(M) = g_p(initial) for all p. Choice-free formula. Verified on
  {4,6} by hand and on 400 random boards.

Case coverage: complete and disjoint (gcd = 1 / gcd > 1, m != n / m = n; exponent cases
a=b>0, a!=b positive, one zero, both zero). Each named lemma has a stated, correct
mechanism. Open gaps are pure write-up rigor, not mathematical unknowns.

Minor notes for the builder (not blockers):
- In step 2, state explicitly why the two claims combine into a STRICT lex decrease in
  every case (gcd > 1 => S strictly drops; gcd = 1 => S unchanged AND C strictly drops).
- Per-prime invariance is legitimate but termination must stay the single global (S,C)
  monovariant — the outline already flags this; hold the builder to it.
- State the induction "after k moves g_p equals its initial value" formally (GAP 2).

This approach can plausibly reach `solved` this round.

## newman-confluence — VERDICT: CHANGES REQUESTED

Whole attempt: yes. Technique: Newman's lemma is a legitimate, capable engine for (b),
and the framing is far from the invariant route — worth keeping in the field. Steps 1,
2, 4, 5, 6 and the disjoint-diamond L2 are sound as outlined; L5's exponent case check
is correct and the outline rightly notes confluence alone does not exclude the all-ones
normal form. My exhaustive 3-board test supports the L3 target statement.

Required change (address while building, at Step 3 / L3):
1. **The candidate mechanism for L3 as stated risks circularity.** "Prove 3-element
   boards have a unique terminal multiset by strong induction on the product" — the
   natural induction step for uniqueness of terminals IS local confluence on the smaller
   board, i.e. the very statement being proved. The outline's no-circularity warning in
   GAP 1 names the risk but no mechanism that escapes it. The builder must do one of:
   (i) run the strong induction as a Newman-style argument scoped to 3-boards (prove
   local confluence for 3-boards by explicit joining sequences for each overlap pattern,
   then get uniqueness by the induction — the joining sequences are the actual content
   and must be exhibited, not deferred); or (ii) prove the 3-board terminal multiset
   directly ({M', 1, 1} with M' pinned by some self-contained argument) — but if that
   argument is the g_p invariant, say so honestly: the approach then differs from
   per-prime-gcd-invariant only in its outer architecture, and the reviewer should weigh
   whether it still earns a separate slug.
2. Per the outline's own tripwire: joining sequences must be built at the INTEGER level;
   any per-prime joinability argument is inadmissible unless the shared-schedule
   coupling is handled explicitly.
3. GAP 2 (Newman's lemma proved inline by well-founded induction) is mandatory — it is
   not in knowledge_base.md and may not be cited bare.

If L3 cannot be closed non-circularly after honest effort, this slug is RETHINK next
round (the outline itself says so) — do not let it limp as a permanent gap.

---

## Ranking

Registered both new slugs at 1500 (fresh population, no established opponents).
Comparison applied: per-prime-gcd-invariant beats newman-confluence — every lemma in
the former has a verified elementary mechanism and its gaps are write-up work, while
the latter carries one load-bearing hard gap (L3) with an unresolved circularity risk.
Elo now: per-prime-gcd-invariant 1516, newman-confluence 1484.

## Build set

Both build: the favorite to push for `solved`, the fallback to test whether L3 closes
(cheap to learn now; its failure mode is well-specified).

build set: per-prime-gcd-invariant, newman-confluence
