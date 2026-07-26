# proof-outliner — per-role rules

ALWAYS: before outlining, verify any recursion/identity the explorers claim by a quick sympy/Fraction check (the dispatch's "convergence" can still have sign or direction errors). Round 1. (Confirmed the Möbius linearization u = −1/A gives the linear recursion u(n+1)=2u−1 for imo-2026-03.)

ALWAYS: for a minimax game with a conjectured formula, find the Möbius/conjugation that linearizes the value recursion — a linear monovariant is a genuinely different framing from naive induction on the nonlinear recursion, and gives a clean per-step potential drop. Round 1.

ALWAYS: each slug is a WHOLE proof (lower bound + upper bound + small-n); when the lower bound is shared across slugs, write it once as a shared lemma block that every skeleton includes, but the builder still writes it per-slug. Round 1.

NEVER: outline an upper-bound approach as "casework/heuristic on which piece to split" when the explorers recorded that all simple greedy heuristics (split-largest, split-all, split-n-largest) FAIL — the route must be induction/recursion/potential/pairing/surrogate, not a greedy rule. Round 1.

NEVER: pair pieces into EQUAL halves as the upper-bound certificate — that yields the wrong value (n+1)/(2n+1) and ignores Xiang's shred-the-small mode. The correct pair structure is the dyadic-ratio pair-pile. Round 1.

ALWAYS: when revising a stuck approach, name the SPECIFIC explorer insight that closes each gap (e.g. "M ⊎ R self-similar decomposition + L* dual IH" for Lemma L; "regime-N pairing under non-dominance" for Lemma U) — vague "use the explorer's insight" leaves the builder guessing. (Round 2, imo-2026-03.)
NEVER: use the dispatch's `V(n+1)=(1+V(n))/2` recursion form for imo-2026-03 — it is mathematically WRONG (predicts V(2)=5/6 vs verified 4/7). The correct form is `1/V(n+1)=1+1/(2V(n))` (Mersenne `B(n+1)=2B(n)+1`). (Round 2, imo-2026-03.)
ALWAYS: for the two-regime upper-bound framing, the regime-N pairing lemma (non-dominant → all pair-excesses ≤ 0 → A ≤ 0 → Liu ≤ 1/2 < f(n)) is the EASIER half and should be built/proved first; regime-D (dyadic-dominant rescaling) is where the interleaving wall lives. (Round 2, imo-2026-03.)
NEVER: trust coarse-grid (D=84) computational evidence for the "cap tight only at dyadic" claim — non-dyadic configs falsely appear to attain the cap on coarse grids. Use D ≳ 2520 or analytic perturbation. (Round 2, imo-2026-03.)

ALWAYS: verify the explorer's "engine gives equality at the dyadic" claim by running the engine ON the dyadic config before fielding it. (Round 3, imo-2026-03: the greedy two-largest pile-match OVERSHOOTS on the dyadic (8,4,2,1)/15 → oddsum 3/5 > f(3)=8/15 — it is a regime-N tool only; the certified pair-pile remains the regime-D equality case. The explorer's "equality characterization falls out at the dyadic" was wrong for this engine.)

NEVER: field a "subset-probability / Kraft / binary-tree" framing for imo-2026-03 as a genuinely-different approach — the subset recursion D(n)=2D(n−1)+1 IS the Mersenne recursion, so it collapses into the unified-Mersenne-potential framing; and oddsum is a sorted-RANK sum (sort-by-weight) that misaligns with tree-leaf-depth. (Round 3, imo-2026-03.)

ALWAYS: when fielding multiple NEW approaches that share an empirical equality-case invariant (e.g. the sliver-canceling flat polytope / odd-multiplicity `{1}`/`{2^j,2^j+1}` structure for imo-2026-03), flag the shared-wall risk explicitly in BOTH skeletons and in the field report's diversity check — two approaches leaning on the same unproven real-valued classification die together if it fails to lift, even if their surrounding framings diverge. (Round 4, imo-2026-03: `cell-complex-l3` and `equality-case-classification` share the flat-polytope equality locus; `equality-case-classification` and `two-regime-disjunctive` share the equality-case classification as G2 load-bearing.)

NEVER: claim the structural equality-case classification (odd-mult `{1}`/`{2^j,2^j+1}`) alone closes G2 for imo-2026-03 — it gives `A ≠ α` off the dyadic, but the SIDE (`A < α` not `A > α`) needs the sliver forcing, which is the (U-E) global wall restated, not a bypass. (Round 4, imo-2026-03.)

ALWAYS: before importing a certified lemma's COROLLARY (not just the main statement), re-verify it computationally — a certified lemma can have a valid identity but a FALSE corollary. (Round 5, imo-2026-03: `lemma-superincreasing-R.md` identity `a_j−Σ_{l>j}a_l=α(n+1)` stands, but the corollary `σ≤M/2=a_1` is FALSE for k≥2 — 50% of n=3 unrefined-R configs have σ>a_1; verified at m=(3,3,1,1): σ=5>4=a_1.)

ALWAYS: when a proof splits on a structural condition (e.g. "m_1 is global rank 1"), verify the condition holds for ALL configs in the sub-case it claims to cover — a proof that only covers 50% of its claimed domain is invalid even if the result is true. (Round 5, imo-2026-03: the L(3) unrefined-R proof's setup "m_1≥a_1=4" fails for 50% of k≥2 configs; the m_1-split into Branch 1 (m_1≥a_1) and Branch 2 (m_1<a_1) is the fix.)

NEVER: field a U(3) approach using only the 5-cap subfamily `{a, b−a, c−b, 2d−1, |a+b−c|}` — it FAILS for d<1/2 (5 violations on N=60 grid, because `2d−1` is invalid when d<1/2). The full 17-strategy exact-pair family (adding `|a+c−d|, |b+c−d|, d−b−c` and sliver-tuned strategies) is needed for the d<1/2 regime. (Round 5, imo-2026-03.)

ALWAYS: for the 2-adic/halving-depth induction on G2, distinguish "induction on the CONFIG's halving depth" (how many consecutive ratios are exactly 2:1 — a structural property of Liu's partition) from "induction on the round-level value recursion" (conceded dead as a bypass, round 2) and from "bisect largest and recurse on halves" (KILLED round 3, because f(n)/2<f(n−1) strictly). The halving-depth induction is on the config structure, not on the value or on a sub-game. (Round 5, imo-2026-03.)

NEVER: trust a cap *value* (like `d−b−c`) as a valid Xiang strategy without checking its realizability condition (`d≥b+c`) — round-5's "17-family necessary / no 4–7-cap subfamily suffices" ruling for U(3) extreme sub-cases was an artifact of including un-realizable cap values; with realizability enforced, the 7-cap subfamily `{a, b−a, c−b, d−c, |a+b−c|, |a+c−d|, |a+b−d|}` (all always-realizable, none requiring `d≥b+c`) closes BOTH extreme sub-cases. (Round 6, imo-2026-03.)

ALWAYS: when an explorer reports "computationally 0 violations but no small subfamily suffices," re-audit the realizability mask on the candidate subfamilies before accepting the ruling — a census that includes un-realizable cap values will falsely inflate the necessary family size. (Round 6, imo-2026-03.)

ALWAYS: when a certified lemma's "factor-of-2 gap" (e.g. `L(n)` on R gives only `o_R≥M/2` but `e_M≤o_R` needs the full `o_R`) is numerically loose with slack GROWING with n (0 violations n=3..7), treat it as a PROOF-TOOLING gap (the induction is too weak a tool) not a real obstruction — field a direct-injection route bypassing the induction. (Round 6, imo-2026-03.)
