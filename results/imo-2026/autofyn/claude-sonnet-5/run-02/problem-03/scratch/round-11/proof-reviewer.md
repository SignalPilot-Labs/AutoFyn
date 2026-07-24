# Round 11 proof-reviewer report — imo-2026-03

Scope: adversarial re-check of the round-11 additions ONLY (both files have
long, previously-certified histories). Prior-round content re-cited but not
re-litigated unless a new round-11 claim depends on it.

## greedy-halving-adversary — verdict: CHANGES REQUESTED (Status: partial, matches file's own header)

### What was checked and how

1. **Unified Theorem P(n) and its induction.** Read the full write-up
   (`greedy-halving-adversary.md` lines 1856–2107). The branch trace
   (ℓ(F)=0 and new ℓ(F)=2 sub-case (a) use L(n-1); closed ℓ(F)=1
   sub-branches use only L(n-2); no depth used to prove itself) is
   internally consistent and I traced it independently against the cited
   propositions (16, 20–22, 24, 25) — correct. The stated unconditional
   range (n≤3, not n≤4 as the round-11 outline-reviewer's note claimed) is
   the right correction: for n≥4, L(n-1) is needed by the ℓ(F)=0/sub-case-(a)
   branches, and L(n-1) is the *full*, unrestricted statement one level
   down (including ℓ(F)≥3 splits), which is not established for n-1≥3.
   Confirmed by direct substitution that L(0),L(1),L(2) are exactly what's
   already certified (n≤2 fully closed, n=0 trivial).

2. **New Lemma 25 (ℓ(F)=2 exact identity), re-derived from scratch.** I
   wrote an independent verification script. **First attempt found ~99.9%
   "mismatches"** — traced this to my own script bug: I initially computed
   $A(S)$ as the literal claiming-game value (Liu Bang's share,
   $\Sigma_{\text{odd rank}}$), but the file's own Lemma 2 defines
   $A(S):=\sum_i(-1)^{i+1}L_i$ (an alternating sum, $=O-E$, related to the
   game value by $\Phi=(\mathrm{Total}+A)/2$, NOT equal to it). Re-running
   with the file's own convention gave **0/5000 mismatches** over random
   exact-`Fraction` multisets, confirming Lemma 25 is correct as stated and
   proved. (This is exactly the failure mode flagged in a standing
   per-role rule about symbol redefinition across sections — caught before
   it produced a false verdict.)

3. **Sub-case (a) — found a genuine issue: it is VACUOUS for the ladder.**
   The proof requires $v_1,v_2\ge p_2$ where $v_1>v_2>0$ are the two
   odd-multiplicity values of $F$ (a split of $p_1$) and $P$ (the
   exactly-paired remainder) has $\mathrm{Total}(P)\ge0$. Since
   $\mathrm{Total}(F)=p_1$ and (certified) $p_1=2p_2$ exactly, $v_1\ge p_2$
   and $v_2\ge p_2$ force $v_1+v_2\ge2p_2=p_1\ge v_1+v_2+\mathrm{Total}(P)
   \ge v_1+v_2$ — forcing equality throughout, hence $\mathrm{Total}(P)=0$
   and $v_1=v_2=p_2$. But $v_1=v_2$ contradicts the defining condition
   $v_1>v_2$ of $\ell(F)=2$ (equal values would make $\ell(F)=0$, not $2$).
   **I confirmed this exhaustively by direct algebra (above) and by two
   independent randomized-search scripts** (one parametrizing $c=1$ splits
   directly, one allowing arbitrary numbers of exactly-paired residuals):
   zero configurations satisfy sub-case (a)'s hypothesis in tens of
   thousands of trials, consistent with the algebraic proof of vacuity.
   **This means sub-case (a)'s "closure" is a vacuously-true implication**
   (the hypothesis is never satisfiable), not the substantive new content
   the approach file's header claims — it describes sub-case (a) as "a
   genuinely new closed sub-case, same depth as ℓ(F)=0, no new dependency,"
   which overstates its content. This does **not** make Theorem P(n) or
   P(3) false (a vacuous branch trivially holds, and the theorem's
   conclusion is unaffected), but it is an overclaim of significance that
   should be corrected in the next round's exposition — I've written this
   correction into `current.md` and the certified lemma file rather than
   silently letting "new closed sub-case" stand as written.

4. **Sub-cases (b), (c) — honestly open, correctly diagnosed.** Verified
   the algebra of the mixed-regime identity $A(F\cup G')=v_1-A(F_2\cup G')$
   (sub-case (c)) two ways (direct substitution and via Lemma 25 + Prop 20,
   as the file itself cross-checks) — both agree. The file's diagnosis that
   this needs an upper bound on $A(F_2\cup G')$ at *budget $n-1$* (one notch
   worse than anything Prop 21's $(\dagger)$ supplies, since $\ell(F)=2$ can
   arise from as few as $c=1$ cut, not $c\ge2$ as $\ell(F)=1$ forces) is
   correct and precisely traced — this is genuinely new, not previously
   on file.

5. **P(3) full unconditional closure.** I independently re-verified the
   *overall conclusion* (not just each cited branch) with a fresh
   200,000-trial continuum random search over every legal $(F,G')$ pair
   with $\ell(F)\le2$ at $n=3$: **zero violations**, minimum found
   $\approx0.06698$, consistent with (never below) the target
   $f(3)=1/15\approx0.06667$. The vacuity of sub-case (a) noted above does
   not undermine this — the ℓ(F)=0 branch (using already-certified L(2))
   and the genuinely-vacuous-at-n=3 remaining ℓ(F)=1 sub-branches (correct:
   at $n=3$ the tail below $p_3$ is a single piece $\{p_4\}$, with no room
   for the further-refined sub-tail these sub-branches require) are the
   real content, and both check out. **P(3) closure is genuinely, correctly
   established** — I certify this conclusion (see lemma file), while
   explicitly not certifying "sub-case (a)" as meaningful standalone
   content.

6. **Base-case correction of the outline-reviewer's note.** The file
   claims the round-11 outline-reviewer's note ("base case $n\le4$ already
   closed") is imprecise, correct only for individual propositions needing
   $L(n-2)$ alone, not the fully-assembled $P(n)$ once $\ell(F)=0/2$
   (needing the deeper $L(n-1)$) are folded in. I re-traced this and it is
   correct: the honest unconditional range for $P(n)$ is $n\le3$, not
   $n\le4$. This is a genuine, useful self-correction, not an error.

### Overall verdict

The round-11 build's *correctness* is sound (Lemma 25 checks out exactly
once the right $A$-convention is used; the induction's depth-tracing is
right; P(3)'s conclusion is independently confirmed). The one real issue
is a **significant overclaim of substance** in framing sub-case (a) as new
progress when it is vacuous for the ladder — this is exactly the kind of
gap a proof-reviewer should catch, even though it does not sink the
theorem. **Status: partial** (matches the file's own self-report).
**Verdict: CHANGES REQUESTED** — close sub-cases (b)/(c), attack ℓ(F)≥3,
and correct the sub-case (a) framing (recommend restating it as "vacuous,
no content" rather than "closed").

## lp-duality-certificate — verdict: CHANGES REQUESTED (Status: partial, matches file's own header)

### What was checked and how

1. **Zero-Pin Harmlessness Lemma.** Trivial, fully general fact (appending
   zero-valued elements never displaces any positive element's sorted
   rank). Re-derived from scratch, agrees exactly with the file's proof.
   Correct.

2. **Corrected Simplex Vertex-Maximization Lemma (pin set includes 0).**
   Cross-checked the *original* (round-10) boxed statement against its own
   proof: the boxed statement (line ~810) restricts pins to
   $\{\tau_1,\dots,\tau_r\}$, but the proof (line ~830) explicitly defines
   $\mathcal R:=\{0,\tau_1,\dots,\tau_r\}$ and uses boundary case "(i) $f_j$
   hits 0" throughout — confirming the round-10 gap was real and the
   round-11 fix (adding 0 to the boxed pin set, changing nothing in the
   proof) is exactly the right repair. **Independently re-verified with a
   robust multi-start Nelder-Mead continuum optimizer** (my first, quick
   single-start attempt produced 3 of 20 spurious "mismatches" that turned
   out to be pure optimizer artifacts — unconstrained-scale blowups and a
   shallow local optimum, not real gaps in the lemma; a corrected
   multi-restart optimizer with tight tolerances reproduced the vertex
   family's value exactly in all 20 fresh random test cases). **Certified.**

3. **Witness reclassification — independently recomputed both witnesses
   from scratch by brute-force vertex enumeration** (not trusting the
   builder's numbers): at $(3/8,1/4,1/4,1/8)$, trisecting $p_1$ gives
   $\Phi=1/2\le a_3T=8/15$ **exactly** — confirms this witness **is**
   solved by a cut-$p_1$-only strategy, contradicting the old claim that
   both witnesses defeat "cut $p_1$ only." At $(2/5,3/10,1/5,1/10)$, an
   independent brute-force enumeration over $k\in\{1,\dots,4\}$ and all
   pin-patterns from $\{0\}\cup\tau$ gives a minimum of exactly $11/20=0.55$
   — matching the builder's figure exactly and confirming this witness
   **does** genuinely defeat every cut-$p_1$-only strategy ($0.55>8/15$).
   **Both halves of the round-11 correction are confirmed correct** by
   independent computation, not just re-reading the builder's numbers.

4. **Per-Piece Vertex Decomposition Theorem.** The proof is a standard
   "each block of a jointly-optimal product-space point is itself optimal
   given the rest" contradiction argument; re-checked the logic (the only
   load-bearing fact is that pieces' legal move spaces are mutually
   independent, i.e. $\mathcal Q=\prod_i\Delta_i$ is a literal product —
   true by the game's own rules, since Xiang Yu cannot move mass between
   original pieces). Spot-checked numerically: for a 3-piece marking with a
   mixed composition (piece 1 gets 1 cut, piece 2 gets 1 cut, piece 3 gets
   0), found the joint global minimizer of $\Phi$ via a multi-start
   optimizer and confirmed piece 1's own split, holding the rest fixed, is
   itself $\Phi$-minimizing (no unilateral improvement found by a fine
   scan). Consistent with the theorem. **Certified.**

5. **Honest scope.** The file correctly does not claim a general-n
   evaluation of the joint vertex family against $a_nT$ — this remains
   explicitly open, and the diagnosis of why the ladder-specific tools
   (Ratio-2 Spacing Lemma, Last-Element Bound) don't transfer to arbitrary
   markings is sound (no fixed numeric threshold analogous to the ladder's
   $p_1=2p_2$ midpoint exists for an arbitrary marking; the equal-pieces
   marking is correctly flagged as the natural hard test case, consistent
   with two prior unrelated mechanisms already failing there).

### Overall verdict

All round-11 claims independently re-verified and found correct — no
overclaims, no gaps found in the new material. This is genuine progress:
a real gap (round-10's pin-set omission) is now closed, not just
patched around, and a real factual error (both witnesses "requiring
tail-touching") is corrected with an independently-confirmed replacement
claim. The upper-bound program's central open item (evaluating the general
vertex family against $a_nT$) remains open, as honestly reported.
**Status: partial** (matches the file's own header). **Verdict: CHANGES
REQUESTED** — the natural next target is the general evaluation problem
(§R11.5's open gap 0), which the file itself identifies as the genuinely
hard remaining content.

## Lemmas certified this round

- `results/imo-2026-03/lemmas/l2-general-exact-identity.md` (Lemma 25,
  greedy-halving-adversary) — new, fully certified.
- `results/imo-2026-03/lemmas/p3-unified-restricted-claim-b-closure.md`
  (P(3) closure, greedy-halving-adversary) — certified for its overall
  conclusion, WITH a correction note that "sub-case (a)" is vacuous for the
  ladder and not separately certified as meaningful content.
- `results/imo-2026-03/lemmas/simplex-exchange-smoothing-vertex-
  maximization.md` — REWRITTEN and certified with the round-11 pin-set
  correction, superseding the round-10 version that was left uncertified
  with a gap note.
- `results/imo-2026-03/lemmas/zero-pin-harmlessness-lemma.md` — new,
  certified.
- `results/imo-2026-03/lemmas/per-piece-vertex-decomposition-theorem.md`
  — new, certified.

## current.md

Updated with a new "Round 11" entry under `## Approaches tried` summarizing
both builds, the vacuity finding, and the certified lemma list. `## Status`
remains `partial` (unchanged, correctly).

## Ranking

`record_outcome` called for both slugs:
- `greedy-halving-adversary`: outcome `partial` (real progress, but the
  headline "new closed sub-case" claim was found to be vacuous/overclaimed;
  net still a genuine narrowing via Lemma 25 and the P(3) closure).
- `lp-duality-certificate`: outcome `advanced` (closed a real prior gap —
  the pin-set omission — plus a correct factual correction and a genuinely
  new general theorem, no issues found).

## Independent scripts used (this round, not the builders' own)

- `/tmp/check_l25.py`, `/tmp/check_l25b.py` — Lemma 25 verification (first
  version buggy on $A$-convention, second version correct, 5000/5000 match).
- `/tmp/check_subcases.py` through `/tmp/check_subcases4.py` — sub-case (a)
  feasibility search, confirming vacuity.
- `/tmp/p3_check.py`-equivalent inline script — 200,000-trial P(3) overall
  continuum check (zero violations).
- Witness reclassification brute-force enumeration (both witnesses,
  independent from the builder's script).
- Corrected multi-start Nelder-Mead vs. finite-vertex-family comparison for
  the corrected Simplex Vertex-Maximization Lemma (20 fresh random cases,
  zero mismatches after fixing my own optimizer's robustness).
- 3-piece mixed-composition numeric spot-check of the Per-Piece Vertex
  Decomposition Theorem.

## Final verdicts

- **greedy-halving-adversary: CHANGES REQUESTED** (Status: partial).
- **lp-duality-certificate: CHANGES REQUESTED** (Status: partial).

Neither is a whole-round gate — both route independently per CLAUDE.md;
this is a normal mixed (here: uniform CHANGES REQUESTED) result, not a
failed round. No APPROVE this round; the overall problem `imo-2026-03`
remains `partial`.
