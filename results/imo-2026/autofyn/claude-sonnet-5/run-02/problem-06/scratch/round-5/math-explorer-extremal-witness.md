## imo-2026-06

### Lens: extremal property of minimal/earliest witnesses (why literal-minimal S₀ might force V=∅)

- **Distinct openings surfaced:**
  1. **Ordering argument via canonical-witness indices (re-derives existing lemmas, does NOT close V).**
     Order all base types' canonical witnesses m_B increasingly. For a *canonical* witness a_{m_A}, every
     disjoint base type B with m_B<m_A forces A_can∩F_B≠∅ via the already-certified Bounded Witness Lemma —
     this is exactly the certified Canonical-Refinement Lemma, not new. Checked this explicitly by hand; it
     only ever reaches "at least one side canonical," never a genuine rogue (both non-canonical) pair. Not a
     new opening, but worth recording so the outliner doesn't waste a slot re-deriving it under new notation.
  2. **Symmetric Lemma-G-style pairwise argument, but with n_A, n_B (earliest occurrence of the *extended*
     type, not the base type) as the well-ordering measure, instead of round 3's failed |A'|+|B'| size
     measure.** WLOG n_A<n_B in a candidate rogue pair. Free Facts forces gcd(a_{n_A},a_{n_B})>1 (this is
     Lemma G, certified). The open question is whether minimality of (n_A,n_B) among *all* rogue pairs can
     be leveraged to show the forced common prime cannot be genuinely new (∉S₀) — i.e. a minimal-counterexample
     descent on the PAIR OF WITNESS INDICES themselves, not on set sizes and not on "recruitment rounds."
     This is a genuinely different measure from both round-3 attempts (documented as failing for reasons tied
     to the size measure specifically) and round-4's Round Resolution Lemma (which used "first bad round" of
     the recruitment *process*, a different object from "first bad witness-index pair"). Not yet attempted in
     this exact form. I could not complete a descent step in the time available (see "what's promising" below
     for the concrete obstruction), so this is scouted terrain, not a working proof.
  3. **"Near-universal small glue prime" numeric pattern, re-verified but NOT a new mechanism — same dead
     end as round 2.** In several tested seeds (a1=175, a1=1001) a single small prime not in Q (e.g. 3 for
     Q={5,7}, or 2 for Q={7,11,13}) turns out to divide literally EVERY extended-persistent type except the
     full-Q canonical type. This is exactly the round-2 "universal glue prime, sparse-Q regime" pattern
     (memory rule #8), already known and already falsified in the dense-Q regime (rule #9, a1=210/a1=35
     counterexamples) — re-confirming it here is *not* new ground and should not be proposed as a general
     mechanism. Recording it only because it explains numerically *why* V=∅ in the specific seeds checked,
     without generalizing.

- **Candidate technique(s):** minimal-counterexample / extremal-principle descent using witness-index (not
  set-size, not process-round) as the monovariant, directly modeled on the crux-corpus analog below. Use
  the certified Lemma G (`extended-earliest-witness-intersection.md`) as the "coprimality-forces-a-prime"
  engine and the Canonical-Refinement Lemma to dispose of all non-rogue cases first, leaving only the
  descent to handle rogue-vs-rogue.

- **Cheap-kill candidates:** none obvious beyond what's already certified (Canonical-Refinement Lemma
  already prunes every pair with ≥1 canonical side; the only thing left is genuinely rogue×rogue). No new
  parity/pigeonhole shortcut found this round.

- **Knowledge-base entries to use:** the Extremal/well-ordering principle and minimal-counterexample method
  entries in `knowledge_base.md` (generic "assume a minimal violating instance, derive a smaller one"
  template) — check the exact entry name in `knowledge_base.md` when outlining; also re-cite
  `free-facts-gcd.md` (used directly by Lemma G).

