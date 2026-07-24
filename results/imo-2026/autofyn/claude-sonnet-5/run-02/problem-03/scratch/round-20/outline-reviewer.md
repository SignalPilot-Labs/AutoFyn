# Outline review — round 20, imo-2026-03

## rank-pigeonhole-budget — APPROVE

**Target:** fix the `v2=p4` boundary bug in §7.5's unconditional $n=3$
middle-band closure (`Delta(3,v2) <= s-(v1-v2)`, i.e. $(\sharp)$).

**Verification performed.** Read the live §7.5 text (approaches/
rank-pigeonhole-budget.md:727-760) and independently re-derived the case
split by hand:

- The current (buggy) file splits `v2>=p3`, `v2 in (p4,p3)`, `v2<=p4`.
  At `v2=p4` exactly, `p4` is **not** `>v2` (strict convention used
  everywhere else in the file, `truncated-alternating-sum-ceiling`/
  `-floor`), so `tau_{>v2}` should be `{p3}` only, not `{p3,p4}` — the old
  third case's formula (`Delta=-A(tau)=-p4`) is wrong for `v2=p4`
  specifically; the correct value there is `Delta=A(tau)-2p3=-3p4` (the
  second case's formula).
- Confirmed this is exactly the bug round 19 already flagged (current.md
  round-19 log) and that it was **not fatal to the theorem** (the wrong
  value `-p4` is larger than the true `-3p4`, so the theorem's proof
  accidentally proved a strictly stronger inequality at that one point) —
  but the outline is right that the case split itself needs a clean fix
  before this can be called correct as *written*.
- Re-derived the outline's proposed fix — `v2>=p3`, `v2 in [p4,p3)`
  (closed left), `v2<p4` (open right) — and checked:
  - **Exhaustiveness/no gap:** with `p4<p3<s` (ladder), `[0,p4) ∪
    [p4,p3) ∪ [p3,s) = [0,s)` exactly, no overlap, no gap.
  - **Middle case unchanged on the extended domain:** the formula
    `Delta=A(tau)-2p3=-3p4` only depends on `tau_{>v2}={p3}`, which is
    true for *every* `v2` in `[p4,p3)` including the left endpoint (at
    `v2=p4`, `p4` is excluded, `p3` is included since `p3>p4=v2`) — so
    extending the interval to include the boundary point does not change
    the formula or its proof (the bound only used `v2>0`, satisfied at
    `v2=p4`).
  - **Third case (`v2<p4`) unchanged on the restricted domain:** formula
    `Delta=-A(tau)=-p4` requires `tau_{>v2}=tau`, true exactly when
    `v2<p4` strictly — matches.
  - **First case boundary (`v2=p3`) was already correct** (`p3` not `>v2`
    at `v2=p3`, so `tau_{>v2}=empty`, matching the outline's own note) —
    confirmed by hand, no fix needed there.
- This is a genuine pure case-boundary relabel, not new algebra — the
  outline's claim is accurate and verified.

**Verdict: APPROVE.** Sound, minimal, load-bearing fix; correctly scoped
(does not touch §7.6's honestly-open general-$n\ge4$ gap). No changes
needed to the outline.

---

## greedy-halving-adversary — APPROVE, with one clarifying note

**Target:** close Theorem 35's Case (b) ("$p_3$ is cut") at $n=3,4$ via
reframing the whole $R'=\{a,b\}\cup T'$ (not just $B=\{b\}\cup T'$) as a
legal response to the $(n-2)$-ladder $\{p_3,\dots,p_{n+1}\}$, then
substituting the unconditionally-closed full theorems at $n-2\in\{1,2\}$.

**Verification performed.**

1. **The reframing is mathematically legitimate, non-circular.**
   $\{p_3,\dots,p_{n+1}\}$ is exactly (rescaled) the $(n-2)$-ladder: with
   $p_i=2^{n+1-i}f(n)$, the sequence $p_3,\dots,p_{n+1}$ has ratios
   $2^{n-2},\dots,2,1$ — the same ratio pattern as a standard $(n-2)$-ladder
   (which has $n-1$ pieces, matching the count here). Producing
   $R'=\{a,b\}\cup T'$ from this tail costs exactly $1+(\le n-4)=\le n-3$
   cuts, matching the already-corrected (round 19) cap on $R'$ exactly —
   so $R'$ is indeed a legal $(n-2)$-ladder response using the level-$(n-2)$
   analog of Xiang Yu's own budget. Applying the level-$(n-2)$ version of
   the *same* theorem to it, via strong induction with $n-2<n$, is a valid
   (not circular) recursion, structurally identical in kind to the already
   -certified use of `tail-self-similarity` in Theorem 34's own proof (one
   level up). Confirmed the outline's own "Watch out for" note is correct:
   the IH genuinely needs the *full* theorem (Claim A+B+middle-band) at
   level $n-2$, and only $n-2\in\{1,2\}$ currently have that unconditionally
   — so the recursion tower climbs by $+2$, not by an arbitrary $n-2$;
   $n=3,4$ are the only currently-available free instantiations, as stated.

2. **Correction to the outline's own framing at $n=3$ (non-fatal, worth
   flagging to the builder).** The outline frames $n=3$ as needing "direct
   substitution using $c(1)$'s closure," implying a genuine (if small)
   computation. In fact, at $n=3$ the corrected cap gives $R'$ a total
   budget of $n-3=0$ — **zero cuts available**, so $p_3$ *cannot* be cut at
   all. "Case (b): $p_3$ is cut" is therefore **vacuously empty at $n=3$**,
   not merely "closes for free by substitution" — there is nothing to
   substitute into, the case simply does not arise (this matches
   `rank-pigeonhole-budget`'s own §7.5 finding that budget $0$ forces
   $R'=\tau$ exactly). This makes $n=3$ *even easier* than the outline's
   plan suggests, but the builder should record the correct reason (vacuity,
   not substitution) rather than force through an unnecessary computation.
   $n=4$ ($n-3=1$ cut available, genuinely non-vacuous) is where the
   substitution argument is actually needed and non-trivial.

3. **Spot-checked $n=4$'s target inequality numerically** (independent
   script, not reusing any builder script): sampled 20,000 random
   $(a,b,v)$ with $a+b=p_3=4/31$, $a\ge b>0$, $T'=\{p_4,p_5\}$ untouched
   (forced, since the single cut is spent splitting $p_3$), $v\in(0,s)$ —
   found the target inequality $\Delta(4,v)\le v-f(4)$ holds in every
   trial (minimum margin $\approx1.4\times10^{-4}>0$, no violations). This
   is consistent with (does not prove) the plan succeeding at $n=4$; it
   rules out the possibility that the plan is chasing a false statement.

4. **Honest scoping confirmed adequate.** The outline correctly flags, as
   an explicit open item rather than silently assuming coverage, that a
   legal "$p_3$ is cut" response may split $p_3$ into 3+ pieces or further
   split $b$ — the current reframing only covers the single-cut-on-$p_3$
   sub-case. This matches CLAUDE.md's no-hand-waving rule; the outline does
   not overclaim.

**Verdict: APPROVE**, with one instruction added for the builder: state
$n=3$'s closure as a **vacuity** (budget $n-3=0$ forces $R'=\tau$, so
Case (b) never arises), not as a substitution computation — this is
simpler and removes any risk of the builder writing an unnecessary/awkward
"trivial substitution" argument. $n=4$'s substitution is the first
genuinely non-trivial instance of the plan and should be the actual focus.

---

## lp-duality-certificate — RETHINK (the probabilistic-method mechanism as
outlined; not the whole slug)

