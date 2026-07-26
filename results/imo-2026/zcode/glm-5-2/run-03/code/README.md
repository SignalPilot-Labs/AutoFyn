# Geometry problem — `OM = ON`

Computational support for the proof that, under the stated angle conditions on
`K` (inside `△BMC`) and `L` (inside `△BNC`), the circumcenter `O` of `△AKL`
satisfies `OM = ON` (`M`, `N` midpoints of `AB`, `AC`).

## Key result

In similarity-normalized coordinates `B=(0,0)`, `C=(2,0)`, `A=(2u,2v)`, with
`M=(u,v)`, `N=(u+1,v)` (so `MN` is horizontal and its perpendicular bisector is
`x = u + 1/2`), the proof reduces to the **ideal-membership statement**

```
P  ∈  ⟨F1, F2⟩  ⊂  ℝ[u, v, a, b, g],
```

where:
- `a = tan(∠KBA) = tan(∠ACL)`,
- `b = tan(∠LBK) = tan(∠LNC)`,
- `g = tan(∠LCK) = tan(∠BMK)`,
- `F1 = 0`  encodes `∠LBK = ∠LNC` (the `LBK = β` relation),
- `F2 = 0`  encodes `∠LCK = ∠BMK` (the `LCK = γ` relation),
- `P = 0`   is exactly the statement "`O` has x-coordinate `u + 1/2`".

`KBA = ACL = α` and `LNC = β` hold automatically from the construction of `K`, `L`,
so `F1`, `F2` are the only nontrivial constraints.

## Files

| file | role |
|------|------|
| `final_check.py`        | clean one-shot verification: builds `P,F1,F2`, divides, reports remainder `0`. **Start here.** |
| `genproof.py`           | derives `cond1 (=F1)`, `cond2 (=F2)`, `P`, and checks the remainder is zero. |
| `genfixed.py`           | builds the corrected symbolic `K, L` and the two conditions (sign-debugged against numerics). |
| `genfix.py`             | debug helper that fixed the `dNL` rotation direction. |
| `cert_final.py`         | writes the Gröbner-basis certificate `P = Σ qᵢ Gᵢ` to `certificate_full.txt`. |
| `get_Q1Q2.py`           | companion certificate generator (confirms the identity symbolically + numerically over 10 000 pts). |
| `certificate.txt`       | saved certificate (`P, F1, F2`, Gröbner basis `Gᵢ`, quotients `qᵢ`, verification record). |
| `certificate_full.txt`  | full human-readable certificate with the identity `P − Σ qᵢ Gᵢ = 0` to check by expansion. |
| `validate_final.py`     | validates `F1, F2` vanish to ~1e-15 on 9 independently-solved valid configurations (full geometric hypotheses enforced). |
| `debug_cond1b.py`       | filters solver output by the positional hypotheses (`K` inside `∠LBA`, `L` inside `∠ACK`) and checks `F1=F2=0` and `OM=ON`. |
| `numverify.py`          | broad numerical sweep: 40 random triangles, 33 valid solutions, max `|OM−ON| ≈ 1.8e-15`. |

## How to re-verify

```bash
python3 final_check.py      # reports: Remainder ... : ZERO
python3 cert_final.py       # rewrites the certificate; reports numerical max err 0.00e+00
python3 numverify.py        # broad numeric sanity check over random triangles
```

The identity `P = Σ_{i=0}^{7} qᵢ·Gᵢ` in `certificate_full.txt` is an exact
polynomial identity: a skeptic can verify it purely by expanding the right-hand
side and comparing with `P` term-by-term. Each `Gᵢ` is a Gröbner-basis element
of `⟨F1, F2⟩`, hence `Gᵢ = 0` whenever `F1 = F2 = 0`; therefore `P = 0` on the
solution locus, i.e. `O` lies on the perpendicular bisector of `MN`, i.e.
`OM = ON`.
