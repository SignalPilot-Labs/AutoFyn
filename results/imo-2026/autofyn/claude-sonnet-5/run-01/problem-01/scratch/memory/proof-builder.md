# proof-builder role memory

ALWAYS: when an invariant is a product Π_p p^{e_p} over primes, the terminal/empty
case (all exponents 0, e.g. an all-1's board) evaluates to 1, NOT 0 — p^0=1 is
definitional. To get a contradiction against "collapse to all-1's" you must show
Γ(initial) > 1 strictly (via a prime factor of some initial entry >1), not ≥1.
(This was the exact arithmetic slip the outline-reviewer caught for imo-2026-01,
round 1.)

ALWAYS: prove multi-argument gcd Grouping/Subtraction lemmas via the universal
property (∗): for d≥1, d | gcd(a_1..a_r) ⟺ d | every a_i. This handles the
all-zero edge case (gcd(0..0)=0) uniformly and avoids hand-waving — cleaner than
size arguments. (imo-2026-01, round 1.)

ALWAYS: for gcd/lcm process problems, the p-adic valuation reformulation
(v_p(gcd)=min, v_p(lcm)=max, v_p(lcm/gcd)=|x-y|) decouples into independent
per-prime additive problems; the move becomes (x,y)↦(min,|x-y|), one Euclid
subtraction step, so gcd of exponents per prime is the natural invariant.
(imo-2026-01, round 1.)

NEVER: state a monovariant case split by relative size (e.g. "1<g<min(m,n)");
use exact boolean conditions (g=1 / g>1∧m=n / g>1∧m≠n). The size boundary is
false: m=4,n=8 has g=min(m,n)=4 yet lands in the "c unchanged" case.
(imo-2026-01, round 1.)

ALWAYS: when asked to produce a standalone .tex from an already-verified prose
proof, actually verify it compiles in this sandbox (no root/sudo, no apt,
no pdflatex preinstalled): download the `tectonic` static binary matching
`uname -m` from the GitHub releases API (aarch64 -> the
`aarch64-unknown-linux-musl` asset; x86_64 assets fail here via a
rosetta/gVisor mismatch even on an aarch64 host that reports x86_64 tools
exist) and run `tectonic file.tex --outdir <dir>`; it self-fetches the TeX
Live bundle over network on first run in ~1-2 min. This caught real overfull
\hbox issues (lines too wide) that pure visual proofreading missed.
(imo-2026-01 LaTeX transcription, round 1.)

NEVER: put `\tag{...}` inside a plain `\[ ... \]` displaymath block — amsmath's
\tag machinery requires an amsmath-aware numbered environment (`equation*`,
`align*`, etc.). Wrap any tagged formula (e.g. a named property like "(*)")
in `equation*` instead, or it will error at compile time.
(imo-2026-01 LaTeX transcription, round 1.)
