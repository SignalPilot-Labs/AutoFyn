## Status
partial

## Approaches tried

- **Round 7 (this round, first build of this copied slug).** Dispatch: pursue
  orthogonallens's Finding 1 — decompose the sibling `ptolemy-trig-identity`'s
  open odd-parity claim into two independent "linear-form-at-both-roots"
  sub-lemmas (Lemma A: `F(U_2,V)<4` for both roots `V_1,V_2` of `q_2`; Lemma B:
  the mirror statement), reusing the resultant-of-quadratic-vs-linear-form
  template already certified in `lemmas/g2b-true-supplementary-parity.md`,
  as a **genuinely independent mechanism** from the sibling's IVT/single-
  radical route. **Result: real, fully rigorous new algebraic content — a
  new exact identity linking Lemma A directly to the master quantity `Ψ` —
  but this identity, honestly followed to its conclusion, shows the natural
  resultant/discriminant route to Lemma A is *not* strictly easier than the
  original `Ψ>0` claim: it reduces to a sign question provably equivalent
  (via an explicit, sign-known prefactor) to `Ψ>0` itself.** This is a
  precise, valuable negative result — narrower and more informative than
  "not attempted" — and it is reported honestly below, not papered over.
  Status remains `partial`; the open gap is unchanged in substance from the
  sibling's (the master parity/positivity claim), but the population now
  knows one natural decomposition route does not cheapen it.

## Current best

### Setup (identical to `ptolemy-trig-identity`, imported verbatim)

All of `ptolemy-trig-identity.md`'s Lemmas 1–4, the reduction to the
Ptolemy-equality target, Steps 0–3 of that file's Round 4–6 development, and
the two certified lemmas
`lemmas/ptolemy-resultant-elimination-to-sextic.md`,
`lemmas/ptolemy-sextic-parity-reduction.md` are imported unchanged. In
particular:

- $\tau=\tan\theta$, $U=\cot\alpha$ solves $q_1(U):=\tilde P_1U^2+\tilde
  Q_1U+\tilde R_1=0$ with
  $$\tilde P_1=\sin A\,\tau(\tau\cos C-\sin C),\quad
  \tilde Q_1=\sin A\sin C(\tau^2+1)+2\tau\sin B,\quad
  \tilde R_1=-2\tau^2\sin C\cos A-\tau\sin A\sin C+\sin A\cos C,$$
  and $V=\cot\alpha'$ solves $q_2(V):=\tilde P_2V^2+\tilde Q_2V+\tilde
  R_2=0$ with the same formulas, $B\leftrightarrow C$ swapped.
- $F(U,V):=\sin A\,UV-\cos A(U+V)-\sin A$; the target is
  $F(U_1,V_1)>4$ for the genuine roots $U_1$ (larger root of $q_1$, since
  $\tilde P_1<0$ on the domain — certified) and $V_1$ (larger root of $q_2$,
  $\tilde P_2<0$).
- **Certified sign facts** (`ptolemy-trig-identity.md` Round 6 Step 2):
  $\tau\cos C-\sin C<0$ and $\sin B-\tau\cos B>0$ throughout the open domain
  $D=\{0<\theta<\min(B,C)\}$; consequently $\tilde P_1,\tilde P_2<0$ on $D$.
- **Certified multiplicative resultant identity** (Round 6 Step 1):
  writing $m(U):=\sin A\,U-\cos A$, $n(U):=-\cos A\,U-\sin A-4$ (so
  $F(U,V)-4=m(U)V+n(U)$, affine in $V$), and
  $$\Phi(U):=\tilde P_2\,n(U)^2-\tilde Q_2\,n(U)m(U)+\tilde R_2\,m(U)^2$$
  (a quadratic in $U$), then $\Phi(U)=\tilde P_2\,L(U,V_1)\,L(U,V_2)$ where
  $L(U,V):=F(U,V)-4$, and
  $$\mathrm{Res}_U(q_1,\Phi)=\tilde P_1^2\tilde P_2^2\!\!\prod_{i,j\in\{1,2\}}\!\!\bigl(F(U_i,V_j)-4\bigr).$$
