## imo-2026-06 (lens: formation-window / growth-structure route to E5″)

- **Distinct openings surfaced this round:**
  1. **Index-vs-value bound (Lemma 2 direct).** Since `t = ∏G = u(G)` is a genuine term (Lemma
     R1) at some index `i`, Lemma 2 gives `a₁+(i−1) ≤ t ≤ a₁+(i−1)M`. This bounds `t` in terms of
     `i` and `M`, but gives **no a₁-only ceiling on `t`** unless `i` itself is first shown to be
     `a₁`-bounded — which is exactly the ERW target (§10 of the antichain approach) and is not a
     new lever, just a restatement.
  2. **"Formation window via non-realization of predecessor" (the natural formation-window
     idea).** Ask: can `t=∏G`'s *index* be bounded by observing that the predecessor `a_{i-1}`
     satisfies `a_{i-1} ≥ t−M` (gap bound), and that any *smaller* candidate value in
     `(a_{i-1}, t)` — in particular `∏S` for `S=G∖{p_max}`, if `∏S<t` and `∏S≥a_1` — must have
     been **rejected** at stage `i−1` because it failed to meet some support already realized by
     then. I traced this precisely: **it is only possible for `∏S` to be legitimately rejected if
     some minimal-support member disjoint from `S` (e.g. `H_{p_max}`, whose existence is only
     guaranteed globally by E3) has *already been realized as an actual term* by index `i−1`.**
     If it hasn't yet been realized, `∏S` (assuming `∏S ∈ (a_{i-1}, t)`) would be admissible and
     get selected **before** `t`, which would realize the proper sub-support `S ⊊ G` as a term —
     exactly the excluded "realize a sub-support to contradict minimality" mechanism (R4
     Collapse). So this route bifurcates: either (a) it reduces to showing `H_{p_max}` (or some
     disjoint member) forms *before* index `i-1`, which is a mutual/circular timing claim about
     *all* of `𝓐_∞` simultaneously (the "simultaneous interaction of all minimal supports"
     difficulty flagged in §7b/§8.4, never resolved), or (b) it collapses verbatim into the R4
     Collapse mechanism if pushed to conclude non-realization directly. **I could not find a
     window/growth argument that avoids this fork.** This is a negative finding, not a
     construction — reported honestly below.
  3. **Pure counting / pigeonhole on primes across a bounded number of terms (no dynamics).**
     Tried to get an a₁-only bound purely from Lemma 1 (Anchor) + Lemma 3 (Distance–prime) + Lemma
     2 (linear growth), with **no appeal to admissibility rejection/realization timing at all**
     (to dodge the fork above). Distance–prime only gives a *lower* bound on gaps between terms
     sharing a prime (`q ≤ |a_i−a_j|`), which bounds how *close together* two same-prime terms can
     be, not how *far apart* — it does not produce an upper ceiling on `p_max` or `∏G`. Anchor
     bounds only `|P|` (the fixed `a₁`-prime-count), already fully used in Prop 12.A. No new
     purely-static inequality emerged; every attempt to get traction needed to reason about *when*
     a competing support first gets realized, which reopens the dynamical fork of opening 2.

- **Candidate technique(s):** none beyond what's already certified (R1/R2, E1–E3, gap bound). The
  "formation window" idea is real machinery (Lemma 2 + E1 realizability) but every concrete
  attempt to turn it into an a₁-only ceiling on `∏G` bottoms out at the same fork as opening 2.

- **Cheap-kill candidates:** none obvious for the window route directly. One useful negative
  cheap-check I did perform: verified the fork above is *forced*, not merely likely — i.e. any
  proof that `∏S = ∏(G∖{p_max}) ≥ a₁` cannot appear as `a_i` before `t` **must** exhibit an
  already-realized disjoint witness by index `i-1`; there is no way around invoking realization
  timing of some other minimal support. This confirms (independently, via a different route than
  `residual-anchor-peeling`) that the R4 Collapse phenomenon is not an artifact of the
  anchor-partition framing specifically — it is structural to *any* argument that tries to rule
  out `∏S ≥ a₁` by appeal to greedy selection/rejection.

- **Knowledge-base entries to use:** none new found beyond what's already invoked
  (Pigeonhole/extremal principle already used in E4; Bertrand's postulate considered — could in
  principle supply "a prime in `(X,2X]`" but I found no way to connect it to bounding `p_max` or
  `∏G` from above, since the problem needs an *upper* ceiling on the realized radical, not
  existence of a prime in a range). No LTE/Zsigmondy/Dirichlet applicability found (no exponential
  or AP structure here — the sequence is defined by a greedy `gcd` rule, not a recurrence).

