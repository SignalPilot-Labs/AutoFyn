# outline-reviewer role memory

ALWAYS: call ranker functions (update_ranking/register_approach/copy_approach) via `python3 -c "import sys; sys.path.insert(0,'.autofyn'); import approach_ranker as r; r.update_ranking(...)"` — approach_ranker.py has NO argparse CLI, it runs mcp.run() under __main__ (round 1).
ALWAYS: for imo-2026-06 the whole problem reduces to ONE crux (essential primes finite / A periodic mod finite M); the "for every n" finish is trivial via min-of-superset (a_{n+1}=min(A∩(a_n,∞))). Empirically prime factors of L are always ≤ maxpf(a_1). Beware fields where all approaches share this single crux (round 1).
ALWAYS: for imo-2026-06 verify structural clause claims at DEPTH — shallow greedy sims (N<=800) wildly overcount minimal clauses/large essential primes (a1=2310: 243 clauses at N=800 collapse to 1 at N=1600); truncated clauses aren't truly minimal (round 2).
ALWAYS: run r via `cd /home/agentuser/repo && python3 -c "import sys;sys.path.insert(0,'.autofyn');import approach_ranker as r;..."` — bash cwd resets to repo root-ish but module needs absolute .autofyn on path from repo root (round 2).
