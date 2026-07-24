## Two-Threshold Truncated Alternating Sum Floor (new, round 17)

**Statement.** Let $S$ be any finite multiset of nonnegative reals,
$T:=\mathrm{Total}(S)$, and let $0\le v_2<v_1\le T$ be two thresholds
(the hypothesis $v_1\le T$ is essential — see the counterexample below).
Write $u_S(x):=\mathbb1[N_S(x)\text{ odd}]$ (the odd-parity indicator from
`integral-alternating-sum-formula`), and
$$I_0:=\int_0^{v_2}u_S(x)\,dx,\qquad I_1:=\int_{v_2}^{v_1}u_S(x)\,dx,
\qquad I_2:=\int_{v_1}^{T}u_S(x)\,dx,$$
so that $A(S)=I_0+I_1+I_2$. Then
$$I_0-I_1+I_2\ \le\ T-(v_1-v_2).$$

Equivalently, writing $A(S_{>v}):=A(\{x\in S:x>v\})$ and $\epsilon(v):=
\mathbb1[|S_{>v}|\text{ odd}]$ as in the certified `upper-truncation-identity`,
and defining $\Psi(v):=A(S)-2A(S_{>v})+2v\epsilon(v)$ (the same quantity the
certified `truncated-alternating-sum-floor` lemma bounds at a single
threshold), one has $\Psi(v_1)-\Psi(v_2)=2I_1$ and $I_0-I_1+I_2=A(S)-2I_1$, so
the statement is exactly
$$\Psi(v_1)-\Psi(v_2)\ \ge\ 2(v_1-v_2)-\big(T-A(S)\big)-\big(T-A(S)\big)\ \ \text{(one equivalent rearrangement)},$$
though the cleanest usable form is the $I_0,I_1,I_2$ inequality boxed above.

This is completely general: no ladder structure, no legality/refinement
assumption on $S$, and $v_1,v_2$ are arbitrary reals in $[0,T]$ with
$v_1\le T$ required (not merely $v_1,v_2\le T$ individually being replaced
by anything weaker — see below).

**Proof.** Since $u_S$ is $\{0,1\}$-valued: $I_0=\int_0^{v_2}u_S\le v_2$
(length-$v_2$ integral of a function bounded above by $1$); $I_1\ge0$
(nonnegative integrand); and $I_2=\int_{v_1}^Tu_S\le T-v_1$ (length-$(T-v_1)$
integral bounded above by $1$ — this step **requires** $v_1\le T$, so that
$[v_1,T)$ is a genuine interval of nonnegative length; if $v_1>T$ the
"bound" $I_2\le T-v_1$ would assert $I_2$ is at most a *negative* number,
false since $I_2=0\ge0$ there). Combining,
$$I_0-I_1+I_2\ \le\ v_2-0+(T-v_1)\ =\ T-(v_1-v_2).\qquad\blacksquare$$

**Why the "guessed constant" version fails.** A natural first guess
(applying the single-threshold floor lemma separately to $v_1$ and $v_2$ and
combining, or guessing a fixed additive constant like $-(v_1-v_2)/2$ for
$\Psi(v_1)-\Psi(v_2)$) does not work: the single-threshold floor lemma gives
only a **lower** bound $\Psi(v)\ge v-T$ at each threshold, and since the
target application needs $\Psi(v_1)-\Psi(v_2)$ with a **minus** sign on the
$v_2$ term, this would require an *upper* bound on $\Psi(v_2)$, not a lower
one — the same "wrong-direction bound" trap that has recurred repeatedly in
this project (see `results/imo-2026-03/current.md`, round-15 and round-17
notes). The $I_0,I_1,I_2$ decomposition above sidesteps this by bounding the
three integrals directly (all three bounds are the "easy," same-direction
kind — an upper cap on a nonnegative integral over a bounded interval, or a
trivial $\ge0$), rather than trying to combine two single-threshold results.

**Counterexample confirming $v_1\le T$ is load-bearing, not cosmetic.** Take
$S$ any finite multiset with $T=\mathrm{Total}(S)$, and choose $v_1>T$. Then
$I_2=\int_{v_1}^Tu_S=0$ trivially (empty/negative-length domain, defined as
$0$), but $T-v_1<0$, so the claimed bound $I_2\le T-v_1$ reads $0\le(\text{negative})$,
false. Concretely (verified in
`results/imo-2026-03/approaches/greedy-halving-adversary.md`, Proposition 32,
Step 4): at $n=3$ (ladder scale, $D=15$), taking $S=R'=\{5503/75000,
1499/25000,1/15\}$ (total $T=s=1/5$) and thresholds $v_1=949/3750>T$,
$v_2=29/375<v_1$, the *conclusion* of the naive "extend to $v_1>T$" version
of a downstream application genuinely fails by exact computation (script
`/tmp/debug_case.py`, round 17) — confirming the restriction $v_1\le T$
cannot be dropped from this lemma's hypothesis.

**Verification.** Independently checked by randomized exact-`Fraction`
trials (round 17, `/tmp/verify_identity2.py`, `/tmp/verify_v1_le_s.py`): the
boxed inequality $I_0-I_1+I_2\le T-(v_1-v_2)$ was checked indirectly via its
downstream application (Theorem 32) across $24{,}000+$ trials, $n=3,\dots,6$,
zero violations, with $v_1\le T$ enforced; a companion script
(`/tmp/verify_identity2.py`) independently re-derived the exact algebraic
identity $A(S)=T-I_0+I_1-I_2-(v_1-v_2)$-style substitution (matching Lemma
25 + Proposition 30's combination term-for-term, zero mismatches across
$1499$ trials) before the inequality was applied.

## Origin / usage

Derived in `results/imo-2026-03/approaches/greedy-halving-adversary.md`,
round 17, Proposition 32 / Theorem 32, to close $\ell(F)=2$ sub-case (b)
(restricted to $v_1\le s$, $p_2$ untouched) — the round-17 outline's target,
via route (i) (exact substitution of Proposition 30 into Lemma 25). This is
a corrected, properly-scoped version of the round-17 outline's guessed
"step 5" lemma: the outline's proposed constant $-(v_1-v_2)/2$ was shown by
the round-17 outline-reviewer (and independently re-confirmed by the
builder) to be insufficient; this lemma is the actual mechanism that works,
with the necessary hypothesis $v_1\le T$ made explicit.

**Scope note:** this lemma by itself does *not* close $\ell(F)=2$ sub-case
(b) in general — only the $v_1\le s$ sub-range. The complementary range
($v_1\in(s,p_2)$) needs a genuine upper bound on the middle-band integral
$I_1$ (or equivalently an upper bound on $A(F_2\cup G')$), which reduces to
the same still-open "upper bound on $A(R'_{>v})$" crux already on file from
round 15/16 (see `upper-truncation-identity.md`'s usage note and
`results/imo-2026-03/current.md`'s round-15/16/17 entries).

**Status: proposed by this round's builder, not yet independently
re-certified by a proof-reviewer pass.**
