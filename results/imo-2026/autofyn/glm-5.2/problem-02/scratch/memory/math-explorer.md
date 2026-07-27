# math-explorer per-role rules

ALWAYS: check the rotation/sign conventions when numerically constructing a config from angle conditions — the theorem only holds on the valid interior branch; a wrong ray direction yields extraneous (non-interior) solutions that can falsely contradict the theorem (round 1, imo-2026-02).

ALWAYS: for "circumcentre of triangle XYZ, prove OP=OQ" geometry problems, try the antipode/homothety reduction first — if P,Q are images of B,C under a homothety from a vertex, OP=OQ may cleanly reduce to (antipode of that vertex) being equidistant from B,C (round 1, imo-2026-02).

NEVER: trust that the crux corpus has geometry — it does NOT (crux_moves_documentation.md explicitly says geometry is not yet extracted). For geometry analogues, query past_problems_database.json by keyword in `problem`/`solutions` instead (round 1, imo-2026-02).
