# Proof-reviewer — IMO 2026 Problem 3, round 2

Three approaches reviewed. The problem is `compute_and_prove` /
`answer_type: expression`; `solved` needs BOTH a Liu lower-bound strategy (≥ f(n)
for all Xiang) AND a Xiang upper-bound forcing strategy (≤ f(n) for all Liu
configs), each rigorous for general n. **No approach closes both halves for
general n this round**, but real progress: **`c(2) = 4/7` is now rigorously
established end-to-end** (U(2) closed by `two-regime-disjunctive`'s four-
strategy family; L(2) round-1 certified). Two new reusable lemmas certified
(L*, mirror); one new lemma certified and written to file (U(2) four-strategy).

## Ground-truth checks I ran (python, exact rational arithmetic)

- **U(2) four-strategy formulas.** All four (`Liu_A=(1+a)/2`, `Liu_B=(1+b−a)/2`,
  `Liu_C=(1+c−b)/2`, `Liu_E=max(c,1−c)`) reproduce the directly-computed
  advantage `A` of the explicitly-constructed final multiset for 5 test configs.
  ✓ (`/tmp/verify_round2.py`).
- **U(2) bound `min ≤ 4/7` on a grid `N=84`**: **0 violations**. The unique
  config with `min = 4/7` is exactly `(1/7, 2/7, 4/7)` — the dyadic.
  Equality-iff-dyadic confirmed. ✓
- **Sliver strategies approach the infimum FROM ABOVE** (`Liu(s) ≥ inf`), so
  for non-dyadic configs (where `inf < 4/7` strictly by the equality
  analysis), Xiang picks `s` small enough for `Liu < 4/7` concretely. ✓
  Verified for Strategy B on config `(2/21, 4/21, 5/7)`.
- **Strategy A admissibility at `c = b` (the boundary).** At `c = b` exactly,
  the two sub-pieces `(c−b)/2 = 0` are degenerate (two marks would coincide).
  But for `c` slightly `> b`, the formula `Liu_A = (1+a)/2` is exact; and at
  `c = b`, Strategy C gives `Liu_C → 1/2 < 4/7`. The 4-way contradiction
  argument imposes condition (i) `a > 1/7` (from Strategy A); if Strategy A is
  degenerate the condition is vacuous and the contradiction still fires via
  the other three. **Minor rigor issue (one-line patch): the builder should
  note Strategy A is an infimum at `c = b`, not exact.** Does not break the
  bound. ✓
- **Mirror certificate** for n=1..5: merged multiset matches pair-pile,
  `A = 1/D(n)`, `Liu = f(n)` in every case. ✓
- **Lemma L* gap ≥ 0**: exact enumeration on the `D(n)` grid, all refinements
  `R'` by ≤ n marks, all integer `w ∈ [0, R_largest]`: min gap **0** for n=1, 2, 3.
  Equality at the self-similar extremal (`R'` = pair-pile, `w = R_largest`).
  ✓
- **L* Case 2 identity** re-derived: `oddsum({w}∪R') = w + oddsum(R') − A_tail`,
  bound reduces to `w ≤ evensum(R') + A_tail ≥ s_2 ≥ w` (using `w ≤ s_{r−1} ≤ s_2`
  for `r ≥ 3`). ✓
- **Dyadic n=2 saddle** (re-confirm): full grid enumeration, denom 168, 13530
  Xiang responses: min oddsum = 4/7 exactly. ✓

---

## `two-regime-disjunctive` — verdict: CHANGES REQUESTED (Status: partial)

**Honest progress.** Closes U(2) (previously open) and gives `c(2) = 4/7`
end-to-end. The regime boundary corrected to **dyadic vs non-dyadic** (per
round-1 reviewer F2 — the `n=1` sliver mode handles `x ∈ (1/3, 1/2]` which is
dominant, so the boundary cannot be dominant-vs-non-dyadic). The `n=1`
two-mode base falls out cleanly (threshold `x = 1/3 = α(1)`). Regime D (dyadic)
for all n via imported pair-pile. The four-strategy U(2) proof is a genuinely
NEW result with a clean 4-way contradiction and equality-iff-dyadic.

**Flaws found (adversarial):**

