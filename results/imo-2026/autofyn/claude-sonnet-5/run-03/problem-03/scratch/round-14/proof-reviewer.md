# Proof review — imo-2026-03, round 14

Status of the problem remains **partial**. All three built approaches get
**CHANGES REQUESTED**. No approach is `solved`. All three made genuine,
independently-verified progress this round; one cross-file overclaim was
found and corrected in place.

---

## 1. `lp-duality-split-polytope` — CHANGES REQUESTED (Status: partial)

**Headline claim**: the **Chain-Correction Floor Theorem**. At the region
vertex $e_0$ (coordinates $p_i(e_0)=a+(N-i)\delta$, $N=n+1$,
$\delta=\gamma(n)=1/(2^N-1)$, $a=p_N(e_0)=\frac{2-n(n+1)\delta}{2(n+1)}$,
certified in `finite-cell-vertex-reduction-and-region-classification.md`),
for every $n\ge6$ an explicit hybrid construction — splitting pieces
$1,\dots,N-2$ (leaving the two smallest untouched), using $n-1\le n$ cuts —
achieves $\mathrm{OddSum}(M)=\tfrac12$ exactly, the universal absolute floor
for any legal response at any partition.

**Independent re-derivation (from scratch, not the builder's script).** I
wrote my own exact-`Fraction` Python implementation of the construction
directly from its prose description (not the closed-form shortcut) and
tested $n=6,7,8,9,10,12,15,20$:
- every fragment strictly positive,
- total mass exactly $1$ in every case,
- $\mathrm{AltSum}=0$ exactly (hence $\mathrm{OddSum}=1/2$ exactly) in
  every case — zero deviation,
- cut count $=n-1\le n$ (legal) in every case.

I also independently verified the Positivity Lemma's reduction
($a>2\delta \iff (n+1)(n+4)<2^{n+2}-2$) by direct fraction arithmetic for
$n=6,\dots,24$: holds in every case, matching the builder's inductive proof.
And I verified $c(n)=2^n/(2^{n+1}-1)>1/2$ for all tested $n$ (trivially:
$2^{n+1}-1<2^{n+1}$), confirming this construction is strictly better than
$c(n)$, not a violation of anything.

**Verdict on the "correction" claim.** The builder correctly identified a
real problem: `global-lp-vertex-sufficiency.md` Section 4.5 (its Mass-
Constraint corollary) states "$e_0$... already known, Section 4.3, to be a
point where $V(e_0)=c(n)$ *exactly*, i.e. the tightest possible case." But
Section 4.3 itself only ever establishes $V(e_0)\le c(n)$ (an *upper-bound*
witness via the $k$-Anchor-Merge construction) — it never proves a matching
lower bound $V(e_0)\ge c(n)$. This round's Chain-Correction construction is
an equally legal response at the *same* $e_0$ achieving strictly less
($1/2<c(n)$ for $n\ge6$), so the true value is $V(e_0)=1/2$ for $n\ge6$, not
$c(n)$. **This is a genuine, confirmed overclaim, not a contradiction of any
proved theorem** — the overall Existence Theorem's actual target
($V(p)\le c(n)$ for every $p$) is only strengthened by this finding (a
smaller $V(e_0)$ is strictly better news), and I confirmed the Mass-
Constraint Theorem's own derivation (the corollary at issue) uses only
$e_0$'s *coordinates*, never the value of $V(e_0)$, so nothing downstream
is invalidated. **I corrected the offending sentence in place** in
`global-lp-vertex-sufficiency.md` (Section 4.5), replacing the false
equality claim with the correct scoped statement plus a note crediting this
round's finding, per the reviewer's authority to fix a confirmed cross-file
factual error (distinct from editing another builder's proof content).

**Certified**: `lemmas/chain-correction-floor-theorem.md` (new).

**Honest scope, correctly stated by the builder**: does not establish
whether a smaller active-set size $s<n-1$ also reaches the floor (an
unreliable float-only scan hints it might, explicitly not claimed as
established), nor does it cover $n<6$. Status `partial` for the approach as
a whole is correct — this does not close the upper-bound Existence Theorem,
it only sharpens one data point of it (in the right direction).

---

## 2. `self-similar-induction-on-n` — CHANGES REQUESTED (Status: partial)

Three new results this round, plus one correctly-diagnosed negative
finding.

**AltSum Corollary** ($0\le\mathrm{AltSum}(N)\le\max(N)$ for any finite
multiset of positive reals). Independently re-derived (the one-paragraph
peeling induction is straightforward and correct) and stress-tested with my
own exact-`Fraction` script: 20000 random multisets (size 0–10), zero
violations. **Certified.**

**Growth Lemma** (the increasing-direction complement of the certified
Monotonicity Reduction Lemma: for $D$ with $k\ge2$ coordinates in
$(0,2^{m-1}]$ summing to $\le2^m$, there's a coordinatewise-larger $D''$
with the same count/cap summing to exactly $2^m$). The feasibility argument
(intermediate value theorem on a saturate-one-coordinate-at-a-time
construction) is correct and elementary; the monotonicity conclusion
correctly reuses the already-certified Elementwise Monotonicity Lemma
rather than re-proving it. Independently re-verified the feasibility
construction by direct reimplementation ($m=1,\dots,6$, $k=2,\dots,m+1$, 500
trials each): zero violations. **Certified.**

**Small-Sum Reduction Theorem** — **NOT certified**. This theorem
(`Case-B(m,k) \Rightarrow$ the full small-sum branch of $\mathrm{GT}(m)$) is
explicitly proved by the builder only "modulo one flagged tie detail": when
the Growth Lemma's saturating construction produces a $D''$ with a
coordinate landing exactly at the cap $2^{m-1}$, `Case-B(m,k)`'s strict
hypothesis ($\max(B)<2^{m-1}$) does not literally apply, and the builder
honestly reports this reduction (via the certified Tie-Neutrality Lemma) as
"not completed in full this round." This is a real, self-reported,
unclosed gap — correctly not claimed as a closure by the builder, and I
agree it must not be certified as stated. I independently reproduced the
underlying $q{=}0$/$p{=}0$ peeling identity (own 5000-trial exact-`Fraction`
test, zero mismatches) that the theorem's proof rests on, so the *proved
part* of the argument is solid; only the boundary tie case is missing.

**Counterexample killing the "piece-cap-relaxed" fix.** The claim
$D=\{0.4,0.4\}$ (with $\Gamma_{-1}=\varnothing$, $k=0$) giving
$\mathrm{OddSum}(D)=0.4<\min(\mathrm{sum}(D),2^0)=0.8$ is a trivial, correct
computation — I re-checked it by hand. The builder's diagnosis (this
regime is never actually invoked by the real recursion, since $\mathrm{GT}
(1)$ at this $D$ holds with margin — $\mathrm{OddSum}(\{1,0.4,0.4\})=1.4\ge
0.8$) is also correct and I re-verified it. This correctly rules out the
naive fix without overclaiming a closure.

**Net**: `GT(m)` for $m\ge4$ (hence gap (a) of the shared window for
$\ell\ge5$) remains open, narrowed to exactly two named sub-objects
(`Case-B(m,k)`, unresolved since round 4; sub-case $q=1,e\ge1$, newly
precisely diagnosed but not closed). Status `partial` is correct.

---

## 3. `global-lp-vertex-sufficiency` — CHANGES REQUESTED (Status: partial)

Two numerical findings on fragment-vs-fragment tying, both correctly *not*
proposed as lemmas (the dispatch's own instruction, and I agree neither is
a general proved theorem).

**Cheap-kill 1 (cyclic pairwise-tie chain).** Exhaustive search (every odd
$s\le n$, every subset, every cyclic order) in exact rational arithmetic,
tested at 3 catalogued $n=3$ hard points plus 12–15 fresh random points per
$n=3,\dots,6$: fails broadly (9/15 to 15/15 failure rates). This is a clean
negative result — I did not re-run the full exhaustive search myself
(computationally heavy and the claim is purely negative/numerical, correctly
not escalated to a lemma), but the reported methodology (brute-force
enumeration in exact rationals, not sampled or float-based) is sound and
the reported per-point exact excess ($47/30000$ at one hard point) is
internally consistent with $c(3)=8/15$.

**Cheap-kill 2 (descending fragment chain).** The builder found and fixed a
genuine bug (a first draft silently dropped one tied fragment, producing an
impossible OddSum below the floor $\mathrm{sum}(M)/2$ — caught by the
elementary OddSum Floor sanity check, exactly the self-verification
discipline the rigor rules ask for). After the fix, the finding is honestly
mixed: exhaustive search over subset/order/parameter matches the true
$V(p)$ at 2/3 hard points and clears $c(3)$ at all three, but restricted to
natural (simple index-order) rules it fails broadly (5/8–8/8), and no
tractable closed-form selection rule was found. The builder correctly
declines to escalate this to a general theorem (the exhaustive search is as
expensive as computing $V(p)$ directly) — this is the right call, not an
underclaim.

**Scope correction.** The builder's Section 4.8.0 correctly re-reads the
round-11 Mass-Constraint Theorem's hypothesis ($T_a\le p_{i_a}$, a sum of
*whole untouched pieces*) and confirms it structurally cannot cover
fragment-vs-fragment tying — this is a legitimate, verifiable scoping fix
to the round-13 "deprioritized" framing, not an overclaim.

Status `partial` is correct; the $\Sigma$-shape classification gap (the
sole remaining obstruction on the upper-bound Existence Theorem) is
untouched this round.

---

## Cross-cutting finding: cross-file overclaim found and fixed

`global-lp-vertex-sufficiency.md` §4.5 stated "$V(e_0)=c(n)$ exactly, i.e.
the tightest possible case" — an unproven equality (Section 4.3 of the same
file only ever proves $\le$). `lp-duality-split-polytope`'s independently
re-verified Chain-Correction Floor Theorem now shows this is actually false
for $n\ge6$ ($V(e_0)=1/2<c(n)$). I corrected the sentence in place in
`global-lp-vertex-sufficiency.md` and confirmed the fix does not affect the
Mass-Constraint Theorem's own derivation (uses only $e_0$'s coordinates).
Flagging this pattern for future rounds: **an "exact closure" claim proved
only via one construction (an upper-bound witness) must never be restated
elsewhere as "the true minimax value equals X" without a matching lower
bound** — this is exactly the kind of drift that compounds silently across
many rounds of cross-referencing if not caught.

## Lemmas certified this round

- `lemmas/chain-correction-floor-theorem.md` (lp-duality-split-polytope) —
  new.
- `lemmas/altsum-corollary-and-growth-lemma.md` (self-similar-induction-on-n)
  — new (AltSum Corollary + Growth Lemma only; Small-Sum Reduction Theorem
  explicitly excluded, has an acknowledged open gap).

## Lemmas NOT certified this round

- Small-Sum Reduction Theorem (self-similar-induction-on-n) — real, honest,
  self-reported gap (tie-boundary case of the Growth Lemma's saturating
  construction). Push a builder at closing exactly this next round; the
  fix is likely a direct application of the already-certified
  Tie-Neutrality Lemma, per the builder's own diagnosis.
- No lemma proposed by global-lp-vertex-sufficiency this round (correctly).

## current.md

Updated per the file contract: `## Status` remains `partial`, new
"Approaches tried (round 14)" section added (kept prior rounds' sections for
history), "Current best" given a new round-14 paragraph summarizing the
Chain-Correction Floor Theorem + correction, the two certified elementary
lemmas, and the two cheap-kill findings. No `## Full proof` section (Status
is not `solved`).

## Recommendation for next round

1. `self-similar-induction-on-n`: close the Small-Sum Reduction Theorem's
   flagged tie-boundary case via the certified Tie-Neutrality Lemma (the
   builder's own diagnosed next step) — this is the most concrete,
   closest-to-closing target in the lower-bound direction.
2. `lp-duality-split-polytope`: investigate whether smaller active-set size
   $s<n-1$ can also reach the floor $1/2$ at $e_0$ (flagged as an
   unreliable numeric lead this round) — not urgent for the main proof
   (the upper-bound direction only needs $V(e_0)\le c(n)$, already
   over-satisfied), but potentially useful methodology for other vertices.
3. `global-lp-vertex-sufficiency`: push on the two precisely-stated open
   sub-questions from cheap-kill 2 (closed-form selection rule for the
   descending chain; whether $\sigma^*(p)$ always has that shape) — this is
   the most promising lead toward the $\Sigma$-shape classification gap,
   the sole remaining obstruction on the upper-bound side.
