from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

BASE_DIR = Path(__file__).resolve().parent.parent
for env_path in (BASE_DIR / ".env", BASE_DIR / "backend" / ".env"):
    if env_path.exists():
        load_dotenv(env_path)

DATABASE_URL = (
    os.getenv("DATABASE_URL")
    or os.getenv("SUPABASE_DB_URL")
    or "sqlite:///./cosmetics.db"
)

engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
