# proof-builder report — scalar-difference-pigeonhole — round 6

Wrote to `results/imo-2026-06/approaches/scalar-difference-pigeonhole.md` (partial, unchanged status).

## What was done

Per the outline-reviewer's mandatory fix, resolved Step 0 of the Morse-Hedlund
subword-complexity reformulation (the "sums-vs-factors collision gap") as a
required first deliverable before attempting to sharpen the complexity bound.

**Result: the naive Complexity Bound Lemma proposed in the round-6 outline is
FALSE as a bound on the factor-complexity function p(k).** Proved this two ways:

1. Abstractly (Claim 6.1.1): the window-sum map on the alphabet {2,...,R}^k is
   not injective for k≥2, R≥4 (explicit witness: (2,4,2,...,2) vs (3,3,2,...,2)).
2. Concretely, with a genuine witness inside a real instance (Claim 6.1.2,
   independently re-verified by direct simulation): for a1=35, the two distinct
   length-2 factors (d_8,d_9)=(5,4) and (d_16,d_17)=(4,5) both occur in the true
   greedy sequence and both sum to 9 — so counting distinct window sums (Lemma 1,
   already certified) does not bound the number of distinct factors p(k); it
   bounds a strictly smaller, different quantity.

This settles the mandatory Step 0 negatively: the proposed sum-counting route to
p(k) cannot be patched, since the failure is genuine non-injectivity on realized
inputs, not a looseness in the counting.

Beyond Step 0, established (all fully proved, all new this round):
- Lemma 6.0.1: p(k) is non-decreasing (standard "drop-last-symbol" surjection
  argument, proved from scratch).
- Lemma 6.2.1: the only valid unconditional bound is the useless trivial
  exponential one, p(k) ≤ (R-1)^k.
- Theorem 6.2.2 (conditional on the population's still-open central Unified
  Central Claim): if a finite self-sufficient Q exists, then (d_n) is *purely*
  periodic from n=1 (no transient), and p(k) ≤ T = |GoodRes(Q)| for every k —
  a new, free, exact corollary chaining the already-certified
  transient-free-finishing-theorem.md with elementary factor-counting.
- A precise, honest account (§6.3) of why the converse direction (bounded p(k)
  ⟹ the IMO's no-transient conclusion) needs two separate hurdles beyond
  Morse-Hedlund itself: (i) Morse-Hedlund only gives *eventual* periodicity,
  not periodicity "for every n" as the problem literally requires; (ii) no
  transient-removal argument is known outside the Q-machinery this
  reformulation was meant to route around.
- A sanity check (§6.4) against the known-solved even-seed case (p(k)≡1,
  matching Theorem 6.2.2 with T=1 exactly) and honest numerical evidence
  (§6.5, not used as a proof step) that p(k) empirically stabilizes for
  larger k on non-even seeds (a1=35 stabilizes at 34 by k=10; a1=99 at 72 by
  k=40).

## Honest conclusion

The Morse-Hedlund reformulation is a legitimate, precisely stated equivalent
vocabulary (with one new free certified conditional corollary, Theorem 6.2.2),
but this round's work shows it currently offers **no new leverage** over the
population's existing Q/Nec central existence gap — the one concrete mechanism
proposed to attack it (window-sum counting) is proved invalid, and even a
hypothetical future proof of "p(k) bounded" would still leave the no-transient
upgrade open. Central existence gap is untouched. Status remains `partial`,
recorded honestly with no overclaiming.

## Promotable lemmas (new this round, ready for reviewer certification)

- Lemma 6.0.1 (factor complexity non-decreasing) — general combinatorics-on-words fact.
- Corollary 6.1.3 (window-sum counting does not bound factor complexity) — negative result, reusable caution.
- Theorem 6.2.2 (central claim ⟹ exact factor-complexity bound p(k) ≤ T) — conditional, reusable.

All in `results/imo-2026-06/approaches/scalar-difference-pigeonhole.md` §6.0–6.2 and the Promotable lemmas section.

Relevant paths:
- `/home/agentuser/repo/results/imo-2026-06/approaches/scalar-difference-pigeonhole.md` (updated)
- `/home/agentuser/repo/results/imo-2026-06/current.md` (read, not modified)
- `/home/agentuser/repo/results/imo-2026-06/lemmas/transient-free-finishing-theorem.md`,
  `periodicity-of-residue-class-union.md`, `minimum-gap-lemma.md` (imported, not modified)
