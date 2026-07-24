# Cubic locus for K (from hypotheses (i) and (iii), in the WLOG frame)

**Setup.** WLOG frame `B=(0,0), C=(1,0), A=(p,q)`, `K=(k1,k2)`, `L=(l1,l2)`.
Define, via the Dictionary Lemma (see `dictionary-lemma-equal-signed-angle.md`):
```
eq1 := cross(K−B,A−B)·dot(A−C,L−C) − cross(A−C,L−C)·dot(K−B,A−B)
eq3 := cross(L−C,K−C)·dot(B−M,K−M) − cross(B−M,K−M)·dot(L−C,K−C)
```
(the polynomial encodings of `∠KBA = ∠ACL` and `∠LCK = ∠BMK` respectively,
under one specific choice of matched vector pairing — see the caveat below).

**Statement.** `eq1 = 0` is linear jointly in `(l1,l2)`; solving it for `l2`
(valid away from the codimension-1 locus where the coefficient of `l2`
vanishes) and substituting into `eq3 = 0` and clearing the denominator gives
a polynomial `eq3_num(k1,k2,l1,p,q)`, linear in `l1`, which factors as
```
eq3_num = −(p²+q²)·(1 − l1)·X(k1,k2,p,q)
```
where X is an explicit irreducible (over ℚ(p,q)[k1,k2]) cubic in `(k1,k2)`.
The branch `l1 = 1` forces `l2 = 0` identically, i.e. `L = C`, a degenerate
configuration excluded by the problem's hypothesis that L lies strictly
inside triangle BNC. Hence, on every non-degenerate branch,
`X(k1,k2,p,q) = 0`.

**Independent verification.** Fully reproduced from scratch (independent
`sympy` computation, not copying the builder's script) by the round-1
proof-reviewer: eq1 matches the builder's expansion term-for-term; solving
eq1 for l2 and substituting into eq3 reproduces `eq3_num` exactly, and it
factors as `−(p²+q²)(l1−1)·X'` with `X' = −X` (same zero locus, sign
convention differs only by an overall −1, immaterial for `X=0`); substituting
`l1=1` into the solved `l2` collapses it to exactly 0, confirmed
symbolically. All of this algebra is independently confirmed correct.

**Caveat — RESOLVED (round 2, final pass).** The lemma's *geometric*
content — that this is really the locus of the problem's K — depends on
having chosen vector pairings in eq1, eq3 with rotational senses matching
the problem's containment hypotheses ("K lies inside angle LBA", etc.).
This matching is now proved in full: see `complex-number-argument-bash.md`
§3 (the "Master Fact" positive-combination/cone-sign toolkit), which shows
directly from the containment hypotheses (K∈△BMC, L∈△BNC, K∈∠LBA, L∈∠ACK)
that all three Dictionary-Lemma vector pairs used (including the ones in
eq1, eq3 above) have matching rotational sense at every valid configuration
of every triangle shape (q>0) — independently re-verified by the round-2
(final-pass) proof-reviewer.

**Status.** Certified as a correct algebraic fact about the equations eq1,
eq3 as explicitly defined above, AND certified as a correct geometric
statement about the problem's actual K — the orientation-matching caveat
is closed (see above).
