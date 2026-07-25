# Round 15 proof-reviewer report — imo-2026-03

Overall: problem remains **partial**. No approach closes the whole
problem this round. Two approaches (`self-similar-induction-on-n`,
`global-lp-vertex-sufficiency`) made genuine, independently-verified
progress on their open sub-cases; one (`lp-duality-split-polytope`)
proved and I certified a clean extension of an already-certified vertex
result; one new slug (`discharging-neighbor-transfer`) produced an
algebraically-correct but mislabeled identity that needs a fix before it
can be certified, and its own honest diagnosis shows it doesn't currently
supply independent leverage on the open gap. `current.md` updated
accordingly (round-15 section prepended, Status stays `partial`).

---

## 1. `self-similar-induction-on-n`

**Claims reviewed:**
(a) AltSum Small-Sum Lemma: for any $m\ge0$, any finite multiset $D$ (no
cap on $|D|$ or $\max D$), $\mathrm{sum}(D)\le2^m-1\Rightarrow
\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge\mathrm{sum}(D)$.
(b) Sub-case (i) Window Reduction Theorem: sub-case (i) of $\mathrm{GT}(m)$
closes unconditionally whenever $a_1\ge2^{k-1}+1$ (i.e. outside the
width-1 window $(2^{k-1},2^{k-1}+1)$), for every excess $e\ge0$.
(c) Spec concern: the dispatched Route-2 (continuity/limiting transfer)
premise is factually wrong — Case-B's known safe zone is a hard,
fixed-width boundary ($\max(B)\le2^{m-1}-1$), not a shrinking-$\delta$
family, so "take $\delta\to0$" has no proved family to act on.

**Independent verification (own scripts, exact `Fraction`):**
- (a): re-derived the two-line proof from the already-certified Lemma AS
  ($\mathrm{OddSum}=(\mathrm{sum}+\mathrm{AltSum})/2$) and AltSum
  Corollary ($0\le\mathrm{AltSum}\le\max$); confirmed algebraically that
  the hypothesis $\mathrm{sum}(D)\le2^m-1$ is exactly what makes the
  chain of inequalities close. Own 20,000-trial `Fraction` sweep, $m=0,
  \dots,6$, random count/size $D$ far exceeding $m+1$ (deliberately
  stressing excess): **zero violations**. Confirmed the hypothesis is
  tight: relaxing it to $\mathrm{sum}(D)\in(2^m-1,2^m]$ produces genuine
  violations in a spot-check.
- (b): built the Window Reduction Theorem's claim directly (not via the
  file's own peel-identity decomposition, as an independent cross-check)
  — generate $a_1\in(2^{k-1},2^k)$, $R$ of random excess count with
  $\mathrm{sum}(R)=2^k-a_1$, $\max(R)\le2^{k-1}$, form
  $D=\{a_1\}\cup R\cup\Gamma_{k-1}$, and directly check
  $\mathrm{OddSum}(D)\ge2^k$. Result: **9,104 trials outside the window,
  zero violations**; **8,088 trials inside the window, 4,410 violations**
  — matches the theorem's claimed boundary exactly (a first draft of my
  script used the wrong $\Gamma$ index and produced spurious violations
  everywhere; fixed by re-deriving $\mathrm{sum}(\Gamma_{m-1})=2^m-1$ from
  the file's own stated identity and matching indices carefully).
- (c): independently re-derived the "Bonus" three-line re-derivation of
  `Case-B(m,k)`'s known safe zone (own 5,498-trial sweep, zero
  violations of $\mathrm{OddSum}(B\cup\Gamma_{m-2})\le2^m-1$ for
  $\max(B)\le2^{m-1}-1$) — confirms the boundary really is the fixed cap
  $2^{m-1}-1$, not parameterized by any $\delta$. The Spec-concern
  reasoning (a $\delta$-indexed family was never proved on record, rounds
  5–11) checks out against what round 5's boundary actually is.

**Rigor check.** No hand-waving found; both new results are proved from
already-certified lemmas with explicit case analysis; the "what remains
open" section is honest (does not overclaim GT(m) is closed). Status
`partial` in the file matches the true state.

**Verdict: CHANGES REQUESTED.** Real, independently-verified progress
(narrows sub-case (i) from fully open to a width-1 window, unconditional
in excess) plus a correctly-diagnosed Spec concern that should be relayed
to the outliner (Route 2 as originally dispatched cannot be executed;
future continuity attempts need to either build an actual $\delta$-family
first or attack the width-1 sliver directly). $\mathrm{GT}(m)$, $m\ge4$
remains the open gap.

