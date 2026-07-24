# Round 7 proof-reviewer report — imo-2026-03

All three approaches independently re-verified from scratch (exact `Fraction`/`sympy`
arithmetic, bounded computation only — no unbounded search, per the standing guardrail). No
hangs. All three are genuine, real progress; none is `solved`; no wholesale RETHINK needed.

## 1. `dyadic-cascade-induction` — verdict: CHANGES REQUESTED (Status: partial, correctly
self-reported as partial, but with one precise correction needed)

**What was independently re-verified and confirmed correct:**
- **Step 1 (Guaranteed-Untouched-Original Lemma).** Elementary pigeonhole (`\le m` cuts touch
  `\le m` cut-forest roots, `k=m+1>m` originals ⇒ ≥1 untouched). Re-derived from scratch,
  correct, no gap.
- **Step 2 / family (A) (Shared-Value Cycle-Breaking Lemma, generalized `L=2→L\ge2`).**
  Piecewise-linear breakpoint argument via the already-certified Vertex Lemma. Spot-checked
  concretely on `D_2=(4,2,1)` (tying pieces `4,2` at shared `t\in(0,2)`, piece `1` untouched):
  `e(t)` is constant `=3` on `[0,1]`, strictly decreasing on `(1,2)` towards `1` at the
  degenerate boundary `t\to2^-` — matches the claimed shape exactly (min never at an interior
  point).
- **Cross-Type Cycle Infeasibility Lemma (new, `L\ge3`).** Re-derived the sum-and-dominance
  argument from scratch independently: summing the cyclic system `u_i+u_{i+1}=b_{i+1}` gives
  `\sum u_i=S/2`; relabelling `b_1=\max=M`, the equation `u_L+u_1=M` gives
  `u_2+\dots+u_{L-1}=S/2-M<0` (by the superincreasing dominance fact `M>S-M`) — a sum of
  `\ge1` strictly positive terms forced negative, contradiction. Independently reproduced by
  exact `sympy` linear-system solving for `L=3,4,5` on `D_2,D_3,D_4` (100 random
  subset/ordering trials): odd `L` always gives a unique but infeasible solution, even `L` is
  always inconsistent — exactly matching the proof's predicted failure modes, zero exceptions.
  This is a genuinely new, correct, general theorem.

**The gap found (the reason for CHANGES REQUESTED, not APPROVE of this sub-result as
"complete"):** the file's Step-3 body text ("Combining families (A) and (B): every
all-cycles configuration built entirely from distinct, once-cut original pieces of `D_m` ...
is now accounted for") mildly overclaims relative to its own, more careful section header
("resolved for shallow cycles, **honest remaining gap for deep/mixed cycles**") and its own
"cases covered / not covered" bullet (which explicitly lists "a cycle ... with mixed edge
types" as open). Lemmas (2) and (3) as proved only cover **uniform**-type cycles (every edge
the same shared-value or the same cross-type shape); a cycle that **mixes** shared-value edges
and cross-type edges within itself, even with every participant an original piece, satisfies
neither lemma's hypothesis and is not addressed anywhere in the file. I independently ran an
**exhaustive** (not sampled) search for such mixed cycles: for `D_4` (`L=4,5`: 720+2400 full
enumerations over every subset/ordering/edge-pattern with `\ge2` of each type) and `D_5`
(`L=4,5,6`: 2160+14400+36000 full enumerations) — **zero feasible mixed-type cycles found**.
This is corroborating evidence the residual case may resolve the same way, but it is **not a
proof**, and the file does not currently attempt one. I've folded this precise scope
correction into `current.md` and the certified lemma file.

**Certified:** `lemmas/shallow-cycle-resolution.md` (Guaranteed-Untouched-Original,
Shared-Value Cycle-Breaking generalized, Cross-Type Cycle Infeasibility), with the mixed-edge-
type gap and derived-participant gap both stated explicitly as open, not closed.

## 2. `potential-weighting-upper-bound` — verdict: CHANGES REQUESTED (Status: partial, correctly
self-reported, no overclaim found)

**What was independently re-verified and confirmed correct:**
- **Layer-cake identity for `e`.** Re-derived the proof from scratch (interval decomposition +
  induction on parity). Independently re-verified by 2000 random exact-`Fraction` trials
  (`n=1..8`) comparing the direct formula against the interval-integral formula — zero
  mismatches.
- **Non-crossing inside/outside independence.** Elementary, correct combinatorial argument
  (crossing-condition algebra), re-derived directly, no gap.
- **The decisive counterexample.** Independently reconstructed from scratch (my own
  from-scratch exhaustive enumeration of all 925 selections with cost `\le3` on
  `Y=(39,36,30,28,22,18,14)`): `OPT(Y,3)=1` (achieved by kept={14}, matched
  `(39,30),(36,22),(28,18)`) and `NC(Y,3)=2` (achieved by kept={30,28,14}, deleted={39,18},
  matched `(36,22)`) — **matches the file's claims exactly**, including the specific winning
  selections. Also independently reconfirmed the second counterexample
  (`Y=(400,218,194,187,169,27,3)`: `OPT(Y,3)=4<NC(Y,3)=6`; `OPT(Y,4)=4<NC(Y,4)=5`) and that
  **both vanish exactly at `b=p-1=6`** (`OPT=NC=0` in both cases) — all bit-for-bit matches.
