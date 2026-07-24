## Upper-Truncation Identity (new, round 15)

**Statement.** Let $S$ be any finite multiset of nonnegative reals, let
$N_S(x):=\#\{e\in S: e>x\}$, $u_S(x):=\mathbb1[N_S(x)\text{ odd}]$ (the
odd-parity indicator of the certified `integral-alternating-sum-formula`),
and $A(S):=\int_0^\infty u_S(x)\,dx$. For any threshold $v\ge0$, write
$S_{>v}:=\{e\in S : e>v\}$ (a sub-multiset, keeping multiplicities). Then
$$\int_v^\infty u_S(x)\,dx \;=\; A(S_{>v})\;-\;v\cdot\epsilon(v),\qquad
\epsilon(v):=\mathbb1\big[\,|S_{>v}|\text{ is odd}\,\big].$$

Equivalently (subtracting from $A(S)=\int_0^v u_S+\int_v^\infty u_S$),
$$\int_0^v u_S(x)\,dx \;=\; A(S)-A(S_{>v})+v\cdot\epsilon(v).$$

This is completely general: no ladder structure, no legality/refinement
assumption on $S$, and $v$ is an arbitrary nonnegative real (not required
to be an actual element of $S$ or tied to any legal cut).

**Proof.** First, for $x\ge v$: every element $e\le v$ satisfies $e\le v\le
x$, hence does not contribute to $N_S(x)$; so $N_S(x)=N_{S_{>v}}(x)$ for
every $x\ge v$, giving $u_S(x)=u_{S_{>v}}(x)$ on $[v,\infty)$, hence
$$\int_v^\infty u_S(x)\,dx=\int_v^\infty u_{S_{>v}}(x)\,dx. \tag{1}$$
Second, on $[0,v)$: every element of $S_{>v}$ exceeds $v>x$, so
$N_{S_{>v}}(x)=|S_{>v}|$ identically (a constant) for every $x<v$; hence
$u_{S_{>v}}(x)\equiv\epsilon(v)$ on $[0,v)$, giving
$$\int_0^v u_{S_{>v}}(x)\,dx = v\cdot\epsilon(v). \tag{2}$$
Since $A(S_{>v})=\int_0^v u_{S_{>v}}+\int_v^\infty u_{S_{>v}}$, combining (1)
and (2):
$$A(S_{>v}) = v\cdot\epsilon(v)+\int_v^\infty u_S(x)\,dx,$$
which rearranges to the stated identity. $\blacksquare$

**Remark (why the naive parity-free guess is false).** A first-pass guess
that $\int_v^\infty u_S=A(S_{>v})$ exactly (dropping $\epsilon$) is false in
general — e.g. $S=\{5\}$, $v=2$: $S_{>v}=\{5\}$, $A(S_{>v})=5$, but
$\int_2^\infty u_S\,dx=\int_2^5 1\,dx=3=5-2\cdot1$, matching the corrected
formula with $\epsilon=1$ (odd cardinality), not the naive guess of $5$.
The correction term is load-bearing whenever $|S_{>v}|$ is odd.

**Verification.** Independently checked by 3000 random-`Fraction` trials
(random multisets of size 1–7, random threshold $v$), comparing the
directly-computed breakpoint integral $\int_v^\infty u_S$ against
$A(S_{>v})-v\epsilon(v)$: zero mismatches. Script:
`/tmp/round-15/check_upper_truncation.py`.

## Origin / usage

Derived in `results/imo-2026-03/approaches/greedy-halving-adversary.md`,
round 15, to extend Proposition 24 (the $v\ge s$ closure of the
$\ell(F)=1$, $p_2$-untouched sub-branch of restricted Claim (B)) to the
complementary $v<s$ range (Proposition 30). Reduces the previously
qualitative diagnosis ("only a partial integral is available, not the full
$A(R')$") to a precise, fully general algebraic correction, isolating the
open item exactly as "need an upper bound on $A(R'_{>v})$," up to the
explicit parity term above.

**Status: proposed by this round's builder, not yet independently
re-certified by a proof-reviewer pass.**
