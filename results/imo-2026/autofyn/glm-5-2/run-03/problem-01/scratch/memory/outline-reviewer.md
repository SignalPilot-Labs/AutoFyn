# outline-reviewer per-role rules

ALWAYS: test the per-prime move identity gcd(min(α,β),|α−β|)=gcd(α,β) and the Ω-difference identity Ω(m)+Ω(n)−[Ω(gcd)+Ω(lcm/gcd)] numerically before approving any gcd/lcm-move approach — outliners repeatedly mis-state the Ω-difference as 2Ω(gcd) when the correct value is Ω(gcd) (the conclusion Ω drops by ≥1 survives, but the stated lemma is wrong) (imo-2026-01, round 1).

NEVER: rubber-stamp a Dershowitz–Manna multiset-order decrease on exponent vectors for a gcd/lcm *replacement* move without checking the coprime disjoint-support case — the diff vector |u−v| equals max-cw when u,v have disjoint supports (e.g. m=4, n=9: removed {(2,0),(0,2)}, added {(0,0),(2,2)}; (2,2) dominates both removed, so DM decrease FAILS). The natural fix collapses to the (Ω,K) lex route — a technique-clone, not a new framing (imo-2026-01, round 1).
