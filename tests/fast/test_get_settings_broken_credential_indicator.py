"""Regression test: get_settings() must render broken credentials distinctly from valid masked ones.

Bug: When _decrypt_setting() raised any exception, get_settings() substituted
ENV_VARS_MASK_CHAR ("****"), making a broken/undecryptable setting look identical
to a valid masked setting. Also caught broad `except Exception`, swallowing
programming errors.

Fix (T7): Catch only InvalidToken (the specific decrypt failure mode). Substitute
DECRYPT_ERROR_INDICATOR — visually distinct from ENV_VARS_MASK_CHAR. Let all
other exceptions propagate (Fail Fast).
"""

from __future__ import annotations

import sys
from contextlib import asynccontextmanager
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from cryptography.fernet import InvalidToken

# Stub out modules that require live services before importing settings endpoint.
if "db.connection" not in sys.modules:
    sys.modules["db.connection"] = MagicMock()
if "db.models" not in sys.modules:
    sys.modules["db.models"] = MagicMock()

_auth_mock = MagicMock()
_auth_mock.verify_api_key = MagicMock(return_value=None)
sys.modules["backend.auth"] = _auth_mock

import backend.endpoints.settings as settings_mod  # noqa: E402
from backend.constants import DECRYPT_ERROR_INDICATOR, ENV_VARS_MASK_CHAR  # noqa: E402


def _make_encrypted_setting(key: str, value: str) -> MagicMock:
    s = MagicMock()
    s.key = key
    s.value = value
    s.encrypted = True
    return s


def _make_plain_setting(key: str, value: str) -> MagicMock:
    s = MagicMock()
    s.key = key
    s.value = value
    s.encrypted = False
    return s


def _make_session_ctx(settings_list: list[MagicMock]) -> Any:
    """Return an async context manager yielding a session with scalars returning given settings."""
    session_mock = AsyncMock()
    scalars_mock = MagicMock()
    scalars_mock.all = MagicMock(return_value=settings_list)
    execute_result = MagicMock()
    execute_result.scalars = MagicMock(return_value=scalars_mock)
    session_mock.execute = AsyncMock(return_value=execute_result)

    @asynccontextmanager
    async def ctx():  # type: ignore[return]
        yield session_mock

    return ctx


class TestGetSettingsBrokenCredentialIndicator:
    """get_settings() must render a broken credential distinctly from a valid masked one."""

    @pytest.mark.asyncio
    async def test_broken_credential_returns_indicator_not_mask(self) -> None:
        """When crypto.decrypt raises InvalidToken, result[key] must equal DECRYPT_ERROR_INDICATOR.

        The indicator must NOT equal ENV_VARS_MASK_CHAR — that is the core T7 assertion:
        broken credentials render distinctly from valid masked secrets.
        """
        corrupt_setting = _make_encrypted_setting("git_token", "CORRUPT_CIPHERTEXT")

        def fake_decrypt_fail(ciphertext: str, key_path: str) -> str:
            raise InvalidToken()

        with (
            patch.object(settings_mod, "session", _make_session_ctx([corrupt_setting])),
            patch.object(settings_mod.crypto, "decrypt", side_effect=fake_decrypt_fail),
        ):
            result = await settings_mod.get_settings()

        assert result["git_token"] == DECRYPT_ERROR_INDICATOR
        # Core T7 assertion: broken and valid-but-masked must not be the same string.
        assert DECRYPT_ERROR_INDICATOR != ENV_VARS_MASK_CHAR

    @pytest.mark.asyncio
    async def test_broken_and_valid_settings_render_distinctly(self) -> None:
        """A broken encrypted setting and a valid encrypted setting in one response must differ."""
        corrupt_setting = _make_encrypted_setting("git_token", "CORRUPT_CIPHERTEXT")
        valid_setting = _make_encrypted_setting("dashboard_api_key", "VALID_CIPHERTEXT")

        call_count = 0

        def selective_decrypt(ciphertext: str, key_path: str) -> str:
            nonlocal call_count
            call_count += 1
            if ciphertext == "CORRUPT_CIPHERTEXT":
                raise InvalidToken()
            # Return a plaintext that will be masked.
            return "sk-ant-api-validtoken123456"

        with (
            patch.object(
                settings_mod, "session", _make_session_ctx([corrupt_setting, valid_setting])
            ),
            patch.object(settings_mod.crypto, "decrypt", side_effect=selective_decrypt),
        ):
            result = await settings_mod.get_settings()

        # Broken key must show the error indicator.
        assert result["git_token"] == DECRYPT_ERROR_INDICATOR
        # Valid key must show a masked value (contains "*") — not the error indicator.
        assert result["dashboard_api_key"] != DECRYPT_ERROR_INDICATOR
        assert "*" in result["dashboard_api_key"]

    @pytest.mark.asyncio
    async def test_non_invalid_token_exception_propagates(self) -> None:
        """A non-InvalidToken exception from crypto.decrypt must propagate (Fail Fast).

        get_settings() must NOT swallow programming errors into the indicator.
        """
        corrupt_setting = _make_encrypted_setting("git_token", "CORRUPT_CIPHERTEXT")

        def fake_decrypt_key_error(ciphertext: str, key_path: str) -> str:
            raise KeyError("unexpected internal failure")

        with (
            patch.object(settings_mod, "session", _make_session_ctx([corrupt_setting])),
            patch.object(settings_mod.crypto, "decrypt", side_effect=fake_decrypt_key_error),
        ):
            with pytest.raises(KeyError):
                await settings_mod.get_settings()