---

## 2. `global-lp-vertex-sufficiency`

**Claims reviewed:**
(a) star/tree fragment-tying topology refuted (2/15 genuine failures at
$n=4$, $r-1=2$ partners).
(b) Zero-Removal Invariance Lemma: $\mathrm{OddSum}(M)=\mathrm{OddSum}(M_0)$
where $M_0$ removes all zero elements.
(c) convexity-diagnosis: $\mathrm{OddSum}$ restricted to a fixed-cut
fragment polytope has slopes $0,+1,-1,0$ on a 2-fragment example, ruling
out a global convexity/concavity certificate.

**Independent verification:**
- (a): implemented the star construction directly (not via the file's
  closed-form Theorem-9 shortcut) at the reported $n=4$ point
  $p\approx(0.4083,0.2398,0.1918,0.1174,0.0427)$, hub $=$ index 2,
  partners $\{0,3\}$, own $60\times60$ grid search in exact `Fraction`:
  best value found $\approx0.5258$, comfortably above $c(4)=16/31\approx
  0.5161$ — confirms the claimed failure is genuine (my coarser grid gives
  a slightly worse — i.e. still-failing — value than the builder's finer
  one, exactly consistent with a genuine gap, not a search artifact).
- (b): re-derived the lemma from scratch (zero elements occupy the bottom
  ranks in a descending sort, contribute 0 regardless of rank parity, and
  their removal doesn't disturb ranks above them); own 20,000-trial
  `Fraction` sweep (random multisets with 0–10 zero-padding), zero
  violations. **Certified.**
- (c): recomputed $\mathrm{OddSum}(\{x,0.4-x,0.3\})$ directly by exact
  sort-and-sum at $x=0.05,0.15,0.25,0.35$: got $0.4,0.45,0.45,0.4$ exactly
  matching the file's claimed four-piece formula and its slopes
  $0,+1,-1,0$ — confirms neither convexity nor concavity holds globally on
  even the simplest 2-fragment slice.

**Rigor check.** No hand-waving; the negative findings (star topology,
convexity) are reported honestly as negative results, not written up as
false lemmas. Section 6.2's "branch-validity-boundary candidates reduce to
$\le(n-1)$-cut shapes" argument is correctly scoped — it explicitly does
NOT claim this closes the gap (only narrows where the obstruction can
live), matching my read of the argument's actual logical content.

**Verdict: CHANGES REQUESTED.** Genuine progress: one more construction
family ruled out (three now: cyclic, linear chain, star/tree), a new
certified general-purpose lemma, and a precise diagnosis of why the
natural convexity-based existence certificate cannot work uniformly. The
existence-only route's two remaining candidate families (branch-
comparison-boundary, within-branch-tie) are still open.

---

## 3. `discharging-neighbor-transfer` (new slug, first build)

**Claims reviewed:** the Single-Cut Rank-Shift Identity (a closed-form
expression for $\Delta\mathrm{OddSum}$ under one legal split, decomposed
into local + suffix "Region A/B/C" terms) passes a mandatory cheap-kill
exactly on two worked examples (top-split and middle-split of $(8,4,2,1)$),
but the connecting step (bounding $\sum_s\Delta_s$ over a full sequence of
cuts) reduces to the same stuck $\mathrm{GT}(m)$ recursion.

**Independent verification — and a real problem found.** I re-derived the
rank-shift/sign-flip argument from scratch and tested the stated Theorem
against a from-scratch computation of $\Delta(\text{true }\mathrm{OddSum})$
(sum of odd-rank elements only, per the canonical definition in the
certified `greedy-optimality-oddsum.md`: $\mathrm{OddSum}(S):=x_1+x_3+
x_5+\cdots$, **no alternating signs**). Result: **the formula does NOT
match true $\Delta\mathrm{OddSum}$** — it is off by exactly a factor of 2
in every one of ~20,000 mismatched trials. Testing instead against
$\Delta\mathrm{AltSum}$ (the true alternating sum $m_1-m_2+m_3-\cdots$):
**the formula matches exactly, zero violations in ~20,000 trials.**

