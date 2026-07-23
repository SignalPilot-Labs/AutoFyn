## Status
partial

## Approaches tried
- **Antipode reduction (steps 1–4, certified, unchanged).** With `Γ` the
  circumcircle of `AKL`, `O` its center, `A* := 2O−A` the antipode of `A` on
  `Γ`: proved `OM=ON ⟺ A*B=A*C` (pure vector algebra) and `A*` = intersection
  of the perpendicular to `AK` at `K` with the perpendicular to `AL` at `L`
  (Thales / inscribed-angle-in-semicircle). Complete, gap-free, certified in
  `lemmas/antipode-reduction.md`. Unchanged this round; imported as-is.
- **NEW this round: the two-angle-formula route (L1, L2 + angle chase),
  following the outline and the explorer's report.** I re-verified the two
  angle formulas
  $$\angle ABA^* = \theta + 90^\circ-\gamma,\qquad \angle ACA^* = \theta+90^\circ-\beta$$
  independently on 4 triangle shapes `(p,q)=(0.3,1.7),(-0.6,1.2),(0.1,2.5),
  (0.9,1.3)` at 5 values of `θ` each (`5°,10°,15°,20°,25°`), building `K,L`
  from scratch via `fsolve` on the exact hypothesis system `∠KBA=∠ACL=θ`,
  `∠LBK=∠LNC`, `∠LCK=∠BMK`, and computing `A*=2·circumcenter(AKL)−A`
  directly. Agreement to `1e-9`–`1e-13` in every one of the 20 trials — this
  matches and extends the explorer's and outline-reviewer's numerical
  findings. **I did NOT succeed in deriving L1/L2 synthetically from
  H1∧H2∧H3 this round; they remain numerically-verified conjectures.** See
  "Current best" for exactly how far the derivation got and where it stalls,
  and for a new structural finding (the `O'`-reformulation) that clarifies
  the shape of the gap without closing it.
