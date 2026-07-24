# proval

This repo solves Olympiad math problems with AI. Problems are in `problems.jsonl` (the **Math Contests 2026** benchmark, 132 problems); reusable theorems and strategies are in `knowledge_base.md`. Proofs are written in **prose Markdown** (no Lean).

**Two retrieval resources, consult BOTH when solving:**
- `knowledge_base.md` — generic theorems and techniques.
- The **crux corpus** — 2434 load-bearing moves of solved pre-2026 problems across number theory, combinatorics, and algebra, disjoint from the 2026 test set. A retrieved crux is a *hint to adapt*, never a citation — every borrowed step must still be proven from scratch. Filter by `domain` first, then `subtopic`. Files, field schema, and the subtopics index are in `crux_moves_documentation.md` — read that before querying the corpus.

We target the **hard** problems only: the 39 entries whose `difficulty_level` field is `"hard"` (IMO P3 / P6 difficulty, `difficulty_rating` 8–10). Ignore the `easy` and `medium` problems.

A run attacks **one** hard problem, keeping a population of rival approaches for it in `results/<problem_id>/`. Solve it.

## For the orchestrator

This is a math repo, not a code repo. Adapt the standard round accordingly:

- **Setup:** `pip install` scientific and computational python packages: `numpy`, `scipy`, and `sympy`. Do not look for `package.json` / `pyproject.toml`. The only artifacts are Markdown files under `results/`.
- **One problem per run.** A run attacks exactly ONE hard problem `<id>`, chosen in round 1 and fixed for the whole run. All rounds push that one problem. List the hard ids: `grep '"difficulty_level": "hard"' problems.jsonl | grep -o '"problem_id": "[^"]*"'`.
- **Progress signal — the approach ranking, not a solved count.** A hard problem sits `partial` for many rounds while the population moves, so the signal is the ranking (Elo, live vs dead-ended, gaps closing), not a solve flip. Read `results/<id>/approaches/.ranking.json` and `results/<id>/current.md` `## Status` into Eval History each round; a `solved` (proof-reviewer APPROVE) is the headline.
- **The slug is a whole attempt — competing complete solutions, not one proof split into pieces.** Each slug targets the problem's actual claim end to end, gaps and all. Never suggest the outliner to split one proof across slugs — if the shared gap is wrong they all die together (the single-gap trap). Rival approaches must diversify in their framing and route — keep them far apart from each other. Approaches that only differ in technique are too close: they hit the same wall and fail together. Push for diversity of thought across the field, not one idea tried many ways.
- **Break a shared-gap plateau — challenge the gap itself.** When the top approaches have all bottomed out on the same step for 3+ rounds, or the outline-reviewer flags the field has collapsed to one framing, the real problem is usually that the approaches are too close — variations of one framing, so they share one wall. Don't just route around that gap (a bypass in the same framing hits the same wall one step later). Tell next round's outliner to put ≥1 approach on the table that attacks the problem from a genuinely different framing, far from the current field.
- **Rank every round — no fast-path.** The outline-reviewer runs every round so the Elo reflects the latest outcomes and the sampler keeps the population broad. No "skip the reviewer and advance the leader" path — that collapses to one line.
- **Dispatch counts (every round).** `math-explorer ×(1–3) → proof-outliner ×1 → outline-reviewer ×1 → proof-builder ×(1–N) → proof-reviewer ×1`. Explorers fan out **in parallel, each scouting a different route to the whole problem** (not just a different lens on the same one) — diversify and broaden the terrain. Builders fan out **one per approach in the build set, in parallel** — each owns its own approach file, so they never collide; **one proof-reviewer reviews all of them**.
- **Report paths.** Dispatch each subagent to write its report to its canonical `/tmp/round-{N}/<agent-name>.md` — don't rename it; the next agent reads that exact path. When several explorers run, each writes `/tmp/round-{N}/math-explorer-<lens>.md`.
- **Build set.** The outline-reviewer's report ends with `build set: <slug>[, <slug>...]` — dispatch **exactly one proof-builder per slug**, each told its slug. The set mixes approaches to advance (close more gaps) and any new/revised approach the outliner opened this round.
- **Route per approach (overrides the engine's whole-round "all APPROVE" gate).** One verdict per built slug, routed independently:
  - **APPROVE** — Status `solved`, complete and correct: terminal, recorded by the reviewer. Neither holds the round open nor sends the others back.
  - **CHANGES REQUESTED** — Status `partial`, real progress but a gap remains: re-dispatch only that slug's builder to close more (this round or next; its approach stays live either way).
  - **RETHINK** — Status `unsolved`, the approach can't work as set up: that slug goes back to the outliner to re-plan; the others are unaffected.
  A mixed result is normal, not a failed round.
- **Git artifacts.** Commit only the problem workspace `results/<id>/` (and edits to `CLAUDE.md` / `knowledge_base.md`). No build caches.

## The `results/<id>/` folder — one approach = one slug

The problem's workspace. **One approach = one slug = one approach file + one ranker entry.** It holds:

- `approaches/<slug>.md` — the approach itself: a **complete rival attempt at the whole problem** — its top-level target is the problem's actual claim, not a sub-lemma — written as a prose proof with its unproved steps left as explicit **gaps** (so an incomplete approach is still a valid population member). One per approach; the builders each own their own, so parallel builds never collide.
- `approaches/.ranking.json` — the ranker sidecar (Elo, counts, last outcome). **Tool-owned — never hand-edit it**; only the ranking tools (served by `.autofyn/approach_ranker.py`) touch it. Each agent's prompt says which it calls.
- `lemmas/<lemma>.md` — the **shared cache**: a lemma proved and reviewer-certified in one approach, importable by any other instead of re-proving. Builder proposes, reviewer certifies.
- `current.md` — the reviewer-owned tracking file: `## Status` (solved | partial | unsolved) and, once solved, the `## Full proof`.

## Workflow

Each run picks **one** problem and loops over a **population of approaches**, one flow every round (each agent's job is in its own prompt; counts and routing in the orchestrator bullets above):

`math-explorer ×(1–3) → proof-outliner → outline-reviewer → proof-builder ×(1–N) → proof-reviewer`

The explorers scout different routes to the problem — genuinely different framings, not just different lenses on one; the outliner hands a field of rival approaches (new, revise, advance, copy) to the outline-reviewer, which **ranks every round** and is the ranking hub + gate + build-set emitter; builders fan out one per approach in the build set; the reviewer verifies each and records its outcome.

## The file contract

`current.md` (reviewer-owned) and each `approaches/<slug>.md` use these sections:

```
## Status
solved | partial | unsolved

## Approaches tried
- <approach> — <verdict: worked / dead-end and why>

## Current best
The furthest correct progress: the key lemma, reduction, or partial result.
Empty only if nothing correct has been established yet.

## Full proof
Present ONLY when Status is `solved`. The complete, rigorous proof.
```

- **`solved`** = a complete, rigorous proof: every case covered, no gaps, every theorem invoked named, and (for problems with a final answer) the answer stated explicitly and verified.
- **`partial`** = a correct reduction or a proven key lemma, but the proof is not complete.
- **`unsolved`** = no correct progress yet.

## Rigor rules

These are mandatory. The proof-reviewer enforces them.

- **No skipped cases.** Every case in a casework proof must be settled.
- **No hand-waving.** No "clearly / obviously / it is easy to see / it follows" without justification. If a step is non-trivial, justify it.
- **Name your tools.** State every theorem or technique you invoke by name and cite the relevant entry in `knowledge_base.md`.
- **Verify final answers.** For `compute_and_prove` problems (and any with a non-`none` `answer_type`), state the answer explicitly and verify it by substitution or a small computation.
- **Prove, don't conjecture.** Distinguish "we have proved X" from "we conjecture X." Never present an unproven claim as established. Overclaiming is worse than admitting a gap — surface the gap so the next round can attack it.
- **For "find all / largest n":** prove an upper bound AND construct an example that attains it. One without the other is `partial`, not `solved`.
- **For "infinitely many":** exhibit an explicit family, don't assert existence.

## Working rules

- **Always read first.** Before attempting a problem, read `results/<id>/current.md`, the live `approaches/<slug>.md`, and `knowledge_base.md`. Build on prior progress; don't repeat dead ends already recorded.
- **Never re-attempt a solved problem.** If run state marks it `solved`, skip it.
- **Record everything.** A failed approach with the reason it failed is valuable — write it under `Approaches tried` so no agent retries it.
- **One approach, one file.** `results/<id>/approaches/<slug>.md`, one slug per approach; the reviewer-owned `results/<id>/current.md` is the tracking file.
- **The scratch pad is the source of truth.** Discussion, attempts, and the proof all live in the problem workspace — not only in conversation.