- **Certified factorization of the same resultant** (Round 5/6, corrected
  constant): $\mathrm{Res}_U(q_1,\Phi)=\sin^2A\,(\tau\cos C-\sin
  C)(\sin B-\tau\cos B)\,\Psi(\tau,A,C)$, and (Round 6 Step 3, proved):
  $$\Psi>0 \iff F_{11}F_{12}F_{21}F_{22}<0 \iff \text{an odd number of }F_{ij}:=F(U_i,V_j)\text{ exceed }4,$$
  writing $F_{ij}:=F(U_i,V_j)-4$ for brevity below (so the boxed claim reads
  $\Psi>0\iff\prod F_{ij}<0$).

### The target of this approach: Lemma A and Lemma B

**Lemma A.** For every $(\theta,A,B,C)\in D$: $F(U_2,V_1)<4$ **and**
$F(U_2,V_2)<4$ (i.e. $F_{21}<0$ and $F_{22}<0$), where $U_2$ is the
*spurious* (smaller) root of $q_1$.

**Lemma B** (mirror, $B\leftrightarrow C$ / $U\leftrightarrow V$
symmetry). For every $(\theta,A,B,C)\in D$: $F(U_1,V_2)<4$ **and**
$F(U_2,V_2)<4$ (i.e. $F_{12}<0$ and $F_{22}<0$), where $V_2$ is the
spurious root of $q_2$.

If both hold, the only surviving candidate for $F_{ij}>4$ is $(i,j)=(1,1)$,
and (given the already-certified parity dichotomy — an odd number exceed 4)
exactly one of the four exceeds, forcing $F_{11}>4$ — closing the whole
approach. This combination step is pure logic once Lemma A, B are proved;
it is not the difficulty. **The difficulty is proving Lemma A (and by
symmetry B) themselves.**

### New result this round: an exact identity reducing Lemma A to $\Psi$ itself

Write $\Phi(U)$'s value at the two roots of $q_1$ as
$$X_1:=(2\tilde P_1)^2\,\Phi(U_1), \qquad X_2:=(2\tilde P_1)^2\,\Phi(U_2).$$

**Step 1 (proved).** $X_1,X_2$ have the exact form $\alpha\mp\beta\sqrt{D_1}$
for explicit polynomials $\alpha,\beta$ in $(\tau,A,B,C)$ (independent of
the sign choice of the root), where $D_1:=\tilde Q_1^2-4\tilde P_1\tilde
R_1$ is the discriminant of $q_1$.

*Proof.* $U_1=\dfrac{-\tilde Q_1-\sqrt{D_1}}{2\tilde P_1}$ (genuine, larger
root, since $\tilde P_1<0$) and $U_2=\dfrac{-\tilde Q_1+\sqrt{D_1}}{2\tilde
P_1}$ (spurious). Since $\Phi$ is a quadratic polynomial in $U$, substituting
$U=\dfrac{-\tilde Q_1\pm s}{2\tilde P_1}$ (formal symbol $s$) and clearing
the denominator $(2\tilde P_1)^2$ gives
$(2\tilde P_1)^2\Phi\bigl(\tfrac{-\tilde Q_1\pm s}{2\tilde P_1}\bigr) =
c_2s^2+c_1(\pm s)+c_0$ for explicit polynomials $c_2,c_1,c_0$ in
$(\tau,A,B,C)$ (obtained by direct symbolic expansion — computer-algebra
verified, own `sympy` session, `/tmp/setup3.py`; $c_2$ equals $\Phi$'s own
leading coefficient in $U$). Substituting $s^2=D_1$ gives $\alpha:=c_2D_1+c_0$
and $\beta:=c_1$, so $X_1=\alpha-\beta\sqrt{D_1}$, $X_2=\alpha+\beta\sqrt{D_1}$
(sign convention matching $U_1\leftrightarrow-\sqrt{D_1}$,
$U_2\leftrightarrow+\sqrt{D_1}$ above). $\blacksquare$ (Independently
numerically re-verified this round on 3000 random domain samples: $X_1,X_2$
computed directly via $\Phi(U_1),\Phi(U_2)$ match $\alpha\mp\beta\sqrt{D_1}$
computed from the explicit $\alpha,\beta$ formulas to machine precision.)

