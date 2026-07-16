# Halve-All Strategy Lemma (Case A)

## Statement

For any n >= 1 and LB configuration P_1 <= P_2 <= ... <= P_{n+1} with sum 1, if P_1 <= L_0 = 1/(2^{n+1}-1), then XY has a strategy limiting LB to at most c(n) = 2^n/(2^{n+1}-1).

## Proof

**XY's Strategy:** Use exactly n marks to halve each of P_2, P_3, ..., P_{n+1} (one mark per piece, n marks total).

**Resulting pieces:** {P_1, P_2/2, P_2/2, P_3/2, P_3/2, ..., P_{n+1}/2, P_{n+1}/2}.

This is the singleton P_1 plus n pairs: {P_2/2, P_2/2}, {P_3/2, P_3/2}, ..., {P_{n+1}/2, P_{n+1}/2}.

**Total pieces:** 1 + 2n = 2n+1 pieces. LB picks ceil((2n+1)/2) = n+1 pieces.

**Step 1: Apply Pairing Cancellation n times.**

By the Pairing Cancellation Lemma applied to each pair:

lb_score({P_1, P_2/2, P_2/2, ..., P_{n+1}/2, P_{n+1}/2})
= lb_score({P_1}) + P_2/2 + P_3/2 + ... + P_{n+1}/2
= P_1 + (P_2 + P_3 + ... + P_{n+1})/2

**Step 2: Simplify.**

P_2 + P_3 + ... + P_{n+1} = 1 - P_1.

Therefore:
LB = P_1 + (1 - P_1)/2 = P_1 + 1/2 - P_1/2 = 1/2 + P_1/2.

**Step 3: Verify LB <= c(n).**

LB = 1/2 + P_1/2 <= c(n) if and only if P_1 <= 2c(n) - 1.

We have 2c(n) - 1 = 2 * 2^n/(2^{n+1}-1) - 1 = (2^{n+1} - (2^{n+1}-1))/(2^{n+1}-1) = 1/(2^{n+1}-1) = L_0.

Since P_1 <= L_0 by assumption, LB <= c(n). QED.

## Certified

This lemma is certified by the proof-reviewer (Round 5). Independently verified computationally for n=1 to 5 with multiple configurations.
