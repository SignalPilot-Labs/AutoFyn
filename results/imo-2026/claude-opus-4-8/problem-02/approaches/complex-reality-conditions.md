## Status
solved

<!-- Round-2 v2: the SOLE remaining gap (removal of the detA=0 locus) is now CLOSED
unconditionally in §6.2 by an exact polynomial ideal-membership certificate on the *physical*
(real) variety — with NO reference to detA, no continuity, no connectedness. Over the real slice
(conjugates forced, WLOG B=1 by similarity) one has the exact identity
  W·Im(TN) = f1·Im(E1)+f2·Im(E2)+f3·Im(E3),   W = |B-K|²·|C-L|²·Im(K̄L)·Im(B̄C),
certified by Gröbner/Buchberger reduction (an exact, terminating decision procedure). Since every
factor of W is nonzero on an admissible configuration (ND, ND, NL, NC) and Im(E_i)=0 by §3, we get
Im(TN)=0, i.e. TN=0, i.e. OM=ON, for EVERY admissible configuration. §4–§5 (Cramer route) are kept
as the motivating derivation; §6.2 supersedes the old detA-dependent §6 conclusion. -->

## Approach: Complex numbers with A at origin (reality conditions)

**Top-level target:** OM = ON, where O = circumcenter of AKL.

**Spine:** Complex numbers in geometry (knowledge_base.md, *Geometry §Coordinates / complex / barycentric*). Put A = 0; the three angle conditions become three *reality* (∈ ℝ) conditions on cross-ratio-type expressions, and OM = ON becomes one polynomial identity that is forced by an explicit conjugate-elimination. This is the mechanical-but-complete route, and it now **closes**.

## Approaches tried
- Round 2 v2, unconditional removal of the `detA=0` locus (§6.2) — **WORKED; closes the proof**.
  Replaced the flawed continuity paragraph with an exact polynomial ideal-membership certificate on the
  *physical* (real) variety. Key insight: each `E_i` and `TN` have the form `z-\bar z`, hence are purely
  imaginary, so the reality conditions are the three real equations `\mathrm{Im}(E_i)=0` and the target is
  `\mathrm{Im}(TN)=0`. Over the real slice (conjugates forced), WLOG `B=1` by similarity/homogeneity, one has
  the exact identity `W\cdot\mathrm{Im}(TN)=\sum f_i\,\mathrm{Im}(E_i)` with `W=|B-K|^2|C-L|^2\,\mathrm{Im}(\bar KL)\,\mathrm{Im}(\bar BC)`
  — none of whose factors is `\det\mathbf A`, and all nonzero on admissible configs (ND, ND, NL, NC).
  Verified by exact Gröbner/Buchberger reduction to `0` at power `N=1` (`certificate.py`). No `\det\mathbf A`,
  no continuity, no connectedness. NOTE: over the complex ring with *independent* conjugates the same
  membership FAILS (spurious component with `TN\neq0`) — so forcing the reality slice is essential and is
  what makes the certificate go through.
- Round 2, rigorous derivation of the reality conditions (§3) — **WORKED**. Replaced the round-1
  "asserted + numerically confirmed" §3 with a genuine signed-area / directed-angle derivation:
  (i) a reality-hinge lemma (Lemma 2) that lifts an unsigned-angle equality to an *exact* directed-angle
  equality once both directed angles are pinned into `(0,π)` — killing the supplementary branch because
  the difference of two numbers in `(0,π)` lies in `(-π,π)` and equals `0`, not `π`; (ii) the
  side-of-line dictionary (SIDE) and sign rule (SGN); (iii) the interior facts (K1),(L1),(L2) each derived
  as a one-line consequence of "interior of the named triangle" via signed areas; (iv) for each `C_i`,
  an exact argument identity `\arg C_i=\theta_1-\theta_2` plus positivity of both directed angles, the two
  subtle cases (`\beta_1` from "K inside ∠LBA", `\gamma_1` from "L inside ∠ACK") handled by convex-sector
  betweenness. Midpoint factors `2l-c=2(L-N)`, `2k-b=2(K-M)` written out. All sign facts and arg-identities
  confirmed numerically (`check_s3`) as sanity checks, not as proof. Closes the only remaining gap; the
  approach is now complete.
- Round 1, complex reality-condition elimination — **WORKED** (algebraic core). Circumcenter sign corrected to denominator `k l̄ − k̄ l`. The naive "solve (C2),(C3) linearly for the conjugates" is impossible (they are bilinear); instead the three cleared reality equations are jointly **affine-linear in the three monomials `(k̄ l̄, k̄, l̄)`**, so a single 3×3 Cramer solve produces `k̄, l̄` rationally. Substituting into the (corrected) target polynomial `TN` and into the consistency relation `k̄·l̄ = (k̄)(l̄)` produced two polynomials sharing a common degree-10 factor `G`; the target is `−qN·G` and the consistency numerator is `(b−k)(c−l)·G`, so `G = 0` on the configuration kills the target. All identities verified symbolically (`repro.py`) and numerically (`verify_config.py` config).

## Current best
**Complete proof below (Status: solved).** Both former gaps are closed:
1. The synthetic derivation of the three reality conditions `C_1,C_2,C_3\in\mathbb R` (§3) — signed-area /
   directed-angle inequalities (reality-hinge Lemma 2, (SIDE)/(SGN), interior facts (K1),(L1),(L2),
   convex-sector betweenness). Certified rigorous by the round-2 review.
2. The `\det\mathbf A=0` removal (§6.2) — an **exact polynomial ideal-membership certificate on the
   physical real variety**: `W\cdot\mathrm{Im}(TN)=\sum f_i\,\mathrm{Im}(E_i)`, `W=|B-K|^2|C-L|^2\,\mathrm{Im}(\bar KL)\,\mathrm{Im}(\bar BC)`,
   proven by exact Gröbner reduction (power `N=1`, `certificate.py`). This is unconditional and supersedes
   the flawed continuity argument; `\det\mathbf A` is not used.

