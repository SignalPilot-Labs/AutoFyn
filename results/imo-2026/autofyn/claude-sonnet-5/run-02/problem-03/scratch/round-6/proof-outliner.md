# Proof-outliner report, round 6 — IMO-2026-03

## Context read
`current.md`, all 10 existing `approaches/*.md`, all 30 `lemmas/*.md`, and
both round-6 explorer reports
(`math-explorer-two-sided-invariant.md`, `math-explorer-global-potential.md`).
Confirmed the plateau: 4 consecutive rounds (2–5), 6 independently-built
approaches, all converge on the same wall — an induction on $n$ needing an
*upper* bound on $A$ of a reduced sub-instance, only supplying a *lower*
bound. The wall is now pinned down to one precise inequality, stated two
equivalent ways on file: `rank-tie-vertex-reduction.md` §5.1's
$(\star\star)$: $\int_{W\cap[0,r)}v(t)\,dt\le\Delta/2$ (window of length
$\Delta$ straddling $p_1/2$, $v$ = tail's odd-parity indicator), and
`greedy-halving-adversary.md`'s general "Missing inequality" for arbitrary
splits.

## New approaches opened (3), per the shared-gap-plateau rule

1. **`approaches/lp-duality-certificate.md`** (new file). Abandons induction
   on $n$ entirely: seeks an explicit LP-duality / Positivstellensatz-style
   nonnegative-combination certificate proving $\Phi(S)\ge a_n\cdot
   \mathrm{Total}(S)$ directly over the whole `vertex-minimum-theorem`
   polytope, in one shot. Concrete first step: reverse-engineer a certificate
   from the already-fully-closed $n=2$ case (10 compositions), then look for
   a certificate-recursion (induction on the *proof object*, not the value
   function — so it structurally never needs an unavailable upper bound).
   Flagged by the global-potential explorer as the most directly targeted
   new framing. Entirely unstarted; biggest risk is that no certificate
   exists even for $n=2$ cleanly.

2. **`approaches/integer-lattice-reduction.md`** (rewrote the orphan slug
   registered in round 4 with 0 builds — same name, sharper plan). Rescales
   by $D=2^{n+1}-1$ so the ladder becomes the exact integers
   $\{2^n,\dots,1\}$, aiming to evaluate `single-cut-perturbation-identity`'s
   correction term $I_1+I_2$ (equivalently $(\star\star)$'s window integral)
   as an exact binary-digit/carry computation, transplanting the
   domination/popcount mechanisms of crux corpus `aimo-0141`, `aimo-0917`,
   `aimo-0764`. First concrete sub-lemma (looks tractable, reusable
   regardless of the rest): prove minimizing-vertex fragment values are
   rational with denominator dividing $D$ (follows from
   `vertex-minimum-theorem`'s tie-equalities being rational).

3. **`approaches/bijective-mersenne-pairing.md`** (new file). Direct
   piece-to-piece pairing on the final multiset motivated by the ladder's
   own $2{:}1$ doubling ratio and $2^{n+1}-1$ Mersenne structure, reusing
   `aimo-0915`/`aimo-0596` pairing templates. Deliberately cheap: gated on a
   go/no-go test against the fully-known $n=2$ case (10 compositions)
   before any further investment — explicitly the riskiest and
   least-targeted of the three, per the global-potential explorer's own
   ranking (LP-duality first, this second, literal band/mass potential
   ruled out entirely as already-shown-too-coarse by
   `dyadic-band-occupancy`).

## Live approaches sharpened (concrete next steps appended, no new files)

- **`greedy-halving-adversary`**: added round-6 note pointing its own
  "Missing inequality" at the now-more-precise $(\star\star)$ from
  `rank-tie-vertex-reduction`, recommending it defer to whichever new-framing
  approach resolves $(\star\star)$ rather than re-deriving a fourth
  independent mass bound.
- **`rank-pigeonhole-budget`**: added round-6 note — finish remaining Case II
  sub-range + Case I if built again; check whether
  `integer-lattice-reduction`'s rationality sub-lemma can simplify its
  case analysis to pure integer arithmetic.
- **`rank-tie-vertex-reduction`**: added round-6 note flagging $(\star\star)$
  as the cleanest current target for the new certificate/digit approaches,
  and its own tractable residual (§5.3's $n\le7\to$general-$n$ corollary
  finish) if built again.
- **`dyadic-band-occupancy`**: added round-6 note — its assigned coarse
  technique is already certified insufficient (round 5); deprioritize unless
  paired with a finer invariant.
- **`induction-first-move-reduction`** (orphan file, never registered/built,
  0 entries in `.ranking.json`): audited and flagged — it's a "reduce to
  smaller ladder" variant with its own documented arithmetic contradiction in
  Step 6, exactly the pattern this round's directive says not to reopen.
  **Recommend not registering/building it.**

## Recommended build set for outline-reviewer's consideration

New framings (priority, per explorer ranking): `lp-duality-certificate`,
`integer-lattice-reduction`. Optional cheap scout: `bijective-mersenne-
pairing` (time-box it — go/no-go on $n=2$ before real investment). Continue
one or two of the live approaches (`rank-tie-vertex-reduction` and/or
`rank-pigeonhole-budget`) only if the outline-reviewer judges their residual
tractable sub-gaps (not $(\star\star)$ itself) worth a round. Do not rebuild
`dyadic-band-occupancy` or `induction-first-move-reduction` this round.

Final build-set selection, ranking, and registration of the new approaches
in `.ranking.json` is the outline-reviewer's job (register_approach /
copy_approach / update_ranking) — not done here.
