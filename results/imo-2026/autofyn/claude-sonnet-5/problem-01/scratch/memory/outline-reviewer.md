# Outline-reviewer per-role notes (accumulated across rounds)

ALWAYS: independently recompute claimed values of an invariant at degenerate
/ boundary / identity-element states (e.g. "all entries = 1", "empty set",
"all zero") rather than trusting the outliner's stated number — found a real
error in imo-2026-01's outline where `Γ(all-1s board) = 0` was claimed but the
outline's own definition (`Γ = ∏_p p^{γ_p}`) gives `∏_p p^0 = 1`, not 0; the
error was self-consistent-looking because a compensating weak bound
(`Γ(initial)≥1` instead of `>1`) on the other side of the same inequality made
the "contradiction" still look like it closed, when actually both sides needed
correcting together. A single-lemma proof that only cites "verified
computationally, 0 violations" for the *generic* case can still hide a wrong
value at exactly the *degenerate* case that matters for the argument, since
degenerate states are usually undersampled by random stress-testing. (round 1)

ALWAYS: when an outline claims a case-split (e.g. "3 exhaustive disjoint
cases") is exhaustive/disjoint/correctly computed, brute-force it yourself
with a short Python script over a real range rather than accepting "verified:
200,000 random pairs, 0 violations" at face value — cheap (seconds) and it is
exactly where fatal outline errors live (per CLAUDE.md's "no skipped cases").
In this round it held up, but the check is cheap enough that skipping it is
not justified even when the outline reports its own extensive verification.
(round 1)

NEVER: assume a dispatch-flagged "difficulty_level mismatch" (e.g. a problem
tagged "medium" that the round is nonetheless working under the hard-problems
loop) is yours to resolve — note it briefly for the orchestrator and keep the
mathematical verdict independent of it. (round 1)