The whole proof now reads end-to-end with no gaps.

## Full proof

Throughout we use directed angles and complex coordinates (knowledge_base.md, *Geometry*: "Coordinates / complex / barycentric", "Directed Angles (mod 180°)").

### 0. Setup and notation

Place the plane as ℂ with **A = 0**. Write the affixes of B, C, K, L as `b, c, k, l ∈ ℂ`, and write `b̄, c̄, k̄, l̄` for their complex conjugates. Since M, N are the midpoints of AB, AC and A = 0,
$$M = \tfrac{b}{2}, \qquad N = \tfrac{c}{2}.$$
Because ABC is a genuine triangle, `b ≠ 0`, `c ≠ 0`, and A, B, C are not collinear, which in complex terms means `b/c ∉ ℝ`, equivalently
$$b\bar c - \bar b c = -2i\,\mathrm{Im}(\bar b c) \neq 0. \tag{NC}$$
Also `K` lies inside triangle `BMC` and `L` inside triangle `BNC`; in particular `K ≠ B` and `L ≠ C`, i.e.
$$k - b \neq 0, \qquad l - c \neq 0. \tag{ND}$$
Finally A, K, L are three distinct non-collinear points (they lie on a circle with a well-defined center O), so
$$D := k\bar l - \bar k l \;=\; -2i\,\mathrm{Im}(\bar k l)\ \neq\ 0. \tag{NL}$$

### 1. The circumcenter of {A, K, L}

**Lemma 1 (circumcenter formula).** For three points `0, k, l ∈ ℂ` that are not collinear, the circumcenter of the triangle they form is
$$O \;=\; \frac{k\,|l|^2 - l\,|k|^2}{\,k\bar l - \bar k l\,} \;=\; \frac{kl(\bar l - \bar k)}{\,k\bar l - \bar k l\,}. \tag{1}$$

*Proof.* O is the unique point equidistant from 0, k, l. Writing `|O|² = |O−k|²` gives `O\bar k + \bar O k = |k|²`, and `|O|² = |O−l|²` gives `O\bar l + \bar O l = |l|²`. This is a linear system in `O, \bar O`; its determinant is `\bar k l - k \bar l = -D ≠ 0` by (NL). Solving,
$$O = \frac{|k|^2 \bar l - |l|^2 \bar k}{\bar k l - k\bar l}\cdot(\text{after conjugating/Cramer}) = \frac{k|l|^2 - l|k|^2}{k\bar l - \bar k l},$$
where the last equality is Cramer's rule applied to the two equations (solving for `O`, not `\bar O`). Finally `k|l|^2 - l|k|^2 = k(l\bar l) - l(k\bar k) = kl(\bar l - \bar k)`, giving the second form. ∎

(Numerically confirmed: for the audited scalene configuration `O` from (1) equals the true circumcenter, and the *opposite* denominator sign gives its negative — this fixes the sign flagged in the outline review.)

### 2. Reducing OM = ON to a polynomial identity

`OM = ON ⟺ |O − M|² = |O − N|² ⟺ |O − b/2|² = |O − c/2|²`. Expanding `|O−z|² = |O|² − (O\bar z + \bar O z) + |z|²` and cancelling `|O|²`,
$$OM=ON \iff O\bar b + \bar O b - \tfrac{|b|^2}{2}\cdot 2 \;=\; O\bar c + \bar O c - \tfrac{|c|^2}{2}\cdot 2$$
(using `\bar{(b/2)} = \bar b/2`, `|b/2|² = |b|²/4`, and multiplying through by 2). Rearranging,
$$OM=ON \iff \underbrace{2\big[O(\bar c - \bar b) + \bar O(c-b)\big] - (c\bar c - b\bar b)}_{=:T} = 0. \tag{2}$$
`T` is real (it equals `4\,\mathrm{Re}[O(\bar c-\bar b)] - (|c|^2-|b|^2)`). Substitute (1). Since `\bar O` is the conjugate of (1),
$$O = \frac{kl(\bar l-\bar k)}{D}, \qquad \bar O = \frac{\bar k\bar l (l-k)}{\bar D} = \frac{\bar k\bar l(k-l)}{D}, \tag{3}$$
because `\bar D = \bar k l - k\bar l = -D`. Both have denominator `D`. Multiplying (2) by `D` and using (3),
$$T\cdot D \;=\; \underbrace{2kl(\bar l-\bar k)(\bar c-\bar b) + 2\bar k\bar l(k-l)(c-b) - (c\bar c - b\bar b)\,D}_{=:\;TN}. \tag{4}$$
Since `D ≠ 0` by (NL), **`OM = ON ⟺ TN = 0`.** Here `TN` is a polynomial in `b,c,k,l,\bar b,\bar c,\bar k,\bar l`. Our task is to show `TN = 0` under the three angle conditions. (`conj(TN) = T\cdot\bar D = -TN`, consistent with `TN` being `i·` a real quantity.)

### 3. The three angle conditions as reality conditions

This section is the load-bearing translation from the synthetic hypotheses to the three
algebraic reality conditions `C_1,C_2,C_3\in\mathbb R`. Every inequality below is a genuine
signed-area / directed-angle statement derived from the interior hypotheses; numerical checks
(§Verification artifacts, `check_s3` output) are *confirmations only*, never the proof of a step.

#### 3.0 Conventions and orientation reduction

For an ordered triple of points `P,Q,R\in\mathbb C` define the **signed area**
$$[P,Q,R] \;:=\; \tfrac12\,\mathrm{Im}\!\big(\overline{(Q-P)}\,(R-P)\big).$$
This is the standard oriented area: `[P,Q,R]>0 ⟺ P,Q,R` are in counter-clockwise (CCW) order,
`<0 ⟺` clockwise, `=0 ⟺` collinear (knowledge_base.md, *Geometry: Coordinates / complex /
barycentric*). Indeed for `P=0,Q=1,R=i` one gets `[0,1,i]=\tfrac12\mathrm{Im}(i)=\tfrac12>0`, and
`0,1,i` is CCW. The functional `[P,Q,R]` is invariant under cyclic permutation of its arguments
and changes sign under a transposition; it is affine in each argument.

