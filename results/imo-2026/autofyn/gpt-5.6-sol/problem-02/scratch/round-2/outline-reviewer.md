## oblique-circle-linearization — APPROVE

This is a complete whole-problem route, and the new quadratic certificate addresses the sole gap recorded in round 1 rather than merely renaming it. Steps 1 and 3 may import the certified oriented-ray and oblique-circle lemmas. In Steps 2 and 4 the proposed mechanism is sufficiently concrete: eliminate each auxiliary angle separately to obtain independent quadratics in the positive ray lengths, then express the determinant target as the displayed linear combination of those quadratics. The certificate has the right degree pattern and passes a direct symbolic/numerical sanity check.

Builder obligations:
- Derive both equations `Q_t=0` and `Q_s=0` in prose from the midpoint ray equation and the corresponding closure equation; do not cite the explorer's computation.
- Audit the boxed certificate by displaying the coefficient comparison in `1,t,s,t^2,ts,s^2,t^2s,ts^2` (zero coefficients included or explicitly identified). “Direct expansion” or “CAS verifies” is not enough for this load-bearing identity.
- Fix the current file's malformed control characters and remove the empty `## Full proof` section while the status remains partial.
- Preserve the reflection statement, positivity/denominator arguments, and the nondegeneracy justification for `[K,L]`.

## trig-sine-factorization — APPROVE

The route is sound and end-to-end. The same low-degree certificate can replace the former unproved ideal-membership assertion, and the already certified second-intersection and directed-power steps then complete the theorem. The builder would need to derive `Q_t,Q_s`, explicitly identify the old equation (8) with the determinant polynomial `F` with the correct sign, and give the same complete coefficient audit required above.

This is not selected for the present build because, after Step 2, it is algebraically the same proof as `oblique-circle-linearization` with an additional second-intersection detour. Building both would duplicate the identical load-bearing calculation rather than diversify the field. In the head-to-head ranking, `oblique-circle-linearization` wins narrowly because its certified circle criterion reaches the conclusion directly and has fewer sign translations to verify.

## midpoint-cross-intersections — RETHINK

Steps 1–3 and 5–6 form a plausible whole-problem framework, but Step 4 is essentially the entire unsolved problem and has no established mechanism. The outline says to “identify” unspecified second common points/radical axes and, if that fails, try homotheties; it does not state the incidences or an angle/power chain that forces `BD=DV` and `CE=EU`. Numerical agreement with the midpoint theorem is not a proof, and a conjectural midpoint assertion cannot serve as a builder hand-off. The possible-parallel case is also deferred to projective handling without showing how the affine midpoint data survive.

Do not register or build this slug yet. A revised outline should first provide a precise directed-angle proof locating a named second common point, or a displayed sequence of power equalities that independently yields both midpoint identities, including extension and parallel cases. If that lemma is established, this would be valuable diversity from the algebraic field.

## inversion-fixed-collinearity — RETHINK

Steps 1–3 give an interesting and likely correct reformulation, but Step 4 is wholly conjectural. The assertion that the transformed angle conditions force `P,K',L'` collinear is supplied only with a hoped-for spiral similarity; no transformed-circle incidence, directed-angle chain, or scale identity is stated. Angle matching alone cannot determine the required similarity ratio, as the outline itself warns. The isosceles parallel case is likewise only a target, not a derived branch. Expanding inverse coordinates would recreate the already solved determinant wall and therefore would not rescue this as a distinct route.

Do not register or build this slug. Re-propose it only after giving a concrete transformed configuration that proves the collinearity (and separately the `b=c` parallel statement), with the relevant nondegeneracy and orientation cases identified.

## Field assessment and ranking

The two established approaches both advanced in round 1, but they share the same algebraic reduction. The new certificate now plausibly closes that shared gap, so the shortest direct representative should be built. The two proposed diversity routes do not yet have buildable load-bearing lemmas; the field therefore remains concentrated in one framing despite their conceptual novelty. No new approach was registered and no branch copy was justified. The stale round-1 entries were compared head-to-head, with `oblique-circle-linearization` ranked over `trig-sine-factorization` for its shorter certified finish.

build set: oblique-circle-linearization