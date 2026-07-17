# Lemma: Folding Lemma (equal pairs plus one small leftover)

**Certified** by proof-reviewer, round 1 (source: approaches/pairing-exchange-normal-form.md, Section 5, Lemma 5).

## Statement
Let A and B be disjoint sets of current pieces (positive lengths) of a partially cut stick, with v = sigma(A) - sigma(B) >= 0. Using at most |A| + |B| - 1 marks, all strictly interior to current pieces (hence automatically distinct from all existing marks), one can cut so that every resulting fragment of the pieces of A and B is matched into exactly equal pairs, except for at most one leftover fragment of length <= v.

## Proof
Cross-fold: repeatedly Fold(a,b) for a in A, b in B — cut the longer at distance min(a,b) from its end, banking an equal pair at zero cost; the remainder replaces the longer piece. The difference sigma(A) - sigma(B) = v is invariant; B empties first (else sigma(B) = -v <= 0 with positive pieces). Then fold the surviving A' (sigma(A') = v) down pairwise to at most one piece of length <= v. Mark count: each mark-using iteration removes exactly one piece from the working collection, each markless (equal-lengths) iteration removes two, and a finish at zero pieces is necessarily markless, so marks <= |A| + |B| - 1. Handles B empty and v = 0. Full details in the source file, Section 5.

## Reviewer verification
Invariant and mark count re-derived by hand; strategy simulated on 16000+ configurations (n <= 5) always using <= n total marks with leftover <= v.