- **NEW finding this round (genuinely new, not in the explorer's report):
  reformulation of L1 via the circumcenter `O'` of the *original* triangle
  `ABC`.** Numerically discovered and confirmed (same 4 shapes × 5 θ values,
  precision `1e-8`–`1e-12`):
  $$\angle O'BA^* \;=\; \angle ABK \;=\; \theta,$$
  where `O'` is the circumcenter of triangle `ABC` (NOT of `AKL` — a fixed
  point, independent of `θ`). This follows algebraically from L1 using the
  classical fact `∠O'BA = 90°−γ` (isosceles-triangle base-angle argument in
  triangle `O'AB`, since `O'A=O'B=O'C=R_{ABC}`) — indeed if `∠ABA^*=θ+90°-γ`
  and `∠ABO'=90°-γ` with `O'` and `A^*` both on the far side of `BA` from
  `C`-ish in the correct rotational sense, then `∠O'BA^*=∠ABA^*-∠ABO'=θ`.
  **I then tested whether this comes from a full spiral similarity centered
  at `B` sending `O'↦A^*`, `A↦K` (which would need the extra ratio
  `BA^*/BO' = BK/BA`, not just the angle equality) — refuted numerically**:
  e.g. at `(p,q)=(0.3,1.7),θ=10°`: `BK/BA≈0.4038` vs `BA^*/BO'≈0.9209`,
  clearly unequal. So `∠O'BA^*=∠ABK` is a genuine, clean-looking angle
  identity — a strictly simpler-looking restatement of L1 — but it is
  **not** the shadow of an honest spiral similarity/congruence, and I could
  not find the mechanism that forces the angle equality alone (without the
  ratio) from H1∧H2∧H3. This is recorded as a **candidate lead for a future
  round**, not a proof, and should not be mistaken for a completed spiral
  similarity argument.
- **Attempted a direct trigonometric/Law-of-Sines derivation of L1 in
  triangle `ABK` plus the right angle `∠AKA*=90°` (the "H3 pins r1"
  mechanism the outline suggested attempting first).** Set up
  `AK = AB·sinθ/sin(∠AKB)` (Law of Sines in `ABK`, `∠AKB=180°-θ-∠BAK`) and
  tried to express `∠A^*KB` (needed to locate `A^*` relative to `B` via the
  right triangle `AKA^*`) using the perpendicularity `∠AKA^*=90°`. This
  requires knowing on which side of line `AK` the point `A^*` lies and the
  actual magnitude of `∠AKB`, both of which depend on `L` (via the second
  perpendicular defining `A^*`) — i.e. this "local" computation at `K` alone
  cannot pin down `A^*` without re-introducing `L`'s position, exactly as
  the round-2 write-up already found for the "270°" identity. I confirmed
  this is the same obstruction, not a new dead end distinct from the ones
  already on file — **did not find a way to close it in the time available
  this round.**

- **NEW this round (Round 4): replaced the round-3 buggy directed-angle
  sign step with a genuinely cleaner, uniform signed identity — no case
  split needed for the final conclusion.** Working entirely in the
  coordinate frame `B=(-1,0), C=(1,0), A=(p,q)` with `q>0` (WLOG — a
  reflection across line `BC` preserves every hypothesis, since they are
  all unsigned-angle statements, and preserves the conclusion `OM=ON`,
  which is symmetric under reflection; this is the same frame used
  throughout `coordinate-trig-bash`), I derived and extensively
  numerically stress-tested (see below) the **signed** relations
  $$\mathrm{dir}(B,A^*) = \mathrm{dir}(B,A) + (\gamma-90^\circ-\theta)
  \pmod{360^\circ} \qquad (\mathrm{I})$$
  $$\mathrm{dir}(C,A^*) = \mathrm{dir}(C,A) + (\theta+90^\circ-\beta)
  \pmod{360^\circ} \qquad (\mathrm{II})$$
  where `dir(X,Y)` is the direction (angle from the positive `x`-axis) of
  ray `XY`. These are exactly the signed versions of L1
  (`∠ABA*=θ+90°-γ`, up to sign) and L2 (`∠ACA*=θ+90°-β`), but — new finding
  this round — **the sign is completely determinate: there is no
  configuration flip / trichotomy needed at all**, unlike what the
  round-3 file and this round's explorer report suggested (their
  "trichotomy on sign(θ+90°-γ)" was a correct but unnecessarily
  complicated description of what turns out to be a single uniform
  signed law). This closes the round-3 gap (the false "by symmetry, same
  sign convention" step) by REPLACING it entirely, not patching it.
  **Numerical verification (this round):** built `K,L` from a from-scratch
  root-finder (bisection/`brentq` on the exact hypothesis system, with an
  explicit scan over the whole valid `r1`-range to avoid `fsolve`
  convergence failures used in earlier verification attempts), tested on 8
  distinct triangle shapes (including two very-obtuse-angle shapes,
  `γ=163.3°` and `β=153.4°`) across up to 9 values of `θ` each (`2°` up to
  `40°`, always kept `<min(β,γ)`): **(I),(II) matched to `1e-12`–`1e-14` in
  every genuine (containment-respecting) trial.** One apparent counterexample
  was found and diagnosed: at `(p,q)=(-0.6,1.2)`, `θ=34°`–`36°` (close to
  the domain boundary `min(β,γ)=36.87°`), the root-finder's scan picked up
  a *spurious* algebraic root of the hypothesis system for which `L` fails
  the containment condition (`L` not inside triangle `BNC`, confirmed
  directly) — i.e. not the genuine geometric configuration at all. This is
  a **new methodological finding worth flagging explicitly**: naive
  numerical root-finding on the raw hypothesis equations can converge to
  extraneous roots outside the valid domain, especially near the boundary
  `θ→min(β,γ)`, and any future numerical check of L1/L2 (or any hypothesis
  fact) **must explicitly verify containment of K,L** before trusting the
  angle-identity check, not just check that the angle equations are
  satisfied. Once this spurious root is excluded, (I),(II) hold in every
  tested case with no exception.
- **Proved this round (full detail, no gap, granting (I),(II)): the
  reduction "(I)∧(II) ⟹ A*B=A*C" is now simpler and fully rigorous, with NO
  case split on the sign of anything except the single degenerate point
  `θ=90°-α`** (handled by the same continuity argument as round 3, still
  valid). See the full write-up below, replacing round 3's Case-1/2/3
  trichotomy derivation (which itself was fine, but rested on the buggy
  directed-angle step) with a direct computation from (I),(II).
- **Attempted, per this round's dispatch, to prove (I) [equivalently L1]
  synthetically using the isogonal/O'-reformulation as a stepping stone.**
  No success — the obstruction is the same one recorded in round 3 and by
  this round's explorer: any "local" computation using only the right angle
  `∠AKA*=90°` (Thales, certified) and triangle `ABK` cannot pin down `A*`
  without re-introducing `L`'s position (via the second perpendicular
  defining `A*`), and no concyclicity or spiral-similarity linking `A*` to
  `B` (or the fixed point `O'`=circumcenter(ABC)) via `K` alone has been
  found (all specific guesses tested and refuted, see round-3/round-4
  Dead-ends list, unchanged). **Honestly reporting: (I) and (II) — the
  sharpened, sign-determinate replacements for L1/L2 — remain open,
  numerically-verified-only conjectures.** This is the same underlying gap
  as before, now stated in its cleanest possible form.

