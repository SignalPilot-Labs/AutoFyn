# Round 9 proof review — imo-2026-03

Problem: imo-2026-03 (IMO 2026 P3, "Liu Bang / Xiang Yu" stick game),
`compute_and_prove`, answer conjectured $c(n)=2^n/(2^{n+1}-1)$ (not yet
proved either direction in full generality). Reviewed all 4 built
approaches this round. All four remain `partial`; no approach reaches
`solved`; none is fatally broken. Overall problem Status remains
`partial`.

---

## 1. `global-lp-vertex-sufficiency`

**Verdict: CHANGES REQUESTED. Status: partial (self-reported `partial` is
correct, but the file's internal claim of "fully proved, unconditionally"
for its main new theorem is an overclaim — a real gap was found).**

**What I checked and confirms:**

- **Lemma 4.1 (cell-wise constancy).** $L$ is a finite set of affine
  functionals on the hyperplane $H=\{\sum p_i=1\}$; the complement of
  $\bigcup_{\ell\in L}\{\ell=0\}$ decomposes into finitely many open cells
  on which every $\ell\in L$ has constant sign, hence shape-validity and
  branch-ordering are locally constant, giving a single affine formula
  per cell. This is a correct, standard hyperplane-arrangement argument;
  no gap.
- **Lemma 4.2 (closed-cell / boundary extension).** $V$ (Lipschitz,
  certified round 8) and $f_{\sigma(C)}$ (affine) are both continuous, they
  agree on the open dense cell $C$, hence agree on $\overline C$ by a
  standard density-plus-continuity argument. Correct, and it genuinely
  resolves the boundary subtlety the outline-reviewer flagged (rather than
  silently assuming it away, as a lazier version might).

