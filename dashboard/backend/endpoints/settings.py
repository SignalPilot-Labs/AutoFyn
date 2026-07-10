"""Dashboard API endpoints — settings, repos, and token pool."""

import json
import logging

from cryptography.fernet import InvalidToken
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from backend import auth
from backend.constants import (
    DECRYPT_ERROR_INDICATOR,
    MASK_PREFIX_DEFAULT,
    SECRET_KEYS,
)
from config.loader import load_subagents
from common import crypto
from db.constants import (
    DISABLED_SUBAGENTS_KEY_PREFIX,
    GITHUB_REPO_MAX_LEN,
    GITHUB_REPO_RE,
    HOST_MOUNTS_KEY_PREFIX,
    MASTER_KEY_PATH,
    REPO_SUBAGENTS_CACHE_KEY_PREFIX,
    validate_host_mount,
)
from backend.models import (
    AddTokenRequest,
    SaveDisabledSubagentsRequest,
    SaveMcpServersRequest,
    SaveMountsRequest,
    SaveRepoEnvRequest,
    SetActiveRepoRequest,
    UpdateSettingsRequest,
)
from backend.utils import (
    CredentialDecryptionError,
    _decrypt_json,
    read_token_pool,
    add_token_to_pool,
    ensure_repo_in_list,
    get_repo_list,
    list_pool_tokens,
    remove_token_from_pool,
    save_repo_list,
    session,
    upsert_setting,
)
from db.models import Run, Setting

log = logging.getLogger("dashboard.settings")

router = APIRouter(prefix="/api", dependencies=[Depends(auth.verify_api_key)])


def validate_repo_slug(repo: str) -> str:
    """Validate that repo is a safe owner/repo slug. Raises HTTP 400 on failure."""
    if not GITHUB_REPO_RE.fullmatch(repo):
        raise HTTPException(status_code=400, detail="Invalid repo slug format")
    if len(repo) > GITHUB_REPO_MAX_LEN:
        raise HTTPException(status_code=400, detail="Invalid repo slug format")
    owner, _, name = repo.partition("/")
    if owner in (".", "..") or name in (".", ".."):
        raise HTTPException(status_code=400, detail="Invalid repo slug format")
    return repo


@router.get("/settings/status")
async def settings_status() -> dict:
    """Check which credentials are configured."""
    async with session() as s:
        has: dict[str, bool] = {}
        has["has_claude_token"] = bool(await read_token_pool(s, for_update=False))
        for key in ("git_token", "github_repo"):
            has[f"has_{key}"] = (await s.get(Setting, key)) is not None
        has["configured"] = all(has.values())
        return has


def _decrypt_setting(setting: Setting) -> str:
    """Decrypt and mask an encrypted setting value."""
    plain = crypto.decrypt(setting.value, MASTER_KEY_PATH)
    prefix = MASK_PREFIX_DEFAULT
    return crypto.mask(plain, prefix_len=prefix)


def _env_vars_key(repo: str) -> str:
    """Setting table key for per-repo environment variables."""
    return f"env_vars:{repo}"


def _host_mounts_key(repo: str) -> str:
    """Setting table key for per-repo host directory mounts."""
    return f"{HOST_MOUNTS_KEY_PREFIX}{repo}"


def _mcp_servers_key(repo: str) -> str:
    """Setting table key for per-repo MCP server configurations."""
    return f"mcp_servers:{repo}"


def _disabled_subagents_key(repo: str) -> str:
    """Setting table key for the per-repo disabled-subagents list."""
    return f"{DISABLED_SUBAGENTS_KEY_PREFIX}{repo}"


def _repo_subagents_cache_key(repo: str) -> str:
    """Setting table key for a repo's cached user-defined subagents."""
    return f"{REPO_SUBAGENTS_CACHE_KEY_PREFIX}{repo}"


@router.get("/settings")
async def get_settings() -> dict:
    """Get all settings with secrets masked."""
    async with session() as s:
        result = await s.execute(select(Setting))
        settings: dict[str, str] = {}
        for setting in result.scalars().all():
            if setting.key.startswith("env_vars:") or setting.key.startswith(HOST_MOUNTS_KEY_PREFIX) or setting.key.startswith("mcp_servers:"):
                continue
            if setting.encrypted:
                try:
                    settings[setting.key] = _decrypt_setting(setting)
                except InvalidToken as e:
                    log.error("Failed to decrypt setting '%s': %s", setting.key, e, exc_info=True)
                    settings[setting.key] = DECRYPT_ERROR_INDICATOR
            else:
                settings[setting.key] = setting.value
        return settings


@router.put("/settings")
async def update_settings(body: UpdateSettingsRequest) -> dict:
    """Create or update settings. Secrets are encrypted before storage."""
    updates = body.model_dump(exclude_none=True)
    async with session() as s:
        for key, value in updates.items():
            is_secret = key in SECRET_KEYS
            stored_val = crypto.encrypt(value, MASTER_KEY_PATH) if is_secret else value
            await upsert_setting(s, key, stored_val, is_secret)
        if "github_repo" in updates and updates["github_repo"]:
            await ensure_repo_in_list(s, updates["github_repo"])
        await s.commit()
    return {"ok": True, "updated": list(updates.keys())}


