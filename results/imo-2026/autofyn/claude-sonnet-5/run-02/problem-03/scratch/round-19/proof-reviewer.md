# Round 19 proof-reviewer report — imo-2026-03

Problem: determine, for all n, the largest c(n) Liu Bang can guarantee.
Overall status BEFORE and AFTER this round: **partial**. Nothing this round
closes the whole problem. Claim (A) (a restricted lower-bound sub-case,
`rank-pigeonhole-budget`'s own scope) was already fully solved in round 8
and remains solved — this is not new. The two live fronts of the whole
problem — the general lower bound (Claim B / restricted middle band) and
the general upper bound (case (b2)) — both remain open after this round.

`results/imo-2026-03/current.md` has been updated with a new "Round 19"
entry summarizing all four builds and the reviewer's independent checks
(appended at the end of the `## Approaches tried` section, matching the
file's existing chronological-append pattern). Three new lemma files were
certified and written to `results/imo-2026-03/lemmas/`:
- `truncated-alternating-sum-ceiling.md`
- `duality-direction-impossibility-theorem.md`
- `alternating-sum-nonnegativity.md`
and one existing lemma file was corrected in place (see below):
- `theorem-34-v1-in-s-p2-v2-lt-s-conditional-closure.md` (hypothesis
  updated from the stale/wrong "$\le n-2$ cuts" to the corrected
  "$\le n-3$ cuts", with a note explaining why the round-18 proof itself
  is unaffected — only the hypothesis narrows).

---

## 1. `greedy-halving-adversary` — VERDICT: CHANGES REQUESTED (Status: partial)

**Claim under most scrutiny: the Theorem 34 cut-budget cap correction,
$n-2\to n-3$.**

Independently re-derived the combinatorics from scratch: producing
$F=\{v_1,v_2\}\cup P$ with $P$ nonempty and exactly-paired (which is forced
whenever $v_1+v_2<p_1$, the genuinely new content of this sub-case) requires
at least 4 pieces cut out of $p_1$ ($v_1$, $v_2$, and at least one matched
pair of 2 elements), and cutting a stick into $k$ pieces costs $k-1$ cuts —
so $\ge3$ cuts are spent on $p_1$ alone, leaving $\le n-3$ for the tail
refinement $R'$, not $n-2$. This combinatorial argument is correct and the
correction is real.

I also independently wrote a fresh script (not reusing the builder's) to
test the actual load-bearing claim: whether $\Delta(n,v):=A(R')-2A(R'_{>v})
\le v-f(n)$ holds under each cap.

```
n   n-2 cap worst margin       n-3 cap worst margin
3   -0.0651  (VIOLATION)        +0.0000887
4   -0.0287  (VIOLATION)        +0.000165
5   -0.0098  (VIOLATION)        +0.000340
6   +0.00876 (no violation in my 3000-trial sample; builder's more
              exhaustive search does find a tiny violation, 271/63500)
```

This independently corroborates the builder's central claim: the $n-2$ cap
is genuinely too generous (real counterexamples exist), and the $n-3$ cap
removes them. (My n=6 sample didn't catch the tiny violation the builder
found under the wrong cap — expected, since violations shrink with n and
the builder used a more targeted/exhaustive search; this doesn't weaken
their claim, it's a sampling-density artifact on my side.)

**Theorem 35a/35b.** Hand-checked the algebra: Fact 1 (alternating-sum
nonnegativity, elementary telescoping-pairs argument) is correct and I
certify it as a standalone lemma (`alternating-sum-nonnegativity.md`). The
doubling identity $p_2=2p_3$ and the cross-level scaling
$D_{n-3}\cdot f(n-3)=2^{n-3}$ check out arithmetically. Theorem 35a's
remark about the $v\in(s',p_3)$ sub-range is a genuine, correctly-resolved
subtlety (they caught their own oversight rather than glossing past it —
good practice). Theorem 35b's use of the *full* strong IH $(\star_{n-3})$
(not just the narrower Claim-A sub-case) is used correctly.

**The honestly-flagged residual gap** (the $\epsilon(v)=1$ bridge from
$\Delta(n,v)$ back to the actual game quantity $A(F\cup G')$ is only
numerically verified, not proven algebraically) is real and correctly
scoped as a gap, not glossed over. The "$p_3$ is cut" branch is honestly
reported as entirely untouched.

**Verdict rationale.** Real, load-bearing progress (a correct bug fix plus
a genuine partial closure of one branch of one sub-case of one sub-case of
the general lower bound), with an honestly-scoped remaining gap. No
overclaim — Status `partial` is accurate. CHANGES REQUESTED: close the
$\epsilon(v)=1$ bridge algebraically and/or the "$p_3$ is cut" branch next.

---

## 2. `minimax-lp-response-polytope` (new slug) — VERDICT: CHANGES REQUESTED (Status: partial)

Independently re-derived the Weak Duality Theorem for LPs from the
two-line argument in §2 (dual feasibility $C^Tλ+A^Tμ\ge w$, $λ\ge0$, dotted
against primal feasibility $f\ge0$, $Cf\le d$, $Af=b$) — this is correct,
standard, and the direction is genuinely one-way: there is no sign
convention that flips it into a lower-bound certificate. The Duality-
Direction Impossibility Theorem's proof is then a direct, correct
application (termwise $\max$ preserves $\le$), so the corollary (no
constraint-dual construction can ever certify case (b2)'s needed *lower*
bound on $\max_F E(F)$) is sound.

The independence-from-`convex-combination-futility-theorem` argument in §4
is a clear, correct structural distinction (primal-value combination vs.
constraint-side duals) — not a restatement.

This is a genuine negative result (a mechanism ruled out, not a positive
closure), correctly reported as `partial`/dead-end for this direction, with
a substantive, well-typed redirection recommendation (§5) rather than a
vague "try again." Certified `duality-direction-impossibility-theorem.md`
as a promotable lemma.

**Verdict rationale.** Correct, complete, honestly-scoped negative result.
No gap in the reasoning itself, but it does not advance toward closing the
problem (it forecloses one mechanism among several already dead). CHANGES
REQUESTED in the sense that the approach's actual assigned target (case
(b2) upper bound) remains fully open — the slug should pivot per its own
§5 recommendation, or be retired if the outline-reviewer judges the
mechanism space for case (b2) exhausted.

---

## 3. `lp-duality-certificate` — VERDICT: CHANGES REQUESTED (Status: partial)

This round was consolidation/bookkeeping only, exactly as the file states.
Spot-checked the surrogate-adversary dead-end lemma
(`lemmas/surrogate-adversary-dead-end.md`): the claim that the ratio-2
ladder tail is not the argmax tail is plausible and stated with appropriate
numeric-only caveats (differential-evolution search, not exact
verification) — correctly NOT overclaimed as an exact/proved fact, only as
strong evidence. This is fine for a numerically-supported dead-end record.

Checked the "Round 19 re-confirmation" itemization (6 items: case (a),
case (b1), Bisect-Top-k, Cross-Piece-Sign-Assignment witnesses, Alternating
Gap-Cross Lemma, and the negative-lemma family) against the cited proofs
earlier in the same file — each item's stated reason for being unaffected
by the "drifting argmax" finding matches what the corresponding proof
actually does (e.g. case (a)'s bound uses the *actual* IH value on the
actual reduced marking, not an assumed tail shape; case (b1) uses the
universal $A(S)\le\max(S)$ fact with no tail-shape reference at all). No
inaccuracy found in this itemization.

**Verdict rationale.** No new positive coverage, no overclaim, correct
bookkeeping. `partial` is accurate (unchanged from before this round). No
new fatal issue. CHANGES REQUESTED only in the trivial sense that Open Gap
1 (case (b2)) remains open and is this slug's own nominal target.

---

## 4. `rank-pigeonhole-budget` — VERDICT: CHANGES REQUESTED (Status: partial for the round-19 §7 cross-check work; Claim (A) itself remains solved and unaffected)

**Note on Status field.** The file's own top-of-file `## Status: solved` is
correctly scoped ("this approach's own target, Claim (A)") and is NOT an
overclaim — Claim (A) was fully and rigorously closed in round 8 and
re-verified by prior reviewers; this round adds no changes to that proof.
The round-19 work (§7) is explicitly out-of-scope cross-check work on the
sibling `greedy-halving-adversary`'s target, and does not affect Claim A's
`solved` status. I re-confirm Claim (A)'s `solved` status is legitimate
(not re-auditing the full round-8 proof this round, per scope, but noting
no red flags in re-reading it).

**Independently verified the Truncated Alternating Sum Ceiling (§7.1):**
$A(S)-2A(S_{>v})\le v$ for any nonnegative multiset $S$, any $v\ge0$. Wrote
a fresh script (200,000 exact-`Fraction` trials, random $S$ and $v$, no
structure): zero violations, worst margin exactly $0$ (equality attained),
matching the claimed equality case $S=\{v\}$. Certified as
`lemmas/truncated-alternating-sum-ceiling.md`.

**Independently re-verified the $n-2$-cap counterexample / $n-3$-cap
corroboration (§7.3/7.4)** with my own script targeting exactly the
inequality $(\sharp)$ they define — found positive margins throughout under
the $n-3$ cap, consistent with their report (see the shared table in §1
above; same underlying mechanism, corroborated from two independent
scripts plus my own third).

**Scrutinized the $n=3$ exact closure (§7.5) for a genuine flaw — found
one, and confirmed by direct computation it is non-fatal.** At $n=3$ the
corrected cap forces $R'=\tau=\{p_3,p_4\}$ (budget 0), and the file
case-splits on $v_2$ vs. $p_3,p_4$. In the case "$v_2\le p_4$" the file
claims $\tau_{>v_2}=\tau$ (both $p_3,p_4$ "exceed" $v_2$) and computes
$\Delta(3,v_2)=-A(\tau)=-f(3)$. **This is wrong exactly at the single
boundary point $v_2=p_4$:** since "exceeds" means strictly greater than,
at $v_2=p_4$ we have $p_4\not>v_2$, so $\tau_{>v_2}=\{p_3\}$ only, giving
the true value $\Delta(3,p_4)=p_4-2p_3=-3f(3)$, not $-f(3)$ as stated. I
verified this by direct computation (script, exact fractions): true
$\Delta(3,p_4)=-1/5=-3f(3)$, not the claimed $-f(3)=-1/15$.

**This does not break the theorem.** The needed inequality is $\Delta(3,
v_2)\le s-(v_1-v_2)$. The file's (incorrect) claimed value $-f(3)$ is
*larger* (less negative) than the true value $-3f(3)$ — so if the file's
argument correctly shows the larger, wrong value satisfies the inequality,
then the true, smaller value satisfies it too automatically (a smaller
LHS makes a $\le$ inequality only easier). I confirmed directly that the
true value $-3f(3)$ does satisfy the bound at $v_2=p_4$. So the $n=3$
closure's *conclusion* is correct and fully rigorous; only the case-split's
description of $\tau_{>v_2}$ at the single measure-zero boundary point
$v_2=p_4$ is imprecise. This is a genuine (small) proof bug, not just
"could be phrased better" — it is exactly the kind of gap this role is
meant to hunt for — but it is not load-bearing: the theorem as stated
survives. I flag it explicitly for the builder to fix (state the case
split as $v_2<p_4$ / $v_2\in[p_4,p_3)$ / $v_2\ge p_3$, or equivalent,
before this lemma is cited elsewhere as unconditionally closed without
caveat).

**§7.6's honest gap** (general $n\ge4$ vertex enumeration re-encounters the
standing cross-piece tie-vertex obstruction) is correctly reported as
incomplete, not glossed over.

**Verdict rationale.** Genuine new general lemma (Ceiling) certified,
correct $n=3$ base case (modulo the flagged, non-fatal boundary
imprecision), honest negative finding (unrestricted-budget counterexample),
honest gap for $n\ge4$. CHANGES REQUESTED: (i) fix the $v_2=p_4$ boundary
case description in §7.5 (cosmetic but should be corrected before further
citation), (ii) attempt the general-$n$ vertex enumeration in §7.6.

---

## Summary table

| Slug | Verdict | Status |
|---|---|---|
| greedy-halving-adversary | CHANGES REQUESTED | partial |
| minimax-lp-response-polytope | CHANGES REQUESTED | partial |
| lp-duality-certificate | CHANGES REQUESTED | partial |
| rank-pigeonhole-budget | CHANGES REQUESTED | partial (Claim A sub-scope remains solved, unaffected) |

**Overall `imo-2026-03` status: partial.** No slug reaches a full solution
of the whole problem this round. The general lower bound's middle band and
the general upper bound's case (b2) both remain open. `current.md` has been
updated accordingly (new Round-19 entry appended; `## Status` remains
`partial`; `## Full proof` remains absent).

## Files touched by this review
- `/home/agentuser/repo/results/imo-2026-03/current.md` (new Round-19 entry appended)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/truncated-alternating-sum-ceiling.md` (new, certified)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/duality-direction-impossibility-theorem.md` (new, certified)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/alternating-sum-nonnegativity.md` (new, certified)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/theorem-34-v1-in-s-p2-v2-lt-s-conditional-closure.md` (corrected in place: stale $n-2$ hypothesis replaced with the corrected $n-3$ hypothesis, so this lemma file can no longer be mis-cited)
