## Statement

Given any finite multiset $W$ of positive reals with $|W|=m$, define the
**Iterated Greedy-Peel Construction**: while $|W|\ge2$, let $a\ge b$ be the
two largest elements of $W$ (ties broken arbitrarily). If $a=b$: remove
both from $W$ (using $0$ further cuts). If $a>b$: cut $a$ into $(b,a-b)$
(a single legal cut on the existing fragment $a$), remove $a,b$ from $W$,
and insert $a-b$ into $W$ (using $1$ further cut). Stop when $|W|\le1$; let
$v_{\text{final}}$ be the surviving element if $|W|=1$, and set
$v_{\text{final}}:=0$ if $W$ becomes empty.

Then:
1. **(Legality.)** This construction always uses at most $m-1$ cuts total.
2. **(Exact value.)** The resulting real final multiset $M$ (the actual
   physical result of every cut performed) satisfies
   $A(M)=v_{\text{final}}$ exactly, hence $\Phi(M)=(\mathrm{Total}(M)+
   v_{\text{final}})/2$.

## Proof

See `results/imo-2026-03/approaches/lp-duality-certificate.md`, §Route B.3
(round 10).

**Legality.** Let $C_0=m,C_1,\dots,C_T\in\{0,1\}$ be the sequence of
$|W|$-values across steps. Each step reduces $|W|$ by exactly $1$ (an
"$a>b$" step, contributing $1$ to the cut count) or exactly $2$ (an
"$a=b$" step, contributing $0$). Let $s_1,s_2$ be the total number of each
type; cuts used $=s_1$, and $s_1+2s_2=m-C_T$. If $C_T=1$:
$s_1=m-1-2s_2\le m-1$. If $C_T=0$: the last step must be an "$a=b$" step
(an "$a>b$" step always leaves a nonzero remainder $a-b>0$ in $W$, so
$|W|$ can only reach $0$ via a tie-step from $|W|=2$); hence $s_2\ge1$, so
$s_1=m-2s_2\le m-2<m-1$. In both cases $s_1\le m-1$.

**Exact value.** By induction on the number of "$a>b$" steps. Each such
step cuts the current fragment $a$ (a member of the real, current
multiset) into $(b,a-b)$, where $b$ is another member of the real current
multiset. The real multiset immediately after this cut contains two copies
of the value $b$ (the pre-existing one and the new fragment) plus $a-b$
plus every other untouched fragment. By `pair-cancellation-identity`,
$A$(real multiset after this cut)$=A$(real multiset with both copies of
$b$ removed, and $a$ replaced by $a-b$) — exactly the bookkeeping of the
next working-set state. Each "$a=b$" step similarly removes an exact pair
already present, again by `pair-cancellation-identity`. Since
`pair-cancellation-identity` holds regardless of where a pair sits in
sorted order and regardless of how many other pairs have already been
removed, these reductions may be applied once per step, in the order the
steps occurred, telescoping to $A(M)=v_{\text{final}}$ (or $0$). Every pair
identified along the way is disjoint from every other, since each step
consumes the current top two distinct positions of $W$ and paired elements
are removed from $W$ immediately, never revisited.

## Certification note

Certified in the approach file this round (round 10). This is a genuine
new general reduction identity, fully proved, unconditional, marking-
agnostic (no ladder or ratio-2 assumption). It is verified exactly on both
on-file hard witnesses ($n=3$: $(3/8,1/4,1/4,1/8)$ and
$(2/5,3/10,1/5,1/10)$, both giving $\Phi=1/2$ via a $2$-cut route, matching
their previously known optima). **Important scope note**: this identity is
a correct, general computational tool for evaluating one specific
(greedy) Xiang Yu strategy exactly — it is **not** by itself a proof that
this strategy always achieves the target $c(n)\le a_n$; see the companion
dead-end record `greedy-top-two-matching-insufficiency.md` for a proven
counterexample (equal-pieces marking, $n=4$) showing the "always match top
two" selection rule fails in general. The identity itself remains valid
and reusable regardless.

**Certified by:** proof-reviewer, round 10 — independently re-verified with
a freshly-written exact-`Fraction` script (3000 random markings, $m=2,
\dots,7$), directly re-simulating the actual sequence of physical cuts
(not just the abstract working-set bookkeeping) and comparing $A(M)$ via
direct sort-and-alternating-sum against $v_{\text{final}}$: zero
mismatches, and the legality bound (cuts used $\le m-1$) held in every
trial. CERTIFIED.
