# Proof review — imo-2026-06, round 3

Two built approaches reviewed independently. The whole problem is (certified, prior rounds)
reduced — for ALL n≥1, no transient — to the single crux "Π = ⋃𝓐_∞ finite" (Finite Alphabet).
I re-derived every NEW load-bearing step this round from scratch and verified all numeric claims
with python (seeds 6,15,35,105,375,385,867,1155,2025,9375).

Numeric verification (independent simulation, admissibility ⟺ meets every ⊆-minimal support):
- a₁=375 minimal supports = {2,3},{3,5},{2,5,7},{2,5,19},{3,7,19}, Π={2,3,5,7,19}, max|G|=3 — matches both files.
- a₁=9375: 67∈Π, max|G|=4. max|G|≤4 on every seed. Self-blocking (members = minimal transversals) holds EXACTLY for 375 and 9375.

---

## Approach 1: redundant-constraint-antichain

**Verdict: CHANGES REQUESTED. Status: partial.** (Builder's recorded Status `partial` is CORRECT — no overclaim.)

### New content this round: E4 (Size-Bound Reduction). VALID.
Claim: `𝓐_∞` finite ⟺ `sup_{G∈𝓐_∞}|G| < ∞`.

I re-derived the substantive (⇐) direction from scratch (the Pigeonhole chain-descent, §11.2):
- Base: Anchor ⇒ every member meets finite P ⇒ pigeonhole gives p₁ in infinitely many members. ✓
- Case A (B_t a transversal): Lemma 11.0 gives a member G₀⊆B_t; every G∈𝓗_t ⊇ B_t ⊇ G₀, antichain ⇒ G=G₀, so 𝓗_t finite — contradicts (iii). So B_t is never a transversal. ✓
- Case B: each G∈𝓗_t meets W_t (E2⇒) in W_t∖B_t; pigeonhole extends the chain. ✓
- At t=C+1 a member of size ≥C+1 contradicts the size bound. ✓

Lemma 11.0 is sound: the ⊆-minimal transversal T'⊆T is globally minimal (any T''⊊T' lies in T),
finite, hence a member by E2(⇐). E2(⇐) is a one-line consequence of the *certified* realization
preliminary + Domination + E2(⇒) — I checked this derivation; it is present in the approach and sound.

**Adversarial non-vacuity check (the key attack): is E4 accidentally a false purely-combinatorial
claim?** No. E4's (⇐) genuinely uses E2(⇐) (arithmetic realizability) via Lemma 11.0. I tested the
obstruction family `{p*,q_k}` (bounded size 2, infinite): it FAILS self-blocking — `{p*}` is a
minimal transversal but not a member, so E2(⇐) fails and E4's hypotheses correctly exclude it.
Real greedy `𝓐_∞` DO satisfy E2(⇐) (verified for 375, 9375), so for real sequences bounded size ⟹
finite. E4 is correct and non-vacuous. **Equivalence is honest** (both directions hold), NOT a
circular restatement of "solved."

