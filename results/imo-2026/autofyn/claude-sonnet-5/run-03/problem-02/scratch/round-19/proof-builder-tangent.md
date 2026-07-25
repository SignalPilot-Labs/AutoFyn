# proof-builder report: coordinate-bash-resultant-boundary-pointwise-tangent (round 19)

## Task
Close "Open gap 7" (Case (a) of "Full proof" Step 3), per the round-18/19
dispatch's suggested fix: prove `f'(β)>0` on all of `(0,γ)` (already
inside Theorem A's own proof, not just its stated `(β0,γ)` conclusion)
plus `f(0)=sinA(2sin(A+B)−sinB)≥0`, then combine via MVT/monotonicity to
get `f(β1)>0` throughout Case (a).

## What I did
1. **Fully proved both halves of the suggested fix.**
   - `f(0) = sinA·(2sin(A+B) − sinB) > 0` strictly: reduces to
     `sinB ≤ sinC` (given the file's standing WLOG `B ≤ C`), proved by a
     clean two-case argument (`C ≤ π/2`: monotonicity of sin on `[0,π/2]`
     directly; `C > π/2`: `A>0 ⟹ π−C = A+B > B`, so `0<B<π−C<π/2`, again
     monotonicity). No degenerate-limit subtlety needed since `A>0`
     strictly for every genuine triangle. Then `2sinC−sinB = sinC +
     (sinC−sinB) ≥ sinC > 0`.
   - `f'(β) = sin(A+β)cosB + sin(A+B−β) > 0` on the *whole* `(0,γ)`: this
     is literally Theorem A's own proof in
     `lemmas/claim-I-closed-and-claim-II-caseA-closed.md` — the sign
     argument only uses `β∈(0,γ)`, never `β>β0`.
   - Combined via MVT on `[0,β1]`: `f(β1) > f(0) > 0` for every
     `β1∈(0,γ)`, in particular for Case (a)'s `β1∈(0,β0(A)]`. This is a
     genuine, fully rigorous, gap-free new sub-lemma.

2. **Then traced whether this actually closes Case (a) (per the dispatch's
   explicit instruction to re-verify the whole chain, not just patch the
   locally-flagged step) — and found it does NOT.** Case (a)'s actual
   target, per the file's own Step 2 (stated uniformly for all
   `β1∈(0,γ)`, no case split in the target itself), is `G(β1)≥0`, not
   `f(β1)>0`. This is corroborated by an already-certified,
   `β0`-independent lemma, `lemmas/case-b-p-le-0-and-e-ge-0-closed.md`
   ("Case (b) target `G(β1)≥0`"), which proves `G(β1)≥0` unconditionally
   whenever `P≤0` or `P>0∧E≥0`, with **no** restriction on `β1` vs `β0(A)`
   anywhere — leaving only `P>0∧E<0` open.
   - Independent verification (fresh `sympy`, 50-digit precision, own
     `500,000`-sample sweep restricted exactly to the file's own literal
     Case-(a) domain): `G(β1)≥0` fails at ≈70% of genuine Case-(a) points.
   - Decisive finding: **every single failure found has `P>0∧E<0`
     exactly** — i.e. lies precisely in the one residual sub-case of
     `case-b-p-le-0-and-e-ge-0-closed.md` that is **still open across the
     entire population**. That sub-case reduces (via
     `lemmas/case-b-e-lt-0-t-factorization.md`) to `T := B_c²X0 − E² ≥ 0`
     — the same `-q1,-r0` Positivstellensatz-certificate target that has
     been the population's single most persistent open gap since round
     10, unresolved by `coordinate-bash-resultant-boundary`'s LP/SDP
     search or `coordinate-bash-resultant-boundary-pointwise-sos`'s SDP
     search across many rounds.
   - Produced an exact 50-digit witness triangle (`A≈0.010023,
     B≈1.499257, C≈1.632312`) confirming `β1≤β0<γ` (genuine, domain-
     nonempty Case-(a) point), `f(β1)≈0.719>0` (Sub-result A holds, as
     proved) but `G(β1)≈−0.679<0` strictly (the actually-needed fact
     fails), with `P≈0.999>0, E≈−0.499<0` matching the still-open regime.

## Outcome
- **Status left as `partial`** (not solved). I did NOT claim solved.
- Closed, in full, a genuine sub-lemma (`f(β)>0` on all of `[0,γ)`),
  recorded as a Promotable lemma with an explicit caveat that it does not
  establish `G(β1)≥0`.
- Re-diagnosed Open gap 7 much more precisely than round 18: it is not a
  citation-scope slip fixable by extending one lemma's stated interval —
  Case (a)'s nonvacuous residual is *identical* to the population's
  oldest, most persistent open problem (the `T≥0`/`-q1,-r0`
  Positivstellensatz certificate, open since round 10, attacked
  unsuccessfully by two sibling approaches across many rounds). This has
  been the route's Case (a) framing since round 11 (8 rounds), never
  caught until this round's mandated whole-chain re-audit.
- Corrected the "Full proof" section's Conclusion paragraph, which
  previously (as filed by round 18's builder, before the round-18
  reviewer's rejection) implied a full `∎`; it now explicitly states Case
  (b) alone is closed and withholds `∎` for the whole claim.
- Updated `## Approaches tried`, `## Status`, the numbered gap list (item
  7), "Full proof" Step 3, the Conclusion paragraph, the round-18
  dependency-chain audit (added a round-19 addendum explaining what it
  missed), and `## Promotable lemmas` in
  `results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-pointwise-tangent.md`.
  No other files touched (per the "stay in your lane" instruction —
  `lemmas/case-b-p-le-0-and-e-ge-0-closed.md` and
  `lemmas/case-b-e-lt-0-t-factorization.md` were only read, not edited;
  both were already independently certified in round 10 and are cited,
  not re-derived, here).

## Whole-route status (honest assessment)
The route is **not** solved and, based on this round's finding, is now
understood to be **substantially further from solved** than round 18
believed: Case (b) (via gaps 5+6) is genuinely, fully closed, but Case (a)
is not a formality — its hard residual is provably the same open problem
that has resisted the whole population's dedicated effort (LP obstruction
searches, SDP Positivstellensatz searches) since round 10. Any future
round on this route should attack `T := B_c²X0 − E² ≥ 0` directly (or
equivalently the `-q1,-r0` certificate) rather than treating Case (a) as
a citation-scope fix — this is now a shared central target across at
least three sibling approaches in the population
(`coordinate-bash-resultant-boundary`, `-pointwise-sos`, and this file),
and should probably be dispatched as a single unified sub-target next
round rather than three separate rediscoveries of the same wall.

File: `results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-pointwise-tangent.md`
(Status: partial)