**Orientation reduction (WLOG CCW).** All hypotheses of the problem are unsigned angle equalities
(`∠KBA=∠ACL`, etc.) and interior/betweenness conditions, and the conclusion `OM=ON` is an equality
of distances; all of these are invariant under the reflection `z\mapsto\bar z` (an orientation-reversing
isometry fixing the real axis), which sends any configuration to a congruent one satisfying the same
hypotheses. A reflection reverses the sign of every `[\cdot,\cdot,\cdot]`, hence turns a clockwise-labelled
triangle `ABC` into a CCW one. We may therefore **assume throughout that `A,B,C` is CCW**, i.e.
$$[A,B,C]=\tfrac12\,\mathrm{Im}(\bar b c)>0 \iff \mathrm{Im}(\bar b c)>0. \tag{CCW}$$

**Side-of-a-line dictionary.** For a directed line through `A=0` and a second point `w`, a point `z`
satisfies `[A,w,z]=\tfrac12\mathrm{Im}(\bar w z)`, so
$$z\text{ lies strictly on the same side of line }Aw\text{ as }z' \iff \mathrm{Im}(\bar w z)\text{ and }\mathrm{Im}(\bar w z')\text{ have the same sign.}$$
Applying this to the two cevian-base lines `AB` (`w=b`) and `AC` (`w=c`) and evaluating the reference
vertices: `\mathrm{Im}(\bar b c)>0` by (CCW), and `\mathrm{Im}(\bar c b)=-\mathrm{Im}(\bar b c)<0`
(because `\bar c b=\overline{\bar b c}`). Hence:
- **`z` on the `C`-side of line `AB`** `⟺ \mathrm{Im}(\bar b z)>0`;
- **`z` on the `B`-side of line `AC`** `⟺ \mathrm{Im}(\bar c z)<0`. \hfill(SIDE)

#### 3.1 Directed angles and the reality mechanism

For distinct `P,U,V` write the **directed angle** from ray `PU` to ray `PV` as
$$\angle(PU\!\to\!PV) \;:=\; \arg\frac{V-P}{U-P}\ \in(-\pi,\pi]\quad(\text{principal value}).$$
The unsigned geometric angle is `∠UPV=\big|\angle(PU\!\to\!PV)\big|\in[0,\pi]`; in particular
$$\angle(PU\!\to\!PV)\in(0,\pi)\ \Longrightarrow\ ∠UPV=\angle(PU\!\to\!PV). \tag{U}$$
Also, since `\arg\frac{V-P}{U-P}\in(0,\pi)\iff\mathrm{Im}\frac{V-P}{U-P}>0\iff
\mathrm{Im}\big((V-P)\overline{(U-P)}\big)>0\iff[P,U,V]>0`, we have the **sign rule**
$$\angle(PU\!\to\!PV)\in(0,\pi)\iff[P,U,V]>0. \tag{SGN}$$

**Lemma 2 (the reality hinge).** *Let `\theta_1,\theta_2\in(0,\pi)` be two directed angles with*
$$\theta_1=\arg z_1,\quad \theta_2=\arg z_2\qquad(z_1,z_2\in\mathbb C^\times,\ \arg=\text{principal}),$$
*and suppose the corresponding unsigned angles are equal. Then `\arg(z_1/z_2)=\theta_1-\theta_2`
exactly, and if the unsigned angles are equal then `\theta_1=\theta_2`, whence `z_1/z_2>0`; in
particular `z_1/z_2\in\mathbb R`.*

*Proof.* Because `\theta_1,\theta_2\in(0,\pi)`, by (U) each equals its unsigned angle, so the
hypothesis "unsigned angles equal" gives `\theta_1=\theta_2` as **real numbers** (not merely mod `\pi`).
For the argument identity: `\arg(z_1/z_2)\equiv\arg z_1-\arg z_2=\theta_1-\theta_2\pmod{2\pi}`. Now
`\theta_1,\theta_2\in(0,\pi)` force `\theta_1-\theta_2\in(-\pi,\pi)`, and the principal value
`\arg(z_1/z_2)\in(-\pi,\pi]`; two numbers in `(-\pi,\pi]` that are congruent mod `2\pi` are equal, so
`\arg(z_1/z_2)=\theta_1-\theta_2`. When `\theta_1=\theta_2` this is `0`, i.e. `z_1/z_2` is a positive
real. `\square`

This is the exact place where the supplementary branch is killed: an unsigned equality only gives
`\theta_1\equiv\pm\theta_2\pmod\pi` in general, but **once both directed angles are pinned into `(0,\pi)`
the difference lies in `(-\pi,\pi)` and equals `0`, not `\pi`.** The whole task of §3.2–§3.5 is to prove,
for each `C_i`, that the two directed angles it is built from both lie in `(0,\pi)`, using (SGN),
(SIDE) and the interior hypotheses.

#### 3.2 Signed-area facts from the interior hypotheses

We first extract the sign facts we need. Recall `M=b/2,\ N=c/2`, and note `A,M,B` are collinear
(so line `BM=`line `AB`) and `A,N,C` are collinear (so line `NC=`line `AC`).

**(K1) `K` inside `\triangle BMC` `\Rightarrow \mathrm{Im}(\bar b k)>0` (`K` on the `C`-side of `AB`).**
The edge `BM` of `\triangle BMC` lies on line `AB`; a strictly interior point of the triangle lies on the
same side of line `AB` as the opposite vertex `C`. By (SIDE), `C`-side of `AB` means `\mathrm{Im}(\bar b k)>0`.

**(L1) `L` inside `\triangle BNC` `\Rightarrow \mathrm{Im}(\bar c l)<0` (`L` on the `B`-side of `AC`).**
The edge `NC` lies on line `AC`; a strictly interior point lies on the same side of `AC` as the opposite
vertex `B`. By (SIDE), `B`-side of `AC` means `\mathrm{Im}(\bar c l)<0`.

