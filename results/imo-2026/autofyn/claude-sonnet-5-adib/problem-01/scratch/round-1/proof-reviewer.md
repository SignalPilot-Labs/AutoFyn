# Proof review — imo-2026-01, round 1

Note (aside, not blocking review): `problems.jsonl` lists `imo-2026-01`'s `difficulty_level` as
`"medium"` (`difficulty_rating: 5`), not `"hard"`, despite `CLAUDE.md`'s "target hard problems
only" rule. This run's dispatch explicitly fixed this problem, so I reviewed it as directed;
flagging the mismatch for the orchestrator's awareness only.

Both candidates were reviewed independently, each against the actual problem statement (parts
(a): termination to exactly one entry $M>1$; (b): $M$ is independent of Confucius's choices), and
each against `CLAUDE.md`'s rigor rules (no skipped cases, no hand-waving, name every theorem,
prove not conjecture, verify final answers). I additionally wrote and ran independent Python
verification: (1) 200 random-board Monte-Carlo trials (sizes 2–6, 5 random-order plays each)
checking the terminal survivor always equals the claimed closed form
$M=\prod_p p^{\gcd_i v_p(x_i)}$; (2) 40 trials with **exhaustive enumeration of every possible
move order** on boards of size 3–5, confirming the terminal survivor is unique (confluence) and
matches the closed form in every case, including boards with repeated values (stress-testing the
demand-multiset formalism used by `confluence-newman`, e.g. board $\{6,6,10\}$ traced by hand and
matched against the code, correctly getting $M=30$). All checks passed with zero mismatches.

## `prime-valuation-invariant`

**Verdict: APPROVE** — Status: **solved** (matches the builder's claim).

Re-derived independently (not just read): Lemma 1 (valuation formulas for gcd/lcm) is the standard
unique-factorization fact, correctly proved. Lemma 2 (Euclidean-subtraction identity
$\gcd(\min(\alpha,\beta),|\alpha-\beta|)=\gcd(\alpha,\beta)$) is the load-bearing step; its case
split ($\alpha=\beta$; $\alpha<\beta$ with the $\alpha=0$ boundary handled as a genuinely separate
sub-case rather than folded silently into the general common-divisor argument; $\alpha>\beta$
symmetric) is exhaustive and each case is a full divisibility argument, not an assertion — I
re-derived it from scratch and it matches exactly. Lemma 0/0' (multiset-gcd via a commutative
semigroup, extended to include $0$) is a genuine, correct proof (associativity/commutativity
checked including the zero-entry boundary cases, then lifted to arbitrary finite combination via
induction on multiset size) — this is the "multiset-gcd associativity lemma" I was asked to
scrutinize, and it holds up. Lemma 3 (global per-prime invariance) correctly combines Lemma 0 +
Lemma 2, and correctly notes $2026>2$ guarantees the "untouched" sub-multiset is nonempty (not a
hidden edge case — explicitly addressed). Lemma 4's termination monovariant $(\Omega,C)$ splits
into the two *exhaustive, disjoint* cases $\gcd(m,n)=1$ vs. $>1$ and shows strict lexicographic
decrease in both — this exhausts all possibilities since $\gcd(m,n)\ge1$ always holds; no case is
skipped. Steps 5–6 (exactly one survivor) and Step 8 (closed form for $M$) are correctly assembled
from the invariant, and the final closed form $M=\prod_p p^{\gcd_i v_p(x_i)}$ is not merely
asserted — it is derived by explicitly evaluating $g_p$ at the terminal state (a singleton nonzero
entry vs. the all-zero case, both handled) and equating with $g_p(S_0)$, and is additionally
sanity-checked against the classical two-variable subtractive Euclidean algorithm and against my
independent computational check (200/200 random trials matched exactly). No hand-waving, no
skipped cases, no gap found. The proof is self-contained (all theorems, e.g. unique factorization,
well-ordering of $\mathbb Z_{\ge0}\times\mathbb Z_{\ge0}$ under lex order, are invoked by name and
either standard or proved outright — nothing is justified merely by "by the crux from..."). This
proof is complete and correct: **solved**.

## `confluence-newman`

