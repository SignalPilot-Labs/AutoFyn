## imo-2026-02

### Setup used
Numerically reconstructed the 1-parameter family of valid (K,L) for two test
triangles (one accidentally near-isosceles — discarded once diagnosed; one
genuinely scalene: A=(0.2,3.1), B=(−2.0,0.0), C=(3.5,−0.3)). Parametrized
K on ray from B at angle θ=∠KBA to BA, L on ray from C at angle θ=∠ACL to CA
(hypothesis 1 built into the parametrization since ∠KBA=∠ACL forces the same
θ), solved the remaining two hypotheses (∠LBK=∠LNC, ∠LCK=∠BMK) for the two
radii via `fsolve`, filtered by all four containment conditions (K∈△BMC,
L∈△BNC, K inside ∠LBA, L inside ∠ACK) — every solution passing the two
angle-magnitude equations on this parametrization automatically passed all
four containments (consistent with round-1's finding of a clean 1-parameter
family with no extra branch-selection needed once the ray directions are
fixed correctly). Reconfirmed OM=ON to 1e-13 and A,K,L,Q concyclic to 1e-13
(Q = reflection of A in ⊥-bisector of MN) on this scalene instance, and swept
θ over ~120–260 family members for all further tests.

### Distinct openings
This lens does NOT surface a new full opening beyond what's already on the
table — its purpose was to stress-test spiral-similarity-bootstrap's
specific idea, and the verdict is **mostly negative** (see Dead ends). The
one thing worth keeping: the target identity ∠(KA,KQ) = ∠(LA,LQ) (directed,
mod π) is confirmed to hold across the whole family to machine precision —
this is just a restatement of "A,K,L,Q concyclic" via the chord-AQ criterion
(same content as fixed-point-concyclic's Step 3 target, not new), but it is
the cleanest single 2-term identity to attack directly: it says K and L see
segment AQ at equal directed angles, i.e. **the real target can be phrased
purely as "K and L both lie on locus {X : ∠(XA,XQ) = c} for the same
constant c"** — a genuinely different way to state Step 3's gap (angle-to-a-
fixed-segment instead of 4-point concyclicity), which might be more tractable
for a trig chase since it separates into two independent one-variable
problems (find ∠(KA,KQ) as a function of the family parameter using
hypotheses 1+3, find ∠(LA,LQ) similarly using hypotheses 1+2, then check
equality) rather than one 4-point concyclicity claim.

### Candidate technique(s)
None of the "spiral similarity" or "one-angle circle-membership" ideas in
spiral-similarity-bootstrap.md survive contact with numerics (see Dead ends
below) — this framing does not open a shortcut. The residual useful framing
is the "two independent one-variable angle computations, then compare"
restatement above, which is really a trig-Ceva / directed-angle computation
in the spirit of coordinate-bash but potentially lighter (2 angles instead of
a full Gröbner elimination). Recommend knowledge_base.md's directed-angle
chasing toolkit and trig-Ceva entries (if present) over anything
spiral-similarity-specific.

### Cheap-kill candidates
None new. (Round 1 already ruled out the single obvious cheap kill: spiral
similarity at A sending B↦C, K↦L.)

### Knowledge-base entries to use
- Geometry / Synthetic toolkit — directed-angle chasing and its concyclicity
  converse (as already used by fixed-point-concyclic; still the right tool,
  just needs the missing computational link).