## Current best

**Fully proved, no new gap (imported unchanged):** the antipode reduction
`OM=ON ⟺ A^*B=A^*C`, with `A^*` the intersection of (perpendicular to `AK`
at `K`) and (perpendicular to `AL` at `L`) — see
`lemmas/antipode-reduction.md`.

**Fully proved THIS round (new, rigorous, no gap — replaces round 3's proof
of the same reduction, which had a real, reviewer-caught error in its
directed-angle sign bookkeeping): the reduction `(I)∧(II) ⟹ A^*B=A^*C`**,
where (I),(II) are the sign-determinate signed identities stated and
numerically stress-tested above (equivalent to the unsigned L1/L2 up to
taking absolute values, but with a completely uniform sign — **no
configuration trichotomy is needed at all**, only the same single
degenerate boundary point round 3 already needed continuity for). This
proof is simpler than round 3's (no case split on `sign(θ+90°-γ)` is
needed to reach the conclusion) and has no analogue of round 3's bug: it
never asserts a directed-angle "sign convention... by symmetry" — instead
it computes `dir(C,A)` directly from elementary facts about the coordinate
frame, exactly parallel to (not just "by symmetry with") the computation at
`B`.

**Still an open gap (not closed this round): (I) and (II) themselves
[equivalently L1, L2] are not derived from H1∧H2∧H3** — they remain
numerically verified (now to a higher standard of care, see the spurious-root
finding above) but unproved. See "What remains open" below.

### Proof of "(I) ∧ (II) ⟹ A*B = A*C" (new this round, full detail, no gap)

**Setup / WLOG frame.** Place the triangle in coordinates
`B=(-1,0)`, `C=(1,0)`, `A=(p,q)`. We may take `q>0`: if the original
configuration has `q<0`, reflect the entire figure (all of `A,B,C,K,L,M,N,
O,A^*`) across line `BC`. A reflection is an isometry, so it preserves every
distance (`A^*B,A^*C`, hence the target equality) and every unsigned angle
(hence every hypothesis `∠KBA=∠ACL`, `∠LBK=∠LNC`, `∠LCK=∠BMK`, and every
containment condition, all being unsigned-angle/incidence statements). So
this reflection is harmless and we assume `q>0` from now on.