**(L2) `L` inside `\triangle BNC` `\Rightarrow \mathrm{Im}(\bar b l)>0` (`L` on the `C`-side of `AB`).**
The vertices of `\triangle BNC` are `B` (on line `AB`), `N=c/2` and `C=c`. Now
`\mathrm{Im}(\bar b\, N)=\tfrac12\mathrm{Im}(\bar b c)>0` and `\mathrm{Im}(\bar b\, C)=\mathrm{Im}(\bar b c)>0`
by (CCW), so both `N` and `C` are strictly on the `C`-side of `AB` while `B` is on the line. A triangle
with one vertex on a line and the other two strictly on one side has its entire open interior strictly on
that side; hence `\mathrm{Im}(\bar b l)>0`.

(These are exactly the strict inequalities the outline flagged; each is a one-line consequence of the
interior hypothesis via (SIDE), not a numerical assertion.)

#### 3.3 Condition `C_1` from `∠KBA=∠ACL`

Set `C_1:=\dfrac{bc}{(k-b)(l-c)}`. Introduce the two directed angles
$$\theta_1:=\angle(BK\!\to\!BA)=\arg\frac{A-B}{K-B}=\arg\frac{-b}{\,k-b\,},\qquad
\theta_2:=\angle(CA\!\to\!CL)=\arg\frac{L-C}{A-C}=\arg\frac{\,l-c\,}{-c}.$$
Their unsigned values are `∠KBA` and `∠ACL`. Compute the quotient of the two ratios:
$$\frac{-b/(k-b)}{(l-c)/(-c)}=\frac{(-b)(-c)}{(k-b)(l-c)}=\frac{bc}{(k-b)(l-c)}=C_1,$$
so by Lemma 2 (applied with `z_1=\frac{-b}{k-b},\ z_2=\frac{l-c}{-c}`) `\arg C_1=\theta_1-\theta_2`
**provided** `\theta_1,\theta_2\in(0,\pi)`. We verify this:
- `\theta_1\in(0,\pi)`: by (SGN), `\theta_1\in(0,\pi)\iff[B,K,A]>0`. Now
`[B,K,A]=\tfrac12\mathrm{Im}\big(\overline{(K-B)}(A-B)\big)=\tfrac12\mathrm{Im}\big((\bar k-\bar b)(-b)\big)
=\tfrac12\mathrm{Im}(-\bar k b)=\tfrac12\mathrm{Im}(\bar b k)`, using `\mathrm{Im}(-\bar k b)=
-\mathrm{Im}(\overline{\bar b k})=\mathrm{Im}(\bar b k)` and `\bar b b=|b|^2\in\mathbb R`. By **(K1)**
`\mathrm{Im}(\bar b k)>0`, so `[B,K,A]>0` and `\theta_1\in(0,\pi)`.
- `\theta_2\in(0,\pi)`: by (SGN), `\theta_2\in(0,\pi)\iff[C,A,L]>0`. Now
`[C,A,L]=\tfrac12\mathrm{Im}\big(\overline{(A-C)}(L-C)\big)=\tfrac12\mathrm{Im}\big((-\bar c)(l-c)\big)
=\tfrac12\mathrm{Im}(-\bar c l)=-\tfrac12\mathrm{Im}(\bar c l)`. By **(L1)** `\mathrm{Im}(\bar c l)<0`,
so `[C,A,L]>0` and `\theta_2\in(0,\pi)`.

Both directed angles lie in `(0,\pi)` and their unsigned values `∠KBA=∠ACL` are equal, so Lemma 2
gives `\theta_1=\theta_2`, hence `\arg C_1=0`:
$$\boxed{\;C_1=\dfrac{bc}{(k-b)(l-c)}\in\mathbb R_{>0}.\;}$$

#### 3.4 Condition `C_2` from `∠LBK=∠LNC`

Set `C_2:=\dfrac{(k-b)(2l-c)}{c\,(l-b)}`. Introduce
$$\beta_1:=\angle(BL\!\to\!BK)=\arg\frac{K-B}{L-B}=\arg\frac{k-b}{\,l-b\,},\qquad
\beta_2:=\angle(NL\!\to\!NC)=\arg\frac{C-N}{L-N}.$$
Since `N=c/2`, we have `C-N=c/2` and, crucially, `L-N=l-\tfrac c2=\tfrac{2l-c}{2}` (the **midpoint
artifact**), so
$$\beta_2=\arg\frac{c/2}{(2l-c)/2}=\arg\frac{c}{\,2l-c\,}.$$
Their unsigned values are `∠LBK` and `∠LNC`. The quotient of ratios is
$$\frac{(k-b)/(l-b)}{c/(2l-c)}=\frac{(k-b)(2l-c)}{(l-b)\,c}=C_2,$$
so by Lemma 2, `\arg C_2=\beta_1-\beta_2` provided `\beta_1,\beta_2\in(0,\pi)`. We verify:
- `\beta_2\in(0,\pi)`: by (SGN) with the ratio `\frac{C-N}{L-N}`, `\beta_2\in(0,\pi)\iff[N,L,C]>0`.
Directly, `\beta_2\in(0,\pi)\iff\mathrm{Im}\frac{c}{2l-c}>0\iff\mathrm{Im}\big(c\,\overline{(2l-c)}\big)>0
\iff\mathrm{Im}\big(2c\bar l-|c|^2\big)>0\iff\mathrm{Im}(c\bar l)>0\iff\mathrm{Im}(\bar c l)<0`
(using `c\bar l=\overline{\bar c l}`). By **(L1)** `\mathrm{Im}(\bar c l)<0`, so `\beta_2\in(0,\pi)`.
- `\beta_1\in(0,\pi)`: this is the subtle one — it uses the hypothesis "`K` lies inside the angle
`∠LBA`." First, by **(L2)** `\mathrm{Im}(\bar b l)>0`, i.e. `L` is on the `C`-side of line `AB`; hence
`[B,L,A]=\tfrac12\mathrm{Im}\big(\overline{(L-B)}(A-B)\big)=\tfrac12\mathrm{Im}\big((\bar l-\bar b)(-b)\big)
=\tfrac12\mathrm{Im}(-\bar l b)=\tfrac12\mathrm{Im}(\bar b l)>0`. By (SGN) this means
`\varphi:=\angle(BL\!\to\!BA)\in(0,\pi)`, and by (U) `\varphi=∠LBA\in(0,\pi)` (note `∠LBA>0` since `L`
is off line `AB`). Now "`K` inside angle `∠LBA`" means ray `BK` lies strictly inside the **convex**
angular sector of measure `∠LBA<\pi` bounded by rays `BL` and `BA`; since `BA` is reached from `BL` by
the positive rotation `\varphi\in(0,\pi)`, that sector is exactly the set of rays at directed angle from `BL`
in `(0,\varphi)`. Therefore `\beta_1=\angle(BL\!\to\!BK)\in(0,\varphi)\subset(0,\pi)`.

