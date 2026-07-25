# Proof review — imo-2026-03, round 1

Problem: Liu Bang / Xiang Yu stick-cutting game. Determine
$c(n) = \max_{\text{LB}}\min_{\text{XY}}(\text{LB's alternating-claim total})$
where LB marks $\le n$ points, then XY marks $\le n$ points, the stick is
cut, and pieces are claimed alternately (LB first). `task: compute_and_prove`,
`answer_type: expression`. Conjectured/target answer across all three
approaches: $c(n) = 2^n/(2^{n+1}-1)$.

I independently verified the load-bearing shared lemma (Greedy-Optimality:
alternating claim on a fixed multiset has value = OddSum, the sum of
odd-ranked elements in descending order) by brute-force backward induction
against 2000 random multisets of size 1–7 — matches to floating-point
precision. I also independently verified $c(2)=4/7$ by a broad
grid + multi-start Nelder-Mead minimax search over LB partitions and XY
responses (best found value $\approx 4/7$, nothing found above it after
raising restart count to rule out local-optimum artifacts). I verified the
"duplicate-the-rest" closed-form theorem (`universal-halving-adversary`) by
exact integer computation for $n=1,\dots,9$: exact match every time. I also
directly checked the disputed 3-way-tie step in `self-similar-induction-on-n`'s
$j=1$ telescoping argument at $m=2$: fine-grid search over the tail's
1-remaining-cut confirms the claimed value ($4$, unnormalized) is exactly
attained and not beaten — so the underlying claim is true even though the
write-up's justification of it is not fully rigorous (see below).

None of the three approaches claims `solved`; all three self-report
`partial`. My review confirms this is the correct Status for all three —
none overclaims, and none is fatally wrong. All three make genuine,
independently-verifiable progress, and one lemma (Greedy-Optimality) and
the reduction lemma are proved correctly and identically (up to
presentation) in two of the three files, giving a strong cross-check.

## Approach 1: `greedy-reduction-geometric.md`

**Verdict: CHANGES REQUESTED.**

**Status claim: partial. My assessment: correct, and this is the most
rigorous of the three.**

- Lemma 1 (Greedy-Optimality via exchange inequality $(\ast\ast)$): correct,
  independently re-derived and checked by me by brute force. No gap.
- Lemma 2 (Reduction to multiset minimax, position-irrelevance): correct,
  standard bijective argument, no gap.
- Lemma 3 (Global-max peeling identity): correct, immediate corollary of
  Lemma 1's proof, no gap.
- Section 4, Case 1 lower bound (XY never touches LB's top piece):
  correctly proved, a clean corollary of Lemma 3 plus $\mathrm{EvenSum}\ge0$.
  No gap.
- Section 5, $n=0,1$ full two-directional solution: I checked the algebra
  (the piecewise function $g(p_1)$, its continuity and crossing at
  $p_1=2/3$) and it is correct; this **agrees exactly** with the
  independently-derived $n=1$ formula in both `self-similar-induction-on-n`
  and `universal-halving-adversary` — a strong cross-validation.
- **The stated gap is real and precisely identified**: Case 2 of the lower
  bound (XY spends $\ge1$ cut on LB's own largest piece, $n\ge2$) is open;
  the file is honest that only specific XY responses were checked
  (numerically, exactly, via rational arithmetic) rather than proved for
  all responses. The general upper bound (arbitrary, non-geometric LB
  partitions) is not attempted at all beyond $n=0,1$. Both gaps are stated
  explicitly with no hand-waving disguised as a proof.

No hidden gap found beyond what the file itself flags. This is legitimate,
well-organized partial progress.

## Approach 2: `self-similar-induction-on-n.md`

**Verdict: CHANGES REQUESTED.**

**Status claim: partial. My assessment: correct, but the write-up of the
central computation (the $j=1$ "bisect-and-recurse" telescoping) contains a
genuine unaddressed gap beyond what the file itself admits, which the next
round should be told to fix explicitly.**

- Lemma 1 (Greedy-Optimality) and Lemma 2 (position/scale invariance):
  correct, essentially the same proof as in `greedy-reduction-geometric`
  (independently written), matches my brute-force check.
- $n=0$, $n=1$ full solutions: correct, matches the other two approaches.
- $j=0$ case ("top untouched" bound $L(m,k)\ge2^m$ for any $k$): correct,
  same content as `greedy-reduction-geometric`'s Case 1.
- **The $j=1$ telescoping computation ("solved exactly via self-similarity,
  for $k=m$") has a real gap the file does not fully resolve.** When XY
  bisects the top piece $T$ into two copies of $T/2$, the tail (the
  geometric partition $\Gamma_{m-1}$ scaled to $R$) has its own top piece
  exactly equal to $T/2$ as well — i.e. there are (at least) **three**
  mutually-tied pieces at value $T/2$ whenever the tail's own top piece is
  left unsplit, not two. The file's prose notices the tie ("wait these are
  equal, not strictly less") but then only discusses "the two $T/2$ copies
  (one from LB's top-half, one from the tail's own top piece)" — silently
  collapsing the two *XY-generated* halves and the pre-existing tail piece
  into a two-way framing, without ever addressing what happens with the
  full three-way (or, deeper in the recursion, possibly higher-order) tie,
  or justifying that ranks 3, 4, ... are cleanly handed off to a fresh copy
  of the $(m-1,m-1)$ subgame. I checked this numerically at $m=2$ (direct
  fine-grid search over the tail's one remaining cut) and the claimed value
  $2^m$ is genuinely attained — so the final number is right — but the
  *proof* of why does not go through as written; it needs the "block of
  $k$ tied elements contributes an amount depending only on the block's
  starting rank and $k$" generalization of Tie-neutrality (a short, provable
  fact — I stated and used it in the certified lemma
  `lemmas/tie-neutrality-and-first-mover-half.md`), which the file does not
  invoke. This is a real correctness/rigor gap in what is presented as a
  completed sub-computation, even though it doesn't change Status (the file
  never claims the *overall* result is proved — only this specific line of
  play — and honestly flags that $j\ge2$ and general worst-case optimality
  remain open).
- The larger stated gap — that this specific line of XY play is truly XY's
  worst case, for general $n$ and arbitrary top-splits — is honestly
  labeled open, verified only through $n=3$ by exhaustive/spot search.
- The "budget-free domination lemma is false" dead end (documented via an
  explicit counterexample $A=\{4,4\}$, $B=\{3.9,3.9\}$) is correct and
  useful — I checked it: merged descending $4,4,3.9,3.9$, OddSum $=7.9<8$.
  Correct, valuable negative result to record.

**Net: real progress, correctly self-graded as `partial`, but the next
round should be explicitly told to patch the 3-way-tie gap in the $j=1$
computation using the generalized Tie-neutrality lemma before treating that
sub-result as fully closed.**

## Approach 3: `universal-halving-adversary.md`

**Verdict: CHANGES REQUESTED.**

**Status claim: partial. My assessment: correct; this file's proofs are the
cleanest of the three and contain no gaps beyond what is admitted.**

- Lemma 1 (Tie-neutrality) and Lemma 2 (first-mover-gets-half): both
  correct, short and rigorous, standard consecutive-rank / pairwise-sum
  arguments. No gap.
- $n=1$ full solution: correct casework on the median of 3 pieces; I
  checked the case boundaries ($a\ge s$, $t-s\le a\le s$, $a\le t-s$) are
  exhaustive and non-overlapping, and the final $V(t)$ formula matches
  `greedy-reduction-geometric`'s independently-derived $g(p_1)$ exactly
  (both give $c(1)=2/3$ at $t=2/3$). Strong cross-validation, no gap.
- **Duplicate-the-rest theorem**: I independently re-derived and verified
  this by exact integer computation for $n=1,\dots,9$ — matches the claimed
  closed form $2^n$ (unnormalized) exactly every time, and the proof's use
  of Tie-neutrality (pairing $2^j$ with $2^j$, and correctly counting the
  three copies of the leftover value $1$ landing at odd/even/odd ranks) is
  valid and complete. No gap — this is a genuinely proved, reusable result,
  not just a numerical observation as some of the file's other findings are.
- **The admitted open gap (no universal XY response for arbitrary LB
  partitions, $n\ge2$) is real and precisely stated**, with explicit refuting
  counterexamples for each of the three candidate universal rules tried
  (duplicate-the-rest unconditionally; dyadic lineage bisection; two
  threshold heuristics). These counterexamples are correctly computed
  (I spot-checked the $(0.5,0.3,0.2)$, $n=2$ counterexample logic and it is
  sound: with $p_1=0.5\le c(2)\cdot 1$ and $p_1 \le$ sum of rest, yet the
  unsplit value $0.7 > 4/7$, so XY must act on a non-max piece — correct
  reasoning, no error).

No hidden gap found. This file is honest and its "solved" pieces are
genuinely solved.

## Certified lemmas

Held to full rigor bar (no `sorry`, statement not stronger than proved,
independently re-derived/spot-checked by me), the following are admitted
into `results/imo-2026-03/lemmas/`:

- `greedy-optimality-oddsum.md` — the OddSum value lemma (from both
  `greedy-reduction-geometric` and `self-similar-induction-on-n`).
- `reduction-to-multiset-minimax.md` — the two-phase-game reduction
  (position-irrelevance + scale-invariance), from both files.
- `dominant-piece-lower-bound.md` — the peeling identity and the "dominant
  piece guarantees itself" corollary (Case 1 lower bound), from
  `greedy-reduction-geometric` and `self-similar-induction-on-n`.
- `tie-neutrality-and-first-mover-half.md` — both lemmas from
  `universal-halving-adversary`, plus a generalized "tied block" corollary
  I added (needed to patch approach 2's gap; stated and proved here, not
  merely asserted).
- `duplicate-the-rest-exact-response.md` — the exact-equality theorem from
  `universal-halving-adversary`, reviewer-verified for $n=1,\dots,9$.

Nothing else was flagged promotable beyond these; the remaining claims in
all three files (Case 2 lower bound, general upper bound, $j\ge2$
optimality) are explicitly open and not certified as lemmas.

## current.md

Updated: `Status: partial`, `Current best` synthesizes the strongest
verified progress across all three approaches (the reduction, the proved
lemmas above, $n=0,1$ complete, and the two precisely-stated remaining
gaps: general lower-bound Case 2, and general upper bound for arbitrary
LB partitions). `Full proof` section left empty (correctly — nothing is
solved).

## Summary of verdicts

| Approach | Status (my assessment) | Verdict |
|---|---|---|
| `greedy-reduction-geometric` | partial | CHANGES REQUESTED |
| `self-similar-induction-on-n` | partial | CHANGES REQUESTED |
| `universal-halving-adversary` | partial | CHANGES REQUESTED |

All three approaches should stay live. Recommended focus for next round,
in order of leverage: (1) patch the 3-way-tie gap in
`self-similar-induction-on-n`'s $j=1$ computation using the generalized
Tie-neutrality lemma now certified in `lemmas/`; (2) attempt the general
lower-bound Case 2 ($n\ge2$, XY cuts LB's top piece) — likely needs a
genuine induction combining `dominant-piece-lower-bound.md` with a
merge/interleaving argument, not a budget-free domination shortcut (already
refuted); (3) the general upper bound remains the hardest open piece and is
common to all three approaches — the run should consider dispatching a
genuinely different framing for it next round if it stays stuck, per the
orchestrator's plateau-break guidance, since two different explorers
(`self-similar-induction-on-n`, `universal-halving-adversary`) have now
each independently hit the same wall (need for an adaptive/recursive
two-parameter strategy) from different directions.
