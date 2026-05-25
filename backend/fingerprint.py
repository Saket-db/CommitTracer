from __future__ import annotations

import hashlib
import json
from typing import Any


def canonical_json(data: Any) -> str:
    """Return a deterministic JSON string for hashing and comparison."""
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def compute_payload_hash(data: Any) -> str:
    """Return a SHA-256 fingerprint for a JSON-serializable value."""
    return hashlib.sha256(canonical_json(data).encode("utf-8")).hexdigest()
