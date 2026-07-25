# Outline review — round 8, imo-2026-02

Reviewed `/tmp/round-8/proof-outliner.md` against `current.md`,
`knowledge_base.md`, existing approach files, and this round's 3 explorer
reports. Independently re-verified every load-bearing new algebraic claim in
fresh `sympy` sessions (not copying any file's code).

## Independent verification performed

**(1) coordinate-bash-resultant-boundary's scale-invariant reduction.**
Reconstructed the polar reparametrization from scratch (`a=1`, `b=m cosA`,
`cc=m sinA`) and checked, symbolically:
- `B2/(1+u²)³ = -2(b sin3β+cc cos3β)` reduces exactly to `-2m·sin(A+3β)`
  (residual 0). **Confirmed exactly**, matches the outline's claim.
- `Z/(1+u²)` divided by `m` reduces exactly to
  `Q(m) = m²sin(A+β) - 4m sinβ - 4sin(A-β)` (residual 0, fully symbolic).
  **Confirmed exactly.**
- `sin(A+β)>0` unconditionally: the outline's 3-line argument (`β<∠B`,
  `A+∠B<π` since `∠C>0`, hence `A+β<π`; `A+β>0` trivially) is elementary and
  correct — no gap. **Confirmed.** This makes `Q` upward-opening always, a
  genuine, cheap, fully general fact ready to certify immediately.
- What remains genuinely open (correctly flagged as open by the outline, not
  overclaimed): discriminant `≥0` under `sin(A+3β)<0` (step 6), `M0≤r2`
  (step 7, stalled `Q(M0)` simplification), and the rare `r1>0` subcase
  (step 8). All three are honestly numeric-only per the explorer report —
  the outline does not claim more than it has.

**(2) coordinate-bash-resultant-boundary-pointwise's "two lines in ℂ"
reframing.** The claim that `L1=Im(d̄·V1(s2))` and `DK∝Re(d̄·V1(s2))` for the
same complex-affine `V1(s2)` is a correct, standard fact (cross and dot
products of a fixed vector `d` against a variable vector `V1(s2)` are
exactly `Im`/`Re` of `d̄·V1(s2)`, since `d̄v = (d·v) + i(d×v)` up to sign
convention). This is sound linear algebra, not hand-waving, and it is
type-correct progress: it turns "does the L1<0-selected root of an affine
function also satisfy an independent affine sign condition" into "where does
one line in ℂ, parametrized by s2, cross into a target open quadrant" — a
genuinely different mechanism from the already-exhausted both-roots-product
resultant trick (confirmed dead end this round: degree-20 unfactorable
remainder). Good diagnosis, well-posed new lever.

