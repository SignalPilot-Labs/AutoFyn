# Round 26 proof-reviewer report — IMO-2026-03

Adversarial review of 3 built slugs. Each was read in full for its round-26
additions plus enough surrounding/prior context (definitions, cited lemmas,
lemma files) to independently re-derive the claims rather than trust the
builder's own scripts. Independent verification was carried out (partly via
dispatched read-only sub-investigations whose numeric/algebraic claims I
then spot-checked and, for the highest-stakes finding, re-derived myself by
hand from the source files) before reaching each verdict.

## 1. `lp-duality-certificate` — CHANGES REQUESTED

New §R26.1–R26.3 (lines ~6009–6240), claiming a complete, non-numeric proof
of $c(3)\le8/15$ for *every* legal Liu Bang marking at $n=3$ (not just the
ladder), by fixing round 25's citation bug.

**(a) Citation fix (R26.1) — CONFIRMED.** Case (a) is now correctly defined
as $p_2\ge4T/15$, closed via the Corollary to Theorem B ($m=4$,
$S'=\{p_1-p_2,p_3,p_4\}$). I re-derived the threshold algebra by hand:
Theorem B's Corollary needs $p_2\ge a_nT/2\wedge\Phi_{\min}(S')\le
a_{m-2}T'$; with $a_2=4/7,a_3=8/15$, the derived threshold
$(a_2-a_3)/(2a_2-1)\cdot T=4T/15$ matches $a_3T/2$ exactly. The hypothesis
is discharged by the certified `lemmas/n2-upper-bound-lp-argument.md`,
which bounds $\Phi_{\min}$ for *any* 3 positive values with no sortedness
assumption — $\Phi_{\min}$ is a multiset function, so $S'$ needs no
re-sorting. This is genuinely distinct from round 25's wrongly-cited
`generalized-peel-identity` (a bare bookkeeping identity, no threshold).
Real fix, not cosmetic.

**(b) Three-way $p_2$-partition (R26.2) — CONFIRMED.** $(0,T/15]\cup
(T/15,4T/15)\cup[4T/15,T/2]$ is exhaustive and non-overlapping; both
boundaries ($p_2=T/15$, $p_2=4T/15$) are assigned to exactly one closed
case each, whose cited lemma is non-strict there. $p_2\le T/2$ always
holds given sortedness ($2p_2\le p_1+p_2\le T$), so the partition's domain
claim is valid (never tight, but harmless).

