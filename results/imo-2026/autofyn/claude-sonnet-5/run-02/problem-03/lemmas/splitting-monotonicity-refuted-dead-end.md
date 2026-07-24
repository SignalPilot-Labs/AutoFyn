## Statement (DEAD-END RECORD, not a positive reusable lemma)

The conjecture "splitting any single fragment of a Case-I partition $F$
into two never *increases* $E(F\cup\tau)$" (which, if true, would reduce
Case I of Claim (A)/GC($m$) to checking finitely many "coarsest" boundary
partitions) is **FALSE**.

**Counterexample.** $m=2$, $\tau_1=14$, $\tau=(14,7)$, $F=\{8.12\}$
(single fragment, $k=1$, $\le\tau_1$), split into $\{3.8976,4.2224\}$
(still summing to $8.12$, both $\le\tau_1$): $E(F\cup\tau)$ goes from
$8.12$ (before the split) to $10.8976$ (after) — splitting **increased**
$E$, by nearly $3$. Not a rare edge case: $37{,}127$ violations found in
$200{,}000$ random split trials.

## Verification (proof-reviewer, round 7)

Independently recomputed both configurations by direct sort-and-alternate
computation: before split, $S=\{14,8.12,7\}$ sorted, $E=8.12$; after
split, $S=\{14,7,4.2224,3.8976\}$ sorted, $E=7+3.8976=10.8976$. Confirmed
$E$ strictly increases, matching the claimed counterexample exactly.

## Why this matters

Rules out the "reduce Case I to the coarsest partition" strategy entirely
for this project. Any future round attempting a monotonicity-based
reduction of Case I should not re-attempt this exact splitting-direction
claim.

## Recorded as

`results/imo-2026-03/approaches/rank-pigeonhole-budget.md`, §4.10
(round 7).
