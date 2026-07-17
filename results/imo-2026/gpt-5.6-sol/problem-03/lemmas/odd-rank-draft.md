# Odd-rank draft lemma

## Statement
Let fixed pieces have nonincreasing values \(x_1\ge\cdots\ge x_q>0\). Two players alternately claim one remaining piece, with the first player moving first and each maximizing their own total. Then taking a longest remaining piece is optimal at every turn, and the first player's value is
\[
x_1+x_3+x_5+\cdots.
\]
This remains true when values are tied.

## Proof
Use induction on \(q\). The assertion is immediate for one piece. Assume it for every shorter list. If the current player chooses \(x_i\), the induction hypothesis determines the opponent's value from the list with \(x_i\) deleted. Compare the current player's resulting value with \(O=x_1+x_3+x_5+\cdots\), the value obtained by first choosing \(x_1\).

When \(i\) is odd, the loss relative to \(O\) is
\[
(x_1-x_2)+(x_3-x_4)+\cdots+(x_{i-2}-x_{i-1}),
\]
and when \(i\) is even it is
\[
(x_1-x_2)+(x_3-x_4)+\cdots+(x_{i-1}-x_i).
\]
Every term is nonnegative. Hence choosing \(x_1\) is optimal and yields \(O\), completing the induction. Equalities among lengths merely make some displayed differences zero. ∎
