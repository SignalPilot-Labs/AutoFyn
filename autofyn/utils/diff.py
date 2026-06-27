"""Diff utilities: parsing and GitHub API fetching."""

import httpx

GITHUB_API_TIMEOUT = 15


def _status_from_section(body: str) -> str:
    """Classify a diff section by its leading markers (mirror of the FE)."""
    if body.startswith("new file"):
        return "added"
    if body.startswith("deleted file"):
        return "deleted"
    if body.startswith("rename ") or "\nrename to " in body:
        return "renamed"
    return "modified"


def parse_diff_blob_to_files(full_diff: str) -> list[dict]:
    """Parse a full unified diff blob into [{path, status, added, removed}].

    Produces the SAME file-list shape the sandbox temp-index path returns,
    so completed-run (GitHub blob) and live-run diffs share one contract.
    Line counts come from the body's +/- lines, ignoring the +++/--- file
    headers; status comes from the section's leading markers.
    """
    files: list[dict] = []
    sections = full_diff.split("\ndiff --git ")
    for i, raw in enumerate(sections):
        section = raw
        if i == 0:
            if section.startswith("diff --git "):
                section = section[len("diff --git "):]
            else:
                continue
        nl = section.find("\n")
        if nl == -1:
            continue
        header = section[:nl]
        b_idx = header.rfind(" b/")
        if b_idx == -1:
            continue
        path = header[b_idx + 3:]
        body = section[nl + 1:]
        added = 0
        removed = 0
        for line in body.split("\n"):
            if line.startswith("+") and not line.startswith("+++"):
                added += 1
            elif line.startswith("-") and not line.startswith("---"):
                removed += 1
        files.append({
            "path": path,
            "status": _status_from_section(body),
            "added": added,
            "removed": removed,
        })
    return files


def extract_file_patch(full_diff: str, target_path: str) -> str | None:
    """Extract the unified diff patch for a single file from a full diff.

    Returns the patch body or None if the file is not found or is binary.
    """
    marker = f" b/{target_path}"
    sections = full_diff.split("\ndiff --git ")
    for i, section in enumerate(sections):
        if i == 0:
            if section.startswith("diff --git "):
                section = section[len("diff --git "):]
            else:
                continue
        first_newline = section.find("\n")
        if first_newline == -1:
            continue
        header = section[:first_newline]
        if header.endswith(marker):
            body = section[first_newline + 1:]
            if body.startswith("Binary files") and "differ" in body.split("\n")[0]:
                return None
            return body
    return None


async def fetch_github_diff(
    repo: str,
    branch: str,
    base: str,
    token: str,
) -> dict:
    """Fetch full unified diff from GitHub. Tries compare API, falls back to PR.

    Returns {"diff": str} on success or {"error": str, "status": int} on failure.
    Raises ValueError if repo is not a valid 'owner/name' slug.
    """
    parts = repo.split("/")
    if len(parts) != 2 or not parts[0] or not parts[1]:
        raise ValueError(f"Invalid repo slug '{repo}': expected 'owner/name' format")

    headers = {"Authorization": f"token {token}"}

    async with httpx.AsyncClient(timeout=GITHUB_API_TIMEOUT) as http:
        resp = await http.get(
            f"https://api.github.com/repos/{repo}/compare/{base}...{branch}",
            headers={**headers, "Accept": "application/vnd.github.v3.diff"},
        )

        if resp.status_code == 200:
            return {"diff": resp.text}

        if resp.status_code != 404:
            return {"error": f"GitHub API error: {resp.text[:200]}", "status": resp.status_code}

        # Branch deleted — try PR
        pr_resp = await http.get(
            f"https://api.github.com/repos/{repo}/pulls",
            headers={**headers, "Accept": "application/vnd.github+json"},
            params={"head": f"{repo.split('/')[0]}:{branch}", "state": "all", "per_page": 1},
        )

        if pr_resp.status_code != 200 or not pr_resp.json():
            return {"error": "Branch deleted and no PR found — diff unavailable", "status": 404}

        pr_number = pr_resp.json()[0]["number"]
        diff_resp = await http.get(
            f"https://api.github.com/repos/{repo}/pulls/{pr_number}",
            headers={**headers, "Accept": "application/vnd.github.v3.diff"},
        )

        if diff_resp.status_code != 200:
            return {"error": "Could not fetch PR diff", "status": diff_resp.status_code}

        return {"diff": diff_resp.text}
