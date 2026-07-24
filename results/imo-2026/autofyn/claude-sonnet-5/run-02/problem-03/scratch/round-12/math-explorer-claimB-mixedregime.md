## imo-2026-03 — lens: Claim (B) mixed-regime ℓ(F)=2 sub-case (sub-case (c))

### 1. What exactly is the "one budget unit" gap

Setting (all from `greedy-halving-adversary.md`, certified Lemma 25 / Theorem
P(n)): $F=\{v_1,v_2\}\cup P$ is Xiang Yu's split of $p_1$ with $\ell(F)=2$
($v_1>v_2$, $P$ exactly-paired). Sub-case (c) is the *mixed regime*
$v_1\ge p_2>v_2$. Lemma 25 + Proposition 20 give the **exact identity**
$$A(F\cup G') = v_1 - A(F_2\cup G'),\qquad F_2:=\{v_2\}\cup P,$$
so closing Claim B here is equivalent to proving the **upper bound**
$A(F_2\cup G')\le v_1-f(n)$ (where $f(n)=1/(2^{n+1}-1)=2c(n)-1$ is the
project's `A`-scale target, $c(n)=2^n/(2^{n+1}-1)$).

- **What Proposition 21/22 supply:** an upper bound $(\dagger)$: $\max_{G',\,
  \le n-2\text{ cuts}} A(G') \le p_2-f(n)$, valid **only** for *bare* tail
  refinements $G'$ (no extra residual attached), and only because
  Lemma 19's cut-count fact forces $\ell(F)=1$, $v<p_1$ configurations to use
  $c\ge2$ cuts on $p_1$, capping the tail's budget at $n-2$.
- **What sub-case (c) needs:** $F_2=\{v_2\}\cup P$ is itself an $\ell(F_2)=1$
  configuration with residual $v_2<p_2$ — but here $\ell(F)=2$ can arise from
  as few as **$c=1$** cut on $p_1$ (single unequal split, $P=\varnothing$,
  $v_1+v_2=p_1$), so the tail's cut budget is only capped at $n-1$, not $n-2$.
  Also — this is important and NOT clearly separated in the approach file —
  the target quantity is not literally "$(\dagger)$ at budget $n-1$" with the
  *same* right-hand side $p_2-f(n)$: since $v_1=p_1-v_2$ (not a free
  parameter equal to $p_2$), the actual needed bound is the **v₂-dependent**
  inequality
  $$(\ddagger)\qquad A(\{v_2\}\cup G') \;\le\; (p_1-v_2) - f(n),\qquad
  \forall\, v_2\in(0,p_2),\ G' \text{ legal, }\le n-1\text{ cuts}.$$
  Numerically (see §3) this is **tight** (margin $\to 0$) exactly as
  $v_2\to p_2^-$, i.e. as $v_1\to p_2^+$ — so the "one more budget unit" is
  only exercised in the extremal corner where $v_1$ is barely above $p_2$,
  not uniformly across all $v_2$.

### 2. Extending Prop 21/22's own technique, or a different mechanism?

**Numeric check (exact `Fraction`, n=3,4,5, see §3) shows the naive literal
extension is FALSE**: replacing $(\dagger)$'s target with the *same* fixed
bound $p_2-f(n)$ at budget $n-1$ (i.e. treating $\{v_2\}\cup G'$ as if it
were just "$(\dagger)$ one cut richer") is violated by a comfortable margin
at every $n$ tested (best found $\approx0.265$ vs. target $\approx0.2$ at
$n=3$). So a mechanical "push Proposition 22's induction one level deeper
with the same statement" does **not** work — this is a genuine dead end, not
just unattempted, and next round should not waste a build cycle re-deriving
it verbatim.

However, the **correctly-stated** inequality $(\ddagger)$ (with $v_1=p_1-v_2$
substituted in, not a fixed constant) numerically holds with vanishing
margin as $v_2\to p_2$ — i.e. it is true and tight, not just true with slack.
This points to a genuinely different mechanism than a flat budget bump:

- The tightness concentrating at $v_2\to p_2$ suggests the right proof
  should isolate that corner via a **continuity/limiting argument that
  reduces to Proposition 22's already-closed configuration exactly at the
  boundary** ($v_2=p_2$ is the boundary between sub-case (c) and sub-case
  (a)/(the $\ell(F)=1$, $v=p_2$ boundary), and show the "extra slack" $v_1-p_2
  = p_2-v_2$ exactly compensates the increased freedom from one more cut, as
  $v_2$ moves away from $p_2$. This smells like a **first-order/derivative
  trade-off argument** (in the style of round 4/9's "the trade-off is
  genuinely tight" cross-term analyses), not a fresh induction.
- Alternatively: note $F_2\cup G' = \{v_2\}\cup G'$ where, after rescaling
  $\tau/r$ to the $(n-1)$-ladder, $G'/r$ ranges over the **entire, full**
  budget ($n-1$ cuts) of the $(n-1)$-ladder — i.e. $G'$ is not a
  *restricted* sub-instance anymore but an **unrestricted** legal response to
  a full $(n-1)$-level sub-problem, with one extra floating value $v_2$
  attached from a different original scale. This is structurally close to
  Claim (A)'s setup (a full free legal response, plus one extra unpaired
  value) — worth checking whether **Claim (A)'s already-fully-closed
  machinery** (exchange-smoothing vertex-maximization, Ratio-2 Spacing
  Lemma, Last-Element Bound — all cited/certified in `lemmas/claim-a-full-
  closure.md`) can be imported/adapted here, since Claim (A) already solved
  "one extra distinguished element interacting with a fully-free response"
  in the achievability/upper-half direction. This is a genuinely different
  import candidate from Claim (B)'s own peel/self-similarity toolkit, and to
  my knowledge has not yet been tried on this specific sub-case.
- A third option, cheaper to try first: since the gap is only live in the
  narrow corner $v_2$ near $p_2$ (elsewhere $(\ddagger)$ has real slack per
  the numerics), consider **splitting $(\ddagger)$ into two ranges**: $v_2\le
  p_2-\epsilon(n)$ (closeable perhaps by the *existing* $(\dagger)$ machinery
  with a cruder bound, since there is slack) and $v_2\in(p_2-\epsilon(n),p_2)$
  (a small-perturbation/continuity argument near the already-solved boundary
  $v_2=p_2$). This is the kind of "two-regime" split the upper-bound front
  (`lp-duality-certificate`) has used successfully elsewhere (e.g. $p_1\ge
  T/2$ vs. $p_1<T/2$), so it's a technique already validated in this project,
  just not yet applied to this exact residual.

### 3. Numeric sanity checks (exact Fraction, n=3,4,5 — conjectural evidence only)

Script used: random legal tail refinements generated respecting per-piece
boundaries and cut-budget, `Fraction` arithmetic throughout (no floats).

- Confirmed Proposition 22's certified bound $(\dagger)$ at budget $n-2$:
  max bare $A(G')$ found $= p_2-f(n)$ **exactly** at $n=3,4,5$ (matches the
  certified closed form, consistent with existing certification — not new).
- **Naive extension false:** at budget $n-1$, max bare $A(G')$ found
  $\approx0.265$ ($n=3$), $0.254$ ($n=4$), $0.247$ ($n=5$) — all **exceed**
  the fixed target $p_2-f(n)\approx0.2,\,0.226,\,0.238$. So literally bumping
  $(\dagger)$'s budget by one with the same right-hand side is refuted.
- **Correct v₂-dependent inequality $(\ddagger)$ holds, tight at the
  boundary:** minimum margin $A(F\cup G')-f(n)$ found over $60000$ trials at
  budget $n-1$, ranging $v_2$ freely in $(0,p_2)$: $n=3$: margin
  $\approx0.00005$ ($1/18750$); $n=4$: $\approx0.0069$; $n=5$: $\approx
  0.0166$ — all non-negative (no violation found), with the minimum
  occurring at $v_2\to p_2^-$ in every case tested. This is **conjectural**
  (finite random search, not exhaustive vertex enumeration) but consistent
  and non-trivial (the margin is genuinely small, not just numerically
  noisy) — a real target for next round's proof, not just a hopeful guess.

### 4. Knowledge base / crux corpus

- `knowledge_base.md`: nothing beyond what's already cited in the
  approach (extremal principle / induction-and-construction generic
  entries); no new specific entry stands out for this narrowed gap.
- Targeted crux-corpus query this round (`combinatorics` domain,
  subtopics `extremal-principle`, `games-and-strategy`,
  `processes-and-algorithms`, `inequalities-SOS-and-convexity`,
  `invariants-and-monovariants`, filtered for induction+budget/recursion/
  peel language): only 3 hits, and the closest (`aimo-0965`, "peel off the
  object built on the LONGEST relevant diagonal", extremal-principle) is
  **not a strong analog** — it's a dissection/geometry induction whose
  "peel the extremal object, sub-regions add with no double count" shape is
  already exactly what this project's own `dominant-element-removal-identity`
  / `sharp-dominant-removal-identity` mechanism does; it offers no new
  leverage on the specific "attach one floating residual to a fully-free
  one-level-down instance" obstruction identified in §2. Confirms prior
  rounds' finding: **no strong direct crux analog for this problem**, and
  this narrower sub-case is no exception — don't spend further round budget
  re-querying the corpus for it specifically.

### Report summary

- **Distinct openings:** (i) prove the corrected $v_2$-dependent inequality
  $(\ddagger)$ directly via a boundary/continuity argument anchored at the
  already-solved $v_2=p_2$ case (Proposition 22); (ii) try importing Claim
  (A)'s exchange-smoothing vertex-maximization machinery, since sub-case (c)'s
  reduced object (one floating residual + a *fully free*, full-budget
  $(n-1)$-level response) structurally resembles Claim (A)'s own setup more
  than Claim (B)'s peel/self-similarity toolkit; (iii) split $(\ddagger)$
  into a "slack" range (crude bound suffices) and a "tight corner" range
  ($v_2$ near $p_2$) as the upper-bound front has done successfully elsewhere
  (two-regime split).
- **Candidate technique(s):** exchange-smoothing/vertex-maximization
  (imported from Claim A) as the most promising fresh mechanism; boundary
  continuity/derivative argument as a cheaper first attempt.
- **Cheap-kill candidates:** before deep work, check whether $(\ddagger)$
  can be killed/simplified by noting $P$ is forced empty exactly at the
  minimal-cut witness ($c=1$) — the case that matters most since it's the
  one exercising the full $n-1$ budget; larger $c$ (with nonempty $P$)
  automatically has strictly less tail budget, so (per the monotonicity
  remark pattern already used for $(\dagger)$) it suffices to check
  $(\ddagger)$ only at $P=\varnothing$ — this halves the case-analysis work
  needed and should be verified/stated explicitly by whoever builds this.
- **Knowledge-base entries to use:** none beyond what's already cited
  (`dominant-element-removal-identity` / `sharp-dominant-removal-identity`,
  `tail-self-similarity`, `cross-term-identity-threshold`,
  `exchange-smoothing-vertex-maximization` as an import candidate from the
  Claim-A side).
- **Analogous past problems (cruxes):** none strong — `aimo-0965`
  (extremal-principle, "peel the longest/extremal object so sub-regions
  don't double-count") is the closest hit from a targeted query this round
  but only restates a mechanism already in use here (dominant-element
  removal), not new leverage. Confirms the standing finding: no direct
  crux analog for this problem.
- **Prior progress:** Theorem P(n) (Lemma 25, sub-cases (a)/(b)/(c) of
  ℓ(F)=2) fully proved and certified for sub-case (a) (conditional on
  L(n-1) only, no new depth) and precisely reduced (not closed) for (b)/(c);
  P(3) unconditionally closed. Sub-case (c)'s exact reduction to $A(F\cup
  G')=v_1-A(F_2\cup G')$ is itself solid, certified machinery (Lemma 25 +
  Prop 20) — the *only* missing piece is the upper bound $(\ddagger)$ on
  $A(F_2\cup G')$ identified above.
- **Dead ends (do not retry):** literally extending $(\dagger)$'s fixed
  bound $p_2-f(n)$ to budget $n-1$ without substituting $v_1=p_1-v_2$ for
  the constant $p_2$ — refuted numerically this round (§3), comfortable
  margin of violation, not a close call. Do not re-attempt this exact
  "flat budget bump" shortcut; any fix must be $v_2$-dependent.
- **Small-case / intuition notes (conjecture only, exact-Fraction random
  search, not exhaustive):** the corrected inequality $(\ddagger)$ appears
  true and tight exactly at $v_2\to p_2^-$ for $n=3,4,5$; away from that
  corner there is real numeric slack. This suggests the extremal
  configuration for sub-case (c) sits right at its own boundary with
  sub-case (a)/the closed $\ell(F)=1,\,v=p_2$ case — a structural hint that
  whatever proof closes it will look like a perturbation of Proposition 22's
  argument near that boundary, plus a separate (easier) argument for the
  rest of the $v_2$ range.