- **Analogous past problems (cruxes) — the strongest find this round:**
  - **`aimo-0030`** (IMO-style "game of numbers"/Banana game, `number_theory` /
    `size-bounding-and-descent` + `divisibility-and-gcd`) is a genuinely close structural analog. The
    problem's base fact "any two *good* numbers share a common prime factor" (⟷ our Free Facts /
    "any two terms share a common prime") is upgraded to the sharper "any two good numbers share a
    common *small* prime factor" (Claim 5 in the official solution) (⟷ our target "any two
    disjoint-type extended-persistent witnesses share a common *S₀* prime," i.e. V=∅). Claim 5's proof is
    **exactly a minimal-counterexample descent**: take the pair (b,b') of good numbers with no common
    small prime and b' minimal; apply a "stripping" construction (Claim 4: replace b by a similar number
    x with restricted — only-small — prime support, x≤b) to get x coprime to b'; since any two good
    numbers share *a* factor, x must be "bad" (else x,b' both good & coprime, contradiction); bad x has a
    move to some good b*; b*'s primes avoid b's small primes (by construction of x), giving a strictly
    smaller violating pair (b*,b), contradicting minimality of b'.
    **What transfers:** the *skeleton* (upgrade "share a factor" to "share a special-class factor" via
    minimal-counterexample descent, using a legal-move/greedy-minimality step to manufacture a smaller
    violating instance) is the right shape for our V=∅ target.
    **What does NOT transfer literally:** Claim 4's "stripping" construction is only possible because in
    that problem ANY integer ≥k with a chosen factorization is a legal candidate to test for good/bad —
    free construction. Our a_n values are NOT freely constructible; they are whatever the greedy process
    outputs, so there is no direct analog of "replace b by a similar-but-smaller x." Any adaptation must
    replace the stripping step with something intrinsic to the greedy sequence (e.g. an earlier occurrence
    of the same or a related type) — this is the open engineering gap for the outliner to design around,
    not solved here.
  - Secondary, weaker analogs (checked, less transferable): `aimo-0813` (minimal element of an
    addition-closed subset ⟹ subset = multiples of it, via minimal-counterexample) — same generic
    descent flavor but the additive-closure structure doesn't map onto our multiplicative/type-refinement
    setting. `aimo-0277` (minimal period via Bezout) — not analogous beyond superficial "minimality"
    vocabulary; do not pursue.
  - No exact match for a "persistent-type / extended-type / recruitment" style problem was found in the
    corpus; `aimo-0030` is the best available structural cousin, not a template to copy verbatim.

- **Prior progress:** as recorded in `current.md` / Lemma G — V is localized to genuinely rogue
  (non-canonical × non-canonical) disjoint-base-type pairs; Lemma G shows any such pair's earliest S₀-level
  witnesses share SOME prime, but does not show that prime lies in S₀ (that is exactly V=∅). 18/18 prior
  seeds (with correct minimal witnesses) show V=∅ empirically.

- **Dead ends (do not retry):**
  - Round 3's minimal-counterexample attack using the size measure |A'|+|B'| — documented failure (measure
    non-decreasing under the only available refinement operation, recruitment only adds primes). Do not
    retry with this exact measure; the witness-INDEX measure proposed above (opening 2) is different and
    untested, not a retry of this.
  - Round 4's "first bad recruitment round" / Round Resolution Lemma line — conditional on an unproved
    Singleton Hypothesis; per round-4's correction, may be entirely unnecessary now that V=∅ is the
    better-supported direct target — do not re-invest in extending this conditional lemma before trying
    the direct V=∅ descent.
  - Round 2's "universal glue prime"/"cost≤1 sparse regime" claim — reconfirmed here numerically in two
    more seeds (a1=175 via prime 3, a1=1001 via prime 2) but this pattern is KNOWN to fail in the dense-Q
    regime (a1=35, a1=210 counterexamples from round 2) — do not propose it as a general mechanism for V=∅,
    only as color/intuition for why sparse-Q seeds work.

- **Small-case / intuition notes (all conjecture/numeric, not proof):**
  - Re-ran an independent Python simulation (math.gcd, brute-force greedy, N≈1200–1500 terms) for
    a1 ∈ {15,35,105,175}: **zero rogue-pair violations** in all four, confirming round 4's finding with a
    fresh independent implementation (not reusing prior code).
  - For a1=175 (Q={5,7}, S={2,3,13}): every non-canonical extended-persistent type of BOTH base types
    contains the prime 3 (the sole exception being the canonical witness of base type {7}, i.e. {2,7,13},
    which lacks 3 but is handled separately by the Canonical-Refinement Lemma). This is a clean numeric
    illustration of *why* V=∅ holds in this specific seed — a near-universal glue prime among the
    non-canonical types — but (per the dead-end note above) this exact mechanism is known not to generalize.
  - For a1=1001 (Q={7,11,13}, S={2,3,23}): every proper-subset-base extended-persistent type contains
    prime 2 (the full-Q canonical/near-canonical types are the only ones missing it, and full-Q has no
    disjoint partner so it's irrelevant to V). Same caveat as above.
  - For a1=210 (Q={2,3,5,7}, S={11,53}): every persistent BASE type observed already contains prime 2 (a
    member of Q itself) — i.e. in this seed no two persistent base types are even Q-level disjoint, so V
    is vacuously empty for a trivial reason unrelated to the S-level mechanism. This is a useful reminder
    that "V=∅" sometimes holds for a boring reason (no candidate pairs at all), and the genuinely hard
    seeds are the ones with several small-prime-poor base types (e.g. a1=175, a1=1001) where real rogue
    *candidates* exist and still turn out to intersect.
  - Concrete open engineering question for the outliner: in every non-canonical extended-persistent type
    checked, `n_of(type) > m_(base type)` for BOTH sides of a candidate rogue pair (verified for a1=175 and
    a1=1001: all non-canonical witness indices exceed both base types' canonical witness indices). If this
    ordering (min(n_A,n_B) ≥ max(m_A,m_B)) could be proved in general (it looks plausible since canonical
    witnesses tend to be very early — m_B was 1–4 in both tested seeds — but is NOT proved here), it would
    let a descent argument safely assume both canonical witnesses are already "on the table" before either
    rogue witness appears, which is the natural hypothesis a witness-index descent (opening 2) would need.
    This ordering fact itself is unproven and worth an explicit small lemma attempt.
