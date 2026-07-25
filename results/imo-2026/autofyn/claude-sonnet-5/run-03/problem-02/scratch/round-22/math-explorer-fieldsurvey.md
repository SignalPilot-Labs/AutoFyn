## imo-2026-02 — field survey (rest of population, sanity-check for landmines)

### 1. `coordinate-bash-resultant-boundary-pointwise-tangent-via-T` (independent (σ,τ)-route to T)

Read the full file. Status: `partial`, last built round 20, elo ~1783 but flagged `stale` in
the ranker (Elo predates round-21's outcome on the sibling). It only proves the **corner
value** `T(A*,β0(A*))=0` by an independent rational-arithmetic route (exact fractions
σ*=5/32, τ*=5/8, q1*=75/131072, r0*=-125/262144, verified by squaring to a rational
identity both sides = 421875/2199023255552) plus a *numeric* (finite-difference, not
certified) gradient at the corner. It explicitly has **4 open items still not even started**:
(1) a certified 2‑D directional-derivative bound (the corner here is a genuine 2‑D domain
corner, not a 1‑D curve — strictly harder than the D1/Tgt corners already closed elsewhere,
because you must control a whole cone of transverse directions, not one curve), (2) the
Lagrange-remainder assembly, (3) a certified interval sweep away from the corner, (4) the
gluing step. None of this has been attempted yet — this is NOT a "one paragraph" fix; it is
comparable in size to the machinery that took the `D1` lemma (rounds 15-18, several rounds)
to close on a *simpler* 1‑D domain.

**More importantly — this whole sub-gap may be moot this round.** Tracing the logic
(see §2 below and current.md round 21): `T≥0`/`G(β1)≥0` is only ever a proof obligation
on **Case (b)** (`β0(A)<β1<γ`), which is **already fully closed** (round 20, certified,
independently re-verified — `lemmas/t-nonnegative-on-case-b-residual-domain.md`). Case (a)
(`β1≤β0(A)`) is vacuous (round 21, certified). The round-21-discovered third scenario
(`β1≥γ`, i.e. `Y(γ)≥0`) needs **no `T` fact at all** — it is handled unconditionally by
Theorem 16.2's first branch, already proved gap-free in `coordinate-bash-resultant-boundary.md`
§16 (round 9): `Y` strictly decreasing on `(0,γ)` (`Y'=-2sin2β<0`) plus an explicit chain
`2K-f(β)>2K-f(γ)=sin(A+B)(2sinA-sinB)>0` via a certified identity — this is a complete,
independent, already-certified proof, not numeric. I independently checked that Theorem
16.2's β1 (defined by `Y(β1)=0`) is the same β1 as the round-21 gap's (defined by
`cosβ1=√X0`): since `Y(β)=2cos²β−2X0`, `Y(β1)=0 ⟺ cos²β1=X0 ⟺ cosβ1=√X0` (positive root,
β1∈[0,π/2)) — consistent, no hidden mismatch.

**Conclusion: if the tangent route's fix is exactly "splice Theorem 16.2's first branch into
Full-proof Step 2/3 as the third case," then `T≥0` on the *general* domain (which `via-T` is
grinding toward) is never actually needed at all** — the population already has everything
required. `via-T`'s remaining work would only become relevant as a genuine backup if the
splice attempt reveals the round-21 "third scenario" characterization itself has a further
gap (e.g. if `Y(γ)<0 ∧ β1≥γ` can co-occur, which would break the exhaustiveness — I did not
find such a case: `Y(γ)≥0 ⟺ β1≥γ` is a clean iff from `Y`'s strict monotonicity and
`Y(β1)=0` combined with `Y` continuous, so the three cases `β1≤β0(A)` / `β0(A)<β1<γ` /
`β1≥γ` are exhaustive and mutually exclusive by trichotomy on `β1` alone).

**Recommendation:** do NOT put `via-T` in this round's build set as a primary lever — its
own remaining work (2-D corner + sweep + gluing) is large and, per the above, likely
unnecessary if the splice works. Keep it registered as insurance only if the gapclosure
explorer/outliner finds the round-21 diagnosis itself has a snag (e.g. if Theorem 16.2's
citation doesn't actually cover the exact case as invoked, or if there's yet a *fourth*
sub-case lurking — recommend the outliner explicitly re-derive the full case-exhaustiveness
argument as part of closing this gap, not just cite it, given this lineage's 4-round history
of exactly this kind of oversight).

### 2. `ptolemy-trig-identity` + `-parity-decomposition` + `-synthetic` (independent framing)

