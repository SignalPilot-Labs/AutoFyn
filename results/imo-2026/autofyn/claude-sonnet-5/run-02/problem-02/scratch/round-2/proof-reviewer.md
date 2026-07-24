# Proof review — IMO-2026-02, round 2

## Method

Independently re-derived, from the raw hypothesis definitions (not from
the builders' stated intermediate formulas), the entire elimination chain
for `complex-number-argument-bash` in a fresh `sympy` script, and
independently re-verified the vacuity claim for
`symmetric-vector-decomposition-sigma` with unconstrained free-variable
symbolic algebra. Scripts used: `/tmp/verify1.py`, `/tmp/verify2.py`
(complex-number-argument-bash), `/tmp/verify3.py`
(symmetric-vector-decomposition-sigma).

---

## 1. `complex-number-argument-bash`

**Verdict: CHANGES REQUESTED. Status: partial** (builder's own self-report
of `partial` is accurate; this is real, substantial, independently
confirmed progress with one concrete gap remaining).

### What I independently re-checked, from scratch

Built `eq1, eq2, eq3` directly from the cross/dot definitions in the WLOG
frame `B=(0,0), C=(1,0), A=(p,q)`, exactly as specified in the approach
file's Dictionary-Lemma section, with no reliance on the builder's
intermediate algebra.

- **Step 1 (eliminate L via eq1).** Confirmed `eq1`'s `l2`-coefficient is
  exactly `-D` with `D = k1p²-k1p-k1q²+2k2pq-k2q` (matches). **Found a
  sign error in the write-up's displayed formula**: it states
  `l2 = l2_num/D`, but I verified by direct substitution that this does
  NOT satisfy `eq1=0` (`sympy` gives a nonzero residual); the correct
  formula is `l2 = -l2_num/D`. This is confirmed to be a prose/LaTeX typo
  and not a computational error: rebuilding Steps 2-4 from scratch with
  the correct-sign `l2` reproduces the claimed `X`, `eq2_num` (degree 2 in
  `l1`, degree 3 in `k1,k2`), `Fn_den_raw = 4·D·D3`, and the closing
  identity exactly — so whatever `sympy` session actually produced those
  downstream artifacts must have used the correct sign internally. I
  corrected the display formula in the approach file and added an
  explanatory note; this does not weaken the proof, but the sign slip
  itself is worth flagging as a lesson (see memory update below).
- **Step 2 (cubic locus X).** Independently re-derived `eq3_num =
  -(l1-1)(p²+q²)·X`, with `X` matching the approach file's cubic
  **exactly** (confirmed via `sympy.factor`).
- **Step 3 (eq2_num).** Confirmed degree 2 in `l1`, total degree 3 in
  `(k1,k2)` — matches.
- **Step 4 — THE LOAD-BEARING CLAIM.** Independently computed
  `Fn_num_raw` (numerator of `O_x - (p/2+1/4)` for the circumcenter of
  `A,K,L` with `l2` eliminated), confirmed `Fn_den_raw = 4·D·D3` exactly,
  and directly verified the claimed identity
  `Fn_num_raw·D2 - (k2-q)·eq2_num = D·X·(E1·l1+E0)` by expanding both
  sides and checking `sympy.expand(LHS-RHS) == 0`. **Result: `True`,
  reproduced independently from raw definitions, not copy-checked from the
  builder's numbers.** Also independently confirmed the corollary
  `D_circ|_{l2=l2_expr} = 2·D3/D` exactly. This is the identity the round-2
  explorer's earlier (unverified) cofactor claim failed to reproduce, per
  the outline-reviewer's report — the builder's replacement identity is
  correct where the explorer's was not. **This is a genuine, closed, hard
  computational result — the field's single deepest verified fact.**

### The genericity argument (Step 5)

The linear-independence-of-D,D2 argument and the resultant/Bezout argument
for `X=0 ∩ {D=0 or D2=0}` being finite are sound in structure and the
concrete algebraic sub-claims (coefficient pairs of `D`, `D2` never both
vanishing for `q>0`) check out by direct substitution. The
continuity/implicit-function-theorem closing argument is a legitimate
proof technique (continuous function vanishing on a dense subset of a
connected continuum vanishes everywhere on it) and is not obviously
flawed, though it is denser prose than hard computation. The builder
**explicitly and honestly flags** one sub-step (re-running the finiteness
argument for finitely many exceptional triangle shapes) as asserted by
analogy rather than executed — this is a minor, likely-fixable residual
gap, clearly smaller than the orientation gap below, and not fatal to the
overall Step-5 strategy.

### The orientation/sign-matching gap — confirmed real and still open

This is the correct characterization of what remains. The Dictionary
Lemma (verified correct as pure algebra: `cross(u,v)dot(w,z) =
cross(w,z)dot(u,v) ⟺ θ1=θ2` when the two vector pairs have matching
rotational sense, `⟺ θ1+θ2=π` if mismatched) only proves what it proves —
it does NOT by itself establish that the *specific* pairings chosen for
`eq1,eq2,eq3` are the sense-matched ones. If even one of the three
pairings is mismatched, `eq1=0`/`eq2=0`/`eq3=0` encode a supplementary-
angle condition instead of the problem's actual hypothesis, and the entire
downstream algebra — while internally consistent as I've now verified it
to be — would be solving a *different* (wrong) system, and the numeric
witness's agreement, while corroborating, is not a proof (a genuinely
mismatched system could still have isolated solutions that happen to
satisfy the target coincidentally, or the numeric witness itself may not
be representative if there are multiple branches of the (K,L) family with
different orientation behavior). The builder is right to flag this
honestly as unclosed; I confirm it is a real, load-bearing gap and not
already resolved elsewhere in the writeup (I searched the whole approach
file for any hidden justification and found none beyond the acknowledged
partial betweenness argument).

