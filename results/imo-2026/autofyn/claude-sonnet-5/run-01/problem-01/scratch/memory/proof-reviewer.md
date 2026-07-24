# proof-reviewer role memory

ALWAYS: re-derive the invariant/monovariant of a process problem by brute-force
simulation over many random boards AND many random move-orders, checking the
invariant at EVERY move (not just endpoints) — this instantly confirms or refutes
Γ-invariance, Ψ-descent, and any closed form (round 1, imo-2026-01: 20k sims,
0 counterexamples confirmed the proof).

ALWAYS: for "collapse/empty-product" edge cases, recompute the empty product = 1
(and gcd(0,…,0)=0, gcd(a,0)=a) by hand — an earlier builder error in imo-2026-01
was claiming Γ(all-ones)=0 instead of 1; verify the FIX is right, don't trust
"already reviewed" (round 1).

ALWAYS: verify a case split is BOTH exhaustive and disjoint by enumerating all
small (m,n) and classifying each — catches a missing/overlapping sub-case fast
(round 1: {g=1}/{g>1,m=n}/{g>1,m≠n} confirmed a partition, g=1⟹m≠n).

ALWAYS: grep the proof for KB citations and confirm each cited entry actually
exists in knowledge_base.md (round 1: all of "v_p count", "Invariant/monovariant",
"Infinite descent", "Reformulate" were present).

NEVER: assume a strict monovariant descent from a non-strict inequality — check
the proof separately establishes strictness (e.g. Ψ_old≥4>0 giving Ψ_new<Ψ_old),
which the descent bound alone does not (round 1, imo-2026-01, done correctly).

NOTE: imo-2026-01 is tagged difficulty_level "medium" (rating 5) in problems.jsonl,
NOT "hard" — a correct solved file here does not increment the hard-problem count
the run targets. Flag such metadata mismatches to the orchestrator (round 1).