@router.get("/repos/{repo:path}/env")
async def get_repo_env(repo: str) -> dict:
    """Get decrypted env vars for a repo. Values are shown in plaintext for the settings UI."""
    repo = validate_repo_slug(repo)
    async with session() as s:
        setting = await s.get(Setting, _env_vars_key(repo))
        if not setting:
            return {"repo": repo, "env_vars": {}}
        try:
            env_dict: dict[str, str] = _decrypt_json(setting, _env_vars_key(repo))
        except CredentialDecryptionError as e:
            log.error("Failed to decrypt env vars for %s: %s", repo, e, exc_info=True)
            raise HTTPException(status_code=500, detail="Failed to decrypt env vars") from e
        return {"repo": repo, "env_vars": env_dict}


@router.put("/repos/{repo:path}/env")
async def save_repo_env(repo: str, body: SaveRepoEnvRequest) -> dict:
    """Save env vars for a repo. Full replacement — omitted keys are deleted."""
    repo = validate_repo_slug(repo)
    env_vars: dict[str, str] = body.env_vars
    async with session() as s:
        if env_vars:
            encrypted = crypto.encrypt(json.dumps(env_vars), MASTER_KEY_PATH)
            await upsert_setting(s, _env_vars_key(repo), encrypted, True)
        else:
            existing = await s.get(Setting, _env_vars_key(repo))
            if existing:
                await s.delete(existing)
        await s.commit()
    return {"ok": True, "repo": repo, "key_count": len(env_vars)}


@router.get("/repos/{repo:path}/mounts")
async def get_repo_mounts(repo: str) -> dict:
    """Get host directory mounts for a repo."""
    repo = validate_repo_slug(repo)
    async with session() as s:
        setting = await s.get(Setting, _host_mounts_key(repo))
        if not setting:
            return {"repo": repo, "mounts": []}
        try:
            mounts: list[dict[str, str]] = json.loads(setting.value)
            return {"repo": repo, "mounts": mounts}
        except Exception as e:
            log.error("Failed to parse host mounts for %s: %s", repo, e, exc_info=True)
            raise HTTPException(status_code=500, detail="Failed to parse host mounts")


@router.put("/repos/{repo:path}/mounts")
async def save_repo_mounts(repo: str, body: SaveMountsRequest) -> dict:
    """Save host directory mounts for a repo. Full replacement."""
    repo = validate_repo_slug(repo)
    for mount in body.mounts:
        error = validate_host_mount(mount.host_path, mount.container_path, mount.mode)
        if error:
            raise HTTPException(status_code=422, detail=error)
    serialized = [m.model_dump() for m in body.mounts]
    async with session() as s:
        if serialized:
            await upsert_setting(s, _host_mounts_key(repo), json.dumps(serialized), False)
        else:
            existing = await s.get(Setting, _host_mounts_key(repo))
            if existing:
                await s.delete(existing)
        await s.commit()
    return {"ok": True, "repo": repo, "mount_count": len(serialized)}


@router.get("/repos/{repo:path}/mcp-servers")
async def get_repo_mcp_servers(repo: str) -> dict:
    """Get MCP server configurations for a repo. Values decrypted for settings UI."""
    repo = validate_repo_slug(repo)
    async with session() as s:
        setting = await s.get(Setting, _mcp_servers_key(repo))
        if not setting:
            return {"repo": repo, "servers": {}}
        try:
            servers: dict[str, dict] = _decrypt_json(setting, _mcp_servers_key(repo))
        except CredentialDecryptionError as e:
            log.error("Failed to decrypt MCP servers for %s: %s", repo, e, exc_info=True)
            raise HTTPException(status_code=500, detail="Failed to decrypt MCP servers") from e
        return {"repo": repo, "servers": servers}


@router.put("/repos/{repo:path}/mcp-servers")
async def save_repo_mcp_servers(repo: str, body: SaveMcpServersRequest) -> dict:
    """Save MCP server configurations for a repo. Full replacement — omitted servers are deleted."""
    repo = validate_repo_slug(repo)
    async with session() as s:
        if body.servers:
            encrypted = crypto.encrypt(json.dumps(body.servers), MASTER_KEY_PATH)
            await upsert_setting(s, _mcp_servers_key(repo), encrypted, True)
        else:
            existing = await s.get(Setting, _mcp_servers_key(repo))
            if existing:
                await s.delete(existing)
        await s.commit()
    return {"ok": True, "repo": repo, "server_count": len(body.servers)}