**Honest assessment of "progress".** E4 is a rigorously-proved NEW certified lemma, but it is a
*lateral* reformulation: Crux ⟺ finite ⟺ bounded prime-magnitude (R2's q≤a₁) ⟺ bounded |G| (R4).
All three are equivalent to the same open crux; E4 does not strictly reduce the difficulty, it gives
another equivalent target. The actual finiteness (the E5 gap) is fully OPEN. The §10 ERW window is
retained only as numerical motivation (K≤1/3), explicitly NOT asserted proved — correct labeling.

### Gap remaining (name the step): **E5 (Cardinality bound)** — prove `sup_{G∈𝓐_∞}|G| ≤ C` for an
a₁-computable C. Everything else (§1–§5 endgame, no-transient, E1/E2/E3, E4) is complete/certified.

Scores: Correctness 10/10 (E4 verified) · Completeness/rigor: partial (E5 open, honestly flagged) ·
Progress: moderate — a new certified equivalence, but lateral (same wall).

### Lemma certification
- **`size-bound-reduction.md` (E4): CERTIFIED.** Statement is exactly what is proved (no stronger),
  sorry-free, non-vacuity confirmed. Flipped PROPOSED→CERTIFIED; added a note pinning the E2(⇐)
  derivation to the certified realization preliminary (the file previously cited "E2(⇐)" as if
  literally in enumeration-and-transversal.md; it is an immediate consequence, now documented).

---

## Approach 2: value-stream-double-freeze

**Verdict: RETHINK. Status: unsolved (as an independent route — it provably collapses onto the crux).**
(Builder's recorded Status `partial` is technically defensible but MISLEADING: the round's own
K-equiv result shows the framing cannot be an independent pole. I route RETHINK.)

### K1′ — no new content.
"Π finite ⇒ theorem for all n, T=|ρ(A)|, L=∏Π" is the ALREADY-certified endgame
(`no-transient-fixed-successor.md`) re-derived. Correct but not new. The residue-count T=|ρ(A)|
matches antichain Corollary 11. Fine, but adds nothing.

### K-equiv — the load-bearing new claim. (⇐) trivial/certified; (⇒) NOT rigorous.
Claim: a finite-state deterministic value-stream automaton exists ⟺ Π finite.
- (⇐): W_n = a_n mod L₀ works. Sound (= the certified endgame). ✓
- (⇒): the proof asserts "a state that determines the output for all these [infinitely many
  load-bearing prime] choices must distinguish residues mod infinitely many primes, so it takes
  infinitely many values." This is a **hand-wave**, not a derivation. Moreover it is delicate:
  the theorem is TRUE, so d_n IS eventually periodic, so the trivial "position-in-period" automaton
  (W_n = n mod T for large n) ALWAYS exists — making "automaton exists" always true. The (⇒)
  argument does not confront this and is not rigorous.

**Is the "iff" honest, or a bypass/circular restatement?** It is neither a bypass nor progress: by
the builder's own conclusion (and Spec-concerns section), the automaton framing is *logically
equivalent* to Π finite and "cannot supply a Π-finite-avoiding pole." So as a distinct approach it
has **collapsed onto the shared crux** — exactly the single-gap trap CLAUDE.md warns against. It
provides no new machinery to attack Π-finite. The (⇒) proof's gap does not create a false `solved`
(nothing is claimed solved), but it does mean K-equiv is not fully rigorous.

### One correct small by-product (§4a): the A_n-obstruction family `{p*,q_k}` violates E2(⇒)
self-blocking, hence is not a realizable greedy `𝓐_∞`. I verified this (independently confirmed
above in the E4 non-vacuity test). Correct — but it is an immediate consequence of the *already
certified* E2(⇒), not new leverage.

Scores: Correctness: K1′ ✓, K-equiv(⇐) ✓, K-equiv(⇒) unrigorous · Completeness: n/a (route
collapses) · Progress: none toward Π-finite; it proves the route cannot bypass the crux.

### Lemma certification
- **K1′: NOT certified as new** — it is the already-certified endgame (`no-transient-fixed-successor.md`).
  No new file needed.
- **K-equiv: REJECTED.** The (⇒) direction is a hand-wave (see above), so it does not meet the rigor
  bar. (The honest meta-conclusion "automaton framing ⟺ crux" is a useful cautionary note, but not a
  certifiable theorem as proved.)
- **Self-blocking-excludes-obstruction (§4a): not separately certified** — it is a direct corollary
  of certified E2(⇒); no new lemma file created.

### Why RETHINK (not just CHANGES REQUESTED). The approach's sole new theorem proves the framing is
equivalent to the crux with no independent handle — it has bottomed out onto the same Π-finite wall
as the leader (self-admittedly). Per the plateau/single-gap-trap rule, this pole should go back to the
outliner for a genuinely different framing (e.g., attack large-prime persistence / the shared witness
mechanism head-on — why a prime like 19 sitting in two mutually-blocking supports must be bounded),
not re-derive the equivalence. The certified E2/monovariant content it leans on is untouched.

---

## Summary for the orchestrator
- Field now: one live leader (antichain, E4 certified, gap E5) + one pole routed RETHINK
  (value-stream collapsed onto crux). Both live framings reduce to Π-finite — the plateau the
  outline-reviewer flagged is real. Next round should seed ≥1 genuinely NEW framing attacking the
  large-prime-persistence arithmetic directly (the single fact underlying both walls).
- Certified this round: `lemmas/size-bound-reduction.md` (E4). Rejected: K-equiv.

---

**Verdict (redundant-constraint-antichain): CHANGES REQUESTED — Status partial.** Gap = E5 (bound |G|).
**Verdict (value-stream-double-freeze): RETHINK — Status unsolved.** Route provably collapses onto the Π-finite crux; send to outliner.
