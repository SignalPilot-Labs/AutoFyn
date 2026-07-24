# Round 21 proof-review — imo-2026-03

Three builds reviewed independently and adversarially. Overall problem
Status remains `partial` — only Claim (A) (`rank-pigeonhole-budget`,
round 8) is a fully closed top-level sub-target. No approach closes the
whole imo-2026-03 theorem this round.

## 1. greedy-halving-adversary — CHANGES REQUESTED (Status: partial)

**Claim under review:** Band-Parity Fact (new, general) + Theorem 35a'
closing the true epsilon-corrected target (Diamond') for Theorem 35a's
range v in [0,p3).

**Band-Parity Fact.** Re-derived by hand independently: for a sorted-descending
multiset with conventions r0=+inf, r_{k+1}=0, N_S(v)=j exactly on the band
v in [r_{j+1},r_j). This is a two-line consequence of the sorted order,
correctly proved, fully general (no ladder structure). The "parity flip
under prepending a dominant element" corollary is also correct (consecutive
integers have opposite parity). **CERTIFIED** — see
`lemmas/band-parity-fact.md`.

**Theorem 35a', sub-range 1 (v in [0,s'], unconditional).** I re-derived the
whole algebraic chain independently by hand:
- eps(v) = 1 - eps'(v) via the Band-Parity corollary (M=p3, S=T').
- Xi = A(T')-2A(T'_{>v}) >= v-s'-2v*eps'(v) via the certified
  `truncated-alternating-sum-floor` lemma.
