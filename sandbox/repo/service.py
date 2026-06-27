"""RepoService — all git/gh operations for the sandbox repo lifecycle.

One instance per sandbox, stored on the aiohttp app. Endpoints call
public methods; the service owns git state (RepoState) and all
subprocess interactions via shared.subprocess helpers.

Lifecycle: bootstrap → (save per round) → teardown.
"""

import contextlib
import logging
import os
import uuid
from collections.abc import AsyncIterator

from aiohttp import web

from constants import (
    AUTO_COMMIT_MESSAGE,
    CLONE_TMP_DIR,
    CMD_TIMEOUT,
    DIFF_FILE_BODY_MAX_CHARS,
    DIFF_TMP_INDEX_PREFIX,
    GH_NO_DIFF_MARKER,
    GIT_CLONE_DEPTH,
    PR_BODY_FILE,
    REPO_BRANCH_NAME_MAX_LEN,
    REPO_BRANCH_NAME_PATTERN,
    REPO_WORK_DIR,
    STDERR_BRIEF_LIMIT,
    STDERR_SHORT_LIMIT,
)
from models import CmdResult, RepoState
from repo.parsers import is_binary_diff_body, parse_name_status, parse_numstat
from shared.subprocess import fail, gh, git, git_indexed, run_cmd, scrub_secrets

log = logging.getLogger("sandbox.repo.service")

_GIT_TOKEN_KEY: str = "GIT_TOKEN"