Both directed angles lie in `(0,\pi)` and their unsigned values `∠LBK=∠LNC` are equal, so Lemma 2
gives `\beta_1=\beta_2` and `\arg C_2=0`:
$$\boxed{\;C_2=\dfrac{(k-b)(2l-c)}{c\,(l-b)}\in\mathbb R_{>0}.\;}$$

#### 3.5 Condition `C_3` from `∠LCK=∠BMK`

Set `C_3:=\dfrac{b\,(k-c)}{(l-c)(2k-b)}`. Introduce
$$\gamma_1:=\angle(CL\!\to\!CK)=\arg\frac{K-C}{L-C}=\arg\frac{k-c}{\,l-c\,},\qquad
\gamma_2:=\angle(MB\!\to\!MK)=\arg\frac{K-M}{B-M}.$$
Since `M=b/2`, `B-M=b/2` and `K-M=k-\tfrac b2=\tfrac{2k-b}{2}` (the **midpoint artifact**), so
$$\gamma_2=\arg\frac{(2k-b)/2}{b/2}=\arg\frac{2k-b}{\,b\,}.$$
Their unsigned values are `∠LCK` and `∠BMK`. The quotient of ratios is
$$\frac{(k-c)/(l-c)}{(2k-b)/b}=\frac{b\,(k-c)}{(l-c)(2k-b)}=C_3,$$
so by Lemma 2, `\arg C_3=\gamma_1-\gamma_2` provided `\gamma_1,\gamma_2\in(0,\pi)`. We verify:
- `\gamma_2\in(0,\pi)`: `\gamma_2\in(0,\pi)\iff\mathrm{Im}\frac{2k-b}{b}>0\iff
\mathrm{Im}\big((2k-b)\bar b\big)>0\iff\mathrm{Im}\big(2k\bar b-|b|^2\big)>0\iff\mathrm{Im}(k\bar b)>0
\iff\mathrm{Im}(\bar b k)>0` (using `k\bar b=\overline{\bar b k}`... indeed
`\mathrm{Im}(k\bar b)=\mathrm{Im}(\bar b k)` since `k\bar b=\bar b k`). By **(K1)** `\mathrm{Im}(\bar b k)>0`,
so `\gamma_2\in(0,\pi)`.
- `\gamma_1\in(0,\pi)`: this uses "`L` lies inside the angle `∠ACK`." From §3.3 we already have
`\theta_2=\angle(CA\!\to\!CL)\in(0,\pi)`, i.e. ray `CL` is reached from ray `CA` by a positive rotation
`\theta_2\in(0,\pi)`. "`L` inside angle `∠ACK`" means ray `CL` lies strictly inside the convex sector of
measure `∠ACK\le\pi` bounded by rays `CA` and `CK`. Since the interior ray `CL` sits at positive directed
angle `\theta_2>0` from `CA`, the sector must extend CCW from `CA` past `CL` to `CK`; hence
`\angle(CA\!\to\!CK)\in(\theta_2,\pi]` (it cannot be a clockwise/negative angle, for then the convex
sector between `CA` and `CK` would lie on the clockwise side and could not contain the CCW ray `CL`).
Consequently
$$\gamma_1=\angle(CL\!\to\!CK)=\angle(CA\!\to\!CK)-\angle(CA\!\to\!CL)=\angle(CA\!\to\!CK)-\theta_2
\in(0,\ \pi-\theta_2)\subset(0,\pi),$$
where the subtraction is exact because `\angle(CA\!\to\!CK)\in(\theta_2,\pi]` and `\theta_2\in(0,\pi)`
put both directed angles, and their difference, in `(-\pi,\pi]`.

Both directed angles lie in `(0,\pi)` and their unsigned values `∠LCK=∠BMK` are equal, so Lemma 2
gives `\gamma_1=\gamma_2` and `\arg C_3=0`:
$$\boxed{\;C_3=\dfrac{b\,(k-c)}{(l-c)(2k-b)}\in\mathbb R_{>0}.\;}$$

*(Numerical confirmation on a valid configuration, `check_s3`: `\mathrm{Im}(\bar b c)=3.0>0`,
`\mathrm{Im}(\bar b k)=0.199>0`, `\mathrm{Im}(\bar c l)=-0.556<0`, `\mathrm{Im}(\bar b l)=1.80>0`;
`\theta_1=\theta_2=20.0^\circ`, `\beta_1=\beta_2=37.62^\circ`, `\gamma_1=\gamma_2=15.77^\circ`, all in
`(0,\pi)`; `\arg C_1,\arg C_2,\arg C_3\approx0` and `C_1,C_2,C_3>0`. Confirmation only — the proof is the
signed-area derivation above.)*

#### 3.6 Reality `\Rightarrow` the polynomial system

