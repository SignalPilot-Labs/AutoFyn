# Outline Review — imo-2026-06, Round 7

Context: 6-round structural plateau; the whole theorem is certified-equivalent to the Crux
(𝓐_∞ finite / Π finite). R7 put up a genuinely new lever — the **fresh-prime rescale-witness**,
sourced from the located official IMO-2026-P6 Solution 2, to be re-derived from scratch (not cited).
Two slugs ride it. I vetted the lever HARD (guardrail-collapse audit + full numerical counterexample
hunt) before gating.

## Verdict summary
- **redundant-constraint-antichain** — **APPROVE** (advance; closes Crux directly via new §15).
- **key-term-first-appearance** — **APPROVE** (new; self-contained bypass of E4/E5/E5″, same lever, different bridge).

Both build.

---

## 1. Does the lever secretly collapse to a forbidden guardrail? NO — the distinction is real.

I audited against every certified guardrail. The lever survives all of them, and the load-bearing
novelty (flagged by the explorer) is genuine:

- **Not JSC / spread bound (R5, dead).** y is built by *multiplying* the residual radical r=∏S by
  powers of a known small anchor prime q≤q₀≤a₁ until it lands in [a₁, q·a₁). It is never a difference
  |t−t′| of two realizers. No a₁-only spread inequality appears. Confirmed: the construction is
  r·q^t, verified mechanically (§below).
- **Not RBD / rejection-budget (R6, dead).** No rejection-stream accounting, no per-recruit disjoint
  cost sum. It is a single deterministic witness per hypothetical over-threshold key term.
