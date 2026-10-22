from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv


ROOT = Path(__file__).resolve().parent.parent
for env_file in (ROOT / ".env", ROOT / "backend" / ".env"):
    if env_file.exists():
        load_dotenv(env_file)

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


def main() -> int:
    print("=== Supabase connection test ===")
    print(f"URL: {SUPABASE_URL}")
    print(f"Anon key loaded: {bool(SUPABASE_ANON_KEY)}")
    print(f"Service role key loaded: {bool(SUPABASE_SERVICE_ROLE_KEY)}")

    if not SUPABASE_URL:
        print("ERROR: SUPABASE_URL is missing.")
        return 1

    key = SUPABASE_SERVICE_ROLE_KEY or SUPABASE_ANON_KEY
    if not key:
        print("ERROR: No Supabase key was found in environment variables.")
        return 1

    try:
        from supabase import create_client

        client = create_client(SUPABASE_URL, key)
        try:
            response = client.auth.get_session()
            print("RESULT: Supabase API reachable.")
            print(f"Session response type: {type(response).__name__}")
            return 0
        except Exception as exc:
            print(f"API reachable, auth call returned: {type(exc).__name__}: {exc}")
            return 0
    except Exception as exc:
        print(f"ERROR: Cannot create Supabase client: {type(exc).__name__}: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
