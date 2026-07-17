# Proof-Outliner Memory

## Learned rules

ALWAYS: For game theory problems with alternating selection, verify greedy is optimal via exchange argument before assuming it (because it's load-bearing for the entire analysis, round 1)

ALWAYS: For "find largest c that player can guarantee" problems, structure the approach as: lower bound (player's strategy) + upper bound (opponent's counter), both required (because one without the other is partial, round 1)

ALWAYS: When approaches share the same gap (e.g., both need to prove "XY can limit ANY LB marking"), that's a single-gap trap — they fail together. Open a genuinely different framing (exchange argument, variational, minimax duality) rather than just varying the technique on the same wall (round 2)

ALWAYS: For alternating-sum game problems, pair-cancellation is the key mechanism: equal pieces at adjacent sorted positions contribute 0 to A. Use this to reduce the problem to controlling the non-paired pieces (round 2)

ALWAYS: When a pigeonhole argument gives "exists k with property P", consider whether choosing the LARGEST or SMALLEST such k gives additional constraints (like ratio bounds between k and k+1). This is the extremal choice principle (round 3)
