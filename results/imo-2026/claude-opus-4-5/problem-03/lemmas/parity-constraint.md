# Parity Constraint Lemma

## Statement

In the stick-cutting game:
- If LB uses exactly n marks (creating n+1 pieces) and XY uses j marks (0 <= j <= n), the total number of pieces is n+1+j.
- LB picks ceil((n+1+j)/2) pieces and XY picks floor((n+1+j)/2) pieces.
- If j = n-1: total = 2n pieces (even). Both pick n pieces.
- If j = n: total = 2n+1 pieces (odd). LB picks n+1, XY picks n.

**Consequence:** XY prefers j <= n-1 to avoid giving LB an extra pick.

## Proof

The number of pieces equals (LB marks) + (XY marks) + 1 = n + j + 1.

In alternating selection with LB going first, LB picks the pieces at positions 1, 3, 5, ... (odd positions). If the total number of pieces is m:
- LB picks ceil(m/2) pieces
- XY picks floor(m/2) pieces

When m is odd, LB gets one more piece than XY. Therefore XY prefers to make m even by using j = n-1 marks (if possible), giving m = 2n pieces. QED.

## Certified

This lemma is certified by the proof-reviewer (Round 2). Direct counting argument.
