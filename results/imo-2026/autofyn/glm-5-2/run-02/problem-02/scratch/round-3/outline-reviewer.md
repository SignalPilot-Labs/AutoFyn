## imo-2026-02 outline review (round 3)

Problem is SOLVED since round 2 (analytic-branch-cert + analytic-resultant-cert, both APPROVE). This round strengthens with two independent synthetic rival certificates. I read the outliner field, both approach files, the antipode scout certificate, the live ranking, CLAUDE.md, and the per-role rules. I **independently re-ran `/tmp/probe_reduce.py`** (per the NEVER-trust-prior-field-claim rule): remainder `is_zero = True` reproduced in 82.8 s, step-1 remainder degree 3 in `t_γ` (nonzero, expected), step-2 remainder zero. I also independently printed and numerically evaluated the two divisor leading coefficients — both generically nonzero at a generic rational point (`tA=tB=...` sample: `0.334`, `0.154`), confirming the field-division is genuine (not pseudo-remainder).

### antipode-rightangle — revise (close the §7 gap via sequential field-division) — APPROVE

- **Whole attempt.** Targets `OM=ON` end-to-end via the homothety+antipode+Thales route; the closing identity (T) is the antipode framing's own derivation, not a sub-lemma handed off to a sibling.
- **Right technique.** Sequential univariate polynomial field-division over `QQ.frac_field(t_A,t_B,t_α,t_β)[t_γ]` then `[...][t_β]` is the SAME certificate style that closed `analytic-branch-cert` Prop 4 (reviewer-certified). The half-angle-only-on-`(γ,β)`-keeping-`t_A,t_B,t_α`-as-atoms trick is the documented fix for the round-2 `expand_trig` blowup (the scout's 35-monomials-vs-10⁴ finding). Sound.
- **Sound skeleton.** Steps 1–7 retained from rounds 1–2 (all reviewer-certified rigorous). Step 8 is the new certificate; I reproduced it: `sp.div(num, C1_num, t_γ, …)` → remainder `r1` (degree 3, nonzero); `sp.div(r1, C2_num, t_β, …)` → remainder `is_zero = True`. Mechanism is exact: univariate polynomial division over a field is genuine field division when the divisor's leading coeff is a unit, verified nonzero above.
- **Load-bearing lemmas with mechanism.** Both lemmas are stated with a one-line mechanism and both mechanisms check out: (i) the sequential-division ideal-membership lemma — exactness of univariate division over a field when the leading coeff is a unit (verified nonzero); (ii) the leading-coeff-genericity lemma — a nonzero rational function vanishes only on a proper Zariski-closed subset, so one numerical eval certifies genericity (I performed it).
- **Denominator-clearing follow-up.** Step 8e correctly notes the field-division yields `(T')_num = q1·(C1)_num + q2·(C2)_num` with rational-function `q1,q2`; multiplying by the LCM of coefficient denominators gives a polynomial identity over `Z[t_A,t_B,t_α,t_γ,t_β]`. Mechanical; the builder should print `q1, q2`, the LCM `D`, and the explicit `Q1, Q2` and state the polynomial identity.
- **Independence.** Does NOT cite `analytic-branch-cert`'s saturation identity. The (T') coordinate reformulation is the antipode framing's own; the ideal-membership certificate is an independent close. Tactic (c) — invoke analytic-branch-cert as a black box — is correctly flagged as a FALLBACK ONLY that forfeits independence; since Step 8 is verified, the fallback is not triggered. If the builder's reproduction somehow fails (it should not), the builder MUST flag this and defer rather than silently fall back to (c).
- **Cases.** None — parameter-free polynomial identity valid for every non-degenerate triangle simultaneously (no casework, no "find all" bound/construction pair needed).
- **Avoids recorded dead ends.** Explicitly avoids `expand_trig` (the round-2 blowup); explicitly forbids the round-1 isogonality/three-similarities trap. ✓
- **Small-case sanity.** Reproduced remainder 0; verified leading coeffs nonzero. ✓

