---
description: "Use when the task involves a database, SQL queries, or dbt models. Covers schema introspection, connection setup, query execution, and dbt workflows."
---

# Database Schema & dbt Workflows

## Database Connection Patterns

Connect to the database using the appropriate client for the dialect:

- **PostgreSQL**: `psql $DATABASE_URL -c "SELECT ..."` or `psql -h host -U user -d db -c "..."`
- **SQLite**: `sqlite3 path/to/db.sqlite "SELECT ..."`
- **DuckDB**: `python -c "import duckdb; print(duckdb.sql('SELECT ...').df())"`
- **BigQuery**: check for service account JSON in env vars (`GOOGLE_APPLICATION_CREDENTIALS`) or mounted files; use `bq query --use_legacy_sql=false '...'`
- **Snowflake**: check for `SNOWFLAKE_ACCOUNT`, `SNOWFLAKE_USER`, `SNOWFLAKE_PASSWORD` env vars or `~/.snowsql/config`; use `snowsql -q '...'`


## Schema Introspection

List tables and inspect columns using dialect-specific queries:

**List all tables:**
- PostgreSQL/DuckDB: `SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'`
- SQLite: `SELECT name FROM sqlite_master WHERE type='table'`
- BigQuery: `SELECT table_name FROM <dataset>.INFORMATION_SCHEMA.TABLES`
- Snowflake: `SHOW TABLES IN SCHEMA <schema>`

**List columns for a table:**
- All dialects (except SQLite): `SELECT column_name, data_type, is_nullable FROM information_schema.columns WHERE table_name = '<table>'`
- SQLite: `.schema <table>` via the `sqlite3` CLI, or `PRAGMA table_info(<table>)`

**Row counts:**
```sql
SELECT COUNT(*) FROM <table>;
```

**For dbt projects:** run `dbt ls` to list all models, then read `models/**/*.yml` for `sources:` blocks and column definitions with tests.


## dbt Workflows

| Command | Purpose |
|---------|---------|
| `dbt ls` | List all models, sources, tests in the project |
| `dbt compile` | Render Jinja to plain SQL (output in `target/compiled/`) — syntax check only, no DB writes |
| `dbt run --select model_name` | Execute a specific model |
| `dbt test --select model_name` | Run data quality tests for a specific model |
| `dbt run --select tag:staging` | Run all models with a given tag |
| `dbt docs generate && dbt docs serve` | Browse lineage graph (only if interactive session) |

Connection settings are in `profiles.yml`, usually at `~/.dbt/profiles.yml`. The active profile is set by `profile:` in `dbt_project.yml`.

**Jinja reference syntax:**
- `{{ source('schema_name', 'table_name') }}` — reference a raw/external table declared in a `sources:` block
- `{{ ref('model_name') }}` — reference another dbt model; never hardcode schema-qualified table names
- Materializations: set `materialized: view` for staging models (`stg_*`), `materialized: table` or `materialized: incremental` for marts and aggregates


## Query Execution Workflow

1. **Introspect schema first** — never assume column names or data types; run the introspection queries above
2. **Write query, run it, inspect first 20 rows** — use `LIMIT 20` or equivalent
3. **Check for NULLs in join keys before joining** — `SELECT COUNT(*) FROM t WHERE join_key IS NULL`
4. **Use EXPLAIN to verify index usage** — `EXPLAIN (ANALYZE, BUFFERS) <query>` (PostgreSQL) or `EXPLAIN QUERY PLAN <query>` (SQLite/DuckDB); look for sequential scans on large tables
5. **Compare output shape against expected result** — row count, column names, sample values; fix mismatches before marking done