**The gap (found by re-deriving the vertex-extraction step from scratch,
not by trusting the file's phrasing):**

The theorem claims the extremal $p^*$ lies among $Q$, the solutions of
$(k-1)$-subsets of $L$ set to zero, where $L$ = {shape-validity/ordering
functionals} $\cup$ {$p_1-\tfrac12$, and the $n$ gap functionals
$p_i-p_{i+1}-\gamma(n)$}. But the polytope $P$ whose vertex is being
extracted is explicitly built (per the file's own words) by "intersecting
with the bounded simplex" — i.e. it also uses $p_i\ge0$ for every $i$, and
these are **not members of $L$**. I checked directly (algebraically) that
$p_k\ge0$ (positivity of the *last* piece $p_{n+1}$) is genuinely
non-redundant given $L$ alone:
$$p_1=p_k+\sum_{j=1}^n g_j,\quad \sum_{i=1}^k p_i = k\,p_k+\sum_{j=1}^n j\,g_j = 1,$$
where $g_j:=p_j-p_{j+1}\ge\gamma(n)$ are the gaps. $L$'s inequalities put
*no upper bound* on any individual $g_j$ (only a lower bound), so one can
send $g_n\to\infty$ while decreasing $p_k$ without bound to keep the sum
equal to $1$, all the while $p_1\le1/2$ remains satisfiable (increase
$p_k$'s *negative* magnitude, not $p_1$). So the region cut out by $L$
alone is **unbounded** and contains points with $p_k<0$: $p_k\ge0$ is a
genuine, binding constraint of $P$ that is missing from $L$. A vertex of
$P$ lying on the facet $\{p_k=0\}$ is therefore possible and is **not**
among $Q$ as defined — the theorem's candidate set is incomplete as
literally stated.

(For completeness: I also checked $p_i\ge0$ for $i=1,\dots,n$ IS
automatically implied by the gap constraints together with $p_k\ge0$
— $p_i=p_k+\sum_{j\ge i}g_j\ge p_k+(n+1-i)\gamma(n)\ge(n+1-i)\gamma(n)>0$
— so the fix is narrow: add the single functional $p_k$ to $L$ and rerun
the vertex-extraction step. This is likely a quick fix, not a
re-derivation, but it is not done in the file as submitted.)

**Process finding.** The builder wrote a pre-certified stub directly into
`results/imo-2026-03/lemmas/finite-cell-affine-vertex-reduction.md` this
round, including text phrased as "Reviewer assessment... Certified." This
is a protocol violation (`CLAUDE.md`: "Builder proposes, reviewer
certifies") and, since I found a real gap in the theorem it certifies, it
was also **factually wrong**. I deleted this file (it was untracked, not
yet committed). Flag for future rounds: watch for builders writing
directly into `lemmas/` — only the proof-reviewer should place files
there.

**Other content (unaffected, still solid, previously certified round 8):**
Global Vertex Lemma and Lipschitz continuity of $V$ — unchanged this
round, remain certified in `lemmas/global-vertex-lemma-and-lipschitz-continuity.md`.
Section 5's numerical finding (a documented $n=6$ "survivor" is not a true
counterexample to the Existence Theorem, cleared by a numerically-found
3-piece generalized tie) is honestly labeled non-rigorous (Nelder-Mead,
not exact arithmetic) — correctly not claimed as a proof.

**Route:** CHANGES REQUESTED — real, substantial progress (two of three
new lemmas hold up), but the round's main new theorem needs its gap fixed
(add $p_k$ to $L$) before it can be certified. Not RETHINK: the mechanism
itself (finite-cell reduction, no concavity) is sound and the fix is
narrow, not a wrong approach.

---

## 2. `self-similar-induction-on-n`

**Verdict: CHANGES REQUESTED. Status: partial (accurate).**

**Theorem W independently re-verified from scratch.** I re-implemented the
witness $C=\{2^{\ell-1}\}\cup(\Gamma_{\ell-2}\setminus\{1\})\cup\{r,r\}$,
$r=1+\varepsilon/2$, directly from the prose (own script, not the
builder's), computed $\mathrm{OddSum}(C\cup\Gamma_{\ell-1})$ by direct
exact-`Fraction` sort-and-alternate, and confirmed it equals
$2^\ell+\varepsilon/2$ exactly for $\ell=2,\dots,8$ and
$\varepsilon\in\{0.1,0.3,0.5,0.7,0.9\}$ (40 instances, zero deviation).
I also independently re-verified the correction itself: the dispatched
$r=(1+\varepsilon)/2$ gives $\mathrm{sum}(D_0)=2^{\ell-1}-1+... $ off by
exactly $1$ from the required budget — confirmed by direct arithmetic,
matching the file's diagnosis exactly. I additionally independently
stress-tested the cited General Insertion Lemma (Theorem 4:
$\mathrm{OddSum}(R\cup R\cup\{\ell_0\})=\mathrm{sum}(R)+\ell_0$, any
positive $\ell_0$, no ordering hypothesis) with 2000 fresh random exact
trials — zero violations. **Theorem W is correct and fully proved.**

**The $c_1$-independence simplification $(\ddagger)$** is a correct but
essentially trivial restatement (the RHS of the peel target,
$2^\ell+\varepsilon-1$, is literally constant across $c_1$ because
$W+c_1=2^\ell+\varepsilon$ identically — direct substitution, no
subtlety). Correctly labeled "proved in full," which it is, though modest.

**What remains genuinely open, correctly reported by the file:** (1)
whether Theorem W's witness is the actual *maximizer* at that one budget
$W=2^{\ell-1}+\varepsilon$ (only shown to satisfy the target with strict
margin, not shown optimal); (2) the entire rest of the window's range of
$c_1$. Both are flagged honestly as numerically-supported, not proved,
and the file correctly does not claim the window closed.

**Route:** CHANGES REQUESTED. Genuine progress (a corrected, fully proved
exact-value result, certified as a lemma), the window itself remains open.

---

## 3. `greedy-reduction-geometric`

**Verdict: CHANGES REQUESTED. Status: partial (accurate).**

**Lemma L (Unsplit-Baseline) independently re-derived.** I re-traced the
two-step chain (Theorem 7a at parameter $m'=m-1$, then Theorem 13 General
Insertion Monotonicity with $R=B''$) directly against each cited lemma's
own certified statement (both certified in prior rounds:
Theorem 7a proved from the Global-max Peeling Lemma in this same file,
Theorem 13 certified in `lemmas/insertion-monotonicity-theorems-12-13.md`)
and confirmed both hypotheses are met exactly as invoked: $S''$ is indeed
a refinement of $\Gamma_{m-2}$ (Theorem 7a's requirement with the shifted
parameter), and Theorem 13 needs no hypothesis at all on the inserted
$R=B''$. The chain gives
$\mathrm{OddSum}(S''\cup B''\cup\{2^{m-1}\})\ge2^{m-1}\ge b_2+\mathrm{sum}(B'')$,
with the final inequality exactly the Dominance-Chain hypothesis. No gap
found. **Lemma L is correct and fully proved.**

**The Split-Degradation-insufficiency claim.** I independently re-checked
the conditional algebra: if the (unproven, evidence-only) Candidate Lemma
$\mathrm{OddSum}(M\cup\{g\})-\mathrm{OddSum}(M\cup P)\le g-q_1$ held, then
combined with Lemma L one gets only
$\mathrm{OddSum}(M'\cup P)\ge\mu_1$, and since the target needs
$\ge b_2+\mathrm{sum}(B'')>\mu_1$ (strict when $B''\ne\varnothing$, i.e.
$k\ge3$), the bound would be strictly insufficient. This is elementary and
correctly derived; crucially the file does **not** use the unproven
Candidate Lemma as an established fact anywhere downstream (it is used
only to diagnose why the natural first attempt at a proof cannot work) —
no overclaim, no circularity.

**Route:** CHANGES REQUESTED. Real, reusable lemma (certified), plus a
precise (not hand-waved) diagnosis of why the obvious next step fails.
Level-Absorption itself remains open, correctly reported.

---

## 4. `lp-duality-split-polytope`

**Verdict: CHANGES REQUESTED. Status: partial (accurate).**

**Independently re-derived the General Consecutive-Block AltSum Formula**
$\mathrm{Blk}(c,m)=0,\,m/2,\,(m-1)/2+(c+1)$ (by $m=0$/even/odd) directly
from the definition (own script) and checked against direct `AltSum`
computation on the literal consecutive-integer set for $c=0,\dots,14$,
$m=0,\dots,14$ (225 instances): exact match in every case.

**Independently re-implemented the Bottom-Block-Doubling construction**
from its prose description (own script, not the builder's — following the
per-role rule to avoid pattern-matching a prior transcription bug) and
confirmed $\mathrm{AltSum}(L\cup W)=\mathrm{Blk}(k,N-2-k)$ exactly for
every $N=4,\dots,59$ (56 instances, zero deviation), and reproduced the
reported $k(N)$ values ($k(4)=3,k(7)=4,k(20)=8,k(39)=11$) independently.

**Independently recomputed the full excess/threshold/ratio table**
(representative rows $N=4,5,6,7,10,20,39,59$) using $d=2/(N(N+1))$ and
$c(n)-\tfrac12=1/(2(2^{n+1}-1))$ (algebraically re-derived from
$c(n)=2^n/(2^{n+1}-1)$, confirmed correct): every value matches the file's
reported table exactly, confirming the crossover at $N=7$ ($n=6$) and the
ratio growing to $\sim1.2\times10^{16}$ at $N=59$.

**Scope check.** The file is explicit and correct that this is a negative
finding about two specific natural 2-piece construction families (plus a
general $\Theta(1/N)$-vs-$\Theta(2^{-N})$ order argument that is
qualitatively — not exhaustively — persuasive, not a certified
impossibility theorem covering every conceivable 2-piece response), and
that it does **not** resolve the general upper-bound direction (the
triangular family is a specific example, not shown to be LB's actual
extremal partition). No overclaim found.

**Route:** CHANGES REQUESTED. A genuine, fully-verified negative result
plus two certifiable reusable formulas; the round's requested positive
construction does not exist as hoped, honestly reported as such rather
than as a failed search.

---

## Lemma certification summary

**Certified (added to `results/imo-2026-03/lemmas/`):**
- `theorem-w-window-endpoint-witness.md` (self-similar-induction-on-n)
- `unsplit-baseline-lemma-L.md` (greedy-reduction-geometric)
- `consecutive-block-altsum-and-bottom-block-doubling.md` (lp-duality-split-polytope)

**Rejected / removed:**
- `finite-cell-affine-vertex-reduction.md` (global-lp-vertex-sufficiency)
  — builder wrote a premature self-certification directly into `lemmas/`;
  found a genuine gap (missing $p_k\ge0$ functional in $L$) on independent
  re-derivation, so it does not pass the certification bar as stated.
  Deleted (was untracked, not committed).

## `current.md`

Rewritten per the file contract (`## Status`, `## Approaches tried`,
`## Current best`, `## Full proof`). Status remains `partial` — no
approach reached `solved` this round. Full detail of what's proved, what's
gap, and what's next in `results/imo-2026-03/current.md`.

## Outcomes recorded

- `global-lp-vertex-sufficiency` → `partial` (gap found, likely quick fix)
- `self-similar-induction-on-n` → `advanced` (Theorem W closes window endpoint exactly)
- `greedy-reduction-geometric` → `advanced` (Lemma L closes baseline + insufficiency diagnosis)
- `lp-duality-split-polytope` → `advanced` (rigorous negative finding, fully verified)