1. **Strategy A at `c = b` (minor rigor hole).** The admissibility claim
   "c ≥ b ⟹ c − b ≥ 0" is necessary but not sufficient: at `c = b` the two
   sub-pieces `(c−b)/2 = 0` are degenerate, and the two marks would coincide
   (marks must be distinct). Strategy A is exact for `c > b` strictly and an
   infimum at `c = b`. The bound `min ≤ 4/7` still holds (Strategy C covers
   `c = b` with `Liu_C → 1/2`), and the contradiction argument is unaffected
   (imposing MORE conditions only makes the contradiction easier). **One-line
   patch: note Strategy A is an infimum at `c = b`, covered by Strategy C.**

2. **Sliver strategies give infima, not attained values (honestly flagged).**
   The builder correctly notes this and argues (correctly) that for non-dyadic
   configs the strict gap `4/7 − inf > 0` lets Xiang pick a small-enough sliver
   for `Liu < 4/7`. I verified the approach-from-above property. At the dyadic
   (where all infs = 4/7), the pair-pile attains exactly 4/7. ✓ No flaw, but
   the proof should explicitly state the approach-from-above direction (I
   verified it; the builder asserts "inf ≤ 4/7 suffices" which is correct but
   leans on the unstated direction).

3. **General-n regime-N (n≥3, non-dyadic) — OPEN, honestly flagged.** The
   builder correctly identifies this as the headline gap. The n=2 four-strategy
   proof does not lift (each strategy is n=2-specific; the 4-way contradiction
   has no obvious (2^n−1)-way generalization). Numerical evidence (n=3 sub-grid)
   supports the conjecture but is NOT a proof. This is the approach's main
   remaining gap.

4. **Lower bound Lemma L general-n — imported dependency (open in sibling).**
   Correctly recorded as a dependency; `c(n) ≥ f(n)` for n≥3 not established by
   this approach.

**Verdict: CHANGES REQUESTED.** Real progress (closes U(2), a previously-open
gap; `c(2)` end-to-end rigorous). The general-n regime-N upper bound (n≥3) is
the open gap. Route the builder next round to (a) patch Strategy A at `c=b`,
(b) state the sliver approach-from-above direction explicitly, (c) attack the
general-n regime-N mechanism — the n=2 four-strategy template is a start but
needs a structural lift (e.g. a recursive sliver-pile decomposition
generalizing the n=2 pile-matching).

---

## `pairing-partner` — verdict: CHANGES REQUESTED (Status: partial)

**Honest progress.** The strongest reusable infrastructure of the round:
- **Lemma L* certified** (single-aux strengthened dual of L(n)): 3-case rank
  analysis, correctly stated as a corollary of L(n) (only r=1 case uses L(n)).
  I re-derived Case 2's identity and the bound; verified gap=0 for n=1,2,3.
  Importable.
- **Mirror certificate certified** (n=1..5): symmetry-based equivalent of the
  pair-pile. Importable.
- **L(n+1) k=0 sub-case PROVED** (trivial, no induction).
- **L(n+1) k=1 sub-case PROVED** (reduces to L*(n)): the reduction is clean —
  `m_1 ≥ M/2 = R_largest` (unrefined), so `m_1` is global rank 1;
  `global_oddsum = m_1 + evensum({m_2}∪R') ≥ m_1 + m_2 = M` by L*(n). I verified
  the scaling (`w = m_2·D(n+1)/D(n) ≤ R_largest = 2^n/D(n)`) and the reduction.

**Flaws found (adversarial):**

1. **L(n+1) k≥2 sub-case — OPEN, honestly flagged.** The multi-aux L*
   generalization is FALSE (verified counterexample `W=(1/9,4/9,1/9)` over
   D=9, `R'={2/3,1/3}`, `evensum=5/9 < 6/9=ΣW`). The per-round peeling (D1) is
   blocked by the ΔA −2T tail-flip locally. The WLOG-k=1 exchange (D2) is
   unverified — and the n=3 brute force (7 k=1 extremals, 21 k=2, 12 k=3) shows
   the literal monotonicity "splitting M further only helps Liu" is FALSE.
   This blocks L(n) for n≥3. Honest gap.

2. **Lemma U regime-N — OPEN, delegated to sibling.** The builder correctly
   retires the Hall-matching route (dead since round 1) and records the
   two-regime split with regime-D (dyadic) closed (pair-pile/mirror) and
   regime-N delegated to `two-regime-disjunctive`. The dependency is honestly
   tracked; no false claim.