**(c) The "bonus" domain-widening of `case-b2-n3-covering-closure.md`
(dropping $p_1<T/2$) — BROKEN.** This is the load-bearing claim for the
round's headline ("complete proof for *every* marking"), and it does not
hold. I read `lemmas/case-b2-n3-covering-closure.md` and the Triple-Pin
chamber's derivation in the approach file (§R24.3, lines ~5461–5480): the
chamber's closed form $\Phi_{\text{TriplePin}}=T-p_1$ is derived by first
showing $v_3:=p_1-p_2-p_3<p_4$ **using $p_1<T/2$ explicitly** ("the order
step used $p_1<T/2$ explicitly, so this exact form of the argument is
scoped to case (b2)" — the file's own words). Round 26's justification for
dropping the restriction only checks that the six *Farkas certificates'*
summed inequalities don't literally mention $p_1$ vs. $T/2$ — but it never
re-checks whether the underlying *chamber formulas* those certificates
combine remain valid outside $p_1<T/2$. They don't, for Triple-Pin.

Concrete counterexample (exact rationals, $T=1$):
$$p=(p_1,p_2,p_3,p_4)=(3/5,\ 9/40,\ 29/200,\ 3/100).$$
Sorted ($0.6\ge0.225\ge0.145\ge0.03$), sums to $1$, $p_1=3/5\ge T/2$,
$p_2=0.225\in(1/15,4/15)$ — squarely in the widened region. Recomputing
correctly:
- Bisect$\{1,4\}$: $\Phi=0.54$, $g_{14}=8/15-0.54<0$ — fails.
- Bisect$\{1,2\}$: $\Phi=0.5575$, $g_{12}<0$ — fails.
- DS-Above: feasible ($p_1>p_2+p_3$); $\Phi=p_1+p_4/2=0.615$, $g<0$ — fails.
- Triple-Pin: feasible ($p_1>p_2+p_3$); but $v_3=p_1-p_2-p_3=0.23>p_4=0.03$,
  so the order used in the stale formula is wrong. Recomputing $A(M')$
  correctly from $M'=\{v_3,p_4\}=\{0.23,0.03\}$ gives $A(M')=0.2$, so the
  true $\Phi_{\text{TriplePin}}=(T+A(M'))/2=0.6=p_1$ (matching
  $\max(p_1,T-p_1)$), and $g_{\text{TP}}=8/15-0.6=-1/15<0$ — fails (the
  stale formula $T-p_1=0.4$ would have wrongly shown success).
- R22.1.1: needs $p_2\le p_3+p_4=0.175$; but $p_2=0.225>0.175$ —
  infeasible.

All five chambers fail or are infeasible. This does not (necessarily)
mean $c(3)>8/15$ is violated at this point — some other strategy outside
the 5-chamber family might still achieve $\le8/15$ — but it does mean the
file's proof that "the 5-chamber family covers this widened region" is
false, so **R26.3's headline claim (general-marking upper bound for every
$n=3$ marking) is not established as written.**

**Verdict: CHANGES REQUESTED.** R26.1/R26.2 stand and are reusable
progress. The bonus widening must be reverted (restore
`case-b2-n3-covering-closure`'s $p_1<T/2$ hypothesis) and a genuinely new
mechanism found for the corner $p_1\ge T/2,\ T/15<p_2<4T/15$ before the
"complete, non-ladder-restricted $n=3$ upper bound" milestone can be
claimed. Recorded via `record_outcome` as `partial`.

## 2. `rank-pigeonhole-budget` — APPROVE

New §7.11–7.13 (lines ~1861–2350).

**§7.11 Index-Chain Identity $\mathrm{MinFloor}(\ell)\equiv(\star_{\ell-1})$
— CONFIRMED.** Independently re-derived both objects' exact statements
(not copied): $\mathrm{MinFloor}(\ell)$ is about a ratio-2 tail of length
$\ell$ with budget $\le\ell-1$; $(\star_k)$ is about a unit ratio-2 ladder
of length $k+1$ with budget $\le k$. Setting $k=\ell-1$ matches both
length ($\ell$) and budget ($\ell-1$) exactly. The rescaling bijection
(ratio-2 sequences of fixed length are unique up to scale) is genuine, and
I cross-checked the length convention against its actual prior use in §7.8
(the "unit $(n-3)$-ladder" of length $n-2$, i.e. $k+1$ for $k=n-3$) — no
off-by-one. Hand-checked concretely at $\ell=2,3$: e.g. $\ell=3$,
$\sigma=(4,2,1)$ vs. $\pi=(4,2,1)$ ($\lambda=1$) — literally the same
statement, both requiring $A\ge1$ with $\le2$ cuts.

**§7.12/§7.13 MaxCeil(3)/MaxCeil(4) closure ($n=6,7$) — CONFIRMED.**
MaxCeil(3) ($n=6$) is a straightforward 2-case split (budget $\le1$ cut),
reproduced by hand. MaxCeil(4) ($n=7$) uses a 5-shape cut-distribution
enumeration on tuples $(c_1,c_2,c_3,c_4)$, $c_1\ge1,\sum c_i\le2$. I
independently enumerated from this rule: $c_1=1$ leaves budget $\le1$ for
the rest → 4 tuples; $c_1=2$ leaves $0$ → 1 tuple. Exactly 5, matching the
file's list with no missing or duplicate shape. Recomputed each shape's
bound by hand from $\sigma=(8,4,2,1)$: all five give $A\le7$, with the
supremum genuinely attained in the boundary limit of shape $(1,1,0,0)$ —
this matches an independent cross-check against $\mathrm{MinFloor}(3)$'s
own minimizer. One minor cosmetic looseness: the $a=4$ triple-tie boundary
of shapes $(1,0,1,0)/(1,0,0,1)$ deserves a fuller write-up than the
file's terse "direct check as above," but the conclusion checks out
exactly ($5-2c$ and $3-2d$, both $\le7$) — not a correctness bug.

**Verdict: APPROVE.** Both new results are independently re-derivable,
exhaustive, with no index or case-count gap. This is a genuine, clean
milestone — $\mathrm{MaxCeil}$ is now closed unconditionally through
$\ell=4$ ($n\le7$), both branches, via a technique (full shape enumeration)
that does not rely on the previously-flagged-insufficient Triangle-Bound
shortcut. General $\ell\ge5$ ($n\ge8$) is honestly left open, correctly
diagnosed as blocked on $(\star_k)$, $k\ge3$. Recorded via `record_outcome`
as `verified-milestone`.

## 3. `greedy-halving-adversary` — CHANGES REQUESTED

New Theorem 40 (Anchored Single-Tie Deletion Bound), lines ~5681–5860 (plus
pointers at ~794–811 and a summary at ~6438–6454).

**Proof chain — CONFIRMED.** Theorem 40 claims: if the boundary element
ties to $t^\ast\in T''$ with odd multiplicity, $A(B)=f(n)+t^\ast>f(n)$
unconditionally for $n\ge5$, no induction. Traced the chain: Step 1
(`odd-run-reduction-lemma`, cancels the now-even-multiplicity pair) →
Step 2 (`sharp-dominant-removal-identity`, valid since $p_4>\max(X)$ and
$p_4>\max(X\cup\{t^\ast\})$) gives the exact identity
$A(B)=p_4-A(X\setminus\{t^\ast\})$ → Step 3 (trivial $A\le\mathrm{Total}$
bound plus the ladder's own geometric-sum identity
$\mathrm{Total}(T'')=p_4-f(n)$). None of these three steps hides an
induction on $n$ or a small-$n$-only base case; the mass identity and the
domination fact $\max(X)\le p_5=p_4/2$ are closed-form ladder-geometry
facts for every $n\ge5$.

**Domination hypothesis $w>\max(X)$ — CONFIRMED, genuinely automatic.**
This follows directly from the ladder's doubling identity $p_4=2p_5$
(splitting never raises a fragment above its parent, so
$\max(T'')\le p_5<p_4$) — not an extra unverified assumption. The file also
honestly and correctly explains (lines ~5802–5824) why this same mechanism
does *not* transfer to the sibling object $A(\{c_2\}\cup T''')$ ($c_2$ has
no analogous forced-doubling guarantee), and correctly leaves the
even-multiplicity sub-case open, diagnosing it as needing the project's
central still-missing upper bound (not hand-waved past).

**Overclaim hunt — one FOUND, not from this round's new text but left
uncorrected in the file.** The new Theorem 40 material itself, everywhere
it appears, is scrupulously scoped: e.g. "Do not conflate: this round's
closure applies only within Theorem 37's own branch; Case (b)'s '$v\ge a$'
branch as a whole remains open" (immediately preceding the Round 25 status
block). But directly below that correct statement, the **uncorrected**
round-24/25 status text still reads: "Combined with Theorem 37
(unconditional for $n\le6$), Case (b)'s whole '$v\ge a$' branch is now
fully, unconditionally closed at $n=6$ as well as $n=5$" (and the matching
$n=5$-only claim a few lines below it). These are false as stated even
after Theorem 40 — the even-multiplicity sub-case of Theorem 37's own gap
is still open at $n=5,6$ — and this is exactly the 3rd-round-running
overclaim pattern the task flagged. The round-26 outline itself explicitly
warned against repeating it, yet the stale lines were never struck or
corrected.

**Verdict: CHANGES REQUESTED.** Theorem 40 is sound and reusable — certify
it — but the stale round-24/25 "branch fully closed at $n=5/n=6$" lines
must be struck or corrected next round so the file stops contradicting its
own honest round-26 diagnosis. Recorded via `record_outcome` as `partial`.

## Overall

`current.md` updated with a Round 26 entry (Status remains `partial`).
Net effect this round: one genuine clean milestone
(`rank-pigeonhole-budget`'s MaxCeil(4)/$n=7$ full closure, both branches),
one real new lemma pair with a load-bearing bug found in its "bonus"
extension (`lp-duality-certificate`'s widened case (b2), false as claimed —
concrete counterexample on file), and one sound new theorem
(`greedy-halving-adversary`'s Theorem 40) shipped alongside stale,
uncorrected overclaim text elsewhere in the same file. No slug reaches
`solved`; the whole-problem Status stays `partial`.

slug: lp-duality-certificate verdict: CHANGES REQUESTED
slug: rank-pigeonhole-budget verdict: APPROVE
slug: greedy-halving-adversary verdict: CHANGES REQUESTED
