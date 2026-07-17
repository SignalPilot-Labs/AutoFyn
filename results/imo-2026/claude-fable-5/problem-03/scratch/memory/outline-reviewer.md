# outline-reviewer per-role rules

ALWAYS: numerically stress-test any "verified on hand cases" lemma with random instances before approving — the geometric-cascade-induction Merge Lemma passed 6 hand-picked equality cases but failed ~40% of random instances (round 1)
ALWAYS: invoke the ranker by `python3 -c "import sys; sys.path.insert(0,'.autofyn'); import approach_ranker as ar; ar.register_approach(...)"` from /home/agentuser/repo — it is an MCP server but its tool functions are directly callable (round 1)
ALWAYS: when refuting a greedy/algorithmic upper-bound strategy, also check that the OPTIMAL adversary still meets the target on the same configs — distinguishes "gap in the invariant" (fixable) from "conjectured answer wrong" (fatal) (round 1)
NEVER: approve a lemma of the form "f(A∪B) ≥ g(A) + f(B)" without testing whether it must instead factor through min_B f(B) — charging B at its actual value rather than its minimum is how the false Merge Lemma arose (round 1)