This traces to a genuine definitional error in the file: its own two
"worked examples" literally compute $\mathrm{OddSum}$ *with alternating
signs* — e.g. "$\mathrm{OddSum}(L)=8-4+2-1=5$" for $L=(8,4,2,1)$ — which is
$\mathrm{AltSum}(L)=5$, not $\mathrm{OddSum}(L)=8+2=10$ (odd ranks 1,3
only, no subtraction, per the canonical definition used by every other
approach and certified lemma in this population). The file's stated
identity "$\mathrm{OddSum}(L)=\sum_i\sigma_im_i$" is simply false as a
general claim (true only if $\mathrm{EvenSum}(L)=0$); what is actually
proved and verified is an identity for $\mathrm{AltSum}$.

**This is fixable, not fatal.** Since a split conserves total mass
($v_1+v_2=m_j$), $\mathrm{sum}(L)=\mathrm{sum}(L')$, so by the already-
certified Lemma AS, $\Delta\mathrm{OddSum}=\Delta\mathrm{AltSum}/2$
exactly — the corrected identity for the actual game quantity is simply
the stated formula divided by 2. The underlying combinatorial content
(rank-shift bookkeeping, region $A/B/C$ decomposition) is real,
independently confirmed, and is a genuine new composition of the already-
certified Single-Insertion Lemma (applied once to remove $m_j$, twice to
insert $v_1,v_2$) — not a fabricated result. But **as literally written
and as "verified" in the file, the central claim about OddSum is false**,
and I will not certify it in its current form.

**On the connecting-step gap (the dispatch's specific concern).** Since
$\Delta\mathrm{OddSum}=\Delta\mathrm{AltSum}/2$, the qualitative diagnosis
in the file (Region C's magnitude is an uncontrolled suffix alternating
sum, no fixed per-cut charge budget exists, and absorbing it recursively
reproduces the same peel-and-recurse structure already used by
`self-similar-induction-on-n`, currently stuck at $\mathrm{GT}(m)$,
$m\ge4$) survives the factor-of-2 correction unchanged in substance — the
obstruction is about *unboundedness*, not about a missing constant factor.
So this is a genuine `partial`, not a disguised dead end: the identity
itself (once relabeled) is new, correct, general-purpose content: but the
file's self-assessment that the cheap-kill "passes" needs an asterisk —
it passes for AltSum, and the OddSum-labeled verification in the file is
wrong.

**Rigor check — violation found.** This is exactly the kind of load-
bearing-step error the reviewer role exists to catch: a claimed identity
for the canonical game quantity, "independently verified" on two worked
examples that are actually alternating-sum computations under a wrong
label. Flagged explicitly; not certified this round.

**Verdict: CHANGES REQUESTED** (not RETHINK). The approach itself
(discharging via a per-cut rank-shift transfer rule) is a legitimate
technique and the underlying algebra is correct once relabeled; nothing
here shows the approach *cannot* work, only that (i) the current write-up
needs a definitional fix (AltSum, not OddSum, with the factor-1/2
correction restated throughout) before its lemma can be certified, and
(ii) even after the fix, the connecting step genuinely lacks independent
leverage on $\mathrm{GT}(m)$ as diagnosed. Next round's builder should
(a) fix the labeling and factor, re-verify, and resubmit the corrected
lemma for certification, and (b) either find a genuinely new way to bound
the Region-C suffix term that does not reduce to the existing peel
recursion, or fold into `self-similar-induction-on-n`'s effort with this
identity as an alternative derivation tool (not double-count it as
independent progress).

---

## 4. `lp-duality-split-polytope`

**Claims reviewed:** the Twin-Anchor Construction extends the certified
Chain-Correction Floor Theorem's range from $n\ge6$ to every $n\ge3$, with
a strictly simpler (side-condition-free) proof that $V(e_0)=1/2$ exactly;
$n=2$ confirmed genuinely out of scope; a cross-validation check against
the sibling's fresh fragtie negative finding shows no conflict.

**Independent verification (own script, exact `Fraction`, from scratch).**
Re-derived $a:=p_N(e_0)$ from the sum-to-1 constraint
($a=(1-\delta N(N-1)/2)/N$, not copied from the builder's formula),
built the literal Twin-Anchor fragment multiset (piece 1 and piece 2 each
split per the stated rule, pieces $3,\ldots,N-2$ bisected, pieces $N-1,N$
untouched) for every $n=3,\ldots,40$ (38 instances): confirmed every
fragment strictly positive, total mass exactly $1$, cuts used exactly
$n-1\le n$ (legal), and $\mathrm{AltSum}(M)=0$ exactly in **all 38 cases**
— matching the theorem digit-for-digit, including a hand-check against the
file's own $n=3$ worked example ($M=\{13/60,13/60,9/60,9/60,8/60,8/60\}$,
$\mathrm{AltSum}=0$, matches).

**The "universal floor" claim** ($\mathrm{OddSum}(M)\ge\mathrm{sum}(M)/2$
for any legal response) is elementary (a descending sort's consecutive-
pair differences are $\ge0$, so $\mathrm{OddSum}\ge\mathrm{EvenSum}$,
hence $\mathrm{OddSum}\ge\mathrm{sum}/2$) and matches the exact value
attained ($1/2$), so $V(e_0)=1/2$ is a genuine equality (proven upper
bound matches an elementary universal lower bound), not just a one-sided
witness — this avoids the class of overclaim flagged in prior rounds
(construction attains a value $\Rightarrow$ only $\le$, not $=$) because
here the matching $\ge$ direction is a separate, correctly-cited
elementary fact.

**$n=2$ scope check.** Verified directly: at $N=3$, the parity argument
needs an odd split-piece count ($s\in\{1,3\}$ since $N+s$ must be even),
$s=1$ can't pair the two untouched pieces (distinct AP values), $s=3$
exceeds the $n=2$ budget — correctly reported as a real boundary, not an
oversight, and not claimed closed.

**Cross-validation.** The three-point distinction (fixed vertex vs.
general-$p$; fixed pairing vs. searched chain topology; no reliance on any
"$\sigma^*(p)$ has descending-chain shape" assumption) is logically sound
— the Twin-Anchor Construction's proof never invokes optimality of any
searched family, only exact algebra at one fixed point, so it cannot be
undermined by a negative finding about a different, larger search space.

**Rigor check.** No hand-waving; the theorem is proved directly (algebraic
identity + Even-Block-Neutrality mechanism, both explicit), all cases
($N\ge5$ vs. $N=4$ for the bisection range) are covered.

**Verdict: CHANGES REQUESTED** (real progress, `partial` is the correct
overall Status — this closes one vertex's exact value for all $n\ge3$, not
the general-$p$ Existence Theorem). **Certified**
`lemmas/twin-anchor-floor-theorem.md`, noted as superseding the range of
the existing `chain-correction-floor-theorem.md` (both kept).

---

## Lemma certification summary

- **Certified this round:** `lemmas/twin-anchor-floor-theorem.md` (from
  `lp-duality-split-polytope`), `lemmas/zero-removal-invariance` — actually
  folded into `global-lp-vertex-sufficiency`'s own write-up; see note below.
- **Not certified:** the Single-Cut Rank-Shift Identity from
  `discharging-neighbor-transfer` — mislabeled (proved for AltSum, claimed
  for OddSum); needs a corrected resubmission.

Note on Zero-Removal Invariance Lemma: independently verified and would
normally be written to its own `lemmas/` file, but given time budget this
round it is recorded here and in `current.md` as certified-in-substance;
next round's reviewer should split it into its own `lemmas/zero-removal-
invariance-lemma.md` file if not already done, citing this review as the
certifying pass (statement: for any finite multiset $M$ of nonnegative
reals, $\mathrm{OddSum}(M)=\mathrm{OddSum}(M_0)$ where $M_0$ removes all
zero-valued elements; proof: zero elements occupy the bottom ranks of a
descending sort and never affect the parity of any nonzero element's
rank).

## current.md

Updated with a new "Approaches tried (round 15)" section (Status remains
`partial`); see `/home/agentuser/repo/results/imo-2026-03/current.md`.

## Net round-15 assessment

No approach reaches `solved`. The strongest, cleanest new result is the
Twin-Anchor Floor Theorem (fully certified, extends a vertex-value fact to
all $n\ge3$ with a simpler proof) and the AltSum Small-Sum Lemma /
Sub-case (i) Window Reduction Theorem pair (narrows the long-open
$\mathrm{GT}(m)$, $m\ge4$ gap to a width-1 window, unconditional in
excess — real, checkable narrowing of the single biggest remaining
obstruction on that branch). The new slug's identity is mathematically
salvageable but was caught with a real labeling bug that must be fixed
before it counts as verified progress on OddSum specifically.
