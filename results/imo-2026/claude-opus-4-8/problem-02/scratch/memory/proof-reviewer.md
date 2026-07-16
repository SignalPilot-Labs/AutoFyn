# proof-reviewer role memory

ALWAYS: for complex/algebraic geometry bashes, the load-bearing gap is usually the geometry→algebra
TRANSLATION (angle condition → reality/algebra condition with correct orientation/signs), NOT the
final algebra. Verify the algebra symbolically (repro.py exact identities) AND check the translated
conditions hold across MULTIPLE valid configs (not one) — but a numerically-correct translation that
is only ASSERTED (not derived) still blocks `solved`. (imo-2026-02 round 1: complex approach's C2,C3
reality conditions were exact-verified but hand-derived → downgraded solved→partial.)

ALWAYS: the ranker `.autofyn/approach_ranker.py` tools are FastMCP-wrapped; call them from python via
`import approach_ranker as ar; ar.record_outcome(...)` (sys.path.insert the .autofyn dir). No CLI.
(round 1)

NEVER: approve `solved` when a key step is only numerically confirmed — the dispatch and CLAUDE.md
both require every translation step to be DERIVED. Numerical verification of an identity is not a
proof. (round 1)

ALWAYS: for complex/algebraic-bash geometry, after the geometry→algebra translation is fixed,
re-scrutinize the DEGENERATE-LOCUS removal (the "detA≠0 / by continuity" step). It is often
justified only at the single audited config ("nonzero at the audited value"), which does NOT
cover an arbitrary triangle — a real gap. Demand: prove the non-degeneracy for ALL admissible
configs, or a genericity argument on the full connected config manifold. (imo-2026-02 round 2:
complex approach §3 fully closed but detA=0 removal only per-audited-config → still partial.)

ALWAYS: a "detA=0 / by continuity" degenerate-locus gap in a complex-number bash can be closed
UNCONDITIONALLY by an exact real-slice ideal-membership certificate: if target TN and reality
conditions E_i are all purely imaginary (z-zbar), prove W*Im(TN) in (Im E_1,...,Im E_n) over the REAL
coordinates with W a product of GEOMETRIC non-degeneracies (|B-K|^2, Im(kbar l), Im(bbar c), ...),
none being detA. Reproduce it yourself: retype E_i/TN from the proof text, confirm Re==0, run
sp.groebner + sp.reduced and check target reconstructs EXACTLY as a combo of GB elements (remainder 0)
-- that is the rigorous certificate (sp.groebner returns a basis of the SAME ideal). Also verify each
W-factor is nonzero on every admissible config and the bidegree homogeneity that justifies WLOG B=1.
(imo-2026-02 round 2 v2: this closed the last gap -> SOLVED/APPROVE.)
NEVER: reject a Groebner ideal-membership certificate as "numerical" -- Buchberger reduction to
remainder 0 is EXACT symbolic; acceptable as rigorous PROVIDED you reproduce it and the multiplier W
is nonzero on all admissible configs (not a dense subset). (round 2)
