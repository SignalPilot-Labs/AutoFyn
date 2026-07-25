# Build report — greedy-reduction-geometric, round 5

## Task
Pivot off the now-subsumed TOP-ONLY casework (self-similar-induction-on-n
is separately proving Case-B(m,k)) to the genuinely open fully-general
Case 2 (top piece AND tail cut simultaneously), via a Joint Dominance-Chain
extension, per the outliner's skeleton.

## What was proved (fully rigorous, new this round)

1. **Lemma 8 (General Domination Prefix-Run Lemma).** A clean
   generalization of the certified Prefix-Run Peeling Decomposition Lemma
   (Lemma 6) to an arbitrary dominating block: if every element of $P$ is
   $\ge$ every element of $Q$, $\mathrm{OddSum}(P\cup Q)=\mathrm{OddSum}(P)+$
   (OddSum or EvenSum of $Q$, by parity of $|P|$). No geometric structure
   needed on $P$ or $Q$.

2. **Theorem 7 (Joint Dominance-Chain Closure, top-levels-clear).** If XY's
   split $B$ of the top piece $2^m$ has the certified Dominance-Chain
   property with $k=|B|\le m$ fragments, and the tail refinement $S$ leaves
   the top $k$ tail-levels ($2^{m-1},\ldots,2^{m-k}$) completely unsplit
   (arbitrary splitting is allowed on the remaining bottom $m-k$ levels),
   then $\mathrm{OddSum}(B\cup S)\ge 2^m$. Proved by strong induction on
   $k$, using only Global-max Peeling, Companion Peeling, and Lemma 8. This
   is the **first proved closure in this approach's history of any instance
   combining $j\ge1$ top-piece cuts with $c\ge1$ tail cuts simultaneously**
   — real new territory in the fully general Case 2, not a rehash of
   TOP-ONLY.

3. A negative check ruling out a natural shortcut: "refining the tail can
   only help LB" (which would trivially reduce Case 2 to TOP-ONLY) is
   **false** — an exact rational counterexample at $m=6$ found via random
   search.

4. A precise, proved diagnosis (the **Leftover-Fragment Obstruction**,
   Section 9.4) of exactly why the identical technique cannot be extended
   to allow splitting of the top tail levels themselves: peeling into a
   partially-split top level leaves a residual "leftover fragment" that
   does not have the clean recursive shape (refinement of a smaller
   $\Gamma$) the induction needs — a genuinely different obstruction from
   Proposition C (not a same-size loop; $m$ strictly decreases; the
   sub-problem simply leaves the proved hypothesis class).

5. Substantial numeric stress-testing (30,000+ random exact-rational trials,
   plus a `scipy` Nelder-Mead adversarial search over the tightest boundary
   configuration up to $m=11$) showing the wider, unproved conjecture
   ("Dominance-Chain $B$ implies the target for *any* tail refinement,
   including interleaved/top-level splits") is consistent with all evidence
   — reported honestly as a well-supported open conjecture, not a theorem.

## Explicit dependency note

This work does **not** depend on and does not duplicate
`self-similar-induction-on-n`'s Case-B(m,k) (that target is scoped strictly
to TOP-ONLY, $S=\Gamma_{m-2}$ exactly; this round's target needed genuine
tail refinements, $S$ an arbitrary refinement). No result from Case-B(m,k)
was assumed or needed.

## Status

`partial` (unchanged headline status — the fully general lower-bound
direction is still open) but the specific gap this round targeted (fully
general Case 2) now has a real, non-trivial, unconditionally proved
sub-closure plus a precisely located remaining obstruction, replacing what
was previously a completely open, unattempted target.

## Promotable lemmas

- **Lemma 8 (General Domination Prefix-Run Lemma)** — Section 9.1,
  `results/imo-2026-03/approaches/greedy-reduction-geometric.md`. Fully
  proved, no hypotheses beyond a domination ordering.
- **Theorem 7 (Joint Dominance-Chain Closure, top-levels-clear)** — Section
  9.2, same file. Fully proved by strong induction, strictly generalizes
  the certified Dominant-Chain Theorem.

File updated:
`/home/agentuser/repo/results/imo-2026-03/approaches/greedy-reduction-geometric.md`
