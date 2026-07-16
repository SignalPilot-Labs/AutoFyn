# Geometric Dominance Lemma

## Statement

For the geometric configuration L_k = 2^k/D where D = 2^{n+1}-1 and k = 0, 1, ..., n:

L_n > L_0 + L_1 + ... + L_{n-1}

## Proof

The sum L_0 + L_1 + ... + L_{n-1} equals:
(1 + 2 + 4 + ... + 2^{n-1}) / D = (2^n - 1) / D

Meanwhile, L_n = 2^n / D.

Since 2^n > 2^n - 1, we have L_n > L_0 + L_1 + ... + L_{n-1}. QED.

## Certified

This lemma is certified by the proof-reviewer (Round 2). The proof is a direct computation of the geometric sum.
