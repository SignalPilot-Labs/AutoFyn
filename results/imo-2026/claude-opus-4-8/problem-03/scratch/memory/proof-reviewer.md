
## Round 2 (imo-2026-03)
ALWAYS: call the ranker via `python3 -c "import importlib.util; ...record_outcome(...)"` directly against .autofyn/approach_ranker.py — the MCP tool is not exposed as a function; the @mcp.tool()-decorated fns are plain callable and mutate approaches/.ranking.json (because no CLI main exists, round 2).
NEVER: promote an "AltSum reformulation" as a separate lemma — it is identical to the R2 parity form O=(1+A)/2; certify one canonical copy only (round 2).
ALWAYS: for a refuted-engine approach, verdict RETHINK even if the builder salvaged correct lemmas, when those lemmas are subsumed by a rival approach's certified ones (no independent progress) (round 2).

## Round 3 (imo-2026-03)
ALWAYS: for Lemma-H-style "halve p-1 largest, spare a_p" claims, the continuity extension is valid because the pairs are exact for EVERY LB vector (a_i) and genericity is only on the a_i values — O and 1/2+a_p/2 are both continuous coordinates, so dense-set equality gives everywhere (round 3, verified).

## Round 4 (imo-2026-03)
ALWAYS: independently re-run any "menu/strategy is optimal" kill-switch over the HARD regime only, not the full config space (because caseB's Lemma M kill-switch passed on random configs but was FALSE — random configs are dominated by easy cases where Reduction 2 trivially wins; the menu fails only when all gaps > 1/D, round 4, verified).
ALWAYS: when a builder refutes its own core lemma but salvages correct general-n reductions, verdict RETHINK (mechanism dead) yet still certify the salvaged lemmas into lemmas/ (round 4: caseB Lemma X + Reductions 1/2 certified despite Lemma M refuted).
NEVER: certify a "reduction to a vertex/global-min inequality" as a closed lemma file — it references an open gap (★); keep it in the approach file (round 4, direct-constructive Δ-reduction).

ALWAYS: when a lower-bound proof claims "min attained at a vertex" then invokes a genericity-only lemma (all-distinct values) at that minimiser, check the lemma at CLUSTERED/tie points — vertices are non-generic by construction, and random numerics never sample the measure-zero clustered set (imo-2026-03 round 5: "receiver always exists" was FALSE at clustered a=0 configs e.g. n=4 frags {2,10/3,10/3,11/3,11/3}, despite 1.5e5 random configs passing).
NEVER: accept a "closes ~94%" / empirical-percentage claim as a certified lemma; certify only the exact conditional sub-step, reject the percentage (imo-2026-03 round 5 IH(q) reduction).

## Round 6 (imo-2026-03)
ALWAYS: the directional-derivative A'+(e_a-e_b)=(-1)^G(g_a)+(-1)^Geq(g_b) (up-move strict-above G, down-move Geq) is CORRECT and holds AT TIES — verified 5e4 exact tie-laden checks; the round-5 refutation was the "receiver EXISTS" step, not the derivative (round 6).
ALWAYS: for IH(q) reductions, remember IH(q-1) as stated is GAP-FREE, so "cut b1 at b2 may break a gap" is a non-issue — the reduced instance only needs pieces>1/D and sum<(2^{q-1}-1)/D; don't demand gap-preservation (round 6, the reducible lemma's gap-preservation worry was moot).
NEVER: trust my own IH(q) test thresholds — I first coded the halve-branch cutoff as 3/D instead of the correct (2^{q-1}-1)/D=7/D and got false "fails"; the active-sum bound for reducing IH(4)->IH(3) is 7/D (round 6).
ALWAYS: the dyadic two-case split (Case1 w1<=2^{n-2} direct A>=2^{n-2}; Case2 named-receiver-by-counting) genuinely repairs the confined lower bound — both round-5 counterexamples land in Case1. Certified DyadicLower-confined. Remaining lower gap is L2 (cuts OUTSIDE R_n), a different simplex (round 6).

## Round 7 (imo-2026-03)
ALWAYS: certify VertexFace-style "every vertex of the constraint polytope lies on a face where a certified strategy wins" — verified by exact vertex enumeration (q=2..5, 0 off-face) AND polytope combinatorics (q+1 constraints, >=q active at a vertex => <=1 inactive); it is a CLOSED conditional-free fact even though the overall bound still needs the OPEN (V) max-at-vertex — write the (V)-is-separate caveat INTO the lemma file so IH(q) can't be misread out of it (round 7).
ALWAYS: GreedyCascade (dominant piece b_1>=1/2 => cascade cut b_1 to match each b_j, final multiset pairs each b_j twice => XOR-cancels => A=2b_1-1) is CORRECT and certifiable; legality r_j>=b_{j+1} from b_1>=1/2>=1-b_1; verified 0/3000 exact. Closes B2-large all n, no q-induction (round 7).
ALWAYS: re-derive threshold arithmetic yourself — the double-cancel IH(n-1) threshold is 3*2^(n-2)/D not 2^(n-1)/D (off by 3/2); the geometric config sits EXACTLY on the corrected threshold. Old value was an overclaim; builder corrected it (round 7).

## Round 8 (imo-2026-03)
ALWAYS: record_outcome signature is (problem_id, slug, round_number, outcome, note) — outcome in {advanced,partial,dead-end,verified-milestone}; call via importlib against .autofyn/approach_ranker.py (round 8, worked).
ALWAYS: verify a builder's "the closed slivers are only ~1/(2D) wide, so the residual is the BULK" claim by computing the window width from the constraints — upper-vertex-reduction c1 needs b_1∈[S/2,(S+1/D)/2], width exactly 1/(2D); confirmed c2b is the bulk not a remainder (round 8, honest builder, not overclaimed).
ALWAYS: the (‡) reformulation A≥1⟺E_F≤O_G rests on ΣG=(D−1)/2=2^n−1 exactly — check this before trusting the group-split identity; verified numerically E−ΣG=E_F−O_G tie-break independent (round 8).
