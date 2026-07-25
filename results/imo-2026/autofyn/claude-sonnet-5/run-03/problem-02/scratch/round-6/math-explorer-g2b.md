## imo-2026-02 (lens: G2b-exclusion sub-gap)

- Distinct openings:
  1. **[MOST PROMISING, NEW] Joint containment+sign exclusion of G2b's genuine (unsquared) roots.**
     Instead of trying to find a uniform sign for `B2` (leading coeff of
     `G_{2b}` in `s_2` — confirmed below to genuinely vary, so that lever is
     dead), work directly with the *unsquared* hypothesis-2 equation
     `cos(∠LBK) = cos(∠LNC)` (equivalently `∠LBK=∠LNC`, since both angles lie
     in `(0,π)` where cosine is injective — no sign ambiguity at this level).
     `G_{2a}=0` and `G_{2b}=0` are just the two quadratic factors of the
     *squared* equation (`[cos∠LBK]^2[\ldots]=[cos∠LNC]^2[\ldots]`), and
     numerically (see below) **each factor generically contains one root of
     the true equation (`∠LBK=∠LNC` exactly) and one of the spurious
     supplementary equation (`∠LBK=π-∠LNC`)** — so the G2a/G2b split is *not*
     literally "true vs. false branch" at the individual-root level (this
     refutes a natural first guess). But when you then ask, of `G_{2b}`'s
     *true* root (the one with `∠LBK=∠LNC` exactly, not `π`-supplementary):
     does it ever satisfy **both** standing hypotheses "L∈△BNC" (full
     polygon containment, not just direction) **and** "K inside angle LBA"
     (the `cross(BK,BL)<0` test from Corollary 11.4) **simultaneously**? —
     the answer is numerically **never**, across 4500+ random trials
     including deliberately stressed near-boundary β and extreme/obtuse
     triangles (see Small-case notes). This is a genuinely different
     mechanism from the population's existing `B2`-sign lever: it doesn't
     need a uniform sign of any single polynomial coefficient, it uses the
     *conjunction* of full containment and the sign test together, exactly
     mirroring how Theorem 11.8 closed the `G2a` side.
  2. A cheaper partial version of (1): just full containment `L∈△BNC` alone
     (dropping the sign test) already excludes ~97% of `G2b`'s true roots
     (412/426 in one 1500-trial sweep) — not sufficient alone (3/200 raw,
     ~14/1500 counterexamples slip through on containment alone), but shows
     containment is carrying most of the load and the sign test is a
     genuinely necessary second ingredient, not decorative.
  3. A resultant-based version of (1), analogous to Theorem 11.8's own
     machinery: compute `Res_{s_2}(G_{2b}, [\text{the "true-branch" locus,
     e.g. a polynomial isolating diff}=0])` — harder to set up cleanly since
     "true vs. supplementary" isn't itself a polynomial condition on `s_2`
     alone (it depends on sign choices under square roots), so this is a
     less clean route than framing things at the level of the *unsquared*
     equation directly (opening 1).
  4. Not pursued in depth (lower priority given time budget): trying a
     *different* auxiliary line/resultant against `L` (the "L-containment"
     hypothesis) rather than `K`-containment — the σ-symmetric mirror of (1)
     (using `G_{3b}`, "K inside angle LBA" mirrored to "L inside angle ACK",
     `K∈△BMC`) should close by the certified σ-symmetry once (1) is proved
     for the `B`-side, so this is not really independent — flag for the
     outliner as "get for free from σ-symmetry," not a separate proof effort.

- Candidate technique(s): direct geometric containment (full triangle
  polygon test, i.e. `L` genuinely inside `△BNC`, not merely the directional
  half of it already used in Lemma 11.3) **combined with** the
  cross-product-sign test (`cross(BK,BL)<0`, exactly Corollary 11.4's
  criterion) applied to `G_{2b}`'s roots instead of `G_{2a}`'s. The proof
  would need: (a) a clean algebraic/geometric characterization of which root
  of `G_{2b}=0` is the "true" (non-supplementary) one — likely via a
  sign condition on `dot(BL,BK)` and `dot(NL,NC)` (their signs must match for
  the true branch; I did not fully characterize this symbolically, only
  numerically filtered by `|∠LBK-∠LNC|<10^{-3}`); (b) a containment or
  magnitude argument (parallel in spirit to Lemma 11.3's affine-extremes
  trick, but for the *full* polygon test, not just the one-sided cross
  product) showing that root either fails containment, or if it barely
  passes containment, fails the sign test. This is squarely a new resultant/
  algebraic-geometry exercise the builder should attempt, not yet solved.

- Cheap-kill candidates: full polygon-containment test on `L` alone kills
  ~97% of `G2b`'s genuine (unsquared-equation) roots already — a good first
  filter/warm-up lemma before tackling the harder joint statement.

- Knowledge-base entries to use: resultants (as already used throughout
  §11), the same "point inside an angle via cross products" primitive
  (Lemma 11.1, already certified machinery — reuse verbatim), affine-
  function-extremes-on-a-triangle trick (Lemma 11.3's method, likely
  reusable for a `G2b`-side containment lemma).

