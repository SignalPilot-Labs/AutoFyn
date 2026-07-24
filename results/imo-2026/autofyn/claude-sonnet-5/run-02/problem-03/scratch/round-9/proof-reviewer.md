# Round 9 proof review — imo-2026-03

Reviewed builds: `greedy-halving-adversary.md`, `lp-duality-certificate.md`.
Problem: `problems.jsonl` entry `imo-2026-03` (IMO-2026 P3-difficulty),
target $c(n)=2^n/(2^{n+1}-1)$, both directions, general $n$. Both slugs
attack pieces of this (Claim B of the lower bound; the general upper
bound respectively) — neither claims to close the whole problem.

All load-bearing claims below were independently re-derived/re-verified
with fresh exact-`Fraction` Python scripts (not the builders' own scripts),
per the round-8 lesson in memory. Scripts: `/tmp/round-9/verify_greedy.py`,
`verify_greedy2.py`, `verify_lpdual.py`, `verify_witness.py`,
`search_witness.py`, `verify_more.py`.

---

## `greedy-halving-adversary`

**Claimed Status:** partial. **Confirmed: partial is correct — no overclaim.**

### Lemma 19 (single-residual indicator)
Statement: for $F=\{v\}\cup P$, $P$ exactly-paired, $u_F(x)\equiv\mathbb1[x<v]$
pointwise, so $A(F)=v$. Proof is a direct, correct parity argument (even
multiplicities of $P$ never flip parity). **Independently re-verified**:
2000 random exact-`Fraction` trials of $A(\{v\}\cup P)$ vs. $v$, zero
mismatches. **Correct, general, no gap.**

### Proposition 20 (exact identity $A(F\cup G')=v-A(G')$ for $v\ge p_2$)
Derivation combines Lemma 19 with `cross-term-identity-threshold` and
`safe-window-lemma` (both already certified): the truncation
$\min(v,r)\ge p_2$ plus $v_{G'}\equiv0$ above $p_2$ collapses the cross
term to exactly $A(G')$. **Independently re-verified**: 1200 random trials
across $n=2,3,4,5$, random $v\in[p_2,p_1]$, random tail refinements with
up to $n-2$ cuts — exact match every time. **Correct, general, no gap.**

**The claimed correction of the outline is real.** The round-9 outline
proposed reusing `half-window-vanishing-lemma`'s midpoint argument to get
$\int_0^{p_2}v_{G'}\le p_2/2$. I independently checked this at $n=3$: the
untouched-tail value alone is $A(\tau)=1/5=3/15 > p_2/2=2/15$, so the
proposed bound is false as stated. The builder correctly diagnosed why
(the half-window mechanism relies on a *narrow* window from a two-fragment
$F$; here $u_F=\mathbb1_{[0,v)}$ spans the *entire* interval from 0, not a
narrow window) and used the exact identity instead. This is a genuine,
verified correction, not an evasion.

### Proposition 21 (reduction to $(\dagger)$)
Straightforward algebra given Proposition 20 plus a correct minimal-cut-count
argument ($\ell(F)=1$, $v<p_1$ forces $\ge2$ cuts on $p_1$, since a single
cut yields exactly two fragments, either equal [$\ell=0$] or unequal
[$\ell=2$]). The $c=0$/$F=\{p_1\}$ edge case is correctly carved out and
separately justified via the already-proven Lemma 6, with an explicit note
that $(\dagger)$'s smaller budget bound does not (and need not) transfer to
it. **Correct, general, no gap.**

### Proposition 22 (partial closure of $(\dagger)$)
Rescales to the $(n-1)$-ladder, applies `dominant-element-removal-identity`
with $q_1>\mathrm{Total}(R)$ (verified: $q_1>1/2\iff2^{m+1}>2^{m+1}-1$,
true), then uses the granted $(\star_{n-2})$ hypothesis plus
`tail-self-similarity`'s cross-level constant to close exactly with zero
slack. I **independently re-derived and re-verified** the closed-form bound
$\max A(G')=p_2-f(n)$ (with $f(n)=1/(2^{n+1}-1)$, distinct from the
target $a_n=2^nf(n)$ — I caught my own initial confusion of these two
constants and re-ran with the correct definition) for $n=3,4,5,6$ via a
fresh 5000-trial exact-`Fraction` random search restricted to the
$p_2$-uncut sub-case: exact match with the closed form in every case
($1/5$, $7/31$, $5/21$, and the $n=6$ analogue). I also ran a 20000-trial
search over the *full* $(\dagger)$ domain (including refinements that cut
$p_2$) at $n=3,4,5$ and found the *same* maximum — this corroborates (does
not prove) that the uncovered "$G'$ cuts $p_2$" sub-case is not the actual
bottleneck, consistent with the builder's own framing.

**Correctly scoped as conditional, not certified standalone** (the builder
itself declines to propose it for certification until the complementary
sub-case closes — good judgment, endorsed).

### What remains open (confirmed accurate)
1. The complementary sub-case of $(\dagger)$ where $G'$ cuts $p_2$ itself —
   genuinely not covered by Proposition 22's argument (it needs $p_2$
   uncut for the dominant-removal step to apply directly to $Q$'s own top
   piece).
2. The entire $v<p_2$ case — correctly diagnosed as not reducible via the
   same rescaling trick, since $v$ is not tied to the tail's own ladder
   scale for generic $v$.
3. $\ell(F)\ge2$ — honestly flagged as only weakly proxy-checked (via
   $\ell(S)$, not $\ell(F)$ itself), explicitly **not** a real check of the
   intended target; correctly not claimed as evidence either way.

**No overclaim found.** The write-up is precise about what is
unconditional vs. conditional vs. still open at every step.

**Verdict: CHANGES REQUESTED.** Real, verified progress (3 new
unconditional general lemmas plus a correctly-scoped conditional
proposition); Claim (B) is not closed even for $\ell(F)=1$ in full
generality.

---

## `lp-duality-certificate`

**Claimed Status:** partial. **Confirmed: partial is correct — no overclaim.**

### Theorem C′ (bisect-top recursive identity)
Pure pair-cancellation bookkeeping, structurally identical in mechanism to
the already-certified `one-step-peel-identity`. **Independently
re-verified**: 2000 random exact-`Fraction` trials (random $m$, random
tail refinement), zero mismatches.

### Telescoping threshold identity $a_{n-1}=a_n/(2(1-a_n))$
Elementary algebra from $a_k-1/2=1/(2(2^{k+1}-1))$. **Independently
re-verified** symbolically for $n=1,\dots,14$ (exact match both sides as
`Fraction`s) — this is a genuinely general algebraic proof, not a finite
check, matching the file's own claim.

### $n\le3$ closure of $p_1\ge T/2$ regime
Combines Theorem A (Full-Match, re-verified: 2000 trials) with Theorem C′
+ the telescoping identity + the already-certified `n2-upper-bound-lp-
argument` as the $P(3)$ base case. I independently re-derived the
algebraic threshold-matching corollary (§2's Corollary) from scratch and
confirmed it collapses to exactly $a_nT$ with zero slack. I then ran a
**200,000-trial random search** over 4-piece markings with $p_1\ge T/2$,
checking the ceiling bound $p_1/2+a_2(T-p_1)\le a_3T$ from both sub-cases
(Theorem A directly for $p_1<a_3T$, the Corollary for $p_1\ge a_3T$): zero
violations. This corroborates the closed-form proof (which is itself fully
rigorous, not numeric) rather than substituting for it.

### The claimed circularity/coupling (§4's "Why this does not extend past $n=3$")
I traced the dependency by hand: to close $p_1\ge T/2$ at level $n\ge4$ via
Theorem C′, the inductive step needs $\Phi_{\min}(\text{tail})\le a_{n-1}T'$
for an **arbitrary** $(n)$-piece tail (not just tails whose own $p_1\ge T/2$
half), because nothing in Theorem C′'s statement restricts which regime the
*tail itself* falls into — a concrete instance is given ($(6,2,2,1)/11$'s
own tail $\{2,2,1\}/11$ sits in the tail's own $p_1<T/2$ regime). This means
$P(n-1)$ (the **full**, both-regime statement) is required as the induction
hypothesis, not merely its $p_1\ge T/2$ half — a real coupling, correctly
diagnosed as blocking a "close each regime independently" strategy. I
confirm this is not a fixable oversight within the current mechanism: it is
inherent to Theorem C′ operating on an *arbitrary* tail, and the file does
not claim it is unfixable in principle by a different route (only that this
route requires it) — an accurate, non-overclaiming diagnosis. Terminology
note: "circularity" is a slightly loose word for what is really a strong
induction hypothesis requirement (not a logical circularity/self-reference),
but the file's own precise explanation (§4, the paragraph beginning "Why
this does not extend past $n=3$") states the actual mechanism correctly, so
this is not a substantive error, just an imprecise label — I note it here
but do not treat it as a flaw in the mathematics.

### New witness $(2/5,3/10,1/5,1/10)$
I independently recomputed: Theorem D′ gives $11/20=0.55$, Theorem E gives
$11/20=0.55$ (both exactly as claimed), and the proposed resolving strategy
(peel $p_1$ against $p_4$ via Theorem B$_k$, then bisect $p_3$) produces the
exact final multiset $\{3/10,3/10,1/10,1/10,1/10,1/10\}$ with
$\Phi=1/2$ exactly — I verified this multiset sums to $1$ and its $\Phi$
directly. I additionally ran a **300,000-trial randomized search** over
legal $\le3$-cut Xiang Yu strategies at this exact marking (not restricted
to any template) and found no strategy beating $1/2$ (best found $0.5004$,
consistent with $1/2$ being the tight optimum, given random cut-position
discretization can't hit the exact rational optimum). This corroborates
(does not itself prove) the claim that $\Phi_{\min}=1/2$ exactly at this
witness, and confirms the witness is correctly resolved (not a
counterexample to $c(3)\le8/15$).

### Theorems D′, E, B$_k$, and the equal-pieces negative result
All independently re-verified: D′/E identities (2000 trials each, zero
mismatches), B$_k$ identity (2000 trials, random $k$, zero mismatches),
$s^\ast=\frac32a_nT$ closed form (re-derived from scratch and matched
symbolically for $n=2,\dots,19$), and the equal-pieces-insufficiency
inequality ($8-2^{2-n}<3(n+1)$ for $n\ge2$) checked symbolically for
$n=2,\dots,19$ with zero violations. All correct.

### What remains open (confirmed accurate)
The entire $p_1<T/2$ regime beyond $n\le2$ (only two specific witnesses
resolved, no general closed-form condition); pushing $p_1\ge T/2$ past
$n=3$ (blocked on the coupling above). No overclaim: the file is explicit
throughout that "resolved individually... not by a closed-form threshold."

**Verdict: CHANGES REQUESTED.** Real, verified progress (a genuine
complete sub-result — $p_1\ge T/2$ fully closed at $n\le3$ — plus 5 new
general, unconditional, reusable identities/negative results); the general
upper bound is not closed.

---

## Lemmas certified this round

Written to `results/imo-2026-03/lemmas/`:
- `single-residual-indicator.md` (Lemma 19)
- `single-residual-exact-peel-identity.md` (Proposition 20)
- `v-geq-p2-budget-reduction.md` (Proposition 21)
- `bisect-top-recursive-identity.md` (Theorem C′)
- `telescoping-threshold-identity.md`
- `generalized-peel-identity.md` (Theorem B$_k$)
- `bisect-top-bottom-recursive-identity.md` (Theorems D′ and E, plus the
  exact $s^\ast$ threshold and the equal-pieces-insufficiency negative
  result)
- `full-match-achievability.md` (Theorem A — backfilled from round 8 since
  round 9's §3-4 directly builds on it and it had not yet been written as
  a standalone file)

**Not certified:** Proposition 22 (conditional, not proposed for
certification by its own builder — endorsed, correct call); the round-9
outline's "$\le p_2/2$" bound (refuted, recorded as false in the
`single-residual-exact-peel-identity.md` note rather than a separate
dead-end file, since it never had independent content beyond the
refutation already documented in the approach file itself).

## current.md

Updated `## Status` section's round-8 entry with a new round-9 paragraph
summarizing both builds' verified content, matching the scope confirmed
above (no overclaim propagated). Status remains `partial`; the problem is
not solved.

## Overall round-9 verdicts

- `greedy-halving-adversary`: **CHANGES REQUESTED** (Status: partial —
  correctly self-reported, genuine new progress, real gaps remain: $v<p_2$
  case, complementary sub-case of $(\dagger)$, $\ell(F)\ge2$ unresolved).
- `lp-duality-certificate`: **CHANGES REQUESTED** (Status: partial —
  correctly self-reported, genuine new progress including a full closure
  of a real sub-case ($p_1\ge T/2$ at $n\le3$) and a correctly-diagnosed
  structural obstruction blocking $n\ge4$; $p_1<T/2$ regime remains open in
  general).

No RETHINK, no APPROVE this round — both approaches remain live and
productive, converging (from opposite directions of the theorem) on the
same underlying pattern: closed-form templates resolve individual
witnesses but not the full simplex/domain without either a genuinely
sharper mechanism or exact (not ceiling) recursive values.
