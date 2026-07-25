## imo-2026-02 (route: `coordinate-bash-resultant-boundary`, CLARABEL/SDP conditioning lens)

### 1. Which 2 of 8 combos were inconclusive, and exactly why

From the approach file (`results/imo-2026-02/approaches/coordinate-bash-resultant-boundary.md`,
round-16 §3, lines 93-134): the joint Putinar/SDP escalation tested `-q_1` and
`-r_0`, bare and with two positive multipliers (`(1-\sigma)`,
`(1-\sigma)(1-\tau)`), at `\mathrm{maxdeg}\in\{6,8\}` for `-q_1` and
`\{7,9,11\}` for `-r_0` (six cases total, all cleanly `infeasible` under
CLARABEL) — **plus two more cases at `\mathrm{maxdeg}=10`**:
- `-q_1\cdot(1-\sigma)(1-\tau)` at `maxdeg=10`
- `-r_0\cdot(1-\sigma)` at `maxdeg=10`

These two were flagged **inconclusive** (not infeasible) because CLARABEL
"fails to converge on the larger problem size." I independently reproduced
this exactly: rebuilding the generator basis `\{1,\sigma,\tau,1-\sigma,
1-\tau,B_1,-B_2,B_4,B_6,B_{G_0E},B_{G_0N}\text{(corrected)},B_{EN}\}` from
the file's own displayed closed forms (own fresh `sympy`, own fresh `cvxpy`
session, `total_vars=911`, `n_eqs=977` — 12 PSD blocks of sizes
`231,120,120,120,120,10,10,6,6,6,6,3`), the plain **feasibility** SDP
(`minimize 0` subject to the Gram-matrix PSD + coefficient-matching
constraints) genuinely throws `Terminated with status = NumericalError` on
both flagged instances under CLARABEL — the file's diagnosis is confirmed
correct, this is a real solver failure, not a mislabeling. Verbose CLARABEL
output shows the classic signature: `dcost` diverges to `~3.9e5` while `μ`
collapses to `~3e-8` — the interior-point iterates are converging toward a
point on the boundary between feasible and infeasible (a **degenerate
self-dual-embedding** case), which is exactly the pathology a pure
`minimize 0` feasibility SDP is prone to near a true infeasibility boundary:
there is no interior point to certify strict infeasibility robustly, so the
solver's regularization can't resolve it in finite iterations. This is a
genuine numerical-conditioning issue (not primarily a "coefficient dynamic
range" issue — rescaling variables barely helped, see below), specifically
the **lack of a Slater point / near-degenerate feasibility boundary**
pathology.

### 2 & 3. Conditioning fix — tried for real, with a real updated result

**Rescaling alone (as in the `-sos` sibling's `n4→n4sq` affine trick) does
NOT fix it.** I mapped `(\sigma,\tau)\to(u,v)` via the exact affine
substitution `\sigma=0.2089+0.0521u,\ \tau=0.7056+0.0803v$ (centering the
domain box `\sigma\in[0.1568,0.2610],\tau\in[0.6253,0.7859]` to
`(u,v)\in[-1,1]^2`) — a legitimate technique since SOS-representability is
preserved exactly under invertible affine substitution (a square of an
affine image is still a square). Re-running the plain feasibility SDP in
`(u,v)`: the primal residual (`pres`) trajectory improves markedly (peaks
around `3e-2` instead of exploding), but CLARABEL **still** terminates with
`NumericalError` — rescaling alone is not sufficient here, because the
underlying issue is not really coefficient dynamic range but the
feasibility-boundary degeneracy itself.

**The fix that actually works: reformulate as a margin/robustness SDP,
not a pure feasibility SDP.** Instead of asking "does `\mathrm{target} =
\sum_i\sigma_iG_i` have a solution?" (degenerate at the boundary), I posed
the standard, better-conditioned equivalent: **maximize `t` subject to
`\mathrm{target}-t=\sum_i\sigma_iG_i`** (i.e. subtract a free scalar slack
from the target's constant coefficient and maximize it). This is a
textbook robustness reformulation for exactly this kind of
near-degenerate SDP feasibility problem, and it resolved both previously-
inconclusive instances **decisively and reproducibly**:

- `-q_1\cdot(1-\sigma)(1-\tau)`, `maxdeg=10`: CLARABEL gives `status=optimal`,
  `t^*=-0.16057325859936641` (raw coordinates). Rescaled `(u,v)` coordinates
  give `t^*\approx-0.15854934548463978` (matches to 2 significant digits,
  `status=optimal_inaccurate` but consistent). **Cross-solver validation
  with SCS** (`max_iters=50000,eps=1e-9`): `t^*\approx-0.1424`
  (`optimal_inaccurate`) — same sign, same order of magnitude.
- `-r_0\cdot(1-\sigma)`, `maxdeg=10`: CLARABEL gives `status=optimal`,
  `t^*=-0.1292696322013131`. SCS cross-check: `t^*\approx-0.1245`. Same
  sign, same order of magnitude.

**Both margins are comfortably negative (`\approx-0.13` to `-0.16`), far
from `0`** — not a borderline numeric-tolerance call. I independently
verified the CLARABEL solutions are genuine (not spurious non-PSD
artifacts, the exact SCS-artifact pitfall round 16 flagged): recomputed
every returned Gram matrix's minimum eigenvalue directly (own fresh
`numpy.linalg.eigvalsh`) — worst eigenvalue across all 12 blocks is
`\approx-1.5\times10^{-9}` for the `q_1` case and `\approx-1.7\times10^{-8}`
for the `r_0` case (i.e. PSD to numerical precision, not `-4.6` like the
caught SCS artifact), and the maximum equality-constraint (coefficient-
matching) violation is `\approx5\times10^{-10}$ and `\approx2\times10^{-10}`
respectively — both essentially exact.

**Degree escalation does not help either.** Re-running the same margin SDP
at `maxdeg=12` (two extra degrees of multiplier freedom) gives
`t^*=-0.16057328068\ldots` for `q_1` and `t^*=-0.12926962473\ldots` for
`r_0` — **identical to 9-10 significant digits versus `maxdeg=10`**. This
is a strong, degree-independent signature: the extra SOS-multiplier
freedom at `maxdeg=12` is not being used at all, i.e. this is not a
degree-truncation artifact — the obstruction appears to be a genuine
structural gap in this specific generator family, not something a higher
relaxation degree will close.

**Verdict: the two previously-inconclusive instances are now conclusively
INFEASIBLE**, resolving round 16's `6/8 infeasible, 2/8 inconclusive` into
`8/8 infeasible` (with comfortable margins, cross-solver-validated,
eigenvalue-verified, degree-escalation-checked). This completes and
strengthens the round-16 negative finding: **no Putinar/Lasserre
certificate for `-q_1` or `-r_0` exists in the generator family
`\{1,\sigma,\tau,1-\sigma,1-\tau,B_1,-B_2,B_4,B_6,B_{G_0E},B_{G_0N},
B_{EN}\}` at any of the eight tested degree/multiplier combinations** — the
LP and SDP techniques have now both been fully exhausted (not just
partially) on this generator family.

### 4. Should next round prioritize the case-split fallback?

**Yes, now more strongly than the file's own round-16 assessment.** Before
this round the negative evidence was "6/8 SDP-infeasible, 2/8
inconclusive" — leaving open the possibility that the 2 inconclusive cases
might turn out feasible and save the generator family. That possibility is
now closed: all 8 are infeasible, with the `maxdeg=10\to12` degree-
insensitivity suggesting the whole generator family (not just this
specific degree window) is fundamentally insufficient — consistent with
(and reinforcing) round 13's parity-obstruction theorem
(`lemmas/parity-obstruction-q1-r0-certificate.md`), which already proved
any certificate from this generator family needs a multiplier with an
explicit bare odd power of `c` or `d` (i.e. something genuinely outside the
"nice" `(0,0)`-graded product basis this round's LP/SDP search has
exhaustively covered). Given LP + phase-1 residual + SDP (now fully, not
partially, exhausted) have all failed, the two live options per the file's
own round-16 note are: (i) a genuinely new base generator beyond
`\{G_0,E_{\mathrm{num}},\mathrm{Num},\mathrm{Bc}\}`, or (ii) the
domain-aware case-split (Step 3). I'd prioritize (ii) first since it is
cheaper to attempt and the file's own round-16 scoping note already
identified the obstacle (no naive sign-pattern split works on `q_1` alone;
a working split needs the actual domain conditions
`G_0>0,E_{\mathrm{num}}<0,\mathrm{Bc}\ge0,\mathrm{Num}<0` region-by-region)
— but (i) should not be dismissed either, since the parity-obstruction
theorem gives a precise target (an odd-power-in-`c`-or-`d` multiplier) for
what a new generator would need to look like.

### Cheap-kill candidates
None obvious beyond what's already been tried on this route — the parity/
grading argument (round 13) is the sharpest structural pruning found so
far, and it's a necessary-condition result, not itself a proof.

### Knowledge-base entries to use
Whatever Positivstellensatz/SOS entries the outliner has already been
citing for this route (not re-surveyed this round — scope was the SDP
conditioning diagnostic specifically).

### Reusable artifact
Working, independently-built cvxpy/CLARABEL SDP harness (generator basis,
coefficient-matching constraint builder, affine-rescale option, and the
margin/robustness reformulation) at `/tmp/round-17/sdp_work/sdp_run.py` —
usable by a future round to test new generators or higher degrees quickly
without re-deriving the coefficient-matching machinery. Key lesson baked
into it: **always use the margin/robustness formulation
(`maximize t` s.t. `target - t \in` cone) instead of a pure feasibility
SDP** when a Putinar/Lasserre instance is near the feasibility boundary —
it is far better-conditioned and gave decisive, cross-solver-validated,
eigenvalue-verified answers where the pure feasibility SDP threw
`NumericalError` under CLARABEL on both solvers tried.

### Prior progress
As recorded in `current.md` round 16: this route has the sign-error-fixed
generator basis, LP infeasibility (with phase-1 residual non-artifact
check), and (as of this round) a now-complete 8/8 SDP infeasibility across
all previously-tested degree/multiplier combinations. Central target
(`-q_1<0,-r_0<0` Positivstellensatz certificate) still NOT found. Status
`partial`.

### Dead ends (do not retry)
- Raw Gröbner-basis ideal-membership test against the mixed generator set
  (round 15, confirmed structurally useless — the combined ideal trivially
  forces `s=t=0`, degenerate, "remainder 0" is meaningless for polynomials
  with zero constant term).
- Bare 3-generator (`B_1,B_4,B_6` only) linear ansatz at `q_1`'s own degree
  (round 14, confirmed overdetermined/infeasible).
- Rescaling alone (without the margin reformulation) does NOT fix the
  CLARABEL `NumericalError` on the two flagged instances — new finding
  this round, save future rounds the trouble of just re-trying rescaling.
- Degree escalation from `maxdeg=10\to12` does not change the margin at
  all (to 9+ significant digits) — new finding this round; further degree
  escalation within this generator family is unlikely to help either.

### Small-case / intuition notes (conjecture, not proof)
The near-identical negative margins at `maxdeg=10` and `12`
(`t^*\approx-0.1606` and `-0.1293` respectively for `q_1,r_0`, essentially
unchanged) is suggestive — though not proof — that this specific
generator family has a genuine, degree-independent obstruction to
representing `-q_1,-r_0`, reinforcing (numerically) the round-13 parity
theorem's qualitative prediction that a fundamentally different kind of
multiplier (with an odd power of `c` or `d`) is structurally required, not
just a higher-degree combination of the current generators.
