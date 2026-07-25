# proof-builder report: state-compactness-pigeonhole (round 6)

File updated: `/home/agentuser/repo/results/imo-2026-06/approaches/state-compactness-pigeonhole.md`
Status: partial (unchanged)

## What was done this round

Added new §13, hand-tracing the assigned outlier instance
$a_1=20735=5\cdot11\cdot13\cdot29$ per the round-6 outline.

- Computed the sequence and its Nec-witness pairs (via direct, independently
  cross-checked computation; sequence generation is fully deterministic/
  mechanical, not a proof-by-computer logical step).
- Verified by hand trial-factorization: $a_4=20748=2^2\cdot3\cdot7\cdot13\cdot19$,
  $a_{70}=21185=5\cdot19\cdot223$, giving witness pair $(4,70)$ for the
  necessary prime $19$ — the outlier the round-6 outline referenced.
- Extracted the exact combinatorial mechanism: the "obstruction set"
  $O=R(a_4)\setminus\{19\}=\{2,3,7,13\}$ is accidentally hit by 5 consecutive
  earlier multiples of 19 ($a_{13},a_{27},a_{41},a_{55}$) before the 6th
  ($a_{70}$) finally avoids all of $O$.
- Cross-checked an "obstruction-set-size drives delay" heuristic (an
  independent-avoidance probability model) against two previously-fast seeds
  ($a_1=385$: $|O|=2$, delay 2 trials; $a_1=194287$: $|O|=3$, delay 2
  trials) — order-of-magnitude consistent but explicitly NOT proved or
  turned into a bound.
- Honestly recorded (§13.4) that this is diagnostic content only: it
  explains *why* no simple closed-form bound has been found (obstruction-set
  size can itself grow as recruitment proceeds — a possible feedback loop),
  but produces no new certified lemma and does not touch the central
  existence gap (finiteness of Nec / self-sufficiency of $Q_{\min}$).

## Outcome

Central gap (does a finite self-sufficient $Q$ exist; equivalently is
$\mathrm{Nec}$ finite) remains fully open. No promotable lemmas this round
(purely diagnostic case study, no new unconditional proven fact beyond
already-certified lemmas used as ingredients). Status correctly kept
`partial`.
