## imo-2026-03 (lens: no-dominant-fragment branch of the p2-Pinned-Dominance Lemma, front 1, `greedy-halving-adversary`)

- **Distinct openings** (ranked by promise):

  1. **[HEADLINE — new, promising] Bypass the dominant/no-dominant case split
     entirely with a stronger unconditional claim.** Numerically, for the
     actual application (m = p2, τ = R a legal refinement of the ratio-2
     tail {p3,...,p_{n+1}}), the *unconditional* inequality
     $$A(F_2\cup R)\ \le\ p_2 - A(R)\qquad\text{for every legal split }F_2\text{ of }p_2\text{ (any }k\ge1\text{, dominant or not)}$$
     holds with **zero violations** across 20,000+ fresh exact-`Fraction`
     trials (n=3..7, random k up to 6, random legal R, correctly respecting
     per-piece cut-budget boundaries). The maximum of $A(F_2\cup R)$ over all
     splits $F_2$ of $p_2$, for fixed $R$, is empirically attained **exactly**
     at the trivial "no cut" vertex $F_2=\{p_2\}$ (verified by a 20,000-trial
     max-search across n=3..6: gap between the found max and the claimed
     bound is exactly 0 in every case). Since $\mathrm{Total}(\text{tail})<p_2$
     always (already-certified `general-ladder-dominance`/safe-window fact),
     $p_2$ *always* dominates $R$ automatically — so this single inequality,
     if proved, closes Prop 28's dominant-fragment branch AND the
     complementary no-dominant-fragment branch **in one shot**, with no case
     split on $f_1$ vs $\mathrm{Total}(F_2'')+s$ at all. This is a genuinely
     different, more powerful target than Prop 28's own framing.
     **Caveat, load-bearing:** this is *not* true for arbitrary (non-ladder)
     reference sets — I found a concrete counterexample with a random
     reference multiset $\tau=\{49,2/5\}$, $m=203/4$ (dominant: $m>
     \mathrm{Total}(\tau)$), where a 3-part split of $m$ gives $A(F\cup\tau)$
     strictly exceeding $m-A(\tau)$ (2810/20000 violations in a broad random
     search). It *does* survive for raw ratio-2 $\tau$ with a strict
     dominance margin (30,000 trials, zero violations) and for genuine legal
     refinements $R$ of the ladder tail (20,000+ trials, zero violations,
     including the actual application). **So the needed hypothesis is
     genuinely ladder/ratio-2-structure-dependent, matching round 13's
     diagnosis — this is not a free generic fact, but it is real and
     narrower/cleaner than Prop 28's split-by-dominance approach.**

  2. **Vertex-maximization mechanism for opening 1.** The certified
     `exchange-smoothing-vertex-maximization` proposition's proof (per its
     own lemma file) **does not require box constraint $f_i\le\tau_1$ for
     compactness** — boundedness already follows from $\sum f_i=s$, $f_i\ge0$
     — so an unrestricted-simplex corollary (maximize $E(F\cup\tau)$ over ALL
     splits of mass $s$, no box cap) should follow by the identical exchange
     argument, landing on vertices of the same "pinned + one tied group"
     form. This is exactly the shape needed for opening 1: apply it with
     reference $\tau=R$ (need not be ratio-2 per the general statement) and
     moving variable $F_2$ (splitting $p_2$). **Blocking issue found by round
     10 and still unresolved:** the box-free "simplex" variant of this lemma
     (`simplex-exchange-smoothing-vertex-maximization.md`) was submitted but
     **not certified** — round 10's reviewer found its literal pin-set
     $\{\tau_1,\dots,\tau_r\}$ omits $0$, contradicting its own proof (which
     treats "$f_j$ hits 0" as a stopping condition) and exhibited a concrete
     failing case. **Before this mechanism can be used rigorously, that
     lemma must be restated with pin set $\{0,\tau_1,\dots,\tau_r\}$ and
     re-certified** — a precise, scoped prerequisite, not a new obstruction.
     Once fixed, evaluating at the resulting vertex family would need
     `odd-run-reduction-lemma`, same as Case I Closure did.

  3. **Direct induction on cut-count $k$ of $F_2$ — tested and REFUTED as a
     simple mechanism.** I tested whether merging any two fragments of
     $F_2$ (reducing $k\to k-1$) weakly *increases* $A(F_2\cup R)$ under the
     dominance hypothesis alone — a natural simplification that would avoid
     the vertex machinery entirely. **This single-step merge-monotonicity is
     FALSE even when $p_2$ dominates $R$**: 3844/16000 violations found
     (n=3..6, random $k$, random legal $R$). So the true maximum (opening 1)
     is real but is a *global* fact about the full polytope, not obtainable
     by a naive greedy pairwise-merge argument — don't propose this as the
     proof mechanism; use the vertex-maximization route (opening 2) instead.

  4. **$\ell(F)=2$, $P\ne\varnothing$ dominance-threshold-with-$\mathrm{Total}(P)$
     idea (dispatch's second target): PARTIALLY CONFIRMED, closes a genuine
     sub-case quickly.** Recall (see round-13 diagnosis in the approach
     file) this reduces to bounding $\psi(t^*)=A(\{t^*\}\cup G')$ where
     $t^*=p_2-\mathrm{Total}(P)$, target $\psi(t^*)\le p_2-f(n)$. Splitting
     on whether $t^*\ge\mathrm{Total}(G')$ (note $\mathrm{Total}(G')=
     \mathrm{Total}(\text{tail})$ always, independent of how it's refined):
     - **If $t^*\ge\mathrm{Total}(G')$ (i.e. $\mathrm{Total}(P)$ small
       enough that $t^*$ still dominates)**: `dominant-element-removal-
       identity` gives $\psi(t^*)=t^*-A(G')$ exactly, so the target reduces
       to $A(G')\ge f(n)-\mathrm{Total}(P)$ — **strictly weaker** than the
       standard $A(G')\ge f(n)$ bound the recursive machinery already
       targets elsewhere (e.g. Prop 26's own $L(n-1)$-style argument), so
       this sub-branch should close "for free" once the standard recursive
       bound is available at the appropriate depth. **Verified numerically,
       correctly respecting the actual cut-budget constraint** (total cuts
       on $p_1$'s split $\ge3$ when $P\ne\varnothing$, so $G'$'s own budget
       is $\le n-3$; my first pass ignored this and found a spurious
       "violation" that vanished once corrected — same class of bug round
       10 already flagged): n=4,5,6, ~4600+ trials each, zero violations
       once budget-legal.
     - **If $t^*<\mathrm{Total}(G')$ (large $\mathrm{Total}(P)$)**: falls
       into the same open no-dominant-fragment territory as opening 1/the
       main $(\dagger)$ obstruction — not closed by this mechanism.
     So the "Total(P)-threshold" idea does *not* close the whole sub-case
     but does **cleanly and immediately close a genuine, non-vacuous chunk
     of it** (small-$\mathrm{Total}(P)$ regime) via existing tools, narrowing
     what's left to the identical no-dominant-fragment core.

- **Candidate technique(s):** exchange-smoothing-vertex-maximization
  (general/box-free form, once the pin-set-with-0 fix is certified) +
  `odd-run-reduction-lemma` for evaluation, targeting opening 1's stronger
  unconditional claim directly rather than Prop 28's dominant/no-dominant
  split. `dominant-element-removal-identity` continues to be the right tool
  for opening 4's small-$\mathrm{Total}(P)$ sub-branch.

- **Cheap-kill candidates:** none obvious to fully close the core obstruction,
  but two cheap sanity/pruning checks worth running before heavy proof effort:
  (a) confirm $\mathrm{Total}(\text{tail})<p_2$ (already certified, reused
  here as the reason $p_2$/R dominance is automatic — no new proof needed);
  (b) always double-check "legal refinement" respects per-piece cut-budget
  and total-cut-budget coupling before trusting any numeric check in this
  area — this exact bug (over-allocating cuts across two independently
  varied quantities) produced a **spurious violation** in my own first-pass
  test of opening 4, and is flagged as a recurring trap in rounds 10 and
  now again this round.

- **Knowledge-base entries to use:** none of `knowledge_base.md`'s generic
  entries add new leverage beyond what's already reused (this is deep
  in project-specific lemma territory); the relevant machinery is entirely
  in `results/imo-2026-03/lemmas/` (`exchange-smoothing-vertex-maximization`,
  `odd-run-reduction-lemma`, `dominant-element-removal-identity`,
  `triangle-bound-for-a`, `cross-term-identity-threshold`,
  `general-ladder-dominance`).

- **Analogous past problems (cruxes):** none newly consulted this round —
  this lens is entirely internal to the project's own accumulated machinery
  (13 rounds deep); a fresh crux-corpus search is unlikely to add value at
  this level of specificity (the obstruction is about evaluating $A$ of an
  "already-cut vs already-cut" configuration, a bespoke construction not
  resembling a standard corpus pattern). Prior rounds' explorers have not
  reported a match either.

- **Prior progress:** Prop 28 (certified `triangle-bound-for-a`, Prop 28
  itself recorded but not separately promoted) closes the dominant-fragment
  branch modulo one flagged bookkeeping step (combine with the
  $(\star_{n-2})$-recursive argument, mechanically identical to Prop 22's).
  The no-dominant-fragment branch and the $\ell(F)=2,P\ne\varnothing$
  shifted-threshold sub-case are both open as of round 13.

- **Dead ends (do not retry):**
  - Transplanting `ratio-2-spacing-lemma`/`last-element-bound` verbatim to
    an already-cut reference set $R$: **directly refuted this round** — the
    generalized claim "$A(X)\ge\min(X)$ for $X$ a subset of a legal
    refinement's fragments" is FALSE (262/12000 violations, exact
    counterexample found at $n=3$). These lemmas are ratio-2-spacing-
    specific and do not generalize to cut multisets, confirming round 13's
    diagnosis rather than just repeating it.
  - Single-step merge/split monotonicity of $F_2$'s fragments as a proof
    mechanism for opening 1 (even restricted to the dominant-$p_2$-over-$R$
    setting): refuted this round, 3844/16000 violations. Consistent with
    (but a strictly narrower/harder-hit instance of) the pre-existing
    `splitting-monotonicity-refuted-dead-end` record from round 7 — do not
    re-propose a pairwise-merge argument here; if opening 1 is pursued it
    needs the full vertex-maximization machinery (opening 2), not a greedy
    step argument.
  - The fully generic (non-ladder) form of opening 1's inequality is FALSE
    — concrete counterexample found ($\tau=\{49,2/5\}$, $m=203/4$,
    3-part split). Do not attempt to prove opening 1 as a pure "$A$-of-
    multisets" fact without using ratio-2/ladder structure on $\tau$; the
    proof will need to invoke that structure somewhere (most likely a
    revised/adapted spacing argument, or the vertex-evaluation step).

- **Small-case / intuition notes (all labeled conjecture, not proof):**
  - Opening 1's bound $A(F_2\cup R)\le p_2-A(R)$ appears to be **tight only
    at the trivial vertex** $F_2=\{p_2\}$ (no cut) — every genuine split
    strictly decreases the value in every sampled instance (max-search gap
    exactly 0, i.e. the untouched piece is the unique-looking maximizer in
    all trials found). This suggests a possible proof strategy: show the
    untouched vertex globally dominates via the vertex-maximization theorem
    directly landing there (i.e. the vertex enumeration might collapse to
    a single case, $p=0$ pins, one tied value $v=p_2$ itself) rather than
    needing to evaluate many vertex types as Case I Closure did — this
    would be a much shorter argument if it can be shown structurally that
    no other vertex type can beat $p=0,v=p_2$ specifically for a dominant
    reference. Purely a numeric hint, not established.
  - The $\ell(F)=2,P\ne\varnothing$ small-$\mathrm{Total}(P)$ sub-branch
    (opening 4) genuinely reduces to a *weaker* instance of the same
    recursive lower bound already used elsewhere in the theorem (needs
    $A(G')\ge f(n)-\mathrm{Total}(P)$, not $A(G')\ge f(n)$), so it should
    not need any new machinery once the outliner threads it through the
    existing $L(n-1)$/rescaling argument the same way Prop 26/28 do.
