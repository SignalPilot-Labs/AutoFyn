# Lemma: multiset-gcd-invariance

**Status: certified (proof-reviewer, round 1).** Proved in full in `approaches/prime-gcd-invariant.md`, Setup ((★), (G1), (G2)) and Step 5 (Lemmas 6–7 there). Statement checked against the proof — no overclaim; invariance re-derived independently and verified on 25,000 random moves (0 violations).

## Statement

For a finite multiset S of nonnegative integers, define gcd(S) as the unique d ≥ 0 such that for every integer e ≥ 1: (e | s for all s ∈ S) ⟺ e | d. (Exists and is unique; conventions gcd(a, 0) = a, gcd(0, …, 0) = 0.)

1. **(Zeros are inert.)** Adding or removing entries equal to 0 does not change gcd(S); in particular gcd(a, 0, …, 0) = a for a ≥ 0.
2. **(Fold rule.)** For any finite multiset R of nonnegative integers and a, b ≥ 0: gcd(R ∪ {a, b}) = gcd(R ∪ {gcd(a, b)}).
3. **(Subtractive Euclid identity with zero cases.)** For all integers a, b ≥ 0: gcd(a, b) = gcd(min(a,b), |a − b|).
4. **(Invariance under the blackboard move.)** Consequently, for a board of positive integers and each prime p, the quantity g_p = gcd of the multiset of p-exponents of all entries is unchanged by every move (m, n) → (gcd(m,n), lcm(m,n)/gcd(m,n)): the exponent multiset changes from R ∪ {a, b} to R ∪ {min(a,b), |a − b|}, and by 2. and 3. these have equal gcd. This is an identity for every prime under each single global move; no per-prime legality is involved.

## Where proved

`results/imo-2026-01/approaches/prime-gcd-invariant.md`: Setup (existence/uniqueness of gcd via (★), facts (G1), (G2)), Lemma 6 (part 3), Lemma 7 (part 4). Part 4 also uses the valuation formulas of the proposed lemma `move-anatomy.md`.