**Net assessment.** This round closed the single hardest remaining
computational obstacle (Step 4) with a result I independently reproduced
from first principles. The proof is NOT yet complete: the orientation
gap is real, substantive, and — if unresolved — could in principle
invalidate the entire chain (not just weaken it). Status: **partial**,
not solved. `current.md` updated accordingly (kept at `partial`, with an
accurate, updated Current best).

---

## 2. `symmetric-vector-decomposition-sigma`

**Verdict: RETHINK. Status: unsolved** (overriding the builder's own
self-labeled `partial`, per the standing per-role rule that a refuted
core/load-bearing mechanism is RETHINK even when generic byproduct lemmas
survive).

### Lemma A (σ-invariance of the 8-clause system) — checked, sound

Read the full clause-by-clause argument. Each step is an elementary
labeling fact (a triangle's interior / an angle's identity depend only on
the unordered vertex set / unordered ray pair, not on the order symbols
are listed). No hidden gap. This genuinely upgrades the round-2 explorer's
numeric spot-check to a real proof, and is correct.

### Lemma B (vacuity of the naive antisymmetry mechanism) — independently
re-verified, confirmed correct

I built the O-free reformulation's `O·(C-B)` term with 10 fully free,
unconstrained coordinate symbols (`Ax,...,Ly`, no hypotheses imposed at
all) in `sympy`, applied the swap `B↔C, K↔L`, and confirmed
`Oterm(swap) + Oterm` simplifies to exactly `0` — matching the builder's
claim that this sign-flip is a content-free algebraic tautology, using
zero information from hypotheses (i)-(iii). Combined with the (equally
trivial) order-invariance of circumcenter/nine-point-center, this
confirms `T(A,C,B,L,K) = -T(A,B,C,K,L)` holds identically for **all**
points, not just valid solutions.

**This is a correct, well-executed negative result.** The builder's
conclusion — "a sign-flip identity alone can never force `T=0` without a
second, independent relation, and relabeling alone supplies none" — is
logically sound: `f(x') = -f(x)` for the *same* evaluation `x` (since
relabeling doesn't produce an independent second data point, just a
description of the same numbers) never implies `f(x)=0` in general.

