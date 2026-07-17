# Outline Review: IMO 2026 P3, Round 2

## Critical Finding

**induction-on-n already claims Status `solved`** in its approach file. The proof includes a complete upper bound via saddle-point verification: (geometric, copy) is a saddle point, and the file contains a detailed n=2 worked example verifying that XY's optimal response to non-geometric markings limits LB to below c(n). This needs proof-reviewer verification before any further building.

---

## Approach Reviews

### induction-on-n (Status: solved in file)

**Verdict: APPROVE (pending proof-reviewer verification)**

The approach file claims a complete proof:
1. Lower bound via geometric marking: proven.
2. Upper bound via saddle point: (geometric, copy) is shown to be a saddle point. The key insight is that XY's response to non-geometric LB marking can limit LB to strictly below c(n). The n=2 example (LB marks 1/4, 1/4, 1/2; XY responds by splitting 1/2 into three near-equal pieces) demonstrates XY can push LB arbitrarily close to 1/2 < 4/7.

Sanity check passed: Numerical verification confirms that against 1/4, 1/4, 1/2, XY splitting the 1/2 piece into a, b, c with b close to 1/4 yields LB share approaching 1/2 < c(2).

**Issues to verify in proof-review:**
- The saddle-point argument for general n (not just n=2)
- The claim that copy strategy is XY-optimal against geometric marking (Lemma 2 proof sketch)
- Completeness of the case analysis in the upper bound

---

### geometric-dominance (Status: partial, action: revise)

**Verdict: CHANGES REQUESTED**

Good structure with pigeonhole + pair-cancellation lemmas. Cases k=1, k=2, k=n+1 are complete. The gap is cases k=3,...,n for n >= 3.

**Specific issues:**
1. **Gap k=3,...,n:** The naive strategy fails (alternating sum can exceed t_n). The outline notes "Needed: A different XY strategy" but provides no mechanism.
2. **Redundancy with induction-on-n:** If induction-on-n is truly solved via saddle point, geometric-dominance's explicit case analysis is superseded. However, if the saddle-point argument has a hole, the explicit casework approach is the backup.

**Changes needed:** Either close the k=3,...,n gap with an explicit XY strategy, or prove that when k in {3,...,n} holds, one of k=1, k=2, or k=n+1 also holds (reducing to handled cases).

---

### ratio-based-induction (Status: partial, action: new)

**Verdict: CHANGES REQUESTED**

The n=1 proof is clean and complete. The inductive step has gaps.

**Specific issues:**
1. **Sorted order after first XY move:** The proof does not rigorously handle how halved/cloned pieces interleave with residual pieces.
2. **Residual IH verification:** For r>2 case, must show a_1 <= S' * t_{n-1}. This is not proven.
3. **Combining A contributions:** The claim that "total A = A' since pair contributes 0" requires the pair to occupy consecutive sorted positions, which is not guaranteed.

**Changes needed:** Either fix the inductive argument with rigorous sorted-order tracking, or reframe as an explicit strategy that avoids the interleaving complexity.

---

### exchange-argument (Status: new)

**Verdict: CHANGES REQUESTED**

Interesting variational framing: prove geometric marking is uniquely LB-optimal (a local and global maximum of V(L) = min_X G(L,X)).

**Specific issues:**
1. **No mechanism for V(L) < c(n) when L is not geometric:** The outline states "XY halves if ratio > 2, exploits slack if ratio < 2" but does not prove V(L) is strictly below c(n).
2. **Continuity/critical point argument not developed:** Claims geometric is a critical point but no derivative or perturbation analysis.
3. **Risk of circularity:** Proving "geometric is optimal" requires showing V(L) < c(n) for ALL other L, which is the same upper bound problem.

**Changes needed:** Either develop a rigorous variational argument (gradient of V, second derivative test), or acknowledge this reduces to the same problem as the other approaches.

---

### pairing-interleave (stale)

**Verdict: RETHINK**

Superseded by the cleaner pigeonhole/pair-cancellation structure in geometric-dominance. Should be marked stale and not built.

---

## Diversity Assessment

**Warning: Field collapse detected.** All four live approaches share the same core structure:
- LB's geometric marking achieves c(n)
- Upper bound requires showing XY limits ANY LB marking to c(n)

The approaches differ only in technique (casework vs induction vs variational), not in framing. They all hit the same wall: proving XY can handle non-geometric LB markings.

**However:** The induction-on-n saddle-point argument may actually close this shared gap. If it passes proof-review, the problem is solved. If not, the field needs a genuinely different framing (e.g., game tree minimax, potential function, LP duality).

---

## Rankings (Elo updated)

| Rank | Slug | Elo | Status |
|------|------|-----|--------|
| 1 | induction-on-n | 1574 | claims solved |
| 2 | geometric-dominance | 1540 | partial, gap k=3...n |
| 3 | ratio-based-induction | 1500 | partial, inductive gaps |
| 4 | exchange-argument | 1470 | partial, not developed |
| 5 | pairing-interleave | 1415 | stale |

---

## Build Set Decision

**Priority 1:** Verify induction-on-n with the proof-reviewer. If it passes, the problem is solved.

**Priority 2:** If induction-on-n fails review, advance geometric-dominance (most complete structure for the explicit casework approach).

**This round:** Build induction-on-n only (for verification). The other approaches need not be built until we know whether the claimed solution holds.

build set: induction-on-n
