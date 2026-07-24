# Build report — lp-duality-certificate, round 29

## Task

Per dispatch: sequence the free transplants for the n=4 upper bound
(`unconditional-p2-threshold-closure`, the case-(a) analog via
`generalized-peel-identity` + round-27's complete n=3 upper bound,
`p1-geq-half-closure-n4`), narrow the residual to
p1<T/2 AND T/31<p2<8T/31, instantiate `bisect-subset-lemma` at n=4
(m=5, 30 chambers), and numerically measure coverage before attempting
new hand-derived chambers.

## What was done

1. **Free transplants (R29.1).** All three closed unconditionally by pure
   instantiation of already-general-n lemmas, with the exact threshold
   arithmetic re-derived (not just cited): p2<=T/31, p2>=8T/31 (derived
   from scratch: (a3-a4)T/(2a3-1) = 8T/31, matching a4*T/2), p1>=T/2.
   Residual confirmed exactly: **p1<T/2 AND T/31<p2<8T/31**.

2. **Bisect-Subset-Lemma at n=4 (R29.3).** 30 chambers instantiated by
   substitution. Measured coverage (exact `Fraction`, 20000–30000 random
   trials rejection-sampled into the residual box): **~93% covered**,
   ~7% uncovered — a genuine interior gap, not a boundary sliver.

3. **Beyond the dispatched scope (permitted, time allowed):** searched for
   and found a new chamber shape that closes the uncovered points — bisect
   2 pieces, pin 1 of the remaining 3 to another (matching value), leave
   the last untouched. Proved this in full as the **Double-Bisect-Pin
   Theorem** (general closed form Φ=(T+|p_k-p_l-p_r|)/2, via 3 iterated
   applications of the already-certified `pair-insensitivity-corollary` —
   a genuine proof, not a numeric fit). 30 such chambers exist
   (C(5,2)*C(3,2)=30).

4. **Combined coverage (R29.5).** Bisect-Subset (30) + Double-Bisect-Pin
   (30) = 60 chambers: **100% coverage on 30000 fresh exact-Fraction
   trials**, zero violations. Diagnosed that no small subset of the pin
   family dominates (>=14 distinct chambers each win on some fraction of
   points) — the full family is genuinely needed, not prunable.

## Honest scope / what remains open

This is empirical (strong: 50,000+ exact trials, zero violations) but
**not a proof**. The actual Farkas-style exhaustive covering argument
(showing "all 60 chambers fail" is algebraically infeasible everywhere in
the residual box) has not been derived. This is flagged explicitly as
next round's task, per the project's own repeated lesson (rounds 24-26)
that numeric-only coverage claims have previously hidden real gaps.

Status set to: **partial** (real narrowing + a new proved lemma, but n=4's
upper bound is not fully closed).

## Files changed

- `results/imo-2026-03/approaches/lp-duality-certificate.md` — updated
  Status, Approaches tried, Current best; appended full "Round 29 build"
  section (§R29.0–R29.5) with complete proofs and verification scripts.
- `results/imo-2026-03/lemmas/double-bisect-pin-family-n4.md` — new
  proposed lemma, pending proof-reviewer certification.
- Scripts (not committed, referenced by path in the proof):
  `/tmp/round-29/coverage_n4.py`, `coverage_n4_extra.py`,
  `find_pin_witnesses.py`, `verify_pin_formulas.py`,
  `coverage_named33.py`, `coverage_named33_exact.py`,
  `find_extra_pins.py`, `diagnose_remaining.py`.