**Step 2 (proved, the new identity).**
$$\alpha^2-\beta^2D_1 \;=\; X_1X_2 \;=\; 16\,\tilde P_1^2\sin^2A\,(\tau\cos
C-\sin C)(\sin B-\tau\cos B)\,\Psi(\tau,A,C).$$

*Proof.* $X_1X_2=(\alpha-\beta\sqrt{D_1})(\alpha+\beta\sqrt{D_1})=\alpha^2-\beta^2D_1$
by difference of squares — this holds identically as polynomials once
$s^2$ is substituted by $D_1$ (elementary algebra, no further computation
needed). Also, directly from the definitions,
$$X_1X_2=(2\tilde P_1)^4\Phi(U_1)\Phi(U_2).$$
By the certified Proposition ($\Phi(U)=\tilde P_2L(U,V_1)L(U,V_2)$, applied
at $U=U_1$ and $U=U_2$ separately), $\Phi(U_1)\Phi(U_2)=\tilde P_2^2\,
L(U_1,V_1)L(U_1,V_2)L(U_2,V_1)L(U_2,V_2)=\tilde P_2^2\,F_{11}F_{12}F_{21}F_{22}$.
Hence
$$X_1X_2=16\tilde P_1^4\tilde P_2^2\,F_{11}F_{12}F_{21}F_{22}
=16\tilde P_1^2\cdot\bigl(\tilde P_1^2\tilde P_2^2\!\!\prod_{i,j}F_{ij}\bigr)
=16\tilde P_1^2\cdot\mathrm{Res}_U(q_1,\Phi)$$
(using the certified multiplicative resultant identity for the bracketed
factor), and substituting the certified factorization of
$\mathrm{Res}_U(q_1,\Phi)$ gives exactly the displayed formula. $\blacksquare$
(Independently re-verified numerically this round, 5 random domain samples,
`/tmp/check_identity.py`: $X_1X_2$ computed directly from $\Phi(U_1),
\Phi(U_2)$ matches $16\tilde P_1^4\tilde P_2^2F_{11}F_{12}F_{21}F_{22}$ to
machine precision — ratio $1.000000$ in every sample — and also matches
$\Phi(U_2)/\tilde P_2=F_{21}F_{22}$ exactly, confirming the resultant
Proposition's evaluation-at-a-root consequence directly, not just the
polynomial identity in the abstract.)

**Consequence (honest, negative, but precise).** Since $\sin^2A>0$ and (by
the already-certified sign lemma) $(\tau\cos C-\sin C)<0$, $(\sin B-\tau\cos
B)>0$ throughout $D$, the coefficient $16\tilde P_1^2\sin^2A(\tau\cos
C-\sin C)(\sin B-\tau\cos B)$ is **strictly negative** everywhere on $D$
(a product of a nonzero square $\tilde P_1^2>0$, $\sin^2A>0$, and one
negative factor $(\tau\cos C-\sin C)(\sin B-\tau\cos B)<0$). Hence
$$\alpha^2-\beta^2D_1 <0 \iff \Psi(\tau,A,C)>0.$$
That is: **the statement "$X_1,X_2$ have the same sign" (equivalently
$\alpha^2<\beta^2D_1$, i.e. the radical term $\beta\sqrt{D_1}$ dominates
$\alpha$ in $X_2=\alpha+\beta\sqrt{D_1}$) is *logically equivalent*, given
only already-certified sign facts, to the master claim $\Psi>0$ itself** —
which is exactly the still-open gap for the whole population's Ptolemy
route. Recall also $X_2/(2\tilde P_1)^2=\Phi(U_2)=\tilde P_2F_{21}F_{22}$,
so "$X_2$ has a definite value" is the same data as "$F_{21}F_{22}$ has a
definite sign" (since $\tilde P_2<0$ is already known): **the "same sign"
half of Lemma A is not a strictly smaller sub-problem than $\Psi>0$ — via
this natural resultant/discriminant route, it is provably the *same*
sub-problem**, up to the explicit, fully-determined sign prefactor derived
above.

