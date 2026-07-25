## imo-2026-03 (lens: `greedy-reduction-geometric`'s Level-Absorption k=2 base case)

### Precise restatement of the target (re-derived from the approach file + lemma, all hypotheses included)

Source: `approaches/greedy-reduction-geometric.md` Section 14.3, certified negative
result + reduction in `lemmas/level-absorption-banking-lemma-and-swap-refutation.md`.

> **Base Case (Level-Absorption, k=2).** Let $m\ge3$. Let $b_2\in[2^{m-2},2^{m-1}]$.
> Let $P$ be a finite multiset of positive reals with $\mathrm{sum}(P)=2^{m-1}$ and
> $\max(P)<b_2$ (this forces $|P|\ge2$). Let $S'''$ be a refinement of
> $\Gamma_{m-3}=\{2^{m-3},2^{m-4},\dots,2^0\}$ (each level split into an arbitrary
> number of positive pieces summing to that level's value; a level may be left
> unsplit). **Budget constraint (load-bearing — corrected per round-10's note,
> this is the exact game's total-cut budget, not an ad hoc cap):**
> $(|P|-1)+(\text{cuts used inside }S''')\le m-1$. Then
> $$\mathrm{OddSum}\bigl(P\cup\{2^{m-2}\}\cup S'''\bigr)\ \ge\ b_2.$$

This is the $B''=\varnothing$ (i.e. $k=2$) instance of (10.3b), Subcase (b) of
Theorem 7'$(m,k;L)$'s inductive step; it is what remains after Lemma M
(B''-Banking) disposed of the $B''\ne\varnothing$ layer and the Candidate Swap
Lemma was refuted as the combination mechanism.

### New this round: a genuine, cheap, rigorous reduction (not just numerics)

**Claim (WLOG $b_2=2^{m-1}$).** It suffices to prove the Base Case for
$b_2=2^{m-1}$ exactly (with hypothesis $\max(P)<2^{m-1}$, automatic since
$|P|\ge2$). *Proof:* $b_2$ appears in the statement only (i) as the value being
subtracted on the right and (ii) in the constraint $\max(P)<b_2$. Neither $P$,
$S'''$, nor the budget depend on $b_2$. If $b_2'<2^{m-1}$ and $P$ satisfies
$\max(P)<b_2'$, then a fortiori $\max(P)<2^{m-1}$, so $P,S'''$ is *also* a valid
instance of the $b_2=2^{m-1}$ statement; if that gives
$\mathrm{OddSum}(M)\ge2^{m-1}$, then trivially $\ge b_2'$. $\blacksquare$

This matches (and now rigorously explains, not just numerically observes) the
fact that **every worst/tight instance found (both by the approach's own
27,430-trial search and by my independent re-tests below) has $b_2=2^{m-1}$
exactly**. At $b_2=2^{m-1}$ the target is exactly Lemma L's zero-slack baseline
($\Sigma=2^{m-1}-b_2-\mathrm{sum}(B'')=0$ when $B''=\varnothing$), so the
Base Case reduces cleanly to a **single-parameter-fewer** statement: "does
splitting the value $2^{m-1}$ into $P$ ($\ge2$ pieces) and unioning with
$\{2^{m-2}\}\cup(\text{budget-limited refinement of }\Gamma_{m-3})$ still reach
$\mathrm{OddSum}\ge2^{m-1}$" — i.e. a **Split-Degradation-at-zero-slack**
question, the $k=2$ special case of the Section 13.2 diagnosis.

### Why the already-refuted / already-insufficient mechanisms recur here too (checked, not assumed)

Applying the certified tools directly: if $\max(P)=q_1\ge2^{m-2}$ (call this
**Case A**), Theorem 7a (with $M:=m-1$, $b_1:=q_1$) applied to
$\{q_1\}\cup\{2^{m-2}\}\cup S'''$ gives $\mathrm{OddSum}(\{q_1\}\cup\{2^{m-2}\}\cup
S''')\ge q_1$, and then Theorem 13 (General Insertion Monotonicity) inserting
$R:=P\setminus\{q_1\}$ gives only $\mathrm{OddSum}(M)\ge q_1$ — **strictly weaker
than the target $b_2>q_1$**, exactly the same shortfall pattern Section 13.2
already proved insufficient for the general case. So the base case is **not**
mechanically easier than the general problem; it inherits the identical
obstruction (a structure-agnostic peel+insert loses exactly the gap
$b_2-q_1$, i.e. discards exactly the "second-fragment" contribution of $P$).
**Any workable proof of the base case must extract a quantitative contribution
from $P\setminus\{q_1\}$'s own rank position, not just its existence** — i.e.
it needs the same missing ingredient as the general problem, just in its
smallest instance.

