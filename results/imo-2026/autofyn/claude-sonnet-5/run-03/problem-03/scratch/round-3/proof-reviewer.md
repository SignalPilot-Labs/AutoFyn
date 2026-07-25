# Round 3 proof-reviewer report — imo-2026-03

Problem: for each n, determine c(n), the largest length Liu Bang can
guarantee in the two-phase stick-cutting alternating-claim game. Certified
reduction (all rounds): c(n) = max over LB partitions p (k<=n+1 pieces) of
min over XY refinements (<=n cuts) of OddSum(final multiset). Conjectured
closed form c(n) = 2^n/(2^{n+1}-1), proved for n=0,1. Four approaches built
this round; each reviewed independently below. Every new quantitative claim
was independently re-derived (exact algebra) and/or numerically stress-tested
with fresh scripts (not the builders' scripts) before being accepted.

---

## 1. self-similar-induction-on-n — Verdict: CHANGES REQUESTED (Status: partial, correctly self-reported)

**Claims checked:**

- **Lemma Z (z-trick identity).** EvenSum(X) = OddSum({z}∪X) − z for z ≥
  max(X). Elementary two-line consequence of the certified Global-max
  Peeling Lemma. Re-derived from scratch — correct, no gap.

- **Theorem 1 (T(2) fully closed).** New content is the j=2 sub-case (top
  piece "4" split into three fragments a1≥a2≥a3, tail {2,1} untouched),
  claiming OddSum≥4 always, via two closed-form identities: OddSum =
  5 − median(a2,a3,1) when a1>2, and OddSum = 7 − (n1+n3) when a1≤2. I
  independently re-verified:
  - The min-value claim: 500,000 random splits of 4 into 3 positive parts,
    minimum OddSum observed 4.0000 (approached, not beaten) — matches.
  - The two closed-form identities exactly: 200,000 random trials, **zero
    mismatches** against direct sorted-sum computation.
  - The casework bounding median(a2,a3,1)≤1 and n1+n3≤3 is exhaustive
    (each splits into exactly two sub-cases covering all of (0,∞) for the
    relevant variable) — no gap found.
  This theorem is **correct and rigorously proved**, genuinely closing T(2)
  in full generality (previously only T(1) was closed).

- **Proposition C (Case-A circularity).** Claims U(m,k) (an upper bound
  needed to complete Case A of the peeling induction) is, via Lemma Z,
  algebraically equivalent to an instance of the generalized target
  G(m,k;V'') with the *same* fragment count as the state before peeling
  (i.e., peeling the top fragment and then trying to bound the residual
  makes no net progress). I re-derived the full algebraic chain manually
  with a concrete example (m=3, B={5,2,1}, S={4,2,1}: OddSum(B∪S)=8,
  EvenSum(B'∪S)=3 via peeling = matches direct computation; the z-trick
  substitution EvenSum(B'∪S)=OddSum({4}∪B'∪S)−4=7−4=3, matches exactly),
  then ran a randomized check of the general equivalence (U(m,k)'s
  inequality ⟺ the substituted OddSum inequality) — my first attempt at
  this check used an arbitrary tail S not respecting sum(S)=2^m−1 (the
  actual constraint from S being a genuine Γ_{m-1}-refinement) and
  produced many "mismatches"; after correcting the harness to enforce
  sum(S)=2^m−1 (as the proof's own algebra requires — it uses
  sum(B'∪S)=(V'+2^m−1)), the equivalence held in **16,681/16,681** random
  trials with zero mismatches. **This is a correct, non-circular-in-itself
  proof of a genuine circularity in the peeling method** — a real,
  proven obstruction, not merely a diagnosis.

**Status assessment.** All new claims check out. Status `partial` is
accurate — T(2) is now fully closed (real, certified progress), but T(m)
for m≥3 remains open, and Proposition C shows precisely why the natural
continuation of the current method cannot close it without tracking
additional structure. No overclaim. **Verdict: CHANGES REQUESTED** — real
progress, technique is sound, gap (T(m), m≥3) remains and is now more
sharply characterized than before.

---

## 2. greedy-reduction-geometric — Verdict: CHANGES REQUESTED (Status: partial, correctly self-reported)

**Claims checked:**

- **Theorem 5 (Dominant-Chain Theorem).** Strong induction on k: if a
  descending sequence a1≥...≥ak (sum ≤2^m) has the recursively-defined
  Dominance-Chain property (a1≥2^{m-1}, tail has the property at level
  m-1), then OddSum({a_i}∪Γ_{m-1}) ≥ Σa_i. I re-derived the induction step
  algebraically (two applications of peeling — Global-max Peeling then the
  new Companion Peeling Lemma — chained with the IH) and it is airtight:
  each step's "current max" claim (a1 = max, then 2^{m-1} = max of the
  residual) is correctly justified from the arithmetic bounds S'≤2^{m-1}.
  I additionally ran 8,808 random Dominance-Chain-satisfying instances
  (m≤5, k≤4) through a fresh independent OddSum computation: **zero
  violations**. Correct and rigorous; a genuine strict generalization of
  the original Case-1 result (verified: it reduces to Case 1 exactly when
  k=0, i.e., j=0).

- **Lemma 5 (Companion Peeling Lemma)** and **Lemma 6 (Prefix-Run Peeling
  Decomposition Lemma).** Both re-derived from scratch: Lemma 5 is a
  one-line consequence of Global-max Peeling + the sum decomposition —
  correct. Lemma 6's parity-of-d case split was independently verified
  over 20,000 random instances (m≤6, arbitrary d, arbitrary fragment
  count/values respecting the a1<2^{m-d} hypothesis): **zero mismatches**
  to $10^{-9}$. Correct.

- **Second dead-end (tail-priority strategy).** Claims a static
  "tail-priority" LB strategy gives only a floor of 7 (< target 8) at
  n=3, tail {4,2,1}, fragments {3.9,3.9,0.2} (a Dominance-Chain-violating
  split), while the true optimal (greedy) value is 8.9. I wrote an
  **independent exact game-tree minimax solver** (full enumeration, no
  reuse of the builder's code) implementing exactly the described
  strategy (LB clears the known tail first, else claims the pool max) and
  reproduced **7 exactly** as the guaranteed floor, and separately
  confirmed the true optimal (both-sides-optimal) value is **8.9**
  exactly via direct OddSum computation. The counterexample is fully
  verified and rules out this strategy family as claimed.

**Status assessment.** All new claims verified. The Dominant-Chain Theorem
is a genuinely stronger positive result than round 2's content, the two
peeling lemmas are correct general tools, and the tail-priority dead end is
a real, independently-confirmed negative result extending the existing
catalog. TOP-ONLY is closed only within the Dominance-Chain regime; the
complementary regime and the fully general Case 2 remain open, honestly
reported. No overclaim. **Verdict: CHANGES REQUESTED** — real progress
(a strictly stronger sub-case closed + a rigorous new negative result),
gap remains.

---

## 3. universal-halving-adversary — Verdict: CHANGES REQUESTED (Status: partial, correctly self-reported)

**Claims checked (dispatch specifically flagged Theorem 3 as claimed to
"fully close the k≤n regime" — verified in detail):**

- **Theorem 1 (Doubling Lemma, imported/reused).** OddSum(R∪R)=sum(R).
  Re-verified over 20,000 random trials (including forced ties/repeated
  values), zero mismatches.

- **Theorem 3 (Perfect-Pairing/Bisect-Everything Corollary).** For any LB
  partition with k≤n pieces, bisecting every piece gives OddSum=1/2
  exactly, hence ≤c(n) since c(n)>1/2 for all n. This is a one-line
  consequence of the Doubling Lemma (M = R∪R with R = the bisected
  halves). I independently confirmed c(n) = 2^n/(2^{n+1}-1) > 1/2 exactly
  by rational arithmetic for n=1..7 (equivalent to 2·2^n > 2^{n+1}-1,
  i.e. 2^{n+1} > 2^{n+1}-1, trivially true — I confirm this holds for
  **every** n≥0, not just the checked range, since it's an immediate
  algebraic identity). **Confirmed correct and complete** — this does
  fully close the entire slack-budget regime k≤n, unconditionally, for
  every n and every such partition, exactly as claimed. No gap.

- **Lemma S (Subadditivity of OddSum).** OddSum(A∪B) ≤ OddSum(A)+OddSum(B)
  unconditionally, no domination hypothesis. Re-derived the induction
  (removal identity g(X)=f(X\{max X}), applied to both A∪B and A when
  max is WLOG in A) — correct, and structurally distinct from the
  previously-disproven Lemma X′ (that was a conditional threshold claim;
  this is unconditional). Independently verified over 50,000 random
  trials: **zero violations** (max observed lhs−rhs ≈ 1.8×10⁻¹⁵, pure
  float noise).

- **Theorem 4 (General Insertion Lemma).** OddSum(R∪R∪{ℓ}) = sum(R)+ℓ for
  **any** ℓ>0, no relation to R required — strictly generalizes the
  previous ℓ=p1−S≥0 identity. The proof reuses Theorem 2's case-(a)/(b)
  block-counting argument, re-examined to confirm it never actually used
  an ordering hypothesis on ℓ. I independently verified this over 50,000
  random trials with ℓ **unconstrained** relative to R (including ℓ above
  max(R) and below min(R)): **zero violations**. Confirmed correct — the
  claimed strengthening is real, not overclaimed.

- **Theorem 5 (conditional reduction, p1≥c(n) given T(n-1)).** Explicitly
  and correctly flagged as *conditional*, not a standalone closure. Key
  identity φ(c(n))=c(n) where φ(p1)=p1/2+(1−p1)c(n−1): I verified this
  **exactly by rational arithmetic** for n=1..7 (the algebra
  c(n−1)(1−c(n))+c(n)/2 = c(n) reduces via exact fraction cancellation to
  2·2^{n-1}/(2^{n+1}-1) = 2^n/(2^{n+1}-1), confirmed identically). The
  slope 1/2−c(n−1) is negative since c(n−1)>1/2 (same fact as above).
  Correct, and honestly labeled conditional throughout the file (Status
  line and body both say "conditional," not overclaimed as unconditional).

**Status assessment.** Every new claim this round checks out, including
the headline Theorem 3 the dispatch flagged for special scrutiny — it does
fully and correctly close the k≤n regime as claimed, with no gap. Lemma S
and Theorem 4 are genuinely new, general, correct tools. Theorem 5 is
correctly and honestly presented as conditional. The remaining open gap
(p1<1/2 and p_{n+1}>1/(2^{n+1}-1), the balanced/near-uniform regime) is
real and precisely stated; no attempt to paper over it. **Verdict: CHANGES
REQUESTED** — substantial real progress (an entire regime, k≤n, closed
unconditionally for the first time; two new general-purpose lemmas),
Status `partial` accurately reflects the state (not `solved`).

---

## 4. dyadic-potential-invariant — Verdict: CHANGES REQUESTED (Status: partial, correctly self-reported; net effect is a documented dead end)

**Claims checked:**

- **Disproof of the literal Cut-Reallocation Exchange Lemma.** At n=3,
  Γ_3=(8,4,2,1): configuration M (cuts on pieces "2" and "1") has min
  OddSum=9.5 (a=b=1, c=d=0.5); configuration M' (moving the cut from
  piece "2" to piece "4", per the literal exchange rule) has infimum
  OddSum=10 (not attained, approached as fragments→0), strictly worse for
  XY. I **independently re-implemented** both optimizations from scratch
  (random search over the free parameters, 200,000 samples each) and
  reproduced: M min ≈ 9.503 (converging to 9.5 as fragments equalize
  exactly), M' min ≈ 10.002 (converging to 10 as fragments shrink toward
  the degenerate zero-cut limit). This **exactly matches** the claimed
  counterexample. The literal Exchange Lemma is genuinely false; this is
  a real, correctly-verified negative result.

