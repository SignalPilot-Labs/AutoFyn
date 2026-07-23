
ALWAYS: re-derive the descent's companion-object bound (Lemma S4-style: a1<=x<a_j) and BOTH descent cases from scratch before approving; the whole IMO-2026-P6 proof rests on that single construction (round 2).
ALWAYS: run the greedy simulation (sympy primefactors + gcd) to spot-check the finiteness crux across many a1 incl. primorials and the round-1 counterexample a1=385 before an APPROVE; caught nothing wrong this time but is the cheapest sanity gate (round 2).
NEVER: assume the MCP ranker tool is exposed as a function — it is not in the reviewer's toolset; replicate record_outcome by importing .autofyn/approach_ranker.py's _load/_save (same code path, not a hand-edit) (round 2).