This is a genuine (if negative) new finding, not a restatement of what was
already known: it **rigorously explains**, via an exact identity (not
numerics), why orthogonallens's optimistic framing ("a much smaller ask,"
"the resultant sign is forced by cancellation exactly as in
`g2b-true-supplementary-parity.md`") does not transfer here as directly as
hoped. The key structural difference from `g2b-true-supplementary-parity.md`
is: in that lemma, the analogous discriminant-product quantity
($\mathrm{Res}_{s_2}(G_{2b},D_KD_N)$) was shown to equal a manifestly
non-negative expression (a known-sign prefactor times a **perfect square**),
so its sign was pinned unconditionally with no further input. Here, by
contrast, the same computation produces a known-sign prefactor times
$\Psi(\tau,A,C)$ itself — not (as far as this derivation shows) a perfect
square or otherwise independently sign-pinnable quantity — so the chain
closes back on the original open problem instead of resolving it externally.

### What would still be needed to close Lemma A (honestly unresolved)

Two directions remain open, neither completed this round:

1. **A genuinely different route to $\mathrm{sign}(X_2)$ not going through
   the $\alpha,\beta,D_1$ discriminant decomposition** — e.g. bounding
   $F(U_2,V)$ directly using $U_2$'s own defining relation $\tilde
   P_1U_2^2+\tilde Q_1U_2+\tilde R_1=0$ (eliminating $U_2^2$ in favor of
   $U_2$ inside $F$, then bounding the resulting expression using known
   bounds on $U_2$ itself, e.g. via the already-certified fact that $U_2$
   is a genuine real cotangent value with a known interval of validity) —
   flagged as the most promising untried lever, per the sibling file's own
   Step 4(a) discussion, but not attempted this round for lack of time.
