# Outline review — IMO 2026 P6 (round 1)

## Headline finding (read this first)

**The entire field shares ONE crux: prove the essential-prime set E is finite.** All five approaches reduce to it:

- `crude-reduced-type` faces it as the "free-rider wall" (Step 7 / Lemma C).
- `essential-monovariant` attacks it head-on (the monovariant IS the E-finite proof).
- `covering-system-redundancy` faces it as "late primes are redundant mod L" (Lemma B), which is the free-rider dichotomy = E-finite.
- `translation-self-similarity` — the lift requires L = ∏E and the free-rider dichotomy, i.e. the same wall.
- `windowed-state-pigeonhole` — the window bound reduces to the essential-prime set (same wall) OR is circular in L.

This is a **single-gap collapse from round 1**: every approach dies together if the E-finite crux is unbreakable in this framing. The orchestrator should commission a **genuinely different framing** next round (e.g. a direct growth-rate/structural argument on the greedy itself, or an explicit family/construction angle) — not another variation of "stabilize reduced types mod a product of primes." I am fielding the two that attack the crux most directly, but the diversity warning stands.

## Numerics that re-frame the round's assumptions

- **E stabilizes by n=3 and never grows** (verified for a_1 ∈ {15,35,77,105,1001} over 500 terms). Max essential prime ≤ a_1 in every case. So E ⊆ {primes ≤ a_1} appears to be a TRUE, deep fact (equivalent to the problem's truth) — provable, but non-trivial. It is the crux, not a side detail.
- **The "transient" is a misdiagnosis.** For a_1=15 (T=8,L=30), a_1=35 (T=34,L=210), a_1=1001 (T=282,L=2002), a_1=105 (T=58,L=210), the identity a_{n+T}=a_n+L **holds from n=1** once T,L are chosen. The explorers' "long transient for 1001" was a long PERIOD (282), not a transient. So the problem's "for every positive integer n" is satisfiable with the periodic T,L directly — no transient absorption needed. Approaches must still PROVE no-transient (not assume from numerics), but the "load-bearing ambiguity" flagged for all five is largely defused. The cleanest route: the residue-walk transition φ is a cyclic permutation (bijection) on V, so the orbit is purely periodic from the starting state — no tail — PROVIDED the wall holds from n=1. Add this as a step.

## Per-approach verdicts

### crude-reduced-type — APPROVE (with CHANGES)
Sound skeleton, the most concrete scaffold. The finite-lattice stabilization (Steps 1-6) is standard and correct. The wall (Step 7) is the crux but is genuinely attackable.

**Changes the builder must make:**
1. **Modulus enlargement is mandatory, not optional.** The skeleton's L_0 = ∏_{p ≤ a_1} p is the RIGHT starting modulus (Q = primes ≤ a_1 captures all essential primes by the E ⊆ primes ≤ a_1 fact — which the wall proves). But the free-rider wall argument as written bounds "rescue primes by the frozen prefix max B = max(a_1,…,a_{N''})", and B can exceed a_1. The clean formulation: prove E ⊆ Q directly (the real crux); then free-riders (> a_1) are NEVER essential (dichotomy) and NEVER the unique shared prime, so they cannot rescue an invalid candidate — no enlargement needed. The frozen-prefix-bound sub-argument in the file is a reasonable ANGLE on this but must be written rigorously and must avoid the infinite-regress trap (re-stabilizing over a larger Q gives a larger N'', hence a larger B, hence a larger Q…). The regress terminates precisely because E is finite — so the argument must either (a) prove E-finite first (which is the crux, somewhat circular) or (b) argue directly that a free-rider q > a_1 is never the unique shared prime of any pair (the dichotomy), which sidesteps the regress. Route (b) is cleaner; pursue it.
2. **"For all n" / transient:** add a step proving the identity holds from n=1, via the bijection observation (φ is a cyclic shift on V_0, so the residue orbit is purely periodic from a_1's state, no tail) — once the wall holds from n=1. The wall must hold from n=1, not just n ≥ N''; argue the wall is index-independent (it depends only on the stabilized family F, which is frozen by a finite prefix, and the dichotomy is index-free).
3. **Step 10 lift:** verify the gap-sum = L_0 over one cycle (the cycle wraps exactly once). State explicitly.

**Not cut.** Top of the field. Build it.

### essential-monovariant — APPROVE (with CHANGES)
Correct target (the true essential set E and the small L = ∏E) and the right idea (a monovariant proving E stabilizes). This is the most direct attack on the shared crux.

**Changes the builder must make:**
1. **Design w_n concretely.** "min-of-set monovariant, to be refined" is the entire approach — if w_n is not defined with a proven monotonicity, the approach collapses into crude-reduced-type (which would still be progress, but loses the distinct contribution). The builder must produce a SPECIFIC w_n with a proof it is non-decreasing and bounded, OR honestly fall back to the crude lattice-stabilization and re-label the approach as a cleaner-L variant of crude. Do not leave Step 4 as an open design problem.
2. **Step 3 bound "E_n ⊆ primes ≤ a_1" is flagged wrong by the outliner.** Numerics say it is TRUE (E stabilizes with max ≤ a_1), but the proof is the crux. The monovariant must yield it; the witness-a_i-doesn't-have-p|a_1 objection must be resolved by the monovariant, not assumed.
3. **Transient:** same bijection step as crude.

**Not cut.** High ceiling, direct crux attack. Build it. If the monovariant cannot be designed this round, the builder should at minimum produce the cleaner-L version of the crude wall (still progress).

### translation-self-similarity — CHANGES REQUESTED (do NOT build this round)
The literal core mechanism is **provably FALSE**. I checked concretely:

> a_1=15, T=8, L=30. Lemma B claims A_{T+n} = L + A_n (allowed sets are translates). Take n=1: A_1 = {m>15 : 3|m or 5|m}. 30 + A_1 = {m'>45 : 3|m' or 5|m'}. But 51 = 30+21 ∈ 30+A_1 (21 div by 3), and 51 = 3·17 is coprime to a_3=20 (gcd(51,20)=1), so 51 ∉ A_9. The allowed SETS are not translates.

Yet min A_9 = 48 = min(30+A_1) — the MINS coincide even though the sets differ (the counterexample 51 lies above the min). So the right statement is **min-preservation** (a_{T+n+1} = a_{n+1}+L), NOT set-translation.

**Why it's not built this round:** the min-preservation is exactly the conclusion we're trying to prove. To make it a proof mechanism, the builder would need an independent reason the min is preserved. My analysis: the only viable route is "a_{n+1} hits every earlier a_i via an ESSENTIAL prime (free-rider dichotomy), and L = ∏E, so a_{n+1}+L ≡ a_{n+1} mod every essential prime, hence a_{n+1}+L still hits every a_i" — which is the crude/essential wall. So the lift **reduces to the shared crux**; the translation symmetry is a reformulation, not an independent mechanism.

**Action:** keep registered (live), but send back to the outliner to either (a) find a genuinely independent min-preservation argument (not via essential primes) or (b) re-label as a hybrid that explicitly imports the crude wall. Do not spend a builder slot until the mechanism is non-circular.

### covering-system-redundancy — CHANGES REQUESTED (do NOT build this round)
**Too close to crude-reduced-type — same framing, different vocabulary.** The "redundancy of late primes" observation is exactly the free-rider dichotomy: a free-rider prime q ∉ E has gcd(q, L)=1, so {m : q|m} mod L = all residues (q invertible mod L), contributing no constraint. This is the SAME wall as crude, restated in covering language. The approach does not escape the E-finite crux and adds no genuinely distinct mechanism (the outliner's diversity table notwithstanding).

**Action:** keep registered, but ask the outliner to either differentiate the load-bearing mechanism from crude's lattice-nesting (currently both prove the same dichotomy) or merge it into crude as a lemma. Not built this round.

### windowed-state-pigeonhole — RETHINK (cut, not registered)
Two fatal issues:
1. **Window bound is circular.** Lemma A claims a_{n+1}−a_n ≤ W(a_1) independent of n. The only honest source of such a bound is the essential-prime set (Jacobsthal-style: among 2^|E| consecutive integers, one is non-coprime to each fixed modulus simultaneously). That makes the window bound DEPEND on the E-finite stabilization — the same crux. Alternatively, a window bound in terms of L is circular (L is what we're proving exists). The outliner himself flags this as the likely fatal wall.
2. **Lemma B ("far terms captured by recent residues") is the hidden stabilization** — i.e. the same crux again. So windowed-state pays the crux cost twice (window + stabilization) with no independent gain.

The approach does not escape the shared crux and carries an extra circular load-bearing lemma. Not viable as a distinct framing.

**Action:** RETHINK — send back to the outliner. Suggested re-plan: either (a) reframe the window bound via Jacobsthal's function on the essential-prime set (becomes a variant of crude, not distinct — probably not worth a slot), or (b) find a genuinely independent window source (e.g. the greedy's own structure forces bounded gaps without naming E — this would be a real new framing worth fielding). (b) is the interesting direction; (a) is not.

## Copy request — DECLINED

The outliner asked to copy `crude-reduced-type` → `crude-reduced-type-witness` to pursue fill (b) (witness construction) in parallel with fill (a) (frozen-prefix bound). I decline, for two reasons:
1. **Nothing is proven yet.** The copy mechanism is for an approach that has *proved a shared prefix* and now faces two viable gap-fills. Round 1, the entire skeleton is unproven — there is no certified shared prefix to branch from. Branching now risks the single-gap trap (if the prefix has a flaw, both twins die together).
2. **Fill (b) is speculative.** "Witness construction bounding the candidate range" needs the candidate range to exceed the gap, which depends on V_0 / L_0 — likely circular or at least as hard as the wall itself.

The witness angle can be opened next round, after crude's prefix (Steps 1-6) is certified and the wall is confirmed as the live gap. For now, the builder of `crude-reduced-type` should pursue the cleaner route (b) dichotomy directly — no free-rider is ever the unique shared prime — which is closer to fill (a) but sharper.

## Registration / copy log
- REGISTERED: `crude-reduced-type`, `essential-monovariant`, `translation-self-similarity`, `covering-system-redundancy` (all cold-start Elo 1500).
- NOT registered (RETHINK, cut): `windowed-state-pigeonhole`.
- COPY: declined (see above).

## Ranking (post-update Elo)

| rank | slug | Elo | note |
|---|---|---|---|
| 1 | crude-reduced-type | 1546 | most concrete, sound scaffold, wall attackable |
| 2 | essential-monovariant | 1515 | direct crux attack; monovariant must be designed |
| 3 | covering-system-redundancy | 1485 | correct but not distinct from crude |
| 4 | translation-self-similarity | 1454 | literal mechanism false; reduces to crude wall |

Pairwise comparisons emitted (all anchored to promise/risk since round 1 has no outcomes): crude > essential, crude > covering, crude > translation, essential > covering, essential > translation, covering > translation.

## Build set

Two approaches this round (round 1; both attack the shared crux from different angles — frozen-prefix/lattice vs monovariant). Do not over-build on a single shared wall.

build set: crude-reduced-type, essential-monovariant

## For the orchestrator (next round)

The field has collapsed to one framing (finite-state mod ∏E + free-rider dichotomy). If round-2 builders do not break the E-finite crux, commission **at least one approach on a genuinely different framing** — not another "stabilize reduced types" variant. Candidates: a direct structural/growth-rate argument on the greedy recurrence itself; an explicit construction of T,L from the seed block without naming E; a sieve-density lower bound on admissible candidates. The shared crux is real but the current field will stall together if it is not broken.
