# Lemma L1 (θ = 90°: universal one-cut win) — CERTIFIED (round 1)

**Statement.** Let θ = 90°. From any triangle with no angle equal to 90°, Mulan has a legal cut after which BOTH children contain an angle of exactly 90°: label R a largest angle and P, Q the others (then P, Q < 90), attack R with t = 90 − P; the children are (P, 90 − P, 90) and (Q, R + P − 90, 90). Hence Mulan wins with at most 1 cut from any start.

**Proof.** Lemma 4.4 of `approaches/circle-group-quotient.md`; Lemma 3 of `approaches/residue-divisibility-characterization.md`. Legality: t > 0 ⟺ P < 90; t < R ⟺ Q < 90. Verified by simulation.
