# Certified lemmas: Fresh-Prime Rescale-Witness (the crux-closing lever)

Certified by proof-reviewer, round 7. These close the Finite-Alphabet crux of imo-2026-06
unconditionally. Both `key-term-first-appearance` (§2–§5) and `redundant-constraint-antichain` (§15)
proved them independently; the reviewer re-derived every step from scratch and numerically confirmed
the load-bearing claims. Notation: `P(x)` = set of primes dividing `x`; `Q = P(a₁)`, `q₀ = max Q`,
`C = q₀·a₁`. Depends only on the certified free lemmas L1–L4 (`free-lemmas.md`) and the greedy rule.

---

## Lemma FA (Forward-admissibility)
For an integer `c > a₁`: `c` is a term ⟺ `gcd(c, a_i) > 1` for every term `a_i < c`.

Whether `c` is a term is decided purely by the terms already emitted below `c` — a local criterion
derived directly from the greedy rule, needing no global admissible set. (Proof: §2 of
`key-term-first-appearance`; = §15.1 of antichain. (⇐) uses L2 growth + minimality in the greedy
definition; (⇒) is L4.) **Reviewer status: airtight.**

## Lemma DOM (Domination) and DIST
Define **key terms** by first occurrence: `aₙ` is key ⟺ no earlier key term `b` has `P(b) ⊆ P(aₙ)`.
- **DOM:** every term `aₙ` has a key term `b` of index `≤ n` with `P(b) ⊆ P(aₙ)`.
- **DIST:** distinct key terms have distinct supports.
(The antichain "no earlier *term* dominates" variant is equivalent — antichain Lemma 15.2a — and
gives `𝓐_∞ ⊆ {key supports}`, Lemma 15.2b.) **Reviewer status: airtight.**

## Lemma RW (Fresh-Prime Rescale-Witness) — THE LEVER
A prime `p` is **fresh at** a key term `x` if `p ∈ P(x)` and `p ∉ P(b)` for every earlier key term
`b`. Then: **no key term `x > C` contains a prime fresh at `x`.**

*Proof sketch (full proof: §4 key-term / §15.3 antichain).* Suppose `x = a_m` key, `x > C`, `p`
fresh. `a₁` is an earlier key term so `p ∉ Q`. Pick anchor `q ∈ P(x)∩Q` (L4), `q ≠ p`, `q ≤ q₀`. With
`S = P(x)∖{p}`, `r = ∏S`, build `y ∈ [a₁, x)` with `P(y) = S`: if `r ≥ a₁` take `y = r < rad(x) ≤ x`;
else `y = r·q^t` for least `t` with `y ≥ a₁`, giving `y < q·a₁ ≤ C < x` and `P(y) = S` (multiplying by
the anchor `q ∈ S` adds no prime). Then `y` is a term: for every term `a_i < y`, DOM gives an earlier
key term `b` with `P(b) ⊆ P(a_i)`; L4 gives a shared prime `w ∈ P(x)∩P(b)`, and freshness forces
`w ≠ p` so `w ∈ S ∩ P(a_i)` — by FA, `y` is a term with `P(y) = S ⊊ P(x)` and `y < x`, contradicting
`x` key.

**Two guardrail-critical, load-bearing distinctions (verified by reviewer):**
- **Fresh, not `p_max`.** Freshness gives `p ∉ P(b)` for the dominating key term `b`, so its shared
  prime with `x` is a genuine element of `S`. Removing `p_max` instead could leave a private-witness
  term (sharing only `p_max` with `x`) unmet — the certified R5/JSC-E3 obstruction. The removal prime
  MUST be fresh.
- **Local, not a transversal.** `y` need only meet the finitely many already-emitted terms below it
  (via FA), never a transversal of an infinite family — keeping the argument off the certified
  R4-Collapse guardrail.

**Reviewer status: airtight.** Independently re-derived; anchor existence and the `|P(x)|=1` edge case
(forbidden by L4) both handled; case split (Case A `r ≥ a₁` / Case B `r < a₁`) exhaustive.

## Corollary (Finite Alphabet crux — CLOSED)
Let `K = ⋃{P(b) : b key, b ≤ C}` (finite). Every key support `⊆ K` (least-index-violator argument via
RW), so `|𝓚| ≤ 2^{|K|}` by DIST; hence `Π = ⋃_{b key} P(b)` is finite. Thus `𝓐_∞` is finite and the
support alphabet `Π` is a finite set of primes — the crux that resisted six rounds.

## Numerical confirmation (reviewer's own simulation)
`a₁ ∈ {375, 385, 105, 9, 49}`: all key terms `≤ C = q₀·a₁`; zero mismatches in the
"term ⟺ meets every key term" characterization; `a₁ = 375 → q₀=5, C=1875`, six key terms
`{375,378,380,384,399,490}`, `Π = {2,3,5,7,19}`, `L = 3990`, `T = 852`, zero periodicity violations.