- **Analogous past problems (cruxes):** `aimo-0447` (already in use — the pincer analogy: line
  value ≥ product of distinct primes, matching R2). I did not find a second corpus entry with a
  genuinely analogous "greedy admissible-set / minimal transversal" structure; the corpus's
  window/formation-time problems I sampled (interval-covering, prime-gap arguments) rely on a
  *fixed ambient bound* (like the aimo-0447 template's fixed `N`) that this problem does not have
  a priori — obtaining that fixed bound *is* the open problem, so those analogies do not transfer
  a new technique, only confirm the pincer shape already exploited in `realizer-value-pincer.md`.

- **Prior progress:** as recorded in `current.md` / `realizer-value-pincer.md` — E5 reduced to the
  single residual E5″ (`∏(G∖{p_max}) < a₁` for minimal `G` with `∏G ≥ a₁`), with the small-radical
  regime `∏G<a₁` fully closed (Prop 12.A) and the pincer's lower jaw (R1/R2) in hand.

- **Dead ends (do not retry):**
  - "Realize `S=G∖{p_max}` (or any proper sub-support) as a term to contradict `G`'s minimality" —
    proved to collapse to E5 verbatim (R4 Collapse theorem, reconfirmed independently this round
    via the formation-window fork above).
  - M-threshold confinement (`p|L ⇒ p≤M`) — refuted (`a₁=375` has `19|L`, `M=15`).
  - A_n-only monovariants — proven insufficient (concrete obstruction family freezes all
    statistics).
  - Value-stream automaton — proven logically equivalent to the crux, no bypass.
  - New this round: **any "window/growth" argument that tries to bound `∏G`'s formation index by
    reasoning about rejection of competing smaller-support candidates** reduces to the same
    collapse — do not re-attempt without a genuinely different (non-dynamical) mechanism.

- **Small-case / intuition notes (numerical, conjecture only, not proof):**
  Ran the greedy simulation on ~150 seeds (all previously-tested seeds plus ~80 new ones: random
  seeds up to 5000, primorial-type products `2·3·5·7·…`, and structured products of 2–5 small
  primes up to `255255`). Findings, all **conjectural evidence**:
  - `∏G/a₁` stays `≤ 1.448` across every seed tested (worst at `a₁=899`, `G={2,3,7,31}`), well
    under the sufficient window form `∏G<2a₁`.
  - `redMax(G)/a₁ = ∏(G∖{p_max})/a₁` stays `≤ 0.2` across every seed tested (worst at `a₁=15`),
    far below the `E5″` threshold of `1` — E5″ holds with a **wide margin** on all data, suggesting
    the true bound is much stronger than needed, but no structural reason for the margin was
    identified (i.e. the numerical slack does not by itself suggest a new proof mechanism).
  - Even highly composite / many-prime-factor seeds (`15015=3·5·7·11·13`, `255255`,
    `9375=3·5^5`) do not push the ratio up — `max|G|` stays small (`≤6`) and `redMax/a₁` stays
    small, consistent with E5″ but not pointing to any new inequality beyond what's already
    targeted.
  - No seed was found that stresses `∏G/a₁` above ~1.45, and no trend suggests it grows with `a₁`
    or with `|G|` — the data is consistent with a *fixed* small constant, not merely `a₁`-bounded,
    but this is only evidence, not a proof, and does not resolve the fork identified above.

**Bottom line for the outliner:** the formation-window/growth-structure lens, worked through
carefully, does **not** offer an independent bypass of E5″ — it forks into either (a) the already-
excluded sub-support-realization collapse, or (b) an unresolved mutual/simultaneous-timing claim
about when *all* minimal supports form relative to each other (the same "simultaneous interaction"
difficulty flagged since §7b/§8.4 of the antichain approach, never closed by any prior round). No
purely static (non-dynamical) counting argument using only Anchor/Distance-prime/Gap-bound was
found to produce an a₁-only ceiling on `∏G` or `p_max`. This should be read as reinforcing evidence
that the E5″ wall is a genuine structural obstruction shared by every framing tried so far
(antichain endgame, anchor-partition, and now formation-window) — the outliner may want to
prioritize either (i) a genuinely new invariant/potential function on the *joint* system of all
minimal supports (not on a single `G` or a single window), or (ii) revisiting whether E5″ needs a
sharper use of E3's private-witness *distance* bound `q ≤ |t−t'|` combined with an *upper* bound on
`|t−t'|` derived from the fact that both `t` and `t'` are the *first* realizers of their respective
supports (an angle not yet tried: bounding `|t-t'|` via double-counting realizer indices rather
than rejection timing) — flagged as a possible but unexplored opening, not attempted here.
