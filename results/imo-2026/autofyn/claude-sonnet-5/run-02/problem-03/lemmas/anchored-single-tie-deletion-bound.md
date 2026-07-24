## Statement (PROPOSED — awaiting proof-reviewer certification)

Let $w>0$ and let $X$ be a finite multiset of positive reals with
$\max(X)<w$. Let $t\in X$ be a value occurring in $X$ with **odd**
multiplicity (in particular this covers the generic case where $t$ occurs
in $X$ exactly once). Then
$$A(\{w\}\cup X\cup\{t\})\ =\ w-A(X\setminus\{t\})\ \ge\ w-\mathrm{Total}(X)+t,$$
where $A(\cdot)$ is the alternating-sum-of-sorted-descending-order
functional (`integral-alternating-sum-formula`), $X\setminus\{t\}$ denotes
$X$ with exactly one copy of $t$ removed, and $\mathrm{Total}(X\setminus\{t\})
=\mathrm{Total}(X)-t$.

Fully general: no ladder structure or legality/refinement structure on $X$
is assumed — only the two hypotheses $\max(X)<w$ (the anchor $w$ strictly
dominates every element of $X$) and $t$ has odd multiplicity in $X$ (so
that inserting one more copy of $t$ makes it even and hence cancels in the
odd-run reduction).

## Proof

**Step 1 (exact identity via odd-run cancellation).** Write $\mu$ for the
(odd, by hypothesis) multiplicity of $t$ in $X$. In the multiset
$X\cup\{t\}$, $t$ has multiplicity $\mu+1$ (even). By the certified
`odd-run-reduction-lemma`, $A$ is unchanged by deleting any two adjacent
equal copies of a value; deleting the $\mu+1$ (an even number) copies of
$t$ from $X\cup\{t\}$ in pairs, two at a time, leaves the reduced multiset
$X\setminus\{t\}$ (i.e. $X$ with its own $\mu$ copies of $t$ *all* removed,
since $\mu$ is odd and each pairing removes two, one copy is left over
paired with the freshly-inserted copy — concretely: pair the newly inserted
copy with one existing copy of $t$, cancel that pair by
`odd-run-reduction-lemma`, and — since $\mu-1$ is even — the remaining
$\mu-1$ copies of $t$ already still in $X\setminus\{t\}$ cancel among
themselves in pairs exactly as they would inside $A(X)$ itself, contributing
the same net effect as removing all of $t$'s original copies). Net result:
$$A(X\cup\{t\})=A\big(X\setminus\{t\}\big)$$
(here $X\setminus\{t\}$ means one copy removed; the displayed equality
holds because $\mu$ is odd, so removing one copy of $t$ from $X$ leaves an
even remaining multiplicity $\mu-1$, and adding the fresh copy restores the
same odd-run-reduced representative that dropping all copies of $t$ from
$X$ would give — both descriptions denote the same value of $A$).

**Step 2 (peel the anchor).** By hypothesis $w>\max(X)\ge\max(X\setminus\{t\})$
and $w>\max(X\cup\{t\})$ (adding a copy of an already-present value $t\le\max(X)$
cannot raise the max), so the certified `sharp-dominant-removal-identity`
applies directly to $\{w\}\cup(X\cup\{t\})$:
$$A(\{w\}\cup X\cup\{t\})=w-A(X\cup\{t\})=w-A(X\setminus\{t\}),$$
using Step 1 for the last equality.

**Step 3 (trivial upper bound).** By the integral formula
$A(S)=\int_0^\infty\mathbb1[N_S(x)\text{ odd}]\,dx$ and
$\mathrm{Total}(S)=\int_0^\infty N_S(x)\,dx$ (`integral-alternating-sum-formula`,
layer-cake identity for a sum of nonnegative reals), $\mathbb1[N_S(x)\text{
odd}]\le N_S(x)$ pointwise, so $A(S)\le\mathrm{Total}(S)$ for any finite
multiset $S$ of nonnegative reals — this is the standard trivial bound
already noted as a corollary of `triangle-bound-for-a`'s proof. Applying it
to $S=X\setminus\{t\}$:
$$A(X\setminus\{t\})\le\mathrm{Total}(X\setminus\{t\})=\mathrm{Total}(X)-t.$$

Combining Steps 2–3:
$$A(\{w\}\cup X\cup\{t\})=w-A(X\setminus\{t\})\ \ge\ w-\mathrm{Total}(X)+t.\qquad\blacksquare$$

## Scope note — what this does NOT cover

This lemma requires $t$ to have **odd** multiplicity in $X$ before
insertion (in particular the generic single-occurrence case). If $t$ has
**even** multiplicity in $X$ (including $0$), inserting one more copy makes
it odd, and the resulting object $A(X\cup\{t\})$ is **not** given by a
simple deletion — it equals $A\big((X)'\cup\{t\}\big)$ where $(X)'$ is $X$'s
own odd-run reduction, a genuinely different (harder) computation. See the
"Round 26" write-up in `approaches/greedy-halving-adversary.md` for the
diagnosis that this even-multiplicity residual reduces to needing a
non-trivial *upper* bound on $A(X)$ itself (not just $\mathrm{Total}(X)$),
i.e. the project's general central obstruction — this lemma does **not**
close that residual, and no claim to the contrary is made here.

## Verification

Independently checked by exact-`Fraction` script
(`/tmp/round-26/verify_deletion_lemma.py`): for $n=5,\dots,9$, the unit
$n$-ladder's tail $\{p_5,\dots,p_{n+1}\}$, $14{,}990$ random legal
refinements $T''$ (using $\le n-4$ cuts) with $t=t^\ast$ a randomly chosen
element of $T''$ restricted to the odd-multiplicity case, comparing
$A(\{p_4\}\cup T''\cup\{t^\ast\})$ (direct sort-and-alternating-sum) against
the closed-form bound $f(n)+t^\ast$: **zero violations**, with the bound
observed tight (equality) in at least one trial, confirming it is not
loose by construction. A second script
(`/tmp/round-26/verify_even_mult.py`) confirms — separately, and not
claimed as proved — that the excluded even-multiplicity sub-case also
never violates $A(B)\ge f(n)$ in $71$ observed trials (rare, since exact
ties among independently-generated random fragments are measure-zero
except when explicitly engineered), consistent with (but not a substitute
for) the missing general closure of that residual.

## Origin / usage

Derived in `results/imo-2026-03/approaches/greedy-halving-adversary.md`,
round 26, to close (in the odd-multiplicity sub-case) the vertex family
"$b$ ties to a non-maximal element of $T''$" in Theorem 37's own
"$T'$-untouched" branch of Case (b)'s "$v\ge a$" target: applying with
$w=p_4$, $X=T''$ (a legal $\le(n-4)$-cut refinement of
$\{p_5,\dots,p_{n+1}\}$), using the ladder facts $\max(T'')\le p_5<p_4$
(splitting never raises the max) and $\mathrm{Total}(T'')=p_4-f(n)$ (ladder
telescoping sum), gives $A(B)\ge f(n)+t^\ast>f(n)$ unconditionally, for
every $n$ and every legal $T''$ — no induction hypothesis $(\star_{n-4})$
required.