3. **L* Case 2 "no induction used" — correct but subtle.** The bound
   `w ≤ evensum(R') + A_tail ≥ s_2 ≥ w` uses only sortedness (no IH). I verified
   `w ≤ s_{r−1} ≤ s_2` for r≥3 odd. Correct. Case 3 (r=1) correctly invokes
   L(n) via `oddsum(R') ≥ R_largest ≥ w`. The induction chain
   `L(n) ⟹ L*(n) ⟹ L(n+1)[k≤1]` is sound for the k≤1 sub-cases. ✓

**Verdict: CHANGES REQUESTED.** Real, reusable progress (L*, mirror, k=0/k=1
sub-cases). The k≥2 sub-case of Lemma L and the regime-N of Lemma U are the
open gaps. Route the builder next round to attack k≥2 via the per-round peeling
with a controlled global-sort interleaving argument (the M⊎R decomposition
sidesteps local cuts; the peeling needs to preserve that global structure).

---

## `induct-one-mark` — verdict: CHANGES REQUESTED (Status: partial, bordering RETHINK)

**Honest but weak progress.** The approach's central strategy — the round-level
value-recursion identity `1/V(n+1) = 1 + 1/(2V(n))` (Mersenne form
`B(n+1) = 2B(n)+1`) as an INDEPENDENT value-level induction — is **conceded by
the builder to be a REPHRASING of (Lemma L + Lemma U), not a bypass**. The
builder explicitly flags "no potential accounting for the `+1` interleaving
correction is identified" and "the value-recursion route is, on the current
evidence, a REPHRASING ... not an independent bypass." This is an honest and
correct assessment: the identity is a CONSEQUENT of the conjectured closed
form (verified algebraically for n=1..5), not a game-theoretic lemma that
closes a step.

**Correct contributions (real but largely duplicated from siblings):**
- k=0 sub-case of L(n+1) — same as pairing-partner.
- k=1 reduction to L*(n) — same as pairing-partner.
- Algebraic Mersenne identity — verified, but consequent, not proof.
- Grid cross-checks (n=2 denom 168, n=3 denom 120) — computational, not proof.

**Flaws found (adversarial):**

1. **Central strategy conceded dead.** The value-recursion route cannot work
   as an independent proof (builder's honest assessment, which I confirm: the
   `+1` term is the same interleaving obstruction as Lemma L's k≥2 sub-case,
   and no potential absorbs it). The approach AS A RIVAL SOLUTION is dead — it
   packages (L+U) into one algebraic statement but proves neither.

2. **No independent progress on either main gap.** Both Lemma L general-n and
   Lemma U general-n are delegated to siblings. The approach's own
   contributions (k=0, k=1) are duplicated; the identity is a consequent.

3. **Dispatch error corrected.** The builder correctly refused the dispatch's
   wrong recursion `V(n+1) = (1+V(n))/2` (predicts V(2)=5/6, false; verified
   V(2)=4/7) and used the correct Mersenne form. Good catch.

**Verdict: CHANGES REQUESTED (partial).** The approach has correct pieces
(k=0, k=1, identity, cross-checks) but its central strategy is a conceded dead
end. The approach is bordering RETHINK: as a rival solution it cannot work via
the value-recursion route. The outliner should either retire this approach
(letting pairing-partner and two-regime-disjunctive carry the work) or
re-conceive it on a genuinely different strategy. The correct sub-results are
reusable but belong to siblings. Outcome: `partial` (main route dead, correct
pieces shared).

---

## Lemma certifications (round 2)

**CERTIFIED (admitted to `results/imo-2026-03/lemmas/`):**

1. **Lemma L* (single-aux strengthened dual of L(n))** —
   `lemmas/lemma-L-star-single-aux.md`. 3-case rank analysis rigorous; Case 2
   identity and bound re-derived; Case 3 correctly invokes L(n). Verified
   gap=0 for n=1,2,3 (exact enumeration). Correctly stated as a corollary of
   L(n). Status header added. Importable.

2. **Mirror certificate (dyadic cap via point-reflection)** —
   `lemmas/lemma-mirror-dyadic-cap.md`. Collision, symmetry, central-piece,
   and excess arguments rigorous. Verified n=1..5. Uses n marks (≤ n budget).
   Status header added. Importable.