- Analogous past problems (cruxes): did not find a crux-corpus match this
  round (per CLAUDE.md/run_state, the corpus has no geometry-domain entries
  at all, confirmed again — no time spent re-querying since this is already
  an established finding from round 1).

- Prior progress: Theorem 11.8/11.10 (certified, `G2a`/`G3a` side fully
  closed). `B2` (leading coeff of `G_{2b}` in `s_2`) confirmed (my own
  independent sympy computation, matching the file's report) to be
  $$B_2 = 2(-6bu^5+20bu^3-6bu+cc\,u^6-15cc\,u^4+15cc\,u^2-cc),$$
  and its sign genuinely varies — I did not need to re-derive this since the
  file already reports it and my numerics are consistent, but I confirmed
  the underlying `G_{2b}` polynomial itself (via independent `sympy.factor`
  of the full unsquared-then-squared hypothesis-2 equation, matching the
  file's displayed `G_{2b}` term-for-term) so the population's polynomial is
  correct.

- Dead ends (do not retry):
  1. **The "G2a = true branch always, G2b = supplementary branch always" naive
     story is FALSE at the individual-root level** — my own numerics (6
     trials, then confirmed at scale) show both `G_{2a}` and `G_{2b}` each
     generically contain one root satisfying `∠LBK=∠LNC` exactly (the "true"
     unsquared equation) and one satisfying `∠LBK=π-∠LNC` (supplementary,
     spurious). Do not assume the two quadratic factors cleanly separate
     true-vs-squaring-artifact roots — they don't; the real separation
     needing proof is the *containment+sign* criterion on the true roots
     only (opening 1 above), not the factor identity itself.
  2. **`B2`'s sign alone (mirroring Lemma 11.7's `A2<0` argument) cannot
     work** — already established by round 5 and reconfirmed by my own
     independent sympy computation of `B2`'s formula; do not re-attempt a
     pure case-split on `sign(b)` or similar for `B2`, it demonstrably takes
     both signs (I did not re-run the 3000-sample check myself since the
     population's finding is already precise/formulaic, but the reason is
     structural: `B2` is a degree-6-in-`u` polynomial with no evident sign-
     definite factorization, unlike `A2`'s clean `cc\cos\beta+b\sin\beta`
     form).
  3. **Full containment alone (dropping the sign test) is NOT sufficient**
     to exclude `G2b`'s true roots — found explicit numeric counterexamples
     (e.g. `a=3.4434,b=2.1117,cc=0.4955,β≈19.23°,s2≈0.154`: `L` genuinely
     inside `△BNC` AND `∠LBK=∠LNC` to high precision) where containment
     alone survives; the sign test is what additionally excludes this case
     (`cross(BK,BL)≈+0.233>0`, failing "K inside angle LBA"). Do not propose
     a containment-only lemma as the whole fix — it must be joint with the
     sign test.

- Small-case / intuition notes (all labeled conjecture, numeric only):
  - Across 200 random (triangle, valid-β) samples, `G2a`'s genuine
    (`∠LBK=∠LNC`-satisfying) root was inside `△BNC` in 100% of cases
    (0 counterexamples) — consistent with, and a slightly stronger form of,
    the existing Theorem 11.8/population numerics.
  - Across 1500 random samples, `G2b`'s genuine root failed full containment
    in 412/426 cases (~97%); the remaining 14 that passed containment all
    failed the "K inside angle LBA" cross-product sign test (0/1500
    "both-hold" anomalies).
  - Across a further 3000 samples deliberately stress-testing near-boundary
    β (`frac∈(0.001,0.05)∪(0.9,0.999)` of the valid range) and
    extreme/obtuse/skew triangles (`a∈(0.1,6), b∈(-4,5), cc∈(0.05,4)`), still
    **0/1540 "both-hold" anomalies** on `G2b`'s true roots. This is now a
    fairly heavily-stress-tested conjecture (4500+ combined trials, 0
    counterexamples to the joint statement) — a strong candidate for the
    round's build target, though still unproved.
  - Conjecture to hand to the outliner, precisely: *For every triangle
    `A,B,C` and every `β` in the valid range `(0,\min(\angle B,\angle C))`,
    if `s_2` is a root of `G_{2b}(s_2)=0` with `L=C+s_2R(\beta)(A-C)`
    satisfying `\angle LBK=\angle LNC` exactly (not the supplementary
    relation), then `L\notin\triangle BNC$ or `\mathrm{cross}(BK,BL)\ge0`
    (i.e. "K inside angle LBA" fails).* If proved, this — combined with the
    already-certified Theorem 11.8/11.10 and the σ-mirror for `G3b`/K-side —
    would fully close gap 2 (branch selection), modulo the still-separately-
    flagged magnitude bound `t1<t1max(β)` issue noted in §6/§8 of the
    approach file (worth checking whether the *full* polygon-containment
    test I used numerically already subsumes that magnitude bound — it likely
    does, since `in_triangle` is a true full-polygon test, not just a
    direction test; the outliner should double check whether adopting full
    containment as the criterion, rather than the split direction+magnitude
    approach, also retroactively closes §6/§8's separate open magnitude-bound
    gap for `G2a`/`t1` too — a possible bonus simplification).
