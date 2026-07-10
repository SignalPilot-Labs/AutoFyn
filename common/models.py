"""Shared data models for the credential pool."""

from pydantic import BaseModel, Field

from db.constants import TOKEN_LABEL_MAX_LEN, TOKEN_VALUE_MAX_LEN


class Token(BaseModel):
    """A Claude credential in the pool: the secret value and an optional name."""

    value: str = Field(min_length=1, max_length=TOKEN_VALUE_MAX_LEN)
    label: str | None = Field(default=None, max_length=TOKEN_LABEL_MAX_LEN)


def parse_token_pool(raw: list) -> list[Token]:
    """Parse a decrypted pool into Tokens, upgrading legacy bare-string entries."""
    return [Token(value=e, label=None) if isinstance(e, str) else Token(**e) for e in raw]
