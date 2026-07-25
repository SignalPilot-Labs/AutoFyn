# Outline review — imo-2026-06, round 3

Numerically vetted every crux sub-claim before ruling. Simulator uses the
antichain-of-minimal-supports admissibility characterization (c admissible ⟺ primes(c)
meets every ⊆-minimal support), N=6000 terms/seed, seeds {4,6,105,375,385,139,9375,15015}.
Antichains stabilized well before N (last change: 375→t26, 385→t38, 9375→t906, 15015→t1293),
so the measured limiting antichains are trustworthy, not truncation artifacts.

## Numerical findings (load-bearing)

**ERW window K (antichain §10) — TRUE, robust.** For every seed, every prime q in the
limiting antichain divides some term within K·M of a₁, with **K ≤ 0.33 across all 8 seeds**
(worst cases: 19 on a₁=375 and 67 on a₁=9375 both first divide a term at value a₁+5,
K=0.33). No seed even approaches the honest fallback K≈2. The ERW target is on very solid
numerical ground and — crucially — is a *different* quantity from the refuted K-real below.

**K-real (monovariant-witness-descent R3 target) — REFUTED.** The build target's wall lemma
is "every pending small companion S is realized by a term with F(a_j)⊆S in bounded time."
On **a₁=375** the limiting antichain contains G=[2,5,19] and G=[3,7,19]; their companions
{2,5} and {3,7} are **never realized as terms** (verified: no term has all prime factors in
{2,5}, none in {3,7}), yet both supports **persist** in 𝓐_∞. The mechanism is mutual
blocking: a pure-{2,5} number fails to meet [3,7,19], a pure-{3,7} number fails to meet
[2,5,19] — 19 is the shared private witness that keeps both companions permanently
unrealizable. Consequently the descent object Φ_n (# pending companions) **freezes at 2, not
0** — and a frozen-nonzero Φ_n is *exactly* the certified obstruction family {p*,q_k}
(companion {p*} never realized, Π infinite). So Φ_n cannot separate finite-Π from infinite-Π,
which is precisely what the route needs. K-real is not merely unproven — it is false.

## Verdicts

### redundant-constraint-antichain — APPROVE (advance; build)
Technique sound end-to-end: §1–§5 complete, endgame certified, E1/E2/E3 certified, and §10
reframes the sole gap as the ERW window inequality — a genuinely different top-level target
(formation-time bound, provable by bounded computation) from the size bound q≤a₁. ERW is
numerically robust (K≤0.33). The mechanism is stated with a real lever (E1 realizability +
E3 witness-pair localization + first-formation bound m<a₁+∏B), and the closing "exchange"
argument in the candidate finish is honestly flagged as the open quantitative step.
- Issues to close while building (§10): (i) prove the uniform constant K exists — the
  candidate exchange argument (a₁+K·M formation window) is the load-bearing step and is not
  yet an argument, only a sketch; make the "E1 would have realized a smaller-support term in
  between, violating ⊆-minimality" loop-closure rigorous or flag it as still-open. (ii) State
  K≈2 honestly (19>M=15 needs K>1); do NOT bound q by M. (iii) Cover |P|=1 (Π={p}) and
  |P|≥2; verify vs 105→T=58,L=210.
This is the leader and closest to a complete proof. Build it.

### value-stream-double-freeze — APPROVE (new; register + build)
Registered (Elo seed 1500 → 1515 after ranking). Genuinely distinct pole: dynamical
finite-automaton on the gap-word d_n, targeting periodicity directly, vs the antichain's
size/formation bound. Its load-bearing K3 (bounded active minimal supports per length-Γ*
window) is numerically plausible — |antichain| ≤ 7 and companions live in the finite pool
2^{primes≤M} on every seed — and, importantly, K3 does NOT rest on the refuted K-real.
- Issues (build): The real wall is the **SECONDARY gap (determinism)**: is s(a_n) a function
  of W_n alone? It is NOT obviously so, because large primes outside the window are
  load-bearing for admissibility — concretely 380=2²·5·19 on a₁=375 is admissible *only*
  via 19 (it fails companion {3,7}), so W_n=(a_n mod M; window supports) can miss the datum
  that decides the choice. The builder must either enlarge W_n to capture large-prime
  divisibility of the candidate (and show that stays finite-state) or prove such exceptions
  are sparse/non-binding. This is the speculative heart — flag it as the primary gap, above
  K3. Steps 2–3 are exploratory; expect partial, not solved. Still worth a build as the
  distinct pole.

### monovariant-witness-descent — RETHINK (do not build this round)
The R3 build target (per-small-companion-set descent, wall lemma K-real) is refuted above
(a₁=375: companions {2,5},{3,7} never realized, supports persist; Φ_n freezes at 2 not 0,
consistent with infinite Π). The descent object does not certify Π finite, so the route as
re-planned cannot close the crux. Its *earlier* certified content (Lemmas A, B, the
Obstruction Lemma in lemmas/monovariants-and-obstruction.md) stands and is untouched — only
the forward R3 plan is dead. Send back to the outliner: the "count pending companions → 0"
idea is holed by mutual-blocking steady states where a large shared witness keeps companions
permanently unrealizable while Π is nonetheless finite. Any revival must descend on a
quantity that stays bounded through such steady states (e.g. count distinct large primes
*directly* via an L3 spreading bound, not via companion realization).

### anomaly-count-terminates — dead (unchanged)
M-threshold confinement refuted (R1). Not on the table.

## Field diversity (plateau watch)
With monovariant off the build set, two live builds: antichain (order-theory /
formation-time window) and value-stream-double-freeze (dynamical automaton / gap-word cycle).
Different framings, different gaps: antichain's gap is the ERW formation constant K
(numerically TRUE); double-freeze's hard gap is automaton determinism under load-bearing
large primes (a genuinely different obstacle). **Shared-substrate risk to flag to the
orchestrator:** both benefit from a "bounded per-window / finite companion pool" fact
(antichain §8.4 ≈ double-freeze K3); this fact is itself numerically sound and finite-pool
trivial, so it is not the shared *wall* — the two walls (formation-time vs determinism) are
distinct, so a refutation of one does not sink the other. Field is acceptably far apart for
this round. If both stall next round on the large-prime/window interaction, the orchestrator
should re-seed a third framing that attacks the large-prime persistence mechanism head-on
(why a shared witness like 19 must be bounded), since that single arithmetic fact — a large
prime q sitting in two mutually-blocking supports — underlies both the ERW closure and the
double-freeze determinism.

## Ranking (this round)
redundant-constraint-antichain 1560.2 (leader, advance) · value-stream-double-freeze 1515.4
(new, live) · monovariant-witness-descent 1485.4 (R3 target refuted, RETHINK) ·
anomaly-count-terminates 1439.0 (dead). Stale flags cleared.

build set: redundant-constraint-antichain, value-stream-double-freeze