Write `dir(X,Y) \in (-180°,180°]` for the direction of ray `XY` (angle from
the positive `x`-axis, taken mod `360°` in this range), and let
`\alpha=\angle BAC,\ \beta=\angle ABC,\ \gamma=\angle ACB`
(so `\alpha+\beta+\gamma=180°`, standard angle-sum).

**Step 1 (elementary base-angle directions).** Since `B=(-1,0),C=(1,0)`,
`dir(B,C)=0°` and `dir(C,B)=180°`. Since `q>0`, both `A-B` and `A-C` have
strictly positive `y`-component, so `dir(B,A)\in(0°,180°)` and
`dir(C,A)\in(0°,180°)`. By definition, the (unsigned) interior angle
`\beta=\angle ABC` is the angle between rays `BA,BC`; since `dir(B,C)=0`
and `dir(B,A)\in(0°,180°)`, this unsigned angle equals `dir(B,A)` itself
(the absolute value of `dir(B,A)-0`, which is already nonnegative and
`<180°`). Hence
$$dir(B,A) = \beta. \qquad (\star)$$
Likewise `\gamma=\angle BCA` is the angle between rays `CB,CA`; since
`dir(C,B)=180°` and `dir(C,A)\in(0°,180°)`, this equals `180°-dir(C,A)`
(again already the correct nonnegative value `<180°`). Hence
$$dir(C,A) = 180°-\gamma. \qquad (\star\star)$$

**Step 2 (apply (I), (II)).** By (I), `dir(B,A^*) = dir(B,A)+(\gamma-90°-
\theta)`; substituting `(\star)`:
$$dir(B,A^*) = \beta+\gamma-90°-\theta = (180°-\alpha)-90°-\theta = 90°-\alpha-\theta,$$
using `\beta+\gamma=180°-\alpha`. By (II), `dir(C,A^*)=dir(C,A)+(\theta+90°-
\beta)`; substituting `(\star\star)`:
$$dir(C,A^*) = (180°-\gamma)+\theta+90°-\beta = 270°-\beta-\gamma+\theta = 270°-(180°-\alpha)+\theta = 90°+\alpha+\theta.$$

**Step 3 (unsigned base angles of triangle `A^*BC` agree).** Since
`dir(B,C)=0°`, the unsigned angle `\angle A^*BC` between rays `BA^*,BC`
equals `|dir(B,A^*)-0°| = |90°-\alpha-\theta|` (taking the representative
in `(-180°,180°]`; since `\alpha,\theta\in(0°,180°)` with `\alpha+\theta`
bounded well below `270°` in any genuine triangle configuration, this
absolute value is the correct unsigned angle with no further wraparound
ambiguity). Since `dir(C,B)=180°`, the unsigned angle `\angle A^*CB`
between rays `CA^*,CB` equals `|dir(C,A^*)-180°| = |90°+\alpha+\theta-180°|
= |\alpha+\theta-90°| = |90°-\alpha-\theta|`. Hence
$$\angle A^*BC = \angle A^*CB = |90°-\alpha-\theta| \qquad (\heartsuit)$$
**identically**, with no case split on any sign — the two absolute values
resolve to literally the same quantity `|90°-\alpha-\theta|` regardless of
its sign, because the two directions `dir(B,A^*),dir(C,A^*)` were computed
by the same substitution `\beta+\gamma=180°-\alpha` acting with opposite
signs at the two vertices.

**Step 4 (conclude, splitting only on whether the common angle is `0`).**

