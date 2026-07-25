## proof-builder report — global-lp-vertex-sufficiency (round 14)

File updated: `/home/agentuser/repo/results/imo-2026-03/approaches/global-lp-vertex-sufficiency.md`
(Status unchanged: `partial`).

### What was done

1. **Corrected the target's scope** (mandatory first step per dispatch,
   new Section 4.8.0): the round-11 Mass-Constraint Theorem only rules
   out a *fixed*, $n$-independent split-piece count $s_0$ for the
   tie-to-whole-untouched-piece construction family. It says nothing
   about (a) an $n$-dependent construction using up to the full $n$-cut
   budget, or (b) fragment-vs-fragment tying (its proof's key inequality
   $T_a\le p_{i_a}$ literally requires $T_a$ to be a sum of whole
   untouched pieces). Round 13's "deprioritized" framing for
   fragment-vs-fragment tying is corrected: it's the one route the
   Mass-Constraint Theorem does not touch.

2. **Cheap-kill 1 (cyclic pairwise-tie chain), own independent exact-
   `Fraction` script**: tested exhaustively (every odd $s\le n$, every
   subset, every cyclic order) against the 3 catalogued $n=3$ hard
   interior points plus 12–15 fresh random balanced-region points per
   $n=3,4,5,6$. **Result: fails broadly, in exact rational arithmetic (no
   noise possible)** — 9/15 (n=3), 15/15 (n=4), 13/15 (n=5), 15/15 (n=6)
   of tested points have the family's own best member exceed $c(n)$;
   even at the specific $n=3$ hard point where round 12/13's own $V(p)$
   is well below $c(3)$, this family's best member gives an exact excess
   of $47/30000\approx0.00157$ over $c(3)$. Reported as a negative
   finding, not written up as a lemma, per the dispatch's instructions.

3. **Cheap-kill 2 (descending fragment chain, the outline's specified
   next candidate)**: found and fixed a genuine construction bug in the
   first draft (conflating a tied *value* with a single shared
   *variable*, silently dropping a fragment — caught because it produced
   $\mathrm{OddSum}<\mathrm{sum}(M)/2$, violating the elementary OddSum
   Floor fact). After the fix: **mixed, inconclusive result**. Restricted
   to natural/simple orderings (full-chain descending or ascending index
   order), it fails broadly (5/8 to 8/8 across $n=3..6$, same order of
   failure as the cyclic family). But an *exhaustive* search over
   subset/order choice at the 3 catalogued $n=3$ hard points **matches
   the true $V(p)$ exactly at 2 of 3 points** and clears $c(3)$ at all
   three — genuinely promising as an existence signal, but that
   exhaustive search is combinatorially as expensive as computing $V(p)$
   directly, so it is **not** a closed form and does not constitute a
   "survival" of the cheap-kill in the sense the dispatch meant (a
   tractable construction). Per the dispatch's own gate, since no
   tractable rule for choosing subset/order/free-parameter was found,
   the mandatory next step (generalize Singleton-Interleaving to a
   closed form and prove $\le c(n)$ for all $n,p$) was **not** attempted
   this round — doing so on this unproven premise would be an overclaim.

### Honest open question left for next round

Two precisely-stated open sub-questions (Section 4.8.2, end): (1) is
there a closed-form/simple rule for choosing the descending-chain's
subset, order, and free parameter that always matches or beats $c(n)$?
(2) does the true optimal adversary response $\sigma^*(p)$ always have a
descending-fragment-chain shape (which would explain the exact match at
2/3 tested points), connecting to the still-open $\Sigma(n,k)$-
classification route? Neither is established.

### No lemma proposed for certification

Both findings this round are numerical (one cleanly negative/exact, one
genuinely mixed), not general proved theorems — correctly not proposed
for `lemmas/`.

### Status: `partial` (unchanged)
