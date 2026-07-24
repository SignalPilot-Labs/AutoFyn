# Outline review — imo-2026-03, Round 7

Whole problem is ONE gap from solved: `f≥1` at the tied non-degenerate Φ-max minimizer `P*`,
where `Uw=b`, `ker U={0}`, `f=sᵀw`. All three explorers independently re-confirm (Cramer:
`f=Σ_j s_j det(U_j)/det(U)`, so `f·det U∈ℤ`) that EVERY route must control `det U` (square) or the
maximal-minor gcd (rectangular) — the shared fact is **minimality ⇒ benign incidence matrix `U`**.
No real-valued/geometric bypass exists (primal-geometry explorer verified `K` is the unconstrained
product of simplices; nonintegrality explorer gave the Cramer necessity proof). The field is three
approaches, each attacking that shared fact with a different object. Diversity is acceptable
(cycle-exclusion vs dual-λ-lattice vs single-column-concentration), with one overlap flagged below.

---

## self-similar-recursion — APPROVE (advance)

Elo 1689 (lead). Primal cycle-exclusion machinery. Steps 0–5 + Lemmas CC/S-core/blocks already
certified. Residual correctly localized this round by the primal-geometry explorer:

- Gap A′ EVEN sub-case narrowed to exactly {genuine chord} ∪ {cycle-COMPONENT touching an
  off-cycle piece, comp-deg≥3} ∪ {non-uniform cycle multiplicity} — VERIFIED numerically: the even
  ker-U witness `d(Q_i)=(−1)^i` survives off-cycle-PIECE attachment and uniform-mult scaling, dies
  only on those three shapes (all exactly where the cycle sub-system gains full column rank). The
  θ-full-rank lemma (chord glues two cycles ⇒ rank deficiency 1→0) + distinct-powers-RHS positivity
  is a sound, stated mechanism.
