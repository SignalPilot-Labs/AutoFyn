# Build report — confined-competitor-construction (round 10)

## What was done
Built out the round-10 outline for `confined-competitor-construction` (a
constructive-competitor + greedy-minimality-contradiction mechanism aimed at Joint
Cofinite FAH, the sole remaining crux of the whole problem). Carried the outline's
Steps 1–4 to a complete conclusion.

## Result: decisive negative, not a re-run of Lemma K's inconclusive stall
Proved a new, fully general, unconditional theorem — the **Minimality Tautology
Lemma**: for any n≥2, any integer c with a_{n-1}<c and gcd(c,a_i)>1 for all i<n
automatically satisfies c ≥ a_n. This is a one-line consequence of the problem's own
greedy definition (a_n is the MINIMUM legal candidate), with no dependence on any
certified lemma or open hypothesis.

Applying this to the outline's specific candidate `c` (smallest multiple of q*
exceeding a_{n_j-1}) shows the outline's central "Step 2/3" mechanism cannot ever
reach a contradiction: whenever c<a_{n_j} (the only case that would matter), c is
*provably* illegal against some earlier term — not an open question a cleverer
construction or the Confined-GCD Lemma could resolve, but a forced fact. When
c>a_{n_j}, the construction is simply vacuous. Either way Step 3 is unreachable, for
this or ANY refinement of the competitor construction.

This is a sharper conclusion than "fails the same way as Lemma K": it shows the
entire *family* of constructive-smaller-competitor mechanisms (Lemma F, Lemma K, and
this round's attempt) is subject to one forced obstruction, intrinsic to the
sequence's definition — not a deficiency of the currently certified toolkit that a
future round might patch. The theorem also retroactively explains *why* Lemma K's
own proof has the shape it has (Lemma K's second branch is literally an instance of
this lemma's contrapositive).

Per the dispatch instructions and the outline's own honesty clause, this is reported
as a clean RETHINK for this specific mechanism, not forced into a fake rescue —
Status is `unsolved` for this approach, with the negative result documented in full.

## Promotable lemma
**Minimality Tautology Lemma** (+ its No-Smaller-Fully-Legal-Competitor Corollary) —
proved in full in the approach file. Fully unconditional, portable, general (holds
for any n≥2 of any sequence obeying this problem's greedy rule). Recommend
certifying to `lemmas/minimality-tautology-lemma.md`; it rules out an entire family
of future "construct a smaller legal competitor" proof attempts in one stroke,
generalizing Lemma K's internal proof step (round 7) into standalone reusable
content.

## File written
`/home/agentuser/repo/results/imo-2026-06/approaches/confined-competitor-construction.md`
