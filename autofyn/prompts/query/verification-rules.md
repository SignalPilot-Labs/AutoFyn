## Verification

Before considering work done, run:
1. **Typechecker** — `pyright` for Python, `tsc --noEmit` for TypeScript.
2. **Linter** — `ruff check` for Python, `eslint` for JS/TS if configured.
3. **Tests** — `pytest tests/fast/` for backend. If frontend tests exist (`vitest.config.*` or `jest.config.*`), run those too.
4. **Goal eval** — Run the eval command from run_state.md's Concrete Target. Compare against the last Eval History entry. Report the delta.
5. **SQL/dbt** — if the task modified dbt models or SQL files: run `dbt compile` to check syntax, `dbt test` for data quality. If `sqlfluff` is configured (check `setup.cfg` or `.sqlfluff`), run `sqlfluff lint <path>`. Compare eval results against the baseline in run_state.md Eval History.
