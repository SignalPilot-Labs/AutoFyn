## imo-2026-03 (lens: residual region for n=3 upper bound, p1>=T/2 corner)

### The precise residual region

From `lemmas/case-b2-n3-covering-closure.md`'s round-26 correction and
`current.md`'s round-26 entry: with $T=p_1+p_2+p_3+p_4$ normalized to $1$,
$D_3=15$, $a_3=8/15$, the **exact open region** not yet covered by any
certified mechanism is
$$\mathcal R := \Big\{(p_1,p_2,p_3,p_4):\ p_1\ge p_2\ge p_3\ge p_4>0,\
p_1\ge T/2,\ \ T/15 < p_2 < 4T/15\Big\}.$$
This is exactly case (b2)'s own box ($T/15<p_2<4T/15$) intersected with
$p_1\ge T/2$ — the complement, within that box, of the already-certified
`case-b2-n3-covering-closure` (which is scoped to $p_1<T/2$). It is
disjoint from "case (a)" ($p_2\ge 4T/15$, closed by the Corollary to
Theorem B / `n2-upper-bound-lp-argument`) and from "case (b1)"
($p_2\le T/15$). The round-26 reviewer's witness
$p=(3/5,\,9/40,\,29/200,\,3/100)$ ($p_1=0.6\ge1/2$, $p_2=0.225\in(1/15,4/15)$)
lies in $\mathcal R$ and defeats all five chambers of
`case-b2-n3-covering-closure` (Bisect$\{1,4\}$, Bisect$\{1,2\}$, DS-Above,
Triple-Pin, R22.1.1) as literally stated.

### Key structural fact: Triple-Pin's formula bifurcates at $p_1=T/2$

The Triple-Pin chamber (composition $(2,0,0,0)$: split $p_1$ into
$(p_2,\,p_3,\,v_3)$ with $v_3=p_1-p_2-p_3$, feasible iff $p_1>p_2+p_3$) was
derived in `approaches/lp-duality-certificate.md` §R24.3 under the order
$p_4>v_3$, which the derivation explicitly obtains from $p_1<T/2$ (since
$p_1<T/2\Rightarrow v_3=p_1-p_2-p_3<T-p_1-p_2-p_3=p_4$). Redoing the same
odd-run-reduction computation for $v_3>p_4$ (which happens **exactly** when
$p_1>T/2$, since $v_3>p_4\iff p_1-p_2-p_3>p_4\iff p_1>T-p_1$) gives the rank
order $v_3$ (rank 1, +), $p_4$ (rank 2, −), so $A(M)=v_3-p_4=2p_1-T$ and
$$\Phi_{\text{TriplePin}}(p)=\frac{T+2p_1-T}2=p_1\qquad(p_1\ge T/2).$$
So on the $p_1\ge T/2$ side, Triple-Pin's corrected formula is
$\Phi_{\text{TriplePin}}=\max(p_1,\,T-p_1)$ globally, i.e. $=p_1$ once
$p_1\ge T/2$ — exactly the value the round-26 reviewer flagged as the
correction, but not previously written out in closed form. Consequence:
Triple-Pin (corrected) **succeeds** on $\mathcal R$ whenever $p_1\le
8T/15=a_3T$ and $p_1>p_2+p_3$ (feasibility) — i.e. it already covers the
sub-strip $T/2\le p_1\le 8T/15$ with $p_1>p_2+p_3$. It necessarily **fails**
once $p_1>8T/15$ (since $\Phi=p_1$ itself already exceeds the target),
which is exactly what happens at the round-26 witness ($p_1=3/5>8/15$).

### A new chamber that appears to close the rest of $\mathcal R$

