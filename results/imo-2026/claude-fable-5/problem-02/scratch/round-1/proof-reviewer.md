# Proof review — imo-2026-02, round 1

Reviewed adversarially. All verification artifacts in `/tmp/round-1/review/`
(`check_identities.py`, `check_cert_sym.py`, `check_cert_num.py`, `check_tables.py`,
`check_6b.py`, `endtoend.py`, `check_mri.py`) — all written from scratch by the
reviewer, independent of any builder script.

## Independent verification performed

1. **Load-bearing identities re-derived/verified from scratch (symbolic, sympy
   exp-rewrite — not numeric):**
   - secant's Key Identity KI: N(s)U + N(t)V + W = sin(s−t)[N(s)N(t) − sin²s sin²t] — holds identically. ✓
   - secant's Lemmas 4.1–4.4, all four interpolation evaluations D(t)=D(0)=D(φ)=D(μ−φ)=0, and every displayed intermediate (U|_{s=φ}, V|_{s=φ}, W|_{s=φ}, U|_{s=μ−φ}, V|_{s=μ−φ}, W|_{s=μ−φ}, V|_{s=t}=−U|_{s=t}, U|_{s=0}=−sin t N(t)). ✓
   - secant's Step-5 coefficient collection (4): G·sin s sin t = c² sin²t·V + b² sin²s·U + bc·W — holds identically. ✓
   - complex's certificate (10): 2 sin A·G = αℓ_K + βℓ_L — holds identically in all six free variables (sympy's default simplify fails; exp-rewrite closes it; also numeric to 1e-31 at random points). ✓
   - complex's bracket identity, (Id-b²), (Id-c²), (Id-bc), and **every individual Fourier-table row** (4 bracket rows, T1–T5 + decomposition, S1–S6 + decomposition) — all exactly as displayed. ✓
   - The two constraint forms agree: sin(φ+u)sin(φ+A−u) − 2 sin u sin(A−u) ≡ cos A − cos(φ+u)cos(A+φ−u). ✓
2. **Elimination steps re-derived by hand** (secant Step 3 determinant; complex Part 3 r-parametrization — the branch-pinning via sin χ > 0 is sound, no division by a possibly-zero quantity: divisor is r sinφ > 0, and the parametrization (2) is valid even when sin(φ−u) = 0).
3. **End-to-end configuration test, built from scratch** (`endtoend.py`): for 5 unrelated triangles (including isoceles b=c and obtuse A=110°), constructed K, L by root-finding on the decoupled conditions ∠ACK = φ+∠BMK, ∠ABL = φ+∠LNC, then *verified all five hypothesis conditions independently* (K ∈ int△BMC, L ∈ int△BNC, both angle-additivity/interiority conditions, both angle equalities). In every valid configuration: (K), (L), ℓ_K, ℓ_L ≈ 0 (1e-15) and OM − ON ≈ 0 (1e-16). This confirms the hypothesis→constraint encodings are correct, not just the identities.
4. **Interiority/angle bookkeeping audited line by line** (secant Lemmas 0.1–0.3 and consequences (a)–(d); complex Part 0): the six Law-of-Sines triangles are genuinely nondegenerate, ray BM = ray BA / ray CN = ray CA justified, angle additivity from "inside the angle" justified (proved via sector computation in secant; asserted with crossbar-theorem support in complex — see minor note below), all sines shown positive before any division.
5. **Non-collinearity of A, K, L:** complex proves it from the hypotheses (Part 4, cot-monotonicity — checked, valid). secant flags reliance on the problem statement's "triangle AKL" (legitimate, and used exactly once); complex's Part 4 removes even that.
6. **Interpolation logic (secant 6a–6c):** frequency count checked term by term (all summands have odd s-frequency ≤ 3, so D(s) = e^{−3is}Q(e^{2is}), deg Q ≤ 3); the six collision hyperplane families are exactly right; four distinct roots ⟹ Q ≡ 0; density + continuity of the trig polynomial D closes the degenerate parameter set. Valid.
7. **Answer requirement:** `task: proof_only`, `answer_type: none` — the proofs prove exactly the stated claim OM = ON. Statement in problems.jsonl matches the Problem restated in both files.

## Verdicts (per approach)

### 1. `secant-trig-identity` — **APPROVE** (Status: solved)
- Correctness: every step valid; all identities and the elimination verified independently. No circularity (hypotheses ⟹ (K),(L); KI is unconditional; goal follows).
- Completeness/rigor: configuration input fully consumed in Step 0 with proofs; no hidden gaps found; all divisions justified (sinφ, sin s sin t, Δ = sin(A−α−β) via "triangle AKL", flagged).
- Progress: complete solution.
- Builder's claimed Status `solved` is **correct**.

### 2. `complex-certificate` — **APPROVE** (Status: solved)
- Correctness: certificate (10) and all three coefficient identities hold; every displayed Fourier-table row is exactly right; Part 3 branch-pinned elimination sound; Part 4 non-collinearity proven from the hypotheses.
- Minor (non-blocking) notes: Part 0a has a mid-sentence restart ("lies on the edge... more directly:") but the signed-distance argument actually given is complete; Part 0d asserts angle additivity for "ray inside an angle" without the sector computation (it is a standard fact, and the identical fact is proven in full as secant's Lemma 0.3 / Lemma 0.1). Neither affects validity.
- Builder's claimed Status `solved` is **correct**. This proof is fully self-contained (does not even lean on "triangle AKL" for non-collinearity) — copied to `current.md` as the canonical proof.

### 3. `midpoint-reflection-isogonal` — **CHANGES REQUESTED** (Status: partial — as claimed)
- Lemmas 1–4 re-checked by hand and numerically (`check_mri.py`): reflection dictionary, Apollonius/parallelogram-law reduction, and directed power step are all correct, including the tangent-at-A edge case. Reduction (I) confirmed to 1e-15.
- Gap (file: Step 5): no synthetic derivation of (I) from the transferred hypotheses; the candidate hunt is exhaustively refuted. Honest status accounting — no overclaim.
- With the problem now solved twice, this slug's remaining value is the certified synthetic reduction (promoted to `lemmas/reflection-reduction.md`); recommend pruning or freezing it rather than further build effort.

## Promotable lemmas — certified into `results/imo-2026-02/lemmas/`
- `median-reduction.md` (complex Parts 1+5 / secant Step 1) — admitted.
- `AKL-noncollinear.md` (complex Part 4) — admitted.
- `side-relations.md` ((K)/(L) = ℓ_K/ℓ_L, both forms, shown identical) — admitted.
- `certificate-identity.md` (certificate (10) + KI, both symbolically verified) — admitted.
- `reflection-reduction.md` (midpoint approach Lemmas 1–4; reduction only, gap noted) — admitted.
All statements checked no-stronger-than-proved; none rejected.

## Files written
- `results/imo-2026-02/current.md` — created; Status **solved**; Full proof = complex-certificate's (canonical), secant-trig-identity recorded as independent second proof.
- Five lemma files as above.

## Goal Progress:
Status: **solved** (round 1). Two independent complete proofs APPROVED (`secant-trig-identity`, `complex-certificate`), both reviewer-verified end to end (all identities symbolic-checked, hypothesis encoding validated on independently built configurations); `midpoint-reflection-isogonal` remains partial (certified reduction, open synthetic gap) and can be frozen. Ranking picture: two verified-milestone leaders, one partial trailer. Run goal met — no further rounds needed on this problem.