- Substituting into Delta(n,v)=-p3-Xi and the target (Diamond'), the
  2v*eps'(v) terms cancel identically, reducing the whole claim to
  f(n) <= p3-s', which is an *equality*, established via Lemma 24
  (f(n)+s=p2) and the doubling identity p2=2p3.
This matches the file's derivation term-for-term. I additionally wrote a
fresh exact-`Fraction` script (using per-piece-legal refinements, not a
lumped composition — per the standing ALWAYS rule about per-piece testing)
and ran 7500 trials across n=3..7: **zero violations**. Sub-range 1 is
solid, unconditional, correctly proved. No overclaim.

**Theorem 35a', sub-range 2 (v in (s',p3), conditional on IH).** The
reduction to A(T') >= v-s' (and the observation that A(T')>=f(n) is a
strictly stronger sufficient bound, since v-s'<f(n) in this sub-range) is
correct and cleanly derived. The file cites this stronger bound as
"exactly what Theorem 35b proves: A(T') >= f(n)*2^{n-3} >= f(n)."

**Bug found (real, non-fatal).** I independently re-derived Theorem 35b's
own "cross-level identity" step and found a genuine algebra error: it
claims $D_{n-3}\cdot f(n-3) = 2^{n-3}$, computed by substituting
$f(n-3) = 2^{n-3}/D_{n-3}$ — but by the file's own standing definition
(rule 26 of project memory, confirmed throughout this file, e.g. line 1636)
$f(m) := 1/D_m$ (the "unit," NOT the game value $c(m)=2^m/D_m$). So
$D_{n-3}\cdot f(n-3) = 1$ identically — a trivial fact, needing no
"cross-level identity" at all — and Theorem 35b's stated conclusion
$A(T') \ge f(n)\cdot 2^{n-3}$ is **false as written** for $n\ge4$. I
constructed an explicit counterexample confirming this: at $n=4$, the
untouched tail $T'=\{p_4,p_5\}$ (budget 0, the base/extremal case) gives
$A(T')=1/31=f(4)$ exactly, strictly less than the claimed bound
$f(4)\cdot2^{4-3}=2/31$. I verified this both by hand and by an exact-
`Fraction` script over legal per-piece refinements.

**Why this is non-fatal.** The actually-needed weaker fact, $A(T')\ge f(n)$
(no bonus factor), is correctly implied by $(\star_{n-3})$ via the trivial
identity $D_{n-3}f(n-3)=1$ (no "cross-level identity" needed), and I
verified numerically (5000+ trials, per-piece-legal refinements, n=3..8)
that it holds robustly (tight at budget 0, the base case, and never
violated at any tested higher budget). This is exactly the bound both
Theorem 35b's own use (deriving Delta(n,v)<=v-f(n) at v=p3) and Theorem
35a''s sub-range 2 actually consume — so the final conclusions of both
Theorem 35b and Theorem 35a' survive, just via a currently-buggy
intermediate step that must be corrected (drop the false "2^{n-3}" factor)
before the derivation can be called fully rigorous. This is the same
"flagged-but-non-fatal" pattern this project has seen before (rules 6, 30
in project memory) — a real defect, not a fatal one, and it must be fixed
before Theorem 35b is reused again without caveat.

**Scope discipline.** The file explicitly and correctly leaves "step 4"
(Theorem 35b's own range v>=p3) and "step 6" (Theorem 36's Case (b), p3
cut) open, exactly as instructed by this round's dispatch — no oversell
found there. The one "unverified observation" about step 4 is explicitly
flagged as not relied upon or claimed established, which is honest.

**Verdict:** CHANGES REQUESTED. Real, verified progress (Band-Parity Fact,
sub-range 1 fully closed unconditional). Gap to close next round: fix
Theorem 35b's algebra bug (trivial fix — replace the false "2^{n-3}"
derivation with the correct D_{n-3}f(n-3)=1 identity, conclusion becomes
A(T')>=f(n), which is all that's ever used downstream), then proceed to
steps 4/6.

## 2. rank-pigeonhole-budget — APPROVE (Status: solved, correctly scoped
to Claim (A); new §7.5 content independently re-verified, no bugs)

**Claim (A) itself.** Already APPROVEd round 8 (achievability + Case I +
Case II, full closure for every n). Untouched this round. The file's own
`## Status: solved` header is explicitly and correctly scoped: "this
approach's own target, Claim (A) ... Claim (B) ... and the general upper
bound are proved by sibling approaches and are outside this file's scope."
This scoping language is accurate — I did not find it overclaiming the
whole imo-2026-03 problem.

**New §7.5 closure of the TRUE (♯') target at n=3.** I independently
re-derived the middle-band algebra from scratch: with $p_3=2p_4$, $p_2=4p_4$,
$s=3p_4$, the middle band $v_2\in[p_4,p_3)$ gives
$\Delta(3,v_2)=A(\tau)-2A(\{p_3\})=p_4-4p_4=-3p_4$ (constant), and the true
target $(\sharp')$ with $\varepsilon(v_2)=1$ reduces exactly to
$v_1+v_2\le6p_4$, which follows by summing the two strict domain bounds
$v_1<p_2=4p_4$ and $v_2<p_3=2p_4$ termwise. I confirmed this matches the
file's derivation exactly and wrote a fresh, independent exact-`Fraction`
script sampling the *full* domain ($v_1\in(s,p_2)$, $v_2\in(p_2-v_1,s)$,
using the true $\varepsilon$-corrected target, not the weaker $(\sharp)$):
**200,000 trials, zero violations.** The Band-Parity Fact's use to locate
$\varepsilon(v_2)=1$ exactly on the interior band (and $=0$ on both outer
bands, matching the pre-existing 3-case split) is correctly applied. No
bugs found in this closure — unlike the sibling's Theorem 35b this round.
The round-19/20 boundary-relabeling fix (v2=p4 case) is also correctly
folded in.

**§7.6 (general n>=4).** Honestly left open. The file correctly diagnoses
that the multi-piece polytope re-encounters the project's central
cross-piece tie-vertex enumeration obstruction when adapting
`exchange-smoothing-vertex-maximization`, and does not claim closure — this
is presented as a valuable convergence finding, not a closure, and the
"Open gaps" section correctly states "None remaining for this approach's
own target, Claim (A)" while separately noting the §7.6 addendum "does not
affect Claim A's status."

**Verdict:** APPROVE (for Claim (A), the approach's own scoped target,
which remains fully closed and correctly labeled). The new §7.5 result is
additional, independently-verified, bug-free progress on the (unrelated
to Claim A) middle-band target, correctly not conflated with a broader
"solved" claim.

## 3. lp-duality-certificate — CHANGES REQUESTED (Status: partial)

**Claim under review:** Within-Chamber Affinity Theorem (conditional on
M(tau) invertibility) + companion singular-case proposition, for case (b2).

**Note on labeling.** The relevant content is headed "Round 20 build" in
the approach file, but the git diff confirms this ~370-line section was
added fresh this round (round 21) — the internal round-number label is
stale/mislabeled (should say "Round 21"). This is a cosmetic
documentation issue, not a correctness issue, but should be fixed by the
builder next round to avoid confusing future readers about when this work
was actually done.

**Linear-system derivation.** I independently re-derived the row structure
of $(\dagger)$: for each tied piece $i\in I$, the mass-conservation row
$q_iv_i+\sum_{j\in I}n_{ij}v_j=p_i-\sum_{j\notin I}n_{ij}p_j$ has
coefficients $q_i,n_{ij}$ that are pure slot/pin-target counts — determined
entirely by the combinatorial type $\tau$, never by the numeric value of
$p$ — while the right-hand side is manifestly linear (homogeneous) in $p$.
This is exactly the "mass conservation rows are p-linear, tie/pin rows are
p-independent" structure the dispatch asked me to check, and it holds:
$M(\tau)$'s entries are counts (type-dependent, $p$-independent), and
$L(p)=Np$ for a fixed count-matrix $N$. The resolution-cycle argument
(every pin target resolves after finitely many hops to a constant, a
forced $p_j$, or a genuine tied unknown $v_j$) is a standard finite
dependency-graph argument and is correctly handled.

**Within-Chamber Affinity Theorem.** Given $M(\tau)$ invertible, the unique
solution $\mathbf v(p)=M(\tau)^{-1}Np$ is manifestly linear in $p$ (fixed
matrix times $p$), hence every slot value and $\Phi_{\min}(p)=T(p)-E(F^*(p))$
is linear in $p$ on the chamber. This is standard LP/linear-algebra
reasoning (a basic-feasible-solution depends affinely on the RHS when the
basis matrix is fixed and invertible), correctly executed with no gaps.

**Singular-case proposition.** The two-way dichotomy (some $\phi_rN\ne0$
forces $U$ into a proper hyperplane, hence empty interior / not a genuine
chamber; or all $\phi_rN\equiv0$, the honestly-flagged unresolved residual
case) is a standard range/null-space argument, correctly executed. The file
is explicit that case (ii) is *not* ruled out in general, only reduced to a
finite per-type check — no overclaim.

**Scoping.** The file is explicit and consistent throughout ("Current best"
section, "Approaches tried" entry, and the "Net honest assessment"-style
prose) that case (b2) itself remains open: affinity is necessary
infrastructure only, the extreme-point evaluation against $a_nT$ (the
outline's own identified "actual work") has not been attempted, and the
chamber-count growth signal ($\approx28\%\to64\%$ from $n=3$ to $n=4$) is
reported honestly as an amber flag, not glossed over or spun positively.

**Verdict:** CHANGES REQUESTED. Real, sound, independently-verified new
general machinery (conditional affinity theorem + singular-case
dichotomy), correctly scoped as infrastructure, not a closure. No overclaim
found. Gap to close next round: extend past the necessary-condition
affinity theorem to an actual finite extreme-point evaluation (step 4 of
the outline, the piece the file itself identifies as the real remaining
work), and address whether the chamber-growth signal threatens tractability
of that evaluation for general n.

## Promotable lemmas — certification decisions

- **Band-Parity Fact** (`greedy-halving-adversary`) — **CERTIFIED**, see
  `lemmas/band-parity-fact.md`. General, self-contained, correctly proved,
  already independently reused (and independently verified) by the sibling
  approach this same round.
- **Theorem 35a'** — **NOT independently certified as a standalone lemma
  file this round.** Its sub-range 1 closure is solid and unconditional,
  but its sub-range 2 closure currently cites Theorem 35b's buggy
  derivation (see above); recommend certifying only after Theorem 35b's
  algebra is corrected. Noted in `current.md`, not written as a separate
  lemma file to avoid certifying a citation chain with a known unfixed
  defect.
- **Within-Chamber Affinity Theorem + singular-case proposition**
  (`lp-duality-certificate`) — **CERTIFIED**, see
  `lemmas/within-chamber-affinity-theorem.md`. Sound conditional theorem,
  correctly scoped, independently re-derived and confirmed with no gaps.
- **n=3 middle-band closure (§7.5/§7.5.2)** (`rank-pigeonhole-budget`) — a
  fully re-verified, bug-free, concrete instance (not yet abstracted into a
  standalone reusable general lemma by the builder itself, which correctly
  says so — "supersedes the round-19/20 (♯)-only version as a concrete
  instance, not yet a standalone general lemma"). No separate lemma file
  needed this round per the builder's own honest framing; recorded in
  `current.md` instead.

## current.md

Updated: appended a new "Round 21" bullet under `## Approaches tried`
summarizing all three builds' verified content and the Theorem 35b bug
finding, consistent with the combined true state (`## Status` remains
`partial` for the whole problem; Claim (A) remains the only closed
top-level sub-target). No change to `## Full proof` (still absent, Status
partial).

## Summary of verdicts

| Approach | Verdict | True Status |
|---|---|---|
| greedy-halving-adversary | CHANGES REQUESTED | partial |
| rank-pigeonhole-budget | APPROVE | solved (Claim A only, correctly scoped) |
| lp-duality-certificate | CHANGES REQUESTED | partial |

No RETHINK this round — all three approaches made genuine, independently
verified progress with no fatal errors. One real (non-fatal) bug found and
flagged (Theorem 35b's algebra error, inherited by this round's Theorem
35a'), consistent with this project's established pattern of catching
non-fatal-but-real defects before they compound.
