# Outline review — imo-2026-05 (IMO 2026 P5), round 1

Answer confirmed: f(x)=x+c for every c≥0. All four approaches correctly target the **full family**
(sufficiency + rigidity), not f=id alone — good. I re-verified the shared skeleton in sympy:

- Sufficiency: for f=x+c, both `(f(x)+y)²−4x f(y)` and `2(x²+f(y)²)−(f(x)+y)²` factor to `(x−y−c)²≥0`. ✓
- (★) f(f(y))=2f(y)−y from x=f(y) (sandwich collapses since QM=GM at equal args). ✓
- Off-diagonal lever (∗): `(a+g(a)+b)²−4a(b+g(b)) = (a−b)²+2(a+b)g(a)+g(a)²−4a g(b)`. Exact. ✓

So the three "cheap" shared facts (★, injectivity via (★), f≥id from orbit positivity, g orbit-invariant)
are genuinely rigorous and can be a certified shared lemma.

I also checked the **interleaving crux** (`all-positive-defects-equal`) by hand: for g(a)=s_a>0, g(b)=s_b>0,
pick A=a+k·s_a→∞ in O(a) and B∈O(b) with B≤A, A−B<s_b; (∗) at (A,B) gives 4A·s_b ≤ s_b²+4A·s_a+s_a²;
÷4A, A→∞ ⇒ s_b≤s_a; symmetric ⇒ equal. This is airtight. Steps 1–4 of the orbit route are a real proof.

## Note to the builder — the residual gap CLOSES cleanly (do not treat it as open-ended)

After Step 4, g:R>0→{0,c}. Let Z={g=0}, P={g=c}, c>0. The only cross-constraint is (R) at (z,b), z∈Z, b∈P:
`(b−z)² ≥ 4cz`. This immediately makes **both Z and P open**:
- Any zero within δ of b∈P would give (b−z)²<δ² but 4cz≈4cb>0 — impossible for small δ. So a neighborhood
  of every b∈P is zero-free ⇒ **P open**.
- Symmetrically, no P-point lies within 2√(cz) of z∈Z, so a neighborhood of z is all-Z ⇒ **Z open**.

Z⊔P=R>0 is a partition into two open sets; (0,∞) is connected ⇒ one is empty ⇒ g is constant (0 or c).
This retires the sole gap without the fuzzier "P dense / not separated" language in the outline — the builder
should use the openness+connectedness argument. Recommend caching (★)/injectivity/f≥id and (∗) as a shared lemma.

## Verdicts

**orbit-interleaving — APPROVE (leader; essentially a complete proof).**
Steps 1–4 verified rigorous above; the residual `no-fixed-point` gap closes by the openness+connectedness
argument above. Only fixable items: (i) write sufficiency's c≥0 necessity explicitly (c<0 fails positivity at
small x); (ii) confirm both orbits are truly infinite in Step 4 (needs s_a,s_b>0 — zeros correctly quarantined
to Step 5); (iii) replace the Step-5 "P dense enough" hand-wave with the clean openness argument. Build it.

**mixed-defect-contradiction — CHANGES REQUESTED, but NOT in the build set.**
Sound, but its Step 3 interleaving IS orbit-interleaving's Step 4 and its Step 4 IS orbit-interleaving's Step 5
— same crux, same wall, same residual gap. This is the single-gap-trap sibling of the leader, not a distinct
framing. Its one genuine extra is the explicit c₂=∞ handling (fold that observation into orbit-interleaving
instead). Kept in the population, ranked just under the leader (its Steps 1–4 are as rigorous), but building it
would put two builders on one wall — excluded for diversity.

**convex-duality — CHANGES REQUESTED (far-framing hedge; build).**
Genuinely different machinery (Legendre conjugate in a=√x), so it does not share the orbit wall — valuable for
field diversity. Real concerns the builder must resolve, not wave through:
- `conjugate-tight` (Step 3): equality in (R) holds only at x∈image(f)={y+g(y)}; must justify tightness at
  **every** a>0 without assuming surjectivity. Do this via (★) directly, not by asserting the image is cofinal.
- Step 5 "extract affineness" is currently an assertion ("must satisfy the exact relation"). The "convex tight
  against conjugates from both (R) and (L) ⇒ affine" step is the whole proof and needs a real mechanism (name
  the convex-analysis fact, e.g. a convex function equal to its biconjugate with matching upper/lower support).
Approve to build as a diversity hedge, but the reviewer will hold it to closing Steps 3 and 5 concretely.

**monotone-continuity — CHANGES REQUESTED (far-framing hedge; build).**
Different framing again (order/topology; earns continuity rather than assuming it — correctly flagged as the
whole point). Concerns:
- Step 2 `f-increasing`: "pin the gap" between the increasing lower envelope and slower upper envelope is not
  yet an argument. Make precise which of (R)/(L) forces the order.
- Step 3 `f-continuous`: "a jump breaks the squeeze" must be a concrete inequality violation, and the countable
  jump set must be shown **empty**, not merely small.
- Step 4 `g-constant`: note it can borrow the leader's result g∈{0,c} to shortcut, but as a standalone framing
  it needs the local-constant⇒global upgrade spelled out.
Build as the second diversity hedge.

## Field diversity

Three genuinely distinct walls in the build set: orbit-AP interleaving (leader), convex conjugate duality, and
order/continuity. mixed-defect-contradiction is a fourth registered member but is a re-skin of the leader (same
crux + same gap) — flagged so the orchestrator does not mistake it for independent insurance. The leader's gap
already falls to a clean topological argument, so the field is not plateaued; the two hedges guard against a
writeup snag in the orbit route.

## Ranking (Elo after this round)
orbit-interleaving 1546 > mixed-defect-contradiction 1515 > monotone-continuity 1471 ≈ convex-duality 1467.

build set: orbit-interleaving, convex-duality, monotone-continuity
