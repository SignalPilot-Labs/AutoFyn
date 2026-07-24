# Round 17 outline review — imo-2026-03

Reviewed: `results/imo-2026-03/current.md`, the two revised approach files
(`approaches/greedy-halving-adversary.md`, `approaches/lp-duality-certificate.md`,
specifically their embedded "Round 17 outline" sections), `/tmp/round-17/proof-outliner.md`,
and both round-17 explorer reports (`math-explorer-target-b.md`, `math-explorer-case-b2.md`).
Every load-bearing arithmetic/algebraic claim below was independently re-derived by hand
and cross-checked with fresh exact-`Fraction` Python scripts, not taken on faith from the
outline or the explorer.

## greedy-halving-adversary — verdict: CHANGES REQUESTED

**(1) The "peel p2 first is structurally dead by mass-count" claim is WRONG — do not let
the builder treat it as settled or certify it.**

The round-17 explorer's mass-count argument rests on the claim "$s=p_2-f(n)<p_2<f(n)=2p_2$"
— i.e. it asserts $f(n)=2p_2$. This is false. The certified `level-2-dominance-identity`
(Lemma 24) states $p_2-s=f(n)$ with $s\ge0$, which forces $f(n)\le p_2$, the *opposite*
direction from the explorer's claim. I recomputed $f(n)=1/(2^{n+1}-1)$ and $p_2=2^{n-1}f(n)$
exactly for $n=2,\dots,7$ (script below) and confirmed $f(n)<p_2$ always, with the gap
growing geometrically (e.g. $n=6$: $f(n)=1/127$, $p_2=32/127$ — $f(n)$ is over 30× smaller
than $p_2$, not double it). The explorer appears to have conflated the alternating-sum
target $f(n)=1/D_n$ with the game-value target $c(n)=p_1=2^n/D_n$ (true that $p_1=2p_2$,
Lemma 23 — but $f(n)\ne p_1$).

Consequence: both "impossibility" checks in the explorer's fold-1/fold-2 arguments are
invalid. Recomputing directly: fold 1's bound $\mathrm{Total}(R'')\le p_3+s$ is **not**
less than $f(n)$ — it's 2×–47× larger than $f(n)$ across $n=2,\dots,7$ (e.g. $n=3$:
$p_3+s=1/3 \gg f(3)=1/15$), so "$A(R'')\ge f(n)$ is provably impossible by total mass" is
false; there is ample mass headroom. Fold 2's boundary check ($s-p_3-f(n)$) is $\ge0$ for
every $n\ge3$ tested (exactly $0$ at $n=3$), meaning the needed inequality $A(R)\ge t^*+f(n)$
sits at or inside the mass budget, not outside it. **Neither fold is "provably impossible";
this negative finding is not established and must not be written up as a certified dead-end
lemma this round.** (Verification script: see below — reproduce with `python3` and exact
`Fraction`, ~15 lines, takes seconds.)

Practical effect on the outline: this does *not* invalidate the outline's actual **redirect
target** (sub-case (b) via route (i)) — that target stands on its own regardless of whether
peel-$p_2$-first is dead. But the outline's "Watch out for (1): do NOT revive peel-$p_2$-first
… proven structurally dead by mass-count" instruction is currently false-as-justified. Tell
the builder: (a) do not cite or certify the explorer's mass-count argument; (b) "peel $p_2$
first" remains formally open, not closed — it may still be worth a future round's attention,
though this round's budget should stay on sub-case (b) per the redirect, which is independently
motivated; (c) if the builder wants to write up a genuine mass-count observation, it must use
the correct values ($f(n)=p_2-s$, not $2p_2$) and re-derive from scratch.

**(2) Route (i)'s substitution algebra (steps 1–4) is correct — I independently re-derived it.**

