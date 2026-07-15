## imo-2026-01

Round 1, fresh workspace — the field is three new rival approaches, each a complete attempt at BOTH parts (a) and (b). All explorer reports agree on the terrain: a move acts per prime as the subtractive-Euclid step (a,b) → (min(a,b), |a−b|); g_p = gcd of the exponent multiset is exactly invariant; W = (#entries>1) + ΣΩ is a strict monovariant; M = ∏_p p^{g_p} (computationally confirmed on thousands of plays). Traps flagged and baked into the skeletons: Σxᵢ is NOT monotone; Σ_p-exponents is only monotone, not invariant; legality (m,n > 1) is a single GLOBAL condition, so no per-prime move is ever "applied" — every skeleton states this; part (a) demands EXACTLY one (N never reaches 0 because a move never outputs two 1s: gcd = 1 ⇒ other output mn ≥ 4; gcd > 1 ⇒ gcd output > 1; the m = n case gives (m,1)).

Cheap kill considered and adopted: this problem IS the cheap kill — a two-line Euclid identity plus a monovariant; no heavy machinery was rejected because none is needed. The field's job is to hedge the packaging, not the difficulty.

---

prime-gcd-invariant: new
File: results/imo-2026-01/approaches/prime-gcd-invariant.md
Target: full problem — (a) every play terminates with exactly one entry M > 1; (b) M is play-independent (with closed form M = ∏_p p^{g_p}).
Technique: invariants & monovariants + p-adic valuation (knowledge_base: "Invariants & monovariants", "Divisor analysis / gcd structure"); direct proof with three-case move analysis.
Skeleton:
  1. Move anatomy: v_p(gcd) = min(a,b), v_p(lcm/gcd) = |a−b| — by valuation formulas / unique factorization.
  2. Lemma A: no move outputs two 1s — by the gcd = 1 / gcd > 1 case split (incl. m = n).
  3. Termination: W = N + ΣΩ strictly drops in all three move cases (ΔΣΩ = −Ω(gcd)) — by casework; W a non-negative integer.
  4. Exactly one: N starts at 2026, drops by ≤ 1, never 2 → 0 (Lemma A), stuck ⇔ N ≤ 1, hence terminal N = 1 — part (a).
  5. Invariant: g_p = gcd of the 2026 p-exponents is move-invariant — by gcd(a,b) = gcd(min(a,b), |a−b|) (subtractive Euclid) + gcd associativity.
  6. Read-off: terminal exponents {v_p(M), 0,…,0} give v_p(M) = g_p, so M = ∏_p p^{g_p} — part (b).
Key lemmas (claim + mechanism):
  - gcd(a,b) = gcd(min(a,b), |a−b|) for a,b ≥ 0 — because d | a,b ⇔ d | min(a,b), a−b (WLOG a ≥ b), with zero cases gcd(a,0) = a, gcd(0,0) = 0.
  - ΔΣΩ = −Ω(gcd(m,n)) per move — because Σ_p [min + |a−b|] = Σ_p max and (a+b) − max = min.
  - No move outputs two 1s — because gcd·(lcm/gcd) = lcm ≥ max(m,n) ≥ 2, so at least one output ≥ 2, refined by the case split.
  - lcm/gcd = 1 ⇔ m = n — because lcm = gcd ⇔ m = n.
Open gaps: all six steps need full rigorous write-up (listed in the file); nothing conceptually open.
Cases to cover: move cases m = n / coprime / gcd > 1 & m ≠ n; exponent cases a = b, b = 0.
Watch out for: gcd-with-0 conventions must be stated; "exactly one" needs both N ≥ 1 and stuck ⇔ N ≤ 1; never phrase the invariance as a per-prime move.

star-monoid-product-descent: new
File: results/imo-2026-01/approaches/star-monoid-product-descent.md
Target: full problem — (a) and (b), same closed form.
Technique: invariant packaged as a commutative-monoid fold Φ under m ⋆ n = ∏_p p^{gcd(v_p m, v_p n)}; termination by lex descent of (∏ entries, N). Same Euclid core as prime-gcd-invariant (acknowledged) but different termination engine, different exactly-one argument, and lighter bookkeeping — a hedge against write-up failure modes (multiset-gcd conventions, W casework), not against the identity itself.
Skeleton:
  1. (ℤ≥1, ⋆, 1) is a commutative monoid — because exponentwise gcd is commutative/associative and gcd(0,k) = k gives identity 1.
  2. Lemma S: m ⋆ n = gcd(m,n) ⋆ (lcm/gcd) — by the same subtractive-Euclid identity per prime.
  3. Φ(board) = ⋆-fold is move-invariant — by monoid algebra + Lemma S.
  4. Φ(initial) ≥ 2 — because any prime p | x₁ contributes folded exponent ≥ 1 (gcd of nonneg integers, one positive).
  5. Termination: a move multiplies P = ∏ entries by 1/gcd(m,n); gcd > 1 ⇒ P drops by factor ≥ 2; gcd = 1 ⇒ P fixed, N drops by 1; lex (P, N) strictly decreases, well-founded.
  6. Terminal N = 1: N = 0 would give Φ = 1, contradicting step 4 — part (a). Then M = Φ(terminal) = Φ(initial) — part (b).
Key lemmas: Lemma S (Euclid identity per prime); gcd·lcm = mn (so the P-factor is 1/gcd); Φ ≥ 2 forever.
Open gaps: monoid axioms, Lemma S zero cases, fold bookkeeping, lex well-foundedness — all mechanical.
Cases to cover: gcd = 1 vs gcd > 1 (m = n sits inside gcd > 1); a = b, b = 0 in Lemma S.
Watch out for: P alone is not strict — the lex pair is load-bearing; do not use Σxᵢ.

newman-confluence: new
File: results/imo-2026-01/approaches/newman-confluence.md
Target: full problem — (a) via monovariant, (b) via unique normal form (no closed form for M, which the problem doesn't require).
Technique: abstract rewriting — termination + LOCAL confluence ⇒ confluence ⇒ unique normal form (Newman's lemma, proved from scratch by well-founded induction on W). Adapts the aimo-0003 crux ("reduce order-invariance to local swap checks"). Genuinely independent of the g_p invariant: the only route in the field that survives if the invariant line hides a flaw.
Skeleton:
  1. Termination via W (shared engine) — casework.
  2. Reachable normal forms have exactly one entry > 1 — Lemma A + N-walk — part (a).
  3. Disjoint moves commute — bookkeeping.
  4. Overlapping moves (shared entry m among m,n,r) are joinable — THE hard lemma; non-circular plan: either explicit bounded joining schedules verified by per-prime gcd/min/|·| identities on triples, or a standalone 3-entry unique-terminal lemma proved first by its own induction. Legality (intermediate 1s cannot be moved) must be handled.
  5. Newman's lemma by well-founded induction on W ⇒ unique normal form {M,1,…,1} — part (b).
Key lemmas: overlapping joinability (mechanism candidate: both reducts reach the sub-board terminal {M₃,1,1}, with the 3-entry uniqueness proved independently first); Newman induction.
Open gaps: Step 4 is a major open gap and the approach's kill-risk; rest mechanical.
Cases to cover: disjoint vs overlapping pairs; gcd patterns among (m,n,r); intermediate entries = 1.
Watch out for: circularity in Step 4; legality of every join move; Newman needs termination first.

---

Field notes for the reviewer:
- Single-line-trap audit: prime-gcd-invariant and star-monoid-product-descent share the Euclid identity gcd(a,b) = gcd(min(a,b), |a−b|) (two-line classical fact, risk accepted and disclosed); newman-confluence does not depend on it for part (b), so the field is not single-lined.
- Recommended build set this round: **prime-gcd-invariant, star-monoid-product-descent** — both are near-complete and one should reach APPROVE quickly; the problem is rated medium. Add **newman-confluence** only if builder capacity allows (its Step 4 is real work and it is the diversity hedge, worth keeping live rather than building first).

build set: prime-gcd-invariant, star-monoid-product-descent
