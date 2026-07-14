"""Shared data models for the credential pool."""

from pydantic import BaseModel, Field, field_validator

from common.constants import DEFAULT_PROVIDER, VALID_PROVIDERS
from db.constants import TOKEN_LABEL_MAX_LEN, TOKEN_VALUE_MAX_LEN


class Token(BaseModel):
    """A credential in the pool: its provider, the secret value, and an optional name."""

    provider: str = Field(default=DEFAULT_PROVIDER)
    value: str = Field(min_length=1, max_length=TOKEN_VALUE_MAX_LEN)
    label: str | None = Field(default=None, max_length=TOKEN_LABEL_MAX_LEN)

    @field_validator("provider")
    @classmethod
    def _provider_is_known(cls, v: str) -> str:
        """Reject unknown providers here so every write path shares one gate."""
        if v not in VALID_PROVIDERS:
            raise ValueError(f"unknown provider '{v}' (valid: {', '.join(VALID_PROVIDERS)})")
        return v


def parse_token_pool(raw: list) -> list[Token]:
    """Parse a decrypted pool into Tokens, upgrading legacy entries.

    Two legacy shapes are upgraded to DEFAULT_PROVIDER: bare strings (pre-pool)
    and dicts written before the provider field existed. Token's provider
    default supplies anthropic when the key is absent.
    """
    return [Token(value=e) if isinstance(e, str) else Token(**e) for e in raw]
