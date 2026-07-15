"""Verify the /api/models payload contract the frontend depends on.

The dashboard fetches its model list from /api/models at runtime, so
common.constants.SUPPORTED_MODELS is the single source of truth — there is no
TypeScript model list to keep in sync. This test guards the payload shape the
frontend's ModelInfo interface (dashboard/frontend/lib/api.ts) consumes:
every model carries the same fields, the ids match VALID_MODELS, and the
default is a real model.
"""

import re
from pathlib import Path

from common.constants import MODEL_PROVIDER_SLUGS, SUPPORTED_MODELS, VALID_MODELS, DEFAULT_MODEL

# Fields the frontend ModelInfo interface reads off each model. A model is no
# longer tied to one provider/api_model here — provider routing lives in
# MODEL_PROVIDER_SLUGS and is offered per run.
_REQUIRED_MODEL_FIELDS = {
    "id",
    "label",
    "short",
    "description",
    "context",
    "tier",
    "family",
}

TS_API_PATH = Path("dashboard/frontend/lib/api.ts")


class TestModelPayloadContract:
    """SUPPORTED_MODELS must satisfy the frontend's ModelInfo contract."""

    def test_every_model_has_required_fields(self) -> None:
        """Each model dict must carry exactly the fields the frontend reads."""
        for model in SUPPORTED_MODELS:
            assert set(model.keys()) == _REQUIRED_MODEL_FIELDS, (
                f"Model {model.get('id')!r} fields {set(model.keys())} "
                f"!= required {_REQUIRED_MODEL_FIELDS}"
            )

    def test_model_ids_match_valid_models(self) -> None:
        """The ids in SUPPORTED_MODELS must equal VALID_MODELS exactly."""
        payload_ids = {m["id"] for m in SUPPORTED_MODELS}
        assert payload_ids == set(VALID_MODELS)

    def test_default_is_a_known_model(self) -> None:
        """DEFAULT_MODEL must be one of the served models."""
        assert DEFAULT_MODEL in {m["id"] for m in SUPPORTED_MODELS}

    def test_every_model_has_provider_slugs(self) -> None:
        """Every served model must have a MODEL_PROVIDER_SLUGS routing entry,
        and every routing entry must correspond to a served model — so no model
        ships without provider routing and no orphan routing lingers."""
        payload_ids = {m["id"] for m in SUPPORTED_MODELS}
        assert payload_ids == set(MODEL_PROVIDER_SLUGS)

    def test_ts_modelinfo_fields_match_payload(self) -> None:
        """The TypeScript ModelInfo interface must declare exactly the fields
        the backend sends — otherwise the frontend silently drops or expects
        fields that don't exist."""
        content = TS_API_PATH.read_text(encoding="utf-8")
        match = re.search(r"export interface ModelInfo\s*\{(.*?)\}", content, re.DOTALL)
        assert match, "ModelInfo interface not found in api.ts"
        ts_fields = set(re.findall(r"(\w+)\s*:", match.group(1)))
        assert ts_fields == _REQUIRED_MODEL_FIELDS, (
            f"ModelInfo fields {ts_fields} != backend payload {_REQUIRED_MODEL_FIELDS}"
        )
