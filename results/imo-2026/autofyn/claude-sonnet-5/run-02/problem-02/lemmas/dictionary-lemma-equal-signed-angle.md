# Dictionary Lemma: equal-signed-angle ⇔ cross/dot polynomial identity

**Statement.** For nonzero planar vectors u, v, w, z, write
`cross(u,v) = u_x v_y − u_y v_x`, `dot(u,v) = u_x v_x + u_y v_y`. Let θ1 be
the angle from u to v measured in a fixed rotational sense, θ2 the angle
from w to z measured in the *same* rotational sense, both in (0, π). Then
```
cross(u,v)·dot(w,z) − cross(w,z)·dot(u,v) = |u||v||w||z|·sin(θ1 − θ2),
```
and consequently, given θ1, θ2 ∈ (0,π) measured in a matched rotational
sense,
```
cross(u,v)·dot(w,z) = cross(w,z)·dot(u,v)   ⟺   θ1 = θ2.
```

**Proof.** Writing u, v, w, z in polar form relative to the fixed sense
(`cross(u,v) = |u||v| sin θ1`, `dot(u,v) = |u||v| cos θ1`, and likewise for
w, z with θ2), the left side becomes
`|u||v||w||z| (sin θ1 cos θ2 − cos θ1 sin θ2) = |u||v||w||z| sin(θ1 − θ2)`
by the sine subtraction formula. For the equivalence: if the polynomial
identity holds, `sin(θ1−θ2) = 0` (since all four magnitudes are nonzero), so
`θ1 − θ2 ∈ {0, ±π, ...}`; since θ1, θ2 ∈ (0,π), their difference lies in
(−π,π), forcing θ1 = θ2 unless one of θ1, θ2 equals a boundary value which
is excluded by hypothesis. The converse (θ1=θ2 ⟹ the polynomial identity)
is immediate. ∎

**Independent verification.** Re-derived and numerically spot-checked
(general base angles a0, b0, random magnitudes and angle differences,
5 random trials, residual 0 to machine precision) by the round-1
proof-reviewer.

**Caveat (not part of the lemma, a usage note).** Applying this dictionary
to convert a *geometric* angle-equality hypothesis (e.g. "∠KBA = ∠ACL") into
the polynomial equation requires an independent argument that the chosen
vector pairs (u,v) and (w,z) are measured in a *matched* rotational sense —
this must come from the problem's containment/orientation hypotheses (e.g.
"K lies inside angle LBA") and is NOT automatic from the angle equality
alone. Each application of this lemma to the problem's hypotheses (i)-(iii)
still needs this matching verified separately.

**Status.** Fully proved and independently verified. Certified for shared
reuse. Any approach using it to encode angle hypotheses (i)-(iii) as
polynomial equations must still separately verify the matched-rotational-
sense caveat above.