### Stress-testing (exact `Fraction`, independent from the builder's script)

- General random search (60,000+ trials across $m=3,\dots,10$, both
  uniform-random and "skewed" adversarial split shapes — near-equal,
  one-dominant, geometric — for both $P$ and $S'''$, full cut-budget
  respected): **zero violations**, worst margin found is **exactly $0$**,
  always at $b_2=2^{m-1}$ (confirming the WLOG reduction above independently).
- Restricting to **Case B** ($\max(P)<2^{m-2}$, i.e. $P$'s top fragment stays
  below the next level down): 23,905 valid trials, worst margin
  $102503/300500\approx0.34$ — **substantial slack**, no near-ties found. This
  is a genuine structural finding: **the hard regime is exactly Case A**
  ($\max(P)\ge2^{m-2}$); Case B looks like it should follow from a much
  cruder/easier argument (worth confirming next round, but not yet attempted).
- A finer probe at $m=4$: fixing $S'''=\Gamma_1=\{2,1\}$ unsplit and sweeping
  $P=(q_1,4-... )$ wait: sweeping $P=(8-q_2,q_2)$ over $q_2\in(0,4]$ gives
  margin $\ge1$ everywhere (never tight) — so the genuinely tight instances
  need **either** $S'''$ itself split (20,000 trials with $S'''$'s 2 extra
  cuts randomly allocated, $p=2$: worst margin found $=1/2$, still not $0$)
  **or** $P$ itself split into $\ge4$ pieces in a near-geometric pattern (the
  actual zero-margin instance found has $P\approx\{0.53,1.07,2.13,4.27\}$,
  ratios close to $1:2:4:8$, i.e. $P$ mimics LB's own self-similar shape one
  level down). This is consistent with the file's own repeated observation
  (round 5/6/9, memory rule #6) that the extremal mechanism is self-similar
  "many exact ties," not a 2-piece split — **worth telling the outliner
  explicitly: the base case's own worst case is not $|P|=2$; a proof
  strategy that only handles $|P|=2$ well and treats larger $|P|$ by crude
  induction/insertion is likely to hit the same wall the general case hit.**

### Distinct openings for a proof mechanism (none attempted beyond diagnosis)

1. **Direct new induction on $m$ via Peeling + Companion Peeling** (reusing
   certified Lemma 3/Lemma 5, the same tools Theorem 5's proof used), but on
   the genuinely different hypothesis "$\max(P)<2^{m-1}$" (no per-element
   chain on the rest of $P$) rather than full Dominance-Chain shape — would
   need a case split on $q_1$ vs $2^{m-2}$ (Case A/B above) and likely a
   secondary induction on $|P|$ or on the rank of $q_1$ within the merged
   sort order, tracking how much of $P\setminus\{q_1\}$'s mass lands at
   *odd* vs *even* ranks once merged with $\{2^{m-2}\}\cup S'''$ — this is
   exactly the "second-fragment contribution" the insufficiency diagnosis
   above says is missing.
2. **Exchange/extremal-profile reduction** (crux `aimo-0146`, already flagged
   by round 9's dispatch as the live lead for the general Level-Absorption
   problem): now sharply testable on this smaller base case — reduce
   arbitrary $P,S'''$ to a small finite family of extremal shapes (the
   near-geometric self-similar shape found above is a strong candidate
   extremizer) and check the inequality only there. The base case's much
   smaller parameter space (no $B''$ layer) makes this more tractable than
   attempting it directly on the general $k\ge3$ statement.
3. **A sharper Split-Degradation bound using $S'''$'s actual structure**
   (Section 13.2's lead (b)): since $\max(P)<b_2=2^{m-1}$ exactly and
   $S'''\cup\{2^{m-2}\}$ is not an arbitrary multiset but a refinement of
   $\Gamma_{m-2}$, a bound on the degradation that uses the specific
   power-of-two levels (not just $g,q_1$) might close the gap — e.g. compare
   $q_2$ (second-largest of $P$) against $2^{m-3}$ (top of $\Gamma_{m-3}$):
   my probe above found the tight/zero-margin locus is roughly where $q_2$
   is *not small* relative to $2^{m-3}$, i.e. a genuine interleaving/tie
   condition between $P$'s own second fragment and $S'''$'s top level — this
   smells like a natural target for a Prefix-Run-Peeling-style
   decomposition (Lemma 6, already certified) applied to $P$ itself as a
   two-tier object, not just to the original $A\cup\Gamma$ setup.

### Cheap-kill candidates
- **The WLOG $b_2=2^{m-1}$ reduction above** — free, rigorous, should be
  adopted immediately; removes one free parameter before any proof attempt.
- **The Case A/Case B split** ($\max(P)\gtrless2^{m-2}$) — Case B has large
  numeric slack (∼0.34 at $m=4$) suggesting it may close via a much cheaper
  argument (e.g. direct application of a TOP-ONLY/Dominance-Chain-style
  bound treating $2^{m-2}$ as the true dominant element and $P$ as bounded
  "extra" mass via Theorem 13 insertion alone) — worth confirming/closing
  Case B outright next round as a quick win, isolating Case A as the sole
  remaining hard sub-case.

### Knowledge-base / crux entries
- No new `knowledge_base.md` entries beyond what's already in use
  (elementary exchange/pairing arguments, already fully internalized by this
  approach's own from-scratch lemmas — this problem does not match any
  named KB theorem closely enough to cite beyond general proof-method
  entries already implicitly used).
- Crux corpus: per round 9's finding, `aimo-0146` (exchange-smoothing /
  extremal-profile reduction) remains the best analogue for reducing an
  infinite split-shape adversary to a finite checkable family — directly
  relevant to opening (2) above. I did not find a closer match this round
  specific to the "split-then-merge-with-fixed-geometric-tail" shape; the
  problem's specific combination (OddSum of a merge with a fixed dyadic
  sequence) still appears to have no close analogue in the corpus beyond
  this already-identified one (consistent with prior rounds' memory rule
  #26: games-and-strategy subtopic matches are mostly false positives here).

### Dead ends (confirmed, do not retry)
- **Candidate Swap Lemma family** (structure-agnostic "$Q\cup P\ge Q\cup\{b\}$
  whenever $\mathrm{sum}(P)\ge b,\max(P)<b$") — refuted with an exact
  counterexample ($Q=\varnothing,b=10,P=\{6,6\}$); I additionally checked
  that even the *sum-equality* restriction ($\mathrm{sum}(P)=b$ exactly, not
  just $\ge b$) with $Q=\varnothing$ still fails ($P=\{5,5\},b=10$:
  $\mathrm{OddSum}(P)=5<10$) — so narrowing to exact-sum does not rescue it
  either; the fix must come from $Q$'s specific (non-arbitrary) structure.
- **Structure-agnostic Split-Degradation bound** (depending only on $g,q_1$,
  Section 13.2) — proved insufficient whenever $B''\ne\varnothing$; I
  verified above it is *also* insufficient at $B''=\varnothing$ (the base
  case itself), since the peel+insert chain via Theorem 7a+13 caps out at
  $q_1$, strictly below the $b_2=2^{m-1}$ target whenever $|P|\ge2$ — so
  this mechanism is dead for the base case too, not just the general case.

### Small-case / intuition notes (all conjecture, labeled)
- The base case's true worst-case locus is $b_2=2^{m-1}$ (now proved, not
  conjectured, via the WLOG reduction) combined with $\max(P)\ge2^{m-2}$
  (Case A, numerically the only regime with near-zero margin) and $P$ having
  $\ge3$–$4$ pieces in a near-geometric/self-similar shape (numerically the
  only configurations reaching exact margin $0$; $|P|=2$ configurations
  retain visible slack in every test run, $\ge0.5$ at $m=4$).
- No violation found anywhere (89,000+ combined exact-`Fraction` trials
  across this round and the certified round-10 search), consistent with the
  base case being true; the obstruction is a missing proof technique
  (quantifying $P$'s "second-fragment" OddSum contribution against the
  specific dyadic tail), not near-tightness/falsity.

### Prior progress (from `current.md` / lemma file, verified consistent)
Lemma M (B''-Banking) and the Candidate Swap Lemma refutation are both
correctly certified (traced hypotheses myself against Theorem 7, consistent
with the reviewer's own trace). Level-Absorption itself remains open; this
round's contribution is (a) a free rigorous parameter reduction
($b_2=2^{m-1}$ WLOG), (b) a precise re-derivation that the "obvious" tools
(Theorem 7a+13 chain) fail on the base case for the *same* reason they fail
on the general case, and (c) numeric localization of the hard sub-regime
(Case A, $|P|\ge3$-ish near-geometric shapes) to focus the next attempt.
