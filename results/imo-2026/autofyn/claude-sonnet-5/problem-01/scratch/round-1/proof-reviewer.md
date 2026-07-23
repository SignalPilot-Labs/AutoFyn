# Proof Review — imo-2026-01 (Confucius gcd/lcm blackboard)

**Verdict: APPROVE**
**True Status: solved** (matches the recorded `## Status: solved` — no correction needed)

## Scores
- **Correctness: 10/10.** Every step is valid; I re-derived the load-bearing
  claims from scratch and reproduced them.
- **Completeness / rigor: 10/10.** All cases present, disjoint, and settled; every
  invoked theorem named and cited to an existing `knowledge_base.md` entry; no
  hand-waving; edge cases (gcd(a,0), gcd(0,…,0), m=n, g=1) all handled.
- **Progress: 10/10.** Moves from the prior `partial`/conjectural state (numerically
  stress-tested invariant + monovariant) to a fully proven solution of both (a)
  and (b), plus a bonus closed form for M.

## What I verified independently (Bash/python3)
1. **Closed form M = ∏_p p^{gcd_i v_p(x_i)}.** 4000 random boards (N=2–8) × 5 random
   move-orders each = 20,000 full simulations: **0** mismatches, **0** terminals
   with ≠1 surviving entry. Separately confirmed the two in-text examples:
   (4,8)→M=2 with the stated path [(4,8),(4,2),(2,2),(2,1)], and (2,3,5,7)→210.
2. **Ψ-descent (Lemma H).** At *every* move of all 20,000 sims, checked
   Ψ_new ≤ Ψ_old/2 **and** strict Ψ_new < Ψ_old — held every time. Ψ_old is
   always divisible by 4 (c_old≥2), so the halving is genuine, giving termination
   in ≤ log₂Ψ₀ moves.
3. **3-way case split.** For all m,n∈2..200: classification into {g=1} / {g>1,m=n}
   / {g>1,m≠n} is exhaustive and disjoint; Δc equals the claimed −1/−1/0; the
   Ψ-ratio (1/g)·2^{Δc} is ≤ 1/2 in every case; and g=1 ⟹ m≠n (so no missing
   sub-case). 0 violations.
4. **Γ-invariance (Lemma G).** Γ recomputed after every move in all sims — never
   changed. The proof derives it for an *arbitrary* pair i≠j among all N via
   Grouping (F) + Subtraction (E) with the untouched entries carried identically
   on both sides — this is a genuine general proof, not an illustration.
5. **Lemma E (Euclid step).** gcd(min(x,y),|x−y|)=gcd(x,y) for all x,y∈0..119
   incl. edges (x=y, zeros); 0 failures; gcd(0,0)=0 as the proof states.
6. **Lemma B valuation identities.** v_p(gcd)=min, v_p(lcm)=max, v_p(lcm/gcd)=|diff|
   over 200,000 random pairs: 0 violations.
7. **Collapse-to-all-1's exclusion (the spot with the earlier caught error).**
   Re-derived from scratch: Γ(all-ones) = empty/zero-exponent product = **1**
   (not 0 — the earlier bug), while Γ(initial) ≥ 2 because x₁>1 forces some
   prime p₀ with γ_{p₀}≥1. Min closed-form over 20,000 all-initial>1 boards was
   3.3×10⁷ (always ≥2). The fix now in the proof (1 = Γ(terminal) = Γ(initial) ≥ 2
   contradiction) is correct.

## Targeted checks from the dispatch
- (a) Case split exhaustive & disjoint — **yes** (verified by hand and code).
- (b) Γ-invariance proved for arbitrary pair among all N with untouched entries —
  **yes**, via Lemmas F+E, then lifted by induction on move count.
- (c) Collapse-impossibility airtight, earlier sign error fixed — **yes**,
  Γ(terminal)=1 vs Γ(initial)≥2; re-derived independently.
- (d) Ψ strict descent in every branch, exact strictness — **yes** (Ψ_old≥4>0).
- (e) gcd/lcm valuation identities incl gcd(a,0) — **yes**, all correct.
- (f) Formula verified by a run-to-termination example — **yes** ((4,8)→2).
- (g) Unjustified "clearly/obviously" — **none**; grep found no such language.
- (h) Overclaim — **none**; the closed form for M is a bonus beyond the
  proof_only requirement, correctly proven.

## Dependency / circularity check
Lemma order A→B→C→D→E→F→G→H→(a)→(b) is acyclic; no lemma assumes its own
conclusion. Forward reference to Lemma B in the setup (for h∈ℤ₊) is legitimate
since B is proven independently.

## Nitpicks (NOT gaps — do not block)
- Lemma B derives v_p(lcm)=max via "the identical argument with max in place of
  min." This is the standard dual and the substitution is stated explicitly, so
  it meets IMO rigor; a maximally pedantic reader could want it spelled out, but
  it is not a gap. I re-verified the lcm side directly (200k pairs).
- **Metadata note (not a proof issue):** in `problems.jsonl` this entry is
  `difficulty_level: "medium"`, `difficulty_rating: 5` — not `"hard"`. Per
  CLAUDE.md the run targets the 39 hard problems, so this solved file does not
  increment the *hard* count even though the proof is correct. Flagging for the
  orchestrator; it does not affect the correctness verdict.

## Conclusion
The proof is complete and rigorous. Both parts (a) and (b) are fully established;
the value M = ∏_p p^{gcd(v_p(x₁),…,v_p(x_N))} is proven and verified. No gap
remains. **APPROVE / solved.**
