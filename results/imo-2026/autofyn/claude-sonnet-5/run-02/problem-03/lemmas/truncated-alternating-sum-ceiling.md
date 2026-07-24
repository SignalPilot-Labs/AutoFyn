## Truncated Alternating Sum Ceiling (new, round 19, certified by reviewer)

**Statement.** For any finite multiset $S$ of nonnegative reals and any
$v\ge0$ (with $S_{>v}:=\{x\in S:x>v\}$, $A(\cdot)$ the sorted-descending
alternating-sum functional of `integral-alternating-sum-formula`),
$$A(S)-2A(S_{>v})\ \le\ v,$$
with equality attained, e.g., at $S=\{v\}$ (more generally, at any
$S=\{v\}\cup P$ with $P$ an exactly-paired multiset all of whose elements
are $<v$).

This is completely general: no ladder structure, no legality/refinement
assumption, and $v$ need not be $\le\mathrm{Total}(S)$. It is the natural
"ceiling" dual to the already-certified `truncated-alternating-sum-floor`
(same elementary decomposition, opposite pair of one-sided bounds).

**Proof.** Write $N_S(x):=\#\{a\in S:a>x\}$ and
$u_S(x):=\mathbb1[N_S(x)\text{ odd}]\in\{0,1\}$, so
$A(S)=\int_0^\infty u_S(x)\,dx$ (`integral-alternating-sum-formula`).

*Step 1 (truncation identity).* For $x\ge v$: an element of $S$ exceeds
$x$ iff it exceeds $v$ and exceeds $x$ (since $x\ge v$), so
$N_S(x)=N_{S_{>v}}(x)$, hence $u_S(x)=u_{S_{>v}}(x)$ for all $x\ge v$. For
$x\in[0,v)$: every element of $S_{>v}$ exceeds $v>x$, so all of them exceed
$x$; hence $N_{S_{>v}}(x)=|S_{>v}|$ constant, so $u_{S_{>v}}(x)\equiv
\epsilon(v):=\mathbb1[|S_{>v}|\text{ odd}]$ on $[0,v)$. Therefore
$$A(S_{>v})=\int_0^v u_{S_{>v}}(x)dx+\int_v^\infty u_{S_{>v}}(x)dx
= v\,\epsilon(v)+\int_v^\infty u_S(x)\,dx.\tag{1}$$

*Step 2 (assemble).* Using $A(S)=\int_0^v u_S+\int_v^\infty u_S$ and (1),
$$A(S)-2A(S_{>v})=\int_0^v u_S(x)\,dx-\int_v^\infty u_S(x)\,dx-2v\,
\epsilon(v).\tag{2}$$

*Step 3 (one-line bounds).* Since $u_S\in\{0,1\}$: $\int_0^vu_S\le v$,
$\int_v^\infty u_S\ge0$, and $\epsilon(v)\ge0$. Substituting into (2):
$$A(S)-2A(S_{>v})\ \le\ v-0-0\ =\ v.\qquad\blacksquare$$

**Equality case.** $S=\{v\}$: $A(S)=v$, $S_{>v}=\varnothing$ (as
$v\not>v$), $A(S_{>v})=0$, so $A(S)-2A(S_{>v})=v$. General equality holds
iff $u_S\equiv1$ on $[0,v)$, $u_S\equiv0$ on $[v,\infty)$, and
$\epsilon(v)=0$.

**Provenance and verification.** First proved in
`approaches/rank-pigeonhole-budget.md` §7.1 (round 19). Independently
re-derived and re-verified by the proof-reviewer from scratch: 200,000
random-rational trials (exact `Fraction` arithmetic, no structure imposed
on $S$ or $v$), zero violations, with the worst-case margin found to be
exactly $0$ (equality attained, matching the claimed equality case).

**Usage.** Directly targets the quantity `greedy-halving-adversary`'s
Theorem 34/35 work calls $\Delta(n,v):=A(R')-2A(R'_{>v})$: this lemma
alone gives $\Delta(n,v)\le v$ (the trivial, structure-free ceiling), which
is by itself too weak to close the middle band (see
`rank-pigeonhole-budget.md` §7.2 for why); the sharper ladder-specific
work in Theorem 35 is still required for the actual target
$\Delta(n,v)\le v-f(n)$.
