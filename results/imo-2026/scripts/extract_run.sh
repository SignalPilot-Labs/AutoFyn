#!/bin/bash
# Archive a completed olympiad-math run's full audit trail into
# results/imo-2026/<model>/problem-NN/. Proves the run was AI-generated with no
# human intervention by capturing all three artifact sources verbatim.
#
# Usage: extract_run.sh <run_uuid> <branch> <imo-slug> <abs_dest_problem_dir>
#   run_uuid  — the run's UUID (keys the DB tables and the rounds volume)
#   branch    — the run's branch_name on the target repo (github_repo from the run row)
#   imo-slug  — e.g. imo-2026-01; the run's custom_prompt must reference it
#   dest      — ABSOLUTE path to results/imo-2026/<model>/problem-NN (must exist,
#               with empty approaches/ lemmas/ scratch/ subdirs). Relative paths
#               break the cp block, which runs with cwd inside the clone.
#
# Three artifact sources (each derived, never guessed):
#   1. target git branch -> current.md, approaches/ (incl. hidden .ranking.json), lemmas/
#   2. Postgres (user+db both 'autofyn') -> logs.jsonl (run + audit_log + tool_calls, chronological)
#   3. autofyn_autofyn-rounds Docker volume, keyed by run UUID -> scratch/
#
# NOTE: the trailing secret scan uses grep, which exits 1 when it finds ZERO
# matches — the good outcome. With `set -e` that aborts the script at the very
# end AFTER all work is done. Treat a non-zero exit here as success if the
# preceding "scratch files" and "logs" lines printed; verify the scan count
# independently if unsure.
set -euo pipefail
RID="$1"; BRANCH="$2"; SLUG="$3"; DEST="$4"
REPO_ROOT=/Users/adibhasan/Downloads/projects/AutoFyn
WORK=/tmp/proval-$RID
EXPORT=/tmp/export-$RID
mkdir -p "$EXPORT"

echo "[$SLUG] === branch artifacts from tempcollab/proval @ $BRANCH ==="
rm -rf "$WORK"
git clone --no-checkout --depth 1 -b "$BRANCH" https://github.com/tempcollab/proval.git "$WORK" 2>&1 | tail -1
cd "$WORK"
git checkout HEAD -- "results/$SLUG" 2>&1
echo "[$SLUG] branch files:"; find "results/$SLUG" -type f | sort

cp "results/$SLUG/current.md" "$DEST/current.md"
cp -a "results/$SLUG/approaches/." "$DEST/approaches/"
cp -a "results/$SLUG/lemmas/." "$DEST/lemmas/"

echo "[$SLUG] === logs.jsonl from DB ==="
cd "$REPO_ROOT"
docker compose exec -T db psql -U autofyn -d autofyn -A -t -c \
"SELECT row_to_json(r) FROM (SELECT * FROM runs WHERE id='$RID') r;" > "$EXPORT/run.json" 2>/dev/null
docker compose exec -T db psql -U autofyn -d autofyn -A -t -c \
"SELECT json_agg(row_to_json(a) ORDER BY a.ts, a.id) FROM (SELECT id, run_id, ts, event_type, details, idempotency_key FROM audit_log WHERE run_id='$RID') a;" > "$EXPORT/audit.json" 2>/dev/null
docker compose exec -T db psql -U autofyn -d autofyn -A -t -c \
"SELECT json_agg(row_to_json(t) ORDER BY t.ts, t.id) FROM (SELECT id, run_id, ts, phase, tool_name, input_data, output_data, duration_ms, permitted, deny_reason, agent_role, tool_use_id, session_id, agent_id, idempotency_key FROM tool_calls WHERE run_id='$RID') t;" > "$EXPORT/tools.json" 2>/dev/null

RID="$RID" EXPORT="$EXPORT" DEST="$DEST" python3 - <<'PY'
import json, os
E=os.environ['EXPORT']; D=os.environ['DEST']
run=json.load(open(f'{E}/run.json')); audit=json.load(open(f'{E}/audit.json')); tools=json.load(open(f'{E}/tools.json'))
lines=[{"record_type":"run",**run}]+[{"record_type":"audit_log",**a} for a in audit]+[{"record_type":"tool_call",**t} for t in tools]
with open(f'{D}/logs.jsonl','w') as f:
    for o in lines: f.write(json.dumps(o,ensure_ascii=False,separators=(',',':'))+"\n")
for ln in open(f'{D}/logs.jsonl'): json.loads(ln)
print(f"[logs] {len(lines)} records (1 run + {len(audit)} audit + {len(tools)} tool_call), {os.path.getsize(f'{D}/logs.jsonl')} bytes")
PY

echo "[$SLUG] === scratch from autofyn-rounds volume ==="
docker run --rm -v autofyn_autofyn-rounds:/v -v "$DEST/scratch":/out alpine sh -c "
  if [ -d /v/$RID ]; then cp -a /v/$RID/. /out/; else echo 'NO SCRATCH DIR /v/$RID'; fi"
echo "[$SLUG] scratch files:"; find "$DEST/scratch" -type f | wc -l

echo "[$SLUG] === secret scan (whole dest) ==="
N=$(grep -raoiE "gh[pous]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-ant-[A-Za-z0-9-]{20,}|AKIA[0-9A-Z]{16}|xox[baprs]-|BEGIN (RSA|OPENSSH|EC|PGP) PRIVATE KEY|Bearer [A-Za-z0-9._-]{20,}" "$DEST" 2>/dev/null | wc -l | tr -d ' ')
echo "[$SLUG] secret matches: $N"
[ "$N" = "0" ] || { echo "!!! SECRETS FOUND in $SLUG — aborting"; exit 2; }
echo "[$SLUG] DONE"
