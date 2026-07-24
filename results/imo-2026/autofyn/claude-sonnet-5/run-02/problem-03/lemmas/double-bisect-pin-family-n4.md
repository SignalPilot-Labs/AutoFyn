# Theorem: Double-Bisect-Pin Chamber Family at $n=4$

**Source:** `approaches/lp-duality-certificate.md`, round 29, §R29.4.
**Certification status:** proposed this round — pending proof-reviewer
certification.

## Statement

Fix a 5-piece marking $p_1\ge p_2\ge p_3\ge p_4\ge p_5>0$, $T=\sum p_i$.
For any 2 distinct indices $i,j\in\{1,\dots,5\}$ (the "bisected" pair) and
any 2 distinct indices $k,l\in\{1,\dots,5\}\setminus\{i,j\}$ with $k<l$
(so $p_k\ge p_l$, automatic from the sorted order), let $r$ be the unique
remaining index. The response "bisect $p_i,p_j$; cut $p_k$ into
$(p_l,\,p_k-p_l)$; leave $p_l,p_r$ untouched" is legal (uses exactly $3$
cuts $\le n=4$), and
$$\Phi_{i,j;k,l}(p)\ =\ \frac{T+|p_k-p_l-p_r|}{2}.$$

There are $\binom52\cdot\binom32=10\times3=30$ such chambers.

## Proof

The fragment multiset is
$\{p_i/2,p_i/2\}\cup\{p_j/2,p_j/2\}\cup\{p_l,\,p_k-p_l\}\cup\{p_l\}\cup\{p_r\}$,
total mass $T$. Writing $M=\{p_k-p_l,\,p_r\}$ and applying the certified
`pair-insensitivity-corollary` (iterated form, 3 applications: once each
for the values $p_i/2$, $p_j/2$, $p_l$ — each occurring exactly twice in
the full multiset), $A(\text{full multiset})=A(M)$. Since $M$ has exactly
2 elements, $A(M)=|p_k-p_l-p_r|$ directly. Hence
$\Phi=(T+A(M))/2=(T+|p_k-p_l-p_r|)/2$.

Feasibility ($p_k\ge p_l$) is automatic from $k<l$ in the sorted marking.
Legality (cut budget) holds since exactly 3 cuts are used, $\le n=4$.

## Verification

Independently checked (exact `Fraction`, `/tmp/round-29/verify_pin_formulas.py`):
3 representative instances of the formula, $5000$ random trials each
($15000$ total), against a direct sort-and-alternate-sum computation on
the un-reduced fragment multiset — zero mismatches. The general indexed
formula was also exercised across tens of thousands of further instances
inside the coverage-measurement scripts (`/tmp/round-29/coverage_n4_extra.py`,
`/tmp/round-29/find_pin_witnesses.py`, `/tmp/round-29/coverage_named33_exact.py`)
with no discrepancy against direct computation.

## Discussion / provenance

Discovered by the standing project technique (round 27's rule): running
an exhaustive search over a natural chamber shape ("bisect 2, pin 1,
leave 1 untouched" — the predicted "Quad-Pin" analog of $n=3$'s
Bisect1+Pin2to3 chamber, one index up) against the specific points left
uncovered by the `bisect-subset-lemma` family alone (measured at
$\approx93\%$ coverage of the residual box $p_1<T/2$, $T/31<p_2<8T/31$),
then reverse-engineering and proving the closed form.

Combined with the 30 `bisect-subset-lemma` chambers at $m=5$, this
60-chamber family covers $100\%$ of $30{,}000$ fresh exact-`Fraction`
random trials in the residual box (`/tmp/round-29/coverage_named33_exact.py`)
— strong empirical evidence, **not yet a proof**, that it closes the
$n=4$ upper bound's remaining open territory. A Farkas-style exhaustive
covering argument (proving no marking in the residual defeats all 60
chambers simultaneously) has not yet been derived — that is the next
open step, flagged explicitly in the approach file (§R29.5).

## Open generalization (not proved, flagged only)

The mechanism plausibly generalizes to any $m$: "bisect $m-3$ pieces, pin
1 of the remaining 3 pieces to another, leave the last untouched" would
use $m-2$ cuts, within budget $n=m-1$ (1 spare cut). This round only
proves and verifies the $m=5$ instance; general-$m$ is an open
generalization, not claimed here.

## Certification

**Certified (round 29).** The theorem statement above (the exact
closed-form identity $\Phi_{i,j;k,l}(p)=(T+|p_k-p_l-p_r|)/2$ for the
described legal response, and the count of 30 chambers) is proved in
full and gap-free — reviewer independently re-derived and re-verified it
from scratch (fresh exact-`Fraction` script, 20,000 random trials, zero
mismatches). Certification covers only this identity, not the separate
"100% empirical coverage of $\mathcal R$" claim in the approach file,
which remains explicitly unproved (no Farkas-style argument yet) and is
not part of what is certified here.
