# Proof-reviewer — round 2 — imo-2026-06

Reviewed both built approaches independently. Both are honestly labeled `partial`; neither claims
`solved`. Confirmed. The whole-problem crux (Π = ⋃𝓐_∞ finite, the "Finite Alphabet" statement)
remains open in both. I re-derived every new load-bearing step by hand and re-simulated with sympy.

Numerical checks (independent): greedy sequence for a₁∈{15,35,105,375,385,1155,2025,9375,867}.
- E1 (A∩[a₁,∞) = term set): holds exactly for a₁=375 over the whole computed range.
- E2(⇒) (each ⊆-minimal support is a ⊆-minimal transversal of 𝓐_∞): holds for a₁∈{105,375,385,1155}.
- E3 (private witness G_p with G∩G_p={p} for every (G,p)): holds for the same a₁.
- Reduced-crux bound q≤a₁: holds in every simulated case (max prime in a minimal support ≤ a₁,
  equality only when a₁ prime) — consistent with the builder's claim, but note the a₁∈{867,9375}
  runs are truncated (400 terms), so their large "minimal supports" are provisional; this only
  supports the OPEN target, it does not establish it.
- Density monovariant (a₁=375): 0.467→0.410→0.283→0.274→… non-increasing, floor 1/M=1/15. ✓
- Max-gap monovariant (a₁=375): 3→3→6→6→… freezes at 6, bounded by M=15. ✓
- Obstruction family density 1/p*+(1−1/p*)∏1/q_k: p*=2 gives 0.667→0.533→0.505→… → 1/2. ✓

---

## Approach 1: redundant-constraint-antichain

**Verdict: CHANGES REQUESTED. True Status: partial (correctly labeled).**

Scores — Correctness 10/10 (everything written is valid); Rigor 9/10 (crux honestly open, no
hand-waving in the proved part); Progress: real — three new unconditional lemmas that sharpen the
sole gap to a single tight inequality.

What I verified line by line:
- **E1 (Enumeration).** ⊆ from no-transient lemma + monotonicity; ⊇ by the maximal-index argument
  using a_{n+1}=s(a_n). The "n:=max{k:a_k≤c} exists and a_{n+1}>c" step is valid (a_n→∞, a₁≤c).
  Rigorous.
- **E2 realization preliminary + E2(⇒).** Preliminary: B meets each G'⊆F(a_j) ⇒ m∈A ⇒ (E1) m is a
  term. Correct. E2(⇒): transversal by L4; minimality by realizing any proper transversal subset as
  a term support ⊊ G, contradicting minimality of G. Correct. The builder explicitly flags that
  "every minimal transversal is finite" is NOT settled and NOT used — honest, not an overclaim.
- **E3 (Private-witness distance).** G minimal transversal ⇒ G∖{p} misses some G_p∈𝓐_∞ ⇒
  G∩G_p={p} ⇒ gcd(t,t')=p^m ⇒ (L3) p≤|t−t'|. Correct and unconditional.
- **Reduction.** Crux ⟺ primes in minimal supports bounded: trivial and correct.
- Non-circularity confirmed: only §4–§5 (endgame) use the finiteness hypothesis; §9 lemmas are
  unconditional.

**The precise remaining gap (name the step):** the **Reduced Crux** — "every prime occurring in a
⊆-minimal support satisfies q≤a₁" (equivalently the E3 witness distance |t−t'|≤a₁ for private-
witness pairs). §9.4 explicitly leaves this unproved; it is the sole open step. Self-blocking (E2)
alone admits infinite abstract clutters, so closing it must use E1-realizability plus an
a₁-anchored distance bound not yet found. Correctly identified as the honest locus.

Certified lemmas (moved to `lemmas/enumeration-and-transversal.md`): **E1, E2(⇒), E3** — all hold
the full bar (sorry-free, unconditional, statements no stronger than proved, verified numerically).
E2's converse and "minimal transversal ⇒ finite" NOT certified (builder didn't claim them).

## Approach 2: monovariant-witness-descent

**Verdict: CHANGES REQUESTED. True Status: partial (correctly labeled).**

Scores — Correctness 10/10; Rigor 8/10 (the two monovariants and the concrete obstruction are
rigorous; the meta-slogan is heuristic, see below); Progress: a genuine, well-tested negative
result that redirects the route, plus two certified monovariants.

What I verified:
- **Lemma A (density).** Non-increasing under inclusion of periodic sets; ≥1/M via multiples of M
  (L1); equality ⟺ A_{n+1}=A_n via density ≥1/D_{n+1} of a nonempty residue union. Correct.
- **Lemma B (max-gap).** ≤M (multiples of M present); non-decreasing (deleting points only enlarges
  gaps); integer + bounded ⇒ freezes. Correct.
- **Obstruction.** The concrete family G_k={p*,q_k} is a valid intersecting anchored clutter with
  infinite Π on which density→1/p* and max-gap freezes ≤p*. Density formula verified. Rigorous.

**Caveat I am recording (not a fatal flaw, but the Status labeling must reflect it):** the broad
claim "*no* monovariant that is a function of A_n alone can prove the Crux" is a heuristic reading
of the concrete family — there is no formal definition of "monovariant," so it is not a certified
impossibility theorem. The builder's prose occasionally states it as if proved ("a *proved*
meta-obstruction"). The **concrete witness family is rigorously proved**; the universal
impossibility is not, and should be read as a strong cautionary heuristic. I certified only the
concrete content, with this caveat noted in the lemma file. This does not change the verdict
(partial either way) but the "proved that no A_n-only monovariant can work" phrasing is a mild
overclaim of a heuristic as a theorem.

**The precise remaining gap:** G-dyn — the Crux (Π finite) is unclosed; this route establishes it
CANNOT be closed by an A_n set-statistic and points to a monovariant on the greedy choices a_n
(via L3 on chosen values), which is "not yet found." Honest.

Certified lemmas (moved to `lemmas/monovariants-and-obstruction.md`): **density monovariant A**,
**max-gap monovariant B**, and the **concrete obstruction family** (as a negative result, with the
heuristic caveat on the universal claim).

---

## Cross-cutting

- Both routes now share the same wall (bound the primes in minimal supports / forbid the p*-family).
  Antichain sharpened it to a clean q≤a₁ inequality; monovariant proved A_n-statistics are blind to
  it. Per the plateau rule this is the moment to seed a genuinely different framing that reads the
  greedy CHOICES a_n (e.g. an a₁-anchored distance bound on E3 witness pairs, or a descent on the
  least newly-recruited large prime) — the two live routes have converged onto one gap.
- No M-threshold reappears (antichain bounds by a₁, not M=rad(a₁)); consistent with the R1
  refutation (a₁=375: 19∈Π, 19>M=15 but 19<a₁).

## current.md
Updated (Status stays partial; both approaches' progress and the two new certified lemma files
recorded; monovariant obstruction added as a recorded negative result).
