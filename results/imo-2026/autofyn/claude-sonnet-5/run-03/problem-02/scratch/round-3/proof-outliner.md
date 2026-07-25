## imo-2026-02

### Framing note (per CLAUDE.md's shared-gap-plateau rule)
This round's `math-explorer-newframing` ran an exhaustive negative search
(inversion at A, alternate 4-point concyclicities B/K/L/C and K/L/M/N,
radical-axis-of-O, fixed-point/fixed-direction of line KL, and a re-check of
`spiral-similarity-bootstrap`'s one-angle circle-membership idea) and found
**no** viable alternative top-level target: everything either collapses back
to the AKLQ-concyclic identity or is outright numerically false. Combined
with round 2's spiral-lens exhaustive refutation, this is now two
independent rounds of negative search over the auxiliary-construction space.
Per CLAUDE.md, the rule is satisfied by having genuinely tried a different
framing and found none — the population below stays on the AKLQ-concyclic /
`O·(C−B)=(|C|²−|B|²)/4` target but diversifies by **technique** (Gröbner
elimination, complex cross-ratio, Ptolemy/trig) and, within
`coordinate-bash-resultant`, by **two different levers** for the one
remaining sub-gap (branch selection). If round 4 still can't close branch
selection by either lever, the outliner should treat that specifically
(not the whole identity) as the next thing to re-examine structurally.

---

### 1. `coordinate-bash-resultant` — revise (primary, closest to solved)

Target: OM = ON for every valid configuration (K,L) of the original
problem — the full problem statement, via the certified reduction
`OM=ON ⟺ O·(C−B)=(|C|²−|B|²)/4` (`lemmas/vector-reduction-OM-ON.md`).

Technique: Weierstrass tangent-half-angle rationalization + rotation
parametrization + homogeneity-decoupling + Gröbner-basis ideal-membership
(knowledge_base.md polynomial-ideal-membership / Buchberger's algorithm),
now run **fully symbolically** (all triangles at once), plus a synthetic
acute-angle argument to close branch selection.

Skeleton:
  1. Import §§1–2 verbatim (reduction + rotation parametrization + Cramer
     circumcenter formula) — already certified, no re-derivation.
  2. **Replace §2's concrete triangle with the fully symbolic setup**
     `A=(0,0), B=(a,0), C=(b,cc)` (three free real parameters), using
     `L = C + s2·R(β)(A−C)` (i.e. `s2 = t2/|AC|`, absorbing `|AC|` so no
     square root enters the ring — the one change vs. the concrete case,
     reported by this round's genericity explorer as costing nothing).
     — by direct substitution, reproducing the round's `<10s` sympy pipeline.
  3. Rebuild `eq2, eq3`, confirm the homogeneity-decoupling factorization
     `eq2 = t1²·g2(s2,u,a,b,cc)`, `eq3 = s2²·g3(t1,u,a,b,cc)` **holds
     symbolically, exactly as the certified lemma
     `lemmas/homogeneity-decoupling-rotation-param.md` already guarantees
     geometrically** — by exact polynomial division, zero remainder.
  4. Factor `g2 = -(b²+cc²)²(u²+1)·G2a·G2b`, `g3 = -a²(u²+1)·G3a·G3b`
     (symbolic analogues of the concrete `G2a,G2b,G3a,G3b`) — by
     `sympy.factor`.
  5. Build symbolic target `T(t1,s2,u,a,b,cc)` (numerator of
     `O·(C−B) − (|C|²−|B|²)/4`) — by direct substitution into the Cramer
     circumcenter formula.
  6. **Genericity certificate**: `Gröbner([G2a,G3a], t1,s2,u,a,b,cc,
     grevlex)` (18 generators, ~2.6s), `reduce(T) = 0` — i.e.
     `T ∈ ⟨G2a,G3a⟩ ⊂ ℚ[t1,s2,u,a,b,cc]` for **every** `a,b,cc`
     simultaneously, cross-checked by an independent pseudo-remainder chain
     (`sp.prem` twice) also giving 0. This **replaces** the round-2
     concrete-triangle certificate outright — gap 1 (genericity) closes.
  7. **Branch selection (gap 2, the one remaining step)**: prove, for every
     triangle and every valid parameter, that the correct branch is
     `G2a=G3a=0` (not `G2b,G3b`). Reduce this — as the sign-lemma explorer
     found — to the synthetic claim: **∠LBK, ∠LNC, ∠LCK, ∠BMK are always
     acute**, i.e. `BL·BK>0`, `NL·NC>0`, `CK·CL>0`, `MB·MK>0`. This is
     because the squaring in `(†)` that produced `eq2/eq3` from the true
     `cos`-equality is only ambiguous in the sign of the dot products, and
     `G2a/G3a` was constructed (by sympy's factorization) to correspond to
     the `+,+` sign choice — this correspondence must be verified
     explicitly in the writeup (a short check, not re-derivation), then the
     acute-angle fact settles it.
  8. Attempt the acute-angle proof via **lever 1** (length/position bound):
     `K` interior to triangle `BMC` with `BM=AB/2` short forces `BK` short;
     combined with the containment hypotheses ("K inside angle LBA", "L
     inside angle ACK" — the exact conditions that exist to pin the branch,
     per the per-role memory rule on signed/directed angles), bound
     `∠LBK` via a triangle-angle-sum argument at B. Symmetric argument at
     C, N, M by the certified σ-symmetry (`lemmas/sigma-symmetry.md`, swap
     B↔C,K↔L,M↔N) — proving it at one vertex pair gives the other for free.

Key lemmas (claim + mechanism):
  - **Symbolic homogeneity-decoupling** — because `BK=t1·(direction)`,
    `CL=s2·(direction)` are exactly homogeneous (zero intercept) in
    `t1,s2` regardless of `a,b,cc`, so squaring-and-cross-multiplying the
    angle-equality hypotheses always isolates a `t1²`/`s2²` factor — a
    coordinate-free fact already certified, now shown to survive
    symbolic `(a,b,cc)`.
  - **Genericity certificate** — `T ∈ ⟨G2a,G3a⟩` for symbolic `a,b,cc`,
    because Buchberger's algorithm + normal-form reduction is a decision
    procedure for ideal membership (Cox–Little–O'Shea), verified by two
    independently-coded methods (Gröbner reduce, pseudo-remainder chain).
  - **Acute-angle branch lemma (open, the crux of gap 2)** — conjectured
    (9 triangles × ~150 points, max angle ≈49.4°, real margin below 90°)
    but not yet proved in general; needs the containment-hypothesis bound
    of skeleton step 8.

Open gaps: step 8 (the acute-angle proof) is the ONLY thing left to close
this approach to `solved` — everything else (steps 1–7) is either already
certified or a direct, fast, reproducible rerun of certified machinery.
Also needs: the explicit check that the `+,+` sign choice really is what
`G2a/G3a` (as opposed to `G2b/G3b`) encodes (flagged by the sign-lemma
explorer as needing to be written out, likely short).

Cases to cover: none additional — the symbolic run already covers every
triangle shape at once; the acute-angle claim needs no triangle-type
casework per the numeric evidence (acute, obtuse-at-B, thin scalene, near-
right all tested and gave acute hypothesis angles).

Watch out for: (a) don't conflate this branch-selection sign question (a
DOT-PRODUCT / acute-vs-obtuse question) with `fixed-point-concyclic`'s
already-closed H2/H3 sign question (a CROSS-PRODUCT / rotation-direction
question) — the sign-lemma explorer verified these are genuinely different
facts, the cross-product technique does not transfer; (b) if step 8 doesn't
close quickly, fall back to the copy below (boundary/continuity argument)
rather than repeating the same lever.

---

### 2. `coordinate-bash-resultant-boundary` — copy of `coordinate-bash-resultant`

Two independently viable ways to close the SAME gap 2 (branch selection)
are on the table — pursue both in parallel per CLAUDE.md's copy rule.

Target: same as above (OM=ON, full problem).

Technique: identical to approach 1 through step 7, but closes branch
selection via a **continuity/boundary argument** instead of a direct
length bound:
  8'. The valid parameter range (for fixed triangle ABC) is a connected
      interval of `β` (established in earlier rounds — the containment
      conditions carve out a connected sub-range). Each hypothesis angle
      (`∠LBK` etc.) is a continuous function of `β` on this interval. An
      angle can only cross from acute to obtuse by passing through exactly
      90°, i.e. through a dot-product zero. So it suffices to (i) rule out
      dot-product-zero anywhere strictly inside the valid range — via the
      resultant computation already run on the concrete triangle
      (`Res(G2a,G2b)`, `Res(G3a,G3b)` share no common root with `t1,s2>0`
      inside the range; rerun symbolically or via a degree/sign argument
      on the resultant's real roots for general `a,b,cc`), and (ii) check
      ONE point (or the boundary limit `β→0⁺`, or the containment-breaking
      boundary) is acute — giving acuteness on the whole range by the
      intermediate value theorem, without needing the length-bound
      synthetic argument of approach 1's step 8.

Key lemmas:
  - **No branch-crossing inside the valid range** — because the resultant
    `Res_{s2}(G2a,G2b)` (resp. `Res_{t1}(G3a,G3b)`) has no roots with
    `0 < u <` the containment-breaking threshold (established on the
    concrete triangle at `u≈0.2655`; needs a symbolic/general version, or a
    Schwartz–Zippel-style multi-triangle check as an honest interim step if
    the fully symbolic resultant sign argument doesn't close quickly).
  - **Boundary acuteness** — as `β→0⁺` (K→B, L→C degenerate limit) or at
    the containment boundary, the hypothesis angles have an explicit
    limiting value checkable by direct substitution/limit, giving the IVT
    anchor point.

Open gaps: both (i) and (ii) above — this is a genuinely different
mechanism from approach 1's step 8 (topological/IVT vs. direct metric
bound), so a stall in one doesn't imply a stall in the other.

Cases to cover: none beyond the single continuity argument, but the
boundary-limit computation at `β→0` needs care (K,L degenerating, some
ratios may need L'Hôpital / leading-order expansion — flag as a real
computation, not hand-waved).

Watch out for: this lever needs the "valid range is connected" fact to
actually be re-confirmed/cited (it was established numerically in earlier
rounds — check whether it has a synthetic proof anywhere in the population
before assuming it as given).

---

### 3. `fixed-point-concyclic` — revise

Target: same (OM=ON, full problem), via A,K,L,Q concyclic
(`lemmas/amnq-concyclic-and-reduction.md`) and a complex cross-ratio route
(`lemmas/cross-ratio-real-concyclic-criterion.md`).

Technique: complex-number cross-ratio computation (distinct mechanism from
the Gröbner route above — this diversifies the population by technique
even though the top-level target is shared, consistent with this round's
finding that no different top-level target exists).

Skeleton:
  1. Import the certified cross-ratio-real criterion and the vector/Q setup
     verbatim (no re-derivation).
  2. **Splice in this round's closed H2/H3 sign derivation verbatim**
     (math-explorer-signlemma Part A): the four cross-product identities
     `cross(BA,BC)=-bxc`, `cross(CA,CB)=+bxc`, `cross(NB,NC)=+bxc/2`,
     `cross(MB,MC)=+bxc/2` (all proved by direct symbolic expansion, valid
     for every CCW triangle, `bxc=b×c=2·signed_area(A,B,C)`) — this fully
     replaces the file's flagged "representative triangle" sentence and
     removes the round-2 overclaim entirely. State (H1),(H2),(H3) with
     these now-general signs.
  3. Push the central elimination `(H1)∧(H2)∧(H3) ⟹ χ∈ℝ` (χ = the
     cross-ratio of A,K,L,Q) — this is the one remaining gap. Given
     approach 1's now-generic algebraic certificate exists as a fallback,
     this route's marginal value is (a) a genuinely different, possibly
     shorter, complex-analytic proof if it closes, and (b) cross-
     validation of approach 1's result by an independent method — both
     worth the round's effort.

Key lemmas:
  - **General vertex-sign facts (now closed)** — the four cross-product
    identities above, because each reduces algebraically to `bxc` or
    `bxc/2` exactly (e.g. `cross(NB,NC) = (b−c/2)×(c/2) = (b×c)/2` since
    `c×c=0`), with no residual terms and no case split.
  - **χ∈ℝ elimination (open)** — express χ as an explicit rational
    function of the angle parameters via (H1)-(H3), then show the
    imaginary part vanishes identically on the constraint variety — the
    remaining hard step, structurally analogous to approach 1's Gröbner
    target but in the complex/cross-ratio ring instead of the real
    coordinate ring.

Open gaps: step 3, the central elimination — unchanged in difficulty from
round 2's assessment, but now built on a fully clean (no-overclaim)
foundation.

Cases to cover: none beyond the AB vs AC sign split already known to exist
(shared with `ptolemy-trig-identity`, see below) — flag it explicitly here
too so this route doesn't silently drop it.

Watch out for: don't re-introduce the single-example sign check this round
closed — always cite the four general identities, not a numerical check.

---

### 4. `ptolemy-trig-identity` — advance

Target: same (OM=ON), via the certified Ptolemy-equality ⟹ concyclic
theorem (`lemmas/general-ptolemy-equality-concyclic.md`) applied to
A,K,L,Q.

Technique: trigonometric/length identity (Ptolemy), a third genuinely
distinct mechanism from Gröbner-elimination and cross-ratio — keeps the
population's technique diversity even though the newframing search found
no new top-level target.

Skeleton (continuing from round 2's state, no re-derivation of Lemmas 1–4):
  1. Use Lemma 4's closed form `AQ = |b²−c²|/(2a)` and the exact cyclic
     order A,K,L,Q (established round 2) to state the Ptolemy target
     `AL·KQ = AK·LQ + KL·AQ` (or its σ-swap, depending on sign(AB−AC)).
  2. **Resolve the AB vs AC case-split synthetically** (round 2 asserted it
     from 2 numerical examples only — an open gap) using the same
     signed-area technique this round's sign-lemma explorer used to close
     `fixed-point-concyclic`'s H2/H3 gap: the case split is plausibly
     governed by which of `cross(BA,BC)`-type sign facts flips as AB, AC
     swap magnitude order — check whether the general four-identity
     derivation in approach 3 above (imported, not re-derived) already
     settles which Ptolemy pairing applies, avoiding a second from-scratch
     sign argument.
  3. Compute closed forms for KQ, LQ (in the angle parametrization of
     Lemmas 1–3) and complete the trig identity check that round 2 left
     open.

Key lemmas:
  - **AQ closed form** (already certified) — `AQ=|b²−c²|/(2a)` by direct
    computation from Q's reflection definition.
  - **Case-split criterion (open)** — sign(AB−AC) determines the Ptolemy
    pairing; leverage approach 3's general sign identities to attempt a
    proof instead of a fresh derivation, since the underlying geometric
    fact (which side of the configuration "AKLQ" the sign asymmetry
    appears on) plausibly comes from the same B/C-vertex sign asymmetry.

Open gaps: step 2 (case-split proof) and step 3 (KQ, LQ closed forms +
trig identity completion) — both flagged as open in round 2, neither
touched by this round's explorers directly, but step 2 now has a concrete
lever to try (reuse of approach 3's general sign identities) instead of
being stuck.

Cases to cover: AB > AC and AB < AC (the two Ptolemy pairings) — both must
be closed; AB = AC (isosceles) remains the flagged degenerate edge case
(Q=A) needing separate handling, still outstanding since round 1.

Watch out for: the isosceles case AB=AC (Q=A) is still unhandled by any
approach in the population — flag it as a gap that must eventually be
closed regardless of which approach reaches `solved` first (it doesn't
block the generic case, but "solved" for the full problem needs it too).

---

### Held, not in build set this round
- `coordinate-bash` (round 1/2 negative report on σ-symmetry shortcut and
  resultant chains) — its Sylvester-resultant content is now superseded by
  approach 1's cleaner Gröbner recipe; no new lever to try, keep it live in
  the population (do not delete) but do not re-dispatch a builder.
- `power-of-point-secants` — already self-reported as "not an independent
  route" (same central gap, different language); nothing new to add this
  round.
- `spiral-similarity-bootstrap` — doubly refuted (round 2 spiral-lens +
  this round's newframing explorer); do not revive.

Build-set recommendation: coordinate-bash-resultant,
coordinate-bash-resultant-boundary (copy), fixed-point-concyclic,
ptolemy-trig-identity.
