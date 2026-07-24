## imo-2026-03 — lens: closing the last 2/6 (star_3) residual shapes (1,2,0,0) and (2,1,0,0)

### Setup recap (verified against the approach file, §7.18.4)
Shape (2,1,0,0): π1=8 splits into a triple f1≥f2≥f3≥0 (sum 8, pigeonhole f1≥8/3);
π2=4 splits into a pair c≥d≥0 (sum 4, forced c≥2); π3=2, π4=1 untouched.
U = {f1,f2,f3,c,d,2,1}. Need: A(U) ≥ 1 for **every** feasible (f2,f3,d) (equivalently
f1=8-f2-f3, c=4-d), where A is the peel-the-max alternating-sum functional
(A(S) = max(S) − A(S∖max), the same functional used throughout the file). Achievability
of A=1 is already proved (round 28, construction {4,4,2,2,2,1}). Shape (1,2,0,0) is the
mirror case: π1=8 splits into a pair a≥b≥0, π2=4 splits into a triple g≥h≥i≥0.

### Distinct openings
1. **Vertex-enumeration closure (recommended primary route).** The domain is a
   3-free-parameter polytope (f2,f3,d for (2,1,0,0); b,h,i for (1,2,0,0)) and A(U) is
   piecewise-linear on it (linear on each fixed sorted-order region). The file's own
   certified `vertex-minimum-theorem` / `exchange-smoothing-vertex-maximization`
   machinery (dualized to a minimum) says the min of a piecewise-linear function on a
   polytope is attained at a vertex — a point pinned by ties among {f1,f2,f3,c,d,2,1}
   or by hitting a boundary face (f3=0 or d=0, i.e. the "cut is degenerate"). Round 10
   already found and partially fixed a real gap in this exact mechanism (the pin-set
   must include 0, not just {τ_1,...,τ_r}) — that fix should be pulled in here rather
   than re-derived. This turns the open casework into: (a) enumerate the finitely many
   vertex types for this specific 3-parameter polytope (much smaller than a general
   enumeration since only 2 pairs/triples are free), (b) evaluate A at each via the
   already-certified Odd-Run Reduction Lemma, (c) check ≥1 at each. This is the same
   discrete-enumeration discipline that closed all of §7.16's other shapes and Claim
   A's Case I — it replaces the stalled ad hoc branch tree (which the file itself
   diagnoses as "not independent" sub-cases) with a finite, exhaustive, structurally
   justified list.
2. **Direct identity on the equality face.** Numerically (see below) the minimum A=1
   is attained not at one isolated point but on a whole positive-dimensional flat
   region (e.g. d=0 with f1>c=4>f2>π3=2>f3>π4=1>0 gives A = (f1+f2+f3) − (4+2+1) =
   8−7=1 identically, for ANY f1,f2,f3 satisfying that order — not just at a vertex).
   This suggests hunting for a clean **general identity**: whenever the sorted order
   interleaves the π1-fragments and π2-fragments with the untouched values in a fixed
   pattern, A(U) collapses to (sum of one π's fragments) − (sum of the other fixed
   values), independent of the exact split — i.e., an extension of the already-
   certified `cross-term-reduction-theorem` / `peel-decomposition-identity` machinery
   to two simultaneously-split parents. If this identity is proved once, in general,
   most order-type cases become free (A is *constant* = 1 there), and only a much
   smaller number of genuinely non-flat regions need bounding, not enumerating.
3. **Reduce the "which top dominates" branch via a monotonicity/exchange argument
   instead of casework.** Fix f1,f2,f3 and vary the split (c,d) with c+d=4 continuously
   from the symmetric point toward (4,0): check whether A(U) is monotonic (weakly
   decreasing) in c on this segment for every fixed f-triple. If so, the worst case for
   the (c,d) split is always at the degenerate vertex d=0, cutting the problem down to
   a genuinely 2-parameter problem (f2,f3) against fixed values {4,2,1,0}, which is
   exactly a "known" shape-type problem the file has already closed elsewhere (single
   split against 3 fixed untouched values, cf. (2,0,0,1)/(2,0,1,0) closures). This is a
   bypass that never needs the "cross-pair joint feasibility" branch the file flagged
   as the blocker, because it establishes d=0 is always at least as bad as any other d
   — collapsing the two-split shape to a one-split shape whose closure technique is
   already on file.

### Cheap-kill candidates
- Check whether A(U) is *linear and monotone* in d on each fixed order-type region
  (opening 3 above) — if provable in general (not just numerically), this alone
  reduces the two-split shapes to already-solved one-split shapes, killing most of the
  remaining casework in one stroke.
- The "d=0 identity" (opening 2) is a cheap structural check: verify by hand (not just
  numerics) that whenever f1>c, c>π3, f2 lies between π3 and c, etc. — i.e. whenever
  the untouched values 2,1 interleave one-for-one with fragments of BOTH splits — A
  collapses to a totals-difference. This is a two-line algebra check, much cheaper than
  full casework.

