# Proof Reviewer Rules

ALWAYS: Verify the key identity/lemma independently using Python computation before approving (because proofs can have subtle computational errors that look correct on paper, round 1)

ALWAYS: Check the gcd(k,0)=k convention explicitly when proofs involve p-adic valuations with zeros (because this convention is load-bearing for invariant arguments, round 1)

ALWAYS: Test the claimed invariant on concrete small examples with simulation before approving (because simulation catches errors that symbolic reasoning misses, round 1)
