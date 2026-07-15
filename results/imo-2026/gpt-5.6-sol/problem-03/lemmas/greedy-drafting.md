# Greedy drafting lemma

## Statement
For a finite multiset \(b_1\ge\cdots\ge b_m\ge0\), the first player's value in alternating take-one drafting is \(b_1+b_3+b_5+\cdots\); ties do not change the value.

## Certified proof
Induct on \(m\). Taking \(b_1\) leaves the opponent a position whose inductive value is \(b_2+b_4+\cdots\), so the first player obtains the odd-ranked sum. If instead the first move removes \(b_j\), the opponent's odd-ranked sum in the remaining sorted list is at least \(b_2+b_4+\cdots\), by pairing each earlier odd rank \(b_{2i-1}\) against \(b_{2i}\); the unchanged tail contributes the even-ranked terms directly. Therefore no first move yields more. All inequalities are non-strict, so ties cause no problem. ∎