**Target as outlined:** close case (b2) via "probabilistic method +
derandomization" — randomize Xiang Yu's cut position continuously,
bound $E[\Phi]\le a_nT$ via a closed-form integral, then invoke
$\min_x\Phi(x)\le E[\Phi]$ to get a deterministic witness.

**Verification performed — this is the load-bearing check the dispatch
asked for, and it fails.** The outline's own step 1 correctly identifies
the risk (collapsing into the dead **Convex-Combination Futility
Theorem**) and argues the randomization is safe *because* it is over a
continuous parameter, not a finite named family. I checked this claim
directly against the certified theorem's actual proof
(`lemmas/convex-combination-futility-theorem.md`):

- The Futility Theorem's proof uses only two facts: (i) $\min_i\Phi_i\le
  \sum_i\lambda_i\Phi_i$ for any nonnegative weights summing to 1 (trivial
  "min $\le$ average"), and (ii) if $\Phi_i(p)>\theta(p)$ for *every* $i$,
  then *every* nonnegative-weighted combination also exceeds $\theta(p)$.
  **Neither fact uses finiteness of the index set anywhere** — (i) is the
  elementary measure-theory fact $\mathrm{ess\,inf}(\Phi)\le\int\Phi\,d\mu$
  for *any* probability measure $\mu$ (density $f$ on a continuum
  included), and (ii)'s proof is a term-by-term sum that generalizes
  verbatim to an integral: if $\Phi(x)>\theta$ pointwise, then
  $\int\Phi(x)f(x)dx>\theta\int f(x)dx=\theta$ for any density $f$.