Composition $(1,1,0,0)$, but **not** the already-certified
`chamber-a2-p1-tied-to-p2-pair` / P1P2-tied-to-$p_3$ chamber: **exactly
bisect $p_1$** (one cut, $v_1=v_2=p_1/2$ — a same-piece equal pair, so it
cancels *unconditionally*, by `odd-run-reduction-lemma`, regardless of
where it sits in the global order — this reuses the exact mechanism behind
the already-certified Bisect-Subset family), and **split $p_2$ into
$(w_1,w_2)$** (one cut) chosen so that the order is $w_2>p_3>w_1>p_4$, i.e.
$w_1\in(p_4,\ p_2-p_3)$ — feasible iff $p_2>p_3+p_4$. Only 2 cuts used
(legal at $n=3$). After $p_1$'s pair cancels, $M'=\{w_1,w_2,p_3,p_4\}$ and,
throughout the feasible interval for $w_1$, the order $w_2>p_3>w_1>p_4$ is
fixed, giving (independent of exactly where $w_1$ sits in that interval)
$$A(M')=w_2-p_3+w_1-p_4=(w_1+w_2)-p_3-p_4=p_2-p_3-p_4,$$
so
$$\Phi_{\text{Bisect1-Sandwich2}}(p)=\frac{T+p_2-p_3-p_4}2,\qquad
\text{feasible iff } p_2>p_3+p_4,$$
succeeding ($\Phi\le a_3T$) iff $p_2\le p_3+p_4+T/15$. **This is a genuine
new closed form, not previously on file** (distinct from Bisect$\{1,2\}$,
which bisects *both* $p_1$ and $p_2$ and gives $\Phi=(T+p_3-p_4)/2$ — a
strictly worse value here — and distinct from Chamber A2/B1/B2, which tie
fragments of $p_1$ to $p_2$/$p_3$ rather than bisecting $p_1$ cleanly).

**Direct check at the round-26 witness** $p=(3/5,9/40,29/200,3/100)$:
$p_2=9/40=0.225$, $p_3+p_4=29/200+3/100=7/40=0.175<p_2$ (feasible), and
$$\Phi_{\text{Bisect1-Sandwich2}}=\frac{1+9/40-7/40}2=\frac{1+1/20}2
=\frac{21}{40}=0.525\ \le\ 8/15\approx0.5333.$$
**This one new chamber alone defeats the round-26 "all five fail"
witness** — a concrete positive result on the exact point that broke the
domain-widening bonus.

### Numeric coverage check (conjecture, not yet a proof)

Combining the corrected Triple-Pin ($\Phi=\max(p_1,T-p_1)$), the existing
20-chamber family from `approaches/lp-duality-certificate.md` §R24.4
(15 Bisect-Subset chambers + DS-Below/Above + Triple-Pin + B1/B2 +
P1P2-tied-to-$p_3$ + R22.1.1 + Chamber A/A2), and this new
Bisect1-Sandwich2 chamber:
- Exact rational grid search over $\mathcal R$ (denominator up to 250,
  restricted to $p_1\ge T/2$, $T/15<p_2<4T/15$, sorted $p_1\ge p_2\ge p_3\ge
  p_4>0$): **zero points where all chambers fail** (`/tmp/probe2.py`).
- Independent random exact-`Fraction` search, ~200,000 trials sampled
  directly inside $\mathcal R$ (not just the grid): **zero violations**
  (`/tmp/round-27's` verification, reproducible via the same script logic).
- Without the new chamber, the same grid/random search reproduces the
  known failures (e.g. the round-26 witness, plus a whole cluster near
  $p\approx(0.54,\,0.23{-}0.25,\,0.15,\,0.075)$, margin $\approx0.003$–$0.005$
  above $8/15$) — confirming these are genuine gaps in the old 5/20-chamber
  family, not sampling noise, and that the new chamber specifically plugs
  them.

**This is strong numeric evidence, not a proof**, that
$\{\text{20-chamber family}\}\cup\{\text{corrected Triple-Pin}\}\cup
\{\text{Bisect1-Sandwich2}\}$ covers all of $\mathcal R$. An exact Farkas-style
covering argument (in the style of `case-b2-n3-covering-closure`'s own
6-branch proof) has **not** been attempted — that is the natural next
step for a builder, and the two "moving parts" needed are exactly (a) the
corrected Triple-Pin formula bifurcation at $p_1=T/2$ (derived above,
essentially free — same computation as the existing §R24.3 argument, just
the other order branch) and (b) formalizing Bisect1-Sandwich2's feasibility
and value as a lemma (the computation above is already a complete,
non-numeric derivation from `odd-run-reduction-lemma`, just not yet written
up as a standalone certified lemma file).

### Candidate technique(s)
- Same LP/chamber-covering machinery already in use
  (`cross-piece-sign-assignment-identity`, `odd-run-reduction-lemma`,
  Bisect-Subset Lemma) — no new machinery needed, just two new/corrected
  chamber formulas plus a Farkas-style exhaustive case split analogous to
  `case-b2-n3-covering-closure`'s own proof, restricted to $\mathcal R$.

### Cheap-kill candidates
- None beyond what's already exploited: the corrected Triple-Pin formula
  already for free covers $T/2\le p_1\le 8T/15$ (a simple algebraic
  observation, $\Phi_{\text{TriplePin}}=p_1\le a_3T$), cutting $\mathcal R$
  roughly in half before any new chamber is needed for $p_1>8T/15$.

### Knowledge-base entries to use
- `odd-run-reduction-lemma`, `cross-piece-sign-assignment-identity`
  (certified lemmas already in `results/imo-2026-03/lemmas/`) — the new
  Bisect1-Sandwich2 chamber is a direct, elementary corollary of these,
  exactly as every other chamber in the family is.

### Analogous past problems (cruxes)
Not separately queried this round (scope was narrow, numeric/algebraic
probing of one specific residual region); the existing chamber-covering
machinery already in the approach file is the load-bearing technique and
was built without needing external crux imports (per rounds 22-26's own
record). No new crux search performed — flag for a future round if this
lens needs restarting from scratch.

### Prior progress
`case-b2-n3-covering-closure` (certified, but scoped to $p_1<T/2$ only) is
the furthest correct progress on the box $T/15<p_2<4T/15$; case (a)
($p_2\ge4T/15$) is separately closed via `n2-upper-bound-lp-argument`'s
Corollary. The $p_1\ge T/2$, $T/15<p_2<4T/15$ corner ($\mathcal R$ above)
was, until this round's probing, entirely uncovered by any written
mechanism (round 26 found the counterexample but proposed no fix).

### Dead ends (do not retry)
- Do **not** re-attempt "the 5-chamber family's Farkas certificates never
  literally mention $p_1$ vs $T/2$, so the restriction can be dropped for
  free" — this is exactly the round-26 overclaim the reviewer refuted;
  Triple-Pin's derivation silently uses $p_1<T/2$ to fix an ordering, and
  the corrected formula for $p_1\ge T/2$ is $\Phi=p_1$, not $T-p_1$ — see
  above for the actual fix (bifurcate, don't just drop the restriction).
- The existing 5-chamber family (Bisect$\{1,4\}$, Bisect$\{1,2\}$, DS-Above,
  uncorrected Triple-Pin, R22.1.1), **as literally stated with the old
  Triple-Pin formula**, is confirmed (independently reproduced) to fail at
  the round-26 witness and at a broader cluster near
  $p\approx(0.54,0.23,0.15,0.075)$ — do not re-check this exact family
  without the corrected Triple-Pin and the new chamber below.

### Small-case / intuition notes (conjecture, numerically supported)
- Corrected Triple-Pin ($\Phi=\max(p_1,T-p_1)$) plus the new
  Bisect1-Sandwich2 chamber ($\Phi=(T+p_2-p_3-p_4)/2$, feasible iff
  $p_2>p_3+p_4$) together appear, from exact grid + random search
  (zero violations across ~450,000+ combined sample points), to fully cover
  $\mathcal R$ when added to the existing 20-chamber family — this is a
  concrete, checkable conjecture ready for a builder to try to turn into an
  exact Farkas-style proof (likely a small case split on $p_1$ vs $8T/15$
  and $p_2$ vs $p_3+p_4$, structurally similar in size to
  `case-b2-n3-covering-closure`'s existing 6-branch argument).
- The two mechanisms' natural boundary is $p_1=8T/15$ (where corrected
  Triple-Pin stops succeeding) — worth checking whether Bisect1-Sandwich2
  alone (or in combination with one more existing chamber) already succeeds
  for all $p_1>8T/15$ within $\mathcal R$, which would make the case split
  even cleaner. Not verified separately from the combined grid check above;
  a builder should isolate this.