**Verdict: APPROVE** — Status: **solved** (matches the builder's claim).

This is a substantially more elaborate route and I scrutinized it hardest, per the dispatch
instructions.

- **Multiset-vs-tuple modeling.** The "Position-irrelevance" argument for working with multisets
  instead of labeled tuples is informal but sound: the problem statement itself does not specify
  which vacated slot receives $\gcd$ vs. $\mathrm{lcm}/\gcd$, so slot-labels carry no information
  relevant to "how many entries exceed 1" or "what is the surviving value" — exactly what parts
  (a),(b) ask about. This is an acceptable, correctly-justified simplification, not a hidden gap.

- **Newman's Lemma.** The statement (well-founded + locally confluent $\Rightarrow$ confluent) is
  correct, and the proof given is the standard Noetherian-induction diamond argument: fix $a$,
  assume $P(a')$ for all direct successors $a'$; the $a=b$ (resp. $a=c$) base case is handled
  trivially and correctly; the general case correctly builds $e$ from local confluence at $a$, then
  applies the induction hypothesis twice (at $a_1$ then at $a_2$, composing via transitivity of
  $\to^*$) to reach a common $d$. This is a faithful, complete, and correct reproduction of the
  standard proof — I checked each transitivity/IH-application step and found no gap. The "in
  particular, unique terminal state reachable" corollary is correctly derived (a terminal element's
  only $\to^*$-successor is itself).

- **Overlap Localization Lemma (the highest-risk claim).** I independently re-derived this: writing
  $\delta_1,\delta_2$ as the two size-2 demand multisets, the identity
  $|\delta_1|+|\delta_2|=|L|+|\delta_1\wedge\delta_2|$ (from $x+y=\max(x,y)+\min(x,y)$ pointwise) is
  correct, giving $4=|L|+|\delta_1\wedge\delta_2|$. Case $|\delta_1\wedge\delta_2|=0$ (disjoint
  support) $\Rightarrow|L|=4$; case $\ge1$ (shared value) $\Rightarrow|L|\le3$, and $|L|=2$ is ruled
  out because it would force $\delta_1=\delta_2$ (a sub-multiset with size equal to its ambient
  multiset must equal it) — contradicting $\delta_1\ne\delta_2$; so $|L|=3$ exactly whenever
  overlapping. This is an exhaustive, correct case split with no missing case (the only possible
  overlap sizes are $0,1,2$ since $|\delta_i|=2$, and all three are handled). I stress-tested this
  against a concrete repeated-value example (board $\{6,6,10\}$, i.e. $\delta_1=\{6,6\}$ vs.
  $\delta_2=\{6,10\}$) by hand and by code; it correctly predicts $|L|=3$ and the labeling
  $\delta_1=\{a,b\},\delta_2=\{b,c\}$, and the resulting confluence computation checks out
  ($M_0=30$ from both branches, matching independent simulation).

- **Local confluence, disjoint case ($|L|=4$, §8) and overlapping case ($|L|=3$, §9).** The
  disjoint case is straightforward (each move remains legal after the other is applied first) and
  correct. The overlapping case is the one where the builder reports discarding the outline's
  original (false) shortcut and replacing it — I checked the replacement argument carefully: it
  reduces local confluence on the 3-occurrence footprint $\{a,b,c\}$ to the *same* invariant +
  termination machinery already proved for general $k\ge2$ in §§2–3 (not circular: those lemmas are
  proved directly from the Euclidean-subtraction identity and never invoke confluence), applied at
  $k=3$ to show every maximal play from $\{a,b,c\}$ reaches the same terminal multiset $\{M_0,1,1\}$
  where $M_0=\prod_p p^{\gcd(v_p(a),v_p(b),v_p(c))}$; then a "Freezing observation" (a legal move on
  a sub-multiset of $S$ is a legal move on all of $S$, leaving the rest untouched) lifts both
  branches' continuations back to the full board, landing on the same state $D=R+\{M_0,1,1\}$. Each
  step of this chain is justified, not asserted; I re-derived the $M_0$ computation on $\{4,6,9\}$
  by hand (predicted $M_0=6$) and it is correct. This replacement argument is sound — no gap found.
  (Note: this makes the confluence machinery logically redundant with the direct invariant argument
  — §11's closed form is proved directly via the same Lemma 2 at $k=2026$ without needing §§6–10 at
  all — but redundancy is not an error; §10 alone is still a complete, self-standing proof of part
  (b), and §11 is correctly labeled as a corollary, not required for part (b) since the problem
  does not demand an explicit formula, only non-dependence on choices.)

- **Termination (§3).** Uses the identical $(\Omega,C)$ lexicographic monovariant as the sibling
  approach, proved independently here (not imported), with the same two exhaustive cases
  ($\gcd(m,n)=1$ vs. $>1$). Correct.

No unresolved gap found in `confluence-newman`. It is longer and more indirect than
`prime-valuation-invariant`, and its confluence machinery turns out to be provably unnecessary
(the direct invariant argument alone suffices, as the corollary in §11 shows), but that is a
matter of economy, not correctness. Both parts (a) and (b) — including an explicit, verified
closed form for $M$ as a bonus corollary — are established rigorously. **solved**.

## Overclaim check

Both builders marked their approach `solved`, and in both cases this matches my independent
assessment after re-deriving the load-bearing lemmas from scratch and cross-checking numerically
(200 random + 40 exhaustive-enumeration trials, zero mismatches). No downgrade needed for either.

## Actions taken

- `results/imo-2026-01/current.md` updated: `## Status` set to `solved`, `## Full proof` populated
  with the `prime-valuation-invariant` proof (chosen as the more direct of the two correct proofs,
  per dispatch instruction to prefer the simpler one), `## Approaches tried` records both as
  verified-solved with a note on why `confluence-newman` was not selected as the primary write-up
  (redundant machinery, not a correctness issue).
- Certified two promotable lemmas (both approaches' shared core, re-verified independently) into
  `results/imo-2026-01/lemmas/`:
  - `euclidean-subtraction-identity.md` — $\gcd(\min(\alpha,\beta),|\alpha-\beta|)=\gcd(\alpha,\beta)$.
  - `multiset-gcd-invariance.md` — per-prime $g_p$ invariance under the board move, general $k\ge2$.
- `mcp__approach-ranker__record_outcome` called for both slugs with outcome `verified-milestone`.

## Verdict summary

- **prime-valuation-invariant: APPROVE** (Status: solved)
- **confluence-newman: APPROVE** (Status: solved)

The problem `imo-2026-01` is fully solved; `current.md` `## Status` is now `solved` with a complete
Full proof.
