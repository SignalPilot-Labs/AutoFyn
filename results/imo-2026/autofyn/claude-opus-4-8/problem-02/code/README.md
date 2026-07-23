# Certificate verification — Opus 4.8, IMO 2026 P2

Makes the §6 polynomial certificate of `../current.md` independently re-runnable.

## Provenance

The run built its certificate in a sandbox `/tmp` and never committed the scripts, so the original archive had no `code/` directory: `current.md` and `../lemmas/T-reduction-and-certificate.md` asserted the identity `lc(P)·lc(Q)·TN = f·P + g·Q` without showing `f`, `g`, or preserving a checker.

`gb2_build.py` is recovered **verbatim** from `../logs.jsonl` — the run created it with a `cat > /tmp/gb2_build.py << 'PY'` heredoc at `2026-07-17T06:33:54Z` (proof-builder), and that Bash command is recorded in full. It is byte-for-byte the run's own builder, not a reimplementation.

`verify_certificate.py` is **not** from the run. It was written afterwards to re-run the checks and emit the cofactors, which the run computed but never printed.

## Files

- `gb2_build.py` — builds `TN`, `P`, `Q` from the geometry (recovered from the log)
- `verify_certificate.py` — rebuilds them, verifies both pseudo-division identities and the `R2 ≡ 0 (mod ρ)` reduction, and writes the cofactors
- `certificate_cofactors.txt` — explicit `f` (1058 terms) and `g` (840 terms), generated output

## Reproducing

```
python3 verify_certificate.py     # needs sympy; exits 0 iff certified
```

Independently reproduced, matching the values the run logged:

| Claim | Logged by run | Reproduced |
|---|---|---|
| `deg_t P`, `deg_s Q` | 4, 4 | 4, 4 |
| `lc(P,t)` | `-2*sin(A)*sin(th)*sin(C - th)` | same |
| `lc(Q,s)` | `-2*sin(A)*sin(th)*sin(A + C + th)` | same |
| identity (6.2) remainder | zero | zero |
| identity (6.3) remainder | zero | zero |
| `deg R2 (t,s)` | (3, 3) | (3, 3) |
| `R2` coeffs mod ρ | all zero | all zero |
| `lc(P)·lc(Q)·TN = f·P + g·Q` | asserted, cofactors never shown | verified, cofactors emitted |

`current.md` writes `lc(Q,s) = −2 sinA sinθ sin(B−θ)`; the builder yields `sin(A+C+θ)`. These agree under `sin(A+C+θ) = sin(B−θ)`, which `current.md` §5 states explicitly.
