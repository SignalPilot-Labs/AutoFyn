# Pair-pile construction — Xiang caps the dyadic config at f(n), all n ≥ 1

**Statement.** Against Liu's dyadic config — pieces `(1, 2, 4, …, 2^n) / D(n)`
where `D(n) = 2^{n+1} − 1`, i.e. Liu's n marks at cumulative sums of
`(1, 2, 4, …, 2^{n−1})/D(n)` — Xiang has a response using **≤ n marks** that
forces the final sorted multiset into the **pair-pile**

`2^{n−1}, 2^{n−1}, 2^{n−2}, 2^{n−2}, …, 4, 4, 3, 2, 1, 1`  (all over `D(n)`),

whose alternating advantage sum is `A = 1/D(n)`, hence (by Lemma G's parity
identity `Liu = (1+A)/2`) Liu's payoff is exactly

`Liu = (1 + 1/D(n))/2 = (D(n)+1)/(2 D(n)) = 2^{n+1}/(2 D(n)) = 2^n / D(n) = f(n)`.

This certifies that the dyadic config's value is **at most** `f(n)` for every
n ≥ 1. Combined with a matching lower bound (Lemma L: `S_odd ≥ f(n)` for every
Xiang response on the dyadic config — open for general n), it pins the dyadic
value to exactly `f(n)` and gives `c(n) ≥ f(n)`.

**Construction (uses n−1 marks for n ≥ 2; 1 mark for n = 1).**
For n ≥ 2, Xiang places one mark inside each of Liu's pieces of size `2^k/D`
for `k = 2, 3, …, n` (that is n−1 pieces, hence n−1 ≤ n marks), splitting:
- piece `2^2 = 4` (over D) into `(1, 3)` (mark at distance `1/D` from its left end),
- piece `2^k` (over D), `k ≥ 3`, into `(2^{k−1}, 2^{k−1})` (mark at its midpoint),

and leaving Liu's pieces `1` and `2` (over D) untouched. The marks lie inside
Liu's pieces, hence are distinct from Liu's marks and from each other. Number
of marks `= n − 1 ≤ n`. ✓ For n = 1: Xiang bisects Liu's single piece `2/D(1) = 2/3`
into `(1, 1)` over `D(1) = 3` (one mark), giving the pair-pile `1, 1, 1` over 3.

**Total check.** The final pieces (over `D(n)`) are `1, 2, (1, 3), (2, 4, 4), …,
(2^{n−1}, 2^{n−1})` — i.e. `1, 2, 1, 3, 4, 4, 8, 8, …, 2^{n−1}, 2^{n−1}`, summing
to `1 + 2 + (1+3) + Σ_{k=3}^{n} 2^k = 7 + (2^{n+1} − 8) = 2^{n+1} − 1 = D(n)`. ✓

**Excess check.** Sorted descending, the multiset is the pair-pile
`2^{n−1}, 2^{n−1}, 2^{n−2}, 2^{n−2}, …, 4, 4, 3, 2, 1, 1`. Consecutive sorted
pairs are `(2^{n−1}, 2^{n−1}), (2^{n−2}, 2^{n−2}), …, (4, 4), (3, 2), (1, 1)`.
Each pair's excess `p_{2k−1} − p_{2k}` is `0` except the `(3, 2)` pair which has
excess `1`. So `A = 1` (over `D(n)`, `A = 1/D(n)`), and
`Liu = (1 + 1/D(n))/2 = f(n)`. ✓

**Verification.** Exact rational arithmetic for n = 2, 3, 4, 5: piece-sum = D(n),
A = 1, oddsum = 2^n in every case (matching f(n)).

**Knowledge-base tools.** Constructive / incremental (explicit mark placement);
Invariants & monovariants (the pair-excess A is the controlled invariant).

**Where proved.** `approaches/pairing-partner.md`, "Pair-pile construction."
