"""Pydantic request models and path validators for the dashboard API."""

from fastapi import Path
from pydantic import BaseModel, Field, field_validator, model_validator

from common.constants import DEFAULT_MODEL, DEFAULT_PROVIDER, VALID_MODELS_PATTERN, VALID_PROVIDERS_PATTERN, providers_for_model
from db.constants import DEFAULT_EFFORT, ENV_VAR_KEY_RE, ENV_VAR_MAX_KEY_LEN, ENV_VAR_MAX_VALUE_LEN, GITHUB_REPO_MAX_LEN, GITHUB_REPO_PATTERN, INT_SETTING_MAX_LEN, MAX_CONCURRENT_RUNS_MAX, MAX_CONCURRENT_RUNS_MIN, MAX_ENV_VARS, MAX_HOST_MOUNTS, MAX_MCP_SERVERS, MAX_SUBAGENTS, RUNS_PAGE_SIZE_MAX, RUNS_PAGE_SIZE_MIN, SETTING_MAX_CONCURRENT_RUNS, SETTING_RUNS_PAGE_SIZE, TOKEN_LABEL_MAX_LEN, TOKEN_VALUE_MAX_LEN, VALID_EFFORTS_PATTERN, VALID_PRESET_PATTERN, validate_int_setting, validate_prompt_length


RunId = Path(min_length=36, max_length=36, pattern=r"^[0-9a-f\-]{36}$")


class ControlSignalRequest(BaseModel):
    """Request body for control signal endpoints."""

    payload: str | None = None


class StopRunRequest(BaseModel):
    """Request body for the stop endpoint."""

    payload: str | None = None
    skip_pr: bool


class StartRunRequest(BaseModel):
    """Request body for starting a new run."""

    prompt: str | None = None
    preset: str | None = Field(None, pattern=VALID_PRESET_PATTERN, description="Starter preset key. Mutually exclusive with prompt.")
    max_budget_usd: float = Field(default=0, ge=0, description="Max spend in USD. 0 = unlimited.")
    duration_minutes: float = Field(default=0, ge=0, description="Session duration in minutes. 0 = unlimited.")
    base_branch: str = Field(default="main", min_length=1, max_length=256, description="Branch to base the work on.")
    model: str = Field(default=DEFAULT_MODEL, pattern=VALID_MODELS_PATTERN, description="Claude model to use.")
    provider: str = Field(pattern=VALID_PROVIDERS_PATTERN, description="Provider serving the model for this run.")
    effort: str = Field(default=DEFAULT_EFFORT, pattern=VALID_EFFORTS_PATTERN, description="Thinking effort level.")
    repo: str | None = Field(None, description="Active repo slug for per-repo env vars lookup.")
    sandbox_id: str | None = Field(default=None, description="UUID of remote sandbox config. None for local Docker.")
    start_cmd: str = Field(default="", max_length=65536, description="Start command for sandbox.")

    @field_validator("prompt")
    @classmethod
    def prompt_max_length(cls, v: str | None) -> str | None:
        """Validate prompt length."""
        return validate_prompt_length(v)

    @model_validator(mode="after")
    def provider_serves_model(self) -> "StartRunRequest":
        """Reject a provider that cannot serve the selected model."""
        if self.provider not in providers_for_model(self.model):
            raise ValueError(f"provider '{self.provider}' does not serve model '{self.model}'")
        return self


class UpdateSettingsRequest(BaseModel):
    """Request body for updating settings."""

    git_token: str | None = Field(None, min_length=1, max_length=4096)
    github_repo: str | None = Field(None, min_length=1, max_length=GITHUB_REPO_MAX_LEN, pattern=GITHUB_REPO_PATTERN)
    max_budget_usd: str | None = Field(None, min_length=1, max_length=20)
    dashboard_api_key: str | None = Field(None, min_length=20, max_length=256)
    model: str | None = Field(None, pattern=VALID_MODELS_PATTERN, description="Default Claude model.")
    max_concurrent_runs: str | None = Field(None, min_length=1, max_length=INT_SETTING_MAX_LEN)
    runs_page_size: str | None = Field(None, min_length=1, max_length=INT_SETTING_MAX_LEN)

    @field_validator("max_concurrent_runs")
    @classmethod
    def max_concurrent_runs_in_bounds(cls, v: str | None) -> str | None:
        """Validate max_concurrent_runs is an integer within bounds."""
        return validate_int_setting(v, SETTING_MAX_CONCURRENT_RUNS, MAX_CONCURRENT_RUNS_MIN, MAX_CONCURRENT_RUNS_MAX)

    @field_validator("runs_page_size")
    @classmethod
    def runs_page_size_in_bounds(cls, v: str | None) -> str | None:
        """Validate runs_page_size is an integer within bounds."""
        return validate_int_setting(v, SETTING_RUNS_PAGE_SIZE, RUNS_PAGE_SIZE_MIN, RUNS_PAGE_SIZE_MAX)


