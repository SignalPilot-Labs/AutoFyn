## imo-2026-02 (lens: trig identities / trig Ceva / Ptolemy)

- Distinct openings:
  1. **Ptolemy on cyclic quadrilateral A,K,L,Q in this exact cyclic order**
     (numerically confirmed order — see below): the target concyclicity is
     *equivalent* to the identity `AL·KQ = AK·LQ + KL·AQ`. This is a genuinely
     different top-level target from the directed-angle-chase target
     (`∠(LA,LK)=∠(QA,QK)`) used by fixed-point-concyclic.md: instead of chasing
     one angle equality through the hypotheses, the goal becomes proving one
     *length* identity, which can be attacked by expressing AK, AL, KL, AQ, KQ,
     LQ each via the Law of Sines in the auxiliary triangles ABK, ACL, BMK,
     CNL (using the hypothesis angles as the "opposite angle" in each) with a
     **single free parameter kept symbolic** (see Small-case notes — the
     family is 1-parameter, so no length is individually determined; only the
     Ptolemy combination should collapse to an identity). This has NOT been
     executed symbolically — it's an opening, not a result.
  2. **Trig-Ceva-style reading of the vertex-B and vertex-C ray configurations.**
     At B the four rays BA, BK, BL, BC occur in this cyclic order (K inside
     ∠LBA ⟹ BK between BA,BL); two of the three consecutive angles are pinned
     by hypotheses 1,2 (`∠KBA`, `∠LBK`), leaving `∠LBC` free. Symmetrically at
     C: rays CA,CL,CK,CB with `∠ACL`,`∠LCK` pinned, `∠KCB` free. This is the
     natural setting for a trig-Ceva-like relation IF a third fact pins down
     `∠LBC`/`∠KCB` or a concurrency (e.g. of BK, CL, and some fixed line) —
     but numerically **no such concurrency exists** (BK∩CL moves substantially
     across the family, see below), so plain trig Ceva does not directly apply;
     this rules out one natural-looking route and should not be retried as
     stated.
  3. **Symbolic (angle-parametrized) law-of-sines elimination**, as a
     trigonometric analogue of coordinate-bash's polynomial elimination:
     parametrize by `θ = ∠KBA = ∠ACL` (or by the position of K along the family)
     and derive AK, BK from triangle ABK, AL, CL from triangle ACL, then feed
     hypotheses 2–3 (which involve M, N) through triangles BMK and CNL via the
     Law of Sines to pin the remaining free parameter as a function of θ; this
     is mechanically the same content as coordinate-bash's Gröbner elimination
     but in trigonometric (angle) variables, which sometimes simplifies IMO
     geometry eliminations better than raw coordinates. Not attempted this
     round beyond the setup above.

- Candidate technique(s): Law of Sines chase across triangles ABK, ACL, BMK,
  CNL, LBK, LNC combined into one Ptolemy identity on A,K,L,Q (knowledge_base.md
  "Circle/triangle configuration facts" — Ptolemy `AC·BD=AB·CD+AD·BC`); trig
  Ceva (`knowledge_base.md`, Synthetic toolkit — "trig cevians (Ceva/Menelaus)")
  was considered but does not directly apply (see Cheap-kill candidates).

