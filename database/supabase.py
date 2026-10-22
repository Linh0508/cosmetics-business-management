from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

try:
    from supabase import Client, create_client
except ImportError:  # pragma: no cover - optional dependency until installed
    Client = Any
    create_client = None

BASE_DIR = Path(__file__).resolve().parent.parent
for env_path in (BASE_DIR / ".env", BASE_DIR / "backend" / ".env"):
    if env_path.exists():
        load_dotenv(env_path)

SUPABASE_URL = (os.getenv("SUPABASE_URL") or "").strip()
SUPABASE_ANON_KEY = (
    os.getenv("SUPABASE_ANON_KEY")
    or os.getenv("SUPABASE_PUBLISHABLE_KEY")
    or ""
).strip()
SUPABASE_SERVICE_ROLE_KEY = (
    os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    or os.getenv("SUPABASE_SECRET_KEY")
    or ""
).strip()


def _looks_like_placeholder(value: str) -> bool:
    value_norm = value.lower()
    return "your-" in value_norm or "replace" in value_norm or "example" in value_norm or "placeholder" in value_norm or not value


def get_supabase_client(use_service_role: bool = True) -> Client | None:
    if create_client is None:
        return None

    url = SUPABASE_URL
    key = SUPABASE_SERVICE_ROLE_KEY if use_service_role else SUPABASE_ANON_KEY

    if _looks_like_placeholder(url) or _looks_like_placeholder(key):
        return None

    return create_client(url, key)


supabase: Client | None = get_supabase_client(use_service_role=True)