2. **Pinning $\mathrm{sign}(\beta)$ and $\mathrm{sign}(\alpha)$ separately**:
   numerically (3000 domain samples, normal sampling across the whole
   domain, `/tmp/numcheck2.py`), neither $\alpha:=c_2D_1+c_0$ (this round's
   "$k_0$" scaled) nor $\beta=c_1$ (this round's "$k_1$") has a fixed sign
   across $D$ (both take both positive and negative values in the sample),
   so the easy sub-case ("$\alpha,\beta$ same sign $\Rightarrow$ sum trivially
   signed") does not apply uniformly; a full case split on
   $\mathrm{sign}(\alpha),\mathrm{sign}(\beta)$ combined with the (circular,
   as shown above) $\alpha^2$ vs. $\beta^2D_1$ comparison does not, by
   itself, produce new information beyond $\Psi>0$.

**Numerically** (3000 fresh domain samples this round, `/tmp/numcheck.py`,
independent of all prior population numerics): Lemma A holds with zero
exceptions ($F_{21},F_{22}<0$ always), consistent with the certified parity
dichotomy and with Round 4/6's independent large-scale sweeps — but, per the
above, this numeric confirmation is not closer to a proof than the master
claim's own numerics were, given the demonstrated equivalence.

### Lemma B

By the $B\leftrightarrow C$ symmetry already used throughout this population
(swap $b\leftrightarrow c$, $B\leftrightarrow C$, $\theta\leftrightarrow$ the
mirrored angle — the same $\sigma$-symmetry certified elsewhere in
`current.md`'s history, here applied at the level of $q_1\leftrightarrow
q_2$, $U\leftrightarrow V$, which the defining formulas for $\tilde
P_1,\tilde Q_1,\tilde R_1$ vs. $\tilde P_2,\tilde Q_2,\tilde R_2$ are
manifestly symmetric under), the identical derivation with the roles of $U$
and $V$ exchanged gives the mirror identity
$$\alpha_2^2-\beta_2^2D_2 = 16\tilde P_2^2\sin^2A(\tau\cos B-\sin
B)(\sin C-\tau\cos C)\,\Psi'(\tau,A,B)$$
for the corresponding quantities on the $V$-side, where $\Psi'$ is the
$B\leftrightarrow C$ image of $\Psi$ — reducing Lemma B to the same
equivalence with $\Psi'>0$ in place of $\Psi>0$. Since $\Psi$ and $\Psi'$
are images of each other under the same symmetry that exchanges (III) and
(IV) throughout this population (not independently re-derived as a separate
polynomial here, but following by the identical computation with $B,C$
swapped — the formulas for $\tilde P_2,\tilde Q_2,\tilde R_2$ are already
defined as exactly this swap of $\tilde P_1,\tilde Q_1,\tilde R_1$), Lemma B
is equivalent, by the identical argument, to $\Psi'>0$, which is the
$B\leftrightarrow C$-mirrored form of the same still-open master claim.

### Honest assessment

This round's work is **real, fully proved new mathematics** (Steps 1–2
above: a new, exact, independently-verified algebraic identity, not
previously in the population, connecting $\Phi$'s values at $q_1$'s two
roots to $\Psi$ via a perfect-square-free discriminant computation) — but
its **conclusion is negative**: the specific decomposition route proposed
by orthogonallens's Finding 1, when followed rigorously through the natural
resultant/discriminant machinery (the exact template that worked for
`g2b-true-supplementary-parity.md`), does **not** yield a sub-problem
strictly easier than the master claim $\Psi>0$ (equivalently, the four-branch
odd-parity claim) — it yields a sub-problem **provably equivalent** to it,
via the identity in Step 2. This differs from the sibling `g2b`-type lemma
precisely because there the analogous resultant produced a manifest
non-negative expression (prefactor times a perfect square), giving an
unconditional sign; here it produces prefactor times $\Psi$ itself, with no
squared structure to fall back on.

**No overclaiming**: Status remains `partial`. The single remaining gap for
this approach is identical in substance to the sibling `ptolemy-trig-identity`'s
gap (the master claim $\Psi(\tau,A,C)>0$, equivalently the four-branch
odd-parity claim), now additionally known — via this round's new identity —
to NOT be reducible via the natural Lemma-A/B discriminant-product
decomposition to something strictly smaller. The most promising untried
lever, per the discussion above, is a direct bound on $F(U_2,V)$ using
$U_2$'s defining quadratic relation (not the discriminant/resultant route),
not attempted this round.

## Promotable lemmas

- **New identity: $\Phi$'s value-product at $q_1$'s two roots equals a
  known-sign prefactor times $\Psi$** (Step 1–2 above): for the certified
  quadratic $q_1(U)=\tilde P_1U^2+\tilde Q_1U+\tilde R_1$ with discriminant
  $D_1$ and roots $U_{1,2}=(-\tilde Q_1\mp\sqrt{D_1})/(2\tilde P_1)$, and
  $\Phi(U):=\tilde P_2n(U)^2-\tilde Q_2n(U)m(U)+\tilde R_2m(U)^2$ (as
  defined in `ptolemy-resultant-elimination-to-sextic.md`), writing
  $\Phi(U)=c_2U^2+\ldots$ (its own quadratic expansion) and
  $\alpha:=c_2D_1+c_0$, $\beta:=c_1$ (the coefficients obtained by
  substituting $U_{1,2}$ formally and clearing denominators — explicit but
  lengthy polynomials in $\tau,A,B,C$, given in `/tmp/setup3.py`/
  `/tmp/setup4.py`), the identity
  $$\alpha^2-\beta^2D_1 = 16\tilde P_1^2\sin^2A\,(\tau\cos C-\sin C)(\sin
  B-\tau\cos B)\,\Psi(\tau,A,C)$$
  holds exactly (proved via resultant multiplicativity + the certified
  factorization of $\mathrm{Res}_U(q_1,\Phi)$; independently numerically
  verified to machine precision on 5 samples). This is a genuinely reusable
  structural fact: it shows that for a "two-quadratics-plus-bilinear-target"
  system of this shape, the discriminant of the "value at one root of the
  first quadratic" quantity is always proportional (with an explicit,
  computable prefactor) to the resultant that governs the master parity/
  positivity claim — a fact worth checking first, before attempting a
  similar discriminant-product decomposition elsewhere in this population
  (e.g. on the coordinate-route's own remaining $G_{2b}$-adjacent gaps), to
  avoid the same circularity found here.