- **Not R4 Collapse / sub-support realization (R4, dead) — THE CRITICAL CHECK.** R4's forbidden move
  realized a *common core* B of an ASSUMED-INFINITE sub-family via E2⇐ (transversality); it died
  because such a B is **not a transversal** of all of 𝓐_∞, so it cannot be realized that way. The
  fresh-prime lever escapes because it realizes y via a **different criterion — forward-realizability
  (meet-below), not E2⇐ transversality**: y is a term because it meets every term *below x* (a finite,
  already-emitted set), which **freshness of p** guarantees. Transversality of S is then a free *a
  posteriori* consequence (every term's support is a transversal), never something you must verify
  upfront for an infinite family. So the R4-Collapse guardrail's hypothesis ("realize a common core of
  an infinite family via growth/E2⇐") simply does not apply. The distinction — *per-candidate,
  meet-already-emitted-terms* vs *global common core, transversal-of-everything* — is load-bearing and
  real.
- **Not an A_n-only monovariant (obstruction, dead).** The argument reads the actual key terms
  selected and the actual term x — greedy choices, not A_n statistics. Consistent with R2's finding.
- **Not the M-threshold framing (dead).** No "p|L ⇒ p≤M" premise; primes >M are freely allowed in K
  (the finite pool is ⋃ supports of key terms ≤C, not primes ≤M).

**Fresh vs p_max — the outliner's correction is correct and necessary.** Removing p_max would revive
R5-JSC/E3: by E3, p_max has a private witness sharing only p_max with G, so the residual would fail to
meet that earlier term ⇒ not realized. Freshness is exactly the property that forbids an earlier term
from sharing only p with P(x) (an earlier term sharing only p is dominated by an earlier key term
containing p, contradicting freshness). The finiteness argument (step 6) only ever invokes the lemma
on a prime that is fresh by construction (the first key term with support ⊄K has a prime ∉K, which is
in no earlier key term). **The proof never needs p_max.** No JSC revival. This correction must reach
every builder (both slugs already carry it).

## 2. Numerical counterexample hunt — every step holds on data.

Seeds a₁ ∈ {375, 385, 867, 105, 9375, 9, 49} (composite, three-odd-prime 385, large 867/9375,
prime-powers 9/49). Independent greedy simulation, key-term first-occurrence filter.

- **Domination** (every term's support ⊇ some earlier key-term support): holds on all seeds.
- **No fresh prime fires above C=q₀·a₁** (the lemma's whole conclusion): TRUE on all seeds — the full
  key-prime pool equals K(≤C) exactly in every case. a₁=375 → K={2,3,5,7,19} = the run's independently
  certified L-primes (L=3990). Strong corroboration.
- **Forward-realizability** (step 3): for every c>a₁ up to the horizon, "c meets every term below c"
  ⟺ "c is a term" — **zero mismatches** on all seeds. This self-contained handle is exactly right.
- **y-window mechanics**: P(y)=S, a₁≤y, and y<q·a₁≤C (hence <x) whenever r<a₁ — all pass; the r≥a₁
  case gives y=∏S<∏P(x)≤x directly.
- **Prime-power seeds** (9, 49): single key term {q₀}, 𝓐_∞={{q₀}} trivially finite — the fresh-prime
  case never fires, as the outline's separate disposal predicts.

No step is contradicted by any concrete instance. The lever is not merely plausible; it produces the
exact certified answer on the run's own test case.

## 3. Load-bearing lemmas and remaining gaps (fixable during build, not fatal).

Each hard step has a stated mechanism; the gaps are re-derivation work, not holes in the strategy:
- Step 3 forward-realizability — greedy-successor-is-least-admissible mechanism, numerically exact;
  builder proves directly from the greedy rule (do NOT route through global A if E1 friction appears).
- Step 2 key-support = 𝓐_∞ — first-occurrence + domination; the ⊆-minimal ⟺ key equivalence must be
  written out (builder gap c).
- Step 5(iii) y realized — the freshness argument over all earlier terms (key + dominated-non-key);
  the mechanism is correct as audited above (builder gap b).
- Step 5(iv) minimality contradiction — y a term with P(y)=S⊊P(x), y<x ⇒ x dominated by an earlier
  key term ⇒ contradiction. Non-circular (does not presuppose the Crux).
- Window bounds in both r-cases (builder gap d) — mechanics verified numerically.

CHANGES-level items for the builders (not blockers): (i) the leader must close the Crux DIRECTLY in
§15 and leave the certified E5″/p_max chain as untouched legacy — do NOT try to route the fresh-prime
argument through E5″ (that framing is p_max-shaped and would reintroduce the JSC obstruction);
(ii) the key-term slug must actually re-verify the endgame re-instantiation with Π' (=⋃ key supports),
not assume the no-transient/Reduction lemmas port unchanged.

## 4. Single-gap-trap decision — KEEP BOTH (justified hedge).

The two slugs share the identical core lever, which is normally the single-gap trap. I keep both,
deliberately, because: (a) this is the sole live opening after a 6-round certified plateau; (b) the
lever is from the official solution and is now numerically airtight on every step; (c) the risk in a
re-derivation is at the **bridge**, and the two slugs are genuinely different there — the leader must
reconcile the new §15 with the legacy static-𝓐_∞ / E1-global-A / E5″ apparatus (friction risk with the
p_max framing), while `key-term-first-appearance` is a clean-slate dynamic proof importing ONLY the
certified free-lemmas + no-transient endgame and never touching E4/E5/E5″. If the leader's bridge
snags on legacy reconciliation, the clean-slate slug still stands. My HARD vet of the shared lever
(sections 1–3) is the "vet the shared lever once, up front" the single-gap rule calls for; with the
lever cleared, double-investing on two independent bridges is the right hedge, not redundant effort.

## 5. Ranking (updated; K=32, anchored to last outcomes).

New slug registered at cold-start 1500, then ranked head-to-head across the whole field.
- redundant-constraint-antichain **1714.8** (live leader, advance, full certified chain + endgame).
- key-term-first-appearance **1561.8** (new, live; same vetted crux-closer, cleaner bridge, but
  cold-start with unverified endgame re-instantiation — narrowly behind the leader, clear of all dead
  poles).
- realizer-index-joint-double-count 1523.7 (dead), joint-recruitment-budget 1513.1 (dead),
  residual-anchor-peeling 1488.8 (dead), value-stream-double-freeze 1437.5 (dead),
  anomaly-count-terminates 1332.0 (dead).

Both live approaches now sit clearly above the dead field, reflecting that the round finally has a
non-forked opening.

build set: redundant-constraint-antichain, key-term-first-appearance
