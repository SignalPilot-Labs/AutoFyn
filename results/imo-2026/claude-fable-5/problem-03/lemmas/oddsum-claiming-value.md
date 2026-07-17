# Lemma: oddsum value of the alternating-claiming game

**Certified** by proof-reviewer, round 1 (source: approaches/pairing-exchange-normal-form.md, Section 1, "Lemma 0").

## Statement
Let M = {a_1 >= a_2 >= ... >= a_N} be a finite multiset of nonnegative reals. In the game where two players alternately claim elements of M (first mover first), each maximizing the sum of his claimed elements, the first mover can guarantee himself at least oddsum(M) = a_1 + a_3 + a_5 + ..., and the second player can guarantee the first mover gets at most oddsum(M). Hence the game value is exactly oddsum(M) = (sigma(M) + A(M))/2, where A(M) = a_1 - a_2 + a_3 - ... is the alternating sum.

## Proof
Backward induction on |M| with V(M) = max_x [x + sigma(M\x) - V(M\x)]: both guarantee directions (i)/(ii) follow from the induction hypothesis with roles swapped. Then V(M) = oddsum(M) by the rank computation: claiming a_i yields P(a_i) = a_i + evensum(M\a_i) with evensum(M\a_i) = sum_{j<i even} a_j + sum_{j>i odd} a_j, and oddsum(M) - P(a_i) telescopes into a sum of nonnegative differences for both parities of i, so the max is at a_1 and equals oddsum(M). Full details in the source file, Section 1.

## Reviewer verification
Re-derived by hand; confirmed against exact minimax on 200 random multisets (|M| <= 7), agreement to 1e-12.
