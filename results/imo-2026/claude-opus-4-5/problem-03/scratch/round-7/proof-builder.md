# Proof Builder Report: Round 7

## Approach: geometric-direct

### Summary of Changes

**Status: partial (n=1,2,3,4 COMPLETE; n>=5 OPEN)**

The Round 6 gap "B and PP require 4-mark constructions" was **false** — it was caused by a parameterization mismatch in the verification code. The explorer proved that B and PP use the **same 3-mark construction** as the other strategies.

### Changes Made

1. **Replaced the incorrect B/PP section (lines 655-673)** with the verified 3-mark unified "BPP" construction:
   - Cut P_4 at position P_3 from left -> pair {P_3, P_3}
   - Cut d_3 at position P_1 from left -> pair {P_1, P_1}  
   - Halve P_5 -> pair {P_5/2, P_5/2}
   - Singletons: {P_2, d_3-P_1}
   - LB = 1/2 + |P_1+P_2-d_3|/2

2. **Added algebraic proof for PP range bound:**
   - In PP range, singleton diff = (eta-2-2*alpha-beta)*L_0
   - Need eta - 2 - 2*alpha - beta < 1 for all valid PP configs
   - Since eta < eta_max = 3-6*alpha-4*beta (using gamma >= alpha+1):
     - eta_max - (2+2*alpha+beta) = 1-8*alpha-5*beta < 1
   - Hence LB < c(4) in PP range

3. **Merged B and PP into unified "BPP" strategy** — the absolute value |P_1+P_2-d_3| handles both B range (d_3 < P_1+P_2) and PP range (d_3 > P_1+P_2)

4. **Deleted all "4 marks" and "4-Pair + 1-Singleton" language** — replaced with "3 marks" and "3-Pair + 2-Singleton"

5. **Updated n=4 Case B status from "PARTIAL" to "PROVED"**

6. **Updated conclusion** to reflect n=1,2,3,4 COMPLETE

### Files Modified

- `/home/agentuser/repo/results/imo-2026-03/approaches/geometric-direct.md`

### Proof Structure

The n=4 Case B proof now consists of four strategies (all using 3 XY marks):
- **S6**: covers |gamma - alpha| <= 1 (d_2 close to P_1)
- **S4**: covers |eta - beta| <= 1 (d_3 close to d_1)
- **S5**: covers |eta - (alpha+beta+1)| <= 1 (d_3 close to P_2)
- **BPP**: covers eta in [1+2*alpha+beta, eta_max) (d_3 close to P_1+P_2)

Gap width between S5 and BPP = alpha - 1 < -2/3 < 0, so they overlap with no gap.

### Remaining Gap

**n >= 5**: Computationally verified (0/200k failures) but algebraic proof requires generalizing the interval coverage argument to arbitrary n. The approach generalizes — each additional n adds more singleton-pair comparison strategies — but the explicit construction of all necessary strategies is not yet done.

### New Promotable Lemmas

1. **BPP Unified Construction**: The 3-mark construction gives LB = 1/2 + |P_1+P_2-d_3|/2
2. **BPP Range Bound**: In [1+2*alpha+beta, eta_max), singleton difference < 1, hence LB <= c(4)