The builder's own isosceles sanity check (where σ IS realized by an
actual reflection isometry, supplying the missing second relation, and
the mechanism *does* work there) is a nice consistency check that
correctly explains why the general-scalene mechanism fails: σ there is
only a combinatorial symmetry of the equations, not a geometric isometry
of the plane.

### Why this is RETHINK, not CHANGES REQUESTED

Per the standing memory rule (round 1): a builder's own report saying the
approach's load-bearing mechanism "cannot complete as designed" overrides
a self-labeled `partial` to `unsolved`/RETHINK, since CLAUDE.md's RETHINK
criterion is about the mechanism being wrong, not about whether some
prior/generic lemma still stands. Here the builder has done exactly that:
proved, not just conjectured, that the slug's defining mechanism (naive
σ-antisymmetry ⟹ vanishing) is mathematically incapable of proving the
theorem, with the negative result independently confirmed by me. The two
lemmas produced (σ-invariance, vacuity) are valuable, certified,
general-purpose byproducts, but they do not constitute progress toward
`OM=ON` by themselves — the slug's own approach is dead as conceived.

The builder does sketch a possible "genuine rescue" (explicit sine-rule
use of conditions (ii)/(iii), not just formal σ-pairing) but explicitly
did not attempt it, and flags it as comparable in difficulty to
`complex-number-argument-bash`'s already-mostly-closed elimination. This
is a legitimate direction for the outliner to consider next round, but as
a *new* approach (or a substantial pivot), not a continuation of the
current mechanism.

---

## Lemma certification

Certified two new lemma files (both `sorry`-free, independently
re-verified, statements no stronger than proved):

- `results/imo-2026-02/lemmas/closing-polynomial-identity-step4.md` — the
  Step-4 closing identity `Fn_num_raw·D2 - (k2-q)·eq2_num = D·X·(E1·l1+E0)`
  and the `D_circ = 2D3/D` corollary, both independently re-derived from
  scratch and confirmed. Includes a documented note on the Step-1 sign
  typo in the source approach file (corrected there too).
- `results/imo-2026-02/lemmas/sigma-invariance-and-vacuity.md` — Lemma A
  (σ-invariance of the 8-clause system) and Lemma B (vacuity of the naive
  antisymmetry mechanism), both independently verified.

## current.md

Updated (`results/imo-2026-02/current.md`). Status remains `partial`.
`## Full proof` remains empty. `## Current best` rewritten to reflect: (1)
the Step-4 identity is now a fully closed, independently-verified
computational result — the deepest fact established in the project so
far; (2) the orientation/sign-matching gap is the sole remaining item
standing between the current state and a complete proof via
`complex-number-argument-bash`; (3)
`symmetric-vector-decomposition-sigma`'s own mechanism is a proven dead
end, with two certified byproduct lemmas salvaged.

## record_outcome calls

- `complex-number-argument-bash`: outcome `advanced`, round 2 — closed
  Step-4 identity (independently reproduced), orientation gap is the sole
  remaining item.
- `symmetric-vector-decomposition-sigma`: outcome `dead-end`, round 2 —
  core mechanism proven vacuous (independently reconfirmed); byproduct
  lemmas certified but the slug's own approach cannot yield the proof.

## Bottom line for next round

`complex-number-argument-bash` is the clear leader and the only live route
to a complete proof. The single remaining task is: for each of the three
Dictionary-Lemma applications (hypotheses (i),(ii),(iii)), determine the
actual rotational sense forced by the corresponding containment hypothesis
(`K∈∠LBA`/`L∈∠ACK` for (i); the relevant betweenness for (ii),(iii)) using
the betweenness ⟺ matching-cross-product-sign criterion already derived
this round, and confirm all three pairings used in `eq1,eq2,eq3` are
sense-matched (or, if not, correct the sign and re-verify the identity
still gives the target — likely no change needed since flipping a sign in
the Dictionary Lemma just flips which of `θ=φ` / `θ+φ=π` is being encoded,
but this must be checked explicitly, not assumed).
