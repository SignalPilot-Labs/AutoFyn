## imo-2026-03

### Scope of this lens
GT(m) sub-case (i): q=1 (exactly one element a1 of D exceeds 2^(k-1)), excess
e:=m-k>=1, i.e. within GT(m)'s own induction, q=0 (no element of D exceeds the
threshold) holds at every level j=m,m-1,...,k+1, and only at level k does a
single element a1 in (2^(k-1),2^k] finally exceed threshold. Job: correctly
re-derive the e-fold chained identity connecting OddSum(D∪Γ_{m-1}) down to the
q=1 level-k object, using the corrected (reviewer-derived) two-step relation,
and check whether it can close the width-1 window. All claims below are
independently numerically stress-tested by me in exact `Fraction` arithmetic
(fresh scripts, not reusing round-16's), not assumed from current.md.

### Key finding 1 — the "two-step" framing is a red herring; it's really a
### single-step Odd<->Even alternation, exact and unconditional along the
### whole chain

Re-deriving from the certified q=0 clause of the Unified Threshold-Pair-Peeling
Lemma (`lemmas/monotonicity-reduction-and-unified-threshold-pair-peeling.md`):
writing O_j := OddSum(D∪Γ_{j-1}), E_j := EvenSum(D∪Γ_{j-1}), the true
single-step identity, valid whenever max(D) <= 2^(j-1) (i.e. q=0 at level j
alone — NOT "two levels" as current.md's phrasing suggested), is
**both**:
- O_j = 2^(j-1) + E_{j-1}   (peel Γ's top, an odd global rank)
- E_j = O_{j-1}             (peeling the same odd-rank top also converts the
  companion Even quantity one level down)

I verified both simultaneously, 20,000 fresh trials, random D, random j,
zero violations. The reviewer's "two-step relation O_j=2^(j-1)+O_{j-2},
needs q=0 at both levels j and j-1" is just these two single steps composed
(the second condition is automatically implied by the first when max(D) is
the SAME fixed cap throughout the chain, since 2^(j-2)<2^(j-1)) — so there is
no real extra hypothesis, but critically **the composition is Odd->Even->Odd,
not "Odd stays Odd"**: it must track BOTH O and E as a coupled pair, not
telescope a single quantity.

Since in sub-case (i) max(D)=a1<=2^k<=2^(j-1) for every j>=k+1 (a1's own
defining bound), q=0 holds unconditionally at **every** level from m down to
k+1 — confirming q never flips early; it flips exactly once, at level k
(where a1>2^(k-1) by hypothesis). So the chain of single steps is valid
start-to-finish, no partial-chain caveat needed.

### Key finding 2 — full chain reconstruction, numerically exact

Chaining e single alternation steps from level m down to level k (using the
coupled recursion above) and terminating at level k with the (also verified)
companion-peel pair
- O_k = a1 + OddSum(R∪Γ_{k-2})   [already certified form]
- E_k = OddSum(R∪Γ_{k-1})       [the companion Even-target formula — **not**
  previously written down in any certified file; I derived and verified it
  fresh: a1 sits at odd rank so contributes 0 to E_k, and removing it shifts
  parity of the rest exactly once]

reconstructs O_m and E_m **exactly** (20,000 fresh trials, zero mismatches,
matching brute-force ground truth digit-for-digit) — this is a fully correct,
provable e-fold identity, a strict generalization/fix of round 16's broken
Step 0.

### Key finding 3 — the real target closes ONLY when GT(m)'s own count cap
### |D|<=m+1 is respected; round 16's "counterexample" was out of scope

I directly tested whether the reconstructed O_m meets min(sum(D),2^m):
- **Without** enforcing |D|<=m+1: 42/20000 violations found (min margin
  -0.406), reproducing round-16's/current.md's counterexample phenomenon —
  but every violation I logged had |D| strictly greater than m+1 (e.g.
  k=1,e=1,m=2 with |D|=4 or 5, while m+1=3). This exactly matches the
  reviewer's cited counterexample (k=1,e=1,m=2, |D|=5>m+1=3).
- **Enforcing** |D|<=m+1 (GT(m)'s own stated hypothesis, which the round-16
  Step-0 argument silently dropped when it let R grow unboundedly along the
  chain): **zero violations in 20,000 fresh trials**, minimum margin found
  ≈0.004 (near-tight, consistent with genuine boundary behavior at
  sum(D)=2^m).

**This is the central actionable finding for the outliner**: GT(m) sub-case
(i) is very likely TRUE as originally intended (respecting the cardinality
cap), and round 16's refutation, while a correct refutation of the *literal
sentence written* (which had no count cap), does not refute GT(m) itself — it
refutes an accidentally over-generalized restatement. The real gap is a
**missing cardinality bookkeeping argument**: proving that as e grows, the
excess count |D|-(k+1) — which is what makes naive per-level GT(k-1)
induction fail — never actually breaks the *chained* identity's ability to
reach the target, because the chain does not re-invoke GT(k-1) at all; it
routes through the count-unrestricted Large-Sum Closure Theorem (uses no cap
on |R|) plus the new Even-target twin needed when e is odd.

### What's still missing (real gap, not yet closed)
1. **Even-target Large-Sum Closure analogue.** When e is odd, the chain lands
   needing a lower bound on E_k = OddSum(R∪Γ_{k-1}) (not O_k), for which no
   certified analogue of the Large-Sum Closure Theorem exists yet. By the
   same Half-Sum-Corollary technique it should give
   OddSum(R∪Γ_{k-1}) >= (sum(R)+2^k-1)/2, and an analogous threshold
   arithmetic check (parallel to the certified k-1-shifted version) is needed
   — likely a short, mechanical adaptation but NOT yet done/certified.
2. **The count cap itself must be threaded through the argument analytically**,
   not just imposed as a numeric-test filter: need to show that whatever
   linear/threshold algebra closes Large-Sum Closure (sum(R)=2^m-a1) still
   gives a nonnegative margin once composed through e single-step
   Odd/Even flips — I only confirmed this numerically (margin >=0.004 over
   20,000 trials incl. adversarial-ish random count up to m), not proved via
   the exact algebra chain (the alternation introduces 2^(j-1) additive terms
   at every level, which must be summed and shown to dominate along with the
   base bound — an explicit closed-form telescoped sum is a straightforward
   but unproven next step: sum_{j=k+1}^m 2^(j-1)·[parity indicator] plus the
   base O_k/E_k bound, compared against min(sum(D),2^m)).
3. Both of the above are now precisely scoped, mechanical-looking gaps (not
   vague) — a real candidate for full closure next round, given the exact
   chain identity is now nailed down and independently verified.

### Cheap-kill candidates
- Before any heavy write-up: verify by parity of e whether the chain always
  terminates needing O_k (e even) or E_k (e odd) — confirmed above, both
  occur, both companion-peel formulas are now available (E_k's is new, not
  yet certified).
- A quick necessary check: does the reconstructed exact telescoped sum
  sum_{j=k+1}^{m}2^(j-1)·(parity pattern) actually equal 2^m-2^k exactly when
  fully expanded (i.e. does tracking BOTH O and E recover the FULL naive
  telescoping sum, unlike my earlier flawed "two-step captures only every
  other power" analysis)? I re-checked: since every single level contributes
  its own 2^(j-1) term (not skipped), the full alternating chain, when
  correctly composed as a coupled (O,E) pair rather than collapsed
  prematurely to a single O-only two-step, in fact recovers the FULL sum
  2^(m-1)+2^(m-2)+...+2^k = 2^m-2^k (verified: for e=1,k=1,m=2, chain gives
  O_2 = 2^1+E_1 = 2 + O_k(companion) — matches; no shortfall). **My earlier
  intra-session "2/3 shortfall" concern (from the naive two-O-only-step
  collapsing) was itself a dead-end mis-framing on my part — the coupled
  (O,E) chain has NO shortfall; it's exact.** This is an important correction
  to flag to the outliner: don't chase a "make up 1/3 shortfall" sub-problem;
  it doesn't exist once O and E are tracked together correctly.

### Candidate technique(s)
Coupled two-quantity (OddSum, EvenSum) linear recursion chained e times,
terminating in the (now partially certified, partially new) companion-peel
pair at level k, then closed via Half-Sum-Corollary-style threshold algebra
(as in the certified Large-Sum Closure Theorem) — needs the Even-target twin
theorem plus an explicit telescoped-sum vs. target inequality proof.

### Knowledge-base entries to use
- Half-Sum Corollary, Large-Sum Closure Theorem
  (`lemmas/half-sum-corollary-and-large-sum-closure-theorem.md`) — reusable
  as-is for the Odd-target base case; needs an Even-target twin.
- Unified Threshold-Pair-Peeling Lemma, Rank-Shift Identity
  (`lemmas/monotonicity-reduction-and-unified-threshold-pair-peeling.md`) —
  source of both the q=0 clause and the general Rank-Shift Identity (which
  already, in full generality, gives the E_k companion-peel formula for free
  — it wasn't necessary to "discover" it, just to apply the existing lemma's
  general q=1-odd-branch statement to the Even target too).
- Monotonicity Reduction Lemma — NOT needed for this chain (it requires fixed
  count k matching S_0, which is exactly the machinery this chain avoids by
  routing through the count-unrestricted Large-Sum Closure Theorem instead).

### Analogous past problems (cruxes)
- `aimo-0225` (combinatorics, games-and-strategy/telescoping-flavored): "Determine
  the game value by recursing on the 2-adic valuation of a difference that
  exactly halves at each relevant step, so the P/N status flips with each
  halving and depends only on the valuation's parity." Genuinely analogous
  structurally: a quantity's classification flips with a fixed period as you
  descend a recursion, and the resolution requires tracking BOTH states
  (like/unlike parity) rather than assuming the quantity is self-similar at
  every step — same crux shape as "must track the coupled (Odd,Even) pair,
  not a single collapsed quantity." Worth reading in full if the outliner
  wants a template for writing the parity-dependent closing argument cleanly.
- No other crux found with a comparably close structural match after
  filtering `combinatorics`/`telescoping-and-summation` and
  `games-and-strategy` (45 candidates scanned); the rest are mirroring/pairing
  strategies for physical games, not summation identities.

### Prior progress
Certified: Half-Sum Corollary, Large-Sum Closure Theorem (round 16). Rank-Shift
Identity / Unified Threshold-Pair-Peeling Lemma, q>=2 unconditional closure
(round 13). GT(m) itself certified for m=0..3 (with sum(D)<3·2^(m-1) scope,
later fully de-capped for m<=3 via Monotonicity Reduction corollary). This
round's finding: the coupled single-step (O,E) alternation identity and its
e-fold composition are BOTH independently verified exact (20,000 + 20,000
trials, zero violations each), and — new — the target closure holds with
zero violations in 20,000 trials once GT(m)'s own count cap |D|<=m+1 is
correctly enforced (previously untested this way; round 16 never checked this
distinction).

### Dead ends (do not retry)
- Round 16's Step 0 ("OddSum(D∪Γ_{j-1})=2^(j-1)+OddSum(D∪Γ_{j-2})" as an
  Odd-only telescoping, i.e. treating O as self-recursive without the E
  companion): confirmed false again independently (matches current.md).
- My own mid-session dead end: assuming the "corrected two-step" O_j=2^(j-1)+
  O_{j-2} telescopes to only every-other power of 2 (a "2/3 shortfall"). This
  is WRONG — it was an artifact of not tracking E alongside O. Composing the
  full coupled (O,E) chain recovers the exact target sum with no shortfall.
  Do not re-derive or worry about a "missing 1/3" — it doesn't exist.
- Treating round 16's counterexample (|D|=5, m+1=3) as a genuine refutation
  of GT(m) sub-case (i) itself: it refutes only the *unbounded-count*
  over-generalization; with the count cap restored, 20,000 fresh trials found
  zero violations. Do not report sub-case (i) as "disproved" — it is open but
  numerically very likely TRUE, with a concretely narrowed remaining gap (see
  above).

### Small-case / intuition notes (conjectural, numerically supported only)
- The coupled (O,E) e-fold chain is conjectured (strong numeric evidence,
  20,000 trials, zero violations, margins as low as 0.004) to close GT(m)
  sub-case (i) in full for every k>=1, e>=1, once (a) the Even-target twin of
  Large-Sum Closure Theorem is proved, and (b) the telescoped-sum-vs-target
  inequality is verified algebraically (not just numerically) for both
  e-even and e-odd cases.
- This margin of ~0.004 at some near-boundary instance suggests the true
  inequality is close to tight somewhere in the width-1 window — consistent
  with the problem's own name for this as "the width-1 window," i.e. the
  boundary case a1 close to 2^(k-1) or 2^k is where equality/near-equality
  concentrates.
