# proof-builder per-role rules

ALWAYS: define multiset-gcd conventions (all-zero -> 0; common divisors of T = divisors of gcd(T), proved via the lcm(d,e) maximality trick) BEFORE using per-prime gcd invariants — the zero-valuation edge cases are where reviewers probe (worked cleanly, imo-2026-01 round 1).
ALWAYS: prove common-divisor-SET equality instead of gcd-value equality for Euclidean-type identities — it handles all zero cases uniformly with no case explosion (round 1).
ALWAYS: prove lex well-foundedness on N x N inline (eventually-constant first coordinate, then strictly decreasing second) — it is not in knowledge_base.md and may not be cited bare (round 1).
ALWAYS: before subtracting valuations of a quotient, first show the quotient is an integer (e.g. gcd | m | lcm) — otherwise v_p subtraction is unjustified (round 1).
ALWAYS: for gcd/lcm rewriting confluence, search for FIXED integer-level joining schedules by BFS over move sequences applied to a whole random test vector (schedule shared across tests) — a depth-7 BFS found the uniform "pull shared place to triple-gcd, then pair-collapse" join that closes the overlap case without per-prime scheduling (round 1).
ALWAYS: relax legality with a "formal move" device when moves have side conditions (entry > 1): a formal move violating the condition fixes the multiset, so formal paths project to real paths by deleting stationary steps — kills all intermediate-legality edge cases at once (round 1).
ALWAYS: replace lex monovariants by a single nonnegative-integer monovariant when one coordinate is bounded (N = (size+1)*P + C) — makes Newman's well-founded induction a plain strong induction on an integer (round 1).
