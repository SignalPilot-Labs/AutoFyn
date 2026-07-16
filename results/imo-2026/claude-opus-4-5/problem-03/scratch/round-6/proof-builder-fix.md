# Proof Builder Fix Report: Round 6

## Approach: geometric-direct

## Issues Addressed

The proof-reviewer identified three critical errors in the n=4 Case B proof:

1. **Strategy B construction was WRONG** - it created only 2 pairs, not 3, so the Singleton-Pair Formula didn't apply.
2. **3-mark constructions are insufficient** - for some configs in B/PP range, XY needs 4 marks.
3. **Strategy PP had no explicit construction**.

## What Was Correct (Preserved)

- Sum constraint: 4*alpha + 3*beta + 2*gamma + eta < 5
- Case A constraint: 6*alpha + 4*beta < 2, hence alpha < 1/3
- Gap-width: alpha - 1 < -2/3 < 0 (S5 and B intervals overlap)
- Interval coverage logic is sound
- S5 construction works for its range
- S6 construction works for its range

## Changes Made

### 1. Removed incorrect 3-mark Strategy B construction

The original construction that attempted to create 3 pairs from cutting P_4 and P_5 was removed. It created only 2 pairs, which doesn't give the Singleton-Pair Formula structure.

### 2. Added 4-Pair + 1-Singleton Formula

For n=4 with 4 marks, XY creates 9 pieces. If 4 exact pairs + 1 singleton s:
- LB = (1 - s)/2 + s = 1/2 + s/2
- For LB <= c(4), need s <= L_0

### 3. Updated Strategy B and PP descriptions

The B and PP ranges now correctly state:
- These require 4-mark strategies (not 3-mark)
- The constructions are computationally verified (0/100k failures)
- Explicit algebraic constructions are pending

### 4. Updated Status

Changed from claiming n=4 is "PROVED" to honest "PARTIAL" status:
- Interval coverage framework: PROVED
- S5, S6, S4 explicit constructions: COMPLETE
- B and PP ranges: COMPUTATIONALLY VERIFIED, explicit constructions pending

## Remaining Gap

The proof needs explicit 4-mark XY strategy constructions for the B and PP interval ranges (eta > alpha + beta + 2). The computational verification confirms such strategies exist, but the algebraic characterization is non-trivial because:

1. Creating 4 exact pairs from 5 arbitrary pieces requires matching cuts
2. The singleton needs to be <= L_0, which must come from a difference (not an original piece, since P_1 > L_0 in Case B)
3. Different configurations may require different cut patterns

## Current Status

**Status:** partial

**Complete for:** n = 1, 2, 3

**Partial for n = 4:**
- Lower bound: Complete
- Upper bound Case A (P_1 <= L_0): Complete  
- Upper bound Case B Non-Case-A: Complete (S6, S4 explicit)
- Upper bound Case B Case A with S5: Complete (eta in [beta+1, alpha+beta+2])
- Upper bound Case B Case A with B/PP: Computationally verified, explicit construction pending

**Open for:** n >= 5

## Output

File updated: `/home/agentuser/repo/results/imo-2026-03/approaches/geometric-direct.md`

Status: `partial` (complete proof for n = 1, 2, 3; partial for n = 4 with explicit construction gap)
