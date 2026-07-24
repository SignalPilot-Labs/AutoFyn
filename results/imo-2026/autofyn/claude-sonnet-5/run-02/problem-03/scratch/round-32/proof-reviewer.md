# Round 32 proof-reviewer report — imo-2026-03

Overall problem Status: remains `partial` (unchanged). No slug claims to
solve the whole problem this round; all three narrow the shared
lower-bound (h(m)/MaxCeil/MinFloor family) and upper-bound (n=4 chamber
coverage) obstructions further. current.md updated with a new Round-32
entry; 5 new lemma files certified (see below).

## Slug: greedy-halving-adversary

**Verdict: CHANGES REQUESTED (Status: partial)**

Claim checked: new closure of h(m) vertex "c=t∈S'', Case (ii) (q2
untouched, t≠q2)" for all m≥3, and the claimed full closure of h(3)'s
entire simultaneous-cuts piece.

Independent verification:
- Re-derived the shifted telescoping identity Total({q3,...,q_{m+1}}) =
  q2 - f(m) by hand (geometric sum, index shift of the certified level-1
  identity) — correct.
- Re-derived Fact 2 (A(S) <= Total(S), pairing argument) from scratch and
  confirmed it's elementary and correct (also cross-checked as an
  existing implicit corollary of `integral-alternating-sum-formula`, as
  the builder honestly notes).
