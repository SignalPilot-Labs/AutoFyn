# proof-outliner per-role rules

ALWAYS: stress-test candidate lemmas with small numeric counterexamples BEFORE putting them in a skeleton (pointwise rank bounds q_{2i-1} ≤ 2^{n-i} for imo-2026-03 looked plausible but failed at n=3 with 8→(3,3,2); only the aggregate/alternating-sum form survived, round 1)
ALWAYS: for imo-2026-03, reformulate LB's value as (σ + A)/2 with A = alternating sorted sum; both bounds become "A vs 1 unit of 1/(2^{n+1}-1)" — this is the cleanest common currency across approaches (round 1)
NEVER: give two slugs the same load-bearing sub-lemma without flagging it to the reviewer — GAP III (leftover invariant) is shared by geometric-cascade-induction and pairing-exchange-normal-form; parity-alternating-sum was added as the hedge whose upper bound avoids it (round 1)
ALWAYS: record concrete test data (computed minima like L(3,c) = 10,9,8,8; stress configs like (0.45,0.15,0.1,0.1,0.1,0.1)) inside the approach file — the builder needs them to find the right invariant (round 1)