Genuinely different top-level framing (Ptolemy equality on A,K,L,Q via Law-of-Sines chase,
not coordinates/resultants). Sharpest remaining gap, unchanged in substance since round 6:
`Ψ(τ,A,C)>0` on the bounded domain `τ∈(0,tan(min(B,C)))` (equivalently the four-branch
resolvent quartic `P(t)`'s claimed "exactly 3 negative, 1 positive real root" pattern,
verified only on 8 samples, round 8/20). **This is now a 15-round-old (rounds 6–21) plateau
specific to this family**: at least 5 distinct reduction levers have each been *proved*
algebraically equivalent in difficulty to `Ψ>0` itself (radical-isolation route, round 7;
Lemma-A discriminant route, round 7; Lemma-A/B decomposition, round 21 memory-rule; the
resolvent-quartic's e4<0 recasting, round 8) — i.e. every "cheap reformulation" tried so far
provably collapses back to the same sextic positivity claim. `ptolemy-trig-identity-synthetic`
has an untried, flagged-but-never-dispatched lever (direct monotonicity/convexity comparison
of α(θ) vs β_L(θ) as functions of the shared parameter θ, round 16 note) — this is the one
genuinely fresh idea sitting in the population for this family, still unbuilt.

**Is progress plausible this round?** Low-to-moderate. No new lever has been identified since
round 16 (the α(θ)/β_L(θ) monotonicity idea, itself untested), and every attempted shortcut
has independently verified as circular. Given the coordinate-route fix is diagnosed as
plausibly closing the *entire problem* this round, I recommend NOT prioritizing a ptolemy
build this round — but if the outliner wants insurance against the tangent-route fix failing,
the monotonicity-in-θ lever is the correct next thing to try here, not another
resultant/discriminant reformulation (those are now exhausted with proof, not just suspicion).

### 3. Scan for other silent-missing-branch ("phantom gap") risk elsewhere in the population

Checked Status/last-note of every other live sibling: `coordinate-bash-resultant-boundary-
pointwise` (parent, `partial`, last built round 9-10 machinery only), `-pointwise-sos`
(`partial`, round 18, diagnostic-only, no case-split claim), `-pointwise-tangent-twopoint`
(`partial`, round 12, an unfinished concavity/positivity lever, no completed casework to
audit). None of these currently carry a "Full proof"/solved claim with casework to silently
miss — the pattern that bit rounds 17/18/19/21 is specific to the `-tangent` file's own
"Full proof" assembly step (a 2‑variable domain with several nested case splits: (I)/(II),
Case a/b, sign(P), sign(E), Y(γ) sign), which is uniquely complex among the population's
approaches. `fixed-point-concyclic` and `ptolemy-*`'s remaining gaps are each a single
scalar inequality (`Rem=0`, `Ψ>0`), not a multi-branch case tree, so there's structurally
much less room for a silently-dropped branch there. `spiral-similarity-bootstrap` is a
negative/diagnostic result, no casework. I did not find a second landmine — the risk is
concentrated exactly where round 21 found it (the `-tangent` file's Full Proof Step 2-4
case split), and per the round-21 write-up the fix is understood but not yet spliced in.

One thing worth flagging to the outliner as a rigor check (not a new gap, a caution): when
the splice is written up, explicitly re-verify (don't just cite) that the three cases
(`β1≤β0(A)`, `β0(A)<β1<γ`, `β1≥γ`) are jointly exhaustive AND that Theorem 16.2's proof
of the middle inequality (`2K-f(β)>2K-f(γ)=sin(A+B)(2sinA-sinB)>0`) doesn't itself have an
unstated sub-case (e.g. sign of `2sinA-sinB` — worth a two-line explicit check since this
same lineage has now produced 4 near-miss overclaims from exactly this kind of unstated
sub-case).

## Recommendation for build set

- Primary: whatever slug the gapclosure explorer/outliner is advancing on
  `coordinate-bash-resultant-boundary-pointwise-tangent` (splice Theorem 16.2's first branch
  into Full Proof Steps 2-4) — this is the fastest path to `solved` this round per the above
  analysis (the needed fact is already certified, only the assembly is missing).
- Do NOT build `coordinate-bash-resultant-boundary-pointwise-tangent-via-T` this round as a
  primary lever — its own remaining work (2-D corner Lagrange-remainder + sweep + gluing) is
  large and probably unnecessary if the splice succeeds. Keep as a documented backup only.
- Do NOT prioritize `ptolemy-trig-identity`/`-parity-decomposition` this round — 15-round
  plateau, all cheap reformulations proven circular; only fresh untried lever is the
  round-16 θ-monotonicity idea in `-synthetic`, worth a single exploratory build only if the
  tangent-route splice fails or the outliner wants diversity insurance.
- No new landmine found elsewhere in the population; the risk pattern from rounds 17-21 is
  isolated to the `-tangent` file's own multi-case assembly and is understood.

## Knowledge-base / crux notes
No new KB entries beyond what's already cited (Weierstrass substitution, resultant/Gröbner
elimination, MVT/Lagrange-remainder, tangent-line trick per crux `aimo-0005`, all already in
use). Per repo history (round 1 finding, still true), the crux corpus has no geometry-domain
entries relevant to this problem; did not re-query given prior rounds' documented negative
result and the round budget being better spent on the audit above.
