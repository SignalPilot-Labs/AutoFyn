# Round 18 proof-reviewer report — imo-2026-06

Four slugs built this round. Reviewed independently, adversarially, each
against its own claimed target. All independent re-derivations and
re-simulations described below were performed fresh in this review (scripts
in `/tmp/round-18/`), not merely re-read from the builder's report.

## 1. `prime-power-seed-periodicity-theorem` — **APPROVE**

**Claim.** For every `a_1 = p^k` (`p` prime, `k ≥ 1`), `a_n = a_1+p(n-1)`
for every `n ≥ 1`; `T=1, L=p` witness the problem's conclusion literally
from `n=1`.

**Independent re-derivation of the proof.** Strong induction on `n`.
Inductive step, given `p | a_i` for all `i ≤ n` (from the IH):
- For `1 ≤ j ≤ p-1`: `a_n+j ≡ j ≢ 0 (mod p)`, so `p ∤ (a_n+j)`. Since
  `P(a_1) = {p}` is a singleton (as `a_1 = p^k`), any common factor of
  `a_n+j` and `a_1` must be a power of `p`; since `p` itself doesn't divide
  `a_n+j`, that common factor is `1`. So the candidate fails the `i=1`
  legality test — illegal.
- `a_n+p`: divisible by `p` (since `a_n` is), hence shares `p` with every
  `a_i`, `i ≤ n` (all divisible by `p` by IH) — legal against everything.
- Minimality of `a_{n+1}` (defined as the min of the legal set, all elements
  of which exceed `a_n`) then forces `a_{n+1}=a_n+p` exactly.