Verdict: **APPROVE.** This is the high-confidence build target this round. The builder's job is mechanical: reproduce `/tmp/probe_reduce.py` in the approach file, print both quotients and the zero remainder, perform the one-line leading-coeff-nonzero check (one numeric eval), and clear denominators for the polynomial-ring certificate. If the builder's reproduction fails (it should not, given the scout's and my independent reproductions), the builder MUST flag this and defer rather than silently fall back to (c).

### power-secant-product — revise (Step 9 — directed-trig cancellation) — APPROVE (with deferral fallback intact)

- **Whole attempt.** Targets `OM=ON` end-to-end via the secant-power route; the crux `(**)_corr` is the power framing's own derivation.
- **Right technique.** The frac_field-atom symbolic check mirrors the antipode scout's verified pattern; the directed-separation sign rule (Step 8's separation-sign rule, applied to ONE verified config) is the principled replacement for the numpy acute-angle pick that stalled round 2. Sound *in principle*.
- **Sound skeleton (steps 1–8).** All retained from rounds 1–2, reviewer-certified rigorous. Step 9's two sub-steps are precisely located.
- **Load-bearing lemmas with mechanism.** Both are stated with a mechanism: (i) directed-separation sign rule — sign of cross-ratio is `−` iff the pairs separate, constant on connected components (the sine-of-arc form acquires `±1` exactly when a directed angular difference crosses a `2π` boundary); (ii) branch-connectedness — the inside-hypothesis region is convex (hence connected) and the cross-ratio sign is locally constant. Both check out as principles.
- **The single real risk — 9a (sign-pinning).** This is the exact numpy-sign-trap that stalled round 2. Unlike antipode (where the scout *verified* remainder 0), the power scout did NOT verify 9b symbolically — 9b is conjectured "Expected: remainder zero" but unrun. So the builder is attempting 9a + 9b for the first time. The dispatch correctly characterizes this as "sound but riskier."
- **Honest deferral path.** The outline correctly states: if 9a cannot be rigorously closed (signs still unresolved, or 9b run with guessed signs), defer power (CHANGES REQUESTED → deferral), NOT RETHINK — the framing is sound, the gap is just hard. The approach stays alive (`partial`). This is the right call and the dispatch endorses it.
- **Independence.** Explicitly forbids citing antipode's `(T')` certificate (forfeits independence). The symbolic check is over `(**)_corr`, the power framing's own crux. ✓
- **Builder instructions to emphasize.** (a) Pin signs by directed-separation (mod π, cyclic-order-based) on the verified config `A=(0,0),B=(4,0),C=(1,3),K=(2.8,0.49465),L=(1.0479,2.3099)` — NOT by `numpy.arccos`/`arctan2`. (b) Only AFTER 9a is rigorous, run 9b with `sin/cos` (or `t_x`) as frac_field atoms (never `expand_trig`). (c) If 9b returns a NONZERO remainder, do NOT claim completion — the sign-pinning may be wrong; flag for deferral. (d) If 9a stalls, defer (do not force a half-baked 9b with guessed signs; the dispatch explicitly forbids this).
- **Avoids recorded dead ends.** Avoids the round-1 `b−β` sign bug (corrected to `sin(b+β)`); avoids `expand_trig` blowup; avoids citing antipode. ✓

Verdict: **APPROVE** with the deferral fallback intact. The framing is sound, the gap is precisely located, and the principled sign-pinning mechanism (directed-separation, not numpy picks) is the right tool. The honest deferral path is correctly written and the dispatch endorses it. The expected reviewer routing this round: if the builder closes 9a+9b with remainder 0 → APPROVE; if 9a stalls or 9b is run with guessed signs → CHANGES REQUESTED → deferral (NOT RETHINK).

### Correlation risk (noted for the orchestrator)

The two SOLVED analytic approaches (`analytic-branch-cert`, `analytic-resultant-cert`) **share the saturation-identity backbone** — `analytic-branch-cert` directly proves the saturation identity `Qt2·e3_line − et2·Q_line = D₀·G` (Prop 4), and `analytic-resultant-cert` leans on that same saturation identity for the exceptional isosceles stratum (§10 generic-to-all). They are two certificates of the *same* closing identity, not two fully-independent proofs. A single flaw in the saturation identity would sink both. This is a mild (not blocking) correlation — the saturation identity has been independently verified by true field division (remainder 0) and cross-checked by `sp.simplify`, so the shared dependency is itself well-certified. **An independent synthetic APPROVE (either antipode via `(T')` ideal-membership, or power via cross-ratio + arc-sum) would be high-value** as it closes `OM=ON` through a completely different mechanism. Antipode is the closest to landing this round.

### Ranking (whole field, head-to-head, anchored to last outcomes)

Six pairwise comparisons submitted to `update_ranking`:

1. `analytic-branch-cert` > `analytic-resultant-cert` — both SOLVED APPROVE; branch-cert is the more direct/self-contained saturation proof (doesn't need Galois/inert-prime machinery; resultant-cert leans on saturation for the isosceles stratum). Slight win to the headline.
2. `analytic-branch-cert` > `antipode-rightangle` — SOLVED vs partial (even with sound revision).
3. `analytic-branch-cert` > `power-secant-product` — SOLVED vs partial.
4. `analytic-resultant-cert` > `antipode-rightangle` — resultant is reviewer-APPROVE solved; antipode is partial (one mechanical round from a sound independent close, but not yet built/approved). Resultant wins this round; the gap should narrow next round if antipode lands APPROVE.
5. `analytic-resultant-cert` > `power-secant-product` — SOLVED vs partial.
6. `antipode-rightangle` > `power-secant-product` — antipode's revision is scout-verified sound (I reproduced remainder 0; leading coeffs nonzero); power's 9b is unrun and 9a is the documented numpy-sign-trap. Antipode clearly stronger this round.

Post-ranking Elo: `analytic-branch-cert` 1595, `analytic-resultant-cert` 1515, `antipode-rightangle` 1496, `power-secant-product` 1394. All `stale` flags cleared.

No new approaches to register (antipode and power keep their existing slugs; both analytics stay as-is). No copy requests from the outliner.

build set: antipode-rightangle, power-secant-product
