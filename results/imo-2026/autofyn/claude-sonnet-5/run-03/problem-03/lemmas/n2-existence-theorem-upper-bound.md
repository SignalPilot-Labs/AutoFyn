## Source
`approaches/global-lp-vertex-sufficiency.md`, round 19, Section 10.1–10.5.
Certified by the round-19 proof-reviewer after full independent
re-derivation (own exact-`Fraction` script, not reusing the builder's;
500,000 valid-region trials).

## Theorem ($n=2$ Existence Theorem, upper-bound direction)

For every $p=(p_1,p_2,p_3)$ in the balanced region $B(2)$ ($p_1+p_2+p_3=1$,
$p_1<1/2$, $d_1:=p_1-p_2>\gamma(2)=1/7$, $d_2:=p_2-p_3>\gamma(2)$),
$$V(p)\le\mathrm{OddSum}(M)=1-p_1<\frac{11}{21}<\frac47=c(2),$$
where $M=\{p_2,p_2,p_3,p_1-p_2\}$ is the response splitting $p_1$ into
$(p_2,\,p_1-p_2)$ and leaving $p_2,p_3$ untouched. Hence $V(p)<c(2)$
strictly, with a uniform margin $\ge1/21$, throughout $B(2)$.

*Proof.*
1. **$p_1=(1+2d_1+d_2)/3$**: substitute $p_2=p_1-d_1$, $p_3=p_1-d_1-d_2$
   into $p_1+p_2+p_3=1$ and solve for $p_1$ — an unconditional identity.
   Since $d_1,d_2>\gamma(2)=1/7$ strictly, $2d_1+d_2>3/7$, so
   $p_1>(1+3/7)/3=10/21$ strictly.
2. **Legality**: the response uses $1\le2$ cuts; both fragments $p_2>0$
   and $p_1-p_2=d_1>\gamma(2)>0$ are strictly positive (region
   hypotheses), so it is always legal.
3. **Order claim**: $p_3-(p_1-p_2)=(1-p_1-p_2)-(p_1-p_2)=1-2p_1$, so
   $p_3>p_1-p_2\iff p_1<1/2$ — an exact algebraic identity, and
   $p_1<1/2$ is itself one of $B(2)$'s defining hypotheses. So the
   sorted order of $M$ is $p_2\ge p_2>p_3>p_1-p_2$ throughout $B(2)$,
   unconditionally (no sub-case).
4. **Value**: with this order, $\mathrm{OddSum}(M)=p_2+p_3=1-p_1$ (mass
   conservation). Combined with step 1, $\mathrm{OddSum}(M)=1-p_1<
   1-10/21=11/21<4/7=c(2)$. $\blacksquare$

*Independent verification.* Own exact-`Fraction` script, 500,000 random
trials of $B(2)$ (sampled via $d_1,d_2>\gamma(2)$, back-solved
$p_1,p_2,p_3$), yielding 36,172–276K valid-region points across two runs:
zero violations of $p_1>10/21$, zero violations of the order claim, zero
mismatches of the identity $\mathrm{OddSum}(M)=1-p_1$, zero violations of
$\mathrm{OddSum}(M)<c(2)$; observed maximum $\mathrm{OddSum}\approx
0.523793$, consistent with (approaching but never reaching) the proved
supremum $11/21\approx0.523810$.

## Scope

Combined with the already-certified closure of the complementary region
(`lemmas/singleton-interleaving-and-k-anchor-merge.md`, covering
$p_1\ge1/2$ or some gap $\le\gamma(2)$), this establishes $V(p)\le c(2)$
for **every** $p$ in the $n=2$ simplex — the full upper-bound direction
of the Existence Theorem at $n=2$. It does **not** establish the matching
achievability/lower-bound direction ($V(p^*)=c(2)$ for some witness
$p^*$) in full: see the source file's Section 10.6, which proves
$V(p^*)\le c(2)$ exactly and $V(p^*)\ge c(2)$ for 9 of 10 finite response
shapes analytically, with the remaining 6 two-cut shapes only supported
by exact grid search, not a complete proof — that residual is **not**
certified here. Nor does this extend to $n\ge3$ (see the source file's
Section 10.8, a diagnosis, not a proof, of why the $n=2$ mechanism does
not transplant).