- Cheap-kill candidates (all executed numerically this round, robust across
  two very different triangles — one near-isosceles from round 1's instance,
  one deliberately scalene, `A=(0,4.5), B=(-3,0), C=(5,0.3)`, 22-point family):
  - **No fixed length ratio exists.** AK/AL, BK/CL, MK/NL, and the product
    AK·AL/(AB·AC) all *drift substantially* along the 1-parameter family (e.g.
    AK/AL ranges 0.911→0.843, BK/CL ranges 0.40→0.81, on the scalene triangle).
    This kills any hoped-for "AK/AL = fixed function of triangle ABC's angles"
    shortcut — the free parameter genuinely must appear in any correct
    trig identity, so a naive Ptolemy-from-fixed-ratios approach cannot work;
    the elimination in opening 1/3 must keep the free parameter symbolic
    throughout and only cancel it at the very end.
  - **No hidden similar triangle touching K or L.** Ran an exhaustive
    AA-similarity search over all `C(8,3)=56` triangles on {A,B,C,K,L,M,N,Q},
    matching angle-triples (in all 6 vertex correspondences) to within 1e-4
    across all 22 members of the scalene family simultaneously (stronger than
    round 1's single-instance check, which only tested one config). Found
    exactly 7 matches, **all among A,B,C,M,N,Q only** (e.g. `ABC~AMN~QNM`,
    consequences of the midline homothety + A,M,N,Q concyclic already proved
    in fixed-point-concyclic.md Lemma 3) — none involving K or L. This is a
    stronger, family-wide confirmation of round 1's single-instance refutation
    of "spiral similarity at A sending B↦C, K↦L", and rules out *any* fixed
    triangle-similarity shortcut as a route to the concyclicity, not just the
    specific one round 1 checked.
  - **No hidden concurrency at vertex B/C.** `BK ∩ CL` moves substantially
    across the family (from ≈(−0.69,0.99) to ≈(0.03,3.93) on the scalene
    triangle) — not a fixed point, and quadrilateral B,K,L,C is not concyclic
    (determinant test ≈7 to 46, nowhere near 0). Rules out trig-Ceva-via-
    concurrency (opening 2) as stated.

- Knowledge-base entries to use: `knowledge_base.md` "Circle/triangle
  configuration facts" (Ptolemy identity, exact statement + inequality form);
  "Synthetic toolkit" (angle chasing, power of a point, similar triangles,
  trig cevians, spiral similarity) for context/vocabulary only — most of these
  were tested and ruled out as *direct* shortcuts (see Cheap-kill candidates).

- Analogous past problems (cruxes): none searched — per
  `/tmp/memory/math-explorer.md` rule 3, the crux corpus has not extracted
  geometry cruxes yet (confirmed by prior round; not re-verified this round to
  save time, but flagged as still-true guidance).

- Prior progress: identical to current.md — all four approaches reduce to one
  central identity `O·(C−B) = (|C|²−|B|²)/4` (A at origin), equivalently A,K,L,Q
  concyclic for Q = reflection of A in perp-bisector(MN) = unique point with
  AQ∥BC, QB=QC. This round's numerics **reconfirm this identity exactly**
  (residuals ~1e-13 to 1e-15) on both the round-1 near-isosceles instance and a
  fresh, deliberately scalene triangle across a 20+ point family in each,
  strengthening confidence the identity is correctly stated and the sign
  branch used by prior rounds is right.

- Dead ends (do not retry):
  - Fixed-ratio-based Ptolemy/law-of-sines shortcuts (AK/AL, BK/CL, MK/NL, or
    AK·AL as a function of ABC alone) — refuted by direct computation this
    round (see Cheap-kill candidates); do not assume any such quantity is
    constant along the family.
  - Naive spiral similarity at A sending B↦C, K↦L — already refuted in round 1
    (fixed-point-concyclic.md and spiral-similarity-bootstrap.md); reconfirmed
    this round via the exhaustive family-wide similarity search (no K/L
    triangle matches any B/C/M/N/Q triangle).
  - Trig Ceva via a concurrency of BK, CL (or similar cevian pairs at B, C) —
    refuted numerically this round (BK∩CL is not fixed, BKLC not concyclic).
  - (Carried from round 1) exhaustive search over the 70 four-point subsets of
    {A,B,C,K,L,M,N,Q} plus BK∩CL, BL∩CK found no hidden auxiliary circle beyond
    (A,M,N,Q) and the target (A,K,L,Q) — reconfirmed consistent with this
    round's BKLC-non-concyclic check.

- Small-case / intuition notes (all numerical, i.e. conjectural until proved):
  - The cyclic order of A,K,L,Q on their common circle is **A,K,L,Q** (not
    A,K,Q,L or another order) — verified by angular sort around A and by the
    fact that only this ordering makes Ptolemy's equality hold exactly (the
    other pairing gives a large residual, ~10–50, i.e. macroscopically false).
    The exact target identity for a Ptolemy-based proof is therefore
    $$AL\cdot KQ \;=\; AK\cdot LQ \;+\; KL\cdot AQ,$$
    confirmed to residual < 1e-14 across all sampled family members on two
    different triangles. This is the precise statement opening 1 would need
    to derive independently of assuming concyclicity.
  - The family genuinely has one free real parameter (matches round-1's
    finding); every individual length (AK, AL, BK, CL, MK, NL, KL) is a
    non-trivial function of that parameter, so any correct trig identity must
    be an identity *in that parameter*, not a numeric coincidence at one
    point — this is the central reason plain "similar triangles" or "constant
    ratio" attempts fail, and should reset expectations for what a
    trig/Ptolemy proof needs to accomplish (a genuine elimination, not a
    lookup of a fixed similar-triangle pair).