class SetActiveRepoRequest(BaseModel):
    """Request body for setting active repo."""

    repo: str = Field(min_length=1, max_length=GITHUB_REPO_MAX_LEN, pattern=GITHUB_REPO_PATTERN)


class ResumeRunRequest(BaseModel):
    """Request body for resuming a previous run."""

    run_id: str = Field(min_length=36, max_length=36, pattern=r"^[0-9a-f\-]{36}$")
    max_budget_usd: float = Field(default=0, ge=0, description="Max spend in USD. 0 = unlimited.")
    model: str | None = Field(None, pattern=VALID_MODELS_PATTERN, description="Override model for the resumed run. Defaults to the original run's model.")


class HostMountEntry(BaseModel):
    """A single host directory mount."""

    host_path: str = Field(min_length=1, max_length=4096)
    container_path: str = Field(min_length=1, max_length=4096)
    mode: str = Field(pattern=r"^(ro|rw)$")


class SaveMountsRequest(BaseModel):
    """Request body for saving per-repo host mounts."""

    mounts: list[HostMountEntry] = Field(default_factory=list, max_length=MAX_HOST_MOUNTS)


class SaveMcpServersRequest(BaseModel):
    """Request body for saving per-repo MCP server configurations."""

    servers: dict[str, dict] = Field(default_factory=dict)

    @field_validator("servers")
    @classmethod
    def servers_max_count(cls, v: dict[str, dict]) -> dict[str, dict]:
        """Validate that the number of servers does not exceed MAX_MCP_SERVERS."""
        if len(v) > MAX_MCP_SERVERS:
            raise ValueError(f"Cannot configure more than {MAX_MCP_SERVERS} MCP servers")
        return v


class SaveDisabledSubagentsRequest(BaseModel):
    """Request body for saving the per-repo disabled-subagents list.

    Holds the names of shipped subagents the user has turned off. Names are
    validated against the shipped subagents (and the all-disabled case
    rejected) in the endpoint, where they are loaded.
    """

    disabled: list[str] = Field(default_factory=list, max_length=MAX_SUBAGENTS)


class SaveRepoEnvRequest(BaseModel):
    """Request body for saving per-repo environment variables."""

    env_vars: dict[str, str]

    @field_validator("env_vars")
    @classmethod
    def validate_env_vars(cls, v: dict[str, str]) -> dict[str, str]:
        """Validate count, key format, and value length for all env vars."""
        if len(v) > MAX_ENV_VARS:
            raise ValueError(f"Cannot store more than {MAX_ENV_VARS} env vars per repo")
        for key, value in v.items():
            if len(key) > ENV_VAR_MAX_KEY_LEN:
                raise ValueError(
                    f"Env var key exceeds maximum length of {ENV_VAR_MAX_KEY_LEN}: {key!r}"
                )
            if not ENV_VAR_KEY_RE.fullmatch(key):
                raise ValueError(
                    f"Env var key {key!r} must match ^[A-Za-z_][A-Za-z0-9_]*$"
                )
            if len(value) > ENV_VAR_MAX_VALUE_LEN:
                raise ValueError(
                    f"Env var value for key {key!r} exceeds maximum length of {ENV_VAR_MAX_VALUE_LEN}"
                )
        return v


class AddTokenRequest(BaseModel):
    """Request body for adding a credential to the pool."""

    provider: str = Field(default=DEFAULT_PROVIDER, pattern=VALID_PROVIDERS_PATTERN)
    token: str = Field(min_length=1, max_length=TOKEN_VALUE_MAX_LEN)
    label: str | None = Field(default=None, max_length=TOKEN_LABEL_MAX_LEN)


class RenameTokenRequest(BaseModel):
    """Request body for renaming a pool credential's label (value never changes)."""

    label: str | None = Field(default=None, max_length=TOKEN_LABEL_MAX_LEN)
