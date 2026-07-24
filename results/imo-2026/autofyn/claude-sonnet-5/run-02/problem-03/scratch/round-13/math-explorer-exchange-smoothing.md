## imo-2026-03 (lens: exchange-smoothing-vertex-maximization transplant, Front 1 / Claim B)

### Setup recap (for the outliner, precise definitions used below)
Ladder: $p_i=2^{n+1-i}/D$, $D=2^{n+1}-1$, $i=1,\dots,n+1$. Target for the
lower-bound induction is $A(\text{final multiset})\ge f(n):=1/D=p_{n+1}$
(NOT $p_1$ — I re-derived this from Prop 22's own worked numeric checks,
$f(3)=1/15$, $f(4)=1/31$; $c(n)=2^n/D$ is recovered via $\Phi=(1+A)/2$, i.e.
$c(n)=(1+f(n))/2\cdot$... actually the clean identity used throughout the
project is $\Phi=(Total+A)/2$ and $Total=1$, so $c(n)=(1+f(n))/2$ — sanity
check $n=3$: $(1+1/15)/2=8/15=c(3)$. Correct.) $(\dagger)$ (Prop 21):
$\max\{A(G'):G'$ legal refinement of $\tau=\{p_2,\dots,p_{n+1}\}$, $\le n-2$
cuts$\}\le p_2-f(n)$.

### Distinct openings
1. **(†) is directly a max-A / min-E problem over a multi-piece legal
   refinement — structurally identical in shape to Claim (A)'s Case I
   target, and the SAME two certified tools (exchange-smoothing-vertex-
   maximization + per-piece-vertex-decomposition-theorem) apply to it with
   zero adaptation of their statements.** Case-I-Closure-Theorem proves
   $\max_F E(F\cup\tau)\le R(\tau)$ by (a) reducing the continuum
   maximization to a finite pinned+tied vertex family (exchange-smoothing),
   then (b) evaluating that family in closed form via
   `odd-run-reduction-lemma` + `ratio-2-spacing-lemma` + `last-element-bound`.
   $(\dagger)$ asks for $\max_{G'}A(G')=\max_{G'}(Total(G')-2E(G'))
   =Total(\tau)-2\min_{G'}E(G')$, i.e. a **minimization** of $E$, not a
   maximization — but the exchange-smoothing argument is symmetric (push
   toward $0$/pinned/tied along the SAME affine local-perturbation
   direction works whether you're pushing $E$ up or down: an affine
   functional on a polytope attains BOTH its max and min at vertices of
   the same finite family — this symmetry is already stated explicitly in
   `vertex-minimum-theorem`'s own text, "the minimum (and by symmetry the
   maximum)..."). So step (a) transplants for free with literally no new
   proof needed beyond noting the symmetry. $(\dagger)$'s $G'$ ranges over
   a MULTI-PIECE composition (independent cuts across $p_2,\dots,p_{n+1}$,
   not a single mass split into $k$ parts of one value), which is exactly
   `per-piece-vertex-decomposition-theorem`'s setting (already certified,
   marking-agnostic, proved for the *maximizing-$E$* direction but its
   own proof — "if some $F_i^*$ were not itself optimal... a strictly
   improving deviation would produce a legal global point... contradicting
   global optimality" — is direction-agnostic and reproves verbatim for
   minimizing $E$). **This gives, essentially for free, a full reduction
   of $(\dagger)$ over ALL compositions and ALL splits to a finite
   enumeration** — a genuinely new opening that bypasses the
   self-similarity+induction route Prop 21/22 used (and hence bypasses
   the $(\star_{n-2})$ conditioning entirely, since exchange-smoothing
   needs no induction hypothesis, only the vertex reduction + a direct
   evaluation).
2. **The evaluation step is the real open work, and it is genuinely
   different from Case I's — this is the honest caveat.** Case I's
   evaluation exploited the ratio-2 structure of $\tau$ itself via
   `ratio-2-spacing-lemma`/`last-element-bound`. Here $(\dagger)$'s
   $G'$-polytope is over the SAME ratio-2 tail $\tau$, so those exact
   lemmas may transplant almost verbatim (worth checking directly — this
   is the fastest possible win: literally re-run Case-I-Closure-Theorem's
   proof with reference set $=\varnothing$ and target multiset $=\tau$
   itself, i.e. treat $(\dagger)$ as "Case I of Claim (A) with the roles of
   'pinned tail' and 'moving mass' swapped" — $\tau$ is playing the role
   `exchange-smoothing-vertex-maximization`'s $\tau$ (reference) usually
   plays for Claim (A), but here $\tau$ is itself being refined, so the roles
   are inverted). This inversion needs to be checked carefully — it's not
   an automatic reuse, it's a genuinely new instantiation of the same
   machinery with the "moving" and "fixed" roles swapped, which is exactly
   the kind of thing that has bitten this project before (round 11's
   "NEVER assume Theorem GC(m) transfers... by substitution" rule).
3. **For the $\ell(F)=2$, $P\ne\varnothing$ gap (the round's headline ask):**
   the needed bound is $\max_{G'}A(F_2\cup G')\le p_2-f(n)$ (shifted
   boundary $t^*$ version), where $F_2=\{t^*\}\cup P$ is a FIXED extra
   reference thrown into the union, and $G'$ is again the multi-piece tail
   refinement. This is now even MORE directly `per-piece-vertex-
   decomposition-theorem`'s exact shape: at the joint maximizer, piece $i$'s
   split is optimal relative to $\tau_i:=F_2\cup(\text{other pieces'
   splits})$ — $F_2$ just becomes a permanent extra element appended to
   every piece's own reference set. This is the "genuinely new
   upper-bound-producing mechanism" the round's dispatch note asked to look
   for — I believe it structurally exists (the reduction step), but the
   evaluation is harder than plain $(\dagger)$ because $F_2$'s extra point
   $t^*$ breaks the pure ratio-2 spacing of the reference set (matches
   exactly the obstacle already flagged for the general-upper-bound front:
   "ladder-specific evaluation lemmas... do not transfer" once markings/
   references are no longer pure ratio-2).
4. **Fallback opening if evaluation resists:** even a WEAKER, non-tight
   corollary of the vertex reduction (e.g. bounding the finite vertex
   family crudely via $A\le Total$ on each branch, or via the already-
   certified `half-bound-lemma`, `last-element-bound` used more crudely)
   might be enough — Prop 26's own P=∅ closure already showed the
   necessary target inequality has slack in some regimes; it does not need
   to be proved via an exact closed form, only an upper bound that beats
   $p_2-f(n)$ (or the shifted $t^*$-analogue). This lowers the bar from
   "reprove Case-I-Closure-Theorem's full 3-branch machinery" to "find any
   valid crude bound on the vertex family that suffices."

### Candidate technique(s)
Exchange-smoothing vertex-maximization (dualized to minimization by the
same symmetry already noted in `vertex-minimum-theorem`) + `per-piece-
vertex-decomposition-theorem` (to handle the multi-piece composition) +
`odd-run-reduction-lemma` (to evaluate $A$/$E$ at any resulting vertex) —
exactly the toolkit Case-I-Closure-Theorem used, reused here for a
structurally analogous but polarity-inverted and (for item 3) reference-
perturbed target.

### Cheap-kill candidates
- Numerically confirmed (see below): the maximizer of $(\dagger)$ never
  needs to cut $p_2$ itself (random search restricted to "$p_2$ forced cut"
  configurations stays strictly below the true target at $n=4,5,6$,
  approaching but not reaching it) — this is evidence (not proof) that a
  direct vertex-family argument showing "$p_2$ pinned/untouched dominates
  every vertex where $p_2$ is split" could close $(\dagger)$'s open branch
  in one clean lemma, without needing the harder general evaluation.
  Worth trying as the first, cheapest sub-target: show the exchange-
  smoothing vertex family's maximum is always attained at a vertex with
  $p_2$ pinned (a much narrower claim than fully evaluating every vertex).
- Parity/size check: the reduced problem after per-piece-vertex-
  decomposition has finitely many "pinned + one tied group" configurations
  per piece, but the piece count is $n-1$ (or $n-2$) — the total vertex
  family size grows combinatorially; a cheap first check is whether the
  budget cap ($\le n-2$ or $\le n-1$ cuts total, not per piece) collapses
  most of this combinatorics away (in Case I, the analogous collapse came
  from the budget cap $k\le m+1$) — should be checked before committing to
  full enumeration.

### Knowledge-base entries to use
No `knowledge_base.md` generic entry beyond what's already cited
project-wide (standard LP-vertex/compactness facts, already fully
internalized via the certified lemmas above) — this is a within-project
lemma-transplant question, not a fresh knowledge-base lookup.

### Analogous past problems (cruxes)
Per the established project rule (round 1): the crux corpus has no strong
direct analog for this problem's overall shape (checked in round 1 across
combinatorics/games-and-strategy/extremal-principle/processes-and-
algorithms). I did not find reason to re-search this round — this lens is
about transplanting the project's OWN certified exchange-smoothing lemma
(itself originally crux-adjacent, `aimo-0146`-flavored per round 8's
history) from Claim (A) to Claim (B)'s residual, not about finding a new
external analog. `none new`.

### Prior progress
- $(\dagger)$'s $p_2$-untouched branch: closed conditionally on
  $(\star_{n-2})$ via self-similarity+induction (Prop 22), unconditional
  for $n\le4$.
- $\ell(F)=2$ sub-case (c) at $P=\varnothing$: fully closed (Prop 26,
  conditional only on $L(n-1)$, no new depth).
- $\ell(F)=2$ sub-case (c) at $P\ne\varnothing$: open, precisely diagnosed
  as needing an UPPER bound on a quantity ($\psi(t^*)=A(F_2\cup G')$) that
  every existing Claim-B lemma only lower-bounds.
- $(\dagger)$'s $p_2$-cut complement: open, numerically supported
  (Prop 22's own 80k-trial checks + my fresh checks below), never proved.

### Dead ends (do not retry)
- None new found this round. Re-confirm existing dead ends still apply:
  parity/$\ell(S)$-induction (round 8) and naive "swap dominant element"
  (round 10) are irrelevant here since this is a genuinely different
  (vertex-reduction, not peel-induction) mechanism.

### Small-case / intuition notes (all CONJECTURE / numeric evidence, not proof)
Fresh exact-`Fraction` checks (this round, `/tmp` scripts, not reused from
prior rounds):
- Confirmed $(\dagger)$'s exact target $p_2-f(n)$ empirically for
  $n=2,3,4,5$ (15,000–20,000 trials each, random legal multi-piece
  refinements at budget exactly $n-2$): exact match every time
  ($n=2$: $1/7$; $n=3$: $1/5$; $n=4$: $7/31$; $n=5$: $5/21$).
- Confirmed the empirical maximizer always leaves $p_2$ untouched (its
  fragment list always contains the literal value $p_2$ unsplit) at
  $n=3,4,5$.
- Confirmed a "$p_2$ forced to be cut at least once" restricted search
  stays **strictly below** the target at $n=4$ ($43743/193750\approx
  0.22577 < 7/31\approx0.22581$), $n=5$ ($\approx0.23767<0.23810$), $n=6$
  ($\approx0.24020<0.24409$, gap larger here likely due to weaker random
  search coverage for the bigger vertex family, not a real gap) —
  consistent with (but not proof of) the conjecture that $p_2$-pinned
  vertices always dominate $p_2$-cut vertices for this specific
  maximization, which would be exactly the missing piece to close
  $(\dagger)$ unconditionally via the vertex-maximization route instead of
  Prop 22's conditional induction.
- I did not have time this round to run the full finite-vertex enumeration
  itself (per-piece pinned+tied family, cross-checked against continuum
  search) for $(\dagger)$ or for the $\ell(F)=2$, $P\ne\varnothing$
  shifted-boundary target — recommend the next builder round start there:
  write the enumeration explicitly for $n=3,4$ and check it reproduces
  Prop 22's already-known exact values, before attempting the general-$n$
  closed-form evaluation.
