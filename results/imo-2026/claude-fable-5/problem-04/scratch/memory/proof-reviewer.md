# proof-reviewer — per-role rules

ALWAYS: simulate game-strategy proofs with an exhaustive adversary AND a *stateless* variant of the claimed strategy — the stateless run exposes cycles (θ=22.5°, (67.5,45,67.5) reproduces itself) that reveal whether the proof's induction genuinely tracks state; both round-2 proofs passed only because their descent tracks the exhibited multiple. (round 2)
ALWAYS: re-derive the piece/cut formula from raw coordinates (law of sines placement + measured angles), not from the proof's own algebra — independent derivation is what certifies the load-bearing identity. (round 2)
ALWAYS: when testing an invariant-preservation lemma, include the adversarial parameters that break it in the complementary regime (here t = θ − r_b and t = kθ), not just random cuts. (round 2)
NEVER: call `approach_ranker.py --help` — it is an MCP server with no CLI; import it from `.autofyn` in python3 and call `record_outcome(problem_id, slug, round_number, outcome, note)` directly. (round 2)
