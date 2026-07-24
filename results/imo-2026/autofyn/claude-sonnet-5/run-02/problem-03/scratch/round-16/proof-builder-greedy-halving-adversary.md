# Round 16 build report — greedy-halving-adversary

**This slug's status: `partial`** (unchanged at the whole-problem level —
the overall theorem is still not fully closed), but a real, previously-open
sub-target (Target Q, as isolated by Proposition 30 / the round-16 outline)
is now **closed unconditionally**.

## What was done

1. **Resolved the outline's flagged prerequisite** ("does truncation at a
   threshold $v$ preserve the piecewise-affine/vertex structure needed to
   transplant `vertex-minimum-theorem`?"): **yes**, confirmed directly —
   adjoining the finite hyperplane family "fragment $=v$" to the existing
   tie/zero families still yields cells on which sort order and
   `>v`-membership are both locally constant, so $S\mapsto A(S_{>v})$ is
   affine per-cell, exactly as for $A(S)$ itself.

2. Worked out the resulting **exact vertex/max closed form** as a
   byproduct: for a $k$-ladder (top piece $q_1$), the construction "leave
   $q_1$ untouched, split every other piece exactly in half" (using
   exactly $k$ cuts) gives an exactly-paired residual (`odd-run-reduction-
   lemma`) dominated by $q_1$ (`dominant-element-removal-identity` +
   `general-ladder-dominance`), yielding $\max_S A(S_{>v}) = q_1$ for
   $v<q_1$, matching the a priori `max-domination-lemma` ceiling exactly.

3. **Discovered (by direct computation, not the vertex route) that this
   exact-max fact alone is too weak** to close Proposition 30's remaining
   gap for $v$ near $s$ — the true requirement is a bound on the *joint*
   quantity $\Psi(v)=A(R')-2A(R'_{>v})+2v\epsilon(v)$, not a composition of
   separately-extremized one-sided bounds on $A(R')$ and $A(R'_{>v})$.

4. **Proved the joint bound directly**: a new, fully general lemma,
   the **Truncated Alternating Sum Floor**
   (`results/imo-2026-03/lemmas/truncated-alternating-sum-floor.md`):
   for any finite multiset $S$ (total $T$) and any $v\in[0,T]$,
   $$A(S)-2A(S_{>v})+2v\epsilon(v)\ge v-T,$$
   a two-line consequence of the already-certified
   `upper-truncation-identity` plus trivial $\{0,1\}$-valued-integral
   bounds — no ladder structure, no legality assumption, no induction
   hypothesis needed.

5. Applied it to close **Theorem 31**: the entire $\ell(F)=1$, $v<p_2$,
   $p_2$-untouched branch (round 15's "items 1 and 2") is now closed
   **unconditionally**, for every $n\ge3$ — this upgrades Proposition 24
   too (which previously needed a recursive hypothesis).

6. **Checked honestly whether the same trick closes Target B** (item 3,
   $\ell(F)=2$, $\tau_P\ge p_3$) — it does **not**, and I diagnosed exactly
   why: Target B's object refines the *full* tail $\{p_2,\ldots,p_{n+1}\}$
   (total $r=p_2+s$), not just $\{p_3,\ldots\}$ (total $s$), so the
   relevant truncation interval has length $\approx r$ instead of
   $\approx s$ — an order of magnitude too crude for the elementary bound.
   This corrects round 15's conjecture that items 1/2 and item 3 are "the
   same obstruction"; a concrete restart point (peel $p_2$ off first) is
   recorded for the next round.

## Verification

All new claims checked with exact-`Fraction` Python scripts (not floating
point), left at:
- `/tmp/round-16/check_target_q.py` — refutes the naive "untouched ladder
  maximizes $A(S_{>v})$" guess by explicit counterexample, motivating the
  correct exact-max construction.
- `/tmp/round-16/check_psi_bound.py` — the Truncated Alternating Sum Floor
  itself, 20,000 trials/level, $k=1,\dots,5$, zero violations.
- `/tmp/round-16/check_full_closure.py` — end-to-end: $A(F\cup G')\ge f(n)$
  for random $\ell(F)=1$, $v<s$ configurations, $n=3,\dots,6$, 20,000
  trials each, zero violations.

## Files changed

- `results/imo-2026-03/approaches/greedy-halving-adversary.md` — added
  Theorem 31 and the Target B round-16 addendum (right after Proposition
  30 / before the pre-existing Target B section), updated Status/round-16
  preamble under "Current best," added a round-16 "Approaches tried"
  bullet, and updated "Open gaps" with a round-16 status block.
- `results/imo-2026-03/lemmas/truncated-alternating-sum-floor.md` — new
  lemma file (proposed, not yet reviewer-certified).

## What remains open (unaffected by this round)

- Target B (item 3): genuinely open, diagnosed reason the Floor-lemma
  trick fails, concrete next step given (peel $p_2$ first).
- $v<p_2$ with $G'$ cutting $p_2$ itself (remaining branches of
  Propositions 21/25) and the general $\ell(F)\ge2$ collapse: untouched
  this round, exactly as previously recorded.
