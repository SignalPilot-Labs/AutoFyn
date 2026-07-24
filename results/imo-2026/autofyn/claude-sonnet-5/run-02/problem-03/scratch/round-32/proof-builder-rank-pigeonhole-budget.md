# Build report: rank-pigeonhole-budget, round 32

## Summary
File updated: `/home/agentuser/repo/results/imo-2026-03/approaches/rank-pigeonhole-budget.md`
(new §7.19; Open-gaps addendum; Promotable lemmas (round 32); Approaches-tried entry).

## Part (a) — done exactly as dispatched
Wrote up MaxCeil(5)'s top-untouched branch as a one-paragraph free corollary
(§7.19.1) of the certified §7.10.4 reduction + §7.11 Index-Chain Identity +
round-31's full closure of (star_3)=MinFloor(4). Resolves (7.9.1)'s
top-untouched branch unconditionally at n=8.

## Part (b) — achieved more than dispatched
Instead of just enumerating shapes for the sigma_2-touched residual, found
and proved two new fully general lemmas:
- **Max Bound**: A(S) <= max(S) for any finite nonnegative multiset.
- **Insertion Sandwich**: |A(T u {a}) - A(T)| <= a.
Both proved from scratch (rank-shift/parity case split using only Fact 1 +
sharp-dominant-removal-identity) and independently verified by 200,000-trial
exact-Fraction search each, zero violations.

Combined these into a **Master Theorem**: MinFloor(m-1) = (star_{m-2})
implies MaxCeil(m) in full (both top-untouched and top-cut branches, every
shape, one unified 2-case argument on the largest fragment of sigma_1's
split vs sigma_2) -- explicitly NOT the two-peel+Fact-2 route the Necessity
Theorem (Sec 7.15) proved insufficient; this mechanism uses MinFloor(m-1)'s
lower bound directly plus Insertion Sandwich to absorb sigma_1's other
fragments, genuinely different.

Instantiated at m=5 using the now-certified (star_3): **MaxCeil(5) is
closed unconditionally, in full**, hence (7.9.1) at n=8 -- one level past
round 26's n<=7. This supersedes needing a separate shape census of the
sigma_2-touched residual (the dispatch's step 3) since the Master Theorem
covers every shape at once.

Sanity-checked numerically at sigma=(16,8,4,2,1) over 250,000 random and
targeted-adversarial legal <=3-cut configurations: max A found ~14.997,
never exceeding 15 = sigma_1-sigma_5, consistent throughout.

## Honest scope / what's NOT closed
- The Master Theorem is conditional in general: MaxCeil(m) for m>=6 needs
  (star_4), not yet certified -- not claimed closed.
- The general-n pattern (all (star_k), k>=3) remains exactly as open as
  before this round; only k=3 (hence m=5, n=8) is newly unconditional.
- Claim (A) (this approach's own already-`solved` target) is unaffected --
  this round's work is additional side-progress on the shared
  MaxCeil/MinFloor obstruction, not a change to Claim (A)'s status.

## Status
Approach file's Status remains `solved` (scoped explicitly to Claim (A),
unchanged since round 8). This round's new §7.19 material is recorded
under Open gaps / Approaches tried / Promotable lemmas as additional,
honestly-scoped progress on the shared MaxCeil/MinFloor family, not as a
change to the whole-problem status (which remains `partial` per
`current.md`).

## Promotable lemmas proposed this round
- `max-bound-fact` (Max Bound, A(S) <= max(S))
- `insertion-sandwich-lemma` (|A(T u {a}) - A(T)| <= a)
- `maxceil-master-theorem` (MinFloor(m-1) => MaxCeil(m) in full, conditional)
- Corollary: MaxCeil(5) full unconditional closure (usable directly by
  `greedy-halving-adversary`'s h(5) c=x vertex, per round-32 outline's
  cross-reference)
