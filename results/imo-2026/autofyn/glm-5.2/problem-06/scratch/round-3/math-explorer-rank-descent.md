# imo-2026-06 — rank-descent / termination-measure lens

Lens: a natural-number rank R(M_n) that is monotone-bounded or strictly descends, forcing finiteness of M (≡ the saturated-regime wall GAP-S). I tracked **every** plausible rank across the M_n evolution (at each promotion) on 13+ seeds: 15,21,35,105,175,187,221,231,273,323,385,429,667,141,147,153,19549, plus ~24 small odd composites (33–153). Transversal enumeration is full 2^|Pess| subset enumeration (no min-card shortcut); the fast method was cross-checked against the brute term-by-term greedy on 15,21,35,105.

## Distinct openings

1. **The four-monotone plateau.** mtp, τ (transversal number = min cardinality of a transversal), minAvSz (min cardinality of an AVOIDING transversal), and fixTr# (number of distinct traces M∩T* against the final mtp-witness T*) are **all monotone non-decreasing on every computable seed** (13 saturated + freeze seeds). But — critically — they all STABILIZE EARLY (within ~5 promotions) and promotions CONTINUE at the plateau (a1=429: 9 further promotions all at mtp=6, τ=2, minAvSz=2, fixTr#=3). So bounded-monotone does NOT force termination. This opening leads to a **plateau + crash** articulation, not a proof.
2. **minAvSz as the distance-to-termination coordinate.** minAvSz = None ⟺ no avoiding transversal exists ⟺ self-blocking ⟺ frozen (the certified Sat-criterion). So minAvSz reaching None IS the terminal event, and it is a monotone (conjectured) integer coordinate. The opening: prove minAvSz is forced to None. (See why it fails below — but it is the cleanest "rank" framing of the wall.)
3. **The crash event as the real driver (NOT a descent).** In every saturated seed the final act is a single promotion by a SMALL-support minimal (e.g. a1=429 step 55: a=675=3³·5², support {3,5}, refines away 7 large minimals at once → self-blocking). The monotone ranks are flat across the plateau; the crash is a smooth-number / smallest-first-dynamics event, not a descent. This points the outliner to a smooth-number-covering mechanism (a genuinely different route) rather than to any rank.

## Candidate technique(s)

- **Invariants & monovariants** (knowledge_base.md): the only provably-monotone ranks here are mtp (certified) and τ (provable: Trans(M_{n+1})⊆Trans(M_n) ⟹ min cardinality over the subset is ≥). Both stabilize, so neither is a descent-to-termination.
- **Pigeonhole/extremal** (knowledge_base.md): the crash is really a pigeonhole/smooth-covering event (small numbers ≤ a_n + mtp have small prime factors; eventually one is a minimal that refines the accumulated large-support minimals). This is the technique the crash needs — NOT a rank descent. The rank-descent lens confirms it cannot substitute.
- **min-transversal-product monovariant** (`mtp-monovariant-and-gap-bound`, certified): the sharpest gap bound; its boundedness (GAP-1) is exactly the wall this lens cannot close.

## Cheap-kill candidates

- **τ ≤ 2 in the saturated regime (CONJECTURE).** On every saturated seed τ stabilizes at exactly 2 (a 2-element transversal {2,p*} or {p*,q*} persists). On the freeze regime τ=1. A proof that τ never exceeds 2 in the saturated regime (i.e. a 2-transversal always exists once no prime is common) would be a real structural lemma — but it does not force M finite (τ=2 is reached in ~3 promotions and then flat). Worth proposing as a certified lemma but it is NOT a wall-closer.
- **fixTr# ≤ 2^|T*|−1 and reaches the full powerset of T* (CONJECTURE).** On every saturated seed the trace family vs the final witness saturates to ALL nonempty subsets of T* (fixTr#=3=2²−1 when |T*|=2). This happens by ~promotion 5, long before self-blocking. Saturated-trace is NOT self-blocking (9 more promotions happen at fixTr#=3 in a1=429). So trace-saturation is also not a wall-closer.

## Knowledge-base entries to use

- `mtp-monovariant-and-gap-bound` (certified): the monotonicity Trans(M_{n+1})⊆Trans(M_n) is the engine behind BOTH τ's monotonicity and (conjecturally) minAvSz's. Import; do not re-prove.
- `Sat-criterion` (certified): self-blocking ⟹ frozen. This is what makes "minAvSz = None" the terminal coordinate.
- `pairwise-intersection` (certified): the family is pairwise-intersecting; this is why τ≥2 in the saturated regime (no singleton transversal once no prime is common) and why LLL/inclusion-exclusion are vacuous — do NOT revisit.
- `common-primes-bounded`, `freeze-lock`, `singleton-freeze` (certified): the freeze regime (τ=1) is already solved; this lens only bears on the saturated regime (τ=2).

