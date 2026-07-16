# V_j Strategy for n=5

## Statement

For n=5 with 6 pieces P_1 <= P_2 <= ... <= P_6 and differences d_j = P_{j+1} - P_j for j=1,...,5:

If d_j <= L_0 = 1/63 for some j in {1,2,3,4,5}, then XY can limit LB's score to at most c(5) = 32/63 using 4 marks.

## Proof

XY halves all pieces except P_j and P_{j+1}. This uses exactly 4 marks (on pieces P_i for i not in {j, j+1}).

**Piece structure:** After 4 marks on 6 pieces, total pieces = 6 + 4 = 10.
- 4 pairs: {P_i/2, P_i/2} for each i not in {j, j+1}
- 2 singletons: {P_j, P_{j+1}}

**LB score calculation:** By Pairing Cancellation Lemma (certified), for each pair {v, v}, LB gets exactly v from that pair. Thus:

LB = sum(P_i/2 for i not in {j, j+1}) + lb_score({P_j, P_{j+1}})

Since lb_score of two singletons {a, b} with a <= b is b:

LB = (sum of all pieces - P_j - P_{j+1})/2 + P_{j+1}
   = (1 - P_j - P_{j+1})/2 + P_{j+1}
   = 1/2 - P_j/2 - P_{j+1}/2 + P_{j+1}
   = 1/2 + (P_{j+1} - P_j)/2
   = 1/2 + d_j/2

**Bound:** Since d_j <= L_0 = 1/63:

LB = 1/2 + d_j/2 <= 1/2 + L_0/2 = 1/2 + 1/126 = 64/126 = 32/63 = c(5). QED.

## Verification

- L_0 = 1/63 verified
- c(5) = 32/63 verified
- 2*c(5) - 1 = 64/63 - 1 = 1/63 = L_0 verified
- 1/2 + L_0/2 = 1/2 + 1/126 = 63/126 + 1/126 = 64/126 = 32/63 = c(5) verified

## Certified

Round 12, proof-reviewer.
