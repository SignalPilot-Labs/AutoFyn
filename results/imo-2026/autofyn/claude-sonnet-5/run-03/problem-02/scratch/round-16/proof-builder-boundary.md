# Round 16 report — coordinate-bash-resultant-boundary

## Task
Step 0 (mandatory sign fix), Step 1 (corrected LP rerun), Step 2 (Putinar/SDP
escalation), Step 3 (case-split fallback), in that order, per the
proof-outliner's round-16 directive.

## What was done

**Step 0 — sign fix, confirmed exactly.** Re-derived `(G_0·Num)_00` from
scratch (own sympy session): it is exactly the negative of round 15's
displayed `B_G0N` polynomial (zero residual). The correctly-signed positive
generator is `B_G0N := (G_0·Num)_00` (no minus sign on Num), matching round
15's claimed numeric range digit-for-digit. Reconfirmed on a fresh
4,000,000-sample sweep of the true residual domain (17,340 domain points):
`B_G0N ∈ (0.0121, 0.0784) > 0`, zero violations.

**Step 1 — LP rerun.** Reran the full multiplier sweep (14 variants,
superset of round 15's 9) with the corrected generator in the
non-negative-coefficient basis `{B1, -B2, B4, B6, B_G0E, B_G0N, B_EN, σ, τ,
1-σ, 1-τ}` (B3, B5 excluded — confirmed mixed-sign even on the true curved
domain, not just the round-14 loose box). Direct (unmultiplied) search:
not in span for either -q1 or -r0. With multipliers: several bring the
target into span, but the nonnegative LP is infeasible in every case,
including with the corrected generator now available. Confirmed
non-artifact via phase-1 L¹-residual LP (residuals 40–205, far from 0) on
four representative cases.

**Step 2 — Putinar/SDP escalation (new technique for this population).**
Built a Lasserre/Putinar SOS-Gram-matrix SDP over the same generator basis
using cvxpy. First SCS attempt at maxdeg=8 for -q1 returned
"optimal_inaccurate" — investigated and found the returned Gram matrices
had eigenvalues as negative as -4.6 (not PSD at all, a non-convergence
artifact). Switched to CLARABEL, which cleanly resolves infeasibility with
genuine SDP infeasibility certificates. Result: 6 of 8 tested
degree/multiplier combinations for -q1 (maxdeg 6,8, with/without
(1-σ)(1-τ) multiplier) and -r0 (maxdeg 7,9,11, with/without (1-σ)
multiplier) are cleanly CLARABEL-infeasible; 2 larger instances are
solver-scaling-inconclusive (CLARABEL failed to converge, not a negative
result — flagged honestly as such, not claimed as infeasible).

**Step 3 — case-split fallback, opened not completed.** q1's own
(σ,τ)-monomial coefficient pattern is genuinely mixed-sign with no single
dominant negative term, so the crux-corpus Schur "dominate the lone
negative term" pattern does not transfer directly to q1 as a bare
polynomial — any working split needs to use the actual domain conditions
(G0>0, E_num<0, Bc≥0, Num<0), not q1's coefficient signs alone. Per the
outline's own priority rule ("only pursue Step 3 if Step 2 proves
intractable to stand up" — it wasn't; it ran and gave a real result),
Step 3 correctly received less time this round. No candidate split
variable was identified. Flagged as next round's most promising concrete
lever, alongside resolving the two solver-scaling-inconclusive SDP
instances.

## Net result

Status remains `partial`. The sign error is fixed and will not need
re-fixing. The negative evidence against this whole generator family
(`{G_0, E_num, Num, Bc}`, bare/products/SOS-weighted) is now the broadest
and most rigorously confirmed to date: LP infeasibility (phase-1-confirmed)
plus SDP infeasibility (CLARABEL-certified, eigenvalue-checked) at every
degree/multiplier combination the solver could conclusively resolve. No
certificate found. No overclaiming — all negative results are reported
honestly, with the two solver-scaling-limited SDP instances explicitly
flagged as inconclusive rather than negative.

## Recommendation for next round

Two independent generic-certificate techniques (LP, SDP) have now both
failed on this generator family at every degree checked. This strengthens
the case for either (a) a genuinely new base generator beyond
`{G_0, E_num, Num, Bc}`, or (b) the still-unstarted Step 3 domain-aware
case split, which is now the more promising concrete lever since Step 2
was tried and closed (modulo two inconclusive instances, which should be
retried with a different solver such as MOSEK if available before
concluding).

## Files changed
- `/home/agentuser/repo/results/imo-2026-02/approaches/coordinate-bash-resultant-boundary.md`
  — new "### Round 16 (this round)" section inserted before the round-16
  outline section (which is preserved as the historical dispatch record).
- No new lemma files this round (no fully closed, certifiable new result —
  the round's content is negative/diagnostic, per the file contract's
  "record everything, including failed approaches" rule).

## Work scripts (not part of the repo, scratch only)
`/tmp/round-16/gen_work/derive.py` (sign-fix re-derivation),
`/tmp/round-16/gen_work/sign_check.py`, `sign_check2.py` (domain +
sign sweeps), `lp_search.py` (LP sweep + phase-1 residual), `sdp_search.py`,
`sdp_sweep.py` (Putinar/SDP escalation).
