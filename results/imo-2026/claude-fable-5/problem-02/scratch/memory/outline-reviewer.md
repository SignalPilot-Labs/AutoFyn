# outline-reviewer per-role rules

ALWAYS: call the ranker via `python3 -c "import sys; sys.path.insert(0,'.autofyn'); import approach_ranker"` and invoke `f.fn(...)` if the FastMCP decorator wrapped it — the MCP tools are not in the reviewer's tool list (round 1).
ALWAYS: re-verify outlined formulas with your OWN script built only from the formulas as displayed in the approach file, not the outliner's code — this catches transcription errors in the displayed coefficients (round 1, all formulas checked clean this way).
ALWAYS: for geometry parametrization approaches, test the FORWARD direction too (construct K, L from the claimed roots and measure the original hypothesis angles + interiority) — the proof needs hypotheses ⟹ constraint, not just constraint ⟹ conclusion (round 1).
NEVER: put an approach in the build set whose critical closing step has no verified mechanism (power-point-trig Step 5, round 1) — hold it live instead; register it anyway if the partial reduction is correct.
NOTE: numpy.cross rejects 2D vectors in this container's numpy version — compute 2D cross products by hand (round 1).
