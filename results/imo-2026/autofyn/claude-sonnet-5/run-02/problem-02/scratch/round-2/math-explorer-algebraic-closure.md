## imo-2026-02 (lens: algebraic closure terrain)

### HEADLINE: Gap (a) — the final polynomial identity — IS CLOSED. Exact symbolic identity found via polynomial division in `l1` (not Gröbner/resultant). Gap (b) — orientation matching — gets strong numeric confirmation (a genuine containment-respecting solution was found with correctly matching signs).

### What actually works (concretely, sympy)

**Gröbner basis over the rational function field `QQ(p,q)`(k1,k2,l1) TIMED OUT** (`sympy.groebner` with `domain=FractionField(QQ,[p,q])`, `order='lex'`, ideal `(eq2_num, X)`) — killed after 5 min, does not terminate in reasonable time. **Do not use this route** — it's the wrong tool here (parametric-coefficient Gröbner bases are much slower than plain polynomial division/factoring).

**What DOES work and closes the gap: univariate polynomial division in `l1` + factoring.** Concretely:
1. Reproduced the whole derivation from scratch independently (own sympy script, not copied) — `eq1`, `eq3` expansions and the resulting cubic `X(k1,k2,p,q)` match the approach file's `X` **exactly** (verified `sympy.expand(mine - theirs) == 0`), and `l2 = l2(k1,k2,l1,p,q)` (solving `eq1=0`) matches too. So the approach's algebra through Step 2 is independently re-re-confirmed correct.
2. Built `eq2_num` (from hypothesis (ii), after substituting `l2`) — confirmed degree 2 in `l1`, total degree 6 in `(k1,k2)`, matching the approach file's claim.
3. Built the target numerator `Fn_num` = numerator of `O_x - (p/2+1/4)` after clearing the `l2`-substitution denominator (via the standard circumcenter formula for `A,K,L`) — degree 2 in `l1`, denominator `2·D²` where `D = k1p²-k1p-k1q²+2k2pq-k2q` (the same `D` from the Step-1 elimination).
4. **`sympy.div(Poly(Fn_num,l1), Poly(eq2_num,l1), l1)`** (plain univariate polynomial division treating `k1,k2,p,q` as coefficients) gives quotient degree 0 in `l1`, remainder `r1·l1 + r0` linear in `l1`. Division identity checked exactly (`Fn_num - quo*eq2_num - rem == 0` symbolically).
5. **Both `r1` and `r0`, when divided by `X`, give exact rational functions with a common denominator `(k1q - k2p + k2)`** (i.e. `r1 = X·P1/(k1q-k2p+k2)`, `r0 = X·P0/(k1q-k2p+k2)` for explicit polynomials `P1,P0`).
6. This was turned into a fully polynomial (denominator-free) identity: setting `D2 = -k1q+k2p-k2` (from the quotient's denominator) and `D = k1p²-k1p-k1q²+2k2pq-k2q`,
```
Fn_num · D2 · D  −  (q − k2) · eq2_num  =  D² · X · L(k1,k2,l1,p,q)
```
where `L = -2k1l1pq + k1l1q + k1p²q + k1pq - k1q³ - k1q + k2l1p² - k2l1p - k2l1q² - k2p² + 2k2pq² + k2p` (linear in `l1`). **This was verified as an EXACT symbolic polynomial identity**: `sympy.div` of the LHS by `D²·X` (as polynomials in `l1` over `ZZ[p,q,k1,k2]`) returns remainder exactly `Poly(0, l1, domain='ZZ[p,q,k1,k2]')` — this is not a numeric check, it's exact integer-coefficient polynomial arithmetic.

**Consequence:** whenever `X(k1,k2,p,q)=0` (K's cubic locus) AND `eq2_num(k1,k2,l1,p,q)=0` (hypothesis (ii)) hold, and `D2, D ≠ 0` (the same genericity conditions already used to eliminate `l2` — i.e. away from the codimension-1 degenerate locus already excluded in Step 1), then `Fn_num·D2·D = 0`, forcing `Fn_num = 0`, i.e. **`O_x = p/2 + 1/4` exactly**. **This closes gap (a) completely** — the target identity is proved to lie in the ideal `(eq2_num, X)` (localized away from `D·D2`), via an explicit, checkable cofactor identity, not an appeal to a black-box Gröbner computation. The identity above is short enough to state and verify directly in a written proof (a builder just needs to state the cofactor identity and note `sympy`/hand verification, or better, present it as "clearing denominators and expanding, one checks the polynomial identity ... holds" — this is exactly the kind of thing a human olympiad solution would present as a "brute force but exact" final computation).

The `D≠0` and `D2≠0` genericity conditions need a brief non-degeneracy argument (D≠0 is already required in Step 1 to solve for `l2`; D2≠0 should be checked doesn't correspond to another degenerate configuration — worth a quick check next round, but structurally this is the same kind of removable codimension-1 exceptional set as the `l1=1` branch already handled).

### Gap (b) — orientation/sign-matching — strong new numeric evidence it's fine

I ran a numeric root-find (`scipy.optimize.fsolve`) on a concrete triangle `A=(0.35,0.9), B=(0,0), C=(1,0)`, searching over `K` inside triangle `BMC` and `L` inside triangle `BNC` for solutions of `eq1=eq2=eq3=0` (exactly as defined in `complex-number-argument-bash.md`, i.e. with that specific vector-pairing choice). **Found one**: `K≈(0.1790,0.2390), L≈(0.6848,0.2514)`, residual `~1e-13`. For this solution I independently checked:
- Unsigned angle magnitudes: `∠KBA=0.27196..=∠ACL`, `∠LBK=0.57608..=∠LNC`, `∠LCK=0.39002..=∠BMK` — all three hypothesis angle-equalities hold to ~10 significant figures (confirms `eq1,eq2,eq3=0` really do encode the three angle equalities, not sign-flipped/supplementary versions).
- **Containment**: `K` lies inside angle `LBA` (ray `BK` between rays `BL,BA`) — **True**. `L` lies inside angle `ACK` — **True**. (Both checked via a signed-angle "between rays" test, not just eyeballing.)
- `K` inside triangle `BMC`, `L` inside triangle `BNC` — enforced in the search, both True.
- Target: `O_x = 0.42500...`, and `p/2+1/4 = 0.35/2+0.25 = 0.425` — **matches to full float precision**.
- `OM = 0.2618879731652...`, `ON = 0.2618879731654...` — equal to ~1e-9 (float/solver precision).

**This is strong (though numeric, not a proof) evidence that the specific vector pairings chosen in `complex-number-argument-bash.md` for eq1/eq2/eq3 are the geometrically correct ones** — a genuine problem-hypothesis-respecting configuration satisfies exactly those three polynomial equations with the correct sign convention, and the resulting O does land at the claimed target. This substantially de-risks gap (b): the round-1 worry that a numeric solver "did not converge to any valid solutions" appears to have been a search/robustness issue in that attempt, not a real sign-mismatch — a wider random search here found a valid point on the first structured attempt.

This is NOT a substitute for a synthetic/algebraic proof that the pairing is forced by the containment hypotheses (still needed for full rigor — a builder should give a clean argument, e.g. via the standard fact that "P inside angle XYZ" forces a specific ordering of the rays and hence a specific sign in the cross product, rather than relying on this one numeric witness), but it removes the doubt that the whole `eq1/eq2/eq3` setup might be systematically sign-flipped.

### Recommended next step for the outliner/builder

1. Fold the exact cofactor identity `Fn_num·D2·D − (q−k2)·eq2_num = D²·X·L` into `complex-number-argument-bash.md` as the closing computation for gap (a) — this is essentially proof-complete algebra now, just needs writing up (state the identity, note it's checked by expansion, handle the `D,D2≠0` genericity same way as the existing `l1=1` exclusion).
2. For gap (b), a builder should still write the short synthetic argument for why the containment hypotheses force the specific rotational-sense matching used (this is a genuine remaining proof obligation, just now de-risked numerically). Suggest: fix one global orientation (say ABC counterclockwise, `q>0` as already WLOG'd), then argue directly from "`K` inside angle `LBA`" etc. that each pair of vectors in the Dictionary Lemma applications has matched sign — this should be a short case-free argument once the correct pairing (now confirmed numerically) is written down.
3. Still open, but minor: confirm `D≠0, D2≠0` don't hide a real degenerate case that needs separate handling (structurally analogous to the already-handled `l1=1`/`L=C` branch).

### Knowledge-base / crux corpus
Not separately consulted this round (lens was purely computational/algebraic closure of an already-chosen approach); the relevant machinery (Dictionary Lemma, nine-point center reduction) is already certified in `lemmas/`. No new KB entries needed — this is direct polynomial-identity verification, standard technique, no named theorem beyond what's already cited.

### Dead ends / things NOT to retry
- **Gröbner basis over `QQ(p,q)` with `k1,k2,l1` as generators, lex order** — times out (>5 min, killed). If a builder wants a Gröbner-flavored writeup, compute it over `QQ` with `p,q` also as polynomial generators, or just use the direct division approach above (much faster, ~seconds, and already found the answer).
- Do not re-attempt "resultant of `Fn_num` and `eq2_num` w.r.t. `l1`" — it's not the right target (resultant only certifies "at least one common root," not "identity holds at both roots of the quadratic `eq2_num`"); the univariate-division approach used above is the correct one and it worked directly.

### Small-case / intuition notes
- (Conjecture, now very strongly supported both symbolically-exactly for gap (a) and numerically for gap (b)) The theorem is true and the `complex-number-argument-bash` reduction chain is fully correct, including the specific vector-pairing/orientation choice.
- The numeric witness configuration `A=(0.35,0.9),B=(0,0),C=(1,0),K≈(0.179,0.239),L≈(0.685,0.251)` is a genuine, containment-verified point of the problem's admissible family and can be reused by future rounds as a concrete sanity-check instance (e.g. to re-verify any rewritten proof step).
