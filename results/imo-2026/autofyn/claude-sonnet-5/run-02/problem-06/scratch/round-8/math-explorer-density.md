## imo-2026-06 (lens: density / asymptotic-domination)

- **Distinct openings** (all genuinely different from the FAH-recruitment framing that
  has owned the population since round 6):
  1. **"Density can't reach the target strength" cheap-kill check (structural, not a
     proof route).** FAH/Symmetric FAH are stated as *cofinite* claims ("q divides
     EVERY sufficiently large term of type A", not "a density-1 subset of them"). A
     bare natural-density or counting argument (e.g. "the fraction of type-A terms up
     to N divisible by q tends to 1") is a strictly weaker conclusion than FAH: a
     density-1 set can still miss infinitely many terms (e.g. exceptions at
     doubly-exponentially sparse indices). So any approach that produces only a
     density statement about q-divisibility among type-A terms provably CANNOT close
     FAH by itself — it would need to be paired with an independent argument bounding
     the gaps between potential exceptions (i.e. showing the exception set is not just
     density-0 but literally finite/empty), which is exactly the kind of
     magnitude/exchange argument Lemma H, Lemma K, and Lemma I's diagnosis already show
     the current toolkit cannot supply. This is worth recording explicitly as a
     pre-emptive pruning: don't dispatch a builder on "prove FAH has density 1" as if
     that were progress toward FAH — it is a strictly weaker, insufficient target.
  2. **A different top-level target inspired by crux `aimo-0680` (ISL "Table"
     problem, `f(n)-n` eventually periodic): attack periodicity of the WHOLE sequence
     directly via row-density + a bounded-quantity pigeonhole, bypassing FAH and the
     rogue-pair/recruitment machinery entirely.** `aimo-0680`'s crux move (see below)
     proves each "row" of a partition-into-orbits is an eventual AP using (a) a
     counting/density argument to certify a "non-sparse" residual row once finitely
     many rows are already known to be AP, then (b) a *bounded-integer pigeonhole* to
     find one recurring step value along an infinite subset of that row, then (c) a
     genuinely different, non-density trick — an exact divisibility-difference
     argument — to upgrade "holds along an infinite subset" to "holds at every index."
     This third step ((c)) is precisely the missing ingredient Lemma I's diagnosis
     calls for ("converts an existential per-occurrence fact into a uniform identity
     claim"). It is a *candidate template*, not an available proof: see the gap below.
  3. **Growth-rate / counting comparison between "type-A occurs" and "q divides a_n"
     as independent asymptotic rates** — checked computationally (see Small-case notes)
     and found NOT to distinguish rogue from safe pairs: the fraction of type-A terms
     divisible by a fixed non-core prime stays roughly constant (not tending to 0 or 1)
     across the whole tested range, for primes unrelated to the actual Lemma-G
     witness. This growth-rate angle does not by itself supply new information; it is
     consistent with (but does not newly support or refute) FAH.

- **Candidate technique(s):** the aimo-0680 "dense-row + bounded-pigeonhole +
  divisibility-difference-vanishing" template (density as a *discovery* tool to locate
  which object to examine, combined with an *exact* arithmetic argument — not density
  itself — to nail the cofinite claim). Classical natural-density / counting arguments
  alone are not the right tool for FAH's cofinite strength.

- **Cheap-kill candidates:** the density-vs-cofinite mismatch above (point 1) — use it
  to reject, without further computation, any future approach whose deliverable is
  merely "density 1 of type-A terms are divisible by q." This should save a round of
  wasted building if such an approach is proposed.

- **Knowledge-base entries to use:** none of `knowledge_base.md`'s generic entries are
  specifically density-flavored for this problem (the workspace's own certified lemma
  stack — Free Facts, Bounded/Generalized Bounded Gap Lemma, Persistent-Type
  Pigeonhole, Finite Core Theorem, Monotonicity of Resolution, Projection Lemma,
  Collateral-Safety — already IS the applicable machinery; no additional KB entry
  supplies a genuine density theorem beyond ordinary pigeonhole, which is already in
  use). Recommend the outliner not expect a new KB citation here; the missing
  ingredient is a bespoke arithmetic identity (per opening 2), not a named theorem.

- **Analogous past problems (cruxes):**
  1. **`aimo-0680`** (ISL-style "prove f(n)-n is eventually periodic", `number_theory`
     / `divisibility-and-gcd` + `size-bounding-and-descent`) — genuinely the closest
     structural analog in the corpus: same top-level shape (partition an increasing
     index set into finitely many classes/"rows", each row individually forced toward
     an AP, then combined via lcm of steps exactly as `covering-system-construction`'s
     Step 5 CRT finish already does). Its crux move is the three-part template in
     opening 2. **Caveat, important:** its step-(c) "upgrade infinite-often to
     everywhere" argument crucially uses the problem's OWN hypothesis that
     `f^n(m)-m` is divisible by `n` for every `m,n` — an exact global arithmetic
     identity that has NO known analog in imo-2026-06 (our sequence's gaps are only
     bounded, `a_{n+1} ≤ a_n + a_1`, not tied to any divisibility-by-index identity).
     So the crux move is a genuine hint at proof *shape*, not a transplantable
     step — matches the precedent already set (and already burned once) by
     `scalar-well-ordering-lock-in`'s aimo-0678 transplant, which failed for the
     analogous reason (Witness Discontinuity Obstruction: no persistence/continuity
     identity survives recruitment). Recommend: if pursued, this must be flagged from
     the start as needing a *new* exact identity peculiar to this problem's gcd
     structure to play the role of `f^n(m)-m ≡ 0 (mod n)` — not assumed to exist.
  2. **`aimo-0516`** (`p-adic-valuation`/`divisibility-and-gcd`, "find |S| given a
     gcd-uniqueness property") — its crux ("compute the proportion of a finite set
     divisible by p by transferring the divisibility condition into a divisor-count
     ratio, then force the ratio to be element-independent") is a nice example of a
     genuine *proportion* argument closing a gcd problem, but it operates on a FINITE
     set with an exact bijective structure (`d ↦ unique t with gcd(s,t)=d`); our
     problem's persistent-type classes have no known bijective/tau-function structure
     to exploit. Judged: suggestive of the general *flavor* (turn a divisibility
     condition into a ratio, force ratios to agree) but not directly portable —
     weaker analogy than `aimo-0680`.
  3. **`aimo-0308`** (pigeonhole-collision via counting outgrowing range) — generic
     "count exceeds range forces collision" pigeonhole, already essentially the same
     tool already in use in this workspace's Persistent-Type Pigeonhole / Finite Core
     Theorem. Not a new mechanism; recorded only to confirm no untried pigeonhole
     variant is hiding here.

- **Prior progress:** unchanged from round 7 — (†) is reduced (Collateral-Safety
  Theorem, certified) exactly to base-type-pair-level termination, which in turn is
  now known (Steps 8.5/8.7 of `covering-system-construction`) to follow from
  FAH + Symmetric FAH (equivalently a single canonical-prime "Joint FAH" for
  q* = min(F'∩F'')). Both FAH and Symmetric FAH remain open, empirically supported
  (0 counterexamples across every tested seed, independently re-verified 4 times).

- **Dead ends (do not retry):** joint Lemma-H branch analysis (Two-Witness
  Intersection Uniqueness); inductive chaining / exchange-minimality built solely from
  Free Facts + Generalized Bounded Witness + Gap Lemmas + Critical Prime Dichotomy
  (Lemma I's diagnosis); Blocking-Data Bridging via Lemma K (uncontrolled competitor
  factorization); the aimo-0678-style algebraic-recursion transplant (Witness
  Discontinuity Obstruction, certified); all three `recruitment-round-charging`
  variants (ω/Ω-charging, O(n)-growth-charging, batch-resolution-charging — the last
  reduces to FAH, not independent). **New this round:** any approach whose
  deliverable is a bare density-1 (not cofinite) divisibility statement about
  type-A-terms-divisible-by-q — provably insufficient to close FAH as stated (see
  opening 1), should not be treated as progress if proposed.

- **Small-case / intuition notes (all conjectural/empirical, not proved):**
  - Computed a_1=187 out to 1200 terms (Q={11,17}, persistent base types
    {11},{17},{11,17}). The type-{11} occurrence subsequence's gap pattern is NOT a
    clean eventual AP at the base-type level: gaps are {22: dominant (~85%), 11: rare,
    33/44: rare} in both an early window and a late window (first-50 vs last-50
    windows: 41/6/3 vs 44/3/2/1 split) — i.e. the *base*-type row is only "eventually
    periodic in distribution," not literally AP; this is consistent with the
    workspace's own framing that periodicity only emerges at the *extended*-type
    level (S₀-refined), not the base-type level, reinforcing why `covering-system-
    construction`'s whole machinery works at extended types.
  - Checked whether the fraction of type-{11} terms divisible by a fixed
    unrelated small prime (7, not itself a core or Lemma-G-recruited prime for this
    pair) drifts toward 0 or 1 as n grows: it does NOT — stays flat at ≈18-19% in an
    early window (n≤100 occurrences) vs a late window (last 100 up to n=1200),
    conjecturally consistent with 7 not being a Lemma-G/FAH-relevant prime for this
    particular type pair. This confirms (conjecturally, on one seed) that "generic"
    primes show no asymptotic domination — only the specific Lemma-G-recruited prime
    for a genuinely rogue pair is conjectured to reach density 1 (in fact cofinity,
    per FAH) — i.e. asymptotic domination is not a generic phenomenon one could detect
    by density alone without already knowing which prime to test, so a density-first
    "discover the FAH prime by growth-rate scanning" strategy adds no new leverage
    beyond what Lemma G already hands you explicitly (the canonical witness prime).
  - Net conjecture from this round's probing: density/asymptotic tools in their
    classical form are the wrong strength of instrument for FAH (opening 1); the only
    genuinely new avenue found (opening 2, the aimo-0680 template) requires an exact
    arithmetic identity this problem is not currently known to possess, so it is an
    honest *open opening*, not a route already shown to work — next round would need
    to search specifically for such an identity (e.g., something exact relating
    gcd-recruitment to an index-divisibility fact) before this becomes more than a
    hint.
