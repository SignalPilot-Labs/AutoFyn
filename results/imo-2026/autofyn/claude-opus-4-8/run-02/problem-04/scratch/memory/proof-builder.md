# proof-builder role memory

ALWAYS: for the Mulan triangle game (imo-2026-04), the sufficiency range-existence gap ("a cut
realizes a multiple of theta") is closed by cutting from the LARGEST-angle vertex: its two
orientation P-angle ranges (a,180-b) and (b,180-a) overlap because the middle angle <90, and
union to (a_min,180-a_min), which always contains a multiple of 180/n. This beats the 3-window
pigeonhole (round 1).

ALWAYS: necessity for that game is one uniform residue lemma (both-children-bad forces an
angle ≡0 mod θ or 180≡0), covering all θ∤180 at once — no 90-degree case split needed; the
non-obtuse invariant is only an optional independent check for θ>90 (round 1).
