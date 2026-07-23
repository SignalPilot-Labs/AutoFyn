## Goal

Solve IMO 2026 Problem 1 (`problem_id: imo-2026-01`), the Confucius
gcd/lcm blackboard problem, per explicit user instruction (overrides
CLAUDE.md's default "hard problems only" scope for this run — note
imo-2026-01 is actually labeled `difficulty_level: "medium"`,
`difficulty_rating: 5` in problems.jsonl, not "hard").

Problem (number_theory, proof_only, answer_type none):
2026 integers >1 on a blackboard. A move picks m>1, n>1 in different
positions and replaces them with gcd(m,n) and lcm(m,n)/gcd(m,n).
(a) Prove the process always terminates with exactly one entry >1.
(b) Prove that final value M is independent of the choices made.

Deliverable: `results/imo-2026-01.md` with `## Status` = `solved`,
containing a complete rigorous proof of both (a) and (b), passing
proof-reviewer with APPROVE (no gaps, no hand-waving, every theorem
named per CLAUDE.md rigor rules).

Metric: solved (1) vs not (0) for this specific problem.
Eval command: `grep -A1 '^## Status' /home/agentuser/repo/results/imo-2026-01.md | tail -1`
  → must print `solved`.
(General benchmark eval for reference, not this run's focus:
`grep -rl '^solved$' results/ | wc -l`.)
Baseline: 0 (no results file existed at round 1 start).
Target: 1 (solved).
Constraint: full rigor — no skipped cases, every tool named and cited
to knowledge_base.md, both directions (termination AND invariance of M)
fully proved.

User supplied a partial proof seed in their message (worth checking
whether math-explorer/proof-outliner should build on it): "Write the
entries currently on the board as x_1,...,x_2026. Entries equal to 1
remain on the board, but they cannot be selected for a subsequent
move." — this is just a setup sentence, not real progress; pass along
as context but don't treat as established progress.

## Goal Updates

- [Round 1, mid-turn] User: "once done can you push this in a branch with an
  accompanying latex file and a separate markdown file with nicely formatted
  solution and commentary of the solution. branch name: modelname-imo
  year-problem <no> e.g. sonnet5-imo2026-01" — i.e. once imo-2026-01 is
  solved, additionally produce (1) a LaTeX writeup of the solution, (2) a
  separate polished Markdown file with solution + commentary (distinct from
  the terse `results/imo-2026-01.md` contract file), and (3) push to a
  branch named `sonnet5-imo2026-01` (model running this session is Sonnet 5).
  IMPORTANT CONFLICT: orchestrator constraints explicitly forbid
  branch/commit/push operations myself — "the harness handles git" — so I
  cannot rename/create branches or push directly. Plan: produce the LaTeX +
  polished-Markdown deliverables as build output once solved (extra
  artifacts beyond the standard results/ contract); surface the branch-name
  request to the user as a limitation since teardown branch naming is not
  exposed to me as a tool. Will remind the user of this in my final summary.

## Eval History

- Round 1: baseline eval = 0 (no results/imo-2026-01.md existed).
- Round 1: math-explorer recon → strong lead (p-adic valuation reformulation;
  candidate monovariant Ψ=Φ·2^c; candidate invariant Γ=per-prime gcd-of-
  valuations), numerically stress-tested, explicitly labeled conjectural.
- Round 1: proof-outliner produced full outline, marked "Spec review:
  required."
- Round 1: outline-reviewer verdict CHANGES REQUESTED — found one real
  arithmetic error (Γ(all-1s terminal) = 1, not 0; collapse-exclusion needs
  strict Γ(initial) > 1 not ≥1) but independently reverified everything else
  (case split via 40k brute-force pairs, Γ-invariance via 400 simulations).
  Not a technique-level RETHINK — a localized, precisely-specified fix.
- Round 1: proof-outliner applied the exact fix, reverified numerically.
- Round 1: proof-builder wrote the complete proof (Lemmas A–H, Parts a+b),
  Status → solved.
