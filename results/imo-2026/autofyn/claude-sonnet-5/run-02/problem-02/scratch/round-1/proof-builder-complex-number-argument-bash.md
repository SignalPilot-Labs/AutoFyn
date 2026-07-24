## Build report — complex-number-argument-bash, round 1

Status written to file: **partial**.

### What was done
Carried out the full symbolic coordinate bash announced by the outline
(WLOG frame B=(0,0), C=(1,0), A=(p,q); the "equal signed angle ⟺
cross·dot cross-multiplication" dictionary, proved from scratch via the sine
subtraction formula). Confirmed Lemma 0's target reduces in these
coordinates to the single scalar identity `O_x = p/2 + 1/4`.

Translated the three angle hypotheses into three polynomial equations
(eq1, eq2, eq3) in `(k1,k2,l1,l2; p,q)`. Eliminated `l2` linearly using eq1
(eq1 is genuinely linear in `l1,l2` jointly). Substituted into eq3: after
clearing denominators, eq3 factors exactly as
`eq3_num = -(p²+q²)(1-l1)·X(k1,k2,p,q)`, where `X` is an explicit irreducible
cubic (verified via `sympy.factor_list`). Showed `l1=1` is a spurious root
(forces `L=C` exactly, contradicting `L` interior to triangle `BNC`), so the
genuine constraint from (i)+(iii) is that **K is confined to the fixed cubic
curve `X(k1,k2,p,q)=0`, independent of L** — a real structural finding, not
previously identified by any explorer. eq2, after the same substitution, is
degree 2 in `l1` (quadratic residual pinning `l1` given K on the cubic).

### Where it stopped
Computed the circumcenter `O` of `A,K,L(k1,k2,l1)` via the standard formula
and cleared denominators to get the target polynomial `F_n(k1,k2,l1,p,q)`
that must vanish whenever `X=0` and `eq2_num=0`. Polynomial division of
`F_n` by `eq2_num` (in `l1`) leaves a nonzero remainder — a degree-5-in-
`(k1,k2)` expression I could not, within the time budget, show is a multiple
of `X` (which would close the ideal-membership argument). This is the
recorded open gap; I neither proved nor refuted it.

A second, independent open gap: I attempted to numerically re-verify the
Dictionary Lemma's rotational-sense/orientation matching against actual
containment-respecting `(K,L)` solutions (as the outline-reviewer required),
using a multi-start `fsolve` warm/cold search with barycentric containment
filters; it did not converge to any solutions passing all filters within the
time budget (consistent with the outline-reviewer's own report of this
difficulty). So the specific sign convention used to write eq1/eq2/eq3 is
unverified against the problem's actual orientation hypotheses, though the
algebra downstream of those equations (as literally stated) is correct.

### Promotable lemmas (see file for full statements)
- **Dictionary Lemma** (equal-signed-angle ⟺ cross·dot cross-multiplication),
  fully self-contained proof via sine subtraction — reusable by any other
  approach needing to convert an angle equality to polynomial form.
- **Lemma 0, coordinate form**: in the WLOG frame, `OM=ON ⟺ O_x = p/2+1/4`.
- **Cubic locus for K**: explicit irreducible cubic `X(k1,k2,p,q)=0`
  confining K, derived from hypotheses (i)+(iii) alone (independent of L,
  modulo the excluded degenerate branch). Flagged as depending on the still-
  unverified orientation convention.

File: `/home/agentuser/repo/results/imo-2026-02/approaches/complex-number-argument-bash.md`