- Gap A′ ODD sub-case: genuinely escapes pure algebra (explorer's explicit cex `b=(1,2,2.5)→u=
  (0.75,0.25,1.75)` all positive) — must go through MINIMALITY (is the escaping feasible point ever
  actually a Φ-max minimizer of `f` over `K`?), NOT extended telescoping. The outline commits to
  the S-core feasible-shift engine here; this is the right lever.
- Gap B (`μ=3` even-block leaf) via Lemma BD (degenerate-Φ-domination): mechanism stated (slide a
  copy to the shared partner ⇒ length-0 sub-piece degenerate competitor with `f` exactly flat ⇒
  Claim(N−1)). Load-bearing and still unconstructed — the builder must track the moved value's
  global rank to keep `f` exactly flat, or it fails.

Verdict: technique sound, residual is now concretely the smallest it has ever been. Issues to close
while building: (1) prove θ-full-rank as a general lemma, not the 4-node example; (2) the odd-case
minimality argument must exhibit an actual feasible descent/flat+Φ-rise direction in `∏Δ_k`, not a
cross-piece transfer (see the concentration caveat below — same trap applies here). Do NOT retry
full-cycle telescoping on non-isolated cycles (refuted, 479 cex).

## dual-integer-certificate — APPROVE (advance)

Elo 1557. Dual lattice/congruence machinery, genuinely distinct object (coprime maximal minors, not
det=±1). Lemma DUAL + gap-d-not-universal certified. Two concrete new levers this round, both sound
to pursue:

- Small-`p` reduction: dual explorer found Gap-D failures concentrate at `p=n+1` (maximal distinct
  value-classes); does minimality/Φ-max bias `P*` toward small `p`? Untested but a real structural
  lead.
- aimo-0281 unified-invariant (nonintegrality explorer's corpus hit): a SINGLE minimality-derived
  congruence on `(U,s)` that forces `s∈Uᵀℤ` (Gap D) AND `f≠0` (Pos) at once, rather than two
  independent gaps. This is the crispest merge of the dual route's two open gaps.

Verdict: right technique, honestly reduces to Gap D-at-minimizers + Positivity. Enforce: (1) MUST
use minimality (Gap D false as universal S-core property — certified); (2) Positivity is a
CO-EQUAL gap, do NOT re-assert "min is positive" — the λ₀-parity mechanism is REFUTED (λ
non-unique), naive per-piece KKT is REFUTED (subgradient at a tie is the full interval `[−1,1]`,
vacuous — dual explorer re-confirmed 5/9 n=3 minimizers violate same-sign-per-piece), `μ_j odd⇒
μ_j=1` is REFUTED. The unified-invariant lever is the sanctioned path.

## concentration-exclusion-rigidity — CHANGES REQUESTED (new, registered)

Elo 1498. Registered this round. Third machinery — forbid a **concentrated value-class column**
`m·e_k` (`m≥2`) at the Φ-max minimizer, then Cramer gives `f∈ℤ,≥1`. Genuinely a different object
(`{2,4/3,4/3,4/3,1}` is not a cycle and not a λ-construction), and it attacks the shared wall
head-on as the orchestrator asked. It does NOT re-derive any round-6 refutation: it uses minimality
(not universal S-core), does not use λ₀-parity, naive KKT, global integrality, or the dead
geometric lever. So it clears the "does it bypass the refutations" bar — but the core mechanism has
two real defects the builder MUST fix, so this is not APPROVE:

1. **Step-2 exchange mechanism is flawed as written (the load-bearing lemma).** "Increase `C_j`'s
   copies in `2^k` and compensate in `2^{k'}`" is a CROSS-PIECE mass transfer — infeasible in
   `K=∏_k Δ_k`, where each piece's sub-pieces sum to its own fixed length `2^k` (primal-geometry
   explorer + round-5 finding: the product of simplices has NO cross-piece moves). The only
   charitable reading — move the shared value `v` as one class, compensating WITHIN each piece — is
   a tie-preserving direction `d` with `Ud=0`, which cannot exist since `ker U={0}` (S-core). So
   "the same feasible-shift engine as Lemma S-core" cannot yield MORE than S-core already extracted
   (which was only `ker U={0}`). The genuine feasible moves are tie-BREAKING (split the `m` copies),
   governed by the certified cut-slide-derivative — the builder must recast step 2 as a one-sided
   derivative / Φ-second-order argument at the chamber boundary, NOT a cross-piece exchange, and
   must show the perturbation provably STAYS in the minimizer set `G` (my role-memory: the
   compensated same-piece 3-shift `{v,v,v}→{v+s,v+s,v−2s}` is the refuted V-kink move `f=m+2|s|`,
   strictly up both ways, it LEAVES `G`).

2. **The unshared-concentration case = Gap B, left unaddressed.** The fatal instance
   `{2,4/3,4/3,4/3,1}` has `4/3` present ONLY in piece 4 (column `3·e_k`, not shared). The step-2
   exchange (which needs a sharing piece `2^{k'}`) does not apply; the outline waves it as "`m∣det U`
   outright." That is exactly self-similar's open Gap B (`μ=3` even-block leaf). So the approach
   silently reduces its fatal case to Gap B — which contradicts its own "Watch out for: do NOT
   reduce to another approach's object." This is acceptable ONLY if the builder attacks that
   unshared case with a genuinely new argument (e.g. Cramer-det + a counting/degenerate-competitor
   bound), not by re-labeling it.

3. **Step-3 benign-U peeling re-asserts the conclusion.** "Each non-concentrated class contributes a
   `±1` pivot against the distinct powers `2^k`" is the whole `det=±1` claim restated with a
   plausible-sounding but unproven pivot mechanism. Distinct-powers-RHS being load-bearing is
   correct (det=2 cex known), but the contiguous-rank-interval + `±1`-pivot step needs an actual
   proof, or it hides the same wall.

Verdict: worth building — the Cramer + concentration framing is the crispest head-on statement of
minimality⇒benign-U and could crack both routes — but the builder is directed to (a) discard the
cross-piece exchange and use a tie-breaking cut-slide-derivative argument that stays in `G`, (b)
give the unshared/Gap-B case its own argument, (c) supply a real pivot mechanism for step 3, or
honestly record the gap. Not RETHINK: the target and the Cramer/variational technique are sound;
only the sub-mechanism is wrong.

## Diversity note (for the orchestrator)

The three do NOT collapse to one machinery: primal cycle-rank (self-similar), dual congruence
lattice (dual), single-column concentration + Cramer det (concentration). All three share the
DESIGNED common target (minimality⇒benign-U) — that is intentional (round-6 decision) and
acceptable. One real overlap: concentration's unshared case coincides with self-similar's Gap B.
Watch that these two builders don't both stall on the identical `μ=3` leaf with the same argument —
concentration must bring the Cramer-det angle to it, self-similar the degenerate-Φ-dominator (Lemma
BD). If both stall on Gap B next round, that is a genuine shared-wall signal to seed a fourth
framing.

## Ranking (updated this round)

self-similar-recursion 1689 > dual-integer-certificate 1557 > concentration-exclusion-rigidity 1498
> cut-budget 1493 > block-recursion 1456 > game-value 1406 > majorization 1301. (alternating-sum
1600 untouched — holds the certified upper bound, not a lower-bound approach.) Newcomer anchored
against established opponents (lost to self-similar and dual, beat the dormant no-gap-closed
game-value and the dead-end majorization).

build set: self-similar-recursion, dual-integer-certificate, concentration-exclusion-rigidity
