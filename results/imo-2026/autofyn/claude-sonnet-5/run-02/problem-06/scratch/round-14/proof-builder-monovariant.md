## Summary — integer-monovariant-difference-identity build (round 14)

File written: `/home/agentuser/repo/results/imo-2026-06/approaches/integer-monovariant-difference-identity.md`
Status: **unsolved** (RETHINK)

Independently re-derived crux `aimo-0134`'s mechanism from the raw corpus
(`past_crux_moves_database.json`), confirming the outline's summary is
accurate. Confirmed the literal transplant (average the unbounded terms
`a_n`) fails outright since `a_n -> infinity`. Searched 5 candidate integer
statistics of the gap sequence / auxiliary quantities:

1. Running average of gaps `b_n = (a_{n+1}-a_1)/n` — fails: not forced
   integer, and computationally REFUTED as monotone on both mandated rogue
   seeds (a_1=4807: increases on 1196/2498 steps; a_1=11305: 998/2498) —
   confirms the outline's structural suspicion with hard numbers.
2. Running minimum of gaps `M_n` — genuinely monotone + bounded, but proved
   structurally uninformative (no difference identity recovers
   identity-level/prime information from a running min).
3. Overall gcd of all terms `D_n = gcd(a_1,...,a_n)` — genuinely monotone +
   bounded, but computationally collapses to 1 by the 3rd term on both seeds
   (immediate, uninformative stabilization).
4. Persistent-type count — confirmed (as outline pre-flagged) to restate the
   already-certified Persistent-Type Pigeonhole verbatim, no new leverage.
5. Recruited-core size — confirmed (as outline pre-flagged) circular: its
   boundedness IS gap (†) itself.

Proved a general diagnosis (§3): every candidate satisfies at most 2 of the
4 properties aimo-0134's technique needs (integer-by-rule, forcing per-step
inequality, crux-independent boundedness, identity-recovering difference
identity) because the recurrence's own legality test is already certified
class-blind (references only THAT a shared prime exists, never WHICH) —
this poisons any purely numeric (count/min/gcd/average) statistic built from
it, generalizing past the 5 specific candidates tried.

Conclusion: recorded as the 16th confirmed-dead FAH/(†) mechanism, a genuine
informative negative result, no counterexample sought/found, no
overclaiming. No new lemma certified as portable machinery (diagnostic
content only, matching prior round precedent). Memory file
`/tmp/memory/proof-builder.md` updated with a new screening-checklist rule
for future integer-monovariant transplant attempts (dropped one superseded
rule to stay at the 30-rule cap).
