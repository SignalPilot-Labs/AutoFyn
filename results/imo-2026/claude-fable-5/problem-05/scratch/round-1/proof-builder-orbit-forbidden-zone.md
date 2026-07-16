# Build report — round 1, imo-2026-05, slug: orbit-forbidden-zone

## Outcome
Status: **solved** (claimed). Full proof written to `results/imo-2026-05/approaches/orbit-forbidden-zone.md`.

Answer: the solutions are exactly **f(x) = x + c for constants c ≥ 0**, verified (Part 1, both margins equal (x − y − c)²/4, QM–AM and AM–GM per `knowledge_base.md` "Standard inequalities") and uniqueness proved (Part 2) with no continuity/monotonicity assumptions.

## Gaps closed this round
- **GAP 1 (Step 2.5, two positive values a < b die).** Written in full: the f-image of the a-orbit is the AP {y₀ + (n+1)a}; a "within-one-step hit" sub-claim (well-ordering + Archimedean, with the n = 0 boundary sub-case handled — it forces f(y₀) = x exactly); explicit Archimedean threshold m > max{(y₀ + a − x₀)/b, (a²/(4(b−a)) − x₀)/b}; (L) then gives a² > 4(b−a)x, contradiction.
- **GAP 2 (Step 2.6, fixed points cannot coexist with h ≡ a > 0).** Written in full: (i) forbidden interval I(y₀) = (y₀ + a − w, y₀ + a + w), w = √(4ay₀ + 2a²), with |I(y₀)| > a since (2w)² − a² = 16ay₀ + 7a² > 0; (ii) AP-hits-interval with both sub-cases (u ∈ I; u ≤ inf I via minimal m, m ≥ 1 forced, landing in (α, α+a] ⊂ (α, β)), plus a note making the case split exhaustive for any sign of α; (iii) supremum squeeze with all three reviewer-requested points explicit: T < ∞ because any u₁ ∈ P gives the upper bound u₁ − a for F (nonempty), (T, ∞) ⊆ P from F ∪ P = ℝ_{>0} and T = sup F, and y₀ ∈ F with y₀ > T − ε exists by the definition of supremum of a nonempty set. The limit ε → 0 was replaced by the single choice ε = a/4 (gives a/4 > 3a/4, immediate contradiction) — cleaner, no limiting argument needed.
- The induction fⁿ(y) = y + n·h(y) and h(fⁿ(y)) = h(y) is written out fully (base + step, positivity of iterates by its own induction), per dispatch.

## Reviewer notes addressed
All three from `/tmp/round-1/outline-reviewer.md` (section orbit-forbidden-zone): the two explicit-existence points in 2.6(iii) and the inf I ≤ 0 concern in the AP lemma (in my case structure, α ≤ 0 makes the "u ≤ α" case vacuous since u > 0, so the split remains exhaustive — noted inline).

## Checks run
- sympy: verification margins, the (L) reduction identity 2x² + 2F² − (x+F)² = (x−F)², the (x+F+c)² expansion, and the forbidden-interval roots (y₀ + a) ± √(4ay₀ + 2a²) — all pass.
- Numeric spot-checks (10⁴ random samples each): f = id + c satisfies both inequalities; the (L) form agrees with the squared LEFT for arbitrary positive (x, y, fx, fy). All pass. (These are checks only; the written proof stands on the derivations.)

## Promotable lemmas (proposal files written, pending certification)
- `results/imo-2026-05/lemmas/fe-double-iterate.md` — f∘f = 2f − id for any solution (Step 2.1).
- `results/imo-2026-05/lemmas/orbit-invariance.md` — h∘f = h, fⁿ(y) = y + n·h(y), h(fⁿ(y)) = h(y) (Step 2.2, full induction).
- `results/imo-2026-05/lemmas/h-nonnegative.md` — h ≥ 0 via orbit escape (Step 2.3).
These are exactly the shared steps 2.1–2.3 the outline-reviewer asked to certify for the sibling `right-spreading-fixed-points`.

## Spec concerns
None. The problem is `compute_and_prove` / `answer_type: characterization`; the file states the family explicitly, verifies it by substitution (Part 1), and proves uniqueness (Part 2). One point for the proof-reviewer to eyeball: in Step 2.5's sub-claim the n = 0 boundary case concludes f(y₀) = x exactly (equality, still giving (x − f(yₙ))² = 0 < a²) — intentional, not a typo.