@router.get("/repos/{repo:path}/subagents")
async def get_repo_subagents(repo: str) -> dict:
    """Get the subagents (shipped + repo-defined) and which are disabled.

    `agents` is the merged list (name/type/description/source) the toggle UI
    renders; each carries `source` = "core" (shipped) or "user" (repo-defined).
    User agents come from a cache the agent writes at run time (a repo never run
    yet shows core agents only). A user agent that overrides a core name wins.
    `disabled` is the user's per-repo off-list, filtered to names that still
    exist in the merged set — so an agent removed from `.autofyn/subagents.json`
    leaves no ghost in the disabled list or the "N of M enabled" count.
    """
    repo = validate_repo_slug(repo)
    async with session() as s:
        agents = await _merged_subagents(s, repo)
        stored_disabled = await _disabled_subagents(s, repo)
    known_names = {a["name"] for a in agents}
    disabled = [name for name in stored_disabled if name in known_names]
    return {"repo": repo, "agents": agents, "disabled": disabled}


async def _merged_subagents(s: AsyncSession, repo: str) -> list[dict]:
    """Core (shipped) subagents merged with the repo's cached ones (user wins)."""
    merged: dict[str, dict] = {
        spec.name: {
            "name": spec.name,
            "type": spec.type,
            "description": spec.description,
            "source": "core",
        }
        for spec in load_subagents()
    }
    cached = await s.get(Setting, _repo_subagents_cache_key(repo))
    if cached:
        try:
            repo_agents: list[dict] = json.loads(cached.value)
        except (json.JSONDecodeError, TypeError) as e:
            log.error("Failed to parse repo subagents cache for %s: %s", repo, e, exc_info=True)
            raise HTTPException(status_code=500, detail="Failed to parse repo subagents") from e
        for agent in repo_agents:
            merged[agent["name"]] = {**agent, "source": "user"}
    return list(merged.values())


async def _disabled_subagents(s: AsyncSession, repo: str) -> list[str]:
    """The user's per-repo disabled-subagents list ([] if unset)."""
    setting = await s.get(Setting, _disabled_subagents_key(repo))
    if not setting:
        return []
    try:
        return json.loads(setting.value)
    except (json.JSONDecodeError, TypeError) as e:
        log.error("Failed to parse disabled subagents for %s: %s", repo, e, exc_info=True)
        raise HTTPException(status_code=500, detail="Failed to parse disabled subagents") from e


@router.put("/repos/{repo:path}/subagents")
async def save_repo_subagents(repo: str, body: SaveDisabledSubagentsRequest) -> dict:
    """Save the disabled-subagents list for a repo. Full replacement.

    Rejects unknown agent names and the all-disabled case — a run needs at
    least one subagent. An empty list deletes the setting (all enabled).
    """
    repo = validate_repo_slug(repo)
    disabled = set(body.disabled)
    async with session() as s:
        known_names = {a["name"] for a in await _merged_subagents(s, repo)}
        unknown = disabled - known_names
        if unknown:
            raise HTTPException(
                status_code=422,
                detail=f"Unknown subagent(s): {', '.join(sorted(unknown))}",
            )
        if disabled >= known_names:
            raise HTTPException(
                status_code=422,
                detail="Cannot disable every subagent — at least one must stay enabled",
            )
        if disabled:
            await upsert_setting(
                s, _disabled_subagents_key(repo), json.dumps(sorted(disabled)), False
            )
        else:
            existing = await s.get(Setting, _disabled_subagents_key(repo))
            if existing:
                await s.delete(existing)
        await s.commit()
    return {"ok": True, "repo": repo, "disabled_count": len(disabled)}


@router.get("/repos")
async def list_repos() -> list:
    """List all configured repos with run counts."""
    async with session() as s:
        repos = await get_repo_list(s)

        active = await s.get(Setting, "github_repo")
        if active and active.value and active.value not in repos:
            await ensure_repo_in_list(s, active.value)
            repos.append(active.value)
            await s.commit()

        result = []
        for repo in repos:
            count = (
                await s.execute(
                    select(func.count()).select_from(Run).where(Run.github_repo == repo)
                )
            ).scalar_one()
            result.append({"repo": repo, "run_count": count})
        return result


@router.put("/repos/active")
async def set_active_repo(body: SetActiveRepoRequest) -> dict:
    """Set the active repo."""
    async with session() as s:
        await upsert_setting(s, "github_repo", body.repo, False)
        await ensure_repo_in_list(s, body.repo)
        await s.commit()
    return {"ok": True, "active_repo": body.repo}


@router.delete("/repos/{repo_slug:path}")
async def remove_repo(repo_slug: str) -> dict:
    """Remove a repo from the list (does not delete runs)."""
    repo_slug = validate_repo_slug(repo_slug)
    async with session() as s:
        repos = [r for r in await get_repo_list(s) if r != repo_slug]
        await save_repo_list(s, repos)
        await s.commit()
    return {"ok": True, "remaining": repos}


@router.get("/tokens")
async def get_tokens() -> list:
    """List all Claude tokens in the pool (masked)."""
    return await list_pool_tokens()


@router.post("/tokens")
async def add_token(body: AddTokenRequest) -> dict:
    """Add a Claude token to the pool."""
    stripped = body.label.strip() if body.label else ""
    label = stripped or None
    try:
        return await add_token_to_pool(body.token.strip(), label)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))


@router.delete("/tokens/{index}")
async def delete_token(index: int) -> dict:
    """Remove a token from the pool by index."""
    try:
        return await remove_token_from_pool(index)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
