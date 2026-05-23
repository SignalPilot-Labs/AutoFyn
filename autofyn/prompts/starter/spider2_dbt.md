Solve Spider 2.0 benchmark tasks. Spider 2.0 is a benchmark of ~600 real-world enterprise data workflows. Each task gives a natural-language question and a database (BigQuery, Snowflake, DuckDB, PostgreSQL, SQLite, or a dbt project). Produce SQL or dbt models that answer the question correctly.

## Evaluation Metrics

**EX (Execution Accuracy)** is the primary metric. The agent's query result set must match the gold result set exactly — same rows, same column values after normalization. This is NOT a string comparison of SQL text; the query can differ from gold as long as the result set matches.

**Exact Match (EM)** is the secondary metric for dbt tasks. The generated model's `schema.yml` (column names, types, test names) must match the gold schema exactly.

**How to run the eval harness:**
```
python eval/spider2_eval.py --pred outputs/<task_id>.sql --gold gold/<task_id>.sql --db <db_path>
```
Check `run_state.md` for the exact command this repo uses. If no eval harness is present, verify manually with `EXCEPT` queries:
```sql
-- Rows in agent output but NOT in gold (should return 0 rows):
(SELECT ... FROM result_table) EXCEPT (SELECT ... FROM gold_table);
-- Rows in gold but NOT in agent output (should return 0 rows):
(SELECT ... FROM gold_table) EXCEPT (SELECT ... FROM result_table);
```
Both directions must return 0 rows for EX = 1.0.

## Workflow for Each Task

1. Read the task description: identify the target database, the natural-language question, and any schema hints.
2. Dispatch `sql-analyst` to introspect the actual schema — never assume column names or types from the task description alone.
3. Write a candidate SQL query or dbt model.
4. Run it. Inspect the first 20 rows of output.
5. Run the eval harness (or EXCEPT comparison). If EX fails, read the gold output, identify the discrepancy row-by-row, and fix the query.
6. For dbt tasks: also run `dbt test --select model_name` to verify EM against `schema.yml`.
7. Repeat steps 3–6 until EX = 1.0 for the task.

## Common Failure Modes

- **Wrong aggregation granularity:** GROUP BY a column that should not be grouped, or missing a GROUP BY that is required. Compare the row count of your output against the gold row count first.
- **Dialect mismatch:** writing BigQuery syntax for a DuckDB task, or using PostgreSQL window functions in SQLite. Identify the dialect in step 1 and stay consistent.
- **Missing NULL handling:** nullable join keys in an INNER JOIN silently drop rows. Use LEFT JOIN with explicit NULL filtering, or add `IS NOT NULL` guards on the join key.
- **Hardcoded schema names:** table references that don't match the actual database. For dbt projects, always use `{{ source('schema', 'table') }}` and `{{ ref('model_name') }}`.
- **Off-by-one in date/time filters:** boundary conditions in `BETWEEN`, `>=`/`<=`, and `DATE_TRUNC` differ by dialect. Check the gold output's date range explicitly.

## Iterative Improvement

Fix one task at a time — do not attempt all tasks in one round. After EX = 1.0 for a task, mark it as done in `run_state.md` before moving to the next. Track progress as a count: `N of M tasks solved (EX = 1.0)`.