*Non-degenerate case: `\alpha+\theta\neq 90°`.* Then `(\heartsuit)` gives a
strictly positive common value `\delta:=|90°-\alpha-\theta|>0` for both
`\angle A^*BC` and `\angle A^*CB`. In particular `A^*` does not lie on line
`BC` (a point `X` on line `BC` distinct from `B,C` has `\angle XBC\in\{0°,
180°\}`, not the positive value `\delta<180°`; and `X=B` or `X=C` are
excluded since `A^*B=0` or `A^*C=0` would force `\delta=0` by extending the
inscribed-angle argument in the degenerate limit, contradiction). So
`A^*BC` is a genuine, non-degenerate triangle with two equal angles at
`B,C`. By the **Isosceles Triangle Converse** (standard Euclidean fact:
equal base angles imply equal opposite sides — via the Law of Sines in
triangle `A^*BC`, `A^*C/\sin(\angle A^*BC) = A^*B/\sin(\angle A^*CB)`, and
`\sin(\angle A^*BC)=\sin(\angle A^*CB)` since the angles themselves are
equal, giving `A^*C=A^*B`), we conclude `A^*B=A^*C`.

*Degenerate case: `\alpha+\theta=90°`.* Here `(\heartsuit)` gives
`\angle A^*BC=\angle A^*CB=0`, i.e. `A^*` lies on ray `BC` extended (both
rays `BA^*,CA^*` are along line `BC`) — a single, isolated value of `\theta`
(namely `\theta_0:=90°-\alpha`), and only when `\theta_0` lies in the valid
domain `(0,\min(\beta,\gamma))` at all. We handle it by **continuity**,
exactly as in round 3's version of this argument (the underlying continuity
input is unchanged, only what it is applied to is simplified): the function
`f(\theta):=A^*(\theta)B-A^*(\theta)C` is continuous on the open interval
`(0,\min(\beta,\gamma))` wherever `K(\theta),L(\theta)` are the (locally
unique, per the certified existence/uniqueness machinery in
`lemmas/existence-uniqueness-r1-r2.md`) solutions of the hypothesis system,
since `A^*=A^*(K,L)` is defined by intersecting two lines through `K,L`
depending continuously (in fact real-analytically) on `(K,L)`. The
non-degenerate case shows `f\equiv 0` on the interval minus the single point
`\theta_0`; taking `\theta\to\theta_0` along this dense complement and using
continuity of `f` gives `f(\theta_0)=\lim_{\theta\to\theta_0}f(\theta)=0` as
well. So `A^*B=A^*C` holds at `\theta_0` too.

Both cases give `A^*B=A^*C`; they are exhaustive (they partition on whether
the single real number `\alpha+\theta-90°` is zero or not). This completes
the proof of "(I)∧(II) ⟹ A^*B=A^*C", **granting (I) and (II)**, and hence
(via the certified `lemmas/antipode-reduction.md`) of "(I)∧(II) ⟹ OM=ON".
$\blacksquare$ *(conditional on (I),(II) — see below, the one remaining
gap.)*

### What remains open

The **only** remaining gap in this entire chain is proving the signed
identities **(I)** `dir(B,A^*)=dir(B,A)+(\gamma-90°-\theta)` and **(II)**
`dir(C,A^*)=dir(C,A)+(\theta+90°-\beta)` — equivalently, the unsigned facts
L1 (`\angle ABA^*=|\theta+90°-\gamma|`) and L2
(`\angle ACA^*=|\theta+90°-\beta|`) together with the (now shown to be
automatic/uniform, not case-dependent) sign — from the three hypotheses
`\angle KBA=\angle ACL=\theta`, `\angle LBK=\angle LNC`, `\angle LCK=
\angle BMK` and the containment/orientation conditions on `K,L`. I was
unable to close this gap this round. What I can honestly report:

