# Round-3 outline-reviewer report — IMO 2026 P6

## Headline finding: free-rider universality is FALSE

Before reviewing individual approaches, I must report a **counterexample to the free-rider universality conjecture** that the entire round-3 field is built on. The outliner and all three explorers claim (135+ seeds, 0 violations) that every promotion M'=P(a_{n+1}) has a proper subset R⊊M' that is a transversal of old M_n. This is **false**, verified by hand and by computation.

**Counterexample (a1=15, step 3).** a1=15={3,5}, a2=18={2,3}, a3=20={2,5}. Old M_2={{3,5},{2,3}}. P(a3)={2,5} is a transversal of M_2 (hits {3,5} via 5, hits {2,3} via 2). But no proper subset is a transversal: {2} misses {3,5}; {5} misses {2,3}. So {2,5} IS a minimal transversal of M_2 — free-rider VIOLATED.

**Pattern (confirmed on 12 seeds).** Free-rider violations occur at **crash events** — the tight (minimal-transversal) promotions whose small-support minimals become final family members. a1=15: violation at {2,5} (final member). a1=1001: violations at {2,7},{2,11},{2,13} (final members). a1=429: violations at the final {2,*} minimals. The free-rider holds for "fat" (large-support) promotions but fails exactly at the crash. **The crash IS the non-free-rider (tight) event.** The conjecture's negation is the crash mechanism itself.

**Impact.** The free-rider was supposed to (a) refute γ's unique-connector obstruction (GAP-3), (b) provide β's non-circular large-a_n-no-promotion handle, and (c) discharge α's reach-to-saturation (step 4). All three are now broken or re-blocked. The field must be revised: the crash is HARDER than the outliner thought — it requires proving a tight minimal arrives, not that free-riders make it easy.

**SPT conjecture still holds (0 violations, 280 seeds + my 12-seed check).** Every minimal M ever arising has min(M) ≤ p*=min P(a_1). This remains the field's strongest structural target. But see the mechanism critique below.

## SPT mechanism critique (applies to ALL approaches)

The proposed SPT proof mechanism (outliner α step 3): "multiples of each small prime p≤p* are spaced p≤p* apart while the window length is mtp≥p* (pigeonhole), so a p*-rough valid candidate is always beaten by a smoother valid one."

**Flaw.** The pigeonhole gives that the mtp-window [a_n, a_n+mtp] (length ≥ p*, since mtp(M_n) ≥ mtp(M_1) = p* by monotonicity) contains a multiple of each p≤p*. But a multiple of p is **valid** (hits every minimal) only if {p} is a transversal of M_n, i.e. p is common — which is the FREEZE regime, not the saturated regime. In the saturated regime no singleton is a transversal, so small-prime multiples are NOT automatically valid. The mechanism confuses "a small-prime multiple exists in the window" with "a small-prime multiple is valid." SPT is a valid conjecture but this proof handle does not close.

