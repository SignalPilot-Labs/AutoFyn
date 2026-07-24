# proof-builder report — concavity-minimax-duality — round 5

## Status: partial (unchanged)

## Task
Advance §10's 1-Lipschitz/Kantorovich weak-duality certificate lemma toward an actual
lower-bound proof: find g_m such that Σ(-1)^{i+1} g_m(x_i) ≥ e_m for every D/M-reachable
configuration from D_m within budget m.

## What was done (all exact `fractions.Fraction` arithmetic; LP solves via `scipy.linprog`
used only as an exploratory diagnostic, not as a proof step)

1. **Ran the LP feasibility check** specified in §10 Step 3, scoped to the *full* BFS-reachable
   state set from `D_m` (m=1,2,3,4; 4/22/164/1607 states, 4/9/23/61 distinct values) —
   feasible in every case.

2. **Proved the feasibility is circular** — re-solving with "maximize Σg(v)" returns `g=id`
   exactly in every case, because `e_g=e` under `g=id`, and the raw claim `min e ≥ target` on
   the same finite sample is already known true by direct enumeration. This concretely confirms
   (not merely anticipates) the risk the outline-reviewer flagged: "LP feasible on samples"
   carries no evidential weight toward a general-m certificate by itself.

3. **Proved two new general (all-m) forced-value lemmas**, via an explicit, exact
   cascade-reachability construction (`M(2^j,2^{j-1})` applied to `D_j` yields exactly
   `D_{j-1}`, verified exactly for j=1..6): any valid certificate g must satisfy `g(1)=1` and
   `g(2)=2` exactly (zero slack), for every m.

4. **Upgraded two clip-candidate refutations to exact closed-form proofs** (previously only
   numeric stress-test observations): `min(t,1)` fails at every *odd* m via a telescoping-parity
   identity at the base configuration `D_m` itself; `min(t,2)` fails via a second reachable
   witness `(4,2,1/2,1/2)` (verified reachable for every m≥2) forcing `g(4)≥3`, contradicting
   `g(4)=2`.

5. **Located genuine slack** at `g(4)∈[3,4]` (LP-confirmed range, matches the exact lower bound
   from step 4), but minimize-sum LP vertex-hunting there produces only irregular, non-monotone
   sawtooth patterns — no recognizable closed form emerges.

6. **Tested and refuted** a family of two-slope piecewise-linear clip candidates.

## Honest result
No working closed-form `g_m` found this round. The round's real contribution is two new,
fully general, fully proved lemmas (cascade reachability; forced values at 1,2) plus two
sharpened exact refutations (replacing stress-test observations), and a concrete diagnosis of
why this is hard (identity is forced at the bottom of the value range; whatever slack exists
higher up is not obviously structured). The multi-cut lower-bound gap remains open. Status
stays `partial` — no overclaim.

## File updated
`/home/agentuser/repo/results/imo-2026-03/approaches/concavity-minimax-duality.md`
— new §11 (full detail), updated `## Status` (unchanged, `partial`), `## Approaches tried`
(new round-5 entry), `## Full proof` placeholder note, and `## Promotable lemmas` (two new
lemma entries: cascade reachability, forced-value Lemmas A/B).

## Promotable lemmas (candidates for reviewer certification)
- **Cascade reachability lemma** — `D_j → D_{j-1}` via a single `M(2^j,2^{j-1})` operation;
  `D_j` reduces to singleton `{1}` in exactly `j` ops. Proved in full, general-purpose.
- **Forced-value Lemmas A, B** — any valid 1-Lipschitz weak-duality certificate for this
  problem's lower bound must satisfy `g(1)=1`, `g(2)=2` exactly, for every m. Proved in full
  via the cascade lemma + Lipschitz sandwich.

## Memory file updated
`/tmp/memory/proof-builder.md` — added 3 new rules (LP-feasibility circularity trap; upgrading
stress-test failures to exact closed-form proofs), 22 rules total (under the 30 cap, no
trimming needed).