3. **Lemma U(2) (four-strategy upper bound, equality iff dyadic)** —
   `lemmas/lemma-u2-four-strategy.md` (NEW, written by reviewer from the
   approach's Section 4). Four formulas verified; 4-way contradiction verified
   (N=84 grid, 0 violations, unique equality at dyadic). Minor Strategy-A
   edge case at `c=b` noted (covered by Strategy C). Status: CERTIFIED.
   Importable.

**Rejected:** none this round. (Lemma G, pair-pile, ΔA — round-1 certified,
unchanged.)

---

## Recorded outcomes (mcp__approach-ranker__record_outcome)

- `two-regime-disjunctive` — round 2, `advanced`. Note: "Closes U(2) via
  four-strategy family (verified: 0 violations on N=84 grid, equality iff
  dyadic); gives c(2)=4/7 end-to-end with L(2). U(1) corrected. Regime D all n
  via pair-pile. General-n regime-N upper bound (n≥3) OPEN."
- `pairing-partner` — round 2, `advanced`. Note: "Closes L(n+1) k=0/k=1
  sub-cases; certifies Lemma L* and mirror. k≥2 sub-case of Lemma L OPEN
  (multi-aux FALSE); regime-N of Lemma U delegated. L*, mirror importable."
- `induct-one-mark` — round 2, `partial`. Note: "Value-recursion route
  conceded as REPHRASING of (L+U), not a bypass — central strategy dead.
  k=0/k=1 sub-cases duplicate pairing-partner. Both main gaps delegated."

## Goal Progress

**Status: partial.** Headline progress this round: **`c(2) = 4/7` rigorously
established end-to-end** (both bounds). The upper bound U(2) is closed by a
new four-strategy family (4-way contradiction, equality iff dyadic, verified);
the lower bound L(2) was round-1 certified. Two new reusable lemmas (L*,
mirror) and one new result-lemma (U(2)) certified into the shared cache. The
L(n+1) lower-bound spine is closed for the k=0 and k=1 sub-cases via the
M⊎R decomposition + L* (the Xiang-side dual). The n=1 two-mode base is
corrected (dyadic/non-dyadic boundary).

**Concrete remaining gaps for round 3 (raw, not paraphrased):**

1. **Lemma L general-n, k≥2 sub-case.** When ≥2 Xiang marks land in the
   largest dyadic piece `M = 2^{n+1}/D(n+1)`, `M` is split into ≥3 sub-pieces
   `m_1 ≥ m_2 ≥ … ≥ m_{k+1}`; `m_1 ≥ M/(k+1) ≤ M/3 < M/2 = R`'s largest
   (unrefined) piece, so `m_1` need NOT be global rank 1, and the global
   descending sort INTERLEAVES M-sub-pieces with R'-pieces in a way the k≤1
   reductions do not control. The multi-aux generalization of L* is FALSE
   (counterexample `W=(1/9,4/9,1/9)` over D=9, `R'={2/3,1/3}`,
   `evensum=5/9 < 6/9=ΣW`). The per-round peeling (peel one mark from M AND one
   from R per round, matching `1/f(n+1)=1+1/(2f(n))`) is blocked locally by
   the ΔA `−2T` tail-flip. The WLOG-k=1 exchange is unverified and the n=3
   brute force (7/21/12 extremals at k=1/2/3) shows literal monotonicity is
   FALSE. This blocks `c(n) ≥ f(n)` for n≥3.

2. **Lemma U general-n, regime-N mechanism (n≥3, non-dyadic Liu configs).**
   Prove Xiang forces `Liu < f(n)` strictly for every non-dyadic n≥3 Liu
   config via a sliver/shave strategy (NOT the false `A≤0` pairing — non-dyadic
   n=2 configs cap above 1/2). The n=2 four-strategy proof (a 4-way
   contradiction in 3 variables with equality iff dyadic) does NOT lift: each
   strategy (A, B, C, E) is n=2-specific (consumes 2 marks in a particular
   pattern), and the (2^n−1)-way generalization in (n+1) variables has no
   clean contradiction argument. Numerical evidence (n=3 sub-grid: dyadic gives
   exactly 8/15; every tested non-dyadic n=3 config strictly less, e.g.
   `(1/4,1/4,1/4,1/4) → 0.514 < 8/15≈0.533`) supports the conjecture but is
   NOT a proof. This blocks `c(n) ≤ f(n)` for n≥3 (regime D / dyadic is closed
   for all n via the pair-pile/mirror; regime N is the open half).

3. **`induct-one-mark` route is dead.** The value-recursion
   `1/V(n+1)=1+1/(2V(n))` is a verified algebraic consequent of the closed
   form, NOT an independent game-theoretic induction (no potential for the `+1`
   interleaving correction is identified). The outliner should either retire
   this approach or re-conceive it on a genuinely different strategy; the
   correct sub-results (k=0, k=1) are carried by `pairing-partner`.