**The real SPT attack should target:** at a promotion, a_{n+1} is NOT the mtp-multiple (else P(a_{n+1})⊇T* and if T*∈M_n it's dominated — no promotion). So a_{n+1} is a strictly-smaller valid candidate. SPT claims this candidate carries a prime ≤p*. The mechanism must show: any valid m < (smallest mtp-multiple above a_n) that the greedy picks must have a small prime factor. This is genuinely hard and unproved — it is the true linchpin.

## Per-approach review

### density-promotion-bound (α): CHANGES REQUESTED

- Freeze branch (F): SOLVED, certified. No changes needed.
- Saturated branch (S), step 3 (SPT): viable conjecture (0 violations) but the proposed pigeonhole mechanism is flawed (see critique above). The builder must find a real proof — the "validity of small-prime candidates" gap is the core difficulty.
- Step 4 (free-rider universality): **FALSE.** Counterexample at a1=15. Must be dropped entirely. The "cheap-kill" sub-lemma ("no strictly-smaller non-mtp-multiple valid m beats the mtp-multiple") is also false — a1=15 step 3 shows m=20 (not an mtp-multiple; mtp=3, mtp-multiple above 18 is 21) is picked and IS a promotion.
- Step 6 (SPT-density crash): the crash must be reframed. It is NOT "free-riders make large-prime minimals fat so a small one crashes." It IS "a tight (minimal-transversal) small-support minimal eventually arrives and refines the family." SPT forces small-support; the crash is the arrival of a TIGHT one. The mechanism for WHY a tight one arrives (not just any small-support one) is the open core.
- **Verdict: CHANGES REQUESTED.** Sound structure (regime casework + SPT + Sat-criterion + post-stabilization) but two steps need revision: drop free-rider (false), reframe crash around tight-minimal arrival. SPT proof is the linchpin — the builder should focus here.

### bounded-gap-lcm-reduction (γ): CHANGES REQUESTED

- mtp monovariant + gap bound (step 1): certified, unconditional. Solid.
- GAP-1 closure via SPT (step 2): imports SPT from α. Viable IF α proves SPT; γ has a backup route ("permanent-2-transversal") that should be attempted independently.
- τ monovariant (step 4): PROVABLE. Trans(M_{n+1})⊆Trans(M_n) is certified (refinement shrinks transversals); min cardinality over a subset is ≥. This is a real new structural lemma — the builder should certify it. The τ≤2 cap is conjectural (0 violations) but not load-bearing for the crash.
- Free-rider (step 3): **FALSE.** The unique-connector obstruction is NOT refuted — it returns. γ's crash is re-blocked.
- Crash via avoiding-transversal counting (step 5): re-blocked by the free-rider failure. The avoiding-transversal space may be unbounded via large primes (the outliner's own flag). minAvSz monotonicity is NOT a lattice formality (rank-descent explorer confirmed Avoid(M_{n+1})⊄Avoid(M_n) in general). The crash mechanism is conjectural with a known obstruction.
- **Verdict: CHANGES REQUESTED.** The τ monovariant is a genuine contribution worth certifying. The crash is in serious trouble (re-blocked by free-rider failure + unbounded avoiding space). The builder should: (1) certify τ monovariant, (2) attempt the backup SPT route (permanent-2-transversal), (3) honestly assess whether the avoiding-transversal crash can survive without free-rider. If the crash can't be unblocked, γ falls back to importing α's crash.

### bertrand-dickson-eviction (β): RETHINK

- Cofactor bound (step 2, q ≤ a_n/mtp+1): still valid arithmetically (free-rider decomposition isn't needed for the bound itself — any entering prime q divides the cofactor k=a_{n+1}/prod(R) where prod(R)≥mtp). But the bound is a_n-dependent (circular).
- Large-a_n-no-promotion handle (step 3): **DOUBLY BROKEN.** (a) It uses free-rider universality (FALSE — tight promotions exist at large a_n; the crash is one). (b) The "T*∈M_n" sub-step is unproved: T* is a transversal but being a transversal ≠ being a MEMBER of M_n; if T*∉M_n, domination of P(a_{n+1})⊋T* does not follow. (c) The circularity (bounding a_n by termination) is not broken.
- Bounded promotion count (step 4) + Dickson finish (step 5): downstream of step 3; cannot close without the non-circular a_n handle.
- **Verdict: RETHINK.** The load-bearing step (step 3) is broken by the free-rider failure and the T*∈M_n gap. No non-circular handle for bounding a_n exists in the outline. The cofactor arithmetic is a genuine different mechanism but has no path to close without it. Send β back to the outliner to find a genuinely different non-circular a_n bound, OR fold its cofactor arithmetic into α as a sub-lemma. Do NOT build β this round.

### smooth-window-crash (NEW): CHANGES REQUESTED

- Technique (smooth-number distribution in the mtp-window): genuinely analytic, far from the others. Registered.
- Step 1 (import SPT + free-rider): **free-rider must be dropped.** The approach can survive without it — the crash needs a smooth valid number that is a tight (minimal-transversal) new minimal, not a free-rider.
- Step 3 (smooth-window crash lemma): the core claim — "p*-smooth valid numbers are forced into the window." Two risks the outliner flags: (1) smooth numbers become sparse for large a_n (the window length G*≤R=primorial(p*) is huge for large p* but only 2 for p*=2); (2) "valid AND smooth" simultaneously is not guaranteed by density alone — the smallest-first dynamics must force the coincidence. This is the genuinely different angle and its open core.
- Step 4 (smooth minimal dominates fat minimals): needs the smooth minimal to be a subset of, or refined-from, the fat ones. Not automatic.
- **Collapse risk with α.** α's SPT-density crash (step 6) and smooth-window-crash's step 3 both argue "a small-support valid number lands in the window." α uses structural SPT-density; smooth-window uses analytic smooth-number density. These are related but distinct justifications (structural vs analytic). If both reduce to "smooth numbers are dense in intervals of length mtp," they collapse. Flag: the builder must keep the analytic mechanism genuinely independent of α's structural one, or this approach is a duplicate.
- **Verdict: CHANGES REQUESTED.** The analytic angle is worth one builder. Drop free-rider (false). The crash must be about tight-minimal arrival, not free-rider fatness. Flag the sparsity risk and the α-collapse risk for the builder to address.

### transversal-single-cycle-finish (δ): hold (certified absorber)
No changes. Conditional theorem certified. Pairs with any wall-closer. Not in the build set.

### omega-induction-loaded (ε): RETIRE (fold) — agreed
ε's s_n-ascent reduces to SPT (not a rival). The ω-only variant is DEAD (round 2). Retired; not built. Outcome: dead-end (folded into α's SPT sub-argument).

## Diversity check (single-gap-trap guard)

**GAP-1 (SPT, mtp≤R): shared by ALL four approaches.** This is the intentional convergent target (0-violation, 280 seeds). If SPT is unprovable or false, all four die. This is an accepted risk — SPT is the data-backed real lemma. BUT: only α (primary) and γ (backup, permanent-2-transversal route) attempt an SPT proof; β and smooth-window-crash import it. **Recommendation: instruct γ's builder to attempt the backup SPT proof in parallel with α, so the linchpin is attacked from two angles, not one.**

**GAP-3 / crash diversity (after dropping free-rider):**
- α: SPT-density → tight-minimal arrival (static-structural). Genuine.
- γ: τ/avoiding-transversal-counting (dynamic-combinatorial). Genuine, but re-blocked by free-rider failure (unique-connector returns) + unbounded avoiding space.
- β: cofactor+bounded-promotion-count+Dickson (arithmetic+WQO). Genuine mechanism, but RETHINK (no non-circular a_n handle).
- smooth-window-crash: smooth-number distribution (analytic). Genuine, but collapse risk with α.

The four mechanisms are genuinely different AT THE CRASH STEP (structural / combinatorial / arithmetic / analytic). But α and smooth-window-crash risk collapsing (both: "small-support valid number in the window"). γ's crash is the most damaged (re-blocked). β is RETHINK. **The field has real diversity at the crash step but SPT is the single upstream dependency — the true single-gap-trap.**

**Free-rider was a false shared lemma.** Its removal is a DIVERSIFICATION event: the crash is now correctly understood as tight-minimal arrival (harder, but each approach must find its own mechanism for it, rather than all leaning on the same false shortcut).

## Ranking (head-to-head, anchored to last outcomes)

Post-update Elo: δ 1636 (verified-milestone) > α 1584 (advanced) > smooth-window-crash 1500 (new) > β 1461 (partial, RETHINK) ≈ γ 1456 (advanced, re-blocked) > ε 1362 (retired).

Key comparisons: δ beats all (certified milestone, only fully solid line). α > γ (freeze solved + SPT home + more progress, despite free-rider failure in both). γ drops to ≈β level (its crash is re-blocked; β is RETHINK but has a different mechanism). smooth-window-crash enters at cold-start 1500, drawn with γ (both CHANGES REQUESTED, γ has more machinery but re-blocked crash). ε retired at the bottom.

## Build set

Three builders, each attacking the wall from a genuinely different crash mechanism, all attempting the SPT linchpin or the crash:

- **α** — prove SPT (the linchpin, step 3); drop free-rider (false); reframe crash (step 6) around tight-minimal arrival. Most credible path.
- **γ** — certify τ monovariant (step 4, provable); attempt backup SPT proof (permanent-2-transversal route, step 2 alternative); honestly assess whether the avoiding-transversal crash survives without free-rider.
- **smooth-window-crash** — outline+attack the smooth-window-crash lemma (step 3, the analytic core); drop free-rider dependency; address smooth-number sparsity at large a_n; keep the mechanism independent of α's structural SPT-density.

β is RETHINK (sent back to outliner for a non-circular a_n handle or fold). δ held. ε retired.

build set: density-promotion-bound, bounded-gap-lcm-reduction, smooth-window-crash
