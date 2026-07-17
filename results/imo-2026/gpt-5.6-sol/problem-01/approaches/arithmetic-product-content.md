## Status
solved

## Approaches tried
- Direct arithmetic invariant/monovariant — live: use a strictly decreasing weighted product for termination and prime-adic column gcds for the terminal value.
- Direct arithmetic invariant/monovariant, completed this round — worked: the positive integer `2^kP` proves termination in every case, while the gcd of each full prime-exponent column determines the unique terminal nonunit.

## Current best
Let the initial entries be `a_1,...,a_2026`. Every maximal sequence of legal moves terminates with exactly one nonunit, and that nonunit is

`M = product_{p in S} p^{d_p},   where   d_p = gcd(v_p(a_1),...,v_p(a_2026))`

and `S` is the finite set of primes dividing the initial product. Thus the terminal value is independent of all choices.

## Full proof
We use the **invariant/monovariant method** from the knowledge base for termination and schedule-independence, together with the knowledge-base technique of **divisor analysis** applied prime by prime.

At any stage, let

- `P` be the product of all 2026 entries on the board, and
- `k` be the number of entries that are greater than `1`.

Thus `P` and `2^kP` are positive integers. We first prove that

`Psi = 2^k P`

strictly decreases after every legal move.

Suppose the two selected entries are `m,n>1`, and put `g=gcd(m,n)`. By the **GCD–LCM Product Identity**,

`gcd(m,n) lcm(m,n)=mn`.

Consequently, the product of the two replacement entries is

`g * (lcm(m,n)/g) = lcm(m,n) = mn/g`.

All unselected entries are unchanged, so the new board product is

`P' = P/g`.

We now give an exhaustive case split.

**Case 1: `g=1`.** The two replacement entries are `1` and `mn`. Since `mn>1`, two nonunit entries have been replaced by exactly one nonunit entry. Hence `k'=k-1`, while `P'=P`. Therefore

`Psi' = 2^{k-1}P = Psi/2 < Psi`.

**Case 2: `g>1` and `m=n`.** Here `g=m=n`, and `lcm(m,n)/g=m/m=1`. Thus the selected pair is replaced by `m,1`; in particular `k'=k-1`. Also `P'=P/g=P/m`. Hence

`Psi' = 2^{k-1}(P/m) = Psi/(2m) < Psi`.

**Case 3: `g>1` and `m!=n`.** The first output `g` is greater than `1`. The second output is also greater than `1`: if `lcm(m,n)/g=1`, then `lcm(m,n)=g`; since both `m` and `n` divide their least common multiple and `g` divides both, this would force `m=g=n`, contrary to `m!=n`. Thus two nonunits are replaced by two nonunits, so `k'=k`. Since `g>=2`,

`Psi' = 2^k(P/g) = Psi/g <= Psi/2 < Psi`.

These three cases are disjoint and cover every legal move. Therefore `Psi` is a strictly decreasing positive-integer monovariant. There cannot be infinitely many moves: after each move its integer value falls by at least `1`, so a play beginning at `Psi_0` has fewer than `Psi_0` moves. Thus every sequence in which Confucius continues whenever a move is possible eventually reaches a state with no legal move.

A state has a legal move whenever at least two of its entries exceed `1`, because any two such entries in different places may be selected. Therefore a terminal state has at most one entry greater than `1`.

It remains both to rule out a terminal board consisting entirely of ones and to determine the possible remaining entry. Let

`S={p : p is prime and p divides a_1a_2...a_2026}`.

This set is finite because the initial product is a fixed positive integer, and it is nonempty because every initial entry is greater than `1`. For `p in S`, define

`d_p = gcd(v_p(a_1),v_p(a_2),...,v_p(a_2026))`,

where zero exponents are included. We use the convention that the gcd of a list of nonnegative integers is nonnegative and is `0` exactly when every member of the list is `0`. Since `p in S`, at least one exponent in its initial column is positive, so `d_p>0`.

We claim that `d_p` is invariant under every move. Fix a prime `p`, and suppose that the selected entries have exponents

`r=v_p(m),   s=v_p(n)`.

The standard prime-valuation formulas for gcd and lcm, consequences of the **Fundamental Theorem of Arithmetic**, give

`v_p(gcd(m,n))=min(r,s)`

and

`v_p(lcm(m,n)/gcd(m,n))=max(r,s)-min(r,s)=|r-s|`.

Thus, in the full `p`-exponent column, the selected pair `(r,s)` is replaced by

`(u,v)=(min(r,s),|r-s|)`.

We first prove the two-coordinate identity

`gcd(r,s)=gcd(u,v)`,

including the possibility that one exponent is zero. If `r>=s`, then `(u,v)=(s,r-s)`. An integer divides both `r` and `s` if and only if it divides both `s` and `r-s`: in one direction it divides the difference `r-s`, and in the other it divides the sum `s+(r-s)=r`. Hence the two pairs have exactly the same common divisors and therefore the same gcd. If `s>=r`, the identical argument with `r` and `s` interchanged compares `(r,s)` with `(r,s-r)`. This proves the identity in all cases, including `r=s` and `r=0` or `s=0`.

We now pass from the selected pair to the whole column. Let `A` be the gcd of the other 2024 exponents in that column. By associativity of gcd,

`gcd(A,r,s)=gcd(A,gcd(r,s))`

and

`gcd(A,u,v)=gcd(A,gcd(u,v))`.

The proved two-coordinate identity makes the right-hand sides equal. Hence replacing the selected entries leaves the gcd of all 2026 exponents unchanged. This proves the claimed invariance of every `d_p`.

Choose any `p in S`. Its invariant exponent-column gcd is the positive integer `d_p`. On a board consisting entirely of ones, however, every `p`-exponent would be zero, and the column gcd would be `0`. Such a board therefore cannot be terminal (indeed, cannot be reached at all). Since we already proved that a terminal board has at most one nonunit, every terminal board has exactly one entry `M>1`. This proves part (a).

We finally identify `M`. At a terminal board the `p`-exponent column is

`(0,...,0,v_p(M),0,...,0)`,

so its gcd is `v_p(M)`. Invariance gives

`v_p(M)=d_p`

for every `p in S`. Moreover, no prime outside `S` can ever appear: initially all its exponents are zero, and the update `(r,s)->(min(r,s),|r-s|)` sends `(0,0)` to `(0,0)`. Hence, by the **Fundamental Theorem of Arithmetic**,

`M = product_{p in S} p^{d_p}`.

The right-hand side depends only on the initial entries, not on any choices made during the process. Therefore the value of `M` is independent of Confucius's choices, proving part (b). ∎

## Promotable lemmas
- **Weighted-product termination lemma.** For this blackboard process, if `P` is the product of all entries and `k` is the number of nonunit entries, then `2^kP` strictly decreases under every legal move. Proved in the first three cases of the Full proof.
- **Prime-column content invariant.** Under a move, for every prime `p` the gcd of the complete column of exponents `v_p` (zeros included) is unchanged. Proved in the valuation portion of the Full proof by showing that `(r,s)` and `(min(r,s),|r-s|)` have the same common divisors and then adjoining the unaffected coordinates.