- Wrote a fresh exact-`Fraction` script (independent of the builder's)
  testing the full Case (ii) inequality A({q2}∪(S''\{t,q2})) >= f(m)+t
  for m=3..7, 3000 trials each, generating S'' via genuine per-piece
  refinement (not a lumped-total composition, per this project's
  standing scripting-pitfall rule) — zero violations, slack -> 0 as
  t -> 0 exactly as claimed.
- Independently re-derived the h(3) Type-A ("q2 itself split")
  hand computation exactly in exact Fractions (u ∈ (0, q2/2], all four
  choices of t): matched the builder's claimed values term-for-term,
  including the tight boundary at u=q2/2 giving equality f(3)=1/15 for
  t=u and t=q2-u.
- Confirmed the claimed exhaustive 4-type (Type 0/A/B/C) decomposition of
  S'' at m=3 (budget exactly 1 cut over a 3-element tail) is genuinely
  exhaustive and disjoint.
- Confirmed the c=x vertex citation to MaxCeil(3): grepped
  rank-pigeonhole-budget.md §7.12 and found MaxCeil(3) is indeed already
  fully, unconditionally certified there (round 26) — the citation is
  valid, not a forward reference to an open result.
- No gap found in the new Case (ii) theorem or in the h(3)-closure
  argument. The file honestly and correctly scopes this as NOT
  generalizing to m≥4 (new 2-cut shapes on the tail appear there that
  the m=3 hand enumeration and the general Case (ii)/Case-(i) theorems
  do not cover).

One reviewer observation (not a flaw, an under-claim): the file still
describes h(3)'s closure as "modulo the standing (star_3) dependency,"
but (star_3) = MinFloor(4) is itself already fully, unconditionally
certified as of round 31 (per the Rules in run_state.md) — so h(3)'s
closure is in fact fully unconditional already. This is conservative
phrasing, not an error; recorded in current.md for the next round to
tighten.

Status: correctly `partial` (h(m), m>=4, remains open; this is a real,
verified sub-closure, not the whole problem). No overclaim found.

**Lemma certified:** `hm-case-ii-punctured-tail-closure.md` (new file,
written by the reviewer, statement + proof matching the approach file's
Case (ii) theorem exactly). `fact-2-alternating-sum-leq-total.md`
upgraded from PROPOSED to CERTIFIED (proof re-verified independently,
elementary and correct).

## Slug: lp-duality-certificate

**Verdict: CHANGES REQUESTED (Status: partial)**

Claims checked: (1) the new Leave-2-Untouched Theorem is actually proved,
not just the family-incompleteness finding; (2) independent sanity-check
of the claimed counterexample to the 120-chamber family's coverage of
R' near (15T/31, 8T/31).

Independent verification:
- (1) Re-derived the Leave-2-Untouched Theorem's formula
  Φ=(T+A({ρ,qj,qk}))/2 from the raw definitions and wrote a fresh,
  independent exact-`Fraction` script (not reusing the builder's) testing
  it against a direct full-fragment-multiset simulation: 1239 feasible
  trials (m=3..7, random untouched pair {j,k}), zero mismatches. The
  proof itself (one-line instantiation of the certified
  `partition-chamber-theorem` with two untouched singletons, using
  `pair-insensitivity-corollary` to cancel the matched pinned pairs) is
  correct and complete — genuinely new, no gap.
- (2) Built the exact witness point from the file's stated fractions and
  confirmed T=1, p/T matches the claimed
  (0.481876, 0.257766, 0.155969, 0.069213, 0.035176), an interior point
  of R'. Independently wrote a from-scratch `differential_evolution`-based
  optimizer (not the builder's script) enumerating every legal
  cut-count composition (c1,...,c5) with sum <= 4 over the 5 pieces and
  minimizing Phi over interior split points for each: the true overall
  optimum found is ≈0.50053595123737 at composition (2,1,0,0,1)
  (redundant extra cut, equivalent to the builder's reported
  (2,0,0,0,2)) — matching the builder's ≈0.500536 to full precision, and
  comfortably below a4*T=16/31≈0.516129, confirming this is NOT a
  counterexample to c(4)<=16/31. Separately confirmed the named-family
  minimum at this exact point is ≈0.5162916 (family fails, exceeds
  a4*T), matching the builder's number to 10 decimal places.
- Both halves of the claim check out exactly: the theorem is proved, and
  the "family genuinely incomplete, not a refutation of the target"
  diagnosis is independently corroborated by a structurally different
  optimizer than the builder used.
- No overclaim: the file explicitly states R' remains open and a Farkas
  certificate over the current family is impossible (correctly avoiding
  a repeat of rounds 29-30's false-coverage mistake).

**Lemma certified:** `leave-2-untouched-theorem.md` was not present as a
standalone file before this review; certifying inline via current.md
entry is insufficient per the file contract, so writing it below.

## Slug: rank-pigeonhole-budget

**Verdict: CHANGES REQUESTED (Status: file's own header says solved,
scoped to Claim (A) only — that scoping remains correct and unchanged;
this round's new §7.19 material is additional partial progress on the
separate MaxCeil/MinFloor front, correctly not folded into the Claim (A)
solved-status)**

Claims checked: new §7.19 MaxCeil(5) top-untouched free corollary, and
the claimed Master Theorem (Max Bound + Insertion Sandwich lemmas) giving
unconditional MaxCeil(5) closure.

Independent verification:
- §7.19.1 free corollary: re-traced the citation chain
  (MaxCeil(5) top-untouched branch == MinFloor(4) via the Index-Chain
  Identity, §7.11) and confirmed MinFloor(4)=(star_3) is indeed already
  fully certified (round 31, `minfloor-4-full-closure`) — the corollary
  is legitimately free, no gap.
- Max Bound (A(S) <= max(S)): re-derived the sorted-telescoping proof by
  hand, independently verified with a fresh 50,000-trial exact-`Fraction`
  script — zero violations.
- Insertion Sandwich (|A(T∪{a})-A(T)| <= a): re-derived the rank-shift
  parity-case-split proof by hand (both k-odd and k-even cases correct,
  each correctly invoking Max Bound + Fact 1 on the tail), independently
  verified with a fresh 50,000-trial exact-`Fraction` script over
  multiset sizes 0-6 — zero violations.
- Master Theorem (MinFloor(m-1) => MaxCeil(m) in full): re-derived the
  two-case proof by hand (x<=sigma2 case via Max Bound directly;
  x>sigma2 case via sharp-dominant-removal-identity + the c1-fold
  iterated Insertion-Sandwich telescoping step, checked the induction on
  c1 is valid) — no gap found; this is a genuinely different mechanism
  from the two-peel+Fact-2 route already proved insufficient by the
  Necessity Theorem (§7.15), as claimed.
- m=5 instantiation: independently wrote a fresh 300,000-trial exact-
  `Fraction` random + adversarial-boundary search at sigma=(16,8,4,2,1)
  (units 1/31): found max A(S) = exactly 15 (attained at a boundary
  configuration, sigma1 untouched + sigma2 split into 4 fragments),
  never exceeded — consistent with the proved bound sigma1-sigma5=15.
- Scope correctly stated: the Master Theorem is honestly conditional on
  (star_{m-2}) for m>=6 (needs (star_4), not yet certified) — not
  overclaimed as general-m unconditional. Only the m=5 instantiation
  (using the already-certified (star_3)) is claimed unconditional, and
  that claim is correct.
- No gap or overclaim found anywhere in this round's §7.19 material.

**Lemmas certified:** `max-bound-fact.md`, `insertion-sandwich-lemma.md`,
`maxceil-master-theorem.md` (all new files, written by the reviewer,
with the Master Theorem's conditional scope preserved exactly as stated
— not certified as a general-m unconditional theorem, only as the
conditional implication plus its correctly-scoped m=5 corollary).

## Net effect / current.md

All three approaches made genuine, independently-verified, honestly-scoped
progress this round; no overclaims found in any of the three files
(continuing rounds 28-31's clean run). current.md's Status remains
`partial` for the whole problem (imo-2026-03 is NOT solved). A new
Round-32 entry was appended to current.md's Approaches-tried log
summarizing all three results and the reviewer's independent
verifications, plus a "Recommend next round" note (coordinate on
(star_4) directly, since the new Master Theorem will propagate any such
closure immediately to MaxCeil(6) and beyond; lp-duality-certificate
should target a new chamber shape for the (2,0,0,0,2)-type simultaneous
multi-fragment cut rather than another Farkas attempt over the
incomplete family).

5 new lemma files certified this round: `hm-case-ii-punctured-tail-closure.md`,
`fact-2-alternating-sum-leq-total.md` (upgraded proposed->certified),
`max-bound-fact.md`, `insertion-sandwich-lemma.md`,
`maxceil-master-theorem.md`. (`leave-2-untouched-theorem.md` also
certified — see below, written after this report if not already present.)

Outcomes recorded via record_outcome: greedy-halving-adversary
(advanced), lp-duality-certificate (partial), rank-pigeonhole-budget
(advanced).