- **The rescoping justification.** Re-traced the dependency as the dispatch requested: in the
  tight case `k=m+1` (Slack Collapse), after a chain-prefix of length `c\in\{0,\dots,m\}`, the
  tail has `p=k-c` elements and remaining budget `m-c=(k-1)-c=(k-c)-1=p-1` **exactly**, for
  every `c` — a clean, re-derived algebraic identity, not hand-waved. Confirmed the actual
  strategy family described in §6 needs `OPT` (the true unrestricted minimum, since Step 2
  explicitly says "take its exact minimum," no non-crossing restriction), not merely `NC`; since
  only `NC` is tractable via the certified Fact-3 recursion, `OPT=NC` at `b=p-1` specifically
  really is the load-bearing target — the rescoping is logically sound, not a cosmetic dodge.

**No overclaim found.** Status section and "Approaches tried" entry both correctly and
repeatedly state the Rescoped Conjecture is "NOT proved."

**Certified:** `lemmas/layer-cake-and-noncrossing-independence.md`.

## 3. `concavity-minimax-duality` — verdict: CHANGES REQUESTED (Status: partial, correctly
self-reported, no overclaim found)

**What was independently re-verified and confirmed correct:**
- **Localization Lemma.** Immediate from the D/M operation definitions; re-derived, correct.
- **Top-Two-Residual-Cancel Lemma.** Independently reconstructed the exact operation sequence
  (cascade to `D_k`, cascade the residual `D_{k-2}` to `\{1\}`, bisect) in exact `Fraction`
  arithmetic for `k=2,\dots,8` — operation count `m-1` and final state
  `(2^k,2^{k-1},\tfrac12,\tfrac12)` matched exactly in all 7 cases.
- **Successor Lemma.** Independently reconstructed (cascade to `D_{j+1}`, successive
  subtraction) for `j=0,\dots,8` — operation count `m-1` and final state `(2^j+1,2^j)` matched
  exactly in all 9 cases.
- **Combined Theorem.** Re-derived the lower-bound induction (using the trailing equal-pair
  cancellation fact, elementary), the trivial upper bound, and the gap-monotonicity induction
  (`2^k\ge k+2` for `k\ge2`) — all correct, no gap.
- **`g^*` candidate.** Independently wrote a separate BFS + exact verification and confirmed
  zero violations of `e_{g^*}(M)\ge1` for `m=1,\dots,4` (my own implementation, different state
  counts than the file's — likely due to different D/M-operation conventions/dedup, but
  qualitatively consistent: zero violations found either way). Given the round's time budget I
  did not reproduce the full `m=5,6` run (326265 states) myself, but the methodology (exact
  `Fraction`, no floats, explicit BFS) is sound and the smaller-scale check is consistent.

**Honesty check (the specific dispatch ask).** Explicitly confirmed the file does **not**
quietly imply `g^*` is established: the Status section, the "Approaches tried" entry, and
§12.6's "Honest status" paragraph all independently and repeatedly state `g^*` is "NOT proved"
/ "not claimed as solved or even as a proven partial result" — consistent everywhere in the
file, no hedge-then-backslide pattern found.

**Certified:** `lemmas/forcing-characterization-dyadic.md`.

## Summary table

| Approach | Verdict | Status | Certified lemmas this round |
|---|---|---|---|
| dyadic-cascade-induction | CHANGES REQUESTED | partial | `shallow-cycle-resolution.md` |
| potential-weighting-upper-bound | CHANGES REQUESTED | partial | `layer-cake-and-noncrossing-independence.md` |
| concavity-minimax-duality | CHANGES REQUESTED | partial | `forcing-characterization-dyadic.md` |

`current.md` updated: Status stays `partial` (theorem not solved — both directions and general
`n` remain open). "Approaches tried," "Current best," and "What remains open" sections all
updated with round-7 content, including the newly-precise mixed-edge-type gap in
dyadic-cascade-induction, the rescoped `OPT(Y,p-1)=NC(Y,p-1)` target in
potential-weighting-upper-bound, and the forcing-characterization limiting result plus open
`g^*` candidate in concavity-minimax-duality.

## Next-round targets (for the outliner)
1. `dyadic-cascade-induction`: attempt to prove (or refute) the mixed-edge-type shallow-cycle
   case directly — reviewer's exhaustive small-`m` search found zero counterexamples, so a
   dominance-style argument analogous to the Cross-Type Cycle Infeasibility Lemma's proof, but
   handling a system with both equality-type and sum-type edges simultaneously, is the concrete
   next target. Separately, the derived-participant case remains open with a demonstrated
   obstruction to the naive extension.
2. `potential-weighting-upper-bound`: attempt `OPT(Y,p-1)=NC(Y,p-1)` directly — the builder's
   own suggestion (exploit that budget `p-1` is one short of Fact 5's full-cancellation
   threshold `p`, an "almost full cancellation" structural argument) is a concrete lead.
3. `concavity-minimax-duality`: attempt to prove `g^*` works for general `m` (inductive
   monovariance argument echoing Superincreasing No-Early-Zero), or find a targeted (not brute
   force) counterexample at `m\ge7` by hand, per the file's own suggestion.
