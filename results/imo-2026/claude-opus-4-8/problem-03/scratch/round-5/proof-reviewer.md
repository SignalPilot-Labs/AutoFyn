# Proof-reviewer report — Round 5 — imo-2026-03

## Approach: direct-constructive

**Verdict: CHANGES REQUESTED**
**True Status: partial** (matches the builder's recorded Status; but the builder's *characterisation*
"lower bound essentially complete modulo one minor degenerate face" is an OVERCLAIM — see below).

### Scores
- Correctness: the certified prior content stands; the new upper-bound reduction is correct as a
  conditional; the new lower-bound "Descent Lemma" contains a false load-bearing sub-claim.
- Completeness/rigor: lower bound NOT closed (new gap found); upper bound honestly ~94% + open.
- Progress: real but smaller than claimed. Genuine advance = corrected IH(q) relative threshold.
  The lower-bound "closure" claim does not hold up.

### Load-bearing step I re-derived independently

**Lower bound.** The whole round-5 lower-bound claim rests on: *min over Δ of A is attained at a
cell-complex vertex, and at any interior vertex a **receiver** (a fragment value w with
#{pieces > w} odd) exists, driving a descent unless A ≥ 1.* I re-derived the receiver-existence
argument and tested it computationally.

- The generic (all-distinct) argument is CORRECT: assuming no receiver forces
  i′(w_{j+1})−i′(w_j) ≡ μ_j ≡ 1 (mod 2), so i′ increases by ≥1 across n distinct levels within a
  range of only n−1 — contradiction. Verified.
- BUT the promotable claim "**a receiver always exists**" for all a=0 configs is **FALSE at clustered
  (non-generic) configs.** Exact reviewer counterexamples (n=4, intacts {1,2,4,8}, all fragments < 8,
  a=0):
  - fragments {2, 10/3, 10/3, 11/3, 11/3}: no fragment value has an odd # of pieces above it (A=5);
  - fragments {2, 7/2, 7/2, 7/2, 7/2}: same (A=5);
  - fragments {8/3, 3, 3, 11/3, 11/3}: same (A=17/3).
  (Enumerated exactly over rational grids; several more exist for n=4.)

**Why this is a real gap, not a nit.** The minimiser of A over Δ is attained at a *vertex* — a point
where n constraints {g_i=g_j}, {g_i=2^s}, {g_i=0} are tight, i.e. a *clustered, tie-laden,
non-generic* point. That is exactly the regime where receiver-existence fails. The interior-vertex
case of §4.2.7 invokes "a receiver a exists (above)"; since the universal receiver claim is false,
this branch has an **uncovered sub-case: no-receiver clustered vertices**, on top of the flat-move
(ii) termination the builder already admits is unwritten. The random numerics (1.5·10^5 configs) do
NOT detect this because clustered configs are measure-zero — they never get sampled. min_Δ A = 1 is
numerically true (I reconfirmed for n=2..5), so the *answer* is right, but the *proof* does not
establish A ≥ 1 at these vertices. **The lower bound is NOT closed this round.**

**Upper bound.** I checked the corrected IH(q) reduction. The two one-cut moves (halve b_1 → residual
sum S−b_1 on {b_2,…,b_q}; cut b_1 at b_2 → residual sum S−2b_2 on {b_1−b_2, b_3,…,b_q}) each cancel a
consecutive equal pair (valid Lemma-H pair-cancellation, A unchanged, parities preserved) and leave a
valid IH(q−1) instance with all pieces >1/D (in the hard regime b_1−b_2 > 1/D). So a valid reduction
exists iff S − max(b_1, 2b_2) < (2^{q−1}−1)/D — a correct tautology given those two moves. The
refutation of the earlier absolute threshold b_1 > 2^{q−2}/D is legitimate. This is a genuine, correct
advance, but it is a **conditional** — it does not prove IH(q); the ~94% figure is empirical, and the
~6% flat two-cut residual + sub-case B2 (a_1 ≤ 1/2) are honestly open.

### Certification of the three proposed lemmas
1. **Descent Lemma (a=0 lower-bound engine)** — **REJECTED.** Contains the false receiver-existence
   sub-claim at clustered vertices, plus the admitted unwritten flat-move (ii) termination. Not
   `sorry`-free.
2. **Receiver-existence parity lemma** — **REJECTED.** FALSE as stated (counterexamples above). Only
   true on generic all-distinct configs; the statement must be restricted to that case, in which form
   it is correct but is not what the descent argument needs at a minimising vertex.
3. **Corrected IH(q) relative-threshold reduction** — the *conditional reduction step* is rigorous and
   correct. But the promotable statement bundles in the empirical "closes ~94%" claim, which is not a
   theorem. **Not certified as a standalone lemma this round** (it does not prove IH(q); it is a
   correct sub-step already recorded in the approach file). If re-proposed trimmed to the pure
   conditional ("IF S−max(b_1,2b_2)<(2^{q−1}−1)/D THEN one cut reduces to a valid IH(q−1) instance"),
   it would pass.

### Precise remaining gaps
- **Lower bound (★):** A ≥ 1 at a=0 **clustered vertices** of Δ — now sharpened: the descent argument
  fails there because no receiver need exist. Next round must either (a) prove A ≥ 1 directly at
  no-receiver clustered vertices, or (b) show a minimiser is never a no-receiver clustered vertex, or
  (c) find a different certificate. The flat-move (ii) termination is a second, smaller loose end.
- **Upper bound U1:** the ~6% flat two-cut cascade residual of B1-large (IH(q≥4)) and sub-case B2
  (a_1 ≤ 1/2, no dominant piece) entirely.

### Why CHANGES REQUESTED (not RETHINK)
The approach remains the field leader with a large certified core (G1, R, H, X, CaseB-reductions,
Spare-R_n, Lemma S, fragment-count, interleaving value, IH(1–3)). The Δ-minimisation framing is sound;
only the descent step is over-claimed. The gap is repairable within the framing. Not a dead end.

### Recorded
`record_outcome(direct-constructive, round 5, partial)` — note names the receiver-existence
overclaim + the correct IH advance. current.md updated (Status partial; reviewer finding appended;
no new lemmas certified).
