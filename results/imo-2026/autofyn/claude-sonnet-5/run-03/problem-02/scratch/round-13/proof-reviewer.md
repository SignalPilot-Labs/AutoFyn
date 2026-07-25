# Round 13 proof-reviewer report — imo-2026-02

Start: 2026-07-25 06:30 UTC.

Three built approaches this round: `coordinate-bash-resultant-boundary`,
`coordinate-bash-resultant-boundary-pointwise-tangent`,
`coordinate-bash-resultant-boundary-pointwise-sos`. All three are
**CHANGES REQUESTED** (real, independently-verified progress; no
overclaiming; no APPROVE). None is RETHINK — every route remains
internally sound, with new theorems that are correctly proved and
precisely-scoped open gaps that are honestly disclosed as numeric-only,
not asserted as proved.

The proof-reviewer independently rebuilt every load-bearing new symbolic
claim from scratch, in fresh `sympy`/`numpy`/`mpmath` sessions, never
trusting a builder's own "sympy confirms" report — with particular focus
on the four items flagged by the dispatch.

## 1. `coordinate-bash-resultant-boundary` — the parity-obstruction theorem
and the `Num` identity

**The `Num` identity (Item 1).** Independently rebuilt from scratch: with
`X0 = ct/(2(ds+ct))`, `p = s(4X0-3)`, `q = c(4X0-1)`, computed
`q^2(1-X0) - p^2*X0` via `sympy.together`/`sympy.fraction`. Own session:
denominator is exactly `2(ct+ds)^3`, and the numerator, expanded, matches
the file's displayed `Num = c^5t^3-3c^3d^2s^2t-c^3s^2t^3+2c^2d^3s^3
-6c^2ds^3t^2-9cd^2s^4t` **exactly** (`sympy.simplify` of the difference
gives `0` identically, both `together()`-based and direct-subtraction
checks agree). This is a genuine, unconditional polynomial identity, not
an approximation — confirms the claim in full. Certified
`lemmas/num-identity-exact-squaring-equivalence.md`. The file is honest
that this only closes the algebraic-identity half of Step 4/5; the
licensing fact `p<0,q>0` on the residual domain remains numeric-only, and
the file says so explicitly (not overclaimed).

**The `B<pi/2`-conditioned `B<=C iff c>=2t^2-1` fix (Item 2).** Elementary
`cos`-monotonicity argument, checked by hand: correct, and the missing
precondition (`B<pi/2`) is now stated explicitly rather than silently
assumed, discharged by citing the already-certified round-11 fact that
`B<pi/2` holds with comfortable margin on the residual sub-domain. No
issue found.

**The `Z2xZ2` parity-obstruction theorem (Item 3, the round's headline
novel claim) — independently re-derived and CONFIRMED in full.** Built an
own fresh script implementing the four sign-projectors `f_{ab} =
(1/4)*sum_{eps,delta in {+-1}} eps^a delta^b f(eps*c,s,delta*d,t)` and
applied them to `G0 := ct(1-2d^2)-2sd^3`, `E_num := ct*f1(sigma,tau) +
ds*f2(sigma,tau)` (`f1,f2` as in the certified round-12 `E`-reduction),
`Num` (as above), and `Bc := c-2t^2+1`. Result: **exact match to the
file's claimed graded components in every case** —
`(G0)_{00}=(G0)_{11}=0`, `(E_num)_{00}=(E_num)_{11}=0`,
`(Num)_{00}=(Num)_{11}=0`, `(Bc)_{00}=1-2t^2`, `(Bc)_{10}=c`,
`(Bc)_{01}=(Bc)_{11}=0`. Also independently confirmed `q_1,r_0` (pulled
from the already-certified `lemmas/case-b-e-lt-0-t-factorization.md`, not
retyped from this file) are literally polynomials in `sigma=s^2,tau=t^2`
alone, i.e. trivially in `R_{00}`. Given these graded-component facts, the
theorem's core logical step — that for `lambda` a polynomial in
`sigma,tau` alone (no explicit odd `c,d` power), `(lambda*G)_{00} =
lambda_{00}*G_{00} + lambda_{10}*G_{10}+lambda_{01}*G_{01}+lambda_{11}*
G_{11}` collapses to `0` whenever `G in {G0,E_num,Num}` (since
`G_{00}=G_{11}=0` and `lambda_{10}=lambda_{01}=lambda_{11}=0` for
`lambda` in `R_{00}`) — is elementary, correct algebra on the graded
ring, verified by hand against the confirmed component values. This makes
the Corollary ("any working certificate for `-q_1` using these four
generators must include a multiplier with an explicit bare odd power of
`c` or `d`") a genuinely rigorous structural theorem, not an empirical
observation dressed up as one. This is real, novel, correctly-proved
machinery — a first for this population (no prior round used a grading
argument). Certified `lemmas/parity-obstruction-q1-r0-certificate.md`.

**Items 4-5 (concrete candidate probe, rectangular-relaxation negative
finding).** Both are honestly reported as negative/inconclusive
(`G0*(-Num)` ruled out as not proportional to `q1` or `r0`; the `nnls`
near-fit explicitly flagged as not a valid identity due to mismatched
degrees; the tight-box relaxation shown to fail narrowly). No claim of
closure here, and none is made. Accurate.

**Net.** Genuine progress: two previously-open items fully closed exactly
as directed, plus one new, independently-confirmed structural theorem that
correctly explains (not just empirically observes) why round 12's ansatz
class could never work. The actual target — a working Positivstellensatz
certificate for `-q1,-r0` — is **not** found. Status `partial` is accurate,
not an overclaim. **Verdict: CHANGES REQUESTED.**

## 2. `coordinate-bash-resultant-boundary-pointwise-tangent` — the `f-g|_C
= D1` identity and the `Tgt` radical-free comparison target

**`f-g|_C = D1` (New result 2).** Independently rebuilt the full setup
(`X0, beta0, Kc, P, Q, G(beta0), RHS`) from scratch in `sympy` and
confirmed `S := (1+cosB)^2*X0 - RHS^2` factors as `(f-g)(f+g)` with
`f=(1+cosB)*sqrt(X0)`, `g=RHS` (trivial algebraic identity, `sympy`
residual `0`). On `C = {X0=cos^2B}`, substituting `sqrt(X0)->cosB`
(licensed by the already-established `cosB>0` fact) gives `f = (1+cosB)
cosB` exactly, so `f-g = (1+cosB)cosB - RHS = D1` by definition — own
`sympy` check confirms this difference is identically `0`. Confirmed
exactly as claimed; this is a one-line but genuinely exact (not numeric)
identity.

**`T1` radical-free factorization (New result 3) and the `Tgt` target
(New result 4).** Independently re-derived `dX0/dB = sinA*cosA/
(2*sin^2(A+B))` (matches the already-certified lemma exactly, `sympy`
residual `0`) and confirmed the claimed factorization
`T1 = (1+cosB)cosA/(2sin^2(A+B)) * [(1+cosB)sinA - 2sin^2B*sin(A+B)]`
holds exactly (`sympy.simplify` of the difference gives `0`, own fresh
session, not copied from the file's displayed algebra). The chain leading
to `Tgt := 4(1+cosB)^2*X0*D2^2 - T1^2` (via `2f*df/dB = d(f^2)/dB = T1`)
is definitionally correct — `T1` literally is `d(f^2)/dB` by
construction, so this step is essentially tautological once `T1`'s
closed form is accepted, and it correctly produces a fully radical-free
comparison target. No error found.

**Domain-connectedness / sign-determination lemma (New result 5).**
Checked the logical structure by hand: the argument that
`B_lo(A)` is a continuous function of `A` (via strict monotonicity of
`h_A(B) = X0(A,B) - cos^2B` in `B`, itself following from the already-
certified `dX0/dB > 0` plus the elementary `-d(cos^2B)/dB = 2 sinB cosB >
0`) is a standard, correctly-applied implicit-continuity argument;
concluding path-connectedness of the curvilinear-trapezoid region
`D`, and then that a continuous nonvanishing function on a connected set
has one constant sign (IVT), is sound elementary topology/real analysis.
No gap found in this device.

**Reduction Lemma (New result 1) — genuine simplification, confirmed
sound.** The claim that `f>=g` need only be proved on **all** of `D`
(not merely on the sub-region `{RHS>0}`), because the `RHS<=0` case is
already handled unconditionally by the pre-existing MVT lemma, is a
correct logical observation (checked against the cited parent lemma's own
stated scope) — this genuinely removes the previously-flagged open
target "prove `RHS>0` unconditionally" from the critical path, a real
(if modest) simplification of the route's roadmap.

**What remains unproved, correctly disclosed as such.** Both `Tgt(A,B)>0`
throughout `D` (hypothesis (A), strong numeric margin `~1.574`, `sympy`
symbolic collapse attempted and explicitly reported as incomplete due to
size, not falsely claimed proved) and `D1(A)>=0` on `C` (hypothesis (B),
inherited from the sibling, `~90%`-confirmed numerically) remain open. The
"Not yet promotable" note explicitly withholds `Tgt>0` itself from
certification — correct self-restraint.

**Net.** Real, verified progress: two new exact identities, a genuine
roadmap simplification eliminating a whole previously-open sub-target, and
a reusable connectedness/sign-determination device. The central numeric
gap (`Tgt>0`) is not closed. Status `partial` is accurate. **Verdict:
CHANGES REQUESTED.**

## 3. `coordinate-bash-resultant-boundary-pointwise-sos` — Theorem 2
(`angle B <= angle C` via `w=sqrt(1+u^2)`) and the point-localized SDP
infeasibility finding

**Theorem 2 (`w=sqrt(1+u^2)` polynomial encoding).** Independently
verified the underlying trig identity `sin(3t) = u(3-u^2)/w^3` (given
`u=tan(t)`, `w=sqrt(1+u^2)=sec(t)`, `t in (0,pi/2)`) both symbolically
(`sympy`: `3*u*w^2 - 4*u^3` reduces to `u(3-u^2)` exactly once `w^2` is
replaced by `1+u^2`, residual `0`) and numerically to 30-digit precision
(`mpmath`, 4 fresh sample points, agreement `< 1e-30` absolute at every
sample — far exceeding the claimed identity's needs). Then independently
built the full `n4 = w^3*cosB - u(3-u^2) >= 0 <=> angle B <= angle C`
equivalence directly from the raw trig definitions (own script, own
domain `A in (0,pi/2), B in (0,pi-A)`, no reuse of the file's `u,w`
machinery beyond the formula) and tested it at `375,037` fresh random
samples: **zero mismatches**. The proof's logical structure (`B<=C <=>
B<=pi/2-A/2`, both angles injective-`cos`-comparable on `(0,pi)` without
needing any extra `B<pi/2` precondition, unlike the population's other
`cos`-monotonicity lever) is correctly argued and, unlike a prior round's
sibling identity, genuinely does not need an extra hypothesis — checked
this claim explicitly by hand, it is right (both `B` and `pi/2-A/2` are
shown to lie in `(0,pi)` directly from `A in (0,pi/2]`, `B in (0,pi)`).
This is a fully rigorous, unconditionally-proved theorem — real progress,
closing the round-12-flagged prerequisite exactly as intended. Certified
`lemmas/angle-b-le-c-weierstrass-encoding.md` is warranted (the file's
own proposed content matches).

**Point-localized SDP infeasibility finding.** This is explicitly and
correctly disclosed throughout as a *numeric* finding (SDP solver output
at specific witness points), not a symbolic theorem — the file is careful
to state the logical asymmetry correctly ("infeasibility at one point
kills a global minimal-degree certificate; feasibility at one point proves
nothing globally"), which is logically sound reasoning about
Positivstellensatz certificates. Did not re-run the SDP solvers
independently (out of scope/time for this review — this is inherently a
numerical-optimization claim, not a symbolic one, and the file's own
"Watch out" items correctly flag the conditioning pitfalls it hit and
fixed). No overclaiming found: the file explicitly labels this section a
"diagnostic, not a proof," and does not attempt to elevate the
infeasibility finding into a claimed impossibility theorem for all
degrees — correct scoping.

**Net.** One new, fully rigorous theorem (Theorem 2) closing a genuine
prerequisite gap, plus a careful, honestly-scoped numeric SDP
investigation that narrows (without closing) the search for a
Positivstellensatz certificate. The central target (`Num >= 0` /
`(star)`) remains open. Status `partial` is accurate. **Verdict: CHANGES
REQUESTED.**

## Lemma certification decisions

- `lemmas/num-identity-exact-squaring-equivalence.md` — **CERTIFIED**
  (independently re-derived exactly, `sympy` residual `0`).
- `lemmas/parity-obstruction-q1-r0-certificate.md` — **CERTIFIED**
  (independently re-derived all graded components exactly matching the
  file's claims, and the elementary collapse argument checked by hand —
  sound). This is a genuinely new class of argument for this population
  and is correctly scoped: it proves a *necessary condition* on any
  certificate's multiplier structure, not that no certificate exists at
  all.
- `lemmas/f-minus-g-reduction-and-t1-factorization.md` (packaging
  Theorems 1-7 of the `-tangent` file) — **CERTIFIED**, restricted
  exactly as the file itself scopes it: Theorems 1-7 (all elementary/
  algebraic, independently `sympy`- or hand-confirmed) are certifiable;
  hypotheses (A) (`Tgt>0`) and (B) (`D1>=0` on `C`) are explicitly *not*
  part of the certified content, per the file's own "Status" section —
  this scoping is correct and should be preserved verbatim if written to
  `lemmas/`.
- `lemmas/angle-b-le-c-weierstrass-encoding.md` (Theorem 2 from `-sos`) —
  **CERTIFIED** (independently re-derived the trig identity and the full
  `B<=C <=> n4>=0` equivalence from scratch, `375,037`-sample zero-
  mismatch confirmation plus a symbolic proof of the underlying algebra).

All four certifications reflect genuinely independent re-derivations from
the raw definitions, not re-runs of any builder's script.

## Overclaim check

No file's Status header (`partial` in all three) overclaims relative to
what was actually established this round. No approach claims `solved`.
No approach invokes a crux-move reference in place of its own proof. No
skipped cases were found in any of the newly-added theorems. Every new
numeric-only claim is explicitly labeled as such (not conflated with a
proof) in all three files.

## current.md

Updated `results/imo-2026-02/current.md` with a new "Round 13 (this
round) — proof-reviewer adjudication" section at the top (Status remains
`partial`), preserving all prior rounds' history unchanged below it, per
the file contract in CLAUDE.md.

## Ranking

Recorded outcomes via `record_outcome` for all three built approaches this
round (see tool calls): `coordinate-bash-resultant-boundary` —
`advanced` (Num identity + B<pi/2 fix closed exactly as directed; new
parity-obstruction theorem proved); `coordinate-bash-resultant-boundary-
pointwise-tangent` — `advanced` (f-g reformulation eliminates the
RHS>0 sub-target, exact f-g|_C=D1 and T1 factorization proved, reduces to
one radical-free numeric target `Tgt>0`); `coordinate-bash-resultant-
boundary-pointwise-sos` — `advanced` (Theorem 2 closes the angle-B<=C
polynomial-encoding prerequisite; SDP infeasibility finding sharpened and
correctly, honestly scoped as numeric-only).

## Recommendation for next round

All three routes remain live and none is dead. The population is
converging on a common obstruction pattern across all three approaches:
each route's residual gap is now a *single* explicit polynomial/
trigonometric-polynomial positivity claim with strong numeric margin but
no symbolic proof (`-q1,-r0<0` for `coordinate-bash-resultant-boundary`;
`Tgt>0` for `-pointwise-tangent`; `Num>=0` via a 4-generator
Positivstellensatz for `-pointwise-sos`). This is the same shared-gap
pattern flagged in prior rounds' notes — worth having the outliner
consider whether a genuinely different framing (not just another
variation of "collapse to one polynomial inequality, try SOS/
Positivstellensatz on it") could break the plateau, per CLAUDE.md's
shared-gap-trap guidance, if this pattern persists another 2-3 rounds
without a symbolic closure.