Each `C_i\in\mathbb R\iff C_i=\bar C_i`. Clearing denominators (all of
`k-b,\ l-c,\ c,\ l-b,\ 2k-b` are nonzero on a valid configuration: `k\ne b,\ l\ne c` by (ND), `c\ne0`,
and `l\ne b,\ 2k\ne b` hold since otherwise a `\beta`- or `\gamma`-ratio would be `0/\cdot` or `\cdot/0`,
contradicting `\beta_1,\gamma_2\in(0,\pi)`), each condition becomes a polynomial equation:
$$
\begin{aligned}
E_1 &:= bc(\bar k-\bar b)(\bar l-\bar c) - \bar b\bar c(k-b)(l-c) = 0,\\
E_2 &:= (k-b)(2l-c)\,\bar c(\bar l-\bar b) - (\bar k-\bar b)(2\bar l-\bar c)\,c(l-b) = 0,\\
E_3 &:= b(k-c)(\bar l-\bar c)(2\bar k-\bar b) - \bar b(\bar k-\bar c)(l-c)(2k-b) = 0.
\end{aligned}\tag{5}
$$
(Each `E_i` is the numerator of `C_i - \bar C_i`, so `E_i = 0 \iff C_i \in ℝ`; note `E_i` involves the "denominator" factors `(k-b),(l-c),c,(l-b),(2k-b)` which are all nonzero for a valid interior configuration.)

### 4. Conjugate elimination

