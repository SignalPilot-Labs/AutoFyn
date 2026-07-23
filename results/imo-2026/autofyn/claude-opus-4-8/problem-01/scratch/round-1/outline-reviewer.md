# Outline review — imo-2026-01 (gcd/lcm blackboard), round 1

Simulation check (2000 random boards, 5 random plays each): every play terminates with **exactly one** entry >1, and that entry always equals ∏_p p^{gcd_i v_p(x_i)}. Both the part-(a) claim and the part-(b) invariant are concretely confirmed. Neither approach is chasing a phantom.

Both approaches are whole attempts at parts (a)+(b) end to end — not fragments, not one proof split in two. They share the (forced) part-(b) g_p invariant and diverge on the genuine difficulty: the part-(a) termination argument. That is the right place to diversify.

## global-lex-monovariant — APPROVE

Technique is sound and the lex descent is airtight as written:
- Step 1: P_new = P_old/gcd(m,n) from gcd·lcm = mn. Non-increasing always; strict iff gcd>1; **unchanged** (not increased) when gcd=1 — the outliner's original GAP A1 confusion is already resolved in the file. Good.
- Step 3 lex descent (N primary, P secondary): every move drops N (coprime) or, if N is unchanged, the move cannot be coprime so gcd>1 and P strictly drops. The one subtlety a builder must state explicitly: **a non-coprime move may also drop N** (e.g. {p,p}→{p,1}); that is harmless since any N-drop is a lex decrease regardless of P. The clean phrasing is "N is non-increasing every move; if N is unchanged then gcd>1 and P strictly drops." Close GAP A1 with exactly that wording.
- Steps 4–6, 7–9: well-foundedness of lex on ℕ×ℕ, terminal N∈{0,1}, N=0 excluded via g_p>0, and the g_p invariant are all correct. GAP B1 (subtractive-Euclid identity gcd(min,|a−b|)=gcd(a,b), boundaries a=0/b=0/a=b) and B2 (gcd associativity over a zero-containing multiset) are routine and must be written out, not waved.

No circularity: part (a) step 6 (N≠0) legitimately imports the part (b) invariant (step 8); the invariant does not itself depend on termination. Fine.

## per-prime-valuation-descent — APPROVE

Distinct framing (valuation-mass potential Ω=Σ_p S_p instead of a global product), and the direct lex route is sound:
- Ω non-increasing; a non-coprime move (some prime divides both entries ⇒ min>0) strictly drops Ω; a coprime move keeps Ω constant and drops N by 1. Lex (Ω primary, N secondary): if Ω is unchanged the move is coprime so N drops — airtight, symmetric to the sibling. GAP T1 should be closed with this "if Ω unchanged ⇒ coprime ⇒ N drops" phrasing; **fix the visible re-derivation clutter in step 3** (the file still contains the outliner's scratch "corrected orientation" musings — the final orientation is (Ω,N), state it cleanly).
- Must note **finitely many primes appear** before summing over primes (already flagged in Watch-out) — otherwise Ω is a sum with unbounded index; it is a finite sum because E_p≡0 for p not dividing any initial entry.
- The extremal / minimal-Ω counterexample engine (step 5') is a legitimate second route but is **redundant** given the direct lex works; a builder should lead with the direct lex and may drop 5' unless the lex snags. Not load-bearing.
- B1/B2/B3 identical to the sibling.

## Diversity note for the orchestrator

The two termination engines are genuinely different (global scalar product vs per-prime valuation mass), so they will not stall on the same wall in part (a). They **do** share the part-(b) g_p invariant and the N=0 exclusion — but that part is essentially forced and simulation-confirmed, so shared reliance there is acceptable, not the single-gap trap. If a future round needs more spread, the place to diversify is a third framing of part (a) (e.g. the Euclid-swap/sorting-network view), not part (b).

## Ranking

Both registered at cold start; global-lex-monovariant rated the marginal winner (1516 vs 1484) — slightly cleaner exposition (single scalar monovariant, no finiteness-of-primes bookkeeping) puts it marginally closer to a writeable proof. Both are sound and both build.

build set: global-lex-monovariant, per-prime-valuation-descent
