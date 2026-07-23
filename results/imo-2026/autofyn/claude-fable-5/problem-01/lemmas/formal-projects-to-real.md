# Lemma: formal-projects-to-real

**Statement.** Define a formal move like a real move but allowing chosen entries equal to 1.
A formal move either equals a real move or fixes the board multiset (a move touching a 1 sends
{1, y} to {1, y}). Hence formal reachability B ⇒* C implies real reachability B →* C.

**Proof.** Proved in full as Lemma 3 (§3) of `approaches/newman-confluence.md` (delete the
multiset-fixing steps from any formal path).

**Certified** by proof-reviewer, round 1. sorry-free; statement exactly as proved.