- Geometry / Synthetic toolkit — spiral similarity (checked exhaustively
  below; does not apply directly here, but worth citing as "considered and
  ruled out" so future rounds don't re-try it).

### Analogous past problems (cruxes)
Per run_state.md's recorded rule and round-1 finding: the crux corpus has no
geometry-domain entries extracted yet. Did not re-query (per per-role rule
"NEVER assume a crux match exists for geometry problems"); no analogous crux
found or expected.

### Prior progress
Same as current.md: all four approaches converge on proving A,K,L,Q
concyclic (equivalently O·(C−B) = (|C|²−|B|²)/4). Nothing in this lens closes
that gap; see restatement above as the one new framing contribution.

### Dead ends (do not retry) — all newly verified this round, numerically, on a genuinely scalene triangle over a ~120-point sweep of the family
1. **Spiral similarity centered at K sending B→L (or any fixed-ratio/fixed-
   angle claim about triangle BKL relative to a fixed pair)**: |KB|/|KL|
   ranges from ~0.002 to ~0.74 across the family — wildly non-constant, so
   there is no per-family-invariant similarity here (expected: a spiral
   similarity is a single-instance fact, not a family invariant; this
   framing question was ill-posed as "fixed across the family" and is
   recorded so it isn't retried the same way).
2. **Full similarity △BLK ∼ △NLC (from hyp. 2 alone)**: tested ∠BLK vs ∠NLC
   and LB/LN vs LK/LC across the family — neither the angles nor the ratios
   match (e.g. at θ=32.7°: ∠BLK=2.2°, ∠NLC=124.7°, LB/LN=2.84, LK/LC=3.67).
   Confirms round-1's computational-lens refutation from a different
   triangle; this is now doubly confirmed and should be considered closed.
3. **"K lies on a fixed circle as θ varies" / "L lies on a fixed circle as θ
   varies"**: best-fit algebraic circles through 50 family members of K (resp.
   L) have max residual ≈0.0009 against a radius ≈2.3 (relative error ~4e-4)
   — i.e. NOT a circle to any useful precision; the loci of K and L are some
   other (non-circular) curve as θ varies. Any attempted lemma of the form
   "K always lies on circle ω(θ-independent)" is false.
4. **Spiral similarity center S sending B↦K, C↦L (computed in closed form via
   the complex-number fixed-point formula, for each family member)**: S moves
   substantially (distance to A ranges 0.56–4.7, distance to Q ranges
   0.96–4.2) and does not fit a line to useful precision (residual ~1.8 vs.
   coordinate scale ~3) — S is neither a fixed point, nor confined to a fixed
   line or the family's own line ℓ. This directly refutes
   spiral-similarity-bootstrap's underlying hope that "O is the image of a
   fixed point under a spiral similarity tied to the hypotheses" — the
   analogous B↦K,C↦L similarity center itself has no such fixed structure,
   so there is no reason to expect O (circumcenter of AKL) to be one either.
   This corroborates the outline's own self-flagged doubt about step 5 and
   makes it a confirmed dead end, not just a suspicion.
5. **One-angle "circle-membership" candidates from steps 2–3 of the outline**
   (testing 6 different directed-angle pairings meant to place K or L on an
   auxiliary circle through 2 of the fixed points {B,C,M,N,Q} without using
   the other of {K,L}): of 8 candidate directed-angle identities tested
   (KB,KM vs LC,LN; KB,KA vs LC,LA; KM,KQ vs LN,LQ; AK,AQ vs AL,AQ; BK,BQ vs
   CL,CQ; MK,MQ vs NL,NQ; plus two "constant across family" checks:
   dirang(K,Q,K,M), dirang(K,Q,K,B), dirang(K,Q,K,A), and their L-analogues),
   **none hold as identities** except the two that are algebraically
   equivalent to the already-known target A,K,L,Q concyclicity itself
   (∠(KA,KQ)=∠(LA,LQ), and ∠(QK,QA)=∠(LK,LA) — the exact Step-3 target from
   fixed-point-concyclic.md). No intermediate one-angle shortcut was found;
   the concyclicity really does need the full 3-hypothesis chase, confirming
   round-1's exhaustive-4-point-subset search from yet another angle (dynamic
   family-wide sweep rather than a single-instance static check).

### Small-case / intuition notes (all labeled conjecture/numeric evidence only)
- The whole spiral-similarity-bootstrap framing (steps 1–5) is now
  numerically refuted at every non-trivial step (1, 2, 3, 4/5 as listed
  above); only its trivial step 6 (homothety h(A,1/2) sends
  perp-bisector(BC) to perp-bisector(MN)) survives, and that alone was
  already noted as insufficient by itself. **Recommendation: do not build
  out spiral-similarity-bootstrap.md as currently outlined next round** — it
  would very likely earn another RETHINK for the same reason the
  outline-reviewer gave it one in round 1, now with much stronger numerical
  backing for that verdict.
- The one live contribution from this lens is reframing the Step-3 gap as
  two separate single-point angle computations (∠(KA,KQ) as a function of
  the family parameter via hyps 1+3, and ∠(LA,LQ) via hyps 1+2) that must be
  shown equal, rather than a single 4-point concyclicity claim — this is
  the same underlying fact but may be more amenable to a direct trig
  computation (each angle is a function of one parameter θ and the fixed
  triangle data) than an abstract 4-point concyclicity chase. This is worth
  handing to the outliner as a possible variant framing of the SAME central
  gap (not a new opening around it) — CLAUDE.md's shared-gap-plateau rule
  still calls for a genuinely different top-level target elsewhere in the
  field (e.g. a direct trig-Ceva / algebraic identity route computing
  ∠(KA,KQ) and ∠(LA,LQ) in closed form and checking the polynomial identity
  with sympy, distinct from coordinate-bash's Gröbner approach and from
  fixed-point-concyclic's pure synthetic chase).