**(3) fixed-point-concyclic's ideal-membership corollary test (step 5,
6a/6b).** The design is correctly binary and honestly handles both outcomes:
if `Rem(u)` (after substituting the branch's rational parametrizations)
reduces to 0 modulo `⟨G2a,G3a⟩`, the whole route collapses to an already-
certified corollary (6a); if not, the file must report that honestly and
treat `Rem=0` as separate new content (6b). This mirrors exactly the
methodology that worked for the central identity `T`
(`lemmas/symbolic-genericity-certificate.md`), and the ring/variables match
(`t1,s2,u,a,b,cc`), so the plan is well-posed and directly executable, not
speculative. **One real gap in the outline's own step 7**: this round's
explorer flagged that the *existing* "Rem≈0 on the true branch" numeric
evidence is thinner than claimed (round 7's 3-sample base, and the
explorer's own quick fsolve replication got Rem≈-3.12, likely a setup bug
but unresolved) — the outline correctly puts a robust re-sweep as step 7,
but it should be sequenced *before*, not after, investing heavily in the
symbolic ideal-membership test, since if a careful large sweep instead finds
Rem is generically nonzero on the true branch, the whole corollary-test
plan is moot. Recommend the builder run step 7 first (cheap, <5 min) before
steps 3-6.

**(4) inversion-at-A-collinearity's soundness.** "A circle through the
center of inversion maps to a line" is a standard, correctly-stated
classical fact; the reduction to `det[K*-L*,Q*-L*]=0` is a valid
reformulation of A,K,L,Q concyclic. The outline is honest that this is *not*
known to reduce difficulty (explorer's own finding: cross-ratio realness and
post-inversion collinearity are classically equivalent formulations of the
same fact) — its value is technique/framing diversity (a determinant target
combinable with fixed-point-concyclic's already-bilinear Cramer machinery)
plus a real chance the inverted coordinates are lower-degree. This is a
legitimate speculative approach with an explicit, appropriately-scoped
fail-fast instruction ("abandon quickly within this round if step 5 doesn't
visibly simplify") — not a doomed line, not overclaiming. Well-posed and
answers CLAUDE.md's standing "put ≥1 genuinely different framing on the
table" instruction (population has been in one "sign/parity survives across
roots" shape for 3 rounds running now).

## Diversity assessment

- `coordinate-bash-resultant-boundary` / `-pointwise`: same underlying
  Weierstrass/resultant machinery, but — per the standing rule from round
  6 — these target genuinely different, non-overlapping sub-obligations
  (G2b exclusion vs. G2a-side same-root correlation) using different
  mechanisms this round (3-sinusoid quadratic-root comparison vs.
  complex-affine-line quadrant argument). Acceptable as siblings, not a
  redundant pair.
- `fixed-point-concyclic`: genuinely different mechanism (bilinear/Cramer's
  rule, zero root-counting) — the population's most technique-diverse live
  route, per round 7's rule; still alive and correctly prioritized.
- `inversion-at-A-collinearity`: new framing, built on fixed-point-concyclic's
  machinery but reformulates the *target* itself (determinant vs. realness)
  — satisfies CLAUDE.md's diversity push without being a fragment of another
  proof (it targets the whole problem end-to-end, same as its siblings).
- No approach is a slice of another proof; all four target the full OM=ON
  claim through their own complete (if partial) route. No fragment-splitting
  observed.
- All four gaps remain, in shape, "prove a sign/parity/uniqueness pattern
  over roots of a polynomial or a positioned line" — this shared shape
  (flagged since round 6) persists; `inversion-at-A-collinearity` and the
  complex-affine-line lever for `-pointwise` are the two most promising
  attempts this population has made yet at genuinely escaping that shape,
  so continuing to fund them is the right call rather than switching
  everything again.

## Verdicts

- **`coordinate-bash-resultant-boundary`** (advance) — **APPROVE**. Both
  linchpin identities (B2, Z-quadratic reduction) and the `sin(A+β)>0` lemma
  independently confirmed exact. Remaining steps (discriminant, M0≤r2,
  r1>0 subcase) are correctly scoped as open, not glossed over.
- **`coordinate-bash-resultant-boundary-pointwise`** (advance) — **APPROVE**.
  The complex-affine "two lines in ℂ" reframing is sound linear algebra and
  a genuinely different technique from the already-exhausted resultant-ratio
  extension; correctly avoids repeating the confirmed dead end.
- **`fixed-point-concyclic`** (advance) — **APPROVE, with a sequencing
  note**: run the large, careful numeric re-sweep of Rem on the true branch
  (step 7) *before* the symbolic ideal-membership test (steps 3-6), since
  the existing evidence base for "Rem≈0 on the true branch" is thin (3
  samples) and this round's explorer's own quick replication did not
  reproduce it cleanly (Rem≈-3.12, likely a bug but unresolved) — don't sink
  the ideal-membership effort before confirming the target claim is even
  numerically true at scale.
- **`inversion-at-A-collinearity`** (new) — **APPROVE**. Classically sound
  reformulation, correctly and honestly scoped as unproven-to-be-easier,
  with an explicit fail-fast instruction. Registered in the ranking pool.

No approach is RETHINK this round — all four are well-posed, buildable, and
none repeats a recorded dead end (the outline explicitly avoids the three
confirmed-dead levers: literal ptolemy-IVT transfer to the coordinate route,
both-roots-product resultant extension for the same-root question, and
"Rem=0 follows from Φ=0 plus bare realness alone").

## Ranking

Registered `inversion-at-A-collinearity` (cold-start 1500). Ranked the
sampled field against established approaches (anchoring newcomers/advances
to siblings and to the dormant Ptolemy family per this round's verified
progress): `coordinate-bash-resultant-boundary` (1664, strongest — two
identities independently confirmed exact this round) >
`coordinate-bash-resultant-boundary-pointwise` (1590, sound new complex-
affine lever) > `ptolemy-trig-identity` (1564) >
`ptolemy-trig-identity-parity-decomposition` (1545) >
`inversion-at-A-collinearity` (1493, new, untested) ≈
`fixed-point-concyclic` (1492, real machinery but thinner current numeric
base, flagged above) > `ptolemy-trig-identity-synthetic` (1431, dormant) >
`power-of-point-secants` (1341, dormant, known non-independent route).

build set: coordinate-bash-resultant-boundary, coordinate-bash-resultant-boundary-pointwise, fixed-point-concyclic, inversion-at-A-collinearity
