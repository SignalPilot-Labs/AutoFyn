# math-explorer per-role rules

Accumulated rules from prior rounds. Follow these like the Rules in run_state.md.

ALWAYS: verify "stabilizes / is finite / is periodic" conjectures with enough terms AND a structural argument, not just the first ~30 terms (round 1, imo-2026-06). For the greedy non-coprime sequence, the prime set looked bounded in the first 30 terms but is actually infinite — confirmed by exhibiting an explicit unbounded sub-sequence `a_{8k+6}=6(6+5k)`. Small-case periodicity evidence can hide an infinite, non-stabilizing underlying structure.

ALWAYS: when a sequence looks "periodic from the start", still search for eventual (offset>0) periodicity with longer `N` before reporting it as from-start — some starts (e.g. `a_1=315, 385`) had no detectable period within 1100 terms while the small cases settled at `T≤282` (round 1, imo-2026-06).

NEVER: assume a clean closed-form for the period modulus `L` in terms of `a_1` from a few data points (round 1, imo-2026-06). `L` was `2·rad(a_1)` for some starts (77, 91, 1001) but `2·3·5·7` for `a_1=35` (adds 3) and `2·3·11·13` for `a_1=143` (adds 3) — path-dependent, no simple threshold; recommend proving existence over computing.

ALWAYS: separate "essential" primes (load-bearing for the covering/transversal) from "free-rider" primes (factors of a_n that the greedy carries along by arithmetic, e.g. cofactors in a_n=p·n) — only the essential set is the real invariant; free riders can be infinite (round 1, imo-2026-06).

NEVER: build the whole field around the "common-prime collapse to T=1, L=p" framing for a greedy-gcd sequence — it is a terminal sub-case (triggered when a pure prime power term appears), not the main argument; multi-prime starts like a_1=15 (T=8,L=30), 35 (T=34,L=210), 77 (T=18,L=154) need general T>1 (round 1, imo-2026-06).
ALWAYS: query the crux corpus with `technique` + `how_used` fields (NOT `crux_move` / `statement` — they don't exist). Filter by `domain` first, then `subtopic`. The corpus has 548 NT cruxes; keyword grep over (technique + how_used) is the effective query (round 2).
ALWAYS: read the full solution of a corpus hit before judging adaptability — the `technique` field is a one-line summary; the load-bearing mechanics are in `how_used` and the full solution text, and the analogy often breaks at the mechanics even when the crux-move name matches (round 2, aimo-0030: crux name matches Lemma 4 perfectly but the game-move descent does not port to P6's greedy).
NEVER: trust a numeric check as proof — label small-case evidence as conjecture in the report (round 2).
ALWAYS: state, for each corpus hit, the P6 analogue of EACH sub-claim (not just the top-level crux) — the top-level match is necessary but not sufficient; the descent's specific sub-claims must each have a P6 counterpart or the route is a restatement (round 2).

ALWAYS: when a field has collapsed to a single shared gap (outline-reviewer flags 3+ approaches dying on the same wall), prioritize corpus cruxes whose *mechanism* differs from the field's framing — not just whose *target* matches. For imo-2026-06 Lemma 4, the field's framing is "finite-state mod ∏E + free-rider dichotomy"; the genuinely different mechanisms found were aimo-0030 (minimal-counterexample descent via stripped auxiliary), aimo-0648 (extremal-forces-equality + Bezout-propagate from consecutive seed), aimo-0447 (grid-cell counting via "large prime > span divides at most one term"). Each is orthogonal to lattice-stabilization; fielding one of these breaks the single-gap trap (round 2).

ALWAYS: when scouting "alternative framings" for a problem with a known shared crux, explicitly check whether each framing's load-bearing step reduces to the crux — most "different framings" are relabels. State this honestly even if the dispatch hoped for escape (the outliner needs truth, not wishful framing diversity). (round 2, imo-2026-06: every finite-state/translation framing reduced to Lemma 4 = E-finiteness; the real contribution was a different PROOF ROUTE for the crux, not a bypass.)

NEVER: brand a framing as "without E" / "without essential primes" just because it uses a cruder finite set (e.g. Q_R = primes ≤ R). If the wall is free-rider irrelevance, it IS E-finiteness in disguise. Flag relabels explicitly so the reviewer cuts them. (round 2, imo-2026-06: "mod rad(a_1) without E" = essential-monovariant relabel.)

ALWAYS: for a greedy-sequence periodicity problem, probe (a) whether singleton-type witnesses exist before proposing witness constructions — they may be provably inadmissible (for imo-2026-06, terms with singleton small-type are inadmissible because they're coprime to the odd a_1); (b) the pair-witness structure (terms with small-type exactly {p,q}) — it exists but doesn't rule out large-prime rescue. (round 2)
