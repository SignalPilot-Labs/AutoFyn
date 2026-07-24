## imo-2026-06

### Summary of this round's field

All three explorers this round independently converged on the same diagnosis: no
genuinely new TOP-LEVEL framing escapes the "existential-to-universal promotion"
wall (Lemma I) that has killed 9 mechanisms across 9 rounds, but two explorers
(analytic, crux-mining) both independently flagged crux `aimo-0680`'s
"window-counting → AP-identity divisibility-difference-vanishing" template as the
closest structural match to the exact missing step — with the caveat, confirmed by
all three explorers independently, that aimo-0680's literal mechanism needs a global
algebraic identity (`n | f^n(m)-m`) that our greedy, existential/minimality-defined
recursion structurally lacks. The crux-mining explorer additionally checked
aimo-0477, aimo-0678, and aimo-0611 and found the same disanalogy each time (all
lean on an explicit closed-form recurrence to induct/recur through). The analytic
explorer ran two new numeric cheap-kills: (1) raw `g_n` monotonicity (opening #4,
aimo-0477-style) is FALSE on a_1=4807's data (`17,17,17,17,221,17,...` — not
monotone) — do not pursue a bare monotone-potential transplant; (2) Return-Time
Boundedness of the rogue-pair type's occurrence gaps is numerically SUPPORTED
(≈555, occasionally doubling, on a_1=4807 to N=7775) but the explorer itself flagged
a circularity risk.

Per the dispatch and CLAUDE.md's plateau-breaking rule, I did NOT propose another
repair within the same gcd-pigeonhole/qualitative-branch family. Instead:

### 1. `covering-system-construction` — REVISE (leader, Elo ~1832)
Appended new **Step 11: Growth-Forced Divisibility** — the mandated aimo-0680-style
import, adapted concretely: since aimo-0680's exact algebraic identity is
unavailable, I substitute the certified Bounded/Generalized Bounded Gap Lemma's
LINEAR MAGNITUDE ceiling (a_{n+1} ≤ a_n + c) as the source of an "AP-identity-style"
squeeze, combined with the certified Confined-GCD Lemma's finite alphabet `Div(b)`
(imported verbatim from `cofinite-window-capacity-bound`, now folded into the leader
approach rather than left in a satellite file). The new, honestly-unproved
"Escape-Cost Lemma" (Step 11.2/11.3) is the concrete open target: does repeating the
same bad divisor-class force a growing index gap via the greedy rule's own
minimality? Step 11.2c gives the builder a concrete, cheap NUMERIC premise-check to
run before investing in a general proof (track repeat-rate of the same bad class,
not just raw q*-divisibility, on a1=4807/11305 and any fresh |F'|,|F''|≥2 seed with
`D_bad≠∅` — note a1=11305 already has `D_bad=∅`, vacuously done, per
`cofinite-window-capacity-bound`'s own finding, so a NEW seed with genuinely nonempty
`D_bad` is needed to make this a real test). Section 11.5 explicitly documents why I
rejected opening a standalone Return-Time Boundedness approach (see below).

### 2. `greedy-exchange-cost-potential` — REVISE (Elo ~1762)
Appended new **ROUND 10 section: quantitative Escape-Budget attack on the Successor
Claim** (imports the certified Successor-Transport Reduction Lemma verbatim).
Distinct mechanism from approach 1: instead of a two-far-index AP-style squeeze, this
uses a LOCAL, one-step "growth outpaces escape budget" argument in the flavor of
crux `aimo-0611` (flagged by the fresh-framing explorer) — a `D_bad`-class occurrence
must force every `q*`-multiple in its Bounded-Gap-Lemma window to be illegal, tying
failures to specific EARLIER terms' factorization (negative/illegality data, in the
spirit of the round-7 Lemma K but now anchored to the Confined-GCD Lemma's CONTROLLED
finite alphabet rather than an uncontrolled competitor — this is the concrete repair
of Lemma K's exact defect that the dispatch asked me to look for). Honestly flagged:
the central Escape-Budget Lemma is unproved, and a circularity risk (illegality
unpacking into full S₀-sufficiency, which is (†) itself) is explicitly called out for
the builder to check before trusting any progress.

