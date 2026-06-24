"""Shared env setup for the tests/slow suite.

Importing sandbox modules pulls in sandbox/constants.py, which reads
AF_SANDBOX_PORT (and friends) at import time. Seed the same test defaults
as tests/fast/conftest.py so slow tests collect standalone, not only when
run alongside the fast suite.
"""

import os

os.environ.setdefault("AGENT_INTERNAL_SECRET", "test-secret")
os.environ.setdefault("AF_IMAGE_TAG", "test")
os.environ.setdefault("AF_SANDBOX_PORT", "8923")
os.environ.setdefault("SANDBOX_INTERNAL_SECRET", "test-sandbox-secret")
