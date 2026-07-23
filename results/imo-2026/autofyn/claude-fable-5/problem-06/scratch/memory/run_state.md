## Goal

**Problem:** imo-2026-06

**Statement:** Let $a_1, a_2, a_3, \ldots$ be an infinite sequence of positive integers greater than 1. Suppose that for all positive integers $n$, the number $a_{n+1}$ is the smallest positive integer greater than $a_n$ such that $\gcd(a_{n+1}, a_i) > 1$ for every $i = 1, 2, \ldots, n$. Prove that there exist positive integers $T$ and $L$ such that $a_{n+T} = a_n + L$ for every positive integer n.

**Task:** proof_only (no answer to verify, just prove the statement)

**Metric:** proof correctness (APPROVE from proof-reviewer)

**Eval command:** Read results/imo-2026-06/current.md - Status solved = goal achieved

**Baseline:** Status = unsolved (no proof attempts yet)

**Target:** Status = solved (complete, rigorous proof with proof-reviewer APPROVE)

**Constraint:** All rigor rules from CLAUDE.md must be satisfied

## Goal Updates

## Eval History

### Round 3 — BREAKTHROUGH / SOLVED
- Status: **solved** (proof-reviewer APPROVE on both `small-prime-core` and `wqo-domination`)
- Two independent complete proofs delivered
- Key insight: Small Common Prime Lemma (SCPL) — any two terms share a prime ≤ a_1 — proved by minimal-counterexample descent with Companion Lemma at threshold z = a_1
- Threshold correction: z = a_1 is load-bearing (rad(a_1) fails for non-squarefree a_1, e.g. a_1=48 term 56=2³·7)
- Goal achieved: `results/imo-2026-06/current.md` Status = solved

## Rules
- ALWAYS read knowledge_base.md and crux_moves before generating new approaches (round 1)
- NEVER split one proof across slugs -- each slug is a complete attempt at the whole problem
- ALWAYS diversify approaches: different framings, not just different techniques
- ALWAYS run outline-reviewer every round regardless of perceived progress
- NEVER use rad(a_1) as companion threshold — use z = a_1; rad(a_1) fails for non-squarefree a_1 (round 3)
- NEVER cite Dickson's lemma on P_fin(primes) under inclusion — it is NOT WQO (round 3)
- ALWAYS give outline-reviewer a concise prompt to avoid timeouts (916s idle failure in round 2)

## State

**Done:**
- Round 1: Setup complete. Problem identified as imo-2026-06. Workspace created.
- Round 2: Explorers ran; outliner produced plan; outline-reviewer timed out (force-interrupted at 916s idle).
- Round 3: Three parallel explorers → outliner → fast outline-reviewer → two parallel builders → proof-reviewer APPROVE. PROBLEM SOLVED.

**Broken:**
(none)

**Next:**
- GOAL ACHIEVED. End session.
