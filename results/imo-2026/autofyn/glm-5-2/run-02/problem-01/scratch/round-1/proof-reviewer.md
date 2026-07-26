# Proof review — imo-2026-01 (IMO 2026 P1, blackboard gcd/lcm process)

Two candidate proofs this round:
- `/home/agentuser/repo/results/imo-2026-01/approaches/invariant-first.md`
- `/home/agentuser/repo/results/imo-2026-01/approaches/monovariant-first.md`

## Problem statement (verified against problems.jsonl)

2026 integers > 1 on a board. A move picks m, n > 1 from distinct places and replaces them with gcd(m, n) and lcm(m, n)/gcd(m, n). (a) Prove that regardless of choices, after finitely many moves, exactly one integer M > 1 remains. (b) Prove M is independent of choices. `answer_type: none`, `task: proof_only` — no numeric answer to verify.

## Independent verification of load-bearing claims

I re-derived the key steps from scratch (with python3 over 2000 random moves and explicit small cases):

- **Move reduction (g, ab):** with g = gcd(m,n), m = ga, n = gb, gcd(a,b) = 1, lcm = m·n/g = gab, so lcm/g = ab. Correct.
- **ΔW = −Ω(g):** Old Ω-sum = 2Ω(g) + Ω(a) + Ω(b); new = Ω(g) + Ω(ab) = Ω(g) + Ω(a) + Ω(b) (Ω(ab)=Ω(a)+Ω(b) via coprime disjointness). ΔW = −Ω(g). Verified numerically on 2000 random pairs (including all small cases {2,4},{4,8},{9,27},{2,2}).
- **Three-case partition** {g=1}, {m=n}, {g>1 & m≠n}: disjoint, exhaustive. Case (iii) correctly handles g>1 with one of a,b = 1: a≠b (since m≠n) plus gcd(a,b)=1 plus not both =1 ⇒ ab > 1, so ΔC = 0, ΔW = −Ω(g) ≤ −1. The flagged examples {4,8}→{4,2}, {9,27}→{9,3}, {2,4}→{2,2} all fall in case (iii) and behave as claimed.
- **Euclidean-pair preservation (actually proved, not asserted):** Both proofs give the divisor-set coincidence argument gcd(a,b) = gcd(a, b−a) (assume a ≤ b): common divisors of {a,b} = common divisors of {a, b−a} since each divides b−a iff it divides b. Plus the zero sub-case (0,b) → (0,b) is identical. Genuine proof, not hand-waving.
- **gcd(0,k)=k convention stated and used:** both proofs state it; it makes zeros neutral in the fold, and is used to handle non-divisible entries and the all-1s terminal g_p = 0 case.
- **Terminal-state forcing:** Termination + well-foundedness of ℕ × {0,…,N} lexicographic ⇒ terminal state with ≤ 1 entry > 1 (legal move iff two entries > 1 exist, since (g, ab) is always a valid positive-integer pair). The invariant Q ≥ 2 forbids 0 entries > 1 (all-1s ⇒ g_p = 0 ⇒ Q = 1 ≠ Q ≥ 2). Hence exactly one. Bridge is sound.
- **M = Q for part (b):** terminal valuations {v_p(M), 0,…,0} have gcd v_p(M) (by gcd(0,k)=k, folding); by invariance v_p(M) = g_p; so M = ∏ p^{g_p} = Q, determined by initial board. Choice-independence follows. No gap.
- **Well-foundedness of the lex descent:** ΔC ≤ 0 always (cases (i),(ii) give −1, case (iii) gives 0), so C is non-increasing and bounded below; W ≤ W_0 and drops only finitely often. Both proofs give a finite bound (monovariant-first's crude W_0 + 2026·(W_0+1) is valid, though unnecessarily loose; invariant-first uses general well-foundedness). Either way finiteness holds.
- **knowledge_base references:** "Invariants & monovariants" (line 117/191), "Divisor analysis" (line 86), "Infinite descent" (line 184) — all exist as cited.

No gaps found in either proof. Both are complete and rigorous; every theorem named; every case settled; the zero/edge sub-cases are handled; the three-case partition is exhaustive and disjoint; the gcd(0,k)=k convention is stated and used consistently; the Euclidean-pair preservation is proved (divisor-set coincidence), not asserted; the terminal-state forcing bridge (≤1 from termination, ≥1 from invariant Q ≥ 2) is sound; M = Q is shown for part (b) and depends only on the initial board.

## Per-slug verdict

### invariant-first
- Correctness: full. ΔW = −Ω(g) verified; three-case casework exhaustive and disjoint; Euclidean preservation proved.
- Completeness / rigor: full. gcd(0,k)=k convention stated; zero sub-case handled; well-foundedness of lex descent cited; all steps justified.
- Progress: complete solution of (a) and (b).
- Status: **solved**. Builder's "solved" status is correct.
- Verdict: **APPROVE**.

### monovariant-first
- Correctness: full. Same load-bearing structure, identical ΔW = −Ω(g), identical three-case partition handling the {4,8}/{9,27}/{2,4} subcase.
- Completeness / rigor: full. Convention stated, zero sub-case handled, Euclidean preservation proved (not asserted), M = Q derived for part (b).
- Progress: complete solution of (a) and (b).
- Status: **solved**. Builder's "solved" status is correct.
- Verdict: **APPROVE**.

The two proofs are essentially equivalent in structure and strength (same invariant g_p / Q, same monovariant (W, C), same three-case casework). Both are correct; no need to prefer one. current.md records a unified Full proof.

## Lemma certification
- `exponent-euclidean-step` — **certified**. Statement correct (no stronger than proved), sorry-free, proved from scratch in the lemma file. Admitted to `results/imo-2026-01/lemmas/`.
- `exponent-pair-euclidean-invariant` — **certified**. Statement correct (the whole-board gcd invariance), sorry-free, proved in the lemma file. Admitted.

## current.md
Created with Status = solved (at least one APPROVE), both approaches listed with verdicts, Current best filled, Full proof written (unified statement of the shared argument).

---
invariant-first: APPROVE
monovariant-first: APPROVE