- Round 1: proof-reviewer independently re-derived every load-bearing step
  (~20,000 simulations + exhaustive small-range checks), confirmed the fix,
  found zero remaining gaps. **Verdict: APPROVE. Status: solved.**
  → Eval metric: 0 → 1 (target reached). BREAKTHROUGH: full solve, review
  round-trip, and fix all completed within round 1.
- Round 1: extra deliverables (LaTeX + polished Markdown solution/commentary,
  requested mid-turn by user) produced by proof-builder as pure exposition
  over the already-approved proof; LaTeX independently verified to compile
  (via a fetched tectonic binary) with zero errors.

## Rules

- ALWAYS treat an explicit user request to solve a *named specific problem*
  as overriding CLAUDE.md's "hard problems only" default scope for the
  run (round 1). The named problem becomes the sole Goal even if its
  difficulty_level is "medium" or "easy".
- ALWAYS `pip install numpy scipy sympy` at round 1 setup per CLAUDE.md
  (not preinstalled in this container; round 1 confirmed missing).
- ALWAYS, when a plan/outline reviewer returns CHANGES REQUESTED with an
  exact, precisely-specified, localized fix (not a wrong-technique finding),
  route back to the *same planner* to apply it and treat that as sufficient
  before moving to the builder — don't fix mathematical content yourself
  (orchestrator does not do math), and don't demand a second full review
  pass when the reviewer already independently verified everything else and
  gave the exact corrected argument (round 1, imo-2026-01: saved a full
  extra review round-trip this way).
- ALWAYS route "extra deliverable" requests (LaTeX writeup, polished
  Markdown solution+commentary, or other presentation formats) to
  proof-builder as a pure exposition/formatting pass over an *already
  proof-reviewer-APPROVED* results/<id>.md — instruct it explicitly not to
  alter mathematical content and to stop/report rather than silently fix
  anything if it spots an error while transcribing (round 1, imo-2026-01).
- NEVER attempt git branch/commit/push operations myself even when the user
  explicitly requests a specific branch name or asks to "push this" —
  orchestrator constraints reserve all git write operations for the harness.
  Surface the request/limitation to the user in the round summary instead of
  silently dropping it or silently attempting it (round 1: user asked for
  branch `sonnet5-imo2026-01`; flagged as unfulfillable by me directly).

## State

### Done
- Round 1: read CLAUDE.md, README.md; confirmed no existing
  results/imo-2026-01.md; confirmed baseline eval = 0; installed numpy/
  scipy/sympy; set Goal in run_state.md.
- Round 1: full pipeline run on imo-2026-01 — math-explorer → proof-outliner
  (Spec review: required) → outline-reviewer (CHANGES REQUESTED, one fix)
  → proof-outliner (fix applied) → proof-builder (Status: solved) →
  proof-reviewer (**APPROVE**). Goal achieved: results/imo-2026-01.md
  Status = solved, full rigorous proof of both parts.
- Round 1: produced extra deliverables requested mid-turn:
  results/imo-2026-01.tex (compiles cleanly, verified via tectonic) and
  results/imo-2026-01-solution.md (polished write-up + commentary).
- Round 1: confirmed via `git status` no stray build artifacts (PDF/tectonic
  binary) left in the repo tree; only the 3 intended new files are untracked.

### Broken
(none)

### Next
- imo-2026-01 is fully solved and APPROVEd — do not re-attempt it in future
  rounds (per "never re-attempt a solved problem").
- User also asked to "push this in a branch" named `sonnet5-imo2026-01`.
  Orchestrator cannot perform git branch/push ops (harness-only). This was
  surfaced to the user in the round summary; if the user wants this
  fulfilled, it likely needs to happen outside this orchestration loop (or
  the user may accept the harness's normal auto-branch/PR flow instead).
- No further user-specified scope exists beyond imo-2026-01. If future
  rounds continue, default back to CLAUDE.md's standard scope (hard
  problems, 1–3 in parallel per round) unless the user gives new direction —
  check Goal Updates for any new message first.
