## imo-2026-03

- Distinct openings:
  1. **(MAIN FINDING) A single explicit witness closes the whole n=2
     Existence Theorem in closed form — no casework, no Σ-shape
     classification needed.** Construction: split only piece 1 (cut
     budget 1 ≤ n=2) into fragments (p2, p1−p2); leave p2, p3 untouched.
     The resulting multiset is {p2, p2, p3, p1−p2} (this is exactly the
     "pin piece 1's fragment to p2" branch of cut-allocation (1,0,0) —
     one cut fewer than the previously-studied shape (1,0,1), which
     additionally and unnecessarily bisects piece 3). Full derivation
     below; verified this is what the outliner/next round should adopt
     as the n=2 proof.
  2. Enumerate-and-eliminate via brute force: wrote a complete Σ-shape
     enumerator for arbitrary n,k (any cut-allocation, any block
     partition, any pin choice among {0,p_j}), confirmed n=2 has exactly
     the expected 10 cut-allocations, and confirmed by exact-`Fraction`
     random sampling (480+ region points, several parametrizations) that
     the winning (argmin) cut-allocation is **always (1,0,0)** — i.e.
     splitting only the largest piece — never any other of the 10
     allocations, across every sampled point. (This is evidence the
     true V(p) argmin always lives in this one family; not needed for
     the proof above, which only needs *a* witness ≤ c(2), not the
     true argmin — but useful context.)
  3. n=3 scoping: tested the direct generalization of the n=2 witness
     (split only p1 into (p2, p1−p2), leave p2,p3,p4 untouched) at
     random n=3 balanced-region points — **fails badly** (71/94 sampled
     points violate OddSum ≤ c(3), max observed value ≈0.616 vs.
     c(3)=8/15≈0.533), and the rank position of the leftover fragment
     p1−p2 relative to the tail pieces p3,p4 is **not fixed** (3 distinct
     rank-orders observed across samples). This pins down precisely why
     n=3 is qualitatively harder: the n=2 proof's key algebraic
     coincidence (see below) does not have an obvious 1-piece-split
     analogue at n=3; a working n=3 witness will need to actually use
     more of the 3-cut budget (e.g. split 2 or 3 pieces) and handle a
     case split on where fragments land among the tail.

- **Full derivation of the n=2 closure (verified in exact `Fraction`
  arithmetic, no floating point, no reviewer certification yet):**

  Region (Section 0 of `global-lp-vertex-sufficiency.md`): k=3 pieces
  p1>p2>p3>0, p1<1/2, d1:=p1−p2>γ(2), d2:=p2−p3>γ(2), γ(2)=1/7,
  p1+p2+p3=1. Target c(2)=1/2+γ(2)/2=4/7 (certified identity).

  **Step 1 (elementary algebra, exact).** From p1+p2+p3=1 and the
  substitutions p3=p4-analogue chain, one gets the closed form
  p1=(1+2d1+d2)/3. Since d1,d2>γ(2)=1/7 strictly (part of the region's
  own definition), 2d1+d2 > 3/7 strictly, hence **p1 > 10/21 for every
  point of the balanced region** — a hidden, previously unremarked
  consequence of the region's defining gap inequalities alone (does not
  even need the p1<1/2 clause). Verified both symbolically and against
  1284 exact-`Fraction` random region samples: min p1 found ≈0.4767,
  consistent with (and approaching) 10/21≈0.4762, zero violations.

  **Step 2 (the witness and its closed form).** Legal response: split
  p1 into (p2, p1−p2) [1 cut ≤ n=2], leave p2, p3 untouched. Multiset
  M={p2, p2, p3, p1−p2}, all four entries positive (p2>0 trivially,
  p1−p2>0 since d1>0).

  **Step 3 (rank order, exact, no casework).** Claim: descending order
  is always p2, p2, p3, p1−p2 — i.e. p3 > p1−p2 throughout the region.
  Proof: p3 − (p1−p2) = (1−p1−p2) − (p1−p2) = 1−2p1, and 1/2−p1 =
  (1−2p1)/2, so **p3 > p1−p2 is exactly equivalent to p1 < 1/2** — the
  region's own defining inequality. So the order claim is not a separate
  case needing verification, it is definitionally forced by the region.
  (p2 ≥ p2 tie, then p3, then p1−p2, verified this is the unique correct
  order given also p2>p3 from d2>0.)

  **Step 4 (closed form and bound).** With this order,
  OddSum(M) = rank1+rank3 = p2+p3 = 1−p1 (using sum=1). Combined with
  Step 1 (p1>10/21): **OddSum(M) < 1 − 10/21 = 11/21 < 12/21 = 4/7 =
  c(2)**, strictly, for every point of the balanced region, with margin
  exactly 1/21 at the (unattained) worst case. Hence V(p) ≤ OddSum(M) <
  c(2) for all p in the region — **this proves the n=2 Existence
  Theorem in full**, via one witness, no branch analysis, no cases.

  Verified computationally: 1284 exact-`Fraction` region samples (fresh
  parametrization, seed 7), zero mismatches between the predicted
  closed form 1−p1 and the directly-computed OddSum of the actual
  multiset; zero violations of OddSum<c(2); max observed witness value
  0.52334 (below 11/21≈0.52381 bound as expected, both below
  c(2)≈0.57143).