class RepoService:
    """Manages the full git lifecycle for one sandbox run.

    Public API:
        bootstrap(body)      → RepoState
        save(message)        → dict
        teardown(body)       → dict
        diff_list()          → list[dict]   (file list, no bodies)
        diff_file(path)      → str          (one file's unified body)
    """

    def __init__(self) -> None:
        """Initialize with no repo state (set by bootstrap)."""
        self._state: RepoState | None = None

    @property
    def state(self) -> RepoState:
        """Return repo state. Fails fast if not bootstrapped."""
        if self._state is None:
            raise web.HTTPConflict(
                reason="repo not bootstrapped — call /repo/bootstrap first",
            )
        return self._state

    # ── Bootstrap ─────────────────────────────────────────────────────

    async def bootstrap(self, body: dict) -> RepoState:
        """Clone the repo, verify base branch, create working branch.

        GIT_TOKEN must be in os.environ (injected via POST /env).
        """
        repo, base_branch, working_branch = self._parse_bootstrap(body)

        if not os.environ.get(_GIT_TOKEN_KEY):
            raise web.HTTPBadRequest(
                reason="GIT_TOKEN not set — call POST /env before bootstrap",
            )

        await self._clone(repo)
        base_sha = await self._setup_base_branch(base_branch)
        await self._setup_working_branch(working_branch)

        self._state = RepoState(
            repo=repo,
            base_branch=base_branch,
            working_branch=working_branch,
            base_sha=base_sha,
        )
        return self._state

    # ── Save (per-round commit + push) ────────────────────────────────

    async def save(self, message: str) -> dict:
        """Commit + push. No-op if the working tree is clean."""
        await self._require_on_working_branch()

        if not await self._has_changes():
            return {"committed": False, "pushed": False, "push_error": None}

        committed = await self._commit(message)
        if not committed:
            return {"committed": False, "pushed": False, "push_error": None}

        push_error = await self._push()
        return {
            "committed": True,
            "pushed": push_error is None,
            "push_error": push_error,
        }

    # ── Teardown (end-of-run commit + push + PR + diff) ───────────────

    async def teardown(self, body: dict) -> dict:
        """Commit leftovers, push, create/update PR, capture diff."""
        pr_title: str = body["pr_title"]
        pr_description: str = body["pr_description"]
        base: str = body["base"]
        self._validate_branch(base)

        await self._require_on_working_branch()

        auto_committed = False
        if await self._has_changes():
            auto_committed = await self._commit(AUTO_COMMIT_MESSAGE)

        ahead = await self._commits_ahead(base)
        if ahead == 0:
            diff = await self._branch_diff()
            return self._teardown_response(
                auto_committed, 0, False, None, None, None, diff,
            )

        push_error = await self._push()
        if push_error is not None:
            diff = await self._branch_diff()
            return self._teardown_response(
                auto_committed, ahead, False, push_error, None, None, diff,
            )

        pr_url, pr_error = await self._create_or_update_pr(
            pr_title, pr_description, base,
        )
        diff = await self._branch_diff()
        return self._teardown_response(
            auto_committed, ahead, True, None, pr_url, pr_error, diff,
        )

    # ── Diff ──────────────────────────────────────────────────────────

    async def diff_list(self) -> list[dict]:
        """File-level changes of the working tree against base.

        Includes tracked edits AND untracked (new) files. Untracked files
        would be invisible to a plain `git diff <base>`, so we stage the
        whole working tree into a THROWAWAY index and diff that against base —
        the repo's real index is never touched. Returns
        [{path, status, added, removed}].
        """
        async with self._tmp_index() as index:
            base = self.state.base_sha
            numstat = await git_indexed(
                ["diff", "--numstat", "--cached", base],
                CMD_TIMEOUT, REPO_WORK_DIR, index,
            )
            self._fail_diff(numstat, "git diff --numstat")
            if not numstat.stdout.strip():
                return []
            name_status = await git_indexed(
                ["diff", "--name-status", "--cached", base],
                CMD_TIMEOUT, REPO_WORK_DIR, index,
            )
            self._fail_diff(name_status, "git diff --name-status")
            return parse_numstat(
                numstat.stdout, parse_name_status(name_status.stdout),
            )

    async def diff_response(self, expand: str | None) -> dict:
        """Build the unified diff response: file list with bodies null.

        Every file carries a `body` key (None by default). When `expand` is
        given, that one file's body is filled — and the path MUST be in the
        list, else it's a contract violation (404), never a silent empty
        body. This is the single source: the list defines what exists, and a
        body is only ever served for a path the same list contains.
        """
        files = await self.diff_list()
        for f in files:
            f["body"] = None
        if expand is not None:
            match = next((f for f in files if f["path"] == expand), None)
            if match is None:
                raise web.HTTPNotFound(
                    reason=f"expand path not in diff list: {expand}",
                )
            match["body"] = await self.diff_file(expand)
        return {"files": files}

    async def diff_file(self, path: str) -> str | None:
        """Unified diff body for a single file from the live working tree.

        The path must be one returned by diff_list() — the caller validates
        membership first, so an unknown path is a contract violation, not a
        silent empty body. Uses the same throwaway-index technique so tracked
        and untracked files render identically (untracked → 'new file' block).

        Returns None for a binary file (git emits "Binary files ... differ"
        instead of a text patch). This matches the GitHub path's
        extract_file_patch contract, so the frontend's single binary check
        (body === null) is correct for both sources.
        """
        async with self._tmp_index() as index:
            result = await git_indexed(
                ["diff", "--cached", self.state.base_sha, "--", path],
                CMD_TIMEOUT, REPO_WORK_DIR, index,
            )
            self._fail_diff(result, "git diff (file body)")
            if is_binary_diff_body(result.stdout):
                return None
            return result.stdout[:DIFF_FILE_BODY_MAX_CHARS]

    @contextlib.asynccontextmanager
    async def _tmp_index(self) -> AsyncIterator[str]:
        """Stage the working tree into a unique throwaway index, then clean up.

        Yields the path to a per-call index file (so concurrent diff requests
        never share one index and corrupt each other's `git add -A`). Copies
        the real index into it so renames/mode bits are seen relative to it,
        then `git add -A` stages everything — tracked edits AND untracked
        files — into THAT index. The real index is never written, so this
        never races the agent's own commits. The temp index is removed on
        exit regardless of success.
        """
        index = f"{DIFF_TMP_INDEX_PREFIX}{uuid.uuid4().hex}"
        try:
            cp = await run_cmd(
                ["cp", "-f", f"{REPO_WORK_DIR}/.git/index", index],
                REPO_WORK_DIR, CMD_TIMEOUT,
            )
            self._fail_cmd(cp, "cp real index → tmp index")
            add = await git_indexed(
                ["add", "-A"], CMD_TIMEOUT, REPO_WORK_DIR, index,
            )
            self._fail_diff(add, "git add -A (tmp index)")
            yield index
        finally:
            await run_cmd(["rm", "-f", index], REPO_WORK_DIR, CMD_TIMEOUT)

    def _fail_diff(self, result: CmdResult, label: str) -> None:
        """Raise HTTP 500 on a failed diff/index command.

        git diff returns exit code 1 for "differences found", which is
        success here — only treat exit codes other than 0/1 as failures.
        (git add returns 0 or a fatal 128, never 1, so accepting 1 here is
        harmless for the staging step.)
        """
        if result.exit_code in (0, 1):
            return
        self._raise_cmd_error(result, label)

    def _fail_cmd(self, result: CmdResult, label: str) -> None:
        """Raise HTTP 500 unless a plain command succeeded (exit 0).

        Used for non-diff steps (e.g. the index copy) where only exit 0 is
        success — surfacing the failure rather than silently diffing a stale
        or missing index.
        """
        if result.exit_code == 0:
            return
        self._raise_cmd_error(result, label)

    def _raise_cmd_error(self, result: CmdResult, label: str) -> None:
        """Raise a scrubbed HTTP 500 for a failed command."""
        detail = scrub_secrets(result.stderr)[:STDERR_SHORT_LIMIT]
        raise web.HTTPInternalServerError(
            text=f'{{"error": "{label} failed", "detail": "{detail}"}}',
            content_type="application/json",
        )

    # ── Private: bootstrap helpers ────────────────────────────────────

    def _parse_bootstrap(self, body: dict) -> tuple[str, str, str]:
        """Extract and validate bootstrap request fields."""
        repo: str = body["repo"]
        base_branch: str = body["base_branch"]
        working_branch: str = body["working_branch"]

        if "/" not in repo:
            raise web.HTTPBadRequest(reason="repo must be owner/name")
        self._validate_branch(base_branch)
        self._validate_branch(working_branch)

        return repo, base_branch, working_branch

    async def _clone(self, repo: str) -> None:
        """Clone repo via temp dir + rsync to handle bind mount conflicts."""
        await run_cmd(["rm", "-rf", CLONE_TMP_DIR], "/", CMD_TIMEOUT)
        await run_cmd(["mkdir", "-p", CLONE_TMP_DIR], "/", CMD_TIMEOUT)
        await run_cmd(["rm", "-rf", REPO_WORK_DIR], "/", CMD_TIMEOUT)
        await run_cmd(["mkdir", "-p", REPO_WORK_DIR], "/", CMD_TIMEOUT)

        remote_url = f"https://github.com/{repo}.git"
        fail(
            await git(
                ["clone", "--depth", str(GIT_CLONE_DEPTH), "--no-single-branch",
                 remote_url, "."],
                CMD_TIMEOUT,
                cwd=CLONE_TMP_DIR,
            ),
            "git clone",
        )

        mount_entries = await run_cmd(["ls", "-A", REPO_WORK_DIR], "/", CMD_TIMEOUT)
        excludes = [
            name.strip()
            for name in mount_entries.stdout.strip().split("\n")
            if name.strip()
        ]
        rsync_cmd = ["rsync", "-a"]
        for name in excludes:
            log.warning("Host mount shadows repo dir '%s' — using mounted version", name)
            rsync_cmd.append(f"--exclude=/{name}")
        rsync_cmd += [f"{CLONE_TMP_DIR}/", f"{REPO_WORK_DIR}/"]
        fail(await run_cmd(rsync_cmd, "/", CMD_TIMEOUT), "rsync clone into repo dir")
        await run_cmd(["rm", "-rf", CLONE_TMP_DIR], "/", CMD_TIMEOUT)

    async def _setup_base_branch(self, base_branch: str) -> str:
        """Verify base exists, fetch, checkout, return frozen base_sha."""
        fail(
            await git(
                ["ls-remote", "--exit-code", "--heads", "origin", base_branch],
                CMD_TIMEOUT,
                cwd=REPO_WORK_DIR,
            ),
            f"base branch '{base_branch}' not found on origin",
        )
        fail(
            await git(["fetch", "origin", base_branch], CMD_TIMEOUT, cwd=REPO_WORK_DIR),
            "git fetch",
        )
        fail(
            await git(
                ["checkout", "-B", base_branch, f"origin/{base_branch}"],
                CMD_TIMEOUT,
                cwd=REPO_WORK_DIR,
            ),
            "git checkout base",
        )
        sha_result = await git(
            ["rev-parse", f"origin/{base_branch}"], CMD_TIMEOUT, cwd=REPO_WORK_DIR,
        )
        fail(sha_result, f"git rev-parse origin/{base_branch}")
        base_sha = sha_result.stdout.strip()
        if not base_sha:
            raise web.HTTPInternalServerError(
                reason=f"git rev-parse origin/{base_branch} returned empty SHA",
            )
        return base_sha

    async def _setup_working_branch(self, working_branch: str) -> None:
        """Check out or create the working branch."""
        ls_result = await git(
            ["ls-remote", "--exit-code", "--heads", "origin", working_branch],
            CMD_TIMEOUT,
            cwd=REPO_WORK_DIR,
        )
        if ls_result.exit_code == 0:
            fail(
                await git(
                    ["fetch", "origin", working_branch], CMD_TIMEOUT, cwd=REPO_WORK_DIR,
                ),
                "git fetch working branch",
            )
            fail(
                await git(
                    ["checkout", "-b", working_branch, f"origin/{working_branch}"],
                    CMD_TIMEOUT,
                    cwd=REPO_WORK_DIR,
                ),
                "git checkout existing branch",
            )
        else:
            fail(
                await git(
                    ["checkout", "-b", working_branch], CMD_TIMEOUT, cwd=REPO_WORK_DIR,
                ),
                "git checkout -b",
            )

    # ── Private: git operations ───────────────────────────────────────

    async def _require_on_working_branch(self) -> None:
        """Refuse if HEAD isn't on the expected working branch."""
        s = self.state
        current = await git(
            ["branch", "--show-current"], CMD_TIMEOUT, cwd=REPO_WORK_DIR,
        )
        fail(current, "git branch --show-current")
        head = current.stdout.strip()
        if head != s.working_branch:
            raise web.HTTPConflict(
                reason=f"HEAD is on '{head}', not working branch '{s.working_branch}'",
            )

    async def _has_changes(self) -> bool:
        """True if the working tree has uncommitted or staged changes."""
        result = await git(["status", "--porcelain"], CMD_TIMEOUT, cwd=REPO_WORK_DIR)
        fail(result, "git status")
        return bool(result.stdout.strip())

    async def _commit(self, message: str) -> bool:
        """Stage everything and commit. Returns True on commit, False if clean.

        Always passes --no-verify to bypass pre-commit hooks on the target
        repo. We develop on a branch and squash-merge via PR — the target
        repo's CI validates the PR, not the commit hooks.
        """
        fail(await git(["add", "."], CMD_TIMEOUT, cwd=REPO_WORK_DIR), "git add")
        result = await git(
            ["commit", "--no-verify", "-m", message], CMD_TIMEOUT, cwd=REPO_WORK_DIR,
        )
        if result.exit_code != 0 and "nothing to commit" in (result.stdout + result.stderr):
            return False
        fail(result, "git commit")
        return True

    async def _push(self) -> str | None:
        """Push working branch. Returns error string on failure, None on success."""
        s = self.state
        result = await git(
            ["push", "--no-verify", "-u", "origin", s.working_branch], CMD_TIMEOUT, cwd=REPO_WORK_DIR,
        )
        if result.exit_code != 0:
            err = scrub_secrets(result.stderr.strip())[:STDERR_SHORT_LIMIT]
            log.warning("push failed: %s", err)
            return err
        return None

    async def _commits_ahead(self, base: str) -> int:
        """Count commits between origin/base and HEAD."""
        fail(
            await git(
                ["fetch", "origin", base, "--depth", "1"], CMD_TIMEOUT, cwd=REPO_WORK_DIR,
            ),
            "git fetch base",
        )
        result = await git(
            ["rev-list", "--count", f"origin/{base}..HEAD"], CMD_TIMEOUT, cwd=REPO_WORK_DIR,
        )
        fail(result, "git rev-list")
        count_str = result.stdout.strip()
        lines = count_str.splitlines()
        if not lines:
            raise RuntimeError("git rev-list --count returned empty output")
        count_str = lines[-1].strip()
        if not count_str.isdigit():
            raise RuntimeError(
                f"git rev-list --count returned non-integer output: {count_str!r}"
            )
        return int(count_str)

    async def _diff_stats(self, base_sha: str, end_ref: str | None) -> list[dict]:
        """File-level diff stats from base_sha, optionally to end_ref (else working tree)."""
        refs = [base_sha] if end_ref is None else [base_sha, end_ref]
        numstat = await git(
            ["diff", "--numstat"] + refs, CMD_TIMEOUT, cwd=REPO_WORK_DIR,
        )
        if numstat.exit_code != 0 or not numstat.stdout.strip():
            return []
        name_status = await git(
            ["diff", "--name-status"] + refs, CMD_TIMEOUT, cwd=REPO_WORK_DIR,
        )
        if name_status.exit_code != 0:
            return []
        return parse_numstat(numstat.stdout, parse_name_status(name_status.stdout))

    async def _branch_diff(self) -> list[dict]:
        """File-level diff stats between working branch and base SHA."""
        return await self._diff_stats(self.state.base_sha, self.state.working_branch)

    async def _create_or_update_pr(
        self, title: str, description: str, base: str,
    ) -> tuple[str | None, str | None]:
        """Create a PR, or edit the existing one. Returns (url, error)."""
        s = self.state
        find = await gh(
            ["pr", "view", s.working_branch, "--repo", s.repo,
             "--json", "url", "-q", ".url"],
            CMD_TIMEOUT,
            cwd=REPO_WORK_DIR,
        )
        existing = find.stdout.strip() if find.exit_code == 0 else ""

        # Pass the body via --body-file: a large body as a single argv element
        # trips the kernel's 128KB per-arg limit (E2BIG) at exec time.
        with open(PR_BODY_FILE, "w") as f:
            f.write(description)

        if existing:
            edit = await gh(
                ["pr", "edit", existing, "--title", title,
                 "--body-file", PR_BODY_FILE],
                CMD_TIMEOUT,
                cwd=REPO_WORK_DIR,
            )
            if edit.exit_code != 0:
                err = scrub_secrets(edit.stderr.strip())[:STDERR_BRIEF_LIMIT]
                return existing, f"gh pr edit failed: {err}"
            return existing, None

        create = await gh(
            [
                "pr", "create",
                "--repo", s.repo,
                "--base", base,
                "--head", s.working_branch,
                "--title", title,
                "--body-file", PR_BODY_FILE,
            ],
            CMD_TIMEOUT,
            cwd=REPO_WORK_DIR,
        )
        if create.exit_code != 0:
            err = scrub_secrets(create.stderr.strip())[:STDERR_BRIEF_LIMIT]
            if GH_NO_DIFF_MARKER in err:
                log.info("GitHub reports no diff between branches — no PR needed")
                return None, None
            return None, f"gh pr create failed: {err}"
        return create.stdout.strip(), None

    # ── Private: validation ───────────────────────────────────────────

    def _validate_branch(self, name: str) -> None:
        """Reject branch names with invalid characters."""
        if not name or len(name) > REPO_BRANCH_NAME_MAX_LEN:
            raise web.HTTPBadRequest(reason=f"invalid branch length: {len(name or '')}")
        if not REPO_BRANCH_NAME_PATTERN.match(name):
            raise web.HTTPBadRequest(reason="invalid branch name characters")
        if ".." in name or name.endswith(".lock") or name.endswith("/"):
            raise web.HTTPBadRequest(reason="invalid branch name format")

    def _teardown_response(
        self,
        auto_committed: bool,
        commits_ahead: int,
        pushed: bool,
        push_error: str | None,
        pr_url: str | None,
        pr_error: str | None,
        diff_stats: list[dict],
    ) -> dict:
        """Construct the teardown response dict."""
        return {
            "auto_committed": auto_committed,
            "commits_ahead": commits_ahead,
            "pushed": pushed,
            "push_error": push_error,
            "pr_url": pr_url,
            "pr_error": pr_error,
            "diff_stats": diff_stats,
        }