- **The weaker "top-only-dominates" aggregate claim (unproven).** I
  independently spot-checked this at n=2, budgets b=1,2 (exhaustive over
  all cut-count compositions among the 3 pieces {4,2,1}, random-restart
  search per composition): in both cases the top-only allocation's
  minimum matched the global minimum over all compositions exactly. This
  is consistent with (does not contradict) the builder's own more
  extensive exhaustive-for-small-n claim (n=2,3,4, all budgets), but
  remains **unproven** — correctly reported as conjecture, not fact, in
  the file's Status/Full-proof sections.

**Status assessment.** This file establishes a genuine negative result
(rules out an entire proof-mechanism family) but closes **no** gap toward
the target theorem — it is honestly `partial` with an accurate
self-assessment ("no promotable lemmas... this disproves rather than
establishes a fact"). Per the standing rule that documented dead ends are
valuable population-pruning progress, I record this as outcome `dead-end`
in the ranker (not `advanced`, since — unlike the other three files — no
positive lemma or sub-case was closed this round, only a negative result
plus unproven conjecture). **Verdict: CHANGES REQUESTED** — Status
`partial` is correct; the file should not be promoted to a stronger claim,
and the next round should not re-attempt the "always move a cut toward the
top" mechanism.

---

## Certification actions taken

Certified into `results/imo-2026-03/lemmas/` (all independently
re-verified above):
- `perfect-pairing-subadditivity-and-general-insertion.md` — Theorem 3
  (Perfect-Pairing Corollary), Lemma S (Subadditivity), Theorem 4 (General
  Insertion Lemma). Replaces/renames the round-3
  `CANDIDATE-perfect-pairing-and-subadditivity.md` file (deleted after
  content moved into the certified file).
- `dominant-chain-theorem-and-prefix-run-decomposition.md` — Companion
  Peeling Lemma, Dominant-Chain Theorem (Theorem 5), Prefix-Run Peeling
  Decomposition Lemma (Lemma 6), from `greedy-reduction-geometric`.
- `z-trick-identity-and-T2-closed.md` — Lemma Z and Theorem 1 (T(2) fully
  closed), from `self-similar-induction-on-n`. Proposition C's
  mathematical content is verified correct but recorded as a documented
  obstruction within this file (and in `current.md`), not certified as a
  separate reusable positive lemma, consistent with how prior rounds
  handled negative/obstruction results (e.g. Q-priority, tail-priority
  dead ends were not given standalone `lemmas/` files either).
- `conditional-top-dominant-reduction.md` — Theorem 5 (conditional
  reduction), from `universal-halving-adversary`, clearly marked
  conditional so future rounds cite it correctly (only usable once T(n-1)
  is closed in full).

Not certified: dyadic-potential-invariant's counterexample (a disproof,
not a reusable positive fact — already recorded in `current.md`'s
"documented dead ends" list; no separate `lemmas/` file needed per the
builder's own note and consistent with prior-round practice for negative
results).