## Analogous past problems (cruxes)

- `aimo-0678` (IMO-SL 2015 NT; crux: min-of-a-set integer monovariant + bounded coordinate ⟹ lcm-reduce ⟹ finite-state ⟹ periodic). The bounded-coordinate lcm-reduction is the structural cousin of "minAvSz/τ bounded ⟹ finite-state," but the analogue's load-bearing step ("a_n | M" — bounded coordinate divides the reduction modulus) has NO exact P6 analogue: here the bounded coordinate is the gap/minAvSz, not a term value, and the greedy depends on M_n. γ's GAP-3 already attempted this template and hit the circularity. The rank-descent lens does not improve on γ's attempt.
- (No other crux is a close analogue for a monotone-rank-forcing-finiteness argument on an evolving antichain of supports; the corpus's monovariant cruxes are mostly "bounded monotone ⟹ stabilizes ⟹ finite-state," which is exactly what fails to terminate here because promotions continue on the plateau.)

## Prior progress

The field's best: the conditional transversal theorem (δ, certified) + the freeze regime solved end-to-end (α) + the mtp monovariant (γ, certified). The saturated-regime wall (GAP-S / GAP-1 / GAP-3, all convergent to "only finitely many primes enter minimals") is open. This lens CONFIRMS, by exhaustive measure-tracking, that no already-named rank closes it, and ADDS two new monotone coordinates (τ provable, minAvSz conjectural) plus the plateau+crash articulation.

## Dead ends (do not retry)

- **|M_n| (number of minimal supports) as a descent — DEAD.** NOT monotone: rises then crashes. Refuted a1=21 (1→2→1), a1=105 (1,2,3,4,5,4), a1=429 (1,2,…,12,5), a1=187 (1,2,3,4,5,6,5). Naive "supports shrink" is false: new minimals enter INCOMPARABLE to existing ones (a1=15: {3,5}→{2,3}→{2,5}, prime 2 enters via incomparable minimals, nothing refined away).
- **sum of |M|, prod of essential primes, |Pess|, #transversals, #minimal-transversals, #avoiding-transversals — ALL DEAD as descents.** Each is NOT monotone (same rise-then-crash shape). Refuting seed a1=105: prod_ess = 105,210,2310,2310,30030,210 (rises then crashes); a1=175: avoid = 2,6,8,2,0 (rises then falls). The crash is a single refinement event dropping all of these at once.
- **"avoid" (#avoiding transversals) as a descent — DEAD.** Reaches 0 at termination (self-blocking) but is NOT monotone: a1=175 avoid 2→6→8→2→0; a1=187 avoid 2→6→4→6→8→4→0. It goes UP before coming down.
- **minAvSz bounded ⟹ reaches None — DEAD (as a standalone argument).** minAvSz is monotone non-dec (conjecture) and bounded (≤3 on all saturated seeds), but it STABILIZES at a finite value (a1=429: minAvSz=2 for 9 promotions) without reaching None. Bounded monotone integer stabilizing does NOT imply reaching None. The transition minAvSz→None is the crash event, which needs a separate (smooth-number) mechanism. So "minAvSz monotone bounded" alone cannot close the wall.
- **trace-saturation ⟹ self-blocking — DEAD.** The trace family vs the final witness saturates (fixTr#=2^|T*|−1) by ~promotion 5, but self-blocking arrives much later (a1=429: step 5 vs step 55). Saturated traces do NOT block promotions.
- **τ (transversal number) as a descent-to-termination — DEAD.** Provably monotone non-dec, but stabilizes at 2 in ≤3 promotions and stays 2. Cannot force finiteness.
- **Cutoff artifacts mistaken for Sat-criterion violations (a1=141,147,153):** these show minAvSz "reviving" from None — this is NOT a real violation; it is my 14-prime enumeration cutoff firing in the FREEZE regime where |Pess| transiently hits 15–16 (a1=141: tau=1, mtp=3 constant, Pess grows to 16 then crashes to {3} at 243=3^5, the singleton freeze). Sat-criterion (self-blocking⟹frozen) is NOT violated. Do not treat these as counterexamples.

## Small-case / intuition notes (all CONJECTURE unless flagged certified)

- **mtp: MONO-INC, certified** (`mtp-monovariant-and-gap-bound`). Boundedness = GAP-1 (open). Stabilizes in ≤4 strict increases on every seed (a1=175: 5,5,10,14,21; a1=19549: 113,113,226 then flat for 26 promotions). CONJECTURE: in the saturated regime mtp stabilizes to 2·p* where p* is the smallest prime of a1 (a1=15→6=2·3, a1=175→21=3·7 NOT 2·5 — refuted; a1=429→6=2·3, a1=19549→226=2·113, a1=667→58=2·29, a1=187→22=2·11, a1=221→34=2·17, a1=385→14=2·7). So mtp = 2·(some prime of a1) EXCEPT a1=175 (=3·7, prime 3 enters). The entering-prime exception is exactly the wall.
- **τ (transversal number): MONO-INC (provable).** CONJECTURE: τ=1 in freeze, τ=2 in saturated regime, always (no seed has τ≥3). If true this is a clean lemma: in the saturated regime a 2-element transversal always exists.
- **minAvSz (min avoiding-transversal cardinality): MONO-INC (CONJECTURE).** Holds on all 13 saturated+freeze seeds where |Pess|≤14 (computable). Provability obstruction: Avoid(M_{n+1})⊄Avoid(M_n) in general (refining away a large minimal removes a constraint, potentially enabling a smaller avoiding transversal), so the subset argument that works for mtp/τ does NOT directly work for minAvSz; the monotonicity may be a true-but-nontrivial property of the greedy's smallest-first dynamic, not a transversal-lattice formality. Worth a dedicated proof attempt but NOT assume. Values: freeze→1; saturated→2 (occasionally 3, a1=385 reaches 3) then None at termination.
- **fixTr# (distinct traces vs final witness): MONO-INC (CONJECTURE).** Reaches 2^|T*|−1 (full powerset) in every saturated seed; stays 1 in freeze. The witness T* is the FINAL mtp-witness, so this is a retroactive measure; whether it is monotone against a TIME-VARYING witness (as needed for an inductive proof) is not established.
- **The plateau+crash structure (CONJECTURE, data-backed):** every saturated evolution has two phases. (a) Plateau-reach: ~3–5 promotions; mtp, τ, minAvSz, fixTr# all stabilize; a permanent 2-transversal T*={2,p*} (or {p*,q*}) emerges. (b) Crash: after a long flat plateau (9 promotions in a1=429, 26 in a1=19549), a small-support minimal appears (support ⊆ T*∪{one entering prime}, size 2) that refines away the accumulated large-support minimals en masse → self-blocking → frozen. The crash is the hard part; it is a smooth-number/pigeonhole event (among the small numbers ≤ a_n+mtp* the greedy is forced to pick one whose support is small), NOT a rank descent. **This is the sharpest articulation the rank-descent lens can offer the outliner: the wall is the crash, and the crash wants a smooth-covering argument, not a monovariant.**

## Verdict on the rank-descent route

**DEAD as a standalone wall-closer.** No natural-number rank both (i) is bounded and (ii) strictly changes forever (forcing termination). The four monotone ranks (mtp, τ, minAvSz, fixTr#) all stabilize early and then promotions continue on the plateau — bounded monotone stabilization does NOT imply reaching the terminal value (minAvSz=None). The non-monotone quantities (|M|, |Pess|, avoid, prod_ess, #transversals) rise then crash; they are not descents. **Termination is driven by the crash, which is a smooth-number/smallest-first-dynamics mechanism — a genuinely different route (smooth-number covering), not a rank descent.** 

What this lens CONTRIBUTES (for the outliner to wire into a different approach or as supporting lemmas):
- **τ monovariant** (provable, monotone non-dec; CONJECTURE τ≤2 in saturated regime) — a new certified-able structural lemma.
- **minAvSz monovariant** (CONJECTURE monotone non-dec; reaching None ≡ self-blocking ≡ frozen via certified Sat-criterion) — the cleanest "distance-to-termination" coordinate; a proof that it is monotone would be a real lemma, but it still would not alone force None.
- **The plateau+crash articulation** — tells the outliner the wall lives in the crash (phase b), which wants a smooth-covering / smallest-first-dynamics argument, NOT any monotone rank. This is the route to put on the table as the genuinely-different mechanism (per the run-state WATCH on single-gap-trap): a smooth-number-covering approach attacking the crash directly, rather than another variation of the saturation-reach framing.