- Candidate technique(s): the elementary-algebra witness-construction
  method above (no LP duality, no concavity, no vertex enumeration
  needed for the actual proof — vertex enumeration was only used as a
  search tool to *find* the witness). The Flat/Kink Parity Lemma is
  useful context (this witness's pinned/free fragments, p2 and p1−p2,
  sit at ranks 2 and 4 — both even, i.e. "Flat" type per the lemma,
  meaning it sits on a mildly degenerate/robust face, not a knife-edge
  vertex — consistent with the comfortable 1/21 margin found, not
  needed for the proof itself).

- Cheap-kill candidates: none further needed for n=2 (closed). For n=3,
  a first cheap structural check for next round: before attempting
  full casework, check whether splitting p1 into 3 fragments (using 2
  of the 3 cuts) with one fragment tied to p2 and another to p3 (a
  direct extension of the mechanism) fixes the order-instability found
  in opening 3 above — untested this round, flagged as the natural next
  probe.

- Knowledge-base entries to use: the Reduction Lemma
  (`lemmas/reduction-to-multiset-minimax.md`), the c(n) identity
  c(n)=1/2+γ(n)/2, and — for context/robustness only, not needed in the
  proof — the certified Flat/Kink Parity Lemma
  (`lemmas/flat-kink-parity-lemma.md`).

- Analogous past problems (cruxes): did not find genuinely new corpus
  matches this round beyond what prior rounds already used (the
  Singleton-Interleaving / k-Anchor-Merge lemmas, already certified
  in-house); this specific "split only the largest piece, tie one
  fragment to the runner-up" witness is a direct elementary
  construction, not adapted from a corpus crux.

- Prior progress: Round 18 certified that the **(1,0,1)-branch**
  (splitting BOTH p1 and p3) always exceeds c(2) in the region — a
  correct negative result about *that* branch, but it does not
  preclude other branches from working. This round found that the
  **strictly simpler (1,0,0) branch** (splitting only p1, one fewer
  cut used) **does** work, and closes the n=2 Existence Theorem outright
  via the clean algebraic coincidence in Step 3 above.

- Dead ends (do not retry): the (1,0,1)-branch, pin-to-p2/bisect-p3
  (round 18, certified always > c(2) in the region — do not reuse as a
  witness). The naive direct n=3 lift of this round's n=2 witness
  (split only p1, tie to p2, leave rest untouched) — fails broadly
  (71/94 sampled violations) and has unstable rank order; do not retry
  verbatim at n=3 without modification.

- Small-case / intuition notes: (conjecture, not proved) numeric
  sampling (480 exact-`Fraction` region points) suggests the *true*
  global argmin V(p) at n=2 always uses cut-allocation (1,0,0) with
  this same pin-to-p2 branch (100% of sampled winners), i.e. this
  witness may not just be *a* valid certificate but the actual
  minimizer everywhere in the region — worth a follow-up exact check
  if a tighter characterization of V(p) itself (not just an upper
  bound) is ever wanted, though it is not needed to close the Existence
  Theorem. For n=3, the breakdown of the direct analogue strongly
  suggests the eventual witness must use ≥2 of the 3 available cuts
  (i.e. split more than one piece, or split p1 into 3 fragments) and
  will likely require a genuine 2–3-way case split on where the
  leftover fragment(s) rank relative to the tail pieces — this is a
  concrete, scoped starting point for the next round's n=3 attempt, not
  yet attempted.
