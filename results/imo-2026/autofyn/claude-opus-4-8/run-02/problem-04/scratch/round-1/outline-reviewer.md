# Outline review — imo-2026-04 (Mulan's Triangle Game), round 1

## Answer check (both directions)
Conjectured answer **θ = 180°/n, integer n ≥ 2** (θ divides 180 an integral number of times).
I verified both directions numerically before ruling:
- **Necessity** (θ∤180 ⇒ Shan-Yu survives): 0 both-bad events over 50k random good-triangle
  moves for θ ∈ {100,120,50,80,17,73,25,44}. Lemma A's algebra is airtight (see below).
- **Sufficiency** (θ=180/n ⇒ Mulan wins): the alignment cut making both children carry a
  multiple of θ exists for every random triangle, all n=2..12 (0 failures / 3000 each).
- Consistency: 180/n ≤ 90 for n≥2, so the θ>90 exclusion is automatically compatible; n=2
  gives θ=90 (winning via altitude), the boundary.
The answer and its characterization (both directions) are correct.

## Necessity mechanism — sound and essentially complete
The move algebra T1={x,β,180−β−x}, T2={α−x,γ,β+x} is correct (verified by re-derivation).
Lemma A's exclusion is valid: with residues a,b,c,S mod θ and t=x mod θ, T1 bad ⟺ t∈{0,S−b},
T2 bad ⟺ t∈{a,−b}; both-bad forces one of a≡0, b≡0, c≡0 (from S−b=a ⇒ c≡0), or S≡0 — all
four excluded for a good triangle with θ∤180. "Good" (no angle a multiple of θ) ⇒ no angle =θ,
and good is forward-closed, so Shan-Yu survives by keeping a good child every move. This is a
genuine, complete necessity argument, not a hand-wave.

## Sufficiency mechanism — sound modulo one shared gap
Alignment (Lemma B) + peel (Lemma C) is a valid forced-win construction: after alignment
Shan-Yu keeps a child with an angle mθ (2≤m≤n−1); peeling with x=(m−1)θ forces mθ→(m−1)θ (the
θ-child is an immediate Mulan win, so Shan-Yu keeps the (m−1)θ child), terminating at 2θ where
BOTH children carry θ — a forced double-fork win. Verified. The one real remaining gap is **G1:
range-existence of the alignment cut x∈(0,α) with the required residue** (the pigeonhole over
the three vertex windows summing to 180=nθ), including acute triangles at n=2. This gap is
shared by all three approaches — the field's single wall — but it is constructive, low-risk, and
numerically always satisfiable.

---

## Verdicts

### residue-invariant — APPROVE (top build)
Cleanest framing; necessity fully reduced and essentially proven (Lemma A); sufficiency reduced
to alignment+peel. Build tasks:
- Close **G1**: write the range-existence pigeonhole rigorously (some vertex admits x∈(0,α) with
  x≡−β mod θ), handling the labeling and the n=2 acute case. This is the load-bearing gap.
- **G3**: write the "good child stays good" closure explicitly (untouched base angle keeps its
  nonzero residue; sum stays 180 so S≠0 persists).
- State the explicit generic initial triangle Shan-Yu picks for necessity (θ∤180 ⇒ finitely many
  multiples of θ in (0,180) to avoid).

### geometric-forcing-extremal — APPROVE (second build)
Genuinely adds one distinct sub-mechanism: the **proven non-obtuse invariant** for θ>90 (the two
children's large third-angles sum to 180 ⇒ at most one >90 ⇒ a non-obtuse child always exists).
This is a real independent idea, not just a restatement, and it makes the raw-degree presentation
worth building as an independent check. Note honestly: Lemma D (θ≤90 non-divisor necessity) is the
SAME complementarity as Lemma A, in raw degrees — that is fine as an alternative write-up. Build
tasks: (G1) exhaustive 6-slot case enumeration for Lemma D; (G2) justify/glue the θ=90 split
between the non-obtuse engine and Lemma D; (G3) the shared alignment range-existence.

### q-linear-independence — CHANGES REQUESTED (registered, not built this round)
Not doomed, but the weakest and most redundant. Its necessity Lemma G/H is **the same
complementarity 180−β−x + β+x = 180 recast in ℚ-linear algebra** — the "genuinely different
mechanism" claim is overstated; it is a third dress on one idea, and the genericity-closure (G1)
is exactly the hand-wave-prone part the file self-flags. It stays in the population for sampling
diversity but is ranked lowest and is not in this round's build set. If pursued later it must (a)
give a precise finite-dimensional invariant with a real closure proof under cuts + discard, and
(b) show Lemma H is a firewall that does not also "prove" survival at θ=180/n. If G1 cannot be
nailed it should RETHINK toward the residue framing.

## Field diversity note (for the orchestrator)
The three approaches share the **sufficiency alignment+peel construction and its G1 gap** — the
field's single wall. Necessity is diverse only in that geometric-forcing adds the θ>90 non-obtuse
engine; for θ<90 all three use the same complementarity (and it is essentially proven, so this is
acceptable, not a stall). The real risk sits on the shared sufficiency range-existence (G1). If
both builds stall on G1, next round put ≥1 approach on a different sufficiency construction (e.g.
a direct inductive/angle-bisection route to the 2θ double-fork) rather than the residue-alignment
cut. Necessity does not need a new framing — it is done.

## Ranking (Elo after this round)
residue-invariant 1531 > geometric-forcing-extremal 1500 > q-linear-independence 1469.

build set: residue-invariant, geometric-forcing-extremal
