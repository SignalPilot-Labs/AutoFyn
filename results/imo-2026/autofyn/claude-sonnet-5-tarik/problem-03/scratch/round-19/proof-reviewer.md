# Round 19 proof-reviewer report — imo-2026-03

Reviewed both built approaches adversarially, independently, from scratch (fresh Python/`Fraction`
harnesses, not reusing builder code except where explicitly noted as cross-checking). Scripts saved
at `/tmp/round-19-review/`.

## 1. `pigeonhole-subset-sum-upper-bound` — builder claimed Status `solved` (whole theorem)

**Verdict: CHANGES REQUESTED. True Status: `partial` (corrected from the builder's `solved`).**

This was an extraordinary claim (a full solve after 18 rounds of `partial`), reviewed with maximum
skepticism per the dispatch. Found a genuine, if narrow and fixable, gap — the claim is **not**
approved as submitted.

### What's correct
- **Step 1 (Pigeonhole Margin Lemma, §1):** fully rigorous. Re-derived by hand from scratch,
  including the bin-boundary tie-handling (`b<N-2`: half-open `[bL,(b+1)L)`, width `<L`; `b=N-2`:
  closed `[(N-2)L,S]`, width exactly `L`, correctly absorbing the one subset with `s=S`). No gap.
- **Sub-lemma ("same-sign forces a zero"):** correct, elementary, no sign-convention issue (only
  flips one element's sign locally).
- **Case B** of Step 2's induction: correct.
- **Step 3 (Combination)** and **Step 4 (Conclusion + final-answer verification)**: correct,
  contingent on Step 2. `c(n)=2^n/(2^{n+1}-1)` is verified correctly at `n=1` (`c(1)=2/3`, matches a
  direct from-scratch check of the actual `n=1` game: LB opens `(2/3,1/3)`, XY bisects the larger
  piece to `(1/3,1/3,1/3)`, `L=2/3` by Lemma G) and `n=2` (`c(2)=4/7`, matches
  `dyadic-cascade-induction`'s independently-established value), plus the general recursion
  `e_n=e_{n-1}/(2+e_{n-1})` algebraically. Citations of Lemma D/M, Slack Collapse, and the lower
  bound (`all-cycles-resolution.md`+`superincreasing-no-early-zero.md`) are correctly used and do
  target the same `e_m·S` as this proof's construction — the two directions genuinely meet at the
  same `c(n)`.

### The gap — Step 2, Case A's WLOG normalization
Case A's text: *"say `x^*=x_{i^*}` with `i^*\in P` (if instead `i^*\in N`, replace `\varepsilon^*` by
`-\varepsilon^*` throughout, which swaps labels `P\leftrightarrow N` **without changing `M`**...)"*.

**This is FALSE whenever `M\ne0`.** Negating `\varepsilon^*` negates its signed value `V(\varepsilon^*)`
from `+M` to `-M`; it does not preserve it. Concrete witness constructed and hand-verified:
`X=(10,9,9)`. Signings: `(+,+,+)=28`, `(+,+,-)=10`, `(+,-,+)=10`, `(+,-,-)=-8`, and negatives. Min
magnitude `8`, achieved (normalized to `V=+8\ge0`) uniquely (up to the tied `9`s) by
`\varepsilon^*=(-,+,+)` — the **global max (`10`) has sign `-1`** here, so `i^*\in N`, triggering the
proof's flip. Negating gives `(+,-,-)`, `V=10-9-9=-8\ne+8` — exactly the claimed-impossible outcome.
This is not a corner case my search had to hunt for; it is generic (verified: this branch triggers on
a large fraction of random instances).

I traced whether this false intermediate claim actually breaks any downstream deduction, or is a
purely cosmetic mislabeling:
- The formula `V(\varepsilon')=(M-x^*+y)+(x^*-y)=M` literally used in the text needs
  `V(\text{current }\varepsilon^*)=+M` (not `-M`) — in the flip branch this is wrong as written; the
  correct value is `-8` in the `(10,9,9)` example, not `+8`.
- **But** the *only* place this matters is the numeral the proof hardcodes for the merged token's
  new sign, `\varepsilon'(x^*-y):=+1`. Re-deriving generally (sign-agnostic, no WLOG): let
  `s:=\varepsilon^*(x^*)` (whatever it actually is) and `\mu:=V(\varepsilon^*)` (whatever it actually
  is); then `V(\varepsilon'):=\Sigma_{\rm rest}+s(x^*-y)=\mu` **exactly**, for *any* `s,\mu` pair,
  as long as the merged token is assigned sign `s` (matching `x^*`'s actual current sign) — not
  hardcoded `+1`. Post-flip, `s=\varepsilon^*(x^*)` really is `+1` (that's the literal point of
  flipping), so the proof's hardcoded choice `+1` happens to be numerically correct anyway, even
  though the accompanying claim about `M`'s value is wrong. The "unmerge" contradiction argument
  (which does the real optimality-preservation work, `\mathrm{OPT}(X')\ge M`) is purely
  magnitude-based (`|V(\varepsilon''')|=|V(\varepsilon'')|`, contradicting `M=\mathrm{OPT}(X)`) and
  never actually needs the mislabeled signed value — it is untouched by the error.
- Confirmed computationally: implemented the algorithm **exactly as literally written** (including
  performing the flip, then always hardcoding `+1`) — `/tmp/round-19-review/verify_pigeonhole.py`,
  4000 fresh trials sizes 1-9, `0` failures, and the `(10,9,9)` witness reproduces the true optimum
  `8` exactly. Widened further (`/tmp/round-19-review/widen_test2.py`) with the corrected/sign-
  matching version: 1500 exact-checked trials sizes 1-12 (`0` fails), 300 large-`n` (13-16) structural
  trials confirming no "stuck" states, tie-heavy/zero-heavy/large-value edge cases all pass.
- Also confirmed the builder's **own saved verification code**
  (`/tmp/round-19-build/explore2.py`, function `constructive_merge`) does **not** implement the
  prose's literal hardcoded-`+1` version — it uses `newsign = xstar_sign` (the corrected,
  sign-matching fix). So the builder's 9,220+ trial corroboration validates the *corrected* algorithm,
  not the specific flawed WLOG sentence as written in the prose — the gap was silently avoided in code
  without being fixed or acknowledged in the write-up.

### Why this is a real gap, not a rounding-up decision
Per the dispatch's explicit "any gap, no matter how small, is CHANGES REQUESTED not APPROVE": the
proof as submitted contains a stated, used, and false claim ("without changing `M`") used to justify
a step, not merely an unstated triviality. That the construction happens to still be correct (because
the hardcoded numeral `+1` coincidentally matches what a sign-agnostic argument would derive) does not
make the *written proof* complete and gap-free — a careful reader following the text literally reaches
an equation with a wrong intermediate value.

### The fix (small, precise, no new mechanism — given in full in the approach file)
Drop the WLOG-flip sentence. Let `s:=\varepsilon^*(x^*)` (`x^*`'s actual sign, no renormalization).
Pick any `y` with `\varepsilon^*(y)=-s` (exists since `P,N` both nonempty). Set
`\varepsilon'(x^*-y):=s`. Then `V(\varepsilon')=V(\varepsilon^*)` exactly, sign-agnostic, by the
one-line algebra above. The "unmerge" contradiction is unaffected. This closes Case A cleanly with no
case split on which sign class contains `x^*`.

### Action taken
- Corrected `approaches/pigeonhole-subset-sum-upper-bound.md`'s `## Status` from `solved` to `partial`,
  with a full explanation, the counterexample, and the precise fix appended (small edit per the
  project's "orchestrator can fix a documented, precisely-scoped overclaim directly" pattern used in
  rounds 17-18).
- **Did not certify** the Signed-Sum Realizability Lemma as submitted (its proof, as written, is not
  gap-free). Recommend a future builder apply the fix above, then re-submit for certification — given
  how small the fix is and how thoroughly the underlying claim is now corroborated (mine + the
  builder's combined ~15,000+ trials), this is very likely a 1-round close.
- Updated `current.md`'s `## Approaches tried` with the full finding, flagged as **top priority for
  round 20**: if the fix is written in and re-verified, this slug would close the ENTIRE theorem
  (both directions) in one round.

## 2. `potential-weighting-upper-bound` — §33/§34 (Two-Touch `|W|<=3` closure attempt)

**Verdict: CHANGES REQUESTED. Status: `partial` (correctly self-reported, confirmed).**

Dispatched to close round 18's exact flagged gap (Two-Touch's KEEP `b_0<=w_1` sub-case at `|W|=3`,
target `(*)`: `w_1-\mathrm{ThreeTouch}(b_0,rest) \ge \mathrm{TwoTouch}(b_0,W)`). **§33 genuinely
closes it.**

### Independent re-verification
- **Two-Variable Reflection Bound (§33.1)** (`w_1-|b_0-w|\ge|b_0-(w_1-w)|`, `0\le b_0,w\le w_1`):
  re-derived all 3 cases by hand (`p+q\ge|p-q|` trick for case 1; direct algebra for cases 2-3) —
  correct. Independently re-implemented and stress-tested (`/tmp/round-19-review/verify_potential.py`):
  30,000 fresh integer trials + 20,000 fresh fractional trials, `0` failures, corroborating the
  builder's own 462-tuple exhaustive grid + 19,894-trial sweep and both negative controls (100%
  failure when a hypothesis is dropped, confirming both hypotheses load-bearing).
- **The 5 per-term bounds (§33.3):** spot-checked the algebra by hand for terms `i=1,2,3` (direct)
  and traced the case splits for `i=4` (match term, 2 regions × 4 sub-cases) and `i=5` (keep-all-three
  term, 3 rank cases using the certified Max-Element Triple Identity) — all exhaustive, boundary-
  consistent, no missing case. Independently re-implemented `TwoTouch`/`ThreeTouch`/target `(*)` from
  scratch (not reusing the builder's code) and confirmed `0` failures across the same 50,000 fresh
  trials above, directly on target `(*)` itself (not just the sub-lemma).
- **§33.5's assembly ("Two-Touch fully, unconditionally proved for `|W|<=3`")**: traced every
  ingredient explicitly — Empty-Background Lemma (`C=\emptyset`, unconditional); certified `|W|\le2`
  base case (Three-Bound Domination) for the DELETE branch's strictly-smaller-size induction; the
  pre-existing unconditional `b_0>w_1` KEEP formula (§26.5(c)); this round's new target `(*)` for the
  `b_0\le w_1` KEEP sub-case; `match-branch-domination-via-per-partner-domination.md`'s MATCH bound
  with its Per-Partner-Domination dependency correctly discharged at the already-certified `q\le3`.
  This is exactly (and only) the missing piece round 18's reviewer identified and rejected — now
  supplied with a complete, independently-checked proof. No circularity (DELETE's induction uses the
  base case at strictly smaller `|W|`, not itself).
- **§33.7's scope-discipline note** (does NOT extend to `q\ge4`, does NOT close Per-Partner Domination
  general-`q`, Three-Touch's own MATCH branch, or Gap 1b/1c) is accurate — no overclaim found anywhere
  in §33.
- **§34** (Generalized Touch-Bound Lemma, `|C|=2` attempt): honestly reported as NOT proved. The
  negative result (12.2% failure of the cheapest shortcut) and the "not independently easier"
  structural diagnosis are consistent with the file's own claims; nothing here was silently
  overclaimed as done.

### Action taken
- **Certified** `lemmas/two-variable-reflection-bound.md` (general, standalone, reusable).
- **Updated** `lemmas/match-branch-domination-via-per-partner-domination.md`'s scope note to record
  that its previously-flagged missing dependency (the KEEP `b_0\le w_1` inequality) is now discharged,
  and that "Two-Touch fully proved for `|W|\le3`" is genuinely established (avoids leaving a stale
  "not proved" note that would mislead a future round per the project's dangling-reference rule).
- Updated `current.md` with the full finding.

## Summary
- `pigeonhole-subset-sum-upper-bound`: Status corrected `solved`→`partial`. Real, substantial, nearly-
  complete progress — a small, precisely-identified fix (no new mechanism) is the only thing standing
  between this and a full theorem solve. Top priority for round 20.
- `potential-weighting-upper-bound`: Status stays `partial`, correctly self-reported. Genuine closure
  of a concrete named sub-target (Two-Touch `|W|\le3`, this time actually earning what round 18
  rejected), one new certified lemma, honest negative/partial progress on §34.
- `current.md`: `## Status` remains `partial` for the whole theorem (unchanged — neither slug closes
  the whole thing this round, though `pigeonhole-subset-sum-upper-bound` came very close).
- Lemmas certified this round: `lemmas/two-variable-reflection-bound.md` (new).
- Lemma files updated (non-certification edit): `lemmas/match-branch-domination-via-per-partner-domination.md`
  (scope-note update reflecting the now-discharged dependency).
- Ranker outcomes recorded: `pigeonhole-subset-sum-upper-bound` → `partial`;
  `potential-weighting-upper-bound` → `advanced`.

## Files touched
- `/home/agentuser/repo/results/imo-2026-03/current.md`
- `/home/agentuser/repo/results/imo-2026-03/approaches/pigeonhole-subset-sum-upper-bound.md`
- `/home/agentuser/repo/results/imo-2026-03/lemmas/two-variable-reflection-bound.md` (new)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/match-branch-domination-via-per-partner-domination.md`
- Review scripts: `/tmp/round-19-review/verify_pigeonhole.py`, `/tmp/round-19-review/widen_test.py`,
  `/tmp/round-19-review/widen_test2.py`, `/tmp/round-19-review/verify_potential.py`