Regard `b,c,\bar b,\bar c` as fixed and `k,l` as fixed, and treat the conjugates `\bar k, \bar l` as the unknowns constrained by (5). **Each `E_i` is affine in the two monomials `\bar k` and `\bar l` and contains the product `\bar k\bar l`;** hence it is *not* linear in `\bar k,\bar l` separately. The correct move (the outline's "linear solve" is impossible as stated, per the review) is to treat the **three monomials**
$$X := \bar k\,\bar l,\qquad Y := \bar k,\qquad Z := \bar l$$
as three unknowns. Writing `E_i = a_i\,X + p_i\,Y + q_i\,Z + d_i` (the `a_i,p_i,q_i,d_i` are explicit polynomials in `b,c,\bar b,\bar c,k,l` read off from (5)), the three conditions become a **linear system**
$$\mathbf{A}\begin{pmatrix}X\\Y\\Z\end{pmatrix} = \begin{pmatrix}-d_1\\-d_2\\-d_3\end{pmatrix}, \qquad \mathbf{A}=\begin{pmatrix}a_1&p_1&q_1\\a_2&p_2&q_2\\a_3&p_3&q_3\end{pmatrix}. \tag{6}$$
A direct computation (in `repro.py`) gives
$$\det\mathbf{A} = b\,\bar b\,c\,\bar c\cdot P_4, \quad P_4 = 2c^2k^2 - 6ck^2l + 4k^2l^2 - 6bkl^2 + 8bckl + 2b^2l^2 - 3b^2ck - 3bc^2k + b^2cl + bc^2l.$$
On the audited configuration `b\bar b c\bar c\neq 0` and `P_4 \approx -6.71 - 4.24i \neq 0`, so `\det\mathbf{A}\neq 0` there. **Assume for now `\det\mathbf{A}\neq 0`** (the exceptional locus is treated at the end of §6 by continuity). Then (6) has the unique solution `(X,Y,Z) = \mathbf{A}^{-1}(-d_1,-d_2,-d_3)^{\!\top}`; call its coordinates `(X_s, Y_s, Z_s)` (explicit rational functions of `b,c,\bar b,\bar c,k,l` with denominator `\det\mathbf A`). Because the true conjugates `(\bar k\bar l,\ \bar k,\ \bar l)` also satisfy (6), uniqueness forces
$$\bar k = Y_s, \qquad \bar l = Z_s, \qquad \bar k\,\bar l = X_s. \tag{7}$$

The first two of (7) determine the conjugates; the third is an **automatic consistency relation** since `\bar k\bar l = (\bar k)(\bar l) = Y_s Z_s`. Thus
$$Y_s Z_s - X_s = 0. \tag{8}$$
Let `R_{num}` be the numerator of `Y_s Z_s - X_s` (over the common denominator `(\det\mathbf A)^2`); then (8) says `R_{num} = 0` on the configuration.

### 5. Two certified factorizations

Let `\mathrm{num}` denote the numerator of `TN` after substituting `\bar k = Y_s`, `\bar l = Z_s` from (7) into (4) (again over a power of `\det\mathbf A`), and let `G := \gcd(\mathrm{num},\,R_{num})`, an explicit polynomial of total degree 10 in `b,c,\bar b,\bar c,k,l`. Direct polynomial expansion (verified symbolically in `repro.py`) establishes the two identities:

- **(I)** `R_{num} = (b-k)(c-l)\,G;`
- **(II)** `\mathrm{num} = q_N\cdot G`, where
$$q_N = -b^2ck - b^2cl + 2b^2kl - bc^2k - bc^2l + 2bck^2 + 4bckl + 2bcl^2 - 2bk^2l - 4bkl^2 + 2c^2kl - 4ck^2l - 2ckl^2 + 4k^2l^2 .$$

(The identity `R_{num} = (b-k)(c-l)G` and `\mathrm{num} = q_N G` are checked to be exact polynomial equalities — `sp.expand(R_{num} - (b-k)(c-l)G) = 0` and `sp.expand(\mathrm{num} - q_N G) = 0`.)

### 6. Conclusion of the identity

On the configuration, (8) gives `R_{num} = 0`. By (I), `(b-k)(c-l)\,G = 0`. By (ND) the factors `b-k\neq 0` and `c-l\neq 0`, hence
$$G = 0.$$
By (II) then `\mathrm{num} = q_N\cdot G = 0`. Since `\mathrm{num}` is the numerator of `TN|_{\bar k = Y_s,\bar l = Z_s}` over a nonzero power of `\det\mathbf A`, we get `TN|_{\bar k=Y_s,\bar l=Z_s} = 0`; and by (7) `\bar k = Y_s, \bar l = Z_s`, so in fact
$$TN = 0.$$
Finally `D\neq 0` by (NL), so by (4) `T = TN/D = 0`, and by (2) `OM = ON`. This proves the claim for every valid configuration with `\det\mathbf A \neq 0`.

The Cramer route above is valid only where `\det\mathbf A\neq0`. Rather than remove the locus `\det\mathbf A=0` by an analytic-continuation argument, we now give a **completely independent, unconditional** proof that `TN=0` on *every* admissible configuration — with no reference whatsoever to `\det\mathbf A`. This subsection alone suffices; §4–§5 are retained only as the motivation that produced the polynomials `E_1,E_2,E_3`.

### 6.2 Unconditional polynomial certificate (removes every non-degeneracy but the geometric ones)

We work on the **physical variety**: the eight quantities are no longer independent — they satisfy the reality relations `\bar b,\bar c,\bar k,\bar l` = complex conjugates of `b,c,k,l`. Write
$$b=b_1+ib_2,\quad c=c_1+ic_2,\quad k=k_1+ik_2,\quad l=l_1+il_2\qquad(b_j,c_j,k_j,l_j\in\mathbb R).$$

**Purely-imaginary structure.** Each `E_i` in (5) has the exact form `z_i-\bar z_i` (its second summand is the complex conjugate of its first: e.g. for `E_1`, `\overline{bc(\bar k-\bar b)(\bar l-\bar c)}=\bar b\bar c(k-b)(l-c)`). Hence `E_i=2i\,\mathrm{Im}(z_i)` is **purely imaginary**, so
$$E_i=0 \iff \mathrm{Im}(E_i)=0. \tag{9}$$
Likewise `\overline{TN}=T\bar D=-TN` (noted after (4)), so `TN` is purely imaginary and `TN=0\iff\mathrm{Im}(TN)=0`. Regarding `\mathrm{Im}(E_i)` and `\mathrm{Im}(TN)` as real polynomials in the eight real coordinates `b_1,b_2,\dots,l_2`, the three reality conditions of §3 read `\mathrm{Im}(E_1)=\mathrm{Im}(E_2)=\mathrm{Im}(E_3)=0`, and the goal is `\mathrm{Im}(TN)=0`.

**Reduction to `B=1`.** All of `E_i` and `TN` are homogeneous under the complex scaling `z\mapsto\mu z` (unbarred variables carry a factor `\mu`, barred ones `\bar\mu`): each of the three summands of `TN` scales by `\mu^2\bar\mu^2`, and each `E_i` by `\mu^2\bar\mu^2`. Applying `\mu=1/b` (`b\neq0`) sends the admissible configuration `(A,B,C,K,L)=(0,b,c,k,l)` to the congruent-up-to-similarity configuration `(0,1,c/b,k/b,l/b)` — a similarity preserves every angle condition, every interior/inside-angle hypothesis, and all non-collinearities, so it is again admissible — and multiplies `TN` by `b^{-2}\bar b^{-2}\neq0`. Thus `TN=0` for the original configuration **iff** it holds after normalizing `b=1`. We may therefore set
$$b=1,\qquad \bar b=1\quad(\text{i.e. }b_1=1,\ b_2=0),$$
leaving the six real unknowns `c_1,c_2,k_1,k_2,l_1,l_2`.

**The four geometric non-degeneracy factors.** Put
$$
w_1=|B-K|^2=(k_1-1)^2+k_2^2,\quad
w_2=|C-L|^2=(l_1-c_1)^2+(l_2-c_2)^2,
$$
$$
w_3=\mathrm{Im}(\bar k\,l)=k_1l_2-k_2l_1,\qquad
w_4=\mathrm{Im}(\bar b\,c)=c_2,\qquad
W:=w_1w_2w_3w_4 .
$$
On an admissible configuration **each factor is nonzero**: `w_1>0` since `K\neq B` (ND); `w_2>0` since `L\neq C` (ND); `w_3=\tfrac{1}{2i}D=\mathrm{Im}(\bar kl)\neq0` since `A,K,L` are non-collinear (NL); `w_4=\mathrm{Im}(\bar bc)\neq0` since `A,B,C` are non-collinear (NC, and here `\bar bc=c` so `w_4=c_2`). Hence `W\neq0` on every admissible configuration.

**The certificate.** In the polynomial ring `\mathbb Q[c_1,c_2,k_1,k_2,l_1,l_2]` there is an **exact polynomial identity**
$$
\boxed{\;W\cdot\mathrm{Im}(TN)\;=\;f_1\,\mathrm{Im}(E_1)+f_2\,\mathrm{Im}(E_2)+f_3\,\mathrm{Im}(E_3)\;}
\tag{10}
$$
for suitable polynomials `f_1,f_2,f_3\in\mathbb Q[c_1,c_2,k_1,k_2,l_1,l_2]`; equivalently, `W\cdot\mathrm{Im}(TN)` lies in the ideal `\mathcal I=\big(\mathrm{Im}(E_1),\mathrm{Im}(E_2),\mathrm{Im}(E_3)\big)`. This membership is a decidable, *exact* fact, established by reducing `W\cdot\mathrm{Im}(TN)` to normal form `0` modulo a Gröbner basis of `\mathcal I` (**Buchberger's algorithm**, a finite, exact — non-numerical — decision procedure): a terminating reduction to `0` is a rigorous certificate of ideal membership (knowledge_base.md, *Optimization / critical points*: "**Gröbner-basis ideal membership (normal form `=0`): a terminating reduction is a rigorous certificate**", together with the ideal-saturation/Rabinowitsch trick `y\Pi-1` there for imposing `\Pi\neq0`). The reduction returns remainder `0` at the first power `W^1`; the computation and the existence of the cofactors `f_i` (they exist precisely because the reduction succeeds) are recorded in `certificate.py` (`N=1: W*iTN in ideal? True`, and remainder `0` after division by the Gröbner basis).

Because (10) is an identity of polynomials, it holds at **every** real point `(c_1,\dots,l_2)`, in particular at every admissible configuration (normalized to `b=1`). There, by §3 and (9), `\mathrm{Im}(E_1)=\mathrm{Im}(E_2)=\mathrm{Im}(E_3)=0`, so the right-hand side of (10) is `0`; and `W\neq0`. Therefore
$$\mathrm{Im}(TN)=0\ \Longrightarrow\ TN=0.$$
By (4), `T=TN/D=0` (`D\neq0` by (NL)); by (2), `OM=ON`. Un-normalizing (the reduction `b=1` was reversible), this holds for **every** admissible configuration — with `\det\mathbf A` playing no role at all. `\blacksquare`

**Why this closes the former gap.** The old §6 proved `OM=ON` only where `\det\mathbf A\neq0` and then tried to remove the locus `\{\det\mathbf A=0\}` by continuity — an argument that required (and did not supply) real-analyticity of the `\alpha`-branch and non-vanishing of `\det\mathbf A(\alpha)` for *every* triangle. Identity (10) sidesteps this entirely: it is an unconditional polynomial identity on the physical variety whose only hypotheses are the four *geometric* non-degeneracies `w_1,\dots,w_4\neq0` (all built into "admissible"), so `TN=0` follows on the whole admissible set at once, including wherever `\det\mathbf A=0`. (Over the complex-independent-conjugate ring the analogous membership *fails* — there is a spurious component on which `TN\neq0` — which is exactly why the reality slice `\bar\bullet=\overline{\bullet}` is essential and is used here.) ∎

### Verification artifacts
- `results/imo-2026-02/certificate.py` — the §6.2 closure: verifies (a) each `E_i` and `TN` is purely
  imaginary (real part `\equiv0`); (b) the exact ideal membership `W\cdot\mathrm{Im}(TN)\in(\mathrm{Im}E_1,\mathrm{Im}E_2,\mathrm{Im}E_3)`
  at power `N=1` via Gröbner reduction to remainder `0`; over the real slice with `B=1`. Output:
  `Re(...) all 0: True True True True`; `N=0: iTN in ideal? False`; `N=1: W*iTN in ideal? True`;
  `remainder after division by GB is 0: True`.
- `results/imo-2026-02/repro.py` — proves symbolically: (a) each `E_i` is affine in `(X,Y,Z)=(\bar k\bar l,\bar k,\bar l)`; (b) `\det\mathbf A = b\bar b c\bar c\,P_4`; (c) identities **(I)** and **(II)**; and evaluates every quantity on the audited configuration.
- `results/imo-2026-02/verify_config.py` — supplies the numerical configuration and confirms `OM=ON`, all `C_i\in ℝ`, and the corrected circumcenter sign.
- `results/imo-2026-02/check_s3.py` — confirms (sanity check only) every §3 sign fact on a valid CCW configuration: `\mathrm{Im}(\bar b c)>0`, `\mathrm{Im}(\bar b k)>0`, `\mathrm{Im}(\bar c l)<0`, `\mathrm{Im}(\bar b l)>0`; the six directed angles `\theta_i,\beta_i,\gamma_i\in(0,\pi)`; the exact arg-identities `\arg C_i=(\text{angle}_1-\text{angle}_2)`; and `C_1,C_2,C_3\in\mathbb R_{>0}`.

## Promotable lemmas

- **Lemma 2 (reality hinge for directed angles):** if two directed angles `\theta_1=\arg z_1`,
  `\theta_2=\arg z_2` (principal args) both lie in `(0,\pi)` and their unsigned values are equal, then
  `\arg(z_1/z_2)=\theta_1-\theta_2=0`, so `z_1/z_2>0`; in particular the ratio is real. This is the
  general mechanism for turning an *unsigned* Olympiad angle equality into an *exact* directed-angle
  equality (mod `2\pi`, not merely mod `\pi`) whenever an interior/orientation hypothesis pins both
  directed angles into `(0,\pi)`, killing the supplementary branch. Proved in §3.1. Reusable in any
  complex-coordinate angle-condition problem. Companion facts also proved: sign rule (SGN)
  `\angle(PU\!\to\!PV)\in(0,\pi)\iff[P,U,V]>0`, and the side-of-line dictionary (SIDE).
- **Lemma 1 (circumcenter of `0,k,l`):** `O = (k|l|^2 - l|k|^2)/(k\bar l - \bar k l) = kl(\bar l-\bar k)/(k\bar l-\bar k l)`, valid whenever `k\bar l-\bar k l\neq 0` (non-collinear). Proved in §1. Reusable in any complex-coordinate circumcenter computation.
- **Reality-elimination lemma (crux):** three reality conditions on cross-ratio-type expressions that are each *affine-bilinear* in the conjugate pair `(\bar k,\bar l)` linearize in the three monomials `(\bar k\bar l,\bar k,\bar l)`, so a single 3×3 Cramer solve extracts the conjugates rationally; the leftover consistency `\bar k\cdot\bar l = (\bar k)(\bar l)` is the equation that drives the target to zero. Proved (as identities I, II) in §4–§5.
- **Physical-slice certificate lemma (crux, §6.2):** when a complex-coordinate target `TN` and reality
  conditions `E_i` all have the form `z-\bar z` (purely imaginary), the identity `TN=0` on the *physical*
  configuration set is equivalent to `\mathrm{Im}(TN)=0` on `\{\mathrm{Im}(E_i)=0\}` over the **real**
  variables `\mathrm{Re},\mathrm{Im}` of the affixes. This *real* ideal membership can hold (certified
  exactly by Gröbner/Buchberger) even when the naïve complex membership with independent conjugates fails
  (spurious components). It removes any auxiliary determinant / genericity hypothesis in one exact step.
  General recipe for closing "valid where `\det\neq0`" gaps in complex-number olympiad proofs. Proved as
  identity (10) in §6.2 (`certificate.py`).