### 3. `confined-competitor-construction` — NEW
A third, genuinely different mechanism: rather than arguing ABOUT the window
abstractly (approach 2) or a magnitude squeeze across far indices (approach 1), this
approach explicitly CONSTRUCTS a concrete smaller candidate integer `c` (the smallest
`q*`-multiple exceeding the immediately preceding term) and attempts to prove it
legal, contradicting the greedy minimality of the actual failing witness — the
constructive twin of round 7's dead Blocking-Data Bridging mechanism (Lemma K),
repaired using this round's certified Confined-GCD Lemma to control `c`'s
`q*`-divisibility explicitly (unavailable in round 7). The central open gap
(Controlled-Competitor Legality: is `c` legal against ALL earlier terms, not just
`a_{n_B}`?) is stated honestly as the load-bearing unknown, with an explicit note
that if it fails for the same "uncontrolled factorization against arbitrary earlier
i" reason as Lemma K, the builder must say so and RETHINK cleanly rather than
force a rescue.

### Considered and explicitly rejected: standalone Return-Time Boundedness Lemma
Per the dispatch's instruction to investigate the circularity risk carefully before
proposing it as a target: I checked whether a general Return-Time Boundedness Lemma
(uniform bound on ALL consecutive-occurrence gaps of a fixed extended-persistent type
`A'`, independent of q*-divisibility) can be proved without assuming what's being
proved. Conclusion: it cannot be safely opened as a standalone target. The only
certified fact about occurrence frequency, Persistent-Type Pigeonhole
(`lemmas/persistent-type-pigeonhole.md`), gives ONLY infinitude — no density or gap
bound of any kind (verified by re-reading its proof: pure pigeonhole over a finite
type-alphabet, no density argument). The natural route to a gap bound (a CRT/density
argument on residues mod the current core S₀) would need "eventually, legality is
governed purely by residue mod S₀" — and `reversible-transition-map` (round 5)
already proved this is LOGICALLY EQUIVALENT to gap (†) itself. So this target either
smuggles in (†) or degenerates to restating it; I did not open it as a separate
approach. Both revised approaches above (1 and 2) instead use ONLY the certified
Bounded Gap Lemma's magnitude bound, deliberately avoiding this circularity, and I
recorded this reasoning explicitly in `covering-system-construction.md` Step 11.5 so
no future round re-proposes the naive version without the same check.

### Field composition and rationale
- Kept the population at 3 live, mutually-diverse mechanisms all targeting the same
  precisely-localized crux (Joint Cofinite FAH / the Successor Claim) via genuinely
  different proof shapes: (1) a two-far-index AP-style magnitude squeeze, (2) a
  local one-step escape-budget/illegality argument, (3) an explicit constructive
  competitor. This satisfies CLAUDE.md's diversity mandate (different mechanisms,
  not technique variants of one idea) while all three honestly reduce to the same
  underlying open sub-lemma pattern (something must link consecutive/repeated
  divisor-class data, which no certified tool currently supplies) — this is
  expected and was the explorers' own diagnosis, not a design flaw.
  `cofinite-window-capacity-bound` (the round-9 satellite that produced Confined-GCD
  and Cofinite Sufficiency) is intentionally left stale this round — its content is
  now fully imported into approach 1's Step 11, so rebuilding it separately would
  waste a builder slot on the identical target (per the round-2 "don't revise
  duplicate-gap approaches" rule).
- `seed-coupling-induction` and `scalar-well-ordering-lock-in` remain confirmed dead
  (RETHINK), correctly left out.
- `amortized-charging-budget`, `density-sieve-contradiction`, `hypergraph-transversal`,
  `recruitment-round-charging`, `witness-depth-bound`, `witness-index-descent`,
  `reversible-transition-map` all remain stale/superseded/dead per prior rounds;
  correctly left out.

### Recommended build set
`covering-system-construction`, `greedy-exchange-cost-potential`,
`confined-competitor-construction` — all three carry genuinely new, concretely
scoped (not hand-wavy) mechanisms with explicit cheap-kill numeric checks the
builder should run before investing in the general proof, per this round's dispatch
and the "cheap kill first" heuristic. Each is honestly flagged as speculative; if
all three stall at the same underlying "no certified tool links repeated/consecutive
divisor-class data" pattern, that itself will be valuable new information sharpening
exactly what a 4th-generation mechanism would need to supply (a genuine consecutive-
occurrence identity or inequality — see the crux-mining explorer's aimo-0477
target-shape analysis for the sharpest statement of what's missing).