`current.md` updated: Status remains `partial`; Approaches tried and
Current best sections rewritten to reflect this round's four verified
outcomes (three genuine advances narrowing both the lower-bound and
upper-bound gaps, one genuine negative result/dead end); no Full proof
section added (problem not solved).

## Ranker outcomes recorded
- `self-similar-induction-on-n`: `advanced` — T(2) fully closed, Lemma Z,
  proven (not just diagnosed) Case-A circularity.
- `greedy-reduction-geometric`: `advanced` — Dominant-Chain Theorem
  (strict generalization of Case 1), two new peeling lemmas, second
  independently-confirmed static-strategy dead end.
- `universal-halving-adversary`: `advanced` — entire k≤n regime closed
  unconditionally (Theorem 3), two new general lemmas (Subadditivity,
  General Insertion), conditional reduction narrowing the open gap to one
  region.
- `dyadic-potential-invariant`: `dead-end` — confirmed disproof of the
  proposed mechanism; no positive gap closed; weaker claim remains
  unproven.

## Overall round assessment

No approach reached `solved`; the population made genuine, independently
verified progress on both the lower-bound gap (T(2) closed, Dominant-Chain
regime closed, the obstruction to going further now *proved* rather than
merely diagnosed, and cross-confirmed by two independent approaches from
different framings) and the upper-bound gap (an entire regime, k≤n, closed
unconditionally; the open region narrowed from a blanket "p1<1/2" to a
single precisely-characterized "balanced/near-uniform" strip, at every
level of the induction). No overclaiming was found in any of the four
files — every builder correctly self-reported `partial` (or an honest
negative result) and none of my adversarial checks (exact game-tree
minimax reproduction, large-scale random-trial verification, and manual
algebraic re-derivation of every load-bearing identity) turned up a
false claim.