- (I), (II) are **numerically extremely robust and now verified to a
  higher standard**: this round I built a from-scratch bisection/`brentq`
  root-finder (avoiding `fsolve`'s occasional non-convergence), tested 8
  triangle shapes (including two very-obtuse configurations, `γ=163.3°`
  and `β=153.4°`) across up to 9 `θ` values each, and **explicitly checked
  containment of `K,L`** at every trial (a check earlier rounds did not
  always perform) — this caught and correctly diagnosed one spurious
  algebraic root (see above) as non-geometric, rather than mistaking it
  for a counterexample. In every genuine (containment-respecting) trial,
  agreement is to `1e-12`–`1e-14`.
- Attempted, per this round's task, to prove (I) using the isogonal/`O'`
  reformulation (`O'`=circumcenter of `ABC`, a fixed point) as a stepping
  stone: no success. The obstruction is unchanged from round 2/3: any
  computation using only the right angle `∠AKA^*=90°` (Thales, certified
  in `lemmas/antipode-reduction.md`) and triangle `ABK` cannot pin down
  `A^*` without re-introducing `L`'s position (via the second perpendicular
  that also defines `A^*`), and no concyclicity or spiral-similarity
  linking `A^*` to `B` or `O'` via `K` alone has been found — every specific
  guess tested (this round and previous rounds) has been numerically
  refuted; see the unchanged Dead-ends list.
- (I), (II) genuinely require the **full** hypothesis system (perturbing
  `r1` or `r2` away from their hypothesis-satisfying values, holding `θ`
  fixed, breaks the formula — confirmed by the originating explorer in
  round 3, not independently re-verified by me this round due to time, but
  structurally consistent with the certified Decoupling Lemma, where both
  `r1,r2` enter the definition of `A^*` through the two perpendiculars).

I am reporting this honestly as **Status: partial**. The reduction
`(I)∧(II) ⟹ OM=ON` is now a complete, rigorous, case-complete piece of
mathematics (rewritten and simplified this round, with the round-3 bug
fully removed rather than patched); (I) and (II) themselves are not
proved, only strongly corroborated numerically, now with an extra layer of
care (containment-checking) that specifically rules out the failure mode
that could have made round 3's or the explorer's numerical claims
unreliable.

## Promotable lemmas

**Lemma (signed-angle isosceles reduction: (I)∧(II) ⟹ A*B=A*C) — NEW,
supersedes round 3's version of this lemma.**
*Statement:* Let `ABC` be a triangle in the frame `B=(-1,0),C=(1,0),
A=(p,q)` with `q>0`, `\alpha=\angle BAC,\beta=\angle ABC,\gamma=\angle ACB`,
and let `A^*` be any point such that, for some `\theta\in(0,\min(\beta,
\gamma))`, the **signed** identities
`dir(B,A^*)=dir(B,A)+(\gamma-90°-\theta)` and
`dir(C,A^*)=dir(C,A)+(\theta+90°-\beta)` hold (mod `360°`). Then `A^*B=A^*C`.
*Proved in full above* (Steps 1–4), with the degenerate case
`\alpha+\theta=90°` handled by continuity, and **no other case split
needed** — this is a genuine simplification over round 3's three-case
proof of the analogous (but buggy-derivation) statement, since here the two
base angles of triangle `A^*BC` are shown to coincide as literal absolute
values of two directions computed by the identical substitution
`\beta+\gamma=180°-\alpha`, rather than via an asserted "same sign
convention." Reusable, fully general (does not depend on how `A^*`,`K`,`L`
were constructed, only on the two signed-angle hypotheses and the frame
convention `q>0`), recommended for certification into
`results/imo-2026-02/lemmas/` as the clean building block for whichever
future round manages to close (I)/(II). **(I) and (II) themselves are NOT
part of this lemma and remain unproved** — this is the sole remaining gap
of this whole approach.

**Minor methodological finding (not a lemma, but worth recording for future
numerical verification in this problem):** naive root-finding on the raw
hypothesis equations `∠LBK=∠LNC`, `∠LCK=∠BMK` can converge to algebraic
roots for which `K` or `L` fails the required containment condition
(inside triangle `BMC`/`BNC` respectively), especially for `θ` close to the
domain boundary `\min(\beta,\gamma)`. Any future numerical check of L1, L2,
(I), (II), or any other hypothesis-derived fact in this problem should
explicitly verify containment of the constructed `K,L`, not just that the
angle equations are satisfied to high precision.