I re-derived this completely independently before reading the file's own
proof line-by-line; it matches exactly, with no gap, no hidden case, and no
"clearly/obviously" language covering real content. The `p=2` overlap with
the already-certified `even-seed-literal-periodicity-theorem.md` is
correctly acknowledged (cited, not re-derived), and the scope boundary
(`|Q|=1` only, argument breaks for `|Q| ≥ 2` because the "fails against `a_1`
entirely" step needs `P(a_1)` to be a singleton) is correctly and honestly
stated, with an explicit forward-reference to the sibling file's genuine
counterexample for `|Q|≥2` (see item 3 below).

**Independent computational verification.** Fresh Python script
(`/tmp/round-18/verify_primepower.py`), brute-force trial-division greedy
generator (no shortcuts, no reuse of the builder's code). Tested 43 seeds:
the builder's 24 plus 19 more I chose independently to specifically probe
primes NOT in the builder's set (`p=29,31,37,41`) and larger exponents
(`k` up to `10`, e.g. `a_1=1024=2^10`, `a_1=2187=3^7`). All 43 match the
closed form exactly on the first 15 terms, zero discrepancies (see full
output above in my working log). `T` and `L` are stated explicitly (`T=1,
L=p`) and verified by substitution, per the rigor rules.

**Verdict.** Complete, gap-free, unconditional proof of the stated
restricted-scope target. **Status: solved** (for the `a_1=p^k` subfamily
only; the workspace-level Status for the general problem stays `partial`).
**APPROVE.** Certified a new lemma:
`lemmas/prime-power-seed-literal-periodicity-theorem.md` (see below).

## 2. `self-absorbing-by-construction` — **CHANGES REQUESTED**

**Claim (this round, record-correction).** The round-17-flagged unresolved
`a_1=255255` candidate exception (type `{5,7,11,13,17}`, first occurrence
`n=27184`, no second occurrence confirmed through window 65000) is resolved:
extending the simulation to `n=500000` shows the type recurs at `n=135914`.

**Independent verification.** I wrote a THIRD, completely independent
simulation script (`/tmp/round-18/sim_255255_full.py`), using a different
algorithmic approach from both the builder's and the round-18
outline-reviewer's implementations: a sieve of smallest-prime-factors up to
30,000,000 combined with a per-prime bitmask coverage test (candidate `c` is
legal iff the union of the bitmasks of indices divisible by each prime of
`c` covers every earlier index — an `O(1)`-per-candidate big-integer
bitwise-OR test, not `O(n)` trial gcd checks). This ran to `n=500000` in
under 22 seconds and reproduced EXACTLY:
- `{5,7,11,13,17}` occurrences: `27184, 135914, 190280, 299010, 353376,
  462106` (matches the claimed `n=135914` second occurrence exactly, plus 4
  further occurrences not mentioned in the file, consistent with it).
- Full-`Q` type occurrences: `81549, 163097, 244645, 326193, 407741, 489289`
  (constant gap `81548`, exactly as claimed).
- `63` distinct observed types by `n=500000`, minimum occurrence count `6`
  across all of them — exactly matching the file's summary.

This is a genuine, independently-reproduced computational fact (three
mutually independent implementations now agree exactly), not a re-trust of
a single number. The round-17 "one genuinely unresolved candidate" is
correctly retired.

**What is NOT established (correctly, honestly, not overclaimed).** NTBT
(`N(Q) ≤ 1` for every `a_1`) remains an open conjecture — the file
correctly states "zero open counterexamples" is evidence, not proof, and no
new proof route was attempted. The Vacuous/Weak Self-Absorption Lemma was
already certified in round 17; no new certifiable content this round beyond
the numeric correction itself. The §6 "counting/pigeonhole corridor
exhausted" negative finding (items (a)/(b)/(c)) is independently re-derived
here and confirmed correct: (a) is literally the same statement as
`N(S_k)`-boundedness in different notation (matches round-17's RETHINK on
`type-alphabet-counting-bound` for the identical reason); (b) is circular
(assumes `S_∞` finite, which is H2's own conclusion); (c) targets a
genuinely weaker statement that would not discharge the Master Conditional
Theorem's actual hypothesis (a fixed terminal `S*`, not merely a bounded
type-count under an ever-growing core) — all three diagnoses hold up under
independent scrutiny.

**Verdict.** Genuine, independently triple-verified record correction; no
overclaim; NTBT honestly still open. **Status: partial. CHANGES REQUESTED**
(no gap to close in the correction itself — the remaining work is a general
proof of NTBT, or abandoning the NTBT route for H2).

## 3. `n1-periodicity-reconciliation` — **CHANGES REQUESTED**

**Claim 1 (Odd-Prime Non-Trivialization Proposition).** The `2|a_1`
trivialization of H1 (every prime of `Q` divides every term when `2|a_1`)
does NOT generalize to odd primes: on `a_1=15,45` (`Q={3,5}`), `3` does NOT
divide every term.

**Independent verification.** Fresh simulation (`/tmp/round-18/verify_15.py`):
generated the first 24 terms of `a_1=15` from scratch, confirmed the exact
sequence `15,18,20,24,30,36,...,102` and the exact period-4 base-type
pattern `{3,5},{3},{5},{3},{3,5},...` starting at `n=1`. Extended to 3000
terms: `3|a_n` for exactly 2250/3000 (75%), `5|a_n` for exactly 1500/3000
(50%), and the "`3` fails" indices form the exact arithmetic progression
`3,7,11,15,...` with constant difference `4` (confirmed by computing the
actual difference set, which is exactly `{4}`, not merely "looks like 4 on
the first few terms"). This is a genuine, structurally-explained
counterexample (the file's structural explanation — the `p-2 ≥ 1`
intermediate-candidate slot available to odd `p` but not to `p=2` — is
independently confirmed sound and matches the mechanism seen in the
computation) to any naive "any `p|a_1` trivializes H1" generalization. Not
an artifact, not overclaimed (the file correctly scopes this as a negative
finding about a specific shortcut, not a statement about H1 in general).

**Claim 2 (`|Q|=2` Non-Tractability finding).** `|Q|=2` is not an easier
"warm-up" subfamily for H1 — the four canonical standing hard test seeds
(187, 209, 221, 247) already live inside it.

I did not independently rerun the full 36-seed sweep (time-budget
trade-off), but this claim is consistent with, and directly corroborated
by, ten-plus prior rounds' documented independent use of exactly these four
seeds as the workspace's hardest test cases (rounds 6, 8, 9, 11, 14, etc.,
all cited correctly in the file) — an internally consistent finding, not a
new unverified assertion pulled from nowhere. Accepted as correctly
characterized: negative/diagnostic, not a positive proof step.

**Verdict.** Both findings are genuine, correctly scoped as diagnostic/
negative (matching the established Lemma-F/Lemma-I "do not certify as
portable machinery" precedent), and neither touches H1/H2 or the Master
Conditional Theorem (re-audited, still gap-free). **Status: partial.
CHANGES REQUESTED** (real permanent narrowing of what NOT to re-attempt;
no progress on H1/H2 themselves, correctly not claimed).

## 4. `triangle-consistency-pigeonhole` — **CHANGES REQUESTED**

**Claim A (§2, Same-Type Triangle Vacuity).** The outline's proposed
triangle mechanism (deriving `gcd(d_1,d_2)>1` from `e:=gcd(a_{m_A},a_{m_A'})`
for two same-type witnesses `m_A,m_A'`) cannot work: `e`'s "> 1" conclusion
is already fully explained by the shared type `A`'s own in-core primes, so
Free Facts on this pair gives zero outside-core information.

I independently re-derived this: since `ρ(m_A)=ρ(m_A')=A` and `A` is
nonempty, `A ⊆ P(a_{m_A}) ∩ P(a_{m_A'})` forces `e>1` for a trivial reason
unrelated to any outside-core content; no certified lemma (Confined-GCD
requires a *disjoint*-type partner to rule out in-core primes, which is
unavailable for a same-type pair) links the outside-core factors of two
same-type witnesses. This is a correct, sound negative finding about the
specific derivation route the outline proposed — appropriately scoped as
killing that route, not as a claim that no future use of `e` could ever
work.

**Claim B (§1, Double-Witness Nested Pigeonhole Lemma).** Correct — I
independently re-derived it: two sequential finite-pigeonhole passes on the
finite divisor set `Div(a_{m_A})` (resp. `Div(a_{m_A'})`) against a shrinking
infinite subset of `X_B`, each pass confined via a direct application of the
already-certified Confined-GCD Lemma (the lemma's own proof only needs
`n≠n_B` plus rogue-pair disjointness, not the `n>n_B` ordering in its
statement, so applying it with the roles/ordering exchanged, as this proof
does, is legitimate reuse, not a stretch).

**Claim C (§3, Two-Sided Singleton Witness Theorem).** If a rogue pair
`(A,B)` has some occurrence of each side whose out-of-core prime set is the
SAME singleton `{q}`, Cofinite FAH holds for the pair with witness `q`.

Correct and essentially a direct two-fold citation of the already-certified
Singleton-Side FAH Lemma (whose own stated setup already permits arbitrary,
not-necessarily-canonical witnesses — this is not new machinery, but a
correctly-noted-as-such combination). **Independently verified
computationally on both of the workspace's two known hard rogue-pair seeds**
using fresh from-scratch scripts:
- `a_1=4807`, `S_0={2,3,5,11,19,23}`: reproduced exactly 13 `A'={3,5,19}`
  occurrences, 180 `B'={2,11}` occurrences, `a_6` outcore `{17}`, singleton
  `B'` witness at `x_1=72` with outcore signature exactly `{17}` (count 20
  matching among the sampled occurrences), and zero exceptions for `q=17`
  on both sides beyond the stated thresholds — exact match.
- `a_1=11305`, `S_0={2,3,5,7,13,17,19,23,29,37,43,101}`: reproduced 247
  `A'={2,5}` occurrences, singleton `A'` witness at `x_2=103` with outcore
  signature exactly `{11}` (count 23, matching), zero exceptions for `q=11`
  on both sides. (Minor, immaterial discrepancy: I counted 80 `B'`
  occurrences vs. the file's 79 — does not affect the zero-exception claim
  or the theorem's correctness.)

**Claim D (§4, residual gap).** The Theorem's own hypothesis (existence of
matching singleton witnesses) is honestly left unproved. I examined whether
this is (i) a disguised restatement of FAH, or (ii) genuinely tractable/
easier. Neither is established by the file, and my own attempt to settle it
also failed to find a reduction either way: the hypothesis does not follow
from FAH (FAH only needs `q` to divide, not to be the *sole* outside-core
prime), and there is no argument — here or elsewhere in the workspace — that
such a matching pair of singletons must exist for a general rogue pair
(indeed, it is structurally plausible that some rogue pairs never have a
singleton-outcore occurrence on either side, in which case this mechanism,
even if fully leveraged, would not suffice). The file's own characterization
("genuinely new, narrower, not proved tractable, not a restatement") is
accurate and not an overclaim in either direction.

**Verdict.** Genuine progress: one more FAH mechanism variant conclusively
killed (19th+), one new, correctly-scoped, computationally-verified
sufficient theorem discovered, with an honestly open and appropriately
sharpened residual question. Does not close H1. **Status: partial. CHANGES
REQUESTED.**

## Lemma certification this round

**Certified:** `lemmas/prime-power-seed-literal-periodicity-theorem.md`
(from `prime-power-seed-periodicity-theorem`) — see full certification text
in that file; independently re-derived and re-simulated as described in
item 1 above.

**Not certified as standalone lemma files (correctly, per established
precedent):**
- The Double-Witness Nested Pigeonhole Lemma and Two-Sided Singleton Witness
  Theorem from `triangle-consistency-pigeonhole` — both correct and
  reusable, but left recorded in the approach file itself rather than
  promoted to `lemmas/` this round; a future round that wants to build on
  them directly is free to request formal certification then.
- The Odd-Prime Non-Trivialization Proposition and `|Q|=2` Non-Tractability
  finding from `n1-periodicity-reconciliation` — diagnostic/negative
  findings, matching the Lemma-F/Lemma-I precedent (do not certify negative
  results asserting absence of a shortcut as portable "machinery").
- No new lemma from `self-absorbing-by-construction` this round (the
  Vacuous/Weak Self-Absorption Lemma was already certified in round 17; this
  round's contribution is a numeric record correction, not new provable
  content).

## Summary of verdicts

| Slug | Verdict | Status |
|---|---|---|
| `prime-power-seed-periodicity-theorem` | **APPROVE** | solved (restricted subfamily `a_1=p^k`) |
| `self-absorbing-by-construction` | **CHANGES REQUESTED** | partial |
| `n1-periodicity-reconciliation` | **CHANGES REQUESTED** | partial |
| `triangle-consistency-pigeonhole` | **CHANGES REQUESTED** | partial |

Overall workspace Status: **partial**. The general problem (`a_1>1`
arbitrary) is not solved. It is now solved unconditionally for two disjoint
infinite subfamilies (`2|a_1`; `a_1=p^k`, overlapping exactly at `a_1=2^k`)
and reduced, for every other `a_1`, to exactly two open hypotheses H1 (FAH —
19+ confirmed-dead mechanisms, now with a new correctly-scoped-but-unproved
sufficient condition) and H2 (absorption-chain termination — evidenced
numerically, "counting/pigeonhole" corridor now confirmed exhausted).
`results/imo-2026-06/current.md` updated accordingly (Status header, new
lemma reference in Current best, Approaches-tried entries).
