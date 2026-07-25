# Lemma L11 — Parity-vs-mean reformulation of an XOR-split residual

**Status:** CERTIFIED (proof-reviewer, round 4). Derived from certified L3; re-verified.
Source: induction-peel §3.3 (R1, R2). NOTE: this certifies the reformulation and the pointwise
sufficient condition ONLY — the general inequality (PM) is an OPEN gap, not certified.

**Setup.** Let B_low = Q_low ⊔ C with all parts ≤ H. Put D(t) := N_{Q_low}(t) − N_C(t).

**(R1) Reformulation.** Since N_{B_low} = N_{Q_low} + N_C ≡ N_{Q_low} − N_C = D (mod 2), the
odd-sets coincide, so by L3
  S(B_low) = meas{ t : N_{B_low}(t) odd } = ∫_0^∞ 1[D(t) odd] dt,
and by the L3 sum identity ∫_0^∞ N_X = sum(X),
  ∫_0^∞ D(t) dt = sum(Q_low) − sum(C).
Hence the residual "S(B_low) ≥ sum(Q_low) − sum(C)" is EXACTLY
  (PM)   ∫_0^∞ 1[D(t) odd] dt ≥ ∫_0^∞ D(t) dt.

**(R2) Pointwise sufficient condition.** If D(t) ≤ 1 for a.e. t, then (PM) holds.
**Proof.** For integer d put f(d) := 1[d odd] − d. If d ≤ 0 then 1[d odd] ≥ 0 and −d ≥ 0, so
f(d) ≥ 0; if d = 1 then f(1) = 1 − 1 = 0. Thus f(d) ≥ 0 for every integer d ≤ 1, so
D ≤ 1 a.e. ⟹ ∫ f(D) ≥ 0 ⟹ (PM). ∎

R2 covers every case N_{Q_low} ≤ N_C + 1, in particular the extremal family Q_low = C ⊔ {u}
(there D = 1[t<u] ∈ {0,1}). The general (PM) — compensating regions where D ≥ 2 — remains OPEN.
