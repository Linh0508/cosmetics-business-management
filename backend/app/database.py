"""Backward-compatible import shim for the database layer.

The real database configuration now lives under the repository-level database folder.
"""

from database.supabase import *

__all__ = [
    "SUPABASE_URL",
    "SUPABASE_ANON_KEY",
    "SUPABASE_SERVICE_ROLE_KEY",
    "get_supabase_client",
    "supabase",
]