### Candidate technique(s)
Discrete piecewise-linear vertex minimization (dualizing the certified
`exchange-smoothing-vertex-maximization` / `vertex-minimum-theorem`), combined with the
Odd-Run Reduction Lemma for closed-form evaluation at each vertex — the same toolbox
that closed Claim A's Case I and the other 4 (star_3) shapes. Do NOT re-attempt the
branch-by-branch casework as currently written; it is exactly the "not independent
sub-cases" trap the file diagnosed.

### Knowledge-base / lemma entries to use
- `vertex-minimum-theorem`, `exchange-smoothing-vertex-maximization` (dualize to min;
  apply round-10's pin-set-includes-0 correction).
- `odd-run-reduction-lemma` (closed-form evaluation at ties/vertices, handles multi-way
  ties — needed here since the flagged obstruction is exactly a joint tie/boundary
  condition across two independently-split parents).
- `sharp-dominant-removal-identity`, `peel-decomposition-identity`,
  `cross-term-reduction-theorem` (for opening 2's identity-hunting).
- `case-i-closure-theorem` as a worked template for "how a two-split-parent case was
  closed elsewhere in this project" (Claim A's own closure used exactly this
  exchange-smoothing + odd-run-reduction combination).

### Analogous past problems (cruxes)
Did not re-run the crux corpus query this pass (out of scope for this narrow lens —
the analogous "cases" already live inside this same project's own certified lemmas,
which are a stronger match than any external corpus problem). No specific external
crux stands out beyond what prior rounds already cited for this problem's general
vertex-enumeration technique.

### Prior progress
- 4 of 6 (star_3) residual shapes fully closed: (2,0,1,0), (2,0,0,1), (1,1,0,1),
  (1,1,1,0).
- (1,2,0,0), (2,1,0,0): achievability at A=1 already proved (construction
  {4,4,2,2,2,1}). Lower bound NOT closed; one sub-sub-case worked as a template
  (branch f1≥c, f2≥c, f3≥c, using the cross-constraint c≥4−f3).

### Dead ends (do not retry)
- Treating c and f3 (or the analogous pair in (1,2,0,0)) as independently free when
  bounding the residual after peeling — the file explicitly caught this bug this round
  (spurious near-violation →6⁻ instead of >6) before fixing it with the joint
  feasibility constraint c≥4−f3. Any future derivation must carry this cross-
  constraint explicitly, not assume the two splits' own defining inequalities alone
  suffice.
- Continuing the branch tree exactly as currently split (f1≥c vs f1<c, then f2 vs c,
  then f3 vs c, ...) — the file itself found these sub-cases are "not independent,"
  i.e. this exact case tree is the wrong decomposition to keep pushing on verbatim;
  better to re-derive from the vertex-enumeration mechanism (opening 1) which is
  structurally guaranteed exhaustive, rather than patching more ad hoc branches onto
  the existing tree.

### Small-case / intuition notes (numeric, NOT a proof)
Ran exact-`Fraction` (not float) dense grid searches over the full feasible polytope
for both shapes (grid step 1/24, ~10⁴–10⁵ points each, `/tmp/search3.py`,
`/tmp/search4.py`):
- Shape (2,1,0,0): global minimum of A(U) found = exactly 1 (Fraction(1,1)), zero
  violations below 1 across the grid; 351 distinct grid points hit exactly 1,
  indicating the equality locus is a positive-dimensional set (a face), not an
  isolated vertex — consistent with opening 2's "flat identity region" conjecture.
  Confirmed by hand: at d=0, c=4, any f1,f2,f3 with sum 8 and order
  f1>4>f2>2>f3>1>0 gives A = f1+f2+f3−4−2−1 = 8−7 = 1 exactly (checked symbolically
  for several exact rational triples, e.g. (41/10,21/10,9/5), (9/2,5/2,1),
  (401/100,201/100,99/50) — all give A=1 exactly). A second distinct equality vertex
  also found: (f1,f2,f3,c,d)=(4,4,0,3,1), sorted {4,4,3,2,1,1,0}, A=4-4+3-2+1-1+0=1.
- Shape (1,2,0,0): same grid search, global minimum found = exactly 1, no violations,
  witness (a,b,g,h,i)=(4,4,0,2,2).
Both results are strong numeric corroboration (conjecture, not proof) that MinFloor(4)
= 1 genuinely holds on these last two shapes with no slack anywhere, and that the
equality locus is large/structured — favoring opening 2 (a general identity on
sorted-order regions) or opening 1 (finite vertex enumeration) over more branch-by-
branch casework, since a flat equality face is exactly the signature of an underlying
identity rather than a tight-margin inequality needing delicate case splitting.
