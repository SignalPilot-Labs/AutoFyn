# Lemma: Partition Lemma (alternating sum = min pairing-partition cost)

**Certified** by proof-reviewer, round 1 (source: approaches/pairing-exchange-normal-form.md, Section 2, Lemmas 1-4).

## Statement
For a finite multiset M of nonnegative reals with alternating sum A(M) = a_1 - a_2 + a_3 - ... (decreasing order), and any partition Pi of M into pairs {a,b} and singletons {c}, define cost(Pi) = sum_pairs |a-b| + sum_singletons c. Then

  A(M) <= cost(Pi) for every such Pi, with equality for the adjacent pairing {a_1,a_2},{a_3,a_4},...

Hence A(M) = min_Pi cost(Pi).

## Proof
Peeling: removing a singleton x changes A by at most +x (Lemma 2: sign-flip of the tail, 0 <= T <= a_{i+1}); removing a pair x >= y changes A by at most x - y (Lemma 3: four parity cases via facts F1-F3 about alternating sums of decreasing blocks). Peel all blocks of Pi to reach A(empty) = 0; the accumulated bound is cost(Pi). Equality for the adjacent pairing is definitional. Full parity casework in the source file, Section 2.

## Reviewer verification
All four parity cases of Lemma 3 (including the c = 0 subcase) re-derived by hand from the sign-flip formulas; bound never violated across the round's numerical simulations.