Substituting Proposition 30's exact formula at $v=v_1$ and $v=v_2$ into Lemma 25
($A(F\cup G')=A(G')+A(F_1\cup G')-A(F_2\cup G')$), the $p_2$ and $A(R')$ terms cancel exactly
in the $F_1-F_2$ difference (both instances share the literal same reference $R'$, as required),
leaving exactly the outline's claimed closed form
$$A(F\cup G')=A(G')+(v_2-v_1)+2\big(A(R'_{>v_2})-A(R'_{>v_1})\big)+2\big(v_1\epsilon(v_1)-v_2\epsilon(v_2)\big).$$
I derived this independently by hand and it matches the outline's step-3 formula term for term.
Hypotheses compose correctly: Proposition 30 requires $v\in(0,p_2)$, and sub-case (b)'s own
defining condition ($v_1,v_2<p_2$) satisfies this for both substitutions, using the identical
reference $R'$ (Prop 30's $R'$ is defined purely from the tail refinement, independent of $v$).
So steps 1–4 are sound and well-posed.

**(3) Step 5's proposed "Two-Threshold Truncated Alternating Sum Floor" is not the "2-line"
lemma the outline implies — flag this explicitly for the builder.**

The certified single-threshold floor (`truncated-alternating-sum-floor`) gives, after
rearranging, an **upper** bound on $A(S_{>v})$ (not a lower bound) — I re-derived this from
the stated identity $A(S)-2A(S_{>v})+2v\epsilon(v)\ge v-T$. "Apply the floor lemma to both
$v_1$ and $v_2$ and combine" (the outline's step-5 sketch) therefore naturally supplies an
upper bound on $A(S_{>v_1})$ and needs a *separate* (not automatically supplied) handle on
$A(S_{>v_2})$ from below; the only elementary such handle is the trivial $A(S_{>v_2})\ge0$,
which does **not** produce the outline's guessed constant $-(v_1-v_2)/2$ — substituting the
trivial bound plus the certified upper bound gives an expression depending on $A(R')$ and
$\epsilon$, not a clean universal constant. I also found a cleaner exact identity worth
handing to the builder directly (saves rediscovery time): using the certified floor lemma's
own proof mechanism, $\Psi(v_1)-\Psi(v_2)=2\int_{v_2}^{v_1}u_{R'}(x)\,dx$ exactly (where
$\Psi(v):=A(R')-2A(R'_{>v})+2v\epsilon(v)$ is Theorem 31's own quantity) — so the band-integral
is bounded only trivially, $0\le\Psi(v_1)-\Psi(v_2)\le2(v_1-v_2)$, and plugging the *lower*
end ($\ge0$) into the full chain gives $A(F\cup G')\ge p_2-A(R')-(v_1-v_2)$, which needs
$A(R')+(v_1-v_2)\le s$ — **not generally true** (the trivial bound $A(R')\le s$ combined with
$v_1-v_2$ possibly comparable to $p_2\gg s$ can push this negative). This is exactly the same
"lower bound is insufficient, an upper bound is needed" trap the round-15 reviewer already
flagged for this exact Lemma-25 minus sign, now showing up one level deeper inside the new
lemma's own derivation. The outline's own hedge ("or the sharpest provable constant" / fall
back to route (ii)) is appropriate — just make sure the builder does not spend the round
assuming step 5 is routine; give it the $\Psi(v_1)-\Psi(v_2)=2\int_{v_2}^{v_1}u_{R'}$ identity
above as a starting point and expect to need either a genuinely joint (not two
separately-bounded) argument, or route (ii) from early in the round rather than as a
late fallback.

**Verification script** (reproduce independently if in doubt):
```python
from fractions import Fraction as F
for n in range(2,8):
    D = 2**(n+1)-1; fn = F(1,D)
    p = [F(2**(n+1-i))*fn for i in range(1,n+2)]
    p2,p3 = p[1],p[2]; s = sum(p[2:])
    assert p2-s==fn        # Lemma 24, certified — confirms f(n) < p2, not f(n)=2p2
    assert not (p3+s < fn) # fold-1 "impossibility" is false
```

## lp-duality-certificate — verdict: CHANGES REQUESTED

**(4) The convex-combination bounding device (min(A,B) ≤ λA+(1-λ)B) is algebraically valid
as stated, and legitimately useful as a *sufficient* condition — but step 5's proposed
mechanism for finding λ(p) ("equating the two strategies' worst-case values… linear algebra")
is, read literally, a tautology that adds zero proving power beyond the already-tried
min(Phi_BTk,Phi_CP) check. This must be clarified before the builder invests real time.**

The chain $\Phi_{\min}\le\min(\Phi_{BTk},\Phi_{CP})\le\lambda\Phi_{BTk}+(1-\lambda)\Phi_{CP}$
is valid for any fixed $\lambda\in[0,1]$, so if the RHS is provably $\le a_nT$ everywhere in
case (b2)'s box, that suffices — this is a legitimate device (I verified the logic; it is a
genuine, if unusual, relaxation, not vacuous per se). **But** if $\lambda(p)$ is defined, as
step 5 literally describes, by solving $\lambda\Phi_{BTk}(p)+(1-\lambda)\Phi_{CP}(p)=a_nT(p)$
for $\lambda$ at each marking $p$, this is a tautology: the resulting combination is
*identically* $a_nT(p)$ by construction, and $\lambda(p)$ lands in $[0,1]$ **if and only if**
$a_nT(p)$ already lies between $\Phi_{BTk}(p)$ and $\Phi_{CP}(p)$ — i.e. iff
$\min(\Phi_{BTk},\Phi_{CP})(p)\le a_nT(p)$ already holds by direct comparison, no $\lambda$
needed. Wherever both constructions exceed target simultaneously (both above $a_nT$), no
$\lambda\in[0,1]$ can rescue the point (a convex combination of two numbers both $\ge a_nT$ is
itself $\ge a_nT$) — so this exact mechanism cannot extend coverage beyond
$\min(\Phi_{BTk},\Phi_{CP})\le a_nT$, which is precisely what R16.3's grid check already
partially tested and found 2/214 gaps in. As literally written, step 5 is circular: it cannot
close anything the plain min-of-constructions check doesn't already close.

The outline's actual value lies in step 4's framing (prove the pointwise inequality directly,
possibly via a $\lambda(p)$ that is *not* defined by pointwise equating — e.g. a simple,
independently-motivated closed form, like a ratio of piece sizes, whose resulting combination
is then proven $\le a_nT$ as a genuine algebraic inequality, not by construction) — this is a
real, different, and more tractable target than case-splitting on which of $\Phi_{BTk},\Phi_{CP}$
is smaller. Tell the builder explicitly: do **not** define $\lambda(p)$ by solving the
equal-to-target equation (that's circular); pick $\lambda(p)$ independently (e.g. from the
structure of the two identities, not from the target value) and then prove the resulting bound
as a nontrivial inequality — or else state plainly that this reduces to "does one of the two
constructions already beat target" and stop calling it a new mechanism.

**Step 1 (cheap-kill numeric check) is a sound, appropriately-gated first move regardless** —
if a fixed simple rational weighting already covers the R16.3 uncovered points, that's useful
signal either way and should be run first, as the outline says.

## Diversity note

Both fronts remain a lower-bound push (`greedy-halving-adversary`, Claim (B)) and an
upper-bound push (`lp-duality-certificate`, case (b2)) — genuinely orthogonal halves of the
theorem, not two framings of the same wall; this is healthy diversity, not a shared-gap
plateau. No action needed on diversity this round.

## Ranking

Registered: no new slugs this round (both revised approaches keep their existing slugs,
already in the population). Ranked the full field via `update_ranking` (comparisons: the two
revised approaches roughly drawn against each other; both anchored below the still-highest
`rank-pigeonhole-budget` [Claim (A), fully closed, verified-milestone] and above
`rank-tie-vertex-reduction` [last a general negative result, no new closure since round 8]).
Updated Elo: `rank-pigeonhole-budget` 1749, `rank-tie-vertex-reduction` 1601,
`greedy-halving-adversary` 1596, `lp-duality-certificate` 1594. All `stale` flags cleared.

## Build instructions summary

- `greedy-halving-adversary`: proceed with route (i) (steps 1–4, verified sound); treat step
  5 as genuinely open (use the $\Psi(v_1)-\Psi(v_2)=2\int_{v_2}^{v_1}u_{R'}$ identity as a
  starting point, not a "2-line" finish) and keep route (ii) live in parallel, not as a late
  fallback. Do **not** write up or certify the "peel-$p_2$-first is mass-count-dead" claim —
  it is false as argued (see script above); either drop it or redo it correctly.
- `lp-duality-certificate`: run the cheap-kill numeric check first (step 1). If pursuing the
  weighted-combination idea further, do not define $\lambda(p)$ by pointwise-equating to the
  target (circular, see above) — either find an independently-motivated $\lambda(p)$ and prove
  the resulting bound as a genuine inequality, or honestly report that the combination device
  reduces to the already-tried min-of-constructions check and pivot to a different mechanism
  (e.g. a third construction family) for the residual points.

build set: greedy-halving-adversary, lp-duality-certificate
