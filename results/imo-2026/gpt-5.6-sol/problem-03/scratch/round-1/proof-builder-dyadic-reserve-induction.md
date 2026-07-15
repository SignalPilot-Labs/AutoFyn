## Status
partial

## Build outcome
Wrote the assigned approach at `results/imo-2026-03/approaches/dyadic-reserve-induction.md`.

Substantial rigorous progress:
- proved the greedy drafting value by backward induction, including all ties;
- derived the alternating discrepancy payoff identity;
- proved the layer-cake identity and exact arbitrary-real split toggle, explicitly covering repeated cuts of current daughters and provenance;
- gave the legal normalized dyadic marking construction;
- completely solved the `n=1` case, including Liu using no mark and every arbitrary two-parent configuration;
- made the infimum/epsilon upper-bound quantifiers and legal positive/distinct perturbation requirement explicit.

The approach remains partial. The two load-bearing all-`n` assertions—the dyadic refinement lower bound and universal provenance-respecting refinement upper bound—are not proved by the outline’s reserve language. The approach file records them as explicit gaps rather than overclaiming the conjectural answer.

## Promotable lemmas
The approach proposes the greedy drafting lemma, alternating discrepancy layer-cake lemma, single-refinement toggle lemma, and exact `n=1` solution for certification.