- Consequently the theorem's content — **"a weighted/probabilistic
  combination can certify a marking iff the plain pointwise minimum
  already does"** — applies verbatim whether the family is a handful of
  named strategies or a continuum of cut positions. The outline's central
  claim ("this is the precise reason the Futility Theorem does NOT apply
  here — it only rules out combining a FIXED, FINITE set... not
  integrating a continuous function against a density") is **false**; the
  finiteness was never load-bearing in the certified proof.
- Concretely: proving $E_X[\Phi(X)]\le a_nT$ (outline step 3) is
  **provably at least as hard as, and in general strictly harder than**,
  proving $\min_x\Phi(x)\le a_nT$ directly (outline's actual target),
  since $E[\Phi]\ge\min_x\Phi(x)$ always. The "derandomization" step
  (step 4) adds no leverage — it is the same tautology the Futility
  Theorem already isolates and disposes of. This is not a numeric
  coincidence to be caught by the outline's own suggested cheap check
  (uniform density vs. two witnesses); it is a structural fact true for
  *every* choice of density $f$, so no density-tuning in step 3 can ever
  escape it.

This is exactly the "wrong technique / plausible-looking dead end" case
the reviewer role is meant to catch before build effort is spent — the
mechanism cannot work as designed, for any choice of the free parameters
(density, randomization scheme) the outline leaves open.

**What survives and should be redirected (not a full loss).** Step 2's
concrete idea — write $\Phi(x)$ in closed form as a function of a single
continuous cut position $x$ (via the certified Theorem C/D-style
identities), then find the *specific* $x^\ast$ minimizing $\Phi(x)$
directly by calculus/algebra and show $\Phi(x^\ast)\le a_nT$ — is a
legitimate, not-yet-tried construction (previously the field tried only
finitely many *named* templates plus weighted combinations of them, never
a full continuous-parameter sweep with a closed-form derivative/critical-
point argument). This is worth keeping as the 7th attempt on this front,
but framed correctly: as a **direct construction/minimization**, with no
expectation, density, or "derandomization" language at all — drop outline
steps 1, 3 (as an integral), and 4 entirely; replace with "solve
$d\Phi/dx=0$ (or check the boundary) for the closed-form $\Phi(x)$ and
verify the minimizer clears $a_nT$ throughout case (b2)'s band."

**Verdict: RETHINK** the probabilistic-method framing as literally
outlined — it is a restatement of the already-dead mechanism 2 dressed in
different language, not a genuinely distinct 7th mechanism. The slug
itself is not cut from the population (its historical results — Theorems
A-E, telescoping-threshold-identity, etc. — remain certified and reusable,
and the 6 confirmed-dead mechanisms stay dead); only this round's proposed
new direction goes back to the outliner. Recommend the outliner rewrite
the skeleton as the direct-minimization version described above before
the next build.

---

## Diversity check

The three approaches target disjoint fronts of the whole theorem (Claim
B middle band at two different points — a boundary fix vs. the p3-cut
branch — and the general upper bound's case (b2)), so there is no
shared-gap risk this round. The rejected lp-duality-certificate mechanism
does not affect the other two fronts.

## Population / ranking

No new slugs to register this round (all three candidates are advances of
existing registered slugs). `update_ranking` called, comparing across the
sampled field and anchoring to last known outcomes: `rank-pigeonhole-
budget` and `greedy-halving-adversary` beat `lp-duality-certificate`
(mechanism-level flaw found this round) and beat `minimax-lp-response-
polytope` (confirmed dead-end last round); `rank-pigeonhole-budget` and
`greedy-halving-adversary` compared as a draw (both delivered a verified,
correctly-scoped fix this round); `lp-duality-certificate` still beats
`minimax-lp-response-polytope` (richer live history vs. a fully dead
mechanism). This also clears the `stale` flags left from round 19 on all
four touched slugs.

build set: rank-pigeonhole-budget, greedy-halving-adversary
