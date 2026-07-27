# Proof-reviewer — Round 2 — IMO 2026 P6 (`imo-2026-06`)

Reviewed both built approaches. Recomputed every load-bearing computational claim (mtp monotonicity, gap bound, common ⊆ P(a1), a1=175 mtp=21 with prime 3 entering, a1=273 regime-(F) freeze, a1=175 self-blocking family) on the 8 builder seeds plus adversarial seeds {105,231,385,1001,187,221}. All hold.

## α `density-promotion-bound` — verdict: CHANGES REQUESTED (Status: partial)

The freeze branch (F) is genuinely CLOSED end-to-end. I verified each load-bearing step:

- **`freeze-lock` (Lemma 3) — CORRECT, airtight.** The forward direction "p∈C_{n+1} ⟹ a_{n+1}=a_n+p" (under p|a_n, p∈C_n) is proved cleanly: {p} is a transversal so a_{n+1}≤a_n+p; if strict, then p∤a_{n+1}, and P(a_{n+1}) is a new minimal — I checked the new-minimal argument handles every subcase, including the tricky P(a_{n+1})=P(a_j) (j≤n) case: then P(a_{n+1})∈M_n (no proper subset exists by the bullet argument), which contains p (p∈C_n), contradicting p∉P(a_{n+1}). Solid. The contrapositive "gap<p ⟹ p∉C_{n+1}" follows correctly.

- **Lemma 2 (common primes ⊆ P(a1)) — CORRECT, verified on all 14 seeds.** The proof (pick minimal M_1⊆P(a_1); q∈C_n ⟹ q∈M_1⊆P(a1)) is valid. This pins the case split on P(a1) alone and rules out promoted primes becoming common. Confirmed computationally: common stayed ⊆ P(a1) in every seed.

- **Lemma 4 (AP, induction) — CORRECT.** Uses only the forward direction of freeze-lock + regime-(F) hypothesis (p∈C_n ∀n). Induction base and step both check: p|a_n maintained, p∈C_{n+1} supplied by regime (F), freeze-lock supplies the lock.

- **Lemma 5 (AP hits p^k) — CORRECT.** n=p^{k-1}−c+1 with k minimal s.t. p^{k-1}≥c gives a_n=p^k. (Minor: k≥1 suffices, not k≥2 as stated; irrelevant — P(p^k)={p} either way.)

- **Lemma 6 (singleton freeze) — CORRECT.** Regime (F) gives p∈C_{n-1}, so every M∈M_{n-1} contains p, so {p} dominates all existing minimals; M_n={{p}}; singleton-freeze freezes. (Edge n=1 with a_1=p^k is handled trivially by singleton-freeze directly — M_0 reference is vacuous there; acceptable.)

- **Branch (F) end-to-end: closed.** Computationally confirmed non-trivial: a1=273=3·7·13 is regime (F) — prime 3 persists common, ALL gaps are exactly 3 (verified: gap distribution Counter({3:2000})), the AP 3·90,3·91,… hits 3^6=729 at n≈154, singleton-freeze gives M={{3}}, L=3, T=1. So the freeze branch is a meaningful advance, not just the trivial even/prime-power collapses.

- **Case split (F)/(S) — EXHAUSTIVE.** Excluded middle on "∃p∈P(a1) persisting common"; Lemma 2 ensures (S) means no prime at all persists common.

- **Branch (S): honestly open (GAP-S).** Lemma 7 (Sat-criterion: self-blocking ⟹ frozen) is CORRECT — clean induction, no gap. Lemma 8 (mtp density ≥1/mtp, correlation-surviving) is CORRECT (single-transversal bound, no independence assumption). GAP-S (reaching self-blocking / finiteness in saturated regime) is honestly flagged open with the correct obstruction (free-rider quotient unbounded). Verified a1=175 reaches a self-blocking family |M|=5 with mtp-witness {3,7} being itself a member.

