# proof-reviewer — role memory

ALWAYS: verify geometry candidate proofs end-to-end by reconstructing configurations directly from the problem hypotheses (root-solve the angle conditions from raw coordinates, confirm every hypothesis numerically, then test the claimed conclusion/closed forms) — this catches wrong bookkeeping that identity-checking alone misses (worked round 1, imo-2026-02).
ALWAYS: re-derive claimed polynomial/trig identities in sympy from the RAW definitions (e.g. F(T;t) − m·q(t) from the dot-product definition), not from the proof's intermediate steps — that independently certifies the load-bearing step in one shot (round 1).
ALWAYS: when auditing angle-chase bookkeeping, check exactly where "P inside angle XYZ" hypotheses are invoked — they are usually load-bearing for the SIGN/ordering of direction angles (θ_L < θ_K), the classic place a geometry proof silently flips (round 1).
NEVER: treat "the problem posits triangle AKL / its circumcentre" as a gap when the statement itself grants the object's existence — accept it if the proof flags the reliance explicitly (round 1).
ALWAYS: call record_outcome by importing .autofyn/approach_ranker.py directly in python3 (sys.path.insert(0,'.autofyn'); ar.record_outcome(...)) — it is an MCP server with no CLI (round 1).