**Gaps / issues found:**
1. **Overclaim in `freeze-lock.md` remarks (non-load-bearing).** The remark states "the lock and persistence of p are *equivalent*". Only the forward direction (persistence ⟹ lock) and its contrapositive (lock-broken ⟹ not-persistence) are proved — these are one implication, NOT an equivalence. The backward direction (lock ⟹ persistence, i.e. gap=p ⟹ p∈C_{n+1}) is NOT proved and may be false. This does NOT affect any proof: Lemma 4's induction only uses the forward direction. The formal lemma STATEMENT (just the forward implication) is correct and certifiable; the "equivalence" language in the remark should be struck or qualified. Not a blocking gap.
2. **Minor factual discrepancy (non-load-bearing).** α claims "a1=273 has 47 promotions before freeze"; my simulation counts 57 promotions (frozen at step ~152). The qualitative point (full density ρ≥1/3 yet many promotions — density doesn't control promotions) survives; the number is wrong. Used only as illustration, not in any proof step.
3. **GAP-S genuinely open** — this is the real blocker. The saturated branch is partial by honest admission.

**Promotable lemmas (α):**
- `freeze-lock` — CERTIFY (formal statement correct; flag the remark's "equivalence" overclaim to be struck).
- common-primes-bounded (Lemma 2) — CERTIFY.
- Sat-criterion (Lemma 7) — CERTIFY.
- min-prod-transversal density (Lemma 8) — CERTIFY (note: same content as γ's mtp gap-bound; the density half is the addition here).

**Scores:** Correctness 9/10, Completeness 6/10 (branch S open), Progress 8/10 (freeze branch is a real closed sub-result covering non-trivial regime-(F) seeds like 273).

**Outcome: advanced** — freeze branch closed end-to-end, four correct lemmas; GAP-S remains.

---

## γ `bounded-gap-lcm-reduction` — verdict: CHANGES REQUESTED (Status: partial)

The mtp monovariant is a correct, reusable, unconditional asset. I verified:

- **mtp monotonicity (Lemma 1a) — CORRECT.** The crux "refinement shrinks the transversal family: Trans(M_{n+1})⊆Trans(M_n)" is proved correctly. I checked the logic: every M∈M_n either survives (hit directly) or is removed by the new minimal P(a_{n+1})⊂neq M (hit via P(a_{n+1})⊆M). The only subtlety — that M∉M_{n+1} forces P(a_{n+1})⊂neq M — is valid because at step n+1 exactly one new support is added, so the only possible refiner is P(a_{n+1}). Min over subset ≥ min over superset gives monotonicity. Verified on all 14 seeds (mono=True everywhere).

- **Global gap bound (Lemma 1b) — CORRECT.** Same multiples-of-witness logic as `gap-bound-at-promotion` but at EVERY step (not just promotions) and governed by the global monovariant, independent of a_{i−1}. Verified: gapbound=True on all seeds, and the bound is tight (max gap = stabilized mtp in every case: 15→6, 175→21, 187→22, 221→34, etc.).

- **De-history-ing claim — CORRECT.** `gap-bound-at-promotion` bound depends on a_{i−1}→∞; the mtp bound does not (depends only on M_n). Genuine sharpening.

- **a1=175 mtp=21 with prime 3 entering — VERIFIED.** P(a1)={5,7}; final Mn primes = {2,3,5,7,13}; mtp_final=21=3·7; 3∉P(a1) enters mid-evolution. Refutes the naive mtp≤2·p_max(a1)=14 bound. Correct.

- **GAP-1 (mtp bounded) — honestly open.** The "pigeonhole on small primes" attack is articulated but admits its own circularity (bounding small-prime witnesses requires knowing G, which is the conjectured bound). The builder honestly states the structural "only small primes enter minimals" lemma IS the wall, shared with α's GAP-S. Honest.

- **GAP-3 (bounded gaps ⟹ M finite) — honestly open.** The "unique connector" obstruction is real and correctly diagnosed: a large fresh prime q>G can be the unique connector between a new minimal and an old one, perfectly consistent with gaps ≤G. I verified the logic: q>G and q|a_{n+1} ⟹ q∤a_n (a_n lies strictly between consecutive multiples of q), so q is fresh. The `aimo-0678` lcm-reduction template's load-bearing step "a_n | M" has no exact analogue (the bounded coordinate is the GAP, not a term value; the greedy depends on M_n). The builder correctly identifies that closing GAP-3 requires either M-finite-first (circular) or a "no large unique connector" structural lemma (the wall). Honest.

- **Single-gap-trap risk.** γ and β both ultimately need "only small primes enter minimals" — the shared wall. γ's GAP-1 attack (pigeonhole on small primes) is framed differently from β's permanent-transversal/Bertrand mechanism, but the builder honestly admits both reduce to the same structural lemma. The mtp monovariant itself (proven, unconditional) is genuinely new and reusable independent of how GAP-1 is closed — so γ contributes a real asset even if its wall is shared. The field has NOT collapsed to one framing: α's freeze branch is a different closed route, and γ's contribution is the monovariant machinery, not the wall-attack.

**Gaps / issues found:**
1. **GAP-1 and GAP-3 both genuinely open** — by honest admission, correctly diagnosed. No papering over.
2. No errors in the proved machinery.

**Promotable lemma (γ):**
- `mtp-monovariant-and-gap-bound` — CERTIFY. Statement (monotonicity + global gap bound) correct, unconditional, verified computationally on 14 seeds. Subsumes `gap-bound-at-promotion`. Remarks correctly scoped (does not claim what it doesn't prove).

**Scores:** Correctness 10/10 (all proved claims check out), Completeness 4/10 (both sub-gaps open, no end-to-end finish), Progress 7/10 (the mtp monovariant is the sharpest unconditional gap control in the field, a reusable asset imported by α/β/δ).

**Outcome: advanced** — proven monovariant + global gap bound; GAP-1 and GAP-3 remain.

---

## Cross-approach notes

- α's freeze branch and γ's mtp monovariant are both genuine advances this round. Neither approach is solved (the saturated wall / GAP-S / GAP-1+GAP-3 — all articulations of "only finitely many primes enter minimals" / "M finite" — remains the single open wall).
- The two new lemmas are both correct and certifiable. `freeze-lock` remark needs a one-line fix (strike "equivalent"). `mtp-monovariant-and-gap-bound` is clean.
- α's Lemma 8 (density) and γ's mtp gap-bound overlap (both use the multiples-of-witness argument); γ's is the stronger global version. No conflict.
- Both approaches honestly mark Status `partial` — no overclaiming.

## Verdicts
- α `density-promotion-bound`: **CHANGES REQUESTED** (partial; freeze branch closed, GAP-S open).
- γ `bounded-gap-lcm-reduction`: **CHANGES REQUESTED** (partial; mtp monovariant proved, GAP-1 + GAP-3 open).
